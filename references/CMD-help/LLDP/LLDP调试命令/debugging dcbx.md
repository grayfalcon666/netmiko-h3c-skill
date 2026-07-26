::: {#-1146704443 .myid}
[]{#_Toc404784587}[]{#struct_0_x1118_x1357_20226756}[]{#_Toc301269709}[]{#_Toc257809353}[]{#_Toc87257691}

**LLDP \-- LLDP调试命令 \-- debugging dcbx**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x941832717}

[**[debugging]{lang="EN-US"}**[ **dcbx** { **all** \| **error** \| **event** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1118_x1357_377170075}

[**[undo]{lang="EN-US"}**[ **debugging** **dcbx** { **all** \| **error** \| **event** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1118_x1357_1628384426}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_1326408084}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x20457412}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_211338157}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x1357_1572176739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x1357_622954250}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x737411380}

[**[all]{lang="EN-US"}**]{#struct_0_x1118_x1357_264269311}[：表示]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1118_x1357_x1679047942}[：表示]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1118_x1357_x1769143552}[：表示]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1118_x1357_1159138191}[：打开或关闭指定端口上的相关调试信息开关，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示端口类型和端口编号。如果未指定该参数，将打开或关闭所有端口上的相关调试信息开关。]{style="font-family:
宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_184994243}

