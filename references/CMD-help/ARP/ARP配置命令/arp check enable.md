::::: {#-177266216 .myid}
[]{#_Toc404786112}[]{#struct_0_21179_14956_x81070462}[]{#_Toc183856418}

**ARP \-- ARP配置命令 \-- arp check enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ARP命令.files/image001.png){#图片 1 width="62" height="27"}]{lang="EN-US"}]{#struct_0_21179_14956_x1859279570}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_21179_14956_2119692297}
:::

[ ]{lang="EN-US"}

[**[arp]{lang="EN-US"}**[ **check** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x2136766715}[命令用来开启动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的检查功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **arp** **check** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_319487598}[命令用来关闭动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x260068212}

[**[arp]{lang="EN-US"}**[ **check** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_2016770951}

[**[undo]{lang="EN-US"}**[ **arp** **check** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x1938753400}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1593211865}

[[动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_77021399}[表项的检查功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1100206885}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x2136439035}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x112126960}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1502037174}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x136118182}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x536574240}

[[动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x1152380917}[表项检查功能可以控制设备上是否可以学习]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文中的发送端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启]{style="font-family:宋体"}]{#struct_0_21179_14956_x28693831}[ARP]{lang="EN-US"}[表项的检查功能后，设备上不能学习]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文中发送端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，也不能手工添加]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭]{style="font-family:宋体"}]{#struct_0_21179_14956_742498424}[ARP]{lang="EN-US"}[表项的检查功能后，设备可以学习以太网源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[且]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文中发送端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，也可以手工添加]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_988891347}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x2136373499}[开启动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_855901804}

[\[Sysname\] arp check enable]{lang="EN-US"}
:::::

::: {#1496166786 .myid}
[]{#_Toc404786113}[]{#struct_0_21179_14956_x2060000395}

**ARP \-- ARP配置命令 \-- arp check log enable**

------------------------------------------------------------------------

[**[arp check log enable]{lang="EN-US"}**]{#struct_0_21179_14956_x736906118}[命令开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[日志信息功能。]{style="font-family:宋体"}

[**[undo arp check log enable]{lang="EN-US"}**]{#struct_0_21179_14956_1817901504}[命令关闭]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[日志信息功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_1304334179}

[**[arp check log enable]{lang="EN-US"}**]{#struct_0_21179_14956_x3344776}

[**[undo arp check log enable]{lang="EN-US"}**]{#struct_0_21179_14956_x2136570107}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_892052973}

[[设备]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x552835432}[日志信息功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1559974904}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x1770367462}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x3192881}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_547854518}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1326611919}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2136504571}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_567438134}[日志是为了满足网络管理员审计的需要，对处理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的信息进行的记录，包括设备未使能]{style="font-family:宋体"}[ARP]{lang="EN-US"}[代理功能时收到目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[不是设备接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转化的外部网络地址；收到的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文中源地址和接收接口地址、]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组中的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换的外部网络地址冲突，且此报文不是]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文等。]{style="font-family:宋体"}

