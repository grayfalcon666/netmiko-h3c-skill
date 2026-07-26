::: {#1742433432 .myid}
[]{#_Toc348095196}[]{#_Toc404785233}[]{#struct_0_19500_x1656_x1908919557}[]{#_Toc350872242}[]{#_Toc345946912}

**ATM \-- ATM配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_19500_x1656_973183433}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_19500_x1656_625631553}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1097678877}

[**[bandwidth]{lang="EN-US"}***[ bandwidth-value]{lang="EN-US"}*]{#struct_0_19500_x1656_1997409708}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_19500_x1656_x1384497482}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x664196273}

[[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_19500_x1656_1767957722}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2019458333}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_266172675}[接口视图]{style="font-family:宋体"}[/VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x268041518}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x133982982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1404449738}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_14827760}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_19500_x1656_x1266528022}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1972652262}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_19500_x1656_2005736949}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1768023258}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1418415711}[配置]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[50kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_71327702}

[\[Sysname\] interface virtual-ethernet 2/4/1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet2/4/1\] bandwidth 50]{lang="EN-US"}
:::

::: {#-389412524 .myid}
[]{#_Toc404785234}[]{#struct_0_19500_x1656_717292691}

**ATM \-- ATM配置命令 \-- broadcast**

------------------------------------------------------------------------

[**[broadcast]{lang="EN-US"}**]{#struct_0_19500_x1656_x26552307}[命令用来打开当前]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的广播属性。]{style="font-family:宋体"}

[**[undo broadcast]{lang="EN-US"}**]{#struct_0_19500_x1656_x617709831}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1074266873}

[**[broadcast]{lang="EN-US"}**]{#struct_0_19500_x1656_x1901727508}

[**[undo broadcast]{lang="EN-US"}**]{#struct_0_19500_x1656_1768088794}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_223457004}

[[广播属性处于关闭状态。]{style="font-family:宋体"}]{#struct_0_19500_x1656_863701185}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_434813451}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x822453243}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x87597267}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x266277867}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x344764199}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x910147826}

[[如果某]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x2058205517}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[配置了广播属性，则]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[所属接口上的广播或组播报文都要在该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[上发送一份。]{style="font-family:宋体"}

[[如果在]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1768154330}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[上需要发送广播或者组播报文，请务必配置此关键字。例如：]{style="font-family:宋体"}[PIM]{lang="EN-US"}[组播如果要想在以]{style="font-family:宋体"}[ATM]{lang="EN-US"}[链路相连的路由器间建立]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居，则链路两端的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[必须配置广播属性，因为建立]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居时需要通过]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口来发送]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播报文。]{style="font-family:宋体"}

[[本命令不能在]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x654957031}[下的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[下配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1614429519}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x334970565}[打开]{style="font-family:宋体"}[PVC 0/100]{lang="EN-US"}[的广播属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x534256910}

[\[Sysname\] interface atm 2/4/1.1]{lang="EN-US"}

[\[Sysname-ATM2/4/1.1\] pvc 0/100]{lang="EN-US"}

[\[Sysname-ATM2/4/1.1-pvc-0/100\] broadcast]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404785235}[]{#struct_0_19500_x1656_165279931}[]{#_Toc350872243}[]{#_Toc345946913}

**ATM \-- ATM配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_19500_x1656_363484395}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x167739448}

[**[default]{lang="EN-US"}**]{#struct_0_19500_x1656_1768219866}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1028185134}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_1101270146}[接口视图]{style="font-family:宋体"}[/VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1974019120}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x11658346}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1795394385}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_874450926}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_19500_x1656_1487107722}

[[您可以在执行]{style="font-family:宋体"}]{#struct_0_19500_x1656_x578431710}**[default]{lang="EN-US"}**[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1768285402}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x616719596}[将]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_1861878531}

[\[Sysname\] interface virtual-ethernet 2/4/1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet2/4/1\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404785236}[]{#struct_0_19500_x1656_717991405}[]{#_Toc350872244}[]{#_Toc345946914}[]{#_Toc349121969}[]{#_Toc349122126}[]{#_Toc349121997}[]{#_Toc349122154}

**ATM \-- ATM配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_19500_x1656_x87494957}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_19500_x1656_955246956}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x822447505}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_19500_x1656_x1226339139}

[**[undo description]{lang="EN-US"}**]{#struct_0_19500_x1656_578075646}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1768350938}

[[接口的描述信息为"]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1069394965}*[该接口的接口名]{style="font-family:宋体"}* [Interface]{lang="EN-US"}["，比如：]{style="font-family:宋体"}[Virtual-Ethernet2/4/1 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x924239064}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_x1209787869}[接口视图]{style="font-family:宋体"}[/VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x368847845}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1178381823}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1617428900}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1678779689}

[*[text]{lang="EN-US"}*]{#struct_0_19500_x1656_x1872872628}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1768416474}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_2088636136}[配置]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[Virtual-Ethernet]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x1684515736}

[\[Sysname\] interface virtual-ethernet 2/4/1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet2/4/1\] description Virtual-Ethernet]{lang="EN-US"}
:::