[**[debugging dcbx]{lang="EN-US"}**]{#struct_0_x1118_x1357_x362194568}[命令用来打开]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging dcbx]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_x1894649049}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging dcbx error]{lang="EN-US"}]{#struct_0_x1118_x1357_379902468}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1594418386}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x1357_623019786}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x810903194}

[[Failed to get local data]{lang="EN-US"}]{#struct_0_x1118_x1357_x298814150}

[[获取本地运行参数失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_643692816}

[[Failed to parse DCBX Control Sub-TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x613507817}

[[解析]{style="font-family:宋体"}[DCBX Control Sub-TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1713551593}[失败]{style="font-family:宋体"}

[[Failed to update remote data by remote TLV(sym)]{lang="EN-US"}]{#struct_0_x1118_x1357_571126740}

[[通过远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_622036746}[更新远端运行参数失败（对称状态机）]{style="font-family:宋体"}

[[Failed to update local data by local configuration(sym)]{lang="EN-US"}]{#struct_0_x1118_x1357_x176578269}

[[通过本端配置更新本地运行参数失败（对称状态机）]{style="font-family:宋体"}]{#struct_0_x1118_x1357_520969610}

[[Failed to update local data by remote TLV(sym)]{lang="EN-US"}]{#struct_0_x1118_x1357_303103202}

[[通过远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1877281331}[更新本端运行参数失败（对称状态机）]{style="font-family:宋体"}

[[Failed to update local data by remote data(Asy)]{lang="EN-US"}]{#struct_0_x1118_x1357_622102282}

[[通过远端数据更新本端运行参数失败（非对称状态机）]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x551878765}

[[Failed to get DCBX data from remote TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1875339294}

[[从远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x118648690}[获取]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to malloc for getting local DCBX data]{lang="EN-US"}]{#struct_0_x1118_x1357_1150711742}

[[获取本地]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_x1559384039}[数据时分配内存失败]{style="font-family:宋体"}

[[Failed to make TLV for buffer overflow]{lang="EN-US"}]{#struct_0_x1118_x1357_622561031}

[[缓冲区溢出时构建]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1608248010}[失败]{style="font-family:宋体"}

[[Failed to update local data (comm)]{lang="EN-US"}]{#struct_0_x1118_x1357_x2050495707}

[[更新本地数据失败（普通状态机）]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x2037231459}

[[Failed to update remote data by remote TLV(comm)]{lang="EN-US"}]{#struct_0_x1118_x1357_1954862826}

[[通过远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_622626567}[失败更新远端运行（普通状态机）]{style="font-family:宋体"}

[[Failed to update remote data by remote TLV(asy)]{lang="EN-US"}]{#struct_0_x1118_x1357_1375647819}

[[通过远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_116947915}[失败更新远端运行（非对称状态机）]{style="font-family:宋体"}

[[Failed to update local data for malloc failed]{lang="EN-US"}]{#struct_0_x1118_x1357_607593222}

[[内存申请失败导致更新本端运行参数失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x1524039331}

[[Failed to get the queue scheduling of local precedence]{lang="EN-US"}]{#struct_0_x1118_x1357_622692103}

[[获取本地优先级队列信息失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x1732080742}

[[Failed to get local configuration for malloc failed(ETS)]{lang="EN-US"}]{#struct_0_x1118_x1357_161315845}

[[内存分配失败导致获取本地配置失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x1784305184}

[[Failed to malloc for getting local PDCBX data]{lang="EN-US"}]{#struct_0_x1118_x1357_622757639}

[[获取]{style="font-family:宋体"}[PDCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_1022700631}[本地数据时内存申请失败]{style="font-family:宋体"}

[[Failed to update local data]{lang="EN-US"}]{#struct_0_x1118_x1357_x942394494}

[[更新本地运行参数失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_667631242}

[[Failed to get PDCBX CB for making TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_622823175}

[[构造]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_59804345}[时获取]{style="font-family:宋体"}[PDCBX]{lang="EN-US"}[控制块失败]{style="font-family:宋体"}

[[Failed to malloc for getting local PFC data]{lang="EN-US"}]{#struct_0_x1118_x1357_1219836321}

[[获取本地]{style="font-family:宋体"}[PFC]{lang="EN-US"}]{#struct_0_x1118_x1357_2010049877}[数据时内存申请失败]{style="font-family:宋体"}

[[Failed to update databy local data(pre)]{lang="EN-US"}]{#struct_0_x1118_x1357_622888711}

[[通过本端数据更新运行参数失败（预标准）]{style="font-family:宋体"}]{#struct_0_x1118_x1357_20226761}

[[Failed to update remote data by remote TLV(pre)]{lang="EN-US"}]{#struct_0_x1118_x1357_213072526}

[[通过远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x874266246}[更新远端运行参数失败（预标准）]{style="font-family:宋体"}

[[Failed to update local data by remote TLV(pre)]{lang="EN-US"}]{#struct_0_x1118_x1357_622954247}

[[通过远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1601240773}[更新本端运行参数失败（预标准）]{style="font-family:宋体"}

[[PDCBX TLV length is invalid]{lang="EN-US"}]{#struct_0_x1118_x1357_1393042478}

[[PDCBX TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x672960644}[长度非法]{style="font-family:宋体"}

[[The version of received DCBX TLV is not supported]{lang="EN-US"}]{#struct_0_x1118_x1357_623019783}

[[本端不支持收到的]{style="font-family:宋体"}[DCBX TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x810903199}[版本]{style="font-family:宋体"}

[[Failed to get PDCBX CB for parsing TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x298617542}

[[解析]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_622036743}[时获取]{style="font-family:宋体"}[PDCBX]{lang="EN-US"}[控制块失败]{style="font-family:宋体"}

[[Failed to handle interface-up/interface-down event for no CB found]{lang="EN-US"}]{#struct_0_x1118_x1357_x176578274}

[[获取]{style="font-family:宋体"}[PDCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_520248715}[控制块失败导致接口]{style="font-family:宋体"}[up/down]{lang="EN-US"}[事件处理失败]{style="font-family:宋体"}

[[Failed to save remote data TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1494511934}

[[保存远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_622102279}[信息失败]{style="font-family:宋体"}

[[Unknown State Machine Type]{lang="EN-US"}]{#struct_0_x1118_x1357_x1743519846}

[[无法识别的状态机类型]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x1205871886}

[[Failed to update DCBX version]{lang="EN-US"}]{#struct_0_x1118_x1357_622561032}

[[更新]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_x1608248013}[版本失败]{style="font-family:宋体"}

[[Unknown DCBX version TLV received]{lang="EN-US"}]{#struct_0_x1118_x1357_x1647211180}

[[接收到未知]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_622626568}[版本的]{style="font-family:宋体"}[TLV ]{lang="EN-US"}

[[DCBX version in TLV is not equal to current version]{lang="EN-US"}]{#struct_0_x1118_x1357_1375647824}

[[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_117144522}[中的]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[版本不等于当前的版本]{style="font-family:宋体"}

[[APP data space is not enough]{lang="EN-US"}]{#struct_0_x1118_x1357_622692104}

[[APP]{lang="EN-US"}]{#struct_0_x1118_x1357_x1732080735}[的数据空间不足]{style="font-family:宋体"}

[[APP data length is incorrect]{lang="EN-US"}]{#struct_0_x1118_x1357_x598526722}

[[APP]{lang="EN-US"}]{#struct_0_x1118_x1357_622757640}[的数据长度错误]{style="font-family:宋体"}

[[APP data format is incorrect]{lang="EN-US"}]{#struct_0_x1118_x1357_x1315951520}

[[APP]{lang="EN-US"}]{#struct_0_x1118_x1357_x1553222493}[的数据模式错误]{style="font-family:宋体"}

[[APP data is reduplicate]{lang="EN-US"}]{#struct_0_x1118_x1357_622823176}

[[APP]{lang="EN-US"}]{#struct_0_x1118_x1357_59804342}[的数据信息出现了重复]{style="font-family:宋体"}

[[Protocol ID is illegal]{lang="EN-US"}]{#struct_0_x1118_x1357_x736478815}

[[协议]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1118_x1357_622888712}[不合法]{style="font-family:宋体"}

[[App TLV data length is incorrect]{lang="EN-US"}]{#struct_0_x1118_x1357_20226762}

[[APP TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1743242610}[数据长度错误]{style="font-family:宋体"}

[[App TLV data length is not a multiple of 3]{lang="EN-US"}]{#struct_0_x1118_x1357_622954248}

[[APP TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1601240772}[数据长度不是]{style="font-family:宋体"}[3]{lang="EN-US"}[的倍数]{style="font-family:宋体"}

[[The LP is *value*,Dot1p is *value*, LP is incorrect]{lang="EN-US"}]{#struct_0_x1118_x1357_1393108014}

[[LP]{lang="EN-US"}]{#struct_0_x1118_x1357_623019784}[不正确]{style="font-family:宋体"}

[[The scheduling algorithm of queue LP *value* is *algorithm*]{lang="EN-US"}]{#struct_0_x1118_x1357_x810903192}

[[LP]{lang="EN-US"}]{#struct_0_x1118_x1357_622036744}[的队列调度算法]{style="font-family:宋体"}

[[ETS TLV data length is incorrect]{lang="EN-US"}]{#struct_0_x1118_x1357_x176578271}

[[ETS TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_520445323}[长度错误]{style="font-family:宋体"}

[[The priority of ETS TLV is invalid]{lang="EN-US"}]{#struct_0_x1118_x1357_622102280}

[[ETS TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x551878767}[的优先级无效]{style="font-family:宋体"}

[[The sum of bandwidth of ETS TLV is not 100%]{lang="EN-US"}]{#struct_0_x1118_x1357_622561029}

[[ETS TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_730404142}[的总带宽不是]{style="font-family:宋体"}[100]{lang="EN-US"}[％]{style="font-family:宋体"}

[[Failed to get local standard DCBX data]{lang="EN-US"}]{#struct_0_x1118_x1357_x1158316291}

[[获取本端标准]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_622626565}[数据错误]{style="font-family:宋体"}

[[Failed to update *name* standard data for malloc failed]{lang="EN-US"}]{#struct_0_x1118_x1357_1375647821}

[[内存申请失败导致更新标准数据失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_622692101}

[[Failed to update *name* standard data while updating data]{lang="EN-US"}]{#struct_0_x1118_x1357_x1732080740}

[[更新数据失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_622757637}

[[Failed to update standard local data for malloc failed]{lang="EN-US"}]{#struct_0_x1118_x1357_1022700633}

[[内存申请失败导致更新本地标准数据失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x942525566}

[[Priority flow control is not in auto mode]{lang="EN-US"}]{#struct_0_x1118_x1357_622823173}

[[PFC]{lang="EN-US"}]{#struct_0_x1118_x1357_59804339}[没有配置成自动模式]{style="font-family:宋体"}

[[The length of PFC TLV is not enough]{lang="EN-US"}]{#struct_0_x1118_x1357_622888709}

[[PFC TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1976541889}[的长度不足]{style="font-family:宋体"}

[[PFC TLV length is error]{lang="EN-US"}]{#struct_0_x1118_x1357_622954245}

[[PFC]{lang="EN-US"}]{#struct_0_x1118_x1357_1601240775}[长度错误]{style="font-family:宋体"}

[[PFC capability value is error]{lang="EN-US"}]{#struct_0_x1118_x1357_1393173550}

[[PFC]{lang="EN-US"}]{#struct_0_x1118_x1357_623019781}[能力值错误]{style="font-family:宋体"}

[[Failed to get PFC work mode]{lang="EN-US"}]{#struct_0_x1118_x1357_x810903197}

[[获取]{style="font-family:宋体"}[PFC]{lang="EN-US"}]{#struct_0_x1118_x1357_622036741}[工作模式失败]{style="font-family:宋体"}

[[The PFC work mode is invalid(work mode = *mode*)]{lang="EN-US"}]{#struct_0_x1118_x1357_x176578276}

[[PFC]{lang="EN-US"}]{#struct_0_x1118_x1357_622102277}[的工作模式无效]{style="font-family:宋体"}

[[Failed to get PFC enabled table]{lang="EN-US"}]{#struct_0_x1118_x1357_x1743519856}

[[PFC]{lang="EN-US"}]{#struct_0_x1118_x1357_x1205937422}[开启表获取失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging dcbx event]{lang="EN-US"}]{#struct_0_x1118_x1357_622561030}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1580193215}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x1608248011}

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x484411766}

[[Local data is not updated(sym)]{lang="EN-US"}]{#struct_0_x1118_x1357_x882853493}

[[本地运行参数未更新（对称状态机）]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x723660582}

[[Changed flag is not set(sym)]{lang="EN-US"}]{#struct_0_x1118_x1357_x2007367263}

[[未设置变动标志位（对称状态机）]{style="font-family:宋体"}]{#struct_0_x1118_x1357_478630109}

[[Driver is not set by remote TLV(sym)]{lang="EN-US"}]{#struct_0_x1118_x1357_622626566}

[[配置参数已通过远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1375647818}[更新，未设置驱动（对称状态机）]{style="font-family:宋体"}

[[Driver is not set by remote TLV(asy)]{lang="EN-US"}]{#struct_0_x1118_x1357_116882379}

[[未通过远端]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_588755100}[设置驱动（非对称状态机）]{style="font-family:宋体"}

[[DCBX-data is not set to driver for getting cfg-data failed]{lang="EN-US"}]{#struct_0_x1118_x1357_x1772823698}

[[获取配置数据失败，未设置驱动]{style="font-family:宋体"}]{#struct_0_x1118_x1357_837857889}

[[PDCBX version changed to *version*]{lang="EN-US"}]{#struct_0_x1118_x1357_2132584810}

[[PDCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_622692102}[版本切换至]{style="font-family:宋体"}*[version]{lang="EN-US"}*

[[Local peer data changed]{lang="EN-US"}]{#struct_0_x1118_x1357_x1732080741}

[[本地运行参数改变]{style="font-family:宋体"}]{#struct_0_x1118_x1357_1727399786}

[[Changed flag is not set (std)]{lang="EN-US"}]{#struct_0_x1118_x1357_x267891347}

[[未设置变动标志位（标准类型）]{style="font-family:宋体"}]{#struct_0_x1118_x1357_40932959}

[[Current version is *version*]{lang="EN-US"}]{#struct_0_x1118_x1357_622757638}

[[当前版本类型]{style="font-family:宋体"}]{#struct_0_x1118_x1357_1022700632}

[[Current state machine is *state*]{lang="EN-US"}]{#struct_0_x1118_x1357_x942460030}

[[当前状态机类型]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x560983729}

[[DCBX version changed from *version* to *version*]{lang="EN-US"}]{#struct_0_x1118_x1357_x1123385477}

[[DCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_x1542217822}[版本切换]{style="font-family:宋体"}

[[Process DCBX neighbor delete event]{lang="EN-US"}]{#struct_0_x1118_x1357_622823174}

[[处理]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1118_x1357_59804344}[邻居删除事件]{style="font-family:宋体"}

[[There is no DCBX TLV in message]{lang="EN-US"}]{#struct_0_x1118_x1357_x1118815839}

[[消息中无]{style="font-family:宋体"}[DCBX TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1072953020}

[[The TSA Table of ETS TLV is unknown]{lang="EN-US"}]{#struct_0_x1118_x1357_622888710}

[[ETS TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_20226760}[中的]{style="font-family:宋体"}[TSA]{lang="EN-US"}[表不识别]{style="font-family:宋体"}

[[Source data is equal to destination data for ETS Recommendation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x2125579634}

[[ETS RecommendationTLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1323500384}[源数据等于目的数据]{style="font-family:宋体"}

[[Source data is not equal to destination data for ETS Recommendation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1445737285}

[[ETS RecommendationTLV]{lang="EN-US"}]{#struct_0_x1118_x1357_622954246}[源数据不等于目的数据]{style="font-family:宋体"}

[[Update local ETS Recommendation TLV successfully]{lang="EN-US"}]{#struct_0_x1118_x1357_1601240774}

[[更新本端]{style="font-family:宋体"}[ETS Recommendation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1393239086}[成功]{style="font-family:宋体"}

[[Update remote ETS Recommendation TLV successfully]{lang="EN-US"}]{#struct_0_x1118_x1357_916078452}

[[更新远端]{style="font-family:宋体"}[ETS Recommendation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_623019782}[成功]{style="font-family:宋体"}

[[There is no DCBX ETS Recommendation TLV in message]{lang="EN-US"}]{#struct_0_x1118_x1357_x810903198}

[[消息中无]{style="font-family:宋体"}[DCBX ETS Recommendation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x298552006}

[[There is no DCBX PFC Configuration TLV in message]{lang="EN-US"}]{#struct_0_x1118_x1357_x897434416}

[[消息中无]{style="font-family:宋体"}[DCBX ETS Configuration TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_622036742}

[[Update local PFC TLV successfully]{lang="EN-US"}]{#struct_0_x1118_x1357_x176578273}

[[更新本地]{style="font-family:宋体"}[PFC TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_520314251}[成功]{style="font-family:宋体"}

[[Update remote PFC TLV successfully]{lang="EN-US"}]{#struct_0_x1118_x1357_622102278}

[[更新远端]{style="font-family:宋体"}[PFC TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1743519847}[成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_360212055}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x1357_869276483}[设备通过端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[与另一台设备相连，在本设备上打开]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging dcbx event]{lang="EN-US"}]{#struct_0_x1118_x1357_x336575331}

[\*Mar 23 14:38:34:266 2010 Sysname DCBX/7/EVENT: PDCBX version changed to 1.]{lang="EN-US"}

[*[// PDCBX]{lang="EN-US"}*]{#struct_0_x1118_x1357_x1408590996}*[版本切换至]{style="font-family:宋体"}[1.00]{lang="EN-US"}[版本]{style="font-family:宋体"}*

::: {#1217530099 .myid}
[]{#_Toc404784588}[]{#struct_0_x1118_x1357_x531857165}[]{#_Toc301269710}

**LLDP \-- LLDP调试命令 \-- debugging lldp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x1167948477}

[**[debugging lldp]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \[ **interface** *interface-type interface-number* \] \| **packet** \[ **receive** \| **send** \] \[ **interface** *interface-type interface-number* \] \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750091962}

[**[undo debugging lldp]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \[ **interface** *interface-type interface-number* \] \| **packet** \[ **receive** \| **send** \] \[ **interface** *interface-type interface-number* \] }]{lang="EN-US"}]{#struct_0_x1118_x1357_1966804769}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_1213474102}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1118_x1357_1648285453}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x521804213}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_x1357_1812606832}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_x1357_1155067414}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_141948115}

[**[all]{lang="EN-US"}**]{#struct_0_x1118_x1357_1865453569}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1118_x1357_x1750026426}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1118_x1357_565418839}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x1118_x1357_x1701660468}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1118_x1357_1299800483}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1118_x1357_295851949}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[接收报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1118_x1357_x1255388953}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[发送报文调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1118_x1357_1733654935}[：打开或关闭指定端口上的相关调试信息开关，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示端口类型和端口编号。如果未指定该参数，将打开或关闭所有端口上的相关调试信息开关。]{style="font-family:
宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1118_x1357_x1021885845}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的详细调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x1638361383}

[**[debugging lldp]{lang="EN-US"}**]{#struct_0_x1118_x1357_x219076137}[命令用来打开]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging lldp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749960890}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging lldp error]{lang="EN-US"}]{#struct_0_x1118_x1357_1417919935}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1584443767}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x1123273670}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x2036804210}

[[The packet is too short]{lang="EN-US"}]{#struct_0_x1118_x1357_x517628205}

[[报文长度过短]{style="font-family:宋体"}]{#struct_0_x1118_x1357_1829140406}

[[The packet is too long]{lang="EN-US"}]{#struct_0_x1118_x1357_1081488321}

[[报文长度过长]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x1749895354}

[[TLV exceeds end of the frame, type: *type*]{lang="EN-US"}]{#struct_0_x1118_x1357_x522156787}

[[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x259123306}[长度超过报文物理总长度，]{style="font-family:宋体"}[TLV]{lang="EN-US"}[的类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[End TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x678873072}

[[End of LLDPDU TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749829818}[长度错误]{style="font-family:宋体"}

[[Chassis ID TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1705230629}

[[Chassis ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1442703483}[长度错误]{style="font-family:宋体"}

[[Chassis ID TLV MAC length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x326578478}

[[Chassis ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_741385748}[子类型为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的长度错误]{style="font-family:宋体"}

[[Receive repeated chassis ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749764282}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Chassis ID TLV ]{lang="EN-US"}]{#struct_0_x1118_x1357_x267398017}

[[Chassis ID TLV subtype error]{lang="EN-US"}]{#struct_0_x1118_x1357_x323191796}

[[Chassis ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_622097769}[子类型非法]{style="font-family:宋体"}

[[Port ID TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x556752290}

[[Port ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749698746}[长度错误]{style="font-family:宋体"}

[[Port ID TLV MAC length error]{lang="EN-US"}]{#struct_0_x1118_x1357_68525011}

[[Chassis ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x315842609}[子类型为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的长度错误]{style="font-family:宋体"}

[[Receive repeated port ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1717955051}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Port ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1291608529}

[[Port ID TLV subtype error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749633210}

[[Port ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_851640942}[子类型非法]{style="font-family:宋体"}

[[TTL TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x544518520}

[[Time to Live TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1911572984}[长度错误]{style="font-family:宋体"}

[[Receive repeated TTL TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1163342875}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Time to Live TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750616250}

[[Receive repeated Port Description TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1266653746}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Port Description TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x228636736}

[[Receive repeated System Name TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_461903969}

[[收到的报文中含有重复的]{style="font-family:宋体"}[System Name TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750550714}

[[Receive repeated System Description TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x138361663}

[[收到的报文中含有重复的]{style="font-family:宋体"}[System Description TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_2082762141}

[[Receive repeated System Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x855604832}

[[收到的报文中含有重复的]{style="font-family:宋体"}[System Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750091961}

[[System Capabilities TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x762078586}

[[System Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x562267265}[长度错误]{style="font-family:宋体"}

[[System Capability TLV conflict: Support: 0x%x, Enable: 0x%x]{lang="EN-US"}]{#struct_0_x1118_x1357_697520344}

[[System Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750026425}[信息错误，支持能力为]{style="font-family:宋体"}[0x%x]{lang="EN-US"}[与开启能力为]{style="font-family:宋体"}[0x%x]{lang="EN-US"}[相矛盾]{style="font-family:宋体"}

[[System Capability TLV station-only error: 0x%x]{lang="EN-US"}]{#struct_0_x1118_x1357_x1000665102}

[[System Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1428765586}[信息错误，表示支持功能的第七位置位，且仍有其它有效置位]{style="font-family:宋体"}

[[Receive repeated Management Address TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749960889}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Management Address TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_208131890}

[[Management Address TLV total length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1432435338}

[[Management Address TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_739063111}[总长度错误]{style="font-family:宋体"}

[[Management Address TLV address length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749895353}

[[Management Address TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1850496208}[管理地址长度错误]{style="font-family:宋体"}

[[Management Address TLV conflict error]{lang="EN-US"}]{#struct_0_x1118_x1357_1136683243}

[[Management Address TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749829817}[解析出的长度和总长度相矛盾]{style="font-family:宋体"}

[[Management Address TLV OID length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x2108515156}

[[Management Address TLV OID]{lang="EN-US"}]{#struct_0_x1118_x1357_1986125120}[长度错误]{style="font-family:
  宋体"}

[[Management Address TLV subtype error]{lang="EN-US"}]{#struct_0_x1118_x1357_1905311320}

[[Management Address TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749764281}[子类型非法]{style="font-family:宋体"}

[[Management Address TLV if subtype error]{lang="EN-US"}]{#struct_0_x1118_x1357_x670682544}

[[Management Address TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x2098729990}[接口子类型非法]{style="font-family:宋体"}

[[Management Address TLV format conflict]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749698745}

[[Management Address TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1497558930}[本端封装格式与接收到的封装格式不一致]{style="font-family:宋体"}

[[Management Address TLV IPv4 address error]{lang="EN-US"}]{#struct_0_x1118_x1357_x542586118}

[[Management Address TLV IPv4]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749633209}[地址错误]{style="font-family:
  宋体"}

[[Port VLAN ID TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_2061428987}

[[Port VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x541678865}[长度错误]{style="font-family:宋体"}

[[Receive repeated Port VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750616249}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Port VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1105933713}

[[Port VLAN ID TLV VLAN IDerror]{lang="EN-US"}]{#struct_0_x1118_x1357_936554025}

[[Port VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750550713}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Port And Protocol VLAN ID TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_1427722278}

[[Port And Protocol VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1250761916}[长度错误]{style="font-family:
  宋体"}

[[Port And Protocol VLAN ID TLV VLAN ID error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750091964}

[[Port And protocol VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1521593473}[的]{style="font-family:
  宋体"}[VLAN ID]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Receive repeated Port And Protocol ID VLAN TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750026428}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Port And Protocol VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x597380575}

[[VLAN Name TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_1277699548}

[[VLAN Name TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749960892}[长度错误]{style="font-family:宋体"}

[[Vlan Name string length error]{lang="EN-US"}]{#struct_0_x1118_x1357_255120521}

[[VLAN Name TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749895356}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[名称长度错误]{style="font-family:宋体"}

[[Vlan Name TLV VLAN ID error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1684956201}

[[VLAN Name TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_668596889}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Receive repeated VLAN Name TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749829820}

[[收到的报文中含有重复的]{style="font-family:宋体"}[VLAN Name TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1349196877}

[[Protocol Identity TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x867507023}

[[Protocol Identity TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749764284}[长度错误]{style="font-family:宋体"}

[[Receive repeated Protocol Identity TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1073967071}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Protocol Identity TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749698748}

[[MAC/ PHY Configuration/Status TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x738044043}

[[MAC/PHY Configuration/Status TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1094447298}[长度错误]{style="font-family:
  宋体"}

[[Receive repeated MAC/PHY Configuration/Status TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749633212}

[[收到的报文中含有重复的]{style="font-family:宋体"}[MAC/PHY Configuration/Status TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_2014440356}

[[MAC/PHY Configuration/Status TLV MAU type error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750616252}

[[MAC/PHY Configuration/Status TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x103854332}[中端口支持]{style="font-family:
  宋体"}[MAU]{lang="EN-US"}[类型非法]{style="font-family:宋体"}

[[Power via MDI TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750550716}

[[Power via MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1024437751}[长度错误]{style="font-family:宋体"}

[[Receive repeated power via MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x306397508}

[[收到的报文中含有重复的]{style="font-family:宋体"}[power via MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750091963}

[[Power via MDI TLV power pair error]{lang="EN-US"}]{#struct_0_x1118_x1357_400720828}

[[Power via MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750026427}[中]{style="font-family:宋体"}[power pair]{lang="EN-US"}[值错误]{style="font-family:宋体"}

[[Power via MDI TLV power class error]{lang="EN-US"}]{#struct_0_x1118_x1357_2131502780}

[[Power via MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749960891}[中]{style="font-family:宋体"}[power class]{lang="EN-US"}[值错误]{style="font-family:宋体"}

[[Power via MDI TLV PD requested power value error]{lang="EN-US"}]{#struct_0_x1118_x1357_1195537047}

[[Power via MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1440494431}[中]{style="font-family:宋体"}[PD requested power value]{lang="EN-US"}[值错误]{style="font-family:宋体"}

[[Power via MDI TLV PSE allocated power value error]{lang="EN-US"}]{#struct_0_x1118_x1357_1195078295}

[[Power via MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1195143831}[中]{style="font-family:宋体"}[PSE allocated power value]{lang="EN-US"}[值错误]{style="font-family:宋体"}

[[Link Aggregation TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x148164006}

[[Link Aggregation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749895355}[长度错误]{style="font-family:宋体"}

[[Link Aggregation TLV member port ID error]{lang="EN-US"}]{#struct_0_x1118_x1357_1043927154}

[[Link Aggregation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1134427053}[中聚合成员端口]{style="font-family:宋体"}[ID]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Receive repeated Link Aggregation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749829819}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Link Aggregation TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1023652726}

[[Max Frame Size TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749764283}

[[Max Frame Size TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1833481958}[长度错误]{style="font-family:宋体"}

[[Receive repeated Max Frame Size TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749698747}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Max Frame Size TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1634608952}

[[Power Stateful Control TLV or EEE TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749633211}

[[Power Stateful Control TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1877242413}[或者]{style="font-family:
  宋体"}[EEE TLV]{lang="EN-US"}[长度错误]{style="font-family:宋体"}

[[Receive repeated Power Stateful Control or EEE TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750616251}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Power Stateful Control TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1462229609}[或者]{style="font-family:宋体"}[EEE TLV]{lang="EN-US"}

[[Power Stateful Control TLV type error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750550715}

[[Power Stateful Control TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1704445604}[中]{style="font-family:
  宋体"}[type]{lang="EN-US"}[信息错误]{style="font-family:宋体"}

[[Power Stateful Control TLV source error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750091966}

[[Power Stateful Control TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x358794059}[中]{style="font-family:
  宋体"}[source]{lang="EN-US"}[信息错误]{style="font-family:宋体"}

[[Power Stateful Control TLV priority error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750026430}

[[Power Stateful Control TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x241084679}[中]{style="font-family:
  宋体"}[priority]{lang="EN-US"}[信息错误]{style="font-family:宋体"}

[[MED capabilities TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749960894}

[[LLDP-MED Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x551448533}[长度错误]{style="font-family:宋体"}

[[Receive repeated MED capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749895358}

[[收到的报文中含有重复的]{style="font-family:宋体"}[LLDP-MED Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1803442041}

[[MED capability TLV cap error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749829822}

[[LLDP-MED Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1782971005}[中支持]{style="font-family:宋体"}[capabilities TLV]{lang="EN-US"}[的未置位]{style="font-family:宋体"}

[[MED capability TLV device type error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749764286}

[[LLDP-MED Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_2058200811}[中支持]{style="font-family:宋体"}[pse]{lang="EN-US"}[和]{style="font-family:宋体"}[pd]{lang="EN-US"}[扩展]{style="font-family:宋体"}[MDI TLV]{lang="EN-US"}[标志均置位]{style="font-family:宋体"}

[[MED capability TLV MED class error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749698750}

[[LLDP-MED Capabilities TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1094208867}[中表示设备类型的值非法]{style="font-family:宋体"}

[[MED network policy TLV conflict with MED capability]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749633214}

[[MED capability]{lang="EN-US"}]{#struct_0_x1118_x1357_x1473957886}[不支持发送]{style="font-family:宋体"}[Network policy TLV]{lang="EN-US"}

[[MED network policy TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750616254}

[[Network Policy TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_702714722}[长度错误]{style="font-family:宋体"}

[[Receive repeated Network Policy TLV, type: *type*]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750550718}

[[收到的报文中含有重复的类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x1118_x1357_x2107730131}[的]{style="font-family:宋体"}[Network Policy TLV]{lang="EN-US"}

[[Receive repeated Network Policy unknown TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750091965}

[[收到的报文中含有重复的类型未知的]{style="font-family:宋体"}[Network Policy TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1207289882}

[[MED power MDI TLV conflict with MED capability]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750026429}

[[MED capability]{lang="EN-US"}]{#struct_0_x1118_x1357_968703366}[不支持发送]{style="font-family:宋体"}[MED power MDI TLV]{lang="EN-US"}

[[MED power MDI TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749960893}

[[MED power MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749895357}[长度错误]{style="font-family:宋体"}

[[Receive repeated MED power MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x118872260}

[[收到的报文中含有重复的]{style="font-family:宋体"}[MED power MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749829821}

[[MED power MDI TLV type error]{lang="EN-US"}]{#struct_0_x1118_x1357_1379686478}

[[MED power MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749764285}[信息中]{style="font-family:宋体"}[power type]{lang="EN-US"}[位段非法]{style="font-family:宋体"}

[[MED power MDI TLV PSE(PD) type error]{lang="EN-US"}]{#struct_0_x1118_x1357_1654916284}

[[MED power MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749698749}[信息中表示]{style="font-family:宋体"}[power type]{lang="EN-US"}[位段与]{style="font-family:宋体"}[MED capability]{lang="EN-US"}[中不一致，不同为]{style="font-family:宋体"}[pse]{lang="EN-US"}[或者]{style="font-family:宋体"}[pd]{lang="EN-US"}

[[MED power MDI TLV PSE source error]{lang="EN-US"}]{#struct_0_x1118_x1357_828039898}

[[MED power MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1749633213}[信息中表示]{style="font-family:宋体"}[power source]{lang="EN-US"}[的位段的值非法]{style="font-family:宋体"}

[[MED power MDI TLV PSE(PD) priority error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750616253}

[[MED power MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1669938273}[信息中表示]{style="font-family:宋体"}[power priority]{lang="EN-US"}[的位段的值非法]{style="font-family:宋体"}

[[MED power MDI TLV power value error]{lang="EN-US"}]{#struct_0_x1118_x1357_x1750550717}

[[MED power MDI TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x541646190}[信息中表示]{style="font-family:宋体"}[power value]{lang="EN-US"}[的位段的值非法]{style="font-family:宋体"}

[[MED location ID TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x184008021}

[[Location Identification TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1978375984}[长度错误]{style="font-family:
  宋体"}

[[MED location ID TLV LCI length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x183942485}

[[Location Identification TLV LCI]{lang="EN-US"}]{#struct_0_x1118_x1357_x183876949}[长度错误]{style="font-family:
  宋体"}

[[MED location ID TLV format error]{lang="EN-US"}]{#struct_0_x1118_x1357_135343776}

[[Location Identification TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183811413}[格式错误]{style="font-family:
  宋体"}

[[Receive repeated Location ID TLV, format: *format*]{lang="EN-US"}]{#struct_0_x1118_x1357_x183745877}

[[收到的报文中含有重复的类型为]{style="font-family:宋体"}*[format]{lang="EN-US"}*]{#struct_0_x1118_x1357_2071956499}[的]{style="font-family:宋体"}[Location Identification TLV]{lang="EN-US"}

[[MED Location TLV conflict with MED capability]{lang="EN-US"}]{#struct_0_x1118_x1357_x183680341}

[[MED capability]{lang="EN-US"}]{#struct_0_x1118_x1357_112543024}[不支持发送]{style="font-family:宋体"}[Location Identification TLV]{lang="EN-US"}

[[MED Inventory TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x183614805}

[[MED inventory TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183549269}[长度错误]{style="font-family:宋体"}

[[MED Inventory TLV conflict with MED capability]{lang="EN-US"}]{#struct_0_x1118_x1357_538055824}

[[MED capability]{lang="EN-US"}]{#struct_0_x1118_x1357_x184532309}[不支持发送]{style="font-family:宋体"}[Inventory TLV]{lang="EN-US"}

[[Receive repeated MED Inventory TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x184466773}

[[收到的报文中含有重复的]{style="font-family:宋体"}[Inventory TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1919233573}

[[Failed to update neighbor information]{lang="EN-US"}]{#struct_0_x1118_x1357_x184008020}

[[更新邻居信息失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x183942484}

[[No chassis ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1851237343}

[[没有]{style="font-family:宋体"}[Chassis ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183876948}

[[No port ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183811412}

[[没有]{style="font-family:宋体"}[Port ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_2043132424}

[[No TTL TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183745876}

[[没有]{style="font-family:宋体"}[Time to Live TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183680340}

[[Dropped neighbor because of too many neighbors]{lang="EN-US"}]{#struct_0_x1118_x1357_112477488}

[[由于邻居过多而丢弃邻居]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x183614804}

[[Failed to get port ID]{lang="EN-US"}]{#struct_0_x1118_x1357_x183549268}

[[获取]{style="font-family:宋体"}[Port ID]{lang="EN-US"}]{#struct_0_x1118_x1357_537990288}[失败]{style="font-family:宋体"}

[[Failed to create gcb save timer]{lang="EN-US"}]{#struct_0_x1118_x1357_x184532308}

[[创建定时保存定时器失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x184466772}

[[Failed to create Interface Data]{lang="EN-US"}]{#struct_0_x1118_x1357_x184008023}

[[创建接口数据失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_1978244912}

[[Failed to delete configure data from DBM]{lang="EN-US"}]{#struct_0_x1118_x1357_x183942487}

[[主控板删除]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x1118_x1357_x183876951}[配置数据失败]{style="font-family:宋体"}

[[Failed to set interface statistic data to DBM]{lang="EN-US"}]{#struct_0_x1118_x1357_134819487}

[[保存接口统计数据到]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x1118_x1357_x183811415}[失败]{style="font-family:宋体"}

[[Failed to register interface event]{lang="EN-US"}]{#struct_0_x1118_x1357_x183745879}

[[注册接口事件失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_2072874003}

[[Failed to receive event packet]{lang="EN-US"}]{#struct_0_x1118_x1357_x183680343}

[[接收事件报文失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x183614807}

[[Failed to create neighbor aging timer]{lang="EN-US"}]{#struct_0_x1118_x1357_x183549271}

[[创建邻居老化定时器失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_537531537}

[[Failed to send message]{lang="EN-US"}]{#struct_0_x1118_x1357_x184532311}

[[发包失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x184466775}

[[Failed to refresh timer]{lang="EN-US"}]{#struct_0_x1118_x1357_x184008022}

[[刷新定时器失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_1978179376}

[[Failed to announce timer]{lang="EN-US"}]{#struct_0_x1118_x1357_x183942486}

[[通知定时器处理失败]{style="font-family:宋体"}]{#struct_0_x1118_x1357_x183876950}

[[VLAN name string is too long]{lang="EN-US"}]{#struct_0_x1118_x1357_x183811414}

[[VLAN]{lang="EN-US"}]{#struct_0_x1118_x1357_x183745878}[名称的长度过长]{style="font-family:宋体"}

[[Failed to send nearest customer packet, because connecting EVB error failed]{lang="EN-US"}]{#struct_0_x1118_x1357_2072808467}

[[由于连接]{style="font-family:宋体"}[EVB]{lang="EN-US"}]{#struct_0_x1118_x1357_x183680342}[失败，不能发送最近客户桥代理类型报文]{style="font-family:宋体"}

[[Failed to send nearest customer packet, because no EVB TLV is enabled]{lang="EN-US"}]{#struct_0_x1118_x1357_x183614806}

[[由于未开启]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183549270}[，不能发送最近客户桥代理类型报文]{style="font-family:宋体"}

[[Failed to send nearest customer packet, because of no EVB data]{lang="EN-US"}]{#struct_0_x1118_x1357_x184532310}

[[由于没有]{style="font-family:宋体"}[EVB]{lang="EN-US"}]{#struct_0_x1118_x1357_x1168942186}[数据，不能发送最近客户桥代理类型报文]{style="font-family:宋体"}

[[Failed to send nearest non-tpmr packet, because of connecting EVB error]{lang="EN-US"}]{#struct_0_x1118_x1357_x184466774}

[[由于连接]{style="font-family:宋体"}[EVB]{lang="EN-US"}]{#struct_0_x1118_x1357_x184008025}[失败，不能发送最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[代理类型报文]{style="font-family:宋体"}

[[Failed to send nearest non-tpmr packet, because of no enabled EVB TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183942489}

[[由于未开启]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x1850385375}[，不能发送最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[代理类型报文]{style="font-family:宋体"}

[[Failed to send nearest non-tpmr packet, because of no EVB data]{lang="EN-US"}]{#struct_0_x1118_x1357_x183876953}

[[由于没有]{style="font-family:宋体"}[EVB]{lang="EN-US"}]{#struct_0_x1118_x1357_x183811417}[数据，不能发送最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[代理类型报文]{style="font-family:宋体"}

[[CDCP TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x183549273}

[[接收的]{style="font-family:宋体"}[CDCP TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x184532313}[长度错误]{style="font-family:宋体"}

[[Receive repeated CDCP TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x184466777}

[[收到的报文中含有重复的]{style="font-family:宋体"}[CDCP TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x184008024}

[[EVB TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_1978572592}

[[接收的]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183942488}[长度错误]{style="font-family:宋体"}

[[Receive repeated EVB TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183876952}

[[收到的报文中含有重复的]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183811416}

[[Receive repeated Management VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183745880}

[[接收到重复的管理]{style="font-family:宋体"}[VLAN TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x183680344}

[[Management VID TLV length is error]{lang="EN-US"}]{#struct_0_x1118_x1357_x183614808}

[[管理]{style="font-family:宋体"}[VLAN TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x654829672}[长度错误]{style="font-family:宋体"}

[[Management VID TLV vlan id is error]{lang="EN-US"}]{#struct_0_x1118_x1357_x183549272}

[[管理]{style="font-family:宋体"}[VLAN TLV VLAN ID]{lang="EN-US"}]{#struct_0_x1118_x1357_x184532312}[错误]{style="font-family:宋体"}

[[Received a TLV (port and protocol VLAN ID TLV) that is not supported but enabled.]{lang="EN-US"}]{#struct_0_x1118_x1357_x184466776}

[[收到一个不支持但已开启的错误的]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1382075920}[（]{style="font-family:宋体"}[Port And Protocol VLAN ID TLV]{lang="EN-US"}[）]{style="font-family:宋体"}

[[CN TLV length error]{lang="EN-US"}]{#struct_0_x1118_x1357_x951157947}

[[接收的]{style="font-family:宋体"}[CN TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x950961339}[长度错误]{style="font-family:宋体"}

[[CN TLV value error]{lang="EN-US"}]{#struct_0_x1118_x1357_x951026875}

[[接收的]{style="font-family:宋体"}[CN TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x951354555}[的值错误]{style="font-family:宋体"}

[[Received repeated CN TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_124723137}

[[收到的报文中含有重复的]{style="font-family:宋体"}[CN TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_x951420091}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging lldp event]{lang="EN-US"}]{#struct_0_x1118_x1357_x804143493}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1550145965}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x1485407171}

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x605731002}

[[MED neighbor refresh send shutdown]{lang="EN-US"}]{#struct_0_x1118_x1357_x1217763809}

[[MED]{lang="EN-US"}]{#struct_0_x1118_x1357_1382141456}[邻居变化，发送]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[MED neighbor refresh send normal]{lang="EN-US"}]{#struct_0_x1118_x1357_x398201869}

[[刷新]{style="font-family:宋体"}[MED]{lang="EN-US"}]{#struct_0_x1118_x1357_x1133334302}[邻居]{style="font-family:宋体"}

[[MED neighbor number changed to zero]{lang="EN-US"}]{#struct_0_x1118_x1357_1622264937}

[[MED]{lang="EN-US"}]{#struct_0_x1118_x1357_1803510196}[邻居个数变为零]{style="font-family:宋体"}

[[Board *n* insertion event happened]{lang="EN-US"}]{#struct_0_x1118_x1357_x1330633904}

[[板]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1118_x1357_1382206992}[插入事件发生]{style="font-family:宋体"}

[[Creation/Deletion/Active/Deactive/Up/Down/Link up/Link down event happened.]{lang="EN-US"}]{#struct_0_x1118_x1357_1195143829}

[[接口创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1118_x1357_1195209365}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[激活]{style="font-family:宋体"}[/]{lang="EN-US"}[去激活]{style="font-family:宋体"}[/up/down]{lang="EN-US"}[事件发生]{style="font-family:宋体"}

[[Reinit/Tx-inter/Tx-delay/Fast send/Polling/Gsave/Nb age/trap timer already exists]{lang="EN-US"}]{#struct_0_x1118_x1357_x461905776}

[[重新初始化]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1118_x1357_1439197355}[发送间隔]{style="font-family:宋体"}[/]{lang="EN-US"}[发送延迟]{style="font-family:宋体"}[/]{lang="EN-US"}[快发]{style="font-family:宋体"}[/]{lang="EN-US"}[轮询]{style="font-family:宋体"}[/]{lang="EN-US"}[定时保存]{style="font-family:宋体"}[/Trap]{lang="EN-US"}[定时器已经存在]{style="font-family:宋体"}

[[Update statistic on unsupported port]{lang="EN-US"}]{#struct_0_x1118_x1357_804108080}

[[在不支持的接口上更新接口统计数据]{style="font-family:宋体"}]{#struct_0_x1118_x1357_1382272528}

[[LLDP exit]{lang="EN-US"}]{#struct_0_x1118_x1357_x1962307972}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_x562843504}[去初始化]{style="font-family:宋体"}

[[LLDP received terminal signal]{lang="EN-US"}]{#struct_0_x1118_x1357_x440303720}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_1362140244}[已经收到终端信号]{style="font-family:宋体"}

[[packet encapsulation format is not matched]{lang="EN-US"}]{#struct_0_x1118_x1357_1382338064}

[[接收到的报文封装格式与本端报文封装格式不符合]{style="font-family:宋体"}]{#struct_0_x1118_x1357_1556861627}

[[LLDP/CDP packet2CPU control:]{lang="EN-US"}]{#struct_0_x1118_x1357_x1067012241}

[[ifIndex: *IfIndex*]{lang="EN-US"}]{#struct_0_x1118_x1357_x1494364813}

[[value: *value*]{lang="EN-US"}]{#struct_0_x1118_x1357_1382403600}

[[result: *result*]{lang="EN-US"}]{#struct_0_x1118_x1357_x1187184045}

[[接口（接口索引为]{style="font-family:宋体"}*[IfIndex]{lang="EN-US"}*]{#struct_0_x1118_x1357_x1494185640}[）下发协议控制状态（]{style="font-family:宋体"}*[value]{lang="EN-US"}*[值为开启或者关闭）的结果（]{style="font-family:宋体"}*[result]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[LLDP get index info \[Request\]]{lang="EN-US"}]{#struct_0_x1118_x1357_1078965757}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_1382469136}[获取下一个数据的当前索引信息]{style="font-family:宋体"}

[[LLDP get index info \[Response\]]{lang="EN-US"}]{#struct_0_x1118_x1357_x1950136654}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_128288878}[获取的下一个数据的索引信息]{style="font-family:宋体"}

[[Syns send data with len *len*]{lang="EN-US"}]{#struct_0_x1118_x1357_x581512806}

[[syns]{lang="EN-US"}]{#struct_0_x1118_x1357_x401122412}[向]{style="font-family:宋体"}[client]{lang="EN-US"}[发送数据长度为]{style="font-family:宋体"}*[len]{lang="EN-US"}*[的数据]{style="font-family:宋体"}

[[LLDP sent message to EVB, result is *value*]{lang="EN-US"}]{#struct_0_x1118_x1357_1382534672}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_x438220490}[向]{style="font-family:宋体"}[EVB]{lang="EN-US"}[发送消息，发送的结果是]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[LLDP processed EVB message, EVB enable value is *n*, data length is *length*]{lang="EN-US"}]{#struct_0_x1118_x1357_823124456}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_x28287880}[处理]{style="font-family:宋体"}[EVB]{lang="EN-US"}[消息，]{style="font-family:宋体"}[EVB]{lang="EN-US"}[开启值为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[LLDP processed EVB message and data information is no change]{lang="EN-US"}]{#struct_0_x1118_x1357_1381551632}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_494005097}[处理]{style="font-family:宋体"}[EVB]{lang="EN-US"}[消息，数据信息没有发生变化]{style="font-family:宋体"}

[[LLDP processed EVB message and restarted sending machine]{lang="EN-US"}]{#struct_0_x1118_x1357_x22794546}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_243639270}[处理]{style="font-family:宋体"}[EVB]{lang="EN-US"}[消息并重新启动发送状态机]{style="font-family:宋体"}

[[The max credit is zero]{lang="EN-US"}]{#struct_0_x1118_x1357_1381617168}

[[LLDP]{lang="EN-US"}]{#struct_0_x1118_x1357_x307505925}[发包限速令牌桶当前值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[No end TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1195340436}

[[没有]{style="font-family:宋体"}[End of LLDPDU TLV]{lang="EN-US"}]{#struct_0_x1118_x1357_1195405972}

[[Set EEE TxSystemValue=*n*,RxSystemValue=*n*]{lang="EN-US"}]{#struct_0_x1118_x1357_x1209061948}

[[向设备设置发送及等待接收来自对端的]{style="font-family:宋体"}[EEE]{lang="EN-US"}]{#struct_0_x1118_x1357_x602848615}[的时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[，单位为微秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging lldp fsm]{lang="EN-US"}]{#struct_0_x1118_x1357_639907912}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1555155438}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x279109193}

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x1357_825485442}

[[Receive state machine change from *state1* state to *state2* state]{lang="EN-US"}]{#struct_0_x1118_x1357_1382075921}

[[接收状态机由]{style="font-family:宋体"}[state1]{lang="EN-US"}]{#struct_0_x1118_x1357_x804209029}[迁移至]{style="font-family:宋体"}[state2]{lang="EN-US"}[，状态包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_RX_IDLE]{lang="EN-US"}]{#struct_0_x1118_x1357_x723842511}[：表示空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_RX_INIT]{lang="EN-US"}]{#struct_0_x1118_x1357_x833754350}[：表示初始状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_RX_WAIT]{lang="EN-US"}]{#struct_0_x1118_x1357_1269502023}[：表示等待接收状态，包括]{lang="EN-US" style="font-family:宋体"}[FRAME_RCVD]{lang="EN-US"}[、]{style="font-family:宋体"}[NB_AGED]{lang="EN-US"}[、]{style="font-family:宋体"}[ALLNB_DEL]{lang="EN-US"}[和]{style="font-family:宋体"}[CDPNB_DEL]{lang="EN-US"}[这四种]{style="font-family:宋体"}[事件]{lang="EN-US" style="font-family:宋体"}

[[Send state machine change from *state1* state to *state2* state]{lang="EN-US"}]{#struct_0_x1118_x1357_1813134429}

[[发送状态机由]{style="font-family:宋体"}*[state1]{lang="EN-US"}*]{#struct_0_x1118_x1357_1103681392}[迁移至]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[，状态包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_TX_WAIT_PORT]{lang="EN-US"}]{#struct_0_x1118_x1357_1382141457}[：表示等待端口开启]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_TX_ACTIVE]{lang="EN-US"}]{#struct_0_x1118_x1357_x398136333}[：表示激活状态处理]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_TX_INIT]{lang="EN-US"}]{#struct_0_x1118_x1357_x1119809833}[：表示端口发送初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_TX_IDLE]{lang="EN-US"}]{#struct_0_x1118_x1357_x1738722560}[：表示端口空闲]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_TX_SHUTDOWN_FRAME]{lang="EN-US"}]{#struct_0_x1118_x1357_2138301381}[：表示发送]{lang="EN-US" style="font-family:宋体"}[SHUTDOWN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP_TX_INFO_FRAME]{lang="EN-US"}]{#struct_0_x1118_x1357_1382206993}[：表示发送报文]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging lldp packet]{lang="EN-US"}]{#struct_0_x1118_x1357_x398630687}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1553914886}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x1091230097}

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_x1357_x1010284486}

[[Packet received/sent: ]{lang="EN-US"}]{#struct_0_x1118_x1357_x2031291315}

[[Interface *Interfacename*; Length is *len*]{lang="EN-US"}]{#struct_0_x1118_x1357_x2138853679}

[[收到]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1118_x1357_x157692690}[发送报文：接口名为]{style="font-family:宋体"}*[Interfacename]{lang="EN-US"}*[；长度为]{style="font-family:宋体"}*[len]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_x1357_1382272529}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x1357_x1962373508}[设备通过端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[与另一台设备相连，两台设备全局和端口均开启了]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能，在本设备上打开]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging lldp fsm]{lang="EN-US"}]{#struct_0_x1118_x1357_1370721405}

[\*Dec 6 10:54:12:978 2011 Sysname LLDP/7/Fsm:Port GigabitEthernet1/0/1 (IfIndex 51314688) nearest-bridge:]{lang="EN-US"}

[    Send state machine change from LLDP_TX_IDLE state to LLDP_TX_INFO_FRAME state]{lang="EN-US"}

[    Send state machine change from LLDP_TX_INFO_FRAME state to LLDP_TX_IDLE state]{lang="EN-US"}

[    Receive state machine change from LLDP_RX_INIT state to LLDP_RX_WAIT state]{lang="EN-US"}

[    Receive state machine change from LLDP_RX_WAIT state to EVT: FRAME_RCVD state]{lang="EN-US"}

[    Receive state machine change from RX_FRAME state to RX_WAIT_FOR_FR AME state]{lang="EN-US"}

[*[// LLDP]{lang="EN-US"}*]{#struct_0_x1118_x1357_355909643}*[最近桥代理发送状态机由]{style="font-family:宋体"}[TX_IDLE]{lang="EN-US"}[状态迁移到]{style="font-family:宋体"}[LLDP_TX_INFO_FRAME]{lang="EN-US"}[状态，再迁移到]{style="font-family:宋体"}[LLDP_TX_IDLE]{lang="EN-US"}[状态。接收状态机由]{style="font-family:宋体"}[LLDP_RX_INIT]{lang="EN-US"}[状态迁移到]{style="font-family:宋体"}[LLDP_RX_WAIT]{lang="EN-US"}[状态，再切换到]{style="font-family:宋体"}[EVT: FRAME_RCVD]{lang="EN-US"}[事件，但是状态不迁移]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1118_x1357_1903321323}[设备通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[与另一台设备相连，两台设备全局和端口均开启了]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能，在本设备上打开]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging lldp packet verbose]{lang="EN-US"}]{#struct_0_x1118_x1357_1382534673}

[\<Sysname\> \*Aug  7 09:50:43:493 2012 Sysname LLDP/7/Packet received: -MDC=1;]{lang="EN-US"}

[Interface GigabitEthernet1/0/1 nearest-bridge; Length is 375.]{lang="EN-US"}

[ Chassis type        : MAC address]{lang="EN-US"}

[ Chassis ID          : 0011-2200-0101]{lang="EN-US"}

[ Port ID type        : Interface name]{lang="EN-US"}

[ Port ID             : GigabitEthernet1/0/1]{lang="EN-US"}

[ Time to live        : 120]{lang="EN-US"}

[ Port description    : GigabitEthernet1/0/1 Interface]{lang="EN-US"}

[ System name         : Sysname]{lang="EN-US"}

[ System description  : Sysname Comware Platform Software, Software Version 7.1.034,]{lang="EN-US"}

[                       Alpha 0101]{lang="EN-US"}

[                       Sysname Simware32]{lang="EN-US"}

[                       Copyright (c) 2004-2012 Hangzhou Sysname Tech. Co., Ltd. All]{lang="EN-US"}

[                       rights reserved.]{lang="EN-US"}

[ System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge]{lang="EN-US"}

[ System capabilities enabled   : Bridge, Router, Customer Bridge]{lang="EN-US"}

[ Management address type           : All802]{lang="EN-US"}

[ Management address                : 000c-2919-c860]{lang="EN-US"}

[ Management address interface type : IfIndex]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Aug  7 09:50:43:493 2012 Sysname LLDP/7/Packet received: -MDC=1;]{lang="EN-US"}

[ Management address interface ID   : Unknown]{lang="EN-US"}

[ Management address OID            : 0]{lang="EN-US"}

[ Port VLAN ID(PVID)  : 1]{lang="EN-US"}

[ DCBX Control info:]{lang="EN-US"}

[  Oper version       : Standard]{lang="EN-US"}

[ DCBX ETS configuration info:]{lang="EN-US"}

[  CBS                : False]{lang="EN-US"}

[  Max TCs            : 8]{lang="EN-US"}

[  CoS     Local priority      Percentage        TSA]{lang="EN-US"}

[   0            7                 16            ETS]{lang="EN-US"}

[   1            6                 16            ETS]{lang="EN-US"}

[   2            5                 17            ETS]{lang="EN-US"}

[   3            4                 17            ETS]{lang="EN-US"}

[   4            3                 17            ETS]{lang="EN-US"}

[   5            2                 17            ETS]{lang="EN-US"}

[   6            1                 0             ETS]{lang="EN-US"}

[   7            0                 0             SP]{lang="EN-US"}

[ DCBX ETS recommendation info:]{lang="EN-US"}

[  CoS     Local priority      Percentage        TSA]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Aug  7 09:50:43:493 2012 Sysname LLDP/7/Packet received: -MDC=1;]{lang="EN-US"}

[   0            7                 16            ETS]{lang="EN-US"}

[   1            6                 16            ETS]{lang="EN-US"}

[   2            5                 17            ETS]{lang="EN-US"}

[   3            4                 17            ETS]{lang="EN-US"}

[   4            3                 17            ETS]{lang="EN-US"}

[   5            2                 17            ETS]{lang="EN-US"}

[   6            1                 0             ETS]{lang="EN-US"}

[   7            0                 0             SP]{lang="EN-US"}

[ DCBX PFC info:]{lang="EN-US"}

[  P0-0     P1-0     P2-0     P3-1     P4-1     P5-0     P6-0     P7-0]{lang="EN-US"}

[  Number of traffic classes supported: 8]{lang="EN-US"}

[  Value of MBC: 0]{lang="EN-US"}

[ DCBX APP info:]{lang="EN-US"}

[  Selected Field              Protocol ID Priority]{lang="EN-US"}

[  Ethertype                   0x22ca      0x3]{lang="EN-US"}

[ Auto-negotiation supported : No]{lang="EN-US"}

[ Auto-negotiation enabled   : No]{lang="EN-US"}

[ OperMau                    : Speed(0)/Duplex(Unknown)]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Aug  7 09:50:43:493 2012 Sysname LLDP/7/Packet received: -MDC=1;]{lang="EN-US"}

[ Power port class           : PSE]{lang="EN-US"}

[ PSE power supported        : No]{lang="EN-US"}

[ PSE power enabled          : No]{lang="EN-US"}

[ PSE pairs control ability  : No]{lang="EN-US"}

[ Power pairs                : Signal]{lang="EN-US"}

[ Port power classification  : Class 0]{lang="EN-US"}

[ Power type                 : Type 2 PD]{lang="EN-US"}

[ Power source               : PSE and local]{lang="EN-US"}

[ Power priority             : High]{lang="EN-US"}

[ PD requested power value   : 21.1 w]{lang="EN-US"}

[ PSE allocated power value  : 15.3 w]{lang="EN-US"}

[ Link aggregation supported : Yes]{lang="EN-US"}

[ Link aggregation enabled   : No]{lang="EN-US"}

[ Aggregation port ID        : 0]{lang="EN-US"}

[ Maximum frame size         : 9216]{lang="EN-US"}

[ Transmit Tw                : 100 us]{lang="EN-US"}

[ Receive Tw                 : 90 us]{lang="EN-US"}

[ Fallback Tw                : 90 us]{lang="EN-US"}

[ Echo Transmit Tw           : 0 us]{lang="EN-US"}

[ Echo Receive Tw            : 0 us]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Aug  7 09:50:48:076 2012 Sysname LLDP/7/Packet sent: -MDC=1;]{lang="EN-US"}

[Interface GigabitEthernet1/0/1 nearest-bridge; Length is 311.]{lang="EN-US"}

[ Chassis type        : MAC address]{lang="EN-US"}

[ Chassis ID          : 0011-2200-0001]{lang="EN-US"}

[ Port ID type        : Interface name]{lang="EN-US"}

[ Port ID             : GigabitEthernet1/0/1]{lang="EN-US"}

[ Time to live        : 120]{lang="EN-US"}

[ Port description    : GigabitEthernet1/0/1 Interface]{lang="EN-US"}

[ System name         : Sysname]{lang="EN-US"}

[ System description  : Sysname Comware Platform Software, Software Version 7.1.034,]{lang="EN-US"}

[                       Alpha 0101]{lang="EN-US"}

[                       Sysname Simware32]{lang="EN-US"}

[                       Copyright (c) 2004-2012 Hangzhou Sysname Tech. Co., Ltd. All]{lang="EN-US"}

[                       rights reserved.]{lang="EN-US"}

[ System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge]{lang="EN-US"}

[ System capabilities enabled   : Bridge, Router, Customer Bridge]{lang="EN-US"}

[ Management address type           : All802]{lang="EN-US"}

[ Management address                : 000c-2990-45fd]{lang="EN-US"}

[ Management address interface type : IfIndex]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Aug  7 09:50:48:076 2012 Sysname LLDP/7/Packet sent: -MDC=1;]{lang="EN-US"}

[ Management address interface ID   : Unknown]{lang="EN-US"}

[ Management address OID            : 0]{lang="EN-US"}

[ Port VLAN ID(PVID)  : 1]{lang="EN-US"}

[ DCBX Control info:]{lang="EN-US"}

[  Oper version       : Standard]{lang="EN-US"}

[ DCBX PFC info:]{lang="EN-US"}

[  P0-0     P1-0     P2-0     P3-1     P4-0     P5-0     P6-0     P7-0]{lang="EN-US"}

[  Number of traffic classes supported: 8]{lang="EN-US"}

[  Value of MBC: 0]{lang="EN-US"}

[ Auto-negotiation supported : No]{lang="EN-US"}

[ Auto-negotiation enabled   : No]{lang="EN-US"}

[ OperMau                    : Speed(0)/Duplex(Unknown)]{lang="EN-US"}

[ Power port class           : PSE]{lang="EN-US"}

[ PSE power supported        : No]{lang="EN-US"}

[ PSE power enabled          : No]{lang="EN-US"}

[ PSE pairs control ability  : No]{lang="EN-US"}

[ Power pairs                : Signal]{lang="EN-US"}

[ Port power classification  : Class 0]{lang="EN-US"}

[ Power type                 : Type 2 PD]{lang="EN-US"}

[ Power source               : PSE and local]{lang="EN-US"}

[ Power priority             : High]{lang="EN-US"}

[ PD requested power value   : 21.1 w]{lang="EN-US"}

[ PSE allocated power value  : 15.3 w]{lang="EN-US"}

[ Link aggregation supported : Yes]{lang="EN-US"}

[ Link aggregation enabled   : No]{lang="EN-US"}

[ Aggregation port ID        : 0]{lang="EN-US"}

[ Maximum frame size         : 9216]{lang="EN-US"}

[ Transmit Tw                : 100 us]{lang="EN-US"}

[ Receive Tw                 : 90 us]{lang="EN-US"}

[ Fallback Tw                : 90 us]{lang="EN-US"}

[ Echo Transmit Tw           : 0 us]{lang="EN-US"}

[ Echo Receive Tw            : 0 us]{lang="EN-US"}

[*[// LLDP]{lang="EN-US"}*]{#struct_0_x1118_x1357_x438286026}*[发送报文和接收报文的详细信息]{style="font-family:宋体"}*
