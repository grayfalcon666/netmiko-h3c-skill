::: {#2076033456 .myid}
[]{#_Toc404782725}[]{#struct_0_71526_x1155_x337356397}[]{#_Toc339613382}[]{#_Toc339613414}

**ISSU \-- ISSU配置命令 \-- display install active**

------------------------------------------------------------------------

[**[display install active]{lang="EN-US"}**]{#struct_0_71526_x1155_2124544261}[命令用来显示当前系统中处于激活状态的软件包的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1076450584}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x487181173}

[**[display install active]{lang="EN-US"}**[ \[ **verbose** \]]{lang="EN-US"}]{#struct_0_71526_x1155_x617891587}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_362831501}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display install active]{lang="EN-US"}**[ \[ **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_71526_x1155_547736874}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1667661650}[模式：]{style="font-family:宋体"}

[**[display install active]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_71526_x1155_607553288}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_859242475}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1221573576}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1775235098}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x177745489}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_113074299}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2068251159}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_2084915429}[：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x228937555}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x1242351222}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_607487752}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x609049430}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_71526_x1155_1007507}[：显示处于激活状态的软件包的详细信息，包括软件包的名称、基本信息和所包含的组件。不指定该参数时，仅显示软件包的名称。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1000115717}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1963427168}[显示设备上处于激活状态的软件包的简要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display install active]{lang="EN-US"}]{#struct_0_71526_x1155_x466451581}

[Active packages on the device:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/feature.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_669357543}[显示设备上处于激活状态的软件包的简要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display install active]{lang="EN-US"}]{#struct_0_71526_x1155_14719026}

[Active packages on slot 1:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/feature.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_607422216}[显示设备上处于激活状态的软件包的简要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display install active]{lang="EN-US"}]{#struct_0_71526_x1155_x353894280}

[Active packages on chassis 1 slot 1:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/feature.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1836375895}[显示设备上处于激活状态的软件包的详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display install active verbose]{lang="EN-US"}]{#struct_0_71526_x1155_607815432}

[Active packages on the device:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: boot]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: cen]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: boot]{lang="EN-US"}

[ Description: boot package]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/system.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: system]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: cen]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: system]{lang="EN-US"}

[ Description: system package]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: test]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: cen]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: test]{lang="EN-US"}

[ Description: test package]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1290267019}[显示设备上处于激活状态的软件包的详细信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display install active verbose]{lang="EN-US"}]{#struct_0_71526_x1155_607684360}

[Active packages on slot 1:]{lang="EN-US"}

[flash:/boot.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: boot]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: mpu]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: boot]{lang="EN-US"}

[ Description: boot package]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/system.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: system]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: mpu]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: system]{lang="EN-US"}

[ Description: system package]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: test]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: mpu]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: test]{lang="EN-US"}

[ Description: test package]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_284003621}[显示设备上处于激活状态的软件包的详细信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display install active verbose]{lang="EN-US"}]{#struct_0_71526_x1155_607618824}

[Active packages on chassis 1 slot 1:]{lang="EN-US"}

[flash:/boot.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: boot]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: mpu]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: boot]{lang="EN-US"}

[ Description: boot package]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/system.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: system]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: mpu]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: system]{lang="EN-US"}

[ Description: system package]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: XXX]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: test]{lang="EN-US"}

[ Platform version: 7.1.022]{lang="EN-US"}

[ Product version: Test 2201]{lang="EN-US"}

[ Supported board: mpu]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: test]{lang="EN-US"}

[ Description: test package]{lang="EN-US"}

