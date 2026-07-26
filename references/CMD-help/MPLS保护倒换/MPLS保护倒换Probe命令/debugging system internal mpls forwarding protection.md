::: {#-984665339 .myid}
[]{#_Toc404799890}[]{#struct_0_x9021_83908_x458161234}[]{#_Toc351046991}

**MPLS保护倒换 \-- MPLS保护倒换Probe命令 \-- debugging system internal mpls forwarding protection**

------------------------------------------------------------------------

[**[debugging system internal mpls forwarding protection]{lang="EN-US"}**]{#struct_0_x9021_83908_x1796833942}[命令用来打开]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发平面]{style="font-family:宋体"}[保护倒换的调试信息开关。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[debugging system internal mpls forwarding protection]{lang="EN-US"}**]{#struct_0_x9021_83908_344976266}[命令用来关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发平面]{style="font-family:宋体"}[保护倒换的调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9021_83908_x754101693}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9021_83908_2040036705}

[**[debugging system internal mpls forwarding protection]{lang="EN-US"}**[ { **all** \| **error** \| **process** }]{lang="EN-US"}]{#struct_0_x9021_83908_882080691}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[debugging system internal mpls forwarding protection]{lang="EN-US"}**[ { **all** \| **error** \| **process** }]{lang="EN-US"}]{#struct_0_x9021_83908_x682662596}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9021_83908_x2022351874}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging system internal mpls forwarding protection]{lang="EN-US"}**[ { **all** \| **error** \| **process** } **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x9021_83908_x24133892}

[**[undo debugging system internal mpls forwarding protection ]{lang="EN-US"}**[{ **all** \| **error** \| **process** } **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x9021_83908_317699527}

[[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9021_83908_x104692569}[模式：]{style="font-family:宋体"}

[**[debugging system internal mpls forwarding protection]{lang="EN-US"}**[ { **all** \| **error** \| **process** } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x9021_83908_1697646704}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[debugging system internal mpls forwarding protection]{lang="EN-US"}**[ { **all** \| **error** \| **process** } **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x9021_83908_x2137046624}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9021_83908_1609669031}

[[MPLS]{lang="EN-US"}]{#struct_0_x9021_83908_14826777}[转发]{style="font-family:宋体"}[平面保护倒换的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9021_83908_x876296828}

[[Probe]{lang="EN-US"}]{#struct_0_x9021_83908_x1102463619}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9021_83908_1915717183}

[[network-admin]{lang="EN-US"}]{#struct_0_x9021_83908_x1538885289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9021_83908_112908427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9021_83908_x815832711}

[**[all]{lang="EN-US"}**]{#struct_0_x9021_83908_221178346}[：表示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发平面]{style="font-family:宋体"}[保护倒换的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x9021_83908_1017944762}[：表示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发平面]{style="font-family:宋体"}[保护倒换的错误调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_x9021_83908_1177015916}[：表示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[转发平面]{style="font-family:宋体"}[保护倒换的处理过程调试信息开关。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x9021_83908_70554327}[：表示指定单板上的调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。（分布式设备―独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x9021_83908_x1243534508}*[ slot-number]{lang="PT-BR"}*[：表示]{style="font-family:宋体"}[指定成员设备上的调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x9021_83908_1346369662}*[ slot-number]{lang="PT-BR"}*[：表示]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的调试信息开关。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x9021_83908_x104889177}*[chassis-number]{lang="PT-BR"}*[ **slot** *slot-number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示指定成员设备指定单板上的调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x9021_83908_x717922966}*[chassis-number]{lang="PT-BR"}*[ **slot** *slot-number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示指定单板上的调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu]{lang="PT-BR"}**]{#struct_0_x9021_83908_x276058874}[ *cpu-number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示指定]{style="font-family:宋体"}[CPU]{lang="PT-BR"}[的调试信息开关。]{style="font-family:宋体"}*[cpu-number]{lang="PT-BR"}*[表示]{style="font-family:宋体"}[CPU]{lang="PT-BR"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::

::: {#1438647033 .myid}
[]{#_Toc404799891}[]{#struct_0_x9021_83908_892013398}

**MPLS保护倒换 \-- MPLS保护倒换Probe命令 \-- display system internal mpls protection statistics**

------------------------------------------------------------------------

[**[display ]{lang="EN-US"}[s]{lang="EN-US"}[ystem internal mpls protection statistics]{lang="EN-US"}**]{#struct_0_x9021_83908_x130765983}[命令用来显示]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[保护倒换的统计信息，包括]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换收到的信息、]{style="font-family:宋体"}[PSC]{lang="EN-US"}[控制报文信息、错误处理信息等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9021_83908_312056759}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9021_83908_2095036193}

[**[display ]{lang="EN-US"}[system internal mpls protection statistics]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9021_83908_x844941989}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9021_83908_x843020714}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[system internal mpls protection statistics]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9021_83908_x1523249047}**[slot ]{lang="IT"}***[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9021_83908_x760259258}[模式：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[system internal mpls protection statistics]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9021_83908_x53546911}**[chassis ]{lang="IT"}***[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot ]{lang="IT"}***[slot-number]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9021_83908_893981392}

[[Probe]{lang="EN-US"}]{#struct_0_x9021_83908_572892229}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9021_83908_708643585}

[[network-admin]{lang="EN-US"}]{#struct_0_x9021_83908_2036966410}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9021_83908_868425242}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9021_83908_1725671428}

[**[slot]{lang="PT-BR"}**]{#struct_0_x9021_83908_x965367754}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换统计信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x9021_83908_x104823641}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定成员设备上的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换统计信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_x9021_83908_x1026217797}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换统计信息。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x9021_83908_1733131591}*[chassis-number]{lang="PT-BR"}*[ **slot** *slot-number*]{lang="PT-BR"}[：显示指定成员设备指定单板上的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_x9021_83908_1702665558}*[chassis-number]{lang="PT-BR"}*[ **slot** *slot-number*]{lang="PT-BR"}[：显示指定单板上的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[cpu ]{lang="PT-BR"}**]{#struct_0_x9021_83908_2062593278}*[cpu-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="PT-BR"}[上的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[保护倒换统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="PT-BR"}*[表示]{style="font-family:宋体"}[CPU]{lang="PT-BR"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
