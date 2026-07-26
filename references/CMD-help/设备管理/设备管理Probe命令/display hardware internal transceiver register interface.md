::::: {#-1436686529 .myid}
[]{#_Toc404800672}[]{#struct_0_13030_15280_x419292956}[]{#_Toc339630670}[]{#_Toc322446699}[]{#_Toc322446704}

**设备管理 \-- 设备管理Probe命令 \-- display hardware internal transceiver register interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](设备管理Probe命令.files/image001.png){#图片 20 width="62" height="25"}]{lang="EN-US"}]{#struct_0_13030_15280_667412672}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_13030_15280_1934480064}
:::

[ ]{lang="EN-US"}

[**[d]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_1314985109}**[isplay hardware internal transceiver register interface]{lang="EN-US"}**[命令]{style="font-family:宋体"}[用来]{style="font-family:宋体"}[显示可插拔光模块上指定寄存器区域的内容，用十六进制数表示。]{style="font-size:10.0pt;font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13030_15280_x1434754609}

[**[d]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_31908935}**[isplay hardware internal transceiver register interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}***[ device ]{lang="EN-US"}***[device-index]{lang="EN-US"}***[ address ]{lang="EN-US"}***[start-address]{lang="EN-US"}***[ length ]{lang="EN-US"}***[region-length]{lang="EN-US"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_13030_15280_360601969}

[[Probe]{lang="EN-US"}]{#struct_0_13030_15280_x234146589}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13030_15280_x1493632814}

[[network-admin]{lang="EN-US"}]{#struct_0_13030_15280_x1980257065}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13030_15280_1234165908}

[**[interface]{lang="EN-US"}**]{#struct_0_13030_15280_915000821}[ *interface-type interface-number*]{lang="EN-US"}[：显示接口上插入的可插拔光模块上的寄存器信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}

[**[device]{lang="EN-US"}**[ device-index]{lang="EN-US"}]{#struct_0_13030_15280_x45160592}[：表示指定接口上光模块内部寄存器的]{style="font-family:宋体"}[索引号，用]{style="font-size:10.0pt;font-family:宋体;color:black"}[十六]{style="font-size:10.0pt;font-family:宋体;color:black"}[进制数表示，取值范围为]{style="font-size:10.0pt;font-family:宋体;color:black"}[0]{lang="EN-US" style="font-size:10.0pt;color:black"}[～]{style="font-size:
10.0pt;font-family:宋体;color:black"}[FF]{lang="EN-US" style="font-size:
10.0pt;color:black"}[。]{style="font-size:10.0pt;font-family:宋体;
color:black"}

[**[address ]{lang="EN-US"}**]{#struct_0_13030_15280_356690882}*[start-address]{lang="EN-US"}*[：]{style="font-family:宋体"}[起始地址，即需要显示的寄存器区域的起始点的偏移地址。用]{style="font-size:10.0pt;font-family:宋体;color:black"}[十六]{style="font-size:10.0pt;font-family:宋体;color:black"}[进制数表示，取值范围为]{style="font-size:10.0pt;font-family:宋体;color:black"}[0]{lang="EN-US" style="font-size:10.0pt;color:black"}[～]{style="font-size:
10.0pt;font-family:宋体;color:black"}[FFFF]{lang="EN-US" style="font-size:
10.0pt;color:black"}[。]{style="font-size:10.0pt;font-family:宋体;
color:black"}

[**[length ]{lang="EN-US"}**]{#struct_0_13030_15280_1321903464}*[region-length]{lang="EN-US"}*[：]{style="font-family:宋体"}[寄存器区域的长度，即需要显示的寄存器区域的字节数]{style="font-size:10.0pt;font-family:宋体;
color:black"}[。用十]{style="font-family:宋体"}[进制数表示，取值范围为]{style="font-size:10.0pt;font-family:宋体;color:black"}[1]{lang="EN-US" style="font-size:10.0pt;color:black"}[～]{style="font-size:
10.0pt;font-family:宋体;color:black"}[256]{lang="EN-US" style="font-size:
10.0pt;color:black"}[。]{style="font-size:10.0pt;font-family:宋体;
color:black"}
:::::

::: {#743724273 .myid}
[]{#_Toc404800673}[]{#struct_0_13030_15280_x1908339888}[]{#_Toc339630671}[]{#_Toc257634905}[]{#_Toc360006436}[]{#_Toc361126818}[]{#_Toc360006437}[]{#_Toc361126819}[]{#_Toc360006438}[]{#_Toc361126820}[]{#_Toc360006439}[]{#_Toc361126821}[]{#_Toc360006440}[]{#_Toc361126822}[]{#_Toc360006441}[]{#_Toc361126823}[]{#_Toc360006442}[]{#_Toc361126824}[]{#_Toc360006443}[]{#_Toc361126825}[]{#_Toc360006444}[]{#_Toc361126826}[]{#_Toc360006445}[]{#_Toc361126827}[]{#_Toc360006446}[]{#_Toc361126828}[]{#_Toc322446705}[]{#_Toc257634904}[]{#_Toc139168962}

**设备管理 \-- 设备管理Probe命令 \-- display system internal dbm**

------------------------------------------------------------------------

[**[display system internal dbm]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_516899545}[命令用来显示数据库信息]{style="font-size:10.0pt;font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13030_15280_x228554555}

[[集中式设备：]{style="font-size:10.0pt;font-family:宋体;color:black"}]{#struct_0_13030_15280_x331600174}

[**[display system internal dbm]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_x1430723882}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[{ ]{lang="EN-US"}**[all]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ \| **name** *dbname* ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ ]{lang="EN-US"}**[key]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ *keyname*]{lang="EN-US" style="font-size:10.0pt;color:black"}[ \] }]{lang="EN-US"}

[[分布式设备－独立运行模式[/]{lang="EN-US"}集中式]{style="font-family:宋体"}]{#struct_0_13030_15280_x1974287897}[IRF]{lang="EN-US"}[设备[:]{lang="EN-US"}]{style="font-family:宋体"}

[**[display system internal dbm]{lang="EN-US" style="font-size:
10.0pt;color:black"}**]{#struct_0_13030_15280_360470897}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[{ ]{lang="EN-US"}**[all]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\|]{lang="EN-US"}[ **name** *dbname* ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\[ ]{lang="EN-US"}**[key]{lang="EN-US" style="font-size:10.0pt;color:black"}**[ *keyname*]{lang="EN-US" style="font-size:10.0pt;color:black"}[ \] } { ]{lang="EN-US"}**[slot]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[ *slot-number*]{lang="EN-US" style="font-size:10.0pt;
color:black"}[ }]{lang="EN-US"}

[[分布]{style="font-family:宋体"}]{#struct_0_13030_15280_724287591}[式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal dbm]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_222219654}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[{]{lang="EN-US"}[ **all** ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\|]{lang="EN-US"}[ **name** *dbname*]{lang="EN-US" style="font-size:10.0pt;color:black"}[ \[]{lang="EN-US"}[ **key** *keyname*]{lang="EN-US" style="font-size:10.0pt;color:black"}[ \] } { ]{lang="EN-US"}**[chassis]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[ *chassis-number* **slot** *slot-number* ]{lang="EN-US" style="font-size:10.0pt;
color:black"}[}]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13030_15280_x309838396}

[[Probe]{lang="EN-US"}]{#struct_0_13030_15280_x323447099}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13030_15280_1445760196}

[[network-admin]{lang="EN-US"}]{#struct_0_13030_15280_1885029230}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13030_15280_x2015475914}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13030_15280_906211226}

[**[all]{lang="EN-US"}**]{#struct_0_13030_15280_1517987533}[：表示所有数据库。]{style="font-family:宋体"}

[**[name]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_1452505241}[ *dbname*]{lang="EN-US" style="font-size:10.0pt;color:black"}[：]{style="font-family:宋体"}[指定数据库名。]{style="font-family:宋体"}

[**[key]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_x201073309}[ *keyname*]{lang="EN-US" style="font-size:10.0pt;color:black"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[key]{lang="EN-US"}[的名称，在数据库中以]{style="font-family:宋体"}[key]{lang="EN-US"}[名称标识一项数据。]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_x1086187947}[ *slot-number*]{lang="EN-US" style="font-size:10.0pt;color:black"}[：表示单板所在的槽位号。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-size:10.0pt;
font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_1642695408}[ *slot-number*]{lang="EN-US" style="font-size:10.0pt;color:black"}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US" style="font-size:10.0pt;color:black"}**]{#struct_0_13030_15280_x1649678910}[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="font-size:10.0pt;color:black"}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US" style="font-size:10.0pt;color:black"}*[表示设备在]{style="font-size:10.0pt;font-family:宋体;color:black"}[IRF]{lang="EN-US" style="font-size:10.0pt;color:black"}[中的成员编号]{style="font-size:10.0pt;font-family:宋体;color:black"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="font-size:10.0pt;
color:black"}*[表示单板所在的槽位号。（分布式设备－]{style="font-size:10.0pt;font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="font-size:
10.0pt;color:black"}[模式）]{style="font-size:10.0pt;font-family:宋体;
color:black"}
:::

::: {#-272963754 .myid}
[]{#_Toc404800674}[]{#struct_0_13030_15280_x1498635681}[]{#_Toc381194819}[]{#_Toc360006448}[]{#_Toc360006449}[]{#_Toc360006450}[]{#_Toc360006451}[]{#_Toc360006452}[]{#_Toc360006453}[]{#_Toc360006454}[]{#_Toc360006455}[]{#_Toc360006456}[]{#_Toc360006457}[]{#_Toc360006458}[]{#_Toc360006459}[]{#_Toc360006460}[]{#_Toc360006461}[]{#_Toc360006462}[]{#_Toc360006463}[]{#_Toc360006464}[]{#_Toc360006465}[]{#_Toc360006466}[]{#_Toc360006467}[]{#_Toc360006468}[]{#_Toc360006469}[]{#_Toc360006470}[]{#_Toc360006471}[]{#_Toc360006472}[]{#_Toc360006473}[]{#_Toc322446707}[]{#_Toc322446708}[]{#_Toc360006495}[]{#_Toc322446706}

**设备管理 \-- 设备管理Probe命令 \-- display transceiver information interface**

------------------------------------------------------------------------

[**[display transceiver information interface]{lang="EN-US"}**]{#struct_0_13030_15280_x640331807}[命令用来显示光模块的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13030_15280_x336034393}

[**[display transceiver information interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_13030_15280_1311772474}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13030_15280_x739239019}

[[Probe]{lang="EN-US"}]{#struct_0_13030_15280_x359263698}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13030_15280_2051511309}

[[network-admin]{lang="EN-US"}]{#struct_0_13030_15280_585147416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13030_15280_1096368683}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13030_15280_598979568}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13030_15280_580365844}[：显示接口上插入的可插拔光模块的详细信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号，如果不指定该参数，表示所有接口。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
