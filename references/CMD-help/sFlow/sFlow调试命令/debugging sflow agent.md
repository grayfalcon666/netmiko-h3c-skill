::: {#-17207008 .myid}
[]{#_Toc404797326}[]{#struct_0_x1536_97982_778864389}[]{#_Toc306018988}

**sFlow \-- sFlow调试命令 \-- debugging sflow agent**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1560864803}

[**[debugging sflow agent]{lang="EN-US"}**]{#struct_0_x1536_97982_x1078254289}

[**[undo debugging sflow agent]{lang="EN-US"}**]{#struct_0_x1536_97982_x1505933080}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1630589770}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1156627279}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1536_97982_261373008}

[[network-admin]{lang="EN-US"}]{#struct_0_x1536_97982_1385429116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1536_97982_x1289861456}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1536_97982_778929925}

[[无]{style="font-family:宋体"}]{#struct_0_x1536_97982_2028219761}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1536_97982_553468042}

[]{#OLE_LINK1}[**[debugging sflow agent]{lang="EN-US"}**]{#struct_0_x1536_97982_1260717274}[命令用于打开]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging sflow agent]{lang="EN-US"}**[命令用于关闭]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[sFlow ]{lang="EN-US"}[Agent]{lang="EN-US"}]{#struct_0_x1536_97982_3048367}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_x1536_97982_365227215}[[表1-1 ]{lang="EN-US"}[debugging sflow agent]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1004174092}[[字段]{style="font-family:黑体"}]{#struct_0_x1536_97982_1221276435}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1536_97982_x2120004887}

[[Created a timer for finding agent address, interval *n* seconds]{lang="EN-US"}]{#struct_0_x1536_97982_x210542789}

[[创建寻找]{style="font-family:宋体"}[Agent]{lang="EN-US"}]{#struct_0_x1536_97982_778995461}[地址的定时器，间隔时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Destroyed the agent address timer.]{lang="EN-US"}]{#struct_0_x1536_97982_1190539583}

[[删除寻找]{style="font-family:宋体"}[Agent]{lang="EN-US"}]{#struct_0_x1536_97982_1589591711}[地址的定时器]{style="font-family:宋体"}

[[Created a timer for VPN reconnection, interval *n* seconds.]{lang="EN-US"}]{#struct_0_x1536_97982_x609752216}

[[创建]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1536_97982_438044749}[重连定时器，间隔时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Destroyed the VPN reconnection timer.]{lang="EN-US"}]{#struct_0_x1536_97982_493797565}

[[删除]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1536_97982_779585285}[重连定时器]{style="font-family:宋体"}

[[Received IF\_*event_name(event_id)* event on interface *interface_name(ifIndex).*]{lang="EN-US"}]{#struct_0_x1536_97982_1288197885}

[[收到]{style="font-family:宋体"}*[interface_name]{lang="EN-US"}*]{#struct_0_x1536_97982_79549724}[接口的]{style="font-family:宋体"}[IF\_*event_name*]{lang="EN-US"}[事件，该事件的事件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[event_id]{lang="EN-US"}*[，该接口索引为]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*

[[Succeeded in processing IF\_*event_name(event_id)* event on interface *interface-name(ifIndex).*]{lang="EN-US"}]{#struct_0_x1536_97982_x62510239}

[[处理]{style="font-family:宋体"}*[interface_name]{lang="EN-US"}*]{#struct_0_x1536_97982_x733091327}[接口的]{style="font-family:宋体"}[IF\_*event_name*]{lang="EN-US"}[事件成功，该事件的事件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[event_id]{lang="EN-US"}*[，该接口的接口索引为]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*

[[Failed to process IF*\_event_name(event_id)* event on interface *interface-name(ifIndex).*]{lang="EN-US"}]{#struct_0_x1536_97982_x253924075}

[[处理]{style="font-family:宋体"}*[interface_name]{lang="EN-US"}*]{#struct_0_x1536_97982_779650821}[接口的]{style="font-family:宋体"}[IF\_*event_name*]{lang="EN-US"}[事件失败，该事件的事件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[event_id]{lang="EN-US"}*[，该接口的接口索引为]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*

[[Received SLOT\_*event_name(event_id)* event for slot *slot_id.*]{lang="EN-US"}]{#struct_0_x1536_97982_x793929270}[（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Received SLOT\_*event_name(event_id)* event for chassis *chassis_id* slot *slot_id.*]{lang="EN-US"}]{#struct_0_x1536_97982_254741779}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[收到一个板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*]{#struct_0_x1536_97982_26472648}[的]{style="font-family:宋体"}[SLOT\_*event_name*]{lang="EN-US"}[事件，该事件的事件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[event_id]{lang="EN-US"}*[（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[收到一个成员设备]{style="font-family:宋体"}*[chassis_id]{lang="EN-US"}*]{#struct_0_x1536_97982_x734043830}[上一个板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*[的]{style="font-family:宋体"}[SLOT\_*event_name*]{lang="EN-US"}[事件，该事件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[event_id]{lang="EN-US"}*[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Received *event_name(event_id)* event for vpn-instance *vpn_name*(vrfindex *vrfIndex*).]{lang="EN-US"}]{#struct_0_x1536_97982_779060998}

[[收到一个名为]{style="font-family:宋体"}*[vpn_name]{lang="EN-US"}*]{#struct_0_x1536_97982_395781253}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}*[event_name]{lang="EN-US"}*[事件，该事件的事件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[event_id]{lang="EN-US"}*[，]{style="font-family:宋体"}*[vpn_name]{lang="EN-US"}*[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vrfIndex]{lang="EN-US"}*

[[Succeeded in finding agent address *address,* and broadcast it to all slots*.*]{lang="EN-US"}]{#struct_0_x1536_97982_2096706030}

[[成功找到]{style="font-family:宋体"}[Agent]{lang="EN-US"}]{#struct_0_x1536_97982_983905604}[地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*[，并同步到所有板]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1990936945}

[[\# ]{lang="EN-US"}]{#struct_0_x1536_97982_1282097344}[在一台设备上启动]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的调试信息开关，不配置]{style="font-family:宋体"}[Agent]{lang="EN-US"}[地址，进行如下操作：拔去某一接口板，然后插入；配置一]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，然后删除该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[[\<Sysname\> debugging sflow agent]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}]{#struct_0_x1536_97982_779126534}

[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ CREATE_AGNETIPTIMER:]{lang="EN-US"}

[Created a timer for finding agent address, interval 60 seconds. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_1083022521}*[在未配置]{style="font-family:宋体"}[Agent]{lang="EN-US"}[地址的情况下，创建]{style="font-family:宋体"}[Agent]{lang="EN-US"}[地址自动查找定时器，间隔时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[%Jun 13 10:03:53 673 2011 Sysname SFLOW/7/ DESTROY_AGENTIPTIMER:]{lang="EN-US"}]{#struct_0_x1536_97982_319393342}

[Destroyed the agent address timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_1026748725}*[自动查找到]{style="font-family:宋体"}[Agent]{lang="EN-US"}[地址后，删除]{style="font-family:宋体"}[Agent]{lang="EN-US"}[地址自动查找定时器]{style="font-family:宋体"}*

[[%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ RCV_IFEVENT:]{lang="EN-US"}]{#struct_0_x1536_97982_x486483879}

[Received IF_DEACTIVE(0x01) event on interface GigabitEthernet1/0/1(1).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x1755787180}*[拔去某一接口板，收到接口去激活事件]{style="font-family:宋体"}* *[，接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ PROC_IFEVENT:]{lang="EN-US"}]{#struct_0_x1536_97982_1294338037}

[Succeeded in processing IF\_ DEACTIVE(0x01) event on interface GigabitEthernet1/0/1(1).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x943410181}*[处理接口去激活事件]{style="font-family:宋体"}* *[，接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ RCV_SLOTEVENT:]{lang="EN-US"}]{#struct_0_x1536_97982_779192070}

[Received SLOT_INSERTED(0x01) event for slot 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_730284047}*[接口板插入，收到板插入事件，槽号为]{style="font-family:宋体"}[2]{lang="EN-US"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}*

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1536_97982_x1389360275}

[\[Sysname\] ip vpn-instance vpn]{lang="EN-US"}

[%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ RCV_VPNEVENT:]{lang="EN-US"}

[Received VPN_CREATE(0x01) event for vpn-instance vpn(vrfindex 1).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x1340782464}*[创建]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn]{lang="EN-US"}[，收到]{style="font-family:宋体"}[VPN]{lang="EN-US"}[创建事件，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[名字为]{style="font-family:宋体"}[vpn]{lang="EN-US"}[，索引为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\[Sysname\] undo ip vpn-instance vpn]{lang="EN-US"}]{#struct_0_x1536_97982_899711328}

[%Jun 13 10:03:53 673 2011 Sysname SFLOW/7/ CREATE_VPNTIMER:]{lang="EN-US"}

[Created a timer for VPN reconnection, interval 1 seconds.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_912725132}*[删除]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例后，创建]{style="font-family:宋体"}[VPN]{lang="EN-US"}[重连定时器，间隔时间为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[%Jun 13 10:03:53 673 2011 Sysname SFLOW/7/ DESTROY_VPNTIMER:]{lang="EN-US"}]{#struct_0_x1536_97982_543737411}

[Destroyed the VPN reconnection timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_779257606}*[删除]{style="font-family:宋体"}[VPN]{lang="EN-US"}[重连定时器]{style="font-family:宋体"}*

[[\[Sysname\] quit]{lang="EN-US"}]{#struct_0_x1536_97982_x207935533}

[\<Sysname\> debugging sflow synchronization]{lang="EN-US"}

[%Jun 13 10:04:53 674 2011 Sysname SFLOW/7/ LOOKUP_AGENTADDR:]{lang="EN-US"}

[Succeeded in finding agent address 192.168.20.104, and broadcast it to all slots.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x1442170675}*[自动寻找到]{style="font-family:宋体"}[Agent]{lang="EN-US"}[地址，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.20.104]{lang="EN-US"}[，并同步到所有接口板]{style="font-family:宋体"}*

::: {#-969233062 .myid}
[]{#_Toc404797327}[]{#struct_0_x1536_97982_x1683006369}[]{#_Toc306018989}

**sFlow \-- sFlow调试命令 \-- debugging sflow all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1545752348}

[**[debugging sflow all]{lang="EN-US"}**]{#struct_0_x1536_97982_x1386125269}

[**[undo debugging sflow all]{lang="EN-US"}**]{#struct_0_x1536_97982_461608413}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1482474126}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1932179108}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1536_97982_778798854}

[[network-admin]{lang="EN-US"}]{#struct_0_x1536_97982_x487278080}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1536_97982_x1338269848}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1170164562}

[[无]{style="font-family:宋体"}]{#struct_0_x1536_97982_x697825450}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x986741642}

[**[debugging sflow all]{lang="EN-US"}**]{#struct_0_x1536_97982_x1622951516}[命令用于打开所有]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging sflow all]{lang="EN-US"}**[命令用于关闭所有]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_x1536_97982_1735344375}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}
:::

::: {#131416466 .myid}
[]{#_Toc404797328}[]{#struct_0_x1536_97982_778864390}[]{#_Toc306018990}[]{#_Toc306010713}[]{#_Toc306010714}[]{#_Toc306010715}[]{#_Toc306010716}[]{#_Toc306010717}[]{#_Toc306010718}[]{#_Toc306010719}[]{#_Toc306010720}[]{#_Toc306010721}[]{#_Toc306010722}[]{#_Toc306010723}[]{#_Toc306010767}[]{#_Toc306010768}[]{#_Toc306010769}[]{#_Toc306010770}[]{#_Toc306010772}[]{#_Toc306010773}[]{#_Toc306010774}[]{#_Toc306010775}[]{#_Toc306010776}[]{#_Toc306010777}[]{#_Toc306010778}[]{#_Toc306010779}[]{#_Toc306010780}[]{#_Toc306010781}[]{#_Toc306010782}[]{#_Toc306010783}[]{#_Toc306010785}[]{#_Toc306010786}[]{#_Toc306010787}[]{#_Toc306010788}[]{#_Toc306010790}[]{#_Toc306010791}[]{#_Toc306010792}[]{#_Toc306010793}[]{#_Toc306010794}[]{#_Toc306010795}

**sFlow \-- sFlow调试命令 \-- debugging sflow collector**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x395450326}

[**[debugging sflow collector]{lang="EN-US"}**]{#struct_0_x1536_97982_x1969084889}

[**[undo debugging sflow collector]{lang="EN-US"}**]{#struct_0_x1536_97982_x240284861}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x830194118}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1536_97982_1007816613}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1055853591}

[[network-admin]{lang="EN-US"}]{#struct_0_x1536_97982_332121663}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1536_97982_x1946730009}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1536_97982_778929926}

[[无]{style="font-family:宋体"}]{#struct_0_x1536_97982_2028219762}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1536_97982_553533578}

[**[debugging sflow collector]{lang="EN-US"}**]{#struct_0_x1536_97982_x651641542}[命令用于打开]{style="font-family:
宋体"}[sFlow Collector]{lang="EN-US"}[的调试信息开关。]{style="font-family:
宋体"}**[undo debugging sflow collector]{lang="EN-US"}**[命令用于关闭]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}]{#struct_0_x1536_97982_x978813389}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging sflow collector]{lang="EN-US"}]{#struct_0_x1536_97982_1991341990}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1005349918}[[字段]{style="font-family:黑体"}]{#struct_0_x1536_97982_2073945134}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1787525877}

[[Created an aging timer for collector *collector-id*, interval *n* seconds.]{lang="EN-US"}]{#struct_0_x1536_97982_778995462}

[[创建]{style="font-family:宋体"}[Collector]{lang="EN-US"}[ *collector-id*]{lang="EN-US"}]{#struct_0_x1536_97982_1190539582}[的老化定时器，间隔时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Destroyed the aging timer for collector *collector-id*.]{lang="EN-US"}]{#struct_0_x1536_97982_1589657247}

[[删除]{style="font-family:宋体"}[Collector]{lang="EN-US"}[ *collector-id*]{lang="EN-US"}]{#struct_0_x1536_97982_x614345476}[的老化定时器]{style="font-family:宋体"}

[[Time to age out collector *collector-id*, and broadcast the event to all slots.]{lang="EN-US"}]{#struct_0_x1536_97982_1236283429}

[[Collector]{lang="EN-US"}[ *collector-id*]{lang="EN-US"}]{#struct_0_x1536_97982_318540278}[老化到期，并同步到所有板]{style="font-family:宋体"}

[[Broadcast new vrfindex *vrfindex* of vpn-instace *vpn_name* on collector *collector-id* to all slots.]{lang="EN-US"}]{#struct_0_x1536_97982_779585286}

[[广播绑定到]{style="font-family:宋体"}[Collector]{lang="EN-US"}[ *collector-id*]{lang="EN-US"}]{#struct_0_x1536_97982_1288197882}[的]{style="font-family:宋体"}[VPN *vpn_name*]{lang="EN-US"}[的新]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引]{style="font-family:宋体"}*[vrfindex]{lang="EN-US"}*

[[sFlow datagram version = *version*]{lang="EN-US"}]{#struct_0_x1536_97982_79090972}

[[sFlow]{lang="EN-US"}]{#struct_0_x1536_97982_1225879864}[版本号]{style="font-family:宋体"}

[[Agent IP version = *address_type*]{lang="EN-US"}]{#struct_0_x1536_97982_1898728529}

[[Agent]{lang="EN-US"}]{#struct_0_x1536_97982_2128524150}[地址类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1536_97982_779650822}[：]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1536_97982_x793929271}[：]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[Agent IP address = *address*]{lang="EN-US"}]{#struct_0_x1536_97982_254807315}

[[Agent]{lang="EN-US"}]{#struct_0_x1536_97982_x586497356}[地址]{style="font-family:宋体"}

[[Sub agent ID = *id*]{lang="EN-US"}]{#struct_0_x1536_97982_317891263}

[[子代理号]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593591994}

[[Sequence number = *number*]{lang="EN-US"}]{#struct_0_x1536_97982_232940011}

[[报文序列号]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1336662044}

[[UpTime = *UpTime*]{lang="EN-US"}]{#struct_0_x1536_97982_1837945796}

[[系统启动时间]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1693135626}

[[Sample number = *number*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593526458}

[[样本个数]{style="font-family:宋体"}]{#struct_0_x1536_97982_1824722799}

[[sFlow counter sample header information:]{lang="EN-US"}]{#struct_0_x1536_97982_x211805010}

[[Counter]{lang="EN-US"}]{#struct_0_x1536_97982_996487409}[采样样本头信息]{style="font-family:宋体"}

[[Data format = *format*]{lang="EN-US"}]{#struct_0_x1536_97982_1751073983}

[[样本类型]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593460922}

[[Sample length = *length*]{lang="EN-US"}]{#struct_0_x1536_97982_x647791210}

[[样本长度]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1916631542}

[[Data source type = *type*]{lang="EN-US"}]{#struct_0_x1536_97982_x992084428}

[[数据源类型]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593395386}

[[Data source index = *index*]{lang="EN-US"}]{#struct_0_x1536_97982_1943292699}

[[数据源索引]{style="font-family:宋体"}]{#struct_0_x1536_97982_x534357287}

[[Record number = *number*]{lang="EN-US"}]{#struct_0_x1536_97982_540050552}

[[记录个数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593854138}

[[sFlow flow sample header information:]{lang="EN-US"}]{#struct_0_x1536_97982_1781295083}

[[Flow]{lang="EN-US"}]{#struct_0_x1536_97982_x1369915726}[采样样本头信息]{style="font-family:宋体"}

[[Source id type = type]{lang="EN-US"}]{#struct_0_x1536_97982_x360905402}

[[数据源]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1536_97982_x1593788602}[类型]{style="font-family:宋体"}

[[Source id index = index]{lang="EN-US"}]{#struct_0_x1536_97982_x1747921663}

[[数据源]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1536_97982_x860066100}[索引]{style="font-family:宋体"}

[[Sampling rate = *rate*]{lang="EN-US"}]{#struct_0_x1536_97982_624221186}

[[采样率]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593723066}

[[Sample pool = *pool*]{lang="EN-US"}]{#struct_0_x1536_97982_976973797}

[[采样池]{style="font-family:宋体"}]{#struct_0_x1536_97982_1258398152}

[[Drops = *number*]{lang="EN-US"}]{#struct_0_x1536_97982_x166999543}

[[丢弃样本个数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593657530}

[[Input interface format = *format*]{lang="EN-US"}]{#struct_0_x1536_97982_1304412951}

[[入接口格式]{style="font-family:宋体"}]{#struct_0_x1536_97982_x722322901}

[[Input interface index = *ifIndex*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593067706}

[[入接口索引]{style="font-family:宋体"}]{#struct_0_x1536_97982_1732029224}

[[Output interface format = *format*]{lang="EN-US"}]{#struct_0_x1536_97982_x1888402087}

[[出接口格式]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593002170}

[[Output interface index= *ifIndex*]{lang="EN-US"}]{#struct_0_x1536_97982_1378599994}

[[出接口索引]{style="font-family:宋体"}]{#struct_0_x1536_97982_1721506554}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x653178367}

[[\# ]{lang="EN-US"}]{#struct_0_x1536_97982_x1536452901}[在一台设备上启动了]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的调试信息开关，进行如下配置：配置一个有老化时间的]{style="font-family:宋体"}[Collector]{lang="EN-US"}[；配置一个没有老化时间且能够正确收集报文的地址的]{style="font-family:宋体"}[Collector]{lang="EN-US"}[；在某接口下配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样实例，并能够正确采样；在某一接口下配置]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样实例，并能够正确采样；创建一]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例和配置一绑定到该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Collector]{lang="EN-US"}[，然后删除该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<[Sysname]{.TerminalDisplayChar}\> debugging sflow collector]{lang="EN-US"}]{#struct_0_x1536_97982_x1593591993}

[\<[Sysname]{.TerminalDisplayChar}\> system-view]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] sflow collector 1 ip 1.1.1.1 time-out 90]{lang="EN-US"}

[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ CREATE_COLLECTORTIMER:]{lang="EN-US"}

[Created an aging timer for collector 1, interval 90 seconds.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_636224538}*[创建]{style="font-family:宋体"}[Collector 1]{lang="EN-US"}[的老化定时器，间隔时间为]{style="font-family:宋体"}[90]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ AGE_COLLECTOR:]{lang="EN-US"}]{#struct_0_x1536_97982_2008841492}

[Time to age out collector 1, and broadcast the event to all slots.]{lang="EN-US"}

[*[// Collector 1]{lang="EN-US"}*]{#struct_0_x1536_97982_x1483568379}*[老化时间超时，并同步到所有接口板]{style="font-family:宋体"}*

[[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ DESTROY_COLLECTORTIMER:]{lang="EN-US"}]{#struct_0_x1536_97982_x1149322244}

[Destroyed the aging timer for collector 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x1583561425}*[删除]{style="font-family:宋体"}[Collector 1]{lang="EN-US"}[的老化定时器]{style="font-family:宋体"}*

[[\<[Sysname]{.TerminalDisplayChar}\> system-view]{lang="EN-US"}]{#struct_0_x1536_97982_x1593526457}

[\[[Sysname]{.TerminalDisplayChar}\] sflow collector 1 ip 11.1.1.1]{lang="EN-US"}

[\[Sysname\] sflow collector 2 ip 11.1.1.2]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow counter interval 2]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow counter collector 2]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow sampling-rate 1000]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow flow collector 1]{lang="EN-US"}

[\[Sysname\] \*Mar 29 10:37:40:515 2013 Sysname SFLOW/7/COLLECTOR: -MDC=1; sFlow counter sampl]{lang="EN-US"}

[e header information:]{lang="EN-US"}

[Data format = 4]{lang="EN-US"}

[Sample length = 60]{lang="EN-US"}

[Sequence number = 10]{lang="EN-US"}

[Data source type = 0]{lang="EN-US"}

[Data source index = 1]{lang="EN-US"}

[Record number = 3]{lang="EN-US"}

[\*Mar 29 10:37:39:504 2013 Sysname SFLOW/7/COLLECTOR: -MDC=1; sFlow send a packet]{lang="EN-US"}

[:]{lang="EN-US"}

[Collector ID = 2]{lang="EN-US"}

[Collector address = 11.1.1.2]{lang="EN-US"}

[Vrfindex = 0]{lang="EN-US"}

[sFlow datagram version = 5]{lang="EN-US"}

[Agent IP version = 1]{lang="EN-US"}

[Agent IP address = 10.1.1.1]{lang="EN-US"}

[Sub agent id = 0]{lang="EN-US"}

[Sequence number = 30]{lang="EN-US"}

[Uptime = 326000]{lang="EN-US"}

[Sample number = 1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x191699836}*[采集到一个]{style="font-family:宋体"}[Counter]{lang="EN-US"}[样本，打印样本头信息。其中数据格式为]{style="font-family:宋体"}[4]{lang="EN-US"}[，样本长度为]{style="font-family:宋体"}[60]{lang="EN-US"}[，样本序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，数据源类型为]{style="font-family:宋体"}[0]{lang="EN-US"}[，数据源索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，记录个数为]{style="font-family:宋体"}[3]{lang="EN-US"}*

[[\*Mar 29 13:44:31:966 2013 MSR26.62 SFLOW/7/COLLECTOR: sFlow flow sample header i]{lang="EN-US"}]{#struct_0_x1536_97982_x1593395385}

[nformation:]{lang="EN-US"}

[Data format = 3]{lang="EN-US"}

[Sample length = 80]{lang="EN-US"}

[Sequence number = 10]{lang="EN-US"}

[Source id type = 0]{lang="EN-US"}

[Source id index = 1]{lang="EN-US"}

[Sampling rate = 1000]{lang="EN-US"}

[Sample pool = 5000]{lang="EN-US"}

[Drops = 0]{lang="EN-US"}

[Input interface format = 0]{lang="EN-US"}

[Input interface = 1]{lang="EN-US"}

[Output interface format = 0]{lang="EN-US"}

[Output interface = 3]{lang="EN-US"}

[Record number = 5]{lang="EN-US"}

[\*Mar 29 13:44:32:635 2013 MSR26.62 SFLOW/7/COLLECTOR: sFlow send a packet:]{lang="EN-US"}

[Collector ID = 1]{lang="EN-US"}

[Collector address = 11.1.1.1]{lang="EN-US"}

[Vrfindex = 0]{lang="EN-US"}

[sFlow datagram version = 5]{lang="EN-US"}

[Agent IP version = 1]{lang="EN-US"}

[Agent IP address = 10.1.1.1]{lang="EN-US"}

[Sub agent id = 0]{lang="EN-US"}

[Sequence number = 2]{lang="EN-US"}

[Uptime = 18153000]{lang="EN-US"}

[Sample number = 1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x1948390070}*[采集到一个]{style="font-family:宋体"}[Flow]{lang="EN-US"}[样本，打印样本头信息。其中数据格式为]{style="font-family:宋体"}[3]{lang="EN-US"}[，样本长度为]{style="font-family:宋体"}[80]{lang="EN-US"}[，样本序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，数据源]{style="font-family:宋体"}[ID]{lang="EN-US"}[类型为]{style="font-family:宋体"}[0]{lang="EN-US"}[，数据源]{style="font-family:宋体"}[ID]{lang="EN-US"}[索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，采样率为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，样本次个数]{style="font-family:宋体"}[5000]{lang="EN-US"}[，丢弃个数]{style="font-family:宋体"}[0]{lang="EN-US"}[，入接口格式为]{style="font-family:宋体"}[0]{lang="EN-US"}[，入接口索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，出接口格式为]{style="font-family:宋体"}[0]{lang="EN-US"}[，出接口索引为]{style="font-family:宋体"}[3]{lang="EN-US"}[，记录个数为]{style="font-family:宋体"}[5]{lang="EN-US"}*

[[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}]{#struct_0_x1536_97982_1277081543}

[\[[Sysname]{.TerminalDisplayChar}\] sflow collector 3 vpn-instance vpn ip 1.1.1.1]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] ip vpn-instance vpn]{lang="EN-US"}

[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ COLLECTOR:]{lang="EN-US"}

[Broadcast new vrfindex 2 of vpn-instace vpn on collector 3 to all slots.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x198328208}*[配置]{style="font-family:宋体"}[Collector 3]{lang="EN-US"}[关联的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，创建该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，打印]{style="font-family:宋体"}[VPN]{lang="EN-US"}[变化调试信息]{style="font-family:宋体"}*

::: {#-1077993518 .myid}
[]{#_Toc404797329}[]{#struct_0_x1536_97982_x525369108}[]{#_Toc306018991}[]{#_Toc306010797}[]{#_Toc306010798}[]{#_Toc306010799}[]{#_Toc306010800}[]{#_Toc306010801}[]{#_Toc306010802}[]{#_Toc306010803}[]{#_Toc306010804}[]{#_Toc306010805}[]{#_Toc306010806}[]{#_Toc306010807}[]{#_Toc306010895}[]{#_Toc306010896}[]{#_Toc306010897}[]{#_Toc306010898}[]{#_Toc306010901}[]{#_Toc306010902}[]{#_Toc306010903}[]{#_Toc306010906}[]{#_Toc306010907}[]{#_Toc306010908}[]{#_Toc306010909}[]{#_Toc306010910}[]{#_Toc306010911}[]{#_Toc306010912}[]{#_Toc306010913}[]{#_Toc306010914}[]{#_Toc306010916}[]{#_Toc306010917}[]{#_Toc306010918}[]{#_Toc306010919}[]{#_Toc306010920}[]{#_Toc306010921}[]{#_Toc306010922}[]{#_Toc306010923}[]{#_Toc306010924}[]{#_Toc306010925}[]{#_Toc306010926}[]{#_Toc306010927}[]{#_Toc306010928}[]{#_Toc306010929}[]{#_Toc306010930}[]{#_Toc306010931}[]{#_Toc306010932}[]{#_Toc306010933}[]{#_Toc306010934}[]{#_Toc306010935}[]{#_Toc306010936}

**sFlow \-- sFlow调试命令 \-- debugging sflow counter-polling**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1536_97982_755440265}

[**[debugging sflow counter-polling]{lang="EN-US"}**]{#struct_0_x1536_97982_x549445267}

[**[undo debugging sflow counter-polling]{lang="EN-US"}**]{#struct_0_x1536_97982_1374532482}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1593854137}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1536_97982_1828349250}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x529642125}

[[network-admin]{lang="EN-US"}]{#struct_0_x1536_97982_x304485683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1536_97982_762329201}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1536_97982_940311374}

[[无]{style="font-family:宋体"}]{#struct_0_x1536_97982_x170341060}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1259179401}

[**[debugging sflow counter-polling]{lang="EN-US"}**]{#struct_0_x1536_97982_x1593788601}[命令用于打开]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样的调试信息开关。]{style="font-family:宋体"}**[undo debugging sflow counter-polling]{lang="EN-US"}**[命令用于关闭]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Counter]{lang="EN-US"}]{#struct_0_x1536_97982_2143761106}[采样的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging sflow counter-polling ]{lang="EN-US"}]{#struct_0_x1536_97982_118205393}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_994806158}[[字段]{style="font-family:黑体"}]{#struct_0_x1536_97982_133235416}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1536_97982_407847632}

[[sFlow poller sample data information]{lang="EN-US"}]{#struct_0_x1536_97982_x1846223832}

[[sFlow Poller]{lang="EN-US"}]{#struct_0_x1536_97982_2035295321}[数据项信息]{style="font-family:宋体"}

[[Summary info:]{lang="EN-US"}]{#struct_0_x1536_97982_x939343537}

[[概要信息]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593723065}

[[Ifindex = *Ifindex*]{lang="EN-US"}]{#struct_0_x1536_97982_x1751909558}

[[接口索引]{style="font-family:宋体"}]{#struct_0_x1536_97982_1669964429}

[[Iftype = *Iftype*]{lang="EN-US"}]{#struct_0_x1536_97982_1938105618}

[[接口类型]{style="font-family:宋体"}]{#struct_0_x1536_97982_257281526}

[[Direction = *direction*]{lang="EN-US"}]{#struct_0_x1536_97982_x342194968}

[[报文方向]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593657529}

[[IfStatus = *If_status*]{lang="EN-US"}]{#struct_0_x1536_97982_x1068305580}

[[接口状态]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1878649939}

[[IfSpeed = *if_speed*]{lang="EN-US"}]{#struct_0_x1536_97982_1714698336}

[[接口速率]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1315264071}

[[Bitmap = *bitmap*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593067705}

[[数据项]{style="font-family:宋体"}]{#struct_0_x1536_97982_x996854131}

[[IfTable info:]{lang="EN-US"}]{#struct_0_x1536_97982_471464214}

[[IfTable]{lang="EN-US"}]{#struct_0_x1536_97982_1820133301}[表信息]{style="font-family:宋体"}

[[LastChange = *last_change_time*]{lang="EN-US"}]{#struct_0_x1536_97982_1222807954}

[[接口最后一次修改时的系统启动时长为]{style="font-family:宋体"}*[last_change_time]{lang="EN-US"}*]{#struct_0_x1536_97982_x1593002169}

[[Mtu = *mtu*]{lang="EN-US"}]{#struct_0_x1536_97982_x543779843}

[[接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x1536_97982_1008610023}

[[Speed = *speed*]{lang="EN-US"}]{#struct_0_x1536_97982_854139814}

[[接口速率]{style="font-family:宋体"}]{#struct_0_x1536_97982_1468596891}

[[InOctets = *InOctets*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593591996}

[[入站包字节数]{style="font-family:宋体"}]{#struct_0_x1536_97982_1395739425}

[[InUcastPkts = *InUcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_1948335835}

[[入站的单播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1778784725}

[[InNUcastPkts = *InNUcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593526460}

[[入站的非单播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x2113817529}

[[InDiscards = *Discard number*]{lang="EN-US"}]{#struct_0_x1536_97982_872412628}

[[丢弃的入站包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_1812161625}

[[InErrors = *Errors number*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593460924}

[[有错误的入站包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_158777844}

[[InUnknownProtos = *InUnknownProtos*]{lang="EN-US"}]{#struct_0_x1536_97982_1987629620}

[[不支持的协议的入站包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_816793329}

[[OutOctets = *OutOctets*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593395388}

[[出站包字节数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1188875183}

[[OutUcastPkts = *OutUcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x2095744869}

[[出站的单播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x34429707}

[[OutNUcastPkts = *OutNUcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593854140}

[[出站的非单播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_1425392403}

[[OutDiscards = *Discard number*]{lang="EN-US"}]{#struct_0_x1536_97982_2114657593}

[[丢弃的出站包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1688375942}

[[OutErrors = *Errors number*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593788604}

[[有错误的出站包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_1740476579}

[[OutQLen = *Queen length*]{lang="EN-US"}]{#struct_0_x1536_97982_614631342}

[[出包队列长度]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593723068}

[[usOperStatus = *Status*]{lang="EN-US"}]{#struct_0_x1536_97982_1427312491}

[[接口的当前运行状态]{style="font-family:宋体"}]{#struct_0_x1536_97982_870260018}

[[PhysAddress = *mac Address*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593657532}

[[接口在协议子层的物理地址]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1827754931}

[[IfXTable info:]{lang="EN-US"}]{#struct_0_x1536_97982_803536841}

[[IfXTable]{lang="EN-US"}]{#struct_0_x1536_97982_x1394420772}[表信息]{style="font-family:宋体"}

[[HCInOctets = *HCInOctets*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593067708}

[[入站包字节数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1043908298}

[[HCInUcastPkts = *HCInUcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_1516782348}

[[入站单播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593002172}

[[HCInMulticastPkts = *HCInMulticastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_215800580}

[[入站多播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x2142776951}

[[HCInBroadcastPkts = *HCInBroadcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593591995}

[[入站广播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_1799023952}

[[HCOutOctets = *HCOutOctets*]{lang="EN-US"}]{#struct_0_x1536_97982_154729184}

[[出站包字节数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593526459}

[[HCOutUcastPkts = *HCOutUcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_258638858}

[[出站单播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_748537213}

[[HCOutMulticastPkts = *HCOutMulticastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593460923}

[[出站多播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_2081092145}

[[HCOutBroadcastPkts= *HCOutBroadcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x728202817}

[[出站广播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593395387}

[[InMulticastPkts = *InMulticastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x785590656}

[[入站的多播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593854139}

[[InBroadcastPkts = *InBroadcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x947588272}

[[入站的广播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_753972746}

[[OutMulticastPkts = *OutMulticastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593788603}

[[出站的多播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_980961692}

[[OutBroadcastPkts = *OutBroadcastPkts*]{lang="EN-US"}]{#struct_0_x1536_97982_x1800721788}

[[出站的广播包数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593723067}

[[HighSpeed = *HighSpeed*]{lang="EN-US"}]{#struct_0_x1536_97982_x589110144}

[[接口的当前带宽]{style="font-family:宋体"}]{#struct_0_x1536_97982_1353663586}

[[CounterDiscontinuityTime = *CounterDiscontinuityTime*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593657531}

[[计数中断时间]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1424470404}

[[PromiscuousMode = *PromiscuousMode*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593067707}

[[混杂模式设置状态]{style="font-family:宋体"}]{#struct_0_x1536_97982_165945283}

[[ConnectorPresent = *ConnectorPresent*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593002171}

[[是否有物理连接器]{style="font-family:宋体"}]{#struct_0_x1536_97982_x187483947}

[[Ethernet statistics:]{lang="EN-US"}]{#struct_0_x1536_97982_x168964013}

[[以太网链路统计信息]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593591998}

[[AlignmentErrors = *AlignmentErrors*]{lang="EN-US"}]{#struct_0_x1536_97982_x1736428457}

[[队列错误数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593526462}

[[FCSErrors = *FCSErrors*]{lang="EN-US"}]{#struct_0_x1536_97982_x951018115}

[[校验码错误帧数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x716663172}

[[SingleCollisionFrames = *SingleCollisionFrames*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593460926}

[[单个冲突帧数]{style="font-family:宋体"}]{#struct_0_x1536_97982_1321577258}

[[MultipleCollisionFrames = *MultipleCollisionFrames*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593395390}

[[多个冲突帧数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1545171079}

[[SQETestErrors = *SQETestErrors*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593854142}

[[SQE]{lang="EN-US"}]{#struct_0_x1536_97982_x1706775479}[测试错误数]{style="font-family:宋体"}

[[DeferredTransmissions = *DeferredTransmissions*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593788606}

[[超时帧数]{style="font-family:宋体"}]{#struct_0_x1536_97982_577677165}

[[LateCollisions = *LateCollisions*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593723070}

[[延迟冲突数]{style="font-family:宋体"}]{#struct_0_x1536_97982_1783477315}

[[ExcessiveCollisions = *ExcessiveCollisions*]{lang="EN-US"}]{#struct_0_x1536_97982_x719268673}

[[额外冲突数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593657534}

[[InternalMacTransmitErrors = *InternalMacTransmitErrors*]{lang="EN-US"}]{#struct_0_x1536_97982_x1021185877}

[[内部传送错误数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593067710}

[[CarrierSenseErrors = *CarrierSenseErrors*]{lang="EN-US"}]{#struct_0_x1536_97982_x1400073122}

[[载波侦听错误数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593002174}

[[FrameTooLongs = *FrameTooLongs*]{lang="EN-US"}]{#struct_0_x1536_97982_x590768474}

[[过长的帧数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593591997}

[[InternalMacReceiveErrors = *InternalMacReceiveErrors*]{lang="EN-US"}]{#struct_0_x1536_97982_x1333143930}

[[内部接收错误数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593526461}

[[SymbolErrors = *symbol_errors*]{lang="EN-US"}]{#struct_0_x1536_97982_615065826}

[[符号错误数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593460925}

[[DuplexStatus = *DuplexStatus*]{lang="EN-US"}]{#struct_0_x1536_97982_x1407306097}

[[双工状态]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593395389}

[[Run info:]{lang="EN-US"}]{#struct_0_x1536_97982_377208758}

[[运行信息]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593854141}

[[Sequence = *Sequence number*]{lang="EN-US"}]{#struct_0_x1536_97982_x1303490952}

[[序列号]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593788605}

[[Next polling time = *Next polling time*]{lang="EN-US"}]{#struct_0_x1536_97982_x1593723069}

[[下一次采样时刻]{style="font-family:宋体"}]{#struct_0_x1536_97982_x1593657533}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x261670990}

[[\# ]{lang="EN-US"}]{#struct_0_x1536_97982_x330554995}[在一台设备上启动了]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样调试开关，并配置了]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样。]{style="font-family:宋体"}

[[\<[Sysname]{.TerminalDisplayChar}\> debugging sflow counter-polling]{lang="EN-US"}]{#struct_0_x1536_97982_x1593002173}

[\<[Sysname]{.TerminalDisplayChar}\> system-view]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] sflow agent ip 1.1.1.1]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] sflow collector 1 ip 192.168.20.104]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow counter interval 2]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow counter collector 1]{lang="EN-US"}

[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/POLLER:]{lang="EN-US"}

[sFlow poller sample data information]{lang="EN-US"}

[Summary info:]{lang="EN-US"}

[Ifindex = 3]{lang="EN-US"}

[Iftype = 3]{lang="EN-US"}

[Direction = 1]{lang="EN-US"}

[IfStatus = 1]{lang="EN-US"}

[IfSpeed = 100]{lang="EN-US"}

[Bitmap = 3]{lang="EN-US"}

[IfTable info:]{lang="EN-US"}

[LastChange = 32900]{lang="EN-US"}

[Mtu = 1500]{lang="EN-US"}

[Speed = 100]{lang="EN-US"}

[InOctets = 30]{lang="EN-US"}

[InUcastPkts = 50]{lang="EN-US"}

[InNUcastPkts = 39]{lang="EN-US"}

[InDiscards = 24]{lang="EN-US"}

[InErrors = 3]{lang="EN-US"}

[InUnknownProtos = 99]{lang="EN-US"}

[OutOctets = 10]{lang="EN-US"}

[OutUcastPkts = 0]{lang="EN-US"}

[OutNUcastPkts = 0]{lang="EN-US"}

[OutDiscards = 23]{lang="EN-US"}

[OutErrors = 1]{lang="EN-US"}

[OutQLen = 100]{lang="EN-US"}

[OperStatus = 1]{lang="EN-US"}

[PhysAddress = 00-e4-67-90-23-f5]{lang="EN-US"}

[IfXTable info:]{lang="EN-US"}

[HCInOctets = 35]{lang="EN-US"}

[HCInUcastPkts = 12]{lang="EN-US"}

[HCInMulticastPkts = 10]{lang="EN-US"}

[HCInBroadcastPkts = 0]{lang="EN-US"}

[HCOutOctets = 19]{lang="EN-US"}

[HCOutUcastPkts = 0]{lang="EN-US"}

[HCOutMulticastPkts = 0]{lang="EN-US"}

[HCOutBroadcastPkts = 0]{lang="EN-US"}

[InMulticastPkts = 0]{lang="EN-US"}

[InBroadcastPkts = 0]{lang="EN-US"}

[OutMulticastPkts = 0]{lang="EN-US"}

[OutBroadcastPkts = 0]{lang="EN-US"}

[HighSpeed = 1000]{lang="EN-US"}

[CounterDiscontinuityTime = 29808]{lang="EN-US"}

[PromiscuousMode = 1]{lang="EN-US"}

[ConnectorPresent = 1]{lang="EN-US"}

[Ethernet statistics:]{lang="EN-US"}

[Index = 3]{lang="EN-US"}

[AlignmentErrors = 0]{lang="EN-US"}

[FCSErrors = 0]{lang="EN-US"}

[SingleCollisionFrames = 0]{lang="EN-US"}

[MultipleCollisionFrames = 0]{lang="EN-US"}

[SQETestErrors = 0]{lang="EN-US"}

[DeferredTransmissions = 0]{lang="EN-US"}

[LateCollisions = 0]{lang="EN-US"}

[ExcessiveCollisions = 0]{lang="EN-US"}

[InternalMacTransmitErrors = 0]{lang="EN-US"}

[CarrierSenseErrors = 0]{lang="EN-US"}

[FrameTooLongs = 0]{lang="EN-US"}

[InternalMacReceiveErrors = 0]{lang="EN-US"}

[SymbolErrors = 0]{lang="EN-US"}

[DuplexStatus = 0]{lang="EN-US"}

[Run info:]{lang="EN-US"}

[Sequence = 34]{lang="EN-US"}

[Next polling time = 35009]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x1350283361}*[封装了一个]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样的数据项]{style="font-family:宋体"}*

::: {#-1963333354 .myid}
[]{#_Toc404797330}[]{#struct_0_x1536_97982_x27508053}[]{#_Toc306018992}

**sFlow \-- sFlow调试命令 \-- debugging sflow driver**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x506068580}

[**[debugging sflow driver]{lang="EN-US"}**]{#struct_0_x1536_97982_x1059809971}

[**[undo debugging sflow driver]{lang="EN-US"}**]{#struct_0_x1536_97982_x1729198025}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1746530189}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1536_97982_1917380825}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x116456118}

[[network-admin]{lang="EN-US"}]{#struct_0_x1536_97982_544062418}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1536_97982_x1389993692}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x27442517}

[[无]{style="font-family:宋体"}]{#struct_0_x1536_97982_x2054070187}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1901369573}

[**[debugging sflow driver]{lang="EN-US"}**]{#struct_0_x1536_97982_501890431}[命令用来打开]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[驱动的调试信息开关。]{style="font-family:宋体"}**[undo debugging sflow driver]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[驱动的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_x1536_97982_2143733127}[驱动的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging sflow driver]{lang="EN-US"}]{#struct_0_x1536_97982_x1042627939}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1011236544}[[字段]{style="font-family:黑体"}]{#struct_0_x1536_97982_1911471663}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1283420156}

[*[commad_type direction]{lang="EN-US"}*[ on interface *interface_name(ifIndex),* parameter = *parameter,* result *= result*]{lang="EN-US"}]{#struct_0_x1536_97982_x27376981}

[*[interface_name]{lang="EN-US"}*]{#struct_0_x1536_97982_493611312}[接口]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样]{style="font-family:宋体"}*[commad_type]{lang="EN-US"}*[下驱动，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*[，下驱动参数为]{style="font-family:宋体"}*[parameter]{lang="EN-US"}*[，下驱动结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1956219820}

[[\# ]{lang="EN-US"}]{#struct_0_x1536_97982_x104436736}[在一台设备上启动了]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[驱动调试开关，配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样的采样频率。]{style="font-family:宋体"}

[[\<[Sysname]{.TerminalDisplayChar}\> debugging sflow driver]{lang="EN-US"}]{#struct_0_x1536_97982_x632759655}

[\<[Sysname]{.TerminalDisplayChar}\> system-view]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow sampling-rate 1000]{lang="EN-US"}

[%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/DRIVER:]{lang="EN-US"}

[Enable the sampling inbound on interface GigabitEthernet1/0/1(1), parameter = 0, result = 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_1862669045}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，入方向开启采样功能，参数为]{style="font-family:宋体"}[0]{lang="EN-US"}[，下驱动结果为]{style="font-family:宋体"}[0]{lang="EN-US"}[（成功）]{style="font-family:宋体"}*

[[%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/DRIVER:]{lang="EN-US"}]{#struct_0_x1536_97982_x27311445}

[Enable the sampling outbound on interface GigabitEthernet1/0/1(1), parameter = 0, result = 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x385100699}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，出方向开启采样功能，参数为]{style="font-family:宋体"}[0]{lang="EN-US"}[，下驱动结果为]{style="font-family:宋体"}[0]{lang="EN-US"}[（成功）]{style="font-family:宋体"}*

[[%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/DRIVER:]{lang="EN-US"}]{#struct_0_x1536_97982_x172604320}

[Set the sampling rate inbound on interface GigabitEthernet1/0/1(1), parameter = 1000, ret = 0.  ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_721147179}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，入方向]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样频率下驱动，参数为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，下驱动结果为]{style="font-family:宋体"}[0]{lang="EN-US"}[（成功）]{style="font-family:宋体"}*

[[%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/DRIVER:]{lang="EN-US"}]{#struct_0_x1536_97982_239564311}

[Set the sampling rate outbound on interface GigabitEthernet1/0/1(1), parameter = 1000, result = 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x1945047394}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，出方向]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样频率下驱动，参数为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，下驱动结果为]{style="font-family:宋体"}[0]{lang="EN-US"}[（成功）]{style="font-family:宋体"}*

::: {#1038339566 .myid}
[]{#_Toc404797331}[]{#struct_0_x1536_97982_x1502640978}[]{#_Toc306018993}

**sFlow \-- sFlow调试命令 \-- debugging sflow flow-sampling**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x836482853}

[**[debugging sflow flow-sampling]{lang="EN-US"}**]{#struct_0_x1536_97982_1425525708}

[**[undo debugging sflow flow-sampling]{lang="EN-US"}**]{#struct_0_x1536_97982_x27770197}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1536_97982_2109771270}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1536_97982_235768810}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x574177878}

[[network-admin]{lang="EN-US"}]{#struct_0_x1536_97982_x811906817}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1536_97982_1671478329}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x2034724948}

[[无]{style="font-family:宋体"}]{#struct_0_x1536_97982_132199292}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x27704661}

[**[debugging sflow flow-sampling]{lang="EN-US"}**]{#struct_0_x1536_97982_x609239748}[命令用于打开]{style="font-family:
宋体"}[Flow]{lang="EN-US"}[采样的调试信息开关。]{style="font-family:宋体"}**[undo debugging flow-sampling]{lang="EN-US"}**[命令用于关闭]{style="font-family:
宋体"}[Flow]{lang="EN-US"}[采样的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_x1536_97982_1577650734}[采样的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging sflow flow-sampling]{lang="EN-US"}]{#struct_0_x1536_97982_1815491779}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1014262980}[[字段]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1323790333}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1536_97982_1474213458}

[[sFlow poller sample data information]{lang="EN-US"}]{#struct_0_x1536_97982_x642340377}

[[Poller]{lang="EN-US"}]{#struct_0_x1536_97982_x27639125}[数据项信息]{style="font-family:宋体"}

[[ifIndex = *ifIndex*]{lang="EN-US"}]{#struct_0_x1536_97982_x1792701048}

[[接口索引]{style="font-family:宋体"}]{#struct_0_x1536_97982_686108118}

[[HeaderLen = *length*]{lang="EN-US"}]{#struct_0_x1536_97982_297708266}

[[原始报文头长度]{style="font-family:宋体"}]{#struct_0_x1536_97982_1820791234}

[[EthType = *type*]{lang="EN-US"}]{#struct_0_x1536_97982_2037622813}

[[以太帧类型]{style="font-family:宋体"}]{#struct_0_x1536_97982_x27573589}

[[EthTotalLen = *length*]{lang="EN-US"}]{#struct_0_x1536_97982_x840933252}

[[以太帧总长度]{style="font-family:宋体"}]{#struct_0_x1536_97982_570989845}

[[DstMac = *mac_address*]{lang="EN-US"}]{#struct_0_x1536_97982_605533778}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1536_97982_x1605839180}[地址]{style="font-family:宋体"}

[[SrcMac = *mac_address*]{lang="EN-US"}]{#struct_0_x1536_97982_x26983765}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1536_97982_x2101390848}[地址]{style="font-family:宋体"}

[[L3Protocol = *protocol*]{lang="EN-US"}]{#struct_0_x1536_97982_1274634344}

[[IP]{lang="EN-US"}]{#struct_0_x1536_97982_293340973}[头协议字段表示的协议类型]{style="font-family:宋体"}

[[TcpFlag = *flag*]{lang="EN-US"}]{#struct_0_x1536_97982_1782790494}

[[TCP Flag]{lang="EN-US"}]{#struct_0_x1536_97982_x26918229}[标记字段]{style="font-family:宋体"}

[[IPTos = *tos*]{lang="EN-US"}]{#struct_0_x1536_97982_x2120021520}

[[IP]{lang="EN-US"}]{#struct_0_x1536_97982_162502223}[头]{style="font-family:宋体"}[tos]{lang="EN-US"}[字段]{style="font-family:宋体"}

[[SrcPort = *port*]{lang="EN-US"}]{#struct_0_x1536_97982_1609899288}

[[源端口号]{style="font-family:宋体"}]{#struct_0_x1536_97982_366492764}

[[DstPort = *port*]{lang="EN-US"}]{#struct_0_x1536_97982_x27508052}

[[目的端口号]{style="font-family:宋体"}]{#struct_0_x1536_97982_x506068579}

[[vrfIndex = *vrfIndex*]{lang="EN-US"}]{#struct_0_x1536_97982_x1060268716}

[[VPN]{lang="EN-US"}]{#struct_0_x1536_97982_x1220026913}[索引]{style="font-family:宋体"}

[[SrcIP = *address*]{lang="EN-US"}]{#struct_0_x1536_97982_x27442516}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1536_97982_x2054070186}[地址]{style="font-family:宋体"}

[[DstIP = *address*]{lang="EN-US"}]{#struct_0_x1536_97982_335285632}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1536_97982_x654942333}[地址]{style="font-family:宋体"}

[[NextHop = *address*]{lang="EN-US"}]{#struct_0_x1536_97982_x27376980}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_x1536_97982_493611311}

[[SrcMaskLen = *length*]{lang="EN-US"}]{#struct_0_x1536_97982_x1956219823}

[[源地址掩码长度]{style="font-family:宋体"}]{#struct_0_x1536_97982_1461647205}

[[DstMaskLen = *length*]{lang="EN-US"}]{#struct_0_x1536_97982_x27311444}

[[目的地址掩码长度]{style="font-family:宋体"}]{#struct_0_x1536_97982_x385100700}

[[IPPacketLen = *length*]{lang="EN-US"}]{#struct_0_x1536_97982_1784169575}

[[IP]{lang="EN-US"}]{#struct_0_x1536_97982_x1227077862}[包长度]{style="font-family:宋体"}

[[Bitmap = *bitmap*]{lang="EN-US"}]{#struct_0_x1536_97982_x27770196}

[[数据项]{style="font-family:宋体"}[Bitmap]{lang="EN-US"}]{#struct_0_x1536_97982_2109771269}

[[sFlow flow sample additional information:]{lang="EN-US"}]{#struct_0_x1536_97982_236227563}

[[sFlow Flow]{lang="EN-US"}]{#struct_0_x1536_97982_x1100968433}[采样驱动上传的]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[附加信息]{style="font-family:宋体"}

[[Direction = *direction*]{lang="EN-US"}]{#struct_0_x1536_97982_x27704660}

[[样本经过设备的方向]{style="font-family:宋体"}]{#struct_0_x1536_97982_x609239747}

[[Input interface = *internet_name*]{lang="EN-US"}]{#struct_0_x1536_97982_1578633774}

[[入接口]{style="font-family:宋体"}]{#struct_0_x1536_97982_x27639124}

[[Output interface = *internet_name*]{lang="EN-US"}]{#struct_0_x1536_97982_x1792701049}

[[出接口]{style="font-family:宋体"}]{#struct_0_x1536_97982_x879975823}

[[Input TCI = *TCI*]{lang="EN-US"}]{#struct_0_x1536_97982_x581082957}

[[入接口]{style="font-family:宋体"}[TCI]{lang="EN-US"}]{#struct_0_x1536_97982_x27573588}[信息]{style="font-family:宋体"}

[[Output TCI = *TCI*]{lang="EN-US"}]{#struct_0_x1536_97982_x840933253}

[[出接口]{style="font-family:宋体"}[TCI]{lang="EN-US"}]{#struct_0_x1536_97982_571055381}[信息]{style="font-family:宋体"}

[[Sample pool = *number*]{lang="EN-US"}]{#struct_0_x1536_97982_x26983764}

[[样本池个数]{style="font-family:宋体"}]{#struct_0_x1536_97982_x2101390847}

[[Forward type = *type*]{lang="EN-US"}]{#struct_0_x1536_97982_2034149231}

[[转发类型]{style="font-family:宋体"}]{#struct_0_x1536_97982_x26918228}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x2120021521}

[[\# ]{lang="EN-US"}]{#struct_0_x1536_97982_x1403581718}[在一台设备上启动了]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样调试开关，配置了]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样实例并能够正确采样。]{style="font-family:宋体"}

[[\<[Sysname]{.TerminalDisplayChar}\> debugging sflow flow-sampling]{lang="EN-US"}]{#struct_0_x1536_97982_x27508055}

[\<[Sysname]{.TerminalDisplayChar}\> system-view]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] sflow agent ip 1.1.1.1]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] sflow collector 1 ip 192.168.20.104]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow sampling-rate 1000]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow flow collector 1]{lang="EN-US"}

[%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/SAMPLER:]{lang="EN-US"}

[sFlow flow sample additional information:]{lang="EN-US"}

[Direction = inbound]{lang="EN-US"}

[Input interface = GigabitEthernet1/0/3]{lang="EN-US"}

[Output interface = GigabitEthernet1/0/5]{lang="EN-US"}

[Input TCI = 3]{lang="EN-US"}

[Output TCI = 3]{lang="EN-US"}

[Sample pool = 5000]{lang="EN-US"}

[Forward type = L3 forward ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x506068586}*[驱动上传了一个]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[，其中包方向为]{style="font-family:宋体"}[inbound]{lang="EN-US"}[，入接口为]{style="font-family:宋体"}[GigabitEthernet 1/0/3]{lang="EN-US"}[，出接口为]{style="font-family:宋体"}[GigabitEthernet 1/0/5]{lang="EN-US"}[，入接口]{style="font-family:宋体"}[TCI]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[，出接口]{style="font-family:宋体"}[TCI]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[，样本池为]{style="font-family:宋体"}[5000]{lang="EN-US"}[，转发类型为]{style="font-family:宋体"}[L3 forward]{lang="EN-US"}*

[[%Jun 13 09:50:53 672 2011 Sysname SFLOW/7/SAMPLER:]{lang="EN-US"}]{#struct_0_x1536_97982_x27442519}

[sFlow poller sample data information]{lang="EN-US"}

[ifIndex = 2]{lang="EN-US"}

[HeaderLen = 50]{lang="EN-US"}

[EthType = 2048]{lang="EN-US"}

[EthTotalLen = 1600]{lang="EN-US"}

[DstMac = 00-e0-fc-6f-84-a6]{lang="EN-US"}

[SrcMac = 00-46-a5-90-e3-43]{lang="EN-US"}

[L3Protocol = 6]{lang="EN-US"}

[TcpFlag = 0]{lang="EN-US"}

[IPTos = 0]{lang="EN-US"}

[SrcPort = 6343]{lang="EN-US"}

[DstPort = 6343]{lang="EN-US"}

[vrfIndex = 4]{lang="EN-US"}

[SrcIP = 10.55.98.114]{lang="EN-US"}

[DstIP = 10.55.99.55]{lang="EN-US"}

[NextHop = 10.55.98.1]{lang="EN-US"}

[SrcMaskLen = 24]{lang="EN-US"}

[DstMaskLen = 24]{lang="EN-US"}

[IPPacketLen = 1500]{lang="EN-US"}

[Bitmap = 48]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x2054070185}*[封装了一个]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样数据项，其中采样接口接口索引为]{style="font-family:宋体"}[2]{lang="EN-US"}[，原始头长度为]{style="font-family:宋体"}[50]{lang="EN-US"}[，以太帧类型为]{style="font-family:宋体"}[2048]{lang="EN-US"}[，以太帧总长度为]{style="font-family:宋体"}[1600]{lang="EN-US"}[，源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00-46-a5-90-e3-43]{lang="EN-US"}[，目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00-e0-fc-6f-84-a6]{lang="EN-US"}[，三层协议字段类型为]{style="font-family:宋体"}[6]{lang="EN-US"}[，]{style="font-family:宋体"}[TCP Flag]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[IP TOS]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，源端口为]{style="font-family:宋体"}[6343]{lang="EN-US"}[，目的端口为]{style="font-family:宋体"}[6343]{lang="EN-US"}[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引为]{style="font-family:宋体"}[4]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.55.98.114]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[10.55.98.117]{lang="EN-US"}[，下一跳为]{style="font-family:宋体"}[10.55.98.55.1]{lang="EN-US"}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[包长度为]{style="font-family:宋体"}[1500]{lang="EN-US"}[，]{style="font-family:宋体"}[bitmap]{lang="EN-US"}[为]{style="font-family:宋体"}[48]{lang="EN-US"}*

::: {#932935188 .myid}
[]{#_Toc404797332}[]{#struct_0_x1536_97982_738570159}[]{#_Toc306018994}

**sFlow \-- sFlow调试命令 \-- debugging sflow synchronization**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x167390789}

[**[debugging sflow synchronization]{lang="EN-US"}**]{#struct_0_x1536_97982_771236075}

[**[undo debugging sflow synchronization]{lang="EN-US"}**]{#struct_0_x1536_97982_x1966478528}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1458205335}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1536_97982_1852733478}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1536_97982_598263526}

[[network-admin]{lang="EN-US"}]{#struct_0_x1536_97982_x27376983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1536_97982_493611314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1536_97982_x1956219826}

[[无]{style="font-family:宋体"}]{#struct_0_x1536_97982_702132318}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1536_97982_1501788114}

[**[debugging sflow synchronization]{lang="EN-US"}**]{#struct_0_x1536_97982_2031994975}[命令用于打开]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[同步的调试信息开关。]{style="font-family:宋体"}**[undo debugging sflow synchronization]{lang="EN-US"}**[命令用于关闭]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[同步的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_x1536_97982_x657967906}[同步的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging sflow synchronization]{lang="EN-US"}]{#struct_0_x1536_97982_x1365523792}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1037273652}[[字段]{style="font-family:黑体"}]{#struct_0_x1536_97982_x27311447}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1536_97982_x385100701}

[[Start smoothing process on slot *slot_id*]{lang="EN-US"}]{#struct_0_x1536_97982_1784235111}[（集中式设备、分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Start smoothing process on chassis *chassis_id* slot *slot_id*]{lang="EN-US"}]{#struct_0_x1536_97982_698793659}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[开始在板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*]{#struct_0_x1536_97982_1946567617}[上进行平滑处理（集中式设备、分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[开始在在成员设备]{style="font-family:宋体"}*[chassis_id]{lang="EN-US"}*]{#struct_0_x1536_97982_362544173}[的单板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*[上进行平滑处理（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Stop smoothing process on slot *slot_id*]{lang="EN-US"}]{#struct_0_x1536_97982_1606328443}[（集中式设备、分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Stop smoothing process on chassis *chassis_id* slot *slot_id*]{lang="EN-US"}]{#struct_0_x1536_97982_x27770199}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[结束在板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*]{#struct_0_x1536_97982_2109771280}[上的平滑处理（集中式设备、分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[结束在在成员设备]{style="font-family:宋体"}*[chassis_id]{lang="EN-US"}*]{#struct_0_x1536_97982_235768797}[的单板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*[上的平滑处理（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Succeeded in sending a smooth message to slot *slot_id*, length *length*, errcode *code*]{lang="EN-US"}]{#struct_0_x1536_97982_x1323374440}[（集中式设备、分布式设备－独立运行模式、集中式]{style="font-family:
  宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Succeeded in sending a smooth message to chassis *chassis_id* slot *slot_id,* length *length*, errcode *code*]{lang="EN-US"}]{#struct_0_x1536_97982_x1267743658}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[向]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*]{#struct_0_x1536_97982_x27704663}[发送一个平滑消息，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，返回的错误码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[（集中式设备、分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[向成员设备]{style="font-family:宋体"}*[chassis_id]{lang="EN-US"}*]{#struct_0_x1536_97982_x609239746}[上的单板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*[发送一个平滑消息，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，返回的错误码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Succeeded in synchronizing the configuration on interface *interface_name(ifIndex).*]{lang="EN-US"}]{#struct_0_x1536_97982_1578568238}

[[向]{style="font-family:宋体"}*[interface_name]{lang="EN-US"}*]{#struct_0_x1536_97982_91590540}[接口所在板同步该接口数据成功，该接口的接口索引为]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*

[[Failed to synchronize the configuration on interface *Interfacen_name(ifIndex).*]{lang="EN-US"}]{#struct_0_x1536_97982_x355449904}

[[向]{style="font-family:宋体"}*[interface_name]{lang="EN-US"}*]{#struct_0_x1536_97982_x27639127}[接口所在板同步该接口数据失败，该接口的接口索引为]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*

[[Succeeded in synchronizing the message to slot *slot_id,* socket fd *fd,* length *length,* errcode *errcode*]{lang="EN-US"}]{#struct_0_x1536_97982_x1792701046}[（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Succeeded in synchronizing the message to chassis *chassis_id* slot *slot_id,* socket fd *fd,* length *length,* errcode *errcode*]{lang="EN-US"}]{#struct_0_x1536_97982_x120460936}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[同步数据到]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*]{#struct_0_x1536_97982_x232193703}[成功，]{style="font-family:宋体"}[socket ]{lang="EN-US"}[文件描述符为]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，数据长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，返回的错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[同步数据到成员设备]{style="font-family:宋体"}*[chassis_id]{lang="EN-US"}*]{#struct_0_x1536_97982_972052139}[上的单板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*[成功，]{style="font-family:宋体"}[socket ]{lang="EN-US"}[文件描述符为]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，数据长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，返回的错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Failed to synchronize the message to slot *slot_id,* socket fd *fd,* length *length,* errcode *errcode*]{lang="EN-US"}]{#struct_0_x1536_97982_x27573591}[（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[Failed to synchronize the message to chassis *chassis_id* slot *slot_id,* socket fd *fd,* length *length,* errcode *errcode*]{lang="EN-US"}]{#struct_0_x1536_97982_1115381876}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[同步数据到]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*]{#struct_0_x1536_97982_1887867052}[失败，]{style="font-family:宋体"}[socket ]{lang="EN-US"}[文件描述符为]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，数据长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，返回的错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[同步数据到成员设备]{style="font-family:宋体"}*[chassis_id]{lang="EN-US"}*]{#struct_0_x1536_97982_x617425858}[上的单板]{style="font-family:宋体"}*[slot_id]{lang="EN-US"}*[失败，]{style="font-family:宋体"}[socket ]{lang="EN-US"}[文件描述符为]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，数据长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，返回的错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Succeeded in synchronizing *message_type* message to kernel*,* length *length,* errcode *errcode*]{lang="EN-US"}]{#struct_0_x1536_97982_x26983767}

[[用户态成功同步消息到内核，消息类型为]{style="font-family:宋体"}*[message_type]{lang="EN-US"}*]{#struct_0_x1536_97982_x2101390846}[，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，返回的错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*

[[Failed to synchronize *message_type* message to kernel*,* length *length,* errcode *errcode*]{lang="EN-US"}]{#struct_0_x1536_97982_468065290}

[[用户态未成功同步消息到内核，消息类型为]{style="font-family:宋体"}*[message_type]{lang="EN-US"}*]{#struct_0_x1536_97982_1234729470}[，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，返回的错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*

[[Received smooth message, length *length*.]{lang="EN-US"}]{#struct_0_x1536_97982_x734640898}

[[用户态收到平滑消息，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x1536_97982_x26918231}

[[Received *message_type* configuration message*,* length *length*]{lang="EN-US"}]{#struct_0_x1536_97982_x163706376}

[[用户态收到配置消息，消息类型为]{style="font-family:宋体"}*[message_type]{lang="EN-US"}*]{#struct_0_x1536_97982_217111816}[，消息长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1536_97982_2080539463}

[[\# ]{lang="EN-US"}]{#struct_0_x1536_97982_x684639527}[在一台设备上启动]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[同步的调试信息开关，进行如下配置和操作：配置一全局配置；配置接口板上的接口的采样实例；拔出某一接口板然后再插入。]{style="font-family:宋体"}

[[\<[Sysname]{.TerminalDisplayChar}\> debugging sflow synchronization]{lang="EN-US"}]{#struct_0_x1536_97982_x27508054}

[\<[Sysname]{.TerminalDisplayChar}\> system-view]{lang="EN-US"}

[\[[Sysname]{.TerminalDisplayChar}\] sflow agent ip 192.168.20.104  ]{lang="EN-US"}

[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ SYNC_UNICAST:]{lang="EN-US"}

[Succeeded in synchronizing the message to slot 2, length 40, errcode 0x00.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x506068585}*[成功同步配置数据到槽号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的接口板，消息长度为]{style="font-family:宋体"}[40]{lang="EN-US"}[，错误码为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[（成功）（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}*

[[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ SYNC_KERNEL:]{lang="EN-US"}]{#struct_0_x1536_97982_x1060006579}

[Succeeded in synchronizing configuration message to kernel, length 40, errcode 0x%00.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_1075325880}*[配置数据下内核成功，消息长度为]{style="font-family:宋体"}[40]{lang="EN-US"}[，错误码为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[（成功）]{style="font-family:宋体"}*

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1536_97982_x705850637}

[\[[Sysname]{.TerminalDisplayChar}-GigabitEthernet1/0/1\] sflow counter interval 2   ]{lang="EN-US"}

[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ SYNC_IFCFG:]{lang="EN-US"}

[Succeeded in synchronizing the configuration on interface GigabitEthernet1/0/1(4).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_1269756392}*[成功同步接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1(4)]{lang="EN-US"}[的数据到接口板（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[-IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}*

[[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ START_SMOOTH:]{lang="EN-US"}]{#struct_0_x1536_97982_x27442518}

[Start smoothing process with slot 2. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x2054070184}*[接口板拔出再插入，开始与槽号为]{style="font-family:宋体"}[2]{lang="EN-US"}[接口板进行平滑处理]{style="font-family:宋体"}*

[[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ SEND_SMTHMSG:]{lang="EN-US"}]{#struct_0_x1536_97982_x827513782}

[Succeeded in sending a smooth message to slot 2, length 90, errcode 0x00000000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_1667522322}*[发送平滑数据到槽号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的接口板，消息长度为]{style="font-family:宋体"}[90]{lang="EN-US"}*

[[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ STOP_SMOOTH:]{lang="EN-US"}]{#struct_0_x1536_97982_x1787282336}

[Stop smoothing process with slot 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_1055763048}*[结束与槽号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的接口板的平滑处理]{style="font-family:宋体"}*

[[%Jun 13 09:59:53 672 2011 Sysname SFLOW/7/ RCV_MSG:]{lang="EN-US"}]{#struct_0_x1536_97982_1904264931}

[Received smooth message, length 90.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1536_97982_x888539499}*[收到平滑消息，消息长度为]{style="font-family:宋体"}[90]{lang="EN-US"}[（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
