::: {#-691796861 .myid}
[]{#_Toc404793462}[]{#struct_0_56603_18771_2027784469}[]{#_Toc329272278}[]{#_Toc329184389}[]{#_Toc325276360}

**APR \-- APR配置命令 \-- app-group**

------------------------------------------------------------------------

[**[app-group]{lang="EN-US"}**]{#struct_0_56603_18771_1947423962}[命令用来创建应用组，并进入应用组视图。]{style="font-family:宋体"}

[**[undo app-group]{lang="EN-US"}**]{#struct_0_56603_18771_x592177896}[命令用来删除指定的应用组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x3433933}

[**[app-group ]{lang="EN-US"}***[group-name]{lang="EN-US"}*]{#struct_0_56603_18771_x1626948107}

[**[undo app-group ]{lang="EN-US"}***[group-name]{lang="EN-US"}*]{#struct_0_56603_18771_540916389}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56603_18771_156147253}

[[系统中存在若干预定义应用组，可通过]{style="font-family:宋体"}**[display app-group pre-defined]{lang="EN-US"}**]{#struct_0_56603_18771_1258437760}[命令查看。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_724169806}

[[系统视图]{style="font-family:宋体"}]{#struct_0_56603_18771_x130888192}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1351120906}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x1122622687}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_x591194856}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_81065992}

[*[group-name]{lang="EN-US"}*]{#struct_0_56603_18771_x979030428}[：应用组的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，可以为数字、字母、连字符、下划线，不允许为"]{style="font-family:宋体"}[invalid]{lang="EN-US"}["、"]{style="font-family:宋体"}[other]{lang="EN-US"}["或系统预定义应用组的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_1624834461}

[[系统中最多可以定义]{style="font-family:宋体"}[65536]{lang="EN-US"}]{#struct_0_56603_18771_2015977585}[个应用组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1077187602}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1829530097}[创建名字为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的应用组，并进入应用组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_1855337286}

[\[Sysname\] app-group aaa]{lang="EN-US"}

[\[Sysname-app-group-aaa\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_471069935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[copy app-group]{lang="EN-US"}**]{#struct_0_56603_18771_x591260392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[description]{lang="EN-US"}**]{#struct_0_56603_18771_1658267003}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[include application]{lang="EN-US"}**]{#struct_0_56603_18771_x742460139}
:::

::: {#-56087993 .myid}
[]{#struct_0_56603_18771_838603088}[]{#_Toc404793463}[]{#_Toc329272281}[]{#_Toc329184392}[]{#_Toc325276363}[]{#_Toc312690465}[]{#_Toc312690466}[]{#_Toc312690467}[]{#_Toc312690468}[]{#_Toc312690469}[]{#_Toc312690470}[]{#_Toc312690471}[]{#_Toc312690472}[]{#_Toc312690473}[]{#_Toc312690474}[]{#_Toc312690475}[]{#_Toc312690476}[]{#_Toc312690477}[]{#_Toc312690478}[]{#_Toc312690479}[]{#_Toc312690480}[]{#_Toc312690481}[]{#_Toc312690482}[]{#_Toc312690483}[]{#_Toc312690487}[]{#_Toc312690488}[]{#_Toc312690489}

**APR \-- APR配置命令 \-- application statistics enable**

------------------------------------------------------------------------

[**[application statistics enable]{lang="EN-US"}**]{#struct_0_56603_18771_920621315}[命令用来开启接口的应用统计功能。]{style="font-family:
宋体"}

[**[undo application statistics enable]{lang="EN-US"}**]{#struct_0_56603_18771_x276050660}[命令用来关闭接口的应用统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1708458393}

[**[application statistics enable]{lang="EN-US"}**[ \[ **inbound \| outbound** \]]{lang="EN-US"}]{#struct_0_56603_18771_x1777547194}

[**[undo application statistics enable]{lang="EN-US"}**[ \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_56603_18771_x540085113}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56603_18771_1112912537}

[[接口的应用统计功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_56603_18771_x591719147}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1828844328}

[[三层接口视图]{style="font-family:宋体"}]{#struct_0_56603_18771_1415335716}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_190931738}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x432963114}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_1235638164}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_x327370325}

[**[inbound]{lang="EN-US"}**]{#struct_0_56603_18771_1979187449}[：在接口的入方向上开启应用统计功能。]{style="font-family:宋体"}

[**[outbound]{lang="SV"}**]{#struct_0_56603_18771_x1900643341}[：在接口的出方向上开启应用统计功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_x591784683}

[[如果不指定任何参数，则表示同时开启接口出方向和入方向上的应用统计功能。]{style="font-family:宋体"}]{#struct_0_56603_18771_1226111163}

[[在接口上开启应用统计功能之后，设备能够对接口上收到或者发送的报文的数目、速率按照应用协议分别进行统计，生成的统计信息可以通过]{style="font-family:宋体"}**[display application statistics]{lang="EN-US"}**]{#struct_0_56603_18771_603301982}[命令查看]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}]{#struct_0_56603_18771_69849685}[接口的应用统计功能会消耗大量系统内存。当系统出现内存告警时，请关闭接口的应用统计功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_1919952853}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_56603_18771_x703259955}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_x927790545}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上开启入方向应用统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_56603_18771_x2038562441}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] application statistics enable inbound]{lang="SV"}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_1575893614}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="SV"}[上开启出方向应用统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_56603_18771_x591850219}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/2\] application statistics enable outbound]{lang="SV"}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_x309451095}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="SV"}[上开启所有方向应用统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_56603_18771_x276142588}

[\[Sysname\] interface gigabitethernet 1/0/3]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/3\] application statistics enable]{lang="SV"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_56603_18771_535161642}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_661936431}[在接口]{style="font-family:宋体"}[Vlan-interface1]{lang="SV"}[入方向上]{style="font-family:宋体"}[开启入方向应用统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_56603_18771_x1400129175}

[\[Sysname\] ]{lang="SV"}[interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-]{lang="SV"}[vlan-interface1]{lang="EN-US"}[\] application statistics enable inbound]{lang="SV"}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_x1380555747}[在接口]{style="font-family:宋体"}[Vlan-interface2]{lang="SV"}[上开启出方向应用统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_56603_18771_x591915755}

[\[Sysname\] interface vlan-interface 2]{lang="SV"}

[\[Sysname-vlan-interface2\] application statistics enable outbound]{lang="SV"}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_470516821}[在接口]{style="font-family:宋体"}[Vlan-interface3]{lang="SV"}[上开启所有方向应用统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_56603_18771_858567518}

[\[Sysname\] interface vlan-interface 3]{lang="SV"}

[\[Sysname-vlan-interface3\] application statistics enable]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1261623255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display application statistics]{lang="EN-US"}**]{#struct_0_56603_18771_x767577770}
:::

::: {#-1400361948 .myid}
[]{#_Toc404793464}[]{#struct_0_56603_18771_x2023665306}[]{#_Toc329272280}[]{#_Toc329184391}[]{#_Toc325276362}

**APR \-- APR配置命令 \-- copy app-group**

------------------------------------------------------------------------

[**[copy app-group]{lang="EN-US"}**]{#struct_0_56603_18771_854454921}[命令用来在应用组中拷贝另一个应用组中的所有应用。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1638495885}

[**[copy app-group]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_56603_18771_x2093167209}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_x591981291}

[[应用组视图]{style="font-family:宋体"}]{#struct_0_56603_18771_1231401461}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_1918803962}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x1873172910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_1418587983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_x142378715}

[*[group-name]{lang="SV"}*]{#struct_0_56603_18771_1249424838}[：要拷贝的应用组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_140144871}

[[可以通过多次执行本命令拷贝多个应用组里的应用。]{style="font-family:宋体"}]{#struct_0_56603_18771_1888798781}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_x592046827}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_x1567420808}[在组]{style="font-family:宋体"}[abc]{lang="SV"}[中拷贝组]{style="font-family:
宋体"}[bcd]{lang="EN-US"}[中的所有应用。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_1633256594}

[\[Sysname\] app-group abc]{lang="EN-US"}

[\[Sysname-app-group-abc\] copy app-group bcd]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1630131169}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[app-group]{lang="EN-US"}**]{#struct_0_56603_18771_x1580148668}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[include application]{lang="EN-US"}**]{#struct_0_56603_18771_1387546784}
:::

::: {#-1461383778 .myid}
[]{#_Toc404793465}[]{#struct_0_56603_18771_929128461}[]{#_Toc329272282}[]{#_Toc329184393}[]{#_Toc325276364}[]{#_Toc312690491}[]{#_Toc312690492}[]{#_Toc312690493}[]{#_Toc312690494}[]{#_Toc312690495}[]{#_Toc312690496}[]{#_Toc312690497}[]{#_Toc312690498}[]{#_Toc312690499}[]{#_Toc312690500}[]{#_Toc312690501}[]{#_Toc312690502}[]{#_Toc312690503}[]{#_Toc312690504}[]{#_Toc312690505}[]{#_Toc312690506}[]{#_Toc312690507}[]{#_Toc312690508}[]{#_Toc312690509}[]{#_Toc312690510}[]{#_Toc312690511}[]{#_Toc312690512}[]{#_Toc312690513}[]{#_Toc312690514}[]{#_Toc312690515}[]{#_Toc312690516}[]{#_Toc312690518}[]{#_Toc312690519}[]{#_Toc312690520}[]{#_Toc312690521}[]{#_Toc312690522}[]{#_Toc312690523}[]{#_Toc312690524}[]{#_Toc312690525}[]{#_Toc312690526}[]{#_Toc312690527}[]{#_Toc312690528}[]{#_Toc312690529}[]{#_Toc312690530}[]{#_Toc312690531}[]{#_Toc312690532}[]{#_Toc312690533}[]{#_Toc312690534}[]{#_Toc312690535}[]{#_Toc312690536}

**APR \-- APR配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_56603_18771_1581861090}[命令用来为自定义的应用组设置描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_56603_18771_744418061}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x592112363}

[**[description ]{lang="EN-US"}***[group-description]{lang="EN-US"}*]{#struct_0_56603_18771_342178921}

[**[undo description ]{lang="EN-US"}**]{#struct_0_56603_18771_x1177205515}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1108814622}

[[自定义应用组的描述信息为]{style="font-family:宋体"}[User-defined application group]{lang="EN-US"}]{#struct_0_56603_18771_77049771}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_1503228225}

[[应用组视图]{style="font-family:宋体"}]{#struct_0_56603_18771_x10368767}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_255151990}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x1468380945}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_x592177899}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_x4154829}

[*[group-description]{lang="EN-US"}*]{#struct_0_56603_18771_930613930}[：应用组的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，可以包含空格，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_1406884678}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_x874056365}[配置名字为]{style="font-family:宋体"}[aaa]{lang="SV"}[的应用组描述信息为]{style="font-family:宋体"}[User defined aaa group]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_56603_18771_2090319163}

[\[Sysname\] app-group aaa]{lang="SV"}

[\[Sysname-app-group-aaa\] description User defined aaa group]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1730530796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[app-group]{lang="EN-US"}**]{#struct_0_56603_18771_x599713810}
:::

::: {#1935013717 .myid}
[]{#_Toc404793466}[]{#struct_0_56603_18771_x591194859}[]{#_Toc329272284}[]{#_Toc329184396}[]{#_Toc325276367}

**APR \-- APR配置命令 \-- display app-group**

------------------------------------------------------------------------

[**[display app-group]{lang="EN-US"}**]{#struct_0_56603_18771_80607240}[命令用来显示应用组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_530585409}

[**[display app-group ]{lang="EN-US"}**[\[ **name** *group-name* \| **pre-defined** \| **user-defined** \]]{lang="EN-US"}]{#struct_0_56603_18771_x1544428575}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_844102574}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56603_18771_1358233490}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_870696825}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_342352758}

[[network-operator]{lang="EN-US"}]{#struct_0_56603_18771_x76826848}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_x591260395}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56603_18771_1657939323}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_556815400}

[**[name]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_56603_18771_1842681108}[：显示指定名称的应用组信息。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[表示应用组的名字，不区分大小写，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[pre-defined]{lang="EN-US"}**]{#struct_0_56603_18771_442480687}[：显示预定义的应用组信息。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_56603_18771_1021981754}[：显示用户自定义的应用组信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_x52910247}

[[如果不指定任何参数，则表示显示所有的应用组信息。]{style="font-family:宋体"}]{#struct_0_56603_18771_1257368071}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_1990314507}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x1089590468}[显示用户自定义的所有应用组信息。]{style="font-family:宋体"}

[[\<Sysname\> display app-group user-defined]{lang="EN-US"}]{#struct_0_56603_18771_x591719146}

[ Group name                         Type           Group ID]{lang="EN-US"}

[ g1                                 User-defined   0x80000001]{lang="EN-US"}

[ g1234                              User-defined   0x80000003]{lang="EN-US"}

[ g2                                 User-defined   0x80000002]{lang="EN-US"}

[ g234                               User-defined   0x80000004]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x1828778792}[显示系统预定义的所有应用组信息。]{style="font-family:宋体"}

[[\<Sysname\> display app-group pre-defined ]{lang="EN-US"}]{#struct_0_56603_18771_x591784682}

[ Group name                         Type           Group ID]{lang="EN-US"}

[ authentication                     Pre-defined    0x00000010]{lang="EN-US"}

[ database                           Pre-defined    0x00000003]{lang="EN-US"}

[ email                              Pre-defined    0x00000002]{lang="EN-US"}

[ file-share                         Pre-defined    0x00000009]{lang="EN-US"}

[ games                              Pre-defined    0x00000004]{lang="EN-US"}

[ im                                 Pre-defined    0x0000000a]{lang="EN-US"}

[ internet                           Pre-defined    0x00000005]{lang="EN-US"}

[ multimedia                         Pre-defined    0x00000008]{lang="EN-US"}

[ network-management                 Pre-defined    0x0000000e]{lang="EN-US"}

[ network-service                    Pre-defined    0x0000000f]{lang="EN-US"}

[ news                               Pre-defined    0x0000000d]{lang="EN-US"}

[ p2p                                Pre-defined    0x00000006]{lang="EN-US"}

[ productivity-tools                 Pre-defined    0x00000012]{lang="EN-US"}

[ routing                            Pre-defined    0x00000011]{lang="EN-US"}

[ shopping-and-bank                  Pre-defined    0x0000000c]{lang="EN-US"}

[ stock                              Pre-defined    0x0000000b]{lang="EN-US"}

[ voip                               Pre-defined    0x00000007]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1226045627}[显示所有应用组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display app-group]{lang="EN-US"}]{#struct_0_56603_18771_x591850218}

[ Group name                         Type           Group ID]{lang="EN-US"}

[ authentication                     Pre-defined    0x00000010]{lang="EN-US"}

[ database                           Pre-defined    0x00000003]{lang="EN-US"}

[ email                              Pre-defined    0x00000002]{lang="EN-US"}

[ file-share                         Pre-defined    0x00000009]{lang="EN-US"}

[ g1                                 User-defined   0x80000001]{lang="EN-US"}

[ g1234                              User-defined   0x80000003]{lang="EN-US"}

[ g2                                 User-defined   0x80000002]{lang="EN-US"}

[ g234                               User-defined   0x80000004]{lang="EN-US"}

[ games                              Pre-defined    0x00000004]{lang="EN-US"}

[ im                                 Pre-defined    0x0000000a]{lang="EN-US"}

[ internet                           Pre-defined    0x00000005]{lang="EN-US"}

[ multimedia                         Pre-defined    0x00000008]{lang="EN-US"}

[ network-management                 Pre-defined    0x0000000e]{lang="EN-US"}

[ network-service                    Pre-defined    0x0000000f]{lang="EN-US"}

[ news                               Pre-defined    0x0000000d]{lang="EN-US"}

[ p2p                                Pre-defined    0x00000006]{lang="EN-US"}

[ productivity-tools                 Pre-defined    0x00000012]{lang="EN-US"}

[ routing                            Pre-defined    0x00000011]{lang="EN-US"}

[ shopping-and-bank                  Pre-defined    0x0000000c]{lang="EN-US"}

[ stock                              Pre-defined    0x0000000b]{lang="EN-US"}

[ voip                               Pre-defined    0x00000007]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x309385559}[显示名为]{style="font-family:宋体"}[group_A]{lang="EN-US"}[的应用组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display app-group name group_A]{lang="EN-US"}]{#struct_0_56603_18771_x1073072115}

[ Group name:         group_A]{lang="EN-US"}

[ Group ID:           0x80000005]{lang="EN-US"}

[ Type:               User-defined]{lang="EN-US"}

[ Application count:  5]{lang="EN-US"}

[ Include application list:]{lang="EN-US"}

[ Application name                   Type           App ID]{lang="EN-US"}

[ 3com-amp3                          Pre-defined    0x00000003]{lang="EN-US"}

[ app1                               User-defined   0x80000001]{lang="EN-US"}

[ bapp3                              User-defined   0x80000006]{lang="EN-US"}

[ pop3                               Pre-defined    0x00000e75]{lang="EN-US"}

[ smtp                               Pre-defined    0x00001135]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display app-group]{lang="EN-US"}]{#struct_0_56603_18771_1186705232}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1872952754}[[字段]{style="font-family:黑体"}]{#struct_0_56603_18771_x591915754}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56603_18771_470582357}

[[Group name]{lang="EN-US"}]{#struct_0_56603_18771_120756448}

[[应用组的组名]{style="font-family:宋体"}]{#struct_0_56603_18771_x1842350661}

[[Group ID]{lang="EN-US"}]{#struct_0_56603_18771_523763445}

[[应用组的组号]{style="font-family:宋体"}]{#struct_0_56603_18771_x1166134668}

[[Type]{lang="EN-US"}]{#struct_0_56603_18771_1962463156}

[[应用组或应用的类型，取值包括：]{style="font-family:宋体"}]{#struct_0_56603_18771_x591981290}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pre-defined]{lang="EN-US"}]{#struct_0_56603_18771_1231335925}[：系统预定义]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[User-defined]{lang="EN-US"}]{#struct_0_56603_18771_787009081}[：用户自定义]{lang="EN-US" style="font-family:宋体"}

[[Application count]{lang="EN-US"}]{#struct_0_56603_18771_x1099752576}

[[应用组中包含的应用个数]{style="font-family:宋体"}]{#struct_0_56603_18771_1751635666}

[[Include application list]{lang="EN-US"}]{#struct_0_56603_18771_x812261951}

[[包含的应用列表]{style="font-family:宋体"}]{#struct_0_56603_18771_x592046826}

[[Application name]{lang="EN-US"}]{#struct_0_56603_18771_x1567486344}

[[应用名]{style="font-family:宋体"}]{#struct_0_56603_18771_2079655359}

[[App ID]{lang="EN-US"}]{#struct_0_56603_18771_x273774946}

[[应用协议编号]{style="font-family:宋体"}]{#struct_0_56603_18771_x727788278}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_112240211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[app-group ]{lang="EN-US"}**]{#struct_0_56603_18771_x1566434159}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[include]{lang="EN-US"}**]{#struct_0_56603_18771_x592112362}

::: {#-482506299 .myid}
[]{#struct_0_56603_18771_342244457}[]{#_Toc404793467}[]{#_Toc329272283}[]{#_Toc329184395}[]{#_Toc325276366}

**APR \-- APR配置命令 \-- display application**

------------------------------------------------------------------------

[**[display application]{lang="EN-US"}**]{#struct_0_56603_18771_x1591584393}[命令用来显示应用信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1711191693}

[**[display application]{lang="EN-US"}**[ \[ **name** *application-name* \| **pre-defined** \| **user-defined** \]]{lang="EN-US"}]{#struct_0_56603_18771_x2022288413}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1687137696}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56603_18771_336350693}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1075902636}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x53454993}

[[network-operator]{lang="EN-US"}]{#struct_0_56603_18771_x1041362255}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_x592177898}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56603_18771_x4089293}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_1191193629}

[**[name]{lang="SV"}**]{#struct_0_56603_18771_x410256709}*[ app]{lang="SV"}[lication]{lang="EN-US"}[-name]{lang="SV"}*[：显示指定名称的应用信息。]{style="font-family:宋体"}*[app-name]{lang="SV"}*[表示应用的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[pre-defined]{lang="SV"}**]{#struct_0_56603_18771_x1461339343}[：]{style="font-family:宋体"}[显示系统预定义的应用列表。]{style="font-family:宋体"}

[**[user-defined]{lang="SV"}**]{#struct_0_56603_18771_x299842698}[：]{style="font-family:宋体"}[显示用户自定义的应用列表。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_x492814982}

[[若不指定任何参数，则表示显示所有的应用信息。]{style="font-family:宋体"}]{#struct_0_56603_18771_2133063965}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_175078715}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x591194858}[显示系统预定义的应用列表。]{style="font-family:宋体"}

[[\<Sysname\> display application pre-defined]{lang="EN-US"}]{#struct_0_56603_18771_80672776}

[ Pre-defined count:   15]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Application name                   Type          App ID       Tunnel   Encrypted ]{lang="EN-US"}

[ ambit-lm                           Pre-defined   0x000000b9   No       No]{lang="EN-US"}

[ amdsched                           Pre-defined   0x000000ba   No       No]{lang="EN-US"}

[ amidxtape                          Pre-defined   0x000000bb   No       No]{lang="EN-US"}

[ amiganetfs                         Pre-defined   0x000000bc   No       No]{lang="EN-US"}

[ aminet                             Pre-defined   0x000000bd   No       No]{lang="EN-US"}

[ amp                                Pre-defined   0x000000be   No       No]{lang="EN-US"}

[ amt-soap-https                     Pre-defined   0x000000cc   No       Yes]{lang="EN-US"}

[ appserv-http                       Pre-defined   0x00000122   No       No]{lang="EN-US"}

[ appserv-https                      Pre-defined   0x00000123   No       Yes]{lang="EN-US"}

[ ktelnet                            Pre-defined   0x000009ae   No       No]{lang="EN-US"}

[ l2c-connect                        Pre-defined   0x000009b6   No       No]{lang="EN-US"}

[ l2c-info                           Pre-defined   0x000009b7   No       No]{lang="EN-US"}

[ l2tp                               Pre-defined   0x000009b8   Yes      No]{lang="EN-US"}

[ l3-exprt                           Pre-defined   0x000009b9   No       No]{lang="EN-US"}

[ l3-hawk                            Pre-defined   0x000009ba   No       No]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_567440663}[显示用户自定义的应用列表。]{style="font-family:宋体"}

[[\<Sysname\> display application user-defined]{lang="EN-US"}]{#struct_0_56603_18771_x591260394}

[ User-defined count:  2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Application name                   Type          App ID       Tunnel   Encrypted ]{lang="EN-US"}

[ amp_User                           User-defined  0x80000003   No       No]{lang="EN-US"}

[ amp_User2                          User-defined  0x80000004   No       No]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1657873787}[显示所有应用列表。]{style="font-family:宋体"}

[[\<Sysname\> display application]{lang="EN-US"}]{#struct_0_56603_18771_x591719149}

[ Total count:         17]{lang="EN-US"}

[ Pre-defined count:   15]{lang="EN-US"}

[ User-defined count:  2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Application name                   Type          App ID       Tunnel   Encrypted ]{lang="EN-US"}

[ ambit-lm                           Pre-defined   0x000000b9   No       No]{lang="EN-US"}

[ amdsched                           Pre-defined   0x000000ba   No       No]{lang="EN-US"}

[ amidxtape                          Pre-defined   0x000000bb   No       No]{lang="EN-US"}

[ amiganetfs                         Pre-defined   0x000000bc   No       No]{lang="EN-US"}

[ aminet                             Pre-defined   0x000000bd   No       No]{lang="EN-US"}

[ amp                                Pre-defined   0x000000be   No       No]{lang="EN-US"}

[ amp_User                           User-defined  0x80000003   No       No]{lang="EN-US"}

[ amp_User2                          User-defined  0x80000004   No       No]{lang="EN-US"}

[ amt-soap-https                     Pre-defined   0x000000cc   No       Yes]{lang="EN-US"}

[ appserv-http                       Pre-defined   0x00000122   No       No]{lang="EN-US"}

[ appserv-https                      Pre-defined   0x00000123   No       Yes]{lang="EN-US"}

[ ktelnet                            Pre-defined   0x000009ae   No       No]{lang="EN-US"}

[ l2c-connect                        Pre-defined   0x000009b6   No       No]{lang="EN-US"}

[ l2c-info                           Pre-defined   0x000009b7   No       No]{lang="EN-US"}

[ l2tp                               Pre-defined   0x000009b8   Yes      No]{lang="EN-US"}

[ l3-exprt                           Pre-defined   0x000009b9   No       No]{lang="EN-US"}

[ l3-hawk                            Pre-defined   0x000009ba   No       No]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x1828188968}[显示名为]{style="font-family:宋体"}[telnet]{lang="EN-US"}[的应用信息。]{style="font-family:宋体"}

[[\<Sysname\> display application name telnet ]{lang="EN-US"}]{#struct_0_56603_18771_786268870}

[ Application name: telnet]{lang="EN-US"}

[ Application ID:   0x000012b7]{lang="EN-US"}

[ Tunnel:           No]{lang="EN-US"}

[ Encrypted:        No]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display application]{lang="EN-US"}]{#struct_0_56603_18771_991335496}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1867212114}[[字段]{style="font-family:黑体"}]{#struct_0_56603_18771_545912250}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56603_18771_2115185336}

[[Total count]{lang="EN-US"}]{#struct_0_56603_18771_x591784685}

[[应用总数]{style="font-family:宋体"}]{#struct_0_56603_18771_1225980091}

[[Pre-defined count]{lang="EN-US"}]{#struct_0_56603_18771_331690690}

[[预定义应用总数]{style="font-family:宋体"}]{#struct_0_56603_18771_x1116674894}

[[User-defined count]{lang="EN-US"}]{#struct_0_56603_18771_716374983}

[[自定义应用总数]{style="font-family:宋体"}]{#struct_0_56603_18771_281086275}

[[Application Name]{lang="EN-US"}]{#struct_0_56603_18771_1272974955}

[[应用名]{style="font-family:宋体"}]{#struct_0_56603_18771_x591850221}

[[Type]{lang="EN-US"}]{#struct_0_56603_18771_x308926806}

[[应用的类型，取值包括：]{style="font-family:宋体"}]{#struct_0_56603_18771_x1104094467}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pre-defined]{lang="EN-US"}]{#struct_0_56603_18771_x1794201602}[：系统预定义]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[User-defined]{lang="EN-US"}]{#struct_0_56603_18771_x2074559348}[：用户自定义]{lang="EN-US" style="font-family:宋体"}

[[App ID/Application ID]{lang="EN-US"}]{#struct_0_56603_18771_x197542658}

[[应用协议编号]{style="font-family:宋体"}]{#struct_0_56603_18771_x591915757}

[[Tunnel]{lang="EN-US"}]{#struct_0_56603_18771_470647893}

[[应用是否为隧道类型，例如]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_56603_18771_767145027}[为一个隧道类型的应用]{style="font-family:宋体"}

[[Encrypted]{lang="EN-US"}]{#struct_0_56603_18771_657332887}

[[应用是否为加密类型，例如]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_56603_18771_x1416334835}[为一个加密类型的应用]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1743248875}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[app-group ]{lang="EN-US"}**]{#struct_0_56603_18771_x591981293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[include]{lang="EN-US"}**]{#struct_0_56603_18771_1231270389}

::: {#-154187737 .myid}
[]{#_Toc404793468}[]{#struct_0_56603_18771_x845671083}[]{#_Toc329272285}[]{#_Toc329184397}[]{#_Toc325276368}[]{#_Toc312690585}[]{#_Toc312690586}[]{#_Toc312690587}[]{#_Toc312690588}[]{#_Toc312690589}[]{#_Toc312690590}[]{#_Toc312690591}[]{#_Toc312690592}[]{#_Toc312690593}[]{#_Toc312690594}[]{#_Toc312690595}[]{#_Toc312690596}[]{#_Toc312690597}[]{#_Toc312690598}[]{#_Toc312690599}[]{#_Toc312690600}[]{#_Toc312690601}[]{#_Toc312690602}[]{#_Toc312690603}[]{#_Toc312690633}[]{#_Toc312690634}[]{#_Toc312690635}[]{#_Toc312690636}[]{#_Toc312690637}[]{#_Toc312690638}

**APR \-- APR配置命令 \-- display application statistics**

------------------------------------------------------------------------

[**[display application statistics]{lang="EN-US"}**]{#struct_0_56603_18771_x865761741}[命令用来显示接口上的应用统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1948882430}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_56603_18771_x1333175911}

[**[display application statistics ]{lang="EN-US"}**[\[ **direction** { **inbound** \| **outbound** } \| **interface** *interface-type interface-number* \| **name** *application-name* \] \*]{lang="EN-US"}]{#struct_0_56603_18771_x541110336}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_56603_18771_1510805707}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display application statistics ]{lang="EN-US"}**[\[ **direction** { **inbound** \| **outbound** } \| **interface** *interface-type interface-number* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \| **name** *application-name* \] \*]{lang="EN-US"}]{#struct_0_56603_18771_1051288045}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_56603_18771_1316997679}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display application statistics ]{lang="EN-US"}**[\[ **direction** { **inbound** \| **outbound** } \| **interface** *interface-type interface-number* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \| **name** *application-name* \] \*]{lang="EN-US"}]{#struct_0_56603_18771_x592046829}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1568076168}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56603_18771_811847027}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_1558191685}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_1497215054}

[[network-operator]{lang="EN-US"}]{#struct_0_56603_18771_x85412157}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_1598127462}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56603_18771_1892601134}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_x608967731}

[**[direction]{lang="EN-US"}**]{#struct_0_56603_18771_x592112365}[：显示指定方向的应用统计信息。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_56603_18771_341785705}[：显示接口入方向的应用统计信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_56603_18771_501968849}[：显示接口出方向的应用统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_56603_18771_x1779918410}[：显示指定接口的应用统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示要显示统计信息的接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_56603_18771_x1307351279}[：显示指定单板上全局接口的应用统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_56603_18771_20440351}[：显示指定成员设备上全局接口的应用统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_56603_18771_714152259}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上全局接口的应用统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_56603_18771_1764873703}[：显示指定成员设备的指定单板上全局接口的应用统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_56603_18771_x1658566272}[：显示指定单板上全局接口的应用统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_56603_18771_x99291449}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局接口的应用统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[app]{lang="EN-US"}[lication-name]{lang="EN-US"}*]{#struct_0_56603_18771_805679252}[：显示指定名称的应用统计信息。]{style="font-family:宋体"}*[app-name]{lang="EN-US"}*[表示应用的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1375513249}

[[如果不指定任何参数，则表示显示所有接口的应用统计信息。]{style="font-family:宋体"}]{#struct_0_56603_18771_x592177901}

[[只有在接口应用统计功能开启的情况下，接口才能产生相应的应用统计信息。因此，使用本命令查看接口统计信息之前，请确保接口的应用统计功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_56603_18771_x1959945668}

[[可以按应用名称、接口出方向、接口入方向、接口名称分别显示相应的应用统计信息，也可以通过指定多个参数，显示同时符合多个参数的应用统计信息。]{style="font-family:宋体"}]{#struct_0_56603_18771_x663499724}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_x370020088}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x444792429}[显示接口上的所有应用统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics]{lang="EN-US"}]{#struct_0_56603_18771_x591194861}

[Interface : GigabitEthernet1/0/1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[                OUT  170034             270011351          3211       451134]{lang="EN-US"}

[app2            IN   2195               18560000           300        654222]{lang="EN-US"}

[                OUT  21986666666        655555555123123101 55551      5454125111]{lang="EN-US"}

[aPP3            IN   2195               17560000           300        45161]{lang="EN-US"}

[                OUT  21986666666        5555555551231231   55551       5454125111]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface : GigabitEthernet1/0/2]{lang="EN-US"}

[Application   In/Out Packets          Bytes               PPS         BPS]{lang="EN-US"}

[app4            IN   1900231111111    252334402111        2342222222  3411222222]{lang="EN-US"}

[                OUT  170034           270011351           3211        451134]{lang="EN-US"}

[app2            IN   2195             18560000            300         654222]{lang="EN-US"}

[                OUT  21986666666      65555555512         55551       45412]{lang="EN-US"}

[App123456981200 IN   2195             17560000            300         45161]{lang="EN-US"}

[123456789012300 OUT  21986666666      5555555551231231    55551       54541251]{lang="EN-US"}

[11111111111100]{lang="EN-US"}

[01234567890100]{lang="EN-US"}

[0123456]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_81131531}[显示接口]{style="font-family:宋体"}[Vlan-interface1]{lang="EN-US"}[上所有应用的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics interface vlan-interface 1]{lang="EN-US"}]{#struct_0_56603_18771_x534210465}

[Interface : Vlan-interface1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[                OUT  170034             270011351          3211       451134]{lang="EN-US"}

[app2            IN   2195               18560000           300        654222]{lang="EN-US"}

[                OUT  21986666666        655555555123123101 55551      5454125111]{lang="EN-US"}

[APP3            IN   2195               17560000           300        45161]{lang="EN-US"}

[                OUT  21986666666        5555555551231231   55551      5454125111]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1274470890}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上所有的入方向应用统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics interface gigabitethernet 1/0/1 direction inbound]{lang="EN-US"}]{#struct_0_56603_18771_x591260397}

[Interface : GigabitEthernet1/0/1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[app2            IN   2195               18560000           300        654222]{lang="EN-US"}

[APP3            IN   2195               17560000           300        45161]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1658070395}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上所有的出方向应用统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics interface gigabitethernet 1/0/1 direction outbound]{lang="EN-US"}]{#struct_0_56603_18771_x1160829687}

[Interface : GigabitEthernet1/0/1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[appaaaaasg      OUT  190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[app2            OUT  2195               18560000           300        654222]{lang="EN-US"}

[APP3            OUT  2195               17560000           300        45161]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_480488732}[显示应用名为]{style="font-family:宋体"}[app1]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics name app1]{lang="EN-US"}]{#struct_0_56603_18771_x591719148}

[Interface : GigabitEthernet1/0/1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[app1            IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[                OUT  170034             270011351          3211       451134]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface : GigabitEthernet1/0/2]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[app1            IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[                OUT  170034             270011351          3211       451134]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface : GigabitEthernet1/0/3]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[app1            IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display application statistics]{lang="EN-US"}]{#struct_0_56603_18771_x1828123432}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1863886898}[[字段]{style="font-family:黑体"}]{#struct_0_56603_18771_1242113167}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56603_18771_x1377120482}

[[Interface]{lang="EN-US"}]{#struct_0_56603_18771_1093030238}

[[接口的名称]{style="font-family:宋体"}]{#struct_0_56603_18771_x319661906}

[[Application]{lang="EN-US"}]{#struct_0_56603_18771_x942318012}

[[应用的名称]{style="font-family:宋体"}]{#struct_0_56603_18771_x591784684}

[[In/Out]{lang="EN-US"}]{#struct_0_56603_18771_1225914555}

[[入方向]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_56603_18771_742744146}[出方向]{style="font-family:宋体"}

[[Packets ]{lang="EN-US"}]{#struct_0_56603_18771_x1851159029}

[[接口上接收或发送的报文个数]{style="font-family:宋体"}]{#struct_0_56603_18771_x545771689}

[[Bytes]{lang="EN-US"}]{#struct_0_56603_18771_x698841581}

[[接口上接收或发送的字节数]{style="font-family:宋体"}]{#struct_0_56603_18771_x591850220}

[[PPS]{lang="EN-US"}]{#struct_0_56603_18771_x308861270}

[[每秒报文数]{style="font-family:宋体"}]{#struct_0_56603_18771_x1440651650}

[[BPS]{lang="EN-US"}]{#struct_0_56603_18771_1794492904}

[[每秒比特数]{style="font-family:宋体"}]{#struct_0_56603_18771_x1426952462}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_231727582}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[app-group]{lang="EN-US"}**]{#struct_0_56603_18771_x591915756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[application statistics enable]{lang="EN-US"}**]{#struct_0_56603_18771_470713429}

::: {#1967813999 .myid}
[]{#_Toc404793469}[]{#struct_0_56603_18771_x1957437190}[]{#_Toc329272286}[]{#_Toc329184398}[]{#_Toc325276369}[]{#_Toc312690640}[]{#_Toc312690641}

**APR \-- APR配置命令 \-- display application statistics top**

------------------------------------------------------------------------

[**[display application statistics top]{lang="EN-US"}**]{#struct_0_56603_18771_x1709089820}[命令用来按指定类型的统计排名显示接口应用统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x413887515}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_56603_18771_x1639168069}

[**[display application statistics top ]{lang="EN-US"}***[number]{lang="EN-US"}*[ { **bps** \| **bytes** \| **packets** \| **pps** } **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_56603_18771_x91822759}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_56603_18771_x1834006899}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display application statistics top ]{lang="EN-US"}***[number]{lang="EN-US"}*[ { **bps** \| **bytes** \| **packets** \| **pps** } **interface** *interface-type interface-number* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_56603_18771_x720370736}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_56603_18771_x591981292}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display application statistics top ]{lang="EN-US"}***[number]{lang="EN-US"}*[ { **bps** \| **bytes** \| **packets** \| **pps** } **interface** *interface-type interface-number* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_56603_18771_1231204853}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_1557545716}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56603_18771_1344527717}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_1029766189}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_2138655297}

[[network-operator]{lang="EN-US"}]{#struct_0_56603_18771_510771662}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_842595525}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56603_18771_999616706}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_x592046828}

[*[number]{lang="EN-US"}*]{#struct_0_56603_18771_x1568141704}[：显示排名前]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的应用统计信息。]{style="font-family:宋体"}

[**[bytes]{lang="EN-US"}**]{#struct_0_56603_18771_x185383074}[：显示接口字节数为前]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的应用统计信息。]{style="font-family:宋体"}

[**[bps]{lang="EN-US"}**]{#struct_0_56603_18771_372625397}[：显示接口比特速率统计为前]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的应用统计信息。]{style="font-family:宋体"}

[**[packets]{lang="EN-US"}**]{#struct_0_56603_18771_x270366485}[：显示接口包数为前]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的应用统计信息。]{style="font-family:宋体"}

[**[pps]{lang="EN-US"}**]{#struct_0_56603_18771_x1807106616}[：显示接口包速率统计为前]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的应用统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_56603_18771_1917858854}[：显示指定接口的应用统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[指定要显示统计信息的接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_56603_18771_217360632}[：显示指定单板上全局接口的应用统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_56603_18771_1517806696}[：显示指定成员设备上全局接口的应用统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_56603_18771_x1255281745}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上全局接口的应用统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_56603_18771_1866001755}[：显示指定成员设备的指定单板上全局接口应用的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_56603_18771_1473601610}[：显示指定单板上全局接口应用的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。该参数仅在指定显示全局接口（例如]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口）时可见。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_56603_18771_x99029306}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上全局接口的应用统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_x592112364}

[[只有在接口应用统计功能开启的情况下，接口才能产生相应的应用统计信息。因此，使用本命令查看接口统计信息之前，请确保接口的应用统计功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_56603_18771_341851241}

[[系统以接口上某一个应用的出方向和入方向的统计值之和为依据对应用进行排名。统计值相同的应用，再按照应用名称的字母顺序排列。]{style="font-family:宋体"}]{#struct_0_56603_18771_x53996589}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1348953097}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1567173084}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上包数为前]{style="font-family:宋体"}[3]{lang="EN-US"}[的应用统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics top 3 packets interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_56603_18771_x696733323}

[Interface : GigabitEthernet1/0/1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[                OUT  170034             270011351          3211       451134]{lang="EN-US"}

[app2            IN   2196               18560000           300        654222]{lang="EN-US"}

[                OUT  21986666666        655555555123123101 55551      5454125111]{lang="EN-US"}

[aPP3            IN   2195               17560000           300        45161]{lang="EN-US"}

[                OUT  21986666666        5555555551231231   55551      5454125111]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x592177900}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[字节数为前]{style="font-family:宋体"}[3]{lang="EN-US"}[的应用统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics top 3 bytes interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_56603_18771_x1959880132}

[Interface : GigabitEthernet1/0/1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[                OUT  170034             270011351          3211       451134]{lang="EN-US"}

[app2            IN   2196               18560000           300        654222]{lang="EN-US"}

[                OUT  21986666666        155555555123123101 55551      5454125111]{lang="EN-US"}

[aPP3            IN   2195               17560000           300        45161]{lang="EN-US"}

[                OUT  21986666666        5555555551231231   55551      5454125111]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1343910345}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[包速率为前]{style="font-family:宋体"}[3]{lang="EN-US"}[的应用统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics top 3 pps interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_56603_18771_1156465331}

[Interface : GigabitEthernet1/0/1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222]{lang="EN-US"}

[                OUT  170034             270011351          3211       451134]{lang="EN-US"}

[app2            IN   2196               18560000           305        654222]{lang="EN-US"}

[                OUT  21986666666        655555555123123101 55551      5454125111]{lang="EN-US"}

[aPP3            IN   2195               17560000           300        45161]{lang="EN-US"}

[                OUT  21986666666        5555555551231231   55551      5454125111]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x591194860}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[比特速率为前]{style="font-family:宋体"}[3]{lang="EN-US"}[的应用统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display application statistics top 3 bps interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_56603_18771_81197067}

[Interface : GigabitEthernet1/0/1]{lang="EN-US"}

[Application   In/Out Packets            Bytes              PPS        BPS]{lang="EN-US"}

[appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 9411222222]{lang="EN-US"}

[                OUT  170034             270011351          3211       451134]{lang="EN-US"}

[app2            IN   2196               18560000           300        654222]{lang="EN-US"}

[                OUT  21986666666        155555555123123101 55551      5454125111]{lang="EN-US"}

[aPP3            IN   2195               17560000           300        45161]{lang="EN-US"}

[                OUT  21986666666        5555555551231231   55551      5454125111]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display application statistics top]{lang="EN-US"}]{#struct_0_56603_18771_976936804}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1864613234}[[字段]{style="font-family:黑体"}]{#struct_0_56603_18771_x217330398}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56603_18771_x516107707}

[[Interface]{lang="EN-US"}]{#struct_0_56603_18771_x1309129036}

[[接口的名称]{style="font-family:宋体"}]{#struct_0_56603_18771_x591260396}

[[Application]{lang="EN-US"}]{#struct_0_56603_18771_1658004859}

[[应用的名称]{style="font-family:宋体"}]{#struct_0_56603_18771_371282601}

[[In/Out]{lang="EN-US"}]{#struct_0_56603_18771_1543627889}

[[入方向]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_56603_18771_1456405652}[出方向]{style="font-family:宋体"}

[[Packets ]{lang="EN-US"}]{#struct_0_56603_18771_1099095425}

[[接口上接收或发送的报文个数]{style="font-family:宋体"}]{#struct_0_56603_18771_1787290842}

[[Bytes]{lang="EN-US"}]{#struct_0_56603_18771_203323319}

[[接口上接收或发送的字节数]{style="font-family:宋体"}]{#struct_0_56603_18771_1912896764}

[[PPS]{lang="EN-US"}]{#struct_0_56603_18771_155708761}

[[每秒报文数]{style="font-family:宋体"}]{#struct_0_56603_18771_x1803815724}

[[BPS]{lang="EN-US"}]{#struct_0_56603_18771_1646341040}

[[每秒比特数]{style="font-family:宋体"}]{#struct_0_56603_18771_1787356378}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1386504395}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[app-group]{lang="EN-US"}**]{#struct_0_56603_18771_x1083422396}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[application statistics ]{lang="EN-US"}**]{#struct_0_56603_18771_326137717}**[enable]{lang="EN-US"}**

::: {#1826051177 .myid}
[]{#_Toc404793470}[]{#struct_0_56603_18771_x1172800735}

**APR \-- APR配置命令 \-- display port-mapping pre-defined**

------------------------------------------------------------------------

[**[display port-mapping pre-defined]{lang="EN-US"}**]{#struct_0_56603_18771_x1800023015}[命令用来显示预定义的端口映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1998230990}

[**[display port-mapping]{lang="EN-US"}**[ **pre-defined**]{lang="EN-US"}]{#struct_0_56603_18771_x952965200}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_1787421914}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56603_18771_578677641}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_x211660727}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x1326001443}

[[network-operator]{lang="EN-US"}]{#struct_0_56603_18771_x1316809733}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_x139914248}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56603_18771_501682312}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_56603_18771_1348842}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x48084261}[显示预定义的端口映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display port-mapping pre-defined]{lang="EN-US"}]{#struct_0_56603_18771_1787487450}

[ Application                      Protocol Port]{lang="EN-US"}

[ tacacs-ds                        TCP      65]{lang="EN-US"}

[                                  UDP      65]{lang="EN-US"}

[ net-bios-dgm                     TCP      137, 138, 139]{lang="EN-US"}

[                                  UDP      137, 138, 139]{lang="EN-US"}

[ ftp                              TCP      21]{lang="EN-US"}

[ tftp                             UDP      69]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display port-mapping pre-defined]{lang="EN-US"}]{#struct_0_56603_18771_1807471803}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1623991570}[[字段]{style="font-family:黑体"}]{#struct_0_56603_18771_1496029185}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56603_18771_x1215480014}

[[Application]{lang="EN-US"}]{#struct_0_56603_18771_x173860202}

[[进行端口映射的应用层协议]{style="font-family:宋体"}]{#struct_0_56603_18771_367002371}

[[Protocol]{lang="EN-US"}]{#struct_0_56603_18771_1787552986}

[[传输层协议类型]{style="font-family:宋体"}]{#struct_0_56603_18771_972721568}

[[Port]{lang="EN-US"}]{#struct_0_56603_18771_x627444768}

[[应用层协议的端口号]{style="font-family:宋体"}]{#struct_0_56603_18771_x1176817935}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1003954938}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-mapping]{lang="EN-US"}**]{#struct_0_56603_18771_1918781450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-mapping]{lang="EN-US"}**]{#struct_0_56603_18771_x1030647762}

::: {#1837015446 .myid}
[]{#_Toc404793471}[]{#struct_0_56603_18771_428582606}[]{#_Toc329272289}[]{#_Toc312690542}[]{#_Toc312690543}[]{#_Toc312690544}[]{#_Toc312690545}[]{#_Toc312690546}[]{#_Toc312690547}[]{#_Toc312690548}[]{#_Toc312690549}[]{#_Toc312690550}[]{#_Toc312690551}[]{#_Toc312690552}[]{#_Toc312690553}[]{#_Toc312690554}[]{#_Toc312690555}[]{#_Toc312690556}[]{#_Toc312690557}[]{#_Toc312690558}[]{#_Toc312690559}[]{#_Toc312690560}[]{#_Toc312690561}[]{#_Toc312690562}[]{#_Toc312690563}[]{#_Toc312690564}[]{#_Toc312690565}[]{#_Toc312690566}[]{#_Toc312690567}[]{#_Toc312690568}[]{#_Toc312690569}[]{#_Toc312690570}[]{#_Toc312690571}[]{#_Toc312690572}[]{#_Toc312690573}[]{#_Toc312690574}[]{#_Toc312690575}[]{#_Toc312690576}[]{#_Toc312690577}[]{#_Toc312690578}[]{#_Toc312690579}[]{#_Toc312690580}[]{#_Toc312690581}[]{#_Toc312690582}[]{#_Toc312690583}

**APR \-- APR配置命令 \-- display port-mapping user-defined**

------------------------------------------------------------------------

[**[display port-mapping user-defined]{lang="EN-US"}**]{#struct_0_56603_18771_1787618522}[命令用来显示自定义的端口映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x507915691}

[**[display port-mapping user-defined ]{lang="EN-US"}**[\[ **application** ]{lang="EN-US"}]{#struct_0_56603_18771_152713428}*[app]{lang="ES-AR"}[lication]{lang="EN-US"}[-name \| ]{lang="ES-AR"}***[port]{lang="ES-AR"}**[ *port-number* ]{lang="ES-AR"}[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_1850368332}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56603_18771_x1303852529}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_406643870}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x1759929739}

[[network-operator]{lang="EN-US"}]{#struct_0_56603_18771_x1341374770}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_x2092252117}

[[mdc-operator]{lang="EN-US"}]{#struct_0_56603_18771_1787684058}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_1005537688}

[**[application]{lang="EN-US"}**[ *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_1510965536}[：显示指定端口映射的应用协议。]{style="font-family:
宋体"}*[app]{lang="ES-AR"}[lication-name]{lang="EN-US"}*[表示应用协议名称，必须标准且能够被设备识别，不区分大小写。]{style="font-family:宋体"}

[**[port]{lang="ES-AR"}**]{#struct_0_56603_18771_1446797775}*[ port-number]{lang="ES-AR"}*[：显示指定应用层协议的端口。]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[表示端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_2114911349}

[[若不指定任何参数，则表示显示所有的用户自定义端口映射信息。]{style="font-family:宋体"}]{#struct_0_56603_18771_304775868}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_x323166137}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_669521822}[显示所有自定义的端口映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display port-mapping user-defined]{lang="EN-US"}]{#struct_0_56603_18771_1787749594}

[ Application       Port  Protocol    Match Type  Match Condition]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ FTP                21     TCP          \-\--          \-\--]{lang="EN-US"}

[ FTP                21     UDP          IPv4 host   10.10.10.1(vpn1)]{lang="EN-US"}

[ FTP                2121   UDP          IPv4 host   \[11.10.10.1, 11.10.10.10\](vpn2)]{lang="EN-US"}

[ FTP                21     UDP          IPv4 subnet 10.10.10.1/24]{lang="EN-US"}

[ FTP                21     SCTP         IPv6 host   2000:fdb8::1:00ab:853c:39ab]{lang="EN-US"}

[ HTTP               899    TCP          IPV4 ACL    3002]{lang="EN-US"}

[ HTTP               999    SCTP         IPv6 ACL    3002]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ]{lang="EN-US"}]{#struct_0_56603_18771_x2075900198}[port-mapping user-defined]{lang="ES-AR"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1625546066}[[字段]{style="font-family:黑体"}]{#struct_0_56603_18771_x699680792}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_56603_18771_x1969478033}

[[Application]{lang="EN-US"}]{#struct_0_56603_18771_2077312642}

[[进行端口映射的应用层协议]{style="font-family:宋体"}]{#struct_0_56603_18771_1786766554}

[[Port]{lang="ES-AR"}]{#struct_0_56603_18771_2125750337}

[[应用层协议映射的端口号]{style="font-family:宋体"}]{#struct_0_56603_18771_x1689508031}

[[Protocol]{lang="ES-AR"}]{#struct_0_56603_18771_1215911551}

[[传输层协议类型]{style="font-family:宋体"}]{#struct_0_56603_18771_1925484392}

[[Match Type]{lang="ES-AR"}]{#struct_0_56603_18771_807690487}

[[匹配方式，包括以下类型：]{style="font-family:宋体"}]{#struct_0_56603_18771_1507992104}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\-\--]{lang="EN-US"}]{#struct_0_56603_18771_1786832090}[：表示通配，即未指定匹配类型和匹配条件，所有报文都可以进行匹配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 host]{lang="EN-US"}]{#struct_0_56603_18771_1000639804}[：表示基于]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}[的目的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址进行匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 host]{lang="EN-US"}]{#struct_0_56603_18771_1004223771}[：表示基于]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}[的目的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址进行匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 subnet]{lang="EN-US"}]{#struct_0_56603_18771_x22171758}[：表示基于]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}[的目的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[网段进行匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 subnet]{lang="EN-US"}]{#struct_0_56603_18771_x1724740376}[：表示基于]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}[的目的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[网段]{style="font-family:宋体"}[进行匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 ACL]{lang="EN-US"}]{#struct_0_56603_18771_658925823}[：表示基于]{lang="EN-US" style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[进行匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 ACL]{lang="EN-US"}]{#struct_0_56603_18771_1787290843}[：表示基于]{lang="EN-US" style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[进行匹配]{lang="EN-US" style="font-family:宋体"}

[[Match Condition]{lang="ES-AR"}]{#struct_0_56603_18771_203257783}

[[匹配条件，包括以下几种情况：]{style="font-family:宋体"}]{#struct_0_56603_18771_x396055831}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}[IPv4 host]{lang="EN-US"}]{#struct_0_56603_18771_1833141011}[/]{lang="EN-US"}[IPv6 host]{lang="EN-US"}[匹配方式，显示为]{style="font-family:
  宋体"}[主机]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}[的目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}[IPv4 subnet]{lang="EN-US"}]{#struct_0_56603_18771_x712073118}[/]{lang="EN-US"}[IPv6 subnet]{lang="EN-US"}[匹配方式，显示为]{style="font-family:
  宋体"}[主机]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}[的目的]{lang="EN-US" style="font-family:宋体"}[网段地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_56603_18771_1787356379}[IPv4 ACL/IPv6 ACL]{lang="EN-US"}[匹配方式，显示为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[host]{lang="EN-US"}]{#struct_0_56603_18771_1386438859}[和]{style="font-family:宋体"}[subnet]{lang="EN-US"}[类型的端口映射配置，如果指定了主机所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则还会显示其所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2111149125 .myid}
[]{#_Toc404793472}[]{#struct_0_56603_18771_563794449}[]{#_Toc329272279}[]{#_Toc329184390}[]{#_Toc325276361}

**APR \-- APR配置命令 \-- include application**

------------------------------------------------------------------------

[**[include application]{lang="EN-US"}**]{#struct_0_56603_18771_x1449447270}[命令用来在应用组中添加应用。]{style="font-family:宋体"}

[**[undo include application]{lang="EN-US"}**]{#struct_0_56603_18771_x1186947978}[命令用来在应用组中删除应用。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1572396405}

[**[include application]{lang="EN-US"}***[ application-name]{lang="EN-US"}*]{#struct_0_56603_18771_x479114541}

[**[undo include application ]{lang="EN-US"}***[application-name]{lang="EN-US"}*]{#struct_0_56603_18771_1787421915}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56603_18771_578743177}

[[应用组中不包含任何应用。]{style="font-family:宋体"}]{#struct_0_56603_18771_x2103256173}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_1435130394}

[[应用组视图]{style="font-family:宋体"}]{#struct_0_56603_18771_x452651787}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_x589857224}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x614423744}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_x300780337}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_1041494408}

[*[app]{lang="SV"}[lication]{lang="EN-US"}*]{#struct_0_56603_18771_1787487451}*[-name]{lang="SV"}*[：向应用组中添加的应用的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，可以为数字、字母、连字符、下划线，不允许为系统保留的]{style="font-family:宋体"}[invalid]{lang="EN-US"}[或]{style="font-family:宋体"}[other]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_1807537339}

[[可以通过多次执行本命令为一个应用组中添加多个预定义应用和自定义应用，]{style="font-family:宋体"}]{#struct_0_56603_18771_x1584299753}[每个组里最多可以包含]{style="font-family:宋体"}[65536]{lang="EN-US"}[个自定义应用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[向应用组中添加应用时，如果对应的应用不存在就会创建这个应用，但该应用的报文是否能被识别，取决于系统中是否定义了相应的识别规则，比如端口映射配置。]{style="font-family:宋体"}]{#struct_0_56603_18771_x786430857}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_634406126}

[[\# ]{lang="SV"}]{#struct_0_56603_18771_1420663530}[在应用组]{style="font-family:宋体"}[abc]{lang="SV"}[中增加应用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[和]{style="font-family:宋体"}[FTP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_61772140}

[\[Sysname\] app-group abc]{lang="EN-US"}

[\[Sysname-app-group-abc\] include application http]{lang="EN-US"}

[\[Sysname-app-group-abc\] include application ftp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x879364401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[app-group]{lang="EN-US"}**]{#struct_0_56603_18771_x152578934}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[copy app-group]{lang="EN-US"}**]{#struct_0_56603_18771_1787552987}
:::

::: {#568950091 .myid}
[]{#_Toc404793473}[]{#struct_0_56603_18771_972656032}[]{#_Toc329272290}[]{#_Toc329184404}[]{#_Toc316572034}

**APR \-- APR配置命令 \-- port-mapping**

------------------------------------------------------------------------

[]{#struct_0_56603_18771_2042450278}[**[port-mapping]{lang="EN-US"}**]{#_Toc329272291}[命令用来配置通用端口映射。]{style="font-family:宋体"}

[**[undo port-mapping]{lang="EN-US"}**]{#struct_0_56603_18771_x471189544}[命令用来删除指定的通用端口映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1507268475}

[**[port-mapping]{lang="EN-US"}**[ **application** *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_572143366}**[ ]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}[\[ **protocol** *protocol-name* \]]{lang="ES-AR"}

[**[undo port-mapping]{lang="EN-US"}**[ **application** *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_x1477017290}**[ ]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}[\[ **protocol** *protocol-name* \]]{lang="ES-AR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56603_18771_1087659898}

[[各应用层协议与其对应的知名端口号映射。]{style="font-family:宋体"}]{#struct_0_56603_18771_x1103018246}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_1787618523}

[[系统视图]{style="font-family:宋体"}]{#struct_0_56603_18771_x507981227}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1425709469}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_548250225}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_1207467426}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_x273514183}

[**[application]{lang="EN-US"}***[ application-name]{lang="EN-US"}*]{#struct_0_56603_18771_805426388}[：指定端口映射的应用层协议。]{style="font-family:宋体"}*[app-name]{lang="EN-US"}*[表示应用协议名称。该应用层协议名称必须标准且能够被设备识别，不区分大小写。]{style="font-family:宋体"}

[**[port]{lang="ES-AR"}**]{#struct_0_56603_18771_x412753645}*[ port-number]{lang="ES-AR"}*[：指定与应用层协议映射的端口。]{style="font-family:宋体"}*[port-number]{lang="ES-AR"}*[表示]{style="font-family:宋体"}[端口号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="ES-AR"}[～]{style="font-family:宋体"}[65535]{lang="ES-AR"}[。]{style="font-family:宋体"}

[**[protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*]{#struct_0_56603_18771_768177387}[：指定应用层协议使用的传输层协议名称，其取值及含义如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}**[dccp]{lang="EN-US"}**]{#struct_0_56603_18771_1787684059}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[DCCP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Datagram Congestion Control Protocol]{lang="PT-BR"}[，数据报拥塞控制协议）协议]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sctp]{lang="EN-US"}**]{#struct_0_56603_18771_1005603224}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[SCTP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Stream Control Transmission Protocol]{lang="PT-BR"}[，流控制传输协议）协议]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tcp]{lang="PT-BR"}**]{#struct_0_56603_18771_x1572163829}[：表示]{style="font-family:
宋体"}[TCP]{lang="PT-BR"}[协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp]{lang="EN-US"}**]{#struct_0_56603_18771_688011494}[：]{style="font-family:
宋体"}[表示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[udp-lite]{lang="SV"}**]{#struct_0_56603_18771_1349463036}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[UDP-Lite]{lang="SV"}[协议。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_x2001613128}

[[若不指定]{style="font-family:宋体"}**[protocol]{lang="EN-US"}**]{#struct_0_56603_18771_x1414565468}[参数，则表示]{style="font-family:宋体"}[所有传输层协议的指定报文均可被识别为指定应用层协议的报文。]{style="font-family:宋体"}

[[如果报文的目的端口号与某个通用端口映射匹配，则该报文将被识别为相应的应用层协议报文。]{style="font-family:宋体"}]{#struct_0_56603_18771_125382905}

[[对于端口号、传输层协议参数均相同但是应用层协议名称不相同的两个配置，新的配置会覆盖原有的配置。]{style="font-family:宋体"}]{#struct_0_56603_18771_1787749595}

[[指定传输层协议名称的映射优先级高于不指定传输层协议名称的映射。]{style="font-family:宋体"}]{#struct_0_56603_18771_x2075834662}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_x659678452}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1553700775}[建立端口]{style="font-family:宋体"}[3456]{lang="EN-US"}[到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的通用端口映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_x1206115160}

[\[Sysname\] port-mapping application ftp port 3456]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1996610629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-mapping user-defined]{lang="EN-US"}**]{#struct_0_56603_18771_1256282217}
:::

::: {#-1640911320 .myid}
[]{#_Toc404793474}[]{#struct_0_56603_18771_57031708}[]{#_Toc329272292}[]{#_Toc329184405}[]{#_Toc316572035}[]{#_Ref298764731}[]{#_Toc292975128}

**APR \-- APR配置命令 \-- port-mapping acl**

------------------------------------------------------------------------

[**[port-mapping acl]{lang="EN-US"}**]{#struct_0_56603_18771_x1445260374}[命令用来配置基于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的主机端口映射。]{style="font-family:宋体"}

[**[undo port-mapping acl]{lang="EN-US"}**]{#struct_0_56603_18771_1786766555}[命令用来删除指定的主机端口映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_2125815873}

[**[port-mapping]{lang="EN-US"}**[ **application** *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_x850343795}**[ ]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}[\[ **protocol** *protocol-name* \] ]{lang="ES-AR"}**[acl]{lang="EN-US"}**[ \[ **ipv6** \] *acl-number*]{lang="EN-US"}

[**[undo ]{lang="EN-US"}[port-mapping]{lang="EN-US"}**[ **application** *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_x2017618848}**[ ]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}[\[ **protocol** *protocol-name* \] ]{lang="ES-AR"}**[acl]{lang="EN-US"}**[ \[ **ipv6** \] *acl-number*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56603_18771_x375033263}

[[各应用层协议与其对应的知名端口号映射。]{style="font-family:宋体"}]{#struct_0_56603_18771_x315787724}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1049213091}

[[系统视图]{style="font-family:宋体"}]{#struct_0_56603_18771_1392984654}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_859253239}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_1786832091}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_1000574268}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_1383331245}

[**[application]{lang="EN-US"}***[ application-name]{lang="EN-US"}*]{#struct_0_56603_18771_748612652}[：指定端口映射的应用层协议。]{style="font-family:宋体"}*[application-name]{lang="EN-US"}*[表示应用层协议名称。该应用协议名称必须标准且能够被设备识别，不区分大小写。]{style="font-family:宋体"}

[**[port]{lang="ES-AR"}**]{#struct_0_56603_18771_x1804646651}*[ port-number]{lang="ES-AR"}*[：指定与应用层协议映射的端口。]{style="font-family:宋体"}*[port-number]{lang="ES-AR"}*[表示]{style="font-family:宋体"}[端口号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="ES-AR"}[～]{style="font-family:宋体"}[65535]{lang="ES-AR"}[。]{style="font-family:宋体"}

[**[protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*]{#struct_0_56603_18771_x1635371726}[：指定应用层协议使用的传输层协议名称，其取值及含义如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}**[dccp]{lang="EN-US"}**]{#struct_0_56603_18771_x480805108}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[DCCP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Datagram Congestion Control Protocol]{lang="PT-BR"}[，数据报拥塞控制协议）协议]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sctp]{lang="EN-US"}**]{#struct_0_56603_18771_527010933}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[SCTP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Stream Control Transmission Protocol]{lang="PT-BR"}[，流控制传输协议）协议]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tcp]{lang="PT-BR"}**]{#struct_0_56603_18771_x1363146128}[：表示]{style="font-family:
宋体"}[TCP]{lang="PT-BR"}[协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp]{lang="EN-US"}**]{#struct_0_56603_18771_1787290840}[：]{style="font-family:
宋体"}[表示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[udp-lite]{lang="SV"}**]{#struct_0_56603_18771_203454391}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[UDP-Lite]{lang="SV"}[协议。]{lang="EN-US" style="font-family:宋体"}

[**[acl]{lang="ES-AR"}**]{#struct_0_56603_18771_243170647}[ \[ **ipv6** \] *acl-number*]{lang="ES-AR"}[：]{style="font-family:宋体"}[ACL]{lang="ES-AR"}[编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="ES-AR"}[～]{style="font-family:宋体"}[2999]{lang="ES-AR"}[。如果指定]{style="font-family:宋体"}**[ipv6]{lang="ES-AR"}**[，则]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6 ACL]{lang="ES-AR"}[，]{style="font-family:宋体"}[否则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="ES-AR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_x955900086}

[[若不指定]{style="font-family:宋体"}**[protocol]{lang="EN-US"}**]{#struct_0_56603_18771_1799222006}[参数，则表示]{style="font-family:宋体"}[所有传输层协议的指定报文均可被识别为指定应用层协议的报文。]{style="font-family:宋体"}

[[对于匹配指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_56603_18771_x601788488}[的报文（其目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中某规则指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址参数相匹配），如果报文的目的端口号与某个映射关系匹配，则该报文将被识别为对应的应用层协议报文。]{style="font-family:宋体"}

[[对于端口号、传输层协议、]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_56603_18771_x622225820}[参数均相同但是应用层协议名称不相同的两个配置，新的配置会覆盖原有的配置。]{style="font-family:宋体"}

[[指定传输层协议名称的映射优先级高于不指定传输层协议名称的映射。]{style="font-family:宋体"}]{#struct_0_56603_18771_x2109955358}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_x2075049621}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_189966232}[为匹配]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[的报文，建立端口]{style="font-family:宋体"}[3456]{lang="EN-US"}[到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_1787356376}

[\[Sysname\] port-mapping application ftp port 3456 acl 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1386635467}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-mapping user-defined]{lang="EN-US"}**]{#struct_0_56603_18771_x322060751}
:::

::: {#-812520306 .myid}
[]{#_Toc404793475}[]{#struct_0_56603_18771_1048182895}[]{#_Toc329272293}[]{#_Toc329184406}[]{#_Toc316572036}[]{#_Ref298764861}[]{#_Toc292975129}

**APR \-- APR配置命令 \-- port-mapping host**

------------------------------------------------------------------------

[**[port-mapping host]{lang="EN-US"}**]{#struct_0_56603_18771_640768634}[命令用来设置基于]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的主机端口映射。]{style="font-family:宋体"}

[**[undo port-mapping host]{lang="EN-US"}**]{#struct_0_56603_18771_x822219151}[命令用来删除指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的主机端口映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1070668324}

[**[port-mapping]{lang="EN-US"}**[ **application** *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_1498386411}**[ ]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}[\[ **protocol** *protocol-name* \] ]{lang="ES-AR"}**[host ]{lang="EN-US"}**[{ **ip** *\|* **ipv6** } *start-ip-address* \[ *end-ip-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[**[undo port-mapping]{lang="EN-US"}**[ **application** *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_1787421912}**[ ]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}[\[ **protocol** *protocol-name* \] ]{lang="ES-AR"}**[host ]{lang="EN-US"}**[{ **ip** *\|* **ipv6** } *start-ip-address* \[ *end-ip-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56603_18771_578284425}

[[各应用层协议与其对应的知名端口号映射。]{style="font-family:宋体"}]{#struct_0_56603_18771_39729006}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_x596630271}

[[系统视图]{style="font-family:宋体"}]{#struct_0_56603_18771_x293919127}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1203827435}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_x1141302605}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_862734548}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_x24514560}

[**[application]{lang="EN-US"}***[ application-name]{lang="EN-US"}*]{#struct_0_56603_18771_1787487448}[：指定端口映射的应用层协议。]{style="font-family:宋体"}*[application-name]{lang="EN-US"}*[表示应用层协议名称，该应用协议名称必须标准且能够被设备识别，不区分大小写。]{style="font-family:宋体"}

[**[port]{lang="ES-AR"}**]{#struct_0_56603_18771_1806947514}*[ port-number]{lang="ES-AR"}*[：指定与应用层协议映射的端口。]{style="font-family:宋体"}*[port-number]{lang="ES-AR"}*[表示]{style="font-family:宋体"}[端口号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="ES-AR"}[～]{style="font-family:宋体"}[65535]{lang="ES-AR"}[。]{style="font-family:宋体"}

[**[protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*]{#struct_0_56603_18771_x848396139}[：指定应用层协议使用的传输层协议名称，其取值及含义如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}**[dccp]{lang="EN-US"}**]{#struct_0_56603_18771_x339782322}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[DCCP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Datagram Congestion Control Protocol]{lang="PT-BR"}[，数据报拥塞控制协议）协议]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sctp]{lang="EN-US"}**]{#struct_0_56603_18771_1498401774}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[SCTP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Stream Control Transmission Protocol]{lang="PT-BR"}[，流控制传输协议）协议]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tcp]{lang="PT-BR"}**]{#struct_0_56603_18771_x1403788405}[：表示]{style="font-family:
宋体"}[TCP]{lang="PT-BR"}[协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp]{lang="EN-US"}**]{#struct_0_56603_18771_1968051051}[：]{style="font-family:
宋体"}[表示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[udp-lite]{lang="SV"}**]{#struct_0_56603_18771_x1276000150}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[UDP-Lite]{lang="SV"}[协议。]{lang="EN-US" style="font-family:宋体"}

[**[ip]{lang="ES-AR"}**]{#struct_0_56603_18771_x1830673883}[：指定基于]{style="font-family:宋体"}[IPv4]{lang="ES-AR"}[地址的主机端口映射。]{style="font-family:宋体"}

[**[ipv6]{lang="ES-AR"}**]{#struct_0_56603_18771_1787552984}[：指定基于]{style="font-family:宋体"}[IPv6]{lang="ES-AR"}[地址的主机端口映射。]{style="font-family:宋体"}

[*[start-ip-address ]{lang="ES-AR"}*]{#struct_0_56603_18771_972852640}[\[ *end-ip-address* \]]{lang="ES-AR"}[：表示]{style="font-family:宋体"}[IPv4]{lang="ES-AR"}[地址范围或]{style="font-family:宋体"}[IPv6]{lang="ES-AR"}[地址范围]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[start-ip-address]{lang="ES-AR"}*[表示起始]{style="font-family:宋体"}[IP]{lang="ES-AR"}[地址，]{style="font-family:宋体"}*[end-ip-address]{lang="ES-AR"}*[表示终止]{style="font-family:宋体"}[IP]{lang="ES-AR"}[地址。]{style="font-family:宋体"}[如果仅配置]{style="font-family:宋体"}*[start-ip-address]{lang="ES-AR"}*[，则]{style="font-family:宋体"}[表示单个主机]{style="font-family:宋体"}[；]{style="font-family:宋体"}[如果同时配置]{style="font-family:宋体"}*[start-ip-address]{lang="ES-AR"}*[和]{style="font-family:宋体"}*[end-ip-address]{lang="ES-AR"}*[，则]{style="font-family:宋体"}[表示位于]{style="font-family:宋体"}*[start-ip-address]{lang="ES-AR"}*[和]{style="font-family:宋体"}*[end-ip-address]{lang="ES-AR"}*[范围内的所有主机，]{style="font-family:宋体"}[其中的]{style="font-family:宋体"}*[end-ip-address]{lang="EN-US"}*[必须大于等于]{style="font-family:宋体"}*[start-ip-address]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="ES-AR"}**]{#struct_0_56603_18771_x1999280082}*[vpn-]{lang="ES-AR"}[instance-]{lang="EN-US"}[name]{lang="ES-AR"}*[：表示报文所属的]{style="font-family:宋体"}[VPN]{lang="ES-AR"}[。]{style="font-family:宋体"}*[vpn-]{lang="ES-AR"}[instance-]{lang="EN-US"}[name]{lang="ES-AR"}*[为]{style="font-family:宋体"}[MPLS L3VPN]{lang="ES-AR"}[的]{style="font-family:宋体"}[VPN]{lang="ES-AR"}[实例名称，为]{style="font-family:宋体"}[1]{lang="ES-AR"}[～]{style="font-family:宋体"}[31]{lang="ES-AR"}[个字符的字符串，区分大小写。如果不指定该参数，则表示报文属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_1439825197}

[[若不指定]{style="font-family:宋体"}**[protocol]{lang="EN-US"}**]{#struct_0_56603_18771_x726545133}[参数，则表示]{style="font-family:宋体"}[所有传输层协议的指定报文均可被识别为指定应用层协议的报文。]{style="font-family:宋体"}

[[对于目的地址为指定地址或指定范围的地址的报文，如果报文的目的端口号与某个映射关系匹配，则该报文将被识别为对应的应用层协议报文。]{style="font-family:宋体"}]{#struct_0_56603_18771_2071044968}

[[对于应用协议、端口号、传输层协议参数均相同的配置，要求各配置中指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_56603_18771_x854983944}[地址或者]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围不能重叠。]{style="font-family:宋体"}

[[对于端口号、传输层协议、]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_56603_18771_x1839950567}[地址或地址范围参数均相同但是应用层协议名称不相同的两个配置，新的配置会覆盖原有的配置。]{style="font-family:宋体"}

[[指定传输层协议名称的映射优先级高于不指定传输层协议名称的映射。]{style="font-family:宋体"}]{#struct_0_56603_18771_1520822581}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_1787618520}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x507784619}[为目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[～]{style="font-family:宋体"}[1.1.1.10]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文，建立端口]{style="font-family:宋体"}[3456]{lang="EN-US"}[到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_1701168111}

[\[Sysname\] port-mapping application ftp port 3456 host ip 1.1.1.1 1.1.1.10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1893910689}[为目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文，建立端口]{style="font-family:宋体"}[3456]{lang="EN-US"}[到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_954292110}

[\[Sysname\] port-mapping application ftp port 3456 host ipv6 1::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x563816607}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-mapping user-defined]{lang="EN-US"}**]{#struct_0_56603_18771_x1266688663}
:::

::: {#406922500 .myid}
[]{#_Toc404793476}[]{#struct_0_56603_18771_1875933681}[]{#_Toc329272294}[]{#_Toc329184407}[]{#_Toc316572037}[]{#_Ref298764870}[]{#_Toc292975187}[]{#_Toc292975130}[]{#_Toc292975131}[]{#_Toc292975132}[]{#_Toc292975133}[]{#_Toc292975134}[]{#_Toc292975135}[]{#_Toc292975136}[]{#_Toc292975137}[]{#_Toc292975138}[]{#_Toc292975139}[]{#_Toc292975140}[]{#_Toc292975141}[]{#_Toc292975142}[]{#_Toc292975143}[]{#_Toc292975144}[]{#_Toc292975145}[]{#_Toc292975146}[]{#_Toc292975147}[]{#_Toc292975148}[]{#_Toc292975149}[]{#_Toc292975150}[]{#_Toc292975151}[]{#_Toc292975152}[]{#_Toc292975153}[]{#_Toc292975154}[]{#_Toc292975155}[]{#_Toc292975156}[]{#_Toc292975157}[]{#_Toc292975158}[]{#_Toc292975159}[]{#_Toc292975160}[]{#_Toc292975161}[]{#_Toc292975162}[]{#_Toc292975163}[]{#_Toc292975164}[]{#_Toc292975165}[]{#_Toc292975166}[]{#_Toc292975167}[]{#_Toc292975168}[]{#_Toc292975169}[]{#_Toc292975170}[]{#_Toc292975171}[]{#_Toc292975172}[]{#_Toc292975173}[]{#_Toc292975174}[]{#_Toc292975175}[]{#_Toc292975176}[]{#_Toc292975177}[]{#_Toc292975178}[]{#_Toc292975179}[]{#_Toc292975180}[]{#_Toc292975181}[]{#_Toc292975182}[]{#_Toc292975183}[]{#_Toc292975184}[]{#_Toc292975185}[]{#_Toc292975186}

**APR \-- APR配置命令 \-- port-mapping subnet**

------------------------------------------------------------------------

[**[port-mapping subnet]{lang="EN-US"}**]{#struct_0_56603_18771_1309583491}[命令用来配置基于网段的主机端口映射。]{style="font-family:宋体"}

[**[undo port-mapping subnet]{lang="EN-US"}**]{#struct_0_56603_18771_1787684056}[命令用来删除指定网段的主机端口映射。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_1005930904}

[**[port-mapping]{lang="EN-US"}**[ **application** *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_1194992323}**[ ]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}[\[ **protocol** *protocol-name* \] ]{lang="ES-AR"}**[subnet ]{lang="EN-US"}**[{ **ip** *ipv4-address* { *mask-length* \| *mask* } \| **ipv6** *ipv6-address* *prefix-length* } \[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}

[**[undo port-mapping]{lang="EN-US"}**[ **application** *application-name*]{lang="EN-US"}]{#struct_0_56603_18771_113471054}**[ ]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}[\[ **protocol** *protocol-name* \] ]{lang="ES-AR"}**[subnet ]{lang="EN-US"}**[{ **ip** *ipv4-address* { *mask-length* \| *mask* } \| **ipv6** *ipv6-address* *prefix-length* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_56603_18771_x394980162}

[[各应用层协议与其对应的知名端口号映射。]{style="font-family:宋体"}]{#struct_0_56603_18771_1522280068}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1079364573}

[[系统视图]{style="font-family:宋体"}]{#struct_0_56603_18771_x1256226473}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1593131643}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_1787749592}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_x2076031270}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_2088055347}

[**[application]{lang="EN-US"}***[ application-name]{lang="EN-US"}*]{#struct_0_56603_18771_1820832252}[：指定端口映射的应用层协议。]{style="font-family:宋体"}*[application-name]{lang="EN-US"}*[表示应用层协议名称。该应用协议名称必须标准且能够被设备识别，不区分大小写。]{style="font-family:宋体"}

[**[port]{lang="ES-AR"}**]{#struct_0_56603_18771_450042897}*[ port-number]{lang="ES-AR"}*[：指定与应用层协议映射的端口。]{style="font-family:宋体"}*[port-number]{lang="ES-AR"}*[表示]{style="font-family:宋体"}[端口号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="ES-AR"}[～]{style="font-family:宋体"}[65535]{lang="ES-AR"}[。]{style="font-family:宋体"}

[**[protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*]{#struct_0_56603_18771_126006343}[：指定应用层协议使用的传输层协议名称，其取值及含义如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="ES-AR" style="font-size:10.0pt;font-family:Symbol"}**[dccp]{lang="EN-US"}**]{#struct_0_56603_18771_1584378270}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[DCCP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Datagram Congestion Control Protocol]{lang="PT-BR"}[，数据报拥塞控制协议）]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sctp]{lang="EN-US"}**]{#struct_0_56603_18771_1317130941}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[SCTP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Stream Control Transmission Protocol]{lang="PT-BR"}[，流控制传输协议）]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tcp]{lang="PT-BR"}**]{#struct_0_56603_18771_1173292298}[：表示]{style="font-family:
宋体"}[TCP]{lang="PT-BR"}[协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[udp]{lang="EN-US"}**]{#struct_0_56603_18771_1786766552}[：]{style="font-family:
宋体"}[表示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[协议]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[udp-lite]{lang="SV"}**]{#struct_0_56603_18771_2125881409}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[UDP-Lite]{lang="SV"}[协议。]{lang="EN-US" style="font-family:宋体"}

[**[ip]{lang="ES-AR"}**]{#struct_0_56603_18771_x536110350}[：指定基于]{style="font-family:宋体"}[IPv4]{lang="ES-AR"}[网段的主机端口映射。]{style="font-family:宋体"}

[*[ipv4-address]{lang="ES-AR"}*]{#struct_0_56603_18771_x796073462}[ { *mask-length* \| *mask* }]{lang="ES-AR"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv4]{lang="ES-AR"}[网段。其中，]{style="font-family:宋体"}*[ipv4-address]{lang="ES-AR"}*[表示]{style="font-family:宋体"}[IPv4]{lang="ES-AR"}[地址；]{style="font-family:宋体"}*[mask-length]{lang="ES-AR"}*[表示子网掩码长度，取值范围为]{style="font-family:宋体"}[1]{lang="ES-AR"}[～]{style="font-family:宋体"}[32]{lang="ES-AR"}[；]{style="font-family:宋体"}*[mask]{lang="ES-AR"}*[表示子网掩码，为点分十进制格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="ES-AR"}**]{#struct_0_56603_18771_333956973}[：指定基于]{style="font-family:宋体"}[IPv6]{lang="ES-AR"}[网段的主机端口映射。]{style="font-family:宋体"}

[*[ipv6-address prefix-length]{lang="EN-US"}*]{#struct_0_56603_18771_1511603518}[：]{style="font-family:
宋体"}[指定]{style="font-family:宋体"}[IPv6]{lang="ES-AR"}[网段。其中，]{style="font-family:宋体"}*[ipv6-address]{lang="ES-AR"}*[表示]{style="font-family:宋体"}[IPv6]{lang="ES-AR"}[地址；]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="ES-AR"}[前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="ES-AR"}[～]{style="font-family:宋体"}[128]{lang="ES-AR"}[。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="ES-AR"}**]{#struct_0_56603_18771_x1652250862}*[vpn-]{lang="ES-AR"}[instance-]{lang="EN-US"}[name]{lang="ES-AR"}*[：表示主机所属的]{style="font-family:宋体"}[VPN]{lang="ES-AR"}[。]{style="font-family:宋体"}*[vpn-]{lang="ES-AR"}[instance-]{lang="EN-US"}[name]{lang="ES-AR"}*[为]{style="font-family:宋体"}[MPLS L3VPN]{lang="ES-AR"}[的]{style="font-family:宋体"}[VPN]{lang="ES-AR"}[实例名称，为]{style="font-family:宋体"}[1]{lang="ES-AR"}[～]{style="font-family:宋体"}[31]{lang="ES-AR"}[个字符的字符串，区分大小写。如果不指定该参数，则表示主机属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1645288669}

[[若不指定]{style="font-family:宋体"}**[protocol]{lang="EN-US"}**]{#struct_0_56603_18771_2059188989}[参数，则表示]{style="font-family:宋体"}[所有传输层协议的指定端口的报文均被识别为指定应用层协议的报文。]{style="font-family:宋体"}

[[对于目的地址为指定网段的报文，如果报文的目的端口号与某个映射关系匹配，则该报文将被识别为对应的应用层协议报文。]{style="font-family:宋体"}]{#struct_0_56603_18771_1786832088}

[[PBAR]{lang="EN-US"}]{#struct_0_56603_18771_1001164091}[以最精确的网络范围对报文进行匹配，即如果配置了多条网段映射关系，且各映射关系中指定的网段范围互相包含，则使用网络范围最小的映射配置进行匹配。]{style="font-family:宋体"}

[[对于端口号、传输层协议、]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_56603_18771_x1743849936}[网段参数均相同但是应用层协议名称不相同的两个配置，新的配置会覆盖原有的配置。]{style="font-family:宋体"}

[[指定传输层协议名称的映射优先级高于不指定传输层协议名称的映射。]{style="font-family:宋体"}]{#struct_0_56603_18771_1836738726}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_1324071316}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x256137094}[为目的网段地址为]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[主机报文，建立端口]{style="font-family:宋体"}[3456]{lang="EN-US"}[到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_x1065827902}

[\[Sysname\] port-mapping application ftp port 3456 subnet ip 1.1.1.0 24]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x716051368}[为目的网段地址为]{style="font-family:宋体"}[1:: /120]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[主机报文，建立端口]{style="font-family:宋体"}[3456]{lang="EN-US"}[到]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议的映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_56603_18771_1787290841}

[\[Sysname\] port-mapping application ftp port 3456 subnet ipv6 1:: 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_203388855}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-mapping user-defined]{lang="EN-US"}**]{#struct_0_56603_18771_289778799}
:::

::: {#1570268031 .myid}
[]{#_Toc404793477}[]{#struct_0_56603_18771_x1254375265}[]{#_Toc329272287}[]{#_Toc329184399}[]{#_Toc325276370}[]{#_Toc311133303}[]{#_Toc311133367}[]{#_Toc313523055}[]{#_Toc311133304}[]{#_Toc311133368}[]{#_Toc313523056}[]{#_Toc311133305}[]{#_Toc311133369}[]{#_Toc313523057}[]{#_Toc311133306}[]{#_Toc311133370}[]{#_Toc313523058}[]{#_Toc311133307}[]{#_Toc311133371}[]{#_Toc313523059}[]{#_Toc311133308}[]{#_Toc311133372}[]{#_Toc313523060}[]{#_Toc311133309}[]{#_Toc311133373}[]{#_Toc313523061}[]{#_Toc311133310}[]{#_Toc311133374}[]{#_Toc313523062}[]{#_Toc311133311}[]{#_Toc311133375}[]{#_Toc313523063}[]{#_Toc311133312}[]{#_Toc311133376}[]{#_Toc313523064}[]{#_Toc311133314}[]{#_Toc311133378}[]{#_Toc313523066}[]{#_Toc311133315}[]{#_Toc311133379}[]{#_Toc313523067}[]{#_Toc311133316}[]{#_Toc311133380}[]{#_Toc313523068}[]{#_Toc311133317}[]{#_Toc311133381}[]{#_Toc313523069}[]{#_Toc311133318}[]{#_Toc311133382}[]{#_Toc313523070}[]{#_Toc311133319}[]{#_Toc311133383}[]{#_Toc313523071}[]{#_Toc311133320}[]{#_Toc311133384}[]{#_Toc313523072}[]{#_Toc311133321}[]{#_Toc311133385}[]{#_Toc313523073}[]{#_Toc311133322}[]{#_Toc311133386}[]{#_Toc313523074}[]{#_Toc311133323}[]{#_Toc311133387}[]{#_Toc313523075}[]{#_Toc311133324}[]{#_Toc311133388}[]{#_Toc313523076}[]{#_Toc311133325}[]{#_Toc311133389}[]{#_Toc313523077}[]{#_Toc311133326}[]{#_Toc311133390}[]{#_Toc313523078}[]{#_Toc311133327}[]{#_Toc311133391}[]{#_Toc313523079}[]{#_Toc311133328}[]{#_Toc311133392}[]{#_Toc313523080}[]{#_Toc311133329}[]{#_Toc311133393}[]{#_Toc313523081}[]{#_Toc311133330}[]{#_Toc311133394}[]{#_Toc313523082}[]{#_Toc311133331}[]{#_Toc311133395}[]{#_Toc313523083}[]{#_Toc311133332}[]{#_Toc311133396}[]{#_Toc313523084}[]{#_Toc311133333}[]{#_Toc311133397}[]{#_Toc313523085}[]{#_Toc292975189}[]{#_Toc292975190}[]{#_Toc292975191}[]{#_Toc292975192}[]{#_Toc292975193}[]{#_Toc292975194}[]{#_Toc292975195}[]{#_Toc292975196}[]{#_Toc292975197}[]{#_Toc292975198}[]{#_Toc292975199}[]{#_Toc292975200}[]{#_Toc292975201}[]{#_Toc292975202}[]{#_Toc292975203}[]{#_Toc292975204}[]{#_Toc292975205}[]{#_Toc292975206}[]{#_Toc292975207}[]{#_Toc292975208}[]{#_Toc292975209}[]{#_Toc292975210}[]{#_Toc292975211}[]{#_Toc292975212}[]{#_Toc292975213}[]{#_Toc292975214}[]{#_Toc292975215}[]{#_Toc292975216}[]{#_Toc292975217}[]{#_Toc292975218}[]{#_Toc292975219}[]{#_Toc292975220}[]{#_Toc292975221}[]{#_Toc292975222}[]{#_Toc292975223}[]{#_Toc292975224}[]{#_Toc292975225}[]{#_Toc292975226}[]{#_Toc292975227}[]{#_Toc292975228}[]{#_Toc292975229}[]{#_Toc292975230}[]{#_Toc292975231}[]{#_Toc292975232}[]{#_Toc292975233}[]{#_Toc292975234}[]{#_Toc292975235}[]{#_Toc292975236}[]{#_Toc292975237}[]{#_Toc292975238}[]{#_Toc292975239}[]{#_Toc292975240}[]{#_Toc292975241}[]{#_Toc292975242}[]{#_Toc292975243}[]{#_Toc292975244}[]{#_Toc292975245}[]{#_Toc311133334}[]{#_Toc311133398}[]{#_Toc313523086}[]{#_Toc311133335}[]{#_Toc311133399}[]{#_Toc313523087}[]{#_Toc311133336}[]{#_Toc311133400}[]{#_Toc313523088}[]{#_Toc311133337}[]{#_Toc311133401}[]{#_Toc313523089}[]{#_Toc311133338}[]{#_Toc311133402}[]{#_Toc313523090}[]{#_Toc311133339}[]{#_Toc311133403}[]{#_Toc313523091}[]{#_Toc311133340}[]{#_Toc311133404}[]{#_Toc313523092}[]{#_Toc311133341}[]{#_Toc311133405}[]{#_Toc313523093}[]{#_Toc311133342}[]{#_Toc311133406}[]{#_Toc313523094}[]{#_Toc311133344}[]{#_Toc311133408}[]{#_Toc313523096}[]{#_Toc311133345}[]{#_Toc311133409}[]{#_Toc313523097}[]{#_Toc311133346}[]{#_Toc311133410}[]{#_Toc313523098}[]{#_Toc311133347}[]{#_Toc311133411}[]{#_Toc313523099}[]{#_Toc311133348}[]{#_Toc311133412}[]{#_Toc313523100}[]{#_Toc311133349}[]{#_Toc311133413}[]{#_Toc313523101}[]{#_Toc311133350}[]{#_Toc311133414}[]{#_Toc313523102}[]{#_Toc311133351}[]{#_Toc311133415}[]{#_Toc313523103}[]{#_Toc311133352}[]{#_Toc311133416}[]{#_Toc313523104}[]{#_Toc311133353}[]{#_Toc311133417}[]{#_Toc313523105}[]{#_Toc311133354}[]{#_Toc311133418}[]{#_Toc313523106}[]{#_Toc311133355}[]{#_Toc311133419}[]{#_Toc313523107}[]{#_Toc311133356}[]{#_Toc311133420}[]{#_Toc313523108}[]{#_Toc311133357}[]{#_Toc311133421}[]{#_Toc313523109}[]{#_Toc311133358}[]{#_Toc311133422}[]{#_Toc313523110}

**APR \-- APR配置命令 \-- reset application statistics**

------------------------------------------------------------------------

[**[reset application statistics]{lang="EN-US"}**]{#struct_0_56603_18771_x249890396}[命令用来清除指定接口或所有接口的应用统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_x1042935335}

[**[reset application statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_56603_18771_x1481089310}

[[【视图】]{style="font-family:黑体"}]{#struct_0_56603_18771_x891767437}

[[用户视图]{style="font-family:宋体"}]{#struct_0_56603_18771_x2044618010}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_56603_18771_1787356377}

[[network-admin]{lang="EN-US"}]{#struct_0_56603_18771_1386569931}

[[mdc-admin]{lang="EN-US"}]{#struct_0_56603_18771_1350977169}

[[【参数】]{style="font-family:黑体"}]{#struct_0_56603_18771_255062959}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_56603_18771_x1098888955}[：清除指定接口上的应用统计信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_56603_18771_41785327}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_x1036317216}[清除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的应和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset application statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_56603_18771_x947449364}

[[\# ]{lang="EN-US"}]{#struct_0_56603_18771_1120217799}[清除所有统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset application statistics ]{lang="EN-US"}]{#struct_0_56603_18771_1787421913}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_56603_18771_578349961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[application statistics enable]{lang="EN-US"}**]{#struct_0_56603_18771_894580405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display application statistics]{lang="EN-US"}**]{#struct_0_56603_18771_x1827304448}
:::
