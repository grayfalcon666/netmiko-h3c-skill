::::: {#1198809358 .myid}
[]{#_Toc404793911}[]{#struct_0_x5542_17155_881130768}[]{#_Toc302999829}[]{#_Toc297297256}

**IPv4 uRPF \-- IPv4 uRPF配置命令 \-- display ip urpf**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](uRPF命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5542_17155_92705714}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5542_17155_306098580}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **ip** **urpf**]{lang="EN-US"}]{#struct_0_x5542_17155_2112262442}[命令用来显示]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[的配置应用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1115156696}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x5542_17155_x1345401329}

[**[display]{lang="EN-US"}**[ **ip** **urpf** ]{lang="EN-US"}[\[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x5542_17155_1696892295}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5542_17155_x1404998025}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **ip** **urpf** ]{lang="EN-US"}[\[ **interface** *interface-type* *interface-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x5542_17155_127000121}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5542_17155_949403755}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **ip** **urpf** ]{lang="EN-US"}[\[ **interface** *interface-type* *interface-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x5542_17155_799795923}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5542_17155_1710630560}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5542_17155_1683817692}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1685728189}

[[network-admin]{lang="EN-US"}]{#struct_0_x5542_17155_x1345335793}

[[network-operator]{lang="EN-US"}]{#struct_0_x5542_17155_x62564066}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5542_17155_1216086427}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5542_17155_x965349795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5542_17155_1387065519}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x5542_17155_903659128}[：接口类型和接口编号。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x5542_17155_x1085293059}[：显示指定单板上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x5542_17155_x1583620918}[：显示指定成员设备]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x5542_17155_x911020756}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x5542_17155_1465585524}[：显示指定成员设备上指定单板上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x5542_17155_x911217364}[：显示指定单板上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_x5542_17155_x88412473}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[cpu]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5542_17155_2113887109}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_1974037559}[显示单板]{style="font-family:宋体"}[slot 3]{lang="EN-US"}[上]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[的应用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display ip urpf slot 3]{lang="EN-US"}]{#struct_0_x5542_17155_307461137}

[Global uRPF configuration information(failed):]{lang="EN-US"}

[   Check type: strict]{lang="EN-US"}

[   Allow default route]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_x326453199}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上已经应用的]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[的配置情况。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display ip urpf interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x5542_17155_x1344811508}

[uRPF configuration information of interface GigabitEthernet1/0/1:]{lang="EN-US"}

[   Check type: strict]{lang="EN-US"}

[   Allow default route]{lang="EN-US"}

[   Link check]{lang="EN-US"}

