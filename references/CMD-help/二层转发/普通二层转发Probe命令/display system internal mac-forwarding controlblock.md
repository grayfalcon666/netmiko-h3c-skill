::::: {#1073791520 .myid}
[]{#_Toc404800455}[]{#struct_0_x1607_30507_x1752099503}[]{#_Toc401842322}[]{#_Toc401842323}[]{#_Toc401842324}[]{#_Toc401842325}[]{#_Toc401842326}[]{#_Toc401842327}[]{#_Toc401842328}[]{#_Toc401842329}[]{#_Toc401842330}[]{#_Toc401842331}[]{#_Toc401842332}[]{#_Toc401842333}[]{#_Toc401842334}[]{#_Toc401842335}[]{#_Toc401842336}[]{#_Toc401842337}[]{#_Toc401842338}[]{#_Toc401842339}[]{#_Toc401842340}[]{#_Toc401842341}[]{#_Toc401842342}[]{#_Toc401842343}[]{#_Toc401842344}[]{#_Toc401842345}[]{#_Toc401842346}[]{#_Toc401842347}[]{#_Toc401842348}[]{#_Toc401842349}[]{#_Toc401842350}[]{#_Toc401842351}[]{#_Toc401842352}[]{#_Toc401842353}[]{#_Toc401842354}[]{#_Toc401842355}[]{#_Toc401842356}[]{#_Toc401842357}[]{#_Toc401842358}[]{#_Toc401842359}[]{#_Toc401842360}[]{#_Toc401842361}[]{#_Toc401842362}[]{#_Toc401842363}[]{#_Toc401842364}[]{#_Toc401842365}[]{#_Toc401842366}[]{#_Toc401842367}[]{#_Toc401842368}[]{#_Toc401842369}[]{#_Toc401842370}[]{#_Toc401842371}

**二层转发 \-- 普通二层转发Probe命令 \-- display system internal mac-forwarding controlblock**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](二层转发Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1607_30507_1471710210}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1607_30507_1491625736}
:::

[ ]{lang="EN-US"}

[**[display system internal mac-forwarding controlblock]{lang="EN-US"}**]{#struct_0_x1607_30507_682538553}[命令用来显示二层转发的接口控制信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1607_30507_x163006488}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1607_30507_x592847878}

[**[display system internal mac-forwarding controlblock interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1607_30507_x2057406}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1607_30507_1514082984}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mac-forwarding controlblock interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number ]{lang="EN-US"}*[\[ **cpu**]{lang="EN-US"}*[ cpu-number]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_x1607_30507_421469158}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1607_30507_1507490885}[模式：]{style="font-family:宋体"}

