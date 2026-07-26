::: {#414141947 .myid}
[]{#_Toc404789582}[]{#struct_0_x6797_42255_x572081993}[]{#_Toc299461496}[]{#_Toc94588230}[]{#_Toc80176777}

**IGMP \-- IGMP配置命令 \-- display igmp group**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **igmp** **group**]{lang="EN-US"}]{#struct_0_x6797_42255_2035780856}[命令用来显示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组（即通过]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[加入的组播组）的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_249235582}

[**[display]{lang="EN-US"}**[ **igmp** \[ **vpn-instance** *vpn-instance-name* \] **group** \[ *group-address* \| **interface** *interface-type interface-number* \] \[ **static** \| **verbose** \]]{lang="EN-US"}]{#struct_0_x6797_42255_1370073436}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1521592739}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1879912946}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x379537443}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1728661867}

[[network-operator]{lang="EN-US"}]{#struct_0_x6797_42255_x120674254}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_538521393}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6797_42255_668594706}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1792624538}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6797_42255_812268999}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_x6797_42255_x1190762845}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x6797_42255_x996737729}[：显示指定接口上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:
宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_x6797_42255_2033162981}[：显示静态加入的组播组信息。如果未指定本参数，将只显示动态加入的组播组信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x6797_42255_x1879978482}[：显示详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1225775422}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1510790576}[显示公网实例中动态加入的所有]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp group]{lang="EN-US"}]{#struct_0_x6797_42255_1815545020}

[IGMP groups in total: 3]{lang="EN-US"}

[ GigabitEthernet1/0/1(10.10.1.20):]{lang="EN-US"}

[  IGMP groups reported in total: 3]{lang="EN-US"}

[   Group address   Last reporter   Uptime      Expires]{lang="EN-US"}

[   225.1.1.1       10.10.1.10      00:02:04    00:01:15]{lang="EN-US"}

[   225.1.1.2       10.10.1.10      00:02:04    00:01:15]{lang="EN-US"}

[   225.1.1.3       10.10.1.10      00:02:04    00:01:15]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display igmp group]{lang="EN-US"}]{#struct_0_x6797_42255_x48687360}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1508244852}[[字段]{style="font-family:黑体"}]{#struct_0_x6797_42255_948097235}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1774801614}

[[IGMP groups in total]{lang="EN-US"}]{#struct_0_x6797_42255_x47835392}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x957909317}[组播组的总数]{style="font-family:宋体"}

[[IGMP groups reported in total]{lang="EN-US"}]{#struct_0_x6797_42255_1268392748}

[[当前接口上动态加入的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x2093073119}[组播组总数]{style="font-family:宋体"}

[[Group address]{lang="EN-US"}]{#struct_0_x6797_42255_x839144281}

[[组播组地址]{style="font-family:宋体"}]{#struct_0_x6797_42255_1207177116}

[[Last reporter]{lang="EN-US"}]{#struct_0_x6797_42255_x47769856}

[[最后发送报告报文的主机地址]{style="font-family:宋体"}]{#struct_0_x6797_42255_2030525931}

[[Uptime]{lang="EN-US"}]{#struct_0_x6797_42255_521585075}

[[组播组的运行时间]{style="font-family:宋体"}]{#struct_0_x6797_42255_734065332}

[[Expires]{lang="EN-US"}]{#struct_0_x6797_42255_2063119505}

[[组播组的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}]{#struct_0_x6797_42255_x48359681}[表示该定时器关闭]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x2131271087}[显示公网实例中动态加入的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组]{style="font-family:宋体"}[232.1.1.1]{lang="EN-US"}[的详细信息（假设当前运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> display igmp group 232.1.1.1 verbose]{lang="EN-US"}]{#struct_0_x6797_42255_x1880437233}

[ GigabitEthernet1/0/1(10.10.1.20):]{lang="EN-US"}

[  IGMP groups reported in total: 3]{lang="EN-US"}

[   Group: 232.1.1.1]{lang="EN-US"}

[     Uptime: 00:00:34]{lang="EN-US"}

[     Exclude expires: 00:04:16]{lang="EN-US"}

[     Mapping expires: 00:02:16]{lang="EN-US"}

[     Last reporter: 10.10.1.10]{lang="EN-US"}

[     Last-member-query-counter: 0]{lang="EN-US"}

[     Last-member-query-timer-expiry: Off]{lang="EN-US"}

[     Mapping last-member-query-counter: 0]{lang="EN-US"}

[     Mapping last-member-query-timer-expiry: Off]{lang="EN-US"}

[     Group mode: Exclude]{lang="EN-US"}

[     Version1-host-present-timer-expiry: Off]{lang="EN-US"}

[     Version2-host-present-timer-expiry: 00:02:11]{lang="EN-US"}

[     Mapping version1-host-present-timer-expiry: Off]{lang="EN-US"}

[     Source list (sources in total: 1):]{lang="EN-US"}

[       Source: 10.1.1.1]{lang="EN-US"}

[          Uptime: 00:00:03]{lang="EN-US"}

[          V3 expires: 00:04:16]{lang="EN-US"}

[          Mapping expires: 00:02:16]{lang="EN-US"}

[          Last-member-query-counter: 0]{lang="EN-US"}

[          Last-member-query-timer-expiry: Off]{lang="EN-US"}

[]{#struct_0_x6797_42255_x1165210769}[]{#_Toc94671227}[]{#_Toc80176856}[]{#_Toc80175838}[]{#_Toc17344296}[[表1-2 ]{lang="EN-US"}[display igmp group]{lang="EN-US"}]{#_Toc16220259}[ verbose]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_452608648}[[字段]{style="font-family:黑体"}]{#struct_0_x6797_42255_659772389}

[[描述]{style="font-family:黑体"}]{#struct_0_x6797_42255_2043665480}

[[IGMP groups reported in total]{lang="EN-US"}]{#struct_0_x6797_42255_1096669630}

[[当前接口上动态加入的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1880502769}[组播组总数]{style="font-family:宋体"}

[[Group]{lang="EN-US"}]{#struct_0_x6797_42255_x1546452255}

[[组播组地址]{style="font-family:宋体"}]{#struct_0_x6797_42255_1795194028}

[[Uptime]{lang="EN-US"}]{#struct_0_x6797_42255_1142669488}

[[组播组的运行时间]{style="font-family:宋体"}]{#struct_0_x6797_42255_1263492367}

[[Exclude expires]{lang="EN-US"}]{#struct_0_x6797_42255_x1880306161}

[[EXCLUDE]{lang="EN-US"}]{#struct_0_x6797_42255_x641423429}[模式下组播组的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

 

[[Mapping expires]{lang="EN-US"}]{#struct_0_x6797_42255_1687545460}

[[IGMP SSM Mapping]{lang="EN-US"}]{#struct_0_x6797_42255_x1123566125}[规则所生成组播组的超时时间。只有运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Last reporter]{lang="EN-US"}]{#struct_0_x6797_42255_51879092}

[[最后发送报告报文的主机地址]{style="font-family:宋体"}]{#struct_0_x6797_42255_882652909}

[[Last-member-query-counter]{lang="EN-US"}]{#struct_0_x6797_42255_x740006258}

[[最后组成员查询次数]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1323346748}

[[Last-member-query-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_x1880371697}

[[最后组成员查询定时器的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}]{#struct_0_x6797_42255_x1626428829}[表示该定时器关闭]{style="font-family:宋体"}

[[Mapping last-member-query-counter]{lang="EN-US"}]{#struct_0_x6797_42255_1687938676}

[[IGMP SSM Mapping]{lang="EN-US"}]{#struct_0_x6797_42255_1667354999}[规则所生成组播组的最后组成员查询次数。只有运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Mapping last-member-query-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_1688004212}

[[IGMP SSM Mapping]{lang="EN-US"}]{#struct_0_x6797_42255_630409694}[规则所生成组播组的最后组成员查询定时器的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭。只有运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Group mode]{lang="EN-US"}]{#struct_0_x6797_42255_x324681342}

[[对组播源的过滤模式：]{style="font-family:宋体"}]{#struct_0_x6797_42255_x271681991}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Include]{lang="EN-US"}]{#struct_0_x6797_42255_x1766486483}[：表示]{lang="EN-US" style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Exclude]{lang="EN-US"}]{#struct_0_x6797_42255_x259228428}[：表示]{lang="EN-US" style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[IGMPv1/v2]{lang="EN-US"}]{#struct_0_x6797_42255_672144470}[本身并不区分过滤模式，但当运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时，会根据具体配置以及加入的组播组来显示相应的模式；而当未运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时，则固定显示为]{style="font-family:宋体"}[Exclude]{lang="EN-US"}

[[Version1-host-present-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_x1880175089}

[[IGMPv1]{lang="EN-US"}]{#struct_0_x6797_42255_67670939}[主机超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭。只有运行]{style="font-family:宋体"}[IGMPv2]{lang="EN-US"}[或]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Version2-host-present-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_x1438998277}

[[IGMPv2]{lang="EN-US"}]{#struct_0_x6797_42255_x686361207}[主机超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭。只有运行]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Mapping version1-host-present-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_1687283315}

[[运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}]{#struct_0_x6797_42255_1989083929}[时]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[主机的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭。只有运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Source list (sources in total: 1)]{lang="EN-US"}]{#struct_0_x6797_42255_1213184323}

[[组播源列表及总数。只有运行]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}]{#struct_0_x6797_42255_x1880240625}[或]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_x6797_42255_x48621830}

[[组播源地址。只有运行]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}]{#struct_0_x6797_42255_595435376}[或]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_x6797_42255_x48556294}

[[组播源的运行时间。只有运行]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}]{#struct_0_x6797_42255_x1986765927}[或]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[V3 expires]{lang="EN-US"}]{#struct_0_x6797_42255_x48752902}

[[IGMPv3]{lang="EN-US"}]{#struct_0_x6797_42255_1380848780}[组播源的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭，"]{style="font-family:宋体"}[\-\--]{lang="EN-US"}["表示该组播源由]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[规则生成。只有运行]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}[或]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Mapping expires]{lang="EN-US"}]{#struct_0_x6797_42255_x48687366}

[[IGMP SSM Mapping]{lang="EN-US"}]{#struct_0_x6797_42255_948097233}[规则所生成组播源的超时时间。只有运行]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Last-member-query-counter]{lang="EN-US"}]{#struct_0_x6797_42255_x47835398}

[[最后源组成员查询次数。只有运行]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}]{#struct_0_x6797_42255_x957909311}[或]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Last-member-query-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_x47769862}

[[最后源组成员查询定时器的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}]{#struct_0_x6797_42255_x308126233}[表示该定时器关闭。只有运行]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}[或]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[]{#_Toc296158434}[]{#_Toc296159749}[]{#_Toc296158436}[]{#_Toc296159751}[]{#_Toc296158437}[]{#_Toc296159752}[]{#_Toc296158438}[]{#_Toc296159753}[]{#_Toc296158439}[]{#_Toc296159754}[]{#_Toc296158440}[]{#_Toc296159755}[]{#_Toc296158441}[]{#_Toc296159756}[]{#_Toc296158442}[]{#_Toc296159757}[]{#_Toc296158443}[]{#_Toc296159758}[]{#_Toc296158444}[]{#_Toc296159759}[]{#_Toc296158445}[]{#_Toc296159760}[]{#_Toc296158446}[]{#_Toc296159761}[]{#_Toc296158447}[]{#_Toc296159762}[]{#_Toc296158448}[]{#_Toc296159763}[]{#_Toc296158449}[]{#_Toc296159764}[]{#_Toc296158450}[]{#_Toc296159765}[]{#_Toc296158451}[]{#_Toc296159766}[]{#_Toc296158452}[]{#_Toc296159767}[]{#_Toc296158453}[]{#_Toc296159768}[]{#_Toc296158454}[]{#_Toc296159769}[]{#_Toc296158455}[]{#_Toc296159770}[]{#_Toc296158456}[]{#_Toc296159771}[]{#_Toc296158457}[]{#_Toc296159772}[]{#_Toc296158458}[]{#_Toc296159773}[]{#_Toc296158459}[]{#_Toc296159774}[]{#_Toc296158460}[]{#_Toc296159775}[]{#_Toc296158461}[]{#_Toc296159776}[]{#_Toc296158462}[]{#_Toc296159777}[]{#_Toc296158463}[]{#_Toc296159778}[]{#_Toc296158464}[]{#_Toc296159779}[]{#_Toc296158465}[]{#_Toc296159780}[]{#_Toc296158469}[]{#_Toc296159784}[]{#_Toc296158476}[]{#_Toc296159791}[]{#_Toc296158477}[]{#_Toc296159792}[]{#_Toc296158478}[]{#_Toc296159793}[]{#_Toc296158487}[]{#_Toc296159802}[]{#_Toc296158488}[]{#_Toc296159803}[]{#_Toc296158534}[]{#_Toc296159849}[]{#_Toc296158536}[]{#_Toc296159851}[]{#_Toc296158537}[]{#_Toc296159852}[]{#_Toc296158538}[]{#_Toc296159853}[]{#_Toc296158539}[]{#_Toc296159854}[]{#_Toc296158540}[]{#_Toc296159855}[]{#_Toc296158541}[]{#_Toc296159856}[]{#_Toc296158542}[]{#_Toc296159857}[]{#_Toc296158543}[]{#_Toc296159858}[]{#_Toc296158544}[]{#_Toc296159859}[]{#_Toc296158545}[]{#_Toc296159860}[]{#_Toc296158546}[]{#_Toc296159861}[]{#_Toc296158547}[]{#_Toc296159862}[]{#_Toc296158548}[]{#_Toc296159863}[]{#_Toc296158549}[]{#_Toc296159864}[]{#_Toc296158550}[]{#_Toc296159865}[]{#_Toc296158551}[]{#_Toc296159866}[]{#_Toc296158552}[]{#_Toc296159867}[]{#_Toc296158553}[]{#_Toc296159868}[]{#_Toc296158554}[]{#_Toc296159869}[]{#_Toc296158556}[]{#_Toc296159871}[]{#_Toc296158557}[]{#_Toc296159872}[]{#_Toc296158562}[]{#_Toc296159877}[]{#_Toc296158584}[]{#_Toc296159899}[]{#_Toc296158586}[]{#_Toc296159901}[]{#_Toc296158587}[]{#_Toc296159902}[]{#_Toc296158588}[]{#_Toc296159903}[]{#_Toc296158589}[]{#_Toc296159904}[]{#_Toc296158590}[]{#_Toc296159905}[]{#_Toc296158591}[]{#_Toc296159906}[]{#_Toc296158592}[]{#_Toc296159907}[]{#_Toc296158593}[]{#_Toc296159908}[]{#_Toc296158594}[]{#_Toc296159909}[]{#_Toc296158595}[]{#_Toc296159910}[]{#_Toc296158596}[]{#_Toc296159911}[]{#_Toc296158597}[]{#_Toc296159912}[]{#_Toc296158598}[]{#_Toc296159913}[]{#_Toc296158599}[]{#_Toc296159914}[]{#_Toc296158600}[]{#_Toc296159915}[]{#_Toc296158601}[]{#_Toc296159916}[]{#_Toc296158602}[]{#_Toc296159917}[]{#_Toc296158603}[]{#_Toc296159918}[]{#_Toc296158604}[]{#_Toc296159919}[]{#_Toc296158605}[]{#_Toc296159920}[]{#_Toc296158606}[]{#_Toc296159921}[]{#_Toc296158607}[]{#_Toc296159922}[]{#_Toc296158608}[]{#_Toc296159923}[]{#_Toc296158609}[]{#_Toc296159924}[]{#_Toc296158610}[]{#_Toc296159925}[]{#_Toc296158611}[]{#_Toc296159926}[]{#_Toc296158612}[]{#_Toc296159927}[]{#_Toc296158613}[]{#_Toc296159928}[]{#_Toc296158614}[]{#_Toc296159929}[]{#_Toc296158615}[]{#_Toc296159930}[]{#_Toc296158625}[]{#_Toc296159940}[]{#_Toc296158626}[]{#_Toc296159941}[]{#_Toc296158648}[]{#_Toc296159963}[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x48359687}[显示公网实例中静态加入的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp group static]{lang="EN-US"}]{#struct_0_x6797_42255_x1904726524}

[ Entries in total: 2]{lang="EN-US"}

[   Group address   Source address  Interface           Expires]{lang="EN-US"}

[   225.1.1.1       0.0.0.0         GE1/0/1             Never]{lang="EN-US"}

[   225.2.2.2       1.1.1.1         GE1/0/1             Never]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display igmp group static]{lang="EN-US"}]{#struct_0_x6797_42255_x48294151}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1187793468}[[字段]{style="font-family:黑体"}]{#struct_0_x6797_42255_2004466155}

[[描述]{style="font-family:黑体"}]{#struct_0_x6797_42255_x816709344}

[[Entries in total]{lang="EN-US"}]{#struct_0_x6797_42255_x48490759}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_660775721}[组播组的总数]{style="font-family:宋体"}

[[Group address]{lang="EN-US"}]{#struct_0_x6797_42255_x48425223}

[[组播组地址]{style="font-family:宋体"}]{#struct_0_x6797_42255_721378063}

[[Source address]{lang="EN-US"}]{#struct_0_x6797_42255_x48621831}

[[组播源地址]{style="font-family:宋体"}]{#struct_0_x6797_42255_595435375}

[[Interface]{lang="EN-US"}]{#struct_0_x6797_42255_x163269020}

[[接口名称]{style="font-family:宋体"}]{#struct_0_x6797_42255_x48556295}

[[Expires]{lang="EN-US"}]{#struct_0_x6797_42255_x1986765926}

[[组播组的超时时间，固定显示为]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x6797_42255_x48752903}[，表示永不超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc299461497}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_590917616}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **igmp** **group**]{lang="EN-US"}]{#struct_0_x6797_42255_746454007}

::: {#1261885225 .myid}
[]{#_Toc404789583}[]{#struct_0_x6797_42255_x1136838230}

**IGMP \-- IGMP配置命令 \-- display igmp interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **igmp** **interface**]{lang="EN-US"}]{#struct_0_x6797_42255_x1880044017}[命令用来显示接口上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[配置和运行的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_591589354}

[**[display]{lang="EN-US"}**[ **igmp** \[ **vpn-instance** *vpn-instance-name* \] **interface** \[ *interface-type interface-number* \] \[ **host** \| **proxy** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x6797_42255_1211340004}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1390871880}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1300045038}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_295778796}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x644290502}

[[network-operator]{lang="EN-US"}]{#struct_0_x6797_42255_2083197099}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1656436632}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6797_42255_1215075599}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1880109553}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6797_42255_x1491234579}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6797_42255_x1121342975}[：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[**[host]{lang="EN-US"}**]{#struct_0_x6797_42255_2120094494}[：显示主机接口（即使能了]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[主机行为的接口）的信息。如果未指定本参数，将显示所有接口的信息。有关]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[主机行为的详细介绍，请参见"]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}["。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[proxy]{lang="EN-US"}**]{#struct_0_x6797_42255_688572680}[：显示代理接口的信息。如果未指定本参数，将显示所有接口的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x6797_42255_x127988329}[：显示详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1831688557}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_937721612}[显示公网实例接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（非代理接口）上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[配置和运行的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp interface gigabitethernet 1/0/1 verbose]{lang="EN-US"}]{#struct_0_x6797_42255_x1879912945}

[ GigabitEthernet1/0/1(10.10.1.20):]{lang="EN-US"}

[   IGMP is enabled.]{lang="EN-US"}

[   IGMP version: 2]{lang="EN-US"}

[   Query interval for IGMP: 125s]{lang="EN-US"}

[   Other querier present time for IGMP: 255s]{lang="EN-US"}

[   Maximum query response time for IGMP: 10s]{lang="EN-US"}

[   Last member query interval: 1s]{lang="EN-US"}

[   Last member query count: 2]{lang="EN-US"}

[   Startup query interval: 31s]{lang="EN-US"}

[   Startup query count: 2]{lang="EN-US"}

[   General query timer expiry (hh:mm:ss): 00:00:54]{lang="EN-US"}

[   Querier for IGMP: 10.10.1.20 (This router)]{lang="EN-US"}

[   IGMP activity: 1 join(s), 0 leave(s)]{lang="EN-US"}

[   Multicast routing on this interface: Enabled]{lang="EN-US"}

[   Robustness: 2]{lang="EN-US"}

[   Require-router-alert: Disabled]{lang="EN-US"}

[   Fast-leave: Disabled]{lang="EN-US"}

[   Startup-query: Off]{lang="EN-US"}

[   Other-querier-present-timer-expiry (hh:mm:ss): \--:\--:\--]{lang="EN-US"}

[   Authorization: Disabled]{lang="EN-US"}

[   Join-by-session: Disabled]{lang="EN-US"}

[   User-VLAN-aggregation: Disabled]{lang="EN-US"}

[  IGMP groups reported in total: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_688507144}[显示公网实例所有代理接口上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[配置和运行的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp interface proxy verbose]{lang="EN-US"}]{#struct_0_x6797_42255_688441608}

[ GigabitEthernet1/0/2(20.10.1.20):]{lang="EN-US"}

[   IGMP proxy is enabled.]{lang="EN-US"}

[   IGMP version: 2]{lang="EN-US"}

[   Multicast routing on this interface: Enabled]{lang="EN-US"}

[   Require-router-alert: Disabled]{lang="EN-US"}

[   Version1-querier-present-timer-expiry (hh:mm:ss): \--:\--:\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_2119570203}[显示公网实例所有主机接口上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[配置和运行的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp interface host verbose]{lang="EN-US"}]{#struct_0_x6797_42255_x1189349177}

[ GigabitEthernet1/0/3(30.10.1.20):]{lang="EN-US"}

[   IGMP host is enabled.]{lang="EN-US"}

[   IGMP version: 2]{lang="EN-US"}

[   Multicast routing on this interface: Enabled]{lang="EN-US"}

[   Require-router-alert: Disabled]{lang="EN-US"}

[   Version1-querier-present-timer-expiry (hh:mm:ss): \--:\--:\--]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display igmp interface]{lang="EN-US"}]{#struct_0_x6797_42255_x1945621384}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_447977824}[[字段]{style="font-family:黑体"}]{#struct_0_x6797_42255_676414292}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6797_42255_465444633}

[[GigabitEthernet1/0/1(10.10.1.20)]{lang="EN-US"}]{#struct_0_x6797_42255_x1225370384}

[[接口的名称和]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6797_42255_x198116990}[地址]{style="font-family:宋体"}

[[IGMP is enabled]{lang="EN-US"}]{#struct_0_x6797_42255_x1879978481}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1629059949}[已使能]{style="font-family:宋体"}

[[IGMP version]{lang="EN-US"}]{#struct_0_x6797_42255_x1083552426}

[[此接口运行的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x2113939949}[版本]{style="font-family:宋体"}

[[Query interval for IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1956177378}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_2080830648}[普遍组查询报文的发送间隔（秒）]{style="font-family:宋体"}

[[Other querier present time for IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1880437236}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1924725656}[其它查询器的存在时间（秒）]{style="font-family:宋体"}

[[Maximum query response time for IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_2121804976}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_2142917618}[普遍组查询报文的最大响应时间（秒）]{style="font-family:宋体"}

[[Last member query interval]{lang="EN-US"}]{#struct_0_x6797_42255_2094132996}

[[最后组成员查询间隔（秒）]{style="font-family:宋体"}]{#struct_0_x6797_42255_x806395236}

[[Last member query count]{lang="EN-US"}]{#struct_0_x6797_42255_x717595699}

[[最后组成员查询次数]{style="font-family:宋体"}]{#struct_0_x6797_42255_167915605}

[[Startup query interval]{lang="EN-US"}]{#struct_0_x6797_42255_1918711819}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1880502772}[查询器启动查询间隔（秒）]{style="font-family:宋体"}

[[Startup query count]{lang="EN-US"}]{#struct_0_x6797_42255_x1593571958}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1663981565}[查询器启动查询次数]{style="font-family:宋体"}

[[General query timer expiry]{lang="EN-US"}]{#struct_0_x6797_42255_362137413}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x829269871}[普遍组查询的超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

[[Querier for IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1880306164}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x238138902}[查询器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。当本设备运行]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[且不是]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[查询器时，将不会显示本字段]{style="font-family:宋体"}

[[IGMPv1]{lang="EN-US"}]{#struct_0_x6797_42255_x451775281}[查询器由]{style="font-family:宋体"}[PIM DR]{lang="EN-US"}[来担任，可通过]{style="font-family:宋体"}**[display pim interface]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}

[[No querier elected]{lang="EN-US"}]{#struct_0_x6797_42255_1687414386}

[[没有进行]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1524872863}[查询器选举。只有本设备运行]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[且不是]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[查询器时才会显示本字段]{style="font-family:宋体"}

[[IGMPv1]{lang="EN-US"}]{#struct_0_x6797_42255_1687479922}[查询器由]{style="font-family:宋体"}[PIM DR]{lang="EN-US"}[来担任，可通过]{style="font-family:宋体"}**[display pim interface]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}

[[IGMP activity: 1 join(s), 0 leave(s)]{lang="EN-US"}]{#struct_0_x6797_42255_1666549480}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_2128683763}[的活动统计：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[join(s)]{lang="EN-US"}]{#struct_0_x6797_42255_1134855540}[：表示加入过的组播组]{lang="EN-US" style="font-family:宋体"}[总数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[leave(s)]{lang="EN-US"}]{#struct_0_x6797_42255_x1880371700}[：表示离开过的组播组]{lang="EN-US" style="font-family:宋体"}[总数]{style="font-family:宋体"}

[[Multicast routing on this interface]{lang="EN-US"}]{#struct_0_x6797_42255_746813989}

[[是否使能]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6797_42255_x674756109}[组播路由功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6797_42255_1557118531}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6797_42255_x1467561526}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Robustness]{lang="EN-US"}]{#struct_0_x6797_42255_x1880175092}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1854708898}[查询器的健壮系数]{style="font-family:宋体"}

[[Require-router-alert]{lang="EN-US"}]{#struct_0_x6797_42255_2018372870}

[[是否使能丢弃未携带]{style="font-family:宋体"}[Router-Alert]{lang="EN-US"}]{#struct_0_x6797_42255_x1783492920}[选项的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6797_42255_901296613}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6797_42255_x1880240628}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Fast-leave]{lang="EN-US"}]{#struct_0_x6797_42255_x342864455}

[[是否使能快速离开功能：]{style="font-family:宋体"}]{#struct_0_x6797_42255_14499681}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6797_42255_x1318070038}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6797_42255_x1880044020}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Startup-query]{lang="EN-US"}]{#struct_0_x6797_42255_x1087950052}

[[是否处于启动查询状态：]{style="font-family:宋体"}]{#struct_0_x6797_42255_x420936665}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x6797_42255_865343617}[：表示处于启动查询状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x6797_42255_x1879912948}[：表示未处于启动查询状态]{style="font-family:宋体"}

[[Other-querier-present-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_x1542336857}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x178478462}[其它查询器的存在超时时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

[[Authorization]{lang="EN-US"}]{#struct_0_x6797_42255_x717726771}

[[是否使能可控组播功能：]{style="font-family:宋体"}]{#struct_0_x6797_42255_x717792307}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6797_42255_2130045321}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6797_42255_1454621077}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x6797_42255_x451119921}

[[Join-by-session]{lang="EN-US"}]{#struct_0_x6797_42255_x717333555}

[[是否使能按会话记录加入组播组的用户功能：]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1002670971}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6797_42255_x717399091}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6797_42255_x653917553}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x6797_42255_x451054385}

[[User-VLAN-aggregation]{lang="EN-US"}]{#struct_0_x6797_42255_1614004907}

[[是否使能边缘复制时封装]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x6797_42255_x717857844}[功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6797_42255_1657948087}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6797_42255_1718208713}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x6797_42255_x451644210}

[[IGMP groups reported in total]{lang="EN-US"}]{#struct_0_x6797_42255_x1906392460}

[[此接口上动态加入的组播组数量。没有加入组时不显示本字段]{style="font-family:宋体"}]{#struct_0_x6797_42255_1051309961}

[[IGMP proxy is enabled]{lang="EN-US"}]{#struct_0_x6797_42255_688769287}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_688703751}[代理功能已使能]{style="font-family:宋体"}

[[IGMP host is enabled]{lang="EN-US"}]{#struct_0_x6797_42255_2119701275}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_387941359}[主机行为功能已使能。本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Version1-querier-present-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_688638215}

[[IGMPv1]{lang="EN-US"}]{#struct_0_x6797_42255_208891927}[查询器的存在超时时间]{style="font-family:宋体"}

[[Version2-querier-present-timer-expiry]{lang="EN-US"}]{#struct_0_x6797_42255_688572679}

[[IGMPv2]{lang="EN-US"}]{#struct_0_x6797_42255_688507143}[查询器的存在超时时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1417563709 .myid}
[]{#_Toc404789584}[]{#struct_0_x6797_42255_x1280258421}[]{#_Toc355963320}

**IGMP \-- IGMP配置命令 \-- display igmp proxy group**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **igmp** **proxy** **group**]{lang="EN-US"}]{#struct_0_x6797_42255_x1464913973}[命令用来显示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理记录的组播组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_26739083}

[**[display]{lang="EN-US"}**[ **igmp** \[ **vpn-instance** *vpn-instance-name* \] **proxy** **group** \[ *group-address* \| **interface** *interface-type* *interface-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x6797_42255_688441607}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x87080282}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_43576379}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1363745670}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_688376071}

[[network-operator]{lang="EN-US"}]{#struct_0_x6797_42255_1589860581}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_608663153}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6797_42255_49073505}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_689359111}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6797_42255_1687610994}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_x6797_42255_x184957497}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x6797_42255_x1614240983}[：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x6797_42255_1678478551}[：显示详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2113507239}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_689293575}[显示公网实例中]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理记录的所有组播组信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp proxy group]{lang="EN-US"}]{#struct_0_x6797_42255_1335007651}

[IGMP proxy group records in total: 2]{lang="EN-US"}

[ GigabitEthernet1/0/1(1.1.1.20):]{lang="EN-US"}

[  IGMP proxy group records in total: 2]{lang="EN-US"}

[   Group address      Member state      Expires]{lang="EN-US"}

[   225.1.1.1          Delay             00:00:02]{lang="EN-US"}

[   225.1.1.2          Idle              Off]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x1301366963}[显示公网实例中]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理记录的组播组]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp proxy group 225.1.1.1 verbose]{lang="EN-US"}]{#struct_0_x6797_42255_688834822}

[ GigabitEthernet1/0/1(1.1.1.20):]{lang="EN-US"}

[  IGMP proxy group records in total: 2]{lang="EN-US"}

[   Group: 225.1.1.1]{lang="EN-US"}

[     Group mode: Include]{lang="EN-US"}

[     Member state: Delay]{lang="EN-US"}

[     Expires: 00:00:02]{lang="EN-US"}

[     Source list (sources in total: 1):]{lang="EN-US"}

[       1.1.1.1]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display igmp proxy group]{lang="EN-US"}]{#struct_0_x6797_42255_x1133398924}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1567769352}[[字段]{style="font-family:黑体"}]{#struct_0_x6797_42255_688769286}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6797_42255_185757579}

[[IGMP proxy group records in total]{lang="ES-AR"}]{#struct_0_x6797_42255_688703750}

[[IGMP]{lang="ES-AR"}]{#struct_0_x6797_42255_585938878}[代理记录的组播组总数]{style="font-family:宋体"}

[[GigabitEthernet1/0/1(1.1.1.20)]{lang="EN-US"}]{#struct_0_x6797_42255_688638214}

[[IGMP]{lang="ES-AR"}]{#struct_0_x6797_42255_208891928}[代理接口的名称和]{style="font-family:宋体"}[IP]{lang="ES-AR"}[地址]{style="font-family:宋体"}

[[Pending proxy group]{lang="EN-US"}]{#struct_0_x6797_42255_x1404056316}

[[等待生效的代理组]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1246228691}

[[Group address/Group]{lang="EN-US"}]{#struct_0_x6797_42255_688572678}

[[组播组地址]{style="font-family:宋体"}]{#struct_0_x6797_42255_x501202412}

[[Member state]{lang="EN-US"}]{#struct_0_x6797_42255_2110654346}

[[组播组成员的状态，其中：]{style="font-family:宋体"}]{#struct_0_x6797_42255_688507142}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delay]{lang="EN-US"}]{#struct_0_x6797_42255_x1280258422}[：表示加入了一个组，并对该组启动了延迟发送报告报文的定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x6797_42255_688441606}[：表示加入了一个组，但对该组尚未启动延迟发送报告报文的定时器]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_x6797_42255_x87080283}

[[组播组延迟发送报告报文的时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}]{#struct_0_x6797_42255_688376070}[表示该定时器关闭]{style="font-family:宋体"}

[[Group mode]{lang="ES-AR"}]{#struct_0_x6797_42255_1589860582}

[[对组播源的过滤模式，其中：]{style="font-family:宋体"}]{#struct_0_x6797_42255_689359110}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Include]{lang="EN-US"}]{#struct_0_x6797_42255_x184957496}[：表示]{lang="EN-US" style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Exclude]{lang="EN-US"}]{#struct_0_x6797_42255_689293574}[：表示]{lang="EN-US" style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Source list]{lang="EN-US"}]{#struct_0_x6797_42255_1335007652}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_688834821}[代理的组播组所包含的组播源列表]{style="font-family:宋体"}

[[sources in total]{lang="EN-US"}]{#struct_0_x6797_42255_688769285}

[[组播源的总数]{style="font-family:宋体"}]{#struct_0_x6797_42255_185757582}

[ ]{lang="EN-US"}

::: {#847931979 .myid}
[]{#_Toc404789585}[]{#struct_0_x6797_42255_x1256137371}[]{#_Toc355963321}

**IGMP \-- IGMP配置命令 \-- display igmp proxy routing-table**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **igmp** **proxy** **routing-table**]{lang="EN-US"}]{#struct_0_x6797_42255_688703749}[命令用来显示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理路由表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1370376249}

[**[display]{lang="EN-US"}**[ **igmp** \[ **vpn-instance** *vpn-instance-name* \] **proxy** **routing-table** \[ *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *group-address* \[ **mask** { *mask-length* \| *mask* } \] \] \* \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x6797_42255_1115115999}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1885037264}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_688638213}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_208891925}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1104558438}

[[network-operator]{lang="EN-US"}]{#struct_0_x6797_42255_886753310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_688572677}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6797_42255_x501202407}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2110457737}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6797_42255_x1403794172}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_x6797_42255_688507141}[：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_x6797_42255_x1280258423}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的信息。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x6797_42255_x302114559}[：指定组播组或组播源地址的掩码长度。对于组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；对于组播组地址，其取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x6797_42255_x1031486648}[：指定组播组或组播源地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x6797_42255_688441605}[：显示详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x87080284}

[[\# ]{lang="FR"}]{#struct_0_x6797_42255_43576373}[显示公网实例]{style="font-family:宋体"}[IGMP]{lang="FR"}[代理路由表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp proxy routing-table]{lang="FR"}]{#struct_0_x6797_42255_688376069}

[ Total 1 (\*, G) entries, 2 (S, G) entries.]{lang="FR"}

[ ]{lang="FR"}

[ ]{lang="FR"}[(172.168.0.12, 227.0.0.1)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (1 in total):]{lang="EN-US"}

[         1: Vlan-interface2]{lang="EN-US"}

[             Protocol: IGMP]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (\*, 225.1.1.1)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (1 in total):]{lang="EN-US"}

[         1: Vlan-interface2]{lang="EN-US"}

[             Protocol: STATIC]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (2.2.2.2, 225.1.1.1)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (2 in total):]{lang="EN-US"}

[         1: LoopBack1]{lang="EN-US"}

[             Protocol: STATIC]{lang="EN-US"}

[         2: Vlan-interface2]{lang="EN-US"}

[             Protocol: PROXY]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x366454563}[显示公网实例]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理路由表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp proxy routing-table verbose]{lang="EN-US"}]{#struct_0_x6797_42255_689359109}

[ Total 1 (\*, G) entries, 2 (S, G) entries.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (172.168.0.12, 227.0.0.1)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (1 in total):]{lang="EN-US"}

[         1: Vlan-interface2]{lang="EN-US"}

[             Protocol: IGMP]{lang="EN-US"}

[             Querier state: Querier]{lang="EN-US"}

[             Join/Prune state]{lang="EN-US"}[：]{style="font-family:宋体"}[Join]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Non-downstream interfaces: None]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (\*, 225.1.1.1)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (1 in total):]{lang="EN-US"}

[         1: Vlan-interface2]{lang="EN-US"}

[             Protocol: STATIC]{lang="EN-US"}

[             Querier state: Querier]{lang="EN-US"}

[             Join/Prune state]{lang="EN-US"}[：]{style="font-family:宋体"}[Join]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Non-downstream interfaces (1 in total):]{lang="EN-US"}

[         1: Vlan-interface3]{lang="EN-US"}

[             Protocol: IGMP]{lang="EN-US"}

[             Querier state: Non-querier]{lang="EN-US"}

[             Join/Prune state]{lang="EN-US"}[：]{style="font-family:宋体"}[Join]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (2.2.2.2, 225.1.1.1)]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[     Downstream interfaces (2 in total):]{lang="EN-US"}

[         1: LoopBack1]{lang="EN-US"}

[             Protocol: STATIC]{lang="EN-US"}

[             Querier state: Querier]{lang="EN-US"}

[             Join/Prune state: Join]{lang="EN-US"}

[         2: Vlan-interface2]{lang="EN-US"}

[             Protocol: PROXY]{lang="EN-US"}

[             Querier state: Querier]{lang="EN-US"}

[             Join/Prune state: Join]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Non-downstream interfaces: None]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display igmp proxy routing-table]{lang="EN-US"}]{#struct_0_x6797_42255_x2141272641}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1549655792}[[字段]{style="font-family:黑体"}]{#struct_0_x6797_42255_689293573}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6797_42255_1335007645}

[[Total 1 (\*, G) entries, 2 (S, G) entries]{lang="EN-US"}]{#struct_0_x6797_42255_688834820}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x6797_42255_x1133398926}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项和（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的总数]{style="font-family:宋体"}

[[(172.168.0.12, 227.0.0.1)]{lang="EN-US"}]{#struct_0_x6797_42255_688769284}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x6797_42255_185757581}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Upstream interface]{lang="EN-US"}]{#struct_0_x6797_42255_x1256137368}

[[表项的入接口]{style="font-family:宋体"}]{#struct_0_x6797_42255_688703748}

[[Downstream interfaces (1 in total)]{lang="EN-US"}]{#struct_0_x6797_42255_x1370376250}

[[下游的出接口信息及总数]{style="font-family:宋体"}]{#struct_0_x6797_42255_688638212}

[[Non-downstream interfaces (1 in total)]{lang="EN-US"}]{#struct_0_x6797_42255_208891926}

[[下游的非出接口信息及总数]{style="font-family:宋体"}]{#struct_0_x6797_42255_688572676}

[[1: Vlan-interface2]{lang="EN-US"}]{#struct_0_x6797_42255_x501202406}

[[索引号为]{style="font-family:宋体"}]{#struct_0_x6797_42255_688507140}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}

[[Protocol]{lang="EN-US"}]{#struct_0_x6797_42255_x1280258424}

[[接口使用的协议类型：]{style="font-family:宋体"}]{#struct_0_x6797_42255_688441604}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x87080285}[：表示动态]{style="font-family:宋体"}[IGMP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROXY]{lang="EN-US"}]{#struct_0_x6797_42255_x1403794173}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC]{lang="EN-US"}]{#struct_0_x6797_42255_688376068}[：表示静态]{lang="EN-US" style="font-family:宋体"}[IGMP]{lang="EN-US"}

[[Querier state]{lang="EN-US"}]{#struct_0_x6797_42255_x366454562}

[[接口的查询器状态：]{style="font-family:宋体"}]{#struct_0_x6797_42255_689359108}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Querier]{lang="EN-US"}]{#struct_0_x6797_42255_x2141272640}[：表示接口为]{lang="EN-US" style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Non-querier]{lang="EN-US"}]{#struct_0_x6797_42255_689293572}[：表示接口不是]{lang="EN-US" style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器]{lang="EN-US" style="font-family:宋体"}

[[Join/Prune state]{lang="EN-US"}]{#struct_0_x6797_42255_1335007646}

[[接口的加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6797_42255_x2040048530}[剪枝状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NI]{lang="EN-US"}]{#struct_0_x6797_42255_686210454}[：表示默认状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Join]{lang="EN-US"}]{#struct_0_x6797_42255_x2040114066}[：表示处于]{lang="EN-US" style="font-family:宋体"}[IGMP]{lang="EN-US"}[加入的状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Prune]{lang="EN-US"}]{#struct_0_x6797_42255_x1137504056}[：表示处于]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[剪枝的状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-535323251 .myid}
[]{#_Toc404789586}[]{#struct_0_x6797_42255_x1403663101}[]{#_Toc360705929}

**IGMP \-- IGMP配置命令 \-- display igmp ssm-mapping**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **igmp** **ssm-mapping**]{lang="EN-US"}]{#struct_0_x6797_42255_x1403728637}[命令用来显示]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1880652657}

[**[display]{lang="EN-US"}**[ **igmp** \[ **vpn-instance** *vpn-instance-name* \] **ssm-mapping** *group-address*]{lang="EN-US"}]{#struct_0_x6797_42255_192581109}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403532029}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x512972250}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403597565}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x266281507}

[[network-operator]{lang="EN-US"}]{#struct_0_x6797_42255_x1404056318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1696567385}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6797_42255_x1404121854}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_277076389}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6797_42255_x1403925246}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_x6797_42255_x367398904}[：显示指定组播组的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403990782}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1428925858}[显示公网实例中组播组]{style="font-family:宋体"}[232.1.1.1]{lang="EN-US"}[对应的]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[\<Sysname\> display igmp ssm-mapping 232.1.1.1]{lang="EN-US"}]{#struct_0_x6797_42255_x1403794174}

[ Group: 232.1.1.1]{lang="EN-US"}

[ Source list:]{lang="EN-US"}

[        1.2.3.4]{lang="EN-US"}

[        5.5.5.5]{lang="EN-US"}

[        10.1.1.1]{lang="EN-US"}

[        100.1.1.10]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display igmp ssm-mapping]{lang="EN-US"}]{#struct_0_x6797_42255_1169910078}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x90388792}[[字段]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403859710}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403663102}

[[Group]{lang="EN-US"}]{#struct_0_x6797_42255_x1403728638}

[[组播组地址]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1403532030}

[[Source list]{lang="EN-US"}]{#struct_0_x6797_42255_x1403597566}

[[组播源地址列表]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1404056319}

[ ]{lang="EN-US"}

::::: {#-638550645 .myid}
[]{#_Toc404789587}[]{#struct_0_x6797_42255_x717857845}[]{#_Toc372127316}[]{#_Toc364430855}[]{#_Toc363576219}

**IGMP \-- IGMP配置命令 \-- display igmp user-authorization**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6797_42255_x451578671}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6797_42255_668636997}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **igmp** **user-authorization**]{lang="EN-US"}]{#struct_0_x6797_42255_x717923381}[命令用来显示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[用户的授权信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x614107848}

[**[display]{lang="EN-US"}**[ **igmp** **user-authorization** \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x6797_42255_2065909424}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1230236221}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x161587277}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1469337957}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x717988917}

[[network-operator]{lang="EN-US"}]{#struct_0_x6797_42255_1272018904}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_487886895}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6797_42255_1015380417}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x718054453}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_x6797_42255_x1225219039}[：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_867150760}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_641373521}[显示所有]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[用户的授权信息。]{style="font-family:宋体"}

[[\<Sysname\> display igmp user-authorization]{lang="EN-US"}]{#struct_0_x6797_42255_x717595701}

[ Authorized users in total: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[   User name: user1@isp1]{lang="EN-US"}

[   Access type: PPP]{lang="EN-US"}

[   Interface: Virtual-Access0]{lang="EN-US"}

[   Access interface: Virtual-Access0]{lang="EN-US"}

[   Maximum programs for order: 4]{lang="EN-US"}

[   User profile: profile1]{lang="EN-US"}

[   Authorized programs list:]{lang="EN-US"}

[     225.0.0.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[   User name: user2]{lang="EN-US"}

[   Access type: IPoE]{lang="EN-US"}

[   Interface: Multicast-UA0]{lang="EN-US"}

[   Access interface: GigabitEthernet1/0/1.1]{lang="EN-US"}

[   VLAN ID: 100]{lang="EN-US"}

[   Second VLAN ID: 10]{lang="EN-US"}

[   Maximum programs for order: 4]{lang="EN-US"}

[   User profile: profile1]{lang="EN-US"}

[   Authorized programs list:]{lang="EN-US"}

[     225.0.0.1]{lang="EN-US"}

[     225.0.0.2]{lang="EN-US"}

[     225.0.0.3]{lang="EN-US"}

[ ]{lang="EN-US"}

[   User name: user3]{lang="EN-US"}

[   Access type: Portal]{lang="EN-US"}

[   Interface: Multicast-UA1]{lang="EN-US"}

[   Access interface: GigabitEthernet1/0/2]{lang="EN-US"}

[   Maximum programs for order: 4]{lang="EN-US"}

[   User profile: profile1]{lang="EN-US"}

[   Authorized programs list:]{lang="EN-US"}

[     225.0.0.1]{lang="EN-US"}

[     225.0.0.2]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display igmp user-authorization]{lang="EN-US"}]{#struct_0_x6797_42255_2124755022}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x681354773}[[字段]{style="font-family:黑体"}]{#struct_0_x6797_42255_x717661237}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1422959038}

[[Authorized users in total]{lang="EN-US"}]{#struct_0_x6797_42255_x1339527420}

[[接入用户总数]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1108556229}

[[User name]{lang="EN-US"}]{#struct_0_x6797_42255_x717726773}

[[用户名]{style="font-family:宋体"}]{#struct_0_x6797_42255_x619398154}

[[Access type]{lang="EN-US"}]{#struct_0_x6797_42255_515798830}

[[用户接入的方式：]{style="font-family:宋体"}]{#struct_0_x6797_42255_x717792309}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPoE]{lang="EN-US"}]{#struct_0_x6797_42255_2129389961}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Portal]{lang="EN-US"}]{#struct_0_x6797_42255_x888520659}[：表示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_x6797_42255_x1540209456}[：表示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[方式]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x6797_42255_x717333557}

[[用户接口]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1002539899}

[[Access interface]{lang="EN-US"}]{#struct_0_x6797_42255_x1972120031}

[[用户接入的实际接口]{style="font-family:宋体"}]{#struct_0_x6797_42255_x717399093}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x6797_42255_x654048625}

[[用户带]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x6797_42255_1048614526}[接入时所携带的第一层（或唯一一层）]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Second VLAN ID]{lang="EN-US"}]{#struct_0_x6797_42255_x717857846}

[[用户带]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x6797_42255_1657817015}[接入时所携带的第二层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Maximum programs for order]{lang="EN-US"}]{#struct_0_x6797_42255_x571542580}

[[允许用户加入组播组的最大数量]{style="font-family:宋体"}]{#struct_0_x6797_42255_x717923382}

[[User profile]{lang="EN-US"}]{#struct_0_x6797_42255_x614304456}

[[用户授权的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_x6797_42255_x338975550}[名称，用户可加入该]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下通过]{style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **access-policy**]{lang="EN-US"}[命令所配置接入策略中的组播组]{style="font-family:宋体"}

[[Authorized programs list]{lang="EN-US"}]{#struct_0_x6797_42255_x1957454866}

[[用户授权加入的组播组列表]{style="font-family:宋体"}]{#struct_0_x6797_42255_x717988918}

[ ]{lang="EN-US"}

::: {#1929387136 .myid}
[]{#_Toc404789588}[]{#struct_0_x6797_42255_1032315970}

**IGMP \-- IGMP配置命令 \-- igmp**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**]{#struct_0_x6797_42255_x1404121855}[命令用来进入]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp**]{lang="EN-US"}]{#struct_0_x6797_42255_1843160330}[命令用来清除]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403925247}

[**[igmp]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x6797_42255_1198685037}

[**[undo]{lang="EN-US"}**[ **igmp** \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x6797_42255_x1403990783}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x137158083}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1403794175}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x396173863}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1403859711}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_792674063}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403663103}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6797_42255_x454742548}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403532031}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x156807426}[进入公网实例的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1403597567}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x1429080921}[进入]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1404056320}

[\[Sysname\] igmp vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-igmp-mvpn\]]{lang="EN-US"}
:::

::::: {#1720312761 .myid}
[]{#_Toc404789589}[]{#struct_0_x6797_42255_x718054454}[]{#_Toc372127318}[]{#_Toc364430856}[]{#_Toc363576229}

**IGMP \-- IGMP配置命令 \-- igmp access-policy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6797_42255_x452037423}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6797_42255_1777713514}
:::

[ ]{lang="EN-US"}

[**[igmp]{lang="EN-US"}**[ **access-policy**]{lang="EN-US"}]{#struct_0_x6797_42255_x1225284575}[命令用来配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[用户的接入策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **access-policy**]{lang="EN-US"}]{#struct_0_x6797_42255_x717595702}[命令用来删除]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[用户的接入策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2124689486}

[**[igmp]{lang="EN-US"}**[ **access-policy** *acl-number*]{lang="EN-US"}]{#struct_0_x6797_42255_x964345588}

[**[undo]{lang="EN-US"}**[ **igmp** **access-policy** *acl-number*]{lang="EN-US"}]{#struct_0_x6797_42255_x1010407438}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_470631043}

[[没有配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_379260614}[用户的接入策略，即]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[用户未被授权加入组播组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x717661238}

[[User-Profile]{lang="EN-US"}]{#struct_0_x6797_42255_x1423155646}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1407250735}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1846570271}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_566575918}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x459402455}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x6797_42255_x717726774}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[用户只能加入该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的组播组。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，将过滤掉所有组播组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x619070474}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1122310346}[IPv4]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定]{style="font-family:宋体"}[IGMP]{lang="DA"}[报文中的]{style="font-family:宋体"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1773329432}[IPv4]{lang="DA"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="DA"}[，]{lang="EN-US" style="font-family:宋体"}[该]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{lang="EN-US" style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[IGMP]{lang="DA"}[报文中的组播源地址]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[IGMPv1/v2]{lang="DA"}[报文和未携带组播源地址的]{lang="EN-US" style="font-family:宋体"}[IS_EX/TO_EX]{lang="DA"}[类型的]{lang="EN-US" style="font-family:宋体"}[IGMPv3]{lang="DA"}[报文]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[视其组播源地址为]{lang="EN-US" style="font-family:
宋体"}[0.0.0.0]{lang="DA"}[）]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:
宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过多次执行本命令可以配置多条]{style="font-family:宋体"}]{#struct_0_x6797_42255_1761726903}[IGMP]{lang="EN-US"}[用户接入策略，用户发送的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文只需匹配其中一条就允许通过。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1630400756}

[[\#]{lang="EN-US"}]{#struct_0_x6797_42255_x1058163964}[[ ]{lang="EN-US"}]{#_Toc80176819}[在名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下配置只允许]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[用户加入组播组]{style="font-family:宋体"}[225.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x717792310}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 225.1.1.2 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] user-profile abc]{lang="EN-US"}

[\[Sysname-user-profile-abc\] igmp access-policy 2000]{lang="EN-US"}
:::::

::::: {#324576144 .myid}
[]{#_Toc404789590}[]{#struct_0_x6797_42255_2129979784}[]{#_Toc372127319}[]{#_Toc364430857}[]{#_Toc363576226}[]{#_Toc363465604}

**IGMP \-- IGMP配置命令 \-- igmp authorization-enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6797_42255_x451119919}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6797_42255_x1255792060}
:::

[ ]{lang="EN-US"}

[**[igmp]{lang="EN-US"}**[ **authorization-enable**]{lang="EN-US"}]{#struct_0_x6797_42255_1501052801}[命令用来使能可控组播功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **authorization-enable**]{lang="EN-US"}]{#struct_0_x6797_42255_1348352691}[命令用来关闭可控组播功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1926191804}

[**[igmp]{lang="EN-US"}**[ **authorization-enable**]{lang="EN-US"}]{#struct_0_x6797_42255_x717333558}

[**[undo]{lang="EN-US"}**[ **igmp** **authorization-enable**]{lang="EN-US"}]{#struct_0_x6797_42255_x1002343291}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_751716672}

[[可控组播功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x6797_42255_x462433101}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_518946581}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6797_42255_1970843128}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/VT]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x717399094}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x653589873}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1186865835}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1828502898}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x533193604}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能可控组播功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x717857839}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp authorization-enable]{lang="EN-US"}
:::::

::: {#499747696 .myid}
[]{#_Toc404789591}[]{#struct_0_x6797_42255_x967879313}[]{#_Toc299461498}[]{#_Toc94588234}[]{#_Toc80176780}[]{#_Toc30075880}[]{#_Toc375301624}[]{#_Toc375301964}[]{#_Toc375301625}[]{#_Toc375301965}[]{#_Toc296158651}[]{#_Toc296159966}[]{#_Toc296158652}[]{#_Toc296159967}[]{#_Toc296158653}[]{#_Toc296159968}[]{#_Toc296158654}[]{#_Toc296159969}[]{#_Toc296158655}[]{#_Toc296159970}[]{#_Toc296158656}[]{#_Toc296159971}[]{#_Toc296158657}[]{#_Toc296159972}[]{#_Toc296158658}[]{#_Toc296159973}[]{#_Toc296158659}[]{#_Toc296159974}[]{#_Toc296158660}[]{#_Toc296159975}[]{#_Toc296158661}[]{#_Toc296159976}[]{#_Toc296158662}[]{#_Toc296159977}[]{#_Toc296158663}[]{#_Toc296159978}[]{#_Toc296158664}[]{#_Toc296159979}[]{#_Toc296158665}[]{#_Toc296159980}[]{#_Toc296158666}[]{#_Toc296159981}[]{#_Toc296158667}[]{#_Toc296159982}[]{#_Toc296158668}[]{#_Toc296159983}[]{#_Toc296158669}[]{#_Toc296159984}[]{#_Toc296158670}[]{#_Toc296159985}[]{#_Toc296158671}[]{#_Toc296159986}[]{#_Toc296158672}[]{#_Toc296159987}[]{#_Toc296158677}[]{#_Toc296159992}[]{#_Toc296158685}[]{#_Toc296160000}[]{#_Toc296158686}[]{#_Toc296160001}[]{#_Toc296158687}[]{#_Toc296160002}[]{#_Toc296158716}[]{#_Toc296160031}[]{#_Toc296158718}[]{#_Toc296160033}[]{#_Toc296158719}[]{#_Toc296160034}[]{#_Toc296158720}[]{#_Toc296160035}[]{#_Toc296158721}[]{#_Toc296160036}[]{#_Toc296158722}[]{#_Toc296160037}[]{#_Toc296158723}[]{#_Toc296160038}[]{#_Toc296158724}[]{#_Toc296160039}[]{#_Toc296158725}[]{#_Toc296160040}[]{#_Toc296158726}[]{#_Toc296160041}[]{#_Toc296158727}[]{#_Toc296160042}[]{#_Toc296158728}[]{#_Toc296160043}[]{#_Toc296158729}[]{#_Toc296160044}[]{#_Toc296158730}[]{#_Toc296160045}[]{#_Toc296158731}[]{#_Toc296160046}[]{#_Toc296158732}[]{#_Toc296160047}[]{#_Toc296158733}[]{#_Toc296160048}[]{#_Toc296158734}[]{#_Toc296160049}[]{#_Toc296158735}[]{#_Toc296160050}[]{#_Toc296158736}[]{#_Toc296160051}[]{#_Toc296158737}[]{#_Toc296160052}[]{#_Toc296158738}[]{#_Toc296160053}[]{#_Toc296158739}[]{#_Toc296160054}[]{#_Toc296158740}[]{#_Toc296160055}[]{#_Toc296158741}[]{#_Toc296160056}[]{#_Toc296158742}[]{#_Toc296160057}[]{#_Toc296158743}[]{#_Toc296160058}[]{#_Toc296158745}[]{#_Toc296160060}[]{#_Toc296158747}[]{#_Toc296160062}[]{#_Toc296158750}[]{#_Toc296160065}[]{#_Toc296158752}[]{#_Toc296160067}[]{#_Toc296158753}[]{#_Toc296160068}[]{#_Toc296158754}[]{#_Toc296160069}[]{#_Toc296158755}[]{#_Toc296160070}[]{#_Toc296158756}[]{#_Toc296160071}[]{#_Toc296158757}[]{#_Toc296160072}[]{#_Toc296158760}[]{#_Toc296160075}[]{#_Toc296158761}[]{#_Toc296160076}[]{#_Toc296158762}[]{#_Toc296160077}[]{#_Toc296158795}[]{#_Toc296160110}[]{#_Toc137035624}[]{#_Toc137036654}[]{#_Toc137041713}[]{#_Toc137042384}[]{#_Toc87442398}[]{#_Toc87787038}[]{#_Toc87851901}[]{#_Toc87852680}[]{#_Toc87853461}[]{#_Toc87867500}[]{#_Toc87442408}[]{#_Toc87787048}[]{#_Toc87851911}[]{#_Toc87852690}[]{#_Toc87853471}[]{#_Toc87867510}[]{#_Toc87442409}[]{#_Toc87787049}[]{#_Toc87851912}[]{#_Toc87852691}[]{#_Toc87853472}[]{#_Toc87867511}[]{#_Toc87442410}[]{#_Toc87787050}[]{#_Toc87851913}[]{#_Toc87852692}[]{#_Toc87853473}[]{#_Toc87867512}[]{#_Toc87442411}[]{#_Toc87787051}[]{#_Toc87851914}[]{#_Toc87852693}[]{#_Toc87853474}[]{#_Toc87867513}[]{#_Toc87442412}[]{#_Toc87787052}[]{#_Toc87851915}[]{#_Toc87852694}[]{#_Toc87853475}[]{#_Toc87867514}[]{#_Toc87442413}[]{#_Toc87787053}[]{#_Toc87851916}[]{#_Toc87852695}[]{#_Toc87853476}[]{#_Toc87867515}[]{#_Toc87442414}[]{#_Toc87787054}[]{#_Toc87851917}[]{#_Toc87852696}[]{#_Toc87853477}[]{#_Toc87867516}[]{#_Toc87442415}[]{#_Toc87787055}[]{#_Toc87851918}[]{#_Toc87852697}[]{#_Toc87853478}[]{#_Toc87867517}[]{#_Toc87442416}[]{#_Toc87787056}[]{#_Toc87851919}[]{#_Toc87852698}[]{#_Toc87853479}[]{#_Toc87867518}[]{#_Toc87442417}[]{#_Toc87787057}[]{#_Toc87851920}[]{#_Toc87852699}[]{#_Toc87853480}[]{#_Toc87867519}[]{#_Toc87442418}[]{#_Toc87787058}[]{#_Toc87851921}[]{#_Toc87852700}[]{#_Toc87853481}[]{#_Toc87867520}[]{#_Toc87442419}[]{#_Toc87787059}[]{#_Toc87851922}[]{#_Toc87852701}[]{#_Toc87853482}[]{#_Toc87867521}[]{#_Toc87442420}[]{#_Toc87787060}[]{#_Toc87851923}[]{#_Toc87852702}[]{#_Toc87853483}[]{#_Toc87867522}[]{#_Toc87442426}[]{#_Toc87787066}[]{#_Toc87851929}[]{#_Toc87852708}[]{#_Toc87853489}[]{#_Toc87867528}[]{#_Toc35952990}[]{#_Toc35953393}[]{#_Toc35954277}[]{#_Toc35955154}[]{#_Toc296158797}[]{#_Toc296160112}[]{#_Toc296158798}[]{#_Toc296160113}[]{#_Toc296158799}[]{#_Toc296160114}[]{#_Toc296158800}[]{#_Toc296160115}[]{#_Toc296158801}[]{#_Toc296160116}[]{#_Toc296158802}[]{#_Toc296160117}[]{#_Toc296158803}[]{#_Toc296160118}[]{#_Toc296158804}[]{#_Toc296160119}[]{#_Toc296158805}[]{#_Toc296160120}[]{#_Toc296158806}[]{#_Toc296160121}[]{#_Toc296158807}[]{#_Toc296160122}[]{#_Toc296158808}[]{#_Toc296160123}[]{#_Toc296158809}[]{#_Toc296160124}[]{#_Toc296158810}[]{#_Toc296160125}[]{#_Toc296158811}[]{#_Toc296160126}[]{#_Toc296158812}[]{#_Toc296160127}[]{#_Toc296158813}[]{#_Toc296160128}[]{#_Toc296158814}[]{#_Toc296160129}[]{#_Toc296158815}[]{#_Toc296160130}[]{#_Toc296158816}[]{#_Toc296160131}[]{#_Toc296158817}[]{#_Toc296160132}[]{#_Toc296158821}[]{#_Toc296160136}[]{#_Toc296158826}[]{#_Toc296160141}[]{#_Toc296158839}[]{#_Toc296160154}[]{#_Toc296158840}[]{#_Toc296160155}[]{#_Toc296158841}[]{#_Toc296160156}[]{#_Toc296158842}[]{#_Toc296160157}[]{#_Toc296158843}[]{#_Toc296160158}[]{#_Toc296158844}[]{#_Toc296160159}[]{#_Toc296158845}[]{#_Toc296160160}[]{#_Toc296158846}[]{#_Toc296160161}[]{#_Toc296158847}[]{#_Toc296160162}[]{#_Toc296158848}[]{#_Toc296160163}[]{#_Toc296158849}[]{#_Toc296160164}[]{#_Toc296158850}[]{#_Toc296160165}[]{#_Toc296158851}[]{#_Toc296160166}[]{#_Toc296158852}[]{#_Toc296160167}[]{#_Toc296158853}[]{#_Toc296160168}[]{#_Toc296158854}[]{#_Toc296160169}[]{#_Toc296158855}[]{#_Toc296160170}[]{#_Toc296158856}[]{#_Toc296160171}[]{#_Toc296158857}[]{#_Toc296160172}[]{#_Toc296158858}[]{#_Toc296160173}[]{#_Toc296158859}[]{#_Toc296160174}[]{#_Toc296158860}[]{#_Toc296160175}[]{#_Toc296158861}[]{#_Toc296160176}[]{#_Toc296158862}[]{#_Toc296160177}[]{#_Toc296158877}[]{#_Toc296160192}[]{#_Toc296158878}[]{#_Toc296160193}[]{#_Toc296158915}[]{#_Toc296160230}[]{#_Toc296158917}[]{#_Toc296160232}[]{#_Toc296158918}[]{#_Toc296160233}[]{#_Toc296158919}[]{#_Toc296160234}[]{#_Toc296158920}[]{#_Toc296160235}[]{#_Toc296158921}[]{#_Toc296160236}[]{#_Toc296158922}[]{#_Toc296160237}[]{#_Toc296158923}[]{#_Toc296160238}[]{#_Toc296158924}[]{#_Toc296160239}[]{#_Toc296158925}[]{#_Toc296160240}[]{#_Toc296158926}[]{#_Toc296160241}[]{#_Toc296158927}[]{#_Toc296160242}[]{#_Toc296158928}[]{#_Toc296160243}[]{#_Toc296158929}[]{#_Toc296160244}[]{#_Toc296158930}[]{#_Toc296160245}[]{#_Toc296158931}[]{#_Toc296160246}[]{#_Toc296158932}[]{#_Toc296160247}[]{#_Toc296158933}[]{#_Toc296160248}[]{#_Toc296158934}[]{#_Toc296160249}[]{#_Toc296158935}[]{#_Toc296160250}[]{#_Toc296158937}[]{#_Toc296160252}[]{#_Toc296158938}[]{#_Toc296160253}[]{#_Toc296158939}[]{#_Toc296160254}[]{#_Toc296158943}[]{#_Toc296160258}[]{#_Toc296158965}[]{#_Toc296160280}[]{#_Toc296158966}[]{#_Toc296160281}[]{#_Toc296158967}[]{#_Toc296160282}[]{#_Toc296158969}[]{#_Toc296160284}[]{#_Toc296158970}[]{#_Toc296160285}[]{#_Toc296158971}[]{#_Toc296160286}[]{#_Toc296158972}[]{#_Toc296160287}[]{#_Toc296158973}[]{#_Toc296160288}[]{#_Toc296158974}[]{#_Toc296160289}[]{#_Toc296158975}[]{#_Toc296160290}[]{#_Toc296158976}[]{#_Toc296160291}[]{#_Toc296158977}[]{#_Toc296160292}[]{#_Toc296158978}[]{#_Toc296160293}[]{#_Toc296158979}[]{#_Toc296160294}[]{#_Toc296158980}[]{#_Toc296160295}[]{#_Toc296158981}[]{#_Toc296160296}[]{#_Toc296158982}[]{#_Toc296160297}[]{#_Toc296158983}[]{#_Toc296160298}[]{#_Toc296158984}[]{#_Toc296160299}[]{#_Toc296158987}[]{#_Toc296160302}[]{#_Toc296158988}[]{#_Toc296160303}[]{#_Toc296158991}[]{#_Toc296160306}[]{#_Toc296158992}[]{#_Toc296160307}[]{#_Toc296158993}[]{#_Toc296160308}[]{#_Toc296158994}[]{#_Toc296160309}[]{#_Toc296158995}[]{#_Toc296160310}[]{#_Toc296158996}[]{#_Toc296160311}[]{#_Toc296158997}[]{#_Toc296160312}[]{#_Toc296158998}[]{#_Toc296160313}[]{#_Toc296158999}[]{#_Toc296160314}[]{#_Toc296159000}[]{#_Toc296160315}[]{#_Toc296159001}[]{#_Toc296160316}[]{#_Toc296159002}[]{#_Toc296160317}[]{#_Toc296159003}[]{#_Toc296160318}[]{#_Toc296159004}[]{#_Toc296160319}[]{#_Toc296159005}[]{#_Toc296160320}[]{#_Toc296159006}[]{#_Toc296160321}[]{#_Toc296159007}[]{#_Toc296160322}[]{#_Toc296159010}[]{#_Toc296160325}[]{#_Toc296159011}[]{#_Toc296160326}[]{#_Toc296159014}[]{#_Toc296160329}[]{#_Toc296159015}[]{#_Toc296160330}[]{#_Toc296159016}[]{#_Toc296160331}[]{#_Toc296159017}[]{#_Toc296160332}[]{#_Toc296159018}[]{#_Toc296160333}[]{#_Toc296159019}[]{#_Toc296160334}[]{#_Toc296159020}[]{#_Toc296160335}[]{#_Toc296159021}[]{#_Toc296160336}[]{#_Toc296159022}[]{#_Toc296160337}[]{#_Toc296159023}[]{#_Toc296160338}[]{#_Toc296159024}[]{#_Toc296160339}[]{#_Toc296159025}[]{#_Toc296160340}[]{#_Toc296159026}[]{#_Toc296160341}[]{#_Toc296159027}[]{#_Toc296160342}[]{#_Toc296159028}[]{#_Toc296160343}[]{#_Toc296159029}[]{#_Toc296160344}[]{#_Toc296159030}[]{#_Toc296160345}[]{#_Toc296159034}[]{#_Toc296160349}[]{#_Toc296159035}[]{#_Toc296160350}[]{#_Toc296159042}[]{#_Toc296160357}

**IGMP \-- IGMP配置命令 \-- igmp enable**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x6797_42255_131854730}[命令用来在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **enable**]{lang="EN-US"}]{#struct_0_x6797_42255_x1880437235}[命令用来在接口上关闭]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x358641715}

[]{#struct_0_x6797_42255_x286032337}[]{#_Hlt20797640}**[igmp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **igmp** **enable**]{lang="EN-US"}]{#struct_0_x6797_42255_x65185071}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2131292941}

[[接口上的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1678511734}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1512414240}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1062349048}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1192063584}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1880502771}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1190287431}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_810572473}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在相应实例中先使能了]{style="font-family:宋体"}]{#struct_0_x6797_42255_1699483609}[IP]{lang="EN-US"}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在接口上使能了]{lang="EN-US" style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_771750487}[，在该接口上]{lang="EN-US" style="font-family:宋体"}[所做的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[配置才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1264696704}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_895749932}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1286499953}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1880306163}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_521375985}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_2050893058}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_578337212}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp enable]{lang="EN-US"}

[]{#_Toc94588235}[]{#_Toc80176782}[]{#struct_0_x6797_42255_x1097171624}[]{#_Toc136487931}[]{#_Toc136504493}[]{#_Toc87442432}[]{#_Toc87787072}[]{#_Toc87851935}[]{#_Toc87852714}[]{#_Toc87853495}[]{#_Toc87867534}[]{#_Toc87442434}[]{#_Toc87787074}[]{#_Toc87851937}[]{#_Toc87852716}[]{#_Toc87853497}[]{#_Toc87867536}[]{#_Toc87442435}[]{#_Toc87787075}[]{#_Toc87851938}[]{#_Toc87852717}[]{#_Toc87853498}[]{#_Toc87867537}[]{#_Toc87442436}[]{#_Toc87787076}[]{#_Toc87851939}[]{#_Toc87852718}[]{#_Toc87853499}[]{#_Toc87867538}[]{#_Toc87442437}[]{#_Toc87787077}[]{#_Toc87851940}[]{#_Toc87852719}[]{#_Toc87853500}[]{#_Toc87867539}[]{#_Toc87442438}[]{#_Toc87787078}[]{#_Toc87851941}[]{#_Toc87852720}[]{#_Toc87853501}[]{#_Toc87867540}[]{#_Toc87442439}[]{#_Toc87787079}[]{#_Toc87851942}[]{#_Toc87852721}[]{#_Toc87853502}[]{#_Toc87867541}[]{#_Toc87442440}[]{#_Toc87787080}[]{#_Toc87851943}[]{#_Toc87852722}[]{#_Toc87853503}[]{#_Toc87867542}[]{#_Toc87442441}[]{#_Toc87787081}[]{#_Toc87851944}[]{#_Toc87852723}[]{#_Toc87853504}[]{#_Toc87867543}[]{#_Toc87442442}[]{#_Toc87787082}[]{#_Toc87851945}[]{#_Toc87852724}[]{#_Toc87853505}[]{#_Toc87867544}[]{#_Toc87442443}[]{#_Toc87787083}[]{#_Toc87851946}[]{#_Toc87852725}[]{#_Toc87853506}[]{#_Toc87867545}[]{#_Toc87442444}[]{#_Toc87787084}[]{#_Toc87851947}[]{#_Toc87852726}[]{#_Toc87853507}[]{#_Toc87867546}[]{#_Toc87442445}[]{#_Toc87787085}[]{#_Toc87851948}[]{#_Toc87852727}[]{#_Toc87853508}[]{#_Toc87867547}[]{#_Toc87442446}[]{#_Toc87787086}[]{#_Toc87851949}[]{#_Toc87852728}[]{#_Toc87853509}[]{#_Toc87867548}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast]{lang="EN-US"}**[ **routing**]{lang="EN-US"}]{#struct_0_x6797_42255_x691621935}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#377962365 .myid}
[]{#_Toc404789592}[]{#struct_0_x6797_42255_1370599882}[]{#_Toc299461499}

**IGMP \-- IGMP配置命令 \-- igmp fast-leave**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **fast-leave**]{lang="EN-US"}]{#struct_0_x6797_42255_x782165255}[命令用来在接口上使能组播组成员快速离开功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **fast-leave**]{lang="EN-US"}]{#struct_0_x6797_42255_x1534031000}[命令用来在接口上关闭组播组成员快速离开功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1880371699}

[**[igmp]{lang="EN-US"}**[ **fast-leave** \[ **group-policy** *acl-number* \]]{lang="EN-US"}]{#struct_0_x6797_42255_x463629415}

[**[undo]{lang="EN-US"}**[ **igmp** **fast-leave**]{lang="EN-US"}]{#struct_0_x6797_42255_x1788415672}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1257109151}

[[组播组成员快速离开功能处于关闭状态，即]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1849923235}[查询器在收到主机发送的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[离开组报文后将发送]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文或]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定源组查询报文，而不会直接向上游发送离开通告。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x779891181}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_697273967}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1297808645}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1040665903}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x440184885}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1880175091}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x6797_42255_x288624957}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果指定了本参数，快速离开功能将只为该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的组播组服务；如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则快速离开功能将为所有组播组服务。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1525463806}

[[ACL]{lang="EN-US"}]{#struct_0_x6797_42255_2062134123}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[组播组的范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_875501467}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x308450254}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_123662693}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能组播组成员快速离开功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_784477088}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp fast-leave]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1616107133}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x1660261083}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能组播组成员快速离开功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1880240627}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp fast-leave]{lang="EN-US"}
:::

::: {#-245691417 .myid}
[]{#_Toc404789593}[]{#struct_0_x6797_42255_60420072}[]{#_Toc299461500}[]{#_Toc307402133}[]{#_Toc307402134}[]{#_Toc307402135}[]{#_Toc296159045}[]{#_Toc296160360}[]{#_Toc296159046}[]{#_Toc296160361}[]{#_Toc296159047}[]{#_Toc296160362}[]{#_Toc296159049}[]{#_Toc296160364}[]{#_Toc296159050}[]{#_Toc296160365}[]{#_Toc296159051}[]{#_Toc296160366}[]{#_Toc296159052}[]{#_Toc296160367}[]{#_Toc296159053}[]{#_Toc296160368}[]{#_Toc296159054}[]{#_Toc296160369}[]{#_Toc296159055}[]{#_Toc296160370}[]{#_Toc296159056}[]{#_Toc296160371}[]{#_Toc296159057}[]{#_Toc296160372}[]{#_Toc296159058}[]{#_Toc296160373}[]{#_Toc296159059}[]{#_Toc296160374}[]{#_Toc296159060}[]{#_Toc296160375}[]{#_Toc296159061}[]{#_Toc296160376}[]{#_Toc296159062}[]{#_Toc296160377}[]{#_Toc296159063}[]{#_Toc296160378}[]{#_Toc296159064}[]{#_Toc296160379}[]{#_Toc296159065}[]{#_Toc296160380}[]{#_Toc296159066}[]{#_Toc296160381}[]{#_Toc296159067}[]{#_Toc296160382}[]{#_Toc296159068}[]{#_Toc296160383}[]{#_Toc296159069}[]{#_Toc296160384}[]{#_Toc296159070}[]{#_Toc296160385}[]{#_Toc296159071}[]{#_Toc296160386}[]{#_Toc296159073}[]{#_Toc296160388}

**IGMP \-- IGMP配置命令 \-- igmp group-policy**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **group-policy**]{lang="EN-US"}]{#struct_0_x6797_42255_x1621955539}[命令用来在接口上配置组播组过滤器，以限定该接口下的主机所能加入的组播组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **group-policy**]{lang="EN-US"}]{#struct_0_x6797_42255_1867751145}[命令用来在接口上删除组播组过滤器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1078642698}

[**[igmp]{lang="EN-US"}**[ **group-policy** *acl-number* \[ *version-number* \]]{lang="EN-US"}]{#struct_0_x6797_42255_1320623618}

[**[undo]{lang="EN-US"}**[ **igmp** **group-policy**]{lang="EN-US"}]{#struct_0_x6797_42255_1560580462}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1618891558}

[[接口上没有配置组播组过滤器，即该接口下的主机可以加入任意组播组。]{style="font-family:宋体"}]{#struct_0_x6797_42255_559058822}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2058462007}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1880044019}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1754388768}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1109538291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1301103045}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1452453684}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x6797_42255_203474628}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。主机只能加入该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的组播组。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，将过滤掉所有组播组。]{style="font-family:宋体"}

[*[version-number]{lang="EN-US"}*]{#struct_0_x6797_42255_x545185987}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[的版本号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。缺省情况下，系统同时支持对]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[、]{style="font-family:宋体"}[IGMPv2]{lang="EN-US"}[和]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}[报告报文的过滤。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_520532721}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1525660414}[IPv4]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定]{style="font-family:宋体"}[IGMP]{lang="DA"}[报文中的]{style="font-family:宋体"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1305395761}[IPv4]{lang="DA"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="DA"}[，]{lang="EN-US" style="font-family:宋体"}[该]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{lang="EN-US" style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[IGMP]{lang="DA"}[报文中的组播源地址]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[IGMPv1/v2]{lang="DA"}[报文和未携带组播源地址的]{lang="EN-US" style="font-family:宋体"}[IS_EX/TO_EX]{lang="DA"}[类型的]{lang="EN-US" style="font-family:宋体"}[IGMPv3]{lang="DA"}[报文]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[视其组播源地址为]{lang="EN-US" style="font-family:
宋体"}[0.0.0.0]{lang="DA"}[）]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[组播组地址]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:
宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于本命令只能过滤]{style="font-family:宋体"}]{#struct_0_x6797_42255_611610843}[IGMP]{lang="EN-US"}[报文，因此无法对接口静态加入组播组或组播源组进行限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1825141740}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1880109555}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x684665525}[限定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下的主机只能加入组播组]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_1697156144}

[\[Sysname\] acl basic 2005]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2005\] rule permit source 225.1.1.1 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2005\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp group-policy 2005]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x992067129}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_340040158}[限定接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[下的主机只能加入组播组]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x826175361}

[\[Sysname\] acl basic 2005]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2005\] rule permit source 225.1.1.1 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2005\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp group-policy 2005]{lang="EN-US"}
:::

::::: {#776769157 .myid}
[]{#_Toc404789594}[]{#struct_0_x6797_42255_x717661231}

**IGMP \-- IGMP配置命令 \-- igmp join-by-session**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6797_42255_x451840816}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6797_42255_x828181748}
:::

[ ]{lang="EN-US"}

[**[igmp]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_x6797_42255_x1422565822}[命令用来配置按会话记录用户加入的组播组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **join-by-session**]{lang="EN-US"}]{#struct_0_x6797_42255_x1516789187}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x2008998748}

[**[igmp]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_x6797_42255_x717726767}

[**[undo]{lang="EN-US"}**[ **igmp** **join-by-session**]{lang="EN-US"}]{#struct_0_x6797_42255_x619136009}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x614614193}

[[按接口记录用户加入的组播组。]{style="font-family:宋体"}]{#struct_0_x6797_42255_1233036627}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_607005671}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6797_42255_286970661}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x717792303}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_2129783177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1611168490}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2033038384}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当按接口记录用户加入的组播组时，设备只会向物理接口发送一份组播报文；当按会话记录用户加入的组播组时，设备会向接口下的每位用户分别发送一份组播报文。]{style="font-family:宋体"}]{#struct_0_x6797_42255_x842879638}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_x6797_42255_x1002933115}[命令]{style="font-family:宋体"}[与]{lang="EN-US" style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}[命令]{style="font-family:宋体"}[互斥，不]{lang="EN-US" style="font-family:宋体"}[允许]{style="font-family:宋体"}[同时配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1171497244}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x558717067}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置按会话记录用户加入的组播组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x828849552}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp join-by-session]{lang="EN-US"}
:::::

::: {#1799784233 .myid}
[]{#_Toc33096884}[]{#_Toc404789595}[]{#struct_0_x6797_42255_1426529098}[]{#_Toc372205804}[]{#_Toc371343393}[]{#_Toc368325554}[]{#_Toc368294498}

**IGMP \-- IGMP配置命令 \-- igmp last-member-query-count**

------------------------------------------------------------------------

[**[igmp last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x717399087}[命令用来在接口上配置]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[最后组成员查询次数。]{style="font-family:宋体"}

[**[undo igmp last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x653786480}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1929890031}

[**[igmp last-member-query-count ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_x6797_42255_x1714011379}

[**[undo igmp last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_1957091491}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x717857840}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1658210231}[最后组成员查询次数等于]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_782771537}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1057375297}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1430558987}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1362803032}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x717923376}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x614042323}

[*[count]{lang="EN-US"}*]{#struct_0_x6797_42255_1668081796}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x817379233}

[[本命令与]{style="font-family:宋体"}**[last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_81724028}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x717988912}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1272215512}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1205113625}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询次数为]{style="font-family:宋体"}[6]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x952193234}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp last-member-query-count 6]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1552520244}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x718054448}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询次数为]{style="font-family:宋体"}[6]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1225546720}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp last-member-query-count 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x43414207}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[last-member-query-count]{lang="EN-US"}**[ (IGMP view)]{lang="EN-US"}]{#struct_0_x6797_42255_1894566721}
:::

::: {#1404235417 .myid}
[]{#_Toc404789596}[]{#struct_0_x6797_42255_x373341890}[]{#_Toc372205805}[]{#_Toc371343394}[]{#_Toc368325555}[]{#_Toc368294499}

**IGMP \-- IGMP配置命令 \-- igmp last-member-query-interval**

------------------------------------------------------------------------

[**[igmp last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x717595696}[命令用来在接口上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询间隔。]{style="font-family:宋体"}

[**[undo igmp last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_168636501}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1141719398}

[**[igmp last-member-query-interval]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x6797_42255_172976711}

[**[undo igmp last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x69026078}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x717661232}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1422762430}[最后组成员查询间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1019442313}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_1609315198}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x368874742}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1123158992}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x717726768}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x618808329}

[*[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_x250251270}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1224179013}

[[本命令与]{style="font-family:宋体"}**[last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x1650963147}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x717792304}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_2130241929}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x1661234245}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_2043295349}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp last-member-query-interval 6]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1900206398}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x717333552}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1002736507}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp last-member-query-interval 6]{lang="EN-US"}

[]{#_Toc371343395}[]{#_Toc368325556}[]{#_Toc368294500}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_673794070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[last-member-query-interval]{lang="EN-US"}**[ (IGMP view)]{lang="EN-US"}]{#struct_0_x6797_42255_x2071922628}
:::

::: {#-1786821695 .myid}
[]{#_Toc404789597}[]{#struct_0_x6797_42255_x150296697}[]{#_Toc372205806}

**IGMP \-- IGMP配置命令 \-- igmp max-response-time**

------------------------------------------------------------------------

[**[igmp max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_x717399088}[命令用来在接口上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的最大响应时间。]{style="font-family:宋体"}

[**[undo igmp max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_x654376304}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1220200795}

[**[igmp max-response-time]{lang="EN-US"}***[ time]{lang="EN-US"}*]{#struct_0_x6797_42255_x1616616101}

[**[undo igmp max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_x1052873140}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848226098}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1493397179}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_909422661}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_1091002284}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x978423953}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x389908707}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_848160562}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1413621822}

[*[time]{lang="EN-US"}*]{#struct_0_x6797_42255_1812054650}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的最大响应时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3174]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x832252012}

[[本命令与]{style="font-family:宋体"}**[max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_848095026}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1348637224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1213989749}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_256824148}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_848029490}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp max-response-time 25]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_544957353}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x744046949}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_395269315}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp max-response-time 25]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x787431677}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-response-time]{lang="EN-US"}**[ (IGMP view)]{lang="EN-US"}]{#struct_0_x6797_42255_848488242}
:::

::: {#1812268882 .myid}
[]{#_Toc404789598}[]{#struct_0_x6797_42255_x2056804418}[]{#_Toc365363041}[]{#_Toc363907096}

**IGMP \-- IGMP配置命令 \-- igmp other-querier-present-interval**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **other-querier-present-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_x1480673204}[命令用来在接口上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[其它查询器的存在时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp other-querier-present-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_x1472665718}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x2056214595}

[**[igmp]{lang="EN-US"}**[ **other-querier-present-interval** *interval*]{lang="EN-US"}]{#struct_0_x6797_42255_133364519}

[**[undo]{lang="EN-US"}**[ **igmp** **other-querier-present-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_x1917202983}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x525618841}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x1183013259}[其它查询器的存在时间＝]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔×]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数＋]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间÷]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x2056280131}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_319735778}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x375405459}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1239507027}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1372473691}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x2056345667}

[*[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_1643548975}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[其它查询器的存在时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848422706}

[[本命令与]{style="font-family:宋体"}**[other-querier-present-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_1848110860}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_305522695}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1555472218}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1194314959}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[其它查询器的存在时间为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x2056411203}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp other-querier-present-interval 125]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1953227864}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x1916275432}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[其它查询器的存在时间为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1012589023}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp other-querier-present-interval 125]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848357170}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[other-querier-present-interval]{lang="EN-US"}**[ (IGMP view)]{lang="EN-US"}]{#struct_0_x6797_42255_x743963311}
:::

::: {#-934848912 .myid}
[]{#_Toc404789599}[]{#struct_0_x6797_42255_x2039524242}[]{#_Toc355963325}

**IGMP \-- IGMP配置命令 \-- igmp proxy enable**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **proxy** **enable**]{lang="EN-US"}]{#struct_0_x6797_42255_x1391680054}[命令用来在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **proxy** **enable**]{lang="EN-US"}]{#struct_0_x6797_42255_x2039589778}[命令用来关闭接口上的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x256230925}

[**[igmp]{lang="EN-US"}**[ **proxy** **enable**]{lang="EN-US"}]{#struct_0_x6797_42255_1665855973}

[**[undo]{lang="EN-US"}**[ **igmp** **proxy** **enable**]{lang="EN-US"}]{#struct_0_x6797_42255_691968465}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x2040048531}

[[接口上的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x2042672901}[代理功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1303400756}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x2040114067}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1591379299}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_904740691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_471377239}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x2040179603}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6797_42255_x1157023185}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1881553680}

[]{#struct_0_x6797_42255_719817337}[]{#_Hlt26244069}[]{#_Toc32805310}[]{#_Toc32805323}[]{#_Hlt16393071}[]{#_Hlt26244065}[]{#_Toc32812466}[]{#_Toc32812467}[]{#_Toc32812468}[]{#_Toc32812469}[]{#_Toc32812470}[]{#_Toc32812471}[]{#_Toc32812472}[]{#_Toc32812473}[]{#_Toc32812474}[]{#_Toc32812475}[]{#_Toc32812476}[]{#_Toc32812477}[]{#_Toc32812478}[]{#_Toc32812479}[]{#_Toc32812480}[]{#_Toc32812481}[]{#_Toc32812482}[]{#_Toc32812484}[]{#_Toc32812509}[]{#_Toc32812511}[]{#_Toc32812512}[]{#_Toc32812513}[]{#_Toc32812514}[]{#_Toc32812515}[]{#_Hlt20986286}[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}[：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="FR"}]{#struct_0_x6797_42255_x2040245139}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="FR"}[组播路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[上使能]{style="font-family:宋体"}[IGMP]{lang="FR"}[代理功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_159556647}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp proxy enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1779384636}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x2040310675}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1001099625}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp proxy enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1756188980}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast]{lang="EN-US"}**[ **routing**]{lang="EN-US"}]{#struct_0_x6797_42255_x2040376211}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#1756861926 .myid}
[]{#_Toc404789600}[]{#struct_0_x6797_42255_x1404121857}

**IGMP \-- IGMP配置命令 \-- igmp proxy forwarding**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **proxy** **forwarding**]{lang="EN-US"}]{#struct_0_x6797_42255_680360916}[命令用来使能非查询器转发功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **proxy** **forwarding**]{lang="EN-US"}]{#struct_0_x6797_42255_x1403925249}[命令用来关闭非查询器转发功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_748346343}

[**[igmp]{lang="EN-US"}**[ **proxy** **forwarding**]{lang="EN-US"}]{#struct_0_x6797_42255_812050538}

[**[undo]{lang="EN-US"}**[ **igmp** **proxy** **forwarding**]{lang="EN-US"}]{#struct_0_x6797_42255_x1403990785}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x943727137}

[[非查询器转发功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1403794177}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1558973277}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1403859713}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x370125351}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1403663105}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1261311602}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403728641}

[[组播数据通常只被查询器转发，非查询器不具备组播转发能力，这样可避免组播数据被重复转发。但如果]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1074018067}[代理设备的路由器接口未能当选查询器，应在该接口上使能非查询器转发功能，否则下游主机将无法收到组播数据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1403532033}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1005991988}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x1403597569}[在]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理设备的路由器接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能非查询器转发功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_2059317321}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp proxy forwarding]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_1324827039}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_917618238}[在]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理设备的路由器接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能非查询器转发功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_1324761503}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp proxy forwarding]{lang="EN-US"}
:::

::: {#-1985577040 .myid}
[]{#_Toc404789601}[]{#struct_0_x6797_42255_x2056804419}[]{#_Toc365363043}[]{#_Toc363907095}

**IGMP \-- IGMP配置命令 \-- igmp query-interval**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **query-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_1248210151}[命令用来在接口上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **query-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_x2056214596}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1699448460}

[**[igmp]{lang="EN-US"}**[ **query-interval** *interval*]{lang="EN-US"}]{#struct_0_x6797_42255_x337267890}

[**[undo]{lang="EN-US"}**[ **igmp** **query-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_x647003113}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x723477553}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x2056280132}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_723020305}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1235783695}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2039064061}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x2056345668}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1690603142}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1331624597}

[*[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_x230931852}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848160561}

[[本命令与]{style="font-family:宋体"}**[query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x1413621823}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_372600410}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x2056411204}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x775655491}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_941514906}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp query-interval 60]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x574532787}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x2055952452}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x589531004}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp query-interval 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848095025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[query-interval]{lang="EN-US"}**[ (IGMP view)]{lang="EN-US"}]{#struct_0_x6797_42255_1348637221}
:::

::: {#-1121800609 .myid}
[]{#_Toc404789602}[]{#struct_0_x6797_42255_x1213793141}[]{#_Toc372205811}[]{#_Toc371343400}[]{#_Toc368325560}[]{#_Toc368294501}

**IGMP \-- IGMP配置命令 \-- igmp robust-count**

------------------------------------------------------------------------

[**[igmp robust-count]{lang="EN-US"}**]{#struct_0_x6797_42255_848029489}[命令用来在接口上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[**[undo igmp robust-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x1793694798}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1631737531}

[**[igmp robust-count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_x6797_42255_x1865697563}

[**[undo igmp robust-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x941501106}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848488241}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1840294094}[查询器的健壮系数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1378120099}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_956708065}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848422705}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1848110859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1971895364}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1611114258}

[*[count]{lang="EN-US"}*]{#struct_0_x6797_42255_422925331}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848357169}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1594688840}[查询器的健壮系数是为了弥补可能发生的网络丢包而设置的报文重传次数，健壮系数越大，]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器就越"健壮"，但是组播组超时所需的时间也就越长。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{style="font-family:宋体"}]{#struct_0_x6797_42255_1443869582}**[robust-count]{lang="EN-US"}**[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1171807305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_848291633}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1578924889}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_381552211}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp robust-count 5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x929098797}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x701782717}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_848750385}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp robust-count 5]{lang="EN-US"}

[]{#_Toc371343401}[]{#_Toc368325561}[]{#_Toc368294502}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2107972630}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[robust-count]{lang="EN-US"}**[ (IGMP view)]{lang="EN-US"}]{#struct_0_x6797_42255_x1488376601}
:::

::: {#-1101948543 .myid}
[]{#_Toc404789603}[]{#struct_0_x6797_42255_848684849}[]{#_Toc372205812}

**IGMP \-- IGMP配置命令 \-- igmp startup-query-count**

------------------------------------------------------------------------

[**[igmp startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x1354371804}[命令用来在接口上配置]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询次数。]{style="font-family:宋体"}

[**[undo igmp startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x917149974}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x557252014}

[**[igmp startup-query-count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_x6797_42255_125700273}

[**[undo igmp startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_848226096}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1493397189}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_908832837}[查询器的启动查询次数等于]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_707850436}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_1296756048}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848160560}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1413621824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_649255236}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_565924135}

[*[count]{lang="EN-US"}*]{#struct_0_x6797_42255_848095024}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1348637222}

[[本命令与]{style="font-family:宋体"}**[startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x1213596533}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1001331215}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1417650430}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_848029488}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1793694799}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp startup-query-count 5]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1097145824}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1147900182}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_848488240}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp startup-query-count 5]{lang="EN-US"}

