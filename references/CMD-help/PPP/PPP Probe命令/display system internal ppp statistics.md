::: {#-1041121701 .myid}
[]{#_Toc404800107}[]{#struct_0_x1267_13474_x1849006002}[]{#_Toc371150019}

**PPP \-- PPP Probe命令 \-- display system internal ppp statistics**

------------------------------------------------------------------------

[**[display system internal ppp statistics]{lang="EN-US"}**]{#struct_0_x1267_13474_x622590250}[命令用来显示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x623115973}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1267_13474_623944448}

[**[display system internal ppp statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| ]{lang="EN-US"}]{#struct_0_x1267_13474_x1933737881}**[interface-event]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \] }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1267_13474_1709732401}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ppp statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| ]{lang="EN-US"}]{#struct_0_x1267_13474_x936232366}**[interface-event]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \] } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1267_13474_1160497953}[模式：]{style="font-family:宋体"}

[**[display system internal ppp statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| ]{lang="EN-US"}]{#struct_0_x1267_13474_1105822592}**[interface-event]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \] } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1267_13474_2126985651}

[[Probe]{lang="EN-US"}]{#struct_0_x1267_13474_1298843712}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1267_13474_1862859219}

[[network-admin]{lang="EN-US"}]{#struct_0_x1267_13474_2124096134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1267_13474_650460716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1267_13474_1427071757}

[**[aggregation]{lang="EN-US"}**]{#struct_0_x1267_13474_x280188802}[：显示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的]{style="font-family:宋体"}[聚合处理统计信息。]{style="font-family:宋体;color:black"}

[**[all]{lang="EN-US"}**]{#struct_0_x1267_13474_x36724849}[：显示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[统计信息。]{style="font-family:宋体;color:black"}

[**[interface-event]{lang="EN-US"}**]{#struct_0_x1267_13474_x1933737882}[：显示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的]{style="font-family:宋体"}[接口处理统计信息。]{style="font-family:宋体;color:black"}

[**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_x1267_13474_x1019150954}[：显示]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的多机备份实例统计信息。]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[表示多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定多机备份实例时，将显示所有多机备份实例的统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_x110051308}[：显示指定单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_x238330594}[：显示指定成员设备的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定本参数时，将显示所有成员设备的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_361757479}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定本参数时，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_x984096197}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有成员设备上所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_769576810}[：显示指定单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定本参数时，将显示所有单板上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1267_13474_2056138035}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1267_13474_1347403012}

[[在主用设备和备用设备上都可以查询]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x1267_13474_1690947254}[的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}
:::

::: {#-629601170 .myid}
[]{#_Toc404800108}[]{#struct_0_x1267_13474_945015843}[]{#_Toc371150022}[]{#_Toc370829937}

**PPP \-- PPP Probe命令 \-- display system internal pppoe-server statistics**

------------------------------------------------------------------------

[**[display system internal pppoe-server statistics]{lang="EN-US"}**]{#struct_0_x1267_13474_x492378159}[命令用来显示]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1267_13474_984318193}

[[集中式设备[:]{lang="EN-US"}]{style="font-family:宋体;color:black"}]{#struct_0_x1267_13474_x681519527}

[**[display system internal pppoe-server statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| **vsrp** \[ **vsrp-instance** *vsrp-instance-name* \] }]{lang="EN-US"}]{#struct_0_x1267_13474_1631523983}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1267_13474_x303003366}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal pppoe-server statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| **vsrp** \[ **vsrp-instance** *vsrp-instance-name* \] } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1267_13474_x1933737879}

[[分布式设备---]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}]{#struct_0_x1267_13474_1352519001}[模式[:]{lang="EN-US"}]{style="font-family:宋体;
color:black"}

[**[display system internal pppoe-server statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| **vsrp** \[ **vsrp-instance** *vsrp-instance-name* \] } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1267_13474_2025018539}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x728445894}

[[Probe]{lang="EN-US"}]{#struct_0_x1267_13474_1859888015}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x1046492960}

[[network-admin]{lang="EN-US"}]{#struct_0_x1267_13474_1950748015}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1267_13474_829016457}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x1527823162}

[**[aggregation]{lang="EN-US"}**]{#struct_0_x1267_13474_x480403970}[：显示]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[的]{style="font-family:宋体"}[聚合处理统计信息。]{style="font-family:宋体;color:black"}

[**[all]{lang="EN-US"}**]{#struct_0_x1267_13474_x196292524}[：显示]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[的]{style="font-family:宋体"}[所有统计信息。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_x1267_13474_1528446027}[：显示]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例时，显示所有]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例的统计信息。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_x1075557849}[：显示指定单板的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有单板的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_x1123334069}[：显示指定成员设备的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定本参数时，将显示所有成员设备的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_1524556893}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定本参数时，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_x1933737880}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将显示所有成员设备上所有单板的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_817711629}[：显示指定单板的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定本参数时，将显示所有单板上的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1267_13474_143648460}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x204979669}

[[在主用设备和备用设备上都可以查询]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}]{#struct_0_x1267_13474_x986969292}[的统计信息。]{style="font-family:宋体"}
:::

::: {#275839556 .myid}
[]{#_Toc404800109}[]{#struct_0_x1267_13474_1553601819}[]{#_Toc371150020}[]{#_Toc370829938}

**PPP \-- PPP Probe命令 \-- reset system internal ppp statistics**

------------------------------------------------------------------------

[**[reset system internal ppp statistics]{lang="EN-US"}**]{#struct_0_x1267_13474_787722292}[命令用来清除]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x1948318601}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1267_13474_x1510046974}

[**[reset system internal ppp statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| ]{lang="EN-US"}]{#struct_0_x1267_13474_1150931285}**[interface-event]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \] }]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1267_13474_1165995863}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal ppp statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| ]{lang="EN-US"}]{#struct_0_x1267_13474_x1076061778}**[interface-event]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \] } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1267_13474_x1608679793}[模式：]{style="font-family:宋体"}

[**[reset system internal ppp statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| ]{lang="EN-US"}]{#struct_0_x1267_13474_373957080}**[interface-event]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \] } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x760279811}

[[Probe]{lang="EN-US"}]{#struct_0_x1267_13474_x1204424603}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x1933737877}

[[network-admin]{lang="EN-US"}]{#struct_0_x1267_13474_x1423418521}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1267_13474_617176825}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1267_13474_504394142}

[**[aggregation]{lang="EN-US"}**]{#struct_0_x1267_13474_x871520668}[：清除]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的]{style="font-family:宋体"}[聚合处理统计信息。]{style="font-family:宋体;color:black"}

[**[all]{lang="EN-US"}**]{#struct_0_x1267_13474_804848226}[：清除]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的所有]{style="font-family:宋体"}[统计信息。]{style="font-family:宋体;color:black"}

[**[interface-event]{lang="EN-US"}**]{#struct_0_x1267_13474_x1274252353}[：清除]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的]{style="font-family:宋体"}[接口处理统计信息。]{style="font-family:宋体;color:black"}

[**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_x1267_13474_148153679}[：清除]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例时，将清除所有]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例的统计信息。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_943808526}[：清除指定单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将清除所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_429845410}[：清除指定成员设备的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定本参数时，将清除所有成员设备的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_408811646}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定本参数时，将清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_636098202}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将清除所有成员设备上所有单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1267_13474_x487634110}[：清除指定单板的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定本参数时，将清除所有单板上的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。（（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1267_13474_x602595294}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1267_13474_418461776}

[[在主用设备和备用设备上都可以清除]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x1267_13474_351977732}[的]{style="font-family:宋体"}[统计信息]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}
:::

::: {#-2675053 .myid}
[]{#_Toc404800110}[]{#struct_0_x1267_13474_x1933737878}[]{#_Toc371150023}[]{#_Toc370829939}

**PPP \-- PPP Probe命令 \-- reset system internal pppoe-server statistics**

------------------------------------------------------------------------

[**[reset system internal pppoe-server statistics]{lang="EN-US"}**]{#struct_0_x1267_13474_x213564940}[命令用来清除]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1267_13474_120825070}

[[集中式设备[:]{lang="EN-US"}]{style="font-family:宋体;color:black"}]{#struct_0_x1267_13474_1895244844}

[**[reset system internal pppoe-server statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| **vsrp** \[ **vsrp-instance** *vsrp-instance-name* \] }]{lang="EN-US"}]{#struct_0_x1267_13474_1622223711}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1267_13474_569086451}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset system internal pppoe-server statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| **vsrp** \[ **vsrp-instance** *vsrp-instance-name* \] } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1267_13474_x1796007763}

[[分布式设备---]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}]{#struct_0_x1267_13474_917909860}[模式[:]{lang="EN-US"}]{style="font-family:宋体;
color:black"}

[**[reset system internal pppoe-server statistics]{lang="EN-US"}**[ { **aggregation** \| **all** \| **vsrp** \[ **vsrp-instance** *vsrp-instance-name* \] } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1267_13474_1126018487}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1267_13474_880662704}

[[Probe]{lang="EN-US"}]{#struct_0_x1267_13474_348887814}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1267_13474_815515820}

[[network-admin]{lang="EN-US"}]{#struct_0_x1267_13474_2028266385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1267_13474_1353858543}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1267_13474_x322516763}

[**[aggregation]{lang="EN-US"}**]{#struct_0_x1267_13474_x744259485}[：清除]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[的]{style="font-family:宋体"}[聚合处理统计信息。]{style="font-family:宋体;color:black"}

[**[all]{lang="EN-US"}**]{#struct_0_x1267_13474_x1670960618}[：清除]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[的]{style="font-family:宋体"}[所有统计信息。]{style="font-family:宋体;color:black"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vsrp]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_x1267_13474_475712836}[：清除]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例统计信息。]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例时，将清除所有]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例的统计信息。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_x1229015934}[：清除指定单板的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定本参数时，将清除所有单板的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_279949022}[：清除指定成员设备的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定本参数时，将清除所有成员设备的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_765107542}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定本参数时，将清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1267_13474_959532205}[：清除指定单板的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定本参数时，将清除所有单板上的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体;color:black"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1267_13474_x1319531100}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1267_13474_1903289605}

[[在主用设备和备用设备上都可以清除]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}]{#struct_0_x1267_13474_x17875553}[的统计信息。]{style="font-family:宋体"}
:::