[**[display system internal mac-forwarding controlblock interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*[ **chassis** *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_2054103917}**[ ]{lang="EN-US"}***[slot-number ]{lang="EN-US"}*[\[ **cpu**]{lang="EN-US"}*[ cpu-number]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1607_30507_1942075997}

[[Probe]{lang="EN-US"}]{#struct_0_x1607_30507_655287804}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1607_30507_330280303}

[[network-admin]{lang="EN-US"}]{#struct_0_x1607_30507_932750690}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1607_30507_x1568184273}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1607_30507_428004834}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1607_30507_1491625735}[：显示指定接口的二层转发控制信息。其中，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为指定接口类型和接口编号。]{style="font-family:
宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1607_30507_682341945}[：显示指定]{style="font-family:宋体"}[单板的二层转发控制信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1607_30507_279588687}[：显示指定成员设备的]{style="font-family:宋体"}[二层转发控制信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1607_30507_496106279}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[二层转发控制信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1607_30507_x653052942}[：显示指定成员设备上指定单板的二层转发控制信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1607_30507_x1069977662}[：显示指定单板的二层转发控制信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位]{style="font-family:宋体"}[号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1607_30507_88082538}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[二层转发控制信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::

::::: {#635600327 .myid}
[]{#_Toc404800457}[]{#struct_0_x1607_30507_1179440557}

**二层转发 \-- 快速二层转发Probe命令 \-- display system internal mac-forwarding cache ip verbose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](二层转发Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1607_30507_x1225116546}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1607_30507_1302828940}
:::

[ ]{lang="EN-US"}

[**[display system internal mac-forwarding cache ip verbose]{lang="EN-US"}**]{#struct_0_x1607_30507_531023806}[命令用来显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[快转表项的详细内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1607_30507_752589109}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1607_30507_x1592160267}

[**[display system internal mac-forwarding cache ip]{lang="EN-US"}**[ \[ *ip-address* \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_x241688711}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1607_30507_1125296276}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mac-forwarding cache ip]{lang="EN-US"}**[ \[ *ip-address* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_x521712915}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1607_30507_1044048559}[模式：]{style="font-family:宋体"}

[**[display system internal mac-forwarding cache]{lang="EN-US"}**[ **ip** \[ *ip-address* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_x1418139471}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1607_30507_891768799}

[[probe]{lang="EN-US"}]{#struct_0_x1607_30507_276599568}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1607_30507_1207667968}

[[network-admin]{lang="EN-US"}]{#struct_0_x1607_30507_x317226637}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1607_30507_2004466478}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1607_30507_1905131810}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1607_30507_x2029283225}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的快速转发表信息。如果不指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，将显示所有快速转发表信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x440787665}*[slot-number]{lang="EN-US"}*[：显示指定单板的快速转发表信息。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_968936040}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有成员设备的快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_x1283811940}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_452254636}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的快速转发表信息。如果不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_508442063}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板的快速转发表信息。如果不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x1375770893}*[cpu-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上快速转发表信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::

::::: {#479275988 .myid}
[]{#_Toc404800458}[]{#struct_0_x1607_30507_x1215708004}

**二层转发 \-- 快速二层转发Probe命令 \-- display system internal mac-forwarding cache ipv6 verbose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](二层转发Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1607_30507_2024463038}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1607_30507_x707951177}
:::

[ ]{lang="EN-US"}

[**[display system internal mac-forwarding cache]{lang="EN-US"}**[ **ipv6 verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_780756574}[命令用来显示分布式各板]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快转表项的详细内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1607_30507_x1198632756}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1607_30507_1481592172}

[**[display system internal mac-forwarding cache ipv6]{lang="EN-US"}**[ \[ *ipv6-address* \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_x1013346924}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1607_30507_1748013203}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal mac-forwarding cache ipv6]{lang="EN-US"}**[ \[ *ipv6-address* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_830525242}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1607_30507_26825857}[模式：]{style="font-family:宋体"}

[**[display system internal mac-forwarding cache ipv6]{lang="EN-US"}**[ \[ *ipv6-address* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_281456222}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1607_30507_234557327}

[[probe]{lang="EN-US"}]{#struct_0_x1607_30507_1804387038}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1607_30507_99058145}

[[network-admin]{lang="EN-US"}]{#struct_0_x1607_30507_x84491769}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1607_30507_x450966859}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1607_30507_x810666167}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1607_30507_449362967}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_1368795900}*[slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_x32531854}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_x1650575710}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_783616422}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x178116340}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x2048410214}*[cpu-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::

::::: {#834373389 .myid}
[]{#_Toc404800460}[]{#struct_0_x1607_30507_556398033}

**二层转发 \-- Bridge快速转发Probe命令 \-- display system internal bridge cache ip verbose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](二层转发Probe命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1607_30507_1506434806}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1607_30507_556463569}
:::

[ ]{lang="EN-US"}

[**[display system internal bridge cache ip verbose]{lang="EN-US"}**]{#struct_0_x1607_30507_x211252595}[命令用来显示]{style="font-family:宋体"}[Bridge]{lang="EN-US"}[转发创建的]{style="font-family:宋体"}[IP]{lang="EN-US"}[快速转发表的详细内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1607_30507_x832217354}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1607_30507_74810395}

[**[display system internal bridge cache ip]{lang="EN-US"}**[ \[ *ip-address* \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_1650931378}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1607_30507_x832217351}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal bridge cache ip]{lang="EN-US"}**[ \[ *ip-address* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_75138075}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1607_30507_x1747228347}[模式：]{style="font-family:宋体"}

[**[display system internal bridge cache]{lang="EN-US"}**[ **ip** \[ *ip-address* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_x56729865}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1607_30507_x1826194490}

[[probe]{lang="EN-US"}]{#struct_0_x1607_30507_1197457124}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1607_30507_770297030}

[[network-admin]{lang="EN-US"}]{#struct_0_x1607_30507_x56729866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1607_30507_x1826194493}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1607_30507_x1531426231}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1607_30507_x56729863}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的快速转发表信息。如果不指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，将显示所有快速转发表信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x1826194488}*[slot-number]{lang="EN-US"}*[：显示指定单板的快速转发表信息。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_1553753020}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有成员设备的快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_1658905693}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_1155974876}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的快速转发表信息。如果不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x739386135}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板的快速转发表信息。如果不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x56729864}*[cpu-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上快速转发表信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}
:::::

::::: {#-1865376946 .myid}
[]{#struct_0_x1607_30507_x1826194491}[]{#_Toc404800461}

**二层转发 \-- Bridge快速转发Probe命令 \-- display system internal bridge cache ipv6 verbose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](二层转发Probe命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1607_30507_x368626817}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1607_30507_x56729861}
:::

[ ]{lang="EN-US"}

[**[display system internal bridge cache ipv6 verbose]{lang="EN-US"}**]{#struct_0_x1607_30507_x1826194486}[命令用来显示]{style="font-family:宋体"}[Bridge]{lang="EN-US"}[转发创建的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表的详细内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1607_30507_2004091714}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1607_30507_x56729862}

[**[display system internal bridge cache ipv6]{lang="EN-US"}**[ \[ *ipv6-address* \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_x1826194489}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1607_30507_x12330921}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal bridge cache ipv6]{lang="EN-US"}**[ \[ *ipv6-address* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_x1581114773}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1607_30507_x56729859}[模式：]{style="font-family:宋体"}

[**[display system internal bridge cache]{lang="EN-US"}**[ **ipv6** \[ *ipv6-address* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **verbose**]{lang="EN-US"}]{#struct_0_x1607_30507_512457666}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1607_30507_x1292092915}

[[probe]{lang="EN-US"}]{#struct_0_x1607_30507_x56729860}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1607_30507_x1826194487}

[[network-admin]{lang="EN-US"}]{#struct_0_x1607_30507_1519410940}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1607_30507_x819241227}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1607_30507_1085824350}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1607_30507_x601667367}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x819241228}*[slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_1085758814}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有成员设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1607_30507_2109244387}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_x819241225}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_1790503323}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。如果不指定]{style="font-family:宋体"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[，将显示所有单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1607_30507_1085955422}*[cpu-number]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[快速转发表信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::::
