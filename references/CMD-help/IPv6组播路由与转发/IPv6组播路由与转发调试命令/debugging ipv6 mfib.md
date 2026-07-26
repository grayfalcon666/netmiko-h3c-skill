::: {#1179111878 .myid}
[]{#_Toc404790115}[]{#struct_0_15550_84251_2057057781}[]{#_Toc135730194}[]{#_Toc135128925}[]{#_Toc94588332}[]{#_Toc80176757}[]{#_Toc59873210}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**IPv6组播路由与转发 \-- IPv6组播路由与转发调试命令 \-- debugging ipv6 mfib**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15550_84251_657582155}

[**[debugging ipv6 mfib]{lang="EN-US"}**[ \[ **multicast-vlan** \| **vpn-instance** *vpn-instance-name* \] { **all** \| **error** \| **no-cache** \| **packet** \| **register** \| **route** \| **upcall** \| **wrong-iif** }]{lang="EN-US"}]{#struct_0_15550_84251_729129969}

[**[undo debugging ipv6]{lang="EN-US"}**[ ]{lang="EN-US"}**[mfib]{lang="EN-US"}**[ \[ **multicast-vlan** \| **vpn-instance** *vpn-instance-name* \] { **all** \| **error** \| **no-cache** \| **packet** \| **register** \| **route** \| **upcall** \| **wrong-iif** }]{lang="EN-US"}]{#struct_0_15550_84251_468264313}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15550_84251_x301508238}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15550_84251_624072218}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15550_84251_x75809780}

[[network-admin]{lang="EN-US"}]{#struct_0_15550_84251_576307559}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15550_84251_x1811379753}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15550_84251_x1512187819}

[**[multicast-vlan]{lang="EN-US"}**]{#struct_0_15550_84251_679794523}[：指定组播]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_15550_84251_x830301794}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_15550_84251_x565351008}[：表示]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Multicast Forwarding Information Base]{lang="EN-US"}[，组播转发信息库）的所有调试信息开关。]{style="font-family:
宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_15550_84251_x2132437603}[：表示]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[no-cache]{lang="EN-US"}**]{#struct_0_15550_84251_x301573774}[：表示]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[未匹配报文调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_15550_84251_x1270645589}[：表示]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[register]{lang="SV"}**]{#struct_0_15550_84251_x1811604862}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[注册报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[route]{lang="EN-US"}**]{#struct_0_15550_84251_x214366746}[：表示]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[路由调试信息开关。]{style="font-family:宋体"}

[**[upcall]{lang="EN-US"}**]{#struct_0_15550_84251_735427446}[：表示]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[上报]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[相关]{style="font-family:宋体"}[报文调试信息开关。]{style="font-family:宋体"}

[**[wrong-iif]{lang="EN-US"}**]{#struct_0_15550_84251_x1185007389}[：表示]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[错误入接口的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15550_84251_x1838563199}

[**[debugging ipv6 mfib]{lang="EN-US"}**]{#struct_0_15550_84251_x347335615}[命令用来打开]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 mfib]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}]{#struct_0_15550_84251_x630017251}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定]{style="font-family:宋体"}**[multicast-vlan]{lang="EN-US"}**]{#struct_0_15550_84251_66946010}[和]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数，表示公网实例。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ipv6 mfib error]{lang="EN-US"}]{#struct_0_15550_84251_x301639310}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_116513040}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_1004145430}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_1505651409}

[[Failed to allocate memory for add entry/add OIF/RP]{lang="EN-US"}]{#struct_0_15550_84251_x520841150}

[[添加表项]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_x541821325}[添加出接口]{style="font-family:宋体"}[/]{lang="EN-US"}[设置]{style="font-family:宋体"}[RP]{lang="EN-US"}[时分配内存失败]{style="font-family:宋体"}

[[Failed to create entry (*src*, *dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x44136850}

[[创建转发表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_937473477}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）失败]{style="font-family:宋体"}

[[Failed to allocate memory for outgoing interface list]{lang="EN-US"}]{#struct_0_15550_84251_x301704846}

[[创建出接口列表时分配内存失败]{style="font-family:宋体"}]{#struct_0_15550_84251_682673133}

[[Failed to convert outgoing interface list]{lang="EN-US"}]{#struct_0_15550_84251_1626900976}

[[转换出接口列表失败]{style="font-family:宋体"}]{#struct_0_15550_84251_356528829}

[[Failed to construct driver message]{lang="EN-US"}]{#struct_0_15550_84251_x562452936}

[[创建下驱动信息失败]{style="font-family:宋体"}]{#struct_0_15550_84251_354880124}

[[Failed to flush entry (*src*, *dst*) to driver]{lang="EN-US"}]{#struct_0_15550_84251_x301770382}

[[表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x2072186483}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）下驱动失败]{style="font-family:宋体"}

[[Failed to get entry (*src*, *dst*) driver statistic]{lang="EN-US"}]{#struct_0_15550_84251_200400325}

[[表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1170711251}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）下驱动获取统计信息失败]{style="font-family:宋体"}

[[Failed to write forwarding message to queue]{lang="EN-US"}]{#struct_0_15550_84251_879083536}

[[转发消息入队列失败]{style="font-family:宋体"}]{#struct_0_15550_84251_x76820204}

[[Multicast hasn\'t been enabled]{lang="EN-US"}]{#struct_0_15550_84251_x301835918}

[[组播没有使能]{style="font-family:宋体"}]{#struct_0_15550_84251_1062353132}

[[Entry (*src*, *dst*) does not found]{lang="EN-US"}]{#struct_0_15550_84251_800174531}

[[找不到表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x970029962}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[(*src*, *dst*) is dummy entry]{lang="EN-US"}]{#struct_0_15550_84251_x300852878}

[[表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_706611373}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）是临时表项]{style="font-family:宋体"}

[[Entry (*src*, *dst*) does not exist]{lang="EN-US"}]{#struct_0_15550_84251_x1802659845}

[[表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x1004154529}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）不存在]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ipv6 mfib no-cache]{lang="EN-US"}]{#struct_0_15550_84251_370064640}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_109160872}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_x797113121}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_x300918414}

[[Packet (*src*, *dst*) matched nothing]{lang="EN-US"}]{#struct_0_15550_84251_x1313040736}

[[报文（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x1522488216}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）无匹配的转发表项]{style="font-family:宋体"}

[[dropped for invalid address]{lang="EN-US"}]{#struct_0_15550_84251_x430856412}

[[由于非法源地址而丢弃]{style="font-family:宋体"}]{#struct_0_15550_84251_x1730020896}

[[dropped for rate limit]{lang="EN-US"}]{#struct_0_15550_84251_x1607260488}

[[由于速率限制而丢弃]{style="font-family:宋体"}]{#struct_0_15550_84251_1620937138}

[[dropped for forward queue full]{lang="EN-US"}]{#struct_0_15550_84251_x1644446178}

[[由于转发队列满而丢弃]{style="font-family:宋体"}]{#struct_0_15550_84251_1029588424}

[[dropped for total entry limit]{lang="EN-US"}]{#struct_0_15550_84251_932173843}

[[由于表项总数限制而丢弃]{style="font-family:宋体"}]{#struct_0_15550_84251_x814352798}

[[Matched entry, no need to forward null-reg packet]{lang="EN-US"}]{#struct_0_15550_84251_x949032689}

[[匹配到表项，不需要转发空注册报文]{style="font-family:宋体"}]{#struct_0_15550_84251_1620871602}

[[Matched entry, forward packet]{lang="EN-US"}]{#struct_0_15550_84251_336963442}

[[匹配到表项，转发报文]{style="font-family:宋体"}]{#struct_0_15550_84251_1991777786}

[[Matched dummy entry, no need to save null-reg packet]{lang="EN-US"}]{#struct_0_15550_84251_94751967}

[[匹配临时表项，不需要缓存空注册报文]{style="font-family:宋体"}]{#struct_0_15550_84251_x1178672683}

[[Matched dummy entry, save packet]{lang="EN-US"}]{#struct_0_15550_84251_1620806066}

[[匹配临时表项，缓存报文]{style="font-family:宋体"}]{#struct_0_15550_84251_1876052391}

[[Dummy limit specific is 0, don\'t create dummy entry]{lang="EN-US"}]{#struct_0_15550_84251_796925492}

[[临时表项上限为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_15550_84251_x1707668366}[，不创建临时表项]{style="font-family:宋体"}

[[No-cache packet is filtered, don\'t encap no-cache upcall]{lang="EN-US"}]{#struct_0_15550_84251_x1117477202}

[[未匹配组播报文被过滤掉，不上报]{style="font-family:宋体"}[no-cache]{lang="EN-US"}]{#struct_0_15550_84251_1620740530}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ipv6 mfib packet]{lang="EN-US"}]{#struct_0_15550_84251_326644603}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_111984396}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_x1550186643}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_15783030}

[[Cache packet for dummy entry (*src*, *dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x670590488}

[[缓存临时表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x1299119513}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的数据报文]{style="font-family:宋体"}

[[Free cached packet from dummy entry (*src*, *dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x641320393}

[[释放临时表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1620674994}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）缓存的数据报文]{style="font-family:宋体"}

[[Dummy entry (*src*, *dst*) can\'t cache the packet, dropped it]{lang="EN-US"}]{#struct_0_15550_84251_1533370682}

[[临时表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1421546805}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）不能缓存报文，将其丢弃]{style="font-family:宋体"}

[[Sent PIM *type* packet (*src*, *dst*) to PIM]{lang="EN-US"}]{#struct_0_15550_84251_1282427399}

[[上送]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_15550_84251_160289990}[类型的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文到]{style="font-family:宋体"}[PIM]{lang="EN-US"}[模块，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_15550_84251_1620609458}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Register]{lang="EN-US"}]{#struct_0_15550_84251_1064979725}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RegisterStop]{lang="EN-US"}]{#struct_0_15550_84251_x73391514}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Join-Prune]{lang="EN-US"}]{#struct_0_15550_84251_2081463276}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BootStrap]{lang="EN-US"}]{#struct_0_15550_84251_433125081}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Assert]{lang="EN-US"}]{#struct_0_15550_84251_x618332069}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Graft]{lang="EN-US"}]{#struct_0_15550_84251_1620543922}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GraftAck]{lang="EN-US"}]{#struct_0_15550_84251_x841182961}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CRP-Advertise]{lang="EN-US"}]{#struct_0_15550_84251_x549247089}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StateRefresh]{lang="EN-US"}]{#struct_0_15550_84251_x171259492}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_15550_84251_916056161}

[[Hoplimit(*hoplimit*) of packet (*src*, *dst*) is less than hoplimit threshold(*hoplimit*) on *interface-name*, dropped it]{lang="EN-US"}]{#struct_0_15550_84251_1620478386}

[[报文（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1067374651}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的]{style="font-family:宋体"}[Hoplimit]{lang="EN-US"}[值小于接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上的]{style="font-family:宋体"}[Hoplimit]{lang="EN-US"}[阀值，将其丢弃]{style="font-family:宋体"}

[[Forwarded packet (*src*, *dst*) to interface *interface-name*]{lang="EN-US"}]{#struct_0_15550_84251_1358571096}

[[向接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_15550_84251_x1487753252}[转发报文（]{style="font-family:宋体"}*[src]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Dropped packet (*src*, *dst*) for hoplimit is 1]{lang="EN-US"}]{#struct_0_15550_84251_x598875715}

[[报文（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1621461426}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的]{style="font-family:宋体"}[Hoplimit]{lang="EN-US"}[值为]{style="font-family:宋体"}[1]{lang="EN-US"}[，将其丢弃]{style="font-family:宋体"}

[[Received packet (*src*, *dst*) from interface *interface-name*, hoplimit is *hoplimit*]{lang="EN-US"}]{#struct_0_15550_84251_1505339384}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_15550_84251_1405369719}[收到]{style="font-family:宋体"}[Hoplimit]{lang="EN-US"}[值为]{style="font-family:宋体"}*[hoplimit]{lang="EN-US"}*[的报文（]{style="font-family:宋体"}*[src]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received a PIM *type* packet, then directly send to PIM module]{lang="EN-US"}]{#struct_0_15550_84251_x1909113471}

[[收到]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_15550_84251_1350075105}[类型的报文直接上送]{style="font-family:宋体"}[PIM]{lang="EN-US"}[模块，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_15550_84251_1621395890}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Register]{lang="EN-US"}]{#struct_0_15550_84251_x1615276504}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RegisterStop]{lang="EN-US"}]{#struct_0_15550_84251_575563844}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Join-Prune]{lang="EN-US"}]{#struct_0_15550_84251_1986705838}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BootStrap]{lang="EN-US"}]{#struct_0_15550_84251_1620937139}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Assert]{lang="EN-US"}]{#struct_0_15550_84251_x1644380642}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Graft]{lang="EN-US"}]{#struct_0_15550_84251_x2103008851}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GraftAck]{lang="EN-US"}]{#struct_0_15550_84251_x727639184}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CRP-Advertise]{lang="EN-US"}]{#struct_0_15550_84251_1620871603}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StateRefresh]{lang="EN-US"}]{#struct_0_15550_84251_337028978}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknow]{lang="EN-US"}]{#struct_0_15550_84251_1940067032}

[[Received a PIM packet with invalid type *type*]{lang="EN-US"}]{#struct_0_15550_84251_x1588134704}

[[收到非法类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_15550_84251_1620806067}[的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Dropped the packet (*src*, *dst*)]{lang="EN-US"}]{#struct_0_15550_84251_1875986855}

[[丢弃报文（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x591859833}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[for hoplimit is 0]{lang="EN-US"}]{#struct_0_15550_84251_x1010627272}

[[Hoplimit]{lang="EN-US"}]{#struct_0_15550_84251_1620740531}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[for entry hasn\'t any OIF]{lang="EN-US"}]{#struct_0_15550_84251_326579067}

[[表项没有出接口]{style="font-family:宋体"}]{#struct_0_15550_84251_913132400}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging ipv6 mfib register]{lang="EN-US"}]{#struct_0_15550_84251_x1273995046}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_108965190}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_x1837057960}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_1620674995}

[[No RP for (*src, dst*) to send register]{lang="EN-US"}]{#struct_0_15550_84251_1533436218}

[[（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x513922207}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）没有]{style="font-family:宋体"}[RP]{lang="EN-US"}[用于发送注册报文]{style="font-family:宋体"}

[[No local address for (*src, dst*) to send register]{lang="EN-US"}]{#struct_0_15550_84251_x225318453}

[[（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1467852244}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）没有本地地址用于发送注册报文]{style="font-family:宋体"}

[[Sent register for (*src, dst*) to RP *rp*]{lang="EN-US"}]{#struct_0_15550_84251_696269822}

[[发送（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1620609459}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的注册报文到]{style="font-family:宋体"}[RP *rp*]{lang="EN-US"}

[[Sent proxy register for (*src, dst*) to RP *rp*]{lang="EN-US"}]{#struct_0_15550_84251_1064914189}

[[发送（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x490068711}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的代理注册报文到]{style="font-family:宋体"}[RP *rp*]{lang="EN-US"}

[[Sent register-stop packet for (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x428048280}

[[发送（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_270705988}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的注册停止报文]{style="font-family:宋体"}

[[Dropped register packet for length is 0 or larger than max length *maxlength*]{lang="EN-US"}]{#struct_0_15550_84251_709439715}

[[丢弃报文长度为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_15550_84251_1620543923}[或大于最大长度]{style="font-family:宋体"}*[maxlength]{lang="EN-US"}*[的注册报文]{style="font-family:宋体"}

[[Dropped register packet for invalid source address *src*]{lang="EN-US"}]{#struct_0_15550_84251_x841248497}

[[丢弃非法源地址为]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x246106757}[的注册报文]{style="font-family:宋体"}

[[Dropped register packet from *src*, for length is wrong: data length is *dlen*(should be larger than *ldlen*), total length is *tlen*(should be *ltlen*)]{lang="EN-US"}]{#struct_0_15550_84251_x451914458}

[[丢弃从]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1894523007}[收到的长度错误的注册报文，数据长度是]{style="font-family:宋体"}*[dlen]{lang="EN-US"}*[（应该大于]{style="font-family:宋体"}*[ldlen]{lang="EN-US"}*[），总长度是]{style="font-family:宋体"}*[tlen]{lang="EN-US"}*[（应该是]{style="font-family:宋体"}*[ltlen]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Dropped register packet from *src* for checksum error]{lang="EN-US"}]{#struct_0_15550_84251_1620478387}

[[丢弃从]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1067440187}[收到的校验和错误的注册报文]{style="font-family:宋体"}

[[Received register packet from *src* to *dst*, with data packet: (*src1, dst2*)]{lang="EN-US"}]{#struct_0_15550_84251_2142131024}

[[收到从]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1675013005}[到]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[的注册报文，其中包含（]{style="font-family:宋体"}*[src1]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst2]{lang="EN-US"}*[）数据]{style="font-family:宋体"}

[[Multicast hasn\'t been enabled, dropped the register packet]{lang="EN-US"}]{#struct_0_15550_84251_x765417055}

[[组播未使能，丢弃收到的注册报文]{style="font-family:宋体"}]{#struct_0_15550_84251_1621461427}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ipv6 mfib route]{lang="EN-US"}]{#struct_0_15550_84251_1505273848}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_101437564}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_321695636}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_998302904}

[[Add/Remove OIF *interface-name* to (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_1431397569}

[[表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x1744062613}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除出接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*

[[Add/Delete entry (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x1019918147}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_1621395891}[删除表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Add/Delete dummy entry (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x1615210968}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_x102280062}[删除临时表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Set IIF *interface-name* to entry (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x504893254}

[[设置表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_656768327}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的入接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*

[[Change dummy entry (*src, dst*) to normal]{lang="EN-US"}]{#struct_0_15550_84251_x1106406674}

[[临时表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x1831152378}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）转换为正式表项]{style="font-family:宋体"}

[[The dummy entry (*src, dst*)  is replaced for route limit(*limit*)]{lang="EN-US"}]{#struct_0_15550_84251_1620937136}

[[由于达到表项规格（]{style="font-family:宋体"}*[limit]{lang="EN-US"}*]{#struct_0_15550_84251_x1643528674}[），临时表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）被正式表项替换]{style="font-family:宋体"}

[[Set/Reset flag *flag* for entry (%s, %s)]{lang="EN-US"}]{#struct_0_15550_84251_675219428}

[[设置]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_x2107624250}[清除表项标记]{style="font-family:宋体"}*[flag]{lang="EN-US"}*

[[Set RP (*rp*) for group *group*]{lang="EN-US"}]{#struct_0_15550_84251_580360029}

[[设置组]{style="font-family:宋体"}*[group]{lang="EN-US"}*]{#struct_0_15550_84251_1620871600}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[为]{style="font-family:宋体"}*[rp]{lang="EN-US"}*

[[Flush entry (*src, dst*) to driver]{lang="EN-US"}]{#struct_0_15550_84251_336832370}

[[下发表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_437364922}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）到驱动]{style="font-family:宋体"}

[[Get entry (*src, dst*) driver statistic, matched: *matched*, wrongif: *wrongif*]{lang="EN-US"}]{#struct_0_15550_84251_1443825497}

[[从驱动获取表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_819651844}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的统计信息：匹配数为]{style="font-family:宋体"}*[matched]{lang="EN-US"}*[，错误入接口数为]{style="font-family:宋体"}*[wrongif]{lang="EN-US"}*

[[Reached dummy limit, don\'t create dummy entry]{lang="EN-US"}]{#struct_0_15550_84251_1620806064}

[[达到临时表项数目上限，不再创建临时表项]{style="font-family:宋体"}]{#struct_0_15550_84251_1875921319}

[[Re-add entry (*src, dst*) to driver]{lang="EN-US"}]{#struct_0_15550_84251_1332461382}

[[重新下刷表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_387751940}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）到驱动]{style="font-family:宋体"}

[[Re-add *num* OIF(s) of entry (*src, dst*) to driver]{lang="EN-US"}]{#struct_0_15550_84251_x1850141833}

[[重新下刷表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1620740528}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）添加]{style="font-family:宋体"}*[num]{lang="EN-US"}*[个出接口到驱动]{style="font-family:宋体"}

[[Aged dummy entry (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_326120316}

[[临时表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_798730455}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）老化]{style="font-family:宋体"}

[[Reached entry limit(*limit*), don\'t add entry (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x1187762180}

[[达到表项上限]{style="font-family:宋体"}[,]{lang="EN-US"}]{#struct_0_15550_84251_1620674992}[不再添加表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received add-entry/delete-entry message of (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_1533763898}

[[收到添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_x2050258597}[删除表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）消息]{style="font-family:宋体"}

[[OIF num is *num*]{lang="EN-US"}]{#struct_0_15550_84251_368825735}

[[出接口数目为]{style="font-family:宋体"}*[num]{lang="EN-US"}*]{#struct_0_15550_84251_247712891}

[[Received set-IIF message of (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_1620609456}

[[收到设置表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1064324365}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）入接口消息]{style="font-family:宋体"}

[[Received add-OIF/delete-OIF message of (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x874043815}

[[收到添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_2135193141}[删除表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）出接口消息]{style="font-family:宋体"}

[[Received set-RP *rp* for group *group* message]{lang="EN-US"}]{#struct_0_15550_84251_1620543920}

[[收到设置组]{style="font-family:宋体"}*[group]{lang="EN-US"}*]{#struct_0_15550_84251_x841314033}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[为]{style="font-family:宋体"}*[rp]{lang="EN-US"}*[消息]{style="font-family:宋体"}

[[Received set-active/set-inactive message of (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_2145271428}

[[收到表项（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1620478384}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）激活]{style="font-family:宋体"}[/]{lang="EN-US"}[非激活消息]{style="font-family:宋体"}

[[Received set-multicast-enable/set-multicast-disable message on interface *interface-name*]{lang="EN-US"}]{#struct_0_15550_84251_1067243579}

[[收到接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_15550_84251_975090144}[上使能]{style="font-family:宋体"}[/]{lang="EN-US"}[去使能消息]{style="font-family:宋体"}

[[Received multicast enable/disable message]{lang="EN-US"}]{#struct_0_15550_84251_354144106}

[[收到组播使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_1621461424}[去使能消息]{style="font-family:宋体"}

[ ]{lang="PT-BR"}

[[表1-6 ]{lang="EN-US"}[debugging ipv6 mfib upcall]{lang="EN-US"}]{#struct_0_15550_84251_1505470456}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_134008816}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_1050288994}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_1342360098}

[[Succeeded in sending *type* upcall (*src, dst*)]{lang="EN-US"}]{#struct_0_15550_84251_x1191033870}

[[成功发送（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_1944434034}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的]{style="font-family:宋体"}[upcall]{lang="EN-US"}[消息，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no-cache]{lang="EN-US"}]{#struct_0_15550_84251_1621395888}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[wrong-IIF]{lang="EN-US"}]{#struct_0_15550_84251_x1615800791}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPT-switchover]{lang="EN-US"}]{#struct_0_15550_84251_x909552130}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[source-active]{lang="EN-US"}]{#struct_0_15550_84251_x1580333044}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[source-inactive]{lang="EN-US"}]{#struct_0_15550_84251_x1671364583}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reset]{lang="EN-US"}]{#struct_0_15550_84251_x2052672463}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging ipv6 mfib wrong-iif]{lang="EN-US"}]{#struct_0_15550_84251_x696203820}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_132870572}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_1620937137}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_x1643463138}

[[Packet (*src, dst*) should came from *interface-name*]{lang="EN-US"}]{#struct_0_15550_84251_1841453359}

[[报文的（]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_15550_84251_x222572878}[，]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[）正确入接口应该是]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*

[[dropped for rate limit]{lang="EN-US"}]{#struct_0_15550_84251_x1076172174}

[[由于速率限制而丢弃]{style="font-family:宋体"}]{#struct_0_15550_84251_x385473396}

[[dropped for forward queue full]{lang="EN-US"}]{#struct_0_15550_84251_x1711026090}

[[由于转发队列满而丢弃]{style="font-family:宋体"}]{#struct_0_15550_84251_1620871601}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15550_84251_336897906}

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_2028149228}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，打开]{style="font-family:宋体"}[公网实例]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[错误]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mfib error]{lang="EN-US"}]{#struct_0_15550_84251_x1026670481}

[\*Apr 26 12:53:18:979 2011 Sysname MFIB6/7/DRIVER: -MDC=1;]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[IPv6: Failed to create entry (1::1, ff0e::1). (A062520)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_721244709}*[创建转发表项（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_x694329523}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，打开公网实例]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[未匹配报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mfib no-cache]{lang="EN-US"}]{#struct_0_15550_84251_x852554642}

[\*Apr 26 12:43:19:09 2011 Sysname MFIB6/7/NOCACHE: -MDC=1; IPv6: Packet (1::1, ff0e::1) matched nothing. (A08303)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_x1753014270}*[收到无匹配转发表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Apr 26 12:43:19:15 2011 Sysname MFIB6/7/NOCACHE: -MDC=1; IPv6: Succeeded in sending no-cache upcall (1::1, ff0e::1). (A08453)]{lang="EN-US"}]{#struct_0_15550_84251_1620806065}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_1875855783}*[成功发送没有转发表项（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）的]{style="font-family:宋体"}[upcall]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_129536472}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，打开公网实例]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mfib packet]{lang="EN-US"}]{#struct_0_15550_84251_1321085758}

[\*Apr 26 12:28:50:578 2011 Sysname MFIB6/7/PACKET: -MDC=1; IPv6: Received packet (1::1, ff0e::1) from interface Vlan-interface20, hoplimit is 128. (A012942)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_1564202514}*[从接口]{style="font-family:宋体"}[Vlan-interface20]{lang="EN-US"}[收到]{style="font-family:宋体"}[Hoplimit]{lang="EN-US"}[值为]{style="font-family:宋体"}[128]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Apr 26 12:28:50:625 2011 Sysname MFIB6/7/PACKET: -MDC=1; IPv6: Forwarded packet (1::1, ff0e::1) to interface GigabitEthernet1/0/1. (A083551)]{lang="EN-US"}]{#struct_0_15550_84251_x1381221052}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_695655457}*[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）通过端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[转发出去]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_2052928596}[分别在两台设备的接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[RP]{lang="EN-US"}[和]{style="font-family:宋体"}[BSR]{lang="EN-US"}[，打开公网实例]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[注册报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ]{lang="NO-BOK"}[ipv6 ]{lang="EN-US"}]{#struct_0_15550_84251_1620740529}[mfib register]{lang="NO-BOK"}

[\*Apr 26 13:29:33:753 2011 Sysname MFIB6/7/REGISTER: -MDC=1;]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[IPv6: Received register packet from 2::1 to 1::1, with data packet: (2::10, ff0e::1). (A086218)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_326054780}*[收到由]{style="font-family:宋体"}[2::1]{lang="EN-US"}[发往]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的、封装有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文（]{style="font-family:宋体"}[2::10]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）的注册报文]{style="font-family:宋体"}*

[[\*Apr 26 13:29:33:763 2011 Sysname MFIB6/7/REGISTER: -MDC=1;]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[IPv6: Sent register-stop packet for (2::10, ff0e::1). (A085970)]{lang="EN-US"}]{#struct_0_15550_84251_x1153991700}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_701987340}*[向]{style="font-family:宋体"}[2::1]{lang="EN-US"}[发送（]{style="font-family:宋体"}[2::10]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）的注册停止报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_x1726378282}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，打开公网实例]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[路由调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mfib route]{lang="EN-US"}]{#struct_0_15550_84251_716994573}

[\*Apr 26 12:39:59:272 2011 Sysname MFIB6/6/ROUTE: -MDC=1; IPv6: Add dummy entry (1::1, ff0e::1). (A07120)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_x1390050759}*[收到无匹配转发表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[），为其创建临时转发表项]{style="font-family:宋体"}*

[[\*Apr 26 12:39:59:297 2011 Sysname MFIB6/6/ROUTE: -MDC=1; IPv6: Received add-entry message of (1::1, ff0e::1), OIF num is 1.(A112030)]{lang="EN-US"}]{#struct_0_15550_84251_1620674993}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_1533829434}*[收到]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[通知添加（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）表项的消息，表项的出接口数目为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Apr 26 12:39:59:327 2011 Sysname MFIB6/6/ROUTE: -MDC=1; IPv6: Change dummy entry (1::1, ff0e::1) to normal. (A07391)]{lang="EN-US"}]{#struct_0_15550_84251_x570669998}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_1447881046}*[删除临时转发表项（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[），并添加相应的正式转发表项]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_x1398294675}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，打开]{style="font-family:宋体"}[公网实例]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[上报]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[相关]{style="font-family:宋体"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mfib upcall]{lang="EN-US"}]{#struct_0_15550_84251_x279982596}

[\*Sep  7 21:10:08:130 2011 Sysname MFIB6/7/UPCALL: -MDC=1; IPv6: Succeeded in sending no-cache upcall (1::1, ff0e::1). (A08453)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_x3216349}*[向]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[上报未匹配报文（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）的消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_1939230769}[在接口]{style="font-family:宋体"}[VLAN-interface40]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN-interface60]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[PIM-DM]{lang="EN-US"}[，发送相同源组的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文，打开]{style="font-family:宋体"}[公网实例]{style="font-family:宋体"}[IPv6 MFIB]{lang="EN-US"}[错误入接口调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mfib wrong-iif]{lang="EN-US"}]{#struct_0_15550_84251_1620609457}

[\*Jan 24 04:36:52:990 2011 Sysname MFIB6/7/WRONGIIF: -MDC=1; IPv6: -Slot=3; Packet (1::1, ff0e::1) should came from Vlan-interface40. (A08734)]{lang="EN-US"}

[*[// IPv6]{lang="EN-US"}*]{#struct_0_15550_84251_1064258829}*[组播数据报文]{style="font-family:宋体"}[（]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::1]{lang="EN-US"}[）正确的入接口应为]{style="font-family:宋体"}[Vlan-interface40]{lang="EN-US"}*

::: {#1179111898 .myid}
[]{#_Toc404790116}[]{#struct_0_15550_84251_1541386036}[]{#_Toc306715540}[]{#_Toc300304085}[]{#_Toc280695264}

**IPv6组播路由与转发 \-- IPv6组播路由与转发调试命令 \-- debugging ipv6 mrib**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15550_84251_x38762413}

[**[debugging ipv6]{lang="EN-US"}**[ **mrib** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **error** \| **event** \| **interface** \[ *interface-type* *interface-number* \] \| **proxy** \[ **event** \| **routing-table** \] \| **route** \[ *advanced-acl6-number* \] }]{lang="EN-US"}]{#struct_0_15550_84251_x1071900779}

[**[undo debugging ipv6]{lang="EN-US"}**[ **mrib** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **error** \| **event** \| **interface** \| **proxy** \[ **event** \| **routing-table** \] \| **route** }]{lang="EN-US"}]{#struct_0_15550_84251_1957571609}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15550_84251_x1809797165}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15550_84251_1483694387}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15550_84251_x1934145116}

[[network-admin]{lang="EN-US"}]{#struct_0_15550_84251_1479187351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15550_84251_1620543921}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15550_84251_x841379569}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_15550_84251_146156134}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_15550_84251_x120141888}[：表示]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Multicast Routing Information Base]{lang="EN-US"}[，组播路由信息库）的所有调试信息开关。]{style="font-family:
宋体"}

[**[error]{lang="SV"}**]{#struct_0_15550_84251_153843048}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="SV"}**]{#struct_0_15550_84251_616699038}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6 MRIB]{lang="SV"}[事件调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="SV"}**]{#struct_0_15550_84251_1899509478}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6 MRIB]{lang="SV"}[接口管理调试信息开关。]{style="font-family:宋体"}

[*[interface-type]{lang="SV"}*]{#struct_0_15550_84251_2144353938}[ *interface-number*]{lang="SV"}[：]{style="font-family:宋体"}[表示指定接口的]{style="font-family:宋体"}[IPv6 MRIB]{lang="SV"}[接口管理调试信息开关。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示所有接口的]{style="font-family:宋体"}[IPv6 MRIB]{lang="SV"}[接口管理调试信息开关。]{style="font-family:宋体"}

[**[proxy]{lang="SV"}**]{#struct_0_15550_84251_x866763358}[ \[ **event** \| **routing-table** \]]{lang="SV"}[：表示]{style="font-family:
宋体"}[MLD]{lang="SV"}[代理调试信息开关，包括事件（]{style="font-family:宋体"}**[event]{lang="SV"}**[）和路由表（]{style="font-family:宋体"}**[routing-table]{lang="SV"}**[）两种。如果未指定]{style="font-family:宋体"}**[event]{lang="SV"}**[和]{style="font-family:宋体"}**[routing-table]{lang="SV"}**[参数，表示同时包括这两种调试信息开关。]{style="font-family:宋体"}

[**[route]{lang="SV"}**]{#struct_0_15550_84251_1620478385}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6 MRIB]{lang="SV"}[路由表项调试信息开关。]{style="font-family:宋体"}

[*[advanced-acl6-number]{lang="SV"}*]{#struct_0_15550_84251_1067309115}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6]{lang="SV"}[高级]{style="font-family:宋体"}[ACL]{lang="SV"}[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[3000]{lang="SV"}[～]{style="font-family:宋体"}[3999]{lang="SV"}[。]{style="font-family:
宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15550_84251_229122995}

[**[debugging ipv6 mrib]{lang="SV"}**]{#struct_0_15550_84251_1297035892}[命令用来打开]{style="font-family:宋体"}[IPv6 MRIB]{lang="SV"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 mfib]{lang="SV"}**[命令用来关闭]{style="font-family:宋体"}[IPv6 MRIB]{lang="SV"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}]{#struct_0_15550_84251_1590867573}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging ipv6 mrib error]{lang="EN-US"}]{#struct_0_15550_84251_x1456419770}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_127648058}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_1100111768}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_x1136551832}

[[multicast routing]{lang="EN-US"}]{#struct_0_15550_84251_1621461425}

[[组播路由]{style="font-family:宋体"}]{#struct_0_15550_84251_1505404920}

[[MBoundary]{lang="EN-US"}]{#struct_0_15550_84251_x1263536685}

[[组播边界]{style="font-family:宋体"}]{#struct_0_15550_84251_x728187381}

[[MFIB]{lang="EN-US"}]{#struct_0_15550_84251_x819557327}

[[组播转发信息库]{style="font-family:宋体"}]{#struct_0_15550_84251_x84850921}

[[iif]{lang="EN-US"}]{#struct_0_15550_84251_1621395889}

[[入接口]{style="font-family:宋体"}]{#struct_0_15550_84251_x1615735255}

[[oif]{lang="EN-US"}]{#struct_0_15550_84251_1029155700}

[[出接口]{style="font-family:宋体"}]{#struct_0_15550_84251_x970730000}

[[spt thres]{lang="EN-US"}]{#struct_0_15550_84251_203555490}

[[SPT]{lang="EN-US"}]{#struct_0_15550_84251_x112511407}[切换阈值]{style="font-family:宋体"}

[[reg suppress]{lang="EN-US"}]{#struct_0_15550_84251_1620937134}

[[注册抑制]{style="font-family:宋体"}]{#struct_0_15550_84251_x1643659746}

[[flush mrt table]{lang="EN-US"}]{#struct_0_15550_84251_x1222033084}

[[下刷路由表]{style="font-family:宋体"}]{#struct_0_15550_84251_x806175292}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging ipv6 mrib event]{lang="EN-US"}]{#struct_0_15550_84251_1890531295}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_129994168}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_699327352}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_1620871598}

[[Multicast Boundary]{lang="EN-US"}]{#struct_0_15550_84251_x1237670021}

[[组播边界]{style="font-family:宋体"}]{#struct_0_15550_84251_662192332}

[[Multicast routing]{lang="EN-US"}]{#struct_0_15550_84251_1464562896}

[[组播路由]{style="font-family:宋体"}]{#struct_0_15550_84251_x1504166808}

[[MFIB]{lang="EN-US"}]{#struct_0_15550_84251_246692248}

[[组播转发信息库]{style="font-family:宋体"}]{#struct_0_15550_84251_1620806062}

[[spt thres]{lang="EN-US"}]{#struct_0_15550_84251_1876314535}

[[SPT]{lang="EN-US"}]{#struct_0_15550_84251_x1944516711}[切换阈值]{style="font-family:宋体"}

[[reg suppress]{lang="EN-US"}]{#struct_0_15550_84251_1432978053}

[[注册抑制]{style="font-family:宋体"}]{#struct_0_15550_84251_816953553}

[[Add msg to ipc buffer]{lang="EN-US"}]{#struct_0_15550_84251_x1761561576}

[[向]{style="font-family:宋体"}[IPC]{lang="EN-US"}]{#struct_0_15550_84251_1620740526}[缓冲区中添加一个消息]{style="font-family:宋体"}

[[Send msg to MFIB success]{lang="EN-US"}]{#struct_0_15550_84251_327037820}

[[成功向]{style="font-family:宋体"}[MFIB]{lang="EN-US"}]{#struct_0_15550_84251_x975075508}[发送一个消息]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_15550_84251_x461217940}

[[消息类型]{style="font-family:宋体"}]{#struct_0_15550_84251_1453347035}

[[Len]{lang="EN-US"}]{#struct_0_15550_84251_1620674990}

[[消息长度]{style="font-family:宋体"}]{#struct_0_15550_84251_1533632826}

[[Count]{lang="EN-US"}]{#struct_0_15550_84251_663748108}

[[消息数量]{style="font-family:宋体"}]{#struct_0_15550_84251_x1114013170}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging ipv6 mrib interface]{lang="EN-US"}]{#struct_0_15550_84251_x1635138062}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_122189178}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_116596753}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_1620609454}

[[Succeed in adding interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1064193293}

[[成功添加接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x1661619849}

[[Remove interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1464685581}

[[删除接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x1598121319}

[[Create interface address for (*interface*, *address*), reference *cnt*]{lang="EN-US"}]{#struct_0_15550_84251_1620543918}

[[创建接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x841838324}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*

[[Remove interface address *address* of *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x1428441428}

[[删除接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x809549461}[的地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[Create interface address for (*interface*, *address*) while exist, reference *cnt*]{lang="EN-US"}]{#struct_0_15550_84251_154274488}

[[创建接口地址时，地址已经存在，增加它的引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_15550_84251_x892047088}

[[Create interface address for (*interface*, *address*) when sending message, reference *cnt*]{lang="EN-US"}]{#struct_0_15550_84251_1620478382}

[[发送接口变化消息时，创建接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_15550_84251_1067636795}

[[Create interface address for (*interface*, *address*) when getting by index, reference *cnt*]{lang="EN-US"}]{#struct_0_15550_84251_191631155}

[[根据接口索引获取接口上的接口地址时，创建接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_15550_84251_x2072014678}

[[Create interface address for (*interface*, *address*) when getting by address, reference *cnt*]{lang="EN-US"}]{#struct_0_15550_84251_x1731336679}

[[根据全局]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_15550_84251_1621461422}[地址获取接口上的接口地址时，创建接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*

[[Destroy interface address for (*interface*, *address*) when deleting it, reference *cnt*]{lang="EN-US"}]{#struct_0_15550_84251_1505077240}

[[销毁接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_15550_84251_264536510}

[[Create interface address for (*interface*, *address*) at (*file*, *line*), reference *cnt* ]{lang="EN-US"}]{#struct_0_15550_84251_x2144282400}

[[在文件]{style="font-family:宋体"}*[file]{lang="EN-US"}*]{#struct_0_15550_84251_x596449526}[的]{style="font-family:宋体"}*[line]{lang="EN-US"}*[引用行创建接口地址，引用计数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*

[[Failed to create interface]{lang="EN-US"}]{#struct_0_15550_84251_1621395886}

[[创建接口失败]{style="font-family:宋体"}]{#struct_0_15550_84251_x1615669719}

[[Succeed in adding PIM interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x203037480}

[[成功添加]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_15550_84251_727273031}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Remove PIM interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1620937135}

[[删除]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_15550_84251_x1643594210}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Enable/Disable protocol packet deliver up on interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1219606841}

[[使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_1198321173}[关闭接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[协议功能]{style="font-family:宋体"}

[[Succeed in enabling/disabling PIM packet to CPU for interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x176298956}

[[使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_1620871599}[关闭接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[协议功能成功]{style="font-family:宋体"}

[[PIM interface *interface* is up/down]{lang="EN-US"}]{#struct_0_15550_84251_x1237604485}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_15550_84251_x2058459551}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[生效]{style="font-family:宋体"}[/]{lang="EN-US"}[失效]{style="font-family:宋体"}

[[No address or memory for PIM interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x672797255}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_1620806063}[没有配置地址或内存不足]{style="font-family:宋体"}

[[Message to add(*type*) interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1876248999}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_1656262760}[添加消息，消息子类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[Message to up interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1620740527}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_326972284}[生效消息]{style="font-family:宋体"}

[[Message to down(*type*) interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x951372633}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x281999115}[失效消息，消息子类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[Message to change configuration of interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1620674991}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_1533698362}[配置变化消息]{style="font-family:宋体"}

[[Ignore non-primary or borrow address of *interface*, state *state*]{lang="EN-US"}]{#struct_0_15550_84251_x1353467478}

[[忽略从地址和借用地址逻辑接口变化消息]{style="font-family:宋体"}]{#struct_0_15550_84251_x2036613372}

[[Message to add/delete address *address*/*masklen* (*interface*)]{lang="EN-US"}]{#struct_0_15550_84251_1620609455}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_1064127757}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*[/*masklen*]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Message to up/down vlink interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x512523281}

[[Vlink]{lang="EN-US"}]{#struct_0_15550_84251_1620543919}[接口]{style="font-family:宋体"}*[interface ]{lang="EN-US"}*[up/down]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Vlink state of interface *interface* is not up, state *state* ]{lang="EN-US"}]{#struct_0_15550_84251_x841903860}

[[Vlink]{lang="EN-US"}]{#struct_0_15550_84251_206085394}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[状态不是]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[[Succeed in creating basic interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1620478383}

[[创建基本接口（注册口、]{style="font-family:宋体"}[Null0]{lang="EN-US"}]{#struct_0_15550_84251_1067702331}[接口等）]{style="font-family:宋体"}

[[Succeed in destroying basic interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x1363329884}

[[删除基本接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_1621461423}

[[Try to enable/disable protocol *pro* on interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1505011704}

[[尝试在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_1809488004}[上使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭协议]{style="font-family:宋体"}*[pro]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging ipv6 mrib proxy]{lang="EN-US"}]{#struct_0_15550_84251_x866304607}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1157602343}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_x915934385}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_x866370143}

[[Process gmp querier enable/disable for interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x2054545177}

[[为接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x866435679}[使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭查询器]{style="font-family:宋体"}

[[Notify proxy up/down message on interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1815504976}

[[通报代理接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x866501215}[生效]{style="font-family:宋体"}[/]{lang="EN-US"}[失效消息]{style="font-family:宋体"}

[[Add proxy interface for interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x1277192767}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x866042463}[上添加代理功能]{style="font-family:宋体"}

[[Process proxy enable/disable message on interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1827080596}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x1830865961}[上处理代理功能使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭消息]{style="font-family:宋体"}

[[Delete proxy interface on interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x866107999}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x1656532745}[上删除代理接口]{style="font-family:宋体"}

[[Proxy interface logup/logdown for interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x866566752}

[[代理接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x1720263476}[逻辑]{style="font-family:宋体"}[up/]{lang="EN-US"}[逻辑]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Notify proxy enable/disable message]{lang="EN-US"}]{#struct_0_15550_84251_x866632288}

[[通报代理功能使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_1454049988}[关闭消息]{style="font-family:宋体"}

[[Proxy routing-table adjust timer expired]{lang="EN-US"}]{#struct_0_15550_84251_x866697824}

[[代理路由表重整定时器超时]{style="font-family:宋体"}]{#struct_0_15550_84251_x866763360}

[[Create/Delete proxy routing-table relate interface: *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x2081784010}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x866304608}[上创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除代理路由表]{style="font-family:宋体"}

[[Create/Delete proxy routing-table adjust timer(*time*)]{lang="EN-US"}]{#struct_0_15550_84251_x915475633}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_x866370144}[删除代理路由表重整定时器（时间值为]{style="font-family:宋体"}*[time]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Could not find (\*,*group*), ignore the prune message]{lang="EN-US"}]{#struct_0_15550_84251_x2054741785}

[[没有找到（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_15550_84251_x866435680}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）表项，忽略剪枝报文]{style="font-family:宋体"}

[[Receive gmp aux/ex join/prune for (*source*, *group*) on *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1814915155}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x866501216}[上收到（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）表项的加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文]{style="font-family:宋体"}

[[Relate group *group* to proxy interface: *interface*]{lang="EN-US"}]{#struct_0_15550_84251_x1277258303}

[[将组]{style="font-family:宋体"}*[group]{lang="EN-US"}*]{#struct_0_15550_84251_x866042464}[与代理接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[相关联]{style="font-family:宋体"}

[[Relate group *group* to niif list]{lang="EN-US"}]{#struct_0_15550_84251_1827015060}

[[将组]{style="font-family:宋体"}*[group]{lang="EN-US"}*]{#struct_0_15550_84251_x866108000}[与空接口列表相关联]{style="font-family:宋体"}

[[Create/Delete proxy routing-table (*source*, *group*)]{lang="EN-US"}]{#struct_0_15550_84251_x449872919}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15550_84251_x866566753}[删除代理路由表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Failed to create entry (*source*, *group*) for reaching route limit]{lang="EN-US"}]{#struct_0_15550_84251_x1720329012}

[[由于超出规格，创建表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_15550_84251_x866632289}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）创建失败]{style="font-family:宋体"}

[[Add/Delete/Set iif: *interface* for (*source*, *group*)]{lang="EN-US"}]{#struct_0_15550_84251_1454115524}

[[为表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_15550_84251_x866697825}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更改入接口，并与该表项关联]{style="font-family:宋体"}[/]{lang="EN-US"}[解绑]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联]{style="font-family:宋体"}

[[Cannot add downstream *interface* for (*source*, *group*), since it is not in the immediate olist]{lang="EN-US"}]{#struct_0_15550_84251_322785729}

[[由于表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_15550_84251_x866763361}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）不在直接出接口列表中，因此不能为该表项添加下游接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Cannot delete downstream *interface* for (*source*, *group*), since it is in the immediate olist]{lang="EN-US"}]{#struct_0_15550_84251_x866304609}

[[由于表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_15550_84251_x915541169}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）在直接出接口列表中，因此不能为该表项删除下游接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Add/Delete oif: *interface* for (*source*, *group*)]{lang="EN-US"}]{#struct_0_15550_84251_x866370145}

[[为表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_15550_84251_x2054676249}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除出接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Notify MRIB to add/delete oif *interface* before adding entry (*source*, *group*)]{lang="EN-US"}]{#struct_0_15550_84251_x866435681}

[[在添加表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_15550_84251_1814980691}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）之前，就通知]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除出接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Process multicast boundary message on proxy interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1329349022}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x195932808}[上处理组播边界消息]{style="font-family:宋体"}

[[Create multicast boundary timer on proxy interface *interface*]{lang="EN-US"}]{#struct_0_15550_84251_1329283486}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_x179727893}[上创建组播边界定时器]{style="font-family:宋体"}

[[Multicast boundary timer on interface *interface* expired]{lang="EN-US"}]{#struct_0_15550_84251_1329217950}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_15550_84251_1755561866}[上的组播边界定时器超时]{style="font-family:宋体"}

[[Process MFIB/MRIB reset entry message]{lang="EN-US"}]{#struct_0_15550_84251_1329676702}

[[处理]{style="font-family:宋体"}[MFIB/MRIB]{lang="EN-US"}]{#struct_0_15550_84251_1414417000}[表项删除消息]{style="font-family:宋体"}

[[Create flush entry timer]{lang="EN-US"}]{#struct_0_15550_84251_1329611166}

[[创建表项下刷定时器]{style="font-family:宋体"}]{#struct_0_15550_84251_1388619827}

[[Proxy flush entry timer expired]{lang="EN-US"}]{#struct_0_15550_84251_1329152413}

[[表项下刷定时器超时]{style="font-family:宋体"}]{#struct_0_15550_84251_1405361400}

[[Delete all expand oif from sg entry when delete (\*, *group*)]{lang="EN-US"}]{#struct_0_15550_84251_1329086877}

[[在删除（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_15550_84251_1354844847}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）表项时，同时删除对应（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项中的扩展出接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging ipv6 mrib route]{lang="EN-US"}]{#struct_0_15550_84251_x1785739202}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_120206412}[[字段]{style="font-family:黑体"}]{#struct_0_15550_84251_x822220000}

[[描述]{style="font-family:黑体"}]{#struct_0_15550_84251_1621395887}

[[iif]{lang="EN-US"}]{#struct_0_15550_84251_x1615604183}

[[入接口]{style="font-family:宋体"}]{#struct_0_15550_84251_x1524929338}

[[oif]{lang="EN-US"}]{#struct_0_15550_84251_x666955827}

[[出接口]{style="font-family:宋体"}]{#struct_0_15550_84251_x1780324175}

[[Merge state]{lang="EN-US"}]{#struct_0_15550_84251_1471513744}

[[抵消状态]{style="font-family:宋体"}]{#struct_0_15550_84251_416196859}

[[spt thres]{lang="EN-US"}]{#struct_0_15550_84251_x1107946217}

[[SPT]{lang="EN-US"}]{#struct_0_15550_84251_x488233712}[切换阈值]{style="font-family:宋体"}

[[reg suppress]{lang="EN-US"}]{#struct_0_15550_84251_1580978092}

[[注册抑制]{style="font-family:宋体"}]{#struct_0_15550_84251_1163776377}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15550_84251_205852436}

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_1218528841}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mrib event]{lang="EN-US"}]{#struct_0_15550_84251_x1108011753}

[\*Sep  7 15:59:02:172 2011 Sysname MRIB6/7/EVENT: -MDC=1; IPv6: Add msg(Type: add mfib, Len: 146) to ipc buffer(Count: 1) (M02346)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_991443727}*[向]{style="font-family:宋体"}[IPC]{lang="EN-US"}[缓冲区中添加一个消息（消息类型为：往]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[添加表项，长度为]{style="font-family:宋体"}[146]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Sep  7 15:59:02:185 2011 Sysname MRIB6/7/EVENT: -MDC=1; IPv6: Send msg to MFIB(Count 1, Len 158) success (M02272)]{lang="EN-US"}]{#struct_0_15550_84251_x363358495}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_x282231788}*[成功向]{style="font-family:宋体"}[MFIB]{lang="EN-US"}[发送一个消息（数量为]{style="font-family:宋体"}[1]{lang="EN-US"}[，长度为]{style="font-family:宋体"}[158]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_x1769162533}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[接口管理调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mrib interface]{lang="EN-US"}]{#struct_0_15550_84251_251057278}

[\*Oct 30 06:16:27:689 2012 Sysname MRIB6/7/IFM: -MDC=1; IPv6: Try to enable protocol 0x2 on interface GigabitEthernet1/0/1. (PM055007)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_299765640}*[尝试在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[（]{style="font-family:宋体"}[protocol 0x2]{lang="EN-US"}[）协议]{style="font-family:宋体"}*

[[\*Oct 30 06:16:27:689 2012 Sysname MRIB6/7/IFM: -MDC=1; IPv6: Create interface address for (GigabitEthernet1/0/1, 7:11::1) when sending message, reference 1. (PM052755)]{lang="EN-US"}]{#struct_0_15550_84251_1281242532}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_x1624600965}*[增加接口地址引用计数，用于发送接口变化消息]{style="font-family:宋体"}*

[[\*Oct 30 06:16:27:695 2012 Sysname MRIB6/7/IFM: -MDC=1; IPv6: Succeed in adding interface GigabitEthernet1/0/1. (PM052427)]{lang="EN-US"}]{#struct_0_15550_84251_x1108077289}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_705037996}*[成功添加接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的生效]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[接口]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_x866108001}[在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理功能，并打开公网实例]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mrib proxy]{lang="EN-US"}]{#struct_0_15550_84251_699517193}

[\*Jul  8 18:19:00:393 2013 Sysname MRIB6/7/PRY_RT: -MDC=1; IPv6: Relate group FF1E::1 to nonif list. (MP051207)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_x1682258391}*[将组]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[与空接口列表相关联]{style="font-family:宋体"}*

[[\*Jul  8 18:19:00:393 2013 Sysname MRIB6/7/PRY_EVT: -MDC=1; IPv6: Delete proxy routing-table relate interface: Vlan-interface33. (MP05821)]{lang="EN-US"}]{#struct_0_15550_84251_x1178338830}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_1176840996}*[在接口]{style="font-family:宋体"}[Vlan-interface33]{lang="EN-US"}[上删除代理路由表]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15550_84251_x1383449751}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 MRIB]{lang="EN-US"}[路由表项调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 mrib route]{lang="EN-US"}]{#struct_0_15550_84251_55249465}

[\*Sep  7 15:59:02:143 2011 Sysname MRIB6/7/ROUTE: -MDC=1; IPv6: Proc add entry (7:11::6,FFE3::101) msg with iif GigabitEthernet1/0/1(Oifs 1,RP 8:12::1) (M032579)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_1231108706}*[处理添加表项（]{style="font-family:宋体"}[7:11::6]{lang="EN-US"}[，]{style="font-family:宋体"}[FFE3::101]{lang="EN-US"}[）消息，表项入接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（出接口数量为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[8:12::1]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Sep  7 15:59:02:169 2011 Sysname MRIB6/7/ROUTE: -MDC=1; IPv6: Add oif GigabitEthernet1/0/1(Status ADD) to entry (7:11::6,FFE3::101) (M032419)]{lang="EN-US"}]{#struct_0_15550_84251_x1246905900}

[*[// ]{lang="EN-US"}*]{#struct_0_15550_84251_x1307267694}*[将出接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（状态为]{style="font-family:宋体"}[ADD]{lang="EN-US"}[）添加到表项（]{style="font-family:宋体"}[7:11::6]{lang="EN-US"}[，]{style="font-family:宋体"}[FFE3::101]{lang="EN-US"}[）中]{style="font-family:宋体"}*
