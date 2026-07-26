::: {#3265328 .myid}
[]{#_Toc404793963}[]{#struct_0_x1477_x1861_221206898}[]{#_Toc343703752}

**加密引擎 \-- 加密引擎配置命令 \-- crypto-engine accelerator disable**

------------------------------------------------------------------------

[**[crypto-engine accelerator disable]{lang="EN-US"}**]{#struct_0_x1477_x1861_2041617780}[命令用来关闭硬件加密引擎。]{style="font-family:宋体"}

[**[undo crypto-engine accelerator disable]{lang="EN-US"}**]{#struct_0_x1477_x1861_486338696}[命令用来开启硬件加密引擎。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x204342714}

[**[crypto-engine accelerator disable]{lang="EN-US"}**]{#struct_0_x1477_x1861_1396639692}

[**[undo crypto-engine accelerator disable]{lang="EN-US"}**]{#struct_0_x1477_x1861_1814904575}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1371285907}

[[硬件加密引擎处于开启状态。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1466144012}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_494610362}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1477_x1861_221272434}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_1636354805}

[[network-admin]{lang="EN-US"}]{#struct_0_x1477_x1861_1298285265}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1477_x1861_x526272830}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x879629846}

[[无]{style="font-family:宋体"}]{#struct_0_x1477_x1861_1032710482}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x22604622}

[[加密引擎包括硬件加密引擎和软件加密引擎两种类型。硬件加密引擎可以是集成在]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1477_x1861_x959441088}[上的协处理器或者硬件加密卡；软件加密引擎指设备上的软件加密算法。]{style="font-family:宋体"}

[[开启硬件加密引擎加密功能，是指开启硬件加密引擎来加速加密过程。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x71008778}

[[当硬件加密引擎加密功能处于开启状态时，设备会优先选择使用硬件加密引擎对数据进行加密处理，如果硬件加密引擎不支持某种加密算法，则设备会使用软件加密引擎进行加密处理；如果硬件加密引擎加密功能关闭，则设备只能使用软件加密引擎进行加密处理。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x239778229}

[[硬件加密引擎的开启或关闭状态的改变对业务模块的影响由业务模块决定，例如，对于]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x1477_x1861_221337970}[业务来说，硬件加密引擎状态的改变只对新建立的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[有影响，已建的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[仍旧使用之前选择的加密引擎来处理。因此，建议在开启或关闭硬件加密引擎之后，使用]{style="font-family:宋体"}**[reset ipsec sa]{lang="EN-US"}**[命令将当前已有的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[删除，使得所有新建立的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[都将使用新选择的加密引擎处理流程来处理。]{style="font-family:宋体"}

[[硬件加密引擎加密功能仅允许在测试、调试或故障排除的环境下关闭，正常情况下不建议关闭该功能。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_1628252222}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_932388181}

[[\# ]{lang="EN-US"}]{#struct_0_x1477_x1861_1050593034}[关闭硬件加密引擎。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1477_x1861_577554076}

[\[Sysname\] **crypto-engine accelerator disable**]{lang="EN-US"}
:::

::: {#758161594 .myid}
[]{#_Toc404793964}[]{#struct_0_x1477_x1861_x610327443}[]{#_Toc343703753}

**加密引擎 \-- 加密引擎配置命令 \-- display crypto-engine**

------------------------------------------------------------------------

[**[display crypto-engine]{lang="EN-US"}**]{#struct_0_x1477_x1861_x1996339470}[命令用来显示加密引擎的基本信息，包括各个加密引擎的名称、支持的算法能力等信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1896028309}

[**[display crypto-engine]{lang="EN-US"}**]{#struct_0_x1477_x1861_1809511441}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_221403506}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1477_x1861_751392379}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x236810579}

[[network-admin]{lang="EN-US"}]{#struct_0_x1477_x1861_x57351404}

[[network-operator]{lang="EN-US"}]{#struct_0_x1477_x1861_x1506618161}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1477_x1861_x424186107}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1477_x1861_574101407}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_999972964}

[[若设备没有硬件加密引擎，则只会显示软件加密引擎信息。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1971102491}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_221469042}

[[\# ]{lang="EN-US"}]{#struct_0_x1477_x1861_1897724132}[显示加密引擎的基本信息。]{style="font-family:宋体"}

[[\<Sysname\> display crypto-engine]{lang="EN-US"}]{#struct_0_x1477_x1861_1083321019}

[  Crypto engine name: cavium crypto driver]{lang="EN-US"}

[  Crypto engine state: Enabled]{lang="EN-US"}

[  Crypto engine type: Hardware]{lang="EN-US"}

[  Slot ID: 0]{lang="EN-US"}

[  CPU ID]{lang="EN-US"}[：]{style="font-family:宋体"}[0]{lang="EN-US"}

[  Crypto engine ID: 0]{lang="EN-US"}

[  Symmetric algorithms: des-ecb 3des-cbc 3des-ecb aes-cbc aes-ecb aes-ctr camellia_cbc sha1 sha2-256 sha2-384 sha2-512 md5-hmac sha1hmac sha2-256-hmac sha2-384-hmac sha2-512-hmac]{lang="EN-US"}

[  Asymmetric algorithms: dh-group1 dh-group2 dh-group5 dh-group14 dh-group24 ]{lang="EN-US"}

[  Random number generation function: Supported]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Crypto engine name: Software crypto engine]{lang="EN-US"}

[  Crypto engine state: Enabled]{lang="EN-US"}

[  Crypto engine type: Software]{lang="EN-US"}

[  Slot ID: 0]{lang="EN-US"}

[  CPU ID]{lang="EN-US"}[：]{style="font-family:宋体"}[0]{lang="EN-US"}

[  Crypto engine ID: 1]{lang="EN-US"}

[  Symmetric algorithms: des-cbc des-ecb 3des-ecb aes-ecb sha1 sha2-256 sha1-hmac sha2-256-hmac]{lang="EN-US"}

[  Asymmetric algorithms:]{lang="EN-US"}

[  Random number generation function: Supported]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1477_x1861_1489562673}[显示加密引擎的基本信息。（设备上无硬件加密引擎的情况）]{style="font-family:宋体"}

[[\<Sysname\> display crypto-engine]{lang="EN-US"}]{#struct_0_x1477_x1861_221534578}

[  Crypto engine name: Software crypto engine]{lang="EN-US"}

[  Crypto engine state: Enabled]{lang="EN-US"}

[  Crypto engine type: Software]{lang="EN-US"}

[  Slot ID: 0]{lang="EN-US"}

[  CPU ID]{lang="EN-US"}[：]{style="font-family:宋体"}[0]{lang="EN-US"}

[  Crypto engine ID: 0]{lang="EN-US"}

[  Symmetric algorithms: des-cbc des-ecb 3des-ecb aes-ecb sha1 sha2-256 sha1-hmac sha2-256-hmac]{lang="EN-US"}

[  Asymmetric algorithms:]{lang="EN-US"}

[  Random number generation function: Supported]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display crypto-engine]{lang="EN-US"}]{#struct_0_x1477_x1861_328619482}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1858965363}[[字段]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x847625921}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1477_x1861_562279357}

[[Crypto engine name]{lang="EN-US"}]{#struct_0_x1477_x1861_164200788}

[[加密引擎名称]{style="font-family:宋体"}]{#struct_0_x1477_x1861_221600114}

[[Crypto engine state]{lang="EN-US"}]{#struct_0_x1477_x1861_x465967516}

[[加密引擎的状态，对于不同类型的加密引擎状态不同]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x5287449}

[[对于硬件加密引擎，包括以下两种：]{style="font-family:宋体"}]{#struct_0_x1477_x1861_1698844722}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1477_x1861_x777967086}[：已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1477_x1861_221665650}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[对于软件加密引擎，只包含以下一种：]{style="font-family:宋体"}]{#struct_0_x1477_x1861_1380639260}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1477_x1861_x659077395}[：已开启]{lang="EN-US" style="font-family:宋体"}

[[Crypto engine type]{lang="EN-US"}]{#struct_0_x1477_x1861_x1916812960}

[[加密引擎的类型，包括以下两种：]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x526387356}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware]{lang="EN-US"}]{#struct_0_x1477_x1861_x551580554}[：硬件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Software]{lang="EN-US"}]{#struct_0_x1477_x1861_220682610}[：软件]{lang="EN-US" style="font-family:宋体"}

[[Slot ID]{lang="EN-US"}]{#struct_0_x1477_x1861_x677183593}

[[加密引擎所在的接口板编号]{style="font-family:宋体"}]{#struct_0_x1477_x1861_672691853}

[[CPU ID]{lang="EN-US"}]{#struct_0_x1477_x1861_1220039050}

[[单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x1477_x1861_1220039047}[编号]{style="font-family:宋体"}

[[Crypto engine ID ]{lang="EN-US"}]{#struct_0_x1477_x1861_x1503151144}

[[加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1477_x1861_x663424857}[号]{style="font-family:宋体"}

[[Symmetric algorithms]{lang="EN-US"}]{#struct_0_x1477_x1861_220748146}

[[支持的对称加密算法]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1452045178}

[[Asymmetric algorithms]{lang="EN-US"}]{#struct_0_x1477_x1861_2009773283}

[[支持的非对称加密算法]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x721640793}

[[Random number generation function]{lang="EN-US"}]{#struct_0_x1477_x1861_883753378}

[[是否支持获取随机数的功能]{style="font-family:宋体"}]{#struct_0_x1477_x1861_2143521202}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[upported]{lang="EN-US"}]{#struct_0_x1477_x1861_2082909203}[：支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not supported]{lang="EN-US"}]{#struct_0_x1477_x1861_736377195}[：不支持]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1833259495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[crypto-engine accelerator disable]{lang="EN-US"}**]{#struct_0_x1477_x1861_x379203156}

::: {#1957550275 .myid}
[]{#_Toc404793965}[]{#struct_0_x1477_x1861_2135062131}[]{#_Toc343703754}[]{#_Toc292201223}[]{#_Toc145229910}[]{#_Toc32567516}

**加密引擎 \-- 加密引擎配置命令 \-- display crypto-engine statistics**

------------------------------------------------------------------------

[**[display crypto-engine statistics]{lang="EN-US"}**]{#struct_0_x1477_x1861_2143586738}[命令用来显示加密引擎的统计信息，包括建立会话的个数，加密引擎处理的报文数等信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1434616877}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1477_x1861_548423827}

[**[display crypto-engine statistics ]{lang="EN-US"}**[\[ **engine-id** *engine-id* \]]{lang="EN-US"}]{#struct_0_x1477_x1861_1514979793}

[[分布式设备]{style="font-family:宋体"}[---]{lang="EN-US"}]{#struct_0_x1477_x1861_1153578049}[独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display crypto-engine statistics]{lang="EN-US"}**[ \[ **engine-id** *engine*-*id* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1477_x1861_1381878082}

[[分布式设备]{style="font-family:宋体"}[---IRF]{lang="EN-US"}]{#struct_0_x1477_x1861_2082132378}[模式：]{style="font-family:宋体"}

[**[display crypto-engine statistics]{lang="EN-US"}**[ \[ **engine-id** *engine*-*id* **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1477_x1861_x467107501}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1271639810}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1477_x1861_2143652274}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1828499868}

[[network-admin]{lang="EN-US"}]{#struct_0_x1477_x1861_1953260546}

[[network-operator]{lang="EN-US"}]{#struct_0_x1477_x1861_x46586537}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1477_x1861_x1553962804}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1477_x1861_x198625650}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1336572869}

[**[engine-id]{lang="EN-US"}***[ engine-id]{lang="EN-US"}*]{#struct_0_x1477_x1861_475854138}[：显示指定加密引擎的统计信息，]{style="font-family:宋体"}*[engine-id]{lang="EN-US"}*[为加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1477_x1861_172923789}[：显示指定单板上的加密引擎统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1477_x1861_2143717810}[：显示指定成员设备上的加密引擎统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1477_x1861_x1370517664}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的加密引擎统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1477_x1861_1731653678}[：显示指定成员设备上指定单板的加密引擎统计信息，]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1477_x1861_193796810}[：显示指定指定单板的加密引擎统计信息，]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1477_x1861_x1251211887}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的加密引擎统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1339651730}

[[如果未开启硬件加密引擎或者设备上没有硬件加密引擎，则只会显示软件加密引擎的统计信息。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1287015139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则显示所有加密引擎统计信息。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x917525525}[（集中式设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则显示所有单板的上的加密引擎统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x870961075}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则显示所有成员设备上的加密引擎统计信息。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_1961856580}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{lang="EN-US" style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}]{#struct_0_x1477_x1861_x160664083}[上的加密引擎统计信息。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{lang="EN-US" style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则显示所有所有单板上的加密引擎统计信息。（分布式设备－]{style="font-family:宋体"}]{#struct_0_x1477_x1861_57806446}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1529661021}

[[\# ]{lang="EN-US"}]{#struct_0_x1477_x1861_2143783346}[显示所有加密引擎统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display crypto-engine statistics]{lang="EN-US"}]{#struct_0_x1477_x1861_x1440169313}

[  Submitted sessions: 0]{lang="EN-US"}

[  Failed sessions: 0]{lang="EN-US"}

[  Symmetric operations: 0]{lang="EN-US"}

[  Symmetric errors: 0]{lang="EN-US"}

[  Asymmetric operations: 0]{lang="EN-US"}

[  Asymmetric errors: 0]{lang="EN-US"}

[  Get-random operations: 0]{lang="EN-US"}

[  Get-random errors: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1477_x1861_840117609}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上加密引擎号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的加密引擎统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display crypto-engine statistics engine-id 1 slot 2]{lang="EN-US"}]{#struct_0_x1477_x1861_1119233743}

[  Submitted sessions: 0]{lang="EN-US"}

[  Failed sessions: 0]{lang="EN-US"}

[  Symmetric operations: 0]{lang="EN-US"}

[  Symmetric errors: 0]{lang="EN-US"}

[  Asymmetric operations: 0]{lang="EN-US"}

[  Asymmetric errors: 0]{lang="EN-US"}

[  Get-random operations: 0]{lang="EN-US"}

[  Get-random errors: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1477_x1861_2143848882}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上加密引擎号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的加密引擎统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display crypto-engine statistics engine-id 1 slot 2]{lang="EN-US"}]{#struct_0_x1477_x1861_x1449993427}

[  Submitted sessions: 0]{lang="EN-US"}

[  Failed sessions: 0]{lang="EN-US"}

[  Symmetric operations: 0]{lang="EN-US"}

[  Symmetric errors: 0]{lang="EN-US"}

[  Asymmetric operations: 0]{lang="EN-US"}

[  Asymmetric errors: 0]{lang="EN-US"}

[  Get-random operations: 0]{lang="EN-US"}

[  Get-random errors: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1477_x1861_x1479412380}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板的加密引擎号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的加密引擎统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display crypto-engine statistics engine-id 1 chassis 1 slot 2]{lang="EN-US"}]{#struct_0_x1477_x1861_2143914418}

[  Submitted sessions: 0]{lang="EN-US"}

[  Failed sessions: 0]{lang="EN-US"}

[  Symmetric operations: 0]{lang="EN-US"}

[  Symmetric errors: 0]{lang="EN-US"}

[  Asymmetric operations: 0]{lang="EN-US"}

[  Asymmetric errors: 0]{lang="EN-US"}

[  Get-random operations: 0]{lang="EN-US"}

[  Get-random errors: 0]{lang="EN-US"}

[]{#struct_0_x1477_x1861_x1835900001}[]{#_Toc138131783}[]{#_Toc95386919}[]{#_Toc85621933}[]{#_Toc81452881}[]{#_Toc74712938}[]{#_Toc74712796}[]{#_Toc72595594}[]{#_Toc66003028}[]{#_Toc60131209}[]{#_Toc42655612}[]{#_Toc40150010}[]{#_Toc535897061}[]{#_Toc534882583}[[表1-2 ]{lang="EN-US"}[display crypto-engine statistics]{lang="EN-US"}]{#_Toc533152964}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1832796147}[[字段]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x119560063}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x1564945792}

[[Submitted sessions]{lang="EN-US"}]{#struct_0_x1477_x1861_425013272}

[[已创建的会话数目]{style="font-family:宋体"}]{#struct_0_x1477_x1861_83306105}

[[Failed sessions]{lang="EN-US"}]{#struct_0_x1477_x1861_1636959781}

[[创建失败的会话数目]{style="font-family:宋体"}]{#struct_0_x1477_x1861_1971012664}

[[Symmetric operations]{lang="EN-US"}]{#struct_0_x1477_x1861_2143979954}

[[加密引擎使用对称算法的操作次数]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1061924998}

[[Symmetric errors]{lang="EN-US"}]{#struct_0_x1477_x1861_x1126848634}

[[加密引擎使用对称算法操作失败的次数]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1533371958}

[[Asymmetric operations]{lang="EN-US"}]{#struct_0_x1477_x1861_x1372956675}

[[加密引擎使用非对称算法操作的次数]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1305949473}

[[Asymmetric errors]{lang="EN-US"}]{#struct_0_x1477_x1861_2142996914}

[[加密引擎使用非对称算法操作失败的次数]{style="font-family:宋体"}]{#struct_0_x1477_x1861_540375657}

[[Get-random operations]{lang="EN-US"}]{#struct_0_x1477_x1861_x182649662}

[[加密引擎获取随机数操作的次数]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x246672143}

[[Get-random errors]{lang="EN-US"}]{#struct_0_x1477_x1861_720185438}

[[加密引擎获取随机数操作失败的次数]{style="font-family:宋体"}]{#struct_0_x1477_x1861_2143062450}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x670544348}

[**[reset crypto-engine statistics]{lang="EN-US"}**]{#struct_0_x1477_x1861_x521612081}

::: {#-961154183 .myid}
[]{#_Toc404793966}[]{#struct_0_x1477_x1861_617343703}[]{#_Toc343703755}

**加密引擎 \-- 加密引擎配置命令 \-- reset crypto-engine statistics**

------------------------------------------------------------------------

[**[reset crypto-engine statistics]{lang="EN-US"}**]{#struct_0_x1477_x1861_1512070664}[命令用来清除加密引擎的统计计数。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_155583786}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1477_x1861_1860498385}

[**[reset crypto-engine statistics ]{lang="EN-US"}**[\[ **engine-id** *engine-id* \]]{lang="EN-US"}]{#struct_0_x1477_x1861_726576760}

[[分布式设备]{style="font-family:宋体"}[---]{lang="EN-US"}]{#struct_0_x1477_x1861_x1448711746}[独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset crypto-engine statistics ]{lang="EN-US"}**[\[ **engine-id** *engine***-***id* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1477_x1861_2143521203}

[[分布式设备]{style="font-family:宋体"}[---IRF]{lang="EN-US"}]{#struct_0_x1477_x1861_2082974739}[模式：]{style="font-family:宋体"}

[**[reset crypto-engine statistics]{lang="EN-US"}**[ \[ **engine-id** *engine***-***id* **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1477_x1861_x2045887471}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_197814709}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1942324248}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x2047774620}

[[network-admin]{lang="EN-US"}]{#struct_0_x1477_x1861_2064244069}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1477_x1861_1460541807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_x469645372}

[**[engine-id]{lang="EN-US"}***[ engine-id]{lang="EN-US"}*]{#struct_0_x1477_x1861_2143586739}[：清除指定加密引擎的统计信息，]{style="font-family:宋体"}*[engine-id]{lang="EN-US"}*[为加密引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1477_x1861_x1434551341}[：清除指定单板上的加密引擎统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1477_x1861_340541290}[：清除指定成员设备上的加密引擎统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x1477_x1861_1761584682}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的加密引擎统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-numbe*]{lang="EN-US"}]{#struct_0_x1477_x1861_x248171850}[：清除指定成员设备上指定单板的加密引擎统计信息，]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-numbe*]{lang="EN-US"}]{#struct_0_x1477_x1861_714286492}[：清除指定单板上的加密引擎统计信息，]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x1477_x1861_x1251539567}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的加密引擎统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_105481571}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则清除所有加密引擎统计信息。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1605051135}[（集中式设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则清除所有单板的上的加密引擎统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1216688923}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则清除所有成员设备上的加密引擎统计信息。]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x664432743}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{lang="EN-US" style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}]{#struct_0_x1477_x1861_x967298673}[上的加密引擎统计信息。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{lang="EN-US" style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则清除所有单板上的加密引擎统计信息。（分布式设备－]{style="font-family:宋体"}]{#struct_0_x1477_x1861_x1693775235}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_2143652275}

[[\# ]{lang="EN-US"}]{#struct_0_x1477_x1861_x1828565404}[清除加密引擎的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset crypto-engine statistics]{lang="EN-US"}]{#struct_0_x1477_x1861_309287749}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1477_x1861_1235796821}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display crypto-engine statistics]{lang="EN-US"}**]{#struct_0_x1477_x1861_x1058395258}

[]{#_Toc141674701}[]{#_Toc141674796}[]{#_Toc141685277}[]{#_Toc141686198}[]{#_Toc141674702}[]{#_Toc141674797}[]{#_Toc141685278}[]{#_Toc141686199}[ ]{lang="EN-US"}
:::
