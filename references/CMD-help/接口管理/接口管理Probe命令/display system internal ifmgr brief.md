::: {#359218879 .myid}
[]{#_Toc404800602}[]{#_Toc360005391}[]{#_Toc360004671}[]{#struct_0_18798_10625_x2007427820}[]{#_Toc350627540}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr brief**

------------------------------------------------------------------------

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_629313224}**[brief]{lang="EN-US"}**[命令用来显示接口基本信息同步的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_x1614982763}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_x1217385199}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x2007296748}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[brief ]{lang="EN-US"}**[{]{lang="EN-US"}*[ para]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \| **help** }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_1717135472}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x2007231212}**[brief]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ ]{lang="EN-US"}*[para]{lang="EN-US"}*[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \| **help** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_x584735053}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_x1488614378}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_51856999}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_x2007034604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_887024397}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_x355286164}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_x2007100140}[：指定显示时的参数，为接口索引值。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_18798_10625_371451098}*[ slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1460075775}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1658446941}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_371516634}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1555261670}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_80060944}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_630449589}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}
:::

::: {#-1452508156 .myid}
[]{#_Toc404800603}[]{#_Toc360005353}[]{#_Toc360004670}[]{#struct_0_18798_10625_151051531}[]{#_Toc350627539}[]{#_Toc360004847}[]{#_Toc360005486}[]{#_Toc360004848}[]{#_Toc360005487}[]{#_Toc360004849}[]{#_Toc360005488}[]{#_Toc360004850}[]{#_Toc360005489}[]{#_Toc360004851}[]{#_Toc360005490}[]{#_Toc360004852}[]{#_Toc360005491}[]{#_Toc360004853}[]{#_Toc360005492}[]{#_Toc360004854}[]{#_Toc360005493}[]{#_Toc360004855}[]{#_Toc360005494}[]{#_Toc360004856}[]{#_Toc360005495}[]{#_Toc360004857}[]{#_Toc360005496}[]{#_Toc360004858}[]{#_Toc360005497}[]{#_Toc360004859}[]{#_Toc360005498}[]{#_Toc360004860}[]{#_Toc360005499}[]{#_Toc360004861}[]{#_Toc360005500}[]{#_Toc360004862}[]{#_Toc360005501}[]{#_Toc360004863}[]{#_Toc360005502}[]{#_Toc360004864}[]{#_Toc360005503}[]{#_Toc360004865}[]{#_Toc360005504}[]{#_Toc360004866}[]{#_Toc360005505}[]{#_Toc360004867}[]{#_Toc360005506}[]{#_Toc360004868}[]{#_Toc360005507}[]{#_Toc360004869}[]{#_Toc360005508}[]{#_Toc360004870}[]{#_Toc360005509}[]{#_Toc360004871}[]{#_Toc360005510}[]{#_Toc360004872}[]{#_Toc360005511}[]{#_Toc360004873}[]{#_Toc360005512}[]{#_Toc360004874}[]{#_Toc360005513}[]{#_Toc360004890}[]{#_Toc360005529}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr down**

------------------------------------------------------------------------

[**[display system internal ifmgr down]{lang="EN-US"}**]{#struct_0_18798_10625_1810981457}[命令用来显示已注册的]{style="font-family:宋体"}[down]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_2072743784}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_560635130}

[**[display system internal ifmgr down]{lang="EN-US"}**]{#struct_0_18798_10625_x2007362285}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_x1086232665}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x2007165677}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[down]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_x2118746515}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_325914272}**[down]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_x1659030724}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_864201717}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_x2007231213}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_2144148302}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_1519442892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_x1471210637}

[**[slot]{lang="EN-US"}**]{#struct_0_18798_10625_x1410673817}*[ slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x1043511983}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_92363000}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x2007034605}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_872744521}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_79733264}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#-1279514826 .myid}
[]{#_Toc404800604}[]{#_Toc360005110}[]{#_Toc360004669}[]{#struct_0_18798_10625_721783215}[]{#_Toc350627538}[]{#_Toc360004892}[]{#_Toc360005531}[]{#_Toc360004893}[]{#_Toc360005532}[]{#_Toc360004894}[]{#_Toc360005533}[]{#_Toc360004895}[]{#_Toc360005534}[]{#_Toc360004896}[]{#_Toc360005535}[]{#_Toc360004897}[]{#_Toc360005536}[]{#_Toc360004898}[]{#_Toc360005537}[]{#_Toc360004899}[]{#_Toc360005538}[]{#_Toc360004900}[]{#_Toc360005539}[]{#_Toc360004901}[]{#_Toc360005540}[]{#_Toc360004902}[]{#_Toc360005541}[]{#_Toc360004903}[]{#_Toc360005542}[]{#_Toc360004904}[]{#_Toc360005543}[]{#_Toc360004905}[]{#_Toc360005544}[]{#_Toc360004921}[]{#_Toc360005560}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr entry**

------------------------------------------------------------------------

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x1294990476}**[entry]{lang="EN-US"}**[命令用来显示指定接口的数据结构信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_1616462882}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_x1545659534}

[**[display system internal ifmgr entry]{lang="EN-US"}**]{#struct_0_18798_10625_x2007558889}*[ ]{lang="EN-US"}*[{ ]{lang="EN-US"}*[para ]{lang="EN-US"}*[\| **help** }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_968736040}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x2007624425}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[entry ]{lang="EN-US"}**[{]{lang="EN-US"}*[ para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_96201869}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x2007427817}**[entry ]{lang="EN-US"}**[{]{lang="EN-US"}*[ para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_x936967325}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_x2007493353}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_x1338533711}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_x311070587}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_x1915039311}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_x1482919318}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_x1708571331}[：指定显示时的参数。表示接口名或接口索引，格式为：]{style="font-family:宋体"}[1\*]{lang="EN-US"}[接口索引，]{style="font-family:宋体"}[2\*]{lang="EN-US"}[接口名。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_18798_10625_x343926143}*[ slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x1947314675}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_542701694}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x1147293643}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x1498990174}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_79208977}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_627276423}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}
:::

::: {#908661508 .myid}
[]{#_Toc404800605}[]{#_Toc360004891}[]{#_Toc360004665}[]{#struct_0_18798_10625_1108490931}[]{#_Toc350627534}[]{#_Toc360004923}[]{#_Toc360005562}[]{#_Toc360004924}[]{#_Toc360005563}[]{#_Toc360004925}[]{#_Toc360005564}[]{#_Toc360004926}[]{#_Toc360005565}[]{#_Toc360004927}[]{#_Toc360005566}[]{#_Toc360004928}[]{#_Toc360005567}[]{#_Toc360004929}[]{#_Toc360005568}[]{#_Toc360004930}[]{#_Toc360005569}[]{#_Toc360004931}[]{#_Toc360005570}[]{#_Toc360004968}[]{#_Toc360005607}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr event**

------------------------------------------------------------------------

[**[display system internal ifmgr event]{lang="EN-US"}**]{#struct_0_18798_10625_195502951}[命令用来显示接口事件的注册信息，包括哪些模块注册了该事件，以及模块在哪些接口上注册了该事件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_x2140056243}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_853498264}

[**[display system internal ifmgr event]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_18798_10625_721455536}*[para ]{lang="EN-US"}*[\| **help** }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_x1600239405}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1209838253}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[event]{lang="EN-US"}**[ { ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_x2056665155}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721390000}**[event]{lang="EN-US"}**[ { ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_1664412808}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_x1653130115}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_x1870973286}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_729197159}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_x1883518098}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_1148082493}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_x1863296361}[：指定显示时的参数。]{style="font-family:宋体"}*[para]{lang="EN-US"}*[为事件或接口类型，如果同时指定事件和接口类型，事件和接口中间需用"]{style="font-family:宋体"}[\*]{lang="EN-US"}["连接，格式为：]{style="font-family:宋体"}*[event]{lang="EN-US"}*[\*]{lang="EN-US"}*[type]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721586608}*[slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x1204300331}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x1829885765}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_456079535}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_898997590}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_79798801}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_805537337}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}
:::

