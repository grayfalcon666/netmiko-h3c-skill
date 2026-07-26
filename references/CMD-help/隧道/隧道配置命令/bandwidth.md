::: {#1742433432 .myid}
[]{#_Toc404787122}[]{#struct_0_11842_x1255_x477268653}

**隧道 \-- 隧道配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_11842_x1255_x285451008}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_11842_x1255_1609349509}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1483509696}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_11842_x1255_x563447994}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_11842_x1255_1522291081}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1652009140}

[[接口的期望带宽＝接口的最大速率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_11842_x1255_x567983}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1862623139}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x587706112}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1924869697}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x837923758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1483575232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x2022071377}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_11842_x1255_x146993956}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1835572501}

[[接口的期望带宽会影响链路开销值。具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_11842_x1255_1875574190}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1708984025}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x1734281936}[设置接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[100kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_x2026132919}

[\[Sysname\] interface tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] bandwidth 100]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc137103150}[]{#_Toc404787123}[]{#struct_0_11842_x1255_1444271892}[]{#_Toc318203182}[]{#_Toc309912009}[]{#_Toc273281609}[]{#_Toc218395051}[]{#_Toc215479534}[]{#_Toc207017822}[]{#_Toc207011361}[]{#_Toc207010293}[]{#_Toc207010026}[]{#_Toc139515317}

**隧道 \-- 隧道配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_11842_x1255_x1483640768}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1915338607}

[**[default]{lang="EN-US"}**]{#struct_0_11842_x1255_x456107101}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1127989705}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_132271148}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1046390802}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1855306759}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1413783171}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1483706304}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_11842_x1255_285969933}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_11842_x1255_x1431615218}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_461194589}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x812823390}[将接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_346715479}

[\[Sysname\] interface tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404787124}[]{#struct_0_11842_x1255_x1242948208}

**隧道 \-- 隧道配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_11842_x1255_1354183057}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_11842_x1255_x1483771840}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_578534015}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_11842_x1255_339895947}

[**[undo description]{lang="EN-US"}**]{#struct_0_11842_x1255_515192216}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1562782154}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"} [Interface]{lang="EN-US"}]{#struct_0_11842_x1255_1857698971}["，如"]{style="font-family:宋体"}[Tunnel1 Interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1847314848}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_183333257}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1613233779}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1483837376}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_4494856}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x280809093}

[*[text]{lang="EN-US"}*]{#struct_0_11842_x1255_x56224456}[：接口的描述字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x2009795833}

[[当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1067935496}

[[本命令仅用于标识某接口，并无特别的功能。使用]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_11842_x1255_x71087908}[等命令可以看到设置的描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_2024538981}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_867028050}[设置]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[接口的描述信息为"]{style="font-family:宋体"}[tunnel1[["]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}]{lang="EN-US"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_x1483902912}

[\[Sysname\] interface tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] description tunnel1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1425431331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x305443009}
:::

