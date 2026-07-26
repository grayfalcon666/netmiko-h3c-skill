::: {#-1663023487 .myid}
[]{#_Toc404800171}[]{#struct_0_17327_x8313_1596218314}[]{#_Toc375561110}[]{#_Toc369852564}

**RIP \-- RIP probe命令 \-- display system internal rip database standby**

------------------------------------------------------------------------

[**[display system internal rip]{lang="EN-US"}**[ **database standby**]{lang="EN-US"}]{#struct_0_17327_x8313_1683993623}[命令用来显示备份的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[数据库的激活路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_268501425}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17327_x8313_1312111959}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rip]{lang="EN-US"}**[ *process-id* **database standby** \[ *ip-address* { *mask-length* \| *mask* } \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_x1251700624}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17327_x8313_236975047}[模式：]{style="font-family:宋体"}

[**[display system internal rip]{lang="EN-US"}**[ *process-id* **database standby**[ ]{style="color:blue"}\[ *ip-address* { *mask-length* \| *mask* } \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_x320846031}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1960581287}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_1595759562}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x519618862}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_33060792}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x982700706}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_223692045}

[*[process-id]{lang="EN-US"}*]{#struct_0_17327_x8313_1902643020}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_17327_x8313_1567534859}[：目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length/mask]{lang="EN-US"}*]{#struct_0_17327_x8313_x741923441}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x166945517}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定单板的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[数据库的激活路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x1239979855}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定成员设备的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[数据库的激活路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x477663574}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定成员设备上指定单板的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[数据库的激活路由]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17327_x8313_1595825098}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#299988245 .myid}
[]{#_Toc404800172}[]{#struct_0_17327_x8313_x557402754}[]{#_Toc375561111}[]{#_Toc369852565}

**RIP \-- RIP probe命令 \-- display system internal rip graceful-restart event-log**

------------------------------------------------------------------------

[**[display system internal rip]{lang="EN-US"}**[ **graceful-restart event-log**]{lang="EN-US"}]{#struct_0_17327_x8313_932186455}[命令用来显示]{style="font-family:宋体"}[RIP GR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1529053177}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17327_x8313_2050778632}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rip]{lang="EN-US"}**[ **graceful-restart event-log** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_x612057782}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17327_x8313_994788939}[模式：]{style="font-family:宋体"}

[**[display system internal rip graceful-restart event-log ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_1147501520}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x106973236}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_1985445163}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1595890634}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_967268263}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_511130529}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1308643854}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x687689976}[：显示指定单板的]{style="font-family:宋体"}[RIP GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_412554481}[：显示指定成员设备的]{style="font-family:宋体"}[RIP GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17327_x8313_710233235}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[RIP GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17327_x8313_1069752530}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1538919271 .myid}
[]{#_Toc404800173}[]{#struct_0_17327_x8313_x242146619}[]{#_Toc341285938}[]{#_Toc337801719}[]{#_Toc286220949}[]{#_Toc286220951}[]{#_Toc286220952}[]{#_Toc286220953}[]{#_Toc286220954}[]{#_Toc286220955}[]{#_Toc286220956}[]{#_Toc286220957}[]{#_Toc286220958}[]{#_Toc286220959}[]{#_Toc286220960}[]{#_Toc286220961}[]{#_Toc286220962}[]{#_Toc286220963}[]{#_Toc286220964}[]{#_Toc286220965}[]{#_Toc286220967}[]{#_Toc135620324}[]{#_Toc135620327}[]{#_Toc135620328}[]{#_Toc135620329}[]{#_Toc135620330}[]{#_Toc135620331}[]{#_Toc135620332}[]{#_Toc135620333}[]{#_Toc135620334}[]{#_Toc135620335}[]{#_Toc135620336}[]{#_Toc135620337}[]{#_Toc135620338}[]{#_Toc135620339}[]{#_Toc135620340}[]{#_Toc135620341}[]{#_Toc135620342}[]{#_Toc135620343}[]{#_Toc135620345}[]{#_Toc135620346}[]{#_Toc135620347}[]{#_Toc135620348}[]{#_Toc135620349}[]{#_Toc135620350}[]{#_Toc135620351}[]{#_Toc135620352}[]{#_Toc135620354}[]{#_Toc135620355}[]{#_Toc135620356}[]{#_Toc135620357}[]{#_Toc135620358}[]{#_Toc135620359}[]{#_Hlt5077351}[]{#_Toc135620360}[]{#_Toc135620361}[]{#_Toc135620362}[]{#_Toc135620363}[]{#_Toc135620364}[]{#_Toc135620365}[]{#_Toc135620366}[]{#_Toc135620367}[]{#_Toc135620368}[]{#_Toc135620369}[]{#_Toc286220969}[]{#_Toc286220970}[]{#_Toc286220971}[]{#_Toc286220972}[]{#_Toc286220973}[]{#_Toc286220974}[]{#_Toc286220975}[]{#_Toc286220976}[]{#_Toc286220977}[]{#_Toc286220978}[]{#_Toc286220979}[]{#_Toc286220980}[]{#_Toc286220981}[]{#_Toc286220982}[]{#_Toc286220983}[]{#_Toc286220984}[]{#_Toc286220985}[]{#_Toc286220987}[]{#_Toc286220990}[]{#_Toc286220991}[]{#_Toc286220992}[]{#_Toc286220993}[]{#_Toc286220994}[]{#_Toc286220995}[]{#_Toc286220996}[]{#_Toc286220997}[]{#_Toc286220998}[]{#_Toc286220999}[]{#_Toc286221000}[]{#_Toc286221001}[]{#_Toc286221002}[]{#_Toc286221003}[]{#_Toc286221004}[]{#_Toc286221005}[]{#_Toc286221006}[]{#_Toc286221007}[]{#_Toc286221008}[]{#_Toc286221009}[]{#_Toc286221011}[]{#_Toc185153148}[]{#_Toc185153317}[]{#_Toc185153358}[]{#_Toc185153149}[]{#_Toc185153318}[]{#_Toc185153359}[]{#_Toc338678034}[]{#_Toc341341645}[]{#_Toc341782454}[]{#_Toc341782702}[]{#_Toc137261554}[]{#_Toc137543101}[]{#_Toc137261556}[]{#_Toc137543103}[]{#_Toc137261557}[]{#_Toc137543104}[]{#_Toc137261558}[]{#_Toc137543105}[]{#_Toc137261559}[]{#_Toc137543106}[]{#_Toc137261560}[]{#_Toc137543107}[]{#_Toc137261561}[]{#_Toc137543108}[]{#_Toc137261562}[]{#_Toc137543109}[]{#_Toc137261563}[]{#_Toc137543110}[]{#_Toc137261568}[]{#_Toc137543115}[]{#_Toc137261572}[]{#_Toc137543119}[]{#_Toc137261603}[]{#_Toc137543150}[]{#_Toc338678037}

**RIP \-- RIP probe命令 \-- display system internal rip interface**

------------------------------------------------------------------------

[**[display system internal rip interface]{lang="EN-US"}**]{#struct_0_17327_x8313_x569027286}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1687859052}

[**[display system internal rip interface ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] \[ *interface-type* *interface-number* \| *ip-address* { *mask* \| *mask-length* } \]]{lang="EN-US"}]{#struct_0_17327_x8313_1395814229}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1608111597}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_1572570452}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1074121634}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_1275080914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x1965324539}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1801424658}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_17327_x8313_x1558419484}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x505009434}[：接口类型和接口编号。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_17327_x8313_x166589965}[：接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制，显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和掩码]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码长度接口的信息。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_17327_x8313_x1928859414}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_17327_x8313_1158960787}[：掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}
:::

::: {#-339137818 .myid}
[]{#_Toc404800174}[]{#struct_0_17327_x8313_1595956170}[]{#_Toc375561113}[]{#_Toc369852567}

**RIP \-- RIP probe命令 \-- display system internal rip interface standby**

------------------------------------------------------------------------

[**[display system internal rip interface standby]{lang="EN-US"}**]{#struct_0_17327_x8313_1596545994}[命令用来显示备份的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x259213855}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17327_x8313_x127495151}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ interface standby ]{lang="EN-US"}**[\[ *interface-type interface-number* \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_x1409309814}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17327_x8313_1426165464}[模式：]{style="font-family:宋体"}

[**[display system internal rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ interface standby ]{lang="EN-US"}**[\[ *interface-type interface-number* \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_862639602}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1633721199}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_x1160920872}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_296219677}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_329056901}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_77412126}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1596611530}

[*[process-id]{lang="EN-US"}*]{#struct_0_17327_x8313_x306060338}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x1664814977}[：接口类型和编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的所有接口信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x827715519}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定单板的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x1438080085}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定成员设备的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17327_x8313_1256330316}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定成员设备上指定单板的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接口信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x717347531}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#928413830 .myid}
[]{#_Toc404800175}[]{#struct_0_17327_x8313_1324828403}[]{#_Toc375561114}[]{#_Toc369852569}

**RIP \-- RIP probe命令 \-- display system internal rip neighbor standby**

------------------------------------------------------------------------

[**[display system internal rip neighbor standby]{lang="EN-US"}**]{#struct_0_17327_x8313_471783344}[命令用来显示备份的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1336840420}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17327_x8313_1596021707}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ neighbor standby ]{lang="EN-US"}**[\[ *interface-type interface-number* \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_87417873}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17327_x8313_831778264}[模式：]{style="font-family:宋体"}

[**[display system internal rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ neighbor standby ]{lang="EN-US"}**[\[ *interface-type interface-number* \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_x336906895}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1764820533}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_1092614675}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1226582736}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_169417842}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x454446153}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x697354518}