::: {#-1659185967 .myid}
[]{#_Toc404800606}[]{#_Toc360004922}[]{#_Toc360004666}[]{#struct_0_18798_10625_x543918491}[]{#_Toc350627535}[]{#_Toc360004970}[]{#_Toc360005609}[]{#_Toc360004971}[]{#_Toc360005610}[]{#_Toc360004972}[]{#_Toc360005611}[]{#_Toc360004973}[]{#_Toc360005612}[]{#_Toc360004974}[]{#_Toc360005613}[]{#_Toc360004975}[]{#_Toc360005614}[]{#_Toc360004976}[]{#_Toc360005615}[]{#_Toc360004977}[]{#_Toc360005616}[]{#_Toc360004978}[]{#_Toc360005617}[]{#_Toc360004979}[]{#_Toc360005618}[]{#_Toc360004995}[]{#_Toc360005634}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr hotplug**

------------------------------------------------------------------------

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_560903825}**[hotplug]{lang="EN-US"}**[命令用来显示板或子卡的热插拔信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_721848752}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_2004639572}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1877094689}**[hotplug ]{lang="EN-US"}**[\[ ]{lang="EN-US"}*[para ]{lang="EN-US"}*[\| **help** \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_x1098840213}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721783216}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[hotplug]{lang="EN-US"}**[ \[ \[ ]{lang="EN-US"}*[para ]{lang="EN-US"}*[\] \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_x1294990477}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721324465}**[hotplug]{lang="EN-US"}**[ \[ \[ ]{lang="EN-US"}*[para ]{lang="EN-US"}*[\] \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_68730316}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_x1770541110}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_721258929}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_x1127212222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_x457593010}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_1879676058}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_1780805730}[：指定显示时的参数。]{style="font-family:宋体"}*[para]{lang="EN-US"}*[为]{style="font-family:宋体"}[槽位号或者槽位号和子槽位号（格式为]{style="font-family:宋体"}*[slot-number\*subslot-number]{lang="EN-US"}*[），用于显示该板或子卡的热插拔信息。不指定该参数以及]{style="font-family:宋体"}**[help]{lang="EN-US"}**[参数时，显示所有板的热插拔信息；]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_18798_10625_x973030029}*[ slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。用于显示]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[单板上记录的热插拔信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1255801245}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。用于显示]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[成员设备上记录的热插拔信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x667086351}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。用于显示]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上记录的热插拔信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x975655054}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。用于显示]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[单板上记录的热插拔信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_510450686}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。用于显示]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上记录的热插拔信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_79667729}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_1108697237}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}
:::

