::: {#-1504013224 .myid}
[]{#_Toc404790171}[]{#struct_0_20662_54297_x288107522}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**MLD \-- MLD调试命令 \-- debugging mld**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20662_54297_143303222}

[**[debugging]{lang="EN-US"}**[ **mld** \[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}[{ **all** \| **done** \| **event** \| **query** \[ **receive** \| **send** \] \| **report** \| \| **timer** }]{lang="EN-US"}]{#struct_0_20662_54297_2017656403}

[**[undo]{lang="EN-US"}**[ **debugging** **mld** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **done** \| **event** \| **query** \[ **receive** \| **send** \] \| **report** \| **timer** }]{lang="EN-US"}]{#struct_0_20662_54297_x820160138}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20662_54297_1994916052}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20662_54297_1003962561}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20662_54297_2051488143}

[[network-admin]{lang="EN-US"}]{#struct_0_20662_54297_x1022050840}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20662_54297_2010115216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20662_54297_x29272557}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_20662_54297_314672152}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_20662_54297_1021882384}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[done]{lang="EN-US"}**]{#struct_0_20662_54297_x854320106}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[离开组报文调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_20662_54297_x820094602}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[query]{lang="EN-US"}**]{#struct_0_20662_54297_513814024}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_20662_54297_1273693172}[：表示接收的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_20662_54297_1191356761}[：表示发送的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询报文调试信息开关。]{style="font-family:宋体"}

[**[report]{lang="EN-US"}**]{#struct_0_20662_54297_x1981267452}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[成员关系报告报文调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_20662_54297_1496222491}[：表示]{style="font-family:宋体"}[MLD]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20662_54297_x866881616}

[**[debugging]{lang="EN-US"}**[ **mld**]{lang="EN-US"}]{#struct_0_20662_54297_x495282590}[命令用来打开]{style="font-family:宋体"}[MLD]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **mld**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[MLD]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MLD]{lang="EN-US"}]{#struct_0_20662_54297_1586445380}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mld done]{lang="EN-US"}]{#struct_0_20662_54297_x820029066}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_538340807}[[字段]{style="font-family:黑体"}]{#struct_0_20662_54297_x1546118683}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20662_54297_1229281342}

[[Ignore MLD packet from *src* to *dest*]{lang="EN-US"}]{#struct_0_20662_54297_1970317505}

[[忽略源地址为]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_20662_54297_x1762034639}[、]{style="font-family:宋体"}[目的地址为]{style="font-family:宋体"}*[dest]{lang="EN-US"}*[的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[TTL is 0]{lang="EN-US"}]{#struct_0_20662_54297_1239762369}

[[TTL]{lang="EN-US"}]{#struct_0_20662_54297_1721499126}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[length *length* is too short]{lang="EN-US"}]{#struct_0_20662_54297_x819963530}

[[报文长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_20662_54297_728462640}[太短]{style="font-family:宋体"}

[[Router-Alert option]{lang="EN-US"}]{#struct_0_20662_54297_35276284}

[[IPv6]{lang="EN-US"}]{#struct_0_20662_54297_x66205509}[选项]{style="font-family:宋体"}[Router-Alert]{lang="EN-US"}

[[interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_20662_54297_x785684641}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_1885345691}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[done]{lang="EN-US"}]{#struct_0_20662_54297_x819373706}

[[MLD]{lang="EN-US"}]{#struct_0_20662_54297_1116763243}[离开组报文]{style="font-family:宋体"}

[[group address *gaddr* is not in multicast range ]{lang="EN-US"}]{#struct_0_20662_54297_2133567223}

[[组播组]{style="font-family:宋体"}[g*addr*]{lang="EN-US"}]{#struct_0_20662_54297_1335012074}[不是组播地址]{style="font-family:宋体"}

[[group address *gaddr* is reserved ]{lang="EN-US"}]{#struct_0_20662_54297_x1695547818}

[[组地址]{style="font-family:宋体"}[g*addr*]{lang="EN-US"}]{#struct_0_20662_54297_304039346}[为保留地址]{style="font-family:宋体"}

[[group address g*addr* is node-local]{lang="EN-US"}]{#struct_0_20662_54297_x819308170}

[[组地址]{style="font-family:宋体"}[g*addr*]{lang="EN-US"}]{#struct_0_20662_54297_1456961307}[为节点本地地址]{style="font-family:宋体"}

[[group address g*addr* is link-local]{lang="EN-US"}]{#struct_0_20662_54297_708489039}

[[组地址]{style="font-family:宋体"}[g*addr*]{lang="EN-US"}]{#struct_0_20662_54297_187391723}[为链路本地地址]{style="font-family:宋体"}

[[scope of group address g*addr* is zero]{lang="EN-US"}]{#struct_0_20662_54297_1841265382}

[[组地址]{style="font-family:宋体"}[g*addr*]{lang="EN-US"}]{#struct_0_20662_54297_x819897997}[的]{style="font-family:宋体"}[Scope]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[group(]{lang="EN-US"}*[gaddr)]{lang="EN-US"}*]{#struct_0_20662_54297_1087588291}

[[组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x1454779904}

[[this group does not exist]{lang="EN-US"}]{#struct_0_20662_54297_x380216050}

[[组播组不存在]{style="font-family:宋体"}]{#struct_0_20662_54297_x1482281607}

[[this group has v1 host]{lang="EN-US"}]{#struct_0_20662_54297_x819832461}

[[存在]{style="font-family:宋体"}[MLDv1]{lang="EN-US"}]{#struct_0_20662_54297_1514007017}[的主机]{style="font-family:宋体"}

[[fast-leave is off and interface is non-querier]{lang="EN-US"}]{#struct_0_20662_54297_x767592000}

[[组播组成员快速离开功能处于关闭状态，接口也不是查询器]{style="font-family:宋体"}]{#struct_0_20662_54297_730663514}

[[this group is leaving]{lang="EN-US"}]{#struct_0_20662_54297_x1301065663}

[[组播组正在离开]{style="font-family:宋体"}]{#struct_0_20662_54297_x819766925}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging mld event]{lang="EN-US"}]{#struct_0_20662_54297_x513295368}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_566233095}[[字段]{style="font-family:黑体"}]{#struct_0_20662_54297_x1831325755}

[[描述]{style="font-family:黑体"}]{#struct_0_20662_54297_2108517006}

[[Create/Add/Remove/Delete MLD configuration interface *interfacename* ]{lang="EN-US"}]{#struct_0_20662_54297_236942685}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20662_54297_1155793774}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[移动]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[MLD]{lang="EN-US"}[配置接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*

[[Create /Delete MLD interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_20662_54297_491898598}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20662_54297_x819701389}[删除]{style="font-family:宋体"}[MLD]{lang="EN-US"}[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*[，其地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_20662_54297_x1245356499}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_1178916208}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[Send/Notify/Receive/Ignore]{lang="EN-US"}]{#struct_0_20662_54297_x92606590}

[[发送]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20662_54297_1472635555}[通知]{style="font-family:宋体"}[/]{lang="EN-US"}[接收]{style="font-family:宋体"}[/]{lang="EN-US"}[忽略]{style="font-family:宋体"}

[*[message-type]{lang="EN-US"}*[ message]{lang="EN-US"}]{#struct_0_20662_54297_1057985169}

[*[message-type]{lang="EN-US"}*]{#struct_0_20662_54297_x1333797659}[类型的消息，]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[join-prune]{lang="EN-US"}]{#struct_0_20662_54297_x820160141}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[加入]{lang="EN-US" style="font-family:
  宋体"}[/]{lang="EN-US"}[剪枝消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[querier]{lang="EN-US"}]{#struct_0_20662_54297_1995374801}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[查询器消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth]{lang="EN-US"}]{#struct_0_20662_54297_1418996540}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[平滑消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth over]{lang="EN-US"}]{#struct_0_20662_54297_296938808}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[平滑结束消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HA]{lang="EN-US"}]{#struct_0_20662_54297_742891992}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[高可靠性相关的消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MLD enable]{lang="EN-US"}]{#struct_0_20662_54297_x1349634888}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[协议使能消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MRIB connection up]{lang="EN-US"}]{#struct_0_20662_54297_x820094605}[：]{lang="EN-US" style="font-family:
  宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[与]{lang="EN-US" style="font-family:宋体"}[MRIB]{lang="EN-US"}[建立连接成功消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MRIB connection down]{lang="EN-US"}]{#struct_0_20662_54297_513486344}[：]{lang="EN-US" style="font-family:
  宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[与]{lang="EN-US" style="font-family:宋体"}[MRIB]{lang="EN-US"}[连接中断消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MRIB smooth]{lang="EN-US"}]{#struct_0_20662_54297_x6916282}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[与]{lang="EN-US" style="font-family:
  宋体"}[MRIB]{lang="EN-US"}[进行平滑消息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicast boundary message]{lang="EN-US"}]{#struct_0_20662_54297_x587423086}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[组播边界消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicast routing-enable]{lang="EN-US"}]{#struct_0_20662_54297_376688726}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[三层组播使能消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicast routing-disable]{lang="EN-US"}]{#struct_0_20662_54297_x820029069}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[三层组播关闭消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIM DR]{lang="EN-US"}]{#struct_0_20662_54297_x1546053147}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[指定路由器消息]{lang="EN-US" style="font-family:宋体"}

[[MRIB]{lang="EN-US"}]{#struct_0_20662_54297_x1461754397}

[[组播路由信息库]{style="font-family:宋体"}]{#struct_0_20662_54297_x1854992728}

[[set binary data]{lang="EN-US"}]{#struct_0_20662_54297_x483076074}

[[设置二进制数据]{style="font-family:宋体"}]{#struct_0_20662_54297_x819963533}

[[static-group]{lang="EN-US"}]{#struct_0_20662_54297_728528176}

[[添加静态组]{style="font-family:宋体"}]{#struct_0_20662_54297_407425611}

[[open DBM ]{lang="EN-US"}]{#struct_0_20662_54297_1969544169}

[[打开]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_20662_54297_x819373709}

[[batch backup data on interface(*interfacename*) configuration]{lang="EN-US"}]{#struct_0_20662_54297_1116697707}

[[关于接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x1046644354}[配置的批量备份数据]{style="font-family:宋体"}

[[batch backup data on global configuration]{lang="EN-US"}]{#struct_0_20662_54297_x819308173}

[[关于全局配置的批量备份数据]{style="font-family:宋体"}]{#struct_0_20662_54297_1456764699}

[[Add/Delete address  *address* for interface *interfacename*]{lang="EN-US"}]{#struct_0_20662_54297_x463121859}

[[为接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_569546073}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[(*saddr, gaddr*)]{lang="EN-US"}]{#struct_0_20662_54297_x819897996}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_20662_54297_1087522755}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项，]{style="font-family:宋体"}*[saddr]{lang="EN-US"}*[为源地址，]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*[为组地址]{style="font-family:宋体"}

[[group(*gaddr*)]{lang="EN-US"}]{#struct_0_20662_54297_x1056469610}

[[组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x819832460}

[[Change mode from *mode1* to *mode2*]{lang="FR"}]{#struct_0_20662_54297_1513941481}

[[组播组的模式由]{style="font-family:宋体"}]{#struct_0_20662_54297_x640446614}*[mode1]{lang="FR"}*[变更为]{style="font-family:宋体"}*[mode2]{lang="FR"}*[，具体模式包括]{style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[和]{style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}

[[Create group (*gaddr*)]{lang="EN-US"}]{#struct_0_20662_54297_x1869851220}

[[创建组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x819766924}

[[Becomes querier/non-querier]{lang="EN-US"}]{#struct_0_20662_54297_x513229832}

[[成为查询器]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20662_54297_1712456246}[非查询器]{style="font-family:宋体"}

[[Stop event thread]{lang="EN-US"}]{#struct_0_20662_54297_x819701388}

[[终止事件处理线程]{style="font-family:宋体"}]{#struct_0_20662_54297_x1245290963}

[[real time backup data]{lang="EN-US"}]{#struct_0_20662_54297_x820160140}

[[实时备份数据]{style="font-family:宋体"}]{#struct_0_20662_54297_1995440337}

[[batch backup data]{lang="EN-US"}]{#struct_0_20662_54297_x1340188630}

[[批量备份数据]{style="font-family:宋体"}]{#struct_0_20662_54297_x820094604}

[[HA batch backup event]{lang="EN-US"}]{#struct_0_20662_54297_513420808}

[[高可靠性的批量备份事件]{style="font-family:宋体"}]{#struct_0_20662_54297_1155049785}

[[HA degrade/stop/upgrade event]{lang="EN-US"}]{#struct_0_20662_54297_x820029068}

[[高可靠性的降级]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20662_54297_x1545987611}[停止]{style="font-family:宋体"}[/]{lang="EN-US"}[升级事件]{style="font-family:宋体"}

[*[event]{lang="EN-US"}*[ event on interface *interfacename*]{lang="EN-US"}]{#struct_0_20662_54297_x105893104}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x231637685}[上发生事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_20662_54297_x819963532}[：表示添加接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_20662_54297_728593712}[：表示删除接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x3]{lang="EN-US"}]{#struct_0_20662_54297_447003816}[：表示接口]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x4]{lang="EN-US"}]{#struct_0_20662_54297_x819373708}[：表示接口]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x6]{lang="EN-US"}]{#struct_0_20662_54297_1116632171}[：表示接口配置变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x9]{lang="EN-US"}]{#struct_0_20662_54297_x1769137242}[：表示接口解除绑定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0xa]{lang="EN-US"}]{#struct_0_20662_54297_x819308172}[：表示拔出接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0xb]{lang="EN-US"}]{#struct_0_20662_54297_1456830235}[：表示插入接口]{lang="EN-US" style="font-family:宋体"}

[[address event *event* on interface *interfacename* (*address*), state is *state*]{lang="EN-US"}]{#struct_0_20662_54297_1087513610}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x819897999}[（地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[）上发生地址事件。事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[event]{lang="EN-US"}*]{#struct_0_20662_54297_1087195075}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_20662_54297_41139805}[：表示添加地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_20662_54297_x819832463}[：表示删除地址]{lang="EN-US" style="font-family:宋体"}

[*[state]{lang="EN-US"}*]{#struct_0_20662_54297_1513875945}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x200]{lang="EN-US"}]{#struct_0_20662_54297_1345544689}[：表示主地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x400]{lang="EN-US"}]{#struct_0_20662_54297_x819766927}[：表示链路本地地址]{style="font-family:宋体"}

[[ifnet connection down event]{lang="EN-US"}]{#struct_0_20662_54297_x513164296}

[[与接口管理的连接中断事件]{style="font-family:宋体"}]{#struct_0_20662_54297_x819701391}

[[Process interface *interfacename* *event*]{lang="EN-US"}]{#struct_0_20662_54297_x1245880786}

[[处理接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x953667229}[上发生的事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_20662_54297_x820160143}[：表示添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_20662_54297_1995505873}[：表示删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[plugout]{lang="EN-US"}]{#struct_0_20662_54297_x820094607}[：表示拔出]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_20662_54297_513617416}[：表示连接成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_20662_54297_1073164678}[：表示连接中断]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[attribute changed]{lang="EN-US"}]{#struct_0_20662_54297_x820029071}[：表示属性变化]{lang="EN-US" style="font-family:
  宋体"}

[[MLD proxy]{lang="EN-US"}]{#struct_0_20662_54297_278253669}

[[MLD]{lang="EN-US"}]{#struct_0_20662_54297_x1885580222}[代理]{style="font-family:宋体"}

[[proxy database]{lang="EN-US"}]{#struct_0_20662_54297_278319205}

[[代理成员关系数据库]{style="font-family:宋体"}]{#struct_0_20662_54297_1271759190}

[[proxy cache]{lang="EN-US"}]{#struct_0_20662_54297_x586671316}

[[代理缓存]{style="font-family:宋体"}]{#struct_0_20662_54297_278909029}

[[Create/Delete MLD proxy interface *interfacename*]{lang="EN-US"}]{#struct_0_20662_54297_x344429833}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20662_54297_278974565}[删除]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*

[[Send MLD proxy enable/disable on interface *interfacename* to MRIB]{lang="EN-US"}]{#struct_0_20662_54297_x373378595}

[[通过接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x1321247409}[向]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[通知使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}[MLD]{lang="EN-US"}[代理功能]{style="font-family:宋体"}

[[Add/Remove source(*saddr*) to proxy cache on interface *interfacename* for group(*gaddr*)]{lang="EN-US"}]{#struct_0_20662_54297_278384742}

[[在接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x1522809001}[上为组节点]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除源节点]{style="font-family:宋体"}*[saddr]{lang="EN-US"}*[到代理缓存]{style="font-family:宋体"}

[[Add/Remove/Update group(*gaddr*) to proxy cache on interface *interfacename*]{lang="EN-US"}]{#struct_0_20662_54297_278450278}

[[在接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x833584683}[上添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新组节点]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*[到代理缓存]{style="font-family:宋体"}

[[Add/Remove source(*saddr*) to proxy database for group(*gaddr*)]{lang="EN-US"}]{#struct_0_20662_54297_278515814}

[[在代理成员关系数据库的组节点]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x18496077}[下添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除源]{style="font-family:宋体"}*[saddr]{lang="EN-US"}*

[[Add INCLUDE/EXCLUDE group(*gaddr*) to proxy database]{lang="EN-US"}]{#struct_0_20662_54297_278581350}

[[在代理成员关系数据库中添加]{style="font-family:宋体"}[INCLUDE/EXCLUDE]{lang="EN-US"}]{#struct_0_20662_54297_278122598}[模式的组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mld query]{lang="EN-US"}]{#struct_0_20662_54297_x1546577436}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_564729095}[[字段]{style="font-family:黑体"}]{#struct_0_20662_54297_x970679047}

[[描述]{style="font-family:黑体"}]{#struct_0_20662_54297_1406396754}

[[Ignore MLD packet from *src* to *dest*]{lang="EN-US"}]{#struct_0_20662_54297_306842944}

[[忽略源地址为]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_20662_54297_1609505685}[、]{style="font-family:宋体"}[目的地址为]{style="font-family:宋体"}*[dest]{lang="EN-US"}*[的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[TTL is 0]{lang="EN-US"}]{#struct_0_20662_54297_x819963535}

[[TTL]{lang="EN-US"}]{#struct_0_20662_54297_728134960}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[length *length* is too short]{lang="EN-US"}]{#struct_0_20662_54297_333589838}

[[报文长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_20662_54297_x179458047}[太短]{style="font-family:宋体"}

[[Router-Alert option]{lang="EN-US"}]{#struct_0_20662_54297_1515740587}

[[IPv6]{lang="EN-US"}]{#struct_0_20662_54297_17695947}[选项]{style="font-family:宋体"}[Router-Alert]{lang="EN-US"}

[[interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_20662_54297_x23718280}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x819373711}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[query]{lang="EN-US"}]{#struct_0_20662_54297_1117221996}

[[MLD]{lang="EN-US"}]{#struct_0_20662_54297_x1397911357}[查询报文]{style="font-family:宋体"}

[[length is invalid]{lang="EN-US"}]{#struct_0_20662_54297_x742873966}

[[报文长度非法]{style="font-family:宋体"}]{#struct_0_20662_54297_877698356}

[[group address is invalid]{lang="EN-US"}]{#struct_0_20662_54297_1628292183}

[[组地址非法]{style="font-family:宋体"}]{#struct_0_20662_54297_x819308175}

[[group address *gaddr* is reserved ]{lang="EN-US"}]{#struct_0_20662_54297_1457157915}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x1229458250}[为保留地址]{style="font-family:宋体"}

[[group address *gaddr* is node-local]{lang="EN-US"}]{#struct_0_20662_54297_x820331397}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_60126619}[为节点本地地址]{style="font-family:宋体"}

[[group address *gaddr* is link-local]{lang="EN-US"}]{#struct_0_20662_54297_x819897998}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_1087129539}[为链路本地地址]{style="font-family:宋体"}

[[general query]{lang="EN-US"}]{#struct_0_20662_54297_x1434433771}

[[MLD]{lang="EN-US"}]{#struct_0_20662_54297_332287844}[普遍组查询]{style="font-family:宋体"}

[[group specific query]{lang="EN-US"}]{#struct_0_20662_54297_x1321939254}

[[MLD]{lang="EN-US"}]{#struct_0_20662_54297_x819832462}[特定组查询]{style="font-family:宋体"}

[[group-source specific query]{lang="EN-US"}]{#struct_0_20662_54297_1513810409}

[[MLD]{lang="EN-US"}]{#struct_0_20662_54297_2073822236}[特定源组查询]{style="font-family:宋体"}

[[group *gaddr*]{lang="EN-US"}]{#struct_0_20662_54297_1739854007}

[[查询的组地址为]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x819766926}

[[source count *num*]{lang="EN-US"}]{#struct_0_20662_54297_x513098760}

[[源数目为]{style="font-family:宋体"}*[num]{lang="EN-US"}*]{#struct_0_20662_54297_x306612594}

[[S flag]{lang="EN-US"}]{#struct_0_20662_54297_1839270005}

[[查询报文的]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_20662_54297_x819701390}[标记]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging mld report]{lang="EN-US"}]{#struct_0_20662_54297_x1245815250}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_560547911}[[字段]{style="font-family:黑体"}]{#struct_0_20662_54297_1408097251}

[[描述]{style="font-family:黑体"}]{#struct_0_20662_54297_x234389058}

[[Ignore MLD packet from *src* to *dest*]{lang="EN-US"}]{#struct_0_20662_54297_x1520430476}

[[忽略源地址为]{style="font-family:宋体"}*[src]{lang="EN-US"}*]{#struct_0_20662_54297_x1730734369}[、]{style="font-family:宋体"}[目的地址为]{style="font-family:宋体"}*[dest]{lang="EN-US"}*[的]{style="font-family:宋体"}[MLD]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[TTL is 0]{lang="EN-US"}]{#struct_0_20662_54297_1240852405}

[[TTL]{lang="EN-US"}]{#struct_0_20662_54297_1103780248}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[length *length* is too short]{lang="EN-US"}]{#struct_0_20662_54297_x820160142}

[[报文长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_20662_54297_1995571409}[太短]{style="font-family:宋体"}

[[Router-Alert option]{lang="EN-US"}]{#struct_0_20662_54297_x1341987985}

[[IPv6]{lang="EN-US"}]{#struct_0_20662_54297_x1347881383}[选项]{style="font-family:宋体"}[Router-Alert]{lang="EN-US"}

[[interface *interfacename*(*address*)]{lang="EN-US"}]{#struct_0_20662_54297_2058423763}

[[接口]{style="font-family:宋体"}*[interfacename]{lang="EN-US"}*]{#struct_0_20662_54297_x1109017791}[的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[group address *gaddr* is not in multicast range ]{lang="EN-US"}]{#struct_0_20662_54297_x820094606}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_513551880}[不是组播地址]{style="font-family:宋体"}

[[group address *gaddr* is reserved ]{lang="EN-US"}]{#struct_0_20662_54297_407546196}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x1086936081}[为保留地址]{style="font-family:宋体"}

[[group address *gaddr* is node-local]{lang="EN-US"}]{#struct_0_20662_54297_826421813}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x820029070}[为节点本地地址]{style="font-family:宋体"}

[[group address *gaddr* is link-local]{lang="EN-US"}]{#struct_0_20662_54297_x1546511900}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_1582228392}[为链路本地地址]{style="font-family:宋体"}

[[scope of group address *gaddr* is scope-none]{lang="EN-US"}]{#struct_0_20662_54297_x144452908}

[[组地址]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_x1152309224}[的]{style="font-family:宋体"}[Scope]{lang="EN-US"}[为]{style="font-family:宋体"}[scope-none]{lang="EN-US"}

[[group(]{lang="EN-US"}*[gaddr)]{lang="EN-US"}*]{#struct_0_20662_54297_x819963534}

[[组播组]{style="font-family:宋体"}*[gaddr]{lang="EN-US"}*]{#struct_0_20662_54297_728200496}

[[report]{lang="EN-US"}]{#struct_0_20662_54297_970600538}

[[MLD]{lang="EN-US"}]{#struct_0_20662_54297_x1197700992}[成员关系报告报文]{style="font-family:宋体"}

[[group record]{lang="EN-US"}]{#struct_0_20662_54297_x819373710}

[[组播组记录]{style="font-family:宋体"}]{#struct_0_20662_54297_1117156460}

[[IS_IN/IS_EX/TO_IN/TO_EX/ALLOW/BLOCK]{lang="EN-US"}]{#struct_0_20662_54297_x1775768002}

[[MLDv2]{lang="EN-US"}]{#struct_0_20662_54297_x2020325224}[报告报文中组记录的类型]{style="font-family:宋体"}

[[number of sources is zero]{lang="EN-US"}]{#struct_0_20662_54297_x1350082521}

[[组播源的数目为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_20662_54297_x819308174}

[[this group does not exist]{lang="EN-US"}]{#struct_0_20662_54297_1457223451}

[[组播组不存在]{style="font-family:宋体"}]{#struct_0_20662_54297_1129957253}

[[old version host exists]{lang="EN-US"}]{#struct_0_20662_54297_x1213612509}

[[存在低版本主机]{style="font-family:宋体"}]{#struct_0_20662_54297_1102416306}

[[fast-leave is off and interface is non-querier]{lang="EN-US"}]{#struct_0_20662_54297_x904590180}

[[组播组成员快速离开功能处于关闭状态，接口也不是查询器]{style="font-family:宋体"}]{#struct_0_20662_54297_x1661210293}

[[v1 host exists]{lang="EN-US"}]{#struct_0_20662_54297_2054414881}

[[存在]{style="font-family:宋体"}[MLDv1]{lang="EN-US"}]{#struct_0_20662_54297_1102481842}[的主机]{style="font-family:宋体"}

[[can\'t pass multicast boundary]{lang="EN-US"}]{#struct_0_20662_54297_694654973}

[[不能通过组播边界]{style="font-family:宋体"}]{#struct_0_20662_54297_x2045755652}

[[can\'t pass group policy]{lang="EN-US"}]{#struct_0_20662_54297_485426151}

[[不能通过组播组策略]{style="font-family:宋体"}]{#struct_0_20662_54297_1102547378}

[[group address is in SSM range]{lang="EN-US"}]{#struct_0_20662_54297_1822130451}

[[组地址属于]{style="font-family:宋体"}[SSM]{lang="EN-US"}]{#struct_0_20662_54297_x827116602}[组范围]{style="font-family:宋体"}

[[destination address *addr* is invalid]{lang="EN-US"}]{#struct_0_20662_54297_x1048307809}

[[目的地址]{style="font-family:宋体"}*[addr]{lang="EN-US"}*]{#struct_0_20662_54297_1102612914}[非法]{style="font-family:宋体"}

[[Proxy send]{lang="EN-US"}]{#struct_0_20662_54297_278515819}

[[代理发送]{style="font-family:宋体"}]{#struct_0_20662_54297_278581355}

[[Failed to send packet]{lang="EN-US"}]{#struct_0_20662_54297_x1617824536}

[[发送报文失败]{style="font-family:宋体"}]{#struct_0_20662_54297_909111701}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging mld timer]{lang="EN-US"}]{#struct_0_20662_54297_x847037839}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_583732231}[[字段]{style="font-family:黑体"}]{#struct_0_20662_54297_1745144164}

[[描述]{style="font-family:黑体"}]{#struct_0_20662_54297_x806194864}

[[Static group activation timer]{lang="EN-US"}]{#struct_0_20662_54297_1572979525}

[[静态组激活定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_x1820255634}

[[Group reset timer]{lang="EN-US"}]{#struct_0_20662_54297_1102154162}

[[表项清除定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_x133040583}

[[Multicast boundary timer]{lang="EN-US"}]{#struct_0_20662_54297_x264511065}

[[组播边界定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_1727567298}

[[Multicast ]{lang="EN-US"}[routing enable timer]{lang="EN-US"}]{#struct_0_20662_54297_1285537448}

[[组播使能定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_x746204004}

[[v1/v2 host timer]{lang="EN-US"}]{#struct_0_20662_54297_1102219698}

[[v1/v2]{lang="EN-US"}]{#struct_0_20662_54297_x2086519402}[主机存在定时器]{style="font-family:宋体"}

[[Source aging timer]{lang="EN-US"}]{#struct_0_20662_54297_x981474210}

[[源老化定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_1491212117}

[[Group aging timer]{lang="EN-US"}]{#struct_0_20662_54297_308244408}

[[组老化定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_295387608}

[[Group retransmit timer]{lang="EN-US"}]{#struct_0_20662_54297_1102285234}

[[组重传定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_637365040}

[[General query timer]{lang="EN-US"}]{#struct_0_20662_54297_1378817628}

[[普遍组查询定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_567114504}

[[Source retransmit timer]{lang="EN-US"}]{#struct_0_20662_54297_x130448976}

[[源重传定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_1102350770}

[[Delay timer]{lang="EN-US"}]{#struct_0_20662_54297_x507999410}

[[延迟发送报告报文定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_x1449456840}

[[Other/other querier present timer]{lang="EN-US"}]{#struct_0_20662_54297_1453859852}

[[其它查询器存在时间定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_1359893577}

[[Create/Delete/Set/expired]{lang="EN-US"}]{#struct_0_20662_54297_x695286211}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20662_54297_1430589113}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[设置]{style="font-family:宋体"}[/]{lang="EN-US"}[超时]{style="font-family:宋体"}

[[Smooth timer]{lang="EN-US"}]{#struct_0_20662_54297_1102940594}

[[平滑定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_1077617356}

[[Smooth over timer]{lang="EN-US"}]{#struct_0_20662_54297_x464749625}

[[平滑结束定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_1621487916}

[[Proxy database adjust timer]{lang="EN-US"}]{#struct_0_20662_54297_278319211}

[[代理成员关系数据库调整定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_278909035}

[[old querier present timer]{lang="EN-US"}]{#struct_0_20662_54297_1611885291}

[[旧版本查询器的存在时间定时器]{style="font-family:宋体"}]{#struct_0_20662_54297_278974571}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20662_54297_1497349825}

[[\# ]{lang="EN-US"}]{#struct_0_20662_54297_x1227276449}[在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MLD]{lang="EN-US"}[离开组报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mld done]{lang="EN-US"}]{#struct_0_20662_54297_1103006130}

[\*Jun 23 15:01:00:288 2011 Sysname MLD/7/DONE: -MDC=1; Received MLDv1 done for group FF0E::101:101 on interface GigabitEthernet1/0/1(FE80::1:101) (G19849)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_x879293151}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到离开组]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}[的报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20662_54297_x1288604045}[在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MLD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mld event]{lang="EN-US"}]{#struct_0_20662_54297_1961453254}

[\*Jun 23 15:06:16:139 2011 Sysname MLD/7/EVENT: -MDC=1; Create group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) (G102769)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_x348475116}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上创建组播组]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}*

[[\*Jun 23 15:06:16:152 2011 Sysname MLD/7/EVENT: -MDC=1; Change mode from INCLUDE to EXCLUDE for group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) (G101882)]{lang="EN-US"}]{#struct_0_20662_54297_x1615875204}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_955607101}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上组播组]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}[的模式由]{style="font-family:宋体"}[INCLUDE]{lang="EN-US"}[变为]{style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}*

[[\*Jun 23 15:06:16:153 2011 Sysname MLD/7/EVENT: -MDC=1; Send JOIN for (::,FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) to MRIB (G10105)]{lang="EN-US"}]{#struct_0_20662_54297_1102416307}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_x904655716}*[通知]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上有（]{style="font-family:宋体"}[::]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}[）加入]{style="font-family:宋体"}*

[[\*Jun 23 15:06:39:766 2011 Sysname MLD/7/EVENT: -MDC=1; Change mode from EXCLUDE to INCLUDE for group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) (G101789)]{lang="EN-US"}]{#struct_0_20662_54297_x543344470}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_x2105852263}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上组播组]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}[的模式由]{style="font-family:宋体"}[EXCLUDE]{lang="EN-US"}[变为]{style="font-family:宋体"}[INCLUDE]{lang="EN-US"}*

[[\*Jun 23 15:06:39:767 2011 Sysname MLD/7/EVENT: -MDC=1; Send PRUNE for (::,FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) to MRIB (G10105)]{lang="EN-US"}]{#struct_0_20662_54297_878271065}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_1250922740}*[通知]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上有（]{style="font-family:宋体"}[::]{lang="EN-US"}[，]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}[）离开]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20662_54297_84294328}[在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mld query receive]{lang="EN-US"}]{#struct_0_20662_54297_x656339426}

[\*Jun 22 18:31:11:221 2011 Sysname MLD/7/QUERY SEND: -MDC=1; Received MLD  v1 query on GigabitEthernet1/0/1(FE80::1:101) from FE80::1:102 (G10308) ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_x1036311934}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到]{style="font-family:宋体"}[MLDv1]{lang="EN-US"}[普遍组查询报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20662_54297_1102481843}[在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[MLD]{lang="EN-US"}[查询报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mld query send]{lang="EN-US"}]{#struct_0_20662_54297_694720509}

[Jun 23 15:16:32:744 2011 Sysname MLD/7/QUERY SEND: -MDC=1; Send MLD version 1 general query on GigabitEthernet1/0/1(FE80::1:101) to destination FF02::1 (G10308)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_1169344583}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[MLDv1]{lang="EN-US"}[普遍组查询报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20662_54297_x203217325}[在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MLD]{lang="EN-US"}[成员关系报告报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mld report]{lang="EN-US"}]{#struct_0_20662_54297_1532579471}

[\*Jun 23 15:55:25:514 2011 Sysname MLD/7/REPORT: -MDC=1; Received MLDv1 report for group FF0E::101:101 on interface GigabitEthernet1/0/1(FE80::1:101) (G19849)]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_20662_54297_1412908209}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上收到加入组]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}[的成员关系报告报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20662_54297_1479846102}[在接口上使能]{style="font-family:宋体"}[MLD]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MLD]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mld timer]{lang="EN-US"}]{#struct_0_20662_54297_x1325207647}

[\*Jun 22 18:53:49:129 2011 Sysname MLD/7/TIMER: -MDC=1; ]{lang="NO-BOK"}[Setting v1 host timer for group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) to 260s (G102089)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_1102547379}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[设置组]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}[的]{style="font-family:宋体"}[MLDv1]{lang="EN-US"}[主机存在定时器]{style="font-family:宋体"}*

[[\*Jun 22 18:55:58:012 2011 Sysname MLD/7/TIMER: -MDC=1;]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[Setting group aging timer for group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) to 260s (G102379)]{lang="EN-US"}]{#struct_0_20662_54297_1822195987}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_1171641832}*[设置组]{style="font-family:宋体"}[FF0E::101:101]{lang="EN-US"}[的老化定时器超时]{style="font-family:宋体"}*

[[\*Jun 22 18:56:33:261 2011 Sysname MLD/7/TIMER: -MDC=1; ]{lang="NO-BOK"}[Setting general query timer on interface GigabitEthernet1/0/1(FE80::1:101) to 125s (G10338)]{lang="EN-US"}]{#struct_0_20662_54297_513720359}

[*[// ]{lang="EN-US"}*]{#struct_0_20662_54297_1476163835}*[设置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的普遍组查询定时器]{style="font-family:宋体"}*
