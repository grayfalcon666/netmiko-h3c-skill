::: {#-1916349637 .myid}
[]{#_Toc293559741}[]{#_Toc339972636}[]{#_Toc343245648}[]{#_Toc404798794}[]{#struct_0_17117_13792_x1976183374}[]{#_Toc344209273}[]{#_Toc343245651}

**CFD \-- CFD Probe命令 \-- debugging system internal cfd**

------------------------------------------------------------------------

[**[debugging]{lang="EN-US"}**[ **system** **internal** **cfd**]{lang="EN-US"}]{#struct_0_17117_13792_840927340}[命令用来打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **cfd**]{lang="EN-US"}]{#struct_0_17117_13792_x2135701222}[命令用来关闭]{style="font-family:宋体"}[CFD]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17117_13792_x918766121}

[**[debugging]{lang="EN-US"}**[ **system** **internal** **cfd** { **error** \| **hardware** }]{lang="EN-US"}]{#struct_0_17117_13792_973702919}

[**[undo]{lang="EN-US"}**[ **debugging** **system** **internal** **cfd** { **error** \| **hardware** }]{lang="EN-US"}]{#struct_0_17117_13792_1001743080}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17117_13792_1795993318}

[[CFD]{lang="EN-US"}]{#struct_0_17117_13792_x1843267149}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17117_13792_x987688098}

[[Probe]{lang="EN-US"}]{#struct_0_17117_13792_x752639909}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17117_13792_x1749933305}

[[network-admin]{lang="EN-US"}]{#struct_0_17117_13792_72727400}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17117_13792_x227728257}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17117_13792_595109456}

[**[error]{lang="EN-US"}**]{#struct_0_17117_13792_973768455}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[hardware]{lang="EN-US"}**]{#struct_0_17117_13792_305750033}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[硬件调试信息开关。]{style="font-family:宋体"}
:::

::: {#1637184171 .myid}
[]{#_Toc404798795}[]{#struct_0_17117_13792_1287598677}[]{#_Toc361301941}[]{#_Toc361301942}[]{#_Toc361301943}[]{#_Toc361301944}[]{#_Toc361301945}[]{#_Toc361301946}[]{#_Toc361301947}[]{#_Toc361301948}[]{#_Toc361301949}

**CFD \-- CFD Probe命令 \-- display system internal cfd hardware**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **cfd** **hardware**]{lang="EN-US"}]{#struct_0_17117_13792_973833991}[命令用来显示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[硬件表项的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17117_13792_x1569627263}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17117_13792_x509108675}

[**[display]{lang="EN-US"}**[ **system** **internal** **cfd** **hardware** **level** *level-value* \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_17117_13792_1118410163}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17117_13792_x12450657}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **cfd** **hardware** **slot** *slot-number* **level** *level-value* \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_17117_13792_1435375622}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17117_13792_1899941433}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **cfd** **hardware** **chassis** *chassis-number* **slot** *slot-number* **level** *level-value* \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_17117_13792_x1801657622}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17117_13792_1100587331}

[[Probe]{lang="EN-US"}]{#struct_0_17117_13792_780566807}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17117_13792_973899527}

[[network-admin]{lang="EN-US"}]{#struct_0_17117_13792_109767945}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17117_13792_1036336883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17117_13792_x1419039744}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17117_13792_494775696}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17117_13792_752513944}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17117_13792_x449629263}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[level]{lang="EN-US"}**[ *level-value*]{lang="EN-US"}]{#struct_0_17117_13792_x41932027}[：显示指定]{style="font-family:宋体"}[MD]{lang="EN-US"}[级别的信息，]{style="font-family:宋体"}*[level-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_17117_13792_x1261645245}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示无]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[属性的]{style="font-family:宋体"}[CFD]{lang="EN-US"}[硬件表项信息。]{style="font-family:宋体"}
:::

::: {#-1994419823 .myid}
[]{#_Toc404798796}[]{#struct_0_17117_13792_973113095}[]{#_Toc361301951}[]{#_Toc361301952}[]{#_Toc361301953}[]{#_Toc361301954}[]{#_Toc361301955}[]{#_Toc361301956}[]{#_Toc361301957}[]{#_Toc361301958}[]{#_Toc361301959}[]{#_Toc361301960}[]{#_Toc361301961}[]{#_Toc361301962}[]{#_Toc361301963}[]{#_Toc361301964}[]{#_Toc361301986}

**CFD \-- CFD Probe命令 \-- display system internal cfd mep**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **cfd** **mep**]{lang="EN-US"}]{#struct_0_17117_13792_1039545094}[命令用来显示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[节点信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17117_13792_1893191034}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17117_13792_x2140478478}

[**[display]{lang="EN-US"}**[ **system** **internal** **cfd** **mep** *mep-id* **service-instance** *instance-id*]{lang="EN-US"}]{#struct_0_17117_13792_92961241}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17117_13792_x216261563}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **cfd** **mep** *mep-id* **service-instance** *instance-id* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17117_13792_1789025626}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17117_13792_x365773190}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **cfd** **mep** *mep-id* **service-instance** *instance-id* **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17117_13792_1125613377}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17117_13792_x2083614360}

[[Probe]{lang="EN-US"}]{#struct_0_17117_13792_973178631}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17117_13792_1812220330}

[[network-admin]{lang="EN-US"}]{#struct_0_17117_13792_x56556188}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17117_13792_641242567}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17117_13792_x52280076}

[*[mep-id]{lang="EN-US"}*]{#struct_0_17117_13792_897909209}[：显示指定]{style="font-family:宋体"}[MEP]{lang="EN-US"}[上的信息。其中，]{style="font-family:宋体"}*[mep-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8191]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-instance]{lang="EN-US"}**[ *instance-id*]{lang="EN-US"}]{#struct_0_17117_13792_x731236401}[：显示指定服务实例中的信息。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[表示服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17117_13792_x1316030278}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_17117_13792_1428373511}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17117_13792_973637384}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