::: {#-1567505019 .myid}
[]{#_Toc404800607}[]{#_Toc360004969}[]{#_Toc360004667}[]{#struct_0_18798_10625_x1319978521}[]{#_Toc350627536}[]{#_Toc360004997}[]{#_Toc360005636}[]{#_Toc360004998}[]{#_Toc360005637}[]{#_Toc360004999}[]{#_Toc360005638}[]{#_Toc360005000}[]{#_Toc360005639}[]{#_Toc360005001}[]{#_Toc360005640}[]{#_Toc360005002}[]{#_Toc360005641}[]{#_Toc360005003}[]{#_Toc360005642}[]{#_Toc360005004}[]{#_Toc360005643}[]{#_Toc360005005}[]{#_Toc360005644}[]{#_Toc360005027}[]{#_Toc360005666}[]{#_Toc360005028}[]{#_Toc360005667}[]{#_Toc360005029}[]{#_Toc360005668}[]{#_Toc360005030}[]{#_Toc360005669}[]{#_Toc360005031}[]{#_Toc360005670}[]{#_Toc360005032}[]{#_Toc360005671}[]{#_Toc360005033}[]{#_Toc360005672}[]{#_Toc360005034}[]{#_Toc360005673}[]{#_Toc360005044}[]{#_Toc360005683}[]{#_Toc360005045}[]{#_Toc360005684}[]{#_Toc360005046}[]{#_Toc360005685}[]{#_Toc360005047}[]{#_Toc360005686}[]{#_Toc360005048}[]{#_Toc360005687}[]{#_Toc360005049}[]{#_Toc360005688}[]{#_Toc360005050}[]{#_Toc360005689}[]{#_Toc360005051}[]{#_Toc360005690}[]{#_Toc360005052}[]{#_Toc360005691}[]{#_Toc360005053}[]{#_Toc360005692}[]{#_Toc360005075}[]{#_Toc360005714}[]{#_Toc360005076}[]{#_Toc360005715}[]{#_Toc360005077}[]{#_Toc360005716}[]{#_Toc360005078}[]{#_Toc360005717}[]{#_Toc360005079}[]{#_Toc360005718}[]{#_Toc360005080}[]{#_Toc360005719}[]{#_Toc360005081}[]{#_Toc360005720}[]{#_Toc360005082}[]{#_Toc360005721}[]{#_Toc360005083}[]{#_Toc360005722}[]{#_Toc360005084}[]{#_Toc360005723}[]{#_Toc360005085}[]{#_Toc360005724}[]{#_Toc360005086}[]{#_Toc360005725}[]{#_Toc360005087}[]{#_Toc360005726}[]{#_Toc360005109}[]{#_Toc360005748}[]{#_Toc350450614}[]{#_Toc350515348}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr index**

------------------------------------------------------------------------

[**[display system internal ifmgr index]{lang="EN-US"}**]{#struct_0_18798_10625_667766906}[命令用来显示接口索引节点的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_x2004615962}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_721652145}

[**[display system internal ifmgr index]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_18798_10625_x543918490}*[para ]{lang="EN-US"}*[\| **help** }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_560969361}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721848753}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[index]{lang="EN-US"}**[ { ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_2004639571}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721783217}**[index]{lang="EN-US"}**[ { ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_x1294990478}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_x1515705000}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_x992295813}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_1952940883}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_x788651022}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_1193064900}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_721324462}[：指定显示时的参数。为接口索引值的十进制形式。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_18798_10625_68730315}*[ slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_568111050}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_495713063}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x739744178}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_925175726}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_80060945}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_1646202954}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}
:::