::: {#-1511398521 .myid}
[]{#_Toc404787125}[]{#struct_0_11842_x1255_1995865287}[]{#_Toc138149896}[]{#_Toc138149697}[]{#_Toc136937207}[]{#_Toc124673333}[]{#_Toc123629828}

**隧道 \-- 隧道配置命令 \-- destination**

------------------------------------------------------------------------

[**[destination]{lang="EN-US"}**]{#struct_0_11842_x1255_598193534}[命令用来设置隧道的目的端地址。]{style="font-family:宋体"}

[**[undo destination]{lang="EN-US"}**]{#struct_0_11842_x1255_1886956650}[命令用来删除设置的目的端地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1320116102}

[**[destination]{lang="EN-US"}**[ { *ip-address* \| *ipv6-address* }]{lang="EN-US"}]{#struct_0_11842_x1255_x10925429}

[**[undo destination]{lang="EN-US"}**]{#struct_0_11842_x1255_x170802397}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1483968448}

[[没有设置隧道的目的端地址]{style="font-family:宋体"}]{#struct_0_11842_x1255_1571369112}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x915399755}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x1181023618}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x525124729}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_778120810}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x543246127}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x2076814073}

[*[ip-address]{lang="EN-US"}*]{#struct_0_11842_x1255_x1701583782}[：]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[的目的端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_11842_x1255_x1482985408}[：]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[的目的端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1047419433}

[[配置手动隧道时，需要通过本命令设置隧道的目的端地址；配置自动隧道时，无需设置隧道的目的端地址。]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1499112250}

[[隧道的目的端地址是对端接收报文的接口的地址，该地址将作为封装后隧道报文的目的地址。]{style="font-family:宋体"}]{#struct_0_11842_x1255_x295113955}

[[在本端设备上为隧道指定的目的端地址，应该与在对端设备上为该隧道指定的源端地址相同；在本端设备上为隧道指定的源端地址，应该与在对端设备上为该隧道指定的目的端地址相同。]{style="font-family:宋体"}]{#struct_0_11842_x1255_1023133646}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_196841878}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11842_x1255_1131064952}

[[\# Sysname1]{lang="FR"}]{#struct_0_11842_x1255_x852409678}[上接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[的]{style="font-family:宋体"}[IP]{lang="FR"}[地址是]{style="font-family:
宋体"}[193.101.1.1]{lang="FR"}[，]{style="font-family:宋体"}[Sysname2]{lang="FR"}[上接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[的]{style="font-family:宋体"}[IP]{lang="FR"}[地址是]{style="font-family:
宋体"}[192.100.1.1]{lang="FR"}[。配置]{style="font-family:宋体"}[Sysname1]{lang="FR"}[的源端地址为]{style="font-family:宋体"}[193.101.1.1]{lang="FR"}[，目的端地址为]{style="font-family:宋体"}[192.100.1.1]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname1\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_x1483050944}

[\[Sysname1\] interface tunnel 1 mode gre]{lang="EN-US"}

[\[Sysname1-Tunnel1\] source 193.101.1.1]{lang="EN-US"}

[\[Sysname1-Tunnel1\] destination 192.100.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x1884293110}[配置]{style="font-family:宋体"}[Sysname2]{lang="FR"}[的源端地址为]{style="font-family:宋体"}[192.100.1.1]{lang="FR"}[，目的端地址为]{style="font-family:宋体"}[193.101.1.1]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname2\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_x437404003}

[\[Sysname2\] interface tunnel 1 mode gre]{lang="EN-US"}

[\[Sysname2-Tunnel1\] source 192.100.1.1]{lang="FR"}

[\[Sysname2-Tunnel1\] destination 193.101.1.1]{lang="FR"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11842_x1255_x547745753}

[[\# Sysname1]{lang="FR"}]{#struct_0_11842_x1255_1203155874}[上接口]{style="font-family:宋体"}[Vlan-int100]{lang="FR"}[的]{style="font-family:宋体"}[IP]{lang="FR"}[地址是]{style="font-family:
宋体"}[193.101.1.1]{lang="FR"}[，]{style="font-family:宋体"}[Sysname2]{lang="FR"}[上接口]{style="font-family:宋体"}[Vlan-int100]{lang="FR"}[的]{style="font-family:宋体"}[IP]{lang="FR"}[地址是]{style="font-family:
宋体"}[192.100.1.1]{lang="FR"}[。]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[Sysname1]{lang="FR"}[的源端地址为]{style="font-family:宋体"}[193.101.1.1]{lang="FR"}[，目的端地址为]{style="font-family:宋体"}[192.100.1.1]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname1\> system-view]{lang="FR"}]{#struct_0_11842_x1255_x417174827}

[\[Sysname1\] interface tunnel 1 mode ipv6-ipv4]{lang="FR"}

[\[Sysname1-Tunnel1\] source 193.101.1.1]{lang="FR"}

[\[Sysname1-Tunnel1\] destination 192.100.1.1]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_11842_x1255_1622844548}[配置]{style="font-family:宋体"}[Sysname2]{lang="FR"}[的源端地址为]{style="font-family:宋体"}[192.100.1.1]{lang="FR"}[，目的端地址为]{style="font-family:宋体"}[193.101.1.1]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname2\> system-view]{lang="FR"}]{#struct_0_11842_x1255_x1483509699}

[\[Sysname2\] interface tunnel 1 mode ipv6-ipv4]{lang="FR"}

[\[Sysname2-Tunnel1\] source 192.100.1.1]{lang="FR"}

[\[Sysname2-Tunnel1\] destination 193.101.1.1]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1452974641}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_1765560706}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x1922149592}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source]{lang="EN-US"}**]{#struct_0_11842_x1255_389531781}
:::

::: {#-769895972 .myid}
[]{#_Toc404787126}[]{#struct_0_11842_x1255_2037630054}[]{#_Toc333304515}[]{#_Toc329791757}[]{#_Toc329352654}

**隧道 \-- 隧道配置命令 \-- display ds-lite b4 information**

------------------------------------------------------------------------

[**[display ds-lite b4 information]{lang="EN-US"}**]{#struct_0_11842_x1255_2057439457}[命令用来在]{style="font-family:
宋体"}[AFTR]{lang="EN-US"}[端显示已连接的]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备的信息，包括]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址与]{style="font-family:宋体"}[Tunnel ID]{lang="EN-US"}[的映射关系等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1362278066}

[**[display ds-lite b4 information]{lang="EN-US"}**]{#struct_0_11842_x1255_x1483575235}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1513381032}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1437560663}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x250204563}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x700440715}

[[network-operator]{lang="EN-US"}]{#struct_0_11842_x1255_x134814}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_1986081134}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11842_x1255_x407049202}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x827258383}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x1111841402}[显示已连接的]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备的信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display ds-lite b4 information]{lang="EN-US"}]{#struct_0_11842_x1255_x1483640771}

[ B4 address                                     Tunnel ID  Tunnel interface  Idle time ]{lang="EN-US"}

[ 1234:5678:1234:5678:abcd:abcd:efff:1234  0x00000023          1           12]{lang="EN-US"}

[ 2000::100:1                                    0x80000013          2           13]{lang="EN-US"}

[ 3000::2                                         0x00000015          3           8]{lang="EN-US"}

[ 3001::2                                         0x00000032          \--          15]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x705419490}[显示已连接的]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备的信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display ds-lite b4 information]{lang="EN-US"}]{#struct_0_11842_x1255_x315421987}

[Slot 0 Cpu 0:]{lang="EN-US"}

[ B4 address                                     Tunnel ID  Tunnel interface  Idle time ]{lang="EN-US"}

[ 1234:5678:1234:5678:abcd:abcd:efff:1234  0x00000023          1           12]{lang="EN-US"}

[ 2000::100:1                                    0x80000013          2           13]{lang="EN-US"}

[ 3000::2                                         0x00000015          3           2]{lang="EN-US"}

[ 3001::2                                         0x00000032          \--          \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 1 Cpu 0:]{lang="EN-US"}

[ B4 address                                     Tunnel ID  Tunnel interface  Idle time ]{lang="EN-US"}

[ 1234:5678:1234:5678:abcd:abcd:efff:ffff  0x00000125          1           12]{lang="EN-US"}

[ 5000::100:1                                    0x80000010          5           13]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x581018102}[显示已连接的]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display ds-lite b4 information]{lang="EN-US"}]{#struct_0_11842_x1255_x1483706307}

[Chassis 1 Slot 0 Cpu0:]{lang="EN-US"}

[ B4 address                                     Tunnel ID  Tunnel interface  Idle time ]{lang="EN-US"}

[ 1234:5678:1234:5678:abcd:abcd:efff:1234  0x00000023          1           12]{lang="EN-US"}

[ 2000::100:1                                    0x80000013          2           13]{lang="EN-US"}

[ 3000::2                                         0x00000015          3           2]{lang="EN-US"}

[ 3001::2                                         0x00000032          \--          \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 1 Slot 1 Cpu0:]{lang="EN-US"}

[ B4 address                                     Tunnel ID  Tunnel interface  Idle time ]{lang="EN-US"}

[ 1234:5678:1234:5678:abcd:abcd:efff:ffff  0x00000125          1           12]{lang="EN-US"}

[ 5000::100:1                                    0x80000010          5           13]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ds-lite b4 information]{lang="EN-US"}]{#struct_0_11842_x1255_x1280114008}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1226229891}[[字段]{style="font-family:黑体"}]{#struct_0_11842_x1255_776156744}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11842_x1255_x104896005}

[[Slot 0 Cpu0]{lang="EN-US"}]{#struct_0_11842_x1255_919657244}

[[指定单板指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_11842_x1255_x1483771843}[上的信息]{style="font-family:宋体"}

[[Chassis 1 Slot 0 Cpu0]{lang="EN-US"}]{#struct_0_11842_x1255_175249488}

[[指定成员设备指定单板指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_11842_x1255_275665448}[上的信息]{style="font-family:宋体"}

[[B4 address]{lang="EN-US"}]{#struct_0_11842_x1255_x1215674787}

[[B4]{lang="EN-US"}]{#struct_0_11842_x1255_1756857579}[设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_11842_x1255_1526723538}

[[B4]{lang="EN-US"}]{#struct_0_11842_x1255_x1483837379}[设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[Tunnel ID]{lang="EN-US"}

[[Tunnel interface]{lang="EN-US"}]{#struct_0_11842_x1255_x1111250391}

[[映射关系所属的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}]{#struct_0_11842_x1255_x496144192}[隧道接口编号]{style="font-family:宋体"}

[[当映射关系所属的隧道被删除或者删除后创建编号相同但模式不同的隧道时，本字段显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}]{#struct_0_11842_x1255_x86575097}["]{style="font-family:宋体"}

[[Idle time]{lang="EN-US"}]{#struct_0_11842_x1255_846209382}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_11842_x1255_933940004}[与]{style="font-family:宋体"}[B4]{lang="EN-US"}[设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址映射关系的剩余有效时间，单位为分钟]{style="font-family:宋体"}

[[当映射关系老化时间已到，但仍有会话引用该映射关系时，本字段显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}]{#struct_0_11842_x1255_x1483902915}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1547981745 .myid}
[]{#_Toc404787127}[]{#struct_0_11842_x1255_1303452024}

**隧道 \-- 隧道配置命令 \-- display interface tunnel**

------------------------------------------------------------------------

[**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x1006421454}[命令用来显示]{style="font-family:
宋体"}[Tunnel]{lang="EN-US"}[接口的相关信息，包括源端地址、目的端地址、隧道模式等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_2084200783}

[**[display interface]{lang="EN-US"}**[ \[ **tunnel** \[ *number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_11842_x1255_x436494532}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1752567848}

[[任意视图]{style="font-family:宋体"}]{#struct_0_11842_x1255_647164972}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1095566105}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1483968451}

[[network-operator]{lang="EN-US"}]{#struct_0_11842_x1255_x1513810139}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1762539124}

[[mdc-operator]{lang="EN-US"}]{#struct_0_11842_x1255_x2000510057}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1624343907}

[*[number]{lang="EN-US"}*]{#struct_0_11842_x1255_x305425965}[：显示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口编号，取值为已创建的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_11842_x1255_1603549295}[：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_11842_x1255_836476640}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_11842_x1255_612703999}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1482985411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_11842_x1255_x2037759818}**[tunnel]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x1273149299}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_874584844}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_680592194}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface tunnel 1]{lang="EN-US"}]{#struct_0_11842_x1255_x1483050947}

[]{#_Toc42598113}[]{#_Toc138217142}[]{#_Toc138153939}[]{#_Toc85622797}[]{#_Toc81453340}[]{#_Toc74711153}[]{#_Toc72631499}[]{#_Toc66003572}[]{#_Toc60131644}[Tunnel1]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Tunnel1 Interface]{lang="EN-US"}

[Bandwidth: 64kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1476]{lang="EN-US"}

[Internet Address is 10.1.2.1/24 Primary]{lang="EN-US"}

[Tunnel source 2002::1:1 (]{lang="EN-US"}[Vlan-interface10]{lang="EN-US"}[), destination 2001::2:1]{lang="EN-US"}

[Tunnel keepalive enabled, Period(50 s), Retries(3)]{lang="EN-US"}

[Tunnel TOS 0xC8, Tunnel TTL 255]{lang="EN-US"}

[Tunnel protocol/transport GRE/IPv6]{lang="EN-US"}

[    GRE key value is 1]{lang="EN-US"}

[    Checksumming of GRE packets disabled]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display interface tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x318209169}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1232137811}[[字段]{style="font-family:黑体"}]{#struct_0_11842_x1255_1772945970}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_11842_x1255_x61304395}

[[Tunnel1]{lang="EN-US"}]{#struct_0_11842_x1255_x2077133852}

[[接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}]{#struct_0_11842_x1255_x778364076}[的相关信息]{style="font-family:宋体"}

[[Current state]{lang="EN-US"}]{#struct_0_11842_x1255_x1483509698}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x113109300}[接口的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administr]{lang="EN-US"}]{#struct_0_11842_x1255_801833559}[a]{lang="EN-US"}[t]{lang="EN-US"}[ive]{lang="EN-US"}[ly DOWN]{lang="EN-US"}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_11842_x1255_x969638681}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN ( Tunnel-Bundle administratively down )]{lang="EN-US"}]{#struct_0_11842_x1255_612835071}[：表示该接口所属的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口]{style="font-family:宋体"}[已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_11842_x1255_346389686}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_11842_x1255_1314653566}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_155625228}[接口的链路层协议状态。其值由链路层经过参数协商决定，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_11842_x1255_x1483575234}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_11842_x1255_x1215502323}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_11842_x1255_x884715688}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_11842_x1255_x106460132}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x1912409757}[接口的描述信息]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_11842_x1255_x1483640770}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_2023463865}[接口的期望带宽]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_11842_x1255_x1721924174}

[[Tunnel]{lang="NO-BOK"}]{#struct_0_11842_x1255_x34205608}[接口的最大传输单元]{style="font-family:宋体"}

[[Internet Address]{lang="EN-US"}]{#struct_0_11842_x1255_x384936768}

[[Tunnel]{lang="NO-BOK"}]{#struct_0_11842_x1255_x1483706306}[接口的]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址。如果没有为]{style="font-family:宋体"}[Tunnel]{lang="NO-BOK"}[接口配置]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址，则该字段显示为]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}[，表示不能处理]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[报文]{style="font-family:宋体"}

[[Primary]{lang="EN-US"}]{#struct_0_11842_x1255_1448769347}[表示该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Tunnel source]{lang="EN-US"}]{#struct_0_11842_x1255_x72777217}

[[隧道的源端地址和源接口。如果为]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1072567631}[Tunnel]{lang="NO-BOK"}[接口配置的是隧道的源端地址，则该字段只显示源端地址]{style="font-family:宋体"}

[[destination]{lang="EN-US"}]{#struct_0_11842_x1255_1270764983}

[[隧道的目的端地址]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1483771842}

[[Tunnel keepalive enabled, Period(50 s), Retries(3)]{lang="EN-US"}]{#struct_0_11842_x1255_1741333429}

[[启用隧道的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_11842_x1255_x172896421}[功能，本例中]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒，最大发送次数为]{style="font-family:宋体"}[3]{lang="EN-US"}

[[如果没有启用隧道的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_11842_x1255_x1625440601}[功能，则显示为]{style="font-family:宋体"}[Tunnel keepalive disabled]{lang="EN-US"}

[[Tunnel TOS]{lang="EN-US"}]{#struct_0_11842_x1255_x1321765399}

[[封装后隧道报文的]{style="font-family:宋体"}[ToS]{lang="EN-US"}]{#struct_0_11842_x1255_x1483837378}[值]{style="font-family:宋体"}

[[Tunnel TTL]{lang="EN-US"}]{#struct_0_11842_x1255_454833550}

[[封装后隧道报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_11842_x1255_1772343522}[值]{style="font-family:宋体"}

[[Tunnel protocol/transport]{lang="EN-US"}]{#struct_0_11842_x1255_x459298366}

[[隧道模式和传输协议，可能取值为：]{style="font-family:宋体"}]{#struct_0_11842_x1255_474781369}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CR_LSP]{lang="EN-US"}]{#struct_0_11842_x1255_753042382}[：表示]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DSLITE]{lang="EN-US"}]{#struct_0_11842_x1255_1181642569}[：表示]{style="font-family:宋体"}[AFTR]{lang="EN-US"}[端的]{style="font-family:宋体"}[IPv4 over IPv]{lang="DA"}[6 ]{lang="DA"}[DS-Lite]{lang="EN-US"}[隧道模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[GRE/IP]{lang="DA"}]{#struct_0_11842_x1255_x1483902914}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[GRE over IPv4]{lang="DA"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[GRE/IPv6]{lang="DA"}]{#struct_0_11842_x1255_x262631917}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[GRE over IPv6]{lang="DA"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[GRE_ADVPN/IP]{lang="DA"}]{#struct_0_11842_x1255_2127893278}[：表示]{lang="EN-US" style="font-family:宋体"}[GRE]{lang="DA"}[封装的]{lang="EN-US" style="font-family:宋体"}[IPv4 ADVPN]{lang="DA"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[GRE_ADVPN/IPv6]{lang="DA"}]{#struct_0_11842_x1255_x258964433}[：表示]{lang="EN-US" style="font-family:宋体"}[GRE]{lang="DA"}[封装的]{lang="EN-US" style="font-family:宋体"}[IPv6 ADVPN]{lang="DA"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[GRE_EVI/IP]{lang="DA"}]{#struct_0_11842_x1255_x1691185676}[：表示]{style="font-family:
  宋体"}[GRE]{lang="DA"}[封装的]{style="font-family:宋体"}[IPv4 EVI]{lang="DA"}[隧道模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[GRE_EVI/IPv6]{lang="DA"}]{#struct_0_11842_x1255_1962830427}[：表示]{style="font-family:
  宋体"}[GRE]{lang="DA"}[封装的]{style="font-family:宋体"}[IPv6 EVI]{lang="DA"}[隧道模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[IP/IP]{lang="DA"}]{#struct_0_11842_x1255_x2021943776}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[IPv4 over IPv4]{lang="DA"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[IP/IPv6]{lang="DA"}]{#struct_0_11842_x1255_1628290075}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv4 over IPv6]{lang="DA"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="DA"}]{#struct_0_11842_x1255_x1859159655}[：]{lang="EN-US" style="font-family:
  宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="DA"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[IPv6/IP]{lang="DA"}]{#struct_0_11842_x1255_x1483968450}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[IPv6 over IPv4]{lang="DA"}[手]{lang="EN-US" style="font-family:宋体"}[动]{style="font-family:宋体"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6/IP 6to4]{lang="EN-US"}]{#struct_0_11842_x1255_1215073216}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6 over IPv4 6to4]{lang="EN-US"}[隧道模式]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6/IP auto-tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x1579964589}[：表示]{lang="EN-US" style="font-family:
  宋体"}[IPv6 over IPv4]{lang="EN-US"}[自动隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6/IP ISATAP]{lang="EN-US"}]{#struct_0_11842_x1255_804993522}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6 over IPv4 ISATAP]{lang="EN-US"}[隧道模式]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6/IPv6]{lang="EN-US"}]{#struct_0_11842_x1255_128005156}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6 over IPv6]{lang="EN-US"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP_ADVPN/IP]{lang="EN-US"}]{#struct_0_11842_x1255_2127958814}[：表示]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[封装的]{lang="EN-US" style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP_ADVPN/IPv6]{lang="EN-US"}]{#struct_0_11842_x1255_x1874867475}[：表示]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[封装的]{lang="EN-US" style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP_VXLAN/IP]{lang="EN-US"}]{#struct_0_11842_x1255_1532908919}[：表示]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[封装的]{lang="EN-US" style="font-family:宋体"}[IPv4 VXLAN]{lang="EN-US"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NVE/IP]{lang="EN-US"}]{#struct_0_11842_x1255_x1120519420}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv4 NVE]{lang="EN-US"}[隧道模式]{lang="EN-US" style="font-family:宋体"}

[[GRE key value is 1]{lang="EN-US"}]{#struct_0_11842_x1255_x1482985410}

[[GRE]{lang="EN-US"}]{#struct_0_11842_x1255_691123537}[类型隧道接口的密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}

[[如果没有设置]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_11842_x1255_x526105294}[类型隧道接口的密钥，则显示为]{style="font-family:宋体"}[GRE key disabled]{lang="EN-US"}

[[Checksumming of GRE packets disabled]{lang="EN-US"}]{#struct_0_11842_x1255_x1483050946}

[[未使能]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_11842_x1255_1247874772}[报文校验和功能]{style="font-family:宋体"}

[[如果使能了]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_11842_x1255_x1188007833}[报文校验和功能，则显示为]{style="font-family:宋体"}[Checksumming of GRE packets enabled]{lang="EN-US"}

[[Source port number is 18001]{lang="EN-US"}]{#struct_0_11842_x1255_2127762206}

[[UDP]{lang="EN-US"}]{#struct_0_11842_x1255_1326321782}[封装的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[类型隧道接口发送]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[报文使用的源端口号]{style="font-family:宋体"}

[[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}]{#struct_0_11842_x1255_x72449537}

[[输出队列的紧急队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11842_x1255_1441375117}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}]{#struct_0_11842_x1255_x72384001}

[[输出队列的协议队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11842_x1255_x72973826}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}]{#struct_0_11842_x1255_1448584788}

[[输出队列的先进先出队列中当前的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11842_x1255_x72908290}[最大可容纳的消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[已丢弃的消息数。该显示信息与用户的配置有关，当配置为]{style="font-family:宋体"}[CBQ]{lang="EN-US"}[、]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[等队列时则显示为]{style="font-family:宋体"}[CBQ/WFQ]{lang="EN-US"}[等队列的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_11842_x1255_937833247}

[[最近一次清除计数的时间]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1483509701}

[[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_11842_x1255_1808746250}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_11842_x1255_2125335748}[秒钟的平均输入速率：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_11842_x1255_x1483575237}[表示平均每秒输入的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_11842_x1255_x1618786850}[表示平均每秒输入的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_11842_x1255_x1072854167}[表示平均每秒输入的包数]{lang="EN-US" style="font-family:宋体"}

[[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}]{#struct_0_11842_x1255_x1483640773}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_11842_x1255_457379924}[秒钟的平均输出速率：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bytes/sec]{lang="EN-US"}]{#struct_0_11842_x1255_1272973049}[表示平均每秒输出的字节数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bits/sec]{lang="EN-US"}]{#struct_0_11842_x1255_x1536317313}[表示平均每秒输出的比特数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets/sec]{lang="EN-US"}]{#struct_0_11842_x1255_x1483706309}[表示平均每秒输出的包数]{lang="EN-US" style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}]{#struct_0_11842_x1255_x829775314}

[[总计输入的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_11842_x1255_295281579}[总计输入的字节，总计丢弃的输入报文数]{style="font-family:宋体"}

[[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}]{#struct_0_11842_x1255_x1483771845}

[[总计输出的报文数]{style="font-family:宋体"}[, ]{lang="EN-US"}]{#struct_0_11842_x1255_981818542}[总计输出的字节，总计丢弃的输出报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_1507885277}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface tunnel 1 brief]{lang="EN-US"}]{#struct_0_11842_x1255_899901935}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Tun1                  UP    UP       1.1.1.1          aaaaaaaaaaaaaaaaaaaaaaaaaaa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x1483837381}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的概要信息，包括用户配置的全部描述信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface tunnel 1 brief description]{lang="EN-US"}]{#struct_0_11842_x1255_x754692351}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Tun1                  UP    UP       1.1.1.1          aaaaaaaaaaaaaaaaaaaaaaaaaaaaa]{lang="EN-US"}

[Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_895814041}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface tunnel brief down]{lang="EN-US"}]{#struct_0_11842_x1255_1110785720}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Tun0                  DOWN Not connected]{lang="EN-US"}

[Tun1                  DOWN Not connected]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display interface tunnel brief]{lang="EN-US"}]{#struct_0_11842_x1255_1319789207}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1240412022}[[字段]{style="font-size:9.0pt;
   font-family:宋体"}]{#struct_0_11842_x1255_584267009}

[[描述]{style="font-size:9.0pt;font-family:宋体"}]{#struct_0_11842_x1255_x1483902917}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_11842_x1255_x1828715858}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_11842_x1255_x426026454}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_11842_x1255_x712632519}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_11842_x1255_789244329}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_11842_x1255_561111145}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_11842_x1255_1914732385}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_11842_x1255_x1483968453}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["字符串，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_11842_x1255_1618357743}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_11842_x1255_1363835366}

[[Link]{lang="EN-US"}]{#struct_0_11842_x1255_1629526481}

[[接口物理连接状态，取值为：]{style="font-family:宋体"}]{#struct_0_11842_x1255_x993768946}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_11842_x1255_422019436}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_11842_x1255_x1482985413}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_11842_x1255_x874960404}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_11842_x1255_1696072420}[：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_11842_x1255_x994283656}

[[接口数据链路层协议状态，取值为：]{style="font-family:宋体"}]{#struct_0_11842_x1255_642041773}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_11842_x1255_x1483050949}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_11842_x1255_932565589}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_11842_x1255_x768547863}[：表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会取该值]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_11842_x1255_x27715938}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_11842_x1255_x164632447}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_11842_x1255_x1483509700}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_11842_x1255_242662309}

[[Cause]{lang="EN-US"}]{#struct_0_11842_x1255_x720665237}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_11842_x1255_x1464425529}[的原因，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_11842_x1255_x683478934}[：表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not connected]{lang="EN-US"}]{#struct_0_11842_x1255_x1483575236}[：表示未成功建立隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN ( Tunnel-Bundle administratively down )]{lang="EN-US"}]{#struct_0_11842_x1255_x1316098361}[：表示隧道接口所属的]{style="font-family:宋体"}[Tunnel-Bundle]{lang="EN-US"}[接口被手工关闭了]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x52702909}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[destination]{lang="FR"}**]{#struct_0_11842_x1255_x944367137}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[interface tunnel]{lang="FR"}**]{#struct_0_11842_x1255_1286392297}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[source]{lang="FR"}**]{#struct_0_11842_x1255_1869778520}

::: {#-2007708668 .myid}
[]{#_Toc404787128}[]{#struct_0_11842_x1255_2119347861}[]{#_Toc333304542}[]{#_Toc329791755}[]{#_Toc329352652}

**隧道 \-- 隧道配置命令 \-- ds-lite enable**

------------------------------------------------------------------------

[**[ds-lite enable]{lang="EN-US"}**]{#struct_0_11842_x1255_x1606128486}[命令用来使能接口的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[隧道功能。]{style="font-family:宋体"}

[**[undo ds-lite enable]{lang="EN-US"}**]{#struct_0_11842_x1255_1352724923}[命令用来关闭接口的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}[隧道功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1411558842}

[**[ds-lite enable]{lang="EN-US"}**]{#struct_0_11842_x1255_x1483640772}

[**[undo ds-lite enable]{lang="EN-US"}**]{#struct_0_11842_x1255_x1108704017}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x534617941}

[[接口的]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}]{#struct_0_11842_x1255_1722647815}[隧道功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1169572093}

[[接口视图]{style="font-family:宋体"}]{#struct_0_11842_x1255_897493178}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_730192660}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_659027075}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x278185240}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1483706308}

[[在]{style="font-family:宋体"}]{#struct_0_11842_x1255_1899108041}[AFTR]{lang="SV"}[连接]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[公网的接口上需要通过本命令使能]{style="font-family:宋体"}[DS-Lite]{lang="SV"}[隧道功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}[只有使能该功能后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[AFTR]{lang="SV"}[从公网接口接收到的]{style="font-family:宋体"}[IPv4]{lang="SV"}[报文才能够通过]{style="font-family:宋体"}[DS-Lite]{lang="SV"}[隧道正确地转发到]{style="font-family:宋体"}[B4]{lang="SV"}[设备。]{style="font-family:宋体"}

[[不能在]{style="font-family:宋体"}]{#struct_0_11842_x1255_1342354362}**[ds-lite-aftr]{lang="SV"}**[模式的隧道接口上使能]{style="font-family:宋体"}[DS-Lite]{lang="SV"}[隧道功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x797281909}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11842_x1255_740733159}

[[\# ]{lang="SV"}]{#struct_0_11842_x1255_376667815}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上使能]{style="font-family:宋体"}[DS-Lite]{lang="SV"}[隧道功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_737060536}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ds-lite enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11842_x1255_1108899882}

[[\# ]{lang="SV"}]{#struct_0_11842_x1255_942160989}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="SV"}[上使能]{style="font-family:宋体"}[DS-Lite]{lang="SV"}[隧道功能。]{style="font-family:宋体"}

[[\<Sysname1\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_x1483771844}

[\[Sysname1\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname1-Vlan-interface10\] ds-lite enable]{lang="EN-US"}
:::

::::: {#-1071457417 .myid}
[]{#_Toc404787129}[]{#struct_0_11842_x1255_x1747064813}[]{#_Toc280023071}[]{#_Toc303083797}[]{#_Toc303083798}[]{#_Toc303083799}[]{#_Toc303083800}[]{#_Toc303083801}[]{#_Toc303083802}[]{#_Toc303083803}[]{#_Toc303083804}[]{#_Toc303083805}[]{#_Toc303083806}[]{#_Toc303083807}[]{#_Toc303083808}[]{#_Toc303083809}[]{#_Toc303083810}[]{#_Toc303083811}[]{#_Toc303083853}[]{#_Toc303083854}[]{#_Toc303083977}[]{#_Toc303083978}[]{#_Toc303083983}[]{#_Toc303083984}[]{#_Toc303084011}

**隧道 \-- 隧道配置命令 \-- encapsulation-limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](隧道命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_11842_x1255_x1823258398}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11842_x1255_x1018810500}
:::

[ ]{lang="EN-US"}

[**[encapsulation-limit]{lang="EN-US"}**]{#struct_0_11842_x1255_x1882141235}[命令用来设置隧道允许的最大嵌套封装次数。]{style="font-family:宋体"}

[**[undo encapsulation-limit]{lang="EN-US"}**]{#struct_0_11842_x1255_x1247017228}[用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1336489809}

[**[encapsulation-limit]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_11842_x1255_1303266516}

[**[undo encapsulation-limit]{lang="EN-US"}**]{#struct_0_11842_x1255_x1483837380}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_811391590}

[[不限制隧道的最大嵌套封装次数。]{style="font-family:宋体"}]{#struct_0_11842_x1255_1618902438}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x195224888}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_927594471}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x2084428187}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_620299063}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x821033207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_432954949}

[*[number]{lang="EN-US"}*]{#struct_0_11842_x1255_x1483902916}[：]{style="font-family:宋体"}[隧道的最大嵌套封装次数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_900167497}

[[对报文进行过多次的封装，在报文上增加过多的报文头，会造成报文过大。如果报文的大小超过了]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_11842_x1255_x1317792843}[值，则需要对报文进行分片处理，这会降低报文的转发速度，增加报文处理的复杂度。通过本命令可以限制报文被封装的次数，避免上述情况发生。]{style="font-family:宋体"}

[[本命令只用于]{style="font-family:宋体"}[IPv6 over IPv6]{lang="EN-US"}]{#struct_0_11842_x1255_1061992155}[隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1803797536}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_1887175328}[设置隧道允许的最大嵌套封装次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_2125053528}

[\[Sysname\] interface tunnel 1 mode ipv6]{lang="EN-US"}

[\[Sysname-Tunnel1\] encapsulation-limit 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1709734606}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x409528012}
:::::

::: {#1037677792 .myid}
[]{#_Toc404787130}[]{#struct_0_11842_x1255_x1483968452}[]{#_Toc296524900}[]{#_Toc296525605}

**隧道 \-- 隧道配置命令 \-- interface tunnel**

------------------------------------------------------------------------

[**[interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_52273802}[命令用来创建一个]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口，]{style="font-family:宋体"}[指定隧道模式，]{style="font-family:宋体"}[并进入该]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[**[undo interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x30071902}[命令用来删除指定的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x2113139974}

[**[interface tunnel]{lang="EN-US"}***[ number ]{lang="EN-US"}*[\[ **mode** { **advpn** { **gre** \| **udp** } \[ **ipv6** \] \| **ds-lite-aftr** \| **evi** \[ **ipv6** \] \| **gre** \[ **ipv6** \] \| **ipv4-ipv4** \| **ipv4-ipv6** \| **ipv6** \| **ipv6-ipv4** \[ **6to4** \| **auto-tunnel** \| **isatap** \] \| **ipv6-ipv6** \| **mpls-te** \| **nve** \| **nvgre** \| **vxlan** } \]]{lang="EN-US"}]{#struct_0_11842_x1255_x1918269423}

[**[undo interface tunnel]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_11842_x1255_1566179517}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_103359342}

[[设备上不存在任何]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_708282641}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1627764695}

[[系统视图]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1482985412}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1853922951}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_1000880825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x2091900188}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x871808279}

[*[number]{lang="EN-US"}*]{#struct_0_11842_x1255_1217551912}[：]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但实际可创建的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[数目将受到接口总数及内存状况的限制。]{style="font-family:宋体"}

[**[mode advpn gre]{lang="EN-US"}**]{#struct_0_11842_x1255_2127762203}[：指定隧道模式为]{style="font-family:宋体"}[GRE]{lang="EN-US"}[封装的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode advpn udp]{lang="EN-US"}**]{#struct_0_11842_x1255_1326125174}[：指定隧道模式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[封装的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode advpn gre ipv6]{lang="EN-US"}**]{#struct_0_11842_x1255_x1934567949}[：指定隧道模式为]{style="font-family:宋体"}[GRE]{lang="EN-US"}[封装的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode advpn udp ipv6]{lang="EN-US"}**]{#struct_0_11842_x1255_x352207898}[：指定隧道模式为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[封装的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **ds-lite-aftr**]{lang="EN-US"}]{#struct_0_11842_x1255_x1345875992}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[AFTR]{lang="FR"}[端的]{style="font-family:宋体"}[DS-Lite]{lang="FR"}[隧道。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **evi**]{lang="EN-US"}]{#struct_0_11842_x1255_x1078088237}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[IPv4 EVI]{lang="EN-US"}[隧道。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **evi ipv6**]{lang="EN-US"}]{#struct_0_11842_x1255_230755461}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[IPv6 EVI]{lang="EN-US"}[隧道。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **gre**]{lang="EN-US"}]{#struct_0_11842_x1255_x1483050948}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[GRE over IPv4]{lang="EN-US"}[隧道。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **gre ipv6**]{lang="EN-US"}]{#struct_0_11842_x1255_797536078}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[GRE over IPv6]{lang="EN-US"}[隧道]{style="font-family:宋体"}[。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **ipv4-ipv4**]{lang="EN-US"}]{#struct_0_11842_x1255_323951400}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[IPv4 over IPv4]{lang="EN-US"}[隧道]{style="font-family:宋体"}[。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode ipv4 over ipv6]{lang="EN-US"}**]{#struct_0_11842_x1255_1628224539}[：指定隧道模式为]{style="font-family:宋体"}[IPv4 over IPv6]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **ipv6**]{lang="EN-US"}]{#struct_0_11842_x1255_192297618}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[隧道。配置]{style="font-family:宋体"}[IPv4 over IPv6]{lang="EN-US"}[手动]{style="font-family:宋体"}[隧道、]{style="font-family:宋体"}[IPv6 over IPv6]{lang="EN-US"}[隧道时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[需要将隧道模式指定为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[隧道。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **ipv6-ipv4**]{lang="EN-US"}]{#struct_0_11842_x1255_898189707}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[IPv6 over IPv4]{lang="EN-US"}[手动]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode ipv6-ipv4 6to4]{lang="EN-US"}**]{#struct_0_11842_x1255_x1601507369}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[6to4]{lang="EN-US"}[隧道]{style="font-family:宋体"}[。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode ipv6-ipv4 auto-tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x697192258}[：]{style="font-family:
宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:
宋体"}[模式为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[兼容]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[自动隧道。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode ipv6-ipv4 isatap]{lang="EN-US"}**]{#struct_0_11842_x1255_x1386005402}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[ISATAP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode ipv6 over ipv6]{lang="EN-US"}**]{#struct_0_11842_x1255_x744428456}[：指定隧道模式为]{style="font-family:宋体"}[IPv6 over IPv6]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**[ **mpls-te**]{lang="EN-US"}]{#struct_0_11842_x1255_x459956384}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[模式为]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode nve]{lang="EN-US"}**]{#struct_0_11842_x1255_x1481908939}[：指定隧道模式为]{style="font-family:宋体"}[NVE]{lang="EN-US"}[（]{style="font-family:宋体"}[Network Virtualization Endpoint]{lang="EN-US"}[，网络虚拟端点）隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode nvgre]{lang="EN-US"}**]{#struct_0_11842_x1255_2041786147}[：指定隧道模式为]{style="font-family:宋体"}[NVGRE]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode vxlan]{lang="EN-US"}**]{#struct_0_11842_x1255_2127827739}[：指定隧道模式为]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_82574244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令创建]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1715715155}[Tunnel]{lang="EN-US"}[接口时，必须携带]{style="font-family:宋体"}**[mode]{lang="EN-US"}**[关键字，指定隧道模式。通过本命令进入已经创建的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图时，不需要携带]{style="font-family:宋体"}**[mode]{lang="EN-US"}**[关键字。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_868306888}[接口编号只具有本地意义，隧道两端可以使用相同或不同的接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_756608042}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x340116925}[创建接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[，指定隧道模式为]{style="font-family:宋体"}[GRE over IPv4]{lang="EN-US"}[隧道，并进入]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_146560295}

[\[Sysname\] interface tunnel 1 mode gre]{lang="EN-US"}

[\[Sysname-Tunnel1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1228291259}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[destination]{lang="EN-US"}**]{#struct_0_11842_x1255_x1536251712}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x842486548}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source]{lang="EN-US"}**]{#struct_0_11842_x1255_82508708}
:::

::: {#988247972 .myid}
[]{#_Toc404787131}[]{#struct_0_11842_x1255_x1742334427}[]{#_Toc205783682}

**隧道 \-- 隧道配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_11842_x1255_587572116}[命令用来设置]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_11842_x1255_952807437}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x283214078}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_11842_x1255_945886893}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_11842_x1255_1240262778}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1227793693}

[[隧道接口的状态始终为]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_11842_x1255_x1521686930}[时，本命令的缺省情况与设备的型号有关，请以设备的实际情况为准；隧道接口的状态当前为]{style="font-family:宋体"}[Up]{lang="EN-US"}[时，隧道的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为根据隧道目的地址查找路由而得到的出接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值减隧道封装报文头长度。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_82443172}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x2123108900}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1083025110}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_1477099128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_65805206}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_444425931}

[*[size]{lang="EN-US"}*]{#struct_0_11842_x1255_x105887607}[：]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[64000]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_55333328}

[[如果没有手工配置隧道的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_11842_x1255_x1136307760}[，则只有在隧道接口状态为]{style="font-family:宋体"}[Up]{lang="EN-US"}[时才会根据出接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[计算、更新隧道的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[，而在]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态不会计算、更新。隧道的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[被手工配置后，其值不受隧道接口状态和出接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[的影响，以手工配置为准。]{style="font-family:宋体"}

[[为了防止隧道封装后的报文二次分片，手工配置隧道的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_11842_x1255_x86464655}[时，建议隧道的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[与封装报文头长度之和不大于出接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1290948535}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_83800749}[设置接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[10000]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_82377636}

[\[Sysname\] interface tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] mtu 10000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1056474433}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x1035024704}
:::

::: {#2052875588 .myid}
[]{#_Toc404787132}[]{#struct_0_11842_x1255_2040619245}[]{#_Toc139515326}[]{#_Toc273281618}[]{#_Toc218395061}[]{#_Toc215479543}[]{#_Toc213490054}[]{#_Toc207010309}[]{#_Toc207010042}

**隧道 \-- 隧道配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_11842_x1255_1590448398}[命令用来清除]{style="font-family:
宋体"}[Tunnel]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_130724697}

[**[reset counters interface]{lang="EN-US"}**[ \[ **tunnel** \[ *number* \] \]]{lang="EN-US"}]{#struct_0_11842_x1255_1048382819}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_641030852}

[[用户视图]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1894872105}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_82312100}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_853476905}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1846321446}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x208144703}

[*[number]{lang="EN-US"}*]{#struct_0_11842_x1255_x73088181}[：]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x110924164}

[[如果需要统计一定时间内]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_922068328}[接口的流量来判断接口和链路工作是否正常，可以使用该命令先清除接口原有的统计信息，然后让接口自动重新统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x1776570609}[和]{lang="EN-US" style="font-family:宋体"}*[number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_585702633}[而不指定]{lang="EN-US" style="font-family:宋体"}*[number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_82246564}[和]{lang="EN-US" style="font-family:宋体"}*[number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1097319500}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_493145454}[清除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface tunnel 1]{lang="EN-US"}]{#struct_0_11842_x1255_404237876}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1456264070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x1609542936}
:::

::::: {#-780779607 .myid}
[]{#_Toc404787133}[]{#struct_0_11842_x1255_1849078335}[]{#_Toc303865071}[]{#_Toc215545670}[]{#_Toc215479545}

**隧道 \-- 隧道配置命令 \-- service**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](隧道命令.files/image002.png){#图片 7 width="63" height="25"}]{lang="EN-US"}]{#struct_0_11842_x1255_x34019153}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11842_x1255_x1477343899}
:::

[ ]{lang="EN-US"}

[**[service]{lang="EN-US"}**]{#struct_0_11842_x1255_1849143871}[命令用来指定转发当前接口流量的业务处理板。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_11842_x1255_364629791}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x703466485}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_11842_x1255_1776343711}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[service slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_11842_x1255_1849209407}

[**[undo service slot]{lang="EN-US"}**]{#struct_0_11842_x1255_x403677813}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_11842_x1255_x1709551756}[模式：]{style="font-family:宋体"}

[**[service ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_11842_x1255_603412159}

[**[undo service ]{lang="EN-US"}[chassis]{lang="EN-US"}**]{#struct_0_11842_x1255_1849274943}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1568706128}

[[没有指定转发当前接口流量的业务处理板。]{style="font-family:宋体"}]{#struct_0_11842_x1255_545428704}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1498815474}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_1849864767}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_808087656}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_436632379}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_1849930303}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x383565137}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11842_x1255_1133415377}[：指定单板所在的槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11842_x1255_2126630285}[：指定设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_11842_x1255_x1860173703}[：指定成员编号或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[虚拟槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11842_x1255_1849340478}[：指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_11842_x1255_x919313573}[：指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_799032312}

[[没有通过]{style="font-family:宋体"}**[service]{lang="EN-US"}**]{#struct_0_11842_x1255_2052841715}[命令指定转发当前接口流量的业务处理板时，直接在接收报文的单板]{style="font-family:宋体"}[/]{lang="EN-US"}[成员设备上进行业务处理。而某些业务（如]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[抗重放检测）要求同一个]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的流量必须在同一个单板]{style="font-family:宋体"}[/]{lang="EN-US"}[成员设备上进行处理，此时可以在]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下通过]{style="font-family:宋体"}**[service]{lang="EN-US"}**[命令指定转发当前接口流量的业务处理板。]{style="font-family:宋体"}

[[需要注意的是，如果拔出指定的转发流量业务板，即使隧道]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_11842_x1255_1849406014}[，流量也转发不通；如果重新插入指定的转发流量业务板，则流量可以恢复在指定板正常转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1917352017}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x1741370671}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板转发]{style="font-family:宋体"}[Tunnel 200]{lang="EN-US"}[的流量。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_1849471550}

[\[Sysname\] interface tunnel 200]{lang="EN-US"}

[\[Sysname-Tunnel200\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_1191819240}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备转发]{style="font-family:宋体"}[Tunnel 200]{lang="EN-US"}[的流量。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_1177828918}

[\[Sysname\] interface tunnel 200]{lang="EN-US"}

[\[Sysname-Tunnel200\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_1224874476}[指定虚拟槽位为]{style="font-family:宋体"}[120]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备转发]{style="font-family:宋体"}[Tunnel 200]{lang="EN-US"}[的流量。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_x2001837967}

[\[Sysname\] interface tunnel 200]{lang="EN-US"}

[\[Sysname-Tunnel200\] service slot 120]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_1849537086}[指定]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板转发]{style="font-family:宋体"}[Tunnel 200]{lang="EN-US"}[的流量。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_11842_x1255_813431860}

[\[Sysname\] interface tunnel 200]{lang="IT"}

[\[Sysname-Tunnel200\] service ]{lang="IT"}[chassis]{lang="EN-US"}[ ]{lang="EN-US"}[2 slot 2]{lang="IT"}

[[\# ]{lang="IT"}]{#struct_0_11842_x1255_x1504008879}[指定]{style="font-family:宋体"}[虚拟框为]{style="font-family:宋体"}[20]{lang="EN-US"}[槽位为]{style="font-family:宋体"}[120]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备转发]{style="font-family:宋体"}[Tunnel 200]{lang="EN-US"}[的流量。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_1690473573}

[\[Sysname\] interface tunnel 200]{lang="EN-US"}

[\[Sysname-Tunnel200\] service chassis 20 slot 120]{lang="EN-US"}
:::::

::: {#1170655049 .myid}
[]{#_Toc404787134}[]{#struct_0_11842_x1255_x2066600083}[]{#_Toc137103160}[]{#_Toc296524904}[]{#_Toc296525609}

**隧道 \-- 隧道配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_11842_x1255_422682325}[命令用来关闭]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_11842_x1255_x186942653}[命令用来打开]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_82181028}

[**[shutdown]{lang="EN-US"}**]{#struct_0_11842_x1255_2119699706}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_11842_x1255_1912219939}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x248891999}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1863219596}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_214742803}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_624876724}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1000743361}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_743262465}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_2038048766}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_82115492}

[[执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**]{#struct_0_11842_x1255_x854841751}[命令会导致使用该接口建立的链路中断，请谨慎使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1210351213}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_1788776622}[关闭接口]{style="font-family:宋体"}[Tunnel 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_x1524080572}

[\[Sysname\] interface tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_476173663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_1850014414}
:::

::: {#-773629 .myid}
[]{#_Toc59352378}[]{#_Toc404787135}[]{#struct_0_11842_x1255_1900106404}[]{#_Toc138149905}[]{#_Toc138149706}[]{#_Toc136937217}[]{#_Toc124673340}[]{#_Toc123629830}[]{#_Toc296524906}[]{#_Toc296525611}[]{#_Toc156191643}[]{#_Toc57621079}[]{#_Toc57628421}[]{#_Toc57629567}[]{#_Toc156191644}[]{#_Toc156191645}[]{#_Toc57621082}[]{#_Toc57628424}[]{#_Toc57629570}[]{#_Toc156191647}[]{#_Toc156191648}[]{#_Toc57621084}[]{#_Toc57628426}[]{#_Toc57629572}[]{#_Toc156191649}[]{#_Toc156191650}[]{#_Toc57621089}[]{#_Toc57628431}[]{#_Toc57629577}[]{#_Toc156191651}[]{#_Toc156191652}[]{#_Toc156191653}[]{#_Toc57621099}[]{#_Toc57628441}[]{#_Toc57629587}[]{#_Toc156191654}[]{#_Toc156191655}[]{#_Toc156191656}[]{#_Toc156191662}[]{#_Toc156191663}[]{#_Toc156191664}[]{#_Toc156191665}[]{#_Toc156191666}[]{#_Toc156191667}[]{#_Toc156191668}[]{#_Toc156191669}[]{#_Toc156191670}[]{#_Toc156191671}[]{#_Toc156191672}[]{#_Toc156191673}[]{#_Toc156191674}[]{#_Toc156191675}[]{#_Toc156191676}[]{#_Toc156191677}[]{#_Toc156191678}[]{#_Toc156191682}[]{#_Toc156191684}[]{#_Toc156191685}[]{#_Toc156191686}[]{#_Toc156191687}[]{#_Toc156191688}[]{#_Toc156191689}[]{#_Toc156191690}[]{#_Toc156191691}[]{#_Toc156191692}[]{#_Toc156191693}[]{#_Toc156191694}[]{#_Toc156191695}[]{#_Toc156191696}[]{#_Toc156191697}[]{#_Toc156191698}[]{#_Toc156191699}[]{#_Toc156191700}[]{#_Toc156191701}[]{#_Toc156191702}[]{#_Toc156191703}[]{#_Toc156191704}[]{#_Toc156191705}[]{#_Toc156191706}[]{#_Toc156191707}[]{#_Toc156191708}[]{#_Toc156191709}

**隧道 \-- 隧道配置命令 \-- source**

------------------------------------------------------------------------

[**[source]{lang="EN-US"}**]{#struct_0_11842_x1255_83098532}[命令用来设置隧道的源端地址或源接口。]{style="font-family:宋体"}

[**[undo source]{lang="EN-US"}**]{#struct_0_11842_x1255_x1119510429}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_405993105}

[**[source]{lang="EN-US"}**[ { *ip-address* \| *ipv6-address* \| *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_11842_x1255_x354903515}

[**[undo source]{lang="EN-US"}**]{#struct_0_11842_x1255_x411134690}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1101028225}

[[没有设置隧道的源端地址和源接口。]{style="font-family:宋体"}]{#struct_0_11842_x1255_1456683234}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1473496827}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x1676939225}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_83032996}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x734908821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x799307823}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_528652924}

[*[ip-address]{lang="EN-US"}*]{#struct_0_11842_x1255_1130575514}[：]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[的源端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_11842_x1255_1069927794}[：]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[的源端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_11842_x1255_x9731349}[：隧道]{style="font-family:宋体"}[的]{style="font-family:宋体"}[源接口的接口类型及接口编号。]{style="font-family:宋体"}

[]{#struct_0_11842_x1255_x972622293}[]{#_Hlt19451604}[【使用指导】]{style="font-family:黑体"}

[[如果设置的是隧道的源端地址，则该地址将作为封装后隧道报文的源地址；如果设置的是]{style="font-family:宋体"}]{#struct_0_11842_x1255_2014637054}[隧道的源接口，则该接口的地址]{style="font-family:宋体"}[将作为封装后隧道报文的源地址。通过]{style="font-family:宋体"}**[display interface tunnel]{lang="EN-US"}**[命令可以查看隧道的源端地址。]{style="font-family:宋体"}

[[在本端设备上为隧道指定的目的端地址，应该与在对端设备上为该隧道指定的源端地址相同；在本端设备上为隧道指定的源端地址，应该与在对端设备上为该隧道指定的目的端地址相同。]{style="font-family:宋体"}]{#struct_0_11842_x1255_82574245}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_11842_x1255_240599981}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在同一个隧道接口下重复执行本命令指定源端地址或源接口，则新的配置会覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_11842_x1255_2026123154}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定的源接口需要是处于]{style="font-family:宋体"}]{#struct_0_11842_x1255_1906869450}[up]{lang="EN-US"}[状态、且已配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[模式为]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11842_x1255_94059608}[AFTR]{lang="FR"}[端]{lang="EN-US" style="font-family:宋体"}[DS-Lite]{lang="FR"}[隧道]{lang="EN-US" style="font-family:宋体"}[的隧道接口不能指定为源接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1166207714}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11842_x1255_x89044576}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_296059900}[配置接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的源接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_1284183857}

[\[Sysname\] interface tunnel 1 mode gre]{lang="EN-US"}

[\[Sysname-Tunnel1\] source gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_82508709}[配置接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.100.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_596317733}

[\[Sysname\] interface tunnel 1 mode gre]{lang="EN-US"}

[\[Sysname-Tunnel1\] source 192.100.1.1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11842_x1255_x856984859}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_1949376639}[配置接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的源接口为]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_1784449114}

[\[Sysname\] interface tunnel 1 mode gre]{lang="FR"}

[\[Sysname-Tunnel1\] source vlan-interface 10]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_11842_x1255_x1980676431}[配置接口]{style="font-family:宋体"}[Tunnel1]{lang="FR"}[的源]{style="font-family:宋体"}[IP]{lang="FR"}[地址为]{style="font-family:
宋体"}[192.100.1.1]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_11842_x1255_741380494}

[\[Sysname\] interface tunnel 1 mode gre]{lang="FR"}

[\[Sysname-Tunnel1\] source 192.100.1.1]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_82443173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[destination]{lang="EN-US"}**]{#struct_0_11842_x1255_215543260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_1286877150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_303420478}
:::

::: {#-517191464 .myid}
[]{#_Toc215545671}[]{#_Toc215479546}[]{#_Toc205783685}[]{#_Toc138149906}[]{#_Toc138149707}[]{#_Toc136937218}[]{#_Toc404787136}[]{#struct_0_11842_x1255_1403992563}[]{#_Toc344454801}[]{#_Toc345061236}[]{#_Toc344454802}[]{#_Toc345061237}[]{#_Toc344454803}[]{#_Toc345061238}[]{#_Toc344454804}[]{#_Toc345061239}[]{#_Toc344454805}[]{#_Toc345061240}[]{#_Toc344454806}[]{#_Toc345061241}[]{#_Toc344454807}[]{#_Toc345061242}[]{#_Toc344454808}[]{#_Toc345061243}[]{#_Toc344454809}[]{#_Toc345061244}[]{#_Toc344454810}[]{#_Toc345061245}[]{#_Toc344454811}[]{#_Toc345061246}[]{#_Toc344454812}[]{#_Toc345061247}[]{#_Toc344454813}[]{#_Toc345061248}[]{#_Toc344454814}[]{#_Toc345061249}[]{#_Toc344454815}[]{#_Toc345061250}[]{#_Toc344454816}[]{#_Toc345061251}[]{#_Toc344454817}[]{#_Toc345061252}[]{#_Toc344454818}[]{#_Toc345061253}[]{#_Toc344454819}[]{#_Toc345061254}[]{#_Toc344454820}[]{#_Toc345061255}[]{#_Toc344454821}[]{#_Toc345061256}[]{#_Toc344454822}[]{#_Toc345061257}[]{#_Toc344454823}[]{#_Toc345061258}[]{#_Toc344454824}[]{#_Toc345061259}[]{#_Toc296524909}[]{#_Toc296525614}[]{#_Toc288212396}[]{#_Toc288220143}

**隧道 \-- 隧道配置命令 \-- tunnel dfbit enable**

------------------------------------------------------------------------

[**[tunnel dfbit enable]{lang="EN-US"}**]{#struct_0_11842_x1255_1759918479}[命令用来]{style="font-family:宋体"}[设置封装后的隧道报文的]{style="font-family:宋体"}[DF]{lang="EN-US"}[（]{style="font-family:宋体"}[Don't Fragment]{lang="EN-US"}[，不分片）标志，即转发隧道报文时不允许分片。]{style="font-family:宋体"}

[**[undo tunnel dfbit enable]{lang="EN-US"}**]{#struct_0_11842_x1255_1326958790}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x827730022}

[**[tunnel dfbit enable]{lang="EN-US"}**]{#struct_0_11842_x1255_1256915325}

[**[undo]{lang="EN-US"}**[ **tunnel dfbit enable**]{lang="EN-US"}]{#struct_0_11842_x1255_82377637}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_899840703}

[[封装后的隧道报文未设置]{style="font-family:宋体"}[DF]{lang="EN-US"}]{#struct_0_11842_x1255_x858069396}[标志，即转发隧道报文时允许分片。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1663377881}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x364870621}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x829152822}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_248113673}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_943805379}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1225369413}

[[转发报文时对报文进行分片、重组，可能会导致报文的转发延时较大。通过本命令]{style="font-family:宋体"}]{#struct_0_11842_x1255_x100643465}[设置封装后隧道报文的]{style="font-family:宋体"}[DF]{lang="EN-US"}[标志，不允许对隧道报文进行分片，可以避免引入分片延时。这种情况下，要求隧道报文转发路径上各个接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大于隧道报文长度，否则，会导致隧道报文被丢弃。如果无法保证转发路径上各个接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大于隧道报文长度，则建议不要]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[DF]{lang="EN-US"}[标志。]{style="font-family:宋体"}

[[模式为]{style="font-family:宋体"}[GRE over IPv6]{lang="EN-US"}]{#struct_0_11842_x1255_82312101}[隧道和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口不支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1485175255}

[[\# ]{lang="DA"}]{#struct_0_11842_x1255_1522162918}[在接口]{style="font-family:宋体"}[Tunnel1]{lang="DA"}[上]{style="font-family:宋体"}[设置封装后隧道报文的]{style="font-family:宋体"}[DF]{lang="DA"}[标志，不允许对隧道报文进行分片]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_11842_x1255_929307893}

[\[Sysname\] interface tunnel 1 mode gre]{lang="IT"}

[\[Sysname-Tunnel1\] tunnel dfbit enable]{lang="IT"}
:::

::::: {#1068442964 .myid}
[]{#_Toc404787137}[]{#struct_0_11842_x1255_x7745186}[]{#_Toc280023074}

**隧道 \-- 隧道配置命令 \-- tunnel discard ipv4-compatible-packet**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](隧道命令.files/image003.png){#图片 3 width="57" height="23"}]{lang="EN-US"}]{#struct_0_11842_x1255_51347179}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11842_x1255_1815455504}
:::

[ ]{lang="EN-US"}

[**[tunnel discard ipv4-compatible-packet]{lang="EN-US"}**]{#struct_0_11842_x1255_82246565}[命令用来配置丢弃含有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[兼容]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文。]{style="font-family:宋体"}**[undo tunnel discard ipv4-compatible-packet]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1241332660}

[**[tunnel discard ipv4-compatible-packet]{lang="EN-US"}**]{#struct_0_11842_x1255_x2011669823}

[**[undo tunnel discard ipv4-compatible-packet]{lang="EN-US"}**]{#struct_0_11842_x1255_1110003757}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_2143856471}

[[不会丢弃含有]{style="font-family:宋体"}]{#struct_0_11842_x1255_1288075954}[IPv4]{lang="EN-US"}[兼容]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x701055364}

[[系统]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1609418878}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_853234949}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_1411866442}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_82181029}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_163384570}

[[执行]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1610560245}**[tunnel discard ipv4-compatible-packet]{lang="EN-US"}**[命令后，对于从隧道接收的报文，如果解封装后原始]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的源或目的地址为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[兼容]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，则丢弃该报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_550310310}

[[\# ]{lang="IT"}]{#struct_0_11842_x1255_x764633557}[配置丢弃含有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[兼容]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_1194819419}

[\[Sysname\] tunnel discard ipv4-compatible-packet]{lang="EN-US"}
:::::

::::: {#1980622970 .myid}
[]{#_Toc404787138}[]{#struct_0_11842_x1255_x341209465}

**隧道 \-- 隧道配置命令 \-- tunnel ipv6-fragmentation-check enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](隧道命令.files/image004.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_11842_x1255_868644116}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_11842_x1255_x1132985041}
:::

[ ]{lang="EN-US"}

[**[tunnel ipv6-fragmentation-check enable]{lang="EN-US"}**]{#struct_0_11842_x1255_1223842559}[命令用来使能隧道报文的分片检查功能。]{style="font-family:宋体"}

[**[undo tunnel ipv6-fragmentation-check enable]{lang="EN-US"}**]{#struct_0_11842_x1255_x338093039}[命令用来关闭隧道报文的分片检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x63154613}

[**[tunnel ipv6-fragmentation-check enable]{lang="EN-US"}**]{#struct_0_11842_x1255_1630992702}

[**[undo tunnel ipv6-fragmentation-check enable]{lang="EN-US"}**]{#struct_0_11842_x1255_x1909916375}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x323374984}

[[隧道报文的分片检查功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_11842_x1255_x2028917101}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1190019692}

[[系统视图]{style="font-family:宋体"}]{#struct_0_11842_x1255_x1135395023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x58885561}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1860239239}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_901007558}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1915256966}

[[执行本命令后，对于将要通过]{style="font-family:宋体"}[IPv6 over IPv4]{lang="EN-US"}]{#struct_0_11842_x1255_x346100065}[隧道转发的报文，会在进行隧道封装前对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进行分片检查。如果]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的大小超过了隧道出接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[减去]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文头长度的差值和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[要求的链路层所支持的最小]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值（]{style="font-family:宋体"}[1280]{lang="EN-US"}[字节），则隧道向]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文源发送报文过大的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[消息并丢弃该报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x658960187}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_x776211723}[使能隧道报文的分片检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_11842_x1255_827100479}

[\[Sysname\] tunnel ipv6-fragmentation-check enable]{lang="EN-US"}
:::::

::: {#1952233808 .myid}
[]{#_Toc404787139}[]{#struct_0_11842_x1255_1311129137}[]{#_Toc288212398}[]{#_Toc288220145}

**隧道 \-- 隧道配置命令 \-- tunnel tos**

------------------------------------------------------------------------

[**[tunnel tos]{lang="EN-US"}**]{#struct_0_11842_x1255_769013058}[命令用来设置封装后隧道报文的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[（]{style="font-family:宋体"}[Type of Service]{lang="EN-US"}[，服务类型）值。]{style="font-family:宋体"}

[**[undo tunnel tos]{lang="EN-US"}**]{#struct_0_11842_x1255_82115493}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1101473385}

[**[tunnel tos]{lang="EN-US"}**[ *tos-value*]{lang="EN-US"}]{#struct_0_11842_x1255_x372461869}

[**[undo]{lang="EN-US"}**[ **tunnel tos**]{lang="EN-US"}]{#struct_0_11842_x1255_x132608534}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1830320214}

[[封装后隧道报文的]{style="font-family:宋体"}[ToS]{lang="EN-US"}]{#struct_0_11842_x1255_943840975}[值与封装前原始报文的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值相同。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_407986807}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_1724611007}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1792387128}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_83098533}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_836804707}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1584307605}

[*[tos-value]{lang="EN-US"}*]{#struct_0_11842_x1255_2027935077}[：封装后]{style="font-family:宋体"}[隧道报文]{style="font-family:宋体"}[的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1156696126}

[[ToS]{lang="EN-US"}]{#struct_0_11842_x1255_x385586901}[值用于标识]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的服务类型。通过本命令设置封装后隧道报文的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值后，同一个隧道中转发的报文将具有相同的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值，即报文的业务类型都相同。关于]{style="font-family:宋体"}[ToS]{lang="EN-US"}[的详细介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[QoS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_253373953}

[[\# ]{lang="IT"}]{#struct_0_11842_x1255_1380071610}[在接口]{style="font-family:宋体"}[Tunnel1]{lang="IT"}[上设置封装后隧道报文的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_11842_x1255_83032997}

[\[Sysname\] interface tunnel 1 mode gre]{lang="NO-BOK"}

[\[Sysname-Tunnel1\] tunnel tos 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1221406315}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_989547045}
:::

::: {#1954265417 .myid}
[]{#_Toc404787140}[]{#struct_0_11842_x1255_1589802444}[]{#_Toc296524913}[]{#_Toc296525618}

**隧道 \-- 隧道配置命令 \-- tunnel ttl**

------------------------------------------------------------------------

[**[tunnel ttl]{lang="EN-US"}**]{#struct_0_11842_x1255_1771212087}[命令用来设置封装后隧道报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[（]{style="font-family:宋体"}[Time to Live]{lang="EN-US"}[，生存时间）值，从而决定隧道报文的最大跳数。]{style="font-family:宋体"}

[**[undo tunnel ttl]{lang="EN-US"}**]{#struct_0_11842_x1255_1214062198}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1971577882}

[**[tunnel ttl]{lang="EN-US"}**[ *ttl-value*]{lang="EN-US"}]{#struct_0_11842_x1255_x688795401}

[**[undo]{lang="EN-US"}**[ **tunnel ttl**]{lang="EN-US"}]{#struct_0_11842_x1255_x1335325677}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1766710386}

[[封装后隧道报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_11842_x1255_82574242}[值为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1333378131}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_935874488}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_452030548}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1687568140}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_x1217678117}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x2001959637}

[*[ttl-value]{lang="EN-US"}*]{#struct_0_11842_x1255_x1950332286}[：]{style="font-family:宋体"}[封装后隧道报文]{style="font-family:宋体"}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1830252968}

[[设置封装后隧道报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_11842_x1255_82508706}[值用来限制报文在隧道中转发的最大跳数。当报文转发跳数大于设置的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值时，该隧道报文将被丢弃，以避免出现环路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1359997403}

[[\# ]{lang="IT"}]{#struct_0_11842_x1255_1638618094}[在接口]{style="font-family:宋体"}[Tunnel1]{lang="IT"}[上设置封装后隧道报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_11842_x1255_1803336121}

[\[Sysname\] interface tunnel 1 mode gre]{lang="NO-BOK"}

[\[Sysname-Tunnel1\] tunnel ttl 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x171963067}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_11842_x1255_x1084196999}
:::

::: {#791499587 .myid}
[]{#_Toc404787141}[]{#struct_0_11842_x1255_x925246224}[]{#_Toc296524915}[]{#_Toc296525620}

**隧道 \-- 隧道配置命令 \-- tunnel vpn-instance**

------------------------------------------------------------------------

[**[tunnel vpn-instance]{lang="EN-US"}**]{#struct_0_11842_x1255_x9824386}[命令用来配置隧道目的端地址所属的]{style="font-family:宋体"}[VPN]{lang="FR"}[。]{style="font-family:宋体"}

[**[undo tunnel vpn-instance]{lang="EN-US"}**]{#struct_0_11842_x1255_1144439125}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_82443170}

[**[tunnel vpn-instance ]{lang="FR"}**]{#struct_0_11842_x1255_x1740771876}*[vpn-instance-name]{lang="FR"}*

[**[undo]{lang="FR"}**]{#struct_0_11842_x1255_2075806029}[ **tunnel vpn-instance**]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_11842_x1255_423944994}

[[隧道目的端地址属于公网]{style="font-family:宋体"}]{#struct_0_11842_x1255_x674877219}[，]{style="font-family:宋体"}[设备查找公网路由表转发隧道封装后的报文]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11842_x1255_406538762}

[[Tunnel]{lang="EN-US"}]{#struct_0_11842_x1255_x1318949147}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x1906892320}

[[network-admin]{lang="EN-US"}]{#struct_0_11842_x1255_1035777922}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11842_x1255_82377634}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11842_x1255_x674137409}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_11842_x1255_1544898818}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11842_x1255_2029971366}

[[通过本命令指定隧道目的端地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_11842_x1255_2114820779}[后，设备将查找指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的路由表转发隧道封装后的报文。]{style="font-family:宋体"}

[[在隧道的源接口上通过]{style="font-family:宋体"}**[ip binding vpn-instance]{lang="EN-US"}**]{#struct_0_11842_x1255_x485820509}[命令可以指定隧道源端地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。隧道的源端地址和目的端地址必须属于相同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，否则隧道接口链路状态无法]{style="font-family:宋体"}[UP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_11842_x1255_1465009518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_11842_x1255_440869774}

[[\# ]{lang="EN-US"}]{#struct_0_11842_x1255_1340566906}[在接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上指定封装后的隧道报文在]{style="font-family:宋体"}[vpn10]{lang="EN-US"}[中进行路由发送。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_11842_x1255_82312098}

[\[Sysname\] ip vpn-instance vpn10]{lang="EN-US"}

[\[Sysname-vpn-instance-vpn10\] route-distinguisher 1:1]{lang="EN-US"}

[\[Sysname-vpn-instance-vpn10\] vpn-target 1:1]{lang="EN-US"}

[\[Sysname-vpn-instance-vpn10\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip binding vpn-instance vpn10]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip address 1.1.1.1 24]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="FR"}

[\[Sysname\] interface tunnel 1 mode gre]{lang="FR"}

[\[Sysname-Tunnel1\] source gigabitethernet 1/0/1]{lang="FR"}

[\[Sysname-Tunnel1\] destination 1.1.1.2]{lang="FR"}

[\[Sysname-Tunnel1\] tunnel vpn-instance vpn10]{lang="FR"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_11842_x1255_1246377574}

[[\# ]{lang="FR"}]{#struct_0_11842_x1255_1888222449}[在接口]{style="font-family:宋体"}[Tunnel1]{lang="FR"}[上指定封装后的隧道报文在]{style="font-family:宋体"}[vpn10]{lang="FR"}[中进行路由发送。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_11842_x1255_82246562}

[\[Sysname\] ip vpn-instance vpn10]{lang="FR"}

[\[Sysname-vpn-instance-vpn10\] route-distinguisher 1:1]{lang="EN-US"}

[\[Sysname-vpn-instance-vpn10\] vpn-target 1:1]{lang="EN-US"}

[\[Sysname-vpn-instance-vpn10\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ip binding vpn-instance vpn10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ip address 1.1.1.1 24]{lang="EN-US"}

[\[Sysname-Vlan-interface10\]]{lang="EN-US"}[ quit]{lang="FR"}

[\[Sysname\] interface tunnel 1 mode gre]{lang="FR"}

[\[Sysname-Tunnel1\] source ]{lang="FR"}[vlan-interface 10]{lang="EN-US"}

[\[Sysname-Tunnel1\] destination 1.1.1.2]{lang="FR"}

[\[Sysname-Tunnel1\] tunnel vpn-instance vpn10]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_11842_x1255_2050636724}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[ip binding vpn-instance]{lang="EN-US"}**]{#struct_0_11842_x1255_x2108990162}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/MPLS L3VPN]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::
