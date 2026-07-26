::::: {#1083034321 .myid}
[]{#_Toc404793634}[]{#struct_0_38774_20165_x1670783024}[]{#_Toc384729392}

**对象策略 \-- 对象策略配置命令 \-- accelerate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](对象策略命令.files/image001.png){#图片 1 width="62" height="26"}]{lang="EN-US"}]{#struct_0_38774_20165_204942376}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_38774_20165_x87047364}
:::

**[ ]{lang="EN-US"}**

[**[accelerate]{lang="EN-US"}**]{#struct_0_38774_20165_1981183774}[命令用来开启]{style="font-family:宋体"}[对象策略]{style="font-family:宋体"}[加速功能。]{style="font-family:宋体"}

[**[undo accelerate]{lang="EN-US"}**]{#struct_0_38774_20165_1941111483}[命令用来关闭对象策略加速功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1925888074}

[**[accelerate]{lang="EN-US"}**]{#struct_0_38774_20165_1151260597}

[**[undo accelerate ]{lang="EN-US"}**]{#struct_0_38774_20165_1955865930}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1670848560}

[[对象策略的加速功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_38774_20165_x662759309}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_x748031703}

[[对象策略视图]{style="font-family:宋体"}]{#struct_0_38774_20165_x731740924}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_1040769715}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_x1141613335}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_x1740013976}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1993745826}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1615963231}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_x1917501445}[关闭对象策略加速功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_x1305819100}

[\[Sysname\] object-policy ip a]{lang="EN-US"}

[\[Sysname-object-policy-ip-a\] undo accelerate]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1410739061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}]{#struct_0_38774_20165_886722171}[**[display object-policy accelerate]{lang="EN-US" style="color:windowtext;text-decoration:none"}**](#_display_object-policy_accelerate)
:::::

::: {#-1461383778 .myid}
[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc404793635}[]{#struct_0_38774_20165_357615554}[]{#_Toc357591517}[]{#_Toc350153659}

**对象策略 \-- 对象策略配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_38774_20165_x1371960782}[命令用来配置对象策略的描述信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_38774_20165_1641427147}[命令用来删除对象策略的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_446364742}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_38774_20165_2066378702}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_38774_20165_x1769758256}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_x2050969791}

[[对象策略没有任何描述信息。]{style="font-family:宋体"}]{#struct_0_38774_20165_x1946118440}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_1214773089}

[[对象策略视图]{style="font-family:宋体"}]{#struct_0_38774_20165_1870535768}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_1197904431}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_1956325873}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_x1001464276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_669839970}

[*[text]{lang="EN-US"}*]{#struct_0_38774_20165_x1920786159}[：表示对象策略的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1507131764}

[[使用]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_38774_20165_x945618657}[命令时，如果当前对象策略没有描述信息，则为其添加描述信息，否则修改其描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_2000729707}

[]{#struct_0_38774_20165_x567660355}[]{#_Toc252888206}[]{#_Toc253213276}[]{#_Toc253213622}[]{#_Toc252888207}[]{#_Toc253213277}[]{#_Toc253213623}[]{#_Toc252888210}[]{#_Toc253213280}[]{#_Toc253213626}[]{#_Toc252888212}[]{#_Toc253213282}[]{#_Toc253213628}[]{#_Toc252888213}[]{#_Toc253213283}[]{#_Toc253213629}[]{#_Toc139096874}[]{#_Toc139101656}[]{#_Toc139112024}[]{#_Toc140415830}[]{#_Toc140757796}[\# ]{lang="EN-US"}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略配置描述信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_1286414730}

[\[Sysname\] object-policy ip permit ]{lang="EN-US"}

[\[Sysname-object-policy-ip-permit\] description zone-pair security office to library]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1870470232}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display]{lang="EN-US"}**[ **object-policy ip**]{lang="EN-US"}]{#struct_0_38774_20165_20001924}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display]{lang="EN-US"}**[ **object-policy ipv6**]{lang="EN-US"}]{#struct_0_38774_20165_1419127445}
:::

::::: {#1390010454 .myid}
[]{#_Toc404793636}[]{#struct_0_38774_20165_x1670455344}[]{#_Toc384729396}[]{#_Toc374456824}[]{#_Toc374454046}[]{#_Toc373832987}

**对象策略 \-- 对象策略配置命令 \-- display object-policy accelerate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](对象策略命令.files/image001.png){#图片 3 border="0" width="62" height="26"}]{lang="EN-US"}]{#struct_0_38774_20165_420662304}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_38774_20165_1682414350}
:::

**[ ]{lang="EN-US"}**

[**[display object-policy]{lang="EN-US"}**[ **accelerate**]{lang="EN-US"}]{#struct_0_38774_20165_x1697035946}[命令用来显示对象策略的加速状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_445992432}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_38774_20165_2099395675}

[**[display object-policy accelerate]{lang="EN-US"}**[ { **summary** { **ip** \| **ipv6** } \| **verbose** { **ip** *object-policy-name* \| **ipv6** *object-policy-ipv6name* } }]{lang="EN-US"}]{#struct_0_38774_20165_398043479}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_38774_20165_1522024919}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display object-policy]{lang="EN-US"}**[ **accelerate** { **summary** { **ip \| ipv6** } \| **verbose** { **ip** *object-policy-name* \| **ipv6** *object-policy-name* } **slot** *slot-number* \[]{lang="EN-US"}]{#struct_0_38774_20165_1727291764}[[ ]{lang="EN-US" style="font-size:8.5pt;color:black"}]{.apple-converted-space}**[cpu]{lang="EN-US"}**[[ ]{lang="EN-US" style="font-size:8.5pt;color:black"}]{.apple-converted-space}*[cpu-number ]{lang="EN-US"}*[\] }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_38774_20165_x623990594}[模式：]{style="font-family:宋体"}

[**[display object-policy]{lang="EN-US"}**[ **accelerate** { **summary** { **ip** \| **ipv6** } \| **verbose** { **ip** *object-policy-name* \| **ipv6** *object-policy-name* } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu**]{lang="EN-US"}]{#struct_0_38774_20165_x1670914097}[[ ]{lang="EN-US" style="font-size:8.5pt;color:black"}]{.apple-converted-space}*[cpu-number ]{lang="EN-US"}*[\] }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_339742550}

[[任意视图]{style="font-family:宋体"}]{#struct_0_38774_20165_1033481856}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_1547542519}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_19028475}

[[network-operator]{lang="EN-US"}]{#struct_0_38774_20165_499151350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_1683351036}

[[mdc-operator]{lang="EN-US"}]{#struct_0_38774_20165_1073015852}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x971205925}

[**[summary]{lang="EN-US"}**]{#struct_0_38774_20165_1005215660}[：显示对象策略加速的概要信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_38774_20165_x1616352459}[：显示对象策略加速的详细信息。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_38774_20165_1075683253}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略的加速状态。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_29862235}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略的加速状态。]{style="font-family:宋体"}

[*[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x1501891913}[：指定]{style="font-family:宋体"}[对象策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_38774_20165_x1670979633}[：显示指定单板的]{style="font-family:宋体;
color:black"}[对象策略加速]{style="font-family:宋体"}[信息，该单板必须为加速芯片所在单板，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:
宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_38774_20165_889629654}[：显示指定成员设备的]{style="font-family:宋体;
color:black"}[对象策略加速]{style="font-family:宋体"}[信息，该设备必须为加速芯片所在成员设备，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_38774_20165_310336426}[：显示指定成员设备上指定单板的]{style="font-family:宋体;color:black"}[对象策略加速]{style="font-family:宋体"}[信息，该单板必须为加速芯片所在单板，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_38774_20165_x2062619283}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[对象策略加速]{style="font-family:宋体"}[信息，]{style="font-family:宋体;color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;
color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1389173900}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_1376437537}[显示加速状态的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display object-policy accelerate summary ip]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_38774_20165_x80643189}

[[Object-policy ip a]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_38774_20165_1953850884}

[[Object-policy ip c]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_38774_20165_x2808815}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_1609358028}[显示加速状态的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display object-policy accelerate verbose ip a]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_38774_20165_1574095074}

[[Object-policy ip a]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_38774_20165_x473263394}

[[ rule 1 drop]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_38774_20165_690321007}

[[ rule 0 pass (failed)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_38774_20165_792987174}

[[表1-1 ]{lang="EN-US"}[display object-policy accelerate verbose]{lang="EN-US"}]{#struct_0_38774_20165_x1671045169}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x999087111}[[字段]{style="font-family:黑体"}]{#struct_0_38774_20165_x114740659}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_38774_20165_1458557629}

[[failed]{lang="EN-US"}]{#struct_0_38774_20165_x1753353169}

[[表示此规则加速失败，匹配不生效]{style="font-family:宋体"}]{#struct_0_38774_20165_500436047}

[ ]{lang="EN-US"}

::: {#901412185 .myid}
[]{#_Toc404793637}[]{#struct_0_38774_20165_323058085}[]{#_Toc357591518}[]{#_Toc350153660}

**对象策略 \-- 对象策略配置命令 \-- display object-policy ip**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **object-policy ip**]{lang="EN-US"}]{#struct_0_38774_20165_x1216344837}[命令用来显示指定名称的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1473445310}

[**[display object-policy ip]{lang="EN-US"}**[ \[ *object-policy-name* \]]{lang="EN-US"}]{#struct_0_38774_20165_x1332277168}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1472567064}

[[任意视图]{style="font-family:宋体"}]{#struct_0_38774_20165_1180642730}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_1819184631}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_1104926577}

[[network-operator]{lang="EN-US"}]{#struct_0_38774_20165_1870404696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_1585710838}

[[mdc-operator]{lang="EN-US"}]{#struct_0_38774_20165_1297905421}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x705645227}

[*[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_1269774504}[表示对象策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。若未指定本参数，将显示所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略配置信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_x133552681}

[[本命令将按照实际匹配顺序即规则配置的先后顺序来排列对象策略内的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_x1446720590}[规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1068848050}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_x717147234}[显示所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display object-policy ip]{lang="EN-US"}]{#struct_0_38774_20165_x248953163}

[Object-policy ip pass]{lang="EN-US"}

[This is an IPv4 object policy for zone-pair security source office destination library]{lang="EN-US"}

[Object-policy accelerated]{lang="EN-US"}

[ rule 5 pass source-ip sourceip]{lang="EN-US"}

[ rule 5 comment This rule is used for source-ip sourceip]{lang="EN-US"}

[]{#struct_0_38774_20165_1870339160}[[表1-2 ]{lang="EN-US"}[display object-policy ip]{lang="EN-US"}]{#_Toc138129447}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_227864696}[[字段]{style="font-family:黑体"}]{#struct_0_38774_20165_x337437771}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_38774_20165_x1382120249}

[[Object-policy ip pass]{lang="EN-US"}]{#struct_0_38774_20165_59806969}

[[对象策略的名称]{style="font-family:宋体"}]{#struct_0_38774_20165_x707243923}

[[This is an IPv4 object policy for zone-pair security source office destination library]{lang="EN-US"}]{#struct_0_38774_20165_1152220194}

[[该对象策略的描述信息]{style="font-family:宋体"}]{#struct_0_38774_20165_x1700387510}

[[Object-policy accelerated]{lang="EN-US"}]{#struct_0_38774_20165_x1671110705}

[[该对象策略使能了加速功能]{style="font-family:宋体"}]{#struct_0_38774_20165_x1670651953}

[[rule 5 pass source-ip sourceip]{lang="EN-US"}]{#struct_0_38774_20165_x683634033}

[[规则]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_38774_20165_665458582}[的具体内容，]{style="font-family:宋体"}[sourceip]{lang="EN-US"}[为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组的名称]{style="font-family:宋体"}

[[rule 5 comment This rule is used for source-ip sourceip]{lang="EN-US"}]{#struct_0_38774_20165_1869749336}

[[规则]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_38774_20165_1697850161}[的描述信息]{style="font-family:宋体"}

::: {#-1037153372 .myid}
[]{#_Toc404793638}[]{#struct_0_38774_20165_2139903914}[]{#_Toc357591519}[]{#_Toc350153661}

**对象策略 \-- 对象策略配置命令 \-- display object-policy ipv6**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **object-policy ipv6**]{lang="EN-US"}]{#struct_0_38774_20165_76708843}[命令用来显示指定名称的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x517474568}

[**[display object-policy ipv6]{lang="EN-US"}**[ \[ *object-policy-name* \]]{lang="EN-US"}]{#struct_0_38774_20165_1078961422}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_2101526339}

[[任意视图]{style="font-family:宋体"}]{#struct_0_38774_20165_x760872769}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_306187003}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_x622376481}

[[network-operator]{lang="EN-US"}]{#struct_0_38774_20165_1390286808}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_1869683800}

[[mdc-operator]{lang="EN-US"}]{#struct_0_38774_20165_x1863143077}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1342473262}

[*[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x267080379}[表示对象策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。若未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略配置信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_1609310301}

[[本命令将按照实际匹配顺序即规则配置的先后顺序来排列对象策略内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_x746511348}[规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_204309965}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_x904113971}[显示所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display object-policy ipv6]{lang="EN-US"}]{#struct_0_38774_20165_x1641841601}

[Object-policy ipv6 pass]{lang="EN-US"}

[This is an IPv6 object policy for zone-pair security source office destination library]{lang="EN-US"}

[Object-policy accelerated]{lang="EN-US"}

[ rule 5 pass source-ip sourceipv6]{lang="EN-US"}

[ rule 5 comment This rule is used for source-ip sourceipv6]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display object-policy ipv6]{lang="EN-US"}]{#struct_0_38774_20165_1870273623}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_229659640}[[字段]{style="font-family:黑体"}]{#struct_0_38774_20165_1984276962}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_38774_20165_506814700}

[[Object-policy ipv6 pass]{lang="EN-US"}]{#struct_0_38774_20165_1919513318}

[[对象策略的名称]{style="font-family:宋体"}]{#struct_0_38774_20165_1679140530}

[[This is an IPv6 object policy for zone-pair security source office destination library]{lang="EN-US"}]{#struct_0_38774_20165_x1425918744}

[[该对象策略的描述信息]{style="font-family:宋体"}]{#struct_0_38774_20165_199277834}

[[Object-policy accelerated]{lang="EN-US"}]{#struct_0_38774_20165_x1670717489}

[[该对象策略使能了加速功能]{style="font-family:宋体"}]{#struct_0_38774_20165_1561023408}

[[rule 5 pass source-ip sourceipv6]{lang="EN-US"}]{#struct_0_38774_20165_1932637048}

[[规则]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_38774_20165_1439807236}[的具体内容，]{style="font-family:宋体"}[sourceipv6]{lang="EN-US"}[为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组的名称]{style="font-family:宋体"}

[[rule 5 comment This rule is used for source-ip sourceipv6]{lang="EN-US"}]{#struct_0_38774_20165_1870208087}

[[规则]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_38774_20165_50827369}[的描述信息]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ ]{lang="EN-US"}]{#_Toc350153662}

::: {#916342184 .myid}
[]{#_Toc404793639}[]{#struct_0_38774_20165_1870535767}

**对象策略 \-- 对象策略配置命令 \-- display object-policy statistics zone-pair security**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **object-policy statistics zone-pair security**]{lang="EN-US"}]{#struct_0_38774_20165_1197576751}[命令用来显示指定安全域间实例的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1938276035}

[**[display object-policy statistics ]{lang="EN-US"}[zone-pair security]{lang="EN-US"}**[ **source** *source-zone-name* **destination** *destination-zone-name* \[ **ip** \| **ipv6** \]]{lang="EN-US"}]{#struct_0_38774_20165_x1299726194}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_297766929}

[[任意视图]{style="font-family:宋体"}]{#struct_0_38774_20165_x1684074674}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_x260937628}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_x758099484}

[[network-operator]{lang="EN-US"}]{#struct_0_38774_20165_2126127577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_144487004}

[[mdc-operator]{lang="EN-US"}]{#struct_0_38774_20165_x856669486}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x126344432}

[*[source-zone-name]{lang="EN-US"}*]{#struct_0_38774_20165_1870470231}[：表示安全域间实例源安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}*[destination-zone-name]{lang="FR"}*[：表示安全域间实例目的安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_38774_20165_20198532}[：表示显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[对象策略的统计信息。]{style="font-family:宋体"}

[**[Ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_x968059090}[：表示显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1632178150}

[[如果不指定指定]{style="font-family:宋体"}**[ip]{lang="EN-US"}**]{#struct_0_38774_20165_x710372017}[或者]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[，则显示指定安全域间实例应用的所有对象策略的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1059722972}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_x184816420}[显示所有的安全域间实例应用对象策略的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display object-policy statistics zone-pair security source office destination library]{lang="EN-US"}]{#struct_0_38774_20165_x39309658}

[Object-policy apply ip OfficeToLibrary]{lang="EN-US"}

[ rule 0 pass source-ip sourceip1 (5 times matched)]{lang="EN-US"}

[ rule 1 drop source-ip sourceip2 (6 times matched)]{lang="EN-US"}

[Object-policy apply ipv6 OfficeToLibraryIPv6]{lang="EN-US"}

[ rule 0 pass source-ip sourceip3]{lang="EN-US"}

[ rule 1 drop source-ip sourceip4 (6 times matched)]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display object-policy statistics zone-pair security]{lang="EN-US"}]{#struct_0_38774_20165_x716763537}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_222678840}[[字段]{style="font-family:黑体"}]{#struct_0_38774_20165_1870404695}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_38774_20165_1585776374}

[[Object-policy apply ip OfficeToLibrary]{lang="EN-US"}]{#struct_0_38774_20165_2046451775}

[[安全域间实例应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_1602464883}[对象策略名称]{style="font-family:宋体"}

[[rule 0 pass source-ip sourceip1 ]{lang="EN-US"}]{#struct_0_38774_20165_103151065}

[[安全域间实例应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_876876917}[对象策略规则，]{style="font-family:宋体"}[sourceip1]{lang="EN-US"}[为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组的名称]{style="font-family:宋体"}

[[Object-policy apply ipv6 OfficeToLibraryIPv6]{lang="EN-US"}]{#struct_0_38774_20165_x228770545}

[[安全域间实例应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_1998848375}[对象策略名称]{style="font-family:宋体"}

[[rule 0 pass source-ip sourceip3]{lang="EN-US"}]{#struct_0_38774_20165_x1996770606}

[[安全域间实例应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_1870339159}[对象策略规则，]{style="font-family:宋体"}[sourceip3]{lang="EN-US"}[为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组的名称]{style="font-family:宋体"}

[[5 times matched]{lang="EN-US"}]{#struct_0_38774_20165_x336847948}

[[该规则匹配的次数为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_38774_20165_x2147252926}[（当匹配次数为]{style="font-family:宋体"}[0]{lang="EN-US"}[时不显示本字段）]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x2142461523}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[reset object-policy statistics]{lang="EN-US"}**]{#struct_0_38774_20165_x567274418}

::: {#-1379841826 .myid}
[]{#_Toc350153663}[]{#_Toc357591522}[]{#_Toc404793640}[]{#struct_0_38774_20165_x448835474}[]{#_Toc357591521}[]{#_Toc350957066}

**对象策略 \-- 对象策略配置命令 \-- display object-policy zone-pair security**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **object-policy zone-pair security**]{lang="EN-US"}]{#struct_0_38774_20165_x362171394}[命令用来显示指定安全域间实例应用对象策略的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x324037291}

[**[display object-policy ]{lang="EN-US"}[zone-pair security]{lang="EN-US"}**[ \[ **source** *source-zone-name* **destination** *destination-zone-name* \]]{lang="EN-US"}]{#struct_0_38774_20165_528255952}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_1775842964}

[[任意视图]{style="font-family:宋体"}]{#struct_0_38774_20165_x2120475334}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_790102682}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_165147544}

[[network-operator]{lang="EN-US"}]{#struct_0_38774_20165_1870142551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_x1157816797}

[[mdc-operator]{lang="EN-US"}]{#struct_0_38774_20165_141489065}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_1372652576}

[*[source-zone-name]{lang="EN-US"}*]{#struct_0_38774_20165_x1728963084}[：表示安全域间实例源安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}*[destination-zone-name]{lang="FR"}*[：表示安全域间实例目的安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}

[[若未指定安全域间实例，将显示所有安全域间实例应用对象策略的配置信息。]{style="font-family:宋体"}]{#struct_0_38774_20165_x1199861694}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_965249519}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_1594293030}[显示所有的安全域间实例应用对象策略的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display object-policy zone-pair security]{lang="EN-US"}]{#struct_0_38774_20165_x560202980}

[Zone-pair source office destination library]{lang="EN-US"}

[object-policy apply ip permit]{lang="EN-US"}

[object-policy apply ipv6 drop]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display object-policy zone-pair security]{lang="EN-US"}]{#struct_0_38774_20165_84412879}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_229455736}[[字段]{style="font-family:黑体"}]{#struct_0_38774_20165_1870077015}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_38774_20165_1161788429}

[[Zone-pair source office destination library]{lang="EN-US"}]{#struct_0_38774_20165_x1955811691}

[[安全域间实例]{style="font-family:宋体"}]{#struct_0_38774_20165_1532158004}

[[object-policy apply ip permit]{lang="EN-US"}]{#struct_0_38774_20165_607500755}

[[安全域间实例应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_413490822}[对象策略配置信息]{style="font-family:宋体"}

[[object-policy apply ipv6 drop]{lang="EN-US"}]{#struct_0_38774_20165_772711337}

[[安全域间实例应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_1286961164}[对象策略配置信息]{style="font-family:宋体"}

::: {#7642594 .myid}
[]{#_Toc404793641}[]{#struct_0_38774_20165_1266676494}

**对象策略 \-- 对象策略配置命令 \-- move rule**

------------------------------------------------------------------------

[**[move rule]{lang="EN-US"}**]{#struct_0_38774_20165_x779808973}[命令用来移动对象策略规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_293625385}

[**[move]{lang="EN-US"}**[ **rule** *rule-id* **before** *insert-rule-id*]{lang="EN-US"}]{#struct_0_38774_20165_x1537901328}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_1869749335}

[[对象策略视图]{style="font-family:宋体"}]{#struct_0_38774_20165_1697915697}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1375750819}

[*[rule-id]{lang="EN-US"}*]{#struct_0_38774_20165_585122484}[：指定待移动的对象策略规则编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[insert-rule-id]{lang="EN-US"}*]{#struct_0_38774_20165_1912160735}[：表示移动到指定编号的规则之前，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，其中指定编号为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示移动到所有规则之后。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1030683387}

[[如果]{style="font-family:宋体"}*[insert-rule-id]{lang="EN-US"}*]{#struct_0_38774_20165_x360939593}[与]{style="font-family:宋体"}*[rule-id]{lang="EN-US"}*[相同或其指定的规则不存在，则不执行任何移动操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x2103905931}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_x1416684687}[在]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略]{style="font-family:宋体"}[permit]{lang="EN-US"}[上，将对象策略规则]{style="font-family:宋体"}[5]{lang="EN-US"}[移动到规则]{style="font-family:宋体"}[2]{lang="EN-US"}[之前。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_x1591411390}

[\[Sysname\] object-policy ip permit]{lang="EN-US"}

[\[Sysname-object-policy-ip-permit\] move rule 5 before 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_468050651}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy ip]{lang="EN-US"}**]{#struct_0_38774_20165_1869683799}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy apply ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_x1819102878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[rule(ipv4 object-policy view)]{lang="EN-US"}**]{#struct_0_38774_20165_1756133584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[rule(ipv6 object-policy view)]{lang="EN-US"}**]{#struct_0_38774_20165_x439564520}
:::

::: {#-1911173542 .myid}
[]{#_Toc404793642}[]{#struct_0_38774_20165_1246498822}[]{#_Toc357591523}

**对象策略 \-- 对象策略配置命令 \-- object-policy apply ip**

------------------------------------------------------------------------

[**[object-policy apply ip]{lang="EN-US"}**]{#struct_0_38774_20165_x1642076116}[命令用来在安全域间实例内应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **object-policy apply ip**]{lang="EN-US"}]{#struct_0_38774_20165_x735871355}[命令用来在安全域间实例内取消应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_749956728}

[**[object-policy apply ip ]{lang="EN-US"}***[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x264850649}

[**[undo object-policy apply ip ]{lang="EN-US"}***[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x627367484}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_1145998451}

[[安全域间实例内不应用任何]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_1870273622}[对象策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_1984211426}

[[安全域间实例视图]{style="font-family:宋体"}]{#struct_0_38774_20165_2031021133}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_483365890}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_x1491688010}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_x659769996}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1217781009}

[*[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x801582127}[：指定对象策略的名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_1544882187}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[object-policy apply ip]{lang="EN-US"}**]{#struct_0_38774_20165_82139551}[时，对应的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略必须已经创建，否则将配置失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[每个安全域间实例只能应用一个]{style="font-family:宋体"}]{#struct_0_38774_20165_x1338616823}[IPv4]{lang="EN-US"}[对象策略。如果使用]{style="font-family:宋体"}**[object-policy apply ip]{lang="EN-US"}**[时对应安全域间实例已经应用其他]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[策略，则会配置失败。若要应用新的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略，需要先将已经应用的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略删掉。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1850116252}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_1870208086}[创建]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略，并将该对象策略应用于一个安全域间实例中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_50892905}

[\[Sysname\] object-policy ip permit]{lang="EN-US"}

[\[Sysname-object-policy-ip-permit\]quit]{lang="EN-US"}

[\[Sysname\] zone-pair security source office destination library]{lang="EN-US"}

[\[Sysname-zone-pair-security-office-library\] object-policy apply ip permit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_687957811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy ip]{lang="EN-US"}**]{#struct_0_38774_20165_x110136860}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy apply ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_180140874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display object-policy ]{lang="EN-US"}[zone-pair security]{lang="EN-US"}**]{#struct_0_38774_20165_x1627600838}
:::

::: {#1279895995 .myid}
[]{#_Toc404793643}[]{#struct_0_38774_20165_1620059656}[]{#_Toc357591524}[]{#_Toc350153664}

**对象策略 \-- 对象策略配置命令 \-- object-policy apply ipv6**

------------------------------------------------------------------------

[**[object-policy apply ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_688868695}[命令用来在安全域间实例内应用]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[对象策略。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **object-policy apply ipv6**]{lang="EN-US"}]{#struct_0_38774_20165_366952954}[命令用来在安全域间实例内取消应用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x364700811}

[**[object-policy apply ipv6 ]{lang="EN-US"}***[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_1870142550}

[**[undo object-policy apply ipv6 ]{lang="EN-US"}***[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x1157751261}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_x286863558}

[[安全域间实例内不应用任何]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_x1254960946}[对象策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1012312493}

[[安全域间实例视图]{style="font-family:宋体"}]{#struct_0_38774_20165_x569157619}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_1839419644}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_408175824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_x1485718016}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x42675247}

[*[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_1625221808}[：指定对象策略的名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_1870077014}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[object-policy apply ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_1161722893}[时，对应的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略必须已经创建，否则将配置失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[每个安全域间实例只能应用一个]{style="font-family:宋体"}]{#struct_0_38774_20165_x1180222310}[IPv6]{lang="EN-US"}[对象策略。如果使用]{style="font-family:宋体"}**[object-policy apply ipv6]{lang="EN-US"}**[时对应安全域间实例已经应用其他]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[策略，则会配置失败。若要应用新的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略，需要先将已经应用的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略删掉。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x743139755}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_421997112}[创建]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略，并将该对象策略应用于一个安全域间实例中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_2023324224}

[\[Sysname\] object-policy ipv6 permit]{lang="EN-US"}

[\[Sysname-object-policy-ipv6-permit\]quit]{lang="EN-US"}

[\[Sysname\] zone-pair security source office destination library]{lang="EN-US"}

[\[Sysname-zone-pair-security-office-library\] object-policy apply ipv6 permit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1806980178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_x1186192698}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy apply ip]{lang="EN-US"}**]{#struct_0_38774_20165_468672823}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display object-policy ]{lang="EN-US"}[zone-pair security]{lang="EN-US"}**]{#struct_0_38774_20165_x1883783686}
:::

::: {#893529347 .myid}
[]{#_Toc404793644}[]{#struct_0_38774_20165_1870535766}[]{#_Toc357591525}[]{#_Toc350153665}

**对象策略 \-- 对象策略配置命令 \-- object-policy ip**

------------------------------------------------------------------------

[**[object-policy ip]{lang="EN-US"}**]{#struct_0_38774_20165_1197511215}[命令用来创建一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略，并进入相应的对象策略视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **object-policy ip**]{lang="EN-US"}]{#struct_0_38774_20165_1572922224}[命令用来删除指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1233788183}

[**[object-policy ip ]{lang="EN-US"}***[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x614418038}

[**[undo object-policy ip ]{lang="EN-US"}***[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_1220573047}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1379692278}

[[不存在任何]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_x693003529}[对象策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1528903823}

[[系统视图]{style="font-family:宋体"}]{#struct_0_38774_20165_x365801333}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_347379300}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_x906518205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_1870470230}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_20132996}

[*[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x582933182}[：指定对象策略的名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_1388892347}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_38774_20165_x465793736}**[object-policy ip]{lang="EN-US"}**[时，如果指定名称的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略不存在，则创建该对象策略，并进入其视图，否则直接进入其视图。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_x1972207813}[对象策略的名称只能在创建时设置。对象策略一旦创建，便不允许再修改其原有名称。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo object-policy ip]{lang="EN-US"}**]{#struct_0_38774_20165_x1308476426}[时，必须保证无安全域间实例应用指定]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略，否则，将删除失败。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_1878383613}

[[\#]{lang="EN-US"}]{#struct_0_38774_20165_x887576122}[创建一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_x1383911937}

[\[Sysname\] object-policy ip permit]{lang="EN-US"}

[\[Sysname-object-policy-ip-permit\] rule pass]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1870404694}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_1585841910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display object-policy]{lang="EN-US"}**]{#struct_0_38774_20165_1702619909}**[ ip]{lang="EN-US"}**
:::

::: {#298658608 .myid}
[]{#_Toc404793645}[]{#struct_0_38774_20165_x1322107622}[]{#_Toc357591526}[]{#_Toc350153666}

**对象策略 \-- 对象策略配置命令 \-- object-policy ipv6**

------------------------------------------------------------------------

[**[object-policy ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_510566002}[命令用来创建一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略，并进入相应的对象策略视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **object-policy ipv6**]{lang="EN-US"}]{#struct_0_38774_20165_556864426}[命令用来删除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1462507003}

[**[object-policy ipv6 ]{lang="EN-US"}***[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_512000870}

[**[undo object-policy ipv6 ]{lang="EN-US"}***[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_507168692}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_295493737}

[[不存在任何]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_1054402307}[对象策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_1523006295}

[[系统视图]{style="font-family:宋体"}]{#struct_0_38774_20165_1870339158}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_x336913484}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_118970267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_x1858826782}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_1938713495}

[*[object-policy-name]{lang="EN-US"}*]{#struct_0_38774_20165_x165246642}[：指定对象策略的名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_49011776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_38774_20165_x940871334}**[object-policy ipv6]{lang="EN-US"}**[时，如果指定名称的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略不存在，则创建该对象策略，并进入其视图，否则直接进入其视图。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_x434665874}[对象策略的名称只能在创建时设置。对象策略一旦创建，便不允许再修改其原有名称。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo object-policy ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_x1558012977}[时，必须保证无安全域间实例应用指定]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略，否则，将删除失败。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x403392938}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_1869749334}[创建一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_1697981233}

[\[Sysname\] object-policy ipv6 permit ]{lang="EN-US"}

[\[Sysname-object-policy-ipv6-permit\] rule pass]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1337123563}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy ip]{lang="EN-US"}**]{#struct_0_38774_20165_1332185497}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display object-policy]{lang="EN-US"}**]{#struct_0_38774_20165_x1149579794}**[ ipv6]{lang="EN-US"}**
:::

::: {#1345481637 .myid}
[]{#_Toc350153667}[]{#_Toc404793646}[]{#struct_0_38774_20165_1499464669}[]{#_Toc357591527}

**对象策略 \-- 对象策略配置命令 \-- reset object-policy statistics**

------------------------------------------------------------------------

[**[reset object-policy statistics]{lang="EN-US"}**]{#struct_0_38774_20165_x1430246765}[命令用来清除对象策略在安全域间实例中的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1943776219}

[**[reset]{lang="EN-US"}**[ **object-policy** **statistics** \[ **zone-pair security** **source** *source-zone-name* **destination** *destination-zone-name* \] \[ **ip** \| **ipv6** \]]{lang="EN-US"}]{#struct_0_38774_20165_798747967}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_809118916}

[[用户视图]{style="font-family:宋体"}]{#struct_0_38774_20165_x1347462936}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_1869683798}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_x1819037342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_1242224666}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_606433710}

[*[source-zone-name]{lang="EN-US"}*]{#struct_0_38774_20165_x896178719}[：表示安全域间实例源安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}*[destination-zone-name]{lang="FR"}*[：表示安全域间实例目的安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_38774_20165_x853966645}[：表示清除]{style="font-family:宋体"}[IP]{lang="EN-US"}[对象策略的统计信息。]{style="font-family:宋体"}

[**[Ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_x1376176312}[：表示清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_1157517399}

[[若未指定]{style="font-family:宋体"}]{#struct_0_38774_20165_1216148538}[安全]{style="font-family:宋体"}[域间实例，则清除所有]{style="font-family:宋体"}[安全]{style="font-family:宋体"}[域间实例指定类型对象策略的统计信息。若未指定]{style="font-family:宋体"}**[ip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}[，]{style="font-family:宋体"}**[则清除所有类型对象策略的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_575580637}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_x277457151}[清除]{style="font-family:宋体"}[指定安全域间实例的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset object-policy statistics zone-pair security source office destination library ip]{lang="EN-US"}]{#struct_0_38774_20165_x858609728}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_910238470}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display]{lang="EN-US"}**]{#struct_0_38774_20165_x520940415}**[ object-policy]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}**[ ]{lang="EN-US"}[zone-pair security]{lang="EN-US"}**
:::

::: {#1031359485 .myid}
[]{#_Toc404793647}[]{#struct_0_38774_20165_x858544192}[]{#_Toc357591530}[]{#_Toc350153669}

**对象策略 \-- 对象策略配置命令 \-- rule comment**

------------------------------------------------------------------------

[**[rule]{lang="EN-US"}**[ **comment**]{lang="EN-US"}]{#struct_0_38774_20165_2097094663}[命令用来为指定规则配置描述信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule** **comment**]{lang="EN-US"}]{#struct_0_38774_20165_1764564638}[命令用来删除指定规则的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1193289109}

[**[rule]{lang="EN-US"}**[ *rule-id* **comment** *text*]{lang="EN-US"}]{#struct_0_38774_20165_x1285734532}

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* **comment**]{lang="EN-US"}]{#struct_0_38774_20165_x317259094}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_x376765905}

[[规则没有任何描述信息。]{style="font-family:宋体"}]{#struct_0_38774_20165_773021811}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1767202773}

[[对象策略视图]{style="font-family:宋体"}]{#struct_0_38774_20165_x840581976}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1354005043}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_330735386}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_x859134016}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_551296923}

[*[rule-id]{lang="EN-US"}*]{#struct_0_38774_20165_x1449450665}[：指定规则的编号，该规则必须存在。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[text]{lang="EN-US"}*]{#struct_0_38774_20165_x1968345764}[：表示规则的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_1203829226}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_38774_20165_x1224131497}**[rule]{lang="EN-US"}**[ **comment**]{lang="EN-US"}[命令时，指定的规则必须已经创建，如果没有创建，则会配置失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ **comment**]{lang="EN-US"}]{#struct_0_38774_20165_1021266383}[命令时，如果指定的规则没有描述信息，则为其添加描述信息，否则修改其描述信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_1119177444}

[]{#struct_0_38774_20165_392460709}[]{#_Toc252888219}[]{#_Toc253213289}[]{#_Toc253213635}[]{#_Toc252888220}[]{#_Toc253213290}[]{#_Toc253213636}[]{#_Toc252888222}[]{#_Toc253213292}[]{#_Toc253213638}[]{#_Toc252888223}[]{#_Toc253213293}[]{#_Toc253213639}[]{#_Toc252888224}[]{#_Toc253213294}[]{#_Toc253213640}[]{#_Toc252888226}[]{#_Toc253213296}[]{#_Toc253213642}[]{#_Toc252888227}[]{#_Toc253213297}[]{#_Toc253213643}[]{#_Toc252888228}[]{#_Toc253213298}[]{#_Toc253213644}[\# ]{lang="EN-US"}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略配置规则]{style="font-family:宋体"}[0]{lang="EN-US"}[，并为该规则配置描述信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_1562687228}

[\[Sysname\] object-policy ip permit]{lang="EN-US"}

[\[Sysname-object-policy-ip-permit\] rule 0 pass source-ip ip1]{lang="EN-US"}

[\[Sysname-object-policy-ip-permit\] rule 0 comment This rule is used for source-ip ip1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x859199552}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display]{lang="EN-US"}**[ **object-policy ip**]{lang="EN-US"}]{#struct_0_38774_20165_1717510720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display]{lang="EN-US"}**[ **object-policy ipv6**]{lang="EN-US"}]{#struct_0_38774_20165_x1784150909}
:::

::: {#869475701 .myid}
[]{#_Toc404793648}[]{#struct_0_38774_20165_x2078735941}[]{#_Toc357591528}

**对象策略 \-- 对象策略配置命令 \-- rule(ipv4 object-policy view)**

------------------------------------------------------------------------

[**[rule]{lang="EN-US"}**]{#struct_0_38774_20165_x111690269}[命令用来创建一条]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_38774_20165_1691865825}[命令用来删除一条]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略规则或删除规则中的部分内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_1749071223}

[**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **drop** \| **pass** } \[ \[ **source-ip** { *object-group-name* \| **any ** } \] \[ **destination-ip** { *object-group-name \|* **any** } \] \[ **service** { *object-group-name* \| **any** } \] \[ **vrf** *vrf-name* \] \[ **counting** \] \[ **disable** \] \[ **logging** \] \[ **time-range** *time-range-name* \] \] ]{lang="EN-US"}]{#struct_0_38774_20165_x763578254}*[\*]{lang="EN-US" style="font-size:8.5pt"}*

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* \[ **source-ip** *\|* **destination-ip** *\|* **service** *\|* **vrf** \| **counting** \|**disable** \| **logging** \| **time-range** \] ]{lang="EN-US"}]{#struct_0_38774_20165_x1734706097}*[\*]{lang="EN-US" style="font-size:8.5pt"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_x842965323}

[[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_x1528384544}[对象策略内不存在任何规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_203198845}

[[IPv4]{lang="EN-US"}]{#struct_0_38774_20165_x858675264}[对象策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_944090054}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_175268555}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_652271044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1825237681}

[*[rule-id]{lang="EN-US"}*]{#struct_0_38774_20165_x1606524162}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略规则的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。若未指定本参数，]{style="font-family:宋体"}[系统将从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，自动分配一个大于现有最大编号的最小编号]{style="font-family:宋体"}[，步长为]{style="font-family:宋体"}[1]{lang="EN-US"}[。若新编号超出了编号上限（]{style="font-family:宋体"}[65534]{lang="EN-US"}[），则选择当前未使用的最小编号作为新的编号。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_38774_20165_x1160461278}[：表示丢弃符合条件的报文。]{style="font-family:宋体"}

[**[pass]{lang="EN-US"}**]{#struct_0_38774_20165_x1906997755}[：表示允许符合条件的报文。]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}***[ object-group-name]{lang="EN-US"}*]{#struct_0_38774_20165_671903871}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组的名称。]{style="font-family:宋体"}*[object-group-name]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示任意源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}***[ object-group-name]{lang="EN-US"}*]{#struct_0_38774_20165_x68449162}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组的名称。]{style="font-family:宋体"}*[object-group-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示任意目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组。]{style="font-family:宋体"}

[**[service]{lang="EN-US"}***[ object-group-name]{lang="EN-US"}*]{#struct_0_38774_20165_914078086}[：指定服务对象组的名称。]{style="font-family:宋体"}*[object-group-name]{lang="EN-US"}*[表示服务对象组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示任意服务对象组。]{style="font-family:宋体"}

[**[vrf]{lang="EN-US"}**[ *vrf-name*]{lang="EN-US"}]{#struct_0_38774_20165_x858740800}[：表示对指定]{style="font-family:宋体"}[VRF]{lang="EN-US"}[中的报文有效。]{style="font-family:宋体"}*[vrf]{lang="EN-US"}[-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VRF]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若未指定本参数，表示该规则仅对公网报文有效。]{style="font-family:宋体"}

[**[counting]{lang="EN-US"}**]{#struct_0_38774_20165_x1746623900}[：表示使能当前]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略规则匹配统计功能，缺省为关闭。]{style="font-family:宋体"}

[**[disable]{lang="EN-US"}**]{#struct_0_38774_20165_x681446740}[：表示关闭当前]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略规则。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_38774_20165_815017507}[：表示对符合条件的报文记录日志信息。]{style="font-family:宋体"}

[**[time-range]{lang="EN-US"}**[ *time-range-name*]{lang="EN-US"}]{#struct_0_38774_20165_x785057865}[：指定本规则生效的时间段。]{style="font-family:宋体"}*[time-range-name]{lang="EN-US"}*[表示时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"时间段"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_744464852}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_38774_20165_x1689924092}**[rule]{lang="EN-US"}**[命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[创建规则时可以不指定任何对象，则规则对任意报文生效。]{style="font-family:宋体"}]{#struct_0_38774_20165_2128725062}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[创建规则时，若指定的对象组不存在，该规则仍会成功创建，但不会匹配任何报文。]{style="font-family:宋体"}]{#struct_0_38774_20165_771606901}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_38774_20165_x1464919076}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}[命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_38774_20165_2125154443}[命令时必须指定一个已存在规则的编号，可以使用]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}**[ **object-policy**]{lang="EN-US"}[命令来查看当前对象策略所有已存在的规则。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1293855602}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_x1209752333}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对象策略创建规则如下：允许源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组]{style="font-family:宋体"}[sourceip1]{lang="EN-US"}[对应的报文在时间段]{style="font-family:宋体"}[time1]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_x858806336}

[\[Sysname\] object-policy ip permit]{lang="EN-US"}

[\[Sysname-object-policy-ip-permit\] rule pass source-ip sourceip1 logging time-range time1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_558774124}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy ip]{lang="EN-US"}**]{#struct_0_38774_20165_1157946291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display]{lang="EN-US"}**[ **object-policy**]{lang="EN-US"}]{#struct_0_38774_20165_1987078225}**[ ip]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[move rule]{lang="EN-US"}**]{#struct_0_38774_20165_x1152265572}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[time-range]{lang="EN-US"}**]{#struct_0_38774_20165_x786885554}
:::

::: {#259044407 .myid}
[]{#_Toc404793649}[]{#struct_0_38774_20165_1759022193}[]{#_Toc357591529}[]{#_Toc350153668}

**对象策略 \-- 对象策略配置命令 \-- rule(ipv6 object-policy view)**

------------------------------------------------------------------------

[**[rule]{lang="EN-US"}**]{#struct_0_38774_20165_x1764541485}[命令用来创建一条]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_38774_20165_x147488820}[命令用来删除一条]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略规则或删除规则中的部分内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_2135733800}

[**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **drop** \| **pass** } \[ \[ **source-ip** { *object-group-name* \| **any** } \] \[ **destination-ip** { *object-group-name* \| **any** } \] \[ **service** { *object-group-name* \| **any** } \] \[**vrf** *vrf-name* \] \[ **counting** \] \[ **disable** \] \[ **logging** \] \[ **time-range** *time-range-name* \] \] ]{lang="EN-US"}]{#struct_0_38774_20165_x1511490282}*[\*]{lang="EN-US" style="font-size:8.5pt"}*

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* \[ **source-ip** *\|* **destination-ip** *\|* **service** *\|* **vrf** *\|* **counting** \| **disable** \| **logging** \| **time-range** \] ]{lang="EN-US"}]{#struct_0_38774_20165_x858347584}*[\*]{lang="EN-US" style="font-size:8.5pt"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_38774_20165_1735574003}

[[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_x1185005045}[对象策略内不存在任何规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_38774_20165_x492418754}

[[IPv6]{lang="EN-US"}]{#struct_0_38774_20165_598376784}[对象策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_38774_20165_1412416738}

[[network-admin]{lang="EN-US"}]{#struct_0_38774_20165_x437588520}

[[mdc-admin]{lang="EN-US"}]{#struct_0_38774_20165_x992639158}

[[【参数】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1168372489}

[*[rule-id]{lang="EN-US"}*]{#struct_0_38774_20165_x609543481}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略规则的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。若未指定本参数，]{style="font-family:宋体"}[系统将从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，自动分配一个大于现有最大编号的最小编号]{style="font-family:宋体"}[，步长为]{style="font-family:宋体"}[1]{lang="EN-US"}[。若新编号超出了编号上限（]{style="font-family:宋体"}[65534]{lang="EN-US"}[），则选择当前未使用的最小编号作为新的编号。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_38774_20165_2021751983}[：表示丢弃符合条件的报文。]{style="font-family:宋体"}

[**[pass]{lang="EN-US"}**]{#struct_0_38774_20165_x858413120}[：表示允许符合条件的报文。]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}***[ object-group-name]{lang="EN-US"}*]{#struct_0_38774_20165_544052410}[：指定源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组的名称。]{style="font-family:宋体"}*[object-group-name]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示任意源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}***[ object-group-name]{lang="EN-US"}*]{#struct_0_38774_20165_x1389993781}[：指定目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组的名称。]{style="font-family:宋体"}*[object-group-name]{lang="EN-US"}*[表示目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示任意目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组。]{style="font-family:宋体"}

[**[service]{lang="EN-US"}***[ object-group-name]{lang="EN-US"}*]{#struct_0_38774_20165_1514119238}[：指定服务对象组的名称。]{style="font-family:宋体"}*[object-group-name]{lang="EN-US"}*[表示服务对象组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示任意服务对象组。]{style="font-family:宋体"}

[**[vrf]{lang="EN-US"}**[ *vrf-name*]{lang="EN-US"}]{#struct_0_38774_20165_x1962003133}[：表示对指定]{style="font-family:宋体"}[VRF]{lang="EN-US"}[中的报文有效。]{style="font-family:宋体"}*[vrf]{lang="EN-US"}[-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VRF]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若未指定本参数，表示该规则仅对公网报文有效。]{style="font-family:宋体"}

[**[counting]{lang="EN-US"}**]{#struct_0_38774_20165_x1746492827}[：表示使能当前]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略规则匹配统计功能，缺省为关闭。]{style="font-family:宋体"}

[**[disable]{lang="EN-US"}**]{#struct_0_38774_20165_1540701181}[：表示关闭当前]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略规则。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_38774_20165_x832718825}[：表示对符合条件的报文记录日志信息。]{style="font-family:宋体"}

[**[time-range]{lang="EN-US"}**[ *time-range-name*]{lang="EN-US"}]{#struct_0_38774_20165_72451984}[：指定本规则生效的时间段。]{style="font-family:宋体"}*[time-range-name]{lang="EN-US"}*[表示时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"时间段"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_38774_20165_923129900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_38774_20165_x1273470174}**[rule]{lang="EN-US"}**[命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[创建规则时可以不指定任何对象，则规则对任意报文生效。]{style="font-family:宋体"}]{#struct_0_38774_20165_x1174573603}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[创建规则时，若指定的对象组不存在，该规则仍会成功创建，但不会匹配任何报文。]{style="font-family:宋体"}]{#struct_0_38774_20165_x858478656}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_38774_20165_1295030116}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}[命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_38774_20165_x2141890388}[命令时必须指定一个已存在规则的编号，可以使用]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}**[ **object-policy**]{lang="EN-US"}**[ ipv6]{lang="EN-US"}**[命令来查看当前对象策略所有已存在的规则。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_38774_20165_1749442671}

[[\# ]{lang="EN-US"}]{#struct_0_38774_20165_x1116382694}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对象策略创建规则如下：允许源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址对象组]{style="font-family:宋体"}[sourceip1]{lang="EN-US"}[对应的报文在时间段]{style="font-family:宋体"}[time1]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_38774_20165_372184286}

[\[Sysname\] object-policy ipv6 permit]{lang="EN-US"}

[\[Sysname-object-policy-ipv6-permit\] rule pass source-ip sourceip1 logging time-range time1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_38774_20165_x1060105435}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[object-policy ipv6]{lang="EN-US"}**]{#struct_0_38774_20165_x1479101323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display]{lang="EN-US"}**[ **object-policy**]{lang="EN-US"}]{#struct_0_38774_20165_x864043933}**[ ipv6]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[move rule]{lang="EN-US"}**]{#struct_0_38774_20165_37846578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[time-range]{lang="EN-US"}**]{#struct_0_38774_20165_189580614}
:::
