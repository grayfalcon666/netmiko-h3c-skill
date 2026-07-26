::: {#-479810411 .myid}
[]{#_Toc404797468}[]{#struct_0_x9799_x9248_x329976305}

**GOLD \-- GOLD配置命令 \-- diagnostic bootup level**

------------------------------------------------------------------------

[**[diagnostic bootup level]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2115823481}[命令用来配置设备下次启动时，是否执行所有启动诊断测试例。]{style="font-family:宋体"}

[**[undo diagnostic bootup level]{lang="EN-US"}**]{#struct_0_x9799_x9248_x941133765}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1188783062}

[**[diagnostic ]{lang="EN-US"}[bootup level ]{lang="EN-US"}**[{ **bypass** \| **complete** }]{lang="EN-US"}]{#struct_0_x9799_x9248_828046932}

[**[undo diagnostic bootup level]{lang="EN-US"}**]{#struct_0_x9799_x9248_1892573272}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_561969716}

[[系统在启动时不执行任何启动测试例。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1407293053}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_23995066}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1570517448}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x594707610}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x942116805}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1277209303}

[**[bypass]{lang="EN-US"}**]{#struct_0_x9799_x9248_1127776219}[：所有测试例均不执行。]{style="font-family:宋体"}

[**[complete]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1005565366}[：执行所有的测试例。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_529789639}

[[启动诊断是在系统启动过程或者板卡插拔时对板卡进行检查，设备将根据检查的结果决定板卡能否运行。启动诊断能够保证板卡基本硬件功能正常后才开始工作。设备支持的启动诊断的具体内容与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1747410850}

[[本命令配置后，将在设备下次启动时生效。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_181326909}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1745517309}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1797511298}[配置设备下次启动时，执行所有启动诊断测试例。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_1145037685}

[\[sysname\] diagnostic bootup level complete]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_385350855}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display diagnostic bootup level]{lang="EN-US"}**]{#struct_0_x9799_x9248_x941592516}
:::

::: {#1169072508 .myid}
[]{#_Toc404797469}[]{#struct_0_x9799_x9248_x76728933}

**GOLD \-- GOLD配置命令 \-- diagnostic bootup enable test**

------------------------------------------------------------------------

[**[diagnostic bootup enable test]{lang="EN-US"}**]{#struct_0_x9799_x9248_x777260957}[命令用来配置设备下次启动时，执行指定的启动诊断测试例。]{style="font-family:
宋体"}

[**[undo diagnostic bootup enable test]{lang="EN-US"}**]{#struct_0_x9799_x9248_31982041}[命令用来取消执行指定的启动诊断测试例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_379656984}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1152501984}

[**[diagnostic bootup enable test]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_818825394}*[test-name]{lang="EN-US"}*[ \[ **para** ]{lang="EN-US"}*[parameters]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo diagnostic bootup enable test]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_30612638}*[test-name]{lang="EN-US"}*[ \[ **para** ]{lang="EN-US"}*[parameters]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_1351066012}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[diagnostic bootup enable slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1384757032}*[slot-number-list]{lang="EN-US"}*[ \[ **cpu** ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \[ **para** ]{lang="EN-US"}*[parameters]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo diagnostic bootup enable ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1027001223}**[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \[ **para** ]{lang="EN-US"}*[parameters]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_x1189042051}[模式：]{style="font-family:宋体"}

[**[diagnostic bootup enable chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1134705690}*[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*[ \[ **cpu** ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \[ **para** ]{lang="EN-US"}*[parameters]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo diagnostic bootup ]{lang="EN-US"}**]{#struct_0_x9799_x9248_424791468}**[enable]{lang="EN-US"}[ ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \[ **para** ]{lang="EN-US"}*[parameters]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1155881750}

[[系统在启动时不执行任何启动测试例。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1660792689}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1822540632}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1688834645}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x131774247}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x903999418}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_365628219}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1724396319}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时使能多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x126334261}*[slot-number-list]{lang="EN-US"}*[：成员编号列表，表示同时使能多个成员设备的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_2115382929}*[slot-number-list]{lang="EN-US"}*[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时使能多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_631665603}*[chassis-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1919496273}*[chassis-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x419419071}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时使能多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_283837151}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时使能多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_1210487643}*[cpu-number]{lang="EN-US"}*[：表示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[test]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2114553544}*[ test-name]{lang="EN-US"}*[：表示启动诊断类型的测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。具体取值可通过在]{style="font-family:宋体"}**[test]{lang="EN-US"}**[参数后输入问号，并回车来获取。]{style="font-family:宋体"}

[**[para]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_181712974}*[parameters]{lang="EN-US"}*[：表示测试例的执行参数，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[511]{lang="EN-US"}[个字符的字符串，不区分大小写。参数的取值、输入方式以及缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1276785991}

[[本命令配置后，将在设备下次启动时生效。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_960795248}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1306109540}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x95570391}[配置设备下次启动时，执行启动诊断测试例]{style="font-family:宋体"}[OnlyBootUp]{lang="EN-US"}[，并指定参数为]{style="font-family:宋体"}[123]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_x934418338}

[\[sysname\] diagnostic bootup enable test OnlyBootUp para 123]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x682457236}[配置设备下次启动时，执行]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板上的启动诊断测试例]{style="font-family:宋体"}[OnlyBootUp]{lang="EN-US"}[，并指定参数为]{style="font-family:宋体"}[123]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_1834132157}

[\[sysname\] diagnostic bootup enable slot 0 test OnlyBootUp para 123]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_715914807}[配置设备下次启动时，执行成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上的启动诊断测试例]{style="font-family:宋体"}[OnlyBootUp]{lang="EN-US"}[，并指定参数为]{style="font-family:宋体"}[123]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_x1781026749}

[\[sysname\] diagnostic bootup enable slot 1 test OnlyBootUp para 123]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x584076671}[配置设备下次启动时，执行]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板上的启动诊断测试例]{style="font-family:宋体"}[OnlyBootUp]{lang="EN-US"}[，并指定参数为]{style="font-family:宋体"}[123]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_x694211270}

[\[sysname\] diagnostic bootup enable chassis 1 slot 0 test OnlyBootUp para 123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_987437211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display diagnostic bootup]{lang="EN-US"}**]{#struct_0_x9799_x9248_141376617}
:::

::: {#-500068872 .myid}
[]{#_Toc404797470}[]{#struct_0_x9799_x9248_8136698}[]{#_Toc334794713}

**GOLD \-- GOLD配置命令 \-- diagnostic event-log size**

------------------------------------------------------------------------

[**[diagnostic event-log size]{lang="EN-US"}**]{#struct_0_x9799_x9248_640199421}[命令用来配置可存储的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的最大条数。]{style="font-family:宋体"}

[**[undo diagnostic event-log size]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1652237961}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x204207941}

[**[diagnostic event-log size ]{lang="EN-US"}**]{#struct_0_x9799_x9248_253316749}[]{#OLE_LINK57}[*[number]{lang="EN-US"}*]{#OLE_LINK56}

[**[undo diagnostic event-log size]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2084459920}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x381162175}

[[可存储的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}]{#struct_0_x9799_x9248_x1056548052}[日志的最大条数为]{style="font-family:宋体"}[512]{lang="EN-US"}[条。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x941526980}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1197430165}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1945151449}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x57494583}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1975295819}

[*[number]{lang="EN-US"}*]{#struct_0_x9799_x9248_x473807558}[：可存储的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的最大条数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[，单位为条。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x136099323}

[[执行该命令时，如果指定的]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1394479598}*[number]{lang="EN-US"}*[值小于当前已存储的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的条数，则系统会自动删除最旧的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志，直到当前]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的条数为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[当设备当前已存储的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}]{#struct_0_x9799_x9248_x783532355}[日志的条数达到最大值，同时还有新的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志需要存储时，系统会删除最旧的日志来存储新的日志。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1471718505}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x941461444}[配置可存储的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的最大条数]{style="font-family:宋体"}[为]{style="font-family:宋体"}[600]{lang="EN-US"}[条。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_1919714797}

[\[sysname\] diagnostic event-log size 600]{lang="EN-US"}
:::

::: {#-1969464266 .myid}
[]{#_Toc404797471}[]{#struct_0_x9799_x9248_x1458383063}

**GOLD \-- GOLD配置命令 \-- diagnostic monitor enable**

------------------------------------------------------------------------

[**[diagnostic monitor enable]{lang="EN-US"}**]{#struct_0_x9799_x9248_1771157115}[命令用来开启监控诊断功能。]{style="font-family:
宋体"}

[**[undo diagnostic monitor enable]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1534821395}[命令用来关闭监控诊断功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x245236820}

[]{#OLE_LINK76}[]{#OLE_LINK75}[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x653765368}

[**[diagnostic monitor enable]{lang="EN-US"}**[ \[ **test** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1644342182}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo diagnostic monitor enable]{lang="EN-US"}**[ \[ **test** ]{lang="EN-US"}]{#struct_0_x9799_x9248_181885626}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_x941395908}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[diagnostic monitor enable]{lang="EN-US"}**[ **slot** ]{lang="EN-US"}]{#struct_0_x9799_x9248_808629020}*[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo diagnostic monitor enable slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1118793411}*[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_x1209298512}[模式：]{style="font-family:宋体"}

[**[diagnostic monitor enable chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1284993556}*[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo diagnostic monitor enable chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1538129483}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] \[ **test**]{lang="EN-US"}*[ test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x327085323}

[[监控诊断测试例缺省是否使能与设备的型号以及版本有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1927765339}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x941330372}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1990520588}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1381134367}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x1496299071}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x779482097}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1655968835}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时使能多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1703440450}*[slot-number-list]{lang="EN-US"}*[：成员编号列表，表示同时使能多个成员设备的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x928845}*[slot-number-list]{lang="EN-US"}*[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时使能多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_624370530}*[chassis-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1819329742}*[chassis-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1773062009}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时使能多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x994381}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时使能多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x941264836}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示使能设备上的所有监控诊断测试例。（集中式设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_395656765}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示使能指定单板上的所有监控诊断测试例。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_506391732}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示使能指定成员设备上的所有监控诊断测试例。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x969926995}*[cpu-number]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1140297220}

[[系统在运行过程中]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1658193129}[按照一定的时间间隔定时执行测试例]{style="font-family:宋体"}[，来]{style="font-family:宋体"}[检测系统中的硬件故障并记录诊断结果的过程，称为监控诊断。监控诊断]{style="font-family:宋体"}[只能执行非破坏性的测试例。]{style="font-family:宋体"}

[[破坏性和非破坏性是测试例的一个属性，由开发人员在设计测试例的时候指定。其中：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x403650782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[破坏性测试例在执行过程中会对设备当前正常运行的业务产生影响或导致业务无法运行，如内存耗尽测试例。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1728712276}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非破坏性测试例在执行过程中不会对设备当前正常运行的业务产生影响。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1641405393}

[[对于]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x941199300}[缺省启动的监控诊断测试例，在设备启动后会自动执行；对于缺省关闭的监控诊断测试例，须使用本命令才能执行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1107700286}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_449913729}[使能测试例]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_x271337493}

[\[sysname\] diagnostic monitor enable test HGMonitor]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_550127918}[使能]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的测试例]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_497429666}

[\[sysname\] diagnostic monitor enable slot 2 test HGMonitor]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x941133764}[使能]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上的测试例]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_x1188717526}

[\[sysname\] diagnostic monitor enable slot 2 test HGMonitor]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1189207356}[使能]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上的测试例]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_1624954248}

