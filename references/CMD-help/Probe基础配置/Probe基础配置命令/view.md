::: {#-1199128229 .myid}
[]{#_Toc404800525}[]{#struct_0_x1308_x6311_1872068442}[]{#_Toc346182467}

**Probe基础配置 \-- Probe基础配置命令 \-- view**

------------------------------------------------------------------------

[[view]{lang="EN-US"}]{#struct_0_x1308_x6311_x456880077}[命令用来查看系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_687665930}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1308_x6311_842857705}

[**[view ]{lang="EN-US"}***[file-path]{lang="EN-US"}*]{#struct_0_x1308_x6311_1523335851}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1308_x6311_x1399400908}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[view ]{lang="EN-US"}***[file-path ]{lang="EN-US"}*[\[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1308_x6311_2008093050}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1308_x6311_x1892244781}[模式：]{style="font-family:宋体"}

[**[view ]{lang="EN-US"}***[file-path ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1308_x6311_1504326787}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_x911536838}

[[Probe]{lang="EN-US"}]{#struct_0_x1308_x6311_1468513203}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_x1063931654}

[[network-admin]{lang="EN-US"}]{#struct_0_x1308_x6311_x698589396}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1308_x6311_x1161556839}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_1523270315}

[*[file-path]{lang="EN-US"}*]{#struct_0_x1308_x6311_1309553698}[：要查看文件的路径，区分大小写。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x1308_x6311_x1821987147}*[slot-number]{lang="EN-US"}*[：查看指定单板系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件的内容。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x1308_x6311_x121340144}*[slot-number]{lang="EN-US"}*[：查看指定设备系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件的内容。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x1308_x6311_x1498077292}*[slot-number]{lang="EN-US"}*[：查看指定设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件的内容。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1308_x6311_1693843707}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：查看指定设备上单板系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件的内容。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示主用主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1308_x6311_x1905154924}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：查看单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件的内容。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示主用主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_x1902708269}

[[执行该命令显示的文件路径中不能包含文件链接。文件链接类似于文件的快捷方式，文件链接指向另一个文件或目录。通过文件链接可以访问到其所指向的文件或目录。]{style="font-family:宋体"}]{#struct_0_x1308_x6311_1502541045}
:::

::: {#-353399185 .myid}
[]{#_Toc404800526}[]{#struct_0_x1308_x6311_x1865659081}[]{#_Toc346182468}[]{#_Toc360005658}[]{#_Toc360005769}[]{#_Toc360005659}[]{#_Toc360005770}[]{#_Toc360005660}[]{#_Toc360005771}[]{#_Toc360005661}[]{#_Toc360005772}[]{#_Toc360005662}[]{#_Toc360005773}[]{#_Toc360005663}[]{#_Toc360005774}[]{#_Toc360005664}[]{#_Toc360005775}[]{#_Toc360005665}[]{#_Toc360005776}[]{#_Toc360005666}[]{#_Toc360005777}[]{#_Toc360005667}[]{#_Toc360005778}[]{#_Toc360005668}[]{#_Toc360005779}[]{#_Toc360005669}[]{#_Toc360005780}[]{#_Toc360005670}[]{#_Toc360005781}[]{#_Toc360005671}[]{#_Toc360005782}[]{#_Toc360005672}[]{#_Toc360005783}[]{#_Toc360005673}[]{#_Toc360005784}[]{#_Toc360005674}[]{#_Toc360005785}[]{#_Toc360005675}[]{#_Toc360005786}[]{#_Toc360005676}[]{#_Toc360005787}[]{#_Toc360005677}[]{#_Toc360005788}[]{#_Toc360005678}[]{#_Toc360005789}[]{#_Toc360005679}[]{#_Toc360005790}[]{#_Toc360005680}[]{#_Toc360005791}[]{#_Toc360005681}[]{#_Toc360005792}[]{#_Toc360005682}[]{#_Toc360005793}[]{#_Toc360005683}[]{#_Toc360005794}[]{#_Toc360005684}[]{#_Toc360005795}[]{#_Toc360005685}[]{#_Toc360005796}[]{#_Toc360005686}[]{#_Toc360005797}[]{#_Toc360005687}[]{#_Toc360005798}[]{#_Toc360005688}[]{#_Toc360005799}[]{#_Toc360005689}[]{#_Toc360005800}[]{#_Toc360005690}[]{#_Toc360005801}[]{#_Toc360005691}[]{#_Toc360005802}[]{#_Toc360005692}[]{#_Toc360005803}[]{#_Toc360005693}[]{#_Toc360005804}[]{#_Toc360005694}[]{#_Toc360005805}

**Probe基础配置 \-- Probe基础配置命令 \-- list**

------------------------------------------------------------------------

[**[list]{lang="EN-US"}**]{#struct_0_x1308_x6311_x1024029981}[命令用来查看系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件和子目录的相关信息，且文件路径中不能包含文件链接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_x1644029431}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1308_x6311_153183764}

[**[list ]{lang="EN-US"}***[file-path]{lang="EN-US"}*]{#struct_0_x1308_x6311_784905797}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1308_x6311_x1383606}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[list ]{lang="EN-US"}***[file-path ]{lang="EN-US"}*[\[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1308_x6311_1523073707}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1308_x6311_1670812080}[模式：]{style="font-family:宋体"}

[**[list ]{lang="EN-US"}***[file-path ]{lang="EN-US"}*[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1308_x6311_644095292}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_x1741406784}

[[Probe]{lang="EN-US"}]{#struct_0_x1308_x6311_x293207972}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_x1212179945}

[[network-admin]{lang="EN-US"}]{#struct_0_x1308_x6311_x707105390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1308_x6311_x1557579812}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_x827780743}

[*[file-path]{lang="EN-US"}*]{#struct_0_x1308_x6311_2081423735}[：要查看的文件或目录的路径，区分大小写。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x1308_x6311_1633744605}*[slot-number]{lang="EN-US"}*[：查看指定单板系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件和子目录的相关信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x1308_x6311_1523008171}*[slot-number]{lang="EN-US"}*[：查看指定设备系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件和子目录的相关信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}**]{#struct_0_x1308_x6311_1634090590}*[slot-number]{lang="EN-US"}*[：查看指定设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件和子目录的相关信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1308_x6311_2041370814}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：查看指定设备上单板系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件和子目录的相关信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1308_x6311_x625339117}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：查看单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[系统目录（]{style="font-family:宋体"}[/proc/]{lang="EN-US"}[、]{style="font-family:宋体"}[/sys/]{lang="EN-US"}[、]{style="font-family:宋体"}[/var/]{lang="EN-US"}[）下的文件和子目录的相关信息。]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}
:::

::: {#-1509900112 .myid}
[]{#_Toc404800527}[]{#struct_0_x1308_x6311_847562497}[]{#_Toc346182469}[]{#_Toc360005696}[]{#_Toc360005807}[]{#_Toc360005697}[]{#_Toc360005808}[]{#_Toc360005698}[]{#_Toc360005809}[]{#_Toc360005699}[]{#_Toc360005810}[]{#_Toc360005700}[]{#_Toc360005811}[]{#_Toc360005701}[]{#_Toc360005812}[]{#_Toc360005702}[]{#_Toc360005813}[]{#_Toc360005703}[]{#_Toc360005814}[]{#_Toc360005704}[]{#_Toc360005815}[]{#_Toc360005705}[]{#_Toc360005816}[]{#_Toc360005706}[]{#_Toc360005817}[]{#_Toc360005707}[]{#_Toc360005818}[]{#_Toc360005708}[]{#_Toc360005819}[]{#_Toc360005709}[]{#_Toc360005820}[]{#_Toc360005710}[]{#_Toc360005821}[]{#_Toc360005711}[]{#_Toc360005822}[]{#_Toc360005712}[]{#_Toc360005823}[]{#_Toc360005713}[]{#_Toc360005824}[]{#_Toc360005714}[]{#_Toc360005825}[]{#_Toc360005715}[]{#_Toc360005826}[]{#_Toc360005716}[]{#_Toc360005827}[]{#_Toc360005717}[]{#_Toc360005828}[]{#_Toc360005718}[]{#_Toc360005829}[]{#_Toc360005719}[]{#_Toc360005830}[]{#_Toc360005720}[]{#_Toc360005831}[]{#_Toc360005721}[]{#_Toc360005832}[]{#_Toc360005722}[]{#_Toc360005833}[]{#_Toc360005723}[]{#_Toc360005834}[]{#_Toc360005724}[]{#_Toc360005835}[]{#_Toc360005725}[]{#_Toc360005836}[]{#_Toc360005726}[]{#_Toc360005837}[]{#_Toc360005727}[]{#_Toc360005838}[]{#_Toc360005728}[]{#_Toc360005839}[]{#_Toc360005729}[]{#_Toc360005840}[]{#_Toc360005730}[]{#_Toc360005841}[]{#_Toc360005731}[]{#_Toc360005842}[]{#_Toc360005732}[]{#_Toc360005843}[]{#_Toc360005733}[]{#_Toc360005844}[]{#_Toc360005734}[]{#_Toc360005845}[]{#_Toc360005735}[]{#_Toc360005846}[]{#_Toc360005736}[]{#_Toc360005847}[]{#_Toc360005737}[]{#_Toc360005848}[]{#_Toc360005738}[]{#_Toc360005849}[]{#_Toc360005739}[]{#_Toc360005850}[]{#_Toc360005740}[]{#_Toc360005851}[]{#_Toc360005741}[]{#_Toc360005852}[]{#_Toc360005742}[]{#_Toc360005853}[]{#_Toc360005743}[]{#_Toc360005854}[]{#_Toc360005744}[]{#_Toc360005855}[]{#_Toc360005745}[]{#_Toc360005856}[]{#_Toc360005746}[]{#_Toc360005857}[]{#_Toc360005747}[]{#_Toc360005858}[]{#_Toc360005748}[]{#_Toc360005859}[]{#_Toc360005749}[]{#_Toc360005860}[]{#_Toc360005750}[]{#_Toc360005861}[]{#_Toc360005751}[]{#_Toc360005862}[]{#_Toc360005763}[]{#_Toc360005874}

**Probe基础配置 \-- Probe基础配置命令 \-- probe**

------------------------------------------------------------------------

[**[probe]{lang="EN-US"}**]{#struct_0_x1308_x6311_1523335852}[命令用来从系统视图进入]{style="font-family:宋体"}[Probe]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_x1399466444}

[**[probe]{lang="EN-US"}**]{#struct_0_x1308_x6311_588567523}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_663006776}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1308_x6311_1652726214}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_1226402060}

[[network-admin]{lang="EN-US"}]{#struct_0_x1308_x6311_995630224}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1308_x6311_505567746}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1308_x6311_341828760}

[[在]{style="font-family:宋体"}[Probe]{lang="EN-US"}]{#struct_0_x1308_x6311_x859082500}[视图下，用户可以通过命令查看系统的状态和信息，以便对系统故障进行诊断。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
