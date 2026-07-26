::: {#745620628 .myid}
[]{#_Toc95362256}[]{#_Toc37217646}[]{#_Toc30751576}[]{#_Toc15982605}[]{#_Toc6373264}[]{#_Toc298249418}[]{#_Ref135293160}[]{#_Toc95362249}[]{#_Toc306705052}[]{#_Toc295825272}[]{#struct_0_41576_x1443_1579561687}[]{#_Toc404800573}[]{#_Toc343699024}

**快速转发 \-- 快速转发Probe配置命令 \-- display system internal ip fast-forwarding cache verbose**

------------------------------------------------------------------------

[**[display system internal ip fast-forwarding cache verbose]{lang="EN-US"}**]{#struct_0_41576_x1443_x1496596528}[命令用来显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[快转表项的详细内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_41576_x1443_1624524677}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_41576_x1443_1635147981}

[**[display system internal ip fast-forwarding cache ]{lang="EN-US"}**[\[ *ip-address* \] **verbose**]{lang="EN-US"}]{#struct_0_41576_x1443_1937731647}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_41576_x1443_x1520263133}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal ip fast-forwarding cache ]{lang="EN-US"}**[\[ *ip-address* \] **verbose** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_41576_x1443_x1460145756}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_41576_x1443_x1964616667}[模式：]{style="font-family:宋体"}

[**[display system internal ip fast-forwarding cache]{lang="EN-US"}**[ \[ *ip-address* \] **verbose** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_41576_x1443_1558652085}

[[【视图】]{style="font-family:黑体"}]{#struct_0_41576_x1443_x60277856}

[[probe]{lang="EN-US"}]{#struct_0_41576_x1443_1236309598}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_41576_x1443_1866941812}

[[network-admin]{lang="EN-US"}]{#struct_0_41576_x1443_1099220801}

[[mdc-admin]{lang="EN-US"}]{#struct_0_41576_x1443_1938059327}

[[【参数】]{style="font-family:黑体"}]{#struct_0_41576_x1443_1742226778}

[*[ip-address]{lang="EN-US"}*]{#struct_0_41576_x1443_1278773368}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ IPv4 ]{lang="EN-US"}[快转表详细信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_41576_x1443_1553574215}[ *slot-number*]{lang="EN-US"}[：]{style="font-family:宋体"} [显示]{style="font-family:宋体"}[指定单板]{style="font-family:宋体"}[的快转表详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[快转表详细信息]{style="font-family:宋体"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_41576_x1443_x1950723584}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备的快转表详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的快转表详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_41576_x1443_x1204064318}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快转表详细信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的快转表详细信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_41576_x1443_x792545498}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的快转表详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的快转表详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_41576_x1443_1524819037}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定单板的快转表详细信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的快转表详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_41576_x1443_x2003874739}[ *cpu-number*]{lang="EN-US"}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的快转表详细信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1458047048 .myid}
[]{#struct_0_41576_x1443_1937797181}[]{#_Toc404800574}[]{#_Toc343699025}

**快速转发 \-- 快速转发Probe配置命令 \-- display system internal ip fast-forwarding service-sequece**

------------------------------------------------------------------------

[**[display system internal ip fast-forwarding service-sequece]{lang="EN-US"}**]{#struct_0_41576_x1443_433108705}[命令用来显示业务模块向快转模块的注册信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_41576_x1443_1290510916}

[**[display system internal ip fast-forwarding service-sequece]{lang="EN-US"}**]{#struct_0_41576_x1443_x317564917}

[[【视图】]{style="font-family:黑体"}]{#struct_0_41576_x1443_x780819221}

[[probe]{lang="EN-US"}]{#struct_0_41576_x1443_x940305102}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_41576_x1443_1917367068}

[[network-admin]{lang="EN-US"}]{#struct_0_41576_x1443_1061648865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_41576_x1443_1791995564}
:::

::: {#800535948 .myid}
[]{#struct_0_41576_x1443_1937731645}[]{#_Toc404800575}[]{#_Toc343699026}

**快速转发 \-- 快速转发Probe配置命令 \-- display system internal max-ecmp-num**

------------------------------------------------------------------------

[**[display system internal max-ecmp-num]{lang="EN-US"}**]{#struct_0_41576_x1443_x1520132061}[命令用来显示分布式各板]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的最大等价路由条数配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_41576_x1443_x1235984918}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_41576_x1443_1491617843}

[**[display system internal max-ecmp-num]{lang="EN-US"}**]{#struct_0_41576_x1443_714001666}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_41576_x1443_x1665634640}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal max-ecmp-num]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] ]{lang="EN-US"}]{#struct_0_41576_x1443_x1500283420}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_41576_x1443_1530314154}[模式：]{style="font-family:宋体"}

[**[display system internal max-ecmp-num]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] ** **]{lang="EN-US"}]{#struct_0_41576_x1443_x12631340}

[[【视图】]{style="font-family:黑体"}]{#struct_0_41576_x1443_1938059325}

[[probe]{lang="EN-US"}]{#struct_0_41576_x1443_1742095706}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_41576_x1443_890365444}

[[network-admin]{lang="EN-US"}]{#struct_0_41576_x1443_x420343903}

[[mdc-admin]{lang="EN-US"}]{#struct_0_41576_x1443_x698786104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_41576_x1443_x826404995}

[**[slot]{lang="EN-US"}**]{#struct_0_41576_x1443_x1045090573}[ *slot-number*]{lang="EN-US"}[：]{style="font-family:宋体"} [显示]{style="font-family:宋体"}[指定单板]{style="font-family:宋体"}[的最大等价路由条数配置信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[最大等价路由条数配置信息]{style="font-family:宋体"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_41576_x1443_x1036674959}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备的最大等价路由条数配置信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的最大等价路由条数配置信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_41576_x1443_409073790}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的最大等价路由条数配置信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的最大等价路由条数配置信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_41576_x1443_x67261104}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的最大等价路由条数配置信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的最大等价路由条数配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_41576_x1443_x1744324438}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定单板的最大等价路由条数配置信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的最大等价路由条数配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_41576_x1443_79995407}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的最大等价路由条数配置信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[]{#_Toc233801336}[]{#_Toc234730244}[]{#_Toc234742408}[]{#_Toc234742411}[]{#_Toc234742412}[]{#_Toc233801338}[]{#_Toc234730247}[]{#_Toc234742413}[]{#_Toc233801340}[]{#_Toc234730249}[]{#_Toc234742415}[]{#_Toc233801341}[]{#_Toc234730250}[]{#_Toc234742416}[]{#_Toc233801342}[]{#_Toc234730251}[]{#_Toc234742417}[]{#_Toc233801344}[]{#_Toc234730253}[]{#_Toc234742419}[ ]{lang="EN-US"}
:::
