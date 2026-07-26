::: {#-1728193055 .myid}
[]{#_Toc262637992}[]{#_Toc216513766}[]{#_Toc404799544}[]{#struct_0_x1966_13435_431297760}

**IRF \-- IRF2 Probe命令 \-- display system internal irf global**

------------------------------------------------------------------------

[**[display system internal irf global]{lang="EN-US"}**]{#struct_0_x1966_13435_x1275632780}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的部分全局信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1966_13435_858284153}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_1794705054}[设备：]{style="font-family:宋体"}

[**[display system internal irf global]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_x1488210409}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_1997381701}[模式：]{style="font-family:宋体"}

[**[display system internal irf global]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_x1011424203}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1966_13435_933965895}

[[Probe]{lang="EN-US"}]{#struct_0_x1966_13435_1859376980}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1427478134}

[[network-admin]{lang="EN-US"}]{#struct_0_x1966_13435_704702608}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1966_13435_1276341942}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1355956085}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_1135725416}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* slot *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_1595329972}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-813757842 .myid}
[]{#_Toc404799545}[]{#struct_0_x1966_13435_1483358045}[]{#_Toc360006699}[]{#_Toc360006700}[]{#_Toc360006701}[]{#_Toc360006702}[]{#aa_57}[]{#_Toc317589907}[]{#_Toc266869840}[]{#_Toc266284581}[]{#_Toc264097537}[]{#_Ref264046745}

**IRF \-- IRF2 Probe命令 \-- display system internal irf msg**

------------------------------------------------------------------------

[**[display system internal irf msg]{lang="EN-US"}**]{#struct_0_x1966_13435_x1869688135}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x237308781}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x375271294}[设备：]{style="font-family:宋体"}

[**[display system internal irf msg]{lang="EN-US"}**[ \[ **reverse** \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_x1469739719}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x1827850676}[模式：]{style="font-family:宋体"}

[**[display system internal irf msg ]{lang="EN-US"}**[\[ **reverse** \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_x1304333223}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1966_13435_247617852}

[[Probe]{lang="EN-US"}]{#struct_0_x1966_13435_x1115126965}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1966_13435_749943121}

[[network-admin]{lang="EN-US"}]{#struct_0_x1966_13435_x1434138201}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1966_13435_1004359521}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1966_13435_1872969090}

[**[reverse]{lang="EN-US"}**]{#struct_0_x1966_13435_1873746550}[：表示反向显示信息，先显示时间新的日志，再显示时间旧的日志。不指定该参数时，表示按时间先后顺序显示信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_x928321459}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_x1466534505}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#1780318056 .myid}
[]{#_Toc404799546}[]{#struct_0_x1966_13435_1190812647}

**IRF \-- IRF2 Probe命令 \-- display system internal irf roledb**

------------------------------------------------------------------------

[**[display system internal irf roledb]{lang="EN-US"}**]{#struct_0_x1966_13435_787115635}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的角色数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1575233791}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x363938685}[设备：]{style="font-family:宋体"}

[**[display system internal irf roledb]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_x678069031}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_2107500586}[模式：]{style="font-family:宋体"}

[**[display system internal irf roledb]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_2023888772}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1393505482}

[[Probe]{lang="EN-US"}]{#struct_0_x1966_13435_x104227139}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1966_13435_1719553678}

[[network-admin]{lang="EN-US"}]{#struct_0_x1966_13435_x1981503827}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1966_13435_726588996}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1731392749}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_x731567190}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* slot *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_x1332443991}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-110730558 .myid}
[]{#_Toc404799547}[]{#struct_0_x1966_13435_x1285289496}

**IRF \-- IRF2 Probe命令 \-- display system internal irf topodb**

------------------------------------------------------------------------

[**[display system internal irf topodb]{lang="EN-US"}**]{#struct_0_x1966_13435_665596260}[命令用来显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的拓扑数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1966_13435_1079254780}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_1690896301}[设备：]{style="font-family:宋体"}

[**[display system internal irf topodb]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_1691500762}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_947673095}[模式：]{style="font-family:宋体"}

[**[display system internal irf topodb]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_1233408691}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1966_13435_2123741558}

[[Probe]{lang="EN-US"}]{#struct_0_x1966_13435_1161010142}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1966_13435_1131893712}

[[network-admin]{lang="EN-US"}]{#struct_0_x1966_13435_834516751}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1966_13435_1819612790}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x438035532}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_x1894868311}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，则表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）。]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_1583855767}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::::: {#-54971439 .myid}
[]{#_Toc404799548}[]{#struct_0_x1966_13435_1758539430}[]{#_Toc325728114}[]{#_Toc260412083}

**IRF \-- IRF2 Probe命令 \-- irf link-status auto-recovery enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF%20Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1966_13435_2104251563}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1966_13435_1302629308}
:::

[ ]{lang="EN-US"}

[**[irf link-status auto-recovery enable]{lang="EN-US"}**]{#struct_0_x1966_13435_877149467}[命令用来使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路故障恢复功能。]{style="font-family:宋体"}

[**[undo irf link-status auto-recovery enable]{lang="EN-US"}**]{#struct_0_x1966_13435_2012815508}[命令用来关闭]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路故障恢复功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x2100538003}

[**[irf link-status auto-recovery enable]{lang="EN-US"}**]{#struct_0_x1966_13435_209213256}

[**[undo irf link-status auto-recovery enable]{lang="EN-US"}**]{#struct_0_x1966_13435_x308583793}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x787285085}

[[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x560231610}[链路故障恢复功能处于使能状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x307849923}

[[Probe]{lang="EN-US"}]{#struct_0_x1966_13435_x1320940709}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1448759676}

[[network-admin]{lang="EN-US"}]{#struct_0_x1966_13435_x629928018}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1966_13435_1290512019}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1966_13435_2004709077}

[[使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x1219678014}[链路故障恢复功能后，系统能自动对检测到的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路故障尝试修复，增强系统的稳定性。]{style="font-family:宋体"}

[[该命令仅供调试]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x787219549}[链路故障恢复功能运行是否正常]{style="font-family:宋体"}[。如果调试结束，请输入使能命令，确保设备的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路故障恢复功能处于使能状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1966_13435_x2073422842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有先使能]{style="font-family:宋体"}]{#struct_0_x1966_13435_666823701}[IRF]{lang="EN-US"}[链路状态检测功能，本命令才生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_1506436672}[模式下支持。配置]{lang="EN-US" style="font-family:宋体"}**[undo irf link-status auto-recovery enable]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#924034640 .myid}
[]{#_Toc404799549}[]{#struct_0_x1966_13435_2054520954}[]{#_Toc325728113}[]{#_Toc258834803}

**IRF \-- IRF2 Probe命令 \-- irf link-status detect enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IRF%20Probe命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1966_13435_1534662838}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1966_13435_162397709}
:::

[ ]{lang="EN-US"}

[**[irf link-status detect enable]{lang="EN-US"}**]{#struct_0_x1966_13435_1373879844}[命令用来使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路状态检测功能。]{style="font-family:宋体"}

[**[undo irf link-status detect enable]{lang="EN-US"}**]{#struct_0_x1966_13435_x786957405}[命令用来关闭]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路状态检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1772707041}

[**[irf link-status detect enable]{lang="EN-US"}**]{#struct_0_x1966_13435_x711142738}

[**[undo irf link-status detect enable]{lang="EN-US"}**]{#struct_0_x1966_13435_1307568356}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1670920164}

[[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x1620804619}[链路状态检测功能处于使能状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x586370980}

[[Probe]{lang="EN-US"}]{#struct_0_x1966_13435_x1162197856}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x786891869}

[[network-admin]{lang="EN-US"}]{#struct_0_x1966_13435_x910968314}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1966_13435_x942311461}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1966_13435_1409516942}

[[使能]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_1706101881}[链路的状态检测功能后，当存在多于一条]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理连接]{style="font-family:宋体"}[时，系统会检测每条]{style="font-family:宋体"}[IRF]{lang="EN-US"}[物理连接]{style="font-family:宋体"}[是否连通，确保系统能及时发现故障链路。]{style="font-family:宋体"}

[[该命令仅供调试]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_819501149}[链路的状态检测功能运行是否正常]{style="font-family:宋体"}[。如果调试结束，请输入使能命令，确保设备的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[链路状态检测功能处于使能状态。]{style="font-family:宋体"}

[[需要注意的是，本命令只在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x1841955420}[模式下支持。配置]{style="font-family:宋体"}**[undo irf link-status detect enable]{lang="EN-US"}**[命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式，仍需重新配置。]{style="font-family:宋体"}
:::::

::: {#157542144 .myid}
[]{#_Toc404799550}[]{#struct_0_x1966_13435_x328282663}

**IRF \-- IRF2 Probe命令 \-- reset system internal irf msg**

------------------------------------------------------------------------

[**[reset system internal irf msg]{lang="EN-US"}**]{#struct_0_x1966_13435_219802086}[命令用来清空]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[日志消息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1966_13435_1739934770}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_1594031638}[设备：]{style="font-family:宋体"}

[**[reset system internal irf msg]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_1004987412}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_334069909}[模式：]{style="font-family:宋体"}

[**[reset system internal irf msg]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x1966_13435_1599886592}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1256308509}

[[Probe]{lang="EN-US"}]{#struct_0_x1966_13435_1363931628}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1887058114}

[[network-admin]{lang="EN-US"}]{#struct_0_x1966_13435_1854954898}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1966_13435_1663127943}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1966_13435_1584563181}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_1671889467}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示主设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_688724625}[：]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示主控板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的全局主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}
:::

::: {#-1251326491 .myid}
[]{#_Toc404799552}[]{#struct_0_x1966_13435_1373552161}[]{#_Toc388427586}

**IRF \-- IRF3 Probe命令 \-- display system internal pex-port verbose**

------------------------------------------------------------------------

[**[display system internal pex-port verbose]{lang="EN-US"}**]{#struct_0_x1966_13435_x562815596}[命令用来显示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的信息，包括]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的编号、描述信息、绑定的物理端口的信息等。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1966_13435_707094743}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x105421964}[设备：]{style="font-family:宋体"}

[**[display system internal pex-port verbose slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_x570726909}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1966_13435_x577126845}[模式：]{style="font-family:宋体"}

[**[display system internal pex-port verbose chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_1731050905}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1966_13435_1035932954}

[[Probe]{lang="EN-US" style="color:black"}]{#struct_0_x1966_13435_x915538641}[视图]{style="font-family:宋体;color:black"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x1929412507}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_x1966_13435_29792684}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_x1966_13435_582320143}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1966_13435_x78800970}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_2038371272}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上保存的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1966_13435_x1248750759}[：显示指定单板]{style="font-family:
宋体"}[/PEX]{lang="EN-US"}[上保存的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[端口的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