[[设备生成的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x774131834}[日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}

[[为了防止设备输出过多的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x1996284914}[日志信息，一般情况下建议不要打开此功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_813175771}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1281240881}[开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[日志信息功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_29038647}

[\[Sysname\] arp check log enable]{lang="EN-US"}
:::

::::: {#969153939 .myid}
[]{#_Toc69790683}[]{#_Toc404786114}[]{#struct_0_21179_14956_481879600}[]{#_Toc183856419}[]{#_Toc122491180}

**ARP \-- ARP配置命令 \-- arp max-learning-num**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ARP命令.files/image002.png){#图片 2 width="62" height="27"}]{lang="EN-US"}]{#struct_0_21179_14956_x454174275}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_21179_14956_2033590165}
:::

[ ]{lang="EN-US"}

[**[arp]{lang="EN-US"}**[ **max-learning-num**]{lang="EN-US"}]{#struct_0_21179_14956_x2136176891}[命令用来配置接口允许学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **arp** **max-learning-num**]{lang="EN-US"}]{#struct_0_21179_14956_x174104168}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_606065762}

[**[arp]{lang="EN-US"}**[ **max-learning-num** *number*]{lang="EN-US"}]{#struct_0_21179_14956_x626760356}

[**[undo]{lang="EN-US"}**[ **arp** **max-learning-num**]{lang="EN-US"}]{#struct_0_21179_14956_x2013527683}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_865611889}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_21179_14956_x605101159}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_736585076}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_x2136111355}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1814921429}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x306252842}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_1510344582}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_x123611221}

[*[number]{lang="EN-US"}*]{#struct_0_21179_14956_x1940621773}[：接口允许学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1695255862}

[[设备可以通过]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x901091557}[协议自动生成动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。为了防止部分接口下的用户占用过多的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[资源，可以通过设置接口学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数来进行限制。当接口学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的个数达到所设置的值时，该接口将不再学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[当配置接口允许学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x2136701178}[表项的最大个数为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示禁止接口学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_600591431}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_1142413687}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[40]{lang="EN-US"}[上可以学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数为]{style="font-family:宋体"}[500]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_125619903}

[\[Sysname\] interface vlan-interface 40]{lang="EN-US"}

[\[Sysname-Vlan-interface40\] arp max-learning-num 500]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1536469714}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上可以学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x1686453617}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp max-learning-num 1000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x792349059}[配置二层聚合接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上可以学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x2136635642}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] arp max-learning-num 1000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_1820642571}[配置三层聚合接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上可以学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x1897128755}

[\[Sysname\] interface route-aggregation 1]{lang="EN-US"}

[\[Sysname-Route-Aggregation1\] arp max-learning-num 1000]{lang="EN-US"}
:::::

::: {#1634299576 .myid}
[]{#_Toc404786115}[]{#struct_0_21179_14956_190212920}

**ARP \-- ARP配置命令 \-- arp max-learning-number**

------------------------------------------------------------------------

[**[arp max-learning-number]{lang="EN-US"}**]{#struct_0_21179_14956_x812040898}[命令用来配置设备允许学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数。]{style="font-family:宋体"}

[**[undo arp max-learning-number]{lang="EN-US"}**]{#struct_0_21179_14956_x14691920}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1349375194}

[[集中式设备]{style="font-family:宋体"}[:]{lang="EN-US"}]{#struct_0_21179_14956_x2136832250}

[**[arp max-learning-number ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_21179_14956_x654592451}

[**[undo arp max-learning-number]{lang="EN-US"}**]{#struct_0_21179_14956_x114095818}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_x871485559}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[:]{lang="EN-US"}

[**[arp max-learning-number ]{lang="EN-US"}***[number]{lang="EN-US"}*[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_21179_14956_1996054611}

[**[undo arp max-learning-number slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_21179_14956_x720164072}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21179_14956_484191845}[模式]{style="font-family:宋体"}[:]{lang="EN-US"}

[**[arp max-learning-number ]{lang="EN-US"}***[number]{lang="EN-US"}*[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_21179_14956_x233778595}

[**[undo arp max-learning-number chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_21179_14956_161449879}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2136766714}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_21179_14956_1885571539}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_678751081}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_187193640}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x379261054}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x979858115}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x317104598}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_1215079551}

[*[number]{lang="EN-US"}*]{#struct_0_21179_14956_x2017577627}[：设备允许学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x2136439034}[：设置指定单板学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x1678210901}[：设置指定成员设备上学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x1297269154}[：设置指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_994507259}[：设置指定成员设备上指定单板学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x684471541}[：设置指定单板学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_21179_14956_x392523535}[：设置指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_2049996847}

[[设备可以通过]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x903120282}[协议自动生成动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。为了防止用户占用过多的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[资源，可以通过设置设备学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数来进行限制。当设备学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的个数达到所设置的值时，该设备将不再学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[当配置设备允许学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_414118103}[表项的最大个数为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示禁止该设备学习动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2122407154}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_2108216351}[限制单板]{style="font-family:宋体"}[1]{lang="EN-US"}[上学习的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的最大个数为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x2136373498}

[\[Sysname\] arp max-learning-number 64 slot 1]{lang="EN-US"}
:::

::: {#-1715887290 .myid}
[]{#_Toc404786116}[]{#struct_0_21179_14956_x710182137}

**ARP \-- ARP配置命令 \-- arp mode uni**

------------------------------------------------------------------------

[**[arp mode uni]{lang="EN-US"}**]{#struct_0_21179_14956_1313597668}[命令用来配置接口为用户侧接口。]{style="font-family:宋体"}

[**[undo arp mode]{lang="EN-US"}**]{#struct_0_21179_14956_251951383}[命令用来配置接口为网络侧接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_81042164}

[**[arp mode uni]{lang="EN-US"}**]{#struct_0_21179_14956_1508703790}

[**[undo arp mode]{lang="EN-US"}**]{#struct_0_21179_14956_x1176523020}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x354022379}

[[接口为网络侧接口。]{style="font-family:宋体"}]{#struct_0_21179_14956_x2136570106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x674030968}

[[VLAN]{lang="EN-US"}]{#struct_0_21179_14956_829948312}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x895347713}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1931699616}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_1172622724}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1202250247}

[[当接口连接终端主机时，可以配置接口为用户侧接口。对于这种接口上学到的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x559266087}[表项，不再和设备上的路由信息相关联。]{style="font-family:宋体"}

[[当接口连接网络设备时，需要配置接口为网络侧接口。对于这种接口上学到的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x1591462340}[表项，可以与设备上的路由信息关联，可作为路由信息的下一跳。]{style="font-family:宋体"}

[[通过实际使用情况，正确配置接口的工作模式，可以适当的节省硬件资源。]{style="font-family:宋体"}]{#struct_0_21179_14956_x2136504570}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x430200973}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_999809514}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[角色为用户侧接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x1636445174}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] arp mode uni]{lang="EN-US"}
:::

::: {#1305717958 .myid}
[]{#_Toc404786117}[]{#struct_0_21179_14956_x1218045834}

**ARP \-- ARP配置命令 \-- arp multiport**

------------------------------------------------------------------------

[**[arp multiport]{lang="EN-US"}**]{#struct_0_21179_14956_x1740677035}[命令用来配置多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_x2076644476}[命令用来删除]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_91757718}

[**[arp]{lang="EN-US"}**[ **multiport** *ip-address mac-address vlan-id* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_21179_14956_x2136176890}

[**[undo]{lang="EN-US"}**[ **arp** *ip-address* \[ *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_21179_14956_x1740188109}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1002460154}

[[没有配置多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1297210234}[表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_78272748}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x424259345}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_175184421}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1615179363}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_742990135}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2136111354}

[*[ip-address]{lang="EN-US"}*]{#struct_0_21179_14956_913961926}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址部分。]{style="font-family:宋体"}

[*[mac-address]{lang="EN-US"}*]{#struct_0_21179_14956_456221368}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址部分，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_21179_14956_1884134627}[：多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_21179_14956_1454983613}[：指定多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。如果未指定本参数，则表示多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_1205782042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{style="font-family:宋体"}]{#struct_0_21179_14956_x548586921}*[vlan-id]{lang="EN-US"}*[用于指定多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项所对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[必须是用户已经创建好的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备多端口]{style="font-family:宋体"}]{#struct_0_21179_14956_152130958}[ARP]{lang="EN-US"}[表项所对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口被删除时，该表项需删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{lang="EN-US" style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*]{#struct_0_21179_14956_x560378515}[对应的接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址与参数]{lang="EN-US" style="font-family:宋体"}[ip-address]{lang="EN-US"}[对应的地址属于同一网段时，多端口]{lang="EN-US" style="font-family:宋体"}[ARP]{lang="EN-US"}[配置才能生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须配置对应的多端口单播]{style="font-family:宋体"}]{#struct_0_21179_14956_x214386874}[/]{lang="EN-US"}[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项才能指导转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_767736697}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x535374138}[配置一条多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[202.38.10.2]{lang="EN-US"}[，对应的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00e0-fc01-0000]{lang="EN-US"}[，此条]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项属于]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_937299938}

[\[Sysname\] arp multiport 202.38.10.2 00e0-fc01-0000 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x559924611}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **arp** **multiport**]{lang="EN-US"}]{#struct_0_21179_14956_x819519360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_x883227971}**[ multiport]{lang="EN-US"}**
:::

::: {#1608676368 .myid}
[]{#_Toc404786118}[]{#struct_0_21179_14956_x719674862}[]{#_Toc183856421}

**ARP \-- ARP配置命令 \-- arp static**

------------------------------------------------------------------------

[**[arp]{lang="EN-US"}**[ **static**]{lang="EN-US"}]{#struct_0_21179_14956_x214321338}[命令用来配置静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_382557604}[命令用来删除]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x183221623}

[**[arp]{lang="EN-US"}**[ **static** *ip-address mac-address* \[ *vlan-id* *interface-type interface-number \| interface-type interface-number* *interface-type interface-number* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_21179_14956_1671543009}

[**[undo]{lang="EN-US"}**[ **arp** *ip-address* \[ *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_21179_14956_x1290688258}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x268744857}

[[没有配置静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x582618160}[表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x537616299}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x214517946}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_392644381}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1676899918}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x44838060}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1161621267}

[*[ip-address]{lang="EN-US"}*]{#struct_0_21179_14956_x577786499}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址部分。]{style="font-family:宋体"}

[*[mac-address]{lang="EN-US"}*]{#struct_0_21179_14956_x591675830}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址部分，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_21179_14956_1675461686}[：静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_21179_14956_1609084085}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_21179_14956_x214452410}[：指定静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。如果未指定本参数，则表示静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_742517094}

[[静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_636623415}[表项通过手工配置和维护，不会被老化，不会被动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项覆盖，可以增加通信的安全性。]{style="font-family:宋体"}

[[静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x581957514}[表项分为短静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项和长静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。一般情况下，]{style="font-family:宋体"}[ARP]{lang="EN-US"}[动态执行并自动寻求]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址到以太网]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的解析，无需管理员的介入。当希望设备和指定用户只能使用某个固定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址通信时，可以配置短静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，当进一步希望限定这个用户只在某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的某个特定接口上连接时就可以配置长静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_21179_14956_x1206541538}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态]{style="font-family:宋体"}]{#struct_0_21179_14956_x335728006}[ARP]{lang="EN-US"}[表项在设备正常工作时间一直有效，当某设备]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项所对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口被删除时，如果是长静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项则被删除，如果是已经解析的短静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项则重新变为未解析状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于已经解析的短静态]{style="font-family:宋体"}]{#struct_0_21179_14956_1794738062}[ARP]{lang="EN-US"}[表项，也会由于外部事件，比如解析到的出接口状态]{style="font-family:宋体"}[down]{lang="EN-US"}[等原因，恢复到未解析状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于长静态]{style="font-family:宋体"}]{#struct_0_21179_14956_x1451445395}[ARP]{lang="EN-US"}[表项，根据设备的当前状态可能处于有效或无效两种状态。处于无效状态的原因可能是该]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口状态]{style="font-family:宋体"}[down]{lang="EN-US"}[或出接口状态]{style="font-family:宋体"}[down]{lang="EN-US"}[等原因。处于无效状态的长静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项不能指导报文转发。、]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_21179_14956_x763568910}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[用于指定]{lang="EN-US" style="font-family:宋体"}[ARP]{lang="EN-US"}[表项所对应的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为以太网接口。]{lang="EN-US" style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[所对应的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口必须存在，接口]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[必须属于此]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}*[，]{lang="EN-US" style="font-family:宋体"}*[否则系统均将提示出错]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定了参数]{style="font-family:宋体"}]{#struct_0_21179_14956_2048569945}*[vlan-id]{lang="EN-US"}*[时，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[对应的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须和]{lang="EN-US" style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[属于同一网段]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_21179_14956_1907270789}**[undo]{lang="EN-US"}**[命令中没有指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则只删除公网中的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[某些组网环境需要使用参数]{style="font-family:宋体"}]{#struct_0_21179_14956_802515031}*[interface-type interface-number interface-type interface-number]{lang="EN-US"}*[，比如]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[接入]{style="font-family:宋体"}[L3VPN]{lang="EN-US"}[组网，一个]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口会对应多个]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口。那么配置长静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项时，需要通过该参数指定]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[口和]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口之间的对应关系。]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口和]{style="font-family:宋体"}[L2VE]{lang="EN-US"}[子接口的描述和配置请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[使用指导"中的"]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[接入]{style="font-family:宋体"}[L3VPN]{lang="EN-US"}[或]{style="font-family:宋体"}[IP]{lang="EN-US"}[骨干网"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_2136089636}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x173066022}[配置一条静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[202.38.10.2]{lang="EN-US"}[，对应的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00e0-fc01-0000]{lang="EN-US"}[，此条]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项对应的出接口为属于]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x57230017}

[\[Sysname\] arp static 202.38.10.2 00e0-fc01-0000 10 gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1474146937}[配置一条长静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，对应的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00e0-fc01-0000]{lang="EN-US"}[，此条]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项对应的出接口为]{style="font-family:宋体"}[VE-L3VPN1]{lang="EN-US"}[下的]{style="font-family:宋体"}[VE-L2VPN1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x1955608146}

[\[Sysname\] arp static 1.1.1.1 00e0-fc01-0000 ve-l3vpn 1 ve-l2vpn 1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_2019557942}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_558001510}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_311405940}
:::

::: {#-516993627 .myid}
[]{#_Toc404786119}[]{#struct_0_21179_14956_x214059194}[]{#_Toc183856422}[]{#_Toc69790684}[]{#_Toc49089698}

**ARP \-- ARP配置命令 \-- arp timer aging**

------------------------------------------------------------------------

[**[arp]{lang="EN-US"}**[ **timer** **aging**]{lang="EN-US"}]{#struct_0_21179_14956_1106379245}[命令用来配置动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的老化时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **arp** **timer** **aging**]{lang="EN-US"}]{#struct_0_21179_14956_x790413956}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x413874088}

[**[arp]{lang="EN-US"}**[ **timer** **aging** *aging-time*]{lang="EN-US"}]{#struct_0_21179_14956_x442784363}

[**[undo]{lang="EN-US"}**[ **arp** **timer** **aging**]{lang="EN-US"}]{#struct_0_21179_14956_x756203773}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x46623728}

[[动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1424773335}[表项的老化时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_977965395}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x214255802}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x792121396}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1364545283}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_757235504}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_x715884300}

[*[aging-time]{lang="EN-US"}*]{#struct_0_21179_14956_1826661772}[：动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1915115470}

[[为适应网络的变化，]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_421984000}[表需要不断更新。]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表中的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项并非永远有效，每一条记录都有一个生存周期，到达生存周期仍得不到刷新的记录将被从]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表中删除，这个生存周期被称作老化时间。如果在到达老化时间前纪录被刷新，则重新计算老化时间。]{style="font-family:宋体"}

[[配置代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x214190266}[功能后，应该减小动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的老化时间，以尽快使无效动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项失效，减少发给设备而设备却不能转发的报文，以尽快删除无效的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_749785620}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_1107765605}[配置动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的老化时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_440625808}

[\[Sysname\] arp timer aging 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_336311289}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **arp** **timer** **aging**]{lang="EN-US"}]{#struct_0_21179_14956_x1065012134}
:::

::: {#-774465352 .myid}
[]{#_Toc404786120}[]{#struct_0_21179_14956_x1091408033}[]{#_Toc183856423}[]{#_Toc69790686}[]{#_Toc45685348}

**ARP \-- ARP配置命令 \-- display arp**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_372773547}[命令用来显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x249442892}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_21179_14956_x213862586}

[**[display]{lang="EN-US"}**[ **arp** \[ \[ **all** \| **dynamic** \| **multiport** \| **static** \] \| **vlan** *vlan-id* \| **interface** *interface-type interface-number* \] \[ **count** \| **verbose** \]]{lang="EN-US"}]{#struct_0_21179_14956_x1073944077}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_x1559916406}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **arp** \[ \[ **all** \| **dynamic** \| **multiport** \| **static** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \| **vlan** *vlan-id* \| **interface** *interface-type interface-number* \] \[ **count** \| **verbose** \]]{lang="EN-US"}]{#struct_0_21179_14956_603275665}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21179_14956_x810807980}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **arp** \[ \[ **all** \| **dynamic** \| **multiport** \| **static** \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \| **vlan** *vlan-id* \| **interface** *interface-type interface-number* \] \[ **count** \| **verbose** \]]{lang="EN-US"}]{#struct_0_21179_14956_497174468}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1375997235}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_360004770}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x213797050}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_82134872}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_x545428792}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1116752338}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_1593983302}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_1527839156}

[**[all]{lang="EN-US"}**]{#struct_0_21179_14956_1008356431}[：显示所有的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_21179_14956_1243483462}[：显示动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[multiport]{lang="EN-US"}**]{#struct_0_21179_14956_2112540341}[：显示多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_21179_14956_x214386873}[：显示静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_767540089}[：显示指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x729605483}[：显示指定成员设备的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_1431548665}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_358458320}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x1297334690}[：显示指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_21179_14956_1173757019}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_21179_14956_x1082590535}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_21179_14956_589016750}[：显示指定接口的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口类型和接口编号。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_21179_14956_x488719323}[：显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的数目。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_21179_14956_x1138092846}[：显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_1016274209}

[[使用本命令可以查看静态、动态和多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x214321337}[表项的具体内容，包括]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、出接口、表项类型以及老化时间等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x195282263}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x670286777}[显示所有]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display arp all]{lang="EN-US"}]{#struct_0_21179_14956_x214517945}

[  Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid]{lang="EN-US"}

[IP Address       MAC Address     VLAN     Interface              Aging Type]{lang="EN-US"}

[20.1.1.1         00e0-fc00-0001  N/A      N/A                    N/A   S]{lang="PT-BR"}

[193.1.1.70       00e0-fe50-6503  100      GE1/0/1                N/A   IS]{lang="PT-BR"}

[192.168.0.115    000d-88f7-9f7d  1        GE1/0/2                18    D]{lang="PT-BR"}

[192.168.0.39     0012-a990-2241  1        GE1/0/3                20    D]{lang="PT-BR"}

[22.1.1.1         000c-299d-c041  10       N/A                    N/A   M]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_21179_14956_392840989}[显示所有]{style="font-family:宋体"}[ARP]{lang="PT-BR"}[表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display arp all verbose]{lang="PT-BR"}]{#struct_0_21179_14956_x214452409}[]{#_Toc533579660}

[  ]{lang="PT-BR"}[Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid]{lang="EN-US"}

[IP Address       MAC Address     VLAN     Interface              Aging Type]{lang="EN-US"}

[Vpn Instance                   NickNameRb]{lang="PT-BR"}

[20.1.1.1         00e0-fc00-0001  N/A      N/A                    N/A   S]{lang="PT-BR"}

[test                           0x0001]{lang="PT-BR"}

[193.1.1.70       00e0-fe50-6503  100      GE1/0/1                N/A   IS]{lang="PT-BR"}

[\[No Vrf\]                       0x0000]{lang="PT-BR"}

[192.168.0.115    000d-88f7-9f7d  1        GE1/0/2                18    D]{lang="PT-BR"}

[\[No Vrf\]                       0x0000]{lang="PT-BR"}

[192.168.0.39     0012-a990-2241  1        GE1/0/3                20    D]{lang="PT-BR"}

[\[No Vrf\]                       0x0000]{lang="PT-BR"}

[22.1.1.1         000c-299d-c041  10       N/A                    N/A   M]{lang="PT-BR"}

[\[No Vrf\]                       0x0000]{lang="PT-BR"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_743106919}[显示所有]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的数目。]{style="font-family:宋体"}

[[\<Sysname\> display arp all count]{lang="EN-US"}]{#struct_0_21179_14956_559557593}

[ Total number of entries : 5]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display arp]{lang="EN-US"}]{#struct_0_21179_14956_x126573089}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1525210294}[[字段]{style="font-family:黑体"}]{#struct_0_21179_14956_x647733486}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21179_14956_853122269}

[[IP Address]{lang="EN-US"}]{#struct_0_21179_14956_1546590242}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x441105618}[表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_21179_14956_x214124729}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1906680964}[表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_21179_14956_1370432418}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x53011016}[表项所属的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[（当表项类型为静态表项时，"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["表示未解析的短静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项；如果]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项中的接口不属于某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，也显示"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["）]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_21179_14956_x1980702195}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_2027931424}[表项所对应的出接口（当表项类型为静态表项时，"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["表示未解析的短静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项；当表项类型为多端口表项时，"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["表示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项不持有端口信息，需要参考对应的多端口]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_21179_14956_x214059193}

[[动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1106575853}[表项的老化时间，单位为分钟（"]{style="font-family:宋体"}[N/A]{lang="PT-BR"}["表示老化时间不可知或者没有老化时间）]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_21179_14956_x732599733}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x299625807}[表项类型：动态，用]{style="font-family:宋体"}[D]{lang="EN-US"}[表示；静态，用]{style="font-family:宋体"}[S]{lang="EN-US"}[表示；]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[，用]{style="font-family:宋体"}[O]{lang="EN-US"}[表示；]{style="font-family:宋体"}[Rule]{lang="EN-US"}[，用]{style="font-family:宋体"}[R]{lang="EN-US"}[表示；多端口，用]{style="font-family:宋体"}[M]{lang="EN-US"}[表示；无效，用]{style="font-family:宋体"}[I]{lang="EN-US"}[表示]{style="font-family:宋体"}

[[Vpn Instance]{lang="PT-BR"}]{#struct_0_21179_14956_x2104064968}

[[VPN]{lang="EN-US"}]{#struct_0_21179_14956_x214255801}[实例名称，]{style="font-family:宋体"}[\[No Vrf\]]{lang="EN-US"}[表示没有配置相应]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[NickNameRb]{lang="PT-BR"}]{#struct_0_21179_14956_1592229989}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_813318003}[表项的]{style="font-family:宋体"}[NickName]{lang="EN-US"}[（长度为]{style="font-family:宋体"}[4]{lang="EN-US"}[的十六进制数字，例如]{style="font-family:宋体"}[0x012a]{lang="EN-US"}[），关于]{style="font-family:宋体"}[NickName]{lang="EN-US"}[的详细介绍，请参见"]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[TRILL]{lang="EN-US"}["]{style="font-family:宋体"}

[[Total number of entries]{lang="EN-US"}]{#struct_0_21179_14956_x791924788}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x1235420931}[表项数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_516507790}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp]{lang="EN-US"}**[ **static**]{lang="EN-US"}]{#struct_0_21179_14956_2057007877}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_1388308570}

::: {#-2104880608 .myid}
[]{#_Toc404786121}[]{#struct_0_21179_14956_x214190265}[]{#_Toc183856424}[]{#_Toc138923529}

**ARP \-- ARP配置命令 \-- display arp ip-address**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **arp** *ip-address*]{lang="EN-US"}]{#struct_0_21179_14956_749982228}[命令用来显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_129783537}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_21179_14956_1636414843}

[**[display]{lang="EN-US"}**[ **arp** *ip-address* \[ **verbose** \]]{lang="EN-US"}]{#struct_0_21179_14956_1289241126}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_137948237}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **arp** *ip-address* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_21179_14956_930487734}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21179_14956_1189650511}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **arp** *ip-address* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_21179_14956_x213862585}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1073878541}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_1800068328}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2043819836}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_319951187}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_x211428364}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x195725445}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_493061141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_1564249156}

[*[ip-address]{lang="EN-US"}*]{#struct_0_21179_14956_x213797049}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_82724695}[：显示指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x1738732388}[：显示指定成员设备的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x537885339}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_479026616}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x1936286702}[：显示指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_21179_14956_1173560410}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_21179_14956_1865100571}[：显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1151446096}

[[用户可以通过本命令查看指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21179_14956_x1483201432}[地址的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的具体内容，包括]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、出接口、表项类型以及老化时间等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1798855464}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_1672429589}[显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[20.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display arp 20.1.1.1]{lang="EN-US"}]{#struct_0_21179_14956_x214386876}

[  Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid]{lang="EN-US"}

[IP address       MAC address     VLAN     Interface              Aging Type]{lang="EN-US"}

[20.1.1.1         00e0-fc00-0001  N/A      N/A                    N/A   S]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_767867769}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp]{lang="EN-US"}**[ **static**]{lang="EN-US"}]{#struct_0_21179_14956_509239642}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_x334614268}
:::

::: {#1307984816 .myid}
[]{#_Toc69790688}[]{#_Toc49089699}[]{#_Toc404786122}[]{#struct_0_21179_14956_x2054549397}[]{#_Toc183856425}[]{#_Toc323392264}[]{#_Toc323398499}[]{#_Toc324512798}[]{#_Toc323392265}[]{#_Toc323398500}[]{#_Toc324512799}[]{#_Toc323392266}[]{#_Toc323398501}[]{#_Toc324512800}[]{#_Toc323392267}[]{#_Toc323398502}[]{#_Toc324512801}[]{#_Toc323392268}[]{#_Toc323398503}[]{#_Toc324512802}[]{#_Toc323392269}[]{#_Toc323398504}[]{#_Toc324512803}[]{#_Toc323392270}[]{#_Toc323398505}[]{#_Toc324512804}[]{#_Toc323392271}[]{#_Toc323398506}[]{#_Toc324512805}[]{#_Toc323392272}[]{#_Toc323398507}[]{#_Toc324512806}[]{#_Toc323392273}[]{#_Toc323398508}[]{#_Toc324512807}[]{#_Toc323392274}[]{#_Toc323398509}[]{#_Toc324512808}[]{#_Toc323392275}[]{#_Toc323398510}[]{#_Toc324512809}[]{#_Toc323392276}[]{#_Toc323398511}[]{#_Toc324512810}[]{#_Toc323392277}[]{#_Toc323398512}[]{#_Toc324512811}[]{#_Toc323392278}[]{#_Toc323398513}[]{#_Toc324512812}[]{#_Toc323392279}[]{#_Toc323398514}[]{#_Toc324512813}[]{#_Toc323392280}[]{#_Toc323398515}[]{#_Toc324512814}[]{#_Toc323392281}[]{#_Toc323398516}[]{#_Toc324512815}[]{#_Toc323392282}[]{#_Toc323398517}[]{#_Toc324512816}[]{#_Toc323392283}[]{#_Toc323398518}[]{#_Toc324512817}[]{#_Toc323392284}[]{#_Toc323398519}[]{#_Toc324512818}[]{#_Toc323392285}[]{#_Toc323398520}[]{#_Toc324512819}[]{#_Toc323392286}[]{#_Toc323398521}[]{#_Toc324512820}[]{#_Toc323392287}[]{#_Toc323398522}[]{#_Toc324512821}[]{#_Toc323392288}[]{#_Toc323398523}[]{#_Toc324512822}[]{#_Toc323392289}[]{#_Toc323398524}[]{#_Toc324512823}[]{#_Toc323392290}[]{#_Toc323398525}[]{#_Toc324512824}[]{#_Toc323392291}[]{#_Toc323398526}[]{#_Toc324512825}[]{#_Toc323392292}[]{#_Toc323398527}[]{#_Toc324512826}[]{#_Toc323392293}[]{#_Toc323398528}[]{#_Toc324512827}[]{#_Toc323392294}[]{#_Toc323398529}[]{#_Toc324512828}[]{#_Toc323392295}[]{#_Toc323398530}[]{#_Toc324512829}[]{#_Toc323392296}[]{#_Toc323398531}[]{#_Toc324512830}[]{#_Toc323392297}[]{#_Toc323398532}[]{#_Toc324512831}[]{#_Toc323392298}[]{#_Toc323398533}[]{#_Toc324512832}[]{#_Toc323392299}[]{#_Toc323398534}[]{#_Toc324512833}[]{#_Toc323392300}[]{#_Toc323398535}[]{#_Toc324512834}[]{#_Toc323392301}[]{#_Toc323398536}[]{#_Toc324512835}[]{#_Toc323392302}[]{#_Toc323398537}[]{#_Toc324512836}[]{#_Toc323392303}[]{#_Toc323398538}[]{#_Toc324512837}[]{#_Toc323392304}[]{#_Toc323398539}[]{#_Toc324512838}[]{#_Toc323392305}[]{#_Toc323398540}[]{#_Toc324512839}[]{#_Toc323392306}[]{#_Toc323398541}[]{#_Toc324512840}[]{#_Toc323392307}[]{#_Toc323398542}[]{#_Toc324512841}[]{#_Toc323392335}[]{#_Toc323398570}[]{#_Toc324512869}[]{#_Toc323392336}[]{#_Toc323398571}[]{#_Toc324512870}[]{#_Toc323392337}[]{#_Toc323398572}[]{#_Toc324512871}[]{#_Toc323392338}[]{#_Toc323398573}[]{#_Toc324512872}

**ARP \-- ARP配置命令 \-- display arp timer aging**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **arp** **timer** **aging**]{lang="EN-US"}]{#struct_0_21179_14956_x1056993044}[命令用来显示动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的老化时间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x214321340}

[**[display]{lang="EN-US"}**[ **arp** **timer** **aging**]{lang="EN-US"}]{#struct_0_21179_14956_383081893}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_2142482438}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_1298615974}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x555567563}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_1830011442}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_1779540100}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x888327069}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_x796482976}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x214517948}

[[使用本命令可以查看用户配置的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_391989021}[表项的老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x664732870}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1649341795}[显示动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的老化时间。]{style="font-family:宋体"}

[[\<Sysname\> display arp timer aging]{lang="EN-US"}]{#struct_0_21179_14956_766551034}

[Current ARP aging time is 10 minute(s)]{lang="EN-US"}

[[以上显示信息表示动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1836595646}[表项的老化时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2108961427}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp]{lang="EN-US"}**[ **timer** **aging**]{lang="EN-US"}]{#struct_0_21179_14956_1253763041}
:::

::: {#1506497573 .myid}
[]{#_Toc135621952}[]{#_Toc92095572}[]{#_Toc89675317}[]{#_Toc404786123}[]{#struct_0_21179_14956_x214452412}[]{#_Toc183856426}[]{#_Toc138923531}

**ARP \-- ARP配置命令 \-- display arp vpn-instance**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **arp** **vpn-instance**]{lang="EN-US"}]{#struct_0_21179_14956_742386022}[命令用来显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x442623136}

[**[display]{lang="EN-US"}**[ **arp** **vpn-instance** *vpn-instance-name* \[ **count** \]]{lang="EN-US"}]{#struct_0_21179_14956_x1522492174}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_978936224}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x1535333270}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2026187960}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1064444236}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_x1152770990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x214124732}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_1907139717}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_933444927}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_21179_14956_x2090245511}[：表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不可以包含空格，区分大小写。显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_21179_14956_465914107}[：显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x772302064}

[[用户可以通过本命令查看指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_21179_14956_703851373}[实例的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的具体内容，包括]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、出接口、表项类型以及老化时间等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_1502179216}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1593688772}[显示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名为]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> display arp vpn-instance test]{lang="EN-US"}]{#struct_0_21179_14956_x214059196}

[  Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid]{lang="EN-US"}

[IP address       MAC address     VLAN     Interface              Aging Type]{lang="EN-US"}

[20.1.1.1         00e0-fc00-0001  N/A      N/A                    N/A   S]{lang="PT-BR"}[]{#_Toc69790689}[]{#_Toc154822889}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_1106248173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp]{lang="EN-US"}**[ **static**]{lang="EN-US"}]{#struct_0_21179_14956_x1560688379}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_x739089785}
:::

::: {#1232735859 .myid}
[]{#_Toc404786124}[]{#struct_0_21179_14956_1242042851}[]{#_Toc183856428}[]{#_Toc99445785}

**ARP \-- ARP配置命令 \-- reset arp**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_609049251}[命令用来清除]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x214255804}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_21179_14956_x792252468}

[**[reset]{lang="EN-US"}**[ **arp** { **all** \| **dynamic** \| **interface** *interface-type interface-number* \| **multiport** \| **static** }]{lang="EN-US"}]{#struct_0_21179_14956_1001602118}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_1031551601}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ **arp** { **all** \| **dynamic** \| **interface** *interface-type interface-number* \| **multiport** \| **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **static** }]{lang="EN-US"}]{#struct_0_21179_14956_x1861640227}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21179_14956_x938968146}[模式：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ **arp** { **all** \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **dynamic** \| **interface** *interface-type interface-number* \| **multiport** \| **static** }]{lang="EN-US"}]{#struct_0_21179_14956_559253452}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1606083973}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x214190268}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_750178836}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1877234060}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x608410818}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_1955590498}

[**[all]{lang="EN-US"}**]{#struct_0_21179_14956_x1712380809}[：表示清除所有的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_21179_14956_1834527809}[：表示清除动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[multiport]{lang="EN-US"}**]{#struct_0_21179_14956_377271975}[：表示清除多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_21179_14956_x1592782025}[：表示清除静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x213862588}[：表示清除指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x1073026573}[：表示清除指定成员设备的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x1297400226}[：表示清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x421633875}[：表示清除指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x1205276212}[：表示清除指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则清除全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_21179_14956_1174019161}[：表示清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_21179_14956_2026528620}[：表示清除指定接口的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口的类型和编号。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_1474481240}

[[本命令可以单独清除静态、动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1321779172}[表项和多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，也可以单独清除指定单板、指定接口的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_82003800}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x952757001}[清除静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> reset arp static]{lang="EN-US"}]{#struct_0_21179_14956_x1179598225}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_155852024}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp]{lang="EN-US"}**[ **static**]{lang="EN-US"}]{#struct_0_21179_14956_718873705}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **arp**]{lang="EN-US"}]{#struct_0_21179_14956_x1498825995}
:::

[\
]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

::: {.Section3 style="layout-grid:15.75pt"}
:::

::: {#-1164816556 .myid}
[]{#_Toc183856431}[]{#_Toc297209526}[]{#_Toc404786127}[]{#struct_0_21179_14956_767671161}

**免费ARP \-- 免费ARP配置命令 \-- arp ip-conflict log prompt**

------------------------------------------------------------------------

[**[arp ip-conflict log prompt]{lang="EN-US"}**]{#struct_0_21179_14956_x1296194017}[命令用来开启源]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址冲突提示功能。]{style="font-family:宋体"}

[**[undo arp ip-conflict log prompt]{lang="EN-US"}**]{#struct_0_21179_14956_602847483}[命令用来关闭源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址冲突提示功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x236567698}

[**[arp ip-conflict log prompt]{lang="EN-US"}**]{#struct_0_21179_14956_x1611692884}

[**[undo arp ip-conflict log prompt]{lang="EN-US"}**]{#struct_0_21179_14956_x1219172703}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1017358381}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21179_14956_1367958011}[地址冲突提示功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x214321339}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_382492068}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_584395327}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_1617542443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1107129}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x3863891}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1480182289}[在设备上开启源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址冲突提示功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x1798576814}

[\[Sysname\] arp ip-conflict log prompt]{lang="EN-US"}
:::

::: {#543259416 .myid}
[]{#_Toc404786128}[]{#struct_0_21179_14956_x214517947}

**免费ARP \-- 免费ARP配置命令 \-- arp send-gratuitous-arp**

------------------------------------------------------------------------

[**[arp]{lang="EN-US"}**[ **send-gratuitous-arp**]{lang="EN-US"}]{#struct_0_21179_14956_392709917}[命令用来在接口上开启定时发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能，并设置发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的周期。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **arp** **send-gratuitous-arp**]{lang="EN-US"}]{#struct_0_21179_14956_1809990858}[命令用来关闭定时发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x607051064}

[**[arp]{lang="EN-US"}**[ **send-gratuitous-arp** \[ **interval** *milliseconds* \]]{lang="EN-US"}]{#struct_0_21179_14956_x945527530}

[**[undo]{lang="EN-US"}**[ **arp** **send-gratuitous-arp**]{lang="EN-US"}]{#struct_0_21179_14956_x1834038745}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_1398968500}

[[定时发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1288745646}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1423786468}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_x214452411}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_742582630}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_1374695980}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_479040158}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_1516687242}

[**[interval]{lang="EN-US"}***[ milliseconds]{lang="EN-US"}*]{#struct_0_21179_14956_x140871303}[：发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的周期，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[200000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x940538259}

[[配置本命令后，只有当接口链路状态]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_21179_14956_x843729396}[并且配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，此功能才真正生效。]{style="font-family:宋体"}

[[只能为]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_21179_14956_797321965}[虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和手工配置的从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[。主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址可以是手工配置或者通过其他方式获取的，但是从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须是手工配置的。]{style="font-family:宋体"}

[[如果修改了免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x214124731}[报文的发送周期，则在下一个发送周期才能生效。]{style="font-family:宋体"}

[[如果同时在很多接口下开启本功能，或者每个接口有大量的从]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21179_14956_1907205253}[地址，或者两种情况共存的同时又配置很小的发送时间间隔，那么免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的发送频率可能会远远低于用户的预期。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_1704684342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21179_14956_x643500529}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x2060054224}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启定时发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能，发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的周期为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x1500368033}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp send-gratuitous-arp interval 300]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21179_14956_x240914011}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_714555208}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上开启定时发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能，发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的周期为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x214059195}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] arp send-gratuitous-arp interval 300]{lang="EN-US"}
:::

::::: {#-1158166766 .myid}
[]{#_Toc404786129}[]{#struct_0_21179_14956_1106444781}

**免费ARP \-- 免费ARP配置命令 \-- gratuitous-arp-learning enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ARP命令.files/image002.png){#图片 3 width="62" height="27"}]{lang="EN-US"}]{#struct_0_21179_14956_1555822042}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_21179_14956_x140166442}
:::

[ ]{lang="EN-US"}

[**[gratuitous-arp-learning]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x1282190043}[命令用来开启免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的学习功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **gratuitous-arp-learning** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_1934550443}[命令用来关闭免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文学习功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_2057639028}

[**[gratuitous-arp-learning]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x598324979}

[**[undo]{lang="EN-US"}**[ **gratuitous-arp-learning** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x214255803}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x792055860}

[[免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_996967183}[报文的学习功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_1038607818}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x485247225}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1264213481}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_1943460872}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1306180785}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x214190267}

[[开启免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_749851156}[报文学习功能后，设备会根据收到的免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文中携带的信息对自身维护的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表进行修改（新建或者更新]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项）。]{style="font-family:宋体"}

[[关闭免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x1022178833}[报文学习功能后，设备不会根据收到的免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文来新建]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，但是会更新已存在的对应]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。如果用户不希望通过免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文来新建]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，可以关闭免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文学习功能，以节省]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项资源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1341244821}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x2065626616}[开启免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_1467161061}

[\[Sysname\] gratuitous-arp-learning enable]{lang="EN-US"}
:::::

::::: {#-373580119 .myid}
[]{#_Toc404786130}[]{#struct_0_21179_14956_x1652373430}

**免费ARP \-- 免费ARP配置命令 \-- gratuitous-arp-sending enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ARP命令.files/image001.png){#图片 4 width="62" height="27"}]{lang="EN-US"}]{#struct_0_21179_14956_1064241639}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_21179_14956_x213862587}
:::

[ ]{lang="EN-US"}

[**[gratuitous-arp-sending]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x1074009613}[命令用来开启设备收到非同一网段的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求时发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **gratuitous-arp-sending** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x475292007}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_2089544467}

[**[gratuitous-arp-sending]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_1451048322}

[**[undo]{lang="EN-US"}**[ **gratuitous-arp-sending** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x899167765}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_1695324727}

[[设备收到非同一网段的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1046948665}[请求时不发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_1187506057}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x213797051}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_82200408}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_1530799340}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x456964878}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_1155539069}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1071623003}[关闭设备收到非同一网段的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求时发送免费]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x827826042}

[\[Sysname\] undo gratuitous-arp-sending enable]{lang="EN-US"}
:::::

[\
]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

::: {.Section4 style="layout-grid:15.75pt"}
:::

::::: {#1184447219 .myid}
[]{#_Toc404786133}[]{#struct_0_21179_14956_767998841}[]{#_Toc183856464}

**代理ARP \-- 代理ARP配置命令 \-- display local-proxy-arp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ARP命令.files/image001.png){#图片 5 width="62" height="27"}]{lang="EN-US"}]{#struct_0_21179_14956_527398800}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_21179_14956_443907620}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **local-proxy-arp**]{lang="EN-US"}]{#struct_0_21179_14956_1599018722}[命令用来显示本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_1919464406}

[**[display]{lang="EN-US"}**[ **local-proxy-arp** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_21179_14956_491640589}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x81965456}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x1636653747}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x214321342}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_382950821}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_x1700147044}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x76185884}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_1149009131}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_1612078410}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_21179_14956_200583677}[：显示指定接口的本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的状态。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[指定接口类型和接口编号。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_739966878}

[[使用本命令可以查看本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x214517950}[是处于开启（]{style="font-family:宋体"}[enabled]{lang="EN-US"}[）状态还是关闭（]{style="font-family:宋体"}[disabled]{lang="EN-US"}[）状态。]{style="font-family:宋体"}

[[如果指定接口，则显示指定接口的本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_392513310}[的状态；如果不指定接口，则显示所有接口的本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1959163632}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_710148252}[显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[的本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> display local-proxy-arp interface vlan-interface 2]{lang="EN-US"}]{#struct_0_21179_14956_37167176}

[Interface Vlan-interface2]{lang="EN-US"}

[ Local Proxy ARP status: enabled]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_720923076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-proxy-arp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x1220408792}
:::::

::::: {#610060953 .myid}
[]{#_Toc404786134}[]{#struct_0_21179_14956_x960707796}[]{#_Toc183856465}[]{#_Toc92095581}[]{#_Toc89675323}[]{#_Toc87849841}[]{#_Toc78966449}[]{#_Toc77739090}

**代理ARP \-- 代理ARP配置命令 \-- display proxy-arp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ARP命令.files/image002.png){#图片 6 width="62" height="27"}]{lang="EN-US"}]{#struct_0_21179_14956_x214452414}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_21179_14956_742254950}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **proxy-arp**]{lang="EN-US"}]{#struct_0_21179_14956_x475843798}[命令用来显示代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1803978843}

[**[display]{lang="EN-US"}**[ **proxy-arp** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_21179_14956_x1770071932}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_781588751}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x546086591}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1210624832}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_406562185}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_x214124734}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_1907532933}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_x638371312}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_687893941}

[**[interface]{lang="EN-US"}***[ interface-type Interface-number]{lang="EN-US"}*]{#struct_0_21179_14956_x2040398155}[：显示指定接口的代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的状态。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1059410320}

[[使用本命令可以查看代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1348878925}[是处于开启（]{style="font-family:宋体"}[enabled]{lang="EN-US"}[）状态还是关闭（]{style="font-family:宋体"}[disabled]{lang="EN-US"}[）状态。]{style="font-family:宋体"}

[[如果指定接口，则显示指定接口的代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x133765208}[的状态；如果不指定接口，则显示所有接口的代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_171482031}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x214059198}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> display proxy-arp interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_21179_14956_1107165677}

[Interface GigabitEthernet1/0/1]{lang="EN-US"}

[ Proxy ARP status: disabled]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_440756949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[proxy-arp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x1216927628}
:::::

::::: {#-1931154236 .myid}
[]{#_Toc404786135}[]{#struct_0_21179_14956_x1265755989}[]{#_Toc183856466}

**代理ARP \-- 代理ARP配置命令 \-- local-proxy-arp enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ARP命令.files/image002.png){#图片 7 width="62" height="27"}]{lang="EN-US"}]{#struct_0_21179_14956_x1712365350}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_21179_14956_1717550253}
:::

[ ]{lang="EN-US"}

[**[local-proxy-arp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_1312425084}[命令用来开启本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **local-proxy-arp** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x214255806}[命令用来关闭本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x792383540}

[**[local-proxy-arp]{lang="EN-US"}**[ **enable** \[ **ip-range** *startIP* **to** *endIP* \]]{lang="EN-US"}]{#struct_0_21179_14956_642107406}

[**[undo]{lang="EN-US"}**[ **local-proxy-arp** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_1643463661}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_1474809524}

[[本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_179575438}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_54667967}

[[VLAN]{lang="EN-US"}]{#struct_0_21179_14956_1678442292}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x214190270}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_749654549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x97477538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2012520325}

[**[ip-range]{lang="EN-US"}**[ *startIP* **to** *endIP*]{lang="EN-US"}]{#struct_0_21179_14956_x343282743}[：配置对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围进行本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[。]{style="font-family:宋体"}*[startIP]{lang="EN-US"}*[表示起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[endIP]{lang="EN-US"}*[表示结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[startIP]{lang="EN-US"}*[必须小于等于]{style="font-family:宋体"}*[endIP]{lang="EN-US"}*[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_747906930}

[[如果]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1066205710}[请求是从一个网络的主机发往同一网段却不在同一物理网络上的另一台主机，那么连接它们的具有代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能的设备就可以回答该请求，这个过程称作代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[（]{style="font-family:宋体"}[Proxy ARP]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x638870764}[功能屏蔽了分离的物理网络这一事实，使用户使用起来，好像在同一个物理网络上。]{style="font-family:宋体"}

[[代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x1643257068}[分为普通代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[和本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[，二者的应用场景有所区别：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[普通代理]{style="font-family:宋体"}]{#struct_0_21179_14956_x213862590}[ARP]{lang="EN-US"}[的应用场景为：想要互通的主机分别连接到设备的不同三层接口上，且这些主机不在同一个广播域中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地代理]{style="font-family:宋体"}]{#struct_0_21179_14956_x1073550862}[ARP]{lang="EN-US"}[的应用场景为：想要互通的主机连接到设备的同一个三层接口上，且这些主机不在同一个广播域中。]{style="font-family:宋体"}

[[需要注意的是，配置本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x138119098}[功能时，如果配置]{style="font-family:宋体"}**[ip-range]{lang="EN-US"}**[，则一个接口下只能配置一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x711716282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21179_14956_x1851802627}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_268978758}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_238930074}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] local-proxy-arp enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_1117547082}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能，并指定进行]{style="font-family:宋体"}[ARP]{lang="EN-US"}[代理的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x213797054}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] local-proxy-arp enable ip-range 1.1.1.1 to 1.1.1.20]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21179_14956_82397016}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x856387191}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上开启本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_1926218228}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] local-proxy-arp enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_1002363128}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上开启本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能，并指定进行]{style="font-family:宋体"}[ARP]{lang="EN-US"}[代理的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x680349836}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] local-proxy-arp enable ip-range 1.1.1.1 to 1.1.1.20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1862069144}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **local-proxy-arp**]{lang="EN-US"}]{#struct_0_21179_14956_x214386877}
:::::

::::: {#-342272301 .myid}
[]{#_Toc404786136}[]{#struct_0_21179_14956_767802233}[]{#_Toc183856467}

**代理ARP \-- 代理ARP配置命令 \-- proxy-arp enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ARP命令.files/image001.png){#图片 8 width="62" height="27"}]{lang="EN-US"}]{#struct_0_21179_14956_x289930059}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_21179_14956_x241679028}
:::

[ ]{lang="EN-US"}

[**[proxy-arp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x1685574911}[命令用来开启代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **proxy-arp** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_127076983}[命令用来关闭代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x558163146}

[**[proxy-arp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x440167376}

[**[undo]{lang="EN-US"}**[ **proxy-arp** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x214321341}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_383016357}

[[代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_969703708}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1385829673}

[[VLAN]{lang="EN-US"}]{#struct_0_21179_14956_x1962782430}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1905174029}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_1112993151}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x760240590}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_392054557}

[[如果]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1429655025}[请求是从一个网络的主机发往同一网段却不在同一物理网络上的另一台主机，那么连接它们的具有代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能的设备就可以回答该请求，这个过程称作代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[（]{style="font-family:宋体"}[Proxy ARP]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1481889227}[功能屏蔽了分离的物理网络这一事实，使用户使用起来，好像在同一个物理网络上。]{style="font-family:宋体"}

[[代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_943277615}[分为普通代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[和本地代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[，二者的应用场景有所区别：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[普通代理]{style="font-family:宋体"}]{#struct_0_21179_14956_1637697937}[ARP]{lang="EN-US"}[的应用场景为：想要互通的主机分别连接到设备的不同三层接口上，且这些主机不在同一个广播域中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地代理]{style="font-family:宋体"}]{#struct_0_21179_14956_1211741958}[ARP]{lang="EN-US"}[的应用场景为：想要互通的主机连接到设备的同一个三层接口上，且这些主机不在同一个广播域中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x910258130}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21179_14956_x560433456}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x214452413}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_742451558}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] proxy-arp enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_21179_14956_x1367032850}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_588863845}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[上开启代理]{style="font-family:宋体"}[ARP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x1509244321}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] proxy-arp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_2080053677}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **proxy-arp**]{lang="EN-US"}]{#struct_0_21179_14956_x1877346723}
:::::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section5 style="layout-grid:15.75pt"}
:::

::: {#-1976820917 .myid}
[]{#_Toc404786139}[]{#struct_0_21179_14956_1282659306}[]{#_Toc297209528}[]{#_Toc183856457}[]{#_Toc182033660}[]{#_Toc181443086}

**ARP Snooping \-- ARP Snooping配置命令 \-- arp snooping enable**

------------------------------------------------------------------------

[**[arp]{lang="EN-US"}**[ **snooping** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x1373550861}[命令用来开启]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **arp** **snooping** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_224501146}[命令用来关闭]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x735663114}

[**[arp]{lang="EN-US"}**[ **snooping** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_1528452976}

[**[undo]{lang="EN-US"}**[ **arp** **snooping** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x214059197}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_1106313709}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_797945714}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_795828640}

[[VLAN]{lang="EN-US"}]{#struct_0_21179_14956_1943293863}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_283496319}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x2025030685}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x968335510}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1660459029}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x214255805}[开启]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[下的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x792186932}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] arp snooping enable]{lang="EN-US"}
:::

::: {#-1408194669 .myid}
[]{#_Toc404786140}[]{#struct_0_21179_14956_637079256}[]{#_Toc297209529}[]{#_Toc183856458}[]{#_Toc182033661}[]{#_Toc181443087}

**ARP Snooping \-- ARP Snooping配置命令 \-- display arp snooping**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **arp** **snooping**]{lang="EN-US"}]{#struct_0_21179_14956_x2021785681}[命令用来显示]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_764438855}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_21179_14956_x1858613559}

[**[display]{lang="EN-US"}**[ **arp** **snooping**]{lang="EN-US"}[ \[ **vlan** *vlan-id* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_21179_14956_x605332963}

[**[display]{lang="EN-US"}**[ **arp** **snooping**]{lang="EN-US"}[ **ip** *ip-address*]{lang="EN-US"}]{#struct_0_21179_14956_x387446812}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_x214190269}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **arp** **snooping**]{lang="EN-US"}[ \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_21179_14956_750244372}

[**[display]{lang="EN-US"}**[ **arp** **snooping**]{lang="EN-US"}[ **ip** *ip-address* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_21179_14956_x1539992350}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21179_14956_x723152837}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **arp** **snooping**]{lang="EN-US"}[ \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_21179_14956_x793908725}

[**[display]{lang="EN-US"}**[ **arp** **snooping**]{lang="EN-US"}[ **ip** *ip-address* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_21179_14956_1413775795}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x832150898}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x291708407}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x213862589}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1073092109}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_1952802798}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_1541356250}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_369854553}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_1167175261}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_21179_14956_351574710}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_21179_14956_1978560864}[：显示当前]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项的计数。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_21179_14956_x1171049378}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x213797053}[：显示指定单板上的所有]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_82069336}[：显示指定成员设备上的所有]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x122847304}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x1730568094}[：显示指定成员设备上指定单板上的所有]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x786592447}[：显示指定单板上的所有]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_21179_14956_1173953622}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2074937247}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1019685852}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[下的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> display arp snooping vlan 2]{lang="EN-US"}]{#struct_0_21179_14956_1351697067}

[IP Address   MAC Address    VLAN ID Interface  Aging       Status]{lang="EN-US"}

[3.3.3.3      0003-0003-0003 2       GE1/0/1    20          Valid]{lang="EN-US"}

[3.3.3.4      0004-0004-0004 2       GE1/0/2    5           Invalid]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1318980468}[显示当前]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项的计数。]{style="font-family:宋体"}

