::: {#-725530759 .myid}
[]{#_Toc404797117}[]{#struct_0_86484_x7486_x1132185055}[]{#_Toc309396735}

**EAA \-- EAA配置命令 \-- action cli**

------------------------------------------------------------------------

[**[action ]{lang="EN-US"}[cli]{lang="EN-US"}**]{#struct_0_86484_x7486_x1084520301}[命令用]{style="font-family:宋体"}[来]{style="font-family:宋体"}[配置事件发生时执行指定的命令行。]{style="font-family:宋体"}

[**[undo action]{lang="EN-US"}**]{#struct_0_86484_x7486_454695427}[命令用来取]{style="font-family:宋体"}[消指定的操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1553029916}

[**[action ]{lang="EN-US"}***[number ]{lang="EN-US"}***[cli ]{lang="EN-US"}***[command-line]{lang="EN-US"}*]{#struct_0_86484_x7486_x1190570674}

[**[undo action ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_86484_x7486_1371290026}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_321074503}

[[监控策略下未配置任何]{style="font-family:宋体"}[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_200694422}[动作。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1340938102}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_90885360}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x124497456}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_1805487296}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_1266057534}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x12090358}

[*[number]{lang="EN-US"}*]{#struct_0_86484_x7486_129982358}[：动作序号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[231]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cli ]{lang="EN-US"}***[command-line]{lang="EN-US"}*]{#struct_0_86484_x7486_1371355562}[：需要执行的命令。该参数可以是命令的不完整形式，比如为命令]{style="font-family:宋体"}**[display current-configuration]{lang="EN-US"}**[的缩写形式]{style="font-family:
宋体"}**[dis cu]{lang="EN-US"}**[，但需要用户保证其为设备可识别的合法命令，否则，该动作不能成功执行。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1133548281}

[[如果配置事件发生时执行指定的命令行为非用户视图下的，则必须先配置进入相应视图的]{style="font-family:宋体"}**[action cli]{lang="EN-US"}**]{#struct_0_86484_x7486_1371158954}[，且进视图的]{style="font-family:宋体"}**[action]{lang="EN-US"}**[的编号应小于执行指定命令的]{style="font-family:宋体"}**[action]{lang="EN-US"}**[的编号。比如，要使用]{style="font-family:宋体"}[CLI]{lang="EN-US"}[策略来关闭接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，则需要配置三条]{style="font-family:宋体"}**[action]{lang="EN-US"}**[命令，]{style="font-family:宋体"}**[action]{lang="EN-US"}**[ 1 **cli** system-view]{lang="EN-US"}[、]{style="font-family:宋体"}**[action]{lang="EN-US"}**[ 2 **cli** interface gigabitethernet 1/0/1]{lang="EN-US"}[、]{style="font-family:宋体"}**[action]{lang="EN-US"}**[ 3 **cli** shutdown]{lang="EN-US"}[。]{style="font-family:宋体"}

[[同一个监控策略下可以配置多个动作，当监控策略被触发后，系统会按照动作序号从小到大依次执行这些动作。如果用户配置了相同序号的动作，当管理员执行]{style="font-family:宋体"}**[commit]{lang="EN-US"}**]{#struct_0_86484_x7486_416321557}[命令时，新配置的]{style="font-family:宋体"}**[action]{lang="EN-US"}**[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1370192359}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_2033585740}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置动作：当]{style="font-family:宋体"}[test]{lang="EN-US"}[被触发时，关闭接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x1205157446}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_1666110151}

[[\[Sysname-rtm-test\] action 1 cli system-view]{lang="EN-US"}]{#struct_0_86484_x7486_1319392175}

[[\[Sysname-rtm-test\] action 2 cli interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_86484_x7486_x931914735}

[[\[Sysname-rtm-test\] action 3 cli shutdown]{lang="EN-US"}]{#struct_0_86484_x7486_796463243}
:::

::: {#-1324787428 .myid}
[]{#_Toc404797118}[]{#struct_0_86484_x7486_1371224490}[]{#_Toc309396734}[]{#_Toc307902158}

**EAA \-- EAA配置命令 \-- action reboot**

------------------------------------------------------------------------

[**[action reboot]{lang="EN-US"}**]{#struct_0_86484_x7486_1899628460}[命令用]{style="font-family:宋体"}[来]{style="font-family:宋体"}[配置事件发生时]{style="font-family:宋体"}[执行重启操作。]{style="font-family:宋体"}

[**[undo action]{lang="EN-US"}**]{#struct_0_86484_x7486_573420429}[命令用来取]{style="font-family:宋体"}[消指定的操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1957638645}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_86484_x7486_1282656675}

[**[action ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_86484_x7486_x1391566753}**[reboot ]{lang="EN-US"}**[\[ **subslot** *subslot-number* \]]{lang="EN-US"}

[**[undo action ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_86484_x7486_178860235}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_86484_x7486_x732393994}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[action ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_86484_x7486_x639609117}**[reboot ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **subslot** *subslot-number* \] \]]{lang="EN-US"}

[**[undo action ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_86484_x7486_1816859410}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_86484_x7486_1371552170}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[action ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_86484_x7486_x830530155}**[reboot ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \[ **slot** *slot-number* \[ **subslot** *subslot-number* \] \] \]]{lang="EN-US"}

[**[undo action ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_86484_x7486_x982326663}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x947769915}

[[监控策略下未配置任何重启动作。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1260246299}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_916855433}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x227785796}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1812505523}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1602723247}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_1977515062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1371617706}

[*[number]{lang="EN-US"}*]{#struct_0_86484_x7486_x1625195572}[：动作序号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[231]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_86484_x7486_x1213095244}*[chassis-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_86484_x7486_1120649106}*[chassis-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号。不指定该参数时，表示所有成员设备]{style="font-family:宋体"}[/]{lang="EN-US"}[虚拟框。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_2144426633}[ *slot-number*]{lang="EN-US"}[：表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_82201873}[ *slot-number*]{lang="EN-US"}[：表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_x2007650224}[ *slot-number*]{lang="EN-US"}[：表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_409107514}*[ slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_x143736885}*[ slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot]{lang="EN-US"}**]{#struct_0_86484_x7486_1340842359}[ *subslot-number*]{lang="EN-US"}[：子卡所在的子槽位号。不指定该参数时，表示所有子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x660907621}

[[使用]{style="font-family:宋体"}**[action reboot]{lang="EN-US"}**]{#struct_0_86484_x7486_x1357855478}[命令，或者使用]{style="font-family:宋体"}**[action ]{lang="EN-US"}[cli]{lang="EN-US"}**[命令并将]{style="font-family:宋体"}*[command-line]{lang="EN-US"}*[参数指定为]{style="font-family:宋体"}**[reboot]{lang="EN-US"}**[命令，均可实现在事件发生时执行重启操作。只是]{style="font-family:宋体"}**[action reboot]{lang="EN-US"}**[命令会直接执行重启操作，使用]{style="font-family:宋体"}**[action ]{lang="EN-US"}[cli]{lang="EN-US"}**[命令时，用户可以选择是否先保存当前配置，再执行重启操作。]{style="font-family:宋体"}

[[同一个监控策略下可以配置多个动作，当监控策略被触发后，系统会按照动作序号从小到大依次执行这些动作。如果用户配置了相同序号的动作，当管理员执行]{style="font-family:宋体"}**[commit]{lang="EN-US"}**]{#struct_0_86484_x7486_1496370767}[命令时，新配置的]{style="font-family:宋体"}**[action]{lang="EN-US"}**[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1271179058}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_572843262}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置动作：当]{style="font-family:宋体"}[test]{lang="EN-US"}[被触发时，重启整个设备。（]{style="font-family:宋体"}[集中式设备[/]{lang="EN-US"}分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x58192745}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_1130734362}

[[\[Sysname-rtm-test\] action 3 reboot]{lang="EN-US"}]{#struct_0_86484_x7486_x105037228}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_540823121}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置动作：当]{style="font-family:宋体"}[test]{lang="EN-US"}[被触发时，重启成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[。（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x1383233598}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_x1357789942}

[[\[Sysname-rtm-test\] action 3 reboot slot 1]{lang="EN-US"}]{#struct_0_86484_x7486_x789377575}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_32023154}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置动作：当]{style="font-family:宋体"}[test]{lang="EN-US"}[被触发时，重启成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x689546511}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_1834036735}

[[\[Sysname-rtm-test\] action 3 reboot chassis 1]{lang="EN-US"}]{#struct_0_86484_x7486_x1227215898}
:::

::: {#1697134716 .myid}
[]{#_Toc404797119}[]{#struct_0_86484_x7486_1897019223}[]{#_Toc309396737}

**EAA \-- EAA配置命令 \-- action switchover**

------------------------------------------------------------------------

[**[action ]{lang="EN-US"}[switchover]{lang="EN-US"}**]{#struct_0_86484_x7486_x735803443}[命令用]{style="font-family:宋体"}[来]{style="font-family:宋体"}[配置事件发生时启动主备倒换]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo action]{lang="EN-US"}**]{#struct_0_86484_x7486_x1357921014}[命令用来取]{style="font-family:宋体"}[消指定的操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_156699908}

[**[action ]{lang="EN-US"}***[number]{lang="EN-US"}***[ switchover]{lang="EN-US"}**]{#struct_0_86484_x7486_1265705583}

[**[undo action ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_86484_x7486_x1029989782}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_813418497}

[[监控策略下未配置主备倒换动作。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x734765988}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_403741622}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_517412708}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_998009587}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_1542904838}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1357593334}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_616810574}

[*[number]{lang="EN-US"}*]{#struct_0_86484_x7486_1747221745}[：动作序号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[231]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x921519946}

[[同一个监控策略下可以配置多个动作，当监控策略被触发后，系统会按照动作序号从小到大依次执行这些动作。如果用户配置了相同序号的动作，当管理员执行]{style="font-family:宋体"}**[commit]{lang="EN-US"}**]{#struct_0_86484_x7486_x538568016}[命令时，新配置的]{style="font-family:宋体"}**[action]{lang="EN-US"}**[生效。]{style="font-family:宋体"}

[[即便当前设备不是主备环境（未部署备用主控板或者备用主控板未正常启动），该命令也会执行成功，但不会触发主备倒换动作。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x42199303}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1751418698}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_307939693}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置动作：当]{style="font-family:宋体"}[test]{lang="EN-US"}[被触发时，执行主备倒换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_462809029}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_x255189277}

[[\[Sysname-rtm-test\] action 3 switchover]{lang="EN-US"}]{#struct_0_86484_x7486_x636607938}
:::

::: {#139847418 .myid}
[]{#_Toc404797120}[]{#struct_0_86484_x7486_x1357527798}[]{#_Toc309396736}

**EAA \-- EAA配置命令 \-- action syslog**

------------------------------------------------------------------------

[**[action ]{lang="EN-US"}[syslog]{lang="EN-US"}**]{#struct_0_86484_x7486_975672767}[命令用]{lang="EN-US" style="font-family:宋体"}[来]{lang="EN-US" style="font-family:宋体"}[配置事件发生时]{lang="EN-US" style="font-family:宋体"}[生成]{style="font-family:宋体"}[一条指定内容的日志]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[**[undo action]{lang="EN-US"}**]{#struct_0_86484_x7486_x423554413}[命令用来取]{style="font-family:宋体"}[消指定的操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1615581490}

[**[action ]{lang="EN-US"}***[number ]{lang="EN-US"}***[syslog priority ]{lang="EN-US"}***[level]{lang="EN-US"}***[ facility ]{lang="EN-US"}***[local-number]{lang="EN-US"}***[ msg ]{lang="EN-US"}***[msg-body]{lang="EN-US"}*]{#struct_0_86484_x7486_x1210283326}

[**[undo action ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_86484_x7486_x1457508196}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x585229836}

[[监控策略下未配置任何日志动作。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1357724406}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1662508086}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_801789304}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1564098071}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_1657829645}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_2132300873}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x995227660}

[*[number]{lang="EN-US"}*]{#struct_0_86484_x7486_208247320}[：动作序号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[231]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[priority ]{lang="EN-US"}***[level]{lang="EN-US"}*]{#struct_0_86484_x7486_x83953958}[：生成的日志的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。优先级的值越小，优先级越高。]{style="font-family:
宋体"}

[**[facility ]{lang="EN-US"}***[local-number]{lang="EN-US"}*]{#struct_0_86484_x7486_x1357658870}[：生成日志的设备号，取值范围为]{style="font-family:宋体"}[local0]{lang="EN-US"}[～]{style="font-family:宋体"}[local7]{lang="EN-US"}[。]{style="font-family:宋体"}[主要用于在日志主机端标志不同的日志来源，查找、过滤对应日志源的日志。]{style="font-family:宋体"}

[**[msg ]{lang="EN-US"}***[msg-body]{lang="EN-US"}*]{#struct_0_86484_x7486_x1668798077}[：生成的日志的内容。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1914228966}

[[事件触发后生成的日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1545491903}

[[同一个监控策略下可以配置多个动作，当监控策略被触发后，系统会按照动作序号从小到大依次执行这些动作。如果用户配置了相同序号的动作，当管理员执行]{style="font-family:宋体"}**[commit]{lang="EN-US"}**]{#struct_0_86484_x7486_1763247196}[命令时，新配置的]{style="font-family:宋体"}**[action]{lang="EN-US"}**[生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1403222973}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x1357331190}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置动作：当]{style="font-family:宋体"}[test]{lang="EN-US"}[被触发时，生成一条优先级为]{style="font-family:宋体"}[7]{lang="EN-US"}[、设备号为]{style="font-family:宋体"}[local3]{lang="EN-US"}[、内容为]{style="font-family:宋体"}[hello]{lang="EN-US"}[的日志。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_843209054}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_2014195368}

[[\[Sysname-rtm-test\] action 3 syslog priority 7 facility local3 msg hello]{lang="EN-US"}]{#struct_0_86484_x7486_x1466673650}
:::

::: {#399103237 .myid}
[]{#_Toc404797121}[]{#struct_0_86484_x7486_489762743}[]{#_Toc309396738}

**EAA \-- EAA配置命令 \-- commit**

------------------------------------------------------------------------

[**[commit]{lang="EN-US"}**]{#struct_0_86484_x7486_x1231374066}[命令用]{style="font-family:宋体"}[来]{style="font-family:宋体"}[启用]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1793388567}

[**[commit]{lang="EN-US"}**]{#struct_0_86484_x7486_x1753211263}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x724515806}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x2062507161}[监控策略未被启用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1357265654}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x142587842}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_936561196}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1569790521}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_575699311}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1181829837}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x671604206}[策略策略创建并配置事件和动作后，并不会立即生效，需要执行]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[命令才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1319840468}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x20563151}[启用]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x1357855477}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_x1588742948}

[[\[Sysname-rtm-test\] commit]{lang="EN-US"}]{#struct_0_86484_x7486_x1573500399}
:::

::: {#1318966325 .myid}
[]{#_Toc404797122}[]{#struct_0_86484_x7486_x1281417372}[]{#_Toc309396726}[]{#_Toc307902150}

**EAA \-- EAA配置命令 \-- display rtm environment**

------------------------------------------------------------------------

[**[display rtm environment]{lang="EN-US"}**]{#struct_0_86484_x7486_x1868512074}[命令用来显示用户自定义的]{style="font-family:宋体"}[EAA]{lang="EN-US"}[环境变量配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_153461033}

[**[display rtm environment]{lang="EN-US"}**[ \[ *var-name* \]]{lang="EN-US"}]{#struct_0_86484_x7486_x1827466025}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1357789941}

[[任意]{style="font-family:宋体;color:black"}]{#struct_0_86484_x7486_x386093048}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x291385497}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1525906530}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1262500736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1540021469}

[*[var-name]{lang="EN-US"}*]{#struct_0_86484_x7486_362723446}[：]{style="font-family:宋体"}[显示指定名称的环境变量的配置。不指定该参数时，显示所有环境变量的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1357986549}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x2050665260}[显示用户自定义的所有]{style="font-family:宋体"}[EAA]{lang="EN-US"}[环境变量配置。]{style="font-family:宋体"}

[[\<Sysname\> display rtm environment]{lang="EN-US"}]{#struct_0_86484_x7486_x1972690366}

[[Name             Value]{lang="EN-US"}]{#struct_0_86484_x7486_864841623}

[[config_cmd       interface m1/0/1]{lang="EN-US"}]{#struct_0_86484_x7486_286368089}

[[save_cmd         save main force]{lang="EN-US"}]{#struct_0_86484_x7486_x1354086522}

[[show_run_cmd     display current-configuration]{lang="EN-US"}]{#struct_0_86484_x7486_1508052400}

[[表1-1 ]{lang="EN-US"}[display rtm environment]{lang="EN-US"}]{#struct_0_86484_x7486_x1564460365}[命令信息描述]{style="font-family:黑体"}

[]{#table_struct_0_x751009406}[[主要字段]{style="font-size:9.0pt;
   line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x1357921013}
:::

[[描述]{style="font-size:9.0pt;
   line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x1765614393}

[[Name]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_x1258568607}

[[环境变量的名称]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x1498887319}

[[Value]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_x1572608327}

[[环境变量的值]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x823153365}

[ ]{lang="EN-US"}

::: {#-884705362 .myid}
[]{#_Toc404797123}[]{#struct_0_86484_x7486_1888181920}[]{#_Toc309752979}

**EAA \-- EAA配置命令 \-- display rtm policy**

------------------------------------------------------------------------

[**[display rtm policy]{lang="EN-US"}**]{#struct_0_86484_x7486_x1357593333}[命令用来]{style="font-family:宋体"}[显示监控策略的相关信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x2112072781}

[**[display rtm policy]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **active** \| **registered** \[ **verbose** \] } \[ *policy-name* \]]{lang="EN-US"}]{#struct_0_86484_x7486_x418946907}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1675969480}

[[任意]{style="font-family:宋体;color:black"}]{#struct_0_86484_x7486_x817157833}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1492498764}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1329960715}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x118011779}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_405953819}

[**[active]{lang="EN-US"}**]{#struct_0_86484_x7486_391558400}[：显示正在执行的监控策略的相关信息。]{style="font-family:宋体"}

[**[registered]{lang="EN-US"}**]{#struct_0_86484_x7486_x1357527797}[：显示已创建的监控策略的相关信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_86484_x7486_x234180814}[：显示指定监控策略的相关信息。]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[表示监控策略的名称，]{style="font-family:宋体"}[不指定]{style="font-family:宋体"}[该参数]{style="font-family:宋体"}[时，显示所有]{style="font-family:宋体"}[正在执行的或者是已创建的]{style="font-family:宋体"}[监控策略的]{style="font-family:宋体"}[相关信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_86484_x7486_654668932}[：显示监控策略的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x677387759}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x1679668929}[显示所有正在运行的监控策略。]{style="font-family:宋体"}

[[\<Sysname\> display rtm policy active]{lang="EN-US"}]{#struct_0_86484_x7486_x2141961421}

[[JID   Type  Event      TimeActive           PolicyName]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_86484_x7486_x1357724405}

[[507   TCL   INTERFACE  Aug 29 14:55:55 2013 test]{lang="EN-US"}]{#struct_0_86484_x7486_654603396}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_1066375269}[显示所有监控策略的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display rtm policy registered]{lang="EN-US"}]{#struct_0_86484_x7486_538352372}

[Total number: 1]{lang="EN-US"}

[Type  Event      TimeRegistered       PolicyName]{lang="EN-US"}

[CLI              Aug 29 14:54:50 2013 test]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_654800004}[显示所有监控策略的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display  rtm policy registered verbose]{lang="EN-US"}]{#struct_0_86484_x7486_654734468}

[  Total number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Policy Name: test]{lang="EN-US"}

[   Policy Type: CLI]{lang="EN-US"}

[    Event Type:]{lang="EN-US"}

[TimeRegistered: Aug 29 14:54:50 2013]{lang="EN-US"}

[     User-role: network-operator]{lang="EN-US"}

[                network-admin]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display rtm policy]{lang="EN-US"}]{#struct_0_86484_x7486_1416250102}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x724257214}[[主要字段]{style="font-size:9.0pt;
   line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x673184409}
:::

[[描述]{style="font-size:9.0pt;
   line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x693775257}

[[JID]{lang="EN-US"}]{#struct_0_86484_x7486_x1133411301}

[[任务]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_86484_x7486_x1357331189}[，执行]{style="font-family:宋体"}**[display  rtm policy active]{lang="EN-US"}**[命令时才显示该信息]{style="font-family:宋体"}

[[PolicyName]{lang="EN-US"}]{#struct_0_86484_x7486_x1079039711}

[[监控策略的名称]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1779253832}

[[Type]{lang="EN-US"}]{#struct_0_86484_x7486_x633086753}

[[监控策略的类型，其中：]{style="font-family:宋体"}]{#struct_0_86484_x7486_x2042890123}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCL]{lang="EN-US"}]{#struct_0_86484_x7486_x1357265653}[表示这个策略是通过]{style="font-family:宋体"}[TCL]{lang="EN-US"}[脚本定义的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x1708671783}[表示这个策略是通过命令行定义的]{style="font-family:宋体"}

[[Policy Type]{lang="EN-US"}]{#struct_0_86484_x7486_654275713}

[[Event]{lang="EN-US"}]{#struct_0_86484_x7486_828965811}

[[监控策略触发事件的类型]{style="font-family:宋体"}]{#struct_0_86484_x7486_1346956258}[，包括]{style="font-family:宋体"}[CLI]{lang="EN-US"}[、]{style="font-family:宋体"}[HOTPLUG]{lang="EN-US"}[、]{style="font-family:宋体"}[INTERFACE]{lang="EN-US"}[、]{style="font-family:宋体"}[PROCESS]{lang="EN-US"}[、]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[、]{style="font-family:宋体"}[SNMP_NOTIF]{lang="EN-US"}[、]{style="font-family:宋体"}[SYSLOG]{lang="EN-US"}[七种，具体配置及含义参考相应]{style="font-family:宋体"}**[event]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[Event Type]{lang="EN-US"}]{#struct_0_86484_x7486_244899397}

[[TimeActive]{lang="EN-US"}]{#struct_0_86484_x7486_1126678890}

[[监控策略开始运行的时间]{style="font-family:宋体"}]{#struct_0_86484_x7486_654210177}

[[PolicyName]{lang="EN-US"}]{#struct_0_86484_x7486_x950494579}

[[监控策略的名称]{style="font-family:宋体"}]{#struct_0_86484_x7486_x253353950}

[[TimeRegistered]{lang="EN-US"}]{#struct_0_86484_x7486_531400466}

[[监控策略的创建时间]{style="font-family:宋体"}]{#struct_0_86484_x7486_x648624501}

[[Total number]{lang="EN-US"}]{#struct_0_86484_x7486_654406785}

[[监控策略的总数]{style="font-family:宋体"}]{#struct_0_86484_x7486_946134860}

[[User-role]{lang="EN-US"}]{#struct_0_86484_x7486_x1357789940}

[[执行监控策略需要的最小用户角色]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1952176989}

[ ]{lang="EN-US"}

::: {#1187546778 .myid}
[]{#_Toc404797124}[]{#struct_0_86484_x7486_678218095}[]{#_Toc309396727}[]{#_Toc307902151}

**EAA \-- EAA配置命令 \-- event cli**

------------------------------------------------------------------------

[**[event cli]{lang="EN-US"}**]{#struct_0_86484_x7486_x1832953456}[命令用来配置命令行事件。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_x806587502}[命令用来取消当前的事件配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x824422636}

[**[event cli ]{lang="EN-US"}**[{ **async** \[ ]{lang="EN-US"}**[skip ]{lang="EN-US"}**[\]]{lang="EN-US"}[ \| **sync** } **mode** { **execute** \| **help** \| **tab** } **pattern** *regular-exp*]{lang="EN-US"}]{#struct_0_86484_x7486_x1357921012}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_963268962}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1835295419}

[[未配置任何命令行事件。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1975398827}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1770593088}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_1660209868}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x976804910}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x159525522}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1688884383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1507709551}

[**[async]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[skip]{lang="EN-US"}**[ \]]{lang="EN-US"}]{#struct_0_86484_x7486_x1357658868}[：]{style="font-family:宋体"}[异步监控。如果指定]{style="font-family:宋体"}**[skip]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，则表示事件发生时，只执]{style="font-family:宋体"}[行]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监]{style="font-family:宋体"}[控策略中的动作，不执行]{style="font-family:宋体"}**[event cli]{lang="EN-US"}**[中指定的命令；如果不]{style="font-family:宋体"}[指定]{style="font-family:宋体"}**[skip]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，则表示事件发生时，]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监]{style="font-family:宋体"}[控策略和]{style="font-family:宋体"}**[event cli]{lang="EN-US"}**[中指定的命令同时执行。]{style="font-family:宋体"}

[**[sync]{lang="EN-US"}**]{#struct_0_86484_x7486_x1312633253}[：]{style="font-family:宋体"}[同步监控。只有]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控]{style="font-family:宋体"}[策略执行成功，]{style="font-family:宋体"}**[event cli]{lang="EN-US"}**[中指定的命令]{style="font-family:宋体"}[才能执行。]{style="font-family:宋体"}

[**[execute]{lang="EN-US"}**]{#struct_0_86484_x7486_80435350}[：]{style="font-family:宋体"}[监控命令行的执行。当用户执行特定命令时，触发]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[help]{lang="EN-US"}**]{#struct_0_86484_x7486_x57551092}[：]{style="font-family:宋体"}[监控命令行]{style="font-family:宋体"}[的"]{style="font-family:宋体"}[?]{lang="EN-US"}["]{style="font-family:宋体"}[帮助。当用户执行特定帮助命令时，触发]{style="font-family:
宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[tab]{lang="EN-US"}**]{#struct_0_86484_x7486_1157497441}[：]{style="font-family:宋体"}[监控命令行]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Tab]{lang="EN-US"}[补]{style="font-family:宋体"}[全。当用户执行特定命令并使用]{style="font-family:宋体"}[Tab]{lang="EN-US"}[键]{style="font-family:宋体"}[自动补全功能时，触发]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[pattern]{lang="EN-US"}***[ regular-exp]{lang="EN-US"}*]{#struct_0_86484_x7486_x1357265652}[：]{style="font-family:宋体"}[用于匹配命令行的正则表达式。只要输入的命令行中包含该字符串，则匹配成功，触发策略执行。关于正则表达式的详细描述请参见"基础配置指导"中的"]{style="font-family:宋体"}[CLI]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1020211572}

[[配置该事件后，当用户输入指定的命令并执行相应动作（执行、帮助或者补全）就会触发策略执行。用户输入命令是否执行、帮助或者补全，以及是否等待]{style="font-family:宋体"}[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x821778242}[监控]{style="font-family:宋体"}[策略执行成功后再执行、帮助或者补全，由]{style="font-family:宋体"}**[sync]{lang="EN-US"}**[、]{style="font-family:宋体"}**[async]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[skip]{lang="EN-US"}**[ \]]{lang="EN-US"}[参数]{style="font-family:宋体"}[决定。]{style="font-family:宋体"}

[[同一监控策略下，只能配置一个事件。如果多次执行]{style="font-family:宋体"}**[event]{lang="EN-US"}**]{#struct_0_86484_x7486_1185588815}[命令配置了不同事件，则最新配置并]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1357855475}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_1543424934}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置异步]{style="font-family:宋体"}[CLI]{lang="EN-US"}[事件，当用户输入命令中含有]{style="font-family:宋体"}[dis inter brief]{lang="EN-US"}[字符并执行该命令时触发策略执行，同时跳过命令行执行。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_86484_x7486_1847357672}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_x935985935}

[[\[Sysname-rmt-test\] event cli async skip mode execute pattern dis inter brief]{lang="EN-US"}]{#struct_0_86484_x7486_x1357789939}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x1357986547}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置异步]{style="font-family:宋体"}[CLI]{lang="EN-US"}[事件，当用户输入的命令中含有]{style="font-family:宋体"}[dis inter brief]{lang="EN-US"}[字符并使用了]{style="font-family:宋体"}[\<Tab\>]{lang="EN-US"}[键补全功能时，触发策略执行，同时将]{style="font-family:宋体"}[\<Tab\>]{lang="EN-US"}[键补全的结果返回给用户。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_1081502622}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_1247514007}

[[\[Sysname-rmt-test\] event cli async mode tab pattern dis inter brief]{lang="EN-US"}]{#struct_0_86484_x7486_x1357921011}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x1357593331}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置同步]{style="font-family:宋体"}[CLI]{lang="EN-US"}[事件，当用户输入的命令中含有]{style="font-family:宋体"}[dis inter brief]{lang="EN-US"}[字符并使用了帮助功能时，触发策略执行。系统等策略执行成功后，返回帮助的结果。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_86484_x7486_1020095101}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_1894897167}

[[\[Sysname-rmt-test\] event cli sync mode help pattern dis inter brief]{lang="EN-US"}]{#struct_0_86484_x7486_x1357527795}
:::

::: {#806257264 .myid}
[]{#_Toc404797125}[]{#struct_0_86484_x7486_928618600}[]{#_Toc309396729}

**EAA \-- EAA配置命令 \-- event hotplug**

------------------------------------------------------------------------

[**[event hotplug]{lang="EN-US"}**]{#struct_0_86484_x7486_x483230063}[命令用来配置板卡热插拔事件。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_x1526315966}[命令用来取消当前的事件配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1077518154}

[[集中式设备[/]{lang="EN-US"}分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1357724403}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[event hotplug]{lang="EN-US"}**]{#struct_0_86484_x7486_1872944323}**[ ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[insert]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[remove]{lang="EN-US"}**[ \] ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **subslot** *subslot-number* \]]{lang="EN-US"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_1419642442}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_86484_x7486_337119792}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[event hotplug]{lang="EN-US"}**]{#struct_0_86484_x7486_x1357658867}**[ ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[insert]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[remove]{lang="EN-US"}**[ \] ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **subslot** *subslot-number* \]]{lang="EN-US"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_x102779672}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x2090464521}

[[未配置任何热插拔事件。]{style="font-family:宋体"}]{#struct_0_86484_x7486_601569541}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1873787828}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x322505091}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x509172879}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_1517291429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1665101623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1357331187}

[**[insert]{lang="EN-US"}**]{#struct_0_86484_x7486_x445680433}[：表示监控单板的插入事件。不指定]{style="font-family:宋体"}**[insert]{lang="EN-US"}**[和]{style="font-family:宋体"}**[remove]{lang="EN-US"}**[参数时，表示监控单板的插入和拔出事件。]{style="font-family:宋体"}

[**[remove]{lang="EN-US"}**]{#struct_0_86484_x7486_664867213}[：表示监控单板的拔出事件。不指定]{style="font-family:宋体"}**[insert]{lang="EN-US"}**[和]{style="font-family:宋体"}**[remove]{lang="EN-US"}**[参数时，表示监控单板的插入和拔出事件。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_x1357265651}*[ slot-number]{lang="EN-US"}*[：取值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，无实际意义。（集中式设备）]{style="font-family:
宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_x1357855474}[ *slot-number*]{lang="EN-US"}[：表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_x1185458421}*[ slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_1120321427}*[ slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_86484_x7486_1614901545}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的指定单板。其中，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_86484_x7486_930916512}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的指定单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或]{style="font-family:宋体"}[者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对]{style="font-family:宋体"}[应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[subslot]{lang="EN-US"}**]{#struct_0_86484_x7486_x1357986546}[ *subslot-number*]{lang="EN-US"}[：子卡所在的子槽位号。不指定该参数时，表示单板上的任一子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x484581319}

[[配置该事件后，当用户插入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86484_x7486_x1670071961}[拔出指定板卡，会触发监控策略执行。]{style="font-family:宋体"}

[[同一监控策略下，只能配置一个事件。如果多次执行]{style="font-family:宋体"}**[event]{lang="EN-US"}**]{#struct_0_86484_x7486_x1147693819}[命令配置了不同事件，则最新配置并]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x900076413}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x1357921010}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置监控事件：热插拔]{style="font-family:宋体"}[2]{lang="EN-US"}[号子卡均触发策略执行。（]{style="font-family:宋体"}[集中式设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_2126068376}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_x1357593330}

[[\[Sysname-rtm-test\] event hotplug slot 0 subslot 2]{lang="EN-US"}]{#struct_0_86484_x7486_x1708788254}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x1357527794}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置监控事件：热插拔]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位的板卡时触发策略执行。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x637465341}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_x1832281201}

[[\[Sysname-rtm-test\] event hotplug slot 2]{lang="EN-US"}]{#struct_0_86484_x7486_1171613732}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_487434589}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置监控事件：热插拔成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[上的子卡时均触发策略执行。（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x995590723}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_x549247484}

[[\[Sysname-rtm-test\] event hotplug slot 2]{lang="EN-US"}]{#struct_0_86484_x7486_x935212644}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_98552611}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置监控事件：热插拔成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[2]{lang="EN-US"}[号槽位的板卡时触发策略执行。（]{style="font-family:
宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x1357724402}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_306860382}

[[\[Sysname-rtm-test\] event hotplug chassis 1 slot 2]{lang="EN-US"}]{#struct_0_86484_x7486_1131915615}
:::

::: {#823272471 .myid}
[]{#_Toc404797126}[]{#struct_0_86484_x7486_x97596178}[]{#_Toc309396730}

**EAA \-- EAA配置命令 \-- event interface**

------------------------------------------------------------------------

[**[event interface]{lang="EN-US"}**]{#struct_0_86484_x7486_1890029137}[命令用来配置接口事件。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_x1237237957}[命令用来取消当前的事件配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1134774775}

[**[event interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*[ **monitor-obj** *monitor-obj* **start-op** *start-op* **start-val** *start-val* **restart-op** *restart-op* **restart-val** *restart-val* \[ **interval** *interval* \]]{lang="EN-US"}]{#struct_0_86484_x7486_1186349653}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_1818314581}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x2028546132}

[[未配置任何接口事件。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1357658866}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1463304269}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_1317611097}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x742354865}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1053540710}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1930743104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x853900311}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_86484_x7486_x979963153}[：表示要监控的接口类型和编号。]{style="font-family:宋体"}

[**[monitor-obj]{lang="EN-US"}***[ monitor-obj]{lang="EN-US"}*]{#struct_0_86484_x7486_x1526237316}[：]{style="font-family:宋体"}[表示要监控的对]{style="font-family:宋体"}[象，具体描述请见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?823272471#_Ref323135376)[。]{style="font-family:宋体"}

[**[start-op ]{lang="EN-US"}***[start-op]{lang="EN-US"}*]{#struct_0_86484_x7486_x1583474682}[：]{style="font-family:宋体"}[触发监控策略执行的操]{style="font-family:宋体"}[作码，取值如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?823272471#_Ref323135406)[所示。]{style="font-family:宋体"}

[**[start-val ]{lang="EN-US"}***[start-val]{lang="EN-US"}*]{#struct_0_86484_x7486_x1357331186}[：]{style="font-family:宋体"}[触发监控策略执行的监控对象的值，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位请见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?823272471#_Ref323135376)[。]{style="font-family:宋体"}

[**[restart-op ]{lang="EN-US"}***[restart-op]{lang="EN-US"}*]{#struct_0_86484_x7486_2006074004}[：重新开启触发开关]{style="font-family:宋体"}[的操]{style="font-family:宋体"}[作码，具体描述请见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?823272471#_Ref323135406)[。]{style="font-family:宋体"}

[**[restart-val ]{lang="EN-US"}***[restart-val]{lang="EN-US"}*]{#struct_0_86484_x7486_x1726748203}[：重新开启触发开关]{style="font-family:宋体"}[的监控对象的值，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位请见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?823272471#_Ref323135376)[。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_86484_x7486_x1357265650}[：]{style="font-family:宋体"}[获取监控对象数据的时]{style="font-family:宋体"}[间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[]{#struct_0_86484_x7486_x2111956310}[[表1-3 ]{lang="EN-US"}[监控对象说明]{style="font-family:
黑体"}]{#_Ref323135376}

[]{#table_struct_0_x711398590}[[监控对象]{style="font-size:9.0pt;
   line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x1750538917}
:::

[[含义]{style="font-size:9.0pt;
   line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x445108558}

[[input-drops]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_x1293240928}

[[接口接收方向丢弃包的个数]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x1077726755}

[[input-errors]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_x1357855473}

[[接口接收到的错误包的个数]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_736855880}

[[output-drops]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_832935115}

[[接口发送方向丢弃包的个数]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_1398719080}

[[output-errors]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_1270169297}

[[接口发送出去的错误包的个数]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_591534958}

[[rcv-bps]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_x1588386695}

[[接口接收速率，单位为比特]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x1357789937}[/]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}[秒]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}

[[rcv-broadcasts]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_x1192596566}

[[接口接收到的广播包个数]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x243655698}

[[rcv-pps]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_574403526}

[[接口接收速率，单位为包]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x1201220354}[/]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}[秒]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}

[[tx-bps]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_939626279}

[[接口传输速率，单位为比特]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x1357986545}[/]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}[秒]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}

[[tx-pps]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}]{#struct_0_86484_x7486_x81296792}

[[接口传输速率，单位为包]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_755124123}[/]{lang="EN-US" style="font-size:9.0pt;line-height:125%"}[秒]{style="font-size:9.0pt;
  line-height:125%;font-family:宋体"}

[ ]{lang="EN-US" style="font-size:9.0pt"}

[]{#struct_0_86484_x7486_x1858431312}[[表1-4 ]{lang="EN-US"}[比较操作符说明]{style="font-family:
黑体"}]{#_Ref323135406}

[]{#table_struct_0_x716033470}[[比较操作符]{style="font-size:9.0pt;
   line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_x106869546}

[[含义]{style="font-size:9.0pt;
   line-height:125%;font-family:宋体"}]{#struct_0_86484_x7486_1937640277}

[[eq]{lang="EN-US"}]{#struct_0_86484_x7486_1959990482}

[[等于]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1357921009}

[[ge]{lang="EN-US"}]{#struct_0_86484_x7486_x958979803}

[[大于等于]{style="font-family:宋体"}]{#struct_0_86484_x7486_1037247275}

[[gt]{lang="EN-US"}]{#struct_0_86484_x7486_2075506573}

[[大于]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1149639604}

[[le]{lang="EN-US"}]{#struct_0_86484_x7486_x1864398648}

[[小于等于]{style="font-family:宋体"}]{#struct_0_86484_x7486_1021958167}

[[lt]{lang="EN-US"}]{#struct_0_86484_x7486_x1357593329}

[[小于]{style="font-family:宋体"}]{#struct_0_86484_x7486_1376390997}

[[ne]{lang="EN-US"}]{#struct_0_86484_x7486_1149646115}

[[不等于]{style="font-family:宋体"}]{#struct_0_86484_x7486_x675379215}

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1889146679}

[[接口事件中存在一个触发开关：]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1357527793}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[配置该事件后，触发开关立即打开。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1357724401}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[当指定接口上的指定报文的数目达到]{lang="EN-US" style="font-family:宋体"}**[start-op]{lang="EN-US"}**[ *start-op* **start-val** *start-val*]{lang="EN-US"}]{#struct_0_86484_x7486_x1357658865}[参数指定的条件时，触发监控策略执行一次（第一次执行），并关闭触发开关，但系统会继续监控接口事件。]{lang="EN-US" style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[当满足]{lang="EN-US" style="font-family:宋体"}**[restart-op ]{lang="EN-US"}***[restart-op]{lang="EN-US"}***[ restart-val ]{lang="EN-US"}***[restart-val]{lang="EN-US"}*]{#struct_0_86484_x7486_x1265579086}[参数指定的条件时，才重新开启触发开关。]{lang="EN-US" style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果指定接口上的指定报文的数目再次达到]{lang="EN-US" style="font-family:宋体"}**[start-op]{lang="EN-US"}**[ *start-op* **start-val** *start-val*]{lang="EN-US"}]{#struct_0_86484_x7486_x1357331185}[参数指定的条件时，则再次触发监控策略执行一次（第二次执行），并关闭触发开关，系统继续监控接口事件。]{lang="EN-US" style="font-family:宋体"}

[[(5)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如此循环。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_86484_x7486_x1357265649}

[[同一监控策略下，只能配置一个事件。如果多次执行]{style="font-family:宋体"}**[event]{lang="EN-US"}**]{#struct_0_86484_x7486_x189707545}[命令配置了不同事件，则最新配置并]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_478126810}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x556220968}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置监控事件：每]{style="font-family:宋体"}[60]{lang="EN-US"}[秒获取一次]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收到的错误包的个数。当错误包的个数大于]{style="font-family:宋体"}[1000]{lang="EN-US"}[时触发]{style="font-family:宋体"}[test]{lang="EN-US"}[执行并关闭触发开关，当错误包的个数小于]{style="font-family:宋体"}[50]{lang="EN-US"}[时重新开启触发开关，如此循环。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_1315041760}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_2108657808}

[[\[Sysname-rtm-test\] event interface gigabitethernet 1/0/1 monitor-obj input-errors start-op gt start-val 1000 restart-op lt restart-val 50 interval 60]{lang="EN-US"}]{#struct_0_86484_x7486_1757771132}

::: {#737186560 .myid}
[]{#_Toc404797127}[]{#struct_0_86484_x7486_353546257}[]{#_Toc309396728}

**EAA \-- EAA配置命令 \-- event process**

------------------------------------------------------------------------

[**[event process]{lang="EN-US"}**]{#struct_0_86484_x7486_899151445}[命令用来配置进程事件。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_1649362008}[命令用来取消当前的事件配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_208228463}

[[集中式设备[/]{lang="EN-US"}分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_86484_x7486_x698342395}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[event process ]{lang="EN-US"}**[{ **exception** \| **restart** \| **shutdown** \| **start** } \[ **name** *process-name* \[ **instance** *instance-id* \] \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_86484_x7486_793328804}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_x2104647633}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_86484_x7486_1433490053}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[event process ]{lang="EN-US"}**[{ **exception** \| **restart** \| **shutdown** \| **start** } \[ **name** *process-name* \[ **instance** *instance-id* \] \] \[ **chassis** *chassis-number* \[ **slot** *slot-number* \] \]]{lang="EN-US"}]{#struct_0_86484_x7486_208293999}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_1158232418}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x544523236}

[[未配置任何进程事件。]{style="font-family:宋体"}]{#struct_0_86484_x7486_118660244}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x2093904394}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_1276955593}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1033530950}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_208097391}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_75232524}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1734216849}

[**[exception]{lang="EN-US"}**]{#struct_0_86484_x7486_1970678826}**[：]{style="font-family:宋体"}**[监控进程异常事件。当进程发生异常时，触]{style="font-family:宋体"}[发]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策]{style="font-family:宋体"}[略。]{style="font-family:宋体"}

[**[restart]{lang="EN-US"}**]{#struct_0_86484_x7486_x1688956949}[：]{style="font-family:宋体"}[监控进程重启事件。当进程重启时，触]{style="font-family:宋体"}[发]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策]{style="font-family:宋体"}[略。]{style="font-family:宋体"}

[**[shutdown]{lang="EN-US"}**]{#struct_0_86484_x7486_1025089530}[：]{style="font-family:宋体"}[监控进程关闭事件。当进程关闭时，触]{style="font-family:宋体"}[发]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策]{style="font-family:宋体"}[略。]{style="font-family:宋体"}

[**[start]{lang="EN-US"}**]{#struct_0_86484_x7486_1985629524}[：]{style="font-family:宋体"}[监控进程启动事件。当进程启动时，触]{style="font-family:宋体"}[发]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策]{style="font-family:宋体"}[略。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ process-name]{lang="EN-US"}*]{#struct_0_86484_x7486_121784049}[：监控的用户态]{style="font-family:宋体"}[进程的名称，可以是当前正在运行的进程也可以是没有运行的进程。]{style="font-family:宋体"}

[**[instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_86484_x7486_1426654244}**[：]{style="font-family:宋体"}**[监控的]{style="font-family:宋体"}[用户态]{style="font-family:宋体"}[进程的实例的编号。不指定该参数时，表示进程下的任意实例异常、重启、关闭、启动都会触发事件，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。可以是当前不存在的实例号]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_86484_x7486_2048155950}*[chassis-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}**]{#struct_0_86484_x7486_x1608561925}*[chassis-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或]{style="font-family:宋体"}[者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应]{style="font-family:宋体"}[的虚拟框号。不指定该参数时，表示所有成员设备[/]{lang="EN-US"}虚拟框。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_208162927}[ *slot-number*]{lang="EN-US"}[：表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_314381075}[ *slot-number*]{lang="EN-US"}[：表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_2065250791}[ *slot-number*]{lang="EN-US"}[：表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，表示所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_1245330169}*[ slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_86484_x7486_x1607709957}*[ slot-number]{lang="EN-US"}*[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或]{style="font-family:宋体"}[者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟]{style="font-family:宋体"}[槽位号。不指定该参数时，表示所有成员设备[/]{lang="EN-US"}]{style="font-family:宋体"}[PEX]{lang="EN-US"}[。（集中式]{style="font-family:
宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_2024883191}

[[配置该事件后，当指定进程异常、关闭、启动或重启时（可以为用户命令行触发的或者系统自动触发的），均触发]{style="font-family:宋体"}]{#struct_0_86484_x7486_1625785393}[监控策]{style="font-family:宋体"}[略执行。]{style="font-family:宋体"}

[[同一监控策略下，只能配置一个事件。如果多次执行]{style="font-family:宋体"}**[event]{lang="EN-US"}**]{#struct_0_86484_x7486_208490607}[命令配置了不同事件，则最新配置并]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x590982441}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_866467151}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置监控事件：当进程]{style="font-family:宋体"}[snmpd]{lang="EN-US"}[重启时触发策略执行。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_86484_x7486_264167884}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_x1915429774}

[[\[Sysname-rtm-test\] event process restart name snmpd]{lang="EN-US"}]{#struct_0_86484_x7486_1620001624}
:::

::: {#607682884 .myid}
[]{#_Toc404797128}[]{#struct_0_86484_x7486_325625980}[]{#_Toc309396732}

**EAA \-- EAA配置命令 \-- event snmp oid**

------------------------------------------------------------------------

[**[event snmp oid]{lang="EN-US"}**]{#struct_0_86484_x7486_1237798026}[命令用来配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[操作事件]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_x2037139052}[命令用来取消当前的事件配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1097442993}

[**[event snmp]{lang="EN-US"}**[ **oid** *oid* **monitor-obj** { **get** ]{lang="EN-US"}[\| **next** } **start-op** *start-op* **start-val** *start-val* **restart-op** *restart-op* **restart-val** *restart-val* \[ **interval** *interval* \]]{lang="EN-US"}]{#struct_0_86484_x7486_208556143}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_x1784160340}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x56312493}

[[未配置任何]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_86484_x7486_1917842221}[操作事件]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1079909097}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x988079498}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1008145344}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x732075306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_2050071207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1362273269}

[**[oid]{lang="EN-US"}***[ oid]{lang="EN-US"}*]{#struct_0_86484_x7486_208359535}[：]{style="font-family:宋体"}[表示需要监控的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[monitor-obj]{lang="EN-US"}**[ { **get \| next** }]{lang="EN-US"}]{#struct_0_86484_x7486_1080799774}[：表示需要监控的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[操作。]{style="font-family:宋体"}**[get]{lang="EN-US"}**[表示]{style="font-family:宋体"}[SNMP Get]{lang="EN-US"}[操作；]{style="font-family:宋体"}**[next]{lang="EN-US"}**[表示]{style="font-family:宋体"}[SNMP Get Next]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[**[start-op ]{lang="EN-US"}***[start-op]{lang="EN-US"}*]{#struct_0_86484_x7486_1258505947}[：]{style="font-family:宋体"}[触发监控策略执行的操]{style="font-family:宋体"}[作码，取值如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?823272471#_Ref323135406)[所示。]{style="font-family:宋体"}

[*[start-val]{lang="EN-US"}*]{#struct_0_86484_x7486_208425071}[：]{style="font-family:宋体"}[触发监控策略执行的值。]{style="font-family:宋体"}[可以是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块支持的所有类型，例如，数字、字符串等。因为支持多类型，帮助时统一提示为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[512]{lang="EN-US"}[个字符的字符串。如果该值中包含空格，需要在值的首末添加英文格式的引号，形如]{style="font-family:宋体"}["xxx xxx"]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[restart-op ]{lang="EN-US"}***[op]{lang="EN-US"}*]{#struct_0_86484_x7486_960719536}[：]{style="font-family:宋体"}[重新开启触发开关]{style="font-family:宋体"}[的操]{style="font-family:宋体"}[作码，取值如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-4]{lang="EN-US"}](?823272471#_Ref323135406)[所示。]{style="font-family:
宋体"}

[*[restart-val]{lang="EN-US"}*]{#struct_0_86484_x7486_208228464}[：]{style="font-family:宋体"}[重新开启触发开关]{style="font-family:宋体"}[的监控对象的值]{style="font-family:宋体"}[。可以是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块支持的所有类型，例如，数字、字符串等。因为支持多类型，帮助时统一提示为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[512]{lang="EN-US"}[个字符的字符串。如果该值中包含空格，需要在值的首末添加英文格式的引号，形如]{style="font-family:宋体"}["xxx xxx"]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_86484_x7486_208294000}[：]{style="font-family:宋体"}[获取监控对象数据的时]{style="font-family:宋体"}[间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x2030212696}

[[SNMP]{lang="EN-US"}]{#struct_0_86484_x7486_208097392}[操作]{style="font-family:宋体"}[事件中存在一个触发开关：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[配置该事件后，触发开关立即打开。]{style="font-family:宋体"}]{#struct_0_86484_x7486_208162928}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[此后系统按照用户设定的]{lang="EN-US" style="font-family:宋体"}**[interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_86484_x7486_208490608}[值定时]{lang="EN-US" style="font-family:宋体"}[获取设备上某个]{lang="EN-US" style="font-family:宋体"}[OID]{lang="EN-US"}[对应节点的值，且该值达到]{lang="EN-US" style="font-family:宋体"}**[start-op]{lang="EN-US"}**[ *start-op* **start-val** *start-val*]{lang="EN-US"}[参数指定的条件时，触发监控策略执行一次（第一次执行），并关闭触发开关，但系统会继续监控]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}[事件。]{lang="EN-US" style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[当满足]{lang="EN-US" style="font-family:宋体"}**[restart-op ]{lang="EN-US"}***[restart-op]{lang="EN-US"}***[ restart-val ]{lang="EN-US"}***[restart-val]{lang="EN-US"}*]{#struct_0_86484_x7486_208556144}[参数指定的条件时，才重新开启触发开关。]{lang="EN-US" style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果用户获取的]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_86484_x7486_208359536}[对象的值再次达到]{lang="EN-US" style="font-family:宋体"}**[start-op]{lang="EN-US"}**[ *start-op* **start-val** *start-val*]{lang="EN-US"}[参数指定的条件时，则再次触发监控策略执行一次（第二次执行），并关闭触发开关，系统继续监控]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}[事件。]{lang="EN-US" style="font-family:宋体"}

[[(5)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如此循环。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_86484_x7486_1080799773}

[[同一监控策略下，只能配置一个事件。如果多次执行]{style="font-family:宋体"}**[event]{lang="EN-US"}**]{#struct_0_86484_x7486_1258964699}[命令配置了不同事件，则最新配置并]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_208425072}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_960719533}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置监控事件：系统每]{style="font-family:宋体"}[5]{lang="EN-US"}[秒检查]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象]{style="font-family:宋体"}[1.3.6.4.9.9.42.1.2.1.6.4]{lang="EN-US"}[的值，当该值等于]{style="font-family:宋体"}[1]{lang="EN-US"}[时触发执行监控策略并关闭监控开关，当等于]{style="font-family:宋体"}[2]{lang="EN-US"}[时重新启动监控。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x1366062886}

[[\[Sysname\] rtm cli-policy snmp]{lang="EN-US"}]{#struct_0_86484_x7486_x1031774415}

[[\[Sysname-rtm-snmp\] event snmp oid 1.3.6.4.9.9.42.1.2.1.6.4 monitor-obj get start-op eq start-val 1 restart-op eq restart-val 2 interval 5]{lang="EN-US"}]{#struct_0_86484_x7486_x1687149628}
:::

::: {#321727526 .myid}
[]{#_Toc404797129}[]{#struct_0_86484_x7486_x1396226582}[]{#_Toc309396733}

**EAA \-- EAA配置命令 \-- event snmp-notification**

------------------------------------------------------------------------

[**[event snmp-notification]{lang="EN-US"}**]{#struct_0_86484_x7486_1199430889}[命令用来配置]{style="font-family:宋体"}[SNMP Trap]{lang="EN-US"}[事件]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_x1774823375}[命令用来取消当前的事件配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_434180315}

[**[event snmp-notification oid]{lang="EN-US"}**[ *oid* **oid-val** *oid-val* **op** *op* \[ **drop** \]]{lang="EN-US"}]{#struct_0_86484_x7486_x1454327603}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_208752752}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_82036963}

[[未配置任何]{style="font-family:宋体"}[SNMP Trap]{lang="EN-US"}]{#struct_0_86484_x7486_x1459093974}[触发事件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x458236249}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_1728263745}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_704549366}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1390693173}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_205239755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_95020971}

[**[oid]{lang="EN-US"}***[ oid]{lang="EN-US"}*]{#struct_0_86484_x7486_1239642854}[：]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息中携带的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象的]{style="font-family:宋体"}[OID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[oid-val]{lang="EN-US"}***[ oid-val]{lang="EN-US"}*]{#struct_0_86484_x7486_208294001}[：]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息中携带的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象的值。可以是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块支持的所有类型，例如，数字、字符串等。因为支持多类型，帮助时统一提示为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[512]{lang="EN-US"}[个字符的字符串。如果该值中包含空格，需要在值的首末添加英文格式的引号，形如]{style="font-family:宋体"}["xxx xxx"]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[op ]{lang="EN-US"}***[op]{lang="EN-US"}*]{#struct_0_86484_x7486_x2030212697}[：比较操作码，]{style="font-family:宋体"}[取值如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-4]{lang="EN-US"}](?823272471#_Ref323135406)[所示。]{style="font-family:
宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_86484_x7486_x2038987423}[：表示匹配成功后丢弃该]{style="font-family:宋体"}[Trap]{lang="EN-US"}[信息。不指定该参数时，表示正常发送。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1481528198}

[[配置该事件后，当系统生成一条]{style="font-family:宋体"}[Trap]{lang="EN-US"}]{#struct_0_86484_x7486_208097393}[，且]{style="font-family:宋体"}[Trap]{lang="EN-US"}[中携带的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[对象（由]{style="font-family:宋体"}*[oid]{lang="EN-US"}*[参数指定）的值到达]{style="font-family:宋体"}**[oid-val]{lang="EN-US"}***[ oid-val ]{lang="EN-US"}***[op]{lang="EN-US"}***[ op]{lang="EN-US"}*[指定的条件]{style="font-family:宋体"}[时，触发监控策略执行。]{style="font-family:宋体"}

[[同一监控策略下，只能配置一个事件。如果多次执行]{style="font-family:宋体"}**[event]{lang="EN-US"}**]{#struct_0_86484_x7486_75232522}[命令配置了不同事件，则最新配置并]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_587205777}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_208425073}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置]{style="font-family:宋体"}[SNMP Trap]{lang="EN-US"}[监控事件：当发生]{style="font-family:宋体"}[Trap]{lang="EN-US"}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.3.6.1.4.1.318.2.8.3]{lang="EN-US"}[，并且其值为]{style="font-family:宋体"}[UPS:Returned from battery backup power]{lang="EN-US"}[时，触发策略，同时丢弃这个]{style="font-family:宋体"}[Trap]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_960719534}

[[\[Sysname\] rtm cli-policy snmp-notification]{lang="EN-US"}]{#struct_0_86484_x7486_x1366062883}

[[\[Sysname-rtm-snmp-notification\] event snmp-notification oid 1.3.6.1.4.1.318.2.8.3 oid-val "UPS:Returned from battery backup power" op eq drop]{lang="EN-US"}]{#struct_0_86484_x7486_x1435058942}
:::

::: {#-2035667460 .myid}
[]{#_Toc404797130}[]{#struct_0_86484_x7486_1696588162}[]{#_Toc309396731}

**EAA \-- EAA配置命令 \-- event syslog**

------------------------------------------------------------------------

[**[event syslog]{lang="EN-US"}**]{#struct_0_86484_x7486_1351856943}[命令用来配置日志事件。]{style="font-family:宋体"}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_208752753}[命令用来取消当前的事件配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_82036962}

[**[event syslog ]{lang="EN-US"}[priority ]{lang="EN-US"}***[level]{lang="EN-US"}***[ msg]{lang="EN-US"}***[ msg ]{lang="EN-US"}***[occurs ]{lang="EN-US"}***[times]{lang="EN-US"}***[ period ]{lang="EN-US"}***[period]{lang="EN-US"}*]{#struct_0_86484_x7486_879558186}

[**[undo event]{lang="EN-US"}**]{#struct_0_86484_x7486_208818289}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x538672799}

[[未配置任何日志事件。]{style="font-family:宋体"}]{#struct_0_86484_x7486_x552154093}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1938104208}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x544128368}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1246541216}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1642022961}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x516070043}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1073009076}

[**[priority]{lang="EN-US"}***[ level]{lang="EN-US"}*]{#struct_0_86484_x7486_x2121655399}[：表示需要匹配的日志的最低优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[或者]{style="font-family:
宋体"}[all]{lang="EN-US"}[。对于数字表示的优先级，值越小，优先级越高。当]{style="font-family:宋体"}*[level]{lang="EN-US"}*[配置为]{style="font-family:宋体"}[3]{lang="EN-US"}[时，表示能匹配优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[的日志；]{style="font-family:宋体"}[all]{lang="EN-US"}[表示和任意优先级匹配。]{style="font-family:宋体"}

[**[msg]{lang="EN-US"}***[ msg]{lang="EN-US"}*]{#struct_0_86484_x7486_208097394}[：正则表达式，表示需要匹配的日志的部分或全部，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。该日志必须为]{style="font-family:宋体"}[H3C]{lang="EN-US"}[格式的日志，关于日志的详细介绍请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}

[**[occurs ]{lang="EN-US"}***[times]{lang="EN-US"}***[ period ]{lang="EN-US"}***[period]{lang="EN-US"}*]{#struct_0_86484_x7486_75232521}[：表示指定日志在]{style="font-family:宋体"}*[period]{lang="EN-US"}*[秒内发生了]{style="font-family:宋体"}*[times]{lang="EN-US"}*[次时触发监控策略执行。]{style="font-family:宋体"}*[times]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，]{style="font-family:宋体"}*[period]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1369109359}

[[配置该事件后，当系统在指定时间段内生成指定规格的日志信息时触发监控策略执行。为了防止循环触发，]{style="font-family:宋体"}[RTM]{lang="EN-US"}]{#struct_0_86484_x7486_208162930}[模块产生的日志不会触发策略。]{style="font-family:宋体"}

[[同一监控策略下，只能配置一个事件。如果多次执行]{style="font-family:宋体"}**[event]{lang="EN-US"}**]{#struct_0_86484_x7486_208490610}[命令配置了不同事件，则最新配置并]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1747669726}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x580952828}[为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[配置监控事件：当优先级高于或等于]{style="font-family:宋体"}[3]{lang="EN-US"}[、内容中含有]{style="font-family:宋体"}[down]{lang="EN-US"}[的日志在]{style="font-family:宋体"}[6]{lang="EN-US"}[秒内出现过]{style="font-family:宋体"}[5]{lang="EN-US"}[次时触发执行策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x1176871910}

[[\[Sysname\] rtm cli-policy syslog]{lang="EN-US"}]{#struct_0_86484_x7486_1802193613}

[[\[Sysname-rtm-syslog\] event syslog priority 3 msg down occurs 5 period 6]{lang="EN-US"}]{#struct_0_86484_x7486_1425387313}
:::

::: {#267419540 .myid}
[]{#_Toc404797131}[]{#struct_0_86484_x7486_x207700119}

**EAA \-- EAA配置命令 \-- rtm cli-policy**

------------------------------------------------------------------------

[**[rtm cli-policy]{lang="EN-US"}**]{#struct_0_86484_x7486_x1440091770}[命令用来创建]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略并进入]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略视图。]{style="font-family:宋体"}

[**[undo rtm cli-policy]{lang="EN-US"}**]{#struct_0_86484_x7486_x1320184245}[命令来删除指定的]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_208556146}

[**[rtm cli-policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_86484_x7486_x1784160335}

[**[undo rtm cli-policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}*]{#struct_0_86484_x7486_703005786}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x659513914}

[[未创建]{style="font-family:宋体"}[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_1542755479}[监控策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1697258084}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1479255925}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_629930192}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_1814087148}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_208359538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1080799763}

[*[policy-name]{lang="EN-US"}*]{#struct_0_86484_x7486_1258964698}[：]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略的名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x2023861881}

[[使用该命令用来创建]{style="font-family:宋体"}[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_647201514}[监控策略并进入]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略视图。在该视图下，用户可以通过命令行给]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略配置触发事件以及需要执行的动作。其中，触发事件只能定义一个，动作可以定义多个。当条件满足、事件被触发时，系统会按照动作序号由小到大顺序执行这些动作。监控动作在后台执行，用户可以通过查看日志信息了解策略的执行结果。]{style="font-family:宋体"}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_1828222287}[监控策略配置完成后（即配置完触发事件以及需要执行的动作后），必须执行]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[命令才能启用]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略，使配置的事件和动作生效。]{style="font-family:宋体"}

[[多次执行该命令可以创建多个]{style="font-family:宋体"}[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_1845566800}[监控策略且数量没有限制。请尽量确保同时启用的策略间动作不要冲突，因为当系统同时执行多个策略，且不同策略间动作有冲突时，执行结果是随机的。]{style="font-family:宋体"}

[[如果同为]{style="font-family:宋体"}[TCL]{lang="EN-US"}]{#struct_0_86484_x7486_x28735599}[监控策略或者同为]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略，则策略名不能相同。如果策略类型不同，则名称可以相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x901018727}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_208425074}[创建]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[并进入]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_960719531}

[\[Sysname\] rtm cli-policy test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1366062888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[commit]{lang="EN-US"}**]{#struct_0_86484_x7486_x1482113109}
:::

::: {#417053394 .myid}
[]{#_Toc404797132}[]{#struct_0_86484_x7486_x1918387750}[]{#_Toc309396725}[]{#_Toc307902149}

**EAA \-- EAA配置命令 \-- rtm environment**

------------------------------------------------------------------------

[**[rtm environment]{lang="EN-US"}**]{#struct_0_86484_x7486_x298588545}[命令用来创建监控]{style="font-family:宋体"}[策略]{style="font-family:宋体"}[的环境变量。]{style="font-family:宋体"}

[**[undo rtm environment]{lang="EN-US"}**]{#struct_0_86484_x7486_1477083442}[命令来]{style="font-family:宋体"}[删除指定的]{style="font-family:宋体"}[环境变量。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1141069402}

[**[rtm environment ]{lang="EN-US"}***[var-name]{lang="EN-US"}***[ ]{lang="EN-US"}***[var-value]{lang="EN-US"}*]{#struct_0_86484_x7486_2011406291}

[**[undo rtm environment ]{lang="EN-US"}***[var-name]{lang="EN-US"}*]{#struct_0_86484_x7486_208752754}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_82036969}

[[无用户自定义的环境变量，系统中支持一系列内部环境变量，不同事件支持的内部环境变量及其意义有所不同，请参见]{style="font-family:宋体"}]{#struct_0_86484_x7486_1688862250}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-5]{lang="EN-US"}](?417053394#_Ref321835254)[。]{style="font-family:
宋体"}

[]{#struct_0_86484_x7486_1449823544}[[表1-5 ]{lang="EN-US"}[内部环境变量描述表]{style="font-family:
黑体"}]{#_Ref321835254}

[]{#table_struct_0_x713862014}[[事件]{style="font-family:黑体"}]{#struct_0_86484_x7486_x751972809}
:::

[[内部环境变量的名称]{style="font-family:黑体"}]{#struct_0_86484_x7486_1924860343}

[[描述]{style="font-family:黑体"}]{#struct_0_86484_x7486_1945645788}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x300292661}

[[\_cmd]{lang="EN-US"}]{#struct_0_86484_x7486_208818290}

[[匹配上的命令]{style="font-family:宋体"}]{#struct_0_86484_x7486_1799979354}

[[SYSLOG]{lang="EN-US"}]{#struct_0_86484_x7486_x198754795}

[[\_syslog_pattern]{lang="EN-US"}]{#struct_0_86484_x7486_x583665475}

[[匹配的日志信息的内容]{style="font-family:宋体"}]{#struct_0_86484_x7486_x192705483}

[[HOTPLUG]{lang="EN-US"}]{#struct_0_86484_x7486_x2092268511}

[[\_slot]{lang="EN-US"}]{#struct_0_86484_x7486_x992331449}

[[发生热插拔的单板所在的槽位号]{style="font-family:宋体"}]{#struct_0_86484_x7486_208294003}

[[\_subslot]{lang="EN-US"}]{#struct_0_86484_x7486_x2030212699}

[[发生热插拔的子卡所在的子槽位号]{style="font-family:宋体"}]{#struct_0_86484_x7486_208490611}

[[INTERFACE]{lang="EN-US"}]{#struct_0_86484_x7486_1747669725}

[[\_ifname]{lang="EN-US"}]{#struct_0_86484_x7486_208556147}

[[接口的名称]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1784160336}

[[SNMP]{lang="EN-US"}]{#struct_0_86484_x7486_1106290313}

[[\_oid]{lang="EN-US"}]{#struct_0_86484_x7486_x1549458389}

[[SNMP]{lang="EN-US"}]{#struct_0_86484_x7486_986117140}[操作中携带的]{style="font-family:宋体"}[OID]{lang="EN-US"}

[[\_oid_value]{lang="EN-US"}]{#struct_0_86484_x7486_1843586640}

[[OID]{lang="EN-US"}]{#struct_0_86484_x7486_208425075}[对应节点的值]{style="font-family:宋体"}

[[SNMP TRAP]{lang="EN-US"}]{#struct_0_86484_x7486_960719532}

[[\_oid]{lang="EN-US"}]{#struct_0_86484_x7486_208752755}

[[SNMP Trap]{lang="EN-US"}]{#struct_0_86484_x7486_82036968}[信息中携带的]{style="font-family:宋体"}[OID]{lang="EN-US"}

[[PROCESS]{lang="EN-US"}]{#struct_0_86484_x7486_x267452886}

[[\_process_name]{lang="EN-US"}]{#struct_0_86484_x7486_x1561720190}

[[进程的名称]{style="font-family:宋体"}]{#struct_0_86484_x7486_1987913917}

[[公共环境变量]{style="font-family:宋体"}]{#struct_0_86484_x7486_208818291}

[[\_event_id]{lang="EN-US"}]{#struct_0_86484_x7486_1799979353}

[[事件的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_86484_x7486_x198427115}

[[\_event_type]{lang="EN-US"}]{#struct_0_86484_x7486_986094271}

[[事件的类型]{style="font-family:宋体"}]{#struct_0_86484_x7486_1451973620}

[[\_event_type_string]{lang="EN-US"}]{#struct_0_86484_x7486_208228468}

[[事件类型字符串，用于对事件类型进行详细描述]{style="font-family:宋体"}]{#struct_0_86484_x7486_x95601373}

[[\_event_time]{lang="EN-US"}]{#struct_0_86484_x7486_877827029}

[[事件发生的时间]{style="font-family:宋体"}]{#struct_0_86484_x7486_274353880}

[[\_event_severity]{lang="EN-US"}]{#struct_0_86484_x7486_x1879057329}

[[事件的严重级别]{style="font-family:宋体"}]{#struct_0_86484_x7486_208294004}

[ ]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x2030212700}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86484_x7486_x1278882713}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1161722414}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x416007006}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x290109868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1445000151}

[*[var-name]{lang="EN-US"}*]{#struct_0_86484_x7486_225462086}[：]{style="font-family:宋体"}[环境变量的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，只能包含数字、字母和下划线，并且不能以下划线开头。]{style="font-family:宋体"}

[*[var-value]{lang="EN-US"}*]{#struct_0_86484_x7486_208097396}[：环境变量的值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_75232519}

[[在配置监控策略的动作时，我们可以在应该输入参数的地方输入"]{style="font-family:宋体"}[\$]{lang="EN-US"}]{#struct_0_86484_x7486_x1332373514}[环境变量名"，表示此处需要引用环境变量值。系统在运行监控策略的时候，会自动用环境变量值去替代"]{style="font-family:宋体"}[\$]{lang="EN-US"}[环境变量名"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_669839776}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x401756379}[设置环境变量]{style="font-family:宋体"}[if]{lang="EN-US"}[，其值为]{style="font-family:宋体"}[interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x834282822}

[\[Sysname\] rtm environment if interface]{lang="EN-US"}

::: {#1477639925 .myid}
[]{#_Toc404797133}[]{#struct_0_86484_x7486_1157810981}[]{#_Toc309396739}

**EAA \-- EAA配置命令 \-- rtm scheduler suspend**

------------------------------------------------------------------------

[**[rt]{lang="EN-US"}[m scheduler suspend]{lang="EN-US"}**]{#struct_0_86484_x7486_755704849}[命令用来暂停运行所有的]{style="font-family:宋体"}[监控]{style="font-family:宋体"}[策略，包]{style="font-family:宋体"}[括所有]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略和]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策]{style="font-family:宋体"}[略。]{style="font-family:宋体"}

[**[undo rtm scheduler suspend]{lang="EN-US"}**]{#struct_0_86484_x7486_883011691}[命令用]{style="font-family:
宋体"}[来]{style="font-family:宋体"}[恢复运行监控策略。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_208162932}

[**[rt]{lang="EN-US"}[m scheduler suspend]{lang="EN-US"}**]{#struct_0_86484_x7486_x1093321996}

[**[undo rt]{lang="EN-US"}[m scheduler suspend]{lang="EN-US"}**]{#struct_0_86484_x7486_300119931}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1349072061}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86484_x7486_x442082650}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1598433071}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_325122646}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_878207145}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x710474344}

[[本命令是用来暂停所有已经配置但还未被触发的策略的，不能暂停处于]{style="font-family:宋体"}[active]{lang="EN-US"}]{#struct_0_86484_x7486_89957644}[状态的策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_208490612}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_1747669724}[暂停所有的]{style="font-family:宋体"}[监控]{style="font-family:
宋体"}[策略]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_x580821756}

[[\[Sysname\] rtm scheduler suspend]{lang="EN-US"}]{#struct_0_86484_x7486_1143781893}
:::

::: {#1338959532 .myid}
[]{#_Toc404797134}[]{#struct_0_86484_x7486_914077705}[]{#_Toc309752976}[]{#_Toc307475479}

**EAA \-- EAA配置命令 \-- rtm tcl-policy**

------------------------------------------------------------------------

[**[rtm tcl-policy]{lang="EN-US"}**]{#struct_0_86484_x7486_x2089018757}[命令用来创建并启用]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策略，并将它和]{style="font-family:宋体"}[TCL]{lang="EN-US"}[脚本绑定。]{style="font-family:宋体"}

[**[undo rtm tcl-policy]{lang="EN-US"}**]{#struct_0_86484_x7486_x433420633}[命令来删除]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1620566676}

[**[rtm tcl-policy]{lang="EN-US"}***[ policy-name tcl-filename]{lang="EN-US"}*]{#struct_0_86484_x7486_742279683}

[**[undo rtm tcl-policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_86484_x7486_208556148}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1784160345}

[[未创建]{style="font-family:宋体"}[TCL]{lang="EN-US"}]{#struct_0_86484_x7486_703202394}[监控策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x20287436}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86484_x7486_325895248}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x484560326}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x75086647}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x418367639}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x834910502}

[*[policy-name]{lang="EN-US"}*]{#struct_0_86484_x7486_322036472}[：]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策略的名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[tcl-filename]{lang="EN-US"}*]{#struct_0_86484_x7486_208359540}[：]{style="font-family:宋体"}[TCL]{lang="EN-US"}[脚本文件的名称。文件名区分大小写，扩展名必须为"]{style="font-family:宋体"}[.tcl]{lang="EN-US"}["，扩展名不区分大小写，且必须为设备存储介]{style="font-family:宋体"}[质（]{style="font-family:宋体"}[Flash]{lang="EN-US"}[或者]{style="font-family:宋体"}[CF]{lang="EN-US"}[卡）上存]{style="font-family:宋体"}[在的文件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_271495707}

[[使用该命令用来创建并启用一个]{style="font-family:宋体"}[TCL]{lang="EN-US"}]{#struct_0_86484_x7486_x1055445168}[监控策略，策略的具体内容由绑定的]{style="font-family:宋体"}[TCL]{lang="EN-US"}[脚本来定义。脚本中会定义策略的触发事件、事件触发时要执行的操作、执行操作需要的角色、策略的运行时间等参数。]{style="font-family:宋体"}

[[TCL]{lang="EN-US"}]{#struct_0_86484_x7486_1612353060}[监控策略启用后，不允许修改]{style="font-family:宋体"}[TCL]{lang="EN-US"}[脚本。如需修改，请先停用]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策略，修改后，再启用]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策略。否则，]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策略将不能运行。]{style="font-family:宋体"}

[[TCL]{lang="EN-US"}]{#struct_0_86484_x7486_485262286}[监控策略创建后，如果需要绑定另外一个]{style="font-family:宋体"}[TCL]{lang="EN-US"}[脚本，请先删除该]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策略，再重新创建并绑定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1007986552}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_x916059138}[创建并启用]{style="font-family:宋体"}[TCL]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[，并将它和脚本]{style="font-family:宋体"}[test.tcl]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_1808466423}

[\[Sysname\] rtm tcl-policy test test.tcl]{lang="EN-US"}
:::

::: {#838869868 .myid}
[]{#_Toc404797135}[]{#struct_0_86484_x7486_1738738846}

**EAA \-- EAA配置命令 \-- running-time**

------------------------------------------------------------------------

[**[running-time]{lang="EN-US"}**]{#struct_0_86484_x7486_208752756}[命令用]{lang="EN-US" style="font-family:宋体"}[来]{lang="EN-US" style="font-family:
宋体"}[配置事件发生时]{lang="EN-US" style="font-family:宋体"}[CLI]{lang="EN-US"}[监控]{style="font-family:宋体"}[策略的运行时间]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[**[undo running-time]{lang="EN-US"}**]{#struct_0_86484_x7486_82036967}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x694419926}

[**[running-time]{lang="EN-US"}***[ time]{lang="EN-US"}*]{#struct_0_86484_x7486_1141836979}

[**[undo running-time]{lang="EN-US"}**]{#struct_0_86484_x7486_695043889}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x688280599}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_2130542764}[监控策略的运行时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1683033611}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_1730117030}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_235124523}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_2130608300}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x1716015692}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_119343395}

[*[time]{lang="EN-US"}*]{#struct_0_86484_x7486_2130411692}[：]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略的运行时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31536000]{lang="EN-US"}[，单位为秒。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示策略可以永久运行下去。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_679253116}

[[当条件满足，监控策略被触发时，系统会开始计时。当运行时间到，即便策略还没有执行完，也会立即停止执行。该命令用于限制策略的运行时间，以免策略长时间运行占用系统资源。而策略是否会触发以及停止后是否会被再次触发则由]{style="font-family:宋体"}**[event]{lang="EN-US"}**]{#struct_0_86484_x7486_2130673836}[配置决定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1454865782}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_2131067052}[配置]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[的运行时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_1449503438}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_1591791255}

[[\[Sysname-rtm-test\] running-time 60]{lang="EN-US"}]{#struct_0_86484_x7486_1233052587}
:::

::: {#1580969545 .myid}
[]{#_Toc404797136}[]{#struct_0_86484_x7486_963051081}

**EAA \-- EAA配置命令 \-- user-role**

------------------------------------------------------------------------

[**[user-role]{lang="EN-US"}**]{#struct_0_86484_x7486_x1482345826}[命令用]{lang="EN-US" style="font-family:宋体"}[来]{lang="EN-US" style="font-family:宋体"}[配置执行]{lang="EN-US" style="font-family:
宋体"}[CLI]{lang="EN-US"}[监控]{style="font-family:宋体"}[策略]{lang="EN-US" style="font-family:宋体"}[时]{style="font-family:宋体"}[使用的]{lang="EN-US" style="font-family:宋体"}[用户]{style="font-family:宋体"}[角色]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[**[undo user-role]{lang="EN-US"}**]{#struct_0_86484_x7486_1264038451}[命令用来删除已经配置的指定用户角色]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x588796169}

[**[user-role ]{lang="EN-US"}***[role-name]{lang="EN-US"}*]{#struct_0_86484_x7486_2099260996}

[**[undo user-role ]{lang="EN-US"}***[role-name]{lang="EN-US"}*]{#struct_0_86484_x7486_2131132588}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x892669577}

[[执行]{style="font-family:宋体"}[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x1741222667}[监控策略时使用的用户角色为创建该策略的用户]{style="font-family:宋体"}[的角色。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1538431926}

[[CLI]{lang="EN-US"}]{#struct_0_86484_x7486_x1775919107}[监控策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86484_x7486_392688119}

[[network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_1054252680}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x61719531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86484_x7486_x1224921111}

[*[role-name]{lang="EN-US"}*]{#struct_0_86484_x7486_265177251}[：执行]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略时使用的用户角色，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符。必须为设备支持的用户角色。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86484_x7486_2130542765}

[[本命令用来指定执行监控策略的用户角色。用户角色中定义了允许用户操作哪些系统功能以及资源对象，设备支持的每条命令都有缺省用户角色，如果监控策略中指定的用户角色权限比命令行的缺省用户角色的权限小，则不能执行该命令以及该命令后面的所有动作。如果指定的用户角色不存在，则监控策略不能执行。如果给某个监控策略配置了多个用户角色，则使用这些用户角色权限的并集去执行该策略。例如，给某策略配置了用户角色]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_86484_x7486_x1682968075}[和]{style="font-family:宋体"}[B]{lang="EN-US"}[，如果策略中的动作是角色]{style="font-family:宋体"}[A]{lang="EN-US"}[或者]{style="font-family:宋体"}[B]{lang="EN-US"}[允许执行的，则策略可以执行；如果策略中存在角色]{style="font-family:宋体"}[A]{lang="EN-US"}[和]{style="font-family:宋体"}[B]{lang="EN-US"}[都不能执行的命令，则该命令以及该命令后面的所有动作都不能执行。关于用户角色的详细描述请参见"基础配置指导"中的"]{style="font-family:
宋体"}[RBAC]{lang="EN-US"}["。]{style="font-family:宋体"}

[[同一监控策略下可配置多个用户角色，最多可以配置]{style="font-family:宋体"}[64]{lang="EN-US"}]{#struct_0_86484_x7486_x1629023770}[个有效用户角色，]{style="font-family:宋体"}[超过该上限后，新配置的用户角色即便]{style="font-family:宋体"}**[commit]{lang="EN-US"}**[也不会生效。]{style="font-family:宋体"}

[[安全日志管理员角色与其它用户角色互斥：为监控策略配置安全日志管理员角色后，系统会自动删除当前配置的其它用户角色；反之亦然。]{style="font-family:宋体"}]{#struct_0_86484_x7486_2016593510}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86484_x7486_1296620299}

[[\# ]{lang="EN-US"}]{#struct_0_86484_x7486_64444530}[配置执行]{style="font-family:宋体"}[CLI]{lang="EN-US"}[监控策略]{style="font-family:宋体"}[test]{lang="EN-US"}[时使用的用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[和]{style="font-family:宋体"}[admin]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86484_x7486_580763285}

[[\[Sysname\] rtm cli-policy test]{lang="EN-US"}]{#struct_0_86484_x7486_1904880249}

[[\[Sysname-rtm-test\] user-role network-admin]{lang="EN-US"}]{#struct_0_86484_x7486_x89709850}

[[\[Sysname-rtm-test\] user-role admin]{lang="EN-US"}]{#struct_0_86484_x7486_1958576233}
:::
