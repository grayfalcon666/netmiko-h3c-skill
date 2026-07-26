::: {#-839206977 .myid}
[]{#_Toc340836288}[]{#_Toc340836290}[]{#_Toc404794807}[]{#struct_0_73193_x1990_2125682936}[]{#_Toc393205672}

**AP管理 \-- AP管理配置命令 \-- ap**

------------------------------------------------------------------------

[**[ap]{lang="EN-US"}**]{#struct_0_73193_x1990_1854607574}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[名字入组规则。]{style="font-family:宋体"}

[**[undo ap]{lang="EN-US"}**]{#struct_0_73193_x1990_x1888815989}[命令用来删除]{style="font-family:宋体"}[AP]{lang="EN-US"}[名字入组规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1052561092}

[**[ap]{lang="EN-US"}**[ *ap-name-list*]{lang="EN-US"}]{#struct_0_73193_x1990_2014883804}

[**[undo ap]{lang="EN-US"}**[ *ap-name-list*]{lang="EN-US"}]{#struct_0_73193_x1990_150968779}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1999994495}

[[未配置]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x357011299}[名字入组规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1688437503}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1094161738}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x152861725}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x524714380}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1163120874}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1120090382}

[[ap-name-list:A[P]{style="color:black"}]{lang="EN-US"}]{#struct_0_73193_x1990_895235032}[的名字列表，表示方式为]{style="font-family:宋体"}[ap-name-list={ ap-name[ ]{style="color:black"}}&\<1[-10]{style="color:black"}\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}[ap-name]{lang="EN-US"}[为]{style="font-family:宋体"}[AP]{lang="EN-US" style="color:black"}[的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，可以包含字母、数字及下划线，不区分大小写，]{style="font-family:宋体"}[&\<[1]{style="color:black"}-[10]{style="color:black"}\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x834322695}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不检查指定的]{style="font-family:宋体"}]{#struct_0_73193_x1990_x1246770319}[AP]{lang="EN-US"}[是否存在。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同型号的设备支持的最大]{style="font-family:宋体"}]{#struct_0_73193_x1990_1156244928}[AP]{lang="EN-US"}[数不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x736996635}[名字如入规则的优先级高于序列号入组规则，序列号入组规则的优先级高于]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址入组规则。]{style="font-family:宋体"}[AP]{lang="EN-US"}[优先根据]{style="font-family:宋体"}[AP]{lang="EN-US"}[名字入组规则匹配入组，其次是]{style="font-family:宋体"}[AP]{lang="EN-US"}[序列号入组规则，然后是]{style="font-family:宋体"}[AP MAC ]{lang="EN-US"}[地址入组规则，若未匹配到任何入组规则，则]{style="font-family:宋体"}[AP]{lang="EN-US"}[将被加入到默认组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[默认组视图下不能进行该配置。]{style="font-family:宋体"}]{#struct_0_73193_x1990_636877250}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1902698890}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1851766425}[在]{style="font-family:宋体"}[AP]{lang="EN-US"}[组视图下添加名字入组规则。]{style="font-family:宋体"}

[[\<System\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_1504012560}

[\[System\] wlan ap-group group1]{lang="EN-US"}

[\[System-wlan-ap-group-group1\] ap ap1 ap2 ap3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1718945666}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wlan]{lang="EN-US"}**]{#struct_0_73193_x1990_1171876224}**[ ]{lang="EN-US"}[ap-group]{lang="EN-US"}**
:::

::: {#1391204813 .myid}
[]{#_Toc404794808}[]{#struct_0_73193_x1990_x274748668}

**AP管理 \-- AP管理配置命令 \-- cir**

------------------------------------------------------------------------

[**[cir]{lang="EN-US"}**]{#struct_0_73193_x1990_322330056}[命令用来设置承诺信息速率和承诺突发尺寸以实现流量保护功能。]{style="font-family:宋体"}

[**[undo cir]{lang="EN-US"}**]{#struct_0_73193_x1990_x1495848201}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1687541929}

[**[cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*[ \[ **cbs** *committed-burst-size* \]]{lang="EN-US"}]{#struct_0_73193_x1990_1232327002}

[**[undo cir]{lang="EN-US"}**]{#struct_0_73193_x1990_1008711533}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_862033959}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x888510651}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_63348541}[组视图：未设置承诺信息速率和承诺突发尺寸]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1529920304}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1077577588}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x107984434}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1918974926}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_794840058}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x2140853916}

[**[cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*]{#struct_0_73193_x1990_1997054100}[：承诺信息速率，取值范围为]{style="font-family:宋体"}[40]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}***[ committed-burst-size]{lang="EN-US"}*]{#struct_0_73193_x1990_873212697}[：承诺突发尺寸，取值范围为]{style="font-family:宋体"}[2500]{lang="EN-US"}[～]{style="font-family:宋体"}[62500000]{lang="EN-US"}[。如果未指定本参数，则表示承诺突发尺寸为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒以]{style="font-family:宋体"}[CIR]{lang="EN-US"}[速率通过的流量，单位为]{style="font-family:宋体"}[Bytes]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x254982765}

[[开启流量保护功能后可以对]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_73193_x1990_2127759794}[和]{style="font-family:宋体"}[AP]{lang="EN-US"}[间的数据流量进行限速，防止由于]{style="font-family:宋体"}[AP]{lang="EN-US"}[遭受超过其处理能力的数据流量冲击，使]{style="font-family:宋体"}[AP]{lang="EN-US"}[无法及时向]{style="font-family:宋体"}[AC]{lang="EN-US"}[回复报文而导致]{style="font-family:宋体"}[AP]{lang="EN-US"}[频繁重启。]{style="font-family:宋体"}

[[有关]{style="font-family:宋体"}**[cir]{lang="EN-US"}**]{#struct_0_73193_x1990_x506489575}[命令的详细介绍与配置请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考"中的"]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_133972138}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1911398423}[设置承诺速率为]{style="font-family:宋体"}[60Kbps]{lang="EN-US"}[，承诺突发尺寸为]{style="font-family:宋体"}[3000Bytes]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_1439148578}

[\[Sysname\] wlan ap ap1 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] cir 60 cbs 3000]{lang="EN-US"}
:::

::: {#-1194519698 .myid}
[]{#_Toc404794809}[]{#struct_0_73193_x1990_1814264331}[]{#_Toc177034948}

**AP管理 \-- AP管理配置命令 \-- description(AP view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_73193_x1990_1765529552}[命令用来设置]{style="font-family:宋体"}[AP]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_73193_x1990_83370726}[命令用来清除]{style="font-family:宋体"}[AP]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1666248541}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_73193_x1990_1738387257}

[**[undo description]{lang="EN-US"}**]{#struct_0_73193_x1990_1277802351}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x202105544}

[[未设置]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1913337826}[的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x992970267}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x47110524}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_385966025}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1047716652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_248180390}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_202241358}

[*[text]{lang="EN-US"}*]{#struct_0_73193_x1990_609715628}[：网络中]{style="font-family:宋体"}[AP]{lang="EN-US"}[的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1375937541}

[[当存在多个]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_53377771}[时，可以配置每个]{style="font-family:宋体"}[AP]{lang="EN-US"}[的描述信息，以便区别各个]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[使用]{style="font-family:宋体"}**[display wlan ap]{lang="EN-US"}**]{#struct_0_73193_x1990_x284907760}[命令可以看到配置的描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_424321818}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_2110510053}[设置]{style="font-family:宋体"}[ap1]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_73193_x1990_542439626}

[\[Sysname\] wlan ap ap1 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-ap-ap1\] description L3-office]{lang="EN-US"}
:::

::: {#-2105995816 .myid}
[]{#_Toc404794810}[]{#struct_0_73193_x1990_x1099450873}[]{#_Toc367213910}

**AP管理 \-- AP管理配置命令 \-- description(AP group view)**

------------------------------------------------------------------------

[**[description ]{lang="EN-US"}**]{#struct_0_73193_x1990_x1870104308}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_73193_x1990_1733487643}[命令用来清除]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1693103809}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_73193_x1990_x1484260676}

[**[undo description]{lang="EN-US"}**]{#struct_0_73193_x1990_x818252455}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_725936320}

[[未配置]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1280266919}[组的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_906874019}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1959104132}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x309874271}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x301677489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1284550787}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1575532670}

[*[text]{lang="EN-US"}*]{#struct_0_73193_x1990_1049184231}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x885296822}

[[当存在多个]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x813945476}[组时，可以配置每个]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的描述信息，以便区别各个]{style="font-family:宋体"}[AP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[使用]{style="font-family:宋体"}**[display wlan ap-group]{lang="EN-US"}**]{#struct_0_73193_x1990_466633068}[命令可以看到配置的描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_133054129}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1312923622}[设置]{style="font-family:宋体"}[group1]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_73193_x1990_690267691}

[\[Sysname\] wlan ap-group group1]{lang="EN-US"}

[\[Sysname-ap-group-group1\] description L3-office]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1976757878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wlan ap-group]{lang="EN-US"}**]{#struct_0_73193_x1990_225672116}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display wlan ap-group]{lang="EN-US"}**]{#struct_0_73193_x1990_465413084}
:::

::: {#799262023 .myid}
[]{#_Toc404794811}[]{#struct_0_73193_x1990_x2141111857}[]{#_Toc345613631}

**AP管理 \-- AP管理配置命令 \-- display wlan ap**

------------------------------------------------------------------------

[**[display wlan ap]{lang="EN-US"}**]{#struct_0_73193_x1990_x775526505}[命令用来显示指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[或所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1317903551}

[**[display wlan ap]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ **all** *\|* **name** *ap-name* } \[ **radio** \| **verbose** \]]{lang="EN-US"}]{#struct_0_73193_x1990_1647258271}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_29616370}

[[任意视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_920351725}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x422994115}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x851431598}

[[network-operator]{lang="EN-US"}]{#struct_0_73193_x1990_x61374987}

[[mdc -admin]{lang="EN-US"}]{#struct_0_73193_x1990_1780548349}

[[mdc -operator]{lang="EN-US"}]{#struct_0_73193_x1990_x1332162062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1296122858}

[**[all]{lang="EN-US"}**]{#struct_0_73193_x1990_1379408049}[：显示所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ap-name]{lang="EN-US"}*]{#struct_0_73193_x1990_1387761575}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，可以包含字母、数字、下划线和横线。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**]{#struct_0_73193_x1990_x1660140973}[：显示]{style="font-family:宋体"}[AP]{lang="EN-US"}[上]{style="font-family:宋体"}[radio]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_73193_x1990_1410979804}[：显示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_868561979}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x214802286}[显示所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan ap all]{lang="EN-US"}]{#struct_0_73193_x1990_x393418253}

[Total number of APs: 2]{lang="EN-US"}

[Total number of connected APs: 1]{lang="EN-US"}

[Total number of configured APs connected: 1]{lang="EN-US"}

[Total number of connected auto APs: 0]{lang="EN-US"}

[Maximum AP capacity: 60000]{lang="EN-US"}

[Remaining AP capacity: 59999]{lang="EN-US"}

[                                 AP information]{lang="EN-US"}

[ State : I = Idle,       J  = Join,       JA = JoinAck,    IL = ImageLoad]{lang="EN-US"}

[         C = Config,     DC = DataCheck,  R  = Run]{lang="EN-US"}

[ ]{lang="EN-US"}

[AP name                AP ID   State   Model             Serial ID]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ap1                    1       I       WA4620i-AGN       210235A1BSC123000050]{lang="EN-US"}

[ap2                    2       R       WA5620i-AGN       210456B9CEN238400040]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display wlan ap name]{lang="EN-US"}]{#struct_0_73193_x1990_x1028095664}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1995609217}[[字段]{style="font-family:黑体"}]{#struct_0_73193_x1990_x478594244}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1343302448}

[[Total number of APs]{lang="EN-US"}]{#struct_0_73193_x1990_x578909291}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1645275511}[的数量]{style="font-family:宋体"}

[[Total number of connected APs]{lang="EN-US"}]{#struct_0_73193_x1990_x1378425273}

[[处于连接状态的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x968499926}[的数量]{style="font-family:宋体"}

[[Total number of configured APs connected]{lang="EN-US"}]{#struct_0_73193_x1990_1267142583}

[[处于连接状态的手工]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1896923941}[数量]{style="font-family:宋体"}

[[Total number of connected auto APs]{lang="EN-US"}]{#struct_0_73193_x1990_x578843755}

[[处于连接状态的自动]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_452229018}[的数量]{style="font-family:宋体"}

[[Maximum AP capacity]{lang="EN-US"}]{#struct_0_73193_x1990_x1215391501}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_x298941358}[上最大]{style="font-family:宋体"}[AP]{lang="EN-US"}[容量]{style="font-family:宋体"}

[[Remaining AP capacity]{lang="EN-US"}]{#struct_0_73193_x1990_x504253972}

[[剩余]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1872657439}[容量，即最大]{style="font-family:宋体"}[AP]{lang="EN-US"}[容量减去处于连接状态的]{style="font-family:宋体"}[AP]{lang="EN-US"}[数]{style="font-family:宋体"}

[[AP ID]{lang="EN-US"}]{#struct_0_73193_x1990_x155104137}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_934551449}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，用于在]{style="font-family:宋体"}[AC]{lang="EN-US"}[上唯一标识一个]{style="font-family:宋体"}[AP]{lang="EN-US"}

[[AP name]{lang="EN-US"}]{#struct_0_73193_x1990_x1709273368}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1266863149}[实体名]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_73193_x1990_1015294882}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1439836213}[当前状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_73193_x1990_817379576}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[J]{lang="EN-US"}]{#struct_0_73193_x1990_x1628656552}[：连接建立状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[JA]{lang="EN-US"}]{#struct_0_73193_x1990_x168857679}[：]{style="font-family:宋体"}[LWAPP]{lang="EN-US"}[连接确认阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IL]{lang="EN-US"}]{#struct_0_73193_x1990_x1721188078}[：版本下载状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_73193_x1990_317142989}[：初始化配置下载状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DC]{lang="EN-US"}]{#struct_0_73193_x1990_167449485}[：数据校验状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_73193_x1990_796853995}[：运行状态，表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[与]{style="font-family:宋体"}[AC]{lang="EN-US"}[成功建立]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Model]{lang="EN-US"}]{#struct_0_73193_x1990_x2049308309}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1119563980}[型号信息]{style="font-family:宋体"}

[[Serial ID]{lang="EN-US"}]{#struct_0_73193_x1990_x628181102}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1007695277}[序列号，如果未指定，则显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1399679656}[显示]{style="font-family:宋体"}[ap1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan ap name ap1 verbose]{lang="EN-US"}]{#struct_0_73193_x1990_x558388664}

[AP name                       : ap1]{lang="EN-US"}

[AP ID                         : 1]{lang="EN-US"}

[State                         : Run]{lang="EN-US"}

[Model                         : WA4620i-AGN]{lang="EN-US"}

[Serial ID                     : 210235A1BSC123000050]{lang="EN-US"}

[IP address                    : 192.168.1.50]{lang="EN-US"}

[H/W version                   : Ver.C]{lang="EN-US"}

[S/W version                   : V700R001B49D001]{lang="EN-US"}

[Boot version                  : 1.01]{lang="EN-US"}

[Description                   : wtp1]{lang="EN-US"}

[Priority                      : 4]{lang="EN-US"}

[Echo interval                 : 10 seconds]{lang="EN-US"}

[Statistics report interval    : 50 seconds]{lang="EN-US"}

[CIR                           : 60 kbps]{lang="EN-US"}

[CBS                           : 3000 bytes]{lang="EN-US"}

[Jumbo frame value             : Disabled]{lang="EN-US"}

[MAC address                   : 80F6-2EBF-C580]{lang="EN-US"}

[MAC type                      : Local MAC & Split MAC]{lang="EN-US"}

[Tunnel mode                   : Local Bridging & 802.3 Frame & Native Frame]{lang="EN-US"}

[Discovery type                : Static Configuration]{lang="EN-US"}

[Retransmission count          : 3]{lang="EN-US"}

[Retransmission interval       : 5 seconds]{lang="EN-US"}

[Firmware upgrade              : Enabled]{lang="EN-US"}

[Sent control packets          : 1]{lang="EN-US"}

[Received control packets      : 1]{lang="EN-US"}

[Connection count              : 1]{lang="EN-US"}

[Radio 1:]{lang="EN-US"}

[    Basic BSSID               : N/A]{lang="EN-US"}

[    Admin state               : Down]{lang="EN-US"}

[    Radio type                : 802.11n(5GHz)]{lang="EN-US"}

[    Client dot11n-only        : Disabled]{lang="EN-US"}

[    Channel band-width        : 20/40MHz]{lang="EN-US"}

[    Secondary channel offset  : SCN]{lang="EN-US"}

[    Short GI for 20MHz        : Supported]{lang="EN-US"}

[    Short GI for 40MHz        : Supported]{lang="EN-US"}

[    A-MSDU                    : Enabled]{lang="EN-US"}

[    A-MPDU                    : Enabled]{lang="EN-US"}

[    Operational HT MCS Set:]{lang="EN-US"}

[        Mandatory             : Not configured]{lang="EN-US"}

[        Supported             : Not configured]{lang="EN-US"}

[    Channel                   : auto\<64\>]{lang="EN-US"}

[    Max power                 : 13 dBm]{lang="EN-US"}

[    Operational rate:]{lang="EN-US"}

[        Mandatory             : 6, 12, 24 Mbps]{lang="EN-US"}

[        Supported             : 9, 18, 36, 48, 54 Mbps]{lang="EN-US"}

[        Multicast             : 24 Mbps]{lang="EN-US"}

[        Disabled              : Not configured]{lang="EN-US"}

[    beacon-interval           : 100 time unit]{lang="EN-US"}

[    distance                  : 1 kilometer]{lang="EN-US"}

[Radio 2:]{lang="EN-US"}

[    Basic BSSID               : N/A]{lang="EN-US"}

[    Admin state               : Down]{lang="EN-US"}

[    Radio type                : 802.11n(2.4GHz)]{lang="EN-US"}

[    Client dot11n-only        : Disabled]{lang="EN-US"}

[    Channel band-width        : 20MHz]{lang="EN-US"}

[    Secondary channel offset  : SCN]{lang="EN-US"}

[    Short GI for 20MHz        : Supported]{lang="EN-US"}

[    Short GI for 40MHz        : Supported]{lang="EN-US"}

[    A-MSDU                    : Enabled]{lang="EN-US"}

[    A-MPDU                    : Enabled]{lang="EN-US"}

[    Operational HT MCS Set:]{lang="EN-US"}

[        Mandatory             : Not configured]{lang="EN-US"}

[        Supported             : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]{lang="EN-US"}

[                                10, 11, 12, 13, 14, 15]{lang="EN-US"}

[    Channel                   : auto\<6\>]{lang="EN-US"}

[    Max power                 : 20 dBm]{lang="EN-US"}

[    Preamble type             : short]{lang="EN-US"}

[    Operational rate:]{lang="EN-US"}

[        Mandatory             : 1, 2, 5.5, 11 Mbps]{lang="EN-US"}

[        Supported             : 6, 9, 12, 18, 24, 36, 48, 54 Mbps]{lang="EN-US"}

[        Multicast             : 11 Mbps]{lang="EN-US"}

[        Disabled              : Not configured]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display wlan ap name verbose]{lang="EN-US"}]{#struct_0_73193_x1990_285382425}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1965531437}[[字段]{style="font-family:黑体"}]{#struct_0_73193_x1990_x968014559}

[[描述]{style="font-family:黑体"}]{#struct_0_73193_x1990_x98241849}

[[AP ID]{lang="EN-US"}]{#struct_0_73193_x1990_1442291737}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x756434768}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，用于唯一标识一个]{style="font-family:宋体"}[AP]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_73193_x1990_1509105698}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1522428616}[当前状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_73193_x1990_1458033971}[：空闲]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Join]{lang="EN-US"}]{#struct_0_73193_x1990_1279838021}[：连接建立状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[JoinAck]{lang="EN-US"}]{#struct_0_73193_x1990_1600360233}[：]{lang="EN-US" style="font-family:宋体"}[LWAPP]{lang="EN-US"}[连接确认状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Image Download]{lang="EN-US"}]{#struct_0_73193_x1990_x1343216631}[：版本下载状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Config]{lang="EN-US"}]{#struct_0_73193_x1990_x534224973}[：初始化配置下载状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Data Check]{lang="EN-US"}]{#struct_0_73193_x1990_x995291265}[：数据校验状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Run]{lang="EN-US"}]{#struct_0_73193_x1990_x1704021790}[：运行状态]{lang="EN-US" style="font-family:宋体"}

[[Model]{lang="EN-US"}]{#struct_0_73193_x1990_x108049970}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x999290386}[型号信息]{style="font-family:宋体"}

[[Serial ID]{lang="EN-US"}]{#struct_0_73193_x1990_x447732357}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_596256824}[序列号。如果未指定序列号，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}

[[IP address]{lang="EN-US"}]{#struct_0_73193_x1990_x814047655}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_598885967}[当前连接的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[H/W version]{lang="EN-US"}]{#struct_0_73193_x1990_1814198795}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_595241431}[当前硬件信息]{style="font-family:宋体"}

[[S/W version]{lang="EN-US"}]{#struct_0_73193_x1990_1143685668}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_500753853}[当前软件信息]{style="font-family:宋体"}

[[Boot version]{lang="EN-US"}]{#struct_0_73193_x1990_x1710507998}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1948003723}[当前引导程序版本]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_73193_x1990_248114854}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x946747980}[描述信息。如果未指定描述信息，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}

[[Priority]{lang="EN-US"}]{#struct_0_73193_x1990_22137458}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_x529378599}[配置的]{style="font-family:宋体"}[AP]{lang="EN-US"}[连接的优先级]{style="font-family:宋体"}

[[Echo interval]{lang="EN-US"}]{#struct_0_73193_x1990_x1878678043}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1484036922}[的两次回声请求的时间间隔]{style="font-family:宋体"}

[[Statistics report interval]{lang="EN-US"}]{#struct_0_73193_x1990_x1317969087}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x219586806}[上报统计信息的时间间隔]{style="font-family:宋体"}

[[CIR]{lang="EN-US"}]{#struct_0_73193_x1990_1181465524}

[[限制]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_73193_x1990_235126263}[向]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送数据报文的速率。如果未指定速率，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}

[[CBS]{lang="EN-US"}]{#struct_0_73193_x1990_x918606057}

[[限制]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_73193_x1990_1410914268}[向]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送数据报文的突发尺寸。如果未指定突发尺寸，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}

[[Jumbo frame value]{lang="EN-US"}]{#struct_0_73193_x1990_x1881221524}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_x530456789}[配置的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧的最大长度。如果未指定最大长度，显示为]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[MAC address]{lang="EN-US"}]{#struct_0_73193_x1990_11467108}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_2049979416}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC type]{lang="EN-US"}]{#struct_0_73193_x1990_x155169673}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_73867838}[与]{style="font-family:宋体"}[AC]{lang="EN-US"}[连接的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[模式类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local MAC]{lang="EN-US"}]{#struct_0_73193_x1990_x1859784113}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[侧数据帧支持]{lang="EN-US" style="font-family:宋体"}[802.3]{lang="EN-US"}[格式封装]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Split MAC]{lang="EN-US"}]{#struct_0_73193_x1990_x832184887}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[侧数据帧支持]{lang="EN-US" style="font-family:宋体"}[802.11]{lang="EN-US"}[格式封装]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local & Split MAC]{lang="EN-US"}]{#struct_0_73193_x1990_1696796572}[：]{lang="EN-US" style="font-family:
  宋体"}[AP]{lang="EN-US"}[侧数据帧支持]{lang="EN-US" style="font-family:
  宋体"}[802.3]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[802.11]{lang="EN-US"}[格式封装]{lang="EN-US" style="font-family:宋体"}

[[Tunnel mode]{lang="EN-US"}]{#struct_0_73193_x1990_x1721253614}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1764966156}[支持的隧道模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local Bridging]{lang="EN-US"}]{#struct_0_73193_x1990_17567305}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[侧支持用户数据本地桥接，不上送给]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.3 Frame]{lang="EN-US"}]{#struct_0_73193_x1990_x616426157}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[侧支持用户数据以]{style="font-family:宋体"}[802.3]{lang="EN-US"}[帧格式封装上传给]{style="font-family:宋体"}[AC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Native Frame]{lang="EN-US"}]{#struct_0_73193_x1990_1007629741}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[侧支持用户数据以]{lang="EN-US" style="font-family:宋体"}[802.11]{lang="EN-US"}[帧格式封装上传给]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local Bridging & 802.3 Frame]{lang="EN-US"}]{#struct_0_73193_x1990_636960023}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[侧支持用户数据本地桥接、以]{lang="EN-US" style="font-family:宋体"}[802.]{lang="EN-US"}[3]{lang="EN-US"}[帧格式封装上传]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.3 Frame & Native Frame]{lang="EN-US"}]{#struct_0_73193_x1990_819672352}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[侧支持用户数据以]{lang="EN-US" style="font-family:宋体"}[802.3]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[802.11]{lang="EN-US"}[帧格式封装上传]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local Bridging & Native Frame]{lang="EN-US"}]{#struct_0_73193_x1990_x1175841696}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[侧支持用户数据本地桥接、以]{lang="EN-US" style="font-family:宋体"}[802.11]{lang="EN-US"}[帧格式封装上传]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local Bridging & 802.3 Frame & Native Frame]{lang="EN-US"}]{#struct_0_73193_x1990_x307813170}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[侧支持用户数据本地桥接、以]{lang="EN-US" style="font-family:宋体"}[802.3]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[802.11]{lang="EN-US"}[帧格式封装上传]{lang="EN-US" style="font-family:宋体"}

[[Discovery type]{lang="EN-US"}]{#struct_0_73193_x1990_x558454200}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1605623780}[的发现方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static Configuration]{lang="EN-US"}]{#struct_0_73193_x1990_1580325519}[：]{lang="EN-US" style="font-family:
  宋体"}[AP]{lang="EN-US"}[使用静态配置的]{lang="EN-US" style="font-family:
  宋体"}[IPv4]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址发现]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_73193_x1990_x444088678}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[使用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项发现]{style="font-family:宋体"}[AC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNS]{lang="EN-US"}]{#struct_0_73193_x1990_1457968435}[：]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[使用]{lang="EN-US" style="font-family:宋体"}[DHCP+DNS]{lang="EN-US"}[发现]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_73193_x1990_1091815617}[：未知的发现方式]{lang="EN-US" style="font-family:宋体"}

[[Retransmission count]{lang="EN-US"}]{#struct_0_73193_x1990_x985942667}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_x703636461}[重传请求报文的重传次数]{style="font-family:宋体"}

[[Retransmission interval]{lang="EN-US"}]{#struct_0_73193_x1990_x108115506}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_x1321256986}[重传请求报文的重传间隔]{style="font-family:宋体"}

[[Firmware upgrade]{lang="EN-US"}]{#struct_0_73193_x1990_x84828823}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_781104513}[的版本下载：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_73193_x1990_1814133259}[：开启]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[的版本下载]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_73193_x1990_1813096250}[：关闭]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[的版本下载]{lang="EN-US" style="font-family:宋体"}

[[Sent control packets]{lang="EN-US"}]{#struct_0_73193_x1990_x1185092002}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_1994649314}[在]{style="font-family:宋体"}[Run]{lang="EN-US"}[状态之后发送的控制报文的个数（包含]{style="font-family:宋体"}[Change State Event Response]{lang="EN-US"}[报文）]{style="font-family:宋体"}

[[Received control packets]{lang="EN-US"}]{#struct_0_73193_x1990_248049318}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_1314780882}[在]{style="font-family:宋体"}[Run]{lang="EN-US"}[状态之后接收的控制报文的个数（包含]{style="font-family:宋体"}[Change State Event Request]{lang="EN-US"}[报文）]{style="font-family:宋体"}

[[Connection count]{lang="EN-US"}]{#struct_0_73193_x1990_678511185}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x410399189}[和]{style="font-family:宋体"}[AC]{lang="EN-US"}[的连接次数，只有在以下情况下连接次数会清零：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_678511182}[重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重新配置]{style="font-family:宋体"}]{#struct_0_73193_x1990_x410399196}[AP]{lang="EN-US"}[序列号]{style="font-family:宋体"}

[[需要注意的是，使用]{style="font-family:宋体"}[reset wlan ap]{lang="EN-US"}]{#struct_0_73193_x1990_420086402}[命令不会造成]{style="font-family:宋体"}[AP]{lang="EN-US"}[连接次数清零]{style="font-family:宋体"}

[[Basic BSSID]{lang="EN-US"}]{#struct_0_73193_x1990_x533677415}

[[Radio]{lang="EN-US"}]{#struct_0_73193_x1990_1040300706}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[还未与]{style="font-family:宋体"}[AC]{lang="EN-US"}[建立]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Admin state]{lang="EN-US"}]{#struct_0_73193_x1990_1040300704}

[[Radio]{lang="EN-US"}]{#struct_0_73193_x1990_1040300701}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_73193_x1990_1040300699}[[：]{style="font-size:10.5pt;font-family:宋体"}]{.MsoCommentReference}[Radio]{lang="EN-US"}[处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_73193_x1990_1040300697}[[：]{style="font-size:10.5pt;font-family:宋体"}]{.MsoCommentReference}[Radio]{lang="EN-US"}[处于关闭状态]{style="font-family:宋体"}

[[Wireless mode]{lang="EN-US"}]{#struct_0_73193_x1990_x916014430}

[[Radio]{lang="EN-US"}]{#struct_0_73193_x1990_x916014432}[类型：]{style="font-family:宋体"}[802.11a]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[（]{style="font-family:宋体"}[5GHz]{lang="EN-US"}[）、]{style="font-family:宋体"}[802.11b]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11g]{lang="EN-US"}[、]{style="font-family:宋体"}[802.11n]{lang="EN-US"}[（]{style="font-family:宋体"}[2.4GHz]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Client dot11n-only]{lang="EN-US"}]{#struct_0_73193_x1990_1267208119}

[[仅允许]{style="font-family:宋体"}[802.11n]{lang="EN-US"}]{#struct_0_73193_x1990_1651683125}[及]{style="font-family:宋体"}[802.11ac]{lang="EN-US"}[客户端接入功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_73193_x1990_x298875822}[：兼容]{lang="EN-US" style="font-family:宋体"}[802.11a/b/g]{lang="EN-US"}[的无线客户端，同时还要接入]{lang="EN-US" style="font-family:宋体"}[802.11n]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[802.11ac]{lang="EN-US"}[的无线客户端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_73193_x1990_63545149}[：只有]{lang="EN-US" style="font-family:宋体"}[802.11n]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[802.11ac]{lang="EN-US"}[的无线客户端才能接入射频]{lang="EN-US" style="font-family:宋体"}

[[Channel band-width]{lang="EN-US"}]{#struct_0_73193_x1990_1396278396}

[[配置的带宽模式：]{style="font-family:宋体"}]{#struct_0_73193_x1990_1831711758}

[[5MHz]{lang="EN-US"}]{#struct_0_73193_x1990_104408705}[：工作带宽为]{style="font-family:宋体"}[5MHz]{lang="EN-US"}

[[10MHz]{lang="EN-US"}]{#struct_0_73193_x1990_x1354498862}[：工作带宽为]{style="font-family:宋体"}[10MHz]{lang="EN-US"}

[[20MHz]{lang="EN-US"}]{#struct_0_73193_x1990_664919802}[：工作带宽为]{style="font-family:宋体"}[20MHz]{lang="EN-US"}

[[20/40MHz]{lang="EN-US"}]{#struct_0_73193_x1990_x1461675236}[：工作带宽为]{style="font-family:宋体"}[20/40MHz]{lang="EN-US"}

[[80MHz]{lang="EN-US"}]{#struct_0_73193_x1990_x940948040}[：工作带宽为]{style="font-family:宋体"}[80MHz]{lang="EN-US"}

[[Secondary channel offset]{lang="EN-US"}]{#struct_0_73193_x1990_x474761593}

[[802.11n]{lang="EN-US"}]{#struct_0_73193_x1990_x1414621069}[射频模式中的辅信道信息：]{style="font-family:宋体"}

[[SCA]{lang="EN-US"}]{#struct_0_73193_x1990_602463302}[：]{style="font-family:宋体"}[Second Channel Above]{lang="EN-US"}[，表示射频当前工作在]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[带宽模式，并且辅信道高于主信道]{style="font-family:宋体"}

[[SCB]{lang="EN-US"}]{#struct_0_73193_x1990_x700812540}[：]{style="font-family:宋体"}[Second Channel Below]{lang="EN-US"}[，表示射频当前工作在]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[带宽模式，并且辅信道低于主信道]{style="font-family:宋体"}

[[SCN]{lang="EN-US"}]{#struct_0_73193_x1990_1314262286}[：表示射频未工作在]{style="font-family:宋体"}[40MHz]{lang="EN-US"}[带宽模式]{style="font-family:宋体"}

[[Short GI for 20MHz]{lang="EN-US"}]{#struct_0_73193_x1990_x599122903}

[[射频工作带宽为]{style="font-family:宋体"}[20MHz]{lang="EN-US"}]{#struct_0_73193_x1990_x1259651989}[时，对于]{style="font-family:宋体"}[Short GI]{lang="EN-US"}[的支持情况：]{style="font-family:宋体"}

[[Not supported]{lang="EN-US"}]{#struct_0_73193_x1990_x1058325173}[：射频不支持]{style="font-family:宋体"}[20MHz Short GI]{lang="EN-US"}

[[Supported]{lang="EN-US"}]{#struct_0_73193_x1990_x1875615348}[：射频支持]{style="font-family:宋体"}[20MHz Short GI]{lang="EN-US"}

[[Short GI for 40MHz]{lang="EN-US"}]{#struct_0_73193_x1990_x1121333735}

[[射频工作带宽为]{style="font-family:宋体"}[40MHz]{lang="EN-US"}]{#struct_0_73193_x1990_1670558182}[时，对于]{style="font-family:宋体"}[Short GI]{lang="EN-US"}[的支持情况：]{style="font-family:宋体"}

[[Not supported]{lang="EN-US"}]{#struct_0_73193_x1990_1472237459}[：射频不支持]{style="font-family:宋体"}[40MHz Short GI]{lang="EN-US"}

[[Supported]{lang="EN-US"}]{#struct_0_73193_x1990_x117081005}[：射频支持]{style="font-family:宋体"}[40MHz Short GI]{lang="EN-US"}

[[Operational HT MCS Set]{lang="EN-US"}]{#struct_0_73193_x1990_2073842709}

[[高吞吐操作]{style="font-family:宋体"}[MCS]{lang="EN-US"}]{#struct_0_73193_x1990_161616052}[集：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_73193_x1990_x48167673}[：支持]{lang="EN-US" style="font-family:宋体"}[MCS]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Mandatory]{lang="EN-US"}]{#struct_0_73193_x1990_x1099254265}[：强制]{lang="EN-US" style="font-family:宋体"}[MCS]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[A-MSDU]{lang="EN-US"}]{#struct_0_73193_x1990_507758768}

[[A-MSDU]{lang="EN-US"}]{#struct_0_73193_x1990_1090939751}[功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_73193_x1990_1412972056}[：]{lang="EN-US" style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}[处于关闭状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_73193_x1990_x2127940444}[：]{lang="EN-US" style="font-family:宋体"}[A-MSDU]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}[处于开启状态]{style="font-family:宋体"}

[[A-MPDU]{lang="EN-US"}]{#struct_0_73193_x1990_1267273655}

[[A-MPDU]{lang="EN-US"}]{#struct_0_73193_x1990_x1504136734}[功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_73193_x1990_x8716030}[：]{lang="EN-US" style="font-family:宋体"}[A-MPDU]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}[处于关闭状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_73193_x1990_466829676}[：]{lang="EN-US" style="font-family:宋体"}[A-MPDU]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}[处于开启状态]{style="font-family:宋体"}

[[Channel]{lang="EN-US"}]{#struct_0_73193_x1990_x916014434}

[[Radio]{lang="EN-US"}]{#struct_0_73193_x1990_x916014435}[信道：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto\<*Number*\>]{lang="EN-US"}]{#struct_0_73193_x1990_x916014437}[：表示自动信道模式根据实际环境自动选择最优信道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Number]{lang="EN-US"}*]{#struct_0_73193_x1990_x916014439}[：手动配置的工作信道]{style="font-family:宋体"}

[[Maximum power]{lang="EN-US"}]{#struct_0_73193_x1990_657963681}

[[Radio]{lang="EN-US"}]{#struct_0_73193_x1990_657963679}[的最大传输功率]{style="font-family:宋体"}

[[Preamble type]{lang="EN-US"}]{#struct_0_73193_x1990_657963677}

[[前导码类型：]{style="font-family:宋体"}]{#struct_0_73193_x1990_657963675}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Long]{lang="EN-US"}]{#struct_0_73193_x1990_657963673}[：长和短前导码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Short]{lang="EN-US"}]{#struct_0_73193_x1990_x1298351455}[：短前导码]{style="font-family:宋体"}

[[Operational rate]{lang="EN-US"}]{#struct_0_73193_x1990_x1298351457}

[[操作速率：]{style="font-family:宋体"}]{#struct_0_73193_x1990_x1298351460}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Mandatory]{lang="EN-US"}]{#struct_0_73193_x1990_1676683257}[：强制速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_73193_x1990_1418312354}[：支持速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multicast]{lang="EN-US"}]{#struct_0_73193_x1990_1418312352}[：]{lang="EN-US" style="font-family:宋体"}[组]{style="font-family:宋体"}[播速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_73193_x1990_1418312350}[：禁止速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not configured]{lang="EN-US"}]{#struct_0_73193_x1990_1418312347}[：]{lang="EN-US" style="font-family:宋体"}[未指定速率]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1629937641}[显示所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[上的]{style="font-family:宋体"}[radio]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan ap all radio]{lang="EN-US"}]{#struct_0_73193_x1990_678511183}

[Total number of APs                       : 3]{lang="EN-US"}

[Total number of connected APs             : 1]{lang="EN-US"}

[Total number of connected auto APs        : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[AP                    Radio ID             Channel           Tx power (dBm)]{lang="EN-US"}

[ap1                   1                    161               79]{lang="EN-US"}

[ap1                   2                    3                 100]{lang="EN-US"}

[ap2                   1                    157               79]{lang="EN-US"}

[ap2                   2                    11                100]{lang="EN-US"}

[ap3                   1                    161               79]{lang="EN-US"}

[ap3                   2                    5                 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x410399195}[显示]{style="font-family:宋体"}[ap1]{lang="EN-US"}[上的]{style="font-family:宋体"}[radio]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan ap name ap1 radio]{lang="EN-US"}]{#struct_0_73193_x1990_420020866}

[AP                    Radio ID             Channel          Tx power (dBm)]{lang="EN-US"}

[ap1                   1                    161              79]{lang="EN-US"}

[ap1                   2                    3                100]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display wlan ap name]{lang="EN-US"}]{#struct_0_73193_x1990_x1482116089}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1819679896}[[字段]{style="font-family:黑体"}]{#struct_0_73193_x1990_1867989590}

[[描述]{style="font-family:黑体"}]{#struct_0_73193_x1990_x22994319}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1867989591}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x23059855}[名称]{style="font-family:宋体"}

[[Radio ID]{lang="EN-US"}]{#struct_0_73193_x1990_x2049603759}

[[射频的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_73193_x1990_1867989588}[号]{style="font-family:宋体"}

[[Channel]{lang="EN-US"}]{#struct_0_73193_x1990_x23518608}

[[射频使用的工作信道]{style="font-family:宋体"}]{#struct_0_73193_x1990_469760210}

[[Tx power (dBm)]{lang="EN-US"}]{#struct_0_73193_x1990_1867989589}

[[射频的发送功率（缺省为最大功率）]{style="font-family:宋体"}]{#struct_0_73193_x1990_x23584144}

[ ]{lang="EN-US"}

::: {#-515331716 .myid}
[]{#_Toc404794812}[]{#struct_0_73193_x1990_x604961604}

**AP管理 \-- AP管理配置命令 \-- display wlan ap reboot-log**

------------------------------------------------------------------------

[**[display wlan ap reboot-log]{lang="EN-US"}**]{#struct_0_73193_x1990_x1608620447}[命令用来显示指定]{style="font-family:
宋体"}[AP]{lang="EN-US"}[的重启日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1850506586}

[**[display wlan ap reboot-log name]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_73193_x1990_x1224972076}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1649471380}

[[任意视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_x1318034623}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_753752508}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_809939970}

[[network-operator]{lang="EN-US"}]{#struct_0_73193_x1990_x326215388}

[[mdc -admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1553489187}

[[mdc -operator]{lang="EN-US"}]{#struct_0_73193_x1990_52733800}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_556016841}

[**[name]{lang="EN-US"}***[ ap-name]{lang="EN-US"}*]{#struct_0_73193_x1990_1296211407}[：]{style="font-family:宋体"}[指定重启的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_2007295060}

[[如果]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1782079016}[曾发生过系统崩溃，那么可以使用该命令查看相关信息，注意指定的]{style="font-family:宋体"}[AP]{lang="EN-US"}[必须处于]{style="font-family:宋体"}[Run]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x301119691}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1410848732}[显示名为]{style="font-family:宋体"}[ap1]{lang="EN-US"}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的重启日志信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan ap reboot-log name ap1]{lang="EN-US"}]{#struct_0_73193_x1990_2029431030}

[Debugging information is not available on the AC.]{lang="EN-US"}

[Downloading debugging data from AP. Continue? \[Y/N\]:y]{lang="EN-US"}

[Downloading debugging data. Please wait\...]{lang="EN-US"}

[Please enter the same command again to view the log messages.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x214786943}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset wlan ap reboot-log]{lang="EN-US"}**]{#struct_0_73193_x1990_x1188774926}
:::

::: {#1724885851 .myid}
[]{#_Toc404794813}[]{#struct_0_73193_x1990_x603331491}[]{#_Toc393205673}

**AP管理 \-- AP管理配置命令 \-- display wlan ap-group**

------------------------------------------------------------------------

[**[display wlan ap-group]{lang="EN-US"}**]{#struct_0_73193_x1990_x720935502}[命令用来显示]{style="font-family:宋体"}[AP [Group]{style="color:black"}]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_500933611}

[**[display wlan ap-group]{lang="EN-US"}**[ [\[ ]{style="color:black"}*group-name* [\]]{style="color:black"}]{lang="EN-US"}]{#struct_0_73193_x1990_458816576}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_580954386}

[[任意视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_930389682}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x235328590}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_439584531}

[[network-operator]{lang="EN-US"}]{#struct_0_73193_x1990_1925685268}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_1579865543}

[[mdc-operator]{lang="EN-US"}]{#struct_0_73193_x1990_x1891724845}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_2125551864}

[*[group-name]{lang="EN-US"}*]{#struct_0_73193_x1990_1466276895}[：显示指定的]{style="font-family:宋体"}[AP]{lang="EN-US"}[组信息。如果未指定本参数，表示显示所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[组信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1087115175}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_2032848081}[显示全部]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的信息。]{style="font-family:宋体"}

[[\[System\] display wlan ap-group]{lang="EN-US"}]{#struct_0_73193_x1990_1091480690}

[AP group name       : default-group]{lang="EN-US"}

[Description         : Not configured]{lang="EN-US"}

[AP model            : Not configured]{lang="EN-US"}

[APs                 : Not configured]{lang="EN-US"}

[ ]{lang="EN-US"}

[AP group name       : group1]{lang="EN-US"}

[Description         : abcd]{lang="EN-US"}

[AP model            : WA2620i-AGN]{lang="EN-US"}

[AP grouping rules:]{lang="EN-US"}

[  AP name           : ap1, ap2]{lang="EN-US"}

[  Serial ID         : 123456789, 2345678]{lang="EN-US"}

[  MAC address       : 0012-2233-4455, 1112-3344-5566]{lang="EN-US"}

[APs                 : ap1 (AP name)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x597862352}[显示指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的信息。]{style="font-family:宋体"}

[[\[System\] display wlan ap-group group1]{lang="EN-US"}]{#struct_0_73193_x1990_x696035274}

[AP group name       : group1]{lang="EN-US"}

[Description         : Not configured]{lang="EN-US"}

[AP model            : WA2620i-AGN]{lang="EN-US"}

[AP grouping rules:]{lang="EN-US"}

[  AP name           : ap1, ap2]{lang="EN-US"}

[  Serial ID         : 123456789, 2345678]{lang="EN-US"}

[  MAC address       : 0012-2233-4455, 1112-3344-5566]{lang="EN-US"}

[APs                 : ap1 (AP name)]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display wlan ap-group]{lang="EN-US"}]{#struct_0_73193_x1990_x1083776577}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1667003066}[[字段]{style="font-family:黑体"}]{#struct_0_73193_x1990_x152992797}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_73193_x1990_1022036417}

[[AP group name  ]{lang="EN-US"}]{#struct_0_73193_x1990_1801341609}

[[组名]{style="font-family:宋体"}]{#struct_0_73193_x1990_x1221551960}

[[AP grouping rules]{lang="EN-US"}]{#struct_0_73193_x1990_x1719076738}

[[入组规则]{style="font-family:宋体"}]{#struct_0_73193_x1990_x1034800177}

[[AP model]{lang="EN-US"}]{#struct_0_73193_x1990_354435265}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1846914633}[型号名]{style="font-family:宋体"}

[[AP name]{lang="EN-US"}]{#struct_0_73193_x1990_203172027}

[[入组规则：]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1635059840}[名字列表]{style="font-family:宋体"}

[[Serial ID]{lang="EN-US"}]{#struct_0_73193_x1990_1767130459}

[[入组规则：]{style="font-family:宋体"}[AP ]{lang="EN-US"}]{#struct_0_73193_x1990_x1217965137}[序列号列表]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_73193_x1990_326123430}

[[入组规则：]{style="font-family:宋体"}[AP MAC]{lang="EN-US"}]{#struct_0_73193_x1990_x1362911914}[地址列表]{style="font-family:宋体"}

[[APs]{lang="EN-US"}]{#struct_0_73193_x1990_x988341499}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1358084397}[组中的]{style="font-family:宋体"}[AP]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_856642204}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wlan ap-group]{lang="EN-US"}**]{#struct_0_73193_x1990_79648290}

::: {#-1061803161 .myid}
[]{#_Toc404794814}[]{#struct_0_73193_x1990_x1552606510}[]{#_Toc403999219}[]{#_Toc403999220}[]{#_Toc403999221}[]{#_Toc403999222}[]{#_Toc403999223}[]{#_Toc403999224}[]{#_Toc403999225}[]{#_Toc403999226}[]{#_Toc403999227}[]{#_Toc403999228}[]{#_Toc403999229}[]{#_Toc403999230}[]{#_Toc403999231}[]{#_Toc403999232}[]{#_Toc403999233}[]{#_Toc403999234}[]{#_Toc403999235}[]{#_Toc403999236}[]{#_Toc403999237}[]{#_Toc403999238}[]{#_Toc403999239}[]{#_Toc403999240}[]{#_Toc403999241}[]{#_Toc403999242}[]{#_Toc403999243}[]{#_Toc403999244}[]{#_Toc403999245}[]{#_Toc403999246}[]{#_Toc403999247}[]{#_Toc403999248}[]{#_Toc403999276}

**AP管理 \-- AP管理配置命令 \-- echo-interval**

------------------------------------------------------------------------

[**[echo-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_763836558}[命令用来设置两次回声请求的时间间隔。]{style="font-family:宋体"}

[**[undo echo-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_x2021280716}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1939993773}

[**[echo-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_73193_x1990_x1320384366}

[**[undo echo-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_2092657307}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x155235209}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_923839200}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_2032520401}[组视图：]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送回声请求的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1415570308}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x2130223216}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x358175456}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x283071748}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x611469155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_711131870}

[*[interval]{lang="EN-US"}*]{#struct_0_73193_x1990_x1037332458}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送两次回声请求之间的时间间隔，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x713530801}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x367799683}[和]{style="font-family:宋体"}[AC]{lang="EN-US"}[之间通过保活机制来检查控制隧道是否正常工作。]{style="font-family:宋体"}[AP]{lang="EN-US"}[周期性地向]{style="font-family:宋体"}[AC]{lang="EN-US"}[发送回声请求]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文，若一定时间内没有收到]{style="font-family:宋体"}[AC]{lang="EN-US"}[回复的]{style="font-family:宋体"}[Echo response]{lang="EN-US"}[报文，则]{style="font-family:宋体"}[AP]{lang="EN-US"}[断开控制隧道；若]{style="font-family:宋体"}[AC]{lang="EN-US"}[在一定时间内没有收到]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文，则]{style="font-family:宋体"}[AC]{lang="EN-US"}[断开控制隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1721319150}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1692922259}[设置]{style="font-family:宋体"}[ap3]{lang="EN-US"}[向]{style="font-family:宋体"}[AC]{lang="EN-US"}[发送的回声请求时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_x1918341550}

[\[Sysname\] wlan ap ap3 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap3\] echo-interval 15]{lang="EN-US"}
:::

::: {#-215738606 .myid}
[]{#_Toc404794815}[]{#struct_0_73193_x1990_609727201}

**AP管理 \-- AP管理配置命令 \-- firmware-upgrade enable**

------------------------------------------------------------------------

[**[firmware-upgrade enable]{lang="EN-US"}**]{#struct_0_73193_x1990_x571649615}[命令用来开启]{style="font-family:宋体"}[AP]{lang="EN-US"}[版本下载功能。]{style="font-family:宋体"}

[**[firmware-upgrade disable]{lang="EN-US"}**]{#struct_0_73193_x1990_1036773710}[命令用来关闭]{style="font-family:
宋体"}[AP]{lang="EN-US"}[版本下载功能。]{style="font-family:宋体"}

[**[undo firmware-upgrade]{lang="EN-US"}**]{#struct_0_73193_x1990_x1110865578}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x183692957}

[**[firmware-upgrade]{lang="EN-US"}**[ { **disable** \| **enable** }]{lang="EN-US"}]{#struct_0_73193_x1990_2091604985}

[**[undo firmware-upgrade]{lang="EN-US"}**]{#struct_0_73193_x1990_x1740431662}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1741875803}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1007564205}[视图：开启]{style="font-family:宋体"}[AP]{lang="EN-US"}[版本下载功能。]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x696362954}[组视图：未开启]{style="font-family:宋体"}[AP]{lang="EN-US"}[版本下载功能。]{style="font-family:宋体"}

[[全局配置视图：]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x947372888}[版本下载功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1323108941}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1280955865}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组视图]{style="font-family:宋体"}[/]{lang="EN-US"}[全局配置视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1949523291}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x981152095}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_1910790954}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1873085641}

[**[disable]{lang="EN-US"}**]{#struct_0_73193_x1990_104539777}[：]{style="font-family:宋体"}[关闭]{style="font-family:宋体"}[AP]{lang="EN-US"}[版本下载功能。]{style="font-family:宋体"}

[**[enable]{lang="EN-US"}**]{#struct_0_73193_x1990_1455067868}[：开启]{style="font-family:宋体"}[AP]{lang="EN-US"}[版本下载功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1922196190}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建立]{style="font-family:宋体"}]{#struct_0_73193_x1990_x1242206344}[CAPWAP]{lang="EN-US"}[隧道过程中，如果开启]{style="font-family:宋体"}[AP]{lang="EN-US"}[版本下载功能，且]{style="font-family:宋体"}[AP]{lang="EN-US"}[的固件版本低于]{style="font-family:宋体"}[AC]{lang="EN-US"}[的固件版本时，则]{style="font-family:宋体"}[AP]{lang="EN-US"}[必须从]{style="font-family:宋体"}[AC]{lang="EN-US"}[上下载对应的固件版本文件后才能与]{style="font-family:宋体"}[AC]{lang="EN-US"}[建立]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建立]{style="font-family:宋体"}]{#struct_0_73193_x1990_x558519736}[CAPWAP]{lang="EN-US"}[隧道过程中，如果关闭]{style="font-family:宋体"}[AP]{lang="EN-US"}[版本下载功能，则不比较]{style="font-family:宋体"}[AP]{lang="EN-US"}[当前的固件版本和]{style="font-family:宋体"}[AC]{lang="EN-US"}[的固件版本，直接与]{style="font-family:宋体"}[AC]{lang="EN-US"}[建立]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x87481689}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x1388069204}[开启]{style="font-family:宋体"}[ap3]{lang="EN-US"}[的版本下载功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_73193_x1990_x977742840}

[\[Sysname\] wlan ap ap3 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap3\] firmware-upgrade enable]{lang="EN-US"}
:::

::: {#524738056 .myid}
[]{#_Toc404794816}[]{#struct_0_73193_x1990_175172564}

**AP管理 \-- AP管理配置命令 \-- jumboframe enable**

------------------------------------------------------------------------

[**[jumboframe enable]{lang="EN-US"}**]{#struct_0_73193_x1990_x809443932}[命令用来开启]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧传输功能并设置]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧的最大长度。]{style="font-family:宋体"}

[**[undo jumboframe enable]{lang="EN-US"}**]{#struct_0_73193_x1990_x1409450808}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1786343443}

[**[jumboframe enable]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_73193_x1990_201458429}

[**[undo jumboframe enable]{lang="EN-US"}**]{#struct_0_73193_x1990_x1078080726}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1457902899}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1862744765}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_869720987}[组视图：未开启]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧的传输功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x649124387}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_664026710}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_50650887}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x2023711053}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x227256238}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x938469507}

[*[value]{lang="EN-US"}*]{#struct_0_73193_x1990_1360728784}[：指定]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧的最大长度，取值范围为]{style="font-family:宋体"}[1500]{lang="EN-US"}[～]{style="font-family:宋体"}[1748]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x914116981}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Jumbo]{lang="EN-US"}]{#struct_0_73193_x1990_x741164216}[帧即超长帧，在进行文件传输等大吞吐量数据的时候，]{style="font-family:宋体"}[AP]{lang="EN-US"}[收到帧的长度可能大于标准以太网帧的长度，通过配置此命令允许不超过指定长度的超长帧通过。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若]{style="font-family:宋体"}]{#struct_0_73193_x1990_1367948893}[AP]{lang="EN-US"}[收到的帧长度大于配置的]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧的最大长度，则]{style="font-family:宋体"}[AP]{lang="EN-US"}[会使用配置的]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧长度对该帧进行分片。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x108181042}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x937335434}[设置]{style="font-family:宋体"}[Jumbo]{lang="EN-US"}[帧的长度为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_831626030}

[\[Sysname\] wlan ap ap1 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-ap-ap1\] jumboframe enable 1500]{lang="EN-US"}
:::

::: {#-636046328 .myid}
[]{#_Toc404794817}[]{#struct_0_73193_x1990_x1859162368}[]{#_Toc393205676}

**AP管理 \-- AP管理配置命令 \-- mac-address**

------------------------------------------------------------------------

[**[mac-address]{lang="EN-US"}**]{#struct_0_73193_x1990_x311053400}[命令用来配置]{style="font-family:宋体"}[AP MAC ]{lang="EN-US"}[地址入组规则。]{style="font-family:宋体"}

[**[undo mac-address]{lang="EN-US"}**]{#struct_0_73193_x1990_830895080}[命令用来删除]{style="font-family:宋体"}[AP MAC ]{lang="EN-US"}[地址入组规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_2036154010}

[**[mac-address]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_73193_x1990_x1056754228}

[**[undo mac-address]{lang="EN-US"}**[ *mac-address* ]{lang="EN-US"}]{#struct_0_73193_x1990_x109593283}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x939950928}

[[未配置]{style="font-family:宋体"}[AP MAC]{lang="EN-US"}]{#struct_0_73193_x1990_2132927222}[地址入组规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1324263806}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1722061299}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1893509235}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_1392721558}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_2069291958}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1601193055}

[*[mac-address]{lang="EN-US"}*]{#struct_0_73193_x1990_1807637316}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，形式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_63151933}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_111318705}[组下]{lang="EN-US" style="font-family:宋体"}[AP MAC]{lang="EN-US"}[地址可配置多个。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_13990310}[名字如入规则的优先级高于序列号入组规则，序列号入组规则的优先级高于]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址入组规则。]{style="font-family:宋体"}[AP]{lang="EN-US"}[优先根据]{style="font-family:宋体"}[AP]{lang="EN-US"}[名字入组规则匹配入组，其次是]{style="font-family:宋体"}[AP]{lang="EN-US"}[序列号入组规则，最后是]{style="font-family:宋体"}[AP MAC ]{lang="EN-US"}[地址入组规则，若为匹配到任何入组规则，则]{style="font-family:宋体"}[AP]{lang="EN-US"}[将被加入到默认组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若其它组已经存在该]{style="font-family:宋体"}]{#struct_0_73193_x1990_x1939024811}[MAC]{lang="EN-US"}[地址入组规则，在新组配置该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址入组规则，则原]{style="font-family:宋体"}[AP]{lang="EN-US"}[组将删除该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址入组规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[默认组视图下不能进行该配置。]{style="font-family:宋体"}]{#struct_0_73193_x1990_894798568}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_39649453}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1465092813}[在]{style="font-family:宋体"}[AP]{lang="EN-US"}[组视图下添加]{style="font-family:宋体"}[AP MAC]{lang="EN-US"}[地址入组规则]{style="font-family:宋体"}[0AC1-F9B2-B1C2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<System\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_x744014591}

[\[System\] wlan ap-group group1 ]{lang="EN-US"}

[\[System-wlan-ap-group-group1\] mac-address 0AC1-F9B2-B1C2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x441238026}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wlan]{lang="EN-US"}**]{#struct_0_73193_x1990_x262097534}**[ ]{lang="EN-US"}[ap-group]{lang="EN-US"}**
:::

::: {#567732879 .myid}
[]{#_Toc404794818}[]{#struct_0_73193_x1990_x363454736}[]{#_Toc340836280}

**AP管理 \-- AP管理配置命令 \-- priority**

------------------------------------------------------------------------

[**[priority]{lang="EN-US"}**]{#struct_0_73193_x1990_x321457231}[命令用来配置]{style="font-family:宋体"}[AC]{lang="EN-US"}[上]{style="font-family:宋体"}[AP]{lang="EN-US"}[连接的优先级。]{style="font-family:宋体"}

[**[undo priority]{lang="EN-US"}**]{#struct_0_73193_x1990_1554353342}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1698773146}

[**[priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_73193_x1990_x2001895509}

[**[undo priority]{lang="EN-US"}**]{#struct_0_73193_x1990_x272507805}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x733066905}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_134674552}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x2085138274}[组视图：]{style="font-family:宋体"}[AP]{lang="EN-US"}[连接的优先级为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x2099229872}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1272423892}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1240312101}

[[network-admin ]{lang="EN-US"}]{#struct_0_73193_x1990_x78947645}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x358928860}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1170958400}

[*[priority]{lang="EN-US"}*]{#struct_0_73193_x1990_308435346}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[连接的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。该数值越大，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_570489326}

[[建立]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}]{#struct_0_73193_x1990_547855584}[隧道的过程中，]{style="font-family:宋体"}[AP]{lang="EN-US"}[会优先选择优先级高的]{style="font-family:宋体"}[AC]{lang="EN-US"}[建立隧道连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x2133753283}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1371429403}[配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[连接的优先级为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_x533145931}

[\[Sysname\] wlan ap ap3 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap3\] priority 255]{lang="EN-US"}
:::

::: {#-1477709035 .myid}
[]{#_Toc404794819}[]{#struct_0_73193_x1990_708877065}

**AP管理 \-- AP管理配置命令 \-- reset wlan ap**

------------------------------------------------------------------------

[**[reset wlan ap]{lang="EN-US"}**]{#struct_0_73193_x1990_x2045747932}[命令用来重启]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_369993631}

[**[reset wlan ap]{lang="EN-US"}**[ { **all** \| **name** *ap-name* }]{lang="EN-US"}]{#struct_0_73193_x1990_x15189928}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1244847278}

[[用户视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_x112053705}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1134201880}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_187017014}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1556990740}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1984824501}

[**[all]{lang="EN-US"}**]{#struct_0_73193_x1990_1032938010}[：重启连接到当前]{style="font-family:宋体"}[AC]{lang="EN-US"}[的所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ap-name]{lang="EN-US"}*]{#struct_0_73193_x1990_1093843149}[：指定重启]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1874003496}

[[当]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_73193_x1990_x1526671816}[要断开与]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道连接时，输入此命令，]{style="font-family:宋体"}[AP]{lang="EN-US"}[重启，]{style="font-family:宋体"}[AC]{lang="EN-US"}[端与]{style="font-family:宋体"}[AP]{lang="EN-US"}[相关的连接资源将被清除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x939025155}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x146761053}[重启]{style="font-family:宋体"}[ap1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset wlan ap name ap1]{lang="EN-US"}]{#struct_0_73193_x1990_x2086762999}

[Reset the AP that has established or is to establish a primary tunnel with the AC. Continue? \[Y/N\]:]{lang="EN-US"}
:::

::: {#-606954986 .myid}
[]{#_Toc404794820}[]{#struct_0_73193_x1990_589291279}

**AP管理 \-- AP管理配置命令 \-- reset wlan ap reboot-log**

------------------------------------------------------------------------

[**[reset wlan ap reboot-log]{lang="EN-US"}**]{#struct_0_73193_x1990_579820901}[命令用来清除指定]{style="font-family:
宋体"}[AP]{lang="EN-US"}[或全部]{style="font-family:宋体"}[AP]{lang="EN-US"}[的重启日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_987901560}

[**[reset wlan ap reboot-log]{lang="EN-US"}**[ { **all** \| **name** *ap-name* }]{lang="EN-US"}]{#struct_0_73193_x1990_1812115552}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1695945345}

[[用户视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_160211834}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1924609882}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1913766744}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x952535938}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_803973986}

[**[all]{lang="EN-US"}**]{#struct_0_73193_x1990_1813012184}[：清除所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[的重启日志信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ ap-name]{lang="EN-US"}*]{#struct_0_73193_x1990_x1189602329}[：清除指定名称的]{style="font-family:宋体"}[AP]{lang="EN-US"}[的重启日志信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_2051064069}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x1360247254}[清除]{style="font-family:宋体"}[ap1]{lang="EN-US"}[的重启日志信息。]{style="font-family:宋体"}

[[\<Sysname\> reset wlan ap reboot-log name ap1]{lang="EN-US"}]{#struct_0_73193_x1990_x251447483}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x129861404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display wlan ap reboot-log]{lang="EN-US"}**]{#struct_0_73193_x1990_x1186957705}
:::

::: {#12061890 .myid}
[]{#_Toc404794821}[]{#struct_0_73193_x1990_1371227123}

**AP管理 \-- AP管理配置命令 \-- retransmit-count**

------------------------------------------------------------------------

[**[retransmit-count]{lang="EN-US"}**]{#struct_0_73193_x1990_x1240499122}[命令用来设置]{style="font-family:宋体"}[AC]{lang="EN-US"}[发送给]{style="font-family:宋体"}[AP]{lang="EN-US"}[的请求报文重传次数。]{style="font-family:宋体"}

[**[undo retransmit-count]{lang="EN-US"}**]{#struct_0_73193_x1990_1631547597}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1859078483}

[**[retransmit-count]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_73193_x1990_414934179}

[**[undo retransmit-count]{lang="EN-US"}**]{#struct_0_73193_x1990_861643606}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1995176067}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1112987317}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1099647481}[组视图：请求报文重传次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1954314394}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_648106689}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1436222537}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_960691856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1006704712}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1306626060}

[*[value]{lang="EN-US"}*]{#struct_0_73193_x1990_1063849176}[：]{style="font-family:宋体"}[指定请求报文重传次数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x315678068}

[[为了使]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_73193_x1990_2079225785}[的请求报文尽可能的发送到]{style="font-family:宋体"}[AP]{lang="EN-US"}[，提高报文的可靠传输能力，]{style="font-family:宋体"}[AC]{lang="EN-US"}[会对请求报文进行重传。]{style="font-family:宋体"}

[[重传次数为配置的请求报文重传次数。]{style="font-family:宋体"}]{#struct_0_73193_x1990_x1031436771}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_1234704126}[发送给]{style="font-family:宋体"}[AP]{lang="EN-US"}[的请求报文包括]{style="font-family:宋体"}[Image Data Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Configuration Update Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Reset Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Data Transfer Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[IEEE 802.11 WLAN Configuration Request]{lang="EN-US"}[报文和]{style="font-family:宋体"}[Station Configuration Request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1116418411}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x1828411016}[配置]{style="font-family:宋体"}[AC]{lang="EN-US"}[发往]{style="font-family:宋体"}[ap3]{lang="EN-US"}[的请求报文重传次数为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_73193_x1990_x1292660818}

[\[Sysname\] wlan ap ap3 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap3\] retransmit-count 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1368768127}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[retransmit-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_1862920911}
:::

::: {#-1720057218 .myid}
[]{#_Toc404794822}[]{#struct_0_73193_x1990_175723174}

**AP管理 \-- AP管理配置命令 \-- retransmit-interval**

------------------------------------------------------------------------

[**[retransmit-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_x785993541}[命令用来设置请求报文重传的时间间隔。]{style="font-family:宋体"}

[**[undo retransmit-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_x1601646417}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_45726173}

[**[retransmit-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_73193_x1990_x1052677196}

[**[undo retransmit-interva]{lang="EN-US"}**[l]{lang="EN-US"}]{#struct_0_73193_x1990_x405467938}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_516116276}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1911106521}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_466436460}[组视图：请求报文重传的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x112267718}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_273423123}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1547867069}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x765002804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1077671531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1276977820}

[*[interval]{lang="EN-US"}*]{#struct_0_73193_x1990_2073706739}[：]{style="font-family:宋体"}[指定请求报文重传的时间间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[，单位为秒。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1800150006}

[[为了使]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_73193_x1990_x1540394156}[的请求报文尽可能的发送到]{style="font-family:宋体"}[AP]{lang="EN-US"}[，提高报文的可靠传输能力，]{style="font-family:宋体"}[AC]{lang="EN-US"}[会对请求报文进行重传。]{style="font-family:宋体"}

[[重传时间间隔为配置的请求报文重传时间。]{style="font-family:宋体"}]{#struct_0_73193_x1990_2127907476}

[[AC]{lang="EN-US"}]{#struct_0_73193_x1990_1234310910}[发送给]{style="font-family:宋体"}[AP]{lang="EN-US"}[的请求报文包括]{style="font-family:宋体"}[Image Data Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Configuration Update Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Reset Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Data Transfer Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[IEEE 802.11 WLAN Configuration Request]{lang="EN-US"}[报文和]{style="font-family:宋体"}[Station Configuration Request]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1351332212}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x165659649}[设置]{style="font-family:宋体"}[AC]{lang="EN-US"}[发往]{style="font-family:宋体"}[ap3]{lang="EN-US"}[的请求报文重传的时间间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_73193_x1990_x1742999512}

[\[Sysname\] wlan ap ap3 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap3\] retransmit-interval 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1884342368}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[retransmit-count]{lang="EN-US"}**]{#struct_0_73193_x1990_x468742563}
:::

::: {#-784389225 .myid}
[]{#_Toc404794823}[]{#struct_0_73193_x1990_x1826223461}

**AP管理 \-- AP管理配置命令 \-- serial-id(AP view)**

------------------------------------------------------------------------

[**[serial-id]{lang="EN-US"}**]{#struct_0_73193_x1990_x313485072}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[的序列号。]{style="font-family:宋体"}

[**[undo serial-id]{lang="EN-US"}**]{#struct_0_73193_x1990_1037316211}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_516434953}

[**[serial-id]{lang="EN-US"}**[ *serial-id*]{lang="EN-US"}]{#struct_0_73193_x1990_102568625}

[**[undo serial-id]{lang="EN-US"}**]{#struct_0_73193_x1990_x309114269}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x305478843}

[[未配置]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x753494466}[的序列号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x176915571}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1096261456}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x614010067}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_863490486}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_1020419428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1490111697}

[*[serial-id]{lang="EN-US"}*]{#struct_0_73193_x1990_x850205716}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的序列号，序列号为每个]{style="font-family:宋体"}[AP]{lang="EN-US"}[的唯一标识，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1121561311}

[[如果]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_514762713}[已经与]{style="font-family:宋体"}[AC]{lang="EN-US"}[建立]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道连接，改变和删除序列号将触发]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道的拆除，]{style="font-family:宋体"}[AP]{lang="EN-US"}[将会重新发现]{style="font-family:宋体"}[AC]{lang="EN-US"}[并与]{style="font-family:宋体"}[AC]{lang="EN-US"}[建立]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1465445518}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x1164666290}[将]{style="font-family:宋体"}[ap1]{lang="EN-US"}[的序列号设置为]{style="font-family:宋体"}[210235A1BSC123000050]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_73193_x1990_x2099295408}

[\[Sysname\] wlan ap ap1 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-ap-ap1\] serial-id 210235A1BSC123000050]{lang="EN-US"}
:::

::: {#-1278350207 .myid}
[]{#_Toc404794824}[]{#struct_0_73193_x1990_x1052593314}[]{#_Toc393205675}

**AP管理 \-- AP管理配置命令 \-- serial-id(AP group view)**

------------------------------------------------------------------------

[**[serial-id]{lang="EN-US"}**]{#struct_0_73193_x1990_2048765616}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[序列号入组规则。]{style="font-family:宋体"}

[**[undo serial-id]{lang="EN-US"}**]{#struct_0_73193_x1990_x465512092}[命令用来删除]{style="font-family:宋体"}[AP]{lang="EN-US"}[序列号入组规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_802556516}

[**[serial-id]{lang="EN-US"}**[ *serial-id*]{lang="EN-US"}]{#struct_0_73193_x1990_x1459687599}

[**[undo serial-id]{lang="EN-US"}**[ *serial-id*]{lang="EN-US"}]{#struct_0_73193_x1990_x1543224217}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_413590658}

[[未配置]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1153952367}[序列号入组规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_462075885}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_1873527838}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_2032454865}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_1173632688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1998840317}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x940568392}

[*[serial-id]{lang="EN-US"}*]{#struct_0_73193_x1990_1483912720}[：]{style="font-family:宋体;color:black"}[AP]{lang="EN-US" style="color:black"}[序列号，]{style="font-family:宋体;color:black"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，输入后的字母自动改为大写形式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x346059501}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一]{style="font-family:宋体"}]{#struct_0_73193_x1990_1236412893}[AP]{lang="EN-US"}[组下]{style="font-family:宋体"}[AP]{lang="EN-US"}[序列号可配置多个。配置后符合该序列号的]{style="font-family:宋体"}[AP]{lang="EN-US"}[可以入组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_768146900}[名字如入规则的优先级高于序列号入组规则，序列号入组规则的优先级高于]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址入组规则。]{style="font-family:宋体"}[AP]{lang="EN-US"}[优先根据]{style="font-family:宋体"}[AP]{lang="EN-US"}[名字入组规则匹配入组，其次是]{style="font-family:宋体"}[AP]{lang="EN-US"}[序列号入组规则，最后是]{style="font-family:宋体"}[AP MAC ]{lang="EN-US"}[地址入组规则，若为匹配到任何入组规则，则]{style="font-family:宋体"}[AP]{lang="EN-US"}[将被加入到默认组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若其它组已经存在该序列号入组规则，在新组配置该序列号入组规则，则原]{style="font-family:宋体"}]{#struct_0_73193_x1990_452078794}[AP]{lang="EN-US"}[组将删除该序列号入组规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[默认组视图下不能进行该配置。]{style="font-family:宋体"}]{#struct_0_73193_x1990_1031908010}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1616427213}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x45975236}[在]{style="font-family:宋体"}[AP]{lang="EN-US"}[组视图下添加序列号入组规则]{style="font-family:宋体"}[serial-id SER123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<System\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_x1017640588}

[\[System\] wlan ap-group group1]{lang="EN-US"}

[\[System-wlan-ap-group-group1\] serial-id SERl123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1204282937}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wlan]{lang="EN-US"}**]{#struct_0_73193_x1990_407878891}[ ]{lang="EN-US"}**[ap-group]{lang="EN-US"}**
:::

::: {#365931513 .myid}
[]{#_Toc404794825}[]{#struct_0_73193_x1990_687696047}

**AP管理 \-- AP管理配置命令 \-- statistics-interval**

------------------------------------------------------------------------

[**[statistics-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_1965168682}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[向]{style="font-family:宋体"}[AC]{lang="EN-US"}[上报]{style="font-family:宋体"}[Radio]{lang="EN-US"}[统计信息的时间间隔。]{style="font-family:宋体"}

[**[undo statistics-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_999403213}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1020169472}

[**[statistics-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_73193_x1990_1479822647}

[**[undo statistics-interval]{lang="EN-US"}**]{#struct_0_73193_x1990_x1707532999}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1691478212}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x589253807}[视图：继承]{style="font-family:宋体"}[AP]{lang="EN-US"}[组配置。]{style="font-family:宋体"}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x696428490}[组视图：]{style="font-family:宋体"}[AP]{lang="EN-US"}[向]{style="font-family:宋体"}[AC]{lang="EN-US"}[上报]{style="font-family:宋体"}[Radio]{lang="EN-US"}[统计信息的时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1792946260}

[[AP]{lang="EN-US"}]{#struct_0_73193_x1990_579054776}[视图]{style="font-family:宋体"}[/AP]{lang="EN-US"}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x2006467410}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x533211467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x938054321}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1789398853}

[*[interval]{lang="EN-US"}*]{#struct_0_73193_x1990_445108927}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[向]{style="font-family:宋体"}[AC]{lang="EN-US"}[上报]{style="font-family:宋体"}[Radio]{lang="EN-US"}[统计信息的时间间隔，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1318371258}

[[为了对]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1457624559}[的运行情况进行有效监控，]{style="font-family:宋体"}[AP]{lang="EN-US"}[会周期性的向]{style="font-family:宋体"}[AC]{lang="EN-US"}[上报]{style="font-family:宋体"}[Radio]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x689180537}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_638862439}[设置]{style="font-family:宋体"}[ap1]{lang="EN-US"}[上报]{style="font-family:宋体"}[Radio]{lang="EN-US"}[统计信息的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_73193_x1990_x1257821396}

[\[Sysname\] wlan ap ap1 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\] statistics-interval 10]{lang="EN-US"}
:::

::: {#-1506845022 .myid}
[]{#_Toc404794826}[]{#struct_0_73193_x1990_x1080157386}

**AP管理 \-- AP管理配置命令 \-- wlan ap**

------------------------------------------------------------------------

[**[wlan ap]{lang="EN-US"}**]{#struct_0_73193_x1990_1032872474}[命令用来创建并进入]{style="font-family:宋体"}[AP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo wlan ap]{lang="EN-US"}**]{#struct_0_73193_x1990_1126825294}[命令用来删除指定的]{style="font-family:宋体"}[AP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_555472142}

[**[wlan ap ]{lang="EN-US"}***[ap-name ]{lang="EN-US"}*[\[ **model** *model-name* \]]{lang="EN-US"}]{#struct_0_73193_x1990_x1728864234}

[**[undo wlan ap]{lang="EN-US"}***[ ap-name ]{lang="EN-US"}*]{#struct_0_73193_x1990_x256864188}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_863707305}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_81240897}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_809582175}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_704315048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_696724025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_92747274}

[*[ap-name]{lang="EN-US"}*]{#struct_0_73193_x1990_1564634424}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[model]{lang="EN-US"}***[ model-name]{lang="EN-US"}*]{#struct_0_73193_x1990_x1696010881}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[的型号名称，在创建]{style="font-family:宋体"}[AP]{lang="EN-US"}[时，该参数必须配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1221607787}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wlan ap]{lang="EN-US"}**]{#struct_0_73193_x1990_1640725636}[命令用来创建并进入]{style="font-family:
宋体"}[AP]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[AP]{lang="EN-US"}[已创建，则该命令直接用来进入该]{style="font-family:宋体"}[AP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[undo wlan ap]{lang="EN-US"}**]{#struct_0_73193_x1990_1067488547}[命令用来删除指定的]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[，如果]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[已经与]{lang="EN-US" style="font-family:宋体"}[AC]{lang="EN-US"}[建立了]{lang="EN-US" style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[隧道连接，使用]{lang="EN-US" style="font-family:宋体"}**[undo wlan ap]{lang="EN-US"}**[命令将会导致连接断开。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_2016863648}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x1195271729}[创建]{style="font-family:宋体"}[ap1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_x720828918}

[\[Sysname\] wlan ap ap1 model WA4620i-AGN]{lang="EN-US"}

[\[Sysname-wlan-ap-ap1\]]{lang="EN-US"}
:::

::: {#1403743026 .myid}
[]{#_Toc404794827}[]{#struct_0_73193_x1990_x200243572}[]{#_Toc393383824}

**AP管理 \-- AP管理配置命令 \-- wlan apdb file**

------------------------------------------------------------------------

[**[wlan apdb file]{lang="EN-US"}**]{#struct_0_73193_x1990_x1851622370}[命令用来加载]{style="font-family:宋体"}[APDB]{lang="EN-US"}[用户脚本文件。]{style="font-family:宋体"}

[**[undo wlan apdb file]{lang="EN-US"}**]{#struct_0_73193_x1990_1324384604}[命令用来卸载]{style="font-family:宋体"}[APDB]{lang="EN-US"}[用户脚本文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1689936279}

[**[wlan apdb file ]{lang="EN-US"}***[user.apdb]{lang="EN-US"}*]{#struct_0_73193_x1990_1017995141}

[**[undo wlan apdb file]{lang="EN-US"}**]{#struct_0_73193_x1990_x415342125}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1766327513}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_170654293}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x745391599}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_736724382}

[[network-operator]{lang="EN-US"}]{#struct_0_73193_x1990_973969367}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_87205654}

[[mdc-operator]{lang="EN-US"}]{#struct_0_73193_x1990_x1611348202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1177682150}

[*[user.apdb]{lang="EN-US"}*]{#struct_0_73193_x1990_95952374}[：指定需要加载的]{style="font-family:宋体;color:black"}[APDB]{lang="EN-US" style="color:black"}[用户脚本文件名，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[63]{lang="EN-US" style="color:black"}[个字符的字符串，区分大小写。]{style="font-family:宋体;color:black"}[apdb]{lang="EN-US"}[为文件后缀。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x881475979}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用本命令加载用户脚本文件后，脚本文件中的]{style="font-family:宋体"}]{#struct_0_73193_x1990_174754806}[AP]{lang="EN-US"}[型号信息将被加载到]{style="font-family:宋体"}[APDB]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户脚本只能加载]{style="font-family:宋体"}]{#struct_0_73193_x1990_183691272}[]{#_GoBack}[一个，支持重复加载，当重复加载时，新脚本内容会替换旧脚本内容。若旧脚本中的某个]{style="font-family:宋体"}[AP]{lang="EN-US"}[型号已经加入]{style="font-family:宋体"}[AP]{lang="EN-US"}[组及全局配置，且该]{style="font-family:宋体"}[AP]{lang="EN-US"}[型号在新脚本中被删除或者有修改时则不允许替换操作，提示用户加载失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_2133785896}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_962555842}[加载名为]{style="font-family:宋体"}[user.apdb]{lang="EN-US"}[的用户脚本。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_1192162878}

[\[Sysname\] wlan apdb file user.apdb]{lang="EN-US"}
:::

::: {#-1482390212 .myid}
[]{#_Toc404794828}[]{#struct_0_73193_x1990_673738587}[]{#_Toc393205670}

**AP管理 \-- AP管理配置命令 \-- wlan ap-group**

------------------------------------------------------------------------

[**[wlan ap-group]{lang="EN-US"}**]{#struct_0_73193_x1990_x2085441550}[命令用来创建一个]{style="font-family:宋体"}[AP]{lang="EN-US"}[组并进入]{style="font-family:宋体"}[AP]{lang="EN-US"}[组视图。]{style="font-family:宋体"}

[**[undo wlan ap-group]{lang="EN-US"}**]{#struct_0_73193_x1990_x2019180955}[命令用来删除一个]{style="font-family:宋体"}[AP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x2102028334}

[**[wlan ap-group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_73193_x1990_x1204960217}

[**[undo wlan ap-group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_73193_x1990_x445890684}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1051922906}

[[存在默认组]{style="font-family:宋体"}[default-group]{lang="EN-US"}]{#struct_0_73193_x1990_238107316}[，不允许删除。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1666709084}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_1355096885}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x603528099}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_439129633}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1366872795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1539759040}

[*[group-name]{lang="EN-US"}*]{#struct_0_73193_x1990_x203995918}[：]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1531263183}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最多可配置]{lang="EN-US" style="font-family:宋体"}[128]{lang="EN-US"}]{#struct_0_73193_x1990_1168345583}[个]{lang="EN-US" style="font-family:宋体"}[AP]{lang="EN-US"}[组。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当执行该命令创建一个已经存在的组时，不会覆盖原有的组，而是进入]{style="font-family:宋体"}]{#struct_0_73193_x1990_2123995886}[AP]{lang="EN-US"}[组视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1135097795}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1017167528}[创建一个名为]{style="font-family:宋体"}[group1]{lang="EN-US"}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[\<System\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_1958967711}

[\[System\] wlan ap-group group1]{lang="EN-US"}

[\[System-wlan-ap-group-group1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1146024878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display wlan ap-group]{lang="EN-US"}**]{#struct_0_73193_x1990_2125355256}
:::

::: {#2003130159 .myid}
[]{#_Toc404794829}[]{#struct_0_73193_x1990_x2044640688}

**AP管理 \-- AP管理配置命令 \-- wlan auto-ap**

------------------------------------------------------------------------

[**[wlan auto-ap]{lang="EN-US"}**]{#struct_0_73193_x1990_x745006675}[命令用来开启自动]{style="font-family:宋体"}[AP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo wlan auto-ap]{lang="EN-US"}**]{#struct_0_73193_x1990_1524847814}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x741818819}

[**[wlan auto-ap]{lang="EN-US"}**]{#struct_0_73193_x1990_x2143111510}

[**[undo wlan auto-ap]{lang="EN-US"}**]{#struct_0_73193_x1990_x1179073129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73193_x1990_164764333}

[[未开启自动]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_73193_x1990_x1100361993}[功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x2044640687}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_370738572}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1986880015}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1179552151}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_89575291}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_73193_x1990_971392597}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在无线网络中部署的]{style="font-family:宋体"}]{#struct_0_73193_x1990_1188528619}[AP]{lang="EN-US"}[数量较多时，使用自动]{style="font-family:宋体"}[AP]{lang="EN-US"}[功能可以减少管理员的配置工作量，并可以简化配置，避免多次配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[序列号，同时降低了配置出错的概率。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[自动]{style="font-family:宋体"}]{#struct_0_73193_x1990_1701040632}[AP]{lang="EN-US"}[不能单独配置，需要固化为手工]{style="font-family:宋体"}[AP]{lang="EN-US"}[或者通过]{style="font-family:宋体"}[AP Group]{lang="EN-US"}[进行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x790289428}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x1158280179}[开启自动]{style="font-family:宋体"}[AP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_x1185135951}

[\[Sysname\] wlan auto-ap]{lang="EN-US"}
:::

::: {#-1614825515 .myid}
[]{#_Toc404794830}[]{#struct_0_73193_x1990_x153189405}[]{#_Toc393205671}

**AP管理 \-- AP管理配置命令 \-- wlan global-configuration**

------------------------------------------------------------------------

[**[wlan global-configuration]{lang="EN-US"}**]{#struct_0_73193_x1990_x589094333}[命令用来进入全局配置视图。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x248244620}

[**[wlan global-configuration]{lang="EN-US"}**]{#struct_0_73193_x1990_962281022}

[[【视图】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_73193_x1990_x606842255}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_x941946708}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1961929199}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x349605754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1594641470}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1719273346}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_1699826333}[进入全局配置视图。]{style="font-family:宋体"}

[[\<System\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_x14401315}

[\[System\] wlan global-configuration]{lang="EN-US"}

[\[System-wlan-global-configuration\]]{lang="EN-US"}
:::

::: {#-950227109 .myid}
[]{#_Toc404794831}[]{#struct_0_73193_x1990_1629170338}[]{#_Toc393205677}[]{#_Toc384720044}

**AP管理 \-- AP管理配置命令 \-- wlan re-group**

------------------------------------------------------------------------

[**[wlan re-group]{lang="EN-US"}**]{#struct_0_73193_x1990_x1016450111}[命令用于将一个或者一组]{style="font-family:宋体"}[AP]{lang="EN-US"}[规则迁移到指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73193_x1990_290808342}

[**[wlan re-group]{lang="EN-US"}**[ { **ap** *ap-name* \| **ap-list** *list-name* \| **ap-group**]{lang="EN-US"}]{#struct_0_73193_x1990_1963500240}**[ ]{lang="EN-US" style="color:black;border:none windowtext 1.0pt;padding:0cm"}***[old-group-name]{lang="EN-US"}*[ \| mac-address *mac-address* \| serial-id *serial-id* } *group-name*]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x437300443}

[[系统视图]{style="font-family:宋体"}]{#struct_0_73193_x1990_1013178934}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73193_x1990_x1716737571}

[[network-admin]{lang="EN-US"}]{#struct_0_73193_x1990_x1099713017}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73193_x1990_528254636}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1710837771}

[**[ap]{lang="EN-US"}***[ ap-name]{lang="EN-US"}*]{#struct_0_73193_x1990_x264668994}[：将指定的]{style="font-family:宋体"}[AP]{lang="EN-US"}[名字入组规则迁移到目的]{style="font-family:宋体"}[AP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[**[ap-list]{lang="EN-US"}**[ *list-name*]{lang="EN-US"}]{#struct_0_73193_x1990_x551125835}[：将指定的]{style="font-family:宋体"}[AP]{lang="EN-US"}[列表名的]{style="font-family:宋体"}[AP]{lang="EN-US"}[迁移到目的]{style="font-family:宋体"}[AP]{lang="EN-US"}[组。]{style="font-family:宋体"}

[**[mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*]{#struct_0_73193_x1990_x1801606401}[：将指定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址入组规则迁移到目的组。]{style="font-family:宋体"}

[**[serial-id]{lang="EN-US"}**[ *serial-id*]{lang="EN-US"}]{#struct_0_73193_x1990_353871897}[：将指定的序列号地址入组规则迁移到目的组。]{style="font-family:宋体"}

[**[ap-group]{lang="EN-US"}**[ *old-group-name*]{lang="EN-US"}]{#struct_0_73193_x1990_1306309016}[：将指定的]{style="font-family:宋体"}[AP]{lang="EN-US"}[组的入组规则迁移到目的]{style="font-family:宋体"}[AP]{lang="EN-US"}[组。]{style="font-family:宋体"}*[old-group-name]{lang="EN-US"}*[不能是默认组。]{style="font-family:宋体"}

[[group-name]{lang="EN-US"}]{#struct_0_73193_x1990_x1304085119}[：目的]{style="font-family:宋体"}[AP]{lang="EN-US"}[组名字，不能是默认组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73193_x1990_1310640462}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x349895459}[创建]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[group2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<System\> system-view]{lang="EN-US"}]{#struct_0_73193_x1990_339260412}

[\[System\] wlan ap-group group2]{lang="EN-US"}

[\[System-wlan-ap-group-group2\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x700833061}[创建]{style="font-family:宋体"}[AP]{lang="EN-US"}[组]{style="font-family:宋体"}[group1]{lang="EN-US"}[，在]{style="font-family:宋体"}[group1]{lang="EN-US"}[下配置三个]{style="font-family:宋体"}[AP]{lang="EN-US"}[名字规则]{style="font-family:宋体"}[ap1]{lang="EN-US"}[、]{style="font-family:宋体"}[ap2]{lang="EN-US"}[、]{style="font-family:宋体"}[ap3]{lang="EN-US"}[，并将]{style="font-family:宋体"}[ap1]{lang="EN-US"}[移至]{style="font-family:宋体"}[group2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[System\] wlan ap-group group1]{lang="EN-US"}]{#struct_0_73193_x1990_371883336}

[\[System-wlan-ap-group-group1\] ap ap1 ap2 ap3]{lang="EN-US"}

[\[System-wlan-ap-group-group1\] quit]{lang="EN-US"}

[\[System\] wlan re-group ap ap1 group2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x423060125}[创建]{style="font-family:宋体"}[AP]{lang="EN-US"}[列表]{style="font-family:宋体"}[list1]{lang="EN-US"}[，并且在]{style="font-family:宋体"}[list1]{lang="EN-US"}[下配置一个]{style="font-family:宋体"}[AP MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[2-2-2-2]{lang="EN-US"}[，并将]{style="font-family:宋体"}[list1]{lang="EN-US"}[移至]{style="font-family:宋体"}[group2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[System\] wlan ap-list list1]{lang="EN-US"}]{#struct_0_73193_x1990_1899364470}

[\[System-wlan-ap-list-list1\] mac-address 2-2-2-2]{lang="EN-US"}

[\[System-wlan-ap-list-list1\] quit]{lang="EN-US"}

[\[System\] wlan re-group ap-list list1 group2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_73193_x1990_x1046271173}[将]{style="font-family:宋体"}[group1]{lang="EN-US"}[中所有]{style="font-family:宋体"}[AP]{lang="EN-US"}[规则移至]{style="font-family:宋体"}[group2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[System\] wlan re-group ap-group group1 group2]{lang="EN-US"}]{#struct_0_73193_x1990_466370924}
:::