[[\<Sysname\> display arp snooping count]{lang="EN-US"}]{#struct_0_21179_14956_x1740810956}

[Total entries: 2]{lang="EN-US"}

[[表4-1 ]{lang="EN-US"}[display arp snooping]{lang="EN-US"}]{#struct_0_21179_14956_x2144806306}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1520885484}[[字段]{style="font-family:黑体"}]{#struct_0_21179_14956_782232461}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21179_14956_1521305486}

[[IP Address]{lang="EN-US"}]{#struct_0_21179_14956_x900803031}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_1306361164}[表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_21179_14956_1351762603}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_x915522694}[表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_21179_14956_x1942951599}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_x74599619}[表项所属的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_21179_14956_x1948625385}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_x1425229676}[表项所对应的入接口]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_21179_14956_1351565995}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_297459056}[表项的老化时间，单位为分钟。当显示]{style="font-family:宋体"}[N/A]{lang="EN-US"}[时，表示当前槽位不是创建]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项的端口所在的槽位]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_21179_14956_x440588117}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_1275246088}[表项的状态，分为以下三种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_21179_14956_273674467}[：有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_21179_14956_1351631531}[：无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Collision]{lang="EN-US"}]{#struct_0_21179_14956_x922636239}[：冲突]{lang="EN-US" style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_21179_14956_x1047979935}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_x82828169}[表项数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_1201500821}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset arp snooping]{lang="EN-US"}**]{#struct_0_21179_14956_x1433590971}

::: {#-1554959152 .myid}
[]{#_Toc404786141}[]{#struct_0_21179_14956_x1623558840}[]{#_Toc297209530}[]{#_Toc183856459}[]{#_Toc182033662}[]{#_Toc181443088}

**ARP Snooping \-- ARP Snooping配置命令 \-- reset arp snooping**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **arp** **snooping**]{lang="EN-US"}]{#struct_0_21179_14956_x539589213}[命令用来清除]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_1351959211}

[**[reset]{lang="EN-US"}**[ **arp** **snooping** \[ **ip** *ip-address* \| **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_21179_14956_x1362734040}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_309811352}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x1899498947}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_1982167045}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x2140023512}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_1839693701}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1106278028}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_21179_14956_x454395133}[：清除指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_21179_14956_1352024747}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x264809815}

