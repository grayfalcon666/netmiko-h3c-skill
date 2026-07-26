::: {#856963458 .myid}
[]{#_Toc404791999}[]{#struct_0_x2088_36527_x1533615553}[]{#_Toc364694870}[]{#_Toc33369468}

**帧中继QoS \-- 帧中继QoS配置命令 \-- cir allow**

------------------------------------------------------------------------

[**[cir allow]{lang="EN-US"}**]{#struct_0_x2088_36527_x385001570}[命令用来配置帧中继虚电路]{style="font-family:宋体"}[CIR ALLOW]{lang="EN-US"}[（]{style="font-family:宋体"}[Committed Information Rate ALLOW]{lang="EN-US"}[，允许的承诺信息速率）。]{style="font-family:
宋体"}

[**[undo cir allow]{lang="EN-US"}**]{#struct_0_x2088_36527_x164251490}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1883073228}

[**[cir allow]{lang="EN-US"}**[ \[ **inbound** \| **outbound** \] *committed-information-rate*]{lang="EN-US"}]{#struct_0_x2088_36527_1372725125}

[**[undo cir allow]{lang="EN-US"}**[ \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_x2088_36527_1757647481}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1552354151}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2088_36527_x739317402}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2088_36527_1655735424}

[[帧中继类视图]{style="font-family:宋体"}]{#struct_0_x2088_36527_1092935078}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1124616870}

[[network-admin]{lang="EN-US"}]{#struct_0_x2088_36527_x1093155333}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2088_36527_x1197967295}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x339542448}

[**[inbound]{lang="EN-US"}**]{#struct_0_x2088_36527_x1579627602}[：报文入方向所允许的承诺信息速率，本参数仅当接口使能帧中继流量监管时有效。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x2088_36527_x98692396}[：报文出方向所允许的承诺信息速率，本参数仅当接口使能帧中继流量整形时有效。]{style="font-family:宋体"}

[*[committed-information-rate]{lang="EN-US"}*]{#struct_0_x2088_36527_1185665198}[：允许的承诺信息速率，单位为]{style="font-family:
宋体"}[bps]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2088_36527_1534574142}

[[允许的承诺信息速率是正常情况下帧中继网络所能提供的发送速率，当网络没有发生拥塞时，它保证用户能够以此速率发送数据。]{style="font-family:宋体"}]{#struct_0_x2088_36527_536035847}

[[如果配置时不指定报文方向，则表示同时配置在入方向和出方向上。]{style="font-family:宋体"}]{#struct_0_x2088_36527_1432460826}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1066134375}

[[\# ]{lang="EN-US"}]{#struct_0_x2088_36527_483257131}[配置名为]{style="font-family:宋体"}[test1]{lang="EN-US"}[的帧中继类的]{style="font-family:宋体"}[CIR ALLOW]{lang="EN-US"}[为]{style="font-family:宋体"}[64000bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2088_36527_x738858650}

[\[Sysname\] fr class test1]{lang="EN-US"}

[\[Sysname-fr-class-test1\] cir allow 64000]{lang="EN-US"}
:::

::: {#242212114 .myid}
[]{#_Toc404792000}[]{#struct_0_x2088_36527_435914731}[]{#_Toc364694871}[]{#_Toc121761579}

**帧中继QoS \-- 帧中继QoS配置命令 \-- display fr class-map**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **fr class-map**]{lang="EN-US"}]{#struct_0_x2088_36527_x1846354065}[命令用来显示帧中继类与接口以及虚电路的映射关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1981164981}

[**[display]{lang="EN-US"}**[ **fr** **class-map** \[ **fr-class** *class-name* \| **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2088_36527_x1377560963}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1079460636}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2088_36527_2093145893}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1871926877}

[[network-admin]{lang="EN-US"}]{#struct_0_x2088_36527_x106033990}

[[network-operator]{lang="EN-US"}]{#struct_0_x2088_36527_x1873511462}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2088_36527_1820428670}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2088_36527_x1127425999}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x587026217}

[**[fr-class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x2088_36527_x408867524}[：显示指定帧中继类与接口以及虚电路的映射关系。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[表示帧中继类名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2088_36527_1745768377}[：]{style="font-family:宋体"}[指定接口的类型和编号]{style="font-family:宋体"}[，可以指定主接口，也可以指定子接口。指定主接口时，显示帧中继类与该主接口及其子接口以及其下的虚电路的映射关系]{style="font-family:宋体"}[。]{style="font-family:宋体"}[指定子接口时，显示帧中继类与该子接口及其下的虚电路的映射关系]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x2048202683}

[[不指定接口和帧中继类名称时，显示所有帧中继类与接口以及虚电路的映射关系。]{style="font-family:宋体"}]{#struct_0_x2088_36527_x1114827856}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x738924186}

[[\# ]{lang="EN-US"}]{#struct_0_x2088_36527_1248465043}[显示接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[与帧中继类的映射关系。]{style="font-family:宋体"}

[[\<Sysname\> display fr class-map interface serial 2/1/0]{lang="EN-US"}]{#struct_0_x2088_36527_547349885}

[Serial2/1/0]{lang="EN-US"}

[  fr-class ts1]{lang="EN-US"}

[  fr dlci 100]{lang="EN-US"}

[    fr-class ts]{lang="EN-US"}

[Serial2/1/0.1]{lang="EN-US"}

[  fr-class ts2]{lang="EN-US"}

[  fr dlci 222]{lang="EN-US"}

[    fr-class ts]{lang="EN-US"}

[[\# ]{lang="IT"}]{#struct_0_x2088_36527_x1226014798}[显示帧中继类]{style="font-family:宋体"}[ts]{lang="IT"}[与接口的映射关系。]{style="font-family:宋体"}

[[\<Sysname\> display fr class-map fr-class ts]{lang="IT"}]{#struct_0_x2088_36527_2026583919}

[Serial2/1/0]{lang="EN-US"}

[  fr dlci 100]{lang="EN-US"}

[    fr-class ts]{lang="EN-US"}

[Serial2/1/0.1]{lang="EN-US"}

[  fr dlci 222]{lang="EN-US"}

[    fr-class ts]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display fr class-map]{lang="EN-US"}]{#struct_0_x2088_36527_364741970}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_361819286}[[字段]{style="font-family:黑体"}]{#struct_0_x2088_36527_x352496310}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2088_36527_x679856410}

[[Serial2/1/0]{lang="EN-US"}]{#struct_0_x2088_36527_104119973}

[[  fr-class ts1]{lang="EN-US"}]{#struct_0_x2088_36527_19750185}

[[帧中继接口及关联的帧中继类]{style="font-family:宋体"}]{#struct_0_x2088_36527_x738989722}

[[fr dlci 100]{lang="EN-US"}]{#struct_0_x2088_36527_76026678}

[[  fr-class ts]{lang="EN-US"}]{#struct_0_x2088_36527_1669624114}

[[帧中继接口下的虚电路及关联的帧中继类]{style="font-family:宋体"}]{#struct_0_x2088_36527_355804662}

[[Serial2/1/0.1]{lang="EN-US"}]{#struct_0_x2088_36527_765092074}

[[  fr-class ts2]{lang="EN-US"}]{#struct_0_x2088_36527_958467191}

[[帧中继子接口及关联的帧中继类]{style="font-family:宋体"}]{#struct_0_x2088_36527_1299974515}

[[fr dlci 222]{lang="EN-US"}]{#struct_0_x2088_36527_276703731}

[[  fr-class ts]{lang="EN-US"}]{#struct_0_x2088_36527_x1251379322}

[[帧中继子接口下的虚电路及关联的帧中继类]{style="font-family:宋体"}]{#struct_0_x2088_36527_953243375}

[ ]{lang="EN-US"}

::: {#-1406617631 .myid}
[]{#_Toc404792001}[]{#struct_0_x2088_36527_637970134}[]{#_Toc364694872}[]{#_Toc56569695}

**帧中继QoS \-- 帧中继QoS配置命令 \-- fr class**

------------------------------------------------------------------------

[**[fr class]{lang="EN-US"}**]{#struct_0_x2088_36527_1351066076}[命令用来创建帧中继类并进入帧中继类视图。]{style="font-family:宋体"}

[**[undo fr class]{lang="EN-US"}**]{#struct_0_x2088_36527_x739055258}[命令用来删除指定的帧中继类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2088_36527_1633000100}

[**[fr class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x2088_36527_x1238887142}

[**[undo fr class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x2088_36527_1093403758}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1483998637}

[[没有创建帧中继类。]{style="font-family:宋体"}]{#struct_0_x2088_36527_119141544}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1581271562}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2088_36527_x205731391}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2088_36527_1406297641}

[[network-admin]{lang="EN-US"}]{#struct_0_x2088_36527_696877569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2088_36527_x96175042}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1095098007}

[*[class-name]{lang="EN-US"}*]{#struct_0_x2088_36527_x1527527936}[：帧中继类名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1911984014}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有将帧中继类同帧中继接口或虚电路相关联，并且使能相应接口的帧中继]{style="font-family:宋体"}]{#struct_0_x2088_36527_1782780687}[QoS]{lang="EN-US"}[功能，配置的帧中继类参数才会起作用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除帧中继类时，将释放所有帧中继接口和虚电路与该帧中继类的关联。]{style="font-family:宋体"}]{#struct_0_x2088_36527_1273460504}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x738596506}

[[\# ]{lang="EN-US"}]{#struct_0_x2088_36527_1661860157}[创建名为]{style="font-family:宋体"}[test1]{lang="EN-US"}[的帧中继类。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2088_36527_932729544}

[\[Sysname\] fr class test1]{lang="EN-US"}

[\[Sysname-fr-class-test1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2088_36527_23065565}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr-class]{lang="EN-US"}**]{#struct_0_x2088_36527_x183894779}
:::

::: {#-1154319416 .myid}
[]{#_Toc404792002}[]{#struct_0_x2088_36527_x1098115113}[]{#_Toc364694873}[]{#_Toc33369506}

**帧中继QoS \-- 帧中继QoS配置命令 \-- fr traffic-shaping**

------------------------------------------------------------------------

[**[fr traffic-shaping]{lang="EN-US"}**]{#struct_0_x2088_36527_x633448138}[命令用来使能帧中继流量整形功能。]{style="font-family:宋体"}

[**[undo fr traffic-shaping]{lang="EN-US"}**]{#struct_0_x2088_36527_x874543251}[命令用来关闭帧中继流量整形功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1012500736}

[**[fr traffic-shaping]{lang="EN-US"}**]{#struct_0_x2088_36527_x1456294732}

[**[undo fr traffic-shaping]{lang="EN-US"}**]{#struct_0_x2088_36527_x49012006}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1275189860}

[[帧中继流量整形功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x2088_36527_371268549}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x765502802}

[[帧中继接口视图]{style="font-family:宋体"}]{#struct_0_x2088_36527_x1077278118}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x738662042}

[[network-admin]{lang="EN-US"}]{#struct_0_x2088_36527_x1911960562}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2088_36527_1899531036}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1028070546}

[[帧中继流量整形功能应用于设备的出接口上，通常应用于帧中继网络的]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_x2088_36527_1485871461}[端。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x2051151093}

[[\# ]{lang="EN-US"}]{#struct_0_x2088_36527_1394738049}[在串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上使能帧中继流量整形功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2088_36527_x1165642888}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr traffic-shaping]{lang="EN-US"}
:::

::: {#724116314 .myid}
[]{#_Toc404792003}[]{#struct_0_x2088_36527_1975883462}[]{#_Toc364694874}[]{#_Toc13387656}

**帧中继QoS \-- 帧中继QoS配置命令 \-- fr-class**

------------------------------------------------------------------------

[**[fr-class]{lang="EN-US"}**]{#struct_0_x2088_36527_732539040}[命令用来将帧中继类与当前帧中继接口或虚电路关联起来。]{style="font-family:宋体"}

[**[undo fr-class]{lang="EN-US"}**]{#struct_0_x2088_36527_881334777}[命令用来取消帧中继类与当前帧中继接口或虚电路的关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x1222143061}

[**[fr-class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x2088_36527_862132256}

[**[undo fr-class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x2088_36527_1883649793}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x329365766}

[[帧中继类没有与帧中继接口或虚电路相关联。]{style="font-family:宋体"}]{#struct_0_x2088_36527_x1308122324}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x739120795}

[[帧中继接口视图（包括主接口和子接口）]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2088_36527_x701373946}[帧中继]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图]{style="font-family:宋体"}[]{#_Toc32639723}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2088_36527_1576238209}

[[network-admin]{lang="EN-US"}]{#struct_0_x2088_36527_244158576}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2088_36527_1345247657}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2088_36527_253033748}

[*[class-name]{lang="EN-US"}*]{#struct_0_x2088_36527_x381441491}[：帧中继类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个字符的字符串，区分大小写。该帧中继类必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2088_36527_118208908}

[[将一个帧中继类和接口关联起来之后，此接口上的所有虚电路都会继承此帧中继类的帧中继]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_x2088_36527_124012333}[参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x2024222949}

[[\# ]{lang="EN-US"}]{#struct_0_x2088_36527_1874312929}[将名为]{style="font-family:宋体"}[test1]{lang="EN-US"}[的帧中继类与]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[的帧中继虚电路关联起来。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2088_36527_x1373364638}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[Sysname-Serial2/1/0-fr-dlci-200\] fr-class test1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2088_36527_x578044154}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr class]{lang="EN-US"}**]{#struct_0_x2088_36527_1195889667}
:::