[]{#struct_0_71526_x1155_720532045}[[表1-1 ]{lang="EN-US"}[display install active]{lang="EN-US"}]{#_Ref302142357}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1135483062}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_1397230088}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_608077576}

[[Active packages on the device]{lang="EN-US"}]{#struct_0_71526_x1155_x349003797}

[[设备上处于激活状态的软件包的相关信息（集中式设备）]{style="font-family:宋体"}]{#struct_0_71526_x1155_x431645754}

[[Active packages on slot *n*]{lang="EN-US"}]{#struct_0_71526_x1155_1798085585}

[[某单板上处于激活状态的软件包的相关信息，其中]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_71526_x1155_968996469}[表示该单板所在的槽位号（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[Active packages on slot *n*]{lang="EN-US"}]{#struct_0_71526_x1155_1424124101}

[[某成员设备上处于激活状态的软件包的相关信息，其中]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_71526_x1155_608012040}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Active packages on chassis *m* slot *n*]{lang="EN-US"}]{#struct_0_71526_x1155_1236621708}

[[某单板上处于激活状态的软件包的相关信息，其中]{style="font-family:宋体"}*[m]{lang="EN-US"}*]{#struct_0_71526_x1155_1897373758}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[表示成员设备上该单板所在的槽位号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[flash:/boot.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x1986856196}

[[软件包的名称]{style="font-family:宋体"}]{#struct_0_71526_x1155_943865738}

[[\[Package\]]{lang="EN-US"}]{#struct_0_71526_x1155_x335555416}

[[软件包的信息]{style="font-family:宋体"}]{#struct_0_71526_x1155_607553285}

[[Vendor]{lang="EN-US"}]{#struct_0_71526_x1155_859242478}

[[生产厂商]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1221573579}

[[Product]{lang="EN-US"}]{#struct_0_71526_x1155_503309563}

[[产品名称]{style="font-family:宋体"}]{#struct_0_71526_x1155_1132510481}

[[Service name]{lang="EN-US"}]{#struct_0_71526_x1155_x236907392}

[[软件包所包含的服务名称：]{style="font-family:宋体"}]{#struct_0_71526_x1155_607487749}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{style="font-family:宋体"}]{#struct_0_71526_x1155_1957322634}[boot]{lang="EN-US"}[，表示该软件包为]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{lang="EN-US" style="font-family:宋体"}[system]{lang="EN-US"}]{#struct_0_71526_x1155_x238863359}[，表示该软件包为]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为]{style="font-family:宋体"}]{#struct_0_71526_x1155_2121226157}[patch]{lang="EN-US"}[，表示该软件包为补丁包]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果显示为其它值，则表示该软件包为提供某项功能的]{style="font-family:宋体"}]{#struct_0_71526_x1155_544226788}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}

[[Platform version]{lang="EN-US"}]{#struct_0_71526_x1155_607422213}

[[平台软件版本号]{style="font-family:宋体"}]{#struct_0_71526_x1155_x353894283}

[[Product version]{lang="EN-US"}]{#struct_0_71526_x1155_x1836572503}

[[产品软件版本号]{style="font-family:宋体"}]{#struct_0_71526_x1155_2079185186}

[[Supported board]{lang="EN-US"}]{#struct_0_71526_x1155_x159415775}

[[软件包支持的单板类型（本字段的取值与设备的型号有关，请以设备的实际情况为准）：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1317164153}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[cen]{lang="EN-US"}]{#struct_0_71526_x1155_1453535607}[表示集中式设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[m]{lang="EN-US"}]{#struct_0_71526_x1155_607815429}[pu]{lang="EN-US"}[表示主控板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[lc]{lang="EN-US"}]{#struct_0_71526_x1155_x1048385132}[表示]{lang="EN-US" style="font-family:宋体"}[业务板]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sfc]{lang="EN-US"}]{#struct_0_71526_x1155_x525547484}[表示网板]{lang="EN-US" style="font-family:宋体"}

[[\[Component\]]{lang="EN-US"}]{#struct_0_71526_x1155_x1532078642}

[[组件信息，表示软件包的组成部分]{style="font-family:宋体"}]{#struct_0_71526_x1155_607684357}

[[Component]{lang="EN-US"}]{#struct_0_71526_x1155_x2054648540}

[[组件的名称]{style="font-family:宋体"}]{#struct_0_71526_x1155_x782093539}

[[Description]{lang="EN-US"}]{#struct_0_71526_x1155_493997933}

[[组件的描述信息]{style="font-family:宋体"}]{#struct_0_71526_x1155_607618821}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_720532040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install active]{lang="EN-US"}**]{#struct_0_71526_x1155_1397230083}

::: {#-621959267 .myid}
[]{#_Toc404782726}[]{#struct_0_71526_x1155_241981671}

**ISSU \-- ISSU配置命令 \-- display install backup**

------------------------------------------------------------------------

[**[display install backup]{lang="EN-US"}**]{#struct_0_71526_x1155_1099292883}[命令用来显示设备下次启动时使用的备用软件包的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1550610353}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_1648633035}

[**[display install backup]{lang="EN-US"}**[ \[ **verbose** \]]{lang="EN-US"}]{#struct_0_71526_x1155_1431817975}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_608077573}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display install backup]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x349003794}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x431842362}[模式：]{style="font-family:宋体"}

[**[display install backup]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_189713483}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_661531385}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_522815792}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1560391200}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_437307529}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_x175800866}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x507903231}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_608012037}[：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x337356403}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x1598581582}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备和本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x214370052}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x546712101}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/]{lang="EN-US"}[本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板和本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_71526_x1155_1058980488}*[cpu-number]{lang="EN-US"}*[：表示安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于显示安全引擎下次启动时使用的备用软件包的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_71526_x1155_1145098817}[：显示详细信息，包括软件包的名称、基本信息和所包含的组件。不指定该参数时，仅显示软件包的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1196758867}

[[设备下次启动时使用的软件包的名称会记录在启动软件包列表中，启动软件包列表分为主用启动软件包列表和备用启动软件包列表，可以分别配置。]{style="font-family:宋体"}]{#struct_0_71526_x1155_908471600}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备启动时，优先使用主用启动软件包列表中的软件包。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x588808625}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主用启动软件包列表中的]{style="font-family:宋体"}]{#struct_0_71526_x1155_1411489943}[Boot]{lang="EN-US"}[包或]{style="font-family:宋体"}[System]{lang="EN-US"}[包不存在或者损坏，再使用备用启动软件包列表中的软件包。]{style="font-family:宋体"}

[[执行]{style="font-family:宋体"}**[boot-loader file]{lang="EN-US"}**]{#struct_0_71526_x1155_x712428326}[命令可以修改设备下次启动时使用的备用软件包列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_607553286}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_859242477}[显示设备下次启动时使用的备用软件包的相关信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display install backup]{lang="EN-US"}]{#struct_0_71526_x1155_x1221573574}

[Backup startup software images on the device:]{lang="EN-US"}

[  flash:/boot-a0201.bin]{lang="EN-US"}

[[  flash:/system-a0201.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x612435684}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x184995723}[显示设备下次启动时使用的备用软件包的相关信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display install backup]{lang="EN-US"}]{#struct_0_71526_x1155_1496484948}

[Backup startup software images on slot 1:]{lang="EN-US"}

[  flash:/boot-a0201.bin]{lang="EN-US"}

[  flash:/system-a0201.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1648547183}[显示设备下次启动时使用的备用软件包的相关信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display install backup]{lang="EN-US"}]{#struct_0_71526_x1155_607487750}

[Backup startup software images on chassis 1 slot 1:]{lang="EN-US"}

[  flash:/boot-a0201.bin]{lang="EN-US"}

[  flash:/system-a0201.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1007505}[显示设备下次启动时使用的备用软件包的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display install backup verbose]{lang="EN-US"}]{#struct_0_71526_x1155_607422214}

[Backup startup software images on slot 1:]{lang="EN-US"}

[ flash:/boot-a0201.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: H3C]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: boot]{lang="EN-US"}

[ Platform version: 7.1]{lang="EN-US"}

[ Product version: Beta 1330]{lang="EN-US"}

[ Supported board: mpu]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: boot]{lang="EN-US"}

[ Description: boot package]{lang="EN-US"}

[ ]{lang="EN-US"}

[ flash:/system-a0201.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: H3C]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: system]{lang="EN-US"}

[ Platform version: 7.1]{lang="EN-US"}

[ Product version: Beta 1330]{lang="EN-US"}

[ Supported board: mr, lc, sfc]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: system]{lang="EN-US"}

[ Description: system package]{lang="EN-US"}

[[本命令显示信息的描述请参见]{style="font-family:宋体"}]{#struct_0_71526_x1155_x353894278}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?2076033456#_Ref302142357)[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1836900194}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader file]{lang="EN-US"}**]{#struct_0_71526_x1155_284183312}[（基础配置命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[软件升级）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install committed]{lang="EN-US"}**]{#struct_0_71526_x1155_x602226252}
:::

::: {#811695277 .myid}
[]{#_Toc404782727}[]{#struct_0_71526_x1155_843438578}[]{#_Toc344717783}

**ISSU \-- ISSU配置命令 \-- display install committed**

------------------------------------------------------------------------

[**[display install committed]{lang="EN-US"}**]{#struct_0_71526_x1155_x1627658234}[命令用来显示设备下次启动时使用的主用软件包的相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_607356678}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1815686569}

[**[display install committed]{lang="EN-US"}**[ \[ **verbose** \]]{lang="EN-US"}]{#struct_0_71526_x1155_1406668166}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_x1622947718}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display install committed]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_1169704224}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x1003543079}[模式：]{style="font-family:宋体"}

[**[display install committed]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_382903467}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x853845781}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x981357554}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_607815430}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_1290267021}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_1599524232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x874632586}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_915860479}[：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_248410114}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_1756254292}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x1266688217}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x1597091105}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_71526_x1155_1058849416}*[cpu-number]{lang="EN-US"}*[：表示安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于显示安全引擎下次启动时使用的主用软件包的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_71526_x1155_x93762471}[：显示详细信息，包括软件包的名称、基本信息和所包含的组件。不指定该参数时，仅显示软件包的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_840372328}

[[在设备上执行]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**]{#struct_0_71526_x1155_607749894}[命令确认运行当前的软件包后，这些软件包会被列入主用下次启动软件包，以便设备重启后，这些软件包能够继续生效。]{style="font-family:宋体"}

[[执行]{style="font-family:宋体"}**[boot-loader file]{lang="EN-US"}**]{#struct_0_71526_x1155_315060778}[命令可以修改设备下次启动时使用的主用软件包列表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x749736820}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1532406324}[显示设备下次启动时使用的主用软件包的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display install committed]{lang="EN-US"}]{#struct_0_71526_x1155_644781665}

[Committed packages on slot 1:]{lang="EN-US"}

[ flash:/boot-a0201.bin]{lang="EN-US"}

[ flash:/system-a0201.bin]{lang="EN-US"}

[ flash:/feature.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x149656652}[显示设备下次启动时使用的主用软件包的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display install committed verbose]{lang="EN-US"}]{#struct_0_71526_x1155_607618822}

[Committed packages on slot 1:]{lang="EN-US"}

[ flash:/boot-a0201.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: H3C]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: boot]{lang="EN-US"}

[ Platform version: 7.1]{lang="EN-US"}

[ Product version: Beta 1330]{lang="EN-US"}

[ Supported board: mr, lc, sfc]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: boot]{lang="EN-US"}

[ Description: boot package]{lang="EN-US"}

[ ]{lang="EN-US"}

[ flash:/system-a0201.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: H3C]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: system]{lang="EN-US"}

[ Platform version: 7.1]{lang="EN-US"}

[ Product version: Beta 1330]{lang="EN-US"}

[ Supported board: mr, lc, sfc]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: system]{lang="EN-US"}

[ Description: system package]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/ssh-feature.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: H3C]{lang="EN-US"}

[ Product: xxxx]{lang="EN-US"}

[ Service name: ssh]{lang="EN-US"}

[ Platform version: 7.1]{lang="EN-US"}

[ Product version: Beta 1330]{lang="EN-US"}

[ Supported board: mr, lc, sfc]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: ssh]{lang="EN-US"}

[ Description: ssh package]{lang="EN-US"}

[[本命令显示信息的描述请参见]{style="font-family:宋体"}]{#struct_0_71526_x1155_720532039}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?2076033456#_Ref302142357)[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1323759092}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[boot-loader file]{lang="EN-US"}**]{#struct_0_71526_x1155_x1755002074}[（基础配置命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[软件升级）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install backup]{lang="EN-US"}**]{#struct_0_71526_x1155_x1748535968}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x318808642}
:::

::: {#-600703777 .myid}
[]{#_Toc404782728}[]{#struct_0_71526_x1155_1016756213}[]{#_Toc344717785}

**ISSU \-- ISSU配置命令 \-- display install inactive**

------------------------------------------------------------------------

[**[display install inactive]{lang="EN-US"}**]{#struct_0_71526_x1155_x1198461445}[命令用来显示存储介质根目录下、没有被激活的所有软件包的相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x593035605}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_608077574}

[**[display install inactive]{lang="EN-US"}**[ \[ **verbose** \]]{lang="EN-US"}]{#struct_0_71526_x1155_x349003799}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_x432563258}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display install inactive]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x721463532}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_87187243}[模式：]{style="font-family:宋体"}

[**[display install inactive]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_1724958874}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2116495467}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1499748288}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1404715342}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1876399468}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_608012038}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x337356396}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_2124609797}[：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_1009336589}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x213114176}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备和本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x307360453}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_1652597889}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/]{lang="EN-US"}[本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板和本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_71526_x1155_1058128520}*[cpu-number]{lang="EN-US"}*[：表示安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于显示安全引擎存储介质根目录下、没有被激活的所有软件包的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_71526_x1155_x71044858}[：显示详细信息，包括软件包的名称、基本信息和所包含的组件。不指定该参数时，仅显示软件包的名称。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_2038921084}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x855338322}[显示存储介质根目录下、没有被激活的所有软件包的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display install inactive]{lang="EN-US"}]{#struct_0_71526_x1155_x1765099706}

[Inactive packages on slot 1:]{lang="EN-US"}

[ flash:/ssh-feature.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_588791174}[显示存储介质根目录下、没有被激活的所有软件包的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display install inactive verbose]{lang="EN-US"}]{#struct_0_71526_x1155_x954869250}

[Inactive packages on slot 1:]{lang="EN-US"}

[flash:/ssh-feature.bin]{lang="EN-US"}

[ \[Package\]]{lang="EN-US"}

[ Vendor: H3C]{lang="EN-US"}

[ Product: XXXX]{lang="EN-US"}

[ Service name: ssh]{lang="EN-US"}

[ Platform version: 7.1]{lang="EN-US"}

[ Product version: Beta 1330]{lang="EN-US"}

[ Supported board: mr, lc, sfc]{lang="EN-US"}

[ \[Component\]]{lang="EN-US"}

[ Component: ssh]{lang="EN-US"}

[ Description: ssh package]{lang="EN-US"}

[[本命令显示信息的描述请参见]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1744231611}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?2076033456#_Ref302142357)[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2136371850}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install deactivate]{lang="EN-US"}**]{#struct_0_71526_x1155_x1333930445}
:::

::: {#665485774 .myid}
[]{#_Toc404782729}[]{#struct_0_71526_x1155_x1765165242}

**ISSU \-- ISSU配置命令 \-- display install ipe-info**

------------------------------------------------------------------------

[**[display install ipe-info]{lang="EN-US"}**]{#struct_0_71526_x1155_x1716500330}[命令用来显示]{style="font-family:
宋体"}[IPE]{lang="EN-US"}[文件包含的软件包列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1902171023}

[**[display install ipe-info]{lang="EN-US"}**[ *ipe-filename*]{lang="EN-US"}]{#struct_0_71526_x1155_x1558472604}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1487579602}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_666149935}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x638581472}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x2067632675}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_x1765230778}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x949235278}

[*[ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x2141474092}[：表示]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件名，以]{style="font-family:宋体"}[.ipe]{lang="EN-US"}[作为后缀名，从存储介质名开始为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串（包括存储介质名在内），不区分大小写。如果该]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件不存在，命令执行失败。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1262873648}

[[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x2059882343}[文件是一个或多个软件包的集合。用户获得该]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件后，可以选择其中的软件包进行升级。]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的]{style="font-family:宋体"}[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x1132011825}[文件必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的]{style="font-family:宋体"}[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x1880392126}[文件必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[或者]{style="font-family:宋体"}[slot*n*#flash:/xx.ipe]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为备用主控板所在的槽位号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的]{style="font-family:宋体"}[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_496501271}[文件必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[或者]{style="font-family:宋体"}[slot*n*#flash:/xx.ipe]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为从设备的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的]{style="font-family:宋体"}[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_184952832}[文件必须放在存储介质的根目录下，文件名中必须含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[或者]{style="font-family:宋体"}[chassis*m*#slot*n*#flash:/startup-boot.ipe]{lang="EN-US"}[，]{style="font-family:宋体"}[chassis*m*#slot*n*]{lang="EN-US"}[用于指定全局备用主控板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1765296314}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1984779340}[显示]{style="font-family:宋体"}[flash:/test.ipe]{lang="EN-US"}[的]{style="font-family:宋体"}[IPE]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display install ipe-info flash:/test.ipe]{lang="EN-US"}]{#struct_0_71526_x1155_x1764837562}

[Verifying the file flash:/test.ipe on the device\...\...\...\...\....Done.]{lang="EN-US"}

[H3C Device images in IPE:]{lang="EN-US"}

[  boot.bin]{lang="EN-US"}

[  system.bin]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1580502387}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install package]{lang="EN-US"}**]{#struct_0_71526_x1155_x1988260448}
:::

::: {#-580458775 .myid}
[]{#_Toc404782730}[]{#struct_0_71526_x1155_20137924}

**ISSU \-- ISSU配置命令 \-- display install job**

------------------------------------------------------------------------

[**[display install job]{lang="EN-US"}**]{#struct_0_71526_x1155_1009257426}[命令用来显示系统中正在执行的激活、卸载或回滚操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_461734395}

[**[display install job]{lang="EN-US"}**]{#struct_0_71526_x1155_1517130286}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1465844989}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1764903098}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_207921939}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_1349521114}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_1108457423}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x536706759}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1187251838}[显示系统中正在执行的激活、卸载、回滚三种]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[操作。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display install job]{lang="EN-US"}]{#struct_0_71526_x1155_643121458}

[ JobID:5]{lang="EN-US"}

[  Action:install activate flash:/ssh-feature.bin on the device]{lang="EN-US"}

[[以上显示信息表明：设备正在执行]{style="font-family:宋体"}**[install activate flash:/ssh-feature.bin]{lang="EN-US"}**]{#struct_0_71526_x1155_x160226064}[操作。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1764968634}[显示系统中正在执行的激活、卸载、回滚三种]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[操作。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display install job]{lang="EN-US"}]{#struct_0_71526_x1155_x799996833}

[ JobID:5]{lang="EN-US"}

[  Action:install activate flash:/ssh-feature.bin on slot 1]{lang="EN-US"}

[[以上显示信息表明：设备正在执行]{style="font-family:宋体"}**[install activate flash:/ssh-feature.bin slot 1]{lang="EN-US"}**]{#struct_0_71526_x1155_x1026879552}[操作。]{style="font-family:
宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_80266943}[显示系统中正在执行的激活、卸载、回滚三种]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[操作。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display install job]{lang="EN-US"}]{#struct_0_71526_x1155_x31960450}

[ JobID:5]{lang="EN-US"}

[  Action:install activate flash:/ssh-feature.bin on chassis 1 slot 1]{lang="EN-US"}

[[以上显示信息表明：设备正在执行]{style="font-family:宋体"}**[install activate flash:/ssh-feature.bin chassis 1 slot 1]{lang="EN-US"}**]{#struct_0_71526_x1155_1810539851}[操作。]{style="font-family:宋体"}
:::

::: {#-177174250 .myid}
[]{#_Toc404782731}[]{#struct_0_71526_x1155_1649030332}

**ISSU \-- ISSU配置命令 \-- display install log**

------------------------------------------------------------------------

[**[display install log]{lang="EN-US"}**]{#struct_0_71526_x1155_x1306770472}[命令用来显示与]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级相关的日志。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1765034170}

[**[display install log]{lang="EN-US"}**[ \[ *log-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_71526_x1155_x1132628344}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x926890969}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_1089274330}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_253512221}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1448152721}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_627851242}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1567358961}

[*[log-id]{lang="EN-US"}*]{#struct_0_71526_x1155_x1463636200}[：显示指定升级日志的信息。]{style="font-family:宋体"}*[log-id]{lang="EN-US"}*[表示升级日志的编号，不指定该参数时，则显示所有升级日志的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_71526_x1155_x1764575418}[：表示显示日志的详细信息。不指定该参数时，仅显示日志的摘要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1379837966}

[[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_1683847948}[日志记录了软件包历史操作信息，每当用户执行一次安装、升级、卸载、删除、取消或回滚操作时，都会自动产生一条日志信息，记录下该操作的过程，以及操作结果是成功还是失败。每条日志均分配一个全局唯一的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[设备最多可保存]{style="font-family:宋体"}[50]{lang="EN-US"}]{#struct_0_71526_x1155_x1630809026}[条]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[日志，超出该规格时新日志会覆盖最老的日志。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_138261255}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1965060619}[显示所有]{style="font-family:宋体"}[显示与软件包升级相关的日志。]{style="font-family:
宋体"}

[[\<Sysname\> display install log]{lang="EN-US"}]{#struct_0_71526_x1155_x1764640954}

[Install job 1 started by user root at 04/28/2001 08:39:29.]{lang="EN-US"}

[Job 1 completed successfully at 04/28/2001 08:39:30.]{lang="EN-US"}

[Install job 1 started by user root at 04/28/2001 08:39:29.]{lang="EN-US"}

[    Install activate flash:/ssh.bin on slot 1]{lang="EN-US"}

[Job 1 completed successfully at 04/28/2001 08:39:30.]{lang="EN-US"}

[Install job 1 started by user root at 04/28/2001 08:39:29.]{lang="EN-US"}

[Job 1 completed successfully at 04/28/2001 08:39:30.]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Install job 2 started by user root at 04/28/2001 08:40:29.]{lang="EN-US"}

[Job 2 completed successfully at 04/28/2001 08:40:30.]{lang="EN-US"}

[Install job 2 started by user root at 04/28/2001 08:40:29.]{lang="EN-US"}

[    Install activate flash:/route.bin on slot 1]{lang="EN-US"}

[Job 2 completed successfully at 04/28/2001 08:40:30.]{lang="EN-US"}

[Install job 2 started by user root at 04/28/2001 08:40:29.]{lang="EN-US"}

[Job 2 completed successfully at 04/28/2001 08:40:30.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1569196950}[显示系统中编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的软件包升级日志的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display install log 1 verbose]{lang="EN-US"}]{#struct_0_71526_x1155_1343096032}

[Install job 1 started by user root at 04/28/2001 08:39:29.]{lang="EN-US"}

[Job 1 completed successfully at 04/28/2001 08:39:30.]{lang="EN-US"}

[Install job 1 started by user root at 04/28/2001 08:39:29.]{lang="EN-US"}

[    Install activate flash:/ssh.bin on slot 1]{lang="EN-US"}

[Job 1 completed successfully at 04/28/2001 08:39:30.]{lang="EN-US"}

[Install job 1 started by user root at 04/28/2001 08:39:29.]{lang="EN-US"}

[Job 1 completed successfully at 04/28/2001 08:39:30.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Detail of activating packages on slot 1.]{lang="EN-US"}

[    Get upgrade policy successfully.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Detail of activating packages on slot 1.]{lang="EN-US"}

[    Uncompress package to system successfully.]{lang="EN-US"}

[    Remove files from system successfully.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[[display install log]{lang="EN-US"}]{.FigureDescriptionChar}]{#struct_0_71526_x1155_374048821}[[命令显示信息描述]{style="font-family:黑体"}]{.FigureDescriptionChar}[表]{style="font-family:黑体"}

[]{#table_struct_0_x1140193022}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1765099705}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2140092181}

[[Install job 1 started by user root at 04/28/2001 08:39:29.]{lang="EN-US"}]{#struct_0_71526_x1155_1569916047}

[[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_x1158967308}[动作的执行者和执行时间]{style="font-family:宋体"}

[[Job 1 completed successfully at 04/28/2001 08:39:30.]{lang="EN-US"}]{#struct_0_71526_x1155_1693353836}

[[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_407116633}[动作的完成时间]{style="font-family:宋体"}

[[Install activate flash:/ssh.bin on slot 1]{lang="EN-US"}]{#struct_0_71526_x1155_x1609306002}

[[执行的]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_1372119524}[动作]{style="font-family:宋体"}

[[Detail of activating packages on slot 1.]{lang="EN-US"}]{#struct_0_71526_x1155_x43222061}

[[激活包动作的详细信息]{style="font-family:宋体"}]{#struct_0_71526_x1155_68674032}

[[Get upgrade policy successfully]{lang="EN-US"}]{#struct_0_71526_x1155_x339177397}

[[表示升级决策处理成功]{style="font-family:宋体"}]{#struct_0_71526_x1155_754353208}

[[Uncompress package to system successfully]{lang="EN-US"}]{#struct_0_71526_x1155_x1717354354}

[[解压软件包文件到系统成功]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1743372357}

[[Remove files from system successfully]{lang="EN-US"}]{#struct_0_71526_x1155_x242100928}

[[从系统中删除文件成功]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1765165241}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1012383025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset install log-history oldest]{lang="EN-US"}**]{#struct_0_71526_x1155_1412474745}

::: {#-690534616 .myid}
[]{#_Toc404782732}[]{#struct_0_71526_x1155_730388233}

**ISSU \-- ISSU配置命令 \-- display install package**

------------------------------------------------------------------------

[**[display install package]{lang="EN-US"}**]{#struct_0_71526_x1155_544547379}[命令用来显示软件包的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_301776562}

[**[display install package]{lang="EN-US"}**[ { *filename* \| **all** } \[ **verbose** \]]{lang="EN-US"}]{#struct_0_71526_x1155_779442837}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_507943269}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1422848588}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1765230777}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1352519805}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_x1351184479}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1765518291}

[*[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x824452310}[：表示软件包的文件名，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x974919027}[：表示设备上存储介质根目录下的所有软件包。（集中式设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_1944971631}[：表示主用主控板上存储介质根目录下的所有软件包。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x1472874679}[：表示主设备上存储介质根目录下的所有软件包。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x856334584}[：表示全局主用主控板上存储介质根目录下的所有软件包。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_71526_x1155_x1765296313}[：显示软件包的基本信息和软件包所包含的组件。不指定该参数时，仅显示软件包的基本信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x387873655}

[[当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x634138418}[。（集中式设备）]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}]{#struct_0_71526_x1155_1706198758}[或者]{style="font-family:宋体"}[slot*n*#flash:/xx.bin]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为备用主控板所在的槽位号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x822753115}[或者]{style="font-family:宋体"}[slot*n*#flash:/xx.bin]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为从设备的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}]{#struct_0_71526_x1155_1868848973}[或]{style="font-family:宋体"}[chassis*m*#slot*n*#flash:/startup-boot.bin]{lang="EN-US"}[，]{style="font-family:宋体"}[chassis*m*#slot*n*]{lang="EN-US"}[用于指定全局备用主控板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x285495823}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1898607629}[显示软件包]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display install package flash:/system.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x1764837561}

[  flash:/system.bin]{lang="EN-US"}

[  \[Package\]]{lang="EN-US"}

[  Vendor: H3C]{lang="EN-US"}

[  Product: xxxx]{lang="EN-US"}

[  Service name: system]{lang="EN-US"}

[  Platform version: 7.1.022]{lang="EN-US"}

[  Product version: Beta 1330]{lang="EN-US"}

[  Supported board: mpu]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1177217860}[显示软件包]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display install package flash:/system.bin verbose]{lang="EN-US"}]{#struct_0_71526_x1155_x1764903097}

[  flash:/system.bin]{lang="EN-US"}

[  \[Package\]]{lang="EN-US"}

[  Vendor: H3C]{lang="EN-US"}

[  Product: xxxx]{lang="EN-US"}

[  Service name: system]{lang="EN-US"}

[  Platform version: 7.1.022]{lang="EN-US"}

[  Product version: Beta 1330]{lang="EN-US"}

[  Supported board: mpu]{lang="EN-US"}

[  \[Component\]]{lang="EN-US"}

[  Component: system]{lang="EN-US"}

[  Description: system package]{lang="EN-US"}

[[本命令显示信息的描述请参见]{style="font-family:宋体"}]{#struct_0_71526_x1155_967436826}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?2076033456#_Ref302142357)[。]{style="font-family:宋体"}
:::

::: {#-1476908894 .myid}
[]{#_Toc404782733}[]{#struct_0_71526_x1155_x709841317}

**ISSU \-- ISSU配置命令 \-- display install rollback**

------------------------------------------------------------------------

[**[display install rollback]{lang="EN-US"}**]{#struct_0_71526_x1155_1766352513}[命令用来显示回滚点的相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1269023453}

[**[display install rollback]{lang="EN-US"}**[ \[ *point-id* \]]{lang="EN-US"}]{#struct_0_71526_x1155_x1051017824}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1637519630}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_1686632849}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1764968633}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_1572656162}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_1218572384}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1490347180}

[*[point-id]{lang="EN-US"}*]{#struct_0_71526_x1155_x1766089938}[：回滚点的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x883249868}

[[可以通过这个命令查看回滚点信息，以便进行相应的回滚操作。]{style="font-family:宋体"}]{#struct_0_71526_x1155_97260549}

[[issu]{lang="EN-US"}]{#struct_0_71526_x1155_1260688968}[命令升级过程中不会记录回滚点，因此，在]{style="font-family:宋体"}[issu]{lang="EN-US"}[命令升级过程中执行该命令，没有信息可显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1962847585}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1807711193}[显示回滚点的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display install rollback]{lang="EN-US"}]{#struct_0_71526_x1155_x1765034169}

[Install rollback information 1 on slot 1:]{lang="EN-US"}

[  Updating from flash:/route-1.bin]{lang="EN-US"}

[         to flash:/route-2.bin.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Install rollback information 2 on slot 1:]{lang="EN-US"}

[   Deactivating flash:/route-2.bin]{lang="EN-US"}

[[以上显示信息表明：设备上共有两个回滚点，回滚点]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_71526_x1155_1239959115}[是将]{style="font-family:宋体"}[flash:/route-1.bin]{lang="EN-US"}[升级到了]{style="font-family:宋体"}[flash:/route-2.bin]{lang="EN-US"}[，回滚点]{style="font-family:宋体"}[2]{lang="EN-US"}[是将]{style="font-family:宋体"}[flash:/route-2.bin]{lang="EN-US"}[卸载了。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[display install rollback]{lang="EN-US"}]{#struct_0_71526_x1155_2091664434}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1138442550}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_1349459673}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_x867279678}

[[Install rollback information *n*]{lang="EN-US"}]{#struct_0_71526_x1155_1910960222}

[[回滚点信息，]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_71526_x1155_x1764575417}[为回滚点编号]{style="font-family:宋体"}

[[Updating from *A* to *B*]{lang="EN-US"}]{#struct_0_71526_x1155_620323079}

[[从软件包]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_71526_x1155_x1589377492}[升级到软件包]{style="font-family:宋体"}*[B]{lang="EN-US"}*[，]{style="font-family:宋体"}*[A]{lang="EN-US"}*[和]{style="font-family:宋体"}*[B]{lang="EN-US"}*[为软件包的名称]{style="font-family:宋体"}

[[Deactivating *A*]{lang="EN-US"}]{#struct_0_71526_x1155_590793384}

[[卸载软件包]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_71526_x1155_133340480}[，]{style="font-family:宋体"}*[A]{lang="EN-US"}*[为软件包的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1612333611}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install rollback]{lang="EN-US"}**]{#struct_0_71526_x1155_621389685}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset install rollback oldest]{lang="EN-US"}**]{#struct_0_71526_x1155_x1764640953}

::: {#1310287279 .myid}
[]{#_Toc404782734}[]{#struct_0_71526_x1155_x1165912423}[]{#_Toc304800158}[]{#_Toc304800159}[]{#_Toc304800160}[]{#_Toc304800161}[]{#_Toc304800162}[]{#_Toc304800163}[]{#_Toc304800164}[]{#_Toc304800165}[]{#_Toc304800166}[]{#_Toc304800167}[]{#_Toc304800168}[]{#_Toc304800169}[]{#_Toc304800170}

**ISSU \-- ISSU配置命令 \-- display install which**

------------------------------------------------------------------------

[**[display install which]{lang="EN-US"}**]{#struct_0_71526_x1155_x1154759208}[命令用来显示一个组件或文件的所属软件包，以及该软件包的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1994503588}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x948831679}

[**[display install which]{lang="EN-US"}**[ { **component** *name* \| **file** *filename* }]{lang="EN-US"}]{#struct_0_71526_x1155_x2129295766}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_1118969077}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display install which]{lang="EN-US"}**[ { **component** *name* \| **file** *filename* } \[ **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x426363842}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_2056871628}[模式：]{style="font-family:宋体"}

[**[display install which]{lang="EN-US"}**[ { **component** *name* \| **file** *filename* } \[ **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x1765099708}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_2107820948}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_26613349}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1728910871}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_1458582205}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_x259245256}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1850583771}

[**[component]{lang="EN-US"}***[ name]{lang="EN-US"}*]{#struct_0_71526_x1155_x1993488744}[：软件包所包含的组件的名称。]{style="font-family:宋体"}

[**[file]{lang="EN-US"}**[ *filename*]{lang="EN-US"}]{#struct_0_71526_x1155_x806808776}[：软件包所包含的文件的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。必须为纯文件名的形式。系统查询时，只有名称完全相同（除了大小写），才认为匹配成功。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x1765165244}[：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_1771897912}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_996673869}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备和本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_1254849286}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_492686500}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/]{lang="EN-US"}[本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板和本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_71526_x1155_1058980485}*[cpu-number]{lang="EN-US"}*[：表示安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于显示安全引擎上一个组件或文件属于哪个软件包以及该软件包的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_2117882958}

[[当软件包运行错误，系统提示]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_71526_x1155_147197547}[组件或者]{style="font-family:宋体"}[xx]{lang="EN-US"}[文件运行错误的时候，可以根据组件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件的名字使用该命令查找它属于哪个软件包，从而帮助进一步定位是否是软件包本身有缺陷。]{style="font-family:宋体"}

[[执行该命令后，系统会扫描指定]{style="font-family:宋体"}[slot]{lang="EN-US"}]{#struct_0_71526_x1155_x754544204}[存储介质的根目录下所有软件包，将包含该组件]{style="font-family:宋体"}[/]{lang="EN-US"}[文件的软件包都依次显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1670062077}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_659168835}[显示文件]{style="font-family:宋体"}[sshc.cli]{lang="EN-US"}[属于哪个软件包以及该软件包的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display install which file sshc.cli]{lang="EN-US"}]{#struct_0_71526_x1155_x1765230780}

[Verifying the file flash:/system.bin on the device\...Done.  ]{lang="EN-US"}

[Verifying the file flash:/boot.bin on the device\...Done.  ]{lang="EN-US"}

[File sshc.cli is in following packages on slot 1:]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  \[Package\]]{lang="EN-US"}

[  Vendor: xxx]{lang="EN-US"}

[  Product: xxxx]{lang="EN-US"}

[  Service name: ssh]{lang="EN-US"}

[  Platform version: 7.1.022]{lang="EN-US"}

[  Product version: Beta 1330]{lang="EN-US"}

[  Supported board: mr, lc, sfc]{lang="EN-US"}

[[本命令显示信息的描述请参见]{style="font-family:宋体"}]{#struct_0_71526_x1155_x593463670}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?2076033456#_Ref302142357)[。]{style="font-family:宋体"}
:::

::: {#2127206730 .myid}
[]{#_Toc404782735}[]{#struct_0_71526_x1155_372885594}[]{#_Toc329856486}[]{#_Toc315975335}

**ISSU \-- ISSU配置命令 \-- display issu rollback-timer**

------------------------------------------------------------------------

[**[display issu rollback-timer]{lang="EN-US"}**]{#struct_0_71526_x1155_x101987296}[命令用来显示回滚定时器的相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x9351263}

[**[display issu rollback-timer]{lang="EN-US"}**]{#struct_0_71526_x1155_x1716839779}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1566381861}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_1996603100}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1765296316}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1147388542}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_x1029046800}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x431046932}

[[因为新设置的回滚定时器时长会在下次]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_247396474}[升级中生效，因此，可能出现剩余时间大于定时器时长的情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1048312229}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1256301883}[执行]{style="font-family:宋体"}**[issu run switchover]{lang="EN-US"}**[命令后，显示回滚定时器的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display issu rollback-timer]{lang="EN-US"}]{#struct_0_71526_x1155_x1764837564}

[Rollback timer: Working]{lang="EN-US"}

[Rollback interval]{lang="EN-US"}[：]{style="font-family:宋体"}[45 minutes]{lang="EN-US"}

[Rollback time remaining : 40 minutes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_417702973}[执行]{style="font-family:宋体"}**[issu accept]{lang="EN-US"}**[命令后，显示回滚定时器的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display issu rollback-timer]{lang="EN-US"}]{#struct_0_71526_x1155_x985528688}

[Rollback timer: Not working]{lang="EN-US"}

[Rollback interval]{lang="EN-US"}[：]{style="font-family:宋体"}[30 minutes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_114663419}[当前没有进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级，显示回滚定时器的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display issu rollback-timer]{lang="EN-US"}]{#struct_0_71526_x1155_x504467153}

[Rollback timer: Not working]{lang="EN-US"}

[Rollback interval]{lang="EN-US"}[：]{style="font-family:宋体"}[45 minutes]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display issu rollback-timer]{lang="EN-US"}]{#struct_0_71526_x1155_1443385143}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1109465966}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_1992025636}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1764903100}

[[Rollback timer]{lang="EN-US"}]{#struct_0_71526_x1155_563693546}

[[回滚定时器是否处于工作状态：]{style="font-family:宋体"}]{#struct_0_71526_x1155_859814918}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Working]{lang="EN-US"}]{#struct_0_71526_x1155_x817014551}[：回滚定时器已经启动]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not working]{lang="EN-US"}]{#struct_0_71526_x1155_2069996576}[：回滚定时器没有启动或者已经超时]{lang="EN-US" style="font-family:宋体"}

[[Rollback interval]{lang="EN-US"}]{#struct_0_71526_x1155_1158611357}

[[用户配置的回滚定时器的时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_71526_x1155_606908463}

[[Rollback time remaining]{lang="EN-US"}]{#struct_0_71526_x1155_x1764968636}

[[距离回滚定时器超时的时间，单位为分钟]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1962796247}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1614027725}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu rollback-timer]{lang="EN-US"}**]{#struct_0_71526_x1155_1195742121}

::: {#1316911812 .myid}
[]{#_Toc404782736}[]{#struct_0_71526_x1155_912486168}[]{#_Toc329856488}[]{#_Toc251161054}[]{#_Toc304800173}[]{#_Toc304813443}

**ISSU \-- ISSU配置命令 \-- display issu state**

------------------------------------------------------------------------

[**[display issu state]{lang="EN-US"}**]{#struct_0_71526_x1155_x1693202685}[命令用来显示当前]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级所处的状态，以及]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_171059243}

[**[display issu state]{lang="EN-US"}**]{#struct_0_71526_x1155_x1794958516}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1765034172}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_1999539538}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x397721962}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_1004908971}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_1155581854}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1323347920}

[**[issu]{lang="EN-US"}**]{#struct_0_71526_x1155_1873198954}[命令升级需要经过一系列的操作步骤，升级过程中有严格的步骤要求，执行升级步骤会导致]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[状态的变化，通过该命令的显示信息可以帮助管理员确定下一步需执行的操作。]{style="font-family:宋体"}

[[该命令不能显示]{style="font-family:宋体"}**[install]{lang="EN-US"}**]{#struct_0_71526_x1155_664165997}[命令升级过程中设备所处的状态，因为]{style="font-family:宋体"}**[install]{lang="EN-US"}**[命令升级过程没有用到状态机。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1552912405}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1967768909}[当前设备没有]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级，显示]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[状态。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display issu state]{lang="EN-US"}]{#struct_0_71526_x1155_x1764640956}

[ISSU state: Init]{lang="EN-US"}

[Compatibility: Unknown]{lang="EN-US"}

[Work state: Normal]{lang="EN-US"}

[Current version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2402]{lang="EN-US"}

[  system: 7.1.041, Demo 2402]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2402]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/ssh.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x406397536}[当前设备没有]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级，显示]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[状态。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备）]{style="font-family:宋体"}

[[\<Sysname\> display issu state]{lang="EN-US"}]{#struct_0_71526_x1155_x1765099707}

[ISSU state: Init]{lang="EN-US"}

[Compatibility: Unknown]{lang="EN-US"}

[Work state: Normal]{lang="EN-US"}

[Upgrade method: Card by card]{lang="EN-US"}

[Upgraded slot: None]{lang="EN-US"}

[Current upgrading slot: None]{lang="EN-US"}

[Current version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2402]{lang="EN-US"}

[  system: 7.1.041, Demo 2402]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2402]{lang="EN-US"}

[Current software images:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/ssh.bin]{lang="EN-US"}

[[\# **issu load**]{lang="EN-US"}]{#struct_0_71526_x1155_x977292767}[命令执行过程中，显示]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[状态。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display issu state]{lang="EN-US"}]{#struct_0_71526_x1155_x1765296315}

[ISSU state: Loading]{lang="EN-US"}

[Compatibility: Incompatible]{lang="EN-US"}

[Work state: Normal]{lang="EN-US"}

[Previous version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2402]{lang="EN-US"}

[  system: 7.1.041, Demo 2402]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2402]{lang="EN-US"}

[Previous software images:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/ssh.bin]{lang="EN-US"}

[Upgrade version list:]{lang="EN-US"}

[  boot: 7.1.042, Demo 2403]{lang="EN-US"}

[  system: 7.1.042, Demo 2403]{lang="EN-US"}

[  ssh: 7.1.042, Demo 2403]{lang="EN-US"}

[Upgrade software images]{lang="EN-US"}[：]{style="font-family:宋体"}

[  flash:/boot02.bin]{lang="EN-US"}

[  flash:/system04.bin]{lang="EN-US"}

[  flash:/ssh04.bin]{lang="EN-US"}

[[\# **issu load**]{lang="EN-US"}]{#struct_0_71526_x1155_418695399}[命令执行过程中，显示]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[状态。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display issu state]{lang="EN-US"}]{#struct_0_71526_x1155_x1764968635}

[ISSU state: Loading]{lang="EN-US"}

[Compatibility: Incompatible]{lang="EN-US"}

[Work state: Normal]{lang="EN-US"}

[Upgrade method: Card by card]{lang="EN-US"}

[Upgraded slot: None]{lang="EN-US"}

[Current upgrading slot:]{lang="EN-US"}

[  slot 1]{lang="EN-US"}

[Previous version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2402]{lang="EN-US"}

[  system: 7.1.041, Demo 2402]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2402]{lang="EN-US"}

[Previous software images:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/ssh.bin]{lang="EN-US"}

[Upgrade version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2403]{lang="EN-US"}

[  system: 7.1.041, Demo 2403]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2403]{lang="EN-US"}

[Upgrade software images]{lang="EN-US"}[：]{style="font-family:宋体"}

[  flash:/boot02.bin]{lang="EN-US"}

[  flash:/system04.bin]{lang="EN-US"}

[  flash:/ssh04.bin]{lang="EN-US"}

[[\# **issu load**]{lang="EN-US"}]{#struct_0_71526_x1155_766087108}[命令执行过程中，显示]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备）]{style="font-family:宋体"}

[[\<Sysname\> display issu state]{lang="EN-US"}]{#struct_0_71526_x1155_x1765099710}

[ISSU state: Loading]{lang="EN-US"}

[Compatibility: Incompatible]{lang="EN-US"}

[Work state: Normal]{lang="EN-US"}

[Upgrade method: Card by card]{lang="EN-US"}

[Upgraded slot: None]{lang="EN-US"}

[Current upgrading slot:]{lang="EN-US"}

[  chassis 1 slot 1]{lang="EN-US"}

[Previous version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2402]{lang="EN-US"}

[  system: 7.1.041, Demo 2402]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2402]{lang="EN-US"}

[Previous software images:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/ssh.bin]{lang="EN-US"}

[Upgrade version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2403]{lang="EN-US"}

[  system: 7.1.041, Demo 2403]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2403]{lang="EN-US"}

[Upgrade software images]{lang="EN-US"}[：]{style="font-family:宋体"}

[  flash:/boot02.bin]{lang="EN-US"}

[  flash:/system04.bin]{lang="EN-US"}

[  flash:/ssh04.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1751656124}[执行]{style="font-family:宋体"}**[issu load]{lang="EN-US"}**[命令后，在全局主用主控板上显示]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备）]{style="font-family:宋体"}

[[\<Sysname\> display issu state]{lang="EN-US"}]{#struct_0_71526_x1155_x1765296318}

[ISSU state: Loaded]{lang="EN-US"}

[Compatibility: Compatible]{lang="EN-US"}

[Work state: Normal]{lang="EN-US"}

[Upgrade method: Card by card]{lang="EN-US"}

[Upgraded slot:]{lang="EN-US"}

[  chassis 1 slot 1]{lang="EN-US"}

[Current upgrading slot: None]{lang="EN-US"}

[Previous version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2402]{lang="EN-US"}

[  system: 7.1.041, Demo 2402]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2402]{lang="EN-US"}

[Previous software images:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/ssh.bin]{lang="EN-US"}

[Upgrade version list:]{lang="EN-US"}

[  system: 7.1.041, Demo 2403]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2403]{lang="EN-US"}

[Upgrade software images:]{lang="EN-US"}

[  flash:/system02.bin]{lang="EN-US"}

[  flash:/ssh02.bin]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_371641232}[执行]{style="font-family:宋体"}**[issu load]{lang="EN-US"}**[命令后，在原主设备上显示]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[状态。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式多成员设备）]{style="font-family:宋体"}

[[\<Sysname\> display issu state]{lang="EN-US"}]{#struct_0_71526_x1155_x1765034174}

[ISSU state: Loaded]{lang="EN-US"}

[Compatibility: Incompatible]{lang="EN-US"}

[Work state: Independent active]{lang="EN-US"}

[Upgrade method: Chassis by chassis]{lang="EN-US"}

[Upgraded chassis:]{lang="EN-US"}

[  chassis 2]{lang="EN-US"}

[Current upgrading chassis: None]{lang="EN-US"}

[Previous version list:]{lang="EN-US"}

[  boot: 7.1.041, Demo 2402]{lang="EN-US"}

[  system: 7.1.041, Demo 2402]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2402]{lang="EN-US"}

[Previous software images:]{lang="EN-US"}

[  flash:/boot.bin]{lang="EN-US"}

[  flash:/system.bin]{lang="EN-US"}

[  flash:/ssh.bin]{lang="EN-US"}

[Upgrade version list:]{lang="EN-US"}

[  system: 7.1.041, Demo 2403]{lang="EN-US"}

[  ssh: 7.1.041, Demo 2403]{lang="EN-US"}

[Upgrade software images:]{lang="EN-US"}

[  flash:/system04.bin]{lang="EN-US"}

[  flash:/ssh04.bin]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display issu state]{lang="EN-US"}]{#struct_0_71526_x1155_836740124}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1107577166}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2109152888}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_2102477172}

[[ISSU state]{lang="EN-US"}]{#struct_0_71526_x1155_x1764575422}

[[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_x138995200}[升级状态，取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_71526_x1155_502307825}[：表示还没有开始]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级或者]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级已经完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loading]{lang="EN-US"}]{#struct_0_71526_x1155_183945135}[：表示正在执行]{lang="EN-US" style="font-family:宋体"}**[issu load]{lang="EN-US"}**[操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loaded]{lang="EN-US"}]{#struct_0_71526_x1155_x1531469833}[：表示]{lang="EN-US" style="font-family:宋体"}**[issu load]{lang="EN-US"}**[操作完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Switching]{lang="EN-US"}]{#struct_0_71526_x1155_235729406}[：表示正在执行]{lang="EN-US" style="font-family:宋体"}**[issu run switchover]{lang="EN-US"}**[操作]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Switchover]{lang="EN-US"}]{#struct_0_71526_x1155_x919517732}[：表示]{lang="EN-US" style="font-family:宋体"}**[issu run switchove]{lang="EN-US"}**[r]{lang="EN-US"}[操作完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Accepted]{lang="EN-US"}]{#struct_0_71526_x1155_x1764640958}[：表示]{lang="EN-US" style="font-family:宋体"}**[issu accept]{lang="EN-US"}**[操作完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Committing]{lang="EN-US"}]{#struct_0_71526_x1155_756401878}[：表示正在执行]{lang="EN-US" style="font-family:宋体"}**[issu commit]{lang="EN-US"}**[操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Rollbacking]{lang="EN-US"}]{#struct_0_71526_x1155_1007326581}[：表示系统正在回滚中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_x903017157}[：在非原主用主控板上查看，表示设备正在升级过程中]{style="font-family:宋体"}

[[Compatibility]{lang="EN-US"}]{#struct_0_71526_x1155_x1947578806}

[[版本兼容性检查结果，取值可能为：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1765099709}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Compatible]{lang="EN-US"}]{#struct_0_71526_x1155_541737007}[：表示兼容升级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incompatible]{lang="EN-US"}]{#struct_0_71526_x1155_2063725643}[：表示]{lang="EN-US" style="font-family:宋体"}[不兼容升级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_796954167}[：没有升级]{lang="EN-US" style="font-family:宋体"}

[[Work state]{lang="EN-US"}]{#struct_0_71526_x1155_x875254203}

[[设备的工作模式，取值可能为：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1765165245}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_71526_x1155_x956985443}[：表示正常模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Independent active]{lang="EN-US"}]{#struct_0_71526_x1155_1305258979}[：表示独立主控模式。当升级到不兼容版本时，先升级的备用主控板就会进入独立主控模式。该模式使得同一设备上的不同主控板可以运行不同的软件版本]{lang="EN-US" style="font-family:
  宋体"}

[[Upgrade method]{lang="EN-US"}]{#struct_0_71526_x1155_1206503685}

[[升级方式，取值可能为：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1466519884}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Card by card]{lang="EN-US"}]{#struct_0_71526_x1155_x1765230781}[：表示以主控板为单位进行升级，升级完一块主控板再升级另一块主控板]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Chassis by chassis]{lang="EN-US"}]{#struct_0_71526_x1155_2135419685}[：在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中多成员设备运行的情况下，表示以成员设备为单位进行升级，先升级备设备，再升级原主设备（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Upgraded slot]{lang="EN-US"}]{#struct_0_71526_x1155_354171219}

[[完成升级的单板。取值为]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_x33140169}[时，表示设备处于回滚过程中（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[Current upgrading slot]{lang="EN-US"}]{#struct_0_71526_x1155_x1765296317}

[[正在升级的单板。取值为]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_1581494813}[时，表示设备处于回滚过程中（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[Upgraded chassis]{lang="EN-US"}]{#struct_0_71526_x1155_x1222686374}

[[完成升级的成员设备。取值为]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_243014160}[时，表示设备处于回滚过程中（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Current upgrading chassis]{lang="EN-US"}]{#struct_0_71526_x1155_615289758}

[[正在升级的成员设备。取值为]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_x1764837565}[时，表示设备处于回滚过程中（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备）]{style="font-family:宋体"}

[[Current version list]{lang="EN-US"}]{#struct_0_71526_x1155_x1148380968}

[[设备没有升级，表示当前系统软件版本]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1293729095}

[[Current software images]{lang="EN-US"}]{#struct_0_71526_x1155_658840239}

[[设备没有升级，表示当前运行软件包的名称]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1764903101}

[[Previous version list]{lang="EN-US"}]{#struct_0_71526_x1155_2129777487}

[[进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_1938141853}[升级前的系统软件版本]{style="font-family:宋体"}

[[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_957128806}[：不兼容升级的时候，在非原主用主控板上查看，表示设备正在升级过程中]{style="font-family:宋体"}

[[Previous software images]{lang="EN-US"}]{#struct_0_71526_x1155_x1764968637}

[[进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_x396712306}[升级前版本文件]{style="font-family:宋体"}

[[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_1020017938}[：不兼容升级的时候，在非原主用主控板上查看，表示设备正在升级过程中]{style="font-family:宋体"}

[[Upgrade version list]{lang="EN-US"}]{#struct_0_71526_x1155_x1765034173}

[[正在]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_433455597}[升级的目标版本]{style="font-family:宋体"}

[[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_712358201}[：不兼容升级的时候，在非原主用主控板上查看，表示设备正在升级过程中]{style="font-family:宋体"}

[[Upgrade software images]{lang="EN-US"}]{#struct_0_71526_x1155_1156580078}

[[正在]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_x1764575421}[升级中用到的目标文件]{style="font-family:宋体"}

[[Unknown]{lang="EN-US"}]{#struct_0_71526_x1155_x542279727}[：不兼容升级的时候，在非原主用主控板上查看，表示设备正在升级过程中]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x584439268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu accept]{lang="EN-US"}**]{#struct_0_71526_x1155_x257092430}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x308344720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x265632913}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu rollback]{lang="EN-US"}**]{#struct_0_71526_x1155_1376651963}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_x1764640957}

::: {#-937301353 .myid}
[]{#_Toc404782737}[]{#struct_0_71526_x1155_1159686405}[]{#_Toc329856487}[]{#_Toc344717795}[]{#_Toc299981181}[]{#_Toc299981182}[]{#_Toc299981183}

**ISSU \-- ISSU配置命令 \-- display version comp-matrix**

------------------------------------------------------------------------

[**[display version comp-matrix]{lang="EN-US"}**]{#struct_0_71526_x1155_x2100532947}[命令用来显示软件版本兼容信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1731209643}

[**[display version comp-matrix]{lang="EN-US"}**]{#struct_0_71526_x1155_x2132589155}

[**[display version comp-matrix file ]{lang="EN-US"}**[{ **boot** ]{lang="EN-US"}*[filename]{lang="EN-US"}[ ]{lang="EN-US"}*[\| **system** ]{lang="EN-US"}*[filename]{lang="EN-US"}[ ]{lang="EN-US"}*[\| **feature** ]{lang="EN-US"}*[filename]{lang="EN-US"}*[&\<1-30\> } **\***]{lang="EN-US"}]{#struct_0_71526_x1155_584485010}

[**[display version comp-matrix file ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x2038746774}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1522569580}

[[任意视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x678146889}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x199015765}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x2137029872}

[[network-operator]{lang="EN-US"}]{#struct_0_71526_x1155_x1528135527}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_239772587}

[**[boot]{lang="EN-US"}**]{#struct_0_71526_x1155_1371187683}[：表示]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**]{#struct_0_71526_x1155_703101927}[：表示]{style="font-family:宋体"}[System]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**]{#struct_0_71526_x1155_x731108397}[：表示]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x977959202}[：表示软件包的文件名，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}[&\<1-30\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[ipe]{lang="EN-US"}***[ ]{lang="EN-US"}[ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x1687295631}[：]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件名，以]{style="font-family:宋体"}[.ipe]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x199081301}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}]{#struct_0_71526_x1155_585937062}[/IPE]{lang="EN-US"}[文件必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}[（集中式设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1810230222}[/IPE]{lang="EN-US"}[文件必须放在主用主控板存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[slot]{lang="EN-US"}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}]{#struct_0_71526_x1155_844748500}[/IPE]{lang="EN-US"}[文件必须放在主设备存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[slot]{lang="EN-US"}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}]{#struct_0_71526_x1155_574619434}[/IPE]{lang="EN-US"}[文件必须放在全局主用主控板存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[chassis]{lang="EN-US"}[和]{style="font-family:宋体"}[slot]{lang="EN-US"}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}[（分布式设备－]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定文件名，则显示指定软件包的兼容性信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式；如果不指定文件名，则显示设备当前运行版本的兼容性信息。（不支持]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1528962484}[IRF3/]{lang="EN-US"}[安全引擎的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能显示父设备的软件包之间的兼容性，以及]{style="font-family:宋体"}]{#struct_0_71526_x1155_x482845072}[PEX]{lang="EN-US"}[设备的软件包之间的兼容性，不能判断父设备和]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的软件包是否兼容。请通过软件版本说明书来判断父设备和]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的软件包是否兼容。（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能显示设备的软件包之间的兼容性，以及安全引擎的软件包之间的兼容性，不能判断设备和安全引擎的软件包是否兼容。请通过软件版本说明书来判断设备和安全引擎的软件包是否兼容。（支持安全引擎的设备）]{style="font-family:宋体"}]{#struct_0_71526_x1155_1058914950}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1535865742}[IRF3]{lang="EN-US"}[组网环境，本设备下挂]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的情况下，使用该命令，如果不指定文件名，则分别显示父设备以及]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备当前运行版本的兼容性信息。（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备中安装了防火墙插卡，使用该命令，如果不指定文件名，则分别显示设备以及安全引擎当前运行版本的兼容性信息。（支持安全引擎的设备）]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1159310973}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_71526_x1155_x482845071}[IRF3]{lang="EN-US"}[组网环境下，要显示]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备升级软件包的兼容信息时，请先使用]{style="font-family:宋体"}**[issu pex]{lang="EN-US"}**[命令指定]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包，再使用该命令，并且]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[指定为父设备上的升级软件包。此时，会显示父设备上该软件包的兼容性信息，]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备上]{style="font-family:宋体"}**[issu pex]{lang="EN-US"}**[命令指定软件包的兼容性信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。只要父设备上有一个软件包不兼容，或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备上有一个软件包不兼容，均判定为不兼容升级方式，需要重启整个]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[系统。（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[要显示安全引擎升级软件包的兼容信息时，请先使用]{style="font-family:宋体"}]{#struct_0_71526_x1155_1058980486}**[issu blade]{lang="EN-US"}**[命令指定安全引擎的升级软件包，再使用该命令，并且]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[指定为设备上的升级软件包。此时，会显示设备上该软件包的兼容性信息，安全引擎上]{style="font-family:宋体"}**[issu blade]{lang="EN-US"}**[命令指定软件包的兼容性信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。只要设备上有一个软件包不兼容，或者安全引擎上有一个软件包不兼容，均判定为不兼容升级方式，需要重启整个系统。（支持安全引擎的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1018741452}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x199146837}[显示设备当前正在使用的软件包的兼容信息。]{style="font-family:宋体"}

[[\<Sysname\> display version comp-matrix]{lang="EN-US"}]{#struct_0_71526_x1155_x198753621}

[Boot image: flash:/cmw710-boot-a7122.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  7.1.031]{lang="EN-US"}

[ ]{lang="EN-US"}

[System image: flash:/cmw710-system-a7122.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  V700R001B31D001]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  V700R001B31D001]{lang="EN-US"}

[  Version dependency boot list:]{lang="EN-US"}

[  7.1.031]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature image: flash:/cmw710-cfa-a7124.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  V700R001B31D003]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  V700R001B31D003]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  V700R001B31D001]{lang="EN-US"}

[  V700R001B31D002]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x549402503}[显示文件]{style="font-family:宋体"}[flash:/boot-e2205.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/system-e2205.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/dhcp-e2205.re.bin]{lang="EN-US"}[和当前运行软件包的兼容信息。（不兼容版本显示信息举例）（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display version comp-matrix file boot flash:/boot-e2205.bin system flash:/system-e2205.bin feature flash:/dhcp-e2205.re.bin]{lang="EN-US"}]{#struct_0_71526_x1155_608839703}

[Verifying the file flash:/dhcp-e2205.re.bin on the device\.....Done.]{lang="EN-US"}

[Verifying the file flash:/boot-e2205.bin on the device\.....Done.]{lang="EN-US"}

[Verifying the file flash:/system-e2205.bin on the device\.....Done.]{lang="EN-US"}

[Boot image: flash:/boot-e2205.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  7.1.035]{lang="EN-US"}

[ ]{lang="EN-US"}

[System image: flash:/system-e2205.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  V200R001B02D012]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  V200R001B02D012]{lang="EN-US"}

[  Version dependency boot list:]{lang="EN-US"}

[  7.1.035]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature image: flash:/dhcp-e2205.re.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  V200R001B02D012]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  V200R001B02D012]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  V200R001B02D012]{lang="EN-US"}

[  V200R001B02D014]{lang="EN-US"}

[Incompatible upgrade.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x198819157}[显示文件]{style="font-family:宋体"}[flash:/boot-e2205.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/system-e2205.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/dhcp-e2205.incom.bin]{lang="EN-US"}[和当前运行软件包的兼容信息。（兼容版本显示信息举例）（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display version comp-matrix file boot flash:/boot-e2205.bin system flash:/system-e2205.bin feature flash:/dhcp-e2205.incom.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x543093455}

[Verifying the file flash:/dhcp-e2205.incom.bin on slot 2\.....Done.]{lang="EN-US"}

[Verifying the file flash:/boot-e2205.bin on slot 2\.....Done.]{lang="EN-US"}

[Verifying the file flash:/system-e2205.bin on slot 2\.....Done.]{lang="EN-US"}

[Boot image: flash:/boot-e2205.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  7.1.035]{lang="EN-US"}

[ ]{lang="EN-US"}

[System image: flash:/system-e2205.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  V200R001B02D012]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  V200R001B02D012]{lang="EN-US"}

[  Version dependency boot list:]{lang="EN-US"}

[  7.1.035]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature image: flash:/dhcp-e2205.incom.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  V200R001B02D014]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  V200R001B02D014]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  V200R001B02D012]{lang="EN-US"}

[  V200R001B02D014]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot     Upgrade Way]{lang="EN-US"}

[  2        File Upgrade]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1755290571}[查看当前软件版本和]{style="font-family:宋体"}[cmw710-cfa-a7125.bin]{lang="EN-US"}[软件版本的兼容性信息。（兼容版本显示信息举例）（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display version comp-matrix file feature flash:/cmw710-cfa-a7125.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x199015764}

[Verifying the file flash:/cmw710-cfa-a7125.bin on slot 0\.....Done.]{lang="EN-US"}

[Feature image: flash:/cmw710-cfa-a7125.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  V700R001B31D002]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  V700R001B31D001]{lang="EN-US"}

[  V700R001B31D002]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  V700R001B31D001]{lang="EN-US"}

[  V700R001B31D002]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  0                           Service Upgrade]{lang="EN-US"}

[  1                           Service Upgrade]{lang="EN-US"}

[  1.1                         Service Upgrade]{lang="EN-US"}

[  4                           Service Upgrade]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 0:]{lang="EN-US"}

[flash:/cmw710-cfa-a7125.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 4:]{lang="EN-US"}

[flash:/cmw710-cfa-a7125.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 1:]{lang="EN-US"}

[flash:/cmw710-cfa-a7125.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 1.1:]{lang="EN-US"}

[flash:/cmw710-cfa-a7125.bin]{lang="EN-US"}

[CFA]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x2136964336}[查看当前软件版本和]{style="font-family:宋体"}[cmw710-cfa-a7122.bin]{lang="EN-US"}[软件版本的兼容性信息。（兼容版本显示信息举例）（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display version comp-matrix file feature flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x198557012}

[Verifying the file flash:/cmw710-cfa-a7122.bin on chassis 1 slot 0\.....Done.]{lang="EN-US"}

[Feature image: flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  V700R001B31D002]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  V700R001B31D001]{lang="EN-US"}

[  V700R001B31D002]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  V700R001B31D001]{lang="EN-US"}

[  V700R001B31D002]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         0                 Service Upgrade]{lang="EN-US"}

[  1         0.1               Service Upgrade]{lang="EN-US"}

[  1         7                 Service Upgrade]{lang="EN-US"}

[  1         9                 Service Upgrade]{lang="EN-US"}

[  2         0                 Service Upgrade]{lang="EN-US"}

[  2         0.1               Service Upgrade]{lang="EN-US"}

[  2         1                 Service Upgrade]{lang="EN-US"}

[  2         6                 Service Upgrade]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 1 slot 0:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 1 slot 7:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 1 slot 9:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 1 slot 0.1:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 2 slot 0:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 2 slot 1:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 2 slot 6:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 2 slot 0.1:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x482845076}[显示父设备和]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备当前正在使用的软件包的兼容信息。]{style="font-family:宋体"}

[[\<Sysname\> display version comp-matrix]{lang="EN-US"}]{#struct_0_71526_x1155_x482845075}

[Boot image: flash:/s5820v2_5830v2-cmw710-boot-d2404001.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  7.1.046]{lang="EN-US"}

[ ]{lang="EN-US"}

[System image: flash:/s5820v2_5830v2-cmw710-system-d2404001.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2404001]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2404001]{lang="EN-US"}

[  Version dependency boot list:]{lang="EN-US"}

[  7.1.046]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature image: flash:/s5820v2_5830v2-cmw710-devkit-d2404001-b01-base.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2404001]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2402003]{lang="EN-US"}

[  D2404001]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  D2404001]{lang="EN-US"}

[ ]{lang="EN-US"}

[Compatible info of S5120HI:]{lang="EN-US"}

[Boot image: flash:/rpu-s5120hi-boot.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  7.1.041]{lang="EN-US"}

[ ]{lang="EN-US"}

[System image: flash:/rpu-s5120hi-system.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  T2206]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  T2206]{lang="EN-US"}

[  Version dependency boot list:]{lang="EN-US"}

[  7.1.041]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature image: flash:/rpu-s5120hi-devkit-b46-b01-base.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  T2206]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  T2206]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  T2206]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1535538062}[显示父设备文件]{style="font-family:宋体"}[flash:/boot-d2404.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/system-d2404.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/http-d2404.bin]{lang="EN-US"}[的兼容信息，]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备（设备型号]{style="font-family:宋体"}[S5120HI]{lang="EN-US"}[）文件]{style="font-family:宋体"}[flash:/s5120hi-boot-d2404.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/s5120hi-system-d2404.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/s5120hi-http-d2404.bin]{lang="EN-US"}[的兼容信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。（不兼容版本显示信息举例）（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file boot flash:/s5120hi-boot-d2404.bin system flash:/s5120hi-system-d2404.bin feature flash:/s5120hi-http-d2404.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x482845078}

[Verifying the file flash:/s5120hi-http-d2404.bin on slot 1\...Done.]{lang="EN-US"}

[Verifying the file flash:/s5120hi-boot-d2404.bin on slot 1\...Done.]{lang="EN-US"}

[Verifying the file flash:/s5120hi-system-d2404.bin on slot 1\...Done.]{lang="EN-US"}

[\<Sysname\> display version comp-matrix file boot flash:/boot-d2404.bin system flash:/system-d2404.bin feature flash:/http-d2404.bin]{lang="EN-US"}

[Verifying the file flash:/http-d2404.bin on slot 1\.....Done.]{lang="EN-US"}

[Verifying the file flash:/boot-d2404.bin on slot 1\.....Done.]{lang="EN-US"}

[Verifying the file flash:/system-d2404.bin on slot 1\.....Done.]{lang="EN-US"}

[Verifying the file flash:/s5120hi-boot-d2404.bin on slot 1\...Done.]{lang="EN-US"}

[Verifying the file flash:/s5120hi-system-d2404.bin on slot 1\...Done.]{lang="EN-US"}

[Verifying the file flash:/s5120hi-http-d2404.bin on slot 1\...Done.]{lang="EN-US"}

[Boot image: flash:/boot-d2404.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  7.1.041]{lang="EN-US"}

[ ]{lang="EN-US"}

[System image: flash:/system-d2404.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[  Version dependency boot list:]{lang="EN-US"}

[  7.1.041]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature image: flash:/http-d2404.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[ ]{lang="EN-US"}

[Compatible info of S5120HI:]{lang="EN-US"}

[Boot image: flash:/rpu-s5120hi-boot-d2404.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  7.1.041]{lang="EN-US"}

[ ]{lang="EN-US"}

[System image: flash:/rpu-s5120hi-system-d2404.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[  Version dependency boot list:]{lang="EN-US"}

[  7.1.041]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature image: flash:/s5120hi-http-d2404.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2404]{lang="EN-US"}

[Incompatible upgrade.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1536258958}[显示父设备文件]{style="font-family:宋体"}[flash:/boot-d2403.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/system-d2403.bin]{lang="EN-US"}[、]{style="font-family:宋体"}[flash:/http-d2403.bin]{lang="EN-US"}[的兼容信息，]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备（设备型号]{style="font-family:宋体"}[S5120HI]{lang="EN-US"}[）文件]{style="font-family:宋体"}[flash:/s5120hi-http-d2403.bin]{lang="EN-US"}[的兼容信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。（兼容版本显示信息举例）（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file feature flash:/s5120hi-http-d2403.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x482845077}

[Verifying the file flash:/s5120hi-http-d2403.bin on slot 1\.....Done.]{lang="EN-US"}

[\<Sysname\> display version comp-matrix file boot flash:/boot-d2403.bin system flash:/system-d2403.bin feature flash:/http-d2403.bin]{lang="EN-US"}

[Verifying the file flash:/http-d2403.bin on slot 1\.....Done.]{lang="EN-US"}

[Verifying the file flash:/boot-d2403.bin on slot 1\.....Done.]{lang="EN-US"}

[Verifying the file flash:/system-d2403.bin on slot 1\.....Done.]{lang="EN-US"}

[Verifying the file flash:/s5120hi-http-d2403.bin on slot 1\.....Done.]{lang="EN-US"}

[Boot image: flash:/boot-d2403.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  7.1.041]{lang="EN-US"}

[ ]{lang="EN-US"}

[System image: flash:/system-d2403.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version dependency boot list:]{lang="EN-US"}

[  7.1.041]{lang="EN-US"}

[ ]{lang="EN-US"}

[Feature image: flash:/http-d2403.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[ ]{lang="EN-US"}

[Compatible info of S5120HI:]{lang="EN-US"}

[Feature image: flash:/s5120hi-http-d2403.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot     Upgrade Way]{lang="EN-US"}

[  1        File Upgrade]{lang="EN-US"}

[  102      File Upgrade]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1535669134}[查看父设备文件]{style="font-family:宋体"}[cmw710-cfa-a0042.bin]{lang="EN-US"}[的兼容信息，]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备（设备型号]{style="font-family:宋体"}[S5120HI]{lang="EN-US"}[）文件]{style="font-family:宋体"}[flash:/s5120hi-http-d2403.bin]{lang="EN-US"}[的兼容信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。（兼容版本显示信息举例）（分布式设备－独立运行模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file feature flash:/s5120hi-http-d2403.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x2058985869}

[Verifying the file flash:/s5120hi-http-d2403.bin on slot 0\.....Done.]{lang="EN-US"}

[\<Sysname\> display version comp-matrix file feature flash:/cmw710-cfa-a0042.bin]{lang="EN-US"}

[Verifying the file flash:/cmw710-cfa-a0042.bin on slot 0\.....Done.]{lang="EN-US"}

[Verifying the file flash:/s5120hi-http-d2403.bin on slot 0\.....Done.]{lang="EN-US"}

[Feature image: flash:/cmw710-cfa-a0042.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  A0042]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  A0041]{lang="EN-US"}

[  A0042]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  A0041]{lang="EN-US"}

[ ]{lang="EN-US"}

[Compatible info of S5120HI:]{lang="EN-US"}

[Feature image: flash:/s5120hi-http-d2403.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  0                           Service Upgrade]{lang="EN-US"}

[  1                           Service Upgrade]{lang="EN-US"}

[  1.1                         Service Upgrade]{lang="EN-US"}

[  4                           Service Upgrade]{lang="EN-US"}

[  102                         Service Upgrade]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 0:]{lang="EN-US"}

[flash:/cmw710-cfa-a0042.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 4:]{lang="EN-US"}

[flash:/cmw710-cfa-a7125.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 1:]{lang="EN-US"}

[flash:/cmw710-cfa-a0042.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 1.1:]{lang="EN-US"}

[flash:/cmw710-cfa-a0042.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on slot 102:]{lang="EN-US"}

[flash:/cmw710-cfa-d2403.bin]{lang="EN-US"}

[    HTTP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x461495467}[查看父设备文件]{style="font-family:宋体"}[cmw710-cfa-a0041.bin]{lang="EN-US"}[的兼容信息，]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备（设备型号]{style="font-family:宋体"}[S5120HI]{lang="EN-US"}[）文件]{style="font-family:宋体"}[flash:/s5120hi-http-d2403.bin]{lang="EN-US"}[的兼容信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。（兼容版本显示信息举例）（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file feature flash:/s5120hi-http-d2403.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x2058985872}

[Verifying the file flash:/s5120hi-http-d2403.bin on chassis 1 slot 0\.....Done.]{lang="EN-US"}

[Copying file flash:/s5120hi-http-d2403.bin to chassis2#slot0#flash:/s5120hi-http-d2403.bin\...Done.]{lang="EN-US"}

[\<Sysname\> display version comp-matrix file feature flash:/cmw710-cfa-a0041.bin]{lang="EN-US"}

[Verifying the file flash:/cmw710-cfa-a0041.bin on chassis 1 slot 0\.....Done.]{lang="EN-US"}

[Verifying the file flash:/s5120hi-http-d2403.bin on chassis 1 slot 0\.....Done.]{lang="EN-US"}

[Feature image: flash:/cmw710-cfa-a0041.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  A0042]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  A0041]{lang="EN-US"}

[  A0042]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  A0041]{lang="EN-US"}

[ ]{lang="EN-US"}

[Compatible info of S5120HI:]{lang="EN-US"}

[Feature image: flash:/s5120hi-http-d2403.bin]{lang="EN-US"}

[  Version:]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version compatibility list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[  D2403]{lang="EN-US"}

[  Version dependency system list:]{lang="EN-US"}

[  D2402]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         0                 Service Upgrade]{lang="EN-US"}

[  1         0.1               Service Upgrade]{lang="EN-US"}

[  1         7                 Service Upgrade]{lang="EN-US"}

[  1         9                 Service Upgrade]{lang="EN-US"}

[  2         0                 Service Upgrade]{lang="EN-US"}

[  2         0.1               Service Upgrade]{lang="EN-US"}

[  2         1                 Service Upgrade]{lang="EN-US"}

[  2         6                 Service Upgrade]{lang="EN-US"}

[  101       0                 Service Upgrade]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 1 slot 0:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 1 slot 7:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 1 slot 9:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 1 slot 0.1:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 2 slot 0:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 2 slot 1:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 2 slot 6:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 2 slot 0.1:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    CFA]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table on chassis 101 slot 0:]{lang="EN-US"}

[flash:/cmw710-cfa-a7122.bin]{lang="EN-US"}

[    HTTP]{lang="EN-US"}

[]{#struct_0_71526_x1155_x199015767}[[表1-6 ]{lang="EN-US"}[display version comp-matrix]{lang="EN-US"}]{#_Toc138069139}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1112738846}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2136898800}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1263073771}

[[Verifying the file flash:/xx.bin on chassis 1 slot 0\.....Done.]{lang="EN-US"}]{#struct_0_71526_x1155_x1038122100}

[[验证文件是否合法]{style="font-family:宋体"}]{#struct_0_71526_x1155_512003872}

[[Boot image: flash:/cmw710-boot-a7122.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x199146839}

[[  Version:]{lang="EN-US"}]{#struct_0_71526_x1155_x617476393}

[[要显示的]{style="font-family:宋体"}[Boot]{lang="EN-US"}]{#struct_0_71526_x1155_370588635}[包的相关信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Boot]{lang="EN-US"}]{#struct_0_71526_x1155_x643235022}[包的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version]{lang="EN-US"}]{#struct_0_71526_x1155_x80825640}[：]{lang="EN-US" style="font-family:宋体"}[Boot]{lang="EN-US"}[包的版本]{lang="EN-US" style="font-family:宋体"}

[[System image: flash:/cmw710-system-a7122.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x198753623}

[[  Version:]{lang="EN-US"}]{#struct_0_71526_x1155_x549271431}

[[  V700R001B31D001]{lang="EN-US"}]{#struct_0_71526_x1155_x198819159}

[[  Version compatibility list:]{lang="EN-US"}]{#struct_0_71526_x1155_x544010959}

[[  V700R001B31D001]{lang="EN-US"}]{#struct_0_71526_x1155_x266399642}

[[  Version dependency boot list:]{lang="EN-US"}]{#struct_0_71526_x1155_x1526599510}

[[  7.1.031]{lang="EN-US"}]{#struct_0_71526_x1155_x147746788}

[[要显示的]{style="font-family:宋体"}[System]{lang="EN-US"}]{#struct_0_71526_x1155_1875203543}[包的相关信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[System]{lang="EN-US"}]{#struct_0_71526_x1155_x198884695}[包的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version]{lang="EN-US"}]{#struct_0_71526_x1155_1371011356}[：]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包的版本]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version compatibility list]{lang="EN-US"}]{#struct_0_71526_x1155_x53952401}[：和该]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包兼容的]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包版本列表]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version dependency boot list]{lang="EN-US"}]{#struct_0_71526_x1155_x158068730}[：依赖的]{lang="EN-US" style="font-family:宋体"}[Boot]{lang="EN-US"}[包版本列表，即安装该]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包前，必须先安装如下版本的]{lang="EN-US" style="font-family:宋体"}[Boot]{lang="EN-US"}[包中的任意一个]{lang="EN-US" style="font-family:宋体"}

[[Feature image: flash:/cmw710-cfa-a7124.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x1365928322}

[[  Version:]{lang="EN-US"}]{#struct_0_71526_x1155_x198950231}

[[  V700R001B31D003]{lang="EN-US"}]{#struct_0_71526_x1155_x188012919}

[[  Version compatibility list:]{lang="EN-US"}]{#struct_0_71526_x1155_1603689167}

[[  V700R001B31D003]{lang="EN-US"}]{#struct_0_71526_x1155_800800020}

[[  Version dependency system list:]{lang="EN-US"}]{#struct_0_71526_x1155_470498675}

[[  V700R001B31D001]{lang="EN-US"}]{#struct_0_71526_x1155_x198491479}

[[  V700R001B31D002]{lang="EN-US"}]{#struct_0_71526_x1155_987607439}

[[要显示的]{style="font-family:宋体"}[Feature]{lang="EN-US"}]{#struct_0_71526_x1155_1954292994}[包的相关信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Feature]{lang="EN-US"}]{#struct_0_71526_x1155_681196564}[包的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version]{lang="EN-US"}]{#struct_0_71526_x1155_x198557015}[：]{lang="EN-US" style="font-family:宋体"}[Feature]{lang="EN-US"}[包的版本]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version compatibility list]{lang="EN-US"}]{#struct_0_71526_x1155_x1372022110}[：和该]{lang="EN-US" style="font-family:宋体"}[Feature]{lang="EN-US"}[包兼容的]{lang="EN-US" style="font-family:宋体"}[Feature]{lang="EN-US"}[包版本列表]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version dependency system list]{lang="EN-US"}]{#struct_0_71526_x1155_x1764410926}[：依赖的]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包版本列表，即安装该]{lang="EN-US" style="font-family:宋体"}[Feature]{lang="EN-US"}[包前，必须先安装如下版本的]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包中的任意一个]{lang="EN-US" style="font-family:宋体"}

[[Compatible info of S5120HI:]{lang="EN-US"}]{#struct_0_71526_x1155_x2058985873}

[[Boot image: flash:/rpu-s5120hi-boot.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x2058985876}

[[  Version:]{lang="EN-US"}]{#struct_0_71526_x1155_x2027513872}

[[  7.1.041]{lang="EN-US"}]{#struct_0_71526_x1155_x2058985875}

[ ]{lang="EN-US"}

[[System image: flash:/rpu-s5120hi-system.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x2058985878}

[[  Version:]{lang="EN-US"}]{#struct_0_71526_x1155_1104654010}

[[  D2402]{lang="EN-US"}]{#struct_0_71526_x1155_x2058985877}

[[  Version compatibility list:]{lang="EN-US"}]{#struct_0_71526_x1155_279666290}

[[  D2402]{lang="EN-US"}]{#struct_0_71526_x1155_x1186503881}

[[  Version dependency boot list:]{lang="EN-US"}]{#struct_0_71526_x1155_279666291}

[[  7.1.041]{lang="EN-US"}]{#struct_0_71526_x1155_279666288}

[ ]{lang="EN-US"}

[[Feature image: flash:/s5120hi-http-d2402.bin]{lang="EN-US"}]{#struct_0_71526_x1155_769811247}

[[  Version:]{lang="EN-US"}]{#struct_0_71526_x1155_279666289}

[[  D2404]{lang="EN-US"}]{#struct_0_71526_x1155_279666286}

[[  Version compatibility list:]{lang="EN-US"}]{#struct_0_71526_x1155_769811261}

[[  D2404]{lang="EN-US"}]{#struct_0_71526_x1155_279666287}

[[  Version dependency system list:]{lang="EN-US"}]{#struct_0_71526_x1155_279666284}

[[  D2402]{lang="EN-US"}]{#struct_0_71526_x1155_769811259}

[[要显示的]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_71526_x1155_279666285}[设备的相关信息，包括：]{style="font-family:宋体"}

[[要显示的]{style="font-family:宋体"}[Boot]{lang="EN-US"}]{#struct_0_71526_x1155_279666282}[包的相关信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Boot]{lang="EN-US"}]{#struct_0_71526_x1155_769811257}[包的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version]{lang="EN-US"}]{#struct_0_71526_x1155_279666283}[：]{lang="EN-US" style="font-family:宋体"}[Boot]{lang="EN-US"}[包的版本]{lang="EN-US" style="font-family:宋体"}

[[要显示的]{style="font-family:宋体"}[System]{lang="EN-US"}]{#struct_0_71526_x1155_x1676648846}[包的相关信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[System]{lang="EN-US"}]{#struct_0_71526_x1155_x1456220856}[包的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version]{lang="EN-US"}]{#struct_0_71526_x1155_x1676648845}[：]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包的版本]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version compatibility list]{lang="EN-US"}]{#struct_0_71526_x1155_x1676648848}[：和该]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包兼容的]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包版本列表]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version dependency boot list]{lang="EN-US"}]{#struct_0_71526_x1155_x293421442}[：依赖的]{lang="EN-US" style="font-family:宋体"}[Boot]{lang="EN-US"}[包版本列表，即安装该]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包前，必须先安装如下版本的]{lang="EN-US" style="font-family:宋体"}[Boot]{lang="EN-US"}[包中的任意一个]{lang="EN-US" style="font-family:宋体"}

[[要显示的]{style="font-family:宋体"}[Feature]{lang="EN-US"}]{#struct_0_71526_x1155_x1676648847}[包的相关信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Feature]{lang="EN-US"}]{#struct_0_71526_x1155_x1676648850}[包的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version]{lang="EN-US"}]{#struct_0_71526_x1155_x649586266}[：]{lang="EN-US" style="font-family:宋体"}[Feature]{lang="EN-US"}[包的版本]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version compatibility list]{lang="EN-US"}]{#struct_0_71526_x1155_1259705931}[：和该]{lang="EN-US" style="font-family:宋体"}[Feature]{lang="EN-US"}[包兼容的]{lang="EN-US" style="font-family:宋体"}[Feature]{lang="EN-US"}[包版本列表]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Version dependency system list]{lang="EN-US"}]{#struct_0_71526_x1155_667671980}[：依赖的]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包版本列表，即安装该]{lang="EN-US" style="font-family:宋体"}[Feature]{lang="EN-US"}[包前，必须先安装如下版本的]{lang="EN-US" style="font-family:宋体"}[System]{lang="EN-US"}[包中的任意一个]{lang="EN-US" style="font-family:宋体"}

[[Influenced service according to following table]{lang="EN-US"}]{#struct_0_71526_x1155_x1486520959}

[[如果升级，受影响的功能模块。只有版本兼容时，才会显示该信息]{style="font-family:宋体"}]{#struct_0_71526_x1155_x642982769}

[[Incompatible upgrade]{lang="EN-US"}]{#struct_0_71526_x1155_x199015766}

[[如果升级指定的软件包，则升级的方式为不兼容升级]{style="font-family:宋体"}]{#struct_0_71526_x1155_x2136833264}

[[Chassis]{lang="EN-US"}]{#struct_0_71526_x1155_1805093033}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x1435455664}[中的成员编号。只有版本兼容时，才会显示该信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_71526_x1155_x199081302}

[[单板所在的槽位号。只有版本兼容时，才会显示该信息（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_585740454}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1145848361}[中的成员编号。只有版本兼容时，才会显示该信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Upgrade Way]{lang="EN-US"}]{#struct_0_71526_x1155_x199146838}

[[兼容升级策略。只有版本兼容时，才会显示该信息。取值可能为：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x617541929}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service Upgrade]{lang="EN-US"}]{#struct_0_71526_x1155_x1612489244}[：表示服务级增量升级，该方式下，仅对本业务模块有影响，对系统以及其他业务模块没有影响]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[File Upgrade]{lang="EN-US"}]{#struct_0_71526_x1155_x2102895451}[：表示文件级增量升级。该方式下，仅对系统内的、用户不可见的程序文件进行升级，对系统以及业务模块没有影响]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISSU Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_x199212374}[：表示通过软重启方式升级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_x2131805114}[：表示通过重启方式升级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sequence Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_1666700352}[：表示逐次重启方式。只有网板支持该升级方式，当网板需要重启升级时，为了避免重启升级过程中流量中断，系统会自动升级完毕一块网板后，再自动升级下一块网板，直到所有网板升级完毕后，再自动升级主控板。该字段的支持情况与网板的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1703826277}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_644680734}

::: {#-501336751 .myid}
[]{#_Toc404782738}[]{#struct_0_71526_x1155_1366089806}

**ISSU \-- ISSU配置命令 \-- install abort**

------------------------------------------------------------------------

[**[install abort]{lang="EN-US"}**]{#struct_0_71526_x1155_x198753622}[命令用来取消正在执行中的]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x549205895}

[**[install]{lang="EN-US"}**[ **abort** \[ *job-id* \]]{lang="EN-US"}]{#struct_0_71526_x1155_x1782467885}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1370620847}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1974979391}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1005888280}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x455942582}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1500313152}

[*[job-id]{lang="EN-US"}*]{#struct_0_71526_x1155_x1762604112}[：任务]{style="font-family:宋体"}[ID]{lang="EN-US"}[。不指定该参数时，则取消正在执行中的操作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x198819158}

[[当用户执行]{style="font-family:宋体"}**[install activate]{lang="EN-US"}**]{#struct_0_71526_x1155_x543945423}[、]{style="font-family:宋体"}**[install add]{lang="EN-US"}**[、]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**[、]{style="font-family:宋体"}**[install deactivate]{lang="EN-US"}**[、]{style="font-family:宋体"}**[install remove]{lang="EN-US"}**[或]{style="font-family:宋体"}**[install rollback to]{lang="EN-US"}**[命令时，系统会创建相应的任务。为了管理和监控这些任务，系统会给每个任务分配一个任务]{style="font-family:宋体"}[ID]{lang="EN-US"}[。一个任务]{style="font-family:宋体"}[ID]{lang="EN-US"}[代表一条命令。其中，只有正在进行的激活或卸载操作可以使用]{style="font-family:宋体"}**[install abort]{lang="EN-US"}**[命令进行取消操作，取消后回退到操作前状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_622965731}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_815046811}[取消正在执行中的操作。]{style="font-family:宋体"}

[[\<Sysname\> install abort]{lang="EN-US"}]{#struct_0_71526_x1155_x1623465201}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1222623299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install job]{lang="EN-US"}**]{#struct_0_71526_x1155_x339893464}
:::

::: {#-293778641 .myid}
[]{#_Toc404782739}[]{#struct_0_71526_x1155_x43493456}[]{#_Toc299981186}[]{#_Toc299981187}[]{#_Toc299981188}

**ISSU \-- ISSU配置命令 \-- install activate**

------------------------------------------------------------------------

[**[install activate]{lang="EN-US"}**]{#struct_0_71526_x1155_x198884694}[命令用来激活软件包。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1370945820}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_1930006959}

[**[install activate]{lang="EN-US"}**[ { **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \* \[ **test** \]]{lang="EN-US"}]{#struct_0_71526_x1155_408955880}

[**[install activate patch ]{lang="EN-US"}***[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x511752957}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_1062714810}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[install activate]{lang="EN-US"}**[ { **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x330422824}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \[ **test** \]]{lang="EN-US"}

[**[install activate patch ]{lang="EN-US"}***[filename ]{lang="EN-US"}*[{ **all** \| **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x247477301}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1142671943}[模式：]{style="font-family:宋体"}

[**[install activate]{lang="EN-US"}**[ { **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \* **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x1819756501}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \[ **test** \]]{lang="EN-US"}

[**[install]{lang="EN-US"}**[ **activate patch** *filename* { **all** \| **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x198950230}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x187947383}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_253338408}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1313327726}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_355708598}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x303311473}

[**[boot]{lang="EN-US"}**]{#struct_0_71526_x1155_x654154333}[：表示]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**]{#struct_0_71526_x1155_x61530214}[：表示]{style="font-family:宋体"}[System]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**]{#struct_0_71526_x1155_x1854740191}[：表示]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[patch]{lang="EN-US"}**]{#struct_0_71526_x1155_x198491478}[：表示补丁包。用于快速修复系统]{style="font-family:宋体"}[Bug]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_987672975}[：表示软件包的文件名，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，从存储介质名开始为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串（包括存储介质名在内），不区分大小写。]{style="font-family:宋体"}[&\<1-30\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_1609709888}[：]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，无特殊意义。（集中式设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_1352642085}[：升级补丁包对应的所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x1045218399}[：升级补丁包对应的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x1608522079}[：升级补丁包对应的所有成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x1381252676}[：升级补丁包对应的所有单板。（分布式设备－独立运行模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x1328898710}[：升级补丁包对应的所有单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（分布式设备－独立运行模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_1531788547}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x2006074995}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_2135692546}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x888068972}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_1755926612}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x957835361}*[cpu-number]{lang="EN-US"}*[：表示待升级的安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于升级防火墙插卡上的安全引擎，其它单板以及防火墙插卡上其它]{style="font-family:宋体"}[CPU]{lang="EN-US"}[升级时，不需要指定该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[test]{lang="EN-US"}**]{#struct_0_71526_x1155_x1183277269}[：查看指定软件包的升级策略。不带该参数时，表示直接执行升级操作。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x287963705}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有进行激活处理后，软件包才能生效。]{style="font-family:宋体"}]{#struct_0_71526_x1155_1529139380}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被激活的软件包只在本次运行的系统中生效。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x198557014}[要使被激活的软件包在设备重启后继续生效，还需要执行]{lang="EN-US" style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请先查看软件包版本发布说明书，如果某软件包需要]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1371956574}[License]{lang="EN-US"}[才能运行，且设备当前没有对应的有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[时，需安装对应的]{style="font-family:宋体"}[License]{lang="EN-US"}[，再执行该命令。]{style="font-family:宋体"}[否则，会导致命令执行失败。]{lang="EN-US" style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_71526_x1155_x199015769}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置该命令时，命令中指定的软件包必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}]{#struct_0_71526_x1155_x199081305}[flash:/xx.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_71526_x1155_x199146841}

[[当配置该命令时：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x199212377}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[命令中指定的软件包必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}]{#struct_0_71526_x1155_x198753625}[flash:/xx.bin]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[slot1#flash:/xx.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行命令行时，如果]{style="font-family:宋体"}]{#struct_0_71526_x1155_x957442145}*[filename]{lang="EN-US"}*[不是存放在待升级主控板上的文件，则系统会先将该文件拷贝到待升级主控板上，再执行升级动作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于安全引擎，执行命令行时，如果]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1441330857}*[filename]{lang="EN-US"}*[不是存放在待升级安全引擎上的文件，则系统会先将该文件拷贝到待升级安全引擎上，再执行升级动作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_71526_x1155_x549664647}**[slot]{lang="EN-US"}**[参数为主用主控板所在的槽位号，则执行该命令，会同时升级主用主控板和业务板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_71526_x1155_x198819161}**[slot]{lang="EN-US"}**[参数为备用主控板所在的槽位号，则执行该命令，只会升级备用主控板。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x198884697}[设备]{lang="EN-US" style="font-family:宋体"}

[[当配置该命令时：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x198491481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[命令中指定的软件包必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}]{#struct_0_71526_x1155_987083154}[flash:/xx.bin]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[slot]{lang="EN-US"}[2]{lang="EN-US"}[#flash:/xx.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_71526_x1155_x957573217}**[slot]{lang="EN-US"}**[参数为成员设备的成员编号，则执行该命令，如果指定的不是该成员设备上的软件包，会先将软件包拷贝到该成员设备上，再升级该成员设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1371891038}**[display device]{lang="EN-US"}**[、]{style="font-family:宋体"}**[display mdc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[命令查看到所有单板处于]{style="font-family:宋体"}[normal]{lang="EN-US"}[状态、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态和所有服务的]{style="font-family:宋体"}[action]{lang="EN-US"}[显示为]{style="font-family:宋体"}[0]{lang="EN-US"}[后，再执行]{style="font-family:宋体"}**[install activate]{lang="EN-US"}**[命令，否则，命令会执行失败。]{style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_71526_x1155_x199081304}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[当配置该命令时：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x199146840}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[命令中指定的软件包必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}]{#struct_0_71526_x1155_x618066220}[flash:/xx.bin]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[chassis1#slot1#flash:/xx.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行命令行时，如果]{style="font-family:宋体"}]{#struct_0_71526_x1155_x958228577}*[filename]{lang="EN-US"}*[不是存放在待升级主控板上的文件，则系统会先将该文件拷贝到待升级主控板上，再执行升级动作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于安全引擎，执行命令行时，如果]{style="font-family:宋体"}]{#struct_0_71526_x1155_x479553864}*[filename]{lang="EN-US"}*[不是存放在待升级安全引擎上的文件，则系统会先将该文件拷贝到待升级安全引擎上，再执行升级动作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_71526_x1155_x199212376}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[参数为全局主用主控板所在的槽位号，则执行该命令，会同时升级该主控板和所有业务板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_71526_x1155_x198753624}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[参数为全局备用主控板所在的槽位号，则执行该命令，只会升级该主控板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过]{style="font-family:宋体"}]{#struct_0_71526_x1155_x198884696}**[display device]{lang="EN-US"}**[、]{style="font-family:宋体"}**[display mdc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[命令查看到所有单板处于]{style="font-family:宋体"}[normal]{lang="EN-US"}[状态、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态和所有服务的]{style="font-family:宋体"}[action]{lang="EN-US"}[显示为]{style="font-family:宋体"}[0]{lang="EN-US"}[后，再执行]{style="font-family:宋体"}**[install activate]{lang="EN-US"}**[命令，否则，命令会执行失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1370814748}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1224538513}[显示]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}[ssh2.bin]{lang="EN-US"}[的升级策略。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> install activate feature flash:/ssh2.bin test]{lang="EN-US"}]{#struct_0_71526_x1155_x198950232}

[Verifying the file flash:/ssh2.bin on the device\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/ssh2.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Beta 1330                   Beta 1331]{lang="EN-US"}

[ ]{lang="EN-US"}

[Upgrade Way: Service Upgrade]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table:]{lang="EN-US"}

[flash:/ssh2.bin]{lang="EN-US"}

[     SSH       IFMGR     CFA       LAGG]{lang="EN-US"}

[[以上显示信息表明，该软件将采用增量方式升级。并且升级过程中会重启功能模块]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_71526_x1155_x187816311}[、]{style="font-family:宋体"}[IFMGR]{lang="EN-US"}[、]{style="font-family:宋体"}[CFA]{lang="EN-US"}[和]{style="font-family:宋体"}[LAGG]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x198491480}[显示备用主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}[ssh2.bin]{lang="EN-US"}[的升级策略。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> install activate feature flash:/ssh2.bin slot 1 test]{lang="EN-US"}]{#struct_0_71526_x1155_1367068176}

[Copying file flash:/ssh2.bin to slot1#flash:/ssh2.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/ssh2.bin on slot 1\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/ssh2.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Beta 1330                   Beta 1331]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  1                           Service Upgrade]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table:]{lang="EN-US"}

[flash:/ssh2.bin]{lang="EN-US"}

[     SSH       IFMGR     CFA       LAGG]{lang="EN-US"}

[[以上显示信息表明，该软件将采用增量方式升级。并且升级过程中会重启功能模块]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_71526_x1155_1446948601}[、]{style="font-family:宋体"}[IFMGR]{lang="EN-US"}[、]{style="font-family:宋体"}[CFA]{lang="EN-US"}[和]{style="font-family:宋体"}[LAGG]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1367002640}[显示从设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}[ssh2.bin]{lang="EN-US"}[。的升级策略（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> install activate feature flash:/ssh2.bin slot 2 test]{lang="EN-US"}]{#struct_0_71526_x1155_1366937104}

[Copying file flash:/ssh2.bin to slot2#flash:/ssh2.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/ssh2.bin on slot 2\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/ssh2.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Beta 1330                   Beta 1331]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  2                           Service Upgrade]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table:]{lang="EN-US"}

[flash:/ssh2.bin]{lang="EN-US"}

[     SSH       IFMGR     CFA       LAGG]{lang="EN-US"}

[[以上显示信息表明，该软件将采用增量方式升级。并且升级过程中会重启功能模块]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_71526_x1155_1366871568}[、]{style="font-family:宋体"}[IFMGR]{lang="EN-US"}[、]{style="font-family:宋体"}[CFA]{lang="EN-US"}[和]{style="font-family:宋体"}[LAGG]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1367330320}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板（全局备用主控板）上的]{style="font-family:
宋体"}[feature]{lang="EN-US"}[包]{style="font-family:
宋体"}[ssh2.bin]{lang="EN-US"}[的升级策略。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> install activate feature flash:/ssh2.bin chassis 1 slot 1 test]{lang="EN-US"}]{#struct_0_71526_x1155_1367068177}

[Copying file flash:/ssh2.bin to chassis1#slot1#flash:/ssh2.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/ssh2.bin on chassis 1 slot 1\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/ssh2.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Beta 1330                   Beta 1331]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         1                 Service Upgrade]{lang="EN-US"}

[ ]{lang="EN-US"}

[Influenced service according to following table:]{lang="EN-US"}

[flash:/ssh2.bin]{lang="EN-US"}

[     SSH       IFMGR     CFA       LAGG]{lang="EN-US"}

[[以上显示信息表明，该软件将采用增量方式升级。并且升级过程中会重启功能模块]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_71526_x1155_1447014137}[、]{style="font-family:宋体"}[IFMGR]{lang="EN-US"}[、]{style="font-family:宋体"}[CFA]{lang="EN-US"}[和]{style="font-family:宋体"}[LAGG]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x179080853}[激活]{style="font-family:宋体"}[System]{lang="EN-US"}[包]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}[feature.bin]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> install activate system flash:/system.bin feature flash:/feature.bin]{lang="EN-US"}]{#struct_0_71526_x1155_1367002641}

[Verifying the file flash:/feature.bin on the device\.....Done.]{lang="EN-US"}

[Verifying the file flash:/system.bin on the device\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/system.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Beta 1330                   Beta 1331]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  NONE                        Beta 1330]{lang="EN-US"}

[ ]{lang="EN-US"}

[Upgrade Way: Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[This operation maybe take several minutes, please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1366871569}[激活备用主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[System]{lang="EN-US"}[包]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}[feature.bin]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> install activate system flash:/system.bin feature flash:/feature.bin slot 1]{lang="EN-US"}]{#struct_0_71526_x1155_1367133713}

[Copying file flash:/system.bin to slot1#flash:/system.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/system.bin on slot 1\.....Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to slot1#flash:/feature.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 1\.....Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 0\.....Done.]{lang="EN-US"}

[Verifying the file flash:/system.bin on slot 0\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/system.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Beta 1330                   Beta 1331]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  None                        Beta 1330]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  1                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[This operation maybe take several minutes, please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1367068174}[激活从设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[System]{lang="EN-US"}[包]{style="font-family:宋体"}[system.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包]{style="font-family:宋体"}[feature.bin]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> install activate system flash:/system.bin feature flash:/feature.bin slot 2]{lang="EN-US"}]{#struct_0_71526_x1155_1367264782}

[Copying file flash:/system.bin to slot2#flash:/system.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/system.bin on slot 2\.....Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to slot2#flash:/feature.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 2\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/system.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Beta 1330                   Beta 1331]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  None                        Beta 1330]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  2                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[This operation maybe take several minutes, please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1367133710}[激活成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号单板（全局备用主控板）上的]{style="font-family:
宋体"}[Feature]{lang="EN-US"}[包]{style="font-family:
宋体"}[feature.bin]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> install activate feature flash:/feature.bin chassis 1 slot 1]{lang="EN-US"}]{#struct_0_71526_x1155_1367330319}

[Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 1\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/route-feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  None                        Beta 1330]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         1                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[This operation maybe take several minutes, please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[install activate]{lang="EN-US"}]{#struct_0_71526_x1155_1406161904}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1093013206}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_x779773850}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_1404991295}

[[Copying file *A* to *B*\...\...Done.]{lang="EN-US"}]{#struct_0_71526_x1155_1367133711}

[[将文件从位置]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_71526_x1155_1367068172}[拷贝到位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*[。当配置备用主控板时才有该提示信息（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[将文件从位置]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_71526_x1155_1366937100}[拷贝到位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*[。当配置从设备时才有该提示信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[将文件从位置]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_71526_x1155_1367330316}[拷贝到位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*[。当配置全局备用主控板时才有该提示信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Verifying the file flash:/xx.bin on chassis 1 slot 0\.....Done.]{lang="EN-US"}]{#struct_0_71526_x1155_1737880958}

[[验证文件是否合法]{style="font-family:宋体"}]{#struct_0_71526_x1155_633017367}

[[Upgrade summary according to following table]{lang="EN-US"}]{#struct_0_71526_x1155_1405572080}

[[升级摘要信息]{style="font-family:宋体"}]{#struct_0_71526_x1155_x671860199}

[[Running Version]{lang="EN-US"}]{#struct_0_71526_x1155_x2058943733}

[[设备当前运行的相同类型软件包的产品版本号]{style="font-family:宋体"}]{#struct_0_71526_x1155_x435831040}

[[New Version]{lang="EN-US"}]{#struct_0_71526_x1155_x1224970632}

[[目标软件包的产品版本号]{style="font-family:宋体"}]{#struct_0_71526_x1155_1367264780}

[[Chassis]{lang="EN-US"}]{#struct_0_71526_x1155_x1313331598}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1559445355}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_71526_x1155_x822813310}

[[单板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_x2035458132}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1367199244}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Upgrade Way]{lang="EN-US"}]{#struct_0_71526_x1155_1810899828}

[[兼容升级策略，取值可能为：]{style="font-family:宋体"}]{#struct_0_71526_x1155_1670067292}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service Upgrade]{lang="EN-US"}]{#struct_0_71526_x1155_x126649338}[：表示服务级增量升级，该方式下，仅对本业务模块有影响，对系统以及其他业务模块没有影响]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[File Upgrade]{lang="EN-US"}]{#struct_0_71526_x1155_1268783882}[：表示文件级增量升级。该方式下，仅对系统内的、用户不可见的程序文件进行升级，对系统以及业务模块没有影响]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISSU Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_975155508}[：表示通过软重启方式升级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_1367133708}[：表示通过重启方式升级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sequence Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_238268798}[：表示逐次重启方式。只有网板支持该升级方式，当网板需要重启升级时，为了避免重启升级过程中流量中断，系统会自动升级完毕一块网板后，再自动升级下一块网板，直到所有网板升级完毕后，再自动升级主控板。该字段的支持情况与网板的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Influenced service according to following table]{lang="EN-US"}]{#struct_0_71526_x1155_x1985361668}

[[将受影响的功能模块]{style="font-family:宋体"}]{#struct_0_71526_x1155_x119716057}

[[Upgrading software images to compatible versions. Continue? \[Y/N\]]{lang="EN-US"}]{#struct_0_71526_x1155_1367592460}

[[询问用户是否执行兼容升级操作]{style="font-family:宋体"}]{#struct_0_71526_x1155_218971225}

[[This operation maybe take several minutes, please wait]{lang="EN-US"}]{#struct_0_71526_x1155_x1096318561}

[[升级操作需要花费一定时间，请等待]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1206697426}

[[Done.]{lang="EN-US"}]{#struct_0_71526_x1155_x1094630300}

[[表示激活成功]{style="font-family:宋体"}]{#struct_0_71526_x1155_1366937101}

[[Operation failed.]{lang="EN-US"}]{#struct_0_71526_x1155_x986348830}

[[表示激活失败]{style="font-family:宋体"}]{#struct_0_71526_x1155_1367199245}

[[Install command does not support incompatible upgrade.]{lang="EN-US"}]{#struct_0_71526_x1155_1367133709}

[[不能使用]{style="font-family:宋体"}**[install]{lang="EN-US"}**]{#struct_0_71526_x1155_1367526925}[命令来升级不兼容版本]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1777987895}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install active]{lang="EN-US"}**]{#struct_0_71526_x1155_x1919696585}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x1361815179}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install deactivate]{lang="EN-US"}**]{#struct_0_71526_x1155_x1470228347}

::: {#2133760451 .myid}
[]{#_Toc404782740}[]{#struct_0_71526_x1155_x1420210178}

**ISSU \-- ISSU配置命令 \-- install add**

------------------------------------------------------------------------

[**[install]{lang="EN-US"}**[ **add**]{lang="EN-US"}]{#struct_0_71526_x1155_768951549}[命令用来解压缩]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x535124890}

[**[install]{lang="EN-US"}**[ **add** *ipe-filename* *medium-name*:]{lang="EN-US"}]{#struct_0_71526_x1155_x1361880715}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_872579520}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_651423636}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x378023783}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_581596718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1361946251}

[*[ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x548432525}[：]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件名，以]{style="font-family:宋体"}[.ipe]{lang="EN-US"}[作为后缀名，从存储介质名开始为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串（包括存储介质名在内），不区分大小写。]{style="font-family:宋体"}

[*[medium-name]{lang="EN-US"}*]{#struct_0_71526_x1155_204875801}[：存储介质的名称，形如]{style="font-family:宋体"}[flash]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[*[medium-name]{lang="EN-US"}*]{#struct_0_71526_x1155_637918221}[：存储介质的名称。如果是解压缩到主用主控板上，则为]{style="font-family:宋体"}[flash]{lang="EN-US"}[；如果是解压缩到备用主控板上，则为]{style="font-family:宋体"}[slot*n*#flash]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为备用主控板所在的槽位号；如果是解压缩到本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备上，则为]{style="font-family:宋体"}[slot*n*#flash]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号；如果是解压缩到安全引擎上，则为]{style="font-family:宋体"}[slot*n*.*x*#flash]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为防火墙插卡所在的槽位号，]{style="font-family:宋体"}*[x]{lang="EN-US"}*[为安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[*[medium-name]{lang="EN-US"}*]{#struct_0_71526_x1155_x1025834922}[：存储介质的名称。如果是解压缩到主设备上，则为]{style="font-family:宋体"}[flash]{lang="EN-US"}[；如果是解压缩到从设备上，则为]{style="font-family:宋体"}[slot*n*#flash]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为从设备的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[*[medium-name]{lang="EN-US"}*]{#struct_0_71526_x1155_242787960}[：存储介质的名称。如果是解压缩到全局主用主控板上，则为]{style="font-family:宋体"}[flash]{lang="EN-US"}[；如果是解压缩到全局备用主控板上，则为]{style="font-family:宋体"}[chassis*m*#slot*n*#flash]{lang="EN-US"}[，]{style="font-family:
宋体"}*[m]{lang="EN-US"}*[为设备的成员编号，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为成员设备上主控板所在的槽位号；如果是解压缩到本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备上，则为]{style="font-family:宋体"}[chassis*m*#slot*n*#flash]{lang="EN-US"}[，]{style="font-family:
宋体"}*[m]{lang="EN-US"}*[为设备的成员编号，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的虚拟槽位号；如果是解压缩到安全引擎上，则为]{style="font-family:宋体"}[chassis*m*#slot*n.x*#flash]{lang="EN-US"}[，]{style="font-family:宋体"}*[m]{lang="EN-US"}*[为防火墙插卡所在设备的成员编号，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为防火墙插卡所在的槽位号，]{style="font-family:宋体"}*[x]{lang="EN-US"}*[为安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1879425078}

[[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_2147081581}[文件是多个软件包的集合。将多个软件包整合成一个]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件对外发布，以便减少]{style="font-family:宋体"}[BIN]{lang="EN-US"}[包之间的版本管理问题。]{style="font-family:宋体"}

[[用户获取]{style="font-family:宋体"}[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x124212248}[文件后，可以使用]{style="font-family:宋体"}**[display install ipe-info]{lang="EN-US"}**[命令查看该]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件中包含了哪些软件包，可以通过]{style="font-family:宋体"}**[install add]{lang="EN-US"}**[命令将]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件解压生成软件包，再利用生成的软件包更新设备软件。]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的]{style="font-family:宋体"}[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x1362011787}[文件必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的]{style="font-family:宋体"}[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x1368426280}[文件必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[或]{style="font-family:宋体"}[slot1#flash:/xx.ipe]{lang="EN-US"}[。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的]{style="font-family:宋体"}[IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x59984024}[文件必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[或]{style="font-family:宋体"}[chassis1#slot1#flash:/xx.ipe]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1095771812}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1361553035}[解压缩]{style="font-family:宋体"}[all.ipe]{lang="EN-US"}[文件到存储介质]{style="font-family:宋体"}[flash]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> install add flash:/all.ipe flash:]{lang="EN-US"}]{#struct_0_71526_x1155_x1361618571}

[Verifying the file flash:/all.ipe on the device\...Done.]{lang="EN-US"}

[Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\.....Done.]{lang="EN-US"}

[[Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}]{#struct_0_71526_x1155_x1361749643}
:::

::: {#609558226 .myid}
[]{#_Toc404782741}[]{#struct_0_71526_x1155_x1927512411}

**ISSU \-- ISSU配置命令 \-- install commit**

------------------------------------------------------------------------

[**[install commit]{lang="EN-US"}**]{#struct_0_71526_x1155_1186169503}[命令用来确认软件包更改。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x515750122}

[**[install commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x753413443}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1769051323}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1361290891}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1317169612}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1522125500}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x829049859}

[[执行]{style="font-family:宋体"}**[install activate]{lang="EN-US"}**]{#struct_0_71526_x1155_x2129520158}[、]{style="font-family:宋体"}**[install deactivate]{lang="EN-US"}**[、]{style="font-family:宋体"}**[install rollback]{lang="EN-US"}**[命令会修改设备当前运行的软件包列表，使得只有符合用户需求的软件运行，不符合要求的不运行。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当执行]{style="font-family:宋体"}]{#struct_0_71526_x1155_641612918}**[install activate]{lang="EN-US"}**[命令，且为增量升级方式时，这些修改只在设备的本次运行过程有效，要使这个修改结果在设备下次重启后继续生效，需要再执行]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令进行确认，确认后的软件包会列入设备主用下次启动软件包列表。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当执行]{lang="EN-US" style="font-family:宋体"}**[install activate]{lang="EN-US"}**]{#struct_0_71526_x1155_1234900868}[命令，且为软重启或重启升级方式时，因为用户在执行]{lang="EN-US" style="font-family:
宋体"}**[install activate]{lang="EN-US"}**[命令时，系统已经修改了下次启动软件列表，所以，即便不再执行]{lang="EN-US" style="font-family:宋体"}**[install]{lang="EN-US"}**[ **commit**]{lang="EN-US"}[命令，升级软件包也会在系统重启后继续生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当执行]{style="font-family:宋体"}**[install deactivate]{lang="EN-US"}**]{#struct_0_71526_x1155_x660859914}[或]{style="font-family:宋体"}**[install rollback]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[这些修改只在设备的本次运行过程有效，要使这个修改结果在设备下次重启后继续生效，需要再执行]{lang="EN-US" style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令进行确认]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[boot-loader file]{lang="EN-US"}**]{#struct_0_71526_x1155_1368191371}[命令和]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令都可以变更主用下次启动软件包列表，最新的配置生效。两条命令的不同之处在于，]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令自动使用当前激活的软件包列表作为主用下次启动软件包列表。而]{style="font-family:宋体"}**[boot-loader file]{lang="EN-US"}**[命令还可以指定其它当前未激活的软件包，可以配置为主用或者备用下次启动软件包列表。]{style="font-family:宋体"}

[[请先查看软件包版本发布说明书，如果某软件包需要]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_71526_x1155_x1361356427}[才能运行，且设备当前没有对应的有效的]{style="font-family:宋体"}[License]{lang="EN-US"}[时，需安装对应的]{style="font-family:宋体"}[License]{lang="EN-US"}[，再执行该命令。否则，会导致命令执行失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1831095242}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x792931101}[确认软件包更改。]{style="font-family:宋体"}

[[\<Sysname\> install commit]{lang="EN-US"}]{#struct_0_71526_x1155_x1753435666}

[This operation will take several minutes, please wait\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x345785687}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install activate]{lang="EN-US"}**]{#struct_0_71526_x1155_1390392232}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install deactivate]{lang="EN-US"}**]{#struct_0_71526_x1155_1393389469}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[install rollback]{lang="EN-US"}**]{#struct_0_71526_x1155_1674854235}
:::

::: {#-1693286687 .myid}
[]{#_Toc404782742}[]{#struct_0_71526_x1155_x1361815178}[]{#_Toc304800180}[]{#_Toc304813450}[]{#_Toc304800181}[]{#_Toc304813451}[]{#_Toc304800183}[]{#_Toc304813453}[]{#_Toc304800187}[]{#_Toc304813457}[]{#_Toc304800193}[]{#_Toc304813463}[]{#_Toc304800195}[]{#_Toc304813465}[]{#_Toc304800196}[]{#_Toc304813466}[]{#_Toc304800200}[]{#_Toc304813470}[]{#_Toc304800206}[]{#_Toc304813476}[]{#_Toc304800207}[]{#_Toc304813477}[]{#_Toc304800208}[]{#_Toc304813478}[]{#_Toc304800209}[]{#_Toc304813479}[]{#_Toc304800220}[]{#_Toc304813490}[]{#_Toc304800221}[]{#_Toc304813491}[]{#_Toc304800222}[]{#_Toc304813492}[]{#_Toc304800224}[]{#_Toc304813494}[]{#_Toc304800225}[]{#_Toc304813495}[]{#_Toc304800227}[]{#_Toc304813497}[]{#_Toc304800228}[]{#_Toc304813498}[]{#_Toc304800230}[]{#_Toc304813500}[]{#_Toc304800231}[]{#_Toc304813501}[]{#_Toc304800232}[]{#_Toc304813502}[]{#_Toc304800233}[]{#_Toc304813503}

**ISSU \-- ISSU配置命令 \-- install deactivate**

------------------------------------------------------------------------

[**[install deactivate]{lang="EN-US"}**]{#struct_0_71526_x1155_95855594}[命令用来卸载]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包或补丁包。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1753430109}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1741216628}

[**[install deactivate]{lang="EN-US"}**[ **feature** *filename*&\<1-30\>]{lang="EN-US"}]{#struct_0_71526_x1155_384781492}

[**[install deactivate patch ]{lang="EN-US"}***[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_2138072958}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_x1901465131}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[install deactivate]{lang="EN-US"}**[ **feature** *filename*&\<1-30\> **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x515565947}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[install deactivate patch ]{lang="EN-US"}***[filename]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **all** \| **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_1619406930}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x1361880714}[模式：]{style="font-family:宋体"}

[**[install deactivate]{lang="EN-US"}**[ **feature** *filename*&\<1-30\> **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x693504421}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[install]{lang="EN-US"}**[ **deactivate patch** *filename* { **all** \| **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x1563428749}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x24768654}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1982704142}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_728906749}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1418937404}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x332485200}

[*[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x3040372}[：表示需要卸载]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包或补丁包的文件名，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}[&\<1-30\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_1351355382}[：表示安装了该补丁包的所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x2088313307}[：表示安装了该补丁包的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_773686988}[：表示安装了该补丁包的所有成员设备或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_x214728559}[：表示安装了该补丁包的所有单板。（分布式设备－独立运行模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_71526_x1155_319649685}[：表示安装了该补丁包的所有单板或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（分布式设备－独立运行模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x1361946250}[：]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，无特殊意义。（集中式设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x2114516466}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_1954471105}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x777831960}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_624340978}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_1606979173}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x957442147}*[cpu-number]{lang="EN-US"}*[：表示安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于卸载防火墙插卡上安全引擎的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包或补丁包，卸载其它单板以及防火墙插卡上其它]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包或补丁包时，不需要指定该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_924598088}

[[该命令只能对已经激活的软件包进行卸载操作。卸载的软件包的特性功能在本次系统运行中失效。如果要使卸载的软件包在设备重启后继续失效，请执行]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x1483054401}[命令对卸载操作进行确认。]{style="font-family:宋体"}

[[当配置该命令时，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x589480180}[。（集中式设备）]{style="font-family:宋体"}

[[当配置该命令时，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[slot]{lang="EN-US"}]{#struct_0_71526_x1155_1336689905}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[当配置该命令时，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[slot]{lang="EN-US"}]{#struct_0_71526_x1155_x653310698}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[当配置该命令时，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[chassis]{lang="EN-US"}]{#struct_0_71526_x1155_x1362011786}[和]{style="font-family:宋体"}[slot]{lang="EN-US"}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过]{style="font-family:宋体"}**[display device]{lang="EN-US"}**]{#struct_0_71526_x1155_197657661}[[、]{style="font-family:宋体"}]{.ItemListCharChar}**[display mdc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[[命令]{style="font-family:
宋体"}]{.ItemListCharChar}[查看到所有单板处于]{style="font-family:宋体"}[normal]{lang="EN-US"}[状态、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态和所有服务的]{style="font-family:宋体"}[action]{lang="EN-US"}[显示为]{style="font-family:宋体"}[0]{lang="EN-US"}[后，再执行]{style="font-family:宋体"}**[install deactivate]{lang="EN-US"}**[命令，否则，命令会执行失败。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1337651207}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1397841858}[卸载设备上的]{style="font-family:宋体"}[patch]{lang="EN-US"}[包]{style="font-family:宋体"}[route-patch.bin]{lang="EN-US"}[。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> install deactivate patch flash:/route-patch.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x884196613}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_313798046}[卸载]{style="font-family:宋体"}[0]{lang="EN-US"}[号单板上的]{style="font-family:宋体"}[patch]{lang="EN-US"}[包]{style="font-family:宋体"}[route-patch.bin]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> install deactivate patch flash:/route-patch.bin slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_1068632952}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_738344123}[卸载成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[patch]{lang="EN-US"}[包]{style="font-family:宋体"}[route-patch.bin]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> install deactivate patch flash:/route-patch.bin slot 1]{lang="EN-US"}]{#struct_0_71526_x1155_x1361553034}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1038920087}[卸载成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[0]{lang="EN-US"}[号槽位的单板上的]{style="font-family:
宋体"}[feature]{lang="EN-US"}[包]{style="font-family:
宋体"}[route-feature.bin]{lang="EN-US"}[。（分布式设备－]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> install deactivate feature flash:/route-feature.bin chassis 1 slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_x1338637380}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x957638755}[卸载安全引擎上的]{style="font-family:宋体"}[feature]{lang="EN-US"}[包]{style="font-family:宋体"}[flash:/issu.bin]{lang="EN-US"}[，安全引擎所在槽位号为]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> install deactivate feature flash:/issu.bin slot 7 cpu 1]{lang="EN-US"}]{#struct_0_71526_x1155_x1056008282}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x957573219}[卸载安全引擎上的]{style="font-family:宋体"}[feature]{lang="EN-US"}[包]{style="font-family:宋体"}[flash:/issu.bin]{lang="EN-US"}[，安全引擎所在设备的成员编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，槽位号为]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> install deactivate feature flash:/issu.bin chassis 1 slot 7 cpu 1]{lang="EN-US"}]{#struct_0_71526_x1155_2087031962}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1892476196}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install active]{lang="EN-US"}**]{#struct_0_71526_x1155_x1017429658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install inactive]{lang="EN-US"}**]{#struct_0_71526_x1155_1556165526}
:::

::: {#1020271610 .myid}
[]{#_Toc404782743}[]{#struct_0_71526_x1155_x1436361236}

**ISSU \-- ISSU配置命令 \-- install remove**

------------------------------------------------------------------------

[**[install remove]{lang="EN-US"}**]{#struct_0_71526_x1155_656110995}[命令用来删除指定的软件包。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1692796333}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1361618570}

[**[install remove]{lang="EN-US"}**[ { *filename \|* **inactive** }]{lang="EN-US"}]{#struct_0_71526_x1155_x2089072450}

[[分布式设备－独立运行模式]{style="font-family:宋体"}*[/]{lang="EN-US"}*]{#struct_0_71526_x1155_1382669733}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[install remove ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_1962297072}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] { *filename \|* **inactive** }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1102808140}[模式：]{style="font-family:宋体"}

[**[install remove ]{lang="EN-US"}**[\[ **chassis** *chassis-number* **slot** *slot-number* \[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x2087532610}**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}*[cpu-number]{lang="EN-US"}*[ \] \] { *filename \|* **inactive** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1936506233}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_784673601}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_996240874}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1361684106}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x53354601}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x124585668}[：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_266838890}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x1330473806}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有成员设备和本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x1222860337}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_1826085521}[：]{style="font-family:
宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/]{lang="EN-US"}[本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的所有单板和本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_71526_x1155_x958228579}*[cpu-number]{lang="EN-US"}*[：表示安全引擎的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数专用于删除安全引擎上的指定软件包，操作其它单板以及防火墙插卡上其它]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，不需要指定该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x192725283}[：表示软件包的文件名，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[inactive]{lang="EN-US"}**]{#struct_0_71526_x1155_x940669919}[：表示将删除指定存储介质根目录下、没有被激活的所有软件包。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1228723454}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能删除存储介质根目录下、没有被激活的软件包。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1361749642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1664120774}[chassis]{lang="EN-US"}[和]{style="font-family:宋体"}[slot]{lang="EN-US"}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[。（]{style="font-family:宋体"}[分布式设]{lang="EN-US" style="font-family:宋体"}[备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令后，指定的软件包将从设备上被彻底删除，用户将不能使用该软件包进行回滚或回退操作。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1706001185}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_2083550656}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x862360809}[删除软件包]{style="font-family:宋体"}[flash:/ssh-feature.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> install remove flash:/ssh-feature.bin]{lang="EN-US"}]{#struct_0_71526_x1155_2124947683}
:::

::: {#1461171130 .myid}
[]{#_Toc404782744}[]{#struct_0_71526_x1155_x1361290890}[]{#_Toc304800236}[]{#_Toc304813506}[]{#_Toc304800238}[]{#_Toc304813508}[]{#_Toc304800239}[]{#_Toc304813509}[]{#_Toc304800240}[]{#_Toc304813510}[]{#_Toc304800241}[]{#_Toc304813511}[]{#_Toc304800242}[]{#_Toc304813512}[]{#_Toc304800243}[]{#_Toc304813513}[]{#_Toc304800244}[]{#_Toc304813514}[]{#_Toc304800245}[]{#_Toc304813515}[]{#_Toc304800246}[]{#_Toc304813516}[]{#_Toc304800247}[]{#_Toc304813517}[]{#_Toc304800248}[]{#_Toc304813518}[]{#_Toc304800249}[]{#_Toc304813519}[]{#_Toc304800250}[]{#_Toc304813520}[]{#_Toc299981194}[]{#_Toc299981196}[]{#_Toc299981197}

**ISSU \-- ISSU配置命令 \-- install rollback to**

------------------------------------------------------------------------

[**[install rollback to]{lang="EN-US"}**]{#struct_0_71526_x1155_x1411713743}[命令用来回滚到指定的回滚点，即按回滚点上记录的信息，进行回滚操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1897171561}

[**[install rollback to]{lang="EN-US"}**[ { *point-id* \| **original** }]{lang="EN-US"}]{#struct_0_71526_x1155_x452988985}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1317771214}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1119645654}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2066048539}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_1739588386}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_440711511}

[*[point-id]{lang="EN-US"}*]{#struct_0_71526_x1155_x1361356426}[：回滚点的编号，当系统中至少存在两个回滚点的时候，才能输入该参数。可以用]{style="font-family:宋体"}**[display install rollback]{lang="EN-US"}**[命令查看系统中存在的回滚点。]{style="font-family:宋体"}

[**[original]{lang="EN-US"}**]{#struct_0_71526_x1155_x265011301}[：回滚到]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级初始状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_554996987}

[[每次激活或者卸载软件包之后，系统中将运行着不同的软件包，系统将这些变化记录为回滚点。通过回滚功能，可将系统回滚到某个历史状态，或者恢复到]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_909396794}[升级初始状态。]{style="font-family:宋体"}

[[当升级方式为增量升级时，软件包回滚只在设备本次运行过程中生效，用户只有通过]{style="font-family:宋体"}**[install commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x1085674435}[命令确认软件包的更改后，才能使此次的回滚操作在系统重启后生效。系统最多支持]{style="font-family:宋体"}[50]{lang="EN-US"}[个回滚点，当回滚点超过最大值时，旧的回滚点会被删除，新的回滚点会被保存。]{style="font-family:宋体"}

[[当升级方式为软重启或重启升级时，系统不会保留任何回滚点，只支持回滚到系统升级初始状态。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1956371408}

[[补丁包不支持回滚操作。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1469111892}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1761906026}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x2053108152}[回滚到回滚点]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> install rollback to 1]{lang="EN-US"}]{#struct_0_71526_x1155_x1361815181}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1113670307}[回滚到]{style="font-family:宋体"}[original]{lang="EN-US"}[回滚点。可通过观察]{style="font-family:宋体"}[active]{lang="EN-US"}[列表和回滚点的变化看出执行的结果。]{style="font-family:宋体"}

[[\<Sysname\> display install active]{lang="EN-US"}]{#struct_0_71526_x1155_584557902}

[Active packages on slot 1:]{lang="EN-US"}

[  flash:/boot-a0201.bin]{lang="EN-US"}

[  flash:/system-a0201.bin]{lang="EN-US"}

[  flash:/ssh-feature-a0201.bin]{lang="EN-US"}

[\<Sysname\> display install rollback]{lang="EN-US"}

[Install rollback information 1 on slot 1:]{lang="EN-US"}

[  Updating from no package]{lang="EN-US"}

[         to flash:/ssh-feature-a0201.bin.]{lang="EN-US"}

[[以上显示信息表明，当前激活的包有三个，但是确认的只有两个，回滚点]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_71526_x1155_x512602968}[是激活了]{style="font-family:宋体"}[flash:/ssh-feature-a0201.bin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> install rollback to original]{lang="EN-US"}]{#struct_0_71526_x1155_x1361880717}

[\<Sysname\> display install active]{lang="EN-US"}

[Active packages on slot 1:]{lang="EN-US"}

[  flash:/boot-a0201.bin]{lang="EN-US"}

[  flash:/system-a0201.bin]{lang="EN-US"}

[\<Sysname\> display install committed]{lang="EN-US"}

[Committed packages on slot 1:]{lang="EN-US"}

[  flash:/boot-a0201.bin]{lang="EN-US"}

[  flash:/system-a0201.bin]{lang="EN-US"}

[[执行]{style="font-family:宋体"}**[install rollback to original]{lang="EN-US"}**]{#struct_0_71526_x1155_2035378934}[命令后，设备运行的软件集恢复到]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级初始状态，]{style="font-family:宋体"}[flash:/ssh-feature-a0201.bin]{lang="EN-US"}[被卸载。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1731285808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install rollback]{lang="EN-US"}**]{#struct_0_71526_x1155_x1042860091}
:::

::: {#183223271 .myid}
[]{#_Toc404782745}[]{#struct_0_71526_x1155_1379678540}

**ISSU \-- ISSU配置命令 \-- install verify**

------------------------------------------------------------------------

[**[install verify]{lang="EN-US"}**]{#struct_0_71526_x1155_x1717137431}[命令用来执行软件包检验。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2002678385}

[**[install verify]{lang="EN-US"}**]{#struct_0_71526_x1155_x355720282}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1538781876}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1361946253}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_614366889}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1448687108}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1754749778}

[[正常情况下，设备上运行的软件必须完整并且处于激活状态的软件包应该和已确认的软件包一致，否则，会导致设备重启前后运行的软件版本不一致，甚至不能正常启动。（集中式设备）]{style="font-family:宋体"}]{#struct_0_71526_x1155_431641829}

[[正常情况下，设备上各主控板运行的软件必须完整并且版本应该一致，各主控板上处于激活状态的软件包应该和已确认的软件包一致，否则，会影响设备的主备倒换，以及导致主控板重启前后运行的软件版本不一致甚至不能正常启动。（分布式设备－独立运行模式）]{style="font-family:宋体"}]{#struct_0_71526_x1155_1942590839}

[[正常情况下，]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x2067250382}[中上各成员设备运行的软件必须完整并且版本应该一致，各成员设备上处于激活状态的软件包应该和已确认的软件包一致，否则，会影响主设备和从设备的倒换，以及导致成员设备重启前后运行的软件版本不一致甚至不能正常启动。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[正常情况下，]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x154568507}[中各主控板运行的软件必须完整并且版本应该一致，各主控板上处于激活状态的软件包应该和已确认的软件包一致，否则，会影响主控板的主备倒换，以及导致主控板重启前后运行的软件版本不一致甚至不能正常启动。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[使用该命令，能帮助用户进行软件包检查，]{style="font-family:宋体"}]{#struct_0_71526_x1155_x319645886}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当系统提示软件包不完整时，请重新下载并安装软件包。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1362011789}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当系统提示软件包不一致时，请使用]{lang="EN-US" style="font-family:宋体"}**[install activate]{lang="EN-US"}**]{#struct_0_71526_x1155_x918087586}[、]{lang="EN-US" style="font-family:
宋体"}**[install deactivate]{lang="EN-US"}**[以及]{lang="EN-US" style="font-family:宋体"}**[install commit]{lang="EN-US"}**[命令来确保它们的一致。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1824045492}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_2104988417}[检验软件包信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> install verify]{lang="EN-US"}]{#struct_0_71526_x1155_884128503}

[Active packages on the device are the reference packages.]{lang="EN-US"}

[Packages will be compared with the reference packages.]{lang="EN-US"}

[This operation will take several minutes, please wait\...]{lang="EN-US"}

[  Verifying packages on the device:]{lang="EN-US"}

[  Start to check active package completeness.]{lang="EN-US"}

[Verifying the file flash:/boot-a0101.bin on the device\...\...\.....Done.]{lang="EN-US"}

[   flash:/boot-a0101.bin verification successful.]{lang="EN-US"}

[Verifying the file flash:/system-a0101.bin on the device\...\...\...\...Done.]{lang="EN-US"}

[   flash:/system-a0101.bin verification successful.]{lang="EN-US"}

[  Start to check active package consistency.]{lang="EN-US"}

[    Active packages are consistent with committed packages on their own board.]{lang="EN-US"}

[    Active packages are consistent with the reference packages.]{lang="EN-US"}

[Verification is done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1361553037}[检验设备各个单板上的软件包信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> install verify]{lang="EN-US"}]{#struct_0_71526_x1155_x1442204614}

[Active packages on slot 1 are the reference packages.]{lang="EN-US"}

[Packages will be compared with the reference packages.]{lang="EN-US"}

[This operation will take several minutes, please wait\...]{lang="EN-US"}

[  Verifying packages on slot 0:]{lang="EN-US"}

[  Start to check active package completeness.]{lang="EN-US"}

[Verifying the file flash:/boot-a0101.bin on slot 0\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/boot-a0101.bin verification successful.]{lang="EN-US"}

[Verifying the file flash:/system-a0101.bin on slot 0\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/system-a0101.bin verification successful.]{lang="EN-US"}

[  Start to check active package consistency.]{lang="EN-US"}

[    Active packages are consistent with committed packages on their own board.]{lang="EN-US"}

[    Active packages are consistent with the reference packages.]{lang="EN-US"}

[  Verifying packages on slot 1:]{lang="EN-US"}

[  Start to check active package completeness.]{lang="EN-US"}

[Verifying the file flash:/boot-a0101.bin on slot 1\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/boot-a0101.bin verification successful.]{lang="EN-US"}

[Verifying the file flash:/system-a0101.bin on slot 1\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/system-a0101.bin verification successful.]{lang="EN-US"}

[  Start to check active package consistency.]{lang="EN-US"}

[    Active packages are consistent with committed packages on their own board.]{lang="EN-US"}

[    Active packages are consistent with the reference packages.]{lang="EN-US"}

[Verification is done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_453479875}[检验设备各个单板上的软件包信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> install verify]{lang="EN-US"}]{#struct_0_71526_x1155_x1361618573}

[Active packages on slot 1 are the reference packages.]{lang="EN-US"}

[Packages will be compared with the reference packages.]{lang="EN-US"}

[This operation will take several minutes, please wait\...]{lang="EN-US"}

[  Verifying packages on slot 1:]{lang="EN-US"}

[  Start to check active package completeness.]{lang="EN-US"}

[Verifying the file flash:/boot-a0101.bin on slot 1\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/boot-a0101.bin verification successful.]{lang="EN-US"}

[Verifying the file flash:/system-a0101.bin on slot 1\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/system-a0101.bin verification successful.]{lang="EN-US"}

[  Start to check active package consistency.]{lang="EN-US"}

[    Active packages are consistent with committed packages on their own board.]{lang="EN-US"}

[    Active packages are consistent with the reference packages.]{lang="EN-US"}

[  Verifying packages on slot 2:]{lang="EN-US"}

[  Start to check active package completeness.]{lang="EN-US"}

[Verifying the file flash:/boot-a0101.bin on slot 2\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/boot-a0101.bin verification successful.]{lang="EN-US"}

[Verifying the file flash:/system-a0101.bin on slot 2\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/system-a0101.bin verification successful.]{lang="EN-US"}

[  Start to check active package consistency.]{lang="EN-US"}

[    Active packages are consistent with committed packages on their own board.]{lang="EN-US"}

[    Active packages are consistent with the reference packages.]{lang="EN-US"}

[Verification is done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1802610319}[检验设备各个单板上的软件包信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> install verify]{lang="EN-US"}]{#struct_0_71526_x1155_x1361684109}

[Active packages on slot 1 are the reference packages.]{lang="EN-US"}

[Packages will be compared with the reference packages.]{lang="EN-US"}

[This operation will take several minutes, please wait\...]{lang="EN-US"}

[  Verifying packages on chassis 1 slot 0:]{lang="EN-US"}

[  Start to check active package completeness.]{lang="EN-US"}

[Verifying the file flash:/boot-a0101.bin on chassis 1 slot 0\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/boot-a0101.bin verification successful.]{lang="EN-US"}

[Verifying the file flash:/system-a0101.bin on chassis 1 slot 0\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/system-a0101.bin verification successful.]{lang="EN-US"}

[  Start to check active package consistency.]{lang="EN-US"}

[    Active packages are consistent with committed packages on their own board.]{lang="EN-US"}

[    Active packages are consistent with the reference packages.]{lang="EN-US"}

[  Verifying packages on chassis 1 slot 1:]{lang="EN-US"}

[  Start to check active package completeness.]{lang="EN-US"}

[Verifying the file flash:/boot-a0101.bin on chassis 1 slot 1\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/boot-a0101.bin verification successful.]{lang="EN-US"}

[Verifying the file flash:/system-a0101.bin on chassis 1 slot 1\...\...\...\...\...\...\...Done.]{lang="EN-US"}

[    flash:/system-a0101.bin verification successful.]{lang="EN-US"}

[  Start to check active package consistency.]{lang="EN-US"}

[    Active packages are consistent with committed packages on their own board.]{lang="EN-US"}

[    Active packages are consistent with the reference packages.]{lang="EN-US"}

[Verification is done.]{lang="EN-US"}
:::

::::: {#753966118 .myid}
[]{#_Toc404782746}[]{#struct_0_71526_x1155_x1619438542}[]{#_Toc329856482}

**ISSU \-- ISSU配置命令 \-- issu accept**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ISSU命令.files/image001.png){#图片 5 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_71526_x1155_x133160814}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_71526_x1155_x215227887}
:::

[ ]{lang="EN-US"}

[**[issu accept]{lang="EN-US"}**]{#struct_0_71526_x1155_x1155709298}[命令用来确认]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[兼容升级，接受已升级的软件版本，并删除回滚定时器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1361749645}

[**[issu accept]{lang="EN-US"}**]{#struct_0_71526_x1155_x1120943357}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1446173688}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1597022220}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1660597449}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x680688799}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1903189924}

[[执行本命令后，系统会删除回滚定时器，本次]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_2099516218}[升级过程中不会再进行自动回滚，用户可以执行]{style="font-family:宋体"}**[issu rollback]{lang="EN-US"}**[命令进行手动回滚。]{style="font-family:宋体"}

[[此命令为可选命令，可以不执行此命令，直接执行后面的]{style="font-family:宋体"}**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x1549191804}[命令完成升级过程。]{style="font-family:宋体"}

[[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_x1361290893}[不兼容升级时，不需要执行该命令，执行该命令会提示失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1814998270}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1572257440}[版本兼容情况下，确认升级步骤。]{style="font-family:宋体"}

[[\<Sysname\> issu accept]{lang="EN-US"}]{#struct_0_71526_x1155_x318800813}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x958016736}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x413387260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_x447199523}
:::::

::::: {#1843086676 .myid}
[]{#_Toc404782747}[]{#struct_0_71526_x1155_x957835366}[]{#_Toc368057764}

**ISSU \-- ISSU配置命令 \-- issu blade**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ISSU命令.files/image002.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_71526_x1155_x1407144956}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_71526_x1155_x957507686}
:::

**[ ]{lang="EN-US"}**

[**[issu blade]{lang="EN-US"}**]{#struct_0_71526_x1155_x1002323403}[命令用来设置安全引擎的升级软件包。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_436482086}

[**[issu blade ]{lang="EN-US"}***[blade-model]{lang="EN-US"}***[ file ]{lang="EN-US"}**[{ **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \*]{lang="EN-US"}]{#struct_0_71526_x1155_x1441134250}

[**[issu blade ]{lang="EN-US"}***[blade-model]{lang="EN-US"}***[ file ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x957638758}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x258646448}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x957573222}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_2087490711}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_91188086}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x958294118}

[**[blade ]{lang="EN-US"}***[blade-model]{lang="EN-US"}*]{#struct_0_71526_x1155_1912807290}[：设备支持的安全引擎的型号，该参数必须完整输入，不区分大小写。可输入]{style="font-family:宋体"}**[boot-loader blade ]{lang="EN-US"}[？]{style="font-family:宋体"}**[，来获取该参数的取值。]{style="font-family:宋体"}

[**[boot]{lang="EN-US"}**]{#struct_0_71526_x1155_x958228582}[：表示]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**]{#struct_0_71526_x1155_x479357257}[：表示]{style="font-family:宋体"}[System]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**]{#struct_0_71526_x1155_x957769829}[：表示]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_1219830507}[：表示软件包的文件名，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，从存储介质名开始为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串（包括存储介质名在内），不区分大小写。]{style="font-family:宋体"}[&\<1-30\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[ipe]{lang="EN-US"}***[ ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x299891683}[：]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件名，以]{style="font-family:宋体"}[.ipe]{lang="EN-US"}[作为后缀名，从存储介质名开始为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串（包括存储介质名在内），不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x957704293}

[[该命令只是指定安全引擎的升级软件包，并不执行升级动作，等主控板升级时，安全引擎使用这些升级软件包启动来完成升级。组网环境不同，安全引擎的具体升级时机不同，具体描述请参见"基础配置指导"中的"]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_x641130423}["。如果不进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级，而仅仅是重启安全引擎，该命令配置的软件包将不会生效。]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}[/IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x957900901}[文件必须放在存储介质主分区的根目录下。]{style="font-family:宋体"}

[[输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}]{#struct_0_71526_x1155_1257632494}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行命令行合法性检查。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x957835365}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将升级文件全部拷贝到系统中所有的主控板和该类型的安全引擎上。如果指定的是]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1407079420}[IPE]{lang="EN-US"}[文件，则会自动解压到所有该类型的安全引擎上。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果源软件包放在主控板的存储介质上，拷贝完成后，提示用户是否需要删除源软件包。如果用户确认，则自动删除源软件包，以便释放空间。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1636779273}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x957507685}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1002126795}[配置型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎的升级软件包为]{style="font-family:宋体"}[flash:/test.bin]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> issu blade Blade-m9k file feature flash:/test.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x957442149}

[Verifying the file flash:/test.bin on slot 1\...Done.]{lang="EN-US"}

[File flash:/test.bin already exists on slot 2.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/test.bin to slot2.1#flash:/test.bin\...Done.]{lang="EN-US"}

[File flash:/test.bin already exists on slot 3.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/test.bin to slot3.1#flash:/test.bin\...Done.]{lang="EN-US"}

[Delete flash:/test.bin from slot 5? \[Y/N\]:N]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1441593001}[配置型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎的升级软件包为]{style="font-family:宋体"}[slot2.1#flash:/test.bin]{lang="EN-US"}[）。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> issu blade Blade-m9k file feature slot2.1#flash:/test.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x957638757}

[Verifying the file flash:/test.bin on slot 1\...Done.]{lang="EN-US"}

[File flash:/test.bin already exists on slot 3.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/test.bin to slot3.1#flash:/test.bin\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1056139354}[配置型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎的升级软件包为]{style="font-family:宋体"}[flash:/test.ipe]{lang="EN-US"}[。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> issu blade Blade-m9k file ipe flash:/test.ipe]{lang="EN-US"}]{#struct_0_71526_x1155_x957573221}

[Verifying the file flash:/test.ipe on slot 0\...Done.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on slot 5.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file blade3fwm9k-cmw710-test-a0002.bin to flash:/blade3fwm9k-cmw710-test-a0002.bin\...Done.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on slot 2.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-test-a0002.bin to slot2.1#flash:/blade3fwm9k-cmw710-test-a0002.bin\...Done.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on slot 3.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:N]{lang="EN-US"}

[Delete flash:/blade3fwm9k-cmw710-test-a0002.bin from slot 5? \[Y/N\]:N]{lang="EN-US"}

[Delete flash:/test.ipe from slot 5? \[Y/N\]:N]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_2087556247}[配置型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎的升级软件包为]{style="font-family:宋体"}[flash:/test.bin]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\>issu blade Blade-m9k file feature flash:/test.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x958294117}

[Verifying the file flash:/test.bin on chassis 1 slot 0\...Done.]{lang="EN-US"}

[File flash:/test.bin already exists on chassis 1 slot 2.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/test.bin to chassis1#slot2.1#flash:/test.bin\...Done.]{lang="EN-US"}

[File flash:/test.bin already exists on chassis 1 slot 3.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/test.bin to chassis1#slot3.1#flash:/test.bin\...Done.]{lang="EN-US"}

[Delete flash:/test.bin from chassis 1 slot 5? \[Y/N\]:N]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1913659258}[配置型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎的升级软件包为]{style="font-family:宋体"}[chassis1#slot2.1#flash:/test.bin]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\>issu blade Blade-m9k file feature chassis1#slot2.1#flash:/test.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x958228581}

[Verifying the file flash:/test.bin on chassis 1 slot 0\...Done.]{lang="EN-US"}

[File flash:/test.bin already exists on chassis 1 slot 3.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/test.bin to chassis1#slot3.1#flash:/test.bin\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x479422793}[配置型号为]{style="font-family:宋体"}[Blade-m9k]{lang="EN-US"}[的安全引擎的升级软件包为]{style="font-family:宋体"}[chassis1#slot3.1#flash:/test.ipe]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\>issu blade Blade-m9k file ipe chassis1#slot3.1#flash:/test.ipe]{lang="EN-US"}]{#struct_0_71526_x1155_608314115}

[Verifying the file flash:/test.ipe on chassis 1 slot 0\...Done.]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on chassis 1 slot 3.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file blade3fwm9k-cmw710-test-a0002.bin to chassis1#slot3.1#flash:/blade3fwm9k-cmw710-test-a0002.bin\...Done]{lang="EN-US"}

[File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on chassis 1 slot 2.1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/blade3fwm9k-cmw710-test-a0002.bin to chassis1#slot2.1#flash:/blade3fwm9k-cmw710-test-a0002.bin\...Done.]{lang="EN-US"}
:::::

::::: {#642127682 .myid}
[]{#_Toc404782748}[]{#struct_0_71526_x1155_154413628}[]{#_Toc329856483}[]{#_Toc304800254}[]{#_Toc304813524}[]{#_Toc304800255}[]{#_Toc304813525}[]{#_Toc299981201}

**ISSU \-- ISSU配置命令 \-- issu commit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ISSU命令.files/image001.png){#图片 6 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_71526_x1155_x1361356429}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_71526_x1155_x312065468}
:::

[ ]{lang="EN-US"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_71526_x1155_x490393720}

[**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_307873781}[命令用来完成升级，升级完成后]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回到初始状态。执行此命令后，不能再通过]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回滚命令或者回滚定时器进行回滚操作。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_71526_x1155_x698453072}

[**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_400738394}[命令用来对原主用主控板进行兼容版本升级，升级完成后]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回到初始状态。执行此命令后，不能再通过]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回滚命令或者回滚定时器进行回滚操作。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1778227753}[设备]{lang="EN-US" style="font-family:宋体"}

[**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x1673233324}[命令用来对原主设备及未升级的从设备进行兼容版本升级。所有成员设备完成升级后，本次升级结束，]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回到初始状态。执行此命令后，不能再通过]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回滚命令或者回滚定时器进行回滚操作。多个从设备的情况下应该在一个备设备启动完成并重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[后再对下一个从设备执行该命令，否则可能引起升级错误。]{style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_71526_x1155_1517267767}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[对于单成员设备双主控的情况，]{style="font-family:宋体"}**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x1361815180}[命令用来对原主用主控板进行兼容版本升级，升级完成后]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回到初始状态。执行此命令后，不能再通过]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回滚命令或者回滚定时器进行回滚操作。]{style="font-family:宋体"}

[[对于多成员设备的情况，]{style="font-family:宋体"}**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_452413634}[命令用来对原主设备及未升级的从设备进行兼容版本升级。所有成员设备完成升级后，本次升级结束，]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回到初始状态。执行此命令后不能再通过]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[回滚命令或者回滚定时器进行回滚操作。如果有多个成员设备需要通过]{style="font-family:宋体"}**[issu commit]{lang="EN-US"}**[命令进行升级，需要等到一个成员设备重启、重新加入]{style="font-family:宋体"}[IRF]{lang="EN-US"}[后再进行下一个成员设备的升级，否则可能造成升级错误。]{style="font-family:宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_71526_x1155_5059905}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_1803472322}

[**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_1408318002}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_71526_x1155_924829925}

[**[issu commit slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x1461880042}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x694599463}[设备：]{style="font-family:宋体"}

[**[issu commit slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_1082330264}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x1361880716}[模式单成员设备：]{style="font-family:宋体"}

[**[issu commit chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_469294993}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_881993968}[模式多成员设备：]{style="font-family:宋体"}

[**[issu commit chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_71526_x1155_685395978}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1703753832}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x107958550}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1929996644}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1048976074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_278507572}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x1361946252}[：原主用主控板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x951717052}[：待升级的原主设备以及其它从设备的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x656620948}[：原主用主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_71526_x1155_1383133902}[：待升级的原主设备以及其它从设备的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式多成员设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_395575992}

[[从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过]{style="font-family:宋体"}**[display device]{lang="EN-US"}**]{#struct_0_71526_x1155_x154252051}[[、]{style="font-family:宋体"}]{.ItemListCharChar}**[display mdc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[[命令]{style="font-family:
宋体"}]{.ItemListCharChar}[查看到所有单板处于]{style="font-family:宋体"}[normal]{lang="EN-US"}[状态、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态和所有服务的]{style="font-family:宋体"}[action]{lang="EN-US"}[显示为]{style="font-family:宋体"}[0]{lang="EN-US"}[后，再执行]{style="font-family:宋体"}**[issu commit]{lang="EN-US"}**[命令，否则，命令会执行失败。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x658241364}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_403406149}[版本兼容情况下，确认升级。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> issu commit]{lang="EN-US"}]{#struct_0_71526_x1155_x968586362}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1362011788}[版本兼容情况下，成员]{style="font-family:宋体"}[2]{lang="EN-US"}[已经升级完成成为新的主设备，升级原主设备（假设成员编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[）和其他成员（假设成员编号为]{style="font-family:宋体"}[4]{lang="EN-US"}[和]{style="font-family:宋体"}[1]{lang="EN-US"}[）。（集中式]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu commit slot 3]{lang="EN-US"}]{#struct_0_71526_x1155_x1361618575}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  3                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[\<Sysname\> issu commit slot 4]{lang="EN-US"}

[Copying file flash:/feature.bin to slot4#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 4\...\...\...\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  4                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[\<Sysname\> issu commit slot 1]{lang="EN-US"}

[Copying file flash:/feature.bin to slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 1\...\...\...\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  1                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1329557563}[在双主控板，版本兼容情况下，升级原主用主控板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> issu commit slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_x1361880718}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  0                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1632094407}[在单主控板，版本兼容情况下，确认原主用主控板的升级。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> issu commit slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_1502888622}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1362011790}[在多成员设备，版本兼容情况下，升级原主设备（假设成员编号为]{style="font-family:宋体"}[3]{lang="EN-US"}[）和其他成员（假设成员编号为]{style="font-family:宋体"}[4]{lang="EN-US"}[和]{style="font-family:宋体"}[1]{lang="EN-US"}[）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> issu commit chassis 3]{lang="EN-US"}]{#struct_0_71526_x1155_560302514}

[Copying file flash:/feature.bin to chassis3#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 3 slot 1\...\...\...\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  3         0                 Service Upgrade]{lang="EN-US"}

[  3         1                 Service Upgrade]{lang="EN-US"}

[  3         2                 Service Upgrade]{lang="EN-US"}

[  3         3                 Service Upgrade]{lang="EN-US"}

[  3         4                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[\<Sysname\> issu commit chassis 4]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis4#slot0#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 4 slot 0\...\...\...\.....Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis4#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 4 slot 1\...\...\...\.....Done]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  4         0                 Service Upgrade]{lang="EN-US"}

[  4         1                 Service Upgrade]{lang="EN-US"}

[  4         2                 Service Upgrade]{lang="EN-US"}

[  4         3                 Service Upgrade]{lang="EN-US"}

[  4         4                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[\<Sysname\> issu commit chassis 1]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis1#slot0#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 0\...\...\...\.....Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 1\...\...\...\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         0                 Service Upgrade]{lang="EN-US"}

[  1         1                 Service Upgrade]{lang="EN-US"}

[  1         2                 Service Upgrade]{lang="EN-US"}

[  1         3                 Service Upgrade]{lang="EN-US"}

[  1         4                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1499833880}[在单成员设备双主控板，版本兼容情况下，升级原主用主控板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> issu commit chassis 1 slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_561023410}

[Verifying the file flash:/feature.bin on chassis 1 slot 1\...\...\...\.....Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         0                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_702924494}[在单成员设备单主控板，版本兼容情况下，确认升级。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> issu commit chassis 1 slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_x1789048912}

[[本命令显示信息的描述请参见]{style="font-family:宋体"}]{#struct_0_71526_x1155_323852032}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?270907887#_Ref329853865)[。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_560957874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu accept]{lang="EN-US"}**]{#struct_0_71526_x1155_x1141000154}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x2131569600}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_1028372123}
:::::

::: {#270907887 .myid}
[]{#_Toc404782749}[]{#struct_0_71526_x1155_x234939077}[]{#_Toc329856480}[]{#_Toc299981203}[]{#_Toc299981204}

**ISSU \-- ISSU配置命令 \-- issu load**

------------------------------------------------------------------------

[**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x1501424848}[命令用来升级设备的启动软件包并将设备的主用下次启动软件包设置为指定的软件包。（集中式设备）]{style="font-family:宋体"}

[**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x1300754623}[命令用来升级备用主控板的启动软件包并将备用主控板的主用下次启动软件包设置为指定的软件包。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x837986810}[命令用来升级从设备的启动软件包并将从设备的主用下次启动软件包设置为指定的软件包。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x1352140349}[命令用来升级全局备用主控板的启动软件包并将全局备用主控板的下次启动软件包设置为指定的软件包。（分布式独立设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备）]{style="font-family:宋体"}

[**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_560499123}[命令用来升级从设备的启动软件包并将从设备的主用下次启动软件包设置为指定的软件包。（分布式独立设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式多成员设备）]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1890158202}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1227508810}

[**[issu load file]{lang="EN-US"}**[ { **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \*]{lang="EN-US"}]{#struct_0_71526_x1155_195079540}

[**[issu load file ]{lang="EN-US"}[ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x1026368087}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1270251890}

[**[issu load file ]{lang="EN-US"}**[{ **boot** ]{lang="EN-US"}*[filename]{lang="EN-US"}[ ]{lang="EN-US"}*[\| **system** ]{lang="EN-US"}*[filename]{lang="EN-US"}[ ]{lang="EN-US"}*[\| **feature** ]{lang="EN-US"}*[filename]{lang="EN-US"}*[&\<1-30\> } **\* slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_1580085191}

[**[issu load file ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_293191281}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1180299398}[设备：]{style="font-family:宋体"}

[**[issu load file ]{lang="EN-US"}**[{ **boot** ]{lang="EN-US"}*[filename]{lang="EN-US"}[ ]{lang="EN-US"}*[\| **system** ]{lang="EN-US"}*[filename]{lang="EN-US"}[ ]{lang="EN-US"}*[\| **feature** ]{lang="EN-US"}*[filename]{lang="EN-US"}*[&\<1-30\> } **\* slot** *slot-number*&\<1-9\>]{lang="EN-US"}]{#struct_0_71526_x1155_560433587}

[**[issu load file ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[&\<1-9\>]{lang="EN-US"}]{#struct_0_71526_x1155_x1204594168}

[[分布式独立设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x76665517}[模式单成员设备：]{style="font-family:宋体"}

[**[issu load file ]{lang="EN-US"}**[{ **boot** ]{lang="EN-US"}*[filename]{lang="EN-US"}[ ]{lang="EN-US"}*[\| **system** ]{lang="EN-US"}*[filename]{lang="EN-US"}[ ]{lang="EN-US"}*[\| **feature** ]{lang="EN-US"}*[filename]{lang="EN-US"}*[&\<1-30\> } **\* chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_1857120399}

[**[issu load file ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}***[ chassis ]{lang="EN-US"}***[chassis-number ]{lang="EN-US"}***[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x448191253}

[[分布式独立设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x1961720477}[模式多成员设备：]{style="font-family:宋体"}

[**[issu load file ]{lang="EN-US"}**[{ **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } **\* chassis** *chassis-number*&\<1-3\>]{lang="EN-US"}]{#struct_0_71526_x1155_x2081346525}

[**[issu load file ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}***[ chassis]{lang="EN-US"}**[ *chassis-number*&\<1-3\>]{lang="EN-US"}]{#struct_0_71526_x1155_x1473831990}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_560368051}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1516301396}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x356995569}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1328632863}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_90986950}

[**[boot]{lang="EN-US"}**]{#struct_0_71526_x1155_x387012697}[：表示]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**]{#struct_0_71526_x1155_926964423}[：表示]{style="font-family:宋体"}[System]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**]{#struct_0_71526_x1155_x948550757}[：表示]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_1763905844}[：表示软件包的文件名，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}[&\<1-30\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。（集中式设备）]{style="font-family:宋体"}

[**[ipe]{lang="EN-US"}***[ ]{lang="EN-US"}[ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_560302515}[：]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件名，以]{style="font-family:宋体"}[.ipe]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x1499833879}[：表示备用主控板的槽位号。如果设备只有一块主控板，则输入主用主控板的槽位号，用来完成整个设备的升级。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x1812157708}[：表示从设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[&\<1-9\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[9]{lang="EN-US"}[次。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1207635858}[IRF]{lang="EN-US"}[中只有一个成员设备，则输入该成员设备的编号，用来完成整个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的升级。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_71526_x1155_1360021325}[IRF]{lang="EN-US"}[中有多个成员设备：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当要升级的软件包的版本和设备当前运行的软件包的版本兼容时，只允许输入一个]{style="font-family:宋体"}]{#struct_0_71526_x1155_358448083}*[slot-number]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[当要升级的软件包的版本和设备当前运行的软件包的版本不兼容时，可以输入多个]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1563931754}*[slot-number]{lang="EN-US"}*[，一次升级多个从设备。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}]{#struct_0_71526_x1155_x1842860239}[：如果]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中只有一块主控板，则输入主用主控板所在设备的成员编号以及该主控板所在的槽位号，用来完成整个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的升级；如果设备上有两块主控板，则输入备用主控板所在设备的成员编号以及备用主控板所在的槽位号。（分布式独立设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x607448294}[：表示从设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[&\<1-3\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[3]{lang="EN-US"}[次。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式多成员设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当要升级的软件包的版本和设备当前运行的软件包的版本兼容时，只允许输入一个]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1160647227}*[chassis-number]{lang="EN-US"}*[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当要升级的软件包的版本和设备当前运行的软件包的版本不兼容时，可以输入多个]{style="font-family:宋体"}]{#struct_0_71526_x1155_1971520655}*[chassis-number]{lang="EN-US"}*[，一次升级多个成员设备。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_596481602}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式设备]{lang="EN-US" style="font-family:宋体"}]{#struct_0_71526_x1155_x1376781052}

[[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}[/IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x1613754897}[文件必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}]{#struct_0_71526_x1155_707835360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。]{style="font-family:宋体"}]{#struct_0_71526_x1155_560761267}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级会对]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1697109384}[CPU]{lang="EN-US"}[进行重启升级；重启升级会自动重启设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[按照升级策略进行升级，并将设备主用下次启动软件包设置为]{style="font-family:宋体"}]{#struct_0_71526_x1155_x2075157177}**[issu load]{lang="EN-US"}**[命令中指定的包，以便指定的包在设备重启后能够继续生效。增量升级方式时是升级前进行设置，软重启和重启升级方式时是升级后进行设置。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_71526_x1155_476173906}

[[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}[/IPE]{lang="EN-US"}]{#struct_0_71526_x1155_1116606194}[文件必须放在主用主控板存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[slot]{lang="EN-US"}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[当设备上有两块主控板时，]{style="font-family:宋体"}**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_558820896}[请指定为备用主控板的槽位号。输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行版本兼容性检查。分为兼容版本的升级和不兼容版本的升级。]{style="font-family:宋体"}]{#struct_0_71526_x1155_2128593361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级会对]{style="font-family:宋体"}]{#struct_0_71526_x1155_1893172565}[CPU]{lang="EN-US"}[进行重启升级；重启升级会自动重启指定主控板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[按照升级策略进行升级备用主控板，并将备用主控板的主用下次启动软件包设置为]{style="font-family:宋体"}]{#struct_0_71526_x1155_560695731}[issu load]{lang="EN-US"}[命令中指定的包。]{style="font-family:宋体"}

[[当设备上只有一块主控板时，]{style="font-family:宋体"}**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_71526_x1155_x2139918418}[指定为主用主控板的槽位号。输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。]{style="font-family:宋体"}]{#struct_0_71526_x1155_220490540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级会对]{style="font-family:宋体"}]{#struct_0_71526_x1155_1368415527}[CPU]{lang="EN-US"}[进行重启升级；重启升级会以指定的软件包为下次启动软件包自动重启设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[按照升级策略进行升级主用主控板，并将主用主控板的主用下次启动软件包设置为]{style="font-family:宋体"}]{#struct_0_71526_x1155_1983158865}[issu load]{lang="EN-US"}[命令中指定的包。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1455805053}[设备]{lang="EN-US" style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}[/IPE]{lang="EN-US"}]{#struct_0_71526_x1155_468245765}[文件必须放在主设备存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[slot]{lang="EN-US"}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过]{style="font-family:宋体"}**[display device]{lang="EN-US"}**]{#struct_0_71526_x1155_1070383302}[[、]{style="font-family:宋体"}]{.ItemListCharChar}**[display mdc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[[命令]{style="font-family:
宋体"}]{.ItemListCharChar}[查看到所有单板处于]{style="font-family:宋体"}[normal]{lang="EN-US"}[状态、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态和所有服务的]{style="font-family:宋体"}[action]{lang="EN-US"}[显示为]{style="font-family:宋体"}[0]{lang="EN-US"}[后，再执行]{style="font-family:宋体"}**[issu load]{lang="EN-US"}**[命令，否则，命令会执行失败。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_284338629}[中只有一个成员设备时，]{style="font-family:宋体"}**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[请指定为该设备的成员编号。输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。]{style="font-family:宋体"}]{#struct_0_71526_x1155_560630195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级会对]{style="font-family:宋体"}]{#struct_0_71526_x1155_x930248802}[CPU]{lang="EN-US"}[进行重启升级；重启升级会自动重启对应的成员设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[按照升级策略进行升级，并将该成员设备的主用下次启动软件包设置为]{style="font-family:宋体"}]{#struct_0_71526_x1155_x417954103}**[issu load]{lang="EN-US"}**[命令中指定的包。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_2054137198}[中有多个成员设备时，可一次指定一个或者多个]{style="font-family:宋体"}**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[，]{style="font-family:宋体"}**[slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*[均应为从设备的成员编号。如果]{style="font-family:宋体"}[IRF]{lang="EN-US"}[为环形连接，建议一次升级一半数量的物理上邻接的成员设备（也称为对半升级），以便尽量减少升级对整个]{style="font-family:宋体"}[IRF]{lang="EN-US"}[业务的影响。输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。]{style="font-family:宋体"}]{#struct_0_71526_x1155_1138878457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级对]{style="font-family:宋体"}]{#struct_0_71526_x1155_1248245998}[CPU]{lang="EN-US"}[进行重启升级；重启升级会自动重启对应的成员设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[按照升级策略进行升级从设备，并将指定成员设备的主用下次启动软件包设置为]{style="font-family:宋体"}]{#struct_0_71526_x1155_116778558}**[issu load]{lang="EN-US"}**[命令中指定的包。]{style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_71526_x1155_1915853418}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}[/IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x768301493}[文件必须放在全局主用主控板存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含]{style="font-family:宋体"}[chassis]{lang="EN-US"}[和]{style="font-family:宋体"}[slot]{lang="EN-US"}[的信息，形如]{style="font-family:宋体"}[flash:/xx.bin]{lang="EN-US"}[（]{style="font-family:宋体"}[flash:/xx.ipe]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过]{style="font-family:宋体"}**[display device]{lang="EN-US"}**]{#struct_0_71526_x1155_560564659}[[、]{style="font-family:宋体"}]{.ItemListCharChar}**[display mdc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[[命令]{style="font-family:
宋体"}]{.ItemListCharChar}[查看到所有单板处于]{style="font-family:宋体"}[normal]{lang="EN-US"}[状态、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态和所有服务的]{style="font-family:宋体"}[action]{lang="EN-US"}[显示为]{style="font-family:宋体"}[0]{lang="EN-US"}[后，再执行]{style="font-family:宋体"}**[issu load]{lang="EN-US"}**[命令，否则，命令会执行失败。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x59769638}[中只有一个成员设备且只有一块主控板时，]{style="font-family:宋体"}**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}[请指定为主用主控板所在的槽位号。输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1470951516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级对]{style="font-family:宋体"}]{#struct_0_71526_x1155_1632273118}[CPU]{lang="EN-US"}[进行重启升级；重启升级会自动重启主用主控板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[按照升级策略进行升级主用主控板，并将主用主控板的主用下次启动软件包设置为]{style="font-family:宋体"}]{#struct_0_71526_x1155_1098746360}**[issu load]{lang="EN-US"}**[命令中指定的包。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x765312632}[中只有一个成员设备且有两块主控板时，]{style="font-family:宋体"}**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[ **slot** *slot-number*]{lang="EN-US"}[请指定为备用主控板所在的槽位号。输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。]{style="font-family:宋体"}]{#struct_0_71526_x1155_1592461877}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级对]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1160060020}[CPU]{lang="EN-US"}[进行重启升级；重启升级会自动重启备用主控板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[按照升级策略进行升级备用主控板，并将备用主控板的主用下次启动软件包设置为]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1408029989}**[issu load]{lang="EN-US"}**[命令中指定的包。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_561023411}[中有多个成员设备时，]{style="font-family:宋体"}**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*[请指定为从设备的成员编号。输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。]{style="font-family:宋体"}]{#struct_0_71526_x1155_702924495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级对]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1789048913}[CPU]{lang="EN-US"}[进行重启升级；重启升级会自动重启对应的成员设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[按照升级策略进行升级从设备，并将从设备的主用下次启动软件包设置为]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1242231909}**[issu load]{lang="EN-US"}**[命令中指定的包**。**]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x239682798}

[**[\# ]{lang="EN-US"}**]{#struct_0_71526_x1155_560564656}[版本兼容情况下，使用]{style="font-family:宋体"}[flash:/boot.bin]{lang="EN-US"}[升级]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包，使用]{style="font-family:宋体"}[flash:/system.bin]{lang="EN-US"}[升级]{style="font-family:宋体"}[System]{lang="EN-US"}[包，使用]{style="font-family:宋体"}[flash:/ssh.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[flash:/http.bin]{lang="EN-US"}[升级]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> issu load file boot flash:/boot.bin system flash:/system.bin feature flash:/ssh.bin flash:/http.bin]{lang="EN-US"}]{#struct_0_71526_x1155_560695726}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/boot.bin on the device\...Done.]{lang="EN-US"}

[Verifying the file flash:/system.bin on the device\...Done.]{lang="EN-US"}

[Verifying the file flash:/ssh.bin on the device\...Done.]{lang="EN-US"}

[Verifying the file flash:/http.bin on the device\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/boot.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  1.0.2                       1.0.3]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/system.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/ssh.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  None                        Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/http.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  None                        Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[Upgrade Way: Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_560761263}[版本不兼容情况下，使用]{style="font-family:宋体"}[flash:/boot.bin]{lang="EN-US"}[升级]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包，使用]{style="font-family:宋体"}[flash:/system.bin]{lang="EN-US"}[升级]{style="font-family:宋体"}[System]{lang="EN-US"}[包，使用]{style="font-family:宋体"}[flash:/ssh.bin]{lang="EN-US"}[和]{style="font-family:宋体"}[flash:/http.bin]{lang="EN-US"}[升级]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> issu load file boot flash:/boot.bin system flash:/system.bin feature flash:/ssh.bin flash:/http.bin]{lang="EN-US"}]{#struct_0_71526_x1155_2126845208}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/boot.bin on the device\...Done.]{lang="EN-US"}

[Verifying the file flash:/system.bin on the device\...Done.]{lang="EN-US"}

[Verifying the file flash:/ssh.bin on the device\...Done.]{lang="EN-US"}

[Verifying the file flash:/http.bin on the device\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/boot.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  1.0.2                       1.0.3]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/system.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/ssh.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  None                        Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/http.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  None                        Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[Upgrade Way: Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_2127041816}[版本兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级从设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu load file feature flash:/feature.bin slot 2]{lang="EN-US"}]{#struct_0_71526_x1155_2126779669}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 1\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to slot2#flash:/feature.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 2\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  2                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_2126517526}[版本不兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级从设备]{style="font-family:宋体"}[3]{lang="EN-US"}[和]{style="font-family:宋体"}[4]{lang="EN-US"}[上的]{style="font-family:
宋体"}[Feature]{lang="EN-US"}[包。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu load file feature flash:/feature.bin slot 3 4]{lang="EN-US"}]{#struct_0_71526_x1155_2127107350}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 1\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to slot3#flash:/feature.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 3\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to slot4#flash:/feature.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 4\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  3                           Reboot]{lang="EN-US"}

[  4                           Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_2126386451}[版本兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级备用主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－独立运行模式双主控）]{style="font-family:宋体"}

[[\<Sysname\> issu load file feature flash:/feature.bin slot 1]{lang="EN-US"}]{#struct_0_71526_x1155_2126583060}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to slot1#flash:/feature.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 1\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  1                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_2126714132}[版本不兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级备用主控板]{style="font-family:宋体"}[1]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－独立运行模式双主控）]{style="font-family:宋体"}

[[\<Sysname\> issu load file feature flash:/feature.bin slot 1]{lang="EN-US"}]{#struct_0_71526_x1155_210822362}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to slot1#flash:/feature.bin\...\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 1\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  1                           Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_210494682}[版本兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级]{style="font-family:宋体"}[slot 0]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－独立运行模式单主控）]{style="font-family:宋体"}

[[\<Sysname\>issu load file feature flash:/feature.bin slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_210756827}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 0\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  0                           Service Upgrade]{lang="EN-US"}

[  2                           Service Upgrade]{lang="EN-US"}

[  3                           Service Upgrade]{lang="EN-US"}

[  4                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_210429147}[版本不兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级主用主控板]{style="font-family:宋体"}[slot 0]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－独立运行模式单主控）]{style="font-family:宋体"}

[[\<Sysname\> issu load file feature flash:/feature.bin slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_210756824}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 0\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  0                           Reboot]{lang="EN-US"}

[  2                           Reboot]{lang="EN-US"}

[  3                           Reboot]{lang="EN-US"}

[  4                           Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_210429144}[版本兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级成员]{style="font-family:宋体"}[2]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式多成员设备）]{style="font-family:宋体"}

[[\<Sysname\> issu load file feature flash:/feature.bin chassis 2]{lang="EN-US"}]{#struct_0_71526_x1155_210822361}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis2#slot0#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 2 slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis2#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 2 slot 1\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  2         0                 Service Upgrade]{lang="EN-US"}

[  2         1                 Service Upgrade]{lang="EN-US"}

[  2         2                 Service Upgrade]{lang="EN-US"}

[  2         3                 Service Upgrade]{lang="EN-US"}

[  2         4                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_210756822}[版本不兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级从设备]{style="font-family:宋体"}[3]{lang="EN-US"}[和从设备]{style="font-family:宋体"}[4]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式多成员设备）]{style="font-family:宋体"}

[[\<Sysname\>issu load file feature flash:/feature.bin chassis 3 4]{lang="EN-US"}]{#struct_0_71526_x1155_210625751}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis3#slot0#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 3 slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis3#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 3 slot 1\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis4#slot0#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 4 slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis4#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 4 slot 1\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  3         0                 Reboot]{lang="EN-US"}

[  3         1                 Reboot]{lang="EN-US"}

[  3         2                 Reboot]{lang="EN-US"}

[  3         3                 Reboot]{lang="EN-US"}

[  3         4                 Reboot]{lang="EN-US"}

[  4         0                 Reboot]{lang="EN-US"}

[  4         1                 Reboot]{lang="EN-US"}

[  4         2                 Reboot]{lang="EN-US"}

[  4         3                 Reboot]{lang="EN-US"}

[  4         4                 Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_210363607}[版本兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的备用主控板]{style="font-family:宋体"}[slot 1]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备双主控）]{style="font-family:宋体"}

[[\<Sysname\>issu load file feature flash:/feature.bin chassis 1 slot 1]{lang="EN-US"}]{#struct_0_71526_x1155_1776840767}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 1\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         1                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1776513087}[版本不兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的备用主控板]{style="font-family:宋体"}[slot 1]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备双主控）]{style="font-family:宋体"}

[[\<Sysname\>issu load file feature flash:/feature.bin chassis 1 slot 1]{lang="EN-US"}]{#struct_0_71526_x1155_1776447552}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 1\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         1                 Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1776644160}[版本兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的主用主控板]{style="font-family:宋体"}[slot0]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备单主控）]{style="font-family:宋体"}

[[\<Sysname\>issu load file feature flash:/feature.bin chassis 1 slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_1776447549}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         0                 Service Upgrade]{lang="EN-US"}

[  1         2                 Service Upgrade]{lang="EN-US"}

[  1         3                 Service Upgrade]{lang="EN-US"}

[  1         4                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1777233981}[版本不兼容情况下，使用]{style="font-family:宋体"}[flash:/feature.bin]{lang="EN-US"}[升级成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的主用主控板]{style="font-family:宋体"}[slot0]{lang="EN-US"}[上的]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备单主控）]{style="font-family:宋体"}

[[\<Sysname\>issu load file feature flash:/feature.bin chassis 1 slot 0]{lang="EN-US"}]{#struct_0_71526_x1155_1776513086}

[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]:Y]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         0                 Reboot]{lang="EN-US"}

[  1         2                 Reboot]{lang="EN-US"}

[  1         3                 Reboot]{lang="EN-US"}

[  1         4                 Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[]{#struct_0_71526_x1155_x1495422714}[[表1-8 ]{lang="EN-US"}[issu load]{lang="EN-US"}]{#_Ref329853865}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1075937758}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_x754525823}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_2093132644}

[[This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? \[Y/N\]]{lang="EN-US"}]{#struct_0_71526_x1155_1776578622}

[[当前操作会删除上一次]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_850562957}[升级的日志信息和回滚点，并且未保存的配置可能会丢失，询问用户是否继续执行升级操作]{style="font-family:宋体"}

[[Verifying the file flash:/xx.bin on chassis 1 slot 0\...\...\...\...\...\...\...\...\...\...\....Done.]{lang="EN-US"}]{#struct_0_71526_x1155_1777299518}

[[验证文件是否合法]{style="font-family:宋体"}]{#struct_0_71526_x1155_1776906299}

[[Decompressing file *A* to *B*\...\...\...\...\...\...\...\...\...Done.]{lang="EN-US"}]{#struct_0_71526_x1155_1776709692}

[[将文件从位置]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_71526_x1155_1776906300}[解压缩到位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*[。只有使用]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件升级时，才显示该信息]{style="font-family:宋体"}

[[Copying file *B* to *C*\...\...Done.]{lang="EN-US"}]{#struct_0_71526_x1155_1776644156}

[[将文件从位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*]{#struct_0_71526_x1155_x952173660}[拷贝到位置]{style="font-family:宋体"}*[C]{lang="EN-US"}*[。当配置备用主控板时才有该提示信息（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[将文件从位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*]{#struct_0_71526_x1155_x952435804}[拷贝到位置]{style="font-family:宋体"}*[C]{lang="EN-US"}*[。当配置从设备时才有该提示信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[将文件从位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*]{#struct_0_71526_x1155_x952239196}[拷贝到位置]{style="font-family:宋体"}*[C]{lang="EN-US"}*[。当配置全局备用主控板时才有该提示信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Upgrade summary according to following table]{lang="EN-US"}]{#struct_0_71526_x1155_x951649372}

[[升级信息摘要]{style="font-family:宋体"}]{#struct_0_71526_x1155_1222845193}

[[Running Version]{lang="EN-US"}]{#struct_0_71526_x1155_2030621966}

[[设备当前运行的相同类型软件包的产品版本号]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1447324605}

[[New Version]{lang="EN-US"}]{#struct_0_71526_x1155_1939236131}

[[将要升级的软件包的产品版本号]{style="font-family:宋体"}]{#struct_0_71526_x1155_x951583836}

[[Chassis]{lang="EN-US"}]{#struct_0_71526_x1155_154899608}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_580028180}[中的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_71526_x1155_1169983427}

[[单板所在的槽位号（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_x601837452}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x952173659}[中的成员编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Upgrade Way]{lang="EN-US"}]{#struct_0_71526_x1155_767464498}

[[升级策略，取值可能为：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1135678274}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service Upgrade]{lang="EN-US"}]{#struct_0_71526_x1155_1499661148}[：表示服务级增量升级，该方式下，仅对本业务模块有影响，对系统以及其他业务模块没有影响]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[File Upgrade]{lang="EN-US"}]{#struct_0_71526_x1155_x952108123}[：表示文件级增量升级。该方式下，仅对系统内的、用户不可见的程序文件进行升级，对系统以及业务模块没有影响]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISSU Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_x852846884}[：表示通过软重启方式升级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_227489651}[：表示通过重启方式升级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sequence Reboot]{lang="EN-US"}]{#struct_0_71526_x1155_x952042587}[：表示逐次重启方式。只有网板支持该升级方式，当网板需要重启升级时，为了避免重启升级过程中流量中断，系统会自动升级完毕一块网板后，再自动升级下一块网板，直到所有网板升级完毕后，再自动升级主控板。该字段的支持情况与网板的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Upgrading software images to compatible versions. Continue? \[Y/N\]]{lang="EN-US"}]{#struct_0_71526_x1155_1151600743}

[[询问用户是否执行兼容升级操作]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1952963381}

[[Upgrading software images to incompatible versions. Continue? \[Y/N\]]{lang="EN-US"}]{#struct_0_71526_x1155_1096589767}

[[询问用户是否执行不兼容升级操作]{style="font-family:宋体"}]{#struct_0_71526_x1155_x951977051}

[ ]{lang="EN-US"}

::::: {#-1689372881 .myid}
[]{#_Toc404782750}[]{#struct_0_71526_x1155_x1678811534}[]{#_Toc351014179}[]{#_Toc360430876}[]{#_Toc340215437}

**ISSU \-- ISSU配置命令 \-- issu pex**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ISSU命令.files/image002.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_71526_x1155_x1678811533}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_71526_x1155_x2025463003}
:::

**[ ]{lang="EN-US"}**

[**[issu pex]{lang="EN-US"}**]{#struct_0_71526_x1155_x1678811536}[命令用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1622178476}

[**[issu pex ]{lang="EN-US"}***[pex-model]{lang="EN-US"}***[ file ]{lang="EN-US"}**[{ **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } **\***]{lang="EN-US"}]{#struct_0_71526_x1155_350125698}

[**[issu pex ]{lang="EN-US"}***[pex-model]{lang="EN-US"}***[ file ipe ]{lang="EN-US"}***[ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x1678811535}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1218893949}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1678811538}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x815609422}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x1678811537}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x56094535}

[*[pex-model]{lang="EN-US"}*]{#struct_0_71526_x1155_x1678811540}[：设备支持的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的型号，该参数必须完整输入，不区分大小写。可输入]{style="font-family:宋体"}**[boot-loader pex ]{lang="EN-US"}[？]{style="font-family:宋体"}**[，回车，来获取该参数的取值。]{style="font-family:宋体"}

[**[boot]{lang="EN-US"}**]{#struct_0_71526_x1155_x459051382}[：表示]{style="font-family:宋体"}[Boot]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[system]{lang="EN-US"}**]{#struct_0_71526_x1155_x1678811539}[：表示]{style="font-family:宋体"}[System]{lang="EN-US"}[包。]{style="font-family:宋体"}

[**[feature]{lang="EN-US"}**]{#struct_0_71526_x1155_750474519}[：表示]{style="font-family:宋体"}[Feature]{lang="EN-US"}[包。]{style="font-family:宋体"}

[*[filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x1696444260}[：表示软件包的文件名，以]{style="font-family:宋体"}[.bin]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}[&\<1-30\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[30]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[ipe]{lang="EN-US"}***[ ipe-filename]{lang="EN-US"}*]{#struct_0_71526_x1155_x1678811542}[：]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件名，以]{style="font-family:宋体"}[.ipe]{lang="EN-US"}[作为后缀名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_703748032}

[[该命令只是指定]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_71526_x1155_x1678811541}[设备的升级软件包，并不执行升级动作，而是等主控板升级时，]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备使用这些升级软件包启动来完成升级。组网环境不同，]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的具体升级时机不同，具体描述请参见"基础配置指导"中的"]{style="font-family:宋体"}[ISSU]{lang="EN-US"}["。如果不进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级，而仅仅是重启]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备，该命令配置的软件包将不会生效。]{style="font-family:宋体"}

[[当配置该命令时，命令中指定的软件包]{style="font-family:宋体"}[/IPE]{lang="EN-US"}]{#struct_0_71526_x1155_x2070225967}[文件必须放在存储介质主分区的根目录下。]{style="font-family:宋体"}

[[对于本地无存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_71526_x1155_608314116}[设备，输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行命令行合法性检查。]{style="font-family:宋体"}]{#struct_0_71526_x1155_608379652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将升级文件全部拷贝到系统中所有的主控板上。如果指定的是]{style="font-family:宋体"}]{#struct_0_71526_x1155_x2069767215}[IPE]{lang="EN-US"}[文件，那么会自动解压到所有主控板上。]{style="font-family:宋体"}

[[对于本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}]{#struct_0_71526_x1155_x1605932402}[设备，输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行命令行合法性检查。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1053679595}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将升级文件全部拷贝到系统中所有的主控板和该类型的]{style="font-family:宋体"}]{#struct_0_71526_x1155_x2069832751}[PEX]{lang="EN-US"}[设备上。如果指定的是]{style="font-family:宋体"}[IPE]{lang="EN-US"}[文件，则会自动解压到所有该类型的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备上。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[拷贝完成后，提示用户是否需要删除源软件包。如果用户确认，则自动删除源软件包，以便释放空间。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1162363464}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_701244280}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x2070357040}[指定型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包为]{style="font-family:宋体"}[flash:/devkit.bin]{lang="EN-US"}[（本地无存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备）。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file feature flash:/devkit.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x2070422576}

[Verifying the file flash:/devkit.bin on slot 1\...Done.]{lang="EN-US"}

[File flash:/devkit.bin already exists on slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/devkit.bin to slot1#flash:/devkit.bin\...Done.]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1658709735}[指定型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包为]{style="font-family:宋体"}[flash:/devkit.bin]{lang="EN-US"}[（本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备）。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5500 file feature flash:/devkit.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x2070488112}

[Verifying the file flash:/devkit.bin on slot 1\...Done.]{lang="EN-US"}

[File flash:/devkit.bin already exists on slot 110.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/devkit.bin to slot110#flash:/devkit.bin\...Done.]{lang="EN-US"}

[Delete flash:/devkit.bin from slot 1? \[Y/N\]:Y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x114136853}[指定型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包为]{style="font-family:宋体"}[flash:/test.ipe]{lang="EN-US"}[（本地无存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备）。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file ipe flash:/test.ipe]{lang="EN-US"}]{#struct_0_71526_x1155_x2070029360}

[Verifying the file flash:/test.ipe on slot 1\...\...\...\...Done.]{lang="EN-US"}

[File flash:/devkit.bin already exists on slot 1.]{lang="EN-US"}

[File flash:/manufacture.bin already exists on slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file devkit.bin to flash:/devkit.bin. \.....Done.]{lang="EN-US"}

[Decompressing file manufacture.bin to flash:/manufacture.bin\.....Done.]{lang="EN-US"}

[File flash:/devkit.bin already exists on slot 2.]{lang="EN-US"}

[File flash:/manufacture.bin already exists on slot 2.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/devkit.bin to slot2#flash:/devkit.bin. \...Done.]{lang="EN-US"}

[Copying file flash:/manufacture.bin to slot2#flash:/manufacture.bin\....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x2070094896}[指定型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包为]{style="font-family:宋体"}[flash:/test.ipe]{lang="EN-US"}[（本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备）。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file ipe flash:/test.ipe]{lang="EN-US"}]{#struct_0_71526_x1155_1883751731}

[Verifying the file flash:/test.ipe on slot 1\...\...\.....Done.]{lang="EN-US"}

[Decompressing file devkit-patch.bin to flash:/devkit-patch.bin\...Done.]{lang="EN-US"}

[Decompressing file manufacture.bin to flash:/manufacture.bin\.....Done.]{lang="EN-US"}

[Copying file flash:/devkit-patch.bin to slot110#flash:/devkit-patch.bin\...Done.]{lang="EN-US"}

[Copying file flash:/manufacture.bin to slot110#flash:/manufacture.bin\...Done.]{lang="EN-US"}

[Delete flash:/devkit-patch.bin from slot 1? \[Y/N\]:Y]{lang="EN-US"}

[Delete flash:/manufacture.bin from slot 1? \[Y/N\]:Y]{lang="EN-US"}

[Delete flash:/test.ipe from slot 1? \[Y/N\]:Y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x2070160432}[指定型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包为]{style="font-family:宋体"}[flash:/devkit.bin]{lang="EN-US"}[（本地无存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file feature flash:/devkit.bin]{lang="EN-US"}]{#struct_0_71526_x1155_x158790798}

[Verifying the file flash:/devkit.bin on chassis 1 slot 0\...\...\...\...Done.]{lang="EN-US"}

[File flash:/devkit.bin already exists on chassis 1 slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/devkit.bin to chassis1#slot1#flash:/devkit.bin\...Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x2070225968}[指定型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包为]{style="font-family:宋体"}[flash:/devkit.bin]{lang="EN-US"}[（本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file feature flash:/devkit.bin]{lang="EN-US"}]{#struct_0_71526_x1155_275293987}

[Verifying the file flash:/devkit.bin on chassis 1 slot 0\...\...\...\...Done.]{lang="EN-US"}

[File flash:/devkit.bin already exists on chassis 101 slot 0.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/devkit.bin to chassis101#slot0#flash:/devkit.bin\...Done.]{lang="EN-US"}

[Delete flash:/devkit.bin from chassis 1 slot 1? \[Y/N\]:Y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x2069767216}[指定型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包为]{style="font-family:宋体"}[flash:/test.ipe]{lang="EN-US"}[（本地无存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file ipe flash:/test.ipe]{lang="EN-US"}]{#struct_0_71526_x1155_1122950953}

[Verifying the file flash:/test.ipe on chassis 1 slot 0\...\...\...\...Done.]{lang="EN-US"}

[File flash:/devkit.bin already exists on chassis 1 slot 0.]{lang="EN-US"}

[File flash:/manufacture.bin already exists on chassis 1 slot 0.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Decompressing file devkit.bin to flash:/devkit.bin. \.....Done.]{lang="EN-US"}

[Decompressing file manufacture.bin to flash:/manufacture.bin\.....Done.]{lang="EN-US"}

[File flash:/devkit.bin already exists on chassis 1 slot 1.]{lang="EN-US"}

[File flash:/manufacture.bin already exists on chassis 1 slot 1.]{lang="EN-US"}

[Overwrite the existing files? \[Y/N\]:Y]{lang="EN-US"}

[Copying file flash:/devkit.bin to chasis1#slot1#flash:/devkit.bin. \...Done.]{lang="EN-US"}

[Copying file flash:/manufacture.bin to chassis1#slot1#flash:/manufacture.bin\....Done.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x2069832752}[指定型号为]{style="font-family:宋体"}[PEX-S5120HI]{lang="EN-US"}[的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备的升级软件包为]{style="font-family:宋体"}[flash:/test.ipe]{lang="EN-US"}[（本地有存储介质的]{style="font-family:宋体"}[PEX]{lang="EN-US"}[设备）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> issu pex PEX-S5120HI file ipe flash:/test.ipe]{lang="EN-US"}]{#struct_0_71526_x1155_x2070291505}

[Verifying the file flash:/test.ipe on chassis 1 slot 0\...\...\...\...Done.]{lang="EN-US"}

[Decompressing file devkit.bin to flash:/devkit.bin\...Done.]{lang="EN-US"}

[Decompressing file manufacture.bin to flash:/manufacture.bin\.....Done.]{lang="EN-US"}

[Copying file flash:/devkit.bin to chassis101#slot0#flash:/devkit.bin\...Done.]{lang="EN-US"}

[Copying file flash:/manufacture.bin to chassis101#slot0#flash:/manufacture.bin\...Done.]{lang="EN-US"}

[Delete flash:/devkit.bin from chassis 1 slot 1? \[Y/N\]:Y]{lang="EN-US"}

[Delete flash:/manufacture.bin from chassis 1 slot 1? \[Y/N\]:Y]{lang="EN-US"}

[Delete flash:/test.ipe from chassis 1 slot 1? \[Y/N\]:Y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1469144685}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[i]{lang="EN-US"}[ssu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x1835325935}
:::::

::::: {#-1621319551 .myid}
[]{#_Toc404782751}[]{#struct_0_71526_x1155_x659045714}[]{#_Toc329856484}[]{#_Toc315975329}

**ISSU \-- ISSU配置命令 \-- issu rollback**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ISSU命令.files/image001.png){#图片 7 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_71526_x1155_x1520522594}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_71526_x1155_818906663}
:::

[ ]{lang="EN-US"}

[**[issu rollback]{lang="EN-US"}**]{#struct_0_71526_x1155_462453296}[命令用来回滚到升级前的版本。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1255016507}

[**[issu ]{lang="EN-US"}**]{#struct_0_71526_x1155_x952435803}**[rollback]{lang="EN-US"}**

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1535399038}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_591541392}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1099983146}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_569308571}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1556260218}

[[设备支持自动回滚和手动回滚，自动回滚定时器的时长由]{style="font-family:宋体"}**[issu rollback-timer]{lang="EN-US"}**]{#struct_0_71526_x1155_x952370267}[命令配置；手工回滚由]{style="font-family:宋体"}**[issu ]{lang="EN-US"}[rollback]{lang="EN-US"}**[命令触发。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不兼容版本升级时，不会启动回滚定时器，即不支持自动回滚。兼容版本只有执行]{style="font-family:宋体"}]{#struct_0_71526_x1155_1128985134}**[issu run switchover]{lang="EN-US"}**[命令时才会创建回滚定时器，因此，自动回滚只有在兼容版本]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[升级状态为]{style="font-family:宋体"}[Swtiching]{lang="EN-US"}[后才生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单主控兼容升级不支持自动回滚。（分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1206201113}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_71526_x1155_x833990727}[ISSU]{lang="EN-US"}[升级状态为]{style="font-family:宋体"}[Loading]{lang="EN-US"}[时进行手工回滚，可能会回滚失败。回滚操作结束后，请使用]{style="font-family:宋体"}**[display version]{lang="EN-US"}**[命令来查看设备当前运行的版本，验证回滚结果。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_x952304731}[升级状态为]{lang="EN-US" style="font-family:宋体"}[Loaded]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Accepted]{lang="EN-US"}[时，支持手工回滚。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[兼容升级、]{lang="EN-US" style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_378085311}[升级状态为]{lang="EN-US" style="font-family:宋体"}[Switching]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Switchover]{lang="EN-US"}[时，支持手工回滚。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不兼容升级、]{style="font-family:宋体"}]{#struct_0_71526_x1155_966588653}[ISSU]{lang="EN-US"}[升级状态为]{style="font-family:宋体"}[Switching]{lang="EN-US"}[时，不支持手工回滚。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不管兼容升级还是不兼容升级，]{style="font-family:宋体"}]{#struct_0_71526_x1155_1702126176}[Switching]{lang="EN-US"}[状态时如果进行手工回滚或者发生自动回滚，整个系统是会重启。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_71526_x1155_1392913920}[ISSU]{lang="EN-US"}[升级状态为]{style="font-family:宋体"}[Commiting]{lang="EN-US"}[时，不允许进行手工和自动回滚操作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多成员设备的情况下，执行]{style="font-family:宋体"}]{#struct_0_71526_x1155_139262387}**[issu run switchover]{lang="EN-US"}**[后，再进行回滚操作，回滚保证版本回到升级前，并且主备状态也会和升级前一致。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多成员设备的情况下，执行]{style="font-family:宋体"}]{#struct_0_71526_x1155_2094463635}**[issu run switchover]{lang="EN-US"}**[后，再进行回滚操作，回滚只保证版本回到升级前，但不能保证主备状态和升级前一致。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_325644002}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_842669329}[回滚到升级之前的版本。]{style="font-family:宋体"}

[[\<Sysname\> issu rollback]{lang="EN-US"}]{#struct_0_71526_x1155_x952239195}

[This command will quit the ISSU process and roll back to the previous version. Continue? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_719856155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu accept]{lang="EN-US"}**]{#struct_0_71526_x1155_x952972818}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu commit]{lang="EN-US"}**]{#struct_0_71526_x1155_x1945564743}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_197066785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_x573801529}
:::::

::::: {#-390052592 .myid}
[]{#_Toc404782752}[]{#struct_0_71526_x1155_460754537}[]{#_Toc329856485}[]{#_Toc315975328}[]{#_Toc304800260}[]{#_Toc304813530}[]{#_Toc299981207}[]{#_Toc299981210}[]{#_Toc299981212}[]{#_Toc299981213}

**ISSU \-- ISSU配置命令 \-- issu rollback-timer**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ISSU命令.files/image001.png){#图片 8 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_71526_x1155_x951583835}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_71526_x1155_155096216}
:::

[ ]{lang="EN-US"}

[**[issu rollback-timer]{lang="EN-US"}**]{#struct_0_71526_x1155_884292281}[命令用来设置回滚定时器时长。]{style="font-family:宋体"}

[**[undo issu rollback-timer]{lang="EN-US"}**]{#struct_0_71526_x1155_1254782287}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x952173662}

[**[issu]{lang="EN-US"}**[ **rollback-timer** *minutes*]{lang="EN-US"}]{#struct_0_71526_x1155_767923247}

[**[undo issu rollback-timer]{lang="EN-US"}**]{#struct_0_71526_x1155_2070217851}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x860262584}

[[回滚定时器的时长为]{style="font-family:宋体"}[45]{lang="EN-US"}]{#struct_0_71526_x1155_1828653520}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2057465491}

[[系统视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_752719838}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2123055334}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x952108126}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x852650276}

[*[minutes]{lang="EN-US"}*]{#struct_0_71526_x1155_1337520844}[：回滚定时器的时长，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为分钟。如果时长设置为]{style="font-family:宋体"}[0]{lang="EN-US"}[，则表示关闭自动回滚功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1059187596}

[[兼容版本升级的情况下，执行]{style="font-family:宋体"}**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_1944819654}[命令后系统会自动启动回滚定时器。如果在指定的时间内（回滚定时器超时前）未执行]{style="font-family:宋体"}**[issu accept]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[issu commit]{lang="EN-US"}**[命令，则系统会自动回滚到升级前的版本。]{style="font-family:宋体"}

[[设备进行升级时，不会启动回滚定时器。（集中式设备）]{style="font-family:宋体"}]{#struct_0_71526_x1155_2105410703}

[[当系统中只配备了一块主控板并进行升级时，不会启动回滚定时器。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_71526_x1155_942611289}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[当系统中只有一台成员设备并进行升级时，不会启动回滚定时器。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x1073811346}[设备）]{style="font-family:宋体"}

[[不兼容升级不会启动回滚定时器。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1114088380}

[[新设置的时长会在下次]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_71526_x1155_x952042590}[升级中生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1151928422}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_364103872}[设置回滚定时器时长为]{style="font-family:宋体"}[50]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_71526_x1155_1179246633}

[\[Sysname\] issu rollback-timer 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_689565928}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu rollback]{lang="EN-US"}**]{#struct_0_71526_x1155_x1873338233}
:::::

::::: {#-1869046052 .myid}
[]{#_Toc404782753}[]{#struct_0_71526_x1155_507369303}[]{#_Toc329856481}

**ISSU \-- ISSU配置命令 \-- issu run switchover**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ISSU命令.files/image001.png){#图片 4 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_71526_x1155_x621045407}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_71526_x1155_x951977054}
:::

[ ]{lang="EN-US"}

[[分布式设备－独立运行模式：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x659242322}

[**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_x1159264082}[命令在升级兼容软件包的情况下，用来进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[倒换，并且升级业务板和网板。升级不兼容软件包的情况下，用来进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[倒换，并且将剩余待升级的所有单板进行升级。]{style="font-family:宋体"}

[[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_x921234086}[设备：]{style="font-family:宋体"}

[**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_x2077217214}[命令在升级兼容软件包的情况下，用来进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[倒换。在升级不兼容软件包的情况下，用来进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[倒换，并且升级剩余的成员设备。]{style="font-family:宋体"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_287403938}[模式单成员设备：]{style="font-family:宋体"}

[**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_x185266421}[命令在升级兼容软件包的情况下，用来进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[倒换，并且升级业务板和网板。升级不兼容软件包的情况下，用来进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[倒换，并且将剩余待升级的所有单板进行升级。]{style="font-family:宋体"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_746794364}[模式多成员设备：]{style="font-family:宋体"}

[**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_x952435806}[命令在升级兼容软件包的情况下，用来进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[倒换。升级不兼容软件包的情况下，用来进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[倒换，并且将剩余待升级的成员设备进行升级。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1535071358}

[**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_1806526826}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_382864507}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_1466879444}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x2029641077}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x10942997}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x952370270}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_71526_x1155_1129443887}

[[当设备上有两块主控板时，输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x2030005963}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[兼容升级：增量升级时系统会将升级的进程进行进程级主备倒换；软重启或者重启升级时系统会将当前主用主控板使用原版本重新启动，将刚使用]{style="font-family:宋体"}]{#struct_0_71526_x1155_x952239198}**[issu load]{lang="EN-US"}**[命令升级的备用主控板上倒换成主用主控板。并]{style="font-family:宋体"}[升级业务板和网板。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不兼容升级：当前主用主控板、业务板和网板以新版本重新启动，刚使用]{style="font-family:宋体"}]{#struct_0_71526_x1155_x951583838}**[issu load]{lang="EN-US"}**[命令升级的备用主控板倒换成主用主控板，原有主用主控板、业务板和网板重启完成后即完成升级过程。]{style="font-family:宋体"}

[[当设备上只有一块主控板并需要升级时，不需要使用此命令。]{style="font-family:宋体"}]{#struct_0_71526_x1155_154244248}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_71526_x1155_1035426339}[设备]{lang="EN-US" style="font-family:宋体"}

[[从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过]{style="font-family:宋体"}**[display device]{lang="EN-US"}**]{#struct_0_71526_x1155_x1328272542}[[、]{style="font-family:宋体"}]{.ItemListCharChar}**[display mdc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[[命令]{style="font-family:
宋体"}]{.ItemListCharChar}[查看到所有单板处于]{style="font-family:宋体"}[normal]{lang="EN-US"}[状态、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态和所有服务的]{style="font-family:宋体"}[action]{lang="EN-US"}[显示为]{style="font-family:宋体"}[0]{lang="EN-US"}[后，再执行]{style="font-family:宋体"}**[issu run switchover]{lang="EN-US"}**[命令，否则，命令会执行失败。]{style="font-family:宋体"}

[[输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x902451608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[兼容升级：增量升级时系统会对升级的进程进行了进程级主备倒换；软重启或者重启升级时系统会将当前主设备使用原版本重新启动，将刚使用]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1945475587}[issu load]{lang="EN-US"}[命令升级的从设备选举为新主设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不兼容版本升级：执行]{style="font-family:宋体"}]{#struct_0_71526_x1155_x951977053}**[issu load]{lang="EN-US"}**[后]{style="font-family:宋体"}[IRF]{lang="EN-US"}[分裂，生成两个的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[。执行]{style="font-family:宋体"}**[issu run switchover]{lang="EN-US"}**[重启并升级原]{style="font-family:宋体"}[IRF]{lang="EN-US"}[，原]{style="font-family:宋体"}[IRF]{lang="EN-US"}[组重启后加入新的]{style="font-family:宋体"}[IRF]{lang="EN-US"}[即完成升级过程，系统选择新]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的主设备为合并后]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的主设备。]{style="font-family:宋体"}

[[当设备上只有一个成员并需要升级时，不需要使用此命令。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x659176786}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}]{#struct_0_71526_x1155_47461979}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过]{style="font-family:宋体"}**[display device]{lang="EN-US"}**]{#struct_0_71526_x1155_x678302610}[[、]{style="font-family:宋体"}]{.ItemListCharChar}**[display mdc]{lang="EN-US"}**[和]{style="font-family:宋体"}**[display system internal ha service-group]{lang="EN-US"}**[[命令]{style="font-family:
宋体"}]{.ItemListCharChar}[查看到所有单板处于]{style="font-family:宋体"}[normal]{lang="EN-US"}[状态、所有]{style="font-family:宋体"}[MDC]{lang="EN-US"}[处于]{style="font-family:宋体"}[active]{lang="EN-US"}[状态和所有服务的]{style="font-family:宋体"}[action]{lang="EN-US"}[显示为]{style="font-family:宋体"}[0]{lang="EN-US"}[后，再执行]{style="font-family:宋体"}**[issu run switchover]{lang="EN-US"}**[命令，否则，命令会执行失败。]{style="font-family:宋体"}

[[当设备上只有一个成员设备，多个主控板时，输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}]{#struct_0_71526_x1155_900524914}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[兼容升级：增量升级时系统会将升级的进程进行进程级主备倒换；软重启或者重启升级时系统会将当前主用主控板使用原版本重新启动，将刚使用]{style="font-family:宋体"}]{#struct_0_71526_x1155_x952370269}**[issu load]{lang="EN-US"}**[命令升级的备用主控板上倒换成主用主控板。]{style="font-family:宋体"}[同时升级业务板和网板。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不兼容升级：当前主用主控板、业务板和网板以新版本重新启动，刚使用]{style="font-family:宋体"}]{#struct_0_71526_x1155_1128854062}**[issu load]{lang="EN-US"}**[命令升级的备用主控板]{style="font-family:宋体"}[倒换成主用主控板，原有主用主控板、业务板和网板重启完成后即完成升级过程。]{style="font-family:宋体"}

[[当设备上只有一个成员并且只有一个主控板且需要升级时，不需要使用此命令。]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1976606606}

[[当设备上有多个成员设备时，输入该命令后，系统将自动执行以下操作：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x952304733}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[兼容版本升级：增量升级时系统会对升级的进程进行了进程级主备倒换；软重启或者重启升级时系统会将当前主设备的主控板使用原版本重新启动，将刚使用]{style="font-family:宋体"}]{#struct_0_71526_x1155_x952239197}**[issu load]{lang="EN-US"}**[命令升级完成的从设备选举为]{style="font-family:宋体"}[IRF]{lang="EN-US"}[的主设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不兼容版本升级：执行]{lang="EN-US" style="font-family:宋体"}**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x952108128}[后]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[分裂，生成两个的]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[。执行]{lang="EN-US" style="font-family:宋体"}**[issu run switchover]{lang="EN-US"}**[重启并升级原]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[，原]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[重启后加入新的]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[即完成升级过程，系统选择新]{lang="EN-US" style="font-family:
宋体"}[IRF]{lang="EN-US"}[的主设备为合并后]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[的主设备。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x852257060}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[兼容版本升级时，如果在回滚定时器超时时仍未执行]{style="font-family:宋体"}]{#struct_0_71526_x1155_x967523932}**[issu accept]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[issu commit]{lang="EN-US"}**[命令，则系统会自动回滚到升级前的版本。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[兼容版本升级时，如果业务板和网板无法使用增量或者软重启升级，这种情况下业务板和网板会重启，并从新主控板加载最新的软件包，途经此业务板和网板的流量会中断，流量恢复时间是"业务板和网板启动时间]{style="font-family:宋体"}]{#struct_0_71526_x1155_x727548171}[+]{lang="EN-US"}[业务板和网板状态恢复时间"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不兼容版本升级执行]{lang="EN-US" style="font-family:宋体"}**[issu run switchover]{lang="EN-US"}**]{#struct_0_71526_x1155_x952042592}[之后，即完成升级过程。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1151797350}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1160770680}[版本兼容情况下，进行主备倒换，同时升级业务板和网板。（分布式设备－独立运行模式双主控）]{style="font-family:宋体"}

[[\<Sysname\> issu run switchover]{lang="EN-US"}]{#struct_0_71526_x1155_x952304736}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Switchover Way]{lang="EN-US"}

[  0                           Active standby process switchover]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  2                           Service Upgrade]{lang="EN-US"}

[  3                           Service Upgrade]{lang="EN-US"}

[  4                           Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_378150847}[版本不兼容情况下，进行主备倒换，同时升级原主板、业务板和网板。（分布式设备－独立运行模式双主控）]{style="font-family:宋体"}

[[\<Sysname\> issu run switchover]{lang="EN-US"}]{#struct_0_71526_x1155_x952173663}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  0                           Reboot]{lang="EN-US"}

[  2                           Reboot]{lang="EN-US"}

[  3                           Reboot]{lang="EN-US"}

[  4                           Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_767857711}[版本兼容情况下，进行主备倒换。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu run switchover]{lang="EN-US"}]{#struct_0_71526_x1155_x952435807}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Switchover Way]{lang="EN-US"}

[  1                           Active standby process switchover]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x951649375}[版本不兼容情况下，进行主备倒换，同时升级成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[（主设备）和成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[（从设备）。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> issu run switchover]{lang="EN-US"}]{#struct_0_71526_x1155_613648137}

[Copying file flash:/feature.bin to slot2#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on slot 2\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Slot                        Upgrade Way]{lang="EN-US"}

[  1                           Reboot]{lang="EN-US"}

[  2                           Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_1041400446}[版本兼容情况下，进行主备倒换。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式多成员设备）]{style="font-family:宋体"}

[[\<Sysname\> issu run switchover]{lang="EN-US"}]{#struct_0_71526_x1155_614434569}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[Chassis   Slot              Switchover Way]{lang="EN-US"}

[  1         0                 Active standby process switchover]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_614041354}[版本不兼容情况下，进行主备倒换，同时升级成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[（主设备）和成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[（从设备）。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式多成员设备）]{style="font-family:宋体"}

[[\<Sysname\> issu run switchover]{lang="EN-US"}]{#struct_0_71526_x1155_614500106}

[Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 1 slot 1\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis2#slot0#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 2 slot 0\...Done.]{lang="EN-US"}

[Copying file flash:/feature.bin to chassis2#slot1#flash:/feature.bin\...Done.]{lang="EN-US"}

[Verifying the file flash:/feature.bin on chassis 2 slot 1\...Done.]{lang="EN-US"}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         0                 Reboot]{lang="EN-US"}

[  1         1                 Reboot]{lang="EN-US"}

[  1         2                 Reboot]{lang="EN-US"}

[  1         3                 Reboot]{lang="EN-US"}

[  1         4                 Reboot]{lang="EN-US"}

[  2         0                 Reboot]{lang="EN-US"}

[  2         1                 Reboot]{lang="EN-US"}

[  2         2                 Reboot]{lang="EN-US"}

[  2         3                 Reboot]{lang="EN-US"}

[  2         4                 Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1569547542}[版本兼容情况下，进行主备倒换，同时升级业务板和网板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备双主控）]{style="font-family:宋体"}

[[\<Sysname\> issu run switchover]{lang="EN-US"}]{#struct_0_71526_x1155_614106887}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Switchover Way]{lang="EN-US"}

[  1         0                 Active standby process switchover]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         2                 Service Upgrade]{lang="EN-US"}

[  1         3                 Service Upgrade]{lang="EN-US"}

[  1         4                 Service Upgrade]{lang="EN-US"}

[Upgrading software images to compatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1716466904}[版本不兼容情况下，进行主备倒换，同时升级原主控板、业务板和网板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式单成员设备双主控）]{style="font-family:宋体"}

[[\<Sysname\> issu run switchover]{lang="EN-US"}]{#struct_0_71526_x1155_614434567}

[Upgrade summary according to following table:]{lang="EN-US"}

[ ]{lang="EN-US"}

[flash:/feature.bin]{lang="EN-US"}

[  Running Version             New Version]{lang="EN-US"}

[  Alpha 7122                  Alpha 7123]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Chassis   Slot              Upgrade Way]{lang="EN-US"}

[  1         0                 Reboot]{lang="EN-US"}

[  1         2                 Reboot]{lang="EN-US"}

[  1         3                 Reboot]{lang="EN-US"}

[  1         4                 Reboot]{lang="EN-US"}

[Upgrading software images to incompatible versions. Continue? \[Y/N\]:y]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[issu load]{lang="EN-US"}]{#struct_0_71526_x1155_x10500126}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1083240046}[[字段]{style="font-family:黑体"}]{#struct_0_71526_x1155_x622566121}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_71526_x1155_200546308}

[[Copying file *A* to *B*\...\...Done.]{lang="EN-US"}]{#struct_0_71526_x1155_613648136}

[[将文件从位置]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_71526_x1155_613910277}[拷贝到位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*[。只有不兼容升级其它从设备时才有该提示信息（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[将文件从位置]{style="font-family:宋体"}*[A]{lang="EN-US"}*]{#struct_0_71526_x1155_613713669}[拷贝到位置]{style="font-family:宋体"}*[B]{lang="EN-US"}*[。只有不兼容升级其它全局备用主控板时才有该提示信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Verifying the file flash:/xx.bin on chassis 1 slot 0\.....Done.]{lang="EN-US"}]{#struct_0_71526_x1155_1488321168}

[[验证文件是否合法]{style="font-family:宋体"}]{#struct_0_71526_x1155_x401478610}

[[Switchover Way]{lang="EN-US"}]{#struct_0_71526_x1155_613779205}

[[倒换方式，取值可能为：]{style="font-family:宋体"}]{#struct_0_71526_x1155_x1301028928}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active standby process switchover]{lang="EN-US"}]{#struct_0_71526_x1155_x594272136}[：表示主备进程的倒换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active standby MPU switchover]{lang="EN-US"}]{#struct_0_71526_x1155_240663627}[：]{style="font-family:
  宋体"}[表示主备主控板之间的倒换（分布式设备－独立运行模式）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global active standby MPU switchover]{lang="EN-US"}]{#struct_0_71526_x1155_1512243428}[：]{style="font-family:宋体"}[表示全局主备主控板之间的倒换（分布式设备－]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master subordinate switchover]{lang="EN-US"}]{#struct_0_71526_x1155_177776531}[：]{style="font-family:
  宋体"}[表示主设备和从设备之间的倒换（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[其它字段]{style="font-family:宋体"}]{#struct_0_71526_x1155_613844741}

[[请参见]{style="font-family:宋体"}]{#struct_0_71526_x1155_1294637378}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?270907887#_Ref329853865)

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x197407489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[issu load]{lang="EN-US"}**]{#struct_0_71526_x1155_x1935893816}

::: {#1009564561 .myid}
[]{#_Toc404782754}[]{#struct_0_71526_x1155_356306422}[]{#_Toc299981216}

**ISSU \-- ISSU配置命令 \-- reset install log-history oldest**

------------------------------------------------------------------------

[**[reset install log-history oldest]{lang="EN-US"}**]{#struct_0_71526_x1155_1117199795}[命令用来清除]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[日志。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_549270844}

[**[reset install log-history oldest ]{lang="EN-US"}***[log-number]{lang="EN-US"}*]{#struct_0_71526_x1155_614434565}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x10500128}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_x622566127}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_200677380}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_280666799}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_1149531509}

[*[log-number]{lang="EN-US"}*]{#struct_0_71526_x1155_488486862}[：]{style="font-family:宋体;layout-grid-mode:
line"}[ISSU]{lang="EN-US" style="layout-grid-mode:line"}[日志的数量。]{style="font-family:宋体;layout-grid-mode:line"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1238909907}

[[使用该命令，系统将清除指定数量的、时间最早的、与]{style="font-family:宋体;layout-grid-mode:line"}[ISSU]{lang="EN-US" style="layout-grid-mode:line"}]{#struct_0_71526_x1155_x1499497065}[升级相关的日志]{style="font-family:
宋体;layout-grid-mode:line"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_614500101}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_x1569547539}[清除]{style="font-family:宋体"}[2]{lang="EN-US"}[条最早的]{style="font-family:宋体"}[ISSU]{lang="EN-US"}[日志。]{style="font-family:宋体"}

[[\<Sysname\> reset install log-history oldest 2]{lang="EN-US"}]{#struct_0_71526_x1155_x1044362776}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_902689516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install log]{lang="EN-US"}**]{#struct_0_71526_x1155_x1595738971}
:::

::: {#-1439638611 .myid}
[]{#_Toc404782755}[]{#struct_0_71526_x1155_1108369080}

**ISSU \-- ISSU配置命令 \-- reset install rollback oldest**

------------------------------------------------------------------------

[**[reset install rollback oldest]{lang="EN-US"}**]{#struct_0_71526_x1155_x567984776}[命令用来清除]{style="font-family:
宋体"}[ISSU]{lang="EN-US"}[回滚点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1484393455}

[**[reset install rollback oldest]{lang="EN-US"}**[ *point-id*]{lang="EN-US"}]{#struct_0_71526_x1155_613910278}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71526_x1155_890495091}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71526_x1155_1077427865}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x511345784}

[[network-admin]{lang="EN-US"}]{#struct_0_71526_x1155_x2068107228}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1722763124}

[*[point-id]{lang="EN-US"}*]{#struct_0_71526_x1155_x1187541221}[：系统存储的回滚点的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_71526_x1155_717831130}

[[使用该命令，系统将清除指定]{style="font-family:宋体;layout-grid-mode:line"}]{#struct_0_71526_x1155_325297797}[回滚点[以及]{style="layout-grid-mode:line"}比[该]{style="layout-grid-mode:line"}回滚点更老的回滚点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71526_x1155_613975814}

[[\# ]{lang="EN-US"}]{#struct_0_71526_x1155_455449443}[清除编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[以及比]{style="font-family:宋体"}[2]{lang="EN-US"}[号回滚点更老的回滚点。]{style="font-family:宋体"}

[[\<Sysname\> reset install rollback oldest 2]{lang="EN-US"}]{#struct_0_71526_x1155_x1349370330}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_71526_x1155_x1556953833}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display install rollback]{lang="EN-US"}**]{#struct_0_71526_x1155_x2054241347}
:::
