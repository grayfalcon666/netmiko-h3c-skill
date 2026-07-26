::::: {#567931052 .myid}
[]{#_Toc404797191}[]{#struct_0_x1309_x3271_39426476}[]{#_Toc133401306}

**端口镜像 \-- 端口镜像配置命令 \-- display mirroring-group**

------------------------------------------------------------------------

[**[display mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_1377256106}[命令用来显示镜像组的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1996427029}

[**[display mirroring-group ]{lang="EN-US"}**[{ *group-id* \| **all** \| **local** \| **remote-destination** \| **remote-source** }]{lang="EN-US"}]{#struct_0_x1309_x3271_222422501}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x30488243}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x780990287}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_999441750}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_1377233516}

[[network-operator]{lang="EN-US"}]{#struct_0_x1309_x3271_761113059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_x1985680506}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1309_x3271_x996332990}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1377190570}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1978518293}[：显示指定镜像组的信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1309_x3271_x586680415}[：显示所有镜像组的信息。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1237236436}[：显示本地镜像组的信息。]{style="font-family:宋体"}

[**[remote-destination]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1727605425}[：显示远程目的镜像组的信息。]{style="font-family:宋体"}

[**[remote-source]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1432717922}[：显示远程源镜像组的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x84148007}

[[显示信息的显示顺序按照镜像组的编号顺序排列，显示内容包括镜像组的类型、状态和构成等信息。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_189796691}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1444233405}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1464192893}[显示所有镜像组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display mirroring-group all]{lang="EN-US"}]{#struct_0_x1309_x3271_1378173610}

[Mirroring group 1:]{lang="EN-US"}

[    Type: Local]{lang="EN-US"}

[    Status: Active]{lang="EN-US"}

[    Sampler: samp (failed)]{lang="EN-US"}

[    Mirroring port:]{lang="EN-US"}

[        GigabitEthernet1/0/1  Inbound]{lang="EN-US"}

[    Monitor port: GigabitEthernet1/0/2]{lang="EN-US"}

[Mirroring group 3]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Type: Local]{lang="EN-US"}

[    Status: Active]{lang="EN-US"}

[    Mirroring port:]{lang="EN-US"}

[        GigabitEthernet1/0/1  Inbound]{lang="EN-US"}

[        GigabitEthernet1/0/2  Both]{lang="EN-US"}

[    Mirroring VLAN:]{lang="EN-US"}

[        1-3, 5-7, 100-120, 130-1100, 1200-1300, 1400-1600, 1700-1800, 1950-2000  Inbound]{lang="EN-US"}

[        4, 8-9  Both]{lang="EN-US"}

[    Mirroring CPU:]{lang="EN-US"}

[        Slot 1, 2, 3  Both]{lang="EN-US"}

[        Slot 4  Inbound]{lang="EN-US"}

[    Monitor port: GigabitEthernet1/0/3]{lang="EN-US"}

[Mirroring group 6:]{lang="EN-US"}

[    Type: Remote source]{lang="EN-US"}

[    Status: Incomplete]{lang="EN-US"}

[    Mirroring port:]{lang="EN-US"}

[        GigabitEthernet1/0/4  Both]{lang="EN-US"}

[    Remote probe VLAN: 1900]{lang="EN-US"}

[Mirroring group 9:]{lang="EN-US"}

[    Type: Remote destination]{lang="EN-US"}

[    Status: Active]{lang="EN-US"}

[    Monitor port: GigabitEthernet1/0/6]{lang="EN-US"}

[    Remote probe VLAN: 1901]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_1378108074}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[显示信息的内容与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_604475411}
:::

[ ]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[ display mirroring-group]{lang="EN-US"}]{#struct_0_x1309_x3271_x571125027}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x330167341}[[字段]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x198221874}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x986074911}

[[Mirroring group]{lang="EN-US"}]{#struct_0_x1309_x3271_1937446513}

[[镜像组的编号]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1923536032}

[[Type]{lang="EN-US"}]{#struct_0_x1309_x3271_1377649319}

[[镜像组的类型：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x356574383}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_x1309_x3271_1038098438}[：本地镜像组]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote source]{lang="EN-US"}]{#struct_0_x1309_x3271_1450359284}[：远程源镜像组]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote destination]{lang="EN-US"}]{#struct_0_x1309_x3271_1454724457}[：远程目的镜像组]{lang="EN-US" style="font-family:
  宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x1309_x3271_x1121496503}

[[镜像组的状态：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_501643744}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1309_x3271_1377583783}[：表示镜像组已经生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incomplete]{lang="EN-US"}]{#struct_0_x1309_x3271_372484359}[：表示镜像组没有配完，暂不生效]{lang="EN-US" style="font-family:宋体"}

[[Sampler]{lang="EN-US"}]{#struct_0_x1309_x3271_1758037951}

[[采样器名称（若引用采样器失败，则在采样器名称后标识]{style="font-family:宋体"}[failed]{lang="EN-US"}]{#struct_0_x1309_x3271_x1402735400}[；若未配置引用的采样器，则不显示该字段）]{style="font-family:宋体"}

[[Mirroring port]{lang="EN-US"}]{#struct_0_x1309_x3271_1547426334}

[[镜像源端口]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1377518247}

[[Mirroring VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_400985992}

[[镜像源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_x388815120}

[[Mirroring CPU]{lang="EN-US"}]{#struct_0_x1309_x3271_1854508151}

[[镜像源]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1309_x3271_x375273149}

[[Monitor port]{lang="EN-US"}]{#struct_0_x1309_x3271_1266185844}

[[镜像目的端口]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1377452711}

[[Reflector port]{lang="EN-US"}]{#struct_0_x1309_x3271_x1174266440}

[[镜像组反射端口]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x498062397}

[[Remote probe VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_931871746}

[[远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_x528640147}

[ ]{lang="EN-US"}

::: {#60706591 .myid}
[]{#_Toc404797192}[]{#struct_0_x1309_x3271_1377387175}[]{#_Toc133401307}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group**

------------------------------------------------------------------------

[**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_x449741776}[命令用来创建一个镜像组。]{style="font-family:宋体"}

[**[undo mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_806520331}[命令用来删除已创建的镜像组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1859373929}

[**[mirroring-group]{lang="EN-US"}***[ group-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **local** \| **remote-destination** \| **remote-source** } \[ **sampler** *sampler-name* \]]{lang="EN-US"}]{#struct_0_x1309_x3271_x1831221403}

[**[undo mirroring-group]{lang="EN-US"}**[ { *group-id* \| **all** \| **local** \| **remote-destination** \| **remote-source** }]{lang="EN-US"}]{#struct_0_x1309_x3271_x838160659}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1214571021}

[[不存在任何镜像组。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1583837211}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1377321639}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1561706642}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_2002259720}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_458109080}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_745562734}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1636817444}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_2016982597}[：表示镜像组的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1309_x3271_x809824740}[：表示本地镜像组。]{style="font-family:宋体"}

[**[remote-destination]{lang="EN-US"}**]{#struct_0_x1309_x3271_1735705678}[：表示远程目的镜像组。]{style="font-family:宋体"}

[**[remote-source]{lang="EN-US"}**]{#struct_0_x1309_x3271_1377256103}[：表示远程源镜像组。]{style="font-family:宋体"}

[**[sampler]{lang="EN-US"}**[ *sampler-name*]{lang="EN-US"}]{#struct_0_x1309_x3271_x1996754709}[：表示端口镜像引用的采样器。]{style="font-family:宋体"}*[sampler-name]{lang="EN-US"}*[为采样器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1309_x3271_x781536217}[：表示所有镜像组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x605409793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每类镜像组可创建的数量与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x2055533859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采样器用来从一组固定数量的报文中选出一个报文，端口镜像通过引用采样器，可以对镜像报文进行采样而减少镜像报文的数量。端口镜像支持引用一个未创建的采样器。如果在端口镜像多次配置采样器，新的配置将覆盖旧的配置。有关采样器的相关配置，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x810393063}[Sampler]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1681093745}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1192231642}[创建本地镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并引用采样器]{style="font-family:宋体"}[samp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_1377190567}

[\[Sysname\] mirroring-group 1 local sampler samp]{lang="EN-US"}
:::

::::: {#1919107378 .myid}
[]{#_Toc133401308}[]{#_Toc404797193}[]{#struct_0_x1309_x3271_x1978977046}[]{#_Toc226197568}[]{#_Toc275522448}[]{#_Toc275522794}[]{#_Toc275522451}[]{#_Toc275522797}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group mirroring-cpu**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_1627890802}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_1843344087}
:::

[ ]{lang="EN-US"}

[**[mirroring-group mirroring-cpu]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1895468667}[命令用来为镜像组配置源]{style="font-family:
宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo mirroring-group mirroring-cpu]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1896350505}[命令用来删除镜像组的指定源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1460326990}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1309_x3271_x1679487094}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ mirroring-cpu slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*[ { **both** \| **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x1309_x3271_743255409}

[**[undo mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ mirroring-cpu slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1859442545}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1309_x3271_1378173607}[模式：]{style="font-family:宋体"}

[**[mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ mirroring-cpu chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number-list* { **both** \| **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x1309_x3271_x1754355325}

[**[undo mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ mirroring-cpu chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number-list*]{lang="EN-US"}]{#struct_0_x1309_x3271_x2093204924}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1299893199}

[[镜像组没有源]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1309_x3271_x893650469}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1327965801}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1950886680}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1703958963}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_1378108071}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_604278803}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x506541533}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_1308452318}[：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x1309_x3271_1298741807}[：源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[所在单板的槽位号列表，表示多个槽位。表示方式为]{style="font-family:宋体"}*[slot-number-list ]{lang="EN-US"}*[= { *slot-number* \[ **to** *slot-number* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[参数配置单板范围时，终止单板的槽位号必须大于等于起始单板的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x1309_x3271_x931929167}[：源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[所在设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号列表，表示多个成员。表示方式为]{style="font-family:宋体"}*[slot-number-list ]{lang="EN-US"}*[= { *slot-number* \[ **to** *slot-number* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[参数配置设备范围时，终止设备的成员编号必须大于等于起始设备的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1561573292}[：源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[所在设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号列表或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，表示多个成员。表示方式为]{style="font-family:宋体"}*[slot-number-list ]{lang="EN-US"}*[= { *slot-number* \[ **to** *slot-number* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[参数配置设备范围时，终止设备的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号必须大于等于起始设备的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number-list*]{lang="EN-US"}]{#struct_0_x1309_x3271_1133777711}[：源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[所在设备及单板的位置。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[表示]{style="font-family:宋体"}[单板的槽位号列表，表示方式为]{style="font-family:宋体"}*[slot-number-list ]{lang="EN-US"}*[= { *slot-number* \[ **to** *slot-number* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[参数配置单板范围时，终止单板的槽位号必须大于等于起始单板的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number-list*]{lang="EN-US"}]{#struct_0_x1309_x3271_2005405897}[：源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[所在单板的位置。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[表示]{style="font-family:宋体"}[单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位号列表，表示方式为]{style="font-family:宋体"}*[slot-number-list ]{lang="EN-US"}*[= { *slot-number* \[ **to** *slot-number* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[参数配置单板范围时，终止单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位号必须大于等于起始单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_x1309_x3271_x245582102}[：表示对源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[收发的报文都进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x1309_x3271_843065337}[：表示仅对源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[收到的报文进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x1309_x3271_1377649320}[：表示仅对源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[发出的报文进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x356115632}

[[只能为本地镜像组或远程源镜像组配置源]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1309_x3271_1025682174}[，不能为远程目的镜像组配置源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x701096755}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1591024356}

[\[Sysname\] mirroring-group 1 local]{lang="EN-US"}

[\[Sysname\] mirroring-group 1 mirroring-cpu slot 1 both]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1657827266}[创建远程源镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，配置其源]{style="font-family:宋体"}[CPU]{lang="EN-US"}[为位于]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，并对该]{style="font-family:宋体"}[CPU]{lang="EN-US"}[收发的报文都进行镜像。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_1377583784}

[\[Sysname\] mirroring-group 2 remote-source]{lang="EN-US"}

[\[Sysname\] mirroring-group 2 mirroring-cpu slot 2 both]{lang="EN-US"}

[]{#struct_0_x1309_x3271_372549895}[]{#_Toc272157626}[]{#_Toc272391006}[]{#_Toc272393519}[]{#_Toc272157628}[]{#_Toc272391008}[]{#_Toc272393521}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_648990910}
:::::

::::: {#1194065403 .myid}
[]{#_Toc404797194}[]{#struct_0_x1309_x3271_x355390889}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group mirroring-port (interface view)**

------------------------------------------------------------------------

[**[mirroring-group]{lang="EN-US"}***[ ]{lang="EN-US"}***[mirroring-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_x390598096}[命令用来配置当前端口为镜像组的源端口。]{style="font-family:宋体"}

[**[undo mirroring-group]{lang="EN-US"}***[ ]{lang="EN-US"}***[mirroring-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1712946889}[命令用来取消当前端口为镜像组的源端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_367052325}

[**[mirroring-group]{lang="EN-US"}***[ group-id ]{lang="EN-US"}***[mirroring-port]{lang="EN-US"}**[ { **both** \| **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x1309_x3271_1831051655}

[**[undo mirroring-group]{lang="EN-US"}***[ group-id]{lang="EN-US"}***[ mirroring-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1357537149}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1377518248}

[[端口不是任何镜像组的源端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_401969032}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_969339114}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1149500864}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x2147035857}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_1298737859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_241552620}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x964697603}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_1752846787}[：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_x1309_x3271_1377452712}[：表示对端口收发的报文都进行镜像。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1174331976}[：表示仅对端口收到的报文进行镜像。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x1309_x3271_1219314025}[：表示仅对端口发出的报文进行镜像。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_830134198}

[[只能为本地镜像组或远程源镜像组配置源端口，不能为远程目的镜像组配置源端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1247563145}

[[对于源端口，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x972728720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请不要将源端口加入到源]{style="font-family:宋体"}]{#struct_0_x1309_x3271_2069388748}[VLAN]{lang="EN-US"}[中和远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常，一个端口只能被一个镜像组使用；而在支持多目的端口的设备上，一个端口可被多个镜像组用作源端口，但源端口不能再被用作本镜像组或其他镜像组的反射端口、出端口或目的端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1993974220}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_x1996674576}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[不同型号的设备支持为本地镜像组配置源端口的接口视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_1377387176}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[不同型号的设备支持为远程源镜像组配置源端口的接口视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_x449676240}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1981044210}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1484868061}[创建本地镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置其源端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，并对该端口收发的报文都进行镜像。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_1906889112}

[\[Sysname\] mirroring-group 1 local]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mirroring-group 1 mirroring-port both]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1689533524}[创建远程源镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，配置其源端口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，并对该端口收发的报文都进行镜像。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x2063662539}

[\[Sysname\] mirroring-group 2 remote-source]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] mirroring-group 2 mirroring-port both]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1377321640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_1561116811}
:::::

::: {#-1111188176 .myid}
[]{#_Toc404797195}[]{#struct_0_x1309_x3271_848957261}[]{#_Toc272157642}[]{#_Toc272391022}[]{#_Toc272393535}[]{#_Toc272157645}[]{#_Toc272391025}[]{#_Toc272393538}[]{#_Toc272157646}[]{#_Toc272391026}[]{#_Toc272393539}[]{#_Toc272157650}[]{#_Toc272391030}[]{#_Toc272393543}[]{#_Toc272157651}[]{#_Toc272391031}[]{#_Toc272393544}[]{#_Toc272157655}[]{#_Toc272391035}[]{#_Toc272393548}[]{#_Toc245098148}[]{#_Toc245098934}[]{#_Toc245098149}[]{#_Toc245098935}[]{#_Toc245098150}[]{#_Toc245098936}[]{#_Toc245098151}[]{#_Toc245098937}[]{#_Toc245098152}[]{#_Toc245098938}[]{#_Toc245098153}[]{#_Toc245098939}[]{#_Toc245098154}[]{#_Toc245098940}[]{#_Toc245098155}[]{#_Toc245098941}[]{#_Toc245098156}[]{#_Toc245098942}[]{#_Toc245098157}[]{#_Toc245098943}[]{#_Toc245098158}[]{#_Toc245098944}[]{#_Toc245098159}[]{#_Toc245098945}[]{#_Toc245098160}[]{#_Toc245098946}[]{#_Toc245098161}[]{#_Toc245098947}[]{#_Toc245098162}[]{#_Toc245098948}[]{#_Toc245098163}[]{#_Toc245098949}[]{#_Toc245098164}[]{#_Toc245098950}[]{#_Toc245098165}[]{#_Toc245098951}[]{#_Toc245098166}[]{#_Toc245098952}[]{#_Toc245098167}[]{#_Toc245098953}[]{#_Toc245098168}[]{#_Toc245098954}[]{#_Toc245098169}[]{#_Toc245098955}[]{#_Toc245098170}[]{#_Toc245098956}[]{#_Toc245098171}[]{#_Toc245098957}[]{#_Toc245098172}[]{#_Toc245098958}[]{#_Toc245098175}[]{#_Toc245098961}[]{#_Toc245098176}[]{#_Toc245098962}[]{#_Toc245098180}[]{#_Toc245098966}[]{#_Toc245098183}[]{#_Toc245098969}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group mirroring-port (system view)**

------------------------------------------------------------------------

[**[mirroring-group mirroring-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1928026241}[命令用来为镜像组配置源端口。]{style="font-family:
宋体"}

[**[undo mirroring-group mirroring-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_1595902721}[命令用来删除镜像组的指定源端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1782672977}

[**[mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ mirroring-port ]{lang="EN-US"}***[interface-list]{lang="EN-US"}*[ { **both** \| **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x1309_x3271_1267633652}

[**[undo mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ mirroring-port ]{lang="EN-US"}***[interface-list]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1495682730}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_143701467}

[[镜像组没有源端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1377256104}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1996295957}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_967006651}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_260574769}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_1095136531}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_x80133693}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1970218438}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_1805043190}[：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-list]{lang="EN-US"}*]{#struct_0_x1309_x3271_490450758}[：源端口列表，表示一个或多个源端口。表示方式为]{style="font-family:宋体"}*[interface-list ]{lang="EN-US"}*[= { *interface-type interface-number* \[ **to** *interface-type interface-number* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[参数配置端口范围时，起始端口和终止端口必须是相同单板上相同类型的端口，且终止端口的端口编号必须大于等于起始端口的端口编号。不同设备支持的本地镜像组源端口和远程源镜像组源端口的端口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1316000557}[：表示对端口收发的报文都进行镜像。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x1309_x3271_1377190568}[：表示仅对端口收到的报文进行镜像。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1979042582}[：表示仅对端口发出的报文进行镜像。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1243529687}

[[只能为本地镜像组或远程源镜像组配置源端口，不能为远程目的镜像组配置源端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_785777643}

[[对于源端口，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1984082141}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请不要将源端口加入到源]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1198348952}[VLAN]{lang="EN-US"}[中和远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常，一个端口只能被一个镜像组使用；而在支持多目的端口的设备上，一个端口可被多个镜像组用作源端口，但源端口不能再被用作本镜像组或其他镜像组的反射端口、出端口或目的端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x582568971}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x2047565833}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x379563805}[创建本地镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置其源端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，并对该端口收发的报文都进行镜像。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_1378173608}

[\[Sysname\] mirroring-group 1 local]{lang="EN-US"}

[\[Sysname\] mirroring-group 1 mirroring-port gigabitethernet 1/0/1 both]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x1755207293}[创建远程源镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，配置其源端口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，并对该端口收发的报文都进行镜像。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1387021211}

[\[Sysname\] mirroring-group 2 remote-source]{lang="EN-US"}

[\[Sysname\] mirroring-group 2 mirroring-port gigabitethernet 1/0/2 both]{lang="EN-US"}

[]{#_Toc203363339}[]{#_Toc178754452}[]{#struct_0_x1309_x3271_288307866}[]{#_Toc272157630}[]{#_Toc272391010}[]{#_Toc272393523}[]{#_Toc272157632}[]{#_Toc272391012}[]{#_Toc272393525}[]{#_Toc225828710}[]{#_Toc226253378}[]{#_Toc225828711}[]{#_Toc226253379}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_x720517601}
:::

::::: {#-40157547 .myid}
[]{#_Toc404797196}[]{#struct_0_x1309_x3271_x1053127523}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group mirroring-vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_2147311789}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_1378108072}
:::

[ ]{lang="EN-US"}

[**[mirroring-group mirroring-vlan]{lang="EN-US"}**]{#struct_0_x1309_x3271_604344339}[命令用来为镜像组配置源]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[undo mirroring-group mirroring-vlan]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1225019077}[命令用来删除镜像组的指定源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_412486690}

[**[mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ mirroring-vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*[ { **both** \| **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x1309_x3271_x862964673}

[**[undo mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ mirroring-vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1309_x3271_1303245840}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x607360201}

[[镜像组没有源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_244248864}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1174348627}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1351234032}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x981897343}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_738239291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_1547924566}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1147244472}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_x2065048061}[：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_x1309_x3271_2096146326}[：源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-list ]{lang="EN-US"}*[= { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。当使用]{style="font-family:宋体"}**[to]{lang="EN-US"}**[参数配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围时，终止]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号必须大于等于起始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_x1309_x3271_x599116545}[：表示对源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[收发的报文都进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1239281965}[：表示仅对源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[收到的报文进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1351299568}[：表示仅对源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[发出的报文进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x1309_x3271_5478926}

[[只能为本地镜像组或远程源镜像组配置源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_1331421281}[，不能为远程目的镜像组配置源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_x1443127292}[只能配置为一个镜像组的源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1664926324}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x131264952}[创建本地镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置其源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[，并对该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[收发的报文都进行镜像。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x852422784}

[\[Sysname\] mirroring-group 1 local]{lang="EN-US"}

[\[Sysname\] mirroring-group 1 mirroring-vlan 1 both]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1746536795}[创建远程源镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，配置其源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[，并对该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[收发的报文都进行镜像。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351365104}

[\[Sysname\] mirroring-group 2 remote-source]{lang="EN-US"}

[\[Sysname\] mirroring-group 2 mirroring-vlan 2 both]{lang="EN-US"}

[]{#struct_0_x1309_x3271_x148748389}[]{#_Toc272157634}[]{#_Toc272391014}[]{#_Toc272393527}[]{#_Toc272157636}[]{#_Toc272391016}[]{#_Toc272393529}[]{#_Toc225828713}[]{#_Toc226253381}[【相关命令】]{style="font-family:
黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1908951471}
:::::

::::::: {#1256297412 .myid}
[]{#_Toc404797197}[]{#struct_0_x1309_x3271_x924577908}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group monitor-egress**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_x1926853474}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_x179808679}
:::

[ ]{lang="EN-US"}

[**[mirroring-group monitor-egress]{lang="EN-US"}**]{#struct_0_x1309_x3271_1148149288}[命令用来为远程源镜像组配置出端口。]{style="font-family:
宋体"}

[**[undo mirroring-group monitor-egress]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1518772958}[命令用来删除远程源镜像组的指定出端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x2030610208}

[[在系统视图下：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1351430640}

[**[mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ monitor-egress ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_703027377}

[**[undo mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ monitor-egress ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_87781363}

[[在接口视图下：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_2040717748}

[**[mirroring-group]{lang="EN-US"}***[ group-id]{lang="EN-US"}***[ monitor-egress]{lang="EN-US"}**]{#struct_0_x1309_x3271_x680529869}

[**[undo mirroring-group]{lang="EN-US"}***[ group-id]{lang="EN-US"}***[ monitor-egress]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1866328941}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1243674308}

[[镜像组没有出端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x959549144}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x2053168469}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351496176}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1116123356}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_185575226}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_1225079680}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_279858507}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_x607933918}[：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_1372224810}[：表示出端口。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_618727348}

[[只能为远程源镜像组配置出端口，不能为本地镜像组和远程目的镜像组配置出端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x116857576}

[[对于出端口，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1351561712}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请不要将出端口加入到源]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1536569547}[VLAN]{lang="EN-US"}[中，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请不要在出端口上配置下列功能：生成树协议、]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1527858352}[802.1X]{lang="EN-US"}[、]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[、静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[出端口不能是现有镜像组的成员端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x2098014284}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image002.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_x291112088}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[出端口是否可以为聚合成员端口与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_x1506329500}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x535972631}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x678114258}[创建远程源镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并在系统视图下配置其出端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351627248}

[\[Sysname\] mirroring-group 1 remote-source]{lang="EN-US"}

[\[Sysname\] mirroring-group 1 monitor-egress gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_986158360}[创建远程源镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，并在接口视图下配置其出端口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x878129374}

[\[Sysname\] mirroring-group 2 remote-source]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] mirroring-group 2 monitor-egress]{lang="EN-US"}[]{#_Toc133401309}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_675539076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_x304216338}
:::::::

::::: {#-52432472 .myid}
[]{#_Toc404797198}[]{#struct_0_x1309_x3271_x1544103437}[]{#_Toc133401313}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group monitor-port (interface view)**

------------------------------------------------------------------------

[**[mirroring-group]{lang="EN-US"}***[ ]{lang="EN-US"}***[monitor-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1535565201}[命令用来配置当前端口为镜像组的目的端口。]{style="font-family:宋体"}

[**[undo mirroring-group]{lang="EN-US"}***[ ]{lang="EN-US"}***[monitor-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_1754925362}[命令用来取消当前端口为指定镜像组的目的端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1351692784}

[**[mirroring-group]{lang="EN-US"}***[ group-id ]{lang="EN-US"}***[monitor-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_493012896}

[**[undo]{lang="EN-US"}**[ **mirroring-group** *group-id* **monitor-port**]{lang="EN-US"}]{#struct_0_x1309_x3271_1934861453}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x670916741}

[[端口不是任何镜像组的目的端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x133579135}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_890835632}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x41867512}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x481808210}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_x1761566571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_869383372}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1350709744}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_1522924548}[：指定镜像组。]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1803067312}

[[只能为本地镜像组或远程目的镜像组配置目的端口，不能为远程源镜像组配置目的端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1508131741}

[[对于目的端口，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x15820695}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请不要将目的端口加入到源]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1761949248}[VLAN]{lang="EN-US"}[中，或在目的端口上使能生成树协议，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当二层聚合接口作为目的端口时，请勿将其成员端口配置为源端口或将其加入源]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1500455531}[VLAN]{lang="EN-US"}[，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从目的端口发出的报文包括镜像报文和其他端口正常转发来的报文。为了保证数据监测设备只对镜像报文进行分析，请将目的端口只用于端口镜像，不作其他用途。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1295018607}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目的端口不能是现有镜像组的成员端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_983544789}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image001.png){#图片 7 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_x1350775280}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[不同型号的设备支持为本地镜像组配置目的端口的接口视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_864761964}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[不同型号的设备支持为远程目的镜像组配置目的端口的接口视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_1986164395}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[目的端口是否可以为聚合成员端口，以及目的端口还存在其他何种限制与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_x449558088}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1152169487}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1405637927}[创建本地镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并配置其目的端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_505643383}

[\[Sysname\] mirroring-group 1 local]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mirroring-group 1 monitor-port]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x134170943}[创建远程目的镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，并配置其目的端口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351234031}

[\[Sysname\] mirroring-group 2 remote-destination]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] mirroring-group 2 monitor-port]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1385181870}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_981118917}
:::::

::::: {#-1577386646 .myid}
[]{#_Toc404797199}[]{#struct_0_x1309_x3271_1642091342}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group monitor-port (system view)**

------------------------------------------------------------------------

[**[mirroring-group monitor-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_x132990860}[命令用来为镜像组配置目的端口。]{style="font-family:
宋体"}

[**[undo mirroring-group monitor-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1018830094}[命令用来删除镜像组的指定目的端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_370142064}

[**[mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ monitor-port ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x789242897}

[**[undo mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ monitor-port ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1351299567}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1571562867}

[[镜像组没有目的端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x153346665}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1351365103}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1714832330}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_45679116}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_1359263742}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_x286734458}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1466439542}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_299967239}[：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1633590479}[：表示目的端口。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。不同设备支持的本地镜像组目的端口和远程目的镜像组目的端口的端口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_400806574}

[[只能为本地镜像组或远程目的镜像组配置目的端口，不能为远程源镜像组配置目的端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1351430639}

[[对于目的端口，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1219090316}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请不要将目的端口加入到源]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1657387902}[VLAN]{lang="EN-US"}[中，或在目的端口上使能生成树协议，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当二层聚合接口作为目的端口时，请勿将其成员端口配置为源端口或将其加入源]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1910773542}[VLAN]{lang="EN-US"}[，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从目的端口发出的报文包括镜像报文和其他端口正常转发来的报文。为了保证数据监测设备只对镜像报文进行分析，请将目的端口只用于端口镜像，不作其他用途。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1831396110}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目的端口不能是现有镜像组的成员端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_501399068}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image003.png){#图片 8 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_x2120617198}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[目的端口是否可以为聚合成员端口，以及目的端口还存在其他何种限制，与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_x803771930}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x141859293}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351496175}[创建本地镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并配置其目的端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1612759999}

[\[Sysname\] mirroring-group 1 local]{lang="EN-US"}

[\[Sysname\] mirroring-group 1 monitor-port gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x1754882364}[创建远程目的镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，并配置其目的端口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x636602968}

[\[Sysname\] mirroring-group 2 remote-destination]{lang="EN-US"}

[\[Sysname\] mirroring-group 2 monitor-port gigabitethernet 1/0/2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1471034356}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_162531965}
:::::

::::::: {#-1513864537 .myid}
[]{#_Toc404797200}[]{#struct_0_x1309_x3271_x242312}[]{#_Toc133401310}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group reflector-port**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image001.png){#图片 9 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351561711}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_x29514394}
:::

[ ]{lang="EN-US"}

[**[mirroring-group reflector-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_1013041101}[命令用来为远程源镜像组配置反射端口。]{style="font-family:
宋体"}

[**[undo mirroring-group reflector-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_1029017738}[命令用来删除远程源镜像组的指定反射端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_200195910}

[[在系统视图下：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_975384467}

[**[mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ reflector-port ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1347391173}

[**[undo mirroring-group ]{lang="EN-US"}***[group-id]{lang="EN-US"}***[ reflector-port ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_1596045012}

[[在接口视图下：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1068910978}

[**[mirroring-group]{lang="EN-US"}***[ group-id]{lang="EN-US"}***[ reflector-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_1834936140}

[**[undo mirroring-group]{lang="EN-US"}***[ group-id]{lang="EN-US"}***[ reflector-port]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1351627247}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x223695221}

[[镜像组没有反射端口，端口不是任何镜像组的反射端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_82944967}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1265093909}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1309_x3271_x258331330}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_682261904}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_x1269092700}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351692783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_2059096837}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_400841969}[：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1501878057}[：表示反射端口。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1350709743}

[[只能为远程源镜像组配置反射端口，不能为本地镜像组和远程目的镜像组配置反射端口。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1926209075}

[[对于反射端口，需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x948286058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请不要将反射端口加入到源]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1400329477}[VLAN]{lang="EN-US"}[中，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议选择设备上未被使用的端口作为反射端口，并不要在该端口上连接网线，否则会影响镜像功能的正常使用。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1484995967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在将端口配置为反射端口时，该端口上已存在的所有配置都将被清除；在配置为反射端口后，该端口上不能再配置其他业务。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x486163116}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于某些型号的设备，只有当端口的双工模式、端口速率和]{style="font-family:宋体"}]{#struct_0_x1309_x3271_2141114317}[MDI]{lang="EN-US"}[属性值均为缺省值时，才能将其配置为反射端口，请以设备的实际情况为准。当端口已配置为反射端口后，不能再修改其双工模式、端口速率和]{style="font-family:宋体"}[MDI]{lang="EN-US"}[属性值，即这些属性只能取缺省值。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image002.png){#图片 10 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_x528849785}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[反射端口是否可以为聚合成员端口与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_69147478}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1350775279}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x346074657}[创建远程源镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并在系统视图下配置其反射端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1839579655}

[\[Sysname\] mirroring-group 1 remote-source]{lang="EN-US"}

[\[Sysname\] mirroring-group 1 reflector-port gigabitethernet 1/0/1]{lang="EN-US"}

[This operation may delete all settings made on the interface. Continue? \[Y/N\]: y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x116080014}[创建远程源镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，并在接口视图下配置其反射端口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_1335022008}

[\[Sysname\] mirroring-group 2 remote-source]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] mirroring-group 2 reflector-port]{lang="EN-US"}

[This operation may delete all settings made on the interface. Continue? \[Y/N\]: y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1692729775}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_x1351234034}
:::::::

::::: {#1772545038 .myid}
[]{#_Toc404797201}[]{#struct_0_x1309_x3271_x1788466397}[]{#_Toc133401311}

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group remote-probe vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image001.png){#图片 11 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_341777320}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_2084675317}
:::

[ ]{lang="EN-US"}

[**[mirroring-group remote-probe vlan]{lang="EN-US"}**]{#struct_0_x1309_x3271_949858875}[命令用来为镜像组配置远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo mirroring-group remote-probe vlan]{lang="EN-US"}**]{#struct_0_x1309_x3271_948687191}[命令用来删除镜像组的指定远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1773210268}

[**[mirroring-group ]{lang="EN-US"}***[group-id ]{lang="EN-US"}***[remote-probe vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_x62835382}

[**[undo mirroring-group ]{lang="EN-US"}***[group-id ]{lang="EN-US"}***[remote-probe vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_1279155941}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1351299570}

[[镜像组没有远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_x350685898}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1830661067}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1768316872}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_42553458}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_x1182478933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_734492525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x913584795}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1812093709}[：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1351365106}[：表示远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1311547803}

[[只有为远程源镜像组和远程目的镜像组配置远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_x376245442}[，不能为本地镜像组配置远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[对于远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1309_x3271_732520362}[，需要注意的是：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当一个]{style="font-family:宋体"}]{#struct_0_x1309_x3271_879851499}[VLAN]{lang="EN-US"}[已被指定为远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[后，请不要将该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[再作其他用途。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[源设备和目的设备上的远程镜像组必须使用相同的远程镜像]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1674527829}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能将已存在的静态]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x746161300}[VLAN]{lang="EN-US"}[配置为远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，且一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[只能配置为一个镜像组的远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当某]{style="font-family:宋体"}]{#struct_0_x1309_x3271_190874981}[VLAN]{lang="EN-US"}[被配置为远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[后，必须先删除远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的配置才能删除该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1455635709}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351430642}[创建远程源镜像组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并为其配置远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x459772037}

[\[Sysname\] mirroring-group 1 remote-source]{lang="EN-US"}

[\[Sysname\] mirroring-group 1 remote-probe vlan 10]{lang="EN-US"}

[]{#_Toc133401312}[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_933497209}[创建远程目的镜像组]{style="font-family:宋体"}[2]{lang="EN-US"}[，并为其配置远程镜像]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_1821056315}

[\[Sysname\] mirroring-group 2 remote-destination]{lang="EN-US"}

[\[Sysname\] mirroring-group 2 remote-probe vlan 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1625574057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mirroring-group]{lang="EN-US"}**]{#struct_0_x1309_x3271_2043830475}

[ ]{lang="EN-US"}
:::::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::::: {#-405820719 .myid}
[]{#_Toc404797204}[]{#struct_0_x1309_x3271_x2016044526}[]{#_Toc304900346}[]{#_Toc293320012}

**流镜像 \-- 流镜像配置命令 \-- mirror-to**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](镜像命令.files/image002.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1309_x3271_x1047037338}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1309_x3271_x1236835754}
:::

**[ ]{lang="EN-US"}**

[**[mirror-to]{lang="EN-US"}**]{#struct_0_x1309_x3271_x720191831}[命令用来在流行为中配置流量的目的地。]{style="font-family:宋体"}

[**[undo mirror-to]{lang="EN-US"}**]{#struct_0_x1309_x3271_x255363728}[命令用来取消流行为中流量的目的地的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_578524249}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1309_x3271_2145189941}

[**[mirror-to]{lang="EN-US"}**[ { **cpu** \| **interface** *interface-type* *interface-number* \[ **backup-interface** *interface-type* *interface-number* \] \[ **sampler** *sampler-name* \] \| **vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_x1309_x3271_x2014544510}

[**[undo mirror-to]{lang="EN-US"}**[ { **cpu** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_x1309_x3271_x251216254}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1309_x3271_x800436125}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[mirror-to]{lang="EN-US"}**[ { **cpu** \| { **interface** *interface-type* *interface-number* \[ **backup-interface** *interface-type* *interface-number* \] \| **slot** *slot-number* \[ **backup slot** *slot-number* \] } \[ **sampler** *sampler-name* \] \| **vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_x1309_x3271_x841164134}

[**[undo mirror-to]{lang="EN-US"}**[ { **cpu** \| **interface** *interface-type* *interface-number* \| **slot** *slot-number* \| **vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_x1309_x3271_x211075490}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1309_x3271_225456001}[模式：]{style="font-family:宋体"}

[**[mirror-to]{lang="EN-US"}**[ { **cpu** \| { **interface** *interface-type* *interface-number* \[ **backup-interface** *interface-type* *interface-number* \] \| **chassis** *chassis-number* **slot** *slot-number* \[ **backup chassis** *chassis-number* **slot** *slot-number* \] } \[ **sampler** *sampler-name* \] \| **vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_x1309_x3271_2145255477}

[**[undo mirror-to]{lang="EN-US"}**[ { **cpu** \| **interface** *interface-type* *interface-number* \| **chassis** *chassis-number* **slot** *slot-number* \| **vlan** *vlan-id* }]{lang="EN-US"}]{#struct_0_x1309_x3271_1152440637}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1351561714}

[[流行为中未配置流量的目的地。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_373770133}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_267491361}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1165845544}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x51114489}

[[network-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_1849009276}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1309_x3271_743398734}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x1095655767}

[**[cpu]{lang="EN-US"}**]{#struct_0_x1309_x3271_1129990895}[：表示流镜像到]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，这里的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[是指报文进入的单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1309_x3271_x1641205054}[：表示流镜像到指定接口，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。本参数的支持情况以及支持的接口类型都与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[backup-interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351627250}[：表示流镜像的备份接口，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。只有当]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}[参数指定的接口出现故障时，流量才可以被镜像到备份接口。本参数的支持情况以及支持的接口类型都与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[sampler]{lang="EN-US"}**[ *sampler-name*]{lang="EN-US"}]{#struct_0_x1309_x3271_1342454256}[：表示流镜像引用的采样器，]{style="font-family:宋体"}*[sampler-name]{lang="EN-US"}*[为采样器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1309_x3271_1159295201}[：表示流镜像到指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_2145321013}[：]{style="font-family:宋体"}[表示流镜像到指定单板。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1737627073}[：]{style="font-family:宋体"}[表示流镜像到指定成员设备。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1561376689}[：]{style="font-family:宋体"}[表示流镜像到指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[backup slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1561875636}[：]{style="font-family:宋体"}[表示流镜像的备份单板。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[backup slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x985043250}[：]{style="font-family:宋体"}[表示流镜像的备份成员设备。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[backup slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x756924158}[：]{style="font-family:宋体"}[表示流镜像的备份成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_2144862261}[：表示流镜像到指定成员设备的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。（分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_368451708}[：表示流镜像到指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[backup chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_1961250077}[：表示流镜像的指定成员设备的备份单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。本参数的支持情况以及支持的接口类型都与设备的型号有关，请以设备的实际情况为准。（分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[backup chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1309_x3271_x1561573297}[：表示流镜像的备份单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。本参数的支持情况以及支持的接口类型都与设备的型号有关，请以设备的实际情况为准。（分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_1768611404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备支持流镜像到多个接口，则在同一流行为中可以通过多次配置将流镜像到不同接口；如果设备只支持流镜像到一个接口，则在同一流行为中新的配置将覆盖旧的配置。是否支持流镜像到多个接口与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1329121316}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在同一流行为中多次配置流镜像到]{style="font-family:宋体"}]{#struct_0_x1309_x3271_1772988509}[VLAN]{lang="EN-US"}[，新的配置将覆盖旧的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采样器用来从一组固定数量的报文中选出一个报文。流镜像通过引用采样器，可以对镜像报文进行采样而减少镜像报文的数量。流镜像支持引用一个未创建的采样器。如果在流镜像多次配置采样器，新的配置将覆盖旧的配置。有关采样器的相关配置，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}]{#struct_0_x1309_x3271_775917319}[Sampler]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备支持流镜像到多个单板，则在同一流行为中可以通过多次配置将流镜像到不同单板；如果设备只支持流镜像到一个单板，则在同一流行为中新的配置将覆盖旧的配置。（分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x327461873}[/]{lang="EN-US"}[分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备支持流镜像到多台设备，则在同一流行为中可以通过多次配置将流镜像到不同设备；如果设备只支持流镜像到一台设备，则在同一流行为中新的配置将覆盖旧的配置。（]{style="font-family:宋体"}]{#struct_0_x1309_x3271_x1737627072}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1309_x3271_x212357727}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1262765785}[配置流行为]{style="font-family:宋体"}[1]{lang="EN-US"}[，并在该流行为中配置流镜像到]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1351692786}

[\[Sysname\] traffic behavior 1]{lang="EN-US"}

[\[Sysname-behavior-1\] mirror-to cpu]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_1655812310}[配置流行为]{style="font-family:宋体"}[1]{lang="EN-US"}[，并在该流行为中配置流镜像到接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x2035926317}

[\[Sysname\] traffic behavior 1]{lang="EN-US"}

[\[Sysname-behavior-1\] mirror-to interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_x1535507688}[配置流行为]{style="font-family:宋体"}[1]{lang="EN-US"}[，并在该流行为中配置流镜像到]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1908858971}

[\[Sysname\] traffic behavior 1]{lang="EN-US"}

[\[Sysname-behavior-1\] mirror-to vlan 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_286658455}[配置流行为]{style="font-family:宋体"}[1]{lang="EN-US"}[，在该流行为中配置流镜像到接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[并引用采样器]{style="font-family:宋体"}[samp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_x1350709746}

[\[Sysname\] traffic behavior 1]{lang="EN-US"}

[\[Sysname-behavior-1\] mirror-to interface gigabitethernet 1/0/1 sampler samp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1309_x3271_2144927797}[配置流行为]{style="font-family:宋体"}[1]{lang="EN-US"}[，在该流行为中配置流镜像到单板]{style="font-family:宋体"}[1]{lang="EN-US"}[并引用采样器]{style="font-family:宋体"}[samp]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1309_x3271_1181413116}

[\[Sysname\] traffic behavior 1]{lang="EN-US"}

[\[Sysname-behavior-1\] mirror-to slot 1 sampler samp]{lang="EN-US"}

[ ]{lang="EN-US"}
:::::
