::: {#83287009 .myid}
[]{#_Toc404799992}[]{#struct_0_x1591_x1845_1485539082}

**OpenFlow \-- OpenFlow Probe命令 \-- debugging system internal openflow**

------------------------------------------------------------------------

[**[debugging ]{lang="EN-US"}**]{#struct_0_x1591_x1845_1114064538}**[system internal]{lang="EN-US" style="color:black"}[ openflow]{lang="EN-US"}**[命令用来打开]{style="font-family:
宋体"}[OpenFlow]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[undo debugging ]{lang="EN-US"}**]{#struct_0_x1591_x1845_x2081564782}**[system internal]{lang="EN-US" style="color:black"}[ openflow]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[OpenFlow]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1591_x1845_2063582411}

[**[debugging ]{lang="EN-US"}**]{#struct_0_x1591_x1845_1569468579}**[system internal]{lang="EN-US" style="color:black"}[ openflow]{lang="EN-US"}**

[**[undo debugging ]{lang="EN-US"}**]{#struct_0_x1591_x1845_1145679470}**[system internal]{lang="EN-US" style="color:black"}[ openflow]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1591_x1845_x348092016}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x1591_x1845_x1245960397}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1591_x1845_48250722}

[[Probe]{lang="EN-US"}]{#struct_0_x1591_x1845_1649347766}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1591_x1845_1470627059}

[[network-admin]{lang="EN-US"}]{#struct_0_x1591_x1845_381713351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1591_x1845_142253748}
:::

::: {#-1244528517 .myid}
[]{#_Toc404799993}[]{#struct_0_x1591_x1845_x1137829064}

**OpenFlow \-- OpenFlow Probe命令 \-- display system internal openflow instance**

------------------------------------------------------------------------

[**[display system internal openflow instance]{lang="EN-US"}**]{#struct_0_x1591_x1845_x806107921}[命令用来显示]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[内部实例信息和流表信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1591_x1845_1159286446}

[**[display system internal openflow instance]{lang="EN-US"}**[ { **inner** \| **inner-redirect** } \[ **flow-table** \[ *table-id* \] \| **group** \[ *group-id* \] \]]{lang="EN-US"}]{#struct_0_x1591_x1845_x2100729419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1591_x1845_x229462077}

[[Probe]{lang="EN-US"}]{#struct_0_x1591_x1845_1234889467}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1591_x1845_x755940266}

[[network-admin]{lang="EN-US"}]{#struct_0_x1591_x1845_1249506027}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1591_x1845_1739491215}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1591_x1845_x311779332}

[**[inner]{lang="EN-US"}**]{#struct_0_x1591_x1845_1154089728}[：]{style="font-family:宋体"}[内部二次引流实例运行信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[inner-redirect]{lang="EN-US"}**]{#struct_0_x1591_x1845_851203408}[：内部引流实例运行信息。]{style="font-family:宋体"}

[**[flow-table ]{lang="EN-US"}**[\[ *table-id* \]]{lang="EN-US"}]{#struct_0_x1591_x1845_x1439305439}[：流表信息。]{style="font-family:宋体"}*[table-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[流表]{style="font-family:宋体"}[ID]{lang="IT"}[，取值范围为]{style="font-family:宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[254]{lang="IT"}[。如果未指定本参数，将显示所有流表的信息]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**[ \[ *group-id* \]]{lang="EN-US"}]{#struct_0_x1591_x1845_x679370003}[：]{style="font-family:宋体"}[Group]{lang="EN-US"}[表项]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[Group ID]{lang="EN-US"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[0xffffff00]{lang="IT"}[。如果未指定本参数，将显示实例所有]{style="font-family:宋体"}[Group]{lang="EN-US"}[表项]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
