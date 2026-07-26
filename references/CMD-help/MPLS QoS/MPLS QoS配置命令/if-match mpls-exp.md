::: {#954979773 .myid}
[]{#_Toc404791985}[]{#struct_0_x1935_x3534_x1381939850}[]{#_Toc224962637}[]{#_Toc198110227}[]{#_Toc115171271}[]{#_Toc81455655}[]{#_Toc56569712}[]{#_Toc41626807}

**MPLS QoS \-- MPLS QoS配置命令 \-- if-match mpls-exp**

------------------------------------------------------------------------

[**[if-match mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_x544218092}[命令用来定义匹配]{style="font-family:宋体"}[第一层]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级的规则。]{style="font-family:宋体"}

[**[undo if-match mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_x719800964}[命令用来删除匹配]{style="font-family:宋体"}[第一层]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级的规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_1496371998}

[**[if-match ]{lang="EN-US"}**[\[ **not** \] **mpls-exp** *exp-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_x1935_x3534_x432181185}

[**[undo if-match ]{lang="EN-US"}**[\[ **not** \] **mpls-exp** *exp-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_x1935_x3534_44330349}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x781831601}

[[没有定义匹配]{style="font-family:宋体"}]{#struct_0_x1935_x3534_195607048}[第一层]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级的规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_2044208393}

[[类视图]{style="font-family:宋体"}]{#struct_0_x1935_x3534_1737808884}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x984106766}

[[network-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_x1876021865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_x1914821543}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x1831832652}

[**[not]{lang="EN-US"}**]{#struct_0_x1935_x3534_x431198145}[：不匹配该规则。]{style="font-family:宋体"}

[*[exp-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1935_x3534_x1026717980}[：]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值的列表，]{style="font-family:宋体"}[EXP]{lang="EN-US"}[优先级的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:
宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:
宋体"}[8]{lang="EN-US"}[次。如果指定了多个相同的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x1596732009}

[[\# ]{lang="EN-US"}]{#struct_0_x1935_x3534_x2026568728}[定义匹配第一层]{style="font-family:宋体"}[EXP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[或]{style="font-family:宋体"}[4]{lang="EN-US"}[的报文的规则。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1935_x3534_1067078564}

[\[Sysname\] traffic classifier database]{lang="EN-US"}

[\[Sysname-classifier-database\] if-match mpls-exp 3 4]{lang="EN-US"}
:::

::: {#1537121915 .myid}
[]{#_Toc115171272}[]{#_Toc81455656}[]{#_Toc56569713}[]{#_Toc41626808}[]{#_Toc404791986}[]{#struct_0_x1935_x3534_1015066362}[]{#_Toc224962638}[]{#_Toc198110228}

**MPLS QoS \-- MPLS QoS配置命令 \-- if-match mpls-label**

------------------------------------------------------------------------

[**[if-match mpls-label]{lang="PT-BR"}**]{#struct_0_x1935_x3534_1271721569}[命令用来定义匹配]{style="font-family:宋体"}[第一层]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[的规则。]{style="font-family:宋体"}

[**[undo if-match mpls-label]{lang="PT-BR"}**]{#struct_0_x1935_x3534_x980697071}[命令用来删除匹配]{style="font-family:
宋体"}[第一层]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[的规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_1910416126}

[**[if-match ]{lang="EN-US"}**[\[ **not** \] **mpls-label** { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]{lang="EN-US"}]{#struct_0_x1935_x3534_x431263681}

[**[undo if-match ]{lang="EN-US"}**[\[ **not** \] **mpls-label** { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]{lang="EN-US"}]{#struct_0_x1935_x3534_x969451900}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x1301244449}

[[没有定义匹配]{style="font-family:宋体"}]{#struct_0_x1935_x3534_x1132286236}[第一层]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[的规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x536663360}

[[类视图]{style="font-family:宋体"}]{#struct_0_x1935_x3534_1952143217}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_1526056738}

[[network-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_1804946092}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_1641679874}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_812145921}

[**[not]{lang="EN-US"}**]{#struct_0_x1935_x3534_x431722432}[：不匹配该规则。]{style="font-family:宋体"}

[*[label-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1935_x3534_1368640495}[：]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[值的列表，]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签值]{style="font-family:宋体"}[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[label-value1]{lang="EN-US"}*[ **to** *label-value2*]{lang="EN-US"}]{#struct_0_x1935_x3534_x1099738223}[：]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[值的范围，]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}*[的值必须小于]{style="font-family:宋体"}*[label-value2]{lang="EN-US"}*[的值，]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签值]{style="font-family:宋体"}[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_229514124}

[[如果指定了多个相同的]{style="font-family:宋体"}]{#struct_0_x1935_x3534_2131220268}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_1436551250}

[[\# ]{lang="EN-US"}]{#struct_0_x1935_x3534_x1345871910}[定义匹配]{style="font-family:宋体"}[第一层]{style="font-family:
宋体"}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:
宋体"}[1000]{lang="EN-US"}[的报文的规则。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1935_x3534_x1705851747}

[\[Sysname\] traffic classifier database]{lang="EN-US"}

[\[Sysname-classifier-database\] if-match mpls-label 1 to 1000]{lang="EN-US"}
:::

::: {#-1192731450 .myid}
[]{#_Toc404791987}[]{#struct_0_x1935_x3534_x431787968}[]{#_Toc224962639}[]{#_Toc198110229}

**MPLS QoS \-- MPLS QoS配置命令 \-- if-match second-mpls-exp**

------------------------------------------------------------------------

[**[if-match second-mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_1780843747}[命令用来定义匹配第二层]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[的]{style="font-family:
宋体"}[EXP]{lang="EN-US"}[域的规则。]{style="font-family:宋体"}

[**[undo if-match second-mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_x174652974}[命令用来删除匹配第二层]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[的]{style="font-family:
宋体"}[EXP]{lang="EN-US"}[域的规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x2100827144}

[**[if-match ]{lang="EN-US"}**[\[ **not** \] **second-mpls-exp** *exp-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_x1935_x3534_x1623735321}

[**[undo if-match ]{lang="EN-US"}**[\[ **not** \] **second-mpls-exp** *exp-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_x1935_x3534_x1063420509}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x2142823345}

[[没有定义匹配第二层]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}]{#struct_0_x1935_x3534_1063205058}[优先级的规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_418355992}

[[类视图]{style="font-family:宋体"}]{#struct_0_x1935_x3534_1341469271}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x431853504}

[[network-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_606623666}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_x253955671}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_715107298}

[**[not]{lang="EN-US"}**]{#struct_0_x1935_x3534_22618717}[：不匹配该规则。]{style="font-family:宋体"}

[*[exp-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1935_x3534_x1007372223}[：]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值的列表，]{style="font-family:宋体"}[EXP]{lang="EN-US"}[优先级的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:
宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:
宋体"}[8]{lang="EN-US"}[次。如果指定了多个相同的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_1907702586}

[[\# ]{lang="EN-US"}]{#struct_0_x1935_x3534_1356544587}[定义匹配第二层]{style="font-family:宋体"}[EXP]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[或]{style="font-family:
宋体"}[4]{lang="EN-US"}[的报文的规则。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1935_x3534_1430999562}

[\[Sysname\] traffic classifier database]{lang="EN-US"}

[\[Sysname-classifier-database\] if-match second-mpls-exp 3 4]{lang="EN-US"}
:::

::: {#-498302267 .myid}
[]{#_Toc404791988}[]{#struct_0_x1935_x3534_x627162061}[]{#_Toc224962640}[]{#_Toc198110230}

**MPLS QoS \-- MPLS QoS配置命令 \-- if-match second-mpls-label**

------------------------------------------------------------------------

[**[if-match second-mpls-label]{lang="PT-BR"}**]{#struct_0_x1935_x3534_x431919040}[命令用来定义匹配第二层]{style="font-family:
宋体"}[MPLS]{lang="PT-BR"}[标签的规则。]{style="font-family:
宋体"}

[**[undo if-match second-mpls-label]{lang="PT-BR"}**]{#struct_0_x1935_x3534_x1399975119}[命令用来删除匹配第二层]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签的规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x375589546}

[**[if-match ]{lang="EN-US"}**[\[ **not** \] **second-mpls-label** { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]{lang="EN-US"}]{#struct_0_x1935_x3534_497543409}

[**[undo if-match ]{lang="EN-US"}**[\[ **not** \] **second-mpls-label** { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]{lang="EN-US"}]{#struct_0_x1935_x3534_x447286547}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x2129046266}

[[没有定义匹配第二层]{style="font-family:宋体"}]{#struct_0_x1935_x3534_880259251}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[的规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_651580407}

[[类视图]{style="font-family:宋体"}]{#struct_0_x1935_x3534_x389694700}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x870246504}

[[network-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_x431984576}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_x183234425}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_1644238514}

[**[not]{lang="EN-US"}**]{#struct_0_x1935_x3534_x1835603728}[：不匹配该规则。]{style="font-family:宋体"}

[*[label-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1935_x3534_x1620740025}[：]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签值的列表，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签值的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[label-value1]{lang="EN-US"}*[ **to** *label-value2*]{lang="EN-US"}]{#struct_0_x1935_x3534_645440182}[：]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签值]{style="font-family:宋体"}[的范围，]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}*[的值必须小于]{style="font-family:宋体"}*[label-value2]{lang="EN-US"}*[的值，]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签值]{style="font-family:宋体"}[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_477532783}

[[如果指定了多个相同的]{style="font-family:宋体"}]{#struct_0_x1935_x3534_x184195350}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签]{style="font-family:宋体"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_731745131}

[[\# ]{lang="EN-US"}]{#struct_0_x1935_x3534_841774623}[定义匹配第二层]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[标签为]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:宋体"}[1000]{lang="EN-US"}[的报文的规则。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1935_x3534_x432050112}

[\[Sysname\] traffic classifier database]{lang="EN-US"}

[\[Sysname-classifier-database\] if-match second-mpls-label 1 to 1000]{lang="EN-US"}
:::

::: {#-177499157 .myid}
[]{#_Toc404791989}[]{#struct_0_x1935_x3534_x1491082834}[]{#_Toc224962643}[]{#_Toc198110233}[]{#_Toc115171274}[]{#_Toc81455658}[]{#_Toc56569715}[]{#_Toc41626810}[]{#_Toc39395299}

**MPLS QoS \-- MPLS QoS配置命令 \-- remark mpls-exp**

------------------------------------------------------------------------

[**[remark mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_x1821603880}[命令用来配置标记]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo remark mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_2124029104}[命令用来取消标记]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_630866130}

[**[remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **mpls-exp** *exp-value*]{lang="EN-US"}]{#struct_0_x1935_x3534_894859738}

[**[undo remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **mpls-exp**]{lang="EN-US"}]{#struct_0_x1935_x3534_1792087563}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x1327051443}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_x1935_x3534_x1249552629}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x432115648}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_x1935_x3534_x685925627}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_515542103}

[[network-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_x1424056329}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_743367746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x1881170788}

[**[green]{lang="EN-US"}**]{#struct_0_x1935_x3534_1232084828}[：对绿色报文进行重标记。]{style="font-family:宋体"}

[**[red]{lang="EN-US"}**]{#struct_0_x1935_x3534_1024475825}[：对红色报文进行重标记。]{style="font-family:宋体"}

[**[yellow]{lang="EN-US"}**]{#struct_0_x1935_x3534_x1433479795}[：对黄色报文进行重标记。]{style="font-family:宋体"}

[*[exp-value]{lang="EN-US"}*]{#struct_0_x1935_x3534_x624403283}[：]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x432181184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定颜色，则对所有颜色的报文进行重标记。]{style="font-family:宋体"}]{#struct_0_x1935_x3534_44395885}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果是多层标签，则是对最外层标签进行标记。]{style="font-family:宋体"}]{#struct_0_x1935_x3534_x1090223617}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x497112682}

[[\# ]{lang="EN-US"}]{#struct_0_x1935_x3534_x1992082332}[配置标记]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1935_x3534_1168178211}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark mpls-exp 0]{lang="EN-US"}
:::

::: {#401275029 .myid}
[]{#_Toc404791990}[]{#struct_0_x1935_x3534_x1089895937}[]{#_Toc359319441}

**MPLS QoS \-- MPLS QoS配置命令 \-- remark imposition-mpls-exp**

------------------------------------------------------------------------

[**[remark imposition-mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_x174537075}[命令用来配置标记]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[新增标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo remark imposition-mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_994986346}[命令用来取消标记]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[新增标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x2133725743}

[**[remark ]{lang="EN-US"}**]{#struct_0_x1935_x3534_x412355409}[\[ **green** \| **red** \| **yellow** \] **imposition-mpls-exp** *exp-value*]{lang="EN-US"}

[**[undo remark ]{lang="EN-US"}**]{#struct_0_x1935_x3534_x420990963}[\[ **green** \| **red** \| **yellow** \] **imposition-mpls-exp**]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x323092041}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_x1935_x3534_x1089830401}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_28914260}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_x1935_x3534_577188297}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_1661471695}

[[network-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_1320667115}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1935_x3534_x1565868286}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x1840635908}

[**[green]{lang="EN-US"}**]{#struct_0_x1935_x3534_x961328965}[：对绿色报文进行重标记。]{style="font-family:宋体"}

[**[red]{lang="EN-US"}**]{#struct_0_x1935_x3534_x1090420226}[：对红色报文进行重标记。]{style="font-family:宋体"}

[**[yellow]{lang="EN-US"}**]{#struct_0_x1935_x3534_160069361}[：对黄色报文进行重标记。]{style="font-family:宋体"}

[*[exp-value]{lang="EN-US"}*]{#struct_0_x1935_x3534_x572870899}[：]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_x1839267061}

[[如果没有指定颜色，则对所有颜色的报文进行重标记。]{style="font-family:宋体"}]{#struct_0_x1935_x3534_x507922181}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_1344538776}

[[\# ]{lang="EN-US"}]{#struct_0_x1935_x3534_2139351046}[配置标记]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[新增标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1935_x3534_x1090354690}

[[\[Sysname\] traffic behavior database]{lang="EN-US"}]{#struct_0_x1935_x3534_1400695892}

[[\[Sysname-behavior-database\] remark imposition-mpls-exp 0]{lang="EN-US"}]{#struct_0_x1935_x3534_x1619957066}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1935_x3534_2126987779}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark mpls-exp]{lang="EN-US"}**]{#struct_0_x1935_x3534_505852276}

[ ]{lang="EN-US"}
:::
