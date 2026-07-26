::: {#-156249095 .myid}
[]{#_Toc404782593}[]{#struct_0_14758_17492_x1382208717}[]{#_Toc185992737}

**配置文件管理 \-- 配置文件管理命令 \-- archive configuration**

------------------------------------------------------------------------

[**[archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x1168841352}[命令用来手工备份当前配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_1291080452}

[**[archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x1122805584}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1993812965}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14758_17492_2011344828}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1964324241}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_1770549311}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_x1863836945}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1464474556}

[[设备支持手工和自动两种方式来备份当前配置。执行该命令后，系统会将当前的配置以指定的文件名保存到指定的路径。]{style="font-family:宋体"}]{#struct_0_14758_17492_x5954129}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14758_17492_x816030158}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_103535028}[命令前必须先执行]{lang="EN-US" style="font-family:宋体"}**[archive configuration location]{lang="EN-US"}**[命令来设置备份配置文件的保存路径和文件名前缀。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令后，只有主用主控板会备份当前配置，备用主控板不进行备份操作。（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_14758_17492_x2126506698}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令后，只有主设备会备份当前配置，从设备不进行备份操作。（集中式]{style="font-family:宋体"}]{#struct_0_14758_17492_627854410}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令后，只有全局主用主控板会备份当前配置，]{style="font-family:宋体"}]{#struct_0_14758_17492_1527703849}[IRF]{lang="EN-US"}[中的其它主控板不进行备份操作。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770483775}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x1083791076}[手工备份当前配置。]{style="font-family:宋体"}

[[\<Sysname\> archive configuration]{lang="EN-US"}]{#struct_0_14758_17492_862212387}

[Save the running configuration to an archive file. Continue? \[Y/N\]: Y]{lang="EN-US"}

[The archive configuration file myarchive_1.cfg is saved.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_1375316831}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration interval]{lang="EN-US"}**]{#struct_0_14758_17492_x1463750449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_x1770492087}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration max]{lang="EN-US"}**]{#struct_0_14758_17492_x1552436903}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x665475798}
:::

::: {#-767952606 .myid}
[]{#_Toc404782594}[]{#struct_0_14758_17492_x922785709}[]{#_Toc185992735}

**配置文件管理 \-- 配置文件管理命令 \-- archive configuration interval**

------------------------------------------------------------------------

[**[archive configuration interval]{lang="EN-US"}**]{#struct_0_14758_17492_1770418239}[命令用来使能自动备份当前配置功能，并设置自动备份的时间间隔。]{style="font-family:
宋体"}

[**[undo archive configuration interval]{lang="EN-US"}**]{#struct_0_14758_17492_x1470918739}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_266028283}

[**[archive configuration interval ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_14758_17492_2087333951}

[**[undo archive configuration interval]{lang="EN-US"}**]{#struct_0_14758_17492_51639726}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14758_17492_795487418}

[[系统不会自动备份当前配置。]{style="font-family:宋体"}]{#struct_0_14758_17492_1024801311}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_97953650}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14758_17492_x488134740}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770876991}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x741019735}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_x606131745}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_1751868789}

[*[minutes]{lang="EN-US"}*]{#struct_0_14758_17492_x2044606232}[：表示自动备份当前配置的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[525600]{lang="EN-US"}[，单位为分钟。（]{style="font-family:宋体"}[525600]{lang="EN-US"}[分钟相当于]{style="font-family:宋体"}[365]{lang="EN-US"}[天）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1070172107}

[[设备支持手工和自动两种方式来备份当前配置。成功执行本命令后，每隔指定时间（由]{style="font-family:宋体"}*[minutes]{lang="EN-US"}*]{#struct_0_14758_17492_x897311202}[值决定）系统会把当前配置以指定文件名自动保存到指定路径，保存完毕后，重新开始计时，进入下一个周期。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14758_17492_138338305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[archive configuration interval]{lang="EN-US"}**]{#struct_0_14758_17492_x41286921}[命令前必须先执行]{lang="EN-US" style="font-family:宋体"}**[archive configuration location]{lang="EN-US"}**[命令来设置备份文件的前缀和保存路径。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令后，只有主用主控板会备份当前配置，备用主控板不进行备份操作。（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_14758_17492_x1248328867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令后，只有主设备会备份当前配置，从设备不进行备份操作。（集中式]{style="font-family:宋体"}]{#struct_0_14758_17492_932250834}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令后，只有全局主用主控板会备份当前配置，全局备用主控板不进行备份操作。（分布式设备－]{style="font-family:宋体"}]{#struct_0_14758_17492_x2133395911}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1150119720}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x1375127129}[设置每隔一小时自动备份当前配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14758_17492_1770352704}

[\[Sysname\] archive configuration interval 60]{lang="EN-US"}

[[Archive files will be saved every 60 minutes.]{lang="EN-US"}]{#_Toc166647677}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_1614814815}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1659885193}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_x1170612982}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration max]{lang="EN-US"}**]{#struct_0_14758_17492_1067995243}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_552966576}
:::

::: {#-186444062 .myid}
[]{#_Toc404782595}[]{#struct_0_14758_17492_x1445476910}[]{#_Toc185992734}

**配置文件管理 \-- 配置文件管理命令 \-- archive configuration location**

------------------------------------------------------------------------

[**[archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_1938340546}[命令用来设置备份配置文件的保存路径和文件名前缀。]{style="font-family:
宋体"}

[**[undo archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_1770287168}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1906475951}

[**[archive configuration location]{lang="EN-US"}***[ directory]{lang="EN-US"}*[ **filename-prefix** *filename-prefix*]{lang="EN-US"}]{#struct_0_14758_17492_1332712127}

[**[undo archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_x408879630}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1784083622}

[[系统没有设置备份配置文件的保存路径和文件名前缀。]{style="font-family:宋体"}]{#struct_0_14758_17492_x1052148556}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_312089513}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14758_17492_1681771554}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_2000808870}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_1770221632}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_x311836500}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_x761217961}

[*[directory]{lang="EN-US"}*]{#struct_0_14758_17492_1096437976}[：表示保存备份配置文件的文件夹的路径，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，格式为存储介质名]{style="font-family:宋体"}[:/\[]{lang="EN-US"}[文件夹名]{style="font-family:宋体"}[\]/]{lang="EN-US"}[子文件夹名。]{style="font-family:宋体"}

[*[filename-prefix]{lang="EN-US"}*]{#struct_0_14758_17492_x941896511}[：表示备份配置文件的文件名前缀，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1977046575}

[[自动或手动备份当前配置前必须使用该命令设置备份配置文件的保存路径和文件名前缀。]{style="font-family:宋体"}]{#struct_0_14758_17492_x2132086610}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14758_17492_x1280776610}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[directory]{lang="EN-US"}*]{#struct_0_14758_17492_1678101288}[必须是主用主控板上已存在的路径，且参数中不能包含槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[directory]{lang="EN-US"}*]{#struct_0_14758_17492_1770156096}[必须是主设备上已存在的路径，且参数中不能包含成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[directory]{lang="EN-US"}*]{#struct_0_14758_17492_x1546325888}[必须是全局主用主控板上已存在的路径，且参数中不能包含成员编号和槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_x2005790698}[命令后，用户将不能手工备份当前配置，系统也不再自动备份当前配置，]{lang="EN-US" style="font-family:宋体"}**[archive configuration interval]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[archive configuration max]{lang="EN-US"}**[的配置也会恢复到缺省情况，]{lang="EN-US" style="font-family:宋体"}**[display archive configuration]{lang="EN-US"}**[的显示信息也会被清除。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_902391857}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x994707540}[在]{style="font-family:宋体"}[flash:/archive/]{lang="EN-US"}[目录下备份配置文件，文件名前缀为]{style="font-family:宋体"}[my_archive]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> mkdir flash:/archive]{lang="EN-US"}]{#struct_0_14758_17492_1376230111}

[Creating directory flash:/archive\... Done.]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] []{#_Toc171256235}[]{#_Toc171257145}archive configuration location flash:/archive filename-prefix my_archive]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1604700856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x1409567757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_1770614848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration max]{lang="EN-US"}**]{#struct_0_14758_17492_63964972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x1776370526}
:::

::: {#165707745 .myid}
[]{#_Toc404782596}[]{#struct_0_14758_17492_x1323766611}[]{#_Toc185992736}

**配置文件管理 \-- 配置文件管理命令 \-- archive configuration max**

------------------------------------------------------------------------

[**[archive configuration max]{lang="EN-US"}**]{#struct_0_14758_17492_x1806624210}[命令用来设置系统允许保存的备份配置文件的最大数。]{style="font-family:
宋体"}

[**[undo archive configuration max]{lang="EN-US"}**]{#struct_0_14758_17492_x1197601403}[用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_500445874}

[**[archive configuration max ]{lang="EN-US"}***[file-number]{lang="EN-US"}*]{#struct_0_14758_17492_x1237272506}

[**[undo archive configuration max]{lang="EN-US"}**]{#struct_0_14758_17492_x983822196}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770549312}

[[系统最多允许保存]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_14758_17492_x1863771409}[个备份配置文件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1462427769}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14758_17492_x951521346}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_877493715}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x1397319998}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_485390765}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_204267139}

[*[file-number]{lang="EN-US"}*]{#struct_0_14758_17492_298626091}[：表示可保存的备份配置文件数目上限，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。该参数的具体数值应根据设备存储介质的空间大小来决定。对于存储空间较小的设备，建议设置]{style="font-family:宋体"}*[file-number]{lang="EN-US"}*[为较小值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770483776}

[[备份配置文件数目过多会占用系统内存空间，通过该命令可以控制备份配置文件的数目。当备份配置文件数目到达上限后，下次备份配置文件（包括自动和手动两种触发方式）时，将删除保存时间最早的备份文件，以保存新的备份配置文件。修改备份配置文件数上限时并不删除多余文件，如果当前已有的备份配置文件数大于或等于新设置的上限值，则在备份新的配置时，系统将自动删除生成时间最早的]{style="font-family:宋体"}[n]{lang="EN-US"}]{#struct_0_14758_17492_x1083725540}[（]{style="font-family:宋体"}[n=]{lang="EN-US"}[当前已有备份配置文件数]{style="font-family:宋体"}[-]{lang="EN-US"}[新设置的上限值]{style="font-family:宋体"}[+1]{lang="EN-US"}[）个备份配置文件。比如，当前已有备份配置文件数为]{style="font-family:宋体"}[7]{lang="EN-US"}[，新设置的上限值为]{style="font-family:宋体"}[4]{lang="EN-US"}[，当有配置需要备份时，系统会先删除"]{style="font-family:宋体"}[7-4+1=4]{lang="EN-US"}["个生成时间最早的备份配置文件。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14758_17492_x705655231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使用该命令前，必须先执行]{lang="EN-US" style="font-family:宋体"}**[archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_1264990377}[命令设置保存路径和文件名前缀，否则，本命令执行失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **archive configuration location**]{lang="EN-US"}]{#struct_0_14758_17492_937579176}[，系统最多允许保存的备份配置文件数目也会恢复到缺省情况。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_1230429721}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x843299626}[设置系统最大允许保存]{style="font-family:宋体"}[10]{lang="EN-US"}[个备份配置文件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14758_17492_x366859747}

[\[Sysname\] archive configuration max 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_624095623}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1770418240}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration location]{lang="EN-US"}**]{#struct_0_14758_17492_x1471377498}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration interval]{lang="EN-US"}**]{#struct_0_14758_17492_x2006264892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x1219770979}
:::

::: {#1634696889 .myid}
[]{#_Toc404782597}[]{#struct_0_14758_17492_764667375}[]{#_Toc206926302}

**配置文件管理 \-- 配置文件管理命令 \-- backup startup-configuration**

------------------------------------------------------------------------

[**[backup startup-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_33797259}[命令用于将设备的主用下次启动配置文件备份到指定的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_471106268}

[**[backup startup-configuration to]{lang="EN-US"}**[ *tftp-server* \[ *dest-filename* \]]{lang="EN-US"}]{#struct_0_14758_17492_x656734477}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x989192128}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14758_17492_1770876992}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_x740823127}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x2142462664}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_x1731950360}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_272044413}

[*[tftp-server]{lang="EN-US"}*]{#struct_0_14758_17492_x1464511117}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或主机名。其中，主机名为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["或"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[dest-filename]{lang="EN-US"}*]{#struct_0_14758_17492_x1666591761}[：目的文件名，后缀必须为"]{style="font-family:宋体"}[.cfg]{lang="EN-US"}["。在服务器上将以该文件名保存设备的启动配置文件。不指定该参数时，使用原文件名备份。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1868020187}

[[FIPS]{lang="EN-US"}]{#struct_0_14758_17492_x1455860796}[模式下，不支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770811456}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_68730728}[将设备的下次启动配置文件备份到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上，文件名为]{style="font-family:宋体"}[192-168-1-26.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> backup startup-configuration to 2.2.2.2 192-168-1-26.cfg]{lang="EN-US"}]{#struct_0_14758_17492_209194395}

[Backup next startup-configuration file to 2.2.2.2, please wait...finished]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_620227853}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[restore startup-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1504488186}
:::

::: {#340680174 .myid}
[]{#_Toc404782598}[]{#struct_0_14758_17492_x2129213371}

**配置文件管理 \-- 配置文件管理命令 \-- configuration encrypt**

------------------------------------------------------------------------

[**[configuration encrypt]{lang="EN-US"}**]{#struct_0_14758_17492_x121220676}[命令用来使能配置文件加密功能。]{style="font-family:宋体"}

[**[undo configuration encrypt]{lang="EN-US"}**]{#struct_0_14758_17492_x631701329}[命令用来关闭配置文件加密功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_442199576}

[**[configuration encrypt]{lang="EN-US"}**[ { **private-key** \| **public-key** }]{lang="EN-US"}]{#struct_0_14758_17492_1770352701}

[**[undo configuration encrypt]{lang="EN-US"}**]{#struct_0_14758_17492_1615011423}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14758_17492_x316436341}

[[配置文件加密功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14758_17492_787397591}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_1474787900}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14758_17492_1706851245}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1577085056}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x1793647482}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_1894159925}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770287165}

[**[private-key]{lang="EN-US"}**]{#struct_0_14758_17492_x1906148271}[：使用私钥进行加密。所有运行]{style="font-family:宋体"}[Comware V7]{lang="EN-US"}[平台软件的]{style="font-family:宋体"}[H3C]{lang="EN-US"}[设备拥有相同的私钥。]{style="font-family:宋体"}

[**[public-key]{lang="EN-US"}**]{#struct_0_14758_17492_x125753539}[：使用公钥进行加密。所有运行]{style="font-family:宋体"}[Comware V7]{lang="EN-US"}[平台软件的]{style="font-family:宋体"}[H3C]{lang="EN-US"}[设备拥有相同的公钥。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1709809841}

[[使能该功能后，每次执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**]{#struct_0_14758_17492_1168787544}[操作，都会先将当前的生效的配置进行加密，再保存。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_777134785}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x724082135}[设置保存配置文件时使用公钥进行加密。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14758_17492_1770221629}

[\[Sysname\] configuration encrypt public-key]{lang="EN-US"}
:::

::: {#701317505 .myid}
[]{#_Toc404782599}[]{#struct_0_14758_17492_x311115605}[]{#_Toc206926304}

**配置文件管理 \-- 配置文件管理命令 \-- configuration replace file**

------------------------------------------------------------------------

[**[configuration replace file]{lang="EN-US"}**]{#struct_0_14758_17492_397684715}[命令用来进行配置回滚。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x201756129}

[**[configuration replace file]{lang="EN-US"}**[ *filename*]{lang="EN-US"}]{#struct_0_14758_17492_x1090135363}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_1974934086}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14758_17492_x1230109100}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_440118372}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x1222272531}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_1770156093}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1546129280}

[*[filename]{lang="EN-US"}*]{#struct_0_14758_17492_x47205148}[：指定用来回滚配置的配置文件名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_702909688}

[[配置回滚是在不重启设备的情况下，将当前的配置回退到指定配置文件中的配置状态。该配置文件必须是有效的]{style="font-family:宋体"}[.cfg]{lang="EN-US"}]{#struct_0_14758_17492_x1660453375}[文件，]{style="font-family:宋体"}[它可以使用手工]{style="font-family:宋体"}[/]{lang="EN-US"}[自动备份功能或者]{style="font-family:宋体"}**[save]{lang="EN-US"}**[命令生成，也可以是别的设备的可兼容配置文件，推荐使用手工]{style="font-family:宋体"}[/]{lang="EN-US"}[自动备份功能生成。如果]{style="font-family:宋体"}[使用的配置文件不是由]{style="font-family:宋体"}**[save]{lang="EN-US"}**[命令、自动备份或手工备份生成的完整文件，或是不同类型设备的配置文件，配置回滚可能不能完全恢复至配置文件中的配置状态。因此，需要用户确保回滚配置文件中配置的正确性和与当前设备的兼容性。]{style="font-family:宋体"}

[[本命令中指定的配置文件只能是明文配置文件，不能是被加密的配置文件。否则，不能回滚。]{style="font-family:宋体"}]{#struct_0_14758_17492_1705914668}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_x692062924}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x1482933236}[将当前配置回滚到配置文件]{style="font-family:宋体"}[my_archive_1.cfg]{lang="EN-US"}[中的配置状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14758_17492_x537553470}

[\[Sysname\] configuration replace file my_archive_1.cfg]{lang="EN-US"}

[Current configuration will be lost, save current configuration? \[Y/N\]:n]{lang="EN-US"}

[Now replacing the current configuration. Please wait\...]{lang="EN-US"}

[Succeeded in replacing current configuration with the file my_archive_1.cfg.]{lang="EN-US"}
:::

::: {#911572789 .myid}
[]{#_Toc404782600}[]{#struct_0_14758_17492_1770614845}[]{#_Toc206926305}[]{#_Toc342654823}[]{#_Toc342654824}[]{#_Toc342654825}[]{#_Toc342654826}[]{#_Toc342654827}[]{#_Toc342654828}[]{#_Toc342654829}[]{#_Toc342654830}[]{#_Toc342654831}[]{#_Toc342654832}[]{#_Toc342654833}[]{#_Toc342654834}[]{#_Toc342654835}[]{#_Toc342654836}[]{#_Toc342654837}[]{#_Toc342654838}[]{#_Toc342654839}[]{#_Toc342654840}[]{#_Toc342654841}[]{#_Toc342654842}

**配置文件管理 \-- 配置文件管理命令 \-- display archive configuration**

------------------------------------------------------------------------

[**[display archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_63637292}[命令用来显示备份配置文件的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_1236407014}

[**[display archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1540339397}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x861381278}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14758_17492_x1279945339}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1830347825}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_104072876}

[[network-operator]{lang="EN-US"}]{#struct_0_14758_17492_430303315}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_1770549309}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14758_17492_x1863312656}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_x995969260}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x2084106991}[显示备份配置文件的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display archive configuration]{lang="EN-US"}]{#struct_0_14758_17492_1055271423}

[Location: flash:/archive]{lang="EN-US"}

[Filename prefix: my_archive]{lang="EN-US"}

[Archive interval in minutes: 120]{lang="EN-US"}

[Maximum number of archive files: 10]{lang="EN-US"}

[Saved archive files:]{lang="EN-US"}

[  No. TimeStamp                  FileName]{lang="EN-US"}

[  1   Wed Dec 15 14:20:18 2010   my_archive_1.cfg]{lang="EN-US"}

[  2   Wed Dec 15 14:33:10 2010   my_archive_2.cfg]{lang="EN-US"}

[\# 3   Wed Dec 15 14:49:37 2010   my_archive_3.cfg]{lang="EN-US"}

['#' indicates the most recent archive file.]{lang="EN-US"}

[Next archive file to be saved: my_archive_4.cfg]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display archive configuration]{lang="EN-US"}]{#struct_0_14758_17492_1770483773}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1744948867}[[字段]{style="font-family:黑体"}]{#struct_0_14758_17492_x1083397860}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14758_17492_868224205}

[[Location]{lang="EN-US"}]{#struct_0_14758_17492_691054601}

[[保存备份配置文件的文件夹的绝对路径]{style="font-family:宋体"}]{#struct_0_14758_17492_x2093494256}

[[Filename prefix]{lang="EN-US"}]{#struct_0_14758_17492_1703301413}

[[备份配置文件的文件名前缀]{style="font-family:宋体"}]{#struct_0_14758_17492_x932865882}

[[Archive interval in minutes]{lang="EN-US"}]{#struct_0_14758_17492_1770418237}

[[自动备份配置文件的时间间隔，以分钟为单位]{style="font-family:宋体"}]{#struct_0_14758_17492_x1471311955}

[[若不自动备份配置文件，不显示此项]{style="font-family:宋体"}]{#struct_0_14758_17492_x120341348}

[[Maximum number of archive files]{lang="EN-US"}]{#struct_0_14758_17492_x655460970}

[[设备可保存的最大备份配置文件数目]{style="font-family:宋体"}]{#struct_0_14758_17492_1525150351}

[[Saved archive files]{lang="EN-US"}]{#struct_0_14758_17492_x1957547069}

[[当前已保存的备份配置文件信息]{style="font-family:宋体"}]{#struct_0_14758_17492_1770876989}

[[No.]{lang="EN-US"}]{#struct_0_14758_17492_x741544024}

[[显示已保存的备份配置文件信息的行号]{style="font-family:宋体"}]{#struct_0_14758_17492_996884164}

[[TimeStamp]{lang="EN-US"}]{#struct_0_14758_17492_1871046395}

[[备份配置文件的保存时间]{style="font-family:宋体"}]{#struct_0_14758_17492_x1578766176}

[[FileName]{lang="EN-US"}]{#struct_0_14758_17492_x2000346976}

[[备份配置文件名，不包含路径]{style="font-family:宋体"}]{#struct_0_14758_17492_1770811453}

[['#' indicates the most recent archive file.]{lang="EN-US"}]{#struct_0_14758_17492_68403048}

[["]{style="font-family:宋体"}[\#]{lang="EN-US"}]{#struct_0_14758_17492_x1057333051}["表示该行描述的备份配置文件是最近一次备份的]{style="font-family:宋体"}

[[Next archive file to be saved]{lang="EN-US"}]{#struct_0_14758_17492_x1224622725}

[[下次保存备份配置文件将使用的文件名]{style="font-family:宋体"}]{#struct_0_14758_17492_x1818551531}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770352702}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1614945887}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration interval]{lang="EN-US"}**]{#struct_0_14758_17492_x1057791530}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration location]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_14758_17492_351371745}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[archive configuration max]{lang="EN-US"}**]{#struct_0_14758_17492_508326243}

::: {#520619923 .myid}
[]{#_Toc404782601}[]{#struct_0_14758_17492_x1648657033}[]{#_Toc298920481}[]{#_Toc267407337}[]{#_Toc263066876}

**配置文件管理 \-- 配置文件管理命令 \-- display current-configuration**

------------------------------------------------------------------------

[**[display current-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_2137252945}[命令用来显示设备当前生效的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x2103053942}

[**[display current-configuration ]{lang="EN-US"}**[\[ **configuration** \[ *module-name* \] \| **interface** \[ *interface-type* \[ *interface-number* \] \] \]]{lang="EN-US"}]{#struct_0_14758_17492_x804532547}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770287166}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14758_17492_x1906082735}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_x129857424}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_1934003523}

[[network-operator]{lang="EN-US"}]{#struct_0_14758_17492_x1460368968}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_x387799901}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14758_17492_490345680}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_417790113}

[**[configuration]{lang="EN-US"}**[ \[ *module-name* \]]{lang="EN-US"}]{#struct_0_14758_17492_513387041}[：显示具体功能模块的配置信息，]{style="font-family:宋体"}*[module-name]{lang="EN-US"}*[参数的取值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ \[ *interface-type* \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_14758_17492_1770221630}[：显示接口的配置。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[表示接口类型，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_x311705428}

[[当用户完成一组配置之后，需要验证是否配置正确，则可以执行]{style="font-family:宋体"}**[display current-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_21508243}[命令来查看当前生效的参数。对于某些当前配置的参数，如果与缺省参数相同，则不显示。对于某些参数，由于硬件或者规格限制，实际生效值和用户配置值不一致，则显示实际生效值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_x584105345}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_469732201}[查看当前设备上本地用户的相关配置。]{style="font-family:宋体"}

[[\<Sysname\> display current-configuration configuration local-user]{lang="EN-US"}]{#struct_0_14758_17492_x984720811}

[\#]{lang="EN-US"}

[local-user ftp]{lang="EN-US"}

[ password simple 123]{lang="EN-US"}

[ service-type ftp]{lang="EN-US"}

[ authorization-attribute user-role network-operator]{lang="EN-US"}

[\#]{lang="EN-US"}

[local-user root]{lang="EN-US"}

[ password simple admin]{lang="EN-US"}

[ service-type ssh telnet terminal]{lang="EN-US"}

[ authorization-attribute user-role network-admin]{lang="EN-US"}

[\#]{lang="EN-US"}

[return]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_1770156094}[查看当前设备上以太网接口的相关配置。]{style="font-family:宋体"}

[[\<Sysname\> display current-configuration interface gigabitethernet]{lang="EN-US"}]{#struct_0_14758_17492_x1546194816}

[\#]{lang="EN-US"}

[interface GigabitEthernet1/0/1]{lang="EN-US"}

[ port link-mode route]{lang="EN-US"}

[\#]{lang="EN-US"}

[return]{lang="EN-US"}
:::

::: {#-1197985820 .myid}
[]{#_Toc298920482}[]{#_Toc404782602}[]{#struct_0_14758_17492_2123320259}[]{#_Toc291763448}[]{#_Toc267407338}[]{#_Toc263066877}

**配置文件管理 \-- 配置文件管理命令 \-- display default-configuration**

------------------------------------------------------------------------

[**[display default-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x364239177}[命令用来显示设备的出厂配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x803934114}

[**[display default-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_991020084}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x482008333}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14758_17492_1770614846}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_63571756}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x538391193}

[[network-operator]{lang="EN-US"}]{#struct_0_14758_17492_970616237}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_1161975969}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14758_17492_358062510}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1660584448}

[[设备在出厂时，通常会带有一些基本的配置，称为出厂配置。它用来保证设备在没有配置文件或者配置文件损坏的情况下，能够正常启动、运行。]{style="font-family:宋体"}]{#struct_0_14758_17492_1842652008}

[[出厂配置可能与命令行的缺省情况不一致，不同型号的设备会根据需要定制各自的出厂配置。]{style="font-family:宋体"}]{#struct_0_14758_17492_x1511433634}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_317896248}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_1493832860}[显示设备的出厂配置（不同型号的设备出厂配置不同，请以设备的实际情况为准，具体显示信息略）。]{style="font-family:宋体"}

[[\<Sysname\> display default-configuration]{lang="EN-US"}]{#struct_0_14758_17492_1380544117}
:::

::: {#1550405248 .myid}
[]{#_Toc404782603}[]{#struct_0_14758_17492_2034125116}

**配置文件管理 \-- 配置文件管理命令 \-- display saved-configuration**

------------------------------------------------------------------------

[**[display saved-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1770549310}[命令用来查看下次启动配置文件的内容。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1863902481}

[**[display saved-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x398916076}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_1222709179}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14758_17492_425479417}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_581451272}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x941946034}

[[network-operator]{lang="EN-US"}]{#struct_0_14758_17492_759322128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_759220817}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14758_17492_1770483774}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1083856612}

[[可以在管理]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14758_17492_388629417}[维护设备时使用该命令确认重要的配置是否已经保存到下次启动配置文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用下次启动配置文件存在，执行该命令会显示主用下次启动配置文件的内容；]{style="font-family:宋体"}]{#struct_0_14758_17492_x1660453376}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用下次启动配置文件不存在，但备用下次启动配置文件存在，执行该命令会显示备用下次启动配置文件的内容；]{style="font-family:宋体"}]{#struct_0_14758_17492_409843030}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用和备用下次启动配置文件均不存在，执行该命令，则不显示任何信息。]{style="font-family:宋体"}]{#struct_0_14758_17492_x595508969}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_x86605517}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x1293785244}[显示主用下次启动配置文件的内容。]{style="font-family:宋体"}

[[\<Sysname\> display saved-configuration]{lang="EN-US"}]{#struct_0_14758_17492_1770418238}

[\#]{lang="EN-US"}

[ version 1.00, Alpha 2009]{lang="EN-US"}

[\#]{lang="EN-US"}

[ sysname Sysname]{lang="EN-US"}

[\#]{lang="EN-US"}

[mdc Admin id 1]{lang="EN-US"}

[\#]{lang="EN-US"}

[ ftp server enable]{lang="EN-US"}

[\#]{lang="EN-US"}

[ telnet server enable]{lang="EN-US"}

[\#]{lang="EN-US"}

[ domain default enable system]{lang="EN-US"}

[\#]{lang="EN-US"}

[vlan 1]{lang="EN-US"}

[\#]{lang="EN-US"}

[domain system]{lang="EN-US"}

[\#]{lang="EN-US"}

[[......略......]{style="font-family:宋体"}]{#struct_0_14758_17492_x1470853203}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_1503191222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[save]{lang="EN-US"}**]{#struct_0_14758_17492_x1958766489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset saved-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_796346308}
:::

::: {#1271120943 .myid}
[]{#_Toc98563091}[]{#_Toc67115442}[]{#_Toc66610528}[]{#_Toc404782604}[]{#struct_0_14758_17492_x459434197}[]{#_Toc298920483}[]{#_Toc206926307}

**配置文件管理 \-- 配置文件管理命令 \-- display startup**

------------------------------------------------------------------------

[**[display startup]{lang="EN-US"}**]{#struct_0_14758_17492_1717837860}[命令用来显示用于本次及下次启动的配置文件的名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770876990}

[**[display startup]{lang="EN-US"}**]{#struct_0_14758_17492_x740954199}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1748549811}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14758_17492_1079517827}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_88767337}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x2047829333}

[[network-operator]{lang="EN-US"}]{#struct_0_14758_17492_1785278706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_1125110491}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14758_17492_1040266170}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1770811454}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_14758_17492_68861800}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[因为备用主控板是根据主用主控板的当前配置启动和运行的，所以主用主控板和备用主控板显示的当前启动配置文件始终是相同的。]{style="font-family:宋体"}]{#struct_0_14758_17492_x1869584689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当主备倒换后，主用主控板和备用主控板的角色交换，新的主用主控板没有从配置文件重启而是沿用当前的配置继续运行，使用]{style="font-family:宋体"}]{#struct_0_14758_17492_827485136}**[display startup]{lang="EN-US"}**[查看时，所有主控板的当前启动配置文件均会显示为]{style="font-family:宋体"}[NULL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14758_17492_x477832449}[设备：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[因为从设备是根据主设备的当前配置启动和运行的，所以]{style="font-family:宋体"}]{#struct_0_14758_17492_1605758005}[IRF]{lang="EN-US"}[中所有成员设备显示的当前启动配置文件始终是相同的。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当主设备角色变更后，新的主设备没有从配置文件重启而是沿用当前的配置继续运行，使用]{style="font-family:宋体"}]{#struct_0_14758_17492_709085280}**[display startup]{lang="EN-US"}**[查看时，所有成员设备的当前启动配置文件均会显示为]{style="font-family:宋体"}[NULL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_610948857}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14758_17492_x1337349440}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_1770352699}[显示本次及下次启动的配置文件名。]{style="font-family:宋体"}

[[\<Sysname\> display startup]{lang="EN-US"}]{#struct_0_14758_17492_x724165034}

[ Current startup saved-configuration file: flash:/startup.cfg]{lang="EN-US"}

[ Next main startup saved-configuration file: flash:/startup.cfg]{lang="EN-US"}

[ Next backup startup saved-configuration file: NULL]{lang="EN-US"}

[]{#struct_0_14758_17492_x546462972}[]{#_Toc140913171}[]{#_Toc138955445}[]{#_Toc124566560}[]{#_Toc123730069}[]{#_Toc123729879}[[表1-2 ]{lang="EN-US"}[display startup]{lang="EN-US"}]{#_Toc17279307}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1775829422}[[字段]{style="font-family:黑体"}]{#struct_0_14758_17492_x1142413282}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14758_17492_178302597}

[[Current Startup saved-configuration file]{lang="EN-US"}]{#struct_0_14758_17492_x693387649}

[[当前启动使用的配置文件]{style="font-family:宋体"}]{#struct_0_14758_17492_x1566598534}

[[Next main startup saved-configuration file]{lang="EN-US"}]{#struct_0_14758_17492_1770287163}

[[下一次启动时使用的主用配置文件]{style="font-family:宋体"}]{#struct_0_14758_17492_x1905755055}

[[Next backup startup saved-configuration file]{lang="EN-US"}]{#struct_0_14758_17492_1948901721}

[[下一次启动时使用的备用配置文件]{style="font-family:宋体"}]{#struct_0_14758_17492_202618696}

[ ]{lang="EN-US"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_14758_17492_x398377534}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_72784482}[显示本次及下次启动的配置文件名。]{style="font-family:宋体"}

[[\<Sysname\> display startup]{lang="EN-US"}]{#struct_0_14758_17492_1770221627}

[MainBoard:]{lang="EN-US"}

[ Current startup saved-configuration file: flash:/startup.cfg]{lang="EN-US"}

[ Next main startup saved-configuration file: flash:/startup.cfg]{lang="EN-US"}

[ Next backup startup saved-configuration file: NULL]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[ Current startup saved-configuration file: flash:/startup.cfg]{lang="EN-US"}

[ Next main startup saved-configuration file: flash:/startup.cfg]{lang="EN-US"}

[ Next backup startup saved-configuration file: NULL]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display startup]{lang="EN-US"}]{#struct_0_14758_17492_x311508821}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1777405308}[[字段]{style="font-family:黑体"}]{#struct_0_14758_17492_16938836}

[[描述]{style="font-family:黑体"}]{#struct_0_14758_17492_439216919}

[[MainBoard]{lang="EN-US"}]{#struct_0_14758_17492_x1812256291}

[[主用主控板使用的本次及下次启动的配置文件名]{style="font-family:宋体"}]{#struct_0_14758_17492_406126329}

[[Current startup saved-configuration file]{lang="EN-US"}]{#struct_0_14758_17492_x645489451}

[[当前启动使用的配置文件]{style="font-family:宋体"}]{#struct_0_14758_17492_1770156091}

[[Next startup saved-configuration file]{lang="EN-US"}]{#struct_0_14758_17492_x1545998208}

[[下一次启动时使用的配置文件]{style="font-family:宋体"}]{#struct_0_14758_17492_580596878}

[[Slot *n*]{lang="EN-US"}]{#struct_0_14758_17492_424326831}

[[备用主控板（所在槽位号为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_14758_17492_1721684974}[）使用的本次及下次启动的配置文件名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_14758_17492_1731617068}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_1019655937}[显示本次及下次启动的配置文件名。]{style="font-family:宋体"}

[[\<Sysname\> display startup]{lang="EN-US"}]{#struct_0_14758_17492_1770614843}

[MainBoard:]{lang="EN-US"}

[ Current startup saved-configuration file: NULL]{lang="EN-US"}

[ Next main startup saved-configuration file: flash:/startup.cfg]{lang="EN-US"}

[ Next backup startup saved-configuration file: flash:/startup2.cfg]{lang="EN-US"}

[Chassis 2 Slot 0:]{lang="EN-US"}

[ Current startup saved-configuration file: NULL]{lang="EN-US"}

[ Next main startup saved-configuration file: flash:/startup.cfg]{lang="EN-US"}

[ Next backup startup saved-configuration file: flash:/startup2.cfg]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display startup]{lang="EN-US"}]{#struct_0_14758_17492_63244076}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1777220464}[[字段]{style="font-family:黑体"}]{#struct_0_14758_17492_1243066015}

[[描述]{style="font-family:黑体"}]{#struct_0_14758_17492_600868915}

[[MainBoard]{lang="EN-US"}]{#struct_0_14758_17492_1964318383}

[[主设备使用的本次及下次启动的配置文件名]{style="font-family:宋体"}]{#struct_0_14758_17492_1770549307}

[[Current startup saved-configuration file]{lang="EN-US"}]{#struct_0_14758_17492_x1863443728}

[[当前启动使用的配置文件]{style="font-family:宋体"}]{#struct_0_14758_17492_x585710880}

[[Next main startup saved-configuration file]{lang="EN-US"}]{#struct_0_14758_17492_1297368340}

[[下一次启动时使用的主用配置文件]{style="font-family:宋体"}]{#struct_0_14758_17492_1675801588}

[[Next backup startup saved-configuration file]{lang="EN-US"}]{#struct_0_14758_17492_795524971}

[[下一次启动时使用的备用配置文件]{style="font-family:宋体"}]{#struct_0_14758_17492_x1770701947}

[[(This file does not exist.)]{lang="EN-US"}]{#struct_0_14758_17492_1770483771}

[[表示配置文件不存在]{style="font-family:宋体"}]{#struct_0_14758_17492_x1083528932}

[[如果用户在配置完下次启动配置文件后又将该文件删除了，这种情况下会在文件名后显示该信息]{style="font-family:宋体"}]{#struct_0_14758_17492_949724431}

[[Chassis 2 Slot 2]{lang="EN-US"}]{#struct_0_14758_17492_x70235934}

[[成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_14758_17492_581503631}[上的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板使用的本次及下次启动的配置文件名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_1780997462}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[startup saved-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1770418235}

::: {#-497896898 .myid}
[]{#_Toc404782605}[]{#struct_0_14758_17492_x1471180883}[]{#_Toc298920484}[]{#_Toc267407357}[]{#_Toc263066894}

**配置文件管理 \-- 配置文件管理命令 \-- display this**

------------------------------------------------------------------------

[**[display this]{lang="EN-US"}**]{#struct_0_14758_17492_2146874732}[命令用来显示当前视图下生效的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_632710116}

[**[display]{lang="EN-US"}**[ **this**]{lang="EN-US"}]{#struct_0_14758_17492_794135191}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1187209589}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14758_17492_586268865}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1347313991}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x139698118}

[[network-operator]{lang="EN-US"}]{#struct_0_14758_17492_446269356}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_1770876987}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14758_17492_x741150808}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1788088522}

[[当用户在某一视图下完成一组配置之后，需要验证是否配置成功，则可以执行]{style="font-family:宋体"}**[display this]{lang="EN-US"}**]{#struct_0_14758_17492_x287583589}[命令来查看当前生效的配置。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14758_17492_1899286584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有些已经生效的配置如果与缺省情况相同，则不显示。]{style="font-family:宋体"}]{#struct_0_14758_17492_x224312803}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于某些参数，虽然用户已经配置，但如果这些参数所在的功能没有生效，则不显示。]{style="font-family:宋体"}]{#struct_0_14758_17492_x803608019}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在任意一个用户界面视图下执行此命令，将会显示所有用户界面下生效的配置。]{style="font-family:宋体"}]{#struct_0_14758_17492_1358468731}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1499936410}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_1770811451}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下生效的配置（该显示信息与设备当前的配置有关）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14758_17492_68534120}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] display this]{lang="EN-US"}

[\#]{lang="EN-US"}

[interface GigabitEthernet1/0/1]{lang="EN-US"}

[ port link-mode route]{lang="EN-US"}

[\#]{lang="EN-US"}

[return]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x304338123}[显示所有用户界面下生效的配置（该显示信息与设备当前的配置有关）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14758_17492_1770352700}

[\[Sysname\] line vty 0]{lang="EN-US"}

[\[Sysname-line-vty0\] display this]{lang="EN-US"}

[\#]{lang="EN-US"}

[line aux 0]{lang="EN-US"}

[ user-role network-operator]{lang="EN-US"}

[\#]{lang="EN-US"}

[line con 0]{lang="EN-US"}

[ user-role network-admin]{lang="EN-US"}

[\#]{lang="EN-US"}

[line vty 0 4]{lang="EN-US"}

[ authentication-mode none]{lang="EN-US"}

[ user-role network-admin]{lang="EN-US"}

[\#]{lang="EN-US"}

[return]{lang="EN-US"}
:::

::: {#99210294 .myid}
[]{#_Toc404782606}[]{#struct_0_14758_17492_1615076959}[]{#_Toc298920485}[]{#_Toc142793100}[]{#_Toc142798652}[]{#_Toc142793101}[]{#_Toc142798653}[]{#_Toc142793102}[]{#_Toc142798654}[]{#_Toc142793103}[]{#_Toc142798655}[]{#_Toc142793104}[]{#_Toc142798656}[]{#_Toc142793105}[]{#_Toc142798657}[]{#_Toc142793106}[]{#_Toc142798658}[]{#_Toc142793107}[]{#_Toc142798659}[]{#_Toc142793109}[]{#_Toc142798661}[]{#_Toc142793110}[]{#_Toc142798662}[]{#_Toc142793111}[]{#_Toc142798663}[]{#_Toc142793112}[]{#_Toc142798664}[]{#_Toc142793113}[]{#_Toc142798665}[]{#_Toc142793114}[]{#_Toc142798666}[]{#_Toc142793115}[]{#_Toc142798667}[]{#_Toc142793120}[]{#_Toc142798672}[]{#_Toc135478246}[]{#_Toc135478247}[]{#_Toc135478248}[]{#_Toc135478249}[]{#_Toc135478250}[]{#_Toc135478251}[]{#_Toc135478252}[]{#_Toc135478253}[]{#_Toc135478254}[]{#_Toc135478255}[]{#_Toc135478256}[]{#_Toc135478257}[]{#_Toc135478258}[]{#_Toc135478259}[]{#_Toc135478260}

**配置文件管理 \-- 配置文件管理命令 \-- reset saved-configuration**

------------------------------------------------------------------------

[**[reset saved-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x1044844961}[命令用来删除设备存储介质中保存的下次启动配置文件。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_561334763}

[**[reset saved-configuration ]{lang="EN-US"}**[\[ **backup** \| **main** \]]{lang="EN-US"}]{#struct_0_14758_17492_203843803}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x2066436615}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14758_17492_279833392}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_x252121671}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_1506901350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_1770287164}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1906213807}

[**[backup]{lang="EN-US"}**]{#struct_0_14758_17492_197630356}[：删除备用下次启动配置文件。]{style="font-family:宋体"}

[**[main]{lang="EN-US"}**]{#struct_0_14758_17492_x1754027581}[：删除主用下次启动配置文件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1458430793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除操作会将配置文件从设备上彻底删除，所以请慎用该命令。（集中式设备]{style="font-family:宋体"}]{#struct_0_14758_17492_x1799936876}[/]{lang="EN-US"}[分布式设备－独立运行模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除操作会将配置文件从所有成员设备上彻底删除，所以请慎用该命令。（集中式]{style="font-family:宋体"}]{#struct_0_14758_17492_x1585243838}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于支持主备用下次启动配置文件的设备，如果当前设备的主备用下次启动配置文件相同，仅执行一次删除操作（假设指定了]{style="font-family:宋体"}]{#struct_0_14758_17492_x1691924113}**[backup]{lang="EN-US"}**[参数），系统只会将相应的下次启动配置文件设置为]{style="font-family:宋体"}[NULL]{lang="EN-US"}[，不会删除该文件，需要再执行一次删除操作（指定]{style="font-family:宋体"}**[main]{lang="EN-US"}**[参数），才能将这个配置文件彻底删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{lang="EN-US" style="font-family:宋体"}**[backup]{lang="EN-US"}**]{#struct_0_14758_17492_1770221628}[和]{lang="EN-US" style="font-family:宋体"}**[main]{lang="EN-US"}**[参数时，缺省使用]{lang="EN-US" style="font-family:宋体"}**[main]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_x311181141}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14758_17492_400186747}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x945525941}[删除主用下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> reset saved-configuration]{lang="EN-US"}]{#struct_0_14758_17492_1329771362}

[The saved configuration file will be erased. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Configuration file in flash: is being cleared.]{lang="EN-US"}

[Please wait \...\...\.....]{lang="EN-US"}

[Configuration file is cleared.]{lang="EN-US"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_14758_17492_1770156092}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x1546063744}[删除主用下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> reset saved-configuration]{lang="EN-US"}]{#struct_0_14758_17492_1690616463}

[The saved configuration file will be erased. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Configuration file in flash: is being cleared.]{lang="EN-US"}

[Please wait \...]{lang="EN-US"}

[..]{lang="EN-US"}

[MainBoard:]{lang="EN-US"}

[Configuration file is cleared.]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Erase next configuration file successfully]{lang="EN-US"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14758_17492_x1014414950}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x1338127019}[删除备用下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> reset saved-configuration backup]{lang="EN-US"}]{#struct_0_14758_17492_1770614844}

[The saved configuration file will be erased. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Configuration file in flash: is being cleared.]{lang="EN-US"}

[Please wait \...]{lang="EN-US"}

[..]{lang="EN-US"}

[MainBoard:]{lang="EN-US"}

[Configuration file is cleared.]{lang="EN-US"}

[Slot 2:]{lang="EN-US"}

[Erase next configuration file successfully]{lang="EN-US"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_14758_17492_63702828}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x868676199}[删除备用下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> reset saved-configuration backup]{lang="EN-US"}]{#struct_0_14758_17492_1770549308}

[The saved configuration file will be erased. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Configuration file in flash: is being cleared.]{lang="EN-US"}

[Please wait \...]{lang="EN-US"}

[..]{lang="EN-US"}

[MainBoard:]{lang="EN-US"}

[Configuration file is cleared.]{lang="EN-US"}

[Chassis 2 Slot 2:]{lang="EN-US"}

[Erase next configuration file successfully]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1863378192}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display saved-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x1008871299}
:::

::: {#-1368840800 .myid}
[]{#_Toc404782607}[]{#struct_0_14758_17492_x27546227}

**配置文件管理 \-- 配置文件管理命令 \-- restore startup-configuration**

------------------------------------------------------------------------

[**[restore startup-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1770483772}[命令用于从指定]{style="font-family:
宋体"}[TFTP]{lang="EN-US"}[服务器上下载配置文件并设置为设备的主用下次启动配置文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1083463396}

[**[restore startup-configuration from]{lang="EN-US"}**[ *tftp-server src-filename*]{lang="EN-US"}]{#struct_0_14758_17492_x728632695}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x59053352}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14758_17492_498780214}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_383481805}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_1868738564}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_1724493465}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_x557674198}

[*[tftp-server]{lang="EN-US"}*]{#struct_0_14758_17492_1770418236}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或主机名。其中，主机名为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["或"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[src-filename]{lang="EN-US"}*]{#struct_0_14758_17492_x1471246419}[：源文件名，]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上将要下载的文件的文件名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_1899702682}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIPS]{lang="EN-US"}]{#struct_0_14758_17492_153382670}[模式下，不支持本命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令会将指定配置文件下载到主用主控板和备用主控板存储介质的根目录下（对于支持存储设备分区的设备，该目录为存储设备的第一个分区），并设置为主用主控板和备用主控板的下次启动配置文件。对于主用主控板和备用主控板使用不同存储介质的情况（如，主用主控板使用]{style="font-family:宋体"}]{#struct_0_14758_17492_x2085213476}[Flash]{lang="EN-US"}[，而备用主控板使用]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡），备份操作失败。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令会将指定配置文件下载到所有成员设备存储介质的根目录下（对于支持存储设备分区的设备，该目录为存储设备的第一个分区），并设置为所有成员设备的主用下次启动配置文件。对于成员设备使用不同存储介质的情况（如，主设备使用]{style="font-family:宋体"}]{#struct_0_14758_17492_x1953099375}[Flash]{lang="EN-US"}[，而从设备使用]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡），备份操作失败。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令会将指定配置文件下载到所有主控板存储介质的根目录下（对于支持存储设备分区的设备，该目录为存储设备的第一个分区），并设置为所有主控板的主用下次启动配置文件。对于主控板使用不同存储介质的情况（如，有些主控板使用]{style="font-family:宋体"}]{#struct_0_14758_17492_1423887791}[Flash]{lang="EN-US"}[，而有些主控板使用]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡），备份操作失败。]{style="font-family:宋体"}[（分布式设备－]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_x475349436}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14758_17492_x1366038354}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_1770876988}[从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上下载]{style="font-family:宋体"}[test.cfg]{lang="EN-US"}[文件作为设备的下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> restore startup-configuration from 2.2.2.2 test.cfg]{lang="EN-US"}]{#struct_0_14758_17492_x741478488}

[Restoring the next startup-configuration file from 2.2.2.2. Please wait\...finished]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_14758_17492_x1390299603}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x589908534}[从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上下载]{style="font-family:宋体"}[config.cfg]{lang="EN-US"}[文件作为设备的主用下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> restore startup-configuration from 2.2.2.2 config.cfg]{lang="EN-US"}]{#struct_0_14758_17492_239116407}

[Restoring the next startup-configuration file from 2.2.2.2. Please wait\...finished.]{lang="EN-US"}

[Now restoring the next startup-configuration file from main board to backup board. Please wait\...finished]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14758_17492_1776033328}[设备]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_1221634467}[从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上下载]{style="font-family:宋体"}[config.cfg]{lang="EN-US"}[文件作为设备的主用下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> restore startup-configuration from 2.2.2.2 config.cfg]{lang="EN-US"}]{#struct_0_14758_17492_1770811452}

[Restoring the next startup-configuration file from 2.2.2.2. Please wait\...finished.]{lang="EN-US"}

[Now restoring the next startup-configuration file from main board to backup board. Please wait\...finished.]{lang="EN-US"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_14758_17492_68468584}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_426694676}[从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器上下载]{style="font-family:宋体"}[config.cfg]{lang="EN-US"}[文件作为设备的主用下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> restore startup-configuration from 2.2.2.2 config.cfg]{lang="EN-US"}]{#struct_0_14758_17492_1935472928}

[Restoring the next startup-configuration file from 2.2.2.2. Please wait\...finished.]{lang="EN-US"}

[Now restoring the next startup-configuration file from main board to backup board. Please wait\...finished.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x624493105}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup startup-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_1197498152}
:::

::: {#-1859589047 .myid}
[]{#_Toc404782608}[]{#struct_0_14758_17492_1971893068}[]{#_Toc298920486}[]{#_Toc206926310}[]{#_Toc98563094}[]{#_Toc210275439}[]{#_Toc210293264}[]{#_Toc213060380}[]{#_Toc213060888}[]{#_Toc213495065}[]{#_Toc210275440}[]{#_Toc210293265}[]{#_Toc213060381}[]{#_Toc213060889}[]{#_Toc213495066}[]{#_Toc210275445}[]{#_Toc210293270}[]{#_Toc213060386}[]{#_Toc213060894}[]{#_Toc213495071}[]{#_Toc210275447}[]{#_Toc210293272}[]{#_Toc213060388}[]{#_Toc213060896}[]{#_Toc213495073}[]{#_Toc145942350}[]{#_Toc145991464}[]{#_Toc146594610}[]{#_Toc141528005}

**配置文件管理 \-- 配置文件管理命令 \-- save**

------------------------------------------------------------------------

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14758_17492_876993537}

[**[save]{lang="EN-US"}**[ *file-url*]{lang="EN-US"}]{#struct_0_14758_17492_x1660453378}[命令用来将设备的当前配置保存到指定文件，但不会将该文件设置为下次启动配置文件。]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \]]{lang="EN-US"}]{#struct_0_14758_17492_1572642444}[命令用来将设备的当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \] \[ **mdc-all** \]]{lang="EN-US"}]{#struct_0_14758_17492_91102710}[命令用来将]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_14758_17492_1915584951}

[**[save]{lang="EN-US"}**[ *file-url* \[ **all** \| **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14758_17492_x1660912130}[命令用来将设备的当前配置保存到指定文件，但不会将该文件设置为下次启动配置文件。]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \]]{lang="EN-US"}]{#struct_0_14758_17492_x969708250}[命令用来将设备的当前配置保存到主用主控板和备用主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \] \[ **mdc-all** \]]{lang="EN-US"}]{#struct_0_14758_17492_1104772236}[命令用来将]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的当前配置保存到主用主控板和备用主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14758_17492_x1775879594}[设备]{lang="EN-US" style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ *file-url* \[ **all** \| **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14758_17492_x1660846594}[命令用来将设备的当前配置保存到指定文件，但不会将该文件设置为下次启动配置文件。]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \]]{lang="EN-US"}]{#struct_0_14758_17492_1828645599}[命令用来将设备的当前配置保存到所有成员设备存储介质的根目录，并将该文件设置为下次启动配置文件。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \] \[ **mdc-all** \]]{lang="EN-US"}]{#struct_0_14758_17492_x1255746092}[命令用来将]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的当前配置保存到主用主控板和备用主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_14758_17492_x1163924721}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[**[save]{lang="EN-US"}***[ file-url]{lang="EN-US"}*[ \[ **all** \| **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14758_17492_x1660781058}[命令用来将设备的当前配置保存到指定文件，但不会将该文件设置为下次启动配置文件。]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \]]{lang="EN-US"}]{#struct_0_14758_17492_x2046385300}[命令用来将设备的当前配置保存到所有主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \] \[ **mdc-all** \]]{lang="EN-US"}]{#struct_0_14758_17492_x1616781654}[命令用来将]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的当前配置保存到主用主控板和备用主控板存储介质的根目录，并将该文件设置为下次启动配置文件。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x958530652}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14758_17492_740160111}

[**[save]{lang="EN-US"}**[ *file-url*]{lang="EN-US"}]{#struct_0_14758_17492_340164056}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \] \[ **mdc-all** \]]{lang="EN-US"}]{#struct_0_14758_17492_1150229424}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14758_17492_1145787790}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ *file-url* \[ **all** \| **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14758_17492_x1968767897}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \] \[ **mdc-all** \]]{lang="EN-US"}]{#struct_0_14758_17492_x356032870}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14758_17492_x2058155924}[模式：]{style="font-family:宋体"}

[**[save]{lang="EN-US"}**[ *file-url* \[ **all** \| **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14758_17492_x1513147188}

[**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \] \[ **mdc-all** \]]{lang="EN-US"}]{#struct_0_14758_17492_x958596188}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_750008016}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14758_17492_1277495909}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_124818004}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_128140219}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_x854553153}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_x330263394}

[*[file-url]{lang="EN-US"}*]{#struct_0_14758_17492_518477443}[：文件路径，文件名部分必须以"]{style="font-family:宋体"}[.cfg]{lang="EN-US"}["为后缀。（集中式设备）]{style="font-family:宋体"}

[*[file-url]{lang="EN-US"}*]{#struct_0_14758_17492_1120221572}[：文件路径，文件名部分必须以"]{style="font-family:宋体"}[.cfg]{lang="EN-US"}["为后缀。当本参数和关键字]{style="font-family:宋体"}**[all]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[一起使用时，本参数不能包含槽位号；如果路径中包含了文件夹，则必须先在相应的主控板上创建该文件夹，否则该主控板上的保存操作将失败。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[*[file-url]{lang="EN-US"}*]{#struct_0_14758_17492_x958661724}[：文件路径，必须以"]{style="font-family:宋体"}[.cfg]{lang="EN-US"}["为后缀。当本参数和关键字]{style="font-family:宋体"}**[all]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[一起使用时，本参数不能包含成员编号，如果路径中包含了文件夹，则必须先在相应的成员设备上创建该文件夹，否则本成员设备上的保存操作将失败。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[*[file-url]{lang="EN-US"}*]{#struct_0_14758_17492_x443706468}[：文件路径，文件名部分必须以"]{style="font-family:宋体"}[.cfg]{lang="EN-US"}["为后缀。当本参数和关键字]{style="font-family:宋体"}**[all]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[一起使用时，本参数不能包含成员编号和槽位号；如果路径中包含了文件夹，则必须先在相应的主控板上创建该文件夹，否则该主控板上的保存操作将失败。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_14758_17492_339639854}[：将当前配置以指定的名称保存到所有主控板。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[或]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数，则保存到主用主控板上。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_14758_17492_x2101892370}**[：]{style="font-family:宋体"}**[将当前配置以指定的名称保存到所有成员设备。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数，则保存到]{style="font-family:宋体"}[Master]{lang="EN-US"}[上。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_14758_17492_x1660060162}**[：]{style="font-family:宋体"}**[将当前配置以指定的名称保存到所有主控板。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}[参数，则保存到全局主用主控板上（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_14758_17492_1879639367}[：将当前配置以指定的名称保存到备用主控板。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[或]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数，则保存到主用主控板上。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_14758_17492_1848187724}[：将当前配置以指定的名称保存到指定从设备。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[参数，则保存到]{style="font-family:宋体"}[Master]{lang="EN-US"}[上。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14758_17492_1236466862}[：将当前配置以指定的名称保存到指定主控板。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定]{style="font-family:宋体"}**[all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}[参数，则保存到全局主用主控板上（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[safely]{lang="EN-US"}**]{#struct_0_14758_17492_x1559811233}[：以安全模式保存配置文件。如果不指定该参数，表示以快速保存方式保存配置文件。]{style="font-family:宋体"}

[**[backup]{lang="EN-US"}**]{#struct_0_14758_17492_1950081986}[：将该文件设置为备用下次启动配置文件。当不指定]{style="font-family:宋体"}**[backup]{lang="EN-US"}**[和]{style="font-family:宋体"}**[main]{lang="EN-US"}**[时，系统缺省使用]{style="font-family:宋体"}**[main]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[main]{lang="EN-US"}**]{#struct_0_14758_17492_x1422610322}[：将该文件设置为主用下次启动配置文件。当不指定]{style="font-family:宋体"}**[backup]{lang="EN-US"}**[和]{style="font-family:宋体"}**[main]{lang="EN-US"}**[时，系统缺省使用]{style="font-family:宋体"}**[main]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[force]{lang="EN-US"}**]{#struct_0_14758_17492_x958727260}[：表示直接将当前配置保存到主用下次启动配置文件，系统不再输出交互信息。缺省情况下，用户执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**[命令，系统要求用户输入]{style="font-family:宋体"}[\<Y\>]{lang="EN-US"}[或]{style="font-family:宋体"}[\<N\>]{lang="EN-US"}[等参数来确认本次操作，如果在]{style="font-family:宋体"}[30]{lang="EN-US"}[秒内没有确认，系统会自动退出本次操作。如果在执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**[操作时使用了]{style="font-family:宋体"}**[force]{lang="EN-US"}**[参数，则系统会直接保存当前配置，不再需要用户输入任何信息。]{style="font-family:宋体"}

[**[mdc-all]{lang="EN-US"}**]{#struct_0_14758_17492_x419380627}[：保存设备上所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[内的配置。不指定该参数时，只保存用户当前登录的]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的当前配置。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_x2042899906}

[[当执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**]{#struct_0_14758_17492_x809414439}[命令时，如果指定的文件名不存在，则系统会先创建该文件，再执行保存操作。如果指定的文件名存在，则会提示用户是否覆盖该文件，如果用户选择不覆盖，则不会继续执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[当执行]{style="font-family:宋体"}**[save]{lang="EN-US"}**[ \[ **safely** \] \[ **backup** \| **main** \] \[ **force** \] \[ **mdc-all** \]]{lang="EN-US"}]{#struct_0_14758_17492_x591674417}[命令输入的文件名和设备上已存在的文件同名时，]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果使用了]{style="font-family:宋体"}]{#struct_0_14758_17492_874117331}**[safely]{lang="EN-US"}**[参数，则系统会先将当前配置保存到一个临时文件，保存成功后，再用这个临时文件替换原同名文件。因此，即使在保存过程中出现设备重启、断电等问题导致配置保存失败，仍然能够以原同名的配置文件启动设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有使用]{style="font-family:宋体"}]{#struct_0_14758_17492_x1372591901}**[safely]{lang="EN-US"}**[参数，则会直接覆盖原同名文件。在保存过程中如果出现设备重启、断电、内存不足等问题，结果是当前配置保存失败，原同名文件已删除，下次启动文件为空。]{style="font-family:宋体"}

[[因此，为了安全起见，在需要将当前配置保存到下次启动配置文件的时候，建议选用]{style="font-family:宋体"}**[safely]{lang="EN-US"}**]{#struct_0_14758_17492_1534618028}[参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14758_17492_866892206}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x958268508}[将当前配置文件保存到指定配置文件]{style="font-family:宋体"}[backup.cfg]{lang="EN-US"}[，但不将该文件设置为下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> save backup.cfg]{lang="EN-US"}]{#struct_0_14758_17492_x487614785}

[The current configuration will be saved to flash:/backup.cfg. Continue? \[Y/N\]:y]{lang="EN-US"}

[Now saving current configuration to the device.]{lang="EN-US"}

[Saving configuration]{lang="EN-US"}

[flash:/backup.cfg. Please wait\...]{lang="EN-US"}

[Configuration is saved to flash successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x2146101344}[直接将当前配置保存到主用下次启动配置文件，不再进行信息确认。]{style="font-family:宋体"}

[[\<Sysname\> save force]{lang="EN-US"}]{#struct_0_14758_17492_2094454017}

[Validating file. Please wait\....]{lang="EN-US"}

[Configuration is saved to device successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_1868701469}[将当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> save]{lang="EN-US"}]{#struct_0_14758_17492_x958334044}

[The current configuration will be written to the device. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.cfg)\[flash:/backup.cfg\]]{lang="EN-US"}

[(To leave the existing filename unchanged, press the enter key):test.cfg]{lang="EN-US"}

[ Validating file. Please wait\...\...\...\...]{lang="EN-US"}

[ Configuration is saved to device successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x438034496}[将当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> save]{lang="EN-US"}]{#struct_0_14758_17492_x1504899270}

[The current configuration will be written to the device. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.cfg)\[flash:/startup.cfg\]]{lang="EN-US"}

[(To leave the existing filename unchanged, press the enter key):]{lang="EN-US"}

[Validating file. Please wait\...]{lang="EN-US"}

[Saved the current configuration to mainboard device successfully.]{lang="EN-US"}

[Slot 1:]{lang="EN-US"}

[Save next configuration file successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x396587047}[将当前配置保存到存储介质的根目录，并将该文件设置为下次启动配置文件。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> save]{lang="EN-US"}]{#struct_0_14758_17492_x2114348379}

[The current configuration will be written to the device. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.cfg)\[flash:/startup.cfg\]]{lang="EN-US"}

[(To leave the existing filename unchanged, press the enter key):]{lang="EN-US"}

[Validating file. Please wait\...]{lang="EN-US"}

[Saved the current configuration to mainboard device successfully.]{lang="EN-US"}

[Chassis 1 Slot 1:]{lang="EN-US"}

[Save next configuration file successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x958399580}[保存所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[内的配置，并将该文件设置为下次启动配置文件。（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> save mdc-all]{lang="EN-US"}]{#struct_0_14758_17492_1101603437}

[Save current configuration in MDC Admin? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.cfg)\[flash:/1.cfg\]]{lang="EN-US"}

[(To leave the existing filename unchanged, press the enter key):]{lang="EN-US"}

[flash:/1.cfg exists, overwrite? \[Y/N\]:y]{lang="EN-US"}

[Validating file. Please wait\...]{lang="EN-US"}

[Saved the current configuration to mainboard device successfully.]{lang="EN-US"}

[Chassis 1 Slot 1:]{lang="EN-US"}

[Save next configuration file successfully.]{lang="EN-US"}

[Save current configuration in MDC mdc1? \[Y/N\]:y]{lang="EN-US"}

[Please input the file name(\*.cfg)\[flash:/mdc1.cfg\]]{lang="EN-US"}

[(To leave the existing filename unchanged, press the enter key):]{lang="EN-US"}

[flash:/mdc1.cfg exists, overwrite? \[Y/N\]:y]{lang="EN-US"}

[Validating file. Please wait\...]{lang="EN-US"}

[Saved the current configuration to mainboard device successfully.]{lang="EN-US"}

[Chassis 1 Slot 1:]{lang="EN-US"}

[Save next configuration file successfully.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_830385930}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display current-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_521295854}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display saved-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x1490839570}
:::

::: {#-174770794 .myid}
[]{#_Toc404782609}[]{#struct_0_14758_17492_x958465116}[]{#_Toc298920487}[]{#_Toc206926312}[]{#_Toc98563095}[]{#_Toc67115447}[]{#_Toc66610533}[]{#_Toc45424897}[]{#_Toc43175518}[]{#_Toc210275449}[]{#_Toc210293274}[]{#_Toc213060390}[]{#_Toc213060898}[]{#_Toc213495075}[]{#_Toc210275452}[]{#_Toc210293277}[]{#_Toc213060393}[]{#_Toc213060901}[]{#_Toc213495078}[]{#_Toc210275453}[]{#_Toc210293278}[]{#_Toc213060394}[]{#_Toc213060902}[]{#_Toc213495079}[]{#_Toc210275454}[]{#_Toc210293279}[]{#_Toc213060395}[]{#_Toc213060903}[]{#_Toc213495080}[]{#_Toc210275455}[]{#_Toc210293280}[]{#_Toc213060396}[]{#_Toc213060904}[]{#_Toc213495081}[]{#_save}

**配置文件管理 \-- 配置文件管理命令 \-- startup saved-configuration**

------------------------------------------------------------------------

[]{#_Toc54490127}[**[startup]{lang="EN-US"}**[ **saved-configuration**]{lang="EN-US"}]{#struct_0_14758_17492_x838816895}[命令用来配置下次启动配置文件（系统下次启动时使用的配置文件）。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **startup saved-configuration**]{lang="EN-US"}]{#struct_0_14758_17492_x1549207064}[命令用来设置设备以出厂配置启动。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_668243819}

[**[startup]{lang="EN-US"}**[ **saved-configuration** *cfgfile* \[ **backup** \| **main** \]]{lang="EN-US"}]{#struct_0_14758_17492_x460868569}

[**[undo startup saved-configuration]{lang="EN-US"}**]{#struct_0_14758_17492_x456426258}

[]{#_Toc54490128}[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14758_17492_1896822506}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14758_17492_x2041811345}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14758_17492_x1154257159}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14758_17492_x958006364}[]{#_Toc54490129}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14758_17492_349124097}

[[network-admin]{lang="EN-US"}]{#struct_0_14758_17492_x51228698}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14758_17492_x1812284632}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14758_17492_923387377}

[*[cfgfile]{lang="EN-US"}*]{#struct_0_14758_17492_x2142459829}[：配置文件的名称，该文件必须是存储介质根目录下、后缀为]{style="font-family:宋体"}[.cfg]{lang="EN-US"}[的文件。]{style="font-family:宋体"}

[**[backup]{lang="EN-US"}**]{#struct_0_14758_17492_530697154}[：将配置文件设置为备用下次启动配置文件。]{style="font-family:宋体"}

[**[main]{lang="EN-US"}**]{#struct_0_14758_17492_1441629814}[：将配置文件设置为主用下次启动配置文件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14758_17492_939613446}

[[主用主控板和备用主控板的下次启动配置文件必须是相同的文件，因此，使用本命令前，请确保指定的配置文件已经保存在主用主控板和备用主控板相同类型存储介质的根目录下，否则，操作失败。（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_14758_17492_x958071900}

[[所有成员设备的下次启动配置文件必须是相同的文件，因此，使用本命令前，请确保指定的配置文件已经保存在所有成员设备相同类型存储介质的根目录下，否则，操作失败。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14758_17492_x1275101942}[设备）]{style="font-family:宋体"}

[[所有成员设备上主控板的下次启动配置文件必须是相同的文件，因此，使用本命令前，请确保指定的配置文件已经保存在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14758_17492_x540407036}[中所有主控板相同类型存储介质的根目录下，否则，操作失败。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[使用该命令设置配置文件时：]{style="font-family:宋体"}]{#struct_0_14758_17492_1929693769}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不指定]{lang="EN-US" style="font-family:宋体"}**[main]{lang="EN-US"}**]{#struct_0_14758_17492_x1462202007}[和]{lang="EN-US" style="font-family:宋体"}**[back]{lang="EN-US"}**[参数时，缺省使用]{lang="EN-US" style="font-family:宋体"}**[main]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主用下次启动配置文件和备用下次启动配置文件可以设置为同一文件，但为了更可靠，建议设置为不同的文件，或者将一份配置保存在两个不同名的文件中，一个设置为主用，一个设置为备用。]{style="font-family:宋体"}]{#struct_0_14758_17492_968003017}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **startup saved-configuration**]{lang="EN-US"}]{#struct_0_14758_17492_x372402944}[命令之后，系统会将主用]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[备用下次启动配置文件均设置为]{lang="EN-US" style="font-family:宋体"}[NULL]{lang="EN-US"}[，但不会删除该文件。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是，执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **startup saved-configuration**]{lang="EN-US"}]{#struct_0_14758_17492_1799154617}[命令并重启]{style="font-family:宋体"}[IRF]{lang="EN-US"}[或]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员设备时，会导致]{style="font-family:宋体"}[IRF]{lang="EN-US"}[分裂，请谨慎使用。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[]{#struct_0_14758_17492_x1799869704}[[【举例】]{style="font-family:黑体"}]{#_Toc54490131}

[[\# ]{lang="EN-US"}]{#struct_0_14758_17492_x958530651}[配置下次启动配置文件。]{style="font-family:宋体"}

[[\<Sysname\> startup saved-configuration testcfg.cfg]{lang="EN-US"}]{#struct_0_14758_17492_740225647}

[Please wait \....]{lang="EN-US"}

[\... Done!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14758_17492_x157355171}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display startup]{lang="EN-US"}**]{#struct_0_14758_17492_x1541821656}
:::