[\[sysname\] diagnostic monitor enable chassis 2 slot 2 test HGMonitor]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_872702032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic monitor interval]{lang="EN-US"}**]{#struct_0_x9799_x9248_1688096106}
:::

::: {#-1593497859 .myid}
[]{#_Toc404797472}[]{#struct_0_x9799_x9248_x2124128089}[]{#_Toc334794707}[]{#_Toc334887872}[]{#_Toc335035521}[]{#_Toc334536975}[]{#_Toc334536976}[]{#_Toc334536977}[]{#_Toc334536978}[]{#_Toc334536979}[]{#_Toc334536980}[]{#_Toc334536981}[]{#_Toc334536982}[]{#_Toc334536983}[]{#_Toc334536984}[]{#_Toc334536985}[]{#_Toc334536986}[]{#_Toc334536987}[]{#_Toc334536988}[]{#_Toc334536989}[]{#_Toc334536990}[]{#_Toc334536991}[]{#_Toc334536992}[]{#_Toc334536993}[]{#_Toc334536994}[]{#_Toc334536995}[]{#_Toc334536996}[]{#_Toc334537010}[]{#_Toc334537027}[]{#_Toc334537028}[]{#_Toc334537029}[]{#_Toc334537030}[]{#_Toc334537032}[]{#_Toc334537033}[]{#_Toc334537034}[]{#_Toc334537035}[]{#_Toc334537036}[]{#_Toc334537037}[]{#_Toc334537038}[]{#_Toc334537039}[]{#_Toc334537040}[]{#_Toc334537041}[]{#_Toc334537042}[]{#_Toc334537043}[]{#_Toc334537044}[]{#_Toc334537045}[]{#_Toc334537046}[]{#_Toc334537047}[]{#_Toc334537048}[]{#_Toc334537049}[]{#_Toc334537050}[]{#_Toc334537051}[]{#_Toc334537053}[]{#_Toc334537054}[]{#_Toc334537055}[]{#_Toc334537056}[]{#_Toc334537057}[]{#_Toc334537058}[]{#_Toc334537059}[]{#_Toc334537060}[]{#_Toc334537061}[]{#_Toc334537062}[]{#_Toc334537063}[]{#_Toc334537064}[]{#_Toc334537065}[]{#_Toc334537066}[]{#_Toc334537067}[]{#_Toc334537068}[]{#_Toc334537069}[]{#_Toc334537070}[]{#_Toc334537071}[]{#_Toc334537072}[]{#_Toc334537073}[]{#_Toc334537074}[]{#_Toc334537075}[]{#_Toc334537080}[]{#_Toc334537081}[]{#_Toc334537082}[]{#_Toc334537083}[]{#_Toc334537084}[]{#_Toc334537085}[]{#_Toc334537086}[]{#_Toc334537087}[]{#_Toc334537088}[]{#_Toc334537089}[]{#_Toc334537090}[]{#_Toc334537091}[]{#_Toc334537092}[]{#_Toc334537093}[]{#_Toc334537094}[]{#_Toc334537095}[]{#_Toc334537096}[]{#_Toc334537097}[]{#_Toc334537098}[]{#_Toc334537099}[]{#_Toc334537100}[]{#_Toc334537101}[]{#_Toc334537102}[]{#_Toc334537103}[]{#_Toc334537104}[]{#_Toc334537105}[]{#_Toc334537106}[]{#_Toc334537107}[]{#_Toc334537109}[]{#_Toc334537110}[]{#_Toc334537111}

**GOLD \-- GOLD配置命令 \-- diagnostic monitor interval**

------------------------------------------------------------------------

[**[diagnostic monitor interval]{lang="EN-US"}**]{#struct_0_x9799_x9248_154972331}[命令用来配置监控诊断测试例的执行时间间隔。]{style="font-family:
宋体"}

[**[undo diagnostic monitor interval]{lang="EN-US"}**]{#struct_0_x9799_x9248_x942116804}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1277143767}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_695438719}

[**[diagnostic monitor interval]{lang="EN-US"}**[ \[ **test** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1451873971}*[test-name]{lang="EN-US"}*[ \] **time** ]{lang="EN-US"}*[time]{lang="EN-US"}*

[**[undo diagnostic monitor interval]{lang="EN-US"}**[ \[ **test** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1525007933}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_1989525319}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[diagnostic monitor interval slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1006977577}*[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \] **time** ]{lang="EN-US"}*[time]{lang="EN-US"}*

[**[undo diagnostic monitor interval slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_318836166}*[slot-number-list ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\]]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_479847204}[模式：]{style="font-family:宋体"}

[**[diagnostic monitor interval chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x942051268}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \] **time** ]{lang="EN-US"}*[time]{lang="EN-US"}*

[**[undo diagnostic monitor interval chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1745451773}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_700101652}

[[监控诊断测试例时间间隔的缺省值与设备的型号以及版本有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1702956136}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1532384700}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x144162095}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1951127666}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x161111876}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_375362903}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1772466928}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时配置多个单板的测试例的时间间隔。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要配置的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_624491428}*[slot-number-list]{lang="EN-US"}*[：成员编号列表，表示同时配置多个成员设备的测试例的时间间隔。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要配置的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1322060}*[slot-number-list]{lang="EN-US"}*[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时配置多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例的时间间隔。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_868766852}*[chassis-number]{lang="EN-US"}*[：表示需要配置测试例时间间隔的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x827647330}*[chassis-number]{lang="EN-US"}*[：表示需要配置测试例时间间隔的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x281809922}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时配置多个单板的测试例的时间间隔。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1387596}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时配置多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例的时间间隔。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1154815283}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有监控诊断测试例。（集中式设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x628499190}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有监控诊断测试例。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1256987347}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有监控诊断测试例。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[]{#struct_0_x9799_x9248_624556964}[]{#OLE_LINK4}[*[time]{lang="EN-US"}*]{#OLE_LINK3}[：指定监控诊断测试例的执行时间间隔，格式为]{style="font-family:宋体"}[hh:mm:ss]{lang="EN-US"}[（小时]{style="font-family:宋体"}[:]{lang="EN-US"}[分钟]{style="font-family:宋体"}[:]{lang="EN-US"}[秒）。其中]{style="font-family:宋体"}[hh]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[，]{style="font-family:宋体"}[mm]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[，]{style="font-family:宋体"}[ss]{lang="EN-US"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。如果要设置成整分，则可以不输入秒；如果要设置成整时，则可以不输入分和秒。比如将]{style="font-family:宋体"}*[time]{lang="EN-US"}*[参数设置为]{style="font-family:宋体"}[1]{lang="EN-US"}[表示时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[小时。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x970123604}*[cpu-number]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x3588357}

[[使能监控诊断测试例后，测试例会按照一定的时间间隔周期执行，这个时间间隔可用该命令配置。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1614073033}

[[用户配置的时间间隔不能小于监控诊断测试例要求的最小值。监控诊断测试例要求的最小值可使用携带]{style="font-family:宋体"}**[verbose]{lang="EN-US"}**]{#struct_0_x9799_x9248_1280288598}[参数的]{style="font-family:宋体"}**[display diagnostic content]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1227959597}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_597510045}[配置测试例]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[的执行时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_624622500}

[\[sysname\] diagnostic monitor interval test HGMonitor time 00:01:00]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x45037506}[配置]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上测试例]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[的时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_x847795417}

[\[sysname\] diagnostic monitor interval slot 1 test HGMonitor time 00:01:00]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_624688036}[配置]{style="font-family:宋体"}[2]{lang="EN-US"}[号框中]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上测试例]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[的时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x9799_x9248_x2043926697}