[]{#_Toc371343402}[]{#_Toc368325562}[]{#_Toc368294503}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1840294093}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[startup-query-count]{lang="EN-US"}**[ (IGMP view)]{lang="EN-US"}]{#struct_0_x6797_42255_1378578851}
:::

::: {#1049792730 .myid}
[]{#_Toc404789604}[]{#struct_0_x6797_42255_2131464073}[]{#_Toc372205813}

**IGMP \-- IGMP配置命令 \-- igmp startup-query-interval**

------------------------------------------------------------------------

[**[igmp startup-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_848422704}[命令用来在接口上配置]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询间隔。]{style="font-family:宋体"}

[**[undo igmp startup-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_1848110858}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1971960900}

[**[igmp startup-query-interval]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x6797_42255_x89319811}

[**[undo igmp startup-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x2107277109}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848357168}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1594688841}[查询器的启动查询间隔为]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文发送间隔的]{style="font-family:宋体"}[1/4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1443935118}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_2009982175}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1878577949}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_848291632}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1578924890}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_382010962}

[*[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_1608926388}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848750384}

[[本命令与]{style="font-family:宋体"}**[startup-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_2107972631}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1488442137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1605288251}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1209275937}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_848684848}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp startup-query-interval 100]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1354371805}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1811733381}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_487040747}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp startup-query-interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848226095}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[startup-query-interval]{lang="EN-US"}**[ (IGMP view)]{lang="EN-US"}]{#struct_0_x6797_42255_x1493397190}
:::

::: {#1509910017 .myid}
[]{#_Toc80176788}[]{#_Toc404789605}[]{#struct_0_x6797_42255_x704142594}[]{#_Toc299461501}[]{#_Toc94588241}[]{#_Toc78346629}[]{#_Toc307402137}[]{#_Toc307402138}[]{#_Toc139983139}[]{#_Toc139983444}[]{#_Toc139983140}[]{#_Toc139983445}[]{#_Toc139983142}[]{#_Toc139983447}[]{#_Toc139983145}[]{#_Toc139983450}[]{#_Toc136487933}[]{#_Toc136504495}[]{#_Toc87442449}[]{#_Toc87787089}[]{#_Toc87851952}[]{#_Toc87852731}[]{#_Toc87853512}[]{#_Toc87867551}[]{#_Toc87442450}[]{#_Toc87787090}[]{#_Toc87851953}[]{#_Toc87852732}[]{#_Toc87853513}[]{#_Toc87867552}[]{#_Toc87442451}[]{#_Toc87787091}[]{#_Toc87851954}[]{#_Toc87852733}[]{#_Toc87853514}[]{#_Toc87867553}[]{#_Toc87442452}[]{#_Toc87787092}[]{#_Toc87851955}[]{#_Toc87852734}[]{#_Toc87853515}[]{#_Toc87867554}[]{#_Toc87442453}[]{#_Toc87787093}[]{#_Toc87851956}[]{#_Toc87852735}[]{#_Toc87853516}[]{#_Toc87867555}[]{#_Toc87442454}[]{#_Toc87787094}[]{#_Toc87851957}[]{#_Toc87852736}[]{#_Toc87853517}[]{#_Toc87867556}[]{#_Toc87442455}[]{#_Toc87787095}[]{#_Toc87851958}[]{#_Toc87852737}[]{#_Toc87853518}[]{#_Toc87867557}[]{#_Toc87442456}[]{#_Toc87787096}[]{#_Toc87851959}[]{#_Toc87852738}[]{#_Toc87853519}[]{#_Toc87867558}[]{#_Toc87442457}[]{#_Toc87787097}[]{#_Toc87851960}[]{#_Toc87852739}[]{#_Toc87853520}[]{#_Toc87867559}[]{#_Toc87442458}[]{#_Toc87787098}[]{#_Toc87851961}[]{#_Toc87852740}[]{#_Toc87853521}[]{#_Toc87867560}[]{#_Toc87442459}[]{#_Toc87787099}[]{#_Toc87851962}[]{#_Toc87852741}[]{#_Toc87853522}[]{#_Toc87867561}[]{#_Toc87442460}[]{#_Toc87787100}[]{#_Toc87851963}[]{#_Toc87852742}[]{#_Toc87853523}[]{#_Toc87867562}[]{#_Toc87442461}[]{#_Toc87787101}[]{#_Toc87851964}[]{#_Toc87852743}[]{#_Toc87853524}[]{#_Toc87867563}[]{#_Toc87442462}[]{#_Toc87787102}[]{#_Toc87851965}[]{#_Toc87852744}[]{#_Toc87853525}[]{#_Toc87867564}[]{#_Toc296159075}[]{#_Toc296160390}[]{#_Toc296159076}[]{#_Toc296160391}[]{#_Toc296159077}[]{#_Toc296160392}[]{#_Toc296159078}[]{#_Toc296160393}[]{#_Toc296159079}[]{#_Toc296160394}[]{#_Toc296159080}[]{#_Toc296160395}[]{#_Toc296159081}[]{#_Toc296160396}[]{#_Toc296159082}[]{#_Toc296160397}[]{#_Toc296159083}[]{#_Toc296160398}[]{#_Toc296159084}[]{#_Toc296160399}[]{#_Toc296159085}[]{#_Toc296160400}[]{#_Toc296159086}[]{#_Toc296160401}[]{#_Toc296159087}[]{#_Toc296160402}[]{#_Toc296159088}[]{#_Toc296160403}[]{#_Toc296159089}[]{#_Toc296160404}[]{#_Toc296159090}[]{#_Toc296160405}[]{#_Toc296159091}[]{#_Toc296160406}[]{#_Toc296159093}[]{#_Toc296160408}[]{#_Toc296159094}[]{#_Toc296160409}[]{#_Toc296159095}[]{#_Toc296160410}[]{#_Toc296159096}[]{#_Toc296160411}[]{#_Toc296159099}[]{#_Toc296160414}[]{#_Toc296159100}[]{#_Toc296160415}[]{#_Toc296159101}[]{#_Toc296160416}[]{#_Toc296159103}[]{#_Toc296160418}[]{#_Toc296159104}[]{#_Toc296160419}[]{#_Toc296159105}[]{#_Toc296160420}[]{#_Toc296159106}[]{#_Toc296160421}[]{#_Toc296159107}[]{#_Toc296160422}[]{#_Toc296159108}[]{#_Toc296160423}[]{#_Toc296159109}[]{#_Toc296160424}[]{#_Toc296159110}[]{#_Toc296160425}[]{#_Toc296159111}[]{#_Toc296160426}[]{#_Toc296159112}[]{#_Toc296160427}[]{#_Toc296159113}[]{#_Toc296160428}[]{#_Toc296159114}[]{#_Toc296160429}[]{#_Toc296159115}[]{#_Toc296160430}[]{#_Toc296159116}[]{#_Toc296160431}[]{#_Toc296159118}[]{#_Toc296160433}[]{#_Toc296159120}[]{#_Toc296160435}[]{#_Toc296159121}[]{#_Toc296160436}[]{#_Toc296159126}[]{#_Toc296160441}[]{#_Toc296159128}[]{#_Toc296160443}[]{#_Toc296159129}[]{#_Toc296160444}[]{#_Toc296159130}[]{#_Toc296160445}[]{#_Toc296159131}[]{#_Toc296160446}[]{#_Toc296159132}[]{#_Toc296160447}[]{#_Toc296159133}[]{#_Toc296160448}[]{#_Toc296159134}[]{#_Toc296160449}[]{#_Toc296159135}[]{#_Toc296160450}[]{#_Toc296159136}[]{#_Toc296160451}[]{#_Toc296159137}[]{#_Toc296160452}[]{#_Toc296159138}[]{#_Toc296160453}[]{#_Toc296159139}[]{#_Toc296160454}[]{#_Toc296159140}[]{#_Toc296160455}[]{#_Toc296159141}[]{#_Toc296160456}[]{#_Toc296159143}[]{#_Toc296160458}[]{#_Hlt19521787}[]{#_Toc296159145}[]{#_Toc296160460}[]{#_Toc296159146}[]{#_Toc296160461}[]{#_Toc136487937}[]{#_Toc136504499}[]{#_Toc139983150}[]{#_Toc139983455}[]{#_Toc139983151}[]{#_Toc139983456}[]{#_Toc139983153}[]{#_Toc139983458}[]{#_Toc139983154}[]{#_Toc139983459}[]{#_Toc296159151}[]{#_Toc296160466}[]{#_Toc296159152}[]{#_Toc296160467}[]{#_Toc296159153}[]{#_Toc296160468}[]{#_Toc296159154}[]{#_Toc296160469}[]{#_Toc296159155}[]{#_Toc296160470}[]{#_Toc296159156}[]{#_Toc296160471}[]{#_Toc296159157}[]{#_Toc296160472}[]{#_Toc296159158}[]{#_Toc296160473}[]{#_Toc296159159}[]{#_Toc296160474}[]{#_Toc296159160}[]{#_Toc296160475}[]{#_Toc296159161}[]{#_Toc296160476}[]{#_Toc296159162}[]{#_Toc296160477}[]{#_Toc296159163}[]{#_Toc296160478}[]{#_Toc296159164}[]{#_Toc296160479}[]{#_Toc296159165}[]{#_Toc296160480}[]{#_Toc296159166}[]{#_Toc296160481}[]{#_Toc296159167}[]{#_Toc296160482}[]{#_Toc296159168}[]{#_Toc296160483}[]{#_Toc296159169}[]{#_Toc296160484}[]{#_Toc296159172}[]{#_Toc296160487}[]{#_Toc296159174}[]{#_Toc296160489}[]{#_Toc296159175}[]{#_Toc296160490}[]{#_Toc296159180}[]{#_Toc296160495}[]{#_Toc296159181}[]{#_Toc296160496}[]{#_Toc296159182}[]{#_Toc296160497}[]{#_Toc296159183}[]{#_Toc296160498}[]{#_Toc296159184}[]{#_Toc296160499}[]{#_Toc296159185}[]{#_Toc296160500}[]{#_Toc296159186}[]{#_Toc296160501}[]{#_Toc296159187}[]{#_Toc296160502}[]{#_Toc296159188}[]{#_Toc296160503}[]{#_Toc296159189}[]{#_Toc296160504}[]{#_Toc296159190}[]{#_Toc296160505}[]{#_Toc296159191}[]{#_Toc296160506}[]{#_Toc296159192}[]{#_Toc296160507}[]{#_Toc296159193}[]{#_Toc296160508}[]{#_Toc296159194}[]{#_Toc296160509}[]{#_Toc296159195}[]{#_Toc296160510}[]{#_Toc296159197}[]{#_Toc296160512}[]{#_Toc296159198}[]{#_Toc296160513}[]{#_Toc296159199}[]{#_Toc296160514}[]{#_Toc296159200}[]{#_Toc296160515}[]{#_Toc296159203}[]{#_Toc296160518}[]{#_Toc296159205}[]{#_Toc296160520}[]{#_Toc296159208}[]{#_Toc296160523}[]{#_Toc296159209}[]{#_Toc296160524}[]{#_Toc296159210}[]{#_Toc296160525}[]{#_Toc296159211}[]{#_Toc296160526}[]{#_Toc296159212}[]{#_Toc296160527}[]{#_Toc296159213}[]{#_Toc296160528}[]{#_Toc296159214}[]{#_Toc296160529}[]{#_Toc296159215}[]{#_Toc296160530}[]{#_Toc296159216}[]{#_Toc296160531}[]{#_Toc296159217}[]{#_Toc296160532}[]{#_Toc296159218}[]{#_Toc296160533}[]{#_Toc296159219}[]{#_Toc296160534}[]{#_Toc296159220}[]{#_Toc296160535}[]{#_Toc296159222}[]{#_Toc296160537}[]{#_Toc296159223}[]{#_Toc296160538}[]{#_Toc87442468}[]{#_Toc87787108}[]{#_Toc87851971}[]{#_Toc87852750}[]{#_Toc87853531}[]{#_Toc87867570}[]{#_Toc87442470}[]{#_Toc87787110}[]{#_Toc87851973}[]{#_Toc87852752}[]{#_Toc87853533}[]{#_Toc87867572}[]{#_Toc87442471}[]{#_Toc87787111}[]{#_Toc87851974}[]{#_Toc87852753}[]{#_Toc87853534}[]{#_Toc87867573}[]{#_Toc87442472}[]{#_Toc87787112}[]{#_Toc87851975}[]{#_Toc87852754}[]{#_Toc87853535}[]{#_Toc87867574}[]{#_Toc87442473}[]{#_Toc87787113}[]{#_Toc87851976}[]{#_Toc87852755}[]{#_Toc87853536}[]{#_Toc87867575}[]{#_Toc87442474}[]{#_Toc87787114}[]{#_Toc87851977}[]{#_Toc87852756}[]{#_Toc87853537}[]{#_Toc87867576}[]{#_Toc87442475}[]{#_Toc87787115}[]{#_Toc87851978}[]{#_Toc87852757}[]{#_Toc87853538}[]{#_Toc87867577}[]{#_Toc87442476}[]{#_Toc87787116}[]{#_Toc87851979}[]{#_Toc87852758}[]{#_Toc87853539}[]{#_Toc87867578}[]{#_Toc87442477}[]{#_Toc87787117}[]{#_Toc87851980}[]{#_Toc87852759}[]{#_Toc87853540}[]{#_Toc87867579}[]{#_Toc87442478}[]{#_Toc87787118}[]{#_Toc87851981}[]{#_Toc87852760}[]{#_Toc87853541}[]{#_Toc87867580}[]{#_Toc87442479}[]{#_Toc87787119}[]{#_Toc87851982}[]{#_Toc87852761}[]{#_Toc87853542}[]{#_Toc87867581}[]{#_Toc87442480}[]{#_Toc87787120}[]{#_Toc87851983}[]{#_Toc87852762}[]{#_Toc87853543}[]{#_Toc87867582}[]{#_Toc87442481}[]{#_Toc87787121}[]{#_Toc87851984}[]{#_Toc87852763}[]{#_Toc87853544}[]{#_Toc87867583}[]{#_Toc87442482}[]{#_Toc87787122}[]{#_Toc87851985}[]{#_Toc87852764}[]{#_Toc87853545}[]{#_Toc87867584}[]{#_Toc87442483}[]{#_Toc87787123}[]{#_Toc87851986}[]{#_Toc87852765}[]{#_Toc87853546}[]{#_Toc87867585}[]{#_Toc296159224}[]{#_Toc296160539}[]{#_Toc296159225}[]{#_Toc296160540}[]{#_Toc296159228}[]{#_Toc296160543}[]{#_Toc296159229}[]{#_Toc296160544}[]{#_Toc296159230}[]{#_Toc296160545}[]{#_Toc296159231}[]{#_Toc296160546}[]{#_Toc296159232}[]{#_Toc296160547}[]{#_Toc296159233}[]{#_Toc296160548}[]{#_Toc296159234}[]{#_Toc296160549}[]{#_Toc296159235}[]{#_Toc296160550}[]{#_Toc296159236}[]{#_Toc296160551}[]{#_Toc296159237}[]{#_Toc296160552}[]{#_Toc296159238}[]{#_Toc296160553}[]{#_Toc296159239}[]{#_Toc296160554}[]{#_Toc296159240}[]{#_Toc296160555}[]{#_Toc296159241}[]{#_Toc296160556}[]{#_Toc296159242}[]{#_Toc296160557}[]{#_Toc296159243}[]{#_Toc296160558}[]{#_Toc296159244}[]{#_Toc296160559}[]{#_Toc296159245}[]{#_Toc296160560}[]{#_Toc296159246}[]{#_Toc296160561}[]{#_Toc296159247}[]{#_Toc296160562}[]{#_Toc296159248}[]{#_Toc296160563}[]{#_Toc296159249}[]{#_Toc296160564}[]{#_Toc296159251}[]{#_Toc296160566}[]{#_Toc296159253}[]{#_Toc296160568}[]{#_Toc296159254}[]{#_Toc296160569}[]{#_Toc296159259}[]{#_Toc296160574}[]{#_Toc296159262}[]{#_Toc296160577}[]{#_Toc296159263}[]{#_Toc296160578}[]{#_Toc296159264}[]{#_Toc296160579}[]{#_Toc296159265}[]{#_Toc296160580}[]{#_Toc296159266}[]{#_Toc296160581}[]{#_Toc296159267}[]{#_Toc296160582}[]{#_Toc296159268}[]{#_Toc296160583}[]{#_Toc296159269}[]{#_Toc296160584}[]{#_Toc296159270}[]{#_Toc296160585}[]{#_Toc296159271}[]{#_Toc296160586}[]{#_Toc296159272}[]{#_Toc296160587}[]{#_Toc296159273}[]{#_Toc296160588}[]{#_Toc296159274}[]{#_Toc296160589}[]{#_Toc296159276}[]{#_Toc296160591}[]{#_Toc296159278}[]{#_Toc296160593}[]{#_Toc296159279}[]{#_Toc296160594}[]{#_Toc296159284}[]{#_Toc296160599}[]{#_Toc296159286}[]{#_Toc296160601}[]{#_Toc296159287}[]{#_Toc296160602}[]{#_Toc296159288}[]{#_Toc296160603}[]{#_Toc296159289}[]{#_Toc296160604}[]{#_Toc296159290}[]{#_Toc296160605}[]{#_Toc296159291}[]{#_Toc296160606}[]{#_Toc296159292}[]{#_Toc296160607}[]{#_Toc296159293}[]{#_Toc296160608}[]{#_Toc296159294}[]{#_Toc296160609}[]{#_Toc296159295}[]{#_Toc296160610}[]{#_Toc296159296}[]{#_Toc296160611}[]{#_Toc296159297}[]{#_Toc296160612}[]{#_Toc296159298}[]{#_Toc296160613}[]{#_Toc296159300}[]{#_Toc296160615}[]{#_Toc296159302}[]{#_Toc296160617}[]{#_Toc296159303}[]{#_Toc296160618}[]{#_Toc296159306}[]{#_Toc296160621}[]{#_Toc296159307}[]{#_Toc296160622}[]{#_Toc296159308}[]{#_Toc296160623}[]{#_Toc296159309}[]{#_Toc296160624}[]{#_Toc296159310}[]{#_Toc296160625}[]{#_Toc296159311}[]{#_Toc296160626}[]{#_Toc296159312}[]{#_Toc296160627}[]{#_Toc296159313}[]{#_Toc296160628}[]{#_Toc296159314}[]{#_Toc296160629}[]{#_Toc296159315}[]{#_Toc296160630}[]{#_Toc296159316}[]{#_Toc296160631}[]{#_Toc296159317}[]{#_Toc296160632}[]{#_Toc296159318}[]{#_Toc296160633}[]{#_Toc296159319}[]{#_Toc296160634}[]{#_Toc296159320}[]{#_Toc296160635}[]{#_Toc296159321}[]{#_Toc296160636}[]{#_Toc296159322}[]{#_Toc296160637}[]{#_Toc296159323}[]{#_Toc296160638}[]{#_Toc296159325}[]{#_Toc296160640}[]{#_Toc296159326}[]{#_Toc296160641}[]{#_Toc296159327}[]{#_Toc296160642}[]{#_Toc296159328}[]{#_Toc296160643}[]{#_Toc296159331}[]{#_Toc296160646}[]{#_Toc296159332}[]{#_Toc296160647}[]{#_Toc296159333}[]{#_Toc296160648}[]{#_Toc296159334}[]{#_Toc296160649}[]{#_Toc296159336}[]{#_Toc296160651}[]{#_Toc296159337}[]{#_Toc296160652}[]{#_Toc296159338}[]{#_Toc296160653}[]{#_Toc296159339}[]{#_Toc296160654}[]{#_Toc296159340}[]{#_Toc296160655}[]{#_Toc296159341}[]{#_Toc296160656}[]{#_Toc296159342}[]{#_Toc296160657}[]{#_Toc296159343}[]{#_Toc296160658}[]{#_Toc296159344}[]{#_Toc296160659}[]{#_Toc296159345}[]{#_Toc296160660}[]{#_Toc296159346}[]{#_Toc296160661}[]{#_Toc296159347}[]{#_Toc296160662}[]{#_Toc296159348}[]{#_Toc296160663}[]{#_Toc296159350}[]{#_Toc296160665}[]{#_Toc296159351}[]{#_Toc296160666}[]{#_Toc296159352}[]{#_Toc296160667}[]{#_Toc296159353}[]{#_Toc296160668}[]{#_Toc296159356}[]{#_Toc296160671}

**IGMP \-- IGMP配置命令 \-- igmp static-group**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **static-group**]{lang="EN-US"}]{#struct_0_x6797_42255_x1879912947}[命令用来配置接口静态加入组播组或组播源组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **static-group**]{lang="EN-US"}]{#struct_0_x6797_42255_1186546498}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_226713614}

[**[igmp]{lang="EN-US"}**[ **static-group** *group-address* \[ **source** *source-address* \] \[ **dot1q** **vid** *vlan-list* \| **dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list* \]]{lang="EN-US"}]{#struct_0_x6797_42255_1205273224}

[**[undo]{lang="EN-US"}**[ **igmp** **static-group** { **all** \| *group-address* \[ **source** *source-address* \] \[ **dot1q** **vid** *vlan-list* \| **dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list* \] }]{lang="EN-US"}]{#struct_0_x6797_42255_x1721258097}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x654450367}

[[接口没有以静态方式加入任何组播组或组播源组。]{style="font-family:宋体"}]{#struct_0_x6797_42255_x2030636402}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x377969242}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_1978067309}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1879978483}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1503107933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_475746215}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1920608094}

[*[group-address]{lang="EN-US"}*]{#struct_0_x6797_42255_x185608067}[：指定组播组地址，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_x6797_42255_x1532452778}[：指定组播源的地址。如果未指定本参数，表示针对所有组播源。]{style="font-family:宋体"}

[**[dot1q]{lang="EN-US"}**[ **vid** *vlan-list*]{lang="EN-US"}]{#struct_0_x6797_42255_848095023}[：指定封装的第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。本参数只在三层以太网子接口视图和三层聚合子接口视图下支持。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[dot1q]{lang="EN-US"}**[ **vid** *vlan-id* **second-dot1q** *vlan-list*]{lang="EN-US"}]{#struct_0_x6797_42255_1348637219}[：指定封装的第一层和第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[；]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一或多个第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。本参数只在三层以太网子接口视图和三层聚合子接口视图下支持。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6797_42255_x1528535134}[：删除此接口加入的所有静态组播组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x172228224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的组播组地址在]{style="font-family:宋体"}]{#struct_0_x6797_42255_x303869}[SSM]{lang="EN-US"}[组地址范围内，则必须同时指定组播源的地址，否则将不会生成组播路由表项用于指导组播转发；如果指定的组播组地址不在]{style="font-family:宋体"}[SSM]{lang="EN-US"}[组地址范围内，则无此限制。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于同一个组播组或组播源组，不带]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1213268852}[VLAN]{lang="EN-US"}[封装、带一层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[封装和带两层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[封装的静态加入配置两两互斥，不允许同时配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置不带]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6797_42255_848029487}[封装的静态加入]{lang="EN-US" style="font-family:宋体"}[时]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[如果子]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[上没有]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}[命令]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}[命令，]{lang="EN-US" style="font-family:宋体"}[才]{style="font-family:宋体"}[生成静态]{lang="EN-US" style="font-family:宋体"}[组播]{style="font-family:宋体"}[表项。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置带]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x6797_42255_x1793694808}[封装的静态加入时，]{lang="EN-US" style="font-family:宋体"}[如果子]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[配置了]{lang="EN-US" style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}[命令，]{lang="EN-US" style="font-family:宋体"}[那么当相应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[用户上线时]{lang="EN-US" style="font-family:宋体"}[才]{style="font-family:宋体"}[生成静态]{lang="EN-US" style="font-family:宋体"}[组播]{style="font-family:宋体"}[表项；]{lang="EN-US" style="font-family:宋体"}[如果子接口上]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}[命令，]{lang="EN-US" style="font-family:宋体"}[那么只有二者的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[封装相同，]{lang="EN-US" style="font-family:宋体"}[才]{style="font-family:宋体"}[生成静态]{lang="EN-US" style="font-family:宋体"}[组播]{style="font-family:宋体"}[表项。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1942170652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x314353291}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_964719732}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[静态加入组播组]{style="font-family:宋体"}[224.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_845224633}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp static-group 224.1.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x585727171}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[静态加入组播源组（]{style="font-family:宋体"}[192.168.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[232.1.1.1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_95527646}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp static-group 232.1.1.1 source 192.168.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_848488239}[配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[按会话记录用户加入的组播组，并静态加入组播组]{style="font-family:宋体"}[224.1.1.1]{lang="EN-US"}[：当第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[、第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[的用户上线时才生成静态组播表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1263032122}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] igmp join-by-session]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] igmp static-group 224.1.1.1 dot1q vid 10 second-dot1q 10 to 20]{lang="EN-US"}

[]{#_Toc94588242}[]{#struct_0_x6797_42255_1631601615}[]{#_Toc138170858}[]{#_Toc139983159}[]{#_Toc139983464}[]{#_Toc138170859}[]{#_Toc139983160}[]{#_Toc139983465}[]{#_Toc138170861}[]{#_Toc139983162}[]{#_Toc139983467}[]{#_Toc138170863}[]{#_Toc139983164}[]{#_Toc139983469}[]{#_Toc138170865}[]{#_Toc139983166}[]{#_Toc139983471}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_2015404094}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[静态加入组播组]{style="font-family:宋体"}[224.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x314418827}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp static-group 224.1.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x238389385}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[静态加入组播源组（]{style="font-family:宋体"}[192.168.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[232.1.1.1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_1301418615}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp static-group 232.1.1.1 source 192.168.1.1]{lang="EN-US"}
:::

::::: {#-2086733806 .myid}
[]{#_Toc404789606}[]{#struct_0_x6797_42255_848422703}[]{#_Toc372127327}[]{#_Toc370719720}[]{#_Toc363576228}

**IGMP \-- IGMP配置命令 \-- igmp user-vlan-aggregation dot1q**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IGMP命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6797_42255_1114308660}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x6797_42255_1822861854}
:::

[ ]{lang="EN-US"}

[**[igmp]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}]{#struct_0_x6797_42255_1848110865}[命令用来配置为组播报文封装的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **user-vlan-aggregation** **dot1q**]{lang="EN-US"}]{#struct_0_x6797_42255_848357167}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1594688846}

[**[igmp]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q** **vid** *vlan-id* \[ **second-dot1q** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x6797_42255_1443476366}

[**[undo]{lang="EN-US"}**[ **igmp** **user-vlan-aggregation** **dot1q**]{lang="EN-US"}]{#struct_0_x6797_42255_2039187374}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848291631}

[[不为组播报文封装]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x6797_42255_1578924887}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_382469715}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6797_42255_x164382968}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848750383}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_2107972636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1488769817}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848684847}

[**[vid]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6797_42255_x1354371794}[：指定封装的第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[second-dot1q]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x6797_42255_x917739801}[：指定封装的第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1794507517}

[**[igmp]{lang="EN-US"}**[ **join-by-session**]{lang="EN-US"}]{#struct_0_x6797_42255_848226102}[命令与]{style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **user-vlan-aggregation** **dot1q**]{lang="EN-US"}[命令互斥，不允许同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_426182106}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1978905078}[在子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[上配置为组播报文封装的第一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[，第二层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_848160566}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] igmp user-vlan-aggregation dot1q vid 10 second-dot1q 20]{lang="EN-US"}
:::::

::: {#1825977646 .myid}
[]{#_Toc404789607}[]{#struct_0_x6797_42255_x146749379}[]{#_Toc299461502}[]{#_Toc94588244}[]{#_Toc80176790}[]{#_Toc307402140}[]{#_Toc307402141}[]{#_Toc296159359}[]{#_Toc296160674}[]{#_Toc296159361}[]{#_Toc296160676}[]{#_Toc296159362}[]{#_Toc296160677}[]{#_Toc296159363}[]{#_Toc296160678}[]{#_Toc296159364}[]{#_Toc296160679}[]{#_Toc296159365}[]{#_Toc296160680}[]{#_Toc296159366}[]{#_Toc296160681}[]{#_Toc296159367}[]{#_Toc296160682}[]{#_Toc296159368}[]{#_Toc296160683}[]{#_Toc296159369}[]{#_Toc296160684}[]{#_Toc296159370}[]{#_Toc296160685}[]{#_Toc296159371}[]{#_Toc296160686}[]{#_Toc296159372}[]{#_Toc296160687}[]{#_Toc296159373}[]{#_Toc296160688}[]{#_Toc296159374}[]{#_Toc296160689}[]{#_Toc296159376}[]{#_Toc296160691}[]{#_Toc296159378}[]{#_Toc296160693}[]{#_Toc296159379}[]{#_Toc296160694}[]{#_Toc296159384}[]{#_Toc296160699}[]{#_Toc296159386}[]{#_Toc296160701}[]{#_Toc296159387}[]{#_Toc296160702}[]{#_Toc296159388}[]{#_Toc296160703}[]{#_Toc296159389}[]{#_Toc296160704}[]{#_Toc296159390}[]{#_Toc296160705}[]{#_Toc296159391}[]{#_Toc296160706}[]{#_Toc296159392}[]{#_Toc296160707}[]{#_Toc296159393}[]{#_Toc296160708}[]{#_Toc296159394}[]{#_Toc296160709}[]{#_Toc296159395}[]{#_Toc296160710}[]{#_Toc296159396}[]{#_Toc296160711}[]{#_Toc296159397}[]{#_Toc296160712}[]{#_Toc296159398}[]{#_Toc296160713}[]{#_Toc296159399}[]{#_Toc296160714}[]{#_Toc296159401}[]{#_Toc296160716}[]{#_Toc296159403}[]{#_Toc296160718}[]{#_Toc296159404}[]{#_Toc296160719}[]{#_Toc296159408}

**IGMP \-- IGMP配置命令 \-- igmp version**

------------------------------------------------------------------------

[**[igmp]{lang="EN-US"}**[ **version**]{lang="EN-US"}]{#struct_0_x6797_42255_986524387}[命令用来在接口上配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[的版本。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **igmp** **version**]{lang="EN-US"}]{#struct_0_x6797_42255_x1515532440}[命令用来恢复缺省情况。]{style="font-family:宋体"}[]{#_Toc296159419}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1339216718}[]{#_Toc296159409}

[**[igmp]{lang="EN-US"}**[ **version** *version-number*]{lang="EN-US"}]{#struct_0_x6797_42255_x1580520410}[]{#_Toc296159410}

[**[undo]{lang="EN-US"}**[ **igmp** **version**]{lang="EN-US"}]{#struct_0_x6797_42255_1811002300}[]{#_Toc296159411}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1081140241}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x314222219}[的版本为]{style="font-family:宋体"}[IGMPv2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x607328060}[]{#_Toc296159412}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_974231026}[]{#_Toc296159413}

[]{#struct_0_x6797_42255_x1103273470}[]{#_Toc296159414}[【缺省用户角色】]{style="font-family:黑体"}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1748052596}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1513576158}

[]{#struct_0_x6797_42255_145288626}[]{#_Toc296159415}[【参数】]{style="font-family:黑体"}[]{#_Toc296159416}

[*[version-number]{lang="EN-US"}*]{#struct_0_x6797_42255_1344628845}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[的版本号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc296159417}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x2104694680}[]{#_Toc296159422}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x314287755}[]{#_Toc296159423}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_2079475345}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使用]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc296159424}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x277838121}[]{#_Toc296159425}

[\[Sysname\] interface gigabitethernet 1/0/1[]{#_Toc296159426}]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] igmp version 1]{lang="EN-US"}[]{#_Toc296159427}

[]{#_Toc94588245}[]{#_Toc80176791}[]{#_Toc30075877}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1336386003}[]{#_Toc296159428}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1794903535}[指定接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[使用]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc296159429}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1873217099}[]{#_Toc296159430}

[\[Sysname\] interface vlan-interface 100[]{#_Toc296159431}]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] igmp version 1]{lang="EN-US"}[]{#_Toc296159432}
:::

::: {#2130704361 .myid}
[]{#_Toc404789608}[]{#struct_0_x6797_42255_848029494}[]{#_Toc372205816}[]{#_Toc371343405}[]{#_Toc368325565}[]{#_Toc368294504}

**IGMP \-- IGMP配置命令 \-- last-member-query-count (IGMP view)**

------------------------------------------------------------------------

[**[last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_544957349}[命令用来全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询次数。]{style="font-family:宋体"}

[**[undo last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_1594605205}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1727744453}

[**[last-member-query-count ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_x6797_42255_848488246}

[**[undo last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_1840294095}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1378185635}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x606825800}[最后组成员查询次数等于]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848422710}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x108204274}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1705262299}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_848357174}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x743963315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1870684906}

[*[count]{lang="EN-US"}*]{#struct_0_x6797_42255_x267348625}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848291638}

[[本命令与]{style="font-family:宋体"}**[igmp last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_1578924880}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_382010963}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1608926389}[在公网实例中全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询次数为]{style="font-family:宋体"}[6]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_848750390}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] last-member-query-count 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x230679525}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp ]{lang="EN-US"}[last-member-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x471264496}
:::

::: {#1720968791 .myid}
[]{#_Toc404789609}[]{#struct_0_x6797_42255_848684854}[]{#_Toc372205817}[]{#_Toc371343406}[]{#_Toc368325566}[]{#_Toc368294505}

**IGMP \-- IGMP配置命令 \-- last-member-query-interval (IGMP view)**

------------------------------------------------------------------------

[**[last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_984280367}[命令用来全局配置]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[最后组成员查询间隔。]{style="font-family:宋体"}

[**[undo last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_840035792}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848226101}

[**[last-member-query-interval]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x6797_42255_426182105}

[**[undo last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_1978905081}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1195413945}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_848160565}[最后组成员查询间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1413621819}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_602135533}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848095029}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1348637209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1213268851}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1918314591}

[*[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_848029493}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_544957356}

[[本命令与]{style="font-family:宋体"}**[igmp last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x744046946}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848488245}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1840294098}[在公网实例中全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[最后组成员查询间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_1377857955}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] last-member-query-interval 6]{lang="EN-US"}

[]{#_Toc371343407}[]{#_Toc368325567}[]{#_Toc368294506}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1099070217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp ]{lang="EN-US"}[last-member-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_848422709}
:::

::: {#-1097059204 .myid}
[]{#_Toc404789610}[]{#struct_0_x6797_42255_1848110871}[]{#_Toc372205818}

**IGMP \-- IGMP配置命令 \-- max-response-time (IGMP view)**

------------------------------------------------------------------------

[**[max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_x1972419654}[命令用来全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的最大响应时间。]{style="font-family:宋体"}

[**[undo max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_848357173}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x743963310}

[**[max-response-time]{lang="EN-US"}***[ time]{lang="EN-US"}*]{#struct_0_x6797_42255_x1870488298}

[**[undo max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_1966863860}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848291637}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1578924893}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_382207570}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x2007577203}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848750389}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_2107972626}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1488769816}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_848684853}

[*[time]{lang="EN-US"}*]{#struct_0_x6797_42255_984280362}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的最大响应时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3174]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_840035789}

[[本命令与]{style="font-family:宋体"}**[igmp max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_1539087276}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_444941571}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x1528835705}[在公网实例中全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的最大响应时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_1391496419}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] max-response-time 25]{lang="EN-US"}

[]{#_Toc371343408}[]{#_Toc368325568}[]{#_Toc368294507}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_444876035}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp ]{lang="EN-US"}[max-response-time]{lang="EN-US"}**]{#struct_0_x6797_42255_1963339579}
:::

::: {#730004430 .myid}
[]{#_Toc404789611}[]{#struct_0_x6797_42255_750527409}[]{#_Toc372205819}

**IGMP \-- IGMP配置命令 \-- other-querier-present-interval (IGMP view)**

------------------------------------------------------------------------

[**[other-querier-present-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x1682842474}[命令用来全局配置]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[其它查询器的存在时间。]{style="font-family:宋体"}

[**[undo other-querier-present-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_444810499}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1545100301}

[**[other-querier-present-interval]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x6797_42255_2052932534}

[**[undo other-querier-present-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_866725390}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_444744963}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_2135378121}[其它查询器的存在时间＝]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔×]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数＋]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询的最大响应时间÷]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x407196463}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_445203715}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_587194318}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1575720847}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x788712287}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445138179}

