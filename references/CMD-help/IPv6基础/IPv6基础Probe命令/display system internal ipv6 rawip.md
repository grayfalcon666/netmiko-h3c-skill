::::: {#1584765948 .myid}
[]{#_Toc404799041}[]{#struct_0_x2623_x1107_360297371}

**IPv6基础 \-- IPv6基础Probe命令 \-- display system internal ipv6 rawip**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础Probe命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2623_x1107_x1466456636}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2623_x1107_607618059}
:::

[ ]{lang="EN-US"}

[**[display system internal ipv6 rawip]{lang="EN-US"}**]{#struct_0_x2623_x1107_x497215704}[命令用来显示设备上所有]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_723878740}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x2044020787}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ipv6 rawip]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_x1104608451}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x798876723}[模式：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ipv6 rawip]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_2118455264}[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1149261559}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_486324406}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1733152270}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1657536054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x2132842298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x553573986}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_1587385504}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定单板上获取的所有]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_733200027}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备上获取的所有]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_944633982}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_770636694}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定成员设备的指定单板上获取的所有]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_958233462}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定单板上获取的所有]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_121416992}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示从指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[IPv6 RawIP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::::

::::: {#10050807 .myid}
[]{#_Toc404799042}[]{#struct_0_x2623_x1107_x1609660852}

**IPv6基础 \-- IPv6基础Probe命令 \-- display system internal ipv6 tcp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2623_x1107_2025234010}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2623_x1107_x1840163662}
:::

[ ]{lang="EN-US"}

[**[display system internal ipv6 tcp]{lang="EN-US"}**]{#struct_0_x2623_x1107_1460159253}[命令用来显示设备上所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_319234933}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_914917883}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ipv6 tcp]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_x1553463658}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x1663062576}[模式：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ipv6 tcp]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_935989804}[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1934563203}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_990183487}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1325798635}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1733348880}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x291784179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x370870093}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x442957046}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定单板上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1880831320}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1831303540}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1573982819}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定成员设备的指定单板上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[ slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1262084939}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定单板上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_2077732124}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示从指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::::

::::: {#-1912197958 .myid}
[]{#_Toc404799043}[]{#struct_0_x2623_x1107_1749751361}

**IPv6基础 \-- IPv6基础Probe命令 \-- display system internal ipv6 udp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础Probe命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2623_x1107_1196931081}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2623_x1107_1733283345}
:::

[ ]{lang="EN-US"}

[**[display system internal ipv6 udp]{lang="EN-US"}**]{#struct_0_x2623_x1107_914983419}[命令用来显示设备上所有]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_495292401}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x1007110421}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ipv6 udp]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_755384840}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_1876799850}[模式：]{style="font-family:宋体"}

[[[display ]{lang="EN-US"}]{.commandkeywordsChar}**[system internal ipv6 udp]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_914496312}[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number]{lang="EN-US"}]{.commandparameterChar}[[ \]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1733348881}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x291718643}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1081638548}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_893346218}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_636622702}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_973235776}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_1733414417}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定单板上获取的所有]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x677232085}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备上获取的所有]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x668504126}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接的摘要信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x2058884342}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定成员设备的指定单板上获取的所有]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_2060379229}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定单板上获取的所有]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_2077732135}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示从指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[IPv6 UDP]{lang="EN-US"}[连接的摘要信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::::

::::: {#1860413812 .myid}
[]{#_Toc404799044}[]{#struct_0_x2623_x1107_x1716590399}[]{#_Toc401672473}[]{#_Toc384046407}[]{#_Toc362453029}[]{#_Toc362454449}[]{#_Toc362453030}[]{#_Toc362454450}[]{#_Toc362453031}[]{#_Toc362454451}[]{#_Toc362453032}[]{#_Toc362454452}[]{#_Toc362453033}[]{#_Toc362454453}[]{#_Toc362453034}[]{#_Toc362454454}[]{#_Toc362453035}[]{#_Toc362454455}[]{#_Toc362453036}[]{#_Toc362454456}[]{#_Toc362453037}[]{#_Toc362454457}[]{#_Toc362453038}[]{#_Toc362454458}[]{#_Toc362453039}[]{#_Toc362454459}[]{#_Toc362453040}[]{#_Toc362454460}[]{#_Toc362453041}[]{#_Toc362454461}[]{#_Toc362453042}[]{#_Toc362454462}[]{#_Toc362453043}[]{#_Toc362454463}[]{#_Toc362453044}[]{#_Toc362454464}[]{#_Toc362453045}[]{#_Toc362454465}[]{#_Toc362453046}[]{#_Toc362454466}[]{#_Toc362453047}[]{#_Toc362454467}[]{#_Toc362453048}[]{#_Toc362454468}[]{#_Toc362453049}[]{#_Toc362454469}[]{#_Toc362453050}[]{#_Toc362454470}[]{#_Toc362453051}[]{#_Toc362454471}[]{#_Toc362453052}[]{#_Toc362454472}[]{#_Toc362453053}[]{#_Toc362454473}[]{#_Toc362453054}[]{#_Toc362454474}[]{#_Toc362453055}[]{#_Toc362454475}[]{#_Toc362453056}[]{#_Toc362454476}[]{#_Toc362453057}[]{#_Toc362454477}[]{#_Toc362453058}[]{#_Toc362454478}[]{#_Toc362453059}[]{#_Toc362454479}[]{#_Toc362453060}[]{#_Toc362454480}[]{#_Toc362453061}[]{#_Toc362454481}[]{#_Toc362453062}[]{#_Toc362454482}[]{#_Toc362453063}[]{#_Toc362454483}[]{#_Toc362453064}[]{#_Toc362454484}[]{#_Toc362453065}[]{#_Toc362454485}[]{#_Toc362453066}[]{#_Toc362454486}[]{#_Toc362453067}[]{#_Toc362454487}[]{#_Toc362453068}[]{#_Toc362454488}[]{#_Toc362453069}[]{#_Toc362454489}[]{#_Toc362453070}[]{#_Toc362454490}[]{#_Toc362453071}[]{#_Toc362454491}[]{#_Toc362453072}[]{#_Toc362454492}[]{#_Toc362453073}[]{#_Toc362454493}[]{#_Toc362453074}[]{#_Toc362454494}[]{#_Toc362453075}[]{#_Toc362454495}[]{#_Toc362453076}[]{#_Toc362454496}[]{#_Toc362453119}[]{#_Toc362454539}

**IPv6基础 \-- IPv6基础Probe命令 \-- display system internal tcp-proxy statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2623_x1107_x644750663}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2623_x1107_x613871246}
:::

[ ]{lang="EN-US"}

[**[display system internal tcp-proxy statistics]{lang="EN-US"}**]{#struct_0_x2623_x1107_1012292956}[命令用来]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_653335604}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x126743104}

[**[display system internal tcp-proxy statistics]{lang="EN-US"}**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_x2623_x1107_1692229452}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x693289088}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal tcp-proxy statistics]{lang="EN-US"}**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** } ]{lang="EN-US"}[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2623_x1107_827067399}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x993279246}[模式：]{style="font-family:宋体"}

[**[display system internal tcp-proxy statistics]{lang="EN-US"}**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** }]{lang="EN-US"}[ \[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_1182141452}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x272765965}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_437936241}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_2143750426}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1266251705}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_450816495}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2025791250}

[**[all]{lang="EN-US"}**]{#struct_0_x2623_x1107_1372327173}[：显示所有统计信息。]{style="font-family:宋体"}

[**[api]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1374389200}[：显示]{style="font-family:宋体"}[API]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x2623_x1107_456270969}[：显示错误统计信息。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x2623_x1107_367267561}[：显示状态机统计信息。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1022522728}[：显示报文统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_221721292}*[slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。如果未指定本参数，则显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_230035242}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_1472867730}*[slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_x1680966905}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2623_x1107_1462631650}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_930072608}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_257370831}

