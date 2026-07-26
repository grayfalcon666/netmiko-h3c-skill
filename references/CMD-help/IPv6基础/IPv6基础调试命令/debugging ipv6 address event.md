::: {#-1876736401 .myid}
[]{#_Toc404786742}[]{#struct_0_11651_x1037_x551160872}

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 address event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1033637374}

[**[debugging ipv6 address event]{lang="EN-US"}**]{#struct_0_11651_x1037_495905422}

[**[undo debugging ipv6 address event]{lang="EN-US"}**]{#struct_0_11651_x1037_714030496}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1455642501}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1500234855}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1300007798}

[[network-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x110132814}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x961384387}

[[【描述】]{style="font-family:黑体"}]{#struct_0_11651_x1037_64025431}

[**[debugging ipv6 address event]{lang="EN-US"}**]{#struct_0_11651_x1037_x1078747480}[命令用来打开]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址事件的调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 address event]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址时间的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x741788774}[地址事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ipv6 address event]{lang="EN-US"}]{#struct_0_11651_x1037_983152201}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1007804115}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1377690665}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_x557564700}

[[Event type]{lang="EN-US"}]{#struct_0_11651_x1037_x217374723}

[[事件类型]{style="font-family:宋体"}]{#struct_0_11651_x1037_x960925634}

[[module]{lang="EN-US"}]{#struct_0_11651_x1037_x1490196305}

[[被通知的模块]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_11651_x1037_x1554457258}

[[Prefix Len]{lang="EN-US"}]{#struct_0_11651_x1037_510057704}

[[前缀长度]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1168150240}

[[VPN Index]{lang="EN-US"}]{#struct_0_11651_x1037_1294686976}

[[Vpn]{lang="EN-US"}]{#struct_0_11651_x1037_1365787034}[索引]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_11651_x1037_x960860098}

[[接口名]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1110564401}

**[ ]{lang="EN-US"}**

[[【举例】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1525339433}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_x1190038147}[在设备上配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址事件的调试信息开关，配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2012::6664]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 address event]{lang="EN-US"}]{#struct_0_11651_x1037_x558814797}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip address 2012::6664]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]]{lang="EN-US"}

[\*Dec 3 15:13:01:182 2012 Sysname IP6ADDR/7/EVENT: -MDC=1;]{lang="EN-US"}

[IPv6 prefix event type 0x20001 notified to module 0x04040000,]{lang="EN-US"}

[Prefix: 2012::, Prefix Length: 64, VPN Index: 0, Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[\*Dec 3 15:13:01:381 2012 Sysname IP6ADDR/7/EVENT: -MDC=1;]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPv6 address event type 0x10001 notified to module 0x04040000,]{lang="EN-US"}

[Prefix 2012::66, Prefix Length: 64, VPN Index: 0, Interface: GigabitEthernet1/0/1]{lang="EN-US"}

::: {#-1964977021 .myid}
[]{#_Toc59352314}[]{#_Toc404786743}[]{#struct_0_11651_x1037_x960794562}

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1482689583}

[**[debugging ipv6 error]{lang="EN-US"}**]{#struct_0_11651_x1037_1832200683}

[**[undo debugging ipv6 error]{lang="EN-US"}**]{#struct_0_11651_x1037_856888661}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1834691069}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1198481352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11651_x1037_932707925}

[[network-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x1186108706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x1568543793}

[[【描述】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x2027439111}

[**[debugging ipv6 error]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_11651_x1037_x960729026}[命令用来打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的错误调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 error]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_1270083884}[报文的错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging ipv6 error]{lang="EN-US"}]{#struct_0_11651_x1037_951298458}[[命令输出信息描述表]{style="font-size:9.0pt;font-family:黑体"}]{.TableHeadingChar}

[]{#table_struct_0_x1014018133}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_115209849}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_x179189280}

[[Number of IPv6 fragments exceeded the threshold.]{lang="EN-US"}]{#struct_0_11651_x1037_x832903039}

[[分片报文的数量超过了限制]{style="font-family:宋体"}]{#struct_0_11651_x1037_x326215790}

[[Number of IPv6 reassembly queues exceeded the threshold.]{lang="EN-US"}]{#struct_0_11651_x1037_x960663490}

[[重组队列的数量超过了限制]{style="font-family:宋体"}]{#struct_0_11651_x1037_2015919966}

[[Invalid IPv6 packet.]{lang="EN-US"}]{#struct_0_11651_x1037_130230162}

[[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_1713215658}[报文非法]{style="font-family:宋体"}

[[Failed to process the hop-by-hop extension header.]{lang="EN-US"}]{#struct_0_11651_x1037_1145529148}

[[处理报文中逐跳扩展头失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_749952162}

[[Failed to process the hop-by-hop option.]{lang="EN-US"}]{#struct_0_11651_x1037_2093992427}

[[处理报文中逐跳选项失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_x960597954}

[[The packet was discarded by services.]{lang="EN-US"}]{#struct_0_11651_x1037_1644450151}

[[业务禁止报文]{style="font-family:宋体"}]{#struct_0_11651_x1037_1342587726}

[[The packet was administratively discarded.]{lang="EN-US"}]{#struct_0_11651_x1037_x14943190}

[[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x1510832663}[报文被管理禁止]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1740600498}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_x960532418}[在一台支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能并在接口下配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的设备上打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的错误调试信息开关，设备收到很多分片报文。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 error]{lang="EN-US"}]{#struct_0_11651_x1037_x701756836}

[\*Aug  4 01:42:06:375 2010 Sysname IP6FW/3/debug_error:]{lang="EN-US"}

[Number of IPv6 fragments exceeded the threshold. Interface is GigabitEthernet1/0/1]{lang="EN-US"}

::: {#-2129694383 .myid}
[]{#_Toc404786744}[]{#struct_0_11651_x1037_x779298121}[]{#_Toc281378362}[]{#_Toc269369450}[]{#_Toc350330598}

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 icmp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1225040638}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_11651_x1037_59847192}

[**[debugging ipv6 icmp]{lang="EN-US"}**]{#struct_0_11651_x1037_x153995525}

[**[undo debugging ipv6 icmp]{lang="EN-US"}**]{#struct_0_11651_x1037_x1321096219}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11651_x1037_x1735460215}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging ipv6 icmp]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_11651_x1037_2047673400}

[**[undo ]{lang="EN-US"}[debugging ipv6 icmp]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_11651_x1037_x960466882}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11651_x1037_848092398}[模式：]{style="font-family:宋体"}

[**[debugging ipv6 icmp]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_11651_x1037_x203743873}

[**[undo debugging ipv6 icmp]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_11651_x1037_391740649}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1262164396}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1387047513}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1193544727}

[[network-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x1642453871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11651_x1037_1505163757}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x961449922}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11651_x1037_x1824788215}[：显示指定单板的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_11651_x1037_x334260642}[：显示指定]{style="font-family:宋体"}[成员设备的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_11651_x1037_1105660406}[：显示指定]{style="font-family:宋体"}[成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11651_x1037_1045750253}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11651_x1037_1325081512}[：显示指定单板的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_11651_x1037_x1975906509}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_11651_x1037_581321594}

[**[debugging ipv6 icmp]{lang="EN-US"}**]{#struct_0_11651_x1037_x1960226256}[命令用来打开]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 icmp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging ipv6 icmp]{lang="EN-US"}]{#struct_0_11651_x1037_63959895}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1017967684}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_x440455521}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_588362623}

[[ICMP6 Output]{lang="EN-US"}]{#struct_0_11651_x1037_1166407596}

[[发送报文的操作]{style="font-family:宋体"}]{#struct_0_11651_x1037_x960925637}

[[ICMP6 Input]{lang="EN-US"}]{#struct_0_11651_x1037_x1489999697}

[[接收报文的操作]{style="font-family:宋体"}]{#struct_0_11651_x1037_x14355102}

[[src]{lang="EN-US"}]{#struct_0_11651_x1037_x1848146488}

[[报文源地址]{style="font-family:宋体"}]{#struct_0_11651_x1037_869355295}

[[dst]{lang="EN-US"}]{#struct_0_11651_x1037_x1086814025}

[[报文目的地址]{style="font-family:宋体"}]{#struct_0_11651_x1037_x960860101}

[[type]{lang="EN-US"}]{#struct_0_11651_x1037_1227629000}

[[ICMPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x588690159}[消息的类型]{style="font-family:宋体"}

[[code]{lang="EN-US"}]{#struct_0_11651_x1037_936461616}

[[ICMPv6]{lang="EN-US"}]{#struct_0_11651_x1037_317402318}[消息的代码，可将某一类型的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[消息细分为更具体的用途]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1011065128}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_x1211866376}[打开]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[调试信息开关，收到]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文时输入下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 icmp]{lang="EN-US"}]{#struct_0_11651_x1037_x960794565}

[\*Dec 24 18:07:49:132 2010 Sysname SOCKET/7/ICMPv6:]{lang="EN-US"}

[ICMP6 Input:]{lang="EN-US"}

[ ICMPv6 Packet: src = 2222::1234, dst = 2222::2222]{lang="EN-US"}

[                type = 128, code = 0 (echo-request)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_x1482624047}*[接收]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#-2110598118 .myid}
[]{#_Toc59352311}[]{#_Toc404786745}[]{#struct_0_11651_x1037_354188074}[]{#_Toc279581741}[]{#_Toc132549860}[]{#_Toc59352313}

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 nd**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_11651_x1037_732183015}

[**[debugging ipv6 nd ]{lang="EN-US"}**[{ **entry** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_11651_x1037_1550392165}

[**[undo debugging ipv6 nd ]{lang="EN-US"}**[{ **entry** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_11651_x1037_852573183}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1195098623}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11651_x1037_894743511}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x960729029}

[[network-admin]{lang="EN-US"}]{#struct_0_11651_x1037_1270804780}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x1008925069}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x2092908706}

[**[entry]{lang="EN-US"}**]{#struct_0_11651_x1037_832484532}[：表示邻居发现的表项信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_11651_x1037_1720381598}[：表示邻居发现的错误信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_11651_x1037_x1441093484}[：表示邻居发现的报文信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1272473879}

[**[debugging ipv6 nd]{lang="EN-US"}**]{#struct_0_11651_x1037_1229302043}[命令用来打开邻居发现的调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 nd]{lang="EN-US"}**[命令用来关闭邻居发现的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，邻居发现的调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1917182667}

[[表1-4 ]{lang="EN-US"}[debugging ipv6 nd packet]{lang="EN-US"}]{#struct_0_11651_x1037_x960663493}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1015458452}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_2016116574}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_1530716530}

[[Sent *packet-type* to *ipv6-address* from interface *interface-type interface-number*]{lang="EN-US"}]{#struct_0_11651_x1037_385756032}

[[从接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_11651_x1037_x454157066}[发送到]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[的]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Received *packet-type* from *ipv6-address* on interface *interface-type interface-number*]{lang="EN-US"}]{#struct_0_11651_x1037_x1471888957}

[[从接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_11651_x1037_x960597957}[接收到来自]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[的]{style="font-family:宋体"}*[packet-type ]{lang="EN-US"}*[的消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ipv6 nd entry]{lang="EN-US"}]{#struct_0_11651_x1037_1644515687}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1016315340}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_x219486871}

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_1181006808}

[[Added neighbor-state NB entry: ipv6-address on interface-type interface-number]{lang="EN-US"}]{#struct_0_11651_x1037_x2079039320}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[[添加邻居地址为]{lang="EN-US" style="font-family:宋体"}[ipv6-address]{lang="EN-US"}]{.TableTextChar}]{#struct_0_11651_x1037_1016738391}[[的邻居表项，邻居状态为]{lang="EN-US" style="font-family:宋体"}[neighbor-state]{lang="EN-US"}]{.TableTextChar}[[，与该邻居相邻的接口为]{lang="EN-US" style="font-family:宋体"}[interface-type interface-number]{lang="EN-US"}]{.TableTextChar}

[[邻居状态：]{style="font-family:宋体"}]{#struct_0_11651_x1037_337815957}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INCMP]{lang="EN-US"}]{#struct_0_11651_x1037_x547351814}[：正在解析地址，邻居的链路层地址尚未确定；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_11651_x1037_x960532421}[正在解析地：邻居可达；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[STALE]{lang="EN-US"}]{#struct_0_11651_x1037_x702346663}[：未确定邻居是否可达，设备不会再验证邻居的可达性，除非有数据发送给该邻居；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DELAY]{lang="EN-US"}]{#struct_0_11651_x1037_x143664560}[：未确定邻居是否可达，延迟一段时间发送邻居请求报文；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROBE]{lang="EN-US"}]{#struct_0_11651_x1037_122961702}[：未确定邻居是否可达，发送邻居请求报文来验证邻居的可达性；]{style="font-family:宋体"}

[[neighbor-state1-\>neighbor-state2: ipv6-address on interface-type interface-number]{lang="EN-US"}]{#struct_0_11651_x1037_x1514946815}

[[邻居表项的状态从]{style="font-family:宋体"}[neighbor-state1]{lang="EN-US"}]{#struct_0_11651_x1037_x960466885}[转换为]{style="font-family:宋体"}[neighbor-state2]{lang="EN-US"}

[[Deleted neighbor-state NB entry: ipv6-address on interface-type interface-number]{lang="EN-US"}]{#struct_0_11651_x1037_848289006}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[[删除邻居地址为]{lang="EN-US" style="font-family:宋体"}[ipv6-address]{lang="EN-US"}]{.TableTextChar}]{#struct_0_11651_x1037_1972802053}[[的邻居表项，邻居状态为]{lang="EN-US" style="font-family:宋体"}[neighbor-state]{lang="EN-US"}]{.TableTextChar}[[，与该邻居相邻的接口为]{lang="EN-US" style="font-family:宋体"}[interface-type interface-number]{lang="EN-US"}]{.TableTextChar}

[[邻居状态：]{style="font-family:宋体"}]{#struct_0_11651_x1037_1627725112}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INCMP]{lang="EN-US"}]{#struct_0_11651_x1037_x1599810132}[：正在解析地址，邻居的链路层地址尚未确定；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_11651_x1037_1487654139}[正在解析地：邻居可达；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[STALE]{lang="EN-US"}]{#struct_0_11651_x1037_x961449925}[：未确定邻居是否可达，设备不会再验证邻居的可达性，除非有数据发送给该邻居；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DELAY]{lang="EN-US"}]{#struct_0_11651_x1037_x1824853751}[：未确定邻居是否可达，延迟一段时间发送邻居请求报文；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROBE]{lang="EN-US"}]{#struct_0_11651_x1037_x139788382}[：未确定邻居是否可达，发送邻居请求报文来验证邻居的可达性；]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging ipv6 nd error]{lang="EN-US"}]{#struct_0_11651_x1037_834307990}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1023288133}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1194690862}

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_1825369865}

[[Packet discarded for hop limit is invalid: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x961384389}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[[报文类型为]{lang="EN-US" style="font-family:宋体"}[packet-type]{lang="EN-US"}]{.TableTextChar}]{#struct_0_11651_x1037_63370071}[[，源地址为]{lang="EN-US" style="font-family:宋体"}[ipv6-address]{lang="EN-US"}]{.TableTextChar}[[的报文被丢弃，因为报文的跳段数限制不合法]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[报文类型：]{style="font-family:宋体"}]{#struct_0_11651_x1037_x284973400}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[RS]{lang="EN-US"}]{#struct_0_11651_x1037_431018164}[：路由器请求消息报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[RA]{lang="EN-US"}]{#struct_0_11651_x1037_804616994}[：路由器宣告消息报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FINAL RA]{lang="EN-US"}]{#struct_0_11651_x1037_x723421451}[：路由器宣告消息的最终报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NS]{lang="EN-US"}]{#struct_0_11651_x1037_x1219660297}[：邻居请求消息报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_11651_x1037_x960925636}[：邻居宣告消息报文]{style="font-family:宋体"}

[[Packet discarded for source address is unspecified and destination address is not solicited multicast: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x1490065233}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_x810209942}[源地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为报文的源地址不合法，目的地址非组播地址]{style="font-family:宋体"}

[[Packet discarded for source address is unspecified and SLLA is included: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x309525964}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_1233074252}[源地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为报文未指定源地址而且报文包含了]{style="font-family:宋体"}[SLLA]{lang="EN-US"}

[[Packet discarded for target address is tentative: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x960860100}

[[报文类型为]{style="font-family:宋体"}[packet-type, ]{lang="EN-US"}]{#struct_0_11651_x1037_1227563464}[目标地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为目标地址未生效]{style="font-family:宋体"}

[[Packet discarded for source addres is error: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x555708152}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_x964388986}[源地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为源地址错误]{style="font-family:宋体"}

[[Packet discarded for source addres is error: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x100697069}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_x960794564}[目的地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为目的地址错误]{style="font-family:宋体"}

[[Packet discarded for option is error: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x1482558511}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_2083733186}[源地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为报文中携带的选项错误]{style="font-family:宋体"}

[[Packet discarded for target address is a multicast address: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x2013202897}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_x72269719}[目标地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为目标地址是组播]{style="font-family:宋体"}

[[Packet discarded for destination address is a multicast address but S flag is set: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x960729028}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_1270739244}[目的地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为目的地址是组播但是]{style="font-family:宋体"}[S]{lang="EN-US"}[标记设置为]{style="font-family:宋体"}[1]{lang="EN-US"}

[[Packet discarded for target address is error: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_598350647}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_981880844}[目标地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为目标地址错误]{style="font-family:宋体"}

[[Packet discarded for no TLLA is included: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x960663492}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_2016051038}[目标地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为目标中没有携带]{style="font-family:宋体"}[TLLA]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[Packet discarded for including invalid TLLA:packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x1178237940}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_x1103484125}[目标地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为携带无效的]{style="font-family:宋体"}[TLLA]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[Packet discarded for including invalid SLLA: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x960597956}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_1644581223}[源地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为报文内的]{style="font-family:宋体"}[SLLA]{lang="EN-US"}[不合法]{style="font-family:宋体"}

[[Packet discarded for getting extend header failed: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_1320269775}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_x1193849450}[源地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为获取报文的扩展头失败]{style="font-family:宋体"}

[[Packet discarded for target address is not this router: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x960532420}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_x702281127}[目标地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文被丢弃，因为目标地址不是本路由器的]{style="font-family:宋体"}

[[Packet could not send for target address is error: packet-type on ipv6-address]{lang="EN-US"}]{#struct_0_11651_x1037_x125868712}

[[报文类型为]{style="font-family:宋体"}[packet-type,]{lang="EN-US"}]{#struct_0_11651_x1037_x557603149}[目标地址为]{style="font-family:宋体"}[ipv6-address]{lang="EN-US"}[的报文无法发送，因为目标地址错误]{style="font-family:宋体"}

[[Packet discarded for interface index is invalid]{lang="EN-US"}]{#struct_0_11651_x1037_x960466884}

[[报文丢弃：接口索引无效]{style="font-family:宋体"}]{#struct_0_11651_x1037_848223470}

[[Packet discarded for VLAN ID is invalid]{lang="EN-US"}]{#struct_0_11651_x1037_1972724649}

[[报文丢弃：]{style="font-family:宋体"}[VLAN id]{lang="EN-US"}]{#struct_0_11651_x1037_x1881798890}[无效]{style="font-family:宋体"}

[[Packet discarded for VLAN is not allowed on the port]{lang="EN-US"}]{#struct_0_11651_x1037_x961449924}

[[报文丢弃：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11651_x1037_x1824919287}[不允许通过]{style="font-family:宋体"}

[[Packet discarded for port is down]{lang="EN-US"}]{#struct_0_11651_x1037_x305875087}

[[报文丢弃：端口]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_11651_x1037_1179400437}

[[Packet discarded for STP state of the port is not forwarding]{lang="EN-US"}]{#struct_0_11651_x1037_x961384388}

[[报文丢弃：端口]{style="font-family:宋体"}[STP]{lang="EN-US"}]{#struct_0_11651_x1037_63304535}[状态不是]{style="font-family:宋体"}[forwarding]{lang="EN-US"}

[[Packet discarded for port is a link aggregatioin member]{lang="EN-US"}]{#struct_0_11651_x1037_71137552}

[[报文丢弃：端口是聚合成员口]{style="font-family:宋体"}]{#struct_0_11651_x1037_605158308}

[[Packet discarded for interface is a link aggregation member]{lang="EN-US"}]{#struct_0_11651_x1037_1360701678}

[[报文丢弃：接口是聚合成员口]{style="font-family:宋体"}]{#struct_0_11651_x1037_x163592179}

[[Updating entry failed for port is not a local interface]{lang="EN-US"}]{#struct_0_11651_x1037_x1749480866}

[[报文丢弃：非本板接口]{style="font-family:宋体"}]{#struct_0_11651_x1037_605223844}

[[Updating entry failed for conflicting with static configuration ]{lang="EN-US"}]{#struct_0_11651_x1037_47885350}

[[与静态配置冲突，更新表项失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_x547246564}

[[Sending syn message failed]{lang="EN-US"}]{#struct_0_11651_x1037_605289380}

[[发送同步消息失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_x682710333}

[[Syn entry failed for interface is down]{lang="EN-US"}]{#struct_0_11651_x1037_272254217}

[[同步表项失败：接口]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_11651_x1037_605354916}

[[Syn entry failed for port is down]{lang="EN-US"}]{#struct_0_11651_x1037_817510142}

[[同步表项失败：端口]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_11651_x1037_x946021866}

[[Syn entry failed for VLAN is not allowed on the port]{lang="EN-US"}]{#struct_0_11651_x1037_605420452}

[[同步表项失败：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11651_x1037_1503999196}[不允许通过]{style="font-family:宋体"}

[[Syn entry failed for maximum number of entires is reached.]{lang="EN-US"}]{#struct_0_11651_x1037_735853628}

[[同步表项失败：表项个数达到上限]{style="font-family:宋体"}]{#struct_0_11651_x1037_605485988}

[[Syn entry failed for interface is a link aggregaton member]{lang="EN-US"}]{#struct_0_11651_x1037_1112750281}

[[同步表项失败：接口是聚合成员口]{style="font-family:宋体"}]{#struct_0_11651_x1037_1183777980}

[[Syn entry failed for port is a link aggregation member]{lang="EN-US"}]{#struct_0_11651_x1037_605551524}

[[同步表项失败：端口是聚合成员口]{style="font-family:宋体"}]{#struct_0_11651_x1037_1135263676}

[[Syn entry failed for conflicting with static configuration]{lang="EN-US"}]{#struct_0_11651_x1037_1162971641}

[[同步表项失败：与静态配置冲突]{style="font-family:宋体"}]{#struct_0_11651_x1037_605617060}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11651_x1037_2130249515}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_x541116266}[在一台支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能并在接口下配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的设备上打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的邻居状态和邻居消息的调试信息开关，并执行]{style="font-family:宋体"}[ping]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 nd packet]{lang="EN-US"}]{#struct_0_11651_x1037_361059622}

[\<Sysname\> debugging ipv6 nd entry]{lang="EN-US"}

[\<Sysname\> ping ipv6 --c 1 1::2]{lang="EN-US"}

[   PING 1::2 : 56  data bytes, press CTRL_C to break]{lang="EN-US"}

[\*Aug  4 01:13:02:703 2006 Sysname ND/7/ND_ENTRY:]{lang="EN-US"}

[ Added INCOMPLETE NB entry: 1::2 on interface GigabitEthernet1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_1092478523}*[添加状态为]{style="font-family:宋体"}[INCOMPLETE]{lang="EN-US"}[的邻居表项。]{style="font-family:宋体"}*

[[\*Aug  4 01:13:02:704 2006 Sysname ND/7/ND_PACKET:]{lang="EN-US"}]{#struct_0_11651_x1037_488223571}

[ Sent NS to FF02::1:FF00:2, from interface GigabitEthernet1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_1193847225}*[向地址]{style="font-family:宋体"}[FF02::1:FF00:2]{lang="EN-US"}[发送邻居请求消息。]{style="font-family:宋体"}*

[[\*Aug  4 01:13:02:707 2006 Sysname ND/7/ND_PACKET:]{lang="EN-US"}]{#struct_0_11651_x1037_604634020}

[ Received NA from 1::2, on interface GigabitEthernet1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_63776174}*[接收到来自]{style="font-family:宋体"}[1::2]{lang="EN-US"}[的邻居应答消息。]{style="font-family:宋体"}*

[[\*Aug  4 01:13:02:708 2006 Sysname ND/7/ND_ENTRY:]{lang="EN-US"}]{#struct_0_11651_x1037_1080519526}

[ INCOMPLETE-\>REACHABLE : 1::2 on interface GigabitEthernet1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_1658275472}*[表项的状态从]{style="font-family:宋体"}[INCOMPLETE]{lang="EN-US"}[转换为]{style="font-family:宋体"}[REACHABLE]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[    Reply from 1::2]{lang="EN-US"}]{#struct_0_11651_x1037_x346038706}

[    Bytes=56 Sequence=1 Hop limit=64  Time = 8 ms]{lang="EN-US"}

[  \-\-- 1::2 ping6 statistics \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_x1123175102}[设备上接收到错误的报文。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 nd error]{lang="EN-US"}]{#struct_0_11651_x1037_604699556}

[\<Sysname\>\*Nov 16 23:32:45:642 2012 Sysname ND/7/ND_ERROR:]{lang="EN-US"}

[ Packet discarded for hop limit is invalid:  RS on 1::3]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_x1113405143}*[接收]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文的跳数错误，报文被丢弃。]{style="font-family:宋体"}*

::: {#1583579229 .myid}
[]{#_Toc404786746}[]{#struct_0_11651_x1037_1812835804}[]{#_Toc402875648}[]{#_Toc397517371}

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 nd snooping**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x408591890}

[**[debugging ipv6 nd snooping]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_11651_x1037_514418151}

[**[undo debugging ipv6 nd snooping]{lang="EN-US"}**]{#struct_0_11651_x1037_732473167}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11651_x1037_246751863}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1594776941}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1282851095}

[[network-admin]{lang="EN-US"}]{#struct_0_11651_x1037_1420516773}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x1086240254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11651_x1037_386371883}

[**[all]{lang="EN-US"}**]{#struct_0_11651_x1037_x1725454700}[：表示]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_11651_x1037_719786469}[：表示]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_11651_x1037_1566446226}[：表示]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_11651_x1037_x1499787541}[：表示]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1319332078}

[**[debugging ipv6 nd snooping]{lang="EN-US"}**]{#struct_0_11651_x1037_1158430764}[命令用来打开]{style="font-family:
宋体"}[ND Snooping]{lang="EN-US"}[的调试信息开关。]{style="font-family:
宋体"}**[undo debugging ipv6 nd snooping]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}]{#struct_0_11651_x1037_x1719589749}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging ipv6 nd snooping error]{lang="EN-US"}]{#struct_0_11651_x1037_x1268667061}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1041949264}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_136611597}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_621910711}

[[Failed to send packet in vlan *vlan-id*.]{lang="EN-US"}]{#struct_0_11651_x1037_x1106682919}

[[在]{style="font-family:宋体"}[vlan *vlan-id*]{lang="EN-US"}]{#struct_0_11651_x1037_1053320917}[内]{style="font-family:宋体"}[发]{lang="EN-US" style="font-family:宋体"}[送报文]{style="font-family:宋体"}[失败]{lang="EN-US" style="font-family:宋体"}

**[ ]{lang="EN-US"}**

[[表1-8 ]{lang="EN-US"}[debugging ipv6 nd snooping event]{lang="EN-US"}]{#struct_0_11651_x1037_1668621621}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1044744358}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_1166919714}

[[描述]{style="font-family:宋体"}]{#struct_0_11651_x1037_758391401}

[[The number of ND snooping entries on the device has reached the maximum.]{lang="EN-US"}]{#struct_0_11651_x1037_590623039}

[[ND Snooping]{lang="EN-US"}]{#struct_0_11651_x1037_x512763024}[表项总数已达到最大规格]{lang="EN-US" style="font-family:宋体"}

[[The number of ND snooping entries on the interface *interface-type interface-number* has reached the maximum.]{lang="EN-US"}]{#struct_0_11651_x1037_947025132}

[[端口]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_11651_x1037_x1138827724}[下的]{lang="EN-US" style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项总数]{lang="EN-US" style="font-family:宋体"}[[已达到最大规格]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[ND snooping successfully notified the user mode.]{lang="EN-US"}]{#struct_0_11651_x1037_x2145270451}

[[ND Snooping]{lang="EN-US"}]{#struct_0_11651_x1037_x2078846965}[通知用户]{lang="EN-US" style="font-family:宋体"}[状态成功]{style="font-family:宋体"}

[[ND snooping failed to notify the user mode.]{lang="EN-US"}]{#struct_0_11651_x1037_x55870804}

[[ND Snooping]{lang="EN-US"}]{#struct_0_11651_x1037_1453102983}[通知用户]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}[失败]{lang="EN-US" style="font-family:宋体"}

[[ND snooping synchronization channel between the kernel mode and the user mode disconnected.]{lang="EN-US"}]{#struct_0_11651_x1037_224148404}

[[ND Snooping]{lang="EN-US"}]{#struct_0_11651_x1037_650036390}[内核与用户状态的同步通道断开]{style="font-family:宋体"}

[[ND snooping packet synchronization channel between the LPU kernel mode and the MPU kernel mode disconnected.]{lang="EN-US"}]{#struct_0_11651_x1037_1344508198}

[[ND Snooping]{lang="EN-US"}]{#struct_0_11651_x1037_1767303188}[接口板内核与主控板内核的报文同步通道断开]{lang="EN-US" style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_11651_x1037_1110487479}

[[IP]{lang="EN-US"}]{#struct_0_11651_x1037_x1272277911}[v6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[First VLAN ID]{lang="EN-US"}]{#struct_0_11651_x1037_x627258525}

[[外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_11651_x1037_1886168459}[编号]{style="font-family:宋体"}

[[Second VLAN ID]{lang="EN-US"}]{#struct_0_11651_x1037_x590425472}

[[内层]{style="font-family:宋体"}]{#struct_0_11651_x1037_1456605444}[VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Valid port]{lang="EN-US"}]{#struct_0_11651_x1037_716627396}

[[生效的入端口]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11651_x1037_x402483237}

[[Tentative port]{lang="EN-US"}]{#struct_0_11651_x1037_1361214664}

[[待验证的接入端口]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1049740991}[]{#_GoBack}

[[MAC address]{lang="EN-US"}]{#struct_0_11651_x1037_1103841874}

[[MAC]{lang="EN-US"}]{#struct_0_11651_x1037_1487181698}[地址]{lang="EN-US" style="font-family:宋体"}

[[Tentative MAC address]{lang="EN-US"}]{#struct_0_11651_x1037_1679142364}

[[待验证的]{style="font-family:宋体"}]{#struct_0_11651_x1037_884153891}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Status changed from *old-status* to *new-status*.]{lang="EN-US"}]{#struct_0_11651_x1037_953549297}

[[状态由]{lang="EN-US" style="font-family:宋体"}*[old-status]{lang="EN-US"}*]{#struct_0_11651_x1037_x1427301517}[迁至]{lang="EN-US" style="font-family:宋体"}*[new-status]{lang="EN-US"}*[。]{lang="EN-US" style="font-family:宋体"}

[[其中]{lang="EN-US" style="font-family:
  宋体"}*[old-status]{lang="EN-US"}*]{#struct_0_11651_x1037_113058423}[、]{lang="EN-US" style="font-family:宋体"}*[ new-status]{lang="EN-US"}*[可选的状态包括：]{style="font-family:宋体"}

[[NO_BIND]{lang="EN-US"}]{#struct_0_11651_x1037_1832993291}[、]{lang="EN-US" style="font-family:宋体"}[TENTATIVE]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[TESTING_TPLT]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[VALID]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}

[[TESTING_VP]{lang="EN-US"}]{#struct_0_11651_x1037_79399064}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging ipv6 nd snooping packet]{lang="EN-US"}]{#struct_0_11651_x1037_340532075}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1031021966}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1453025518}

[[描述]{style="font-family:宋体"}]{#struct_0_11651_x1037_1014856560}

[[Packet not processed by ND snooping.]{lang="EN-US"}]{#struct_0_11651_x1037_1254550873}

[[ND Snooping]{lang="EN-US"}]{#struct_0_11651_x1037_x953408407}[无需处理此报文]{style="font-family:宋体"}

[[Received *packet-type* packet.]{lang="EN-US"}]{#struct_0_11651_x1037_919627477}

[[接收到]{lang="EN-US" style="font-family:宋体"}*[packet-type]{lang="EN-US"}*]{#struct_0_11651_x1037_1117997284}[报文。]{lang="EN-US" style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[可以是：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DAD NS]{lang="EN-US"}]{#struct_0_11651_x1037_164264097}[：重复地址检测的]{lang="EN-US" style="font-family:宋体"}[Neighbor Solicitation]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NS]{lang="EN-US"}]{#struct_0_11651_x1037_x455720050}[：]{lang="EN-US" style="font-family:宋体"}[Neighbor Solicitation]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_11651_x1037_1223619241}[：]{lang="EN-US" style="font-family:宋体"}[Neighbor Advertisement]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DATA]{lang="EN-US"}]{#struct_0_11651_x1037_x646456464}[：数据报文]{lang="EN-US" style="font-family:宋体"}

[[Sent packet from *source*.]{lang="EN-US"}]{#struct_0_11651_x1037_843142577}

[[将报文从]{style="font-family:宋体"}]{#struct_0_11651_x1037_1781720884}*[source]{lang="EN-US"}*[发送出去。]{style="font-family:宋体"}[其中]{lang="EN-US" style="font-family:宋体"}*[source]{lang="EN-US"}*[可以是]{lang="EN-US" style="font-family:宋体"}[TP(]{lang="EN-US"}[信任]{lang="EN-US" style="font-family:宋体"}

[[端口]{style="font-family:宋体"}]{#struct_0_11651_x1037_621377304}[)]{lang="EN-US"}[、]{style="font-family:宋体"}[VP(]{lang="EN-US"}[非信任端口]{style="font-family:宋体"}[)]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[这三者间的组合]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_11651_x1037_2082426891}

[[生效的接入端口]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11651_x1037_1905611940}

[[First VLAN ID]{lang="EN-US"}]{#struct_0_11651_x1037_x77293505}

[[外层]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}]{#struct_0_11651_x1037_x871604049}[编号]{style="font-family:宋体"}

[[Second VLAN ID]{lang="EN-US"}]{#struct_0_11651_x1037_516342950}

[[内层]{style="font-family:宋体"}]{#struct_0_11651_x1037_249434895}[VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_11651_x1037_x273570132}

[[IP]{lang="EN-US"}]{#struct_0_11651_x1037_x1524301217}[v6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_11651_x1037_x1405971351}

[[MAC]{lang="EN-US"}]{#struct_0_11651_x1037_x2347181}[地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x995055439}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_979272467}[打开]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[报文调试信息开关，用户从接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[侧上线。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 nd snooping all]{lang="EN-US"}]{#struct_0_11651_x1037_583354584}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_x270942855}*[设备收到]{style="font-family:宋体"}[DAD NS]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Jan  7 20:07:33:140 2013 H3C ND/7/ND SNOOPING PACKET:]{lang="EN-US"}]{#struct_0_11651_x1037_x606737385}

[ Received DAD NS packet.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  7 20:07:33:140 2013 H3C ND/7/ND SNOOPING EVENT:]{lang="EN-US"}

[ Information about ND snooping entry:]{lang="EN-US"}

[   IPv6 address: fe80::2e0:7fff:fe68:5e78]{lang="EN-US"}

[   First VLAN ID: 1   Second VLAN ID: 0]{lang="EN-US"}

[   Valid port: GE1/0/2]{lang="EN-US"}

[   Tentative port: N/A]{lang="EN-US"}

[   MAC address: 00e0-7f68-5e78]{lang="EN-US"}

[   Tentative MAC address: 0000-0000-0000]{lang="EN-US"}

[   Status changed from NO_BIND to TENTATIVE.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_1322912004}*[设备从信任口发送]{style="font-family:宋体"}[2]{lang="EN-US"}[个]{style="font-family:宋体"}[DAD NS]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Jan  7 20:07:33:141 2013 H3C ND/7/ND SNOOPING PACKET:]{lang="EN-US"}]{#struct_0_11651_x1037_243669999}

[ Sent DAD NS packet from TP.]{lang="EN-US"}

[ Information about ND snooping entry:]{lang="EN-US"}

[   Interface:GE1/0/2           First VLAN ID: 1   Second VLAN ID: 0]{lang="EN-US"}

[   IPv6 address: fe80::2e0:7fff:fe68:5e78    MAC address: 00e0-7f68-5e78]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  7 20:07:33:392 2013 H3C ND/7/ND SNOOPING PACKET:]{lang="EN-US"}

[ Sent DAD NS packet from TP.]{lang="EN-US"}

[ Information about ND snooping entry:]{lang="EN-US"}

[   Interface:GE1/0/2           First VLAN ID: 1   Second VLAN ID: 0]{lang="EN-US"}

[   IPv6 address: fe80::2e0:7fff:fe68:5e78    MAC address: 00e0-7f68-5e78]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  7 20:07:33:640 2013 H3C ND/7/ND SNOOPING EVENT:]{lang="EN-US"}

[ Information about ND snooping entry:]{lang="EN-US"}

[   IPv6 address: fe80::2e0:7fff:fe68:5e78]{lang="EN-US"}

[   First VLAN ID: 1   Second VLAN ID: 0]{lang="EN-US"}

[   Valid port: GE1/0/2]{lang="EN-US"}

[   Tentative port: N/A]{lang="EN-US"}

[   MAC address: 00e0-7f68-5e78]{lang="EN-US"}

[   Tentative MAC address: 0000-0000-0000]{lang="EN-US"}

[   Status changed from TENTATIVE to VALID.]{lang="EN-US"}

[*[// ND Snooping]{lang="EN-US"}*]{#struct_0_11651_x1037_x587581166}*[通知用户状态成功。]{style="font-family:宋体"}*

[[\*Jan  7 20:07:33:640 2013 H3C ND/7/ND SNOOPING EVENT:]{lang="EN-US"}]{#struct_0_11651_x1037_x827868821}

[ ND snooping successfully notified the user mode.]{lang="EN-US"}

::: {#1092321958 .myid}
[]{#_Toc404786747}[]{#struct_0_11651_x1037_2029138483}[]{#_Toc154550829}[]{#_Toc154550833}[]{#_Toc154550834}[]{#_Toc154550835}[]{#_Toc154550836}[]{#_Toc154550837}[]{#_Toc154550838}[]{#_Toc154550839}[]{#_Toc154550840}[]{#_Toc154550841}[]{#_Toc154550843}[]{#_Toc154550844}[]{#_Toc154550845}[]{#_Toc154550846}[]{#_Toc154550847}[]{#_Toc154550849}[]{#_Toc154550850}[]{#_Toc154550851}[]{#_Toc154550852}

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_11651_x1037_942787550}

[**[debugging ipv6 packet]{lang="EN-US"}**[ \[ **acl6** *acl6-number* \]]{lang="EN-US"}]{#struct_0_11651_x1037_2072376479}

[**[undo debugging ipv6 packet]{lang="EN-US"}**]{#struct_0_11651_x1037_x1406344318}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x380223190}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11651_x1037_1261686692}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1957228749}

[[network-admin]{lang="EN-US"}]{#struct_0_11651_x1037_605158309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11651_x1037_1360701677}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x162609139}

[**[acl6 ]{lang="EN-US"}***[acl6-number]{lang="EN-US"}*]{#struct_0_11651_x1037_x918556346}[：输出通过指定访问控制列表过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文调试信息。]{style="font-family:宋体"}*[acl6-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的序号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1265089464}

[**[debugging ipv6 packet]{lang="EN-US"}**]{#struct_0_11651_x1037_x1390271595}[命令用来打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_729578691}[报文的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-10 ]{lang="EN-US"}[debugging ipv6 packet]{lang="EN-US"}]{#struct_0_11651_x1037_1763911577}[[命令输出信息描述表]{style="font-size:9.0pt;font-family:黑体"}]{.TableHeadingChar}

[]{#table_struct_0_x997457531}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_169985860}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_605223845}

[[Discarding]{lang="EN-US"}]{#struct_0_11651_x1037_47885351}

[[丢弃报文的操作]{style="font-family:宋体"}]{#struct_0_11651_x1037_1791405596}

[[Sending]{lang="EN-US"}]{#struct_0_11651_x1037_x47991294}

[[发送报文的操作]{style="font-family:宋体"}]{#struct_0_11651_x1037_x2130973674}

[[Receiving]{lang="EN-US"}]{#struct_0_11651_x1037_881984151}

[[接收报文的操作]{style="font-family:宋体"}]{#struct_0_11651_x1037_1896655644}

[[Delivering]{lang="EN-US"}]{#struct_0_11651_x1037_605289381}

[[IP]{lang="EN-US"}]{#struct_0_11651_x1037_x682710332}[层将报文送到上层]{style="font-family:宋体"}

[[Transferring]{lang="EN-US"}]{#struct_0_11651_x1037_272188681}

[[透传报文的操作或把报文提交给其它模块的操作]{style="font-family:宋体"}]{#struct_0_11651_x1037_935214271}

[[LocalSending]{lang="EN-US"}]{#struct_0_11651_x1037_908155333}

[[本机发送报文的操作]{style="font-family:宋体"}]{#struct_0_11651_x1037_605354917}

[[interface]{lang="EN-US"}]{#struct_0_11651_x1037_817510141}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11651_x1037_x946021869}[发送报文的接口]{style="font-family:宋体"}

[[version]{lang="EN-US"}]{#struct_0_11651_x1037_1183352067}

[[IP]{lang="EN-US"}]{#struct_0_11651_x1037_1672777309}[协议版本号]{style="font-family:宋体"}

[[traffic class]{lang="EN-US"}]{#struct_0_11651_x1037_x1052869716}

[[通信流类别]{style="font-family:宋体"}]{#struct_0_11651_x1037_605420453}

[[flow label]{lang="EN-US"}]{#struct_0_11651_x1037_1503999197}

[[流标签]{style="font-family:宋体"}]{#struct_0_11651_x1037_735788092}

[[payload length]{lang="EN-US"}]{#struct_0_11651_x1037_598936721}

[[有效载荷长度]{style="font-family:宋体"}]{#struct_0_11651_x1037_605485989}

[[protocol]{lang="EN-US"}]{#struct_0_11651_x1037_1112750282}

[[下一个报头]{style="font-family:宋体"}]{#struct_0_11651_x1037_1183974588}

[[hop limit]{lang="EN-US"}]{#struct_0_11651_x1037_x702723905}

[[跳数限制]{style="font-family:宋体"}]{#struct_0_11651_x1037_1455717609}

[[Src]{lang="EN-US"}]{#struct_0_11651_x1037_605551525}

[[报文源地址]{style="font-family:宋体"}]{#struct_0_11651_x1037_1135263675}

[[Dst]{lang="EN-US"}]{#struct_0_11651_x1037_1162906105}

[[报文目的地址]{style="font-family:宋体"}]{#struct_0_11651_x1037_197987911}

[[Ingress interface did not join the group address.]{lang="EN-US"}]{#struct_0_11651_x1037_1250499211}

[[入接口没有加入该组播组]{style="font-family:宋体"}]{#struct_0_11651_x1037_605617061}

[[Sending the packet from local interface *interface-type interface-number*]{lang="EN-US"}]{#struct_0_11651_x1037_2130249514}

[[从本地接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_11651_x1037_x541181802}[发送报文]{style="font-family:宋体"}

[[Sending the packet from *interface-type interface-number1* through *interface-type interface-number2*]{lang="EN-US"}]{#struct_0_11651_x1037_354452837}

[[从]{style="font-family:宋体"}*[interface-type interface-number1]{lang="EN-US"}*]{#struct_0_11651_x1037_604634021}[接受报文后从接口]{style="font-family:宋体"}*[interface-type interface-number2]{lang="EN-US"}*[发送]{style="font-family:
  宋体"}

[[Received an IPv6 packet.]{lang="EN-US"}]{#struct_0_11651_x1037_63776173}

[[接收到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x875795610}[报文]{style="font-family:宋体"}

[[Delivering the IPv6 packet to the upper layer.]{lang="EN-US"}]{#struct_0_11651_x1037_x1801035660}

[[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_604699557}[报文送到上层处理]{style="font-family:宋体"}

[[Invalid next header.]{lang="EN-US"}]{#struct_0_11651_x1037_x1113405144}

[[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x1862544286}[的下一个扩展头无效]{style="font-family:宋体"}

[[Invalid next header sequence.]{lang="EN-US"}]{#struct_0_11651_x1037_81266420}

[[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_605158306}[头扩展头顺序错误]{style="font-family:宋体"}

[[Unknown options in the extension header.]{lang="EN-US"}]{#struct_0_11651_x1037_1360701680}

[[扩展头信息里面的选项无法识别]{style="font-family:宋体"}]{#struct_0_11651_x1037_x163067906}

[[Invalid hop-by-hop header.]{lang="EN-US"}]{#struct_0_11651_x1037_605223842}

[[逐跳选项头错误]{style="font-family:宋体"}]{#struct_0_11651_x1037_47885344}

[[Incorrect format: the hop-by-hop option is after the hop-by-hop extension header.]{lang="EN-US"}]{#struct_0_11651_x1037_254163329}

[[逐跳选项在逐跳选项扩展头的后面，格式错误]{style="font-family:宋体"}]{#struct_0_11651_x1037_1126089458}

[[Length of the fragment packet is invalid.]{lang="EN-US"}]{#struct_0_11651_x1037_605289378}

[[分片报文的报文长度错误]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1492014405}

[[Failed to reassemble fragments.]{lang="EN-US"}]{#struct_0_11651_x1037_1273901339}

[[分片重组失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_605354914}

[[No ]{lang="EN-US"}]{#struct_0_11651_x1037_817510144}[IPv6 address configured for the interface.]{lang="EN-US"}

[[接口上没有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x946021864}[地址]{style="font-family:宋体"}

[[Unknown FIB error]{lang="EN-US"}]{#struct_0_11651_x1037_605420450}

[[未知的]{style="font-family:宋体"}[FIB]{lang="EN-US"}]{#struct_0_11651_x1037_1503999198}[错误]{style="font-family:宋体"}

[[Destination is unreachable!]{lang="EN-US"}]{#struct_0_11651_x1037_735460412}

[[目的不可达]{style="font-family:宋体"}]{#struct_0_11651_x1037_386807803}

[[Exceeded hop limits.]{lang="EN-US"}]{#struct_0_11651_x1037_605485986}

[[报文超过跳数限制]{style="font-family:宋体"}]{#struct_0_11651_x1037_1112750287}

[[No source IP address specified for forwarding the IPv6 packet.]{lang="EN-US"}]{#struct_0_11651_x1037_605551522}

[[转发报文时发现源地址没有指定]{style="font-family:宋体"}]{#struct_0_11651_x1037_1135263678}

[[Invalid source IPv4-compatible address]{lang="EN-US"}]{#struct_0_11651_x1037_1162054137}

[[无效的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_11651_x1037_x980343239}[兼容源地址]{style="font-family:宋体"}

[[Invalid destination IPv4-compatible address.]{lang="EN-US"}]{#struct_0_11651_x1037_605617058}

[[无效的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_11651_x1037_x208402637}[兼容目的地址]{style="font-family:宋体"}

[[Unknown destination]{lang="EN-US"}]{#struct_0_11651_x1037_604634018}

[[未知的目的]{style="font-family:宋体"}]{#struct_0_11651_x1037_2020091318}

[[Source address is link local address but destination address is not.]{lang="EN-US"}]{#struct_0_11651_x1037_x456352773}

[[转发报文时发现报文的源地址是链路本地地址而目的地址不是链路本地地址，丢弃报文]{style="font-family:宋体"}]{#struct_0_11651_x1037_604699554}

[[Invalid version.]{lang="EN-US"}]{#struct_0_11651_x1037_x1113405141}

[[报文版本号错误]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1103029399}

[[Source IPv6 address was a multicast address.]{lang="EN-US"}]{#struct_0_11651_x1037_605158307}

[[源地址为多播地址]{style="font-family:宋体"}]{#struct_0_11651_x1037_1360701679}

[[No destination IPv6 address specified]{lang="EN-US"}]{#struct_0_11651_x1037_x163526643}

[[目的地址未指定]{style="font-family:宋体"}]{#struct_0_11651_x1037_605223843}

[[The packet was bigger than the MTU.]{lang="EN-US"}]{#struct_0_11651_x1037_47885345}

[[报文长度大于]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_11651_x1037_605289379}

[[Sending the ND packet to a module for managing IPv6 neighbors.]{lang="EN-US"}]{#struct_0_11651_x1037_x1492014404}

[[将]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_11651_x1037_x1454982016}[报文送到]{style="font-family:宋体"}[ND]{lang="EN-US"}[模块处理]{style="font-family:宋体"}

[[Sending the IPv6 packet to the control CPU.]{lang="EN-US"}]{#struct_0_11651_x1037_605354915}

[[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_817510143}[报文送到控制核处理]{style="font-family:宋体"}

[[Receiving an IPv6 fragment transported from another slot.]{lang="EN-US"}]{#struct_0_11651_x1037_605420451}

[[收到从其它板透传过来的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_1503999199}[分片报文]{style="font-family:宋体"}

[[Receiving an IPv6 packet transported from another slot.]{lang="EN-US"}]{#struct_0_11651_x1037_735394876}

[[收到从其它板透传过来的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_605485987}[报文]{style="font-family:宋体"}

[[Jumbo payload option is not supported.]{lang="EN-US"}]{#struct_0_11651_x1037_1112750288}

[[不支持]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}]{#struct_0_11651_x1037_605551523}[选项]{style="font-family:宋体"}

[[Failed to obtain the hop-by-hop extension header.]{lang="EN-US"}]{#struct_0_11651_x1037_1135263677}

[[获取逐跳扩展头失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_1163037177}

[[Failed to obtain the destination extension header.]{lang="EN-US"}]{#struct_0_11651_x1037_605617059}

[[获取目的扩展头失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_x208402638}

[[Failed to obtain the route extension header.]{lang="EN-US"}]{#struct_0_11651_x1037_604634019}

[[获取路由扩展头失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_2020091317}

[[Fragments contain overlapped data.]{lang="EN-US"}]{#struct_0_11651_x1037_604699555}

[[分片报文中数据与其它分片重叠]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1113405142}

[[Failed to obtain fragment extension header.]{lang="EN-US"}]{#struct_0_11651_x1037_x699744872}

[[获取分片扩展头失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_605158304}

[[Sending the IPv6 packet to slot *slot-id*.]{lang="EN-US"}]{#struct_0_11651_x1037_1360701682}

[[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_605223840}[报文送到]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*[板处理]{style="font-family:宋体"}

[[Starting multicast forwarding.]{lang="EN-US"}]{#struct_0_11651_x1037_47885346}

[[开始进行组播转发处理]{style="font-family:宋体"}]{#struct_0_11651_x1037_605289376}

[[The packet size is smaller than 40 bytes.]{lang="EN-US"}]{#struct_0_11651_x1037_x1492014399}

[[报文长度小于]{style="font-family:宋体"}[40]{lang="EN-US"}]{#struct_0_11651_x1037_605354912}[字节]{style="font-family:宋体"}

[[The destination IPv6 address is a loopback address.]{lang="EN-US"}]{#struct_0_11651_x1037_817510146}

[[目的地址是环回地址]{style="font-family:宋体"}]{#struct_0_11651_x1037_605420448}

[[The source IPv6 address is a loopback address.]{lang="EN-US"}]{#struct_0_11651_x1037_x834652954}

[[源地址是环回地址]{style="font-family:宋体"}]{#struct_0_11651_x1037_x817705970}

[[The packet payload length cannot be zero.]{lang="EN-US"}]{#struct_0_11651_x1037_605485984}

[[报文的有效载荷长度不能为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_11651_x1037_1112750285}

[[The packet size is smaller than declared in the packet header.]{lang="EN-US"}]{#struct_0_11651_x1037_605551520}

[[报文实际长度小于报文头中标识的长度]{style="font-family:宋体"}]{#struct_0_11651_x1037_1135263680}

[[Sending the IPv6 packet to the MPLS module.]{lang="EN-US"}]{#struct_0_11651_x1037_605617056}

[[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x208402643}[报文送到]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[模块处理]{style="font-family:宋体"}

[[Multicast forwarding the IPv6 packet.]{lang="EN-US"}]{#struct_0_11651_x1037_604634016}

[[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_2020091316}[报文送到组播转发处理]{style="font-family:宋体"}

[[No source address specified.]{lang="EN-US"}]{#struct_0_11651_x1037_604699552}

[[本机发送时没有选到源地址]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1113405147}

[[No outbound interface specified for sending the link local packet.]{lang="EN-US"}]{#struct_0_11651_x1037_605158305}

[[本机发送的链路本地报文没有指定出接口]{style="font-family:宋体"}]{#struct_0_11651_x1037_1360701681}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11651_x1037_605223841}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_47885347}[在一台支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能并在接口下配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的设备上打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的报文调试信息开关，并执行]{style="font-family:宋体"}[ping]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 packet]{lang="EN-US"}]{#struct_0_11651_x1037_x2084488831}

[\<Sysname\> ping ipv6 -c 1 1::2]{lang="EN-US"}

[  PING 1::2 : 56  data bytes, press CTRL_C to break]{lang="EN-US"}

[\*Aug  4 01:42:06:375 2010 Sysname IP6FW/7/debug_case:]{lang="EN-US"}

[Sending, interface = GigabitEthernet1/0/1, version = 6, traffic class = 0,]{lang="EN-US"}

[flow label = 0, payload length = 64, protocol = 58, hop limit = 255,]{lang="EN-US"}

[Src = 1::1, Dst = 1::2,]{lang="EN-US"}

[prompt: Sending the packet from local interface GigabitEthernet1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_x1954584104}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送报文]{style="font-family:宋体"}*

[[\*Aug  4 01:42:06:377 2010 Sysname IP6FW/7/debug_case:]{lang="EN-US"}]{#struct_0_11651_x1037_x352090068}

[Receiving, interface = GigabitEthernet1/0/1, version = 6, traffic class = 0,]{lang="EN-US"}

[flow label = 0, payload length = 64, protocol = 58, hop limit = 64,]{lang="EN-US"}

[Src = 1::2, Dst = 1::1,]{lang="EN-US"}

[prompt: Received an IPv6 packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_87028131}*[接收到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Aug  4 01:42:06:378 2010 Sysname IP6FW/7/debug_case:]{lang="EN-US"}]{#struct_0_11651_x1037_605289377}

[Delivering, interface = GigabitEthernet1/0/1, version = 6, traffic class = 0,]{lang="EN-US"}

[flow label = 0, payload length = 64, protocol = 58, hop limit = 64,]{lang="EN-US"}

[Src = 1::2, Dst = 1::1,]{lang="EN-US"}

[prompt: Delivering the IPv6 packet to the upper layer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_x1492014398}*[将接收报文送到上层]{style="font-family:宋体"}*

[[    Reply from 1::2]{lang="EN-US"}]{#struct_0_11651_x1037_157697341}

[    bytes=56 Sequence=1 hop limit=64  time = 5 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-- 1::2 ping statistics \-\--]{lang="EN-US"}

[    1 packet(s) transmitted]{lang="EN-US"}

[    1 packet(s) received]{lang="EN-US"}

[    0.00% packet loss]{lang="EN-US"}

[    round-trip min/avg/max = 5/5/5 ms]{lang="EN-US"}

::: {#-2032541577 .myid}
[]{#_Toc404786748}[]{#struct_0_11651_x1037_x574117767}

**IPv6基础 \-- IPv6基础调试命令 \-- debugging ipv6 pathmtu**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x869185280}

[**[debugging ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_11651_x1037_x1847367744}

[**[undo debugging ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_11651_x1037_605354913}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11651_x1037_817510145}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11651_x1037_x946021865}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1182565635}

[[network-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x1855013419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x601269885}

[[【描述】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1379273258}

[**[debugging ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_11651_x1037_558148071}[命令用来打开]{style="font-family:宋体"}[IPv6 PMTU]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 pathmtu]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv6 PMTU]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6 PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x443914510}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[[表1-11 ]{lang="EN-US"}]{.TableHeadingChar}[debugging ipv6 pathmtu]{lang="EN-US"}]{#struct_0_11651_x1037_605420449}[[命令输出信息描述表]{style="font-size:
9.0pt;font-family:黑体"}]{.TableHeadingChar}

[]{#table_struct_0_x981337306}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_x834652953}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_x817771506}

[[VPNIndex]{lang="EN-US"}]{#struct_0_11651_x1037_1299144229}

[[VPN]{lang="EN-US"}]{#struct_0_11651_x1037_x534762760}[实例索引]{style="font-family:宋体"}

[[IPv6Addr]{lang="EN-US"}]{#struct_0_11651_x1037_118279149}

[[IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x286594139}[地址]{style="font-family:宋体"}

[[EntryType]{lang="EN-US"}]{#struct_0_11651_x1037_605485985}

[[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_1112750286}[表项类型，可能的取值及其含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC]{lang="EN-US"}]{#struct_0_11651_x1037_1183712444}[：表示静态表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TOOBIG]{lang="EN-US"}]{#struct_0_11651_x1037_x1848406561}[：表示]{style="font-family:宋体"}[toobig]{lang="EN-US"}[报文触发添加的动态表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SOCKET]{lang="EN-US"}]{#struct_0_11651_x1037_x228349665}[：表示本机发包触发添加的动态表项]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_11651_x1037_x1934943632}

[[MTU]{lang="EN-US"}]{#struct_0_11651_x1037_605551521}[值]{style="font-family:宋体"}

[[Agetime]{lang="EN-US"}]{#struct_0_11651_x1037_1135263679}

[[老化时间]{style="font-family:宋体"}]{#struct_0_11651_x1037_1162119673}

[[Adding PMTU entry]{lang="EN-US"}]{#struct_0_11651_x1037_649601907}

[[添加]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_744497588}[表项]{style="font-family:宋体"}

[[The type of the added PMTU entry is wrong]{lang="EN-US"}]{#struct_0_11651_x1037_605617057}

[[添加的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x208402644}[表项类型错误]{style="font-family:宋体"}

[[Delete PMTU entry]{lang="EN-US"}]{#struct_0_11651_x1037_x1596323792}

[[删除]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x1340170723}[表项]{style="font-family:宋体"}

[[The type of the deleted PMTU entry is wrong]{lang="EN-US"}]{#struct_0_11651_x1037_1167931495}

[[删除的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_604634017}[表项类型错误]{style="font-family:宋体"}

[[Age out PMTU entry]{lang="EN-US"}]{#struct_0_11651_x1037_2020091315}

[[老化]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x457073669}[表项]{style="font-family:宋体"}

[[Update agetime]{lang="EN-US"}]{#struct_0_11651_x1037_753832914}

[[更新老化时间]{style="font-family:宋体"}]{#struct_0_11651_x1037_1349528436}

[[Delete all static PMTU entries]{lang="EN-US"}]{#struct_0_11651_x1037_604699553}

[[删除所有静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x1113405148}[表项]{style="font-family:宋体"}

[[Delete all dynamic PMTU entries]{lang="EN-US"}]{#struct_0_11651_x1037_819284902}

[[删除所有动态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_273832393}[表项]{style="font-family:宋体"}

[[Delete all PMTU entries]{lang="EN-US"}]{#struct_0_11651_x1037_x2123725047}

[[删除所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x2037046724}[表项]{style="font-family:宋体"}

[[PMTU entry smoothing started]{lang="EN-US"}]{#struct_0_11651_x1037_1528598797}

[[平滑]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_1604507675}[表项开始]{style="font-family:宋体"}

[[PMTU entry smoothing finished]{lang="EN-US"}]{#struct_0_11651_x1037_x459374316}

[[平滑]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x2123659511}[表项结束]{style="font-family:宋体"}

[[Age timer timed out]{lang="EN-US"}]{#struct_0_11651_x1037_644247784}

[[老化定时器超时]{style="font-family:宋体"}]{#struct_0_11651_x1037_881647306}

[[Update epoch value for dynamic PMTU entries]{lang="EN-US"}]{#struct_0_11651_x1037_x1842036621}

[[更新动态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x2123593975}[表项]{style="font-family:宋体"}[epoch]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Error message received]{lang="EN-US"}]{#struct_0_11651_x1037_703446636}

[[收到错误消息]{style="font-family:宋体"}]{#struct_0_11651_x1037_1789137269}

[[Kernel adding PMTU entry]{lang="EN-US"}]{#struct_0_11651_x1037_x769927895}

[[内核发起添加]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x2123528439}[表项]{style="font-family:宋体"}

[[Kernel delete PMTU entry]{lang="EN-US"}]{#struct_0_11651_x1037_146780238}

[[内核发起删除]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x1651885054}[表项]{style="font-family:宋体"}

[[Adding PMTU entry failed; the maximum number of static PMTU entries has been reached]{lang="EN-US"}]{#struct_0_11651_x1037_x2123462903}

[[添加]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_x948104035}[表项失败，]{style="font-family:宋体"}[static]{lang="EN-US"}[类型表项达到上限]{style="font-family:宋体"}

[[Adding PMTU entry failed; the maximum number of toobig PMTU entries has been reached]{lang="EN-US"}]{#struct_0_11651_x1037_x1748287906}

[[添加]{style="font-family:宋体"}[PMTU]{lang="EN-US"}]{#struct_0_11651_x1037_1877453517}[表项失败，]{style="font-family:宋体"}[toobig]{lang="EN-US"}[类型表项达到上限]{style="font-family:宋体"}

[[Add *number* PMTU entries]{lang="EN-US"}]{#struct_0_11651_x1037_x2123397367}

[[添加]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_11651_x1037_x1879988324}[个]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Get *number* PMTU entries]{lang="EN-US"}]{#struct_0_11651_x1037_x730431498}

[[获取]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_11651_x1037_x2123331831}[个]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Binding socket to PMTU succeeded]{lang="EN-US"}]{#struct_0_11651_x1037_426983689}

[[socket]{lang="EN-US"}]{#struct_0_11651_x1037_1376385276}[绑定]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项成功]{style="font-family:宋体"}

[[Unbinding PMTU from socket succeeded]{lang="EN-US"}]{#struct_0_11651_x1037_x2123266295}

[[socket]{lang="EN-US"}]{#struct_0_11651_x1037_762641868}[解除绑定]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1049607749}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_1889205385}[打开]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pathmtu]{lang="EN-US"}]{#struct_0_11651_x1037_x801915213}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_1882405071}[增加]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项，可以看到如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11651_x1037_x2124249335}

[\[Sysname\] ipv6 pathmtu 1::2 1500]{lang="EN-US"}

[\*Sep  9 10:01:02:688 2011 Sysname IP6PMTU/7/IP6PMTU_DBG: -MDC=1; Adding PMTU entry.]{lang="EN-US"}

[ VPNIndex: 0, IPv6Addr: 1::2, EntryType: STATIC, MTU: 1500]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_1150160418}*[添加]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项：]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::2]{lang="EN-US"}[，静态表项，]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}*

::: {#-127493951 .myid}
[]{#_Toc404786749}[]{#struct_0_11651_x1037_x1472991376}[]{#_Toc401681889}[]{#_Toc382903804}[]{#_Toc320977758}[]{#_Toc320977705}[]{#_Toc320977672}[]{#_Toc320977658}[]{#_Toc320956813}

**IPv6基础 \-- IPv6基础调试命令 \-- debugging tcp-proxy**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1255891979}

[**[debugging]{lang="EN-US"}**[ **tcp-proxy** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_11651_x1037_x949964941}

[**[undo]{lang="EN-US"}**[ **debugging** **tcp-proxy** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_11651_x1037_x1778172093}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x657486053}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11651_x1037_2136028907}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x2055426702}

[[network-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x310191962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11651_x1037_x1535287943}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1117500959}

[**[all]{lang="EN-US"}**]{#struct_0_11651_x1037_x1422671667}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_11651_x1037_x898808427}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_11651_x1037_x206208557}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_11651_x1037_2062461033}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_11651_x1037_1591327853}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_11651_x1037_510578029}

[**[debugging]{lang="EN-US"}**[ **tcp-proxy**]{lang="EN-US"}]{#struct_0_11651_x1037_926225286}[命令用来打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **tcp-proxy**]{lang="EN-US"}[命令用来关闭]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[代理的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_11651_x1037_x1643554098}[代理的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[本命令用来打开]{style="font-family:宋体"}[IPv4 TCP]{lang="EN-US"}]{#struct_0_11651_x1037_x1542509965}[和]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的调试信息开关。]{style="font-family:宋体"}

[[表1-12 ]{lang="EN-US"}[debugging tcp-proxy error]{lang="FR"}]{#struct_0_11651_x1037_496377092}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2022929547}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_368656172}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1876210367}

[[\[]{lang="EN-US"}]{#struct_0_11651_x1037_946357011}*[addressport]{lang="FR"}*[\]]{lang="EN-US"}

[[地址端口信息：]{style="font-family:宋体"}]{#struct_0_11651_x1037_852672988}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[sip]{lang="FR"}*]{#struct_0_11651_x1037_1037264592}[/*sport* \--\> *dip*/*dport*]{lang="FR"}[：]{style="font-family:宋体"}[发起方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="FR"}[端口号]{lang="EN-US" style="font-family:宋体"}*[sip]{lang="FR"}*[/*sport*]{lang="FR"}[，响应方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="FR"}[端口号]{lang="EN-US" style="font-family:宋体"}*[dip]{lang="FR"}*[/*dport*]{lang="FR"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[sip]{lang="FR"}*]{#struct_0_11651_x1037_x713410953}[/*sport -*-\> None]{lang="FR"}[：发起方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{lang="EN-US" style="font-family:宋体"}*[sip]{lang="FR"}*[/*sport*]{lang="FR"}[，无响应方]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[initial]{lang="FR"}]{#struct_0_11651_x1037_1592709793}[：]{style="font-family:宋体"}[未指定地址]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}[端口号]{lang="EN-US" style="font-family:宋体"}

 

[[Failed to connect to IPv4/IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_1956396767}*[ sip]{lang="FR"}*[/*sport*]{lang="FR"}[ on handle \[]{lang="EN-US"}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序用句柄（地址端口信息为]{style="font-family:宋体"}]{#struct_0_11651_x1037_2015472402}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[向]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[的]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IP*sip*/]{lang="FR"}[源端口]{style="font-family:宋体"}*[sport]{lang="FR"}*[发起连接]{style="font-family:宋体"}[失败]{style="font-family:宋体"}

 

[[Failed to create new packet for data of *datalen* bytes due to insufficient memory.]{lang="FR"}]{#struct_0_11651_x1037_1664815090}

[[由于内存不足，导致创建]{style="font-family:宋体"}*[datalen]{lang="EN-US"}*]{#struct_0_11651_x1037_93158101}[字节的报文失败]{style="font-family:宋体"}

 

[[Failed to erase *overlaplen* bytes of overlapping data from packet *packet*]{lang="FR"}]{#struct_0_11651_x1037_x673778088}

[[从报文]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1472925840}*[packet]{lang="FR"}*[中擦除]{style="font-family:宋体"}*[overlaplen]{lang="FR"}*[字节的重叠数据失败]{style="font-family:宋体"}

 

[[Failed to create TCP proxy data block due to insufficient memory.]{lang="FR"}]{#struct_0_11651_x1037_x1629413382}

[[由于内存不足，导致创建]{style="font-family:宋体"}]{#struct_0_11651_x1037_1147134730}[TCP]{lang="FR"}[代理数据信息失败]{style="font-family:宋体"}

 

[[Failed to send SYN ACK packet.]{lang="FR"}]{#struct_0_11651_x1037_1255957515}

[[发送]{style="font-family:宋体"}]{#struct_0_11651_x1037_x2136476754}[SYN ACK]{lang="FR"}[报文失败]{style="font-family:宋体"}

 

[[Invalid ACK packet. Dropped it.]{lang="FR"}]{#struct_0_11651_x1037_x310126426}

[[丢弃无效的]{style="font-family:宋体"}]{#struct_0_11651_x1037_799390542}[ACK]{lang="FR"}[报文]{style="font-family:宋体"}

 

[[Can\'t find listening TCP proxy data block for server/client ]{lang="FR"}[\[]{lang="EN-US"}]{#struct_0_11651_x1037_2062526569}*[addressport]{lang="FR"}*[\]]{lang="EN-US"}[.]{lang="FR"}

[[无法找到服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_x362151150}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）的]{style="font-family:宋体"}[TCP]{lang="FR"}[代理监听数据信息]{style="font-family:宋体"}

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_x702311079}*[addressport]{lang="FR"}*[\] ]{lang="EN-US"}[is unable to process *event* event in *state* state.]{lang="FR"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_496442628}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）的不能在状态]{style="font-family:宋体"}*[state]{lang="FR"}*[下处理]{style="font-family:宋体"}*[event]{lang="FR"}*[事件]{style="font-family:宋体"}

 

[[Failed to create data packet on server/client]{lang="FR"}[ ]{lang="FR"}[\[]{lang="EN-US"}]{#struct_0_11651_x1037_x1752630553}*[addressport]{lang="FR"}*[\]]{lang="EN-US"}[.]{lang="FR"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1876144831}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）创建报文失败]{style="font-family:宋体"}

 

[[Failed to send packet.]{lang="FR"}]{#struct_0_11651_x1037_x1465871545}

[[发送报文失败]{style="font-family:宋体"}]{#struct_0_11651_x1037_852738524}

 

[[ TCP packet: src=*sip*/*sport*, dst=*dip*/*dport*]{lang="FR"}]{#struct_0_11651_x1037_264826876}

[[             seq=*seqnum*, ack=*acknum*, flag=*flag*]{lang="FR"}]{#struct_0_11651_x1037_1420811240}

[[             win=*winsize*, checksum=*checksum*, datalen=*datalen*, headlen=*headlen*]{lang="FR"}]{#struct_0_11651_x1037_x713345417}

[[TCP]{lang="FR"}]{#struct_0_11651_x1037_1525493803}[报文的信息：]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{style="font-family:宋体"}[/]{lang="FR"}[端口号]{style="font-family:宋体"}*[sip]{lang="FR"}*[/*sport*]{lang="FR"}[，]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{style="font-family:宋体"}[/]{lang="FR"}[端口号]{style="font-family:
  宋体"}*[dip]{lang="FR"}*[/*dport*]{lang="FR"}[，序号]{style="font-family:宋体"}*[seqnum]{lang="FR"}*[，确认序号]{style="font-family:宋体"}*[acknum]{lang="FR"}*[，标志]{style="font-family:宋体"}*[flag]{lang="FR"}*[，窗口大小]{style="font-family:宋体"}*[winsize]{lang="FR"}*[，检验和]{style="font-family:宋体"}*[checksum]{lang="FR"}*[，数据长度]{style="font-family:宋体"}*[datalen]{lang="FR"}*[，首部长度]{style="font-family:宋体"}*[headlen]{lang="FR"}*

 

[ ]{lang="FR"}

[[表1-13 ]{lang="EN-US"}[debugging tcp-proxy event]{lang="EN-US"}]{#struct_0_11651_x1037_2015537938}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1723080571}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_932080991}

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1583977502}

[[\[]{lang="EN-US"}]{#struct_0_11651_x1037_93223637}*[addressport]{lang="FR"}*[\]]{lang="EN-US"}

[[地址端口信息：]{style="font-family:宋体"}]{#struct_0_11651_x1037_580027103}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[sip]{lang="FR"}*]{#struct_0_11651_x1037_x1623750720}[/*sport* \--\> *dip*/*dport*]{lang="FR"}[：]{style="font-family:宋体"}[发起方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="FR"}[端口号]{lang="EN-US" style="font-family:宋体"}*[sip]{lang="FR"}*[/*sport*]{lang="FR"}[，响应方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="FR"}[端口号]{lang="EN-US" style="font-family:宋体"}*[dip]{lang="FR"}*[/*dport*]{lang="FR"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[sip]{lang="FR"}*]{#struct_0_11651_x1037_x1472860304}[/*sport -*-\> None]{lang="FR"}[：发起方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{lang="EN-US" style="font-family:宋体"}*[sip]{lang="FR"}*[/*sport*]{lang="FR"}[，无响应方]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[initial]{lang="FR"}]{#struct_0_11651_x1037_241249703}[：]{style="font-family:宋体"}[未指定地址]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}[端口号]{lang="EN-US" style="font-family:宋体"}

 

[[Application has created a new handle.]{lang="EN-US"}]{#struct_0_11651_x1037_1256023051}

[[应用程序已创建一个新句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_1262012227}

 

[[Application is closing handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_x310060890}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序正在关闭一个句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1119039056}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}

 

[[Application is binding handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_1149018008}*[addressport]{lang="FR"}*[\] to IPv4/IPv6]{lang="EN-US"}*[ sip]{lang="FR"}*[/*sport*]{lang="FR"}[.]{lang="EN-US"}

[[应用程序正在绑定句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_2062592105}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[到]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}*[ ]{lang="EN-US"}[sip]{lang="FR"}*[/*sport*]{lang="FR"}

 

[[Application is connecting to IPv4/IPv6]{lang="EN-US"}]{#struct_0_11651_x1037_x1937690460}*[ sip]{lang="FR"}*[/*sport*]{lang="FR"}[ on handle \[]{lang="EN-US"}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序正在]{style="font-family:宋体"}]{#struct_0_11651_x1037_496508164}[用句柄（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[向]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[/IPv6 *sip*/*sport*]{lang="FR"}[发起连接]{style="font-family:宋体"}

 

[[Application set handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_x185814176}*[addressport]{lang="FR"}*[\] to listening state.]{lang="EN-US"}

[[应用程序设置句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1195436073}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[进入监听状态]{style="font-family:宋体"}

 

[[Application accepted a new connection on handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_x2010362559}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序在句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_1162796509}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[上获取了一个新连接]{style="font-family:宋体"}

 

[[Application registered readable/writable/error event on handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_718520796}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序在句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1155875967}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[上注册了可读]{style="font-family:宋体"}[/]{lang="EN-US"}[可写]{style="font-family:宋体"}[/]{lang="EN-US"}[错误事件]{style="font-family:宋体"}

 

[[Application wanted *datalen* bytes of data, actually received *receivelen* bytes on handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_x1352762709}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序期望通过句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_x847563145}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[接收]{style="font-family:宋体"}*[datalen]{lang="EN-US"}*[字节数据，实际接收]{style="font-family:宋体"}*[receivelen]{lang="EN-US"}*[字节]{style="font-family:宋体"}

 

[[Foreign window on handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_188914840}*[addressport]{lang="FR"}*[\] is not enough, declined to send 0 byte.]{lang="EN-US"}

[[句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_1881320210}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[的外部窗口大小不够，拒绝发送]{style="font-family:宋体"}[0]{lang="EN-US"}[字节数据]{style="font-family:宋体"}

 

[[Application is sending *count* packets on handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_x628721770}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序正在通过句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_x40994091}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[发送]{style="font-family:宋体"}*[count]{lang="EN-US"}*[个报文]{style="font-family:宋体"}

 

[[Application received *count* packets on handle \[]{lang="EN-US"}]{#struct_0_11651_x1037_550695368}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序通过句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1815896773}[（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[接收]{style="font-family:宋体"}*[count]{lang="EN-US"}*[个报文]{style="font-family:宋体"}

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_x1607078032}*[addressport]{lang="FR"}*[\] received a retransmitted packet and ignored it.]{lang="EN-US"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_2078649567}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[收到重传报文，忽略此报文]{style="font-family:宋体"}

 

[*[Datalen ]{lang="EN-US"}*[bytes of overlapping data has been erased from packet, *packet*]{lang="EN-US"}]{#struct_0_11651_x1037_1121805323}

[[应用程序已经从报文中擦除]{style="font-family:宋体"}*[datalen]{lang="EN-US"}*]{#struct_0_11651_x1037_x1806641911}[字节重叠数据，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_1722103157}*[addressport]{lang="FR"}*[\] submitted a pipe writable event to application.]{lang="EN-US"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_x444278618}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[提交一个管道可写事件给应用程序]{style="font-family:宋体"}

 

[[Application ignored a pipe writeable event on server/client \[]{lang="EN-US"}]{#struct_0_11651_x1037_x119687805}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序忽略了句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_1928374377}[服务器]{style="font-family:宋体"}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[上的一个管道可写事件]{style="font-family:宋体"}

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_489382294}*[addressport]{lang="FR"}*[\] submitted *datalen* bytes of data to application.]{lang="EN-US"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_362290436}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[提交]{style="font-family:宋体"}*[datalen]{lang="EN-US"}*[字节数据给应用程序]{style="font-family:宋体"}

 

[[Application ignored *datalen* bytes of data on server/client \[]{lang="EN-US"}]{#struct_0_11651_x1037_x595961884}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序忽略了句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_x108482058}[服务器]{style="font-family:宋体"}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[上的]{style="font-family:宋体"}*[datalen]{lang="EN-US"}*[字节数据]{style="font-family:宋体"}

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_x2010297023}*[addressport]{lang="FR"}*[\] state migrated: *state1* -\> *state2*.]{lang="EN-US"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_x955148377}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[状态迁移：]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[-\> *state2*]{lang="EN-US"}

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_718586332}*[addressport]{lang="FR"}*[\] submitted a new connection to application.]{lang="EN-US"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1574114729}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[向应用程序提交一个新连接]{style="font-family:宋体"}

 

[[Application ignored a new connection on server/client \[]{lang="EN-US"}]{#struct_0_11651_x1037_x847497609}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序忽略了句柄]{style="font-family:宋体"}]{#struct_0_11651_x1037_x910636473}[服务器]{style="font-family:宋体"}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[上的一个新连接]{style="font-family:宋体"}

 

[[Received an expired ACK packet. Ignored it.]{lang="EN-US"}]{#struct_0_11651_x1037_1448459286}

[[收到一个过期的]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_11651_x1037_1881385746}[报文，忽略此报文]{style="font-family:宋体"}

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_1344192152}*[addressport]{lang="FR"}*[\] submitted a disconnection event to application.]{lang="EN-US"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_x40928555}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[向应用程序提交一个连接关闭事件]{style="font-family:宋体"}

 

[[Application ignored a disconnection event on server/client \[]{lang="EN-US"}]{#struct_0_11651_x1037_x1009764414}*[addressport]{lang="FR"}*[\].]{lang="EN-US"}

[[应用程序忽略一个来自]{style="font-family:宋体"}]{#struct_0_11651_x1037_x1607012496}[服务器]{style="font-family:宋体"}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）的]{style="font-family:宋体"}[连接关闭事件]{style="font-family:宋体"}

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_x748154791}*[addressport]{lang="FR"}*[\] window size is not enough. Stopped sending packet.]{lang="EN-US"}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_1121870859}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[的窗口尺寸不足，停止发送报文]{style="font-family:宋体"}

 

[ ]{lang="FR"}

[[表1-14 ]{lang="EN-US"}[debugging tcp-proxy fsm]{lang="EN-US"}]{#struct_0_11651_x1037_x1793117477}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1671681229}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_x1555012013}

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_1565844288}

[[\[]{lang="EN-US"}]{#struct_0_11651_x1037_x444213082}*[addressport]{lang="FR"}*[\]]{lang="EN-US"}

[[地址和端口的信息：]{style="font-family:宋体"}]{#struct_0_11651_x1037_704158729}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[sip]{lang="FR"}*]{#struct_0_11651_x1037_1928439913}[/*sport* \--\> *dip*/*dport*]{lang="FR"}[：]{style="font-family:宋体"}[发起方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="FR"}[端口号]{lang="EN-US" style="font-family:宋体"}*[sip]{lang="FR"}*[/*sport*]{lang="FR"}[，响应方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="FR"}[端口号]{lang="EN-US" style="font-family:宋体"}*[dip]{lang="FR"}*[/*dport*]{lang="FR"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[sip]{lang="FR"}*]{#struct_0_11651_x1037_x771339058}[/*sport -*-\> None]{lang="FR"}[：发起方]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{lang="EN-US" style="font-family:宋体"}*[sip]{lang="FR"}*[/*sport*]{lang="FR"}[，无响应方]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[initial]{lang="FR"}]{#struct_0_11651_x1037_1257236677}[：]{style="font-family:宋体"}[未指定地址]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}[端口号]{lang="EN-US" style="font-family:宋体"}

 

[[Server/Client \[]{lang="EN-US"}]{#struct_0_11651_x1037_362355972}*[addressport]{lang="FR"}*[\] before/after FSM processed *event*]{lang="EN-US"}

[[ Info: seq=*expectsendseq*, ack=*expectsendack*, sent ack=*alreadysendack*, received ack=*foreignack*, lwin=*localwin*, fwin=*foreignwin*]{lang="EN-US"}]{#struct_0_11651_x1037_932267315}

[[ State: *state*.]{lang="EN-US"}]{#struct_0_11651_x1037_1021882130}

[[服务器]{style="font-family:宋体"}]{#struct_0_11651_x1037_x2010231487}[/]{lang="FR"}[客户端（地址端口信息为]{style="font-family:宋体"}*[addressport]{lang="FR"}*[）]{style="font-family:宋体"}[在状态机处理]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件前]{style="font-family:宋体"}[/]{lang="EN-US"}[后的信息：]{style="font-family:宋体"}

[[本端下次发送的起始序号]{style="font-family:宋体"}*[expectsendseq]{lang="EN-US"}*]{#struct_0_11651_x1037_188303317}[，本端期待发送的确认号]{style="font-family:宋体"}*[expectsendack]{lang="EN-US"}*[，本端已发出的确认号]{style="font-family:宋体"}*[alreadysendack]{lang="EN-US"}*[，对端已确认的数据]{style="font-family:宋体"}*[foreignack]{lang="EN-US"}*[，本端当前窗口大小]{style="font-family:宋体"}*[localwin]{lang="EN-US"}*[，对端最后一次有效报文通告的窗口大小]{style="font-family:宋体"}*[foreignwin]{lang="EN-US"}*[，状态]{style="font-family:宋体"}*[state]{lang="EN-US"}*[。其中：]{style="font-family:宋体"}

[*[event]{lang="EN-US"}*]{#struct_0_11651_x1037_x1510538532}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_11651_x1037_718651868}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_11651_x1037_x907167623}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN]{lang="EN-US"}]{#struct_0_11651_x1037_x847432073}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_11651_x1037_x188143587}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RST]{lang="EN-US"}]{#struct_0_11651_x1037_2036518852}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONE]{lang="EN-US"}]{#struct_0_11651_x1037_1881451282}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIMEOUT]{lang="EN-US"}]{#struct_0_11651_x1037_2102324113}

[*[state]{lang="EN-US"}*]{#struct_0_11651_x1037_x40863019}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLSD]{lang="EN-US"}]{#struct_0_11651_x1037_x1391136341}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSTN]{lang="EN-US"}]{#struct_0_11651_x1037_x1606946960}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNSND]{lang="EN-US"}]{#struct_0_11651_x1037_1949035242}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNRCV]{lang="EN-US"}]{#struct_0_11651_x1037_1121936395}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EST]{lang="EN-US"}]{#struct_0_11651_x1037_920471948}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLSWT]{lang="EN-US"}]{#struct_0_11651_x1037_x444147546}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FINWT1]{lang="EN-US"}]{#struct_0_11651_x1037_1492568512}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLSNG]{lang="EN-US"}]{#struct_0_11651_x1037_222278451}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSTACK]{lang="EN-US"}]{#struct_0_11651_x1037_1928505449}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FINWT2]{lang="EN-US"}]{#struct_0_11651_x1037_498521448}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TMWT]{lang="EN-US"}]{#struct_0_11651_x1037_x1884670699}

 

[ ]{lang="FR"}

[[表1-15 ]{lang="EN-US"}[debugging tcp-proxy packet]{lang="EN-US"}]{#struct_0_11651_x1037_362421508}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1675160661}[[字段]{style="font-family:黑体"}]{#struct_0_11651_x1037_x318124718}

[[描述]{style="font-family:黑体"}]{#struct_0_11651_x1037_1025877127}

[[Received a disordered packet: expected seq=*expectseq*, packet seq=*packetseq*.]{lang="EN-US"}]{#struct_0_11651_x1037_x296108481}

[[收到一个乱序报文，期待的序号]{style="font-family:宋体"}*[expectseq]{lang="EN-US"}*]{#struct_0_11651_x1037_x2010165951}[，报文实际的序号]{style="font-family:宋体"}*[packetseq]{lang="EN-US"}*

[[Input packet: Time=*time*, total length=*len*]{lang="EN-US"}]{#struct_0_11651_x1037_1739995393}

[[接收报文的时间]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_11651_x1037_x681456397}[，报文总长度]{style="font-family:宋体"}*[len]{lang="EN-US"}*

[[Output packet: Time=*time*, total length=*len*]{lang="EN-US"}]{#struct_0_11651_x1037_718717404}

[[发送报文的时间]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_11651_x1037_1407332405}[，报文总长度]{style="font-family:宋体"}*[len]{lang="EN-US"}*

[[Processing disordered packet *packet*]{lang="EN-US"}]{#struct_0_11651_x1037_x1177601321}

[[处理乱序报文，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*]{#struct_0_11651_x1037_x847366537}

[[ TCP packet: src=*sip*/*sport*, dst=*dip*/*dport*]{lang="FR"}]{#struct_0_11651_x1037_x1335143090}

[[             seq=*seqnum*, ack=*acknum*, flag=*flag*]{lang="FR"}]{#struct_0_11651_x1037_281908697}

[[             win=*winsize*, checksum=*checksum*, datalen=*datalen*, headlen=*headlen*]{lang="FR"}]{#struct_0_11651_x1037_1881516818}

[[TCP]{lang="FR"}]{#struct_0_11651_x1037_x1366401018}[报文的信息：]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{style="font-family:宋体"}[/]{lang="FR"}[端口号]{style="font-family:宋体"}*[sip]{lang="FR"}*[/*sport*]{lang="FR"}[，]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址]{style="font-family:宋体"}[/]{lang="FR"}[端口号]{style="font-family:
  宋体"}*[dip]{lang="FR"}*[/*dport*]{lang="FR"}[，序号]{style="font-family:宋体"}*[seqnum]{lang="FR"}*[，确认序号]{style="font-family:宋体"}*[acknum]{lang="FR"}*[，标志]{style="font-family:宋体"}*[flag]{lang="FR"}*[，窗口大小]{style="font-family:宋体"}*[winsize]{lang="FR"}*[，检验和]{style="font-family:宋体"}*[checksum]{lang="FR"}*[，数据长度]{style="font-family:宋体"}*[datalen]{lang="FR"}*[，首部长度]{style="font-family:宋体"}*[headlen]{lang="FR"}*

[ ]{lang="FR"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11651_x1037_1943897577}

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_x2086470708}[打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging tcp-proxy error]{lang="EN-US"}]{#struct_0_11651_x1037_749811887}

[\*Jan 16 09:29:23:045 2014 Sysname TCPP/7/FSM: ]{lang="EN-US"}[Failed to send packet]{lang="FR"}[.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_x40797483}*[发送报文失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_319734834}[打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging tcp-proxy event]{lang="EN-US"}]{#struct_0_11651_x1037_1601284846}

[\*Jan 16 09:29:23:075 2014 Sysname TCPP/7/EVENT: -MDC=1; Application is closing a client \[5005::5/80\--\>5005::141/45457\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_582874779}*[应用程序正在关闭一个客户端（源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}[5005::5/80\--\>]{lang="EN-US"}[目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}[5005::141/4547]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_x473649439}[打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging tcp-proxy fsm]{lang="EN-US"}]{#struct_0_11651_x1037_x1634539189}

[\*Jan 16 09:29:23:076 2014 Sysname TCPP/7/FSM: -MDC=1; Server \[5005::5:80\--\>5005::141:45457\] before FSM processed ACK]{lang="EN-US"}

[ Info: seq=0x00b4cc08, ack=0x0e4cbe56, sent ack=0x0e4cbe56, received ack=0x00b4cc07, lwin=65535, fwin=64800]{lang="EN-US"}

[ State: FINWAIT1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_x517547736}*[服务器（本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}[5005::5/80\--\>]{lang="EN-US"}[对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}[5005::141/4547]{lang="EN-US"}[）在状态机处理]{style="font-family:宋体"}[ACK]{lang="EN-US"}[事件前的信息：本端下次发送的起始序号]{style="font-family:宋体"}[0x00b4cc08]{lang="EN-US"}[，本端期待发送的确认号]{style="font-family:宋体"}[0x0e4cbe56]{lang="EN-US"}[，本端已发出的确认号]{style="font-family:宋体"}[0x0e4cbe56]{lang="EN-US"}[，对端已确认的数据]{style="font-family:宋体"}[0x00b4cc07]{lang="EN-US"}[，本端当前窗口大小]{style="font-family:宋体"}[65535]{lang="EN-US"}[，对端最后一次有效报文通告的窗口大小]{style="font-family:宋体"}[64800]{lang="EN-US"}[，状态]{style="font-family:宋体"}[FINWAIT1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_11651_x1037_x1606881424}[打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging tcp-proxy packet]{lang="EN-US"}]{#struct_0_11651_x1037_742219151}

[\*Jan 16 09:29:25:089 2014 Sysname TCPP/7/PACKET: -MDC=1; Input packet: Time=4350167781, total length=572]{lang="EN-US"}

[ TCP packet: src=5005::141/45457, dst=5005::5/80]{lang="EN-US"}

[             seq=0x0e4cbe56, ack=0x00b4cc08, flag=0x18]{lang="EN-US"}

[             win=64800, checksum=0x9cc8, datalen=512, headlen=20]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_11651_x1037_x855863593}*[接收报文的时间为]{style="font-family:宋体"}[4350167781]{lang="EN-US"}[，报文总长度为]{style="font-family:宋体"}[572]{lang="EN-US"}[。]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文的信息：源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}[5005::141/45457]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}[5005::5/80]{lang="EN-US"}[，]{style="font-family:宋体"}[序号]{style="font-family:宋体"}[0x0e4cbe56]{lang="EN-US"}[，确认序号]{style="font-family:宋体"}[0x00b4cc08]{lang="EN-US"}[，标志]{style="font-family:宋体"}[0x18]{lang="EN-US"}[，窗口大小]{style="font-family:宋体"}[64800]{lang="EN-US"}[，检验和]{style="font-family:宋体"}[0x9cc8]{lang="EN-US"}[，数据长度]{style="font-family:宋体"}[512]{lang="EN-US"}[，首部长度]{style="font-family:宋体"}[20]{lang="EN-US"}*