[*[process-id]{lang="EN-US"}*]{#struct_0_17327_x8313_x594741170}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17327_x8313_1596087243}[：接口类型和编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的所有邻居信息。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x1881551541}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定单板的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x1114833129}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定成员设备的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17327_x8313_551872057}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定成员设备上指定单板的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x1055132472}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#337925217 .myid}
[]{#_Toc216497585}[]{#_Toc137543160}[]{#_Toc33866017}[]{#_Toc306797772}[]{#_Toc305059803}[]{#_Toc189305424}[]{#_Toc321837765}[]{#_Toc303839441}[]{#_Toc404800176}[]{#struct_0_17327_x8313_x1965324538}[]{#_Toc341285939}[]{#_Toc360798239}[]{#_Toc360798240}[]{#_Toc360798241}[]{#_Toc360798242}[]{#_Toc360798243}[]{#_Toc360798244}[]{#_Toc360798245}[]{#_Toc360798246}[]{#_Toc360798247}[]{#_Toc360798248}[]{#_Toc360798249}[]{#_Toc360798250}[]{#_Toc360798251}[]{#_Toc360798252}[]{#_Toc360798253}[]{#_Toc360798254}[]{#_Toc360798255}[]{#_Toc360798256}[]{#_Toc360798257}[]{#_Toc360798258}[]{#_Toc360798259}[]{#_Toc360798260}[]{#_Toc360798261}[]{#_Toc360798262}[]{#_Toc360798263}[]{#_Toc360798264}[]{#_Toc360798265}[]{#_Toc360798266}[]{#_Toc360798267}[]{#_Toc360798268}[]{#_Toc360798269}[]{#_Toc360798270}[]{#_Toc360798271}[]{#_Toc360798272}[]{#_Toc360798273}[]{#_Toc360798274}[]{#_Toc360798275}[]{#_Toc360798276}[]{#_Toc360798277}[]{#_Toc360798278}[]{#_Toc360798279}[]{#_Toc360798280}[]{#_Toc360798281}[]{#_Toc360798282}[]{#_Toc360798283}[]{#_Toc360798284}[]{#_Toc360798285}[]{#_Toc360798286}[]{#_Toc360798287}[]{#_Toc360798288}[]{#_Toc360798289}[]{#_Toc360798290}[]{#_Toc360798291}[]{#_Toc360798292}[]{#_Toc360798353}[]{#_Toc341341648}[]{#_Toc341782457}[]{#_Toc341782705}[]{#_Toc341969264}[]{#_Toc286221018}[]{#_Toc286221019}[]{#_Toc286221020}[]{#_Toc286221021}[]{#_Toc286221022}[]{#_Toc286221023}[]{#_Toc286221024}[]{#_Toc286221025}[]{#_Toc286221026}[]{#_Toc286221027}[]{#_Toc286221028}[]{#_Toc286221029}[]{#_Toc286221030}[]{#_Toc286221031}[]{#_Toc286221032}[]{#_Toc286221033}[]{#_Toc286221034}[]{#_Toc286221035}[]{#_Toc286221036}[]{#_Toc286221037}[]{#_Toc286221040}[]{#_Toc286221043}[]{#_Toc286221046}[]{#_Toc286221047}[]{#_Toc286221050}[]{#_Toc286221053}[]{#_Toc286221057}[]{#_Toc286221058}[]{#_Toc286221059}[]{#_Toc286221060}[]{#_Toc286221061}[]{#_Toc286221062}[]{#_Toc286221063}[]{#_Toc286221064}[]{#_Toc286221065}[]{#_Toc286221066}[]{#_Toc286221067}[]{#_Toc286221068}[]{#_Toc286221069}[]{#_Toc286221070}[]{#_Toc286221071}[]{#_Toc286221072}[]{#_Toc286221073}[]{#_Toc286221074}[]{#_Toc286221075}[]{#_Toc286221076}[]{#_Toc286221077}[]{#_Toc286221078}[]{#_Toc286221079}[]{#_Toc286221080}[]{#_Toc286221081}[]{#_Toc286221087}[]{#_Toc286221088}[]{#_Toc286221089}[]{#_Toc286221090}[]{#_Toc286221095}[]{#_Toc286221096}[]{#_Toc286221097}[]{#_Toc286221098}[]{#_Toc286221099}[]{#_Toc286221100}[]{#_Toc286221101}[]{#_Toc286221102}[]{#_Toc286221103}[]{#_Toc286221104}[]{#_Toc286221105}[]{#_Toc286221106}[]{#_Toc286221107}[]{#_Toc286221108}[]{#_Toc286221109}[]{#_Toc286221110}[]{#_Toc286221111}[]{#_Toc286221112}[]{#_Toc286221113}[]{#_Toc286221114}[]{#_Toc286221115}[]{#_Toc286221116}[]{#_Toc286221117}[]{#_Toc286221123}[]{#_Toc286221124}[]{#_Toc286221125}[]{#_Toc286221126}[]{#_Toc286221131}[]{#_Toc286221132}[]{#_Toc286221134}[]{#_Toc286221135}[]{#_Toc286221136}[]{#_Toc286221137}[]{#_Toc286221138}[]{#_Toc286221139}[]{#_Toc286221140}[]{#_Toc286221141}[]{#_Toc286221142}[]{#_Toc286221143}[]{#_Toc286221144}[]{#_Toc286221145}[]{#_Toc286221146}[]{#_Toc286221147}[]{#_Toc286221148}[]{#_Toc286221149}[]{#_Toc286221150}[]{#_Toc286221151}[]{#_Toc286221155}[]{#_Toc286221156}[]{#_Toc286221158}[]{#_Toc286221159}[]{#_Toc286221160}[]{#_Toc286221161}[]{#_Toc286221162}[]{#_Toc286221163}[]{#_Toc286221164}[]{#_Toc286221165}[]{#_Toc286221166}[]{#_Toc286221167}[]{#_Toc286221168}[]{#_Toc286221169}[]{#_Toc286221170}[]{#_Toc286221171}[]{#_Toc286221172}[]{#_Toc286221173}[]{#_Toc286221174}[]{#_Toc286221175}[]{#_Toc286221176}[]{#_Toc286221177}[]{#_Toc286221178}[]{#_Toc286221179}[]{#_Toc286221180}[]{#_Toc286221182}[]{#_Toc286221184}[]{#_Toc286221186}[]{#_Toc137261609}[]{#_Toc137543156}[]{#_Toc137261610}[]{#_Toc137543157}[]{#_Toc137261611}[]{#_Toc137543158}[]{#_Toc286221188}[]{#_Toc286221189}[]{#_Toc286221190}[]{#_Toc286221191}[]{#_Toc286221192}[]{#_Toc286221193}[]{#_Toc286221194}[]{#_Toc286221195}[]{#_Toc286221196}[]{#_Toc286221197}[]{#_Toc286221198}[]{#_Toc286221199}[]{#_Toc286221200}[]{#_Toc286221201}[]{#_Toc286221202}

**RIP \-- RIP probe命令 \-- display system internal rip nib**

------------------------------------------------------------------------

[**[display system internal rip nib]{lang="EN-US"}**]{#struct_0_17327_x8313_927458697}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由下一跳信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_286658089}

[**[display system internal rip nib]{lang="EN-US"}**[ \[ *nib-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17327_x8313_x1602533531}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1582138022}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_x1718031983}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1101891791}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x1317695320}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_1602688167}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1965213817}