[[本命令可以显示]{style="font-family:宋体"}[IPv4 TCP]{lang="EN-US"}]{#struct_0_x2623_x1107_1682670479}[和]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}
:::::

::::: {#232650353 .myid}
[]{#_Toc404799045}[]{#struct_0_x2623_x1107_1094154026}[]{#_Toc362453121}[]{#_Toc362454541}[]{#_Toc362453122}[]{#_Toc362454542}[]{#_Toc362453123}[]{#_Toc362454543}[]{#_Toc362453124}[]{#_Toc362454544}[]{#_Toc362453125}[]{#_Toc362454545}[]{#_Toc362453126}[]{#_Toc362454546}[]{#_Toc362453127}[]{#_Toc362454547}[]{#_Toc362453128}[]{#_Toc362454548}[]{#_Toc362453129}[]{#_Toc362454549}[]{#_Toc362453130}[]{#_Toc362454550}[]{#_Toc362453131}[]{#_Toc362454551}[]{#_Toc362453132}[]{#_Toc362454552}[]{#_Toc362453133}[]{#_Toc362454553}[]{#_Toc362453134}[]{#_Toc362454554}[]{#_Toc362453135}[]{#_Toc362454555}[]{#_Toc362453136}[]{#_Toc362454556}[]{#_Toc362453137}[]{#_Toc362454557}[]{#_Toc362453138}[]{#_Toc362454558}[]{#_Toc362453139}[]{#_Toc362454559}[]{#_Toc362453140}[]{#_Toc362454560}[]{#_Toc362453141}[]{#_Toc362454561}[]{#_Toc362453142}[]{#_Toc362454562}[]{#_Toc362453143}[]{#_Toc362454563}[]{#_Toc362453144}[]{#_Toc362454564}[]{#_Toc362453145}[]{#_Toc362454565}[]{#_Toc362453146}[]{#_Toc362454566}[]{#_Toc362453147}[]{#_Toc362454567}[]{#_Toc362453148}[]{#_Toc362454568}[]{#_Toc362453149}[]{#_Toc362454569}[]{#_Toc362453150}[]{#_Toc362454570}[]{#_Toc362453151}[]{#_Toc362454571}[]{#_Toc362453152}[]{#_Toc362454572}[]{#_Toc362453153}[]{#_Toc362454573}[]{#_Toc362453154}[]{#_Toc362454574}[]{#_Toc362453155}[]{#_Toc362454575}[]{#_Toc362453156}[]{#_Toc362454576}[]{#_Toc362453157}[]{#_Toc362454577}[]{#_Toc362453158}[]{#_Toc362454578}[]{#_Toc362453159}[]{#_Toc362454579}[]{#_Toc362453160}[]{#_Toc362454580}[]{#_Toc362453161}[]{#_Toc362454581}[]{#_Toc362453162}[]{#_Toc362454582}[]{#_Toc362453163}[]{#_Toc362454583}[]{#_Toc362453164}[]{#_Toc362454584}[]{#_Toc362453186}[]{#_Toc362454606}

**IPv6基础 \-- IPv6基础Probe命令 \-- display system interval ipv6 tcp-proxy verbose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2623_x1107_1868638968}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2623_x1107_x276189524}
:::

[ ]{lang="EN-US"}

[**[display system interval ipv6 tcp-proxy verbose]{lang="EN-US"}**]{#struct_0_x2623_x1107_573302919}[命令用来显示]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_466170972}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x909955809}

[**[display system interval ipv6 tcp-proxy verbose]{lang="EN-US"}**]{#struct_0_x2623_x1107_x85575474}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x1511710660}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system interval ipv6 tcp-proxy verbose slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[ \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_1328866006}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x937211486}[模式：]{style="font-family:宋体"}

[**[display system interval ipv6 tcp-proxy verbose chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number* \[**cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x1141936818}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x763209142}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x944508832}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1818927546}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1635616611}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1341559314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1975355045}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_1108644599}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定单板上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的详细信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_242742811}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的详细信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1515795268}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示从指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的详细信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x199674738}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定成员设备的指定单板上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的详细信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[ slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_252843605}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示从指定单板上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的详细信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1085391185}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示从指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上获取的所有]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理连接的详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::::

