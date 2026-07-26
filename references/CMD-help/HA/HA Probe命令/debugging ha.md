::: {#1293882804 .myid}
[]{#_Toc404798907}[]{#struct_0_45634_x5354_x1555117489}[]{#_Toc264547790}

**HA \-- HA Probe命令 \-- debugging ha**

------------------------------------------------------------------------

[**[debugging ha]{lang="EN-US"}**]{#struct_0_45634_x5354_1446580239}[命令用来打开]{style="font-family:宋体"}[HA]{lang="EN-US"}[各子模块的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging ha]{lang="EN-US"}**]{#struct_0_45634_x5354_x234077390}[命令用来关闭]{style="font-family:宋体"}[HA]{lang="EN-US"}[各子模块的调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_45634_x5354_1963796386}

[**[debugging ha ]{lang="EN-US"}**[{]{lang="EN-US"}]{#struct_0_45634_x5354_732172037}**[ all ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ config]{lang="EN-US"}**[ \|]{lang="EN-US"}**[ fsm]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[policy]{lang="EN-US"}**[ \|]{lang="EN-US"}**[ standby]{lang="EN-US"}**[ \|]{lang="EN-US"}**[ sync ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo debugging ha]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_45634_x5354_1934891408}**[all ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[config ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ fsm ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ policy ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[standby ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[sync ]{lang="EN-US"}**[}]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x1072725035}

[[HA]{lang="EN-US"}]{#struct_0_45634_x5354_239969477}[各子模块的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x647979144}

[[用户视图]{style="font-family:宋体"}]{#struct_0_45634_x5354_x1977579766}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x238312432}

[[network-admin]{lang="EN-US"}]{#struct_0_45634_x5354_2130824043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_45634_x5354_x2054671062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x1860617451}

[**[all]{lang="EN-US"}**]{#struct_0_45634_x5354_x908067442}[：]{style="font-family:宋体"}[HA]{lang="EN-US"}[所有模块的信息。]{style="font-family:宋体"}

[**[config]{lang="EN-US"}**]{#struct_0_45634_x5354_x30519733}[：]{style="font-family:宋体"}[config]{lang="EN-US"}[子模块的信息。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_45634_x5354_x1960620369}[：]{style="font-family:宋体"}[FSM]{lang="EN-US"}[子模块的信息。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_45634_x5354_x1267568603}[：]{style="font-family:宋体"}[policy]{lang="EN-US"}[子模块的信息。]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**]{#struct_0_45634_x5354_971087220}[：备份]{style="font-family:宋体"}[HA]{lang="EN-US"}[模块的信息。]{style="font-family:宋体"}

[**[sync]{lang="EN-US"}**]{#struct_0_45634_x5354_x1977383158}[：]{style="font-family:宋体"}[sync]{lang="EN-US"}[子模块的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x410384304}

[[\# ]{lang="EN-US"}]{#struct_0_45634_x5354_436118696}[打开]{style="font-family:宋体"}[HA FSM]{lang="EN-US"}[子模块的调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ha fsm]{lang="EN-US"}]{#struct_0_45634_x5354_x1360987640}
:::

::: {#1253777267 .myid}
[]{#_Toc404798908}[]{#struct_0_45634_x5354_332473233}[]{#_Toc264547789}[]{#_Toc350533155}[]{#_Toc350535434}[]{#_Toc350533156}[]{#_Toc350535435}[]{#_Toc350533157}[]{#_Toc350535436}[]{#_Toc350533158}[]{#_Toc350535437}[]{#_Toc350533164}[]{#_Toc350535443}[]{#_Toc350533165}[]{#_Toc350535444}[]{#_Toc350533166}[]{#_Toc350535445}[]{#_Toc350533167}[]{#_Toc350535446}[]{#_Toc350533168}[]{#_Toc350535447}[]{#_Toc350533169}[]{#_Toc350535448}

**HA \-- HA Probe命令 \-- display system internal ha service**

------------------------------------------------------------------------

[**[display system internal ha service]{lang="EN-US"}**]{#struct_0_45634_x5354_x1830218570}[命令用来显示某个业务进程的]{style="font-family:宋体"}[HA]{lang="EN-US"}[统计信息，包括业务注册的基本信息、各控制消息接收处理统计、各数据的发送统计和接收统计等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_45634_x5354_717356429}

[**[display system internal ha service ]{lang="EN-US"}***[socket]{lang="EN-US"}*]{#struct_0_45634_x5354_x1977448694}

[[【视图】]{style="font-family:黑体"}]{#struct_0_45634_x5354_898431370}

[[Probe]{lang="EN-US"}]{#struct_0_45634_x5354_x1471865663}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x1461821952}

[[network-admin]{lang="EN-US"}]{#struct_0_45634_x5354_x1365964464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_45634_x5354_x159496190}

[[【参数】]{style="font-family:黑体"}]{#struct_0_45634_x5354_613758702}

[*[socket]{lang="EN-US"}*]{#struct_0_45634_x5354_x2058381058}[：所要查询的业务进程的]{style="font-family:宋体"}[socket]{lang="EN-US"}[，可通过]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[ *sg-name*]{lang="EN-US"}[查询。]{style="font-family:宋体"}
:::

::: {#-2034914255 .myid}
[]{#_Toc404798909}[]{#struct_0_45634_x5354_958702618}[]{#_Toc360002742}[]{#_Toc360002743}[]{#_Toc360002744}[]{#_Toc360002745}[]{#_Toc360002746}[]{#_Toc360002747}[]{#_Toc360002748}[]{#_Toc360002749}[]{#_Toc360002750}[]{#_Toc360002751}[]{#_Toc360002752}[]{#_Toc360002753}[]{#_Toc360002754}[]{#_Toc360002755}[]{#_Toc360002756}[]{#_Toc360002757}[]{#_Toc360002758}[]{#_Toc360002759}[]{#_Toc360002760}[]{#_Toc360002761}[]{#_Toc360002762}[]{#_Toc360002763}[]{#_Toc360002934}[]{#_Toc350533171}[]{#_Toc350535450}[]{#_Toc350533172}[]{#_Toc350535451}[]{#_Toc350533173}[]{#_Toc350535452}[]{#_Toc350533176}[]{#_Toc350535455}[]{#_Toc350533177}[]{#_Toc350535456}[]{#_Toc350533178}[]{#_Toc350535457}[]{#_Toc350533179}[]{#_Toc350535458}[]{#_Toc350533180}[]{#_Toc350535459}[]{#_Toc350533181}[]{#_Toc350535460}

**HA \-- HA Probe命令 \-- display system internal ha service-group**

------------------------------------------------------------------------

[**[display system internal ha service-group]{lang="EN-US"}**]{#struct_0_45634_x5354_1926200887}[命令用来显示当前到]{style="font-family:宋体"}[HA]{lang="EN-US"}[模块注册的所有]{style="font-family:宋体"}[SG]{lang="EN-US"}[信息，包括]{style="font-family:宋体"}[SG]{lang="EN-US"}[的名称、]{style="font-family:宋体"}[SG]{lang="EN-US"}[的状态、]{style="font-family:宋体"}[SU]{lang="EN-US"}[的个数等信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x1267911654}

[**[display system internal ha service-group]{lang="EN-US"}**[ \[]{lang="EN-US"}*[ name]{lang="EN-US"}*]{#struct_0_45634_x5354_x1351474388}**[ ]{lang="EN-US"}**[\[ ]{lang="EN-US"}*[instance]{lang="EN-US"}***[ ]{lang="EN-US"}**[\] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_45634_x5354_1089133986}

[[Probe]{lang="EN-US"}]{#struct_0_45634_x5354_649790128}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x1977776378}

[[network-admin]{lang="EN-US"}]{#struct_0_45634_x5354_x1625911990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_45634_x5354_237042010}

[[【参数】]{style="font-family:黑体"}]{#struct_0_45634_x5354_1890199818}

[*[name]{lang="EN-US"}*]{#struct_0_45634_x5354_x783139044}[：]{style="font-family:宋体"}[SG]{lang="EN-US"}[的名称。不指定该参数时，显示所有]{style="font-family:宋体"}[SG]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[*[instance]{lang="EN-US"}*]{#struct_0_45634_x5354_489821221}[：]{style="font-family:宋体"}[SG]{lang="EN-US"}[实例的名称（如果有实例）。]{style="font-family:宋体"}
:::

::: {#936960589 .myid}
[]{#_Toc404798910}[]{#struct_0_45634_x5354_x504026595}[]{#_Toc360002936}[]{#_Toc360002937}[]{#_Toc360002938}[]{#_Toc360002939}[]{#_Toc360002940}[]{#_Toc360002941}[]{#_Toc360002942}[]{#_Toc360002943}[]{#_Toc360002944}[]{#_Toc360002945}[]{#_Toc360002946}[]{#_Toc360002947}[]{#_Toc360002948}[]{#_Toc360002949}[]{#_Toc360002950}[]{#_Toc360002951}[]{#_Toc360002952}[]{#_Toc360002953}[]{#_Toc360002954}[]{#_Toc360002973}[]{#_Toc360002974}[]{#_Toc360002975}[]{#_Toc360002976}[]{#_Toc360002977}[]{#_Toc360002978}[]{#_Toc360002979}[]{#_Toc360002980}[]{#_Toc360002981}[]{#_Toc360002982}[]{#_Toc360002983}[]{#_Toc360002984}[]{#_Toc360002985}[]{#_Toc360002986}[]{#_Toc360002987}[]{#_Toc360003039}[]{#_Toc350533183}[]{#_Toc350535462}[]{#_Toc350533184}[]{#_Toc350535463}[]{#_Toc350533185}[]{#_Toc350535464}[]{#_Toc350533188}[]{#_Toc350535467}[]{#_Toc350533189}[]{#_Toc350535468}[]{#_Toc350533190}[]{#_Toc350535469}[]{#_Toc350533191}[]{#_Toc350535470}[]{#_Toc350533192}[]{#_Toc350535471}[]{#_Toc350533193}[]{#_Toc350535472}[]{#_Toc350533194}[]{#_Toc350535473}

**HA \-- HA Probe命令 \-- display system internal ha statistics**

------------------------------------------------------------------------

[**[display system internal ha statistics]{lang="EN-US"}**]{#struct_0_45634_x5354_x529344084}[命令用来显示]{style="font-family:宋体"}[HA]{lang="EN-US"}[各子模块的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x1454297438}

[**[display system internal ha statistics]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_45634_x5354_1336127657}**[submodule ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[fsm ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[service ]{lang="EN-US"}**[} \| ]{lang="EN-US"}**[summary]{lang="EN-US"}**[ }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x1822312656}

[[Probe]{lang="EN-US"}]{#struct_0_45634_x5354_x55462074}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x1338641714}

[[network-admin]{lang="EN-US"}]{#struct_0_45634_x5354_1986184205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_45634_x5354_1528383935}

[[【参数】]{style="font-family:黑体"}]{#struct_0_45634_x5354_x775646768}

[**[submodule]{lang="EN-US"}**]{#struct_0_45634_x5354_x1413235100}[：]{style="font-family:宋体"}[HA]{lang="EN-US"}[子模块的信息。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_45634_x5354_1932647012}[：]{style="font-family:宋体"}[FSM]{lang="EN-US"}[子模块的信息。]{style="font-family:宋体"}

[**[service]{lang="EN-US"}**]{#struct_0_45634_x5354_1426241287}[：]{style="font-family:宋体"}[service]{lang="EN-US"}[子模块的信息。]{style="font-family:宋体"}

[**[summary]{lang="EN-US"}**]{#struct_0_45634_x5354_x1484937035}[：全局统计信息。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