[*[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_x482960549}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[其它查询器的存在时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x726186677}

[[本命令与]{style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **other-querier-present-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_445072643}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x57191218}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x980882399}[在公网实例中全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[其它查询器的存在时间为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x1190175681}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] other-querier-present-interval 125]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445007107}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp]{lang="EN-US"}**]{#struct_0_x6797_42255_1477811054}[ ]{lang="EN-US"}**[other-querier-present-interval]{lang="EN-US"}**
:::

::: {#1735451058 .myid}
[]{#_Toc404789612}[]{#struct_0_x6797_42255_1325154719}

**IGMP \-- IGMP配置命令 \-- proxy multipath (IGMP view)**

------------------------------------------------------------------------

[**[proxy]{lang="EN-US"}**[ **multipath**]{lang="EN-US"}]{#struct_0_x6797_42255_918708566}[命令用来使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理的负载分担功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **proxy** **multipath**]{lang="EN-US"}]{#struct_0_x6797_42255_1325351327}[命令用来关闭]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理的负载分担功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_914204832}

[**[proxy]{lang="EN-US"}**[ **multipath**]{lang="EN-US"}]{#struct_0_x6797_42255_1325285791}

[**[undo]{lang="EN-US"}**[ **proxy** **multipath**]{lang="EN-US"}]{#struct_0_x6797_42255_x666315192}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1324827038}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_917552702}[代理的负载分担功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1324761502}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_896706586}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1324958110}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_2052446098}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1324892574}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x695395309}

[[当在]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1325089182}[代理设备的多个接口上使能了]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理功能时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果关闭了]{style="font-family:宋体"}]{#struct_0_x6797_42255_868568395}[IGMP]{lang="EN-US"}[代理的负载分担功能，则只有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址最大的接口会转发组播流量。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果使能了]{style="font-family:宋体"}]{#struct_0_x6797_42255_1325023646}[IGMP]{lang="EN-US"}[代理的负载分担功能，则可通过这些接口对组播流量按组进行负载分担。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_878285237}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1325220254}[在公网实例中使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理的负载分担功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_517026853}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] proxy multipath]{lang="EN-US"}
:::

::: {#-629776689 .myid}
[]{#_Toc404789613}[]{#struct_0_x6797_42255_445400323}[]{#_Toc372205821}[]{#_Toc371343410}[]{#_Toc368325569}[]{#_Toc368294508}

**IGMP \-- IGMP配置命令 \-- query-interval (IGMP view)**

------------------------------------------------------------------------

[**[query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_461746748}[命令用来全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔。]{style="font-family:宋体"}

[**[undo query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x403282632}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_444941570}

[**[query-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_x1528835706}

[**[undo query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x1337386936}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1391422378}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_444876034}[普遍组查询报文的发送间隔为]{style="font-family:宋体"}[125]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1963339580}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_750068650}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_444810498}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1545100302}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_2052735926}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_505205100}

[*[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_444744962}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的发送间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_2135378120}

[[本命令与]{style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **query-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_x407130927}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445203714}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_587194317}[在公网实例中全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_1575720850}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] query-interval 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445138178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp]{lang="EN-US"}**]{#struct_0_x6797_42255_x482960548}[ ]{lang="EN-US"}**[query-interval]{lang="EN-US"}**
:::

::: {#-1538878081 .myid}
[]{#_Toc404789614}[]{#struct_0_x6797_42255_720460093}[]{#_Toc299461503}[]{#_Toc296159433}[]{#_Toc296160724}[]{#_Toc296159434}[]{#_Toc296160725}[]{#_Toc296159436}[]{#_Toc296160727}[]{#_Toc296159437}[]{#_Toc296160728}[]{#_Toc296159438}[]{#_Toc296160729}[]{#_Toc296159439}[]{#_Toc296160730}[]{#_Toc296159440}[]{#_Toc296160731}[]{#_Toc296159441}[]{#_Toc296160732}[]{#_Toc296159442}[]{#_Toc296160733}[]{#_Toc296159443}[]{#_Toc296160734}[]{#_Toc296159444}[]{#_Toc296160735}[]{#_Toc296159445}[]{#_Toc296160736}[]{#_Toc296159446}[]{#_Toc296160737}[]{#_Toc296159447}[]{#_Toc296160738}[]{#_Toc296159448}[]{#_Toc296160739}[]{#_Toc296159452}[]{#_Toc296160743}[]{#_Toc296159456}[]{#_Toc296160747}[]{#_Toc296159457}[]{#_Toc296160748}[]{#_Toc296159459}[]{#_Toc296160750}[]{#_Toc296159460}[]{#_Toc296160751}[]{#_Toc296159461}[]{#_Toc296160752}[]{#_Toc296159462}[]{#_Toc296160753}[]{#_Toc296159463}[]{#_Toc296160754}[]{#_Toc296159464}[]{#_Toc296160755}[]{#_Toc296159465}[]{#_Toc296160756}[]{#_Toc296159466}[]{#_Toc296160757}[]{#_Toc296159467}[]{#_Toc296160758}[]{#_Toc296159468}[]{#_Toc296160759}[]{#_Toc296159469}[]{#_Toc296160760}[]{#_Toc296159470}[]{#_Toc296160761}[]{#_Toc296159471}[]{#_Toc296160762}[]{#_Toc296159475}[]{#_Toc296160766}[]{#_Toc296159478}[]{#_Toc296160769}[]{#_Toc296159479}[]{#_Toc296160770}[]{#_Toc296159480}[]{#_Toc296160771}[]{#_Toc296159483}[]{#_Toc296160774}[]{#_Toc296159484}[]{#_Toc296160775}[]{#_Toc296159485}[]{#_Toc296160776}[]{#_Toc296159486}[]{#_Toc296160777}[]{#_Toc296159487}[]{#_Toc296160778}[]{#_Toc296159488}[]{#_Toc296160779}[]{#_Toc296159489}[]{#_Toc296160780}[]{#_Toc296159490}[]{#_Toc296160781}[]{#_Toc296159491}[]{#_Toc296160782}[]{#_Toc296159492}[]{#_Toc296160783}[]{#_Toc296159493}[]{#_Toc296160784}[]{#_Toc296159494}[]{#_Toc296160785}[]{#_Toc296159497}[]{#_Toc296160788}[]{#_Toc296159498}[]{#_Toc296160789}[]{#_Toc296159500}[]{#_Toc296160791}[]{#_Toc296159501}[]{#_Toc296160792}

**IGMP \-- IGMP配置命令 \-- reset igmp group**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **igmp** **group**]{lang="EN-US"}]{#struct_0_x6797_42255_653527359}[命令用来清除]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1831900171}

[**[reset]{lang="EN-US"}**[ **igmp** \[ **vpn-instance** *vpn-instance-name* \] **group** { **all** \| **interface** *interface-type interface-number* { **all** \| *group-address* \[ **mask** { *mask* \| *mask-length* } \] \[ *source-address* \[ **mask** { *mask* \| *mask-length* } \] \] } }]{lang="EN-US"}]{#struct_0_x6797_42255_x314091147}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_529292570}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6797_42255_697017459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x201528940}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_883332639}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1861532202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x370586676}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x6797_42255_1883487749}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的记录，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的记录。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6797_42255_1213125819}[：前一个]{style="font-family:宋体"}**[all]{lang="EN-US"}**[表示清除所有接口上的记录，后一个]{style="font-family:宋体"}**[all]{lang="EN-US"}**[表示清除所有组播组的记录。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6797_42255_x314156683}[：清除指定接口上的记录。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_x6797_42255_x1806189752}[：清除指定组播组的记录，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_x6797_42255_1211942620}[：清除指定组播源的记录。如果未指定本参数，将清除所有组播源的记录。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x6797_42255_x154002746}[：指定组播组或组播源地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x6797_42255_2077952107}[：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[；对于组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_312807539}

[[执行本命令可能导致接收者中断组播信息的接收。]{style="font-family:宋体"}]{#struct_0_x6797_42255_x1274019722}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1103116762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x503182077}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x313960075}[清除公网实例所有接口上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset igmp group all]{lang="EN-US"}]{#struct_0_x6797_42255_1462424317}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x663018061}[清除公网实例接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset igmp group interface gigabitethernet 1/0/1 all]{lang="EN-US"}]{#struct_0_x6797_42255_x1127056507}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x894423802}[清除公网实例接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组]{style="font-family:宋体"}[225.0.0.1]{lang="EN-US"}[的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset igmp group interface gigabitethernet 1/0/1 225.0.0.1]{lang="EN-US"}]{#struct_0_x6797_42255_x1081489324}

[]{#_Toc94588246}[]{#_Toc80176793}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x6797_42255_x1752429701}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x970202467}[清除公网实例所有接口上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset igmp group all]{lang="EN-US"}]{#struct_0_x6797_42255_595520269}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1786456864}[清除公网实例接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset igmp group interface vlan-interface 100 all]{lang="EN-US"}]{#struct_0_x6797_42255_x314025611}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_916336521}[清除公网实例接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[组播组]{style="font-family:宋体"}[225.0.0.1]{lang="EN-US"}[的动态加入记录。]{style="font-family:宋体"}

[[\<Sysname\> reset igmp group interface vlan-interface 100 225.0.0.1]{lang="EN-US"}]{#struct_0_x6797_42255_x180700929}[]{#_Toc296159504}[]{#_Toc296159506}[]{#_Toc296159507}[]{#_Toc296159508}[]{#_Toc296159509}[]{#_Toc296159510}[]{#_Toc296159511}[]{#_Toc296159512}[]{#_Toc296159513}[]{#_Toc296159514}[]{#_Toc296159515}[]{#_Toc296159516}[]{#_Toc296159517}[]{#_Toc296159518}[]{#_Toc296159519}[]{#_Toc296159520}[]{#_Toc296159521}[]{#_Toc296159522}[]{#_Toc296159523}[]{#_Toc296159524}[]{#_Toc296159526}[]{#_Toc296159528}[]{#_Toc296159530}[]{#_Toc296159531}[]{#_Toc296159533}[]{#_Toc296159534}[]{#_Toc296159535}[]{#_Toc296159536}[]{#_Toc296159537}[]{#_Toc296159538}[]{#_Toc296159539}[]{#_Toc296159540}[]{#_Toc296159541}[]{#_Toc296159542}[]{#_Toc296159543}[]{#_Toc296159544}[]{#_Toc296159545}[]{#_Toc296159546}[]{#_Toc296159547}[]{#_Toc296159548}[]{#_Toc296159549}[]{#_Toc296159550}[]{#_Toc296159551}[]{#_Toc296159553}[]{#_Toc296159554}[]{#_Toc296159555}[]{#_Toc296159556}[]{#_Toc296159557}[]{#_Toc296159558}[]{#_Toc296159559}[]{#_Toc296159560}[]{#_Toc296159561}[]{#_Toc296159562}[]{#_Toc296159563}[]{#_Toc296159564}[]{#_Toc296159565}[]{#_Toc296159566}[]{#_Toc296159567}[]{#_Toc296159568}[]{#_Toc296159569}[]{#_Toc296159570}[]{#_Toc296159571}[]{#_Toc296159572}[]{#_Toc296159576}[]{#_Toc296159580}[]{#_Toc296159581}[]{#_Toc296159584}[]{#_Toc296159585}[]{#_Toc296159586}[]{#_Toc296159587}[]{#_Toc296159588}[]{#_Toc296159589}[]{#_Toc296159590}[]{#_Toc296159591}[]{#_Toc296159592}[]{#_Toc296159593}[]{#_Toc296159594}[]{#_Toc296159595}[]{#_Toc296159599}[]{#_Toc296159602}[]{#_Toc296159603}[]{#_Toc296159604}[]{#_Toc296159605}[]{#_Toc296159607}[]{#_Toc296159608}[]{#_Toc296159609}[]{#_Toc296159610}[]{#_Toc296159611}[]{#_Toc296159612}[]{#_Toc296159613}[]{#_Toc296159614}[]{#_Toc296159615}[]{#_Toc296159616}[]{#_Toc296159617}[]{#_Toc296159618}[]{#_Toc296159619}[]{#_Toc296159620}[]{#_Toc296159621}[]{#_Toc296159622}[]{#_Toc296159626}[]{#_Toc296159630}[]{#_Toc296159631}[]{#_Toc296159632}[]{#_Toc296159633}[]{#_Toc296159634}[]{#_Toc296159635}[]{#_Toc296159636}[]{#_Toc296159637}[]{#_Toc296159638}[]{#_Toc296159639}[]{#_Toc296159640}[]{#_Toc296159641}[]{#_Toc296159642}[]{#_Toc296159643}[]{#_Toc296159644}[]{#_Toc296159645}[]{#_Toc296159648}[]{#_Toc296159649}[]{#_Toc296159652}[]{#_Toc296159653}[]{#_Toc296159654}[]{#_Toc296159655}[]{#_Toc296159657}[]{#_Toc296159658}[]{#_Toc296159659}[]{#_Toc296159660}[]{#_Toc296159661}[]{#_Toc296159662}[]{#_Toc296159663}[]{#_Toc296159664}[]{#_Toc296159665}[]{#_Toc296159666}[]{#_Toc296159667}[]{#_Toc296159668}[]{#_Toc296159671}[]{#_Toc296159672}[]{#_Toc296159675}[]{#_Toc296159676}[]{#_Toc296159677}[]{#_Toc296159679}[]{#_Toc296159680}[]{#_Toc296159681}[]{#_Toc296159682}[]{#_Toc296159683}[]{#_Toc296159684}[]{#_Toc296159685}[]{#_Toc296159686}[]{#_Toc296159687}[]{#_Toc296159688}[]{#_Toc296159689}[]{#_Toc296159690}[]{#_Toc296159691}[]{#_Toc296159695}[]{#_Toc296159698}[]{#_Toc296159699}[]{#_Toc296159700}[]{#_Toc296159702}[]{#_Toc296159703}[]{#_Toc296159704}[]{#_Toc296159705}[]{#_Toc296159706}[]{#_Toc296159707}[]{#_Toc296159708}[]{#_Toc296159709}[]{#_Toc296159710}[]{#_Toc296159711}[]{#_Toc296159712}[]{#_Toc296159713}[]{#_Toc296159714}[]{#_Toc296159718}[]{#_Toc296159721}[]{#_Toc296159722}[]{#_Toc296159723}[]{#_Toc296159724}[]{#_Toc296159726}[]{#_Toc296159727}[]{#_Toc296159728}[]{#_Toc296159729}[]{#_Toc296159730}[]{#_Toc296159731}[]{#_Toc296159732}[]{#_Toc296159733}[]{#_Toc296159734}[]{#_Toc296159735}[]{#_Toc296159736}[]{#_Toc296159737}[]{#_Toc296159740}[]{#_Toc296159741}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1687141105}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **igmp** **group**]{lang="EN-US"}]{#struct_0_x6797_42255_x728521794}
:::

::: {#-1052067343 .myid}
[]{#_Toc404789615}[]{#struct_0_x6797_42255_445007106}[]{#_Toc372205823}[]{#_Toc371343412}[]{#_Toc368325571}[]{#_Toc368294509}

**IGMP \-- IGMP配置命令 \-- robust-count (IGMP view)**

------------------------------------------------------------------------

[**[robust-count]{lang="EN-US"}**]{#struct_0_x6797_42255_445465858}[命令用来全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[**[undo robust-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x383797852}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_753705691}

[**[robust-count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_x6797_42255_445400322}

[**[undo robust-count]{lang="EN-US"}**]{#struct_0_x6797_42255_461746747}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x403282619}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x583792759}[查询器的健壮系数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_444941569}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_809816447}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1964000454}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_444876033}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1963339573}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_749872049}

[*[count]{lang="EN-US"}*]{#struct_0_x6797_42255_444810497}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1545100291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_96617389}[查询器的健壮系数是为了弥补可能发生的网络丢包而设置的报文重传次数，健壮系数越大，]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器就越"健壮"，但是组播组超时所需的时间也就越长。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{style="font-family:宋体"}**[igmp robust-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x952917986}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_444744961}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_2135378123}[在公网实例中全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_x407327535}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] robust-count 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445203713}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp ]{lang="EN-US"}[robust-count]{lang="EN-US"}**]{#struct_0_x6797_42255_587194320}
:::

::: {#-2028090099 .myid}
[]{#_Toc404789616}[]{#struct_0_x6797_42255_1324827037}[]{#_Toc360705937}[]{#_Toc306713291}[]{#_Toc293993316}

**IGMP \-- IGMP配置命令 \-- ssm-mapping (IGMP view)**

------------------------------------------------------------------------

[**[ssm-mapping]{lang="EN-US"}**]{#struct_0_x6797_42255_1324761501}[命令用来配置]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ssm-mapping**]{lang="EN-US"}]{#struct_0_x6797_42255_896903194}[命令用来删除]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1324958109}

[**[ssm-mapping]{lang="EN-US"}**[ *source-address* *acl-number*]{lang="EN-US"}]{#struct_0_x6797_42255_2051856273}

[**[undo ssm-mapping]{lang="EN-US"}**[ { *source-address* \| **all** }]{lang="EN-US"}]{#struct_0_x6797_42255_1324892573}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x695329773}

[[未配置]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}]{#struct_0_x6797_42255_1325089181}[规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_868502859}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_1325023645}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_878481845}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1325220253}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_517223461}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1325154717}

[*[source-address]{lang="EN-US"}*]{#struct_0_x6797_42255_919363926}[：指定组播源地址。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x6797_42255_1325351325}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。通过该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中的]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[语句指定组播组的范围。当指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则表示未指定任何组播组。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6797_42255_914335904}[：删除所有的]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[规则。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1525725945}

[[ACL]{lang="EN-US"}]{#struct_0_x6797_42255_x74122347}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[组播组的范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1325285789}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_1324827036}[在公网实例中添加如下一条]{style="font-family:宋体"}[IGMP SSM Mapping]{lang="EN-US"}[规则：组地址范围为]{style="font-family:宋体"}[232.1.1.0/24]{lang="EN-US"}[，对应的源地址为]{style="font-family:宋体"}[125.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_916635198}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 232.1.1.1 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] ssm-mapping 125.1.1.1 2001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1324761500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x6797_42255_896837658}**[igmp]{lang="EN-US"}[ ssm-mapping]{lang="EN-US"}**
:::

::: {#1886657045 .myid}
[]{#_Toc404789617}[]{#struct_0_x6797_42255_445072641}[]{#_Toc372205825}[]{#_Toc371343414}[]{#_Toc368325572}[]{#_Toc368294510}

**IGMP \-- IGMP配置命令 \-- startup-query-count (IGMP view)**

------------------------------------------------------------------------

[**[startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x57191216}[命令用来全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询次数。]{style="font-family:宋体"}

[**[undo startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x980882409}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445007105}

[**[startup-query-count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_x6797_42255_1477811056}

[**[undo startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_x1517109401}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445465857}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x383797845}[查询器的启动查询次数等于]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的健壮系数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_753509082}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_445400321}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_461746750}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_1553032512}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x1988543525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_444941568}

[*[count]{lang="EN-US"}*]{#struct_0_x6797_42255_809816446}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1964000455}

[[本命令与]{style="font-family:宋体"}**[igmp startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_444876032}[命令的功能相同，只是作用范围不同：]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1963339574}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_750330801}[在公网实例中全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_444810496}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] startup-query-count 5]{lang="EN-US"}

[]{#_Toc371343415}[]{#_Toc368325573}[]{#_Toc368294511}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_1545100292}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp ]{lang="EN-US"}[startup-query-count]{lang="EN-US"}**]{#struct_0_x6797_42255_96420781}
:::

::: {#-831152917 .myid}
[]{#_Toc404789618}[]{#struct_0_x6797_42255_444744960}[]{#_Toc372205826}

**IGMP \-- IGMP配置命令 \-- startup-query-interval (IGMP view)**

------------------------------------------------------------------------

[**[startup-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_2135378122}[命令用来全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询间隔。]{style="font-family:宋体"}

[**[undo startup-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_x407261999}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445203712}

[**[startup-query-interval]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x6797_42255_587194319}

[**[undo startup-query-interval]{lang="EN-US"}**]{#struct_0_x6797_42255_1575720848}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x789695327}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_445138176}[查询器的启动查询间隔为]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[普遍组查询报文发送间隔的]{style="font-family:宋体"}[1/4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x482960562}

[[IGMP]{lang="EN-US"}]{#struct_0_x6797_42255_x725465783}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445072640}

[[network-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x57191215}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6797_42255_x980882412}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445007104}

[*[interval]{lang="EN-US"}*]{#struct_0_x6797_42255_1477811055}[：指定]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31744]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6797_42255_x1517174937}

[[本命令与]{style="font-family:宋体"}**[igmp]{lang="EN-US"}**[ **startup-query-interval**]{lang="EN-US"}]{#struct_0_x6797_42255_1150101572}[命令的功能相同，只是作用范围不同：]{style="font-family:
宋体"}[IGMP]{lang="EN-US"}[视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445465856}

[[\# ]{lang="EN-US"}]{#struct_0_x6797_42255_x383797846}[在公网实例中全局配置]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器的启动查询间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6797_42255_753443546}

[\[Sysname\] igmp]{lang="EN-US"}

[\[Sysname-igmp\] startup-query-interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6797_42255_445400320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[igmp]{lang="EN-US"}**]{#struct_0_x6797_42255_461746749}[ ]{lang="EN-US"}**[startup-query-interval]{lang="EN-US"}**

[ ]{lang="EN-US"}
:::
