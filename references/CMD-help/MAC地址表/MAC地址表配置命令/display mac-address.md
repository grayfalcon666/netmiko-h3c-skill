::: {#17794847 .myid}
[]{#_Toc404783963}[]{#struct_0_65355_x2050_x824606488}[]{#_Toc137954760}[]{#_Toc72830710}[]{#_Toc7497607}

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address**

------------------------------------------------------------------------

[**[display mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x194373524}[命令用来显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1455765515}

[**[display mac-address]{lang="EN-US"}**[ \[ *mac*-*address* \[ **vlan** *vlan-id* \] \| \[ \[ **dynamic** \| **static** \] \[ **interface** *interface-type interface-number* \] \| **blackhole** \| **multiport** \] \[ **vlan** *vlan-id* \] \[ **count** \] \| **nickname** *nickname* \]]{lang="EN-US"}]{#struct_0_65355_x2050_x1966759219}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_852496885}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_x1950747796}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x111669428}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x1809448166}

[[network-operator]{lang="EN-US"}]{#struct_0_65355_x2050_549676495}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_563055026}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65355_x2050_x326695807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1525046327}

[*[mac]{lang="EN-US"}*[-*address*]{lang="EN-US"}]{#struct_0_65355_x2050_x1433903737}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[-*address*]{lang="EN-US"}[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan]{lang="EN-US"}*[-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_x347733332}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id*]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_65355_x2050_x1040737063}[：显示动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_65355_x2050_x2007360955}[：显示静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}]{#struct_0_65355_x2050_x1353685074}[：显示指定接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[blackhole]{lang="EN-US"}**]{#struct_0_65355_x2050_563120562}[：显示黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[multiport]{lang="EN-US"}**]{#struct_0_65355_x2050_x313017009}[：显示多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_65355_x2050_x114211244}[：显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量。如果配置本参数，将仅显示符合条件的（由]{style="font-family:宋体"}**[count]{lang="EN-US"}**[前面的参数决定）]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量，而不显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体内容。如果不指定本参数，则显示符合条件的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的具体内容。]{style="font-family:宋体"}

[**[nickname]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}]{#struct_0_65355_x2050_1310419933}[：显示报文离开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络的]{style="font-family:宋体"}[RB]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x2033033892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用本命令可以查看静态、动态、黑洞和多端口单播]{style="font-family:宋体"}]{#struct_0_65355_x2050_295216693}[MAC]{lang="EN-US"}[地址表项，表项内容主要包括]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、接口等信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，将显示所有的]{style="font-family:宋体"}]{#struct_0_65355_x2050_x1932960630}[MAC]{lang="EN-US"}[地址表项信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于聚合接口，需要有选中端口，该聚合接口对应的动态]{style="font-family:宋体"}]{#struct_0_65355_x2050_983212484}[MAC]{lang="EN-US"}[地址才能在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项中显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1678270620}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x251316922}[显示]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display mac-address vlan 100]{lang="EN-US"}]{#struct_0_65355_x2050_562530739}

[MAC Address      VLAN ID    State            Port/NickName            Aging]{lang="EN-US"}

[0001-0101-0101   100        Multiport        GE1/0/1                  N]{lang="EN-US"}

[                                             GE1/0/2]{lang="EN-US"}

[0033-0033-0033   100        Blackhole        N/A                      N]{lang="EN-US"}

[0000-0000-0002   100        Static           GE1/0/3                  N]{lang="EN-US"}

[00e0-fc00-5829   100        Learned          GE1/0/4                  Y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x329798038}[显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量。]{style="font-family:宋体"}

[[\<Sysname\> display mac-address count]{lang="EN-US"}]{#struct_0_65355_x2050_1339270742}

[1 mac address(es) found.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x611959904}[显示指定]{style="font-family:宋体"}[nickname]{lang="EN-US"}[为]{style="font-family:宋体"}[0x8c81]{lang="EN-US"}[的]{style="font-family:宋体"}[RB]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}[display mac-address nickname 8c81]{lang="EN-US"}]{#struct_0_65355_x2050_x824507586}

[MAC Address      VLAN ID    State            Port/NickName            Aging]{lang="EN-US"}

[0000-3300-0001   10         Learned          0x8c81                   Y]{lang="EN-US"}

[0000-3300-0002   10         Learned          0x8c81                   Y]{lang="EN-US"}

[0000-3300-0003   10         Learned          0x8c81                   Y]{lang="EN-US"}

[]{#struct_0_65355_x2050_x413788831}[]{#_Toc138235585}[[表1-1 ]{lang="EN-US"}[display mac-address]{lang="EN-US"}]{#_Toc72830631}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2054451605}[[字段]{style="font-family:黑体"}]{#struct_0_65355_x2050_562596275}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65355_x2050_44567301}

[[MAC Address]{lang="EN-US"}]{#struct_0_65355_x2050_x1370286922}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x928838464}[地址]{style="font-family:宋体"}

[[VLAN ID ]{lang="EN-US"}]{#struct_0_65355_x2050_457483954}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x30931676}[地址对应接口所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_65355_x2050_x276047299}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562399667}[地址表项的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_65355_x2050_x1002948453}[：表示该表项是静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Learned]{lang="EN-US"}]{#struct_0_65355_x2050_x1464061324}[：动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。可以手工配置也可以由设备学习获得]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Blackhole]{lang="EN-US"}]{#struct_0_65355_x2050_22097485}[：表示该表项是黑洞]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multiport]{lang="EN-US"}]{#struct_0_65355_x2050_x1514162011}[：表示该表项是多端口单播]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{lang="EN-US" style="font-family:宋体"}

[[Port/NickName]{lang="EN-US"}]{#struct_0_65355_x2050_1650592083}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562465203}[地址对应的接口名称或]{style="font-family:宋体"}[NickName]{lang="EN-US"}[。如果显示为接口名称，表示发往该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文将从此接口发出（黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项此处显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[）；如果显示为]{style="font-family:宋体"}[NickName]{lang="EN-US"}[（长度为]{style="font-family:宋体"}[4]{lang="EN-US"}[的十六进制数字，例如]{style="font-family:宋体"}[0x12ab]{lang="EN-US"}[），表示发往该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文离开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络的]{style="font-family:宋体"}[RB]{lang="EN-US"}[。有关]{style="font-family:宋体"}[NickName]{lang="EN-US"}[、]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[和]{style="font-family:宋体"}[RB]{lang="EN-US"}[的详细介绍，请参见"]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[TRILL]{lang="EN-US"}["]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_65355_x2050_450038998}

[[老化时间，该表项有两种取值：]{style="font-family:宋体"}]{#struct_0_65355_x2050_x1461704638}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_65355_x2050_732072761}[：表示该表项会被老化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_65355_x2050_x768695045}[：表示该表项不会被老化]{style="font-family:宋体"}

[*[n]{lang="EN-US"}*[ mac address(es) found]{lang="EN-US"}]{#struct_0_65355_x2050_562792883}

[[共有]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_65355_x2050_x2076850515}[个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_686211051}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_950089189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address timer]{lang="EN-US"}**]{#struct_0_65355_x2050_136230669}

::: {#-1051840343 .myid}
[]{#_Toc404783964}[]{#struct_0_65355_x2050_1625755530}[]{#_Toc137954759}[]{#_Toc72830709}

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address aging-time**

------------------------------------------------------------------------

[**[display mac-address aging-time]{lang="EN-US"}**]{#struct_0_65355_x2050_x1100491350}[命令用来显示]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址表动态表项的老化时间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1419052264}

[**[display mac-address aging-time]{lang="EN-US"}**]{#struct_0_65355_x2050_562858419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_138039499}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_473582074}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x41353557}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x457756590}

[[network-operator]{lang="EN-US"}]{#struct_0_65355_x2050_x794413293}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x1070282660}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65355_x2050_x1961536992}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x542292884}

[[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562661811}[地址表项可以被老化，用户可以配置动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的老化时间。使用本命令可以查看用户配置的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x2053715846}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_1823507950}[显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表中动态表项的老化时间。]{style="font-family:宋体"}

[[\<Sysname\> display mac-address aging-time]{lang="EN-US"}]{#struct_0_65355_x2050_x1582448993}

[MAC address aging time: 300s.]{lang="EN-US"}

[[以上显示信息表示：]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x1699664024}[地址表中动态表项的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1466857592}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address timer]{lang="EN-US"}**]{#struct_0_65355_x2050_x1503635848}
:::

::::: {#-895469988 .myid}
[]{#_Toc404783965}[]{#struct_0_65355_x2050_x2021296152}[]{#_Toc137954758}[]{#_Toc72830708}[]{#_Toc47002024}[]{#_Toc288119834}[]{#_Toc288119987}[]{#_Toc288137359}[]{#_Toc291054948}

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address mac-learning**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_562727347}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_x824606487}
:::

**[ ]{lang="EN-US"}**

[**[display mac-address mac-learning]{lang="EN-US"}**]{#struct_0_65355_x2050_x194832276}[命令用来显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能的使能状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2091466096}

[**[display mac-address mac-learning ]{lang="EN-US"}**[\[ **interface** *interface*-*type interface*-*number* \]]{lang="EN-US"}]{#struct_0_65355_x2050_951465439}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_789116143}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_1088801392}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x494671092}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_836088275}

[[network-operator]{lang="EN-US"}]{#struct_0_65355_x2050_563055027}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x326695808}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65355_x2050_x1525111863}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x221620253}

[**[interface]{lang="EN-US"}**[ *interface*-*type interface*-*number*]{lang="EN-US"}]{#struct_0_65355_x2050_199950749}[：显示指定接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习状态。]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}[为接口类型和接口编号。如果不指定本参数，则显示全局和所有接口的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址学习状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x838742866}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_763284458}[显示全局和所有接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习状态。]{style="font-family:宋体"}

[[\<Sysname\> display mac-address mac-learning]{lang="EN-US"}]{#struct_0_65355_x2050_563120563}

[Global MAC address learning status: Enabled.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Port                        Learning Status]{lang="EN-US"}

[GE1/0/1                     Enabled]{lang="EN-US"}

[GE1/0/2                     Enabled]{lang="EN-US"}

[GE1/0/3                     Enabled]{lang="EN-US"}

[GE1/0/4                     Enabled]{lang="EN-US"}

[]{#struct_0_65355_x2050_x313017008}[]{#_Toc138235584}[[表1-2 ]{lang="EN-US"}[display mac-address mac-learning]{lang="EN-US"}]{#_Toc72830630}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x2052109685}[[字段]{style="font-family:黑体"}]{#struct_0_65355_x2050_x114145708}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_65355_x2050_x901107733}

[[Global MAC address learning status]{lang="EN-US"}]{#struct_0_65355_x2050_1694846639}

[[全局的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_678314205}[地址学习状态：]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[为使能，]{style="font-family:宋体"}[Disabled]{lang="EN-US"}[为禁止]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_65355_x2050_1247965274}

[[接口名称]{style="font-family:宋体"}]{#struct_0_65355_x2050_562530736}

[[Learning Status]{lang="EN-US"}]{#struct_0_65355_x2050_x329798051}

[[接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_1339729488}[地址学习状态：]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[为使能，]{style="font-family:宋体"}[Disabled]{lang="EN-US"}[为禁止]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x832027409}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address mac-learning enable]{lang="EN-US"}**]{#struct_0_65355_x2050_874152926}

::::: {#1127601417 .myid}
[]{#_Toc137954762}[]{#_Toc404783966}[]{#struct_0_65355_x2050_x1799063926}[]{#_Toc356979412}[]{#_Toc332903080}[]{#_Toc332903081}[]{#_Toc332903082}[]{#_Toc332903083}[]{#_Toc332903084}[]{#_Toc332903085}[]{#_Toc332903086}[]{#_Toc332903087}[]{#_Toc332903088}[]{#_Toc332903089}[]{#_Toc332903090}[]{#_Toc332903091}[]{#_Toc332903092}[]{#_Toc332903093}[]{#_Toc332903094}[]{#_Toc332903095}[]{#_Toc332903096}[]{#_Toc332903097}[]{#_Toc332903098}[]{#_Toc332903099}[]{#_Toc332903100}[]{#_Toc332903101}[]{#_Toc332903102}[]{#_Toc332903103}[]{#_Toc332903104}[]{#_Toc332903105}[]{#_Toc332903127}[]{#_Toc332903128}[]{#_Toc332903129}[]{#_Toc332903130}

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address mac-move**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_562596272}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_44567308}
:::

[ ]{lang="EN-US"}

[**[display mac-address mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_x943319882}[命令用来显示设备启动后的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址迁移记录。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1785277032}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_65355_x2050_x2025007741}

[**[display mac-address mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_1633102300}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65355_x2050_562399664}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display mac-address mac-move]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_65355_x2050_x1002948454}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_65355_x2050_x1867345851}[模式：]{style="font-family:宋体"}

[**[display mac-address mac-move]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_65355_x2050_1526108968}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_646371486}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_562465200}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_450038999}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x1461704637}

[[network-operator]{lang="EN-US"}]{#struct_0_65355_x2050_685018594}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_759545896}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65355_x2050_x83846812}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_562792880}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_65355_x2050_x2076850516}[：显示指定单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_65355_x2050_x2042672304}[：显示指定成员设备上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_65355_x2050_41473253}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_65355_x2050_900116235}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定任何参数，则显示所有单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_65355_x2050_x1880841048}[：显示指定单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定任何参数，则显示所有单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_65355_x2050_1058979462}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1398298786}

[[如果]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562858416}[地址迁移频繁出现，且同一]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址总是在特定的两个接口之间迁移，那么网络中可能存在二层环路。可以通过查看]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录，发现和定位环路。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65355_x2050_138039514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在迁移记录中，如果]{style="font-family:宋体"}]{#struct_0_65355_x2050_436846232}[MAC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[、源端口、新端口都一样，则视作一条表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备最多能保存]{style="font-family:宋体"}]{#struct_0_65355_x2050_x1518196607}[20]{lang="EN-US"}[条最近发生的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。当记录超过]{style="font-family:宋体"}[20]{lang="EN-US"}[条时，新的迁移记录将会根据上次迁移时间覆盖最早的记录。]{style="font-family:宋体"}[（集中式设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个单板最多能保存]{style="font-family:宋体"}]{#struct_0_65355_x2050_x193341600}[20]{lang="EN-US"}[条迁移记录；当记录超过]{style="font-family:宋体"}[20]{lang="EN-US"}[条时，新的迁移记录将会按照上次迁移时间覆盖最早的记录。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个成员设备最多能保存]{style="font-family:宋体"}]{#struct_0_65355_x2050_1799532841}[20]{lang="EN-US"}[条迁移记录；当记录超过]{style="font-family:宋体"}[20]{lang="EN-US"}[条时，新的迁移记录将会按照上次迁移时间覆盖最早的记录。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个成员设备的每个单板最多能保存]{style="font-family:宋体"}]{#struct_0_65355_x2050_562661808}[20]{lang="EN-US"}[条迁移记录。当记录超过]{style="font-family:宋体"}[20]{lang="EN-US"}[条时，新的迁移记录将会按照上次迁移时间覆盖最早的记录。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x97400719}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x460896103}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display mac-address mac-move slot 2]{lang="EN-US"}]{#struct_0_65355_x2050_x164962966}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--MAC address moving information\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[MAC address    VLAN Current port  Source port   Last time           Times]{lang="EN-US"}

[0000-0001-002c 1    GE1/0/1       GE1/0/2       2013-05-20 13:40:52 1]{lang="EN-US"}

[0000-0001-002c 1    GE1/0/2       GE1/0/1       2013-05-20 13:41:30 1]{lang="EN-US"}

[\-\--  2 MAC address moving records found  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_562727344}[显示所有单板上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移记录。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display mac-address mac-move]{lang="EN-US"}]{#struct_0_65355_x2050_x824606486}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--chassis 1 slot 2 MAC address moving information\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[MAC address    VLAN Current port  Source port   Last time           Times]{lang="EN-US"}

[0000-0001-002c 1    GE1/0/1       GE1/0/2       2013-05-20 13:40:52 20]{lang="EN-US"}

[0000-0001-002c 1    GE1/0/2       GE1/0/1       2013-05-20 13:41:32 20]{lang="EN-US"}

[\-\--  2 MAC address moving records found  \-\--]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display mac-address mac-move]{lang="EN-US"}]{#struct_0_65355_x2050_x194766740}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2058919221}[[字段]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1071968390}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_65355_x2050_563055024}

[[MAC address]{lang="EN-US"}]{#struct_0_65355_x2050_x326695809}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x1525177399}[地址]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_65355_x2050_85582746}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_563120560}[地址对应接口所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Current port]{lang="EN-US"}]{#struct_0_65355_x2050_x313017007}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x115128748}[地址迁移新接口]{style="font-family:宋体"}

[[Source port]{lang="EN-US"}]{#struct_0_65355_x2050_562530737}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x329798052}[地址迁移源接口]{style="font-family:宋体"}

[[Last time]{lang="EN-US"}]{#struct_0_65355_x2050_1339663952}

[[发生]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x62092945}[地址迁移的最近一次时间]{style="font-family:宋体"}

[[Times]{lang="EN-US"}]{#struct_0_65355_x2050_562596273}

[[设备启动后，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_44567307}[地址发生迁移的次数。对于同一]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，仅当字段]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[、]{style="font-family:宋体"}[Current port]{lang="EN-US"}[和]{style="font-family:宋体"}[Source port]{lang="EN-US"}[都相同时，次数才加]{style="font-family:宋体"}[1]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x223275850}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[mac-address notification mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_562399665}

::::: {#-1005926965 .myid}
[]{#_Toc404783967}[]{#struct_0_65355_x2050_x1002948455}

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_x301261910}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_x1248762534}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**]{#struct_0_65355_x2050_1894435686}**[ mac-address statistics]{lang="EN-US"}**[命令用来显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_29996546}

[**[display mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x1542448387}[ **statistics**]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x391750398}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_1789666897}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_562465201}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_450039000}

[[network-operator]{lang="EN-US"}]{#struct_0_65355_x2050_x1063317817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x1359605421}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65355_x2050_x836520379}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_197124727}

[[本命令主要显示系统目前存在的各类]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_2117565521}[地址表项的数目、以及系统可以支持的各类表项的最大规格。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1374792042}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_106487538}[显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表中]{style="font-family:宋体"}[的统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display mac-address statistics]{lang="EN-US"}]{#struct_0_65355_x2050_562792881}

[MAC Address Count:]{lang="EN-US"}

[Dynamic Unicast Address (Learned) Count:                         3]{lang="EN-US"}

[Dynamic Unicast Address (Security-service-defined) Count:        4]{lang="EN-US"}

[Static Unicast Address (User-defined) Count:                     0]{lang="EN-US"}

[Static Unicast Address (System-defined) Count:                   3]{lang="EN-US"}

[Total Unicast MAC Addresses In Use:                              10]{lang="EN-US"}

[Total Unicast MAC Addresses Available:                           32768]{lang="EN-US"}

[Multicast and Multiport MAC Address Count:                       1]{lang="EN-US"}

[Static Multicast and Multiport MAC Address (User-defined) Count: 1]{lang="EN-US"}

[Total Multicast and Multiport MAC Addresses Available:           256]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display mac-address statistic]{lang="EN-US"}]{#struct_0_65355_x2050_x2076850517}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2030676917}[[字段]{style="font-family:黑体"}]{#struct_0_65355_x2050_x476588363}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1524605558}

[[Dynamic Unicast Address (Learned) Count]{lang="EN-US"}]{#struct_0_65355_x2050_x1465245755}

[[报文触发添加的动态单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562858417}[地址统计]{style="font-family:宋体"}

[[Dynamic Unicast Address (Security-service-defined) Count]{lang="EN-US"}]{#struct_0_65355_x2050_138039513}

[[安全服务触发添加的动态单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_436846239}[地址统计]{style="font-family:宋体"}

[[Static Unicast Address (User-defined) Count]{lang="EN-US"}]{#struct_0_65355_x2050_x1518196612}

[[用户添加的静态单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_209877391}[地址统计]{style="font-family:宋体"}

[[Static Unicast Address (System-defined) Count]{lang="EN-US"}]{#struct_0_65355_x2050_381546043}

[[系统添加的静态单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562661809}[地址统计]{style="font-family:宋体"}

[[Total Unicast MAC Addresses In Use]{lang="EN-US"}]{#struct_0_65355_x2050_x97400718}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x460896102}[地址统计]{style="font-family:宋体"}

[[Total Unicast MAC Addresses Available]{lang="EN-US"}]{#struct_0_65355_x2050_x165028502}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_2086566792}[地址规格]{style="font-family:宋体"}

[[Multicast and Multiport MAC Address Count]{lang="EN-US"}]{#struct_0_65355_x2050_x1142205375}

[[组播和多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562727345}[地址统计]{style="font-family:宋体"}

[[Static Multicast and Multiport MAC Address (User-defined) Count]{lang="EN-US"}]{#struct_0_65355_x2050_x824606485}

[[用户添加的静态组播和多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x194701204}[地址统计]{style="font-family:宋体"}

[[Total Multicast and Multiport MAC Addresses Available]{lang="EN-US"}]{#struct_0_65355_x2050_527544749}

[[组播和多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x1694209147}[地址规格]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-97260767 .myid}
[]{#_Toc404783968}[]{#struct_0_65355_x2050_x1660928177}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address (interface view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_563055025}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_x326695810}
:::

[ ]{lang="EN-US"}

[**[mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x1524587576}[命令用来在当前接口下添加或者修改]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[undo mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x1374705717}[命令用来删除当前接口下的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x331714165}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65355_x2050_531697736}[二层聚合接口视图：]{style="font-family:宋体"}

[**[mac-address ]{lang="EN-US"}**[{ **dynamic** \| **multiport** \| **static** } *mac*-*address* **vlan** *vlan*-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_x1931712593}

[**[undo mac-address]{lang="EN-US"}**[ { **dynamic** \| **multiport** \| **static** } *mac*-*address* **vlan** *vlan*-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_x1303155920}

[[S]{lang="EN-US"}]{#struct_0_65355_x2050_563120561}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图：]{style="font-family:宋体"}

[**[mac-address ]{lang="EN-US"}**[{ **dynamic** \| **static** } *mac*-*address* **vlan** *vlan*-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_x313017006}

[**[undo mac-address]{lang="EN-US"}**[ { **dynamic** \| **static** } *mac*-*address* **vlan** *vlan*-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_x115063212}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1645251609}

[[接口下没有配置任何]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_1606917970}[地址表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_233668760}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65355_x2050_x1838109941}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1103014187}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_277476942}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_562530734}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x329798049}

[**[dynamic]{lang="EN-US"}**]{#struct_0_65355_x2050_1339205199}[：动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_65355_x2050_x789524915}[：静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[multiport]{lang="EN-US"}**]{#struct_0_65355_x2050_773527349}[：多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。当报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项匹配时，将该报文从多个端口复制转发出去。]{style="font-family:宋体"}

[*[mac]{lang="EN-US"}*[-*address*]{lang="EN-US"}]{#struct_0_65355_x2050_338063350}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，不支持组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和全]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan]{lang="EN-US"}*[-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_491715223}[：[当前接口所属的]{#_Toc121110292}]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须已经创建。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1078724236}

[[一般情况下，设备通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562596270}[地址学习过程自动建立]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表。为了提高接口安全性，网络管理员可手工在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表中加入特定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，将用户设备与接口绑定，从而防止非法用户骗取数据。手工配置的静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项优先级高于自动生成的表项。]{style="font-family:宋体"}

[[需要注意的是，如果不保存配置，设备重启后所有表项都会丢失；如果保存配置，静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_44567306}[地址表项不会丢失，动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项会丢失。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1733039286}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x1875294897}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下增加静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[000f-e201-0101]{lang="EN-US"}[，该端口属于]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1684077851}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-address static 000f-e201-0101 vlan 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_276368021}[在接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="EN-US"}[下增加静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[000f-e201-0102]{lang="EN-US"}[，该接口属于]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1346812021}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] mac-address static 000f-e201-0102 vlan 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x20619184}[在]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:
宋体"}[S-Channel1/1:10]{lang="EN-US"}[下增加静态]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[000f-e201-0102]{lang="EN-US"}[，该接口属于]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_562399662}

[\[Sysname\] interface s-channel 1/1:10]{lang="EN-US"}

[\[Sysname-S-Channel1/1:10\] mac-address static 000f-e201-0102 vlan 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x1002948448}[在]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:2]{lang="EN-US"}[下增加静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[000f-e201-0102]{lang="EN-US"}[，该接口属于]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x254142207}

[\[Sysname\] interface schannel-aggregation 1:2]{lang="EN-US"}

[\[Sysname-Schannel-Aggregation1:2\] mac-address static 000f-e201-0102 vlan 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x967309104}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[下增加多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}[0001-0001-0101]{lang="EN-US"}[，两个端口均属于]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_514846886}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-address multiport 0001-0001-0101 vlan 2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] mac-address multiport 0001-0001-0101 vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1959647284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_562465198}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address]{lang="EN-US"}**[ (system view)]{lang="EN-US"}]{#struct_0_65355_x2050_x1469540300}
:::::

::: {#811055401 .myid}
[]{#_Toc404783969}[]{#struct_0_65355_x2050_x2110582510}[]{#_Toc137954761}[]{#_Toc72830711}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address (system view)**

------------------------------------------------------------------------

[**[mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x1538136547}[命令用来添加或者修改]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[undo mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x327113813}[命令用来删除]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1526554279}

[**[mac-address]{lang="EN-US"}**[ { **dynamic** \| **static** } *mac*-*address* **interface** *interface*-*type interface*-*number* **vlan** *vlan*-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_1833722061}

[**[mac-address]{lang="EN-US"}**[ **blackhole** *mac*-*address* **vlan** *vlan*-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_x1113129482}

[**[mac-address multiport ]{lang="EN-US"}***[mac]{lang="EN-US"}*[-*address* **interface** *interface-list* **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_65355_x2050_x1849196527}

[**[undo mac-address]{lang="EN-US"}**[ \[ \[ **dynamic** \| **static** \] *mac*-*address* **interface** *interface*-*type interface*-*number* **vlan** *vlan*-*id* \]]{lang="EN-US"}]{#struct_0_65355_x2050_562792878}

[**[undo mac-address]{lang="EN-US"}**[ \[ **blackhole** \| **dynamic** \| **static** \] \[ *mac*-*address* \] **vlan** *vlan*-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_1498072740}

[**[undo mac-address]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **dynamic** \| **static** \] **interface** *interface*-*type interface*-*number*]{lang="EN-US"}]{#struct_0_65355_x2050_164851579}

[**[undo mac-address]{lang="EN-US"}**[ **multiport** *mac-address* **interface** *interface-list* **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_65355_x2050_1457055080}

[**[undo mac-address]{lang="EN-US"}**[ \[ **multiport** \] \[ \[ *mac-address* \] **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_65355_x2050_742841858}

[**[undo mac-address]{lang="EN-US"}**[ **nickname** *nickname*]{lang="EN-US"}]{#struct_0_65355_x2050_x2077573562}

[**[undo mac-address]{lang="EN-US"}**[ *mac-address* **nickname** *nickname* **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_65355_x2050_x1352385739}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1627827189}

[[系统没有配置任何]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x1269907108}[地址表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_562858414}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_138039512}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_436846238}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x1518196613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1775961332}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_183484229}

[**[dynamic]{lang="EN-US"}**]{#struct_0_65355_x2050_x2012807856}[：动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_65355_x2050_x989743949}[：静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[blackhole]{lang="EN-US"}**]{#struct_0_65355_x2050_934662254}[：黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。当报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址或目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项匹配时，该报文被丢弃。]{style="font-family:宋体"}

[**[multiport]{lang="EN-US"}**]{#struct_0_65355_x2050_562661806}[：多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。当报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项匹配时，将该报文从多个端口复制转发出去。]{style="font-family:宋体"}

[*[mac]{lang="EN-US"}*[-*address*]{lang="EN-US"}]{#struct_0_65355_x2050_x97400709}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，不支持组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和全]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan]{lang="EN-US"}*[-*id*]{lang="EN-US"}]{#struct_0_65355_x2050_1495419033}[：指定接口所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[必须已经创建。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}]{#struct_0_65355_x2050_1259880119}[：出接口。]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type interface*-*number*]{lang="EN-US"}[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[interface]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_65355_x2050_x118938616}[：接口列表，表示方式为]{style="font-family:宋体"}*[interface-list =]{lang="EN-US"}*[ { *interface-type interface-number* \[ **to** *interface-type interface-number* \] }&\<1-n\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号，目前只支持]{style="font-family:
宋体"}[二层以太网接口及二层聚合接口。]{style="font-family:宋体"}[&\<1-n\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[n]{lang="EN-US"}[次。]{style="font-family:宋体"}[n]{lang="EN-US"}[的取值范围和设备相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[nickname]{lang="EN-US"}**[ *nickname*]{lang="EN-US"}]{#struct_0_65355_x2050_1157461979}[：报文离开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络的]{style="font-family:宋体"}[RB]{lang="EN-US"}[。]{style="font-family:宋体"}*[nickname]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RB]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFE]{lang="EN-US"}[的十六进制数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1971539985}

[[一般情况下，设备通过源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x1333199515}[地址学习过程自动建立]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表。为了提高接口安全性，网络管理员可手工在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表中加入特定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，将用户设备与接口绑定，从而防止非法用户骗取数据。手工配置的静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项优先级高于自动生成的表项。]{style="font-family:宋体"}

[[如果需要丢弃指定源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_562727342}[地址或目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文，可配置黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x824606484}[地址表项用于目的是某个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的报文从多个端口复制转发出去。第一次执行命令配置某一]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项时，添加该表项，再次执行命令配置除接口外其余相同的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项时，则会为该表项添加一个或多个接口。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65355_x2050_x194635668}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x679967686}[地址表项的属性遵循如下原则：用户手工配置的静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项或黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项不会被动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项覆盖，而动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项可以被静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项和黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项覆盖。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_65355_x2050_2059028978}**[undo mac-address]{lang="EN-US"}**[命令时若不指定任何参数，将删除所有单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项和静态组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以删除指定]{style="font-family:宋体"}]{#struct_0_65355_x2050_1921367407}[VLAN]{lang="EN-US"}[的所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项（包括单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项和静态组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项）；可以选择删除动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项、静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项、黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项或者多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项；可以按接口删除单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，但不能按接口删除组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项；可以按报文离开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络的]{style="font-family:宋体"}[RB]{lang="EN-US"}[删除单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不保存配置，设备重启后所有表项都会丢失；如果保存配置，静态]{style="font-family:宋体"}]{#struct_0_65355_x2050_1039449960}[MAC]{lang="EN-US"}[地址表项和黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项不会丢失，动态表项会丢失。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x528988974}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x16210287}[添加静态地址表项，目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000f-e201-0101]{lang="EN-US"}[，出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，且该接口属于]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_563055022}

[\[Sysname\] mac-address static 000f-e201-0101 interface gigabitethernet 1/0/1 vlan 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x326695811}[添加多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000f-e201-0101]{lang="EN-US"}[，出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[、]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[，且出接口属于]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1524653112}

[\[Sysname\] mac-address multiport 000f-e201-0101 interface gigabitethernet 1/0/1 to gigabitethernet 1/0/3 vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1489130328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x203737520}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address]{lang="EN-US"}**[ (interface view)]{lang="EN-US"}]{#struct_0_65355_x2050_x1611378856}
:::

::::: {#-1713806505 .myid}
[]{#_Toc7497605}[]{#_Toc2757619}[]{#_Toc72830712}[]{#_Toc47002028}[]{#_Toc404783970}[]{#struct_0_65355_x2050_209944221}[]{#_Toc137954763}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address mac-learning enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image002.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_410936187}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_563120558}
:::

[ ]{lang="EN-US"}

[**[mac-address mac-learning enable]{lang="EN-US"}**]{#struct_0_65355_x2050_1260961113}[命令用来打开设备全局、接口或者]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[**[undo mac-address mac-learning enable]{lang="EN-US"}**]{#struct_0_65355_x2050_x767113407}[命令用来关闭设备全局、接口或者]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1617330543}

[**[mac-address mac-learning enable]{lang="EN-US"}**]{#struct_0_65355_x2050_1531745515}

[**[undo mac-address mac-learning enable]{lang="EN-US"}**]{#struct_0_65355_x2050_1206046129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x686551774}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_15382890}[地址学习功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x913033827}

[[系统视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}]{#struct_0_65355_x2050_562530735}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x329798050}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1339795024}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1527762357}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1280959313}

[[有时为了保证设备的安全，需要关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x464185082}[地址学习功能。常见的危及设备安全的情况是：非法用户使用大量源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不同的报文攻击设备，导致设备]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表资源耗尽，造成设备无法根据网络的变化更新]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表。关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能可以有效防止这种攻击。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x406558784}[地址学习功能后，设备就学不到新地址，从而影响设备及时刷新]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表。用户可以根据实际情况关闭接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x474311133}[地址学习功能可能会导致广播，因此在关闭接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能的同时，一般还要使用接口广播风暴抑制功能。有关广播风暴抑制功能的介绍，请参见"接口管理配置指导"中的"以太网接口"。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65355_x2050_x230453882}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局]{style="font-family:宋体"}]{#struct_0_65355_x2050_562596271}[MAC]{lang="EN-US"}[地址学习功能不能控制]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[网络、]{style="font-family:宋体"}[EVB]{lang="EN-US"}[的]{style="font-family:宋体"}[S]{lang="EN-US"}[通道以及]{style="font-family:
宋体"}[VPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[中]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的学习。有关]{style="font-family:宋体"}[EVB]{lang="EN-US"}[和]{style="font-family:宋体"}[S]{lang="EN-US"}[通道的介绍，请参见"]{style="font-family:
宋体"}[EVB]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[EVB]{lang="EN-US"}["。有关]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[和]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[VPLS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭全局的]{style="font-family:宋体"}]{#struct_0_65355_x2050_44567305}[MAC]{lang="EN-US"}[地址学习功能的同时也就关闭了全部接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在开启全局的]{style="font-family:宋体"}]{#struct_0_65355_x2050_x605612874}[MAC]{lang="EN-US"}[地址学习功能的前提下，用户可以关闭设备上单个接口或指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭]{style="font-family:宋体"}]{#struct_0_65355_x2050_1946421360}[MAC]{lang="EN-US"}[地址学习功能后，对于已经存在的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的处理情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1138145259}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_517918202}[关闭全局]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1265431272}

[\[Sysname\] undo mac-address mac-learning enable]{lang="EN-US"}

[]{#_Toc72830713}[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x812746946}[关闭]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_562399663}

[\[Sysname\] vlan 10]{lang="EN-US"}

[\[Sysname-vlan10\] undo mac-address mac-learning enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x1002948449}[关闭端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_1311941734}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo mac-address mac-learning enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_43487074}[关闭接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1646007180}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] undo mac-address mac-learning enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_1825032950}[关闭]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channel1/1:10]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1715921639}

[\[Sysname\] interface s-channel 1/1:10]{lang="EN-US"}

[\[Sysname-S-Channel1/1:10\] undo mac-address mac-learning enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_562465199}[关闭]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:2]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1469540299}

[\[Sysname\] interface schannel-aggregation 1:2]{lang="EN-US"}

[\[Sysname-Schannel-Aggregation1:2\] undo mac-address mac-learning enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_974989956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-address mac-learning]{lang="EN-US"}**]{#struct_0_65355_x2050_431127518}
:::::

::::: {#-1993967741 .myid}
[]{#_Toc137954764}[]{#_Toc404783971}[]{#struct_0_65355_x2050_x1552921043}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address mac-learning priority**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){#图片 8 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_398171448}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_345391479}
:::

[ ]{lang="EN-US"}

[**[mac-address mac-learning priority]{lang="EN-US"}**]{#struct_0_65355_x2050_972245253}[命令用来配置接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习优先级。]{style="font-family:宋体"}

[**[undo mac-address mac-learning priority]{lang="EN-US"}**]{#struct_0_65355_x2050_562792879}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1498072739}

[**[mac-address mac-learning priority]{lang="EN-US"}**[ { **high** \| **low** }]{lang="EN-US"}]{#struct_0_65355_x2050_164392824}

[**[undo mac-address mac-learning priority]{lang="EN-US"}**]{#struct_0_65355_x2050_x511449206}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x934280487}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_2079580649}[地址学习优先级为低优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1697786029}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65355_x2050_1315520895}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_191693963}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_562858415}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_138039511}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_436846237}

[**[high]{lang="EN-US"}**]{#struct_0_65355_x2050_x1518196602}[：配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习优先级为高优先级。]{style="font-family:宋体"}

[**[low]{lang="EN-US"}**]{#struct_0_65355_x2050_209942927}[：配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习优先级为低优先级。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1507052740}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口的]{style="font-family:宋体"}]{#struct_0_65355_x2050_2070201237}[MAC]{lang="EN-US"}[地址学习功能分为两个优先级：高优先级和低优先级。对于高优先级的接口，可以学习任何]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址；对于低优先级的接口，在学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时需要查看高优先级接口是否已经学到该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，如果已经学到，则不允许学习该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了预防攻击，可以将上行接口的]{style="font-family:宋体"}]{#struct_0_65355_x2050_1095349160}[MAC]{lang="EN-US"}[地址学习优先级配置为高优先级，下行接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习优先级配置为低优先级，那么，下行接口就不会学到网关等上层设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，避免了攻击。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x800112805}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_562661807}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习优先级为高优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x97400708}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-address mac-learning priority high]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_1495419034}[配置接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习优先级为高优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_1259945655}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] mac-address mac-learning priority high]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_1085725928}[配置]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channel1/1:10]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习优先级为高优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_215006746}

[\[Sysname\] interface s-channel 1/1:10]{lang="EN-US"}

[\[Sysname-S-Channel1/1:10\] mac-address mac-learning priority high]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_1584588889}[配置]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:2]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习优先级为高优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_562727343}

[\[Sysname\] interface schannel-aggregation 1:2]{lang="EN-US"}

[\[Sysname-Schannel-Aggregation1:2\] mac-address mac-learning priority high]{lang="EN-US"}
:::::

::::: {#-172354801 .myid}
[]{#_Toc404783972}[]{#struct_0_65355_x2050_x824606483}[]{#_Toc328491594}[]{#_Toc329164313}[]{#_Toc329694402}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address mac-roaming enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_x195094420}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_x1100810321}
:::

[ ]{lang="EN-US"}

[**[mac-address mac-roaming enable]{lang="EN-US"}**]{#struct_0_65355_x2050_x55226251}[命令用来开启全局的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址同步功能。]{style="font-family:宋体"}

[**[undo mac-address mac-roaming enable]{lang="EN-US"}**]{#struct_0_65355_x2050_387385521}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_669812973}

[**[mac-address mac-roaming enable]{lang="EN-US"}**]{#struct_0_65355_x2050_x1901321902}

[**[undo mac-address mac-roaming enable]{lang="EN-US"}**]{#struct_0_65355_x2050_563055023}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x326695812}

[[全局的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x1524718648}[地址同步功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x2106704243}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_1862677203}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1670874055}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1819674223}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1847777101}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x2129920914}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不同]{style="font-family:宋体"}]{#struct_0_65355_x2050_563120559}[IRF]{lang="EN-US"}[成员设备上的端口为同一聚合组的选中端口，则不论全局的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址同步功能是否开启，这些选中端口所在成员设备间都会进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址同步。有关聚合组的相关介绍和配置内容，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"以太网链路聚合"。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启全局的]{style="font-family:宋体"}]{#struct_0_65355_x2050_1260961114}[MAC]{lang="EN-US"}[地址同步功能后，若不同]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址规格不同，会造成超过成员设备规格的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址无法同步成功。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[设备）]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若设备不同单板上的端口为同一聚合组的选中端口，则不论全局的]{style="font-family:宋体"}]{#struct_0_65355_x2050_x767178943}[MAC]{lang="EN-US"}[地址同步功能是否开启，这些选中端口所在单板间都会进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址同步。有关聚合组的相关介绍和配置内容，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"以太网链路聚合"。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启全局的]{style="font-family:宋体"}]{#struct_0_65355_x2050_x1625785372}[MAC]{lang="EN-US"}[地址同步功能后，若设备上不同单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址规格不同，会造成超过单板规格的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址无法同步成功。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1957518969}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_2114730917}[开启全局的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址同步功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_1891629188}

[\[Sysname\] mac-address mac-roaming enable]{lang="EN-US"}
:::::

::::: {#594119000 .myid}
[]{#_Toc404783973}[]{#struct_0_65355_x2050_x835371264}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address max-mac-count (interface view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_x60133987}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_2128614679}
:::

**[ ]{lang="EN-US"}**

[**[mac-address max-mac-count]{lang="EN-US"}**]{#struct_0_65355_x2050_1179276600}[命令用来配置接口的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址数学习上限。]{style="font-family:宋体"}

[**[undo mac-address max-mac-count]{lang="EN-US"}**]{#struct_0_65355_x2050_687599851}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x181046448}

[**[mac-address max-mac-count]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_65355_x2050_x1321980616}

[**[undo mac-address max-mac-count]{lang="EN-US"}**]{#struct_0_65355_x2050_1535273717}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1450538504}

[[接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x726851358}[地址数学习上限与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128680215}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65355_x2050_x35444830}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1600022687}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_2121825268}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_535873676}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1063626480}

[*[count]{lang="EN-US"}*]{#struct_0_65355_x2050_x1732508965}[：接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限，为]{style="font-family:宋体"}[0]{lang="EN-US"}[即表示不允许该接口学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x671779628}

[[通过配置接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_1105258796}[地址数学习上限，用户可以控制设备维护的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的表项数量。如果]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表过于庞大，可能导致设备的转发性能下降。当接口学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到上限时，该接口将不再对]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行学习。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128483607}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x1203534412}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限为]{style="font-family:宋体"}[600]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_676266599}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-address max-mac-count 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x209945570}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x855230263}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address max-mac-count enable-forwarding]{lang="EN-US"}**[ (interface view)]{lang="EN-US"}]{#struct_0_65355_x2050_x1901792799}
:::::

::::: {#254539544 .myid}
[]{#_Toc72830714}[]{#_Toc404783974}[]{#struct_0_65355_x2050_x1329666312}[]{#_Toc137954765}[]{#_Toc335818082}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address max-mac-count (VLAN view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_x1396851428}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_2128549143}
:::

[ ]{lang="EN-US"}

[**[mac-address max-mac-count]{lang="EN-US"}**]{#struct_0_65355_x2050_1483948281}[命令用来配置]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限。]{style="font-family:宋体"}

[**[undo mac-address max-mac-count]{lang="EN-US"}**]{#struct_0_65355_x2050_2045104507}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_604923016}

[**[mac-address max-mac-count]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_65355_x2050_x1268636143}

[**[undo mac-address max-mac-count]{lang="EN-US"}**]{#struct_0_65355_x2050_88802119}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_864804123}

[[VLAN]{lang="EN-US"}]{#struct_0_65355_x2050_x2079796742}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_176658667}

[[VLAN]{lang="EN-US"}]{#struct_0_65355_x2050_2128876823}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_719535395}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_943841530}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x1507005640}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1351564101}

[*[count]{lang="EN-US"}*]{#struct_0_65355_x2050_x698899092}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限，]{style="font-family:宋体"}[0]{lang="EN-US"}[即表示不允许该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[学习]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1183452478}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过配置]{style="font-family:宋体"}]{#struct_0_65355_x2050_x1856795211}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限，用户可以控制设备维护的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的表项数量。如果]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表过于庞大，可能导致设备的转发性能下降。当]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到上限时，该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[将不再对]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址进行学习。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于]{style="font-family:宋体"}]{#struct_0_65355_x2050_605667038}[Super VLAN]{lang="EN-US"}[没有实际的二层物理端口，学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数永远为]{style="font-family:宋体"}[0]{lang="EN-US"}[，所以在]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[下配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限没有意义。有关]{style="font-family:宋体"}[Super VLAN]{lang="EN-US"}[的详细介绍，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换"中的"]{style="font-family:宋体"}[VLAN]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128942359}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x820048057}[配置]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限为]{style="font-family:宋体"}[600]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_16885063}

[\[Sysname\] vlan 10]{lang="EN-US"}

[\[Sysname-vlan10\] mac-address max-mac-count 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1818906856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_1052699961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address max-mac-count enable-forwarding]{lang="EN-US"}**[ (VLAN view)]{lang="EN-US"}]{#struct_0_65355_x2050_x1120971514}
:::::

::::: {#-277988293 .myid}
[]{#_Toc404783975}[]{#struct_0_65355_x2050_172360340}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address max-mac-count enable-forwarding (interface view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){#图片 9 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_x55733906}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_2128745751}
:::

**[ ]{lang="EN-US"}**

[**[mac-address max-mac-count enable-forwarding]{lang="EN-US"}**]{#struct_0_65355_x2050_1950206322}[命令用来配置当达到接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限时，允许转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[**[undo mac-address max-mac-count enable-forwarding]{lang="EN-US"}**]{#struct_0_65355_x2050_x1052677713}[命令用来配置当达到接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限时，禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1164458543}

[**[mac-address max-mac-count enable-forwarding]{lang="EN-US"}**]{#struct_0_65355_x2050_x365894174}

[**[undo mac-address max-mac-count]{lang="EN-US"}**[ **enable-forwarding**]{lang="EN-US"}]{#struct_0_65355_x2050_x460262351}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1445464531}

[[当达到接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_323645671}[地址数学习上限时，允许转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x844946458}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65355_x2050_2128811287}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1590584582}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x145042317}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1166550835}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1951421224}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x1078939660}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限为]{style="font-family:宋体"}[600]{lang="EN-US"}[，当端口学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到]{style="font-family:宋体"}[600]{lang="EN-US"}[时，禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_926298741}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-address max-mac-count 600]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo mac-address max-mac-count enable-forwarding]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x130178309}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_2129138967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address max-mac-count]{lang="EN-US"}**[ (interface view)]{lang="EN-US"}]{#struct_0_65355_x2050_692833232}
:::::

::::: {#1107669012 .myid}
[]{#_Toc404783976}[]{#struct_0_65355_x2050_x311230736}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address max-mac-count enable-forwarding (VLAN view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){#图片 10 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_x1541811720}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_1579803351}
:::

[ ]{lang="EN-US"}

[**[mac-address max-mac-count enable-forwarding]{lang="EN-US"}**]{#struct_0_65355_x2050_x1920620386}[命令用来配置当达到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限时，允许转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[**[undo mac-address max-mac-count enable-forwarding]{lang="EN-US"}**]{#struct_0_65355_x2050_1726294983}[命令用来配置当达到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限时，禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2126995885}

[**[mac-address max-mac-count enable-forwarding]{lang="EN-US"}**]{#struct_0_65355_x2050_x1383741379}

[**[undo mac-address max-mac-count enable-forwarding]{lang="EN-US"}**]{#struct_0_65355_x2050_2129204503}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_13849777}

[[当达到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_65355_x2050_153994623}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限时，允许转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1391405758}

[[VLAN]{lang="EN-US"}]{#struct_0_65355_x2050_619427317}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2075843864}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x1873241057}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x694322222}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1879129259}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_2128614680}[配置]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数学习上限为]{style="font-family:宋体"}[600]{lang="EN-US"}[，当]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[学习的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到]{style="font-family:宋体"}[600]{lang="EN-US"}[时，禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_1179866413}

[\[Sysname\] vlan 10]{lang="EN-US"}

[\[Sysname-vlan10\] mac-address max-mac-count 600]{lang="EN-US"}

[\[Sysname-vlan10\] undo mac-address max-mac-count enable-forwarding]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_311816096}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_1515715722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address max-mac-count]{lang="EN-US"}**[ (VLAN view)]{lang="EN-US"}]{#struct_0_65355_x2050_x18324846}
:::::

::::: {#61522978 .myid}
[]{#_Toc137954766}[]{#_Toc404783977}[]{#struct_0_65355_x2050_x1047552150}[]{#_Toc356979407}[]{#_Toc335818086}[]{#_Toc335818087}[]{#_Toc335818088}[]{#_Toc335818089}[]{#_Toc335818090}[]{#_Toc335818091}[]{#_Toc335818092}[]{#_Toc335818093}[]{#_Toc335818094}[]{#_Toc335818095}[]{#_Toc335818096}[]{#_Toc335818097}[]{#_Toc335818098}[]{#_Toc335818099}[]{#_Toc335818100}[]{#_Toc335818101}[]{#_Toc335818102}[]{#_Toc335818103}[]{#_Toc335818104}[]{#_Toc335818105}[]{#_Toc335818106}[]{#_Toc335818107}[]{#_Toc335818108}[]{#_Toc335818109}[]{#_Toc335818110}[]{#_Toc335818111}[]{#_Toc335818112}[]{#_Toc335818113}[]{#_Toc335818114}[]{#_Toc335818115}[]{#_Toc335818116}[]{#_Toc335818117}[]{#_Toc335818118}[]{#_Toc335818119}[]{#_Toc335818120}[]{#_Toc335818121}[]{#_Toc335818122}[]{#_Toc335818123}[]{#_Toc335818124}[]{#_Toc335818125}[]{#_Toc335818126}[]{#_Toc335818127}[]{#_Toc335818128}[]{#_Toc335818129}[]{#_Toc335818130}[]{#_Toc335818131}[]{#_Toc335818132}[]{#_Toc335818133}[]{#_Toc335818134}[]{#_Toc335818135}[]{#_Toc335818136}[]{#_Toc335818137}[]{#_Toc335818138}[]{#_Toc335818139}[]{#_Toc335818140}[]{#_Toc335818141}[]{#_Toc335818142}[]{#_Toc335818143}[]{#_Toc335818144}[]{#_Toc335818145}[]{#_Toc335818146}[]{#_Toc335818147}[]{#_Toc335818148}[]{#_Toc335818149}[]{#_Toc335818150}[]{#_Toc335818151}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address notification mac-move**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_2128680216}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_x35641438}
:::

[ ]{lang="EN-US"}

[**[mac-address notification mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_1034756133}[命令用来开启]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移上报功能。]{style="font-family:宋体"}

[**[undo mac-address notification mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_x2117850233}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128483608}

[**[mac-address notification mac-move ]{lang="EN-US"}**[\[ **interval** *interval-value* \]]{lang="EN-US"}]{#struct_0_65355_x2050_1383103791}

[**[undo mac-address notification mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_x1462713415}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x767247232}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_2128549144}[地址迁移上报功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1483751673}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_1598155699}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1624656299}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_2128876824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_719469859}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x188711624}

[**[interval]{lang="EN-US"}***[ interval-value]{lang="EN-US"}*]{#struct_0_65355_x2050_481212842}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移检测周期，单位为分钟，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[。如果未指定该参数，将采用缺省]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移检测周期]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2068027680}

[[开启]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x188711627}[地址迁移上报功能后，当系统检测到地址迁移，会显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移日志，包括]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所在]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移源接口和新接口，以及该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移检测周期内的迁移次数。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65355_x2050_2128942360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令后，必须同时通过]{lang="EN-US" style="font-family:宋体"}**[snmp-agent trap enable mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_x820637882}[命令开启]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的告警功能，系统才会显示]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移日志]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启]{style="font-family:宋体"}]{#struct_0_65355_x2050_x188711626}[MAC]{lang="EN-US"}[地址迁移上报功能后，系统按照]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移检测周期的间隔显示上一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移检测周期内发生的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移日志。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_65355_x2050_x188711629}[MAC]{lang="EN-US"}[地址迁移检测周期内，最多能显示]{style="font-family:宋体"}[20]{lang="EN-US"}[条最新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的迁移日志；新发生的迁移日志会覆盖最旧的日志，旧的日志信息将丢弃。（集中式设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_65355_x2050_480360874}[MAC]{lang="EN-US"}[地址迁移检测周期内，每台成员设备最多能显示]{style="font-family:宋体"}[20]{lang="EN-US"}[条最新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的迁移日志；新发生的迁移日志会覆盖最旧的日志，旧的日志信息将丢弃。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_65355_x2050_x188711628}[MAC]{lang="EN-US"}[地址迁移检测周期内，每个单板最多能显示]{style="font-family:宋体"}[20]{lang="EN-US"}[条最新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的迁移日志。新发生的迁移日志会覆盖最旧的日志，旧的日志信息将丢弃。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x701213363}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x796230626}[开启]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移上报功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_2128811288}

[\[Sysname\] mac-address notification mac-move]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[%May 14 17:16:45:688 2013 H3C MAC/4/MAC_FLAPPING: MAC address 0000-0012-0034 in VLAN 500 has moved from port GE1/0/1 to port GE1/0/2 for 1 times]{lang="EN-US"}

[[以上显示信息表明：]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x188711633}[地址]{style="font-family:宋体"}[0000-0012-0034]{lang="EN-US"}[所在]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[500]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移源接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移新接口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移检测周期内的迁移次数为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_883479267}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-address mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_x1220012080}
:::::

::::: {#-378975656 .myid}
[]{#_Toc404783978}[]{#struct_0_65355_x2050_x188711632}[]{#_Toc356979408}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address notification mac-move suppression (interface view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_692243408}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_1700348787}
:::

[ ]{lang="EN-US"}

[**[mac-address notification mac-move suppression]{lang="EN-US"}**]{#struct_0_65355_x2050_356239580}[命令用来开启当前接口上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移抑制功能。]{style="font-family:宋体"}

[**[undo mac-address notification mac-move suppression]{lang="EN-US"}**]{#struct_0_65355_x2050_2129204504}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_14177457}

[**[mac-address notification mac-move suppression]{lang="EN-US"}**]{#struct_0_65355_x2050_x2145026763}

[**[undo mac-address notification mac-move suppression]{lang="EN-US"}**]{#struct_0_65355_x2050_1541435950}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128614677}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_1180194104}[地址迁移抑制功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2144881087}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65355_x2050_x2145026765}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128680213}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x35838046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_457634350}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1203403340}

[[开启]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x2145026767}[地址迁移抑制功能后，当监测到一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移检测周期内某个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址从某端口上迁移出或者迁移到该端口的次数超过]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移抑制的检测阈值，则将该端口]{style="font-family:宋体"}[down]{lang="EN-US"}[，用户可以执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[将该端口恢复，也可以等]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移抑制时间间隔后让该端口自行恢复]{style="font-family:宋体"}[up]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1296886574}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_2128549141}[开启]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x2145026769}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mac-address notification mac-move suppression]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x934170481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address notification mac-move suppression]{lang="EN-US"}**[ (system view)]{lang="EN-US"}]{#struct_0_65355_x2050_x2145026768}
:::::

::: {#-1408478237 .myid}
[]{#_Toc404783979}[]{#struct_0_65355_x2050_631913460}[]{#_Toc396988540}[]{#_Toc396985788}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address notification mac-move suppression (system view)**

------------------------------------------------------------------------

[**[mac-address notification mac-move suppression]{lang="EN-US"}**]{#struct_0_65355_x2050_x571048649}[命令用来配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移抑制功能的相关参数。]{style="font-family:宋体"}

[**[undo mac-address notification mac-move suppression]{lang="EN-US"}**]{#struct_0_65355_x2050_x530096962}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x394004362}

[**[mac-address notification mac-move suppression]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **interval** *interval-value* \| **threshold** *threshold-value* }]{lang="EN-US"}]{#struct_0_65355_x2050_x571048648}

[**[undo mac-address notification mac-move suppression]{lang="EN-US"}**[ { **interval** \| **threshold** }]{lang="EN-US"}]{#struct_0_65355_x2050_x530162498}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x571048651}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x529572673}[地址迁移抑制功能的相关参数未配置，采用缺省抑制时间间隔]{style="font-family:宋体"}[30]{lang="EN-US"}[秒和缺省阈值]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x571048650}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_x529638209}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x571048653}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x529703745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x571048652}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x529769281}

[**[interval]{lang="EN-US"}***[ interval-value]{lang="EN-US"}*]{#struct_0_65355_x2050_47913717}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移抑制时间间隔（检测攻击后，端口保持]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的持续时间），单位为秒，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[。如果未指定该参数，将采用缺省抑制时间间隔]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}***[ threshold-value]{lang="EN-US"}*]{#struct_0_65355_x2050_x571048655}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移抑制的检测阈值（一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移检测周期内允许]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移的最大的迁移次数），取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。如果未指定该参数，将采用缺省阈值]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x529310529}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[配置本命令后，当]{style="font-family:宋体"}]{#struct_0_65355_x2050_x571048654}[接口上开启了]{style="font-family:宋体"}[MAC]{lang="SV"}[地址迁移抑制功能时，本命令配置的参数才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令可多次配置，配置]{lang="EN-US" style="font-family:宋体"}**[interval]{lang="EN-US"}***[ interval-value]{lang="EN-US"}*]{#struct_0_65355_x2050_x571048657}[和]{lang="EN-US" style="font-family:宋体"}**[threshold]{lang="EN-US"}***[ threshold-value]{lang="EN-US"}*[时互不影响]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x529441601}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x1077316110}[配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移抑制功能的抑制间隔为]{style="font-family:宋体"}[40s]{lang="EN-US"}[，检测阈值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x571048656}

[\[Sysname\] mac-address notification mac-move suppression interval 40]{lang="EN-US"}

[\[Sysname\] mac-address notification mac-move suppression threshold 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1767603511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address notification mac-move suppression]{lang="EN-US"}**[ (interface view)]{lang="EN-US"}]{#struct_0_65355_x2050_345354587}
:::

::: {#-860388654 .myid}
[]{#_Toc404783980}[]{#struct_0_65355_x2050_x1999878344}

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address timer**

------------------------------------------------------------------------

[**[mac-address timer]{lang="EN-US"}**]{#struct_0_65355_x2050_x640273143}[命令用来配置动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的老化时间。]{style="font-family:宋体"}

[**[undo mac-address timer]{lang="EN-US"}**]{#struct_0_65355_x2050_x1917412340}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x518129855}

[**[mac-address timer ]{lang="EN-US"}**[{ **aging** *seconds* \| **no-aging** }]{lang="EN-US"}]{#struct_0_65355_x2050_826016337}

[**[undo mac-address timer]{lang="EN-US"}**]{#struct_0_65355_x2050_2128876821}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_719666467}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_65355_x2050_x1218506646}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_53735977}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_x647205934}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x357256487}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1472935485}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_x1280667207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x754762080}

[**[aging]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_65355_x2050_2128942357}[：动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的老化时间，单位为秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[no-aging]{lang="EN-US"}**]{#struct_0_65355_x2050_x820965561}[：不老化。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1633985510}

[[当网络拓扑改变后，动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_x1257321237}[地址表项不会及时自动更新。这样，由于设备学习不到新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，会导致用户流量不能正常转发。因此，需要配置动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项老化时间。超出设定的老化时间，动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项被自动删除，设备重新进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习，构建新的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[用户配置的老化时间过长或者过短，都可能影响设备的运行性能：]{style="font-family:宋体"}]{#struct_0_65355_x2050_1663209424}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户配置的老化时间过长，设备可能会保存许多过时的]{style="font-family:宋体"}]{#struct_0_65355_x2050_x1926749234}[MAC]{lang="EN-US"}[地址表项，从而耗尽]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表资源，导致设备无法根据网络的变化更新]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户配置的老化时间太短，设备可能会删除有效的]{style="font-family:宋体"}]{#struct_0_65355_x2050_x420969202}[MAC]{lang="EN-US"}[地址表项，可能导致设备广播大量的数据报文，影响设备的运行性能。]{style="font-family:宋体"}

[[所以用户需要根据实际情况，配置合适的老化时间来有效的实现]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_1593973552}[地址老化功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1589904969}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_2128745749}[配置动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的老化时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_1950730611}

[\[Sysname\] mac-address timer aging 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x661183311}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mac-address aging-time]{lang="EN-US"}**]{#struct_0_65355_x2050_875069072}
:::

::: {#1348826561 .myid}
[]{#_Toc404783981}[]{#struct_0_65355_x2050_759512693}[]{#_Toc356979411}

**MAC地址表 \-- MAC地址表配置命令 \-- snmp-agent trap enable mac-address**

------------------------------------------------------------------------

[**[snmp-agent trap enable mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_1433020474}[命令用来开启]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的告警功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[snmp-agent trap enable mac-address]{lang="EN-US"}**]{#struct_0_65355_x2050_2128811285}[命令用来关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1590715654}

[**[snmp-agent trap enable mac-address ]{lang="EN-US"}**[\[ **mac-move** \]]{lang="EN-US"}]{#struct_0_65355_x2050_x968706843}

[**[undo ]{lang="EN-US"}[snmp-agent trap enable mac-address ]{lang="EN-US"}**[\[ **mac-move** \]]{lang="EN-US"}]{#struct_0_65355_x2050_1017371909}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2129138965}

[[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_692964304}[地址表的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1234531074}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_2129204501}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_13980849}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1904155484}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1795189450}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128614678}

[**[mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_1179342136}[：打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表模块的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移上报的告警功能。如果未指定该参数，则表示打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址模块所有的告警功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_702291555}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_65355_x2050_1416281455}[MAC]{lang="EN-US"}[地址表的告警功能关闭后，将采用]{style="font-family:宋体"}[Syslog]{lang="EN-US"}[方式上报信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目前]{style="font-family:宋体"}]{#struct_0_65355_x2050_401948065}[MAC]{lang="EN-US"}[地址表模块仅有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移上报的告警功能，所以打开或关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移上报的告警功能，就相当于打开或关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表所有的告警功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128680214}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x35510366}[配置采用]{style="font-family:宋体"}[Syslog]{lang="EN-US"}[方式上报]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址迁移。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1586916305}

[\[Sysname\] undo snmp-agent trap enable mac-address mac-move]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_616186223}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[mac-address notification mac-move]{lang="EN-US"}**]{#struct_0_65355_x2050_2128483606}

[ ]{lang="EN-US"}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::::: {#1420138091 .myid}
[]{#_Toc404783984}[]{#struct_0_65355_x2050_974285059}[]{#_Toc320103652}

**MAC Information \-- MAC Information配置命令 \-- mac-address information enable (interface view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_79716958}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_x1630240177}
:::

**[ ]{lang="EN-US"}**

[**[mac-address information enable]{lang="EN-US"}**]{#struct_0_65355_x2050_x399853185}[命令用来使能当前接口的]{style="font-family:
宋体"}[MAC Information]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo mac-address information enable]{lang="EN-US"}**]{#struct_0_65355_x2050_2128549142}[命令用来关闭当前接口的]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1483882745}

[**[mac-address information enable ]{lang="EN-US"}**[{ **added** \| **deleted** }]{lang="EN-US"}]{#struct_0_65355_x2050_x367948488}

[**[undo mac-address information enable ]{lang="EN-US"}**[{ **added** \| **deleted** }]{lang="EN-US"}]{#struct_0_65355_x2050_x1270383399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_503657580}

[[接口的]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}]{#struct_0_65355_x2050_x1023296139}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x204809079}

[[二层以太网接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}]{#struct_0_65355_x2050_x1363080362}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1838936753}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_2128876822}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_719600931}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x755948109}

[**[added]{lang="EN-US"}**]{#struct_0_65355_x2050_x1115056187}[：表示配置接口在学习到新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时记录]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化信息。本参数的支持情况与设备的型号相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[deleted]{lang="EN-US"}**]{#struct_0_65355_x2050_x1039323960}[：表示配置接口在删除]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时记录]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化信息。本参数的支持情况与设备的型号相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_650350347}

[[必须同时使能全局和接口的]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}]{#struct_0_65355_x2050_x1956278017}[功能，]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x23324469}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x569831556}[使能端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[功能，使端口在学习到新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[时记录]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_2128942358}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_65355_x2050_x820113593}

[[\[Sysname-GigabitEthernet1/0/1\] mac-address information enable added]{lang="EN-US"}]{#struct_0_65355_x2050_844914335}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_405137638}[使能]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channel1/1:10]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[功能，使接口在学习到新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[时记录]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x185838507}

[[\[Sysname\] interface s-channel 1/1:10]{lang="EN-US"}]{#struct_0_65355_x2050_1186373782}

[[\[Sysname-S-Channel1/1:10\] mac-address information enable added]{lang="EN-US"}]{#struct_0_65355_x2050_x946666766}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x27765264}[使能]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:2]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[功能，使接口在学习到新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[时记录]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_1362291707}

[[\[Sysname\] interface schannel-aggregation 1:2]{lang="EN-US"}]{#struct_0_65355_x2050_2128745750}

[[\[Sysname-Schannel-Aggregation1:2\] mac-address information enable added]{lang="EN-US"}]{#struct_0_65355_x2050_1950140786}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1664230634}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address information enable]{lang="EN-US"}**[ (system view)]{lang="EN-US"}]{#struct_0_65355_x2050_x900180980}
:::::

::::: {#1180694607 .myid}
[]{#_Toc404783985}[]{#struct_0_65355_x2050_566816983}[]{#_Toc320103653}[]{#_Toc309722348}[]{#_Toc316493498}[]{#_Toc316550358}

**MAC Information \-- MAC Information配置命令 \-- mac-address information enable (system view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_x802352532}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_626788302}
:::

**[ ]{lang="EN-US"}**

[**[mac-address information enable]{lang="EN-US"}**]{#struct_0_65355_x2050_x371550942}[命令用来使能全局]{style="font-family:
宋体"}[MAC Information]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo mac-address information enable]{lang="EN-US"}**]{#struct_0_65355_x2050_772145764}[命令用来关闭全局]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_2128811286}

[**[mac-address information enable]{lang="EN-US"}**]{#struct_0_65355_x2050_x1590519046}

[**[undo mac-address information enable]{lang="EN-US"}**]{#struct_0_65355_x2050_x1416847843}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1946030328}

[[全局]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}]{#struct_0_65355_x2050_x1588182056}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1818667084}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_1078163846}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1263118727}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1497214675}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_2129138966}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_692898768}

[[必须同时使能全局和接口的]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}]{#struct_0_65355_x2050_1298834015}[功能，]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1690818032}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x673652286}[使能全局]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_1322314750}

[[\[Sysname\] mac-address information enable]{lang="EN-US"}]{#struct_0_65355_x2050_x1288150636}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1256604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address information enable]{lang="EN-US"}**[ (interface view)]{lang="EN-US"}]{#struct_0_65355_x2050_847520413}
:::::

::::: {#-237821170 .myid}
[]{#_Toc404783986}[]{#struct_0_65355_x2050_2129204502}[]{#_Toc320103654}[]{#_Toc309722349}

**MAC Information \-- MAC Information配置命令 \-- mac-address information interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_13784241}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_1268971442}
:::

**[ ]{lang="EN-US"}**

[**[mac-address information interval]{lang="EN-US"}**]{#struct_0_65355_x2050_1824245572}[命令用来配置发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知的时间间隔。]{style="font-family:宋体"}

[**[undo mac-address information interval]{lang="EN-US"}**]{#struct_0_65355_x2050_x591800750}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_880486053}

[**[mac-address information interval ]{lang="EN-US"}***[interval-time]{lang="EN-US"}*]{#struct_0_65355_x2050_x715899270}

[**[undo mac-address information interval]{lang="EN-US"}**]{#struct_0_65355_x2050_x539294884}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1348276092}

[[发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_2128614675}[变化通知的时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1180063032}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_x934083880}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1780722110}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_791667297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1490682176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x115839186}

[*[interval-time]{lang="EN-US"}*]{#struct_0_65355_x2050_1450050406}[：发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x849795823}

[[为了防止过于频繁发送的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_65355_x2050_2128680211}[变化通知干扰用户，可以将此时间间隔调整为较大值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x35706974}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x133488162}[配置设备发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知的时间间隔为]{style="font-family:宋体"}[200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x681670799}

[[\[Sysname\] mac-address information interval 200]{lang="EN-US"}]{#struct_0_65355_x2050_x345946828}
:::::

::::: {#-457996129 .myid}
[]{#_Toc404783987}[]{#struct_0_65355_x2050_x857713137}[]{#_Toc320103657}[]{#_Toc309722350}[]{#_Toc320103655}[]{#_Toc320103656}[]{#_Toc316493501}[]{#_Toc316550361}

**MAC Information \-- MAC Information配置命令 \-- mac-address information mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_347575518}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_x1788638607}
:::

**[ ]{lang="EN-US"}**

[**[mac-address information mode]{lang="EN-US"}**]{#struct_0_65355_x2050_x1441487684}[命令用来配置发送]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[变化通知的方式。]{style="font-family:宋体"}

[**[undo mac-address information mode]{lang="EN-US"}**]{#struct_0_65355_x2050_2128483603}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1203796556}

[**[mac-address information mode]{lang="EN-US"}**[ { **syslog** \| **trap** }]{lang="EN-US"}]{#struct_0_65355_x2050_x967556158}

[**[undo mac-address information mode]{lang="EN-US"}**]{#struct_0_65355_x2050_1625283788}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1555459606}

[[采用]{style="font-family:宋体"}[Trap]{lang="EN-US"}]{#struct_0_65355_x2050_x1459913649}[方式发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_956646977}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_488849585}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1922148863}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_2128549139}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1484603634}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x87948654}

[**[syslog]{lang="EN-US"}**]{#struct_0_65355_x2050_x1297039835}[：表示采用]{style="font-family:宋体"}[Syslog]{lang="EN-US"}[方式发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知。]{style="font-family:宋体"}

[**[trap]{lang="EN-US"}**]{#struct_0_65355_x2050_245510956}[：表示采用]{style="font-family:宋体"}[Trap]{lang="EN-US"}[方式发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1573144678}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_x1110833320}[配置设备采用]{style="font-family:宋体"}[Trap]{lang="EN-US"}[方式发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x1370442470}

[[\[Sysname\] mac-address information mode trap]{lang="EN-US"}]{#struct_0_65355_x2050_x926479957}
:::::

::::: {#-874997510 .myid}
[]{#_Toc404783988}[]{#struct_0_65355_x2050_2128876819}[]{#_Toc320103660}[]{#_Toc309722351}[]{#_Toc320103658}[]{#_Toc320103659}

**MAC Information \-- MAC Information配置命令 \-- mac-address information queue-length**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_65355_x2050_720190754}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65355_x2050_881027354}
:::

**[ ]{lang="EN-US"}**

[**[mac-address information queue-length]{lang="EN-US"}**]{#struct_0_65355_x2050_x1071398629}[命令用来配置]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[缓存队列长度。]{style="font-family:宋体"}

[**[undo mac-address information queue-length]{lang="EN-US"}**]{#struct_0_65355_x2050_611739589}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1055439659}

[**[mac-address information queue-length ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_65355_x2050_463495699}

[**[undo mac-address information queue-length]{lang="EN-US"}**]{#struct_0_65355_x2050_237704593}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x60717478}

[[MAC Information]{lang="EN-US"}]{#struct_0_65355_x2050_2128942355}[缓存队列长度为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x820834489}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65355_x2050_874983288}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65355_x2050_794260776}

[[network-admin]{lang="EN-US"}]{#struct_0_65355_x2050_643293729}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65355_x2050_1238800995}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1308103706}

[*[value]{lang="EN-US"}*]{#struct_0_65355_x2050_x1033392336}[：]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[缓存队列长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，表示可存放的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化信息条数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65355_x2050_x1675210458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}[MAC Information]{lang="EN-US"}]{#struct_0_65355_x2050_x928003816}[缓存队列长度为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[，则当接口学习到或删除掉一条]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时会立即发送日志或]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_65355_x2050_2128745747}[MAC Information]{lang="EN-US"}[缓存队列长度不为]{style="font-family:宋体"}[0]{lang="EN-US"}[，则将]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化信息存放在缓存队列中。当未达到发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知的时间间隔，此时若缓存队列被写满，新的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化信息将覆盖缓存队列中最后一条写入的信息；当达到发送]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化通知的时间间隔时，不论此时缓存队列是否已被写满，都发送日志或]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65355_x2050_1949813107}

[[\# ]{lang="EN-US"}]{#struct_0_65355_x2050_590794291}[配置]{style="font-family:宋体"}[MAC Information]{lang="EN-US"}[缓存队列长度为]{style="font-family:宋体"}[600]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65355_x2050_x650041174}

[[\[Sysname\] mac-address information queue-length 600]{lang="EN-US"}]{#struct_0_65355_x2050_x615678712}

[ ]{lang="EN-US"}
:::::