::: {#-1427843288 .myid}
[]{#_Toc404800608}[]{#_Toc360004846}[]{#_Toc360004664}[]{#struct_0_18798_10625_1642398585}[]{#_Toc350627533}[]{#_Toc360005111}[]{#_Toc360005750}[]{#_Toc360005112}[]{#_Toc360005751}[]{#_Toc360005113}[]{#_Toc360005752}[]{#_Toc360005114}[]{#_Toc360005753}[]{#_Toc360005115}[]{#_Toc360005754}[]{#_Toc360005116}[]{#_Toc360005755}[]{#_Toc360005117}[]{#_Toc360005756}[]{#_Toc360005118}[]{#_Toc360005757}[]{#_Toc360005119}[]{#_Toc360005758}[]{#_Toc360005120}[]{#_Toc360005759}[]{#_Toc360005121}[]{#_Toc360005760}[]{#_Toc360005122}[]{#_Toc360005761}[]{#_Toc360005123}[]{#_Toc360005762}[]{#_Toc360005124}[]{#_Toc360005763}[]{#_Toc360005125}[]{#_Toc360005764}[]{#_Toc360005126}[]{#_Toc360005765}[]{#_Toc360005127}[]{#_Toc360005766}[]{#_Toc360005128}[]{#_Toc360005767}[]{#_Toc360005129}[]{#_Toc360005768}[]{#_Toc360005130}[]{#_Toc360005769}[]{#_Toc360005131}[]{#_Toc360005770}[]{#_Toc360005132}[]{#_Toc360005771}[]{#_Toc360005133}[]{#_Toc360005772}[]{#_Toc360005134}[]{#_Toc360005773}[]{#_Toc360005135}[]{#_Toc360005774}[]{#_Toc360005136}[]{#_Toc360005775}[]{#_Toc360005137}[]{#_Toc360005776}[]{#_Toc360005138}[]{#_Toc360005777}[]{#_Toc360005139}[]{#_Toc360005778}[]{#_Toc360005140}[]{#_Toc360005779}[]{#_Toc360005141}[]{#_Toc360005780}[]{#_Toc360005142}[]{#_Toc360005781}[]{#_Toc360005143}[]{#_Toc360005782}[]{#_Toc360005144}[]{#_Toc360005783}[]{#_Toc360005145}[]{#_Toc360005784}[]{#_Toc360005146}[]{#_Toc360005785}[]{#_Toc360005147}[]{#_Toc360005786}[]{#_Toc360005148}[]{#_Toc360005787}[]{#_Toc360005149}[]{#_Toc360005788}[]{#_Toc360005150}[]{#_Toc360005789}[]{#_Toc360005151}[]{#_Toc360005790}[]{#_Toc360005152}[]{#_Toc360005791}[]{#_Toc360005153}[]{#_Toc360005792}[]{#_Toc360005154}[]{#_Toc360005793}[]{#_Toc360005155}[]{#_Toc360005794}[]{#_Toc360005156}[]{#_Toc360005795}[]{#_Toc360005157}[]{#_Toc360005796}[]{#_Toc360005158}[]{#_Toc360005797}[]{#_Toc360005159}[]{#_Toc360005798}[]{#_Toc360005160}[]{#_Toc360005799}[]{#_Toc360005161}[]{#_Toc360005800}[]{#_Toc360005162}[]{#_Toc360005801}[]{#_Toc360005163}[]{#_Toc360005802}[]{#_Toc360005164}[]{#_Toc360005803}[]{#_Toc360005165}[]{#_Toc360005804}[]{#_Toc360005166}[]{#_Toc360005805}[]{#_Toc360005167}[]{#_Toc360005806}[]{#_Toc360005168}[]{#_Toc360005807}[]{#_Toc360005169}[]{#_Toc360005808}[]{#_Toc360005170}[]{#_Toc360005809}[]{#_Toc360005171}[]{#_Toc360005810}[]{#_Toc360005172}[]{#_Toc360005811}[]{#_Toc360005173}[]{#_Toc360005812}[]{#_Toc360005174}[]{#_Toc360005813}[]{#_Toc360005352}[]{#_Toc360005991}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr list**

------------------------------------------------------------------------

[**[display system internal ifmgr list]{lang="EN-US"}**]{#struct_0_18798_10625_642246856}[命令用来显示接口树信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_1085913781}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_x594148936}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721717683}**[list]{lang="EN-US"}**[ \[ ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \| **help** \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_594990265}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x180991854}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[list]{lang="EN-US"}**[ \[ \[ ]{lang="EN-US"}*[para ]{lang="EN-US"}*[\] \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_x1319847449}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721652147}**[list]{lang="EN-US"}**[ \[ \[ ]{lang="EN-US"}*[para ]{lang="EN-US"}*[\] \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_x543918488}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_561493650}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_840358991}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_x582461792}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_x2110342771}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_1768241870}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_721848755}[：指定显示时的参数。]{style="font-family:宋体"}*[para]{lang="EN-US"}*[为接口类型对应的数值，该数值可通过]{style="font-family:宋体"}**[help]{lang="EN-US"}**[参数获取。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_2004639569}*[slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1876767008}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1658512477}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1958443949}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x762758348}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_79274514}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_1850263224}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18798_10625_1197306517}

[[接口树用于管理设备上存在的接口。树上的节点对应接口，子节点对应接口下创建的子接口，每个节点的信息包括接口的名称和索引。]{style="font-family:宋体"}]{#struct_0_18798_10625_x1544994297}

[[不指定]{style="font-family:宋体"}]{#struct_0_18798_10625_x622340384}*[para]{lang="EN-US"}*[和]{style="font-family:宋体"}**[help]{lang="EN-US"}**[参数时，显示所有类型接口的接口树信息。]{style="font-family:宋体"}
:::

::: {#-1428135299 .myid}
[]{#_Toc404800609}[]{#_Toc360004996}[]{#_Toc360004668}[]{#struct_0_18798_10625_721586606}[]{#_Toc350627537}[]{#_Toc360005354}[]{#_Toc360005993}[]{#_Toc360005355}[]{#_Toc360005994}[]{#_Toc360005356}[]{#_Toc360005995}[]{#_Toc360005357}[]{#_Toc360005996}[]{#_Toc360005358}[]{#_Toc360005997}[]{#_Toc360005359}[]{#_Toc360005998}[]{#_Toc360005360}[]{#_Toc360005999}[]{#_Toc360005361}[]{#_Toc360006000}[]{#_Toc360005362}[]{#_Toc360006001}[]{#_Toc360005363}[]{#_Toc360006002}[]{#_Toc360005364}[]{#_Toc360006003}[]{#_Toc360005365}[]{#_Toc360006004}[]{#_Toc360005366}[]{#_Toc360006005}[]{#_Toc360005367}[]{#_Toc360006006}[]{#_Toc360005368}[]{#_Toc360006007}[]{#_Toc360005390}[]{#_Toc360006029}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr mdc**

------------------------------------------------------------------------

[**[display system internal ifmgr mdc]{lang="EN-US"}**]{#struct_0_18798_10625_x1204300321}[命令用来显示]{style="font-family:宋体"}[MDC]{lang="EN-US"}[接口分配相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_456145071}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_473644875}

[**[display system internal ifmgr mdc]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_18798_10625_721521070}*[para ]{lang="EN-US"}*[\| **help** }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_742714205}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721717678}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[mdc]{lang="EN-US"}**[ { ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_x125053762}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_721652142}**[mdc]{lang="EN-US"}**[ { ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| **help** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_x543918493}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_561034897}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_1501337876}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_2103214558}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_1041295760}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_1631839817}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_1227703376}[：指定显示时的参数。合法参数形式有如下四种：]{style="font-family:宋体"}[1\*]{lang="EN-US"}*[接口所在分组的编号]{style="font-family:宋体"}*[、]{style="font-family:宋体"}[2\*]{lang="EN-US"}*[接口名]{style="font-family:宋体"}*[、]{style="font-family:宋体"}[3\*]{lang="EN-US"}*[MDC]{lang="EN-US"}[的编号]{style="font-family:宋体"}*[、]{style="font-family:宋体"}[4\*]{lang="EN-US"}*[槽位号]{style="font-family:宋体"}*[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_18798_10625_721848750}*[ slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_2004639574}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_2108851171}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1877487905}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_1403685635}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_79864337}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_1962048394}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}
:::

