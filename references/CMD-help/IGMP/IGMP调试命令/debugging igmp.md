::: {#1623549643 .myid}
[]{#_Toc404789479}[]{#struct_0_18222_x1284_1606155286}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**IGMP \-- IGMP调试命令 \-- debugging igmp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_18222_x1284_x1101458156}

[**[debugging]{lang="EN-US"}**[ **igmp** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **event** \| **leave** \| **query** \[ **receive** \| **send** \] \| **report** \| **timer** }]{lang="EN-US"}]{#struct_0_18222_x1284_x1912823553}

[**[undo]{lang="EN-US"}**[ **debugging** **igmp** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **event** \| **leave** **\|** **query** \[ **receive** \| **send** \] \| **report** **\|** **timer** }]{lang="EN-US"}]{#struct_0_18222_x1284_x2099547382}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18222_x1284_x219568103}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18222_x1284_814249814}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18222_x1284_1620181455}

[[network-admin]{lang="EN-US"}]{#struct_0_18222_x1284_684304478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18222_x1284_444683245}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18222_x1284_x995670990}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_18222_x1284_x1101392620}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_18222_x1284_1827407170}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_18222_x1284_482459326}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[leave]{lang="EN-US"}**]{#struct_0_18222_x1284_x559776553}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[离开组报文调试信息开关。]{style="font-family:宋体"}

[**[query]{lang="EN-US"}**]{#struct_0_18222_x1284_x406309108}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_18222_x1284_1101728372}[：表示接收的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_18222_x1284_x1566848920}[：表示发送的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询报文调试信息开关。]{style="font-family:宋体"}

[**[report]{lang="EN-US"}**]{#struct_0_18222_x1284_x960816750}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_18222_x1284_x719659675}[：表示]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_18222_x1284_x462290146}

[**[debugging]{lang="EN-US"}**[ **igmp**]{lang="EN-US"}]{#struct_0_18222_x1284_x1101327084}[命令用来打开]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **igmp**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_x1676295095}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging igmp event]{lang="EN-US"}]{#struct_0_18222_x1284_467199854}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1287819939}[[字段]{style="font-family:黑体"}]{#struct_0_18222_x1284_1084455390}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18222_x1284_954514940}

[[Create/Add/Remove/Delete IGMP configuration interface *interfacename*]{lang="EN-US"}]{#struct_0_18222_x1284_x725451983}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18222_x1284_x1298434566}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[移动]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[配置接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*

[[Create/Delete IGMP interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_18222_x1284_x1101261548}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18222_x1284_x1068297786}[删除]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[接口]{style="font-family:宋体"}[interfacename]{lang="EN-US"}[，其地址为]{style="font-family:宋体"}[address]{lang="EN-US"}

[[interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_18222_x1284_245876384}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_x1051346268}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[Send/Notify/Receive/Ignore]{lang="EN-US"}]{#struct_0_18222_x1284_1217826237}

[[发送]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18222_x1284_x1306989228}[通知]{style="font-family:宋体"}[/]{lang="EN-US"}[接收]{style="font-family:宋体"}[/]{lang="EN-US"}[忽略]{style="font-family:宋体"}

[*[message-type]{lang="EN-US"}*[ message]{lang="EN-US"}]{#struct_0_18222_x1284_x906275596}

[*[message-type]{lang="EN-US"}*]{#struct_0_18222_x1284_x1101196012}[类型的消息，]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[join-prune]{lang="EN-US"}]{#struct_0_18222_x1284_x773460354}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[加入]{lang="EN-US" style="font-family:
  宋体"}[/]{lang="EN-US"}[剪枝消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[querier]{lang="EN-US"}]{#struct_0_18222_x1284_1879769731}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[查询器消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth]{lang="EN-US"}]{#struct_0_18222_x1284_1070340918}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[平滑消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth over]{lang="EN-US"}]{#struct_0_18222_x1284_712717611}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[平滑结束消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HA]{lang="EN-US"}]{#struct_0_18222_x1284_1333670150}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[高可靠性相关的消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IGMP enable]{lang="EN-US"}]{#struct_0_18222_x1284_x1101130476}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[协议使能消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MRIB connection up]{lang="EN-US"}]{#struct_0_18222_x1284_x164782420}[：]{lang="EN-US" style="font-family:
  宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[与]{lang="EN-US" style="font-family:宋体"}[MRIB]{lang="EN-US"}[建立连接成功消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MRIB connection down]{lang="EN-US"}]{#struct_0_18222_x1284_843516575}[：]{lang="EN-US" style="font-family:
  宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[与]{lang="EN-US" style="font-family:宋体"}[MRIB]{lang="EN-US"}[连接中断消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MRIB smooth]{lang="EN-US"}]{#struct_0_18222_x1284_x439687233}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[与]{lang="EN-US" style="font-family:
  宋体"}[MRIB]{lang="EN-US"}[进行平滑消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicast boundary message]{lang="EN-US"}]{#struct_0_18222_x1284_x1157004031}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[组播边界消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicast routing-enable]{lang="EN-US"}]{#struct_0_18222_x1284_x1102113516}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[三层组播使能消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicast routing-disable]{lang="EN-US"}]{#struct_0_18222_x1284_1655757846}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[三层组播关闭消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIM DR]{lang="EN-US"}]{#struct_0_18222_x1284_1935275118}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[指定路由器消息]{lang="EN-US" style="font-family:宋体"}

[[MRIB]{lang="EN-US"}]{#struct_0_18222_x1284_x1017459115}

[[组播路由信息库]{style="font-family:宋体"}]{#struct_0_18222_x1284_x473549723}

[[set binary data]{lang="EN-US"}]{#struct_0_18222_x1284_x1102047980}

[[设置二进制数据]{style="font-family:宋体"}]{#struct_0_18222_x1284_x195639697}

[[static-group]{lang="EN-US"}]{#struct_0_18222_x1284_x1812525829}

[[添加静态组]{style="font-family:宋体"}]{#struct_0_18222_x1284_237957928}

[[open DBM]{lang="EN-US"}]{#struct_0_18222_x1284_x959312082}

[[打开]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_18222_x1284_739828954}

[[batch backup data on interface(*interfacename*) configuration ]{lang="EN-US"}]{#struct_0_18222_x1284_x1464916618}

[[关于接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_x1134839165}[配置的批量备份数据]{style="font-family:宋体"}

[[batch backup data on global configuration]{lang="EN-US"}]{#struct_0_18222_x1284_x187755571}

[[关于全局配置的批量备份数据]{style="font-family:宋体"}]{#struct_0_18222_x1284_739763418}

[[Add/Delete address  *address* for interface *interfacename*]{lang="EN-US"}]{#struct_0_18222_x1284_229904485}

[[为接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_608640669}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[(*saddr, gaddr*)]{lang="EN-US"}]{#struct_0_18222_x1284_823804584}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_18222_x1284_x1802049631}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项，]{style="font-family:宋体"}*[saddr]{lang="EN-US"}*[为源地址，]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*[为组地址]{style="font-family:宋体"}

[[group(*gaddr*)]{lang="EN-US"}]{#struct_0_18222_x1284_739697882}

[[组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_1876990778}

[[Change mode from *mode1* to *mode2*]{lang="FR"}]{#struct_0_18222_x1284_424162275}

[[组播组的模式由]{style="font-family:宋体"}]{#struct_0_18222_x1284_x56474016}*[mode1]{lang="FR"}*[变更为]{style="font-family:宋体"}*[mode2]{lang="FR"}*[，具体模式包括]{style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[和]{style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}

[[Create group (*gaddr*)]{lang="EN-US"}]{#struct_0_18222_x1284_739632346}

[[创建组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_629072119}

[[Becomes querier/non-querier]{lang="EN-US"}]{#struct_0_18222_x1284_x1514027651}

[[成为查询器]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18222_x1284_740091098}[非查询器]{style="font-family:宋体"}

[[Stop event thread]{lang="EN-US"}]{#struct_0_18222_x1284_x22607035}

[[终止事件处理线程]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1746468753}

[[real time backup data]{lang="EN-US"}]{#struct_0_18222_x1284_x225490694}

[[实时备份数据]{style="font-family:宋体"}]{#struct_0_18222_x1284_740025562}

[[batch backup data]{lang="EN-US"}]{#struct_0_18222_x1284_x1210756821}

[[批量备份数据]{style="font-family:宋体"}]{#struct_0_18222_x1284_958869447}

[[HA batch backup event]{lang="EN-US"}]{#struct_0_18222_x1284_158295870}

[[高可靠性的批量备份事件]{style="font-family:宋体"}]{#struct_0_18222_x1284_739960026}

[[HA degrade/stop/upgrade event]{lang="EN-US"}]{#struct_0_18222_x1284_1229864447}

[[高可靠性的降级]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18222_x1284_x1880137616}[停止]{style="font-family:宋体"}[/]{lang="EN-US"}[升级事件]{style="font-family:宋体"}

[*[event]{lang="EN-US"}*[ event on interface *interfacename*]{lang="EN-US"}]{#struct_0_18222_x1284_739894490}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_1970803324}[上发生事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_18222_x1284_587704476}[：表示添加接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_18222_x1284_740353242}[：表示删除接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x3]{lang="EN-US"}]{#struct_0_18222_x1284_x182574963}[：表示接口]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x4]{lang="EN-US"}]{#struct_0_18222_x1284_895817529}[：表示接口]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x6]{lang="EN-US"}]{#struct_0_18222_x1284_740287706}[：表示接口配置变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x9]{lang="EN-US"}]{#struct_0_18222_x1284_x963090113}[：表示接口解除绑定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0xa]{lang="EN-US"}]{#struct_0_18222_x1284_1920737375}[：表示拔出接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0xb]{lang="EN-US"}]{#struct_0_18222_x1284_739828955}[：表示插入接口]{lang="EN-US" style="font-family:宋体"}

[[address event *event* on interface *interfacename* (*address*), state is *state*]{lang="EN-US"}]{#struct_0_18222_x1284_x1464916619}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_431244776}[（地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[）上发生地址事件。事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[event]{lang="EN-US"}*]{#struct_0_18222_x1284_739763419}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_18222_x1284_229904484}[：表示添加地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_18222_x1284_608640668}[：表示删除地址]{lang="EN-US" style="font-family:宋体"}

[*[state]{lang="EN-US"}*]{#struct_0_18222_x1284_739697883}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x200]{lang="EN-US"}]{#struct_0_18222_x1284_1876990779}[：表示主地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x400]{lang="EN-US"}]{#struct_0_18222_x1284_424227811}[：表示借用地址]{lang="EN-US" style="font-family:宋体"}

[[ifnet connection down event]{lang="EN-US"}]{#struct_0_18222_x1284_739632347}

[[与接口管理的连接中断事件]{style="font-family:宋体"}]{#struct_0_18222_x1284_629072120}

[[Process interface *interfacename* *event*]{lang="EN-US"}]{#struct_0_18222_x1284_59950470}

[[处理接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_740091099}[上发生的事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_18222_x1284_x22607034}[：表示添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_18222_x1284_740025563}[：表示删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[plugout]{lang="EN-US"}]{#struct_0_18222_x1284_x1210756822}[：表示拔出]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_18222_x1284_x607214494}[：表示连接成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_18222_x1284_739960027}[：表示连接中断]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[attribute changed]{lang="EN-US"}]{#struct_0_18222_x1284_1229864446}[：表示属性变化]{lang="EN-US" style="font-family:
  宋体"}

[[IGMP proxy]{lang="EN-US"}]{#struct_0_18222_x1284_431125146}

[[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_431321754}[代理]{style="font-family:宋体"}

[[proxy database]{lang="EN-US"}]{#struct_0_18222_x1284_x1687591677}

[[代理成员关系数据库]{style="font-family:宋体"}]{#struct_0_18222_x1284_1695892766}

[[proxy cache]{lang="EN-US"}]{#struct_0_18222_x1284_431256218}

[[代理缓存]{style="font-family:宋体"}]{#struct_0_18222_x1284_1850803975}

[[Create/Delete IGMP proxy interface *interfacename*]{lang="EN-US"}]{#struct_0_18222_x1284_1902102077}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18222_x1284_431452826}[删除]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*

[[Send IGMP proxy enable/disable on interface *interfacename* to MRIB]{lang="EN-US"}]{#struct_0_18222_x1284_907973923}

[[通过接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_x611108546}[向]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[通知使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[代理功能]{style="font-family:宋体"}

[[Add/Remove source(*saddr*) to proxy cache on interface *interfacename* for group(*gaddr*)]{lang="EN-US"}]{#struct_0_18222_x1284_431387290}

[[在接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_720962948}[上为组节点]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除源节点]{style="font-family:宋体"}*[saddr]{lang="EN-US"}*[到代理缓存]{style="font-family:宋体"}

[[Add/Remove/Update group(*gaddr*) to proxy cache on interface *interfacename*]{lang="EN-US"}]{#struct_0_18222_x1284_430928539}

[[在接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_70211113}[上添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新组节点]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*[到代理缓存]{style="font-family:宋体"}

[[Add/Remove source(*saddr*) to proxy database for group(*gaddr*)]{lang="EN-US"}]{#struct_0_18222_x1284_326408185}

[[在代理成员关系数据库的组节点]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_430863003}[下添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除源]{style="font-family:宋体"}*[saddr]{lang="EN-US"}*

[[Add INCLUDE/EXCLUDE group(*gaddr*) to proxy database]{lang="EN-US"}]{#struct_0_18222_x1284_493817776}

[[在代理成员关系数据库中添加]{style="font-family:宋体"}[INCLUDE/EXCLUDE]{lang="EN-US"}]{#struct_0_18222_x1284_x540106268}[模式的组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging igmp leave]{lang="EN-US"}]{#struct_0_18222_x1284_x1880072080}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1266256767}[[字段]{style="font-family:黑体"}]{#struct_0_18222_x1284_1149991464}

[[描述]{style="font-family:黑体"}]{#struct_0_18222_x1284_x1488603316}

[[Ignore IGMP packet from *src* to *dest*]{lang="EN-US"}]{#struct_0_18222_x1284_739894491}

[[忽略源地址为]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_18222_x1284_1970803325}[、]{style="font-family:宋体"}[目的地址为]{style="font-family:宋体"}*[dest]{lang="EN-US"}*[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[TTL is 0]{lang="EN-US"}]{#struct_0_18222_x1284_587770012}

[[TTL]{lang="EN-US"}]{#struct_0_18222_x1284_x341171028}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[length *length* is too short]{lang="EN-US"}]{#struct_0_18222_x1284_2047706468}

[[报文长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_18222_x1284_518618010}[太短]{style="font-family:宋体"}

[[unsupported type *number*]{lang="EN-US"}]{#struct_0_18222_x1284_625567311}

[[不支持的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_740353243}[报文类型，类型码为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[checksum *value* is wrong]{lang="EN-US"}]{#struct_0_18222_x1284_x182574962}

[[校验和]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_18222_x1284_895883065}[错误]{style="font-family:宋体"}

[[Router-Alert option]{lang="EN-US"}]{#struct_0_18222_x1284_739262375}

[[IP]{lang="EN-US"}]{#struct_0_18222_x1284_1285152811}[选项]{style="font-family:宋体"}[Router-Alert]{lang="EN-US"}

[[interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_18222_x1284_482840094}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_740287707}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[leave]{lang="EN-US"}]{#struct_0_18222_x1284_x963090114}

[[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_1920933983}[离开组报文]{style="font-family:宋体"}

[[group address *gaddr* is is not in multicast range]{lang="EN-US"}]{#struct_0_18222_x1284_x129920878}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_x1613954632}[不是组播地址]{style="font-family:宋体"}

[[group address *gaddr* is reserved]{lang="EN-US"}]{#struct_0_18222_x1284_x65048873}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_739828952}[为保留地址]{style="font-family:宋体"}

[[group(]{lang="EN-US"}*[gaddr)]{lang="EN-US"}*]{#struct_0_18222_x1284_x1464916620}

[[组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_x778412197}

[[this group does not exist]{lang="EN-US"}]{#struct_0_18222_x1284_x124851267}

[[组播组不存在]{style="font-family:宋体"}]{#struct_0_18222_x1284_1829336693}

[[this group has v1 host]{lang="EN-US"}]{#struct_0_18222_x1284_739763416}

[[存在]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}]{#struct_0_18222_x1284_229904491}[的主机]{style="font-family:宋体"}

[[fast-leave is off and interface is non-querier]{lang="EN-US"}]{#struct_0_18222_x1284_x1730011495}

[[组播组成员快速离开功能处于关闭状态，接口也不是查询器]{style="font-family:宋体"}]{#struct_0_18222_x1284_590106366}

[[this group is leaving]{lang="EN-US"}]{#struct_0_18222_x1284_1706794569}

[[组播组正在离开]{style="font-family:宋体"}]{#struct_0_18222_x1284_739697880}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging igmp query]{lang="EN-US"}]{#struct_0_18222_x1284_1876990776}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1268823143}[[字段]{style="font-family:黑体"}]{#struct_0_18222_x1284_424555491}

[[描述]{style="font-family:黑体"}]{#struct_0_18222_x1284_x1841537911}

[[Ignore IGMP packet from *src* to *dest*]{lang="EN-US"}]{#struct_0_18222_x1284_x1914150255}

[[忽略源地址为]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_18222_x1284_1654514042}[、]{style="font-family:宋体"}[目的地址为]{style="font-family:宋体"}*[dest]{lang="EN-US"}*[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[source address is invalid]{lang="EN-US"}]{#struct_0_18222_x1284_x2026548739}

[[源地址非法]{style="font-family:宋体"}]{#struct_0_18222_x1284_739632344}

[[packet length *pktlength* isn\'t equal to the sum of IP header length *headerlength* and IGMP length *igmplength*]{lang="EN-US"}]{#struct_0_18222_x1284_629072121}

[[报文长度]{style="font-family:宋体"}*[pktlength]{lang="EN-US"}*]{#struct_0_18222_x1284_59950469}[不等于报文头长度]{style="font-family:宋体"}*[headerlength]{lang="EN-US"}*[与]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[长度]{style="font-family:宋体"}*[igmplength]{lang="EN-US"}*[之和]{style="font-family:宋体"}

[[TTL is 0]{lang="EN-US"}]{#struct_0_18222_x1284_1533227426}

[[TTL]{lang="EN-US"}]{#struct_0_18222_x1284_x2089568375}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[length *length* is too short]{lang="EN-US"}]{#struct_0_18222_x1284_859334630}

[[报文长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_18222_x1284_x1978377268}[太短]{style="font-family:宋体"}

[[unsupported type *number*]{lang="EN-US"}]{#struct_0_18222_x1284_740091096}

[[不支持的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_x22607029}[报文类型，类型码为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[checksum *value* is wrong]{lang="EN-US"}]{#struct_0_18222_x1284_209846379}

[[校验和]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_18222_x1284_1997991640}[错误]{style="font-family:宋体"}

[[Router-Alert option]{lang="EN-US"}]{#struct_0_18222_x1284_1329193711}

[[IP]{lang="EN-US"}]{#struct_0_18222_x1284_740025560}[选项]{style="font-family:宋体"}[Router-Alert]{lang="EN-US"}

[[interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_18222_x1284_x1210756823}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_2121668861}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[query]{lang="EN-US"}]{#struct_0_18222_x1284_x1430926213}

[[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_x1091220138}[查询报文]{style="font-family:宋体"}

[[length is invalid]{lang="EN-US"}]{#struct_0_18222_x1284_x633195789}

[[报文长度非法]{style="font-family:宋体"}]{#struct_0_18222_x1284_739960024}

[[group address *gaddr* is not in multicast range]{lang="EN-US"}]{#struct_0_18222_x1284_1229864445}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_x1880006544}[不在组播组范围内]{style="font-family:宋体"}

[[group address *gaddr* is reserved]{lang="EN-US"}]{#struct_0_18222_x1284_x235976218}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_739894488}[为保留地址]{style="font-family:宋体"}

[[general query]{lang="EN-US"}]{#struct_0_18222_x1284_x367848844}

[[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_1023900908}[普遍组查询]{style="font-family:宋体"}

[[group specific query]{lang="EN-US"}]{#struct_0_18222_x1284_650457785}

[[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_1864852333}[特定组查询]{style="font-family:宋体"}

[[group-source specific query]{lang="EN-US"}]{#struct_0_18222_x1284_740353240}

[[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_x182574965}[特定源组查询]{style="font-family:宋体"}

[[group *gaddr*]{lang="EN-US"}]{#struct_0_18222_x1284_895686457}

[[查询的组地址为]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_2059431225}

[[source count *num*]{lang="EN-US"}]{#struct_0_18222_x1284_740287704}

[[组播源的数目为]{style="font-family:宋体"}*[num]{lang="EN-US"}*]{#struct_0_18222_x1284_x963090111}

[[S flag]{lang="EN-US"}]{#struct_0_18222_x1284_1920606303}

[[查询报文的]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_18222_x1284_251349608}[标记]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging igmp report]{lang="EN-US"}]{#struct_0_18222_x1284_739828953}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1274457638}[[字段]{style="font-family:黑体"}]{#struct_0_18222_x1284_x1464916621}

[[描述]{style="font-family:黑体"}]{#struct_0_18222_x1284_787671744}

[[Ignore IGMP packet from *src* to *dest*]{lang="EN-US"}]{#struct_0_18222_x1284_x1555144257}

[[忽略源地址为]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_18222_x1284_x327948053}[、]{style="font-family:宋体"}[目的地址为]{style="font-family:宋体"}*[dest]{lang="EN-US"}*[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[source address is invalid]{lang="EN-US"}]{#struct_0_18222_x1284_772122258}

[[源地址非法]{style="font-family:宋体"}]{#struct_0_18222_x1284_1665205077}

[[packet length *pktlength* isn\'t equal to the sum of IP header length *headerlength* and IGMP length *igmplength*]{lang="EN-US"}]{#struct_0_18222_x1284_739763417}

[[报文长度]{style="font-family:宋体"}*[pktlength]{lang="EN-US"}*]{#struct_0_18222_x1284_229904490}[不等于报文头长度]{style="font-family:宋体"}*[headerlength]{lang="EN-US"}*[与]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[长度]{style="font-family:宋体"}*[igmplength]{lang="EN-US"}*[之和]{style="font-family:宋体"}

[[TTL is 0]{lang="EN-US"}]{#struct_0_18222_x1284_x1730011496}

[[TTL]{lang="EN-US"}]{#struct_0_18222_x1284_x2138776989}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[length *length* is too short]{lang="EN-US"}]{#struct_0_18222_x1284_177735345}

[[报文长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_18222_x1284_x1483822649}[太短]{style="font-family:宋体"}

[[unsupported type *number*]{lang="EN-US"}]{#struct_0_18222_x1284_739697881}

[[不支持的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_1876990777}[报文类型，类型码为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[checksum *value* is wrong]{lang="EN-US"}]{#struct_0_18222_x1284_424621027}

[[校验和]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_18222_x1284_x68145380}[错误]{style="font-family:宋体"}

[[Router-Alert option]{lang="EN-US"}]{#struct_0_18222_x1284_x1886007218}

[[IP]{lang="EN-US"}]{#struct_0_18222_x1284_739632345}[选项]{style="font-family:宋体"}[Router-Alert]{lang="EN-US"}

[[interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_18222_x1284_629072122}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_18222_x1284_59950472}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[group address *gaddr* is invalid]{lang="EN-US"}]{#struct_0_18222_x1284_x1240285945}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_1126606125}[非法]{style="font-family:宋体"}

[[group address *gaddr* is reserved]{lang="EN-US"}]{#struct_0_18222_x1284_740091097}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_x22607028}[为保留地址]{style="font-family:宋体"}

[[group(]{lang="EN-US"}*[gaddr)]{lang="EN-US"}*]{#struct_0_18222_x1284_209846380}

[[组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_18222_x1284_x1959268641}

[[report]{lang="EN-US"}]{#struct_0_18222_x1284_x1966169397}

[[IGMP]{lang="EN-US"}]{#struct_0_18222_x1284_740025561}[成员关系报告报文]{style="font-family:宋体"}

[[group record]{lang="EN-US"}]{#struct_0_18222_x1284_x1210756824}

[[组播组记录]{style="font-family:宋体"}]{#struct_0_18222_x1284_199354560}

[[IS_IN/IS_EX/TO_IN/TO_EX/ALLOW/BLOCK]{lang="EN-US"}]{#struct_0_18222_x1284_328775131}

[[IGMPv3]{lang="EN-US"}]{#struct_0_18222_x1284_739960025}[报告报文中的组记录类型]{style="font-family:宋体"}

[[number of sources is zero]{lang="EN-US"}]{#struct_0_18222_x1284_1229864444}

[[组播源的数目为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_18222_x1284_x1879941008}

[[this group does not exist]{lang="EN-US"}]{#struct_0_18222_x1284_37405599}

[[组播组不存在]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1932767921}

[[old version host exists]{lang="EN-US"}]{#struct_0_18222_x1284_739894489}

[[存在低版本的主机]{style="font-family:宋体"}]{#struct_0_18222_x1284_x367848843}

[[fast-leave is off and interface is non-querier]{lang="EN-US"}]{#struct_0_18222_x1284_1024359660}

[[组播组成员快速离开功能处于关闭状态，接口也不是查询器]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1130410636}

[[v1 host exists]{lang="EN-US"}]{#struct_0_18222_x1284_740353241}

[[存在]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}]{#struct_0_18222_x1284_x182574964}[的主机]{style="font-family:宋体"}

[[can\'t pass multicast boundary]{lang="EN-US"}]{#struct_0_18222_x1284_895751993}

[[不能通过组播边界]{style="font-family:宋体"}]{#struct_0_18222_x1284_740287705}

[[can\'t pass group policy]{lang="EN-US"}]{#struct_0_18222_x1284_x963090112}

[[不能通过组播组策略]{style="font-family:宋体"}]{#struct_0_18222_x1284_1920802911}

[[group address is in SSM range]{lang="EN-US"}]{#struct_0_18222_x1284_1430068237}

[[组播组地址属于]{style="font-family:宋体"}[SSM]{lang="EN-US"}]{#struct_0_18222_x1284_739828950}[组范围]{style="font-family:宋体"}

[[destination address *addr* is invalid]{lang="EN-US"}]{#struct_0_18222_x1284_x1464916622}

[[目的地址]{style="font-family:宋体"}*[addr]{lang="EN-US"}*]{#struct_0_18222_x1284_x1941211611}[非法]{style="font-family:宋体"}

[[Proxy send]{lang="EN-US"}]{#struct_0_18222_x1284_431387291}

[[代理发送]{style="font-family:宋体"}]{#struct_0_18222_x1284_720962949}

[[Failed to send packet]{lang="EN-US"}]{#struct_0_18222_x1284_1997012475}

[[发送报文失败]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1034457220}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging igmp timer]{lang="EN-US"}]{#struct_0_18222_x1284_1586332151}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1243024766}[[字段]{style="font-family:黑体"}]{#struct_0_18222_x1284_x804352415}

[[描述]{style="font-family:黑体"}]{#struct_0_18222_x1284_739763414}

[[Static group activation timer]{lang="EN-US"}]{#struct_0_18222_x1284_229904489}

[[静态组激活定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_608640657}

[[Group reset timer]{lang="EN-US"}]{#struct_0_18222_x1284_x1514847578}

[[表项清除定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_x345618039}

[[Multicast boundary timer]{lang="EN-US"}]{#struct_0_18222_x1284_207271525}

[[组播边界定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_157386299}

[[Multicast ]{lang="EN-US"}[routing enable timer]{lang="EN-US"}]{#struct_0_18222_x1284_739697878}

[[组播使能定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1697932496}

[[v1/v2 host timer]{lang="EN-US"}]{#struct_0_18222_x1284_x514699805}

[[v1/v2]{lang="EN-US"}]{#struct_0_18222_x1284_1169883931}[主机存在定时器]{style="font-family:宋体"}

[[Source aging timer]{lang="EN-US"}]{#struct_0_18222_x1284_x646598506}

[[源老化定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1588021754}

[[Group aging timer]{lang="EN-US"}]{#struct_0_18222_x1284_739632342}

[[组老化定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_629072115}

[[Group retransmit timer]{lang="EN-US"}]{#struct_0_18222_x1284_x1514027647}

[[组重传定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_955507943}

[[Source retransmit timer]{lang="EN-US"}]{#struct_0_18222_x1284_x582126888}

[[源重传定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_740091094}

[[General query timer]{lang="EN-US"}]{#struct_0_18222_x1284_x22607031}

[[普遍组查询定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1746468749}

[[Delay timer]{lang="EN-US"}]{#struct_0_18222_x1284_1482674772}

[[延迟发送报告报文定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_1482740308}

[[Other querier present timer]{lang="EN-US"}]{#struct_0_18222_x1284_1293473544}

[[其它查询器存在时间定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1249969580}

[[Create/Delete/Set/expired]{lang="EN-US"}]{#struct_0_18222_x1284_740025558}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18222_x1284_1510232369}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[设置]{style="font-family:宋体"}[/]{lang="EN-US"}[超时]{style="font-family:宋体"}

[[Smooth timer]{lang="EN-US"}]{#struct_0_18222_x1284_1055202354}

[[平滑定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_x1605420000}

[[Smooth over timer]{lang="EN-US"}]{#struct_0_18222_x1284_1442634380}

[[平滑结束定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_739960022}

[[Proxy database adjust timer]{lang="EN-US"}]{#struct_0_18222_x1284_1997143547}

[[代理成员关系数据库调整定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_1997078011}

[[old querier present timer]{lang="EN-US"}]{#struct_0_18222_x1284_534295508}

[[旧版本查询器的存在时间定时器]{style="font-family:宋体"}]{#struct_0_18222_x1284_x788212750}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18222_x1284_1229864451}

[[\# ]{lang="EN-US"}]{#struct_0_18222_x1284_x1879744401}[在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp event]{lang="NO-BOK"}]{#struct_0_18222_x1284_x1470262434}

[\*Jun 22 17:22:17:762 2011 Sysname IGMP/7/EVENT: -MDC=1;]{lang="NO-BOK"}[ Send  become-querier on interface GigabitEthernet1/0/1to MRIB (G10196)]{lang="EN-US"}

[\*Jun 22 17:22:17:763 2011 Sysname IGMP/7/EVENT: -MDC=1; Becomes querier on interface GigabitEthernet1/0/1(10.1.1.1) (G10462)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_530853220}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[被选举为]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[查询器，并将该事件通知]{style="font-family:宋体"}[MRIB]{lang="EN-US"}*

[[Jun 22 17:06:39:157 2011 Sysname IGMP/7/EVENT: -MDC=1;]{lang="NO-BOK"}[ Create group(229.1.1.1) on interface GigabitEthernet1/0/1(10.1.1.1) (G102773)]{lang="EN-US"}]{#struct_0_18222_x1284_739894486}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_x367848838}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[添加组播组]{style="font-family:宋体"}[229.1.1.1]{lang="EN-US"}*

[[\*Jun 22 17:06:39:158 2011 Sysname IGMP/7/EVENT: -MDC=1;]{lang="NO-BOK"}[ Change mode from INCLUDE to EXCLUDE for group(229.1.1.1) on interface GigabitEthernet1/0/1(10.1.1.1) (G101886)]{lang="EN-US"}]{#struct_0_18222_x1284_1023638769}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_x1382885264}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上组播组]{style="font-family:宋体"}[229.1.1.1]{lang="EN-US"}[的模式由]{style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[变为]{style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}*

[[\*Jun 22 17:06:39:159 2011 Sysname IGMP/7/EVENT: -MDC=1;]{lang="NO-BOK"}[ Send JOIN for (0.0.0.0,229.1.1.1) on interface GigabitEthernet1/0/1(10.1.1.1) to MRIB(G10105)]{lang="EN-US"}]{#struct_0_18222_x1284_x463830620}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_x250142262}*[通知]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上有（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[229.1.1.1]{lang="EN-US"}[）加入]{style="font-family:宋体"}*

[[\*Jun 22 17:24:36:256 2011 Sysname IGMP/7/EVENT: -MDC=1;]{lang="NO-BOK"}[ Change mode from EXCLUDE to INCLUDE for group(229.1.1.1) on interface GigabitEthernet1/0/1(10.1.1.1) (G101793)]{lang="EN-US"}]{#struct_0_18222_x1284_x1502541622}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_1794554576}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上组播组]{style="font-family:宋体"}[229.1.1.1]{lang="EN-US"}[的模式由]{style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}[变为]{style="font-family:宋体"}[INCLUDE]{lang="EN-US"}*

[[\*Jun 22 17:24:36:257 2011 Sysname IGMP/7/EVENT: -MDC=1;]{lang="NO-BOK"}[ Send  PRUNE for (0.0.0.0,229.1.1.1) on interface GigabitEthernet1/0/1(10.1.1.1) to MRIB(G10105)]{lang="EN-US"}]{#struct_0_18222_x1284_35990130}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_1188948701}*[通知]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上有（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[229.1.1.1]{lang="EN-US"}[）离开]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_18222_x1284_740353238}[在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[离开组报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp leave]{lang="EN-US"}]{#struct_0_18222_x1284_626729107}

[\*Jun 22 17:40:32:203 2011 Sysname IGMP/7/LEAVE: -MDC=1; Received LEAVE for group 229.1.1.1 on interface GigabitEthernet1/0/1(10.1.1.1) (G16954)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_x1532187997}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到离开组]{style="font-family:宋体"}[229.1.1.1]{lang="EN-US"}[的报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_18222_x1284_1197087672}[在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[成员关系报告报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp report]{lang="EN-US"}]{#struct_0_18222_x1284_1959775565}

[\*Jun 22 17:42:02:017 2011 Sysname IGMP/7/REPORT: -MDC=1; Received IGMPv2 report for group 229.1.1.1 on interface GigabitEthernet1/0/1(10.1.1.1) (G16954)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_x1198400081}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到加入组]{style="font-family:宋体"}[229.1.1.1]{lang="EN-US"}[的成员关系报告报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_18222_x1284_1525554253}[在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[接收查询报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp query receive]{lang="EN-US"}]{#struct_0_18222_x1284_740287702}

[\*Jun 22 18:31:11:221 2011 Sysname IGMP/7/QUERY SEND: -MDC=1; Received IGMP version 2 query on GigabitEthernet1/0/1(10.1.1.1) from 10.1.1.2(G10308)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_x963090117}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到]{style="font-family:宋体"}[IGMPv2]{lang="EN-US"}[普遍组查询报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_18222_x1284_1920999519}[在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[发送查询报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp query send]{lang="EN-US"}]{#struct_0_18222_x1284_x159232979}

[\*Jun 22 18:39:33:257 2011 Sysname IGMP/7/QUERY SEND: -MDC=1; Send IGMP version 2 general query on GigabitEthernet1/0/1(10.1.1.1) to 224.0.0.1 (G10308)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_194775210}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[IGMPv2]{lang="EN-US"}[普遍组查询报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_18222_x1284_1548769855}[在接口上使能]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp timer]{lang="NO-BOK"}]{#struct_0_18222_x1284_128343266}

[\*Jun 22 18:53:49:129 2011 Sysname IGMP/7/TIMER: -MDC=1;]{lang="NO-BOK"}[ Setting v2 host timer for group(229.1.1.1) on interface GigabitEthernet1/0/1(10.1.1.1) to 260s (G102089)]{lang="EN-US"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_18222_x1284_2140704182}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="NO-BOK"}[设置组]{style="font-family:宋体"}[229.1.1.1]{lang="NO-BOK"}[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[v2]{lang="NO-BOK"}[主机存在定时器]{style="font-family:宋体"}*

[[\*Jun 22 18:55:58:012 2011 Sysname IGMP/7/TIMER: -MDC=1;]{lang="NO-BOK"}[ Setting group aging timer for group(229.1.1.1) on interface GigabitEthernet1/0/1(10.1.1.1) to 260s (G102379)]{lang="EN-US"}]{#struct_0_18222_x1284_739828951}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_x1464916623}*[设置组]{style="font-family:宋体"}[229.1.1.1]{lang="EN-US"}[的老化定时器超时]{style="font-family:宋体"}*

[[\*Jun 22 18:56:33:261 2011 Sysname IGMP/7/TIMER: -MDC=1;]{lang="NO-BOK"}[ Setting general query timer on interface GigabitEthernet1/0/1(10.1.1.1) to 125s (G10338)]{lang="EN-US"}]{#struct_0_18222_x1284_x375127670}

[*[// ]{lang="EN-US"}*]{#struct_0_18222_x1284_x1514190594}*[设置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的普遍组查询定时器]{style="font-family:宋体"}*
