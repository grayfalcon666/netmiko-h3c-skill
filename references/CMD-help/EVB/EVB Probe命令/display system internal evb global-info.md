::: {#1337208111 .myid}
[]{#_Toc293559741}[]{#_Toc339972636}[]{#_Toc404798816}[]{#struct_0_x1846_x3220_1791238380}[]{#_Toc343245648}

**EVB \-- EVB Probe命令 \-- display system internal evb global-info**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **evb** **global-info**]{lang="EN-US"}]{#struct_0_x1846_x3220_1135522830}[命令用来显示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[子线程的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1846_x3220_1223753133}

[**[display]{lang="EN-US"}**[ **system** **internal** **evb** **global-info**]{lang="EN-US"}]{#struct_0_x1846_x3220_1623560531}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1846_x3220_x1765264579}

[[Probe]{lang="EN-US"}]{#struct_0_x1846_x3220_1512858128}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1846_x3220_x1067276042}

[[network-admin]{lang="EN-US"}]{#struct_0_x1846_x3220_x1977710839}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1846_x3220_1294678948}
:::

::: {#-158196814 .myid}
[]{#_Toc404798817}[]{#struct_0_x1846_x3220_x1505474044}[]{#_Toc361302045}[]{#_Toc361302046}[]{#_Toc361302047}[]{#_Toc361302048}[]{#_Toc361302049}[]{#_Toc361302050}[]{#_Toc361302051}[]{#_Toc361302052}[]{#_Toc361302053}[]{#_Toc361302054}[]{#_Toc361302055}[]{#_Toc361302074}

**EVB \-- EVB Probe命令 \-- display system internal evb kernel**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **system** **internal** **evb** **kernel**]{lang="EN-US"}]{#struct_0_x1846_x3220_641762762}[命令用来显示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[内核的数据信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1846_x3220_x660186349}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1846_x3220_x695083938}

[**[display]{lang="EN-US"}**[ **system** **internal** **evb** **kernel** **interface** ]{lang="EN-US"}]{#struct_0_x1846_x3220_715245426}**[s-channel]{lang="PT-BR"}**[ { *interface-number*:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}[ \| interface-number]{lang="EN-US"}*[:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}*[.*vsi-local-id* } \[ **section** *section-number* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1846_x3220_x1705363403}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **evb** **kernel** **slot** *slot-number* **interface** ]{lang="EN-US"}]{#struct_0_x1846_x3220_x1649522532}**[s-channel]{lang="PT-BR"}**[ { *interface-number*:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}[ \| interface-number]{lang="EN-US"}*[:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}*[.*vsi-local-id* } \[ **section** *section-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1846_x3220_x1977383159}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **system** **internal** **evb** **kernel** **chassis** *chassis-number* **slot** *slot-number* **interface** ]{lang="EN-US"}]{#struct_0_x1846_x3220_798067450}**[s-channel]{lang="PT-BR"}**[ { *interface-number*:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}[ \| interface-number]{lang="EN-US"}*[:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}*[.*vsi-local-id* } \[ **section** *section-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1846_x3220_1895706418}

[[Probe]{lang="EN-US"}]{#struct_0_x1846_x3220_x1534180989}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1846_x3220_524474380}

[[network-admin]{lang="EN-US"}]{#struct_0_x1846_x3220_x692338978}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1846_x3220_x687832828}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1846_x3220_x758752199}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1846_x3220_2119633276}[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1846_x3220_x777086184}[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1846_x3220_x1977448695}[：显示指定成员设备上指定单板的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1846_x3220_x1830451985}**[s-channel]{lang="PT-BR"}**[ { *interface-number*:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}[ \| interface-number]{lang="EN-US"}*[:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}*[.*vsi-local-id* }]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[上的信息。其中，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[S]{lang="EN-US"}[通道所在端口的编号；]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="EN-US"}[通道的编号，取值范围为已创建]{style="font-family:宋体"}[S]{lang="EN-US"}[通道的编号；]{style="font-family:宋体"}*[vsi-local-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号，取值范围为已创建的]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号。]{style="font-family:宋体"}

[**[section]{lang="EN-US"}**[ *section-number*]{lang="EN-US"}]{#struct_0_x1846_x3220_x1459049185}[：显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口下指定段的过滤信息（每个段包含]{style="font-family:宋体"}[60]{lang="EN-US"}[条]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息），]{style="font-family:宋体"}*[section-number]{lang="EN-US"}*[表示段的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将只显示第一段的过滤信息。当]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口下的过滤信息较多时，可使用本参数进行分段显示，比如当]{style="font-family:宋体"}*[section-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[时显示第]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[条过滤信息，]{style="font-family:宋体"}*[section-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[2]{lang="EN-US"}[时显示第]{style="font-family:宋体"}[61]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[条过滤信息，......以此类推。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