::: {#1265418328 .myid}
[]{#_Toc404800610}[]{#_Toc360005447}[]{#_Toc360004672}[]{#struct_0_18798_10625_56168108}[]{#_Toc350627541}[]{#_Toc360005392}[]{#_Toc360006031}[]{#_Toc360005393}[]{#_Toc360006032}[]{#_Toc360005394}[]{#_Toc360006033}[]{#_Toc360005395}[]{#_Toc360006034}[]{#_Toc360005396}[]{#_Toc360006035}[]{#_Toc360005397}[]{#_Toc360006036}[]{#_Toc360005398}[]{#_Toc360006037}[]{#_Toc360005399}[]{#_Toc360006038}[]{#_Toc360005400}[]{#_Toc360006039}[]{#_Toc360005401}[]{#_Toc360006040}[]{#_Toc360005402}[]{#_Toc360006041}[]{#_Toc360005403}[]{#_Toc360006042}[]{#_Toc360005404}[]{#_Toc360006043}[]{#_Toc360005405}[]{#_Toc360006044}[]{#_Toc360005406}[]{#_Toc360006045}[]{#_Toc360005407}[]{#_Toc360006046}[]{#_Toc360005408}[]{#_Toc360006047}[]{#_Toc360005409}[]{#_Toc360006048}[]{#_Toc360005446}[]{#_Toc360006085}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr name**

------------------------------------------------------------------------

[**[display system internal ifmgr name]{lang="EN-US"}**]{#struct_0_18798_10625_371385560}[命令用来显示接口名字解析树信息。]{style="font-family:宋体"}[该树用于解析接口名字，以及命令行上输入接口名字时的帮助检查。]{style="font-family:宋体;
color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_1137400075}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_1854084244}

[**[display system internal ifmgr name]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_18798_10625_371713240}*[para ]{lang="EN-US"}*[\| ]{lang="EN-US"}**[help]{lang="EN-US"}**[ }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_x229239987}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_371582168}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[name]{lang="EN-US"}**[ {]{lang="EN-US"}*[ para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| ]{lang="EN-US"}**[help]{lang="EN-US"}**[ }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_x149256553}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_371975384}**[name]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[  ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| ]{lang="EN-US"}**[help]{lang="EN-US"}**[ }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_x70344968}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_x970978596}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_1414356501}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_986443390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_45600449}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_1325274584}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_372040920}[：指定显示时的参数，为接口全名或简名。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_18798_10625_1233864020}*[ slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x944684631}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_542767230}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_2080194337}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x1080750888}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_79929872}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_1976319225}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}
:::

