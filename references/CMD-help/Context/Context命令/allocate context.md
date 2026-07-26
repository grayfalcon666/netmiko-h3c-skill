::::: {#-1111221821 .myid}
[]{#_Toc404783296}[]{#struct_0_10889_x4909_x441677171}[]{#_Toc365648364}

**Context \-- Context命令 \-- allocate context**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:0cm 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_587582090}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_x2142625125}
:::

**[ ]{lang="EN-US"}**

[**[allocate context]{lang="EN-US"}**]{#struct_0_10889_x4909_272447684}[命令用来批量指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo allocate context]{lang="EN-US"}**]{#struct_0_10889_x4909_654327472}[命令用来将]{style="font-family:宋体"}[Context]{lang="EN-US"}[的所属]{style="font-family:宋体"}[MDC]{lang="EN-US"}[恢复为缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x532851804}

[**[allocate]{lang="EN-US"}**[ **context** *start-context-id* **to** *end-context-id*]{lang="EN-US"}]{#struct_0_10889_x4909_287993467}

[**[undo allocate]{lang="EN-US"}**[ **context** *start-context-id* **to** *end-context-id*]{lang="EN-US"}]{#struct_0_10889_x4909_241695138}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1276150456}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1325741293}[属于缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1035622381}

[[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_2079594978}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1633318268}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1209553977}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x2051952985}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_170180380}

