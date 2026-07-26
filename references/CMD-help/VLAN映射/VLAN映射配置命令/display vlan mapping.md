::: {#-693493954 .myid}
[]{#_Toc404784212}[]{#struct_0_71588_12744_219276504}

**VLAN映射 \-- VLAN映射配置命令 \-- display vlan mapping**

------------------------------------------------------------------------

[**[display vlan mapping]{lang="EN-US"}**]{#struct_0_71588_12744_x1334990366}[命令用来显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71588_12744_1967544544}

[**[display vlan mapping ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[interface]{lang="EN-US"}***[ interface-type interface-number ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_71588_12744_x303946351}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71588_12744_x1395664134}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71588_12744_861131620}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71588_12744_x1636497340}

[[network-admin]{lang="EN-US"}]{#struct_0_71588_12744_1483061719}

[[network-operator]{lang="EN-US"}]{#struct_0_71588_12744_x743576564}

[[mdc-admin]{lang="EN-US"}]{#struct_0_71588_12744_x1481222766}

[[mdc-operator]{lang="EN-US"}]{#struct_0_71588_12744_219342040}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71588_12744_625626288}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_71588_12744_x1845158372}[：显示指定接口的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定该参数，将显示所有接口的]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71588_12744_x165550104}

[[\# ]{lang="EN-US"}]{#struct_0_71588_12744_1658396965}[显示所有接口上的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display vlan mapping]{lang="EN-US"}]{#struct_0_71588_12744_219407576}

[Interface GigabitEthernet1/0/1:]{lang="EN-US"}

[  Outer VLAN    Inner VLAN    Translated Outer VLAN    Translated Inner VLAN]{lang="EN-US"}

[  10            N/A           120                      N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface GigabitEthernet1/0/2:]{lang="EN-US"}

[  Outer VLAN    Inner VLAN    Translated Outer VLAN    Translated Inner VLAN]{lang="EN-US"}

[  4-4094        N/A           100                      N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface GigabitEthernet1/0/3:]{lang="EN-US"}

[  Outer VLAN    Inner VLAN    Translated Outer VLAN    Translated Inner VLAN]{lang="EN-US"}

[  12            N/A           110                      12]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface GigabitEthernet1/0/4:]{lang="EN-US"}

[  Outer VLAN    Inner VLAN    Translated Outer VLAN    Translated Inner VLAN]{lang="EN-US"}

[  11            30            130                      40]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display vlan mapping]{lang="EN-US"}]{#struct_0_71588_12744_1651616259}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1268118245}[[字段]{style="font-family:黑体"}]{#struct_0_71588_12744_1737124137}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71588_12744_1052131984}

[[Interface]{lang="EN-US"}]{#struct_0_71588_12744_x1464029105}

[[接口信息]{style="font-family:宋体"}]{#struct_0_71588_12744_x681154646}

[[Outer VLAN]{lang="EN-US"}]{#struct_0_71588_12744_219473112}

[[原始外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_71588_12744_x1047668876}

[[当显示信息中]{style="font-family:宋体"}[Inner VLAN]{lang="EN-US"}]{#struct_0_71588_12744_399322685}[显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，此时]{style="font-family:宋体"}[Outer VLAN]{lang="EN-US"}[表示原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Inner VLAN]{lang="EN-US"}]{#struct_0_71588_12744_1704129298}

[[原始内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_71588_12744_2051095860}

[[对于]{style="font-family:宋体"}[1:1 VLAN]{lang="EN-US"}]{#struct_0_71588_12744_x3852006}[映射、]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射和]{style="font-family:宋体"}[1:2 VLAN]{lang="EN-US"}[映射，显示信息中]{style="font-family:宋体"}[Inner VLAN]{lang="EN-US"}[无意义，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Translated Outer VLAN]{lang="EN-US"}]{#struct_0_71588_12744_x1330327153}

[[转换后的外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_71588_12744_470569050}

[[当显示信息中]{style="font-family:宋体"}[Translated Inner VLAN]{lang="EN-US"}]{#struct_0_71588_12744_399257149}[显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，此时]{style="font-family:宋体"}[Translated Outer VLAN]{lang="EN-US"}[表示转换后]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Translated Inner VLAN]{lang="EN-US"}]{#struct_0_71588_12744_x1425862740}

[[转换后的内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_71588_12744_219538648}

[[对于]{style="font-family:宋体"}[1:1 VLAN]{lang="EN-US"}]{#struct_0_71588_12744_369286126}[映射和]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射，显示信息中]{style="font-family:宋体"}[Translated Inner VLAN]{lang="EN-US"}[无意义，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71588_12744_2034578631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vlan mapping]{lang="EN-US"}**]{#struct_0_71588_12744_1735372178}

::::: {#1656294008 .myid}
[]{#_Toc404784213}[]{#struct_0_71588_12744_x35848588}

**VLAN映射 \-- VLAN映射配置命令 \-- vlan mapping**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VLAN映射命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_71588_12744_1992141706}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_71588_12744_x1208294413}
:::

[ ]{lang="EN-US"}

[**[vlan mapping]{lang="EN-US"}**]{#struct_0_71588_12744_x816650547}[命令用来在接口上配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射。]{style="font-family:宋体"}

[**[undo vlan mapping]{lang="EN-US"}**]{#struct_0_71588_12744_863818467}[命令用来取消]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71588_12744_219604184}

[**[vlan mapping ]{lang="EN-US"}**[{ *vlan-id* **translated-vlan** *vlan-id* \| **nest** { **range** *vlan-range-list* \| **single** *vlan-id-list* } **nested-vlan** *vlan-id* \| **nni** \| **tunnel** *outer-vlan-id inner-vlan-id* **translated-vlan** *outer-vlan-id inner-vlan-id* \| **uni** { **range** *vlan-range-list* \| **single** *vlan-id-list* } **translated-vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_71588_12744_x363735147}

[**[undo vlan mapping ]{lang="EN-US"}**[{ *vlan-id* **translated-vlan** *vlan-id* \| **all** \| **nest** { **range** *vlan-range-list* \| **single** *vlan-id-list* } **nested-vlan** *vlan-id* \| **nni** \| **tunnel** *outer-vlan-id inner-vlan-id* **translated-vlan** *outer-vlan-id inner-vlan-id* \| **uni** { **range** *vlan-range-list* \| **single** *vlan-id-list* } **translated-vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_71588_12744_2011785322}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_71588_12744_x834513320}

[[接口上未配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_71588_12744_1903777549}[映射。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71588_12744_x1186037410}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71588_12744_x1649756605}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71588_12744_x867578526}

[[network-admin]{lang="EN-US"}]{#struct_0_71588_12744_1520860235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_71588_12744_x1692585254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71588_12744_219669720}

[*[vlan-id]{lang="EN-US"}***[ translated-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_71588_12744_x1595031287}[：表示]{style="font-family:宋体"}[1:1 VLAN]{lang="EN-US"}[映射的原始]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[和转换后的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。原始]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[和转换后的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[不允许相同。]{style="font-family:宋体"}

[**[uni]{lang="EN-US"}**[ **range** *vlan-range-list* **translated-vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_71588_12744_x1164401909}[：表示]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射的用户侧配置，指定映射的原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[段列表和转换后的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[vlan-range-list]{lang="EN-US"}*[ = { *vlan-id1* **to** *vlan-id2* }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。参数涉及的]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围都为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。不同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[段之间不允许出现交叉重叠。原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与转换后]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不允许相同。]{style="font-family:宋体"}

[**[uni single]{lang="EN-US"}**[ *vlan-id-list* **translated-vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_71588_12744_654199821}[：表示]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射的用户侧配置，指定映射的原始]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[列表和转换后的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。参数涉及的]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围都为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与转换后]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不允许相同。]{style="font-family:宋体"}

[**[nni]{lang="EN-US"}**]{#struct_0_71588_12744_x105395248}[：表示]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射的网络侧配置，用于指导网络侧发往用户侧的流量进行三层转发，并将报文的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[替换为对应的]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射前的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nest range]{lang="EN-US"}**[ *vlan-range-list* **nested-vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_71588_12744_1683044364}[：表示]{style="font-family:宋体"}[1:2 VLAN]{lang="EN-US"}[映射的原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[段列表和添加的外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[vlan-range-list]{lang="EN-US"}*[ = { *vlan-id1* **to** *vlan-id2* }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。参数涉及的]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围都为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。不同]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[段之间不允许出现交叉重叠。]{style="font-family:宋体"}

[**[nest single]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}***[ nested-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_71588_12744_x2049095197}[：表示]{style="font-family:宋体"}[1:2 VLAN]{lang="EN-US"}[映射的原始]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[列表和添加的外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:
宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:
宋体"}[10]{lang="EN-US"}[次。参数涉及的]{style="font-family:
宋体"}*[vlan-id]{lang="EN-US"}*[取值范围都为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tunnel]{lang="EN-US"}***[ outer-vlan-id inner-vlan-id ]{lang="EN-US"}***[translated-vlan]{lang="EN-US"}***[ outer-vlan-id inner-vlan-id]{lang="EN-US"}*]{#struct_0_71588_12744_329500293}[：表示]{style="font-family:宋体"}[2:2 VLAN]{lang="EN-US"}[映射的原始外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、内层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[和转换后的外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、内层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[outer-vlan-id]{lang="EN-US"}*[和]{style="font-family:宋体"}*[inner-vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71588_12744_x544381198}[：表示删除接口上所有的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71588_12744_219735256}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一接口上不同类型映射表项的原始]{style="font-family:宋体"}]{#struct_0_71588_12744_410214993}[VLAN]{lang="EN-US"}[及转换后]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不允许重复；同一类型映射表项中，]{style="font-family:宋体"}[1:1]{lang="EN-US"}[或]{style="font-family:宋体"}[2:2 VLAN]{lang="EN-US"}[映射表项的转换后]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不允许重复，若]{style="font-family:宋体"}[1:1]{lang="EN-US"}[或]{style="font-family:宋体"}[2:2 VLAN]{lang="EN-US"}[映射表项的原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[重复，则以最新配置为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一接口上透传]{style="font-family:宋体"}]{#struct_0_71588_12744_x899799046}[VLAN]{lang="EN-US"}[和映射表项的原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[及转换后]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（对于携带两层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的报文，原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[及转换后]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[都仅指外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）不允许相同。有关透传]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的详细介绍，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[QinQ]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_71588_12744_x1362948911}[N:1 VLAN]{lang="EN-US"}[映射用户侧配置和网络侧配置不成对配置，则]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射功能不能正确执行。同一个接口不能同时配置为]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射的用户侧接口和网络侧接口。接口配置为]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射网络侧接口后，不建议再配置其他类型的映射表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启或关闭]{style="font-family:宋体"}]{#struct_0_71588_12744_1325765965}[QinQ]{lang="EN-US"}[功能之前，要先清除已有的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[QinQ]{lang="EN-US"}]{#struct_0_71588_12744_974181812}[功能和]{style="font-family:宋体"}[2:2 VLAN]{lang="EN-US"}[映射功能互斥。开启]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能后，接口只能识别一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，所以该接口无法再实现]{style="font-family:宋体"}[2:2 VLAN]{lang="EN-US"}[映射功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}]{#struct_0_71588_12744_1343162175}[映射时需要注意的是，该功能不能与]{lang="EN-US" style="font-family:宋体"}[uRPF]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Unicast Reverse Path Forwarding]{lang="EN-US"}[，单播反向路径转发）功能同时使用，否则会造成网络侧发往用户侧的流量不能正常转发。有关]{lang="EN-US" style="font-family:宋体"}[uRPF]{lang="EN-US"}[的详细介绍，请参见"安全配置指导"中的"]{lang="EN-US" style="font-family:宋体"}[uRPF]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[1:2 VLAN]{lang="EN-US"}]{#struct_0_71588_12744_387340932}[映射时需要注意的是，]{lang="EN-US" style="font-family:宋体"}[1:2 VLAN]{lang="EN-US"}[映射]{lang="EN-US" style="font-family:宋体"}[为报文加上外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[后，内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[将被当作报文的数据部分进行传输，报文长度将增加]{style="font-family:宋体"}[4]{lang="EN-US"}[个字节。因此建议用户适当增加映射后报文传输路径上各接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值（至少为]{style="font-family:宋体"}[1504]{lang="EN-US"}[字节）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_71588_12744_x49212524}[映射功能只对接口收到的携带]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的报文生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71588_12744_218752216}

[[\# ]{lang="EN-US"}]{#struct_0_71588_12744_x113933856}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[1:1 VLAN]{lang="EN-US"}[映射：原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，映射后]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_71588_12744_472544558}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] vlan mapping 1 translated-vlan 101]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71588_12744_x1328692857}[将接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[配置为]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射用户侧接口：原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[50]{lang="EN-US"}[、]{style="font-family:宋体"}[80]{lang="EN-US"}[，映射后]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[101]{lang="EN-US"}[。同时将接口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[配置为]{style="font-family:宋体"}[N:1 VLAN]{lang="EN-US"}[映射网络侧接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_71588_12744_x1112283952}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] vlan mapping uni range 1 to 50 translated-vlan 101]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] vlan mapping uni single 80 translated-vlan 101]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] vlan mapping nni]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71588_12744_1675623717}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[上配置]{style="font-family:宋体"}[1:2 VLAN]{lang="EN-US"}[映射：原始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[、]{style="font-family:宋体"}[80]{lang="EN-US"}[，映射后添加的外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_71588_12744_218817752}

[\[Sysname\] interface gigabitethernet 1/0/4]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/4\] vlan mapping nest range 1 to 10 nested-vlan 101]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/4\] vlan mapping nest single 80 nested-vlan 101]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71588_12744_66504799}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/5]{lang="EN-US"}[上配置]{style="font-family:宋体"}[2:2 VLAN]{lang="EN-US"}[映射：原始外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[101]{lang="EN-US"}[、内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，映射后外层]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[201]{lang="EN-US"}[、内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_71588_12744_x1784462168}

[\[Sysname\] interface gigabitethernet 1/0/5]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/5\] vlan mapping tunnel 101 1 translated-vlan 201 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71588_12744_564748841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display vlan mapping]{lang="EN-US"}**]{#struct_0_71588_12744_x379856850}

[ ]{lang="EN-US"}
:::::
