::: {#1637782619 .myid}
[]{#_Toc404789397}[]{#struct_0_63644_x9153_x1317783360}[]{#_Toc300304084}[]{#_Toc135730194}[]{#_Toc135128925}[]{#_Toc94588332}[]{#_Toc80176757}[]{#_Toc59873210}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**组播路由与转发 \-- 组播路由与转发调试命令 \-- debugging mfib**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_63644_x9153_2076225538}

[**[debugging mfib]{lang="EN-US"}**[ \[ **multicast-vlan** \| **vpn-instance** *vpn-instance-name* \] { **all** \| **error** \| **mtunnel** \| **no-cache** \| **packet** \| **register** \| **route** \| **upcall** \| **wrong-iif** }]{lang="EN-US"}]{#struct_0_63644_x9153_x884898284}

[**[undo debugging mfib]{lang="EN-US"}**[ \[ **multicast-vlan** \| **vpn-instance** *vpn-instance-name* \] { **all** \| **error** \| **mtunnel** \| **no-cache** \| **packet** \| **register** \| **route** \| **upcall** \| **wrong-iif** }]{lang="EN-US"}]{#struct_0_63644_x9153_x1970364258}

[[【视图】]{style="font-family:黑体"}]{#struct_0_63644_x9153_824294141}

[[用户视图]{style="font-family:宋体"}]{#struct_0_63644_x9153_967365408}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_63644_x9153_x717441209}

[[network-admin]{lang="EN-US"}]{#struct_0_63644_x9153_x1411424767}

[[mdc-admin]{lang="EN-US"}]{#struct_0_63644_x9153_1449360196}

[[【参数】]{style="font-family:黑体"}]{#struct_0_63644_x9153_x1544076302}

[**[multicast-vlan]{lang="EN-US"}**]{#struct_0_63644_x9153_1147521608}[：指定组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_63644_x9153_1853142990}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_63644_x9153_998718389}[：表示]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Multicast Forwarding Information Base]{lang="EN-US"}[，组播转发信息库）的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_63644_x9153_x1592254263}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[mtunnel]{lang="EN-US"}**]{#struct_0_63644_x9153_x119457942}[：表示]{style="font-family:宋体"}[MFIB MTI]{lang="EN-US"}[（]{style="font-family:宋体"}[Multicast Tunnel Interface]{lang="EN-US"}[，组播隧道接口）接口调试信息开关。]{style="font-family:宋体"}

[**[no-cache]{lang="EN-US"}**]{#struct_0_63644_x9153_343885628}[：表示]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[未匹配报文调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_63644_x9153_x717244601}[：表示]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[register]{lang="SV"}**]{#struct_0_63644_x9153_x1417108378}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[注册报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[route]{lang="EN-US"}**]{#struct_0_63644_x9153_x1023273139}[：表示]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[路由调试信息开关。]{style="font-family:宋体"}

[**[upcall]{lang="EN-US"}**]{#struct_0_63644_x9153_x27284313}[：表示]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[上报]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[相关]{style="font-family:宋体"}[报文调试信息开关。]{style="font-family:宋体"}

[**[wrong-iif]{lang="EN-US"}**]{#struct_0_63644_x9153_797341599}[：表示]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[错误入接口的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_63644_x9153_1273657445}

[**[debugging mfib]{lang="EN-US"}**]{#struct_0_63644_x9153_x1961067576}[命令用来打开]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging mfib]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MFIB]{lang="EN-US"}]{#struct_0_63644_x9153_x1911696861}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定]{style="font-family:宋体"}**[multicast-vlan]{lang="EN-US"}**]{#struct_0_63644_x9153_x1577172451}[和]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数，表示公网实例。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mfib error]{lang="EN-US"}]{#struct_0_63644_x9153_x717310137}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x922196391}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_x637087144}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_x323910695}

[[failed]{lang="EN-US"}]{#struct_0_63644_x9153_247136710}

[[失败]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1167888662}

[[not found]{lang="EN-US"}]{#struct_0_63644_x9153_1931244172}

[[没有查到]{style="font-family:宋体"}]{#struct_0_63644_x9153_1169900274}

[[dummy entry]{lang="EN-US"}]{#struct_0_63644_x9153_x717113529}

[[空转发表项]{style="font-family:宋体"}]{#struct_0_63644_x9153_x998083510}

[[(*sadd, gadd*)]{lang="EN-US"}]{#struct_0_63644_x9153_x1595553937}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_63644_x9153_1161323916}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Memory allocation]{lang="EN-US"}]{#struct_0_63644_x9153_x790318655}

[[内存分配]{style="font-family:宋体"}]{#struct_0_63644_x9153_1165328646}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging mfib mtunnel]{lang="EN-US"}]{#struct_0_63644_x9153_x717179065}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x920331867}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_x682360236}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_x2051193691}

[[MTunnel create]{lang="EN-US"}]{#struct_0_63644_x9153_1725107357}

[[通知驱动创建]{style="font-family:宋体"}[MTI]{lang="EN-US"}]{#struct_0_63644_x9153_x536494296}[接口]{style="font-family:宋体"}

[[MTunnel delete]{lang="EN-US"}]{#struct_0_63644_x9153_x1180692433}

[[通知驱动删除]{style="font-family:宋体"}[MTI]{lang="EN-US"}]{#struct_0_63644_x9153_x738363010}[接口]{style="font-family:宋体"}

[[MTunnel up]{lang="EN-US"}]{#struct_0_63644_x9153_x717637820}

[[通知驱动]{style="font-family:宋体"}[MTI]{lang="EN-US"}]{#struct_0_63644_x9153_1660438391}[接口]{style="font-family:宋体"}[up]{lang="EN-US"}

[[MTunnel down]{lang="EN-US"}]{#struct_0_63644_x9153_x218190216}

[[通知驱动]{style="font-family:宋体"}[MTI]{lang="EN-US"}]{#struct_0_63644_x9153_1615647259}[接口]{style="font-family:宋体"}[down]{lang="EN-US"}

[[source addr]{lang="EN-US"}]{#struct_0_63644_x9153_474184058}

[[封装的源地址]{style="font-family:宋体"}]{#struct_0_63644_x9153_215756130}

[[group addr]{lang="EN-US"}]{#struct_0_63644_x9153_409052184}

[[封装的目的地址]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717703356}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mfib no-cache]{lang="EN-US"}]{#struct_0_63644_x9153_x609979151}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x893272783}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_1969228596}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_1918283565}

[[NoCache packet]{lang="EN-US"}]{#struct_0_63644_x9153_145532824}

[[未匹配的组播数据报文]{style="font-family:宋体"}]{#struct_0_63644_x9153_1959053832}

[[Report NoCache upcall]{lang="EN-US"}]{#struct_0_63644_x9153_298239809}

[[上报未知组播数据报文信息]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717506748}

[[(*sadd, gadd*)]{lang="EN-US"}]{#struct_0_63644_x9153_x614483017}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_63644_x9153_1245344972}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging mfib packet]{lang="EN-US"}]{#struct_0_63644_x9153_x1840418420}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x889935303}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_848690574}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_x1821255379}

[[Dropping]{lang="EN-US"}]{#struct_0_63644_x9153_1041015793}

[[丢弃组播数据报文]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717572284}

[[received]{lang="EN-US"}]{#struct_0_63644_x9153_145221967}

[[收到组播数据报文]{style="font-family:宋体"}]{#struct_0_63644_x9153_1715164561}

[[(*sadd, gadd*)]{lang="EN-US"}]{#struct_0_63644_x9153_x2122459273}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_63644_x9153_1802590678}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_63644_x9153_x141417662}

[[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_63644_x9153_x717375676}[值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging mfib register]{lang="EN-US"}]{#struct_0_63644_x9153_140193829}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x890486201}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_686344100}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_x1416779170}

[[Send]{lang="EN-US"}]{#struct_0_63644_x9153_x1277576423}

[[发送]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1943215369}

[[Dropping ]{lang="EN-US"}]{#struct_0_63644_x9153_694345034}

[[丢弃]{style="font-family:宋体"}]{#struct_0_63644_x9153_1793664465}

[[register]{lang="EN-US"}]{#struct_0_63644_x9153_x717441212}

[[注册报文]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1411883518}

[[register-stop]{lang="EN-US"}]{#struct_0_63644_x9153_1618434633}

[[注册停止报文]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1382164721}

[[(*sadd, gadd*)]{lang="EN-US"}]{#struct_0_63644_x9153_1516116448}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_63644_x9153_x1306726849}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging mfib route]{lang="EN-US"}]{#struct_0_63644_x9153_x717244604}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x896981549}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_x1416911770}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_1087105789}

[[add-entry message]{lang="EN-US"}]{#struct_0_63644_x9153_869383762}

[[添加表项消息]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1539053606}

[[delete-entry message]{lang="EN-US"}]{#struct_0_63644_x9153_1390271132}

[[删除表项消息]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1726880687}

[[set-IIF message]{lang="EN-US"}]{#struct_0_63644_x9153_x717310140}

[[更改入接口消息]{style="font-family:宋体"}]{#struct_0_63644_x9153_x637152681}

[[delete-OIF message]{lang="EN-US"}]{#struct_0_63644_x9153_1657785149}

[[删除出接口消息]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1769349724}

[[add-OIF message]{lang="EN-US"}]{#struct_0_63644_x9153_x630131517}

[[添加出接口消息]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1104188045}

[[(*sadd, gadd*)]{lang="EN-US"}]{#struct_0_63644_x9153_x717113532}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_63644_x9153_x998673335}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[ ]{lang="PT-BR"}

[[表1-7 ]{lang="EN-US"}[debugging mfib upcall]{lang="EN-US"}]{#struct_0_63644_x9153_x1231042413}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x895116961}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_477245189}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_x435901469}

[[Report NoCache upcall]{lang="EN-US"}]{#struct_0_63644_x9153_x453480873}

[[上报未知组播报文信息]{style="font-family:宋体"}]{#struct_0_63644_x9153_x592973170}

[[(*sadd, gadd*)]{lang="EN-US"}]{#struct_0_63644_x9153_x717179068}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_63644_x9153_x682556844}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging mfib wrong-iif]{lang="EN-US"}]{#struct_0_63644_x9153_1488662020}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x900306810}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_1966247416}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_x1918335926}

[[WrongIF packet]{lang="EN-US"}]{#struct_0_63644_x9153_1870975206}

[[从错误入接口收到组播数据报文]{style="font-family:宋体"}]{#struct_0_63644_x9153_x383544911}

[[(*sadd, gadd*)]{lang="EN-US"}]{#struct_0_63644_x9153_x717637819}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_63644_x9153_1660897146}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_63644_x9153_x1872264444}

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_x1576476622}[在接口上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，打开]{style="font-family:宋体"}[公网实例]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[错误]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mfib error]{lang="EN-US"}]{#struct_0_63644_x9153_x976350830}

[\*Apr 26 12:53:18:967 2000 Sysname MFIB/7/ERROR: -MDC=1; Memory allocation is failed (A062115)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x533331423}*[分配内存失败]{style="font-family:宋体"}*

[[\*Apr 26 12:53:18:979 2000 Sysname MFIB/7/DRIVER: -MDC=1; Failed to create entry ]{lang="EN-US"}]{#struct_0_63644_x9153_x933728844}[（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）]{style="font-family:宋体"}[. (A062520)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_644581258}*[创建转发表项（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_x717703355}[打开公网实例]{style="font-family:宋体"}[MFIB MTI]{lang="EN-US"}[接口调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mfib mtunnel]{lang="EN-US"}]{#struct_0_63644_x9153_x610044687}

[\*Apr 26 12:53:18:967 2000 Sysname MFIB/7/MTUNNEL: -MDC=1; MTunnel create, ifindex=469. (A20732)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_1517855772}*[通知驱动创建]{style="font-family:宋体"}[MTI]{lang="EN-US"}[接口]{style="font-family:宋体"}*

[[\*Apr 26 12:53:18:967 2000 Sysname MFIB/7/MTUNNEL: -MDC=1; MTunnel up, ifindex=469, source addr=1.1.1.1, group addr=239.1.1.1. (A20788)]{lang="EN-US"}]{#struct_0_63644_x9153_x2035916300}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x1838101202}*[通知驱动]{style="font-family:宋体"}[MTI]{lang="EN-US"}[接口]{style="font-family:宋体"}[up]{lang="EN-US"}[，封装的源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，封装的目的地址为]{style="font-family:宋体"}[239.1.1.1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_x371652873}[在接口上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，打开公网实例]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[未匹配报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mfib no-cache]{lang="EN-US"}]{#struct_0_63644_x9153_x21435400}

[\*Apr 26 12:43:19:09 2000 Sysname MFIB/7/NO-CACHE: -MDC=1; Packet ]{lang="EN-US"}[（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）]{style="font-family:宋体"} [matched nothing (A08303)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x827677528}*[收到无匹配转发表项的组播数据报文（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[Succeeded to send no-cache upcall (3.4.5.6]{lang="EN-US"}]{#struct_0_63644_x9153_x717506747}[，]{style="font-family:宋体"}[226.1.1.1) (A08453)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x615072841}*[向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[上报没有转发表项（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）的信息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_x1031280514}[在接口上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，打开公网实例]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mfib packet]{lang="EN-US"}]{#struct_0_63644_x9153_812714873}

[\*Apr 26 12:28:50:578 2000 Sysname MFIB/7/PACKET: -MDC=1; Receive packet (3.4.5.6]{lang="EN-US"}[，]{style="font-family:
宋体"}[226.1.1.1) from interface Vlan-interface20, ttl is 128 (A012942)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_1703539297}*[从接口]{style="font-family:宋体"}[Vlan-interface20]{lang="EN-US"}[收到]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值为]{style="font-family:宋体"}[128]{lang="EN-US"}[的组播数据报文（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Apr 26 12:28:50:625 2000 Sysname MFIB/7/PACKET: -MDC=1; Forward multicast packet (3.4.5.6, 226.1.1.1) on GigabitEthernet1/0/1 (A083551)]{lang="EN-US"}]{#struct_0_63644_x9153_x1734198080}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x1241468355}*[将组播数据报文（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）通过端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[转发出去]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_x29076024}[分别在两台设备的接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[RP]{lang="EN-US"}[和]{style="font-family:宋体"}[BSR]{lang="EN-US"}[，打开公网实例]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[注册报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mfib register]{lang="NO-BOK"}]{#struct_0_63644_x9153_x1514789308}

[\*Apr 26 13:29:33:753 2000 Sysname MFIB/7/REGISTER:]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[-MDC=1; Received register packet from 22.1.1.1 to 10.1.1.1, with data packet: (22.1.1.10, 226.1.1.1)(A086218)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x717572283}*[收到由]{style="font-family:宋体"}[22.1.1.1]{lang="EN-US"}[发往]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的、封装有组播数据报文（]{style="font-family:宋体"}[22.1.1.10]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）的注册报文]{style="font-family:宋体"}*

[[\*Apr 26 13:29:33:763 2000 Sysname MFIB/7/REGISTER:]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[-MDC=1; Send register-stop packet to 22.1.1.1 for (22.1.1.10, 226.1.1.1).(A085970)]{lang="EN-US"}]{#struct_0_63644_x9153_145549647}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x1514051352}*[向]{style="font-family:宋体"}[22.1.1.1]{lang="EN-US"}[发送（]{style="font-family:宋体"}[22.1.1.10]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）的注册停止报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_x1093358422}[在接口上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，打开公网实例]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[路由调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mfib route]{lang="EN-US"}]{#struct_0_63644_x9153_x1368325209}

[\*Apr 26 12:39:59:272 2000 Sysname MFIB/6/ROUTE: -MDC=1; Add dummy entry (3.4.5.6, 226.1.1.1)(A07120)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x1596317304}*[收到无匹配转发表项的组播数据报文（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[），为其创建临时转发表项]{style="font-family:宋体"}*

[[\*Apr 26 12:39:59:297 2000 Sysname MFIB/6/ROUTE: -MDC=1; Receive add-entry message of entry (3.4.5.6, 226.1.1.1), oif num is 1.(A112030)]{lang="EN-US"}]{#struct_0_63644_x9153_x1227508214}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x2130519294}*[收到]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[通知添加（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）表项的消息，表项的出接口数目为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Apr 26 12:39:59:327 2000 Sysname MFIB/6/ROUTE: -MDC=1; Change dummy entry (3.4.5.6, 226.1.1.1) to normal (A07391)]{lang="EN-US"}]{#struct_0_63644_x9153_1976693413}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x717375675}*[删除临时转发表项（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[），并添加相应的正式转发表项]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_139997221}[在接口上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，打开]{style="font-family:宋体"}[公网实例]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[上报]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[相关]{style="font-family:宋体"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mfib upcall]{lang="EN-US"}]{#struct_0_63644_x9153_69234257}

[\*Sep  7 21:10:08:130 2006 Sysname MFIB/7/UPCALL: -MDC=1; Succeeded to send no-cache upcall (3.4.5.6, 226.1.1.1) (A08453)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x1722497687}*[向]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[上报未匹配报文（]{style="font-family:宋体"}[3.4.5.6]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[）的消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_446506544}[在接口]{style="font-family:宋体"}[VLAN-interface40]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN-interface60]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，发送相同源组的组播数据报文，打开]{style="font-family:宋体"}[公网实例]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[错误入接口调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mfib wrong-iif]{lang="EN-US"}]{#struct_0_63644_x9153_1167033804}

[\*Jan 24 04:36:52:990 2003 Sysname MFIB/7/WRONGIIF: -MDC=1; Slot=3; WRONG_IF packet (10.11.113.168, 226.1.1.1) received on Vlan-interface60, should from Vlan-interface40(A08734)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_1109438877}*[从错误入接口]{style="font-family:宋体"}[Vlan-interface60]{lang="EN-US"}[收到组播数据报文（]{style="font-family:宋体"}[10.11.113.168]{lang="EN-US"}[，]{style="font-family:宋体"}[226.1.1.1]{lang="EN-US"}[），正确的入接口应为]{style="font-family:宋体"}[Vlan-interface40]{lang="EN-US"}*

::: {#-656239525 .myid}
[]{#_Toc404789398}[]{#struct_0_63644_x9153_x981153733}[]{#_Toc300304085}[]{#_Toc280695264}

**组播路由与转发 \-- 组播路由与转发调试命令 \-- debugging mrib**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_63644_x9153_1919078347}

[**[debugging mrib]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **error** \| **event** \| **interface** \[ *interface-type* *interface-number* \] \| **proxy** \[ **event** \| **routing-table** \] \| **route** \[ *advanced-acl-number* \] }]{lang="EN-US"}]{#struct_0_63644_x9153_x717441211}

[**[undo debugging mrib]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **error** \| **event** \| **interface** \| **proxy** \[ **event** \| **routing-table** \] \| **route** }]{lang="EN-US"}]{#struct_0_63644_x9153_x1411949054}

[[【视图】]{style="font-family:黑体"}]{#struct_0_63644_x9153_1983432996}

[[用户视图]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1678078529}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_63644_x9153_x1996735671}

[[network-admin]{lang="EN-US"}]{#struct_0_63644_x9153_1267561166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_63644_x9153_437700542}

[[【参数】]{style="font-family:黑体"}]{#struct_0_63644_x9153_x24740397}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_63644_x9153_x717244603}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_63644_x9153_x1416977306}[：表示]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Multicast Routing Information Base]{lang="EN-US"}[，组播路由信息库）的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="SV"}**]{#struct_0_63644_x9153_1038733793}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="SV"}**]{#struct_0_63644_x9153_1496746318}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MRIB]{lang="SV"}[事件调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="SV"}**]{#struct_0_63644_x9153_x867417725}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MRIB]{lang="SV"}[接口管理调试信息开关。]{style="font-family:宋体"}

[*[interface-type]{lang="SV"}*]{#struct_0_63644_x9153_x866823805}[ *interface-number*]{lang="SV"}[：]{style="font-family:宋体"}[表示指定接口的]{style="font-family:宋体"}[MRIB]{lang="SV"}[接口管理调试信息开关。如果未指定本参数，表示所有接口的]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[接口管理调试信息开关。]{style="font-family:宋体"}

[**[proxy]{lang="SV"}**]{#struct_0_63644_x9153_1851437630}[ \[ **event** \| **routing-table** \]]{lang="SV"}[：表示]{style="font-family:
宋体"}[IGMP]{lang="SV"}[代理调试信息开关，包括事件（]{style="font-family:宋体"}**[event]{lang="SV"}**[）和路由表（]{style="font-family:宋体"}**[routing-table]{lang="SV"}**[）两种。如果未指定]{style="font-family:宋体"}**[event]{lang="SV"}**[和]{style="font-family:宋体"}**[routing-table]{lang="SV"}**[参数，表示同时包括这两种调试信息开关。]{style="font-family:宋体"}

[**[route]{lang="EN-US"}**]{#struct_0_63644_x9153_x2030403687}[：表示]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[路由表项调试信息开关。]{style="font-family:宋体"}

[*[advanced-acl-number]{lang="EN-US"}*]{#struct_0_63644_x9153_832126940}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_63644_x9153_1925343006}

[**[debugging mrib]{lang="EN-US"}**]{#struct_0_63644_x9153_x717310139}[命令用来打开]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging mfib]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MRIB]{lang="EN-US"}]{#struct_0_63644_x9153_x636693928}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging mrib error]{lang="EN-US"}]{#struct_0_63644_x9153_76765037}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x901167730}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_x2075944676}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_77405235}

[[multicast routing]{lang="EN-US"}]{#struct_0_63644_x9153_1608040117}

[[组播路由]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1519574038}

[[MBoundary]{lang="EN-US"}]{#struct_0_63644_x9153_x1231202118}

[[组播边界]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717113531}

[[MFIB]{lang="EN-US"}]{#struct_0_63644_x9153_x998607799}

[[组播转发信息库]{style="font-family:宋体"}]{#struct_0_63644_x9153_330996489}

[[iif]{lang="EN-US"}]{#struct_0_63644_x9153_848620726}

[[入接口]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1792413940}

[[oif]{lang="EN-US"}]{#struct_0_63644_x9153_x527371926}

[[出接口]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717179067}

[[spt thres]{lang="EN-US"}]{#struct_0_63644_x9153_x682229164}

[[SPT]{lang="EN-US"}]{#struct_0_63644_x9153_x2026236924}[切换阈值]{style="font-family:宋体"}

[[reg suppress]{lang="EN-US"}]{#struct_0_63644_x9153_870247221}

[[注册抑制]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1714400297}

[[flush mrt table]{lang="EN-US"}]{#struct_0_63644_x9153_x819831113}

[[下刷路由表]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717637822}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging mrib event]{lang="EN-US"}]{#struct_0_63644_x9153_1660569463}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x898825735}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_x199875863}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_2108589176}

[[Multicast Boundary]{lang="EN-US"}]{#struct_0_63644_x9153_1757819136}

[[组播边界]{style="font-family:宋体"}]{#struct_0_63644_x9153_720655432}

[[Multicast routing]{lang="EN-US"}]{#struct_0_63644_x9153_857136175}

[[组播路由]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717703358}

[[MFIB]{lang="EN-US"}]{#struct_0_63644_x9153_x609323791}

[[组播转发信息库]{style="font-family:宋体"}]{#struct_0_63644_x9153_61111420}

[[spt thres]{lang="EN-US"}]{#struct_0_63644_x9153_x29357236}

[[SPT]{lang="EN-US"}]{#struct_0_63644_x9153_332676306}[切换阈值]{style="font-family:宋体"}

[[reg suppress]{lang="EN-US"}]{#struct_0_63644_x9153_x779056812}

[[注册抑制]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717506750}

[[Add msg to ipc buffer]{lang="EN-US"}]{#struct_0_63644_x9153_x615007306}

[[向]{style="font-family:宋体"}[IPC]{lang="EN-US"}]{#struct_0_63644_x9153_x1872673197}[缓冲区中添加一个消息]{style="font-family:宋体"}

[[Send msg to MFIB success]{lang="EN-US"}]{#struct_0_63644_x9153_x1981336053}

[[成功向]{style="font-family:宋体"}[MFIB]{lang="EN-US"}]{#struct_0_63644_x9153_145524945}[发送一个消息]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_63644_x9153_x374516333}

[[消息类型]{style="font-family:宋体"}]{#struct_0_63644_x9153_x717572286}

[[Len]{lang="EN-US"}]{#struct_0_63644_x9153_145353039}

[[消息长度]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1766120329}

[[Count]{lang="EN-US"}]{#struct_0_63644_x9153_1910324909}

[[消息数量]{style="font-family:宋体"}]{#struct_0_63644_x9153_x110962764}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging mrib interface]{lang="EN-US"}]{#struct_0_63644_x9153_573499846}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x902293745}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_x717375678}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_139800613}

[[Succeed in adding interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x729988636}

[[成功添加接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_710715029}

[[Remove interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_435817038}

[[删除接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x1096872011}

[[Create interface address for (*interface*, *address*), reference *cnt*]{lang="EN-US"}]{#struct_0_63644_x9153_x701017567}

[[创建接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x717441214}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*

[[Remove interface address *address* of *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x1411752446}

[[删除接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_2069040805}[的地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[Create interface address for (*interface*, *address*) while exist, reference *cnt*]{lang="EN-US"}]{#struct_0_63644_x9153_x1981593781}

[[创建接口地址时，地址已经存在，增加它的引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_63644_x9153_1473200672}

[[Create interface address for (*interface*, *address*) when sending message, reference *cnt*]{lang="EN-US"}]{#struct_0_63644_x9153_1060058442}

[[发送接口变化消息时，创建接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_63644_x9153_x717244606}

[[Create interface address for (*interface*, *address*) when getting by index, reference *cnt*]{lang="EN-US"}]{#struct_0_63644_x9153_x1416780698}

[[根据接口索引获取接口上的接口地址时，创建接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_63644_x9153_1759337235}

[[Create interface address for (*interface*, *address*) when getting by address, reference *cnt*]{lang="EN-US"}]{#struct_0_63644_x9153_190838003}

[[根据全局]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_63644_x9153_1162093584}[地址获取接口上的接口地址时，创建接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*

[[Destroy interface address for (*interface*, *address*) when deleting it, reference *cnt*]{lang="EN-US"}]{#struct_0_63644_x9153_x187125355}

[[销毁接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_63644_x9153_x717310142}

[[Create interface address for (*interface*, *address*) at (*file*, *line*), reference *cnt* ]{lang="EN-US"}]{#struct_0_63644_x9153_x637283753}

[[在文件]{style="font-family:宋体"}*[file]{lang="EN-US"}*]{#struct_0_63644_x9153_855004808}[的]{style="font-family:宋体"}*[line]{lang="EN-US"}*[引用行创建接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*

[[Failed to create interface]{lang="EN-US"}]{#struct_0_63644_x9153_60351353}

[[创建接口失败]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1322599055}

[[Succeed in adding PIM interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x717113534}

[[成功添加]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_63644_x9153_x998280119}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Remove PIM interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x1234623102}

[[删除]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_63644_x9153_519284340}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Enable/Disable protocol packet deliver up on interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x1297422224}

[[使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_63644_x9153_x717179070}[关闭接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[协议功能]{style="font-family:宋体"}

[[Succeed in enabling/disabling PIM packet to CPU for interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x682032557}

[[使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_63644_x9153_x2032706868}[关闭接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[协议功能成功]{style="font-family:宋体"}

[[PIM interface *interface* is up/down]{lang="EN-US"}]{#struct_0_63644_x9153_117785281}

[[PIM]{lang="EN-US"}]{#struct_0_63644_x9153_x717637821}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[生效]{style="font-family:宋体"}[/]{lang="EN-US"}[失效]{style="font-family:宋体"}

[[No address or memory for PIM interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1660372855}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_2118532391}[没有配置地址或内存不足]{style="font-family:宋体"}

[[Message to add(*type*) interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x1553395832}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_441522915}[添加消息，消息子类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[Message to up interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x717703357}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x609913615}[生效消息]{style="font-family:宋体"}

[[Message to down(*type*) interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x1901691606}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x515584636}[失效消息，消息子类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[Message to change configuration of interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x717506749}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x614417481}[配置变化消息]{style="font-family:宋体"}

[[Ignore non-primary or borrow address of *interface*, state *state*]{lang="EN-US"}]{#struct_0_63644_x9153_62474047}

[[忽略从地址和借用地址逻辑接口变化消息]{style="font-family:宋体"}]{#struct_0_63644_x9153_x1445830460}

[[Message to add/delete address *address*/*masklen* (*interface*)]{lang="EN-US"}]{#struct_0_63644_x9153_x717572285}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_145156431}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*[/*masklen*]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Message to up/down vlink interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_706630147}

[[Vlink]{lang="EN-US"}]{#struct_0_63644_x9153_x717375677}[接口]{style="font-family:宋体"}*[interface ]{lang="EN-US"}*[up/down]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Vlink state of interface *interface* is not up, state *state* ]{lang="EN-US"}]{#struct_0_63644_x9153_140128293}

[[Vlink]{lang="EN-US"}]{#struct_0_63644_x9153_x803194125}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[状态不是]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[[Succeed in creating basic interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1012187977}

[[创建基本接口（注册口、]{style="font-family:宋体"}[Null0]{lang="EN-US"}]{#struct_0_63644_x9153_x717441213}[接口等）]{style="font-family:宋体"}

[[Succeed in destroying basic interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x1411817982}

[[删除基本接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_198639866}

[[Try to enable/disable protocol *pro* on interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x717244605}

[[尝试在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x1416846234}[上使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭协议]{style="font-family:宋体"}*[pro]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging mrib proxy]{lang="EN-US"}]{#struct_0_63644_x9153_1851503165}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1438514982}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_x461846889}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_1851437629}

[[Process gmp querier enable/disable for interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_x828705710}

[[为接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_1851372093}[使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭查询器]{style="font-family:宋体"}

[[Notify proxy up/down message on interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_305937399}

[[通报代理接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_1959312998}[生效]{style="font-family:宋体"}[/]{lang="EN-US"}[失效消息]{style="font-family:宋体"}

[[Add proxy interface for interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1851306557}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x823367281}[上添加代理功能]{style="font-family:宋体"}

[[Process proxy enable/disable message on interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1851241021}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x1262178122}[上处理代理功能使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭消息]{style="font-family:宋体"}

[[Delete proxy interface on interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1851175485}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x55583261}[上删除代理接口]{style="font-family:宋体"}

[[Proxy interface logup/logdown for interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1852158525}

[[代理接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x1409627704}[逻辑]{style="font-family:宋体"}[up/]{lang="EN-US"}[逻辑]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Notify proxy enable/disable message]{lang="EN-US"}]{#struct_0_63644_x9153_1852092989}

[[通报代理功能使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_63644_x9153_626801619}[关闭消息]{style="font-family:宋体"}

[[Proxy routing-table adjust timer expired]{lang="EN-US"}]{#struct_0_63644_x9153_1851634236}

[[代理路由表重整定时器超时]{style="font-family:宋体"}]{#struct_0_63644_x9153_x467774880}

[[Create/Delete proxy routing-table relate interface: *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1851568700}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x902313658}[上创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除代理路由表]{style="font-family:宋体"}

[[Create/Delete proxy routing-table adjust timer(*time*)]{lang="EN-US"}]{#struct_0_63644_x9153_1851503164}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_63644_x9153_x461781353}[删除代理路由表重整定时器（时间值为]{style="font-family:宋体"}*[time]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Could not find (\*,*group*), ignore the prune message]{lang="EN-US"}]{#struct_0_63644_x9153_1851437628}

[[没有找到（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_63644_x9153_x828771246}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）表项，忽略剪枝报文]{style="font-family:宋体"}

[[Receive gmp aux/ex join/prune for (*source*, *group*) on *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1851372092}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_305871863}[上收到（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）表项的加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文]{style="font-family:宋体"}

[[Relate (*source*, *group*) to proxy interface: *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1851306556}

[[将组]{style="font-family:宋体"}*[group]{lang="EN-US"}*]{#struct_0_63644_x9153_x823301745}[与代理接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[相关联]{style="font-family:宋体"}

[[Relate (*source*, *group*) to niif list]{lang="EN-US"}]{#struct_0_63644_x9153_1851241020}

[[将组]{style="font-family:宋体"}*[group]{lang="EN-US"}*]{#struct_0_63644_x9153_x1262112586}[与空接口列表相关联]{style="font-family:宋体"}

[[Create/Delete proxy routing-table (*source*, *group*)]{lang="EN-US"}]{#struct_0_63644_x9153_1851175484}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_63644_x9153_x55648797}[删除代理路由表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Failed to create entry (*source*, *group*) for reaching route limit]{lang="EN-US"}]{#struct_0_63644_x9153_1852158524}

[[由于超出规格，创建表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_63644_x9153_x1409693240}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）创建失败]{style="font-family:宋体"}

[[Add/Delete/Set iif: *interface* for (*source*, *group*)]{lang="EN-US"}]{#struct_0_63644_x9153_1851634235}

[[为表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_63644_x9153_x467578272}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更改入接口，并与该表项关联]{style="font-family:宋体"}[/]{lang="EN-US"}[解绑]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联]{style="font-family:宋体"}

[[Cannot add downstream *interface* for (*source*, *group*), since it is not in the immediate olist]{lang="EN-US"}]{#struct_0_63644_x9153_1851568699}

[[由于表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_63644_x9153_1435748687}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）不在直接出接口列表中，因此不能为该表项添加下游接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Cannot delete downstream *interface* for (*source*, *group*), since it is in the immediate olist]{lang="EN-US"}]{#struct_0_63644_x9153_1851503163}

[[由于表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_63644_x9153_x462240105}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）在直接出接口列表中，因此不能为该表项删除下游接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Add/Delete oif: *interface* for (*source*, *group*)]{lang="EN-US"}]{#struct_0_63644_x9153_1851437627}

[[为表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_63644_x9153_x829098926}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除出接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Notify MRIB to add/delete oif *interface* before adding entry (*source*, *group*)]{lang="EN-US"}]{#struct_0_63644_x9153_1851372091}

[[在添加表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_63644_x9153_306068471}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）之前，就通知]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除出接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Process multicast boundary message on proxy interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_2138080761}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_2137884153}[上处理组播边界消息]{style="font-family:宋体"}

[[Create multicast boundary timer on proxy interface *interface*]{lang="EN-US"}]{#struct_0_63644_x9153_1467102507}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_2137949689}[上创建组播边界定时器]{style="font-family:宋体"}

[[Multicast boundary timer on interface *interface* expired]{lang="EN-US"}]{#struct_0_63644_x9153_2138277369}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_63644_x9153_x277763455}[上的组播边界定时器超时]{style="font-family:宋体"}

[[Process MFIB/MRIB reset entry message]{lang="EN-US"}]{#struct_0_63644_x9153_2138342905}

[[处理]{style="font-family:宋体"}[MFIB/MRIB]{lang="EN-US"}]{#struct_0_63644_x9153_x1900154579}[表项删除消息]{style="font-family:宋体"}

[[Create flush entry timer]{lang="EN-US"}]{#struct_0_63644_x9153_2137753080}

[[创建表项下刷定时器]{style="font-family:宋体"}]{#struct_0_63644_x9153_2137818616}

[[Proxy flush entry timer expired]{lang="EN-US"}]{#struct_0_63644_x9153_1057008747}

[[表项下刷定时器超时]{style="font-family:宋体"}]{#struct_0_63644_x9153_2137622008}

[[Delete all expand oif from sg entry when delete (\*, *group*)]{lang="EN-US"}]{#struct_0_63644_x9153_2137687544}

[[在删除（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_63644_x9153_x863327473}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）表项时，同时删除对应（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项中的扩展出接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging mrib route]{lang="EN-US"}]{#struct_0_63644_x9153_1052297703}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x878939339}[[字段]{style="font-family:黑体"}]{#struct_0_63644_x9153_476509462}

[[描述]{style="font-family:黑体"}]{#struct_0_63644_x9153_x1521217226}

[[iif]{lang="EN-US"}]{#struct_0_63644_x9153_816094844}

[[入接口]{style="font-family:宋体"}]{#struct_0_63644_x9153_1560070568}

[[oif]{lang="EN-US"}]{#struct_0_63644_x9153_x717310141}

[[出接口]{style="font-family:宋体"}]{#struct_0_63644_x9153_x637218217}

[[Merge state]{lang="EN-US"}]{#struct_0_63644_x9153_1606846153}

[[抵消状态]{style="font-family:宋体"}]{#struct_0_63644_x9153_x955118564}

[[spt thres]{lang="EN-US"}]{#struct_0_63644_x9153_583636696}

[[SPT]{lang="EN-US"}]{#struct_0_63644_x9153_1411652362}[切换阈值]{style="font-family:宋体"}

[[reg suppress]{lang="EN-US"}]{#struct_0_63644_x9153_x717113533}

[[注册抑制]{style="font-family:宋体"}]{#struct_0_63644_x9153_x998738871}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_63644_x9153_1884258671}

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_x1231301923}[在接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mrib event]{lang="EN-US"}]{#struct_0_63644_x9153_x223523090}

[\*Dec 10 17:15:08:494 2010 Sysname MRIB/7/EVENT: -MDC=1; Add msg(Type: add mfib, Len: 146) to ipc buffer(Count: 1) (M02333)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x317694189}*[向]{style="font-family:宋体"}[IPC]{lang="EN-US"}[缓冲区中添加一个消息（消息类型为：往]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[添加表项，长度为]{style="font-family:宋体"}[146]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Dec 10 17:15:08:502 2010 Sysname MRIB/7/EVENT: -MDC=1; Send msg to MFIB(Count 1, Len 158) success (M02258)]{lang="EN-US"}]{#struct_0_63644_x9153_1958126931}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x2030016177}*[成功向]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[发送一个消息（数量为]{style="font-family:宋体"}[1]{lang="EN-US"}[，长度为]{style="font-family:宋体"}[158]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_1717011810}[在接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[接口管理调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mrib interface]{lang="EN-US"}]{#struct_0_63644_x9153_x717179069}

[\*Oct 30 06:16:27:689 2012 Sysname MRIB/7/IFM: -MDC=1; Try to enable protocol 0x2 on interface GigabitEthernet1/0/1. (PM055007)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x682622380}*[尝试在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[（]{style="font-family:宋体"}[protocol 0x2]{lang="EN-US"}[）协议]{style="font-family:宋体"}*

[[\*Oct 30 06:16:27:689 2012 Sysname MRIB/7/IFM: -MDC=1; Create interface address for (GigabitEthernet1/0/1, 7.11.0.1) when sending message, reference 1. (PM052755)]{lang="EN-US"}]{#struct_0_63644_x9153_x884122627}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x2039653585}*[增加接口地址引用计数，用于发送接口变化消息]{style="font-family:宋体"}*

[[\*Oct 30 06:16:27:695 2012 Sysname MRIB/7/IFM: -MDC=1; Succeed in adding PIM interface GigabitEthernet1/0/1. (PM052427)]{lang="EN-US"}]{#struct_0_63644_x9153_x958253917}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_1852544021}*[成功添加接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的生效]{style="font-family:宋体"}[PIM]{lang="EN-US"}[接口]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_1851175483}[在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理功能，并打开公网实例]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mrib proxy]{lang="EN-US"}]{#struct_0_63644_x9153_x55452189}

[\*May 10 18:20:44:858 2013 Sysname MRIB/7/PRY_RT: -MDC=1; Relate group 225.0.0.1 to nonif list. (MP051207)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_272072149}*[将组]{style="font-family:宋体"}[225.0.0.1]{lang="EN-US"}[与空接口列表相关联]{style="font-family:宋体"}*

[[\*May 10 18:20:44:858 2013 Sysname MRIB/7/PRY_EVT: -MDC=1; Delete proxy routing-table relate interface: Vlan-interface22. (MP05589)]{lang="EN-US"}]{#struct_0_63644_x9153_1852158523}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x1409758776}*[在接口]{style="font-family:宋体"}[Vlan-interface22]{lang="EN-US"}[上删除代理路由表]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_63644_x9153_x1375120896}[在接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[路由表项调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mrib route]{lang="EN-US"}]{#struct_0_63644_x9153_x876403820}

[\*Dec 10 17:15:08:390 2010 Sysname MRIB/7/ROUTE: -MDC=1; Proc add entry (2.1.1.1,225.0.0.25) msg with iif GigabitEthernet1/0/1(Oifs 1,RP 2.1.1.5) (M032598)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_x1885112548}*[处理添加表项（]{style="font-family:宋体"}[2.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）消息，表项入接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（出接口数量为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.1.1.5]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Dec 10 17:15:08:413 2010 Sysname MRIB/7/ROUTE: -MDC=1; Add oif GigabitEthernet1/0/1(Status ADD) to entry (2.1.1.1,225.0.0.25) (M032440)]{lang="EN-US"}]{#struct_0_63644_x9153_848446123}

[*[// ]{lang="EN-US"}*]{#struct_0_63644_x9153_311625009}*[将出接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（状态为]{style="font-family:宋体"}[ADD]{lang="EN-US"}[）添加到表项（]{style="font-family:宋体"}[2.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）中]{style="font-family:宋体"}*