::: {#878233007 .myid}
[]{#_Toc404800611}[]{#_Toc360005482}[]{#_Toc360004673}[]{#struct_0_18798_10625_1594972412}[]{#_Toc350627542}[]{#_Toc360005448}[]{#_Toc360006087}[]{#_Toc360005449}[]{#_Toc360006088}[]{#_Toc360005450}[]{#_Toc360006089}[]{#_Toc360005451}[]{#_Toc360006090}[]{#_Toc360005452}[]{#_Toc360006091}[]{#_Toc360005453}[]{#_Toc360006092}[]{#_Toc360005454}[]{#_Toc360006093}[]{#_Toc360005455}[]{#_Toc360006094}[]{#_Toc360005456}[]{#_Toc360006095}[]{#_Toc360005457}[]{#_Toc360006096}[]{#_Toc360005458}[]{#_Toc360006097}[]{#_Toc360005459}[]{#_Toc360006098}[]{#_Toc360005481}[]{#_Toc360006120}

**接口管理 \-- 接口管理Probe命令 \-- display system internal ifmgr type**

------------------------------------------------------------------------

[**[display system internal ifmgr type]{lang="EN-US"}**]{#struct_0_18798_10625_x1333563826}[命令用来按类型显示接口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18798_10625_798222835}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18798_10625_371582166}

[**[display system internal ifmgr type]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_18798_10625_371647702}*[para ]{lang="EN-US"}*[\| ]{lang="EN-US"}**[help]{lang="EN-US"}**[ }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18798_10625_x660508225}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_372040918}**[system]{lang="EN-US"}**[ ]{lang="EN-US"}**[internal]{lang="EN-US"}**[ ]{lang="EN-US"}**[ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}**[type]{lang="EN-US"}**[ { ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| ]{lang="EN-US"}**[help]{lang="EN-US"}**[ }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18798_10625_x340114100}[模式：]{style="font-family:宋体"}

[**[display system internal ifmgr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_371516631}**[type]{lang="EN-US"}**[ { ]{lang="EN-US"}*[para]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[  ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \] \| ]{lang="EN-US"}**[help]{lang="EN-US"}**[ }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18798_10625_630449592}

[[Probe]{lang="EN-US"}]{#struct_0_18798_10625_371320023}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18798_10625_786824291}

[[network-admin]{lang="EN-US"}]{#struct_0_18798_10625_1234772793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18798_10625_451673577}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18798_10625_x146977190}

[*[para]{lang="EN-US"}*]{#struct_0_18798_10625_1051904693}[：指定显示时的参数。]{style="font-family:宋体"}*[para]{lang="EN-US"}*[为接口类型，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_18798_10625_x1730260601}*[ slot-number]{lang="EN-US"}*[：表示单板所在的槽位号。不指定该参数时，则表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_x265015033}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_765304150}*[slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_371385559}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18798_10625_815044335}*[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_18798_10625_79208976}[：表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_18798_10625_x818915068}[：显示命令参数的帮助信息，用于指导用户输入合法参数。]{style="font-family:宋体"}

[]{#_debugging_interface命令}[ ]{lang="EN-US"}
:::
