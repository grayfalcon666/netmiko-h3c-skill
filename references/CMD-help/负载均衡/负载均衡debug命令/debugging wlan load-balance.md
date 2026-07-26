::: {#541526213 .myid}
[]{#_Toc404795188}[]{#struct_0_15944_11499_226252440}[]{#_Toc398538320}[]{#_Toc392686782}

**负载均衡 \-- 负载均衡debug命令 \-- debugging wlan load-balance**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15944_11499_294722010}

[**[debugging wlan load-balance]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **timer** }]{lang="EN-US"}]{#struct_0_15944_11499_x1568262381}

[**[undo debugging wlan load-balance]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **timer** }]{lang="EN-US"}]{#struct_0_15944_11499_x430074563}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15944_11499_x558690495}

[[用户视图]{style="font-family:宋体;color:black"}]{#struct_0_15944_11499_313455315}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15944_11499_1560576406}

[[network-admin]{lang="EN-US"}]{#struct_0_15944_11499_1748959794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15944_11499_x378053592}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15944_11499_970487341}

[**[all]{lang="EN-US"}**]{#struct_0_15944_11499_1664601567}[：表示]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_15944_11499_251971614}[：表示]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_15944_11499_1267524030}[：表示]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡事件调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_15944_11499_x1912855148}[：表示]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15944_11499_x1222367268}

[**[debugging wlan load-balance]{lang="EN-US"}**]{#struct_0_15944_11499_x90422905}[命令用来打开]{style="font-family:
宋体"}[WLAN]{lang="EN-US"}[负载均衡调试信息开关。]{style="font-family:宋体"}

[**[undo debugging wlan load-balance]{lang="EN-US"}**]{#struct_0_15944_11499_x926610898}[命令用来关闭]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[WLAN]{lang="EN-US"}]{#struct_0_15944_11499_x1265565279}[负载均衡调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#_Ref203361573}[[表1-1 ]{lang="EN-US"}[debugging wlan load-balance error]{lang="EN-US"}]{#struct_0_15944_11499_749349696}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_111143508}[[字段]{style="font-family:黑体"}]{#struct_0_15944_11499_1355556723}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15944_11499_777939146}

[[Failed to get WLB radio information.]{lang="EN-US"}]{#struct_0_15944_11499_x2022594934}

[[获取]{style="font-family:宋体"}[WLB]{lang="EN-US"}]{#struct_0_15944_11499_x288540145}[模块]{style="font-family:宋体"}[radio]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to save WLB global configuration to DBM.]{lang="EN-US"}]{#struct_0_15944_11499_182875853}

[[将]{style="font-family:宋体"}[WLB]{lang="EN-US"}]{#struct_0_15944_11499_x1298999206}[模块全局配置数据保存到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to save WLAN load balancing group configuration to DBM.]{lang="EN-US"}]{#struct_0_15944_11499_678904996}

[[将]{style="font-family:宋体"}[WLB]{lang="EN-US"}]{#struct_0_15944_11499_812788145}[模块无线负载均衡组配置保存到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[APID: *apid* ]{lang="EN-US"}]{#struct_0_15944_11499_x1801403631}

[[AP ID]{lang="EN-US"}]{#struct_0_15944_11499_x319969257}[信息]{style="font-family:宋体"}

[[RADIOID: *radioid*]{lang="EN-US"}]{#struct_0_15944_11499_605619004}

[[Radio ID]{lang="EN-US"}]{#struct_0_15944_11499_978913071}[信息]{style="font-family:宋体"}

[[MAC: *mac-address*]{lang="EN-US"}]{#struct_0_15944_11499_x1383208088}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_846991531}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] Failed to reject the station when loads were not balanced.]{lang="EN-US"}]{#struct_0_15944_11499_x690244222}

[[负载不均衡时，拒绝]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_541587436}[连接失败]{style="font-family:宋体"}

[[Failed to change the load balancing mode from session mode to traffic or bandwidth mode. ]{lang="EN-US"}]{#struct_0_15944_11499_x2129738461}

[[无线负载均衡模式由会话模式改变为流量模式或者带宽模式初始化失败]{style="font-family:宋体"}]{#struct_0_15944_11499_1623540163}

[[Failed to enable WLB: Configuration thread initialization failure.]{lang="EN-US"}]{#struct_0_15944_11499_1760834362}

[[无线负载均衡开启时配置线程初始化失败]{style="font-family:宋体"}]{#struct_0_15944_11499_1345675267}

[[Failed to enable WLB: Service thread initialization failure.]{lang="EN-US"}]{#struct_0_15944_11499_640869821}

[[无线负载均衡开启时业务线程初始化失败]{style="font-family:宋体"}]{#struct_0_15944_11499_526101016}

[[Failed to update probe mask in WLB.]{lang="EN-US"}]{#struct_0_15944_11499_1204175558}

[[更新无线负载均衡]{style="font-family:宋体"}[probe mask]{lang="EN-US"}]{#struct_0_15944_11499_x591631657}[失败]{style="font-family:宋体"}

[[Global neighbor station hash table is empty.]{lang="EN-US"}]{#struct_0_15944_11499_487764432}

[[全局邻居]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_1593439032}[的哈希表为空]{style="font-family:宋体"}

[[\[MAC*: mac-address*\] Failed to identify whether valid neighbor radio existed for the station.]{lang="EN-US"}]{#struct_0_15944_11499_781991608}

[[检查是否存在有效的邻居]{style="font-family:宋体"}[radio]{lang="EN-US"}]{#struct_0_15944_11499_x220408674}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_15944_11499_x1761040843}[[表1-2 ]{lang="EN-US"}[debugging wlan load-balance event]{lang="EN-US"}]{#_Ref206212114}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_106129040}[[描述]{style="font-family:黑体"}]{#struct_0_15944_11499_x1161652729}

[[字段]{style="font-family:黑体"}]{#struct_0_15944_11499_x893507147}

[[Failed to add neighbor station to hash table: Not enough memory space. ]{lang="EN-US"}]{#struct_0_15944_11499_955292325}

[[内存不足，创建邻居]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_753198643}[哈希表失败]{style="font-family:宋体"}

[[APID: *apid* ]{lang="EN-US"}]{#struct_0_15944_11499_x1182985404}

[[AP]{lang="EN-US"}]{#struct_0_15944_11499_x79555596}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[RADIOID: *radioid*]{lang="EN-US"}]{#struct_0_15944_11499_x290946084}

[[Radio]{lang="EN-US"}]{#struct_0_15944_11499_28905416}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[MAC: *mac-address*]{lang="EN-US"}]{#struct_0_15944_11499_x950676489}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_520632113}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[\[MAC: *mac-address* \] The station already existed in global neighbor station hash table.]{lang="EN-US"}]{#struct_0_15944_11499_888899495}

[[邻居]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_x1786492615}[哈希表中已经存在]{style="font-family:宋体"}[station]{lang="EN-US"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The radio was added to neighbor radio list.]{lang="EN-US"}]{#struct_0_15944_11499_498208850}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_x494551657}[被添加到邻居]{style="font-family:宋体"}[radio]{lang="EN-US"}[链表中]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The radio was updated to neighbor radio list.]{lang="EN-US"}]{#struct_0_15944_11499_1222816112}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_470960545}[被更新到邻居]{style="font-family:宋体"}[radio]{lang="EN-US"}[链表]{style="font-family:宋体"}

[[\[MAC: *mac-address*\] Created global neighbor station node.]{lang="EN-US"}]{#struct_0_15944_11499_993679030}

[[创建全局邻居]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_9515714}[节点]{style="font-family:宋体"}

[[\[MAC: *mac-address*\] The station was added to global neighbor station hash table.]{lang="EN-US"}]{#struct_0_15944_11499_x1545090885}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_x1226904175}[被添加到全局邻居]{style="font-family:宋体"}[station]{lang="EN-US"}[哈希表中]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The radio was deleted from neighbor radio list: Aging time expired.]{lang="EN-US"}]{#struct_0_15944_11499_x1108253053}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_229930020}[达到老化时间，]{style="font-family:宋体"}[radio]{lang="EN-US"}[被从邻居]{style="font-family:宋体"}[radio]{lang="EN-US"}[链表中删除]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The radio was deleted from neighbor radio list: Radio went offline.]{lang="EN-US"}]{#struct_0_15944_11499_1439648649}

[[由于]{style="font-family:宋体"}[radio]{lang="EN-US"}]{#struct_0_15944_11499_x1936868947}[下线，]{style="font-family:宋体"}[radio]{lang="EN-US"}[被从邻居]{style="font-family:宋体"}[radio]{lang="EN-US"}[链表中删除]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The radio is in load balanced state.]{lang="EN-US"}]{#struct_0_15944_11499_x311766286}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_x1555383298}[当前为负载均衡状态]{style="font-family:宋体"}

[[\[MAC: *mac-address*\] The station has no valid neighbor radios.]{lang="EN-US"}]{#struct_0_15944_11499_641652708}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_x297182354}[无有效的邻居]{style="font-family:宋体"}[radio]{lang="EN-US"}

[[\[APID: *apid* RADIOID: *radioid*\] The radio is in load balanced state: It is not in any load balancing group.]{lang="EN-US"}]{#struct_0_15944_11499_856505449}

[[AC]{lang="EN-US"}]{#struct_0_15944_11499_x1336153921}[上存在负载均衡组，但是]{style="font-family:宋体"}[radio]{lang="EN-US"}[不在任何负载均衡组内，则本]{style="font-family:宋体"}[radio]{lang="EN-US"}[负载是均衡的]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid*\] The radio is in load balanced state: Its load didn\'t exceed the gap value.]{lang="EN-US"}]{#struct_0_15944_11499_544751723}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_x951063505}[是负载均衡的，因为其负载未超过配置的差值门限]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The radio is in load unbalanced state.]{lang="EN-US"}]{#struct_0_15944_11499_x1440508972}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_877765704}[当前为负载不均衡状态]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid*\] The radio was added to global radio load hash table.]{lang="EN-US"}]{#struct_0_15944_11499_1606456688}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_2145586339}[被添加到全局]{style="font-family:宋体"}[radio]{lang="EN-US"}[负载哈希表]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid*\] The radio was deleted from global radio load hash table.]{lang="EN-US"}]{#struct_0_15944_11499_586225916}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_x216198457}[被从全局]{style="font-family:宋体"}[radio]{lang="EN-US"}[负载哈希表中删除]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid*  MAC: *mac-address*\] The station was deleted from retry station hash table.]{lang="EN-US"}]{#struct_0_15944_11499_x1774094609}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_242499665}[的]{style="font-family:宋体"}[retry]{lang="EN-US"}[节点被从]{style="font-family:宋体"}[retry station]{lang="EN-US"}[哈希表中删除]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The station was added to retry station hash table.]{lang="EN-US"}]{#struct_0_15944_11499_x1376437029}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_x35116737}[被添加到]{style="font-family:宋体"}[retry station]{lang="EN-US"}[哈希表中]{style="font-family:宋体"}

[[\[MAC: *mac-address*\] The neighbor radio list is empty.]{lang="EN-US"}]{#struct_0_15944_11499_1042858436}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_x979858025}[的邻居]{style="font-family:宋体"}[radio]{lang="EN-US"}[链表为空]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The station was deleted from global neighbor station hash table.]{lang="EN-US"}]{#struct_0_15944_11499_2021547565}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_x1589988631}[被从全局邻居]{style="font-family:宋体"}[station]{lang="EN-US"}[哈希表中删除]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] Successfully rejected the association request of the station when the radio was in load unbalanced state.]{lang="EN-US"}]{#struct_0_15944_11499_2028417932}

[[当]{style="font-family:宋体"}[radio]{lang="EN-US"}]{#struct_0_15944_11499_1710863179}[负载不均衡时，拒绝]{style="font-family:宋体"}[station]{lang="EN-US"}[连接成功]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The station was permitted: Its association attempts reached the upper limit.]{lang="EN-US"}]{#struct_0_15944_11499_x1452235182}

[[因为]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_1749025330}[连接达到最大次数，所以允许其连接]{style="font-family:宋体"}[radio]{lang="EN-US"}

[[Changed the load balancing mode from session mode to traffic mode or bandwidth mode.]{lang="EN-US"}]{#struct_0_15944_11499_x1120016889}

[[无线负载均衡模式由会话模式改变为流量模式或者带宽模式]{style="font-family:宋体"}]{#struct_0_15944_11499_832501060}

[[Changed the load balancing mode from traffic or bandwidth mode to session mode.]{lang="EN-US"}]{#struct_0_15944_11499_1280986473}

[[无线负载均衡模式由流量模式或者带宽模式改变为会话模式]{style="font-family:宋体"}]{#struct_0_15944_11499_x2048041084}

[[Changed the load balancing mode between traffic mode and bandwidth mode.]{lang="EN-US"}]{#struct_0_15944_11499_1806209391}

[[无线负载均衡在流量模式或者带宽模式间转变]{style="font-family:宋体"}]{#struct_0_15944_11499_182941389}

[[Reset probe mask for all radios when the load balancing mode was changed.]{lang="EN-US"}]{#struct_0_15944_11499_x1310486220}

[[当无线负载均衡模式改变时重置所有]{style="font-family:宋体"}[radio]{lang="EN-US"}]{#struct_0_15944_11499_x1814778118}[的]{style="font-family:宋体"}[probe mask]{lang="EN-US"}[标志位]{style="font-family:宋体"}

[[\[MAC: *mac-address*\] Display the station\'s]{lang="EN-US"}]{#struct_0_15944_11499_x895475741}[ ]{lang="EN-US" style="font-size:10.5pt"}[neighbor radio list:]{lang="EN-US"}

[[显示]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_x766606342}[的邻居]{style="font-family:宋体"}[radio]{lang="EN-US"}[列表信息]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid*\] The group ID and load of the radio are *GroupID* and *radio-load*.]{lang="EN-US"}]{#struct_0_15944_11499_x1383142552}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_x35356974}[所在无线负载均衡组]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[GroupID]{lang="EN-US"}*[，当前负载信息为]{style="font-family:宋体"}*[radio-load]{lang="EN-US"}*

[[\[MAC: *mac-address*\] The station is a roaming station.]{lang="EN-US"}]{#struct_0_15944_11499_860299947}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_1596282899}[为漫游客户端]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The station was added to radio neighbor station hash table.]{lang="EN-US"}]{#struct_0_15944_11499_904622001}

[[邻居]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_x314220129}[节点添加到]{style="font-family:宋体"}[radio]{lang="EN-US"}[下的邻居]{style="font-family:宋体"}[station]{lang="EN-US"}[哈希表]{style="font-family:宋体"}

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The station was deleted from radio neighbor station hash table.]{lang="EN-US"}]{#struct_0_15944_11499_1345740803}

[[邻居]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_x1663548555}[节点从]{style="font-family:宋体"}[radio]{lang="EN-US"}[下的邻居]{style="font-family:宋体"}[station]{lang="EN-US"}[哈希表中删除]{style="font-family:宋体"}

[[\[MAC: *mac-address*\]]{lang="EN-US"}]{#struct_0_15944_11499_2138398727}[ ]{lang="EN-US" style="font-size:10.5pt;color:black"}[The station\'s RSSI *RSSI-value* is lower than the RSSI threshold *RSSI-cfg*.]{lang="EN-US"}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_x1102598959}[的]{style="font-family:宋体"}[RSSI]{lang="EN-US"}[值]{style="font-family:宋体"}*[RSSI-value]{lang="EN-US"}*[小于]{style="font-family:宋体"}[RSSI]{lang="EN-US"}[门限值]{style="font-family:宋体"}*[RSSI-cfg]{lang="EN-US"}*

[[\[APID: *apid* RADIOID: *radioid* MAC: *mac-address*\] The station was refused *refuse-times* times.]{lang="EN-US"}]{#struct_0_15944_11499_x467539027}

[[station]{lang="EN-US"}]{#struct_0_15944_11499_x220343138}[被无线负载均衡功能拒绝连接次数达到]{style="font-family:宋体"}*[ refuse-times]{lang="EN-US"}*[次]{style="font-family:宋体"}

[[WLB was enabled.]{lang="EN-US"}]{#struct_0_15944_11499_956718795}

[[无线负载均衡模块开启]{style="font-family:宋体"}]{#struct_0_15944_11499_792240628}

[[WLB was disabled.]{lang="EN-US"}]{#struct_0_15944_11499_x1051643848}

[[无线负载均衡模块关闭]{style="font-family:宋体"}]{#struct_0_15944_11499_x1786427079}

[[\[APID: *apid* RADIOID: *radioid*\] The radio between the current traffic load and the max throughput of the radio is *load-value.*]{lang="EN-US"}]{#struct_0_15944_11499_x727207093}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_1687850003}[当前负载的流量占]{style="font-family:宋体"}[radio]{lang="EN-US"}[支持的最大吞吐率的百分比为]{style="font-family:宋体"}*[load-value]{lang="EN-US"}*

[[\[APID: *apid* RADIOID: *radioid*\] The current bandwidth of the radio is *load-value* Mbps.]{lang="EN-US"}]{#struct_0_15944_11499_x1120504215}

[[radio]{lang="EN-US"}]{#struct_0_15944_11499_870664315}[的当前负载的带宽值为]{style="font-family:宋体"}[load-value Mbps]{lang="EN-US"}

[[\[APID:]{lang="EN-US"}]{#struct_0_15944_11499_229995556}*[apid]{lang="IT"}*[ RADIOID:]{lang="EN-US"}*[radioid]{lang="IT"}*[\] Successfully updated probe mask to hide probe response.]{lang="EN-US"}

[[WLB]{lang="EN-US"}]{#struct_0_15944_11499_1839179950}[模块成功更新]{style="font-family:宋体"}[probe mask]{lang="EN-US"}[至隐藏]{style="font-family:宋体"}[probe response]{lang="EN-US"}[状]{style="font-family:宋体"}

[[\[APID:]{lang="EN-US"}]{#struct_0_15944_11499_x29407938}*[apid]{lang="IT"}*[ RADIOID:]{lang="EN-US"}*[radioid]{lang="IT"}*[\] Successfully updated probe mask to answer probe response.]{lang="EN-US"}

[[WLB]{lang="EN-US"}]{#struct_0_15944_11499_x1723528250}[模块成功更新]{style="font-family:宋体"}[probe mask]{lang="EN-US"}[至应答]{style="font-family:宋体"}[probe response]{lang="EN-US"}[状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging wlan load-balance timer]{lang="EN-US"}]{#struct_0_15944_11499_x1460018457}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_130715664}[[字段]{style="font-family:黑体"}]{#struct_0_15944_11499_x1336088385}

[[描述]{style="font-family:黑体"}]{#struct_0_15944_11499_3143458}

[[Successfully created traffic load balancing timer.]{lang="EN-US"}]{#struct_0_15944_11499_x1347495757}

[[创建无线负载均衡流量定时器成功]{style="font-family:宋体"}]{#struct_0_15944_11499_x1271995290}

[[Failed to create traffic load balancing timer.]{lang="EN-US"}]{#struct_0_15944_11499_x1030292334}

[[创建无线负载均衡流量定时器失败]{style="font-family:宋体"}]{#struct_0_15944_11499_x505660969}

[[Failed to create retry station aging timer.]{lang="EN-US"}]{#struct_0_15944_11499_718336421}

[[创建]{style="font-family:宋体"}[retry station]{lang="EN-US"}]{#struct_0_15944_11499_491597816}[老化定时器失败]{style="font-family:宋体"}

[[\[MAC *mac-address*\] Failed to create global neighbor station aging timer.]{lang="EN-US"}]{#struct_0_15944_11499_377983919}

[[创建全局邻居]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_320541090}[老化定时器失败]{style="font-family:宋体"}

[[\[MAC *mac-address*\] Successfully created global neighbor station aging timer.]{lang="EN-US"}]{#struct_0_15944_11499_1057364972}

[[创建全局邻居]{style="font-family:宋体"}[station]{lang="EN-US"}]{#struct_0_15944_11499_585767164}[老化定时器成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15944_11499_x1606901700}

[[\# ]{lang="EN-US"}]{#struct_0_15944_11499_1576061688}[打开]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡事件调试信息开关]{style="font-family:宋体"}[,]{lang="EN-US"}[使能]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡。]{style="font-family:宋体"}

[[\<System\> debugging wlan load-balance event]{lang="EN-US"}]{#struct_0_15944_11499_x1349795741}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] wlan load-balance ]{lang="EN-US"}[enable]{lang="EN-US"}

[\*Sep 11 09:33:10:120 2014 H3C STAMGR/7/Event: WLB was enabled.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15944_11499_x2080661434}*[开启无线负载均衡成功]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15944_11499_236968757}[打开]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡错误调试信息开关，使能]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡，初始化失败。]{style="font-family:宋体"}

[[\<System\> debugging wlan load-balance error]{lang="EN-US"}]{#struct_0_15944_11499_x760973363}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] wlan load-balance ]{lang="EN-US"}[enable]{lang="EN-US"}

[\*Sep 11 09:33:11:120 2014 H3C STAMGR/7/Event**:** Failed to enable WLB: Configuration thread initialization failure.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15944_11499_x494567561}*[配置线程初始化失败，故开启]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15944_11499_809343651}[打开]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡定时器调试信息开关，切换模式到流量模式。]{style="font-family:宋体"}

[[\<System\> debugging wlan load-balance timer]{lang="EN-US"}]{#struct_0_15944_11499_x346924279}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] wlan load-balance ]{lang="EN-US"}[mode traffic 20]{lang="EN-US"}

[\*Sep 11 09:33:11:120 2014 H3C STAMGR/7/Timer**:** Successfully created traffic-mode load balancing timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15944_11499_1688682306}*[切换]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[负载均衡模式到流量模式，创建定时器成功]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
