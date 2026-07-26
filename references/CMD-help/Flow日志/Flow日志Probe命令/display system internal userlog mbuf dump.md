::::: {#738319870 .myid}
[]{#_Toc384286844}[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc404798890}[]{#struct_0_x1974_x3813_x1618090962}

**Flow日志 \-- Flow日志Probe命令 \-- display system internal userlog mbuf dump**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:5.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Flow日志Probe命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1974_x3813_x1752980647}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 5.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1974_x3813_x1941132902}
:::

[ ]{lang="EN-US"}

[**[display system internal userlog mbuf dump]{lang="EN-US"}**]{#struct_0_x1974_x3813_x469303963}[命令用来显示指定个数的]{style="font-family:宋体"}[USERLOG UDP]{lang="EN-US"}[报文内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_x705265990}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_x1974_x3813_1303328703}

[**[display system internal userlog mbuf dump count ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1974_x3813_x1450653467}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1974_x3813_x1591407036}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal userlog mbuf dump count ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1974_x3813_x1093030579}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1974_x3813_505075311}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal userlog mbuf dump count ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1974_x3813_x1368803612}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_x1108470729}

[[Probe]{lang="EN-US"}]{#struct_0_x1974_x3813_x1914526177}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_273260868}

[[network-admin]{lang="EN-US"}]{#struct_0_x1974_x3813_76721579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1974_x3813_1333029772}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_1137001821}

[**[count]{lang="EN-US" style="color:black"}**[ *number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_654286978}[：指定显示]{style="font-family:宋体;
color:black"}[报文[的个数。]{style="color:
black"}]{style="font-family:宋体"}*[number]{lang="EN-US" style="color:black"}*[为需要显示内容的日志个数，取值范围为]{style="font-family:宋体;color:black"}[1-100]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x581287741}[：指定显示]{style="font-family:
宋体;color:black"}[报文[所在的单板。]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[为单板所在的槽位号。如未指定该参数，]{style="font-family:宋体;color:black"}[则默认在当前主控板上显示报文内容。[（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x850288108}[：指定显示]{style="font-family:
宋体;color:black"}[报文[的成员设备。]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[为设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如未指定该参数，]{style="font-family:宋体;color:black"}[则默认在当前主控板上显示报文内容。[（集中式]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）（不支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x131132943}[：指定显示报文的成员设备]{style="font-family:
宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[为设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号[。如未指定该参数，则默认在当前主控板上显示报文内容。（集中式]{style="color:
black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x894003521}[：指定显示]{style="font-family:宋体;color:black"}[报文[的成员设备和单板。]{style="color:black"}]{style="font-family:宋体"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如未指定该参数，]{style="font-family:宋体;
color:black"}[则默认在当前主控板上显示报文内容。[（分布式设备－]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[模式）（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x1657025726}[：指定显示报文的单板。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号[，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如未指定该参数，则默认在当前主控板上显示报文内容。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）（支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_x1974_x3813_x739653774}[：指定显示]{style="font-family:宋体;color:black"}[报文[设备的]{style="color:black"}]{style="font-family:宋体"}[CPU]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="color:black"}]{style="font-family:宋体"}
:::::

::::: {#1676441289 .myid}
[]{#_Toc404798891}[]{#struct_0_x1974_x3813_2018334578}

**Flow日志 \-- Flow日志Probe命令 \-- display system internal userlog statistic**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:5.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Flow日志Probe命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1974_x3813_1757661802}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 5.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1974_x3813_x75714509}
:::

[ ]{lang="EN-US"}

[**[display system internal userlog statistic]{lang="EN-US"}**]{#struct_0_x1974_x3813_371895029}[命令用来显示]{style="font-family:宋体"}[USERLOG]{lang="EN-US"}[模块的运行统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_1125645202}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_x1974_x3813_1058854349}

[**[display system internal userlog statistic]{lang="EN-US"}**]{#struct_0_x1974_x3813_1214861729}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1974_x3813_1139576708}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal userlog statistic]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1974_x3813_x1442108606}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1974_x3813_x1082755335}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal userlog statistic ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1974_x3813_1915630492}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_x1160313622}

[[Probe]{lang="EN-US"}]{#struct_0_x1974_x3813_298799218}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_x1914526176}

[[network-admin]{lang="EN-US"}]{#struct_0_x1974_x3813_1839344809}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1974_x3813_x1941290286}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_120049032}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_1249846120}[：指定查看统计信息的单板。]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[为单板所在的槽位号。如未指定该参数，]{style="font-family:宋体;color:black"}[则默认在显示当前主控板的统计信息。[（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x608139474}[：指定查看统计信息的成员设备。]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[为设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如未指定该参数，]{style="font-family:宋体;color:black"}[则默认在显示当前主控板的统计信息。[（集中式]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）（不支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x534417470}[：指定查看统计信息的成员设备]{style="font-family:
宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[为设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号[。如未指定该参数，则默认在显示当前主控板的统计信息。（集中式]{style="color:
black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x1544222130}[：指定查看统计信息的成员设备和单板。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如未指定该参数，]{style="font-family:宋体;
color:black"}[则默认在显示当前主控板的统计信息。[（分布式设备－]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[模式）（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_1678083272}[：指定查看统计信息的单板。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号[，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如未指定该参数，则默认在显示当前主控板的统计信息。（分布式设备－]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）（支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x705252189}[：指定查看统计信息的成员设备所在的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:
宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="color:black"}。]{style="font-family:宋体"}
:::::

::::: {#1802390444 .myid}
[]{#_Toc404798892}[]{#struct_0_x1974_x3813_916129665}[]{#_Toc384286846}

**Flow日志 \-- Flow日志Probe命令 \-- display system internal userlog test**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:5.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Flow日志Probe命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1974_x3813_x2029703877}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 5.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1974_x3813_x71417553}
:::

[ ]{lang="EN-US"}

[**[display system internal userlog mbuf test]{lang="EN-US"}**]{#struct_0_x1974_x3813_x957141013}[命令用来发送指定个数的]{style="font-family:宋体"}[FLOW]{lang="EN-US"}[测试日志，并显示日志发送结果信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_x668631700}

[[集中式设备]{style="font-family:宋体"}]{#struct_0_x1974_x3813_x791374304}

[**[display system internal userlog test count ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1974_x3813_x484444081}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1974_x3813_298063710}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal userlog test count ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1974_x3813_x59848444}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1974_x3813_1464400020}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display system internal userlog test count ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1974_x3813_x1142336694}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_1227261889}

[[Probe]{lang="EN-US"}]{#struct_0_x1974_x3813_576235701}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_145716006}

[[network-admin]{lang="EN-US"}]{#struct_0_x1974_x3813_1496917236}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1974_x3813_x1649751008}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1974_x3813_x1136972999}

[**[count]{lang="EN-US" style="color:black"}**[ *number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_629933679}[：指定发送测试日志个数。]{style="font-family:宋体;
color:black"}*[number]{lang="EN-US" style="color:black"}*[为发送测试日志的个数，取值范围为]{style="font-family:宋体;color:black"}[1-3000]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x1914526175}[：指定发送测试日志的单板。]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[为单板所在的槽位号。如未指定该参数，]{style="font-family:宋体;color:black"}[则默认在当前主控板上发送测试日志。[（分布式设备－独立运行模式）]{style="color:black"}]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x889538546}[：指定发送测试日志的成员设备。]{style="font-family:
宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[为设备在]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。如未指定该参数，]{style="font-family:宋体;color:black"}[则默认在当前主控板上发送测试日志。[（集中式]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）（不支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}**[ *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_628381944}[：指定发送测试日志的成员设备]{style="font-family:
宋体;color:black"}[/PEX]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[为设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号[。如未指定该参数，则默认在当前主控板上发送测试日志。（集中式]{style="color:
black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[设备）（支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;
color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_1232248823}[：指定发送测试日志的成员设备和单板。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。如未指定该参数，]{style="font-family:宋体;
color:black"}[则默认在当前主控板上发送测试日志。[（分布式设备－]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[模式）（不支持]{style="font-family:宋体;color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x1974_x3813_x1650162717}[：指定发送测试日志的单板。]{style="font-family:宋体;color:black"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号]{style="font-family:宋体;color:black"}[或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号[，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板]{style="font-family:宋体;color:black"}[或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所[在的槽位号。如未指定该参数，则默认在当前主控板上发送测试日志。（分布式设备－]{style="color:black"}]{style="font-family:宋体"}[IRF]{lang="EN-US" style="color:black"}[模式）（支持]{style="font-family:宋体;
color:black"}[IRF3]{lang="EN-US" style="color:black"}[的设备）]{style="font-family:宋体;color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_x1974_x3813_x580470221}[：指定发送测试日志的]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[编号。]{style="font-family:宋体;color:black"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况]{style="color:black"}为准。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::::
