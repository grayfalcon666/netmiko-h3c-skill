::::: {#1352125841 .myid}
[]{#_Toc404784277}[]{#struct_0_x1084_x1162_x767979146}[]{#_Toc247450132}

**VLAN终结 \-- VLAN终结配置命令 \-- dot1q ethernet-type**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VLAN终结命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1084_x1162_x426446489}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x699983830}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x1610954567}
:::

**[ ]{lang="EN-US"}**

[**[dot1q ethernet-type]{lang="EN-US"}**]{#struct_0_x1084_x1162_694793552}[命令用来配置当前接口接收和发送的报文最外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo dot1q ethernet-type]{lang="EN-US"}**]{#struct_0_x1084_x1162_x1931818715}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_299741068}

[**[dot1q ethernet-type]{lang="EN-US"}**[ *hex-value*]{lang="EN-US"}]{#struct_0_x1084_x1162_x623700712}

[**[undo dot1q ethernet-type]{lang="EN-US"}**]{#struct_0_x1084_x1162_2134573433}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x10322603}

[[当前接口接收或发送的报文最外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x1084_x1162_1460525555}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x8100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_650943021}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1084_x1162_1526072703}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层虚拟以太网接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x159769323}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_2131370731}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_x1681324040}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_987355688}

[*[hex-value]{lang="EN-US"}*]{#struct_0_x1084_x1162_x880472538}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[（]{style="font-family:宋体"}[Tag Protocol Identifier]{lang="EN-US"}[，标签协议标识符）值，为]{style="font-family:宋体"}[4]{lang="EN-US"}[个字符长度的十六进制数字，取值范围为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFF]{lang="EN-US"}[，但不允许配置为]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1352125841#_Ref154730745)[中列举的常用协议类型值。]{style="font-family:宋体"}

[]{#struct_0_x1084_x1162_x623504104}[[表1-1 ]{lang="EN-US"}[常用协议类型值]{style="font-family:
黑体"}]{#_Ref154730745}

[]{#table_struct_0_x1170019067}[[协议]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x573755700}
:::::

[[协议类型值]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1889247118}

[[ARP]{lang="EN-US"}]{#struct_0_x1084_x1162_326520581}

[[0x0806]{lang="EN-US"}]{#struct_0_x1084_x1162_x988573170}

[[PUP]{lang="EN-US"}]{#struct_0_x1084_x1162_x989540301}

[[0x0200]{lang="EN-US"}]{#struct_0_x1084_x1162_x1777908533}

[[RARP]{lang="EN-US"}]{#struct_0_x1084_x1162_x1569342298}

[[0x8035]{lang="EN-US"}]{#struct_0_x1084_x1162_x623569640}

[[IP]{lang="EN-US"}]{#struct_0_x1084_x1162_x1018750289}

[[0x0800]{lang="EN-US"}]{#struct_0_x1084_x1162_x66994813}

[[IPv6]{lang="EN-US"}]{#struct_0_x1084_x1162_1970371793}

[[0x86DD]{lang="EN-US"}]{#struct_0_x1084_x1162_x1340424056}

[[PPPoE]{lang="EN-US"}]{#struct_0_x1084_x1162_x197022164}

[[0x8863/0x8864]{lang="EN-US"}]{#struct_0_x1084_x1162_x624028395}

[[MPLS]{lang="EN-US"}]{#struct_0_x1084_x1162_1596106052}

[[0x8847/0x8848]{lang="EN-US"}]{#struct_0_x1084_x1162_488522182}

[[IPX/SPX]{lang="EN-US"}]{#struct_0_x1084_x1162_727177038}

[[0x8137]{lang="EN-US"}]{#struct_0_x1084_x1162_x1408820556}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1084_x1162_x762646298}

[[0x8000]{lang="EN-US"}]{#struct_0_x1084_x1162_x624093931}

[[LACP]{lang="EN-US"}]{#struct_0_x1084_x1162_x331588025}

[[0x8809]{lang="EN-US"}]{#struct_0_x1084_x1162_1246922570}

[[LLDP]{lang="EN-US"}]{#struct_0_x1084_x1162_1495357820}

[[0x88CC]{lang="EN-US"}]{#struct_0_x1084_x1162_1258016109}

[[802.1X]{lang="EN-US"}]{#struct_0_x1084_x1162_300312943}

[[0x888E]{lang="EN-US"}]{#struct_0_x1084_x1162_x623897323}

[[802.1ag]{lang="EN-US"}]{#struct_0_x1084_x1162_x1376416446}

[[0x8902]{lang="EN-US"}]{#struct_0_x1084_x1162_1228932396}

[[集群]{style="font-family:宋体"}]{#struct_0_x1084_x1162_x742777864}

[[0x]{lang="EN-US"}]{#struct_0_x1084_x1162_508283499}[88A]{lang="EN-US"}[7]{lang="EN-US"}

[[设备保留]{style="font-family:宋体"}]{#struct_0_x1084_x1162_x623962859}

[[0xFFFD/0xFFFE/0xFFFF]{lang="EN-US"}]{#struct_0_x1084_x1162_x558372115}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x2012280560}

[[配置]{style="font-family:宋体"}**[dot1q ethernet-type]{lang="EN-US"}**]{#struct_0_x1084_x1162_x1336353340}[命令后，当接收报文时，只有报文最外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x8100]{lang="EN-US"}[或者指定值的报文才会作为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文来处理；发送报文时，会给报文最外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值填入指定值，如果报文带有两层及以上]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，则给报文其他层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值都填入]{style="font-family:宋体"}[0x8100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1084_x1162_x1016875780}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能在三层以太网主接口、三层聚合主接口、三层虚拟以太网主接口、]{style="font-family:宋体"}]{#struct_0_x1084_x1162_x1494491769}[L3VE]{lang="EN-US"}[主接口和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口下配置，不能在子接口上配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在三层以太网接口、三层聚合接口、三层虚拟以太网接口或]{style="font-family:宋体"}]{#struct_0_x1084_x1162_634564778}[L3VE]{lang="EN-US"}[视图下配置，会对相应接口的所有子接口生效；在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口视图下配置，会对该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x2088706532}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_648317000}[设置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下所有子接口能够接收和发送外层]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x9100]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x623766251}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dot1q ethernet-type 9100]{lang="EN-US"}

::::: {#219850183 .myid}
[]{#_Toc404784278}[]{#struct_0_x1084_x1162_x1736435641}[]{#_Toc247450133}

**VLAN终结 \-- VLAN终结配置命令 \-- second-dot1q**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VLAN终结命令.files/image001.png){#图片 2 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1084_x1162_1733135796}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x1836134933}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x1020834662}
:::

**[ ]{lang="EN-US"}**

[**[second-dot1q]{lang="EN-US"}**]{#struct_0_x1084_x1162_243049896}[命令用来使能当前接口的]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[终结功能，并指定当前接口可以终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[（第一层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[等于当前接口的编号，不能配置）。]{style="font-family:宋体"}

[**[undo second-dot1q]{lang="EN-US"}**]{#struct_0_x1084_x1162_1337961972}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1822974116}

[**[second-dot1q ]{lang="EN-US"}**[{ *vlan-id-list* \| **any** } \[ **loose** \]]{lang="EN-US"}]{#struct_0_x1084_x1162_1832531467}

[**[undo second-dot1q]{lang="EN-US"}**[ { *vlan-id-list* \| **any** } \[ **loose** \]]{lang="EN-US"}]{#struct_0_x1084_x1162_2043060183}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x623831787}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1084_x1162_571111038}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1057098743}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1084_x1162_1703027730}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层虚拟以太网子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_1799389629}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_1409564506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_581498291}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_1456474597}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1084_x1162_1491948072}[：当前接口能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_x1084_x1162_x831409487}[：表示当前接口可以终结第一层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为接口编号，第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[中任意值的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[loose]{lang="EN-US"}**]{#struct_0_x1084_x1162_x623635179}[：表示当前接口支持接收并终结携带两层或两层以上]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x2137742389}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_x2109696253}[配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.10]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[；配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.12]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[；配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.100]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[4094]{lang="EN-US"}[中任意值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_861436617}

[\[Sysname\] interface gigabitethernet 1/0/1.10]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.10\] second-dot1q 10 to 20]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.10\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1.12]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.12\] second-dot1q 100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.12\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1.100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] second-dot1q any]{lang="EN-US"}

[[通过以上配置，子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.10]{lang="EN-US"}]{#struct_0_x1084_x1162_82184263}[、]{style="font-family:宋体"}[GigabitEthernet1/0/1.12]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/1.100]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文规格如下：]{style="font-family:宋体"}

[]{#table_struct_0_x1173417531}[[子接口]{style="font-family:黑体"}]{#struct_0_x1084_x1162_577429347}
:::::

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x980313894}[报文的第一层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x623700715}[报文的第二层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[GigabitEthernet1/0/1.10]{lang="EN-US"}]{#struct_0_x1084_x1162_2134114681}

[[10]{lang="EN-US"}]{#struct_0_x1084_x1162_x1147718187}

[[10]{lang="EN-US"}]{#struct_0_x1084_x1162_353986630}[～]{style="font-family:宋体"}[20]{lang="EN-US"}

[[GigabitEthernet1/0/1.12]{lang="EN-US"}]{#struct_0_x1084_x1162_x942923270}

[[12]{lang="EN-US"}]{#struct_0_x1084_x1162_1396088083}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x904743987}

[[GigabitEthernet1/0/1.100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1650688782}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x623504107}

[[1]{lang="EN-US"}]{#struct_0_x1084_x1162_x573690164}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_x1892416830}[配置]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[；配置]{style="font-family:宋体"}[Vlan-interface12]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[；配置]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[4094]{lang="EN-US"}[中任意值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x1343488564}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] second-dot1q 10 to 20]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 12]{lang="EN-US"}

[\[Sysname-Vlan-interface12\] second-dot1q 100]{lang="EN-US"}

[\[Sysname-Vlan-interface12\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] second-dot1q any]{lang="EN-US"}

[[通过以上配置，]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}]{#struct_0_x1084_x1162_1705083372}[、]{style="font-family:宋体"}[Vlan-interface12]{lang="EN-US"}[和]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文规格如下：]{style="font-family:宋体"}

[]{#table_struct_0_x1171524195}[[接口]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x236671147}

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x623569643}[报文的第一层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x1018946897}[报文的第二层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[Vlan-interface10]{lang="EN-US"}]{#struct_0_x1084_x1162_160892434}

[[10]{lang="EN-US"}]{#struct_0_x1084_x1162_415888690}

[[10]{lang="EN-US"}]{#struct_0_x1084_x1162_1744655108}[～]{style="font-family:宋体"}[20]{lang="EN-US"}

[[Vlan-interface12]{lang="EN-US"}]{#struct_0_x1084_x1162_1515972034}

[[12]{lang="EN-US"}]{#struct_0_x1084_x1162_426908360}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x624028394}

[[Vlan-interface100]{lang="EN-US"}]{#struct_0_x1084_x1162_1596171588}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x293608470}

[[1]{lang="EN-US"}]{#struct_0_x1084_x1162_335249808}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_442745315}[配置]{style="font-family:宋体"}[Virtual-Ethernet1.10]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[；配置]{style="font-family:宋体"}[Virtual-Ethernet1.20]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[；配置]{style="font-family:宋体"}[Virtual-Ethernet1.100]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[4094]{lang="EN-US"}[中任意值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x624093930}

[\[Sysname\] interface virtual-ethernet 1.10]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.10\] second-dot1q 10 to 20]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.10\] quit]{lang="EN-US"}

[\[Sysname\] interface virtual-ethernet 1.20]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.20\] second-dot1q 100]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.20\] quit]{lang="EN-US"}

[\[Sysname\] interface virtual-ethernet 1.100]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.100\] second-dot1q any]{lang="EN-US"}

[[通过以上配置，]{style="font-family:宋体"}[Virtual-Ethernet1.10]{lang="EN-US"}]{#struct_0_x1084_x1162_x331653561}[、]{style="font-family:宋体"}[Virtual-Ethernet1.20]{lang="EN-US"}[和]{style="font-family:宋体"}[Virtual-Ethernet1.100]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文规格如下：]{style="font-family:宋体"}

[]{#table_struct_0_x1144493739}[[子接口]{style="font-family:黑体"}]{#struct_0_x1084_x1162_535451506}

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x387920531}[报文的第一层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_136004942}[报文的第二层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[Virtual-Ethernet 1.10]{lang="EN-US"}]{#struct_0_x1084_x1162_x131456111}

[[10]{lang="EN-US"}]{#struct_0_x1084_x1162_1828845916}

[[10]{lang="EN-US"}]{#struct_0_x1084_x1162_1038472454}[～]{style="font-family:宋体"}[20]{lang="EN-US"}

[[Virtual-Ethernet 1.20]{lang="EN-US"}]{#struct_0_x1084_x1162_x2034500152}

[[20]{lang="EN-US"}]{#struct_0_x1084_x1162_x623897322}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1376481982}

[[Virtual-Ethernet 1.100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1610871306}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x742752699}

[[1]{lang="EN-US"}]{#struct_0_x1084_x1162_1256007745}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}

[ ]{lang="EN-US"}

::::: {#-921006161 .myid}
[]{#_Toc404784279}[]{#struct_0_x1084_x1162_440403956}

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-termination broadcast enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[]{lang="EN-US"}]{#struct_0_x1084_x1162_439945204}[![说明](VLAN终结命令.files/image001.png){#图片 5 border="0" width="62" height="25"}]{lang="EN-US"}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本特性的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x308782340}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_1279658059}
:::

**[ ]{lang="EN-US"}**

[**[vlan-termination broadcast enable]{lang="EN-US"}**]{#struct_0_x1084_x1162_1587908584}[命令用来配置允许当前接口发送广播和组播报文，即允许当前接口遍历模糊终结的范围发送报文，具体为当前接口遍历模糊终结范围内的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，给报文分别添加这些]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[对应的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[后发送（比如，对于配置了模糊的]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[终结的接口，报文添加]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[后，最外两层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[分别对应各自模糊终结范围内的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[undo vlan-termination broadcast enable]{lang="EN-US"}**]{#struct_0_x1084_x1162_x358952582}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_1656097216}

[**[vlan-termination broadcast enable]{lang="EN-US"}**]{#struct_0_x1084_x1162_x988613420}

[**[undo vlan-termination broadcast enable]{lang="EN-US"}**]{#struct_0_x1084_x1162_204329103}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1642681427}

[[当前接口配置了模糊的]{style="font-family:宋体"}[Dot1q]{lang="EN-US"}]{#struct_0_x1084_x1162_1652358866}[终结或者模糊的]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[终结功能后，不允许发送广播、组播报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_440010740}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1084_x1162_x2002031529}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层虚拟以太网子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_1333450276}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_795546772}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_x1316038040}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1439177503}

[[在接口配置了模糊终结功能时，建议用户同时配置该命令，以允许接口遍历模糊终结的范围发送报文。如果出于系统性能考虑，不允许接口遍历模糊终结的范围发送报文，则不要配置该命令。]{style="font-family:宋体"}]{#struct_0_x1084_x1162_1526798603}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_962058326}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_x2062045389}[配置允许子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.10]{lang="EN-US"}[遍历模糊]{style="font-family:宋体"}[Dot1q]{lang="EN-US"}[终结范围发送广播、组播报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x1572296}

[\[Sysname\] interface gigabitethernet 1/0/1.10]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.10\] vlan-type dot1q vid 10 to 20]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.10\] vlan-termination broadcast enable]{lang="EN-US"}

[[通过以上配置，当子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.10]{lang="EN-US"}]{#struct_0_x1084_x1162_x2147138553}[发送广播、组播报文的时候，给报文封装]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[（遍历范围]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[）后发送。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_440076276}[配置允许子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.10]{lang="EN-US"}[遍历模糊]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[终结范围发送广播、组播报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x800905704}

[\[Sysname\] interface gigabitethernet 1/0/1.10]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.10\] vlan-type dot1q vid 300 to 400 second-dot1q 500 to 600]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.10\] vlan-termination broadcast enable]{lang="EN-US"}

[[通过以上配置，当子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.10]{lang="EN-US"}]{#struct_0_x1084_x1162_1901410510}[发送广播、组播报文的时候，给报文封装]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[（内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[遍历范围]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[遍历范围]{style="font-family:宋体"}[300]{lang="EN-US"}[～]{style="font-family:宋体"}[400]{lang="EN-US"}[）后发送。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_1717904229}[配置允许接口]{style="font-family:宋体"}[Vlan-interface 10]{lang="EN-US"}[遍历终结范围发送广播、组播报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x643246485}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] second-dot1q 10 to 20]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] vlan-termination broadcast enable]{lang="EN-US"}

[[通过以上配置，当接口]{style="font-family:宋体"}[Vlan-interface 10]{lang="EN-US"}]{#struct_0_x1084_x1162_1093555457}[发送广播、组播报文的时候，给报文封装两层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[（内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[遍历范围]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[，外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[对应]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[）后发送。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_420722136}[配置允许子接口]{style="font-family:宋体"}[Virtual-Ethernet1.10]{lang="EN-US"}[遍历终结范围发送广播、组播报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_908231626}

[\[Sysname\] interface virual-ethernet 1.10]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.10\] vlan-type dot1q vid 10 to 20]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.10\] vlan-termination broadcast enable]{lang="EN-US"}

[[通过以上配置，当子接口]{style="font-family:宋体"}[Virtual-Ethernet1.10]{lang="EN-US"}]{#struct_0_x1084_x1162_440141812}[发送广播、组播报文的时候，给报文封装]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[（遍历范围]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[）后发送。]{style="font-family:宋体"}
:::::

::::: {#-214786114 .myid}
[]{#_Toc404784280}[]{#struct_0_x1084_x1162_x2030324671}

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-type dot1q default**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VLAN终结命令.files/image001.png){#图片 7 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1084_x1162_1350375708}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_270917165}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x964719713}
:::

**[ ]{lang="EN-US"}**

[**[vlan-type dot1q default]{lang="EN-US"}**]{#struct_0_x1084_x1162_229568811}[命令用来使能当前接口的]{style="font-family:宋体"}[Default]{lang="EN-US"}[终结功能，使当前接口可以处理其他子接口都无法处理的报文。]{style="font-family:宋体"}

[**[undo vlan-type dot1q default]{lang="EN-US"}**]{#struct_0_x1084_x1162_1774233495}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1002788388}

[**[vlan-type dot1q default]{lang="EN-US"}**]{#struct_0_x1084_x1162_x805553938}

[**[undo vlan-type dot1q default]{lang="EN-US"}**]{#struct_0_x1084_x1162_x1034126169}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_1899151065}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1084_x1162_440731636}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x802752520}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1084_x1162_626657361}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层虚拟以太网子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x1084_x1162_6591314}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_473569908}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_x1202900718}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x775270024}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_575603162}[配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[Default]{lang="EN-US"}[终结功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x1232298125}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q default]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] quit]{lang="EN-US"}

[[通过以上配置，子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_440797172}[能够处理其他子接口都无法处理的报文。]{style="font-family:宋体"}
:::::

::::: {#-970816794 .myid}
[]{#_Toc404784281}[]{#struct_0_x1084_x1162_2982459}

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-type dot1q untagged**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VLAN终结命令.files/image001.png){#图片 6 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1084_x1162_x625854693}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x1108463752}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_705601755}
:::

**[ ]{lang="EN-US"}**

[**[vlan-type dot1q untagged]{lang="EN-US"}**]{#struct_0_x1084_x1162_x2117739695}[命令用来使能当前接口的]{style="font-family:
宋体"}[Untagged]{lang="EN-US"}[终结功能，使当前接口可以处理不带]{style="font-family:
宋体"}[VLAN Tag]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[**[undo vlan-type dot1q untagged]{lang="EN-US"}**]{#struct_0_x1084_x1162_x357166097}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x2055195043}

[**[vlan-type dot1q untagged]{lang="EN-US"}**]{#struct_0_x1084_x1162_295248849}

[**[undo vlan-type dot1q untagged]{lang="EN-US"}**]{#struct_0_x1084_x1162_359316965}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_440207347}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1084_x1162_241605191}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x635534326}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1084_x1162_1383272457}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层虚拟以太网子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1986752895}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_818078146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_x552204915}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1550114949}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_2098472656}[配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[Untagged]{lang="EN-US"}[终结功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x1906023561}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q untagged]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] quit]{lang="EN-US"}

[[通过以上配置，子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_1215072960}[能够接收不带]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的报文。]{style="font-family:宋体"}
:::::

::::: {#-1066197964 .myid}
[]{#_Toc404784282}[]{#struct_0_x1084_x1162_x1876953896}[]{#_Toc247450134}

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-type dot1q vid**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VLAN终结命令.files/image001.png){#图片 3 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1084_x1162_x1878791907}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x2100296825}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x623962858}
:::

**[ ]{lang="EN-US"}**

[**[vlan-type dot1q vid]{lang="EN-US"}**]{#struct_0_x1084_x1162_x558306579}[命令用来使能当前接口的]{style="font-family:宋体"}[Dot1q]{lang="EN-US"}[终结功能，并指定当前接口能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的最外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围。]{style="font-family:宋体"}

[**[undo vlan-type dot1q vid]{lang="EN-US"}**]{#struct_0_x1084_x1162_x813812066}[命令用来取消当前接口的]{style="font-family:
宋体"}[Dot1q]{lang="EN-US"}[终结功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_1149168105}

[**[vlan-type dot1q vid ]{lang="EN-US"}***[vlan-id-list ]{lang="EN-US"}*[\[ **loose** \]]{lang="EN-US"}]{#struct_0_x1084_x1162_x1120868209}

[**[undo vlan-type dot1q vid ]{lang="EN-US"}***[vlan-id-list ]{lang="EN-US"}*[\[ **loose** \]]{lang="EN-US"}]{#struct_0_x1084_x1162_x1203927547}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_15467498}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1084_x1162_831802763}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x913140920}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1084_x1162_x623766250}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层虚拟以太网子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1736370105}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_x1817252695}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_x2098802134}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_475122858}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1084_x1162_1880274223}[：当前接口能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的最外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[loose]{lang="EN-US"}**]{#struct_0_x1084_x1162_147933726}[：表示当前接口支持接收携带一层或一层以上]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的报文。本参数的支持情况与设备型号有关，请以设备的实际型号为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1346929617}

[[同一以太网主接口下的不同子接口不能终结同一种]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x305191953}[报文，即同一主接口下各子接口指定的]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[不能存在交集。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x739285641}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_x623831786}[配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[能够终结最外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[在范围]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[内的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_571045502}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q vid 2 to 100]{lang="EN-US"}

[[通过以上配置，当子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_x296725897}[收到的报文的最外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[在范围]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[内时，就会对该报文进行终结处理。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_2045084706}[配置子接口]{style="font-family:宋体"}[Virtual-Ethernet1.1]{lang="EN-US"}[能够终结最外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[在范围]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[内的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_970024169}

[\[Sysname\] interface virtual-ethernet 1.1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.1\] vlan-type dot1q vid 2 to 100]{lang="EN-US"}

[[通过以上配置，当子接口]{style="font-family:宋体"}[Virtual-Ethernet1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_386643543}[收到的报文的最外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[在范围]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[内时，就会对该报文进行终结处理。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_1431540434}[配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[能够终结最外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[的带有一层或一层以上]{style="font-family:
宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文。配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.2]{lang="EN-US"}[能够终结最外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x623635178}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q vid 2 loose]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1.2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.2\] vlan-type dot1q vid 3 ]{lang="EN-US"}

[]{#table_struct_0_x1142461749}[[子接口]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x2137807925}
:::::

[[允许终结的最外层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1084_x1162_368593289}

[[是否允许终结携带一层以上]{style="font-family:黑体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x1084_x1162_211322025}[的报文]{style="font-family:黑体"}

[[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_1219360863}

[[2]{lang="EN-US"}]{#struct_0_x1084_x1162_31065414}

[[是]{style="font-family:宋体"}]{#struct_0_x1084_x1162_x952596341}

[[GigabitEthernet1/0/1.2]{lang="EN-US"}]{#struct_0_x1084_x1162_x837940}

[[3]{lang="EN-US"}]{#struct_0_x1084_x1162_x623700714}

[[否]{style="font-family:宋体"}]{#struct_0_x1084_x1162_2134180217}

[ ]{lang="EN-US"}

::::: {#166893560 .myid}
[]{#_Toc404784283}[]{#struct_0_x1084_x1162_402524216}[]{#_Toc247450135}

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-type dot1q vid second-dot1q**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VLAN终结命令.files/image001.png){#图片 4 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1084_x1162_x695859109}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_x1213526731}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1084_x1162_531253322}
:::

**[ ]{lang="EN-US"}**

[**[vlan-type dot1q vid second-dot1q]{lang="EN-US"}**]{#struct_0_x1084_x1162_1449760435}[命令用来使能子接口的]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[终结功能，并指定当前接口可以终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的最外两层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vlan-type dot1q vid second-dot1q]{lang="EN-US"}**]{#struct_0_x1084_x1162_29705080}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x838303724}

[**[vlan-type dot1q vid]{lang="EN-US"}**[ *vlan-id-list* **second-dot1q** { *vlan-id-list* \| **any** } \[ **loose** \]]{lang="EN-US"}]{#struct_0_x1084_x1162_x623504106}

[**[undo vlan-type dot1q vid ]{lang="EN-US"}***[vlan-id-list]{lang="EN-US"}*[ **second-dot1q** { *vlan-id-list* \| **any** } \[ **loose** \]]{lang="EN-US"}]{#struct_0_x1084_x1162_x573624628}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1115171542}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1084_x1162_1476193433}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x391140990}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1084_x1162_x115137125}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层虚拟以太网子接口视图]{style="font-family:宋体"}[/L3VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x2038282573}

[[network-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_1907053445}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1084_x1162_2124132179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1298132947}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1084_x1162_274950741}[：]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_x1084_x1162_1470520760}[：表示当前接口可以终结第一层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为指定值，第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[中任意值的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[loose]{lang="EN-US"}**]{#struct_0_x1084_x1162_x1089998735}[：表示当前接口支持接收携带两层或两层以上]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x490754123}

[[同一以太网主接口下的不同子接口不能终结同一种]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x891619146}[报文，如果为两个子接口配置了相同的第一层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，则第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围不能有交叉。需要注意的是，如果这两个子接口的第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[各配置为]{style="font-family:宋体"}*[vlan-id-list1]{lang="EN-US"}*[和]{style="font-family:宋体"}**[any]{lang="EN-US"}**[，]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[范围内除]{style="font-family:宋体"}*[vlan-id-list1]{lang="EN-US"}*[的其他任意]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x825357064}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_x1743680414}[使能三层以太网子接口的]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[终结功能，并指定子接口可以终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的最外两层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_1107738799}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x624028397}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q vid 100 second-dot1q 100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.2]{lang="EN-US"}]{#struct_0_x1084_x1162_1595974980}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[200]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1.2]{lang="EN-US"}]{#struct_0_x1084_x1162_x1693701639}

[\[Sysname-GigabitEthernet1/0/1.2\] vlan-type dot1q vid 100 second-dot1q 200 to 300]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.2\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.3]{lang="EN-US"}]{#struct_0_x1084_x1162_x2123779865}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[any]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1.3]{lang="EN-US"}]{#struct_0_x1084_x1162_x1400598903}

[\[Sysname-GigabitEthernet1/0/1.3\] vlan-type dot1q vid 100 second-dot1q any]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.3\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.4]{lang="EN-US"}]{#struct_0_x1084_x1162_942088618}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[600]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1.4]{lang="EN-US"}]{#struct_0_x1084_x1162_42166578}

[\[Sysname-GigabitEthernet1/0/1.4\] vlan-type dot1q vid 100 second-dot1q 500 to 600]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.4\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.5]{lang="EN-US"}]{#struct_0_x1084_x1162_x1940559514}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[200]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[600]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1.5]{lang="EN-US"}]{#struct_0_x1084_x1162_x624093933}

[\[Sysname-GigabitEthernet1/0/1.5\] vlan-type dot1q vid 200 second-dot1q 500 to 600]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.5\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.6]{lang="EN-US"}]{#struct_0_x1084_x1162_1470389688}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[400]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1.6]{lang="EN-US"}]{#struct_0_x1084_x1162_x335209553}

[\[Sysname-GigabitEthernet1/0/1.6\] vlan-type dot1q vid 300 to 400 second-dot1q 100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.6\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.7]{lang="EN-US"}]{#struct_0_x1084_x1162_1791758889}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[400]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[600]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1.7]{lang="EN-US"}]{#struct_0_x1084_x1162_1470848440}

[\[Sysname-GigabitEthernet1/0/1.7\] vlan-type dot1q vid 300 to 400 second-dot1q 500 to 600]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.7\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.8]{lang="EN-US"}]{#struct_0_x1084_x1162_x1486188757}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[400]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[any]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface gigabitethernet 1/0/1.8]{lang="EN-US"}]{#struct_0_x1084_x1162_x4588223}

[\[Sysname-GigabitEthernet1/0/1.8\] vlan-type dot1q vid 300 to 400 second-dot1q any]{lang="EN-US"}

[[通过以上配置，子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_x331719097}[～]{style="font-family:宋体"}[GigabitEthernet1/0/1.8]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文规格如下：]{style="font-family:宋体"}

[]{#table_struct_0_x1149132507}[[子接口]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x1471802628}
:::::

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_1631292217}[报文的第一层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x1935409517}[报文的第二层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_x1144004939}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1551777624}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1891412701}

[[GigabitEthernet1/0/1.2]{lang="EN-US"}]{#struct_0_x1084_x1162_x623897325}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1376547518}

[[200]{lang="EN-US"}]{#struct_0_x1084_x1162_93106096}[～]{style="font-family:宋体"}[300]{lang="EN-US"}

[[GigabitEthernet1/0/1.3]{lang="EN-US"}]{#struct_0_x1084_x1162_1120675467}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1410083385}

[[1]{lang="EN-US"}]{#struct_0_x1084_x1162_875631333}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[、]{style="font-family:宋体"}[101]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[、]{style="font-family:宋体"}[301]{lang="EN-US"}[～]{style="font-family:宋体"}[499]{lang="EN-US"}[、]{style="font-family:宋体"}[601]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[（即]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[范围内除]{style="font-family:宋体"}[100]{lang="EN-US"}[、]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[和]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[的值）]{style="font-family:宋体"}

[[GigabitEthernet1/0/1.4]{lang="EN-US"}]{#struct_0_x1084_x1162_x623962861}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x557847824}

[[500]{lang="EN-US"}]{#struct_0_x1084_x1162_901890769}[～]{style="font-family:宋体"}[600]{lang="EN-US"}

[[GigabitEthernet1/0/1.5]{lang="EN-US"}]{#struct_0_x1084_x1162_x556296022}

[[200]{lang="EN-US"}]{#struct_0_x1084_x1162_1287075394}

[[500]{lang="EN-US"}]{#struct_0_x1084_x1162_1485815408}[～]{style="font-family:宋体"}[600]{lang="EN-US"}

[[GigabitEthernet1/0/1.6]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258624736}

[[300]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258690272}[～]{style="font-family:宋体"}[400]{lang="EN-US"}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x764418349}

[[GigabitEthernet1/0/1.7]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258755808}

[[300]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258297056}[～]{style="font-family:宋体"}[400]{lang="EN-US"}

[[500]{lang="EN-US"}]{#struct_0_x1084_x1162_899725629}[～]{style="font-family:宋体"}[600]{lang="EN-US"}

[[GigabitEthernet1/0/1.8]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258362592}

[[300]{lang="EN-US"}]{#struct_0_x1084_x1162_1066281271}[～]{style="font-family:宋体"}[400]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258428128}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[、]{style="font-family:宋体"}[101]{lang="EN-US"}[～]{style="font-family:宋体"}[499]{lang="EN-US"}[、]{style="font-family:宋体"}[601]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[（即]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[范围内除]{style="font-family:宋体"}[100]{lang="EN-US"}[和]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[的值）]{style="font-family:宋体"}

[]{#_Toc202081438}[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_269532529}[使能三层虚拟以太网子接口的]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[终结功能，并指定子接口可以终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的最外两层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[Virtual-Ethernet1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_x623766253}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_x1736566713}

[\[Sysname\] interface virtual-ethernet 1.1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.1\] vlan-type dot1q vid 100 second-dot1q 100]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.1\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[Virtual-Ethernet1.2]{lang="EN-US"}]{#struct_0_x1084_x1162_x1714992902}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[200]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface virtual-ethernet 1.2]{lang="EN-US"}]{#struct_0_x1084_x1162_288213262}

[\[Sysname-Virtual-Ethernet1.2\] vlan-type dot1q vid 100 second-dot1q 200 to 300]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.2\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[Virtual-Ethernet1.3]{lang="EN-US"}]{#struct_0_x1084_x1162_1227850072}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[any]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface virtual-ethernet 1.3]{lang="EN-US"}]{#struct_0_x1084_x1162_606024413}

[\[Sysname-Virtual-Ethernet1.3\] vlan-type dot1q vid 100 second-dot1q any]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.3\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[Virtual-Ethernet1.4]{lang="EN-US"}]{#struct_0_x1084_x1162_x1034942352}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[600]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface virtual-ethernet 1.4]{lang="EN-US"}]{#struct_0_x1084_x1162_x623831789}

[\[Sysname-Virtual-Ethernet1.4\] vlan-type dot1q vid 100 second-dot1q 500 to 600]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.4\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[Virtual-Ethernet1.5]{lang="EN-US"}]{#struct_0_x1084_x1162_570193534}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[200]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[600]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface virtual-ethernet 1.5]{lang="EN-US"}]{#struct_0_x1084_x1162_x1605871391}

[\[Sysname-Virtual-Ethernet1.5\] vlan-type dot1q vid 200 second-dot1q 500 to 600]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.5\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[Virtual-Ethernet1.6]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258100448}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[400]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface virtual-ethernet 1.6]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258559199}

[\[Sysname-Virtual-Ethernet1.6\] vlan-type dot1q vid 300 to 400 second-dot1q 100]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.6\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.7]{lang="EN-US"}]{#struct_0_x1084_x1162_13328755}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[400]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[600]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface virtual-ethernet 1.7]{lang="EN-US"}]{#struct_0_x1084_x1162_1145355855}

[\[Sysname-Virtual-Ethernet1.7\] vlan-type dot1q vid 300 to 400 second-dot1q 500 to 600]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet1.7\] quit]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置子接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.8]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258624735}[能够终结的]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{lang="EN-US" style="font-family:
宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[300]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[400]{lang="EN-US"}[、第二层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{lang="EN-US" style="font-family:宋体"}[any]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\[Sysname\] interface virtual-ethernet 1.8]{lang="EN-US"}]{#struct_0_x1084_x1162_x2140309150}

[\[Sysname-Virtual-Ethernet1.8\] vlan-type dot1q vid 300 to 400 second-dot1q any]{lang="EN-US"}

[[通过以上配置，子接口]{style="font-family:宋体"}[Virtual-Ethernet1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_453708397}[～]{style="font-family:宋体"}[Virtual-Ethernet1.8]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文规格如下：]{style="font-family:宋体"}

[]{#table_struct_0_x1151976095}[[子接口]{style="font-family:黑体"}]{#struct_0_x1084_x1162_x827558737}

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_x1876253168}[报文的第一层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[允许终结的]{style="font-family:黑体"}[VLAN]{lang="EN-US"}]{#struct_0_x1084_x1162_1637000374}[报文的第二层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}

[[Virtual-Ethernet1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_x1085926111}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x623635181}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x2137218096}

[[Virtual-Ethernet1.2]{lang="EN-US"}]{#struct_0_x1084_x1162_x1275536160}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_1383555191}

[[200]{lang="EN-US"}]{#struct_0_x1084_x1162_1131134431}[～]{style="font-family:宋体"}[300]{lang="EN-US"}

[[Virtual-Ethernet1.3]{lang="EN-US"}]{#struct_0_x1084_x1162_x2041953649}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x623700717}

[[1]{lang="EN-US"}]{#struct_0_x1084_x1162_2134245753}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[、]{style="font-family:宋体"}[101]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[、]{style="font-family:宋体"}[301]{lang="EN-US"}[～]{style="font-family:宋体"}[499]{lang="EN-US"}[、]{style="font-family:宋体"}[601]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[（即]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[范围内除]{style="font-family:宋体"}[100]{lang="EN-US"}[、]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[和]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[的值）]{style="font-family:宋体"}

[[Virtual-Ethernet1.4]{lang="EN-US"}]{#struct_0_x1084_x1162_x1540243122}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1719682413}

[[500]{lang="EN-US"}]{#struct_0_x1084_x1162_x1923878486}[～]{style="font-family:宋体"}[600]{lang="EN-US"}

[[Virtual-Ethernet1.5]{lang="EN-US"}]{#struct_0_x1084_x1162_1481526034}

[[200]{lang="EN-US"}]{#struct_0_x1084_x1162_x629448700}

[[500]{lang="EN-US"}]{#struct_0_x1084_x1162_x623504109}[～]{style="font-family:宋体"}[600]{lang="EN-US"}

[[Virtual-Ethernet1.6]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258362591}

[[300]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258428127}[～]{style="font-family:宋体"}[400]{lang="EN-US"}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258493663}

[[Virtual-Ethernet1.7]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258034911}

[[300]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258100447}[～]{style="font-family:宋体"}[400]{lang="EN-US"}

[[500]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258559202}[～]{style="font-family:宋体"}[600]{lang="EN-US"}

[[Virtual-Ethernet1.8]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258690274}

[[300]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258755810}[～]{style="font-family:宋体"}[400]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_x1084_x1162_x1258297058}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[、]{style="font-family:宋体"}[101]{lang="EN-US"}[～]{style="font-family:宋体"}[499]{lang="EN-US"}[、]{style="font-family:宋体"}[601]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[（即]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[范围内除]{style="font-family:宋体"}[100]{lang="EN-US"}[和]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[的值）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1084_x1162_x573034804}[配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[能够终结的第一层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[、第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的带有两层或两层以上]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文；配置子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.2]{lang="EN-US"}[能够终结的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[报文的第一层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[、第二层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1084_x1162_1262015494}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q vid 10 second-dot1q 100 loose]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1.2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.2\] vlan-type dot1q vid 20 second-dot1q 20]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.2\] quit]{lang="EN-US"}

[[通过以上配置，]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_x1274307894}[、]{style="font-family:宋体"}[GigabitEthernet1/0/1.2]{lang="EN-US"}[能够终结的报文规格如下：]{style="font-family:宋体"}

[]{#table_struct_0_x1150494949}[[子接口]{style="font-family:黑体"}]{#struct_0_x1084_x1162_1429206104}

[[允许终结的第一层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1084_x1162_1865435884}

[[允许终结的第二层]{style="font-family:黑体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1084_x1162_x344941993}

[[是否允许终结携带两层以上]{style="font-family:黑体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x1084_x1162_x623569645}[的报文]{style="font-family:黑体"}

[[GigabitEthernet1/0/1.1]{lang="EN-US"}]{#struct_0_x1084_x1162_x1018553681}

[[10]{lang="EN-US"}]{#struct_0_x1084_x1162_151020119}

[[100]{lang="EN-US"}]{#struct_0_x1084_x1162_x130117436}

[[是]{style="font-family:宋体"}]{#struct_0_x1084_x1162_x100957122}

[[GigabitEthernet1/0/1.2]{lang="EN-US"}]{#struct_0_x1084_x1162_1165250454}

[[20]{lang="EN-US"}]{#struct_0_x1084_x1162_466768913}

[[20]{lang="EN-US"}]{#struct_0_x1084_x1162_x624028396}

[[否]{style="font-family:宋体"}]{#struct_0_x1084_x1162_1596040516}

[ ]{lang="EN-US"}
