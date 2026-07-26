::: {#-412572145 .myid}
[]{#_Toc404786528}[]{#struct_0_90377_14718_1474462807}

**邻接表 \-- IPv4邻接表配置命令 \-- display adjacent-table**

------------------------------------------------------------------------

[**[display adjacent-table]{lang="EN-US"}**]{#struct_0_90377_14718_x200270407}[命令用来显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_90377_14718_2117568944}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_90377_14718_1678941603}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display adjacent-table ]{lang="EN-US"}**[{ **all** \| **physical-interface** *interface-type interface-number* \| **routing-interface** *interface-type interface-number* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] } \[ **count** \| **verbose** \]]{lang="EN-US"}]{#struct_0_90377_14718_1312538436}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_90377_14718_254519641}[模式：]{style="font-family:宋体"}

[**[display adjacent-table ]{lang="EN-US"}**[{ **all** \| **physical-interface** *interface-type interface-number* \| **routing-interface** *interface-type interface-number* \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] } \[ **count** \| **verbose** \]]{lang="EN-US"}]{#struct_0_90377_14718_1262844754}

[[【视图】]{style="font-family:黑体"}]{#struct_0_90377_14718_x1289345741}

[[任意视图]{style="font-family:宋体"}]{#struct_0_90377_14718_425138466}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_90377_14718_x1893253763}

[[network-admin]{lang="EN-US"}]{#struct_0_90377_14718_2139231757}

[[network-operator]{lang="EN-US"}]{#struct_0_90377_14718_1294963642}

[[mdc-admin]{lang="EN-US"}]{#struct_0_90377_14718_2117503408}

[[mdc-operator]{lang="EN-US"}]{#struct_0_90377_14718_1774164726}

[[【参数】]{style="font-family:黑体"}]{#struct_0_90377_14718_541067093}

[**[all]{lang="EN-US"}**]{#struct_0_90377_14718_1285682404}[：显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[**[physical-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_90377_14718_x1524527622}[：显示指定物理接口上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[**[routing-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_90377_14718_57449952}[：显示指定路由接口上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_90377_14718_x974924355}[：显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，只能为]{style="font-family:宋体"}[0]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_90377_14718_723834189}[：显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_90377_14718_523536034}[：显示指定成员设备的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_90377_14718_347497758}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_90377_14718_2117437872}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_90377_14718_x267160979}[：显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_90377_14718_x911240970}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_90377_14718_2097180098}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的数目。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_90377_14718_588336082}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_90377_14718_2016831123}

[[\# ]{lang="EN-US"}]{#struct_0_90377_14718_1165198083}[显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display adjacent-table all verbose]{lang="EN-US"}]{#struct_0_90377_14718_x662458675}

[ IP address                     : 0.0.0.0]{lang="EN-US"}

[ Routing interface             : Pos2/2/0]{lang="EN-US"}

[ ]{lang="EN-US"}[Physical interface            : Pos2/2/0]{lang="PT-BR"}

[ Logical interface             : N/A]{lang="PT-BR"}

[ ]{lang="PT-BR"}[Service type                   : PPP]{lang="EN-US"}

[ Action type                    : Forwarding]{lang="EN-US"}

[ ]{lang="EN-US"}[Link media type                : P2P]{lang="NL-BE"}

[ Slot                             : 1]{lang="NL-BE"}

[ Cpu                              : 0]{lang="NL-BE"}

[ ]{lang="NL-BE"}[VPN index                       : 0]{lang="EN-US"}

[ ]{lang="NL-BE"}[Virtual circuit information : N/A]{lang="EN-US"}

[ Link head information(IP)    : ff030021]{lang="EN-US"}

[ Link head information(MPLS) : ff030281]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_90377_14718_2117372336}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display adjacent-table slot 1]{lang="EN-US"}]{#struct_0_90377_14718_x1758785844}

[IP address       Routing interface     Physical interface    Type]{lang="EN-US"}

[0.0.0]{lang="EN-US"}[.0          Pos2/2/0                 Pos2/2/0                PPP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_90377_14718_x764266957}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的数目。]{style="font-family:宋体"}

[[\<Sysname\> display adjacent-table slot 1 count]{lang="EN-US"}]{#struct_0_90377_14718_x1511728064}

[ Total entries on slot 1: 1]{lang="EN-US"}

[[以上显示信息表示]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_90377_14718_2016904845}[号单板的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻接表项的数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_90377_14718_x1936668221}[[表1-1 ]{lang="EN-US"}[display adjacent-table]{lang="EN-US"}]{#_Ref133140459}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1463876108}[[字段]{style="font-family:黑体"}]{#struct_0_90377_14718_507647815}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_90377_14718_x1611628622}

[[IP address]{lang="EN-US"}]{#struct_0_90377_14718_2118355376}

[[报文转发下一跳的]{style="font-family:宋体"}]{#struct_0_90377_14718_x806922801}[IP]{lang="EN-US"}[地址（对于]{style="font-family:宋体"}[P2P]{lang="EN-US"}[链路，不需要下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址信息，本字段的值填为]{style="font-family:宋体"}[0.0.0]{lang="EN-US"}[.0]{lang="EN-US"}[；对于]{style="font-family:
  宋体"}[NBMA]{lang="EN-US"}[链路，取值]{style="font-family:宋体"}[0.0.0]{lang="EN-US"}[.0]{lang="EN-US"}[表示缺省邻接表，从缺省虚链路转发]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Routing interface]{lang="EN-US"}]{#struct_0_90377_14718_x1943205743}

[[路由出接口]{style="font-family:宋体"}]{#struct_0_90377_14718_x535842591}

[[Physical interface]{lang="EN-US"}]{#struct_0_90377_14718_898026581}

[[路由出接口对应的实际发送报文的物理接口]{style="font-family:宋体"}]{#struct_0_90377_14718_1523439685}

[[Logical interface]{lang="EN-US"}]{#struct_0_90377_14718_2118289840}

[[发送报文的逻辑接口（如果没有此信息，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_90377_14718_1089546395}[）]{style="font-family:宋体"}

[[Service type/Type]{lang="EN-US"}]{#struct_0_90377_14718_x903258098}

[[链路层协议]{style="font-family:宋体"}]{#struct_0_90377_14718_1143182735}[类型，如]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[、]{style="font-family:宋体"}[MTunnel]{lang="EN-US"}[等]{style="font-family:宋体"}

[[Action type]{lang="EN-US"}]{#struct_0_90377_14718_890788480}

[[报文]{style="font-family:宋体"}]{#struct_0_90377_14718_908005607}[处理]{style="font-family:宋体"}[类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_90377_14718_x1133019595}[orwarding]{lang="EN-US"}[：]{style="font-family:宋体"}[表示转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Drop]{lang="EN-US"}]{#struct_0_90377_14718_2117831089}[：表示丢弃]{style="font-family:宋体"}

[[Link ]{lang="EN-US"}]{#struct_0_90377_14718_x595426551}[media type]{lang="NL-BE"}

[[链路介质类型：]{style="font-family:宋体"}]{#struct_0_90377_14718_x564719777}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2P]{lang="EN-US"}]{#struct_0_90377_14718_x560008918}[：表示点到点链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NBMA]{lang="EN-US"}]{#struct_0_90377_14718_x1434092664}[：表示点对多点链路]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_90377_14718_2117765553}

[[单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_90377_14718_x1374661031}

[[Cpu]{lang="EN-US"}]{#struct_0_90377_14718_1463710356}

[[CPU]{lang="EN-US"}]{#struct_0_90377_14718_946230128}[编号]{style="font-family:宋体"}

[[VPN index]{lang="EN-US"}]{#struct_0_90377_14718_1463906964}

[[VPN]{lang="EN-US"}]{#struct_0_90377_14718_x1005973943}[索引]{style="font-family:宋体"}

[[Virtual circuit information]{lang="EN-US"}]{#struct_0_90377_14718_228238830}

[[虚链路信息，如]{style="font-family:宋体"}]{#struct_0_90377_14718_183158134}[PVC]{lang="EN-US"}[、]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[等（如果没有此信息，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Link head information(IP)]{lang="EN-US"}]{#struct_0_90377_14718_1385865177}

[[IPv4]{lang="EN-US"}]{#struct_0_90377_14718_2117700017}[协议对应的链路层头信息]{style="font-family:宋体"}

[[Link head information(MPLS)]{lang="EN-US"}]{#struct_0_90377_14718_2136275076}

[[MPLS]{lang="EN-US"}]{#struct_0_90377_14718_299155788}[协议对应的链路层头信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1326808850 .myid}
[]{#_Toc404786530}[]{#struct_0_90377_14718_x1180492199}[]{#_Toc325985365}

**邻接表 \-- IPv6邻接表配置命令 \-- display ipv6 adjacent-table**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](邻接表命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US" style="font-size:18.0pt;
color:#0096d6"}]{#struct_0_90377_14718_2033642355}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_90377_14718_2117634481}
:::

[**[display ipv6 adjacent-table]{lang="EN-US"}**]{#struct_0_90377_14718_x600061110}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_90377_14718_x188127975}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_90377_14718_x1920687565}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 adjacent-table ]{lang="EN-US"}**[{ **all** \| **physical-interface** *interface-type interface-number* \| **routing-interface** *interface-type interface-number* \| **slot** *slot-number* \[ **cpu** *cpu-number* \] } \[ **count** \| **verbose** \]]{lang="EN-US"}]{#struct_0_90377_14718_x20805820}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_90377_14718_677483862}[模式：]{style="font-family:宋体"}

[**[display ipv6 adjacent-table ]{lang="EN-US"}**[{ **all** \| **physical-interface** *interface-type interface-number* \| **routing-interface** *interface-type interface-number* \| **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] } \[ **count** \| **verbose** \]]{lang="EN-US"}]{#struct_0_90377_14718_x174427217}

[[【视图】]{style="font-family:黑体"}]{#struct_0_90377_14718_618744197}

[[任意视图]{style="font-family:宋体"}]{#struct_0_90377_14718_999149067}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_90377_14718_2117568945}

[[network-admin]{lang="EN-US"}]{#struct_0_90377_14718_1679007139}

[[network-operator]{lang="EN-US"}]{#struct_0_90377_14718_90078224}

[[mdc-admin]{lang="EN-US"}]{#struct_0_90377_14718_x1288164377}

[[mdc-operator]{lang="EN-US"}]{#struct_0_90377_14718_x890355705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_90377_14718_299598741}

[**[all]{lang="EN-US"}**]{#struct_0_90377_14718_x157958275}[：显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[**[physical-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_90377_14718_1529976769}[：显示指定物理接口上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[**[routing-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_90377_14718_1279609224}[：显示指定路由接口上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_90377_14718_x748283056}[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，只能为]{style="font-family:宋体"}[0]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_90377_14718_2117503409}[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_90377_14718_1774230262}[：显示指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_90377_14718_x862421359}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_90377_14718_x583781046}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_90377_14718_521836002}[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_90377_14718_x910454539}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_90377_14718_975223211}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的数目。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_90377_14718_989878693}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_90377_14718_1670930317}

[[\# ]{lang="EN-US"}]{#struct_0_90377_14718_1442395102}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 adjacent-table all verbose]{lang="EN-US"}]{#struct_0_90377_14718_2117437873}

[ IPv6 address                    : N/A]{lang="EN-US"}

[ Routing interface              : Pos2/2/0]{lang="EN-US"}

[ Physical interface             : Pos2/2/0]{lang="EN-US"}

[ Logical interface              : N/A]{lang="EN-US"}

[ Service type                    : PPP]{lang="EN-US"}

[ Action type                     : Forwarding]{lang="EN-US"}

[ Link media type                : P2P]{lang="EN-US"}

[ Slot                             : 0]{lang="EN-US"}

[ VPN index                       : 0]{lang="EN-US"}

[ Virtual circuit information : N/A]{lang="EN-US"}

[ Link head information(IPv6) : ff030057]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_90377_14718_2097114562}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 adjacent-table slot 1]{lang="EN-US"}]{#struct_0_90377_14718_x174514639}

[IPv6 address          Routing interface     Physical interface    Type]{lang="EN-US"}

[N/A                     Pos2/2/0                Pos2/2/0                PPP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_90377_14718_x1356671797}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的数目。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 adjacent-table slot 1 count]{lang="EN-US"}]{#struct_0_90377_14718_646181514}

[ Total entries on slot 1: 1]{lang="EN-US"}

[[以上显示信息表示]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_90377_14718_1820950098}[号单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻接表项的数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[display ipv6 adjacent-table]{lang="EN-US"}]{#struct_0_90377_14718_x334089534}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1466838218}[[字段]{style="font-family:黑体"}]{#struct_0_90377_14718_1372852717}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_90377_14718_2117372337}

[[IPv6 address]{lang="EN-US"}]{#struct_0_90377_14718_x1758851380}

[[报文转发下一跳的]{style="font-family:宋体"}]{#struct_0_90377_14718_1963193281}[IPv6]{lang="EN-US"}[地址（对于]{style="font-family:宋体"}[P2P]{lang="EN-US"}[链路，不需要下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息，本字段的值填为]{style="font-family:宋体"}[0::0]{lang="EN-US"}[，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[；对于]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[链路，取值]{style="font-family:宋体"}[0::0]{lang="EN-US"}[表示缺省邻接表，从缺省虚链路转发]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Routing interface]{lang="EN-US"}]{#struct_0_90377_14718_x821317258}

[[路由出接口]{style="font-family:宋体"}]{#struct_0_90377_14718_x1887990687}

[[Physical interface]{lang="EN-US"}]{#struct_0_90377_14718_x1358334024}

[[路由出接口对应的实际发送报文的物理接口]{style="font-family:宋体"}]{#struct_0_90377_14718_x1795150806}

[[Logical interface]{lang="EN-US"}]{#struct_0_90377_14718_2118355377}

[[发送报文的逻辑接口（如果没有此信息，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_90377_14718_x806988337}[）]{style="font-family:宋体"}

[[Service type/Type]{lang="EN-US"}]{#struct_0_90377_14718_x447048034}

[[链路层协议]{style="font-family:宋体"}]{#struct_0_90377_14718_556905795}[类型，如]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[、]{style="font-family:宋体"}[MTunnel]{lang="EN-US"}[等]{style="font-family:宋体"}

[[Action type]{lang="EN-US"}]{#struct_0_90377_14718_1414099713}

[[报文]{style="font-family:宋体"}]{#struct_0_90377_14718_1337800033}[处理]{style="font-family:宋体"}[类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Forwarding]{lang="EN-US"}]{#struct_0_90377_14718_2118289841}[：]{style="font-family:宋体"}[表示转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Drop]{lang="EN-US"}]{#struct_0_90377_14718_1089611931}[：]{style="font-family:宋体"}[表示丢弃]{lang="EN-US" style="font-family:宋体"}

[[Link media type]{lang="EN-US"}]{#struct_0_90377_14718_1816849352}

[[链路介质类型：]{style="font-family:宋体"}]{#struct_0_90377_14718_x1896008611}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2P]{lang="EN-US"}]{#struct_0_90377_14718_1883482340}[：表示点到点链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NBMA]{lang="EN-US"}]{#struct_0_90377_14718_x310473292}[：表示点对多点链路]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_90377_14718_2117831086}

[[单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_90377_14718_x594705655}

[[Cpu]{lang="EN-US"}]{#struct_0_90377_14718_1463775893}

[[CPU]{lang="EN-US"}]{#struct_0_90377_14718_x1393714581}[编号]{style="font-family:宋体"}

[[VPN index]{lang="EN-US"}]{#struct_0_90377_14718_1463710357}

[[VPN]{lang="EN-US"}]{#struct_0_90377_14718_946295664}[索引]{style="font-family:宋体"}

[[Virtual circuit information]{lang="EN-US"}]{#struct_0_90377_14718_x963083237}

[[虚链路信息，如]{style="font-family:宋体"}]{#struct_0_90377_14718_x823099854}[PVC]{lang="EN-US"}[、]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[等（如果没有此信息，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Link head information(IPv6)]{lang="EN-US"}]{#struct_0_90377_14718_x1996351006}

[[IPv6]{lang="EN-US"}]{#struct_0_90377_14718_391528331}[协议对应的链路层头信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}
