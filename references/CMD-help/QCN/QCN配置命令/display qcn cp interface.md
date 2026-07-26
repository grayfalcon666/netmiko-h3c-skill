::: {#1349859859 .myid}
[]{#_Toc340223534}[]{#_Toc404792138}[]{#struct_0_x2117_81929_1364629081}[]{#_Toc340223542}

**QCN \-- QCN配置命令 \-- display qcn cp interface**

------------------------------------------------------------------------

[**[display qcn cp interface]{lang="EN-US"}**]{#struct_0_x2117_81929_1159013205}[命令用来显示]{style="font-family:
宋体"}[CP]{lang="EN-US"}[端的统计信息，包括接口对应]{style="font-family:宋体"}[CND]{lang="EN-US"}[绑定的]{style="font-family:宋体"}[proflie ID]{lang="EN-US"}[、通过的报文数、丢弃的报文数和发送的]{style="font-family:宋体"}[CNM]{lang="EN-US"}[报文数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1345992896}

[**[display qcn cp interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \] \[ **priority** *priority-value* \]]{lang="EN-US"}]{#struct_0_x2117_81929_x1915201336}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x882742764}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_x736273451}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x177187192}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x307476228}

[[network-operator]{lang="EN-US"}]{#struct_0_x2117_81929_1467275930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x1240100618}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2117_81929_x264351429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1811114624}

[*[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_1893870465}[：]{style="font-family:宋体;color:black"}[指定接口类型和接口编号]{style="font-family:宋体"}[。如果未指定本参数，将]{style="font-family:宋体;color:black"}[显示所有二层以太网接口下的统计信息。]{style="font-family:
宋体"}

[**[priority]{lang="EN-US"}***[ priority-value]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_1324963755}[：]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US" style="color:black"}[优先级，取值范围为]{style="font-family:宋体;
color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[7]{lang="EN-US" style="color:black"}[。如果未指定本参数，将]{style="font-family:宋体;color:black"}[显示设备加入的所有]{style="font-family:
宋体"}[CND]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1677627535}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_x1269138486}[显示所有二层以太网接口下的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qcn cp interface]{lang="EN-US"}]{#struct_0_x2117_81929_x1240428298}

[Interface: GE1/0/1]{lang="EN-US"}

[ CNPV 1: CP profile 1]{lang="EN-US"}

[  Passed   : 100000 (Packets)]{lang="EN-US"}

[  Discarded: 10 (Packets)]{lang="EN-US"}

[  CNM count: 3000 (Packets)]{lang="EN-US"}

[CNPV 2: CP profile default]{lang="EN-US"}

[  Passed   : 200000 (Packets)]{lang="EN-US"}

[  Discarded: 20 (Packets)]{lang="EN-US"}

[  CNM count: 3000 (Packets)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GE1/0/2]{lang="EN-US"}

[ CNPV 1: CP profile 1]{lang="EN-US"}

[  Passed   : 100000 (Packets)]{lang="EN-US"}

[  Discarded: 10 (Packets)]{lang="EN-US"}

[  CNM count: 3000 (Packets)]{lang="EN-US"}

[ CNPV 2: CP profile default]{lang="EN-US"}

[  Passed   : 200000 (Packets)]{lang="EN-US"}

[  Discarded: 20 (Packets)]{lang="EN-US"}

[  CNM count: 3000 (Packets)]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display qcn cp interface]{lang="EN-US"}]{#struct_0_x2117_81929_x189655163}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_816043758}[[字段]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1904636875}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2117_81929_334644478}

[[Interface]{lang="EN-US"}]{#struct_0_x2117_81929_506292580}

[[接口]{style="font-family:宋体;
  color:black"}]{#struct_0_x2117_81929_x1901950776}

[[CNPV]{lang="EN-US"}]{#struct_0_x2117_81929_1131626177}

[[CNPV]{lang="EN-US"}]{#struct_0_x2117_81929_x1240493834}[对应]{style="font-family:宋体"}[CDN]{lang="EN-US"}[绑定的]{style="font-family:宋体"}[profile]{lang="EN-US"}

[[Passed]{lang="EN-US"}]{#struct_0_x2117_81929_1991072252}

[[通过报文数]{style="font-family:宋体"}]{#struct_0_x2117_81929_x693342342}

[[Discarded]{lang="EN-US"}]{#struct_0_x2117_81929_61291689}

[[丢弃报文数]{style="font-family:宋体"}]{#struct_0_x2117_81929_495634453}

[[CNM count]{lang="EN-US"}]{#struct_0_x2117_81929_2055093632}

[[发送的]{style="font-family:宋体"}[CNM]{lang="EN-US"}]{#struct_0_x2117_81929_x1250444606}[报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1074796508}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset qcn cp interface]{lang="EN-US"}**]{#struct_0_x2117_81929_x1240297226}

::: {#-994892896 .myid}
[]{#_Toc404792139}[]{#struct_0_x2117_81929_x1663483076}[]{#_Toc340223539}

**QCN \-- QCN配置命令 \-- display qcn global**

------------------------------------------------------------------------

[**[display qcn global]{lang="EN-US"}**]{#struct_0_x2117_81929_463803873}[命令用来显示]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1294359312}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2117_81929_1493738831}

[**[display ]{lang="EN-US"}[qcn global]{lang="EN-US"}**]{#struct_0_x2117_81929_x2107788425}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2117_81929_106006868}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qcn global]{lang="EN-US"}**[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x2117_81929_1383182060}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2117_81929_1527942687}[模式：]{style="font-family:宋体"}

[**[display qcn global]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x2117_81929_288955382}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x808192393}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_x2126182494}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240362762}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_1096844706}

[[network-operator]{lang="EN-US"}]{#struct_0_x2117_81929_1328359953}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x1413591693}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2117_81929_107749948}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1925782296}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2117_81929_x1954931538}[：显示指定单板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2117_81929_x1277511957}[：显示指定成员设备上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示主用设备上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2117_81929_x878580578}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2117_81929_1755748306}[：显示指定成员设备指定单板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则显示全局主用主控板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2117_81929_x895810973}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x732903033}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_x1459923053}[显示]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的全局运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display qcn global chassis 1 slot 1]{lang="EN-US"}]{#struct_0_x2117_81929_x1240690442}

[Chassis 1 Slot 1:]{lang="EN-US"}

[QCN global status: Enabled]{lang="EN-US"}

[ CNPV  Mode   Defense-mode    Alternate  CP-profile]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 1     admin  interior-ready  4          default]{lang="EN-US"}

[ 2     auto   -               0          1]{lang="EN-US"}

[ 3     auto   -               0          1]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display qcn global]{lang="EN-US"}]{#struct_0_x2117_81929_699035850}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_809792958}[[字段]{style="font-family:黑体"}]{#struct_0_x2117_81929_513512877}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2117_81929_751741131}

[[QCN global status]{lang="EN-US"}]{#struct_0_x2117_81929_690386464}

[[QCN]{lang="EN-US" style="color:black"}]{#struct_0_x2117_81929_x796206635}[全局使能状态：]{style="font-family:宋体;color:black"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x2117_81929_1492717239}[：使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x2117_81929_x1240755978}[：未使能]{lang="EN-US" style="font-family:宋体"}

[[CNPV]{lang="EN-US"}]{#struct_0_x2117_81929_x1960157181}

[[拥塞通知优先级]{style="font-family:宋体"}]{#struct_0_x2117_81929_x1374327816}

[[Mode]{lang="EN-US"}]{#struct_0_x2117_81929_65676211}

[[模式选择方式：]{style="font-family:宋体"}]{#struct_0_x2117_81929_167819199}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_x2117_81929_2005581891}[：]{lang="EN-US" style="font-family:宋体"}[LLDP]{lang="EN-US"}[协商方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[admin]{lang="EN-US"}]{#struct_0_x2117_81929_1956285470}[：配置方式]{lang="EN-US" style="font-family:宋体"}

[[Defense-mode]{lang="EN-US"}]{#struct_0_x2117_81929_x1240166155}

[[端口保护模式：]{style="font-family:宋体"}]{#struct_0_x2117_81929_x1365289625}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_x2117_81929_1831502379}[：配置后，接口的优先级映射按优先级映射表起作用，不受任何]{lang="EN-US" style="font-family:宋体"}[QCN]{lang="EN-US"}[配置影响]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[edge]{lang="EN-US"}]{#struct_0_x2117_81929_962592169}[：]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[优先级的报文需要被改写成隔离优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interior]{lang="EN-US"}]{#struct_0_x2117_81929_x354302110}[：优先级保持不变，不按优先级映射表映射。同]{lang="EN-US" style="font-family:宋体"}[interiorReady]{lang="EN-US"}[模式的差异是，出方向需要删除]{lang="EN-US" style="font-family:宋体"}[CN tag]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interior-ready]{lang="EN-US"}]{#struct_0_x2117_81929_1552746739}[：优先级保持不变，不按优先级映射表映射。出方向时保留]{lang="EN-US" style="font-family:宋体"}[CN tag]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局下配置成]{style="font-family:宋体"}]{#struct_0_x2117_81929_x1240231691}[auto]{lang="EN-US"}[时，显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["，表示每个接口独立协商，无全局统一的保护模式]{style="font-family:宋体"}

[[Alternate]{lang="EN-US"}]{#struct_0_x2117_81929_116088751}

[[隔离优先级]{style="font-family:宋体"}]{#struct_0_x2117_81929_1873642240}

[[CP-profile]{lang="EN-US"}]{#struct_0_x2117_81929_x2062279177}

[[CP profile ID]{lang="EN-US"}]{#struct_0_x2117_81929_x1307076541}

[ ]{lang="EN-US"}

::: {#424948660 .myid}
[]{#_Toc404792140}[]{#struct_0_x2117_81929_321343544}[]{#_Toc340223540}

**QCN \-- QCN配置命令 \-- display qcn interface**

------------------------------------------------------------------------

[**[display qcn interface]{lang="EN-US"}**]{#struct_0_x2117_81929_2032294652}[命令用来显示]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的接口运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240035083}

[**[display qcn interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2117_81929_x1586661765}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1638779094}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_1745053922}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1551486780}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x1455396622}

[[network-operator]{lang="EN-US"}]{#struct_0_x2117_81929_x323476870}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_1472272423}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2117_81929_294198909}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1229828234}

[*[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_x2058907634}[：]{style="font-family:宋体;color:black"}[指定接口类型和接口编号]{style="font-family:宋体"}[。如果未指定本参数，将显示所有二层以太网接口的运行信息。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240100619}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_1301732512}[显示]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的接口运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display qcn interface]{lang="EN-US"}]{#struct_0_x2117_81929_x95667628}

[Interface: GE1/0/1]{lang="EN-US"}

[ CNPV  Mode   Defense-mode     Alternate]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 1     comp   interior-ready   4]{lang="EN-US"}

[ 2     admin  edge             0]{lang="EN-US"}

[ 3     auto   edge             0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GE1/0/2]{lang="EN-US"}

[ CNPV  Mode   Defense-mode     Alternate]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 1     comp   interior-ready   4]{lang="EN-US"}

[ 2     admin  edge             0]{lang="EN-US"}

[ 3     auto   edge             0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display qcn interface]{lang="EN-US"}]{#struct_0_x2117_81929_x1826539727}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_812273726}[[字段]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1984660952}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2117_81929_818645929}

[[Interface]{lang="EN-US"}]{#struct_0_x2117_81929_x1240428299}

[[接口]{style="font-family:宋体"}]{#struct_0_x2117_81929_1376428778}

[[CNPV]{lang="EN-US"}]{#struct_0_x2117_81929_x806973528}

[[拥塞通知优先级]{style="font-family:宋体"}]{#struct_0_x2117_81929_1122729258}

[[Mode]{lang="EN-US"}]{#struct_0_x2117_81929_x1593488137}

[[接口保护模式的选择方式，取值包括：]{style="font-family:宋体"}]{#struct_0_x2117_81929_x986440701}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_x2117_81929_x2012986134}[：]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[协商方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[admin]{lang="EN-US"}]{#struct_0_x2117_81929_876940124}[：配置方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[comp]{lang="EN-US"}]{#struct_0_x2117_81929_x1240493835}[：使用全局的保护模式。接口下配置的选择方式会覆盖全局的选择方式]{style="font-family:宋体"}

[[Defense-mode]{lang="EN-US"}]{#struct_0_x2117_81929_424988311}

[[端口保护模式]{style="font-family:宋体"}]{#struct_0_x2117_81929_139573457}

[[Alternate]{lang="EN-US"}]{#struct_0_x2117_81929_726805183}

[[隔离优先级]{style="font-family:宋体"}]{#struct_0_x2117_81929_x180113698}

[ ]{lang="EN-US"}

::::: {#-975203990 .myid}
[]{#_Toc404792141}[]{#struct_0_x2117_81929_x2083795003}[]{#_Toc340223541}

**QCN \-- QCN配置命令 \-- display qcn profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QCN命令.files/image001.png){#图片 134 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2117_81929_x2065852374}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2117_81929_x1240297227}
:::

[ ]{lang="EN-US"}

[**[display qcn profile]{lang="EN-US"}**]{#struct_0_x2117_81929_1065400279}[命令用来显示]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_308892485}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x2117_81929_x1332264902}

[**[display ]{lang="EN-US"}[qcn profile ]{lang="EN-US"}**[\[ *profile-id* \| **default** \]]{lang="EN-US"}]{#struct_0_x2117_81929_x2089174003}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2117_81929_1244937082}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qcn profile]{lang="EN-US"}**[ \[ *profile-id* \| **default** \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x2117_81929_x1474364496}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2117_81929_1954289542}[模式：]{style="font-family:宋体"}

[**[display qcn profile]{lang="EN-US"}**[ \[ *profile-id* \| **default** \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x2117_81929_1762940308}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_950227620}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_779889385}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1725817442}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x1240362763}

[[network-operator]{lang="EN-US"}]{#struct_0_x2117_81929_x1632038649}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x636692351}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2117_81929_422956047}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_442769157}

[*[profile-id]{lang="EN-US"}*]{#struct_0_x2117_81929_81368125}[：显示指定]{style="font-family:宋体"}[profile]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}*[profile-id]{lang="EN-US"}*[的取]{style="font-family:宋体"}[值范围与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_x2117_81929_841805669}[：显示缺省]{style="font-family:宋体"}[profile]{lang="EN-US"}[（即]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[）的运行信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2117_81929_1897924589}[：显示指定单板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x2117_81929_318974458}[：显示指定成员设备上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示主用设备上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x2117_81929_x1994325825}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2117_81929_x1100070537}[：显示指定成员设备指定单板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x2117_81929_x1472546793}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240690443}

[[如果未指定]{style="font-family:宋体"}*[profile-id]{lang="EN-US"}*]{#struct_0_x2117_81929_x867048091}[和]{style="font-family:宋体"}**[default]{lang="EN-US"}**[参数，将显示所有]{style="font-family:宋体"}[profile]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_327515007}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_1078733933}[显示]{style="font-family:宋体"}[QCN]{lang="EN-US"}[的]{style="font-family:宋体"}[profile]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display qcn profile chassis 2 slot 1]{lang="EN-US"}]{#struct_0_x2117_81929_x686511804}

[Chassis 2 Slot 1:]{lang="EN-US"}

[ Profile  Set-point   Weight]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ default  26000       1]{lang="EN-US"}

[ 1        30000       2]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display qcn profile]{lang="EN-US"}]{#struct_0_x2117_81929_x713836187}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_806158286}[[字段]{style="font-family:黑体"}]{#struct_0_x2117_81929_x13910946}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2117_81929_x688647609}

[[Profile]{lang="EN-US"}]{#struct_0_x2117_81929_1439736572}

[[CP profile]{lang="EN-US"}]{#struct_0_x2117_81929_x1240755979}[参数]{style="font-family:宋体"}

[[Set-point]{lang="EN-US"}]{#struct_0_x2117_81929_768726174}

[[期望队列，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_x2117_81929_x1874013624}

[[Weight]{lang="EN-US"}]{#struct_0_x2117_81929_940417195}

[[权重]{style="font-family:宋体"}]{#struct_0_x2117_81929_x1048791437}

[ ]{lang="EN-US"}

::: {#86993264 .myid}
[]{#_Toc404792142}[]{#struct_0_x2117_81929_787728031}

**QCN \-- QCN配置命令 \-- qcn enable**

------------------------------------------------------------------------

[**[qcn enable]{lang="EN-US"}**]{#struct_0_x2117_81929_x706208962}[命令用来开启]{style="font-family:宋体"}[QCN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo qcn enable]{lang="EN-US"}**]{#struct_0_x2117_81929_785552785}[命令用来关闭]{style="font-family:宋体"}[QCN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1443964240}

[**[qcn enable]{lang="EN-US"}**]{#struct_0_x2117_81929_x1240166156}

[**[undo qcn enable]{lang="EN-US"}**]{#struct_0_x2117_81929_x1768574152}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x5563777}

[[QCN]{lang="EN-US"}]{#struct_0_x2117_81929_2143413134}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1046756543}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_x750946076}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_354170696}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_409042906}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_220146365}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1272095567}

[[开启]{style="font-family:宋体"}[QCN]{lang="EN-US"}]{#struct_0_x2117_81929_1188139742}[功能后，其它]{style="font-family:宋体"}[QCN]{lang="EN-US"}[配置才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240231692}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_519373278}[开启]{style="font-family:宋体"}[QCN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_81929_1034641170}

[\[Sysname\] qcn enable]{lang="EN-US"}
:::

::: {#1057743774 .myid}
[]{#_Toc340223535}[]{#_Toc404792143}[]{#struct_0_x2117_81929_612868151}[]{#_Toc340223537}

**QCN \-- QCN配置命令 \-- qcn port priority**

------------------------------------------------------------------------

[**[qcn port priority]{lang="EN-US"}**]{#struct_0_x2117_81929_351308241}[命令用来配置指定接口指定优先级的保护模式选择方式。]{style="font-family:宋体"}

[**[undo qcn port priority]{lang="EN-US"}**]{#struct_0_x2117_81929_896471917}[命令用来]{style="font-family:宋体"}[恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x153862898}

[**[qcn port priority]{lang="EN-US"}**[ *priority-value* { **admin** \[ **defense-mode** { **disabled** \| **edge** \| **interior** \| **interior-ready** } **alternate** *alternate-value* \] \| **auto** }]{lang="EN-US"}]{#struct_0_x2117_81929_x1661138466}

[**[undo]{lang="EN-US"}**[ **qcn** **port** **priority** *priority-value*]{lang="EN-US"}]{#struct_0_x2117_81929_911065560}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1015512996}

[[以全局配置为准。]{style="font-family:宋体"}]{#struct_0_x2117_81929_x1340599914}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240035084}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_x827146878}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1614485402}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_1203790449}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_1109533581}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x109138252}

[*[priority-value]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_x2128374348}[：]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US" style="color:black"}[优先级，取值范围为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[7]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[**[admin]{lang="EN-US"}**]{#struct_0_x2117_81929_x678528186}[：]{style="font-family:宋体;color:black"}[配置方式。]{style="font-family:宋体"}

[**[defense-mode]{lang="EN-US"}**]{#struct_0_x2117_81929_x1423876721}[：接口]{style="font-family:宋体;color:black"}[保护模式，缺省为]{style="font-family:宋体"}[disabled]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[disabled]{lang="EN-US"}**]{#struct_0_x2117_81929_652160793}[：]{style="font-family:宋体;color:black"}[接口的优先级映射按优先级映射表起作用，不受]{style="font-family:宋体"}[QCN]{lang="EN-US"}[配置影响。]{style="font-family:宋体"}

[**[edge]{lang="EN-US"}**]{#struct_0_x2117_81929_1450877082}[：]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US"}[优先级的报文需要被改写成隔离优先级。]{style="font-family:宋体"}

[**[interior]{lang="EN-US"}**]{#struct_0_x2117_81929_x2011761708}[：]{style="font-family:宋体;color:black"}[优先级保持不变，不按优先级映射表映射。出方向时删掉]{style="font-family:宋体"}[CN tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interior-ready]{lang="EN-US"}**]{#struct_0_x2117_81929_x1240100620}[：]{style="font-family:宋体;color:black"}[优先级保持不变，不按优先级映射表映射。出方向时保留]{style="font-family:宋体"}[CN tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[alternate ]{lang="EN-US"}***[alternate-value]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_x620385181}[：隔离优先级，取值范围为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[7]{lang="EN-US" style="color:black"}[，缺省为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[。此隔离优先级不能和已有]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US" style="color:black"}[域冲突。]{style="font-family:宋体;
color:black"}

[**[auto]{lang="EN-US"}**]{#struct_0_x2117_81929_1462281021}[：]{style="font-family:宋体;color:black"}[LLDP]{lang="EN-US"}[协商方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1295108263}

[[如果设备还没有加入对应]{style="font-family:宋体"}[CND]{lang="EN-US"}]{#struct_0_x2117_81929_220771256}[，不能在接口下配置保护模式选择方式。]{style="font-family:宋体"}

[[对于接口而言，接口下的配置优于全局配置生效。]{style="font-family:宋体"}]{#struct_0_x2117_81929_927018522}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1037258561}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_1621516789}[配置在]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[CND]{lang="EN-US"}[中接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的保护模式为]{style="font-family:宋体"}[disabled]{lang="EN-US"}[，隔离优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_81929_x62240242}

[\[Sysname\] qcn priority 1 auto]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qcn port priority 1 admin defense-mode disabled alternate 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_x593237361}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[的模式选择方式为]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[协商方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_81929_x1240428300}

[\[Sysname\] qcn priority 2 admin]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] qcn port priority 2 auto]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_165985372}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qcn priority]{lang="EN-US"}**]{#struct_0_x2117_81929_x358955463}
:::

::: {#-1450918647 .myid}
[]{#_Toc404792144}[]{#struct_0_x2117_81929_x279335967}

**QCN \-- QCN配置命令 \-- qcn priority**

------------------------------------------------------------------------

[**[qcn priority]{lang="EN-US"}**]{#struct_0_x2117_81929_743858165}[命令用来配置]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[，加入]{style="font-family:宋体"}[CND]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo qcn priority]{lang="EN-US"}**]{#struct_0_x2117_81929_1990755932}[命令用来退出]{style="font-family:宋体"}[CND]{lang="EN-US"}[，同时删除此]{style="font-family:宋体"}[CND]{lang="EN-US"}[下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x294930912}

[**[qcn priority ]{lang="EN-US"}***[priority-value]{lang="EN-US"}*[ { **admin** \[ **defense-mode** { **disabled** \| **edge** \| **interior** \| **interior-ready** } **alternate** *alternate-value* \] \| **auto** }]{lang="EN-US"}]{#struct_0_x2117_81929_222307979}

[**[undo qcn priority ]{lang="EN-US"}***[priority-value]{lang="EN-US"}*]{#struct_0_x2117_81929_1204764875}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_81929_638973436}

[[设备未加入任何]{style="font-family:宋体"}[CND]{lang="EN-US"}]{#struct_0_x2117_81929_x93639856}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240493836}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_x1141095630}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1385891138}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x950998266}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_473143232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x180950573}

[*[priority-value]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_x936950454}[：]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US" style="color:black"}[优先级，取值范围为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[7]{lang="EN-US" style="color:black"}[。此]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US" style="color:black"}[优先级不能和全局或者接口下的]{style="font-family:宋体;
color:black"}[admin]{lang="EN-US" style="color:black"}[模式下的隔离优先级冲突。]{style="font-family:宋体;color:black"}

[**[admin]{lang="EN-US"}**]{#struct_0_x2117_81929_x1969888523}[：]{style="font-family:宋体;color:black"}[配置方式。]{style="font-family:宋体"}

[**[defense-mode]{lang="EN-US"}**]{#struct_0_x2117_81929_x169542358}[：接口]{style="font-family:宋体;color:black"}[保护模式，缺省为]{style="font-family:宋体"}[interior]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[disabled]{lang="EN-US"}**]{#struct_0_x2117_81929_x218428832}[：]{style="font-family:宋体;color:black"}[接口的优先级映射按优先级映射表起作用，不受]{style="font-family:宋体"}[QCN]{lang="EN-US"}[配置影响。]{style="font-family:宋体"}

[**[edge]{lang="EN-US"}**]{#struct_0_x2117_81929_x388008074}[：]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US"}[优先级的报文需要被改写成隔离优先级。]{style="font-family:宋体"}

[**[interior]{lang="EN-US"}**]{#struct_0_x2117_81929_x1593270485}[：]{style="font-family:宋体;color:black"}[优先级保持不变，不按优先级映射表映射。出方向时删掉]{style="font-family:宋体"}[CN tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interior-ready]{lang="EN-US"}**]{#struct_0_x2117_81929_x1240297228}[：]{style="font-family:宋体;color:black"}[优先级保持不变，不按优先级映射表映射。出方向时保留]{style="font-family:宋体"}[CN tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[alternate]{lang="EN-US"}***[ alternate-value]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_x500683662}[：隔离优先级，取值范围为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[7]{lang="EN-US" style="color:black"}[，缺省为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[。此隔离优先级不能和已有]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US" style="color:black"}[域冲突。]{style="font-family:宋体;
color:black"}

[**[auto]{lang="EN-US"}**]{#struct_0_x2117_81929_x645366518}[：]{style="font-family:宋体;color:black"}[LLDP]{lang="EN-US"}[协商方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x973712023}

[[配置]{style="font-family:宋体"}**[auto]{lang="EN-US"}**]{#struct_0_x2117_81929_1788212131}[方式后，接口保护模式由]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[协商得到，隔离优先级为小于]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[且最接近]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[的优先级值，如果小于]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[的优先级值都被域占用，隔离优先级为大于]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[且最接近]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[的未被占用的优先级值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x353333636}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_1667929178}[配置设备加入]{style="font-family:宋体"}[CND]{lang="EN-US"}[，]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，模式选择方式为]{style="font-family:
宋体"}[LLDP]{lang="EN-US"}[协商方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_81929_x194436500}

[\[Sysname\] qcn priority 2 auto]{lang="EN-US"}

[\# ]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[配置设备加入]{style="font-size:10.5pt;font-family:宋体"}[CND]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[，]{style="font-size:10.5pt;font-family:宋体"}[CNPV]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[为]{style="font-size:10.5pt;font-family:宋体"}[1]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[，模式选择方式为配置方式，保护模式为]{style="font-size:10.5pt;font-family:宋体"}[disabled]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[，隔离优先级为]{style="font-size:10.5pt;font-family:宋体"}[0]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[。]{style="font-size:10.5pt;font-family:宋体"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] qcn priority 1 admin defense-mode disabled alternate 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x687337637}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qcn ]{lang="EN-US"}**]{#struct_0_x2117_81929_x1240362764}**[port ]{lang="EN-US"}[priority]{lang="EN-US"}**
:::

::::: {#-2098922015 .myid}
[]{#_Toc404792145}[]{#struct_0_x2117_81929_1903413760}[]{#_Toc340223536}

**QCN \-- QCN配置命令 \-- qcn priority profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QCN命令.files/image001.png){#图片 129 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2117_81929_403812041}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2117_81929_1105461174}
:::

[ ]{lang="EN-US"}

[**[qcn priority]{lang="EN-US"}***[ ]{lang="EN-US"}***[profile]{lang="EN-US"}**]{#struct_0_x2117_81929_950507518}[命令用来为指定]{style="font-family:宋体"}[CND]{lang="EN-US"}[绑定]{style="font-family:宋体"}[profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo qcn priority proflie]{lang="EN-US"}**]{#struct_0_x2117_81929_x1292597120}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1461811239}

[**[qcn priority ]{lang="EN-US"}***[priority-value ]{lang="EN-US"}***[profile ]{lang="EN-US"}***[profile-id]{lang="EN-US"}*]{#struct_0_x2117_81929_1107051869}

[**[undo qcn priority ]{lang="EN-US"}***[priority-value ]{lang="EN-US"}***[proflie]{lang="EN-US"}**]{#struct_0_x2117_81929_780834955}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1710039931}

[[CND]{lang="EN-US"}]{#struct_0_x2117_81929_x1453574812}[绑定缺省]{style="font-family:宋体"}[profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240690444}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_1861835264}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1031182801}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_876281394}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x1361916879}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1610344324}

[*[priority-value]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_x520808622}[：]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US" style="color:black"}[优先级，取值范围为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[7]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[*[profile-id]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_x2113952075}[：]{style="font-family:
宋体;color:black"}[指定的]{style="font-family:宋体"}[profile ID]{lang="EN-US"}[。此处不包括缺省]{style="font-family:宋体"}[profile ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1605714767}

[[如果设备还没有加入对应]{style="font-family:宋体"}[CND]{lang="EN-US"}]{#struct_0_x2117_81929_1477506542}[或指定的]{style="font-family:宋体"}[profile]{lang="EN-US"}[不存在，则不能绑定]{style="font-family:宋体"}[profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1598353410}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_x1240755980}[为]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[值为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[CND]{lang="EN-US"}[绑定]{style="font-family:宋体"}[profile 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_81929_1979562795}

[\[Sysname\] qcn priority 2 profile 2]{lang="EN-US"}
:::::

::::: {#-1236169342 .myid}
[]{#_Toc404792146}[]{#struct_0_x2117_81929_820452771}[]{#_Toc340223538}

**QCN \-- QCN配置命令 \-- qcn proflie**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QCN命令.files/image001.png){#图片 131 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2117_81929_x2128700674}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2117_81929_1977406788}
:::

[ ]{lang="EN-US"}

[**[qcn profile]{lang="EN-US"}**]{#struct_0_x2117_81929_1787818029}[命令用来创建]{style="font-family:宋体"}[profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo qcn profile]{lang="EN-US"}**]{#struct_0_x2117_81929_x1698967149}[命令用来删除]{style="font-family:宋体"}[profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x2023234185}

[**[qcn profile]{lang="EN-US"}***[ profile-id ]{lang="EN-US"}***[set-point]{lang="EN-US"}***[ length-value]{lang="EN-US"}***[ weight ]{lang="EN-US"}***[weight-value]{lang="EN-US"}*]{#struct_0_x2117_81929_x428450009}

[**[undo qcn profile ]{lang="EN-US"}***[profile-id]{lang="EN-US"}*]{#struct_0_x2117_81929_294322520}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2117_81929_255777090}

[[没有创建]{style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_x2117_81929_x1240166157}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x202490211}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_x57347743}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1999915400}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_322942295}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_1569592603}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1056717918}

[*[profile-id]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_x118360972}[：]{style="font-family:
宋体;color:black"}[指定的]{style="font-family:宋体"}[profile ID]{lang="EN-US"}[。系统自动创建缺省]{style="font-family:宋体"}[profile]{lang="EN-US"}[，]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，参数不能修改。本参数的取值范围]{style="font-family:
宋体"}[与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[set-point]{lang="EN-US"}**[ *length-value*]{lang="EN-US" style="color:black"}]{#struct_0_x2117_81929_1518981699}[：期望队列长度，]{style="font-family:宋体;color:black"}[单位为]{style="font-family:
宋体"}[byte]{lang="EN-US"}[。]{style="font-family:宋体"}[取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight ]{lang="EN-US"}***[weight-value]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_2059702121}[：权重参数]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}[取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1122226371}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_x1240231693}[创建]{style="font-family:宋体"}[profile]{lang="EN-US"}[，]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，期望队列长度为]{style="font-family:
宋体"}[28000bytes]{lang="EN-US"}[，权重为]{style="font-family:
宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2117_81929_x1046710663}

[\[Sysname\] qcn profile 1 set-point 28000 weight 1]{lang="EN-US"}
:::::

::: {#633485604 .myid}
[]{#_Toc404792147}[]{#struct_0_x2117_81929_81352951}[]{#_Toc340223543}

**QCN \-- QCN配置命令 \-- reset qcn cp interface**

------------------------------------------------------------------------

[**[reset qcn cp interface]{lang="EN-US"}**]{#struct_0_x2117_81929_x1711816926}[命令用来清除]{style="font-family:宋体"}[CP]{lang="EN-US"}[端的统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_2026298049}

[**[reset qcn cp interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \] \[ **priority** *priority-value* \]]{lang="EN-US"}]{#struct_0_x2117_81929_313052145}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2117_81929_1068996704}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2117_81929_374476359}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x854210862}

[[network-admin]{lang="EN-US"}]{#struct_0_x2117_81929_x297995807}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2117_81929_1569293403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1240035085}

[*[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_x2117_81929_1901736477}[：]{style="font-family:宋体;color:black"}[指定接口类型和接口编号]{style="font-family:宋体"}[。如果未指定本参数，将]{style="font-family:宋体;color:black"}[清除所有二层[以太网接口]{style="color:black"}下的统计信息。]{style="font-family:
宋体"}

[**[priority]{lang="EN-US"}**[ *[priority-value]{style="color:black"}*]{lang="EN-US"}]{#struct_0_x2117_81929_928779462}[：]{style="font-family:宋体;color:black"}[CNPV]{lang="EN-US" style="color:black"}[优先级，取值范围为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[7]{lang="EN-US" style="color:black"}[。如果未指定本参数，将]{style="font-family:宋体;color:black"}[清除对应接口加入的所有]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[域统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2117_81929_318728071}

[[\# ]{lang="EN-US"}]{#struct_0_x2117_81929_x119771475}[清除所有域所有二层[以太网接口]{style="color:black"}]{style="font-family:宋体"}[CP]{lang="EN-US"}[端的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset qcn cp interface]{lang="EN-US"}]{#struct_0_x2117_81929_x770417116}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2117_81929_x1929492090}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ qcn cp interface]{lang="EN-US"}**]{#struct_0_x2117_81929_756397992}
:::
