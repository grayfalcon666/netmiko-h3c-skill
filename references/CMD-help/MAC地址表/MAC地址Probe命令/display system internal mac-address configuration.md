::: {#-1387032752 .myid}
[]{#_Toc404799803}[]{#struct_0_85056_90704_757463968}

**MAC地址表 \-- MAC地址Probe命令 \-- display system internal mac-address configuration**

------------------------------------------------------------------------

[**[display system internal mac-address configuration]{lang="EN-US"}**]{#struct_0_85056_90704_1543045343}[命令用来显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85056_90704_1432282632}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_85056_90704_1215233680}

[**[display system internal mac-address configuration ]{lang="EN-US"}**[{ **blackhole \| multiport \| multicast \| static** } \[ **count** \]]{lang="EN-US"}]{#struct_0_85056_90704_x807032946}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_85056_90704_x432601276}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mac-address configuration ]{lang="EN-US"}**[{ **blackhole \| multiport \| multicast \| static** } \[ **count** \] **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu**]{lang="EN-US"}*[ cpu-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}]{#struct_0_85056_90704_x1888457157}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_85056_90704_857729366}[模式：]{style="font-family:宋体"}

[**[display system internal mac-address configuration ]{lang="EN-US"}**[{ **blackhole \| multiport \| multicast \| static** } \[ **count** \] **chassis** *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**]{#struct_0_85056_90704_x1732066450}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu**]{lang="EN-US"}*[ cpu-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85056_90704_1029291180}

[[Probe]{lang="EN-US"}]{#struct_0_85056_90704_1728555189}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85056_90704_757529504}

[[network-admin]{lang="EN-US"}]{#struct_0_85056_90704_309950739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85056_90704_1972618532}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85056_90704_1684901866}

[**[blackhole]{lang="EN-US"}**]{#struct_0_85056_90704_x979440917}[：显示黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[multiport]{lang="EN-US"}**]{#struct_0_85056_90704_1566442110}[：显示多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_85056_90704_x1869202306}[：显示组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_85056_90704_2001196696}[：显示静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_85056_90704_999555141}[：显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量。如果配置本参数，将仅显示符合条件的（由]{style="font-family:宋体"}**[count]{lang="EN-US"}**[前面的参数决定）]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量，而不显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体内容。如果不指定本参数，则显示符合条件的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的具体内容。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x1348861544}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_757857184}[：显示指定成员设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x1829492549}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x374167970}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x817702797}[：显示指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_85056_90704_1248496452}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::::: {#-1004144120 .myid}
[]{#_Toc404799804}[]{#struct_0_85056_90704_24739943}

**MAC地址表 \-- MAC地址Probe命令 \-- display system internal mac-address learned**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MAC地址表Probe命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_85056_90704_156366668}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_85056_90704_x1250291917}
:::

**[ ]{lang="EN-US"}**

[**[display system internal mac-address learned]{lang="EN-US"}**]{#struct_0_85056_90704_x1025555663}[命令用来显示动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85056_90704_x332498814}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_85056_90704_x803502230}

[**[display system internal mac-address learned ]{lang="EN-US"}**[\[ *mac-address* \[ **vlan** *vlan-id* \] \| \[ **interface** *interface-type interface-number* \] \[ **vlan** *vlan-id* \] \[ **count** \] \]]{lang="EN-US"}]{#struct_0_85056_90704_x543356916}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_85056_90704_24739942}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mac-address learned]{lang="EN-US"}**[ \[ *mac*-*address* \[ **vlan** *vlan-id* \] \| \[ **interface** *interface-type interface-number* \] \[ **vlan** *vlan-id* \] \[ **count** \] \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_85056_90704_x1799948468}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_85056_90704_x403615083}[模式：]{style="font-family:宋体"}

[**[display system internal mac-address learned]{lang="EN-US"}**[ \[ *mac*-*address* \[ **vlan** *vlan-id* \] \| \[ **interface** *interface-type interface-number* \] \[ **vlan** *vlan-id* \] \[ **count** \] \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_85056_90704_978532531}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85056_90704_1486085282}

[[Probe]{lang="EN-US"}]{#struct_0_85056_90704_x650199439}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85056_90704_905585219}

[[network-admin]{lang="EN-US"}]{#struct_0_85056_90704_x1997645214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85056_90704_x1824226061}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85056_90704_355965098}

[*[mac]{lang="EN-US"}*[-*address*]{lang="EN-US"}]{#struct_0_85056_90704_24739945}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项，]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[-*address*]{lang="EN-US"}[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan]{lang="EN-US"}*[-*id*]{lang="EN-US"}]{#struct_0_85056_90704_1303377740}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id*]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_85056_90704_2087158234}[：显示指定接口的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_85056_90704_x1447836235}[：显示动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量。如果配置本参数，将仅显示符合条件的（由]{style="font-family:宋体"}**[count]{lang="EN-US"}**[前面的参数决定）动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的数量，而不显示动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体内容。如果不指定本参数，则显示符合条件的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的具体内容。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_2124423664}[：显示指定]{style="font-family:宋体"}[单板的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x518879822}[：显示指定成员设备的]{style="font-family:宋体"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x666693135}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_827851615}[：显示指定成员设备上指定单板的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_900628309}[：显示指定单板的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_85056_90704_x1593636376}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::

::: {#2017344442 .myid}
[]{#_Toc404799805}[]{#struct_0_85056_90704_1695029097}

**MAC地址表 \-- MAC地址Probe命令 \-- display system internal mac-address protocol**

------------------------------------------------------------------------

[**[display system internal mac-address protocol]{lang="EN-US"}**]{#struct_0_85056_90704_1126260373}[命令用来显示指定协议或特性生成的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85056_90704_x652937396}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_85056_90704_834781879}

[**[display system internal mac-address protocol ]{lang="EN-US"}**[\[ **auth** \| **dot1x** \| **ead** \| **evb** \| **security** \| **vlan-interface** \| **voice-vlan** \]]{lang="EN-US"}]{#struct_0_85056_90704_1284965176}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_85056_90704_1200078165}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mac-address protocol ]{lang="EN-US"}**[\[ **auth** \| **dot1x** \| **ead** \| **evb** \| **security** \| **vlan-interface** \| **voice-vlan** \] **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_85056_90704_2000668872}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_85056_90704_x1731412858}[模式：]{style="font-family:宋体"}

[**[display system internal mac-address protocol]{lang="EN-US"}**[ \[ **auth** \| **dot1x** \| **ead** \| **evb** \| **security** \| **vlan-interface** \| **voice-vlan** \] **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_85056_90704_762662066}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85056_90704_695540017}

[[Probe]{lang="EN-US"}]{#struct_0_85056_90704_x536410353}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85056_90704_24739947}

[[network-admin]{lang="EN-US"}]{#struct_0_85056_90704_921040716}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85056_90704_1385207522}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85056_90704_998692227}

[**[auth]{lang="EN-US"}**]{#struct_0_85056_90704_1126260378}[：显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证特性的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[dot1x]{lang="EN-US"}**]{#struct_0_85056_90704_1626406741}[：显示]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[特性的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[ead]{lang="EN-US"}**]{#struct_0_85056_90704_1870154273}[：显示]{style="font-family:宋体"}[EAD]{lang="EN-US"}[特性的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[evb]{lang="EN-US"}**]{#struct_0_85056_90704_x1946810537}[：显示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[特性的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[security]{lang="EN-US"}**]{#struct_0_85056_90704_x1812974557}[：显示端口安全特性中学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[vlan-interface]{lang="EN-US"}**]{#struct_0_85056_90704_406514417}[：显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[voice-vlan]{lang="EN-US"}**]{#struct_0_85056_90704_24739946}[：显示]{style="font-family:宋体"}[Voice VLAN]{lang="EN-US"}[特性的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x1035274420}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_1863507241}[：显示指定成员设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_496106279}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_1694729058}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x1882118136}[：显示指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_85056_90704_339820243}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-71991714 .myid}
[]{#_Toc404799806}[]{#struct_0_85056_90704_x974516365}[]{#_Toc361303267}[]{#_Toc361303330}[]{#_Toc361303268}[]{#_Toc361303331}[]{#_Toc361303269}[]{#_Toc361303332}[]{#_Toc361303270}[]{#_Toc361303333}[]{#_Toc361303271}[]{#_Toc361303334}[]{#_Toc361303272}[]{#_Toc361303335}[]{#_Toc361303273}[]{#_Toc361303336}[]{#_Toc361303274}[]{#_Toc361303337}[]{#_Toc361303290}[]{#_Toc361303353}

**MAC地址表 \-- MAC地址Probe命令 \-- display system internal mac-address statistics**

------------------------------------------------------------------------

[**[display system internal mac-address statistics]{lang="EN-US"}**]{#struct_0_85056_90704_757332897}[命令用来显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85056_90704_539981388}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_85056_90704_x1516967832}

[**[display system internal mac-address statistics]{lang="EN-US"}**]{#struct_0_85056_90704_736788024}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_85056_90704_x560383150}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mac-address statistics slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu**]{lang="EN-US"}*[ cpu-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}]{#struct_0_85056_90704_24084174}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_85056_90704_x723029599}[模式：]{style="font-family:宋体"}

[**[display system internal mac-address statistics chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**]{#struct_0_85056_90704_1093409247}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu**]{lang="EN-US"}*[ cpu-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85056_90704_897138354}

[[Probe]{lang="EN-US"}]{#struct_0_85056_90704_627229584}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85056_90704_757398433}

[[network-admin]{lang="EN-US"}]{#struct_0_85056_90704_52227794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85056_90704_1353596185}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85056_90704_x660838188}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_163544311}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_1763281202}[：显示指定成员设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x1069977662}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_1385351336}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_1658905693}[：显示指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_85056_90704_1296074912}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1329644738 .myid}
[]{#_Toc404799807}[]{#struct_0_85056_90704_1503861864}[]{#_Toc361303292}[]{#_Toc361303355}[]{#_Toc361303293}[]{#_Toc361303356}[]{#_Toc361303294}[]{#_Toc361303357}[]{#_Toc361303295}[]{#_Toc361303358}[]{#_Toc361303296}[]{#_Toc361303359}[]{#_Toc361303297}[]{#_Toc361303360}[]{#_Toc361303298}[]{#_Toc361303361}[]{#_Toc361303299}[]{#_Toc361303362}[]{#_Toc361303300}[]{#_Toc361303363}[]{#_Toc361303301}[]{#_Toc361303364}[]{#_Toc361303302}[]{#_Toc361303365}[]{#_Toc361303303}[]{#_Toc361303366}[]{#_Toc361303325}[]{#_Toc361303388}

**MAC地址表 \-- MAC地址Probe命令 \-- reset system internal mac-address statistics**

------------------------------------------------------------------------

[**[reset system internal mac-address statistics]{lang="EN-US"}**]{#struct_0_85056_90704_1223333762}[命令用来清除]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的统计信息]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_85056_90704_2019070418}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_85056_90704_x2130184027}

[**[reset system internal mac-address statistics]{lang="EN-US"}**]{#struct_0_85056_90704_1984798491}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_85056_90704_x1037249998}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal mac-address statistics]{lang="EN-US"}[ slot]{lang="EN-US"}**]{#struct_0_85056_90704_256252371}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu**]{lang="EN-US"}*[ cpu-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_85056_90704_x65690305}[模式：]{style="font-family:宋体"}

[**[reset system internal mac-address statistics chassis]{lang="EN-US"}**[ *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**]{#struct_0_85056_90704_969118999}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu**]{lang="EN-US"}*[ cpu-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_85056_90704_757660577}

[[Probe]{lang="EN-US"}]{#struct_0_85056_90704_x996116438}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_85056_90704_2036797143}

[[network-admin]{lang="EN-US"}]{#struct_0_85056_90704_x292640082}

[[mdc-admin]{lang="EN-US"}]{#struct_0_85056_90704_x865720721}

[[【参数】]{style="font-family:黑体"}]{#struct_0_85056_90704_x773447319}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x1644213882}[：清除指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_1941430958}[：清除指定成员设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_92821752}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_393429837}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_85056_90704_x1283412059}[：清除指定单板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_85056_90704_1296205984}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::