[[如果没有指定参数，则清除所有的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}]{#struct_0_21179_14956_x156110454}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_1545990659}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_839074481}[清除]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[下的]{style="font-family:宋体"}[ARP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> reset arp snooping vlan 2]{lang="EN-US"}]{#struct_0_21179_14956_x532986722}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_1202156181}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display arp snooping]{lang="EN-US"}**]{#struct_0_21179_14956_x1224536839}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section6 style="layout-grid:15.75pt"}
:::

::: {#1739146267 .myid}
[]{#_Toc404786144}[]{#struct_0_21179_14956_54328325}[]{#_Toc297209532}

**ARP快速应答 \-- ARP快速应答配置命令 \-- arp fast-reply enable**

------------------------------------------------------------------------

[**[arp]{lang="EN-US"}**[ **fast-reply** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x1225396728}[命令用来开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[快速应答功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **arp** **fast-reply** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_x84660936}[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[快速应答功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_1702963973}

[**[arp]{lang="EN-US"}**[ **fast-reply** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_1440394796}

[**[undo]{lang="EN-US"}**[ **arp** **fast-reply** **enable**]{lang="EN-US"}]{#struct_0_21179_14956_1746497926}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x883884980}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1351893675}[快速应答功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_624412221}

[[VLAN]{lang="EN-US"}]{#struct_0_21179_14956_2033728697}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2032423606}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_1873442603}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1297801799}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_36429224}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_1109871258}[开启]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[下的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[快速应答功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_1352221355}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] arp fast-reply enable]{lang="EN-US"}
:::

[\
]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

::: {.Section7 style="layout-grid:15.75pt"}
:::

::: {#-1660619715 .myid}
[]{#_Toc404786147}[]{#struct_0_21179_14956_x1599037439}

**即插即用网关 \-- 即插即用网关配置命令 \-- arp pnp**

------------------------------------------------------------------------

[**[arp pnp]{lang="EN-US"}**]{#struct_0_21179_14956_x1346501625}[命令用来开启即插即用网关功能。]{style="font-family:宋体"}

[**[undo arp pnp]{lang="EN-US"}**]{#struct_0_21179_14956_77659439}[命令用来关闭即插即用网关功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x471228125}

[**[arp pnp]{lang="EN-US"}**]{#struct_0_21179_14956_x838390327}

[**[undo arp pnp]{lang="EN-US"}**]{#struct_0_21179_14956_57991732}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_1566567068}

[[即插即用网关功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_21179_14956_850428771}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_1792121732}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_x2129468429}[三层以太网子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1128102072}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1489715588}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x88324540}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_779717455}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目前该功能需要]{style="font-family:宋体"}]{#struct_0_21179_14956_x828894858}[NAT]{lang="EN-US"}[功能一起配合使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启该功能前，需要在设备上使用]{style="font-family:宋体"}]{#struct_0_21179_14956_295972715}**[reset arp]{lang="EN-US"}**[命令删除接口下的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，以防止功能冲突。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启该功能后，还需要依赖接口主]{style="font-family:宋体"}]{#struct_0_21179_14956_x838586935}[IP]{lang="EN-US"}[地址及对应掩码生成代理地址池。即如果配置了]{style="font-family:宋体"}[24]{lang="EN-US"}[位掩码的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址则可以生成]{style="font-family:宋体"}[253]{lang="EN-US"}[个代理地址，且排除接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。目前接口下支持代理地址个数最大值与设备型号有关，请以设备实际情况为准。只有接口下存在主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即插即用功能才能完全生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启该功能后会导致该接口路由及]{style="font-family:宋体"}]{#struct_0_21179_14956_800782653}[ARP]{lang="EN-US"}[部分特性（如]{style="font-family:宋体"}[ARP]{lang="EN-US"}[代理功能）不可使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x906090576}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x628363141}[开启即插即用网关功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x838521399}

[\[sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp pnp]{lang="EN-US"}
:::

::: {#1750070618 .myid}
[]{#_Toc404786148}[]{#struct_0_21179_14956_1596616162}

**即插即用网关 \-- 即插即用网关配置命令 \-- display arp pnp**

------------------------------------------------------------------------

[**[display arp pnp]{lang="EN-US"}**]{#struct_0_21179_14956_x1473887846}[命令用来显示接入点在即插即用网关上的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1624304785}

[**[display arp pnp]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_21179_14956_2110138507}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1817993957}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x392398909}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x636059412}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x750186004}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_379467363}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x317328738}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_x837669431}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_x589294833}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_21179_14956_x1057548622}[：显示指定接口上的接入点在即插即用网关上的信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口类型和接口编号。如果不指定接口，则显示所有的接入点在即插即用网关上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2022225403}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_1024471078}[显示设备上所有的接入点在即插即用网关上的信息。]{style="font-family:宋体"}

[[\<Sysname\> display arp pnp]{lang="EN-US"}]{#struct_0_21179_14956_x1872779276}

[Total number of entries : 5]{lang="EN-US"}

[Agent IP address   User IP address   MAC address      Interface   Aging]{lang="EN-US"}

[1.1.1.2            20.1.1.1          00e0-fc00-0001   GE1/0/1     10]{lang="EN-US"}

[1.1.1.3            193.1.1.70        00e0-fe50-6503   GE1/0/1     5]{lang="EN-US"}

[2.2.2.2            192.168.0.115     000d-88f7-9f7d   GE1/0/2     11]{lang="EN-US"}

[3.3.3.3            192.168.0.39      0012-a990-2241   GE1/0/3     5 ]{lang="EN-US"}

[3.3.3.4            22.1.1.1          000c-299d-c041   GE1/0/3     14]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x597710171}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的接入点在即插即用网关上的信息。]{style="font-family:宋体"}

[[\<Sysname\> display arp pnp interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_21179_14956_x837603895}

[Total number of entries : 2]{lang="EN-US"}

[Agent IP address   User IP address   MAC address      Interface   Aging]{lang="EN-US"}

[1.1.1.2            20.1.1.1          00e0-fc00-0001   GE1/0/1     10]{lang="EN-US"}

[1.1.1.3            193.1.1.70        00e0-fe50-6503   GE1/0/1     5]{lang="EN-US"}

[[表6-1 ]{lang="EN-US"}[display arp pnp]{lang="EN-US"}]{#struct_0_21179_14956_x1772529801}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_681123782}[[字段]{style="font-family:黑体"}]{#struct_0_21179_14956_1422975644}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21179_14956_x821963540}

[[Agent IP address]{lang="EN-US"}]{#struct_0_21179_14956_x838193718}

[[设备分配的代理]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21179_14956_2021742252}[地址]{style="font-family:宋体"}

[[User IP address]{lang="EN-US"}]{#struct_0_21179_14956_1492586617}

[[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_21179_14956_x838128182}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_21179_14956_768771808}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_21179_14956_x838324790}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_21179_14956_1234767823}

[[接入点在即插即用网关上的表项所对应的接口]{style="font-family:宋体"}]{#struct_0_21179_14956_x261572885}

[[Aging]{lang="EN-US"}]{#struct_0_21179_14956_x838259254}

[[表项的老化时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_21179_14956_x383970775}

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section8 style="layout-grid:15.75pt"}
:::

::: {#853638386 .myid}
[]{#_Toc404786151}[]{#struct_0_21179_14956_2106442475}

**ARP泛洪抑制 \-- ARP泛洪抑制配置命令 \-- arp suppression enable**

------------------------------------------------------------------------

[**[arp suppression enable]{lang="EN-US"}**]{#struct_0_21179_14956_x358863178}[命令用来开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[**[undo arp suppression enable]{lang="EN-US"}**]{#struct_0_21179_14956_x306473671}[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1678607156}

[**[arp suppression enable]{lang="EN-US"}**]{#struct_0_21179_14956_780818077}

[**[undo arp suppression enable]{lang="EN-US"}**]{#struct_0_21179_14956_x1731458492}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_195569732}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x2061241200}[泛洪抑制功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1833815403}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_21179_14956_789088638}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x607150459}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x144838439}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_333952683}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1626790965}

[[配置交叉连接视图时，需要先配置]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_21179_14956_1915640848}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_827327711}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x763849254}[开启交叉连接组]{style="font-family:宋体"}[1]{lang="EN-US"}[，交叉连接]{style="font-family:宋体"}[2]{lang="EN-US"}[下的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_1003286919}

[\[Sysname\] xconnect-group 1]{lang="EN-US"}

[\[Sysname-xcg-1\] connection 2]{lang="EN-US"}

[\[Sysname-xcg-1-2\] arp suppression enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_2079264097}

[]{#_Toc375570478}[]{#_Toc373844273}[]{#_Toc373593097}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp suppression push interval]{lang="EN-US"}**]{#struct_0_21179_14956_x606953851}
:::

::: {#542316273 .myid}
[]{#_Toc404786152}[]{#struct_0_21179_14956_x126911194}

**ARP泛洪抑制 \-- ARP泛洪抑制配置命令 \-- arp suppression push interval**

------------------------------------------------------------------------

[**[arp suppression push interval]{lang="EN-US"}**]{#struct_0_21179_14956_532248161}[命令配置开启推送]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项功能，并配置推送时间间隔。]{style="font-family:宋体"}

[**[undo arp suppression push interval]{lang="EN-US"}**]{#struct_0_21179_14956_1413584890}[命令用来关闭设备主动推送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1997482249}

[**[arp suppression push interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_21179_14956_1112276886}

[**[undo arp suppression push interval]{lang="EN-US"}**]{#struct_0_21179_14956_438890133}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x850209342}

[[设备不会主动推送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_21179_14956_272835104}[泛洪抑制表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1644389550}

[[系统视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x3044640}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_1902699793}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x607019387}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_975440360}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_873915491}

[*[interval]{lang="EN-US"}*]{#struct_0_21179_14956_x1125229481}[：]{style="font-family:宋体"}[主动推送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟**。**]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_21179_14956_x395834440}

[[使用]{style="font-family:宋体"}**[arp suppression push interval]{lang="EN-US"}**]{#struct_0_21179_14956_x1230571247}[命令用来设置主动推送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息的时间间隔，如果当前主动推送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息的功能未开启，将会同时开启主动推送功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_1591575589}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_100906466}[开启主动推送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项功能，将主动推送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项信息的时间设为]{style="font-family:宋体"}[2]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x727845284}

[\[Sysname\] arp suppression ]{lang="EN-US"}[push interval 2 ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_134128658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp suppression enable]{lang="EN-US"}**]{#struct_0_21179_14956_x606822779}
:::

::: {#1268500309 .myid}
[]{#_Toc404786153}[]{#struct_0_21179_14956_x2137651026}[]{#_Toc375570476}[]{#_Toc373844271}[]{#_Toc373593095}

**ARP泛洪抑制 \-- ARP泛洪抑制配置命令 \-- display arp suppression xconnect-group**

------------------------------------------------------------------------

[**[display arp suppression xconnect-group]{lang="EN-US"}**]{#struct_0_21179_14956_1865589156}[命令用来显示]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_474030825}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_21179_14956_x1777347704}

[**[display]{lang="EN-US"}**[ **arp** **suppression xconnect-group** \[ **name** *group-name* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_21179_14956_x527567739}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_21179_14956_x1642754914}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **arp** **suppression xconnect-group** \[ **name** *group-name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_21179_14956_430659517}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_21179_14956_x1314040298}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **arp** **suppression xconnect-group** \[ **name** *group-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_21179_14956_x3851566}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_930238304}

[[任意视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x606888315}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1412000066}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_1756395263}

[[network-operator]{lang="EN-US"}]{#struct_0_21179_14956_x7217618}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_733583161}

[[mdc-operator]{lang="EN-US"}]{#struct_0_21179_14956_x148273151}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_x319448052}

[**[name]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_21179_14956_x1338542216}[：交叉连接组的名称，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不能包含字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["，区分大小写。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_21179_14956_x1022907064}[：当前]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制]{style="font-family:宋体"}[表项的数目。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_1945815941}[：显示指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_x607347070}[：显示指定成员设备的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_21179_14956_1490225268}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_219041514}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_21179_14956_x2057128254}[：显示指定单板的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_21179_14956_738044541}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_1656595470}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_556916067}[显示所有交叉连接组下的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression xconnect-group]{lang="EN-US"}]{#struct_0_21179_14956_x74759515}

[IP address      MAC address     Xconnect-group       Connection           Aging]{lang="EN-US"}

[100.1.1.1       000c-29fe-5a8f  vpna                 svc                  12]{lang="EN-US"}

[100.1.1.2       000c-29fe-5aa3  vpna                 svc                  25]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x2084129952}[显示当前]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项的计数。]{style="font-family:宋体"}

[[\<Sysname\> display arp suppression xconnect-group count]{lang="EN-US"}]{#struct_0_21179_14956_896116078}

[Total entries: 2]{lang="EN-US"}

[[表7-1 ]{lang="EN-US"}[display arp suppression xconnect-group]{lang="EN-US"}]{#struct_0_21179_14956_1250061692}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_489657221}[[字段]{style="font-family:黑体"}]{#struct_0_21179_14956_x607412606}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_21179_14956_x1698559957}

[[IP address]{lang="EN-US"}]{#struct_0_21179_14956_x1767786812}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x1827933836}[泛洪抑制表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_21179_14956_x607215998}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_562378687}[泛洪抑制表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Xconnect-group]{lang="EN-US"}]{#struct_0_21179_14956_1378171469}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1759232079}[泛洪抑制表项的]{style="font-family:宋体"}[Xconnect-group]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Connection]{lang="EN-US"}]{#struct_0_21179_14956_x607281534}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_215377241}[泛洪抑制表项的]{style="font-family:宋体"}[Connection]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_21179_14956_628109114}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_x1272983932}[泛洪抑制表项的老化时间，单位为分钟]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1439628185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset arp suppression xconnect-group]{lang="EN-US"}**]{#struct_0_21179_14956_x607084926}

::: {#909786442 .myid}
[]{#_Toc404786154}[]{#struct_0_21179_14956_2106245867}[]{#_Toc375570477}[]{#_Toc373844272}[]{#_Toc373593096}

**ARP泛洪抑制 \-- ARP泛洪抑制配置命令 \-- reset arp suppression xconnect-group**

------------------------------------------------------------------------

[**[reset arp suppression xconnect-group]{lang="EN-US"}**]{#struct_0_21179_14956_x730702296}[命令用来清除]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_618515442}

[**[reset arp]{lang="EN-US"}**[ **suppression xconnect-group** \[ **name** *group-name* \]]{lang="EN-US"}]{#struct_0_21179_14956_166280761}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x607150462}

[[用户视图]{style="font-family:宋体"}]{#struct_0_21179_14956_x144510756}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_1930694964}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x734838169}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x1236563988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_21179_14956_267207284}

[**[name]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_21179_14956_x603450953}[：交叉连接组的名称，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不能包含字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x126714586}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_537538327}[清除所有交叉连接组下的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[\<Sysname\> reset arp suppression ]{lang="EN-US"}]{#struct_0_21179_14956_x325609272}[xconnect-group ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x688121074}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display arp suppression xconnect-group]{lang="EN-US"}**]{#struct_0_21179_14956_1419950334}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section9 style="layout-grid:15.75pt"}
:::

::: {#1122116310 .myid}
[]{#_Toc404786157}[]{#struct_0_21179_14956_x1891194541}

**ARP直连路由通告 \-- ARP直连路由通告配置命令 \-- arp route-direct advertise**

------------------------------------------------------------------------

[**[arp route-direct advertise]{lang="EN-US"}**]{#struct_0_21179_14956_x1509870925}[命令用来开启]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[直连路由通告功能。]{style="font-family:宋体"}

[**[undo arp route-direct advertise]{lang="EN-US"}**]{#struct_0_21179_14956_1663766972}[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[直连路由通告功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_21179_14956_x607019390}

[**[arp route-direct advertise]{lang="EN-US"}**]{#struct_0_21179_14956_975768041}

[**[undo arp route-direct advertise]{lang="EN-US"}**]{#struct_0_21179_14956_392708727}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_21179_14956_x2045528388}

[[ARP]{lang="EN-US"}]{#struct_0_21179_14956_1879192405}[直连路由通告功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_21179_14956_x1280958946}

[[L3VE]{lang="EN-US"}]{#struct_0_21179_14956_x1089482251}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_21179_14956_x682989005}

[[network-admin]{lang="EN-US"}]{#struct_0_21179_14956_x97905391}

[[mdc-admin]{lang="EN-US"}]{#struct_0_21179_14956_x428491}

[[【举例】]{style="font-family:黑体"}]{#struct_0_21179_14956_x167733450}

[[\# ]{lang="EN-US"}]{#struct_0_21179_14956_x1184858315}[在]{style="font-family:宋体"}[L3VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[下开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[直连路由通告功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_21179_14956_x606822782}

[\[Sysname\] interface ve-l3vpn 1]{lang="EN-US"}

[\[Sysname-VE-L3VPN1\] arp route-direct advertise]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