::: {#-1424534882 .myid}
[]{#_Toc404785237}[]{#struct_0_19500_x1656_x1626468289}[]{#_Toc348095174}[]{#_Toc328667708}

**ATM \-- ATM配置命令 \-- display atm map-info**

------------------------------------------------------------------------

[**[display atm map-info]{lang="EN-US"}**]{#struct_0_19500_x1656_x196418252}[命令用来显示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x368803504}

[**[display atm map-info]{lang="EN-US"}**[ \[ **interface** *interface-type* { *interface-number* \| *interface-number.subnumber* } \[ **pvc** { *pvc-name* \| *vpi/vci* } \| **pvc-group** *group-number* \] \]]{lang="EN-US"}]{#struct_0_19500_x1656_827424665}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x131659151}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_1767433434}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1621446373}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_2077854796}

[[network-operator]{lang="EN-US"}]{#struct_0_19500_x1656_328530419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1125564156}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19500_x1656_x621776216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1241638845}

[**[interface]{lang="EN-US"}**[ *interface-type* { *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_19500_x1656_x656199050}[：显示指定接口的映射信息。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}**]{#struct_0_19500_x1656_x1820908995}[：显示指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的映射信息。]{style="font-family:宋体"}

[*[pvc-name]{lang="EN-US"}*]{#struct_0_19500_x1656_1767498970}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名中不允许使用"]{style="font-family:宋体"}[/]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，如"]{style="font-family:宋体"}[1/20]{lang="EN-US"}["、"]{style="font-family:宋体"}[a-b]{lang="EN-US"}["就不允许作为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}

[*[vpi/vci]{lang="EN-US"}*]{#struct_0_19500_x1656_x1597657490}[：]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPI]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[为]{style="font-family:宋体"}[VCI]{lang="EN-US"}[值，取值范围与接口类型相关，请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?-1864992396#_Ref337389143)["。]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[与]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[不能同时为]{style="font-family:宋体"}[0]{lang="EN-US"}[。通常，]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[取值]{style="font-family:宋体"}[0]{lang="EN-US"}[到]{style="font-family:宋体"}[31]{lang="EN-US"}[保留用于特定用途，建议用户不要使用。]{style="font-family:宋体"}

[**[pvc-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_19500_x1656_1303757714}[：显示指定]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的映射信息。]{style="font-family:宋体"}*[group-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_2091745627}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口，则显示所有接口下]{style="font-family:宋体"}]{#struct_0_19500_x1656_x992957984}[所有]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的映射信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口而不指定]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1190356179}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[，则显示指定接口下所有]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的映射信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口并且指定]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1588147321}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[，则显示指定接口下指定]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的映射信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1205541326}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1395169248}[显示所有接口下所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[和]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display atm map-info]{lang="EN-US"}]{#struct_0_19500_x1656_1767957723}

[ATM2/4/0]{lang="EN-US"}

[  PVC 1/32:]{lang="EN-US"}

[    Protocol: PPP, Interface: Virtual-Template10, State: UP]{lang="EN-US"}

[    Protocol: IP, IP address: 100.11.1.1, State: UP]{lang="EN-US"}

[  PVC-group 1:]{lang="EN-US"}

[    Protocol: IP InARP, IP address: 100.22.22.2, Interval: 2 minutes, State: UP]{lang="EN-US"}

[    Protocol: ETH, Interface: Virtual-Ethernet2, State: UP]{lang="EN-US"}

[ATM2/4/1]{lang="EN-US"}

[  PVC 2/32:]{lang="EN-US"}

[    Protocol: IP InARP, IP address: no IP address, Interval: 3 minutes, State: UP]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display atm map-info]{lang="EN-US"}]{#struct_0_19500_x1656_x2019523869}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1629839683}[[字段]{style="font-family:黑体"}]{#struct_0_19500_x1656_1848164167}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19500_x1656_788754765}

[[ATM2/4/0]{lang="EN-US"}]{#struct_0_19500_x1656_x1759200481}

[[接口名称]{style="font-family:宋体"}]{#struct_0_19500_x1656_1768023259}

[[PVC 1/32]{lang="EN-US"}]{#struct_0_19500_x1656_x1418350175}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1942515072}[的]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值对]{style="font-family:宋体"}

[[PVC-group 1]{lang="EN-US"}]{#struct_0_19500_x1656_x151198371}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x855730471}[名称]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_19500_x1656_x1519324501}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1893673377}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[支持的上层协议的类型，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_19500_x1656_1768088795}[：]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_223522540}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP InARP ]{lang="EN-US"}]{#struct_0_19500_x1656_1659355473}[：]{lang="EN-US" style="font-family:宋体"}[IP InARP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ETH]{lang="EN-US"}]{#struct_0_19500_x1656_433446445}[：以太网协议]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_19500_x1656_x900518347}

[[对应映射的状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_1768154331}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_x655022567}[：对于]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[（包括]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[）映射，表示其]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[状态为]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}[；对于]{lang="EN-US" style="font-family:宋体"}[ETH]{lang="EN-US"}[映射，表示其]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[状态和]{lang="EN-US" style="font-family:宋体"}[VE]{lang="EN-US"}[口状态均为]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_x1647703956}[：对于]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[（包括]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[）映射，表示其]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[状态为]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}[；对于]{lang="EN-US" style="font-family:宋体"}[ETH]{lang="EN-US"}[映射，表示其]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[状态和]{lang="EN-US" style="font-family:宋体"}[VE]{lang="EN-US"}[口状态至少一个为]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[IP address]{lang="EN-US"}]{#struct_0_19500_x1656_x782060521}

[[IP]{lang="EN-US"}]{#struct_0_19500_x1656_x1101642745}[地址]{style="font-family:宋体"}

[[Interval]{lang="EN-US"}]{#struct_0_19500_x1656_1768219867}

[[发送]{style="font-family:宋体"}[InARP]{lang="EN-US"}]{#struct_0_19500_x1656_x1028250670}[报文的间隔时间，单位为分钟]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_19500_x1656_2014113212}

[[承载]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}]{#struct_0_19500_x1656_1313118833}[或]{style="font-family:宋体"}[EoA]{lang="EN-US"}[的虚拟接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-892522285 .myid}
[]{#_Toc404785238}[]{#struct_0_19500_x1656_278112733}[]{#_Toc348095175}

**ATM \-- ATM配置命令 \-- display atm pvc-group**

------------------------------------------------------------------------

[**[display atm pvc-group]{lang="EN-US"}**]{#struct_0_19500_x1656_x212285345}[命令用来显示]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1110822968}

[**[display atm pvc-group]{lang="EN-US"}**[ \[ **interface** *interface-type* { *interface-number* \| *interface-number.subnumber* } \[ **pvc-group** *group-number* \] \]]{lang="EN-US"}]{#struct_0_19500_x1656_1768285403}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x616654060}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_x829119156}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1689183675}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1589766413}

[[network-operator]{lang="EN-US"}]{#struct_0_19500_x1656_x184721339}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1566328405}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19500_x1656_x1631025322}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1768350939}

[**[interface]{lang="EN-US"}**[ *interface-type* { *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_19500_x1656_x1069460501}[：显示指定接口的]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[信息。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[**[pvc-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_19500_x1656_1231263777}[：显示指定]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[group-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1120569849}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口，则显示所有接口的]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_513428652}[的简要信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口而不指定]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x1572922591}[，则显示指定接口的所有]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的简要信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口并且指定]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x383732739}[，则显示指定接口的指定]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的详细信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x421307430}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_472157279}[显示所有接口的]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display atm pvc-group]{lang="EN-US"}]{#struct_0_19500_x1656_1768416475}

[ATM2/4/0, State UP]{lang="EN-US"}

[  PVC-group: 1]{lang="EN-US"}

[    Encapsulation: SNAP, Protocol: IP]{lang="EN-US"}

[    VPI/VCI  PVC name   Precedence        State]{lang="EN-US"}

[    1/32     aa         Default           UP]{lang="EN-US"}

[    2/32     N/A        2-3               UP]{lang="EN-US"}

[    3/32     N/A        5                 UP]{lang="EN-US"}

[  PVC-group: 3]{lang="EN-US"}

[    Encapsulation: SNAP, Protocol: IP]{lang="EN-US"}

[    VPI/VCI  PVC name   Precedence        State]{lang="EN-US"}

[    3/64     bb         4                 UP]{lang="EN-US"}

[    4/64     N/A        Default           UP]{lang="EN-US"}

[ ]{lang="EN-US"}

[ATM2/4/1, State UP]{lang="EN-US"}

[  PVC-group: 1]{lang="EN-US"}

[    Encapsulation: SNAP, Protocol: IP]{lang="EN-US"}

[    VPI/VCI  PVC name   Precedence        State]{lang="EN-US"}

[    1/32     aa         Default           UP]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display atm pvc-group]{lang="EN-US"}]{#struct_0_19500_x1656_2088570600}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1628664732}[[字段]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2046792940}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19500_x1656_1767433435}

[[ATM2/4/0, State UP ]{lang="EN-US"}]{#struct_0_19500_x1656_x1621511909}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x1677080407}[所属的接口名及接口物理状态和管理状态]{style="font-family:宋体"}

[[如果不是子接口，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x589198596}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_217685893}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_944210601}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）或者该接口已经通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{style="font-family:宋体"}

[[如果是子接口，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x324360674}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_1767498971}[：该接口的管理状态和其父接口的物理状态和管理状态均为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_x1597723026}[：表示该接口或其父接口已经通过]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[命令被关闭或者其父接口物理状态为关闭]{style="font-family:宋体"}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_977236073}[：]{style="font-family:宋体"}[1]{lang="EN-US"}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_1481528110}[对应的]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Encapsulation]{lang="EN-US"}]{#struct_0_19500_x1656_x191901192}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x1180716552}[的]{style="font-family:宋体"}[AAL5]{lang="EN-US"}[封装类型，目前只可能取值]{style="font-family:宋体"}[SNAP]{lang="EN-US"}[，表示]{style="font-family:宋体"}[LLC]{lang="EN-US"}[（]{style="font-family:宋体"}[Logical Link Control]{lang="EN-US"}[，逻辑链接控制）]{style="font-family:宋体"}[/SNAP]{lang="EN-US"}[（]{style="font-family:宋体"}[Subnet Access Protocol]{lang="EN-US"}[，子网访问协议）封装类型]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_19500_x1656_1767957720}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x2019327261}[支持的上层协议的类型，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_19500_x1656_2040732261}[：]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_1633439238}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ETH]{lang="EN-US"}]{#struct_0_19500_x1656_x1653455658}[：以太协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_19500_x1656_1768023256}[：未配置任何协议]{lang="EN-US" style="font-family:宋体"}

[[VPI/VCI]{lang="EN-US"}]{#struct_0_19500_x1656_x1418808927}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_81068945}[的]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值对]{style="font-family:宋体"}

[[PVC name]{lang="EN-US"}]{#struct_0_19500_x1656_982443882}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x968886818}[名称，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示没有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Precedence]{lang="EN-US"}]{#struct_0_19500_x1656_1768088792}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_223850220}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的优先级，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Default]{lang="EN-US"}]{#struct_0_19500_x1656_x1782779405}[：表示该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[为缺省]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，则没有指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的优先级别的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包将从缺省]{style="font-family:宋体"}[PVC]{lang="EN-US"}[进行传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a-b]{lang="EN-US"}]{#struct_0_19500_x1656_x82908222}[：表示该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的最小优先级到最大优先级（]{style="font-family:宋体"}[a]{lang="EN-US"}[，]{style="font-family:宋体"}[b]{lang="EN-US"}[表示数字]{style="font-family:宋体"}[0\~7]{lang="EN-US"}[，]{style="font-family:宋体"}[a\<b]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}]{#struct_0_19500_x1656_x876287572}[：表示该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的优先级（]{style="font-family:宋体"}[c]{lang="EN-US"}[表示数字]{style="font-family:宋体"}[0\~7]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_19500_x1656_1768154328}[：表示该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[下没有配置承载]{style="font-family:宋体"}[IP]{lang="EN-US"}[包优先级]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_19500_x1656_x655481318}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_670858734}[的状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_1785160556}[：该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态、]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态和]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态均为]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_1768219864}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态、]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态和]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态中至少其中一个为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1028054062}[显示指定]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display atm pvc-group interface atm 2/4/0 pvc-group 1]{lang="EN-US"}]{#struct_0_19500_x1656_1768285400}

[ATM2/4/0, PVC-group: 1]{lang="EN-US"}

[  Encapsulation: SNAP, Protocol: None]{lang="EN-US"}

[  PVC VPI/VCI: 0/34]{lang="EN-US"}

[    Precedence: default]{lang="EN-US"}

[    Service-type: CBR, Output-pcr: 200 kbps, CDVT: 500 us]{lang="EN-US"}

[    Transmit-Priority: 0]{lang="EN-US"}

[    OAM loopback interval: 0 sec(disabled), OAM loopback retry interval: 1 sec]{lang="EN-US"}

[    OAM loopback retry count (up/down): 3/5]{lang="EN-US"}

[    OAM AIS-RDI count (up/down): 3/1           ]{lang="EN-US"}

[    Interface State: UP, OAM State: UP, PVC State: UP]{lang="EN-US"}

[    Input: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}

[    Output: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}

[    Output queue: (Urgent queuing : Size/Length/Discards)  0/100/0]{lang="EN-US"}

[    Output queue: (Protocol queuing : Size/Length/Discards)  0/500/0]{lang="EN-US"}

[    Output queue: (FIFO queuing : Size/Length/Discards)  0/75/0]{lang="EN-US"}

[    OAM cells received: 42]{lang="EN-US"}

[      F5 Loopback: 0, F5 AIS: 42, F5 RDI: 0]{lang="EN-US"}

[    OAM cells sent: 0]{lang="EN-US"}

[      F5 Loopback: 0]{lang="EN-US"}

[    OAM cell drops: 0]{lang="EN-US"}

[    OAM AIS State: No AIS Alarm]{lang="EN-US"}

[    OAM RDI State: No RDI Alarm]{lang="EN-US"}

[    OAM CC State: No CC Alarm]{lang="EN-US"}

[  PVC VPI/VCI: 0/35]{lang="EN-US"}

[    Precedence: -]{lang="EN-US"}

[    Service-type: UBR, Output-pcr: 200 kbps]{lang="EN-US"}

[    Transmit-Priority: 0]{lang="EN-US"}

[    OAM loopback interval: 0 sec(disabled), OAM loopback retry interval: 1 sec]{lang="EN-US"}

[    OAM loopback retry count (up/down): 3/5]{lang="EN-US"}

[    OAM AIS-RDI count (up/down): 3/1]{lang="EN-US"}

[    Interface State: UP, OAM State: UP, PVC State: UP]{lang="EN-US"}

[    Input: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}

[    Output: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}

[    Output queue: (Urgent queuing : Size/Length/Discards)  0/100/0]{lang="EN-US"}

[    Output queue: (Protocol queuing : Size/Length/Discards)  0/500/0]{lang="EN-US"}

[    Output queue: (FIFO queuing : Size/Length/Discards)  0/75/0]{lang="EN-US"}

[    OAM cells received: 42]{lang="EN-US"}

[      F5 Loopback: 0, F5 AIS: 42, F5 RDI: 0]{lang="EN-US"}

[    OAM cells sent: 0]{lang="EN-US"}

[      F5 Loopback: 0]{lang="EN-US"}

[    OAM cell drops: 0]{lang="EN-US"}

[    OAM AIS State: No AIS Alarm]{lang="EN-US"}

[    OAM RDI State: No RDI Alarm]{lang="EN-US"}

[    OAM CC State: No CC Alarm]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display atm pvc-group]{lang="EN-US"}]{#struct_0_19500_x1656_x616850668}[命令指定]{style="font-family:黑体"}[PVC-group]{lang="EN-US"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1631822784}[[字段]{style="font-family:黑体"}]{#struct_0_19500_x1656_1768350936}

[[描述]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1069263893}

[[ATM2/4/0,PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_2004910434}[：]{style="font-family:宋体"}[ 1]{lang="EN-US"}

[[表示]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_752490013}[所在接口及对应的]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Encapsulation]{lang="EN-US"}]{#struct_0_19500_x1656_1548032831}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_160520866}[的]{style="font-family:宋体"}[AAL5]{lang="EN-US"}[封装类型，目前只可能取值]{style="font-family:宋体"}[SNAP]{lang="EN-US"}[，表示]{style="font-family:宋体"}[LLC]{lang="EN-US"}[（]{style="font-family:宋体"}[Logical Link Control]{lang="EN-US"}[，逻辑链接控制）]{style="font-family:宋体"}[/SNAP]{lang="EN-US"}[（]{style="font-family:宋体"}[Subnet Access Protocol]{lang="EN-US"}[，子网访问协议）封装类型]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_19500_x1656_1768416472}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_2088242920}[支持的上层协议的类型，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_19500_x1656_1811775863}[：]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_100754075}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ETH]{lang="EN-US"}]{#struct_0_19500_x1656_1839407940}[：以太协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_19500_x1656_x1543915838}[：未配置任何协议]{lang="EN-US" style="font-family:宋体"}

[[PVC VPI/ VCI]{lang="EN-US"}]{#struct_0_19500_x1656_1767433432}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1621577445}[的]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值对]{style="font-family:宋体"}

[[Precedence]{lang="EN-US"}]{#struct_0_19500_x1656_x999629710}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x17953549}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的优先级，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Default]{lang="EN-US"}]{#struct_0_19500_x1656_718233658}[：表示该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[为缺省]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，则没有指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的优先级别的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包将从缺省]{style="font-family:宋体"}[PVC]{lang="EN-US"}[进行传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a-b]{lang="EN-US"}]{#struct_0_19500_x1656_507594441}[：表示该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的最小优先级到最大优先级（]{style="font-family:宋体"}[a]{lang="EN-US"}[，]{style="font-family:宋体"}[b]{lang="EN-US"}[表示数字]{style="font-family:宋体"}[0\~7]{lang="EN-US"}[，]{style="font-family:宋体"}[a\<b]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ c]{lang="EN-US"}]{#struct_0_19500_x1656_1767498968}[：表示该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的优先级（]{style="font-family:宋体"}[c]{lang="EN-US"}[表示数字]{style="font-family:宋体"}[0\~7]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[- ]{lang="EN-US"}]{#struct_0_19500_x1656_x1598181779}[：表示该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[下没有配置承载]{style="font-family:宋体"}[IP]{lang="EN-US"}[包优先级]{style="font-family:宋体"}

[[Service-type]{lang="EN-US"}]{#struct_0_19500_x1656_x585312122}

[[服务类型，可能的类型如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x674604176}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBR]{lang="EN-US"}]{#struct_0_19500_x1656_1767957721}[：恒定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UBR]{lang="EN-US"}]{#struct_0_19500_x1656_x2019392797}[：非确定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-NRT]{lang="EN-US"}]{#struct_0_19500_x1656_342410879}[：非实时可变速率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-RT]{lang="EN-US"}]{#struct_0_19500_x1656_x1798582256}[：实时可变速率]{style="font-family:宋体"}

[[Output-pcr]{lang="EN-US"}]{#struct_0_19500_x1656_602778312}

[[输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_1768023257}[信元的峰值速率]{style="font-family:宋体"}

[[CDVT]{lang="EN-US"}]{#struct_0_19500_x1656_x1418743391}

[[信元时延变化容限（]{style="font-family:宋体"}[Cell Delay Variation Tolerance]{lang="EN-US"}]{#struct_0_19500_x1656_254486525}[），单位为微秒]{style="font-family:宋体"}

[[Transmit-Priority]{lang="EN-US"}]{#struct_0_19500_x1656_x1039017962}

[[传输优先级]{style="font-family:宋体"}]{#struct_0_19500_x1656_1768088793}

[[OAM loopback interval]{lang="EN-US"}]{#struct_0_19500_x1656_223915756}

[[发送]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_x190797214}[信元的间隔时间，单位为秒]{style="font-family:宋体"}

[[OAM loopback retry interval]{lang="EN-US"}]{#struct_0_19500_x1656_1131125476}

[[OAM F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_x469578248}[重传验证的间隔时间，单位为秒]{style="font-family:宋体"}

[[OAM loopback retry count (up/down)]{lang="EN-US"}]{#struct_0_19500_x1656_1768154329}

[[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_x655546854}[验证]{style="font-family:宋体"}[UP]{lang="EN-US"}[和]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[的信元数量]{style="font-family:宋体"}

[[OAM AIS-RDI count (up/down)]{lang="EN-US"}]{#struct_0_19500_x1656_371341002}

[[OAM AIS-RDI]{lang="EN-US"}]{#struct_0_19500_x1656_1166998820}[验证]{style="font-family:宋体"}[UP]{lang="EN-US"}[的秒数、]{style="font-family:宋体"}[OAM AIS-RDI]{lang="EN-US"}[验证]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[的信元数量]{style="font-family:宋体"}

[[Interface State]{lang="EN-US"}]{#struct_0_19500_x1656_1768219865}

[[该]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1028119598}[所属的接口名及接口物理状态和管理状态]{style="font-family:宋体"}

[[如果不是子接口，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x433950043}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_1249305332}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_1768285401}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）或者该接口已经通过]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[命令被关闭，即管理状态为关闭]{style="font-family:宋体"}

[[如果是子接口，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x616785132}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_x1249431411}[：该接口的管理状态和其父接口的物理状态和管理状态均为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_1768350937}[：表示该接口或其父接口已经通过]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[命令被关闭或者其父接口物理状态关闭]{style="font-family:宋体"}

[[OAM State]{lang="EN-US"}]{#struct_0_19500_x1656_x1069329429}

[[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_x1199104756}[协议状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_140766188}[：协议状态开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_1768416473}[：协议状态关闭]{style="font-family:宋体"}

[[PVC State]{lang="EN-US"}]{#struct_0_19500_x1656_2088177384}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_652986473}[的状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_1767433433}[：该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态、]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态和]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态均为]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_x1621642981}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态、]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态和]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态中至少其中一个为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}]{#struct_0_19500_x1656_x1585744516}

[[接收的报文数、字节数以及接收报文的错误数]{style="font-family:宋体"}]{#struct_0_19500_x1656_x855185166}

[[Output: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}]{#struct_0_19500_x1656_1767498969}

[[发送的报文数、字节数以及发送报文的错误数]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1598247315}

[[Output queue]{lang="EN-US"}]{#struct_0_19500_x1656_x1274787998}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1767957718}[的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[发送报文队列信息]{style="font-family:宋体"}

[[OAM cells received]{lang="EN-US"}]{#struct_0_19500_x1656_x2019851552}

[[收到的]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_886506598}[信元个数]{style="font-family:宋体"}

[[F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_1768023254}

[[收到的]{style="font-family:宋体"}[F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_x1418677855}[信元个数]{style="font-family:宋体"}

[[F5 AIS]{lang="EN-US"}]{#struct_0_19500_x1656_x1670488685}

[[收到的]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_19500_x1656_1768088790}[信元个数。如果不支持]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警状态，则只显示信元个数，不显示告警状态（即]{style="font-family:宋体"}[OAM AIS State]{lang="EN-US"}[字段）]{style="font-family:宋体"}

[[F5 RDI]{lang="EN-US"}]{#struct_0_19500_x1656_223719148}

[[收到的]{style="font-family:宋体"}[RDI]{lang="EN-US"}]{#struct_0_19500_x1656_x1591045210}[信元个数。如果不支持]{style="font-family:宋体"}[RDI]{lang="EN-US"}[告警状态，则只显示信元个数，不显示告警状态（即]{style="font-family:宋体"}[OAM RDI State]{lang="EN-US"}[字段）]{style="font-family:宋体"}

[[OAM cells sent]{lang="EN-US"}]{#struct_0_19500_x1656_1768154326}

[[发送的]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_x655350246}[信元个数]{style="font-family:宋体"}

[[F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_1474294339}

[[发送的]{style="font-family:宋体"}[F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_1768219862}[信元个数]{style="font-family:宋体"}

[[OAM cell drops]{lang="EN-US"}]{#struct_0_19500_x1656_x1028447278}

[[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_x930145747}[信元丢弃的个数]{style="font-family:宋体"}

[[OAM AIS State]{lang="EN-US"}]{#struct_0_19500_x1656_1768285398}

[[AIS]{lang="EN-US"}]{#struct_0_19500_x1656_2103614221}[告警状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No AIS Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_1768350934}[：无]{lang="EN-US" style="font-family:宋体"}[OAM AIS]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E2E AIS Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_x1069132821}[：端到端]{lang="EN-US" style="font-family:宋体"}[OAM AIS]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[如果支持告警状态，则只显示告警状态，不显示信元个数（即]{style="font-family:宋体"}[F5 AIS]{lang="EN-US"}]{#struct_0_19500_x1656_x1218527803}[字段）]{style="font-family:宋体"}

[[OAM RDI State]{lang="EN-US"}]{#struct_0_19500_x1656_1768416470}

[[RDI]{lang="EN-US"}]{#struct_0_19500_x1656_2088373992}[告警状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No RDI Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_1767433430}[：无]{lang="EN-US" style="font-family:宋体"}[OAM RDI]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E2E RDI Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_x1621708517}[：端到端]{lang="EN-US" style="font-family:宋体"}[OAM RDI]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[如果支持告警状态，则只显示告警状态，不显示信元个数（即]{style="font-family:宋体"}[F5 RDI]{lang="EN-US"}]{#struct_0_19500_x1656_1474707146}[字段）]{style="font-family:宋体"}

[[OAM CC State]{lang="EN-US"}]{#struct_0_19500_x1656_1767498966}

[[CC]{lang="EN-US"}]{#struct_0_19500_x1656_x1597526419}[告警状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No CC Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_1767957719}[：无]{lang="EN-US" style="font-family:宋体"}[OAM CC]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E2E CC Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_x2019917088}[：端到端]{lang="EN-US" style="font-family:宋体"}[OAM CC]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1932741536 .myid}
[]{#_Toc404785239}[]{#struct_0_19500_x1656_x1058704757}[]{#_Toc348095176}

**ATM \-- ATM配置命令 \-- display atm pvc-info**

------------------------------------------------------------------------

[**[display atm pvc-info]{lang="EN-US"}**]{#struct_0_19500_x1656_1637862568}[命令用来显示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x292750002}

[**[display atm pvc-info]{lang="EN-US"}**[ \[ **interface** *interface-type* { *interface-number* \| *interface-number.subnumber* } \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_19500_x1656_x868014520}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1768023255}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1418612319}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1217807614}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1348459262}

[[network-operator]{lang="EN-US"}]{#struct_0_19500_x1656_x1651221309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1302847867}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19500_x1656_1756307635}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x416287501}

[**[interface]{lang="EN-US"}**[ *interface-type* { *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_19500_x1656_x1505016170}[：显示指定接口的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[信息。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}**]{#struct_0_19500_x1656_2041045825}[：显示指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[*[pvc-name]{lang="EN-US"}*]{#struct_0_19500_x1656_1768088791}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名中不允许使用"]{style="font-family:宋体"}[/]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，如"]{style="font-family:宋体"}[1/20]{lang="EN-US"}["、"]{style="font-family:宋体"}[a-b]{lang="EN-US"}["就不允许作为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}

[*[vpi/vci]{lang="EN-US"}*]{#struct_0_19500_x1656_223784684}[：]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPI]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[为]{style="font-family:宋体"}[VCI]{lang="EN-US"}[值，取值范围与接口类型相关，请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?-1864992396#_Ref337389143)["。]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[与]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[不能同时为]{style="font-family:宋体"}[0]{lang="EN-US"}[。通常，]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[取值]{style="font-family:宋体"}[0]{lang="EN-US"}[到]{style="font-family:宋体"}[31]{lang="EN-US"}[保留用于特定用途，建议用户不要使用。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2019418528}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口，则显示所有接口的]{style="font-family:宋体"}]{#struct_0_19500_x1656_x378965368}[PVC]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口而不指定]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1777704785}[PVC]{lang="EN-US"}[，则显示指定接口的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口并且指定]{style="font-family:宋体"}]{#struct_0_19500_x1656_857342214}[PVC]{lang="EN-US"}[，则显示指定接口的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x706594979}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1529822285}[显示所有接口的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display atm pvc-info]{lang="EN-US"}]{#struct_0_19500_x1656_1768154327}

[VPI/VCI   State    PVC name    Encap    Protocol   Interface]{lang="EN-US"}

[1/32      UP       aa          SNAP     IP         ATM2/4/0]{lang="EN-US"}

[1/33      UP       Sysname     MUX      None       ATM2/4/0]{lang="EN-US"}

[1/55      UP       datacomm    SNAP     PPP        ATM2/4/0.1]{lang="EN-US"}

[2/66      UP       N/A         SNAP     IP         ATM2/4/0.4]{lang="EN-US"}

[2/101     UP       beijing     SNAP     ETH  []{#_Hlt23233413}      ATM2/4/0.2]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display atm pvc-info]{lang="EN-US"}]{#struct_0_19500_x1656_x655415782}[命令显示信息描述表]{style="font-family:黑体"}

[]{#_Toc328667711}[]{#table_struct_0_x1641643614}[[字段]{style="font-family:黑体"}]{#struct_0_19500_x1656_x868111479}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1819372201}

[[VPI/VCI]{lang="EN-US"}]{#struct_0_19500_x1656_146993162}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1446197442}[的]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值对]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_19500_x1656_1768219863}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1028512814}[的状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_x33948818}[：该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态、]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态和]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态均为]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_306218867}[：]{style="font-family:宋体"} [PVC]{lang="EN-US"}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态、]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态和]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态中至少其中一个为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[PVC name]{lang="EN-US"}]{#struct_0_19500_x1656_x1883658662}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1637441167}[名称，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示没有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Encap]{lang="EN-US"}]{#struct_0_19500_x1656_1768285399}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_2103679757}[的]{style="font-family:宋体"}[AAL5]{lang="EN-US"}[封装类型，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SNAP]{lang="EN-US"}]{#struct_0_19500_x1656_1414213923}[：表示]{lang="EN-US" style="font-family:宋体"}[LLC]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Logical Link Control]{lang="EN-US"}[，逻辑链接控制）]{lang="EN-US" style="font-family:
  宋体"}[/SNAP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Subnet Access Protocol]{lang="EN-US"}[，子网访问协议）封装类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NLPID]{lang="EN-US"}]{#struct_0_19500_x1656_x2075613292}[：表示]{lang="EN-US" style="font-family:宋体"}[RFC1490]{lang="EN-US"}[封装类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MUX]{lang="EN-US"}]{#struct_0_19500_x1656_906516626}[：表示]{style="font-family:宋体"}[MUX]{lang="EN-US"}[复用封装类型]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_19500_x1656_x513200807}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1768350935}[支持的上层协议的类型，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_19500_x1656_x1069198357}[：]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_x484617752}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ETH]{lang="EN-US"}]{#struct_0_19500_x1656_279683840}[：以太协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_19500_x1656_x418077205}[：未配置任何协议]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_19500_x1656_1768416471}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_2088308456}[所属的接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x344833499}[显示指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display atm pvc-info interface atm 2/4/1 pvc 1/100]{lang="EN-US"}]{#struct_0_19500_x1656_1767498967}

[ATM2/4/1, VPI: 1, VCI: 100]{lang="EN-US"}

[  Encapsulation: SNAP, Protocol: IP]{lang="EN-US"}

[  Service-type: UBR, Output-pcr: 200 kbps]{lang="EN-US"}

[  Transmit-Priority: 0]{lang="EN-US"}

[  OAM loopback interval: 0 sec(disabled), OAM loopback retry interval: 1 sec]{lang="EN-US"}

[  OAM loopback retry count (up/down): 3/5]{lang="EN-US"}

[  OAM AIS-RDI count (up/down): 3/1]{lang="EN-US"}

[  Interface State: UP, OAM State: UP, PVC State: UP]{lang="EN-US"}

[  Input: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}

[  Output: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}

[  Output queue: (Urgent queuing : Size/Length/Discards)  0/100/0]{lang="EN-US"}

[  Output queue: (Protocol queuing : Size/Length/Discards)  0/500/0]{lang="EN-US"}

[  Output queue: (FIFO queuing : Size/Length/Discards)  0/75/0]{lang="EN-US"}

[  OAM cells received: 42]{lang="EN-US"}

[    F5 Loopback: 0, F5 AIS: 42, F5 RDI: 0]{lang="EN-US"}

[  OAM cells sent: 0]{lang="EN-US"}

[    F5 Loopback: 0]{lang="EN-US"}

[  OAM cell drops: 0]{lang="EN-US"}

[  OAM AIS State: No AIS Alarm]{lang="EN-US"}

[  OAM RDI State: No RDI Alarm]{lang="EN-US"}

[  OAM CC State: No CC Alarm]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display atm pvc-info]{lang="EN-US"}]{#struct_0_19500_x1656_x1597591955}[命令指定]{style="font-family:黑体"}[PVC]{lang="EN-US"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1613960430}[[字段]{style="font-family:黑体"}]{#struct_0_19500_x1656_x960925633}

[[描述]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1489737553}

[[ATM2/4/1]{lang="EN-US"}]{#struct_0_19500_x1656_413874423}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1051906546}[所属的接口名]{style="font-family:宋体"}

[[VPI]{lang="EN-US"}]{#struct_0_19500_x1656_x1371187450}

[[虚路径标识符]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1968364560}

[[VCI]{lang="EN-US"}]{#struct_0_19500_x1656_x705554554}

[[虚通道标识符]{style="font-family:宋体"}]{#struct_0_19500_x1656_x960860097}

[[Encapsulation]{lang="EN-US"}]{#struct_0_19500_x1656_x1110629937}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1443159632}[的]{style="font-family:宋体"}[AAL5]{lang="EN-US"}[封装类型，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SNAP]{lang="EN-US"}]{#struct_0_19500_x1656_1700520253}[：表示]{lang="EN-US" style="font-family:宋体"}[LLC]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Logical Link Control]{lang="EN-US"}[，逻辑链接控制）]{lang="EN-US" style="font-family:
  宋体"}[/SNAP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Subnet Access Protocol]{lang="EN-US"}[，子网访问协议）封装类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NLPID]{lang="EN-US"}]{#struct_0_19500_x1656_x1570167999}[：表示]{lang="EN-US" style="font-family:宋体"}[RFC1490]{lang="EN-US"}[封装类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MUX]{lang="EN-US"}]{#struct_0_19500_x1656_x960794561}[：表示]{style="font-family:宋体"}[MUX]{lang="EN-US"}[复用封装类型]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_19500_x1656_x1482886191}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1629077319}[支持的上层协议的类型，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_19500_x1656_1341304777}[：]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_x1429769844}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ETH]{lang="EN-US"}]{#struct_0_19500_x1656_x1783865610}[：以太协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_19500_x1656_x960729025}[：未配置任何协议]{lang="EN-US" style="font-family:宋体"}

[[Service-type]{lang="EN-US"}]{#struct_0_19500_x1656_1270018348}

[[服务类型，可能的类型如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_1366331443}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBR]{lang="EN-US"}]{#struct_0_19500_x1656_x1753626490}[：恒定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UBR]{lang="EN-US"}]{#struct_0_19500_x1656_x960663489}[：非确定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-NRT]{lang="EN-US"}]{#struct_0_19500_x1656_2016509791}[：非实时可变速率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-RT]{lang="EN-US"}]{#struct_0_19500_x1656_x1620170501}[：实时可变速率]{style="font-family:宋体"}

[[Output-pcr]{lang="EN-US"}]{#struct_0_19500_x1656_844761508}

[[输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_594083668}[信元的峰值速率]{style="font-family:宋体"}

[[Transmit-Priority]{lang="EN-US"}]{#struct_0_19500_x1656_x960597953}

[[传输优先级]{style="font-family:宋体"}]{#struct_0_19500_x1656_1644253543}

[[OAM loopback interval]{lang="EN-US"}]{#struct_0_19500_x1656_x621752448}

[[发送]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_x67769676}[信元的间隔时间]{style="font-family:宋体"}

[[OAM loopback retry interval]{lang="EN-US"}]{#struct_0_19500_x1656_x960532417}

[[OAM F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_x702215588}[重传验证的间隔时间]{style="font-family:宋体"}

[[OAM loopback retry count (up/down)]{lang="EN-US"}]{#struct_0_19500_x1656_1411987390}

[[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_2006022306}[验证]{style="font-family:宋体"}[UP]{lang="EN-US"}[和]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[的信元数量]{style="font-family:宋体"}

[[OAM AIS-RDI count (up/down)]{lang="EN-US"}]{#struct_0_19500_x1656_x960466881}

[[OAM AIS-RDI]{lang="EN-US"}]{#struct_0_19500_x1656_848026862}[验证]{style="font-family:宋体"}[UP]{lang="EN-US"}[的秒数、]{style="font-family:宋体"}[OAM AIS-RDI]{lang="EN-US"}[验证]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[的信元数量]{style="font-family:宋体"}

[[Interface State]{lang="EN-US"}]{#struct_0_19500_x1656_221244519}

[[该]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1487841550}[所属的接口名及接口物理状态和管理状态]{style="font-family:宋体"}

[[如果不是子接口，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x961449921}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_x1824591607}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_x239568995}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）或者该接口已经通过]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[命令被关闭，即管理状态为关闭]{style="font-family:宋体"}

[[如果是子接口，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_2061141845}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_x961384385}[：该接口的管理状态和其父接口的物理状态和管理状态均为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_64156503}[：表示该接口或其父接口已经通过]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[命令被关闭或者其父接口物理状态关闭]{style="font-family:宋体"}

[[OAM State]{lang="EN-US"}]{#struct_0_19500_x1656_x289016707}

[[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_x960925632}[协议状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_x1489803089}[：协议状态开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_x1505320207}[：协议状态关闭]{style="font-family:宋体"}

[[PVC State]{lang="EN-US"}]{#struct_0_19500_x1656_449111232}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x960860096}[的状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_x1110695473}[：该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态、]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态和]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态均为]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_763722110}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的状态、]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态和]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态中至少其中一个为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}]{#struct_0_19500_x1656_x960794560}

[[接收的报文数、字节数以及接收报文的错误数]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1482820655}

[[Output: 0 packets, 0 bytes, 0 errors]{lang="EN-US"}]{#struct_0_19500_x1656_968516698}

[[发送的报文数、字节数以及发送报文的错误数]{style="font-family:宋体"}]{#struct_0_19500_x1656_x960729024}

[[Output queue]{lang="EN-US"}]{#struct_0_19500_x1656_1269952812}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x963363876}[的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[发送报文队列信息]{style="font-family:宋体"}

[[OAM cells received]{lang="EN-US"}]{#struct_0_19500_x1656_x1991541061}

[[收到的]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_x960663488}[信元个数]{style="font-family:宋体"}

[[F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_2016444255}

[[收到的]{style="font-family:宋体"}[F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_x34157679}[信元个数]{style="font-family:宋体"}

[[F5 AIS]{lang="EN-US"}]{#struct_0_19500_x1656_x960597952}

[[收到的]{style="font-family:宋体"}[AIS]{lang="EN-US"}]{#struct_0_19500_x1656_1644319079}[信元个数。如果不支持]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警状态，则只显示信元个数，不显示告警状态（即]{style="font-family:宋体"}[OAM AIS State]{lang="EN-US"}[字段）]{style="font-family:宋体"}

[[F5 RDI]{lang="EN-US"}]{#struct_0_19500_x1656_2080922988}

[[收到的]{style="font-family:宋体"}[RDI]{lang="EN-US"}]{#struct_0_19500_x1656_x960532416}[信元个数。如果不支持]{style="font-family:宋体"}[RDI]{lang="EN-US"}[告警状态，则只显示信元个数，不显示告警状态（即]{style="font-family:宋体"}[OAM RDI State]{lang="EN-US"}[字段）]{style="font-family:宋体"}

[[OAM cells sent]{lang="EN-US"}]{#struct_0_19500_x1656_x702150052}

[[发送的]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_x960466880}[信元个数]{style="font-family:宋体"}

[[F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_847961326}

[[发送的]{style="font-family:宋体"}[F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_626770671}[信元个数]{style="font-family:宋体"}

[[OAM cell drops]{lang="EN-US"}]{#struct_0_19500_x1656_x961449920}

[[OAM]{lang="EN-US"}]{#struct_0_19500_x1656_x1824657143}[信元丢弃的个数]{style="font-family:宋体"}

[[OAM AIS State]{lang="EN-US"}]{#struct_0_19500_x1656_x754117018}

[[AIS]{lang="EN-US"}]{#struct_0_19500_x1656_x961384384}[告警状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No AIS Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_64090967}[：无]{lang="EN-US" style="font-family:宋体"}[OAM AIS]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E2E AIS Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_x329778050}[：端到端]{lang="EN-US" style="font-family:宋体"}[OAM AIS]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[如果支持告警状态，则只显示告警状态，不显示信元个数（即]{style="font-family:宋体"}[F5 AIS]{lang="EN-US"}]{#struct_0_19500_x1656_x960925635}[字段）]{style="font-family:宋体"}

[[OAM RDI State]{lang="EN-US"}]{#struct_0_19500_x1656_x1490130769}

[[RDI]{lang="EN-US"}]{#struct_0_19500_x1656_x960860099}[告警状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No RDI Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_x1110498865}[：无]{lang="EN-US" style="font-family:宋体"}[OAM RDI]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E2E RDI Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_1966783960}[：端到端]{lang="EN-US" style="font-family:宋体"}[OAM RDI]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[如果支持告警状态，则只显示告警状态，不显示信元个数（即]{style="font-family:宋体"}[F5 RDI]{lang="EN-US"}]{#struct_0_19500_x1656_x960794563}[字段）]{style="font-family:宋体"}

[[OAM CC State]{lang="EN-US"}]{#struct_0_19500_x1656_x1482755119}

[[CC]{lang="EN-US"}]{#struct_0_19500_x1656_x377887842}[告警状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No CC Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_x960729027}[：无]{lang="EN-US" style="font-family:宋体"}[OAM CC]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E2E CC Alarm]{lang="EN-US"}]{#struct_0_19500_x1656_1270149420}[：端到端]{lang="EN-US" style="font-family:宋体"}[OAM CC]{lang="EN-US"}[告警]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1246997622 .myid}
[]{#_Toc404785240}[]{#struct_0_19500_x1656_205331315}[]{#_Toc350872245}[]{#_Toc345946916}

**ATM \-- ATM配置命令 \-- display interface virtual-ethernet**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[virtual-ethernet]{lang="EN-US"}**]{#struct_0_19500_x1656_x690701801}[命令用来显示]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1373785684}

[**[display interface]{lang="EN-US"}**[ \[ **virtual-ethernet** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_19500_x1656_2015985502}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_83383596}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_x2054998427}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x575254136}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_725472327}

[[network-operator]{lang="EN-US"}]{#struct_0_19500_x1656_608808176}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1279668602}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19500_x1656_x960597955}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1644384615}

[*[interface-number]{lang="EN-US"}*]{#struct_0_19500_x1656_1325035915}[：显示指定]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_19500_x1656_958518798}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_19500_x1656_x1831782800}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_19500_x1656_x2071812160}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x275587880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19500_x1656_301222255}**[virtual-ethernet]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[virtual-ethernet]{lang="EN-US"}**]{#struct_0_19500_x1656_1430000422}[参数，不指定]{lang="EN-US" style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[VE]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x960532419}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x701822372}[显示]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-ethernet 2/4/1]{lang="EN-US"}]{#struct_0_19500_x1656_771950766}

[Virtual-Ethernet2/4/1]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Virtual-Ethernet2/4/1 Interface]{lang="EN-US"}

[Bandwidth: 20000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 00e0-fc0d-9485]{lang="EN-US"}

[IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 00e0-fc0d-9485]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_354377648}[显示]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/1]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-ethernet 2/4/1 brief]{lang="EN-US"}]{#struct_0_19500_x1656_x960466883}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[VE1                  DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_848157934}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface virtual-ethernet brief down]{lang="EN-US"}]{#struct_0_19500_x1656_x1367973771}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[VE2/4/1              DOWN Not connected]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display interface virtual-ethernet]{lang="EN-US"}]{#struct_0_19500_x1656_x570118645}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1622471579}[[字段]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2093654753}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19500_x1656_x961449923}

[[Current state]{lang="EN-US"}]{#struct_0_19500_x1656_x1824722679}

[[该接口的物理状态，状态可能为：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x551160872}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_x1033637374}[：表示该接口已经通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_495905422}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_714030496}[：该端口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_19500_x1656_x961384387}

[[该接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_19500_x1656_64025431}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_x1078747480}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_x741788774}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_19500_x1656_983152201}

[[该接口的描述信息]{style="font-family:宋体"}]{#struct_0_19500_x1656_x960925634}

[[Bandwidth]{lang="EN-US"}]{#struct_0_19500_x1656_x1490196305}

[[该接口的期望带宽]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1554457258}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_19500_x1656_510057704}

[[该接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1168150240}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_19500_x1656_1294686976}

[[该接口网络层协议处理状况]{style="font-family:宋体"}]{#struct_0_19500_x1656_x960860098}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_19500_x1656_x1110564401}

[[该接口]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_19500_x1656_x1525339433}[报文帧格式，取值为]{style="font-family:宋体"}[PKTFMT_ETHNT_2]{lang="EN-US"}[表示报文以]{style="font-family:宋体"}[Ethernet II]{lang="EN-US"}[型帧格式封装]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_19500_x1656_x1190038147}

[[该接口]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19500_x1656_x960794562}[报文帧格式]{style="font-family:宋体"}

[[Hardware Address]{lang="EN-US"}]{#struct_0_19500_x1656_x1482689583}

[[该接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19500_x1656_1832200683}[地址]{style="font-family:宋体"}

[[Last clearing of counters: Never]{lang="EN-US"}]{#struct_0_19500_x1656_856888661}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_19500_x1656_1834691069}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_19500_x1656_x960729026}

[[该接口在最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_19500_x1656_1270083884}[秒接收报文的平均速率]{style="font-family:宋体"}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_19500_x1656_951298458}

[[该接口在最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_19500_x1656_115209849}[秒发送报文的平均速率]{style="font-family:宋体"}

[[Input]{lang="EN-US"}]{#struct_0_19500_x1656_x960663490}

[[输入报文统计信息：]{style="font-family:宋体"}]{#struct_0_19500_x1656_2015919966}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_19500_x1656_130230162}[：]{style="font-family:宋体"}[数据包的个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes]{lang="EN-US"}]{#struct_0_19500_x1656_1713215658}[：总字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[drops]{lang="EN-US"}]{#struct_0_19500_x1656_x960597954}[：丢弃的报文个数]{style="font-family:宋体"}

[[Output]{lang="EN-US"}]{#struct_0_19500_x1656_1644450151}

[[输出报文统计信息：]{style="font-family:宋体"}]{#struct_0_19500_x1656_1342587726}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_19500_x1656_x14943190}[：]{style="font-family:宋体"}[数据包的个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes]{lang="EN-US"}]{#struct_0_19500_x1656_x960532418}[：总字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[drops]{lang="EN-US"}]{#struct_0_19500_x1656_x701756836}[：丢弃的报文个数]{style="font-family:宋体"}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_19500_x1656_x779298121}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1225040638}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_19500_x1656_x960466882}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_19500_x1656_848092398}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_19500_x1656_x203743873}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_19500_x1656_x961449922}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_19500_x1656_x1824788215}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_19500_x1656_x334260642}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_19500_x1656_x961384386}

[[Link]{lang="EN-US"}]{#struct_0_19500_x1656_63959895}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x440455521}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_588362623}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_19500_x1656_x960925637}[：表示]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_19500_x1656_x623475544}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_19500_x1656_x1489999697}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x14355102}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_19500_x1656_1227629000}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_19500_x1656_x1508255785}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_19500_x1656_1448115437}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_19500_x1656_x588690159}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_x960794565}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_19500_x1656_x1482624047}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_19500_x1656_354188074}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_19500_x1656_x960729029}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_19500_x1656_1270804780}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-900899430 .myid}
[]{#_Toc404785241}[]{#struct_0_19500_x1656_x1008925069}[]{#_Toc348095177}[]{#_Ref337902442}[]{#_Toc328667714}

**ATM \-- ATM配置命令 \-- encapsulation**

------------------------------------------------------------------------

[**[encapsulation]{lang="EN-US"}**]{#struct_0_19500_x1656_x2092908706}[命令用来配置]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的]{style="font-family:宋体"}[ATM AAL5]{lang="EN-US"}[封装类型。]{style="font-family:宋体"}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_19500_x1656_832484532}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1720381598}

[**[encapsulation]{lang="EN-US"}**[ { **aal5mux** *\|* **aal5nlpid** *\|* **aal5snap** }]{lang="EN-US"}]{#struct_0_19500_x1656_x960663493}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_19500_x1656_2016116574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1530716530}

[[ATM AAL5]{lang="EN-US"}]{#struct_0_19500_x1656_385756032}[封装类型为]{style="font-family:宋体"}**[aal5snap]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x454157066}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1471888957}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x903706663}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1957897543}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_694990691}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1361406805}

[**[aal5mux]{lang="EN-US"}**]{#struct_0_19500_x1656_x960597957}[：]{style="font-family:宋体"}[MUX]{lang="EN-US"}[复用封装类型。]{style="font-family:宋体"}

[**[aal5nlpid]{lang="EN-US"}**]{#struct_0_19500_x1656_1644515687}[：]{style="font-family:宋体"}[RFC1490]{lang="EN-US"}[封装类型。]{style="font-family:宋体"}

[**[aal5snap]{lang="EN-US"}**]{#struct_0_19500_x1656_x219486871}[：]{style="font-family:宋体"}[LLC]{lang="EN-US"}[（]{style="font-family:宋体"}[Logical Link Control]{lang="EN-US"}[，逻辑链接控制）]{style="font-family:宋体"}[/SNAP]{lang="EN-US"}[（]{style="font-family:宋体"}[Subnet Access Protocol]{lang="EN-US"}[，子网访问协议）封装类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1181006808}

[[不同的]{style="font-family:宋体"}[ATM AAL5]{lang="EN-US"}]{#struct_0_19500_x1656_x2079039320}[封装类型支持的映射类型如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aal5snap]{lang="EN-US"}**]{#struct_0_19500_x1656_1016738391}[封装支持]{lang="EN-US" style="font-family:宋体"}[IPoA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[P]{lang="EN-US"}[oEoA]{lang="EN-US"}[、]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[PPPoEoA]{lang="EN-US"}[映射。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aal5mux]{lang="EN-US"}**]{#struct_0_19500_x1656_337815957}[封装支持]{lang="EN-US" style="font-family:宋体"}[IPoA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[P]{lang="EN-US"}[oEoA]{lang="EN-US"}[、]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[PPPoEoA]{lang="EN-US"}[映射，但不支持同时承载多种协议。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aal5nlpid]{lang="EN-US"}**]{#struct_0_19500_x1656_x547351814}[封装只支持]{lang="EN-US" style="font-family:宋体"}[IPoA]{lang="EN-US"}[映射。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x960532421}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[相互通信的两端设备上配置的]{style="font-family:宋体"}]{#struct_0_19500_x1656_x702346663}[ATM AAL5]{lang="EN-US"}[封装类型要保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有]{lang="EN-US" style="font-family:宋体"}**[aal5snap]{lang="EN-US"}**]{#struct_0_19500_x1656_x143664560}[封装支持]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[协议，当采用]{lang="EN-US" style="font-family:宋体"}**[aal5mux]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[aal5nlpid]{lang="EN-US"}**[封装时不能配置]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[]{#struct_0_19500_x1656_122961702}[]{#_Hlt23234097}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}[PVC/PVC-group]{lang="EN-US"}[支持同时承载多种协议，但某些类型的封装可能并不支持部分应用方式（即]{style="font-family:
宋体"}[IPoA]{lang="EN-US"}[、]{style="font-family:宋体"}[IPoEoA]{lang="EN-US"}[、]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[、]{style="font-family:宋体"}[PPPoEoA]{lang="EN-US"}[中的一种或几种）。当出现不能支持的情况时，系统会给出错误提示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1514946815}[PVC/PVC-group]{lang="EN-US"}[切换封装时，如果已经配置了与切换后封装类型冲突的映射，切换封装后的]{style="font-family:宋体"}[PVC/PVC-group]{lang="EN-US"}[将会删除所有冲突的映射对应的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不能在]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x439073051}[下的]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[下配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_812406341}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x148067525}[指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC 1/32]{lang="EN-US"}[的]{style="font-family:宋体"}[AAL5]{lang="EN-US"}[封装类型为]{style="font-family:宋体"}**[aal5snap]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x960466885}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc 1/32]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-1/32\] encapsulation aal5snap]{lang="EN-US"}
:::

::: {#-1023592256 .myid}
[]{#_Toc404785242}[]{#struct_0_19500_x1656_848289006}

**ATM \-- ATM配置命令 \-- interface virtual-ethernet**

------------------------------------------------------------------------

[**[interface virtual-ethernet]{lang="EN-US"}**]{#struct_0_19500_x1656_1972802053}[命令用来创建]{style="font-family:
宋体"}[VE]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Ethernet]{lang="EN-US"}[，三层虚拟以太网）接口或子接口，并进入]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口或子接口视图。如果该]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口或子接口已经存在，则直接进入]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口或子接口视图。]{style="font-family:宋体"}

[**[undo interface virtual-ethernet]{lang="EN-US"}**]{#struct_0_19500_x1656_1627725112}[命令用来删除]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口或子接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1599810132}

[**[interface virtual-ethernet]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_19500_x1656_1487654139}

[**[undo interface virtual-ethernet]{lang="EN-US"}**[ { *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_19500_x1656_x991213159}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1845442643}

[[不存在]{style="font-family:宋体"}[VE]{lang="EN-US"}]{#struct_0_19500_x1656_x519430587}[接口和子接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x961449925}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1824853751}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x139788382}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_834307990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1194690862}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1825369865}

[*[interface-number]{lang="EN-US"}*]{#struct_0_19500_x1656_x1763160716}[：]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口编号。]{style="font-family:宋体"}

[*[interface-number.subnumber]{lang="EN-US"}*]{#struct_0_19500_x1656_1278221001}[：]{style="font-family:
宋体"}[VE]{lang="EN-US"}[子接口编号，其中]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1554399058}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_x961384389}[接口的波特率为]{style="font-family:宋体"}[10000000bit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_63370071}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x284973400}[创建]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口并进入]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_431018164}

[\[Sysname\] interface virtual-ethernet 2/4/1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet2/4/1\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_804616994}[创建]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口并进入]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x723421451}

[\[Sysname\] interface virtual-ethernet 2/4/1.1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet2/4/1.1\]]{lang="EN-US"}
:::

::: {#-636046328 .myid}
[]{#_Toc348095179}[]{#_Toc328667720}[]{#_Toc404785243}[]{#struct_0_19500_x1656_x1219660297}[]{#_Toc348877553}[]{#_Hlt24951205}[]{#_Toc337389348}[]{#_Toc337476133}[]{#_Toc337480910}[]{#_Toc337540984}[]{#_Toc337555768}[]{#_Toc337389349}[]{#_Toc337476134}[]{#_Toc337480911}[]{#_Toc337540985}[]{#_Toc337555769}[]{#_Toc337389350}[]{#_Toc337476135}[]{#_Toc337480912}[]{#_Toc337540986}[]{#_Toc337555770}[]{#_Toc337389351}[]{#_Toc337476136}[]{#_Toc337480913}[]{#_Toc337540987}[]{#_Toc337555771}[]{#_Toc337389352}[]{#_Toc337476137}[]{#_Toc337480914}[]{#_Toc337540988}[]{#_Toc337555772}[]{#_Toc337389353}[]{#_Toc337476138}[]{#_Toc337480915}[]{#_Toc337540989}[]{#_Toc337555773}[]{#_Toc337389354}[]{#_Toc337476139}[]{#_Toc337480916}[]{#_Toc337540990}[]{#_Toc337555774}[]{#_Toc337389355}[]{#_Toc337476140}[]{#_Toc337480917}[]{#_Toc337540991}[]{#_Toc337555775}[]{#_Toc337389356}[]{#_Toc337476141}[]{#_Toc337480918}[]{#_Toc337540992}[]{#_Toc337555776}[]{#_Toc337389357}[]{#_Toc337476142}[]{#_Toc337480919}[]{#_Toc337540993}[]{#_Toc337555777}[]{#_Toc337389358}[]{#_Toc337476143}[]{#_Toc337480920}[]{#_Toc337540994}[]{#_Toc337555778}[]{#_Toc337389359}[]{#_Toc337476144}[]{#_Toc337480921}[]{#_Toc337540995}[]{#_Toc337555779}[]{#_Toc337389360}[]{#_Toc337476145}[]{#_Toc337480922}[]{#_Toc337540996}[]{#_Toc337555780}[]{#_Toc337389361}[]{#_Toc337476146}[]{#_Toc337480923}[]{#_Toc337540997}[]{#_Toc337555781}[]{#_Toc337389362}[]{#_Toc337476147}[]{#_Toc337480924}[]{#_Toc337540998}[]{#_Toc337555782}[]{#_Toc337389363}[]{#_Toc337476148}[]{#_Toc337480925}[]{#_Toc337540999}[]{#_Toc337555783}[]{#_Toc337389364}[]{#_Toc337476149}[]{#_Toc337480926}[]{#_Toc337541000}[]{#_Toc337555784}[]{#_Toc337389365}[]{#_Toc337476150}[]{#_Toc337480927}[]{#_Toc337541001}[]{#_Toc337555785}[]{#_Toc337389366}[]{#_Toc337476151}[]{#_Toc337480928}[]{#_Toc337541002}[]{#_Toc337555786}[]{#_Toc337389367}[]{#_Toc337476152}[]{#_Toc337480929}[]{#_Toc337541003}[]{#_Toc337555787}[]{#_Toc337389368}[]{#_Toc337476153}[]{#_Toc337480930}[]{#_Toc337541004}[]{#_Toc337555788}[]{#_Toc337389369}[]{#_Toc337476154}[]{#_Toc337480931}[]{#_Toc337541005}[]{#_Toc337555789}[]{#_Toc337389370}[]{#_Toc337476155}[]{#_Toc337480932}[]{#_Toc337541006}[]{#_Toc337555790}[]{#_Toc337389371}[]{#_Toc337476156}[]{#_Toc337480933}[]{#_Toc337541007}[]{#_Toc337555791}[]{#_Toc337389372}[]{#_Toc337476157}[]{#_Toc337480934}[]{#_Toc337541008}[]{#_Toc337555792}[]{#_Toc337389373}[]{#_Toc337476158}[]{#_Toc337480935}[]{#_Toc337541009}[]{#_Toc337555793}[]{#_Toc337389374}[]{#_Toc337476159}[]{#_Toc337480936}[]{#_Toc337541010}[]{#_Toc337555794}[]{#_Toc337389375}[]{#_Toc337476160}[]{#_Toc337480937}[]{#_Toc337541011}[]{#_Toc337555795}[]{#_Toc337389376}[]{#_Toc337476161}[]{#_Toc337480938}[]{#_Toc337541012}[]{#_Toc337555796}[]{#_Toc337389377}[]{#_Toc337476162}[]{#_Toc337480939}[]{#_Toc337541013}[]{#_Toc337555797}[]{#_Toc337389378}[]{#_Toc337476163}[]{#_Toc337480940}[]{#_Toc337541014}[]{#_Toc337555798}[]{#_Toc337389379}[]{#_Toc337476164}[]{#_Toc337480941}[]{#_Toc337541015}[]{#_Toc337555799}[]{#_Toc337389380}[]{#_Toc337476165}[]{#_Toc337480942}[]{#_Toc337541016}[]{#_Toc337555800}[]{#_Toc337389381}[]{#_Toc337476166}[]{#_Toc337480943}[]{#_Toc337541017}[]{#_Toc337555801}[]{#_Toc337389382}[]{#_Toc337476167}[]{#_Toc337480944}[]{#_Toc337541018}[]{#_Toc337555802}[]{#_Toc337389383}[]{#_Toc337476168}[]{#_Toc337480945}[]{#_Toc337541019}[]{#_Toc337555803}[]{#_Toc337389384}[]{#_Toc337476169}[]{#_Toc337480946}[]{#_Toc337541020}[]{#_Toc337555804}[]{#_Toc337389385}[]{#_Toc337476170}[]{#_Toc337480947}[]{#_Toc337541021}[]{#_Toc337555805}[]{#_Toc337389386}[]{#_Toc337476171}[]{#_Toc337480948}[]{#_Toc337541022}[]{#_Toc337555806}[]{#_Toc337389387}[]{#_Toc337476172}[]{#_Toc337480949}[]{#_Toc337541023}[]{#_Toc337555807}[]{#_Toc337389388}[]{#_Toc337476173}[]{#_Toc337480950}[]{#_Toc337541024}[]{#_Toc337555808}

**ATM \-- ATM配置命令 \-- mac-address**

------------------------------------------------------------------------

[**[mac-address]{lang="EN-US"}**]{#struct_0_19500_x1656_x960925636}[命令用来配置]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo mac-address]{lang="EN-US"}**]{#struct_0_19500_x1656_x1490065233}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x810209942}

[**[mac-address]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_19500_x1656_x309525964}

[**[undo mac-address]{lang="EN-US"}**]{#struct_0_19500_x1656_1233074252}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1328921934}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_1105893585}[接口在创建时会使用设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为自己的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_532983375}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_x2128773312}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x960860100}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1227563464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x555708152}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x964388986}

[*[mac-address]{lang="EN-US"}*]{#struct_0_19500_x1656_x100697069}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，形式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1181724809}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_x1700286432}[接口在创建时会使用设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为自己的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，这样，所有的]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口都共用一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。如果同一设备的多个]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口通过不同的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[连接到同一个]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器，而]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器上采用静态绑定方式给]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口进行]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分配，则需要使用]{style="font-family:宋体"}**[mac-address]{lang="EN-US"}**[命令为不同的]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口配置不同的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_619674566}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_343250928}[配置]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0001-0001-0001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x960794564}

[\[Sysname\] interface virtual-ethernet 2/4/1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet2/4/1\] mac-address 1-1-1]{lang="EN-US"}
:::

::: {#-406764260 .myid}
[]{#_Toc404785244}[]{#struct_0_19500_x1656_x1482558511}

**ATM \-- ATM配置命令 \-- map bridge**

------------------------------------------------------------------------

[**[map bridge]{lang="EN-US"}**]{#struct_0_19500_x1656_2083733186}[命令用来为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[创建]{style="font-family:宋体"}[IPoEoA]{lang="EN-US"}[映射、]{style="font-family:宋体"}[PPPoEoA]{lang="EN-US"}[映射。]{style="font-family:宋体"}

[**[undo map bridge]{lang="EN-US"}**]{#struct_0_19500_x1656_x2013202897}[命令用来删除该映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x72269719}

[**[map bridge virtual-ethernet]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_19500_x1656_x1576235769}

[**[undo map bridge]{lang="EN-US"}**]{#struct_0_19500_x1656_x452061174}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x209486585}

[[没有配置任何映射。]{style="font-family:宋体"}]{#struct_0_19500_x1656_x960729028}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1270739244}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_598350647}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_981880844}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x2044868463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1354846396}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1146656658}

[**[virtual-ethernet]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_19500_x1656_1992048971}[：]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口编号。该接口必须已经创建。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x960663492}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aal5snap]{lang="EN-US"}**]{#struct_0_19500_x1656_2016051038}[和]{lang="EN-US" style="font-family:宋体"}**[aal5mux]{lang="EN-US"}**[封装支持]{lang="EN-US" style="font-family:宋体"}[IPoEoA]{lang="EN-US"}[映射、]{lang="EN-US" style="font-family:宋体"}[PPPoEoA]{lang="EN-US"}[映射。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1178237940}[VE]{lang="EN-US"}[接口上最多允许创建]{style="font-family:宋体"}[512]{lang="EN-US"}[条映射。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1103484125}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[只能映射到一个]{lang="EN-US" style="font-family:宋体"}[VE]{lang="EN-US"}[接口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本板]{lang="EN-US" style="font-family:宋体"}[VE]{lang="EN-US"}]{#struct_0_19500_x1656_x499152683}[接口只能绑定到本板]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[，使用前可以看]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的接口编号中对应的板号和]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[所在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口对应板号是否一致]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不能在]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x620610460}[下的]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[下配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_19500_x1656_x2022702693}[IPoEoA]{lang="EN-US"}[、]{style="font-family:宋体"}[PPPoEoA]{lang="EN-US"}[应用时，必须指定一个]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口与之对应。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1907813754}

[[下面这个例子展示了一个完整的]{style="font-family:宋体"}[IPoEoA]{lang="EN-US"}]{#struct_0_19500_x1656_1742415057}[配置过程。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x960597956}[创建]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_1644581223}

[\[Sysname\] interface virtual-ethernet 2/4/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1320269775}[为该]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[10.1.1.1/16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-Virtual-Ethernet2/4/1\] ip address 10.1.1.1 255.255.0.0]{lang="EN-US"}]{#struct_0_19500_x1656_x1193849450}

[\[Sysname-Virtual-Ethernet2/4/1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1580910269}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[下创建]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/102]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}]{#struct_0_19500_x1656_1125283408}

[\[Sysname-ATM2/4/0\] pvc 1/102]{lang="EN-US"}[]{#_Hlt16595042}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_626627059}[在]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图下使用已经创建的]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口来创建]{style="font-family:宋体"}[IPoEoA]{lang="EN-US"}[映射。]{style="font-family:宋体"}

[[\[Sysname-ATM2/4/0-pvc-1/102\] map bridge virtual-ethernet 2/4/1]{lang="EN-US"}]{#struct_0_19500_x1656_x1928776178}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x960532420}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[encapsulation]{lang="EN-US"}**]{#struct_0_19500_x1656_x702281127}
:::

::: {#1511778876 .myid}
[]{#_Toc404785245}[]{#struct_0_19500_x1656_x125868712}[]{#_Toc348095180}[]{#_Toc348114933}

**ATM \-- ATM配置命令 \-- map ip**

------------------------------------------------------------------------

[**[map ip]{lang="EN-US"}**]{#struct_0_19500_x1656_x557603149}[命令用来为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[创建]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[映射，使]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[承载]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文。]{style="font-family:宋体"}

[**[undo map ip]{lang="EN-US"}**]{#struct_0_19500_x1656_x648833795}[命令用来删除该映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1671520961}

[**[map ip]{lang="EN-US"}**[ { *ip-address* \| **default** \| **inarp** \[ *minutes* \] }]{lang="EN-US"}]{#struct_0_19500_x1656_x853163177}

[**[undo map ip]{lang="EN-US"}**[ \[ *ip-address* \| **default** \| **inarp** \]]{lang="EN-US"}]{#struct_0_19500_x1656_x205351888}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1820747172}

[[没有配置任何映射。]{style="font-family:宋体"}]{#struct_0_19500_x1656_x960466884}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_848223470}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1972724649}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1881798890}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1657029101}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_120177669}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_870976696}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19500_x1656_1339369119}[：映射到]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的对端接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_19500_x1656_1896629628}[：配置一个具有缺省路由属性的映射。若某个报文在接口上找不到下一跳地址和]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[相同的映射，但某条]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[配置了]{style="font-family:宋体"}[default]{lang="EN-US"}[映射，则报文将从该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[上发送。]{style="font-family:宋体"}

[**[inarp]{lang="EN-US"}**]{#struct_0_19500_x1656_x961449924}[：使能反向地址解析]{style="font-family:宋体"}[InARP]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[minutes]{lang="EN-US"}*]{#struct_0_19500_x1656_x1824919287}[：发送]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文的间隔时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为分钟，缺省值为]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x305875087}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所有的封装类型都支持]{style="font-family:宋体"}]{#struct_0_19500_x1656_1179400437}[IPoA]{lang="EN-US"}[映射。]{style="font-family:宋体"}[但只有]{lang="EN-US" style="font-family:宋体"}**[aal5snap]{lang="EN-US"}**[封装支持配置]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[映射]{style="font-family:宋体"}[，当采用]{lang="EN-US" style="font-family:宋体"}**[aal5mux]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[aal5nlpid]{lang="EN-US"}**[封装时不能配置]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[映射]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[相同]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1122710660}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[下可以映射多个]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，且]{lang="EN-US" style="font-family:宋体"}[静态]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址映射、]{lang="EN-US" style="font-family:宋体"}[default]{lang="EN-US"}[映射和]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[映射三者可以同时配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[相同接口下不同的]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1158466683}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[不能映射到同一个]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个接口下的]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_365142236}[和]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[最多只能配置一个]{lang="EN-US" style="font-family:宋体"}[default]{lang="EN-US"}[映射。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_19500_x1656_1726690270}[命令时，如果不指定任何参数，则删除该]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[下所有的]{lang="EN-US" style="font-family:宋体"}[静态]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址映射、]{lang="EN-US" style="font-family:宋体"}[default]{lang="EN-US"}[映射和]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[映射。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不能在]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x269143144}[下的]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[下配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x961384388}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_63304535}[在]{style="font-family:宋体"}[PVC 1/32]{lang="EN-US"}[上创建一个静态]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址映射，指定对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[61.123.30.169]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_71137552}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc 1/32]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-1/32\] map ip 61.123.30.169]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_615535214}[在]{style="font-family:宋体"}[PVC 1/33]{lang="EN-US"}[上使能]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射，每]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟发送一次]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_2083200439}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc 1/33]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-1/33\] map ip inarp 10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x470324562}[在]{style="font-family:宋体"}[PVC 1/33]{lang="EN-US"}[上删除所有类型的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_605158308}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc 1/33]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-1/33\] undo map ip]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1360701678}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[encapsulation]{lang="EN-US"}**]{#struct_0_19500_x1656_x163592179}
:::

::: {#-1693452895 .myid}
[]{#_Toc404785246}[]{#struct_0_19500_x1656_x1749480866}[]{#_Toc348095181}[]{#_Toc328667722}

**ATM \-- ATM配置命令 \-- map ppp**

------------------------------------------------------------------------

[**[map ppp]{lang="EN-US"}**]{#struct_0_19500_x1656_x2029213009}[命令用来为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[创建]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[映射。]{style="font-family:宋体"}

[**[undo map ppp]{lang="EN-US"}**]{#struct_0_19500_x1656_1034348326}[命令用来删除该映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x979715560}

[**[map ppp virtual-template]{lang="EN-US"}**[ *vt-number*]{lang="EN-US"}]{#struct_0_19500_x1656_x1121951631}

[**[undo map ppp]{lang="EN-US"}**]{#struct_0_19500_x1656_605223844}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_47885350}

[[没有配置任何映射。]{style="font-family:宋体"}]{#struct_0_19500_x1656_x547246564}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1989104899}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x254522952}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_237373753}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x213291153}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_875584859}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x354098064}

[*[vt-number]{lang="EN-US"}*]{#struct_0_19500_x1656_605289380}[：]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[对应的虚拟模板接口编号。该虚拟模板接口必须已经创建。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x682710333}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aal5snap]{lang="EN-US"}**]{#struct_0_19500_x1656_272254217}[和]{lang="EN-US" style="font-family:宋体"}**[aal5mux]{lang="EN-US"}**[封装支持]{lang="EN-US" style="font-family:宋体"}[PPPoA]{lang="EN-US"}[映射。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_19500_x1656_x2003300166}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[只能映射到一个虚拟模板接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不能在]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x1474579203}[下的]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[下配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1520458736}

[[下面这个例子展示了一个完整的]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}]{#struct_0_19500_x1656_1948571990}[配置过程。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1416251433}[创建虚拟模板接口]{style="font-family:宋体"}[10]{lang="EN-US"}[并为该接口配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_605354916}

[\[Sysname\] interface virtual-template 10]{lang="EN-US"}

[\[Sysname-Virtual-Template10\] ip address 202.38.160.1 255.255.255.0[]{#_Hlt23220430}]{lang="EN-US"}

[\[Sysname-Virtual-Template10\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_817510142}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[下创建]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}]{#struct_0_19500_x1656_x946021866}

[\[Sysname-ATM2/4/0\] pvc 1/101]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1182631171}[使用已经创建的虚拟模板接口来创建]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[映射。]{style="font-family:宋体"}

[[\[Sysname-ATM2/4/0-pvc-1/101\] map ppp virtual-template 10]{lang="EN-US"}]{#struct_0_19500_x1656_x1457722428}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1137867755}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[encapsulation]{lang="EN-US"}**]{#struct_0_19500_x1656_x1232619963}
:::

::: {#988247972 .myid}
[]{#_Toc348095182}[]{#_Toc328667724}[]{#_Toc404785247}[]{#struct_0_19500_x1656_x1547028182}[]{#_Toc354243982}

**ATM \-- ATM配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_19500_x1656_605420452}[命令用来配置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_19500_x1656_1503999196}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_735853628}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_19500_x1656_1657360206}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_19500_x1656_983770419}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2102108065}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_19500_x1656_1239632059}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x611451382}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_730553865}[接口视图]{style="font-family:宋体"}[/VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605485988}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1112750281}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1183777980}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1431186214}

[*[size]{lang="EN-US"}*]{#struct_0_19500_x1656_x583432226}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1017732021}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_19500_x1656_1176771472}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_19500_x1656_x1469923310}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1491673352}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_605551524}[配置接口]{style="font-family:宋体"}[VE2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[200]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_1135263676}

[\[Sysname\] interface virtual-ethernet 2/4/0]{lang="EN-US"}

[\[Sysname- Virtual-Ethernet2/4/0\] mtu 200]{lang="EN-US"}
:::

::: {#-593357428 .myid}
[]{#_Toc404785248}[]{#struct_0_19500_x1656_1162971641}

**ATM \-- ATM配置命令 \-- oam ais-rdi**

------------------------------------------------------------------------

[**[oam ais-rdi]{lang="EN-US"}**]{#struct_0_19500_x1656_1001375556}[命令用来修改]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[（]{style="font-family:宋体"}[Alarm Indication Signal/Remote Defect Indication]{lang="EN-US"}[，告警指示信号]{style="font-family:宋体"}[/]{lang="EN-US"}[远程故障指示）告警信元检测的相关参数。]{style="font-family:宋体"}

[**[undo oam ais-rdi]{lang="EN-US"}**]{#struct_0_19500_x1656_x2120652015}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1764836044}

[**[oam ais-rdi]{lang="EN-US"}**[ **up** *up-seconds* **down** *down-seconds*]{lang="EN-US"}]{#struct_0_19500_x1656_1983123049}

[**[undo oam ais-rdi]{lang="EN-US"}**]{#struct_0_19500_x1656_622265020}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605617060}

[[参数]{style="font-family:宋体"}*[up-seconds]{lang="EN-US"}*]{#struct_0_19500_x1656_2130249515}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒，参数]{style="font-family:
宋体"}*[down-seconds]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。即当系统连续]{style="font-family:
宋体"}[1]{lang="EN-US"}[秒收到]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元后，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[，当连续]{style="font-family:宋体"}[3]{lang="EN-US"}[秒没有收到]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元后，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x541116266}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_361059622}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1092478523}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_488223571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1193847225}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2097492926}

[**[up]{lang="EN-US"}***[ up-seconds]{lang="EN-US"}*]{#struct_0_19500_x1656_900420016}[：连续]{style="font-family:宋体"}*[up-seconds]{lang="EN-US"}*[秒没有收到]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[。]{style="font-family:宋体"}*[up-seconds]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}***[ down-seconds]{lang="EN-US"}*]{#struct_0_19500_x1656_604634020}[：连续]{style="font-family:宋体"}*[down-seconds]{lang="EN-US"}*[秒收到]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元后，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[。]{style="font-family:宋体"}*[down-seconds]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_63776174}

[[系统使用一个超时时间为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19500_x1656_1080519526}[秒的定时器来检测每秒内是否收到了]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元。当连续]{style="font-family:宋体"}*[down-seconds]{lang="EN-US"}*[秒收到]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元后，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[，当连续]{style="font-family:宋体"}*[up-seconds]{lang="EN-US"}*[秒没有收到]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元后，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1658275472}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x346038706}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[PVC1/32]{lang="EN-US"}[上修改]{style="font-family:宋体"}[AIS-RDI]{lang="EN-US"}[告警检测参数，]{style="font-family:宋体"}*[up-seconds]{lang="EN-US"}*[为]{style="font-family:宋体"}[5]{lang="EN-US"}[，]{style="font-family:
宋体"}*[down-seconds]{lang="EN-US"}*[为]{style="font-family:
宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x1123175102}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc 1/32]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-1/32\] oam ais-rdi up 5 down 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1888087123}[在]{style="font-family:宋体"}[PVC-group2]{lang="EN-US"}[下的]{style="font-family:宋体"}[PVC1/33]{lang="EN-US"}[上修改]{style="font-family:宋体"}[AIS-RDI]{lang="EN-US"}[告警检测参数，]{style="font-family:宋体"}*[up-seconds]{lang="EN-US"}*[为]{style="font-family:宋体"}[5]{lang="EN-US"}[，]{style="font-family:
宋体"}*[down-secondst]{lang="EN-US"}*[为]{style="font-family:
宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_604699556}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 2]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-2\] pvc 1/33]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-2-pvc-1/33\] oam ais-rdi up 5 down 5]{lang="EN-US"}
:::

::: {#-1666329201 .myid}
[]{#_Toc404785249}[]{#struct_0_19500_x1656_x1113405143}[]{#_Toc348095183}[]{#_Toc328667725}

**ATM \-- ATM配置命令 \-- oam cc**

------------------------------------------------------------------------

[**[oam cc]{lang="EN-US"}**]{#struct_0_19500_x1656_2029138483}[命令用来启动]{style="font-family:宋体"}[OAM CC]{lang="EN-US"}[（]{style="font-family:宋体"}[Continuity Check]{lang="EN-US"}[，连续性检测）功能。]{style="font-family:宋体"}

[**[undo oam cc]{lang="EN-US"}**]{#struct_0_19500_x1656_942787550}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_2072376479}

[**[oam cc]{lang="EN-US"}**[ { **both** \| **sink** \| **source** }]{lang="EN-US"}]{#struct_0_19500_x1656_x1406344318}

[**[undo oam cc]{lang="EN-US"}**]{#struct_0_19500_x1656_x380223190}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1261686692}

[[OAM CC]{lang="EN-US"}]{#struct_0_19500_x1656_605158309}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1360701677}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x162609139}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x918556346}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1265089464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1390271595}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_729578691}

[**[both]{lang="EN-US"}**]{#struct_0_19500_x1656_1763911577}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[作为接收端时启动]{style="font-family:宋体"}[CC]{lang="EN-US"}[信元的检测功能，以及作为发送端时启动]{style="font-family:宋体"}[CC]{lang="EN-US"}[信元的发送功能。]{style="font-family:宋体"}

[**[sink]{lang="EN-US"}**]{#struct_0_19500_x1656_169985860}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[作为接收端时启动]{style="font-family:宋体"}[CC]{lang="EN-US"}[信元的检测功能。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_19500_x1656_44085964}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[作为发送端时启动]{style="font-family:宋体"}[CC]{lang="EN-US"}[信元的发送功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605223845}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置]{lang="EN-US" style="font-family:宋体"}[OAM CC]{lang="EN-US"}]{#struct_0_19500_x1656_47885351}[功能时，一端配置为]{lang="EN-US" style="font-family:宋体"}**[source]{lang="EN-US"}**[，另一端配置为]{lang="EN-US" style="font-family:宋体"}**[sink]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[启动]{style="font-family:宋体"}]{#struct_0_19500_x1656_1791405596}[OAM CC]{lang="EN-US"}[功能后，一端作为接收端启动]{style="font-family:宋体"}[CC]{lang="EN-US"}[信元的检测功能，一端作为发送端启动]{style="font-family:宋体"}[CC]{lang="EN-US"}[信元的发送功能。如果检测端]{style="font-family:宋体"}[3]{lang="EN-US"}[秒内收不到]{style="font-family:宋体"}[CC]{lang="EN-US"}[信元，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[。当再收到]{style="font-family:宋体"}[CC]{lang="EN-US"}[信元后，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x47991294}

[]{#struct_0_19500_x1656_x2130973674}[[\# ]{lang="EN-US"}]{#_Toc160877085}[在]{style="font-family:
宋体"}[ATM]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[PVC1/32]{lang="EN-US"}[上]{style="font-family:宋体"}[启动]{style="font-family:宋体"}[OAM CC]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_881984151}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc 1/32]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-1/32\] oam cc sink]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1896655644}[在]{style="font-family:宋体"}[PVC-group2]{lang="EN-US"}[下的]{style="font-family:宋体"}[PVC1/33]{lang="EN-US"}[上启动]{style="font-family:宋体"}[OAM CC]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_605289381}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 2]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-2\] pvc 1/33]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-2-pvc-1/33\] oam cc both]{lang="EN-US"}
:::

::: {#-346654571 .myid}
[]{#_Toc404785250}[]{#struct_0_19500_x1656_x682710332}[]{#_Toc348095184}[]{#_Toc328667726}[]{#_Hlt24528571}

**ATM \-- ATM配置命令 \-- oam loopback**

------------------------------------------------------------------------

[**[oam loopback]{lang="EN-US"}**]{#struct_0_19500_x1656_272188681}[命令用来启动]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元的发送以及重传检测，同时修改相关参数。]{style="font-family:宋体"}**[undo oam loopback]{lang="EN-US"}**[命令用来停止]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元的发送以及重传检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_935214271}

[**[oam loopback]{lang="EN-US"}**[ *interval* \[ **up** *up-count* **down** *down-count* **retry** *retry-interval* \]]{lang="EN-US"}]{#struct_0_19500_x1656_908155333}

[**[undo oam loopback]{lang="EN-US"}**]{#struct_0_19500_x1656_x1902043045}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1268906183}

[[不启动]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_1398410831}[信元的发送，但如果收到]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元，则要进行应答。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605354917}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_817510141}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x946021869}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1183352067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1672777309}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1052869716}

[*[interval]{lang="EN-US"}*]{#struct_0_19500_x1656_x1252139491}[：发送]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元的间隔时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[up]{lang="EN-US"}***[ up-count]{lang="EN-US"}*]{#struct_0_19500_x1656_x1182274732}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[之前，必须连续正确收到]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元的数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[3]{lang="EN-US"}[个。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}***[ down-count]{lang="EN-US"}*]{#struct_0_19500_x1656_788327434}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[之前，连续未收到的]{style="font-family:宋体"}[OAM F5 Loopback ]{lang="EN-US"}[信元的数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[**[retry]{lang="EN-US"}***[ retry-interval]{lang="EN-US"}*]{#struct_0_19500_x1656_605420453}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态改变前，]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[在进行重传验证时的信元发送间隔时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1503999197}

[[启动]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_735788092}[信元的发送以及重传检测功能后，每隔]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[秒发送]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元。如果发出]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元后在]{style="font-family:宋体"}*[retry-interval]{lang="EN-US"}*[秒内未正确收到回应信元，则会立即重发]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}]{#struct_0_19500_x1656_598936721}[信元的发送以及重传检测过程中根据收发信元情况更新]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_162776163}[状态为]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}[，当连续正确收到]{lang="EN-US" style="font-family:宋体"}*[up-count]{lang="EN-US"}*[ ]{lang="EN-US"}[个]{lang="EN-US" style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元后，]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1923065878}[状态为]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}[，当连续未收到]{lang="EN-US" style="font-family:宋体"}*[down-count]{lang="EN-US"}*[个]{lang="EN-US" style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元后，]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x620177900}

[]{#_Toc31686800}[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1130335289}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[PVC1/32]{lang="EN-US"}[上启动]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[检测，周期为]{style="font-family:宋体"}[12]{lang="EN-US"}[秒，]{style="font-family:宋体"}*[up-count]{lang="EN-US"}*[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:
宋体"}*[down-count]{lang="EN-US"}*[为]{style="font-family:
宋体"}[4]{lang="EN-US"}[，重传验证周期为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_605485989}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc 1/32]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-1/32\] oam loopback 12 up 4 down 4 retry 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1112750282}[在]{style="font-family:宋体"}[PVC-group2]{lang="EN-US"}[下的]{style="font-family:宋体"}[PVC1/33]{lang="EN-US"}[上启动]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[检测，周期为]{style="font-family:宋体"}[12]{lang="EN-US"}[秒，]{style="font-family:宋体"}*[up-count]{lang="EN-US"}*[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:
宋体"}*[down-count]{lang="EN-US"}*[为]{style="font-family:
宋体"}[3]{lang="EN-US"}[，重传验证周期为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_1183974588}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 2]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-2\] pvc 1/33]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-2-pvc-1/33\] oam loopback 12 up 4 down 3 retry 2]{lang="EN-US"}
:::

::: {#-900849868 .myid}
[]{#_Toc404785251}[]{#struct_0_19500_x1656_x702723905}[]{#_Toc348095185}[]{#_Toc328667727}

**ATM \-- ATM配置命令 \-- oam ping**

------------------------------------------------------------------------

[**[oam ping]{lang="EN-US"}**]{#struct_0_19500_x1656_1455717609}[命令用来在指定接口的特定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上发送]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元，检测链路的连接情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_450163827}

[**[oam ping interface ]{lang="EN-US"}***[interface-type]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ *interface-number* \| *interface-number.subnumber* } **pvc** { *pvc-name* \| *vpi/vci* } \[ *number* *timeout* \]]{lang="EN-US"}]{#struct_0_19500_x1656_480883845}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605551525}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_1135263675}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1162906105}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_197987911}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1250499211}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1571837129}

[**[interface ]{lang="EN-US"}***[interface-type]{lang="EN-US"}*[ { *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_19500_x1656_x1380418809}[：在指定接口上发送]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}**]{#struct_0_19500_x1656_1809122298}[：在指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上发送]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元。]{style="font-family:宋体"}

[*[pvc-name]{lang="EN-US"}*]{#struct_0_19500_x1656_1351170702}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名中不允许使用"]{style="font-family:宋体"}[/]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，如"]{style="font-family:宋体"}[1/20]{lang="EN-US"}["、"]{style="font-family:宋体"}[a-b]{lang="EN-US"}["就不允许作为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}

[*[vpi/vci]{lang="EN-US"}*]{#struct_0_19500_x1656_605617061}[：]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPI]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[为]{style="font-family:宋体"}[VCI]{lang="EN-US"}[值，取值范围与接口类型相关，请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?-1864992396#_Ref337389143)["。]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[与]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[不能同时为]{style="font-family:宋体"}[0]{lang="EN-US"}[。通常，]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[取值]{style="font-family:宋体"}[0]{lang="EN-US"}[到]{style="font-family:宋体"}[31]{lang="EN-US"}[保留用于特定用途，建议用户不要使用。]{style="font-family:宋体"}

[*[number]{lang="EN-US"}*]{#struct_0_19500_x1656_2130249514}[：发送的]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元的个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[*[timeout]{lang="EN-US"}*]{#struct_0_19500_x1656_x541181802}[：接收]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元应答的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_354452837}

[[本命令用来在指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_1243930769}[接口的特定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上发送]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元，根据在设定的时间内是否收到应答来判断链路的连接情况。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[oam ping]{lang="EN-US"}**]{#struct_0_19500_x1656_2139439793}[命令后，系统先发送一个]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元，如果在]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[超时前收到应答，则收到应答后系统马上再发送一个]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元，如果在]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[超时时还没有收到应答，则在]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[超时后再发送一个]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元。一次]{style="font-family:宋体"}**[oam ping]{lang="EN-US"}**[过程中一共发送]{style="font-family:宋体"}*[number]{lang="EN-US"}*[个]{style="font-family:宋体"}[OAM F5 end-to-end]{lang="EN-US"}[信元。如果没有收到应答，可能是链路不通，也可能是链路太忙而发生丢包。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1650932052}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1394722122}[检测]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC1/32]{lang="EN-US"}[的链路状况，发送]{style="font-family:宋体"}[3]{lang="EN-US"}[个信元，超时时间为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> oam ping interface atm 2/4/0 pvc 1/32 3 1]{lang="EN-US"}]{#struct_0_19500_x1656_604634021}

[PING interface ATM2/4/0 pvc 1/32 with 3 of 53 bytes of oam F5 end-to-end cell(s),]{lang="EN-US"}

[timeout is 1 second(s), press CTRL_C to break]{lang="EN-US"}

[Receive reply from pvc 1/32: time=1 ms]{lang="EN-US"}

[Receive reply from pvc 1/32: time=1 ms]{lang="EN-US"}

[Receive reply from pvc 1/32: time=1 ms ]{lang="EN-US"}

[oam ping statistics:]{lang="EN-US"}

[Cells: Sent = 3, Received = 3, Lost = 0 (0.00% loss)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_63776173}[检测]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC 5/100]{lang="EN-US"}[的链路状况，发送]{style="font-family:宋体"}[3]{lang="EN-US"}[个信元，超时时间为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> oam ping interface atm 2/4/0 pvc 5/100 3 1]{lang="EN-US"}]{#struct_0_19500_x1656_x875795610}

[PING interface ATM2/4/0 pvc 5/100 with 3 of 53 bytes of oam F5 end-to-end cell(s),]{lang="EN-US"}

[timeout is 1 second(s), press CTRL_C to break]{lang="EN-US"}

[Request time out!]{lang="EN-US"}

[Request time out!]{lang="EN-US"}

[Request time out!]{lang="EN-US"}

[oam ping statistics:]{lang="EN-US"}

[Cells: Sent = 3, Received = 0, Lost = 3 (100.00% loss)]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[oam ping]{lang="EN-US"}]{#struct_0_19500_x1656_x1801035660}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1864835581}[[字段]{style="font-family:黑体"}]{#struct_0_19500_x1656_x23138825}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19500_x1656_604699557}

[[PING interface ATM2/4/0 pvc 1/32]{lang="EN-US"}]{#struct_0_19500_x1656_x1113405144}

[[检测]{style="font-family:宋体"}[ATM2/4/0 pvc 1/32]{lang="EN-US"}]{#struct_0_19500_x1656_x1862544286}[链路是否可达]{style="font-family:宋体"}

[[53 bytes]{lang="EN-US"}]{#struct_0_19500_x1656_81266420}

[[每个信元的字节数]{style="font-family:宋体"}]{#struct_0_19500_x1656_729288224}

[[timeout is 1 second(s)]{lang="EN-US"}]{#struct_0_19500_x1656_x1658104067}

[[允许]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_605158306}[的回应时间为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[Receive reply from pvc 1/32: time=1 ms]{lang="EN-US"}]{#struct_0_19500_x1656_1360701680}

[[收到]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x163067906}[的应答，]{style="font-family:宋体"}[time]{lang="EN-US"}[表示响应时间]{style="font-family:宋体"}

[[Request time out]{lang="EN-US"}]{#struct_0_19500_x1656_1794920605}

[[在允许的时间内未收到]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x706324603}[的应答]{style="font-family:宋体"}

[[Sent = 3]{lang="EN-US"}]{#struct_0_19500_x1656_x1206860916}

[[发送的信元数]{style="font-family:宋体"}]{#struct_0_19500_x1656_605223842}

[[Received = 0]{lang="EN-US"}]{#struct_0_19500_x1656_47885344}

[[收到的应答数]{style="font-family:宋体"}]{#struct_0_19500_x1656_254163329}

[[Lost = 3(100.00% loss)]{lang="EN-US"}]{#struct_0_19500_x1656_1126089458}

[[未响应请求信元数及其占发送的总请求信元数的百分比]{style="font-family:宋体"}]{#struct_0_19500_x1656_x696169130}

[[ ]{lang="EN-US"}]{#_Toc328667728}

::: {#-1037826138 .myid}
[]{#_Toc404785252}[]{#struct_0_19500_x1656_605289378}[]{#_Toc348095178}[]{#_Toc328667718}

**ATM \-- ATM配置命令 \-- precedence**

------------------------------------------------------------------------

[**[precedence]{lang="EN-US"}**]{#struct_0_19500_x1656_x1492014405}[命令用来设置]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[中的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的优先级。]{style="font-family:宋体"}

[**[undo precedence]{lang="EN-US"}**]{#struct_0_19500_x1656_1273901339}[命令用来删除]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的优先级设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x334905532}

[**[precedence]{lang="EN-US"}**[ { *min* \[ **to** *max* \] *\|* **default** }]{lang="EN-US"}]{#struct_0_19500_x1656_x1291805712}

[**[undo precedence]{lang="EN-US"}**]{#struct_0_19500_x1656_1781318539}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1310666055}

[[不设置优先级。]{style="font-family:宋体"}]{#struct_0_19500_x1656_25118521}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1918766025}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_605354914}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_817510144}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x946021864}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1182500099}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_2066314968}

[*[min]{lang="EN-US"}*]{#struct_0_19500_x1656_x1751705326}[：该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的最小优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[*[max]{lang="EN-US"}*]{#struct_0_19500_x1656_x730636751}[：该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的最大优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}*[max]{lang="EN-US"}*[值必须大于等于]{style="font-family:宋体"}*[min]{lang="EN-US"}*[值。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_19500_x1656_x143722077}[：指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[为缺省]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。没有指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的优先级别的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包将从缺省]{style="font-family:宋体"}[PVC]{lang="EN-US"}[进行传输。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1426642886}

[[本命令只能对该]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_605420450}[内的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[进行设置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有]{style="font-family:宋体"}]{#struct_0_19500_x1656_1503999198}[PVC]{lang="EN-US"}[被]{style="font-family:宋体"}**[precedence]{lang="EN-US"}**[命令指定]{style="font-family:宋体"}**[default]{lang="EN-US"}**[参数，则没有指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的优先级别的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包将从未设置优先级的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[轮询地进行传输。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未找到]{style="font-family:宋体"}]{#struct_0_19500_x1656_735460412}[IP]{lang="EN-US"}[包对应优先级别的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，而且既没有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[被]{style="font-family:宋体"}**[precedence]{lang="EN-US"}**[命令指定]{style="font-family:宋体"}**[default]{lang="EN-US"}**[参数，也没有未设置优先级的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，则该包将做丢弃处理。]{style="font-family:宋体"}

[[需要注意的是，本命令并不能改变]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_386807803}[包的优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_140551791}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_511344921}[设置名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/32]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[包。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_605485986}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\] pvc aa 1/32]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/32\] precedence 0 to 3]{lang="EN-US"}
:::

::: {#537778219 .myid}
[]{#_Toc404785253}[]{#struct_0_19500_x1656_1112750287}[]{#_Toc348095186}

**ATM \-- ATM配置命令 \-- pvc**

------------------------------------------------------------------------

[[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_1183646908}[接口视图、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口视图下：]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}**]{#struct_0_19500_x1656_137453670}[命令用来创建一条]{style="font-family:宋体"}[PVC]{lang="EN-US"}[并进入]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[已创建，则直接进入该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[**[undo pvc]{lang="EN-US"}**]{#struct_0_19500_x1656_1999368198}[命令用来删除指定的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x1209814031}[视图下：]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}**]{#struct_0_19500_x1656_553013508}[命令用来创建一条属于该]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[并进入]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[在]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[已经存在，则直接进入该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[**[undo pvc]{lang="EN-US"}**]{#struct_0_19500_x1656_x779567880}[命令用来将指定的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[从]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[中退出，并删除该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x566408850}

[**[pvc]{lang="EN-US"}**[ { *pvc-name* \[ *vpi/vci* \] \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_19500_x1656_605551522}

[**[undo pvc]{lang="EN-US"}**[ { *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_19500_x1656_1135263678}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1162054137}

[[没有创建]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x980343239}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x823799823}

[]{#struct_0_19500_x1656_x1995891984}[]{#OLE_LINK6}[[ATM]{lang="EN-US"}]{#OLE_LINK5}[接口视图]{style="font-family:宋体"}[/ATM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1976624321}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1756563247}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1125238424}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605617058}

[*[pvc-name]{lang="EN-US"}*]{#struct_0_19500_x1656_x208402637}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名中不允许使用"]{style="font-family:宋体"}[/]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，如"]{style="font-family:宋体"}[1/20]{lang="EN-US"}["、"]{style="font-family:宋体"}[a-b]{lang="EN-US"}["就不允许作为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}

[*[vpi/vci]{lang="EN-US"}*]{#struct_0_19500_x1656_x1596258259}[：]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPI]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[为]{style="font-family:宋体"}[VCI]{lang="EN-US"}[值，取值范围与接口类型相关，请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?-1864992396#_Ref337389143)["。]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[与]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[不能同时为]{style="font-family:宋体"}[0]{lang="EN-US"}[。通常，]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[取值]{style="font-family:宋体"}[0]{lang="EN-US"}[到]{style="font-family:宋体"}[31]{lang="EN-US"}[保留用于特定用途，建议用户不要使用。]{style="font-family:宋体"}

[]{#struct_0_19500_x1656_1762194416}[]{#_Toc95359221}[]{#_Toc85604331}[]{#_Toc81386710}[]{#_Toc74661833}[]{#_Toc72589796}[]{#_Toc72589523}[]{#_Toc72589008}[]{#_Toc65921178}[]{#_Toc65919126}[]{#_Toc65919101}[]{#_Toc65910735}[]{#_Toc65909980}[]{#_Toc60125190}[]{#_Toc60111189}[[表1-8 ]{lang="EN-US"}[不同接口对应的]{style="font-family:黑体"}[VCI]{lang="EN-US"}]{#_Ref57541113}[取值范围]{style="font-family:黑体"}[]{#_Ref337389143}

[]{#table_struct_0_x1864113371}[[接口类型]{style="font-family:黑体"}]{#struct_0_19500_x1656_x190634473}
:::

[[VCI]{lang="EN-US"}]{#struct_0_19500_x1656_366672084}[取值范围]{style="font-family:黑体"}

[[ATM ADSL]{lang="EN-US"}]{#struct_0_19500_x1656_1749502832}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_19500_x1656_604634018}

[[ATM ADSL2+]{lang="EN-US"}]{#struct_0_19500_x1656_2020091318}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_19500_x1656_x456352773}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_19500_x1656_x1253570311}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_19500_x1656_x1830761552}

[[ATM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_19500_x1656_1310737170}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_19500_x1656_604699554}

[[ATM SHDSL_4WIRE_BIS]{lang="EN-US"}]{#struct_0_19500_x1656_x1113405141}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_19500_x1656_x1103029399}

[[ATM SHDSL_8WIRE_BIS]{lang="EN-US"}]{#struct_0_19500_x1656_x290672563}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_19500_x1656_x719962829}

[[ATM E1]{lang="EN-US"}]{#struct_0_19500_x1656_x1642206771}

[[\<0-511\>]{lang="EN-US"}]{#struct_0_19500_x1656_605158307}

[[ATM T1]{lang="EN-US"}]{#struct_0_19500_x1656_1360701679}

[[\<0-511\>]{lang="EN-US"}]{#struct_0_19500_x1656_x163526643}

[[ATM E3]{lang="EN-US"}]{#struct_0_19500_x1656_x970138421}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_19500_x1656_x917414622}

[[ATM T3]{lang="EN-US"}]{#struct_0_19500_x1656_605223843}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_19500_x1656_47885345}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_19500_x1656_x1702151807}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_19500_x1656_x2116493030}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_19500_x1656_1588790797}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_19500_x1656_605289379}

[[ATM 25M]{lang="EN-US"}]{#struct_0_19500_x1656_x1492014404}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_19500_x1656_x1454982016}

[[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_1212158920}[子接口]{style="font-family:宋体"}

[[与]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_605354915}[子接口所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的取值范围相同]{style="font-family:宋体"}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_817510143}

[[与]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x946021867}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的取值范围相同]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1182696707}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_19500_x1656_867590246}[PVC]{lang="EN-US"}[时必须指定]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[。每条]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值对在一个接口范围内（包括接口和子接口以及它们的]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[）唯一。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果创建]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1567737614}[时指定了]{lang="EN-US" style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[，则可以通过命令]{lang="EN-US" style="font-family:宋体"}**[pvc]{lang="EN-US"}**[ *pvc-name* \[ *vpi/vci* \]]{lang="EN-US"}[进入该]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}[在删除该]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[时，既可以通过命令]{lang="EN-US" style="font-family:宋体"}**[undo pvc]{lang="EN-US"}**[ *pvc-name* \[ *vpi/vci* \]]{lang="EN-US"}[，也可以通过命令]{lang="EN-US" style="font-family:宋体"}**[undo pv]{lang="EN-US"}[c]{lang="EN-US"}**[ *vpi/vci*]{lang="EN-US"}[来完成]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ATM P2P]{lang="EN-US"}]{#struct_0_19500_x1656_2071796369}[子接口只允许配置一个]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_19500_x1656_605420451}[PVC-group]{lang="EN-US"}[下最多允许创建]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_19500_x1656_1503999199}[ATM]{lang="EN-US"}[接口]{style="font-family:宋体"}[/ATM]{lang="EN-US"}[子接口下不能删除]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[内的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[实际可以创建的]{style="font-family:宋体"}]{#struct_0_19500_x1656_735394876}[PVC]{lang="EN-US"}[数量与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x701451958}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1551997439}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_105323870}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc aa 1/101 ]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-aa-1/101\] ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x359740885}[在]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[下创建一条名为"]{style="font-family:宋体"}[bb]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/102]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_605485987}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\] pvc bb 1/102]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1-pvc-bb-1/102\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1112750288}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display atm pvc-info]{lang="EN-US"}**]{#struct_0_19500_x1656_1184367804}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pvc-group]{lang="EN-US"}**]{#struct_0_19500_x1656_397858150}

::: {#1584937201 .myid}
[]{#_Toc404785254}[]{#struct_0_19500_x1656_464173135}[]{#_Toc348095187}

**ATM \-- ATM配置命令 \-- pvc-group**

------------------------------------------------------------------------

[**[pvc-group]{lang="EN-US"}**]{#struct_0_19500_x1656_21603287}[命令用来创建一个]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[或进入已经创建的]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo pvc-group]{lang="EN-US"}**]{#struct_0_19500_x1656_x965697837}[命令用来删除指定的]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_625430976}

[**[pvc-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_19500_x1656_931870508}

[**[undo]{lang="EN-US"}**[ **pvc-group** *group-number*]{lang="EN-US"}]{#struct_0_19500_x1656_605551523}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1135263677}

[[没有创建]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_1163037177}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x968719346}

[[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_331084070}[接口视图]{style="font-family:宋体"}[/ATM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1603140411}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_851387337}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x994983447}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605617059}

[*[group-number]{lang="EN-US"}*]{#struct_0_19500_x1656_x208402638}[：]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1597110227}

[[使用]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_1095510667}[后，可以在]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[下的各]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上进行流量的负载分担，将不同优先级的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包通过不同的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[进行传输。用户可以配置每条]{style="font-family:宋体"}[PVC]{lang="EN-US"}[承载的]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的优先级。]{style="font-family:宋体"}

[[当收到]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_1482250244}[包后，根据]{style="font-family:宋体"}[IP]{lang="EN-US"}[包的优先级来找到对应的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[进行传输，如果没有找到对应的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，则从缺省]{style="font-family:宋体"}[PVC]{lang="EN-US"}[（]{style="font-family:宋体"}**[precedence]{lang="EN-US"}**[命令中使用了]{style="font-family:宋体"}**[default]{lang="EN-US"}**[参数）进行传输，如果没有配置缺省]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，则从未设置优先级的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[轮询地进行传输。如果没有未设置优先级的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，则将该]{style="font-family:宋体"}[IP]{lang="EN-US"}[包丢弃。]{style="font-family:宋体"}

[[如果收到的不是]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19500_x1656_x1915193416}[包，则从该]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[下所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[轮询地进行传输。]{style="font-family:宋体"}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_x415248910}[下的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的封装类型、承载的协议类型直接从]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[获取。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1710524718}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1799044487}[只能属于一个]{lang="EN-US" style="font-family:宋体"}[PVC-group]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令可以在]{lang="EN-US" style="font-family:宋体"}[ATM P2MP]{lang="EN-US"}]{#struct_0_19500_x1656_604634019}[子接口下配置，不能在]{lang="EN-US" style="font-family:宋体"}[ATM P2P]{lang="EN-US"}[子接口下配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_2020091317}[的编号在一个接口范围内（包括接口和子接口）唯一。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x456942597}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1634006591}[创建一个编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x914270691}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1961808370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display atm pvc-group]{lang="EN-US"}**]{#struct_0_19500_x1656_1659678193}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[precedence]{lang="EN-US"}**]{#struct_0_19500_x1656_x20198993}
:::

::: {#743086101 .myid}
[]{#_Toc404785255}[]{#struct_0_19500_x1656_1060355720}[]{#_Toc356993805}

**ATM \-- ATM配置命令 \-- remark atm-clp**

------------------------------------------------------------------------

[**[remark atm-clp]{lang="EN-US"}**]{#struct_0_19500_x1656_1060945543}[命令用来重新标记]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的]{style="font-family:宋体"}[CLP]{lang="EN-US"}[标志位的值。]{style="font-family:宋体"}

[**[undo remark atm-clp]{lang="EN-US"}**]{#struct_0_19500_x1656_932223408}[命令用来取消重新标记]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的]{style="font-family:宋体"}[CLP]{lang="EN-US"}[标志位的值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1060880007}

[**[remark]{lang="EN-US"}**[ \[ **green** \| **red** \| **yellow** \] **atm-clp** *atm-clp-value*]{lang="EN-US"}]{#struct_0_19500_x1656_1061076615}

[**[undo remark]{lang="EN-US"}**[ \[ **green** \| **red** \| **yellow** \] **atm-clp**]{lang="EN-US"}]{#struct_0_19500_x1656_1061011079}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_2117978220}

[[没有配置重新标记]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_1060683399}[信元的]{style="font-family:宋体"}[CLP]{lang="EN-US"}[标志位的值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1060617863}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_1060814471}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_166536501}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1060748935}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1060421255}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1060355719}

[**[green]{lang="EN-US"}**]{#struct_0_19500_x1656_547592951}[：对绿色报文进行重新标记。]{style="font-family:宋体"}

[**[red]{lang="EN-US"}**]{#struct_0_19500_x1656_1060945542}[：对红色报文进行重新标记。]{style="font-family:宋体"}

[**[yellow]{lang="EN-US"}**]{#struct_0_19500_x1656_1060880006}[：对黄色报文进行重新标记。]{style="font-family:宋体"}

[*[atm-clp-value]{lang="EN-US"}*]{#struct_0_19500_x1656_1061076614}[：]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元]{style="font-family:宋体"}[CLP]{lang="EN-US"}[（]{style="font-family:宋体"}[Cell Loss Priority]{lang="EN-US"}[，信元丢失优先级）标志位的值，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[。发生拥塞时优先丢弃]{style="font-family:
宋体"}[CLP]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的信元。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1812590739}

[[配置了该特性的策略只能应用在]{style="font-family:宋体"}[ATM PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1061011078}[出方向上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1060683398}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1060617862}[重新标记]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的]{style="font-family:宋体"}[CLP]{lang="EN-US"}[标志位的值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_1060814470}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark atm-clp 1]{lang="EN-US"}
:::

::: {#-922020787 .myid}
[]{#_Toc404785256}[]{#struct_0_19500_x1656_604699555}[]{#_Toc348095189}[]{#_Toc136937659}[]{#_Toc348114943}[]{#_Toc348114944}

**ATM \-- ATM配置命令 \-- reset atm interface**

------------------------------------------------------------------------

[**[reset atm interface]{lang="EN-US"}**]{#struct_0_19500_x1656_x1113405142}[命令用来清除]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x699744872}

[**[reset atm interface]{lang="EN-US"}**[ \[ *interface-type* { *interface-number* \| *interface-number.subnumber* } \]]{lang="EN-US"}]{#struct_0_19500_x1656_343734452}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_649607626}

[[用户视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_1084105820}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1774501464}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_2139602886}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_849146378}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605158304}

[*[interface-type ]{lang="EN-US"}*[{ *interface-number* \| *interface-number.subnumber* }]{lang="EN-US"}]{#struct_0_19500_x1656_1360701682}[：清除指定接口下的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[（包括接口下的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[和]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[下的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[）的统计信息。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。不指定本参数时，将清除所有接口下的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x162936834}

[[本命令只能清除]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_622845258}[的统计信息，不能清除接口的统计信息，接口的统计信息可以通过]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令来清除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1136918763}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1772864815}[清除接口]{style="font-family:宋体"}[ATM2/4/0]{lang="EN-US"}[下的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset atm interface atm 2/4/0]{lang="EN-US"}]{#struct_0_19500_x1656_339316500}
:::

::: {#998864996 .myid}
[]{#_Toc404785257}[]{#struct_0_19500_x1656_x685068835}[]{#_Toc350872247}[]{#_Toc345946920}

**ATM \-- ATM配置命令 \-- reset counters interface virtual-ethernet**

------------------------------------------------------------------------

[**[reset counters interface virtual-ethernet]{lang="EN-US"}**]{#struct_0_19500_x1656_605223840}[命令用来清除]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_47885346}

[**[reset counters interface]{lang="EN-US"}**[ \[ **virtual-ethernet** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_19500_x1656_x128173695}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1197449569}

[[用户视图]{style="font-family:宋体"}]{#struct_0_19500_x1656_x333474051}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1152249814}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1700400503}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_390734693}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1675559996}

[**[virtual-ethernet]{lang="EN-US"}**]{#struct_0_19500_x1656_605289376}[：清除]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_19500_x1656_x1492014399}[：]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1408386600}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_19500_x1656_2112206457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19500_x1656_1214833045}**[virtual-ethernet]{lang="EN-US"}**[参数，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[virtual-ethernet]{lang="EN-US"}**]{#struct_0_19500_x1656_1556719184}[参数而不指定]{lang="EN-US" style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[VE]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[virtual-ethernet]{lang="EN-US"}**]{#struct_0_19500_x1656_461329652}[和]{lang="EN-US" style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[VE]{lang="EN-US"}[接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_952621463}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1703575748}[清除]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/2]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface virtual-ethernet 2/4/2]{lang="EN-US"}]{#struct_0_19500_x1656_605354912}
:::

::: {#1437517977 .myid}
[]{#_Toc404785258}[]{#struct_0_19500_x1656_817510146}[]{#_Toc348095190}[]{#_Toc348114947}[]{#_Toc348114948}

**ATM \-- ATM配置命令 \-- service cbr**

------------------------------------------------------------------------

[**[service]{lang="EN-US"}**[ **cbr**]{lang="EN-US"}]{#struct_0_19500_x1656_x946021862}[命令用来指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[CBR]{lang="EN-US"}[（]{style="font-family:宋体"}[Constant Bit Rate]{lang="EN-US"}[，恒定速率），并指定相关的服务参数。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_19500_x1656_1182893315}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_2035417550}

[**[service]{lang="EN-US"}**[ **cbr** *output-pcr* \[ **cdvt** *cdvt_value* \]]{lang="EN-US"}]{#struct_0_19500_x1656_623029066}

[**[undo service]{lang="EN-US"}**]{#struct_0_19500_x1656_x831850666}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1371398933}

[[创建一个]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_605420448}[后，该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[UBR]{lang="EN-US"}[，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所在接口的最大带宽。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x834652954}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x817705970}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1628713104}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_2078511439}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_2111878155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x660693895}

[*[output-pcr]{lang="EN-US"}*]{#struct_0_19500_x1656_524255071}[：输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率，不同接口的]{style="font-family:宋体"}*[output-pcr]{lang="EN-US"}*[取值范围请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-9]{lang="EN-US"}](?1437517977#_Ref57606154)[，单位为]{style="font-family:宋体"}[Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_19500_x1656_961622840}[]{#_Toc95359224}[]{#_Toc85604334}[]{#_Toc81386713}[]{#_Toc74661836}[]{#_Toc72589799}[]{#_Toc72589526}[]{#_Toc72589011}[]{#_Toc65921181}[]{#_Toc65919129}[]{#_Toc65919104}[]{#_Toc65910738}[]{#_Toc65909983}[]{#_Toc60125193}[]{#_Toc60111192}[[表1-9 ]{lang="EN-US"}*[output-pcr]{lang="EN-US"}*]{#_Ref57606154}[的取值范围]{style="font-family:黑体"}

[]{#table_struct_0_x1873799611}[[接口类型]{style="font-family:黑体"}]{#struct_0_19500_x1656_605485984}
:::

[[output-pcr]{lang="EN-US"}]{#struct_0_19500_x1656_1112750285}[取值范围]{style="font-family:黑体"}

[[ATM ADSL]{lang="EN-US"}]{#struct_0_19500_x1656_1183515836}

[[\<64-640\>]{lang="EN-US"}]{#struct_0_19500_x1656_2074983893}

[[ATM ADSL2+]{lang="EN-US"}]{#struct_0_19500_x1656_1629133775}

[[\<64-640\>]{lang="EN-US"}]{#struct_0_19500_x1656_2102759830}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_19500_x1656_605551520}

[[\<64-2312\>]{lang="EN-US"}]{#struct_0_19500_x1656_1135263680}

[[ATM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_19500_x1656_1162578416}

[[\<128-4624\>]{lang="EN-US"}]{#struct_0_19500_x1656_1828564562}

[[ATM SHDSL_4WIRE_BIS]{lang="EN-US"}]{#struct_0_19500_x1656_306733259}

[[\<128-11392\>]{lang="EN-US"}]{#struct_0_19500_x1656_605617056}

[[ATM SHDSL_8WIRE_BIS]{lang="EN-US"}]{#struct_0_19500_x1656_x208402643}

[[\<256-22784\>]{lang="EN-US"}]{#struct_0_19500_x1656_x1596520400}

[[ATM E1]{lang="EN-US"}]{#struct_0_19500_x1656_1913500906}

[[\<64-1920\>]{lang="EN-US"}]{#struct_0_19500_x1656_x1771895678}

[[ATM T1]{lang="EN-US"}]{#struct_0_19500_x1656_1925368615}

[[\<64-1536\>]{lang="EN-US"}]{#struct_0_19500_x1656_604634016}

[[ATM E3]{lang="EN-US"}]{#struct_0_19500_x1656_2020091316}

[[\<64-34000\>]{lang="EN-US"}]{#struct_0_19500_x1656_x457008133}

[[ATM T3]{lang="EN-US"}]{#struct_0_19500_x1656_x486893954}

[[\<64-44000\>]{lang="EN-US"}]{#struct_0_19500_x1656_604699552}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_19500_x1656_x1113405147}

[[\<64-155000\>]{lang="EN-US"}]{#struct_0_19500_x1656_x296460345}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_19500_x1656_x1900272087}

[[不支持]{style="font-family:宋体"}]{#struct_0_19500_x1656_2018039280}

[[ATM 25M]{lang="EN-US"}]{#struct_0_19500_x1656_605158305}

[[不支持]{style="font-family:宋体"}]{#struct_0_19500_x1656_1360701681}

[[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_x163002370}[子接口]{style="font-family:宋体"}

[[与]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_x2108618349}[子接口所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的取值范围相同]{style="font-family:宋体"}

[[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_605223841}

[[与]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_19500_x1656_47885347}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的取值范围相同]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[**[cdvt ]{lang="EN-US"}***[cdvt_value]{lang="EN-US"}*]{#struct_0_19500_x1656_x2084488831}[：信元时延变化容限（]{style="font-family:宋体"}[Cell Delay Variation Tolerance]{lang="EN-US"}[），取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为μ]{style="font-family:宋体"}[s]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[500]{lang="EN-US"}[μ]{style="font-family:宋体"}[s]{lang="EN-US"}[，表示信元的最大时延是]{style="font-family:
宋体"}[500]{lang="EN-US"}[μ]{style="font-family:宋体"}[s]{lang="EN-US"}[。设置该参数后，当超出峰值速率后，会根据该参数分配缓存，保证业务的稳定。该参数的值配置的越小，要求的硬件资源越多，越不容易配置成功。若配置不成功，可将]{style="font-family:宋体"}*[cdvt_value]{lang="EN-US"}*[的值调大，再试着配置，此情况会在命令行中给出提示（]{style="font-family:宋体"}[Failed to set service parameter. Please adjust cdvt value.]{lang="EN-US"}[）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1954584104}

[[可以使用本命令以及]{style="font-family:宋体"}**[service ubr]{lang="EN-US"}**]{#struct_0_19500_x1656_x352090068}[、]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **vbr-nrt**]{lang="EN-US"}[，]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **vbr-rt**]{lang="EN-US"}[命令来设置]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型和服务参数。新指定的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[服务类型将会覆盖已有的服务类型。]{style="font-family:宋体"}

[[因为每个]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_87028131}[的带宽是独占的，所以建议在设置]{style="font-family:宋体"}[CBR]{lang="EN-US"}[带宽时先设置需要大带宽的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，再设置需要小带宽的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[本命令不支持]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}]{#struct_0_19500_x1656_x1089757085}[接口和]{style="font-family:宋体"}[ATM E3]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605289377}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1492014398}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，并指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[CBR]{lang="EN-US"}[，]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元峰值发送速率为]{style="font-family:宋体"}[50,000Kbit/s]{lang="EN-US"}[，信元时延变化容限为]{style="font-family:宋体"}[1000]{lang="EN-US"}[μ]{style="font-family:宋体"}[s]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_157697341}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-aa-1/101\] service cbr 50000 cdvt 1000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x574117767}[在]{style="font-family:宋体"}[PVC-group1]{lang="EN-US"}[下创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，并指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[CBR]{lang="EN-US"}[，]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元峰值发送速率为]{style="font-family:宋体"}[50,000Kbit/s]{lang="EN-US"}[，信元时延变化容限为]{style="font-family:宋体"}[1000]{lang="EN-US"}[μ]{style="font-family:宋体"}[s]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x869185280}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101\] service cbr 50000 cdvt 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1847367744}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service ubr]{lang="EN-US"}**]{#struct_0_19500_x1656_x234005785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service vbr-nrt]{lang="EN-US"}**]{#struct_0_19500_x1656_605354913}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service vbr-rt]{lang="EN-US"}**]{#struct_0_19500_x1656_817510145}

::: {#1437517963 .myid}
[]{#_Toc404785259}[]{#struct_0_19500_x1656_x946021865}[]{#_Toc348095191}

**ATM \-- ATM配置命令 \-- service ubr**

------------------------------------------------------------------------

[**[service]{lang="EN-US"}**[ **ubr**]{lang="EN-US"}]{#struct_0_19500_x1656_1182565635}[命令用来指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[UBR]{lang="EN-US"}[（]{style="font-family:宋体"}[Unspecified Bit Rate]{lang="EN-US"}[，非确定速率），并指定相关的服务参数。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_19500_x1656_x1855013419}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x601269885}

[**[service]{lang="EN-US"}**[ **ubr** *output-pcr*]{lang="EN-US"}]{#struct_0_19500_x1656_1379273258}

[**[undo service]{lang="EN-US"}**]{#struct_0_19500_x1656_558148071}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x443914510}

[[创建一个]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_605420449}[后，该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[UBR]{lang="EN-US"}[，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所在接口的最大带宽。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x834652953}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x817771506}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1299144229}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x534762760}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_118279149}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x286594139}

[*[output-pcr]{lang="EN-US"}*]{#struct_0_19500_x1656_x1275062474}[：输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率，取值范围请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-9]{lang="EN-US"}](?1437517977#_Ref57606154)[，单位为]{style="font-family:宋体"}[Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_688668519}

[[可以使用本命令以及]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **cbr**]{lang="EN-US"}]{#struct_0_19500_x1656_605485985}[、]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **vbr-nrt**]{lang="EN-US"}[、]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **vbr-rt**]{lang="EN-US"}[命令来设置]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型和服务参数。新指定的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[服务类型将会覆盖已有的服务类型。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1112750286}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1183712444}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，并指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[UBR]{lang="EN-US"}[，]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元峰值发送速率为]{style="font-family:宋体"}[100,000Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x1848406561}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-aa-1/101\] service ubr 100000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x228349665}[在]{style="font-family:宋体"}[PVC-group1]{lang="EN-US"}[下创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，并指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[UBR]{lang="EN-US"}[，]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元峰值发送速率为]{style="font-family:宋体"}[100,000Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x1934943632}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101\] service ubr 100000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_605551521}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service]{lang="EN-US"}**[ **cbr**]{lang="EN-US"}]{#struct_0_19500_x1656_1135263679}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service vbr-nrt]{lang="EN-US"}**]{#struct_0_19500_x1656_1162119673}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service vbr-rt]{lang="EN-US"}**]{#struct_0_19500_x1656_649601907}
:::

::: {#-1320464405 .myid}
[]{#_Toc404785260}[]{#struct_0_19500_x1656_744497588}[]{#_Toc348095192}

**ATM \-- ATM配置命令 \-- service vbr-nrt**

------------------------------------------------------------------------

[**[service]{lang="EN-US"}**[ **vbr-nrt**]{lang="EN-US"}]{#struct_0_19500_x1656_x1982739104}[命令用来指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[VBR-NRT]{lang="EN-US"}[（]{style="font-family:宋体"}[Variable Bit Rate-Non Real Time]{lang="EN-US"}[，非实时可变速率），并指定相关的服务参数。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_19500_x1656_50641134}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x897867427}

[**[service]{lang="EN-US"}**[ **vbr-nrt** *output-pcr output-scr output-mbs*]{lang="EN-US"}]{#struct_0_19500_x1656_x1241277626}

[**[undo service]{lang="EN-US"}**]{#struct_0_19500_x1656_605617057}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x208402644}

[[创建一个]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1596323792}[后，该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[UBR]{lang="EN-US"}[，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所在接口的最大带宽。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1340170723}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_1167931495}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1947518793}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1930553364}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1147308301}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2097223471}

[*[output-pcr]{lang="EN-US"}*]{#struct_0_19500_x1656_604634017}[：输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率，取值范围请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-9]{lang="EN-US"}](?1437517977#_Ref57606154)[，单位为]{style="font-family:宋体"}[Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[output-scr]{lang="EN-US"}*]{#struct_0_19500_x1656_2020091315}[：输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的可承受速率，取值范围与]{style="font-family:宋体"}*[output-pcr]{lang="EN-US"}*[相同，并且]{style="font-family:宋体"}*[output-scr]{lang="EN-US"}*[小于等于]{style="font-family:宋体"}*[output-pcr]{lang="EN-US"}*[，单位为]{style="font-family:宋体"}[Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[output-mbs]{lang="EN-US"}*]{#struct_0_19500_x1656_x457073669}[：输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的最大突发长度，即接口输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的最大缓冲数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[512]{lang="EN-US"}[，单位为信元数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_753832914}

[[可以使用本命令以及]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **cbr**]{lang="EN-US"}]{#struct_0_19500_x1656_1349528436}[、]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **ubr**]{lang="EN-US"}[、]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **vbr-rt**]{lang="EN-US"}[命令来设置]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型和服务参数。新指定的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[服务类型将会覆盖已有的服务类型。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_309651466}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1002233094}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，并指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[VBR-NRT]{lang="EN-US"}[，且]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元峰值发送速率为]{style="font-family:宋体"}[100,000Kbit/s]{lang="EN-US"}[、可承受发送速率为]{style="font-family:宋体"}[50,000Kbit/s]{lang="EN-US"}[、最大突发长度为]{style="font-family:宋体"}[320]{lang="EN-US"}[个信元。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_604699553}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc aa 1/101]{lang="EN-US"}

[]{#_Hlt23223772}[\[Sysname-ATM2/4/0-pvc-aa-1/101\] service vbr-nrt 100000 50000 320]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x1113405148}[在]{style="font-family:宋体"}[PVC-group  1]{lang="EN-US"}[下]{style="font-family:宋体"} [创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，并指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[VBR-NRT]{lang="EN-US"}[，且]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元峰值发送速率为]{style="font-family:宋体"}[100,000Kbit/s]{lang="EN-US"}[、可承受发送速率为]{style="font-family:宋体"}[50,000Kbit/s]{lang="EN-US"}[、最大突发长度为]{style="font-family:宋体"}[320]{lang="EN-US"}[个信元。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_819284902}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101\] service vbr-nrt 100000 50000 320]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_273832393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service]{lang="EN-US"}**[ **cbr**]{lang="EN-US"}]{#struct_0_19500_x1656_x760906604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service]{lang="EN-US"}**[ **ubr**]{lang="EN-US"}]{#struct_0_19500_x1656_310697290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service]{lang="EN-US"}**[ **vbr-rt**]{lang="EN-US"}]{#struct_0_19500_x1656_x315018997}
:::

::: {#1458201989 .myid}
[]{#_Toc404785261}[]{#struct_0_19500_x1656_x1793034616}[]{#_Toc348095193}

**ATM \-- ATM配置命令 \-- service vbr-rt**

------------------------------------------------------------------------

[**[service]{lang="EN-US"}**[ **vbr-rt**]{lang="EN-US"}]{#struct_0_19500_x1656_x2123725047}[命令用来指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[VBR-RT]{lang="EN-US"}[（]{style="font-family:宋体"}[Variable Bit Rate-Real Time]{lang="EN-US"}[，实时可变速率），并指定相关的服务参数。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_19500_x1656_x2037046724}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1528598797}

[**[service]{lang="EN-US"}**[ **vbr-rt** *output-pcr output-scr output-mbs*]{lang="EN-US"}]{#struct_0_19500_x1656_1604507675}

[**[undo service]{lang="EN-US"}**]{#struct_0_19500_x1656_x459374316}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_2109284285}

[[创建一个]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x173807205}[后，该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[UBR]{lang="EN-US"}[，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[所在接口的最大带宽。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1131039242}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x942062244}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2123659511}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_644247784}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_881647306}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1842036621}

[*[output-pcr]{lang="EN-US"}*]{#struct_0_19500_x1656_x1765318029}[：输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率，取值范围请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-9]{lang="EN-US"}](?1437517977#_Ref57606154)[，单位为]{style="font-family:宋体"}[Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[output-scr]{lang="EN-US"}*]{#struct_0_19500_x1656_x1168296364}[：输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的可承受速率，取值范围与]{style="font-family:宋体"}*[output-pcr]{lang="EN-US"}*[相同，并且]{style="font-family:宋体"}*[output-scr]{lang="EN-US"}*[小于等于]{style="font-family:宋体"}*[output-pcr]{lang="EN-US"}*[，单位为]{style="font-family:宋体"}[Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[output-mbs]{lang="EN-US"}*]{#struct_0_19500_x1656_1906354303}[：输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的最大突发长度，即接口输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的最大缓冲数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[512]{lang="EN-US"}[，单位为信元数。用于]{style="font-family:宋体"}[ATM E3]{lang="EN-US"}[接口时，该参数的取值范围也为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[512]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1290729081}

[[可以使用本命令以及]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **cbr**]{lang="EN-US"}]{#struct_0_19500_x1656_89145041}[、]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **ubr**]{lang="EN-US"}[、]{style="font-family:宋体"}**[service]{lang="EN-US"}**[ **vbr-nrt**]{lang="EN-US"}[命令来设置]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型和服务参数。新指定的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[服务类型将会覆盖已有的服务类型。]{style="font-family:宋体"}

[[本命令不支持]{style="font-family:宋体"}[ATM E1]{lang="EN-US"}]{#struct_0_19500_x1656_x2123593975}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_703446636}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1789137269}[在]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，并指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[VBR-RT]{lang="EN-US"}[，且]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元峰值发送速率为]{style="font-family:宋体"}[100,000Kbit/s]{lang="EN-US"}[、可承受发送速率为]{style="font-family:宋体"}[50,000Kbit/s]{lang="EN-US"}[、最大突发长度为]{style="font-family:宋体"}[320]{lang="EN-US"}[个信元。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x769927895}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-aa-1/101\] service vbr-rt 100000 50000 320]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x692301332}[在]{style="font-family:宋体"}[PVC-group1]{lang="EN-US"}[下创建一条名为"]{style="font-family:宋体"}[aa]{lang="EN-US"}["、]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[为]{style="font-family:宋体"}[1/101]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，并指定该]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的服务类型为]{style="font-family:宋体"}[VBR-RT]{lang="EN-US"}[，且]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元峰值发送速率为]{style="font-family:宋体"}[100,000Kbit/s]{lang="EN-US"}[、可承受发送速率为]{style="font-family:宋体"}[50,000Kbit/s]{lang="EN-US"}[、最大突发长度为]{style="font-family:宋体"}[320]{lang="EN-US"}[个信元。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x1150439099}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101\] service vbr-rt 100000 50000 320]{lang="EN-US"}

[]{#_Toc328667740}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2123528439}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service cbr]{lang="EN-US"}**]{#struct_0_19500_x1656_146780238}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service ubr]{lang="EN-US"}**]{#struct_0_19500_x1656_x1651885054}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service vbr-nrt]{lang="EN-US"}**]{#struct_0_19500_x1656_x851366775}
:::

::: {#1170655049 .myid}
[]{#_Toc404785262}[]{#struct_0_19500_x1656_x452315507}[]{#_Toc350872248}[]{#_Toc345946921}

**ATM \-- ATM配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_19500_x1656_989047585}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_19500_x1656_1867895709}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2012571189}

[**[shutdown]{lang="EN-US"}**]{#struct_0_19500_x1656_416263268}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_19500_x1656_x2123462903}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x948104035}

[[接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_19500_x1656_x1748287906}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1877453517}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_1618061597}[接口视图]{style="font-family:宋体"}[/VE]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_589860994}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1700671232}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1146001473}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1318012810}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x2123397367}[关闭]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口]{style="font-family:宋体"}[Virtual-Ethernet2/4/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x1879988324}

[\[Sysname\] interface virtual-ethernet 2/4/1]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet2/4/1\] shutdown]{lang="EN-US"}
:::

::::: {#-716074350 .myid}
[]{#_Toc404785263}[]{#struct_0_19500_x1656_x730431498}[]{#_Toc348095195}[]{#_Toc335742616}

**ATM \-- ATM配置命令 \-- shutdown**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM命令.files/image001.png){#图片 7 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_19500_x1656_629435904}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_19500_x1656_610803990}
:::

**[ ]{lang="EN-US"}**

[**[shutdown]{lang="EN-US"}**]{#struct_0_19500_x1656_x991617064}[命令用来关闭当前]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_19500_x1656_x1476355324}[命令用来打开当前]{style="font-family:宋体"}[PVC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2123331831}

[**[shutdown]{lang="EN-US"}**]{#struct_0_19500_x1656_426983689}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_19500_x1656_1376385276}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_324506362}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x1522612553}[处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x353544365}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_149954560}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_137606619}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1895624864}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x2123266295}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_762641868}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1049607749}[打开]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下]{style="font-family:宋体"}[PVC0/100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_19500_x1656_1889205385}

[\[Sysname\] interface atm 2/4/0.1]{lang="EN-US"}

[\[Sysname-ATM2/4/0.1\] pvc 0/100]{lang="EN-US"}

[\[Sysname-ATM2/4/0.1-pvc-0/100\] undo shutdown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x801915213}[打开]{style="font-family:宋体"}[PVC-group1]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC1/101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_1882405071}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101\] undo shutdown]{lang="EN-US"}
:::::

::::: {#-1726874890 .myid}
[]{#_Toc348095194}[]{#_Toc328667741}[]{#_Toc404785264}[]{#struct_0_19500_x1656_x2124249335}[]{#_Toc345510478}[]{#_Toc263323280}[]{#_Toc252280809}

**ATM \-- ATM配置命令 \-- sub-interface rate-statistic**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ATM命令.files/image002.jpg){#图片 8 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_19500_x1656_1150160418}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_19500_x1656_x785439501}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[开启本功能后可能需要耗费大量系统资源，请谨慎使用。]{style="font-family:KaiTi_GB2312"}]{#struct_0_19500_x1656_x816704340}
:::

**[ ]{lang="EN-US"}**

[**[sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_19500_x1656_x1486052056}[命令用来开启]{style="font-family:
宋体"}[VE]{lang="EN-US"}[子接口的速率统计功能。]{style="font-family:宋体"}

[**[undo sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_19500_x1656_1515720558}[命令用来关闭]{style="font-family:宋体"}[VE]{lang="EN-US"}[子接口的速率统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_12649662}

[**[sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_19500_x1656_1842282410}

[**[undo sub-interface rate-statistic]{lang="EN-US"}**]{#struct_0_19500_x1656_2037930721}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2124183799}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_853128910}[子接口的速率统计功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_328163106}

[[VE]{lang="EN-US"}]{#struct_0_19500_x1656_1087300563}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_492599187}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1995280940}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1067276531}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_565055405}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_1742684680}[开启接口]{style="font-family:宋体"}[VE2/4/0]{lang="EN-US"}[的子接口速率统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x2123725046}

[\[Sysname\] interface virtual-ethernet 2/4/0]{lang="EN-US"}

[\[Sysname-Virtual-Ethernet2/4/0\] sub-interface rate-statistic]{lang="EN-US"}
:::::

::: {#2022929075 .myid}
[]{#_Toc404785265}[]{#struct_0_19500_x1656_x470962783}

**ATM \-- ATM配置命令 \-- transmit-priority**

------------------------------------------------------------------------

[**[transmit-priority]{lang="EN-US"}**]{#struct_0_19500_x1656_1984883746}[命令用来配置]{style="font-family:宋体"}[UBR]{lang="EN-US"}[、]{style="font-family:宋体"}[VBR-NRT]{lang="EN-US"}[、]{style="font-family:宋体"}[VBR-RT]{lang="EN-US"}[服务下的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的传输优先级。]{style="font-family:宋体"}

[**[undo transmit-priority]{lang="EN-US"}**]{#struct_0_19500_x1656_x1455423021}[命令用来按照]{style="font-family:宋体"}[PVC]{lang="EN-US"}[服务类型恢复对应的缺省传输优先级。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_63935776}

[**[transmit-priority]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_19500_x1656_x1527268191}

[**[undo]{lang="EN-US"}**[ **transmit-priority**]{lang="EN-US"}]{#struct_0_19500_x1656_x1150809737}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2004620635}

[[UBR]{lang="EN-US"}]{#struct_0_19500_x1656_x439423884}[服务的传输优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[；]{style="font-family:宋体"}[VBR-NRT]{lang="EN-US"}[服务的传输优先级为]{style="font-family:宋体"}[5]{lang="EN-US"}[；]{style="font-family:宋体"}[VBR-RT]{lang="EN-US"}[服务的传输优先级为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x1960159434}

[[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x2123659510}[视图]{style="font-family:宋体"}[/PVC-group]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x921836157}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_1041832097}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1495049825}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_432887029}

[*[value]{lang="EN-US"}*]{#struct_0_19500_x1656_x162194066}[：传输优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[，数值大的优先级高。]{style="font-family:宋体"}[UBR]{lang="EN-US"}[服务的传输优先级取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[；]{style="font-family:
宋体"}[VBR-NRT]{lang="EN-US"}[服务的传输优先级取值范围是]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[；]{style="font-family:宋体"}[VBR-RT]{lang="EN-US"}[服务的传输优先级取值范围是]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_967897895}

[[传输优先级高的]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_113553186}[优先占有带宽，相同传输优先级的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[占有相同的带宽。]{style="font-family:宋体"}

[[当改变]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_19500_x1656_x2123593974}[的服务类型时，传输优先级变为当前服务的缺省值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x862637305}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x278507069}[配置]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口下]{style="font-family:宋体"}[PVC1/32]{lang="EN-US"}[的传输优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_1929136489}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc 1/32]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-1/32\] transmit-priority 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x277329277}[配置]{style="font-family:宋体"}[PVC-group1]{lang="EN-US"}[下]{style="font-family:宋体"}[PVC1/101]{lang="EN-US"}[的传输优先级为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_x2106922830}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] pvc-group 1]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1\] pvc aa 1/101]{lang="EN-US"}

[\[Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101\] transmit-priority 4]{lang="EN-US"}
:::

::: {#-529007086 .myid}
[]{#_Toc404785266}[]{#struct_0_19500_x1656_297834370}[]{#_Toc348095188}[]{#_Toc328667732}

**ATM \-- ATM配置命令 \-- vp limit**

------------------------------------------------------------------------

[**[vp limit]{lang="EN-US"}**]{#struct_0_19500_x1656_x2123528438}[命令用来配置]{style="font-family:宋体"}[VP]{lang="EN-US"}[监管的参数。]{style="font-family:宋体"}

[**[undo vp limit]{lang="EN-US"}**]{#struct_0_19500_x1656_1712864179}[命令用来取消]{style="font-family:宋体"}[VP]{lang="EN-US"}[监管。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_737859215}

[**[vp limit]{lang="EN-US"}**[ *vpi* *scr*]{lang="EN-US"}]{#struct_0_19500_x1656_144311321}

[**[undo vp limit]{lang="EN-US"}**[ *vpi*]{lang="EN-US"}]{#struct_0_19500_x1656_838979357}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2013127594}

[[不进行]{style="font-family:宋体"}[VP]{lang="EN-US"}]{#struct_0_19500_x1656_x1499373395}[监管。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1092574571}

[[ATM]{lang="EN-US"}]{#struct_0_19500_x1656_x1124783503}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x2123462902}

[[network-admin]{lang="EN-US"}]{#struct_0_19500_x1656_617979906}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19500_x1656_x1220543226}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19500_x1656_449934769}

[*[vpi]{lang="EN-US"}*]{#struct_0_19500_x1656_x1025198035}[：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[scr]{lang="EN-US"}*]{#struct_0_19500_x1656_x1381650634}[：可承受速率，取值范围请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-9]{lang="EN-US"}](?1437517977#_Ref57606154)[，单位为]{style="font-family:宋体"}[Kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19500_x1656_x442268000}

[[VP]{lang="EN-US"}]{#struct_0_19500_x1656_x767249020}[是具有相同]{style="font-family:宋体"}[VPI]{lang="EN-US"}[的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的集合，]{style="font-family:宋体"}[VP]{lang="EN-US"}[监管用来管理]{style="font-family:宋体"}[VP]{lang="EN-US"}[的最大带宽，对一个物理接口下的虚通道（]{style="font-family:宋体"}[VP]{lang="EN-US"}[）流量进行入方向、出方向的监管，即保证]{style="font-family:宋体"}[VP]{lang="EN-US"}[的最大传输速率不能超过设定值，超出的流量将被丢弃。在应用]{style="font-family:宋体"}[VP]{lang="EN-US"}[监管时，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的参数仍然有效，只有满足]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的参数与]{style="font-family:宋体"}[VP]{lang="EN-US"}[监管的参数时，分组才会被接收或发送。在计算流量时，已经包括了]{style="font-family:宋体"}[LLC/SNAP]{lang="EN-US"}[、]{style="font-family:宋体"}[MUX]{lang="EN-US"}[和]{style="font-family:宋体"}[NLPID]{lang="EN-US"}[封装头部，[]{#_Hlt23222623}但不包括]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元头。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19500_x1656_1920921698}

[[\# ]{lang="EN-US"}]{#struct_0_19500_x1656_x2123397366}[配置]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[VP]{lang="EN-US"}[的流量为]{style="font-family:宋体"}[2Mbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19500_x1656_848895031}

[\[Sysname\] interface atm 2/4/0]{lang="EN-US"}

[\[Sysname-ATM2/4/0\] vp limit 1 2000]{lang="EN-US"}

[]{#_Toc328667733}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19500_x1656_793743905}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service cbr]{lang="EN-US"}**]{#struct_0_19500_x1656_x18142487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service ubr]{lang="EN-US"}**]{#struct_0_19500_x1656_x914548901}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service vbr-nrt]{lang="EN-US"}**]{#struct_0_19500_x1656_x1556187306}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service vbr-rt]{lang="EN-US"}**]{#struct_0_19500_x1656_908926114}
:::