[   Suppress drop ACL: 3000]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip urpf]{lang="EN-US"}]{#struct_0_x5542_17155_x1632011900}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1717894669}[[字段]{style="font-family:黑体"}]{#struct_0_x5542_17155_630454469}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1943939069}

[[Global uRPF configuration information]{lang="EN-US"}]{#struct_0_x5542_17155_x1739076271}

[[全局]{style="font-family:宋体"}[uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x113436065}[配置应用情况]{style="font-family:宋体"}

[[uRPF configuration information of interface]{lang="EN-US"}]{#struct_0_x5542_17155_x1533494311}

[[接口]{style="font-family:宋体"}[uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x1344745972}[配置应用情况]{style="font-family:宋体"}

[[(failed)]{lang="EN-US"}]{#struct_0_x5542_17155_513769269}

[[当前]{style="font-family:宋体"}[uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_1846930954}[配置下发转发芯片失败，原因可能为芯片资源不足。没有该字段时表示下发成功]{style="font-family:宋体"}

[[Check type ]{lang="EN-US"}]{#struct_0_x5542_17155_1000293044}

[[uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_1001041813}[检查类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loose]{lang="EN-US"}**]{#struct_0_x5542_17155_1429248132}[：松散型检查]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[strict]{lang="EN-US"}**]{#struct_0_x5542_17155_x1344680436}[：严格型检查]{lang="EN-US" style="font-family:宋体"}

[[Allow default route]{lang="EN-US"}]{#struct_0_x5542_17155_1801677698}

[[允许缺省路由]{style="font-family:宋体"}]{#struct_0_x5542_17155_x56655488}

[[Link check]{lang="EN-US"}]{#struct_0_x5542_17155_x284757096}

[[使能]{style="font-family:宋体"}**[link-check]{lang="EN-US"}**]{#struct_0_x5542_17155_1987224295}[功能]{style="font-family:宋体"}

[[Suppress drop ACL]{lang="EN-US"}]{#struct_0_x5542_17155_1534216727}

[[配置了抑制丢弃，显示配置的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x5542_17155_x1344614900}[规则号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::::::::: {#-1092760003 .myid}
[]{#_Toc404793912}[]{#struct_0_x5542_17155_1918031024}[]{#_Toc302999828}[]{#_Toc297297255}

**IPv4 uRPF \-- IPv4 uRPF配置命令 \-- ip urpf**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](uRPF命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5542_17155_x276655988}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5542_17155_967991450}
:::

[ ]{lang="EN-US"}

[**[ip]{lang="EN-US"}**[ **urpf**]{lang="EN-US"}]{#struct_0_x5542_17155_890054243}[命令用来打开]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **urpf**]{lang="EN-US"}]{#struct_0_x5542_17155_2102219769}[命令用来关闭]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5542_17155_252063892}

[**[ip]{lang="EN-US"}**[ **urpf** { **loose** \[ **allow-default-route** \] \[ **acl** *acl-number* \] \| **strict** \[ **allow-default-route** \] \[ **acl** *acl-number* \] \[ **link-check** \] }]{lang="EN-US"}]{#struct_0_x5542_17155_x158479238}

[**[undo]{lang="EN-US"}**[ **ip** **urpf**]{lang="EN-US"}]{#struct_0_x5542_17155_x1344549364}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1371946099}

[[uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_1517173325}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x460282058}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5542_17155_x539227693}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](uRPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5542_17155_x2103147496}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[同一设备只能支持一种视图，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5542_17155_1032237043}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5542_17155_1140832144}

[[network-admin]{lang="EN-US"}]{#struct_0_x5542_17155_x145794660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5542_17155_x1344483828}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1201253188}

[**[loose]{lang="EN-US"}**]{#struct_0_x5542_17155_x1635491730}[：松散型检查。仅检查报文的源地址是否在转发表中存在，而不再检查报文的入接口与转发表是否匹配。]{style="font-family:宋体"}

[**[strict]{lang="EN-US"}**]{#struct_0_x5542_17155_1751038332}[：严格型检查。不仅检查报文的源地址是否在转发表中存在，而且检查报文的入接口与转发表是否匹配。]{style="font-family:宋体"}

[**[allow-default-route]{lang="EN-US"}**]{#struct_0_x5542_17155_x1270756885}[：允许源地址查转发表时匹配缺省路由表项。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x5542_17155_1475995840}[：访问控制列表，用来抑制报文丢弃。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基本]{style="font-family:宋体"}]{#struct_0_x5542_17155_x1006333515}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[高级]{style="font-family:宋体"}]{#struct_0_x5542_17155_x1149870132}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[link]{lang="EN-US"}[-check]{lang="EN-US"}**]{#struct_0_x5542_17155_1722215705}[：允许对链路信息进行检查。目前仅支持以太网链路。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](uRPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5542_17155_1155454544}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5542_17155_x1344418292}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1936790667}

[[uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_1526880694}[功能一般部署在运营商网络接入客户侧设备的边缘位置，也可以部署在运营商网络对接其他运营商设备的边缘位置设备或部署在客户侧边缘位置设备。]{style="font-family:宋体"}

[[建议在运营商网络接入客户侧设备的边缘位置的接口下配置严格]{style="font-family:宋体"}[uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_603468512}[，在运营商网络对接其他运营商网络的边缘位置的接口下配置松散]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[。如果运营商是用一个三层以太网接口接入大量]{style="font-family:宋体"}[PC]{lang="EN-US"}[机用户时，建议接口下配置]{style="font-family:宋体"}**[link-check]{lang="EN-US"}**[功能。]{style="font-family:宋体"}

[[选择严格或松散]{style="font-family:宋体"}[uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x1724534937}[取决于当前组网中是否存在非对称路径，如果运营商设备上行流量的入接口和下行流量的出接口相同则是对称路径，此时建议用严格]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[。一般运营商接入客户侧的组网中都是对称路径。运营商对接其他运营商的边缘位置可能出现非对称路径，此时建议用松散]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[运营商网络边缘位置一般不会有缺省路由指向客户侧设备，所以一般不需要配置]{style="font-family:宋体"}**[allow-default-route]{lang="EN-US"}**]{#struct_0_x5542_17155_1399104577}[。如果在客户侧边缘设备接口上面启用]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[，这时往往会有缺省路由指向运营商，此时需要配置]{style="font-family:宋体"}**[allow-default-route]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[link-check]{lang="EN-US"}**]{#struct_0_x5542_17155_73411325}[后，设备会根据源地址查转发表得到的下一跳后进一步查]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项来确定源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址是否正确。如果运营商是用以太网接口接入客户，此时一个接口同时接多个不同客户，因此建议接口下配置]{style="font-family:宋体"}**[link-check]{lang="EN-US"}**[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x710587874}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_1337083677}[在全局下配置严格型]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x5542_17155_x1345401332}

[\[Sysname\]ip urpf strict]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_487104250}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上配置严格型]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[检查，同时允许匹配缺省路由，并配置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号为]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x5542_17155_x755037894}

[\[Sysname\]interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\]ip urpf strict allow-default-route acl 2999]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_1708310880}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置松散型]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x5542_17155_1740973060}

[\[Sysname\]interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]ip urpf loose]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x199242215}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ip** **urpf**]{lang="EN-US"}]{#struct_0_x5542_17155_204094540}
:::::::::

::::: {#-236428603 .myid}
[]{#_Toc404793915}[]{#struct_0_x5542_17155_696950821}[]{#_Toc302999833}

**IPv6 uRPF \-- IPv6 uRPF配置命令 \-- display ipv6 urpf**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](uRPF命令.files/image001.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5542_17155_1107923113}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5542_17155_64073257}
:::

[ ]{lang="EN-US"}

[**[display ipv6 urpf]{lang="EN-US"}**]{#struct_0_x5542_17155_x2095490484}[命令用来显示]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[的配置应用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1963574625}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x5542_17155_1627270904}

[**[display ipv6 urpf ]{lang="EN-US"}**[\[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x5542_17155_x467258335}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5542_17155_1133607879}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 urpf ]{lang="EN-US"}**[\[ **interface** *interface-type* *interface-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x5542_17155_x1344877043}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x5542_17155_755448142}[模式：]{style="font-family:宋体"}

[**[display ipv6 urpf ]{lang="EN-US"}**[\[ **interface** *interface-type* *interface-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x5542_17155_x1750493687}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5542_17155_2094051671}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5542_17155_1491130264}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x107980656}

[[network-admin]{lang="EN-US"}]{#struct_0_x5542_17155_x332074556}

[[network-operator]{lang="EN-US"}]{#struct_0_x5542_17155_x361820354}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5542_17155_1373118915}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5542_17155_x1344811507}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5542_17155_384410735}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x5542_17155_1120859187}[：接口类型和接口编号。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x5542_17155_76041299}[：显示指定单板]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x5542_17155_x825742117}[：显示指定成员设备]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备上的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x5542_17155_x911282900}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x5542_17155_x195630414}[：显示指定成员设备上指定单板上的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x5542_17155_1109649605}[：显示指定单板上的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的槽位]{style="font-family:宋体"}[号。如果未指定本参数，则显示所有单板上的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x5542_17155_x170836709}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[配置应用情况。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1344745971}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_2079853210}[显示单板]{style="font-family:宋体"}[slot 3]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[的应用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 urpf slot 3]{lang="EN-US"}]{#struct_0_x5542_17155_902536218}

[Global IPv6 uRPF configuration information(failed):]{lang="EN-US"}

[   Check type: strict]{lang="EN-US"}

[   Allow default route]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_x700171447}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的已经应用的]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[的配置情况。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 urpf interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x5542_17155_763323765}

[IPv6 uRPF configuration information of interface GigabitEthernet1/0/1:]{lang="EN-US"}

[   Check type: loose]{lang="EN-US"}

[   Allow default route]{lang="EN-US"}

[   Suppress drop ACL: 2000]{lang="EN-US"}

[[表2-1 ]{lang="EN-US"}[display ipv6 urpf]{lang="EN-US"}]{#struct_0_x5542_17155_1888722310}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1712158317}[[字段]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1344680435}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x5542_17155_x927205657}

[[Global IPv6 uRPF configuration information]{lang="EN-US"}]{#struct_0_x5542_17155_301703904}

[[全局]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x32101156}[配置应用情况]{style="font-family:宋体"}

[[IPv6 uRPF configuration information of interface]{lang="EN-US"}]{#struct_0_x5542_17155_x776047347}

[[接口]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x745781091}[配置应用情况]{style="font-family:宋体"}

[[(failed)]{lang="EN-US"}]{#struct_0_x5542_17155_x1977252334}

[[当前]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x1344614899}[配置下发转发芯片失败，原因可能为芯片资源不足。没有该字段时表示下发成功]{style="font-family:宋体"}

[[Check type]{lang="EN-US"}]{#struct_0_x5542_17155_x455080722}

[[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_12579239}[检查类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loose]{lang="EN-US"}**]{#struct_0_x5542_17155_968537980}[：松散型检查]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[strict]{lang="EN-US"}**]{#struct_0_x5542_17155_x539531937}[：严格型检查]{lang="EN-US" style="font-family:宋体"}

[[Allow default route]{lang="EN-US"}]{#struct_0_x5542_17155_x1374327335}

[[允许缺省路由]{style="font-family:宋体"}]{#struct_0_x5542_17155_x1344549363}

[[Suppress drop ACL]{lang="EN-US"}]{#struct_0_x5542_17155_550368202}

[[配置了抑制丢弃，显示配置的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}]{#struct_0_x5542_17155_x1172166029}[规则号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::::::: {#347820317 .myid}
[]{#_Toc404793916}[]{#struct_0_x5542_17155_701501866}[]{#_Toc302999832}

**IPv6 uRPF \-- IPv6 uRPF配置命令 \-- ipv6 urpf**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](uRPF命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5542_17155_x714633095}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5542_17155_1048868118}
:::

[ ]{lang="EN-US"}

[**[ipv6 urpf]{lang="EN-US"}**]{#struct_0_x5542_17155_x1321211995}[命令用来打开]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo ipv6 urpf]{lang="EN-US"}**]{#struct_0_x5542_17155_1321569560}[命令用来关闭]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1344483827}

[**[ipv6 urpf]{lang="EN-US"}**[ { **loose** \| **strict** } \[ **allow-default-route** \] \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_x5542_17155_364830753}

[**[undo ipv6 urpf]{lang="EN-US"}**]{#struct_0_x5542_17155_674427884}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5542_17155_1891027690}

[[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x1655517889}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x296790911}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5542_17155_468395593}[接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](uRPF命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5542_17155_x468473809}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[同一设备只能支持一种视图，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5542_17155_851410709}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1344418291}

[[network-admin]{lang="EN-US"}]{#struct_0_x5542_17155_792092688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5542_17155_1068184069}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x1977211365}

[**[loose]{lang="EN-US"}**]{#struct_0_x5542_17155_x525726197}[：松散型检查。仅检查报文的源地址是否在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发表中存在，而不再检查报文的入接口与]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发表是否匹配。]{style="font-family:宋体"}

[**[strict]{lang="EN-US"}**]{#struct_0_x5542_17155_794826827}[：严格型检查。不仅检查报文的源地址是否在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发表中存在，而且检查报文的入接口与]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发表是否匹配。]{style="font-family:宋体"}

[**[allow-default-route]{lang="EN-US"}**]{#struct_0_x5542_17155_549703403}[：允许源地址查]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发时匹配缺省路由表项。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}***[ acl-number]{lang="EN-US"}*]{#struct_0_x5542_17155_x1655039466}[：访问控制列表，用来抑制报文丢弃。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基本]{style="font-family:宋体"}]{#struct_0_x5542_17155_906674756}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[高级]{style="font-family:宋体"}]{#struct_0_x5542_17155_x1345401331}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](uRPF命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5542_17155_2053188191}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5542_17155_x754139890}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5542_17155_473702969}

[[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x2101596069}[功能一般部署在运营商网络接入客户侧设备的边缘位置，也可以部署在运营商网络对接其他运营商设备的边缘位置设备或部署在客户侧边缘位置设备。]{style="font-family:宋体"}

[[建议在运营商网络接入客户侧设备的边缘位置的接口下配置严格]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_x664015915}[，在运营商网络对接其他运营商网络的边缘位置的接口下配置松散]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[选择严格或松散]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x5542_17155_281503591}[取决于当前组网中是否存在非对称路径，如果运营商设备上行流量的入接口和下行流量的出接口相同则是对称路径，此时建议用严格]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[。一般运营商接入客户侧的组网中都是对称路径。运营商对接其他运营商的边缘位置可能出现非对称路径，此时建议用松散]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[运营商网络边缘位置一般不会有缺省路由指向客户侧设备，所以一般不需要配置]{style="font-family:宋体"}**[allow-default-route]{lang="EN-US"}**]{#struct_0_x5542_17155_x1696770442}[。如果在客户侧边缘设备接口上面启用]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[，这时往往会有缺省路由指向运营商，此时需要配置]{style="font-family:宋体"}**[allow-default-route]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5542_17155_101362946}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_x1345335795}[在全局下配置严格型]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x5542_17155_1100235348}

[\[Sysname\]ipv6 urpf strict]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_1958046519}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上配置严格型]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[检查，同时允许匹配缺省路由，并配置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则号为]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x5542_17155_x40474258}

[\[Sysname\]interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\]ipv6 urpf strict allow-default-route acl 2999]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5542_17155_1650657367}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置松散]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x5542_17155_x193530741}

[\[Sysname\]interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]ipv6 urpf loose]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5542_17155_x2098649590}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ipv6** **urpf**]{lang="EN-US"}]{#struct_0_x5542_17155_1579990782}
:::::::::
