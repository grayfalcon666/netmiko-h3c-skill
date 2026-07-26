::::: {#440387863 .myid}
[]{#_Toc404799159}[]{#struct_0_x7427_11331_x538333554}

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system internal rawip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化Probe命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7427_11331_1387943655}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7427_11331_x623836747}
:::

[ ]{lang="EN-US"}

[**[display system internal rawip]{lang="EN-US"}**]{#struct_0_x7427_11331_x1218261487}[命令用来显示设备上所有]{style="font-family:
宋体"}[RawIP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x182042622}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7427_11331_512842450}

[**[display system internal rawip]{lang="EN-US"}**]{#struct_0_x7427_11331_x386576140}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7427_11331_1664036357}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ]{lang="EN-US"}**]{#struct_0_x7427_11331_x132575374}[[rawip]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7427_11331_x1810261136}[模式：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ]{lang="EN-US"}**]{#struct_0_x7427_11331_x1246138198}[[rawip]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[[ \[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x1774827677}

[[Probe]{lang="EN-US"}]{#struct_0_x7427_11331_x193058902}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x1218327023}

[[network-admin]{lang="EN-US"}]{#struct_0_x7427_11331_1840722526}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7427_11331_x207398335}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x1484614180}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_407104185}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定单板上获取的所有]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_720481126}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备上获取的所有]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_552848319}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_x2102034423}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定成员设备的指定单板上获取的所有]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_1993310505}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定单板上获取的所有]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x7427_11331_x1077102375}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示从指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[RawIP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::::

::::: {#790843992 .myid}
[]{#_Toc404799160}[]{#struct_0_x7427_11331_637625069}

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system internal tcp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7427_11331_1512707913}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7427_11331_x225805987}
:::

[ ]{lang="EN-US"}

[**[display system internal tcp]{lang="EN-US"}**]{#struct_0_x7427_11331_1179624467}[命令用来显示设备上所有]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x842594517}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7427_11331_x1074905404}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ]{lang="EN-US"}**]{#struct_0_x7427_11331_1510949062}[[tcp]{lang="EN-US"}]{.commandkeywordsChar}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7427_11331_x2100874176}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ]{lang="EN-US"}**]{#struct_0_x7427_11331_x494003870}[[tcp]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7427_11331_x1858222227}[模式：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ]{lang="EN-US"}**]{#struct_0_x7427_11331_1510949544}[[tcp]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x526502850}

[[Probe]{lang="EN-US"}]{#struct_0_x7427_11331_x886248847}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7427_11331_1414963052}

[[network-admin]{lang="EN-US"}]{#struct_0_x7427_11331_1416341042}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7427_11331_x1443983191}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x813678340}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_x63539269}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定单板上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_x635909250}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_1312363206}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_x622783697}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定成员设备的指定单板上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_1715647733}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定单板上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x7427_11331_x1076447015}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示从指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::::

::::: {#1471852824 .myid}
[]{#_Toc404799161}[]{#struct_0_x7427_11331_2017086828}[]{#_Toc384046407}

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system internal tcp-proxy statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7427_11331_726262236}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7427_11331_x1677385132}
:::

[ ]{lang="EN-US"}

[**[display system internal tcp-proxy statistics]{lang="EN-US"}**]{#struct_0_x7427_11331_x325261102}[命令用来]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7427_11331_533689681}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7427_11331_x1787750024}

[**[display system internal tcp-proxy statistics]{lang="EN-US"}**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_x7427_11331_906903480}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7427_11331_347685824}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal tcp-proxy statistics]{lang="EN-US"}**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** } ]{lang="EN-US"}[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x7427_11331_451002887}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7427_11331_x908684042}[模式：]{style="font-family:宋体"}

[**[display system internal tcp-proxy statistics]{lang="EN-US"}**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** }]{lang="EN-US"}[ \[ ]{lang="EN-US"}]{#struct_0_x7427_11331_x810564588}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7427_11331_847160562}

[[Probe]{lang="EN-US"}]{#struct_0_x7427_11331_x378688479}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x177185302}

[[network-admin]{lang="EN-US"}]{#struct_0_x7427_11331_x1852612659}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7427_11331_x739223306}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x1502980469}

[**[all]{lang="EN-US"}**]{#struct_0_x7427_11331_158848863}[：显示所有统计信息。]{style="font-family:宋体"}

[**[api]{lang="EN-US"}**]{#struct_0_x7427_11331_1391251992}[：显示]{style="font-family:宋体"}[API]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x7427_11331_1444471883}[：显示错误统计信息。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x7427_11331_341751797}[：显示状态机统计信息。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x7427_11331_x1115081054}[：显示报文统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7427_11331_776803451}*[slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。如果未指定本参数，则显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7427_11331_x1034023758}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的统计的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7427_11331_1008808826}*[slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7427_11331_x1553283140}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7427_11331_292106957}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x7427_11331_222511321}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7427_11331_327124174}

[[本命令可以显示]{style="font-family:宋体"}[IPv4 TCP]{lang="EN-US"}]{#struct_0_x7427_11331_x613894236}[和]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}[]{#_Toc362455866}[]{#_Toc362455867}[]{#_Toc362455868}[]{#_Toc362455869}[]{#_Toc362455870}[]{#_Toc362455871}[]{#_Toc362455872}[]{#_Toc362455873}[]{#_Toc362455874}[]{#_Toc362455875}[]{#_Toc362455876}[]{#_Toc362455877}[]{#_Toc362455878}[]{#_Toc362455879}[]{#_Toc362455880}[]{#_Toc362455881}[]{#_Toc362455882}[]{#_Toc362455883}[]{#_Toc362455884}[]{#_Toc362455885}[]{#_Toc362455886}[]{#_Toc362455887}[]{#_Toc362455888}[]{#_Toc362455889}[]{#_Toc362455890}[]{#_Toc362455891}[]{#_Toc362455892}[]{#_Toc362455893}[]{#_Toc362455894}[]{#_Toc362455895}[]{#_Toc362455896}[]{#_Toc362455897}[]{#_Toc362455898}[]{#_Toc362455899}[]{#_Toc362455900}[]{#_Toc362455901}[]{#_Toc362455902}[]{#_Toc362455903}[]{#_Toc362455904}[]{#_Toc362455905}[]{#_Toc362455906}[]{#_Toc362455907}[]{#_Toc362455908}[]{#_Toc362455909}[]{#_Toc362455910}[]{#_Toc362455911}[]{#_Toc362455954}
:::::

::::: {#424365000 .myid}
[]{#_Toc404799162}[]{#struct_0_x7427_11331_x987257457}[]{#_Toc362455956}[]{#_Toc362455957}[]{#_Toc362455958}[]{#_Toc362455959}[]{#_Toc362455960}[]{#_Toc362455961}[]{#_Toc362455962}[]{#_Toc362455963}[]{#_Toc362455964}[]{#_Toc362455965}[]{#_Toc362455966}[]{#_Toc362455967}[]{#_Toc362455968}[]{#_Toc362455969}[]{#_Toc362455970}[]{#_Toc362455971}[]{#_Toc362455972}[]{#_Toc362455973}[]{#_Toc362455974}[]{#_Toc362455975}[]{#_Toc362455976}[]{#_Toc362455977}[]{#_Toc362455978}[]{#_Toc362455979}[]{#_Toc362455980}[]{#_Toc362455981}[]{#_Toc362455982}[]{#_Toc362455983}[]{#_Toc362455984}[]{#_Toc362455985}[]{#_Toc362455986}[]{#_Toc362455987}[]{#_Toc362455988}[]{#_Toc362455989}[]{#_Toc362455990}[]{#_Toc362455991}[]{#_Toc362456013}

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system interval tcp-proxy verbose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7427_11331_x1585864172}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7427_11331_x222986800}
:::

[ ]{lang="EN-US"}

[**[display system interval tcp-proxy verbose]{lang="EN-US"}**]{#struct_0_x7427_11331_1613802301}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7427_11331_1793202918}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7427_11331_x1303744583}

[**[display system interval tcp-proxy verbose]{lang="EN-US"}**]{#struct_0_x7427_11331_x339938451}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7427_11331_1889896397}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system interval tcp-proxy verbose slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x7427_11331_x308512000}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7427_11331_x665712627}[模式：]{style="font-family:宋体"}

[**[display system interval tcp-proxy verbose chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number* \[**cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x7427_11331_1806371482}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x52717408}

[[Probe]{lang="EN-US"}]{#struct_0_x7427_11331_x2053624224}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7427_11331_427700333}

[[network-admin]{lang="EN-US"}]{#struct_0_x7427_11331_1360893086}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7427_11331_2124787869}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x481971541}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_2135210470}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定单板上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的详细信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_x1950676909}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的详细信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_x743702318}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的详细信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_x1874595941}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定成员设备的指定单板上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的详细信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[ slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_1919073957}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定单板上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的详细信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x7427_11331_x1472026793}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示从指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接的详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::::

::::: {#790909529 .myid}
[]{#_Toc404799163}[]{#struct_0_x7427_11331_x287041393}

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system internal udp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化Probe命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7427_11331_x842286952}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7427_11331_1286165765}
:::

[ ]{lang="EN-US"}

[**[display system internal udp]{lang="EN-US"}**]{#struct_0_x7427_11331_x1680032164}[命令用来显示设备上所有]{style="font-family:
宋体"}[UDP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7427_11331_1104557589}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7427_11331_x1829142240}

[**[display system internal udp]{lang="EN-US"}**]{#struct_0_x7427_11331_267102762}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7427_11331_645689226}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ]{lang="EN-US"}**]{#struct_0_x7427_11331_x87023780}[[udp]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7427_11331_x361871132}[模式：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ]{lang="EN-US"}**]{#struct_0_x7427_11331_x572615068}[[udp]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x725065581}

[[Probe]{lang="EN-US"}]{#struct_0_x7427_11331_x1336106342}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7427_11331_211459929}

[[network-admin]{lang="EN-US"}]{#struct_0_x7427_11331_x1693308677}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7427_11331_1279042548}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x7427_11331_5578305}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_1728479898}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定单板上获取的所有]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_237391063}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备上获取的所有]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_987834170}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_265674391}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定成员设备的指定单板上获取的所有]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[ slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x7427_11331_1787083424}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定单板上获取的所有]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x7427_11331_x518389032}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示从指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[UDP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::::

::: {#-445407899 .myid}
[]{#_Toc404799164}[]{#struct_0_x7427_11331_x711796527}[]{#_Toc384046409}

**IP性能优化 \-- IP性能优化Probe配置命令 \-- reset system internal tcp-proxy statistics**

------------------------------------------------------------------------

[**[reset system internal tcp-proxy statistics]{lang="EN-US"}**]{#struct_0_x7427_11331_1660856468}[命令用来]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7427_11331_909184619}

[**[reset system internal tcp-proxy statistics]{lang="EN-US"}**]{#struct_0_x7427_11331_x1385865110}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x1357666864}

[[Probe]{lang="EN-US"}]{#struct_0_x7427_11331_x552318904}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7427_11331_1125291807}

[[network-admin]{lang="EN-US"}]{#struct_0_x7427_11331_1458219197}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7427_11331_1274238343}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7427_11331_1906937973}

[[本命令可以清除]{style="font-family:宋体"}[IPv4 TCP]{lang="EN-US"}]{#struct_0_x7427_11331_955744407}[和]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}
:::

::::: {#394616752 .myid}
[]{#_Toc404799165}[]{#struct_0_x7427_11331_x1034129465}

**IP性能优化 \-- IP性能优化Probe配置命令 \-- tcp-proxy statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IP性能优化Probe命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7427_11331_1046342770}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7427_11331_2007456450}
:::

[ ]{lang="EN-US"}

[**[tcp-proxy statistics]{lang="EN-US"}**]{#struct_0_x7427_11331_94772527}[命令用来开始或停止]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理统计计数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x1234759830}

[**[tcp-proxy statistics]{lang="EN-US"}**[ {]{lang="EN-US"}[ **off** \| **on** }]{lang="EN-US"}]{#struct_0_x7427_11331_x586040288}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7427_11331_x1587657731}

[[不进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x7427_11331_x1259122950}[代理统计计数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7427_11331_1660891720}

[[Probe]{lang="EN-US"}]{#struct_0_x7427_11331_2082654048}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7427_11331_295976355}

[[network-admin]{lang="EN-US"}]{#struct_0_x7427_11331_x36259165}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7427_11331_846763461}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7427_11331_1082736512}

[**[off]{lang="EN-US"}**]{#struct_0_x7427_11331_711876680}[：表示停止]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理统计计数。]{style="font-family:宋体"}

[**[on]{lang="EN-US"}**]{#struct_0_x7427_11331_339858448}[：表示开始]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理统计计数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7427_11331_1607148276}

[[本命令可以开始或停止]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[TCP]{lang="EN-US"}]{#struct_0_x7427_11331_2017152364}[和]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理统计计数。]{style="font-family:宋体"}
:::::
