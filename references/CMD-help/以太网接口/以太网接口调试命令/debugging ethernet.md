::: {#279785751 .myid}
[]{#_Toc404783371}[]{#struct_0_70922_x4169_x976545837}[]{#_Toc350104370}

**以太网接口 \-- 以太网接口调试命令 \-- debugging ethernet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_70922_x4169_x938975184}

[**[debugging ethernet]{lang="EN-US"}**[ {]{lang="EN-US"}]{#struct_0_70922_x4169_x553018375}**[ packet]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[event]{lang="EN-US"}**[ } \[ ]{lang="EN-US"}**[interface]{lang="EN-US"}**[ *interface-type interface-number* \]]{lang="EN-US"}

[**[undo debugging ethernet ]{lang="EN-US"}**[{]{lang="EN-US"}]{#struct_0_70922_x4169_1362808335}**[ packet ]{lang="EN-US"}**[\| ]{lang="EN-US"}**[event ]{lang="EN-US"}**[}]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_70922_x4169_887926253}

[[用户视图]{style="font-family:宋体"}]{#struct_0_70922_x4169_642070539}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_70922_x4169_1243199354}

[[network-admin]{lang="EN-US"}]{#struct_0_70922_x4169_144006447}

[[network-operator]{lang="EN-US"}]{#struct_0_70922_x4169_x189697681}

[[mdc-admin]{lang="EN-US"}]{#struct_0_70922_x4169_x1119902971}

[[mdc-operator]{lang="EN-US"}]{#struct_0_70922_x4169_x2054677449}

[[【参数】]{style="font-family:黑体"}]{#struct_0_70922_x4169_1678194800}

[**[packet]{lang="EN-US"}**]{#struct_0_70922_x4169_427493203}[：表示收发以太网报文的调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_70922_x4169_1363004943}[：表示以太网事件的调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_70922_x4169_2059609660}[：表示指定接口的调试信息开关。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:
宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_70922_x4169_x375699183}

[**[debugging ethernet]{lang="EN-US"}**]{#struct_0_70922_x4169_x271980202}[命令用来打开以太网接口模块报文调试信息开关。]{style="font-family:宋体"}**[undo debugging ethernet]{lang="EN-US"}**[命令用来关闭以太网接口模块报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，以太网接口模块报文调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_70922_x4169_917963492}

[[表1-1 ]{lang="EN-US"}[debugging ethernet]{lang="EN-US"}]{#struct_0_70922_x4169_x892459817}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x121276124}[[字段]{style="font-family:黑体"}]{#struct_0_70922_x4169_x540341071}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_70922_x4169_1132234144}

[[Eth_rcv: Received an ethernet packet]{lang="EN-US"}]{#struct_0_70922_x4169_545473269}

[[接收一个以太网报文]{style="font-family:宋体"}]{#struct_0_70922_x4169_1362939407}

[[Eth_send: Sent an ethernet packet]{lang="EN-US"}]{#struct_0_70922_x4169_119939688}

[[发送一个以太网报文]{style="font-family:宋体"}]{#struct_0_70922_x4169_x632012290}

[[interface]{lang="EN-US"}]{#struct_0_70922_x4169_1858849501}

[[收发报文的接口]{style="font-family:宋体"}]{#struct_0_70922_x4169_1285444678}

[[format: x]{lang="EN-US"}]{#struct_0_70922_x4169_x1939846825}

[[以太网帧的封装格式：]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_70922_x4169_1363136015}[表示]{style="font-family:宋体"}[ETH_II]{lang="EN-US"}[封装，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示]{style="font-family:宋体"}[SNAP]{lang="EN-US"}[封装]{style="font-family:宋体"}

[[src_addr: x--x-x]{lang="EN-US"}]{#struct_0_70922_x4169_x1510731952}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_70922_x4169_582347078}[地址]{style="font-family:宋体"}

[[dst_addr: x--x-x]{lang="EN-US"}]{#struct_0_70922_x4169_x1244519592}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_70922_x4169_x114965187}[地址]{style="font-family:宋体"}

[[payload: x x x ]{lang="EN-US"}]{#struct_0_70922_x4169_x1279184677}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_70922_x4169_1363070479}[之后的报文以太网头信息，以]{style="font-family:宋体"}[16]{lang="EN-US"}[进制格式打印]{style="font-family:宋体"}

[[Eth_event: Received LINKUP message]{lang="EN-US"}]{#struct_0_70922_x4169_68899793}

[[接收到链路上行事件的消息]{style="font-family:宋体"}]{#struct_0_70922_x4169_x72010086}

[[Eth_event: Received LINKDOWN message]{lang="EN-US"}]{#struct_0_70922_x4169_1296695506}

[[接收到链路下行事件的消息]{style="font-family:宋体"}]{#struct_0_70922_x4169_x1935755716}

[[Eth_event: Received IF message]{lang="EN-US"}]{#struct_0_70922_x4169_1091780397}

[[接收到接口事件消息]{style="font-family:宋体"}]{#struct_0_70922_x4169_1363267087}

[[Eth_event: Notified LAGG line status change message]{lang="EN-US"}]{#struct_0_70922_x4169_1233683523}

[[通知聚合链路状态变化的消息]{style="font-family:宋体"}]{#struct_0_70922_x4169_x1772058254}

[[Ifindex *x*]{lang="EN-US"}]{#struct_0_70922_x4169_x947272444}

[[接口索引值为]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_70922_x4169_x1165023374}

[[type *x*]{lang="EN-US"}]{#struct_0_70922_x4169_1363201551}

[[事件子类型为]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_70922_x4169_461818028}

[[status from *x* to *y*]{lang="EN-US"}]{#struct_0_70922_x4169_1328934856}

[[状态从]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_70922_x4169_x585932718}[变到]{style="font-family:宋体"}*[y]{lang="EN-US"}*

[[process return *x*]{lang="EN-US"}]{#struct_0_70922_x4169_1362742796}

[[处理返回值为]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_70922_x4169_1650474138}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_70922_x4169_x210873821}

[[\# ]{lang="EN-US"}]{#struct_0_70922_x4169_x516590254}[打开收发以太网报文的调试信息开关，两台设备直连，进行]{style="font-family:宋体"}**[ping]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[\<Sysname\> debugging ethernet packet]{lang="EN-US"}]{#struct_0_70922_x4169_1427100288}

[\<Sysname\> ping 20.10.3.100]{lang="EN-US"}

[ PING 20.10.3.100: 56  data bytes, press CTRL_C to break]{lang="EN-US"}

[\*Dec  8 09:58:04:957 2006 Sysname ETH/7/Eth_send: Sent an ethernet packet, interface: Vlan-interface1, format: 0, src_addr: 000f-e249-8048, dst_addr: ffff-ffff-ffff, payload: 08 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_70922_x4169_92287929}*[发送一个以太网报文，发送接口为]{style="font-family:宋体"}[Vlan-interface1]{lang="EN-US"}[，以太帧格式为]{style="font-family:宋体"}[ETHII]{lang="EN-US"}[，发送者]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000f-e249-8048]{lang="EN-US"}[，目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[ffff-ffff-ffff]{lang="EN-US"}[，以太头源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[后面的数据为]{style="font-family:宋体"}[0800]{lang="EN-US"}*

[[\*Dec  8 09:58:04:957 2006 Sysname ETH/7/Eth_rcv: Received an ethernet packet, interface: GigabitEthernet1/0/3, format: 0, src_addr: 0015-e944-a947, dst_addr: 000f-e249-8048, payload: 81 00 00 02 08 00]{lang="EN-US"}]{#struct_0_70922_x4169_902237760}

[*[// ]{lang="EN-US"}*]{#struct_0_70922_x4169_609803632}*[接收一个以太网报文，接收接口为]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[，以太帧格式为]{style="font-family:宋体"}[ETHII]{lang="EN-US"}[，发送者]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0015-e944-a947]{lang="EN-US"}[，目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[000f-e249-8048]{lang="EN-US"}[，以太头源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[后面的数据为]{style="font-family:宋体"}[810000020800]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_70922_x4169_1362677260}[打开以太网事件的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ethernet event]{lang="EN-US"}]{#struct_0_70922_x4169_825459649}

[\*Oct 24 11:37:16:425 2012 Sysname ETH/7/Eth_event: -MDC=1; Received IF message, type 1073741888, ifindex 0, process return 0.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_70922_x4169_2139652778}*[接收到接口事件信息，类型为]{style="font-family:宋体"}[1073741888]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，处理返回值为]{style="font-family:宋体"}[0. ]{lang="EN-US"}*

[[\*Oct 24 11:37:16:426 2012 Sysname ETH/7/Eth_event: -MDC=1; Received LINKUP message, type 5, ifindex 2, process return 0.    ]{lang="EN-US"}]{#struct_0_70922_x4169_879161877}

[*[//]{lang="EN-US"}*]{#struct_0_70922_x4169_376229172}*[接收到链路上行事件信息，类型为]{style="font-family:宋体"}[5]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[2]{lang="EN-US"}[，处理返回值为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Oct 24 11:37:16:426 2012 Sysname ETH/7/Eth_event: -MDC=1; Received LINKDOWN message, type 35, ifindex 2, process return 0. ]{lang="EN-US"}]{#struct_0_70922_x4169_x1360412764}

[*[//]{lang="EN-US"}*]{#struct_0_70922_x4169_x1107551543}*[接收到链路下行事件信息，类型为]{style="font-family:宋体"}[35]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[2]{lang="EN-US"}[，处理返回值为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Oct 24 11:01:00:902 2012 Sysname ETH/7/Eth_event: -MDC=1; Notified LAGG line status change message, ifindex 2, status from 0 to 1. ]{lang="EN-US"}]{#struct_0_70922_x4169_411196058}

[*[//]{lang="EN-US"}*]{#struct_0_70922_x4169_x1778061615}*[通知]{style="font-family:宋体"}[LAGG]{lang="EN-US"}[线路状态更新，接口索引为]{style="font-family:宋体"}[2]{lang="EN-US"}[，状态从]{style="font-family:宋体"}[0]{lang="EN-US"}[变为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[表1-2 ]{lang="EN-US"}[debugging ethernet]{lang="EN-US"}]{#struct_0_70922_x4169_1362873868}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x125155291}[[字段]{style="font-family:黑体"}]{#struct_0_70922_x4169_882618523}

[[描述]{style="font-family:黑体"}]{#struct_0_70922_x4169_1277095864}

[[Eth_rcv: Received an ethernet packet]{lang="EN-US"}]{#struct_0_70922_x4169_x1831824674}

[[接收一个以太网报文]{style="font-family:宋体"}]{#struct_0_70922_x4169_393273128}

[[Eth_send: Sent an ethernet packet]{lang="EN-US"}]{#struct_0_70922_x4169_x1311598567}

[[发送一个以太网报文]{style="font-family:宋体"}]{#struct_0_70922_x4169_71099326}

[[interface]{lang="EN-US"}]{#struct_0_70922_x4169_1362808332}

[[收发报文的接口]{style="font-family:宋体"}]{#struct_0_70922_x4169_887729645}

[[format: x]{lang="EN-US"}]{#struct_0_70922_x4169_445713009}

[[以太网帧的封装格式：]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_70922_x4169_1490423732}[表示]{style="font-family:宋体"}[ETH_II]{lang="EN-US"}[封装，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示]{style="font-family:宋体"}[SNAP]{lang="EN-US"}[封装]{style="font-family:宋体"}

[[src_addr: x--x-x]{lang="EN-US"}]{#struct_0_70922_x4169_323025497}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_70922_x4169_x1192478232}[地址]{style="font-family:宋体"}

[[dst_addr: x--x-x]{lang="EN-US"}]{#struct_0_70922_x4169_1363004940}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_70922_x4169_2059413052}[地址]{style="font-family:宋体"}

[[payload: x x x ]{lang="EN-US"}]{#struct_0_70922_x4169_x1514292416}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_70922_x4169_2010729341}[之后的报文以太网头信息，以]{style="font-family:宋体"}[16]{lang="EN-US"}[进制格式打印]{style="font-family:宋体"}

[[Eth_event: Received LINKUP message]{lang="EN-US"}]{#struct_0_70922_x4169_337782982}

[[接收到链路上行事件的消息（物理层通知链路层的事件为上行事件）]{style="font-family:宋体"}]{#struct_0_70922_x4169_x416869976}

[[Eth_event: Received LINKDOWN message]{lang="EN-US"}]{#struct_0_70922_x4169_1362939404}

[[接收到链路下行事件的消息（网络层通知链路层的事件为下行事件）]{style="font-family:宋体"}]{#struct_0_70922_x4169_119874152}

[[Eth_event: Received IF message]{lang="EN-US"}]{#struct_0_70922_x4169_x957291597}

[[接收到接口事件消息]{style="font-family:宋体"}]{#struct_0_70922_x4169_549289283}

[[Eth_event: Notified LAGG line status change message]{lang="EN-US"}]{#struct_0_70922_x4169_584604940}

[[通知聚合链路状态变化的消息]{style="font-family:宋体"}]{#struct_0_70922_x4169_1363136012}

[[Ifindex *x*]{lang="EN-US"}]{#struct_0_70922_x4169_x1510273200}

[[接口索引值为]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_70922_x4169_2057351835}

[[type *x*]{lang="EN-US"}]{#struct_0_70922_x4169_571319123}

[[事件子类型为]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_70922_x4169_x1926922393}

[[status from *x* to *y*]{lang="EN-US"}]{#struct_0_70922_x4169_1363070476}

[[状态从]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_70922_x4169_69882833}[变到]{style="font-family:宋体"}*[y]{lang="EN-US"}*

[[process return *x*]{lang="EN-US"}]{#struct_0_70922_x4169_x2050428365}

[[处理返回值为]{style="font-family:宋体"}*[x]{lang="EN-US"}*]{#struct_0_70922_x4169_463971460}

[ ]{lang="EN-US"}

::: {#1603442096 .myid}
[]{#_Toc404783372}[]{#struct_0_70922_x4169_x475517424}[]{#_Toc343093673}

**以太网接口 \-- 以太网接口调试命令 \-- debugging ifmgr**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_70922_x4169_x1826928283}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_70922_x4169_1363267084}

[**[debugging ifmgr]{lang="EN-US"}**]{#struct_0_70922_x4169_1233749059}

[**[undo]{lang="EN-US"}**[ **debugging ifmgr**]{lang="EN-US"}]{#struct_0_70922_x4169_x995605252}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_70922_x4169_601916475}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging ifmgr ]{lang="EN-US"}**[\[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_70922_x4169_x1762543186}

[**[undo]{lang="EN-US"}**[ **debugging ifmgr** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_70922_x4169_1363201548}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_70922_x4169_461228205}[模式：]{style="font-family:宋体"}

[**[debugging]{lang="EN-US"}**[ **ifmgr** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_70922_x4169_x585169112}

[**[undo]{lang="EN-US"}**[ **debugging** **ifmgr** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_70922_x4169_x1414786008}

[[【视图】]{style="font-family:黑体"}]{#struct_0_70922_x4169_2026658511}

[[用户视图]{style="font-family:宋体"}]{#struct_0_70922_x4169_x870462342}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_70922_x4169_x779621447}

[[network-admin]{lang="EN-US"}]{#struct_0_70922_x4169_1362742797}

[[network-operator]{lang="EN-US"}]{#struct_0_70922_x4169_1650539674}

[[mdc-admin]{lang="EN-US"}]{#struct_0_70922_x4169_543511719}

[[mdc-operator]{lang="EN-US"}]{#struct_0_70922_x4169_x426072528}

[[【参数】]{style="font-family:黑体"}]{#struct_0_70922_x4169_x336991828}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_941649499}[：表示单板所在的槽位号。不指定该参数时，表示设置所有单板的调试开关。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_1362677261}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示设置所有单板的调试开关。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_971305989}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示设置所有单板的调试开关。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_825394113}[：]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的设置所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的调试开关。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_1551323890}[：]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的调试开关。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_70922_x4169_1126571775}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_70922_x4169_318556967}

[**[debugging ifmgr]{lang="EN-US"}**]{#struct_0_70922_x4169_1362873869}[命令用来打开接口管理模块调试信息开关。]{style="font-family:宋体"}**[undo debugging ifmgr]{lang="EN-US"}**[命令用来关闭接口管理模块调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，接口管理模块调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_70922_x4169_882552987}

[[【举例】]{style="font-family:黑体"}]{#struct_0_70922_x4169_x1753127276}

[[\# ]{lang="EN-US"}]{#struct_0_70922_x4169_693410784}[打开接口管理模块调试信息的开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ifmgr]{lang="EN-US"}]{#struct_0_70922_x4169_1362808333}
:::

::: {#-1065923754 .myid}
[]{#_Toc404783373}[]{#struct_0_70922_x4169_887795181}[]{#_Toc350519642}[]{#_Toc350515357}[]{#_Toc350519585}[]{#_Toc350519586}[]{#_Toc350519587}[]{#_Toc350519588}[]{#_Toc350519589}[]{#_Toc350519590}[]{#_Toc350519591}[]{#_Toc350519592}[]{#_Toc350519593}[]{#_Toc350519594}[]{#_Toc350519595}[]{#_Toc350519596}[]{#_Toc350519597}[]{#_Toc350519598}[]{#_Toc350519626}[]{#_Toc350519627}[]{#_Toc350519628}[]{#_Toc350519629}[]{#_Toc350519630}[]{#_Toc350519631}[]{#_Toc350519632}[]{#_Toc350519633}[]{#_Toc350519634}[]{#_Toc350519635}[]{#_Toc350519636}[]{#_Toc350519637}[]{#_Toc350519638}[]{#_Toc350519639}[]{#_Toc350519640}[]{#_Toc350519641}

**以太网接口 \-- 以太网接口调试命令 \-- debugging system-event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_70922_x4169_791468827}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_70922_x4169_1574080334}

[**[debugging system-event]{lang="EN-US"}**]{#struct_0_70922_x4169_1884304649}

[**[undo]{lang="EN-US"}**[ **debugging system-event**]{lang="EN-US"}]{#struct_0_70922_x4169_1453214205}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_70922_x4169_x1749462297}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging system-event]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_70922_x4169_1363004941}

[**[undo]{lang="EN-US"}**[ **debugging system-event** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_70922_x4169_2059478588}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_70922_x4169_x382288412}[模式：]{style="font-family:宋体"}

[**[debugging]{lang="EN-US"}**[ **system-event** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_70922_x4169_785948527}

[**[undo]{lang="EN-US"}**[ **debugging** **system-event** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_70922_x4169_1362939405}

[[【视图】]{style="font-family:黑体"}]{#struct_0_70922_x4169_119808616}

[[用户视图]{style="font-family:宋体"}]{#struct_0_70922_x4169_x604552727}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_70922_x4169_1126893582}

[[network-admin]{lang="EN-US"}]{#struct_0_70922_x4169_x1852665679}

[[network-operator]{lang="EN-US"}]{#struct_0_70922_x4169_x2008930505}

[[mdc-admin]{lang="EN-US"}]{#struct_0_70922_x4169_x1233952762}

[[mdc-operator]{lang="EN-US"}]{#struct_0_70922_x4169_x372857612}

[[【参数】]{style="font-family:黑体"}]{#struct_0_70922_x4169_1363136013}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_x1510338736}[：表示单板所在的槽位号。不指定该参数时，表示设置所有单板的调试开关。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_1363070477}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示设置所有单板的调试开关。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_2134105403}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。不指定该参数时，表示设置所有单板的调试开关。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_1363267085}[：]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，则表示设置所有单板的调试开关。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_70922_x4169_807059762}[：]{style="font-family:宋体"}*[chassis-numbe]{lang="EN-US"}*[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。不指定该参数时，则表示所有单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的调试开关。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_70922_x4169_1126637311}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}[slot]{lang="EN-US"}[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_70922_x4169_1233814595}

[**[debugging system-event]{lang="EN-US"}**]{#struct_0_70922_x4169_1778925998}[命令用来打开系统事件模块调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging system-event**]{lang="EN-US"}[命令用来关闭系统事件模块调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，系统事件模块调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_70922_x4169_1363201549}

[[【举例】]{style="font-family:黑体"}]{#struct_0_70922_x4169_461293741}

[[\# ]{lang="EN-US"}]{#struct_0_70922_x4169_x1366140555}[打开系统事件模块调试信息的开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging system-event]{lang="EN-US"}]{#struct_0_70922_x4169_x2053389359}
:::
