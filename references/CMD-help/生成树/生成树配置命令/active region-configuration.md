::: {#-1772979720 .myid}
[]{#_Toc65310809}[]{#_Toc36367100}[]{#_Toc34185794}[]{#_Toc404784573}[]{#struct_0_x1139_12555_x844582436}

**生成树 \-- 生成树配置命令 \-- active region-configuration**

------------------------------------------------------------------------

[**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_616007434}[命令用来激活]{style="font-family:
宋体"}[MST]{lang="EN-US"}[域的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1624897361}

[**[active]{lang="EN-US"}**[ **region-configuration**]{lang="EN-US"}]{#struct_0_x1139_12555_74067508}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1682238622}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_932781960}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1955107869}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1929216231}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_864832233}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_657814664}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1130376506}[MST]{lang="EN-US"}[域的相关参数（特别是]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表）时，会引发生成树的重新计算，从而引起网络拓扑的振荡。为了减少网络振荡，新配置的]{style="font-family:宋体"}[MST]{lang="EN-US"}[域参数并不会马上生效，而是在使用本命令激活，或使用命令]{style="font-family:宋体"}**[stp global enable]{lang="EN-US"}**[全局开启生成树协议后才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行本命令前，建议先使用]{lang="EN-US" style="font-family:宋体"}**[check region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_615941898}[命令查看]{lang="EN-US" style="font-family:宋体"}[MST]{lang="EN-US"}[域的预配置是否正确，当确认这些配置无误后再执行本命令。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1711123432}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_538683189}[将]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[映射到]{style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[上，并激活该配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x645473896}

[\[Sysname\] stp region-configuration]{lang="EN-US"}

[\[Sysname-mst-region\] instance 1 vlan 2]{lang="EN-US"}

[\[Sysname-mst-region\] active region-configuration]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x171205445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[check region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1522401797}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[instance]{lang="EN-US"}**]{#struct_0_x1139_12555_x681877590}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[region-name]{lang="EN-US"}**]{#struct_0_x1139_12555_x1131109561}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[revision-level]{lang="EN-US"}**]{#struct_0_x1139_12555_x317711549}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp global enable]{lang="EN-US"}**]{#struct_0_x1139_12555_615876362}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vlan-mapping modulo]{lang="EN-US"}**]{#struct_0_x1139_12555_634300598}
:::

::::: {#-339321995 .myid}
[]{#_Toc404784574}[]{#struct_0_x1139_12555_x1350626920}[]{#_Toc295921817}[]{#_Toc240873355}[]{#_Toc287952152}[]{#_Toc287960082}[]{#_Toc287952153}[]{#_Toc287960083}[]{#_Toc287952156}[]{#_Toc287960086}[]{#_Toc287952157}[]{#_Toc287960087}[]{#_Toc287952158}[]{#_Toc287960088}[]{#_Toc287952159}[]{#_Toc287960089}[]{#_Toc287952160}[]{#_Toc287960090}[]{#_Toc287952161}[]{#_Toc287960091}[]{#_Toc287952162}[]{#_Toc287960092}[]{#_Toc287952163}[]{#_Toc287960093}[]{#_Toc287952164}[]{#_Toc287960094}[]{#_Toc287952165}[]{#_Toc287960095}[]{#_Toc287952166}[]{#_Toc287960096}[]{#_Toc287952167}[]{#_Toc287960097}[]{#_Toc287952168}[]{#_Toc287960098}[]{#_Toc287952169}[]{#_Toc287960099}[]{#_Toc287952172}[]{#_Toc287960102}

**生成树 \-- 生成树配置命令 \-- bpdu-drop any**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](生成树命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1139_12555_1208367496}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1139_12555_x459439657}
:::

[ ]{lang="EN-US"}

[**[bpdu-drop any]{lang="EN-US"}**]{#struct_0_x1139_12555_x667868471}[命令用来开启端口的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[拦截功能。]{style="font-family:宋体"}

[**[undo bpdu-drop any]{lang="EN-US"}**]{#struct_0_x1139_12555_x1341293330}[命令用来关闭端口的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[拦截功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1467028477}

[**[bpdu-drop any]{lang="EN-US"}**]{#struct_0_x1139_12555_615810826}

[**[undo bpdu-drop any]{lang="EN-US"}**]{#struct_0_x1139_12555_1356246021}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1459972527}

[[端口的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_2125150898}[拦截功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1261820155}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1473218465}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1319322423}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_89543072}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1968839199}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_615745290}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x414638638}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[拦截功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1741322164}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bpdu-drop any]{lang="EN-US"}
:::::

::: {#-140457279 .myid}
[]{#_Toc404784575}[]{#struct_0_x1139_12555_x174630204}

**生成树 \-- 生成树配置命令 \-- check region-configuration**

------------------------------------------------------------------------

[**[check region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x146799935}[命令用来显示]{style="font-family:
宋体"}[MST]{lang="EN-US"}[域的预配置信息，包括域名、修订级别以及]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x940561689}

[**[check region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_753698258}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_734979499}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_616728330}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1135383510}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1571386918}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1826215803}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x648489391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[两台或多台开启了生成树协议的设备若要属于同一个]{style="font-family:宋体"}]{#struct_0_x1139_12555_585902793}[MST]{lang="EN-US"}[域，必须同时满足以下两个条件：第一是选择因子（取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，不可配）、域名、修订级别和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表的配置都相同；第二是这些设备之间的链路相通。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议在激活]{style="font-family:宋体"}]{#struct_0_x1139_12555_141943761}[MST]{lang="EN-US"}[域的配置前，先使用本命令查看]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的预配置是否正确，当确认这些配置无误后再激活]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_704739643}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_500854348}[显示]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的预配置信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_616662794}

[\[Sysname\] stp region-configuration]{lang="EN-US"}

[\[Sysname-mst-region\] check region-configuration]{lang="EN-US"}

[ Admin Configuration]{lang="EN-US"}

[   Format selector      : 0]{lang="EN-US"}

[   Region name          : 001122334400]{lang="EN-US"}

[   Revision level       : 0]{lang="EN-US"}

[   Configuration digest : 0x3ab68794d602fdf43b21c0b37ac3bca8]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Instance  VLANs Mapped]{lang="EN-US"}

[   0         1, 3 to 4094]{lang="EN-US"}

[   15        2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[check region-configuration]{lang="EN-US"}]{#struct_0_x1139_12555_1933927770}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1246782227}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_264943142}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1680298895}

[[Format selector]{lang="EN-US"}]{#struct_0_x1139_12555_x385066277}

[[生成树协议规定的选择因子，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1139_12555_616204039}[，不可配]{style="font-family:宋体"}

[[Region name]{lang="EN-US"}]{#struct_0_x1139_12555_1374762576}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_70196707}[域的域名]{style="font-family:宋体"}

[[Revision level]{lang="EN-US"}]{#struct_0_x1139_12555_x179833700}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_1893037982}[域的修订级别]{style="font-family:宋体"}

[[Configuration digest]{lang="EN-US"}]{#struct_0_x1139_12555_x572207808}

[[配置摘要]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1085257501}

[[Instance   VLANs Mapped]{lang="EN-US"}]{#struct_0_x1139_12555_616138503}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x79135572}[域的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[之间的映射关系，即]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表]{style="font-family:宋体"}

[]{#_Toc135292481}[]{#_Toc135292482}[]{#_Toc135292483}[]{#_Toc135292484}[]{#_Toc135292485}[]{#_Toc135292486}[]{#_Toc135292487}[]{#_Toc135292488}[]{#_Toc135292489}[]{#_Toc135292490}[]{#_Toc135292491}[]{#_Toc135292492}[]{#_Toc135292493}[]{#_Toc135292494}[]{#_Toc135292495}[]{#_Toc135292562}[]{#_Toc135292563}[]{#_Toc135292577}[]{#_Toc135292578}[]{#_Toc135292579}[]{#_Toc135292580}[]{#_Toc135292583}[]{#_Toc135292584}[]{#_Toc135292585}[]{#_Toc135292586}[]{#_Toc135292587}[]{#_Toc135292588}[]{#_Toc135292589}[]{#_Toc135292590}[]{#_Toc135292591}[]{#_Toc135292592}[]{#_Toc135292593}[]{#_Toc135292594}[]{#_Toc135292595}[]{#_Toc135292596}[]{#_Toc135292597}[]{#_Toc135292598}[]{#_Toc135292599}[]{#_Toc135292600}[]{#_Toc135292601}[]{#_Toc135292602}[]{#_Toc135292603}[]{#_Toc135292604}[]{#_Toc135292605}[]{#_Toc135292606}[]{#_Toc135292633}[]{#_Toc135292634}[]{#_Toc135292635}[]{#_Toc135292639}[]{#_Toc135292641}[]{#_Toc135292642}[]{#_Toc135292643}[]{#_Toc135292644}[]{#_Toc135292645}[]{#_Toc135292646}[]{#_Toc135292647}[]{#_Toc135292648}[]{#_Toc135292649}[]{#_Toc135292650}[]{#_Toc135292651}[]{#_Toc135292652}[]{#_Toc135292653}[]{#_Toc135292654}[]{#_Toc135292655}[]{#_Toc135292656}[]{#_Toc135292657}[]{#_Toc135292658}[]{#_Toc135292659}[]{#_Toc135292660}[]{#_Toc135292670}[]{#_Toc135292671}[]{#_Toc135292672}[]{#_Toc135292673}[]{#_Toc135292678}[]{#_Toc135292680}[]{#_Toc135292683}[]{#_Toc135292684}[]{#_Toc135292685}[]{#_Toc135292686}[]{#_Toc135292687}[]{#_Toc135292688}[]{#_Toc135292689}[]{#_Toc135292690}[]{#_Toc135292691}[]{#_Toc135292692}[]{#_Toc135292693}[]{#_Toc135292694}[]{#_Toc135292695}[]{#_Toc135292696}[]{#_Toc135292697}[]{#_Toc135292698}[]{#_Toc135292699}[]{#_Toc135292719}[]{#_Toc135292720}[]{#_Toc135292727}[]{#_Toc135292728}[]{#_Toc135292729}[]{#_Toc135292735}[]{#_Toc135292736}[]{#_Toc135292737}[]{#_Toc135292747}[]{#_Toc135292748}[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_320504754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1523057158}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[instance]{lang="EN-US"}**]{#struct_0_x1139_12555_x1357678283}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[region-name]{lang="EN-US"}**]{#struct_0_x1139_12555_x386022184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[revision-level]{lang="EN-US"}**]{#struct_0_x1139_12555_x664118584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vlan-mapping modulo]{lang="EN-US"}**]{#struct_0_x1139_12555_1459715040}

::: {#-774072122 .myid}
[]{#_Toc404784576}[]{#struct_0_x1139_12555_616072967}

**生成树 \-- 生成树配置命令 \-- display stp**

------------------------------------------------------------------------

[**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x375388928}[命令用来显示生成树的状态和统计信息。根据这些信息，可以对网络拓扑结构进行分析与维护，也可以用于查看生成树协议工作是否正常。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_932535624}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1139_12555_x637835055}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] \[ **interface** *interface-list* \] \[ **brief** \]]{lang="EN-US"}]{#struct_0_x1139_12555_878418956}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x1193451294}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] \[ **interface** *interface-list* \| **slot** *slot-number* \] \[ **brief** \]]{lang="EN-US"}]{#struct_0_x1139_12555_x612386836}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1139_12555_207797134}[模式：]{style="font-family:宋体"}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] \[ **interface** *interface-list* \| **chassis** *chassis-number* **slot** *slot-number* \] \[ **brief** \]]{lang="EN-US"}]{#struct_0_x1139_12555_616007431}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1624897356}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_477548643}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_565369898}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1582348706}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_x904801604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x907712895}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_1696335960}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x198789470}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_615941895}[：显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的生成树状态和统计信息。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x1099768569}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的生成树状态和统计信息。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** vlan*-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}[vlan*-id*]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-list]{lang="EN-US"}*]{#struct_0_x1139_12555_1711123429}[：显示指定端口上的生成树状态和统计信息。]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[为端口列表，表示多个端口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type interface-number* \[ **to** *interface-type interface-number* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[为端口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为端口编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x1139_12555_539404086}[：显示生成树状态和统计的简要信息。如果未指定本参数，将显示生成树状态和统计的详细信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_1971931047}[：显示指定单板上的生成树状态和统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示所有单板上的生成树状态和统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_x1741242551}[：显示指定成员设备上的生成树状态和统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，将显示所有成员设备上的生成树状态和统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_x1290019587}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的生成树状态和统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定该参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的生成树状态和统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_429269361}[：显示指定成员设备指定单板上的生成树状态和统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示所有单板上的生成树状态和统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_1690176344}[：显示指定单板上的生成树状态和统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，将显示所有单板上的生成树状态和统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x854530400}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}]{#struct_0_x1139_12555_1991570026}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定端口，则显示所有端口上的生成树状态和统计信息，显示信息按照端口名称的顺序排列。]{style="font-family:宋体"}]{#struct_0_x1139_12555_86857736}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了端口，则显示该端口上的生成树状态和统计信息，显示信息按照端口名称的顺序排列。]{style="font-family:宋体"}]{#struct_0_x1139_12555_615876359}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[PVST]{lang="EN-US"}]{#struct_0_x1139_12555_x1099703033}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_1307841427}[VLAN]{lang="EN-US"}[和端口，则显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[在所有端口上的生成树状态和统计信息，显示信息按照]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1632790657}[VLAN]{lang="EN-US"}[但未指定端口，则显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[在所有端口上的生成树状态和统计信息，显示信息按照]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了端口但未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1114028971}[VLAN]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[在指定端口上的生成树状态和统计信息，显示信息按照]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1099899641}[VLAN]{lang="EN-US"}[和端口，则显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[在指定端口上的生成树状态和统计信息，显示信息按照]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_x939677525}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_246711554}[MSTI]{lang="EN-US"}[和端口，则显示所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在所有端口上的生成树状态和统计信息，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_1859620333}[MSTI]{lang="EN-US"}[但未指定端口，则显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在所有端口上的生成树状态和统计信息，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了端口但未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_914171084}[MSTI]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在指定端口上的生成树状态和统计信息，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2070519423}[MSTI]{lang="EN-US"}[和端口，则显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在指定端口上的生成树状态和统计信息，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1126753072}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x652373673}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[～]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[上生成树状态和统计的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 0 interface gigabitethernet 1/0/1 to gigabitethernet 1/0/4 brief]{lang="EN-US"}]{#struct_0_x1139_12555_615810823}

[ MST ID      Port                         Role  STP State     Protection]{lang="EN-US"}

[ 0           GigabitEthernet1/0/1         ALTE  DISCARDING    LOOP]{lang="EN-US"}

[ 0           GigabitEthernet1/0/2         DESI  FORWARDING    NONE]{lang="EN-US"}

[ 0           GigabitEthernet1/0/3         DESI  FORWARDING    NONE]{lang="EN-US"}

[ 0           GigabitEthernet1/0/4         DESI  FORWARDING    NONE]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1100030713}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[～]{style="font-family:宋体"}[GigabitEthernet1/0/4]{lang="EN-US"}[上生成树状态和统计的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x918202555}

[\[Sysname\] stp mode pvst]{lang="EN-US"}

[\[Sysname\] display stp vlan 2 interface gigabitethernet 1/0/1 to gigabitethernet 1/0/4 brief]{lang="EN-US"}

[ VLAN ID     Port                         Role  STP State     Protection]{lang="EN-US"}

[ 2           GigabitEthernet1/0/1         ALTE  DISCARDING    LOOP]{lang="EN-US"}

[ 2           GigabitEthernet1/0/2         DESI  FORWARDING    NONE]{lang="EN-US"}

[ 2           GigabitEthernet1/0/3         DESI  FORWARDING    NONE]{lang="EN-US"}

[ 2           GigabitEthernet1/0/4         DESI  FORWARDING    NONE]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display stp brief]{lang="EN-US"}]{#struct_0_x1139_12555_1356246016}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1248952657}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_1459775920}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_527293867}

[[MST ID]{lang="EN-US"}]{#struct_0_x1139_12555_x698647009}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x1567057151}[的编号]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x1139_12555_x1099965177}

[[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_x1099113209}[的编号]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x1139_12555_x1526485811}

[[端口名称，和相应的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_615745287}[对应]{style="font-family:宋体"}

[[Role]{lang="EN-US"}]{#struct_0_x1139_12555_1924013529}

[[端口角色：]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1598975565}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ALTE]{lang="EN-US"}]{#struct_0_x1139_12555_1432097229}[：表示替换端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BACK]{lang="EN-US"}]{#struct_0_x1139_12555_1225373516}[：表示备份端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ROOT]{lang="EN-US"}]{#struct_0_x1139_12555_x1634168363}[：表示根端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DESI]{lang="EN-US"}]{#struct_0_x1139_12555_616728327}[：表示指定端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAST]{lang="EN-US"}]{#struct_0_x1139_12555_x820931623}[：表示主端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISA]{lang="EN-US"}]{#struct_0_x1139_12555_1251505750}[：表示失效端口]{lang="EN-US" style="font-family:宋体"}

[[STP State]{lang="EN-US"}]{#struct_0_x1139_12555_1649597796}

[[端口状态：]{style="font-family:宋体"}]{#struct_0_x1139_12555_1443953714}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FORWARDING]{lang="EN-US"}]{#struct_0_x1139_12555_x727658987}[：表示可以接收和发送]{lang="EN-US" style="font-family:宋体"}[BPDU]{lang="EN-US"}[，也转发用户流量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISCARDING]{lang="EN-US"}]{#struct_0_x1139_12555_616662791}[：表示可以接收和发送]{lang="EN-US" style="font-family:宋体"}[BPDU]{lang="EN-US"}[，但不转发用户流量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LEARNING]{lang="EN-US"}]{#struct_0_x1139_12555_1933927775}[：表示可以接收和发送]{lang="EN-US" style="font-family:宋体"}[BPDU]{lang="EN-US"}[，但不转发用户流量，是一种过渡状态]{lang="EN-US" style="font-family:宋体"}

[[Protection]{lang="EN-US"}]{#struct_0_x1139_12555_264746534}

[[端口上的保护类型：]{style="font-family:宋体"}]{#struct_0_x1139_12555_2036128267}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ROOT]{lang="EN-US"}]{#struct_0_x1139_12555_2014096651}[：表示根保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LOOP]{lang="EN-US"}]{#struct_0_x1139_12555_616204040}[：表示环路保护]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x2110900665}[：表示]{lang="EN-US" style="font-family:宋体"}[BPDU]{lang="EN-US"}[保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONE]{lang="EN-US"}]{#struct_0_x1139_12555_253642871}[：表示无保护]{lang="EN-US" style="font-family:宋体"}

[]{#_Toc135292750}[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_332377588}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在所有端口上的生成树状态和统计的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp]{lang="EN-US"}]{#struct_0_x1139_12555_679414417}

[\-\-\-\-\-\--\[CIST Global Info\]\[Mode MSTP\]\-\-\-\-\-\--]{lang="EN-US"}

[ Bridge ID           : 32768.0001-0000-0000]{lang="EN-US"}

[ Bridge times        : Hello 2s MaxAge 20s FwdDelay 15s MaxHops 20]{lang="EN-US"}

[ Root ID/ERPC        : 32768.0001-0000-0000, 0]{lang="EN-US"}

[ RegRoot ID/IRPC     : 32768.0001-0000-0000, 0]{lang="EN-US"}

[ RootPort ID         : 0.0]{lang="EN-US"}

[ BPDU-Protection     : Disabled]{lang="EN-US"}

[ Bridge Config-]{lang="EN-US"}

[ Digest-Snooping     : Disabled]{lang="EN-US"}

[ TC or TCN received  : 2]{lang="EN-US"}

[ Time since last TC  : 0 days 0h:0m:58s]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\--\[Port3(Ethernet0/0/2)\]\[FORWARDING\]\-\-\--]{lang="EN-US"}

[ Port protocol       : Enabled]{lang="EN-US"}

[ Port role           : Designated Port (Boundary)]{lang="EN-US"}

[ Port ID             : 128.3]{lang="EN-US"}

[ Port cost(Legacy)   : Config=auto, Active=200]{lang="EN-US"}

[ Desg.bridge/port    : 32768.0001-0000-0000, 128.3]{lang="EN-US"}

[ Port edged          : Config=disabled, Active=disabled]{lang="EN-US"}

[ Point-to-Point      : Config=auto, Active=true]{lang="EN-US"}

[ Transmit limit      : 10 packets/hello-time]{lang="EN-US"}

[ TC-Restriction      : Disabled]{lang="EN-US"}

[ Role-Restriction    : Disabled]{lang="EN-US"}

[ Protection type     : Config=none, Active=none]{lang="EN-US"}

[ MST BPDU format     : Config=auto, Active=802.1s]{lang="EN-US"}

[ Port Config-]{lang="EN-US"}

[ Digest-Snooping     : Disabled]{lang="EN-US"}

[ Rapid transition    : True]{lang="EN-US"}

[ Num of VLANs mapped : 0]{lang="EN-US"}

[ Port times          : Hello 2s MaxAge 20s FwdDelay 15s MsgAge 0s RemHops 20]{lang="EN-US"}

[ BPDU sent           : 32]{lang="EN-US"}

[          TCN: 0, Config: 0, RST: 0, MST: 32]{lang="EN-US"}

[ BPDU received       : 2]{lang="EN-US"}

[          TCN: 0, Config: 0, RST: 0, MST: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\--\[MSTI 1 Global Info\]\-\-\-\-\-\--]{lang="EN-US"}

[ Bridge ID           : 32768.0001-0000-0000]{lang="EN-US"}

[ RegRoot ID/IRPC     : 32768.0001-0000-0000, 0]{lang="EN-US"}

[ RootPort ID         : 0.0]{lang="EN-US"}

[ Master bridge       : 32768.0001-0000-0000]{lang="EN-US"}

[ Cost to master      : 0]{lang="EN-US"}

[ TC received         : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\--\[Port3(Ethernet0/0/2)\]\[FORWARDING\]\-\-\--]{lang="EN-US"}

[ Port protocol       : Enabled]{lang="EN-US"}

[ Port role           : Designated Port (Boundary)]{lang="EN-US"}

[ Port ID             : 128.3]{lang="EN-US"}

[ Port cost(Legacy)   : Config=auto, Active=200]{lang="EN-US"}

[ Desg.bridge/port    : 32768.0001-0000-0000, 128.3]{lang="EN-US"}

[ Protection type     : Config=none, Active=none]{lang="EN-US"}

[ Rapid transition    : True]{lang="EN-US"}

[ Num of VLANs mapped : 64]{lang="EN-US"}

[ Port times          : RemHops 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1099768570}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[在所有端口上的生成树状态和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1099899642}

[\[Sysname\] stp mode pvst]{lang="EN-US"}

[\[Sysname\] display stp]{lang="EN-US"}

[\-\-\-\-\-\--\[VLAN 1 Global Info\]\-\-\-\-\-\--]{lang="EN-US"}

[Protocol status     : Enabled]{lang="EN-US"}

[Bridge ID           : 32768.000f-e200-2200]{lang="EN-US"}

[Bridge times        : Hello 2s MaxAge 20s FwdDelay 15s]{lang="EN-US"}

[VlanRoot ID/RPC     : 0.00e0-fc0e-6554, 200200]{lang="EN-US"}

[RootPort ID         : 128.48]{lang="EN-US"}

[BPDU-Protection     : Disabled]{lang="EN-US"}

[TC or TCN received  : 2]{lang="EN-US"}

[Time since last TC  : 0 days 0h:5m:42s]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \-\-\--\[Port1(GigabitEthernet1/0/1)\]\[FORWARDING\]\-\-\--]{lang="EN-US"}

[ Port protocol       : Enabled]{lang="EN-US"}

[ Port role           : Designated Port]{lang="EN-US"}

[ Port ID             : 128.153]{lang="EN-US"}

[ Port cost(Legacy)   : Config=auto, Active=200]{lang="EN-US"}

[ Desg. bridge/port   : 32768.000f-e200-2200, 128.2]{lang="EN-US"}

[ Port edged          : Config=disabled, Active=disabled]{lang="EN-US"}

[ Point-to-Point      : Config=auto, Active=true]{lang="EN-US"}

[ Transmit limit      : 10 packets/hello-time]{lang="EN-US"}

[ Protection type     : Config=none, Active=none]{lang="EN-US"}

[ Rapid transition    : False]{lang="EN-US"}

[ Port times          : Hello 2s MaxAge 20s FwdDelay 15s MsgAge 2s]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\--\[VLAN 2 Global Info\]\-\-\-\-\-\--]{lang="EN-US"}

[Protocol status      : Enabled]{lang="EN-US"}

[Bridge ID            : 32768.000f-e200-2200]{lang="EN-US"}

[Bridge times         : Hello 2s MaxAge 20s FwDly 15s]{lang="EN-US"}

[VlanRoot ID/RPC      : 0.00e0-fc0e-6554, 200200]{lang="EN-US"}

[RootPort ID          : 128.48]{lang="EN-US"}

[BPDU-Protection      : Disabled]{lang="EN-US"}

[TC or TCN received   : 2]{lang="EN-US"}

[Time since last TC   : 0 days 0h:5m:42s]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x375388933}[当生成树协议未开启时，在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下显示生成树的状态和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp]{lang="EN-US"}]{#struct_0_x1139_12555_932207945}

[ Protocol status    : Disabled]{lang="EN-US"}

[ Protocol Std.      : IEEE 802.1s]{lang="EN-US"}

[ Version            : 3]{lang="EN-US"}

[ Bridge-Prio.       : 32768]{lang="EN-US"}

[ MAC address        : 000f-e200-8048]{lang="EN-US"}

[ Max age(s)         : 20]{lang="EN-US"}

[ Forward delay(s)   : 15]{lang="EN-US"}

[ Hello time(s)      : 2]{lang="EN-US"}

[ Max hops           : 20]{lang="EN-US"}

[ TC Snooping        : Disabled]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1100030714}[当生成树协议未开启时，在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下显示生成树的状态和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp]{lang="EN-US"}]{#struct_0_x1139_12555_1004111746}

[ Protocol status    : Disabled]{lang="EN-US"}

[ Protocol Std.      : IEEE 802.1w (pvst)]{lang="EN-US"}

[ Version            : 2]{lang="EN-US"}

[ Bridge-Prio.       : 32768]{lang="EN-US"}

[ MAC address        : 3822-d69f-0800]{lang="EN-US"}

[ Max age(s)         : 20]{lang="EN-US"}

[ Forward delay(s)   : 15]{lang="EN-US"}

[ Hello time(s)      : 2]{lang="EN-US"}

[ TC Snooping        : Disabled]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display stp]{lang="EN-US"}]{#struct_0_x1139_12555_1406954206}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1038980173}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_x886669524}

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_182457581}

[[Bridge ID]{lang="EN-US"}]{#struct_0_x1139_12555_x930491027}

[[网桥]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1139_12555_x1947374086}[，由两部分构成："]{style="font-family:宋体"}[.]{lang="EN-US"}["之前和之后的内容分别表示为本设备的优先级和本设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。譬如，"]{style="font-family:宋体"}[32768.000f-e200-2200]{lang="EN-US"}["表示本设备的优先级为]{style="font-family:宋体"}[32768]{lang="EN-US"}[，其]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000F-E200-2200]{lang="EN-US"}

[[Bridge times]{lang="EN-US"}]{#struct_0_x1139_12555_135875474}

[[网桥相关的主要参数值：]{style="font-family:宋体"}]{#struct_0_x1139_12555_112153160}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x1139_12555_2092017624}[：表示]{lang="EN-US" style="font-family:宋体"}[Hello time]{lang="EN-US"}[定时器值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MaxAge]{lang="EN-US"}]{#struct_0_x1139_12555_1629798601}[：表示]{lang="EN-US" style="font-family:宋体"}[Max Age]{lang="EN-US"}[定时器值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FwdDelay]{lang="EN-US"}]{#struct_0_x1139_12555_886167638}[：表示]{lang="EN-US" style="font-family:宋体"}[Forward delay]{lang="EN-US"}[定时器值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MaxHops]{lang="EN-US"}]{#struct_0_x1139_12555_1411459261}[：表示]{lang="EN-US" style="font-family:宋体"}[MST]{lang="EN-US"}[域的最大跳数]{lang="EN-US" style="font-family:宋体"}

[[Root ID/ERPC]{lang="EN-US"}]{#struct_0_x1139_12555_x726584100}

[[总根]{style="font-family:宋体"}[ID/]{lang="EN-US"}]{#struct_0_x1139_12555_x632082740}[外部路径开销（即本设备到总根的路径开销）]{style="font-family:宋体"}

[[RegRoot ID/IRPC]{lang="EN-US"}]{#struct_0_x1139_12555_x1289954051}

[[域根]{style="font-family:宋体"}[ID/]{lang="EN-US"}]{#struct_0_x1139_12555_113848600}[内部路径开销（即本设备到域根的路径开销）]{style="font-family:宋体"}

[[VlanRoot ID/RPC]{lang="EN-US"}]{#struct_0_x1139_12555_484584289}

[[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_x1992735698}[根桥]{style="font-family:宋体"}[ID/]{lang="EN-US"}[根路径开销（即本设备到该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[根桥的路径开销）]{style="font-family:宋体"}

[[RootPort ID]{lang="EN-US"}]{#struct_0_x1139_12555_x653835867}

[[根端口的端口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1139_12555_x1468683261}[。"]{style="font-family:宋体"}[0.0]{lang="EN-US"}["表示本设备为根设备，没有根端口]{style="font-family:宋体"}

[[BPDU-Protection]{lang="EN-US"}]{#struct_0_x1139_12555_x1486446669}

[[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_448973972}[保护功能的全局开启状态]{style="font-family:宋体"}

[[Bridge Config-]{lang="EN-US"}]{#struct_0_x1139_12555_276129890}

[[Digest-Snooping]{lang="EN-US"}]{#struct_0_x1139_12555_x1163681232}

[[摘要侦听功能的全局开启状态]{style="font-family:宋体"}]{#struct_0_x1139_12555_739275276}

[[TC or TCN received]{lang="EN-US"}]{#struct_0_x1139_12555_x270117594}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_2100513020}[或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[收到的]{style="font-family:宋体"}[TC]{lang="EN-US"}[及]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[Time since last TC]{lang="EN-US"}]{#struct_0_x1139_12555_804496111}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_181916448}[或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[最近一次拓扑变化时间]{style="font-family:宋体"}

[[\[FORWARDING\]]{lang="EN-US"}]{#struct_0_x1139_12555_x127154637}

[[端口状态为]{style="font-family:宋体"}[Forwarding]{lang="EN-US"}]{#struct_0_x1139_12555_1356934760}[状态]{style="font-family:宋体"}

[[\[DISCARDING\]]{lang="EN-US"}]{#struct_0_x1139_12555_1794068864}

[[端口状态为]{style="font-family:宋体"}[Discarding]{lang="EN-US"}]{#struct_0_x1139_12555_1305195482}[状态]{style="font-family:宋体"}

[[\[LEARNING\]]{lang="EN-US"}]{#struct_0_x1139_12555_1924098762}

[[端口状态为]{style="font-family:宋体"}[Learning]{lang="EN-US"}]{#struct_0_x1139_12555_x1204823874}[状态]{style="font-family:宋体"}

[[Port protocol]{lang="EN-US"}]{#struct_0_x1139_12555_1052282803}

[[生成树协议在端口上的开启状态]{style="font-family:宋体"}]{#struct_0_x1139_12555_1438929304}

[[Port role]{lang="EN-US"}]{#struct_0_x1139_12555_1171211313}

[[端口角色，和]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_89243821}[相对应。具体角色分为：]{style="font-family:宋体"}[Alternate]{lang="EN-US"}[、]{style="font-family:宋体"}[Backup]{lang="EN-US"}[、]{style="font-family:宋体"}[Root]{lang="EN-US"}[、]{style="font-family:宋体"}[Designated]{lang="EN-US"}[、]{style="font-family:宋体"}[Master]{lang="EN-US"}[、]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[(Boundary)]{lang="EN-US"}]{#struct_0_x1139_12555_x1478816221}

[[表示该端口为域边界端口]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1792087232}

[[Port ID]{lang="EN-US"}]{#struct_0_x1139_12555_x681870326}

[[端口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1139_12555_419054959}

[[Port cost(Legacy)]{lang="EN-US"}]{#struct_0_x1139_12555_323184057}

[[端口的路径开销（]{style="font-family:宋体"}[Legacy]{lang="EN-US"}]{#struct_0_x1139_12555_x1997665494}[表示当前设备的路径开销的计算方法，此外还有]{style="font-family:宋体"}[dot1d-1998]{lang="EN-US"}[和]{style="font-family:宋体"}[dot1t]{lang="EN-US"}[两种计算方式）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Config]{lang="EN-US"}]{#struct_0_x1139_12555_x1542425353}[：表示配置值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1139_12555_x2059136560}[：表示实际值]{lang="EN-US" style="font-family:宋体"}

[[Desg.bridge/port]{lang="EN-US"}]{#struct_0_x1139_12555_901788245}

[[端口的指定桥]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1139_12555_397949570}[和端口]{style="font-family:宋体"}[ID]{lang="EN-US"}[（对于不支持端口优先级的端口，这里显示的端口]{style="font-family:宋体"}[ID]{lang="EN-US"}[没有意义）]{style="font-family:宋体"}

[[Port edged]{lang="EN-US"}]{#struct_0_x1139_12555_1889267998}

[[端口是否为边缘端口：]{style="font-family:宋体"}]{#struct_0_x1139_12555_x829303428}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Config]{lang="EN-US"}]{#struct_0_x1139_12555_685661898}[：表示配置值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1139_12555_x1631474890}[：表示实际值]{lang="EN-US" style="font-family:宋体"}

[[Point-to-Point]{lang="EN-US"}]{#struct_0_x1139_12555_1976014183}

[[端口是否与点对点链路相连：]{style="font-family:宋体"}]{#struct_0_x1139_12555_1371932523}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Config]{lang="EN-US"}]{#struct_0_x1139_12555_x1608114924}[：表示配置值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1139_12555_679479953}[：表示实际值]{lang="EN-US" style="font-family:宋体"}

[[Transmit limit]{lang="EN-US"}]{#struct_0_x1139_12555_x1054465872}

[[端口每个]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}]{#struct_0_x1139_12555_x881193886}[时间间隔发送报文的上限]{style="font-family:宋体"}

[[Protection type]{lang="EN-US"}]{#struct_0_x1139_12555_x946483260}

[[端口是否开启保护：]{style="font-family:宋体"}]{#struct_0_x1139_12555_1944624313}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Config]{lang="EN-US"}]{#struct_0_x1139_12555_x2049403402}[：表示配置值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1139_12555_1467713578}[：表示实际值]{lang="EN-US" style="font-family:宋体"}

[[端口遇到异常情况启动保护的类型：]{style="font-family:宋体"}]{#struct_0_x1139_12555_695251267}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1139_12555_x796844662}[OOT]{lang="EN-US"}[：表示根保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LOOP]{lang="EN-US"}]{#struct_0_x1139_12555_x1647773422}[：表示环路保护]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_1842279367}[：表示]{lang="EN-US" style="font-family:宋体"}[BPDU]{lang="EN-US"}[保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVST ]{lang="EN-US"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_1159421325}[：表示]{lang="EN-US" style="font-family:宋体"}[MSTP]{lang="EN-US"}[的]{style="font-family:宋体"}[PVST ]{lang="EN-US"}[BPDU]{lang="EN-US"}[保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x1139_12555_1783410676}[ONE]{lang="EN-US"}[：表示无保护]{lang="EN-US" style="font-family:宋体"}

[[TC-Restriction]{lang="EN-US"}]{#struct_0_x1139_12555_x1496287508}

[[端口是否开启了]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x886603988}[传播限制功能]{style="font-family:宋体"}

[[Role-Restriction]{lang="EN-US"}]{#struct_0_x1139_12555_1388499097}

[[端口是否开启了端口角色限制功能]{style="font-family:宋体"}]{#struct_0_x1139_12555_1113343672}

[[MST BPDU format]{lang="EN-US"}]{#struct_0_x1139_12555_x1917606026}

[[端口发送]{style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_x757568937}[报文的格式，取值为]{style="font-family:宋体"}[legacy]{lang="EN-US"}[和]{style="font-family:宋体"}[802.1s]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Config]{lang="EN-US"}]{#struct_0_x1139_12555_x1289888515}[：表示配置值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1139_12555_x787700100}[：表示实际值]{lang="EN-US" style="font-family:宋体"}

[[Port Config-]{lang="EN-US"}]{#struct_0_x1139_12555_619463948}

[[Digest-Snooping]{lang="EN-US"}]{#struct_0_x1139_12555_1317085319}

[[摘要侦听功能在端口上的开启状态]{style="font-family:宋体"}]{#struct_0_x1139_12555_276195426}

[[Rapid transition]{lang="EN-US"}]{#struct_0_x1139_12555_1447565415}

[[端口在当前]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x165091997}[或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中是否快速迁移至转发状态]{style="font-family:宋体"}

[[Num of VLANs mapped]{lang="EN-US"}]{#struct_0_x1139_12555_x1445096206}

[[端口在当前]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x127089101}[中的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[计数]{style="font-family:宋体"}

[[Port times]{lang="EN-US"}]{#struct_0_x1139_12555_1279007207}

[[端口相关的主要参数值：]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1198556146}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x1139_12555_677093892}[：表示]{lang="EN-US" style="font-family:宋体"}[Hello time]{lang="EN-US"}[定时器值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MaxAge]{lang="EN-US"}]{#struct_0_x1139_12555_1438994840}[：表示]{lang="EN-US" style="font-family:宋体"}[Max Age]{lang="EN-US"}[定时器值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FwdDelay]{lang="EN-US"}]{#struct_0_x1139_12555_776552844}[：表示]{lang="EN-US" style="font-family:宋体"}[Forward delay]{lang="EN-US"}[定时器值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MsgAge]{lang="EN-US"}]{#struct_0_x1139_12555_x309881626}[：表示]{lang="EN-US" style="font-family:宋体"}[Message Age]{lang="EN-US"}[定时器值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RemHops]{lang="EN-US"}]{#struct_0_x1139_12555_x677878141}[：表示剩余跳数]{lang="EN-US" style="font-family:宋体"}

[[BPDU sent]{lang="EN-US"}]{#struct_0_x1139_12555_323249593}

[[端口发送报文计数]{style="font-family:宋体"}]{#struct_0_x1139_12555_632735251}

[[BPDU received]{lang="EN-US"}]{#struct_0_x1139_12555_x1530134803}

[[端口接收报文计数]{style="font-family:宋体"}]{#struct_0_x1139_12555_1730442412}

[[RegRoot ID/IRPC]{lang="EN-US"}]{#struct_0_x1139_12555_1889333534}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x1140260099}[域根]{style="font-family:宋体"}[/]{lang="EN-US"}[内部路径开销]{style="font-family:宋体"}

[[Root Type]{lang="EN-US"}]{#struct_0_x1139_12555_x2007071229}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_56339756}[域根类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary root]{lang="EN-US"}]{#struct_0_x1139_12555_679021201}[：表示根桥]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Secondary root]{lang="EN-US"}]{#struct_0_x1139_12555_1506628014}[：表示备份根桥]{lang="EN-US" style="font-family:宋体"}

[[Master bridge]{lang="EN-US"}]{#struct_0_x1139_12555_123455616}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_2035231548}[的]{style="font-family:宋体"}[Master]{lang="EN-US"}[桥]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Cost to master]{lang="EN-US"}]{#struct_0_x1139_12555_x2049862154}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_2117393539}[到]{style="font-family:宋体"}[Master]{lang="EN-US"}[桥的路径开销]{style="font-family:宋体"}

[[TC received]{lang="EN-US"}]{#struct_0_x1139_12555_x587163087}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_384880579}[收到的]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[Protocol status]{lang="EN-US"}]{#struct_0_x1139_12555_1841820615}

[[生成树协议的全局开启状态]{style="font-family:宋体"}]{#struct_0_x1139_12555_x217103667}

[[Protocol Std.]{lang="EN-US"}]{#struct_0_x1139_12555_1459713091}

[[生成树协议采用的协议标准]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1799829800}

[[Version]{lang="EN-US"}]{#struct_0_x1139_12555_x887062740}

[[生成树协议采用的协议版本]{style="font-family:宋体"}]{#struct_0_x1139_12555_x567780660}

[[Bridge-Prio.]{lang="EN-US"}]{#struct_0_x1139_12555_x1470946968}

[[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_x856836967}[模式下，表示本设备在]{style="font-family:宋体"}[CIST]{lang="EN-US"}[中的桥优先级；在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，表示本设备在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中的桥优先级]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1139_12555_x1290347267}

[[本设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1139_12555_1690239254}[地址]{style="font-family:宋体"}

[[Max age(s)]{lang="EN-US"}]{#struct_0_x1139_12555_x580370560}

[[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_275736674}[的最大生存时间（单位为秒，在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下为在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中的配置）]{style="font-family:宋体"}

[[Forward delay(s)]{lang="EN-US"}]{#struct_0_x1139_12555_x1551999930}

[[端口状态迁移的延时（单位为秒，在]{style="font-family:宋体"}[PVST]{lang="EN-US"}]{#struct_0_x1139_12555_x1105329176}[模式下为在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中的配置）]{style="font-family:宋体"}

[[Hello time(s)]{lang="EN-US"}]{#struct_0_x1139_12555_x245125660}

[[根设备发送]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x127547853}[的周期（单位为秒，在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下为在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中的配置）]{style="font-family:宋体"}

[[Max hops]{lang="EN-US"}]{#struct_0_x1139_12555_x658469725}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x777529}[域中的最大跳数]{style="font-family:宋体"}

[[TC Snooping]{lang="EN-US"}]{#struct_0_x1139_12555_1050544720}

[[TC Snooping]{lang="EN-US"}]{#struct_0_x1139_12555_1438536088}[开启状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_934636247}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x1056212790}

::: {#-1282279868 .myid}
[]{#_Toc138217691}[]{#_Toc404784577}[]{#struct_0_x1139_12555_1093747244}[]{#_Toc144808331}

**生成树 \-- 生成树配置命令 \-- display stp abnormal-port**

------------------------------------------------------------------------

[**[display stp abnormal-port]{lang="EN-US"}**]{#struct_0_x1139_12555_x1887777557}[命令用来显示被生成树保护功能阻塞的端口信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1756448953}

[**[display stp abnormal-port]{lang="EN-US"}**]{#struct_0_x1139_12555_x244017445}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x713832097}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x857613}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_561034749}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1994954523}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_12187717}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_215843020}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_1002182932}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1756514489}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1363293881}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示被生成树保护功能阻塞的端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp abnormal-port]{lang="EN-US"}]{#struct_0_x1139_12555_1647555031}

[ MST ID      Blocked Port                 Reason]{lang="EN-US"}

[ 1           GigabitEthernet1/0/1         Root-Protected]{lang="EN-US"}

[ 2           GigabitEthernet1/0/2         Loop-Protected]{lang="EN-US"}

[ 12          GigabitEthernet1/0/3         Loopback-Protected]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_466053226}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示被生成树保护功能阻塞的端口信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_466118762}

[\[Sysname\] stp mode pvst]{lang="EN-US"}

[\[Sysname\] display stp abnormal-port]{lang="EN-US"}

[ VLAN ID      Blocked Port                 Reason]{lang="EN-US"}

[ 1            GigabitEthernet1/0/1         Root-Protected]{lang="EN-US"}

[ 2            GigabitEthernet1/0/2         Loop-Protected]{lang="EN-US"}

[ 2            GigabitEthernet1/0/3         Loopback-Protected]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display stp abnormal-port]{lang="EN-US"}]{#struct_0_x1139_12555_459007330}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1263419867}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_889775576}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_1503252478}

[[MST ID]{lang="EN-US"}]{#struct_0_x1139_12555_x1756580025}

[[被生成树保护功能阻塞的端口所在]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_1199554894}[的编号]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x1139_12555_467036266}

[[被生成树保护功能阻塞的端口所在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_466446441}[的编号]{style="font-family:宋体"}

[[Blocked Port]{lang="EN-US"}]{#struct_0_x1139_12555_538126975}

[[被生成树保护功能阻塞的端口的名称]{style="font-family:宋体"}]{#struct_0_x1139_12555_2093102702}

[[Reason]{lang="EN-US"}]{#struct_0_x1139_12555_1245274773}

[[导致端口阻塞的原因：]{style="font-family:宋体"}]{#struct_0_x1139_12555_838300077}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Root-Protected]{lang="EN-US"}]{#struct_0_x1139_12555_x1756645561}[：表示发生了根保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loop-Protected]{lang="EN-US"}]{#struct_0_x1139_12555_1420275105}[：表示发生了环路保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loopback-Protected]{lang="EN-US"}]{#struct_0_x1139_12555_1631311441}[：表示发生了自环保护，即有实例端口收到了自己发出的协议报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disputed]{lang="EN-US"}]{#struct_0_x1139_12555_1631428774}[：表示发生了]{lang="EN-US" style="font-family:宋体"}[Dispute]{lang="EN-US"}[保护，即端口收到了非阻塞指定端口发出的低优先级消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[InconsistentPortType-Protected]{lang="EN-US"}]{#struct_0_x1139_12555_466315369}[：表示发生了]{lang="EN-US" style="font-family:宋体"}[端口类型不一致保护]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[InconsistentPvid-Protected]{lang="EN-US"}]{#struct_0_x1139_12555_466380905}[：表示发生了]{style="font-family:
  宋体"}[PVID]{lang="EN-US"}[不一致保护]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc144808332}

::: {#396406738 .myid}
[]{#_Toc404784578}[]{#struct_0_x1139_12555_x1528710803}[]{#_Toc251143559}

**生成树 \-- 生成树配置命令 \-- display stp bpdu-statistics**

------------------------------------------------------------------------

[**[display stp bpdu-statistics]{lang="EN-US"}**]{#struct_0_x1139_12555_x92448634}[命令用来显示端口上的]{style="font-family:
宋体"}[BPDU]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_807409702}

[**[display stp bpdu-statistics]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \[ **instance** *instance-list* \] \]]{lang="EN-US"}]{#struct_0_x1139_12555_x1756711097}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1230434903}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1180351957}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1752509433}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_981488811}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_209897612}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x388287465}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_1872732691}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1457331669}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1139_12555_x1756776633}[：显示指定端口上的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示端口类型和端口编号。]{style="font-family:宋体"}

[**[instance ]{lang="EN-US"}***[instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x1979347237}[：显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在端口上的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x979067909}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_x1965864798}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定端口和]{style="font-family:宋体"}]{#struct_0_x1139_12555_x364135485}[MSTI]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在所有端口上的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[统计信息，显示信息按照端口名称的顺序排列，各端口内部再按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了端口但未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_303785920}[MSTI]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在该端口上的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[统计信息，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_x701088914}[MSTI]{lang="EN-US"}[和端口，则显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在指定端口上的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}]{#struct_0_x1139_12555_400790870}[/PVST]{lang="EN-US"}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定端口，则显示所有端口上的]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2090683786}[BPDU]{lang="EN-US"}[统计信息，显示信息按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了端口，则显示该端口上的]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1756842169}[BPDU]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1897157237}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x849687256}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp bpdu-statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1139_12555_x1756907705}

[ Port: GigabitEthernet1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Instance-Independent:]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Type                        Count      Last Updated]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Invalid BPDUs               0]{lang="EN-US"}

[ Looped-back BPDUs           0]{lang="EN-US"}

[ Max-aged BPDUs              0]{lang="EN-US"}

[ TCN sent                    0]{lang="EN-US"}

[ TCN received                0]{lang="EN-US"}

[ TCA sent                    0]{lang="EN-US"}

[ TCA received                2          10:33:12 01/13/2011]{lang="EN-US"}

[ Config sent                 0]{lang="EN-US"}

[ Config received             0]{lang="EN-US"}

[ RST sent                    0]{lang="EN-US"}

[ RST received                0]{lang="EN-US"}

[ MST sent                    4          10:33:11 01/13/2011]{lang="EN-US"}

[ MST received                151        10:37:43 01/13/2011]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Instance 0:]{lang="EN-US"}

[ Type                        Count      Last Updated]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Timeout BPDUs               0]{lang="EN-US"}

[ Max-hoped BPDUs             0]{lang="EN-US"}

[ TC detected                 1          10:32:40 01/13/2011]{lang="EN-US"}

[ TC sent                     3          10:33:11 01/13/2011]{lang="EN-US"}

[ TC received                 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_467036265}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_466446444}

[\[Sysname\] stp mode pvst]{lang="EN-US"}

[\[Sysname\] display stp bpdu-statistics interface gigabitethernet 1/0/1]{lang="EN-US"}

[ Port: GigabitEthernet1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Type                        Count      Last Updated]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Invalid BPDUs               0]{lang="EN-US"}

[ Looped-back BPDUs           0]{lang="EN-US"}

[ Max-aged BPDUs              0]{lang="EN-US"}

[ TCN sent                    0]{lang="EN-US"}

[ TCN received                0]{lang="EN-US"}

[ TCA sent                    0]{lang="EN-US"}

[ TCA received                2           10:33:12 01/13/2010]{lang="EN-US"}

[ Config sent                 0]{lang="EN-US"}

[ Config received             0]{lang="EN-US"}

[ RST sent                    0]{lang="EN-US"}

[ RST received                0]{lang="EN-US"}

[ MST sent                    4           10:33:11 01/13/2010]{lang="EN-US"}

[ MST received                151         10:37:43 01/13/2010]{lang="EN-US"}

[ Timeout BPDUs               0]{lang="EN-US"}

[ Max-hoped BPDUs             0]{lang="EN-US"}

[ TC detected                 511         10:32:40 01/13/2010]{lang="EN-US"}

[ TC sent                     8844        10:33:11 01/13/2010]{lang="EN-US"}

[ TC received                 1426        10:33:32 01/13/2010]{lang="EN-US"}

[ PVID inconsistency BPDUs    0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display stp bpdu-statistics]{lang="EN-US"}]{#struct_0_x1139_12555_x607977177}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1265141590}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2117382252}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_1606745589}

[[Port]{lang="EN-US"}]{#struct_0_x1139_12555_x594384233}

[[端口名称]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1755924665}

[[Instance-Independent]{lang="EN-US"}]{#struct_0_x1139_12555_x756019011}

[[与]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x2019876382}[无关的统计信息]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1139_12555_x666319138}

[[统计类型]{style="font-family:宋体"}]{#struct_0_x1139_12555_x602476350}

[[Count]{lang="EN-US"}]{#struct_0_x1139_12555_x1106126180}

[[统计值]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1755990201}

[[Last Updated]{lang="EN-US"}]{#struct_0_x1139_12555_x919757998}

[[最后更新时间]{style="font-family:宋体"}]{#struct_0_x1139_12555_849168228}

[[Invalid BPDUs]{lang="EN-US"}]{#struct_0_x1139_12555_x1284601658}

[[无效]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x1887153625}[的数量]{style="font-family:宋体"}

[[Looped-back BPDUs]{lang="EN-US"}]{#struct_0_x1139_12555_1487589930}

[[自环（即收到由本端口发出）的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x1756448956}[数量]{style="font-family:宋体"}

[[Max-aged BPDUs]{lang="EN-US"}]{#struct_0_x1139_12555_515497442}

[[超过最大生存时间的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x1050918760}[数量]{style="font-family:宋体"}

[[TCN sent]{lang="EN-US"}]{#struct_0_x1139_12555_x1889451774}

[[发出的]{style="font-family:宋体"}[TCN]{lang="EN-US"}]{#struct_0_x1139_12555_x1511825970}[报文数量]{style="font-family:宋体"}

[[TCN received]{lang="EN-US"}]{#struct_0_x1139_12555_x1756514492}

[[收到的]{style="font-family:宋体"}[TCN]{lang="EN-US"}]{#struct_0_x1139_12555_153374764}[报文数量]{style="font-family:宋体"}

[[TCA sent]{lang="EN-US"}]{#struct_0_x1139_12555_1823848164}

[[发出的]{style="font-family:宋体"}[TCA]{lang="EN-US"}]{#struct_0_x1139_12555_x1269770314}[报文数量]{style="font-family:宋体"}

[[TCA received]{lang="EN-US"}]{#struct_0_x1139_12555_x1278775647}

[[收到的]{style="font-family:宋体"}[TCA]{lang="EN-US"}]{#struct_0_x1139_12555_x1756580028}[报文数量]{style="font-family:宋体"}

[[Config sent]{lang="EN-US"}]{#struct_0_x1139_12555_x1979667155}

[[发出的]{style="font-family:宋体"}[Configuration]{lang="EN-US"}]{#struct_0_x1139_12555_464287038}[报文数量]{style="font-family:宋体"}

[[Config received]{lang="EN-US"}]{#struct_0_x1139_12555_1462447458}

[[收到的]{style="font-family:宋体"}[Configuration]{lang="EN-US"}]{#struct_0_x1139_12555_x1756645564}[报文数量]{style="font-family:宋体"}

[[RST sent]{lang="EN-US"}]{#struct_0_x1139_12555_x2115177304}

[[发出的]{style="font-family:宋体"}[RSTP BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_652280669}[数量]{style="font-family:宋体"}

[[RST received]{lang="EN-US"}]{#struct_0_x1139_12555_1691430435}

[[收到的]{style="font-family:宋体"}[RSTP BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x1756711100}[数量]{style="font-family:宋体"}

[[MST sent]{lang="EN-US"}]{#struct_0_x1139_12555_x336107791}

[[发出的]{style="font-family:宋体"}[MSTP BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_521045048}[数量]{style="font-family:宋体"}

[[MST received]{lang="EN-US"}]{#struct_0_x1139_12555_x158534499}

[[收到的]{style="font-family:宋体"}[MSTP BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x1756776636}[数量]{style="font-family:宋体"}

[[Instance]{lang="EN-US"}]{#struct_0_x1139_12555_1912335532}

[[与指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x1806081252}[相关的统计信息]{style="font-family:宋体"}

[[Timeout BPDUs]{lang="EN-US"}]{#struct_0_x1139_12555_147310297}

[[老化的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x1756842172}[数量]{style="font-family:宋体"}

[[Max-hoped BPDUs]{lang="EN-US"}]{#struct_0_x1139_12555_1137707886}

[[超过最大跳数的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x508447007}[数量]{style="font-family:宋体"}

[[TC detected]{lang="EN-US"}]{#struct_0_x1139_12555_x33730766}

[[监测到的拓扑变化的次数]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1756907708}

[[TC sent]{lang="EN-US"}]{#struct_0_x1139_12555_x204692650}

[[发出的]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_x1139_12555_x952432527}[报文数量]{style="font-family:宋体"}

[[TC received]{lang="EN-US"}]{#struct_0_x1139_12555_1164904789}

[[收到的]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_x1139_12555_x1755924668}[报文数量]{style="font-family:宋体"}

[[PVID inconsistency BPDUs]{lang="EN-US"}]{#struct_0_x1139_12555_x127482317}

[[收到的]{style="font-family:宋体"}[PVID]{lang="EN-US"}]{#struct_0_x1139_12555_x1025512819}[不一致的]{style="font-family:宋体"}[PVST]{lang="EN-US"}[报文数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#627781411 .myid}
[]{#_Toc404784579}[]{#struct_0_x1139_12555_x352734484}

**生成树 \-- 生成树配置命令 \-- display stp down-port**

------------------------------------------------------------------------

[**[display stp down-port]{lang="EN-US"}**]{#struct_0_x1139_12555_1302863944}[命令用来显示被生成树保护功能]{style="font-family:宋体"}[down]{lang="EN-US"}[掉的端口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1749790283}

[**[display stp down-port]{lang="EN-US"}**]{#struct_0_x1139_12555_830423932}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_374429482}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x760518489}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1755990204}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1679272885}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_1315465419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_2090820209}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_x1369486556}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x325656453}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x256763801}[显示被生成树保护功能]{style="font-family:宋体"}[down]{lang="EN-US"}[掉的端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp down-port]{lang="EN-US"}]{#struct_0_x1139_12555_x275999525}

[ Down Port                     Reason]{lang="EN-US"}

[ GigabitEthernet1/0/1          BPDU protection]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display stp down-port]{lang="EN-US"}]{#struct_0_x1139_12555_705227119}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1291522950}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1756448955}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_918781969}

[[Down Port]{lang="EN-US"}]{#struct_0_x1139_12555_311715260}

[[被生成树保护功能]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1139_12555_x187690162}[掉的端口名称]{style="font-family:宋体"}

[[Reason]{lang="EN-US"}]{#struct_0_x1139_12555_1024148782}

[[导致端口]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1139_12555_x1518741359}[的原因：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x1756514491}[ ]{lang="EN-US"}[protection]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[BPDU]{lang="EN-US"}[保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVST BPDU protection]{lang="EN-US"}]{#struct_0_x1139_12555_322856377}[：表示]{lang="EN-US" style="font-family:
  宋体"}[MSTP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:
  宋体"}[PVST BPDU]{lang="EN-US"}[保护]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1069011744 .myid}
[]{#_Toc404784580}[]{#struct_0_x1139_12555_1719458705}

**生成树 \-- 生成树配置命令 \-- display stp history**

------------------------------------------------------------------------

[**[display stp history]{lang="EN-US"}**]{#struct_0_x1139_12555_x72046216}[命令用来显示生成树端口角色计算的历史信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2019551891}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1139_12555_1733788707}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** ]{lang="EN-US"}]{#struct_0_x1139_12555_x692864623}*[vlan-id-list ]{lang="EN-US"}*[\] **history**]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_813365526}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** ]{lang="EN-US"}]{#struct_0_x1139_12555_162391905}*[vlan-id-list]{lang="EN-US"}*[ ]{lang="EN-US"}[\] **history** \[ **slot** *slot-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1139_12555_x1415033810}[模式：]{style="font-family:宋体"}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** ]{lang="EN-US"}]{#struct_0_x1139_12555_x1756580027}*[vlan-id-list]{lang="EN-US"}*[ ]{lang="EN-US"}[\] **history** \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1932612988}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x87928424}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1025823813}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1445097304}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_737438078}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1499849944}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_x1150105067}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_695069352}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x1756645563}[：显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_466249835}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** vlan*-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}[vlan*-id*]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_x1711892777}[：显示指定单板上端口角色计算的历史信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示所有单板上端口角色计算的历史信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_x108517808}[：显示指定成员设备上端口角色计算的历史信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，将显示所有成员设备上端口角色计算的历史信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_1888940318}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上端口角色计算的历史信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定该参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上端口角色计算的历史信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_1765363476}[：显示指定成员设备的指定单板上端口角色计算的历史信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示所有单板上端口角色计算的历史信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_1559918156}[：显示指定单板上端口角色计算的历史信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，将显示所有单板上端口角色计算的历史信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x369118784}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{style="font-family:宋体"}]{#struct_0_x1139_12555_1651604449}[STP/RSTP]{lang="EN-US"}[模式下，显示信息按照端口角色计算的时间先后顺序排列。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[PVST]{lang="EN-US"}]{#struct_0_x1139_12555_466053227}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1036834776}[VLAN]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中端口角色计算的历史信息，显示信息按照]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内部再按照端口角色计算的时间先后顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_466118763}[VLAN]{lang="EN-US"}[，则显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中端口角色计算的历史信息，显示信息按照]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内部再按照端口角色计算的时间先后顺序排列。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_1754813022}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_488228409}[MSTI]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[中端口角色计算的历史信息，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[内部再按照端口角色计算的时间先后顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1756711099}[MSTI]{lang="EN-US"}[，则显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[中端口角色计算的历史信息，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[内部再按照端口角色计算的时间先后顺序排列。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2037003957}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1139_12555_x311788230}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1911256987}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 2 history]{lang="EN-US"}]{#struct_0_x1139_12555_x881725803}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  Instance 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Port GigabitEthernet1/0/1]{lang="EN-US"}

[   Role change         : ROOT-\>DESI (Aged)]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Port GigabitEthernet1/0/2]{lang="EN-US"}

[   Role change         : ALTER-\>ROOT]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[                         128.153]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[                         128.153]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1906403163}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp vlan 2 history]{lang="EN-US"}]{#struct_0_x1139_12555_x1906599771}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  VLAN 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Port GigabitEthernet1/0/1]{lang="EN-US"}

[   Role change         : ROOT-\>DESI (Aged)]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[ Port GigabitEthernet1/0/2]{lang="EN-US"}

[   Role change         : ALTER-\>ROOT]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式应用]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1780839404}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1756776635}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 2 history slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_x1906534235}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 history trace \-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  Instance 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Port GigabitEthernet1/0/1]{lang="EN-US"}

[   Role change         : ROOT-\>DESI (Aged)]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[ Port GigabitEthernet1/0/2]{lang="EN-US"}

[   Role change         : ALTER-\>ROOT]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[                         128.153]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[                         128.153]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1905682267}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp vlan 2 history slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_71675454}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 history trace \-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  VLAN 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Port GigabitEthernet1/0/1]{lang="EN-US"}

[   Role change         : ROOT-\>DESI (Aged)]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[ Port GigabitEthernet1/0/2]{lang="EN-US"}

[   Role change         : ALTER-\>ROOT]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1139_12555_x418867068}[IRF]{lang="EN-US"}[设备应用]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_312166330}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 2 history slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_x1906141020}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 history trace \-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  Instance 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Port GigabitEthernet1/0/1]{lang="EN-US"}

[   Role change         : ROOT-\>DESI (Aged)]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[ Port GigabitEthernet1/0/2]{lang="EN-US"}

[   Role change         : ALTER-\>ROOT]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[                         128.153]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[                         128.153]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1906337628}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp vlan 2 history slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_71544382}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 history trace \-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  VLAN 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Port GigabitEthernet1/0/1]{lang="EN-US"}

[   Role change         : ROOT-\>DESI (Aged)]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[ Port GigabitEthernet1/0/2]{lang="EN-US"}

[   Role change         : ALTER-\>ROOT]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1139_12555_1540992413}[IRF]{lang="EN-US"}[模式应用]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_740645239}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 2 history chassis 1 slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_x1906599772}

[ \-\-\-\-\-\-\-\-\-- STP chassis 1 slot 1 history trace \-\-\-\-\-\-\--]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  Instance 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Port GigabitEthernet1/1/0/1]{lang="EN-US"}

[   Role change         : ROOT-\>DESI (Aged)]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[ Port GigabitEthernet1/1/0/2]{lang="EN-US"}

[   Role change         : ALTER-\>ROOT]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[                         128.153]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[                         128.153]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1906534236}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中端口角色计算的历史信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp vlan 2 history chassis 1 slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_71609918}

[ \-\-\-\-\-\-\-\-\-- STP chassis 1 slot 1 history trace \-\-\-\-\-\-\--]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  VLAN 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Port GigabitEthernet1/1/0/1]{lang="EN-US"}

[   Role change         : ROOT-\>DESI (Aged)]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1]{lang="EN-US"}

[ Port GigabitEthernet1/1/0/2]{lang="EN-US"}

[   Role change         : ALTER-\>ROOT]{lang="EN-US"}

[   Time                : 2009/02/08 00:22:56]{lang="EN-US"}

[   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display stp history]{lang="EN-US"}]{#struct_0_x1139_12555_x1360116323}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1290666078}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1756907707}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_554822237}

[[Port]{lang="EN-US"}]{#struct_0_x1139_12555_590760408}

[[端口名称]{style="font-family:宋体"}]{#struct_0_x1139_12555_x638654960}

[[Role change]{lang="EN-US"}]{#struct_0_x1139_12555_x1296560022}

[[显示端口的角色变化（]{style="font-family:宋体"}[Aged]{lang="EN-US"}]{#struct_0_x1139_12555_x572815669}[表示由于报文超时引起的角色变化）]{style="font-family:宋体"}

[[Time]{lang="EN-US"}]{#struct_0_x1139_12555_x1755924667}

[[端口角色计算时间]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1918818425}

[[Port priority]{lang="EN-US"}]{#struct_0_x1139_12555_52736148}

[[端口优先级]{style="font-family:宋体"}]{#struct_0_x1139_12555_1352857400}

[[Designated priority]{lang="EN-US"}]{#struct_0_x1139_12555_x1906337625}

[[指定优先级]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1906468697}

[ ]{lang="EN-US"}

::::: {#585389843 .myid}
[]{#_Toc404784581}[]{#struct_0_x1139_12555_1719399372}

**生成树 \-- 生成树配置命令 \-- display stp ignored-vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](生成树命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1139_12555_x2012203643}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1139_12555_x1906896250}
:::

[ ]{lang="EN-US"}

[**[display stp ignored-vlan]{lang="EN-US"}**]{#struct_0_x1139_12555_x1755990203}[命令用来显示已开启]{style="font-family:
宋体"}[VLAN Ignore]{lang="EN-US"}[功能的]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_243041416}

[**[display stp ignored-vlan]{lang="EN-US"}**]{#struct_0_x1139_12555_202782384}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1878164524}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_1401882450}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1997981265}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1182234542}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_1352518688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_77187406}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_x1756448958}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1678296856}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1589899503}[显示已开启]{style="font-family:宋体"}[VLAN Ignore]{lang="EN-US"}[功能的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[\<Sysname\> display stp ignored-vlan]{lang="EN-US"}]{#struct_0_x1139_12555_x1348188628}

[ STP-Ignored VLANs: 1 to 2, 4]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display stp ignored-vlan]{lang="EN-US"}]{#struct_0_x1139_12555_x261466826}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1284170674}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_1203166440}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2008216315}

[[STP-Ignored VLANs]{lang="EN-US"}]{#struct_0_x1139_12555_x1756514494}

[[已开启]{style="font-family:宋体"}[VLAN Ignore]{lang="EN-US"}]{#struct_0_x1139_12555_959943818}[功能的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[None]{lang="EN-US"}[表示尚无]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[开启]{style="font-family:宋体"}[VLAN Ignore]{lang="EN-US"}[功能]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1925780360 .myid}
[]{#_Toc404784582}[]{#struct_0_x1139_12555_x1987915536}

**生成树 \-- 生成树配置命令 \-- display stp region-configuration**

------------------------------------------------------------------------

[**[display stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x2126311931}[命令用来显示当前生效的]{style="font-family:宋体"}[MST]{lang="EN-US"}[域配置信息，包括域名、修订级别以及]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_144658849}

[**[display stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_508225556}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_305442225}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x823184416}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x824037782}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1756580030}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_1959004245}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_722031273}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_1382941486}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x398202130}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1242512458}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示当前生效的]{style="font-family:宋体"}[MST]{lang="EN-US"}[域配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp region-configuration]{lang="EN-US"}]{#struct_0_x1139_12555_x1756645566}

[ Oper Configuration]{lang="EN-US"}

[   Format selector      : 0]{lang="EN-US"}

[   Region name          : hello]{lang="EN-US"}

[   Revision level       : 0]{lang="EN-US"}

[   Configuration digest : 0x5f762d9a46311effb7a488a3267fca9f]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Instance   VLANs Mapped]{lang="EN-US"}

[   0          21 to 4094]{lang="EN-US"}

[   1          1 to 10]{lang="EN-US"}

[   2          11 to 20]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display stp region-configuration]{lang="EN-US"}]{#struct_0_x1139_12555_x952377890}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1287369361}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_1590411764}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_1273619339}

[[Format selector]{lang="EN-US"}]{#struct_0_x1139_12555_x693036209}

[[生成树协议规定的选择因子，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1139_12555_423628406}[，不可配置]{style="font-family:宋体"}

[[Region name]{lang="EN-US"}]{#struct_0_x1139_12555_x1209258508}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x1756711102}[域的域名]{style="font-family:宋体"}

[[Revision level]{lang="EN-US"}]{#struct_0_x1139_12555_826691623}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x1157027297}[域的修订级别，可使用命令]{style="font-family:宋体"}**[revision-level]{lang="EN-US"}**[来配置，缺省为]{style="font-family:宋体"}[0]{lang="EN-US"}[级]{style="font-family:宋体"}

[[Configuration digest]{lang="EN-US"}]{#struct_0_x1139_12555_x1254248921}

[[配置摘要]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2003667302}

[[VLANs Mapped]{lang="EN-US"}]{#struct_0_x1139_12555_x1093942027}

[[映射到]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x1756776638}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1105766478}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[instance]{lang="EN-US"}**]{#struct_0_x1139_12555_x1808003898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[region-name]{lang="EN-US"}**]{#struct_0_x1139_12555_2060941551}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[revision-level]{lang="EN-US"}**]{#struct_0_x1139_12555_x1393247592}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vlan-mapping modulo]{lang="EN-US"}**]{#struct_0_x1139_12555_210992850}

::: {#-430817875 .myid}
[]{#_Toc404784583}[]{#struct_0_x1139_12555_x1315718408}[]{#_Toc144808335}

**生成树 \-- 生成树配置命令 \-- display stp root**

------------------------------------------------------------------------

[**[display stp root]{lang="EN-US"}**]{#struct_0_x1139_12555_x811566746}[命令用来显示所有生成树的根桥信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1756842174}

[**[display stp root]{lang="EN-US"}**]{#struct_0_x1139_12555_x1994459996}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x685621424}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_2102770116}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1840125769}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_976414184}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_x307108269}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_662803889}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_2034350905}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1756907710}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_151472174}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示所有生成树的根桥信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp root]{lang="EN-US"}]{#struct_0_x1139_12555_792104996}

[ MST ID  Root Bridge ID        ExtPathCost IntPathCost Root Port]{lang="EN-US"}

[ 0       0.00e0-fc0e-6554      200200      0           GigabitEthernet1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1906337626}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示所有生成树的根桥信息。]{style="font-family:宋体"}

[[\<Sysname\> display stp root]{lang="EN-US"}]{#struct_0_x1139_12555_x1906272090}

[ VLAN ID  Root Bridge ID        ExtPathCost IntPathCost Root Port]{lang="EN-US"}

[ 1        0.00e0-fc0e-6554      200200      0           GigabitEthernet1/0/1]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display stp root]{lang="EN-US"}]{#struct_0_x1139_12555_x546491441}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1281151191}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1625061908}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_1335581049}

[[MST ID]{lang="EN-US"}]{#struct_0_x1139_12555_x1755924670}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_3430340}[的编号]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x1139_12555_x1906534234}

[[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_x1905682266}[的编号]{style="font-family:宋体"}

[[Root Bridge ID]{lang="EN-US"}]{#struct_0_x1139_12555_x520813285}

[[根桥的编号]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2115346508}

[[ExtPathCost]{lang="EN-US"}]{#struct_0_x1139_12555_x781245912}

[[外部路径开销。设备可自动计算端口的缺省路径开销，用户也可使用命令]{style="font-family:宋体"}**[stp cost]{lang="EN-US"}**]{#struct_0_x1139_12555_x962229425}[来配置端口的路径开销]{style="font-family:宋体"}

[[IntPathCost]{lang="EN-US"}]{#struct_0_x1139_12555_773124195}

[[内部路径开销。设备可自动计算端口的缺省路径开销，用户也可使用命令]{style="font-family:宋体"}**[stp cost]{lang="EN-US"}**]{#struct_0_x1139_12555_x1755990206}[来配置端口的路径开销]{style="font-family:宋体"}

[[Root Port]{lang="EN-US"}]{#struct_0_x1139_12555_x516473471}

[[根端口名称（若当前设备的某个端口是]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x2053868334}[的根端口则显示，否则不显示）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1772438143 .myid}
[]{#_Toc404784584}[]{#struct_0_x1139_12555_1813181746}

**生成树 \-- 生成树配置命令 \-- display stp tc**

------------------------------------------------------------------------

[**[display stp tc]{lang="EN-US"}**]{#struct_0_x1139_12555_1932955759}[命令用来显示生成树所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2073637646}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1139_12555_1723680866}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** ]{lang="EN-US"}]{#struct_0_x1139_12555_x1756448957}*[vlan-id-list ]{lang="EN-US"}*[\] **tc**]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_2081581383}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** ]{lang="EN-US"}]{#struct_0_x1139_12555_x747118681}*[vlan-id-list]{lang="EN-US"}*[ ]{lang="EN-US"}[\] **tc** \[ **slot** *slot-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1139_12555_x957958758}[模式：]{style="font-family:宋体"}

[**[display stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** ]{lang="EN-US"}]{#struct_0_x1139_12555_x1067608125}*[vlan-id-list]{lang="EN-US"}*[ ]{lang="EN-US"}[\] **tc** \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_263566721}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2131973367}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1285203240}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1756514493}

[[network-operator]{lang="EN-US"}]{#struct_0_x1139_12555_x1412709177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_221250147}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1139_12555_1681818669}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1624560023}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x707644610}[：显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x1906468695}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_1573831696}[：显示指定单板上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示所有单板上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_x1880899732}[：显示指定成员设备上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定该参数，将显示所有成员设备上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_1172698055}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定该参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_1334105217}[：显示指定成员设备的指定单板上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定该参数，将显示所有单板上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1139_12555_x1556185300}[：显示指定单板上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定该参数，将显示所有单板上所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1756580029}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{style="font-family:宋体"}]{#struct_0_x1139_12555_x413583214}[STP/RSTP]{lang="EN-US"}[模式下，显示信息按照端口名称的顺序排列。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[PVST]{lang="EN-US"}]{#struct_0_x1139_12555_x1906403159}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1906599767}[VLAN]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，显示信息按照]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1906534231}[VLAN]{lang="EN-US"}[，则显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，显示信息按照]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_1521906862}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_1063668104}[MSTI]{lang="EN-US"}[，则显示所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_x1139_12555_1246211762}[MSTI]{lang="EN-US"}[，则显示指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数，显示信息按照]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号的顺序排列，各]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[内部再按照端口名称的顺序排列。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1467922613}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1139_12555_x79021092}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x816241280}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 0 tc]{lang="EN-US"}]{#struct_0_x1139_12555_x1756645565}

[ MST ID      Port                       Receive      Send]{lang="EN-US"}

[ 0           GigabitEthernet1/0/1       6            4]{lang="EN-US"}

[ 0           GigabitEthernet1/0/2       0            2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1906141016}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[\<Sysname\> display stp vlan 2 tc]{lang="EN-US"}]{#struct_0_x1139_12555_x1906337624}

[ VLAN ID     Port                       Receive      Send]{lang="EN-US"}

[ 2           GigabitEthernet1/0/1       6            4]{lang="EN-US"}

[ 2           GigabitEthernet1/0/2       0            2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式应用]{style="font-family:宋体"}]{#struct_0_x1139_12555_x549093363}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_168336332}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 0 tc slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_1487274743}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 TC or TCN count \-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ MST ID      Port                       Receive      Send]{lang="EN-US"}

[ 0           GigabitEthernet1/0/1       6            4]{lang="EN-US"}

[ 0           GigabitEthernet1/0/2       0            2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1906403160}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[\<Sysname\> display stp vlan 2 tc slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_x1906599768}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 TC or TCN count \-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ VLAN ID     Port                       Receive      Send]{lang="EN-US"}

[ 2           GigabitEthernet1/0/1       6            4]{lang="EN-US"}

[ 2           GigabitEthernet1/0/2       0            2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2142156252}[IRF]{lang="EN-US"}[设备应用]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x714551695}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 0 tc slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_x1756711101}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 TC or TCN count \-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ MST ID      Port                       Receive      Send]{lang="EN-US"}

[ 0           GigabitEthernet1/0/1       6            4]{lang="EN-US"}

[ 0           GigabitEthernet1/0/2       0            2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x340122614}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[\<Sysname\> display stp vlan 2 tc slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_x340057078}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 TC or TCN count \-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[VLAN ID     Port                       Receive      Send]{lang="EN-US"}

[ 2           GigabitEthernet1/0/1      6            4]{lang="EN-US"}

[ 2           GigabitEthernet1/0/2      0            2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1902191732}[IRF]{lang="EN-US"}[模式应用]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1808048080}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[\<Sysname\> display stp instance 0 tc chassis 1 slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_1701103802}

[ \-\-\-\-\-\-\-\-- STP chassis 1 slot 1 TC or TCN count \-\-\-\-\-\-\--]{lang="EN-US"}

[ MST ID      Port                       Receive      Send]{lang="EN-US"}

[ 0           GigabitEthernet1/1/0/1     6            4]{lang="EN-US"}

[ 0           GigabitEthernet1/1/0/2     0            2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_602021635}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中所有端口收发的]{style="font-family:宋体"}[TC]{lang="EN-US"}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[\<Sysname\> display stp vlan 2 tc chassis 1 slot 1]{lang="EN-US"}]{#struct_0_x1139_12555_602218243}

[ \-\-\-\-\-\-\-\-- STP chassis 1 slot 1 TC or TCN count \-\-\-\-\-\-\--]{lang="EN-US"}

[ VLAN ID     Port                       Receive      Send]{lang="EN-US"}

[ 2           GigabitEthernet1/1/0/1     6            4]{lang="EN-US"}

[ 2           GigabitEthernet1/1/0/2     0            2]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display stp tc]{lang="EN-US"}]{#struct_0_x1139_12555_x362565841}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1283358485}[[字段]{style="font-family:黑体"}]{#struct_0_x1139_12555_2052352048}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1139_12555_x712364365}

[[MST ID]{lang="EN-US"}]{#struct_0_x1139_12555_x1756776637}

[[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_346251591}[的编号]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x1139_12555_x339598326}

[[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_x340122615}[的编号]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x1139_12555_157717175}

[[端口名称]{style="font-family:宋体"}]{#struct_0_x1139_12555_x908279729}

[[Receive]{lang="EN-US"}]{#struct_0_x1139_12555_1122634289}

[[端口收到的]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_x1139_12555_1579311418}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[Send]{lang="EN-US"}]{#struct_0_x1139_12555_x1756842173}

[[端口发出的]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_x1139_12555_x1591175469}[或]{style="font-family:宋体"}[TCN]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-417074414 .myid}
[]{#_Toc404784585}[]{#struct_0_x1139_12555_x519969997}

**生成树 \-- 生成树配置命令 \-- instance**

------------------------------------------------------------------------

[**[instance]{lang="EN-US"}**]{#struct_0_x1139_12555_x720370875}[命令用来将指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射到指定的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[上。]{style="font-family:宋体"}

[**[undo instance]{lang="EN-US"}**]{#struct_0_x1139_12555_1282277647}[命令用来删除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[之间的映射关系，这些]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[将重新映射到]{style="font-family:宋体"}[CIST]{lang="EN-US"}[（即]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[）上。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1342297481}

[**[instance]{lang="EN-US"}**[ *instance-id* **vlan** *vlan-id-list*]{lang="EN-US"}]{#struct_0_x1139_12555_1554316553}

[**[undo instance]{lang="EN-US"}**[ *instance-id* \[ **vlan** *vlan-id-list* \]]{lang="EN-US"}]{#struct_0_x1139_12555_x157193836}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1756907709}

[[所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_1361391291}[都映射到]{style="font-family:宋体"}[CIST]{lang="EN-US"}[（即]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[）上。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2128660611}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x787404894}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1777133730}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x99453240}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x553829168}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_337847111}

[*[instance-id]{lang="EN-US"}*]{#struct_0_x1139_12555_x1755924669}[：表示]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。在执行]{style="font-family:宋体"}**[undo instance]{lang="EN-US"}**[命令时，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_1213349457}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_50738562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}**[undo instance]{lang="EN-US"}**]{#struct_0_x1139_12555_x628236192}[命令中没有指定]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[，则与指定]{lang="EN-US" style="font-family:宋体"}[MSTI]{lang="EN-US"}[有映射关系的所有]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[都将重新映射到]{lang="EN-US" style="font-family:宋体"}[CIST]{lang="EN-US"}[上。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能将同一个]{style="font-family:宋体"}]{#struct_0_x1139_12555_1323702136}[VLAN]{lang="EN-US"}[映射到不同的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[上。如果将一个已映射到某]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[重新映射到另一个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[时，原先的映射关系将被取消。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最多只能对]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1303962440}[65]{lang="EN-US"}[个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令后，必须执行]{lang="EN-US" style="font-family:宋体"}**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x499997295}[命令才能激活本配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置全局摘要侦听功能后，如果要修改]{style="font-family:宋体"}]{#struct_0_x1139_12555_x285041874}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[间的映射关系]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[或]{style="font-family:宋体"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo stp region-configuration]{lang="EN-US"}**[命令取消当前域配置，]{lang="EN-US" style="font-family:宋体"}[均可能因与邻接设备的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[映射关系不一致而导致环路或流量中断，因此请谨慎操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_81246366}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1755990205}[将]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[映射到]{style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1049610470}

[\[Sysname\] stp region-configuration]{lang="EN-US"}

[\[Sysname-mst-region\] instance 1 vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_308626317}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1926472757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[check region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1926538293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1889207792}
:::

::: {#-600780815 .myid}
[]{#_Toc404784586}[]{#struct_0_x1139_12555_688558825}[]{#_Toc139807249}

**生成树 \-- 生成树配置命令 \-- region-name**

------------------------------------------------------------------------

[**[region-name]{lang="EN-US"}**]{#struct_0_x1139_12555_x424627125}[命令用来配置]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的域名。]{style="font-family:宋体"}

[**[undo region-name]{lang="EN-US"}**]{#struct_0_x1139_12555_x190365013}[命令用来恢复缺省情况。]{style="font-family:宋体"}[]{#_Toc139807258}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1599437930}[]{#_Toc139807250}

[**[region-name]{lang="EN-US"}**[ *name*]{lang="EN-US"}]{#struct_0_x1139_12555_1017500631}[]{#_Toc139807251}

[**[undo region-name]{lang="EN-US"}**]{#struct_0_x1139_12555_1198785665}[]{#_Toc139807252}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1357859293}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x1951037618}[域的域名为设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2057193889}[]{#_Toc139807253}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_1368811641}[域视图]{style="font-family:宋体"}[]{#_Toc139807254}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190430549}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_379332137}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1730815189}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1651365821}[]{#_Toc139807255}

[*[name]{lang="EN-US"}*]{#struct_0_x1139_12555_x1726292438}[：表示]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}[]{#_Toc139807256}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1979799387}[]{#_Toc139807257}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MST]{lang="EN-US"}]{#struct_0_x1139_12555_1655839531}[域名用来与]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表和]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[的修订级别来共同确定设备所属的]{style="font-family:宋体"}[MST]{lang="EN-US"}[域。]{style="font-family:宋体"}[]{#_Toc139807260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令后，必须执行]{lang="EN-US" style="font-family:宋体"}**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_1435915336}[命令才能激活本配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1207186196}[]{#_Toc139807262}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x190496085}[配置]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的域名为]{style="font-family:宋体"}[hello]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc139807263}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x52687005}[]{#_Toc139807264}

[\[Sysname\] stp region-configuration[]{#_Toc139807265}]{lang="EN-US"}

[\[Sysname-mst-region\] region-name hello]{lang="EN-US"}[]{#_Toc139807266}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x512032296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x190561621}[]{#_Toc139807261}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[check region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_1114505268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_298148429}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[instance]{lang="EN-US"}**]{#struct_0_x1139_12555_1511865818}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[revision-level]{lang="EN-US"}**]{#struct_0_x1139_12555_x872914450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vlan-mapping modulo]{lang="EN-US"}**]{#struct_0_x1139_12555_x2052926131}
:::

::: {#2065411577 .myid}
[]{#_Toc404784587}[]{#struct_0_x1139_12555_x777211543}

**生成树 \-- 生成树配置命令 \-- reset stp**

------------------------------------------------------------------------

[**[reset stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x682914499}[命令用来清除生成树的统计信息，包括端口收发的]{style="font-family:宋体"}[TCN BPDU]{lang="EN-US"}[、]{style="font-family:宋体"}[CONFIG BPDU]{lang="EN-US"}[、]{style="font-family:宋体"}[RST BPDU]{lang="EN-US"}[和]{style="font-family:宋体"}[MST BPDU]{lang="EN-US"}[的数量。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x887154751}

[**[reset stp]{lang="EN-US"}**[ \[ **interface** *interface-list* \]]{lang="EN-US"}]{#struct_0_x1139_12555_x1365698864}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1977206801}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1787563797}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x334161083}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x2065404563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x190627157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x415196411}

[**[interface]{lang="EN-US"}**[ *interface-list*]{lang="EN-US"}]{#struct_0_x1139_12555_x594166959}[：清除指定端口上的生成树统计信息。]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[为端口列表，表示多个端口，表示方式为]{style="font-family:宋体"}*[interface-list]{lang="EN-US"}*[ = { *interface-type interface-number* \[ **to** *interface-type interface-number* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[为端口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为端口编号。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，将清除所有端口上的生成树统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1042681554}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x851462102}[清除端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[到]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[上的生成树统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset stp interface gigabitethernet 1/0/1 to gigabitethernet 1/0/3]{lang="EN-US"}]{#struct_0_x1139_12555_x2038888109}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1169671547}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_197642273}
:::

::: {#-427793638 .myid}
[]{#_Toc404784588}[]{#struct_0_x1139_12555_x190692693}

**生成树 \-- 生成树配置命令 \-- revision-level**

------------------------------------------------------------------------

[**[revision-level]{lang="EN-US"}**]{#struct_0_x1139_12555_769539384}[命令用来配置]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[的修订级别。]{style="font-family:宋体"}

[**[undo revision-level]{lang="EN-US"}**]{#struct_0_x1139_12555_x1235230472}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_509280937}

[**[revision-level]{lang="EN-US"}**[ *level*]{lang="EN-US"}]{#struct_0_x1139_12555_x1081725749}

[**[undo revision-level]{lang="EN-US"}**]{#struct_0_x1139_12555_1216659026}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x964610786}

[[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_x2142756466}[的修订级别为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1606787291}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x190758229}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1945140878}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1219057443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_459700676}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2078813405}

[*[level]{lang="EN-US"}*]{#struct_0_x1139_12555_x1020027879}[：表示]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[的修订级别，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2090418706}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_1226248389}[的修订级别用来与]{style="font-family:宋体"}[MST]{lang="EN-US"}[域名和]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表来共同确定设备所属的]{style="font-family:宋体"}[MST]{lang="EN-US"}[域。修订级别可以在域名和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表相同的情况下，来区分不同的域。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令后，必须执行]{lang="EN-US" style="font-family:宋体"}**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1393108750}[命令才能激活本配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190823765}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_407029974}[配置设备的]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[修订级别为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x2000222505}

[\[Sysname\] stp region-configuration]{lang="EN-US"}

[\[Sysname-mst-region\] revision-level 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x162796667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1926210614}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[check region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_1876698355}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1926276150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[instance]{lang="EN-US"}**]{#struct_0_x1139_12555_1748294919}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[region-name]{lang="EN-US"}**]{#struct_0_x1139_12555_1206088108}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vlan-mapping modulo]{lang="EN-US"}**]{#struct_0_x1139_12555_x1501706046}
:::

::: {#1866876987 .myid}
[]{#_Toc404784589}[]{#struct_0_x1139_12555_x1556119764}[]{#_Toc396825284}[]{#_Toc385773967}[]{#_Toc385773571}[]{#_Toc353116135}

**生成树 \-- 生成树配置命令 \-- snmp-agent trap enable stp**

------------------------------------------------------------------------

[**[snmp-agent trap enable stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x502846807}[命令用来开启生成树的告警功能。]{style="font-family:
宋体"}

[**[undo snmp-agent trap enable stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x1130636517}[命令用来关闭生成树的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1484532143}

[**[snmp-agent trap enable stp]{lang="EN-US"}**[ \[ **new-root** \| **tc** \]]{lang="EN-US"}]{#struct_0_x1139_12555_x866677355}

[**[undo snmp-agent trap enable stp]{lang="EN-US"}**[ \[ **new-root** \| **tc** \]]{lang="EN-US"}]{#struct_0_x1139_12555_249975238}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2101240527}

[[生成树的]{style="font-family:宋体"}[new-root]{lang="EN-US"}]{#struct_0_x1139_12555_x1534097283}[告警功能处于关闭状态。在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，生成树的]{style="font-family:宋体"}[TC]{lang="EN-US"}[告警功能在]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[中处于开启状态，在其他]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[中处于关闭状态；在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，生成树的]{style="font-family:宋体"}[TC]{lang="EN-US"}[告警功能在所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_228764033}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1959404291}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1877727687}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_41028966}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_93387960}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_301079823}

[**[new-root]{lang="EN-US"}**]{#struct_0_x1139_12555_714121629}[：在非]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，当设备在任意实例中由非根桥被选举为根桥后，打印]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[tc]{lang="EN-US"}**]{#struct_0_x1139_12555_1194786072}[：在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，当端口检测或接收到]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文后，打印日志信息并打印]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息。该参数只能控制]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下的]{style="font-family:宋体"}[TC]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_488915337}

[[执行该命令时，如果未指定任何参数，表示开启或关闭生成树的]{style="font-family:宋体"}[new-root]{lang="EN-US"}]{#struct_0_x1139_12555_1109360}[和]{style="font-family:宋体"}[TC]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_647720563}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x340036336}[配置当设备在任意实例中由非根桥被选举为根桥后，打印]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1289442505}

[[\[Sysname\] snmp-agent trap enable stp new-root]{lang="EN-US"}]{#struct_0_x1139_12555_x223638088}
:::

::: {#-519547547 .myid}
[]{#_Toc404784590}[]{#struct_0_x1139_12555_1748551323}[]{#_Toc201632241}[]{#_Toc201632243}[]{#_Toc201632244}[]{#_Toc201632245}[]{#_Toc201632246}[]{#_Toc201632247}[]{#_Toc201632248}[]{#_Toc201632249}[]{#_Toc201632250}[]{#_Toc201632251}[]{#_Toc201632252}[]{#_Toc201632253}[]{#_Toc201632254}[]{#_Toc201632255}[]{#_Toc201632256}[]{#_Toc201632257}[]{#_Toc201632258}[]{#_Toc201632259}[]{#_Toc201632260}[]{#_Toc201632261}[]{#_Toc201632262}[]{#_Toc201632265}[]{#_Toc201632267}[]{#_Toc201632268}

**生成树 \-- 生成树配置命令 \-- stp bpdu-protection**

------------------------------------------------------------------------

[**[stp bpdu-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_30455759}[命令用来开启]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[保护功能。]{style="font-family:宋体"}

[**[undo stp bpdu-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_636933643}[命令用来关闭]{style="font-family:
宋体"}[BPDU]{lang="EN-US"}[保护功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1140395705}

[**[stp bpdu-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_624410077}

[**[undo stp]{lang="EN-US"}**[ **bpdu-protection**]{lang="EN-US"}]{#struct_0_x1139_12555_2000561649}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x189906261}

[[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_1234644607}[保护功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1083096467}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_244630978}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1680429101}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_2001159856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1784033398}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1123615439}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1175246282}[开启]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x190365012}

[\[Sysname\] stp bpdu-protection]{lang="EN-US"}
:::

::: {#-1773151289 .myid}
[]{#_Toc404784591}[]{#struct_0_x1139_12555_x1599503466}

**生成树 \-- 生成树配置命令 \-- stp bridge-diameter**

------------------------------------------------------------------------

[**[stp bridge-diameter]{lang="EN-US"}**]{#struct_0_x1139_12555_x1635013071}[命令用来配置交换网络的网络直径，即交换网络中任意两台终端设备间的最大设备数。]{style="font-family:宋体"}

[**[undo stp bridge-diameter]{lang="EN-US"}**]{#struct_0_x1139_12555_x667652628}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x211416391}

[**[stp]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **vlan** *vlan-id-list* \] **bridge-diameter** *diameter*]{lang="EN-US"}]{#struct_0_x1139_12555_604290010}

[**[undo stp]{lang="EN-US"}**[ \[ **vlan** *vlan-id-list* \] **bridge-diameter**]{lang="EN-US"}]{#struct_0_x1139_12555_1493182200}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1784647848}

[[交换网络的网络直径为]{style="font-family:宋体"}[7]{lang="EN-US"}]{#struct_0_x1139_12555_x190430548}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_379397673}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1380239274}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1809102377}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x983614824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x150202474}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1943140182}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x340319220}[：表示配置]{style="font-family:宋体"}[PVST]{lang="EN-US"}[交换网络中指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的网络直径。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，表示配置]{style="font-family:宋体"}[STP/RSTP/MSTP]{lang="EN-US"}[交换网络的网络直径。]{style="font-family:宋体"}

[*[diameter]{lang="EN-US"}*]{#struct_0_x1139_12555_x300824372}[：表示交换网络的网络直径，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x915487665}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[选用合适的]{style="font-family:宋体"}]{#struct_0_x1139_12555_x190496084}[Hello Time]{lang="EN-US"}[、]{style="font-family:宋体"}[Forward Delay]{lang="EN-US"}[和]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[时间参数，可以加快生成树收敛速度。上述三个时间参数的取值与网络规模有关，因此可以通过调整网络直径使生成树协议自动调整这三个时间参数的值。当网络直径为缺省值]{style="font-family:宋体"}[7]{lang="EN-US"}[时，这三个时间参数也分别取其各自的缺省值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1139_12555_x52621469}[STP/RSTP/MSTP]{lang="EN-US"}[模式下，每个]{style="font-family:宋体"}[MST]{lang="EN-US"}[域将被视为一台设备，且网络直径配置只对]{style="font-family:宋体"}[CIST]{lang="EN-US"}[有效（即只能在总根上生效），而对]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1139_12555_x339598324}[PVST]{lang="EN-US"}[模式下，网络直径的配置只能在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的根桥上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1703596478}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1510582600}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置交换网络的网络直径为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1211612588}

[\[Sysname\] stp bridge-diameter 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x340057077}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置交换网络中]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的网络直径为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x340253685}

[\[Sysname\] stp vlan 2 bridge-diameter 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1426070453}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer forward-delay]{lang="EN-US"}**]{#struct_0_x1139_12555_456995811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer hello]{lang="EN-US"}**]{#struct_0_x1139_12555_1901172904}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer max-age]{lang="EN-US"}**]{#struct_0_x1139_12555_x190561620}
:::

::: {#2055862283 .myid}
[]{#_Toc404784592}[]{#struct_0_x1139_12555_x777277079}[]{#_Toc275870285}[]{#_Toc287952189}[]{#_Toc287960119}[]{#_Toc275870288}[]{#_Toc287952192}[]{#_Toc287960122}

**生成树 \-- 生成树配置命令 \-- stp compliance**

------------------------------------------------------------------------

[**[stp compliance]{lang="EN-US"}**]{#struct_0_x1139_12555_1602570462}[命令用来配置端口收发的]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[报文格式。]{style="font-family:宋体"}

[**[undo stp compliance]{lang="EN-US"}**]{#struct_0_x1139_12555_x1459477692}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1236343048}

[**[stp compliance]{lang="EN-US"}**[ { **auto** \| **dot1s** \| **legacy** }]{lang="EN-US"}]{#struct_0_x1139_12555_x437417515}

[**[undo stp compliance]{lang="EN-US"}**]{#struct_0_x1139_12555_x923695935}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1359455174}

[[端口会自动识别收到的]{style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_x1068835453}[报文格式并根据识别结果确定发送的报文格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190627156}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x415261947}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x504668836}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1665427846}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_486052749}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_259485472}

[**[auto]{lang="EN-US"}**]{#struct_0_x1139_12555_x186966739}[：表示端口会自动识别收到的]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[报文格式并根据识别结果确定发送的报文格式。]{style="font-family:宋体"}

[**[dot1s]{lang="EN-US"}**]{#struct_0_x1139_12555_x1343934844}[：表示端口只发送标准格式（符合]{style="font-family:宋体"}[802.1s]{lang="EN-US"}[协议）的]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[legacy]{lang="EN-US"}**]{#struct_0_x1139_12555_x190692692}[：表示端口只发送与非标准格式兼容的]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_769604920}

[[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_990586291}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_322787651}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_640368831}[配置端口只发送标准格式的]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_2130618904}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp compliance dot1s]{lang="EN-US"}
:::

::: {#79107378 .myid}
[]{#_Toc404784593}[]{#struct_0_x1139_12555_1425845684}

**生成树 \-- 生成树配置命令 \-- stp config-digest-snooping**

------------------------------------------------------------------------

[**[stp config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_1765528847}[命令用来在端口上开启摘要侦听功能。]{style="font-family:
宋体"}

[**[undo stp config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_x190758228}[命令用来在端口上关闭摘要侦听功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1945075342}

[**[stp config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_x1964565061}

[**[undo stp config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_713400940}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x809161774}

[[端口上的摘要侦听功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1139_12555_2132174197}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_536098260}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x1749603593}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2034119043}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x190823764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_406964438}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1150489075}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当全局和端口上都开启了摘要侦听功能后，该功能才能生效。开启摘要侦听功能时，建议先在所有与第三方厂商设备相连的端口上开启该功能，再全局开启该功能，以一次性让所有端口的配置生效，从而减少对网络的冲击。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1889424583}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x387298974}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2056232809}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1701761256}[先在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启摘要侦听功能，再全局开启摘要侦听功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x189840724}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp config-digest-snooping]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] stp global config-digest-snooping]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1254507888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_1429468217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp global config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_1815402547}
:::

::: {#-807632449 .myid}
[]{#_Toc404784594}[]{#struct_0_x1139_12555_x163177625}[]{#_Toc287952196}[]{#_Toc287960126}

**生成树 \-- 生成树配置命令 \-- stp cost**

------------------------------------------------------------------------

[**[stp cost]{lang="EN-US"}**]{#struct_0_x1139_12555_1743212796}[命令用来配置端口的路径开销。]{style="font-family:宋体"}

[**[undo stp cost]{lang="EN-US"}**]{#struct_0_x1139_12555_473324250}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_467003791}

[**[stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **cost** *cost*]{lang="EN-US"}]{#struct_0_x1139_12555_1055483657}

[**[undo stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **cost**]{lang="EN-US"}]{#struct_0_x1139_12555_x189906260}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1234579071}

[[自动按照相应的标准计算各生成树上的路径开销。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1509931856}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2125916108}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x685348179}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_213295049}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x244447416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x720909754}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1484252374}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x190365015}[：表示配置端口在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的路径开销。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，表示配置端口在]{style="font-family:宋体"}[MSTP CIST]{lang="EN-US"}[或]{style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[的路径开销。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x340057074}[：表示配置端口在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的路径开销。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[cost]{lang="EN-US"}*]{#struct_0_x1139_12555_x1599306858}[：表示端口的路径开销值。取值范围由计算端口缺省路径开销所采用的计算方法来决定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x1139_12555_1555898415}[IEEE 802.1D-1998]{lang="EN-US"}[标准来计算时，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x1139_12555_2117191905}[IEEE 802.1t]{lang="EN-US"}[标准来计算时，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用私有标准来计算时，取值范围为]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1425570904}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x372709290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口的路径开销是生成树计算的重要依据，可以影响端口的角色选择。在不同生成树上为同一端口配置不同的路径开销值，可以使不同]{style="font-family:宋体"}]{#struct_0_x1139_12555_1418979640}[VLAN]{lang="EN-US"}[的流量沿不同的物理链路转发，从而实现按]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的负载分担的功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当端口的路径开销值改变时，系统将重新计算端口的角色并进行状态迁移。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1642908609}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_189575322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{lang="EN-US" style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_x340253682}[和]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则表示配置端口在]{lang="EN-US" style="font-family:宋体"}[MSTP CIST]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[的路径开销。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190430551}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_379856424}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[在]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[上的路径开销值为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1708335871}

[\[Sysname\] interface gigabitethernet 1/0/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] stp instance 2 cost 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x340384754}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[上的路径开销值为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x340319218}

[\[Sysname\] interface gigabitethernet 1/0/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] stp vlan 2 cost 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1798870252}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x1510639533}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp pathcost-standard]{lang="EN-US"}**]{#struct_0_x1139_12555_x1068534609}
:::

::: {#-2036448749 .myid}
[]{#_Toc404784595}[]{#struct_0_x1139_12555_x1138859342}[]{#_Toc275870292}[]{#_Toc287952198}[]{#_Toc287960128}[]{#_Toc275870296}[]{#_Toc287952202}[]{#_Toc287960132}

**生成树 \-- 生成树配置命令 \-- stp edged-port**

------------------------------------------------------------------------

[**[stp edged-port]{lang="EN-US"}**]{#struct_0_x1139_12555_531484570}[命令用来配置当前端口为边缘端口。]{style="font-family:宋体"}

[**[undo stp edged-port]{lang="EN-US"}**]{#struct_0_x1139_12555_x190496087}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x52555933}

[**[stp edged-port]{lang="EN-US"}**]{#struct_0_x1139_12555_1128667820}

[**[undo stp]{lang="EN-US"}***[ ]{lang="EN-US"}***[edged-port]{lang="EN-US"}**]{#struct_0_x1139_12555_x839991551}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1643540058}

[[端口为非边缘端口。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x478395603}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x541958161}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_1493415560}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190561623}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x777080471}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_113574297}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1131020809}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当端口直接与用户终端相连，而没有连接到其它设备或共享网段上，则该端口被认为是边缘端口。网络拓扑变化时，边缘端口不会产生临时环路。因此，如果将某个端口配置为边缘端口，则该端口可以快速迁移到转发状态。对于直接与用户终端相连的端口，为能使其快速迁移到转发状态，请将其设置为边缘端口。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x878202848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于边缘端口不与其它设备相连，所以不会收到其它设备发过来的]{style="font-family:宋体"}]{#struct_0_x1139_12555_206105359}[BPDU]{lang="EN-US"}[。在设备没有开启]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[保护功能时，如果端口收到]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[，即使用户设置该端口为边缘端口，该端口的实际运行状态也是非边缘端口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个端口上，不允许同时配置边缘端口和环路保护功能。]{style="font-family:宋体"}]{#struct_0_x1139_12555_170304789}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2076081741}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_696567780}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x190627159}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为边缘端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x415589627}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp edged-port]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_542900921}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp bpdu-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_241515598}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp loop-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_1823954460}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp root-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x843751345}
:::

::: {#292469485 .myid}
[]{#_Toc138217690}[]{#_Toc404784596}[]{#struct_0_x1139_12555_443057672}

**生成树 \-- 生成树配置命令 \-- stp enable**

------------------------------------------------------------------------

[**[stp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1139_12555_222893831}[命令用来在端口上开启生成树协议。]{style="font-family:宋体"}

[**[undo stp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1139_12555_x190692695}[命令用来在端口上关闭生成树协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_769670456}

[**[stp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1139_12555_523702475}

[**[undo stp enable]{lang="EN-US"}**]{#struct_0_x1139_12555_405680550}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x957102177}

[[端口上的生成树协议处于开启状态。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1434384181}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1606860453}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x716625512}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x675532624}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x190758231}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1945665165}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1237313877}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当生成树协议开启后，设备会根据用户配置的生成树工作模式来决定运行在]{style="font-family:宋体"}]{#struct_0_x1139_12555_1882229208}[STP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式还是]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当生成树协议开启后，系统根据收到的]{style="font-family:宋体"}]{#struct_0_x1139_12555_1228228471}[BPDU]{lang="EN-US"}[动态维护相应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的生成树状态；当生成树协议关闭后，系统将不再维护该状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_26728699}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1783434094}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_442780002}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上关闭生成树协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x190823767}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo stp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_407161046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp global enable]{lang="EN-US"}**]{#struct_0_x1139_12555_x1926472751}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp mode]{lang="EN-US"}**]{#struct_0_x1139_12555_x70115128}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp vlan enable]{lang="EN-US"}**]{#struct_0_x1139_12555_x340057075}
:::

::: {#-1153698614 .myid}
[]{#_Toc404784597}[]{#struct_0_x1139_12555_1437165005}

**生成树 \-- 生成树配置命令 \-- stp global config-digest-snooping**

------------------------------------------------------------------------

[**[stp global config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_1023069685}[命令用来全局开启摘要侦听功能。]{style="font-family:宋体"}

[**[undo stp global config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_x616805045}[命令用来全局关闭摘要侦听功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_730018029}

[**[stp global config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_x1300755890}

[**[undo stp global config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_x189840727}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1254442352}

[[摘要侦听功能处于全局关闭状态。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1371683666}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1622300326}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1153911994}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x493852726}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_966409589}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x2073184157}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x189906263}

[[只有当全局和端口上都开启了摘要侦听功能后，该功能才能生效。开启摘要侦听功能时，建议先在所有与第三方厂商设备相连的端口上开启该功能，再全局开启该功能，以一次性让所有端口的配置生效，从而减少对网络的冲击。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1234513535}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1890416366}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x537247247}[先在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启摘要侦听功能，再全局开启摘要侦听功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1598063643}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp config-digest-snooping]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] stp global config-digest-snooping]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x806618401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_1880659580}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp config-digest-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_x2141370629}
:::

::: {#-984779656 .myid}
[]{#_Toc404784598}[]{#struct_0_x1139_12555_x190365014}

**生成树 \-- 生成树配置命令 \-- stp global enable**

------------------------------------------------------------------------

[**[stp]{lang="EN-US"}**[ **global enable**]{lang="EN-US"}]{#struct_0_x1139_12555_x1599372394}[命令用来全局开启生成树协议。]{style="font-family:宋体"}

[**[undo stp]{lang="EN-US"}**[ **global enable**]{lang="EN-US"}]{#struct_0_x1139_12555_x1050573235}[命令用来全局关闭生成树协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_523218638}

[**[stp]{lang="EN-US"}**[ **global** **enable**]{lang="EN-US"}]{#struct_0_x1139_12555_2138970826}

[**[undo stp global enable]{lang="EN-US"}**]{#struct_0_x1139_12555_x1108867249}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1852143763}

[[生成树协议的全局状态与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1139_12555_750364958}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190430550}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_379921960}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1387411061}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1671097223}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1391885327}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1367782776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当生成树协议开启后，设备会根据用户配置的生成树工作模式来决定运行在]{style="font-family:宋体"}]{#struct_0_x1139_12555_1797602472}[STP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式还是]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当生成树协议开启后，系统根据收到的]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1960218833}[BPDU]{lang="EN-US"}[动态维护相应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的生成树状态；当生成树协议关闭后，系统将不再维护该状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1472198191}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x190496086}[全局开启生成树协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x52490397}

[\[Sysname\] stp global enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x384606326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp enable]{lang="EN-US"}**]{#struct_0_x1139_12555_x1925620783}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp mode]{lang="EN-US"}**]{#struct_0_x1139_12555_1016344160}
:::

::: {#-876859954 .myid}
[]{#_Toc404784599}[]{#struct_0_x1139_12555_481417264}

**生成树 \-- 生成树配置命令 \-- stp global mcheck**

------------------------------------------------------------------------

[**[stp global mcheck]{lang="EN-US"}**]{#struct_0_x1139_12555_1001391751}[命令用来全局执行]{style="font-family:宋体"}[mCheck]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_227186853}

[**[stp global mcheck]{lang="EN-US"}**]{#struct_0_x1139_12555_1380745897}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190561622}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x777146007}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_46120349}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x549009615}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1012323875}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x535368764}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在运行]{style="font-family:宋体"}]{#struct_0_x1139_12555_477792035}[MSTP]{lang="EN-US"}[、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[或]{style="font-family:宋体"}[PVST]{lang="EN-US"}[的设备上，若某端口连接着运行]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议的设备，该端口收到]{style="font-family:宋体"}[STP]{lang="EN-US"}[报文后会自动迁移到]{style="font-family:宋体"}[STP]{lang="EN-US"}[模式；但当对端运行]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议的设备关机或撤走，而该端口又无法感知的情况下，该端口将无法自动迁移回原有模式，此时需要通过执行]{style="font-family:宋体"}[mCheck]{lang="EN-US"}[操作将其手工迁移回原有模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备会根据用户配置的生成树工作模式来决定运行在]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1867571529}[STP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式还是]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当生成树的工作模式为]{style="font-family:宋体"}]{#struct_0_x1139_12555_x190627158}[MSTP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式或]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式时执行本命令才有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x415655163}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x942526286}[全局执行]{style="font-family:宋体"}[mCheck]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_636442005}

[\[Sysname\] stp global mcheck]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1216858680}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp mcheck]{lang="EN-US"}**]{#struct_0_x1139_12555_x972637092}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp mode]{lang="EN-US"}**]{#struct_0_x1139_12555_1230719439}
:::

::::: {#-338880356 .myid}
[]{#_Toc404784600}[]{#struct_0_x1139_12555_1488602362}

**生成树 \-- 生成树配置命令 \-- stp ignored vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](生成树命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1139_12555_x190692694}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1139_12555_769735992}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[可同时开启]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1139_12555_585114964}[VLAN Ignore]{lang="EN-US"}[功能的]{style="font-family:KaiTi_GB2312"}[VLAN]{lang="EN-US"}[最大数量与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[stp ignored vlan]{lang="EN-US"}**]{#struct_0_x1139_12555_x1287175129}[命令用来在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内开启]{style="font-family:宋体"}[VLAN Ignore]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo stp ignored vlan]{lang="EN-US"}**]{#struct_0_x1139_12555_71099813}[命令用来在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内关闭]{style="font-family:宋体"}[VLAN Ignore]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2003208203}

[**[stp ignored vlan ]{lang="EN-US"}***[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_480033791}

[**[undo stp ignored vlan]{lang="EN-US"}**[ *vlan-id-list*]{lang="EN-US"}]{#struct_0_x1139_12555_357002392}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1339317987}

[[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_x190758230}[内的]{style="font-family:宋体"}[VLAN Ignore]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1945599629}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x171251869}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_507940156}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_556576754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x209947729}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1635233898}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_263545975}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2105882973}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x190823766}[在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[内开启]{style="font-family:宋体"}[VLAN Ignore]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_407095510}

[\[Sysname\] stp ignored vlan 1 to 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1837268108}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp ignored-vlan]{lang="EN-US"}**]{#struct_0_x1139_12555_565164597}
:::::

::: {#828854131 .myid}
[]{#_Toc404784601}[]{#struct_0_x1139_12555_x1556512980}[]{#_Toc396825297}[]{#_Toc385773965}[]{#_Toc385773569}[]{#_Toc361834728}[]{#_Toc361319128}[]{#_Toc361230552}[]{#_Toc361164421}[]{#_Toc360546793}[]{#_Toc359856175}[]{#_Toc359586004}[]{#_Toc359420149}[]{#_Toc357603287}[]{#_Toc357095105}[]{#_Toc356916779}[]{#_Toc356835031}

**生成树 \-- 生成树配置命令 \-- stp ignore-pvid-inconsistency**

------------------------------------------------------------------------

[**[stp ignore-pvid-inconsistency]{lang="EN-US"}**]{#struct_0_x1139_12555_x14788541}[命令用来关闭]{style="font-family:
宋体"}[PVST]{lang="EN-US"}[的]{style="font-family:宋体"}[PVID]{lang="EN-US"}[不一致保护功能。]{style="font-family:宋体"}

[**[undo stp ignore-pvid-inconsistency]{lang="EN-US"}**]{#struct_0_x1139_12555_x114379776}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1421542016}

[**[stp ignore-pvid-inconsistency]{lang="EN-US"}**]{#struct_0_x1139_12555_842341492}

[**[undo stp ignore-pvid-inconsistency]{lang="EN-US"}**]{#struct_0_x1139_12555_x1961067881}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_460235233}

[[PVST]{lang="EN-US"}]{#struct_0_x1139_12555_859973008}[的]{style="font-family:宋体"}[PVID]{lang="EN-US"}[不一致保护功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_706966058}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1959797507}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1624251079}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1360043887}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_625979797}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x513354171}

[[关闭]{style="font-family:宋体"}[PVST]{lang="EN-US"}]{#struct_0_x1139_12555_1304208576}[的]{style="font-family:宋体"}[PVID]{lang="EN-US"}[不一致保护功能后，如果链路两端端口]{style="font-family:宋体"}[PVID]{lang="EN-US"}[不一致，为了避免生成树的计算错误，需要注意：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[除了]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1197422331}[VLAN 1]{lang="EN-US"}[，本端所在设备不能创建对端]{style="font-family:宋体"}[PVID]{lang="EN-US"}[对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，同样，对端也不能创建本端]{style="font-family:宋体"}[PVID]{lang="EN-US"}[对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本端端口的链路类型是]{style="font-family:宋体"}]{#struct_0_x1139_12555_1539509241}[Hybrid]{lang="EN-US"}[时，建议本端所在设备不创建以]{style="font-family:宋体"}[Untagged]{lang="EN-US"}[方式允许通过的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，同样，对端也不创建本端]{style="font-family:宋体"}[Untagged]{lang="EN-US"}[方式允许通过的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议链路对端设备也关闭]{style="font-family:宋体"}]{#struct_0_x1139_12555_176112816}[PVST]{lang="EN-US"}[的]{style="font-family:宋体"}[PVID]{lang="EN-US"}[不一致保护功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置在]{lang="EN-US" style="font-family:宋体"}[PVST]{lang="EN-US"}]{#struct_0_x1139_12555_346205914}[工作模式下才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x986113271}

[]{#_Toc353442637}[]{#_Toc345072393}[]{#_Toc345072222}[]{#_Toc257636535}[]{#_Toc124742944}[]{#_Toc101584096}[]{#struct_0_x1139_12555_753192903}[]{#_Toc350937938}[]{#_display_rrpp_brief}[\# ]{lang="EN-US"}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，关闭]{style="font-family:宋体"}[PVST]{lang="EN-US"}[的]{style="font-family:宋体"}[PVID]{lang="EN-US"}[不一致保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1606538057}

[\[Sysname\] stp mode pvst]{lang="EN-US"}

[[\[Sysname\] stp ignore-pvid-inconsistency]{lang="EN-US"}]{#struct_0_x1139_12555_x393713566}
:::

::: {#1285943813 .myid}
[]{#_Toc404784602}[]{#struct_0_x1139_12555_222612942}

**生成树 \-- 生成树配置命令 \-- stp loop-protection**

------------------------------------------------------------------------

[**[stp loop-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x611172241}[命令用来开启端口的环路保护功能。]{style="font-family:宋体"}

[**[undo stp loop-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_344844511}[命令用来关闭端口的环路保护功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1541677562}

[**[stp loop-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x189840726}

[**[undo stp]{lang="EN-US"}**[ **loop-protection**]{lang="EN-US"}]{#struct_0_x1139_12555_1254376816}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x142055021}

[[端口的环路保护功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x663899493}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1943801453}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x21319458}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1894079362}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1210868803}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x561862411}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x189906262}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个端口上，不允许同时配置边缘端口和环路保护功能，或者同时配置根保护功能和环路保护功能。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1234447999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_2073409229}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1790250905}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x824157970}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启环路保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1718645707}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp loop-protection]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x375267814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp edged-port]{lang="EN-US"}**]{#struct_0_x1139_12555_113330403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp root-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x190365017}
:::

::: {#1178306194 .myid}
[]{#_Toc404784603}[]{#struct_0_x1139_12555_x1599175786}

**生成树 \-- 生成树配置命令 \-- stp max-hops**

------------------------------------------------------------------------

[**[stp max-hops]{lang="EN-US"}**]{#struct_0_x1139_12555_x1280402157}[命令用来配置]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的最大跳数，该跳数用来限制]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的规模。]{style="font-family:宋体"}

[**[undo stp max-hops]{lang="EN-US"}**]{#struct_0_x1139_12555_526089255}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1183328913}

[**[stp max-hops]{lang="EN-US"}**[ *hops*]{lang="EN-US"}]{#struct_0_x1139_12555_x1368927554}

[**[undo stp]{lang="EN-US"}**[ **max-hops**]{lang="EN-US"}]{#struct_0_x1139_12555_x769782432}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_570559129}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x1035630628}[域的最大跳数为]{style="font-family:宋体"}[20]{lang="EN-US"}[跳。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190430553}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_379725352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1548087833}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_542244049}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1604639913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1930914606}

[*[hops]{lang="EN-US"}*]{#struct_0_x1139_12555_x1716646657}[：表示最大跳数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x776610339}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1503001921}[配置]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的最大跳数为]{style="font-family:宋体"}[35]{lang="EN-US"}[跳。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x190496089}

[\[Sysname\] stp max-hops 35]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x52424861}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x43407986}
:::

::: {#-117249489 .myid}
[]{#_Toc404784604}[]{#struct_0_x1139_12555_1122570730}

**生成树 \-- 生成树配置命令 \-- stp mcheck**

------------------------------------------------------------------------

[**[stp mcheck]{lang="EN-US"}**]{#struct_0_x1139_12555_1175860028}[命令用来在端口上执行]{style="font-family:宋体"}[mCheck]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1016476673}

[**[stp mcheck]{lang="EN-US"}**]{#struct_0_x1139_12555_x438374956}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1158017077}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x190561625}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x776949399}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x295310985}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_619849164}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_605865485}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在运行]{style="font-family:宋体"}]{#struct_0_x1139_12555_789394423}[MSTP]{lang="EN-US"}[、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[或]{style="font-family:宋体"}[PVST]{lang="EN-US"}[的设备上，若某端口连接着运行]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议的设备，该端口收到]{style="font-family:宋体"}[STP]{lang="EN-US"}[报文后会自动迁移到]{style="font-family:宋体"}[STP]{lang="EN-US"}[模式；但当对端运行]{style="font-family:宋体"}[STP]{lang="EN-US"}[协议的设备关机或撤走，而该端口又无法感知的情况下，该端口将无法自动迁移回原有模式，此时需要通过执行]{style="font-family:宋体"}[mCheck]{lang="EN-US"}[操作将其手工迁移回原有模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当运行]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1792208257}[STP]{lang="EN-US"}[的设备]{style="font-family:宋体"}[A]{lang="EN-US"}[、未开启生成树协议的设备]{style="font-family:宋体"}[B]{lang="EN-US"}[和运行]{style="font-family:宋体"}[RSTP/MSTP/PVST]{lang="EN-US"}[的设备]{style="font-family:宋体"}[C]{lang="EN-US"}[三者顺次相连时，设备]{style="font-family:宋体"}[B]{lang="EN-US"}[将透传]{style="font-family:宋体"}[STP]{lang="EN-US"}[报文，设备]{style="font-family:宋体"}[C]{lang="EN-US"}[上连接设备]{style="font-family:宋体"}[B]{lang="EN-US"}[的端口将迁移到]{style="font-family:宋体"}[STP]{lang="EN-US"}[模式。在设备]{style="font-family:宋体"}[B]{lang="EN-US"}[上开启生成树协议后，若想使设备]{style="font-family:宋体"}[B]{lang="EN-US"}[与设备]{style="font-family:宋体"}[C]{lang="EN-US"}[之间运行]{style="font-family:宋体"}[RSTP/MSTP/PVST]{lang="EN-US"}[协议，除了要在设备]{style="font-family:宋体"}[B]{lang="EN-US"}[上配置生成树的工作模式为]{style="font-family:宋体"}[RSTP/MSTP/PVST]{lang="EN-US"}[外，还要在设备]{style="font-family:宋体"}[B]{lang="EN-US"}[与设备]{style="font-family:宋体"}[C]{lang="EN-US"}[相连的端口上都执行]{style="font-family:宋体"}[mCheck]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备会根据用户配置的生成树工作模式来决定运行在]{style="font-family:宋体"}]{#struct_0_x1139_12555_1418485265}[STP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式还是]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当生成树的工作模式为]{style="font-family:宋体"}]{#struct_0_x1139_12555_1064919664}[MSTP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式或]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式时执行本命令才有效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x190627161}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x415065340}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x562679930}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上执行]{style="font-family:宋体"}[mCheck]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1568665927}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp mcheck]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x140797298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp global mcheck]{lang="EN-US"}**]{#struct_0_x1139_12555_1810090611}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp mode]{lang="EN-US"}**]{#struct_0_x1139_12555_130680100}
:::

::: {#1766724212 .myid}
[]{#_Toc404784605}[]{#struct_0_x1139_12555_x1663854723}

**生成树 \-- 生成树配置命令 \-- stp mode**

------------------------------------------------------------------------

[**[stp mode]{lang="EN-US"}**]{#struct_0_x1139_12555_x190692697}[命令用来配置生成树的工作模式。]{style="font-family:宋体"}

[**[undo stp mode]{lang="EN-US"}**]{#struct_0_x1139_12555_769801528}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x795632385}

[**[stp mode]{lang="EN-US"}**[ { **mstp** \| **pvst** \| **rstp** \| **stp** }]{lang="EN-US"}]{#struct_0_x1139_12555_864697656}

[**[undo stp mode]{lang="EN-US"}**]{#struct_0_x1139_12555_x1108040983}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_700994314}

[[生成树工作模式为]{style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_855611054}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x694993220}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x871184198}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190758233}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1945534093}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_285247797}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x163583786}

[**[mstp]{lang="EN-US"}**]{#struct_0_x1139_12555_1367768830}[：配置生成树的工作模式为]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[pvst]{lang="EN-US"}**]{#struct_0_x1139_12555_863630285}[：配置生成树的工作模式为]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[rstp]{lang="EN-US"}**]{#struct_0_x1139_12555_1019850390}[：配置生成树的工作模式为]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[stp]{lang="EN-US"}**]{#struct_0_x1139_12555_976946212}[：配置生成树的工作模式为]{style="font-family:宋体"}[STP]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1036953049}

[[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_x190823769}[模式兼容]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式，]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式兼容]{style="font-family:宋体"}[STP]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[PVST]{lang="EN-US"}]{#struct_0_x1139_12555_863564749}[模式与其他模式的兼容性如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[Access]{lang="EN-US"}]{#struct_0_x1139_12555_863105996}[端口：]{lang="EN-US" style="font-family:宋体"}[PVST]{lang="EN-US"}[模式在任意]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[中都能与其]{lang="EN-US" style="font-family:宋体"}[他]{style="font-family:宋体"}[模式互相兼容。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[Trunk]{lang="EN-US"}]{#struct_0_x1139_12555_863040460}[端口或]{lang="EN-US" style="font-family:宋体"}[Hybrid]{lang="EN-US"}[端口：]{lang="EN-US" style="font-family:宋体"}[PVST]{lang="EN-US"}[模式仅在]{lang="EN-US" style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中能与其]{lang="EN-US" style="font-family:宋体"}[他]{style="font-family:宋体"}[模式互相兼容。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_406767830}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1398708919}[配置生成树的工作模式为]{style="font-family:宋体"}[STP]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x716983435}

[\[Sysname\] stp mode stp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_2108912945}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp enable]{lang="EN-US"}**]{#struct_0_x1139_12555_x1926603824}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp global enable]{lang="EN-US"}**]{#struct_0_x1139_12555_x1925620784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp global mcheck]{lang="EN-US"}**]{#struct_0_x1139_12555_x1738189360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp mcheck]{lang="EN-US"}**]{#struct_0_x1139_12555_x1117512128}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp vlan enable]{lang="EN-US"}**]{#struct_0_x1139_12555_863171532}
:::

::: {#-597502972 .myid}
[]{#_Toc404784606}[]{#struct_0_x1139_12555_x189840729}

**生成树 \-- 生成树配置命令 \-- stp no-agreement-check**

------------------------------------------------------------------------

[**[stp no-agreement-check]{lang="EN-US"}**]{#struct_0_x1139_12555_1255359856}[命令用来在端口上开启]{style="font-family:宋体"}[No Agreement Check]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo stp no-agreement-check]{lang="EN-US"}**]{#struct_0_x1139_12555_1752585582}[命令用来在端口上关闭]{style="font-family:
宋体"}[No Agreement Check]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_655547758}

[**[stp no-agreement-check]{lang="EN-US"}**]{#struct_0_x1139_12555_1824511586}

[**[undo stp no-agreement-check]{lang="EN-US"}**]{#struct_0_x1139_12555_1746708448}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_176678984}

[[No Agreement Check]{lang="EN-US"}]{#struct_0_x1139_12555_x369614039}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x189906265}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_1234906751}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1867830589}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x57521720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1872382179}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x102031777}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当且仅当在根端口上开启本功能才生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x99195626}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1624903610}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x741371768}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x190365016}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[No Agreement Check]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1599241322}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp no-agreement-check]{lang="EN-US"}
:::

::: {#-1112772932 .myid}
[]{#_Toc404784607}[]{#struct_0_x1139_12555_1186380764}[]{#_Toc164422859}[]{#_Toc164486265}[]{#_Toc164422861}[]{#_Toc164486267}[]{#_Toc164422862}[]{#_Toc164486268}[]{#_Toc164422863}[]{#_Toc164486269}[]{#_Toc164422864}[]{#_Toc164486270}[]{#_Toc164422865}[]{#_Toc164486271}[]{#_Toc164422866}[]{#_Toc164486272}[]{#_Toc164422867}[]{#_Toc164486273}[]{#_Toc164422868}[]{#_Toc164486274}[]{#_Toc164422869}[]{#_Toc164486275}[]{#_Toc164422870}[]{#_Toc164486276}[]{#_Toc164422871}[]{#_Toc164486277}[]{#_Toc164422872}[]{#_Toc164486278}[]{#_Toc164422873}[]{#_Toc164486279}[]{#_Toc164422875}[]{#_Toc164486281}

**生成树 \-- 生成树配置命令 \-- stp pathcost-standard**

------------------------------------------------------------------------

[**[stp pathcost-standard]{lang="EN-US"}**]{#struct_0_x1139_12555_1775990675}[命令用来配置缺省路径开销的计算标准。]{style="font-family:宋体"}

[**[undo stp pathcost-standard]{lang="EN-US"}**]{#struct_0_x1139_12555_1751266276}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1509124531}

[**[stp]{lang="EN-US"}**[ **pathcost-standard** { **dot1d-1998** \| **dot1t** \| **legacy** }]{lang="EN-US"}]{#struct_0_x1139_12555_371390007}

[**[undo]{lang="EN-US"}**[ **stp pathcost-standard**]{lang="EN-US"}]{#struct_0_x1139_12555_1169161108}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x190430552}

[[缺省路径开销的计算标准与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1139_12555_379790888}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1137093187}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2074310226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1814460855}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1335486002}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_263269217}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x496045546}

[**[dot1d-1998]{lang="EN-US"}**]{#struct_0_x1139_12555_x2050522354}[：表示按照]{style="font-family:宋体"}[IEEE 802.1D-1998]{lang="EN-US"}[标准来计算缺省路径开销。]{style="font-family:宋体"}

[**[dot1t]{lang="EN-US"}**]{#struct_0_x1139_12555_x190496088}[：表示按照]{style="font-family:宋体"}[IEEE 802.1t]{lang="EN-US"}[标准来计算缺省路径开销。]{style="font-family:宋体"}

[**[legacy]{lang="EN-US"}**]{#struct_0_x1139_12555_x52359325}[：表示按照私有标准来计算缺省路径开销。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1079484660}

[[改变缺省路径开销的计算标准，将使端口的路径开销值恢复为缺省值。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1706994843}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1739500362}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x983384854}[配置按照]{style="font-family:宋体"}[IEEE 802.1D-1998]{lang="EN-US"}[标准来计算缺省路径开销。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x134932742}

[\[Sysname\] stp pathcost-standard dot1d-1998]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_388615210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x360192206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp cost]{lang="EN-US"}**]{#struct_0_x1139_12555_x190561624}
:::

::: {#-1948353019 .myid}
[]{#_Toc404784608}[]{#struct_0_x1139_12555_x1923951607}[]{#_Toc226350027}[]{#_Toc226375106}

**生成树 \-- 生成树配置命令 \-- stp point-to-point**

------------------------------------------------------------------------

[**[stp point-to-point]{lang="EN-US"}**]{#struct_0_x1139_12555_x1484666285}[命令用来配置端口的链路类型。]{style="font-family:宋体"}

[**[undo stp point-to-point]{lang="EN-US"}**]{#struct_0_x1139_12555_x1590105616}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x822956822}

[**[stp point-to-point]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ **auto** \| **force-false** \| **force-true** }]{lang="EN-US"}]{#struct_0_x1139_12555_1536104581}

[**[undo stp]{lang="EN-US"}***[ ]{lang="EN-US"}***[point-to-point]{lang="EN-US"}**]{#struct_0_x1139_12555_1562067591}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1889436673}

[[端口的链路类型为]{style="font-family:宋体"}**[auto]{lang="EN-US"}**]{#struct_0_x1139_12555_x190627160}[，即由系统自动检测与本端口相连的链路是否为点对点链路。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x415130876}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_256496149}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2143700331}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1311499413}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1757825495}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x615575303}

[**[auto]{lang="EN-US"}**]{#struct_0_x1139_12555_x698601394}[：表示自动检测与本端口相连的链路是否为点对点链路。]{style="font-family:宋体"}

[**[force-false]{lang="EN-US"}**]{#struct_0_x1139_12555_x190692696}[：表示与本端口相连的链路不是点对点链路。]{style="font-family:宋体"}

[**[force-true]{lang="EN-US"}**]{#struct_0_x1139_12555_769867064}[：表示与本端口相连的链路是点对点链路。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1144046084}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当端口与非点对点链路相连时，端口的状态无法快速迁移。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1686346118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某端口是二层聚合接口或其工作在全双工模式下，则可以将该端口配置为与点对点链路相连。通常建议使用缺省配置，由系统进行自动检测。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1598513353}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1139_12555_x2017723853}[MSTP]{lang="EN-US"}[模式下，如果某端口被配置为与点对点链路（或非点对点链路）相连，那么该配置对该端口所属的所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[都有效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某端口被配置为与点对点链路相连，但与该端口实际相连的物理链路不是点对点链路，则有可能引入临时回路。]{style="font-family:宋体"}]{#struct_0_x1139_12555_334180599}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_148495378}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2036334152}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x190758232}[配置与端口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[相连的链路是点对点链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1945468557}

[\[Sysname\] interface gigabitethernet 1/0/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] stp point-to-point force-true]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x159198577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_x600926503}
:::

::: {#-1714300537 .myid}
[]{#_Toc404784609}[]{#struct_0_x1139_12555_1767234300}[]{#_Toc169929446}[]{#_Toc169930522}[]{#_Toc169929447}[]{#_Toc169930523}[]{#_Toc169929448}[]{#_Toc169930524}[]{#_Toc169929449}[]{#_Toc169930525}[]{#_Toc169929450}[]{#_Toc169930526}[]{#_Toc169929451}[]{#_Toc169930527}[]{#_Toc169929452}[]{#_Toc169930528}[]{#_Toc169929453}[]{#_Toc169930529}[]{#_Toc169929454}[]{#_Toc169930530}[]{#_Toc169929455}[]{#_Toc169930531}[]{#_Toc169929456}[]{#_Toc169930532}[]{#_Toc169929457}[]{#_Toc169930533}[]{#_Toc169929458}[]{#_Toc169930534}[]{#_Toc169929459}[]{#_Toc169930535}[]{#_Toc169929460}[]{#_Toc169930536}[]{#_Toc169929464}[]{#_Toc169930540}[]{#_Toc169929465}[]{#_Toc169930541}

**生成树 \-- 生成树配置命令 \-- stp port priority**

------------------------------------------------------------------------

[**[stp port priority]{lang="EN-US"}**]{#struct_0_x1139_12555_x849140103}[命令用来配置端口的优先级。端口优先级可以影响端口在生成树上的角色选择。]{style="font-family:宋体"}

[**[undo stp port priority]{lang="EN-US"}**]{#struct_0_x1139_12555_x774631221}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_982093347}

[**[stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **port priority** *priority*]{lang="EN-US"}]{#struct_0_x1139_12555_x190823768}

[**[undo stp]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **port priority**]{lang="EN-US"}]{#struct_0_x1139_12555_406702294}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_540944379}

[[端口的优先级为]{style="font-family:宋体"}[128]{lang="EN-US"}]{#struct_0_x1139_12555_205102790}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x524949421}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x1223943375}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1124603184}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1509741761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1161336861}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x189840728}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_1255294320}[：表示配置端口在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，表示配置端口在]{style="font-family:宋体"}[MSTP CIST]{lang="EN-US"}[或]{style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_863302607}[：表示配置端口在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[priority]{lang="EN-US"}*]{#struct_0_x1139_12555_1364415205}[：表示端口的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[240]{lang="EN-US"}[，以]{style="font-family:宋体"}[16]{lang="EN-US"}[为步长，如]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[16]{lang="EN-US"}[、]{style="font-family:宋体"}[32]{lang="EN-US"}[等。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x838886833}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常，端口优先级的数值越小，端口的优先级就越高。如果设备的所有端口都采用相同的优先级数值，则端口优先级的高低就取决于该端口索引号的大小，即索引号越小优先级越高。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1538262558}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_70859279}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{lang="EN-US" style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_863499215}[和]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则表示配置端口在]{lang="EN-US" style="font-family:宋体"}[MSTP CIST]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[的优先级]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1345534775}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1221542484}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[在]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[上的优先级为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x189906264}

[\[Sysname\] interface gigabitethernet 1/0/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] stp instance 2 port priority 16]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_863630287}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[上的优先级为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_863564751}

[\[Sysname\] interface gigabitethernet 1/0/3]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/3\] stp vlan 2 port priority 16]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1234841215}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp]{lang="EN-US"}**]{#struct_0_x1139_12555_2043780983}
:::

::: {#1586430041 .myid}
[]{#_Toc404784610}[]{#struct_0_x1139_12555_351156014}[]{#_Toc275870308}[]{#_Toc287952217}[]{#_Toc287960147}[]{#_Toc275870312}[]{#_Toc287952221}[]{#_Toc287960151}

**生成树 \-- 生成树配置命令 \-- stp port-log**

------------------------------------------------------------------------

[**[stp]{lang="EN-US"}**[ **port-log**]{lang="EN-US"}]{#struct_0_x1139_12555_x1281557237}[命令用来打开端口状态变化信息显示开关。]{style="font-family:宋体"}

[**[undo stp]{lang="EN-US"}**[ **port-log**]{lang="EN-US"}]{#struct_0_x1139_12555_x906541320}[命令用来关闭端口状态变化信息显示开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1691903452}

[**[stp]{lang="EN-US"}**[ **port-log** { **all** \| **instance** *instance-list* \| **vlan** *vlan-id-list* }]{lang="EN-US"}]{#struct_0_x1139_12555_x987694665}

[**[undo]{lang="EN-US"}**[ **stp** **port-log** { **all** \| **instance** *instance-list* \| **vlan** *vlan-id-list* }]{lang="EN-US"}]{#struct_0_x1139_12555_1375718928}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_943493072}

[[端口状态变化信息显示开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x853003254}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1762300879}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_1003574255}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1860569680}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_673582470}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1928013361}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1880649289}

[**[all]{lang="EN-US"}**]{#struct_0_x1139_12555_1375653392}[：表示打开或关闭]{style="font-family:宋体"}[MSTP/PVST]{lang="EN-US"}[所有]{style="font-family:宋体"}[MSTI/VLAN]{lang="EN-US"}[中的端口状态变化信息显示开关。]{style="font-family:宋体"}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_1653320039}[：表示打开或关闭]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[中的端口状态变化信息显示开关；如果指定了]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[，则表示打开或关闭]{style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[的端口状态变化信息显示开关。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_863499214}[：表示打开或关闭]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的端口状态变化信息显示开关。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_822224176}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x324287932}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，打开]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[中的端口状态变化信息显示开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1713474584}

[\[Sysname\] stp port-log instance 2]{lang="EN-US"}

[%Aug 16 00:49:41:856 2011 Sysname STP/3/STP_DISCARDING: Instance 2\'s port GigabitEthernet1/0/1 has been set to discarding state.]{lang="EN-US"}

[%Aug 16 00:49:41:856 2011 Sysname STP/3/STP_FORWARDING: Instance 2\'s port GigabitEthernet1/0/2 has been set to forwarding state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1139_12555_1906431764}*[上述信息表明：在]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[中，]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的端口状态变为]{style="font-family:宋体"}[Discarding]{lang="EN-US"}[，]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[的端口状态变为]{style="font-family:宋体"}[Forwarding]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_863237073}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，打开]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[中的端口状态变化信息显示开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_863368145}

[\[Sysname\] stp port-log vlan 1 to 4094]{lang="EN-US"}

[%Aug 16 00:49:41:856 2006 Sysname STP/3/STP_DISCARDING: VLAN 2\'s GigabitEthernet1/0/1 has been set to discarding state.]{lang="EN-US"}

[%Aug 16 00:49:41:856 2006 Sysname STP/3/STP_FORWARDING: VLAN 2\'s GigabitEthernet1/0/2 has been set to forwarding state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1139_12555_863302609}*[上述信息表明：在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中，]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的端口状态变为]{style="font-family:宋体"}[Discarding]{lang="EN-US"}[，]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[的端口状态变为]{style="font-family:宋体"}[Forwarding]{lang="EN-US"}[。]{style="font-family:宋体"}*
:::

::: {#-539353298 .myid}
[]{#_Toc404784611}[]{#struct_0_x1139_12555_x1825204225}[]{#_Toc275870314}[]{#_Toc287952223}[]{#_Toc287960153}[]{#_Toc275870319}[]{#_Toc287952228}[]{#_Toc287960158}[]{#_Toc275870320}[]{#_Toc287952229}[]{#_Toc287960159}

**生成树 \-- 生成树配置命令 \-- stp priority**

------------------------------------------------------------------------

[**[stp priority]{lang="EN-US"}**]{#struct_0_x1139_12555_1375587856}[命令用来配置设备的优先级。]{style="font-family:宋体"}

[**[undo stp priority]{lang="EN-US"}**]{#struct_0_x1139_12555_91847528}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x556957850}

[**[stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **priority** *priority*]{lang="EN-US"}]{#struct_0_x1139_12555_1347535531}

[**[undo stp]{lang="EN-US"}**[ \[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **priority**]{lang="EN-US"}]{#struct_0_x1139_12555_1708909921}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1418773449}

[[设备的优先级为]{style="font-family:宋体"}[32768]{lang="EN-US"}]{#struct_0_x1139_12555_468833483}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1749666630}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_1169210801}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375522320}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_80747928}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x322367674}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_275811427}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x1755953731}[：表示配置设备在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，表示配置设备在]{style="font-family:宋体"}[MSTP CIST]{lang="EN-US"}[或]{style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_863564753}[：表示配置设备在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[priority]{lang="EN-US"}*]{#struct_0_x1139_12555_122513339}[：表示设备的优先级，该数值越小表示优先级越高。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[61440]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[4096]{lang="EN-US"}[，即设备可以设置]{style="font-family:宋体"}[16]{lang="EN-US"}[个优先级取值，如]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[4096]{lang="EN-US"}[、]{style="font-family:宋体"}[8192]{lang="EN-US"}[等。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_863106000}

[[如果未指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}]{#struct_0_x1139_12555_863040464}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则表示配置设备在]{style="font-family:宋体"}[MSTP CIST]{lang="EN-US"}[或]{style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[中的优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2007199349}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_278584591}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置设备在]{style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[中的优先级为]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1375456784}

[\[Sysname\] stp instance 1 priority 4096]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_863171536}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置设备在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中的优先级为]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_863368144}

[[\[Sysname\] stp vlan 1 priority 4096]{lang="EN-US"}]{#_Toc324858474}
:::

::: {#1900641884 .myid}
[]{#_Toc404784612}[]{#struct_0_x1139_12555_1442026998}[]{#_Toc396825309}[]{#_Toc385773966}[]{#_Toc385773570}

**生成树 \-- 生成树配置命令 \-- stp pvst-bpdu-protection**

------------------------------------------------------------------------

[**[stp pvst-bpdu-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_484280363}[命令用来开启]{style="font-family:
宋体"}[MSTP]{lang="EN-US"}[的]{style="font-family:宋体"}[PVST]{lang="EN-US"}[报文保护功能。]{style="font-family:宋体"}

[**[undo stp pvst-bpdu-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_840022223}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1911444610}

[**[stp pvst-bpdu-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x530065652}

[**[undo stp pvst-bpdu-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x1912497500}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1038742471}

[[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_x2027946505}[的]{style="font-family:宋体"}[PVST]{lang="EN-US"}[报文保护功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x786621328}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x969754172}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1061221330}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_159828134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x869079977}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1448021984}

[[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}]{#struct_0_x1139_12555_776329768}[模式下，设备上开启了]{style="font-family:宋体"}[PVST]{lang="EN-US"}[报文保护功能后，如果某些端口收到了]{style="font-family:宋体"}[PVST]{lang="EN-US"}[报文，系统就将这些端口关闭。被关闭的端口在经过一定时间间隔之后将被自动重新打开，关闭的时间间隔通过]{style="font-family:宋体"}**[shutdown-interval]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1338010184}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x437840621}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，开启]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[的]{style="font-family:宋体"}[PVST]{lang="EN-US"}[报文保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_639623961}

[\[Sysname\] stp pvst-bpdu-protection]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1815814516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[shutdown-interval]{lang="EN-US"}**]{#struct_0_x1139_12555_x1690140884}[（基础配置指导]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[设备管理）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-723604670 .myid}
[]{#_Toc404784613}[]{#struct_0_x1139_12555_x1117065171}[]{#_Toc275870322}[]{#_Toc287952231}[]{#_Toc287960161}[]{#_Toc275870325}[]{#_Toc287952234}[]{#_Toc287960164}

**生成树 \-- 生成树配置命令 \-- stp region-configuration**

------------------------------------------------------------------------

[**[stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1376244765}[命令用来进入]{style="font-family:
宋体"}[MST]{lang="EN-US"}[域视图。]{style="font-family:宋体"}

[**[undo stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1405041713}[命令用来将]{style="font-family:
宋体"}[MST]{lang="EN-US"}[域的配置恢复为缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1325142162}

[**[stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x1027793671}

[**[undo stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x533691934}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1291030984}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x1546600996}[域的三个参数均取缺省值，即：]{style="font-family:宋体"}[MST]{lang="EN-US"}[域名为设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[都映射到]{style="font-family:宋体"}[CIST]{lang="EN-US"}[上、]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[修订级别为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375391248}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1490042741}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x866638191}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1890876597}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x2049818398}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x1139_12555_3895946}

[[进入]{style="font-family:宋体"}[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x123653667}[域视图后，用户可以对]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的相关参数（域名、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表和修订级别）进行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x21930131}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1887150686}[进入]{style="font-family:宋体"}[MST]{lang="EN-US"}[域视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1375325712}

[\[Sysname\] stp region-configuration]{lang="EN-US"}

[\[Sysname-mst-region\]]{lang="EN-US"}
:::

::: {#1610071568 .myid}
[]{#_Toc404784614}[]{#struct_0_x1139_12555_x720792836}

**生成树 \-- 生成树配置命令 \-- stp role-restriction**

------------------------------------------------------------------------

[**[stp role-restriction]{lang="EN-US"}**]{#struct_0_x1139_12555_x1821250899}[命令用来开启端口角色限制功能。]{style="font-family:宋体"}

[**[undo stp role-restriction]{lang="EN-US"}**]{#struct_0_x1139_12555_638952426}[命令用来关闭端口角色限制功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2047792242}

[**[stp role-restriction]{lang="EN-US"}**]{#struct_0_x1139_12555_857941013}

[**[undo stp role-restriction]{lang="EN-US"}**]{#struct_0_x1139_12555_x742240724}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_467603625}

[[端口角色限制功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1375260176}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1455606454}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x1286339861}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1842831583}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x337004687}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1761145029}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1650807217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当开启了某端口的端口角色限制功能之后，该端口将不能被计算为根端口。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1755771852}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1376243216}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x812865053}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1107636461}[开启端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的端口角色限制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1228147928}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp role-restriction]{lang="EN-US"}
:::

::: {#1816425555 .myid}
[]{#_Toc404784615}[]{#struct_0_x1139_12555_1561902884}

**生成树 \-- 生成树配置命令 \-- stp root primary**

------------------------------------------------------------------------

[**[stp root primary]{lang="EN-US"}**]{#struct_0_x1139_12555_x1470481438}[命令用来配置当前设备为根桥。]{style="font-family:宋体"}

[**[undo stp root]{lang="EN-US"}**]{#struct_0_x1139_12555_1069076098}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x28045467}

[**[stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **root primary**]{lang="EN-US"}]{#struct_0_x1139_12555_1376177680}

[**[undo stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **root**]{lang="EN-US"}]{#struct_0_x1139_12555_x2028110873}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x89171649}

[[设备不是根桥。]{style="font-family:宋体"}]{#struct_0_x1139_12555_700649351}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_614044900}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_1753431872}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_633843696}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x74314270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_467740564}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375718929}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_943427536}[：表示配置当前设备为]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的根桥。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x1865711822}[：表示配置当前设备为]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的根桥。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1926425568}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备一旦被配置为根桥之后，便不能再修改该设备的优先级。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x522267255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1865449678}[MSTI]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则表示配置当前设备为]{style="font-family:宋体"}[MSTP CIST]{lang="EN-US"}[或]{style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[的根桥。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_905939991}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x820939910}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置当前设备为]{style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[的根桥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x730850511}

[\[Sysname\] stp instance 1 root primary]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1865318606}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置当前设备为]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[的根桥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1865777359}

[\[Sysname\] stp vlan 1 root primary]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1399186199}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp priority]{lang="EN-US"}**]{#struct_0_x1139_12555_1375653393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp root secondary]{lang="EN-US"}**]{#struct_0_x1139_12555_1653254503}
:::

::: {#-1816864187 .myid}
[]{#_Toc404784616}[]{#struct_0_x1139_12555_1219384038}[]{#_Toc275870329}[]{#_Toc287952238}[]{#_Toc287960168}[]{#_Toc275870332}[]{#_Toc287952241}[]{#_Toc287960171}

**生成树 \-- 生成树配置命令 \-- stp root secondary**

------------------------------------------------------------------------

[**[stp root secondary]{lang="EN-US"}**]{#struct_0_x1139_12555_815060919}[命令用来配置当前设备为备份根桥。]{style="font-family:宋体"}

[**[undo stp root]{lang="EN-US"}**]{#struct_0_x1139_12555_x53055842}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x424179891}

[**[stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **root secondary**]{lang="EN-US"}]{#struct_0_x1139_12555_980425281}

[**[undo stp ]{lang="EN-US"}**[\[ **instance** *instance-list* \| **vlan** *vlan-id-list* \] **root**]{lang="EN-US"}]{#struct_0_x1139_12555_2085050493}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x212440342}

[[设备不是备份根桥。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1375587857}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_91913064}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x208915695}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_324024535}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1094966588}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x487964476}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_581310390}

[**[instance]{lang="EN-US"}***[ instance-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x1155819983}[：表示配置当前设备为]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的备份根桥。]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[，表示方式为]{style="font-family:宋体"}*[instance-list]{lang="EN-US"}*[ = { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[CIST]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x1865384143}[：表示配置当前设备为]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的备份根桥。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375522321}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备一旦被配置为备份根桥之后，便不能再修改该设备的优先级。]{style="font-family:宋体"}]{#struct_0_x1139_12555_80813464}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1865777356}[MSTI]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则表示配置当前设备为]{style="font-family:宋体"}[MSTP CIST]{lang="EN-US"}[或]{style="font-family:宋体"}[STP/RSTP]{lang="EN-US"}[的备份根桥。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1506782795}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1885927972}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置当前设备为]{style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[的备份根桥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1051665401}

[\[Sysname\] stp instance 1 root secondary]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1865646284}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置当前设备为]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[的备份根桥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1865711820}

[\[Sysname\] stp vlan 1 root secondary]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x559358520}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp priority]{lang="EN-US"}**]{#struct_0_x1139_12555_x860776675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp root primary]{lang="EN-US"}**]{#struct_0_x1139_12555_1439685896}
:::

::: {#1466557497 .myid}
[]{#_Toc404784617}[]{#struct_0_x1139_12555_x1172976167}[]{#_Toc275870334}[]{#_Toc287952243}[]{#_Toc287960173}[]{#_Toc275870337}[]{#_Toc287952246}[]{#_Toc287960176}

**生成树 \-- 生成树配置命令 \-- stp root-protection**

------------------------------------------------------------------------

[**[stp root-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_1375456785}[命令用来开启端口的根保护功能。]{style="font-family:宋体"}

[**[undo stp root-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x1117130707}[命令用来关闭端口的根保护功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1503406778}

[**[stp root-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x781906790}

[**[undo stp]{lang="EN-US"}**[ **root-protection**]{lang="EN-US"}]{#struct_0_x1139_12555_596586123}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x972114436}

[[端口上的根保护功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1139_12555_2028328039}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_924961685}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x1027431019}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375391249}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1490108277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1247478308}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2037127126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个端口上，不允许同时配置根保护功能和环路保护功能。]{style="font-family:宋体"}]{#struct_0_x1139_12555_1344370679}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x547339272}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1612371336}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x727679357}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启根保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1375325713}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp root-protection]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x720727300}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp edged-port]{lang="EN-US"}**]{#struct_0_x1139_12555_2052295903}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp loop-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_492294471}
:::

::: {#-1029739707 .myid}
[]{#_Toc404784618}[]{#struct_0_x1139_12555_x649114841}

**生成树 \-- 生成树配置命令 \-- stp tc-protection**

------------------------------------------------------------------------

[**[stp tc-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_x151110054}[命令用来开启防]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[攻击保护功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **stp tc-protection**]{lang="EN-US"}]{#struct_0_x1139_12555_761983491}[命令用来关闭防]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[攻击保护功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x259604717}

[**[stp tc-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_1485250654}

[**[undo stp]{lang="EN-US"}**[ **tc-protection**]{lang="EN-US"}]{#struct_0_x1139_12555_1375260177}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1455540918}

[[防]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x1898793616}[攻击保护功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_188679038}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_1756198665}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1873594831}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x2016213297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1607501447}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1376243217}

[[当开启了防]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x812799517}[攻击保护功能后，如果设备在单位时间（固定为十秒）内收到]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[的次数大于]{style="font-family:宋体"}**[stp tc-protection threshold]{lang="EN-US"}**[命令所指定的最高次数（假设为]{style="font-family:宋体"}[N]{lang="EN-US"}[次），那么该设备在这段时间之内将只进行]{style="font-family:宋体"}[N]{lang="EN-US"}[次刷新转发地址表项的操作，而对于超出]{style="font-family:宋体"}[N]{lang="EN-US"}[次的那些]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[，设备会在这段时间过后再统一进行一次地址表项刷新的操作，这样就可以避免频繁地刷新转发地址表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_746652414}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x512750573}[关闭防]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[攻击保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_2107364032}

[\[Sysname\] undo stp tc-protection]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1141446349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp tc-protection threshold]{lang="EN-US"}**]{#struct_0_x1139_12555_1725011545}
:::

::: {#1288687743 .myid}
[]{#_Toc404784619}[]{#struct_0_x1139_12555_1002547326}[]{#_Toc144808363}[]{#_Toc82234889}[]{#_Toc72918823}[]{#_Toc36367113}[]{#_Toc34185810}

**生成树 \-- 生成树配置命令 \-- stp tc-protection threshold**

------------------------------------------------------------------------

[**[stp tc-protection threshold]{lang="EN-US"}**]{#struct_0_x1139_12555_2030993686}[命令用来配置在单位时间（固定为十秒）内，设备收到]{style="font-family:
宋体"}[TC-BPDU]{lang="EN-US"}[后一定时间内，允许收到]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[后立即刷新转发地址表项的最高次数。]{style="font-family:宋体"}

[**[undo stp tc-protection threshold]{lang="EN-US"}**]{#struct_0_x1139_12555_1376177681}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2028176409}

[**[stp tc-protection threshold ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1139_12555_702655879}

[**[undo stp tc-protection threshold]{lang="EN-US"}**]{#struct_0_x1139_12555_x487145832}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1313049453}

[[在单位时间（固定为十秒）内，设备收到]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x141347483}[后立即刷新转发地址表项的最高次数为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2068788754}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_765559067}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375718926}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_942575568}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1764291518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_52807849}

[*[number]{lang="EN-US"}*]{#struct_0_x1139_12555_441399716}[：表示在单位时间（固定为十秒）内，设备收到]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[后立即刷新转发地址表项的最高次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1896768370}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1624525957}[配置在单位时间（固定为十秒）内，设备收到]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[后一定时间内，允许收到]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[后立即刷新转发地址表项的最高次数为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1807254303}

[\[Sysname\] stp tc-protection threshold 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x590866803}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp tc-protection]{lang="EN-US"}**]{#struct_0_x1139_12555_1375653390}
:::

::: {#291638870 .myid}
[]{#_Toc404784620}[]{#struct_0_x1139_12555_1653451111}

**生成树 \-- 生成树配置命令 \-- stp tc-restriction**

------------------------------------------------------------------------

[**[stp tc-restriction]{lang="EN-US"}**]{#struct_0_x1139_12555_51556338}[命令用来开启]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[传播限制功能。]{style="font-family:宋体"}

[**[undo stp tc-restriction]{lang="EN-US"}**]{#struct_0_x1139_12555_x21383419}[命令用来关闭]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[传播限制功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1657841044}

[**[stp tc-restriction]{lang="EN-US"}**]{#struct_0_x1139_12555_x1366970511}

[**[undo stp tc-restriction]{lang="EN-US"}**]{#struct_0_x1139_12555_x168841682}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1372296811}

[[TC-BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_1375587854}[传播限制功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_91716456}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x499153919}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_517851090}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_670901352}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x540569145}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x463787355}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当开启了某端口的]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1448717919}[TC-BPDU]{lang="EN-US"}[传播限制功能之后，该端口将不再向其它端口传播]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[，也不删除本机的转发地址表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x967001336}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375522318}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_81272219}[开启端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[TC-BPDU]{lang="EN-US"}[传播限制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x2024498807}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp tc-restriction]{lang="EN-US"}
:::

::: {#973005433 .myid}
[]{#_Toc404784621}[]{#struct_0_x1139_12555_x1865646285}[]{#_Toc362337790}[]{#_Toc341797781}[]{#_Toc324858483}[]{#_Toc295921856}

**生成树 \-- 生成树配置命令 \-- stp tc-snooping**

------------------------------------------------------------------------

[**[stp tc-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_x1865515213}[命令用来开启]{style="font-family:宋体"}[TC Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo stp]{lang="EN-US"}**[ **tc-snooping**]{lang="EN-US"}]{#struct_0_x1139_12555_x1865580749}[命令用来关闭]{style="font-family:宋体"}[TC Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1865384141}

[**[stp tc-snooping]{lang="EN-US"}**]{#struct_0_x1139_12555_x1865449677}

[**[undo stp]{lang="EN-US"}**[ **tc-snooping**]{lang="EN-US"}]{#struct_0_x1139_12555_x1865318605}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1865777354}

[[TC Snooping]{lang="EN-US"}]{#struct_0_x1139_12555_x1865842890}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1865711818}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1865515210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1865580746}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1865449674}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1865253066}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1865318602}

[[TC Snooping]{lang="EN-US"}]{#struct_0_x1139_12555_x1865842891}[功能与生成树协议互斥，因此在开启]{style="font-family:宋体"}[TC Snooping]{lang="EN-US"}[功能之前必须全局关闭生成树协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1865646283}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1865711819}[全局关闭生成树协议，并开启]{style="font-family:宋体"}[TC Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1865580747}

[\[Sysname\] undo stp global enable]{lang="EN-US"}

[\[Sysname\] stp tc-snooping]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1865384139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp ]{lang="EN-US"}**]{#struct_0_x1139_12555_x1865449675}**[global ]{lang="EN-US"}[enable]{lang="EN-US"}**
:::

::: {#478853974 .myid}
[]{#_Toc404784622}[]{#struct_0_x1139_12555_1815201319}[]{#_Toc362451043}[]{#_Toc363033797}

**生成树 \-- 生成树配置命令 \-- stp timer forward-delay**

------------------------------------------------------------------------

[**[stp timer forward-delay]{lang="EN-US"}**]{#struct_0_x1139_12555_x2111205173}[命令用来配置]{style="font-family:宋体"}[Forward Delay]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}

[**[undo stp timer forward-delay]{lang="EN-US"}**]{#struct_0_x1139_12555_2109485585}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x930586900}

[**[stp]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **vlan** *vlan-id-list* \] **timer forward-delay** *time*]{lang="EN-US"}]{#struct_0_x1139_12555_425654590}

[**[undo stp]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **vlan** *vlan-id-list* \] **timer forward-delay**]{lang="EN-US"}]{#struct_0_x1139_12555_1375456782}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1117458387}

[[Forward Delay]{lang="EN-US"}]{#struct_0_x1139_12555_x243585780}[为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1771392154}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1142860822}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1056743344}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x182401309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1073759867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1474570729}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x299627881}[：表示配置]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[Forward Delay]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，表示配置]{style="font-family:宋体"}[STP/RSTP/MSTP]{lang="EN-US"}[的]{style="font-family:宋体"}[Forward Delay]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}

[*[time]{lang="EN-US"}*]{#struct_0_x1139_12555_1375391246}[：表示]{style="font-family:宋体"}[Forward Delay]{lang="EN-US"}[的时间值，取值范围为]{style="font-family:宋体"}[400]{lang="EN-US"}[～]{style="font-family:宋体"}[3000]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[0.01]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1489911669}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Forward Delay]{lang="EN-US"}]{#struct_0_x1139_12555_2091891420}[用于确定状态迁移的延迟时间。为了防止产生临时环路，生成树协议在端口由]{style="font-family:
宋体"}[Discarding]{lang="EN-US"}[状态向]{style="font-family:宋体"}[Forwarding]{lang="EN-US"}[状态迁移的过程中设置了]{style="font-family:宋体"}[Learning]{lang="EN-US"}[状态作为过渡，并规定状态迁移需要等待]{style="font-family:宋体"}[Forward Delay]{lang="EN-US"}[时间，以保持与远端的设备状态切换同步。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下不建议使用本命令直接调整]{style="font-family:宋体"}]{#struct_0_x1139_12555_583849611}[Forward Delay]{lang="EN-US"}[时间参数。由于该时间参数的取值与网络规模有关，因此建议通过使用]{style="font-family:宋体"}**[stp bridge-diameter]{lang="EN-US"}**[命令调整网络直径，使生成树协议自动调整该时间参数的值。当网络直径取缺省值时，该时间参数也取缺省值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x723444892}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_17510132}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置]{style="font-family:宋体"}[Forward Delay]{lang="EN-US"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1341634435}

[\[Sysname\] stp timer forward-delay 2000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x299496809}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的]{style="font-family:宋体"}[Forward Delay]{lang="EN-US"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x299300201}

[\[Sysname\] stp vlan 2 timer forward-delay 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_515076389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp bridge-diameter]{lang="EN-US"}**]{#struct_0_x1139_12555_x360323280}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer hello]{lang="EN-US"}**]{#struct_0_x1139_12555_1375325710}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer max-age]{lang="EN-US"}**]{#struct_0_x1139_12555_x720661764}
:::

::: {#-1852795202 .myid}
[]{#_Toc404784623}[]{#struct_0_x1139_12555_1779951927}[]{#_Toc275870343}[]{#_Toc287952252}[]{#_Toc287960182}[]{#_Toc275870346}[]{#_Toc287952255}[]{#_Toc287960185}

**生成树 \-- 生成树配置命令 \-- stp timer hello**

------------------------------------------------------------------------

[**[stp ]{lang="EN-US"}**[\[ **vlan** *vlan-id-list* \] **timer hello**]{lang="EN-US"}]{#struct_0_x1139_12555_x2092581050}[命令用来配置]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}

[**[undo stp ]{lang="EN-US"}**[\[ **vlan** *vlan-id-list* \] **timer hello**]{lang="EN-US"}]{#struct_0_x1139_12555_2079448521}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1371306956}

[**[stp]{lang="EN-US"}**[ ]{lang="EN-US"}**[timer hello]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1139_12555_x1754995305}

[**[undo stp]{lang="EN-US"}**[ ]{lang="EN-US"}**[timer hello]{lang="EN-US"}**]{#struct_0_x1139_12555_647940360}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375260174}

[[Hello Time]{lang="EN-US"}]{#struct_0_x1139_12555_x1455475382}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1504057481}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x141524558}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1666040120}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_322967965}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x382581482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x423904914}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x299562346}[：表示配置]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，表示配置]{style="font-family:宋体"}[STP/RSTP/MSTP]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}

[*[time]{lang="EN-US"}*]{#struct_0_x1139_12555_x1960366254}[：表示]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[的时间值，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[0.01]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1376243214}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello Time]{lang="EN-US"}]{#struct_0_x1139_12555_x812996125}[用于检测链路是否存在故障。生成树协议每隔]{style="font-family:
宋体"}[Hello Time]{lang="EN-US"}[时间会发送]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[，以确认链路是否存在故障。如果设备在]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[时间内没有收到]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[，则会由于消息超时而重新计算生成树。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下不建议使用本命令直接调整]{style="font-family:宋体"}]{#struct_0_x1139_12555_751680566}[Hello Time]{lang="EN-US"}[时间参数。由于该时间参数的取值与网络规模有关，因此建议通过使用]{style="font-family:宋体"}**[stp bridge-diameter]{lang="EN-US"}**[命令调整网络直径，使生成树协议自动调整该时间参数的值。当网络直径取缺省值时，该时间参数也取缺省值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1807174265}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x819071431}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[秒。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x58630881}

[\[Sysname\] stp timer hello 400]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x299431274}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[秒。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x299496810}

[\[Sysname\] stp vlan 2 timer hello 400]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_428122063}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp bridge-diameter]{lang="EN-US"}**]{#struct_0_x1139_12555_x360454352}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer forward-delay]{lang="EN-US"}**]{#struct_0_x1139_12555_x2026085708}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer max-age]{lang="EN-US"}**]{#struct_0_x1139_12555_1376177678}
:::

::: {#-2071393869 .myid}
[]{#_Toc404784624}[]{#struct_0_x1139_12555_x974078501}[]{#_Toc275870348}[]{#_Toc287952257}[]{#_Toc287960187}[]{#_Toc275870351}[]{#_Toc287952260}[]{#_Toc287960190}

**生成树 \-- 生成树配置命令 \-- stp timer max-age**

------------------------------------------------------------------------

[**[stp timer max-age]{lang="EN-US"}**]{#struct_0_x1139_12555_x815375165}[命令用来配置]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}

[**[undo stp timer max-age]{lang="EN-US"}**]{#struct_0_x1139_12555_x173133805}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1951233687}

[**[stp]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **vlan** *vlan-id-list* \] **timer max-age** *time*]{lang="EN-US"}]{#struct_0_x1139_12555_1290913658}

[**[undo stp]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **vlan** *vlan-id-list* \] **timer max-age**]{lang="EN-US"}]{#struct_0_x1139_12555_x1871251014}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x956182138}

[[Max Age]{lang="EN-US"}]{#struct_0_x1139_12555_1375718927}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_942510032}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1753132601}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1713105638}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1151886039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1557948520}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1452488509}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x299758951}[：表示配置]{style="font-family:宋体"}[PVST]{lang="EN-US"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，表示配置]{style="font-family:宋体"}[STP/RSTP/MSTP]{lang="EN-US"}[的]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[时间参数。]{style="font-family:宋体"}

[*[time]{lang="EN-US"}*]{#struct_0_x1139_12555_193479518}[：表示]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[的时间值，取值范围为]{style="font-family:宋体"}[600]{lang="EN-US"}[～]{style="font-family:宋体"}[4000]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[0.01]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1400123989}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max Age]{lang="EN-US"}]{#struct_0_x1139_12555_1375653391}[用于确定]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[是否超时。在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[的]{style="font-family:宋体"}[CIST]{lang="EN-US"}[上，设备根据]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[时间来确定端口收到的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[是否超时。如果端口收到的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[超时，则需要对该]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[重新计算。]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[时间对]{lang="EN-US" style="font-family:宋体"}[MSTP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[MSTI]{lang="EN-US"}[无效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下不建议使用本命令直接调整]{style="font-family:宋体"}]{#struct_0_x1139_12555_1653385575}[Max Age]{lang="EN-US"}[时间参数。由于该时间参数的取值与网络规模有关，因此建议通过使用]{style="font-family:宋体"}**[stp bridge-diameter]{lang="EN-US"}**[命令调整网络直径，使生成树协议自动调整该时间参数的值。当网络直径取缺省值时，该时间参数也取缺省值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1539973587}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1246177402}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，配置]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x450560848}

[\[Sysname\] stp timer max-age 1000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x299627879}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，配置]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的]{style="font-family:宋体"}[Max Age]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x299496807}

[\[Sysname\] stp vlan 2 timer max-age 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1617169810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp bridge-diameter]{lang="EN-US"}**]{#struct_0_x1139_12555_x359536848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer forward-delay]{lang="EN-US"}**]{#struct_0_x1139_12555_x2127514398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer hello]{lang="EN-US"}**]{#struct_0_x1139_12555_x408327439}
:::

::: {#-203871313 .myid}
[]{#_Toc404784625}[]{#struct_0_x1139_12555_91781992}[]{#_Toc275870353}[]{#_Toc287952262}[]{#_Toc287960192}[]{#_Toc275870356}[]{#_Toc287952265}[]{#_Toc287960195}

**生成树 \-- 生成树配置命令 \-- stp timer-factor**

------------------------------------------------------------------------

[**[stp timer-factor]{lang="EN-US"}**]{#struct_0_x1139_12555_1731071168}[命令用来配置超时时间因子，该因子用来确定设备的超时时间：超时时间]{style="font-family:宋体"}[ = ]{lang="EN-US"}[超时时间因子]{style="font-family:宋体"} [×]{style="font-family:宋体"} [3 ]{lang="EN-US"}[×]{style="font-family:宋体"} [Hello Time]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo stp timer-factor]{lang="EN-US"}**]{#struct_0_x1139_12555_x168124283}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1746989861}

[**[stp timer-factor ]{lang="EN-US"}***[factor]{lang="EN-US"}*]{#struct_0_x1139_12555_628382759}

[**[undo]{lang="EN-US"}**[ **stp timer-factor**]{lang="EN-US"}]{#struct_0_x1139_12555_941734079}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1419762855}

[[超时时间因子为]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_x1139_12555_x1567233445}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1375522319}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_81337755}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1214529763}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x1663880737}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x708998525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2135648608}

[*[factor]{lang="EN-US"}*]{#struct_0_x1139_12555_262283813}[：表示超时时间因子，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1710017227}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当网络拓扑结构稳定后，非根桥设备会每隔]{style="font-family:宋体"}]{#struct_0_x1139_12555_1375456783}[Hello Time]{lang="EN-US"}[时间向周围相连设备转发根桥发出的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[以确认链路是否存在故障。通常如果设备在]{style="font-family:宋体"}[9]{lang="EN-US"}[倍的]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[时间内没有收到上游设备发来的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[，就会认为上游设备已经故障，从而重新进行生成树的计算。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有时设备在较长时间内收不到上游设备发来的]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1117523923}[BPDU]{lang="EN-US"}[，可能是由于上游设备的繁忙导致的，在这种情况下一般不应重新进行生成树的计算。因此在稳定的网络中，可以通过延长超时时间来减少网络资源的浪费。在一个稳定的网络中，建议将超时时间因子配置为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x467208907}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1256555574}[配置超时时间因子为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_x1546953076}

[\[Sysname\] stp timer-factor 7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1243535999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp timer hello]{lang="EN-US"}**]{#struct_0_x1139_12555_631039339}
:::

::: {#1429073405 .myid}
[]{#_Toc404784626}[]{#struct_0_x1139_12555_x1551988429}

**生成树 \-- 生成树配置命令 \-- stp transmit-limit**

------------------------------------------------------------------------

[**[stp transmit-limit]{lang="EN-US"}**]{#struct_0_x1139_12555_x903126301}[命令用来配置端口发送]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[的速率。]{style="font-family:宋体"}

[**[undo stp transmit-limit]{lang="EN-US"}**]{#struct_0_x1139_12555_1375391247}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x1489977205}

[**[stp transmit-limit ]{lang="EN-US"}***[limit]{lang="EN-US"}*]{#struct_0_x1139_12555_1772445034}

[**[undo stp]{lang="EN-US"}***[ ]{lang="EN-US"}***[transmit-limit]{lang="EN-US"}**]{#struct_0_x1139_12555_x870346154}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1932246469}

[[端口发送]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_x1139_12555_x904844247}[的速率为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2082814898}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1139_12555_x2023001732}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_961841007}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1375325711}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x720596228}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1294473220}

[*[limit]{lang="EN-US"}*]{#struct_0_x1139_12555_x574817702}[：表示端口发送]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[的速率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x868857335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每]{style="font-family:宋体"}]{#struct_0_x1139_12555_1375260175}[Hello Time]{lang="EN-US"}[时间内端口能够发送的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[的最大数目]{style="font-family:宋体"}[＝]{lang="EN-US" style="font-family:宋体"}[端口发送]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[的速率]{style="font-family:宋体"}[＋]{lang="EN-US" style="font-family:宋体"}[Hello Time]{lang="EN-US"}[时间]{lang="EN-US" style="font-family:宋体"}[值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[端口发送]{style="font-family:宋体"}]{#struct_0_x1139_12555_x1455409846}[BPDU]{lang="EN-US"}[的速率越高，每个]{style="font-family:宋体"}[Hello Time]{lang="EN-US"}[内可发送的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[数量就越多，占用的系统资源也越多。适当配置发送速率一方面可以限制端口发送]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[的速度，另一方面还可以防止在网络拓扑动荡时，生成树协议占用过多的带宽资源。建议用户采用缺省配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。]{style="font-family:宋体"}]{#struct_0_x1139_12555_x445703751}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_298360019}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_1010723628}[配置端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[的速率为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_9938677}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] stp transmit-limit 5]{lang="EN-US"}
:::

::: {#-1463513680 .myid}
[]{#_Toc404784627}[]{#struct_0_x1139_12555_x299758952}[]{#_Toc362337796}[]{#_Toc341797787}[]{#_Toc324858489}

**生成树 \-- 生成树配置命令 \-- stp vlan enable**

------------------------------------------------------------------------

[**[stp]{lang="EN-US"}**[ **vlan** **enable**]{lang="EN-US"}]{#struct_0_x1139_12555_x299562344}[命令用来在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中开启生成树协议。]{style="font-family:宋体"}

[**[undo stp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1139_12555_x299431272}[命令用来在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中关闭生成树协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x299496808}

[**[stp]{lang="EN-US"}**[ **vlan** *vlan-id-list* **enable**]{lang="EN-US"}]{#struct_0_x1139_12555_x299365736}

[**[undo stp vlan]{lang="EN-US"}**[ *vlan-id-list* ]{lang="EN-US"}**[enable]{lang="EN-US"}**]{#struct_0_x1139_12555_x299169128}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x299234664}

[[生成树协议在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_x299758949}[中的开启状态与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x299562341}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1139_12555_x299431269}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x299496805}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x299365733}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_x299169125}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x299234661}

[**[vlan]{lang="EN-US"}***[ vlan-id-list]{lang="EN-US"}*]{#struct_0_x1139_12555_x299758950}[：开启或关闭指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[上的生成树协议。]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果不指定该参数，将开启或关闭全局的（不包括]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[上的）生成树协议。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x299562342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当生成树协议开启后，设备会根据用户配置的生成树工作模式来决定运行在]{style="font-family:宋体"}]{#struct_0_x1139_12555_x299431270}[STP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[模式、]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式还是]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当生成树协议开启后，系统根据收到的]{style="font-family:宋体"}]{#struct_0_x1139_12555_x299496806}[BPDU]{lang="EN-US"}[动态维护相应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的生成树状态；当生成树协议关闭后，系统将不再维护该状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x299365734}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x299169126}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，先全局开启生成树协议，再开启]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中的生成树协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1266390524}

[\[Sysname\] stp mode pvst]{lang="EN-US"}

[\[Sysname\] stp global enable]{lang="EN-US"}

[\[Sysname\] stp vlan 2 enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1266324988}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp enable]{lang="EN-US"}**]{#struct_0_x1139_12555_1266521596}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp global enable]{lang="EN-US"}**]{#struct_0_x1139_12555_1266652668}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stp mode]{lang="EN-US"}**]{#struct_0_x1139_12555_x360323281}
:::

::: {#-607575441 .myid}
[]{#_Toc404784628}[]{#struct_0_x1139_12555_x1171609485}

**生成树 \-- 生成树配置命令 \-- vlan-mapping modulo**

------------------------------------------------------------------------

[**[vlan-mapping modulo]{lang="EN-US"}**]{#struct_0_x1139_12555_1376243215}[命令用来快速配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射表，使当前]{style="font-family:宋体"}[MST]{lang="EN-US"}[域内的所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[按指定的模值映射到不同的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x812930589}

[**[vlan-mapping modulo]{lang="EN-US"}**[ *modulo*]{lang="EN-US"}]{#struct_0_x1139_12555_x1196633334}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x29259608}

[[所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_287313732}[都映射到]{style="font-family:宋体"}[CIST]{lang="EN-US"}[（即]{style="font-family:宋体"}[MSTI 0]{lang="EN-US"}[）上。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x501715158}

[[MST]{lang="EN-US"}]{#struct_0_x1139_12555_x1841678194}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1139_12555_1471040758}

[[network-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1992176906}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1139_12555_1376177679}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x2028700686}

[*[modulo]{lang="EN-US"}*]{#struct_0_x1139_12555_x1236814369}[：表示模值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[到设备支持的最大值（最大值与设备的型号有关，请以设备的实际情况为准）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x524899322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能将同一个]{style="font-family:宋体"}]{#struct_0_x1139_12555_x62448816}[VLAN]{lang="EN-US"}[映射到不同的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[上。如果将一个已映射到某]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[重新映射到另一个]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[时，原先的映射关系将被取消。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令将]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1139_12555_1953998389}[映射到编号为]{lang="EN-US" style="font-family:宋体"}[ (VLAN ID - 1) % *modulo* + 1]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[MSTI]{lang="EN-US"}[上。其中，]{lang="EN-US" style="font-family:宋体"}[(VLAN ID - 1) % *modulo*]{lang="EN-US"}[表示对]{lang="EN-US" style="font-family:宋体"}[ (VLAN ID - 1) ]{lang="EN-US"}[进行求模运算，如模值为]{lang="EN-US" style="font-family:宋体"}[15]{lang="EN-US"}[，则]{lang="EN-US" style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[映射到]{lang="EN-US" style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[映射到]{lang="EN-US" style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[、......、]{lang="EN-US" style="font-family:宋体"}[VLAN 15]{lang="EN-US"}[映射到]{lang="EN-US" style="font-family:宋体"}[MSTI 15]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[VLAN 16]{lang="EN-US"}[映射到]{lang="EN-US" style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[，依次类推。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1139_12555_x814692150}

[[\# ]{lang="EN-US"}]{#struct_0_x1139_12555_x1305941588}[将所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[按照模]{style="font-family:宋体"}[8]{lang="EN-US"}[映射到不同的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1139_12555_1375718924}

[\[Sysname\] stp region-configuration]{lang="EN-US"}

[\[Sysname-mst-region\] vlan-mapping modulo 8]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1139_12555_942706640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[active region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x360454353}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[check region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x360519889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display stp region-configuration]{lang="EN-US"}**]{#struct_0_x1139_12555_x907546384}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[region-name]{lang="EN-US"}**]{#struct_0_x1139_12555_x1452185550}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[revision-level]{lang="EN-US"}**]{#struct_0_x1139_12555_x66967061}
:::
