::::: {#-1675561441 .myid}
[]{#_Toc404792083}[]{#struct_0_x2723_x1019_1867311219}

**HQoS \-- 转发类配置命令 \-- display qos forwarding-class**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_x1251096437}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_x1967242345}
:::

[ ]{lang="EN-US"}

[**[display qos forwarding-class]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1117420300}[命令用来显示转发类的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_76191582}

[**[display qos forwarding-class]{lang="EN-US"}**[ \[ **name** *fc-name* \]]{lang="EN-US"}]{#struct_0_x2723_x1019_x1027565189}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1892998890}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x2080918857}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x452623013}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_575182073}

[[network-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_1906381479}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x241002329}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_706422582}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1929066058}

[*[fc-name]{lang="EN-US"}*]{#struct_0_x2723_x1019_1528711081}[：转发类的名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将]{style="font-family:宋体"}[显示所有转发类的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1494112223}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_1270904353}[显示指定转发类的信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos forwarding-class name BE]{lang="EN-US"}]{#struct_0_x2723_x1019_x244185519}

[Forwarding class: BE, ID: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1522486533}[显示所有转发类的信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos forwarding-class]{lang="EN-US"}]{#struct_0_x2723_x1019_x831043248}

[Forwarding class: BE, ID: 0]{lang="EN-US"}

[Forwarding class: AF, ID: 1]{lang="EN-US"}

[Forwarding class: EF, ID: 2]{lang="EN-US"}

[Forwarding class: NC, ID: 3]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display qos forwarding-class]{lang="EN-US"}]{#struct_0_x2723_x1019_564811334}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1023305282}[[字段]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x910442989}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_683665775}

[[Forwarding class]{lang="EN-US"}]{#struct_0_x2723_x1019_1365612700}

[[转发类的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x460571456}

[[ID]{lang="EN-US"}]{#struct_0_x2723_x1019_288724421}

[[转发类的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2723_x1019_1734360348}

[]{#_Toc358382998}[]{#_Toc357857442}[]{#_Toc345167685}[[ ]{lang="EN-US"}]{#_Toc339901008}

::::: {#754409639 .myid}
[]{#_Toc404792084}[]{#struct_0_x2723_x1019_x1984686783}

**HQoS \-- 转发类配置命令 \-- remark forwarding-class**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 8 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_565997928}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_x1929131594}
:::

[ ]{lang="EN-US"}

[**[remark forwarding-class]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1924941325}[命令用来重新标记流所属的转发类。]{style="font-family:宋体"}

[**[undo remark forwarding-class]{lang="EN-US"}**]{#struct_0_x2723_x1019_1224145258}[命令用来取消重新标记操作。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x422128139}

[**[remark forwarding-class]{lang="EN-US"}**[ { **id** *fc-id* \| **name** *fc-name* }]{lang="EN-US"}]{#struct_0_x2723_x1019_1845536172}

[**[undo remark forwarding-class]{lang="EN-US"}**]{#struct_0_x2723_x1019_x825260148}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1362820942}

[[未配置重标记转发类功能。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_980439188}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1707718328}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1966684066}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1359438023}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x954604284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1692589977}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x550895923}

[**[id]{lang="EN-US"}**[ *[fc-id]{style="color:black"}*]{lang="EN-US"}]{#struct_0_x2723_x1019_x273110009}[：]{style="font-family:宋体;color:black"}[转发类索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。此转发类索引只能是系统预定义转发类的索引。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *[fc-name]{style="color:black"}*]{lang="EN-US"}]{#struct_0_x2723_x1019_818086396}[：]{style="font-family:宋体"}[转发类名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。此转发类只能是系统预定义转发类。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x128049814}

[[如果同一个流行为中多次配置重标记转发类，那么最后一次的配置生效。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_674437606}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x424252911}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1929197130}[重新标记流所属的转发类为]{style="font-family:宋体"}[BE]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_1159837609}

[\[Sysname\] traffic behavior testtb]{lang="EN-US"}

[\[Sysname-behavior-testtb\] remark forwarding-class name BE]{lang="EN-US"}
:::::

::: {#1596120919 .myid}
[]{#_Toc404792086}[]{#struct_0_x2723_x1019_275256060}

**HQoS \-- 转发组配置命令 \-- display qos forwarding-group**

------------------------------------------------------------------------

[**[display qos forwarding-group]{lang="EN-US"}**]{#struct_0_x2723_x1019_x574809934}[命令用来显示转发组的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1970727314}

[**[d]{lang="EN-US"}[isplay qos forwarding-group]{lang="EN-US"}**[ \[ **name** *fg-name* \]]{lang="EN-US"}]{#struct_0_x2723_x1019_x1377862738}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x860962941}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1064176347}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_277548883}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1278311378}

[[network-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_653372492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x864738268}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_x1097433971}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x2723_x1019_5779999}

[*[fg-name]{lang="EN-US"}*]{#struct_0_x2723_x1019_x823325876}[：]{style="font-family:宋体"}[转发组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有转发组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x410541267}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_1665490405}[显示指定转发组的信息，转发组下嵌套转发组。]{style="font-family:宋体"}

[[\<Sysname\> display qos forwarding-group name testfg1]{lang="EN-US"}]{#struct_0_x2723_x1019_x1928738378}

[Forwarding group: testfg1, ID: 10]{lang="EN-US"}

[ match service-vlan-id 1 to 10]{lang="EN-US"}

[  Forwarding group: subfg1, ID: 1, profile: fgprofile1]{lang="EN-US"}

[ match service-vlan-id 11 to 20]{lang="EN-US"}

[  Forwarding group: subfg2, ID: 2, profile: fgprofile2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_889012946}[显示指定转发组的信息，转发组下嵌套转发类。]{style="font-family:宋体"}

[[\<Sysname\> display qos forwarding-group name testfg2]{lang="EN-US"}]{#struct_0_x2723_x1019_x42772248}

[Forwarding group: testfg2, ID: 10]{lang="EN-US"}

[ Forwarding class: BE, ID: 0, profile: fcprofile1]{lang="EN-US"}

[ Forwarding class: AF, ID: 1, profile: fcprofile2]{lang="EN-US"}

[ Forwarding class: EF, ID: 2, profile: fcprofile3]{lang="EN-US"}

[ Forwarding class: NC, ID: 3, profile: fcprofile4]{lang="EN-US"}

[]{#struct_0_x2723_x1019_864742073}[[表1-2 ]{lang="EN-US"}[display qos forwarding-group]{lang="EN-US"}]{#_Toc148586890}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1019806344}[[字段]{style="font-family:黑体"}]{#struct_0_x2723_x1019_859528443}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1383054112}

[[Forwarding group]{lang="EN-US"}]{#struct_0_x2723_x1019_904055591}

[[转发组的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_92865419}

[[Forwarding class]{lang="EN-US"}]{#struct_0_x2723_x1019_1648287029}

[[转发类的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x920584946}

[[ID]{lang="EN-US"}]{#struct_0_x2723_x1019_x2040975663}

[[转发组或转发类的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2723_x1019_1514093103}

[[match]{lang="EN-US"}]{#struct_0_x2723_x1019_x775706797}

[[match]{lang="EN-US"}]{#struct_0_x2723_x1019_x1405174198}[方式实例化]{style="font-family:宋体"}

[[profile]{lang="EN-US"}]{#struct_0_x2723_x1019_x1928803914}

[[转发策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x132885515}

[]{#_Toc358383001}[]{#_Toc357857445}[]{#_Toc345167688}[[ ]{lang="EN-US"}]{#_Toc339901011}

::::: {#-197893238 .myid}
[]{#_Toc404792087}[]{#struct_0_x2723_x1019_1331665935}

**HQoS \-- 转发组配置命令 \-- forwarding-class profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 10 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_579784143}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_756732328}
:::

[ ]{lang="EN-US"}

[**[forwarding-class]{lang="EN-US"}**[ **profile**]{lang="EN-US"}]{#struct_0_x2723_x1019_x1084778563}[命令用来配置转发组嵌套一个转发类，并为该转发类指定转发策略。]{style="font-family:宋体"}

[**[undo forwarding-class]{lang="EN-US"}**]{#struct_0_x2723_x1019_x437830888}[命令用来取消转发组嵌套的转发类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x993402081}

[**[forwarding-class]{lang="EN-US" style="color:black"}**[ *fc-name* **profile** *fp-name*]{lang="EN-US" style="color:black"}]{#struct_0_x2723_x1019_x807518985}

[**[undo forwarding-class]{lang="EN-US" style="color:black"}**[ *fc-name*]{lang="EN-US" style="color:black"}]{#struct_0_x2723_x1019_1090426403}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x588365473}

[[自定义转发组不嵌套转发类。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1372025944}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_963054646}

[[转发组视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1873983129}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1858104081}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x234925442}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1928869450}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1824629484}

[*[fc-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_x246002407}[：]{style="font-family:
宋体"}[转发类名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写，此转发类只能是系统预定义转发类。]{style="font-family:宋体"}

[**[profile]{lang="EN-US" style="color:black"}***[ fp-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_x847304908}[：]{style="font-family:宋体"}[转发策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_2133278337}

[[预定义转发组下默认嵌套的转发类不允许修改与删除。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1057706705}

[[在转发组内嵌套转发类时需要保证转发类和对应的转发策略都已经存在。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1761757825}

[[转发组中已经嵌套转发组时不能再嵌套转发类。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1801927096}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_326795421}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_1985813648}[在转发组]{style="font-family:宋体"}[testfg]{lang="EN-US"}[中嵌套转发类]{style="font-family:宋体"}[BE]{lang="EN-US"}[，并指定转发类]{style="font-family:宋体"}[BE]{lang="EN-US"}[的转发策略为]{style="font-family:宋体"}[testfp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_2034696659}

[\[Sysname\] qos forwarding-group testfg]{lang="EN-US"}

[\[Sysname-hqos-fg-testfg\] forwarding-class BE profile testfp]{lang="EN-US"}
:::::

::::: {#-1758211667 .myid}
[]{#_Toc404792088}[]{#struct_0_x2723_x1019_212541355}[]{#_Toc358383003}[]{#_Toc357857447}[]{#_Toc345167690}

**HQoS \-- 转发组配置命令 \-- forwarding-group profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_x1700559439}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_2078209958}
:::

[ ]{lang="EN-US"}

[**[forwarding-group]{lang="EN-US"}**[ profile]{lang="EN-US"}]{#struct_0_x2723_x1019_2095320782}[命令用来在转发组指定匹配规则中嵌套一个转发组，并为该转发组指定转发策略。]{style="font-family:宋体"}

[**[undo forwarding-group]{lang="EN-US"}**]{#struct_0_x2723_x1019_x858502255}[命令用来从转发组指定匹配规则下取消嵌套指定的转发组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_545786169}

[**[forwarding-group]{lang="EN-US" style="color:black"}**[ *sub-fg-name* **profile** *fp-name*]{lang="EN-US" style="color:black"}]{#struct_0_x2723_x1019_1915985409}

[**[undo forwarding-group]{lang="EN-US" style="color:black"}**[ *sub-fg-name*]{lang="EN-US" style="color:black"}]{#struct_0_x2723_x1019_x1928934986}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1860489446}

[[自定义转发组下不嵌套转发组。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_728441607}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x731560393}

[[转发组匹配规则视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1353457030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_880748791}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_345217761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x2125140940}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x552483068}

[*[sub-fg-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_345543869}[：子]{style="font-family:宋体"}[转发组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[profile]{lang="EN-US" style="color:black"}***[ fp-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_x1569078814}[：转发策略名称，]{style="font-family:宋体;
color:black"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x2723_x1019_4412953}

[[在转发组内嵌套转发组时需要保证转发组和对应的转发策略都已经存在。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_432641771}

[[转发组中已经嵌套转发类时不能再嵌套转发组。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_374516423}

[[已经嵌套了转发组的转发组不能被其他转发组嵌套。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1907058885}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1086666566}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x55053524}[在转发组]{style="font-family:宋体"}[testfg]{lang="EN-US"}[中指定匹配]{style="font-family:宋体"}[Service VLAN ID 2]{lang="EN-US"}[的流量嵌套转发组]{style="font-family:宋体"}[subfg]{lang="EN-US"}[，并指定转发组]{style="font-family:宋体"}[subfg]{lang="EN-US"}[的转发策略为]{style="font-family:宋体"}[testfp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x1928476234}

[\[Sysname\] qos forwarding-group testfg]{lang="EN-US"}

[\[Sysname-hqos-fg-testfg\] match service-vlan-id 2]{lang="EN-US"}

[\[Sysname-hqos-fg-testfg-match\] forwarding-group subfg profile testfp]{lang="EN-US"}
:::::

::::: {#461028519 .myid}
[]{#_Toc404792089}[]{#struct_0_x2723_x1019_1849046315}[]{#_Toc358383002}[]{#_Toc357857446}[]{#_Toc345167689}

**HQoS \-- 转发组配置命令 \-- match**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 12 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_414156851}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_1004524493}[       ]{lang="EN-US"}
:::

[ ]{lang="EN-US"}

[**[match]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1218841156}[命令用来配置转发组的匹配规则，并进入匹配规则视图。]{style="font-family:宋体"}

[**[undo match]{lang="EN-US"}**]{#struct_0_x2723_x1019_839022358}[命令用来取消转发组的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_635049135}

[**[match]{lang="EN-US"}**[ *match-criteria*]{lang="EN-US"}]{#struct_0_x2723_x1019_x953838990}

[**[undo match]{lang="EN-US"}**[ *match-criteria*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1974102036}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1585324337}

[[自定义转发组下无匹配规则。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x13245247}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_918342606}

[[转发组视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x280199734}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1116279849}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_1734817192}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1185761718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x2080828880}

[*[match-criteria]{lang="EN-US"}*]{#struct_0_x2723_x1019_x2117235279}[：转发组的匹配规则，具体情况如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?461028519#_Ref360725646)[所示。]{style="font-family:宋体"}

[]{#struct_0_x2723_x1019_x1928541770}[[表1-3 ]{lang="EN-US"}[转发组的匹配规则取值]{style="font-family:
黑体"}]{#_Ref360725646}

[]{#table_struct_0_x992406331}[[取值]{style="font-family:黑体"}]{#struct_0_x2723_x1019_472953571}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1607679697}

[[service-vlan-id *vlan-id-list*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1595411484}

[[定义匹配运营商网络]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x2723_x1019_x1501383248}[的规则]{style="font-family:宋体"}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x2723_x1019_1880318693}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[vlan-id-list ]{lang="EN-US"}*[= { *vlan-id* \| *vlan-id1* **to** *vlan-id2* }&\<1-8\>]{lang="EN-US"}[，]{style="font-family:
  宋体"}*[vlan-id]{lang="EN-US"}*[、]{style="font-family:
  宋体"}*[vlan-id1]{lang="EN-US"}*[ ]{lang="EN-US"}[、]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，且]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[必须小于或等于]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[；]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[[local-precedence *precedence-value-list*]{lang="EN-US"}]{#struct_0_x2723_x1019_1007538870}

[[定义匹配本地优先级的规则]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1373845478}

[*[precedence-value-list]{lang="EN-US"}*]{#struct_0_x2723_x1019_x176705778}*[：]{style="font-family:
  宋体"}*[本地优先级列表，]{style="font-family:宋体"}[表示方式为]{style="font-family:宋体"}*[precedence-value-list]{lang="EN-US"}*[ = { *precedence-value* \| *precedence-value1* **to** *precedence-value2* }&\<1-8\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}*[、]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}[1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}[2]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，且]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}[1]{lang="EN-US"}*[必须小于或等于]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}[2]{lang="EN-US"}*[；]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[[dot1p *dot1p-value-list*]{lang="EN-US"}]{#struct_0_x2723_x1019_x708026254}

[[定义匹配运营商网络]{style="font-family:宋体"}[802.1p]{lang="EN-US"}]{#struct_0_x2723_x1019_994367920}[优先级的规则]{style="font-family:宋体"}

[*[dot1p-value-list]{lang="EN-US"}*]{#struct_0_x2723_x1019_x1368163665}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级列表，表示方式为]{style="font-family:宋体"}*[dot1p-value-list ]{lang="EN-US"}*[= { *dot1p-value* \| *dot1p-value1* **to** *dot1p-value2* }&\<1-8\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[dot1p-value]{lang="EN-US"}*[、]{style="font-family:宋体"}*[dot1p-value1]{lang="EN-US"}*[ ]{lang="EN-US"}[、]{style="font-family:宋体"}*[dot1p-value2]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，且]{style="font-family:宋体"}*[dot1p-value1]{lang="EN-US"}*[必须小于或等于]{style="font-family:宋体"}*[dot1p-value2]{lang="EN-US"}*[；]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[[qos-local-id *local-id-list*]{lang="EN-US"}]{#struct_0_x2723_x1019_1557779460}

[[定义匹配]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_x2723_x1019_437295484}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值的规则]{style="font-family:宋体"}

[*[local-id-list]{lang="EN-US"}*]{#struct_0_x2723_x1019_626389283}[：]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值]{style="font-family:宋体"}[列表，表示方式为]{style="font-family:宋体"}*[local-id-list ]{lang="EN-US"}*[= { *local-id* \| *local-id1* **to** *local-id2* }&\<1-8\>]{lang="EN-US"}[，]{style="font-family:
  宋体"}*[local-id]{lang="EN-US"}*[、]{style="font-family:
  宋体"}*[local-id1]{lang="EN-US"}*[ ]{lang="EN-US"}[、]{style="font-family:宋体"}*[local-id2]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，且]{style="font-family:宋体"}*[local-id1]{lang="EN-US"}*[必须小于或等于]{style="font-family:宋体"}*[local-id2]{lang="EN-US"}*[；]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x868212600}

[[配置匹配规则只是进入视图，并不实际生成配置，仅当在匹配规则下进一步配置嵌套的子转发组后，匹配规则配置才真正生效。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_526584280}

[[删除匹配规则会同时删除匹配规则下嵌套的子转发组及其关联的转发策略。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x593941866}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x380194324}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_1621366481}[指定转发组按匹配规则进入配置视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_1908427460}

[\[Sysname\] qos forwarding-group testfg]{lang="EN-US"}

[\[Sysname-hqos-fg-testfg\] match service-vlan-id 2]{lang="EN-US"}

[\[Sysname-hqos-fg-testfg-match\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x21987019}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol;border:none"}]{.TerminalDisplayshading}**[forwarding-group profile]{lang="EN-US"}**[ (scheduler-policy match view)]{lang="EN-US"}]{#struct_0_x2723_x1019_457233192}

::: {#-1891245521 .myid}
[]{#_Toc404792090}[]{#struct_0_x2723_x1019_2058464071}[]{#_Toc358383004}[]{#_Toc357857448}[]{#_Toc345167691}

**HQoS \-- 转发组配置命令 \-- qos forwarding-group**

------------------------------------------------------------------------

[**[qos forwarding-group]{lang="EN-US"}**]{#struct_0_x2723_x1019_x743356761}[命令用来创建用户自定义的转发组，并进入该转发组视图。]{style="font-family:宋体"}

[**[undo qos forwarding-group]{lang="EN-US"}**]{#struct_0_x2723_x1019_437361020}[命令用来删除用户自定义的转发组。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_223158474}

[**[qos]{lang="EN-US"}**[ **forwarding-group** *fg-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_345388629}

[**[undo qos]{lang="EN-US"}**[ **forwarding-group** *fg-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_1363959676}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_2064261739}

[[不存在自定义转发组。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_285522851}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_789953831}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x612918867}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x577407017}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_1762806150}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x230551958}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1596297762}

[*[fg-name]{lang="EN-US"}*]{#struct_0_x2723_x1019_x643335856}[：自定义转发组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。自定义的转发组名称不能使用系统预定义的转发组的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1609911498}

[[系统有一个预定义的转发组，名称为]{style="font-family:宋体"}[default]{lang="EN-US"}]{#struct_0_x2723_x1019_x365996807}[，]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，不允许修改和删除。]{style="font-family:
宋体"}

[[系统最多支持创建的转发组个数为]{style="font-family:宋体"}[8191]{lang="EN-US"}]{#struct_0_x2723_x1019_1511644491}[。]{style="font-family:宋体"}

[[如果转发组已经被其他转发组或调度策略嵌套，需要先取消嵌套关系才能删除。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1678059689}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1580913834}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1619282721}[创建自定义转发组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_437164412}

[\[Sysname\] qos forwarding-group testfg]{lang="EN-US"}

[\[Sysname-fg-testfg\]]{lang="EN-US"}
:::

::::: {#584085261 .myid}
[]{#_Toc404792092}[]{#struct_0_x2723_x1019_1959384489}[]{#_Toc358383006}[]{#_Toc357857450}[]{#_Toc345167693}

**HQoS \-- 丢弃策略配置命令 \-- display qos drop-profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_x408464704}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_x202652722}
:::

[ ]{lang="EN-US"}

[**[display qos drop-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_362285164}[命令用来显示丢弃策略的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1366007436}

[**[display qos drop-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_1745781770}[ \[ **name** *dp-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1126021128}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_542156925}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1155580743}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x2011234892}

[[network-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_186623491}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1252710791}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_x2108236965}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x849996711}

[*[dp-name]{lang="EN-US"}*]{#struct_0_x2723_x1019_x319924718}[：丢弃策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有丢弃策略的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x2102745745}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_437229948}[显示指定丢弃策略]{style="font-family:宋体"}[testdp]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos drop-profile name testdp]{lang="EN-US"}]{#struct_0_x2723_x1019_249366219}

[Drop profile: testdp, ID: 10]{lang="EN-US"}

[ Green thresholds: 50/60/30(min/max/prob)]{lang="EN-US"}

[ Yellow thresholds: 50/60/30(min/max/prob)]{lang="EN-US"}

[ Red thresholds: 50/60/30(min/max/prob)]{lang="EN-US"}

[ Weighting constant: 2]{lang="EN-US"}

[]{#struct_0_x2723_x1019_578773809}[[表1-4 ]{lang="EN-US"}[display qos drop-profile]{lang="EN-US"}]{#_Toc148586891}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x990140794}[[字段]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1702706637}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x121741811}

[[Drop profile]{lang="EN-US"}]{#struct_0_x2723_x1019_937391639}

[[丢弃策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1372917651}

[[ID]{lang="EN-US"}]{#struct_0_x2723_x1019_197556972}

[[丢弃策略]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2723_x1019_1533811439}

[[Green thresholds]{lang="EN-US"}]{#struct_0_x2723_x1019_x937386118}

[[绿色报文的丢弃参数]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1135478531}

[[Yellow thresholds]{lang="EN-US"}]{#struct_0_x2723_x1019_1091526964}

[[黄色报文的丢弃参数]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1387479354}

[[Red thresholds]{lang="EN-US"}]{#struct_0_x2723_x1019_x1401469268}

[[红色报文的丢弃参数]{style="font-family:宋体"}]{#struct_0_x2723_x1019_296824944}

[[min/max/prob]{lang="EN-US"}]{#struct_0_x2723_x1019_437557628}

[[开始丢弃的队列门限]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_453368769}[完全丢弃的队列门限]{style="font-family:宋体"}[/]{lang="EN-US"}[丢弃斜率]{style="font-family:宋体"}

[[Weighting constant]{lang="EN-US"}]{#struct_0_x2723_x1019_1797890819}

[[计算平均队列长度的指数]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1506826149}

[ ]{lang="EN-US"}

::::: {#-742491806 .myid}
[]{#_Toc404792093}[]{#struct_0_x2723_x1019_x1027011557}

**HQoS \-- 丢弃策略配置命令 \-- green**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_1681426023}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_x763469787}
:::

[ ]{lang="EN-US"}

[**[green]{lang="EN-US"}**]{#struct_0_x2723_x1019_x581897970}[命令用来配置绿色报文的丢弃参数。]{style="font-family:宋体"}

[**[undo green]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1995332803}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x823359171}

[**[green]{lang="EN-US"}**[ **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]{lang="EN-US"}]{#struct_0_x2723_x1019_1463687793}

[**[undo green]{lang="EN-US"}**]{#struct_0_x2723_x1019_x683899954}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1119491373}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1974628349}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_2058580233}

[[丢弃策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_437623164}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1229149265}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_231664529}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_1193891504}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x171515126}

[**[low-limit]{lang="EN-US"}***[ low-limit]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_2032820271}[：]{style="font-family:宋体"}[开始丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[high-limit]{lang="EN-US"}***[ high-limit]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_1121912729}[：]{style="font-family:宋体"}[完全丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。完全丢弃的队列门限值要大于开始丢弃的队列门限值。]{style="font-family:宋体"}

[**[discard-probability]{lang="EN-US"}***[ discard-prob]{lang="EN-US"}*]{#struct_0_x2723_x1019_x1818682387}[：丢弃斜率]{style="font-family:宋体"}[。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x648839145}

[[当配置]{style="font-family:宋体"}*[discard-prob]{lang="EN-US"}*]{#struct_0_x2723_x1019_994519872}[等于]{style="font-family:宋体"}[100]{lang="EN-US"}[时，则成为尾丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x321976683}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1943398257}[指定绿色报文的丢弃参数，开始丢弃的队列门限为]{style="font-family:宋体"}[500]{lang="EN-US"}[，完全丢弃的队列门限为]{style="font-family:宋体"}[700]{lang="EN-US"}[，丢弃斜率为]{style="font-family:宋体"}[40]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x1543349997}

[\[Sysname\] qos drop-profile testdp]{lang="EN-US"}

[\[Sysname-hqos-dp-testdp\] green low-limit 500 high-limit 700 discard-probability 40]{lang="EN-US"}
:::::

::::: {#1776294077 .myid}
[]{#_Toc404792094}[]{#struct_0_x2723_x1019_x520135345}[]{#_Toc358383008}[]{#_Toc357857452}[]{#_Toc345167695}

**HQoS \-- 丢弃策略配置命令 \-- qos drop-profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_1034199807}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_1385317689}
:::

[ ]{lang="EN-US"}

[**[qos drop-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_x581315234}[命令用来创建用户自定义的丢弃策略，并进入该丢弃策略视图。]{style="font-family:宋体"}

[**[undo qos drop-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_437426556}[命令用来删除用户自定义的丢弃策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1499169251}

[**[qos drop-profile]{lang="EN-US"}**[ *dp-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1260185627}

[**[undo qos drop-profile]{lang="EN-US"}**[ *dp-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1836299469}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_770627671}

[[不存在自定义丢弃策略。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x44895400}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1982873415}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x931855922}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1208917010}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_307921045}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_1331309630}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1847310978}

[*[dp-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_x571844150}[：自定义]{style="font-family:
宋体"}[丢弃策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。自定义的丢弃策略名称不能使用系统预定义的丢弃策略名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_195876203}

[[系统有一个预定义的丢弃策略，名称为]{style="font-family:宋体"}[default]{lang="EN-US"}]{#struct_0_x2723_x1019_716979069}[，]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，不允许修改和删除。]{style="font-family:
宋体"}

[[如果丢弃策略已经被转发策略引用，需要先取消引用才能删除。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_178272634}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1219911746}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_1644400487}[创建自定义丢弃策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_437492092}

[\[Sysname\] qos drop-profile testdp]{lang="EN-US"}

[\[Sysname-dp-testdp\]]{lang="EN-US"}
:::::

::::: {#-1029288764 .myid}
[]{#_Toc404792095}[]{#struct_0_x2723_x1019_896409277}

**HQoS \-- 丢弃策略配置命令 \-- red**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_x964077938}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_x2135273314}
:::

[ ]{lang="EN-US"}

[**[red]{lang="EN-US"}**]{#struct_0_x2723_x1019_905380701}[命令用来配置红色报文的丢弃参数。]{style="font-family:宋体"}

[**[undo red]{lang="EN-US"}**]{#struct_0_x2723_x1019_x679799965}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_2051860784}

[**[red]{lang="EN-US"}**[ **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1756358768}

[**[undo red]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1023436713}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1582228785}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1518271234}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1439657782}

[[丢弃策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_486466040}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_393428879}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_100118838}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1381971813}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x474793789}

[**[low-limit]{lang="EN-US"}***[ low-limit]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_1297774405}[：]{style="font-family:宋体"}[开始丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[high-limit]{lang="EN-US"}***[ high-limit]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_2017274552}[：]{style="font-family:宋体"}[完全丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。完全丢弃的队列门限值要大于开始丢弃的队列门限值。]{style="font-family:宋体"}

[**[discard-probability]{lang="EN-US"}***[ discard-prob]{lang="EN-US"}*]{#struct_0_x2723_x1019_437819772}[：丢弃斜率]{style="font-family:宋体"}[。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1405983060}

[[当配置]{style="font-family:宋体"}*[discard-prob]{lang="EN-US"}*]{#struct_0_x2723_x1019_1421522392}[等于]{style="font-family:宋体"}[100]{lang="EN-US"}[时，则成为尾丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1126949764}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1673160247}[指定红色报文的丢弃参数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x266172732}

[\[Sysname\] qos drop-profile testdp]{lang="EN-US"}

[\[Sysname-hqos-dp-testdp\] red low-limit 500 high-limit 700 discard-probability 40]{lang="EN-US"}
:::::

::::: {#-230027400 .myid}
[]{#_Toc404792096}[]{#struct_0_x2723_x1019_x384562698}[]{#_Toc358383010}[]{#_Toc357857454}[]{#_Toc345167697}

**HQoS \-- 丢弃策略配置命令 \-- weighting-constant**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_1415142302}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_x1317987376}
:::

[ ]{lang="EN-US"}

[**[weighting-constant]{lang="EN-US"}**]{#struct_0_x2723_x1019_1792961444}[命令用来配置计算平均队列长度的指数。]{style="font-family:宋体"}

[**[undo weighting-constant]{lang="EN-US"}**]{#struct_0_x2723_x1019_x570563858}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_628258557}

[**[weighting-constant ]{lang="EN-US"}***[exponent]{lang="EN-US"}*]{#struct_0_x2723_x1019_151887912}

[**[undo weighting-constant]{lang="EN-US"}**]{#struct_0_x2723_x1019_1638347867}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x903956626}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1962484997}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_202516913}

[[丢弃策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_437885308}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x602303697}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_477658236}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x320140958}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x362872622}

[*[exponent]{lang="EN-US"}*]{#struct_0_x2723_x1019_x698610944}[：]{style="font-family:宋体"}[表示计算平均队列长度的指数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x438294934}

[[平均队列长度的指数越大，计算平均队列长度时对队列的实时变化越不敏感。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1179512958}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1718427692}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_865598098}[指定丢弃策略的计算平均队列长度的指数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_1491746744}

[\[Sysname\] qos drop-profile testdp]{lang="EN-US"}

[\[Sysname-hqos-dp-testdp\] weighting-constant 2]{lang="EN-US"}
:::::

::::: {#4875282 .myid}
[]{#_Toc404792097}[]{#struct_0_x2723_x1019_x2032975482}[]{#_Toc358383011}[]{#_Toc357857455}[]{#_Toc345167698}

**HQoS \-- 丢弃策略配置命令 \-- yellow**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_x1090992684}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_1981561300}
:::

**[ ]{lang="EN-US"}**

[**[yellow]{lang="EN-US"}**]{#struct_0_x2723_x1019_x448271510}[命令用来配置黄色报文的丢弃参数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **yellow**]{lang="EN-US"}]{#struct_0_x2723_x1019_16024902}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x311225303}

[**[yellow]{lang="EN-US"}**[ **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1173999668}

[**[undo yellow]{lang="EN-US"}**]{#struct_0_x2723_x1019_437295485}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_626389282}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x868212601}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_526649816}

[[丢弃策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1232313978}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x158103080}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_1788777517}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x369503008}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_36667126}

[**[low-limit]{lang="EN-US"}***[ low-limit]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_1305357574}[：]{style="font-family:宋体"}[开始丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[high-limit]{lang="EN-US"}***[ high-limit]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_x1553104419}[：]{style="font-family:宋体"}[完全丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。完全丢弃的队列门限值要大于开始丢弃的队列门限值。]{style="font-family:宋体"}

[**[discard-probability]{lang="EN-US"}***[ discard-prob]{lang="EN-US"}*]{#struct_0_x2723_x1019_x2055659675}[：丢弃斜率]{style="font-family:宋体"}[。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1656995721}

[[当配置]{style="font-family:宋体"}*[discard-prob]{lang="EN-US"}*]{#struct_0_x2723_x1019_x1016996636}[等于]{style="font-family:宋体"}[100]{lang="EN-US"}[时，则成为尾丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1943383608}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_180849275}[指定黄色报文的丢弃参数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_1402878507}

[\[Sysname\] qos drop-profile testdp]{lang="EN-US"}

[\[Sysname-hqos-dp-testdp\] yellow low-limit 500 high-limit 700 discard-probability 40]{lang="EN-US"}
:::::

::::: {#1742433432 .myid}
[]{#_Toc358383013}[]{#_Toc357857457}[]{#_Toc345167700}[]{#_Toc339901024}[]{#_Toc151609160}[]{#_Toc151608673}[]{#_Toc404792099}[]{#struct_0_x2723_x1019_437361021}

**HQoS \-- 转发策略配置命令 \-- bandwidth**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_223158475}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_345388628}
:::

**[ ]{lang="EN-US" style="color:black"}**

[**[bandwidth]{lang="EN-US" style="color:black"}**]{#struct_0_x2723_x1019_1363959677}[命令用来配置转发策略的最小带宽保证。]{style="font-family:
宋体;color:black"}

[**[undo bandwidth]{lang="EN-US" style="color:black"}**]{#struct_0_x2723_x1019_2064196203}[命令用来取消配置转发策略的最小带宽保证。]{style="font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x2064907636}

[**[bandwidth ]{lang="EN-US" style="color:black"}***[bandwidth-value]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_x1289660526}

[**[undo bandwidth]{lang="EN-US" style="color:black"}**]{#struct_0_x2723_x1019_1304802431}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x760464979}

[[自定义转发策略不存在最小带宽保证配置。]{style="font-family:宋体;color:black"}]{#struct_0_x2723_x1019_1084748726}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_605082171}

[[转发策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1350855686}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x22331588}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1045781714}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_808061923}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x296853377}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x2723_x1019_x1503344427}[：最小保证带宽，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1414963894}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_1283350161}[配置转发策略]{style="font-family:宋体"}[testfp]{lang="EN-US"}[的最小带宽保证为]{style="font-family:宋体"}[2000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_437164413}

[\[Sysname\] qos forwarding-profile testfp]{lang="EN-US"}

[\[Sysname-hqos-fp-testfp\] bandwidth 2000]{lang="EN-US"}
:::::

::: {#1072173232 .myid}
[]{#_Toc404792100}[]{#struct_0_x2723_x1019_335475513}

**HQoS \-- 转发策略配置命令 \-- display qos forwarding-profile**

------------------------------------------------------------------------

[**[display qos forwarding-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_1959384490}[命令用来显示转发策略的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x408005951}

[**[display qos forwarding-profile]{lang="EN-US"}**[ \[ **name** *fp-name* \]]{lang="EN-US"}]{#struct_0_x2723_x1019_902969216}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_163527286}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1012989588}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_210842691}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_1383203108}

[[network-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_1934951193}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_902733666}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_x1555535661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1433092990}

[*[fp-name]{lang="EN-US"}*]{#struct_0_x2723_x1019_x1063545126}[：转发策略的名称，]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有转发策略的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1292821520}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_2126036120}[显示指定转发策略]{style="font-family:宋体"}[testfp]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos forwarding-profile name testfp]{lang="EN-US"}]{#struct_0_x2723_x1019_437229949}

[Forwarding profile: testfp, ID: 10]{lang="EN-US"}

[ GTS: CIR 100(kbps), CBS 50(Bytes), EBS 100(Bytes), PIR 150(kbps)]{lang="EN-US"}

[ WRR: priority 2, weight 1]{lang="EN-US"}

[ Bandwidth: 1000(kbps)]{lang="EN-US"}

[ Drop profile: default]{lang="EN-US"}

[]{#struct_0_x2723_x1019_249366220}[[表1-5 ]{lang="EN-US"}[display qos forwarding-profile]{lang="EN-US"}]{#_Toc148586893}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x998126301}[[字段]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1759878344}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_648467970}

[[Forwarding profile]{lang="EN-US"}]{#struct_0_x2723_x1019_x1234098038}

[[转发策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_823209300}

[[ID]{lang="EN-US"}]{#struct_0_x2723_x1019_x983129281}

[[转发策略的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2723_x1019_1045959714}

[[CIR]{lang="EN-US"}]{#struct_0_x2723_x1019_2092522531}

[[承诺信息速率]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x307666154}

[[CBS]{lang="EN-US"}]{#struct_0_x2723_x1019_x481895715}

[[承诺突发尺寸]{style="font-family:宋体"}]{#struct_0_x2723_x1019_526814324}

[[EBS]{lang="EN-US"}]{#struct_0_x2723_x1019_x931159946}

[[超额突发尺寸]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x404483511}

[[PIR]{lang="EN-US"}]{#struct_0_x2723_x1019_55409862}

[[峰值信息速率]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1103857684}

[[WRR]{lang="EN-US"}]{#struct_0_x2723_x1019_437557629}

[[加权轮循队列调度]{style="font-family:宋体"}]{#struct_0_x2723_x1019_453368768}

[[priority]{lang="EN-US"}]{#struct_0_x2723_x1019_1797890820}

[[调度优先级]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1507415974}

[[weight]{lang="EN-US"}]{#struct_0_x2723_x1019_490236523}

[[调度权重]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1148671436}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x2723_x1019_2034677804}

[[最小保证带宽]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x129586421}

[[Drop profile]{lang="EN-US"}]{#struct_0_x2723_x1019_x796846079}

[[丢弃策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_337842141}

[]{#_Toc358383014}[]{#_Toc357857458}[]{#_Toc345167701}[[ ]{lang="EN-US"}]{#_Toc339901025}

::::: {#-841546766 .myid}
[]{#_Toc404792101}[]{#struct_0_x2723_x1019_1754380397}

**HQoS \-- 转发策略配置命令 \-- drop-profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 14 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_2064983338}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_679388112}
:::

**[ ]{lang="EN-US"}**

[**[drop-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1326856302}[命令用来将丢弃策略绑定到转发策略。]{style="font-family:宋体"}

[**[undo drop-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_437623165}[命令用来将丢弃策略从转发策略中删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1229149264}

[**[drop-profile]{lang="EN-US"}**[ *dp-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1334419412}

[**[undo drop-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1947800713}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_112308573}

[[自定义转发策略中不引用丢弃策略，对所有报文进行尾丢弃。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1559243248}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1932476796}

[[转发策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_253774534}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1906720393}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x2061339664}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_465198846}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_120763290}

[*[dp-name]{lang="EN-US"}*]{#struct_0_x2723_x1019_x1069598094}[：丢弃策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x896290886}

[[在转发策略下绑定丢弃策略时对应的丢弃策略必须存在。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1189272197}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x239622638}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x991835128}[将丢弃策略]{style="font-family:宋体"}[testdp]{lang="EN-US"}[绑定到转发策略]{style="font-family:宋体"}[testfp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_437426557}

[\[Sysname\] qos forwarding-profile testfp]{lang="EN-US"}

[\[Sysname-hqos-fp-testfp\] drop-profile tetsdp]{lang="EN-US"}
:::::

::: {#1916017645 .myid}
[]{#_Toc404792102}[]{#struct_0_x2723_x1019_x1499169250}[]{#_Toc358383015}[]{#_Toc357857459}[]{#_Toc345167702}

**HQoS \-- 转发策略配置命令 \-- gts cir**

------------------------------------------------------------------------

[**[gts]{lang="EN-US"}**]{#struct_0_x2723_x1019_1468697728}[命令用来配置转发策略的流量整形参数。]{style="font-family:宋体"}

[**[undo gts]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1476295739}[命令用来取消配置转发策略的整形参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_192953421}

[**[gts cir]{lang="EN-US"}**[ *cir-value* \[ **cbs** *cbs-value* \[ **ebs** *ebs-value* \] \] \[ **pir** *pir-value* \]]{lang="EN-US"}]{#struct_0_x2723_x1019_x294625070}

[**[undo gts]{lang="EN-US"}**]{#struct_0_x2723_x1019_x988380103}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1756775561}

[[转发策略中不存在流量整形配置，不对速率进行限制。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1609245278}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1218659884}

[[转发策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1162949928}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1839407718}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_839890629}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_843996298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1564141319}

[*[cir-value]{lang="EN-US"}*]{#struct_0_x2723_x1019_x232502905}[：承诺带宽值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *cbs-value*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1721447510}[：承诺突发尺寸。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。如果设备未指定缺省值，该缺省值为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒内以]{style="font-family:宋体"}[CIR]{lang="EN-US"}[速率通过的流量，单位为]{style="font-family:宋体"}[bytes]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *ebs-value*]{lang="EN-US"}]{#struct_0_x2723_x1019_1601940694}[：超额突发尺寸，在双令牌桶算法中超出承诺突发流量的部分，单位为]{style="font-family:宋体"}[bytes]{lang="EN-US"}[。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。如果设备未指定缺省值，该缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pir]{lang="EN-US"}**[ *pir-value*]{lang="EN-US"}]{#struct_0_x2723_x1019_x563076407}[：峰值带宽值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。不配置峰值带宽值表示是单令牌桶流量监管。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x871113727}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_437492093}[配置转发策略]{style="font-family:宋体"}[testfp]{lang="EN-US"}[的流量整形参数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_896409276}

[\[Sysname\] qos forwarding-profile testfp]{lang="EN-US"}

[[\[Sysname-hqos-fp-testfp\] gts cir 1000 cbs 1000 pir 2000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2723_x1019_x964077939}
:::

::: {#1281262498 .myid}
[]{#_Toc404792103}[]{#struct_0_x2723_x1019_x2135338850}[]{#_Toc358383016}[]{#_Toc357857460}[]{#_Toc345167703}[]{#_Toc339901027}[]{#_Toc151609163}[]{#_Toc151608676}

**HQoS \-- 转发策略配置命令 \-- qos forwarding-profile**

------------------------------------------------------------------------

[**[qos forwarding-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_167949798}[命令用来创建用户自定义的转发策略，并进入该转发策略视图。]{style="font-family:宋体"}

[**[undo qos forwarding-profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_1600682897}[命令用来删除用户自定义的转发策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_605371002}

[**[qos forwarding-profile]{lang="EN-US"}**[ *fp-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_1244661383}

[**[undo qos forwarding-profile]{lang="EN-US"}**[ *fp-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_x331565001}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_152542061}

[[系统中不存在自定义转发策略。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1144730460}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x21675141}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x554738138}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1367435392}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x983994326}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1324410951}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x526622699}

[*[fp-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_1793977048}[：自定义]{style="font-family:宋体"}[转发策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。自定义的转发策略名称不能使用系统预定义的转发策略名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_437819773}

[[系统预定义的转发策略不允许修改和删除。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1405983061}

[[如果转发策略已经被转发组或调度策略嵌套，需要先取消嵌套关系才能删除。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1307360963}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_819802495}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_2109228199}[创建自定义转发策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x548357112}

[\[Sysname\] qos forwarding-profile testfp]{lang="EN-US"}
:::

::::: {#-839206963 .myid}
[]{#_Toc404792104}[]{#struct_0_x2723_x1019_1377618436}

**HQoS \-- 转发策略配置命令 \-- sp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_18714602}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_690234694}
:::

**[ ]{lang="EN-US"}**

[**[sp]{lang="EN-US"}**]{#struct_0_x2723_x1019_1974595324}[命令用来配置转发策略的队列调度方式为严格优先级调度。]{style="font-family:宋体"}

[**[undo sp]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1989569997}[命令用来取消配置转发策略的严格优先级队列调度方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_362599191}

[**[sp]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1093820688}

[**[undo sp]{lang="EN-US"}**]{#struct_0_x2723_x1019_x654494950}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1232330719}

[[自定义转发策略不存在]{style="font-family:宋体"}[sp]{lang="EN-US"}]{#struct_0_x2723_x1019_x256591084}[配置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1893499433}

[[转发策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_146885030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1687507652}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_437885309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x602303696}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_477723772}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1874892982}[配置转发策略]{style="font-family:宋体"}[testfp]{lang="EN-US"}[的队列调度方式为严格优先级调度。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x1212986870}

[\[Sysname\] qos forwarding-profile testfp]{lang="EN-US"}

[\[Sysname-hqos-fp-testfp\] sp]{lang="EN-US"}
:::::

::::: {#-1338530498 .myid}
[]{#_Toc404792105}[]{#struct_0_x2723_x1019_x1890194313}

**HQoS \-- 转发策略配置命令 \-- wfq**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 3 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_1621969184}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_287722547}
:::

**[ ]{lang="EN-US"}**

[**[wfq]{lang="EN-US"}**]{#struct_0_x2723_x1019_825198096}[命令用来配置转发策略队列调度方式是加权公平队列调度。同一优先级的队列按照权重调度，权重决定调度该队列时应该占用的带宽比例。]{style="font-family:宋体"}

[**[undo wfq]{lang="EN-US"}**]{#struct_0_x2723_x1019_1241661383}[命令用来取消配置转发策略的加权公平队列调度方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_299218999}

[**[wfq ]{lang="EN-US"}**[\[ **priority** *priority-value* \] \[ **weight** *weight-value* \]]{lang="EN-US"}]{#struct_0_x2723_x1019_1610822239}

[**[undo wfq]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1210049815}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_361097794}

[[自定义转发策略不存在]{style="font-family:宋体"}[wfq]{lang="EN-US"}]{#struct_0_x2723_x1019_x414486478}[配置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1383023656}

[[转发策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1009733963}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_437295482}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_626389289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x868212610}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_526584279}

[**[priority]{lang="EN-US"}***[ priority-value]{lang="EN-US"}*]{#struct_0_x2723_x1019_x256234867}[：调度优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～设备支持的最大值，不同型号的设备支持的最大值不同，请以设备的实际情况为准。缺省值为最低优先级]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}***[ weight-value]{lang="EN-US"}*]{#struct_0_x2723_x1019_1296703349}[：调度权重，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～设备支持的最大值，不同型号的设备支持的最大值不同，请以设备的实际情况为准。缺省值为最小权重]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1492911489}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1832732201}[配置转发策略]{style="font-family:宋体"}[testfp]{lang="EN-US"}[的队列调度方式为加权公平调度，调度优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[，调度权重为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x1384684937}

[\[Sysname\] qos forwarding-profile testfp]{lang="EN-US"}

[\[Sysname-hqos-fp-testfp\] wfq priority 3 weight 2]{lang="EN-US"}
:::::

::::: {#1391663577 .myid}
[]{#_Toc404792106}[]{#struct_0_x2723_x1019_x720183264}

**HQoS \-- 转发策略配置命令 \-- wrr**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 5 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_2060607139}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_x1427015735}
:::

**[ ]{lang="EN-US"}**

[**[wrr]{lang="EN-US"}**]{#struct_0_x2723_x1019_x2012925469}[命令用来配置转发策略的队列调度方式是加权轮循调度。同一优先级的队列按照权重调度，权重决定调度该队列时应该占用的带宽比例。]{style="font-family:宋体"}

[**[undo wrr]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1651589580}[命令用来取消配置转发策略的加权轮询队列调度方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1211564302}

[**[wrr ]{lang="EN-US"}**[\[ **priority** *priority-value* \] \[ **weight** *weight-value* \]]{lang="EN-US"}]{#struct_0_x2723_x1019_960333317}

[**[undo wrr]{lang="EN-US"}**]{#struct_0_x2723_x1019_x691090054}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x643947203}

[[自定义转发策略不存在]{style="font-family:宋体"}[WRR]{lang="EN-US"}]{#struct_0_x2723_x1019_437361018}[配置。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1733156670}

[[转发策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_21500326}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1770269629}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x683336749}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_1840655834}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1742740032}

[**[priority]{lang="EN-US"}***[ priority-value]{lang="EN-US"}*]{#struct_0_x2723_x1019_x1419602448}[：调度优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～设备支持的最大值，不同型号的设备支持的最大值不同，请以设备的实际情况为准。缺省值为最低优先级]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}***[ weight-value]{lang="EN-US"}*]{#struct_0_x2723_x1019_1934759816}[：调度权重，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～设备支持的最大值，不同型号的设备支持的最大值不同，请以设备的实际情况为准。缺省值为最小权重]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1685734648}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_2079541624}[配置转发策略]{style="font-family:宋体"}[testfp]{lang="EN-US"}[的队列调度方式为加权轮循调度。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x1023167476}

[\[Sysname\] qos forwarding-profile testfp]{lang="EN-US"}

[\[Sysname-hqos-fp-testfp\] wrr priority 3 weight 2]{lang="EN-US"}
:::::

::: {#-945417679 .myid}
[]{#_Toc404792108}[]{#struct_0_x2723_x1019_1091928596}[]{#_Toc358032671}[]{#_Toc357857466}[]{#_Toc345167709}[]{#_Toc339901032}[]{#_Toc151609167}[]{#_Toc151608680}

**HQoS \-- 调度策略配置命令 \-- display qos scheduler-policy**

------------------------------------------------------------------------

[**[display qos scheduler-policy]{lang="EN-US"}**]{#struct_0_x2723_x1019_633254583}[命令用来显示调度策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1891913785}

[**[display qos scheduler-policy ]{lang="EN-US"}**[\[ **name** *sp-name* \]]{lang="EN-US"}]{#struct_0_x2723_x1019_x1356292067}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_437164410}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_335475510}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1959384491}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x407940415}

[[network-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_586184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x108673755}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_x902071028}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1558813413}

[*[sp-name]{lang="EN-US"}*]{#struct_0_x2723_x1019_1682432991}[：]{style="font-family:宋体"}[调度策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有调度策略的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1497206208}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_1100628517}[显示指定调度策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos scheduler-policy name test_sp]{lang="EN-US"}]{#struct_0_x2723_x1019_437557626}

[SP \-- Scheduler policy      FG \-- Forwarding group     FC \-- Forwarding class]{lang="EN-US"}

[FP \-- Forwarding profile    L  \-- Layer]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[SP: test_sp(1)]{lang="EN-US"}

[ \|  Scheduler unit: weight]{lang="EN-US"}

[ \|]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): default(0)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \| ]{lang="EN-US"}

[ \|   +\--FC: BE(0)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|]{lang="EN-US"}

[ \|   +\--FC: AF(1)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|]{lang="EN-US"}

[ \|   +\--FC: EF(2)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|]{lang="EN-US"}

[ \|   +\--FC: NC(3)]{lang="EN-US"}

[ \|          FP: default(0)]{lang="EN-US"}

[ \|  ]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): VOIP(1)]{lang="EN-US"}

[ \|   \|      FP: VOIP(2)]{lang="EN-US"}

[ \|   \| ]{lang="EN-US"}

[ \|   \|  Match: service-vlan-id 2 to 10]{lang="EN-US"}

[ \|   +\--FG(L2): Customer1(2)]{lang="EN-US"}

[ \|   \|   \|      FP: Customer1(1)]{lang="EN-US"}

[ \|   \|   \| ]{lang="EN-US"}

[ \|   \|   +\--FC: BE(0)]{lang="EN-US"}

[ \|   \|   \|      FP: BE(3)]{lang="EN-US"}

[ \|   \|   \|]{lang="EN-US"}

[ \|   \|   +\--FC: AF(1)]{lang="EN-US"}

[ \|   \|   \|      FP: default(0)]{lang="EN-US"}

[\|   \|   \|]{lang="EN-US"}

[ \|   \|   +\--FC: EF(2)]{lang="EN-US"}

[ \|   \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|   \|]{lang="EN-US"}

[ \|   \|   +\--FC: NC(3)]{lang="EN-US"}

[ \|   \|          FP: default(0)]{lang="EN-US"}

[ \|   \|  ]{lang="EN-US"}

[ \|   \|  Match: service-vlan-id 11 to 20]{lang="EN-US"}

[ \|   +\--FG(L2): Customer2(5)]{lang="EN-US"}

[ \|       \|      FP: Customer2(2)]{lang="EN-US"}

[ \|       \|]{lang="EN-US"}

[ \|       +\--FC: BE(0)]{lang="EN-US"}

[ \|       \|      FP: BE(3)]{lang="EN-US"}

[ \|       \|]{lang="EN-US"}

[ \|       +\--FC: AF(1)]{lang="EN-US"}

[ \|       \|      FP: default(0)]{lang="EN-US"}

[ \|       \|]{lang="EN-US"}

[ \|       +\--FC: EF(2)]{lang="EN-US"}

[ \|       \|      FP: default(0)]{lang="EN-US"}

[ \|       \|]{lang="EN-US"}

[ \|       +\--FC: NC(3)]{lang="EN-US"}

[ \|              FP: default(0)]{lang="EN-US"}

[ \|   ]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): INTERNET(4)]{lang="EN-US"}

[     \|      FP: INTERNET(4)]{lang="EN-US"}

[     \|]{lang="EN-US"}

[     \|  Match: service-vlan-id 21 to 30]{lang="EN-US"}

[     +\--FG(L2): Customer3(6)]{lang="EN-US"}

[         \|      FP: Customer3(6)]{lang="EN-US"}

[         \| ]{lang="EN-US"}

[         +\--FC: BE(0)]{lang="EN-US"}

[         \|      FP: BE(3)]{lang="EN-US"}

[         \|]{lang="EN-US"}

[         +\--FC: AF(1)]{lang="EN-US"}

[         \|      FP: default(0)]{lang="EN-US"}

[         \|]{lang="EN-US"}

[         +\--FC: EF(2)]{lang="EN-US"}

[         \|      FP: default(0)]{lang="EN-US"}

[         \|]{lang="EN-US"}

[         +\--FC: NC(3)]{lang="EN-US"}

[                FP: default(0)]{lang="EN-US"}

[]{#struct_0_x2723_x1019_453368783}[[表1-6 ]{lang="EN-US"}[display qos scheduler-policy]{lang="EN-US"}]{#_Toc148586895}[命令显示描述信息表]{style="font-family:黑体"}

[]{#table_struct_0_x1002316951}[[字段]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x113794295}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x774658763}

[[Scheduler policy]{lang="EN-US"}]{#struct_0_x2723_x1019_x2134221334}

[[调度策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1788885811}

[[Forwarding group]{lang="EN-US"}]{#struct_0_x2723_x1019_764610719}

[[转发组的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_841016112}

[[Forwarding class]{lang="EN-US"}]{#struct_0_x2723_x1019_83995188}

[[转发类的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1963107548}

[[Forwarding profile]{lang="EN-US"}]{#struct_0_x2723_x1019_293897198}

[[转发策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x995913042}

[[Layer]{lang="EN-US"}]{#struct_0_x2723_x1019_1028442293}

[[层次的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1345264793}

[[Scheduler unit]{lang="EN-US"}]{#struct_0_x2723_x1019_638939555}

[[调度策略的调度单位]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1475256404}

[[match]{lang="EN-US"}]{#struct_0_x2723_x1019_437623162}

[[match]{lang="EN-US"}]{#struct_0_x2723_x1019_x1229149267}[方式实例化]{style="font-family:宋体"}

[[group]{lang="EN-US"}]{#struct_0_x2723_x1019_x931134885}

[[group]{lang="EN-US"}]{#struct_0_x2723_x1019_1992429468}[方式实例化]{style="font-family:宋体"}

[[service-vlan-id]{lang="EN-US"}]{#struct_0_x2723_x1019_21249716}

[[实例化匹配规则]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1884972972}

[[括号内的数字]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x2004982711}

[[前方对应字段（转发类]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_371354069}[转发组]{style="font-family:宋体"}[/]{lang="EN-US"}[转发策略]{style="font-family:宋体"}[/]{lang="EN-US"}[调度策略）名称的索引]{style="font-family:宋体"}

[]{#_Toc358032672}[]{#_Toc357857467}[]{#_Toc345167710}[[ ]{lang="EN-US"}]{#_Toc339901033}

::: {#-1056954474 .myid}
[]{#_Toc404792109}[]{#struct_0_x2723_x1019_1542847742}

**HQoS \-- 调度策略配置命令 \-- display qos scheduler-policy diagnosis interface**

------------------------------------------------------------------------

[**[display qos scheduler-policy diagnosis interface]{lang="EN-US"}**]{#struct_0_x2723_x1019_x132252726}[命令用来显示端口的诊断信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x656815323}

[**[display qos scheduler-policy diagnosis interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_x2723_x1019_x1766609913}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_355908815}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x118832797}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1977018866}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1334865867}

[[network-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_437426554}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1499169253}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_1871982255}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1541333733}

[*[interface-type interface-numb]{lang="EN-US"}*[er]{lang="EN-US"}]{#struct_0_x2723_x1019_x1746569968}[：指定端口类型和端口号。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1575525773}[：表示显示入方向的诊断信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x2723_x1019_1188732350}[：表示显示出方向的诊断信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x303067680}

[[如果未指定端口，将显示所有端口的诊断信息。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_137186887}

[[如果未指定方向，将显示出入两个方向的诊断信息。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1541370068}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1362536494}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1930941696}[显示指定端口入方向的诊断信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos scheduler-policy diagnosis interface gigabitethernet ]{lang="EN-US"}[1/0/1 inbound]{lang="EN-US"}]{#struct_0_x2723_x1019_437819770}

[SP \-- Scheduler policy      FG \-- Forwarding group     FC \-- Forwarding class]{lang="EN-US"}

[FP \-- Forwarding profile    L  \-- Layer]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: GigabitEthernet]{lang="EN-US"}[1/0/1]{lang="EN-US"}

[Direction: Inbound]{lang="EN-US"}

[SP: test_sp(1)]{lang="EN-US"}

[ \|]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): default(0)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|      Status: Success]{lang="EN-US"}

[ \|   \| ]{lang="EN-US"}

[ \|   +\--FC: BE(0)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|      Status: Success]{lang="EN-US"}

[ \|   \| ]{lang="EN-US"}

[ \|   +\--FC: AF(1)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|      Status: Success]{lang="EN-US"}

[ \|   \| ]{lang="EN-US"}

[ \|   +\--FC: EF(2)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|      Status: Success]{lang="EN-US"}

[ \|   \|  ]{lang="EN-US"}

[ \|   +\--FC: NC(3)]{lang="EN-US"}

[ \|          FP: default(0)]{lang="EN-US"}

[ \|          Status: Success]{lang="EN-US"}

[ \|  ]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): VOIP(1)]{lang="EN-US"}

[ \|   \|      FP: VOIP(2)]{lang="EN-US"}

[ \|   \|      Status: Success]{lang="EN-US"}

[ \|   \| ]{lang="EN-US"}

[ \|   \|  Match: service-vlan-id 2 to 10]{lang="EN-US"}

[ \|   +\--FG(L2): Customer1(2)]{lang="EN-US"}

[ \|   \|   \|      FP: Customer1(1)]{lang="EN-US"}

[ \|   \|   \|      Status: Success]{lang="EN-US"}

[ \|   \|   \| ]{lang="EN-US"}

[ \|   \|   +\--FC: BE(0)]{lang="EN-US"}

[ \|   \|   \|      FP: BE(3)]{lang="EN-US"}

[ \|   \|   \|      Status: Queue Failed]{lang="EN-US"}

[ \|   \|   \|  ]{lang="EN-US"}

[ \|   \|   +\--FC: AF(1)]{lang="EN-US"}

[ \|   \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|   \|      Status: GTS Failed]{lang="EN-US"}

[ \|   \|   \|  ]{lang="EN-US"}

[ \|   \|   +\--FC: EF(2)]{lang="EN-US"}

[ \|   \|   \|      FP: default(0)]{lang="EN-US"}

[ \|   \|   \|      Status: Success]{lang="EN-US"}

[ \|   \|   \|  ]{lang="EN-US"}

[ \|   \|   +\--FC: NC(3)]{lang="EN-US"}

[ \|   \|          FP: default(0)]{lang="EN-US"}

[ \|   \|          Status: Success]{lang="EN-US"}

[ \|   \|  ]{lang="EN-US"}

[ \|   \|  Match: service-vlan-id 11 to 20]{lang="EN-US"}

[ \|   +\--FG(L2): Customer2(5)]{lang="EN-US"}

[ \|       \|      FP: Customer2(2)]{lang="EN-US"}

[ \|       \|      Status: Incomplete]{lang="EN-US"}

[ \|       \|]{lang="EN-US"}

[ \|       +\--FC: BE(0)]{lang="EN-US"}

[ \|       \|      FP: BE(3)]{lang="EN-US"}

[ \|       \|      Status: Incomplete]{lang="EN-US"}

[ \|       \|]{lang="EN-US"}

[ \|       +\--FC: AF(1)]{lang="EN-US"}

[ \|       \|      FP: default(0)]{lang="EN-US"}

[ \|       \|      Status: Incomplete]{lang="EN-US"}

[ \|       \|  ]{lang="EN-US"}

[ \|       +\--FC: NC(3)]{lang="EN-US"}

[ \|              FP: default(0)]{lang="EN-US"}

[ \|              Status: Incomplete]{lang="EN-US"}

[ \|   ]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): INTERNET(4)]{lang="EN-US"}

[     \|      FP: INTERNET(4)]{lang="EN-US"}

[     \|      Status: Insufficent resources]{lang="EN-US"}

[     \|]{lang="EN-US"}

[     \|  Match: service-vlan-id 21 to 30]{lang="EN-US"}

[     +\--FG(L2): Customer3(6)]{lang="EN-US"}

[         \|      FP: Customer3(6)]{lang="EN-US"}

[         \|      Status: Insufficent resources]{lang="EN-US"}

[         \| ]{lang="EN-US"}

[         +\--FC: BE(0)]{lang="EN-US"}

[         \|      FP: BE(3)]{lang="EN-US"}

[         \|      Status: Insufficent resources]{lang="EN-US"}

[         \|         ]{lang="EN-US"}

[         +\--FC: AF(1)]{lang="EN-US"}

[         \|      FP: default(0)]{lang="EN-US"}

[         \|      Status: Insufficent resources]{lang="EN-US"}

[         \|]{lang="EN-US"}

[         +\--FC: EF(2)]{lang="EN-US"}

[         \|      FP: default(0)]{lang="EN-US"}

[         \|      Status: Insufficent resources]{lang="EN-US"}

[         \|]{lang="EN-US"}

[         +\--FC: NC(3)]{lang="EN-US"}

[                FP: default(0)]{lang="EN-US"}

[                ]{lang="EN-US"}[Status: Insufficent resources]{lang="EN-US"}

[]{#struct_0_x2723_x1019_x1405983062}[[表1-7 ]{lang="EN-US"}[display qos scheduler-policy diagnosis interface]{lang="EN-US"}]{#_Toc148586897}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1005372364}[[字段]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1710645490}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1996926068}

[[Interface]{lang="EN-US"}]{#struct_0_x2723_x1019_1274429630}

[[端口]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1900878609}

[[Direction]{lang="EN-US"}]{#struct_0_x2723_x1019_x1051342918}

[[方向]{style="font-family:宋体"}]{#struct_0_x2723_x1019_437885306}

[[Scheduler policy]{lang="EN-US"}]{#struct_0_x2723_x1019_x602303695}

[[调度策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_477527164}

[[Forwarding group]{lang="EN-US"}]{#struct_0_x2723_x1019_x1007047770}

[[转发组的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x275988831}

[[Forwarding class]{lang="EN-US"}]{#struct_0_x2723_x1019_x814588405}

[[转发类的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1367050410}

[[Forwarding profile]{lang="EN-US"}]{#struct_0_x2723_x1019_1703356791}

[[转发策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x938144455}

[[match]{lang="EN-US"}]{#struct_0_x2723_x1019_x933752927}

[[match]{lang="EN-US"}]{#struct_0_x2723_x1019_x896283666}[方式实例化]{style="font-family:宋体"}

[[service-vlan-id]{lang="EN-US"}]{#struct_0_x2723_x1019_1884276652}

[[实例化匹配规则]{style="font-family:宋体"}]{#struct_0_x2723_x1019_285303021}

[[status]{lang="EN-US"}]{#struct_0_x2723_x1019_1359747217}

[[节点的下发状态]{style="font-family:宋体"}]{#struct_0_x2723_x1019_495383668}

[[节点匹配规则不完整显示：]{style="font-family:宋体"}[Incomplete ]{lang="EN-US"}]{#struct_0_x2723_x1019_437295483}

[[所有内容下发成功显示：]{style="font-family:宋体"}[Success]{lang="EN-US"}]{#struct_0_x2723_x1019_626389288}

[[下发未完全成功时显示下发失败的部分，失败的原因包括：]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x868212611}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Insufficient]{lang="EN-US"}]{#struct_0_x2723_x1019_526649815}[ ]{lang="EN-US"}[resources]{lang="EN-US"}[：表示硬件资源不足]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Conflicting match rule]{lang="EN-US"}]{#struct_0_x2723_x1019_1232313975}[：]{lang="EN-US" style="font-family:宋体"}[match]{lang="EN-US"}[规则类型冲突]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not support]{lang="EN-US"}]{#struct_0_x2723_x1019_x157251112}[：配置不支持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GTS Failed]{lang="EN-US"}]{#struct_0_x2723_x1019_783973707}[：表示转发类]{style="font-family:宋体"}[/]{lang="EN-US"}[转发组整形参数下发失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WRED Failed]{lang="EN-US"}]{#struct_0_x2723_x1019_x733635334}[：表示转发类]{style="font-family:宋体"}[/]{lang="EN-US"}[转发组随机丢弃参数下发失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Queue Failed]{lang="EN-US"}]{#struct_0_x2723_x1019_1694014412}[：表示转发类]{style="font-family:宋体"}[/]{lang="EN-US"}[转发组的队列调度下发失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bandwidth Failed]{lang="EN-US"}]{#struct_0_x2723_x1019_x2081740007}[：表示转发类]{style="font-family:宋体"}[/]{lang="EN-US"}[转发组最小带宽保证下发失败]{style="font-family:宋体"}

[[如果多个部分失败，则同时显示所有失败的部分。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1123154685}

[]{#_Toc358032673}[]{#_Toc357857468}[]{#_Toc345167711}[[ ]{lang="EN-US"}]{#_Toc339901034}

::: {#-1012060144 .myid}
[]{#_Toc404792110}[]{#struct_0_x2723_x1019_x1796324523}

**HQoS \-- 调度策略配置命令 \-- display qos scheduler-policy interface**

------------------------------------------------------------------------

[**[display qos scheduler-policy interface]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1558417680}[命令用来显示端口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x410101636}

[**[display qos scheduler-policy interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_x2723_x1019_891706750}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_437361019}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1733156669}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1231419443}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x2021964592}

[[network-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_x995441459}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1348226675}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2723_x1019_x319419037}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_211944155}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2723_x1019_1185121418}[：指定端口类型和端口号。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1974014993}[：表示显示入方向的统计信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x2723_x1019_1034090274}[：表示显示出方向的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_609817888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定端口，将显示所有端口的统计信息。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1578341879}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定方向，将显示出入两个方向的统计信息。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x373636977}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有使能端口统计功能，输入此命令将只显示端口上应用的调度策略信息，不显示流量统计信息。端口统计功能]{style="font-family:宋体"}]{#struct_0_x2723_x1019_220315236}[的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_765144524}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_177980315}[显示指定端口入方向的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos scheduler-policy interface gigabitethernet ]{lang="EN-US"}[1/0/1 inbound]{lang="EN-US"}]{#struct_0_x2723_x1019_437492091}

[SP \-- Scheduler policy      FG \-- Forwarding group     FC \-- Forwarding class]{lang="EN-US"}

[FP \-- Forwarding profile    L  \-- Layer]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: GigabitEthernet]{lang="EN-US"}[1/0/1]{lang="EN-US"}

[Direction: Inbound]{lang="EN-US"}

[SP: test_sp(1)]{lang="EN-US"}

[ \|]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): default(0)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[\|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped red: 0 packets, 0 bytes ]{lang="EN-US"}

[\|   \|]{lang="EN-US"}

[ \|   +\--FC: BE(0)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[\|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|]{lang="EN-US"}

[ \|   +\--FC: AF(1)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[\|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \| ]{lang="EN-US"}

[ \|   +\--FC: EF(2)]{lang="EN-US"}

[ \|   \|      FP: default(0)]{lang="EN-US"}

[\|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|  ]{lang="EN-US"}

[ \|   +\--FC: NC(3)]{lang="EN-US"}

[ \|          FP: default(0)]{lang="EN-US"}

[\|          Total queue length: 200 packets ]{lang="EN-US"}

[ \|          Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|          Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|          Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|          Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|          Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|          Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|          Dropped: 0 packets, 0 bytes]{lang="EN-US"}

[ \|          Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|          Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|          Dropped red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): VOIP(1)]{lang="EN-US"}

[ \|   \|      FP: VOIP(2)]{lang="EN-US"}

[\|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|      Dropped red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \| ]{lang="EN-US"}

[ \|   \|  Match: service-vlan-id 2 to 10]{lang="EN-US"}

[ \|   +\--FG(L2): Customer1(2)]{lang="EN-US"}

[ \|   \|   \|      FP: Customer1(1)]{lang="EN-US"}

[\|   \|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[\|   \|   \|]{lang="EN-US"}

[ \|   \|   +\--FC: BE(0)]{lang="EN-US"}

[ \|   \|   \|      FP: BE(3)]{lang="EN-US"}

[\|   \|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|   \|  ]{lang="EN-US"}

[ \|   \|   +\--FC: AF(1)]{lang="EN-US"}

[ \|   \|   \|      FP: default(0)]{lang="EN-US"}

[\|   \|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|   \|  ]{lang="EN-US"}

[ \|   \|   +\--FC: EF(2)]{lang="EN-US"}

[ \|   \|   \|      FP: default(0)]{lang="EN-US"}

[\|   \|   \|      Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|   \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|   \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|   \|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|   \|  ]{lang="EN-US"}

[ \|   \|   +\--FC: NC(3)]{lang="EN-US"}

[ \|   \|          FP: default(0)]{lang="EN-US"}

[\|   \|          Total queue length: 200 packets ]{lang="EN-US"}

[ \|   \|          Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[ \|   \|          Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|          Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|          Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|          Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|          Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|          Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|          Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|          Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[ \|   \|          Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[ \|   \|  ]{lang="EN-US"}

[ \|   \|  Match: service-vlan-id 11 to 20]{lang="EN-US"}

[ \|   +\--FG(L2): Customer2(5)]{lang="EN-US"}

[ \|       \|      FP: Customer2(2)]{lang="EN-US"}

[ \|       \|]{lang="EN-US"}

[ \|       +\--FC: BE(0)]{lang="EN-US"}

[ \|       \|      FP: BE(3)]{lang="EN-US"}

[ \|       \|]{lang="EN-US"}

[ \|       +\--FC: AF(1)]{lang="EN-US"}

[ \|       \|      FP: default(0)]{lang="EN-US"}

[ \|       \|  ]{lang="EN-US"}

[ \|       +\--FC: NC(3)]{lang="EN-US"}

[ \|              FP: default(0)]{lang="EN-US"}

[ \|   ]{lang="EN-US"}

[ \|  Match: group]{lang="EN-US"}

[ +\--FG(L1): INTERNET(4)]{lang="EN-US"}

[     \|      FP: INTERNET(4)]{lang="EN-US"}

[     \|      Total queue length: 200 packets ]{lang="EN-US"}

[     \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[     \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[     \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[     \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[     \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[     \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[     \|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[     \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[     \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[     \|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[     \|]{lang="EN-US"}

[     \|  Match: service-vlan-id 21 to 30]{lang="EN-US"}

[     +\--FG(L2): Customer3(6)]{lang="EN-US"}

[         \|      FP: Customer3(6)]{lang="EN-US"}

[         \|      Total queue length: 200 packets ]{lang="EN-US"}

[         \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[         \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[         \| ]{lang="EN-US"}

[         +\--FC: BE(0)]{lang="EN-US"}

[         \|      FP: BE(3)]{lang="EN-US"}

[\|      Total queue length: 200 packets ]{lang="EN-US"}

[\|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[\|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[         \|         ]{lang="EN-US"}

[         +\--FC: AF(1)]{lang="EN-US"}

[         \|      FP: default(0)]{lang="EN-US"}

[\|      Total queue length: 200 packets ]{lang="EN-US"}

[\|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[\|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[\|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[         \|]{lang="EN-US"}

[         +\--FC: EF(2)]{lang="EN-US"}

[         \|      FP: default(0)]{lang="EN-US"}

[         \|      Total queue length: 200 packets ]{lang="EN-US"}

[         \|      Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[         \|      Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[         \|      Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[         \|]{lang="EN-US"}

[         +\--FC: NC(3)]{lang="EN-US"}

[                FP: default(0)]{lang="EN-US"}

[Total queue length: 200 packets ]{lang="EN-US"}

[Current queue length: 0 packets, 0% use ratio ]{lang="EN-US"}

[Forwarded: 0 packets, 0 bytes ]{lang="EN-US"}

[Forwarded green: 0 packets, 0 bytes ]{lang="EN-US"}

[Forwarded yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[Forwarded red: 0 packets, 0 bytes ]{lang="EN-US"}

[Tail dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[Dropped: 0 packets, 0 bytes ]{lang="EN-US"}

[Dropped green: 0 packets, 0 bytes ]{lang="EN-US"}

[Dropped yellow: 0 packets, 0 bytes ]{lang="EN-US"}

[Dropped red: 0 packets, 0 bytes]{lang="EN-US"}

[]{#struct_0_x2723_x1019_896409274}[[表1-8 ]{lang="EN-US"}[display qos scheduler-policy interface]{lang="EN-US"}]{#_Toc148586896}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1004069005}[[字段]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x964077937}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x2135207778}

[[Interface]{lang="EN-US"}]{#struct_0_x2723_x1019_343100394}

[[策略应用的端口]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x167542480}

[[Direction]{lang="EN-US"}]{#struct_0_x2723_x1019_374606435}

[[策略应用的方向]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x565483292}

[[Scheduler policy]{lang="EN-US"}]{#struct_0_x2723_x1019_x612794595}

[[调度策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_185247026}

[[Forwarding group]{lang="EN-US"}]{#struct_0_x2723_x1019_1331766411}

[[转发组的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1015403643}

[[Forwarding class]{lang="EN-US"}]{#struct_0_x2723_x1019_x1987439855}

[[转发类的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_437819771}

[[Forwarding profile]{lang="EN-US"}]{#struct_0_x2723_x1019_x1405983063}

[[转发策略的名称]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x144561549}

[[Total queue length]{lang="EN-US"}]{#struct_0_x2723_x1019_748127694}

[[队列总长度]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x194558236}

[[Current queue length]{lang="EN-US"}]{#struct_0_x2723_x1019_x1410170579}

[[当前队列长度]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_607638370}[使用比例]{style="font-family:宋体"}

[[Forwarded]{lang="EN-US"}]{#struct_0_x2723_x1019_x1680962694}

[[转发报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_x1856076227}[字节数]{style="font-family:宋体"}

[[Forwarded green]{lang="EN-US"}]{#struct_0_x2723_x1019_866465518}

[[转发绿色报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_1820767281}[字节数]{style="font-family:宋体"}

[[Forwarded yellow]{lang="EN-US"}]{#struct_0_x2723_x1019_840482524}

[[转发黄色报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_74352006}[字节数]{style="font-family:宋体"}

[[Forwarded red]{lang="EN-US"}]{#struct_0_x2723_x1019_x1763310442}

[[转发红色报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_437885307}[字节数]{style="font-family:宋体"}

[[Dropped]{lang="EN-US"}]{#struct_0_x2723_x1019_x602303694}

[[丢弃的报文总数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_477592700}[字节数]{style="font-family:宋体"}

[[Tail dropped]{lang="EN-US"}]{#struct_0_x2723_x1019_1345152449}

[[尾丢弃的报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_x539469179}[字节数]{style="font-family:宋体"}

[[Dropped green]{lang="EN-US"}]{#struct_0_x2723_x1019_1762530006}

[[丢弃的绿色报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_x1772924120}[字节数]{style="font-family:宋体"}

[[Dropped yellow]{lang="EN-US"}]{#struct_0_x2723_x1019_1321162558}

[[丢弃的黄色报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_1961958652}[字节数]{style="font-family:宋体"}

[[Dropped red]{lang="EN-US"}]{#struct_0_x2723_x1019_x1065701934}

[[丢弃的红色报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2723_x1019_617955500}[字节数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#905651546 .myid}
[]{#_Toc404792111}[]{#struct_0_x2723_x1019_1469936782}[]{#_Toc358032676}[]{#_Toc357857471}[]{#_Toc339901036}[]{#_Toc151609172}[]{#_Toc151608685}

**HQoS \-- 调度策略配置命令 \-- forwarding-group profile (scheduler-policy match view)**

------------------------------------------------------------------------

[**[forwarding-group profile]{lang="EN-US"}**]{#struct_0_x2723_x1019_1268452943}[命令用来配置调度策略嵌套转发组，并为该转发组指定转发策略。]{style="font-family:
宋体"}

[**[undo forwarding-group]{lang="EN-US"}**]{#struct_0_x2723_x1019_437295480}[命令用来取消配置调度策略嵌套的转发组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_626389287}

[**[forwarding-group]{lang="EN-US" style="color:black"}**[ *fg-name* **profile** *fp-name*]{lang="EN-US" style="color:black"}]{#struct_0_x2723_x1019_x868212604}

[**[undo forwarding-group]{lang="EN-US" style="color:black"}**[ *fg-name*]{lang="EN-US" style="color:black"}]{#struct_0_x2723_x1019_526322136}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x474302561}

[[调度策略以]{style="font-family:宋体"}[group]{lang="EN-US"}]{#struct_0_x2723_x1019_132705114}[方式嵌套预定义转发组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_800630911}

[[调度策略匹配规则视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1383552838}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_17665432}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1032085027}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1159561224}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_892337806}

[*[fg-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_862581412}[：]{style="font-family:
宋体"}[转发组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[fp-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_x306676730}[：转发策略名称，]{style="font-family:宋体;color:black"}[为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_256826071}

[[调度策略中默认嵌套的预定义转发组不能修改与删除。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_715212551}

[[在调度策略内嵌套转发组时需要保证转发组和对应的转发策略都已经存在。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1067500646}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_437361016}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1733156664}[配置调度策略]{style="font-family:宋体"}[VLAN ID 1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[匹配规则，嵌套转发组]{style="font-family:
宋体"}[testfg]{lang="EN-US"}[，并指定该转发组的转发策略]{style="font-family:
宋体"}[testfp]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_1990934330}

[\[Sysname\] qos scheduler-policy testsp]{lang="EN-US"}

[\[Sysname-hqos-sp-testsp\] match service-vlan-id 1 to 4]{lang="EN-US"}

[\[Sysname-hqos-sp-testsp-match\] forwarding-group testfg profile testfp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x703256079}[进入]{style="font-family:宋体"}[VLAN ID 1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[匹配规则视图，取消嵌套转发组]{style="font-family:
宋体"}[testfg]{lang="EN-US"}[，并取消关联转发策略]{style="font-family:
宋体"}[testfp]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_1017633264}

[\[Sysname\] qos scheduler-policy testsp]{lang="EN-US"}

[\[Sysname-hqos-sp-testsp\] match service-vlan-id 1 to 4]{lang="EN-US"}

[\[Sysname-hqos-sp-testsp-match\] undo forwarding-group testfg]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1934252276}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[match]{lang="EN-US"}**]{#struct_0_x2723_x1019_1776238411}
:::

::: {#-2049749445 .myid}
[]{#_Toc404792112}[]{#struct_0_x2723_x1019_474583153}

**HQoS \-- 调度策略配置命令 \-- match**

------------------------------------------------------------------------

[**[match]{lang="EN-US"}**]{#struct_0_x2723_x1019_716743174}[命令用来配置调度策略的匹配规则，并进入该匹配规则视图。]{style="font-family:宋体"}

[**[undo match]{lang="EN-US"}**]{#struct_0_x2723_x1019_x772624903}[命令用来取消配置调度策略的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1623141076}

[**[match]{lang="EN-US"}**[ { *match-criteria \|* **group }**]{lang="EN-US"}]{#struct_0_x2723_x1019_2082418334}

[**[undo match]{lang="EN-US"}**[ { *match-criteria* \| **group }**]{lang="EN-US"}]{#struct_0_x2723_x1019_344049312}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1804089541}

[[自定义调度策略无匹配规则。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_437164408}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1620839634}

[[调度策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1293928940}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_915061991}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1584565581}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_1211828566}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1342854917}

[*[match-criteria]{lang="EN-US"}*]{#struct_0_x2723_x1019_903686317}[：转发组的匹配规则，具体情况如]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-9]{lang="EN-US"}](?-2049749445#_Ref360725206)[所示。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**]{#struct_0_x2723_x1019_2035984459}[：该参数表示当前嵌套的转发组的匹配规则为其下嵌套的子转发组匹配规则的并集。]{style="font-family:宋体"}

[]{#struct_0_x2723_x1019_217986272}[[表1-9 ]{lang="EN-US"}[转发组的匹配规则取值]{style="font-family:
黑体"}]{#_Ref360725206}

[]{#table_struct_0_x979496677}[[取值]{style="font-family:黑体"}]{#struct_0_x2723_x1019_321523894}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1573084875}

[[service-vlan-id *vlan-id-list*]{lang="EN-US"}]{#struct_0_x2723_x1019_801214629}

[[定义匹配运营商网络]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x2723_x1019_x1735325686}[的规则]{style="font-family:宋体"}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x2723_x1019_x2011027577}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[vlan-id-list ]{lang="EN-US"}*[= { *vlan-id* \| *vlan-id1* **to** *vlan-id2* }&\<1-8\>]{lang="EN-US"}[，]{style="font-family:
  宋体"}*[vlan-id]{lang="EN-US"}*[、]{style="font-family:
  宋体"}*[vlan-id1]{lang="EN-US"}*[ ]{lang="EN-US"}[、]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，且]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[必须小于或等于]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[；]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[[local-precedence *precedence-value-list*]{lang="EN-US"}]{#struct_0_x2723_x1019_437229944}

[[定义匹配本地优先级的规则]{style="font-family:宋体"}]{#struct_0_x2723_x1019_249366231}

[*[precedence-value-list]{lang="EN-US"}*]{#struct_0_x2723_x1019_196436793}*[：]{style="font-family:
  宋体"}*[本地优先级列表，]{style="font-family:宋体"}[表示方式为]{style="font-family:宋体"}*[precedence-value-list]{lang="EN-US"}*[ = { *precedence-value* \| *precedence-value1* **to** *precedence-value2* }&\<1-8\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}*[、]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}[1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}[2]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，且]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}[1]{lang="EN-US"}*[必须小于或等于]{style="font-family:宋体"}*[precedence-value]{lang="EN-US"}[2]{lang="EN-US"}*[；]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[[dot1p *dot1p-value-list*]{lang="EN-US"}]{#struct_0_x2723_x1019_x2135718865}

[[定义匹配运营商网络]{style="font-family:宋体"}[802.1p]{lang="EN-US"}]{#struct_0_x2723_x1019_x881951019}[优先级的规则]{style="font-family:宋体"}

[*[dot1p-value-list]{lang="EN-US"}*]{#struct_0_x2723_x1019_1720433131}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级列表，表示方式为]{style="font-family:宋体"}*[dot1p-value-list ]{lang="EN-US"}*[= { *dot1p-value* \| *dot1p-value1* **to** *dot1p-value2* }&\<1-8\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[dot1p-value]{lang="EN-US"}*[、]{style="font-family:宋体"}*[dot1p-value1]{lang="EN-US"}*[ ]{lang="EN-US"}[、]{style="font-family:宋体"}*[dot1p-value2]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，且]{style="font-family:宋体"}*[dot1p-value1]{lang="EN-US"}*[必须小于或等于]{style="font-family:宋体"}*[dot1p-value2]{lang="EN-US"}*[；]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[[qos-local-id *local-id-list*]{lang="EN-US"}]{#struct_0_x2723_x1019_458854703}

[[定义匹配]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_x2723_x1019_x1777811355}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值的规则]{style="font-family:宋体"}

[*[local-id-list]{lang="EN-US"}*]{#struct_0_x2723_x1019_307693829}[：]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值]{style="font-family:宋体"}[列表，表示方式为]{style="font-family:宋体"}*[local-id-list ]{lang="EN-US"}*[= { *local-id* \| *local-id1* **to** *local-id2* }&\<1-8\>]{lang="EN-US"}[，]{style="font-family:
  宋体"}*[local-id]{lang="EN-US"}*[、]{style="font-family:
  宋体"}*[local-id1]{lang="EN-US"}*[ ]{lang="EN-US"}[、]{style="font-family:宋体"}*[local-id2]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，且]{style="font-family:宋体"}*[local-id1]{lang="EN-US"}*[必须小于或等于]{style="font-family:宋体"}*[local-id2]{lang="EN-US"}*[；]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_735676047}

[[配置匹配规则只是进入视图，并不实际生成配置，仅当在匹配规则下进一步配置嵌套的子转发组后，匹配规则配置才真正生效。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_437557624}

[[嵌套转发类的转发组不能采用]{style="font-family:宋体"}[group]{lang="EN-US"}]{#struct_0_x2723_x1019_453368781}[方式实例化；但是，调度策略可以以]{style="font-family:宋体"}[group]{lang="EN-US"}[方式嵌套预定义转发组。]{style="font-family:宋体"}

[[取消配置匹配规则会同时删除该匹配规则下嵌套的转发组和转发策略。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x113794293}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x774789835}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x493295317}[配置调度策略的]{style="font-family:宋体"}[VLAN ID 1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[匹配规则。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_935887699}

[\[Sysname\] qos scheduler-policy testsp]{lang="EN-US"}

[\[Sysname-hqos-sp-testsp\] match service-vlan-id 1 to 4]{lang="EN-US"}

[\[Sysname-hqos-sp-testsp-match\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1621395446}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[forwarding-group profile]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x2723_x1019_x850995659}[forwarding-group]{lang="EN-US"}[ match view)]{lang="EN-US"}

::: {#-168396272 .myid}
[]{#_Toc404792113}[]{#struct_0_x2723_x1019_x1194021916}[]{#_Toc358032677}[]{#_Toc357857472}[]{#_Toc345167715}[]{#_Toc339901037}[]{#_Toc151609174}[]{#_Toc151608687}

**HQoS \-- 调度策略配置命令 \-- qos apply scheduler-policy**

------------------------------------------------------------------------

[**[qos apply scheduler-policy]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1941721591}[命令用来在接口上应用调度策略。]{style="font-family:
宋体"}

[**[undo qos apply scheduler-policy]{lang="EN-US"}**]{#struct_0_x2723_x1019_1430555125}[命令用来取消在接口上应用的调度策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1776274799}

[**[qos apply scheduler-policy]{lang="EN-US"}**[ *sp-name* { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x2723_x1019_1575356333}

[**[undo qos apply scheduler-policy ]{lang="EN-US"}***[sp-name ]{lang="EN-US"}*[{ **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x2723_x1019_x2024673080}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_437623160}

[[接口下没有应用调度策略。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1229149269}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1737703939}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_632398655}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1409232335}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1771160845}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x185102541}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_381836077}

[*[sp-name]{lang="EN-US"}*]{#struct_0_x2723_x1019_x457769923}[：]{style="font-family:宋体"}[调度策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1681841429}[：表示在入方向下发调度策略。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x2723_x1019_1229770919}[：表示在出方向下发调度策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_398799744}

[[接口的每个方向上只能应用一个调度策略。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1562850402}

[[在接口上应用调度策略的配置与端口]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_x2723_x1019_x203600334}[配置互斥（包括基于队列的]{style="font-family:宋体"}[GTS]{lang="EN-US"}[、端口]{style="font-family:宋体"}[WRED]{lang="EN-US"}[、硬件队列调度），且不区分方向。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1937830305}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x365226989}[在接口入方向应用调度策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_437426552}

[\[Sysname\] interface gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet]{lang="EN-US"}[1/0/1\] qos apply scheduler-policy testsp inbound]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1499169255}[在接口入方向取消应用调度策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_1065413201}

[\[Sysname\] interface gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet]{lang="EN-US"}[1/0/1\] undo qos apply scheduler-policy testsp inbound]{lang="EN-US"}
:::

::: {#-1288225137 .myid}
[]{#_Toc404792114}[]{#struct_0_x2723_x1019_x95768295}[]{#_Toc358032678}[]{#_Toc357857473}[]{#_Toc345167716}[]{#_Toc339901039}[]{#_Toc151609176}[]{#_Toc151608689}

**HQoS \-- 调度策略配置命令 \-- qos scheduler-policy**

------------------------------------------------------------------------

[**[qos scheduler-policy]{lang="EN-US"}**]{#struct_0_x2723_x1019_115214744}[命令用来创建用户自定义的调度策略，并进入该调度策略视图。]{style="font-family:宋体"}

[**[undo qos scheduler-policy]{lang="EN-US"}**]{#struct_0_x2723_x1019_1848046777}[命令用来删除用户自定义的调度策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x1516992455}

[**[qos scheduler-policy]{lang="EN-US"}**[ *sp-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_x1908806162}

[**[undo qos scheduler-policy]{lang="EN-US"}**[ *sp-name*]{lang="EN-US"}]{#struct_0_x2723_x1019_1988181283}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1764682726}

[[未创建自定义调度策略。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_x1888863043}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1523830756}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_2064986844}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1085145504}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1790001574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1272119301}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1500175199}

[*[sp-name]{lang="EN-US" style="color:black"}*]{#struct_0_x2723_x1019_2063493832}[：自定义]{style="font-family:
宋体"}[调度策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_2002494883}

[[系统最多支持创建的调度策略个数为]{style="font-family:宋体"}[256]{lang="EN-US"}]{#struct_0_x2723_x1019_499444305}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_437492088}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_x1442242893}[创建自定义调度策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x2070736892}

[\[Sysname\] qos scheduler-policy testsp]{lang="EN-US"}
:::

::::: {#1423475573 .myid}
[]{#_Toc404792115}[]{#struct_0_x2723_x1019_x381806019}[]{#_Toc358032675}[]{#_Toc357857470}[]{#_Toc345167713}

**HQoS \-- 调度策略配置命令 \-- scheduler-unit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](HQoS命令.files/image001.png){#图片 39 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2723_x1019_x692375901}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2723_x1019_x725646412}
:::

**[ ]{lang="EN-US"}**

[**[scheduler-unit]{lang="EN-US"}**]{#struct_0_x2723_x1019_x552855452}[命令用来配置调度策略的调度权重单位。]{style="font-family:宋体"}

[**[undo scheduler-unit]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1555387390}[命令用来恢复调度策略调度权重单位的缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x250137843}

[**[scheduler-unit]{lang="EN-US"}**[ { **byte-count** \| **weight** }]{lang="EN-US"}]{#struct_0_x2723_x1019_896909765}

[**[undo scheduler-unit]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1658020457}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x277935937}

[[调度策略调度权重单位的缺省值根据实际设备决定。]{style="font-family:宋体"}]{#struct_0_x2723_x1019_145776820}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_1470810504}

[[调度策略视图]{style="font-family:宋体"}]{#struct_0_x2723_x1019_1198273535}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_x2119304421}

[[network-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_x1158538198}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2723_x1019_437819768}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_550332082}

[**[byte-count]{lang="EN-US"}**]{#struct_0_x2723_x1019_x1517087994}[：]{style="font-family:宋体"}[按照每次轮询可发送的字节数进行计算。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}**]{#struct_0_x2723_x1019_x73756374}[：]{style="font-family:宋体"}[按照权重进行计算]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2723_x1019_652629778}

[[\# ]{lang="EN-US"}]{#struct_0_x2723_x1019_214475141}[将调度策略指定为按]{style="font-family:宋体"}[byte-count]{lang="EN-US"}[调度。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2723_x1019_x1599689776}

[\[Sysname\] qos scheduler-policy testsp]{lang="EN-US"}

[\[Sysname-hqos-sp-testsp\] scheduler-unit byte-count]{lang="EN-US"}

[ ]{lang="EN-US"}
:::::
