::: {#498266813 .myid}
[]{#_Toc47323842}[]{#_Toc404786989}[]{#struct_0_12181_84059_1082147373}[]{#_Toc276713137}[]{#_Toc138239296}[]{#_Toc136679734}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 fib**

------------------------------------------------------------------------

[**[display ipv6 fib]{lang="EN-US"}**]{#struct_0_12181_84059_290444583}[命令用来显示]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1239278808}

[**[display ipv6 fib ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] \[ *ipv6-address* \[ *prefix-length* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_102611509}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_377869801}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_330729455}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x110957171}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1306216344}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x512422554}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_946792811}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_1502072294}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1239344344}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12181_84059_x1771945266}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12181_84059_346217748}[：显示目的地址为指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_12181_84059_x249136288}[：目的地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_2123257121}

[[本命令可以用来查看]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}]{#struct_0_12181_84059_x773410176}[信息，包括转发的目的地址、前缀长度、转发的下一跳地址、转发报文的出接口等内容。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_12181_84059_x2019556731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**]{#struct_0_12181_84059_623469109}[参数，将显示公网的]{lang="EN-US" style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[信息；如果指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数，将显示指定]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{lang="EN-US" style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定前缀长度，将显示与指定目的]{style="font-family:宋体"}]{#struct_0_12181_84059_x1878162994}[IPv6]{lang="EN-US"}[地址最长匹配的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[信息；如果指定前缀长度时，将显示与指定目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和前缀长度精确匹配的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则显示公网所有的]{style="font-family:宋体"}]{#struct_0_12181_84059_1238754521}[IPv6 FIB]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_972636752}

[]{#_Ref189458167}[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x304095891}[显示公网所有的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 fib]{lang="EN-US"}]{#struct_0_12181_84059_x1153878148}

[ ]{lang="EN-US"}

[Destination count: 1 FIB entry count: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flag:]{lang="EN-US"}

[  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static]{lang="EN-US"}

[  R:Relay     F:FRR]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination: ::1                                            Prefix length: 128]{lang="EN-US"}

[Nexthop     : ::1                                            Flags: UH]{lang="EN-US"}

[Time stamp : 0x1                                            Label: Null]{lang="EN-US"}

[Interface  : InLoop0                                        Token: Invalid]{lang="EN-US"}

[]{#struct_0_12181_84059_2136581452}[[表1-1 ]{lang="EN-US"}[display ipv6 fib]{lang="EN-US"}]{#_Toc94583057}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_860010541}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x911895515}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_1238820057}

[[Destination count]{lang="EN-US"}]{#struct_0_12181_84059_1739265046}

[[目的地址的个数]{style="font-family:宋体"}]{#struct_0_12181_84059_1244450393}

[[FIB entry count]{lang="EN-US"}]{#struct_0_12181_84059_1228292953}

[[IPv6 FIB]{lang="EN-US"}]{#struct_0_12181_84059_1147346267}[表项数目]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_12181_84059_682723413}

[[转发的目的地址]{style="font-family:宋体"}]{#struct_0_12181_84059_1238623449}

[[Prefix length]{lang="EN-US"}]{#struct_0_12181_84059_x592148112}

[[转发的目的地址的前缀长度]{style="font-family:宋体"}]{#struct_0_12181_84059_781222088}

[[Nexthop]{lang="EN-US"}]{#struct_0_12181_84059_x8787099}

[[向目的地址转发报文的下一跳地址]{style="font-family:宋体"}]{#struct_0_12181_84059_1708591698}

[[Flags]{lang="EN-US"}]{#struct_0_12181_84059_1810274280}

[[路由的标志：]{style="font-family:宋体"}]{#struct_0_12181_84059_1238688985}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_12181_84059_1647032761}[：表示路由可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[G]{lang="EN-US"}]{#struct_0_12181_84059_x302097755}[：表示网关路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_12181_84059_900943434}[：表示主机路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_12181_84059_2003964790}[：表示黑洞路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_12181_84059_1239016665}[：表示动态路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_12181_84059_972041195}[：表示静态路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_12181_84059_2067121563}[：表示迭代路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_12181_84059_x183780481}[：表示快速重路由]{lang="EN-US" style="font-family:宋体"}

[[Time stamp]{lang="EN-US"}]{#struct_0_12181_84059_x696761067}

[[IPv6 FIB]{lang="EN-US"}]{#struct_0_12181_84059_1239082201}[表项的生成时间]{style="font-family:宋体"}

[[Label]{lang="EN-US"}]{#struct_0_12181_84059_x248316335}

[[MPLS]{lang="EN-US"}]{#struct_0_12181_84059_x1385212594}[内层标签]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_12181_84059_x1087372765}

[[转发报文的出接口]{style="font-family:宋体"}]{#struct_0_12181_84059_2073044077}

[[Token]{lang="EN-US"}]{#struct_0_12181_84059_1238885593}

[[LSP]{lang="EN-US"}]{#struct_0_12181_84059_x1762865901}[索引号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1706346887 .myid}
[]{#_Toc59352317}[]{#_Toc404786990}[]{#struct_0_12181_84059_1001176231}[]{#_Toc279391291}[]{#_Toc249244999}[]{#_Toc138239299}[]{#_Toc136679737}[]{#_Toc69790797}[]{#_Toc216496540}[]{#_Toc216501071}[]{#_Toc217899652}[]{#_Toc216496541}[]{#_Toc216501072}[]{#_Toc217899653}[]{#_Toc216496544}[]{#_Toc216501075}[]{#_Toc217899656}[]{#_Toc216496545}[]{#_Toc216501076}[]{#_Toc217899657}[]{#_Toc216496546}[]{#_Toc216501077}[]{#_Toc217899658}[]{#_Toc216496547}[]{#_Toc216501078}[]{#_Toc217899659}[]{#_Toc216496548}[]{#_Toc216501079}[]{#_Toc217899660}[]{#_Toc216496549}[]{#_Toc216501080}[]{#_Toc217899661}[]{#_Toc216496550}[]{#_Toc216501081}[]{#_Toc217899662}[]{#_Toc216496551}[]{#_Toc216501082}[]{#_Toc217899663}[]{#_Toc216496552}[]{#_Toc216501083}[]{#_Toc217899664}[]{#_Toc216496553}[]{#_Toc216501084}[]{#_Toc217899665}[]{#_Toc216496554}[]{#_Toc216501085}[]{#_Toc217899666}[]{#_Toc216496555}[]{#_Toc216501086}[]{#_Toc217899667}[]{#_Toc90625813}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 icmp statistics**

------------------------------------------------------------------------

[**[display ipv6 icmp statistics]{lang="EN-US"}**]{#struct_0_12181_84059_1768754432}[命令用来显示]{style="font-family:
宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_918889939}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1083152964}

[**[display ipv6 icmp statistics]{lang="EN-US"}**]{#struct_0_12181_84059_x942227634}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_1238951129}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 icmp statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_1334550359}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x1677716363}[模式：]{style="font-family:宋体"}

[**[display ipv6 icmp statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_x1349721396}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_203272052}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1984493443}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1653396510}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x498848297}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_1239278809}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_102677045}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_726283140}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_700166121}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x961315368}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1517000720}[：显示指定成员设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1659847358}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1651194692}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x151470440}[：显示指定单板的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_x1320882490}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_926881504}

[[本命令可以用来查看设备接收和发送的各类]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_624802151}[流量统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1239344345}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1772010802}[显示]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 icmp statistics]{lang="EN-US"}]{#struct_0_12181_84059_950292284}

[  Input: bad code                0           too short                  0]{lang="EN-US"}

[         checksum error          0           bad length                 0]{lang="EN-US"}

[         path MTU changed        0          destination unreachable  0]{lang="EN-US"}

[         too big                  0           parameter problem         0]{lang="EN-US"}

[         echo request            0           echo reply                  0]{lang="EN-US"}

[         neighbor solicit        0           neighbor advertisement   0]{lang="EN-US"}

[         router solicit          0           router advertisement      0]{lang="EN-US"}

[         redirect                 0           router renumbering         0]{lang="EN-US"}

[ output: parameter problem     0           echo request                0]{lang="EN-US"}

[         echo reply               0           unreachable no route       0]{lang="EN-US"}

[         unreachable admin       0           unreachable beyond scope 0]{lang="EN-US"}

[         unreachable address    0           unreachable no port        0]{lang="EN-US"}

[         too big                   0           time exceed transit       0]{lang="EN-US"}

[         time exceed reassembly 0           redirect                    0]{lang="EN-US"}

[         ratelimited               0           other errors               0]{lang="EN-US"}

[]{#struct_0_12181_84059_831084968}[]{#_Toc138413615}[]{#_Toc138239194}[]{#_Toc68600616}[]{#_Toc58505325}[[表1-2 ]{lang="EN-US"}[display ipv6 icmp statistics]{lang="EN-US"}]{#_Toc43289059}[命令显示信息描述]{style="font-family:
黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_857472653}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_1238754518}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_973095503}

[[bad code]{lang="EN-US"}]{#struct_0_12181_84059_x935269115}

[[接收的代码错误的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1661080109}

[[too short]{lang="EN-US"}]{#struct_0_12181_84059_895505355}

[[接收的长度过小的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_620749006}

[[checksum error]{lang="EN-US"}]{#struct_0_12181_84059_880870887}

[[接收的校验和错误的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1238820054}

[[bad length]{lang="EN-US"}]{#struct_0_12181_84059_1739461654}

[[接收的长度错误的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_x1107124232}

[[path MTU changed]{lang="EN-US"}]{#struct_0_12181_84059_1674477715}

[[接收的路径]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_12181_84059_x784827510}[改变报文数]{style="font-family:宋体"}

[[destination unreachable]{lang="EN-US"}]{#struct_0_12181_84059_1238623446}

[[接收的目标不可达报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_x591427216}

[[too big]{lang="EN-US"}]{#struct_0_12181_84059_x1872520512}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1304401297}[发送的数据包超长报文数]{style="font-family:宋体"}

[[parameter problem]{lang="EN-US"}]{#struct_0_12181_84059_753657379}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1583452253}[发送的参数错误报文数]{style="font-family:宋体"}

[[echo request]{lang="EN-US"}]{#struct_0_12181_84059_1238688982}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_1646967225}[发送的回显请求报文数]{style="font-family:宋体"}

[[echo reply]{lang="EN-US"}]{#struct_0_12181_84059_x1098974295}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1873009455}[发送的回应响应报文数]{style="font-family:宋体"}

[[neighbor solicit]{lang="EN-US"}]{#struct_0_12181_84059_1026896808}

[[接收的邻居请求报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1239016662}

[[neighbor advertisement]{lang="EN-US"}]{#struct_0_12181_84059_971582443}

[[接收的邻居通告报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_227931683}

[[router solicit]{lang="EN-US"}]{#struct_0_12181_84059_x1618943098}

[[接收的路由请求报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1239082198}

[[router advertisement]{lang="EN-US"}]{#struct_0_12181_84059_1326251592}

[[接收的路由通告报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1162455220}

[[redirect]{lang="EN-US"}]{#struct_0_12181_84059_x207578543}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1854106081}[发送的重定向报文数]{style="font-family:宋体"}

[[router renumbering ]{lang="EN-US"}]{#struct_0_12181_84059_1238885590}

[[接收的路由器重计数报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_x1762931437}

[[unreachable no route]{lang="EN-US"}]{#struct_0_12181_84059_x1514262791}

[[发送的路由不可达报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1660881240}

[[unreachable admin]{lang="EN-US"}]{#struct_0_12181_84059_1238951126}

[[发送的与目标的通信被管理策略禁止的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1333567319}

[[unreachable beyondscope]{lang="EN-US"}]{#struct_0_12181_84059_x1138379096}

[[发送的源地址超出范围的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_471997131}

[[unreachable address]{lang="EN-US"}]{#struct_0_12181_84059_1239278806}

[[发送的地址不可达报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_103529013}

[[unreachable no port]{lang="EN-US"}]{#struct_0_12181_84059_x561179302}

[[发送的端口不可达报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1239344342}

[[time exceed transit]{lang="EN-US"}]{#struct_0_12181_84059_x1771552050}

[[发送的传输超时报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_x1949633863}

[[time exceed reassembly]{lang="EN-US"}]{#struct_0_12181_84059_965315009}

[[发送的重组超时报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1238754519}

[[ratelimited]{lang="EN-US"}]{#struct_0_12181_84059_973161039}

[[因速率超过限制而未发送的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_x1339411847}

[[other errors]{lang="EN-US"}]{#struct_0_12181_84059_516203737}

[[发送的其他的错误报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1238820055}

[ ]{lang="EN-US"}

::: {#904192593 .myid}
[]{#_Toc59352315}[]{#_Toc404786991}[]{#struct_0_12181_84059_1739396118}[]{#_Toc138417072}[]{#_Toc137020653}[]{#_Toc59352303}[]{#_Toc90625817}[]{#_Toc90625819}[]{#_Toc90625821}[]{#_Toc90625823}[]{#_Toc90625825}[]{#_Toc90625826}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 interface**

------------------------------------------------------------------------

[**[display ipv6 interface]{lang="EN-US"}**]{#struct_0_12181_84059_x1467405306}[命令用来显示接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_2119440886}

[**[display ipv6 interface]{lang="EN-US"}**[ \[ *interface-type* \[ *interface-number* \] \] \[ **brief** \]]{lang="EN-US"}]{#struct_0_12181_84059_x40503008}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_483324022}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1635582044}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1238623447}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x591492752}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x303743757}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x227836697}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1690756947}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x558385844}

[*[interface-type]{lang="EN-US"}*]{#struct_0_12181_84059_1845996348}[：显示指定类型接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_12181_84059_x421689583}[：显示指定接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_12181_84059_1238688983}[：显示接口摘要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1646901689}

[[如果配置命令时指定了]{style="font-family:宋体"}**[brief]{lang="EN-US"}**]{#struct_0_12181_84059_x1153583279}[关键字，则显示接口的摘要信息，包括接口的物理状态、链路层协议状态以及]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息；否则，将显示接口的详细信息，包括接口上和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[相关的配置以及运行信息，以及]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1338490417}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型和接口编号，则显示所有接口的]{style="font-family:宋体"}]{#struct_0_12181_84059_x746658620}[IPv6]{lang="EN-US"}[信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定接口类型，不指定接口编号，则显示所有指定类型接口的]{style="font-family:宋体"}]{#struct_0_12181_84059_545568357}[IPv6]{lang="EN-US"}[信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则显示指定接口的]{style="font-family:宋体"}]{#struct_0_12181_84059_36812547}[IPv6]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1982282205}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1799392894}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1239016663}[查看接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_12181_84059_1239082199}

[GigabitEthernet1/0/1 current state: UP]{lang="EN-US"}

[Line protocol current state: UP]{lang="EN-US"}

[IPv6 is enabled, link-local address is FE80::200:1FF:FE04:5D00 \[TENTATIVE\]]{lang="EN-US"}

[  Global unicast address(es):]{lang="EN-US"}

[    10::1234:56FF:FE65:4322, subnet is 10::/64 \[TENTATIVE\] \[AUTOCFG\]]{lang="EN-US"}

[      \[valid lifetime 4641s/preferred lifetime 4637s\]]{lang="EN-US"}

[    20::1234:56ff:fe65:4322, subnet is 20::/64 \[TENTATIVE\] \[EUI-64\]]{lang="EN-US"}

[    30::1, subnet is 30::/64 \[TENTATIVE\] \[ANYCAST\]]{lang="EN-US"}

[    40::2, subnet is 40::/64 \[TENTATIVE\] \[DHCP\]]{lang="EN-US"}

[    50::3, subnet is 50::/64 \[TENTATIVE\]]{lang="EN-US"}

[  Joined group address(es):]{lang="EN-US"}

[    FF02::1]{lang="EN-US"}

[    FF02::2]{lang="EN-US"}

[    FF02::1:FF00:1]{lang="EN-US"}

[    FF02::1:FF04:5D00]{lang="EN-US"}

[  MTU is 1500 bytes]{lang="EN-US"}

[  ND DAD is enabled, number of DAD attempts: 1]{lang="EN-US"}

[  ND reachable time is 30000 milliseconds]{lang="EN-US"}

[  ND retransmit interval is 1000 milliseconds]{lang="EN-US"}

[  Hosts use stateless autoconfig for addresses]{lang="EN-US"}

[IPv6 Packet statistics:]{lang="EN-US"}

[  InReceives:                       0]{lang="EN-US"}

[  InTooShorts:                      0]{lang="EN-US"}

[  InTruncatedPkts:                0]{lang="EN-US"}

[  InHopLimitExceeds:              0]{lang="EN-US"}

[  InBadHeaders:                    0]{lang="EN-US"}

[  InBadOptions:                    0]{lang="EN-US"}

[  ReasmReqds:                       0]{lang="EN-US"}

[  ReasmOKs:                     0]{lang="EN-US"}

[  InFragDrops:                      0]{lang="EN-US"}

[  InFragTimeouts:                  0]{lang="EN-US"}

[  OutFragFails:                    0]{lang="EN-US"}

[  InUnknownProtos:                 0]{lang="EN-US"}

[  InDelivers:                       0]{lang="EN-US"}

[  OutRequests:                      0]{lang="EN-US"}

[  OutForwDatagrams:               0]{lang="EN-US"}

[  InNoRoutes:                       0]{lang="EN-US"}

[  InTooBigErrors:                  0]{lang="EN-US"}

[  OutFragOKs:                       0]{lang="EN-US"}

[  OutFragCreates:                  0]{lang="EN-US"}

[  InMcastPkts:                      0]{lang="EN-US"}

[  InMcastNotMembers:              0]{lang="EN-US"}

[  OutMcastPkts:                    0]{lang="EN-US"}

[  InAddrErrors:                    0]{lang="EN-US"}

[  InDiscards:                       0]{lang="EN-US"}

[  OutDiscards:                      0]{lang="EN-US"}

[]{#struct_0_12181_84059_1326186056}[]{#_Toc138417051}[[表1-3 ]{lang="EN-US"}[display ipv6 interface]{lang="EN-US"}]{#_Toc94583058}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_882373245}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_1238885591}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x1762996973}

[[GigabitEthernet1/0/1 current state]{lang="EN-US"}]{#struct_0_12181_84059_x415595522}

[[接口的物理状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_x203870131}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_12181_84059_x1981353497}[：表示该接口已经通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_12181_84059_1854589479}[：该接口的管理状态为开启，但物理状态为关闭（可能因为没有连接好或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_12181_84059_1238951127}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol current state]{lang="EN-US"}]{#struct_0_12181_84059_1333632855}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_797900298}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_12181_84059_x1555692353}[：该接口的协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_12181_84059_x992440393}[：该接口的协议状态为开启]{style="font-family:宋体"}

[[IPv6 is enabled]{lang="EN-US"}]{#struct_0_12181_84059_x2009389524}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1239278807}[转发功能状态（为某接口配置任一]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址后系统将自动使能该接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能，此例中处于使能状态）]{style="font-family:宋体"}

[[link-local address]{lang="EN-US"}]{#struct_0_12181_84059_103594549}

[[接口上配置的链路本地地址]{style="font-family:宋体"}]{#struct_0_12181_84059_1789119734}

[[Global unicast address(es)]{lang="EN-US"}]{#struct_0_12181_84059_x1093187818}

[[接口上配置的全球单播地址]{style="font-family:宋体"}]{#struct_0_12181_84059_1928411450}

[[可能的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1239344343}[地址状态及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TENTATIVE]{lang="EN-US"}]{#struct_0_12181_84059_x1771617586}[：该状态为地址初始化状态，此时该地址可能正在进行]{style="font-family:宋体"}[DAD]{lang="EN-US"}[检测或准备进行]{style="font-family:宋体"}[DAD]{lang="EN-US"}[检测，处于该状态的地址不能作为报文的源地址或者目的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DUPLICATE]{lang="EN-US"}]{#struct_0_12181_84059_x442925836}[：该状态表明地址]{style="font-family:宋体"}[DAD]{lang="EN-US"}[检测已经结束，由于该地址在链路上不唯一，因此不能使用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PREFERRED]{lang="EN-US"}]{#struct_0_12181_84059_2036642785}[：该状态表明地址处于首选生命期以内。该状态的地址可以作为报文的源地址或者目的地址。为该状态时，不显示地址的状态标识]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEPRECATED]{lang="EN-US"}]{#struct_0_12181_84059_1624044042}[：该状态表明地址超过首选生命期，但是在有效生命期以内。该状态地址有效，但不应作为新建连接报文的源地址，目的地址是该地址的报文还可以被正常处理]{style="font-family:宋体"}

[[如果地址来源不为手工配置的全球单播地址，则会标记地址来源。可能的地址来源及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1490128833}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTOCFG]{lang="EN-US"}]{#struct_0_12181_84059_1173310796}[：表示无状态自动配置的全球单播地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_12181_84059_x1208732381}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器分配的全球单播地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EUI-64]{lang="EN-US"}]{#struct_0_12181_84059_10117402}[：表示手工配置的]{lang="EN-US" style="font-family:宋体"}[EUI-64]{lang="EN-US"}[格式全球单播地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RANDOM]{lang="EN-US"}]{#struct_0_12181_84059_1522136423}[：表示自动生成的临时地址]{lang="EN-US" style="font-family:宋体"}

[[如果地址为手工配置的任播地址，则会标记]{style="font-family:宋体"}[ANYCAST]{lang="EN-US"}]{#struct_0_12181_84059_x1490063297}

[[valid lifetime]{lang="EN-US"}]{#struct_0_12181_84059_711655382}

[[接口上无状态自动配置的全球单播地址的有效生命期]{style="font-family:宋体"}]{#struct_0_12181_84059_212045101}

[[preferred lifetime]{lang="EN-US"}]{#struct_0_12181_84059_1677368447}

[[接口上无状态自动配置的全球单播地址的首选生命期]{style="font-family:宋体"}]{#struct_0_12181_84059_x1490259905}

[[Joined group address(es)]{lang="EN-US"}]{#struct_0_12181_84059_13855760}

[[接口加入的组播组地址]{style="font-family:宋体"}]{#struct_0_12181_84059_x216903448}

[[MTU]{lang="EN-US"}]{#struct_0_12181_84059_x1708427987}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_12181_84059_x1490194369}

[[ND DAD is enabled, number of DAD attempts]{lang="EN-US"}]{#struct_0_12181_84059_1039314882}

[[重复地址检测功能是否使能（该例中使能）]{style="font-family:宋体"}]{#struct_0_12181_84059_1863467722}

[[若处于使能状态则同时显示重复地址检测时发送邻居请求消息的次数（可通过]{style="font-family:宋体"}**[ipv6 nd dad attempts]{lang="EN-US"}**]{#struct_0_12181_84059_110068615}[命令进行配置）]{style="font-family:宋体"}

[[若处于关闭状态则显示"]{style="font-family:宋体"}[ND DAD is disabled]{lang="EN-US"}]{#struct_0_12181_84059_x1569190695}["（可通过配置重复地址检测时发送邻居请求消息的次数为]{style="font-family:宋体"}[0]{lang="EN-US"}[关闭该功能）]{style="font-family:宋体"}

[[ND reachable time]{lang="EN-US"}]{#struct_0_12181_84059_x1489866689}

[[保持邻居可达的时间]{style="font-family:宋体"}]{#struct_0_12181_84059_723565753}

[[ND retransmit interval]{lang="EN-US"}]{#struct_0_12181_84059_472685727}

[[邻居请求消息重传时间间隔]{style="font-family:宋体"}]{#struct_0_12181_84059_x1489801153}

[[Hosts use stateless autoconfig for addresses]{lang="EN-US"}]{#struct_0_12181_84059_x254267136}

[[主机采用无状态自动配置的方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_998293927}[地址]{style="font-family:宋体"}

[[InReceives]{lang="EN-US"}]{#struct_0_12181_84059_1954658722}

[[接口接收到的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x207042139}[报文，包括各种错误的报文]{style="font-family:宋体"}

[[InTooShorts]{lang="EN-US"}]{#struct_0_12181_84059_1684473673}

[[接口接收到的太短的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1954724258}[报文，譬如报文长度不足]{style="font-family:宋体"}[40]{lang="EN-US"}[字节]{style="font-family:宋体"}

[[InTruncatedPkts]{lang="EN-US"}]{#struct_0_12181_84059_x1687989687}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x929038439}[报文，其实际长度小于报文内容中所指出的报文长度]{style="font-family:宋体"}

[[InHopLimitExceeds]{lang="EN-US"}]{#struct_0_12181_84059_1954789794}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1380996326}[报文，其跳数超出限制]{style="font-family:宋体"}

[[InBadHeaders]{lang="EN-US"}]{#struct_0_12181_84059_458448767}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1955379618}[报文，其基本报文头错误]{style="font-family:宋体"}

[[InBadOptions]{lang="EN-US"}]{#struct_0_12181_84059_572740978}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x282116918}[报文，其扩展报文头错误]{style="font-family:宋体"}

[[ReasmReqds]{lang="EN-US"}]{#struct_0_12181_84059_1955445154}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1305879167}[分片报文]{style="font-family:宋体"}

[[ReasmOKs]{lang="EN-US"}]{#struct_0_12181_84059_x724998460}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1954855329}[分片，被组装好的报文，这里指的不是分片个数，是组装好的报文数]{style="font-family:宋体"}

[[InFragDrops]{lang="EN-US"}]{#struct_0_12181_84059_x2088182524}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1954920865}[分片报文，该分片报文由于错误被丢弃]{style="font-family:宋体"}

[[InFragTimeouts]{lang="EN-US"}]{#struct_0_12181_84059_x510123028}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_670331978}[分片报文，该分片停留在系统缓冲中时间超过指定时间，被丢弃]{style="font-family:宋体"}

[[OutFragFails]{lang="EN-US"}]{#struct_0_12181_84059_1954986401}

[[出接口上分片失败的报文]{style="font-family:宋体"}]{#struct_0_12181_84059_x1691260856}

[[InUnknownProtos]{lang="EN-US"}]{#struct_0_12181_84059_x831295538}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1955051937}[报文，其协议类型不能被识别或不能被支持]{style="font-family:宋体"}

[[InDelivers]{lang="EN-US"}]{#struct_0_12181_84059_x507531145}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_934503905}[报文，该报文被上送到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的用户协议处（如]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[等）]{style="font-family:宋体"}

[[OutRequests]{lang="EN-US"}]{#struct_0_12181_84059_1954593185}

[[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x518404443}[本地出报文，即各]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的用户协议层要求]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[发送出去的报文]{style="font-family:宋体"}

[[OutForwDatagrams]{lang="EN-US"}]{#struct_0_12181_84059_1954658721}

[[出接口上被转发的报文]{style="font-family:宋体"}]{#struct_0_12181_84059_x207238747}

[[InNoRoutes]{lang="EN-US"}]{#struct_0_12181_84059_2066912660}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1954724257}[报文，找不到匹配的路由被丢弃]{style="font-family:宋体"}

[[InTooBigErrors]{lang="EN-US"}]{#struct_0_12181_84059_x1688579511}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1954789793}[报文，转发时，由于超过链路]{style="font-family:宋体"}[MTU]{lang="EN-US"}[被丢弃]{style="font-family:宋体"}

[[OutFragOKs]{lang="EN-US"}]{#struct_0_12181_84059_1380668646}

[[出接口上分片成功的报文]{style="font-family:宋体"}]{#struct_0_12181_84059_157471316}

[[OutFragCreates]{lang="EN-US"}]{#struct_0_12181_84059_1955379617}

[[出接口上成功分片后的分片报文，指分片数]{style="font-family:宋体"}]{#struct_0_12181_84059_572806514}

[[InMcastPkts]{lang="EN-US"}]{#struct_0_12181_84059_1955445153}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1305682559}[组播报文]{style="font-family:宋体"}

[[InMcastNotMembers]{lang="EN-US"}]{#struct_0_12181_84059_x21839207}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_836102413}[组播报文，但该接口却没有加入对应组播组，报文被丢弃]{style="font-family:宋体"}

[[OutMcastPkts]{lang="EN-US"}]{#struct_0_12181_84059_39029089}

[[接口发送的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_494254268}[组播报文]{style="font-family:宋体"}

[[InAddrErrors]{lang="EN-US"}]{#struct_0_12181_84059_38963553}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1751361150}[报文，其目的地址不合法，报文被丢弃]{style="font-family:宋体"}

[[InDiscards]{lang="EN-US"}]{#struct_0_12181_84059_38635873}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1526041585}[报文，由于资源问题被丢弃的报文，而不是由于报文内容等被丢弃的报文]{style="font-family:宋体"}

[[OutDiscards]{lang="EN-US"}]{#struct_0_12181_84059_x673167582}

[[接口需要发送的报文，由于资源问题被丢弃的报文，而不是由于报文内容等被丢弃的报文]{style="font-family:宋体"}]{#struct_0_12181_84059_38570337}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1027565097}[查看所有接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 interface brief]{lang="EN-US"}]{#struct_0_12181_84059_x1489997761}

[\*down: administratively down]{lang="EN-US"}

[(s): spoofing]{lang="EN-US"}

[Interface                                 Physical Protocol IPv6 Address]{lang="EN-US"}

[GigabitEthernet1/0/1                    up        up         2001::1]{lang="EN-US"}

[GigabitEthernet1/0/2                    up        up         Unassigned]{lang="EN-US"}

[]{#struct_0_12181_84059_697240621}[]{#_Toc138417052}[[表1-4 ]{lang="EN-US"}[display ipv6 interface brief]{lang="EN-US"}]{#_Toc94583059}[命令显示信息描述]{style="font-family:
黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_878048277}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_43897505}

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_677930775}

[[\*down: administratively down]{lang="EN-US"}]{#struct_0_12181_84059_x505651734}

[[接口处于管理]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_12181_84059_1818650173}[状态，即采用]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[命令关闭了该接口]{style="font-family:宋体"}

[[(s): spoofing]{lang="EN-US"}]{#struct_0_12181_84059_x1489932225}

[[接口的欺骗属性，即接口的链路协议状态显示是]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_12181_84059_1162486318}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_12181_84059_563220201}

[[接口的名称]{style="font-family:宋体"}]{#struct_0_12181_84059_1475407247}

[[Physical]{lang="EN-US"}]{#struct_0_12181_84059_2087025542}

[[接口的物理状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_1248113148}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\*down]{lang="EN-US"}]{#struct_0_12181_84059_x1489604545}[：表示该接口已经通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_12181_84059_1590893106}[：该接口的管理状态为开启，但物理状态为关闭（可能因为没有连接好或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_12181_84059_1242757587}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_12181_84059_x181601178}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1322272312}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_12181_84059_x902124220}[：该接口的协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_12181_84059_x1489539009}[：该接口的协议状态为开启]{style="font-family:宋体"}

[[IPv6 Address]{lang="EN-US"}]{#struct_0_12181_84059_1311353580}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1507743889}[地址，接口上有全球单播地址时，显示地址最小的全球单播地址，没有全球单播地址则显示链路本地地址，没有链路本地地址则显示"]{style="font-family:宋体"}[Unassigned]{lang="EN-US"}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_2019999308}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1403836520}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 interface vlan-interface 2]{lang="EN-US"}]{#struct_0_12181_84059_x1490063296}

[Vlan-interface2 current state: UP]{lang="EN-US"}

[Line protocol current state: UP]{lang="EN-US"}

[IPv6 is enabled, link-local address is FE80::1234:56FF:FE65:4322 \[TENTATIVE\]]{lang="EN-US"}

[  Global unicast address(es):]{lang="EN-US"}

[    10::1234:56FF:FE65:4322, subnet is 10::/64 \[TENTATIVE\] \[AUTOCFG\]]{lang="EN-US"}

[      \[valid lifetime 4641s/preferred lifetime 4637s\]]{lang="EN-US"}

[    20::1234:56ff:fe65:4322, subnet is 20::/64 \[TENTATIVE\] \[EUI-64\]]{lang="EN-US"}

[    30::1, subnet is 30::/64 \[TENTATIVE\] \[ANYCAST\]]{lang="EN-US"}

[    40::2, subnet is 40::/64 \[TENTATIVE\] \[DHCP\]]{lang="EN-US"}

[    50::3, subnet is 50::/64 \[TENTATIVE\]]{lang="EN-US"}

[  Joined group address(es):]{lang="EN-US"}

[    FF02::1]{lang="EN-US"}

[    FF02::2]{lang="EN-US"}

[    FF02::1:FF00:1]{lang="EN-US"}

[    FF02::1:FF65:4322]{lang="EN-US"}

[  MTU is 1500 bytes]{lang="EN-US"}

[  ND DAD is enabled, number of DAD attempts: 1]{lang="EN-US"}

[  ND reachable time is 30000 milliseconds]{lang="EN-US"}

[  ND retransmit interval is 1000 milliseconds]{lang="EN-US"}

[  Hosts use stateless autoconfig for addresses]{lang="EN-US"}

[IPv6 Packet statistics:]{lang="EN-US"}

[  InReceives:                       0]{lang="EN-US"}

[  InTooShorts:                      0]{lang="EN-US"}

[  InTruncatedPkts:                0]{lang="EN-US"}

[  InHopLimitExceeds:              0]{lang="EN-US"}

[  InBadHeaders:                    0]{lang="EN-US"}

[  InBadOptions:                    0]{lang="EN-US"}

[  ReasmReqds:                       0]{lang="EN-US"}

[  ReasmOKs:                     0]{lang="EN-US"}

[  InFragDrops:                      0]{lang="EN-US"}

[  InFragTimeouts:                  0]{lang="EN-US"}

[  OutFragFails:                    0]{lang="EN-US"}

[  InUnknownProtos:                 0]{lang="EN-US"}

[  InDelivers:                       0]{lang="EN-US"}

[  OutRequests:                      0]{lang="EN-US"}

[  OutForwDatagrams:               0]{lang="EN-US"}

[  InNoRoutes:                       0]{lang="EN-US"}

[  InTooBigErrors:                  0]{lang="EN-US"}

[  OutFragOKs:                       0]{lang="EN-US"}

[  OutFragCreates:                  0]{lang="EN-US"}

[  InMcastPkts:                      0]{lang="EN-US"}

[  InMcastNotMembers:              0]{lang="EN-US"}

[  OutMcastPkts:                    0]{lang="EN-US"}

[  InAddrErrors:                    0]{lang="EN-US"}

[  InDiscards:                       0]{lang="EN-US"}

[  OutDiscards:                      0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ipv6 interface]{lang="EN-US"}]{#struct_0_12181_84059_x854428559}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_878745869}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_385587044}

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x1529079005}

[[Vlan-interface2 current state]{lang="EN-US"}]{#struct_0_12181_84059_x1490259904}

[[接口的物理状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_1579939701}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_12181_84059_88480364}[：表示该]{lang="EN-US" style="font-family:
  宋体"}[VLAN]{lang="EN-US"}[接口已经通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_12181_84059_x54101696}[：该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的管理状态为开启，但物理状态为关闭，即该接口对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内没有处于]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态的端口（可能因为没有连接好或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_12181_84059_406869189}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol current state]{lang="EN-US"}]{#struct_0_12181_84059_x46025693}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1490194368}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_12181_84059_x1689568473}[：该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_12181_84059_1511270835}[：该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的协议状态为开启]{style="font-family:宋体"}

[[IPv6 is enabled]{lang="EN-US"}]{#struct_0_12181_84059_x475265691}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1693605797}[转发功能状态（为某接口配置任一]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址后系统将自动使能该接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能，此例中处于使能状态）]{style="font-family:宋体"}

[[link-local address]{lang="EN-US"}]{#struct_0_12181_84059_x1489866688}

[[接口上配置的链路本地地址]{style="font-family:宋体"}]{#struct_0_12181_84059_x842518188}

[[Global unicast address(es)]{lang="EN-US"}]{#struct_0_12181_84059_x1940081137}

[[接口上配置的全球单播地址]{style="font-family:宋体"}]{#struct_0_12181_84059_x1200710126}

[[可能的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_783521473}[地址状态及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TENTATIVE]{lang="EN-US"}]{#struct_0_12181_84059_x1220728600}[：该状态为地址初始化状态，此时该地址可能正在进行]{style="font-family:宋体"}[DAD]{lang="EN-US"}[检测或准备进行]{style="font-family:宋体"}[DAD]{lang="EN-US"}[检测，处于该状态的地址不能作为报文的源地址或者目的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DUPLICATE]{lang="EN-US"}]{#struct_0_12181_84059_x1489801152}[：该状态表明地址]{style="font-family:宋体"}[DAD]{lang="EN-US"}[检测已经结束，由于该地址在链路上不唯一，因此不能使用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PREFERRED]{lang="EN-US"}]{#struct_0_12181_84059_x1820351077}[：该状态表明地址处于首选生命期以内。该状态的地址可以作为报文的源地址或者目的地址。为该状态时，不显示地址的状态标识]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEPRECATED]{lang="EN-US"}]{#struct_0_12181_84059_1305798639}[：该状态表明地址有效，但不应作为新建连接报文的源地址，目的地址是该地址的报文还需要被正常处理]{style="font-family:宋体"}

[[如果地址来源不为手工配置的全球单播地址，则会标记地址来源。可能的地址来源及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_1902692452}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTOCFG]{lang="EN-US"}]{#struct_0_12181_84059_x1900004755}[：表示无状态自动配置的全球单播地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_12181_84059_x1489997760}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器分配的全球单播地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EUI-64]{lang="EN-US"}]{#struct_0_12181_84059_x2031642734}[：表示手工配置的]{lang="EN-US" style="font-family:宋体"}[EUI-64]{lang="EN-US"}[格式全球单播地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RANDOM]{lang="EN-US"}]{#struct_0_12181_84059_2059505763}[：表示自动生成的临时地址]{lang="EN-US" style="font-family:宋体"}

[[如果地址为手工配置的任播地址，则会标记]{style="font-family:宋体"}[ANYCAST]{lang="EN-US"}]{#struct_0_12181_84059_x1101409874}

[[valid lifetime]{lang="EN-US"}]{#struct_0_12181_84059_x1489932224}

[[接口上无状态自动配置的全球单播地址的有效生命期]{style="font-family:宋体"}]{#struct_0_12181_84059_x1566397037}

[[preferred lifetime]{lang="EN-US"}]{#struct_0_12181_84059_809853573}

[[接口上无状态自动配置的全球单播地址的首选生命期]{style="font-family:宋体"}]{#struct_0_12181_84059_1202245571}

[[Joined group address(es)]{lang="EN-US"}]{#struct_0_12181_84059_x1489604544}

[[接口加入的组播组地址]{style="font-family:宋体"}]{#struct_0_12181_84059_24809165}

[[MTU]{lang="EN-US"}]{#struct_0_12181_84059_39538817}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_12181_84059_462332015}

[[ND DAD is enabled, number of DAD attempts]{lang="EN-US"}]{#struct_0_12181_84059_x1489539008}

[[重复地址检测功能是否使能（该例中使能）]{style="font-family:宋体"}]{#struct_0_12181_84059_x1417529775}

[[若处于使能状态则同时显示重复地址检测时发送邻居请求消息的次数（可通过]{style="font-family:宋体"}**[ipv6 nd dad attempts]{lang="EN-US"}**]{#struct_0_12181_84059_x1019517660}[命令进行配置）]{style="font-family:宋体"}

[[若处于关闭状态则显示"]{style="font-family:宋体"}[ND DAD is disabled]{lang="EN-US"}]{#struct_0_12181_84059_x1478308435}["（可通过配置重复地址检测时发送邻居请求消息的次数为]{style="font-family:宋体"}[0]{lang="EN-US"}[关闭该功能）]{style="font-family:宋体"}

[[ND reachable time]{lang="EN-US"}]{#struct_0_12181_84059_x1490128835}

[[保持邻居可达的时间]{style="font-family:宋体"}]{#struct_0_12181_84059_10511382}

[[ND retransmit interval]{lang="EN-US"}]{#struct_0_12181_84059_1313913389}

[[邻居请求消息重传时间间隔]{style="font-family:宋体"}]{#struct_0_12181_84059_x865819083}

[[Hosts use stateless autoconfig for addresses]{lang="EN-US"}]{#struct_0_12181_84059_x1490063299}

[[主机采用无状态自动配置的方式获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x94913672}[地址]{style="font-family:宋体"}

[[InReceives]{lang="EN-US"}]{#struct_0_12181_84059_x548121305}

[[接口接收到的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1490259907}[报文，包括各种错误的报文]{style="font-family:宋体"}

[[InTooShorts]{lang="EN-US"}]{#struct_0_12181_84059_x1148943654}

[[接口接收到的太短的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_2065078792}[报文，譬如报文长度不足]{style="font-family:宋体"}[40]{lang="EN-US"}[字节]{style="font-family:宋体"}

[[InTruncatedPkts]{lang="EN-US"}]{#struct_0_12181_84059_x1635868052}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1490194371}[报文，其实际长度小于报文内容中所指出的报文长度]{style="font-family:宋体"}

[[InHopLimitExceeds]{lang="EN-US"}]{#struct_0_12181_84059_683018986}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1385047924}[报文，其跳数超出限制]{style="font-family:宋体"}

[[InBadHeaders]{lang="EN-US"}]{#struct_0_12181_84059_x1489866691}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_367400929}[报文，其基本报文头错误]{style="font-family:宋体"}

[[InBadOptions]{lang="EN-US"}]{#struct_0_12181_84059_843256602}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1489801155}[报文，其扩展报文头错误]{style="font-family:宋体"}

[[ReasmReqds]{lang="EN-US"}]{#struct_0_12181_84059_908532278}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_966437999}[分片报文]{style="font-family:宋体"}

[[ReasmOKs]{lang="EN-US"}]{#struct_0_12181_84059_x1489997763}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x465558793}[分片，被组装好的报文，这里指的不是分片个数，是组装好的报文数]{style="font-family:宋体"}

[[InFragDrops]{lang="EN-US"}]{#struct_0_12181_84059_x1899398058}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1489932227}[分片报文，该分片报文由于错误被丢弃]{style="font-family:宋体"}

[[InFragTimeouts]{lang="EN-US"}]{#struct_0_12181_84059_x1969681564}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_205031567}[分片报文，该分片停留在系统缓冲中时间超过指定时间，被丢弃]{style="font-family:宋体"}

[[OutFragFails]{lang="EN-US"}]{#struct_0_12181_84059_x1489604547}

[[出接口上分片失败的报文]{style="font-family:宋体"}]{#struct_0_12181_84059_x1541274776}

[[InUnknownProtos]{lang="EN-US"}]{#struct_0_12181_84059_x1085367253}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1489539011}[报文，其协议类型不能被识别或不能被支持]{style="font-family:宋体"}

[[InDelivers]{lang="EN-US"}]{#struct_0_12181_84059_1667518404}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1356485040}[报文，该报文被上送到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的用户协议处（如]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[等）]{style="font-family:宋体"}

[[OutRequests]{lang="EN-US"}]{#struct_0_12181_84059_x1490128834}

[[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1555572559}[本地出报文，即各]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的用户协议层要求]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[发送出去的报文]{style="font-family:宋体"}

[[OutForwDatagrams]{lang="EN-US"}]{#struct_0_12181_84059_x378519183}

[[出接口上被转发的报文]{style="font-family:宋体"}]{#struct_0_12181_84059_x1490063298}

[[InNoRoutes]{lang="EN-US"}]{#struct_0_12181_84059_x1660997613}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1490259906}[报文，找不到匹配的路由被丢弃]{style="font-family:宋体"}

[[InTooBigErrors]{lang="EN-US"}]{#struct_0_12181_84059_417140287}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_116066753}[报文，转发时，由于超过链路]{style="font-family:宋体"}[MTU]{lang="EN-US"}[被丢弃]{style="font-family:宋体"}

[[OutFragOKs]{lang="EN-US"}]{#struct_0_12181_84059_x1490194370}

[[出接口上分片成功的报文]{style="font-family:宋体"}]{#struct_0_12181_84059_x2045864369}

[[OutFragCreates]{lang="EN-US"}]{#struct_0_12181_84059_1267195558}

[[出接口上成功分片后的分片报文，指分片数]{style="font-family:宋体"}]{#struct_0_12181_84059_x1489866690}

[[InMcastPkts]{lang="EN-US"}]{#struct_0_12181_84059_x1198683012}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1489801154}[组播报文]{style="font-family:宋体"}

[[InMcastNotMembers]{lang="EN-US"}]{#struct_0_12181_84059_x657551663}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1778613716}[组播报文，但该接口却没有加入对应组播组，报文被丢弃]{style="font-family:宋体"}

[[OutMcastPkts]{lang="EN-US"}]{#struct_0_12181_84059_x1489997762}

[[接口发送的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1100525148}[组播报文]{style="font-family:宋体"}

[[InAddrErrors]{lang="EN-US"}]{#struct_0_12181_84059_x1489932226}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x403597623}[报文，其目的地址不合法，报文被丢弃]{style="font-family:宋体"}

[[InDiscards]{lang="EN-US"}]{#struct_0_12181_84059_x1489604546}

[[接口接收到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1187608579}[报文，由于资源问题被丢弃的报文，而不是由于报文内容等被丢弃的报文]{style="font-family:宋体"}

[[OutDiscards]{lang="EN-US"}]{#struct_0_12181_84059_x1489539010}

[[接口需要发送的报文，由于资源问题被丢弃的报文，而不是由于报文内容等被丢弃的报文]{style="font-family:宋体"}]{#struct_0_12181_84059_x1061364951}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_702519093}[查看所有接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 interface brief]{lang="EN-US"}]{#struct_0_12181_84059_900471358}

[\*down: administratively down]{lang="EN-US"}

[(s): spoofing]{lang="EN-US"}

[Interface                                 Physical Protocol IPv6 Address ]{lang="EN-US"}

[Vlan-interface1                          down       down      Unassigned]{lang="EN-US"}

[Vlan-interface2                          up         up         2001::1]{lang="EN-US"}

[Vlan-interface100                        up         up        Unassigned]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ipv6 interface brief]{lang="EN-US"}]{#struct_0_12181_84059_x1490128837}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_901422741}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x1152288032}

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_1808560585}

[[\*down: administratively down]{lang="EN-US"}]{#struct_0_12181_84059_x1380768945}

[[接口处于管理]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_12181_84059_1874085680}[状态，即采用]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令关闭了该接口]{style="font-family:宋体"}

[[(s): spoofing]{lang="EN-US"}]{#struct_0_12181_84059_938906320}

[[接口的欺骗属性，即接口的链路协议状态显示是]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_12181_84059_1496326239}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_12181_84059_x1490063301}

[[接口的名称]{style="font-family:宋体"}]{#struct_0_12181_84059_x450685281}

[[Physical]{lang="EN-US"}]{#struct_0_12181_84059_x1257133108}

[[接口的物理状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_x147932191}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\*down]{lang="EN-US"}]{#struct_0_12181_84059_1058875526}[：表示该接口已经通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_12181_84059_x1900618492}[：该接口的管理状态为开启，但物理状态为关闭，即该接口对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内没有处于]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态的端口（可能因为没有连接好或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_12181_84059_x1490259909}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_12181_84059_x1599282348}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_589194190}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_12181_84059_x2010197497}[：该接口的协议状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_12181_84059_1007535415}[：该接口的协议状态为开启]{style="font-family:宋体"}

[[IPv6 Address]{lang="EN-US"}]{#struct_0_12181_84059_x1490194373}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x479780428}[地址，接口上有全球单播地址时，显示地址最小的全球单播地址，没有全球单播地址则显示链路本地地址，没有链路本地地址则显示"]{style="font-family:宋体"}[Unassigned]{lang="EN-US"}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1948902828 .myid}
[]{#_Toc404786992}[]{#struct_0_12181_84059_1022689956}[]{#_Toc296959540}[]{#_Toc90625828}[]{#_Toc90625830}[]{#_Toc90625832}[]{#_Toc90625833}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 interface prefix**

------------------------------------------------------------------------

[**[display ipv6 interface prefix]{lang="EN-US"}**]{#struct_0_12181_84059_x977711860}[命令用来显示接口的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[前缀信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_587042309}

[**[display ipv6 interface]{lang="EN-US"}**[ *interface-type interface-number* **prefix**]{lang="EN-US"}]{#struct_0_12181_84059_x1160275687}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1455195685}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1489866693}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x795398485}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_118915331}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x714734919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x514218710}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x425298221}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_925607308}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_12181_84059_1252451536}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1489801157}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_2071331692}[查看]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 interface Vlan-interface 10 prefix]{lang="EN-US"}]{#struct_0_12181_84059_x1489997765}

[Prefix: 1001::/65                                          Origin: ADDRESS]{lang="EN-US"}

[Age:    -                                                     Flag:   AL]{lang="EN-US"}

[Lifetime(Valid/Preferred): 2592000/604800]{lang="EN-US"}

[ ]{lang="EN-US"}

[Prefix: 2001::/64                                          Origin: STATIC]{lang="EN-US"}

[Age:    -                                                     Flag:   L]{lang="EN-US"}

[Lifetime(Valid/Preferred): 3000/2000]{lang="EN-US"}

[ ]{lang="EN-US"}

[Prefix: 3001::/64                                          Origin: RA]{lang="EN-US"}

[Age:    600                                                   Flag:   A]{lang="EN-US"}

[Lifetime(Valid/Preferred): -]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display ipv6 interface prefix]{lang="EN-US"}]{#struct_0_12181_84059_x1272127847}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_895066041}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x1585475839}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x892935261}

[[Prefix]{lang="EN-US"}]{#struct_0_12181_84059_x237861803}

[[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_716729980}[地址前缀]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_12181_84059_x430437945}

[[前缀来源，包括：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1489932229}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC]{lang="EN-US"}]{#struct_0_12181_84059_x1519342870}[：手工配置前缀（命令]{lang="EN-US" style="font-family:宋体"}**[ipv6 nd ra prefix]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1356159717}[：使能无状态地址自动配置功能后根据]{style="font-family:宋体"}[RA]{lang="EN-US"}[报文生成的前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADDRESS]{lang="EN-US"}]{#struct_0_12181_84059_28620032}[：由手工配置的地址产生的前缀]{lang="EN-US" style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_12181_84059_x1532845697}

[[老化时间（单位为秒），"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_12181_84059_x2017501953}["表示前缀不会老化]{style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_12181_84059_x1489604549}

[[前缀随]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1090936082}[报文公告时携带的标记，"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示没有标记]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_12181_84059_x1172789846}[：表示前缀是直接可达的。没有此标记，则表示前缀不是该链路上直连可达的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_12181_84059_2000920405}[：表示前缀用于无状态自动配置。没有此标记，则表示前缀不用于无状态自动配置]{style="font-family:宋体"}

[[Lifetime]{lang="EN-US"}]{#struct_0_12181_84059_x1314253280}

[[前缀随]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1489539013}[报文公告时携带的生存时间（单位为秒），"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示前缀不需要公告]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_12181_84059_x1464649478}[：前缀的有效生命期]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Preferred]{lang="EN-US"}]{#struct_0_12181_84059_x805980790}[：前缀的首选生命期]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_95220176}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd ra prefix]{lang="EN-US"}**]{#struct_0_12181_84059_206221424}

::: {#1717628836 .myid}
[]{#_Toc404786993}[]{#struct_0_12181_84059_x1182060765}[]{#_Toc402456133}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 nd snooping**

------------------------------------------------------------------------

[**[display ipv6 nd snooping]{lang="EN-US"}**]{#struct_0_12181_84059_x820314750}[命令用来显示]{style="font-family:
宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1459933552}

[**[display ipv6 nd snooping ]{lang="EN-US"}**[\[ \[ \[ **vlan** *vlan-id \|* **interface** *interface-type interface-number* \] \[ **global** \| **link-local** \] \] **\|** *ipv6-address* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_12181_84059_384023176}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x988106837}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_2093231516}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_55433040}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1493590316}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_1339119627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x452704969}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1339678658}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x275748374}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_12181_84059_x1632399459}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_12181_84059_1619186277}[：显示指定接口的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号]{style="font-family:宋体"}

[*[ipv6-address ]{lang="EN-US"}*]{#struct_0_12181_84059_x257888704}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[global]{lang="EN-US"}**]{#struct_0_12181_84059_x1508010011}[：显示表项地址类型为全球单播地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项]{style="font-family:宋体"}

[**[link-local]{lang="EN-US"}**]{#struct_0_12181_84059_x1491308728}[：显示表项地址类型为链路本地地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_12181_84059_135599775}**[：]{style="font-family:宋体"}**[显示]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的详细信息]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1975651406}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1764302499}[显示]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 nd snooping vlan 1]{lang="EN-US"}]{#struct_0_12181_84059_x66315518}

[IPv6 address              MAC address     VID  Interface     Status       Age]{lang="EN-US"}

[1::2                       0000-1234-0c01  1    GE1/0/2        VALID        57]{lang="EN-US"}

[\<Sysname\> display ipv6 nd snooping vlan 1 verbose]{lang="EN-US"}

[IPv6 address: 1::2]{lang="EN-US"}

[MAC address: 0000-1234-0c01]{lang="EN-US"}

[Interface: GE0/0/2]{lang="EN-US"}

[First VLAN ID: 1   Second VLAN ID: N/A]{lang="EN-US"}

[Status: VALID   Age: 57]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display ipv6 nd snooping]{lang="EN-US"}]{#struct_0_12181_84059_1954637759}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x62956838}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_1820587149}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x705839458}

[[IPv6 address]{lang="EN-US"}]{#struct_0_12181_84059_x319222955}

[[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_x1988564283}[表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_12181_84059_x222363453}

[[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_x1875222835}[表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VID]{lang="EN-US"}]{#struct_0_12181_84059_x422480342}

[[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_1851785564}[表项所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[First VLAN ID]{lang="EN-US"}]{#struct_0_12181_84059_1923014063}

[[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_x1813814918}[表项所属外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[Second VLAN ID]{lang="EN-US"}]{#struct_0_12181_84059_1143603599}

[[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_x276443392}[表项所属内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，当不存在内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息时，则显示]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的描述，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[QinQ]{lang="EN-US"}["]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_12181_84059_1718515489}

[[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_348086874}[表项所对应的入端口]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_12181_84059_x1585279756}

[[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_1048681623}[表项的显示的状态，选项如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TENTATIVE]{lang="EN-US"}]{#struct_0_12181_84059_1855698989}[：临时非生效状态；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VALID]{lang="EN-US"}]{#struct_0_12181_84059_x1479685713}[：生效状态]{lang="EN-US" style="font-family:宋体"}[；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TESTING_TPLT]{lang="EN-US"}]{#struct_0_12181_84059_x19195815}[：从信任端口收到对应源地址的报文，或者表项到达老化，触发向该表项所在端口进行探测；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TESTING_VP]{lang="EN-US"}]{#struct_0_12181_84059_1178108335}[：从其他非信任端口收到对应源地址的报文，触发向该表项所在接口进行探测；]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_12181_84059_x1591373809}

[[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_1546888126}[表项的老化时间，单位为秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#231613114 .myid}
[]{#_Toc404786994}[]{#struct_0_12181_84059_1868883879}[]{#_Toc402456134}[]{#_Toc397517881}[]{#_Toc395012445}[]{#_Toc389730691}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 nd snooping count**

------------------------------------------------------------------------

[**[display ipv6 nd snooping count]{lang="EN-US"}**]{#struct_0_12181_84059_1647227034}[命令用来显示]{style="font-family:
宋体"}[ND Snooping]{lang="EN-US"}[表项的数目。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x706413297}

[**[display ipv6 nd snooping count ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_12181_84059_1562016975}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1623847052}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_369885450}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x396746450}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1404702587}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_1644706379}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1181995229}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x2142901293}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1674195439}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_12181_84059_362582713}[：显示指定接口的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项数目。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x707807911}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x808628297}[显示设备上的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项数目。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 nd snooping count  ]{lang="EN-US"}]{#struct_0_12181_84059_1321309827}

[Total number of entries: 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1159941496}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项数目。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 nd snooping count interface gigabit 1/0/1]{lang="EN-US"}]{#struct_0_12181_84059_x1333088424}

[Total number of entries on interface: 2]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display ipv6 nd snooping count]{lang="EN-US"}]{#struct_0_12181_84059_1569620459}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x42956100}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_384088712}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_984937187}

[[Total number of entries]{lang="EN-US"}]{#struct_0_12181_84059_1526388379}

[[设备的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_x1761486629}[表项数目]{style="font-family:宋体"}

[[Total number of entries on interface: *number*]{lang="EN-US"}]{#struct_0_12181_84059_x1632333923}

[[接口下的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_x2115136480}[表项数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-598491539 .myid}
[]{#_Toc404786995}[]{#struct_0_12181_84059_x1413588443}[]{#_Toc389844695}[]{#_Toc375570476}[]{#_Toc373844271}[]{#_Toc373593095}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 nd suppression xconnect-group**

------------------------------------------------------------------------

[**[display ipv6 nd suppression xconnect-group]{lang="EN-US"}**]{#struct_0_12181_84059_903096885}[命令用来显示]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x713041687}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1413391835}

[**[display]{lang="EN-US"}**[ **ipv6 nd** **suppression xconnect-group** \[ **name** *group-name* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12181_84059_x686498336}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_436051988}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **ipv6 nd** **suppression xconnect-group** \[ **name** *group-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12181_84059_x906948953}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_1702467228}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **ipv6 nd** **suppression xconnect-group** \[ **name** *group-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_12181_84059_x956399304}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1650795109}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1327095208}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_405919247}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_433530484}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1413457371}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_367804171}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x646989846}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_797059873}

[**[name]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_12181_84059_1050899977}[：交叉连接组的名称，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不能包含字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["，区分大小写。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12181_84059_x1388882869}[：当前]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制]{style="font-family:宋体"}[表项的数目。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_161794523}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则表示所有单板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_1137533391}[：显示指定成员设备的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_x1525760702}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1859553564}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_492404178}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_12181_84059_172672663}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1413916126}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1911368816}[显示所有交叉连接组下的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 nd suppression xconnect-group]{lang="EN-US"}]{#struct_0_12181_84059_1022451075}

[IPv6 address            MAC address     Xconnect-group   Connection       Aging  ]{lang="EN-US"}

[2001::1                 000c-29fe-5a8f  vpna                svc               25     ]{lang="EN-US"}

[2001::2                 000c-29fe-5aa3  vpna                svc               2       ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x2136430604}[显示当前]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的计数。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 nd suppression xconnect-group count]{lang="EN-US"}]{#struct_0_12181_84059_1411680429}

[Total entries: 2]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display ipv6 nd suppression xconnect-group]{lang="EN-US"}]{#struct_0_12181_84059_468190433}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_160266324}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x1564265580}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x1413981662}

[[IPv6 address]{lang="EN-US"}]{#struct_0_12181_84059_x1608212782}

[[ND]{lang="EN-US"}]{#struct_0_12181_84059_1581703975}[泛洪抑制表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_12181_84059_x1413785054}

[[ND]{lang="EN-US"}]{#struct_0_12181_84059_102402050}[泛洪抑制表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Xconnect-group]{lang="EN-US"}]{#struct_0_12181_84059_x1491323936}

[[ND]{lang="EN-US"}]{#struct_0_12181_84059_x1413850590}[泛洪抑制表项的]{style="font-family:宋体"}[Xconnect-group]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Connection]{lang="EN-US"}]{#struct_0_12181_84059_1524484722}

[[ND]{lang="EN-US"}]{#struct_0_12181_84059_x415801103}[泛洪抑制表项的]{style="font-family:宋体"}[Connection]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_12181_84059_x1413653982}

[[ND]{lang="EN-US"}]{#struct_0_12181_84059_239657280}[泛洪抑制表项的老化时间，单位为分钟]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1373114161 .myid}
[]{#_Toc404786996}[]{#struct_0_12181_84059_1582307697}[]{#_Toc279579806}[]{#_Toc138417073}[]{#_Toc137020654}[]{#_Toc59352302}[]{#_Toc52166669}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 neighbors**

------------------------------------------------------------------------

[**[display ipv6 neighbors]{lang="EN-US"}**]{#struct_0_12181_84059_995349852}[命令用来显示邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1490128836}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_1576595323}

[**[display ipv6 neighbors]{lang="EN-US"}**[ { *ipv6-address \|* **all** *\|* **dynamic** \| **interface** *interface-type interface-number* \| **static** \| **vlan** *vlan-id* } \[ **verbose** \]]{lang="EN-US"}]{#struct_0_12181_84059_x1779133898}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x456338885}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 neighbors]{lang="EN-US"}**[ { { *ipv6-address \|* **all** *\|* **dynamic** \| **static** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \| **interface** *interface-type interface-number* \| **vlan** *vlan-id* } \[ **verbose** \]]{lang="EN-US"}]{#struct_0_12181_84059_x467953912}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x1296400517}[模式：]{style="font-family:宋体"}

[**[display ipv6 neighbors]{lang="EN-US"}**[ { { *ipv6-address \|* **all** *\|* **dynamic** \| **static** } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \| **interface** *interface-type interface-number* \| **vlan** *vlan-id* } \[ **verbose** \]]{lang="EN-US"}]{#struct_0_12181_84059_361004369}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x407920934}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x57478714}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1490063300}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x2016769222}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x457849453}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1633148091}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x146508379}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1734756854}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12181_84059_1985888157}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的邻居信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_12181_84059_936628629}[：显示所有邻居的信息，包括公网和所有私网下动态获取的和静态配置的邻居信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_12181_84059_x1386271425}[：显示所有动态获取的邻居信息。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_12181_84059_x1490259908}[：显示所有静态配置的邻居信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_x33198407}[：显示指定]{style="font-family:宋体"}[单板的邻居信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未配置本参数，则显示所有单板上的邻居信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_x1438379897}[：显示指定]{style="font-family:宋体"}[成员设备的邻居信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的邻居信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_443607766}[：显示指定]{style="font-family:宋体"}[成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的邻居信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_543835849}[：显示指定成员设备上指定单板的邻居信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的邻居信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1747279295}[：显示指定单板的邻居信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的邻居信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_x1320030525}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_12181_84059_1191356683}[：显示指定接口的邻居信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_12181_84059_357515774}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_12181_84059_307065704}[：显示邻居的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_661418962}

[[用户可以通过]{style="font-family:宋体"}**[reset ipv6 neighbors]{lang="EN-US"}**]{#struct_0_12181_84059_x1490194372}[命令清除指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1086303513}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1108606213}[查看所有的邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 neighbors all]{lang="EN-US"}]{#struct_0_12181_84059_2065249049}

[         Type: S-Static    D-Dynamic    O-Openflow    R-Rule    I-Invalid]{lang="EN-US"}

[IPv6 Address                   Link Layer     VID  Interface      State T  Age]{lang="EN-US"}

[FE80::200:5EFF:FE32:B800    0000-5e32-b800 N/A  GE1/0/1        REACH D  10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x2003364152}[查看所有邻居的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 neighbors all verbose]{lang="EN-US"}]{#struct_0_12181_84059_x1221409549}

[          Type: S-Static    D-Dynamic    O-Openflow    R-Rule    I-Invalid]{lang="EN-US"}

[IPv6 Address: FE80::200:5EFF:FE32:B800]{lang="EN-US"}

[Link layer  : ]{lang="EN-US"}[0000-5e32-b800]{lang="PT-BR"}[      VID : N/A  Interface: ]{lang="EN-US"}[GE1/0/1]{lang="PT-BR"}

[State        : REACH                 Type: IS   Age      : -]{lang="EN-US"}

[Vpn-instance: vpn1]{lang="EN-US"}

[NickName    : 0x0001]{lang="EN-US"}

[]{#struct_0_12181_84059_x1489866692}[]{#_Ref197144306}[]{#_Toc138417053}[[表1-11 ]{lang="EN-US"}[display ipv6 neighbors]{lang="EN-US"}]{#_Toc94583060}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_897093805}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_1933484870}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x2023996888}

[[IPv6 Address]{lang="EN-US"}]{#struct_0_12181_84059_1404987381}

[[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1234010268}[地址]{style="font-family:宋体"}

[[Link Layer]{lang="EN-US"}]{#struct_0_12181_84059_484119841}

[[邻居的链路层地址（]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_12181_84059_x216476855}[地址）]{style="font-family:宋体"}

[[VID]{lang="EN-US"}]{#struct_0_12181_84059_x1489801156}

[[与邻居相连的接口所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_505247751}

[[Interface]{lang="EN-US"}]{#struct_0_12181_84059_99345491}

[[与邻居相连的接口]{style="font-family:宋体"}]{#struct_0_12181_84059_583874176}

[[State]{lang="EN-US"}]{#struct_0_12181_84059_830312481}

[[邻居的状态，包括：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1489997764}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INCMP]{lang="EN-US"}]{#struct_0_12181_84059_293956094}[：正在解析地址，邻居的链路层地址尚未确定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REACH]{lang="EN-US"}]{#struct_0_12181_84059_2136803521}[：邻居可达]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STALE]{lang="EN-US"}]{#struct_0_12181_84059_x1687913425}[：未确定邻居是否可达，设备不会再验证邻居的可达性，除非有数据发送给该邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DELAY]{lang="EN-US"}]{#struct_0_12181_84059_x336749634}[：未确定邻居是否可达，延迟一段时间发送邻居请求报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROBE]{lang="EN-US"}]{#struct_0_12181_84059_x1489932228}[：未确定邻居是否可达，发送邻居请求报文来验证邻居的可达性]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12181_84059_46741071}

[[邻居信息的类型，]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12181_84059_x1165136979}[表示静态配置，]{style="font-family:宋体"}[D]{lang="EN-US"}[表示动态获取，]{style="font-family:宋体"}[O]{lang="EN-US"}[表示从]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[特性获取，]{style="font-family:宋体"}[R]{lang="EN-US"}[表示从]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[或]{style="font-family:宋体"}[Portal]{lang="EN-US"}[等特性获取，]{style="font-family:宋体"}[I]{lang="EN-US"}[表示无效]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_12181_84059_128533493}

[[静态项显示"]{style="font-family:宋体"}[--]{lang="EN-US"}]{#struct_0_12181_84059_1646545412}["，动态项显示上次可达以来经过的时间（单位为秒），如果始终不可达则显示"]{style="font-family:宋体"}[\#]{lang="EN-US"}["（只适用于动态项）]{style="font-family:宋体"}

[[Vpn-instance]{lang="EN-US"}]{#struct_0_12181_84059_x1489604548}

[[VPN]{lang="EN-US"}]{#struct_0_12181_84059_1637947273}[实例名称，]{style="font-family:宋体"}[\[No Vrf\]]{lang="EN-US"}[表示没有配置相应表项的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[NickName]{lang="EN-US"}]{#struct_0_12181_84059_x737771419}

[[邻居表项的]{style="font-family:宋体"}[NickName]{lang="EN-US"}]{#struct_0_12181_84059_x2085851623}[（长度为]{style="font-family:宋体"}[4]{lang="EN-US"}[的十六进制数字，例如]{style="font-family:宋体"}[0x012a]{lang="EN-US"}[），关于]{style="font-family:宋体"}[NickName]{lang="EN-US"}[的详细介绍，请参见"]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[TRILL]{lang="EN-US"}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1664988711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 neighbor]{lang="EN-US"}**]{#struct_0_12181_84059_1056026059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 neighbors]{lang="EN-US"}**]{#struct_0_12181_84059_1798859122}

::: {#302148503 .myid}
[]{#_Toc404786997}[]{#struct_0_12181_84059_x978305485}[]{#_Toc279579807}[]{#_Toc138417074}[]{#_Toc137020655}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 neighbors count**

------------------------------------------------------------------------

[**[display ipv6 neighbors count]{lang="EN-US"}**]{#struct_0_12181_84059_430989303}[命令用来显示邻居表项的个数。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1464035101}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1489539012}

[**[display ipv6 neighbors]{lang="EN-US"}**[ { **all** *\|* **dynamic** \| **interface** *interface-type interface-number* \| **static** \| **vlan** *vlan-id* } **count**]{lang="EN-US"}]{#struct_0_12181_84059_101434463}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x304752713}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 neighbors]{lang="EN-US"}**[ { { **all** *\|* **dynamic** \| **static** } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \| **interface** *interface-type interface-number* \| **vlan** *vlan-id* } **count**]{lang="EN-US"}]{#struct_0_12181_84059_1197869136}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x737395149}[模式：]{style="font-family:宋体"}

[**[display ipv6 neighbors]{lang="EN-US"}**[ { { **all** *\|* **dynamic** \| **static** } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \| **interface** *interface-type interface-number* \| **vlan** *vlan-id* } **count**]{lang="EN-US"}]{#struct_0_12181_84059_x1662280890}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_2041118414}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x736830517}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x560471273}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_75955108}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1609545689}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1528966771}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1981347372}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1117796184}

[**[all]{lang="EN-US"}**]{#struct_0_12181_84059_x403754109}[：显示所有邻居表项的总个数，包括动态获取的和静态配置的邻居信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_12181_84059_213959665}[：显示所有动态获取的邻居表项的总个数。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_12181_84059_884088714}[：显示所有静态配置的邻居表项的总个数。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_984946532}[：显示指定]{style="font-family:宋体"}[单板的邻居表项的总个数。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的邻居表项的总个数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_76020644}[：显示指定]{style="font-family:宋体"}[成员设备的邻居表项的总个数。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的邻居表项的总个数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_40257703}[：显示指定]{style="font-family:宋体"}[成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的邻居表项的总个数。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的邻居表项的总个数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_868214227}[：显示指定成员设备上指定单板的邻居表项的总个数。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的邻居表项的总个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1867308155}[：显示指定单板的邻居表项的总个数。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的邻居表项的总个数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_x1320096062}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的邻居表项的总个数。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_12181_84059_1073391594}[：显示指定接口的邻居表项的总个数。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_12181_84059_935837832}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的邻居表项的总个数。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x740628458}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_2134619756}[显示动态获取的邻居表项的总个数。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 neighbors dynamic count]{lang="EN-US"}]{#struct_0_12181_84059_1144338718}

[ Total number of dynamic entries: 2]{lang="EN-US"}
:::

::::: {#219172819 .myid}
[]{#_Toc138417075}[]{#_Toc137020656}[]{#_Toc404786998}[]{#struct_0_12181_84059_75824036}[]{#_Toc279579808}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 neighbors vpn-instance**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12181_84059_x1252134320}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_12181_84059_x193241104}
:::

**[ ]{lang="EN-US"}**

[**[display ipv6 neighbors vpn-instance]{lang="EN-US"}**]{#struct_0_12181_84059_x921718552}[命令用来显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1791927888}

[**[display ipv6 neighbors vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **count** \]]{lang="EN-US"}]{#struct_0_12181_84059_359517224}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x930715951}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_813603756}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_280416469}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_75889572}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x2087664439}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_859365093}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_4616720}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_560395466}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_12181_84059_x1501240248}[：指定]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12181_84059_x828552959}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中的邻居表项的总数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1803217524}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_76217252}[显示名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中的邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 neighbors vpn-instance vpn1]{lang="EN-US"}]{#struct_0_12181_84059_326550919}

[         Type: S-Static    D-Dynamic    O-Openflow    I-Invalid]{lang="EN-US"}

[IPv6 Address                   Link Layer      VID  Interface      State T  Age]{lang="EN-US"}

[FE80::200:5EFF:FE32:B800    0000-5e32-b800  N/A  GE1/0/1        REACH IS -]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display ipv6 neighbors vpn-instance]{lang="EN-US"}]{#struct_0_12181_84059_x184738965}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_889570105}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x1509187533}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x673756583}

[[IPv6 Address]{lang="EN-US"}]{#struct_0_12181_84059_x1838891445}

[[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1291411789}[地址]{style="font-family:宋体"}

[[Link-layer]{lang="EN-US"}]{#struct_0_12181_84059_76282788}

[[邻居的链路层地址（]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_12181_84059_2044250163}[地址）]{style="font-family:宋体"}

[[VID]{lang="EN-US"}]{#struct_0_12181_84059_1753626381}

[[与邻居相连的接口所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_x1311020748}

[[Interface]{lang="EN-US"}]{#struct_0_12181_84059_x1562566534}

[[与邻居相连的接口]{style="font-family:宋体"}]{#struct_0_12181_84059_x581093824}

[[State]{lang="EN-US"}]{#struct_0_12181_84059_76086180}

[[邻居的状态，包括：]{style="font-family:宋体"}]{#struct_0_12181_84059_796833849}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INCMP]{lang="EN-US"}]{#struct_0_12181_84059_x820931306}[：正在解析地址，邻居的链路层地址尚未确定；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REACH]{lang="EN-US"}]{#struct_0_12181_84059_60061272}[：邻居可达；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STALE]{lang="EN-US"}]{#struct_0_12181_84059_x165646056}[：未确定邻居是否可达，设备不会再验证邻居的可达性，除非有数据发送给该邻居；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DELAY]{lang="EN-US"}]{#struct_0_12181_84059_76151716}[：未确定邻居是否可达，延迟一段时间发送邻居请求报文；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROBE]{lang="EN-US"}]{#struct_0_12181_84059_81231880}[：未确定邻居是否可达，发送邻居请求报文来验证邻居的可达性。]{style="font-family:宋体"}

[[T]{lang="EN-US"}]{#struct_0_12181_84059_170904003}

[[邻居信息的类型，]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12181_84059_990192620}[表示静态配置，]{style="font-family:宋体"}[D]{lang="EN-US"}[表示动态获取，]{style="font-family:宋体"}[O]{lang="EN-US"}[表示通过]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[特性获取，]{style="font-family:宋体"}[I]{lang="EN-US"}[表示无效]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_12181_84059_2076847121}

[[静态项显示"]{style="font-family:宋体"}[--]{lang="EN-US"}]{#struct_0_12181_84059_76479396}["，动态项显示上次可达以来经过的时间（单位为秒），如果始终不可达则显示"]{style="font-family:宋体"}[\#]{lang="EN-US"}["（只适用于动态项）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1661984333 .myid}
[]{#_Toc279391292}[]{#_Toc249245000}[]{#_Toc404786999}[]{#struct_0_12181_84059_2000112847}[]{#_Toc298765618}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 pathmtu**

------------------------------------------------------------------------

[**[display ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_1055272398}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1620165612}

[**[display ipv6 pathmtu]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { *ipv6-address \|* { **all** \| **dynamic** \| **static** } \[ **count** \] }]{lang="EN-US"}]{#struct_0_12181_84059_x1623679737}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1347947671}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1959523660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1528072922}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_820714775}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_76544932}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_334476985}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_629888239}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1049514739}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12181_84059_321220806}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的]{style="font-family:宋体"}[IPv6 PMTU]{lang="EN-US"}[信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12181_84059_1236640055}[：显示到达指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_12181_84059_1127814356}[：]{style="font-family:宋体"}[显示所有公网的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_12181_84059_x207789969}[：显示所有动态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_12181_84059_75955109}[：显示所有静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_12181_84059_346769447}[：显示]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1452088829}

[[通过本]{style="font-family:宋体"}]{#struct_0_12181_84059_x1021130261}[命令可以查看]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息，包括]{style="font-family:宋体"}[动态创建的]{style="font-family:宋体"}[PMTU]{lang="PT-BR"}[信息和]{style="font-family:宋体"}[静态配置的]{style="font-family:宋体"}[PMTU]{lang="PT-BR"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1284780398}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_46167818}[显示所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pathmtu all]{lang="EN-US"}]{#struct_0_12181_84059_1182629935}

[IPv6 destination address                PathMTU   Age   Type]{lang="EN-US"}

[1:2::3:2                                   1800       -      Static]{lang="EN-US"}

[1:2::4:2                                   1400       10     Dynamic]{lang="EN-US"}

[1:2::5:2                                   1280       10     Dynamic]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_957892336}[显示所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项数目。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pathmtu all count]{lang="EN-US"}]{#struct_0_12181_84059_76020645}

[Total number of entries: 3]{lang="EN-US"}

[]{#struct_0_12181_84059_x1088100909}[[表1-13 ]{lang="EN-US"}[display ipv6 pathmtu]{lang="EN-US"}]{#_Toc94583061}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_919660593}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_537251675}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_971235343}

[[IPv6 destination address]{lang="EN-US"}]{#struct_0_12181_84059_12961147}

[[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_930683741}[目的地址]{style="font-family:宋体"}

[[PathMTU]{lang="EN-US"}]{#struct_0_12181_84059_75824037}

[[对应]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1086517840}[地址的]{style="font-family:宋体"}[PMTU]{lang="PT-BR"}[值]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_12181_84059_877450396}

[[PMTU]{lang="EN-US"}]{#struct_0_12181_84059_x950811933}[老化时间（单位为分钟），如果是静态表项则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12181_84059_x1437958541}

[[PMTU]{lang="EN-US"}]{#struct_0_12181_84059_1269645193}[类型，]{style="font-family:宋体"}[Dynamic]{lang="EN-US"}[表示动态协商的]{style="font-family:宋体"}[PMTU]{lang="PT-BR"}[，]{style="font-family:宋体"}[Static]{lang="EN-US"}[表示静态配置的]{style="font-family:宋体"}[PMTU]{lang="PT-BR"}

[[Total number of entries]{lang="EN-US"}]{#struct_0_12181_84059_75889573}

[[PMTU]{lang="EN-US"}]{#struct_0_12181_84059_250987721}[表项数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1131443152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_1431865645}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_x162607856}

::: {#231669364 .myid}
[]{#_Toc404787000}[]{#struct_0_12181_84059_x868679701}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 prefix**

------------------------------------------------------------------------

[**[display ipv6 prefix]{lang="EN-US"}**]{#struct_0_12181_84059_x230690487}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀信息，包括静态和动态前缀。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x868483093}

[**[display ipv6 prefix]{lang="EN-US"}**[ \[ *prefix-number* \]]{lang="EN-US"}]{#struct_0_12181_84059_118259484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1454552777}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x868548629}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1005945781}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_998984136}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x867827733}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x877243898}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x867893269}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x72056937}

[*[prefix-number]{lang="EN-US"}*]{#struct_0_12181_84059_x868352024}[：显示指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀信息。]{style="font-family:宋体"}*[prefix-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。如果不指定本参数，则显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1665206811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态]{style="font-family:宋体"}]{#struct_0_12181_84059_1457917872}[IPv6]{lang="EN-US"}[前缀指的是通过]{style="font-family:宋体"}[ipv6 prefix]{lang="EN-US"}[命令创建的前缀。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[动态]{style="font-family:宋体"}]{#struct_0_12181_84059_x868417560}[IPv6]{lang="EN-US"}[前缀指的是设备作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端获取到前缀后，自动创建的指定编号的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。详细介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[业务命令参考]{style="font-family:宋体"}[/DHCPv6]{lang="EN-US"}["中的命令]{style="font-family:宋体"}**[ipv6 dhcp client pd]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x287878777}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x868220952}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 prefix]{lang="EN-US"}]{#struct_0_12181_84059_73277597}

[Number  Prefix                                     Type]{lang="EN-US"}

[1        1::/16                                     Static]{lang="EN-US"}

[2        11:77::/32                                Dynamic]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x53920565}[显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号]{style="font-family:宋体"}[1]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 prefix 1]{lang="EN-US"}]{#struct_0_12181_84059_x868286488}

[Number: 1]{lang="EN-US"}

[Type  : Dynamic]{lang="EN-US"}

[Prefix: ABCD:77D8::/32]{lang="EN-US"}

[Preferred lifetime 90 sec, valid lifetime 120 sec]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display ipv6 prefix]{lang="EN-US"}]{#struct_0_12181_84059_x868614168}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x111753080}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_880604148}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x868679704}

[[Number]{lang="EN-US"}]{#struct_0_12181_84059_x231018167}

[[前缀编号]{style="font-family:宋体"}]{#struct_0_12181_84059_x868483096}

[[Type]{lang="EN-US"}]{#struct_0_12181_84059_118587164}

[[前缀的类型，取值包括：]{style="font-family:宋体"}]{#struct_0_12181_84059_x868548632}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_12181_84059_x867827736}[：表示静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="EN-US"}]{#struct_0_12181_84059_x876916218}[：表示动态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀]{style="font-family:宋体"}

[[Prefix]{lang="EN-US"}]{#struct_0_12181_84059_x867893272}

[[前缀及其长度。"]{style="font-family:宋体"}[Not-available]{lang="EN-US"}]{#struct_0_12181_84059_x71467114}["表示目前尚未获取到前缀]{style="font-family:宋体"}

[[Preferred lifetime 90 sec]{lang="EN-US"}]{#struct_0_12181_84059_x868352023}

[[首选生命期，单位为秒。如果是静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x868417559}[前缀，则不显示]{style="font-family:宋体"}

[[valid lifetime 120 sec]{lang="EN-US"}]{#struct_0_12181_84059_x287288956}

[[有效生命期，单位为秒。如果是静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x868220951}[前缀，则不显示]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_73080989}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 prefix]{lang="EN-US"}**]{#struct_0_12181_84059_x868286487}

::: {#2016354585 .myid}
[]{#_Toc404787001}[]{#struct_0_12181_84059_x941338170}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 rawip**

------------------------------------------------------------------------

[**[display ipv6 rawip]{lang="EN-US"}**]{#struct_0_12181_84059_x2016496180}[命令用来显示]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_76217253}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_x2012101241}

[**[display ipv6 rawip]{lang="EN-US"}**]{#struct_0_12181_84059_1486694740}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x271365736}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 rawip]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_1718771698}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_1923256367}[模式：]{style="font-family:宋体"}

[**[display ipv6 rawip]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_916146926}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1929330865}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1115737087}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_76282789}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_87935027}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_823615614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1991948911}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_1113990771}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x379517951}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1688226156}[：显示指定单板的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x2102566674}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1202991581}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_76086181}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x431777946}[：显示指定单板的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_246053420}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1159481287}

[[本命令可以用来查看]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}]{#struct_0_12181_84059_99167175}[连接摘要信息，包括本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址、使用]{style="font-family:宋体"}[IPv6 RawIP socket]{lang="EN-US"}[的协议号等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1589548310}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1022207250}[显示]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 rawip]{lang="EN-US"}]{#struct_0_12181_84059_1388429194}

[Local Addr            Foreign Addr        Protocol Chassis Slot  CPU PCB]{lang="EN-US"}

[2001:2002:2003:2     3001:3002:3003:3   58        1         1     0    0x0000000000000009]{lang="EN-US"}

[004:2005:2006:20     004:3005:3006:30]{lang="EN-US"}

[07:2008                07:3008]{lang="EN-US"}

[2002::100             2002::138            58        1         2     0    x0000000000000008]{lang="EN-US"}

[::                     ::                     58        1         5     0    0x0000000000000002]{lang="EN-US"}

[[[表1-15 ]{lang="EN-US"}]{.FigureDescriptionChar}[display ipv6 rawip]{lang="EN-US"}]{#struct_0_12181_84059_x825538888}[[命令显示信息描述表]{style="font-family:黑体"}]{.FigureDescriptionChar}

[]{#table_struct_0_921859769}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_76151717}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_2037547016}

[[Local Addr]{lang="EN-US"}]{#struct_0_12181_84059_x1837192469}

[[本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x176760784}[地址]{style="font-family:宋体"}

[[Foreign Addr]{lang="EN-US"}]{#struct_0_12181_84059_x308280662}

[[对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x660737862}[地址]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_12181_84059_76479397}

[[使用]{style="font-family:宋体"}[IPv6 RawIP socket]{lang="EN-US"}]{#struct_0_12181_84059_x338539313}[的协议号]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_12181_84059_1098126002}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_1577796036}[中的成员编号]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_175370308}

[[单板所在的槽位]{style="font-family:宋体"}]{#struct_0_12181_84059_1007797990}[号]{style="font-family:宋体"}

[[CPU]{lang="EN-US"}]{#struct_0_12181_84059_245135916}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_12181_84059_245725739}[编号]{style="font-family:宋体"}

[[PCB]{lang="EN-US"}]{#struct_0_12181_84059_76544933}

[[协议控制块索引]{style="font-family:宋体"}]{#struct_0_12181_84059_x1621838151}

[ ]{lang="EN-US"}

::: {#1997233542 .myid}
[]{#_Toc404787002}[]{#struct_0_12181_84059_x400130689}[]{#_Toc279391293}[]{#_Toc249245001}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 rawip verbose**

------------------------------------------------------------------------

[**[display ipv6 rawip verbose]{lang="EN-US"}**]{#struct_0_12181_84059_x1983713065}[命令用来显示]{style="font-family:
宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1978290253}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_1632417737}

[**[display ipv6 rawip verbose]{lang="EN-US"}**[ \[ **pcb** *pcb-index* \]]{lang="EN-US"}]{#struct_0_12181_84059_x1621969208}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_75955106}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 rawip verbose]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_1066813479}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x230182758}[模式：]{style="font-family:宋体"}

[**[display ipv6 rawip verbose]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_x1623864509}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x741153640}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_206740523}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_568954585}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1765387740}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_37127215}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_76020642}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_2015225299}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_2052216380}

[**[pcb]{lang="EN-US"}**[ *pcb-index*]{lang="EN-US"}]{#struct_0_12181_84059_x307798860}[：显示指定协议控制块索引的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[pcb-index]{lang="EN-US"}*[表示协议控制块索引，取值范围请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1741580709}[：显示指定单板的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x2082231197}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1122607247}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1179695078}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x682795133}[：显示指定单板的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_245987883}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1147917811}

[[本命令可以用来查看]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}]{#struct_0_12181_84059_75824034}[连接详细信息，包括]{style="font-family:宋体"}[socket]{lang="EN-US"}[的创建者、状态、选项、类型、使用的协议号等，以及]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1634471344}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_39029093}[显示]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 rawip verbose]{lang="EN-US"}]{#struct_0_12181_84059_38963557}

[Total RawIP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Creator: ping ipv6\[320\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 3]{lang="EN-US"}

[ Protocol: 58]{lang="EN-US"}

[ Connection info: src = ::, dst = ::]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[\# ]{lang="SV"}]{#struct_0_12181_84059_x1778932098}[显示]{style="font-family:宋体"}[Ipv6 RawIP]{lang="SV"}[连接详细信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 rawip verbose]{lang="EN-US"}]{#struct_0_12181_84059_38635877}

[Total RawIP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Slot: 6 Cpu: 0]{lang="EN-US"}

[ Creator: ping ipv6\[320\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 3]{lang="EN-US"}

[ Protocol: 58]{lang="EN-US"}

[ Connection info: src = ::, dst = ::]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_675244127}[显示]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 rawip verbose]{lang="EN-US"}]{#struct_0_12181_84059_75889570}

[Total RawIP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Chassis: 2 Slot: 6 Cpu: 0]{lang="EN-US"}

[ Creator: ping ipv6\[320\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 3]{lang="EN-US"}

[ Protocol: 58]{lang="EN-US"}

[ Connection info: src = ::, dst = ::]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display ipv6 rawip verbose]{lang="EN-US"}]{#struct_0_12181_84059_x1705327415}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_915813093}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x1691974310}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_1786942830}

[[Total RawIP socket number]{lang="EN-US"}]{#struct_0_12181_84059_x526676715}

[[IPv6 RawIP socket]{lang="EN-US"}]{#struct_0_12181_84059_1809979492}[总数]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_12181_84059_156253247}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_76217250}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_x55786105}

[[单板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1433108882}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_38766949}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_38701413}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Cpu]{lang="EN-US"}]{#struct_0_12181_84059_246053419}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_12181_84059_245201451}[编号]{style="font-family:宋体"}

[[Creator]{lang="EN-US"}]{#struct_0_12181_84059_741713116}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_1282504419}[的任务名称，括号中为创建者的进程号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12181_84059_76282786}

[[socket]{lang="EN-US"}]{#struct_0_12181_84059_x632109005}[的状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOFDREF]{lang="EN-US"}]{#struct_0_12181_84059_x2057235892}[：用户已经关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTED]{lang="EN-US"}]{#struct_0_12181_84059_x1823073452}[：连接已经建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTING]{lang="EN-US"}]{#struct_0_12181_84059_x1406245915}[：正在建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTING]{lang="EN-US"}]{#struct_0_12181_84059_x1623370411}[：正在断开连接]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASYNC]{lang="EN-US"}]{#struct_0_12181_84059_76086178}[：异步方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTED]{lang="EN-US"}]{#struct_0_12181_84059_1566667058}[：连接已经断开]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROTOREF]{lang="EN-US"}]{#struct_0_12181_84059_850428867}[：协议强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_212984461}[：不处于上述状态]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_12181_84059_76151714}

[[socket]{lang="EN-US"}]{#struct_0_12181_84059_x301105144}[的选项，有以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DEBUG]{lang="EN-US"}]{#struct_0_12181_84059_x1692846110}[：记录套接字的调试信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_ACCEPTCONN]{lang="EN-US"}]{#struct_0_12181_84059_524216830}[：]{lang="EN-US" style="font-family:宋体"}[server]{lang="EN-US"}[端监听连接请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEADDR]{lang="EN-US"}]{#struct_0_12181_84059_2084689803}[：允许本地地址重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVE]{lang="EN-US"}]{#struct_0_12181_84059_76479394}[：协议需要查询空闲的连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DONTROUTE]{lang="EN-US"}]{#struct_0_12181_84059_x1912517425}[：设置不查路由表，由于目的地址是直连网络的情况]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_BROADCAST]{lang="EN-US"}]{#struct_0_12181_84059_x614158482}[：套接字支持广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_LINGER]{lang="EN-US"}]{#struct_0_12181_84059_1993242345}[：套接字关闭但仍发送剩余数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_OOBINLINE]{lang="EN-US"}]{#struct_0_12181_84059_76544930}[：带外数据采用内联方式存储]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEPORT]{lang="EN-US"}]{#struct_0_12181_84059_716814009}[：允许本地端口重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMP]{lang="EN-US"}]{#struct_0_12181_84059_x212583888}[：记录入报文时间戳，只对非连接的协议有效，时间精确到毫秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_NOSIGPIPE]{lang="EN-US"}]{#struct_0_12181_84059_x259296075}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[不能发送数据导致返回失败时不创建]{lang="EN-US" style="font-family:宋体"}[SIGPIPE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMPNS]{lang="EN-US"}]{#struct_0_12181_84059_75955107}[：和时戳选项功能类似，时间可以精确到纳秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVETIME]{lang="EN-US"}]{#struct_0_12181_84059_x456955080}[：设置空闲探测时间，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[支持此选项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_FILTER]{lang="EN-US"}]{#struct_0_12181_84059_x457020616}[：设置报文过滤条件，]{style="font-family:宋体"}[OSI Socket]{lang="EN-US"}[和]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持此选项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x1271838681}[：没有设置选项]{lang="EN-US" style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_12181_84059_1073539953}

[[影响]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_76020643}[连接的错误码]{style="font-family:宋体"}

[[Receiving buffer (cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_12181_84059_58910163}

[[接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态]{style="font-family:宋体"}]{#struct_0_12181_84059_x1378930270}

[[状态的取值有：]{style="font-family:宋体"}]{#struct_0_12181_84059_935418304}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_12181_84059_75824035}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_12181_84059_704180816}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_12181_84059_1983303730}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x1338965251}[：不处于上述状态]{style="font-family:宋体"}

[[Sending buffer (cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_12181_84059_75889571}

[[发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态]{style="font-family:宋体"}]{#struct_0_12181_84059_633324745}

[[状态的取值有：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1946052216}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_12181_84059_76217251}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_12181_84059_1900529031}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_12181_84059_x1465238343}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_76282787}[：不处于上述状态]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12181_84059_1706543155}

[[使用的]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_x778654042}[类型，类型的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_12181_84059_x1307454160}[：]{style="font-family:宋体"}[SOCK_STREAM]{lang="EN-US"}[，]{style="font-family:宋体"}[流模式，提供可靠的字节流。]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[协议使用此类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_12181_84059_76086179}[：]{style="font-family:宋体"}[SOCK_DGRAM]{lang="EN-US"}[，数据报模式的通信。]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议使用此类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_12181_84059_x389648078}[：]{lang="EN-US" style="font-family:宋体"}[SOCK_RAW]{lang="EN-US"}[，]{style="font-family:宋体"}[RAW]{lang="EN-US"}[模式的通信方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x801398699}[：不是上述类型]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_12181_84059_76151715}

[[使用]{style="font-family:宋体"}[IPv6 RawIP socket]{lang="EN-US"}]{#struct_0_12181_84059_1655209992}[的协议号，]{style="font-family:宋体"}[58]{lang="EN-US"}[表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[Connection info]{lang="EN-US"}]{#struct_0_12181_84059_x860334712}

[[连接信息，分别为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_76479395}[地址、目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Inpcb flags]{lang="EN-US"}]{#struct_0_12181_84059_43797711}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_911323153}[协议控制块中的标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVOPTS]{lang="EN-US"}]{#struct_0_12181_84059_76544931}[：接收传入的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVRETOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x1239501127}[：接收回应的]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVDSTADDR]{lang="EN-US"}]{#struct_0_12181_84059_1733131634}[：接收目的]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_HDRINCL]{lang="EN-US"}]{#struct_0_12181_84059_75955104}[：用户提供整个]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEADDR]{lang="EN-US"}]{#struct_0_12181_84059_684476455}[：重复使用地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEPORT]{lang="EN-US"}]{#struct_0_12181_84059_76020640}[：重复使用端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ANONPORT]{lang="EN-US"}]{#struct_0_12181_84059_1632888275}[：]{lang="EN-US" style="font-family:宋体"}[用户未指定端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_PROTOCOL_PACKET]{lang="EN-US"}]{#struct_0_12181_84059_1030404337}[：标识报文为协议报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVVLANID]{lang="EN-US"}]{#struct_0_12181_84059_75824032}[：接收报文的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_IPV6_V6ONLY]{lang="EN-US"}]{#struct_0_12181_84059_x487460272}[：]{style="font-family:宋体"}[仅支持]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议栈]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_PKTINFO]{lang="EN-US"}]{#struct_0_12181_84059_x1362213649}[：]{style="font-family:宋体"}[接收报文的源地址和入接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_HOPLIMIT]{lang="EN-US"}]{#struct_0_12181_84059_75889568}[：]{style="font-family:宋体"}[接收报文]{lang="EN-US" style="font-family:宋体"}[hoplimit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_HOPOPTS]{lang="EN-US"}]{#struct_0_12181_84059_1390104622}[：]{style="font-family:宋体"}[接收报文的逐跳扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_DSTOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x156030216}[：]{style="font-family:宋体"}[接收报文的目的扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RTHDR]{lang="EN-US"}]{#struct_0_12181_84059_76217248}[：]{style="font-family:宋体"}[接收报文的路由扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RTHDRDSTOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x19050260}[：]{style="font-family:宋体"}[接收报文的路由头前的目的扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_TCLASS]{lang="EN-US"}]{#struct_0_12181_84059_76282784}[：]{style="font-family:宋体"}[接收报文的]{lang="EN-US" style="font-family:宋体"}[优先级]{style="font-family:宋体"}[信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_AUTOFLOWLABEL]{lang="EN-US"}]{#struct_0_12181_84059_x249771981}[：]{style="font-family:宋体"}[使用随机流标签]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RFC2292]{lang="EN-US"}]{#struct_0_12181_84059_x1449097708}[：使用]{style="font-family:宋体"}[RFC2292 API]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_MTU]{lang="EN-US"}]{#struct_0_12181_84059_76086176}[：]{style="font-family:宋体"}[感知路径]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[的变化]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[不支持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVMACADDR]{lang="EN-US"}]{#struct_0_12181_84059_x1109692110}[：接收报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_USEICMPSRC]{lang="EN-US"}]{#struct_0_12181_84059_76151712}[：使用配置的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[地址作为源地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SYNCPCB]{lang="EN-US"}]{#struct_0_12181_84059_x683442168}[：阻塞等待]{style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_76479392}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb extflag]{lang="EN-US"}]{#struct_0_12181_84059_1983217766}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_989058439}[协议控制块中的扩展标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_EXTRCVPVCIDX]{lang="EN-US"}]{#struct_0_12181_84059_1983217769}[：接收报文时记录报文的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVPWID]{lang="EN-US"}]{#struct_0_12181_84059_989123975}[：接收报文时记录报文的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x1212916473}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb vflag]{lang="EN-US"}]{#struct_0_12181_84059_x1530180401}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_76544928}[协议控制块中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[版本标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV4]{lang="EN-US"}]{#struct_0_12181_84059_1916349268}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_IPV6]{lang="EN-US"}]{#struct_0_12181_84059_75955105}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV6PROTO]{lang="EN-US"}]{#struct_0_12181_84059_x1654175705}[：运用]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议创建的]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_TIMEWAIT]{lang="EN-US"}]{#struct_0_12181_84059_389048419}[：处于等待状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_ONESBCAST]{lang="EN-US"}]{#struct_0_12181_84059_76020641}[：发送广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DROPPED]{lang="EN-US"}]{#struct_0_12181_84059_x323426861}[：协议丢弃标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_SOCKREF]{lang="EN-US"}]{#struct_0_12181_84059_75824033}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DONTBLOCK]{lang="EN-US"}]{#struct_0_12181_84059_1851191888}[：]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步时不能被阻塞]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_75889569}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Hop limit]{lang="EN-US"}]{#struct_0_12181_84059_x566210514}[(minimum hop limit)]{lang="SV"}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_76217249}[协议控制块中的跳数限制，括号中为最小跳数限制]{style="font-family:宋体"}

[[Send VRF]{lang="EN-US"}]{#struct_0_12181_84059_1937264876}

[[发送实例]{style="font-family:宋体"}]{#struct_0_12181_84059_1549026034}

[[Receive VRF]{lang="EN-US"}]{#struct_0_12181_84059_76282785}

[[接收实例]{style="font-family:宋体"}]{#struct_0_12181_84059_2088880179}

[ ]{lang="EN-US"}

::: {#-627058378 .myid}
[]{#_Toc404787003}[]{#struct_0_12181_84059_x457020617}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 router-renumber statistics**

------------------------------------------------------------------------

[**[display ipv6 router-renumber statistics]{lang="EN-US"}**]{#struct_0_12181_84059_344191396}[命令用来显示路由器重编号的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x456037577}

[**[display ipv6 router-renumber statistics]{lang="EN-US"}**]{#struct_0_12181_84059_1886044517}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_139545053}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x456103113}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x841509834}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1725377185}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x456561866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_753171921}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1230689525}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x456627402}

[[使用本命令可以查看路由器重编号流量统计信息、记录的序列号、重置序列号和分段号信息。]{style="font-family:宋体"}]{#struct_0_12181_84059_x450116978}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1521694303}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x456692938}[显示路由器重编号的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 router-renumber statistics]{lang="EN-US"}]{#struct_0_12181_84059_x456037578}

[Enabling/disabling protocol failed:         0]{lang="EN-US"}

[Packets with sequence number error:         2]{lang="EN-US"}

[Packets with segment number error:           1]{lang="EN-US"}

[PCO check failed:                                  0]{lang="EN-US"}

[Packets with T-flag set and R-flag unset:      1]{lang="EN-US"}

[Router-renumber function disable:            0 ]{lang="EN-US"}

[Packets too short:                              0]{lang="EN-US"}

[Packets with invalid destinations:           0]{lang="EN-US"}

[Create result packets failed:                 0]{lang="EN-US"}

[Sent result packets failed:                   0]{lang="EN-US"}

[Received command packets:                      7]{lang="EN-US"}

[Received reset packets:                          3]{lang="EN-US"}

[Sent result packets:                            9]{lang="EN-US"}

[SequenceNumber:                                   0x2]{lang="EN-US"}

[ResetSequenceNumber:                             0x2]{lang="EN-US"}

[SegmentNumber\[0\]:                             0x1]{lang="EN-US"}

[SegmentNumber\[1\]:                             0x0]{lang="EN-US"}

[SegmentNumber\[2\]:                             0x0]{lang="EN-US"}

[SegmentNumber\[3\]:                             0x0]{lang="EN-US"}

[SegmentNumber\[4\]:                             0x0]{lang="EN-US"}

[SegmentNumber\[5\]:                             0x0]{lang="EN-US"}

[SegmentNumber\[6\]:                             0x0]{lang="EN-US"}

[SegmentNumber\[7\]:                             0x0]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display ipv6 router-renumber statistics]{lang="EN-US"}]{#struct_0_12181_84059_x456103114}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1356008999}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x841575370}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x456561867}

[[Enabling/disabling protocol failed]{lang="EN-US"}]{#struct_0_12181_84059_x456627403}

[[使能协议报文上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_12181_84059_x450182514}[失败的个数]{style="font-family:宋体"}

[[Packets with sequence number error]{lang="EN-US"}]{#struct_0_12181_84059_x456692939}

[[序列号错误的报文个数]{style="font-family:宋体"}]{#struct_0_12181_84059_339478930}

[[Packets with segment number error]{lang="EN-US"}]{#struct_0_12181_84059_x456758475}

[[分段号错误的报文个数]{style="font-family:宋体"}]{#struct_0_12181_84059_x456824011}

[[PCO check failed]{lang="EN-US"}]{#struct_0_12181_84059_x1618272096}

[[PCO]{lang="EN-US"}]{#struct_0_12181_84059_x456889547}[信息块检测错误的报文个数]{style="font-family:宋体"}

[[Packet s with T-flag set and R-flag unset]{lang="EN-US"}]{#struct_0_12181_84059_x456955083}

[[设置了]{style="font-family:宋体"}[T]{lang="EN-US"}]{#struct_0_12181_84059_x40981521}[标志位、没有设置]{style="font-family:宋体"}[R]{lang="EN-US"}[标志位的消息，即不需要回应的测试报文个数]{style="font-family:宋体"}

[[Router-renumber function disable]{lang="EN-US"}]{#struct_0_12181_84059_x457020619}

[[接口没有使能重编号路由协议的报文个数]{style="font-family:宋体"}]{#struct_0_12181_84059_344846756}

[[Packets too short]{lang="EN-US"}]{#struct_0_12181_84059_x456037579}

[[报文长度小于正常值的报文个数]{style="font-family:宋体"}]{#struct_0_12181_84059_x456103115}

[[Packets with invalid destinations]{lang="EN-US"}]{#struct_0_12181_84059_x841640906}

[[无效目的地址的报文个数]{style="font-family:宋体"}]{#struct_0_12181_84059_x456561868}

[[Create result packets failed]{lang="EN-US"}]{#struct_0_12181_84059_x456627404}

[[创建]{style="font-family:宋体"}[Result]{lang="EN-US"}]{#struct_0_12181_84059_x450510194}[消息失败的报文个数]{style="font-family:宋体"}

[[Sent result packets failed]{lang="EN-US"}]{#struct_0_12181_84059_x456692940}

[[发送]{style="font-family:宋体"}[Result]{lang="EN-US"}]{#struct_0_12181_84059_x456758476}[报文失败个数]{style="font-family:宋体"}

[[Received command packets]{lang="EN-US"}]{#struct_0_12181_84059_1839110019}

[[接收]{style="font-family:宋体"}[Command]{lang="EN-US"}]{#struct_0_12181_84059_x456824012}[报文的个数]{style="font-family:宋体"}

[[Received reset packets]{lang="EN-US"}]{#struct_0_12181_84059_x456889548}

[[接收]{style="font-family:宋体"}[Reset]{lang="EN-US"}]{#struct_0_12181_84059_1418273606}[报文的个数]{style="font-family:宋体"}

[[Sent result packets]{lang="EN-US"}]{#struct_0_12181_84059_x456955084}

[[发送]{style="font-family:宋体"}[Result]{lang="EN-US"}]{#struct_0_12181_84059_x457020620}[报文的个数]{style="font-family:宋体"}

[[SequenceNumber]{lang="EN-US"}]{#struct_0_12181_84059_344388007}

[[记录序列号]{style="font-family:宋体"}]{#struct_0_12181_84059_x456037580}

[[ResetSequenceNumber]{lang="EN-US"}]{#struct_0_12181_84059_x456103116}

[[记录重置序列号]{style="font-family:宋体"}]{#struct_0_12181_84059_x841706442}

[[SegmentNumber\[0 - 7\]]{lang="EN-US"}]{#struct_0_12181_84059_x456561869}

[[组成记录分段号]{style="font-family:宋体"}]{#struct_0_12181_84059_x456627405}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x450575730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 router-renumber statistics]{lang="EN-US"}**]{#struct_0_12181_84059_x456692941}

::: {#1305447176 .myid}
[]{#_Toc59352304}[]{#_Toc404787004}[]{#struct_0_12181_84059_76086177}[]{#_Toc277663836}[]{#_Toc138417077}[]{#_Toc137020658}[]{#_Toc59352301}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 statistics**

------------------------------------------------------------------------

[**[display ipv6 statistics]{lang="EN-US"}**]{#struct_0_12181_84059_1228960050}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_426586814}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_1377015941}

[**[display ipv6 statistics]{lang="EN-US"}**]{#struct_0_12181_84059_x72641828}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_70821431}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_1483600469}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x754747606}[模式：]{style="font-family:宋体"}

[**[display ipv6 statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_x1456815506}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_76151713}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1272872968}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_2001804603}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x2113345331}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1589232809}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1578433517}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1182959424}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2069186651}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x345061376}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果不指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_76479393}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x363223432}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_426134735}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x336232848}[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_245987881}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x796954910}

[[本命令可以用来查看设备接收和发送]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1989871372}[报文及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[用户可以通过]{style="font-family:宋体"}**[reset ipv6 statistics]{lang="EN-US"}**]{#struct_0_12181_84059_1357258303}[命令清除所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x39965868}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_115442071}[查看]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display]{lang="EN-US"}]{#struct_0_12181_84059_1642039049}[ ipv6 statistics]{lang="PT-BR"}

[  IPv6 statistics:]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Sent packets:]{lang="EN-US"}

[      Total:      0]{lang="EN-US"}

[        Sent locally:         0            Forwarded:              0]{lang="EN-US"}

[        Raw packets:          0            Discarded:              0]{lang="EN-US"}

[        Fragments:            0            Fragments failed:      0]{lang="EN-US"}

[        Routing failed:       0]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Received packets:]{lang="EN-US"}

[      Total:      0]{lang="EN-US"}

[        Received locally:     0            Hop limit exceeded:  0]{lang="EN-US"}

[        Fragments:             0            Reassembled:           0]{lang="EN-US"}

[        Reassembly failures:  0            Reassembly timeout:  0]{lang="EN-US"}

[        Format errors:         0            Option errors:        0]{lang="EN-US"}

[        Protocol errors:      0]{lang="EN-US"}

[ ]{lang="EN-US"}

[  ICMPv6 statistics:]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Sent packets:]{lang="EN-US"}

[      Total:      0]{lang="EN-US"}

[        Unreachable:           0             Too big:                0]{lang="EN-US"}

[        Hop limit exceeded:   0             Reassembly timeouts: 0]{lang="EN-US"}

[        Parameter problems:   0]{lang="EN-US"}

[        Echo requests:         0             Echo replies:          0]{lang="EN-US"}

[        Neighbor solicits:    0             Neighbor adverts:     0]{lang="EN-US"}

[        Router solicits:      0             Router adverts:        0]{lang="EN-US"}

[        Redirects:             0              Router renumbering:   0]{lang="EN-US"}

[      Send failed:]{lang="EN-US"}

[        Rate limitation:      0             Other errors:          0]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Received packets:]{lang="EN-US"}

[      Total:      0]{lang="EN-US"}

[        Checksum errors:      0             Too short:              0]{lang="EN-US"}

[        Bad codes:             0]{lang="EN-US"}

[        Unreachable:           0             Too big:                 0]{lang="EN-US"}

[        Hop limit exceeded:   0             Reassembly timeouts:   0]{lang="EN-US"}

[        Parameter problems:   0             Unknown error types:   0]{lang="EN-US"}

[        Echo requests:         0             Echo replies:           0]{lang="EN-US"}

[        Neighbor solicits:    0             Neighbor adverts:      0]{lang="EN-US"}

[        Router solicits:       0             Router adverts:        0]{lang="EN-US"}

[        Redirects:              0             Router renumbering:   0]{lang="EN-US"}

[        Unknown info types:   0]{lang="EN-US"}

[      Deliver failed:]{lang="EN-US"}

[        Bad length:           0]{lang="EN-US"}

[]{#struct_0_12181_84059_1642104585}[]{#_Ref197144764}[]{#_Toc138417056}[[表1-18 ]{lang="EN-US"}[display ipv6 statistics]{lang="EN-US"}]{#_Toc94583063}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_906000445}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x2022477502}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x647707181}

[[IPv6 statistics:]{lang="EN-US"}]{#struct_0_12181_84059_1245760113}

[[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_2018526070}[报文统计信息]{style="font-family:宋体"}

[[Sent packets:]{lang="EN-US"}]{#struct_0_12181_84059_x976559618}

[[  Total:]{lang="EN-US"}]{#struct_0_12181_84059_1641907977}

[[    Sent locally:]{lang="EN-US"}]{#struct_0_12181_84059_x1087046740}

[[    Forwarded:]{lang="EN-US"}]{#struct_0_12181_84059_x1139753311}

[[    Raw packets:]{lang="EN-US"}]{#struct_0_12181_84059_137720232}

[[    Discarded:]{lang="EN-US"}]{#struct_0_12181_84059_x414966147}

[[    Fragments:]{lang="EN-US"}]{#struct_0_12181_84059_219724852}

[[    Fragments failed:]{lang="EN-US"}]{#struct_0_12181_84059_1641973513}

[[    Routing failed:]{lang="EN-US"}]{#struct_0_12181_84059_2014563858}

[[发送]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_155556601}[报文的统计信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地发送报文和转发报文的总数]{style="font-family:宋体"}]{#struct_0_12181_84059_1834576074}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地发送报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_339618621}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[转发报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642301193}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}[raw socket]{lang="EN-US"}]{#struct_0_12181_84059_x497895286}[发送的报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[丢弃报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x484932478}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送分片报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1854888980}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分片报文发送失败的个数]{style="font-family:宋体"}]{#struct_0_12181_84059_x1887254295}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由失败报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642366729}

[[Received packets:]{lang="EN-US"}]{#struct_0_12181_84059_1504741460}

[[  Total:]{lang="EN-US"}]{#struct_0_12181_84059_x1297901539}

[[    Received locally:]{lang="EN-US"}]{#struct_0_12181_84059_29547942}

[[    Hop limit exceeded:]{lang="EN-US"}]{#struct_0_12181_84059_1923302024}

[[    Fragments:]{lang="EN-US"}]{#struct_0_12181_84059_1642170121}

[[    Reassembled:]{lang="EN-US"}]{#struct_0_12181_84059_1079133112}

[[    Reassembly failures:]{lang="EN-US"}]{#struct_0_12181_84059_x1814255228}

[[    Reassembly timeout:]{lang="EN-US"}]{#struct_0_12181_84059_x1564266532}

[[    Format errors:]{lang="EN-US"}]{#struct_0_12181_84059_1642235657}

[[    Option errors:]{lang="EN-US"}]{#struct_0_12181_84059_x1246828981}

[[    Protocol errors:]{lang="EN-US"}]{#struct_0_12181_84059_1723943149}

[[接收]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1130991757}[报文的统计信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收报文总数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642563337}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地接收报文数，即目的地是本机的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_x1265381736}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[超出跳数范围的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_269342562}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收的分片报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x378426754}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重组报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642628873}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重组失败的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1855449190}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重组超时的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1585992913}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[格式错误的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_2075757843}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[选项错误的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642039050}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议错误的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1816878413}

[[ICMPv6 statistics:]{lang="EN-US"}]{#struct_0_12181_84059_x1121343244}

[[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_1642104586}[报文的统计信息]{style="font-family:宋体"}

[[Sent packets:]{lang="EN-US"}]{#struct_0_12181_84059_x2022280894}

[[  Total:]{lang="EN-US"}]{#struct_0_12181_84059_776670037}

[[    Unreached:]{lang="EN-US"}]{#struct_0_12181_84059_1490762109}

[[    Too big:]{lang="EN-US"}]{#struct_0_12181_84059_1641907978}

[[    Hop limit exceeded:]{lang="EN-US"}]{#struct_0_12181_84059_x1086325844}

[[    Reassembly timeouts:]{lang="EN-US"}]{#struct_0_12181_84059_1629118803}

[[    Parameter problems:]{lang="EN-US"}]{#struct_0_12181_84059_1641973514}

[[    Echo requests:]{lang="EN-US"}]{#struct_0_12181_84059_2014105106}

[[    Echo replies:]{lang="EN-US"}]{#struct_0_12181_84059_x1065396716}

[[    Neighbor solicits:]{lang="EN-US"}]{#struct_0_12181_84059_1642301194}

[[    Neighbor adverts:]{lang="EN-US"}]{#struct_0_12181_84059_x498222966}

[[    Router solicits:]{lang="EN-US"}]{#struct_0_12181_84059_x1460519865}

[[    Router adverts:]{lang="EN-US"}]{#struct_0_12181_84059_1642366730}

[[    Redirects:]{lang="EN-US"}]{#struct_0_12181_84059_1505331283}

[[    Router Renumbering]{lang="EN-US"}]{#struct_0_12181_84059_1109522076}

[[  Sent failed:]{lang="EN-US"}]{#struct_0_12181_84059_x907110241}

[[    Rate limitation:]{lang="EN-US"}]{#struct_0_12181_84059_1642170122}

[[    Other errors:]{lang="EN-US"}]{#struct_0_12181_84059_1079198648}

[[发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_1339592724}[报文的统计信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送报文总数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642235658}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目的不可达报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1247812021}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文太长的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_778784962}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[超出跳数限制的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642563338}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分片重组超时报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1265971560}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数错误报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_900415631}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[回应请求报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642628874}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[回应响应报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1855383654}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[邻居请求报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x718223520}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[邻居通告报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642039047}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器请求报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1817337164}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器通告报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642104583}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重定向报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x2022084286}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器重编号报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1109325468}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本机发送失败的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_x1824197487}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[因速率超过限制而未发送的报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1641907975}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[其他错误的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1087177812}

[[Received packets:]{lang="EN-US"}]{#struct_0_12181_84059_1641973511}

[[  Total:]{lang="EN-US"}]{#struct_0_12181_84059_2014432786}

[[    Checksum errors:]{lang="EN-US"}]{#struct_0_12181_84059_x1448931350}

[[    Too short:]{lang="EN-US"}]{#struct_0_12181_84059_1642301191}

[[    Bad codes:]{lang="EN-US"}]{#struct_0_12181_84059_x498026358}

[[    Unreachable:]{lang="EN-US"}]{#struct_0_12181_84059_1642366727}

[[    Too big:]{lang="EN-US"}]{#struct_0_12181_84059_1505396820}

[[    Hop limit exceeded:]{lang="EN-US"}]{#struct_0_12181_84059_x109245120}

[[    Reassembly timeouts:]{lang="EN-US"}]{#struct_0_12181_84059_1642170119}

[[    Parameter problems:]{lang="EN-US"}]{#struct_0_12181_84059_1078608821}

[[    Unknown error types:]{lang="EN-US"}]{#struct_0_12181_84059_1642235655}

[[    Echo requests:]{lang="EN-US"}]{#struct_0_12181_84059_x1246960053}

[[    Echo replies:]{lang="EN-US"}]{#struct_0_12181_84059_1642563335}

[[    Neighbor solicits:]{lang="EN-US"}]{#struct_0_12181_84059_x1265250664}

[[    Neighbor adverts:]{lang="EN-US"}]{#struct_0_12181_84059_1642628871}

[[    Router solicits:]{lang="EN-US"}]{#struct_0_12181_84059_1855580262}

[[    Router adverts:]{lang="EN-US"}]{#struct_0_12181_84059_x1886575512}

[[    Redirects:]{lang="EN-US"}]{#struct_0_12181_84059_1642039048}

[[    Router renumbering:]{lang="EN-US"}]{#struct_0_12181_84059_1816354124}

[[    Unknown info types:]{lang="EN-US"}]{#struct_0_12181_84059_1642104584}

[[  Deliver failed:]{lang="EN-US"}]{#struct_0_12181_84059_x2022411966}

[[    Bad length:]{lang="EN-US"}]{#struct_0_12181_84059_1641907976}

[[接收]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1086981204}[报文的统计信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收报文总数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1641973512}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[校验和错误的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_2014498322}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文太短的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642301192}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[错误代码的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x497829750}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不可达报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1960506063}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文太长的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642366728}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[超出跳数限制的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1504806996}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分片重组超时的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642170120}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数错误报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1079067576}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[未知错误报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642235656}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[回应请求报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1246894517}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[回应响应报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642563336}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[邻居请求报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1265316200}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[邻居通告报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642628872}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器请求报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1855514726}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器通告报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1642039045}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重定向报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1817206092}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器重编号报文数]{style="font-family:宋体"}]{#struct_0_12181_84059_1642104581}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[未知信息报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x2022215358}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[上送本机失败的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1641907973}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[长度错误的报文数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1641973509}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_2013908499}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 statistics]{lang="EN-US"}**]{#struct_0_12181_84059_x1364354006}

::: {#-165911377 .myid}
[]{#_Toc404787005}[]{#struct_0_12181_84059_2900002}[]{#_Toc279391294}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 tcp**

------------------------------------------------------------------------

[**[display ipv6 tcp]{lang="EN-US"}**]{#struct_0_12181_84059_1606953622}[命令用来显示]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1745703383}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_2028744961}

[**[display ipv6 tcp]{lang="EN-US"}**]{#struct_0_12181_84059_2107331802}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_793217889}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 tcp]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_1642301189}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x497502069}[模式：]{style="font-family:宋体"}

[**[display ipv6 tcp]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_x842711854}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_858752521}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x815736899}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2085372929}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x537416463}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x365495966}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1642366725}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_1505527892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1649311458}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_148985081}[：显示指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1150776937}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1144418681}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1588816145}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_65434900}[：显示指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_245660199}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_2114740131}

[[本命令可以用来查看]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}]{#struct_0_12181_84059_x880609146}[连接摘要信息，包括本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号、对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的状态等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1374284557}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1642170117}[显示]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 tcp]{lang="EN-US"}]{#struct_0_12181_84059_1079002037}

[\*: TCP MD5 Connection]{lang="EN-US"}

[ LAddr-\>port         FAddr-\>port       State       Chassis Slot  CPU PCB]{lang="EN-US"}

[\*2001:2002:2003:2   3001:3002:3003:3 ESTABLISHED 1       1     0    0x000000000000c387]{lang="EN-US"}

[004:2005:2006:20    004:3005:3006:30]{lang="EN-US"}

[07:2008-\>1200        07:3008-\>1200]{lang="EN-US"}

[2001::1-\>23          2001::5-\>1284     ESTABLISHED 1       2     0    0x0000000000000008]{lang="EN-US"}

[2003::1-\>25          2001::2-\>1283     LISTEN       1       3     0    0x0000000000000009]{lang="EN-US"}

[[[表1-19 ]{lang="EN-US"}]{.FigureDescriptionChar}[display ipv6 tcp]{lang="EN-US"}]{#struct_0_12181_84059_x1035133378}[[命令显示信息描述表]{style="font-family:黑体"}]{.FigureDescriptionChar}

[]{#table_struct_0_908652369}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x583835120}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_984124534}

[[\*]{lang="EN-US"}]{#struct_0_12181_84059_1642235653}

[[如果某个连接前有此标识，则表示该]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12181_84059_x1247091125}[连接是采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[加密算法认证的连接]{style="font-family:宋体"}

[[LAddr-\>port]{lang="EN-US"}]{#struct_0_12181_84059_165793703}

[[本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x565972051}[地址及端口号]{style="font-family:宋体"}

[[FAddr-\>port]{lang="EN-US"}]{#struct_0_12181_84059_601230041}

[[对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_258467580}[地址及端口号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12181_84059_1642563333}

[[TCP]{lang="EN-US"}]{#struct_0_12181_84059_x1265643880}[连接状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_12181_84059_x1775304223}[：服务器收到客户端的关闭连接请求回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_12181_84059_58768485}[：服务器在等待连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_SENT]{lang="EN-US"}]{#struct_0_12181_84059_x1220509722}[：客户端发出连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_RCVD]{lang="EN-US"}]{#struct_0_12181_84059_1642628869}[：服务器收到客户端连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_12181_84059_1856104549}[：服务器和客户端双方建立连接并能进行双向数据传递的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE_WAIT]{lang="EN-US"}]{#struct_0_12181_84059_x2024123766}[：服务器收到客户端关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_1]{lang="EN-US"}]{#struct_0_12181_84059_974419928}[：客户端发出关闭连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSING]{lang="EN-US"}]{#struct_0_12181_84059_1502247737}[：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAST_ACK]{lang="EN-US"}]{#struct_0_12181_84059_1642039046}[：服务器向客户端发出关闭连接请求等待回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_2]{lang="EN-US"}]{#struct_0_12181_84059_1817271628}[：客户端收到服务器关闭连接回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIME_WAIT]{lang="EN-US"}]{#struct_0_12181_84059_x1039626038}[：客户端收到服务器的关闭连接请求后所处的状态]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_12181_84059_334902234}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_1891193370}[中的成员编号]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_1642104582}

[[单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_12181_84059_x2022018750}

[[CPU]{lang="EN-US"}]{#struct_0_12181_84059_245922343}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_12181_84059_246118951}[编号]{style="font-family:宋体"}

[[PCB]{lang="EN-US"}]{#struct_0_12181_84059_x582103899}

[[协议控制块索引]{style="font-family:宋体"}]{#struct_0_12181_84059_1818611650}

[ ]{lang="EN-US"}

::::: {#1188677841 .myid}
[]{#_Toc404787006}[]{#struct_0_12181_84059_1061027139}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 tcp-proxy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_12181_84059_x1029667830}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_12181_84059_x286740746}
:::

[ ]{lang="EN-US"}

[**[display ipv6 tcp-proxy]{lang="EN-US"}**]{#struct_0_12181_84059_1851278601}[命令用来显示]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1442761259}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_1987164181}

[**[display ipv6 tcp-proxy]{lang="EN-US"}**]{#struct_0_12181_84059_x1311560320}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x656824982}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 tcp-proxy slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_12181_84059_x943120216}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x150794036}[模式：]{style="font-family:宋体"}

[**[display ipv6 tcp-proxy chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_12181_84059_1930174531}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_12181_84059_9978511}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x573329004}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1682499786}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1417323035}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1835948166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_884696395}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1740707346}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_732883255}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1346698085}[：显示指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1635372476}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x989135244}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x148760906}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x349367951}[：显示指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_x841627157}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1362152076}

[[IPv6 TCP]{lang="EN-US"}]{#struct_0_12181_84059_x311935770}[代理是一种与传统定义的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[相比更快速更灵活的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[实现。用于支持负载分担或]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[业务。能够提供比普通]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[传输更灵活的控制，从而达到传输优化的目的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1944964914}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1377471265}[显示]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 tcp-proxy]{lang="EN-US"}]{#struct_0_12181_84059_2051529634}

[LAddr-\>port            FAddr-\>port              State        Service type]{lang="EN-US"}

[2001::1-\>45            11:22:33:44-\>54602      ESTABLISHED WAAS]{lang="EN-US"}

[11:22:33:44-\>54602    2001::1-\>45              ESTABLISHED WAAS]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[display ipv6 tcp-proxy]{lang="EN-US"}]{#struct_0_12181_84059_x1781184275}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1065998498}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x1714844847}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x521871967}

[[LAddr-\>port]{lang="EN-US"}]{#struct_0_12181_84059_x1671465356}

[[本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1014038508}[地址及端口号]{style="font-family:宋体"}

[[Faddr-\>port]{lang="EN-US"}]{#struct_0_12181_84059_451783165}

[[对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x2026276327}[地址及端口号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12181_84059_x552045433}

[[IPv6 TCP]{lang="EN-US"}]{#struct_0_12181_84059_x1549227360}[代理连接状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_12181_84059_x1375030008}[：服务器收到客户端的关闭连接请求回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_12181_84059_x2118129374}[：服务器在等待连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_SENT]{lang="EN-US"}]{#struct_0_12181_84059_x970537647}[：客户端发出连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_RECEIVED]{lang="EN-US"}]{#struct_0_12181_84059_610753981}[：服务器收到客户端连接请求时所处的状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_12181_84059_1150623506}[：服务器和客户端双方建立连接并能进行双向数据传递的状态]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE_WAIT]{lang="EN-US"}]{#struct_0_12181_84059_1965541118}[：服务器收到客户端关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_1]{lang="EN-US"}]{#struct_0_12181_84059_x1667790680}[：客户端发出关闭连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[CLOSING]{lang="EN-US"}]{#struct_0_12181_84059_440806996}[：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAST_ACK]{lang="EN-US"}]{#struct_0_12181_84059_1061092675}[：服务器向客户端发出关闭连接请求等待回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_2]{lang="EN-US"}]{#struct_0_12181_84059_152517895}[：客户端收到服务器关闭连接回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIME_WAIT]{lang="EN-US"}]{#struct_0_12181_84059_x1311494784}[：客户端收到服务器的关闭连接请求后所处的状态]{style="font-family:宋体"}

[[Service type]{lang="EN-US"}]{#struct_0_12181_84059_x860733043}

[[服务类型，可能的取值如下：]{style="font-family:宋体"}]{#struct_0_12181_84059_1417388571}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LB]{lang="EN-US"}]{#struct_0_12181_84059_x710366689}[：负载均衡服务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAAS]{lang="EN-US"}]{#struct_0_12181_84059_x148695370}[：]{lang="EN-US" style="font-family:宋体"}[WAAS]{lang="EN-US"}[服务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSL VPN]{lang="EN-US"}]{#struct_0_12181_84059_x1877494848}[：]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[服务]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-318259578 .myid}
[]{#_Toc138239303}[]{#_Toc136679741}[]{#_Toc69790799}[]{#_Toc404787007}[]{#struct_0_12181_84059_x1214148541}[]{#_Toc279391295}[]{#_Toc249245004}[]{#_Toc233688809}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 tcp verbose**

------------------------------------------------------------------------

[**[display ipv6 tcp verbose]{lang="EN-US"}**]{#struct_0_12181_84059_1641907974}[命令用来显示]{style="font-family:
宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1087112276}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1896672815}

[**[display ipv6 tcp verbose]{lang="EN-US"}**[ \[ **pcb** *pcb-index* \]]{lang="EN-US"}]{#struct_0_12181_84059_1472643677}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x2045859495}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 tcp verbose]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_x291359706}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x1863185327}[模式：]{style="font-family:宋体"}

[**[display ipv6 tcp verbose]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_1152191129}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x161566635}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1641973510}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_2014367250}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x667325289}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_148662273}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_547065335}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_23959911}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x848964629}

[**[pcb]{lang="EN-US"}**[ *pcb-index*]{lang="EN-US"}]{#struct_0_12181_84059_1597652805}[：显示指定协议控制块索引的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[pcb-index]{lang="EN-US"}*[表示协议控制块索引，取值范围请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1642301190}[：显示指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x497960822}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_824884251}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1853433480}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_547976498}[：显示指定单板的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_1811744145}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1383872828}

[[本命令可以用来查看]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}]{#struct_0_12181_84059_1855482162}[连接详细信息，包括]{style="font-family:宋体"}[socket]{lang="EN-US"}[的创建者、状态、选项、类型、使用的协议号等，以及]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号、目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号、状态等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1475396779}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1605440709}[显示]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 tcp verbose]{lang="EN-US"}]{#struct_0_12181_84059_1604981956}

[TCP inpcb number: 1(tcpcb number: 1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Creator: bgpd\[199\]]{lang="EN-US"}

[ State: ISCONNECTED]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 65536 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 65536 / 512 / N/A]{lang="EN-US"}

[ Type: 1]{lang="EN-US"}

[ Protocol: 6]{lang="EN-US"}

[ Connection info: src = 2001::1-\>179 ,  dst = 2001::2-\>4181]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Connection state: ESTABLISHED]{lang="EN-US"}

[ TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR]{lang="EN-US"}

[ NSR state: READY(M)]{lang="EN-US"}

[ Send VRF: 0x0]{lang="EN-US"}

[ Receive VRF: 0x0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1218603168}[显示]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 tcp verbose]{lang="EN-US"}]{#struct_0_12181_84059_1604916420}

[TCP inpcb number: 1(tcpcb number: 1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Slot: 6 Cpu: 0]{lang="EN-US"}

[ NSR standby: N/A]{lang="EN-US"}

[ Creator: bgpd\[199\]]{lang="EN-US"}

[ State: ISCONNECTED]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 65536 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 65536 / 512 / N/A]{lang="EN-US"}

[ Type: 1]{lang="EN-US"}

[ Protocol: 6]{lang="EN-US"}

[ Connection info: src = 2001::1-\>179 ,  dst = 2001::2-\>4181]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Connection state: ESTABLISHED]{lang="EN-US"}

[ TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR]{lang="EN-US"}

[ NSR state: READY(M)]{lang="EN-US"}

[ Send VRF: 0x0]{lang="EN-US"}

[ Receive VRF: 0x0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_320355310}[显示]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 tcp verbose]{lang="EN-US"}]{#struct_0_12181_84059_1642366726}

[TCP inpcb number: 1(tcpcb number: 1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Chassis: 2 Slot: 6 Cpu: 0]{lang="EN-US"}

[ NSR standby: N/A]{lang="EN-US"}

[ Creator: bgpd\[199\]]{lang="EN-US"}

[ State: ISCONNECTED]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 65536 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 65536 / 512 / N/A]{lang="EN-US"}

[ Type: 1]{lang="EN-US"}

[ Protocol: 6]{lang="EN-US"}

[ Connection info: src = 2001::1-\>179 ,  dst = 2001::2-\>4181]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Connection state: ESTABLISHED]{lang="EN-US"}

[ TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR]{lang="EN-US"}

[ NSR state: READY(M)]{lang="EN-US"}

[ Send VRF: 0x0]{lang="EN-US"}

[ Receive VRF: 0x0]{lang="EN-US"}

[[[表1-21 ]{lang="EN-US"}]{.FigureDescriptionChar}[display ipv6 tcp verbo[se]{.FigureDescriptionChar}]{lang="EN-US"}]{#struct_0_12181_84059_1505462356}[[命令显示信息描述表]{style="font-family:黑体"}]{.FigureDescriptionChar}

[]{#table_struct_0_938563317}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_1467562540}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x2026750885}

[[TCP inpcb number]{lang="EN-US"}]{#struct_0_12181_84059_1642170118}

[[IPv6 TCP]{lang="EN-US"}]{#struct_0_12181_84059_1078543285}[类型]{style="font-family:宋体"}[Internet]{lang="EN-US"}[协议控制块个数]{style="font-family:宋体"}

[[tcpcb number]{lang="EN-US"}]{#struct_0_12181_84059_x644437753}

[[IPv6 TCP]{lang="EN-US"}]{#struct_0_12181_84059_961202763}[控制块个数（处于]{style="font-family:宋体"}[TIME_WAIT]{lang="EN-US"}[状态的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[则不列入计数）]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_12181_84059_x1349150902}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_1853410293}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_1642235654}

[[单板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1247025589}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_1604719812}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_1115503866}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Cpu]{lang="EN-US"}]{#struct_0_12181_84059_1812071825}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_12181_84059_1812006289}[编号]{style="font-family:宋体"}

[[NSR standby::]{lang="EN-US"}]{#struct_0_12181_84059_1109980826}

[[NSR]{lang="EN-US"}]{#struct_0_12181_84059_1109456537}[备所在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号和槽位号，如果不存在]{style="font-family:宋体"}[NSR]{lang="EN-US"}[备，则显示"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["]{style="font-family:宋体"}

[[Creator]{lang="EN-US"}]{#struct_0_12181_84059_x356604948}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_x872144797}[的任务名称，括号中为创建者的进程号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12181_84059_654693473}

[[socket]{lang="EN-US"}]{#struct_0_12181_84059_1642563334}[的状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOFDREF]{lang="EN-US"}]{#struct_0_12181_84059_x1265185128}[：用户已经关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTED]{lang="EN-US"}]{#struct_0_12181_84059_892584086}[：连接已经建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTING]{lang="EN-US"}]{#struct_0_12181_84059_x757379469}[：正在建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTING]{lang="EN-US"}]{#struct_0_12181_84059_x2011946370}[：正在断开连接]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASYNC]{lang="EN-US"}]{#struct_0_12181_84059_1642628870}[：异步方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTED]{lang="EN-US"}]{#struct_0_12181_84059_1855645798}[：连接已经断开]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROTOREF]{lang="EN-US"}]{#struct_0_12181_84059_50650575}[：协议强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x127175736}[：不处于上述状态]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_12181_84059_1751294723}

[[socket]{lang="EN-US"}]{#struct_0_12181_84059_x730613946}[的选项，有以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DEBUG]{lang="EN-US"}]{#struct_0_12181_84059_x924821645}[：记录套接字的调试信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_ACCEPTCONN]{lang="EN-US"}]{#struct_0_12181_84059_x1186171277}[：]{lang="EN-US" style="font-family:宋体"}[server]{lang="EN-US"}[端监听连接请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEADDR]{lang="EN-US"}]{#struct_0_12181_84059_x651188756}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[允许本地地址重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVE]{lang="EN-US"}]{#struct_0_12181_84059_x730548410}[：协议需要查询空闲的连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DONTROUTE]{lang="EN-US"}]{#struct_0_12181_84059_x578910390}[：设置不查路由表，由于目的地址是直连网络的情况]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_BROADCAST]{lang="EN-US"}]{#struct_0_12181_84059_x1527315734}[：套接字支持广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_LINGER]{lang="EN-US"}]{#struct_0_12181_84059_x85608979}[：套接字关闭但仍发送剩余数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_OOBINLINE]{lang="EN-US"}]{#struct_0_12181_84059_x730745018}[：带外数据采用内联方式存储]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEPORT]{lang="EN-US"}]{#struct_0_12181_84059_x929457235}[：允许本地端口重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_NOSIGPIPE]{lang="EN-US"}]{#struct_0_12181_84059_x708080450}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[不能发送数据导致返回失败时不创建]{lang="EN-US" style="font-family:宋体"}[SIGPIPE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMPNS]{lang="EN-US"}]{#struct_0_12181_84059_x529403782}[：和时戳选项功能类似，时间可以精确到纳秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVETIME]{lang="EN-US"}]{#struct_0_12181_84059_1109128857}[：设置空闲探测时间，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[支持此选项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_FILTER]{lang="EN-US"}]{#struct_0_12181_84059_1109063321}[：设置报文过滤条件，]{style="font-family:宋体"}[OSI Socket]{lang="EN-US"}[和]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持此选项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x730679482}[：没有设置选项]{lang="EN-US" style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_12181_84059_978719513}

[[影响]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_1390992482}[连接的错误码]{style="font-family:宋体"}

[[Receiving buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_12181_84059_x730351802}

[[接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态]{style="font-family:宋体"}]{#struct_0_12181_84059_x138121802}

[[状态的取值有：]{style="font-family:宋体"}]{#struct_0_12181_84059_472739189}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_12181_84059_96834401}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_12181_84059_x730286266}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_12181_84059_x1689782092}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_959947276}[：不处于上述状态]{style="font-family:宋体"}

[[Sending buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_12181_84059_x730482874}

[[发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态]{style="font-family:宋体"}]{#struct_0_12181_84059_x511325233}

[[状态的取值有：]{style="font-family:宋体"}]{#struct_0_12181_84059_1030828073}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_12181_84059_828160240}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_12181_84059_x730417338}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_12181_84059_x2103016252}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_429502154}[：不处于上述状态]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12181_84059_x730089658}

[[使用的]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_630264296}[类型，类型的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_12181_84059_x978183165}[：]{style="font-family:宋体"}[SOCK_STREAM]{lang="EN-US"}[，]{style="font-family:宋体"}[流模式，提供可靠的字节流。]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[协议使用此类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_12181_84059_x730024122}[：]{style="font-family:宋体"}[SOCK_DGRAM]{lang="EN-US"}[，数据报模式的通信。]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议使用此类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_12181_84059_x153219260}[：]{lang="EN-US" style="font-family:宋体"}[SOCK_RAW]{lang="EN-US"}[，]{style="font-family:宋体"}[RAW]{lang="EN-US"}[模式的通信方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x1725488610}[：不是上述类型]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_12181_84059_x730613945}

[[使用]{style="font-family:宋体"}[TCP socket]{lang="EN-US"}]{#struct_0_12181_84059_x924756109}[的协议号，]{style="font-family:宋体"}[6]{lang="EN-US"}[表示运用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[Connection info]{lang="EN-US"}]{#struct_0_12181_84059_1164187717}

[[连接信息，分别为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x730548409}[地址及端口号、目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号]{style="font-family:宋体"}

[[Inpcb flags]{lang="EN-US"}]{#struct_0_12181_84059_x578320565}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_x1898642889}[协议控制块中的标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x730745017}[：接收传入的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVRETOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x929522771}[：接收回应的]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVDSTADDR]{lang="EN-US"}]{#struct_0_12181_84059_89516658}[：接收目的]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_HDRINCL]{lang="EN-US"}]{#struct_0_12181_84059_x730679481}[：用户提供整个]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEADDR]{lang="EN-US"}]{#struct_0_12181_84059_978522905}[：重复使用地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEPORT]{lang="EN-US"}]{#struct_0_12181_84059_x730351801}[：重复使用端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ANONPORT]{lang="EN-US"}]{#struct_0_12181_84059_x138056266}[：]{lang="EN-US" style="font-family:宋体"}[用户未指定端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_PROTOCOL_PACKET]{lang="EN-US"}]{#struct_0_12181_84059_107542647}[：标识报文为协议报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVVLANID]{lang="EN-US"}]{#struct_0_12181_84059_x730286265}[：接收报文的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_IPV6_V6ONLY]{lang="EN-US"}]{#struct_0_12181_84059_x1689847628}[：]{style="font-family:宋体"}[仅支持]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议栈]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_PKTINFO]{lang="EN-US"}]{#struct_0_12181_84059_467027496}[：]{style="font-family:宋体"}[接收报文的源地址和入接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_HOPLIMIT]{lang="EN-US"}]{#struct_0_12181_84059_x730482873}[：]{style="font-family:宋体"}[接收报文]{lang="EN-US" style="font-family:宋体"}[hoplimit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_HOPOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x510866481}[：]{style="font-family:宋体"}[接收报文的逐跳扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_DSTOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x730417337}[：]{style="font-family:宋体"}[接收报文的目的扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RTHDR]{lang="EN-US"}]{#struct_0_12181_84059_x2103475004}[：]{style="font-family:宋体"}[接收报文的路由扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RTHDRDSTOPTS]{lang="EN-US"}]{#struct_0_12181_84059_543228700}[：]{style="font-family:宋体"}[接收报文的路由头前的目的扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_TCLASS]{lang="EN-US"}]{#struct_0_12181_84059_x730089657}[：]{style="font-family:宋体"}[接收报文的]{lang="EN-US" style="font-family:宋体"}[优先级]{style="font-family:宋体"}[信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_AUTOFLOWLABEL]{lang="EN-US"}]{#struct_0_12181_84059_630723048}[：]{style="font-family:宋体"}[使用随机]{lang="EN-US" style="font-family:宋体"}[流标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RFC2292]{lang="EN-US"}]{#struct_0_12181_84059_x84933077}[：使用]{style="font-family:宋体"}[RFC2292 API]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_MTU]{lang="EN-US"}]{#struct_0_12181_84059_x730024121}[：]{style="font-family:宋体"}[感知路径]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[的变化]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[不支持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVMACADDR]{lang="EN-US"}]{#struct_0_12181_84059_x153022652}[：接收报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SYNCPCB]{lang="EN-US"}]{#struct_0_12181_84059_x730613948}[：阻塞等待]{style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x924428429}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb extflag]{lang="EN-US"}]{#struct_0_12181_84059_x357597085}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_x357597086}[协议控制块中的扩展标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_EXTRCVPVCIDX]{lang="EN-US"}]{#struct_0_12181_84059_x515587531}[：接收报文时记录报文的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVPWID]{lang="EN-US"}]{#struct_0_12181_84059_x1580775655}[：接收报文时记录报文的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x357597083}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb vflag]{lang="EN-US"}]{#struct_0_12181_84059_x730548412}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_x578779318}[协议控制块中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[版本标记：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV4]{lang="EN-US"}]{#struct_0_12181_84059_x730745020}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV6]{lang="EN-US"}]{#struct_0_12181_84059_x929981524}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV6PROTO]{lang="EN-US"}]{#struct_0_12181_84059_x730679484}[：运用]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议创建的]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_TIMEWAIT]{lang="EN-US"}]{#struct_0_12181_84059_978326297}[：处于等待状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_ONESBCAST]{lang="EN-US"}]{#struct_0_12181_84059_1670622216}[：发送广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DROPPED]{lang="EN-US"}]{#struct_0_12181_84059_x730351804}[：协议丢弃标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_SOCKREF]{lang="EN-US"}]{#struct_0_12181_84059_x138252874}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DONTBLOCK]{lang="EN-US"}]{#struct_0_12181_84059_x730286268}[：]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步时不能被阻塞]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x1690175308}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Hop limit(minimum hop limit)]{lang="EN-US"}]{#struct_0_12181_84059_x730482876}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_x511194161}[协议控制块中的跳数限制，括号中为最小跳数限制]{style="font-family:宋体"}

[[Connection state]{lang="EN-US"}]{#struct_0_12181_84059_x730417340}

[[TCP]{lang="EN-US"}]{#struct_0_12181_84059_x2103540539}[连接状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_12181_84059_x730089660}[：服务器收到客户端的关闭连接请求回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_12181_84059_630788585}[：服务器在等待连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_SENT]{lang="EN-US"}]{#struct_0_12181_84059_x730024124}[：客户端发出连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_RCVD]{lang="EN-US"}]{#struct_0_12181_84059_x152826044}[：服务器收到客户端连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_12181_84059_1062483815}[：服务器和客户端双方建立连接并能进行双向数据传递的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE_WAIT]{lang="EN-US"}]{#struct_0_12181_84059_x730613947}[：服务器收到客户端关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_1]{lang="EN-US"}]{#struct_0_12181_84059_x730548411}[：客户端发出关闭连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSING]{lang="EN-US"}]{#struct_0_12181_84059_x578844854}[：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAST_ACK]{lang="EN-US"}]{#struct_0_12181_84059_386585963}[：服务器向客户端发出关闭连接请求等待回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_2]{lang="EN-US"}]{#struct_0_12181_84059_x730745019}[：客户端收到服务器关闭连接回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIME_WAIT]{lang="EN-US"}]{#struct_0_12181_84059_x929391699}[：客户端收到服务器的关闭连接请求后所处的状态]{style="font-family:宋体"}

[[TCP options]{lang="EN-US"}]{#struct_0_12181_84059_x1619426814}

[[TCP]{lang="EN-US"}]{#struct_0_12181_84059_x1619492350}[的选项类型，有以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TF_MD5SIG]{lang="EN-US"}]{#struct_0_12181_84059_x1619623422}[：使能密钥]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TF_PASSWORD]{lang="EN-US"}]{#struct_0_12181_84059_x1619688958}[：已经设置密钥]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TF_NODELAY]{lang="EN-US"}]{#struct_0_12181_84059_x1619820030}[：]{lang="EN-US" style="font-family:宋体"}[关]{style="font-family:宋体"}[闭延时]{lang="EN-US" style="font-family:宋体"}[ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TF_NOOPT]{lang="EN-US"}]{#struct_0_12181_84059_x1618902526}[：]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[不使用选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TF_NOPUSH]{lang="EN-US"}]{#struct_0_12181_84059_x1619492351}[：对写入的最后部分不进行]{lang="EN-US" style="font-family:宋体"}[PUSH]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_12181_84059_x1619557887}[F]{lang="EN-US"}[\_BINDFOREIGNADDR]{lang="EN-US"}[：绑定对端]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TF_NSR]{lang="EN-US"}]{#struct_0_12181_84059_x1619688959}[：使能]{lang="EN-US" style="font-family:宋体"}[TCP ]{lang="EN-US"}[NSR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TF_REQ_SCALE]{lang="EN-US"}]{#struct_0_12181_84059_x1619754495}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[使能窗口缩放因子选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TF_REQ_TSTMP]{lang="EN-US"}]{#struct_0_12181_84059_x1618836991}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[使能事件戳选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TF_SACK_PERMIT]{lang="EN-US"}]{#struct_0_12181_84059_x1619361280}[：使能选择性]{lang="EN-US" style="font-family:宋体"}[ACK]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[NSR state]{lang="EN-US"}]{#struct_0_12181_84059_x1619426816}

[[TCP]{lang="EN-US"}]{#struct_0_12181_84059_x1619557888}[连接]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_12181_84059_x1619688960}[：关闭（初始）状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSING]{lang="EN-US"}]{#struct_0_12181_84059_x1619754496}[：]{style="font-family:宋体"}[连接待关闭状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ENABLED]{lang="EN-US"}]{#struct_0_12181_84059_x1618836992}[：]{style="font-family:宋体"}[使能备份功能状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OPEN]{lang="EN-US"}]{#struct_0_12181_84059_x1619361281}[：连接开始同步状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PENDING]{lang="EN-US"}]{#struct_0_12181_84059_x1619426817}[：]{style="font-family:宋体"} [连接判定状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[READY]{lang="EN-US"}]{#struct_0_12181_84059_x1619557889}[：连接备份就绪状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SMOOTH]{lang="EN-US"}]{#struct_0_12181_84059_x1619688961}[：连接平滑状态]{style="font-family:宋体"}

[[角色：]{style="font-family:宋体"}[M]{lang="EN-US"}]{#struct_0_12181_84059_x1619754497}[表示主连接、]{style="font-family:宋体"}[S]{lang="EN-US"}[表示备份连接]{style="font-family:宋体"}

[[Send VRF]{lang="EN-US"}]{#struct_0_12181_84059_x730679483}

[[发送实例]{style="font-family:宋体"}]{#struct_0_12181_84059_978653977}

[[Receive VRF]{lang="EN-US"}]{#struct_0_12181_84059_x730351803}

[[接收实例]{style="font-family:宋体"}]{#struct_0_12181_84059_x138187338}

[ ]{lang="SV"}

::: {#1400107028 .myid}
[]{#_Toc404787008}[]{#struct_0_12181_84059_x730286267}[]{#_Toc279391296}[]{#_Toc249245005}[]{#_Toc233688810}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 udp**

------------------------------------------------------------------------

[**[display ipv6 udp]{lang="EN-US"}**]{#struct_0_12181_84059_x1689716556}[命令用来显示]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1220865892}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_969115037}

[**[display ipv6 udp]{lang="EN-US"}**]{#struct_0_12181_84059_1719891610}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x794325118}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 udp]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_846889907}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_2077900323}[模式：]{style="font-family:宋体"}

[**[display ipv6 udp]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_x1222301893}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x730482875}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x511259697}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1705115088}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_549276958}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_1785081557}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x432477167}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1092057912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_106693465}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1416747754}[：显示指定单板的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x730417339}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_421468652}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x2103081788}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1102043680}[：显示指定单板的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_1811875215}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1852816940}

[[本命令可以用来查看]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}]{#struct_0_12181_84059_1797288550}[连接摘要信息，包括本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号、对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_819835931}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x933340893}[显示]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 udp]{lang="EN-US"}]{#struct_0_12181_84059_x730089659}

[ LAddr-\>port         FAddr-\>port         Chassis  Slot  CPU PCB]{lang="EN-US"}

[ 2001:2002:2003:2   3001:3002:3003:3   1         1      0   0x000000000000c387]{lang="EN-US"}

[ 004:2005:2006:20   004:3005:3006:30]{lang="EN-US"}

[ 07:2008-\>1200      07:3008-\>1200]{lang="EN-US"}

[ 2001::1-\>23         2001::5-\>1284       1         2      0   0x0000000000000008]{lang="EN-US"}

[ 2003::1-\>25         2001::2-\>1283       1         3      0   0x0000000000000009]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[display ipv6 udp]{lang="EN-US"}]{#struct_0_12181_84059_630329832}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_930847757}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_2061413113}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_942777761}

[[LAddr-\>port]{lang="FR"}]{#struct_0_12181_84059_896523501}

[[本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_977646751}[地址及端口号]{style="font-family:宋体"}

[[FAddr-\>port]{lang="FR"}]{#struct_0_12181_84059_x371353294}

[[对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x730024123}[地址及端口号]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_12181_84059_x153153724}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x532442061}[中的成员编号]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_1420217294}

[[单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_12181_84059_68730750}

[[CPU]{lang="EN-US"}]{#struct_0_12181_84059_1812137359}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_12181_84059_1811285391}[编号]{style="font-family:宋体"}

[[PCB]{lang="EN-US"}]{#struct_0_12181_84059_x730613950}

[[协议控制块索引]{style="font-family:宋体"}]{#struct_0_12181_84059_x924952716}

[ ]{lang="EN-US"}

::: {#-364434901 .myid}
[]{#_Toc404787009}[]{#struct_0_12181_84059_x422384908}[]{#_Toc279391297}[]{#_Toc249245007}[]{#_Toc233688812}

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 udp verbose**

------------------------------------------------------------------------

[**[display ipv6 udp verbose]{lang="EN-US"}**]{#struct_0_12181_84059_1909075595}[命令用来显示]{style="font-family:
宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x418682136}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1268651610}

[**[display ipv6 udp verbose]{lang="EN-US"}**[ \[ **pcb** *pcb-index* \]]{lang="EN-US"}]{#struct_0_12181_84059_1201746229}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_1632767169}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 udp verbose]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_x730548414}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x578648246}[模式：]{style="font-family:宋体"}

[**[display ipv6 udp verbose]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_87907820}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1728667776}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1621246211}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1040943743}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1907609037}

[[network-operator]{lang="EN-US"}]{#struct_0_12181_84059_x1756569870}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1167274551}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12181_84059_x730745022}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x929850452}

[**[pcb]{lang="EN-US"}**[ *pcb-index*]{lang="EN-US"}]{#struct_0_12181_84059_874250711}[：显示指定协议控制块索引的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[pcb-index]{lang="EN-US"}*[表示协议控制块索引，取值范围请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_95688211}[：显示指定单板的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_364231066}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1547899816}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1653851408}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x709669980}[：显示指定单板的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_1812006286}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1955503890}

[[本命令可以用来查看]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}]{#struct_0_12181_84059_673040038}[连接详细信息，包括]{style="font-family:宋体"}[socket]{lang="EN-US"}[的创建者、状态、选项、类型、使用的协议号等，以及]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号、目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x730679486}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1604981962}[显示]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 udp verbose]{lang="EN-US"}]{#struct_0_12181_84059_1604916426}

[Total UDP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Creator: sock_test_mips\[250\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 41600 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 2]{lang="EN-US"}

[ Protocol: 17]{lang="EN-US"}

[ Connection info: src = ::-\>69, dst = ::-\>0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1486949370}[显示]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 udp verbose]{lang="EN-US"}]{#struct_0_12181_84059_1605113034}

[Total UDP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Slot: 6 Cpu: 0]{lang="EN-US"}

[ Creator: sock_test_mips\[250\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 41600 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 2]{lang="EN-US"}

[ Protocol: 17]{lang="EN-US"}

[ Connection info: src = ::-\>69, dst = ::-\>0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_978457369}[显示]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 udp verbose]{lang="EN-US"}]{#struct_0_12181_84059_x458481582}

[Total UDP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Chassis: 2 Slot: 6 Cpu: 0]{lang="EN-US"}

[ Creator: sock_test_mips\[250\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 41600 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 2]{lang="EN-US"}

[ Protocol: 17]{lang="EN-US"}

[ Connection info: src = ::-\>69, dst = ::-\>0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV6]{lang="EN-US"}

[ Hop limit: 255 (minimum hop limit: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[[表1-23 ]{lang="EN-US"}]{.FigureDescriptionChar}[display ipv6 udp verbose]{lang="EN-US"}]{#struct_0_12181_84059_131169782}[[命令显示信息描述表]{style="font-family:黑体"}]{.FigureDescriptionChar}

[]{#table_struct_0_924801129}[[字段]{style="font-family:黑体"}]{#struct_0_12181_84059_x730351806}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12181_84059_x138383946}

[[Total UDP socket number]{lang="EN-US"}]{#struct_0_12181_84059_x342403375}

[[IPv6 UDP socket]{lang="EN-US"}]{#struct_0_12181_84059_x1202414408}[总数]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_12181_84059_1771583110}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_465086717}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_x730286270}

[[单板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1689651019}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_12181_84059_1604850890}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x1960828182}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Cpu]{lang="EN-US"}]{#struct_0_12181_84059_1811285390}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_12181_84059_1811219854}[编号]{style="font-family:宋体"}

[[Creator]{lang="EN-US"}]{#struct_0_12181_84059_106995668}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_x405533105}[的任务名称，括号中为创建者的进程号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12181_84059_x290489176}

[[socket]{lang="EN-US"}]{#struct_0_12181_84059_x730482878}[的状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOFDREF]{lang="EN-US"}]{#struct_0_12181_84059_x511587377}[：用户已经关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTED]{lang="EN-US"}]{#struct_0_12181_84059_1795901213}[：连接已经建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTING]{lang="EN-US"}]{#struct_0_12181_84059_1647960809}[：正在建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTING]{lang="EN-US"}]{#struct_0_12181_84059_1590772398}[：正在断开连接]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASYNC]{lang="EN-US"}]{#struct_0_12181_84059_x730417342}[：异步方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTED]{lang="EN-US"}]{#struct_0_12181_84059_x2103671611}[：连接已经断开]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROTOREF]{lang="EN-US"}]{#struct_0_12181_84059_x391356173}[：协议强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x1724510463}[：不处于上述状态]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_12181_84059_1145672776}

[[socket]{lang="EN-US"}]{#struct_0_12181_84059_x730089662}[的选项，有以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DEBUG]{lang="EN-US"}]{#struct_0_12181_84059_630919657}[：记录套接字的调试信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_ACCEPTCONN]{lang="EN-US"}]{#struct_0_12181_84059_x675680453}[：]{lang="EN-US" style="font-family:宋体"}[server]{lang="EN-US"}[端监听连接请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEADDR]{lang="EN-US"}]{#struct_0_12181_84059_1544028869}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[允许本地地址重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVE]{lang="EN-US"}]{#struct_0_12181_84059_x730024126}[：协议需要查询空闲的连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DONTROUTE]{lang="EN-US"}]{#struct_0_12181_84059_x152957116}[：设置不查路由表，由于目的地址是直连网络的情况]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_BROADCAST]{lang="EN-US"}]{#struct_0_12181_84059_653050546}[：套接字支持广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_LINGER]{lang="EN-US"}]{#struct_0_12181_84059_x1546407997}[：套接字关闭但仍发送剩余数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_OOBINLINE]{lang="EN-US"}]{#struct_0_12181_84059_x730613949}[：带外数据采用内联方式存储]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEPORT]{lang="EN-US"}]{#struct_0_12181_84059_x924493965}[：允许本地端口重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMP]{lang="EN-US"}]{#struct_0_12181_84059_418996015}[：入报文记录时间戳，只对非连接的协议有效，时间精确到毫秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_NOSIGPIPE]{lang="EN-US"}]{#struct_0_12181_84059_1638293793}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[不能发送数据导致返回失败时不创建]{lang="EN-US" style="font-family:宋体"}[SIGPIPE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMPNS]{lang="EN-US"}]{#struct_0_12181_84059_x730548413}[：和时戳选项功能类似，时间可以精确到纳秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVETIME]{lang="EN-US"}]{#struct_0_12181_84059_x1619623427}[：设置空闲探测时间，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[支持此选项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_FILTER]{lang="EN-US"}]{#struct_0_12181_84059_x1619688963}[：设置报文过滤条件，]{style="font-family:宋体"}[OSI Socket]{lang="EN-US"}[和]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持此选项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x578713782}[：没有设置选项]{lang="EN-US" style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_12181_84059_437024580}

[[影响]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_1926856215}[连接的错误码]{style="font-family:宋体"}

[[Receiving buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_12181_84059_x730745021}

[[接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态]{style="font-family:宋体"}]{#struct_0_12181_84059_x929915988}

[[状态的取值有：]{style="font-family:宋体"}]{#struct_0_12181_84059_1239852020}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_12181_84059_x730679485}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_12181_84059_978260761}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_12181_84059_849801897}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x650457759}[：不处于上述状态]{style="font-family:宋体"}

[[Sending buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_12181_84059_x730351805}

[[发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态]{style="font-family:宋体"}]{#struct_0_12181_84059_x138318410}

[[状态的取值有：]{style="font-family:宋体"}]{#struct_0_12181_84059_1253017355}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_12181_84059_x730286269}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_12181_84059_x1690109772}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_12181_84059_x1267736424}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_2004366112}[：不处于上述状态]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_12181_84059_x730482877}

[[使用的]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_12181_84059_x511128625}[类型，类型的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_12181_84059_1025799923}[：]{style="font-family:宋体"}[SOCK_STREAM]{lang="EN-US"}[，]{style="font-family:宋体"}[流模式，提供可靠的字节流。]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[协议使用此类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_12181_84059_x730417341}[：]{style="font-family:宋体"}[SOCK_DGRAM]{lang="EN-US"}[，数据报模式的通信。]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议使用此类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_12181_84059_x2103606075}[：]{lang="EN-US" style="font-family:宋体"}[SOCK_RAW]{lang="EN-US"}[，]{style="font-family:宋体"}[RAW]{lang="EN-US"}[模式的通信方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_968968444}[：不是上述类型]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_12181_84059_x730089661}

[[使用]{style="font-family:宋体"}[UDP socket]{lang="EN-US"}]{#struct_0_12181_84059_630854121}[的协议号，]{style="font-family:宋体"}[17]{lang="EN-US"}[表示运用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[Connection info]{lang="EN-US"}]{#struct_0_12181_84059_x1439466950}

[[连接信息，分别为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x730024125}[地址及端口号、目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址及端口号]{style="font-family:宋体"}

[[Inpcb flags]{lang="EN-US"}]{#struct_0_12181_84059_x152760508}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_1820979884}[协议控制块中的标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVOPTS]{lang="EN-US"}]{#struct_0_12181_84059_835469995}[：接收传入的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVRETOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x1209045350}[：接收回应的]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVDSTADDR]{lang="EN-US"}]{#struct_0_12181_84059_x141128255}[：接收目的]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_HDRINCL]{lang="EN-US"}]{#struct_0_12181_84059_835535531}[：用户提供整个]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEADDR]{lang="EN-US"}]{#struct_0_12181_84059_x1551566861}[：重复使用地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEPORT]{lang="EN-US"}]{#struct_0_12181_84059_x1128950739}[：重复使用端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ANONPORT]{lang="EN-US"}]{#struct_0_12181_84059_835338923}[：]{lang="EN-US" style="font-family:宋体"}[用户未指定端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_PROTOCOL_PACKET]{lang="EN-US"}]{#struct_0_12181_84059_x1882296523}[：标识报文为协议报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVVLANID]{lang="EN-US"}]{#struct_0_12181_84059_835404459}[：接收报文的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_IPV6_V6ONLY]{lang="EN-US"}]{#struct_0_12181_84059_1160145975}[：]{style="font-family:宋体"}[仅支持]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议栈]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_PKTINFO]{lang="EN-US"}]{#struct_0_12181_84059_x42231113}[：]{style="font-family:宋体"}[接收报文的源地址和入接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_HOPLIMIT]{lang="EN-US"}]{#struct_0_12181_84059_835732139}[：]{style="font-family:宋体"}[接收报文]{lang="EN-US" style="font-family:宋体"}[hoplimit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_HOPOPTS]{lang="EN-US"}]{#struct_0_12181_84059_266324583}[：]{style="font-family:宋体"}[接收报文的逐跳扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_DSTOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x1533178352}[：]{style="font-family:宋体"}[接收报文的目的扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RTHDR]{lang="EN-US"}]{#struct_0_12181_84059_835797675}[：]{style="font-family:宋体"}[接收报文的路由扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RTHDRDSTOPTS]{lang="EN-US"}]{#struct_0_12181_84059_x1251376094}[：]{style="font-family:宋体"}[接收报文的路由头前的目的扩展头信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_TCLASS]{lang="EN-US"}]{#struct_0_12181_84059_835601067}[：]{style="font-family:宋体"}[接收报文的]{lang="EN-US" style="font-family:宋体"}[优先级]{style="font-family:宋体"}[信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_AUTOFLOWLABEL]{lang="EN-US"}]{#struct_0_12181_84059_1786396317}[：]{style="font-family:宋体"}[使用随机]{lang="EN-US" style="font-family:宋体"}[流标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_RFC2292]{lang="EN-US"}]{#struct_0_12181_84059_1773953225}[：使用]{style="font-family:宋体"}[RFC2292 API]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN6P_MTU]{lang="EN-US"}]{#struct_0_12181_84059_835666603}[：]{style="font-family:宋体"}[感知路径]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[的变化]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[不支持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVMACADDR]{lang="EN-US"}]{#struct_0_12181_84059_1452442297}[：接收报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SYNCPCB]{lang="EN-US"}]{#struct_0_12181_84059_835994283}[：阻塞等待]{style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x1896130932}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb extflag]{lang="EN-US"}]{#struct_0_12181_84059_x1931575194}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_1276195875}[协议控制块中的扩展标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_EXTRCVPVCIDX]{lang="EN-US"}]{#struct_0_12181_84059_x1931575191}[：接收报文时记录报文的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVPWID]{lang="EN-US"}]{#struct_0_12181_84059_872911348}[：接收报文时记录报文的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x453596320}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb vflag]{lang="EN-US"}]{#struct_0_12181_84059_836059819}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_214878255}[协议控制块中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[版本标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_IPV4]{lang="EN-US"}]{#struct_0_12181_84059_835469996}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV6]{lang="EN-US"}]{#struct_0_12181_84059_x1209045349}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV6PROTO]{lang="EN-US"}]{#struct_0_12181_84059_1781120510}[：运用]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议创建的]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_TIMEWAIT]{lang="EN-US"}]{#struct_0_12181_84059_835535532}[：处于等待状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_ONESBCAST]{lang="EN-US"}]{#struct_0_12181_84059_x1551566862}[：发送广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_DROPPED]{lang="EN-US"}]{#struct_0_12181_84059_835338924}[：协议丢弃标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_SOCKREF]{lang="EN-US"}]{#struct_0_12181_84059_x1882296516}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_DONTBLOCK]{lang="EN-US"}]{#struct_0_12181_84059_835404460}[：]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步时不能被阻塞]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_12181_84059_x1560843218}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Hop limit(minimum hop limit)]{lang="EN-US"}]{#struct_0_12181_84059_835732140}

[[Internet]{lang="EN-US"}]{#struct_0_12181_84059_x2072327584}[协议控制块中的跳数限制，括号中为最小跳数限制]{style="font-family:宋体"}

[[Send VRF]{lang="EN-US"}]{#struct_0_12181_84059_x2141442011}

[[发送实例]{style="font-family:宋体"}]{#struct_0_12181_84059_835797676}

[[Receive VRF]{lang="EN-US"}]{#struct_0_12181_84059_x1251376091}

[[接收实例]{style="font-family:宋体"}]{#struct_0_12181_84059_835601068}

[ ]{lang="EN-US"}

::: {#-1250635572 .myid}
[]{#_Toc404787010}[]{#struct_0_12181_84059_1786396322}[]{#_Toc138417083}[]{#_Toc137020664}[]{#_Toc59352346}[]{#_Toc189458191}[]{#_Toc189477191}[]{#_Toc189458193}[]{#_Toc189477193}[]{#_Toc189458194}[]{#_Toc189477194}[]{#_Toc189458195}[]{#_Toc189477195}[]{#_Toc189458196}[]{#_Toc189477196}[]{#_Toc189458197}[]{#_Toc189477197}[]{#_Toc189458198}[]{#_Toc189477198}[]{#_Toc189458199}[]{#_Toc189477199}[]{#_Toc189458200}[]{#_Toc189477200}[]{#_Toc189458201}[]{#_Toc189477201}[]{#_Toc189458202}[]{#_Toc189477202}[]{#_Hlt25138928}[]{#_Toc189458203}[]{#_Toc189477203}[]{#_Toc189458204}[]{#_Toc189477204}[]{#_Toc189458205}[]{#_Toc189477205}[]{#_Toc189458212}[]{#_Toc189477212}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address**

------------------------------------------------------------------------

[**[ipv6 address]{lang="EN-US"}**]{#struct_0_12181_84059_1773756616}[命令用来手工配置接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址。]{style="font-family:宋体"}

[**[undo ipv6 address]{lang="EN-US"}**]{#struct_0_12181_84059_x112201658}[命令用来删除接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1999723867}

[]{#OLE_LINK2}[**[ipv6 address]{lang="EN-US"}**[ { *ipv6-address prefix-length* \| *ipv6-address***/***prefix-length* }]{lang="EN-US"}]{#struct_0_12181_84059_x869205375}

[**[undo ipv6 address]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *ipv6-address prefix-length* \| *ipv6-address***/***prefix-length* \]]{lang="EN-US"}]{#struct_0_12181_84059_835666604}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_1452442298}

[[接口上没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x596165794}[全球单播地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1874033815}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1505944548}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x320452244}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x397284718}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x924256274}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1556473991}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12181_84059_835994284}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_12181_84059_x1896130929}[：前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1046199948}

[[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x726115026}[全球单播地址等同于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[公网地址，提供给网络服务提供商。这种类型的地址允许路由前缀的聚合，从而限制了全球路由表项的数量。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}**[undo ipv6 address]{lang="EN-US"}**]{#struct_0_12181_84059_x265379067}[命令不带参数则删除该接口的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2143817556}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1670175841}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1856672444}[指定]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[，前缀长度为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[方法一：]{style="font-family:宋体"}]{#struct_0_12181_84059_836059820}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_1788856376}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address 2001::1/64]{lang="EN-US"}

[[方法二：]{style="font-family:宋体"}]{#struct_0_12181_84059_1583046566}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x2132057939}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address 2001::1 64]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x676213823}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1484093045}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[，前缀长度为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[方法一：]{style="font-family:宋体"}]{#struct_0_12181_84059_x489028901}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_835469993}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address 2001::1/64]{lang="EN-US"}

[[方法二：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1209045352}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1303927669}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address 2001::1 64]{lang="EN-US"}
:::

::: {#1187562177 .myid}
[]{#_Toc404787011}[]{#struct_0_12181_84059_1709806914}[]{#_Toc296959529}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address anycast**

------------------------------------------------------------------------

[**[ipv6 address anycast]{lang="EN-US"}**]{#struct_0_12181_84059_1355222040}[命令用来给接口配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[任播地址。]{style="font-family:宋体"}

[**[undo ipv6 address anycast]{lang="EN-US"}**]{#struct_0_12181_84059_x6210527}[命令用来删除接口上已配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[任播地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2017063987}

[**[ipv6 address]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *ipv6-address prefix-length* \| *ipv6-address/prefix-length* } **anycast**]{lang="EN-US"}]{#struct_0_12181_84059_835535529}

[**[undo ipv6 address]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *ipv6-address prefix-length* \| *ipv6-address/prefix-length* } **anycast**]{lang="EN-US"}]{#struct_0_12181_84059_787085307}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1162440411}

[[接口上没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x132725132}[任播地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_2117770162}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x213387125}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_2040678105}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1569578095}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_835338921}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1882296521}

[*[ipv6-addres]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_12181_84059_x1333972334}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[任播地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_12181_84059_514453993}[：前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1185854295}

[]{#_Toc296959530}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1244283791}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x742535308}[指定]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[任播地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[，前缀长度为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[方法一：]{style="font-family:宋体"}]{#struct_0_12181_84059_1633792861}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_835404457}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address 2001::1/64 anycast]{lang="EN-US"}

[[方法二：]{style="font-family:宋体"}]{#struct_0_12181_84059_1160145969}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x41444682}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address 2001::1 64 anycast]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_647543765}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1448124918}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[任播地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[，前缀长度为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[方法一：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1244376724}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x218695257}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address 2001::1/64 anycast]{lang="EN-US"}

[[方法二：]{style="font-family:宋体"}]{#struct_0_12181_84059_835732137}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_266324577}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address 2001::1 64 anycast]{lang="EN-US"}
:::

::::: {#-1206463539 .myid}
[]{#_Toc404787012}[]{#struct_0_12181_84059_x1960145396}[]{#_Toc296959531}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address auto**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_12181_84059_35983184}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_12181_84059_x1119247403}
:::

[ ]{lang="EN-US"}

[**[ipv6 address auto]{lang="EN-US"}**]{#struct_0_12181_84059_1209946848}[命令用来使能无状态地址自动配置功能，使接口通过无状态自动配置方式生成全球单播地址。]{style="font-family:宋体"}

[**[undo ipv6 address auto]{lang="EN-US"}**]{#struct_0_12181_84059_x113701891}[命令用来关闭无状态地址自动配置功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_835797673}

[**[ipv6 address auto]{lang="EN-US"}**]{#struct_0_12181_84059_x1251376096}

[**[undo ipv6 address auto]{lang="EN-US"}**]{#struct_0_12181_84059_913802372}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_1294575424}

[[无状态地址自动配置功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12181_84059_x234113575}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1890429274}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1244799281}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1098711783}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1172743884}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_835601065}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1786396319}

[[通过无状态自动配置方式生成全球单播地址时，会自动生成链路本地地址，生成的全球单播地址和链路本地地址可以通过执行]{style="font-family:宋体"}**[undo ipv6 address auto]{lang="EN-US"}**]{#struct_0_12181_84059_1773297865}[命令或]{style="font-family:宋体"}**[undo ipv6 address]{lang="EN-US"}**[命令删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x433357743}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x303725467}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1673345162}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[通过无状态自动配置方式生成全球单播地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_2096927484}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address auto]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_835666601}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1452442295}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[通过无状态自动配置方式生成全球单播地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x595444898}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address auto]{lang="EN-US"}
:::::

::: {#-1946383737 .myid}
[]{#_Toc404787013}[]{#struct_0_12181_84059_646445209}[]{#_Toc296959533}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address auto link-local**

------------------------------------------------------------------------

[**[ipv6 address auto link-local]{lang="EN-US"}**]{#struct_0_12181_84059_28122882}[命令用来配置系统自动为接口生成链路本地地址。]{style="font-family:宋体"}

[**[undo ipv6 address auto link-local]{lang="EN-US"}**]{#struct_0_12181_84059_1378130397}[命令用来删除接口自动生成的链路本地地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1389087519}

[**[ipv6 address auto link-local]{lang="EN-US"}**]{#struct_0_12181_84059_580700593}

[**[undo ipv6 address auto link-local]{lang="EN-US"}**]{#struct_0_12181_84059_835994281}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1896130934}

[[接口上没有链路本地地址。当接口配置了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_642849885}[全球单播地址后，会自动生成链路本地地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2139505996}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_511175674}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x239411718}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1361407479}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_196248450}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_836059817}

[[链路本地地址用于邻居发现协议和无状态自动配置中链路本地上节点之间的通信。使用链路本地地址作为源或目的地址的数据报文不会被转发到其他链路上。]{style="font-family:宋体"}]{#struct_0_12181_84059_214878261}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_12181_84059_2046250495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口配置了]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_447559452}[全球单播地址后，所自动生成的链路本地地址与采用]{lang="EN-US" style="font-family:宋体"}**[ipv6 address auto link-local]{lang="EN-US"}**[命令生成的链路本地地址相同。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[undo ipv6 address auto link-local]{lang="EN-US"}**]{#struct_0_12181_84059_1678963349}[命令只能删除使用]{lang="EN-US" style="font-family:宋体"}**[ipv6 address auto link-local]{lang="EN-US"}**[命令生成的链路本地地址。即如果此时接口已配置了]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址，则接口仍有链路本地地址；如果此时接口没有配置任何]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址，则接口没有链路本地地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置链路本地地址时，手工指定方式的优先级高于自动生成方式。即如果先采用自动生成方式，之后手工指定，则手工指定的地址会覆盖自动生成的地址；如果先手工指定，之后采用自动生成的方式，则自动配置不生效，接口的链路本地地址仍是手工指定的。此时，如果删除手工指定的地址，则自动生成的链路本地地址会生效。]{style="font-family:宋体"}]{#struct_0_12181_84059_1287366782}[关于手工指定方式的介绍请参见命令]{lang="EN-US" style="font-family:宋体"}**[ipv6 address link-local]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1126064323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_157049206}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_556473782}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口自动生成链路本地地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_835469994}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address auto link-local]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1209045351}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1424955686}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[自动生成链路本地地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_214422768}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address auto link-local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1160318956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 address link-local]{lang="EN-US"}**]{#struct_0_12181_84059_x553681409}
:::

::: {#-914660689 .myid}
[]{#_Toc404787014}[]{#struct_0_12181_84059_835535530}[]{#_Toc138417085}[]{#_Toc137020666}[]{#_Toc59352347}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address eui-64**

------------------------------------------------------------------------

[**[ipv6 address]{lang="EN-US"}**[ **eui-64**]{lang="EN-US"}]{#struct_0_12181_84059_x1551566860}[命令用来给接口配置]{style="font-family:宋体"}[EUI-64]{lang="EN-US"}[格式的全球单播地址。]{style="font-family:宋体"}

[**[undo ipv6 address eui-64]{lang="EN-US"}**]{#struct_0_12181_84059_1599932616}[命令用来删除接口上已配置的]{style="font-family:
宋体"}[EUI-64]{lang="EN-US"}[格式的全球单播地址。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x839618994}

[**[ipv6 address]{lang="EN-US"}**[ { *ipv6-address prefix-length* \| *ipv6-address***/***prefix-length* } **eui-64**]{lang="EN-US"}]{#struct_0_12181_84059_x1584887884}

[**[undo ipv6 address]{lang="EN-US"}**[ \[ *ipv6-address prefix-length* \| *ipv6-address***/***prefix-length* \] **eui-64**]{lang="EN-US"}]{#struct_0_12181_84059_x922447610}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_902859964}

[[接口上没有配置]{style="font-family:宋体"}[EUI-64]{lang="EN-US"}]{#struct_0_12181_84059_x1801491756}[格式的全球单播地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_835338922}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1882296522}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x930687807}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x346716924}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_949966289}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1285459156}

[*[ipv6-address]{lang="EN-US"}***[/]{lang="EN-US"}***[prefix-length]{lang="EN-US"}*]{#struct_0_12181_84059_x1086437716}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀长度，共同指定采用]{style="font-family:宋体"}[EUI-64]{lang="EN-US"}[格式形成的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的前缀。前缀长度]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1110365285}

[[EUI-64]{lang="EN-US"}]{#struct_0_12181_84059_835404458}[格式的地址由指定的地址前缀和自动产生的接口标识符生成，最终生成的地址可以通过]{style="font-family:宋体"}**[display ipv6 interface]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[[需要注意的是，在配置]{style="font-family:宋体"}[EUI-64]{lang="EN-US"}]{#struct_0_12181_84059_1160145974}[地址时前缀长度取值不能大于]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x42296649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1523194000}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1676566868}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口采用]{style="font-family:宋体"}[EUI-64]{lang="EN-US"}[格式形成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，其地址前缀与]{style="font-family:宋体"}[2001::1/64]{lang="EN-US"}[的前缀相同，接口标识符由设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址生成。]{style="font-family:宋体"}

[[方法一：]{style="font-family:宋体"}]{#struct_0_12181_84059_x2036797437}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_715114085}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address 2001::1/64 eui-64]{lang="EN-US"}

[[方法二：]{style="font-family:宋体"}]{#struct_0_12181_84059_x773059735}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_835732138}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address 2001::1 64 eui-64]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_266324584}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1533178357}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[采用]{style="font-family:宋体"}[EUI-64]{lang="EN-US"}[格式形成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，其地址前缀与]{style="font-family:宋体"}[2001::1/64]{lang="EN-US"}[的前缀相同，接口标识符由设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址生成。]{style="font-family:宋体"}

[[方法一：]{style="font-family:宋体"}]{#struct_0_12181_84059_1932601274}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1316642761}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address 2001::1/64 eui-64]{lang="EN-US"}

[[方法二：]{style="font-family:宋体"}]{#struct_0_12181_84059_2097547990}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_835797674}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address 2001::1 64 eui-64]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1251376093}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 interface]{lang="EN-US"}**]{#struct_0_12181_84059_510517845}
:::

::: {#-1105385295 .myid}
[]{#_Toc404787015}[]{#struct_0_12181_84059_1675605916}[]{#_Toc138417086}[]{#_Toc137020667}[]{#_Toc59352348}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address link-local**

------------------------------------------------------------------------

[**[ipv6 address link-local]{lang="EN-US"}**]{#struct_0_12181_84059_826446486}[命令用来手动配置指定接口的链路本地地址。]{style="font-family:宋体"}

[**[undo ipv6 address link-local]{lang="EN-US"}**]{#struct_0_12181_84059_x210813097}[命令用来删除接口上手动配置的链路本地地址。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1017214295}

[**[ipv6 address]{lang="EN-US"}**[ *ipv6-address* **link-local**]{lang="EN-US"}]{#struct_0_12181_84059_x8071222}

[**[undo ipv6 address ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[ **link-local**]{lang="EN-US"}]{#struct_0_12181_84059_x890623636}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_835601066}

[[接口上没有手动配置的链路本地地址。]{style="font-family:宋体"}]{#struct_0_12181_84059_1786396316}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1774018761}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x2127523788}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_240663602}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1129906399}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1971697268}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1351733297}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12181_84059_835666602}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路本地地址，地址前面]{style="font-family:宋体"}[10]{lang="EN-US"}[位必须为]{style="font-family:宋体"}[1111111010]{lang="EN-US"}[（二进制标识），即地址最前面的一组十六进制数为]{style="font-family:宋体"}[FE80]{lang="EN-US"}[～]{style="font-family:宋体"}[FEBF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1452442296}

[[配置链路本地地址时，手工指定方式的优先级高于自动生成方式。即如果先采用自动生成方式，之后手工指定，则手工指定的地址会覆盖自动生成的地址；如果先手工指定，之后采用自动生成的方式，则自动配置不生效，接口的链路本地地址仍是手工指定的。此时，如果删除手工指定的地址，则自动生成的链路本地地址会生效。关于自动生成方式的介绍请参见命令]{style="font-family:宋体"}**[ipv6 address auto link-local]{lang="EN-US"}**]{#struct_0_12181_84059_x595510434}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_600122886}

[]{#_Toc59352320}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x942036227}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_638670026}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的链路本地地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1456187164}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address fe80::1 link-local]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1991048511}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_835994282}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[的链路本地地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1896130931}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address fe80::1 link-local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1402364772}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 address auto link-local]{lang="EN-US"}**]{#struct_0_12181_84059_x571738504}
:::

::: {#401584796 .myid}
[]{#_Toc404787016}[]{#struct_0_12181_84059_1596555364}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 bandwidth-based-sharing**

------------------------------------------------------------------------

[**[ipv6 bandwidth-based-sharing]{lang="EN-US"}**]{#struct_0_12181_84059_1646114264}[命令用来配置]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[基于带宽的负载分担功能。]{style="font-family:宋体"}

[**[undo ipv6 bandwidth-based-sharing]{lang="EN-US"}**]{#struct_0_12181_84059_1614442832}[命令用来关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基于带宽的负载分担功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1817502867}

[**[ipv6 bandwidth-based-sharing]{lang="EN-US"}**]{#struct_0_12181_84059_x1788428395}

[**[undo ipv6 bandwidth-based-sharing]{lang="EN-US"}**]{#struct_0_12181_84059_x141261318}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_231834950}

[[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1014245438}[基于带宽的负载分担功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1647338293}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_25422023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_298404480}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1596555367}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1646179800}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_831741225}

[[在设备上配置了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_442905873}[基于带宽的负载分担后，如果]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文转发时查到多个出接口]{style="font-family:宋体"}[/]{lang="EN-US"}[下一跳，则按照接口的带宽值计算出各个接口应该分配的报文比例，然后按照带宽比例对报文进行转发。]{style="font-family:宋体"}

[[支持负载分担协议（如]{style="font-family:宋体"}[LISP]{lang="EN-US"}]{#struct_0_12181_84059_x1284914252}[）的设备，无论是否配置了负载分担命令，负载分担比例都以协议定义的负载分担比例为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2016885444}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1280969797}[配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基于带宽的负载分担功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_1130579479}

[\[Sysname\] ipv6 bandwidth-based-sharing]{lang="EN-US"}
:::

::: {#-812676521 .myid}
[]{#_Toc404787017}[]{#struct_0_12181_84059_1033395657}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 hop-limit**

------------------------------------------------------------------------

[**[ipv6 hop-limit]{lang="EN-US"}**]{#struct_0_12181_84059_1131400756}[命令用来配置设备的跳数限制。]{style="font-family:宋体"}

[**[undo ipv6 hop-limit]{lang="EN-US"}**]{#struct_0_12181_84059_x1670441838}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_836059818}

[**[ipv6 hop-limit]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_12181_84059_214878256}

[**[undo ]{lang="EN-US"}[ipv6 hop-limit]{lang="EN-US"}**]{#struct_0_12181_84059_472272390}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x799441646}

[[设备的跳数限制为]{style="font-family:宋体"}[64]{lang="EN-US"}]{#struct_0_12181_84059_1740681613}[跳。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x148719569}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_438708962}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_153825840}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_977254964}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_835469991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1209045354}

[*[value]{lang="EN-US"}*]{#struct_0_12181_84059_x2110496723}[：跳数值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_424442239}

[[设备的跳数限制有以下两个作用：]{style="font-family:宋体"}]{#struct_0_12181_84059_77415962}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[决定了设备发送的]{style="font-family:宋体"}]{#struct_0_12181_84059_441481134}[IPv6]{lang="EN-US"}[数据报文的跳数，即]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据报文的]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}[字段的值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备发送的]{style="font-family:宋体"}]{#struct_0_12181_84059_235043355}[RA]{lang="EN-US"}[消息中将携带此处配置的跳数限制值。收到该]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息之后，主机在]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文时，将使用该跳数值填充]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文头中的]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}[字段。配置命令]{style="font-family:宋体"}**[ipv6 nd ra hop-limit unspecified]{lang="EN-US"}**[可以]{style="font-family:
宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[RA]{lang="EN-US"}[消息中不指定跳数限制]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1808972608}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_835535527}[配置设备的跳数限制为]{style="font-family:宋体"}[100]{lang="EN-US"}[跳。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_787085301}

[\[Sysname\] ipv6 hop-limit 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1162440413}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd hop-limit]{lang="EN-US"}***[ ]{lang="EN-US"}***[unspecified]{lang="EN-US"}**]{#struct_0_12181_84059_x1295524546}
:::

::: {#-279370498 .myid}
[]{#_Toc233688807}[]{#_Toc404787018}[]{#struct_0_12181_84059_1723300039}[]{#_Toc279391298}[]{#_Toc267662126}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 hoplimit-expires enable**

------------------------------------------------------------------------

[**[ipv6 hoplimit-expires enable]{lang="EN-US"}**]{#struct_0_12181_84059_x413387777}[命令用来开启设备的]{style="font-family:
宋体"}[ICMPv6]{lang="EN-US"}[超时报文的发送功能。]{style="font-family:
宋体"}

[**[undo ipv6 hoplimit-expires enable]{lang="EN-US"}**]{#struct_0_12181_84059_x2021636386}[命令用来关闭设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[超时报文的发送功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_2025051038}

[**[ipv6 hoplimit-expires enable]{lang="EN-US"}**]{#struct_0_12181_84059_835338919}

[**[undo ipv6 hoplimit-expires enable]{lang="EN-US"}**]{#struct_0_12181_84059_456355647}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x874448236}

[[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_197025192}[超时报文发送功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1730035540}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_176226594}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x209937640}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_713904020}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_835404455}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1160145971}

[[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_x41968969}[超时报文发送功能是在设备收到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据报文后，如果发生超时（]{style="font-family:宋体"}[Hop limit]{lang="EN-US"}[超时或者重组超时）差错，则将报文丢弃并给源端发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[超时差错报文。]{style="font-family:宋体"}

[[如果接收到大量需要发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_x116980957}[差错报文的恶意攻击报文，设备会因为处理大量该类报文而导致性能降低。为了避免该现象发生，可以关闭设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[超时报文发送功能，从而减少网络流量、防止遭到恶意攻击。]{style="font-family:宋体"}

[[需要注意的是，关闭]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_2144260863}[超时报文发送功能后，设备不会再发送"]{style="font-family:宋体"}[Hop-Limit]{lang="EN-US"}[超时"]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[差错报文，但"重组超时"]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[差错报文仍会正常发送。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1977169677}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1843534712}[关闭设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[超时报文发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_452096200}

[\[Sysname\] undo ipv6 hoplimit-expires enable]{lang="EN-US"}
:::

::: {#124122290 .myid}
[]{#_Toc404787019}[]{#struct_0_12181_84059_835732135}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 icmpv6 error-interval**

------------------------------------------------------------------------

[**[ipv6 icmpv6 error-interval]{lang="EN-US"}**]{#struct_0_12181_84059_266324579}[命令用来配置发送]{style="font-family:
宋体"}[ICMPv6]{lang="EN-US"}[差错报文对应的令牌桶容量和令牌刷新周期。]{style="font-family:宋体"}

[**[undo ipv6 icmpv6 error-interval]{lang="EN-US"}**]{#struct_0_12181_84059_x1960145386}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_36048720}

[**[ipv6 icmpv6 ]{lang="EN-US"}[error-interval]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_12181_84059_x1587664211}*[milliseconds ]{lang="EN-US"}*[\[ ]{lang="EN-US"}*[bucketsize ]{lang="EN-US"}*[\]]{lang="EN-US"}

[**[undo ipv6 icmpv6 ]{lang="EN-US"}[error-interval]{lang="EN-US"}**]{#struct_0_12181_84059_1355942264}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_388840118}

[[令牌桶容量为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_12181_84059_386393095}[，令牌刷新周期为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_582765096}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_835797671}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1251376098}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_463463678}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_2145064863}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_435578095}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_12181_84059_1567428726}[：令牌刷新周期，取值范围]{style="font-family:宋体"}[0\~2147483647]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为毫秒。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示不限制]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[差错报文的发送。]{style="font-family:宋体"}

[*[bucketsize]{lang="EN-US"}*]{#struct_0_12181_84059_157462129}[：令牌桶中容纳的令牌数，取值范围]{style="font-family:宋体"}[1\~200]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1136771122}

[[如果网络中短时间内发送的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_835601063}[差错报文过多，将可能导致网络拥塞。为了避免这种情况，用户可以控制在指定时间内发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[差错报文的最大个数，目前采用令牌桶算法来实现。]{style="font-family:宋体"}

[[用户可以设置令牌桶的容量，即令牌桶中可以同时容纳的令牌数；同时可以设置令牌桶的刷新周期，即每隔多长时间发放一个令牌到令牌桶中，直到令牌桶中的令牌数达到配置的容量。一个令牌表示允许发送一个]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_1786396313}[差错报文，每当发送一个]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[差错报文，则令牌桶中减少一个令牌。如果连续发送的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[差错报文超过了令牌桶的容量，则后续的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[差错报文将不能被发送出去，直到按照所设置的刷新频率将新的令牌放入令牌桶中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1773691081}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1902297137}[配置设备发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[差错报文对应的令牌桶容量为]{style="font-family:宋体"}[40]{lang="EN-US"}[，令牌刷新时间为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_1963033082}

[\[Sysname\] ipv6 icmpv6 error-interval 200 40]{lang="EN-US"}
:::

::: {#-2113469444 .myid}
[]{#_Toc233688806}[]{#_Toc404787020}[]{#struct_0_12181_84059_x452021867}[]{#_Toc279391299}[]{#_Toc267662128}[]{#_Toc279579810}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 icmpv6 multicast-echo-reply enable**

------------------------------------------------------------------------

[**[ipv6 icmpv6 multicast-echo-reply enable]{lang="EN-US"}**]{#struct_0_12181_84059_208370952}[命令用来配置允许设备回复组播形式的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo ipv6 icmpv6 multicast-echo-reply enable]{lang="EN-US"}**]{#struct_0_12181_84059_x438879593}[命令用来配置不允许设备回复组播形式的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_835666599}

[**[ipv6 icmpv6 multicast-echo-reply enable]{lang="EN-US"}**]{#struct_0_12181_84059_695662426}

[**[undo ipv6 icmpv6 multicast-echo-reply enable]{lang="EN-US"}**]{#struct_0_12181_84059_x652921868}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_75005520}

[[不允许设备回复组播形式的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}]{#struct_0_12181_84059_x2125518290}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x228997678}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_831163677}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x377813079}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x425625701}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_835994279}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1851500926}

[[如果主机]{style="font-family:宋体"}[B]{lang="EN-US"}]{#struct_0_12181_84059_2105398698}[允许回复组播形式的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文，则主机]{style="font-family:宋体"}[A]{lang="EN-US"}[可以构造目的地址为组播地址、源地址为主机]{style="font-family:宋体"}[B]{lang="EN-US"}[的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文，使该组播组中所有的主机都向主机]{style="font-family:宋体"}[B]{lang="EN-US"}[发送]{style="font-family:宋体"}[Echo reply]{lang="EN-US"}[报文，从而达到攻击主机]{style="font-family:宋体"}[B]{lang="EN-US"}[的目的。因此，为了避免主机利用设备达到攻击的目的，缺省情况下，不允许设备回复组播形式的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[但在某些应用场景下，可能需要使用组播形式的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}]{#struct_0_12181_84059_2044443557}[报文来获取信息，此时可以配置允许设备回复组播形式的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x209206469}

[]{#_Toc233688805}[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1894767088}[配置允许设备回复组播形式的]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1528705825}

[\[Sysname\] ipv6 icmpv6 multicast-echo-reply enable]{lang="EN-US"}
:::

::: {#-1011367842 .myid}
[]{#_Toc404787021}[]{#struct_0_12181_84059_836059815}[]{#_Toc347133723}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 icmpv6 source**

------------------------------------------------------------------------

[**[ipv6 icmpv6 source]{lang="EN-US"}**]{#struct_0_12181_84059_214878259}[命令用来配置]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文指定源地址功能。]{style="font-family:宋体"}

[**[undo ipv6 icmpv6 source]{lang="EN-US"}**]{#struct_0_12181_84059_472272375}[命令用来关闭]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文指定源地址功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_347569431}

[**[ipv6 icmpv6 source ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] *ipv6-address*]{lang="EN-US"}]{#struct_0_12181_84059_1296629554}

[**[undo ipv6 icmpv6 source ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12181_84059_x298828045}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x75267635}

[[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_x962054355}[报文指定源地址功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x92212537}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_835469992}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1209045353}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_262156272}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x2020339531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1997459190}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12181_84059_120947659}[：指定地址所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。如果不指定本参数，则表示公网内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12181_84059_x448590685}[：表示设备发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文时指定的源地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1160179401}

[[在网络中]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_835535528}[地址配置较多的情况下，收到]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文时，用户很难根据报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址判断报文来自哪台设备。为了简化这一判断过程，可以配置]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文指定源地址功能。用可配置特定地址（如环回口地址）为]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的源地址，可以简化判断。]{style="font-family:宋体"}

[[设备发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_787085308}[差错报文（]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时、报文过大、端口不可达和参数错误等）和]{style="font-family:宋体"}[ping echo request]{lang="EN-US"}[报文时，都可以通过上述命令指定报文的源地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1162440420}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1699005681}[配置设备发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文时指定的源地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1221634439}

[\[Sysname\] ipv6 icmpv6 source 1::1]{lang="EN-US"}
:::

::: {#-75676253 .myid}
[]{#_Toc59352308}[]{#_Toc59352305}[]{#_Toc279579811}[]{#_Toc138417092}[]{#_Toc137020673}[]{#_Toc59352321}[]{#_Toc52166659}[]{#_Toc404787022}[]{#struct_0_12181_84059_174504758}[]{#_Toc298765621}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 mtu**

------------------------------------------------------------------------

[**[ipv6 mtu]{lang="EN-US"}**]{#struct_0_12181_84059_1521155270}[命令用来配置接口上发送]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ipv6 mtu]{lang="PT-BR"}**]{#struct_0_12181_84059_248894964}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_835338920}

[**[ipv6 mtu]{lang="PT-BR"}**]{#struct_0_12181_84059_x1882296520}[ *mtu-size*]{lang="PT-BR"}

[**[undo ipv6 mtu]{lang="PT-BR"}**]{#struct_0_12181_84059_232111607}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1564394047}

[[没有配置接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_12181_84059_1211982403}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x544924984}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1713454926}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x383396082}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x445829689}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_835404456}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1160145968}

[*[mtu-size]{lang="EN-US"}*]{#struct_0_12181_84059_x41510218}[：接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[的大小，取值范围为]{style="font-family:宋体"}[1280]{lang="EN-US"}[～]{style="font-family:宋体"}[10240]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1712002852}

[[由于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1482507300}[路由器不支持对报文进行分片，当路由器接口收到一个报文后，如果发现报文长度比转发接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值大，则会将其丢弃；同时将转发接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值通过]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的"]{style="font-family:宋体"}[Packet Too Big]{lang="EN-US"}["消息发给源端主机，源端主机以该值重新发送]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文。为减少报文被丢弃带来的额外流量开销，需要根据实际组网环境设置合适的接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_2117122906}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_168169229}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1565822466}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上发送]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[为]{style="font-family:宋体"}[1280]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_835732136}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 mtu 1280]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_266324578}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1960145385}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上发送]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[为]{style="font-family:宋体"}[1280]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1530035221}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 mtu 1280]{lang="EN-US"}
:::

::: {#1398277361 .myid}
[]{#_Toc404787023}[]{#struct_0_12181_84059_x1261609492}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd autoconfig managed-address-flag**

------------------------------------------------------------------------

[**[ipv6 nd autoconfig managed-address-flag]{lang="EN-US"}**]{#struct_0_12181_84059_161811091}[命令用来配置被管理地址的配置标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，即主机通过有状态自动配置（例如]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器）获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 nd autoconfig managed-address-flag**]{lang="EN-US"}]{#struct_0_12181_84059_1303774468}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_835797672}

[**[ipv6 nd autoconfig managed-address-flag]{lang="EN-US"}**]{#struct_0_12181_84059_x1251376095}

[**[undo ipv6 nd autoconfig managed-address-flag]{lang="EN-US"}**]{#struct_0_12181_84059_x652281569}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1145668283}

[[被管理地址的配置标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_12181_84059_574362836}[，即主机通过无状态自动配置获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1226430577}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1356582055}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_462324362}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x219644691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_835601064}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1786396318}

[[被管理地址配置标志位（]{style="font-family:宋体"}[M flag]{lang="EN-US"}]{#struct_0_12181_84059_1773363401}[）用于确定主机是否采用有状态自动配置获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[如果设置该标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_12181_84059_x495277628}[，主机将通过有状态自动配置（例如]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器）来获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址；否则，将通过无状态自动配置获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，即]{style="font-family:宋体"}[根据自己的链路层地址及路由器发布的前缀信息生成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x365454820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_373158834}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x963726887}[配置主机通过有状态自动配置获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_835666600}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd autoconfig managed-address-flag]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1452442294}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x595379362}[配置主机通过有状态自动配置获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x897905558}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd autoconfig managed-address-flag]{lang="EN-US"}
:::

::: {#-1601089149 .myid}
[]{#_Toc404787024}[]{#struct_0_12181_84059_1889436760}[]{#_Toc279579812}[]{#_Toc138417093}[]{#_Toc137020674}[]{#_Toc59352322}[]{#_Toc52166660}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd autoconfig other-flag**

------------------------------------------------------------------------

[**[ipv6 nd autoconfig other-flag]{lang="EN-US"}**]{#struct_0_12181_84059_x1161469918}[命令用来配置其他信息配置标志位为]{style="font-family:
宋体"}[1]{lang="EN-US"}[，即主机通过有状态自动配置（例如]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[服务器）获取除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址外的其他信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ipv6 nd autoconfig other-flag]{lang="EN-US"}**]{#struct_0_12181_84059_x835484067}[命令用来恢复该缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x17035219}

[**[ipv6 nd autoconfig other-flag]{lang="EN-US"}**]{#struct_0_12181_84059_835994280}

[**[undo ipv6 nd autoconfig other-flag]{lang="EN-US"}**]{#struct_0_12181_84059_x1896130933}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1729803110}

[[其他信息配置标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_12181_84059_1642582966}[，即主机通过无状态自动配置获取其他信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1647748614}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_397350998}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1406004369}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x89021749}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1482725909}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_836059816}

[[其他信息配置标志位（]{style="font-family:宋体"}[O flag]{lang="EN-US"}]{#struct_0_12181_84059_214878262}[）用于确定主机是否采用有状态自动配置获取除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址外的其他信息。]{style="font-family:宋体"}

[[如果设置该标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_12181_84059_2046250498}[，主机将通过有状态自动配置（例如]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器）来获取除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址外的其他信息；否则，将通过无状态自动配置获取其他信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_446707484}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x527232719}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x2060129812}[配置主机通过无状态自动配置来获取除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址外的其他信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_1240787842}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo ipv6 nd autoconfig other-flag]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1893413360}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1745486312}[配置主机通过无状态自动配置来获取除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址外的其他信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_29064334}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] undo ipv6 nd autoconfig other-flag]{lang="EN-US"}
:::

::: {#1500473685 .myid}
[]{#_Toc404787025}[]{#struct_0_12181_84059_x2099863755}[]{#_Toc279579813}[]{#_Toc138417094}[]{#_Toc137020675}[]{#_Toc59352330}[]{#_Toc52166668}[]{#_Toc90625854}[]{#_Toc90625857}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd dad attempts**

------------------------------------------------------------------------

[**[ipv6 nd dad attempts]{lang="EN-US"}**]{#struct_0_12181_84059_1892902882}[命令用来配置进行重复地址检测时发送邻居请求消息的次数。]{style="font-family:宋体"}

[**[undo ipv6 nd dad attempts]{lang="EN-US"}**]{#struct_0_12181_84059_1383689816}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x760527118}

[**[ipv6 nd dad attempts ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_12181_84059_x2068229792}

[**[undo ipv6 nd dad attempts]{lang="EN-US"}**]{#struct_0_12181_84059_x1893347824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_2123987930}

[[进行重复地址检测时发送邻居请求消息的次数为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_12181_84059_1989980536}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1393981002}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1265951467}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1028012222}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1143792798}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_884628024}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_591486365}

[*[value]{lang="EN-US"}*]{#struct_0_12181_84059_x1893544432}[：进行重复地址检测时发送邻居请求消息的次数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[。当配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示禁止重复地址检测。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1082299040}

[[接口获得]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_334907259}[地址后，将发送邻居请求消息进行重复地址检测，如果在指定的时间内（通过]{style="font-family:宋体"}**[ipv6 nd ns retrans-timer]{lang="EN-US"}**[命令配置）没有收到响应，则继续发送邻居请求消息，当发送的次数达到所设置的次数后，仍未收到响应，则认为该地址可用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_750670373}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_516265220}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_196750532}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口进行重复地址检测时发送邻居请求消息的次数为]{style="font-family:宋体"}[20]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1477731794}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv]{lang="EN-US"}[6 nd dad attempts 20]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1412488723}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1893478896}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[进行重复地址检测时发送邻居请求消息的次数为]{style="font-family:宋体"}[20]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x900581803}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ]{lang="EN-US"}[ipv6 nd dad attempts 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_956982750}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 interface]{lang="EN-US"}**]{#struct_0_12181_84059_x882072936}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd ns retrans-timer]{lang="EN-US"}**]{#struct_0_12181_84059_x1881384239}
:::

::::: {#1296158572 .myid}
[]{#_Toc404787026}[]{#struct_0_12181_84059_575999259}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd mode uni**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础命令.files/image001.png){#图片 16 width="62" height="25"}]{lang="EN-US"}]{#struct_0_12181_84059_x1893151216}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本特性支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_12181_84059_1993110489}
:::

[ ]{lang="EN-US"}

[**[ipv6 nd mode uni]{lang="EN-US"}**]{#struct_0_12181_84059_1122392198}[命令用来配置接口为用户侧接口。]{style="font-family:宋体"}

[**[undo ipv6 nd mode]{lang="EN-US"}**]{#struct_0_12181_84059_x1586422478}[命令用来恢复接口为网络侧接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1728647186}

[**[ipv6 nd mode uni]{lang="EN-US"}**]{#struct_0_12181_84059_x462831862}

[**[undo ipv6 nd mode]{lang="EN-US"}**]{#struct_0_12181_84059_x217082271}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893085680}

[[接口为网络侧接口。]{style="font-family:宋体"}]{#struct_0_12181_84059_x1108288248}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x710262092}

[[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_x1061689155}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x999426893}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x109441182}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1811637765}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_2048227704}

[[接口为用户侧接口的情况，说明此接口的邻居都为终端主机。对于此种接口上学习到的]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_12181_84059_x1893282288}[表项，驱动软件可以不为其分配下一跳资源。]{style="font-family:宋体"}

[[接口角色为网络侧接口的情况，说明此接口的邻居可能是转发报文的下一跳，因此学习在此接口上的]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_12181_84059_x1684962852}[表项，驱动软件需要为其分配下一跳资源。]{style="font-family:宋体"}

[[通过实际使用情况，正确配置接口的工作模式，可以适当的节省硬件资源。]{style="font-family:宋体"}]{#struct_0_12181_84059_1275829749}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1110317712}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_168065508}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[为用户侧接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1947222466}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 nd mode uni]{lang="EN-US"}
:::::

::: {#-742222199 .myid}
[]{#_Toc404787027}[]{#struct_0_12181_84059_x2045039415}[]{#_Toc279579815}[]{#_Toc138417096}[]{#_Toc137020677}[]{#_Toc59352329}[]{#_Toc52166667}[]{#_Toc241293956}[]{#_Toc241309861}[]{#_Toc241312204}[]{#_Toc241293957}[]{#_Toc241309862}[]{#_Toc241312205}[]{#_Toc241293959}[]{#_Toc241309864}[]{#_Toc241312207}[]{#_Toc241293960}[]{#_Toc241309865}[]{#_Toc241312208}[]{#_Toc241293961}[]{#_Toc241309866}[]{#_Toc241312209}[]{#_Toc241293962}[]{#_Toc241309867}[]{#_Toc241312210}[]{#_Toc241293963}[]{#_Toc241309868}[]{#_Toc241312211}[]{#_Toc241293964}[]{#_Toc241309869}[]{#_Toc241312212}[]{#_Toc241293965}[]{#_Toc241309870}[]{#_Toc241312213}[]{#_Toc241293966}[]{#_Toc241309871}[]{#_Toc241312214}[]{#_Toc241293967}[]{#_Toc241309872}[]{#_Toc241312215}[]{#_Toc241293968}[]{#_Toc241309873}[]{#_Toc241312216}[]{#_Toc241293969}[]{#_Toc241309874}[]{#_Toc241312217}[]{#_Toc241293970}[]{#_Toc241309875}[]{#_Toc241312218}[]{#_Toc241293971}[]{#_Toc241309876}[]{#_Toc241312219}[]{#_Toc241293972}[]{#_Toc241309877}[]{#_Toc241312220}[]{#_Toc241293973}[]{#_Toc241309878}[]{#_Toc241312221}[]{#_Toc241293975}[]{#_Toc241309880}[]{#_Toc241312223}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ns retrans-timer**

------------------------------------------------------------------------

[**[ipv6 nd ns retrans-timer]{lang="NO-BOK"}**]{#struct_0_12181_84059_216162156}[命令用来配置邻居请求消息的重传时间间隔。]{style="font-family:
宋体"}

[**[undo ipv6 nd ns retrans-timer]{lang="EN-US"}**]{#struct_0_12181_84059_x1893216752}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1801524454}

[**[ipv6 nd ns retrans-timer]{lang="NO-BOK"}**]{#struct_0_12181_84059_x2004093520}[ *value*]{lang="NO-BOK"}

[**[undo ipv6 nd ns retrans-timer]{lang="NO-BOK"}**]{#struct_0_12181_84059_1399459113}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x276021579}

[[接口发送]{style="font-family:宋体"}]{#struct_0_12181_84059_950308093}[NS]{lang="NO-BOK"}[消息的时间间隔为]{style="font-family:宋体"}[1000]{lang="NO-BOK"}[毫秒]{style="font-family:宋体"}[；]{style="font-family:宋体"}[接口发布的]{style="font-family:宋体"}[RA]{lang="NO-BOK"}[消息中]{style="font-family:宋体"}[Retrans Timer]{lang="NO-BOK"}[字段的值为]{style="font-family:宋体"}[0]{lang="NO-BOK"}[，]{style="font-family:宋体"}[即不对主机进行指定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_417612148}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1457935600}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x238923904}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1892889072}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1568750089}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x243510779}

[*[value]{lang="NO-BOK"}*]{#struct_0_12181_84059_2135101746}[：]{style="font-family:宋体"}[NS]{lang="NO-BOK"}[消息重传时间间隔]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1000]{lang="NO-BOK"}[～]{style="font-family:宋体"}[4294967295]{lang="NO-BOK"}[，]{style="font-family:宋体"}[单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1960547226}

[[设备发送]{style="font-family:宋体"}[NS]{lang="EN-US"}]{#struct_0_12181_84059_426279780}[消息后，如果未在指定的邻居请求消息重传时间间隔内收到响应，则会重新发送]{style="font-family:宋体"}[NS]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[本命令配置的时间间隔既用于本接口发送]{style="font-family:宋体"}]{#struct_0_12181_84059_x892702869}[NS]{lang="NO-BOK"}[消息的时间间隔]{style="font-family:宋体"}[，]{style="font-family:宋体"}[同时也作为本接口发布的]{style="font-family:宋体"}[RA]{lang="NO-BOK"}[消息中]{style="font-family:宋体"}[Retrans Timer]{lang="NO-BOK"}[字段的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1384267024}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1892823536}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1612646956}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口发送]{style="font-family:宋体"}[NS]{lang="EN-US"}[消息的时间间隔为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1953223084}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6]{lang="NO-BOK"}[ nd ns retrans-timer 10000]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x778586194}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x2070888952}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[发送]{style="font-family:宋体"}[NS]{lang="EN-US"}[消息的时间间隔为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x122525469}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] i]{lang="EN-US"}[pv6 nd ns retrans-timer 10000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1127308438}

[[·[              ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 interface]{lang="EN-US"}**]{#struct_0_12181_84059_x1893413359}
:::

::: {#-727576045 .myid}
[]{#_Toc404787028}[]{#struct_0_12181_84059_627363291}[]{#_Toc279579816}[]{#_Toc138417097}[]{#_Toc137020678}[]{#_Toc59352323}[]{#_Toc52166661}[]{#_Toc90625862}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd nud reachable-time**

------------------------------------------------------------------------

[**[ipv6 nd nud reachable-time]{lang="EN-US"}**]{#struct_0_12181_84059_x1881276525}[命令用来配置接口保持邻居可达状态的时间。]{style="font-family:
宋体"}

[**[undo ipv6 nd nud reachable-time]{lang="EN-US"}**]{#struct_0_12181_84059_x1844919923}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2028828190}

[**[ipv6 nd nud reachable-time ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_12181_84059_1269468960}

[**[undo ipv6 nd nud reachable-time]{lang="EN-US"}**]{#struct_0_12181_84059_x519590290}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1485516156}

[[接口保持邻居可达状态的时间为]{style="font-family:宋体"}[30000]{lang="EN-US"}]{#struct_0_12181_84059_1827197906}[毫秒；接口发布的]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中]{style="font-family:宋体"}[Reachable Timer]{lang="EN-US"}[字段的值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即不对主机进行指定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893347823}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1767694839}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x935182218}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x651637945}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x943078767}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1373391552}

[*[value]{lang="EN-US"}*]{#struct_0_12181_84059_x18293098}[：保持邻居可达状态的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1419885225}

[[当通过邻居可达性检测确认邻居可达后，在所设置的接口保持邻居可达状态的时间内，设备认为邻居可达；超过设置的时间后，如果需要向邻居发送报文，会重新确认邻居是否可达。]{style="font-family:宋体"}]{#struct_0_12181_84059_x1893544431}

[[本命令配置的时间既用于本接口保持邻居可达状态的时间，同时也作为本接口发布的]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_1485583567}[消息中]{style="font-family:宋体"}[Reachable Timer]{lang="EN-US"}[字段的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1284046290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x737964705}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x110227317}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上保持邻居可达状态的时间为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_943212181}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd nud reachable-time 10000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_487767658}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1923228572}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上保持邻居可达状态的时间为]{style="font-family:宋体"}[10000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1893478895}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd nud reachable-time 10000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_665502138}

[[·[              ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 interface]{lang="EN-US"}**]{#struct_0_12181_84059_696161016}
:::

::: {#-665512443 .myid}
[]{#_Toc404787029}[]{#struct_0_12181_84059_114497625}[]{#_Toc402456169}[]{#_Toc397517876}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd snooping enable global**

------------------------------------------------------------------------

[**[ipv6 nd snooping enable global]{lang="EN-US"}**]{#struct_0_12181_84059_x369719534}[命令用来开启学习表项地址类型为全球单播地址的]{style="font-family:
宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[**[undo ipv6 nd snooping enable global]{lang="EN-US"}**]{#struct_0_12181_84059_x296816339}[命令用来关闭学习表项地址类型为全球单播地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x735309856}

[**[ipv6 nd snooping enable global]{lang="EN-US"}**]{#struct_0_12181_84059_1680581566}

[**[undo ipv6 nd snooping enable global]{lang="EN-US"}**]{#struct_0_12181_84059_1564732263}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x573883238}

[[学习表项地址类型为全球单播地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_x1504479328}[表项的功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x925804458}

[[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_x782946453}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_2028220031}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_569255708}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1593883808}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1575880237}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x914708569}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[下开启学习表项地址类型为全球单播地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1048301789}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] ipv6 nd snooping enable global]{lang="EN-US"}
:::

::: {#493455025 .myid}
[]{#_Toc404787030}[]{#struct_0_12181_84059_1898499921}[]{#_Toc402456170}[]{#_Toc397517877}[]{#_Toc395012442}[]{#_Toc389730688}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd snooping enable link-local**

------------------------------------------------------------------------

[**[ipv6 nd snooping enable link-local]{lang="EN-US"}**]{#struct_0_12181_84059_1721253560}[命令用来开启学习表项地址类型为链路本地地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[**[undo ipv6 nd snooping enable link-local]{lang="EN-US"}**]{#struct_0_12181_84059_93688308}[命令用来关闭学习表项地址类型为链路本地地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1125008639}

[**[ipv6 nd snooping enable link-local]{lang="EN-US"}**]{#struct_0_12181_84059_1784797369}

[**[undo ipv6 nd snooping enable link-local]{lang="EN-US"}**]{#struct_0_12181_84059_x825240357}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x976093007}

[[学习表项地址类型为链路本地地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_x545884618}[表项的功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1488502938}

[[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_517782152}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x246960638}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_693703090}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1545205654}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1264248395}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_591507245}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[下开启学习表项地址类型为链路本地地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_1962281702}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] ipv6 nd snooping enable link-local]{lang="EN-US"}
:::

::: {#841559319 .myid}
[]{#_Toc404787031}[]{#struct_0_12181_84059_x431568727}[]{#_Toc402456171}[]{#_Toc397517878}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd snooping glean source**

------------------------------------------------------------------------

[**[ipv6 nd snooping glean source]{lang="EN-US"}**]{#struct_0_12181_84059_x1385396406}[命令用来开启通过]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[数据报文学习]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[**[undo ipv6 nd snooping glean source]{lang="EN-US"}**]{#struct_0_12181_84059_1445157060}[命令用来关闭通过]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据报文学习]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x828900174}

[**[ipv6 nd snooping glean source]{lang="EN-US"}**]{#struct_0_12181_84059_x1498640483}

[**[undo ipv6 nd snooping glean source]{lang="EN-US"}**]{#struct_0_12181_84059_558829870}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x567229993}

[[通过数据报文学习]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}]{#struct_0_12181_84059_1267527773}[表项的功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1507032223}

[[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_x2104199747}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1327388673}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1263530546}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1640450415}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1998930770}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[至少配置了]{style="font-family:宋体"}**[ipv6 nd snooping enable global]{lang="EN-US"}**]{#struct_0_12181_84059_1902860169}[和]{style="font-family:宋体"}**[ipv6 nd snooping enable link-local]{lang="EN-US"}**[这两条命令其中之一后，本功能才能生效。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令开启后，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_67443458}[内非信任口必须开启]{lang="EN-US" style="font-family:宋体"}[IP Source Guard]{lang="EN-US"}[功能，否则会导致该口的报文不能正常转发。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2122656416}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1897111771}[开启]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的接口通过]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据报文学习]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x812588042}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] ipv6 nd snooping glean source]{lang="EN-US"}
:::

::: {#-775595203 .myid}
[]{#_Toc404787032}[]{#struct_0_12181_84059_1895135066}[]{#_Toc402456172}[]{#_Toc397517879}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd snooping max-learning-num**

------------------------------------------------------------------------

[**[ipv6 nd snooping max-learning-num ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_12181_84059_431666785}[命令用来配置接口下学习]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的最大数目。]{style="font-family:宋体"}

[**[undo ipv6 nd snooping max-learning-num]{lang="EN-US"}**]{#struct_0_12181_84059_x1884920448}[命令用来取消接口下学习]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项最大数目的限制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1188718705}

[**[ipv6 nd snooping max-learning-num ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_12181_84059_x265301447}

[**[undo ipv6 nd snooping max-learning-num]{lang="EN-US"}**]{#struct_0_12181_84059_x1016687230}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1854805307}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_12181_84059_135219920}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1903798993}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_280243078}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2119886875}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x605648478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1474926206}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1031737470}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1480737583}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[学习]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的最大数目为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_414726060}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-Gigabitethernet1/0/1\] ipv6 nd snooping max-learning-num 64]{lang="EN-US"}
:::

::: {#-239550468 .myid}
[]{#_Toc404787033}[]{#struct_0_12181_84059_1634546971}[]{#_Toc279579817}[]{#_Toc138417098}[]{#_Toc137020679}[]{#_Toc59352328}[]{#_Toc52166666}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra halt**

------------------------------------------------------------------------

[**[ipv6 nd ra halt]{lang="EN-US"}**]{#struct_0_12181_84059_238627646}[命令用来抑制]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的发布。]{style="font-family:宋体"}

[**[undo ipv6 nd ra halt]{lang="EN-US"}**]{#struct_0_12181_84059_91116511}[命令用来取消对]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息发布的抑制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_360808883}

[**[ipv6 nd ra halt]{lang="EN-US"}**]{#struct_0_12181_84059_x2002075586}

[**[undo ipv6 nd ra halt]{lang="DE"}**]{#struct_0_12181_84059_x1893151215}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_1589825962}

[[抑制发布]{style="font-family:宋体"}]{#struct_0_12181_84059_x641352330}[RA]{lang="DE"}[消息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_428156883}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_756989371}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1445828895}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1253775443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_903864955}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893085679}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_814746949}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1714522521}[取消对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发布]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的抑制。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x213952540}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[Gigabit]{lang="EN-US"}[Ethernet1]{lang="EN-US"}[/0/1]{lang="EN-US"}[\]]{lang="EN-US"}[ undo ipv6 nd ra halt]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1079907896}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_616388601}[取消对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[发布]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的抑制。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1377438990}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] undo ipv6 nd ra halt]{lang="EN-US"}
:::

::: {#-1407631085 .myid}
[]{#_Toc404787034}[]{#struct_0_12181_84059_x1893282287}[]{#_Toc279579814}[]{#_Toc138417095}[]{#_Toc137020676}[]{#_Toc59352325}[]{#_Toc52166663}[]{#_Toc90625865}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra hop-limit unspecified**

------------------------------------------------------------------------

[**[ipv6 nd ra hop-limit unspecified]{lang="EN-US"}**]{#struct_0_12181_84059_x1637908685}[命令用来配置]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中不指定跳数限制。]{style="font-family:宋体"}

[**[undo ipv6 nd ra hop-limit unspecified]{lang="EN-US"}**]{#struct_0_12181_84059_x1567414105}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_627154725}

[**[ipv6 nd ra hop-limit unspecified]{lang="EN-US"}**]{#struct_0_12181_84059_1682857407}

[**[undo ipv6 nd ra hop-limit unspecified]{lang="EN-US"}**]{#struct_0_12181_84059_687199290}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1491599009}

[[RA]{lang="EN-US"}]{#struct_0_12181_84059_x442519518}[消息中发布本设备的跳数限制。本设备的跳数限制默认为]{style="font-family:宋体"}[64]{lang="EN-US"}[跳。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x766235997}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1893216751}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1398239927}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_838680442}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1251763309}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x721762593}

[[本设备的跳数限制默认为]{style="font-family:宋体"}[64]{lang="EN-US"}]{#struct_0_12181_84059_1653336759}[跳，可以通过命令]{style="font-family:宋体"}**[ipv6 hop-limit]{lang="EN-US"}**[进行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x330471020}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1687711226}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1892889071}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中不指定跳数限制。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1165465562}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd ra hop-limit unspecified]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x923593509}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1448845558}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中不指定跳数限制。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1106493078}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd ra hop-limit unspecified]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1330471221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 hop-limit]{lang="EN-US"}**]{#struct_0_12181_84059_1305321470}
:::

::: {#1952283500 .myid}
[]{#_Toc404787035}[]{#struct_0_12181_84059_x1892823535}[]{#_Toc279579818}[]{#_Toc138417099}[]{#_Toc137020680}[]{#_Toc59352324}[]{#_Toc52166662}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra interval**

------------------------------------------------------------------------

[**[ipv6 nd ra interval]{lang="EN-US"}**]{#struct_0_12181_84059_1116236399}[命令用来配置]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息发布的最大时间间隔和最小时间间隔。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[ipv6 nd ra interval]{lang="EN-US"}**]{#struct_0_12181_84059_938274452}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1534158727}

[**[ipv6 nd ra interval]{lang="EN-US"}**[ *max-interval-value min-interval-value*]{lang="EN-US"}]{#struct_0_12181_84059_x698631723}

[**[undo ]{lang="EN-US"}[ipv6 nd ra interval]{lang="EN-US"}**]{#struct_0_12181_84059_x1543786039}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_397072292}

[[RA]{lang="EN-US"}]{#struct_0_12181_84059_x2118183460}[消息发布的最大时间间隔为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1395529850}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1893413362}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1386681570}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x315429948}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x223935778}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1469996057}

[*[max-interval-value]{lang="EN-US"}*]{#struct_0_12181_84059_x603684659}[：指定]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息发布的最大时间间隔，取值范围是]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[min-interval-value]{lang="EN-US"}*]{#struct_0_12181_84059_x1533098988}[：指定]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息发布的最小时间间隔，取值范围是]{style="font-family:宋体"}[3]{lang="EN-US"}[～（]{style="font-family:宋体"}*[max-interval-value]{lang="EN-US"}*[ \* 3/4]{lang="EN-US"}[），单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_459355223}

[[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1893347826}[消息周期性发布时，设备在最大时间间隔与最小时间间隔之间随机选取一个值作为周期性发布]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的时间间隔。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1008179952}[消息发布的最大实际间隔应该小于或等于]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中路由器的生存时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x155728123}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x674261114}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x358118078}[设备周期性发布]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的最大时间间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[700]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_1593153241}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd ra interval 1000 700]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x402523456}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_233798829}[配置设备周期性发布]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的最大时间间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[700]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1893544434}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd ra interval 1000 700]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2049868842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd ra router-lifetime]{lang="EN-US"}**]{#struct_0_12181_84059_x211368512}
:::

::: {#-570487173 .myid}
[]{#_Toc59352332}[]{#_Toc52166683}[]{#_Toc404787036}[]{#struct_0_12181_84059_x1351780587}[]{#_Toc279579819}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra no-advlinkmtu**

------------------------------------------------------------------------

[**[ipv6 nd ra no-advlinkmtu]{lang="EN-US"}**]{#struct_0_12181_84059_1898081016}[命令用来配置]{style="font-family:
宋体"}[RA]{lang="EN-US"}[消息中不携带]{style="font-family:宋体"}[MTU]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[**[undo ipv6 nd ra no-advlinkmtu]{lang="EN-US"}**]{#struct_0_12181_84059_x1796807663}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_900608357}

[**[ipv6 nd ra no-advlinkmtu]{lang="PT-BR"}**]{#struct_0_12181_84059_611896540}

[**[undo ipv6 nd ra no-advlinkmtu]{lang="PT-BR"}**]{#struct_0_12181_84059_x1893478898}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_262217611}

[[RA]{lang="EN-US"}]{#struct_0_12181_84059_199638472}[消息中携带]{style="font-family:宋体"}[MTU]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1643522878}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1121147385}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x652624098}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_2007638119}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x947340156}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1582690062}

[[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1893151218}[消息中携带的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[选项可以用来发布链路的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[，用于确保同一链路上的所有节点采用相同的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1186541435}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1792076649}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x589807130}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中不携带]{style="font-family:宋体"}[MTU]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_956998465}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd ra no-advlinkmtu]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x2074393301}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1782706905}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中不携带]{style="font-family:宋体"}[MTU]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1893085682}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd ra no-advlinkmtu]{lang="EN-US"}
:::

::: {#568977454 .myid}
[]{#_Toc404787037}[]{#struct_0_12181_84059_54511166}[]{#_Toc279579820}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra prefix**

------------------------------------------------------------------------

[**[ipv6 nd ra prefix]{lang="EN-US"}**]{#struct_0_12181_84059_991058223}[命令用来配置]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中的前缀信息。]{style="font-family:宋体"}

[**[undo ipv6 nd ra prefix]{lang="EN-US"}**]{#struct_0_12181_84059_x480495245}[命令用来取消]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中前缀信息的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_2081459189}

[**[ipv6 nd ra prefix]{lang="EN-US"}**[ { *ipv6-prefix* *prefix-length \| ipv6-prefix***/***prefix-length* } *valid-lifetime preferred-lifetime* \[ **no-autoconfig** \| **off-link** \] \*]{lang="EN-US"}]{#struct_0_12181_84059_x1479328976}

[**[undo ipv6 nd ra prefix ]{lang="EN-US"}**[{ *ipv6-prefix* *\| ipv6-prefix***/***prefix-length* }]{lang="EN-US"}]{#struct_0_12181_84059_139844788}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_35441868}

[[没有配置]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1715308490}[消息中的前缀信息，此时将使用发送]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的接口]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[RA]{lang="EN-US"}[中的前缀信息，其手工配置地址的有效生命期是]{style="font-family:宋体"}[2592000]{lang="EN-US"}[秒（]{style="font-family:宋体"}[30]{lang="EN-US"}[天），首选生命期是]{style="font-family:宋体"}[604800]{lang="EN-US"}[（]{style="font-family:宋体"}[7]{lang="EN-US"}[天）；其他自动分配地址（如]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[分配地址）的有效生命期和首选生命期与地址本身的生命期相同。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893282290}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x2041127676}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1221293898}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x2137943574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x2035115610}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1954624207}

[*[ipv6-prefix]{lang="EN-US"}*]{#struct_0_12181_84059_1540500652}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_12181_84059_1542472493}[：前缀长度。]{style="font-family:宋体"}

[*[valid-lifetime]{lang="EN-US"}*]{#struct_0_12181_84059_x1893216754}[：前缀的有效存活时间，即有效生命期。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[preferred-lifetime]{lang="EN-US"}*]{#struct_0_12181_84059_638725040}[：前缀用于无状态地址配置的优选项的存活时间，即首选生命期。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[的值要小于等于]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[**[no-autoconfig]{lang="EN-US"}**]{#struct_0_12181_84059_x1812702805}[：指定前缀不用于无状态地址配置。如果不选择该参数，则指定前缀用于无状态地址配置。]{style="font-family:宋体"}

[**[off-link]{lang="EN-US"}**]{#struct_0_12181_84059_1348195722}[：指定前缀不是该链路上直连可达的]{style="font-family:宋体"}[。如果不选择该参数，则表示指定前缀是直连可达的。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1512039908}

[[在同一链路上的主机收到设备发布的]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1033816735}[消息中后，可以根据]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中的前缀信息进行无状态自动配置等操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1499893981}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_2821179}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1417493812}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中的前缀信息。]{style="font-family:宋体"}

[[方法一：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1892889074}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x762181035}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd ra prefix 2001:10::100/64 100 10]{lang="EN-US"}

[[方法二：]{style="font-family:宋体"}]{#struct_0_12181_84059_983340380}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1068849446}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd ra prefix 2001:10::100 64 100 10]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_311696592}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1750620495}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中的前缀信息。]{style="font-family:宋体"}

[[方法一：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1212799785}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1892823538}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd ra prefix 2001:10::100/64 100 10]{lang="EN-US"}

[[方法二：]{style="font-family:宋体"}]{#struct_0_12181_84059_1163290566}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_2147308560}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd ra prefix 2001:10::100 64 100 10]{lang="EN-US"}
:::

::: {#-690599796 .myid}
[]{#_Toc404787038}[]{#struct_0_12181_84059_1815337864}[]{#_Toc279579821}[]{#_Toc138417101}[]{#_Toc137020682}[]{#_Toc59352326}[]{#_Toc52166664}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra router-lifetime**

------------------------------------------------------------------------

[**[ipv6 nd ra router-lifetime]{lang="EN-US"}**]{#struct_0_12181_84059_x519603743}[命令用来配置]{style="font-family:
宋体"}[RA]{lang="EN-US"}[消息中路由器的生存时间。]{style="font-family:宋体"}

[**[undo ipv6 nd ra router-lifetime]{lang="EN-US"}**]{#struct_0_12181_84059_130905361}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1820414130}

[**[ipv6 nd ra router-lifetime]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_12181_84059_x1893413361}

[**[undo ipv6 nd ra router-lifetime]{lang="EN-US"}**]{#struct_0_12181_84059_983397043}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1514523637}

[[RA]{lang="EN-US"}]{#struct_0_12181_84059_404743399}[消息中路由器的生存时间为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1228716725}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_458050123}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x438053073}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_32855623}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1893347825}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x604895425}

[*[value]{lang="EN-US"}*]{#struct_0_12181_84059_1068644590}[：]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中路由器的生存时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9000]{lang="EN-US"}[，单位为秒。当配置为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示本设备不作为默认路由器。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x395041283}

[[RA]{lang="EN-US"}]{#struct_0_12181_84059_1942073502}[消息中路由器的生存时间用于设置发布]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的路由器作为主机的默认路由器的时间。主机根据接收到的]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中的路由器生存时间参数值，就可以确定是否将发布该]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的路由器作为默认路由器。发布]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中路由器生存时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[的路由器不能作为默认路由器。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1711878341}[消息中路由器的生存时间应该大于或等于]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息的发布时间间隔。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_961419640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1519907773}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_293359711}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中路由器的生存时间为]{style="font-family:宋体"}[1000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1893544433}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd ra router-lifetime 1000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1646584315}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1892357907}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中路由器的生存时间为]{style="font-family:宋体"}[1000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_699197480}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd ra router-lifetime 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_880348731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd ra interval]{lang="EN-US"}**]{#struct_0_12181_84059_x2102027551}
:::

::: {#-717302559 .myid}
[]{#_Toc404787039}[]{#struct_0_12181_84059_1314967233}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd route-direct advertise**

------------------------------------------------------------------------

[**[ipv6 nd route-direct advertise]{lang="EN-US"}**]{#struct_0_12181_84059_x1002604392}[命令用来配置]{style="font-family:
宋体"}[ND]{lang="EN-US"}[直连路由通告功能。]{style="font-family:宋体"}

[**[undo ipv6 route-direct advertise]{lang="EN-US"}**]{#struct_0_12181_84059_1312589604}[命令用来关闭]{style="font-family:宋体"}[ND]{lang="EN-US"}[直连路由通告功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2098252609}

[**[ipv6 nd route-direct advertise]{lang="EN-US"}**]{#struct_0_12181_84059_1314901697}

[**[undo ipv6 nd route-direct advertise]{lang="EN-US"}**]{#struct_0_12181_84059_x1404530836}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_334927470}

[[ND]{lang="EN-US"}]{#struct_0_12181_84059_x29792090}[直连路由通告功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x345758070}

[[L3VE]{lang="EN-US"}]{#struct_0_12181_84059_215463496}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x997636504}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1043132515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x526688469}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_577152627}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x374153202}[在]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下配置]{style="font-family:宋体"}[ND]{lang="EN-US"}[直连路由通告功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1851689321}

[\[Sysname\] interface ve-l3vpn 1]{lang="EN-US"}

[\[Sysname-VE-L3VPN1\] ipv6 nd route-direct advertise]{lang="EN-US"}
:::

::: {#416089167 .myid}
[]{#_Toc404787040}[]{#struct_0_12181_84059_x846984404}[]{#_Toc90625870}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd router-preference**

------------------------------------------------------------------------

[**[ipv6 nd router-preference]{lang="EN-US"}**]{#struct_0_12181_84059_x1893478897}[命令用来配置接口下发送的]{style="font-family:
宋体"}[RA]{lang="EN-US"}[消息中的路由器优先级。]{style="font-family:宋体"}

[**[undo ipv6 nd ]{lang="EN-US"}[router-preference]{lang="EN-US"}**]{#struct_0_12181_84059_1828301552}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1076865179}

[**[ipv6 nd ]{lang="PT-BR"}[router-preference]{lang="EN-US"}**[ { **high** \| **low** \| **medium** }]{lang="EN-US"}]{#struct_0_12181_84059_x1657237035}

[**[undo ipv6 nd router-preference]{lang="PT-BR"}**]{#struct_0_12181_84059_1765488413}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x284905872}

[[设备发送的]{style="font-family:宋体"}]{#struct_0_12181_84059_1631882321}[RA]{lang="PT-BR"}[消息中的路由器优先级为]{style="font-family:宋体"}**[medium]{lang="PT-BR"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_14810442}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1893151217}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_427026548}

[[network-admin]{lang="PT-BR"}]{#struct_0_12181_84059_x1406632433}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_12181_84059_1016805595}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x32873995}

[**[high]{lang="PT-BR"}**]{#struct_0_12181_84059_x1425335573}[：]{style="font-family:宋体"}[设置发布]{style="font-family:宋体"}[RA]{lang="PT-BR"}[的路由器为高优先级。]{style="font-family:宋体"}

[**[low]{lang="PT-BR"}**]{#struct_0_12181_84059_1399666811}[：]{style="font-family:宋体"}[设置发布]{style="font-family:宋体"}[RA]{lang="PT-BR"}[的路由器为低优先级。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_12181_84059_x747748960}[：设置发布]{style="font-family:宋体"}[RA]{lang="EN-US"}[的路由器为中优先级。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x622479798}

[[主机根据接收到的]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_x1893085681}[消息中的路由器优先级，可以选择优先级最高的路由器作为默认网关。]{style="font-family:宋体"}

[[在路由器的优先级相同的情况下，遵循"先来先用"的原则，优先选择先接收到的]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12181_84059_457795693}[消息对应的发送路由器作为默认网关。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x608904609}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1606796338}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x599257925}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口下发送的]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中的路由优先级为]{style="font-family:宋体"}**[low]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1664968165}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 nd router-preference low]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1848143960}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1893282289}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[下发送的]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中的路由优先级为]{style="font-family:宋体"}**[high]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x118878911}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 nd router-preference high]{lang="EN-US"}
:::

::: {#912878869 .myid}
[]{#_Toc404787041}[]{#struct_0_12181_84059_1315229377}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd suppression enable**

------------------------------------------------------------------------

[**[ipv6 nd suppression enable]{lang="EN-US"}**]{#struct_0_12181_84059_1686910373}[命令用来开启]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[**[undo ipv6 nd suppression enable]{lang="EN-US"}**]{#struct_0_12181_84059_807827023}[命令用来关闭]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_916672213}

[**[ipv6 nd suppression enable]{lang="EN-US"}**]{#struct_0_12181_84059_x1591190868}

[**[undo ipv6 nd suppression enable]{lang="EN-US"}**]{#struct_0_12181_84059_x1861733340}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1663212905}

[[ND]{lang="EN-US"}]{#struct_0_12181_84059_x1701304660}[泛洪抑制功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1946627385}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1157449650}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x638436394}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x2049509019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1315163841}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_603891513}

[[配置交叉连接视图时，需要先配置]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_12181_84059_x839208653}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1164212540}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1601714833}[开启交叉连接组]{style="font-family:宋体"}[1]{lang="EN-US"}[，交叉连接]{style="font-family:宋体"}[2]{lang="EN-US"}[下的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_604501489}

[\[Sysname\] xconnect-group 1]{lang="EN-US"}

[\[Sysname-xcg-1\] connection 2]{lang="EN-US"}

[\[Sysname-xcg-1-2\] ipv6 nd suppression enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_648500206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd]{lang="EN-US"}[ suppression push interval]{lang="EN-US"}**]{#struct_0_12181_84059_1876914357}
:::

::: {#1610163802 .myid}
[]{#_Toc404787042}[]{#struct_0_12181_84059_1968244305}[]{#_Toc375570737}[]{#_Toc374544073}[]{#_Toc373592991}[]{#_Toc372036114}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd suppression push interval**

------------------------------------------------------------------------

[**[ipv6 nd suppression push interval]{lang="EN-US"}**]{#struct_0_12181_84059_274867834}[命令配置主动推送]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项功能，并配置推送时间间隔。]{style="font-family:宋体"}

[**[undo ipv6 nd suppression push interval]{lang="EN-US"}**]{#struct_0_12181_84059_1315360449}[命令用来关闭设备主动推送]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1800862396}

[**[ipv6 nd suppression push interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_12181_84059_x1235914580}

[**[undo ipv6 nd suppression push interval]{lang="EN-US"}**]{#struct_0_12181_84059_1391451114}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1320754291}

[[设备不会主动推送]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_12181_84059_572211008}[泛洪抑制表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1203297596}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1086569534}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x911614878}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1667979956}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x873663505}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1315294913}

[*[interval]{lang="EN-US"}*]{#struct_0_12181_84059_161404882}[：]{style="font-family:宋体"}[主动推送]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项信息的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟**。**]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x301749762}

[[使用]{style="font-family:宋体"}**[ipv6 nd suppression push interval]{lang="EN-US"}**]{#struct_0_12181_84059_258935542}[命令用来设置主动推送]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项信息的时间间隔，如果当前主动推送]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项信息的功能未开启，将会同时开启主动推送功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x597839530}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1785656008}[配置主动推送]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项功能，将主动推送]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项信息的时间设为]{style="font-family:宋体"}[2]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x608867062}

[\[Sysname\]ipv6 nd suppression ]{lang="EN-US"}[push interval 2 ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_37310388}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd suppression enable]{lang="EN-US"}**]{#struct_0_12181_84059_x334910988}
:::

::: {#-1226108557 .myid}
[]{#_Toc404787043}[]{#struct_0_12181_84059_1868658680}[]{#_Toc279579822}[]{#_Toc138417102}[]{#_Toc137020683}[]{#_Toc59352331}[]{#_Toc52166671}[]{#_Toc90625873}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 neighbor**

------------------------------------------------------------------------

[**[ipv6 neighbor]{lang="EN-US"}**]{#struct_0_12181_84059_x1001083206}[命令用来配置静态邻居表项。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 neighbor**]{lang="EN-US"}]{#struct_0_12181_84059_1755772080}[命令用来删除静态邻居表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x304596095}

[**[ipv6 neighbor ]{lang="EN-US"}***[ipv6-address mac-address]{lang="EN-US"}*[ { *vlan-id port-type* *port-number* \| **interface** *interface-type interface-number* } ]{lang="EN-US"}[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12181_84059_778492546}

[**[undo ipv6 neighbor]{lang="EN-US"}**[ *ipv6-address interface-type interface-number*]{lang="EN-US"}]{#struct_0_12181_84059_x871914019}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893216753}

[[设备上不存在静态邻居表项。]{style="font-family:宋体"}]{#struct_0_12181_84059_235440513}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1952895504}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1581374722}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1908623870}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x53563642}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_901380508}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1403879806}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12181_84059_1779055701}[：静态邻居表项中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mac-address]{lang="EN-US"}*]{#struct_0_12181_84059_x1892889073}[：静态邻居表项中的链路层地址（]{style="font-family:宋体"}[48]{lang="EN-US"}[位，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[）。]{style="font-family:宋体"}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_12181_84059_x2666148}[：静态邻居表项所对应的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[port-type]{lang="EN-US"}*[ *port-number*]{lang="EN-US"}]{#struct_0_12181_84059_x199551755}[：静态邻居表项所对应的二层端口类型和端口号。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12181_84059_x176836240}[：静态邻居表项所对应的三层接口类型和接口号。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12181_84059_78823073}[：指定静态邻居表项所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示静态邻居表项属于公网。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x87964481}

[[邻居表项保存的是设备在链路范围内的邻居信息，设备邻居表项可以通过邻居请求消息]{style="font-family:宋体"}[NS]{lang="EN-US"}]{#struct_0_12181_84059_2146882860}[及邻居通告消息]{style="font-family:宋体"}[NA]{lang="EN-US"}[来动态创建，也可以通过手工配置来静态创建。]{style="font-family:宋体"}

[[设备根据邻居节点的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1068977437}[地址和与此邻居节点相连的三层接口号来唯一标识一个静态邻居表项。目前，静态邻居表项有两种配置方式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本节点的三层接口相连的邻居节点的]{style="font-family:宋体"}]{#struct_0_12181_84059_x1892823537}[IPv6]{lang="EN-US"}[地址和链路层地址；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本节点]{style="font-family:宋体"}]{#struct_0_12181_84059_x46563015}[VLAN]{lang="EN-US"}[中的二层端口相连的邻居节点的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和链路层地址。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_1592664457}[接口，可以采用上述两种方式来配置静态邻居表项：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用第一种方式配置静态邻居表项后，该邻居表项处于]{style="font-family:宋体"}]{#struct_0_12181_84059_364128979}[INCMP]{lang="EN-US"}[状态。设备解析该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下的二层端口信息后，该邻居表项才会进入]{style="font-family:宋体"}[REACH]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用第二种方式配置静态邻居表项，需要保证]{style="font-family:宋体"}]{#struct_0_12181_84059_x410626931}*[port-type]{lang="EN-US"}*[ *port-number*]{lang="EN-US"}[指定的二层端口属于]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，且该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[已经创建了]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口。在配置后，设备会将]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口与]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址相对应来唯一标识一个静态邻居表项，并且该表项处于]{style="font-family:宋体"}[REACH]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[在删除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_x1854227438}[接口对应的静态邻居表项时，只需要指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口即可。]{style="font-family:宋体"}

[[当以太网冗余接口的成员接口包含子接口时，不能指定该以太网冗余接口为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1173661413}[静态邻居表项所对应的接口。关于以太网冗余接口的详细介绍，请参见"可靠性配置指导"中的"冗余备份"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_574872844}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x762587052}[配置三层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[对应的静态邻居表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1893413364}

[\[Sysname\] ipv6 neighbor 2000::1 fe-e0-89 interface gigabitethernet 1/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_223882156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 neighbors]{lang="EN-US"}**]{#struct_0_12181_84059_581145341}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 neighbors]{lang="EN-US"}**]{#struct_0_12181_84059_1673238227}
:::

::: {#1215794045 .myid}
[]{#_Toc290995534}[]{#_Toc404787044}[]{#struct_0_12181_84059_x200699794}[]{#_Toc305933977}[]{#_Toc90625876}[]{#_Toc90625877}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 neighbor link-local minimize**

------------------------------------------------------------------------

[**[ipv6 neighbor link-local minimize]{lang="EN-US"}**]{#struct_0_12181_84059_x725480674}[命令用来配置链路本地]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项资源占用最小化。]{style="font-family:宋体"}

[**[undo ipv6 neighbor ]{lang="EN-US"}[link-local minimize]{lang="EN-US"}**]{#struct_0_12181_84059_1017839966}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x842320800}

[**[ipv6 neighbor link-local minimize]{lang="EN-US"}**]{#struct_0_12181_84059_x1880551187}

[**[undo ipv6 neighbor link-local minimize]{lang="EN-US"}**]{#struct_0_12181_84059_x1893347828}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_154619462}

[[所有]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_12181_84059_x2003209908}[表项均会下发硬件表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_983843603}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1211255050}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_985817915}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_2049078076}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1416158260}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893544436}

[[本功能可以对链路本地]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_12181_84059_x887069428}[表项（该]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为链路本地地址）占用的资源进行优化。]{style="font-family:宋体"}

[[缺省情况下，所有]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_12181_84059_1393169355}[表项均会下发硬件表项。配置本功能后，新学习的、未被引用的链路本地]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项（该]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项的链路本地地址不是某条路由的下一跳）不下发硬件表项，以节省资源。]{style="font-family:宋体"}

[[本功能只对后续新学习的]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_12181_84059_x1789444320}[表项生效，已经存在的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项不受影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_758885824}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x2115257825}[配置链路本地]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项资源占用最小化。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1996471399}

[\[Sysname\] ipv6 neighbor link-local minimize]{lang="EN-US"}
:::

::: {#-1924518049 .myid}
[]{#_Toc404787045}[]{#struct_0_12181_84059_x185799203}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 neighbor stale-aging**

------------------------------------------------------------------------

[**[ipv6 neighbor]{lang="EN-US"}**[ **stale-aging**]{lang="EN-US"}]{#struct_0_12181_84059_x1893478900}[命令用来配置]{style="font-family:宋体"}[STALE]{lang="EN-US"}[状态]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项的老化时间。]{style="font-family:宋体"}

[**[undo ipv6 neighbor stale-aging]{lang="EN-US"}**]{#struct_0_12181_84059_x94602572}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x419646821}

[**[ipv6 neighbor ]{lang="EN-US"}[stale-aging]{lang="EN-US"}***[ aging-time]{lang="EN-US"}*]{#struct_0_12181_84059_1064221715}

[**[undo ipv6 neighbor]{lang="EN-US"}**[ **stale-aging**]{lang="EN-US"}]{#struct_0_12181_84059_293914792}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1759204762}

[[STALE]{lang="EN-US"}]{#struct_0_12181_84059_1476080001}[状态]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项的老化时间为]{style="font-family:宋体"}[240]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_405746951}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_584073424}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893151220}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_830507683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_54077096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1726075613}

[*[aging-time]{lang="EN-US"}*]{#struct_0_12181_84059_1616249718}[：]{style="font-family:宋体"}[STALE]{lang="EN-US"}[状态]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2040187484}

[[为适应网络的变化，]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_12181_84059_615516951}[表需要不断更新。]{style="font-family:宋体"}[ND]{lang="EN-US"}[表中的]{style="font-family:宋体"}[STALE]{lang="EN-US"}[状态]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项并非永远有效，每一条记录都有一个老化时间。到达老化时间的]{style="font-family:宋体"}[STALE]{lang="EN-US"}[状态]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项将迁移到]{style="font-family:宋体"}[DELAY]{lang="EN-US"}[状态。]{style="font-family:宋体"}[5]{lang="EN-US"}[秒钟后]{style="font-family:宋体"}[DELAY]{lang="EN-US"}[状态超时，]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项将迁移到]{style="font-family:宋体"}[PROBE]{lang="EN-US"}[状态，并发送]{style="font-family:宋体"}[3]{lang="EN-US"}[次]{style="font-family:宋体"}[NS]{lang="EN-US"}[报文进行可达性探测。若邻居已经下线，则收不到回应的]{style="font-family:宋体"}[NA]{lang="EN-US"}[报文，此时会将该]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项删除。]{style="font-family:宋体"}

[[用户可以根据网络实际情况调整老化时间。]{style="font-family:宋体"}]{#struct_0_12181_84059_1644509031}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893085684}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_861080220}[配置]{style="font-family:宋体"}[STALE]{lang="EN-US"}[状态]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项的老化时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1217972609}

[\[Sysname\] ipv6 neighbor stale-aging 120]{lang="EN-US"}
:::

::: {#1959809191 .myid}
[]{#_Toc404787046}[]{#struct_0_12181_84059_484369826}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 neighbors max-learning-num**

------------------------------------------------------------------------

[**[ipv6 neighbors ]{lang="EN-US"}[max-learning-num]{lang="EN-US"}**]{#struct_0_12181_84059_433640559}[命令用来配置接口上允许学习的动态邻居表项的最大个数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 neighbors** **max-learning-num**]{lang="EN-US"}]{#struct_0_12181_84059_x1027294834}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x340313371}

[**[ipv6 neighbors ]{lang="EN-US"}[max-learning-num]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_12181_84059_2053348441}

[**[undo ipv6 neighbors ]{lang="EN-US"}[max-learning-num]{lang="EN-US"}**]{#struct_0_12181_84059_x1893282292}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x878328262}

[[不同型号的设备支持的缺省情况不同，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_12181_84059_1065639244}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1618926775}

[[二层接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_1038652453}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2029715958}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x901549420}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1456862540}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893216756}

[*[number]{lang="EN-US"}*]{#struct_0_12181_84059_x524074374}[：接口上允许学习的动态邻居表项的最大个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1149882874}

[[设备可以通过]{style="font-family:宋体"}[NS]{lang="EN-US"}]{#struct_0_12181_84059_1284445447}[消息和]{style="font-family:宋体"}[NA]{lang="EN-US"}[消息来动态获取邻居节点的链路层地址，并将其加入到邻居表中。为了防止部分接口下的用户占用过多的资源，可以通过设置接口学习动态邻居表项的最大数目来进行限制。当接口学习到的动态邻居表项的个数达到所设置的最大值时，该接口将不再学习动态邻居表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x378028559}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x2120524610}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_821204562}[指定]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上允许动态学习的邻居的最大个数为]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_86146173}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[Gigabit]{lang="EN-US"}[Ethernet1]{lang="EN-US"}[/0/1]{lang="EN-US"}[\]]{lang="EN-US"}[ ]{lang="EN-US"}[ipv6 neighbors max-learning-num 10]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x1892889076}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_400618379}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上允许动态学习的邻居的最大个数为]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_994220530}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 neighbors max-learning-num 10]{lang="EN-US"}
:::

::: {#1629943128 .myid}
[]{#_Toc296959535}[]{#_Toc404787047}[]{#struct_0_12181_84059_x1724185649}[]{#_Toc298765614}[]{#_Toc265680005}[]{#_Toc263067816}[]{#_Toc207010292}[]{#_Toc207010025}[]{#_Toc139515316}[]{#_Toc137103149}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 pathmtu**

------------------------------------------------------------------------

[**[ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_x1918456591}[命令用来配置指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对应的静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ipv6 pathmtu]{lang="PT-BR"}**]{#struct_0_12181_84059_x405205109}[命令用来删除指定]{style="font-family:宋体"}[IPv6]{lang="PT-BR"}[地址的]{style="font-family:宋体"}[PMTU]{lang="PT-BR"}[配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1090046009}

[**[ipv6 pathmtu]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **vpn-instance** *vpn-instance-name* \] *ipv6-address* *value*]{lang="EN-US"}]{#struct_0_12181_84059_x363289560}

[**[undo ipv6 pathmtu]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] *ipv6-address*]{lang="EN-US"}]{#struct_0_12181_84059_x1892823540}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_1519848606}

[[没有配置静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_12181_84059_x1863603980}[值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1051562366}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_2140617522}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x511643506}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1644006131}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x769501671}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893413363}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_12181_84059_x179402371}[：指定]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示公网。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_12181_84059_1093725114}[：指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_12181_84059_1618523678}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1280]{lang="EN-US"}[～]{style="font-family:宋体"}[10240]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_992847533}

[[用户可以为指定的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1079381196}[地址配置静态的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[值。当源端主机从接口发送报文时，将比较该接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[与指定目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[，如果报文长度大于二者中的最小值，则采用此最小值对报文进行分片。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1295673398}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1205498054}[配置指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对应的静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1893347827}

[\[Sysname\] ipv6 pathmtu fe80::12 1300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_557903989}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_44960408}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_x2119088051}
:::

::: {#1770524889 .myid}
[]{#_Toc404787048}[]{#struct_0_12181_84059_x1754506234}[]{#_Toc298765615}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 pathmtu age**

------------------------------------------------------------------------

[**[ipv6 pathmtu age]{lang="EN-US"}**]{#struct_0_12181_84059_1995732353}[命令用来配置动态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[的老化时间。]{style="font-family:宋体"}

[**[undo ipv6 pathmtu age]{lang="EN-US"}**]{#struct_0_12181_84059_1805020955}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1692410861}

[**[ipv6 pathmtu age]{lang="EN-US"}**[ *age-time*]{lang="EN-US"}]{#struct_0_12181_84059_1620989990}

[**[undo ipv6 pathmtu age]{lang="EN-US"}**]{#struct_0_12181_84059_x1893544435}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x483784901}

[[动态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_12181_84059_1209014137}[的老化时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1482356311}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1586585804}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1523170773}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_2073834437}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x247531027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893478899}

[*[age-time]{lang="EN-US"}*]{#struct_0_12181_84059_x1303866330}[：]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[老化时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_41592208}

[[动态确定源端主机到目的端主机的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_12181_84059_x795011917}[后，源端主机将使用这个]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值发送后续报文到目的端主机。当]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[老化时间超时后，源端主机会通过]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[机制重新确定发送报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[需要注意的是，该配置对静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_12181_84059_1686089894}[不起作用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1091614931}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_397754719}[配置动态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[的老化时间为]{style="font-family:宋体"}[40]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_199914474}

[\[Sysname\] ipv6 pathmtu age 40]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1893151219}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_x379542506}
:::

::::: {#1456444812 .myid}
[]{#_Toc404787049}[]{#struct_0_12181_84059_x187569258}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 prefer temporary-address**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_12181_84059_1076827283}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_12181_84059_1852472078}
:::

[ ]{lang="EN-US"}

[**[ipv6 prefer temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_x210748588}[命令用来开启优先选择临时地址作为报文的源地址功能。]{style="font-family:
宋体"}

[**[undo ipv6 prefer temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_x1757120608}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_199734058}

[**[ipv6 prefer temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_x1893085683}

[**[undo ipv6 prefer temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_1620595107}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_1468388715}

[[优先选择临时地址作为报文的源地址功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12181_84059_535015192}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2074894511}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1668477655}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x4626208}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1229734537}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1893282291}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x475043735}

[[在配置了优先选择临时地址功能前提下发送报文，系统将优先选择临时地址作为报文的源地址。如果生成的临时地址因为]{style="font-family:宋体"}[DAD]{lang="EN-US"}]{#struct_0_12181_84059_x1803258313}[冲突不可用，就采用公共地址作为报文的源地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x55241207}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1201731239}[开启优先选择临时地址作为报文的源地址功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x748504264}

[\[Sysname\] ipv6 prefer temporary-address]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1240088264}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 address auto]{lang="EN-US"}**]{#struct_0_12181_84059_x1295980364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd ra prefix]{lang="EN-US"}**]{#struct_0_12181_84059_x1186260331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_x1893216755}
:::::

::: {#1960843217 .myid}
[]{#_Toc404787050}[]{#struct_0_12181_84059_1053765667}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 prefix**

------------------------------------------------------------------------

[**[ipv6 prefix]{lang="EN-US"}**]{#struct_0_12181_84059_855301551}[命令用来手工配置静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{style="font-family:宋体"}

[**[undo ipv6 prefix]{lang="EN-US"}**]{#struct_0_12181_84059_1054486563}[命令用来用来删除指定的静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1054421027}

[**[ipv6 prefix]{lang="EN-US"}**[ *prefix-number ipv6-prefix/prefix-length*]{lang="EN-US"}]{#struct_0_12181_84059_x2003456012}

[**[undo ipv6 prefix ]{lang="EN-US"}***[prefix-number]{lang="EN-US"}*]{#struct_0_12181_84059_1053962276}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_1053896740}

[[设备上不存在任何静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_1054093348}[前缀。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1224751292}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1054027812}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1568535763}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1053700132}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1053634596}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1053831204}

[*[prefix-number]{lang="EN-US"}*]{#struct_0_12181_84059_x1871663250}[：前缀编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-prefix/prefix-length]{lang="EN-US"}*]{#struct_0_12181_84059_1053765668}[：前缀和前缀长度。]{style="font-family:
宋体"}*[prefix-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1054486564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不允许通过重复执行]{style="font-family:宋体"}]{#struct_0_12181_84059_327313641}[ipv6 prefix]{lang="EN-US"}[命令来修改已经创建的静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不允许手工修改和删除从]{style="font-family:宋体"}]{#struct_0_12181_84059_1054421028}[DHCPv6]{lang="EN-US"}[服务器获取的动态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[手工配置的静态]{style="font-family:宋体"}]{#struct_0_12181_84059_x1386872854}[IPv6]{lang="EN-US"}[前缀与动态生成的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀编号允许相同，静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀优先。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x825888111}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1386807318}[创建]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态前缀编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，前缀为]{style="font-family:宋体"}[2001:0410::/32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1386938390}

[\[Sysname\] ipv6 prefix 1 2001:0410::/32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x410065698}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 prefix]{lang="EN-US"}**]{#struct_0_12181_84059_x1386610710}
:::

::: {#-727643935 .myid}
[]{#_Toc404787051}[]{#struct_0_12181_84059_x2071676515}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 reassemble local enable**

------------------------------------------------------------------------

[**[ipv6 reassemble local enable]{lang="EN-US"}**]{#struct_0_12181_84059_1784852266}[命令用来开启设备的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[分片报文本地重组功能。]{style="font-family:宋体"}

[**[undo ipv6 reassemble local enable]{lang="EN-US"}**]{#struct_0_12181_84059_347901241}[命令用来关闭设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[分片报文本地重组功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x2071742051}

[**[ipv6 reassemble local enable]{lang="EN-US"}**]{#struct_0_12181_84059_1388816178}

[**[undo ipv6 reassemble local enable]{lang="EN-US"}**]{#struct_0_12181_84059_x2036637787}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_159729920}

[[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x2071545443}[分片报文本地重组功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_622771704}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x2113036107}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1844587064}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x2071610979}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x705924708}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1266271282}

[[当分布式设备的某块单板收到目的为本设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1921791839}[分片报文时，需要把分片报文送到主用主控板进行重组，这样会导致报文重组性能较低的问题。当开启]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[分片报文本地重组功能后，分片报文会在该单板上直接进行报文重组，这样就能提高分片报文的重组性能。]{style="font-family:宋体"}

[[需要说明的是，开启]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x2072069730}[分片报文本地重组功能后，如果分片报文是从设备上不同的单板进入的，会导致]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[分片报文本地无法重组成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_2038309499}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1260308421}[开启设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[分片报文本地重组功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x2072135266}

[\[Sysname\] ipv6 reassemble local enable]{lang="EN-US"}
:::

::: {#-1861916487 .myid}
[]{#_Toc404787052}[]{#struct_0_12181_84059_x927358901}[]{#_Toc279391300}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 redirects enable**

------------------------------------------------------------------------

[**[ipv6 redirects enable]{lang="EN-US"}**]{#struct_0_12181_84059_587572687}[命令用来开启设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[重定向报文的发送功能。]{style="font-family:宋体"}

[**[undo ipv6 redirects enable]{lang="EN-US"}**]{#struct_0_12181_84059_x610541493}[命令用来关闭设备的]{style="font-family:
宋体"}[ICMPv6]{lang="EN-US"}[重定向报文的发送功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1140415977}

[**[ipv6 redirects enable]{lang="EN-US"}**]{#struct_0_12181_84059_x113318530}

[**[undo ipv6 redirects enable]{lang="EN-US"}**]{#struct_0_12181_84059_376403735}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1920828541}

[[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1892889075}[重定向报文发送功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_803902906}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_281501411}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1729180911}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1618282625}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x602006482}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x307635797}

[[主机启动时，它的路由表中可能只有一条到缺省网关的缺省路由。当满足一定的条件时，作为缺省网关的设备会向源主机发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_x2047657806}[重定向报文，通知主机重新选择正确的下一跳进行后续报文的发送。]{style="font-family:宋体"}

[[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1892823539}[重定向报文发送功能可以简化主机的管理，使具有很少选路信息的主机逐渐建立较完善的路由表，从而找到最佳路由。但是由于重定向功能会在主机的路由表中增加主机路由，当增加的主机路由很多时，会降低主机性能。因此默认情况下设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[重定向报文发送功能是关闭的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1565592789}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_660479433}[开启设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[重定向报文发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x469444660}

[\[Sysname\] ipv6 redirects enable]{lang="EN-US"}
:::

::: {#143715065 .myid}
[]{#_Toc404787053}[]{#struct_0_12181_84059_x860043003}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 router-renumber enable**

------------------------------------------------------------------------

[**[ipv6 router-renumber enable]{lang="EN-US"}**]{#struct_0_12181_84059_x860108539}[命令用来配置接口的路由器重编号功能。]{style="font-family:
宋体"}

[**[undo ipv6 router-renumber enable]{lang="EN-US"}**]{#struct_0_12181_84059_x860174075}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x860239611}

[**[ipv6 router-renumber enable]{lang="EN-US"}**]{#struct_0_12181_84059_x860305147}

[**[undo ipv6 router-renumber enable]{lang="EN-US"}**]{#struct_0_12181_84059_x859322107}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x859387643}

[[路由器重编号功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_12181_84059_587186671}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x859846396}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x859911932}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x859977468}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x860043004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1307083215}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x860108540}

[[设备接收到合法的路由器重编号报文时，会根据报文的内容对本设备上所有使能该功能的三层接口下配置的前缀和地址进行重新配置。]{style="font-family:宋体"}]{#struct_0_12181_84059_x860174076}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x860239612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x860305148}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x859322108}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置路由器重编号功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x859387644}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 router-renumber enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_706237550}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_706172014}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置路由器重编号功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_706106478}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ipv6 router-renumber enable]{lang="EN-US"}
:::

::: {#-651149615 .myid}
[]{#_Toc404787054}[]{#struct_0_12181_84059_x1835535434}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 temporary-address**

------------------------------------------------------------------------

[**[ipv6 temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_1477057529}[命令用来配置系统生成临时地址。]{style="font-family:宋体"}

[**[undo ipv6 temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_x1124238320}[命令用来取消系统生成临时地址功能，同时会删除已经存在的临时地址。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_12181_84059_833022}

[**[ipv6 temporary-address]{lang="EN-US"}**[ \[ *valid-lifetime preferred-lifetime* \]]{lang="EN-US"}]{#struct_0_12181_84059_x327329419}

[**[undo ipv6 temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_x1571218837}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x955599552}

[[系统不生成临时地址。]{style="font-family:宋体"}]{#struct_0_12181_84059_x2128076116}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x498066742}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1802367373}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1222783301}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x836536351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x959710909}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x327263883}

[*[valid-lifetime]{lang="SV"}*]{#struct_0_12181_84059_1537367679}[：临时地址的有效生命期，取值范围为]{style="font-family:宋体"}[600]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[604800]{lang="EN-US"}[秒（]{style="font-family:宋体"}[7]{lang="EN-US"}[天）。]{style="font-family:宋体"}

[*[preferred-lifetime]{lang="EN-US"}*]{#struct_0_12181_84059_837072749}[：临时地址的首选生命期，取值范围为]{style="font-family:宋体"}[600]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒（]{style="font-family:宋体"}[1]{lang="EN-US"}[天）。]{style="font-family:宋体"}*[preferred-lifetime]{lang="EN-US"}*[的值要小于等于]{style="font-family:宋体"}*[valid-lifetime]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_x453601909}

[[在配置了无状态自动配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x1341293008}[地址功能后，接口会根据接收到的]{style="font-family:宋体"}[RA]{lang="EN-US"}[报文中携带的地址前缀信息和接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[，自动生成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址。如果接口是]{style="font-family:宋体"}[IEEE 802]{lang="EN-US"}[类型的接口（例如，以太网接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口），其接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[是由]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址根据一定的规则生成，此接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[具有全球唯一性。对于不同的前缀，接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[部分始终不变，攻击者通过接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[可以很方便的识别出通信流量是由哪台设备产生的，并分析其规律，会造成一定的安全隐患。]{style="font-family:宋体"}

[[如果在地址无状态自动配置时，自动生成接口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_12181_84059_1110601510}[不断变化的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，就可以加大攻击的难度，从而保护网络。为此，设备提供了临时地址功能，使得系统可以生成临时地址。]{style="font-family:宋体"}

[[配置该功能后，通过地址无状态自动配置，]{style="font-family:宋体"}[IEEE 802]{lang="EN-US"}]{#struct_0_12181_84059_x606171065}[类型的接口可以同时生成两类地址：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公共地址：地址前缀采用]{style="font-family:宋体"}]{#struct_0_12181_84059_x1725667977}[RA]{lang="EN-US"}[报文携带的前缀，接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[由]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址产生。]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[始终不变。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[临时地址：地址前缀采用]{style="font-family:宋体"}]{#struct_0_12181_84059_x327460491}[RA]{lang="EN-US"}[报文携带的前缀，接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[由系统根据]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法计算产生。]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[不断变化。]{lang="EN-US" style="font-family:宋体"}

[[当临时地址的有效生命期过期后，这个临时地址将被删除，同时，系统会通过]{style="font-family:宋体"}[MD5]{lang="EN-US"}]{#struct_0_12181_84059_x353238689}[算法重新生成一个接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[不同的临时地址。所以，该接口发送报文的源地址的接口]{style="font-family:宋体"}[ID]{lang="EN-US"}[总是在不停变化。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_12181_84059_1621464759}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[配置本功能时需要打开地址无状态自动配置功能。]{style="font-family:宋体"}]{#struct_0_12181_84059_x1211211540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[配置的临时地址的有效生命期要大于或等于首选生命期。]{style="font-family:宋体"}]{#struct_0_12181_84059_1841290110}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[临时地址的首选生命期是如下两个值之中的较小者：]{style="font-family:宋体"}]{#struct_0_12181_84059_x2145631209}[RA]{lang="EN-US"}[前缀中的首选生命期和（配置的临时地址首选生命期减去]{style="font-family:宋体"}[DESYNC_FACTOR]{lang="EN-US"}[）。]{style="font-family:宋体"}[DESYNC_FACTOR]{lang="EN-US"}[是一个]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[600]{lang="EN-US"}[秒的随机值。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[临时地址的有效生命期是如下两个值之中的较小者：]{style="font-family:宋体"}]{#struct_0_12181_84059_1023206937}[RA]{lang="EN-US"}[前缀中的有效生命期和配置的临时地址有效生命期。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x511751447}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_1851285032}[配置系统生成临时地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x327394955}

[\[Sysname\] ipv6 temporary-address]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1545219728}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 address auto]{lang="EN-US"}**]{#struct_0_12181_84059_1601854856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 nd ra prefix]{lang="EN-US"}**]{#struct_0_12181_84059_613348690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 prefer temporary-address]{lang="EN-US"}**]{#struct_0_12181_84059_561909212}
:::

::::: {#-1327981038 .myid}
[]{#_Toc404787055}[]{#struct_0_12181_84059_x1004008724}[]{#_Toc279391301}

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 unreachables enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_12181_84059_x1635595220}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本特性的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_12181_84059_x327067275}
:::

**[ ]{lang="EN-US"}**

[**[ipv6 unreachables enable]{lang="EN-US"}**]{#struct_0_12181_84059_1595444182}[命令用来开启设备的]{style="font-family:
宋体"}[ICMPv6]{lang="EN-US"}[目的不可达报文的发送功能。]{style="font-family:
宋体"}

[**[undo ipv6 unreachables enable]{lang="EN-US"}**]{#struct_0_12181_84059_x162452836}[命令用来关闭设备的]{style="font-family:
宋体"}[ICMPv6]{lang="EN-US"}[目的不可达报文的发送功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1716123013}

[**[ipv6 unreachables enable]{lang="ES"}**]{#struct_0_12181_84059_x1234407699}

[**[undo ipv6 unreachables ]{lang="ES"}[enable]{lang="EN-US"}**]{#struct_0_12181_84059_1021828492}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x456403017}

[[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_1114543287}[目的不可达报文发送功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1096263353}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x327001739}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x350194416}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1024073627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x328494669}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_1021325042}

[[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_355325486}[目的不可达报文发送功能是在设备收到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据报文后，如果发生目的不可达的差错，则将报文丢弃并给源端发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[目的不可达差错报文。]{style="font-family:宋体"}

[[由于]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_12181_84059_1193757150}[目的不可达报文传递给用户进程的信息为不可达信息，如果有用户恶意攻击，可能会影响终端用户的正常使用。为了避免上述现象发生，可以关闭设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[目的不可达报文发送功能，从而减少网络流量、防止遭到恶意攻击。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_234999020}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x327198347}[开启设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[目的不可达报文发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1979734615}

[\[Sysname\] ipv6 unreachables enable]{lang="EN-US"}
:::::

::: {#-1692140552 .myid}
[]{#_Toc404787056}[]{#struct_0_12181_84059_143326798}

**IPv6基础 \-- IPv6基础配置命令 \-- local-proxy-nd enable**

------------------------------------------------------------------------

[**[local-proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_2073933700}[命令用来开启本地]{style="font-family:宋体"}[ND Proxy]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo local-proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_1729534936}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1869439185}

[**[local-proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_1324819219}

[**[undo local-proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_2052148298}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_x327132811}

[[本地]{style="font-family:宋体"}[ND Proxy]{lang="EN-US"}]{#struct_0_12181_84059_x1206523380}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1270694530}

[[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_x1145111506}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1881660579}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_173438761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1173534571}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1503069899}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x326805131}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1929927668}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上开启本地]{style="font-family:宋体"}[ND Proxy]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1646628505}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] local-proxy-nd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_x2042784791}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_74082599}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上开启本地]{style="font-family:宋体"}[ND Proxy]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x1191629608}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] local-proxy-nd enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1498203257}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_x326739595}
:::

::: {#-945711920 .myid}
[]{#_Toc404787057}[]{#struct_0_12181_84059_1505499895}

**IPv6基础 \-- IPv6基础配置命令 \-- proxy-nd enable**

------------------------------------------------------------------------

[**[proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_1812741345}[命令用来开启]{style="font-family:宋体"}[ND Proxy]{lang="ES"}[功能。]{style="font-family:宋体"}

[**[undo proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_1506971693}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x650012828}

[**[proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_1366952048}

[**[undo proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_222968799}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12181_84059_1951249151}

[[ND Proxy]{lang="EN-US"}]{#struct_0_12181_84059_840717715}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x327329418}

[[VLAN]{lang="EN-US"}]{#struct_0_12181_84059_x1571284373}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1611846872}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_756542809}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x923167614}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1840935877}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_941979897}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x2107848789}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上开启]{style="font-family:宋体"}[ND Proxy]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_x327263882}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] proxy-nd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12181_84059_1537302143}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_392363639}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上开启]{style="font-family:宋体"}[ND Proxy]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12181_84059_926171745}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] proxy-nd enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_405512629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-proxy-nd enable]{lang="ES"}**]{#struct_0_12181_84059_x1600105454}
:::

::: {#-31954021 .myid}
[]{#_Toc404787058}[]{#struct_0_12181_84059_x958237142}[]{#_Toc402456198}[]{#_Toc397517882}[]{#_Toc395012446}[]{#_Toc389730692}

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 nd snooping**

------------------------------------------------------------------------

[**[reset ipv6 nd snooping]{lang="EN-US"}**]{#struct_0_12181_84059_x1991458394}[命令用来清除设备的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_607846799}

[**[reset ipv6 nd snooping]{lang="EN-US"}**[ { \[ **vlan** *vlan-id* \] \[ **global** \| **link-local** \] \| **vlan** *vlan-id ipv6-address* }]{lang="EN-US"}]{#struct_0_12181_84059_1629380110}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1432800255}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1905583828}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x325612865}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x233968942}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x2130999348}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1487183856}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x365661756}[清除设备上的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 nd snooping]{lang="EN-US"}]{#struct_0_12181_84059_1116313124}
:::

::: {#1190853033 .myid}
[]{#_Toc404787059}[]{#struct_0_12181_84059_1315294912}[]{#_Toc375570736}[]{#_Toc374544072}[]{#_Toc373592990}

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 nd suppression xconnect-group**

------------------------------------------------------------------------

[**[reset ipv6 nd suppression xconnect-group]{lang="EN-US"}**]{#struct_0_12181_84059_161470418}[命令用来清除]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1232000823}

[**[reset ipv6 nd suppression xconnect-group]{lang="EN-US"}**[ \[ **name** *group-name* \]]{lang="EN-US"}]{#struct_0_12181_84059_1172314590}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_278049172}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12181_84059_1008328717}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1895118618}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1258641793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x93278149}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_1851485732}

[**[name]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_12181_84059_1315425984}[：交叉连接组的名称，取值为]{style="font-family:宋体"}[1\~31]{lang="EN-US"}[个字符的字符串，不能包含字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1159335906}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_436879824}[清除所有交叉连接组下的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 nd suppression ]{lang="EN-US"}]{#struct_0_12181_84059_x1104700838}[xconnect-group ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_45435918}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_12181_84059_723167252}**[ipv6 nd]{lang="EN-US"}[ suppression xconnect-group]{lang="EN-US"}**
:::

::: {#2083420811 .myid}
[]{#_Toc404787060}[]{#struct_0_12181_84059_159751225}[]{#_Toc279579824}

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 neighbors**

------------------------------------------------------------------------

[**[reset ipv6 neighbors]{lang="EN-US"}**]{#struct_0_12181_84059_x327460490}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x353304225}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_x1814487106}

[**[reset ipv6 neighbors ]{lang="EN-US"}**[{ **all** *\|* **dynamic** *\|* **interface** *interface-type interface-number* \| **static** }]{lang="EN-US"}]{#struct_0_12181_84059_x1549274068}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1892001606}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset ipv6 neighbors ]{lang="EN-US"}**[{ **all** *\|* **dynamic** *\|* **interface** *interface-type interface-number* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **static** }]{lang="EN-US"}]{#struct_0_12181_84059_359543645}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_1768569321}[模式：]{style="font-family:宋体"}

[**[reset ipv6 neighbors ]{lang="EN-US"}**[{ **all** *\|* **dynamic** *\|* **interface** *interface-type interface-number* \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **static** }]{lang="EN-US"}]{#struct_0_12181_84059_x614194451}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_x356014976}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x327394954}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_1545285264}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_475981384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x626347824}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x407008135}

[**[all]{lang="EN-US"}**]{#struct_0_12181_84059_x1226336937}[：清除所有接口上的静态与动态邻居信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_12181_84059_1427655188}[：清除所有接口上的动态邻居信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_12181_84059_x1455172139}[：清除指定接口上的动态邻居信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_x327067274}[：清除指定单板上的动态邻居信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除所有单板上的动态邻居表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_1595378646}[：清除指定成员设备的动态邻居信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除所有成员设备上的动态邻居表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_286095293}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的动态邻居信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的动态邻居表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_639611899}[：清除指定成员设备上指定单板的动态邻居信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除所有单板上的动态邻居表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1852179234}[：清除指定单板的动态邻居信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除所有单板上的动态邻居表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_12181_84059_x1038002898}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的动态邻居信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_12181_84059_x83651082}[：清除所有接口上的静态邻居信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_250929778}

[[当前的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_12181_84059_x2002160385}[邻居信息可以通过]{style="font-family:宋体"}**[display ipv6 neighbors]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1358338339}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x141481598}[清除]{style="font-family:宋体"}[所有接口上的所有邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 neighbors all]{lang="EN-US"}]{#struct_0_12181_84059_x327001738}

[This will delete all the entries. Continue? \[Y/N\]:Y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x350259952}[清除]{style="font-family:宋体"}[所有接口上的动态邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 neighbors dynamic]{lang="EN-US"}]{#struct_0_12181_84059_x1719852513}

[This will delete all the dynamic entries. Continue? \[Y/N\]:Y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_166769810}[清除]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的所有邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 neighbors interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_12181_84059_1348513457}

[This will delete all the dynamic entries by the interface you specified. Contin]{lang="EN-US"}

[ue? \[Y/N\]:Y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_733400725}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 neighbors]{lang="EN-US"}**]{#struct_0_12181_84059_677027271}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 neighbor]{lang="EN-US"}**]{#struct_0_12181_84059_1609695348}
:::

::: {#240899779 .myid}
[]{#_Toc277663837}[]{#_Toc138417110}[]{#_Toc137020691}[]{#_Toc59352333}[]{#_Toc404787061}[]{#struct_0_12181_84059_x327198346}[]{#_Toc298765616}

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 pathmtu**

------------------------------------------------------------------------

[**[reset ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_x1979669079}[命令用来清除]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_915556265}

[**[reset ipv6 pathmtu]{lang="EN-US"}**[ { **all** \| **dynamic** \| **static** }]{lang="EN-US"}]{#struct_0_12181_84059_1280399709}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1116620632}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12181_84059_x1791425312}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_135133580}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_x1673142739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_x522833291}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x327132810}

[**[all]{lang="EN-US"}**]{#struct_0_12181_84059_x1206457844}[：清空所有的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_12181_84059_500492790}[：清空所有动态创建的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_12181_84059_388657072}[：清空所有的静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1804374185}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x1121992174}[清除所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 pathmtu all]{lang="EN-US"}]{#struct_0_12181_84059_x808111395}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1747805555}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_12181_84059_x326805130}
:::

::: {#293425946 .myid}
[]{#_Toc404787062}[]{#struct_0_12181_84059_705909868}

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 router-renumber statistics**

------------------------------------------------------------------------

[**[reset ipv6 router-renumber statistics]{lang="EN-US"}**]{#struct_0_12181_84059_705844332}[命令用来清除路由器重编号统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_705778796}

[**[reset ipv6 router-renumber statistics]{lang="EN-US"}**]{#struct_0_12181_84059_x970859901}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_706761836}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12181_84059_706696300}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_706237547}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_706172011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_1340422530}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_706106475}

[[使用本命令可以清除路由器重编号功能的统计信息，但序列号、重置序列号和分段号不受本命令影响。]{style="font-family:宋体"}]{#struct_0_12181_84059_706040939}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_705975403}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_705909867}[清除路由器重编号的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 router-renumber statistics]{lang="EN-US"}]{#struct_0_12181_84059_x1960071068}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_705844331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 router-renumber statistics]{lang="EN-US"}**]{#struct_0_12181_84059_705778795}
:::

::: {#-588549373 .myid}
[]{#_Toc404787063}[]{#struct_0_12181_84059_x1929993204}

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 statistics**

------------------------------------------------------------------------

[**[reset ipv6 statistics]{lang="EN-US"}**]{#struct_0_12181_84059_x1718688454}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_1787937164}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_12181_84059_205771809}

[**[reset ipv6 statistics]{lang="EN-US"}**]{#struct_0_12181_84059_2136456512}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12181_84059_x1299570711}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset ipv6 statistics ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_x593215223}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_12181_84059_x326739594}[模式：]{style="font-family:宋体"}

[**[reset ipv6 statistics ]{lang="EN-US"}**[\[ **chassis**]{lang="EN-US"}[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_12181_84059_1505565431}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12181_84059_1816095310}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12181_84059_103703285}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12181_84059_455409236}

[[network-admin]{lang="EN-US"}]{#struct_0_12181_84059_1005070037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12181_84059_758785003}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1190764814}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_1372883108}[：清除指定]{style="font-family:宋体"}[单板]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_x327329421}[：清除指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_12181_84059_x2039569071}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x1571743124}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_12181_84059_x473485130}[：清除指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_12181_84059_x513789151}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12181_84059_448153179}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12181_84059_1353458664}

[[\# ]{lang="EN-US"}]{#struct_0_12181_84059_x327263885}[清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文及]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 statistics]{lang="EN-US"}]{#struct_0_12181_84059_1537760895}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12181_84059_x1184557888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 statistics]{lang="EN-US"}**]{#struct_0_12181_84059_1427456271}
:::