[\[sysname\] diagnostic monitor interval chassis 2 slot 1 test HGMonitor time 00:01:00]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1390607651}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic monitor enable]{lang="EN-US"}**]{#struct_0_x9799_x9248_1204562329}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display diagnostic content]{lang="EN-US"}**]{#struct_0_x9799_x9248_637024783}
:::

::: {#132133844 .myid}
[]{#OLE_LINK16}[]{#OLE_LINK15}[]{#_Toc404797473}[]{#struct_0_x9799_x9248_x1205313978}

**GOLD \-- GOLD配置命令 \-- diagnostic ondemand failure**

------------------------------------------------------------------------

[**[diagnostic ondemand failure]{lang="EN-US"}**]{#struct_0_x9799_x9248_624753572}[命令用来配置按需诊断测试例的累计失败执行次数的最大值。]{style="font-family:
宋体"}

[**[undo diagnostic ondemand failure]{lang="EN-US"}**]{#struct_0_x9799_x9248_1550436281}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_120744178}

[]{#struct_0_x9799_x9248_130586633}[**[diagnostic ondemand failure]{lang="EN-US"}**]{#OLE_LINK43}[ ]{lang="EN-US"}*[failure-number]{lang="EN-US"}*

[**[undo diagnostic ondemand failure]{lang="EN-US"}**]{#struct_0_x9799_x9248_x370734055}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1873597707}

[[不限制按需测试例的累计失败执行次数的最大值。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_285571947}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_406210739}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x779456852}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x2126266843}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_624819108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1435788653}

[*[failure-number]{lang="EN-US"}*]{#struct_0_x9799_x9248_1154165365}[：指定失败的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1712446957}

[[使用]{style="font-family:宋体"}**[diagnostic ondemand start]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1942753837}[命令启动按需诊断测试例后，这些测试例什么时候终止执行，受三条命令的限制：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}**[diagnostic ondemand stop]{lang="EN-US"}**]{#struct_0_x9799_x9248_x957298172}[命令可]{style="font-family:宋体"}[立即停止执行]{lang="EN-US" style="font-family:宋体"}[该测试例]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某测试例的]{style="font-family:宋体"}]{#struct_0_x9799_x9248_103913144}[执行次数达到]{lang="EN-US" style="font-family:宋体"}**[diagnostic ondemand repeating]{lang="EN-US"}**[命令中指定的值，则]{lang="EN-US" style="font-family:宋体"}[系统会自动]{style="font-family:宋体"}[停止执行]{lang="EN-US" style="font-family:宋体"}[该测试例]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某测试例的]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x837246875}[执行次数还未达到]{lang="EN-US" style="font-family:宋体"}**[diagnostic ondemand repeating]{lang="EN-US"}**[命令中指定的值，但是测试例在启动后，累计失败的执行次数]{lang="EN-US" style="font-family:宋体"}[已]{style="font-family:宋体"}[达到]{lang="EN-US" style="font-family:宋体"}**[diagnostic ondemand failure]{lang="EN-US"}**[命令中指定的值，则]{lang="EN-US" style="font-family:宋体"}[系统会自动]{style="font-family:宋体"}[停止执行]{lang="EN-US" style="font-family:宋体"}[该测试例]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[本命令可用来修改将要启动的按需诊断测试例的累计失败执行次数的最大值，当前已启动的按需诊断测试例仍使用修改前的值。设备重启后，本命令会恢复到缺省情况，如仍需修改，请重新配置。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1376323404}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624884644}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_178678707}[配置按需诊断测试例的累计失败执行次数的最大值为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand failure 5]{lang="EN-US"}]{#struct_0_x9799_x9248_1784992986}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1563921692}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand repeating]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2015180986}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagno]{lang="EN-US"}**]{#struct_0_x9799_x9248_1788802335}**[stic onde]{lang="EN-US"}[mand start]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display diagnostic ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x729445066}**[ondemand ]{lang="EN-US"}[configuration]{lang="EN-US"}**
:::

::: {#1937515224 .myid}
[]{#_Toc404797474}[]{#struct_0_x9799_x9248_1114678156}[]{#_Toc334794709}

**GOLD \-- GOLD配置命令 \-- diagnostic ondemand repeating**

------------------------------------------------------------------------

[**[diagnostic ondemand repeating]{lang="EN-US"}**]{#struct_0_x9799_x9248_x526865994}[命令用来配置按需诊断测试例重复执行的次数。]{style="font-family:
宋体"}

[**[undo diagnostic ondemand repeating]{lang="EN-US"}**]{#struct_0_x9799_x9248_624950180}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_892705319}

[**[diagnostic ondemand repeating ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1704350909}*[repeating-number]{lang="EN-US"}*

[**[undo diagnostic ondemand repeating]{lang="EN-US"}**]{#struct_0_x9799_x9248_1153890453}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1776952332}

[[按需类型诊断测试例重复执行的次数为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x9799_x9248_x347333354}[次数，表示执行一次就结束。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_623967140}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x979992107}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1226435610}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_1385420170}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_632846059}

[*[repeating-number]{lang="EN-US"}*]{#struct_0_x9799_x9248_1796281824}[：表示按需诊断测试例重复执行的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x763108271}

[[本命令用来修改将要启动的按需诊断测试例重复执行的次数，当前已启动的按需诊断测试例仍使用修改前的值。设备重启后，本命令会恢复到缺省情况，如仍需修改，请重新配置。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1717142555}

[[按需诊断测试例重复执行的次数不能比配置的失败次数小，否则，命令执行失败。按需诊断测试例的失败次数可通过]{style="font-family:宋体"}**[diagnostic ondemand failure]{lang="EN-US"}**]{#struct_0_x9799_x9248_1817834627}[命令配置。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624032676}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_746547730}[配置按需类型测试例重复执行的次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand repeating 2]{lang="EN-US"}]{#struct_0_x9799_x9248_x388994657}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x80734280}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand failure]{lang="EN-US"}**]{#struct_0_x9799_x9248_1898383307}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand start]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1003357441}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display diagnostic configuration]{lang="EN-US"}**]{#struct_0_x9799_x9248_624491429}
:::

::: {#-295631535 .myid}
[]{#_Toc404797475}[]{#struct_0_x9799_x9248_868766851}

**GOLD \-- GOLD配置命令 \-- diagnostic ondemand start**

------------------------------------------------------------------------

[**[diagnostic ondemand start]{lang="EN-US"}**]{#struct_0_x9799_x9248_x281809921}[命令用来启动按需类型诊断。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1154618675}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1252051360}

[**[diagnostic ondemand start test]{lang="EN-US"}**[ { **non-disruptive** \| ]{lang="EN-US"}]{#struct_0_x9799_x9248_300331132}*[test-name]{lang="EN-US"}*[ } \[ **para** ]{lang="EN-US"}*[parameters]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_513249184}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[diagnostic ondemand start slot]{lang="EN-US"}**]{#struct_0_x9799_x9248_548311044}*[ slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** { **non-disruptive** \| ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ } \[ **para** ]{lang="EN-US"}*[parameters ]{lang="EN-US"}*[\]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_x756193717}[模式：]{style="font-family:宋体"}

[**[diagnostic ondemand start chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x35810253}*[chassis-number]{lang="EN-US"}*[ **slot**]{lang="EN-US"}*[ slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** { **non-disruptive** \| ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ } \[ **para** ]{lang="EN-US"}*[parameters ]{lang="EN-US"}*[\]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624556965}

[[所有的按需类型测试例都需要用户手动启动。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x3588358}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1951780041}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1280910516}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x856852916}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_1137248726}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1284720077}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1639447482}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时执行多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_213385676}*[slot-number-list]{lang="EN-US"}*[：成员编号列表，表示同时执行多个成员设备的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213600470}*[slot-number-list]{lang="EN-US"}*[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时执行多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_624622501}*[chassis-number]{lang="EN-US"}*[：表示需要执行测试例的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1009210132}*[chassis-number]{lang="EN-US"}*[：表示需要执行测试例的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x45037505}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时执行多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1169417342}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时执行多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[test-name]{lang="EN-US"}*]{#struct_0_x9799_x9248_x847795418}[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[non-disruptive]{lang="EN-US"}**]{#struct_0_x9799_x9248_634434465}[：执行所有的非破坏性的测试例。]{style="font-family:宋体"}

[**[para]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_1430147909}*[parameters]{lang="EN-US"}*[：扩展参数，暂时无意义。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x970058069}*[cpu-number]{lang="EN-US"}*[：表示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1411364651}

[[在设备维护过程中，用户可以手工启动某些测试例对设备进行诊断，这种诊断称为按需诊断。用于这种诊断的测试例称为按需诊断测试例。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_624688037}

[[用户可以通过命令行配置按需诊断测试例重复执行的次数以及累计失败执行次数的最大值。当用户开启某测试例后，测试例在执行过程中，只要达到上述任意条件，则立即自动停止执行。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2043926696}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1338275704}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1955450454}[启动破坏性按需诊断测试例]{style="font-family:宋体"}[PRBS]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand start test PRBS]{lang="EN-US"}]{#struct_0_x9799_x9248_x1735973752}

[Running test PRBS may disrupt system operation. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_624753573}[启动]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上破坏性按需诊断测试例]{style="font-family:宋体"}[PRBS]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand start slot 1 test PRBS ]{lang="EN-US"}]{#struct_0_x9799_x9248_1550436280}

[Running test PRBS on slot 1 may disrupt system operation. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_120809714}[启动成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上破坏性按需诊断测试例]{style="font-family:宋体"}[PRBS]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand start slot 1 test PRBS ]{lang="EN-US"}]{#struct_0_x9799_x9248_624819109}

[Running test PRBS on slot 1 may disrupt system operation. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1435788654}[启动成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[4]{lang="EN-US"}[号单板上破坏性按需诊断测试例]{style="font-family:
宋体"}[PRBS]{lang="EN-US"}[。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand start chassis 1 slot 4 test PRBS ]{lang="EN-US"}]{#struct_0_x9799_x9248_750880838}

[Running test PRBS on chassis 1 slot 4 may disrupt system operation. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1624854469}[启动非破坏性按需诊断测试例。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand start test non-disruptive]{lang="EN-US"}]{#struct_0_x9799_x9248_2008063859}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x356080941}[在]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板]{style="font-family:宋体"}[上启动非破坏性按需诊断测试例。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand start slot 1 test non-disruptive]{lang="EN-US"}]{#struct_0_x9799_x9248_1436742049}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_624884645}[在成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上启动非破坏性按需诊断测试例。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand start slot 1 test non-disruptive]{lang="EN-US"}]{#struct_0_x9799_x9248_178678708}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1784993001}[在成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上启动非破坏性按需诊断测试例。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[  ]{lang="EN-US"}

[[\<sysname\> diagnostic ondemand start chassis 1 slot 2 test non-disruptive]{lang="EN-US"}]{#struct_0_x9799_x9248_x811662929}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1290660263}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand fail]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1511827355}**[ure]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand repeating]{lang="EN-US"}**]{#struct_0_x9799_x9248_x224527577}
:::

::: {#-685384142 .myid}
[]{#_Toc404797476}[]{#struct_0_x9799_x9248_x56128351}[]{#_Toc214771425}[]{#_Toc195417976}[]{#_Toc193873822}[]{#aa_122}[]{#_Toc317590420}[]{#_Toc271203220}[]{#_Toc262732521}[]{#_Toc202689899}[]{#_Toc202689901}[]{#_Toc202689902}[]{#_Toc202689903}[]{#_Toc202689904}[]{#_Toc202689905}[]{#_Toc202689906}[]{#_Toc202689907}[]{#_Toc202689908}[]{#_Toc202689909}[]{#_Toc202689910}[]{#_Toc202689911}[]{#_Toc202689912}[]{#_Toc202689913}[]{#_Toc202689914}[]{#_Toc202689915}[]{#_Toc202689918}[]{#aa_131}[]{#_Toc317590423}[]{#_Toc271203223}[]{#_Toc335035526}[]{#_Toc335035527}[]{#_Toc335035528}[]{#_Toc335035530}[]{#_Toc335035531}[]{#_Toc335035532}[]{#_Toc335035533}[]{#_Toc335035535}[]{#_Toc335035536}[]{#_Toc335035537}[]{#_Toc335035539}[]{#_Toc335035540}[]{#_Toc335035541}[]{#_Toc335035542}[]{#_Toc335035543}[]{#_Toc335035544}[]{#_Toc335035545}[]{#_Toc335035547}[]{#_Toc335035548}[]{#_Toc335035549}[]{#_Toc335035550}[]{#_Toc335035551}[]{#_Toc335035552}[]{#_Toc335035553}[]{#_Toc335035554}[]{#_Toc335035555}[]{#_Toc335035556}[]{#_Toc335035557}[]{#_Toc335035558}[]{#_Toc335035559}[]{#_Toc335035560}[]{#_Toc335035561}[]{#_Toc335035562}[]{#_Toc335035563}[]{#_Toc335035564}[]{#_Toc335035565}[]{#_Toc335035566}[]{#_Toc335035567}[]{#_Toc335035568}[]{#_Toc335035570}[]{#_Toc335035572}[]{#_Toc335035573}[]{#_Toc335035574}[]{#_Toc335035575}[]{#_Toc335035576}[]{#_Toc335035577}[]{#_Toc335035578}[]{#_Toc335035579}[]{#_Toc335035580}[]{#_Toc335035581}[]{#_Toc335035582}[]{#_Toc335035583}[]{#_Toc335035584}[]{#_Toc335035585}[]{#_Toc335035586}[]{#_Toc335035587}[]{#_Toc335035589}[]{#_Toc335035591}[]{#_Toc335035592}[]{#_Toc335035593}[]{#_Toc335035594}[]{#_Toc335035597}[]{#_Toc335035598}[]{#_Toc335035599}[]{#_Toc335035600}[]{#_Toc335035601}[]{#_Toc335035602}[]{#_Toc335035603}[]{#_Toc335035604}[]{#_Toc335035605}[]{#_Toc335035606}[]{#_Toc335035607}[]{#_Toc335035608}[]{#_Toc335035609}[]{#_Toc335035610}[]{#_Toc335035611}[]{#_Toc335035612}[]{#_Toc335035613}[]{#_Toc335035614}[]{#_Toc335035615}[]{#_Toc335035616}[]{#_Toc335035617}[]{#_Toc335035618}[]{#_Toc335035619}[]{#_Toc335035620}[]{#_Toc335035621}[]{#_Toc335035623}[]{#_Toc335035624}[]{#_Toc335035625}[]{#_Toc335035626}[]{#_Toc335035627}[]{#_Toc335035629}[]{#_Toc335035630}[]{#_Toc335035631}[]{#_Toc335035632}[]{#_Toc335035634}[]{#_Toc335035635}[]{#_Toc335035636}[]{#_Toc335035637}[]{#_Toc335035638}[]{#_Toc335035639}[]{#_Toc335035641}[]{#_Toc335035642}[]{#_Toc335035643}[]{#_Toc335035644}[]{#_Toc335035645}[]{#_Toc335035646}[]{#_Toc335035647}[]{#_Toc335035648}[]{#_Toc335035649}[]{#_Toc335035650}[]{#_Toc335035651}[]{#_Toc335035652}[]{#_Toc335035653}[]{#_Toc335035655}[]{#_Toc335035656}[]{#_Toc335035657}[]{#_Toc335035658}[]{#_Toc335035659}[]{#_Toc335035660}[]{#_Toc335035661}[]{#_Toc335035663}[]{#_Toc335035664}[]{#_Toc335035665}[]{#_Toc335035666}[]{#_Toc335035667}[]{#_Toc335035668}[]{#_Toc335035669}[]{#_Toc335035670}[]{#_Toc335035671}[]{#_Toc335035673}[]{#_Toc335035674}[]{#_Toc335035675}[]{#_Toc335035676}[]{#_Toc335035678}[]{#_Toc335035679}[]{#_Toc335035680}[]{#_Toc335035681}[]{#_Toc335035682}[]{#_Toc335035683}[]{#_Toc335035684}[]{#_Toc335035685}[]{#_Toc335035686}[]{#_Toc335035687}[]{#_Toc335035688}[]{#_Toc335035689}[]{#_Toc335035690}[]{#_Toc335035692}[]{#_Toc335035694}[]{#_Toc335035695}[]{#_Toc335035696}[]{#_Toc335035697}[]{#_Toc335035699}[]{#_Toc335035700}[]{#_Toc335035701}[]{#_Toc335035702}[]{#_Toc335035703}[]{#_Toc335035704}[]{#_Toc335035705}[]{#_Toc335035706}[]{#_Toc335035707}[]{#_Toc335035708}[]{#_Toc335035709}[]{#_Toc335035711}

**GOLD \-- GOLD配置命令 \-- diagnostic ondemand stop**

------------------------------------------------------------------------

[**[diagnostic ondemand stop]{lang="EN-US"}**]{#struct_0_x9799_x9248_x335774093}[命令用来停止指定按需类型诊断。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624950181}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_892705318}

[**[diagnostic ondemand stop test]{lang="EN-US"}**[ { **non-disruptive** \| ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1704350910}*[test-name]{lang="EN-US"}*[ }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_x56028664}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[]{#OLE_LINK24}[]{#OLE_LINK23}[**[diagnostic ondemand stop slot]{lang="EN-US"}**]{#struct_0_x9799_x9248_433249343}*[ ]{lang="EN-US"}[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** { **non-disruptive** \| ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_x1961921226}[模式：]{style="font-family:宋体"}

[**[diagnostic ondemand stop chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_501260480}*[chassis-number]{lang="EN-US"}*[ **slot**]{lang="EN-US"}*[ slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** { **non-disruptive** \| ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1819395923}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2044304613}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_623967141}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x979992106}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1226501146}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_605792212}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时执行多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1727717637}*[slot-number-list]{lang="EN-US"}*[：成员编号列表，表示同时执行多个成员设备的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213338326}*[slot-number-list]{lang="EN-US"}*[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时执行多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x685545775}*[chassis-number]{lang="EN-US"}*[：表示需要执行测试例的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x642198318}*[chassis-number]{lang="EN-US"}*[：表示需要执行测试例的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1818129450}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时执行多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1788917153}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时执行多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要执行的单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[test-name]{lang="EN-US"}*]{#struct_0_x9799_x9248_x427618875}[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[non-disruptive]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1937004941}[：执行所有的非破坏性的测试例。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x969861461}*[cpu-number]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_612670109}

[[用户可以通过命令行配置按需诊断测试例重复执行的次数以及累计失败执行次数的最大值。当用户开启某测试例后，测试例在执行过程中，只要达到上述任意条件，则立即自动停止执行。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_624032677}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_746547729}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1949657494}[手动停止执行非破坏性测试例。（集中式模式）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand stop test non-disruptive]{lang="EN-US"}]{#struct_0_x9799_x9248_x167969644}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_624491426}[在]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上手动停止执行非破坏性测试例。（分布式设备－独立运行模式]{style="font-family:
宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand stop slot 1 test non-disruptive]{lang="EN-US"}]{#struct_0_x9799_x9248_868766862}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_624556962}[在成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上手动停止执行非破坏性测试例。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand stop slot 1 test non-disruptive]{lang="EN-US"}]{#struct_0_x9799_x9248_x3588355}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1996410057}[在成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上手动停止执行非破坏性测试例。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> diagnostic ondemand stop chassis 2 slot 1 test non-disruptive]{lang="EN-US"}]{#struct_0_x9799_x9248_624622498}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1964616789}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand fail]{lang="EN-US"}**]{#struct_0_x9799_x9248_394935166}**[ure]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand repeating]{lang="EN-US"}**]{#struct_0_x9799_x9248_x595087480}
:::

::: {#-572481559 .myid}
[]{#_Toc404797477}[]{#struct_0_x9799_x9248_x982935085}[]{#_Toc334794712}

**GOLD \-- GOLD配置命令 \-- diagnostic simulation**

------------------------------------------------------------------------

[**[diagnostic simulation]{lang="EN-US"}**]{#struct_0_x9799_x9248_x966685602}[命令用来设置诊断的执行方式为模拟方式。]{style="font-family:宋体"}

[**[undo diagnostic simulation]{lang="EN-US"}**]{#struct_0_x9799_x9248_1620273293}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x2030464533}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x387887153}

[**[diagnostic simulation test]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_624688034}*[test-name]{lang="EN-US"}*[ { **failure** \| **random-failure** \| **success** }]{lang="EN-US"}

[**[undo diagnostic simulation test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2043926699}*[test-name]{lang="EN-US"}*

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_2097790591}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[diagnostic simulation slot]{lang="EN-US"}**]{#struct_0_x9799_x9248_1777486852}*[ ]{lang="EN-US"}[slot-number-list ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\]]{lang="EN-US"}*[ ]{lang="EN-US"}***[test]{lang="EN-US"}**[ ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ { **failure** \| **random-failure** \| **success** }]{lang="EN-US"}

[**[undo diagnostic simulation slot]{lang="EN-US"}**]{#struct_0_x9799_x9248_1601105953}*[ ]{lang="EN-US"}[slot-number-list ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_996895444}[模式：]{style="font-family:宋体"}

[**[diagnostic simulation chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1847936301}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ { **failure** \| **random-failure** \| **success** }]{lang="EN-US"}

[**[undo diagnostic simulation chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_624753570}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number-list]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1550436283}

[[诊断为非模拟方式。即启动测试例后，系统会真正执行该测试例。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_120613106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1447585688}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1476811504}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_802078564}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x1591939183}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_67466518}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_470656969}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时模拟多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要模拟的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x459069323}*[slot-number-list]{lang="EN-US"}*[：成员编号列表，表示同时模拟多个成员设备的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要模拟的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213076182}*[slot-number-list]{lang="EN-US"}*[：成员编号]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[虚拟槽位号列表，表示同时模拟多个成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要模拟的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_624819106}*[chassis-number]{lang="EN-US"}*[：表示需要模拟测试例的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1090118264}*[chassis-number]{lang="EN-US"}*[：表示需要模拟测试例的设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1435788659}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时模拟多个单板的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要模拟的单板所在的槽位号。]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1723092040}*[slot-number-list]{lang="EN-US"}*[：槽位号列表，表示同时模拟多个单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例。表示方式为]{style="font-family:宋体"}*[slot-number-list]{lang="EN-US"}*[ ]{lang="EN-US"}*[=]{lang="EN-US"}*[ { ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[to]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[ \] }&\<1-7\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示需要模拟的单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号，]{style="font-family:宋体"}[&\<1-7\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[7]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[*[test-name]{lang="EN-US"}*]{#struct_0_x9799_x9248_347596311}[：指定进行模拟诊断的测试例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[failure]{lang="EN-US"}**]{#struct_0_x9799_x9248_1337040890}[：假设模拟执行测试例失败，此时将输出测试失败的结果。]{style="font-family:宋体"}

[**[random-failure]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1045949166}[：表示随机选择模拟执行测试例的结果是成功还是失败。]{style="font-family:宋体"}

[**[success]{lang="EN-US"}**]{#struct_0_x9799_x9248_x344622589}[：假设模拟执行测试例成功，此时将输出测试成功的结果。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x970123606}*[cpu-number]{lang="EN-US"}*[：表示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1009723490}

[[配置该命令后，当测试例满足执行条件时，在执行测试例的时候就直接生成测试结果，并不真正执行测试例，也不会触发硬件纠正行为。该功能用于判断]{style="font-family:宋体"}[GOLD]{lang="EN-US"}]{#struct_0_x9799_x9248_x1857900825}[模块框架功能是否正常。]{style="font-family:宋体"}

[[只有监控诊断测试例和按需诊断测试例支持该命令，启动诊断测试例不支持该命令。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1693463600}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624884642}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_178678713}[配置]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[模拟诊断失败。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> diagnostic simulation test HGMonitor failure]{lang="EN-US"}]{#struct_0_x9799_x9248_x171322146}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x685905064}[配置]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[模拟诊断失败。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> diagnostic simulation slot 1 test HGMonitor failure]{lang="EN-US"}]{#struct_0_x9799_x9248_x635597741}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_562005158}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[模拟诊断失败。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> diagnostic simulation slot 1 test HGMonitor failure]{lang="EN-US"}]{#struct_0_x9799_x9248_x1240426626}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1979615237}[配置成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的]{style="font-family:
宋体"}[HGMonitor]{lang="EN-US"}[模拟诊断失败。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> diagnostic simulation chassis 1 slot 1 test HGMonitor failure]{lang="EN-US"}]{#struct_0_x9799_x9248_x1161288430}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624950178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display diagnostic simulation]{lang="EN-US"}**]{#struct_0_x9799_x9248_937335327}
:::

::: {#-1821703336 .myid}
[]{#_Toc404797478}[]{#struct_0_x9799_x9248_x1115559161}[]{#_Toc392579826}

**GOLD \-- GOLD配置命令 \-- display diagnostic bootup**

------------------------------------------------------------------------

[**[display diagnostic bootup]{lang="EN-US"}**]{#struct_0_x9799_x9248_689860902}[命令用来显示启动诊断测试例。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_2127634573}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x586394312}

[**[display diagnostic bootup ]{lang="EN-US"}**[\[ **test** ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1247930605}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_x1746914526}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display diagnostic bootup]{lang="EN-US"}**[ \[ **slot** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1608047504}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \[ **test** ]{lang="EN-US"}*[test-name ]{lang="EN-US"}*[\] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_1607369146}[模式：]{style="font-family:宋体"}

[**[display diagnostic bootup ]{lang="EN-US"}**[\[ **chassis** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1373257091}*[chassis-number ]{lang="EN-US"}*[\[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \] \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1372552263}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1613324194}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1373099946}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x2069292136}

[[network-operator]{lang="EN-US"}]{#struct_0_x9799_x9248_982697605}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x699438688}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_38175060}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[表示单板所在的槽位号。不指定该参数时，显示所有单板上测试例的执行结果。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1173561759}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定]{style="font-family:宋体"}[该参数]{style="font-family:宋体"}[时，显示所有成员设备上测试例的执行结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_22942194}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定]{style="font-family:宋体"}[该参数]{style="font-family:宋体"}[时，显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上测试例的执行结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1121136410}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示所有成员设备]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟设备上测试例的诊断结果。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数时，显示指定成员设备所有单板或者指定虚拟设备所有]{style="font-family:宋体"}[PEX]{lang="EN-US"}[上测试例的执行结果。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_2111916684}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有测试例。（集中式设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_2107105417}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有测试例。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_827153934}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有测试例。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x190303020}*[cpu-number]{lang="EN-US"}*[：表示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x788740107}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_47240253}[显示启动诊断测试例]{style="font-family:宋体"}[OnlyBootUp]{lang="EN-US"}[的信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display diagnostic bootup test OnlyBootUp]{lang="EN-US"}]{#struct_0_x9799_x9248_1645462959}

[Test name                : OnlyBootUp]{lang="EN-US"}

[ExtPara                  : 123]{lang="EN-US"}

[State                    : Enabled]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x942188008}[显示]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板上启动诊断测试例]{style="font-family:宋体"}[OnlyBootUp]{lang="EN-US"}[的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display diagnostic bootup slot 0]{lang="EN-US"}]{#struct_0_x9799_x9248_x183650909}

[slot 0:]{lang="EN-US"}

[  Test name                : OnlyBootUp]{lang="EN-US"}

[  ExtPara                  : 123]{lang="EN-US"}

[  State                    : Enabled]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1031781076}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上启动诊断测试例的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display diagnostic bootup slot 1]{lang="EN-US"}]{#struct_0_x9799_x9248_x1518843688}

[slot 1:]{lang="EN-US"}

[  Test name                : OnlyBootUp]{lang="EN-US"}

[  ExtPara                  : 123]{lang="EN-US"}

[  State                    : Enabled]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x880850424}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板上启动诊断测试例的信息。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display diagnostic bootup chassis 1 slot 0]{lang="EN-US"}]{#struct_0_x9799_x9248_1737508208}

[Chassis 1 slot 0:]{lang="EN-US"}

[  Test name                : OnlyBootUp]{lang="EN-US"}

[  ExtPara                  : 123]{lang="EN-US"}

[  State                    : Enabled]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1399961935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic bootup ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1612112618}**[enable test]{lang="EN-US"}**
:::

::: {#-1955430282 .myid}
[]{#_Toc404797479}[]{#struct_0_x9799_x9248_x1334261812}

**GOLD \-- GOLD配置命令 \-- display diagnostic bootup level**

------------------------------------------------------------------------

[**[display diagnostic bootup level]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1419658048}[命令用来显示设备本次启动时生效的启动诊断的级别。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1330483189}

[**[display diagnostic bootup level]{lang="EN-US"}**]{#struct_0_x9799_x9248_1651689578}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x655469306}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1064313541}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1841213884}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_623967138}

[[network-operator]{lang="EN-US"}]{#struct_0_x9799_x9248_2123334093}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1981371479}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_746908719}[显示设备本次启动时生效的启动诊断的级别。]{style="font-family:宋体"}

[[\<sysname\> display diagnostic bootup level]{lang="EN-US"}]{#struct_0_x9799_x9248_70740618}

[Current bootup diagnostic level: complete]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_80981993}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic bootup level ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1112526779}
:::

::: {#1845298034 .myid}
[]{#_Toc404797480}[]{#struct_0_x9799_x9248_x872435710}

**GOLD \-- GOLD配置命令 \-- display diagnostic content**

------------------------------------------------------------------------

[**[display diagnostic content]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2065145777}[命令用来显示测试例的内容。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624032674}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_746547728}

[**[display diagnostic content]{lang="EN-US"}**[ \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x9799_x9248_1949657495}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_x168035180}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display diagnostic content]{lang="EN-US"}**[ \[ **slot** ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1399625889}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_832935434}[模式：]{style="font-family:宋体"}

[**[display diagnostic content]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **chassis** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1021541218}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1235638311}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1168597109}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624491427}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_868766861}

[[network-operator]{lang="EN-US"}]{#struct_0_x9799_x9248_1674505215}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x767061453}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1501795575}*[slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定时，显示所有板的测试例内容。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1672571528}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定时，显示所有设备的测试例内容。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213666005}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定时，显示所有设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例内容。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_624622499}*[chassis-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\]]{lang="EN-US"}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示所有诊断结果。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[未指定槽位号时，显示指定设备所有单板的测试例内容。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1219078677}*[chassis-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\]]{lang="EN-US"}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示所有诊断结果。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[未指定槽位号时，显示指定设备所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的测试例内容。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1964616788}[：显示测试例的详细信息；不指定该参数时，显示测试例的简要信息。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_x969926998}*[cpu-number]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1961019107}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x286383217}[显示诊断测试例的简要信息。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic content]{lang="EN-US"}]{#struct_0_x9799_x9248_624753571}

[Diagnostic test suite attributes:]{lang="EN-US"}

[#B/\*: Bootup test/NA]{lang="EN-US"}

[#O/\*: Ondemand test/NA]{lang="EN-US"}

[#M/\*: Monitoring test/NA]{lang="EN-US"}

[#D/\*:[]{#OLE_LINK6} [Disruptive]{#OLE_LINK5} test/Non-[]{#OLE_LINK12}[disruptive]{#OLE_LINK11} test]{lang="EN-US"}

[#P/\*: Per port test[]{#OLE_LINK20}[/NA]{#OLE_LINK17}]{lang="EN-US"}

[#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Name                      Attributes              Interval]{lang="EN-US"}

[[HGMonitor]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}[                              ]{lang="EN-US"}[[\*\*M\*PI]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}[                               ]{lang="EN-US"}[[00:00:10]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}

[]{#OLE_LINK10}[[BoardSteady]{lang="EN-US"}]{#OLE_LINK9}[               B\*\*\*\*\*                  -NA-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1550436282}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上诊断测试例的简要信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic content slot 1]{lang="EN-US"}]{#struct_0_x9799_x9248_624819107}

[Diagnostic test suite attributes:]{lang="EN-US"}

[#B/\*: Bootup test/NA]{lang="EN-US"}

[#O/\*: Ondemand test/NA]{lang="EN-US"}

[#M/\*: Monitoring test/NA]{lang="EN-US"}

[#D/\*: Disruptive test/Non-disruptive test]{lang="EN-US"}

[#P/\*: Per port test/NA]{lang="EN-US"}

[#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 1 cpu 0:]{lang="EN-US"}

[Name                      Attributes              Interval]{lang="EN-US"}

[[HGMonitor]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}[                              ]{lang="EN-US"}[[\*\*M\*PI]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}[                               ]{lang="EN-US"}[[00:00:10]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}

[BoardSteady               B\*\*\*\*\*                  -NA-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1435788660}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上诊断测试例的简要信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic content slot 1]{lang="EN-US"}]{#struct_0_x9799_x9248_624884643}

[Diagnostic test suite attributes:]{lang="EN-US"}

[#B/\*: Bootup test/NA]{lang="EN-US"}

[#O/\*: Ondemand test/NA]{lang="EN-US"}

[#M/\*: Monitoring test/NA]{lang="EN-US"}

[#D/\*: Disruptive test/Non-disruptive test]{lang="EN-US"}

[#P/\*: Per port test/NA]{lang="EN-US"}

[#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 1 cpu 0:]{lang="EN-US"}

[Name                      Attributes              Interval]{lang="EN-US"}

[[HGMonitor]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}[                              ]{lang="EN-US"}[[\*\*M\*PI]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}[                               ]{lang="EN-US"}[[00:00:10]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}

[BoardSteady               B\*\*\*\*\*                  -NA-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_178678714}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上诊断测试例的简要信息。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic content chassis 1 slot 1]{lang="EN-US"}]{#struct_0_x9799_x9248_624950179}

[Diagnostic test suite attributes:]{lang="EN-US"}

[#B/\*: Bootup test/NA]{lang="EN-US"}

[#O/\*: Ondemand test/NA]{lang="EN-US"}

[#M/\*: Monitoring test/NA]{lang="EN-US"}

[#D/\*: Disruptive test/Non-disruptive test]{lang="EN-US"}

[#P/\*: Per port test/NA]{lang="EN-US"}

[#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 1 slot 1 cpu 0:]{lang="EN-US"}

[Name                      Attributes              Interval]{lang="EN-US"}

[[HGMonitor]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}[                             ]{lang="EN-US"}[[\*\*M\*PI]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}[                                ]{lang="EN-US"}[[00:00:10]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}

[BoardSteady               B\*\*\*\*\*                  -NA-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_937335326}[显示诊断测试例的详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic content verbose]{lang="EN-US"}]{#struct_0_x9799_x9248_623967139}

[Diagnostic test suite attributes:]{lang="EN-US"}

[#B/\*: Bootup test/NA]{lang="EN-US"}

[#O/\*: Ondemand test/NA]{lang="EN-US"}

[#M/\*: Monitoring test/NA]{lang="EN-US"}

[#D/\*: Disruptive test/Non-disruptive test]{lang="EN-US"}

[#P/\*: Per port test/NA]{lang="EN-US"}

[#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Test name        : HGMonitor]{lang="EN-US"}

[Test attributes  : \*\*M\*PI]{lang="EN-US"}

[Test interval    : 00:00:10]{lang="EN-US"}

[Min interval     : 00:00:10]{lang="EN-US"}

[Correct-action   : -NA-]{lang="EN-US"}

[Description       : A Real-time test, disabled by default that checks link status between ports.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Test name        : BoardSteady]{lang="EN-US"}

[Test attributes  : B\*\*\*\*\*]{lang="EN-US"}

[Test interval    : -NA-]{lang="EN-US"}

[Min interval     : -NA-]{lang="EN-US"}

[Correct-action   : Offline.]{lang="EN-US"}

[Description       : A bootup test, to check if the board is steady inserted. If the board is not steady inserted, the board will be offline.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_2123334094}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上诊断测试例的详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic content slot 1 verbose]{lang="EN-US"}]{#struct_0_x9799_x9248_624491424}

[Diagnostic test suite attributes:]{lang="EN-US"}

[#B/\*: Bootup test/NA]{lang="EN-US"}

[#O/\*: Ondemand test/NA]{lang="EN-US"}

[#M/\*: Monitoring test/NA]{lang="EN-US"}

[#D/\*: Disruptive test/Non-disruptive test]{lang="EN-US"}

[#P/\*: Per port test/NA]{lang="EN-US"}

[#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Slot 1 cpu 0:]{lang="EN-US"}

[Test name        : HGMonitor]{lang="EN-US"}

[Test attributes  : \*\*M\*PI]{lang="EN-US"}

[Test interval    : 00:00:10]{lang="EN-US"}

[Min interval     : 00:00:10]{lang="EN-US"}

[Correct-action   : -NA-]{lang="EN-US"}

[Description       : A Real-time test, disabled by default that checks link status between ports.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Test name        : BoardSteady]{lang="EN-US"}

[Test attributes  : B\*\*\*\*\*]{lang="EN-US"}

[Test interval    : -NA-]{lang="EN-US"}

[Min interval     : -NA-]{lang="EN-US"}

[Correct-action   : Offline.]{lang="EN-US"}

[Description       : A bootup test, to check if the board is steady inserted. If the board is not steady inserted, the board will be offline.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_868766864}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上诊断测试例的详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic content slot 1 verbose]{lang="EN-US"}]{#struct_0_x9799_x9248_624622496}

[Diagnostic test suite attributes:]{lang="EN-US"}

[#B/\*: Bootup test/NA]{lang="EN-US"}

[#O/\*: Ondemand test/NA]{lang="EN-US"}

[#M/\*: Monitoring test/NA]{lang="EN-US"}

[#D/\*: Disruptive test/Non-disruptive test]{lang="EN-US"}

[#P/\*: Per port test/NA]{lang="EN-US"}

[#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA]{lang="EN-US"}

[ ]{lang="EN-US"}

[slot 1 cpu 0:]{lang="EN-US"}

[Test name        : HGMonitor]{lang="EN-US"}

[Test attributes  : \*\*M\*PI]{lang="EN-US"}

[Test interval    : 00:00:10]{lang="EN-US"}

[Min interval     : 00:00:10]{lang="EN-US"}

[Correct-action   : -NA-]{lang="EN-US"}

[Description      : A real-time test that checks HG channel status, disabled by default.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Test name        : BoardSteady]{lang="EN-US"}

[Test attributes  : B\*\*\*\*\*]{lang="EN-US"}

[Test interval    : -NA-]{lang="EN-US"}

[Min interval     : -NA-]{lang="EN-US"}

[Correct-action   : Offline.]{lang="EN-US"}

[Description       : A bootup test, to check if the board is steady inserted. If the board is not steady inserted, the board will be offline.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1964616795}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上诊断测试例的详细信息。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic content chassis 1 slot 1 verbose]{lang="EN-US"}]{#struct_0_x9799_x9248_624688032}

[Diagnostic test suite attributes:]{lang="EN-US"}

[#B/\*: Bootup test/NA]{lang="EN-US"}

[#O/\*: Ondemand test/NA]{lang="EN-US"}

[#M/\*: Monitoring test/NA]{lang="EN-US"}

[#D/\*: Disruptive test/Non-disruptive test]{lang="EN-US"}

[#P/\*: Per port test/NA]{lang="EN-US"}

[#A/I/\*: Monitoring test is active/Monitoring test is inactive/NA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis 1 slot 1 cpu 0:]{lang="EN-US"}

[Test name        : HGMonitor]{lang="EN-US"}

[Test attributes  : \*\*M\*PI]{lang="EN-US"}

[Test interval    : 00:00:10]{lang="EN-US"}

[Min interval     : 00:00:10]{lang="EN-US"}

[Correct-action   : -NA-]{lang="EN-US"}

[Description       : A real-time test that checks HG channel status, disabled by default.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Test name        : BoardSteady]{lang="EN-US"}

[Test attributes  : B\*\*\*\*\*]{lang="EN-US"}

[Test interval    : -NA-]{lang="EN-US"}

[Min interval     : -NA-]{lang="EN-US"}

[Correct-action   : Offline.]{lang="EN-US"}

[Description       : A bootup test, to check if the board is steady inserted. If the board is not steady inserted, the board will be offline.]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display diagnostic content]{lang="EN-US"}]{#struct_0_x9799_x9248_x2043926693}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x927204014}[[字段]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624753568}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x405878861}

[[B/\*]{lang="EN-US"}]{#struct_0_x9799_x9248_x682125636}

[[启动诊断测试例]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_x2065527954}[非启动诊断测试例]{style="font-family:宋体"}

[[O/\*]{lang="EN-US"}]{#struct_0_x9799_x9248_163983542}

[[按需诊断测试例]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_712559885}[非按需诊断测试例]{style="font-family:宋体"}

[[M/\*]{lang="EN-US"}]{#struct_0_x9799_x9248_x913719660}

[[监控诊断测试例]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_624819104}[非监控诊断测试例]{style="font-family:宋体"}

[[D/\*]{lang="EN-US"}]{#struct_0_x9799_x9248_x1435788657}

[[破坏性测试例]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_x815203103}[非破坏性测试例]{style="font-family:宋体"}

[[P/\*]{lang="EN-US"}]{#struct_0_x9799_x9248_637957162}

[[端口相关的测试例]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_x1367760352}[不是端口相关的测试例]{style="font-family:宋体"}

[[A/I/\*]{lang="EN-US"}]{#struct_0_x9799_x9248_1551118713}

[[使能的监控诊断测试例]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_624884640}[未使能的监控诊断测试例]{style="font-family:宋体"}[/]{lang="EN-US"}[非监控诊断测试例]{style="font-family:宋体"}

[[Slot 1 cpu 0]{lang="EN-US"}]{#struct_0_x9799_x9248_x969992535}

[[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x9799_x9248_x842331426}[上测试例的内容（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis 1 slot 1 cpu 0]{lang="EN-US"}]{#struct_0_x9799_x9248_x970582359}

[[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x9799_x9248_x970647895}[上测试例的内容（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Test name]{lang="EN-US"}]{#struct_0_x9799_x9248_178678711}

[[测试例的名称]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x171322144}

[[Test attributes]{lang="EN-US"}]{#struct_0_x9799_x9248_x686036136}

[[测试例的属性。从左到右依次为是否为启动诊断测试例，是否为按需诊断测试例，是否为监控诊断测试例，是否是破坏性测试例，是否是端口都相关的测试例，是否使能，对于不相关的属性用"]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_x9799_x9248_1593060670}["表示]{style="font-family:宋体"}

[[Test interval]{lang="EN-US"}]{#struct_0_x9799_x9248_624950176}

[[执行监控测试例的时间间隔，没有时间间隔用"]{style="font-family:宋体"}[-NA-]{lang="EN-US"}]{#struct_0_x9799_x9248_937335329}["表示]{style="font-family:宋体"}

[[Min interval]{lang="EN-US"}]{#struct_0_x9799_x9248_x1334261802}

[[执行监控测试例允许的最小时间间隔，没有最小时间间隔用"]{style="font-family:宋体"}[-NA-]{lang="EN-US"}]{#struct_0_x9799_x9248_x1419723584}["表示]{style="font-family:宋体"}

[[Correct-action]{lang="EN-US"}]{#struct_0_x9799_x9248_375511551}

[[测试失败时的触发动作]{style="font-family:宋体"}]{#struct_0_x9799_x9248_623967136}

[[Description]{lang="EN-US"}]{#struct_0_x9799_x9248_2123334095}

[[测试例的描述信息]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1981764695}

[ ]{lang="EN-US"}

::: {#-1411774965 .myid}
[]{#_Toc404797481}[]{#struct_0_x9799_x9248_722749814}[]{#_Toc335137372}

**GOLD \-- GOLD配置命令 \-- display diagnostic event-log**

------------------------------------------------------------------------

[**[display diagnostic event]{lang="EN-US"}[-log]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1383874998}[命令用来显示]{style="font-family:
宋体"}[GOLD]{lang="EN-US"}[日志的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_2123983155}

[]{#OLE_LINK53}[]{#OLE_LINK52}[**[display diagnostic event]{lang="EN-US"}[-log ]{lang="EN-US"}**[\[ **error** \| **info** \]]{lang="EN-US"}]{#struct_0_x9799_x9248_1550287842}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_624032672}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_746547726}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1949657497}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x167904108}

[[network-operator]{lang="EN-US"}]{#struct_0_x9799_x9248_x28445675}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1980771875}

[**[error]{lang="EN-US"}**]{#struct_0_x9799_x9248_x801510477}[：显示所有错误相关的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_x9799_x9248_x24383162}**[：]{style="font-family:宋体"}**[显示所有非错误的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志信息]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1381464465}

[[不指定]{style="font-family:宋体"}**[error]{lang="EN-US"}**]{#struct_0_x9799_x9248_x812300394}[和]{style="font-family:宋体"}**[info]{lang="EN-US"}**[参数时，显示所有]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的信息。]{style="font-family:宋体"}

[[系统在执行完诊断测试例后，会产生]{style="font-family:宋体"}[GOLD]{lang="EN-US"}]{#struct_0_x9799_x9248_624491425}[日志用于记录测试例相关执行情况，日志内容包括测试例的名称、执行时间、执行结果、失败原因等信息。由于所有测试例在执行过程都会产生日志，因此]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志会较多，为了不影响信息中心的性能，]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志独立存储和显示，不会发往信息中心统一处理。]{style="font-family:宋体"}

[[设备重启或主备倒换后，]{style="font-family:宋体"}[GOLD]{lang="EN-US"}]{#struct_0_x9799_x9248_624556961}[日志会全部被清除掉。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x3588354}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x342242103}[显示所有]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic event-log]{lang="EN-US"}]{#struct_0_x9799_x9248_x10147978}

[Event: E_INFO, Wed Jan  7 11:39:53:314 2012, -Chassis=4-Slot=2-Cpu=0 TestName-\>SystemMgmtBus, Event_INFO: Result-\>Success.]{lang="EN-US"}

[Event: E_ERROR, Wed Jan  7 11:39:53:314 2012, -Chassis=4-Slot=2-Cpu=0 [TestName-\>SystemMgmtBus, Event_INFO: Result-\>Failure Reason-\>The port 9 is offline.]{.TerminalDisplayChar}]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_383257309}[显示所有错误相关的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic event-log error]{lang="EN-US"}]{#struct_0_x9799_x9248_x334331502}

[[Event: E_ERROR, Wed Jan  7 11:39:53:314 2012, -Chassis=4-Slot=2-Cpu=0 TestName-\>SystemMgmtBus, Event_INFO: Result-\>Failure Reason-\>The port 9 is offline.]{lang="EN-US"}]{#struct_0_x9799_x9248_1023110551}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1351928890}[显示所有非错误的]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic event-log info]{lang="EN-US"}]{#struct_0_x9799_x9248_624622497}

[[Event: E_INFO, Wed Jan  7 11:39:53:314 2012, -Chassis=4-Slot=2-Cpu=0 TestName-\>SystemMgmtBus, Event_INFO: Result-\>Success.]{lang="EN-US"}]{#struct_0_x9799_x9248_x1964616794}
:::

::: {#-1168548627 .myid}
[]{#_Toc404797482}[]{#struct_0_x9799_x9248_x8283825}

**GOLD \-- GOLD配置命令 \-- display diagnostic ondemand configuration**

------------------------------------------------------------------------

[**[display diagnostic ondemand configuration]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1371272240}[命令用来显示按需诊断的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1795242185}

[**[display diagnostic ondemand configuration]{lang="EN-US"}**]{#struct_0_x9799_x9248_484536240}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_296961406}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x889710085}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_400835861}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_624688033}

[[network-operator]{lang="EN-US"}]{#struct_0_x9799_x9248_x2043926692}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x987323124}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1181691920}[配置了重复执行次数与失败次数，显示按需诊断配置信息。]{style="font-family:宋体"}

[[\<sysname\> display diagnostic ondemand configuration]{lang="EN-US"}]{#struct_0_x9799_x9248_425985345}

[Maximum test-repeating times: 4]{lang="EN-US"}

[Maximum test-failure times: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1865527506}[只配置了重复执行次数，显示按需诊断配置信息。]{style="font-family:宋体"}

[[\<sysname\> display diagnostic ondemand configuration ]{lang="EN-US"}]{#struct_0_x9799_x9248_767001446}

[Maximum test-repeating times: 4]{lang="EN-US"}

[Maximum test-failure times: Not configured]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1043262958}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand fail]{lang="EN-US"}**]{#struct_0_x9799_x9248_624753569}**[ure]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic ondemand repeating]{lang="EN-US"}**]{#struct_0_x9799_x9248_x405878862}
:::

::: {#819164749 .myid}
[]{#_Toc404797483}[]{#struct_0_x9799_x9248_x682322244}[]{#_Toc334794720}

**GOLD \-- GOLD配置命令 \-- display diagnostic result**

------------------------------------------------------------------------

[**[display diagnostic result]{lang="EN-US"}**]{#struct_0_x9799_x9248_1071930222}[命令用来显示测试例的执行结果。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1071395806}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1256549637}

[**[display diagnostic result ]{lang="EN-US"}**[\[ **test** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1242992033}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}[ []{#OLE_LINK125}[\[ **verbose** \]]{#OLE_LINK124}]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_2127714680}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display diagnostic result]{lang="EN-US"}**[ \[ **slot** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1365791948}*[slot-number]{lang="EN-US"}*[ \[ **test** ]{lang="EN-US"}*[test-name ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] []{#OLE_LINK28}[\]]{#OLE_LINK27} \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_624819105}[模式：]{style="font-family:宋体"}

[**[display diagnostic result ]{lang="EN-US"}**[\[ **chassis** ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1435788658}*[chassis-number ]{lang="EN-US"}*[\[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \] \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1218487630}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1741689437}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1641815638}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x734862081}

[[network-operator]{lang="EN-US"}]{#struct_0_x9799_x9248_1517341780}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x60321628}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_857594349}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[表示单板所在的槽位号。不指定该参数时，显示所有单板上测试例的执行结果。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_624884641}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定]{style="font-family:宋体"}[该参数]{style="font-family:宋体"}[时，显示所有成员设备上测试例的执行结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213469396}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定]{style="font-family:宋体"}[该参数]{style="font-family:宋体"}[时，显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上测试例的执行结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_178678712}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示所有成员设备上测试例的诊断结果。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数时，显示指定成员设备所有单板上测试例的执行结果。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213403860}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示所有测试例的诊断结果。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数时，显示指定成员设备所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上测试例的执行结果。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x171322145}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有测试例。（集中式设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x685970600}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有测试例。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x236894898}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有测试例。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x9799_x9248_1557991602}[：]{style="font-family:宋体"}[显示当前处于使能状态的测试例或者累计执行次数大于]{style="font-family:宋体"}[0]{lang="EN-US"}[的测试例执行结果的详细信息，不包括统计信息。不指定该参数时，只显示累计执行次数大于]{style="font-family:宋体"}[0]{lang="EN-US"}[的测试例执行结果的简要信息。]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_1758956360}*[cpu-number]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1683599182}

[]{#OLE_LINK69}[]{#OLE_LINK68}[]{#OLE_LINK79}[]{#OLE_LINK78}[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1645984103}[显示设备中所有测试例的简要诊断结果。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result]{lang="EN-US"}]{#struct_0_x9799_x9248_624950177}

[  Name                    Run count    Failure count    Last result]{lang="EN-US"}

[  HGMonitor               10           3                Failure]{lang="EN-US"}

[  SystemMgmtBus           10           0                Success]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_937335328}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上所有测试例的简要诊断结果。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result slot 1]{lang="EN-US"}]{#struct_0_x9799_x9248_623967137}

[Slot 1 cpu 0]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Name                    Run count    Failure count    Last result]{lang="EN-US"}

[  HGMonitor               10           3                Failure]{lang="EN-US"}

[  SystemMgmtBus           10           0                Success]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_624032673}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上所有测试例的简要诊断结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result slot 1]{lang="EN-US"}]{#struct_0_x9799_x9248_746547725}

[Slot 1 cpu 0]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Name                    Run count    Failure count    Last result]{lang="EN-US"}

[  HGMonitor               10           3                Failure ]{lang="EN-US"}

[  SystemMgmtBus           10           0                Success]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104326391}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[中]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上所有测试例的简要诊断结果。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result chassis 1 slot 1]{lang="EN-US"}]{#struct_0_x9799_x9248_x711455788}

[Chassis 1 slot 1 cpu 0]{lang="EN-US"}[：]{style="font-family:宋体"}

[  Name                    Run count    Failure count    Last result]{lang="EN-US"}

[  HGMonitor               10           3                Failure ]{lang="EN-US"}

[  SystemMgmtBus           10           0                Success]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_2061774965}[显示所有测试例的详细诊断结果[]{#OLE_LINK14}[（分布式设备－独立运行模式]{#OLE_LINK13}]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result verbose]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104195319}

[Slot 1 cpu 0:]{lang="EN-US"}

[  Test name                : HGMonitor]{lang="EN-US"}

[  Total run count          : 10]{lang="EN-US"}

[  Total failure count      : 3]{lang="EN-US"}

[  Consecutive failure count: 3]{lang="EN-US"}

[  Last execution time      : Tue Oct 30 10:36:55 2012]{lang="EN-US"}

[  First failure time       : Tue Oct 30 10:36:25 2012]{lang="EN-US"}

[  Last failure time        : Tue Oct 30 10:36:55 2012]{lang="EN-US"}

[  Last pass time           : Tue Oct 30 10:36:15 2012]{lang="EN-US"}

[  Last execution result    : Failure]{lang="EN-US"}

[  Last failure reason      : Failed to send packets.]{lang="EN-US"}

[  Next execution time      : Tue Oct 30 10:37:05 2012]{lang="EN-US"}

[  Port link status : error]{lang="EN-US"}

[  Src-Slot Unit      Port      Dest-Slot ]{lang="EN-US"}

[  8        20        3         14]{lang="EN-US"}

[  8        23        5         14]{lang="EN-US"}

[  6        10        3         14]{lang="EN-US"}

[  14       3         13        7]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Test name                : SystemMgmtBus]{lang="EN-US"}

[  Total run count          : 10]{lang="EN-US"}

[  Total failure count      : 0]{lang="EN-US"}

[  Consecutive failure count: 0]{lang="EN-US"}

[  Last execution time      : Tue Oct 30 10:36:55 2012]{lang="EN-US"}

[  First failure time       : -NA-]{lang="EN-US"}

[  Last failure time        : -NA-]{lang="EN-US"}

[  Last pass time           : Tue Oct 30 10:36:55 2012]{lang="EN-US"}

[  Last execution result    : Success]{lang="EN-US"}

[  Last failure reason      : -NA- ]{lang="EN-US"}

[  Next execution time      : -NA-]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display diagnostic result]{lang="EN-US"}]{#struct_0_x9799_x9248_x1056576423}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x931218734}[[字段]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1308965184}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1603523589}

[[Slot 1 cpu 0]{lang="EN-US"}]{#struct_0_x9799_x9248_1759087431}

[[指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x9799_x9248_1759021895}[上测试例的执行结果（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis 1 slot 1 cpu 0]{lang="EN-US"}]{#struct_0_x9799_x9248_1758956359}[：]{style="font-family:宋体"}

[[指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x9799_x9248_1758890823}[上测试例的执行结果（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Test name]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104129783}

[[测试例的名称]{style="font-family:宋体"}]{#struct_0_x9799_x9248_580842766}

[[Total run count]{lang="EN-US"}]{#struct_0_x9799_x9248_x200052415}

[[诊断执行的总次数]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2103998711}

[[Total failure count]{lang="EN-US"}]{#struct_0_x9799_x9248_x48197418}

[[诊断失败的总次数]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1797384253}

[[Consecutive failure count]{lang="EN-US"}]{#struct_0_x9799_x9248_x2115833490}

[[连续执行测试例失败的次数]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1302809118}

[[Last execution time]{lang="EN-US"}]{#struct_0_x9799_x9248_x462942103}

[[最近一次测试执行的时间]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2103933175}

[[First failure time]{lang="EN-US"}]{#struct_0_x9799_x9248_x1543040146}

[[第一次诊断失败的时间。如果没有失败的测试例，此字段内容为]{style="font-family:宋体"}[-NA-]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104850679}

[[Last failure time]{lang="EN-US"}]{#struct_0_x9799_x9248_x908604302}

[[最近一次诊断失败的时间。如果没有失败的测试例，此字段内容为]{style="font-family:宋体"}[-NA-]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104326390}

[[Last pass time]{lang="EN-US"}]{#struct_0_x9799_x9248_854628153}

[[最近一次诊断成功的时间。如果没有成功的测试例，此字段内容为]{style="font-family:宋体"}[-NA-]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104064246}

[[Last execution result]{lang="EN-US"}]{#struct_0_x9799_x9248_x785943864}

[[最近一次诊断结果]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1576283983}

[[Last failure reason]{lang="EN-US"}]{#struct_0_x9799_x9248_1477498277}

[[最近一次诊断失败的原因。当用户配置模拟失败时，此字段内容即为]{style="font-family:宋体"}[Simulated Test]{lang="EN-US"}]{#struct_0_x9799_x9248_455970728}[；当诊断未失败时，此字段内容即为]{style="font-family:宋体"}[-NA-]{lang="EN-US"}

[[Next execution time]{lang="EN-US"}]{#struct_0_x9799_x9248_x2103998710}

[[下次诊断执行的时间。如果是监控诊断类型的测试例，下次执行时间为最后一次测试执行时间加上测试例的时间间隔；如果是按需诊断和启动诊断类型的测试例，则此字段的内容为]{style="font-family:宋体"}[-NA-]{lang="EN-US"}]{#struct_0_x9799_x9248_x1614281359}

[ ]{lang="EN-US"}

::: {#470555659 .myid}
[]{#_Toc404797484}[]{#struct_0_x9799_x9248_730708763}[]{#_Toc335384593}[]{#_Toc335384667}

**GOLD \-- GOLD配置命令 \-- display diagnostic result statistics**

------------------------------------------------------------------------

[**[display diagnostic result statistics]{lang="EN-US"}**]{#struct_0_x9799_x9248_x881366990}[命令用来显示与报文相关的测试例的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_572141000}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x687070369}

[**[display diagnostic result]{lang="EN-US"}**[ \[ **test** ]{lang="EN-US"}]{#struct_0_x9799_x9248_457393155}*[test-name ]{lang="EN-US"}*[\] **statistics**]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_x2103933174}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display diagnostic result]{lang="EN-US"}**[ \[ **slot** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1185843209}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \] \] **statistics**]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_763953615}[模式：]{style="font-family:宋体"}

[**[display diagnostic result ]{lang="EN-US"}**[\[ **chassis** ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1264709162}*[chassis-number ]{lang="EN-US"}*[\[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \] \] \] **statistics**]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_155519769}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_220263595}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1151753911}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_1583269600}

[[network-operator]{lang="EN-US"}]{#struct_0_x9799_x9248_1038305142}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x2104916214}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1216607113}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[表示单板所在的槽位号。不指定该参数时，显示所有单板上与报文相关的测试例的统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2103215747}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定]{style="font-family:宋体"}[该参数]{style="font-family:宋体"}[时，显示所有成员设备上]{style="font-family:宋体"}[与报文相关的测试例的统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213338323}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定]{style="font-family:宋体"}[该参数]{style="font-family:宋体"}[时，显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上测试例的执行结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x727291960}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示所有成员设备上]{style="font-family:宋体"}[与报文相关的测试例的统计信息。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数时，显示指定成员设备所有单板上与报文相关的测试例的统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x238913791}*[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示]{style="font-family:宋体"}[与报文相关的所有测试例的统计信息。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数时，显示指定成员设备所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[与报文相关的测试例的统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_2052093258}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有测试例。（集中式设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1228454596}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有测试例。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x331783945}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有测试例。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_1759087430}*[cpu-number]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x248424627}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104850678}[显示设备中]{style="font-family:宋体"}[PortLoopback]{lang="EN-US"}[执行后的统计结果。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result test PortLoopback statistics]{lang="EN-US"}]{#struct_0_x9799_x9248_1820279053}

[  Test name: PortLoopback]{lang="EN-US"}

[  Port    Packets sent    Packets received   Packets lost]{lang="EN-US"}

[  1       0               0                  0]{lang="EN-US"}

[  2       0               0                  0]{lang="EN-US"}

[  3       0               0                  0]{lang="EN-US"}

[  4       4               4                  0]{lang="EN-US"}

[  5       4               4                  0]{lang="EN-US"}

[  6       4               4                  0]{lang="EN-US"}

[  7       4               4                  0]{lang="EN-US"}

[  8       0               0                  0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1546760808}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[PortLoopback]{lang="EN-US"}[执行后的统计结果。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result slot 1 test PortLoopback statistics]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104391929}

[Slot 1 cpu 0:]{lang="EN-US"}

[  Test name: PortLoopback]{lang="EN-US"}

[  Port    Packets sent    Packets received   Packets lost]{lang="EN-US"}

[  1       0               0                  0]{lang="EN-US"}

[  2       0               0                  0]{lang="EN-US"}

[  3       0               0                  0]{lang="EN-US"}

[  4       4               4                  0]{lang="EN-US"}

[  5       4               4                  0]{lang="EN-US"}

[  6       4               4                  0]{lang="EN-US"}

[  7       4               4                  0]{lang="EN-US"}

[  8       0               0                  0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1587745697}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[PortLoopback]{lang="EN-US"}[执行后的统计结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result slot 1 test PortLoopback statistics]{lang="EN-US"}]{#struct_0_x9799_x9248_1740332488}

[Slot 1 cpu 0:]{lang="EN-US"}

[  Test name: PortLoopback]{lang="EN-US"}

[  Port    Packets sent    Packets received   Packets lost]{lang="EN-US"}

[  1       0               0                  0]{lang="EN-US"}

[  2       0               0                  0]{lang="EN-US"}

[  3       0               0                  0]{lang="EN-US"}

[  4       4               4                  0]{lang="EN-US"}

[  5       4               4                  0]{lang="EN-US"}

[  6       4               4                  0]{lang="EN-US"}

[  7       4               4                  0]{lang="EN-US"}

[  8       0               0                  0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_609245882}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[中单板]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[PortLoopback]{lang="EN-US"}[执行后的统计结果。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> display diagnostic result chassis 1 slot 1 test PortLoopback statistics]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104326393}

[Chassis 1 slot 1 cpu 0:]{lang="EN-US"}

[  Test name: PortLoopback]{lang="EN-US"}

[  Port    Packets sent    Packets received   Packets lost]{lang="EN-US"}

[  1       0               0                  0]{lang="EN-US"}

[  2       0               0                  0]{lang="EN-US"}

[  3       0               0                  0]{lang="EN-US"}

[  4       4               4                  0]{lang="EN-US"}

[  5       4               4                  0]{lang="EN-US"}

[  6       4               4                  0]{lang="EN-US"}

[  7       4               4                  0]{lang="EN-US"}

[  8       0               0                  0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display diagnostic result statistics]{lang="EN-US"}]{#struct_0_x9799_x9248_451343626}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x913388782}[[字段]{style="font-family:黑体"}]{#struct_0_x9799_x9248_2094520801}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1980412849}

[[Slot 1 cpu 0]{lang="EN-US"}]{#struct_0_x9799_x9248_1758825285}

[[指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x9799_x9248_1758759749}[上与报文相关的测试例的统计信息（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Chassis 1 slot 1 cpu 0]{lang="EN-US"}]{#struct_0_x9799_x9248_1758694213}[：]{style="font-family:宋体"}

[[指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x9799_x9248_1758628677}[上与报文相关的测试例的统计信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Test name]{lang="EN-US"}]{#struct_0_x9799_x9248_127130812}

[[测试例的名称]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2145218476}

[[Port]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104260857}

[[端口号]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1411639145}

[[Packets sent]{lang="EN-US"}]{#struct_0_x9799_x9248_834155804}

[[已发送数据包]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x319028754}

[[Packets received]{lang="EN-US"}]{#struct_0_x9799_x9248_222066316}

[[已接收数据包]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2104129785}

[[Packets lost]{lang="EN-US"}]{#struct_0_x9799_x9248_1387411820}

[[丢失的数据包]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1094456437}

[ ]{lang="EN-US"}

::: {#-388567443 .myid}
[]{#_Toc404797485}[]{#struct_0_x9799_x9248_x2104064249}

**GOLD \-- GOLD配置命令 \-- display diagnostic simulation**

------------------------------------------------------------------------

[**[display diagnostic simulation]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1901689111}[命令用来显示模拟诊断的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1433970153}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1643583561}

[**[display diagnostic simulation]{lang="EN-US"}**]{#struct_0_x9799_x9248_x518074731}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_893494311}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display diagnostic simulation ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}]{#struct_0_x9799_x9248_2064491621}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_x2059879316}[模式：]{style="font-family:宋体"}

[**[display diagnostic simulation ]{lang="EN-US"}**[\[ **chassis** ]{lang="EN-US"}]{#struct_0_x9799_x9248_1523453413}*[chassis-number ]{lang="EN-US"}*[\[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x2103998713}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1114601996}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x835153841}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x806463833}

[[network-operator]{lang="EN-US"}]{#struct_0_x9799_x9248_779254984}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1683741396}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_833695393}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[表示单板所在的槽位号。不指定该参数时，显示所有板的模拟诊断配置。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_173581415}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示所有设备的模拟诊断配置。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213010643}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，显示所有设备的模拟诊断配置。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_783172011}*[chassis-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\]]{lang="EN-US"}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示所有设备的模拟诊断配置。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[未指定槽位号时，显示指定设备所有板的模拟诊断配置。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1300314490}*[chassis-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\]]{lang="EN-US"}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，显示所有设备的模拟诊断配置。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[未指定槽位号时，显示指定设备所有板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的模拟诊断配置。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_1758825284}*[cpu-number]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x2103933177}

[[该命令用来显示模拟诊断的配置信息。如果指定的槽号上没有配置模拟诊断，则不显示任何内容。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2104916217}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x349476828}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1238805074}[显示设备上配置的模拟诊断配置信息。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> diagnostic simulation test HGMonitor failure]{lang="EN-US"}]{#struct_0_x9799_x9248_792058721}

[\<sysname\> display diagnostic simulation]{lang="EN-US"}

[  Name                            Mode]{lang="EN-US"}

[  HGMonitor                       failure]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104850681}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上配置的模拟诊断配置信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> diagnostic simulation slot 1 test HGMonitor failure]{lang="EN-US"}]{#struct_0_x9799_x9248_x552177334}

[\<sysname\> display diagnostic simulation slot 1]{lang="EN-US"}

[Slot 1 cpu 0:]{lang="EN-US"}

[Name                            Mode]{lang="EN-US"}

[HGMonitor                       failure]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_771932617}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上配置的模拟诊断配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> diagnostic simulation chassis 1 slot 1 test HGMonitor failure]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104391928}

[\<sysname\> display diagnostic simulation chassis 1 slot 1]{lang="EN-US"}

[Chassis 1 slot 1 cpu 0:]{lang="EN-US"}

[  Name                            Mode]{lang="EN-US"}

[  HGMonitor                       failure]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1141137658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[diagnostic simulation]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1680278347}
:::

::: {#822417227 .myid}
[]{#_Toc404797486}[]{#struct_0_x9799_x9248_x297667872}[]{#_Toc335035713}[]{#_Toc335035720}[]{#_Toc335035721}[]{#_Toc335035722}[]{#_Toc335035723}[]{#_Toc335035724}[]{#_Toc335035725}[]{#_Toc335035726}[]{#_Toc335035727}[]{#_Toc335035728}[]{#_Toc335035730}[]{#_Toc335035731}[]{#_Toc335035732}[]{#_Toc335035733}[]{#_Toc335035734}[]{#_Toc335035735}[]{#_Toc335035736}[]{#_Toc335035738}[]{#_Toc335035740}[]{#_Toc335035741}[]{#_Toc335035742}[]{#_Toc335035743}[]{#_Toc335035744}[]{#_Toc335035745}[]{#_Toc335035746}[]{#_Toc335035747}[]{#_Toc335035752}[]{#_Toc335035753}[]{#_Toc335035755}[]{#_Toc335035756}[]{#_Toc335035757}[]{#_Toc335035758}[]{#_Toc335035759}[]{#_Toc335035760}[]{#_Toc335035761}[]{#_Toc335035766}[]{#_Toc335035767}[]{#_Toc335035768}[]{#_Toc335035769}[]{#_Toc335035770}[]{#_Toc335035771}

**GOLD \-- GOLD配置命令 \-- reset diagnostic event-log**

------------------------------------------------------------------------

[**[reset diagnostic event-log]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2104326392}[命令用来清除]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_2017427567}

[**[reset diagnostic event-log]{lang="EN-US"}**]{#struct_0_x9799_x9248_1967418817}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1656073839}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2104260856}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x1317244210}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_180327965}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_166608290}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104129784}[清除]{style="font-family:宋体"}[GOLD]{lang="EN-US"}[日志]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<sysname\> reset diagnostic event-log]{lang="EN-US"}]{#struct_0_x9799_x9248_x1341471535}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1838120230}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display diagnostic ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1986401531}**[event-log]{lang="EN-US"}**
:::

::: {#-816719520 .myid}
[]{#_Toc404797487}[]{#struct_0_x9799_x9248_340126602}[]{#_Toc334794714}[]{#_Toc335384597}[]{#_Toc335384598}[]{#_Toc335384600}[]{#_Toc335384601}[]{#_Toc335384602}[]{#_Toc335384603}[]{#_Toc335384604}[]{#_Toc335384605}[]{#_Toc335384606}[]{#_Toc335384607}[]{#_Toc335384608}[]{#_Toc335384609}[]{#_Toc335384610}[]{#_Toc335384612}[]{#_Toc335384613}[]{#_Toc335384614}[]{#_Toc335384615}[]{#_Toc335384616}[]{#_Toc335384617}[]{#_Toc335384618}[]{#_Toc335384619}[]{#_Toc335384621}[]{#_Toc335384622}[]{#_Toc335384623}[]{#_Toc335384624}[]{#_Toc335384625}[]{#_Toc335384627}[]{#_Toc335384629}[]{#_Toc335384630}[]{#_Toc335384631}[]{#_Toc335384632}[]{#_Toc335384633}[]{#_Toc335384634}[]{#_Toc335384635}[]{#_Toc335384636}[]{#_Toc335384637}[]{#_Toc335384638}[]{#_Toc335384639}[]{#_Toc335384640}[]{#_Toc335384641}[]{#_Toc335384642}[]{#_Toc335384643}[]{#_Toc335384644}[]{#_Toc335384645}[]{#_Toc335384646}[]{#_Toc335384647}[]{#_Toc335384648}[]{#_Toc335384649}[]{#_Toc335384650}[]{#_Toc335384651}

**GOLD \-- GOLD配置命令 \-- reset diagnostic result**

------------------------------------------------------------------------

[**[reset diagnostic result]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2104064248}[命令用来清除诊断测试结果。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x335605170}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x1654940721}

[**[reset diagnostic result ]{lang="EN-US"}**[\[ **test** ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1410888196}*[test-name]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9799_x9248_1661169844}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset diagnostic result ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}]{#struct_0_x9799_x9248_x180083853}*[slot-number ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\]]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9799_x9248_1818349414}[模式：]{style="font-family:宋体"}

[**[reset diagnostic result ]{lang="EN-US"}**[\[ **chassis**]{lang="EN-US"}]{#struct_0_x9799_x9248_x488753786}*[ chassis-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number ]{lang="EN-US"}*[\] \[ **test** ]{lang="EN-US"}*[test-name]{lang="EN-US"}*[ \] \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1593954426}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9799_x9248_x2103998712}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x451481945}

[[network-admin]{lang="EN-US"}]{#struct_0_x9799_x9248_x1633452558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_x877843848}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_1950513050}*[slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定]{style="font-family:宋体"}[该参数]{style="font-family:宋体"}[时，清除所有板的结果。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_884852378}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，清除所有设备的结果。（集中式]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213666010}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，清除所有设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x751638409}*[chassis-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \]]{lang="EN-US"}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，清除所有设备的结果。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[未指定槽位号时，清除指定设备所有板的结果。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x1213338330}*[chassis-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[ \]]{lang="EN-US"}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[时，清除所有设备的结果。指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[未指定槽位号时，清除指定设备所有板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的结果。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x78800990}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示设备上的所有测试例。（集中式设备）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_419763144}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定单板上的所有测试例。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[test ]{lang="EN-US"}**]{#struct_0_x9799_x9248_x2103933176}*[test-name]{lang="EN-US"}*[：指定测试例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。不指定该参数时，表示指定成员设备上的所有测试例。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9799_x9248_1758300996}*[cpu-number]{lang="EN-US"}*[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_23043795}

[[本命令清除测试结果时，不会清除详细诊断结果中的下次诊断执行时间。]{style="font-family:宋体"}]{#struct_0_x9799_x9248_1470508348}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1226674056}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1796235565}[清除]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[的测试结果。（集中式设备）]{style="font-family:宋体"}

[[\<sysname\> reset diagnostic result test HGMonitor]{lang="EN-US"}]{#struct_0_x9799_x9248_1872672449}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_1067916791}[清除]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[的测试结果。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<sysname\> reset diagnostic result slot 1 test HGMonitor]{lang="EN-US"}]{#struct_0_x9799_x9248_195694160}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x304500913}[清除成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[HGMonitor]{lang="EN-US"}[的测试结果。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<sysname\> reset diagnostic result slot 1 test HGMonitor]{lang="EN-US"}]{#struct_0_x9799_x9248_x2104916216}

[[\# ]{lang="EN-US"}]{#struct_0_x9799_x9248_x1915560769}[清除成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板上]{style="font-family:
宋体"}[HGMonitor]{lang="EN-US"}[的测试结果。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<sysname\> reset diagnostic result chassis 1 slot 1 test HGMonitor]{lang="EN-US"}]{#struct_0_x9799_x9248_x464995389}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9799_x9248_1554737336}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display diagnostic result]{lang="EN-US"}**]{#struct_0_x9799_x9248_265745519}
:::