[*[nib-id]{lang="EN-US"}*]{#struct_0_17327_x8313_x1965390074}[：下一跳]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFFFFFF]{lang="EN-US"}[。如果不指定，显示所有下一跳信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17327_x8313_1927174483}[：显示下一跳详细信息。]{style="font-family:宋体"}
:::

::: {#2134898753 .myid}
[]{#_Toc404800177}[]{#struct_0_17327_x8313_2032074960}[]{#_Toc341285940}[]{#_Toc360798355}[]{#_Toc360798356}[]{#_Toc360798357}[]{#_Toc360798358}[]{#_Toc360798359}[]{#_Toc360798360}[]{#_Toc360798361}[]{#_Toc360798362}[]{#_Toc360798363}[]{#_Toc360798364}[]{#_Toc360798365}[]{#_Toc360798366}[]{#_Toc360798367}[]{#_Toc360798368}[]{#_Toc360798369}[]{#_Toc360798370}[]{#_Toc360798371}[]{#_Toc360798425}[]{#_Toc360798426}[]{#_Toc360798427}[]{#_Toc360798428}[]{#_Toc360798429}[]{#_Toc360798430}[]{#_Toc360798431}[]{#_Toc360798432}[]{#_Toc360798433}[]{#_Toc360798434}[]{#_Toc360798435}[]{#_Toc360798436}[]{#_Toc360798437}[]{#_Toc360798438}[]{#_Toc360798439}[]{#_Toc360798440}[]{#_Toc360798441}[]{#_Toc360798442}[]{#_Toc360798443}[]{#_Toc360798444}[]{#_Toc360798445}[]{#_Toc360798446}[]{#_Toc360798447}[]{#_Toc360798448}[]{#_Toc360798449}[]{#_Toc360798450}[]{#_Toc360798451}[]{#_Toc360798452}[]{#_Toc360798453}[]{#_Toc360798454}[]{#_Toc360798455}[]{#_Toc360798456}[]{#_Toc360798457}[]{#_Toc360798506}

**RIP \-- RIP probe命令 \-- display system internal rip nib log**

------------------------------------------------------------------------

[**[display system internal rip nib log]{lang="EN-US"}**]{#struct_0_17327_x8313_x787335628}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由下一跳日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1734505555}

[**[display system internal rip nib log]{lang="EN-US"}**]{#struct_0_17327_x8313_x2144766590}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x296175833}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_2034533234}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x942768811}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x1734035894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_2144874407}
:::

::: {#-1351848175 .myid}
[]{#_Toc404800178}[]{#struct_0_17327_x8313_1596218315}[]{#_Toc375561117}[]{#_Toc369852570}

**RIP \-- RIP probe命令 \-- display system internal rip non-stop-routing event-log**

------------------------------------------------------------------------

[**[display system internal rip]{lang="EN-US"}**[ **non-stop-routing event-log**]{lang="EN-US"}]{#struct_0_17327_x8313_1683928087}[命令用来显示]{style="font-family:宋体"}[RIP NSR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x2014981766}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17327_x8313_1906046266}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rip]{lang="EN-US"}**[ **non-stop-routing event-log** **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_2081754406}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17327_x8313_48446782}[模式：]{style="font-family:宋体"}

[**[display system internal rip non-stop-routing event-log ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_x988227500}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_575906329}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_x1784170940}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1529974430}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_1595759563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x519684398}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1501125293}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x1479732752}[：显示指定单板的]{style="font-family:宋体"}[RIP NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_1852782837}[：显示指定成员设备的]{style="font-family:宋体"}[RIP NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x1717683331}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[RIP NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17327_x8313_1342310457}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-437857611 .myid}
[]{#_Toc404800179}[]{#struct_0_17327_x8313_x1966324746}[]{#_Toc375561118}[]{#_Toc369852572}

**RIP \-- RIP probe命令 \-- display system internal rip route standby**

------------------------------------------------------------------------

[**[display system internal rip route standby]{lang="EN-US"}**]{#struct_0_17327_x8313_121348488}[命令用来显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_17327_x8313_x1851599083}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17327_x8313_1595825099}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ route standby ]{lang="EN-US"}**[\[ *ip-address* { *mask-length* \| *mask* } \[ **verbose** \] \| **peer** *ip-address* \| **statistics** \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_x557337218}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17327_x8313_x1020214775}[模式：]{style="font-family:宋体"}

[**[display system internal rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ route standby ]{lang="EN-US"}**[\[ *ip-address* { *mask-length* \| *mask* } \[ **verbose** \] \| **peer** *ip-address* \| **statistics** \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_x777359722}

[[【视图】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_17327_x8313_x1427969848}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_529281312}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_17327_x8313_1883760754}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_1588557590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x207039322}

[[【参数】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_17327_x8313_1265699315}

[*[process-id]{lang="EN-US"}*]{#struct_0_17327_x8313_181740364}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_17327_x8313_1595890635}[：目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length/mask]{lang="EN-US"}*]{#struct_0_17327_x8313_967202727}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17327_x8313_894146972}[：显示当前]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由表中指定目的地址和掩码的所有路由信息。如果未指定本参数，则只显示指定目的地址和掩码的最优]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**]{#struct_0_17327_x8313_322532972}*[ip-address]{lang="EN-US"}*[：显示从指定邻居学到的所有路由信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_17327_x8313_x2051259282}[：显示路由的统计信息。路由的统计信息包括路由总数目，各个邻居的路由数目。]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_906065946}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定单板的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_205930735}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定成员设备的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x1502484565}[：显示]{style="font-family:宋体"}[备份的]{style="font-family:宋体"}[指定成员设备上指定单板的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x1616968462}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#785971719 .myid}
[]{#_Toc404800180}[]{#struct_0_17327_x8313_814195517}[]{#_Toc341777610}[]{#_Toc360798508}[]{#_Toc360798509}[]{#_Toc360798510}[]{#_Toc360798511}[]{#_Toc360798512}[]{#_Toc360798513}[]{#_Toc360798514}[]{#_Toc360798515}[]{#_Toc360798516}[]{#_Toc360798517}[]{#_Toc360798518}[]{#_Toc360798519}[]{#_Toc360798520}[]{#_Toc360798521}[]{#_Toc360798522}[]{#_Toc360798523}[]{#_Toc360798524}[]{#_Toc360798525}[]{#_Toc360798526}[]{#_Toc360798527}[]{#_Toc360798528}[]{#_Toc360798529}[]{#_Toc360798530}[]{#_Toc360798531}[]{#_Toc360798532}[]{#_Toc360798533}[]{#_Toc360798534}[]{#_Toc360798535}[]{#_Toc360798587}

**RIP \-- RIP probe命令 \-- display system internal rip status**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}[ system internal rip status]{lang="EN-US"}**]{#struct_0_17327_x8313_1809776826}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议全局状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x42092729}

[**[display]{lang="EN-US"}[ system internal rip status]{lang="EN-US"}**]{#struct_0_17327_x8313_63016235}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1711956313}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_695841708}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x40380717}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_1770737588}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_1596881844}
:::

::: {#1151434578 .myid}
[]{#_Toc404800181}[]{#struct_0_17327_x8313_1595956171}[]{#_Toc375561120}[]{#_Toc369852575}[]{#_Toc292815525}[]{#_Toc216497581}[]{#_Toc137543153}[]{#_Toc286221208}[]{#_Toc286221209}[]{#_Toc286221210}[]{#_Toc286221211}[]{#_Toc286221212}[]{#_Toc286221213}[]{#_Toc286221214}[]{#_Toc286221215}[]{#_Toc286221216}[]{#_Toc286221217}[]{#_Toc286221218}[]{#_Toc286221219}[]{#_Toc286221220}[]{#_Toc286221221}[]{#_Toc286221222}[]{#_Toc286221223}[]{#_Toc286221228}[]{#_Toc286221230}[]{#_Toc286221231}[]{#_Toc286221232}[]{#_Toc286221233}[]{#_Toc286221234}[]{#_Toc286221235}[]{#_Toc286221236}[]{#_Toc286221237}[]{#_Toc286221238}[]{#_Toc286221239}[]{#_Toc286221240}[]{#_Toc286221241}[]{#_Toc286221242}[]{#_Toc286221243}[]{#_Toc286221244}[]{#_Toc286221245}[]{#_Toc286221247}[]{#_Toc286221248}[]{#_Toc137543164}[]{#_Toc137543165}[]{#_Toc137543166}[]{#_Toc137543167}[]{#_Toc137543168}[]{#_Toc137543169}[]{#_Toc137543170}[]{#_Toc137543171}[]{#_Toc137543172}[]{#_Toc137543173}[]{#_Toc137543174}[]{#_Toc137543175}[]{#_Toc137543176}[]{#_Toc137543177}[]{#_Toc137543178}[]{#_Toc137543179}[]{#_Toc137543180}[]{#_Toc137543181}[]{#_Toc137543182}[]{#_Toc137543183}[]{#_Toc137543184}[]{#_Toc137543185}[]{#_Toc137543186}[]{#_Toc137543187}[]{#_Toc137543188}[]{#_Toc137543189}[]{#_Toc137543190}[]{#_Toc286221249}[]{#_Toc286221250}[]{#_Toc286221251}[]{#_Toc286221252}[]{#_Toc286221253}[]{#_Toc286221254}[]{#_Toc286221255}[]{#_Toc286221256}[]{#_Toc286221257}[]{#_Toc286221258}[]{#_Toc286221259}[]{#_Toc286221260}[]{#_Toc286221261}[]{#_Toc286221262}[]{#_Toc286221263}[]{#_Toc286221264}[]{#_Toc286221266}[]{#_Toc286221267}[]{#_Toc286221268}[]{#_Toc286221269}[]{#_Toc286221270}[]{#_Toc286221271}[]{#_Toc286221272}[]{#_Toc286221273}[]{#_Toc286221274}[]{#_Toc286221275}[]{#_Toc286221276}[]{#_Toc286221277}[]{#_Toc286221278}[]{#_Toc286221281}[]{#_Toc286221283}[]{#_Toc286221284}[]{#_Toc286221285}[]{#_Toc286221286}[]{#_Toc286221287}[]{#_Toc286221288}[]{#_Toc286221289}[]{#_Toc286221290}[]{#_Toc286221291}[]{#_Toc286221292}[]{#_Toc286221293}[]{#_Toc286221294}[]{#_Toc286221295}[]{#_Toc286221296}[]{#_Toc286221297}[]{#_Toc286221298}[]{#_Toc286221299}[]{#_Toc286221300}[]{#_Toc286221301}[]{#_Toc286221302}[]{#_Toc286221303}[]{#_Toc286221304}[]{#_Toc286221305}[]{#_Toc286221307}[]{#_Toc286221310}[]{#_Toc286221311}[]{#_Toc286221316}[]{#_Toc286221317}[]{#_Toc286221320}[]{#_Toc286221321}[]{#_Toc286221322}[]{#_Toc286221323}[]{#_Toc286221324}[]{#_Toc286221325}[]{#_Toc286221326}[]{#_Toc286221327}[]{#_Toc286221328}[]{#_Toc286221329}[]{#_Toc286221330}[]{#_Toc286221331}[]{#_Toc286221332}[]{#_Toc286221333}[]{#_Toc286221334}[]{#_Toc286221335}[]{#_Toc286221337}[]{#_Toc286221338}[]{#_Toc286221339}[]{#_Toc286221340}[]{#_Toc286221342}[]{#_Toc286221343}[]{#_Toc286221344}[]{#_Toc286221345}[]{#_Toc286221346}[]{#_Toc286221347}[]{#_Toc286221348}[]{#_Toc286221349}[]{#_Toc286221350}[]{#_Toc286221351}[]{#_Toc286221352}[]{#_Toc286221353}[]{#_Toc286221354}[]{#_Toc286221355}[]{#_Toc286221356}[]{#_Toc286221357}[]{#_Toc286221358}[]{#_Toc286221359}[]{#_Toc286221360}[]{#_Toc286221361}[]{#_Toc286221362}[]{#_Toc286221363}[]{#_Toc286221364}[]{#_Toc286221365}[]{#_Toc286221366}[]{#_Toc286221368}[]{#_Toc286221369}[]{#_Toc286221370}[]{#_Toc286221371}[]{#_Toc286221374}[]{#_Toc286221376}[]{#_Toc286221377}[]{#_Toc286221378}[]{#_Toc286221379}[]{#_Toc286221380}[]{#_Toc286221381}[]{#_Toc286221382}[]{#_Toc286221383}[]{#_Toc286221384}[]{#_Toc286221385}[]{#_Toc286221386}[]{#_Toc286221387}[]{#_Toc286221388}[]{#_Toc286221389}[]{#_Toc286221390}[]{#_Toc286221392}[]{#_Toc286221393}[]{#_Toc286221394}[]{#_Toc286221395}[]{#_Toc286221400}[]{#_Toc286221401}[]{#_Toc286221402}[]{#_Toc286221403}[]{#_Toc286221404}[]{#_Toc286221405}[]{#_Toc286221406}[]{#_Toc286221407}[]{#_Toc286221408}[]{#_Toc286221409}[]{#_Toc286221410}[]{#_Toc286221411}[]{#_Toc286221412}[]{#_Toc286221413}[]{#_Toc286221414}[]{#_Toc286221415}[]{#_Toc286221416}[]{#_Toc286221417}[]{#_Toc286221418}[]{#_Toc286221419}[]{#_Toc286221420}[]{#_Toc286221421}[]{#_Toc286221422}[]{#_Toc286221423}[]{#_Toc286221425}[]{#_Toc286221426}[]{#_Toc286221427}[]{#_Toc286221428}[]{#_Toc286221429}[]{#_Toc286221430}[]{#_Toc286221431}[]{#_Toc286221432}[]{#_Toc286221433}[]{#_Toc286221434}[]{#_Toc286221435}[]{#_Toc286221437}[]{#_Toc286221438}[]{#_Toc286221439}[]{#_Toc286221440}[]{#_Toc286221441}[]{#_Toc286221442}[]{#_Toc286221443}[]{#_Toc286221444}[]{#_Toc286221445}[]{#_Toc286221446}[]{#_Toc286221447}[]{#_Toc286221448}[]{#_Toc286221449}[]{#_Toc286221450}[]{#_Toc286221451}[]{#_Toc286221452}[]{#_Toc286221453}[]{#_Toc286221454}[]{#_Toc286221455}[]{#_Toc286221456}[]{#_Toc286221457}[]{#_Toc286221458}[]{#_Toc286221459}[]{#_Toc286221460}[]{#_Toc286221462}[]{#_Toc286221463}[]{#_Toc286221464}[]{#_Toc286221465}[]{#_Toc286221466}[]{#_Toc286221467}[]{#_Toc286221468}[]{#_Toc286221469}[]{#_Toc286221470}[]{#_Toc286221472}[]{#_Toc286221474}[]{#_Toc286221475}[]{#_Toc286221476}[]{#_Toc286221477}[]{#_Toc286221478}[]{#_Toc286221479}[]{#_Toc286221480}[]{#_Toc286221481}[]{#_Toc286221482}[]{#_Toc286221483}[]{#_Toc286221484}[]{#_Toc286221485}[]{#_Toc286221486}[]{#_Toc286221487}[]{#_Toc286221490}[]{#_Toc286221491}[]{#_Toc137261626}[]{#_Toc137543199}[]{#_Toc137261627}[]{#_Toc137543200}[]{#_Toc137261628}[]{#_Toc137543201}[]{#_Toc137261629}[]{#_Toc137543202}[]{#_Toc137261630}[]{#_Toc137543203}[]{#_Toc137261631}[]{#_Toc137543204}[]{#_Toc137261632}[]{#_Toc137543205}[]{#_Toc137261633}[]{#_Toc137543206}[]{#_Toc137261634}[]{#_Toc137543207}[]{#_Toc137261635}[]{#_Toc137543208}[]{#_Toc137261636}[]{#_Toc137543209}[]{#_Toc137261637}[]{#_Toc137543210}[]{#_Toc137261638}[]{#_Toc137543211}[]{#_Toc137261639}[]{#_Toc137543212}[]{#_Toc137261640}[]{#_Toc137543213}[]{#_Toc137261641}[]{#_Toc137543214}[]{#_Toc137261642}[]{#_Toc137543215}[]{#_Toc286221493}[]{#_Toc286221494}[]{#_Toc286221495}[]{#_Toc286221496}[]{#_Toc286221497}[]{#_Toc286221498}[]{#_Toc286221499}[]{#_Toc286221500}[]{#_Toc286221501}[]{#_Toc286221502}[]{#_Toc286221503}[]{#_Toc286221504}[]{#_Toc286221505}[]{#_Toc286221506}[]{#_Toc286221507}[]{#_Toc286221511}[]{#_Toc286221512}[]{#_Toc292815538}[]{#_Toc157826816}[]{#_Toc286221520}[]{#_Toc286221523}[]{#_Toc286221524}[]{#_Toc286221525}[]{#_Toc286221526}[]{#_Toc286221527}[]{#_Toc286221528}[]{#_Toc286221529}[]{#_Toc286221530}[]{#_Toc286221531}[]{#_Toc286221532}[]{#_Toc286221533}[]{#_Toc286221534}[]{#_Toc286221535}[]{#_Toc286221536}[]{#_Toc286221537}[]{#_Toc286221540}[]{#_Toc286221542}[]{#_Toc286221543}[]{#_Toc286221544}[]{#_Toc286221545}[]{#_Toc286221546}[]{#_Toc286221547}[]{#_Toc286221548}[]{#_Toc286221549}[]{#_Toc286221550}[]{#_Toc286221551}[]{#_Toc286221552}[]{#_Toc286221553}[]{#_Toc286221554}[]{#_Toc286221555}[]{#_Toc286221556}[]{#_Toc286221557}[]{#_Toc286221558}[]{#_Toc286221562}[]{#_Toc286221563}[]{#_Toc286221564}[]{#_Toc286221565}[]{#_Toc286221570}[]{#_Toc286221573}[]{#_Toc286221574}[]{#_Toc286221576}[]{#_Toc286221577}[]{#_Toc286221578}[]{#_Toc286221579}[]{#_Toc286221580}[]{#_Toc286221581}[]{#_Toc286221582}[]{#_Toc286221583}[]{#_Toc286221584}[]{#_Toc286221585}[]{#_Toc286221586}[]{#_Toc286221587}[]{#_Toc286221588}[]{#_Toc286221589}[]{#_Toc286221590}[]{#_Toc286221595}[]{#_Toc286221597}[]{#_Toc286221598}[]{#_Toc286221599}[]{#_Toc286221600}[]{#_Toc286221601}[]{#_Toc286221602}[]{#_Toc286221603}[]{#_Toc286221604}[]{#_Toc286221605}[]{#_Toc286221606}[]{#_Toc286221607}[]{#_Toc286221608}[]{#_Toc286221609}[]{#_Toc286221610}[]{#_Toc286221611}[]{#_Toc286221612}[]{#_Toc286221615}[]{#_Toc286221617}[]{#_Toc286221618}[]{#_Toc286221620}[]{#_Toc286221621}[]{#_Toc286221622}[]{#_Toc286221623}[]{#_Toc286221624}[]{#_Toc286221625}[]{#_Toc286221626}[]{#_Toc286221627}[]{#_Toc286221628}[]{#_Toc286221629}[]{#_Toc286221630}[]{#_Toc286221631}

**RIP \-- RIP probe命令 \-- reset system internal rip graceful-restart event-log**

------------------------------------------------------------------------

[**[reset system internal rip graceful-restart event-log]{lang="ES"}**]{#struct_0_17327_x8313_x1331543872}[命令用来清除]{style="font-family:宋体"}[RIP GR]{lang="ES"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1436450467}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_17327_x8313_1765282965}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="ES"}[集中式]{style="font-family:宋体"}[IRF]{lang="ES"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset system internal rip graceful-restart event-log]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_896023877}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17327_x8313_x266024770}[模式：]{style="font-family:宋体"}

[**[reset system internal rip graceful-restart event-log]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_1596545995}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x259148319}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_628266719}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x233261423}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x583504556}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_x978446535}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x1935688158}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_971737784}[：清除指定单板的]{style="font-family:宋体"}[RIP GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_1652856814}[：清除指定成员设备的]{style="font-family:宋体"}[RIP GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x682465177}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[RIP GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17327_x8313_664570871}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1605202035 .myid}
[]{#_Toc404800182}[]{#struct_0_17327_x8313_1596611531}[]{#_Toc375561121}[]{#_Toc369852576}

**RIP \-- RIP probe命令 \-- reset system internal rip non-stop-routing event-log**

------------------------------------------------------------------------

[**[reset system internal rip non-stop-routing event-log]{lang="ES"}**]{#struct_0_17327_x8313_x306125874}[命令用来清除]{style="font-family:宋体"}[RIP NSR]{lang="ES"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x869058591}

[[分布式设备]{style="font-family:宋体"}]{#struct_0_17327_x8313_2121628543}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="ES"}[集中式]{style="font-family:宋体"}[IRF]{lang="ES"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset system internal rip non-stop-routing event-log]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_1298844797}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17327_x8313_x510121448}[模式：]{style="font-family:宋体"}

[**[reset system internal rip non-stop-routing event-log]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17327_x8313_1068457338}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17327_x8313_x418544762}

[[Probe]{lang="EN-US"}]{#struct_0_17327_x8313_1105241324}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17327_x8313_1327995077}

[[network-admin]{lang="EN-US"}]{#struct_0_17327_x8313_788321515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17327_x8313_1596021712}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17327_x8313_87090194}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x756404631}[：清除指定单板的]{style="font-family:宋体"}[RIP NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[standby slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17327_x8313_x819322849}[：清除指定成员设备的]{style="font-family:宋体"}[RIP NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[standby chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17327_x8313_x492902134}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[RIP NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17327_x8313_175652179}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
