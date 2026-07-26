::: {#-1763219931 .myid}
[]{#_Toc404797793}[]{#struct_0_19361_x3680_x611648604}

**TRILL \-- TRILL调试命令 \-- debugging trill**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_19361_x3680_1097103286}

[**[debugging]{lang="EN-US"}**[ **trill** { **all** \| **error** \| **event** \| **graceful-restart** \| **ha** \| **self-originate-update** \| **timer** \| **vr** \| { **adj-packet** \| **snp-packet** \| **update-packet** } \[ **receive** \| **send** \] \[ **verbose** \] \[ **interface** *interface-type* *interface-number* \] \| **route** \[ **mrc** \[ **thread-index** *thread-index* \] \| **topo** \| **urc** \] \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_19361_x3680_626195125}

[**[undo]{lang="EN-US"}**[ **debugging** **trill** { **all** \| **error** \| **event** \| ]{lang="EN-US"}**[graceful-restart]{lang="EN-US"}**[ \| **ha** \| **self-originate-update** \| **timer** \| **vr** \| { **adj-packet** \| **snp-packet** \| **update-packet** } \[ **receive** \| **send** \] \| **route** \[ **mrc** \| **topo** \| **urc** \] }]{lang="EN-US"}]{#struct_0_19361_x3680_x1944540276}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19361_x3680_2016451482}

[[用户视图]{style="font-family:宋体"}]{#struct_0_19361_x3680_x412908411}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19361_x3680_332298203}

[[network-admin]{lang="EN-US"}]{#struct_0_19361_x3680_229839728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19361_x3680_x1690255316}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19361_x3680_x611714140}

[**[all]{lang="EN-US"}**]{#struct_0_19361_x3680_1099212079}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_19361_x3680_37908410}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_19361_x3680_161797131}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议事件调试信息开关。]{style="font-family:宋体"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_19361_x3680_774737761}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议平滑重启调试信息开关。]{style="font-family:宋体"}

[**[ha]{lang="EN-US"}**]{#struct_0_19361_x3680_x2085559578}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[self-originate-update]{lang="EN-US"}**]{#struct_0_19361_x3680_x739882936}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议本地更新调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_19361_x3680_x1900688305}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议定时器调试信息开关。]{style="font-family:宋体"}

[**[vr]{lang="EN-US"}**]{#struct_0_19361_x3680_1332239872}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议]{style="font-family:宋体"}[VR]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Router]{lang="EN-US"}[，虚拟路由器）调试信息开关。]{style="font-family:宋体"}

[**[adj-packet]{lang="EN-US"}**]{#struct_0_19361_x3680_669222730}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议邻居报文调试信息开关。]{style="font-family:宋体"}

[**[snp-packet]{lang="EN-US"}**]{#struct_0_19361_x3680_x611517532}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[update-packet]{lang="EN-US"}**]{#struct_0_19361_x3680_737691417}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议更新报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_19361_x3680_726331093}[：表示接收的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_19361_x3680_x57394716}[：]{style="font-family:宋体"}[表示发送的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_19361_x3680_x1105573400}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议的详细调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_19361_x3680_x1767320114}[：指定接口类型和名称。如果未指定本参数，表示所有接口。]{style="font-family:宋体"}

[**[route]{lang="EN-US"}**]{#struct_0_19361_x3680_x1620998759}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议路由计算调试信息开关。]{style="font-family:宋体"}

[**[mrc]{lang="EN-US"}**]{#struct_0_19361_x3680_1361236516}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议组播路由计算调试信息开关。]{style="font-family:宋体"}

[**[thread-index]{lang="EN-US"}**[ *thread-index*]{lang="EN-US"}]{#struct_0_19361_x3680_331395601}[：指定组播路由的线程，]{style="font-family:宋体"}*[thread-index]{lang="EN-US"}*[为线程索引号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～当前最大线程数。如果未指定本参数，表示所有线程。]{style="font-family:宋体"}

[**[topo]{lang="EN-US"}**]{#struct_0_19361_x3680_x611583068}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议路由调度和拓扑变化调试信息开关。]{style="font-family:宋体"}

[**[urc]{lang="EN-US"}**]{#struct_0_19361_x3680_1493464242}[：表示]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议单播路由计算调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_19361_x3680_1731799697}

[**[debugging]{lang="EN-US"}**[ **trill**]{lang="EN-US"}]{#struct_0_19361_x3680_x2121775875}[命令用来打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议的调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **trill**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_x1936093609}[协议的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定]{style="font-family:宋体"}**[receive]{lang="EN-US"}**]{#struct_0_19361_x3680_x836311100}[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，则同时打开接收和发送]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议报文的调试信息开关。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging trill error]{lang="EN-US"}]{#struct_0_19361_x3680_1391095191}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x49259826}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_980661877}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_x611386460}

[[Get system\'s area address failed when encoding AREA]{lang="EN-US"}]{#struct_0_19361_x3680_1488829323}

[[对]{style="font-family:宋体"}[AREA TLV]{lang="EN-US"}]{#struct_0_19361_x3680_x1140505041}[进行编码时，未能获取到系统提供的区域地址]{style="font-family:宋体"}

[[DRB/RB send HELLO failed on circuit(*port*) in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_x2057102619}

[[DRB/RB]{lang="EN-US"}]{#struct_0_19361_x3680_1531391170}[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[内发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[RB send HELLO failed on circuit(*port*) in designated VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_x611451996}

[[RB]{lang="EN-US"}]{#struct_0_19361_x3680_x1180869110}[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的指定]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[内发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to send TCN/MTU-ack on circuit(*port*) in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_1492760127}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_1343379534}[的]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[内发送]{style="font-family:宋体"}[TCN/]{lang="EN-US"}[MTU-ack]{lang="SV"}[报文失败]{style="font-family:宋体"}

[[LAN ADJ number has arrived max]{lang="EN-US"}]{#struct_0_19361_x3680_1098538351}

[[邻居数量达到最大值]{style="font-family:宋体"}]{#struct_0_19361_x3680_2012984111}

[[Get TRILL HELLO/MTU/BPDU socket failed]{lang="EN-US"}]{#struct_0_19361_x3680_x611255388}

[[获取]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_x1239207997}[报文]{style="font-family:宋体"}[Hello/MTU/BPDU]{lang="EN-US"}[相关的]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[IF index *port* set *packet* option *index* failed]{lang="EN-US"}]{#struct_0_19361_x3680_1484094842}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x1259058718}[上设置报文]{style="font-family:宋体"}[Hello/MTU/BPDU]{lang="EN-US"}[的]{style="font-family:宋体"}*[index]{lang="EN-US"}*[选项失败]{style="font-family:宋体"}

[[Level-1 Hello timer start failed]{lang="EN-US"}]{#struct_0_19361_x3680_x1672030741}

[[Level-1]{lang="EN-US"}]{#struct_0_19361_x3680_x611320924}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器启动失败]{style="font-family:宋体"}

[[UPDT Module NBR TLV Modify Failed]{lang="EN-US"}]{#struct_0_19361_x3680_1545327193}

[[修改]{style="font-family:宋体"}[UPDT]{lang="EN-US"}]{#struct_0_19361_x3680_915537128}[模块的邻居]{style="font-family:宋体"}[TLV]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Hold timer start failed]{lang="EN-US"}]{#struct_0_19361_x3680_x1052520791}

[[保持定时器启动失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611779675}

[[Get circuit(*port*)\'s *string* failed]{lang="EN-US"}]{#struct_0_19361_x3680_x1629945091}

[[获取接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x934644117}[的]{style="font-family:宋体"}*[string]{lang="EN-US"}*[参数失败。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[priority]{lang="EN-US"}]{#struct_0_19361_x3680_1303580776}[：表示优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MTU]{lang="EN-US"}]{#struct_0_19361_x3680_x1819401406}[：表示最大报文长度]{style="font-family:宋体"}

[[Get adj pointer failed when starting hello timer]{lang="EN-US"}]{#struct_0_19361_x3680_x611845211}

[[当开启]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_19361_x3680_1101934834}[定时器时，获取]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[指针失败]{style="font-family:宋体"}

[[Invalid adj pointer when getting designated vlan information]{lang="EN-US"}]{#struct_0_19361_x3680_823260462}

[[当获取指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x2109842440}[时，]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[指针无效]{style="font-family:宋体"}

[[Hello packet send failed on circuit(*port*)]{lang="EN-US"}]{#struct_0_19361_x3680_x611648603}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_1096906678}[上发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Hello timer create failed on circuit(*port*)]{lang="EN-US"}]{#struct_0_19361_x3680_2130395327}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_1439875314}[上创建]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to create timer *string*]{lang="EN-US"}]{#struct_0_19361_x3680_x611714139}

[[创建定时器失败，]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_19361_x3680_1099801896}[为定时器创建失败的时机]{style="font-family:宋体"}

[[Failed to get memory for *string*]{lang="EN-US"}]{#struct_0_19361_x3680_3793681}

[[创建数据时分配资源失败，]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_19361_x3680_x611517531}[为分配资源失败的时机]{style="font-family:宋体"}

[[Failed to get local DRB when filter the AVF]{lang="EN-US"}]{#struct_0_19361_x3680_737888025}

[[相同链路多端口识别时，无法找到本]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_19361_x3680_557653132}[的]{style="font-family:宋体"}[DRB]{lang="EN-US"}

[[Failed to create bit map for *string*]{lang="EN-US"}]{#struct_0_19361_x3680_210743246}

[[创建位图资源失败，]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_19361_x3680_x611583067}[为创建失败的时机]{style="font-family:宋体"}

[[Failed to get group router information when checking update]{lang="EN-US"}]{#struct_0_19361_x3680_1493791922}

[[更新检查时获取组播路由器信息失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_1757930419}

[[Failed to get buffer when sending MTU-ack]{lang="EN-US"}]{#struct_0_19361_x3680_x611386459}

[[发送]{style="font-family:宋体"}[MTU-ack]{lang="EN-US"}]{#struct_0_19361_x3680_1488239500}[报文时获取资源失败]{style="font-family:宋体"}

[[Invalid NULL parameter in getting AVF information]{lang="EN-US"}]{#struct_0_19361_x3680_x1524938889}

[[入参数为空，错误]{style="font-family:宋体"}]{#struct_0_19361_x3680_441975726}

[[Failed to create nexthop attribute.]{lang="EN-US"}]{#struct_0_19361_x3680_x611451995}

[[创建下一跳属性失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1180672502}

[[Failed to notify next hop message.]{lang="EN-US"}]{#struct_0_19361_x3680_511699914}

[[通知下一跳信息失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611255387}

[[Failed to get SPF node.]{lang="EN-US"}]{#struct_0_19361_x3680_x1238487101}

[[获取]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_19361_x3680_x464291575}[节点失败]{style="font-family:宋体"}

[[Failed to create/get AVF node.]{lang="EN-US"}]{#struct_0_19361_x3680_x611320923}

[[创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_1545392729}[获取]{style="font-family:宋体"}[AVF]{lang="EN-US"}[信息节点失败]{style="font-family:宋体"}

[[Failed to create AVF attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_1632590528}

[[创建]{style="font-family:宋体"}[AVF]{lang="EN-US"}]{#struct_0_19361_x3680_x611779678}[属性失败]{style="font-family:宋体"}

[[Failed to notify AVF message.]{lang="EN-US"}]{#struct_0_19361_x3680_x1630272771}

[[通知]{style="font-family:宋体"}[AVF]{lang="EN-US"}]{#struct_0_19361_x3680_1225591206}[信息失败]{style="font-family:宋体"}

[[Failed to create IPv4 multicast router attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_x611845214}

[[创建]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_19361_x3680_1102262514}[组播路由器属性失败]{style="font-family:宋体"}

[[Failed to notify IPv4 multicast router message.]{lang="EN-US"}]{#struct_0_19361_x3680_x611648606}

[[通知]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_19361_x3680_1097234358}[组播路由器属性失败]{style="font-family:宋体"}

[[Failed to create IPv6 multicast router attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_202845022}

[[创建]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19361_x3680_x611714142}[组播路由器属性失败]{style="font-family:宋体"}

[[Failed to notify IPv6 multicast router message.]{lang="EN-US"}]{#struct_0_19361_x3680_1099081007}

[[通知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19361_x3680_x1542921198}[组播路由器属性失败]{style="font-family:宋体"}

[[Failed to create multicast receiver attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_x611517534}

[[创建组播接收者属性失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_737560345}

[[Failed to notify multicast receiver message.]{lang="EN-US"}]{#struct_0_19361_x3680_74026737}

[[通知组播接收者属性失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611583070}

[[Failed to create used tree attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_1493988529}

[[创建]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_19361_x3680_2124657324}[声明使用的分发树属性失败]{style="font-family:宋体"}

[[Failed to notify used tree message.]{lang="EN-US"}]{#struct_0_19361_x3680_x611386462}

[[通知]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_19361_x3680_1488960395}[声明使用的分发树属性失败]{style="font-family:宋体"}

[[Failed to create spf node attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_x611451998}

[[创建]{style="font-family:宋体"}[SPFNode]{lang="EN-US"}]{#struct_0_19361_x3680_x1181524470}[属性失败]{style="font-family:宋体"}

[[Failed to notify spf node message.]{lang="EN-US"}]{#struct_0_19361_x3680_x494954831}

[[通知]{style="font-family:宋体"}[SPFNode]{lang="EN-US"}]{#struct_0_19361_x3680_x611255390}[属性失败]{style="font-family:宋体"}

[[Failed to create spf link attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_x1238683708}

[[创建]{style="font-family:宋体"}[SPFLink]{lang="EN-US"}]{#struct_0_19361_x3680_x611320926}[属性失败]{style="font-family:宋体"}

[[Failed to notify spf link message.]{lang="EN-US"}]{#struct_0_19361_x3680_1545196121}

[[通知]{style="font-family:宋体"}[SPFLink]{lang="EN-US"}]{#struct_0_19361_x3680_x611779677}[属性失败]{style="font-family:宋体"}

[[Failed to find D-node while adding D-link.]{lang="EN-US"}]{#struct_0_19361_x3680_x1629814019}

[[在添加]{style="font-family:宋体"}[D-link]{lang="EN-US"}]{#struct_0_19361_x3680_x1009858152}[的时候查找]{style="font-family:宋体"}[D-node]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to load root D-node.]{lang="EN-US"}]{#struct_0_19361_x3680_x611845213}

[[加载根]{style="font-family:宋体"}[D-node]{lang="EN-US"}]{#struct_0_19361_x3680_1102065906}[失败]{style="font-family:宋体"}

[[Failed to add VN head, NBR id is *id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x611648605}

[[添加]{style="font-family:宋体"}[VN head]{lang="EN-US"}]{#struct_0_19361_x3680_1097037750}[失败，]{style="font-family:宋体"}[NBR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Failed to alloc VN head while caching prefix, NBR id is *id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x611714141}

[[缓存前缀时分配]{style="font-family:宋体"}[VN head]{lang="EN-US"}]{#struct_0_19361_x3680_1099277615}[失败，]{style="font-family:宋体"}[NBR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Failed to alloc prefix head while caching prefix, NBR id is *id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x760427127}

[[缓存前缀时分配]{style="font-family:宋体"}[prefix head]{lang="EN-US"}]{#struct_0_19361_x3680_x611517533}[失败，]{style="font-family:宋体"}[NBR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[The flush table size is zero.]{lang="EN-US"}]{#struct_0_19361_x3680_737756953}

[[下刷表的大小是零]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611583069}

[[The flush table is not empty.]{lang="EN-US"}]{#struct_0_19361_x3680_1493398706}

[[下刷表不为空]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611386461}

[[Failed to create Ingress/port/TVMac/TVlan/RPF/Tree entry.]{lang="EN-US"}]{#struct_0_19361_x3680_1488763787}

[[创建]{style="font-family:宋体"}[Ingress/]{lang="EN-US"}]{#struct_0_19361_x3680_x611451997}[端口节点]{style="font-family:宋体"}[/TVMac/TVlan/RPF/]{lang="EN-US"}[组播分发树表项失败]{style="font-family:宋体"}

[[Failed to create local entry attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_x1180803574}

[[创建本地端口列表属性失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611255389}

[[Failed to notify local entry message.]{lang="EN-US"}]{#struct_0_19361_x3680_x1239142461}

[[通知本地端口列表属性失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611320925}

[[Failed to get Ingress entry.]{lang="EN-US"}]{#struct_0_19361_x3680_1545261657}

[[获取]{style="font-family:宋体"}[Ingress]{lang="EN-US"}]{#struct_0_19361_x3680_x611779680}[表项失败]{style="font-family:宋体"}

[[Failed to find d-tree node *id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1629748476}

[[获取]{style="font-family:宋体"}[D-node]{lang="EN-US"}]{#struct_0_19361_x3680_x611845216}[失败，]{style="font-family:宋体"}[source ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Failed to find self dtree node.]{lang="EN-US"}]{#struct_0_19361_x3680_1102393586}

[[获取当前]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_19361_x3680_x611648608}[对应的]{style="font-family:宋体"}[D-node]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get source id by nickname.]{lang="EN-US"}]{#struct_0_19361_x3680_1096316854}

[[根据]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_x611714144}[获取]{style="font-family:宋体"}[D-node]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get port info of dtree link.]{lang="EN-US"}]{#struct_0_19361_x3680_1098949935}

[[获取]{style="font-family:宋体"}[D-link]{lang="EN-US"}]{#struct_0_19361_x3680_x611517536}[的端口信息失败]{style="font-family:宋体"}

[[Failed to create calc tree attrib.]{lang="EN-US"}]{#struct_0_19361_x3680_737429273}

[[创建待计算的分发树属性失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611583072}

[[Failed to notify calc tree message.]{lang="EN-US"}]{#struct_0_19361_x3680_1494119601}

[[通知待计算的分发树属性失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611386464}

[[(N*id*) Failed to build nexthop head list.]{lang="EN-US"}]{#struct_0_19361_x3680_1488567179}

[[（]{style="font-family:宋体"}[N*id*]{lang="EN-US"}]{#struct_0_19361_x3680_x611452000}[）构造]{style="font-family:宋体"}[nexthop head]{lang="EN-US"}[链表失败，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[NBR ID]{lang="EN-US"}

[[Failed to expand NBR array, error is *error*, index is *index*.]{lang="EN-US"}]{#struct_0_19361_x3680_x41883290}

[[扩展]{style="font-family:宋体"}[NBR]{lang="EN-US"}]{#struct_0_19361_x3680_x611255392}[数组失败，错误码为]{style="font-family:宋体"}*[error]{lang="EN-US"}*[，索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[Failed to alloc NBR/id node memory.]{lang="EN-US"}]{#struct_0_19361_x3680_x1238814780}

[[申请]{style="font-family:宋体"}[NBR/id node]{lang="EN-US"}]{#struct_0_19361_x3680_x611320928}[内存失败]{style="font-family:宋体"}

[[Create new TMFibNode error.]{lang="EN-US"}]{#struct_0_19361_x3680_1546113625}

[[创建]{style="font-family:宋体"}[TMFibNode]{lang="EN-US"}]{#struct_0_19361_x3680_x611779679}[失败]{style="font-family:宋体"}

[[(L*level*:P*prefix*) Failed to build nexthop list.]{lang="EN-US"}]{#struct_0_19361_x3680_x611845215}

[[（]{style="font-family:宋体"}[L*level*:P*prefix*]{lang="EN-US"}]{#struct_0_19361_x3680_1102196978}[）构造]{style="font-family:宋体"}[nexthop]{lang="EN-US"}[链表失败。]{style="font-family:宋体"}*[level]{lang="EN-US"}*[表示级别，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(M*id*:L*level*) Failed to calculate unicast route, prefix is P*prefix*.]{lang="EN-US"}]{#struct_0_19361_x3680_x611648607}

[[（]{style="font-family:宋体"}[M*id*:L*level*]{lang="EN-US"}]{#struct_0_19361_x3680_1097168822}[）计算单播路由失败。]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[level]{lang="EN-US"}*[表示级别，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[Failed to create flush table.]{lang="EN-US"}]{#struct_0_19361_x3680_x611714143}

[[创建下刷表失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611517535}

[[Get interface index failed.]{lang="EN-US"}]{#struct_0_19361_x3680_737625881}

[[没有获取到接口索引]{style="font-family:宋体"}]{#struct_0_19361_x3680_x611583071}

[[Flush/Clean TMNG information failed.]{lang="EN-US"}]{#struct_0_19361_x3680_1493922993}

[[下刷]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_x611386463}[清除]{style="font-family:宋体"}[TMNG]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[Interface(*port*) cost exceeds max value.]{lang="EN-US"}]{#struct_0_19361_x3680_1488894859}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x611451999}[的]{style="font-family:宋体"}[cost]{lang="EN-US"}[值超过最大值]{style="font-family:宋体"}

[[MTU size exceeds max PDU size (*size*), setting it to max PDU size.]{lang="EN-US"}]{#struct_0_19361_x3680_x611255391}

[[接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_19361_x3680_x1238618172}[超过最大]{style="font-family:宋体"}[PDU]{lang="EN-US"}[值]{style="font-family:宋体"}*[size]{lang="EN-US"}*[，设置其等于最大]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Create VLAN BITMAP failed.]{lang="EN-US"}]{#struct_0_19361_x3680_x611320927}

[[创建]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_1545130585}[位图资源失败]{style="font-family:宋体"}

[[Get interface enable VLAN failed.]{lang="EN-US"}]{#struct_0_19361_x3680_954304265}

[[获取接口使能]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x1328515028}[失败]{style="font-family:宋体"}

[[Processing interface MTU change error.]{lang="EN-US"}]{#struct_0_19361_x3680_954238729}

[[处理接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_19361_x3680_x1735189760}[变化事件错误]{style="font-family:宋体"}

[[The interface(*port*) active failed.]{lang="EN-US"}]{#struct_0_19361_x3680_954435337}

[[激活接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_954369801}[失败]{style="font-family:宋体"}

[[Notify interface delete error on interface: *port*]{lang="EN-US"}]{#struct_0_19361_x3680_x219937260}

[[通知接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_954566409}[删除事件错误]{style="font-family:宋体"}

[[Invalid phase *phase*, ignore event.]{lang="EN-US"}]{#struct_0_19361_x3680_954500873}

[[无效的]{style="font-family:宋体"}*[phase]{lang="EN-US"}*]{#struct_0_19361_x3680_x1124334024}[阶段，忽略该事件]{style="font-family:宋体"}

[[The event type and disable phase mismatch.]{lang="EN-US"}]{#struct_0_19361_x3680_954697481}

[[事件类型与关闭阶段不匹配]{style="font-family:宋体"}]{#struct_0_19361_x3680_954631945}

[[Connect to *module* daemon failed.]{lang="EN-US"}]{#struct_0_19361_x3680_x1252492426}

[[连接到]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_19361_x3680_954828553}[模块失败。]{style="font-family:宋体"}*[module]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HA]{lang="EN-US"}]{#struct_0_19361_x3680_1752892365}[：表示高可用性模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IFM]{lang="EN-US"}]{#struct_0_19361_x3680_954763017}[：表示接口管理模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[KERNEL]{lang="EN-US"}]{#struct_0_19361_x3680_954304266}[：表示内核模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEV]{lang="EN-US"}]{#struct_0_19361_x3680_x1328515027}[：表示设备管理模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MCS]{lang="EN-US"}]{#struct_0_19361_x3680_954238730}[：表示二层组播模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_954435338}[：表示]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[管理模块]{lang="EN-US" style="font-family:宋体"}

[[Send HA response(*type*) error.]{lang="NO-BOK"}]{#struct_0_19361_x3680_x1839010451}

[[向]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_19361_x3680_954369802}[模块发送]{style="font-family:宋体"}*[type]{lang="NO-BOK"}*[响应错误。]{style="font-family:宋体"}*[type]{lang="NO-BOK"}*[包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BATCH_OVER]{lang="EN-US"}]{#struct_0_19361_x3680_954566410}[：表示批量备份结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UPGRADE_OVER]{lang="EN-US"}]{#struct_0_19361_x3680_x645230897}[：表示升级结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STOP_OVER]{lang="EN-US"}]{#struct_0_19361_x3680_954500874}[：表示停止结束]{lang="EN-US" style="font-family:宋体"}

[[External init error.]{lang="EN-US"}]{#struct_0_19361_x3680_954697482}

[[升级时外部初始化错误]{style="font-family:宋体"}]{#struct_0_19361_x3680_x354316196}

[[Invalid MAC type.]{lang="EN-US"}]{#struct_0_19361_x3680_954631946}

[[无效的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19361_x3680_954828554}[地址类型]{style="font-family:宋体"}

[[Create BITMAP failed.]{lang="EN-US"}]{#struct_0_19361_x3680_1752892370}

[[创建位图资源失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_954763018}

[[Get/Set port enabled VLAN failed.]{lang="EN-US"}]{#struct_0_19361_x3680_954304263}

[[获取]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_954238727}[设置端口使能]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VLAN handle moved from epoll failed.]{lang="EN-US"}]{#struct_0_19361_x3680_x1735189766}

[[从]{style="font-family:宋体"}[EPOLL]{lang="EN-US"}]{#struct_0_19361_x3680_954435335}[中移除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[句柄失败]{style="font-family:宋体"}

[[Failed to create lsp change notify message.]{lang="EN-US"}]{#struct_0_19361_x3680_954369799}

[[创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x908715475}[变化通知消息失败]{style="font-family:宋体"}

[[Failed to set updt socket option.]{lang="EN-US"}]{#struct_0_19361_x3680_954566407}

[[设置]{style="font-family:宋体"}[updt]{lang="EN-US"}]{#struct_0_19361_x3680_954500871}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[选项失败]{style="font-family:宋体"}

[[Failed to start csnp/psnp/lsp flood timer on circuit *port*.]{lang="EN-US"}]{#struct_0_19361_x3680_954697479}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_365727825}[上启动]{style="font-family:宋体"}[CSNP/PSNP/LSP]{lang="EN-US"}[泛洪定时器失败]{style="font-family:宋体"}

[[Failed to stop lsp flood/level-1 timer on circuit *port*.]{lang="EN-US"}]{#struct_0_19361_x3680_954631943}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_954828551}[上停止]{style="font-family:宋体"}[LSP]{lang="EN-US"}[泛洪]{style="font-family:宋体"}[/level-1]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to insert neighbor/group record/nickname to list.]{lang="EN-US"}]{#struct_0_19361_x3680_954763015}

[[将邻居信息]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_1937334584}[组地址记录]{style="font-family:宋体"}[/Nickname]{lang="EN-US"}[加入列表失败]{style="font-family:宋体"}

[[Lsp info update failed.]{lang="EN-US"}]{#struct_0_19361_x3680_954304264}

[[更新]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_954238728}[信息失败]{style="font-family:宋体"}

[[Lsp insert failed.]{lang="EN-US"}]{#struct_0_19361_x3680_954435336}

[[添加]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x1839010457}[失败]{style="font-family:宋体"}

[[Failed to send pdu, returns *return*, buffer length is *length*.]{lang="EN-US"}]{#struct_0_19361_x3680_954369800}

[[发送报文失败，发送缓冲区大小为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_19361_x3680_954566408}[，返回值为]{style="font-family:宋体"}*[return]{lang="EN-US"}*

[[Lsp size(*size*) is larger than circuit mtu(*mtu*).]{lang="EN-US"}]{#struct_0_19361_x3680_954500872}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x1124334025}[的大小]{style="font-family:宋体"}*[size]{lang="EN-US"}*[大于接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}*[mtu]{lang="EN-US"}*

[[Lsp send failed.]{lang="EN-US"}]{#struct_0_19361_x3680_954697480}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_954631944}[报文失败]{style="font-family:宋体"}

[[Send level-1 CSNP/PSNP pdu failed.]{lang="EN-US"}]{#struct_0_19361_x3680_954828552}

[[发送]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_1752892364}[的]{style="font-family:宋体"}[CSNP/PSNP]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to install lsp with seq number zero.]{lang="EN-US"}]{#struct_0_19361_x3680_954763016}

[[安装序号为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_19361_x3680_954304261}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to add/delete level-1 area address *address*.]{lang="EN-US"}]{#struct_0_19361_x3680_954238725}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_954435333}[删除]{style="font-family:宋体"}[level-1]{lang="EN-US"}[的区域地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to add/delete level-1 protocol support *ProNumber*(*ProString*).]{lang="EN-US"}]{#struct_0_19361_x3680_x1839010462}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_954369797}[删除]{style="font-family:宋体"}[level-1]{lang="EN-US"}[支持的协议类型]{style="font-family:宋体"}*[ProNumber]{lang="EN-US"}*[(*ProString*)]{lang="EN-US"}[失败。]{style="font-family:宋体"}*[ProString]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_954566405}[：表示]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unknown]{lang="EN-US"}]{#struct_0_19361_x3680_954500869}[：表示其它协议]{lang="EN-US" style="font-family:宋体"}

[[Failed to create timer after sending TCN]{lang="EN-US"}]{#struct_0_19361_x3680_954697477}

[[发送]{style="font-family:宋体"}[TCN]{lang="EN-US"}]{#struct_0_19361_x3680_365727839}[后定时器创建失败]{style="font-family:宋体"}

[[Failed to add/delete/modify level-1neighbour: system *system* =\> neighbour *neighbour*.]{lang="EN-US"}]{#struct_0_19361_x3680_954631941}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_954828549}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新]{style="font-family:宋体"}[level-1]{lang="EN-US"}[由]{style="font-family:宋体"}*[system]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighbour]{lang="EN-US"}*[的邻居信息失败]{style="font-family:宋体"}

[[Failed to add/delete level-1 pseudo neighbour: pseudo *pseudo* =\> neighbour *neighbour*.]{lang="EN-US"}]{#struct_0_19361_x3680_954763013}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_954304262}[删除]{style="font-family:宋体"}[level-1]{lang="EN-US"}[由]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighbour]{lang="EN-US"}*[的伪节点邻居信息失败]{style="font-family:宋体"}

[[Failed to insert local/other nickname to tree root list.]{lang="EN-US"}]{#struct_0_19361_x3680_x1328515031}

[[将本地]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_954238726}[其它]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[加入分发树树根列表失败]{style="font-family:宋体"}

[[No valid nickname.]{lang="EN-US"}]{#struct_0_19361_x3680_954435334}

[[没有可用的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_954369798}

[[Failed to add remote nickname(*remote*) to db.]{lang="EN-US"}]{#struct_0_19361_x3680_954566406}

[[将远端]{style="font-family:宋体"}[Nickname *remote*]{lang="EN-US"}]{#struct_0_19361_x3680_954500870}[加入]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[数据库失败]{style="font-family:宋体"}

[[PDU level(]{lang="EN-US"}[1) mismatch with circuit level(*level*).]{lang="EN-US"}]{#struct_0_19361_x3680_x1124334027}

[[PDU]{lang="EN-US"}]{#struct_0_19361_x3680_954697478}[报文中的]{style="font-family:宋体"}[level(1)]{lang="EN-US"}[与接口级别]{style="font-family:宋体"}*[level]{lang="EN-US"}*[不匹配]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging trill event]{lang="EN-US"}]{#struct_0_19361_x3680_365727826}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x190930}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_954631942}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_x1252492431}

[[DRB changed on *port*: old DRB: *mac1*, new DRB: *mac2*]{lang="EN-US"}]{#struct_0_19361_x3680_x633763882}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x1982834856}[所属网段的]{style="font-family:宋体"}[DRB]{lang="EN-US"}[发生改变，旧]{style="font-family:宋体"}[DRB]{lang="EN-US"}[和新]{style="font-family:宋体"}[DRB]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址分别为]{style="font-family:宋体"}*[mac1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[mac2]{lang="EN-US"}*

[[System\'s state is disable]{lang="EN-US"}]{#struct_0_19361_x3680_622120881}

[[系统处于关闭状态]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1362773262}

[[Update *string* to DBM]{lang="EN-US"}]{#struct_0_19361_x3680_954828550}

[[更新配置到]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_19361_x3680_1752892366}[，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}[proc enable/trill enable/trees calculate/tree root priority/lsp refresh timer/lsp max age timer/log peer change switch]{lang="EN-US"}

[[Update *string* to DBM on the interface *port,* flag is *flag*.]{lang="EN-US"}]{#struct_0_19361_x3680_1392917208}

[[更新接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_2038418465}[上的配置到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[，]{style="font-family:宋体"}*[flag]{lang="EN-US"}*[为删除标记，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}[HELLO holding multiplier/CSNP timer/hello timer/drb priority/trill link type/avf inhibited timer/Lsp throttle]{lang="EN-US"}

[[Delete interface *name* data from DBM *active*.]{lang="EN-US"}]{#struct_0_19361_x3680_1466936820}

[[删除]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_19361_x3680_1078136389}[中的接口配置数据，]{style="font-family:宋体"}*[name]{lang="EN-US"}*[为接口名，]{style="font-family:宋体"}*[active]{lang="EN-US"}*[为]{style="font-family:宋体"}[DBM]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[No need to add receiver for it already exist]{lang="EN-US"}]{#struct_0_19361_x3680_954763014}

[[无需添加组播接收者信息，因为已存在相同的信息]{style="font-family:宋体"}]{#struct_0_19361_x3680_1937334583}

[[No need to delete receiver for it is to be used]{lang="EN-US"}]{#struct_0_19361_x3680_1221411530}

[[无需删除组播接收者信息，因为已不存在]{style="font-family:宋体"}]{#struct_0_19361_x3680_x562976776}

[[None of the port is AVF when receiving MCS information]{lang="EN-US"}]{#struct_0_19361_x3680_x1418348730}

[[二层组播报文中的接口都不是]{style="font-family:宋体"}[AVF]{lang="EN-US"}]{#struct_0_19361_x3680_x98591596}[，无需处理此报文]{style="font-family:宋体"}

[[Ready to process MCS information for circuit *port* AVF change]{lang="EN-US"}]{#struct_0_19361_x3680_506498128}

[[准备处理接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_1469232724}[收到的二层组播报文]{style="font-family:宋体"}

[[Clear all AVF in circuit *port*]{lang="EN-US"}]{#struct_0_19361_x3680_x1057276606}

[[清除接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x1418414266}[上的所有]{style="font-family:宋体"}[AVF]{lang="EN-US"}

[[The new AVF is same as the current, no neet to process]{lang="EN-US"}]{#struct_0_19361_x3680_x1629105034}

[[新分配的]{style="font-family:宋体"}[AVF]{lang="EN-US"}]{#struct_0_19361_x3680_406429062}[与当前]{style="font-family:宋体"}[AVF]{lang="EN-US"}[相同，无需处理]{style="font-family:宋体"}

[[VLAN *vlan-id* is already inhibited, reset the timer]{lang="EN-US"}]{#struct_0_19361_x3680_x492814579}

[[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_x1397819118}[已被抑制，重置抑制定时器]{style="font-family:宋体"}

[[Circuit *port* is already inhibited, no need to notify inhibit of VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_x1418217658}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_1026115172}[已经全局抑制，无需单独进行]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[的抑制]{style="font-family:宋体"}

[[Circuit *port* is already inhibited, reset the timer.]{lang="EN-US"}]{#struct_0_19361_x3680_x1579362829}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_558184957}[已经全局抑制，重启定时器]{style="font-family:宋体"}

[[No need to filter for *string*]{lang="EN-US"}]{#struct_0_19361_x3680_x1418283194}

[[无需进行相同链路多端口识别，]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_19361_x3680_x686061338}[为不进行该处理的原因]{style="font-family:宋体"}

[[Enable the interface *port* packet send to CPU.]{lang="EN-US"}]{#struct_0_19361_x3680_x743720797}

[[通知驱动在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_1638207863}[上送]{style="font-family:宋体"}[/]{lang="EN-US"}[停止上送协议报文]{style="font-family:宋体"}

[[Disable the interface *port* packet send to CPU.]{lang="EN-US"}]{#struct_0_19361_x3680_x1418086586}

[[通知驱动在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_874017304}[停止上送协议报文]{style="font-family:宋体"}

[[Flush/Clean the TMNG information to interface *port*.]{lang="EN-US"}]{#struct_0_19361_x3680_x200283930}

[[下刷]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_1669889058}[清除接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[管理信息]{style="font-family:宋体"}

[[Flush TMNG port link type/enable to interface *por*t.]{lang="EN-US"}]{#struct_0_19361_x3680_x1418152122}

[[下刷]{style="font-family:宋体"}[TMNG]{lang="EN-US"}]{#struct_0_19361_x3680_104391195}[端口链路类型]{style="font-family:宋体"}[/enable]{lang="EN-US"}[到接口]{style="font-family:宋体"}*[por]{lang="EN-US"}*[t.]{lang="EN-US"}

[[Set TRILL PDU/ BPDU up to CPU, flag is *flag*, ifindex is *ifindex*, Mac is *mac*, result is *result.*]{lang="EN-US"}]{#struct_0_19361_x3680_x1198409905}

[[向]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_19361_x3680_x1417955514}[上送]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[报文，]{style="font-family:宋体"}*[flag]{lang="EN-US"}*[表示使能标记，]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[表示索引，]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[result]{lang="EN-US"}*[表示返回值]{style="font-family:宋体"}

[[Reset TMNG port enable/ link type to LAGG member interface *port.*]{lang="EN-US"}]{#struct_0_19361_x3680_x138676094}

[[成员端口向内核重新下刷接口上的管理信息]{style="font-family:宋体"}]{#struct_0_19361_x3680_494074278}

[[Flush TMNG port enable/ link type/ AVF/ default VLAN to LAGG member interface *port*.]{lang="EN-US"}]{#struct_0_19361_x3680_x801094150}

[[成员端口向内核下刷接口上的管理信息]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1418021050}

[[Clean all TMNG information to LAGG member interface *port*..]{lang="EN-US"}]{#struct_0_19361_x3680_x1315591027}

[[清除成员端口的管理信息]{style="font-family:宋体"}]{#struct_0_19361_x3680_x865868763}

[[Failed to get speed from interface *port.*]{lang="EN-US"}]{#struct_0_19361_x3680_x1417824442}

[[获取接口速率失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x2094087438}

[[MTU size is not equal to default PDU size (*size*), setting it to default PDU size.]{lang="EN-US"}]{#struct_0_19361_x3680_2001942935}

[[当]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_19361_x3680_x506254105}[大小不等于默认大小时，设置成默认值]{style="font-family:宋体"}

[[Interface: *ifindex* leave LAGG, clean the initial TRILL config.]{lang="EN-US"}]{#struct_0_19361_x3680_x1417889978}

[[接口离开清除配置]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1337500933}

[[Interface: *ifindex* leave LAGG, set the new TRILL config.]{lang="EN-US"}]{#struct_0_19361_x3680_x1095691295}

[[接口离开设置配置]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1418348729}

[[TMNG smooth end.]{lang="EN-US"}]{#struct_0_19361_x3680_1823788241}

[[设备平滑结束]{style="font-family:宋体"}]{#struct_0_19361_x3680_710596699}

[[Flush TMNG nickname *name*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1418414265}

[[下刷设备名称]{style="font-family:宋体"}]{#struct_0_19361_x3680_x2032389561}

[[Start TMNG smooth.]{lang="EN-US"}]{#struct_0_19361_x3680_1679255849}

[[开始平滑]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1418217657}

[[(MT*index*) *string* level-1 compute tree root nickname *name* to dec.]{lang="EN-US"}]{#struct_0_19361_x3680_979061005}

[[向]{style="font-family:宋体"}[DEC]{lang="EN-US"}]{#struct_0_19361_x3680_x1625524721}[更新]{style="font-family:宋体"}[level-1]{lang="EN-US"}[计算树根，]{style="font-family:宋体"}*[index]{lang="EN-US"}*[拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[:Add/Delete/Modify]{lang="EN-US"}[，]{style="font-family:宋体"}*[name]{lang="EN-US"}*[表示名字]{style="font-family:宋体"}

[[Notifing the TRILL interface state changed.]{lang="EN-US"}]{#struct_0_19361_x3680_x1418283193}

[[通知其它线程]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_x282776811}[接口状态改变]{style="font-family:宋体"}

[[Refresh the TRILL interface parameter on interface: *port*]{lang="EN-US"}]{#struct_0_19361_x3680_x1418086585}

[[刷新]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_1277301831}[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[下保存的接口的各种参数]{style="font-family:宋体"}

[[LSP MTU change from *value1* to *value2*, notify UPDT MTU change.]{lang="EN-US"}]{#struct_0_19361_x3680_156549266}

[[通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}]{#struct_0_19361_x3680_x1418152121}[模块]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文发送的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大小由]{style="font-family:宋体"}*[value1]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[value2]{lang="EN-US"}*

[[Receive *event* event on interface: *port.*]{lang="EN-US"}]{#struct_0_19361_x3680_x298893332}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x1678391079}[收到]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[board insert event]{lang="EN-US"}]{#struct_0_19361_x3680_x1417955513}[：表示板插入事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[board remove event]{lang="EN-US"}]{#struct_0_19361_x3680_x541960621}[：表示板拔出事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface add event]{lang="EN-US"}]{#struct_0_19361_x3680_x1418021049}[：表示接口添加事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface delete event]{lang="EN-US"}]{#struct_0_19361_x3680_606657738}[：表示接口删除事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN \--\> UP event]{lang="EN-US"}]{#struct_0_19361_x3680_x254712393}[：表示接口]{lang="EN-US" style="font-family:
  宋体"}[UP]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP \--\> DOWN event]{lang="EN-US"}]{#struct_0_19361_x3680_x1417824441}[：表示接口]{lang="EN-US" style="font-family:
  宋体"}[DOWN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[speed change event]{lang="EN-US"}]{#struct_0_19361_x3680_634795917}[：表示接口速率变化事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MTU change event]{lang="EN-US"}]{#struct_0_19361_x3680_x1417889977}[：表示]{lang="EN-US" style="font-family:
  宋体"}[MTU]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN add event]{lang="EN-US"}]{#struct_0_19361_x3680_x934216406}[：表示接口加入]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN delete event]{lang="EN-US"}]{#struct_0_19361_x3680_x1418348732}[：表示接口离开]{lang="EN-US" style="font-family:
  宋体"}[VLAN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AVF VLAN change event]{lang="EN-US"}]{#struct_0_19361_x3680_1064207818}[：表示接口]{lang="EN-US" style="font-family:
  宋体"}[AVF]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[designated VLAN change event]{lang="EN-US"}]{#struct_0_19361_x3680_x464419766}[：表示接口指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:宋体"}

[[Receive IFM EPOLLHUP event.]{lang="EN-US"}]{#struct_0_19361_x3680_x1418414268}

[[收到接口管理模块的]{style="font-family:宋体"}[EPOLL]{lang="EN-US"}]{#struct_0_19361_x3680_1146832488}[异常事件]{style="font-family:宋体"}

[[Reconnect to *module* daemon successful, Please wait\...]{lang="EN-US"}]{#struct_0_19361_x3680_x1418217660}

[[和]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_19361_x3680_1382411068}[模块连接成功，请等待。]{style="font-family:宋体"}*[module]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IFM]{lang="EN-US"}]{#struct_0_19361_x3680_x1418283196}[：表示接口管理模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[KERNEL]{lang="EN-US"}]{#struct_0_19361_x3680_476738076}[：表示内核模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEV]{lang="EN-US"}]{#struct_0_19361_x3680_380386979}[：表示设备管理模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MCS]{lang="EN-US"}]{#struct_0_19361_x3680_x1418086588}[：表示二层组播模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_2036816718}[：表示]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[管理模块]{lang="EN-US" style="font-family:宋体"}

[[Reset finished, process with reset code *code.*]{lang="EN-US"}]{#struct_0_19361_x3680_x1418152124}

[[复位完成，处理原因码]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_19361_x3680_x1058408219}[引起的复位。]{style="font-family:宋体"}*[code]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_x1417955516}[：表示]{lang="EN-US" style="font-family:宋体"}[reset TRILL]{lang="EN-US"}[命令引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_19361_x3680_x1301475508}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号翻转引起的复位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_19361_x3680_x1418021052}[：表示]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_19361_x3680_1816576855}[：表示协议进程降级引起的复位]{style="font-family:宋体"}

[[Reset processing with backinfo: module *module*, event *event*, phase *phase*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1417824444}

[[处理]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_19361_x3680_1038080444}[模块回复的]{style="font-family:宋体"}[reset]{lang="EN-US"}[完成事件，事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，阶段为]{style="font-family:宋体"}*[phase]{lang="EN-US"}*[。]{style="font-family:宋体"}*[module]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_19361_x3680_1095898399}[：表示]{lang="EN-US" style="font-family:宋体"}[ADJ]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_x1417889980}[：表示]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_19361_x3680_x1693403613}[：表示]{lang="EN-US" style="font-family:宋体"}[DEC]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[*[event]{lang="EN-US"}*]{#struct_0_19361_x3680_x1418348731}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_19361_x3680_1467492345}[：表示]{lang="EN-US" style="font-family:宋体"}[STOP WORK]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_x1418414267}[：表示]{lang="EN-US" style="font-family:宋体"}[DISABLE]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_19361_x3680_1099778321}[：表示]{lang="EN-US" style="font-family:宋体"}[ENABLE]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[*[phase]{lang="EN-US"}*]{#struct_0_19361_x3680_x1418217659}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_19361_x3680_x539968769}[：表示]{lang="EN-US" style="font-family:宋体"}[STOP WORK]{lang="EN-US"}[阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_x1418283195}[：表示]{lang="EN-US" style="font-family:宋体"}[DISABLE]{lang="EN-US"}[阶段]{lang="EN-US" style="font-family:宋体"}

[[Reset change into phase *phase*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1418086587}

[[复位进入]{style="font-family:宋体"}*[phase]{lang="EN-US"}*]{#struct_0_19361_x3680_x1854866051}[阶段。]{style="font-family:宋体"}*[phase]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_19361_x3680_x1418152123}[：表示]{lang="EN-US" style="font-family:宋体"}[STOP WORK]{lang="EN-US"}[阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_x1461692746}[：表示]{lang="EN-US" style="font-family:宋体"}[DISABLE]{lang="EN-US"}[阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_19361_x3680_x1417955515}[：表示]{lang="EN-US" style="font-family:宋体"}[FINAL]{lang="EN-US"}[阶段]{lang="EN-US" style="font-family:宋体"}

[[Reset processing receive event *event*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1704760035}

[[收到复位事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_19361_x3680_x1418021051}[。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_250492914}[：表示]{lang="EN-US" style="font-family:宋体"}[reset TRILL]{lang="EN-US"}[命令引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_19361_x3680_x1417824443}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号翻转引起的复位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_19361_x3680_x528003497}[：表示]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_19361_x3680_x1417889979}[：表示协议进程降级引起的复位]{style="font-family:宋体"}

[[Reset start up.]{lang="EN-US"}]{#struct_0_19361_x3680_228583008}

[[复位开始]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1418348734}

[[Receive SIGKILL signal from SCM.]{lang="EN-US"}]{#struct_0_19361_x3680_1870776872}

[[从]{style="font-family:宋体"}[SCM]{lang="EN-US"}]{#struct_0_19361_x3680_x1418414270}[模块接收到]{style="font-family:宋体"}[SIGKILL]{lang="EN-US"}[信号]{style="font-family:宋体"}

[[Receive *module* EPOLLHUP or EPOLLERR event.]{lang="EN-US"}]{#struct_0_19361_x3680_1503128384}

[[从]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_19361_x3680_x1418217662}[模块接收到]{style="font-family:宋体"}[EPOLLHUP]{lang="EN-US"}[事件。]{style="font-family:宋体"}*[module]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IFM]{lang="EN-US"}]{#struct_0_19361_x3680_x1418283198}[：表示接口管理模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[KERNEL]{lang="EN-US"}]{#struct_0_19361_x3680_1639537490}[：表示内核模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEV]{lang="EN-US"}]{#struct_0_19361_x3680_x1418086590}[：表示设备管理模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MCS]{lang="EN-US"}]{#struct_0_19361_x3680_1680651894}[：表示二层组播模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x1418152126}[：表示]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[管理模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MemAlert]{lang="EN-US"}]{#struct_0_19361_x3680_2073759663}[：表示门限告警模块]{style="font-family:宋体"}

[*[Action]{lang="EN-US"}*[ compute tree list to dec.]{lang="EN-US"}]{#struct_0_19361_x3680_x1417955518}

[[向路由计算]{style="font-family:宋体"}*[Action]{lang="EN-US"}*]{#struct_0_19361_x3680_x1751814202}[计算的分发树列表。]{style="font-family:宋体"}*[ActionType]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_19361_x3680_x1418021054}[：表示添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_19361_x3680_x1417824446}[：表示删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Modify]{lang="EN-US"}]{#struct_0_19361_x3680_x124718970}[：表示更新]{lang="EN-US" style="font-family:宋体"}

[[Get *TreeNum* nickname(s) for distribution tree root list.]{lang="EN-US"}]{#struct_0_19361_x3680_x1417889982}

[[为分发树树根列表获取]{style="font-family:宋体"}*[TreeNum]{lang="EN-US"}*]{#struct_0_19361_x3680_x530604199}[个]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[The highest priority tree root takes *NickNum* nickname(s), needs *Number*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1418348733}

[[最高优先级树根携带]{style="font-family:宋体"}*[NickNum]{lang="EN-US"}*]{#struct_0_19361_x3680_x1418414269}[个]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[，需要]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[个]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging trill graceful-restart]{lang="EN-US"}]{#struct_0_19361_x3680_x419251453}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x16503698}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_x828285605}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_342860517}

[[Stop level-1 T1 timer.]{lang="EN-US"}]{#struct_0_19361_x3680_x1268003372}

[[停止]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_x1172108385}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[Receive level-1 hello with RR bit set from circuit(*port*) in vlan 10, Ignored.]{lang="EN-US"}]{#struct_0_19361_x3680_1434309661}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x1418217661}[上收到]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[中]{style="font-family:宋体"}[RR]{lang="EN-US"}[位置位的]{style="font-family:宋体"}[Level-1 Hello]{lang="EN-US"}[报文（非指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[下收到的），忽略该报文]{style="font-family:宋体"}

[[Receive level-1 hello with RR bit set from circuit(*port*) in vlan 10.]{lang="EN-US"}]{#struct_0_19361_x3680_x183672873}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_147741687}[上收到]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[中]{style="font-family:宋体"}[RR]{lang="EN-US"}[位置位的]{style="font-family:宋体"}[Level-1 Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Receive level-1 hello with RA bit set from circuit(*port*).]{lang="EN-US"}]{#struct_0_19361_x3680_1935208482}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x1092765139}[上收到]{style="font-family:宋体"}[RA]{lang="EN-US"}[位置位的]{style="font-family:宋体"}[Level-1 Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Level-1 neighbor(*neighbor*) SA bit set, adjacency not advertised.]{lang="EN-US"}]{#struct_0_19361_x3680_x1418283197}

[[Level-1]{lang="EN-US"}]{#struct_0_19361_x3680_2042822017}[的邻居]{style="font-family:宋体"}*[neighbor]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置位，抑制邻居路由发布]{style="font-family:宋体"}

[[Level-1 neighbor(*neighbor*) SA bit clear, adjacency advertised.]{lang="EN-US"}]{#struct_0_19361_x3680_x2009117416}

[[Level-1]{lang="EN-US"}]{#struct_0_19361_x3680_x426175987}[的邻居]{style="font-family:宋体"}*[neighbor]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[位未置位，不抑制邻居路由发布]{style="font-family:宋体"}

[[Receive level-1 hello with SA bit changed from circuit(*port*) in VLAN 1.]{lang="EN-US"}]{#struct_0_19361_x3680_905159420}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x1418086589}[上收到]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置位情况已改变的]{style="font-family:宋体"}[Level-1 Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface(*port*) level-1 T1 timer expiration count: 2.]{lang="EN-US"}]{#struct_0_19361_x3680_x692066637}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x349172103}[上]{style="font-family:宋体"}[level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[次]{style="font-family:宋体"}

[[Level-1T1 timer has stopped.]{lang="EN-US"}]{#struct_0_19361_x3680_1514350485}

[[Level-1]{lang="EN-US"}]{#struct_0_19361_x3680_1565984063}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器停止]{style="font-family:宋体"}

[[Notify SPF calculate completed,Calc Type: *number*]{lang="EN-US"}]{#struct_0_19361_x3680_x1418152125}

[[通知]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_19361_x3680_1670475136}[计算完毕。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_19361_x3680_1429508694}[：表示]{lang="EN-US" style="font-family:宋体"}[单播路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_1045813278}[：表示组播路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_19361_x3680_x1417955517}[：表示单播、组播路由一起通知]{style="font-family:宋体"}

[[Notify SPF calculate,Calc Type: *number*]{lang="EN-US"}]{#struct_0_19361_x3680_1427407847}

[[通知进行]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_19361_x3680_x725893443}[计算。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_19361_x3680_225927080}[：表示]{lang="EN-US" style="font-family:宋体"}[单播路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_x1418021053}[：表示组播路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_19361_x3680_x912306500}[：表示单播、组播路由一起通知]{style="font-family:宋体"}

[[Failed to purge LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x246236302}

[[清除]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x1214491382}[失败]{style="font-family:宋体"}

[[Begin to purge local LSP.]{lang="EN-US"}]{#struct_0_19361_x3680_x1417824445}

[[开始清除本地]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x1690802911}

[[Purge LSP *id*.*pseudo*-n*um*.]{lang="EN-US"}]{#struct_0_19361_x3680_2119390509}

[[清除]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}]{#struct_0_19361_x3680_x392366079}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[[End to purge local LSP.]{lang="EN-US"}]{#struct_0_19361_x3680_x1417889981}

[[清除本地]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x127319672}[结束]{style="font-family:宋体"}

[[LSDB synchronization is complete]{lang="EN-US"}]{#struct_0_19361_x3680_x1813308815}

[[LSDB]{lang="EN-US"}]{#struct_0_19361_x3680_x1599285797}[同步完成]{style="font-family:宋体"}

[[CSNP set synchronization is complete on circuit  *port*.]{lang="EN-US"}]{#struct_0_19361_x3680_147735211}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_45227617}[上]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[同步完成]{style="font-family:宋体"}

[[Graceful-restart complete.]{lang="EN-US"}]{#struct_0_19361_x3680_x586835936}

[[平滑重启完成]{style="font-family:宋体"}]{#struct_0_19361_x3680_147669675}

[[T3 timer is stoped.]{lang="EN-US"}]{#struct_0_19361_x3680_x1204752286}

[[T3]{lang="EN-US"}]{#struct_0_19361_x3680_1260376804}[定时器停止]{style="font-family:宋体"}

[[Enter MCS synchronization phase.]{lang="EN-US"}]{#struct_0_19361_x3680_417795985}

[[进入]{style="font-family:宋体"}[MCS]{lang="EN-US"}]{#struct_0_19361_x3680_147866283}[同步阶段]{style="font-family:宋体"}

[[Enter SPF phase.]{lang="EN-US"}]{#struct_0_19361_x3680_x574153224}

[[进入]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_19361_x3680_x1994033512}[阶段]{style="font-family:宋体"}

[[T3 timer expired before T2 timer.]{lang="EN-US"}]{#struct_0_19361_x3680_147800747}

[[T3]{lang="EN-US"}]{#struct_0_19361_x3680_1019182099}[定时器比]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器提前超时]{style="font-family:宋体"}

[[Level-1 T2 timer expired.]{lang="EN-US"}]{#struct_0_19361_x3680_1764301769}

[[Level-1]{lang="EN-US"}]{#struct_0_19361_x3680_147997355}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Graceful-restart enter *type*.]{lang="EN-US"}]{#struct_0_19361_x3680_1440393344}

[[开始]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_19361_x3680_2107756378}[类型的平滑重启。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Starting]{lang="EN-US"}]{#struct_0_19361_x3680_x740556667}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Restarting]{lang="EN-US"}]{#struct_0_19361_x3680_147931819}

[[Receive T2 timer cancel event]{lang="EN-US"}]{#struct_0_19361_x3680_x884371381}

[[收到停止]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_19361_x3680_x869418708}[定时器的事件]{style="font-family:宋体"}

[[Level-1 T2 timer is stopped.]{lang="EN-US"}]{#struct_0_19361_x3680_148128427}

[[Level-1]{lang="EN-US"}]{#struct_0_19361_x3680_899828257}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器停止]{style="font-family:宋体"}

[[Receive Mcs notify back flag: *number*]{lang="EN-US"}]{#struct_0_19361_x3680_148062891}

[[收到获取二层组播数据完毕。]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_19361_x3680_x2126065065}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_19361_x3680_893189741}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_19361_x3680_148259499}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}

[[Enter LSP generation phase.]{lang="EN-US"}]{#struct_0_19361_x3680_812730692}

[[进入]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x1425447790}[生成阶段]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging trill ha]{lang="EN-US"}]{#struct_0_19361_x3680_148193963}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x253231058}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_197346829}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_509251506}

[[RtBackup TRILL *string.*]{lang="EN-US"}]{#struct_0_19361_x3680_x1118722591}

[[实时备份]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_x1759245230}[的各种配置和属性信息。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process enable]{lang="EN-US"}]{#struct_0_19361_x3680_x137354662}[：表示]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议进程使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Debugging information]{lang="EN-US"}]{#struct_0_19361_x3680_147735212}[：调试信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HA Debugging information]{lang="EN-US"}]{#struct_0_19361_x3680_45227618}[：]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface enable]{lang="EN-US"}]{#struct_0_19361_x3680_222468128}[：表示接口使能]{lang="EN-US" style="font-family:
  宋体"}[TRILL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[distribution tree number]{lang="EN-US"}]{#struct_0_19361_x3680_1891146804}[：表示分发树数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[distribution tree priority]{lang="EN-US"}]{#struct_0_19361_x3680_x76135996}[：表示分发树优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP refresh Interval]{lang="EN-US"}]{#struct_0_19361_x3680_147669676}[：表示]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[刷新间隔]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP life time]{lang="EN-US"}]{#struct_0_19361_x3680_x1204752287}[：表示]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[生命周期]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log peer change]{lang="EN-US"}]{#struct_0_19361_x3680_x305707137}[：表示]{lang="EN-US" style="font-family:
  宋体"}[TRILL]{lang="EN-US"}[邻接状态输出开关]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HELLO time interval]{lang="EN-US"}]{#struct_0_19361_x3680_1975078745}[：表示]{lang="EN-US" style="font-family:
  宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CSNP interval]{lang="EN-US"}]{#struct_0_19361_x3680_x31616973}[：表示发送]{lang="EN-US" style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HELLO lapse number]{lang="EN-US"}]{#struct_0_19361_x3680_147866284}[：表示邻居的]{lang="EN-US" style="font-family:
  宋体"}[Hello]{lang="EN-US"}[报文失效数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DRB priority]{lang="EN-US"}]{#struct_0_19361_x3680_x574153225}[：表示接口]{lang="EN-US" style="font-family:宋体"}[DRB]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[link type]{lang="EN-US"}]{#struct_0_19361_x3680_x1994099048}[：表示]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[端口类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AVF inhibited time]{lang="EN-US"}]{#struct_0_19361_x3680_x690594789}[：表示]{lang="EN-US" style="font-family:
  宋体"}[AVF]{lang="EN-US"}[检测到冲突时抑制自己的时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP throttle time and LSP throttle count]{lang="EN-US"}]{#struct_0_19361_x3680_147800748}[：表示发送链路状态报文的最小时间间隔和一次最多发送的链路状态报文的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_1019182086}[：表示]{lang="EN-US" style="font-family:宋体"}[RB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface delete]{lang="EN-US"}]{#struct_0_19361_x3680_1763974088}[：表示删除接口]{style="font-family:宋体"}

[[Reconnect to HA daemon successful.]{lang="EN-US"}]{#struct_0_19361_x3680_1329210648}

[[重新连接]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_19361_x3680_147997356}[守护进程成功]{style="font-family:宋体"}

[[Receive HA EPOLLHUP or EPOLLERR event.]{lang="EN-US"}]{#struct_0_19361_x3680_1440393341}

[[收到]{style="font-family:宋体"}[HAEPOLLHUP]{lang="EN-US"}]{#struct_0_19361_x3680_2107559770}[或]{style="font-family:宋体"}[EPOLLERR]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[HA upgrade, start TMNG smooth.]{lang="EN-US"}]{#struct_0_19361_x3680_416559360}

[[HA]{lang="EN-US"}]{#struct_0_19361_x3680_147931820}[升级，开始平滑]{style="font-family:宋体"}

[[Receive TRILL real-time backup data.]{lang="EN-US"}]{#struct_0_19361_x3680_1836617810}

[[收到]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_655275783}[实备数据]{style="font-family:宋体"}

[[Receive TRILL batch backup data.]{lang="EN-US"}]{#struct_0_19361_x3680_813028938}

[[收到]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_148128428}[批量备份数据]{style="font-family:宋体"}

[[Receive HA *event* event.]{lang="EN-US"}]{#struct_0_19361_x3680_899828248}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_19361_x3680_x1202157238}[通知事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[batch backup]{lang="EN-US"}]{#struct_0_19361_x3680_x1110024116}[：表示批量备份事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stop]{lang="EN-US"}]{#struct_0_19361_x3680_148062892}[：表示进程停止事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[degrade]{lang="EN-US"}]{#struct_0_19361_x3680_x2126065066}[：表示降级事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[upgrade]{lang="EN-US"}]{#struct_0_19361_x3680_x672894200}[：表示升级事件]{lang="EN-US" style="font-family:宋体"}

[[Receive Memory High/Low Threshold event.]{lang="EN-US"}]{#struct_0_19361_x3680_148259500}

[[收到内存高]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_x1562657322}[低门限事件]{style="font-family:宋体"}

[[Send batch backup data to slave board.]{lang="EN-US"}]{#struct_0_19361_x3680_x1127723469}

[[发送批量备份数据到备板]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1393381174}

[[Notifying thread to stop work.]{lang="EN-US"}]{#struct_0_19361_x3680_148193964}

[[通知线程停止工作]{style="font-family:宋体"}]{#struct_0_19361_x3680_197346834}

[[Processing the HA upgrade.]{lang="EN-US"}]{#struct_0_19361_x3680_x1829400665}

[[处理]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_19361_x3680_147735209}[升级事件]{style="font-family:宋体"}

[[Notifying thread to start work.]{lang="EN-US"}]{#struct_0_19361_x3680_x1911087527}

[[通知线程开始工作]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1056399759}

[[Start up TRILL protocol process.]{lang="EN-US"}]{#struct_0_19361_x3680_x1653577583}

[[开始启动]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_147669673}[协议进程]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging trill self-originate-update]{lang="EN-US"}]{#struct_0_19361_x3680_x1204752284}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x256076690}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_97577390}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_x1013430664}

[[Purging level-1 LSP \[]{lang="EN-US"}*[id]{lang="EN-US"}*[.*pseudo*-*num*]{lang="EN-US"}[\].]{lang="EN-US"}]{#struct_0_19361_x3680_377809553}

[[清除]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_147866281}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[*[String]{lang="EN-US"}*[ into level-1 LSPs, TLV: *TlvType*.]{lang="EN-US"}]{#struct_0_19361_x3680_x574153222}

[[在]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_x1994164584}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[ TLV]{lang="EN-US"}[。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adding router capability]{lang="EN-US"}]{#struct_0_19361_x3680_x1678412581}[：表示添加路由能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adding neighbor]{lang="EN-US"}]{#struct_0_19361_x3680_1249835503}[：表示添加邻居]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adding group address]{lang="EN-US"}]{#struct_0_19361_x3680_147800745}[：表示添加组地址]{lang="EN-US" style="font-family:
  宋体"}

[[The remaining space of level-1 fragment 0 LSP is shortage.]{lang="EN-US"}]{#struct_0_19361_x3680_1019182097}

[[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_1763908553}[的零分片]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中剩余空间不足]{style="font-family:宋体"}

[[level-1 LSP over flow.]{lang="EN-US"}]{#struct_0_19361_x3680_1386327503}

[[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_860280166}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[已满]{style="font-family:宋体"}

[[LSP lifetime change triggers rebuild.]{lang="EN-US"}]{#struct_0_19361_x3680_147997353}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_1440393338}[生存事件改变出发重建]{style="font-family:宋体"}

[[The remaining space of level-1 fragment 0 LSP is shortage while adding area or protocol support.]{lang="EN-US"}]{#struct_0_19361_x3680_2108018529}

[[当添加区域地址或协议支持时]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_x1725514685}[的零分片]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中剩余空间不足]{style="font-family:宋体"}

[[Rebuilding all level-1 LSPs Start.]{lang="EN-US"}]{#struct_0_19361_x3680_147931817}

[[开始对]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_x884371375}[的所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[进行]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{style="font-family:宋体"}

[[Rebuilding all level-1 LSPs end.]{lang="EN-US"}]{#struct_0_19361_x3680_x869680853}

[[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_x1460067959}[所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作结束]{style="font-family:宋体"}

[[MTU change triggers rebuild.]{lang="EN-US"}]{#struct_0_19361_x3680_334960958}

[[MTU]{lang="EN-US"}]{#struct_0_19361_x3680_148128425}[改变触发]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{style="font-family:宋体"}

[[Attempting to exceed max sequence number.]{lang="EN-US"}]{#struct_0_19361_x3680_899828259}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_1136494923}[的序列号超过最大值（需要反转）]{style="font-family:宋体"}

[[Generating level-1 LSP \[*id*.*pseudo*-*num*\], Seq *number*, length *length*.]{lang="EN-US"}]{#struct_0_19361_x3680_x470138323}

[[生成序列号为]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_19361_x3680_148062889}[、长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}[level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[[TLV handle triggers rebuild.]{lang="EN-US"}]{#struct_0_19361_x3680_x169749921}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_2137977132}[处理触发]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{style="font-family:宋体"}

[[Added level-1 area address *String*.]{lang="EN-US"}]{#struct_0_19361_x3680_x92427907}

[[为]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_148259497}[添加区域地址]{style="font-family:宋体"}[String]{lang="EN-US"}

[[Deleted level-1 area address *String.*]{lang="EN-US"}]{#struct_0_19361_x3680_812730678}

[[为]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_193160348}[添加区域地址]{style="font-family:宋体"}[String]{lang="EN-US"}

[[Added/Deleted level-1 protocol support *ProNumber*(*ProString*).]{lang="EN-US"}]{#struct_0_19361_x3680_x781743748}

[[为]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_148193961}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除支持的协议类型]{style="font-family:宋体"}*[ProNumber]{lang="EN-US"}*[(*ProString*)]{lang="EN-US"}

[[Added/Deleted/Modified level-1 neighbour: system *system* =\> neighbour *neighbour*.]{lang="EN-US"}]{#struct_0_19361_x3680_197346831}

[[为]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_x1829400662}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新由]{style="font-family:宋体"}*[system]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighbour]{lang="EN-US"}*[的邻居信息]{style="font-family:宋体"}

[[Added/Deleted level-1 pseudo neighbour: pseudo *pseudo* =\> neighbour *neighbour*.]{lang="EN-US"}]{#struct_0_19361_x3680_147735210}

[[为]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_45227616}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除由]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighbour]{lang="EN-US"}*[的伪节点邻居信息]{style="font-family:宋体"}

[[Added/Deleted group address for vlan *vlan-id*.]{lang="EN-US"}]{#struct_0_19361_x3680_1369479200}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_147669674}[删除]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[的组地址信息]{style="font-family:宋体"}

[[Deleted all group address for vlan *vlan-id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1204752285}

[[删除]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_x1468506551}[下的所有组地址信息]{style="font-family:宋体"}

[[Failed to delete all group address for vlan *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_x750017100}

[[删除]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_147866282}[下的所有组地址信息失败]{style="font-family:宋体"}

[[Added trill version.]{lang="EN-US"}]{#struct_0_19361_x3680_x574153223}

[[添加]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_x1994230120}[版本信息]{style="font-family:宋体"}

[[Failed to add trill version.]{lang="EN-US"}]{#struct_0_19361_x3680_147800746}

[[添加]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_1019182100}[版本信息失败]{style="font-family:宋体"}

[[Added/Deleted/Modified local nickname *local*.]{lang="EN-US"}]{#struct_0_19361_x3680_x574809136}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_147997354}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新本地]{style="font-family:宋体"}[Nickname *local*]{lang="EN-US"}

[[Failed to add/delete/modify local nickname *local*.]{lang="EN-US"}]{#struct_0_19361_x3680_1440393343}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_2107690842}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新本地]{style="font-family:宋体"}[Nickname *local*]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Modified trees information.]{lang="EN-US"}]{#struct_0_19361_x3680_147931818}

[[更新分发树计算信息]{style="font-family:宋体"}]{#struct_0_19361_x3680_x884371382}

[[Failed to modify trees information.]{lang="EN-US"}]{#struct_0_19361_x3680_x869615316}

[[更新分发树计算信息失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_148128426}

[[Added/Deleted tree root nickname *local*.]{lang="EN-US"}]{#struct_0_19361_x3680_899828258}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_1136494922}[删除树根]{style="font-family:宋体"}[Nickname *local*]{lang="EN-US"}

[[Failed to add/delete tree root nickname *local*.]{lang="EN-US"}]{#struct_0_19361_x3680_148062890}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_x2126065064}[删除树根]{style="font-family:宋体"}[Nickname *local*]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Added/Deleted/Modified interested vlan(start *start*, end *end*).]{lang="EN-US"}]{#struct_0_19361_x3680_148259498}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_812730691}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新关注的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围为]{style="font-family:宋体"}*[start]{lang="EN-US"}*[到]{style="font-family:宋体"}*[end]{lang="EN-US"}*

[[Failed to add/delete/modify interested vlan(start *start*, end *end*).]{lang="EN-US"}]{#struct_0_19361_x3680_x1425447789}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_148193962}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新关注的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[失败，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围为]{style="font-family:宋体"}*[start]{lang="EN-US"}*[到]{style="font-family:宋体"}*[end]{lang="EN-US"}*

[[Modified nickname in all interested vlans.]{lang="EN-US"}]{#struct_0_19361_x3680_197346828}

[[更新所有关注]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_509251507}[中的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}

[[Failed to modify nickname in all interested vlans.]{lang="EN-US"}]{#struct_0_19361_x3680_147735207}

[[更新所有关注]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x1911087521}[中的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to add MAC TLV for VLAN *vlan-id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1862968813}

[[为]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_147669671}[添加]{style="font-family:宋体"}[MAC TLV]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Delete GMAC TLV for VLAN *vlan-id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1204752282}

[[为]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_x708991664}[删除]{style="font-family:宋体"}[GMAC TLV]{lang="EN-US"}

[[Generated nickname is *local*.]{lang="EN-US"}]{#struct_0_19361_x3680_147866279}

[[生成的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_x911860222}[为]{style="font-family:宋体"}*[local]{lang="EN-US"}*

[[Local nickname is valid, nickname is *local*.]{lang="EN-US"}]{#struct_0_19361_x3680_147800743}

[[本地]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_1019182095}[为有效值，为]{style="font-family:宋体"}*[local]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging trill timer]{lang="EN-US"}]{#struct_0_19361_x3680_1764039625}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x264555954}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_1249649552}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_905862402}

[[Level-1 adjacency *SystemId* hold timer expired on the circuit *CircName*.]{lang="EN-US"}]{#struct_0_19361_x3680_147997351}

[[在链路]{style="font-family:宋体"}*[CircName]{lang="EN-US"}*]{#struct_0_19361_x3680_1440393340}[上的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[邻居]{style="font-family:宋体"}[Holdtime]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[(M*Number*) Start SPF timer, value is *value* ms.]{lang="EN-US"}]{#struct_0_19361_x3680_2107494234}

[[（拓扑]{style="font-family:宋体"}*[Number]{lang="EN-US"}*]{#struct_0_19361_x3680_x1542985124}[）启动]{style="font-family:宋体"}[SPF]{lang="EN-US"}[定时器，其值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[(M*Number*) Stop SPF timer.]{lang="EN-US"}]{#struct_0_19361_x3680_x776761253}

[[（拓扑]{style="font-family:宋体"}*[Number]{lang="EN-US"}*]{#struct_0_19361_x3680_147931815}[）停止]{style="font-family:宋体"}[SPF]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[(M*Number*) SPF timer expired.]{lang="EN-US"}]{#struct_0_19361_x3680_x884371377}

[[（拓扑]{style="font-family:宋体"}*[Number]{lang="EN-US"}*]{#struct_0_19361_x3680_x869811925}[）的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Starting timer for reconnect to HA/IFM daemon, time value is *value* ms.]{lang="EN-US"}]{#struct_0_19361_x3680_x1080781211}

[[开启重连]{style="font-family:宋体"}[HA/IFM]{lang="EN-US"}]{#struct_0_19361_x3680_x1086560018}[定时器，其值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Starting HA upgrade waiting timer for reset complete.]{lang="EN-US"}]{#struct_0_19361_x3680_x1319873629}

[[为重启开始]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_19361_x3680_148128423}[升级等待定时器]{style="font-family:宋体"}

[[Stop waiting timer for max sequence number exceed/smooth end, timer ID is *value*.]{lang="EN-US"}]{#struct_0_19361_x3680_899828253}

[[超过最大序列号]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_1136494917}[平滑结束停止等待定时器，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Starting waiting timer for max seq num exceed/smooth end, time value is *value* ms.]{lang="EN-US"}]{#struct_0_19361_x3680_x469876182}

[[启动]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_1659428210}[序列号达到最大值]{style="font-family:宋体"}[/smooth end]{lang="EN-US"}[的翻转等待定时器，其值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Level-1 *type* timer expired on the circuit CSNP/PSNP.]{lang="EN-US"}]{#struct_0_19361_x3680_148062887}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x169749935}[下的]{style="font-family:宋体"}[level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP/PSNP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Level-1 flood timer expired on the circuit *String*.]{lang="EN-US"}]{#struct_0_19361_x3680_2137714989}

[[接口]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_19361_x3680_x1288096249}[下的]{style="font-family:宋体"}[level-1]{lang="EN-US"}[泛洪定时器超时]{style="font-family:宋体"}

[[Level-1 LSP \[*id*.*pseudo*-*num*\] gen timer expired.]{lang="EN-US"}]{#struct_0_19361_x3680_148259495}

[[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_812730680}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成定时器超时。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[[Start level-1 LSP \[*id*.*pseudo*-*num*\] gen timer, time vlaue is *value*(ms).]{lang="EN-US"}]{#struct_0_19361_x3680_913204372}

[[启动]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_912631616}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成定时器，其值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[毫秒。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[[Stop level-1 LSP \[*id*.*pseudo*-*num*\] gen timer.]{lang="EN-US"}]{#struct_0_19361_x3680_148193959}

[[停止]{style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_19361_x3680_1771324951}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成定时器。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging trill vr]{lang="EN-US"}]{#struct_0_19361_x3680_x1396577940}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1579366859}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_x1396512404}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_x1539374461}

[[Interface state is down, ignore *event* event.]{lang="EN-US"}]{#struct_0_19361_x3680_x832618685}

[[接口状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_19361_x3680_x1396709012}[，忽略]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[track positive]{lang="EN-US"}]{#struct_0_19361_x3680_x1707172004}[：]{lang="EN-US" style="font-family:宋体"}[探测到链路有效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[track negative]{lang="EN-US"}]{#struct_0_19361_x3680_x1396643476}[：]{lang="EN-US" style="font-family:宋体"}[探测到链路无效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[track notready]{lang="EN-US"}]{#struct_0_19361_x3680_1637068040}[：探测到链路尚未就绪]{style="font-family:宋体"}

[*[Event]{lang="EN-US"}*[ track event on VLAN interface: *ifindex*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1395791508}

[[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x293310577}[接口收到]{style="font-family:宋体"}*[event]{lang="EN-US"}*[探测事件，接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deregister]{lang="EN-US"}]{#struct_0_19361_x3680_x1395725972}[：]{lang="EN-US" style="font-family:宋体"}[撤消注册]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}[egister]{lang="EN-US"}]{#struct_0_19361_x3680_1586158734}[：注册]{style="font-family:
  宋体"}

[[Batch deregister track event on VLAN interface: *ifindex.*]{lang="EN-US"}]{#struct_0_19361_x3680_x1396315803}

[[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_2139715362}[接口收到批量撤销注册探测事件，接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*

[[Flush TMNG the *role* role.]{lang="EN-US"}]{#struct_0_19361_x3680_x270220934}

[[向]{style="font-family:宋体"}[TMNG]{lang="EN-US"}]{#struct_0_19361_x3680_x1396250267}[下刷]{style="font-family:宋体"}*[role]{lang="EN-US"}*[角色。]{style="font-family:宋体"}[role]{lang="EN-US"}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[normal]{lang="EN-US"}]{#struct_0_19361_x3680_71772568}[：]{lang="EN-US" style="font-family:宋体"}[普通]{style="font-family:宋体"}[RB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[gateway]{lang="EN-US"}]{#struct_0_19361_x3680_x1396446875}[：网关]{style="font-family:宋体"}[设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[access]{lang="EN-US"}]{#struct_0_19361_x3680_x695256975}[：]{style="font-family:宋体"}[二层接入设备]{lang="EN-US" style="font-family:宋体"}

[[Current system\'s role is not gateway.]{lang="EN-US"}]{#struct_0_19361_x3680_x1396381339}

[[当前系统角色不是网关]{style="font-family:宋体"}]{#struct_0_19361_x3680_145279374}

[[All gateway TLVs have been deleted.]{lang="EN-US"}]{#struct_0_19361_x3680_x1396577947}

[[所有网关]{style="font-family:宋体"}]{#struct_0_19361_x3680_2141021995}[TLV]{lang="FR"}[已被删除]{style="font-family:宋体"}

[[Clean TRILL virtual IP information.]{lang="EN-US"}]{#struct_0_19361_x3680_x1396512411}

[[清除]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1942724524}[TRILL]{lang="FR"}[虚拟]{style="font-family:宋体"}[IP]{lang="FR"}[地址信息]{style="font-family:宋体"}

[[Receive *event* event.]{lang="EN-US"}]{#struct_0_19361_x3680_x1396709019}

[[收到]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_19361_x3680_x497318423}[事件。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[track]{lang="EN-US"}]{#struct_0_19361_x3680_x1396643483}[ positive]{lang="EN-US"}[：探测到链路有效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[track]{lang="EN-US"}]{#struct_0_19361_x3680_x1899367409}[ negative]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[探测到链路无效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[track]{lang="EN-US"}]{#struct_0_19361_x3680_x1395791515}[ notready]{lang="EN-US"}[：探测到链路尚未就绪]{style="font-family:宋体"}

[[Real-time backup TRILL VLAN interface *ifname* delete.]{lang="EN-US"}]{#struct_0_19361_x3680_x696660640}

[[删除实时备份的]{style="font-family:宋体"}[TRILL VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x1395725979}[接口]{style="font-family:宋体"}*[Ifname]{lang="EN-US"}*

[[Delete *ifname* data from DBM.]{lang="EN-US"}]{#struct_0_19361_x3680_826643847}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_19361_x3680_x1396315802}[中删除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}*[Ifname]{lang="EN-US"}*[的数据]{style="font-family:宋体"}

[[Receive MAC changing event, disable VR on last VLAN interface: *ifindex*.]{lang="EN-US"}]{#struct_0_19361_x3680_573631421}

[[在最后一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x1396250266}[接口上收到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化事件，接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*

[[Receive MAC changing event on VLAN interface: *ifindex*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1494311373}

[[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x1396446874}[接口上收到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化事件，接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*

[[Receive *event* event on VLAN interface: *ifindex*, VR type: *vrtype*.]{lang="EN-US"}]{#struct_0_19361_x3680_870826966}

[[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_x1396381338}[接口上收到]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件，接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[，]{style="font-family:宋体"}[VR]{lang="EN-US"}[类型为]{style="font-family:宋体"}*[vrtype]{lang="EN-US"}*[。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP \--\> DOWN]{lang="EN-US"}]{#struct_0_19361_x3680_1711363315}[：]{lang="EN-US" style="font-family:宋体"}[接口由]{style="font-family:宋体"}[up]{lang="EN-US"}[变为]{style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN \--\> UP]{lang="EN-US"}]{#struct_0_19361_x3680_x1396577946}[：接口由]{style="font-family:宋体"}[down]{lang="EN-US"}[变为]{style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_19361_x3680_574938054}[：删除接口]{style="font-family:宋体"}

[[The role change: *event*]{lang="EN-US"}]{#struct_0_19361_x3680_x1396512410}

[[角色变化事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_19361_x3680_786158831}[。]{style="font-family:宋体"}*[event]{lang="FR"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[normal \--\> gateway]{lang="EN-US"}]{#struct_0_19361_x3680_x1396709018}[：]{lang="EN-US" style="font-family:
  宋体"}[由普通]{style="font-family:宋体"}[RB]{lang="EN-US"}[变为网关设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[normal \--\> access]{lang="EN-US"}]{#struct_0_19361_x3680_1068765518}[：]{lang="EN-US" style="font-family:
  宋体"}[由普通]{style="font-family:宋体"}[RB]{lang="EN-US"}[变为]{style="font-family:宋体"}[二层接入设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[gateway \--\> access]{lang="EN-US"}]{#struct_0_19361_x3680_x1396643482}[：]{lang="EN-US" style="font-family:
  宋体"}[由网关设备变为]{style="font-family:宋体"}[二层接入设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[gateway \--\> normal]{lang="EN-US"}]{#struct_0_19361_x3680_x333283468}[：]{lang="EN-US" style="font-family:
  宋体"}[由网关设备变为普通]{style="font-family:宋体"}[RB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[access \--\> normal]{lang="EN-US"}]{#struct_0_19361_x3680_x1395791514}[：]{lang="EN-US" style="font-family:
  宋体"}[由]{style="font-family:宋体"}[二层接入设备]{lang="EN-US" style="font-family:宋体"}[变为普通]{style="font-family:宋体"}[RB]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[access \--\> gateway]{lang="EN-US"}]{#struct_0_19361_x3680_2032222715}[：]{lang="EN-US" style="font-family:
  宋体"}[由]{style="font-family:宋体"}[二层接入设备]{lang="EN-US" style="font-family:宋体"}[变为网关设备]{style="font-family:宋体"}

[[Flush TMNG, VLAN *vlanid* enable/disable VR.]{lang="EN-US"}]{#struct_0_19361_x3680_x1395725978}

[[下刷在]{style="font-family:宋体"}[VLAN *vlanid*]{lang="EN-US"}]{#struct_0_19361_x3680_x1799600326}[上使能]{style="font-family:宋体"}[/]{lang="EN-US"}[去使能]{style="font-family:宋体"}[VR]{lang="EN-US"}

[[Add/Delete/Batch delete virtual IP to address daemon.]{lang="EN-US"}]{#struct_0_19361_x3680_x247600514}

[[向]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19361_x3680_x1799534790}[地址模添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[批量删除虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Flush TMNG, add/delete/batch delete virtual IP address.]{lang="EN-US"}]{#struct_0_19361_x3680_x145882517}

[[向内核下刷]{style="font-family:宋体"}[TMNG]{lang="EN-US"}]{#struct_0_19361_x3680_x1799731398}[消息，添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[批量删除虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Start/End to flush virtual IP address to *type* address deamon.]{lang="EN-US"}]{#struct_0_19361_x3680_x899457641}

[[开始]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_x1799665862}[结束下刷虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址到]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址模块]{style="font-family:宋体"}

[[Start/End to flush *event-type*.]{lang="EN-US"}]{#struct_0_19361_x3680_x445066103}

[[开始]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_x1799862470}[结束下刷]{style="font-family:宋体"}*[event]{lang="EN-US"}*[。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN enable VR]{lang="EN-US"}]{#struct_0_19361_x3680_x232669773}[：]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[使能]{style="font-family:宋体"}[VR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[virtyal IP address]{lang="EN-US"}]{#struct_0_19361_x3680_x1799796934}[：]{lang="EN-US" style="font-family:
  宋体"}[虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Notify UPDT to add/delete *info* information.]{lang="EN-US"}]{#struct_0_19361_x3680_x967736041}

[[通知]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1799993542}[UPD]{lang="FR"}[添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}*[info]{lang="EN-US"}*[信息。]{style="font-family:宋体"}*[info]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[virtual IP]{lang="EN-US"}]{#struct_0_19361_x3680_x575354519}[：]{lang="EN-US" style="font-family:宋体"}[虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[gateway]{lang="EN-US"}]{#struct_0_19361_x3680_x1799928006}[：网关信息]{style="font-family:
  宋体"}

[[No valid gateway is elected as main gateway on VR *vrid* (*vrtype*).]{lang="EN-US"}]{#struct_0_19361_x3680_x1799076038}

[[在]{style="font-family:宋体"}]{#struct_0_19361_x3680_x2032520236}[VR]{lang="FR"}[上没有有效的网关被选举为主网关，]{style="font-family:宋体"}[VR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vrid]{lang="EN-US"}*[（]{style="font-family:宋体"}[VR]{lang="EN-US"}[类型为]{style="font-family:宋体"}*[vrtype]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[The first time elected main gateway on VR *vrid* (*vrtype*), main gateway: *systemid*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1799010502}

[[在]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1547368127}[VR]{lang="FR"}[上第一次选举主网关，]{style="font-family:宋体"}[VR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vrid]{lang="EN-US"}*[（]{style="font-family:宋体"}[VR]{lang="EN-US"}[类型为]{style="font-family:宋体"}*[vrtype]{lang="EN-US"}*[），主网关的]{style="font-family:宋体"}[system ID]{lang="FR"}[为]{style="font-family:宋体"}*[systemid]{lang="EN-US"}*

[[Main gateway changed on VR *vrid* (*vrtype*), old gateway: *systemid1*, new gateway: *systemid2*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1799600325}

[[在]{style="font-family:宋体"}]{#struct_0_19361_x3680_1318483427}[VR]{lang="FR"}[上主网关改变，]{style="font-family:宋体"}[VR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vrid]{lang="EN-US"}*[（]{style="font-family:宋体"}[VR]{lang="EN-US"}[类型为]{style="font-family:宋体"}*[vrtype]{lang="EN-US"}*[），旧的主网关]{style="font-family:宋体"}[system ID]{lang="FR"}[为]{style="font-family:宋体"}*[systemid1]{lang="EN-US"}[，]{style="font-family:宋体"}*[新的主网关]{style="font-family:宋体"}[system ID]{lang="FR"}[为]{style="font-family:宋体"}*[systemid2]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging trill adj-packet]{lang="EN-US"}]{#struct_0_19361_x3680_x1489107048}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x238214098}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_1769805708}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_x1805936182}

[[Receive a *type* contains invalid *string*. IIH discarded]{lang="EN-US"}]{#struct_0_19361_x3680_147735208}

[[收到]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_19361_x3680_x1911087528}[报文解析报文头时，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[的合法性检查失败，丢弃该报文。]{style="font-family:宋体"}[s*tring*]{lang="EN-US"}[为报文头中的字段，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAN IIH]{lang="EN-US"}]{#struct_0_19361_x3680_59345488}[：表示]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BPDU]{lang="EN-US"}]{#struct_0_19361_x3680_x555243081}[：表示]{lang="EN-US" style="font-family:宋体"}[BPDU]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STP]{lang="EN-US"}]{#struct_0_19361_x3680_1430164493}[：表示生成树报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTP]{lang="EN-US"}]{#struct_0_19361_x3680_1399800457}[：表示快速生成树报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MSTP]{lang="EN-US"}]{#struct_0_19361_x3680_147669672}[：表示多实例生成树报文]{style="font-family:宋体"}

[[Receive a LAN IIH *string* error. IIH discarded]{lang="EN-US"}]{#struct_0_19361_x3680_x1204752283}

[[收到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_19361_x3680_2019891691}[报文解析]{style="font-family:宋体"}[TLV]{lang="EN-US"}[时发生错误，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为错误原因]{style="font-family:宋体"}

[[IIH area address with the local system mismatch.]{lang="EN-US"}]{#struct_0_19361_x3680_x186547446}

[[Hello]{lang="EN-US"}]{#struct_0_19361_x3680_x1340300640}[报文区域地址同本地系统不匹配]{style="font-family:宋体"}

[[IIH *string* with circuit(*port*) mismatch]{lang="EN-US"}]{#struct_0_19361_x3680_147866280}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_19361_x3680_x574153221}[报文的特征与接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的特征不匹配，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文与接口不匹配的特征]{style="font-family:宋体"}

[[IIH has the same SNPA with a NBR, but different System ID. The NBR will be down]{lang="EN-US"}]{#struct_0_19361_x3680_x1994361192}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_19361_x3680_1056344993}[报文与已有邻居有相同的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，但是系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[不同，将这个邻居置]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[IIH has the same System ID with a NBR, but different SNPA. The IIH will be discarded]{lang="EN-US"}]{#struct_0_19361_x3680_x527936831}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_19361_x3680_147800744}[报文与已有邻居有相同的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[，但是]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不同，丢弃该]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Level-1 NBR(*mac*) two way *string*]{lang="EN-US"}]{#struct_0_19361_x3680_1019182098}

[[Level-1]{lang="EN-US"}]{#struct_0_19361_x3680_1764367305}[的邻居]{style="font-family:宋体"}[2-Way]{lang="EN-US"}[检查的结果，]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[为邻居的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为检查结果。]{style="font-family:宋体"}[s*tring*]{lang="EN-US"}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pass]{lang="EN-US"}]{#struct_0_19361_x3680_x1930656725}[：表示通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fail]{lang="EN-US"}]{#struct_0_19361_x3680_1635508369}[：表示不通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pend]{lang="EN-US"}]{#struct_0_19361_x3680_147997352}[：表示邻居信息未收集完整，需继续等待]{style="font-family:宋体"}

[[No VLAN-FLAGS sub-TLV in the MP-CAP TLV]{lang="EN-US"}]{#struct_0_19361_x3680_1440393337}

[[在收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_19361_x3680_2107952993}[报文中，]{style="font-family:宋体"}[Multi-Topology Aware Port Capability TLV]{lang="EN-US"}[里没有包含]{style="font-family:宋体"}[VLAN-Flags]{lang="EN-US"}[子]{style="font-family:宋体"}[TLV]{lang="EN-US"}[，与协议不符]{style="font-family:宋体"}

[[System is under disable state, ADJ packet discarded]{lang="EN-US"}]{#struct_0_19361_x3680_x1154929439}

[[系统处于关闭状态，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_19361_x3680_147931816}[模块收到的报文]{style="font-family:宋体"}

[[Circuit state is not up, ADJ packet discarded]{lang="EN-US"}]{#struct_0_19361_x3680_x884371376}

[[接口处于非]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_19361_x3680_x869877461}[状态，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[模块收到的报文]{style="font-family:宋体"}

[[Receive a packet from self, ADJ packet discarded]{lang="EN-US"}]{#struct_0_19361_x3680_x1853337085}

[[收到的是自己的报文，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_19361_x3680_148128424}[模块收到的报文]{style="font-family:宋体"}

[[Receive a invalid packet, ADJ packet discarded]{lang="EN-US"}]{#struct_0_19361_x3680_899828260}

[[报文合法性检查不通过，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_19361_x3680_x1584494270}[模块收到的报文]{style="font-family:宋体"}

[[Receive a *type* packet from(a*ddress*) on circuit(*port*)]{lang="EN-US"}]{#struct_0_19361_x3680_x1787850791}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_148062888}[上从地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*[收到了]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型报文。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lan L1 Hello]{lang="EN-US"}]{#struct_0_19361_x3680_x169749920}[：表示]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MTU-prob]{lang="EN-US"}]{#struct_0_19361_x3680_2137911596}[：表示]{lang="EN-US" style="font-family:宋体"}[MTU-prob]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Receive unsupport packet *type*, ADJ packet discarded]{lang="EN-US"}]{#struct_0_19361_x3680_148259496}

[[收到不支持的报文，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_19361_x3680_812730677}[模块收到的报文，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[为报文的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[类型值]{style="font-family:宋体"}

[[Receive a packet with invalid length, BPDU packet discarded]{lang="EN-US"}]{#struct_0_19361_x3680_193160341}

[[丢弃收到的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_19361_x3680_x781743757}[报文，因为其长度不合法]{style="font-family:宋体"}

[[Receive a BPDU packet on circuit(*port*)]{lang="EN-US"}]{#struct_0_19361_x3680_148193960}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_197346830}[上收到了]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[No enough PDU space for *string*]{lang="EN-US"}]{#struct_0_19361_x3680_x1829400661}

[[PDU]{lang="EN-US"}]{#struct_0_19361_x3680_1713819152}[长度已达到最大值，无法继续编码，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[PDU]{lang="EN-US"}[达到最大值的时机]{style="font-family:宋体"}

[[No enable VLAN to fill the enable VLAN TLV]{lang="EN-US"}]{#struct_0_19361_x3680_749483102}

[[没有任何使能]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_828623762}[，所以无法对]{style="font-family:宋体"}[Enabled-VLANs]{lang="EN-US"}[子]{style="font-family:宋体"}[TLV]{lang="EN-US"}[进行编码]{style="font-family:宋体"}

[[Get adj pointer failed for string]{lang="EN-US"}]{#struct_0_19361_x3680_1713753616}

[[VLAN FLAGS]{lang="EN-US"}]{#struct_0_19361_x3680_1944626929}[子]{style="font-family:宋体"}[TLV]{lang="EN-US"}[获取]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[指针失败，]{style="font-family:宋体"}[string]{lang="EN-US"}[为获取失败的时机]{style="font-family:宋体"}

[[No need to encode AVF sub-TLV.]{lang="EN-US"}]{#struct_0_19361_x3680_1331922928}

[[不需要编码]{style="font-family:宋体"}[AVF]{lang="EN-US"}]{#struct_0_19361_x3680_1713950224}[子]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[No need to set forward VLAN if not DRB]{lang="EN-US"}]{#struct_0_19361_x3680_776799231}

[[不是]{style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_19361_x3680_x1989270429}[，无需携带]{style="font-family:宋体"}[Appointed Forwarders]{lang="EN-US"}[子]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[DRB/RB send a HELLO on circuit(*port*) in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_1713884688}

[[DRB/RB]{lang="EN-US"}]{#struct_0_19361_x3680_x397945200}[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[内发送了]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[RB send a HELLO on circuit(*port*) in designated VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_x524385189}

[[RB]{lang="EN-US"}]{#struct_0_19361_x3680_1714081296}[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的指定]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[内发送了]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Success to send a TCN/MTU-ack packet on circuit(*port*) in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_19361_x3680_1856999554}

[[成功在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x2048240596}[的]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[内发送了]{style="font-family:宋体"}[TCN/MTU-ack]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Receive invalid/NULL MCS message *type*]{lang="EN-US"}]{#struct_0_19361_x3680_1714015760}

[[收到非法]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_x1327537413}[空的二层组播信息，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[为二层组播报文的类型值]{style="font-family:宋体"}

[[Unsupported MTU size(*size*) in MTU-prob, received length: *length*]{lang="EN-US"}]{#struct_0_19361_x3680_481515865}

[[收到的]{style="font-family:宋体"}[MTU-prob]{lang="EN-US"}]{#struct_0_19361_x3680_1714212368}[报文携带的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大小]{style="font-family:宋体"}*[size]{lang="EN-US"}*[与设备收到的长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[无法匹配]{style="font-family:宋体"}

[[Invalid ACK source ID(*id*) in MTU-prob]{lang="EN-US"}]{#struct_0_19361_x3680_1443765298}

[[收到的]{style="font-family:宋体"}[MTU-prob]{lang="EN-US"}]{#struct_0_19361_x3680_1714146832}[报文中的]{style="font-family:宋体"}[ACK source ID]{lang="EN-US"}[（]{style="font-family:宋体"}*[id]{lang="EN-US"}*[）非法]{style="font-family:宋体"}

[[Circuit(*port*) is not AVF, BPDU discarded]{lang="EN-US"}]{#struct_0_19361_x3680_281013820}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_1228840219}[不作为]{style="font-family:宋体"}[AVF]{lang="EN-US"}[，丢弃收到的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received TCA BPDU on circuit(*port*)]{lang="EN-US"}]{#struct_0_19361_x3680_1714343440}

[[在接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_1815390074}[上收到]{style="font-family:宋体"}[TCA]{lang="EN-US"}[应答报文]{style="font-family:宋体"}

[[Received NULL MCS information]{lang="EN-US"}]{#struct_0_19361_x3680_x1698036409}

[[收到的二层组播信息为空]{style="font-family:宋体"}]{#struct_0_19361_x3680_1714277904}

[[Received MCS information:]{lang="EN-US"}]{#struct_0_19361_x3680_x118195711}

[[type= *type*, INET family= *number*, VLAN= *vlan-id*, MAC= *mac*]{lang="EN-US"}]{#struct_0_19361_x3680_1713819153}

[[收到二层组播信息的具体内容，二层组播报文的类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_19361_x3680_749417566}[，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[，涉及的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}[，]{style="font-family:宋体"}*[如果是组播信息的话，其]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging trill snp-packet]{lang="EN-US"}]{#struct_0_19361_x3680_x749757225}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x245698194}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_46910055}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_174695966}

[[Not find current lsp entry to build csnp.]{lang="EN-US"}]{#struct_0_19361_x3680_1713753617}

[[没有找到当前的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_1944561393}[来创建]{style="font-family:宋体"}[CSNP]{lang="EN-US"}

[[Circuit(*port*) silence, ]{lang="EN-US"}[CSNP/PSNP not send.]{lang="EN-US"}]{#struct_0_19361_x3680_97236951}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_x2132687048}[被配置为]{style="font-family:宋体"}[silence]{lang="EN-US"}[，不发送]{style="font-family:宋体"}[CSNP/PSNP]{lang="EN-US"}

[[Level-1 csnp timer expired on a not DRB circuit(*port*).]{lang="EN-US"}]{#struct_0_19361_x3680_x1507638900}

[[非]{style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_19361_x3680_x1708338283}[的接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上]{style="font-family:宋体"}[level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Send ]{lang="FR"}]{#struct_0_19361_x3680_1713950225}[L1 CSNP/PSNP on circuit *port*.]{lang="FR"}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_19361_x3680_776733695}[发送]{style="font-family:宋体"}[L1 CSNP/PSNP]{lang="EN-US"}

[[Level-1 psnp timer expired on a DRB circuit(*port*).]{lang="EN-US"}]{#struct_0_19361_x3680_x2068580983}

[[DRB]{lang="EN-US"}]{#struct_0_19361_x3680_x712974602}[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上]{style="font-family:宋体"}[level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Wrong lsp entry tlv length(*TlvLen*) in snp.]{lang="EN-US"}]{#struct_0_19361_x3680_x1980521107}

[[SNP]{lang="EN-US"}]{#struct_0_19361_x3680_1713884689}[中携带错误的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Snp contain too much lsp entry.]{lang="EN-US"}]{#struct_0_19361_x3680_x397879664}

[[SNP]{lang="EN-US"}]{#struct_0_19361_x3680_313658676}[中包含]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要的个数超过限制]{style="font-family:宋体"}

[[Invalid lsp id reported in snp.]{lang="EN-US"}]{#struct_0_19361_x3680_x922803258}

[[SNP]{lang="EN-US"}]{#struct_0_19361_x3680_x294756440}[中包含无效的]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}

[[Wrong tlv length in snp.]{lang="EN-US"}]{#struct_0_19361_x3680_1714081297}

[[SNP]{lang="EN-US"}]{#struct_0_19361_x3680_1857065090}[中携带错误的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Invalid tlv in snp.]{lang="EN-US"}]{#struct_0_19361_x3680_1506270721}

[[SNP]{lang="EN-US"}]{#struct_0_19361_x3680_x1040112599}[中携带无效的]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Lsp entry *id*.*pseudo*-n*um* processed, newer/older/same than lsdb copy.]{lang="EN-US"}]{#struct_0_19361_x3680_1714015761}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x1327602949}[摘要]{style="font-family:宋体"}*[id]{lang="EN-US"}*[.*pseudo*-n*um*]{lang="EN-US"}[比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中保存的新]{style="font-family:宋体"}[/]{lang="EN-US"}[旧]{style="font-family:宋体"}[/]{lang="EN-US"}[相同]{style="font-family:宋体"}[。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[[Lsp entry *id*.*pseudo*-n*um* processed, not exist in lsdb.]{lang="EN-US"}]{#struct_0_19361_x3680_1320912339}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_1932925934}[摘要]{style="font-family:宋体"}*[id]{lang="EN-US"}*[.*pseudo*-n*um*]{lang="EN-US"}[，在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中不存在]{style="font-family:宋体"}[。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[[CSNP/PSNP not processed before DRB election.]{lang="EN-US"}]{#struct_0_19361_x3680_1714212369}

[[在]{style="font-family:宋体"}[DRB]{lang="EN-US"}]{#struct_0_19361_x3680_1443699762}[选举前不处理]{style="font-family:宋体"}[CSNP/PSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Psnp not processed, current RB is not DRB.]{lang="EN-US"}]{#struct_0_19361_x3680_765811969}

[[当前]{style="font-family:宋体"}[RB]{lang="EN-US"}]{#struct_0_19361_x3680_1941388207}[不是]{style="font-family:宋体"}[DRB]{lang="EN-US"}[，不处理]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Csnp not processed on DRB.]{lang="EN-US"}]{#struct_0_19361_x3680_1714146833}

[[DRB]{lang="EN-US"}]{#struct_0_19361_x3680_281079356}[上不处理]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Lsp entry *LSPId*.*PseudoId* -*LspNum* is not loaded in csnp.]{lang="EN-US"}]{#struct_0_19361_x3680_x1041130822}

[[在]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_19361_x3680_1714343441}[中没有]{style="font-family:宋体"}[LSP *id*.*pseudo*-n*um*]{lang="EN-US"}[的摘要]{style="font-family:宋体"}[。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[[Invalid type of SNP PDU.]{lang="EN-US"}]{#struct_0_19361_x3680_1815455610}

[[无效的]{style="font-family:宋体"}[SNP PDU]{lang="EN-US"}]{#struct_0_19361_x3680_x980000143}[类型]{style="font-family:宋体"}

[[SNP PDU process failed.]{lang="EN-US"}]{#struct_0_19361_x3680_338052098}

[[处理]{style="font-family:宋体"}[SNP PDU]{lang="EN-US"}]{#struct_0_19361_x3680_1714277905}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging trill update-packet]{lang="EN-US"}]{#struct_0_19361_x3680_x118261247}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x249571762}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_x1164944036}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_x1086577429}

[[Flooding ]{lang="EN-US"}[L1 LSP/CSNP/PSNP *id*.*pseudo*-n*um* on circuit *port*.]{lang="EN-US"}]{#struct_0_19361_x3680_x220091059}

[[在接口]{style="font-family:宋体"}[port]{lang="EN-US"}]{#struct_0_19361_x3680_1739617546}[上扩散]{style="font-family:宋体"}[L1 LSP/CSNP/PSNP *id*.*pseudo*-n*um*]{lang="EN-US"}[。]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pseudo]{lang="EN-US"}*[，]{style="font-family:宋体"}[分片号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*

[[Parsed neighbor ]{lang="EN-US"}*[neighbour]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_19361_x3680_1713819150}

[[解析出邻居]{style="font-family:宋体"}*[neighbour]{lang="EN-US"}*]{#struct_0_19361_x3680_749614174}

[[Parse group mac address, group record number is *number*.]{lang="EN-US"}]{#struct_0_19361_x3680_297912937}

[[解析组]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19361_x3680_1643646635}[地址，组记录个数为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[Parsed *number1* group record(s), tlv takes *number2*.]{lang="EN-US"}]{#struct_0_19361_x3680_711231472}

[[解析出]{style="font-family:宋体"}*[number1]{lang="EN-US"}*]{#struct_0_19361_x3680_1713753614}[个组记录，]{style="font-family:宋体"}[TLV]{lang="EN-US"}[携带了]{style="font-family:宋体"}*[number2]{lang="EN-US"}*[个]{style="font-family:宋体"}

[[Parsed trill version is ]{lang="EN-US"}*[value]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_19361_x3680_1944758001}

[[解析]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_62777421}[版本，版本值为]{style="font-family:宋体"}[value]{lang="EN-US"}

[[Parsed nickname *remote*.]{lang="EN-US"}]{#struct_0_19361_x3680_x84013676}

[[解析出]{style="font-family:宋体"}[Nickname *remote*]{lang="EN-US"}]{#struct_0_19361_x3680_1384535331}

[[Parsed trees info.]{lang="EN-US"}]{#struct_0_19361_x3680_1713950222}

[[解析出分发树计算信息]{style="font-family:宋体"}]{#struct_0_19361_x3680_776930303}

[[Parsed trees list, startnum is *start*.]{lang="EN-US"}]{#struct_0_19361_x3680_x251422794}

[[解析出分发树列表，起始数为]{style="font-family:宋体"}*[start]{lang="EN-US"}*]{#struct_0_19361_x3680_1250888026}

[[Parsed interest vlans, start vlan ]{lang="EN-US"}*[start]{lang="EN-US"}*[, end vlan *end*.]{lang="EN-US"}]{#struct_0_19361_x3680_390449379}

[[解析出关注]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19361_x3680_1713884686}[信息，范围为]{style="font-family:宋体"}*[start]{lang="EN-US"}*[到]{style="font-family:宋体"}*[end]{lang="EN-US"}*

[[Add/Delete/Modify Level-1 spf node(*Source*).]{lang="EN-US"}]{#struct_0_19361_x3680_x397551984}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_1011921267}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[的]{style="font-family:宋体"}[Level-1 SPF]{lang="EN-US"}[节点]{style="font-family:宋体"}

[[(MT*id*) string level-1 group address(vlan *id*: MAC *mac*).]{lang="EN-US"}]{#struct_0_19361_x3680_x808022171}

[[Add/Delete/Modify]{lang="EN-US"}]{#struct_0_19361_x3680_1714081294}[主地址，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Lsp\'s seq number is 0.]{lang="EN-US"}]{#struct_0_19361_x3680_1856868482}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x1692153623}[的序号为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Illegal is-type in level-1 lsp.]{lang="EN-US"}]{#struct_0_19361_x3680_1014031141}

[[Level-1]{lang="EN-US"}]{#struct_0_19361_x3680_897552526}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[内的无效的]{style="font-family:宋体"}[is]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Check sum is zero.]{lang="EN-US"}]{#struct_0_19361_x3680_1714015758}

[[校验和为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_19361_x3680_x1327013126}

[[Check sum error.]{lang="EN-US"}]{#struct_0_19361_x3680_x1679091413}

[[校验和错误]{style="font-family:宋体"}]{#struct_0_19361_x3680_1714212366}

[[Invalid extended is reachability tlv.]{lang="EN-US"}]{#struct_0_19361_x3680_1443372082}

[[无效可达]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_19361_x3680_x1504421189}

[[Unsupported trill version(*id*)]{lang="EN-US"}]{#struct_0_19361_x3680_759465062}

[[不支持的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}]{#struct_0_19361_x3680_1714146830}[版本（版本号）]{style="font-family:宋体"}

[[Invalid nickname/ trees/ tree identifiers/ interested vlans subtlv.]{lang="EN-US"}]{#struct_0_19361_x3680_280882748}

[[无效的]{style="font-family:宋体"}[Nickname/trees/tree identifiers/interested vlans]{lang="EN-US"}]{#struct_0_19361_x3680_182285370}[子]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Support protocol mismatch.]{lang="EN-US"}]{#struct_0_19361_x3680_1485148329}

[[支持协议不匹配]{style="font-family:宋体"}]{#struct_0_19361_x3680_1714343438}

[[Lsp with more than *number* area addr(es).]{lang="EN-US"}]{#struct_0_19361_x3680_1815914355}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x1345989009}[携带多于]{style="font-family:宋体"}*[number]{lang="EN-US"}*[个区域地址]{style="font-family:宋体"}

[[Lsp with wrong area addr length *length*.]{lang="EN-US"}]{#struct_0_19361_x3680_1714277902}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x117802495}[携带长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的错误区域地址]{style="font-family:宋体"}

[[Lsp with wrong area addr *number*.]{lang="EN-US"}]{#struct_0_19361_x3680_208923122}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_1713819151}[携带错误区域地址]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[Bad tlv len in the received lsp.]{lang="EN-US"}]{#struct_0_19361_x3680_749548638}

[[收到的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_x762108047}[中的错误]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Wrong encoding of area address tlv in lsp.]{lang="EN-US"}]{#struct_0_19361_x3680_1713753615}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_1944692465}[中的错误区域地址编码]{style="font-family:宋体"}

[[Pdu size(*size*) is greater than receive buffer size(*size*),ignoring pdu.]{lang="EN-US"}]{#struct_0_19361_x3680_x667461032}

[[PDU]{lang="EN-US"}]{#struct_0_19361_x3680_1713950223}[长度比收到的缓冲区长度大，忽略]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Pdu size(*size*) is less than common/fixed pdu header size(*size*),ignoring pdu.]{lang="EN-US"}]{#struct_0_19361_x3680_776864767}

[[PDU]{lang="EN-US"}]{#struct_0_19361_x3680_134506843}[长度比一般]{style="font-family:宋体"}[/]{lang="EN-US"}[固定]{style="font-family:宋体"}[PDU]{lang="EN-US"}[头长度小，忽略]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Pdu length mismatch: recvLen = *length1*, encodeLen = *length2*,ignoring pdu]{lang="EN-US"}]{#struct_0_19361_x3680_1713884687}

[[PDU]{lang="EN-US"}]{#struct_0_19361_x3680_x397486448}[长度不匹配：收到长度为]{style="font-family:宋体"}*[length1]{lang="EN-US"}*[，编码长度为]{style="font-family:宋体"}*[length2]{lang="EN-US"}*[，忽略]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[LSP or SNP PDU common header error, ignoring pdu.]{lang="EN-US"}]{#struct_0_19361_x3680_633933663}

[[LSP]{lang="EN-US"}]{#struct_0_19361_x3680_1714081295}[或]{style="font-family:宋体"}[SNP PDU]{lang="EN-US"}[通用头错误，忽略]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Received PDU level mismatch.]{lang="EN-US"}]{#struct_0_19361_x3680_1856934018}

[[收到]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_19361_x3680_x830385793}[级别不匹配]{style="font-family:宋体"}

[[No active neighbour with such snpa(*addr*) on the cicuit(*name*), ignoring pdu.]{lang="EN-US"}]{#struct_0_19361_x3680_1714015759}

[[在链路上没有带有这种]{style="font-family:宋体"}[SNPA]{lang="EN-US"}]{#struct_0_19361_x3680_x1327078662}[的激活邻居，忽略]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[LSP PDU process failed.]{lang="EN-US"}]{#struct_0_19361_x3680_432516618}

[[LSP PDU]{lang="EN-US"}]{#struct_0_19361_x3680_1714212367}[处理失败]{style="font-family:宋体"}

[[Received pdu is not lsp or snp, ignoring pdu.]{lang="EN-US"}]{#struct_0_19361_x3680_1443306546}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_19361_x3680_x1111586733}[不是]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或]{style="font-family:宋体"}[SNP]{lang="EN-US"}[，忽略]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Check received packet failed.]{lang="EN-US"}]{#struct_0_19361_x3680_1714146831}

[[检查收到报文失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_280948284}

[[Starting to calculate distribution tree.]{lang="EN-US"}]{#struct_0_19361_x3680_1714343439}

[[开始计算分发树]{style="font-family:宋体"}]{#struct_0_19361_x3680_1815979891}

[[(MT*id*) *string* level-1 used tree root nickname *name* to dec.]{lang="EN-US"}]{#struct_0_19361_x3680_x1332923324}

[[Add/Modify/Delete level-1 ]{lang="EN-US"}]{#struct_0_19361_x3680_1714277903}[树根到]{style="font-family:宋体"}[dec]{lang="EN-US"}

[[Modify nickname node(*name*): tree used identifiers.]{lang="EN-US"}]{#struct_0_19361_x3680_x117868031}

[[修改]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_x1806927878}[节点：树使用标示]{style="font-family:宋体"}

[[Modify nickname node(*name*): trees info.]{lang="EN-US"}]{#struct_0_19361_x3680_1713819148}

[[修改]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_750138461}[节点：树信息]{style="font-family:宋体"}

[[Process local nickname change.]{lang="EN-US"}]{#struct_0_19361_x3680_1713753612}

[[处理本地]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_1944889073}[的改变]{style="font-family:宋体"}

[[Add/Delete nickname node(nickname: *name*, system id: *string*).]{lang="EN-US"}]{#struct_0_19361_x3680_x1481483194}

[[增加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_1713950220}[删除]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[节点]{style="font-family:宋体"}

[[Modify nickname node(*name*): priority.]{lang="EN-US"}]{#struct_0_19361_x3680_777061375}

[[修改]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_1713884684}[节点：优先级]{style="font-family:宋体"}

[[Received nickname has lower /higher priority.]{lang="EN-US"}]{#struct_0_19361_x3680_x397683056}

[[收到的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_1714081292}[有低]{style="font-family:宋体"}[/]{lang="EN-US"}[高优先级]{style="font-family:宋体"}

[[local nickname has lower /higher priority.]{lang="EN-US"}]{#struct_0_19361_x3680_1857261698}

[[本地]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_x1610633041}[有低]{style="font-family:宋体"}[/]{lang="EN-US"}[高优先级]{style="font-family:宋体"}

[[Receive invalid nickname *name*.]{lang="EN-US"}]{#struct_0_19361_x3680_1714015756}

[[收到无效]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_x1327406342}

[[Update distribution tree info, failed to get nickname node.]{lang="EN-US"}]{#struct_0_19361_x3680_1714212364}

[[更新分发树信息：获取]{style="font-family:宋体"}[Nickname]{lang="EN-US"}]{#struct_0_19361_x3680_1443503154}[节点失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging trill route]{lang="EN-US"}]{#struct_0_19361_x3680_x1116615019}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x222773682}[[字段]{style="font-family:黑体"}]{#struct_0_19361_x3680_1086060146}

[[描述]{style="font-family:黑体"}]{#struct_0_19361_x3680_842692470}

[[(M*id*) Set trigger event at *time*]{lang="EN-US"}]{#struct_0_19361_x3680_1714146828}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_281407037}[M*id*]{lang="FR"}[）在]{style="font-family:宋体"}*[time]{lang="FR"}*[时间设置触发事件，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID ]{lang="EN-US"}

[[(M*id*) Old scheduled event is *value*, new trigger event is *event*.]{lang="EN-US"}]{#struct_0_19361_x3680_x556795733}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1088377951}[M*id*]{lang="FR"}[）旧的调度标记是]{style="font-family:宋体"}*[value]{lang="EN-US"}[，]{style="font-family:宋体"}*[新的触发事件是]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[(M*id*) The event *event* is scheduled.]{lang="EN-US"}]{#struct_0_19361_x3680_149181034}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_1853970345}[M*id*]{lang="FR"}[）调度事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[已设置，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[(]{lang="EN-US"}*[M*id) Not allowed to calculate topology for inactive state.*]{lang="EN-US"}]{#struct_0_19361_x3680_1714343436}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_1815783283}[M*id*]{lang="FR"}[）]{style="font-family:宋体"}[Inactive]{lang="FR"}[状态下不允许进行拓扑计算，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[(M*id*) Current running event is revent, trigger event is tevent.]{lang="EN-US"}]{#struct_0_19361_x3680_x918706453}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1451312141}[M*id*]{lang="FR"}[）当前运行事件是]{style="font-family:宋体"}*[revent]{lang="EN-US"}[，]{style="font-family:宋体"}*[触发事件是]{style="font-family:宋体"}*[tevent]{lang="EN-US"}*[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[(M*id*) Stop current calculation work.]{lang="EN-US"}]{#struct_0_19361_x3680_1714277900}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x117933567}[M*id*]{lang="FR"}[）停止当前的计算工作，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[(M*id*) Need to restart SPF calculation work, current running event is revent, new trigger event: tevent]{lang="FR"}]{#struct_0_19361_x3680_x565938901}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x499483440}[M*id*]{lang="FR"}[）需要重启]{style="font-family:宋体"}[SPF]{lang="FR"}[计算工作，当前运行事件是]{style="font-family:宋体"}*[revent]{lang="EN-US"}[，]{style="font-family:宋体"}*[触发事件是]{style="font-family:宋体"}*[tevent]{lang="EN-US"}*[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[(M*id*) All phases of SPF work completed at time.\"]{lang="FR"}]{#struct_0_19361_x3680_1713819149}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_750072925}[M*id*]{lang="FR"}[）所有]{style="font-family:宋体"}[SPF]{lang="FR"}[阶段于]{style="font-family:宋体"}*[time]{lang="EN-US"}*[时间完成，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[(M*id*) Begin SPF calculation work from root node.]{lang="FR"}]{#struct_0_19361_x3680_1663247116}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1176140725}[M*id*]{lang="FR"}[）从根节点开始]{style="font-family:宋体"}[SPF]{lang="FR"}[计算，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[(M*id*)Merge nexthop from root node, count: *num1*/*num2*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1997301303}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_1713753613}[M*id*]{lang="FR"}[）从根节点合并下一跳，数量：]{style="font-family:宋体"}*[num1/num2]{lang="FR"}*[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[(M*id*)) Merge nexthop from parent node, count: *num*.]{lang="EN-US"}]{#struct_0_19361_x3680_1944823537}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_89837108}[M*id*]{lang="FR"}[）从父节点合并下一跳，数量：]{style="font-family:宋体"}*[num]{lang="FR"}*[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Parent node not found.]{lang="FR"}]{#struct_0_19361_x3680_1137535099}

[[没有找到父节点]{style="font-family:宋体"}]{#struct_0_19361_x3680_1713950221}

[[Spf node not found.]{lang="FR"}]{#struct_0_19361_x3680_776995839}

[[没有找到]{style="font-family:宋体"}]{#struct_0_19361_x3680_2123470413}[SPF]{lang="FR"}[节点]{style="font-family:宋体"}

[[Back link not found.]{lang="FR"}]{#struct_0_19361_x3680_768026596}

[[没有找到回指链路]{style="font-family:宋体"}]{#struct_0_19361_x3680_1713884685}

[[New distance is *value*.]{lang="FR"}]{#struct_0_19361_x3680_x397617520}

[[新的距离是]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_19361_x3680_x128214272}

[[New distance exceeds max.]{lang="FR"}]{#struct_0_19361_x3680_1944661571}

[[新的距离超过最大值]{style="font-family:宋体"}]{#struct_0_19361_x3680_1714081293}

[[Greater cost.]{lang="FR"}]{#struct_0_19361_x3680_1857327234}

[[更大的]{style="font-family:宋体"}]{#struct_0_19361_x3680_x32049926}[Cost]{lang="FR"}

[[Less cost, add node to tent heap.]{lang="EN-US"}]{#struct_0_19361_x3680_1714015757}

[[较小的]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1327471878}[Cost]{lang="FR"}[，将]{style="font-family:宋体"}[node]{lang="FR"}[加入到]{style="font-family:宋体"}[tent]{lang="FR"}[中]{style="font-family:宋体"}

[[Equal cost, do nothing.]{lang="FR"}]{#struct_0_19361_x3680_x1588172362}

[[相等的]{style="font-family:宋体"}]{#struct_0_19361_x3680_185780940}[Cost]{lang="FR"}[，不处理]{style="font-family:宋体"}

[[Node update to tent list.]{lang="FR"}]{#struct_0_19361_x3680_1714212365}

[[节点更新到]{style="font-family:宋体"}]{#struct_0_19361_x3680_1443437618}[tent]{lang="FR"}[中]{style="font-family:宋体"}

[[Node is added into SPT path.]{lang="EN-US"}]{#struct_0_19361_x3680_x726795190}

[[节点已经加入到]{style="font-family:宋体"}]{#struct_0_19361_x3680_1714146829}[SPT]{lang="FR"}[路径中]{style="font-family:宋体"}

[[Node has no nexthop. Ignore its nbrs.]{lang="EN-US"}]{#struct_0_19361_x3680_281472573}

[[节点没有下一跳信息，忽略其邻居]{style="font-family:宋体"}]{#struct_0_19361_x3680_x188918185}

[[Node is Overload, ignore its nbrs.]{lang="EN-US"}]{#struct_0_19361_x3680_1714343437}

[[节点已经]{style="font-family:宋体"}]{#struct_0_19361_x3680_1815848819}[overload]{lang="FR"}[，忽略其邻居]{style="font-family:宋体"}

[[Link is to be deleted.]{lang="EN-US"}]{#struct_0_19361_x3680_1393273076}

[[链路被删除]{style="font-family:宋体"}]{#struct_0_19361_x3680_1714277901}

[[Link is backward link, ignore it.]{lang="EN-US"}]{#struct_0_19361_x3680_x117999103}

[[链路是回指链路，忽略]{style="font-family:宋体"}]{#struct_0_19361_x3680_1696138047}

[[2-way check failed while no backward link found.]{lang="EN-US"}]{#struct_0_19361_x3680_x1015064203}

[[当没有发现回指链路，]{style="font-family:宋体"}]{#struct_0_19361_x3680_377966743}[2-way]{lang="FR"}[检查失败]{style="font-family:宋体"}

[[Link\'s valid check failed.]{lang="FR"}]{#struct_0_19361_x3680_1437692880}

[[链路的有效性检查失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1015129739}

[[Dest node not found.]{lang="FR"}]{#struct_0_19361_x3680_x1170161986}

[[没有发现目标节点]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1985026444}

[[(M*id*:L*level*) Running full SPF calculation work.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014933131}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_988885490}[M]{lang="FR"}*[id]{lang="EN-US"}*[:L]{lang="FR"}*[level]{lang="EN-US"}*[）开始进行全部]{style="font-family:
  宋体"}[SPF]{lang="FR"}[计算，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[level]{lang="EN-US"}*[表示级别]{style="font-family:宋体"}

[[Link exceeds max limits]{lang="FR"}]{#struct_0_19361_x3680_1505978478}

[[链路超出最大限制]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014998667}

[[Link is to be deleted.]{lang="FR"}]{#struct_0_19361_x3680_1589167653}

[[链路将要被删除]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1368468186}

[[Link with max metric.]{lang="FR"}]{#struct_0_19361_x3680_x1014802059}

[[带有最大]{style="font-family:宋体"}]{#struct_0_19361_x3680_1359007440}[metric]{lang="FR"}[值的链路]{style="font-family:宋体"}

[[Link is same with backlink.]{lang="FR"}]{#struct_0_19361_x3680_x1014867595}

[[链路和回退链路相同]{style="font-family:宋体"}]{#struct_0_19361_x3680_x935434363}

[[MReceiver info (M*id*:L*level*) add(new) multi-reciever *source* *vlan* *mac*]{lang="EN-US"}]{#struct_0_19361_x3680_2100629549}

[[(M*id*:L*level*)]{lang="EN-US"}]{#struct_0_19361_x3680_x1014670987}[添加组播接收者，源]{style="font-family:
  宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[，组播地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[SPF link (M*id*:L*level*) Create(New) link *source* *\--\>* *dest* \[AttAdjs: *number*\] \[Tree\] \[Back\] \[Usage\] \[Nhop\]]{lang="EN-US"}]{#struct_0_19361_x3680_x229700216}

[[(M*id*:L*level*)]{lang="EN-US"}]{#struct_0_19361_x3680_x1014736523}[创建]{style="font-family:
  宋体"}[SPFLink]{lang="EN-US"}[，源节点为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的节点为]{style="font-family:宋体"}*[dest]{lang="EN-US"}*[，]{style="font-family:宋体"}[ATT]{lang="EN-US"}[邻居数为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[The D-Node pointer is NULL.]{lang="EN-US"}]{#struct_0_19361_x3680_x1728832724}

[[D-node]{lang="FR"}]{#struct_0_19361_x3680_x1014539915}[指针为空]{style="font-family:宋体"}

[[Node is updated in tent heap.]{lang="EN-US"}]{#struct_0_19361_x3680_10706830}

[[Tent]{lang="FR"}]{#struct_0_19361_x3680_x2057528861}[中的]{style="font-family:宋体"}[node]{lang="FR"}[已经更新]{style="font-family:宋体"}

[[D-tree calculation started/ended at *time*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014605451}

[[D-tree]{lang="FR"}]{#struct_0_19361_x3680_1952983548}[计算开始]{style="font-family:宋体"}[/]{lang="FR"}[于结束于]{style="font-family:宋体"}*[time]{lang="EN-US"}*

[[Failed to flush prefix/VN head, NBR Id is *id*, error is *errno*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1015064202}

[[下刷]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1188117198}[prefix head/]{lang="FR"}[VN head]{lang="EN-US"}[失败，邻居]{style="font-family:宋体"}[id]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="FR"}*[错误码是]{style="font-family:宋体"}*[errno]{lang="EN-US"}*

[[Failed to occupy/alloc NBR id *id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1582863538}

[[占用]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1015129738}[/]{lang="FR"}[分配]{style="font-family:宋体"}[NBR ID ]{lang="FR"}*[id]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[The NBR *id* is added, type is  normal/ecmp/unknown.]{lang="EN-US"}]{#struct_0_19361_x3680_1558721369}

[[NBR ]{lang="FR"}*[id]{lang="EN-US"}*]{#struct_0_19361_x3680_x1014933130}[已添加，类型为]{style="font-family:宋体"}[normal]{lang="EN-US"}[/]{lang="FR"}[ecmp/unknown]{lang="EN-US"}

[[Deleting/Add NBR *id*, refer is *refcnt*, type is normal/ecmp/unknown.]{lang="EN-US"}]{#struct_0_19361_x3680_x1739997865}

[[删除]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014998666}[/]{lang="FR"}[添加]{style="font-family:宋体"}[NBR ]{lang="FR"}*[id]{lang="EN-US"}*[，]{style="font-family:宋体"}[引用计数为]{style="font-family:宋体"}*[refcnt]{lang="EN-US"}*[，]{style="font-family:宋体"}[类型为]{style="font-family:宋体"}[normal]{lang="EN-US"}[/]{lang="FR"}[ecmp/unknown]{lang="EN-US"}

[[NBR node to be deleted.]{lang="EN-US"}]{#struct_0_19361_x3680_x1139715702}

[[NBR node]{lang="FR"}]{#struct_0_19361_x3680_x1014802058}[将被删除]{style="font-family:宋体"}

[[NBR node is root node, don\'t process.]{lang="EN-US"}]{#struct_0_19361_x3680_x207076501}

[[NBR]{lang="FR"}]{#struct_0_19361_x3680_x1047668300}[节点是跟节点，不能处理]{style="font-family:宋体"}

[[NBR node is already on SPT.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014867594}

[[NBR]{lang="FR"}]{#struct_0_19361_x3680_1793448992}[节点已在]{style="font-family:宋体"}[SPT]{lang="FR"}[上]{style="font-family:宋体"}

[[(M*id*) Begin SPF from root node.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014670986}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_1336383725}[M*id*]{lang="FR"}[）从根节点开始]{style="font-family:宋体"}[SPF]{lang="FR"}[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Flush prefix message, nickname is *name*, NBR ID is *id*, action is *value*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014736522}

[[下刷前缀信息：]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_19361_x3680_x162748783}[ickname]{lang="FR"}[为]{style="font-family:宋体"}*[name]{lang="FR"}*[，]{style="font-family:宋体"}[NBRID]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="FR"}*[，]{style="font-family:宋体"}[action]{lang="FR"}[为]{style="font-family:宋体"}*[value]{lang="FR"}*

[[Flush VN message, NBR ID is *id*, action is *value*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014539914}

[[下刷]{style="font-family:宋体"}]{#struct_0_19361_x3680_1576790771}[VN]{lang="FR"}[信息，]{style="font-family:宋体"}[NBR ID]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="FR"}*[，]{style="font-family:宋体"}[action]{lang="FR"}[为]{style="font-family:宋体"}*[value]{lang="FR"}*

[[Flush TFIB smooth start/end message.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014605450}

[[下刷平滑开始]{style="font-family:宋体"}]{#struct_0_19361_x3680_386899607}[/]{lang="FR"}[结束信息]{style="font-family:宋体"}

[[Flush adj message, nickname is *name*, action is *value*, ifindex is *index*, MAC is *mac*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1015064205}

[[下刷]{style="font-family:宋体"}]{#struct_0_19361_x3680_x784832671}[adj]{lang="FR"}[信息，]{style="font-family:宋体"}[N]{lang="EN-US"}[ickname]{lang="FR"}[为]{style="font-family:宋体"}*[name]{lang="FR"}*[，]{style="font-family:宋体"}[action]{lang="FR"}[为]{style="font-family:宋体"}*[action]{lang="FR"}*[，]{style="font-family:宋体"}[ifindex]{lang="FR"}[为]{style="font-family:宋体"}*[index]{lang="FR"}*[，]{style="font-family:宋体"}[MAC]{lang="FR"}[是]{style="font-family:宋体"}*[mac]{lang="FR"}*

[[INGRESS run canceled, no used tree finded.]{lang="EN-US"}]{#struct_0_19361_x3680_x1015129741}

[[INGRESS]{lang="FR"}]{#struct_0_19361_x3680_x1526195738}[运行取消，没有找到有用的树]{style="font-family:宋体"}

[[Create(new) Ingress entry, vlan: *id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014933133}

[[创建]{style="font-family:宋体"}]{#struct_0_19361_x3680_x2143282392}[Ingress]{lang="FR"}[条目，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="FR"}*

[[Add/Delete/ Update Remote entry, vlan: *id*, root:*root.*]{lang="EN-US"}]{#struct_0_19361_x3680_x1014998669}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_426368239}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[更新远端条目，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="FR"}*[，根为]{style="font-family:宋体"}*[root]{lang="EN-US"}*

[[Add port entry to Ingress entry(new), vlan: *id*,, ifIndex: *index*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014802061}

[[向]{style="font-family:宋体"}[Ingress]{lang="EN-US"}]{#struct_0_19361_x3680_1002580472}[列表添加端口列表，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}[为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[Ingress entry not found, vlan: *id*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014867597}

[[没有找到]{style="font-family:宋体"}[Ingress]{lang="EN-US"}]{#struct_0_19361_x3680_x2098233777}[列表，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Port entry not found in ingress entry, vlan: *id*, ifIndex: *index*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014670989}

[[在]{style="font-family:宋体"}[ingress]{lang="EN-US"}]{#struct_0_19361_x3680_220638478}[列表中，没有发现端口列表]{style="font-family:宋体"}

[[Set local flag of TVMac entry, root: *root,* vlan: *id*, mac: *mac*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014736525}

[[设置本地]{style="font-family:宋体"}[TVMAC]{lang="EN-US"}]{#struct_0_19361_x3680_x1014539917}[列表的标记，根为]{style="font-family:宋体"}*[root]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Add port entry to TVMac entry, root: *root*, vlan: *id*, mac: *mac*., ifIndex: *index*..]{lang="EN-US"}]{#struct_0_19361_x3680_1173506244}

[[向]{style="font-family:宋体"}[TVMAC]{lang="EN-US"}]{#struct_0_19361_x3680_x1014605453}[列表添加端口列表，根为]{style="font-family:宋体"}*[root]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[，]{style="font-family:宋体"}[ifIndex:*index*]{lang="EN-US"}

[[Update TVMac entry, root: *root*,, vlan: *id*, mac: *mac*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1179184334}

[[更新]{style="font-family:宋体"}[TVMAC]{lang="EN-US"}]{#struct_0_19361_x3680_x1015064204}[列表，根为]{style="font-family:宋体"}*[root]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Process local multicast info.]{lang="EN-US"}]{#struct_0_19361_x3680_1944050684}

[[处理本地组播信息]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1015129740}

[[Find local IPv4 multicast router.]{lang="EN-US"}]{#struct_0_19361_x3680_1202687617}

[[发现本地]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_19361_x3680_x1014933132}[组播路由]{style="font-family:宋体"}

[[Find local IPv6 multicast router.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014998668}

[[发现本地]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19361_x3680_1992452180}[组播路由]{style="font-family:宋体"}

[[Add port entry to TVlan entry, root: *root*, vlan: *id*, ifIndex: *index*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014802060}

[[向]{style="font-family:宋体"}[TVlan]{lang="EN-US"}]{#struct_0_19361_x3680_x563503469}[列表添加端口列表，根为]{style="font-family:宋体"}*[root]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}[为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[Create RPF entry, root: *root*,, ingress:*ingress*, ifIndex: *index*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014867596}

[[创建]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_19361_x3680_x1014670988}[列表，根为]{style="font-family:宋体"}*[root]{lang="EN-US"}*[，]{style="font-family:宋体"}[ingress]{lang="EN-US"}[为]{style="font-family:宋体"}*[ingress]{lang="EN-US"}*[，]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}[为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[Match the filter source id and stop.]{lang="EN-US"}]{#struct_0_19361_x3680_1786722419}

[[匹配过滤的]{style="font-family:宋体"}[source id]{lang="EN-US"}]{#struct_0_19361_x3680_x1014736524}[，并且停止]{style="font-family:宋体"}

[[Process remote multicast info along the d-tree link, ifIndex: *index*..]{lang="EN-US"}]{#struct_0_19361_x3680_643820271}

[[沿着]{style="font-family:宋体"}[d-tree]{lang="EN-US"}]{#struct_0_19361_x3680_x1014539916}[链路处理远端组播信息，]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}[为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[Update port list of IPv4/ IPv6 multi-router in TVlan entry, root: *root*,, vlan: *id*,.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014605452}

[[更新]{style="font-family:宋体"}[TVlan]{lang="EN-US"}]{#struct_0_19361_x3680_1549699021}[列表中的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由的端口列表，根为]{style="font-family:宋体"}*[root]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Add/Update/Delete RPF entry, root: *root*, ingress: *ingress.*]{lang="EN-US"}]{#struct_0_19361_x3680_x1015064207}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19361_x3680_x1947632085}[更新]{style="font-family:宋体"}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[RPF]{lang="EN-US"}[列表，根为]{style="font-family:宋体"}*[root]{lang="EN-US"}*[，]{style="font-family:宋体"}[ingress]{lang="EN-US"}[为]{style="font-family:宋体"}*[ingress]{lang="EN-US"}*

[[Add NBR *id*, new refer count is *count*, type is *type*, result is *result*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1015129743}

[[添加邻居，新的引用计数]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014933135}[为]{style="font-family:宋体"}*[count]{lang="EN-US"}*[，类型]{style="font-family:宋体"}[为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，结果]{style="font-family:宋体"}[为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[NBR *id* has been deleted, type is normal/ecmp/unknown.]{lang="EN-US"}]{#struct_0_19361_x3680_x1336713338}

[[NBR ]{lang="FR"}*[id]{lang="EN-US"}*]{#struct_0_19361_x3680_x1014998671}[已被删除，类型为]{style="font-family:宋体"}[normal]{lang="EN-US"}[/]{lang="FR"}[ecmp/unknown]{lang="EN-US"}

[[Failed to add id node for NBR *id*.]{lang="EN-US"}]{#struct_0_19361_x3680_782533063}

[[为]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014802063}[NBR ]{lang="FR"}*[id]{lang="EN-US"}*[添加]{style="font-family:宋体"}[id node]{lang="FR"}[失败]{style="font-family:宋体"}

[[(M*id*:P*prefix*) Failed to generate normal NBR.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014867599}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_1746394825}[M]{lang="FR"}*[id]{lang="EN-US"}*[:P]{lang="FR"}*[prefix]{lang="EN-US"}*[）产生普通]{style="font-family:
  宋体"}[NBR]{lang="FR"}[失败，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(M*id*:L*level*:P*prefix*) Failed to generate NBR.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014670991}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014736527}[M]{lang="FR"}*[id]{lang="EN-US"}*[:L]{lang="FR"}*[level]{lang="EN-US"}*[:P]{lang="FR"}*[prefix]{lang="EN-US"}*[）产生]{style="font-family:宋体"}[NBR]{lang="FR"}[失败，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[level]{lang="EN-US"}*[表示级别，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(M*id*:L*level*:P*prefix*) Failed to get nexthop from ISPF module.]{lang="EN-US"}]{#struct_0_19361_x3680_240535744}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014539919}[M]{lang="FR"}*[id]{lang="EN-US"}*[:L]{lang="FR"}*[level]{lang="EN-US"}*[:P]{lang="FR"}*[prefix]{lang="EN-US"}*[）从]{style="font-family:宋体"}[ISPF]{lang="FR"}[模块获取下一跳失败，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[level]{lang="EN-US"}*[表示级别，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(M*id*::P*prefix*) The nexthop number is zero.]{lang="EN-US"}]{#struct_0_19361_x3680_x1602431278}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014605455}[M]{lang="FR"}*[id]{lang="EN-US"}*[:P]{lang="FR"}*[prefix]{lang="EN-US"}*[）下一跳的数量为零，]{style="font-family:
  宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:
  宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(M*id*::P*prefix*) Failed to generate normal nbr.]{lang="EN-US"}]{#struct_0_19361_x3680_x1015064206}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_781251270}[M]{lang="FR"}*[id]{lang="EN-US"}*[:P]{lang="FR"}*[prefix]{lang="EN-US"}*[)]{lang="FR"}[）产生普通邻居失败，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(M*id*:L*level*) Failed to get nexthop for *string* from ISPF module, prefix is *prefix*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1015129742}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014933134}[M]{lang="FR"}*[id]{lang="EN-US"}*[:L]{lang="FR"}*[level]{lang="EN-US"}*[）]{style="font-family:
  宋体"}[ISPF]{lang="EN-US"}[模块由于某种原因获取下一跳失败，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(M*id*:L*level*) Processing unicast route entry *prefix*.]{lang="EN-US"}]{#struct_0_19361_x3680_229370603}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014998670}[M]{lang="FR"}*[id]{lang="EN-US"}*[:L]{lang="FR"}*[level]{lang="EN-US"}*[）处理]{style="font-family:
  宋体"}*[prefix]{lang="FR"}*[的单播路由，]{style="font-family:
  宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:
  宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[level]{lang="EN-US"}*[表示级别]{style="font-family:宋体"}

[[(M*id*:L*level*) URC run started/ended at *time*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014802062}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014867598}[M]{lang="FR"}*[id]{lang="EN-US"}*[:L]{lang="FR"}*[level]{lang="EN-US"}*[）]{style="font-family:
  宋体"}[URC]{lang="FR"}[开始]{style="font-family:宋体"}[/]{lang="FR"}[结束于]{style="font-family:宋体"}*[time]{lang="EN-US"}*[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[level]{lang="EN-US"}*[表示级别]{style="font-family:宋体"}

[[(M*id*:L*level*) URC flush ended at *time*.]{lang="EN-US"}]{#struct_0_19361_x3680_180310884}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_x1014670990}[M]{lang="FR"}*[id]{lang="EN-US"}*[:L]{lang="FR"}*[level]{lang="EN-US"}*[）]{style="font-family:
  宋体"}[URC]{lang="FR"}[下刷结束于]{style="font-family:宋体"}*[time]{lang="EN-US"}*[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[level]{lang="EN-US"}*[表示级别]{style="font-family:宋体"}

[[(P*prefix*:N*id*) Destroy route entry successfully, source id is *source*.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014736526}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_1806619685}[P]{lang="FR"}*[prefix]{lang="EN-US"}*[:N]{lang="FR"}*[id]{lang="EN-US"}*[）成功删除一条路由表项，源]{style="font-family:
  宋体"}[ID]{lang="FR"}[为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[Failed to add self route entry, nickname is invalid.]{lang="EN-US"}]{#struct_0_19361_x3680_x1014539918}

[[添加本机路由表项失败，]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_19361_x3680_x1014605454}[ickname]{lang="FR"}[为无效值]{style="font-family:宋体"}

[[Failed to add route entry, nickname is invalid.]{lang="EN-US"}]{#struct_0_19361_x3680_x1938699221}

[[添加路由表项失败，]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_19361_x3680_907250098}[ickname]{lang="FR"}[为无效值]{style="font-family:宋体"}

[[(P*prefix*) Failed to add route entry, the SPF node doesn\'t exist.]{lang="EN-US"}]{#struct_0_19361_x3680_907184562}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_907381170}[P]{lang="FR"}*[prefix]{lang="EN-US"}*[）添加路由表项失败，]{style="font-family:宋体"}[SPF]{lang="FR"}[节点不存在]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(P*prefix*)Failed to alloc route entry.]{lang="EN-US"}]{#struct_0_19361_x3680_572120828}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_907315634}[P]{lang="FR"}*[prefix]{lang="EN-US"}*[）分配路由表项失败]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[(P*prefix*:N*id*) Add or update route entry successfully, source id is *source*.]{lang="EN-US"}]{#struct_0_19361_x3680_907512242}

[[（]{style="font-family:宋体"}]{#struct_0_19361_x3680_907446706}[P]{lang="FR"}*[prefix]{lang="EN-US"}*[:N]{lang="FR"}*[id]{lang="EN-US"}*[）成功添加或更新路由表项，源]{style="font-family:
  宋体"}[ID]{lang="FR"}[为]{style="font-family:
  宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:
  宋体"}*[id]{lang="EN-US"}*[表示拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[表示前缀]{style="font-family:宋体"}

[[Failed to create route attribute.]{lang="EN-US"}]{#struct_0_19361_x3680_1190500656}

[[添加路由属性信息失败]{style="font-family:宋体"}]{#struct_0_19361_x3680_907643314}

[[Add or update route entry, nickname is *name*, NBR ID is *id*, source id is *id*]{lang="EN-US"}]{#struct_0_19361_x3680_907577778}

[[添加或更新路由表，]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_19361_x3680_907774386}[ickname]{lang="FR"}[为]{style="font-family:宋体"}*[name]{lang="FR"}*[，]{style="font-family:宋体"}[NBR ID]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="FR"}*[，源]{style="font-family:宋体"}[ID]{lang="FR"}[为]{style="font-family:宋体"}*[id]{lang="FR"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19361_x3680_1450362703}

[]{#_Toc127096848}[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_x58377218}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill error]{lang="EN-US"}]{#struct_0_19361_x3680_x928490530}

[\*Mar 18 14:28:41:744 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="EN-US"}

[TRILL-ERR: Send level-1 csnp pdu failed.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19361_x3680_x1842347687}*[发送]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_1143074854}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill event]{lang="EN-US"}]{#struct_0_19361_x3680_907708850}

[\*Jun  8 08:29:44:658 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="EN-US"}

[TRILL-Event: Notifing the TRILL interface state changed.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19361_x3680_x1981108809}*[通知]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[接口状态改变]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_x1632701170}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议]{style="font-family:宋体"}[平滑重启调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill graceful-restart]{lang="EN-US"}]{#struct_0_19361_x3680_x2089367022}

[[\*Jun  3 09:56:15:006 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_19361_x3680_x2084911688}

[[TRILL-GR: T3 timer is stoped.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_19361_x3680_1600549420}

[*[// T3]{lang="EN-US"}*]{#struct_0_19361_x3680_1355431099}*[定时器已停止]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_x1578192903}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill ha]{lang="EN-US"}]{#struct_0_19361_x3680_907250099}

[\*Jun  3 09:56:15:006 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="EN-US"}

[TRILL-HA: RtBackup TRILL Nickname.]{lang="EN-US"}

[*[// ]{lang="PT-BR"}*]{#struct_0_19361_x3680_985485957}*[实时备份]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[的]{style="font-family:宋体"}[Nickname]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_1952216035}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议本地更新调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill self-originate-update]{lang="EN-US"}]{#struct_0_19361_x3680_1556113838}

[]{#_Toc148517517}[]{#_Toc148610733}[]{#_Toc148517518}[]{#_Toc148610734}[]{#_Toc148517521}[]{#_Toc148610737}[]{#_Toc148517522}[]{#_Toc148610738}[]{#_Toc148517523}[]{#_Toc148610739}[]{#_Toc148517524}[]{#_Toc148610740}[]{#_Toc148517525}[]{#_Toc148610741}[]{#_Toc148517526}[]{#_Toc148610742}[]{#_Toc148517527}[]{#_Toc148610743}[]{#_Toc148517528}[]{#_Toc148610744}[]{#_Toc148517529}[]{#_Toc148610745}[]{#_Toc148517530}[]{#_Toc148610746}[]{#_Toc148517531}[]{#_Toc148610747}[]{#_Toc148517532}[]{#_Toc148610748}[]{#_Toc148517534}[]{#_Toc148610750}[]{#_Toc148517538}[]{#_Toc148610754}[]{#_Toc147113358}[]{#_Toc148517540}[]{#_Toc148610756}[]{#_Toc147113359}[]{#_Toc148517541}[]{#_Toc148610757}[]{#_Toc147113360}[]{#_Toc148517542}[]{#_Toc148610758}[]{#_Toc147113361}[]{#_Toc148517543}[]{#_Toc148610759}[]{#_Toc147113362}[]{#_Toc148517544}[]{#_Toc148610760}[]{#_Toc147113363}[]{#_Toc148517545}[]{#_Toc148610761}[]{#_Toc147113364}[]{#_Toc148517546}[]{#_Toc148610762}[]{#_Toc147113365}[]{#_Toc148517547}[]{#_Toc148610763}[]{#_Toc146534346}[]{#_Toc147113367}[]{#_Toc148517549}[]{#_Toc148610765}[]{#_Toc146534347}[]{#_Toc147113368}[]{#_Toc148517550}[]{#_Toc148610766}[]{#_Toc146534348}[]{#_Toc147113369}[]{#_Toc148517551}[]{#_Toc148610767}[]{#_Toc146534349}[]{#_Toc147113370}[]{#_Toc148517552}[]{#_Toc148610768}[]{#_Toc146534350}[]{#_Toc147113371}[]{#_Toc148517553}[]{#_Toc148610769}[]{#_Toc146534351}[]{#_Toc147113372}[]{#_Toc148517554}[]{#_Toc148610770}[]{#_Toc146534352}[]{#_Toc147113373}[]{#_Toc148517555}[]{#_Toc148610771}[]{#_Toc146534353}[]{#_Toc147113374}[]{#_Toc148517556}[]{#_Toc148610772}[]{#_Toc146534354}[]{#_Toc147113375}[]{#_Toc148517557}[]{#_Toc148610773}[]{#_Toc146534355}[]{#_Toc147113376}[]{#_Toc148517558}[]{#_Toc148610774}[]{#_Toc146534356}[]{#_Toc147113377}[]{#_Toc148517559}[]{#_Toc148610775}[]{#_Toc146534357}[]{#_Toc147113378}[]{#_Toc148517560}[]{#_Toc148610776}[]{#_Toc146534367}[]{#_Toc147113388}[]{#_Toc148517570}[]{#_Toc148610786}[]{#_Toc146534368}[]{#_Toc147113389}[]{#_Toc148517571}[]{#_Toc148610787}[]{#_Toc146534369}[]{#_Toc147113390}[]{#_Toc148517572}[]{#_Toc148610788}[]{#_Toc146534370}[]{#_Toc147113391}[]{#_Toc148517573}[]{#_Toc148610789}[]{#_Toc146534375}[]{#_Toc147113396}[]{#_Toc148517578}[]{#_Toc148610794}[]{#_Toc146534377}[]{#_Toc147113398}[]{#_Toc148517580}[]{#_Toc148610796}[]{#_Toc146534380}[]{#_Toc147113401}[]{#_Toc148517583}[]{#_Toc148610799}[]{#_Toc146534381}[]{#_Toc147113402}[]{#_Toc148517584}[]{#_Toc148610800}[\*May 27 15:46:13:289 2011 Sysname TRILL/7/TRILLDBG: -MDC=1; ]{lang="EN-US"}

[TRILL-ORG: Generating level-1 LSP \[0011.2233.4401.00-00\], Seq 0x00000001, length 71.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19361_x3680_x629946591}*[生成序列号为]{style="font-family:宋体"}[0x00000001]{lang="EN-US"}[、长度为]{style="font-family:宋体"}[71]{lang="EN-US"}[的]{style="font-family:宋体"}[L1 LSP\[0011.2233.4401.00-00\]]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_966858893}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议定时器调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill timer]{lang="NO-BOK"}]{#struct_0_19361_x3680_907184563}

[\*Mar 18 14:28:41:744 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="NO-BOK"}

[TRILL-Timer: Level-1 hello timer expired on the circuit GigabitEthernet1/0/1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19361_x3680_x101863063}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下的]{style="font-family:宋体"}[Level-1 Hello]{lang="EN-US"}[报文发送定时器超时]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_x1799010506}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议]{style="font-family:宋体"}[VR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill vr]{lang="EN-US"}]{#struct_0_19361_x3680_778230701}

[\*Jul  2 17:16:36:406 2013 ]{lang="EN-US"}[Sysname]{lang="NO-BOK"}[ TRILL/7/TRILLDBG: -MDC=1; TRILL-VR: The role change: normal \--\> access.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19361_x3680_1232124762}*[设备角色由普通]{style="font-family:宋体"}[RB]{lang="EN-US"}[变为二层接入设备]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_1590721865}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议邻居报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill adj-packet]{lang="EN-US"}]{#struct_0_19361_x3680_x1436097622}

[\*Jun  3 09:56:12:666 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="EN-US"}

[TRILL-ADJ: Level-1 NBR(0011.2233.4401) two way pass.]{lang="EN-US"}

[*[// Level-1]{lang="EN-US"}*]{#struct_0_19361_x3680_1667280448}*[的邻居（]{style="font-family:宋体"}[0011.2233.4401]{lang="EN-US"}[）双向连接检查通过]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_x1022077935}[打开接收的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill snp-packet receive]{lang="EN-US"}]{#struct_0_19361_x3680_x1109449824}

[\*Mar 18 14:28:41:744 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="EN-US"}

[TRILL-SNP: Send L1 CSNP on circuit GigabitEthernet1/0/1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19361_x3680_907381171}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_572120827}[打开接收的]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议更新报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill update-packet receive]{lang="EN-US"}]{#struct_0_19361_x3680_53659632}

[\*Jun  8 08:31:21:994 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="EN-US"}

[TRILL-UPDT: Parsed nickname 63.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19361_x3680_x506814123}*[解析出]{style="font-family:宋体"}[Nickname]{lang="EN-US"}[为]{style="font-family:宋体"}[63]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_19361_x3680_125617235}[打开]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[协议路由计算调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging trill route]{lang="EN-US"}]{#struct_0_19361_x3680_x1887618111}

[\*Jun  3 09:56:15:911 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;]{lang="EN-US"}

[TRILL-ROUTE: (M0) The event 0X00001F is scheduled.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19361_x3680_907315635}*[调度事件]{style="font-family:宋体"}[0x00001F]{lang="EN-US"}[已设置]{style="font-family:宋体"}*
