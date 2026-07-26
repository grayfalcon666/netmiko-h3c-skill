::: {#-1840855101 .myid}
[]{#_Toc47323842}[]{#_Toc404786708}[]{#struct_0_13325_x2064_x1451585102}[]{#_Toc138239299}[]{#_Toc136679737}[]{#_Toc69790797}

**IP性能优化 \-- IP性能优化配置命令 \-- display icmp statistics**

------------------------------------------------------------------------

[**[display icmp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x1238613798}[命令用来显示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_829375146}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2047017582}

[**[display icmp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_1323361336}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x116152159}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display icmp statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x1781602079}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x841440624}[模式：]{style="font-family:宋体"}

[**[display icmp statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x219803312}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1248294223}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_1716220330}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x654441115}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_829309610}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x1267311764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1329913043}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x2105641155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x176550397}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1084095895}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1005170525}[：显示指定成员设备的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1658298511}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x815062071}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1346782697}[：显示指定单板的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_x507235550}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1399777408}

[**[display icmp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_829506218}[命令用来显示设备接收和发送的各类]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_980650248}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_358373425}[显示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display icmp statistics]{lang="EN-US"}]{#struct_0_13325_x2064_829440682}

[  Input: bad formats   0                   bad checksum            0]{lang="EN-US"}

[         echo          175                 destination unreachable 0]{lang="EN-US"}

[         source quench 0                   redirects               0]{lang="EN-US"}

[         echo replies  201                 parameter problem       0]{lang="EN-US"}

[         timestamp     0                   information requests    0]{lang="EN-US"}

[         mask requests 0                   mask replies            0]{lang="EN-US"}

[         time exceeded 0                   invalid type            0]{lang="EN-US"}

[         router advert 0                   router solicit          0]{lang="EN-US"}

[         broadcast/multicast echo requests ignored            0]{lang="EN-US"}

[         broadcast/multicast timestamp requests ignored       0]{lang="EN-US"}

[ Output: echo          0                   destination unreachable 0]{lang="EN-US"}

[         source quench 0                   redirects               0]{lang="EN-US"}

[         echo replies  175                 parameter problem       0]{lang="EN-US"}

[         timestamp     0                   information replies     0]{lang="EN-US"}

[         mask requests 0                   mask replies            0]{lang="EN-US"}

[         time exceeded 0                   bad address             0]{lang="EN-US"}

[         packet error  1442                router advert           3]{lang="EN-US"}

[]{#struct_0_13325_x2064_x959096058}[]{#_Toc138413615}[]{#_Toc138239194}[]{#_Toc68600616}[]{#_Toc58505325}[[表1-1 ]{lang="EN-US"}[display icmp statistics]{lang="EN-US"}]{#_Toc43289059}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_x2072610184}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_x804637186}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1871884419}

[[bad formats]{lang="EN-US"}]{#struct_0_13325_x2064_1998285546}

[[输入的格式错误报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1892988612}

[[bad checksum]{lang="EN-US"}]{#struct_0_13325_x2064_x940395857}

[[输入的校验和错误报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1930841311}

[[echo]{lang="EN-US"}]{#struct_0_13325_x2064_829637290}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x680425119}[输出的响应请求报文数]{style="font-family:宋体"}

[[destination unreachable]{lang="EN-US"}]{#struct_0_13325_x2064_388533233}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_705660248}[输出的目的不可达报文数]{style="font-family:宋体"}

[[source quench]{lang="EN-US"}]{#struct_0_13325_x2064_595927335}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_1108588153}[输出的源站抑制报文数]{style="font-family:宋体"}

[[redirects]{lang="EN-US"}]{#struct_0_13325_x2064_829571754}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_1348527818}[输出的重定向报文数]{style="font-family:宋体"}

[[echo replies]{lang="EN-US"}]{#struct_0_13325_x2064_704838701}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x488643863}[输出的响应应答报文数]{style="font-family:宋体"}

[[parameter problem]{lang="EN-US"}]{#struct_0_13325_x2064_1933627539}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_829112999}[输出的参数错误报文数]{style="font-family:宋体"}

[[timestamp]{lang="EN-US"}]{#struct_0_13325_x2064_1297045737}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_859551359}[输出的时间戳报文数]{style="font-family:宋体"}

[[information requests]{lang="EN-US"}]{#struct_0_13325_x2064_x1333914600}

[[输入的信息请求报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1754321998}

[[mask requests]{lang="EN-US"}]{#struct_0_13325_x2064_829047463}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_48317501}[输出的掩码请求报文数]{style="font-family:宋体"}

[[mask replies]{lang="EN-US"}]{#struct_0_13325_x2064_x1465908032}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_1519470405}[输出的掩码应答报文数]{style="font-family:宋体"}

[[invalid type]{lang="EN-US"}]{#struct_0_13325_x2064_1690829984}

[[输入的非法类型报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_829244071}

[[router advert]{lang="EN-US"}]{#struct_0_13325_x2064_1087336915}

[[输入的路由器公告报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x351379252}

[[router solicit]{lang="EN-US"}]{#struct_0_13325_x2064_x1366875542}

[[输入的路由器请求报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x428322723}

[[broadcast/multicast echo requests ignored]{lang="EN-US"}]{#struct_0_13325_x2064_829178535}

[[输入的广播]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_1573965823}[组播响应请求丢弃报文数]{style="font-family:宋体"}

[[broadcast/multicast timestamp requests ignored]{lang="EN-US"}]{#struct_0_13325_x2064_x1451388494}

[[输入的广播]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x560006025}[组播时戳请求丢弃报文数]{style="font-family:宋体"}

[[information replies]{lang="EN-US"}]{#struct_0_13325_x2064_829375143}

[[输出的信息应答报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2047017579}

[[time exceeded]{lang="EN-US"}]{#struct_0_13325_x2064_1277159137}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_216341364}[输出的超时报文数]{style="font-family:宋体"}

[[bad address]{lang="EN-US"}]{#struct_0_13325_x2064_829309607}

[[输出的目的地址非法报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1071340399}

[[packet error]{lang="EN-US"}]{#struct_0_13325_x2064_x1268959965}

[[输出的错误报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1494346295}

[[router advert]{lang="EN-US"}]{#struct_0_13325_x2064_829506215}

[[输入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_980650245}[输出的路由器公告报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1605482474 .myid}
[]{#_Toc233688805}[]{#_Toc404786709}[]{#struct_0_13325_x2064_358373430}[]{#_Toc271702014}

**IP性能优化 \-- IP性能优化配置命令 \-- display ip statistics**

------------------------------------------------------------------------

[**[display ip statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x2126036610}[命令用来显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x739985855}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1484416021}

[**[display ip statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_829440679}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x1003726079}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x1679114631}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_1519450575}[模式：]{style="font-family:宋体"}

[**[display ip statistics]{lang="EN-US"}**[ \[ **chassis**]{lang="EN-US"}[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x652147553}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x306200125}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2050625346}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1724258591}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1778591502}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_829637287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1275890018}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_1069560830}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1985588440}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1410000355}[：显示指定]{style="font-family:宋体"}[单板]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1865939672}[：显示指定成员设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_801518045}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_826100788}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1472651568}[：显示指定单板的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_x507104479}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x361325158}

[**[display ip statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_1751082991}[命令用来显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息，包括接收报文、发送报文、分片、重组的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_829571751}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1348527821}[显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip statistics]{lang="EN-US"}]{#struct_0_13325_x2064_704379946}

[  Input:   sum            7120             local             112]{lang="EN-US"}

[           bad protocol   0                bad format        0]{lang="EN-US"}

[           bad checksum   0                bad options       0]{lang="EN-US"}

[  Output:  forwarding     0                local             27]{lang="EN-US"}

[           dropped        0                no route          2]{lang="EN-US"}

[           compress fails 0]{lang="EN-US"}

[  Fragment:input          0                output            0]{lang="EN-US"}

[           dropped        0]{lang="EN-US"}

[           fragmented     0                couldn\'t fragment 0]{lang="EN-US"}

[  Reassembling:sum        0                timeouts          0]{lang="EN-US"}

[]{#struct_0_13325_x2064_x521780488}[]{#_Toc138413617}[]{#_Toc138239196}[]{#_Toc68600617}[]{#_Toc58505326}[[表1-2 ]{lang="EN-US"}[display ip statistics]{lang="EN-US"}]{#_Toc43289060}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2050904340}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1327824510}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_829113000}

[[Input:]{lang="EN-US"}]{#struct_0_13325_x2064_x337612203}

[[sum]{lang="EN-US"}]{#struct_0_13325_x2064_x1810052085}

[[接收报文总数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2103193307}

[[local]{lang="EN-US"}]{#struct_0_13325_x2064_x2130991204}

[[接收的目的地址是本地的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x232967555}

[[bad protocol]{lang="EN-US"}]{#struct_0_13325_x2064_x1721137884}

[[未知协议的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_829047464}

[[bad format]{lang="EN-US"}]{#struct_0_13325_x2064_48317498}

[[格式错误的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1265644797}

[[bad checksum]{lang="EN-US"}]{#struct_0_13325_x2064_909518333}

[[校验和错误的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1236133692}

[[bad options]{lang="EN-US"}]{#struct_0_13325_x2064_899744520}

[[选项错误的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_829244072}

[[Output:]{lang="EN-US"}]{#struct_0_13325_x2064_1087336912}

[[forwarding]{lang="EN-US"}]{#struct_0_13325_x2064_x351838004}

[[转发的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_970627045}

[[local]{lang="EN-US"}]{#struct_0_13325_x2064_366297528}

[[本地发送报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_829178536}

[[dropped]{lang="EN-US"}]{#struct_0_13325_x2064_1573965822}

[[发送时丢弃的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1451454030}

[[no route]{lang="EN-US"}]{#struct_0_13325_x2064_x75546906}

[[查不到路由的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1513348405}

[[compress fails]{lang="EN-US"}]{#struct_0_13325_x2064_829375144}

[[压缩失败的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2047017580}

[[Fragment:]{lang="EN-US"}]{#struct_0_13325_x2064_x1808806546}

[[input]{lang="EN-US"}]{#struct_0_13325_x2064_1907242116}

[[接收的分片报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_829309608}

[[output]{lang="EN-US"}]{#struct_0_13325_x2064_1071340404}

[[发送的分片报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x78039766}

[[dropped]{lang="EN-US"}]{#struct_0_13325_x2064_x167533965}

[[丢弃的分片报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1229291784}

[[fragmented]{lang="EN-US"}]{#struct_0_13325_x2064_829506216}

[[分片成功的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_980650242}

[[couldn\'t fragment]{lang="EN-US"}]{#struct_0_13325_x2064_358373431}

[[分片失败的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2126036611}

[[Reassembling:]{lang="EN-US"}]{#struct_0_13325_x2064_829440680}

[[sum]{lang="EN-US"}]{#struct_0_13325_x2064_x959096056}

[[重组的报文总数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x803719682}

[[timeouts]{lang="EN-US"}]{#struct_0_13325_x2064_180751104}

[[重组超时的分片报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_829637288}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1275890025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip interface]{lang="EN-US"}**]{#struct_0_13325_x2064_1069364225}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[地址）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x807328163}

::: {#1206451099 .myid}
[]{#_Toc404786710}[]{#struct_0_13325_x2064_x1393706449}[]{#_Toc366483382}[]{#_Toc366483383}[]{#_Toc366483384}[]{#_Toc366483385}[]{#_Toc366483386}[]{#_Toc366483387}[]{#_Toc366483388}[]{#_Toc366483389}[]{#_Toc366483390}[]{#_Toc366483391}[]{#_Toc366483392}[]{#_Toc366483393}[]{#_Toc366483394}[]{#_Toc366483395}[]{#_Toc366483396}[]{#_Toc366483397}[]{#_Toc366483398}[]{#_Toc366483399}[]{#_Toc366483400}[]{#_Toc366483401}[]{#_Toc366483402}[]{#_Toc366483403}[]{#_Toc366483404}[]{#_Toc366483405}[]{#_Toc366483406}[]{#_Toc366483407}[]{#_Toc366483408}[]{#_Toc366483409}[]{#_Toc366483442}

**IP性能优化 \-- IP性能优化配置命令 \-- display rawip**

------------------------------------------------------------------------

[**[display rawip]{lang="EN-US"}**]{#struct_0_13325_x2064_707495242}[命令用来显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1930033758}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_333463910}

[**[display rawip]{lang="EN-US"}**]{#struct_0_13325_x2064_x1899377136}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_578041620}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display rawip]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_2145931303}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_770026151}[模式：]{style="font-family:宋体"}

[**[display rawip]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x1191674179}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x327481948}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1985120777}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1085497047}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_101697024}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x1899442672}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_284922716}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x1528565754}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1695990477}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_656234378}[：显示指定单板的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x61369476}[：显示指定成员设备的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x717511729}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1733076300}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x217621020}[：显示指定单板的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_x507563232}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1283927012}

[**[display rawip]{lang="EN-US"}**]{#struct_0_13325_x2064_x1776233443}[命令用来显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息，包括本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、使用]{style="font-family:宋体"}[RawIP socket]{lang="EN-US"}[的协议号等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1899246064}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1996455064}[显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display rawip]{lang="EN-US"}]{#struct_0_13325_x2064_x301287944}

[ Local Addr       Foreign Addr     Protocol  PCB]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0          1         0x0000000000000009]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0          1         0x0000000000000008]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0          1         0x0000000000000002]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x107327859}[显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display rawip]{lang="EN-US"}]{#struct_0_13325_x2064_1962036951}

[ Local Addr       Foreign Addr     Protocol  Slot  CPU PCB]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0          1         1     0   0x0000000000000009]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0          1         1     0   0x0000000000000008]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0          1         5     0   0x0000000000000002]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x829943951}[显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display rawip]{lang="EN-US"}]{#struct_0_13325_x2064_x1899311600}

[ Local Addr       Foreign Addr    Protocol Chassis Slot  CPU PCB]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0         1        1       1     0   0x0000000000000009]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0         1        1       1     0   0x0000000000000008]{lang="EN-US"}

[ 0.0.0.0          0.0.0.0         1        1       5     0   0x0000000000000002]{lang="EN-US"}

[[[表1-3 ]{lang="EN-US"}]{.FigureDescriptionChar}[display rawip]{lang="EN-US"}]{#struct_0_13325_x2064_x1470693675}[[命令显示信息描述表]{style="font-family:黑体"}]{.FigureDescriptionChar}

[]{#table_struct_0_x2056045360}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_1886152888}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_613649941}

[[Local Addr]{lang="EN-US"}]{#struct_0_13325_x2064_x560847024}

[[本端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_43536902}[地址]{style="font-family:宋体"}

[[Foreign Addr]{lang="EN-US"}]{#struct_0_13325_x2064_449582263}

[[对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x1899770351}[地址]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_13325_x2064_x591925237}

[[使用]{style="font-family:宋体"}[RawIP socket]{lang="EN-US"}]{#struct_0_13325_x2064_x709655461}[的协议号]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_13325_x2064_983840940}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x761109892}[中的成员编号]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_x402984838}

[[单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1899835887}

[[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_x507956448}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_946526968}[编号]{style="font-family:宋体"}

[[PCB]{lang="EN-US"}]{#struct_0_13325_x2064_898529874}

[[协议控制块索引]{style="font-family:宋体"}]{#struct_0_13325_x2064_2084432993}

[[ ]{lang="EN-US"}]{#_Toc233688806}

::: {#-318391958 .myid}
[]{#_Toc404786711}[]{#struct_0_13325_x2064_x2110553544}

**IP性能优化 \-- IP性能优化配置命令 \-- display rawip verbose**

------------------------------------------------------------------------

[**[display rawip verbose]{lang="EN-US"}**]{#struct_0_13325_x2064_181712738}[命令用来显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1446938215}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x838000117}

[**[display rawip verbose]{lang="EN-US"}**[ \[ **pcb** *pcb-index* \]]{lang="EN-US"}]{#struct_0_13325_x2064_x1899639279}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_111328934}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display rawip verbose]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_781399464}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_741326576}[模式：]{style="font-family:宋体"}

[**[display rawip verbose]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x833599180}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1630737081}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_453621488}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1218981365}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1227525989}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x1899704815}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1153750689}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_1403659432}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x217563880}

[**[pcb]{lang="EN-US"}**[ *pcb-index*]{lang="EN-US"}]{#struct_0_13325_x2064_x163547979}[：显示指定协议控制块索引的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[pcb-index]{lang="EN-US"}*[表示协议控制块索引，取值范围请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1790792037}[：显示指定单板的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1522954002}[：显示指定成员设备的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_801452509}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_916545612}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_883326001}[：显示指定单板的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_1058717322}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_853159060}

[**[display rawip verbose]{lang="EN-US"}**]{#struct_0_13325_x2064_x1899508207}[命令用来显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息，包括]{style="font-family:宋体"}[socket]{lang="EN-US"}[的创建者、状态、选项、类型、使用的协议号等，以及]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_705609677}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x773962490}[显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display rawip verbose]{lang="EN-US"}]{#struct_0_13325_x2064_x773896954}

[Total RawIP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Creator: ping\[320\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 3]{lang="EN-US"}

[ Protocol: 1]{lang="EN-US"}

[ Connection info: src = 0.0.0.0, dst = 0.0.0.0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x43073887}[显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display rawip verbose]{lang="EN-US"}]{#struct_0_13325_x2064_x773831418}

[Total RawIP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Slot: 6 Cpu: 0]{lang="EN-US"}

[ Creator: ping\[320\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 3]{lang="EN-US"}

[ Protocol: 1]{lang="EN-US"}

[ Connection info: src = 0.0.0.0, dst = 0.0.0.0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_976179178}[显示]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display rawip verbose]{lang="EN-US"}]{#struct_0_13325_x2064_x1899573743}

[Total RawIP socket number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Chassis: 2 Slot: 6 Cpu: 0]{lang="EN-US"}

[ Creator: ping\[320\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A]{lang="EN-US"}

[ Type: 3]{lang="EN-US"}

[ Protocol: 1]{lang="EN-US"}

[ Connection info: src = 0.0.0.0, dst = 0.0.0.0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display rawip verbose]{lang="EN-US"}]{#struct_0_13325_x2064_432724285}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2062091972}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1190262694}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_584157354}

[[Total RawIP socket number]{lang="EN-US"}]{#struct_0_13325_x2064_x1375551840}

[[RawIP socket]{lang="EN-US"}]{#struct_0_13325_x2064_1924344129}[总数]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_13325_x2064_x499303}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_1781524886}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_x1899377135}

[[单板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_2144125561}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_x774224634}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x1782000569}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Cpu]{lang="EN-US"}]{#struct_0_13325_x2064_1058913930}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_1569572376}[编号]{style="font-family:宋体"}

[[Creator]{lang="EN-US"}]{#struct_0_13325_x2064_x1568286435}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x635793026}[的任务名称，括号中为创建者的进程号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_13325_x2064_x216180914}

[[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x2083597797}[的状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOFDREF]{lang="EN-US"}]{#struct_0_13325_x2064_x1899442671}[：用户已经关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTED]{lang="EN-US"}]{#struct_0_13325_x2064_688207243}[：连接已经建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTING]{lang="EN-US"}]{#struct_0_13325_x2064_836858042}[：正在建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTING]{lang="EN-US"}]{#struct_0_13325_x2064_x1128633070}[：正在断开连接]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASYNC]{lang="EN-US"}]{#struct_0_13325_x2064_x1480280447}[：异步方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTED]{lang="EN-US"}]{#struct_0_13325_x2064_x1899246063}[：连接已经断开]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROTOREF]{lang="EN-US"}]{#struct_0_13325_x2064_x1895227705}[：协议强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1673489146}[：不处于上述状态]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_13325_x2064_x617407733}

[[socket]{lang="EN-US"}]{#struct_0_13325_x2064_1160922938}[的选项，有以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DEBUG]{lang="EN-US"}]{#struct_0_13325_x2064_x1899311599}[：记录套接字的调试信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_ACCEPTCONN]{lang="EN-US"}]{#struct_0_13325_x2064_901369499}[：]{lang="EN-US" style="font-family:宋体"}[server]{lang="EN-US"}[端监听连接请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEADDR]{lang="EN-US"}]{#struct_0_13325_x2064_249623790}[：允许本地地址重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVE]{lang="EN-US"}]{#struct_0_13325_x2064_x1226456955}[：协议需要查询空闲的连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DONTROUTE]{lang="EN-US"}]{#struct_0_13325_x2064_x1220387184}[：设置不查路由表（用于目的地址是直连网络的情况）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_BROADCAST]{lang="EN-US"}]{#struct_0_13325_x2064_x1899770354}[：套接字支持广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_LINGER]{lang="EN-US"}]{#struct_0_13325_x2064_x995209764}[：套接字关闭但仍发送剩余数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_OOBINLINE]{lang="EN-US"}]{#struct_0_13325_x2064_641469450}[：带外数据采用内联方式存储]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEPORT]{lang="EN-US"}]{#struct_0_13325_x2064_2124265702}[：允许本地端口重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMP]{lang="EN-US"}]{#struct_0_13325_x2064_x1899835890}[：记录入报文时间戳，只对非连接的协议有效，时间精确到毫秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_NOSIGPIPE]{lang="EN-US"}]{#struct_0_13325_x2064_x667488531}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[不能发送数据导致返回失败时不创建]{lang="EN-US" style="font-family:宋体"}[SIGPIPE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_FILTER]{lang="EN-US"}]{#struct_0_13325_x2064_309506619}[：]{style="font-family:宋体"}[设置报文过滤条件]{lang="EN-US" style="font-family:宋体"}[，对接收报文有效]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMPNS]{lang="EN-US"}]{#struct_0_13325_x2064_578452590}[：和时]{lang="EN-US" style="font-family:宋体"}[间]{style="font-family:宋体"}[戳选项功能类似，时间可以精确到纳秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x827281959}[：没有设置选项]{lang="EN-US" style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_13325_x2064_x1103661748}

[[影响]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x1899639282}[连接的错误码]{style="font-family:宋体"}

[[Receiving buffer (cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_13325_x2064_x1099507687}

[[接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态，状态的取值有：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x485801695}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_13325_x2064_x1671513584}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_13325_x2064_x1899704818}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_13325_x2064_1557035216}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_141680138}[：不处于上述状态]{style="font-family:宋体"}

[[Sending buffer (cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_13325_x2064_1265340298}

[[发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态，状态的取值有：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1899508210}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_13325_x2064_302259614}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_13325_x2064_597574281}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_13325_x2064_x1899573746}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_29439758}[：不处于上述状态]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_13325_x2064_x1578183202}

[[使用的]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x98743683}[类型，类型的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13325_x2064_x1899377138}[：]{style="font-family:宋体"}[SOCK_STREAM]{lang="EN-US"}[，]{style="font-family:宋体"}[流模式，提供可靠的字节流。]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[协议使用此类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13325_x2064_1740841034}[：]{style="font-family:宋体"}[SOCK_DGRAM]{lang="EN-US"}[，数据报模式的通信。]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议使用此类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13325_x2064_972404587}[：]{lang="EN-US" style="font-family:宋体"}[SOCK_RAW]{lang="EN-US"}[，]{style="font-family:宋体"}[RAW]{lang="EN-US"}[模式的通信方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x1899442674}[：不是上述类型]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_13325_x2064_1447722130}

[[使用]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_980965954}[的协议号]{style="font-family:宋体"}

[[Connection info]{lang="EN-US"}]{#struct_0_13325_x2064_x1899246066}

[[连接信息，分别为源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x1135712818}[地址、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Inpcb flags]{lang="EN-US"}]{#struct_0_13325_x2064_x641373516}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_x1899311602}[协议控制块中的标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVOPTS]{lang="EN-US"}]{#struct_0_13325_x2064_1661474207}[：接收传入的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVRETOPTS]{lang="EN-US"}]{#struct_0_13325_x2064_1682187699}[：接收回应的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVDSTADDR]{lang="EN-US"}]{#struct_0_13325_x2064_1038538010}[：接收目的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_HDRINCL]{lang="EN-US"}]{#struct_0_13325_x2064_x1899770353}[：用户提供整个]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEADDR]{lang="EN-US"}]{#struct_0_13325_x2064_570874177}[：重复使用地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEPORT]{lang="EN-US"}]{#struct_0_13325_x2064_x168261592}[：重复使用端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ANONPORT]{lang="EN-US"}]{#struct_0_13325_x2064_x1899835889}[：]{lang="EN-US" style="font-family:宋体"}[用户未指定端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVIF]{lang="EN-US"}]{#struct_0_13325_x2064_1705098928}[：接收报文时记录报文的入接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVTTL]{lang="EN-US"}]{#struct_0_13325_x2064_929745091}[：携带报文的]{lang="EN-US" style="font-family:宋体"}[TTL]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_DONTFRAG]{lang="EN-US"}]{#struct_0_13325_x2064_x1899639281}[：设置不可分片标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ROUTER_ALERT]{lang="EN-US"}]{#struct_0_13325_x2064_466576254}[：接收携带路由器告警选项的报文]{lang="EN-US" style="font-family:
  宋体"}[，仅]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_PROTOCOL_PACKET]{lang="EN-US"}]{#struct_0_13325_x2064_x1899704817}[：标识报文为协议报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVVLANID]{lang="EN-US"}]{#struct_0_13325_x2064_x1978417193}[：接收报文的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVMACADDR]{lang="EN-US"}]{#struct_0_13325_x2064_1428158366}[：接收报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SNDBYLSPV]{lang="EN-US"}]{#struct_0_13325_x2064_x1899508209}[：通过]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVTOS]{lang="EN-US"}]{#struct_0_13325_x2064_1512178731}[：]{style="font-family:宋体"}[携带报文的]{lang="EN-US" style="font-family:宋体"}[TOS]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_USEICMPSRC]{lang="EN-US"}]{#struct_0_13325_x2064_x1444828706}[：使用配置的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[地址作为源地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SYNCPCB]{lang="EN-US"}]{#struct_0_13325_x2064_x1899573745}[：阻塞等待]{style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1595523699}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb extflag]{lang="EN-US"}]{#struct_0_13325_x2064_x1942388726}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_1568287155}[协议控制块中的扩展标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_EXTRCVPVCIDX]{lang="EN-US"}]{#struct_0_13325_x2064_x1942388725}[：接收报文时记录报文的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVPWID]{lang="EN-US"}]{#struct_0_13325_x2064_1165002628}[：接收报文时记录报文的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_2026650884}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb vflag]{lang="EN-US"}]{#struct_0_13325_x2064_x1899377137}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_x988042321}[协议控制块中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[版本标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_IPV4]{lang="EN-US"}]{#struct_0_13325_x2064_187914962}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_TIMEWAIT]{lang="EN-US"}]{#struct_0_13325_x2064_x1899442673}[：处于等待状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_ONESBCAST]{lang="EN-US"}]{#struct_0_13325_x2064_1851006657}[：发送广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DROPPED]{lang="EN-US"}]{#struct_0_13325_x2064_x1899246065}[：协议丢弃标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_SOCKREF]{lang="EN-US"}]{#struct_0_13325_x2064_x732428291}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INP_DONTBLOCK]{lang="EN-US"}]{#struct_0_13325_x2064_840271731}[：]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步时不能被阻塞]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x1899311601}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_13325_x2064_1258189680}[(minimum TTL)]{lang="SV"}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_x1899770356}[协议控制块中的生存周期，括号中为最小生存周期]{style="font-family:宋体"}

[[Send VRF]{lang="EN-US"}]{#struct_0_13325_x2064_167589650}

[[发送实例]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1595936864}

[[Receive VRF]{lang="EN-US"}]{#struct_0_13325_x2064_x1899835892}

[[接收实例]{style="font-family:宋体"}]{#struct_0_13325_x2064_495310883}

[ ]{lang="EN-US"}

::: {#-773351221 .myid}
[]{#_Toc138239302}[]{#_Toc136679740}[]{#_Toc69790798}[]{#_Toc35059147}[]{#_Toc404786712}[]{#struct_0_13325_x2064_361346182}[]{#_Toc233688807}

**IP性能优化 \-- IP性能优化配置命令 \-- display tcp**

------------------------------------------------------------------------

[**[display tcp]{lang="EN-US"}**]{#struct_0_13325_x2064_x1899639284}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x292938633}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1593278031}

[**[display tcp]{lang="EN-US"}**]{#struct_0_13325_x2064_1688682113}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x160657926}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display tcp]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_1114264001}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x889333805}[模式：]{style="font-family:宋体"}

[**[display tcp]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x802500626}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x164433599}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1899704820}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1913200040}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_2095973739}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x465441521}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_805148129}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x1389114988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1851488751}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x874198688}[：显示指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_991780124}[：显示指定成员设备的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x764696968}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1899508212}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1607956027}[：显示指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_1058913929}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1465059028}

[**[display tcp]{lang="EN-US"}**]{#struct_0_13325_x2064_2020418449}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息，包括本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号、对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的状态等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1238709065}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x324114746}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display tcp]{lang="EN-US"}]{#struct_0_13325_x2064_x256102811}

[ \*: TCP MD5 Connection]{lang="EN-US"}

[ Local Addr:port       Foreign Addr:port     State       PCB]{lang="EN-US"}

[\*0.0.0.0:21            0.0.0.0:0             LISTEN      0x000000000000c387]{lang="EN-US"}

[ 192.168.20.200:23     192.168.20.14:1284    ESTABLISHED 0x0000000000000009]{lang="EN-US"}

[ 192.168.20.200:23     192.168.20.14:1283    ESTABLISHED 0x0000000000000002]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1837758255}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display tcp]{lang="EN-US"}]{#struct_0_13325_x2064_x1899573748}

[ \*: TCP MD5 Connection]{lang="EN-US"}

[ Local Addr:port       Foreign Addr:port     State       Slot  CPU PCB]{lang="EN-US"}

[\*0.0.0.0:21            0.0.0.0:0             LISTEN      1     0   0x000000000000c387]{lang="EN-US"}

[ 192.168.20.200:23     192.168.20.14:1284    ESTABLISHED 1     0   0x0000000000000009]{lang="EN-US"}

[ 192.168.20.200:23     192.168.20.14:1283    ESTABLISHED 1     0   0x0000000000000002]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1192239172}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display tcp]{lang="EN-US"}]{#struct_0_13325_x2064_x1672855683}

[ \*: TCP MD5 Connection]{lang="EN-US"}

[ Local Addr:port       Foreign Addr:port     State       Chassis Slot  CPU PCB]{lang="EN-US"}

[\*0.0.0.0:21            0.0.0.0:0             LISTEN      1       1     0   0x00000000]{lang="EN-US"}

[ 0000c387]{lang="EN-US"}

[ 192.168.20.200:23     192.168.20.14:1284    ESTABLISHED 1       1     0   0x00000000]{lang="EN-US"}

[ 00000009]{lang="EN-US"}

[ 192.168.20.200:23     192.168.20.14:1283    ESTABLISHED 1       1     0   0x00000000]{lang="EN-US"}

[ 00000002]{lang="EN-US"}

[[[表1-5 ]{lang="EN-US"}]{.FigureDescriptionChar}[display tcp]{lang="EN-US"}]{#struct_0_13325_x2064_816082570}[[命令显示信息描述表]{style="font-family:黑体"}]{.FigureDescriptionChar}

[]{#table_struct_0_x2036432656}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_350139748}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1899377140}

[[\*]{lang="EN-US"}]{#struct_0_13325_x2064_1385069426}

[[如果某个连接前有此标识，则表示该]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_1822639927}[连接是采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[加密算法认证的连接]{style="font-family:宋体"}

[[Local Addr:port]{lang="EN-US"}]{#struct_0_13325_x2064_x462861041}

[[本端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_1323013727}[地址及端口号]{style="font-family:宋体"}

[[Foreign Addr:port]{lang="EN-US"}]{#struct_0_13325_x2064_1800049075}

[[对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x1899442676}[地址及端口号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_13325_x2064_x1684445752}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_x598736528}[连接状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_13325_x2064_x1635774597}[：服务器收到客户端的关闭连接请求回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_13325_x2064_1570567081}[：服务器在等待连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_SENT]{lang="EN-US"}]{#struct_0_13325_x2064_188840818}[：客户端发出连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_RCVD]{lang="EN-US"}]{#struct_0_13325_x2064_x1899246068}[：服务器收到客户端连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_13325_x2064_27086596}[：服务器和客户端双方建立连接并能进行双向数据传递的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE_WAIT]{lang="EN-US"}]{#struct_0_13325_x2064_x1923011263}[：服务器收到客户端关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_1]{lang="EN-US"}]{#struct_0_13325_x2064_x1796904105}[：客户端发出关闭连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSING]{lang="EN-US"}]{#struct_0_13325_x2064_1834579392}[：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAST_ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x1899311604}[：服务器向客户端发出关闭连接请求等待回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_2]{lang="EN-US"}]{#struct_0_13325_x2064_498674793}[：客户端收到服务器关闭连接回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIME_WAIT]{lang="EN-US"}]{#struct_0_13325_x2064_x796671838}[：客户端收到服务器的关闭连接请求后所处的状态]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_13325_x2064_x797920822}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_1492002443}[中的成员编号]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_x1899770355}

[[单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_13325_x2064_1733673591}

[[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_1058651784}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_1058717320}[编号]{style="font-family:宋体"}

[[PCB]{lang="EN-US"}]{#struct_0_13325_x2064_2027587964}

[[协议控制块索引]{style="font-family:宋体"}]{#struct_0_13325_x2064_1499312873}

[ ]{lang="EN-US"}

::::: {#1500793178 .myid}
[]{#_Toc404786713}[]{#struct_0_13325_x2064_1146248637}

**IP性能优化 \-- IP性能优化配置命令 \-- display tcp-proxy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化命令.files/image001.png){width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_13325_x2064_977725677}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_13325_x2064_x1132296024}
:::

[ ]{lang="EN-US"}

[**[display tcp-proxy]{lang="EN-US"}**]{#struct_0_13325_x2064_x677891395}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x101675408}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_13449387}

[**[display tcp-proxy]{lang="EN-US"}**]{#struct_0_13325_x2064_2089343210}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_1839003058}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display tcp-proxy slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_13325_x2064_1591511481}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_101507958}[模式：]{style="font-family:宋体"}

[**[display tcp-proxy chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_13325_x2064_1596587331}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_457231525}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x342196814}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1939450582}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x829526721}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x2035083263}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_2036945637}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_1657913415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_989382167}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x776000128}[：显示指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1878916708}[：显示指定成员设备的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1007038790}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x614285958}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1247752136}[：显示指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_1116953154}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x216226254}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_x1326138580}[代理是一种与传统定义的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[相比更快速更灵活的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[实现。用于支持负载分担或]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[业务。能够提供比普通]{style="font-family:宋体"}[TCP]{lang="EN-US"}[传输更灵活的控制，从而达到传输优化的目的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1301945116}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1246909376}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display tcp-proxy]{lang="EN-US"}]{#struct_0_13325_x2064_1952883227}

[Local Addr:port       Foreign Addr:port     State        Service type]{lang="EN-US"}

[192.168.56.25:1111    111.111.111.125:8080  ESTABLISHED  WAAS]{lang="EN-US"}

[111.111.111.125:8080  192.168.56.25:1111    ESTABLISHED  WAAS]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display tcp-proxy]{lang="EN-US"}]{#struct_0_13325_x2064_1550435898}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x971310129}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_1703206286}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_648678745}

[[Local Addr:port]{lang="EN-US"}]{#struct_0_13325_x2064_x1427392846}

[[本端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_386799286}[地址及端口号]{style="font-family:宋体"}

[[Foreign Addr:port]{lang="EN-US"}]{#struct_0_13325_x2064_x889834657}

[[对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x1179284655}[地址及端口号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_13325_x2064_1922700537}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_1299854210}[代理连接状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_13325_x2064_x537253360}[：服务器收到客户端的关闭连接请求回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_13325_x2064_1549598700}[：服务器在等待连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_SENT]{lang="EN-US"}]{#struct_0_13325_x2064_x1806243830}[：客户端发出连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_RECEIVED]{lang="EN-US"}]{#struct_0_13325_x2064_432581137}[：服务器收到客户端连接请求时所处的状态]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_13325_x2064_x16485241}[：服务器和客户端双方建立连接并能进行双向数据传递的状态]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE_WAIT]{lang="EN-US"}]{#struct_0_13325_x2064_846859005}[：服务器收到客户端关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_1]{lang="EN-US"}]{#struct_0_13325_x2064_x294753013}[：客户端发出关闭连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CLOSING]{lang="EN-US"}]{#struct_0_13325_x2064_x196884360}[：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAST_ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x1582569182}[：服务器向客户端发出关闭连接请求等待回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_2]{lang="EN-US"}]{#struct_0_13325_x2064_x1960936117}[：客户端收到服务器关闭连接回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIME_WAIT]{lang="EN-US"}]{#struct_0_13325_x2064_x148183488}[：]{style="font-family:宋体"}[客户端收到服务器的关闭连接请求后所处的状态]{style="font-family:宋体"}

[[Service type]{lang="EN-US"}]{#struct_0_13325_x2064_866163752}

[[服务类型，可能的取值如下：]{style="font-family:宋体"}]{#struct_0_13325_x2064_1146314173}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LB]{lang="EN-US"}]{#struct_0_13325_x2064_x509775476}[：负载均衡服务]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAAS]{lang="EN-US"}]{#struct_0_13325_x2064_1146304652}[：]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[服务]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSL VPN]{lang="EN-US"}]{#struct_0_13325_x2064_x1132230488}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[服务]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1995210496 .myid}
[]{#_Toc404786714}[]{#struct_0_13325_x2064_1282437017}

**IP性能优化 \-- IP性能优化配置命令 \-- display tcp statistics**

------------------------------------------------------------------------

[**[display tcp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_1732760766}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的流量统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1899835891}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_2061394824}

[**[display tcp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_168237334}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_1852441341}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display tcp statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_942583790}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x2100896299}[模式：]{style="font-family:宋体"}

[**[display tcp statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x669783178}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1893695288}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x197478844}[]{#_Hlt24185450}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1557496145}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1899639283}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_1629375668}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_960812595}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_761497820}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_851743071}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1636032952}[：显示指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x680451975}[：显示指定成员设备的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_2011240554}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_830716299}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1569720225}[：显示指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_1058782856}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接流量统计信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1899704819}

[**[display tcp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x1171848139}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的流量统计信息，包括接收报文、发送报文以及]{style="font-family:宋体"}[Syncache/syncookie]{lang="EN-US"}[等相关统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1466424896}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_566877328}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display tcp statistics]{lang="EN-US"}]{#struct_0_13325_x2064_x1899573747}

[Received packets:]{lang="EN-US"}

[    Total: 4150 ]{lang="EN-US"}

[    packets in sequence: 1366 (134675 bytes)]{lang="EN-US"}

[    window probe packets: 0, window update packets: 0]{lang="EN-US"}

[    checksum error: 0, offset error: 0, short error: 0]{lang="EN-US"}

[    packets dropped for lack of memory: 0]{lang="EN-US"}

[    packets dropped due to PAWS: 0]{lang="EN-US"}

[    duplicate packets: 12 (36 bytes), partially duplicate packets: 0 (0 bytes)]{lang="EN-US"}

[    out-of-order packets: 0 (0 bytes)]{lang="EN-US"}

[    packets with data after window: 0 (0 bytes)]{lang="EN-US"}

[    packets after close: 0]{lang="EN-US"}

[    ACK packets: 3531 (795048 bytes)]{lang="EN-US"}

[    duplicate ACK packets: 33, ACK packets for unsent data: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[    Total: 4058]{lang="EN-US"}

[    urgent packets: 0]{lang="EN-US"}

[    control packets: 50]{lang="EN-US"}

[    window probe packets: 3, window update packets: 11]{lang="EN-US"}

[    data packets: 3862 (795012 bytes), data packets retransmitted: 0 (0 bytes)]{lang="EN-US"}

[    ACK-only packets: 150 (52 delayed)]{lang="EN-US"}

[    unnecessary packet retransmissions: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Syncache/syncookie related statistics:]{lang="EN-US"}

[    entries added to syncache: 12]{lang="EN-US"}

[    syncache entries retransmitted: 0]{lang="EN-US"}

[    duplicate SYN packets: 0]{lang="EN-US"}

[    reply failures: 0]{lang="EN-US"}

[    successfully build new socket: 12]{lang="EN-US"}

[    bucket overflows: 0]{lang="EN-US"}

[    zone failures: 0]{lang="EN-US"}

[    syncache entries removed due to RST: 0]{lang="EN-US"}

[    syncache entries removed due to timed out: 0]{lang="EN-US"}

[    ACK checked by syncache or syncookie failures: 0]{lang="EN-US"}

[    syncache entries aborted: 0]{lang="EN-US"}

[    syncache entries removed due to bad ACK: 0]{lang="EN-US"}

[    syncache entries removed due to ICMP unreachable: 0]{lang="EN-US"}

[    SYN cookies sent: 0]{lang="EN-US"}

[    SYN cookies received: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[SACK related statistics:]{lang="EN-US"}

[    SACK recoveries: 1]{lang="EN-US"}

[    SACK retransmitted segments: 0 (0 bytes)]{lang="EN-US"}

[    SACK blocks (options) received: 0]{lang="EN-US"}

[    SACK blocks (options) sent: 0]{lang="EN-US"}

[    SACK scoreboard overflows: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Other statistics:]{lang="EN-US"}

[    retransmitted timeout: 0, connections dropped in retransmitted timeout: 0]{lang="EN-US"}

[    persist timeout: 0]{lang="EN-US"}

[    keepalive timeout: 21, keepalive probe: 0]{lang="EN-US"}

[    keepalive timeout, so connections disconnected: 0]{lang="EN-US"}

[    fin_wait_2 timeout, so connections disconnected: 0]{lang="EN-US"}

[    initiated connections: 29, accepted connections: 12, established connections:]{lang="EN-US"}

[23]{lang="EN-US"}

[    closed connections: 50051 (dropped: 0, initiated dropped: 0)]{lang="EN-US"}

[    bad connection attempt: 0]{lang="EN-US"}

[    ignored RSTs in the window: 0]{lang="EN-US"}

[    listen queue overflows: 0]{lang="EN-US"}

[    RTT updates: 3518(attempt segment: 3537)]{lang="EN-US"}

[    correct ACK header predictions: 0]{lang="EN-US"}

[    correct data packet header predictions: 568]{lang="EN-US"}

[    resends due to MTU discovery: 0]{lang="EN-US"}

[    packets dropped with MD5 authentication: 0]{lang="EN-US"}

[    packets permitted with MD5 authentication: 0]{lang="EN-US"}

[]{#struct_0_13325_x2064_x1536644183}[]{#_Toc138413618}[[表1-7 ]{lang="EN-US"}[display tcp statistics]{lang="EN-US"}]{#_Toc138239197}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2035706392}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_186069076}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_317281156}

[[Received packets:]{lang="EN-US"}]{#struct_0_13325_x2064_x1190676868}

[[Total]{lang="EN-US"}]{#struct_0_13325_x2064_x1899377139}

[[接收的报文总数]{style="font-family:宋体"}]{#struct_0_13325_x2064_174757093}

[[packets in sequence]{lang="EN-US"}]{#struct_0_13325_x2064_x988331213}

[[按顺序到达的报文数，括号中为字节数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1753594149}

[[window probe packets]{lang="EN-US"}]{#struct_0_13325_x2064_248730109}

[[接收的窗口探测报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1741414128}

[[window update packets]{lang="EN-US"}]{#struct_0_13325_x2064_x1339199257}

[[接收的窗口更新报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1899442675}

[[checksum error]{lang="EN-US"}]{#struct_0_13325_x2064_x1281161225}

[[接收的校验和错误报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1572165063}

[[offset error]{lang="EN-US"}]{#struct_0_13325_x2064_x706047298}

[[接收的偏移量错误报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x409186745}

[[short error]{lang="EN-US"}]{#struct_0_13325_x2064_x227616239}

[[接收的报文长度太短的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1899246067}

[[packets dropped for lack of memory]{lang="EN-US"}]{#struct_0_13325_x2064_430371123}

[[由于内存不足而被丢弃的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1799912476}

[[packets dropped due to PAWS]{lang="EN-US"}]{#struct_0_13325_x2064_487119788}

[[由于]{style="font-family:宋体"}[PAWS]{lang="EN-US"}]{#struct_0_13325_x2064_443770546}[（防止序号回绕）而被丢弃的报文数]{style="font-family:宋体"}

[[duplicate packets]{lang="EN-US"}]{#struct_0_13325_x2064_x1899311603}

[[接收的完全重复报文数，括号中为字节数]{style="font-family:宋体"}]{#struct_0_13325_x2064_95390266}

[[partially duplicate packets]{lang="EN-US"}]{#struct_0_13325_x2064_699145488}

[[接收的部分重复报文数，括号中为字节数]{style="font-family:宋体"}]{#struct_0_13325_x2064_876023064}

[[out-of-order packets]{lang="EN-US"}]{#struct_0_13325_x2064_1107914138}

[[接收的顺序错乱的报文数，括号中为字节数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x333686411}

[[packets with data after window]{lang="EN-US"}]{#struct_0_13325_x2064_760084894}

[[落在接收窗口外的报文数，括号中为字节数]{style="font-family:宋体"}]{#struct_0_13325_x2064_197374023}

[[packets after close]{lang="EN-US"}]{#struct_0_13325_x2064_861156521}

[[在连接关闭后到达的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x333751947}

[[ACK packets]{lang="EN-US"}]{#struct_0_13325_x2064_x1124110825}

[[接收的]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x2122809612}[确认报文数，括号中为字节数]{style="font-family:宋体"}

[[duplicate ACK packets]{lang="EN-US"}]{#struct_0_13325_x2064_x228999856}

[[接收的重复的]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x333555339}[确认报文数]{style="font-family:宋体"}

[[ACK packets for unsent data]{lang="EN-US"}]{#struct_0_13325_x2064_1991613292}

[[接收的确认未发送数据的]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_13325_x2064_875231905}[报文数]{style="font-family:宋体"}

[[Sent packets:]{lang="EN-US"}]{#struct_0_13325_x2064_1740664636}

[[Total]{lang="EN-US"}]{#struct_0_13325_x2064_x333620875}

[[发送的报文总数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x358423850}

[[urgent packets]{lang="EN-US"}]{#struct_0_13325_x2064_x1123904325}

[[发送的紧急数据报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_862210303}

[[control packets]{lang="EN-US"}]{#struct_0_13325_x2064_x333424267}

[[发送的控制报文数，括号中为包含的重传数据报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1537142739}

[[window probe packets]{lang="EN-US"}]{#struct_0_13325_x2064_x1787969981}

[[发送的窗口探测报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1450521113}

[[window update packets]{lang="EN-US"}]{#struct_0_13325_x2064_x333489803}

[[发送的窗口更新报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1551307472}

[[data packets]{lang="EN-US"}]{#struct_0_13325_x2064_2090464503}

[[发送的数据报文数，括号中为字节数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x333293195}

[[data packets retransmitted]{lang="EN-US"}]{#struct_0_13325_x2064_1543788163}

[[重发的数据报文数，括号中为字节数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1735321670}

[[ACK-only packets]{lang="EN-US"}]{#struct_0_13325_x2064_x333358731}

[[发送的]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x422410483}[报文数，括号中为延迟]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[unnecessary packet retransmissions]{lang="EN-US"}]{#struct_0_13325_x2064_x1611988640}

[[报文非必要重传次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x281900460}

[[Syncache/syncookie related statistics:]{lang="EN-US"}]{#struct_0_13325_x2064_x333162123}

[[entries added to syncache]{lang="EN-US"}]{#struct_0_13325_x2064_3853124}

[[添加的]{style="font-family:宋体"}[syncache]{lang="EN-US"}]{#struct_0_13325_x2064_1591362215}[对象数]{style="font-family:宋体"}

[[syncache entries  retransmitted]{lang="EN-US"}]{#struct_0_13325_x2064_x333227659}

[[重传的]{style="font-family:宋体"}[syncache]{lang="EN-US"}]{#struct_0_13325_x2064_1957331995}[对象数]{style="font-family:宋体"}

[[duplicate SYN packets]{lang="EN-US"}]{#struct_0_13325_x2064_x1464749934}

[[重复的]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_13325_x2064_x333686410}[报文数]{style="font-family:宋体"}

[[reply failures]{lang="EN-US"}]{#struct_0_13325_x2064_760019358}

[[回复失败的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2146855503}

[[successfully build new socket]{lang="EN-US"}]{#struct_0_13325_x2064_x333751946}

[[创建子]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x1124045289}[成功数]{style="font-family:宋体"}

[[bucket overflows]{lang="EN-US"}]{#struct_0_13325_x2064_x333555338}

[[bucket]{lang="EN-US"}]{#struct_0_13325_x2064_1991678828}[溢出次数]{style="font-family:宋体"}

[[zone failures]{lang="EN-US"}]{#struct_0_13325_x2064_x1798851695}

[[内存分配失败次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x333620874}

[[syncache entries removed due to RST]{lang="EN-US"}]{#struct_0_13325_x2064_x358489386}

[[由于收到]{style="font-family:宋体"}[RST]{lang="EN-US"}]{#struct_0_13325_x2064_809509582}[（复位连接）报文段而删除的]{style="font-family:宋体"}[syncache]{lang="EN-US"}[对象个数]{style="font-family:宋体"}

[[syncache entries removed due to timed out]{lang="EN-US"}]{#struct_0_13325_x2064_x333424266}

[[定时器超时且重传次数超过限制时]{style="font-family:宋体"}[syncache]{lang="EN-US"}]{#struct_0_13325_x2064_x1537208275}[对象删除数]{style="font-family:宋体"}

[[ACK checked by syncache or syncookie failures]{lang="EN-US"}]{#struct_0_13325_x2064_430640070}

[[接收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x333489802}[报文时查找]{style="font-family:宋体"}[syncache]{lang="EN-US"}[处理失败数]{style="font-family:宋体"}

[[syncache entries aborted]{lang="EN-US"}]{#struct_0_13325_x2064_1551241936}

[[创建子]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x333293194}[失败数]{style="font-family:宋体"}

[[syncache entries removed due to bad ACK]{lang="EN-US"}]{#struct_0_13325_x2064_1543853699}

[[由于]{style="font-family:宋体"}[bad ACK]{lang="EN-US"}]{#struct_0_13325_x2064_1396559419}[而删除的]{style="font-family:宋体"}[syncache]{lang="EN-US"}[对象数]{style="font-family:宋体"}

[[syncache entries removed due to ICMP unreachable]{lang="EN-US"}]{#struct_0_13325_x2064_x333358730}

[[由于接收到]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_x422344947}[差错报文导致删除的]{style="font-family:宋体"}[syncache]{lang="EN-US"}[对象数]{style="font-family:宋体"}

[[SYN cookies sent]{lang="EN-US"}]{#struct_0_13325_x2064_1941909135}

[[SYN cookie]{lang="EN-US"}]{#struct_0_13325_x2064_x333162122}[发送数]{style="font-family:宋体"}

[[SYN cookies received]{lang="EN-US"}]{#struct_0_13325_x2064_3787588}

[[SYN cookie]{lang="EN-US"}]{#struct_0_13325_x2064_x333227658}[接收数]{style="font-family:宋体"}

[[SACK related statistics]{lang="EN-US"}]{#struct_0_13325_x2064_1957266459}

[[SACK recoveries]{lang="EN-US"}]{#struct_0_13325_x2064_2105043380}

[[通过]{style="font-family:宋体"}[SACK]{lang="EN-US"}]{#struct_0_13325_x2064_x333686413}[进行恢复的次数]{style="font-family:宋体"}

[[SACK retransmitted segments]{lang="EN-US"}]{#struct_0_13325_x2064_760215966}

[[通过]{style="font-family:宋体"}[SACK]{lang="EN-US"}]{#struct_0_13325_x2064_x333751949}[进行重传的报文段个数，括号中为字节数]{style="font-family:宋体"}

[[SACK blocks (options) received]{lang="EN-US"}]{#struct_0_13325_x2064_x1124766185}

[[接收到的带选择性]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x333555341}[选项的报文数]{style="font-family:宋体"}

[[SACK blocks (options) sent]{lang="EN-US"}]{#struct_0_13325_x2064_1992137585}

[[发送的带选择性]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x414331615}[选项的报文数]{style="font-family:宋体"}

[[SACK scoreboard overflows]{lang="EN-US"}]{#struct_0_13325_x2064_x333620877}

[[本地维护的对端缺失报文段记录队列溢出次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x358554922}

[[Other statistics]{lang="EN-US"}]{#struct_0_13325_x2064_x333424269}

[[retransmitted timeout]{lang="EN-US"}]{#struct_0_13325_x2064_x1536225235}

[[重传定时器超时次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x333489805}

[[connections dropped in retransmitted timeout]{lang="EN-US"}]{#struct_0_13325_x2064_1551438544}

[[重传次数超过限制而丢弃的连接数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x333293197}

[[persist timeout]{lang="EN-US"}]{#struct_0_13325_x2064_1543657091}

[[持续定时器超时次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1310851947}

[[keepalive timeout]{lang="EN-US"}]{#struct_0_13325_x2064_x333358733}

[[存活定时器超时次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x422541555}

[[keepalive probe]{lang="EN-US"}]{#struct_0_13325_x2064_x333162125}

[[发送的存活探测报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_4246340}

[[keepalive timeout, so connections disconnected]{lang="EN-US"}]{#struct_0_13325_x2064_x333227661}

[[存活定时器超时而中断的连接数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1956807706}

[[fin_wait_2 timeout, so connections disconnected]{lang="EN-US"}]{#struct_0_13325_x2064_x333686412}

[[Fin wait 2]{lang="EN-US"}]{#struct_0_13325_x2064_760150430}[定时器超时而中断的连接数]{style="font-family:宋体"}

[[initiated connections]{lang="EN-US"}]{#struct_0_13325_x2064_x333751948}

[[发起连接次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1124700649}

[[accepted connections]{lang="EN-US"}]{#struct_0_13325_x2064_x333555340}

[[接受连接次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1992203121}

[[established connections]{lang="EN-US"}]{#struct_0_13325_x2064_x333620876}

[[已建立连接数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x358620458}

[[closed connections(dropped: 0, initiated dropped: 0)]{lang="EN-US"}]{#struct_0_13325_x2064_x333424268}

[[已关闭连接数目，括号中为意外丢弃连接数（收到对端]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_13325_x2064_x1536290771}[之后）、主动连接失败数（收到对端]{style="font-family:宋体"}[SYN]{lang="EN-US"}[之前）]{style="font-family:宋体"}

[[bad connection attempt]{lang="EN-US"}]{#struct_0_13325_x2064_x333489804}

[[接收到的错误连接报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1551373008}

[[ignored RSTs in the window]{lang="EN-US"}]{#struct_0_13325_x2064_x333293196}

[[窗口中忽略的]{style="font-family:宋体"}[RST]{lang="EN-US"}]{#struct_0_13325_x2064_1543722627}[报文数]{style="font-family:宋体"}

[[listen queue overflows]{lang="EN-US"}]{#struct_0_13325_x2064_x333358732}

[[监听队列溢出次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x422476019}

[[RTT updates(attempt segment)]{lang="EN-US"}]{#struct_0_13325_x2064_x333162124}

[[RTT]{lang="EN-US"}]{#struct_0_13325_x2064_4180804}[更新次数，括号中为发送的报文数]{style="font-family:宋体"}

[[correct ACK header predictions]{lang="EN-US"}]{#struct_0_13325_x2064_x333227660}

[[ACK]{lang="EN-US"}]{#struct_0_13325_x2064_x333686415}[通过首部预测算法的次数]{style="font-family:宋体"}

[[correct data packet header predictions]{lang="EN-US"}]{#struct_0_13325_x2064_760347038}

[[数据报文通过首部预测算法的次数]{style="font-family:宋体"}]{#struct_0_13325_x2064_x333751951}

[[resends due to MTU discovery]{lang="EN-US"}]{#struct_0_13325_x2064_x1124241896}

[[由于]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_13325_x2064_x333555343}[发现而重传的报文数]{style="font-family:宋体"}

[[packets dropped with MD5 authentication]{lang="EN-US"}]{#struct_0_13325_x2064_1992006513}

[[MD5]{lang="EN-US"}]{#struct_0_13325_x2064_x333620879}[验证丢弃报文数]{style="font-family:宋体"}

[[packets permitted with MD5 authentication]{lang="EN-US"}]{#struct_0_13325_x2064_x357637418}

[[MD5]{lang="EN-US"}]{#struct_0_13325_x2064_x333424271}[验证通过报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1536749524}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **tcp** **statistics**]{lang="EN-US"}]{#struct_0_13325_x2064_x1971006841}

::: {#-77253974 .myid}
[]{#_Toc138239303}[]{#_Toc136679741}[]{#_Toc69790799}[]{#_Toc404786715}[]{#struct_0_13325_x2064_x283695797}[]{#_Toc233688809}

**IP性能优化 \-- IP性能优化配置命令 \-- display tcp verbose**

------------------------------------------------------------------------

[**[display tcp verbose]{lang="EN-US"}**]{#struct_0_13325_x2064_1701874746}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x333489807}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_1551569616}

[**[display tcp verbose]{lang="EN-US"}**[ \[ **pcb** *pcb-index* \]]{lang="EN-US"}]{#struct_0_13325_x2064_2035438761}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_954052084}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display tcp verbose]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_1161453910}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x809520872}[模式：]{style="font-family:宋体"}

[**[display tcp verbose]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x634392250}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1346751362}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_497793046}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x333293199}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1543526019}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_256870287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x2092224408}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x30788913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1415383898}

[**[pcb]{lang="EN-US"}**[ *pcb-index*]{lang="EN-US"}]{#struct_0_13325_x2064_642426736}[：显示指定协议控制块索引的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[pcb-index]{lang="EN-US"}*[表示协议控制块索引，取值范围请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1349082752}[：显示指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示所有单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x251684494}[：显示指定成员设备的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x764828040}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x333358735}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1855423253}[：显示指定单板的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_1058782854}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x422148339}

[**[display tcp verbose]{lang="EN-US"}**]{#struct_0_13325_x2064_x2055166548}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的详细信息，包括]{style="font-family:宋体"}[socket]{lang="EN-US"}[的创建者、状态、选项、类型、使用的协议号等，以及]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号、状态等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1567325746}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_792121446}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display tcp verbose]{lang="EN-US"}]{#struct_0_13325_x2064_792186982}

[TCP inpcb number: 1(tcpcb number: 1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Creator: bgpd\[199\]]{lang="EN-US"}

[ State: ISCONNECTED]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 65700 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 65700 / 512 / N/A]{lang="EN-US"}

[ Type: 1]{lang="EN-US"}

[ Protocol: 6]{lang="EN-US"}

[ Connection info: src = 192.168.20.200:179 ,  dst = 192.168.20.14:4181]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Connection state: ESTABLISHED]{lang="EN-US"}

[ TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR]{lang="EN-US"}

[ NSR state: READY(M)]{lang="EN-US"}

[ Send VRF: 0x0]{lang="EN-US"}

[ Receive VRF: 0x0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1796486355}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display tcp verbose]{lang="EN-US"}]{#struct_0_13325_x2064_792252518}

[TCP inpcb number: 1(tcpcb number: 1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Slot: 6 Cpu: 0]{lang="EN-US"}

[ NSR standby: N/A]{lang="EN-US"}

[ Creator: bgpd\[199\]]{lang="EN-US"}

[ State: ISCONNECTED]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 65700 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 65700 / 512 / N/A]{lang="EN-US"}

[ Type: 1]{lang="EN-US"}

[ Protocol: 6]{lang="EN-US"}

[ Connection info: src = 192.168.20.200:179 ,  dst = 192.168.20.14:4181]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Connection state: ESTABLISHED]{lang="EN-US"}

[ TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR]{lang="EN-US"}

[ NSR state: READY(M)]{lang="EN-US"}

[ Send VRF: 0x0]{lang="EN-US"}

[ Receive VRF: 0x0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1273207545}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display tcp verbose]{lang="EN-US"}]{#struct_0_13325_x2064_x333162127}

[TCP inpcb number: 1(tcpcb number: 1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Chassis: 2 Slot: 6 Cpu: 0]{lang="EN-US"}

[ NSR standby: N/A]{lang="EN-US"}

[ Creator: bgpd\[199\]]{lang="EN-US"}

[ State: ISCONNECTED]{lang="EN-US"}

[ Options: N/A]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 65700 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 65700 / 512 / N/A]{lang="EN-US"}

[ Type: 1]{lang="EN-US"}

[ Protocol: 6]{lang="EN-US"}

[ Connection info: src = 192.168.20.200:179 ,  dst = 192.168.20.14:4181]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Connection state: ESTABLISHED]{lang="EN-US"}

[ TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR]{lang="EN-US"}

[ NSR state: READY(M)]{lang="EN-US"}

[ Send VRF: 0x0]{lang="EN-US"}

[ Receive VRF: 0x0]{lang="EN-US"}

[[[表1-8 ]{lang="EN-US"}]{.FigureDescriptionChar}[display tcp verbo[se]{.FigureDescriptionChar}]{lang="EN-US"}]{#struct_0_13325_x2064_4115268}[[命令显示信息描述表]{style="font-family:黑体"}]{.FigureDescriptionChar}

[]{#table_struct_0_x2023156400}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_789092767}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_1093907626}

[[TCP inpcb number]{lang="EN-US"}]{#struct_0_13325_x2064_x1114059745}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_x1264106571}[类型]{style="font-family:宋体"}[internet]{lang="EN-US"}[协议控制块个数]{style="font-family:宋体"}

[[tcpcb number]{lang="EN-US"}]{#struct_0_13325_x2064_x333227663}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_1956676634}[控制块个数（处于]{style="font-family:宋体"}[TIME_WAIT]{lang="EN-US"}[状态的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[则没有此计数）]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_13325_x2064_x1058969302}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_710806751}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_791859302}

[[单板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_791924838}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_1624019005}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_791990374}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Cpu]{lang="EN-US"}]{#struct_0_13325_x2064_792580198}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_x358510603}[编号]{style="font-family:宋体"}

[[NSR standby::]{lang="EN-US"}]{#struct_0_13325_x2064_1875590560}

[[NSR]{lang="EN-US"}]{#struct_0_13325_x2064_1875656096}[备所在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号和槽位号，如果不存在]{style="font-family:宋体"}[NSR]{lang="EN-US"}[备，则显示"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["]{style="font-family:宋体"}

[[Creator]{lang="EN-US"}]{#struct_0_13325_x2064_x333686414}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_760281502}[的任务名称，括号中为创建者的进程号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_13325_x2064_52646512}

[[socket]{lang="EN-US"}]{#struct_0_13325_x2064_1082701868}[的状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOFDREF]{lang="EN-US"}]{#struct_0_13325_x2064_x819401806}[：用户已经关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTED]{lang="EN-US"}]{#struct_0_13325_x2064_x333751950}[：连接已经建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTING]{lang="EN-US"}]{#struct_0_13325_x2064_x1124176360}[：正在建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTING]{lang="EN-US"}]{#struct_0_13325_x2064_x1377577494}[：正在断开连接]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASYNC]{lang="EN-US"}]{#struct_0_13325_x2064_120481537}[：异步方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTED]{lang="EN-US"}]{#struct_0_13325_x2064_x1732744722}[：连接已经断开]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROTOREF]{lang="EN-US"}]{#struct_0_13325_x2064_x333555342}[：协议强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1992072049}[：不处于上述状态]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_13325_x2064_x1592365189}

[[socket]{lang="EN-US"}]{#struct_0_13325_x2064_1950199176}[的选项，有以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DEBUG]{lang="EN-US"}]{#struct_0_13325_x2064_465261874}[：记录套接字的调试信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_ACCEPTCONN]{lang="EN-US"}]{#struct_0_13325_x2064_x333620878}[：]{lang="EN-US" style="font-family:宋体"}[server]{lang="EN-US"}[端监听连接请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEADDR]{lang="EN-US"}]{#struct_0_13325_x2064_x357702954}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[允许本地地址重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVE]{lang="EN-US"}]{#struct_0_13325_x2064_x543159949}[：协议需要查询空闲的连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DONTROUTE]{lang="EN-US"}]{#struct_0_13325_x2064_x1334760903}[：设置不查路由表，由于目的地址是直连网络的情况]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_BROADCAST]{lang="EN-US"}]{#struct_0_13325_x2064_x333424270}[：套接字支持广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_LINGER]{lang="EN-US"}]{#struct_0_13325_x2064_x1536815060}[：套接字关闭但仍发送剩余数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_OOBINLINE]{lang="EN-US"}]{#struct_0_13325_x2064_1167909793}[：带外数据采用内联方式存储]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEPORT]{lang="EN-US"}]{#struct_0_13325_x2064_x1127931279}[：允许本地端口重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMP]{lang="EN-US"}]{#struct_0_13325_x2064_x333489806}[：入报文记录时间戳，只对非连接的协议有效，时间精确到毫秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_NOSIGPIPE]{lang="EN-US"}]{#struct_0_13325_x2064_1551504080}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[不能发送数据导致返回失败时不创建]{lang="EN-US" style="font-family:宋体"}[SIGPIPE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMPNS]{lang="EN-US"}]{#struct_0_13325_x2064_x1842982391}[：和时]{lang="EN-US" style="font-family:宋体"}[间]{style="font-family:宋体"}[戳选项功能类似，时间可以精确到纳秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVETIME]{lang="EN-US"}]{#struct_0_13325_x2064_1874935200}[：设置空闲探测时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1422354467}[：没有设置选项]{lang="EN-US" style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_13325_x2064_365781397}

[[影响]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x333293198}[连接的错误码]{style="font-family:宋体"}

[[Receiving buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_13325_x2064_1543591555}

[[接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态，状态的取值有：]{style="font-family:宋体"}]{#struct_0_13325_x2064_579450824}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_13325_x2064_x1826380999}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_13325_x2064_x333358734}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_13325_x2064_x422082803}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x1235818070}[：不处于上述状态]{style="font-family:宋体"}

[[Sending buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_13325_x2064_x333162126}

[[发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态，状态的取值有：]{style="font-family:宋体"}]{#struct_0_13325_x2064_4049732}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_13325_x2064_96160325}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_13325_x2064_x1207825126}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_13325_x2064_x333227662}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1956611098}[：不处于上述状态]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_13325_x2064_x1443450821}

[[使用的]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_357515024}[类型，类型的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13325_x2064_1588627890}[：]{style="font-family:宋体"}[SOCK_STREAM]{lang="EN-US"}[，]{style="font-family:宋体"}[流模式，提供可靠的字节流。]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[协议使用此类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13325_x2064_x249637623}[：]{style="font-family:宋体"}[SOCK_DGRAM]{lang="EN-US"}[，数据报模式的通信。]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议使用此类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13325_x2064_x206779769}[：]{lang="EN-US" style="font-family:宋体"}[SOCK_RAW]{lang="EN-US"}[，]{style="font-family:宋体"}[RAW]{lang="EN-US"}[模式的通信方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1588562354}[：不是上述类型]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_13325_x2064_x573796973}

[[使用]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_66960964}[的协议号]{style="font-family:宋体"}

[[Connection info]{lang="EN-US"}]{#struct_0_13325_x2064_1588758962}

[[连接信息，分别为源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_2134168114}[地址及端口号、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号]{style="font-family:宋体"}

[[Inpcb flags]{lang="EN-US"}]{#struct_0_13325_x2064_x802181872}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_1588693426}[协议控制块中的标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVOPTS]{lang="EN-US"}]{#struct_0_13325_x2064_x600309102}[：接收传入的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVRETOPTS]{lang="EN-US"}]{#struct_0_13325_x2064_155257491}[：接收回应的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVDSTADDR]{lang="EN-US"}]{#struct_0_13325_x2064_1588890034}[：接收目的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_HDRINCL]{lang="EN-US"}]{#struct_0_13325_x2064_x1401850260}[：用户提供整个]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEADDR]{lang="EN-US"}]{#struct_0_13325_x2064_1421593161}[：重复使用地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEPORT]{lang="EN-US"}]{#struct_0_13325_x2064_1588824498}[：重复使用端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ANONPORT]{lang="EN-US"}]{#struct_0_13325_x2064_184699102}[：]{lang="EN-US" style="font-family:宋体"}[用户未指定端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVIF]{lang="EN-US"}]{#struct_0_13325_x2064_x1354778808}[：接收报文时记录报文的入接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVTTL]{lang="EN-US"}]{#struct_0_13325_x2064_1589021106}[：携带报文的]{lang="EN-US" style="font-family:宋体"}[TTL]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_DONTFRAG]{lang="EN-US"}]{#struct_0_13325_x2064_x201069556}[：设置不可分片标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ROUTER_ALERT]{lang="EN-US"}]{#struct_0_13325_x2064_1588955570}[：接收携带路由器告警选项的报文]{lang="EN-US" style="font-family:
  宋体"}[，仅]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_PROTOCOL_PACKET]{lang="EN-US"}]{#struct_0_13325_x2064_955759958}[：标识报文为协议报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVVLANID]{lang="EN-US"}]{#struct_0_13325_x2064_82342602}[：接收报文的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVMACADDR]{lang="EN-US"}]{#struct_0_13325_x2064_1589152178}[：接收报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SNDBYLSPV]{lang="EN-US"}]{#struct_0_13325_x2064_199265825}[：通过]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVTOS]{lang="EN-US"}]{#struct_0_13325_x2064_x410340466}[：]{style="font-family:宋体"}[携带报文的]{lang="EN-US" style="font-family:宋体"}[TOS]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SYNCPCB]{lang="EN-US"}]{#struct_0_13325_x2064_1589086642}[：阻塞等待]{style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_160719019}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb extflag]{lang="EN-US"}]{#struct_0_13325_x2064_x370573301}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_x52857093}[协议控制块中的扩展标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_EXTRCVPVCIDX]{lang="EN-US"}]{#struct_0_13325_x2064_1968078850}[：接收报文时记录报文的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVPWID]{lang="EN-US"}]{#struct_0_13325_x2064_1467592439}[：接收报文时记录报文的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_288832606}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb vflag]{lang="EN-US"}]{#struct_0_13325_x2064_1588627891}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_x249572087}[协议控制块中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[版本标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV4]{lang="EN-US"}]{#struct_0_13325_x2064_1588562355}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_TIMEWAIT]{lang="EN-US"}]{#struct_0_13325_x2064_x573731437}[：处于等待状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_ONESBCAST]{lang="EN-US"}]{#struct_0_13325_x2064_x1498640893}[：发送广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DROPPED]{lang="EN-US"}]{#struct_0_13325_x2064_1588758963}[：协议丢弃标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_SOCKREF]{lang="EN-US"}]{#struct_0_13325_x2064_2134102578}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DONTBLOCK]{lang="EN-US"}]{#struct_0_13325_x2064_1588693427}[：]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步时不能被阻塞]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x600374638}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_13325_x2064_215335817}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_1588890035}[协议控制块中的生存周期，括号中为最小生存周期]{style="font-family:宋体"}

[[Connection state]{lang="EN-US"}]{#struct_0_13325_x2064_x1401915796}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_1588824499}[连接状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_13325_x2064_184764638}[：服务器收到客户端的关闭连接请求回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_13325_x2064_1589021107}[：服务器在等待连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_SENT]{lang="EN-US"}]{#struct_0_13325_x2064_x201004020}[：客户端发出连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_RCVD]{lang="EN-US"}]{#struct_0_13325_x2064_1588955571}[：服务器收到客户端连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_13325_x2064_955694422}[：服务器和客户端双方建立连接并能进行双向数据传递的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE_WAIT]{lang="EN-US"}]{#struct_0_13325_x2064_x1435799145}[：服务器收到客户端关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_1]{lang="EN-US"}]{#struct_0_13325_x2064_1589152179}[：客户端发出关闭连接请求等待服务器回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSING]{lang="EN-US"}]{#struct_0_13325_x2064_199200289}[：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAST_ACK]{lang="EN-US"}]{#struct_0_13325_x2064_1589086643}[：服务器向客户端发出关闭连接请求等待回应时所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT_2]{lang="EN-US"}]{#struct_0_13325_x2064_160784555}[：客户端收到服务器关闭连接回应后所处的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIME_WAIT]{lang="EN-US"}]{#struct_0_13325_x2064_1588627888}[：客户端收到服务器的关闭连接请求后所处的状态]{style="font-family:宋体"}

[[TCP options]{lang="EN-US"}]{#struct_0_13325_x2064_x853489399}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_x853423863}[的选项类型，有以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_13325_x2064_x853358327}[F]{lang="EN-US"}[\_MD5SIG]{lang="EN-US"}[：使能密钥]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_13325_x2064_x853227255}[F]{lang="EN-US"}[\_PASSWORD]{lang="EN-US"}[：已经设置密钥]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_13325_x2064_x853161719}[F]{lang="EN-US"}[\_NODELAY]{lang="EN-US"}[：关闭延时]{lang="EN-US" style="font-family:宋体"}[ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_13325_x2064_x853030647}[F]{lang="EN-US"}[\_NOOPT]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[不使用选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_13325_x2064_x853489400}[F]{lang="EN-US"}[\_NOPUSH]{lang="EN-US"}[：对写入的最后部分不进行]{lang="EN-US" style="font-family:宋体"}[PUSH]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_13325_x2064_x853423864}[F]{lang="EN-US"}[\_BINDFOREIGNADDR]{lang="EN-US"}[：绑定对端]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_13325_x2064_x853292792}[F]{lang="EN-US"}[\_NSR]{lang="EN-US"}[：使能]{lang="EN-US" style="font-family:宋体"}[TCP ]{lang="EN-US"}[NSR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TF_REQ_SCALE]{lang="EN-US"}]{#struct_0_13325_x2064_x853227256}[：使能窗口缩放因子选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TF_REQ_TSTMP]{lang="EN-US"}]{#struct_0_13325_x2064_x853161720}[：使能]{lang="EN-US" style="font-family:宋体"}[时间]{style="font-family:宋体"}[戳选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TF_SACK_PERMIT]{lang="EN-US"}]{#struct_0_13325_x2064_x853096184}[：使能选择性]{lang="EN-US" style="font-family:宋体"}[ACK]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[NSR state]{lang="EN-US"}]{#struct_0_13325_x2064_x854013688}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_x853948152}[连接]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_13325_x2064_x853489401}[：关闭（初始）状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSING]{lang="EN-US"}]{#struct_0_13325_x2064_x853423865}[：]{style="font-family:宋体"}[连接待关闭状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ENABLED]{lang="EN-US"}]{#struct_0_13325_x2064_x853292793}[：]{style="font-family:宋体"}[使能备份功能状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OPEN]{lang="EN-US"}]{#struct_0_13325_x2064_x853227257}[：连接开始同步状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PENDING]{lang="EN-US"}]{#struct_0_13325_x2064_x853161721}[：]{style="font-family:宋体"} [连接判定状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[READY]{lang="EN-US"}]{#struct_0_13325_x2064_x853030649}[：连接备份就绪状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SMOOTH]{lang="EN-US"}]{#struct_0_13325_x2064_x854013689}[：连接平滑状态]{style="font-family:宋体"}

[[角色：]{style="font-family:宋体"}[M]{lang="EN-US"}]{#struct_0_13325_x2064_x853948153}[表示主连接、]{style="font-family:宋体"}[S]{lang="EN-US"}[表示备份连接]{style="font-family:宋体"}

[[Send VRF]{lang="EN-US"}]{#struct_0_13325_x2064_x250161912}

[[发送实例]{style="font-family:宋体"}]{#struct_0_13325_x2064_1588562352}

[[Receive VRF]{lang="EN-US"}]{#struct_0_13325_x2064_x573403757}

[[接收实例]{style="font-family:宋体"}]{#struct_0_13325_x2064_1588758960}

[ ]{lang="SV"}

::: {#-773023540 .myid}
[]{#_Toc138239304}[]{#_Toc136679743}[]{#_Toc60058940}[]{#_Toc404786716}[]{#struct_0_13325_x2064_2134037042}[]{#_Toc233688810}

**IP性能优化 \-- IP性能优化配置命令 \-- display udp**

------------------------------------------------------------------------

[**[display udp]{lang="EN-US"}**]{#struct_0_13325_x2064_1203088077}[命令用来显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_702859463}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_1377716046}

[**[display udp]{lang="EN-US"}**]{#struct_0_13325_x2064_333049932}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x315277992}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display udp]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_584533645}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x2017822888}[模式：]{style="font-family:宋体"}

[**[display udp]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_1588693424}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x600440174}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_1373892968}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x2116477637}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1049011696}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x875251608}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_142904642}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x849786196}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_56120792}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1588890032}[：显示指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1401457044}[：显示指定成员设备的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x717839409}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x226297889}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1439693987}[：显示指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_x957443169}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x149189613}

[**[display udp]{lang="EN-US"}**]{#struct_0_13325_x2064_x744019393}[命令用来显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息，包括本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号、对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x472634923}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1272654549}[显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display udp]{lang="EN-US"}]{#struct_0_13325_x2064_1588824496}

[ Local Addr:port        Foreign Addr:port      PCB]{lang="EN-US"}

[ 0.0.0.0:69             0.0.0.0:0              0x0000000000000003]{lang="EN-US"}

[ 192.168.20.200:1024    192.168.20.14:69       0x0000000000000002]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_185616606}[显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display udp]{lang="EN-US"}]{#struct_0_13325_x2064_x2005571246}

[ Local Addr:port        Foreign Addr:port     Slot  CPU PCB]{lang="EN-US"}

[ 0.0.0.0:69             0.0.0.0:0             1     0   0x0000000000000003]{lang="EN-US"}

[ 192.168.20.200:1024    192.168.20.14:69      5     0   0x0000000000000002]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1161009349}[显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接摘要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display udp]{lang="EN-US"}]{#struct_0_13325_x2064_x402316397}

[ Local Addr:port        Foreign Addr:port     Chassis Slot  CPU PCB]{lang="EN-US"}

[ 0.0.0.0:69             0.0.0.0:0             1       1     0   0x0000000000000003]{lang="EN-US"}

[ 192.168.20.200:1024    192.168.20.14:69      1       5     0   0x0000000000000002]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display udp]{lang="EN-US"}]{#struct_0_13325_x2064_x975906240}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1734867424}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_1589021104}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_x201200628}

[[Local Addr:port]{lang="EN-US"}]{#struct_0_13325_x2064_x287051586}

[[本端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x1227114343}[地址及端口号]{style="font-family:宋体"}

[[Foreign Addr:port]{lang="EN-US"}]{#struct_0_13325_x2064_1973893627}

[[对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_84912284}[地址及端口号]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_13325_x2064_x1730370333}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_1588955568}[中的成员编号]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_955235671}

[[单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1562343528}

[[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_x957836386}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_x957508706}[编号]{style="font-family:宋体"}

[[PCB]{lang="EN-US"}]{#struct_0_13325_x2064_x2062107270}

[[协议控制块索引]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2078666102}

[ ]{lang="EN-US"}

::: {#25370302 .myid}
[]{#_Toc404786717}[]{#struct_0_13325_x2064_1589152176}

**IP性能优化 \-- IP性能优化配置命令 \-- display udp statistics**

------------------------------------------------------------------------

[**[display udp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_200183329}[命令用来显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x2113297969}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x947721216}

[**[display udp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x1181317619}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x11930201}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display udp statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_1568205063}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_273193750}[模式：]{style="font-family:宋体"}

[**[display udp statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x2087474817}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1589086640}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_160850091}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x2350267}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x965338468}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_628128785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_696956801}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_721260713}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1652973333}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1588627889}[：显示指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x250096376}[：显示指定成员设备的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_935408093}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1500170752}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1165771418}[：显示指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_x957770851}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_915523936}

[**[display udp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_1268675354}[命令用来显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息，包括接收和发送的各类]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1718969716}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x900946167}[显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display udp statistics]{lang="EN-US"}]{#struct_0_13325_x2064_1588562353}

[Received packets:]{lang="EN-US"}

[     Total: 240]{lang="EN-US"}

[     checksum error: 0, no checksum: 0]{lang="EN-US"}

[     shorter than header: 0, data length larger than packet: 0]{lang="EN-US"}

[     no socket on port(unicast): 0]{lang="EN-US"}

[     no socket on port(broadcast/multicast): 240]{lang="EN-US"}

[     not delivered, input socket full: 0]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[     Total: 0]{lang="EN-US"}

[]{#struct_0_13325_x2064_x573338221}[]{#_Toc138413620}[]{#_Toc138239199}[[表1-10 ]{lang="EN-US"}[display udp statistics]{lang="EN-US"}]{#_Toc54497779}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_x1732970128}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_x272605853}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1895997291}

[[Received packets:]{lang="EN-US"}]{#struct_0_13325_x2064_x1660865768}

[[Total]{lang="EN-US"}]{#struct_0_13325_x2064_x289616573}

[[接收的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_13325_x2064_1588758961}[报文总数]{style="font-family:宋体"}

[[checksum error]{lang="EN-US"}]{#struct_0_13325_x2064_2133971506}

[[校验和出错的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1299223222}

[[no checksum]{lang="EN-US"}]{#struct_0_13325_x2064_1850276636}

[[没有校验和的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_343959982}

[[shorter than header]{lang="EN-US"}]{#struct_0_13325_x2064_1514552637}

[[报文长度比报文头部短的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_1588693425}

[[data length larger than packet]{lang="EN-US"}]{#struct_0_13325_x2064_x600505710}

[[报文数据长度超过报文长度的报文数]{style="font-family:宋体"}]{#struct_0_13325_x2064_977483848}

[[no socket on port(unicast)]{lang="EN-US"}]{#struct_0_13325_x2064_207924918}

[[端口上无]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_956370649}[的单播报文数]{style="font-family:宋体"}

[[no socket on port(broadcast/multicast)]{lang="EN-US"}]{#struct_0_13325_x2064_1588890033}

[[端口上无]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x1401522580}[的广播和组播报文数]{style="font-family:宋体"}

[[not delivered, input socket full]{lang="EN-US"}]{#struct_0_13325_x2064_x1298945149}

[[因为]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_1129954845}[缓冲区已满而没有向上层传送的报文数]{style="font-family:宋体"}

[[Sent packets:]{lang="EN-US"}]{#struct_0_13325_x2064_336289873}

[[Total]{lang="EN-US"}]{#struct_0_13325_x2064_1588824497}

[[发送的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_13325_x2064_185682142}[报文总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x472731792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset udp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x885223920}

::: {#128068941 .myid}
[]{#_Toc69790802}[]{#_Toc39143440}[]{#_Toc132083710}[]{#_Toc404786718}[]{#struct_0_13325_x2064_1517539243}[]{#_Toc233688812}

**IP性能优化 \-- IP性能优化配置命令 \-- display udp verbose**

------------------------------------------------------------------------

[**[display udp verbose]{lang="EN-US"}**]{#struct_0_13325_x2064_x906611526}[命令用来显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_2083219005}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_1589021105}

[**[display udp verbose]{lang="EN-US"}**[ \[ **pcb** *pcb-index* \]]{lang="EN-US"}]{#struct_0_13325_x2064_x201135092}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_857749471}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display udp verbose]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x179036010}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_1078574396}[模式：]{style="font-family:宋体"}

[**[display udp verbose]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **pcb** *pcb-index* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_1284507353}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x340274019}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_504118847}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x754985082}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1588955569}

[[network-operator]{lang="EN-US"}]{#struct_0_13325_x2064_955170135}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_89247287}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13325_x2064_x1903441471}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1333713248}

[**[pcb]{lang="EN-US"}**[ *pcb-index*]{lang="EN-US"}]{#struct_0_13325_x2064_x1234470622}[：显示指定协议控制块索引的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[pcb-index]{lang="EN-US"}*[表示协议控制块索引，取值范围请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1060889310}[：显示指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1375722874}[：显示指定成员设备的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1390190735}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_549981386}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1338692620}[：显示指定单板的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_x958295139}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1589152177}

[**[display udp verbose]{lang="EN-US"}**]{#struct_0_13325_x2064_200117793}[命令用来显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接的详细信息，包括]{style="font-family:宋体"}[socket]{lang="EN-US"}[的创建者、状态、选项、类型、使用的协议号等，以及]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_248280278}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_791924843}[显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display udp verbose]{lang="EN-US"}]{#struct_0_13325_x2064_791990379}

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

[ Connection info: src = 0.0.0.0:69, dst = 0.0.0.0:0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_915050160}[显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display udp verbose]{lang="EN-US"}]{#struct_0_13325_x2064_792580203}

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

[ Connection info: src = 0.0.0.0:69, dst = 0.0.0.0:0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1513520965}[显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display udp verbose]{lang="EN-US"}]{#struct_0_13325_x2064_1589086641}

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

[ Connection info: src = 0.0.0.0:69, dst = 0.0.0.0:0]{lang="EN-US"}

[ Inpcb flags: N/A]{lang="EN-US"}

[ Inpcb extflag: N/A]{lang="EN-US"}

[ Inpcb vflag: INP_IPV4]{lang="EN-US"}

[ TTL: 255(minimum TTL: 0)]{lang="EN-US"}

[ Send VRF: 0xffff]{lang="EN-US"}

[ Receive VRF: 0xffff]{lang="EN-US"}

[[[表1-11 ]{lang="EN-US"}]{.FigureDescriptionChar}[display udp verbose]{lang="EN-US"}]{#struct_0_13325_x2064_160915627}[[命令显示信息描述表]{style="font-family:黑体"}]{.FigureDescriptionChar}

[]{#table_struct_0_x1739877764}[[字段]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1530393339}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13325_x2064_1354284849}

[[Total UDP socket number]{lang="EN-US"}]{#struct_0_13325_x2064_800215787}

[[UDP socket]{lang="EN-US"}]{#struct_0_13325_x2064_2075040616}[总数]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_13325_x2064_1588627886}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x249244408}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_2129149504}

[[单板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_1120747633}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_13325_x2064_388836921}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_1591164499}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Cpu]{lang="EN-US"}]{#struct_0_13325_x2064_x957705316}

[[节点所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_13325_x2064_x957901924}[编号]{style="font-family:宋体"}

[[Creator]{lang="EN-US"}]{#struct_0_13325_x2064_x627196185}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_1107433366}[的任务名称，括号中为创建者的进程号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_13325_x2064_1588562350}

[[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x573534829}[的状态，可能的状态如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOFDREF]{lang="EN-US"}]{#struct_0_13325_x2064_1262736589}[：用户已经关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTED]{lang="EN-US"}]{#struct_0_13325_x2064_x498135291}[：连接已经建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISCONNECTING]{lang="EN-US"}]{#struct_0_13325_x2064_x658209940}[：正在建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTING]{lang="EN-US"}]{#struct_0_13325_x2064_1588758958}[：正在断开连接]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASYNC]{lang="EN-US"}]{#struct_0_13325_x2064_2133512755}[：异步方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDISCONNECTED]{lang="EN-US"}]{#struct_0_13325_x2064_518517238}[：连接已经断开]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROTOREF]{lang="EN-US"}]{#struct_0_13325_x2064_x10191583}[：协议强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x746374963}[：不处于上述状态]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_13325_x2064_1588693422}

[[socket]{lang="EN-US"}]{#struct_0_13325_x2064_x600046958}[的选项，有以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DEBUG]{lang="EN-US"}]{#struct_0_13325_x2064_1006557616}[：记录套接字的调试信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_ACCEPTCONN]{lang="EN-US"}]{#struct_0_13325_x2064_991330585}[：]{lang="EN-US" style="font-family:宋体"}[server]{lang="EN-US"}[端监听连接请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEADDR]{lang="EN-US"}]{#struct_0_13325_x2064_1588890030}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[允许本地地址重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_KEEPALIVE]{lang="EN-US"}]{#struct_0_13325_x2064_x1401588116}[：协议需要查询空闲的连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_DONTROUTE]{lang="EN-US"}]{#struct_0_13325_x2064_1560375575}[：设置不查路由表，由于目的地址是直连网络的情况]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_BROADCAST]{lang="EN-US"}]{#struct_0_13325_x2064_452631286}[：套接字支持广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_LINGER]{lang="EN-US"}]{#struct_0_13325_x2064_x891549715}[：套接字关闭但仍发送剩余数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_OOBINLINE]{lang="EN-US"}]{#struct_0_13325_x2064_1588824494}[：带外数据采用内联方式存储]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_REUSEPORT]{lang="EN-US"}]{#struct_0_13325_x2064_185485534}[：允许本地端口重复使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMP]{lang="EN-US"}]{#struct_0_13325_x2064_x1876632314}[：入报文记录时间戳，只对非连接的协议有效，时间精确到毫秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_NOSIGPIPE]{lang="EN-US"}]{#struct_0_13325_x2064_1084723438}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[不能发送数据导致返回失败时不创建]{lang="EN-US" style="font-family:宋体"}[SIGPIPE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SO_TIMESTAMPNS]{lang="EN-US"}]{#struct_0_13325_x2064_1589021102}[：和时戳选项功能类似，时间可以精确到纳秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x201331700}[：没有设置选项]{lang="EN-US" style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_13325_x2064_105997724}

[[影响]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_1588955566}[连接的错误码]{style="font-family:宋体"}

[[Receiving buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_13325_x2064_956153175}

[[接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态，状态的取值有：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1096751642}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_13325_x2064_x172096440}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_13325_x2064_1589152174}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_13325_x2064_200052257}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x141742505}[：不处于上述状态]{style="font-family:宋体"}

[[Sending buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_13325_x2064_x515889093}

[[发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态，状态的取值有：]{style="font-family:宋体"}]{#struct_0_13325_x2064_1589086638}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTSENDMORE]{lang="EN-US"}]{#struct_0_13325_x2064_160325802}[：不能发送数据到对端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CANTRCVMORE]{lang="EN-US"}]{#struct_0_13325_x2064_442026241}[：不能从对端接收数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCVATMARK]{lang="EN-US"}]{#struct_0_13325_x2064_1588627887}[：接收标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x249178872}[：不处于上述状态]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_13325_x2064_x1483033186}

[[使用的]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_1588562351}[类型，类型的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13325_x2064_x573469293}[：]{style="font-family:宋体"}[SOCK_STREAM]{lang="EN-US"}[，]{style="font-family:宋体"}[流模式，提供可靠的字节流。]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[协议使用此类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13325_x2064_1308748052}[：]{style="font-family:宋体"}[SOCK_DGRAM]{lang="EN-US"}[，数据报模式的通信。]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议使用此类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13325_x2064_868468838}[：]{lang="EN-US" style="font-family:宋体"}[SOCK_RAW]{lang="EN-US"}[，]{style="font-family:宋体"}[RAW]{lang="EN-US"}[模式的通信方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1588758959}[：不是上述类型]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_13325_x2064_2133447219}

[[使用]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_13325_x2064_1331080014}[的协议号]{style="font-family:宋体"}

[[Connection info]{lang="EN-US"}]{#struct_0_13325_x2064_1588693423}

[[连接信息，分别为源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x600112494}[地址及端口号、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址及端口号]{style="font-family:宋体"}

[[Inpcb flags]{lang="EN-US"}]{#struct_0_13325_x2064_1391527839}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_1588890031}[协议控制块中的标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVOPTS]{lang="EN-US"}]{#struct_0_13325_x2064_x1401653652}[：接收传入的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVRETOPTS]{lang="EN-US"}]{#struct_0_13325_x2064_405856527}[：接收回应的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[选项]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVDSTADDR]{lang="EN-US"}]{#struct_0_13325_x2064_1588824495}[：接收目的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_HDRINCL]{lang="EN-US"}]{#struct_0_13325_x2064_185551070}[：用户提供整个]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEADDR]{lang="EN-US"}]{#struct_0_13325_x2064_822551662}[：重复使用地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_REUSEPORT]{lang="EN-US"}]{#struct_0_13325_x2064_1589021103}[：重复使用端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ANONPORT]{lang="EN-US"}]{#struct_0_13325_x2064_x201266164}[：]{lang="EN-US" style="font-family:宋体"}[用户未指定端口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVIF]{lang="EN-US"}]{#struct_0_13325_x2064_x1084630544}[：接收报文时记录报文的入接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVTTL]{lang="EN-US"}]{#struct_0_13325_x2064_1588955567}[：携带报文的]{lang="EN-US" style="font-family:宋体"}[TTL]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_DONTFRAG]{lang="EN-US"}]{#struct_0_13325_x2064_956087639}[：设置不可分片标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_ROUTER_ALERT]{lang="EN-US"}]{#struct_0_13325_x2064_x730255882}[：接收携带路由器告警选项的报文]{lang="EN-US" style="font-family:
  宋体"}[，仅]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_PROTOCOL_PACKET]{lang="EN-US"}]{#struct_0_13325_x2064_1589152175}[：标识报文为协议报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVVLANID]{lang="EN-US"}]{#struct_0_13325_x2064_199986721}[：接收报文的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，仅]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVMACADDR]{lang="EN-US"}]{#struct_0_13325_x2064_1589086639}[：接收报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SNDBYLSPV]{lang="EN-US"}]{#struct_0_13325_x2064_160391338}[：通过]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RECVTOS]{lang="EN-US"}]{#struct_0_13325_x2064_x1077760465}[：携带报文的]{lang="EN-US" style="font-family:宋体"}[TOS]{lang="EN-US"}[，仅]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[RawIP]{lang="EN-US"}[支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_SYNCPCB]{lang="EN-US"}]{#struct_0_13325_x2064_x1140255465}[：阻塞等待]{style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1551516360}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb extflag]{lang="EN-US"}]{#struct_0_13325_x2064_x1944551413}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_740096070}[协议控制块中的扩展标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_EXTRCVPVCIDX]{lang="EN-US"}]{#struct_0_13325_x2064_361892685}[：接收报文时记录报文的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INP_RCVPWID]{lang="EN-US"}]{#struct_0_13325_x2064_x755073022}[：接收报文时记录报文的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_1261605845}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[Inpcb vflag]{lang="EN-US"}]{#struct_0_13325_x2064_x1140321001}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_x1225979153}[协议控制块中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[版本标记，标记的取值有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_IPV4]{lang="EN-US"}]{#struct_0_13325_x2064_x1140124393}[：运用与]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[通信]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_TIMEWAIT]{lang="EN-US"}]{#struct_0_13325_x2064_x469765082}[：处于等待状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_ONESBCAST]{lang="EN-US"}]{#struct_0_13325_x2064_1271490678}[：发送广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DROPPED]{lang="EN-US"}]{#struct_0_13325_x2064_x1140189929}[：协议丢弃标志]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_SOCKREF]{lang="EN-US"}]{#struct_0_13325_x2064_x1926908452}[：]{lang="EN-US" style="font-family:宋体"}[socket]{lang="EN-US"}[强关联]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INP_DONTBLOCK]{lang="EN-US"}]{#struct_0_13325_x2064_x1139993321}[：]{lang="EN-US" style="font-family:宋体"}[inpcb]{lang="EN-US"}[同步时不能被阻塞]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_13325_x2064_x439709292}[：不是上述标记]{lang="EN-US" style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_13325_x2064_385684220}

[[Internet]{lang="EN-US"}]{#struct_0_13325_x2064_x1140058857}[协议控制块中的生存周期，括号中为最小生存周期]{style="font-family:宋体"}

[[Send VRF]{lang="EN-US"}]{#struct_0_13325_x2064_156052474}

[[发送实例]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1139862249}

[[Receive VRF]{lang="EN-US"}]{#struct_0_13325_x2064_x1904572598}

[[接收实例]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1139927785}

[ ]{lang="EN-US"}

::: {#-428175606 .myid}
[]{#_Toc138239305}[]{#_Toc136679744}[]{#_Toc404786719}[]{#struct_0_13325_x2064_577911239}[]{#_Toc271702015}

**IP性能优化 \-- IP性能优化配置命令 \-- ip forward-broadcast**

------------------------------------------------------------------------

[**[ip forward-broadcast]{lang="EN-US"}**]{#struct_0_13325_x2064_660147488}[命令用来配置允许接口接收和转发直连网段的定向广播报文。]{style="font-family:宋体"}

[**[undo ip forward-broadcast]{lang="EN-US"}**]{#struct_0_13325_x2064_618584036}[命令用来禁止接口接收和转发直连网段的定向广播报文。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1150442227}

[**[ip forward-broadcast]{lang="EN-US"}**]{#struct_0_13325_x2064_x1570030759}

[**[undo ip forward-broadcast]{lang="EN-US"}**]{#struct_0_13325_x2064_x1125378336}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_236067367}

[[设备禁止转发直连网段的定向广播报文；设备是否允许接收定向广播报文，请以设备实际情况为准。]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1139731177}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1879321342}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x2096971637}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1041035835}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1457561860}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1838874397}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x695227442}

[[定向广播报文是指发送给特定网络的广播报文。该报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x888104423}[地址中网络号码字段为特定网络的网络号，主机号码字段为全]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[接口接收和转发直连网段的定向广播报文包括以下几种情况：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1139796713}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接收定向广播报文的情况下，如果在接口上配置了此命令，设备允许接收此接口直连网段的定向广播报文。]{style="font-family:宋体"}]{#struct_0_13325_x2064_66419398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在转发定向广播报文的情况下，如果在接口上配置了此命令，设备从其他接口接收到目的地址为此接口直连网段的定向广播报文时，会从此接口转发此类报文。]{style="font-family:宋体"}]{#struct_0_13325_x2064_814435502}

[[黑客可以利用定向广播报文来攻击网络系统，给网络的安全带来了很大的隐患。但在某些应用环境下，设备接口需要接收或转发这类定向广播报文，例如：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x394985491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_13325_x2064_x455048092}[UDP Helper]{lang="EN-US"}[功能，将广播报文转换为单播报文发送给指定的服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}[Wake on LAN]{lang="EN-US"}]{#struct_0_13325_x2064_1592694388}[（网络唤醒）功能，发送定向广播报文唤醒远程网络中的计算机。]{lang="EN-US" style="font-family:宋体"}

[[在上述情况下，用户可以通过命令配置接口允许接收和转发直连网段的定向广播报文。]{style="font-family:宋体"}]{#struct_0_13325_x2064_x480171298}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x223364869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13325_x2064_517418641}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1140255464}[配置允许接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收和转发直连网段的定向广播报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x14567581}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip forward-broadcast]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13325_x2064_x1136020546}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x830886329}[配置允许]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[接收和转发面向直连网段的定向广播报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_1781856739}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ip forward-broadcast]{lang="EN-US"}
:::

::: {#-354664333 .myid}
[]{#_Toc404786720}[]{#struct_0_13325_x2064_583098274}

**IP性能优化 \-- IP性能优化配置命令 \-- ip icmp error-interval**

------------------------------------------------------------------------

[**[ip icmp error-interval]{lang="EN-US" style="color:black"}**]{#struct_0_13325_x2064_x948442046}[用来配置发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文对应的令牌桶容量和令牌刷新周期。]{style="font-family:宋体"}

[**[undo ip icmp error-interval]{lang="EN-US" style="color:black"}**]{#struct_0_13325_x2064_x1140321000}[用来恢复缺省情况]{style="font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_340104788}

[**[ip icmp error-interval]{lang="EN-US" style="color:black"}**]{#struct_0_13325_x2064_x1974044351}*[ milliseconds ]{lang="EN-US" style="color:black"}*[\[ ]{lang="EN-US" style="font-size:9.5pt;color:black"}*[bucketsize ]{lang="EN-US" style="color:black"}*[\]]{lang="EN-US" style="color:black"}

[**[undo ip icmp error-interval]{lang="EN-US" style="color:black"}**]{#struct_0_13325_x2064_1753985635}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_247586019}

[[令牌桶容量为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_13325_x2064_x1391843449}[，令牌刷新周期为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1576840932}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_1037448193}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1140124392}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1096318859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x2066959371}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x806359687}

[*[milliseconds]{lang="EN-US" style="color:black"}*]{#struct_0_13325_x2064_688654972}[：]{style="font-family:宋体;color:black"}[令牌刷新周期，取值范围]{style="font-family:宋体"}[0\~2147483647]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}[取值为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:
black"}[时，表示不限制]{style="font-family:宋体;color:black"}[ICMP]{lang="EN-US" style="color:black"}[差错报文的发送。]{style="font-family:宋体;
color:black"}

[*[bucketsize]{lang="EN-US" style="color:black"}*]{#struct_0_13325_x2064_570435817}[：]{style="font-family:
宋体;color:black"}[令牌桶中容纳的令牌数]{style="font-family:宋体;color:black"}[，取值范围]{style="font-family:宋体"}[1\~200]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_2033039321}

[[如果网络中短时间内发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_723007705}[差错报文过多，将可能导致网络拥塞。为了避免这种情况，用户可以控制设备在指定时间内发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文的最大个数，目前采用令牌桶算法来实现。]{style="font-family:宋体"}

[[用户可以设置令牌桶的容量，即令牌桶中可以同时容纳的令牌数；同时可以设置令牌桶的刷新周期，即每隔多长时间发放一个令牌到令牌桶中，直到令牌桶中的令牌数达到配置的容量。一个令牌表示允许发送一个]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_731422151}[差错报文，每当发送一个]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文，则令牌桶中减少一个令牌。如果连续发送的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文超过了令牌桶的容量，则后续的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文将不能被发送出去，直到按照所设置的刷新频率将新的令牌放入令牌桶中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1140189928}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x360824511}[配置设备发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文对应的令牌桶容量为]{style="font-family:宋体"}[40]{lang="EN-US"}[，令牌刷新周期为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x2144603085}

[\[Sysname\] [ip icmp error-interval 200 40]{style="color:black"}]{lang="EN-US"}
:::

::::: {#-1093903595 .myid}
[]{#_Toc404786721}[]{#struct_0_13325_x2064_794118493}[]{#_Toc314755516}[]{#_Toc314755517}[]{#_Toc314755518}[]{#_Toc314755519}[]{#_Toc314755520}[]{#_Toc314755521}[]{#_Toc314755522}[]{#_Toc314755523}[]{#_Toc314755524}[]{#_Toc314755525}[]{#_Toc314755526}[]{#_Toc314755527}[]{#_Toc314755528}[]{#_Toc314755529}[]{#_Toc314755530}[]{#_Toc314755531}[]{#_Toc314755532}[]{#_Toc314755533}[]{#_Toc314755534}[]{#_Toc314755535}[]{#_Toc314755536}[]{#_Toc314755537}[]{#_Toc314755538}[]{#_Toc314755539}[]{#_Toc314755540}[]{#_Toc314755541}[]{#_Toc314755542}[]{#_Toc314755543}[]{#_Toc314755544}[]{#_Toc314755545}[]{#_Toc314755546}[]{#_Toc314755547}[]{#_Toc314755548}[]{#_Toc336436883}[]{#_Toc336609757}[]{#_Toc336436884}[]{#_Toc336609758}[]{#_Toc336436885}[]{#_Toc336609759}[]{#_Toc336436886}[]{#_Toc336609760}[]{#_Toc336436887}[]{#_Toc336609761}[]{#_Toc336436888}[]{#_Toc336609762}[]{#_Toc336436889}[]{#_Toc336609763}[]{#_Toc336436890}[]{#_Toc336609764}[]{#_Toc336436891}[]{#_Toc336609765}[]{#_Toc336436892}[]{#_Toc336609766}[]{#_Toc336436893}[]{#_Toc336609767}[]{#_Toc336436894}[]{#_Toc336609768}[]{#_Toc336436895}[]{#_Toc336609769}[]{#_Toc336436896}[]{#_Toc336609770}[]{#_Toc336436897}[]{#_Toc336609771}[]{#_Toc336436898}[]{#_Toc336609772}[]{#_Toc336436899}[]{#_Toc336609773}[]{#_Toc336436900}[]{#_Toc336609774}[]{#_Toc336436901}[]{#_Toc336609775}[]{#_Toc336436902}[]{#_Toc336609776}[]{#_Toc336436903}[]{#_Toc336609777}[]{#_Toc336436904}[]{#_Toc336609778}

**IP性能优化 \-- IP性能优化配置命令 \-- ip icmp fragment discarding**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_13325_x2064_x1918609464}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_13325_x2064_1342723050}
:::

[ ]{lang="EN-US"}

[**[ip icmp fragment discarding]{lang="EN-US"}**]{#struct_0_13325_x2064_366923487}[命令用来关闭]{style="font-family:
宋体"}[ICMP]{lang="EN-US"}[分片报文转发功能。]{style="font-family:宋体"}

[**[undo ip icmp fragment discarding]{lang="EN-US"}**]{#struct_0_13325_x2064_x71885454}[命令用来开启]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[分片报文转发功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1139993320}

[**[ip icmp fragment discarding]{lang="EN-US"}**]{#struct_0_13325_x2064_x2005793233}

[**[undo ip icmp fragment discarding]{lang="EN-US"}**]{#struct_0_13325_x2064_x1335715734}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x424607199}

[[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_x967471866}[分片报文转发功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_443258341}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1892715307}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1703299382}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1140058856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1410031467}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x979760615}

[[为了防止]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_1996292771}[分片报文攻击，用户可以关闭设备的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[分片报文转发功能，对于收到的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[分片报文不进行转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1846054982}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_392864277}[关闭]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[分片报文转发功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x1086712613}

[\[Sysname\] ip icmp fragment discarding]{lang="EN-US"}
:::::

::: {#-1655029184 .myid}
[]{#_Toc404786722}[]{#struct_0_13325_x2064_x1141876489}

**IP性能优化 \-- IP性能优化配置命令 \-- ip icmp source**

------------------------------------------------------------------------

[**[ip icmp source]{lang="EN-US" style="color:black"}**]{#struct_0_13325_x2064_x1139862248}[命令用来配置]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文指定源地址功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ip icmp source]{lang="EN-US" style="color:black"}**]{#struct_0_13325_x2064_x338488657}[命令用来关闭]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文指定源地址功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_717457262}

[**[ip icmp source]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] *ip-address*]{lang="EN-US"}]{#struct_0_13325_x2064_1772815382}

[**[undo ip icmp source ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13325_x2064_1852543447}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_588695193}

[[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_x1747527167}[报文指定源地址功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_849648739}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_670099046}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1139927784}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_2143995180}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_2067847219}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1726707329}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13325_x2064_x669729055}[：指定地址所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例必须已经存在。]{style="font-family:宋体"}[如果不指定本参数，则表示公网内的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US" style="color:black"}*]{#struct_0_13325_x2064_x1553534676}[：表示设备发送]{style="font-family:宋体;color:black"}[ICMP]{lang="EN-US"}[报文时指定的源地址]{style="font-family:宋体;color:black"}[。]{style="font-family:
宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_13325_x2064_x807533749}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[在网络中]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x379618132}[地址配置较多的情况下，收到]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文时，用户很难根据报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址判断报文来自哪台设备。为了简化这一判断过程，可以配置]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文指定源地址功能。用户配置特定地址（如环回口地址）为]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文的源地址，可以简化判断。]{style="font-family:宋体"}

[[设备发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_x1139731176}[差错报文（]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时、端口不可达和参数错误等）和]{style="font-family:宋体"}[ping echo request]{lang="EN-US"}[报文时，都可以通过上述命令指定报文的源地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_313237401}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1801045555}[配置设备发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文时指定的源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_292882194}

[\[Sysname\] ip icmp source 1.1.1.1]{lang="EN-US"}
:::

::: {#-1414702285 .myid}
[]{#_Toc404786723}[]{#struct_0_13325_x2064_x1126262026}[]{#_Toc298765623}

**IP性能优化 \-- IP性能优化配置命令 \-- ip mtu**

------------------------------------------------------------------------

[**[ip mtu]{lang="EN-US"}**]{#struct_0_13325_x2064_x1405324536}[命令用来配置接口上发送]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ip mtu]{lang="EN-US"}**]{#struct_0_13325_x2064_x212340659}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_493015617}

[**[ip mtu]{lang="PT-BR"}**]{#struct_0_13325_x2064_1930040958}[ *mtu-size*]{lang="PT-BR"}

[**[undo ip mtu]{lang="PT-BR"}**]{#struct_0_13325_x2064_x1139796712}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1499664543}

[[没有配置接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_13325_x2064_x948097362}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1793247585}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_578145665}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1373679572}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x580497476}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_323855041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1140255467}

[*[mtu-size]{lang="EN-US"}*]{#struct_0_13325_x2064_x1580651522}[：接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[的大小，取值范围为]{style="font-family:宋体"}[128]{lang="EN-US"}[～]{style="font-family:宋体"}[2000]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1829153728}

[[当设备收到一个报文后，如果发现报文长度比转发接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_13325_x2064_x1272934000}[值大，则进行下列处理：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果报文不允许分片，则将报文丢弃；]{style="font-family:宋体"}]{#struct_0_13325_x2064_1107255283}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果报文允许分片，则将报文进行分片转发。]{style="font-family:宋体"}]{#struct_0_13325_x2064_1194355499}

[[为了减轻转发设备在传输过程中的分片和重组数据包的压力，更高效的利用网络资源，请]{style="font-family:宋体"}]{#struct_0_13325_x2064_x309610854}[根据实际组网环境设置合适的接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，以减少]{style="font-family:宋体"}[分片的发生。]{style="font-family:宋体"}

[[如果当前接口同时支持]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1484787289}**[mtu]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ip mtu]{lang="EN-US"}**[命令，则设备会以]{style="font-family:宋体"}**[ip mtu]{lang="EN-US"}**[命令配置的接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值对报文进行分片，不会再按照]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值对报文进行分片。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1400183242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13325_x2064_x1140321003}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x63179739}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上发送]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[为]{style="font-family:宋体"}[1280]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x739343125}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip mtu 1280]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13325_x2064_x1889446166}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x715823665}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上发送]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[为]{style="font-family:宋体"}[1280]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x1308592819}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ip mtu 1280]{lang="EN-US"}
:::

::: {#189312183 .myid}
[]{#_Toc404786724}[]{#struct_0_13325_x2064_x1265369605}

**IP性能优化 \-- IP性能优化配置命令 \-- ip reassemble local enable**

------------------------------------------------------------------------

[**[ip reassemble local enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x312626176}[命令用来开启设备的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[分片报文本地重组功能。]{style="font-family:宋体"}

[**[undo ip reassemble local enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x1265435141}[命令用来关闭设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[分片报文本地重组功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1380641756}

[**[ip reassemble local enable]{lang="EN-US"}**]{#struct_0_13325_x2064_1290333126}

[**[undo ip reassemble local enable]{lang="EN-US"}**]{#struct_0_13325_x2064_1619131137}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1745916011}

[[IP]{lang="EN-US"}]{#struct_0_13325_x2064_371623691}[分片报文本地重组功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1408637545}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1265238533}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1971847850}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_204831497}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1832739907}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x321698569}

[[当分布式设备的某块单板收到目的为本设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_1129424500}[分片报文时，需要把分片报文送到主用主控板进行重组，这样会导致报文重组性能较低的问题。当开启]{style="font-family:宋体"}[IP]{lang="EN-US"}[分片报文本地重组功能后，分片报文会在该单板上直接进行报文重组，这样就能提高分片报文的重组性能。]{style="font-family:宋体"}

[[需要说明的是，开启]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_x1265304069}[分片报文本地重组功能后，如果分片报文是从设备上不同的单板进入的，会导致]{style="font-family:宋体"}[IP]{lang="EN-US"}[分片报文本地无法重组成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_318183161}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_633594402}[开启设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[分片报文本地重组功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x876862001}

[\[Sysname\] ip reassemble local enable]{lang="EN-US"}
:::

::: {#-694522530 .myid}
[]{#_Toc404786725}[]{#struct_0_13325_x2064_x1997407334}

**IP性能优化 \-- IP性能优化配置命令 \-- ip redirects enable**

------------------------------------------------------------------------

[**[ip redirects enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x1140124395}[命令用来开启设备的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[重定向报文的发送功能。]{style="font-family:宋体"}

[**[undo ip redirects enable]{lang="EN-US"}**]{#struct_0_13325_x2064_336803972}[命令用来关闭设备的]{style="font-family:
宋体"}[ICMP]{lang="EN-US"}[重定向报文的发送功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1083827445}

[**[ip redirects enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x847254511}

[**[undo ip redirects enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x163496385}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_193518830}

[[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_501791188}[重定向报文发送功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1145339511}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_1508728173}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1140189931}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1570743628}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1164985029}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1737997778}

[[主机启动时，它的路由表中可能只有一条到缺省网关的缺省路由。当满足一定的条件时，缺省网关会向源主机发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_x2106697929}[重定向报文，通知主机重新选择正确的下一跳进行后续报文的发送。]{style="font-family:宋体"}

[[满足下列条件时，设备会发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_x791286623}[重定向报文：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收和转发数据报文的接口是同一接口；]{style="font-family:宋体"}]{#struct_0_13325_x2064_x38269258}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被选择的路由本身没有被]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1982374914}[ICMP]{lang="EN-US"}[重定向报文创建或修改过；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被选择的路由不是设备的默认路由；]{style="font-family:宋体"}]{#struct_0_13325_x2064_878916602}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数据报文中没有源路由选项。]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1139993323}

[[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_723090122}[重定向报文发送功能可以简化主机的管理，使具有很少选路信息的主机逐渐建立较完善的路由表，从而找到最佳路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1514047461}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_6126021}[开启设备的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[重定向报文发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_1709610969}

[\[Sysname\] ip redirects enable]{lang="EN-US"}
:::

::: {#618689887 .myid}
[]{#_Toc404786726}[]{#struct_0_13325_x2064_186786721}[]{#_Toc138239306}[]{#_Toc136679745}

**IP性能优化 \-- IP性能优化配置命令 \-- ip ttl-expires enable**

------------------------------------------------------------------------

[**[ip ttl-expires enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x2074443008}[命令用来开启设备的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[超时报文的发送功能。]{style="font-family:宋体"}

[**[undo ip ttl-expires enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x1565028798}[命令用来关闭设备的]{style="font-family:
宋体"}[ICMP]{lang="EN-US"}[超时报文的发送功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1140058859}

[**[ip ttl-expires enable]{lang="EN-US"}**]{#struct_0_13325_x2064_606391168}

[**[undo ip ttl-expires enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x1525372031}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x667599165}

[[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_x216731411}[超时报文发送功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x542745050}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x925650014}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_772669849}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_470466052}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1139862251}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1548276702}

[[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_1151847112}[超时报文发送功能是在设备收到]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据报文后，如果发生超时差错，则将报文丢弃并给源端发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[超时差错报文。]{style="font-family:宋体"}

[[设备在满足下列条件时会发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_793310155}[超时报文：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备收到]{style="font-family:宋体"}]{#struct_0_13325_x2064_1808893656}[IP]{lang="EN-US"}[数据报文后，如果报文的目的地不是本地且报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[字段是]{style="font-family:宋体"}[1]{lang="EN-US"}[，则发送"]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时"]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备收到目的地址为本地的]{style="font-family:宋体"}]{#struct_0_13325_x2064_1794027082}[IP]{lang="EN-US"}[数据报文的第一个分片后，启动定时器，如果所有分片报文到达之前定时器超时，则会发送"重组超时"]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文。]{style="font-family:宋体"}

[[需要注意的是，关闭]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_1639763263}[超时报文发送功能后，设备不会再发送"]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时"]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文，但"重组超时"]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文仍会正常发送。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1062439246}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1139927787}[开启设备的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[超时报文发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_1740710653}

[\[Sysname\] ip ttl-expires enable]{lang="EN-US"}
:::

::: {#675996977 .myid}
[]{#_Toc404786727}[]{#struct_0_13325_x2064_1393312623}[]{#_Toc138239307}[]{#_Toc136679746}

**IP性能优化 \-- IP性能优化配置命令 \-- ip unreachables enable**

------------------------------------------------------------------------

[**[ip unreachables enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x1069977700}[命令用来开启设备的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[目的不可达报文的发送功能。]{style="font-family:宋体"}

[**[undo ip unreachables enable]{lang="EN-US"}**]{#struct_0_13325_x2064_258822719}[命令用来关闭设备的]{style="font-family:
宋体"}[ICMP]{lang="EN-US"}[目的不可达报文的发送功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_556517510}

[**[ip unreachables enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x2139584081}

[**[undo ip unreachables enable]{lang="EN-US"}**]{#struct_0_13325_x2064_1170234374}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1139731179}

[[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_1072752288}[目的不可达报文发送功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1713249748}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_1130182055}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1412234807}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1530386387}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_750529535}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x940551891}

[[ICMP]{lang="EN-US"}]{#struct_0_13325_x2064_370509267}[目的不可达报文发送功能是在设备收到]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据报文后，如果发生目的不可达的差错，则将报文丢弃并给源端发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[目的不可达差错报文。]{style="font-family:宋体"}

[[设备在满足下列条件时会发送目的不可达报文：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1139796715}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备在转发报文时，如果在路由表中没有找到对应的转发路由，且路由表中没有缺省路由，则给源端发送"网络不可达"]{style="font-family:宋体"}]{#struct_0_13325_x2064_872988452}[ICMP]{lang="EN-US"}[差错报文；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备收到目的地址为本地的数据报文时，如果设备不支持数据报文采用的传输层协议，则给源端发送"协议不可达"]{style="font-family:宋体"}]{#struct_0_13325_x2064_x400131066}[ICMP]{lang="EN-US"}[差错报文；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备收到目的地址为本地、传输层协议为]{style="font-family:宋体"}]{#struct_0_13325_x2064_1891198324}[UDP]{lang="EN-US"}[的数据报文时，如果报文的端口号与正在使用的进程不匹配，则给源端发送"端口不可达"]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[源端如果采用"严格的源路由选择"发送报文，当中间设备发现源路由所指定的下一个设备不在其直接连接的网络上，则给源端发送"源站路由失败"的]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1991920716}[ICMP]{lang="EN-US"}[差错报文；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备在转发报文时，如果转发接口的]{style="font-family:宋体"}]{#struct_0_13325_x2064_565324834}[MTU]{lang="EN-US"}[小于报文的长度，但报文被设置了不可分片，则给源端发送"需要进行分片但设置了不分片比特"]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1541818078}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1866056188}[开启设备的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[目的不可达报文发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x1140255466}

[\[Sysname\] ip unreachables enable]{lang="EN-US"}
:::

::: {#949697493 .myid}
[]{#_Toc138239309}[]{#_Toc136679748}[]{#_Toc69790803}[]{#_Toc39143441}[]{#_Toc27283716}[]{#_Toc404786728}[]{#struct_0_13325_x2064_1711114221}[]{#_Toc271702017}[]{#_Toc138239308}[]{#_Toc136679747}[]{#_Toc366483459}[]{#_Toc366483460}[]{#_Toc366483461}[]{#_Toc366483462}[]{#_Toc366483463}[]{#_Toc366483464}[]{#_Toc366483465}[]{#_Toc366483466}[]{#_Toc366483467}[]{#_Toc366483468}[]{#_Toc366483469}[]{#_Toc366483470}[]{#_Toc366483471}[]{#_Toc366483472}[]{#_Toc366483473}[]{#_Toc366483474}[]{#_Toc366483475}[]{#_Toc366483476}[]{#_Toc366483477}[]{#_Toc366483478}[]{#_Toc366483479}[]{#_Toc366483480}[]{#_Toc366483481}[]{#_Toc366483482}[]{#_Toc366483483}[]{#_Toc366483484}[]{#_Toc366483485}[]{#_Toc366483486}[]{#_Toc366483487}[]{#_Hlt24613669}

**IP性能优化 \-- IP性能优化配置命令 \-- reset ip statistics**

------------------------------------------------------------------------

[**[reset ip statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x688924813}[命令用来清除]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1748887623}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1679756853}

[**[reset ip statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_955740063}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_13325_x2064_x1139993322}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset ip statistics]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_x842993819}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_13325_x2064_x286941927}[模式：]{style="font-family:宋体"}

[**[reset ip statistics]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_13325_x2064_1903737320}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1969062236}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1675084541}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1109423097}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1294422318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1140058858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x959692773}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1199437418}[：清除指定单板的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号]{style="font-family:宋体"}[。如果不指定本参数，则清除所有单板上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x1467524298}[：清除指定成员设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除所有成员设备上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_x630872456}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1010727921}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定成员设备上指定单板的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号]{style="font-family:宋体"}[。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_13325_x2064_1741780539}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[指定单板的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号]{style="font-family:宋体"}[。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_13325_x2064_608182020}[：清除]{style="font-family:宋体"}[指]{style="font-family:宋体"}[定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x2655903}

[[在某些情况下，需要统计一定时间内接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13325_x2064_1858552456}[报文统计信息，这时必须在统计开始前清除原有的统计信息，重新进行统计。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_161364789}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1707837050}[清除]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ip statistics]{lang="EN-US"}]{#struct_0_13325_x2064_x1139862250}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_17807239}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip interface]{lang="EN-US"}**]{#struct_0_13325_x2064_x332729575}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[地址）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x411757838}
:::

::: {#-750411011 .myid}
[]{#_Toc404786729}[]{#struct_0_13325_x2064_x1832302754}

**IP性能优化 \-- IP性能优化配置命令 \-- reset tcp statistics**

------------------------------------------------------------------------

[**[reset tcp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_573327910}[命令用来清除]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的流量统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_455357589}

[**[reset]{lang="EN-US"}**[ **tcp** **statistics**]{lang="EN-US"}]{#struct_0_13325_x2064_x1530803934}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1139927786}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x988172702}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x570598607}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x2108727929}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x497176266}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1102515922}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1075145292}[清除]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset tcp statistics]{lang="EN-US"}]{#struct_0_13325_x2064_1201377970}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_113148381}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display tcp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x1139731178}
:::

::: {#2098536745 .myid}
[]{#_Toc404786730}[]{#struct_0_13325_x2064_x493331653}[]{#_Toc138239310}[]{#_Toc136679749}[]{#_Toc60058943}

**IP性能优化 \-- IP性能优化配置命令 \-- reset udp statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **udp statistics**]{lang="EN-US"}]{#struct_0_13325_x2064_1726066990}[命令用来清除]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1035187550}

[**[reset udp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_x1301094831}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1358389413}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_785553810}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_27439040}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1139796714}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x693095489}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x14974199}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1521646059}[清除]{style="font-family:宋体"}[UDP]{lang="EN-US"}[流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset udp statistics]{lang="EN-US"}]{#struct_0_13325_x2064_x1888109154}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_2044218194}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display udp statistics]{lang="EN-US"}**]{#struct_0_13325_x2064_2118048756}
:::

::: {#-140279334 .myid}
[]{#_Toc145933487}[]{#_Toc404786731}[]{#struct_0_13325_x2064_x805986943}[]{#_Toc271702018}[]{#_Toc138239311}[]{#_Toc136679750}[]{#_Toc95362261}

**IP性能优化 \-- IP性能优化配置命令 \-- tcp mss**

------------------------------------------------------------------------

[**[tcp mss]{lang="EN-US"}**]{#struct_0_13325_x2064_x1418536199}[命令用来配置接口的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[最大报文段长度。]{style="font-family:宋体"}

[**[undo tcp mss]{lang="EN-US"}**]{#struct_0_13325_x2064_x1140255469}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1130312828}

[**[tcp mss ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_13325_x2064_x632788513}

[**[undo tcp mss]{lang="EN-US"}**]{#struct_0_13325_x2064_x2072541300}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1478610315}

[[未配置接口的]{style="font-family:宋体"}]{#struct_0_13325_x2064_x256655957}[TCP]{lang="EN-US"}[最大报文段长度]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_893234119}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_633911921}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_313468785}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1140321005}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_743389315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1614442811}

[*[value]{lang="EN-US"}*]{#struct_0_13325_x2064_x1817699477}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[最大报文段长度，取值范围为]{style="font-family:宋体"}[128]{lang="EN-US"}[～（接口的最大]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值－]{style="font-family:宋体"}[40]{lang="EN-US"}[），单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_966096822}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_1745604070}[最大报文段长度（]{style="font-family:宋体"}[Max Segment Size]{lang="EN-US"}[，]{style="font-family:宋体"}[MSS]{lang="EN-US"}[）表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的对端发往本端的最大]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文段的长度，目前作为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接建立时的一个选项来协商：当一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接建立时，连接的双方要将]{style="font-family:宋体"}[MSS]{lang="EN-US"}[作为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文的一个选项通告给对端，对端会记录下这个]{style="font-family:宋体"}[MSS]{lang="EN-US"}[值，后续在发送]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文时，会限制]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文的大小不超过该]{style="font-family:宋体"}[MSS]{lang="EN-US"}[值。当对端发送的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文的长度小于本端的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[最大报文段长度时，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文不需要分段；否则，对端需要对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文按照最大报文段长度进行分段处理后再发给本端。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13325_x2064_1540845858}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置仅对新建的]{style="font-family:宋体"}]{#struct_0_13325_x2064_1571677441}[TCP]{lang="EN-US"}[连接生效，对于配置前已建立的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置仅对]{style="font-family:宋体"}]{#struct_0_13325_x2064_201685959}[IP]{lang="EN-US"}[报文生效，当接口上配置了]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[功能后，不建议再配置本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1140124397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13325_x2064_1499603386}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x635700574}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[TCP]{lang="EN-US"}[最大报文段长度为]{style="font-family:宋体"}[300]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x206708042}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] tcp mss 300]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13325_x2064_471504473}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x1732722034}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[上]{style="font-family:宋体"}[TCP]{lang="EN-US"}[最大报文段长度为]{style="font-family:宋体"}[300]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x187101128}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] tcp mss 300]{lang="EN-US"}
:::

::: {#-2017149119 .myid}
[]{#struct_0_13325_x2064_x1140189933}[]{#_Toc404786732}[]{#_Toc298765625}

**IP性能优化 \-- IP性能优化配置命令 \-- tcp path-mtu-discovery**

------------------------------------------------------------------------

[**[tcp path-mtu-discovery]{lang="EN-US"}**]{#struct_0_13325_x2064_1561424254}[命令用来开启]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测功能。]{style="font-family:宋体"}

[**[undo tcp path-mtu-discovery]{lang="EN-US"}**]{#struct_0_13325_x2064_1608852912}[命令用来关闭]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[连接的]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1155515988}

[**[tcp path-mtu-discovery]{lang="EN-US"}**[ \[ **aging** *age-time* \| **no-aging** \]]{lang="EN-US"}]{#struct_0_13325_x2064_1661132624}

[**[undo tcp path-mtu-discovery]{lang="EN-US"}**]{#struct_0_13325_x2064_x253608732}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x497051744}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_x1593593694}[连接的]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x34840088}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1139993325}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1529659176}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1611549963}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x822659908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x466871539}

[**[aging]{lang="EN-US"}**[ *age-time*]{lang="EN-US"}]{#struct_0_13325_x2064_664508004}[：]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[的老化时间，]{style="font-family:宋体"}*[age-time]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为分钟，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[**[no-aging]{lang="EN-US"}**]{#struct_0_13325_x2064_x239196588}[：]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[不老化。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1766065966}

[[开启]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_x1140058861}[连接的]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测功能后，新建的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接均会携带]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测属性，可以通过探测机制确定]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[，按照数据路径上的最小]{style="font-family:宋体"}[MTU]{lang="EN-US"}[组织]{style="font-family:宋体"}[TCP]{lang="EN-US"}[分段长度，最大限度利用网络资源，避免]{style="font-family:宋体"}[IP]{lang="EN-US"}[分片的发生。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_962424920}[连接的]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测功能后，系统将停止所有正在运行的]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[定时器，此后创建的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接均无]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测功能，但是对于此前已经建立的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，其]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测功能不会被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1987865372}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1916124534}[开启]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[探测功能，]{style="font-family:宋体"}[Path MTU]{lang="EN-US"}[的老化时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x1309419663}

[\[Sysname\] tcp path-mtu-discovery aging 20]{lang="EN-US"}
:::

::::: {#-2103603074 .myid}
[]{#_Toc404786733}[]{#struct_0_13325_x2064_x999196873}

**IP性能优化 \-- IP性能优化配置命令 \-- tcp syn-cookie enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_13325_x2064_x94564653}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_13325_x2064_x277785109}
:::

[ ]{lang="EN-US"}

[**[tcp syn-cookie enable]{lang="EN-US"}**]{#struct_0_13325_x2064_x1139862253}[命令用来使能]{style="font-family:宋体"}[SYN Cookie]{lang="EN-US"}[功能，防止设备受到]{style="font-family:宋体"}[SYN Flood]{lang="EN-US"}[攻击。]{style="font-family:宋体"}

[**[undo tcp syn-cookie enble]{lang="EN-US"}**]{#struct_0_13325_x2064_x385477288}[命令用来关闭]{style="font-family:
宋体"}[SYN Cookie]{lang="EN-US"}[功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1342659901}

[**[tcp syn-cookie enable]{lang="EN-US"}**]{#struct_0_13325_x2064_1226588023}

[**[undo tcp syn-cookie enable]{lang="EN-US"}**]{#struct_0_13325_x2064_171825171}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x29257524}

[[SYN Cookie]{lang="EN-US"}]{#struct_0_13325_x2064_x883457061}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1144479039}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_1458243110}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1139927789}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1035226869}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1909309123}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1622917758}

[[一般情况下，]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_148329455}[连接的建立需要经过三次握手，一些恶意的攻击者利用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的建立过程进行]{style="font-family:宋体"}[SYN Flood]{lang="EN-US"}[攻击：攻击者向服务器发送大量请求建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文，而不回应服务器的]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文，导致服务器上建立了大量的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[半连接。从而，达到耗费服务器资源，使服务器无法处理正常业务的目的。]{style="font-family:宋体"}

[[SYN Cookie]{lang="EN-US"}]{#struct_0_13325_x2064_x786544093}[功能用来防止]{style="font-family:宋体"}[SYN Flood]{lang="EN-US"}[攻击。当服务器收到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求时，不建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[半连接，而直接向发起者回复]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文。服务器接收到发起者回应的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文后，才建立连接。通过这种方式，可以避免在服务器上建立大量的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[半连接，防止服务器受到]{style="font-family:宋体"}[SYN Flood]{lang="EN-US"}[攻击。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_196286269}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_x59687935}[使能]{style="font-family:宋体"}[SYN Cookie]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x1139731181}

[\[Sysname\] tcp syn-cookie enable]{lang="EN-US"}
:::::

::: {#-126242893 .myid}
[]{#_Toc404786734}[]{#struct_0_13325_x2064_717504968}[]{#_Toc138239312}[]{#_Toc136679751}

**IP性能优化 \-- IP性能优化配置命令 \-- tcp timer fin-timeout**

------------------------------------------------------------------------

[**[tcp timer fin-timeout]{lang="EN-US"}**]{#struct_0_13325_x2064_x928579050}[命令用来配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[的]{style="font-family:宋体"}[finwait]{lang="EN-US"}[定时器超时时间。]{style="font-family:宋体"}

[**[undo tcp timer fin-timeout]{lang="EN-US"}**]{#struct_0_13325_x2064_x350741839}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x113738220}

[**[tcp timer fin-timeout]{lang="EN-US"}**[ *time-value*]{lang="EN-US"}]{#struct_0_13325_x2064_1572370330}

[**[undo tcp timer fin-timeout]{lang="EN-US"}**]{#struct_0_13325_x2064_x1883294426}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_770900639}

[[TCP finwait]{lang="EN-US"}]{#struct_0_13325_x2064_x1139796717}[定时器的超时时间为]{style="font-family:宋体"}[675]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_2035787866}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_652520112}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_383617717}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_214281904}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_2027704260}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1948363558}

[*[time-value]{lang="EN-US"}*]{#struct_0_13325_x2064_1639466947}[：]{style="font-family:宋体"}[TCP finwait]{lang="EN-US"}[定时器的超时时间，取值范围为]{style="font-family:宋体"}[76]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_274344796}

[[当]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_x1140255468}[的连接状态为]{style="font-family:宋体"}[FIN_WAIT_2]{lang="EN-US"}[时，启动]{style="font-family:宋体"}[finwait]{lang="EN-US"}[定时器，如果在定时器超时前没有收到报文，则]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接终止；如果收到]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文，则]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接状态变为]{style="font-family:宋体"}[TIME_WAIT]{lang="EN-US"}[状态；如果收到非]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文，则从收到的最后一个非]{style="font-family:宋体"}[FIN]{lang="EN-US"}[报文开始重新计时，在超时后中止连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1598570527}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1504598027}[配置]{style="font-family:宋体"}[TCP finwait]{lang="EN-US"}[定时器的超时时间为]{style="font-family:宋体"}[800]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x170670048}

[\[Sysname\] tcp timer fin-timeout 800]{lang="EN-US"}
:::

::: {#-1272027163 .myid}
[]{#_Toc404786735}[]{#struct_0_13325_x2064_x308411707}[]{#_Toc138239313}[]{#_Toc136679752}[]{#_Toc69790805}

**IP性能优化 \-- IP性能优化配置命令 \-- tcp timer syn-timeout**

------------------------------------------------------------------------

[**[tcp timer syn-timeout]{lang="EN-US"}**]{#struct_0_13325_x2064_122185213}[命令用来配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[的]{style="font-family:宋体"}[synwait]{lang="EN-US"}[定时器超时时间。]{style="font-family:宋体"}

[**[undo tcp timer syn-timeout]{lang="EN-US"}**]{#struct_0_13325_x2064_x1371988977}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1060596468}

[**[tcp timer syn-timeout]{lang="EN-US"}**[ *time-value*]{lang="EN-US"}]{#struct_0_13325_x2064_x1140321004}

[**[undo tcp timer syn-timeout]{lang="EN-US"}**]{#struct_0_13325_x2064_x1985494040}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_314357540}

[[TCP synwait]{lang="EN-US"}]{#struct_0_13325_x2064_890232296}[定时器的超时时间为]{style="font-family:宋体"}[75]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x338013024}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x47622580}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1510711378}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1106460068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_43262820}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1140124396}

[*[time-value]{lang="EN-US"}*]{#struct_0_13325_x2064_x1229279969}[：]{style="font-family:宋体"}[TCP synwait]{lang="EN-US"}[定时器的超时时间，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1861608943}

[[当发送]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_13325_x2064_x42422610}[报文时，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[启动]{style="font-family:宋体"}[synwait]{lang="EN-US"}[定时器和重传]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文定时器，当]{style="font-family:宋体"}[synwait]{lang="EN-US"}[定时器超时且]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文重传未达到最大次数时，如果设备未收到回应报文，则]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接建立不成功；当]{style="font-family:宋体"}[synwait]{lang="EN-US"}[定时器未超时但是]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文重传达到最大次数时，如果设备未收到回应报文，则]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接建立不成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_590681984}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_2100308717}[配置]{style="font-family:宋体"}[TCP synwait]{lang="EN-US"}[定时器的超时时间为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_792837021}

[\[Sysname\] tcp timer syn-timeout 80]{lang="SV"}
:::

::: {#1923602995 .myid}
[]{#_Toc404786736}[]{#struct_0_13325_x2064_473635322}[]{#_Toc138239314}[]{#_Toc136679753}[]{#_Toc69790806}

**IP性能优化 \-- IP性能优化配置命令 \-- tcp window**

------------------------------------------------------------------------

[**[tcp window]{lang="EN-US"}**]{#struct_0_13325_x2064_x1140189932}[命令用来设置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的收发缓冲区大小。]{style="font-family:宋体"}

[**[undo tcp window]{lang="EN-US"}**]{#struct_0_13325_x2064_x1167459101}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13325_x2064_663277369}

[**[tcp window]{lang="EN-US"}**[ *window-size*]{lang="EN-US"}]{#struct_0_13325_x2064_x1620677854}

[**[undo tcp window]{lang="EN-US"}**]{#struct_0_13325_x2064_577726322}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x1103652643}

[[TCP]{lang="EN-US"}]{#struct_0_13325_x2064_824072735}[连接的收发缓冲区大小为]{style="font-family:宋体"}[64KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x54847920}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13325_x2064_x1139993324}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13325_x2064_x36424765}

[[network-admin]{lang="EN-US"}]{#struct_0_13325_x2064_1100763354}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13325_x2064_x1531859213}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13325_x2064_1773090697}

[*[window-size]{lang="EN-US"}*]{#struct_0_13325_x2064_718681343}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的收发缓冲区大小，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}[（千字节）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13325_x2064_632810070}

[[\# ]{lang="EN-US"}]{#struct_0_13325_x2064_1409619450}[设置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的收发缓冲区大小为]{style="font-family:宋体"}[3KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13325_x2064_x622052074}

[\[Sysname\] tcp window 3]{lang="EN-US"}
:::