::: {#-1636904674 .myid}
[]{#_Toc404799046}[]{#struct_0_x2623_x1107_x150440922}[]{#_Toc401672477}[]{#_Toc384046409}

**IPv6基础 \-- IPv6基础Probe命令 \-- reset system internal tcp-proxy statistics**

------------------------------------------------------------------------

[**[reset system internal tcp-proxy statistics]{lang="EN-US"}**]{#struct_0_x2623_x1107_784593547}[命令用来]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理连接]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1873857895}

[**[reset system internal tcp-proxy statistics]{lang="EN-US"}**]{#struct_0_x2623_x1107_686979853}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_2146472041}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x1716524863}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x573673739}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1246656346}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1227978770}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1117139920}

[[本命令可以清除]{style="font-family:宋体"}[IPv4 TCP]{lang="EN-US"}]{#struct_0_x2623_x1107_x20335063}[和]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}
:::

::::: {#969824644 .myid}
[]{#_Toc404799047}[]{#struct_0_x2623_x1107_736293124}[]{#_Toc401672478}

**IPv6基础 \-- IPv6基础Probe命令 \-- tcp-proxy statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6基础Probe命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2623_x1107_1624420294}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2623_x1107_x1098697884}
:::

[ ]{lang="EN-US"}

[**[tcp-proxy statistics]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1625670842}[命令用来开始或停止]{style="font-family:宋体"}[TCP]{lang="EN-US"}[代理统计计数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1012358492}

[**[tcp-proxy statistics]{lang="EN-US"}**[ {]{lang="EN-US"}[ **off** \| **on** }]{lang="EN-US"}]{#struct_0_x2623_x1107_607300121}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_2143920872}

[[不进行]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}]{#struct_0_x2623_x1107_x1792985595}[代理统计计数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1196739328}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_1486314260}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_937576959}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_515651908}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1590541145}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1562229256}

[**[off]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1266186169}[：表示停止]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理统计计数。]{style="font-family:宋体"}

[**[on]{lang="EN-US"}**]{#struct_0_x2623_x1107_x807127664}[：表示开始]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理统计计数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x17019222}

[[本命令可以开始或停止]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[TCP]{lang="EN-US"}]{#struct_0_x2623_x1107_459598640}[和]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[代理统计计数。]{style="font-family:宋体"}
:::::

::: {#-547780918 .myid}
[]{#_Toc404799049}[]{#struct_0_x2623_x1107_x1030614675}[]{#_Toc350325821}

**IPv6基础 \-- ND Probe命令 \-- debugging system internal nd**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x297558376}

[**[debugging system internal nd]{lang="EN-US"}**[ { **notify** \| **sync** }]{lang="EN-US"}]{#struct_0_x2623_x1107_1669038385}

[**[undo debugging system internal nd]{lang="EN-US"}**[ { **notify** \| **sync** }]{lang="EN-US"}]{#struct_0_x2623_x1107_x1945129237}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x356854557}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_1424760988}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1733611022}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1845387205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1551526341}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1693731808}

[**[notify]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1263311819}**[：]{style="font-family:宋体"}**[表示邻居发现的通知调试开关。]{style="font-family:宋体"}

[**[sync]{lang="EN-US"}**]{#struct_0_x2623_x1107_1849112275}**[：]{style="font-family:宋体"}** [表示邻居发现的同步调试开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1091930528}

[**[debugging system internal nd]{lang="EN-US"}**]{#struct_0_x2623_x1107_2047435178}[命令用来打开邻居发现的调试信息开关。]{style="font-family:
宋体"}**[undo debugging system internal nd]{lang="EN-US"}**[命令用来关闭邻居发现的外部通知调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，邻居发现的调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x2623_x1107_474153413}
:::

::: {#-1835068327 .myid}
[]{#_Toc404799050}[]{#struct_0_x2623_x1107_x1343005556}[]{#_Toc402876865}[]{#_Toc397517373}

**IPv6基础 \-- ND Probe命令 \-- debugging system internal nd sub-features**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2008780502}

[**[debugging system internal nd sub-features]{lang="EN-US"}**[ { **all** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x2623_x1107_x286799840}

[**[undo debugging system internal nd sub-features]{lang="EN-US"}**]{#struct_0_x2623_x1107_x801631028}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x829528515}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x898128366}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1784184636}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_2040237354}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_80605193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1760815978}

[**[all]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1357725461}[：表示]{style="font-family:宋体"}[ND]{lang="EN-US"}[子特性的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1125726727}[：表示]{style="font-family:宋体"}[ND]{lang="EN-US"}[子特性的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x2623_x1107_2052268673}[：表示]{style="font-family:宋体"}[ND]{lang="EN-US"}[子特性的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_422624545}

[**[debugging system internal nd sub-features]{lang="EN-US"}**]{#struct_0_x2623_x1107_988987731}[命令用来打开]{style="font-family:宋体"}[ND]{lang="EN-US"}[子特性的调试开关。]{style="font-family:宋体"}**[undo debugging system internal nd sub-features]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ND]{lang="EN-US"}[子特性的调试开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_x2623_x1107_x1972571182}[子特性的调试开关处于关闭状态。]{style="font-family:宋体"}
:::

::: {#86819929 .myid}
[]{#_Toc404799051}[]{#struct_0_x2623_x1107_x291390954}[]{#_Toc350325822}[]{#_Toc362453259}[]{#_Toc362454679}[]{#_Toc362453260}[]{#_Toc362454680}[]{#_Toc362453261}[]{#_Toc362454681}[]{#_Toc362453262}[]{#_Toc362454682}[]{#_Toc362453263}[]{#_Toc362454683}[]{#_Toc362453264}[]{#_Toc362454684}[]{#_Toc362453265}[]{#_Toc362454685}[]{#_Toc362453266}[]{#_Toc362454686}[]{#_Toc362453267}[]{#_Toc362454687}[]{#_Toc362453268}[]{#_Toc362454688}[]{#_Toc362453269}[]{#_Toc362454689}[]{#_Toc362453270}[]{#_Toc362454690}[]{#_Toc362453271}[]{#_Toc362454691}[]{#_Toc362453272}[]{#_Toc362454692}[]{#_Toc362453273}[]{#_Toc362454693}[]{#_Toc362453274}[]{#_Toc362454694}[]{#_Toc362453275}[]{#_Toc362454695}[]{#_Toc362453276}[]{#_Toc362454696}[]{#_Toc362453277}[]{#_Toc362454697}[]{#_Toc362453335}[]{#_Toc362454755}[]{#_Toc362453336}[]{#_Toc362454756}[]{#_Toc362453373}[]{#_Toc362454793}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd dad**

------------------------------------------------------------------------

[**[display system internal nd dad]{lang="EN-US"}**]{#struct_0_x2623_x1107_66921929}[命令用来显示]{style="font-family:宋体"}[DAD]{lang="EN-US"}[链信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1483841836}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_713273988}

[**[display system internal nd dad]{lang="EN-US"}**]{#struct_0_x2623_x1107_926165765}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_779198826}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal nd dad]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x795960519}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_1733414412}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd dad]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x677428693}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x428450385}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x2044067488}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x148614299}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1661615915}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_147626641}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1733479948}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1073462065}[：显示指定单板的]{style="font-family:宋体"}[DAD]{lang="EN-US"}[链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x368285238}[：显示指定成员设备的]{style="font-family:宋体"}[DAD]{lang="EN-US"}[链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1831238004}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[DAD]{lang="EN-US"}[链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_16869286}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[DAD]{lang="EN-US"}[链信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_897645351}[：显示指定单板的]{style="font-family:宋体"}[DAD]{lang="EN-US"}[链信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_121416989}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[DAD]{lang="EN-US"}[链信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#102841125 .myid}
[]{#_Toc404799052}[]{#struct_0_x2623_x1107_x2115654855}[]{#_Toc350325840}[]{#_Toc362453375}[]{#_Toc362454795}[]{#_Toc362453376}[]{#_Toc362454796}[]{#_Toc362453377}[]{#_Toc362454797}[]{#_Toc362453378}[]{#_Toc362454798}[]{#_Toc362453379}[]{#_Toc362454799}[]{#_Toc362453380}[]{#_Toc362454800}[]{#_Toc362453381}[]{#_Toc362454801}[]{#_Toc362453382}[]{#_Toc362454802}[]{#_Toc362453383}[]{#_Toc362454803}[]{#_Toc362453384}[]{#_Toc362454804}[]{#_Toc362453397}[]{#_Toc362454817}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd entry**

------------------------------------------------------------------------

[**[display system internal nd entry]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1871428711}[命令用来显示各板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1733611021}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x1845321669}

[**[display system internal nd entry]{lang="EN-US"}**]{#struct_0_x2623_x1107_x161221707}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x806054595}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd entry]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_1885324001}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_1850034689}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd entry]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_1514295965}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1182950201}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x1860929973}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1732627981}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1314305807}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x990616807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1060761699}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_739570177}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1732693517}[：显示指定成员设备的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x668373054}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_124881268}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x811827506}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_503754014}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1778812109 .myid}
[]{#_Toc404799053}[]{#struct_0_x2623_x1107_x717840912}[]{#_Toc350325856}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd ifcb**

------------------------------------------------------------------------

[**[display system internal nd ifcb]{lang="EN-US"}**]{#struct_0_x2623_x1107_890032929}[命令用来显示接口的]{style="font-family:宋体"}[ND]{lang="EN-US"}[控制块信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x995468939}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_689996110}

[**[display system internal nd ifcb interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_916244276}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_1772902948}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd ifcb interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_1513954585}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_2069157489}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd ifcb interface]{lang="EN-US"}**[ *interface-type interface-number * **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_1939502895}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1344798135}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x995403403}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1790888020}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1959152946}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1880416742}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_570187808}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x995337867}[：显示指定接口的]{style="font-family:宋体"}[ND]{lang="EN-US"}[控制块信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1828952677}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[控制块信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1083055090}[：显示指定成员设备的]{style="font-family:宋体"}[ND]{lang="EN-US"}[控制块信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_494426360}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[控制块信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x485573008}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[控制块信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1658370682}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[控制块信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_503754012}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[控制块信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-212973693 .myid}
[]{#_Toc404799054}[]{#struct_0_x2623_x1107_622995046}[]{#_Toc350325877}[]{#_Toc362453399}[]{#_Toc362454819}[]{#_Toc362453400}[]{#_Toc362454820}[]{#_Toc362453401}[]{#_Toc362454821}[]{#_Toc362453402}[]{#_Toc362454822}[]{#_Toc362453403}[]{#_Toc362454823}[]{#_Toc362453404}[]{#_Toc362454824}[]{#_Toc362453405}[]{#_Toc362454825}[]{#_Toc362453406}[]{#_Toc362454826}[]{#_Toc362453407}[]{#_Toc362454827}[]{#_Toc362453408}[]{#_Toc362454828}[]{#_Toc362453424}[]{#_Toc362454844}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd machash**

------------------------------------------------------------------------

[**[display system internal nd machash]{lang="EN-US"}**]{#struct_0_x2623_x1107_440604420}[命令用来显示各板上的]{style="font-family:宋体"}[machash]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1609113261}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x1290834322}

[**[display system internal nd machash vlan ]{lang="EN-US"}***[vlan-id ipv6-address]{lang="EN-US"}*]{#struct_0_x2623_x1107_x221380127}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_1752826105}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd machash vlan ]{lang="EN-US"}***[vlan-id ipv6-address]{lang="EN-US"}*[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x1330091930}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_1318065044}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd machash vlan ]{lang="EN-US"}***[vlan-id ipv6-address]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x995534474}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x575080331}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x1244003939}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1441979789}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x245605334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1486048324}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x995468938}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x2623_x1107_689930574}[:]{lang="EN-US" style="font-family:宋体"}[显]{style="font-family:宋体"}[示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[*[IPv6-address]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1422485414}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x18577475}[：显示指定单板的]{style="font-family:宋体"}[machash]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x52095114}[：显示指定成员设备的]{style="font-family:宋体"}[machash]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_944765054}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[machash]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x995403402}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[machash]{lang="EN-US"}[表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1427822405}[：显示指定单板的]{style="font-family:宋体"}[machash]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1452561120}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[machash]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-18971423 .myid}
[]{#_Toc404799055}[]{#struct_0_x2623_x1107_1532724714}[]{#_Toc350325823}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd probe**

------------------------------------------------------------------------

[**[display system internal nd probe]{lang="EN-US"}**]{#struct_0_x2623_x1107_x115981748}[命令用来显示探测链信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2069012893}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_1732627980}

[**[display system internal nd probe]{lang="EN-US"}**]{#struct_0_x2623_x1107_1314240271}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_567936360}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd probe]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x269838144}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x2042594068}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd probe]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_856188844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_2049952136}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_1858555091}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1732693516}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_124946804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1281353766}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1484063480}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_298975951}[：显示指定单板的探测链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x553436524}[：显示指定成员设备的探测链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_2060444765}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[探测链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1733152269}[：显示指定成员设备上指定单板的探测链信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_2115836473}[：显示指定单板的探测链信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1834898145}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的探测链信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-215083218 .myid}
[]{#_Toc404799056}[]{#struct_0_x2623_x1107_1320115717}[]{#_Toc362453426}[]{#_Toc362454846}[]{#_Toc362453427}[]{#_Toc362454847}[]{#_Toc362453428}[]{#_Toc362454848}[]{#_Toc362453429}[]{#_Toc362454849}[]{#_Toc362453430}[]{#_Toc362454850}[]{#_Toc362453431}[]{#_Toc362454851}[]{#_Toc362453432}[]{#_Toc362454852}[]{#_Toc362453433}[]{#_Toc362454853}[]{#_Toc362453434}[]{#_Toc362454854}[]{#_Toc362453435}[]{#_Toc362454855}[]{#_Toc362453448}[]{#_Toc362454868}[]{#_Toc350325825}[]{#_Toc350325826}[]{#_Toc350325827}[]{#_Toc350325828}[]{#_Toc350325829}[]{#_Toc350325830}[]{#_Toc350325831}[]{#_Toc350325832}[]{#_Toc350325833}[]{#_Toc350325834}[]{#_Toc350325835}[]{#_Toc350325836}[]{#_Toc350325837}[]{#_Toc350325838}[]{#_Toc350325839}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd rbhash**

------------------------------------------------------------------------

[**[display system internal nd rbhash]{lang="EN-US"}**]{#struct_0_x2623_x1107_407819761}[命令用来显示指定板上]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1320181253}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_1149151329}

[**[display system internal nd rbhash vlan ]{lang="EN-US"}***[vlan-id ipv6-address]{lang="EN-US"}*]{#struct_0_x2623_x1107_1623570512}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x1767099589}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd rbhash vlan ]{lang="EN-US"}***[vlan-id ipv6-address ]{lang="EN-US"}***[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_541212779}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_1123575974}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd rbhash vlan ]{lang="EN-US"}***[vlan-id ipv6-address]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_833541479}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2079302707}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x1526608761}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1319591430}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x923693082}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_125853555}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2024612508}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1569295831}[:]{lang="EN-US" style="font-family:宋体"}[显]{style="font-family:宋体"}[示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[上]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x2623_x1107_x78415494}[：显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址上]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_732305102}[：显示指定单板的]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1691250957}[：显示指定成员设备的]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1784183837}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x811092561}[：表示指定成员设备上指定单板的]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_944699518}[：显示指定单板的]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_2131428590}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[rbhash]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-306010917 .myid}
[]{#_Toc404799057}[]{#struct_0_x2623_x1107_x903939281}[]{#_Toc350325824}[]{#_Toc362453450}[]{#_Toc362454870}[]{#_Toc362453451}[]{#_Toc362454871}[]{#_Toc362453452}[]{#_Toc362454872}[]{#_Toc362453453}[]{#_Toc362454873}[]{#_Toc362453454}[]{#_Toc362454874}[]{#_Toc362453455}[]{#_Toc362454875}[]{#_Toc362453456}[]{#_Toc362454876}[]{#_Toc362453457}[]{#_Toc362454877}[]{#_Toc362453458}[]{#_Toc362454878}[]{#_Toc362453488}[]{#_Toc362454908}[]{#_Toc350325841}[]{#_Toc350325842}[]{#_Toc350325843}[]{#_Toc350325844}[]{#_Toc350325845}[]{#_Toc350325846}[]{#_Toc350325847}[]{#_Toc350325848}[]{#_Toc350325849}[]{#_Toc350325850}[]{#_Toc350325851}[]{#_Toc350325852}[]{#_Toc350325853}[]{#_Toc350325854}[]{#_Toc350325855}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd reload**

------------------------------------------------------------------------

[**[display system internal nd reload]{lang="EN-US"}**]{#struct_0_x2623_x1107_x793900222}[命令用来显示重刷链信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x950655349}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_1671211976}

[**[display system internal nd reload]{lang="EN-US"}**]{#struct_0_x2623_x1107_x2037006160}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x232087881}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd reload]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_1733348877}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x291325418}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd reload]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x1505131626}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2108680278}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x1723186508}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x486524940}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1362237243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1733414413}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x677494229}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1298737940}[：显示指定单板的重刷链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_814017669}[：显示指定成员设备的重刷链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1300995414}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[重刷链信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1669946909}[：显示指定成员设备上指定单板的重刷链信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x924948021}[：显示指定单板的重刷链信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1834898148}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的重刷链信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#622245145 .myid}
[]{#_Toc404799058}[]{#struct_0_x2623_x1107_1319722502}[]{#_Toc354748820}[]{#_Toc362453490}[]{#_Toc362454910}[]{#_Toc362453491}[]{#_Toc362454911}[]{#_Toc362453492}[]{#_Toc362454912}[]{#_Toc362453493}[]{#_Toc362454913}[]{#_Toc362453494}[]{#_Toc362454914}[]{#_Toc362453495}[]{#_Toc362454915}[]{#_Toc362453496}[]{#_Toc362454916}[]{#_Toc362453497}[]{#_Toc362454917}[]{#_Toc362453498}[]{#_Toc362454918}[]{#_Toc362453499}[]{#_Toc362454919}[]{#_Toc362453500}[]{#_Toc362454920}[]{#_Toc362453501}[]{#_Toc362454921}[]{#_Toc362453502}[]{#_Toc362454922}[]{#_Toc362453503}[]{#_Toc362454923}[]{#_Toc362453504}[]{#_Toc362454924}[]{#_Toc362453505}[]{#_Toc362454925}[]{#_Toc362453506}[]{#_Toc362454926}[]{#_Toc362453507}[]{#_Toc362454927}[]{#_Toc362453508}[]{#_Toc362454928}[]{#_Toc362453545}[]{#_Toc362454965}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd rule**

------------------------------------------------------------------------

[**[display system internal nd rule]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1679156338}[命令用来显示]{style="font-family:宋体"}[ND]{lang="EN-US"}[规则信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1412194349}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_2036903936}

[**[display system internal nd rule ]{lang="EN-US"}**[{ **all** \| **interface** *interface-type* *interface-number* \[ *ipv6-*]{lang="EN-US"}]{#struct_0_x2623_x1107_522877929}*[address]{lang="SV" style="color:black"}[ ]{lang="SV"}*[\] }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_1319788038}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal nd rule ]{lang="EN-US"}**[{ **all** \| **interface** *interface-type* *interface-number* \[ *ipv6-*]{lang="EN-US"}]{#struct_0_x2623_x1107_x1364088417}*[address]{lang="SV" style="color:black"}[ ]{lang="SV"}*[\] } **slot**]{lang="EN-US"}*[ slot-number  ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x1171166334}[模式：]{style="font-family:宋体"}

[**[display system internal nd rule ]{lang="EN-US"}**[{ **all** \| **interface** *interface-type* *interface-number* \[ *ipv6-*]{lang="EN-US"}]{#struct_0_x2623_x1107_1817181607}*[address]{lang="SV" style="color:black"}[ ]{lang="SV"}*[\] } **chassis**]{lang="EN-US"}[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1017212821}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_600719892}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_570534618}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1319853574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x106060207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_426569854}

[**[all]{lang="EN-US"}**]{#struct_0_x2623_x1107_2130877107}[：显示所有]{style="font-family:宋体"}[ND]{lang="EN-US"}[规则信息。]{style="font-family:宋体"}

[**[interface ]{lang="SV" style="color:black"}**]{#struct_0_x2623_x1107_x1297765951}*[interface-type interface-number]{lang="SV" style="color:
black"}*[：]{style="font-family:宋体;
color:black"}[显示指定接口的]{style="font-family:宋体;color:black"}[ND]{lang="EN-US" style="color:black"}[规则信息]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;color:black"}*[interface-type interface-number]{lang="SV" style="color:black"}*[表示接口类型和接口编号。]{style="font-family:宋体;color:black"}

[*[ipv6-]{lang="SV"}*]{#struct_0_x2623_x1107_503785700}*[address]{lang="SV" style="color:black"}*[：显示的指定]{style="font-family:宋体;
color:black"}[IPv6]{lang="SV" style="color:black"}[地址的]{style="font-family:宋体;color:black"}[ND]{lang="SV" style="color:black"}[规则信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体;
color:black"}

[**[slot]{lang="SV"}**]{#struct_0_x2623_x1107_x1837783842}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板]{style="font-family:宋体"}[ND]{lang="SV"}[规则]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[所在的槽位号。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_x2623_x1107_1319919110}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备的]{style="font-family:宋体"}[ND]{lang="SV"}[规则]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_x2623_x1107_x1831172468}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="SV"}[规则]{style="font-family:
宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:
宋体"}*[slot-number]{lang="SV"}*[表示]{style="font-family:
宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_x2126236612}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ND]{lang="SV"}[规则]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[所在的槽位号。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_897710887}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="SV"}[规则]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_x1334138404}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="SV"}[规则]{style="font-family:
宋体"}[信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#2017447727 .myid}
[]{#_Toc404799059}[]{#struct_0_x2623_x1107_x1851904167}[]{#_Toc402876874}[]{#_Toc397517883}[]{#_Toc395012452}[]{#_Toc389743202}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd snooping**

------------------------------------------------------------------------

[**[display system internal nd snooping]{lang="EN-US"}**]{#struct_0_x2623_x1107_x4634035}[命令用来显示]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1565958232}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x539578931}

[**[display system internal nd snooping ]{lang="EN-US"}**[\[ **count** \| **global** \| **link-local** \]]{lang="EN-US"}]{#struct_0_x2623_x1107_1719830348}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_339477536}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal nd snooping slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \[ **count** \| **global** \| **link-local** \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x285820226}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x722582160}[模式：]{style="font-family:宋体"}

[**[display system internal nd snooping chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \[ **count** \| **global** \| **link-local** \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x1974211980}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x929403971}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_430792494}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2096766970}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1229672750}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1858260078}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_2079335764}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1992724435}[：显示指定单板的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1136274107}[：显示指定成员设备的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1071661809}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_719765546}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x786588720}[：显示指定单板的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_1025875956}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x2623_x1107_1306645770}[：显示]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项的总个数。]{style="font-family:宋体"}

[**[global       ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x135763288}[：显示表项地址为全球单播地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[link-local]{lang="EN-US"}**]{#struct_0_x2623_x1107_397367129}[：显示表项地址为链路本地地址的]{style="font-family:宋体"}[ND Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}
:::

::: {#-1569116956 .myid}
[]{#_Toc404799060}[]{#struct_0_x2623_x1107_x995665549}[]{#_Toc350325896}[]{#_Toc362453547}[]{#_Toc362454967}[]{#_Toc362453548}[]{#_Toc362454968}[]{#_Toc362453549}[]{#_Toc362454969}[]{#_Toc362453550}[]{#_Toc362454970}[]{#_Toc362453551}[]{#_Toc362454971}[]{#_Toc362453552}[]{#_Toc362454972}[]{#_Toc362453553}[]{#_Toc362454973}[]{#_Toc362453554}[]{#_Toc362454974}[]{#_Toc362453555}[]{#_Toc362454975}[]{#_Toc362453556}[]{#_Toc362454976}[]{#_Toc362453557}[]{#_Toc362454977}[]{#_Toc362453558}[]{#_Toc362454978}[]{#_Toc362453559}[]{#_Toc362454979}[]{#_Toc362453560}[]{#_Toc362454980}[]{#_Toc362453590}[]{#_Toc362455010}[]{#_Toc350325878}[]{#_Toc350325879}[]{#_Toc350325880}[]{#_Toc350325881}[]{#_Toc350325882}[]{#_Toc350325883}[]{#_Toc350325884}[]{#_Toc350325885}[]{#_Toc350325886}[]{#_Toc350325887}[]{#_Toc350325888}[]{#_Toc350325889}[]{#_Toc350325890}[]{#_Toc350325891}[]{#_Toc350325892}[]{#_Toc350325893}[]{#_Toc350325894}[]{#_Toc350325895}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd static**

------------------------------------------------------------------------

[**[display system internal nd static]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1358003140}[命令用来显示]{style="font-family:宋体"}[ND]{lang="EN-US"}[静态配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2130367742}

[**[display system internal nd static ]{lang="EN-US"}***[ipv6-address ]{lang="EN-US"}***[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_864984947}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1321895970}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_1466373111}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1063170497}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_408703910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x995600013}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_622929510}

[*[IPv6-address]{lang="EN-US"}*]{#struct_0_x2623_x1107_x738740152}[:]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x725228872}[：显示指定接口的信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}
:::

::: {#-465909223 .myid}
[]{#_Toc404799061}[]{#struct_0_x2623_x1107_x1432550571}[]{#_Toc350325916}[]{#_Toc362453592}[]{#_Toc362455012}[]{#_Toc362453593}[]{#_Toc362455013}[]{#_Toc362453594}[]{#_Toc362455014}[]{#_Toc362453595}[]{#_Toc362455015}[]{#_Toc362453596}[]{#_Toc362455016}[]{#_Toc362453597}[]{#_Toc362455017}[]{#_Toc362453598}[]{#_Toc362455018}[]{#_Toc362453599}[]{#_Toc362455019}[]{#_Toc362453600}[]{#_Toc362455020}[]{#_Toc362453601}[]{#_Toc362455021}[]{#_Toc362453602}[]{#_Toc362455022}[]{#_Toc362453603}[]{#_Toc362455023}[]{#_Toc362453604}[]{#_Toc362455024}[]{#_Toc362453605}[]{#_Toc362455025}[]{#_Toc362453606}[]{#_Toc362455026}[]{#_Toc362453607}[]{#_Toc362455027}[]{#_Toc362453646}[]{#_Toc362455066}[]{#_Toc350325897}[]{#_Toc350325898}[]{#_Toc350325899}[]{#_Toc350325900}[]{#_Toc350325901}[]{#_Toc350325902}[]{#_Toc350325903}[]{#_Toc350325904}[]{#_Toc350325905}[]{#_Toc350325906}[]{#_Toc350325907}[]{#_Toc350325908}[]{#_Toc350325909}[]{#_Toc350325910}[]{#_Toc350325911}[]{#_Toc350325912}[]{#_Toc350325913}[]{#_Toc350325914}[]{#_Toc350325915}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd statistics**

------------------------------------------------------------------------

[**[display system internal nd statistics]{lang="EN-US"}**]{#struct_0_x2623_x1107_x996189837}[命令用来显示各板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x195228626}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_922517673}

[**[display system internal nd statistics]{lang="EN-US"}**]{#struct_0_x2623_x1107_x2010683246}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_1652880467}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd statistics]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x755031026}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x1863746293}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal nd statistics]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_221030760}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x995731084}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x2099269195}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1110403048}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_951494348}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1972291132}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x995665548}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1358068676}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_163471209}[：显示指定成员设备的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x265022991}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1745354230}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1378421133}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1452561113}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#749835800 .myid}
[]{#_Toc404799062}[]{#struct_0_x2623_x1107_x360997245}[]{#_Toc375570854}[]{#_Toc374544075}[]{#_Toc373592993}

**IPv6基础 \-- ND Probe命令 \-- display system internal nd suppression xconnect-group verbose**

------------------------------------------------------------------------

[**[display system internal nd suppression xconnect-group verbose]{lang="EN-US"}**]{#struct_0_x2623_x1107_x360669565}[命令用来显示]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2088636085}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x1412800501}

[**[display system internal nd suppression xconnect-group verbose]{lang="EN-US"}**]{#struct_0_x2623_x1107_x183351619}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_1652472101}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal nd suppression xconnect-group verbose]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x360604029}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_580187120}[模式：]{style="font-family:宋体"}

[**[display system internal nd suppression xconnect-group verbose]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x457406951}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1492924138}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x634443279}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1356835020}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x360800637}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1403462089}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x938198472}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1774290659}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_201798989}[：显示指定成员设备的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_897776423}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1482106767}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x568319754}[：显示指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_x360735101}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[泛洪抑制表项的详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1839333199 .myid}
[]{#struct_0_x2623_x1107_1106925715}[]{#_Toc404799063}[]{#_Toc350325934}[]{#_Toc362453648}[]{#_Toc362455068}[]{#_Toc362453649}[]{#_Toc362455069}[]{#_Toc362453650}[]{#_Toc362455070}[]{#_Toc362453651}[]{#_Toc362455071}[]{#_Toc362453652}[]{#_Toc362455072}[]{#_Toc362453653}[]{#_Toc362455073}[]{#_Toc362453654}[]{#_Toc362455074}[]{#_Toc362453655}[]{#_Toc362455075}[]{#_Toc362453656}[]{#_Toc362455076}[]{#_Toc362453657}[]{#_Toc362455077}[]{#_Toc362453658}[]{#_Toc362455078}[]{#_Toc362453659}[]{#_Toc362455079}[]{#_Toc362453660}[]{#_Toc362455080}[]{#_Toc362453661}[]{#_Toc362455081}[]{#_Toc362453662}[]{#_Toc362455082}[]{#_Toc362453663}[]{#_Toc362455083}[]{#_Toc362453664}[]{#_Toc362455084}[]{#_Toc362453665}[]{#_Toc362455085}[]{#_Toc362453666}[]{#_Toc362455086}[]{#_Toc362453667}[]{#_Toc362455087}[]{#_Toc362453668}[]{#_Toc362455088}[]{#_Toc362453669}[]{#_Toc362455089}[]{#_Toc362453751}[]{#_Toc362455171}[]{#_Toc350325917}[]{#_Toc350325918}[]{#_Toc350325919}[]{#_Toc350325920}[]{#_Toc350325921}[]{#_Toc350325922}[]{#_Toc350325923}[]{#_Toc350325924}[]{#_Toc350325925}[]{#_Toc350325926}[]{#_Toc350325927}[]{#_Toc350325928}[]{#_Toc350325929}[]{#_Toc350325930}[]{#_Toc350325931}[]{#_Toc350325932}[]{#_Toc350325933}

**IPv6基础 \-- ND Probe命令 \-- reset system internal nd statistics**

------------------------------------------------------------------------

[**[reset system internal nd statistics]{lang="EN-US"}**]{#struct_0_x2623_x1107_2451915}[命令用来清除各板上的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1428959773}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x129411404}

[**[reset ]{lang="EN-US"}[system internal nd statistics]{lang="EN-US"}**]{#struct_0_x2623_x1107_x995337871}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_1828821606}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset ]{lang="EN-US"}[system internal nd statistics slot ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x1647925389}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x1832795810}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[reset system internal nd statistics]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_358858228}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1349355030}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_1128392235}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1120869692}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_896355410}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x995272335}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1798323274}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x201917697}[：清除指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x691646559}[：清除指定成员设备的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_2060575837}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1736052641}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_2117373554}[：清除指定单板的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x263082724}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ND]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#2054204105 .myid}
[]{#_Toc404799065}[]{#struct_0_x2623_x1107_1670687149}[]{#_Toc350255568}

**IPv6基础 \-- IPv6地址管理 Probe命令 \-- display system internal ipv6 address**

------------------------------------------------------------------------

[**[display system internal ipv6 address]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1737655353}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址详细信息]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_292926550}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x1057896116}

[**[display system internal ipv6 address]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ **interface** *interface-type interface-number* \] \[ *ipv6-address* \] ]{lang="EN-US"}]{#struct_0_x2623_x1107_214353475}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x256023281}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 address]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ **interface** *interface-type interface-number* \] \[ *ipv6-address* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x996189839}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x195883986}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 address]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ **interface** *interface-type interface-number* \] \[ *ipv6-address* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2623_x1107_940624096}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_787235254}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x886766502}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1027002813}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1967975591}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x995731086}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x2099400267}

[*[ipv6-address]{lang="SV" style="color:black"}*]{#struct_0_x2623_x1107_x814726875}[：显示的指定]{style="font-family:宋体;
color:black"}[IPv6]{lang="SV" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[**[vpn-instance]{lang="SV" style="color:black"}**]{#struct_0_x2623_x1107_1418836981}*[ vpn-instance-name]{lang="SV" style="color:black"}*[：]{style="font-family:宋体;
color:black"}[ ]{style="color:black"}[显示指定]{style="font-family:
宋体;color:black"}[VPN]{lang="SV" style="color:black"}[的]{style="font-family:宋体;color:black"}[IPv6]{lang="SV" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[**[interface ]{lang="SV" style="color:black"}**]{#struct_0_x2623_x1107_x1690964645}*[interface-type interface-number]{lang="SV" style="color:
black"}*[：]{style="font-family:宋体;
color:black"}[显示指定接口的]{style="font-family:宋体;color:black"}[IPv6]{lang="SV" style="color:black"}[地址]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;color:black"}*[interface-type interface-number]{lang="SV" style="color:black"}*[表示接口类型和接口编号。]{style="font-family:宋体;color:black"}

[**[slot]{lang="SV" style="color:black"}**]{#struct_0_x2623_x1107_80023970}[ *slot-number*]{lang="SV" style="color:black"}[：]{style="font-family:宋体;color:black"}[显示指定单板上的]{style="font-family:宋体;
color:black"}[IPv6]{lang="SV" style="color:black"}[地址]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;
color:black"}*[slot-number]{lang="SV" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。（分布式设备－独立运行模式）]{style="font-family:宋体;
color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x995665550}[：显示指定成员设备上的]{style="font-family:
宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。（集中式]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1784052765}[：显示指定成员设备]{style="font-family:
宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号或者]{style="font-family:宋体;color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[上的]{style="font-family:宋体;
color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1358592965}[：显示指定成员设备上指定单板的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址，]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体;
color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）（不支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1543255297}[：显示指定单板的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号或者]{style="font-family:宋体;color:black"}[PEX]{lang="EN-US" style="color:black"}[的虚拟框号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板或]{style="font-family:
宋体;color:black"}[PEX]{lang="EN-US" style="color:black"}[所在的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_2075569441}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;
color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1912348837 .myid}
[]{#_Toc404799067}[]{#struct_0_x2623_x1107_119397079}[]{#_Toc347747846}

**IPv6基础 \-- IPv6 PathMTU Probe命令 \-- display system internal ipv6 pathmtu**

------------------------------------------------------------------------

[**[display system internal ipv6 pathmtu]{lang="EN-US"}**]{#struct_0_x2623_x1107_x2106173553}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息，信息全局同步。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x774462020}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_x1602496851}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 pathmtu]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { *ipv6-address* \| { **all** \| **dynamic** \| **static** } \[ **count** \] } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2623_x1107_926845361}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x1693659456}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 pathmtu ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] { *ipv6-address* \| { **all** \| **dynamic** \| **static** } \[ **count** \] } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x190365375}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_357008284}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x970713674}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1781364540}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1357793796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1675639080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1800307230}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x2623_x1107_926910897}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示公网的]{style="font-family:宋体"}[IPv6 PMTU]{lang="EN-US"}[信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x2623_x1107_x518402848}[：显示到达指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2623_x1107_2031741290}[：显示所有公网的]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[dynamic]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1095003177}[：显示所有动态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1006681948}[：显示所有静态]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x2623_x1107_x2004469284}[：显示]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项数目。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_x1992762337}[：显示指定单板上的所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。如果未指定本参数，则显示所有单板上所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_1405932036}[：显示指定成员设备上的所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_x1428281157}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_926976433}[：显示指定成员设备上指定单板上的所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。如果未指定本参数，则显示所有单板上的所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_1300602198}[：显示指定单板上的所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位号。如果未指定本参数，则显示所有单板上的所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_119254304}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[PMTU]{lang="EN-US"}[表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-109470462 .myid}
[]{#_Toc343257217}[]{#_Toc404799069}[]{#struct_0_x2623_x1107_725755126}[]{#_Toc350241013}[]{#_Toc343257221}

**IPv6基础 \-- Fib6 Probe命令 \-- debugging system internal ipv6 fib prefix**

------------------------------------------------------------------------

[**[debugging system internal ipv6 fib prefix]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1482385837}[命令用来]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo debugging system internal ipv6 fib prefix]{lang="EN-US"}**]{#struct_0_x2623_x1107_1472134228}[命令用来]{style="font-family:宋体"}[关闭]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_926583214}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x1388094570}

[**[debugging system internal ipv6 fib prefix]{lang="EN-US"}**[ { **all** \| **message** \| **hardware** }]{lang="EN-US"}]{#struct_0_x2623_x1107_373036288}

[**[undo debugging system internal ipv6 fib prefix]{lang="EN-US"}**[ { **all** \| **message** \| **hardware** }]{lang="EN-US"}]{#struct_0_x2623_x1107_x544475787}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_2061153156}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging system internal ipv6 fib prefix]{lang="EN-US"}**[ { **all** \| **message** \| **hardware** } **slot** ]{lang="EN-US"}]{#struct_0_x2623_x1107_934323382}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[**[undo debugging system internal ipv6 fib prefix]{lang="EN-US"}**[ { **all** \| **message** \| **hardware** } **slot** ]{lang="EN-US"}]{#struct_0_x2623_x1107_x383718141}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_6725681}[模式：]{style="font-family:宋体"}

[**[debugging system internal ipv6 fib prefix]{lang="EN-US"}**[ { **all** \| **message** \| **hardware** } **chassis** ]{lang="EN-US"}]{#struct_0_x2623_x1107_926648750}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[**[undo debugging system internal ipv6 fib prefix ]{lang="EN-US"}**[{ **all** \| **message** \| **hardware** } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x2623_x1107_x21585619}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_749845598}

[[IPv6 FIB]{lang="EN-US"}]{#struct_0_x2623_x1107_x688874484}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_258611169}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_1892474675}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1719544466}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x436349205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x987426193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_926714286}

[**[all]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1562420499}[：]{style="font-family:宋体"}[打开所有调试开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1095037146}[：]{style="font-family:宋体"}[打开前缀消息调试开关，打印路由下发和板间同步的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀消息。]{style="font-family:宋体"}

[**[hardware]{lang="EN-US"}**]{#struct_0_x2623_x1107_953865220}[：]{style="font-family:宋体"}[打开下驱动信息调试开关，打印下发驱动信息以及驱动返回的消息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x2128798794}[：]{style="font-family:宋体"}[打开指定单板的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_614347744}[：]{style="font-family:宋体"}[打开指定成员设备的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1831565684}[：]{style="font-family:宋体"}[打开指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_x272572726}[：]{style="font-family:宋体"}[打开指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[调试信息开关，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_897317671}[：]{style="font-family:宋体"}[打开指定单板的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1837060825}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[打开指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1202708180 .myid}
[]{#_Toc404799070}[]{#struct_0_x2623_x1107_1518108986}[]{#_Toc350241014}[]{#_Toc362453979}[]{#_Toc362455399}[]{#_Toc362453980}[]{#_Toc362455400}[]{#_Toc362453981}[]{#_Toc362455401}[]{#_Toc362453982}[]{#_Toc362455402}[]{#_Toc362453983}[]{#_Toc362455403}[]{#_Toc362453984}[]{#_Toc362455404}[]{#_Toc362453985}[]{#_Toc362455405}[]{#_Toc362453986}[]{#_Toc362455406}[]{#_Toc362453987}[]{#_Toc362455407}[]{#_Toc362453988}[]{#_Toc362455408}[]{#_Toc362453989}[]{#_Toc362455409}[]{#_Toc362453990}[]{#_Toc362455410}[]{#_Toc362454048}[]{#_Toc362455468}[]{#_Toc362454049}[]{#_Toc362455469}[]{#_Toc362454050}[]{#_Toc362455470}[]{#_Toc362454051}[]{#_Toc362455471}[]{#_Toc362454052}[]{#_Toc362455472}[]{#_Toc362454053}[]{#_Toc362455473}[]{#_Toc362454054}[]{#_Toc362455474}[]{#_Toc362454055}[]{#_Toc362455475}[]{#_Toc362454056}[]{#_Toc362455476}[]{#_Toc362454057}[]{#_Toc362455477}[]{#_Toc362454058}[]{#_Toc362455478}[]{#_Toc362454059}[]{#_Toc362455479}[]{#_Toc362454060}[]{#_Toc362455480}[]{#_Toc362454061}[]{#_Toc362455481}[]{#_Toc362454062}[]{#_Toc362455482}[]{#_Toc362454063}[]{#_Toc362455483}[]{#_Toc362454064}[]{#_Toc362455484}[]{#_Toc362454065}[]{#_Toc362455485}[]{#_Toc362454066}[]{#_Toc362455486}[]{#_Toc362454067}[]{#_Toc362455487}[]{#_Toc362454068}[]{#_Toc362455488}[]{#_Toc362454069}[]{#_Toc362455489}[]{#_Toc362454070}[]{#_Toc362455490}[]{#_Toc362454071}[]{#_Toc362455491}[]{#_Toc362454072}[]{#_Toc362455492}[]{#_Toc362454073}[]{#_Toc362455493}[]{#_Toc362454074}[]{#_Toc362455494}[]{#_Toc362454075}[]{#_Toc362455495}[]{#_Toc362454076}[]{#_Toc362455496}[]{#_Toc362454077}[]{#_Toc362455497}[]{#_Toc362454234}[]{#_Toc362455654}

**IPv6基础 \-- Fib6 Probe命令 \-- display system internal ipv6 fib prefix**

------------------------------------------------------------------------

[**[display system internal ipv6 fib prefix]{lang="EN-US"}**]{#struct_0_x2623_x1107_1593551317}[命令用来显示]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1577983123}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_1450169728}

[**[display system internal ipv6 fib prefix ]{lang="EN-US"}**[\[ **vpn-instance** ]{lang="EN-US"}]{#struct_0_x2623_x1107_x1268820691}[[vpn-instance-name ]{lang="EN-US"}]{.commandparameterChar}[\]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_496412407}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 fib prefix]{lang="EN-US"}**[ \[ **vpn-instance** ]{lang="EN-US"}]{#struct_0_x2623_x1107_1761874129}[[vpn-instance-name]{lang="EN-US"}]{.commandparameterChar}[ \] **slot** ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x1802758891}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 fib prefix ]{lang="EN-US"}**[\[**vpn-instance** ]{lang="EN-US"}*[vpn-instance-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}[ **chassis** ]{lang="EN-US"}]{#struct_0_x2623_x1107_1092943603}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}**[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x702350923}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x119475938}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1511403631}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1068279506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x354737199}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_783008376}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x2623_x1107_x1802300138}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则显示公网的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_1925281728}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x1963480901}[：]{style="font-family:宋体"}[显示指定成员设备的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2623_x1107_x668766270}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_x69081690}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2623_x1107_2060117085}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_501591335}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀基本信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1720693750 .myid}
[]{#_Toc404799071}[]{#struct_0_x2623_x1107_369353946}[]{#_Toc350241016}[]{#_Toc343257219}[]{#_Toc362454236}[]{#_Toc362455656}[]{#_Toc362454237}[]{#_Toc362455657}[]{#_Toc362454238}[]{#_Toc362455658}[]{#_Toc362454239}[]{#_Toc362455659}[]{#_Toc362454240}[]{#_Toc362455660}[]{#_Toc362454241}[]{#_Toc362455661}[]{#_Toc362454242}[]{#_Toc362455662}[]{#_Toc362454243}[]{#_Toc362455663}[]{#_Toc362454244}[]{#_Toc362455664}[]{#_Toc362454245}[]{#_Toc362455665}[]{#_Toc362454246}[]{#_Toc362455666}[]{#_Toc362454247}[]{#_Toc362455667}[]{#_Toc362454248}[]{#_Toc362455668}[]{#_Toc362454249}[]{#_Toc362455669}[]{#_Toc362454250}[]{#_Toc362455670}[]{#_Toc362454251}[]{#_Toc362455671}[]{#_Toc362454252}[]{#_Toc362455672}[]{#_Toc362454253}[]{#_Toc362455673}[]{#_Toc362454254}[]{#_Toc362455674}[]{#_Toc362454255}[]{#_Toc362455675}[]{#_Toc362454256}[]{#_Toc362455676}[]{#_Toc362454257}[]{#_Toc362455677}[]{#_Toc362454258}[]{#_Toc362455678}[]{#_Toc362454259}[]{#_Toc362455679}[]{#_Toc362454260}[]{#_Toc362455680}[]{#_Toc362454261}[]{#_Toc362455681}[]{#_Toc362454262}[]{#_Toc362455682}[]{#_Toc362454263}[]{#_Toc362455683}[]{#_Toc362454264}[]{#_Toc362455684}[]{#_Toc362454265}[]{#_Toc362455685}[]{#_Toc362454266}[]{#_Toc362455686}[]{#_Toc362454267}[]{#_Toc362455687}[]{#_Toc362454268}[]{#_Toc362455688}[]{#_Toc362454269}[]{#_Toc362455689}[]{#_Toc362454270}[]{#_Toc362455690}[]{#_Toc362454271}[]{#_Toc362455691}[]{#_Toc362454272}[]{#_Toc362455692}[]{#_Toc362454273}[]{#_Toc362455693}[]{#_Toc362454274}[]{#_Toc362455694}[]{#_Toc362454275}[]{#_Toc362455695}[]{#_Toc362454276}[]{#_Toc362455696}[]{#_Toc362454277}[]{#_Toc362455697}[]{#_Toc362454278}[]{#_Toc362455698}[]{#_Toc362454279}[]{#_Toc362455699}[]{#_Toc362454280}[]{#_Toc362455700}[]{#_Toc362454281}[]{#_Toc362455701}[]{#_Toc362454282}[]{#_Toc362455702}[]{#_Toc362454283}[]{#_Toc362455703}[]{#_Toc362454284}[]{#_Toc362455704}[]{#_Toc362454285}[]{#_Toc362455705}[]{#_Toc362454286}[]{#_Toc362455706}[]{#_Toc362454287}[]{#_Toc362455707}[]{#_Toc362454332}[]{#_Toc362455752}

**IPv6基础 \-- Fib6 Probe命令 \-- display system internal ipv6 fib prefix entry-status**

------------------------------------------------------------------------

[**[display system internal ipv6 fib prefix entry-status]{lang="EN-US"}**]{#struct_0_x2623_x1107_1619212062}[命令用来显示下驱动失败或者待老化的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1350769714}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x1335077650}

[**[display system internal ipv6 fib prefix]{lang="EN-US"}**[ **entry-status**]{lang="EN-US"}]{#struct_0_x2623_x1107_x1832663914}[[ status ]{lang="EN-US"}]{.commandparameterChar}[\[ **vpn-instance** ]{lang="EN-US"}[[vpn-instance-name ]{lang="EN-US"}]{.commandparameterChar}[\]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_422468122}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 fib prefix]{lang="EN-US"}**[ **entry-status**]{lang="EN-US"}]{#struct_0_x2623_x1107_1891144768}[[ status]{lang="EN-US"}]{.commandparameterChar}[ \[ **vpn-instance** ]{lang="EN-US"}[[vpn-instance-name]{lang="EN-US"}]{.commandparameterChar}[ \] **slot** ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x105239812}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 fib prefix entry-status ]{lang="EN-US"}**]{#struct_0_x2623_x1107_369288410}[[status ]{lang="EN-US"}]{.commandparameterChar}[\[ **vpn-instance** ]{lang="EN-US"}[[vpn-instance-name]{lang="EN-US"}]{.commandparameterChar}[ \] **chassis** ]{lang="EN-US"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}**[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x793829074}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_637340980}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_288161163}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_1345118157}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x2132285292}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1721302316}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x2623_x1107_x1475404489}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则显示公网的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[entry-status]{lang="EN-US"}***[ status]{lang="EN-US"}*]{#struct_0_x2623_x1107_369222874}[：用于匹配]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项；取值范围为]{style="font-family:宋体"}[\<A,F\>]{lang="EN-US"}[，"]{style="font-family:宋体"}[A]{lang="EN-US"}["表示需要被老化的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项，"]{style="font-family:宋体"}[F]{lang="EN-US"}["表示下刷驱动失败的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_458599180}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定单板的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x284961344}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定成员设备的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1428215621}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1507739162}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定成员设备上指定单板的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x39034921}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定单板的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x291197657}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的下驱动失败或者待老化的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::

::: {#-1278649611 .myid}
[]{#_Toc404799072}[]{#struct_0_x2623_x1107_x987415261}[]{#_Toc350241015}[]{#_Toc343257218}[]{#_Toc340564366}[]{#_Toc362454334}[]{#_Toc362455754}[]{#_Toc362454335}[]{#_Toc362455755}[]{#_Toc362454336}[]{#_Toc362455756}[]{#_Toc362454337}[]{#_Toc362455757}[]{#_Toc362454338}[]{#_Toc362455758}[]{#_Toc362454339}[]{#_Toc362455759}[]{#_Toc362454340}[]{#_Toc362455760}[]{#_Toc362454341}[]{#_Toc362455761}[]{#_Toc362454342}[]{#_Toc362455762}[]{#_Toc362454343}[]{#_Toc362455763}[]{#_Toc362454344}[]{#_Toc362455764}[]{#_Toc362454345}[]{#_Toc362455765}[]{#_Toc362454346}[]{#_Toc362455766}[]{#_Toc362454347}[]{#_Toc362455767}[]{#_Toc362454348}[]{#_Toc362455768}[]{#_Toc362454349}[]{#_Toc362455769}[]{#_Toc362454350}[]{#_Toc362455770}[]{#_Toc362454351}[]{#_Toc362455771}[]{#_Toc362454352}[]{#_Toc362455772}[]{#_Toc362454353}[]{#_Toc362455773}[]{#_Toc362454354}[]{#_Toc362455774}[]{#_Toc362454355}[]{#_Toc362455775}[]{#_Toc362454356}[]{#_Toc362455776}[]{#_Toc362454357}[]{#_Toc362455777}[]{#_Toc362454358}[]{#_Toc362455778}[]{#_Toc362454359}[]{#_Toc362455779}[]{#_Toc362454360}[]{#_Toc362455780}[]{#_Toc362454361}[]{#_Toc362455781}[]{#_Toc362454362}[]{#_Toc362455782}[]{#_Toc362454363}[]{#_Toc362455783}[]{#_Toc362454364}[]{#_Toc362455784}[]{#_Toc362454365}[]{#_Toc362455785}[]{#_Toc362454366}[]{#_Toc362455786}[]{#_Toc362454367}[]{#_Toc362455787}[]{#_Toc362454368}[]{#_Toc362455788}[]{#_Toc362454369}[]{#_Toc362455789}[]{#_Toc362454370}[]{#_Toc362455790}[]{#_Toc362454371}[]{#_Toc362455791}[]{#_Toc362454441}[]{#_Toc362455861}

**IPv6基础 \-- Fib6 Probe命令 \-- display system internal ipv6 fib prefix ipv6**

------------------------------------------------------------------------

[**[display system internal ipv6 fib prefix]{lang="EN-US"}***[ ipv6]{lang="EN-US"}*]{#struct_0_x2623_x1107_x34042889}[命令用来显示]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1651750445}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2623_x1107_x1802300141}

[**[display system internal ipv6 fib prefix]{lang="EN-US"}**[ \[ **vpn-instance** ]{lang="EN-US"}]{#struct_0_x2623_x1107_x446912515}[[vpn-instance-name ]{lang="EN-US"}]{.commandparameterChar}[\] ]{lang="EN-US"}[[ipv6 ]{lang="EN-US"}]{.commandparameterChar}[\[ *prefix-length* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2623_x1107_1346578558}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ipv6 fib prefix]{lang="EN-US"}**[ \[ **vpn-instance** ]{lang="EN-US"}]{#struct_0_x2623_x1107_x1497241592}[[vpn-instance-name]{lang="EN-US"}]{.commandparameterChar}[ \] ]{lang="EN-US"}[[ipv6 ]{lang="EN-US"}]{.commandparameterChar}[\[ *prefix-length* \] **slot** ]{lang="EN-US"}[[slot-number ]{lang="EN-US"}]{.commandparameterChar}[[\[ **cpu** ]{lang="EN-US" style="font-style:normal"}[cpu-number ]{lang="EN-US"}]{.commandparameterChar}[[\]]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2623_x1107_x864647831}[模式：]{style="font-family:宋体"}

[**[display system internal ipv6 fib prefix ]{lang="EN-US"}**[\[ **vpn-instance**]{lang="EN-US"}**[ ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}**[ ]{lang="EN-US"}**]{#struct_0_x2623_x1107_24924608}[[ipv6]{lang="EN-US"}]{.commandparameterChar}**[ ]{lang="EN-US"}**[\[ ]{lang="EN-US"}*[prefix-length]{lang="EN-US"}*[ \]]{lang="EN-US"}[ **chassis** ]{lang="EN-US"}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}**[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[ \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1640188051}

[[Probe]{lang="EN-US"}]{#struct_0_x2623_x1107_x1205737327}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_1573931435}

[[network-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_x1802234605}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2623_x1107_518230023}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2623_x1107_x1849006444}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x2623_x1107_184240944}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，则显示公网的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}

[*[ipv6]{lang="EN-US"}*]{#struct_0_x2623_x1107_1976720577}[：]{style="font-family:宋体"}[显示目的地址为指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀详细]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x2623_x1107_x186829651}[：指定]{style="font-family:宋体"}[[IPv6]{lang="EN-US"}]{.commandparameterChar}[[地址的前缀]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[长度，取值范围为]{style="font-family:宋体"}[0\~128]{lang="EN-US"}[。]{style="font-family:宋体"}[ ]{.commandkeywordsChar}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_1831408940}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定单板的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1756120725}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定成员设备的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1784511517}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 FIB]{lang="EN-US"}[前缀详细信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_x1802169069}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体"}[[显示指定成员设备上指定单板的]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[IPv6 FIB]{lang="EN-US"}[前缀详细信息]{style="font-family:宋体"}[[，]{style="font-family:宋体;font-style:normal"}[chassis-number]{lang="EN-US"}]{.commandparameterChar}[[表示设备在]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[[IRF]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}[[中的成员编号，]{style="font-family:宋体;font-style:normal"}[slot-number]{lang="EN-US"}]{.commandparameterChar}[[表示单板所在的槽位号。]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x2623_x1107_2092918451}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体"}[[显示指定单板的]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[IPv6 FIB]{lang="EN-US"}[前缀详细信息]{style="font-family:宋体"}[[。]{style="font-family:宋体;font-style:normal"}[chassis-number]{lang="EN-US"}]{.commandparameterChar}[[表示设备在]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[[IRF]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}[[中的成员编号或者]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[[PEX]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}[[对应的虚拟框号，]{style="font-family:宋体;font-style:normal"}[slot-number]{lang="EN-US"}]{.commandparameterChar}[[表示单板或]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[[PEX]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}[[所在的槽位号。]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}**]{#struct_0_x2623_x1107_x1454723811}*[cpu-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[[显示指定]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[[CPU]{lang="EN-US" style="font-style:normal"}]{.commandparameterChar}[[的]{style="font-family:宋体;font-style:normal"}]{.commandparameterChar}[IPv6 FIB]{lang="EN-US"}[前缀详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::
