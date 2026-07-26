::: {#1492484606 .myid}
[]{#_Toc306713397}[]{#_Toc404784185}[]{#struct_0_40938_10595_493493780}[]{#_Toc306713402}[]{#_Toc294526199}

**QinQ \-- QinQ配置命令 \-- display qinq**

------------------------------------------------------------------------

[**[display qinq]{lang="EN-US"}**]{#struct_0_40938_10595_176660734}[命令用来显示使能了]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能的端口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_40938_10595_x881884222}

[**[display qinq]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_40938_10595_1718360028}

[[【视图】]{style="font-family:黑体"}]{#struct_0_40938_10595_219407578}

[[任意视图]{style="font-family:宋体"}]{#struct_0_40938_10595_1651616245}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_40938_10595_1736337704}

[[network-admin]{lang="EN-US"}]{#struct_0_40938_10595_225097580}

[[network-operator]{lang="EN-US"}]{#struct_0_40938_10595_2051919936}

[[mdc-admin]{lang="EN-US"}]{#struct_0_40938_10595_x969980031}

[[mdc-operator]{lang="EN-US"}]{#struct_0_40938_10595_1096032680}

[[【参数】]{style="font-family:黑体"}]{#struct_0_40938_10595_x201035921}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_40938_10595_1284650887}[：显示指定端口是否使能了]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号；如果未指定该参数，]{style="font-family:宋体"}[则显示所有使能]{style="font-family:
宋体"}[QinQ]{lang="EN-US"}[功能的端口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_40938_10595_861239096}

[[如果端口都没有使能]{style="font-family:宋体"}[QinQ]{lang="EN-US"}]{#struct_0_40938_10595_219473114}[功能，则执行该命令后无显示内容。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_40938_10595_x1047668874}

[[\# ]{lang="EN-US"}]{#struct_0_40938_10595_x1428038584}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能，然后显示该端口是否使能了]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_40938_10595_504475055}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qinq enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] display qinq interface gigabitethernet 1/0/1]{lang="EN-US"}

[Interface]{lang="EN-US"}

[ GigabitEthernet1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_40938_10595_x1775815818}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[上使能]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能，然后显示所有使能了]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能的端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_40938_10595_219538650}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qinq enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] qinq enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] display qinq]{lang="EN-US"}

[Interface]{lang="EN-US"}

[ GigabitEthernet1/0/1]{lang="EN-US"}

[ GigabitEthernet1/0/3]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display qinq]{lang="EN-US"}]{#struct_0_40938_10595_x304073537}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_821042100}[[字段]{style="font-family:黑体"}]{#struct_0_40938_10595_10320868}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_40938_10595_1943804968}

[[Interface]{lang="EN-US"}]{#struct_0_40938_10595_x1670746008}

[[接口名称]{style="font-family:宋体"}]{#struct_0_40938_10595_1574419792}

[[GigabitEthernet1/0/1]{lang="EN-US"}]{#struct_0_40938_10595_x418505960}

[[使能了]{style="font-family:宋体"}[QinQ]{lang="EN-US"}]{#struct_0_40938_10595_1044197457}[功能的端口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_40938_10595_219604186}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qinq enable]{lang="EN-US"}**]{#struct_0_40938_10595_x363735145}

::: {#847290813 .myid}
[]{#_Toc404784186}[]{#struct_0_40938_10595_2011654250}

**QinQ \-- QinQ配置命令 \-- qinq enable**

------------------------------------------------------------------------

[**[qinq enable]{lang="EN-US"}**]{#struct_0_40938_10595_x55194793}[命令用来使能端口的]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo qinq enable]{lang="EN-US"}**]{#struct_0_40938_10595_x1007238479}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_40938_10595_x1819420950}

[**[qinq enable]{lang="EN-US"}**]{#struct_0_40938_10595_x1635316301}

[**[undo qinq enable]{lang="EN-US"}**]{#struct_0_40938_10595_x1339331093}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_40938_10595_596400543}

[[端口的]{style="font-family:宋体"}[QinQ]{lang="EN-US"}]{#struct_0_40938_10595_219669722}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_40938_10595_x1595031289}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_40938_10595_x1614740603}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_40938_10595_1663995094}

[[network-admin]{lang="EN-US"}]{#struct_0_40938_10595_x26830414}

[[mdc-admin]{lang="EN-US"}]{#struct_0_40938_10595_232387411}

[[【举例】]{style="font-family:黑体"}]{#struct_0_40938_10595_x498773012}

[[\# ]{lang="EN-US"}]{#struct_0_40938_10595_539150456}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_40938_10595_x1331619204}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qinq enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_40938_10595_219735258}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[qinq]{lang="EN-US"}**]{#struct_0_40938_10595_410215003}
:::

::::: {#-1936232445 .myid}
[]{#_Toc404784187}[]{#struct_0_40938_10595_x501412217}[]{#_Toc306713398}

**QinQ \-- QinQ配置命令 \-- qinq ethernet-type**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QinQ命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_40938_10595_x1043724244}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的视图支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_40938_10595_x2120916822}
:::

**[ ]{lang="EN-US"}**

[**[qinq ethernet-type]{lang="EN-US"}**]{#struct_0_40938_10595_121089597}[命令用来配置内层或外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo qinq ethernet-type]{lang="EN-US"}**]{#struct_0_40938_10595_1003512307}[命令用来恢复内层或外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值为缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_40938_10595_915421713}

[**[qinq ethernet-type]{lang="EN-US"}**[ { **customer-tag** \| **service-tag** } *hex-value*]{lang="EN-US"}]{#struct_0_40938_10595_930681499}

[**[undo qinq ethernet-type ]{lang="EN-US"}**[{ **customer-tag** \| **service-tag** }]{lang="EN-US"}]{#struct_0_40938_10595_x1259989795}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_40938_10595_218752218}

[[内、外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_40938_10595_x113933866}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值的全局配置都为]{style="font-family:宋体"}[0x8100]{lang="EN-US"}[，端口配置等于全局配置（若支持全局配置）或都为]{style="font-family:宋体"}[0x8100]{lang="EN-US"}[（若不支持全局配置）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_40938_10595_472544555}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_40938_10595_x1328692846}[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_40938_10595_1616533867}

[[network-admin]{lang="EN-US"}]{#struct_0_40938_10595_10331822}

[[mdc-admin]{lang="EN-US"}]{#struct_0_40938_10595_1905454741}

[[【参数】]{style="font-family:黑体"}]{#struct_0_40938_10595_x2105805362}

[**[customer-tag]{lang="EN-US"}**]{#struct_0_40938_10595_x1010909736}[：表示配置内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值。本参数及视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[service-tag]{lang="EN-US"}**]{#struct_0_40938_10595_218817754}[：表示配置外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值。本参数及视图的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[hex-value]{lang="EN-US"}*]{#struct_0_40938_10595_66504797}[：表示十六进制格式的协议类型值，取值范围为]{style="font-family:宋体"}[0x0001]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFF]{lang="EN-US"}[，但不允许配置为]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-2]{lang="EN-US"}](?-1936232445#_Ref154730745)[中列举的常用协议类型值。]{style="font-family:宋体"}

[]{#struct_0_40938_10595_x1402125144}[[表1-2 ]{lang="EN-US"}[常用协议类型值]{style="font-family:
黑体"}]{#_Ref154730745}

[]{#table_struct_0_820185372}[[协议类型]{style="font-family:黑体"}]{#struct_0_40938_10595_812701946}
:::::

[[协议类型值]{style="font-family:黑体"}]{#struct_0_40938_10595_x1430034722}

[[ARP]{lang="EN-US"}]{#struct_0_40938_10595_2132787987}

[[0x0806]{lang="EN-US"}]{#struct_0_40938_10595_1729669794}

[[PUP]{lang="EN-US"}]{#struct_0_40938_10595_1064258841}

[[0x0200]{lang="EN-US"}]{#struct_0_40938_10595_219276507}

[[RARP]{lang="EN-US"}]{#struct_0_40938_10595_x1334990365}

[[0x8035]{lang="EN-US"}]{#struct_0_40938_10595_401460603}

[[IP]{lang="EN-US"}]{#struct_0_40938_10595_x1841243615}

[[0x0800]{lang="EN-US"}]{#struct_0_40938_10595_522782479}

[[IPv6]{lang="EN-US"}]{#struct_0_40938_10595_x898281729}

[[0x86DD]{lang="EN-US"}]{#struct_0_40938_10595_219342043}

[[PPPoE]{lang="EN-US"}]{#struct_0_40938_10595_625626291}

[[0x8863/0x8864]{lang="EN-US"}]{#struct_0_40938_10595_493493781}

[[MPLS]{lang="EN-US"}]{#struct_0_40938_10595_176660733}

[[0x8847/0x8848]{lang="EN-US"}]{#struct_0_40938_10595_x881884219}

[[IPX/SPX]{lang="EN-US"}]{#struct_0_40938_10595_1717901273}

[[0x8137]{lang="EN-US"}]{#struct_0_40938_10595_219407579}

[[IS-IS]{lang="EN-US"}]{#struct_0_40938_10595_1651616246}

[[0x8000]{lang="EN-US"}]{#struct_0_40938_10595_1736141096}

[[LACP]{lang="EN-US"}]{#struct_0_40938_10595_x2095603625}

[[0x8809]{lang="EN-US"}]{#struct_0_40938_10595_x2107091089}

[[LLDP]{lang="EN-US"}]{#struct_0_40938_10595_219473115}

[[0x88CC]{lang="EN-US"}]{#struct_0_40938_10595_x1047668875}

[[802.1X]{lang="EN-US"}]{#struct_0_40938_10595_138045357}

[[0x888E]{lang="EN-US"}]{#struct_0_40938_10595_504693328}

[[802.1ag]{lang="EN-US"}]{#struct_0_40938_10595_1636351272}

[[0x8902]{lang="EN-US"}]{#struct_0_40938_10595_219538651}

[[集群]{style="font-family:宋体"}]{#struct_0_40938_10595_x304073538}

[[0x88A7]{lang="EN-US"}]{#struct_0_40938_10595_9468900}

[[设备保留]{style="font-family:宋体"}]{#struct_0_40938_10595_834159872}

[[0xFFFD/0xFFFE/0xFFFF]{lang="EN-US"}]{#struct_0_40938_10595_1228997108}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_40938_10595_219604187}

[[对于某个端口来说，优先采用端口上的配置，最后才采用全局配置。]{style="font-family:宋体"}]{#struct_0_40938_10595_x363735144}

[[【举例】]{style="font-family:黑体"}]{#struct_0_40938_10595_2011719786}

[[\# ]{lang="EN-US"}]{#struct_0_40938_10595_741681338}[全局配置内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x8200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_40938_10595_104697550}

[\[Sysname\] qinq ethernet-type customer-tag 8200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_40938_10595_x1109072674}[全局配置外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x8200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_40938_10595_351142876}

[\[Sysname\] qinq ethernet-type service-tag 8200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_40938_10595_x1316314624}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x9100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_40938_10595_219669723}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qinq ethernet-type customer-tag 9100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_40938_10595_x1595031288}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[TPID]{lang="EN-US"}[值为]{style="font-family:宋体"}[0x9100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_40938_10595_1114142752}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qinq ethernet-type service-tag 9100]{lang="EN-US"}

::: {#2036306891 .myid}
[]{#_Toc404784188}[]{#struct_0_40938_10595_x1661264939}[]{#_Toc306713399}

**QinQ \-- QinQ配置命令 \-- qinq transparent-vlan**

------------------------------------------------------------------------

[**[qinq transparent-vlan]{lang="EN-US"}**]{#struct_0_40938_10595_x1700117957}[命令用来配置端口的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[透传功能，使端口对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文进行透传。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qinq transparent-vlan**]{lang="EN-US"}]{#struct_0_40938_10595_x392075837}[命令用来取消端口对指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文进行透传的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_40938_10595_1293648659}

[**[qinq transparent-vlan ]{lang="EN-US"}***[vlan-id-list]{lang="EN-US"}*]{#struct_0_40938_10595_219735259}

[**[undo qinq transparent-vlan]{lang="EN-US"}**[ { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_40938_10595_410215002}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_40938_10595_x501412216}

[[端口没有配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_40938_10595_x1043658708}[透传功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_40938_10595_x1327740920}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_40938_10595_x226060764}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_40938_10595_x981073806}

[[network-admin]{lang="EN-US"}]{#struct_0_40938_10595_x1180381333}

[[mdc-admin]{lang="EN-US"}]{#struct_0_40938_10595_x996970104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_40938_10595_x1850005878}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_40938_10595_218752219}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，且这些]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须是本地已创建好的。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[的值]{style="font-family:宋体"}[要大于或等于]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[的值]{style="font-family:宋体"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_40938_10595_x113933867}[：表示所有已创建的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_40938_10595_472479019}

[[\# ]{lang="EN-US"}]{#struct_0_40938_10595_1420435258}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能，配置端口为]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型，允许]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:
宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[的报文通过，并对]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的报文进行透传。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_40938_10595_x1098132090}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port link-type trunk]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port trunk permit vlan 2 3 50 to 100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qinq enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qinq transparent-vlan 2]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