[*[start-context-id]{lang="EN-US"}*]{#struct_0_10889_x4909_x365842874}[：]{style="font-family:宋体"}[起始]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。该]{style="font-family:宋体"}[Context]{lang="EN-US"}[必须是已创建、未启动的]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[end-context-id]{lang="EN-US"}*]{#struct_0_10889_x4909_x783545605}[：终止]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}[该]{style="font-family:宋体"}[Context]{lang="EN-US"}[必须是已创建、未启动的]{style="font-family:宋体"}[Context]{lang="EN-US"}[，且]{style="font-family:宋体"}*[end-context-id]{lang="EN-US"}*[必须大于等于]{style="font-family:宋体"}*[start-context-id]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x738882607}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_1272630348}[视图下的]{lang="EN-US" style="font-family:
宋体"}**[allocate context]{lang="EN-US"}**[命令与]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[视图下的]{lang="EN-US" style="font-family:宋体"}**[join mdc]{lang="EN-US"}**[命令功能]{lang="EN-US" style="font-family:宋体"}[相同，]{style="font-family:宋体"}[都是为]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[设置归属]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}**[allocate context]{lang="EN-US"}**[可以]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:宋体"}[Context]{lang="EN-US"}[批量设置归属]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[，]{style="font-family:宋体"}**[join mdc]{lang="EN-US"}**[是]{lang="EN-US" style="font-family:宋体"}[单个]{style="font-family:宋体"}[设置归属]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_x1535626047}**[a]{lang="EN-US"}[llcoate context]{lang="EN-US"}**[命令设置归属]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[时，]{lang="EN-US" style="font-family:宋体"}[系统]{style="font-family:宋体"}[会逐个设置。]{lang="EN-US" style="font-family:宋体"}[如果某个]{style="font-family:宋体"}[Context]{lang="EN-US"}[配置失败，则命令会终止执行，该]{style="font-family:宋体"}[Context]{lang="EN-US"}[之前的]{style="font-family:宋体"}[Context]{lang="EN-US"}[会加入当前]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，该]{style="font-family:宋体"}[Context]{lang="EN-US"}[及其后的]{style="font-family:宋体"}[Context]{lang="EN-US"}[不会加入当前]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1633318267}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x1163099018}[指定]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[到]{style="font-family:
宋体"}[80]{lang="EN-US"}[的]{style="font-family:宋体"}[Context]{lang="EN-US"}[属于名称]{style="font-family:宋体"}[为]{style="font-family:宋体"}[cnt2]{lang="EN-US"}[的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_1317197101}

[\[Sysname\] mdc cnt2]{lang="EN-US"}

[\[Sysname-mdc-2-cnt2\] allocate context 2 to 80]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1933018719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[j]{lang="EN-US"}[oin mdc]{lang="EN-US"}**]{#struct_0_10889_x4909_x2008556210}
:::::

::: {#1546310888 .myid}
[]{#_Toc404783297}[]{#struct_0_10889_x4909_x1672155712}[]{#_Toc359421730}

**Context \-- Context命令 \-- allocate interface**

------------------------------------------------------------------------

[**[allocate interface]{lang="EN-US"}**]{#struct_0_10889_x4909_x739646684}[命令用来为]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配接口。]{style="font-family:宋体"}

[**[undo allocate interface]{lang="EN-US"}**]{#struct_0_10889_x4909_470088102}[命令用来将接口从]{style="font-family:宋体"}[Context]{lang="EN-US"}[中删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1559593499}

[**[allocate interface]{lang="EN-US"}**[ {]{lang="EN-US"}[ *interface-type interface-number* }&\<1-24\> \[ **share** \]]{lang="EN-US"}]{#struct_0_10889_x4909_1500497571}

[**[undo allocate interface]{lang="EN-US"}**[ { *interface-type interface-number* }&\<1-24\>]{lang="EN-US"}]{#struct_0_10889_x4909_108364085}

[**[allocate interface ]{lang="EN-US"}***[interface-type]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_10889_x4909_1519417131}*[interface-number1]{lang="EN-US"}*[ **to** ]{lang="EN-US"}*[interface-type]{lang="EN-US"}[ interface-number2 ]{lang="EN-US"}*[\[ **share** \]]{lang="EN-US"}

[**[undo allocate interface ]{lang="EN-US"}***[interface-type]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_10889_x4909_x1462470338}*[interface-number1]{lang="EN-US"}*[ **to** ]{lang="EN-US"}*[interface-type]{lang="EN-US"}[ interface-number2]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1242944422}

[[设备上的所有接口都属于缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1633318270}[，不属于任何非缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[。（集中式防火墙]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式防火墙]{style="font-family:宋体"}[/]{lang="EN-US"}[防火墙]{style="font-family:宋体"}[IRF]{lang="EN-US"}[）]{style="font-family:宋体"}

[[接口不属于任何]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1565718801}[。（防火墙插卡）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1834856082}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_342239973}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x117291921}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x1425842850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x1307862020}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x494033391}

[[{]{lang="EN-US"}[ *interface-type interface-number* }&\<1-24\>]{lang="EN-US"}]{#struct_0_10889_x4909_1621149543}[：表示给]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配非连续的接口。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和编号，]{style="font-family:宋体"}[&\<1-24\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[24]{lang="EN-US"}[次]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_10889_x4909_x481473225}*[interface-number1]{lang="EN-US"}*[ **to** ]{lang="EN-US"}*[interface-type]{lang="EN-US"}[ interface-number2]{lang="EN-US"}*[：表示给]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配一组连续的接口。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[表示接口类型，]{style="font-family:宋体"}*[interface-number1]{lang="EN-US"}*[表示起始接口的编号，]{style="font-family:宋体"}*[interface-number2]{lang="EN-US"}*[表示结束接口的编号。起始接口和结束接口的类型必须相同，并且处于同一接口板上，否则将配置失败。]{style="font-family:宋体"}

[**[share]{lang="EN-US"}**]{#struct_0_10889_x4909_163369041}[：表示接口是否共享。不指定该参数表示独占。防火墙插卡上不支持该参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1846154457}

[[物理接口和逻辑接口均可以独占或共享方式分配给某个]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1374064304}[。]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[包装防火墙]{style="font-family:宋体"}]{#struct_0_10889_x4909_1037322270}[/]{lang="EN-US"}[集中式防火墙]{style="font-family:宋体"}[IRF]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[独占方式分配（不带]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1455292813}**[share]{lang="EN-US"}**[参数）。使用该方式分配的接口仅归该]{style="font-family:宋体"}[Context]{lang="EN-US"}[所有、使用。用户登录该]{style="font-family:宋体"}[Context]{lang="EN-US"}[后，能查看到该接口，并执行接口支持的所有命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[共享方式分配（带]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1633318269}**[share]{lang="EN-US"}**[参数）。使用该方式分配的接口归多个]{style="font-family:宋体"}[Context]{lang="EN-US"}[所有、使用。在缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[内仍然存在该接口，可执行接口支持的所有命令；在分配给的非缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[内，会新建同名接口，用户登录这些]{style="font-family:宋体"}[Context]{lang="EN-US"}[后，能查看到该接口，但只能执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[、]{style="font-family:宋体"}**[description]{lang="EN-US"}**[、以及网络]{style="font-family:宋体"}[/]{lang="EN-US"}[安全相关的命令。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[插卡防火墙]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_741003898}

[[同一接口只能分配给一个]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1633259647}[使用。分配后的接口仍然在]{style="font-family:宋体"}[Context]{lang="EN-US"}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[内，但接口下的安全业务会被清除。请登录]{style="font-family:宋体"}[Context]{lang="EN-US"}[来配置该接口下的安全业务，接口下的其它命令请在]{style="font-family:宋体"}[Context]{lang="EN-US"}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[下配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x883735139}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1979485207}[将接口]{style="font-family:宋体"}[Ethernet1/1]{lang="EN-US"}[和]{style="font-family:宋体"}[Ethernet1/3]{lang="EN-US"}[以共享的方式分配给]{style="font-family:宋体"}[context sub1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x1915776428}

[\[Sysname\] context sub1]{lang="EN-US"}

[\[Sysname-context-2-sub1\] allocate interface ethernet 1/1 ethernet 1/3 share]{lang="EN-US"}

[[The interfaces will be shared by contexts. Continue? \[Y/N\]:y]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}
:::

::::: {#-666378434 .myid}
[]{#_Toc404783298}[]{#struct_0_10889_x4909_x623025634}[]{#_Toc359421738}

**Context \-- Context命令 \-- allocate vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_585474725}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_x1085283212}
:::

**[ ]{lang="EN-US"}**

[**[allocate vlan]{lang="EN-US"}**]{#struct_0_10889_x4909_x1633318264}[命令用来为]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配]{style="font-family:宋体"}[VLAN]{lang="EN-US"}**[。]{style="font-family:宋体"}**

[**[undo allocate vlan]{lang="EN-US"}**]{#struct_0_10889_x4909_x759814491}[命令用来取消为]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1355407191}

[**[allocate]{lang="EN-US"}**[ **vlan** *vlan-id*&\<1-24\>]{lang="EN-US"}]{#struct_0_10889_x4909_x1108167226}

[**[undo allocate vlan]{lang="EN-US"}**[ *vlan-id*&\<1-24\>]{lang="EN-US"}]{#struct_0_10889_x4909_x725585076}

[**[allocate vlan]{lang="EN-US"}***[ vlan-id1]{lang="EN-US"}*[ **to** *vlan-id2*]{lang="EN-US"}]{#struct_0_10889_x4909_274244460}

[**[undo allocate vlan ]{lang="EN-US"}***[vlan-id1]{lang="EN-US"}*[ **to** *vlan-id2*]{lang="EN-US"}]{#struct_0_10889_x4909_94922092}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_466628711}

[[没有为]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1071747258}[分配]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1098871363}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_863517594}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1046996927}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1289717515}

[[context-admin]{lang="EN-US"}]{#struct_0_10889_x4909_543151331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1746303256}

[*[vlan-id]{lang="EN-US"}*[&\<1-24\>]{lang="EN-US"}]{#struct_0_10889_x4909_x1633318263}**[：]{style="font-family:宋体"}**[表示给]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配非连续的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，]{style="font-family:宋体"}[&\<1-24\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[24]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[vlan-id1]{lang="EN-US"}***[ to ]{lang="EN-US"}***[vlan-id2]{lang="EN-US"}*]{#struct_0_10889_x4909_1162499810}**[：]{style="font-family:宋体"}**[表示给]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配一组连续的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[表示起始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[表示结束]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x514776310}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[包装防火墙]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_x17355054}

[[创建]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x370426892}[时，通过]{style="font-family:宋体"}**[vlan-unshared]{lang="EN-US"}**[参数可选择是否和其]{style="font-family:宋体"}[它]{style="font-family:宋体"}[Context]{lang="EN-US"}[共享]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果选择和其它]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x834403740}[共享]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则设备上所有]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[共享]{lang="EN-US" style="font-family:宋体"}[VLAN 1]{lang="EN-US" style="color:black"}[～]{lang="EN-US" style="font-family:
宋体;color:black"}[VLAN 4094]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}[这些]{lang="EN-US" style="font-family:
宋体;color:black"}[VLAN]{lang="EN-US" style="color:black"}[通过]{lang="EN-US" style="font-family:宋体;color:black"}**[allocate]{lang="EN-US"}**[ **vlan**]{lang="EN-US"}[命令分配。如果]{lang="EN-US" style="font-family:宋体"}[某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[已经分配给某]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[，则不能再分配给其它]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果选择]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_x1632872654}[不]{style="font-family:宋体"}[和其它]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[共享]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[请登录该]{style="font-family:宋体"}[Context]{lang="EN-US"}[，并]{style="font-family:宋体"}[使用]{lang="EN-US" style="font-family:宋体"}**[vlan]{lang="EN-US"}**[命令创建]{lang="EN-US" style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[VLAN 4094]{lang="EN-US"}[。]{style="font-family:宋体"}[Context]{lang="EN-US"}[各自使用和]{style="font-family:宋体"}[管理]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[互不干扰]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[防火墙插卡]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_801073078}

[[设备上所有]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1583438995}[共享]{style="font-family:宋体"}[VLAN 1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[VLAN 4094]{lang="EN-US" style="color:black"}[。这些]{style="font-family:宋体;color:black"}[VLAN]{lang="EN-US" style="color:black"}[通过]{style="font-family:宋体;color:black"}**[allocate]{lang="EN-US"}**[ **vlan**]{lang="EN-US"}[命令分配。如果某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[已经分配给某]{style="font-family:宋体"}[Context]{lang="EN-US"}[了，则不能再分配给其它]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1513602600}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_534584236}[将]{style="font-family:宋体"}[VLAN100]{lang="EN-US"}[分配给]{style="font-family:宋体"}[context sub1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_1038305330}

[[\[Sysname\] context sub1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_x1220555206}

[[\[Sysname-context-2-sub1\] allocate vlan 100]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_1636225536}

[[The VLAN will be allocated to context sub1. Continue? \[Y/N\]:y]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_x1095905708}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1741952414}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display context vlan]{lang="EN-US"}**]{#struct_0_10889_x4909_x1641857266}
:::::

::::: {#620472932 .myid}
[]{#_Toc404783299}[]{#struct_0_10889_x4909_x274250929}[]{#_Toc356459224}

**Context \-- Context命令 \-- blade-controller-team**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_1103561179}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_682006493}
:::

**[ ]{lang="EN-US"}**

[**[blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_x1633318266}[命令用来创建安全引擎组并进入该安全引擎组视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **blade-controller-team**]{lang="EN-US"}]{#struct_0_10889_x4909_402984923}[命令用来删除指定的安全引擎组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_518338279}

[**[blade-controller-team]{lang="EN-US"}**[ *blade-controller-team-name* \[ **id** *blade-controller-team-id* \]]{lang="EN-US"}]{#struct_0_10889_x4909_x288785068}

[**[undo blade-controller-team]{lang="EN-US"}**[ { *blade-controller-team-name \|* **id** *blade-controller-team-id* }]{lang="EN-US"}]{#struct_0_10889_x4909_x284783598}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1535717253}

[[设备上有一个安全引擎组，名字为]{style="font-family:宋体"}[Default]{lang="EN-US"}]{#struct_0_10889_x4909_x124233767}[，编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1813732993}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_1571888007}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x179859674}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x1595545203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_136392690}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1080226233}

[*[blade-controller-team-name]{lang="EN-US"}*]{#struct_0_10889_x4909_x1633318265}[：安全引擎组的名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[id]{lang="EN-US"}***[ blade-controller-team-id]{lang="EN-US"}*]{#struct_0_10889_x4909_1969068864}[：安全引擎组的编号，取值范围为]{style="font-family:
宋体"}[2]{lang="EN-US"}[～]{style="font-family:
宋体"}[256]{lang="EN-US"}[。不指定该参数时，系统会自动分配一个当前空闲的最小编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x2047234310}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省安全引擎组不能创建、删除，且不能进入缺省安全引擎组的视图。]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1655587458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当删除安全引擎组时，如果该组中有]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_1564320821}[进驻]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[安全引擎]{style="font-family:宋体"}[，请先用]{lang="EN-US" style="font-family:宋体"}**[undo ]{lang="EN-US"}[location]{lang="EN-US"}[ ]{lang="EN-US"}[blade-controller]{lang="EN-US"}**[命令取消]{lang="EN-US" style="font-family:宋体"}[进驻]{style="font-family:宋体"}[后，再删除该组]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1417892844}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x1887102229}[创建名为]{style="font-family:宋体"}[abc]{lang="EN-US" style="font-family:\"Arial Unicode MS\",\"sans-serif\""}[的]{style="font-family:宋体"}[安全引擎组]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x1537539091}

[\[sysname\] blade-controller-team abc]{lang="EN-US"}

[\[sysname-blade-controller-team-3-abc\]]{lang="EN-US"}[]{#_Toc365648361}
:::::

::::: {#-1465104500 .myid}
[]{#_Toc404783300}[]{#struct_0_10889_x4909_2016824738}[]{#_Toc382551694}

**Context \-- Context命令 \-- capability object-policy-rule maximum**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_x1221670389}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_450740797}
:::

[ ]{lang="EN-US"}

[**[capability object-policy-rule maximum]{lang="EN-US"}**]{#struct_0_10889_x4909_x669094592}[命令用来设置]{style="font-family:宋体"}[Context]{lang="EN-US"}[的对象策略规则总数限制。]{style="font-family:宋体"}

[**[undo capability object-policy-rule maximum]{lang="EN-US"}**]{#struct_0_10889_x4909_x430312764}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1751594130}

[**[capability object-policy-rule maximum ]{lang="EN-US"}***[max-value]{lang="EN-US"}*]{#struct_0_10889_x4909_119481942}

[**[undo capability object-policy-rule maximum]{lang="EN-US"}**]{#struct_0_10889_x4909_1312767540}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_685996387}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_10889_x4909_502573667}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_470694476}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1124392967}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1446780215}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_10889_x4909_x233815178}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_10889_x4909_x1715495923}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1488563114}

[*[max-value]{lang="EN-US"}*]{#struct_0_10889_x4909_459104012}[：表示]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[内可配置的对象策略规则总数的最大值。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1268335531}

[[配置本命令后，该]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x2092852487}[已进驻的每个安全引擎上都将获得相同的对象策略规则总数限制。]{style="font-family:宋体"}

[[当规则总数达到最大值时，不能新增规则。]{style="font-family:宋体"}]{#struct_0_10889_x4909_246958693}

[[如果当前设置的最大值比之前设置的最大值小，则可能存在最大值比当前存在的规则总数小的情况，但配置仍会成功，多出的规则不会删除，后续不能新增规则。]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1128791283}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_98466540}

[[\#]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\";color:black"}]{#struct_0_10889_x4909_1275159187}[[ ]{lang="EN-US" style="font-size:8.5pt;font-family:
\"Courier New\";color:black"}]{.apple-converted-space}[配置]{style="font-size:10.5pt;
color:black"}[Context]{lang="EN-US" style="font-size:10.5pt;font-family:
\"Arial\",\"sans-serif\";color:black"}[的]{style="font-size:10.5pt;
color:black"}[安全策略规则数最多为]{style="font-size:10.5pt;color:black"}[1000]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\";color:black"}[条]{style="font-size:10.5pt;color:black"}[。]{style="font-size:10.5pt;
color:black"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\";color:black"}]{#struct_0_10889_x4909_x1115343144}

[[\[Sysname\] context cnt2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\";color:black"}]{#struct_0_10889_x4909_1427806568}

[[\[Sysname-context-2-cnt2\] capability object-policy-rule maximum 1000]{lang="EN-US" style="color:black"}]{#struct_0_10889_x4909_503466408}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1329974679}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display]{lang="EN-US"}**[ **object-policy ip**]{lang="EN-US"}]{#struct_0_10889_x4909_633009487}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[对象策略）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#1277096323 .myid}
[]{#_Toc404783301}[]{#struct_0_10889_x4909_541074729}

**Context \-- Context命令 \-- capability session maximum**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_x1469879972}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:
KaiTi_GB2312"}]{#struct_0_10889_x4909_x1316611817}
:::

[ ]{lang="EN-US"}

[**[capability session maximum]{lang="EN-US"}**]{#struct_0_10889_x4909_274048182}[命令用来设置]{style="font-family:
宋体"}[Context]{lang="EN-US"}[的会话并发数限制。]{style="font-family:宋体"}

[**[undo capability session maximum]{lang="EN-US"}**]{#struct_0_10889_x4909_x534401935}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1403294214}

[**[capability session maximum]{lang="EN-US"}***[ max-number]{lang="EN-US"}*]{#struct_0_10889_x4909_1185442111}

[**[undo capability session maximum]{lang="EN-US"}**]{#struct_0_10889_x4909_1613540211}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1008338048}

[[未对该]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1205324001}[允许的会话并发数进行限制，由该]{style="font-family:宋体"}[Context]{lang="EN-US"}[上各安全引擎当前的内存能力决定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1333725575}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x613086075}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1774011667}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1487598107}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_596890103}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1268271525}

[*[max-number]{lang="EN-US"}*]{#struct_0_10889_x4909_168622625}[：允许同时存在的最大会话数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x364748562}

[[配置本命令后，该]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x308774090}[己进驻的每个安全引擎都将获得相同的会话并发数限制。当安全引擎上的会话总数达到最大数目后，该安全引擎上将不允许新建会话；如果本次设置的数值小于当前安全引擎上的会话总数，则配置可以成功，但不再允许新建会话，且已经创建的会话不会被删除，直到已建立的会话通过老化机制使得会话总数低于配置的最大值后，系统才允许新建会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1467956230}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x213827698}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[上的会话并发数为]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_487606211}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] capability session maximum 1000000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_406980923}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[context]{lang="EN-US"}**]{#struct_0_10889_x4909_x750121693}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session statistics]{lang="EN-US"}**]{#struct_0_10889_x4909_x29459103}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[会话管理）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#1490664607 .myid}
[]{#_Toc404783302}[]{#struct_0_10889_x4909_958378346}

**Context \-- Context命令 \-- capability session rate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](Context命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_580657303}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:
KaiTi_GB2312"}]{#struct_0_10889_x4909_x1983209809}
:::

[ ]{lang="EN-US"}

[**[capability session rate]{lang="EN-US"}**]{#struct_0_10889_x4909_x1874858031}[命令用来设置]{style="font-family:宋体"}[Context]{lang="EN-US"}[的会话新建速率限制。]{style="font-family:宋体"}

[**[undo capability session rate]{lang="EN-US"}**]{#struct_0_10889_x4909_1352502018}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1054196935}

[**[capability session rate]{lang="EN-US"}**[ *max-value*]{lang="EN-US"}]{#struct_0_10889_x4909_x1340785983}

[**[undo capablility session rate]{lang="EN-US"}**]{#struct_0_10889_x4909_1529482432}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1236802708}

[[未对该]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1489763657}[允许的会话新建速率进行限制，由该]{style="font-family:宋体"}[Context]{lang="EN-US"}[上各安全引擎当前的内存能力决定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_802161275}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1602931102}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1455349875}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x633621818}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1141337658}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_854025324}

[*[max-value]{lang="EN-US"}*]{#struct_0_10889_x4909_x418256631}[：允许的会话新建速率最大值，单位为每秒会话个数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1896921902}

[[配置本命令后，该]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1607212309}[己进驻的每个安全引擎都将获得相同的会话新建速率限制。当安全引擎上的会话新建速率达到最大值后，该安全引擎上将不允许新建会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1502885543}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x952284848}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[上的会话新建速率最大值为每秒]{style="font-family:宋体"}[20000]{lang="EN-US"}[个会话数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_1204100983}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] capability session rate 20000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_656745411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[context]{lang="EN-US"}**]{#struct_0_10889_x4909_x310048819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display session statistics]{lang="EN-US"}**]{#struct_0_10889_x4909_x758942064}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[会话管理）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#1288995370 .myid}
[]{#_Toc404783303}[]{#struct_0_10889_x4909_x213907019}[]{#_Toc382551693}

**Context \-- Context命令 \-- capability throughput**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_x712058617}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_348812945}
:::

[ ]{lang="EN-US"}

[**[capability throughput]{lang="EN-US"}**]{#struct_0_10889_x4909_430259865}[命令用来设置]{style="font-family:宋体"}[Context]{lang="EN-US"}[的吞吐量限制。]{style="font-family:宋体"}

[**[undo capability throughput]{lang="EN-US"}**]{#struct_0_10889_x4909_x678906907}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x348995963}

[**[capability throughput ]{lang="EN-US"}**[{ **kbps**]{lang="EN-US"}]{#struct_0_10889_x4909_x106646564}[ ]{lang="EN-US"}[\| **pps**]{lang="EN-US"}[ ]{lang="EN-US"}[} *value*]{lang="EN-US"}

[**[undo capability throughput]{lang="EN-US"}**]{#struct_0_10889_x4909_10345180}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_965585459}

[[各]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1488285997}[不做吞吐量限制，按实际能力转发。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x861749582}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x850333390}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1244031904}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x291062163}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_448019465}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1411369867}

[**[kbps]{lang="EN-US"}**]{#struct_0_10889_x4909_x1248133075}[：表示吞吐量按每秒千比特计算。]{style="font-family:宋体"}

[**[pps]{lang="EN-US"}**]{#struct_0_10889_x4909_x1595395195}[：表示吞吐量按每秒报文数计算。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_10889_x4909_x1948455542}[：表示吞吐量限制值，取值范围为]{style="font-family:宋体"}[1000]{lang="EN-US"}[～]{style="font-family:宋体"}[100000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1355387556}

[[配置本命令后，该]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x329129985}[已进驻的每个安全引擎上都将获得相同的吞吐量限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1018553792}

[[\#]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\";color:black"}]{#struct_0_10889_x4909_1660594378}[[ ]{lang="EN-US" style="font-size:8.5pt;font-family:
\"Courier New\";color:black"}]{.apple-converted-space}[配置]{style="font-size:10.5pt;
color:black"}[Context]{lang="EN-US" style="font-size:10.5pt;font-family:
\"Arial\",\"sans-serif\";color:black"}[的]{style="font-size:10.5pt;
color:black"}[吞吐量为]{style="font-size:10.5pt;color:black"}[100Mbps]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\";color:black"}[。]{style="font-size:10.5pt;color:black"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\";color:black"}]{#struct_0_10889_x4909_x1851447919}

[[\[Sysname\] context cnt2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\";color:black"}]{#struct_0_10889_x4909_1731213131}

[[\[Sysname-context-2-cnt2\] capability throughput kbps 100000]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\";color:black"}]{#struct_0_10889_x4909_1006012918}

[[\#]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\";color:black"}]{#struct_0_10889_x4909_x98157901}[[ ]{lang="EN-US" style="font-size:8.5pt;font-family:
\"Courier New\";color:black"}]{.apple-converted-space}[配置]{style="font-size:10.5pt;
color:black"}[Context]{lang="EN-US" style="font-size:10.5pt;font-family:
\"Arial\",\"sans-serif\";color:black"}[的]{style="font-size:10.5pt;
color:black"}[吞吐量为]{style="font-size:10.5pt;color:black"}[10000pps]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\";color:black"}[。]{style="font-size:10.5pt;color:black"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\";color:black"}]{#struct_0_10889_x4909_1152783503}

[[\[Sysname\] context cnt2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\";color:black"}]{#struct_0_10889_x4909_x2083207457}

[[\[Sysname-context-2-cnt2\] capability throughput pps 10000]{lang="EN-US" style="color:black"}]{#struct_0_10889_x4909_x234405787}
:::::

::: {#1340338390 .myid}
[]{#_Toc404783304}[]{#struct_0_10889_x4909_330653425}

**Context \-- Context命令 \-- context**

------------------------------------------------------------------------

[**[context]{lang="EN-US"}**]{#struct_0_10889_x4909_x1691292106}[命令用来创建]{style="font-family:宋体"}[Context]{lang="EN-US"}[并进入]{style="font-family:宋体"}[Context]{lang="EN-US"}[视图]{style="font-family:宋体"}[。如果]{style="font-family:宋体"}[Context]{lang="EN-US"}[已创建，则直接进入]{style="font-family:宋体"}[Context]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo context]{lang="EN-US"}**]{#struct_0_10889_x4909_x1044918304}[命令用来删除]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1543174883}

[[包装防火墙：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x107122366}

[**[context ]{lang="EN-US"}**]{#struct_0_10889_x4909_x1633318260}*[context-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[]{lang="EN-US"}*[ ]{lang="EN-US"}***[id ]{lang="EN-US"}***[context-id ]{lang="EN-US"}*[\]]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[vlan-unshared]{lang="EN-US"}***[ ]{lang="EN-US"}*[\]]{lang="EN-US"}

[**[undo context ]{lang="EN-US"}**]{#struct_0_10889_x4909_1565784337}*[context-name]{lang="EN-US"}*

[[防火墙插卡：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x222747181}

[**[context ]{lang="EN-US"}**]{#struct_0_10889_x4909_1256298058}*[context-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[]{lang="EN-US"}*[ ]{lang="EN-US"}***[id ]{lang="EN-US"}***[context-id ]{lang="EN-US"}*[\]]{lang="EN-US"}

[**[undo context ]{lang="EN-US"}**]{#struct_0_10889_x4909_1191889454}*[context-name]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1231384568}

[[设备上存在缺省]{style="font-family:宋体"}]{#struct_0_10889_x4909_1513441219}[Context]{lang="EN-US"}[，名称为]{style="font-family:宋体"}[Admin]{lang="EN-US"}[，编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。（]{style="font-family:宋体"}[包装防火墙]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[设备上没有]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1787981818}[。（防火墙插卡）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_2144876667}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_393444017}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x664400610}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x902749884}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1556941568}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_884518740}

[*[context-name]{lang="EN-US"}*]{#struct_0_10889_x4909_730535543}[：]{style="font-family:宋体"}[Context]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[context-id]{lang="EN-US"}*]{#struct_0_10889_x4909_x1633318259}[：]{style="font-family:宋体"}[Context]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65279]{lang="EN-US"}[。不指定该参数时，系统会自动给]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配一个当前空闲的最小编号。]{style="font-family:宋体"}

[**[vlan-unshared]{lang="EN-US"}**]{#struct_0_10889_x4909_x356464428}[：不和其它]{style="font-family:宋体"}[Context]{lang="EN-US"}[共享]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。不指定该参数时，表示和其它]{style="font-family:宋体"}[Context]{lang="EN-US"}[共享]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（包装防火墙）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x912449505}

[[创建]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_506528474}[时，通过]{style="font-family:宋体"}**[vlan-unshared]{lang="EN-US"}**[参数可选择是否和其]{style="font-family:宋体"}[它]{style="font-family:宋体"}[Context]{lang="EN-US"}[共享]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果选择和其它]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1040651634}[共享]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则设备上所有]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[共享]{lang="EN-US" style="font-family:宋体"}[VLAN 1]{lang="EN-US" style="color:black"}[～]{lang="EN-US" style="font-family:
宋体;color:black"}[VLAN 4094]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}[这些]{lang="EN-US" style="font-family:
宋体;color:black"}[VLAN]{lang="EN-US" style="color:black"}[通过]{lang="EN-US" style="font-family:宋体;color:black"}**[allocate]{lang="EN-US"}**[ **vlan**]{lang="EN-US"}[命令分配。如果]{lang="EN-US" style="font-family:宋体"}[某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[已经分配给某]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[了，则不能再分配给其它]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果选择]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_461355052}[不]{style="font-family:宋体"}[和其它]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[共享]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[请登录该]{style="font-family:宋体"}[Context]{lang="EN-US"}[，并]{style="font-family:宋体"}[使用]{lang="EN-US" style="font-family:宋体"}**[vlan]{lang="EN-US"}**[命令创建]{lang="EN-US" style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[VLAN 4094]{lang="EN-US"}[。]{style="font-family:宋体"}[Context]{lang="EN-US"}[各自使用和]{style="font-family:宋体"}[管理]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[互不干扰]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x184225722}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1524534093}[创建一个名称为]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_1179672791}

[\[Sysname\] context test]{lang="EN-US"}

[\[Sysname-context-2-test\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_318250498}[创建一个名称为]{style="font-family:宋体"}[test]{lang="EN-US"}[，]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:
宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_903561657}

[\[Sysname\] context test id 2]{lang="EN-US"}

[\[Sysname-context-2-test\]]{lang="EN-US"}
:::

::: {#1430433195 .myid}
[]{#_Toc404783305}[]{#struct_0_10889_x4909_x941995708}[]{#_Toc365648365}

**Context \-- Context命令 \-- context start**

------------------------------------------------------------------------

[**[context start]{lang="EN-US"}**]{#struct_0_10889_x4909_1955640290}[命令用来启动]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo context start]{lang="EN-US"}**]{#struct_0_10889_x4909_705333892}[命令用来停止该]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_2023534592}

[**[context start]{lang="EN-US"}**]{#struct_0_10889_x4909_612914445}

[**[undo context start]{lang="EN-US"}**]{#struct_0_10889_x4909_x1954200687}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x523736518}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1285429315}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x688503120}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x1703227343}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x523014579}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_118238726}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_2025379172}[创建后需要执行]{style="font-family:宋体"}**[context]{lang="EN-US"}[ ]{lang="EN-US"}[start]{lang="EN-US"}**[命令，才能完成新]{style="font-family:宋体"}[Context]{lang="EN-US"}[的初始化，相当于上电启动。启动后，用户可以登录到该]{style="font-family:宋体"}[Context]{lang="EN-US"}[执行配置。]{style="font-family:宋体"}

[[请先配置]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1223114796}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，再登录该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，在这个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[下使用该命令启动]{style="font-family:宋体"}[Context]{lang="EN-US"}[。例如，]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[属于]{style="font-family:宋体"}[MDC test]{lang="EN-US"}[，则必须先通过]{style="font-family:宋体"}**[switchto mdc test]{lang="EN-US"}**[命令或者]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[等方式登录到]{style="font-family:宋体"}[MDC test]{lang="EN-US"}[，才可以启动]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10889_x4909_92430670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[停止]{style="font-family:宋体"}]{#struct_0_10889_x4909_705333893}[Context]{lang="EN-US"}[会导致该]{style="font-family:宋体"}[Context]{lang="EN-US"}[的业务中断，以及登录该]{style="font-family:宋体"}[Context]{lang="EN-US"}[的用户自动退出，请谨慎使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[停止]{style="font-family:宋体"}]{#struct_0_10889_x4909_2023534593}[Context]{lang="EN-US"}[前]{style="font-family:宋体"}[请保存]{style="font-family:宋体"}[Context]{lang="EN-US"}[的配置，否则，可能导]{style="font-family:宋体"}[致]{style="font-family:宋体"}[Context]{lang="EN-US"}[的当前配置丢失。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_612979981}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1444753094}[启动]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_712429267}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] context start]{lang="EN-US"}

[It will take some time to start the context\...]{lang="EN-US"}

[Context started successfully.]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404783306}[]{#struct_0_10889_x4909_1020527443}[]{#_Toc365648366}

**Context \-- Context命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_10889_x4909_x30622050}[命令用来配置]{style="font-family:宋体"}[Context]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1293750080}

[**[description ]{lang="EN-US"}**]{#struct_0_10889_x4909_1260108727}*[text]{lang="EN-US"}*

[**[undo description]{lang="EN-US"}**]{#struct_0_10889_x4909_x699420973}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x30202325}

[[缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1310751710}[描述信息为]{style="font-family:宋体"}[DefaultContext]{lang="EN-US"}[。非缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[没有配置描述信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1128951766}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1409524226}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_705333890}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_2023534594}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_613307661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_528092769}

[*[text]{lang="EN-US"}*]{#struct_0_10889_x4909_316916529}[：]{style="font-family:宋体"}[Context]{lang="EN-US"}[的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1717604907}

[[当设备上配置的]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1070868658}[Context]{lang="EN-US"}[较多时，用户可以为]{style="font-family:宋体"}[Context]{lang="EN-US"}[配置特定的描述信息，以便记忆和管理]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1464106342}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_7278419}[将]{style="font-family:宋体"}[Context]{lang="EN-US"}[的描述信息配置为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x942601459}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] description test]{lang="EN-US"}
:::

::::: {#1598154567 .myid}
[]{#_Toc404783307}[]{#struct_0_10889_x4909_1408140846}[]{#_Toc356459226}

**Context \-- Context命令 \-- display blade-controller-team**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_2108629967}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_x986369760}
:::

[ ]{lang="EN-US"}

[**[display blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_361829458}[命令用来显示安全引擎组的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1318047444}

[**[display blade-controller-team]{lang="EN-US"}**[ \[ *blade-controller-team-name* \| **id** *blade-controller-team-id* \]]{lang="EN-US"}]{#struct_0_10889_x4909_705333891}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_2023534595}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_613373197}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x984710671}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x1080670964}

[[network-operator]{lang="EN-US"}]{#struct_0_10889_x4909_x925651261}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x410880457}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10889_x4909_x315698404}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1470335049}

[*[blade-controller-team-name]{lang="EN-US"}*]{#struct_0_10889_x4909_x1984219896}[：安全引擎组的名称，为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[id]{lang="EN-US"}***[ blade-controller-team-id]{lang="EN-US"}*]{#struct_0_10889_x4909_1255904843}[：安全引擎组的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1810780546}

[[不指定任何参数时，显示所有安全引擎组的信息。]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1449589560}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_589434349}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1211230708}[显示]{style="font-family:宋体"}[安全引擎组的]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display blade-controller-team]{lang="EN-US"}]{#struct_0_10889_x4909_x1319434905}

[ID          Name]{lang="EN-US"}

[1           abc]{lang="EN-US"}

[2           fff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1908032222}[显示名]{style="font-family:宋体"}[称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的安全引擎组的]{style="font-family:宋体"}[信息。（集中式设备[/]{lang="EN-US"}分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display blade-controller-team abc]{lang="EN-US"}]{#struct_0_10889_x4909_705333896}

[ID: 2        Name: abc]{lang="EN-US"}

[Slot    CPU    Status]{lang="EN-US"}

[1       1      Absent]{lang="EN-US"}

[\* 1       1      Normal]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*  : Primary blade controller of the team.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_2023534596}[显示名]{style="font-family:宋体"}[称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的安全引擎组的]{style="font-family:宋体"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display blade-controller-team abc]{lang="EN-US"}]{#struct_0_10889_x4909_613176589}

[ID: 2        Name: abc]{lang="EN-US"}

[Chassis    Slot    CPU    Status]{lang="EN-US"}

[1          1       1      Absent]{lang="EN-US"}

[\* 1          7       1      Normal]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*  : Primary blade controller of the team.]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display blade-controller-team]{lang="EN-US"}]{#struct_0_10889_x4909_x1245925505}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x496132865}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10889_x4909_x1992877322}
:::::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10889_x4909_1994923318}

[[ID]{lang="EN-US"}]{#struct_0_10889_x4909_x2091517514}

[[安全引擎组]{style="font-family:宋体"}]{#struct_0_10889_x4909_x435094948}[的]{style="font-family:宋体"}[编号]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_10889_x4909_x407171265}

[[安全引擎组]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1189386892}[的名称]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_10889_x4909_613242125}

[[安全引擎]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1811185028}[所在设备的成员编号]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_10889_x4909_239960504}

[[安全引擎]{style="font-family:宋体"}]{#struct_0_10889_x4909_444246595}[所在的槽位号]{style="font-family:宋体"}

[[CPU]{lang="EN-US"}]{#struct_0_10889_x4909_85971339}

[[安全引擎]{style="font-family:宋体"}]{#struct_0_10889_x4909_x218305561}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_10889_x4909_1255511627}

[[安全引擎的状态：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x213012527}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Absent]{lang="EN-US"}]{#struct_0_10889_x4909_x1071060859}[：表示该位置没有插入安全引擎]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_10889_x4909_986444380}[：表示该节点的单板不能正常启动]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_10889_x4909_1255708235}[：表示该位置的安全引擎运行正常]{lang="EN-US" style="font-family:宋体"}

[[\*  : Primary blade controller of the team.]{lang="EN-US"}]{#struct_0_10889_x4909_x776804405}

[[\*]{lang="EN-US"}]{#struct_0_10889_x4909_1595848590}[表示安全引擎组的主安全引擎]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#491971759 .myid}
[]{#_Toc404783308}[]{#struct_0_10889_x4909_x1107152877}[]{#_Toc365648371}

**Context \-- Context命令 \-- display context**

------------------------------------------------------------------------

[**[display context]{lang="EN-US"}**]{#struct_0_10889_x4909_x1147261679}[命令用来显示]{style="font-family:宋体"}[已经创建的]{style="font-family:宋体"}[Context]{lang="EN-US"}[的信息，包括编号和状态等]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x2140567800}

[**[display context]{lang="EN-US"}**]{#struct_0_10889_x4909_705333894}[ \[ **name** *context-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_2023534598}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_612521229}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1821835096}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_857134350}

[[network-operator]{lang="EN-US"}]{#struct_0_10889_x4909_x168639605}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_2109458827}

[[mdc-operato]{lang="EN-US"}]{#struct_0_10889_x4909_x994394937}[r]{lang="EN-US"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1013724486}

[**[name]{lang="EN-US"}**]{#struct_0_10889_x4909_601675560}[ ]{lang="EN-US"}*[context-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1999027094}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[包装防火墙]{style="font-family:宋体"}]{#struct_0_10889_x4909_x172538919}

[[在缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_419978633}[中，可使用]{style="font-family:宋体"}**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*[参数查看指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[的信息。不指定]{style="font-family:宋体"}**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*[参数时，则]{style="font-family:宋体"}[显示设备上创建的所有]{style="font-family:宋体"}[Context]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[防火墙插卡]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_179449154}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在缺省]{style="font-family:宋体"}]{#struct_0_10889_x4909_x698227831}[MDC]{lang="EN-US"}[下，]{style="font-family:宋体"}[可使用]{style="font-family:宋体"}**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*[参数查看指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[的信息；不指定]{style="font-family:宋体"}**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*[参数时，则]{style="font-family:宋体"}[显示设备上创建的所有]{style="font-family:宋体"}[Context]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非缺省]{style="font-family:宋体"}]{#struct_0_10889_x4909_705333895}[MDC]{lang="EN-US"}[下，不能指定]{style="font-family:宋体"}**[name ]{lang="EN-US"}***[context-name]{lang="EN-US"}*[参数，]{style="font-family:宋体"}[只能显示属于该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的所有]{style="font-family:宋体"}[Context]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_2023534599}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_612586765}[显示]{style="font-family:宋体"}[已经创建的]{style="font-family:宋体"}[Context]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display context]{lang="EN-US"}]{#struct_0_10889_x4909_x1307335995}

[ID     Name          Status           BelongTo        Description]{lang="EN-US"}

[1      cnt1          active           Admin           context1]{lang="EN-US"}

[2      cnt2          inactive         MDC3            context2]{lang="EN-US"}

[3      cnt3          inactive         MDC2            context3]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display context]{lang="EN-US"}]{#struct_0_10889_x4909_1677738652}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x499691187}[[字段]{style="font-family:黑体"}]{#struct_0_10889_x4909_x430141496}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10889_x4909_1000893806}

[[ID]{lang="EN-US"}]{#struct_0_10889_x4909_x528175545}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_2062459647}[的编号]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_10889_x4909_855447438}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x127439935}[的名称]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_10889_x4909_x1471210804}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_705333900}[的状态：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[a]{lang="EN-US"}[ctive]{lang="EN-US"}]{#struct_0_10889_x4909_x1132315801}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[正常运行]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_10889_x4909_x92254034}[：表示]{style="font-family:
  宋体"}[Context]{lang="EN-US"}[处于未启动状态]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[starting]{lang="EN-US"}]{#struct_0_10889_x4909_x1853816515}[：表示]{style="font-family:
  宋体"}[Context]{lang="EN-US"}[正在启动]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[updating]{lang="EN-US"}]{#struct_0_10889_x4909_1037577134}[：表示正在将]{style="font-family:
  宋体"}[Context]{lang="EN-US"}[加入安全引擎组]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stopping]{lang="EN-US"}]{#struct_0_10889_x4909_112899750}[：表示]{style="font-family:宋体"}[Context]{lang="EN-US"}[正在停止]{style="font-family:宋体"}

[[Belongto]{lang="EN-US"}]{#struct_0_10889_x4909_x813646306}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_740604949}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的名称（防火墙插卡）]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_10889_x4909_x467262498}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_311364047}[描述信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1588442510 .myid}
[]{#_Toc404783309}[]{#struct_0_10889_x4909_x1941570326}[]{#_Toc359421726}[]{#_Toc348877442}

**Context \-- Context命令 \-- display context interface**

------------------------------------------------------------------------

[**[display context interface]{lang="EN-US"}**]{#struct_0_10889_x4909_659114731}[命令用来显示]{style="font-family:
宋体"}[Context]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_84586338}

[**[display context ]{lang="EN-US"}**[\[ **name** *context-name* \] **interface**]{lang="EN-US"}]{#struct_0_10889_x4909_705333901}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1132315800}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1658337975}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1759000453}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_976823573}

[[network-operator]{lang="EN-US"}]{#struct_0_10889_x4909_1312536731}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x512823881}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10889_x4909_x590645929}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1063287755}

[**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*]{#struct_0_10889_x4909_1429206235}[：]{style="font-family:宋体"}[Context]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_291392233}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[包装防火墙]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_x1780347358}

[[在缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x994362702}[中，可使用]{style="font-family:宋体"}**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*[参数查看指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[的接口列表；不指定]{style="font-family:宋体"}**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*[参数时，则]{style="font-family:宋体"}[显示设备上创建的所有]{style="font-family:宋体"}[C]{lang="EN-US"}[ontext]{lang="EN-US"}[的接口列表]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[防火墙插卡]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_1657797053}

[[使用该命令：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x586615699}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在缺省]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_x77493189}[MDC]{lang="EN-US"}[下，]{lang="EN-US" style="font-family:宋体"}[可使用]{lang="EN-US" style="font-family:宋体"}**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*[参数查看指定]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[的接口列表；不]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}**[name]{lang="EN-US"}***[ context-name]{lang="EN-US"}*[参数]{lang="EN-US" style="font-family:宋体"}[时，]{style="font-family:宋体"}[则]{lang="EN-US" style="font-family:宋体"}[显示设备上创建的所有]{lang="EN-US" style="font-family:宋体"}[C]{lang="EN-US"}[ontext]{lang="EN-US"}[的接口列表。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在非缺省]{style="font-family:宋体"}]{#struct_0_10889_x4909_1903463044}[MDC]{lang="EN-US"}[下，不能指定]{style="font-family:宋体"}**[name ]{lang="EN-US"}***[context-name]{lang="EN-US"}*[参数，]{style="font-family:宋体"}[只能显示属于该]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的所有]{style="font-family:宋体"}[C]{lang="EN-US"}[ontext]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1940934969}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1083100357}[显示所有]{style="font-family:宋体"}[Context]{lang="EN-US"}[的接口列表。]{style="font-family:宋体"}

[[\<Sysname\> display context interface]{lang="EN-US"}]{#struct_0_10889_x4909_339638104}

[Context stub1\'s interfaces:]{lang="EN-US"}

[  GigabitEthernet0/1/4]{lang="EN-US"}

[Context stub2\'s interfaces:]{lang="EN-US"}

[  FortyGigE0/1/8]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1014225707}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[allocate interface]{lang="EN-US"}**]{#struct_0_10889_x4909_x687185096}
:::

::: {#-966498513 .myid}
[]{#_Toc404783310}[]{#struct_0_10889_x4909_x391279772}

**Context \-- Context命令 \-- display context resource**

------------------------------------------------------------------------

[**[display context]{lang="EN-US"}[ resource]{lang="EN-US"}**]{#struct_0_10889_x4909_x2063791095}[命令用来显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x460440999}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x860544693}

[**[display context ]{lang="EN-US"}**]{#struct_0_10889_x4909_274854810}[\[ **name** *context-name* \] ]{lang="EN-US"}**[resource]{lang="EN-US"}**[ \[ **cpu** \| **disk** \| **memory[ ]{style="color:red"}**\]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1958552497}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display context ]{lang="EN-US"}**]{#struct_0_10889_x4909_305878675}[\[ **name** *context-name* \] ]{lang="EN-US"}**[resource]{lang="EN-US"}**[ \[ **cpu** \| **disk** \| **memory[ ]{style="color:red"}**\] \[ **slot** *slot-number* **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_10889_x4909_x721919723}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display context ]{lang="EN-US"}**]{#struct_0_10889_x4909_1903463045}[\[ **name** *context-name* \] ]{lang="EN-US"}**[resource ]{lang="EN-US"}**[\[ **cpu** \| **disk** \| **memory** \] \[ **chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1940869433}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_1667759957}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1336877864}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x200821176}

[[network-operator]{lang="EN-US"}]{#struct_0_10889_x4909_88827518}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x1206330090}

[[mdc-operato]{lang="EN-US"}]{#struct_0_10889_x4909_1315957820}[r]{lang="EN-US"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1367574377}

[**[name]{lang="EN-US"}**]{#struct_0_10889_x4909_110686829}[ *context-name*]{lang="EN-US"}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU]{lang="EN-US"}[/]{lang="EN-US" style="font-family:宋体"}[磁盘[/]{lang="EN-US"}内存资源的使用情况。]{style="font-family:宋体"}*[context-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。不指定该参数时，显示]{style="font-family:宋体"}[当前]{style="font-family:宋体"}[MDC]{lang="EN-US"}[下]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[Context]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU]{lang="EN-US"}[/]{lang="EN-US" style="font-family:宋体"}[磁盘[/]{lang="EN-US"}内存资源的使用情况。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_10889_x4909_779208641}[：显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[使用情况。]{style="font-family:宋体"}

[**[disk]{lang="EN-US"}**]{#struct_0_10889_x4909_x940169123}[：显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对磁盘的使用情况。]{style="font-family:宋体"}

[**[memory]{lang="EN-US"}**]{#struct_0_10889_x4909_300231228}[：显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对内存的使用情况。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_10889_x4909_x1059114535}[ *slot-number* **cpu** *cpu-number*]{lang="EN-US"}[：显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对指定安全引擎的]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示安全引擎所在的槽位号，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示安全引擎的]{style="font-family:宋体;
color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号]{style="font-family:宋体;color:black"}[。不指定该参数时，显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对所有安全引擎的]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_10889_x4909_56294212}[ *slot-number* **cpu** *cpu-number*]{lang="EN-US"}[：显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对指定成员设备上安全引擎的]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示安全引擎的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。不指定该参数时]{style="font-family:宋体;color:black"}[，显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对所有安全引擎的]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_10889_x4909_x241395650}[ *chassis-number* **slot** *slot-number* **cpu** *cpu-number*]{lang="EN-US"}[：显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对指定成员设备安全引擎的]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示安全引擎所在的槽位号，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示安全引擎的]{style="font-family:宋体;
color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号]{style="font-family:宋体;color:black"}[。不指定该参数时，显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有安全引擎的]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1903463042}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x1941066041}[显示所有]{style="font-family:宋体"}[Context]{lang="EN-US"}[对]{style="font-family:宋体"}[CPU/]{lang="EN-US"}[磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存资源的使用情况。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display context resource]{lang="EN-US"}]{#struct_0_10889_x4909_x682420604}

[Memory usage:]{lang="EN-US"}

[Slot 0 CPU 0]{lang="EN-US"}

[Used 120.7MB, Free 375.4MB, Total 496.1MB]{lang="EN-US"}

[  ID   Name        Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  1    Admin       496.1        94.9        375.4]{lang="EN-US"}

[  2    cnt2        496.1        25.8        375.4]{lang="EN-US"}

[ ]{lang="EN-US"}

[CPU usage:]{lang="EN-US"}

[Slot 0 CPU 0]{lang="EN-US"}

[  ID   Name        Weight       Usage(%)]{lang="EN-US"}

[  1    Admin       10           3]{lang="EN-US"}

[  2    cnt2        10           0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Disk usage:]{lang="EN-US"}

[Slot 0 CPU 0]{lang="EN-US"}

[flash: Used 0.3MB, Free 462.3MB, Total 462.6MB]{lang="EN-US"}

[  ID   Name        Quota(MB)    Used(MB)    Free(MB)]{lang="EN-US"}

[  1    Admin       416.3        0.3         416]{lang="EN-US"}

[  2    cnt2        46.3         0.0         46.3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1470055657}[显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对所有安全引擎上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[资源的使用情况。（分布式设备]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display context resource cpu]{lang="EN-US"}]{#struct_0_10889_x4909_x1917676837}

[CPU usage:]{lang="EN-US"}

[Slot 2 CPU 1:]{lang="EN-US"}

[  ID   Name        Weight       Usage(%)]{lang="EN-US"}

[  1    cnt1        10           24]{lang="EN-US"}

[  2    cnt2        10           0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 3 CPU 1:]{lang="EN-US"}

[  ID   Name        Weight       Usage(%)]{lang="EN-US"}

[  1    cnt3        10           0]{lang="EN-US"}

[  2    cnt4        10           0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_2112542463}[显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[对所有安全引擎上]{style="font-family:宋体"}[CPU]{lang="EN-US"}[资源的使用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display context resource cpu]{lang="EN-US"}]{#struct_0_10889_x4909_1903463043}

[CPU usage:]{lang="EN-US"}

[Chassis 1 slot 2 CPU 1:]{lang="EN-US"}

[  ID   Name        Weight       Usage(%)]{lang="EN-US"}

[  1    cnt1        10           24]{lang="EN-US"}

[  2    cnt2        10           0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 1 slot 3 CPU 1:]{lang="EN-US"}

[  ID   Name        Weight       Usage(%)]{lang="EN-US"}

[  1    cnt3        10           0]{lang="EN-US"}

[  2    cnt4        10           0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display context resource]{lang="EN-US"}]{#struct_0_10889_x4909_x1941000505}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x500681964}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10889_x4909_x1033255041}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10889_x4909_148595060}

[[Memory]{lang="EN-US"}]{#struct_0_10889_x4909_x97421749}

[[表示下面显示的是内存的使用情况]{style="font-family:宋体"}]{#struct_0_10889_x4909_x2037036837}

[[CPU]{lang="EN-US"}]{#struct_0_10889_x4909_29706472}

[[表示下面显示的是]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_10889_x4909_x105157646}[的使用情况]{style="font-family:宋体"}

[[Disk]{lang="EN-US"}]{#struct_0_10889_x4909_1292914348}

[[表示下面显示的是磁盘的使用情况]{style="font-family:宋体"}]{#struct_0_10889_x4909_x108123658}

[[Slot 0 CPU 0]{lang="EN-US"}]{#struct_0_10889_x4909_1069055041}

[[表示]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1903463048}[对指定安全引擎上资源的使用情况（集中式设备）]{style="font-family:宋体"}

[[Slot 2 CPU 1]{lang="EN-US"}]{#struct_0_10889_x4909_x1940672825}

[[表示]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x628506850}[对指定安全引擎上资源的使用情况（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[Slot 2 CPU 1]{lang="EN-US"}]{#struct_0_10889_x4909_511973381}

[[表示]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_370841336}[对指定安全引擎上资源的使用情况（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis 1 slot 2 CPU 1]{lang="EN-US"}]{#struct_0_10889_x4909_x559896750}

[[表示]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x51955865}[对指定安全引擎上资源的使用情况（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Used 238.1MB, Free 249.3MB, Total 487.4MB]{lang="EN-US"}]{#struct_0_10889_x4909_x1869056168}

[[内存的使用情况，]{style="font-family:宋体"}[Used]{lang="EN-US"}]{#struct_0_10889_x4909_325493979}[表示内存已使用空间的大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[），]{style="font-family:宋体"}[Free]{lang="EN-US"}[表示当前空闲内存的大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[），]{style="font-family:宋体"}[Total]{lang="EN-US"}[表示整个内存大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[）。]{style="font-family:宋体"}[如果]{style="font-family:宋体"}[Context]{lang="EN-US"}[没有启动，]{style="font-family:宋体"}[则]{style="font-family:宋体"}[Used]{lang="EN-US"}[会显示为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Cfa0: Used 0MB,  Free 61MB, Total 61MB]{lang="EN-US"}]{#struct_0_10889_x4909_938363822}

[[Cfa0]{lang="EN-US"}]{#struct_0_10889_x4909_1959849982}[表示磁盘的名称，]{style="font-family:宋体"}[Used]{lang="EN-US"}[表示整个磁盘已使用空间的大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[），]{style="font-family:宋体"}[Free]{lang="EN-US"}[表示整个磁盘当前空闲空间的大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[），]{style="font-family:宋体"}[Total]{lang="EN-US"}[表示整个磁盘空间大小（单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}[）。]{style="font-family:宋体"}[如果]{style="font-family:宋体"}[Context]{lang="EN-US"}[没有启动，]{style="font-family:宋体"}[则]{style="font-family:宋体"}[Used]{lang="EN-US"}[会显示为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[ID]{lang="EN-US"}]{#struct_0_10889_x4909_1903463049}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1940607289}[的编号]{style="font-family:宋体"}

[[name]{lang="EN-US"}]{#struct_0_10889_x4909_529593527}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_176989294}[的名字]{style="font-family:宋体"}

[[Weight]{lang="EN-US"}]{#struct_0_10889_x4909_520502269}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_616769975}[使用]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的权重值]{style="font-family:宋体"}

[[Usage(%)]{lang="EN-US"}]{#struct_0_10889_x4909_x1150483231}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x975772124}[对]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的实际占用率，用百分比表示]{style="font-family:宋体"}

[[Quota(MB)]{lang="EN-US"}]{#struct_0_10889_x4909_340454362}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1658562356}[使用磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存的限制值，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}

[[Used(MB)]{lang="EN-US"}]{#struct_0_10889_x4909_1903463046}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1940803897}[当前已使用的磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存空间的大小，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}

[[Free(MB)]{lang="EN-US"}]{#struct_0_10889_x4909_x2078876189}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x909362961}[还可以使用的磁盘]{style="font-family:宋体"}[/]{lang="EN-US"}[内存空间的大小，单位为]{style="font-family:宋体"}[MB]{lang="EN-US"}

[ ]{lang="EN-US"}

::::: {#-564377485 .myid}
[]{#_Toc404783311}[]{#struct_0_10889_x4909_979036762}

**Context \-- Context命令 \-- display context vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_x54465680}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_x1789241875}
:::

**[ ]{lang="EN-US"}**

[**[display context vlan]{lang="EN-US"}**]{#struct_0_10889_x4909_861992144}[命令用来显示]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x976639171}

[**[display context]{lang="EN-US"}**[ \[ **name** *context-name* \] **vlan**]{lang="EN-US"}]{#struct_0_10889_x4909_260368719}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1610708338}

[[任意视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1651594856}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_979036761}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x54465679}

[[network-operator]{lang="EN-US"}]{#struct_0_10889_x4909_x1833871882}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x785357847}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10889_x4909_744333941}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x794279069}

[**[name]{lang="EN-US"}**[ *context-name*]{lang="EN-US"}]{#struct_0_10889_x4909_107351049}[：]{style="font-family:宋体"}[Context]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1727018093}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[包装防火墙]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_471259312}

[[在缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1152740747}[中，可使用]{style="font-family:宋体"}**[name]{lang="EN-US"}**[ *context-name*]{lang="EN-US"}[参数查看指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表；不指定]{style="font-family:宋体"}**[name]{lang="EN-US"}**[ *context-name*]{lang="EN-US"}[参数时，则显示设备上创建的所有]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[防火墙插卡]{lang="EN-US" style="font-family:宋体"}]{#struct_0_10889_x4909_883339175}

[[可使用]{style="font-family:宋体"}**[name]{lang="EN-US"}**[ *context-name*]{lang="EN-US"}]{#struct_0_10889_x4909_1655814765}[参数查看指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表；不指定]{style="font-family:宋体"}**[name]{lang="EN-US"}**[ *context-name*]{lang="EN-US"}[参数时，则显示所有属于当前登录]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1860719010}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_979036764}[显示所有]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[\<Sysname\> display context vlan]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_x54465674}

[[Context stub1\'s VLAN(s):]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_x1833871887}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[Context stub2\'s VLAN(s):]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_x25842960}

[[  2,4094]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_x2065947962}

[[Context stub3\'s VLAN(s):]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_471484878}

[[  5,6,800-3000,3400]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_x573467767}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x715830901}[显示]{style="font-family:宋体"}[Context sub1]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[\<Sysname\> display context name sub1 vlan]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_1856295712}

[[Context stub1\'s VLAN(s):]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_x52371893}

[[  5,6,11-23,3400]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10889_x4909_506635855}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x2146591208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[allocate vlan]{lang="EN-US"}**]{#struct_0_10889_x4909_1621647667}
:::::

::::: {#866923171 .myid}
[]{#_Toc404783312}[]{#struct_0_10889_x4909_x50722863}[]{#_Toc365648363}[]{#_Toc393298492}

**Context \-- Context命令 \-- join mdc**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:0cm 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_x242969194}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_139143983}
:::

**[ ]{lang="EN-US"}**

[**[join]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_10889_x4909_x879870281}**[mdc]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[Context]{lang="EN-US"}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[join]{lang="EN-US"}**]{#struct_0_10889_x4909_x1324678389}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1187050737}

[**[join]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_10889_x4909_x114526349}**[mdc ]{lang="EN-US"}***[mdc-name]{lang="EN-US"}*

[**[undo ]{lang="EN-US"}[join]{lang="EN-US"}**]{#struct_0_10889_x4909_1903463047}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1940738361}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1236766297}[属于缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x350928958}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1003067331}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1663992252}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x5751843}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1182397995}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1845635745}

[*[mdc-name]{lang="EN-US"}*]{#struct_0_10889_x4909_x201551725}[：指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的]{style="font-family:宋体"}[名称]{style="font-family:宋体"}[。该]{style="font-family:宋体"}[Context]{lang="EN-US"}[必须是已创建、未启动的]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_92825052}

[[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_x1283346527}[视图下的]{style="font-family:宋体"}**[allocate context]{lang="EN-US"}**[命令与]{style="font-family:宋体"}[Context]{lang="EN-US"}[视图下的]{style="font-family:宋体"}**[join mdc]{lang="EN-US"}**[命令功能相同，都是为]{style="font-family:宋体"}[Context]{lang="EN-US"}[设置归属]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}**[allocate context]{lang="EN-US"}**[可以批量设置归属]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，]{style="font-family:宋体"}**[join mdc]{lang="EN-US"}**[是为单个]{style="font-family:宋体"}[Context]{lang="EN-US"}[设置归属]{style="font-family:宋体"}[MDC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1903463052}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[后，]{style="font-family:宋体"}[MDC]{lang="EN-US"}[才能对外提供安全业务。]{style="font-family:宋体"}[一个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[下可以存在多个]{style="font-family:宋体"}[Context]{lang="EN-US"}[，一个]{style="font-family:宋体"}[Context]{lang="EN-US"}[只能隶属于一个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，使用这个]{style="font-family:宋体"}[MDC]{lang="EN-US"}[上的物理资源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1941066042}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_2046462751}[指定]{style="font-family:宋体"}[Context]{lang="EN-US"}[（名称为]{style="font-family:宋体"}[cnt2]{lang="EN-US"}[）]{style="font-family:宋体"}[归属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[（名称为]{style="font-family:宋体"}[test2]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_2003062432}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] join mdc test2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_95366710}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[allocate context]{lang="EN-US"}**]{#struct_0_10889_x4909_x1866493527}
:::::

::: {#305021740 .myid}
[]{#_Toc404783313}[]{#struct_0_10889_x4909_1558577985}[]{#_Toc365648370}[]{#_Toc371341031}[]{#_Toc371341032}

**Context \-- Context命令 \-- limit-resource cpu**

------------------------------------------------------------------------

[**[limit-resource cpu]{lang="EN-US"}**]{#struct_0_10889_x4909_x1242434504}[命令用来配置]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo limit-resource cpu]{lang="EN-US"}**]{#struct_0_10889_x4909_x701383233}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1566473346}

[**[limit-resource cpu]{lang="EN-US"}**[ **weight** *weight-value*]{lang="EN-US"}]{#struct_0_10889_x4909_1240117524}

[**[undo limit-resource cpu]{lang="EN-US"}**]{#struct_0_10889_x4909_x440140626}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1761153225}

[[各]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1280593537}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重均为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_90224592}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1790165382}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1903463053}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x1941000506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x629970514}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_2131755451}

[**[weight ]{lang="EN-US"}***[weight-value]{lang="EN-US"}*]{#struct_0_10889_x4909_x488849033}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Context]{lang="EN-US"}[在指定安全引擎上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}[系统根据]{style="font-family:宋体"}[Context]{lang="EN-US"}[的权重为]{style="font-family:宋体"}[Context]{lang="EN-US"}[分配]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时间。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1210848562}

[[进驻到同一安全引擎的]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1757501189}[共享该安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[资源。]{style="font-family:宋体"}[配置本命令后，]{style="font-family:宋体"}[Context]{lang="EN-US"}[在己进驻的安全引擎上都将获得相同的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[权重。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x624619068}

[[\#]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[ ]{lang="EN-US"}]{#struct_0_10889_x4909_x1931797746}[配置]{style="font-size:10.5pt;font-family:宋体"}[Context]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[的]{style="font-size:10.5pt;font-family:宋体"}[CPU]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[权重为]{style="font-size:10.5pt;font-family:宋体"}[2]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[。]{style="font-size:10.5pt;font-family:宋体"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource cpu weight 2]{lang="EN-US"}
:::

::: {#-1683769703 .myid}
[]{#_Toc404783314}[]{#struct_0_10889_x4909_x172962427}[]{#_Toc365648368}

**Context \-- Context命令 \-- limit-resource disk**

------------------------------------------------------------------------

[**[limit-resource disk]{lang="EN-US"}**]{#struct_0_10889_x4909_363785240}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[Context]{lang="EN-US"}[可使用的磁盘空间上限]{style="font-family:宋体"}[（用百分比表示）。]{style="font-family:宋体"}

[**[undo limit-resource disk]{lang="EN-US"}**]{#struct_0_10889_x4909_2041115750}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x52852092}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x347406022}

[**[limit-resource disk ratio ]{lang="EN-US"}**]{#struct_0_10889_x4909_931419566}*[limit-ratio]{lang="EN-US" style="font-size:11.0pt"}*

[**[undo limit-resource disk]{lang="EN-US"}**]{#struct_0_10889_x4909_898007265}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_10889_x4909_x18700342}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[limit-resource disk slot]{lang="EN-US"}**[ *slot-number* **cpu** *cpu-number* **ratio** *limit-ratio*]{lang="EN-US"}]{#struct_0_10889_x4909_x110375059}

[**[undo limit-resource disk slot]{lang="EN-US"}**[ *slot-number* **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_135213074}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_10889_x4909_2055808246}[模式：]{style="font-family:宋体"}

[**[limit-resource disk chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ cpu]{lang="EN-US"}**[ *cpu-number* **ratio** *limit-ratio*]{lang="EN-US"}]{#struct_0_10889_x4909_x2042839964}

[**[undo limit-resource disk chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_1765403201}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x731729640}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x2072004195}[可以使用物理设备上的所有空闲磁盘空间。（集中式设备）]{style="font-family:宋体"}

[[进驻到同一安全引擎的所有]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x2137124106}[共享该安全引擎的所有磁盘空间，每个]{style="font-family:宋体"}[Context]{lang="EN-US"}[可使用的磁盘空间上限为该安全引擎的空闲磁盘空间值。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="line-height:150%;font-family:宋体"}[/]{lang="EN-US" style="line-height:150%"}[集中式]{style="line-height:150%;font-family:
宋体"}[IRF]{lang="EN-US" style="line-height:150%"}[设备[/]{lang="EN-US"}]{style="line-height:150%;font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1301696986}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1854908331}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_795149938}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1247820508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x52852091}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x347406025}

[**[slot]{lang="EN-US" style="color:black"}**]{#struct_0_10889_x4909_931616174}[ *slot-number* **cpu** *cpu-number*]{lang="EN-US" style="color:black"}[：表示安全引擎所在的位置，其中，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示安全引擎所在的槽位号，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示安全引擎的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number* **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_1967304311}[：表示成员设备安全引擎所在的位置，其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示安全引擎所在的设备的成员编号，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示安全引擎的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_85272156}[：表示成员设备安全引擎所在的位置，其中，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示安全引擎所在的设备的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示安全引擎所在的槽位号，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示安全引擎的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;
color:black"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}**]{#struct_0_10889_x4909_x488582494}*[limit-ratio]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[Context]{lang="EN-US"}[在设备上最多可使用的磁盘空间大小与该设备整个磁盘空间大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}**]{#struct_0_10889_x4909_x401684707}*[limit-ratio]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[Context]{lang="EN-US"}[在指定安全引擎上最多可使用的磁盘空间大小与该安全引擎整个磁盘空间大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x466369520}

[[缺省情况下，所有的]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_310767784}[共享]{style="font-family:宋体"}[已进驻的安全引擎的所有磁盘空间]{style="font-family:宋体"}[。只要磁盘物理空间足够，就可以无限制使用。为了防止单个]{style="font-family:宋体"}[Context]{lang="EN-US"}[过多的占用磁盘而影响其它]{style="font-family:宋体"}[Context]{lang="EN-US"}[，特别是为防止异常情况下对磁盘的占用，可以为指定的]{style="font-family:宋体"}[Context]{lang="EN-US"}[配置]{style="font-family:宋体"}[磁盘上限。]{style="font-family:宋体"}

[[请在]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1948547455}[启动后配置磁盘上限。执行]{style="font-family:宋体"}**[limit-resource disk]{lang="EN-US"}**[命令前，请使用]{style="font-family:宋体"}**[display context resource]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}[Context]{lang="EN-US"}[当前实际已经使用的磁盘空间大小。配置值应大于]{style="font-family:宋体"}[Context]{lang="EN-US"}[当前实际已经使用的磁盘空间大小，否则，会导致]{style="font-family:宋体"}[Context]{lang="EN-US"}[申请新的磁盘空间失败，从而无法进行文件夹创建、文件拷贝和保存等操作。]{style="font-family:宋体"}

[[如果设备上有多块磁盘，该命令对所有磁盘生效。]{style="font-family:宋体"}]{#struct_0_10889_x4909_x2071807587}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_788466113}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x492449438}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[最多可使用设备磁盘空间的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x546632525}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource disk ratio 30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1136142423}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板上安全引擎磁盘空间的]{style="font-family:宋体"}[20%]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x52852094}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource disk slot 3 cpu 1 ratio 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x347406020}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上安全引擎磁盘空间的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_931288494}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource disk slot 2 cpu 1 ratio 30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x506726875}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板上安全引擎]{style="font-family:宋体"}[磁盘空间的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x599270725}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource disk chassis 2 slot 3 cpu 1 ratio 30]{lang="EN-US"}
:::

::: {#2136473035 .myid}
[]{#_Toc404783315}[]{#struct_0_10889_x4909_x2006243968}[]{#_Toc365648369}

**Context \-- Context命令 \-- limit-resource memory**

------------------------------------------------------------------------

[**[limit-resource memory]{lang="EN-US"}**]{#struct_0_10889_x4909_x1096476176}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[Context]{lang="EN-US"}[可使用的内存空间上限]{style="font-family:宋体"}[（用百分比表示）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo limit-resource memory]{lang="EN-US"}**]{#struct_0_10889_x4909_602315047}[命令用来恢复到缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_979047931}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_10889_x4909_1527667806}

[**[limit-resource ]{lang="EN-US"}**]{#struct_0_10889_x4909_x922370302}**[memory]{lang="EN-US"}[ ratio]{lang="EN-US"}[ ]{lang="EN-US"}***[limit-ratio]{lang="EN-US"}*

[**[undo limit-resource ]{lang="EN-US"}**]{#struct_0_10889_x4909_x1848639241}**[memory]{lang="EN-US"}**

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10889_x4909_x564239455}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[limit-resource ]{lang="EN-US"}**]{#struct_0_10889_x4909_x52852093}**[memory]{lang="EN-US"}**[ **slot** *slot-number* **cpu** *cpu-number* **ratio** *limit-ratio*]{lang="EN-US"}

[**[undo limit-resource ]{lang="EN-US"}**]{#struct_0_10889_x4909_x347406023}**[memory]{lang="EN-US"}**[ **slot** *slot-number* **cpu** *cpu-number*]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_10889_x4909_x499221585}[模式：]{style="font-family:宋体"}

[**[limit-resource ]{lang="EN-US"}**]{#struct_0_10889_x4909_x624185120}**[memory]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number* **ratio** *limit-ratio*]{lang="EN-US"}

[**[undo limit-resource ]{lang="EN-US"}**]{#struct_0_10889_x4909_1997906693}**[memory]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_906510533}

[[所有]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x2071742051}[共享物理设备上的所有内存空间，每个]{style="font-family:宋体"}[Context]{lang="EN-US"}[可使用的内存空间上限为空闲内存空间值。（集中式设备）]{style="font-family:宋体"}

[[进驻到同一安全引擎的所有]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1272792901}[共享该安全引擎的所有内存空间，每个]{style="font-family:宋体"}[Context]{lang="EN-US"}[可使用的内存空间上限为该安全引擎的空闲内存空间值。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_146638801}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1251234024}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_2143040126}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1679177559}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x664568847}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1137343568}

[**[slot]{lang="EN-US" style="color:black"}**]{#struct_0_10889_x4909_x52852088}[ *slot-number* **cpu** *cpu-number*]{lang="EN-US" style="color:black"}[：表示安全引擎所在的位置，其中，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示安全引擎所在的槽位号，]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示安全引擎的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number* **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_1608909120}[：表示成员设备安全引擎所在的位置，其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备的成员编号，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示安全引擎的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;color:black"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}***[ cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_1556560951}[：表示成员设备安全引擎所在的位置，其中，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示安全引擎所在的设备的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示安全引擎所在的槽位号，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示安全引擎的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。]{style="font-family:宋体;
color:black"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}**]{#struct_0_10889_x4909_x488516958}*[limit-ratio]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[Context]{lang="EN-US"}[在设备上最多可使用的内存大小与该设备整个内存大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[**[ratio ]{lang="EN-US"}**]{#struct_0_10889_x4909_x1472912980}*[limit-ratio]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[Context]{lang="EN-US"}[在指定安全引擎上最多可使用的内存大小与该安全引擎整个内存大小的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_395533994}

[[缺省情况下，所有的]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_569655012}[共享使用]{style="font-family:宋体"}[已进驻的安全引擎的所有内存空间]{style="font-family:宋体"}[。只要物理内存足够，就可以无限制使用。为了防止单个]{style="font-family:宋体"}[Context]{lang="EN-US"}[过多的占用内存而影响其它]{style="font-family:宋体"}[Context]{lang="EN-US"}[，特别是为防止异常情况下对内存的占用，可以为指定的]{style="font-family:宋体"}[Context]{lang="EN-US"}[配置内存上限。]{style="font-family:宋体"}

[[需要注意的是，请在]{style="font-family:宋体"}]{#struct_0_10889_x4909_1739212815}[Context]{lang="EN-US"}[启动后再配置内存上限，并且配置的上限值不应过小，以免]{style="font-family:宋体"}[Context]{lang="EN-US"}[内业务申请不到内存而引起功能异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_414645907}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x1740355379}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[最多可使用设备内存的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_978122667}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource memory ratio 30]{lang="EN-US"}

[\# ]{lang="EN-US" style="font-size:10.5pt;font-family:
\"Arial\",\"sans-serif\""}[配置]{style="font-size:10.5pt;font-family:宋体"}[Context cnt2]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[最多可使用]{style="font-size:10.5pt;font-family:宋体"}[1]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[号单板安全引擎内存的]{style="font-size:10.5pt;font-family:宋体"}[30%]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[。（分布式设备－独立运行模式）]{style="font-size:10.5pt;font-family:宋体"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource memory slot 1 cpu 1 ratio 30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x1367179660}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备安全引擎内存的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x1942734481}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource memory slot 2 cpu 1 ratio 30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1452437988}[配置]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[最多可使用]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板安全引擎内存的]{style="font-family:宋体"}[30%]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x52852087}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] limit-resource memory chassis 2 slot 1 cpu 1 ratio 30]{lang="EN-US"}
:::

::::: {#870708914 .myid}
[]{#_Toc404783316}[]{#struct_0_10889_x4909_1608909117}[]{#_Toc356459225}

**Context \-- Context命令 \-- location blade-controller**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_1556364340}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_910316235}
:::

**[ ]{lang="EN-US"}**

[**[location blade-controller]{lang="EN-US"}**]{#struct_0_10889_x4909_700274850}[命令用来将安全引擎加入安全引擎组。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **location blade-controller**]{lang="EN-US"}]{#struct_0_10889_x4909_1640738423}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1944262582}

[[集中式设备[/]{lang="EN-US"}分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10889_x4909_x1709405275}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[location blade-controller slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_x1684310558}

[**[undo location blade-controller slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_x1208462181}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_10889_x4909_1000286523}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[location blade-controller chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_x2121134752}

[**[undo location blade-controller chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_x52852090}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x347406024}

[[安全引擎插入时会自动加入缺省安全引擎组。]{style="font-family:宋体"}]{#struct_0_10889_x4909_931550638}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_928910296}

[[安全引擎组]{style="font-family:宋体"}]{#struct_0_10889_x4909_2076224551}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1844443821}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x48968007}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x406698707}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x499542404}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10889_x4909_x1000850224}[：表示安全引擎所在的槽位号。（]{style="font-family:宋体"}[集中式设备[/]{lang="EN-US"}分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10889_x4909_x2072135266}[：表示安全引擎所在设备的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_10889_x4909_x223756604}[：表示安全引擎所在设备的成员编号。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10889_x4909_x710141883}[：表示安全引擎所在的槽位号。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_148790646}[：表示安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x589340797}

[[使用该命令可以：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1473371732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将一个已经在位的安全引擎加入安全引擎组，这样的命令会立即生效。]{style="font-family:宋体"}]{#struct_0_10889_x4909_x2002642865}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将一个不在位的安全引擎加入安全引擎组，这样的命令会在安全引擎插入后生效。这样的配置方式称为预配置，能够帮助用户先完成配置，再进行硬件部署。使用该方式配置前，请先规划安全引擎即将插入的位置。因为，如果配置的位置误插入非安全引擎，设备会自动将该命令删除，以后插入安全引擎时，需要重新配置。]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1018815578}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x856264027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个安全引擎只能属于一个安全引擎组。]{style="font-family:宋体"}]{#struct_0_10889_x4909_x52852089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当前，每个安全引擎组中可加入的安全引擎个数没有限制。]{style="font-family:宋体"}]{#struct_0_10889_x4909_1608909119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将安全引擎从一个安全引擎组切换到另外一个安全引擎组时，防火墙插卡会自动重启。（防火墙插卡）]{style="font-family:宋体"}]{#struct_0_10889_x4909_1557019700}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x283749043}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_986911948}[将安全引擎加入安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x1393213056}

[\[sysname\] blade-controller-team abc]{lang="EN-US"}

[\[Sysname-blade-controller-team-2-abc\] location blade-controller slot 0 cpu 1]{lang="EN-US"}

[This operation will also reboot the blade controller. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1745819814}[将]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位上]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的安全引擎加入安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_1121147969}

[\[sysname\] blade-controller-team abc]{lang="EN-US"}

[\[Sysname-blade-controller-team-2-abc\] location blade-controller slot 2 cpu 1]{lang="EN-US"}

[This operation will also reboot the blade controller. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1731444520}[将]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的安全引擎加入安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x52852084}

[\[sysname\] blade-controller-team abc]{lang="EN-US"}

[\[Sysname-blade-controller-team-2-abc\] location blade-controller slot 2 cpu 1]{lang="EN-US"}

[This operation will also reboot the blade controller. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1608909116}[将]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位上]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的安全引擎加入安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_1556429876}

[\[sysname\] blade-controller-team abc]{lang="EN-US"}

[\[Sysname-blade-controller-team-2-abc\] location blade-controller chassis 2 slot 2 cpu 1]{lang="EN-US"}

[This operation will also reboot the blade controller. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x1473175124}[将]{style="font-family:宋体"}[3]{lang="EN-US"}[号槽位上]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的安全引擎（不在位）加入安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x664511321}

[\[sysname\] blade-controller-team abc]{lang="EN-US"}

[\[Sysname-blade-controller-team-2-abc\] location blade-controller slot 3 cpu 1]{lang="EN-US"}

[Operation successed, but the blade controller is absent.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x896821823}[将]{style="font-family:宋体"}[3]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的安全引擎（不在位）加入安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_349024784}

[\[sysname\] blade-controller-team abc]{lang="EN-US"}

[\[Sysname-blade-controller-team-2-abc\] location blade-controller slot 3 cpu 1]{lang="EN-US"}

[Operation successed, but the blade controller is absent.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x62667648}[将]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备]{style="font-family:
宋体"}[3]{lang="EN-US"}[号槽位上]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的安全引擎（不在位）加入安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_x838789013}

[\[sysname\] blade-controller-team abc]{lang="EN-US"}

[\[Sysname-blade-controller-team-2-abc\] location blade-controller chassis 2 slot 3 cpu 1]{lang="EN-US"}

[Operation successed, but the blade controller is absent.]{lang="EN-US"}
:::::

::: {#-102726406 .myid}
[]{#_Toc404783317}[]{#struct_0_10889_x4909_899634376}[]{#_Toc365648362}

**Context \-- Context命令 \-- location blade-controller-team (Context view)**

------------------------------------------------------------------------

[**[location]{lang="EN-US"}**]{#struct_0_10889_x4909_x304737080}**[ blade-controller-team]{lang="EN-US"}**[命令用]{style="font-family:宋体"}[于使]{style="font-family:宋体"}[Context]{lang="EN-US"}[进驻对应的安全引擎组。]{style="font-family:宋体"}

[**[undo location]{lang="EN-US"}**]{#struct_0_10889_x4909_x776384674}**[ blade-controller-team]{lang="EN-US"}**[命令用于将]{style="font-family:宋体"}[Context]{lang="EN-US"}[从安全引擎组中移除]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x728443742}

[**[location blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_715480876}*[ team-id]{lang="EN-US"}*

[**[undo location blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_x701255315}*[ team-id]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1609484345}

[[缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x1308694254}[进驻了所有安全引擎组，非缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[没有进驻任何安全引擎组。（包装防火墙）]{style="font-family:宋体"}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x488058206}[未进驻任何安全引擎组。（防火墙插卡）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x959036773}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_756692480}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x286913126}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x2017734478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x629579185}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x52852083}

[*[team-id]{lang="EN-US"}*]{#struct_0_10889_x4909_1608909113}[：]{style="font-family:宋体"}[当前已经创建的]{style="font-family:宋体"}[安全引擎组的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1556626484}

[[如果没有进驻安全引擎]{style="font-family:宋体"}]{#struct_0_10889_x4909_2077780276}**[，]{style="font-family:宋体"}**[即使]{style="font-family:宋体"}[Context]{lang="EN-US"}[已经启动，]{style="font-family:宋体"}[Context]{lang="EN-US"}[也没有实际运行的环境，无法运行业务。]{style="font-family:宋体"}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_1099376748}[进驻安全引擎组后，才能使用安全引擎组中安全引擎上的资源，包括]{style="font-family:宋体"}[CPU]{lang="EN-US"}[、磁盘和内存。]{style="font-family:宋体"}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_x369475070}[和安全引擎组的关系如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_10889_x4909_1197959248}[Context]{lang="EN-US"}[只能进驻一个安全引擎组。如果该]{style="font-family:宋体"}[Context]{lang="EN-US"}[已经进驻一个安全引擎组，请先执行]{style="font-family:宋体"}**[undo location]{lang="EN-US"}[ blade-controller-team]{lang="EN-US"}**[命令退出已进驻的安全引擎组，再配置]{style="font-family:宋体"}**[location]{lang="EN-US"}[ blade-controller-team]{lang="EN-US"}**[命令，进驻其它安全引擎组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在不同的]{style="font-family:宋体"}]{#struct_0_10889_x4909_1208368663}[Context]{lang="EN-US"}[视图下执行该命令可以使多个]{style="font-family:宋体"}[Context]{lang="EN-US"}[进驻同一个安全引擎组。最多可以有]{style="font-family:宋体"}[256]{lang="EN-US"}[个]{style="font-family:宋体"}[Context]{lang="EN-US"}[进驻到同一个安全引擎组，安全引擎组和]{style="font-family:宋体"}[Context]{lang="EN-US"}[是一对多的关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[安全引擎组中加入新的安全引擎后，安全引擎组上已进驻的]{style="font-family:宋体"}]{#struct_0_10889_x4909_x82065181}[Context]{lang="EN-US"}[会自动进驻到新加入的安全引擎上，不需要再次配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_863860276}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x494266447}[将]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[进驻到安全引擎组]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_1199967925}

[\[Sysname\] context cnt2]{lang="EN-US"}

[\[Sysname-context-2-cnt2\] location blade-controller-team 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1385968609}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_248233796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[location blade-controller-team]{lang="EN-US"}**[ (MDC view)]{lang="EN-US"}]{#struct_0_10889_x4909_x2071676514}
:::

::::: {#1091136757 .myid}
[]{#_Toc404783318}[]{#struct_0_10889_x4909_x1903179747}

**Context \-- Context命令 \-- location blade-controller-team (MDC view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_1521126020}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令只有防火墙插卡设备支持。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_x1697494388}
:::

[ ]{lang="EN-US"}

[**[location]{lang="EN-US"}**]{#struct_0_10889_x4909_1265000086}**[ blade-controller-team]{lang="EN-US"}**[命令用]{style="font-family:宋体"}[来使]{style="font-family:宋体"}[MDC]{lang="EN-US"}[进驻对应的安全引擎组。]{style="font-family:宋体"}

[**[undo location]{lang="EN-US"}**]{#struct_0_10889_x4909_x215198780}**[ blade-controller-team]{lang="EN-US"}**[命令用来将]{style="font-family:宋体"}[MDC]{lang="EN-US"}[从安全引擎组中移除]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1080588010}

[**[location blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_1635242488}*[ team-id]{lang="EN-US"}*

[**[undo location blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_x991822198}*[ team-id]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_10889_x4909_885800314}

[[缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_540860621}[进驻了所有安全引擎组，非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[没有进驻任何安全引擎组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1347812577}

[[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_146758045}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x875670746}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_529990341}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_695920850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x78992350}

[*[team-id]{lang="EN-US"}*]{#struct_0_10889_x4909_1521126021}[：]{style="font-family:宋体"}[当前已经创建的]{style="font-family:宋体"}[安全引擎组的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1697428852}

[[Context]{lang="EN-US"}]{#struct_0_10889_x4909_638829580}[从属于]{style="font-family:宋体"}[MDC]{lang="EN-US"}[，]{style="font-family:宋体"}[Context]{lang="EN-US"}[必须依附于所属]{style="font-family:宋体"}[MDC]{lang="EN-US"}[环境。为了使]{style="font-family:宋体"}[Context]{lang="EN-US"}[能进驻安全引擎，必须先将其所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[进驻到该安全引擎。]{style="font-family:宋体"}

[[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_1028956338}[和安全引擎组的关系如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行该命令可以使一个]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_1355958658}[进驻多个不同的安全引擎组。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在不同的]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_x1629042489}[视图下执行该命令可以使多个]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[进驻同一个安全引擎组。]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[进驻安全引擎组后，该]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[会进驻引擎组内所有安全引擎。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1937649265}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[该命令用于]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1609893490}[MDC]{lang="EN-US"}[进驻引擎组。]{style="font-family:宋体"}[要使]{lang="EN-US" style="font-family:宋体"}[MDC]{lang="EN-US"}[下的]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[进驻安全引擎组，请在对应的]{lang="EN-US" style="font-family:宋体"}[Context]{lang="EN-US"}[视图下执行]{lang="EN-US" style="font-family:宋体"}**[location ]{lang="EN-US"}[blade-controller-team]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **location** ]{lang="EN-US"}]{#struct_0_10889_x4909_x673127668}**[blade-controller-team]{lang="EN-US"}**[命令时，要求本]{lang="EN-US" style="font-family:
宋体"}[MDC]{lang="EN-US"}[内不存在任何]{lang="EN-US" style="font-family:
宋体"}[Context]{lang="EN-US"}[。否则，命令执行失败。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1681803520}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_827326928}[使]{style="font-family:宋体"}[MDC sub1]{lang="EN-US"}[进驻安全引擎组]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_1640641895}

[\[Sysname\] mdc sub1]{lang="EN-US"}

[\[Sysname-mdc-2-sub1\] location blade-controller-team 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x329926601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_x544270201}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[location blade-controller-team]{lang="EN-US"}**[ (Context view)]{lang="EN-US"}]{#struct_0_10889_x4909_x2071610978}
:::::

::::: {#-1594610173 .myid}
[]{#_Toc404783319}[]{#struct_0_10889_x4909_x1472585300}

**Context \-- Context命令 \-- reset blade-controller-team**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Context命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_10889_x4909_1242114541}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_10889_x4909_x1738641073}
:::

[ ]{lang="EN-US"}

[**[reset blade-controller-team]{lang="EN-US"}**]{#struct_0_10889_x4909_x1473044051}[命令用来清除指定安全引擎组中不在位的安全引擎的数据信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1271629032}

[[集中式设备[/]{lang="EN-US"}分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_10889_x4909_1766857551}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset blade-controller-team]{lang="EN-US"}**[ *team-id* **member slot** *slot-number* **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_x509377787}

[[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_10889_x4909_x1972875543}[设备：]{style="font-family:宋体"}

[**[reset blade-controller-team ]{lang="EN-US"}***[team-id ]{lang="EN-US"}***[member chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ **cpu** *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_1769751926}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_2061289475}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_982456007}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_193417568}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_916901357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1366282026}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_204291394}

[*[team-id]{lang="EN-US"}*]{#struct_0_10889_x4909_x1473109587}[：安全引擎所属安全引擎组的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。可使用]{style="font-family:宋体"}**[display blade-controller-team]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10889_x4909_389778959}[：表示]{style="font-family:宋体"}[安全引擎]{style="font-family:宋体"}[所在的槽位号。（]{style="font-family:宋体"}[集中式[/]{lang="EN-US"}分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10889_x4909_x488451429}[：表示安全引擎所在设备的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_10889_x4909_x772458796}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[安全引擎所在设备]{style="font-family:宋体"}[的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示安全引擎所在的槽位号]{style="font-family:宋体"}[。（]{style="font-family:宋体"}[分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_10889_x4909_1128095151}[：表示]{style="font-family:宋体"}[安全引擎]{style="font-family:宋体"}[的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1212885486}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x1339467862}[清除安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[安全引擎（编号]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，所]{style="font-family:
宋体"}[在位置为]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[）]{style="font-family:宋体"}[的数据信息]{style="font-family:宋体"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<sysname\> reset blade-controller-team 1 member slot 2 cpu 1]{lang="EN-US"}]{#struct_0_10889_x4909_x1700872923}

[This operation will cause a short interruption of NAT session. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Erasing the controller data successed.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_1218052677}[清除安全引擎组]{style="font-family:宋体"}[abc]{lang="EN-US"}[中]{style="font-family:宋体"}[安全引擎（编号]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:
宋体"}[所在位]{style="font-family:宋体"}[置为]{style="font-family:
宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:宋体"}[CPU]{lang="EN-US"}[）]{style="font-family:宋体"}[的数据信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<sysname\> reset blade-controller-team 1 member chassis 1 slot 2 cpu 1]{lang="EN-US"}]{#struct_0_10889_x4909_x1472912979}

[This operation will cause a short interruption of NAT session. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Erasing the controller data successed.]{lang="EN-US"}
:::::

::: {#1786297017 .myid}
[]{#_Toc404783320}[]{#struct_0_10889_x4909_1521126018}[]{#_Toc380149851}

**Context \-- Context命令 \-- switchto context**

------------------------------------------------------------------------

[**[switchto context]{lang="EN-US"}**]{#struct_0_10889_x4909_x1698018679}[命令用来登录到指定的]{style="font-family:宋体"}[Context]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_10889_x4909_553765301}

[**[switchto context ]{lang="EN-US"}**]{#struct_0_10889_x4909_5536120}*[context-name]{lang="EN-US"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_10889_x4909_276038875}

[[系统视图]{style="font-family:宋体"}]{#struct_0_10889_x4909_x1180851764}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x991709340}

[[network-admin]{lang="EN-US"}]{#struct_0_10889_x4909_x659026735}

[[network-operator]{lang="EN-US"}]{#struct_0_10889_x4909_40646149}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10889_x4909_1875645918}

[[mdc-operator]{lang="EN-US"}]{#struct_0_10889_x4909_1743164053}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1253732685}

[*[context-name]{lang="EN-US"}*]{#struct_0_10889_x4909_324549490}[：已启动的]{style="font-family:宋体"}[Context]{lang="EN-US"}[的]{style="font-family:宋体"}[名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_10889_x4909_x1850185364}

[[只要用户和物理设备之间路由可达，就能]{style="font-family:宋体"}]{#struct_0_10889_x4909_x290226513}[使用该命令，通过物理设备]{style="font-family:
宋体"}[和]{style="font-family:宋体"}[Context]{lang="EN-US"}[的内联接口，登录]{style="font-family:宋体"}[Context]{lang="EN-US"}[。（不]{style="font-family:宋体"}[支]{style="font-family:宋体"}[持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设]{style="font-family:宋体"}[备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[只要用户和]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_10889_x4909_1615924920}[之间路由可达，就能]{style="font-family:宋体"}[使用该命令，通过]{style="font-family:宋体"}[MDC]{lang="EN-US"}[和]{style="font-family:宋体"}[Context]{lang="EN-US"}[的内联接口，登录]{style="font-family:宋体"}[Context]{lang="EN-US"}[。请在]{style="font-family:宋体"}[Context]{lang="EN-US"}[所属的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[环境下执行该命令。例如，]{style="font-family:宋体"}[Context cnt2]{lang="EN-US"}[属于]{style="font-family:宋体"}[MDC test]{lang="EN-US"}[，则必须先通过]{style="font-family:宋体"}**[switchto mdc]{lang="EN-US"}**[命令或者]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[等方式登录到]{style="font-family:宋体"}[MDC test]{lang="EN-US"}[，再通过]{style="font-family:宋体"}**[switchto context]{lang="EN-US"}**[命令登录到]{style="font-family:宋体"}[cnt2]{lang="EN-US"}[。]{style="font-family:宋体"}[（支]{style="font-family:宋体"}[持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设]{style="font-family:宋体"}[备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10889_x4909_1521126019}

[[\# ]{lang="EN-US"}]{#struct_0_10889_x4909_x1697953143}[切换到]{style="font-family:宋体"}[Context test2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_10889_x4909_996860913}

[\[Sysname\] switchto context test2]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*]{lang="EN-US"}

[\* Without the owner\'s prior written consent,                                 \*]{lang="EN-US"}

[\* no decompiling or reverse-engineering shall be allowed.                    \*]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[ ]{lang="EN-US"}

[\<Context2\>]{lang="EN-US"}
:::
