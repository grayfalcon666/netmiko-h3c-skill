::: {#1620260494 .myid}
[]{#_Toc404789582}[]{#struct_0_12031_59956_701677540}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**PIM \-- PIM调试命令 \-- debugging pim**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_12031_59956_1909278891}

[**[debugging pim]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **df** \| **error** \| { **event** \| **register** \| **routing-table** } \[ *advanced-acl-number* \] \| { **assert** \| **join-prune** \| **rp** \| **state-refresh** } \[ *advanced-acl-number* \] \[ **receive** \| **send** \] \| **neighbor** \[ *basic-acl-number* \] \[ **receive** \| **send** \] }]{lang="EN-US"}]{#struct_0_12031_59956_x483997445}

[**[undo debugging pim]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **df** \| **error** \| **event** \| **register** \| **routing-table** \| { **assert** \| **join-prune** \| **neighbor** \| **rp** \| **state-refresh** } \[ **receive** \| **send** \] }]{lang="EN-US"}]{#struct_0_12031_59956_x1177509092}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12031_59956_1157247670}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12031_59956_x1506544361}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12031_59956_2060458376}

[[network-admin]{lang="EN-US"}]{#struct_0_12031_59956_x314156682}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12031_59956_x1806124216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12031_59956_x36964677}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12031_59956_1213390121}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_12031_59956_x690354870}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[df]{lang="EN-US"}**]{#struct_0_12031_59956_x607586232}[：表示双向]{style="font-family:宋体"}[PIM DF]{lang="EN-US"}[选举调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_12031_59956_1370675833}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_12031_59956_1919390355}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[register]{lang="EN-US"}**]{#struct_0_12031_59956_1292830021}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[注册报文调试信息开关。]{style="font-family:宋体"}

[**[routing-table]{lang="EN-US"}**]{#struct_0_12031_59956_x313960074}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[组播路由表状态改变调试信息开关。]{style="font-family:宋体"}

[*[advanced-acl-number]{lang="EN-US"}*]{#struct_0_12031_59956_1462358781}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[assert]{lang="EN-US"}**]{#struct_0_12031_59956_196652815}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[断言报文调试信息开关。]{style="font-family:宋体"}

[**[join-prune]{lang="EN-US"}**]{#struct_0_12031_59956_1686482510}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文调试信息开关。]{style="font-family:宋体"}

[**[rp]{lang="EN-US"}**]{#struct_0_12031_59956_5868984}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[RP]{lang="EN-US"}[相关报文的调试信息开关。]{style="font-family:宋体"}

[**[state-refresh]{lang="EN-US"}**]{#struct_0_12031_59956_x1110829584}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[状态刷新报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_12031_59956_x1052523549}[：表示接收的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_12031_59956_1867258884}[：表示发送的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[neighbor]{lang="EN-US"}**]{#struct_0_12031_59956_1861463854}[：表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[与邻居信息相关的调试信息开关。]{style="font-family:宋体"}

[*[basic-acl-number]{lang="EN-US"}*]{#struct_0_12031_59956_x314025610}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_12031_59956_916270985}

[**[debugging pim]{lang="EN-US"}**]{#struct_0_12031_59956_x494255813}[命令用来打开]{style="font-family:宋体"}[PIM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging pim]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[PIM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_12031_59956_1636991827}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging pim assert]{lang="EN-US"}]{#struct_0_12031_59956_870489946}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_588262309}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x1081059341}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_x2005507759}

[[Assert FSM]{lang="EN-US"}]{#struct_0_12031_59956_x313829002}

[[断言状态机]{style="font-family:宋体"}]{#struct_0_12031_59956_x919338146}

[*[state1]{lang="EN-US"}*[-\>*state2*]{lang="EN-US"}]{#struct_0_12031_59956_1253668632}

[[断言状态机从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*]{#struct_0_12031_59956_1837025700}[转换到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[[loser/winner/noinfo]{lang="EN-US"}]{#struct_0_12031_59956_x1690513900}

[[断言状态机处于]{style="font-family:宋体"}[Loser/Winner/Noinfo]{lang="EN-US"}]{#struct_0_12031_59956_x896862077}[状态]{style="font-family:宋体"}

[[timeout of the winner]{lang="EN-US"}]{#struct_0_12031_59956_x857326224}

[[Winner]{lang="EN-US"}]{#struct_0_12031_59956_x313894538}[老化]{style="font-family:宋体"}

[[Rbit]{lang="EN-US"}]{#struct_0_12031_59956_x2107660914}

[[RPT]{lang="EN-US"}]{#struct_0_12031_59956_1806010812}[标识位]{style="font-family:宋体"}

[[Preference]{lang="EN-US"}]{#struct_0_12031_59956_x769514519}

[[优先级字段]{style="font-family:宋体"}]{#struct_0_12031_59956_x628624497}

[[Metric]{lang="EN-US"}]{#struct_0_12031_59956_1353985846}

[[Metric]{lang="EN-US"}]{#struct_0_12031_59956_x314353293}[字段]{style="font-family:宋体"}

[[assert timer expired]{lang="EN-US"}]{#struct_0_12031_59956_964588660}

[[断言定时器超时]{style="font-family:宋体"}]{#struct_0_12031_59956_1714398915}

[[insufficient memory]{lang="EN-US"}]{#struct_0_12031_59956_1832757790}

[[内存不足]{style="font-family:宋体"}]{#struct_0_12031_59956_x698239262}

[[inferior assert]{lang="EN-US"}]{#struct_0_12031_59956_x314418829}

[[度量值比自身差的断言报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x237471881}

[[acceptable assert]{lang="EN-US"}]{#struct_0_12031_59956_714960384}

[[来自断言获胜路由器的度量值比自身好的断言报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x337136501}

[[preferred assert]{lang="EN-US"}]{#struct_0_12031_59956_1729099994}

[[比当前断言获胜路由器具备更优开销的断言报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x314222221}

[[NIIF]{lang="EN-US"}]{#struct_0_12031_59956_x607852349}

[[入接口为空]{style="font-family:宋体"}]{#struct_0_12031_59956_1031014571}

[[OIF]{lang="EN-US"}]{#struct_0_12031_59956_124273332}

[[出接口]{style="font-family:宋体"}]{#struct_0_12031_59956_x989606180}

[[(\*,G) Entry is not exist]{lang="EN-US"}]{#struct_0_12031_59956_x314287757}

[[（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_12031_59956_2079606417}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项不存在]{style="font-family:宋体"}

[[self metric]{lang="EN-US"}]{#struct_0_12031_59956_525788267}

[[自身到源的路由度量值]{style="font-family:宋体"}]{#struct_0_12031_59956_x691787412}

[[unknown neighbor]{lang="EN-US"}]{#struct_0_12031_59956_x314091149}

[[未知邻居]{style="font-family:宋体"}]{#struct_0_12031_59956_529161498}

[[wrong packet length]{lang="EN-US"}]{#struct_0_12031_59956_x1884349741}

[[报文长度非法]{style="font-family:宋体"}]{#struct_0_12031_59956_x344246991}

[[bad group address]{lang="EN-US"}]{#struct_0_12031_59956_697521409}

[[错误的组地址]{style="font-family:宋体"}]{#struct_0_12031_59956_x314156685}

[[invalid group address]{lang="EN-US"}]{#struct_0_12031_59956_x1805796536}

[[非法的组地址]{style="font-family:宋体"}]{#struct_0_12031_59956_2021065442}

[[group boundary]{lang="EN-US"}]{#struct_0_12031_59956_x418002542}

[[组边界]{style="font-family:宋体"}]{#struct_0_12031_59956_x313960077}

[[bad source address]{lang="EN-US"}]{#struct_0_12031_59956_1462293245}

[[错误的源地址]{style="font-family:宋体"}]{#struct_0_12031_59956_x1450069533}

[[invalid source address]{lang="EN-US"}]{#struct_0_12031_59956_x314025613}

[[非法的源地址]{style="font-family:宋体"}]{#struct_0_12031_59956_916205449}

[[SSM group]{lang="EN-US"}]{#struct_0_12031_59956_212550599}

[[SSM]{lang="EN-US"}]{#struct_0_12031_59956_1109117352}[组]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging pim df]{lang="EN-US"}]{#struct_0_12031_59956_x935624287}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_616806506}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x313829005}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_x919403682}

[[DF election/DF-Election]{lang="EN-US"}]{#struct_0_12031_59956_x1044548396}

[[DF]{lang="EN-US"}]{#struct_0_12031_59956_x202016222}[选举]{style="font-family:宋体"}

[[DFT]{lang="EN-US"}]{#struct_0_12031_59956_1122556342}

[[DF]{lang="EN-US"}]{#struct_0_12031_59956_773540355}[选举定时器]{style="font-family:宋体"}

[[WinTimer]{lang="EN-US"}]{#struct_0_12031_59956_x313894541}

[[Winner]{lang="EN-US"}]{#struct_0_12031_59956_x2107202167}[定时器]{style="font-family:宋体"}

[[expire time]{lang="EN-US"}]{#struct_0_12031_59956_x720150453}

[[定时器的超时时间]{style="font-family:宋体"}]{#struct_0_12031_59956_2051408079}

[[MC]{lang="EN-US"}]{#struct_0_12031_59956_1333509611}

[[Offer]{lang="EN-US"}]{#struct_0_12031_59956_x814791498}[或]{style="font-family:宋体"}[Winner]{lang="EN-US"}[报文的发送个数]{style="font-family:宋体"}

[[robustness]{lang="EN-US"}]{#struct_0_12031_59956_x151560658}

[[DF]{lang="EN-US"}]{#struct_0_12031_59956_x314353292}[选举健壮系数，缺省值为]{style="font-family:宋体"}[3]{lang="EN-US"}

[[RPL]{lang="EN-US"}]{#struct_0_12031_59956_964654196}

[[RPL]{lang="EN-US"}]{#struct_0_12031_59956_x1486236173}[链路]{style="font-family:宋体"}

[[Offer]{lang="EN-US"}]{#struct_0_12031_59956_563034326}

[[DF]{lang="EN-US"}]{#struct_0_12031_59956_x1894942514}[选举的初始状态]{style="font-family:宋体"}

[[Lose]{lang="EN-US"}]{#struct_0_12031_59956_x314418828}

[[DF]{lang="EN-US"}]{#struct_0_12031_59956_x237406345}[选举失败]{style="font-family:宋体"}

[[Win]{lang="EN-US"}]{#struct_0_12031_59956_x1962804895}

[[DF]{lang="EN-US"}]{#struct_0_12031_59956_227365568}[选举胜出]{style="font-family:宋体"}

[[Backoff]{lang="EN-US"}]{#struct_0_12031_59956_790005393}

[[处于]{style="font-family:宋体"}[Win]{lang="EN-US"}]{#struct_0_12031_59956_2107938246}[状态的]{style="font-family:宋体"}[DF]{lang="EN-US"}[收到更优的]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[DF FSM]{lang="EN-US"}]{#struct_0_12031_59956_x314222220}

[[DF]{lang="EN-US"}]{#struct_0_12031_59956_x607917885}[选举状态]{style="font-family:宋体"}

[[Receive better Backoff/Pass/Offer/Win]{lang="EN-US"}]{#struct_0_12031_59956_1737510815}

[[收到更优的]{style="font-family:宋体"}[Backoff/Pass/Offer/Win]{lang="EN-US"}]{#struct_0_12031_59956_x1346235274}[报文]{style="font-family:宋体"}

[[Receive worse Backoff/Pass/Offer/Win]{lang="EN-US"}]{#struct_0_12031_59956_x458967221}

[[收到更差的]{style="font-family:宋体"}[Backoff/Pass/Offer/Win]{lang="EN-US"}]{#struct_0_12031_59956_x314287756}[报文]{style="font-family:宋体"}

[[Receive Backoff/Pass for us]{lang="EN-US"}]{#struct_0_12031_59956_2079540881}

[[收到通告自己的]{style="font-family:宋体"}[Backoff/Pass]{lang="EN-US"}]{#struct_0_12031_59956_x677369695}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging pim error]{lang="EN-US"}]{#struct_0_12031_59956_1146677441}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_614268738}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x522126199}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_x314091148}

[[IPC data]{lang="EN-US"}]{#struct_0_12031_59956_529227034}

[[用于进程间通信的数据]{style="font-family:宋体"}]{#struct_0_12031_59956_1858488295}

[[Mfib]{lang="EN-US"}]{#struct_0_12031_59956_2082130284}

[[组播转发信息库]{style="font-family:宋体"}]{#struct_0_12031_59956_x1642173800}

[[Reference]{lang="EN-US"}]{#struct_0_12031_59956_x1503423160}

[[引用计数]{style="font-family:宋体"}]{#struct_0_12031_59956_x1346325436}

[[config info]{lang="EN-US"}]{#struct_0_12031_59956_x314156684}

[[配置信息]{style="font-family:宋体"}]{#struct_0_12031_59956_x1805731000}

[[insufficient memory]{lang="EN-US"}]{#struct_0_12031_59956_x569512351}

[[内存不足]{style="font-family:宋体"}]{#struct_0_12031_59956_x502199715}

[[secondary address node]{lang="EN-US"}]{#struct_0_12031_59956_x48362928}

[[二级地址节点]{style="font-family:宋体"}]{#struct_0_12031_59956_462951671}

[[unsupported PIM packet type]{lang="EN-US"}]{#struct_0_12031_59956_x313960076}

[[不支持的]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_12031_59956_1462227709}[数据包类型]{style="font-family:宋体"}

[[checksum error]{lang="EN-US"}]{#struct_0_12031_59956_x1830321077}

[[检验和字段错误]{style="font-family:宋体"}]{#struct_0_12031_59956_1481146620}

[[invalid pim interface]{lang="EN-US"}]{#struct_0_12031_59956_x998547321}

[[非法的]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_12031_59956_1088592543}[接口]{style="font-family:宋体"}

[[unknown neighbor]{lang="EN-US"}]{#struct_0_12031_59956_x314025612}

[[未知邻居]{style="font-family:宋体"}]{#struct_0_12031_59956_916139913}

[[CRPT]{lang="EN-US"}]{#struct_0_12031_59956_x806796867}

[[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_410376889}[发送定时器]{style="font-family:宋体"}

[[Blank Group]{lang="EN-US"}]{#struct_0_12031_59956_x884034533}

[[不存在]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_x313829004}[的组]{style="font-family:宋体"}

[[Fail to get ifindex]{lang="EN-US"}]{#struct_0_12031_59956_x919469218}

[[获取接口索引失败]{style="font-family:宋体"}]{#struct_0_12031_59956_1235485401}

[[best route]{lang="EN-US"}]{#struct_0_12031_59956_1640811920}

[[最优路由]{style="font-family:宋体"}]{#struct_0_12031_59956_1997846378}

[[Assert_Timer]{lang="EN-US"}]{#struct_0_12031_59956_x313894540}

[[断言定时器]{style="font-family:宋体"}]{#struct_0_12031_59956_x2107136631}

[[invalid event]{lang="EN-US"}]{#struct_0_12031_59956_1112818051}

[[非法事件]{style="font-family:宋体"}]{#struct_0_12031_59956_1166321912}

[[MRIB]{lang="EN-US"}]{#struct_0_12031_59956_x314353295}

[[组播路由信息库]{style="font-family:宋体"}]{#struct_0_12031_59956_964981876}

[[valid RPF interface]{lang="EN-US"}]{#struct_0_12031_59956_x1718614205}

[[合法的]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_12031_59956_741101676}[邻居]{style="font-family:宋体"}

[[Ifstate]{lang="EN-US"}]{#struct_0_12031_59956_x314418831}

[[接口状态]{style="font-family:宋体"}]{#struct_0_12031_59956_x237996170}

[[negotiation]{lang="EN-US"}]{#struct_0_12031_59956_x1599997507}

[[协商]{style="font-family:宋体"}]{#struct_0_12031_59956_x1074473152}

[[wrong flag]{lang="EN-US"}]{#struct_0_12031_59956_x314222223}

[[错误标识]{style="font-family:宋体"}]{#struct_0_12031_59956_x607983421}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging pim event]{lang="EN-US"}]{#struct_0_12031_59956_1391426861}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_608466972}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x921550499}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_x527892158}

[[PIM mrt]{lang="EN-US"}]{#struct_0_12031_59956_x933631218}

[[PIM]{lang="EN-US"}]{#struct_0_12031_59956_x1290703303}[组播路由表]{style="font-family:宋体"}

[[No-Cache msg]{lang="EN-US"}]{#struct_0_12031_59956_x314287759}

[[未知组播消息]{style="font-family:宋体"}]{#struct_0_12031_59956_2079737489}

[[Wrong-If msg]{lang="EN-US"}]{#struct_0_12031_59956_2084990822}

[[从非入接口收到组播流消息]{style="font-family:宋体"}]{#struct_0_12031_59956_995781030}

[[SPT msg]{lang="EN-US"}]{#struct_0_12031_59956_x653114463}

[[SPT]{lang="EN-US"}]{#struct_0_12031_59956_x745594985}[切换消息]{style="font-family:宋体"}

[[Active msg]{lang="EN-US"}]{#struct_0_12031_59956_x314091151}

[[MFIB]{lang="EN-US"}]{#struct_0_12031_59956_529685785}[上报新的组播流消息]{style="font-family:宋体"}

[[Inactive msg]{lang="EN-US"}]{#struct_0_12031_59956_868268759}

[[MFIB]{lang="EN-US"}]{#struct_0_12031_59956_x1296372064}[上报流老化消息]{style="font-family:宋体"}

[[Reg-Timeout msg]{lang="EN-US"}]{#struct_0_12031_59956_x1607337500}

[[注册定时器超时消息]{style="font-family:宋体"}]{#struct_0_12031_59956_532416902}

[[reset forwarding-table msg]{lang="EN-US"}]{#struct_0_12031_59956_x314156687}

[[MIFB]{lang="EN-US"}]{#struct_0_12031_59956_x1805927608}[转发表重置消息]{style="font-family:宋体"}

[[Received BFD event: *type*, *source* -\> *destination*, *interface*]{lang="EN-US"}]{#struct_0_12031_59956_x1439340464}

[[收到]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_12031_59956_1046792712}[会话消息：类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging pim join-prune]{lang="EN-US"}]{#struct_0_12031_59956_1996905024}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_610804813}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x296241835}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_x313960079}

[[JP]{lang="EN-US"}]{#struct_0_12031_59956_1461637885}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12031_59956_x507477041}[剪枝报文]{style="font-family:宋体"}

[[Upstream]{lang="EN-US"}]{#struct_0_12031_59956_149901110}

[[报文中的上游邻居信息]{style="font-family:宋体"}]{#struct_0_12031_59956_144172050}

[[Groups]{lang="EN-US"}]{#struct_0_12031_59956_572605301}

[[报文中的组数目信息]{style="font-family:宋体"}]{#struct_0_12031_59956_x1079672659}

[[Holdtime]{lang="EN-US"}]{#struct_0_12031_59956_x314025615}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12031_59956_916074377}[剪枝报文的保持时间字段]{style="font-family:宋体"}

[[Group: *addr*/*mask* \-\-- *m* joins *n* prunes]{lang="EN-US"}]{#struct_0_12031_59956_x825634997}

[[报文中的组信息：组地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12031_59956_x909168843}[掩码长度------]{style="font-family:宋体"}*[m]{lang="EN-US"}*[个加入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[个剪枝]{style="font-family:宋体"}

[[Join: *addr/mask* flag]{lang="EN-US"}]{#struct_0_12031_59956_x487877197}

[[加入：源地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12031_59956_571188038}[掩码，标志位]{style="font-family:宋体"}

[[RP change]{lang="EN-US"}]{#struct_0_12031_59956_x313829007}

[[RP]{lang="EN-US"}]{#struct_0_12031_59956_x919534754}[发生变化]{style="font-family:宋体"}

[[the packet is received from interface *A*, but destination is *B*. Ignored.]{lang="EN-US"}]{#struct_0_12031_59956_x1454136081}

[[从接口]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_12031_59956_942267076}[上收到一个发给]{style="font-family:宋体"}[B]{lang="EN-US"}[的报文，将其丢弃]{style="font-family:宋体"}

[[Message Truncated]{lang="EN-US"}]{#struct_0_12031_59956_1114198336}

[[报文长度非法]{style="font-family:宋体"}]{#struct_0_12031_59956_x313894543}

[[multicast boundary]{lang="EN-US"}]{#struct_0_12031_59956_x2107333239}

[[组播边界]{style="font-family:宋体"}]{#struct_0_12031_59956_804185695}

[[Join/Prune received from non-local neighbor]{lang="EN-US"}]{#struct_0_12031_59956_897819338}

[[从不属于本接口网段的上游邻居收到一个加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12031_59956_2007155538}[剪枝报文]{style="font-family:宋体"}

[*[Address ]{lang="EN-US"}*[is not a valid multicast address]{lang="EN-US"}]{#struct_0_12031_59956_x314353294}

[*[Address]{lang="EN-US"}*]{#struct_0_12031_59956_965047412}[是一个非法组播地址]{style="font-family:宋体"}

[[Message from unknown neighbor]{lang="EN-US"}]{#struct_0_12031_59956_x209293366}

[[从未知邻居收到报文]{style="font-family:宋体"}]{#struct_0_12031_59956_1087798303}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging pim neighbor]{lang="EN-US"}]{#struct_0_12031_59956_499765817}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_607475458}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x1811767401}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_x314418830}

[[hello packet]{lang="EN-US"}]{#struct_0_12031_59956_x237930634}

[[PIM Hello]{lang="EN-US"}]{#struct_0_12031_59956_775807735}[报文]{style="font-family:宋体"}

[[invalid secondary address]{lang="EN-US"}]{#struct_0_12031_59956_973003602}

[[非法二级地址]{style="font-family:宋体"}]{#struct_0_12031_59956_x1334228626}

[[Holdtime]{lang="EN-US"}]{#struct_0_12031_59956_1278586646}

[[PIM Hello]{lang="EN-US"}]{#struct_0_12031_59956_x800264190}[报文的保持时间字段]{style="font-family:宋体"}

[[Tbit]{lang="EN-US"}]{#struct_0_12031_59956_x314222222}

[[T]{lang="EN-US"}]{#struct_0_12031_59956_x608048957}[位选项]{style="font-family:宋体"}

[[Lan delay]{lang="EN-US"}]{#struct_0_12031_59956_365991250}

[[剪枝延迟时间选项]{style="font-family:宋体"}]{#struct_0_12031_59956_1978937937}

[[Override interval]{lang="EN-US"}]{#struct_0_12031_59956_1937603302}

[[剪枝否决时间选项]{style="font-family:宋体"}]{#struct_0_12031_59956_x1937995404}

[[DR priority]{lang="EN-US"}]{#struct_0_12031_59956_x314287758}

[[DR]{lang="EN-US"}]{#struct_0_12031_59956_2079671953}[优先级选项]{style="font-family:宋体"}

[[Genid]{lang="EN-US"}]{#struct_0_12031_59956_x1456294862}

[[Generation ID]{lang="EN-US"}]{#struct_0_12031_59956_x49339679}[选项]{style="font-family:宋体"}

[[Discarding Hello packet from *address* without Generation ID.]{lang="EN-US"}]{#struct_0_12031_59956_x1027731709}

[[丢弃没有]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}]{#struct_0_12031_59956_x314091150}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[the neighbor information being refreshed]{lang="EN-US"}]{#struct_0_12031_59956_529751321}

[[更新邻居信息]{style="font-family:宋体"}]{#struct_0_12031_59956_482339390}

[[Too many neighbors, ignoring new neighbor *address*.]{lang="EN-US"}]{#struct_0_12031_59956_765754511}

[[邻居过多，忽略新的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_12031_59956_x1739668481}[报文]{style="font-family:宋体"}

[[secondary address list]{lang="EN-US"}]{#struct_0_12031_59956_x314156686}

[[二级地址列表]{style="font-family:宋体"}]{#struct_0_12031_59956_x1805862072}

[[bad secondary address]{lang="EN-US"}]{#struct_0_12031_59956_1089291228}

[[错误的二级地址]{style="font-family:宋体"}]{#struct_0_12031_59956_x1303319475}

[[Received Hello packet from invalid source: *address*]{lang="EN-US"}]{#struct_0_12031_59956_2140048709}

[[收到来自非法源地址的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_12031_59956_x313960078}[报文]{style="font-family:宋体"}

[[Received Hello packet on *interface* from non-local source: *address*]{lang="EN-US"}]{#struct_0_12031_59956_1461572349}

[[收到非本地主机的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_12031_59956_x1685570469}[报文]{style="font-family:宋体"}

[[Received Hello packet with short data from *address*]{lang="EN-US"}]{#struct_0_12031_59956_x52318390}

[[收到数据不完整的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_12031_59956_x314025614}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with wrong Holdtime length:]{lang="EN-US"}]{#struct_0_12031_59956_916008841}

[[收到]{style="font-family:宋体"}[Holdtime]{lang="EN-US"}]{#struct_0_12031_59956_1551420539}[选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with invalid LAN Prune Delay length:]{lang="EN-US"}]{#struct_0_12031_59956_1678124175}

[[收到]{style="font-family:宋体"}[LAN Prune Delay]{lang="EN-US"}]{#struct_0_12031_59956_x313829006}[选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with invalid DR Priority length:]{lang="EN-US"}]{#struct_0_12031_59956_x919600290}

[[收到]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_12031_59956_x683027738}[优先级选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with invalid Generation ID length:]{lang="EN-US"}]{#struct_0_12031_59956_277586393}

[[收到]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}]{#struct_0_12031_59956_x313894542}[选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with invalid State Refresh length:]{lang="EN-US"}]{#struct_0_12031_59956_x2107267703}

[[收到状态更新选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_12031_59956_x244706025}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with Bidir option]{lang="EN-US"}]{#struct_0_12031_59956_89478609}

[[收到带有双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_12031_59956_x725797654}[选项的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with unsupported option:]{lang="EN-US"}]{#struct_0_12031_59956_1607961010}

[[收到带有错误选项的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_12031_59956_x939419812}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with wrong data length]{lang="EN-US"}]{#struct_0_12031_59956_2106135247}

[[收到长度错误的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_12031_59956_1607895474}[报文]{style="font-family:宋体"}

[[Notify create/delete/disable BFD session *source* -\> *destination*, *interface*]{lang="EN-US"}]{#struct_0_12031_59956_591030767}

[[通知创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_12031_59956_x1665767194}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging pim register]{lang="EN-US"}]{#struct_0_12031_59956_1418918816}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_636019655}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x536565545}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_x1154114704}

[[probe]{lang="EN-US"}]{#struct_0_12031_59956_1608092082}

[[探测报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x752403797}

[[no route to RP]{lang="EN-US"}]{#struct_0_12031_59956_x2111793984}

[[没有通往]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_12031_59956_x735104299}[的路由]{style="font-family:宋体"}

[[not knowing RP]{lang="EN-US"}]{#struct_0_12031_59956_x784920678}

[[未知]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_12031_59956_x2010102453}

[[register packet]{lang="EN-US"}]{#struct_0_12031_59956_1608026546}

[[注册报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x1126494941}

[[Bbit]{lang="EN-US"}]{#struct_0_12031_59956_x393637511}

[[边界位]{style="font-family:宋体"}]{#struct_0_12031_59956_861182721}

[[Nbit]{lang="EN-US"}]{#struct_0_12031_59956_x68250545}

[[空位]{style="font-family:宋体"}]{#struct_0_12031_59956_1840024532}

[[RST]{lang="EN-US"}]{#struct_0_12031_59956_x1370459797}

[[注册停止定时器]{style="font-family:宋体"}]{#struct_0_12031_59956_1608223154}

[[register state]{lang="EN-US"}]{#struct_0_12031_59956_41594773}

[[注册状态机状态]{style="font-family:宋体"}]{#struct_0_12031_59956_x1908349832}

[[reg tunnel]{lang="EN-US"}]{#struct_0_12031_59956_147442104}

[[注册通道]{style="font-family:宋体"}]{#struct_0_12031_59956_1720238052}

[[reg-stop packet]{lang="EN-US"}]{#struct_0_12031_59956_1608157618}

[[注册停止报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x1116438118}

[[invalid RPF interface]{lang="EN-US"}]{#struct_0_12031_59956_199645974}

[[非法的]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_12031_59956_499662514}[接口]{style="font-family:宋体"}

[[RP changed]{lang="EN-US"}]{#struct_0_12031_59956_2049614397}

[[RP]{lang="EN-US"}]{#struct_0_12031_59956_1086285092}[发生变化]{style="font-family:宋体"}

[[Null-Register]{lang="EN-US"}]{#struct_0_12031_59956_1608354226}

[[空注册报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x1917192586}

[[register oif]{lang="EN-US"}]{#struct_0_12031_59956_x549597651}

[[注册出接口]{style="font-family:宋体"}]{#struct_0_12031_59956_x583415254}

[[the group address *address* is not valid.]{lang="EN-US"}]{#struct_0_12031_59956_x1359115275}

[[组地址非法]{style="font-family:宋体"}]{#struct_0_12031_59956_1608288690}

[[Received register-stop message with bad group masks from *address* for *address/mask*.]{lang="EN-US"}]{#struct_0_12031_59956_x386610948}

[[收到组掩码错误的注册终止报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x1031912144}

[[the source address is not valid]{lang="EN-US"}]{#struct_0_12031_59956_595720800}

[[源地址非法]{style="font-family:宋体"}]{#struct_0_12031_59956_1608485298}

[[RP for group *address* is unknown.]{lang="EN-US"}]{#struct_0_12031_59956_780823157}

[[相关组的]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_12031_59956_1360297666}[未知]{style="font-family:宋体"}

[[RP dispute for *address*]{lang="EN-US"}]{#struct_0_12031_59956_x991591347}

[[RP]{lang="EN-US"}]{#struct_0_12031_59956_1608419762}[映射错误]{style="font-family:宋体"}

[[no matching entry for *(S,G)*]{lang="EN-US"}]{#struct_0_12031_59956_407387350}

[[没有相关的（]{style="font-family:宋体"}*[S]{lang="EN-US"}*]{#struct_0_12031_59956_2104267575}*[，]{style="font-family:宋体"}[G]{lang="EN-US"}*[）表项]{style="font-family:宋体"}

[[Anycast-RP timer]{lang="EN-US"}]{#struct_0_12031_59956_x118061909}

[[Anycast-RP]{lang="EN-US"}]{#struct_0_12031_59956_x118127445}[定时器]{style="font-family:宋体"}

[[the source address belongs to the Anycast-RP set]{lang="EN-US"}]{#struct_0_12031_59956_x376486223}

[[源地址在]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}]{#struct_0_12031_59956_x118192981}[集中]{style="font-family:宋体"}

[[Notify MFIB not to suppress register packets]{lang="EN-US"}]{#struct_0_12031_59956_336652508}

[[通知]{style="font-family:宋体"}[MFIB]{lang="EN-US"}]{#struct_0_12031_59956_x117209941}[不要抑制注册报文]{style="font-family:宋体"}

[[no active local RP exists]{lang="EN-US"}]{#struct_0_12031_59956_x1045822924}

[[没有激活的本地]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_12031_59956_x117275477}[存在]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging pim rp]{lang="EN-US"}]{#struct_0_12031_59956_x1818594061}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_632004899}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x521194563}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_x1694486938}

[[auto-RP announce packet]{lang="EN-US"}]{#struct_0_12031_59956_1607961011}

[[自动]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_12031_59956_x939485348}[宣告报文]{style="font-family:宋体"}

[[Truncated bootstrap message]{lang="EN-US"}]{#struct_0_12031_59956_248224656}

[[长度非法的自举报文]{style="font-family:宋体"}]{#struct_0_12031_59956_438391775}

[[BSM packet]{lang="EN-US"}]{#struct_0_12031_59956_343129842}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_547991857}[自举报文]{style="font-family:宋体"}

[[Nbit]{lang="EN-US"}]{#struct_0_12031_59956_x1649050081}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1607895475}[报文段禁止转发标志位]{style="font-family:宋体"}

[[Fragment tag]{lang="EN-US"}]{#struct_0_12031_59956_591096303}

[[用于]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1446286664}[报文的分片]{style="font-family:宋体"}

[[Hash mask len]{lang="EN-US"}]{#struct_0_12031_59956_1337493624}

[[哈希掩码长度]{style="font-family:宋体"}]{#struct_0_12031_59956_x1023899340}

[[BSR Priority]{lang="EN-US"}]{#struct_0_12031_59956_x1929573176}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1608092083}[优先级]{style="font-family:宋体"}

[[BSR address]{lang="EN-US"}]{#struct_0_12031_59956_x752338261}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_551458585}[地址]{style="font-family:宋体"}

[[Group]{lang="EN-US"}]{#struct_0_12031_59956_x1154264487}

[[组地址]{style="font-family:宋体"}]{#struct_0_12031_59956_x1324518710}

[[Zbit]{lang="EN-US"}]{#struct_0_12031_59956_x1027812178}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1608026547}[报文段自治域标志位]{style="font-family:宋体"}

[[RP Count]{lang="EN-US"}]{#struct_0_12031_59956_x1126560477}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1571678119}[报文中表示服务这个组播组范围的]{style="font-family:宋体"}[RP]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[Frag RP Count]{lang="EN-US"}]{#struct_0_12031_59956_1806405613}

[[表示]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1608223155}[分片报文中服务这个组播组范围的]{style="font-family:宋体"}[RP]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[RP: *address* \-\-- Holdtime *holdtime*, Priority *priority*]{lang="EN-US"}]{#struct_0_12031_59956_41529237}

[[RP]{lang="EN-US"}]{#struct_0_12031_59956_x1882409257}[：地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[------保持时间为]{style="font-family:宋体"}*[holdtime]{lang="EN-US"}*[，优先级为]{style="font-family:宋体"}*[priority]{lang="EN-US"}*

[[Truncated crp packet]{lang="EN-US"}]{#struct_0_12031_59956_475446982}

[[长度非法的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_468271312}[宣告报文]{style="font-family:宋体"}

[[C-RP-Adv]{lang="EN-US"}]{#struct_0_12031_59956_1608157619}

[[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_x1116372582}[宣告报文]{style="font-family:宋体"}

[[Prefix count]{lang="EN-US"}]{#struct_0_12031_59956_1078062328}

[[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_124657215}[宣告报文中包含的组地址个数]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_12031_59956_1608354227}

[[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_x1917127050}[宣告报文的优先级字段]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_12031_59956_x1149889021}

[[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_x1581884410}[宣告报文的保持时间字段]{style="font-family:宋体"}

[[RP address]{lang="EN-US"}]{#struct_0_12031_59956_1608288691}

[[RP]{lang="EN-US"}]{#struct_0_12031_59956_x386676484}[地址]{style="font-family:宋体"}

[[Failed to build BSM pkt because MTU is too small]{lang="EN-US"}]{#struct_0_12031_59956_90320490}

[[构造]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_x2031405437}[自举报文失败，原因是]{style="font-family:宋体"}[MTU]{lang="EN-US"}[太小了]{style="font-family:宋体"}

[[BSR boundary]{lang="EN-US"}]{#struct_0_12031_59956_28327995}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1608485299}[边界]{style="font-family:宋体"}

[[multicast boundary]{lang="EN-US"}]{#struct_0_12031_59956_780757621}

[[组播边界]{style="font-family:宋体"}]{#struct_0_12031_59956_x1984826632}

[[EBSR]{lang="EN-US"}]{#struct_0_12031_59956_x696778980}

[[最优]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1608419763}

[[EBSR updates RPs by self in scope]{lang="EN-US"}]{#struct_0_12031_59956_407452886}

[[最优]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_x1445954731}[在域内自动更新了]{style="font-family:宋体"}[RP]{lang="EN-US"}

[[Protocol conflict while updating group *address* for crp *address*.]{lang="EN-US"}]{#struct_0_12031_59956_x192856243}

[[更新]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_1607961008}[地址时使用组地址，与协议冲突]{style="font-family:宋体"}

[[Invalid group address]{lang="EN-US"}]{#struct_0_12031_59956_x939944099}

[[非法组地址]{style="font-family:宋体"}]{#struct_0_12031_59956_614666389}

[[multicast boundary]{lang="EN-US"}]{#struct_0_12031_59956_1607895472}

[[组播边界]{style="font-family:宋体"}]{#struct_0_12031_59956_591161839}

[[Received an invalid length C-RP-Adv packet]{lang="EN-US"}]{#struct_0_12031_59956_229087670}

[[收到一个长度非法的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_1224160346}[的宣告报文]{style="font-family:宋体"}

[[The length of C-RP-Adv packet is wrong]{lang="EN-US"}]{#struct_0_12031_59956_1608092080}

[[C-RP]{lang="EN-US"}]{#struct_0_12031_59956_x752272725}[宣告报文长度出错]{style="font-family:宋体"}

[[Received BSR packet with bad bsr address]{lang="EN-US"}]{#struct_0_12031_59956_599591086}

[[收到]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1608026544}[地址非法的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received BSR packet with non-unicast bsr address *address*]{lang="EN-US"}]{#struct_0_12031_59956_x1126363869}

[[收到]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1633650481}[地址不是单播地址的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received a BSM with bad first group address from BSR *address*]{lang="EN-US"}]{#struct_0_12031_59956_1608223152}

[[收到的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_41725845}[自举报文中第一个组地址错误]{style="font-family:宋体"}

[[Unable to pass multicast boundary check for *address/mask*]{lang="EN-US"}]{#struct_0_12031_59956_x625412330}

[[由于组地址和掩码问题无法通过组播边界检查]{style="font-family:宋体"}]{#struct_0_12031_59956_1608157616}

[[no route to BSR *address*]{lang="EN-US"}]{#struct_0_12031_59956_x1115782758}

[[没有通往]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_x1961803246}[的路由信息]{style="font-family:宋体"}

[[BSM from BSR *address* comes from wrong interface *interface*]{lang="EN-US"}]{#struct_0_12031_59956_1608354224}

[[收到来自错误接口的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_x1917061514}[报文]{style="font-family:宋体"}

[[Source address *address1* is not next hop to BSR %A (next hop is*address2*)]{lang="EN-US"}]{#struct_0_12031_59956_x1075415816}

[[源地址不是通往]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1608288688}[的下一跳地址]{style="font-family:宋体"}

[[Received a BSR packet from other PIM-SM domain from *address* on *interface*]{lang="EN-US"}]{#struct_0_12031_59956_x387135237}

[[收到来自其他]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}]{#struct_0_12031_59956_x685077651}[域的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received a BSR packet from *address* with too short length ]{lang="EN-US"}]{#struct_0_12031_59956_1608485296}

[[收到长度过短的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_781216373}[报文]{style="font-family:宋体"}

[[Received BSR packet with bad hash mask length]{lang="EN-US"}]{#struct_0_12031_59956_x423457358}

[[收到哈希掩码长度错误的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1608419760}[报文]{style="font-family:宋体"}

[[Received a BSR packet from unknown neighbor *address*]{lang="EN-US"}]{#struct_0_12031_59956_407518422}

[[收到来自未知邻居的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1607961009}[报文]{style="font-family:宋体"}

[[Scope]{lang="EN-US"}]{#struct_0_12031_59956_x940009635}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_1113991646}[域]{style="font-family:宋体"}

[[Group: *address*/*mask* \-\-- RP Count: *m*, Frag RP Count: *n*]{lang="EN-US"}]{#struct_0_12031_59956_1607895473}

[[BSR]{lang="EN-US"}]{#struct_0_12031_59956_591227375}[自举报文中的组]{style="font-family:宋体"}*[address]{lang="EN-US"}*[/*length*]{lang="EN-US"}[对应的]{style="font-family:宋体"}[Frag]{lang="EN-US"}[字段的数目为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[，]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的数目为]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[RP count *m* differs from previous *n*,  or  accumulative frag count *k* is wrong]{lang="EN-US"}]{#struct_0_12031_59956_x626747763}

[[RP]{lang="EN-US"}]{#struct_0_12031_59956_1608092081}[数量与之前不同，或者累计分片数量错误]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging pim routing-table]{lang="EN-US"}]{#struct_0_12031_59956_x752207189}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_651548505}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_240566689}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_123273434}

[[RPF Interface]{lang="EN-US"}]{#struct_0_12031_59956_999965266}

[[RPF]{lang="EN-US"}]{#struct_0_12031_59956_x63927081}[接口]{style="font-family:宋体"}

[[multicast boundary]{lang="EN-US"}]{#struct_0_12031_59956_1608026545}

[[组播边界]{style="font-family:宋体"}]{#struct_0_12031_59956_x1126429405}

[[Claim the route]{lang="EN-US"}]{#struct_0_12031_59956_1561082285}

[[组播表项声明使用某条单播路由]{style="font-family:宋体"}]{#struct_0_12031_59956_417676537}

[[Unclaim the route]{lang="EN-US"}]{#struct_0_12031_59956_x1479639493}

[[组播表项声明放弃使用某条单播路由]{style="font-family:宋体"}]{#struct_0_12031_59956_x2074885029}

[[Wrong IIF]{lang="EN-US"}]{#struct_0_12031_59956_1608223153}

[[错误的入接口]{style="font-family:宋体"}]{#struct_0_12031_59956_41660309}

[[Assert state machine]{lang="EN-US"}]{#struct_0_12031_59956_x188529812}

[[断言状态机]{style="font-family:宋体"}]{#struct_0_12031_59956_x1483074417}

[[reg oif]{lang="EN-US"}]{#struct_0_12031_59956_x1469889056}

[[注册出接口]{style="font-family:宋体"}]{#struct_0_12031_59956_x1726671827}

[[ET]{lang="EN-US"}]{#struct_0_12031_59956_1608157617}

[[下游超时定时器]{style="font-family:宋体"}]{#struct_0_12031_59956_x1115717222}

[[Downstream FSM]{lang="EN-US"}]{#struct_0_12031_59956_52211464}

[[下游接口状态机]{style="font-family:宋体"}]{#struct_0_12031_59956_1916680810}

[[PPT]{lang="EN-US"}]{#struct_0_12031_59956_335480034}

[[下游剪枝否决定时器]{style="font-family:宋体"}]{#struct_0_12031_59956_x1964893405}

[[Upstream FSM]{lang="EN-US"}]{#struct_0_12031_59956_1608354225}

[[上游接口状态机]{style="font-family:宋体"}]{#struct_0_12031_59956_x1916995978}

[[NotJoined]{lang="EN-US"}]{#struct_0_12031_59956_1890212964}

[[PIM-SM]{lang="EN-US"}]{#struct_0_12031_59956_x834179141}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）、（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）上游状态机处于未加入状态]{style="font-family:宋体"}

[[Joined]{lang="EN-US"}]{#struct_0_12031_59956_1608288689}

[[PIM-SM]{lang="EN-US"}]{#struct_0_12031_59956_x387200773}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）上游状态机处于加入状态]{style="font-family:宋体"}

[[Join]{lang="EN-US"}]{#struct_0_12031_59956_x241875903}

[[PIM-SM]{lang="EN-US"}]{#struct_0_12031_59956_355251201}[下游状态机处于加入状态]{style="font-family:宋体"}

[[Prune-Pending]{lang="EN-US"}]{#struct_0_12031_59956_x1201720388}

[[下游状态机处于剪枝未决状态]{style="font-family:宋体"}]{#struct_0_12031_59956_1608485297}

[[RPF\'(\*,G)]{lang="EN-US"}]{#struct_0_12031_59956_781150837}

[[（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_12031_59956_441028571}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的上游邻居]{style="font-family:宋体"}

[[RPF\'(S,G)]{lang="EN-US"}]{#struct_0_12031_59956_1240944182}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12031_59956_1608419761}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的上游邻居]{style="font-family:宋体"}

[[Join suppressed]{lang="EN-US"}]{#struct_0_12031_59956_407583958}

[[从入接口收到给上游邻居的加入，抑制自己的加入]{style="font-family:宋体"}]{#struct_0_12031_59956_861668641}

[[genid changed]{lang="EN-US"}]{#struct_0_12031_59956_x1254291520}

[[Generation ID]{lang="EN-US"}]{#struct_0_12031_59956_1607961006}[变化]{style="font-family:宋体"}

[[override interval]{lang="EN-US"}]{#struct_0_12031_59956_x939288739}

[[剪枝否决时间]{style="font-family:宋体"}]{#struct_0_12031_59956_599361222}

[[NoInfo]{lang="EN-US"}]{#struct_0_12031_59956_x1188929737}

[[下游状态机处于]{style="font-family:宋体"}[Noinfo]{lang="EN-US"}]{#struct_0_12031_59956_1607895470}[状态]{style="font-family:宋体"}

[[NotPruned]{lang="EN-US"}]{#struct_0_12031_59956_591292911}

[[PIM-SM]{lang="EN-US"}]{#struct_0_12031_59956_1285432152}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）上游状态机处于非剪枝状态]{style="font-family:宋体"}

[[Pruned]{lang="EN-US"}]{#struct_0_12031_59956_1608092078}

[[PIM-SM]{lang="EN-US"}]{#struct_0_12031_59956_x752796998}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）上游状态机处于剪枝状态]{style="font-family:宋体"}

[[override timer]{lang="EN-US"}]{#struct_0_12031_59956_1449932560}

[[剪枝覆盖定时器]{style="font-family:宋体"}]{#struct_0_12031_59956_812341627}

[[PruneTmp]{lang="EN-US"}]{#struct_0_12031_59956_1608026542}

[[PIM-SM]{lang="EN-US"}]{#struct_0_12031_59956_x1126232797}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）下游状态机处于]{style="font-family:宋体"}[Prune Tmp]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[PrunePendingTmp]{lang="EN-US"}]{#struct_0_12031_59956_1390226139}

[[PIM-SM]{lang="EN-US"}]{#struct_0_12031_59956_1608223150}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）下游状态机处于]{style="font-family:宋体"}[Prune Pending Tmp]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[RP changed, no RP is available for*(\*,G)* now]{lang="EN-US"}]{#struct_0_12031_59956_41856917}

[[RP]{lang="EN-US"}]{#struct_0_12031_59956_161209267}[变化，没有当前（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项可用的]{style="font-family:宋体"}[RP]{lang="EN-US"}

[[RP changed, update the upstream state of *(\*,G)*]{lang="EN-US"}]{#struct_0_12031_59956_1608157614}

[[RP]{lang="EN-US"}]{#struct_0_12031_59956_x1115651686}[变化，更新（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的上游状态]{style="font-family:宋体"}

[[SPT switch]{lang="EN-US"}]{#struct_0_12031_59956_1551343972}

[[SPT]{lang="EN-US"}]{#struct_0_12031_59956_1608354222}[切换]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging pim state-refresh]{lang="EN-US"}]{#struct_0_12031_59956_x1917454730}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_649565600}[[字段]{style="font-family:黑体"}]{#struct_0_12031_59956_x1704164407}

[[描述]{style="font-family:黑体"}]{#struct_0_12031_59956_1073421095}

[[SRM]{lang="EN-US"}]{#struct_0_12031_59956_x1769685009}

[[状态刷新报文]{style="font-family:宋体"}]{#struct_0_12031_59956_x928106315}

[[Drop SRM for (S, G) because of rate limit]{lang="EN-US"}]{#struct_0_12031_59956_1653151648}

[[由于对状态刷新报文的接收进行限速，因此丢弃此期间收到的状态刷新报文]{style="font-family:宋体"}]{#struct_0_12031_59956_1608288686}

[[Drop SRM for (S, G) because of invalid ttl(0) or interval(0)]{lang="EN-US"}]{#struct_0_12031_59956_x386742021}

[[丢弃]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_12031_59956_1305500633}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或发送间隔为]{style="font-family:宋体"}[0]{lang="EN-US"}[的状态刷新报文]{style="font-family:宋体"}

[[Originator address]{lang="EN-US"}]{#struct_0_12031_59956_1568809798}

[[产生状态刷新报文的地址]{style="font-family:宋体"}]{#struct_0_12031_59956_x1216404849}

[[preference]{lang="EN-US"}]{#struct_0_12031_59956_1443618256}

[[报文的优先级字段]{style="font-family:宋体"}]{#struct_0_12031_59956_1608485294}

[[metric]{lang="EN-US"}]{#struct_0_12031_59956_781085301}

[[报文的]{style="font-family:宋体"}[Metric]{lang="EN-US"}]{#struct_0_12031_59956_1653903061}[字段]{style="font-family:宋体"}

[[mask length]{lang="EN-US"}]{#struct_0_12031_59956_1220658718}

[[报文的掩码长度字段]{style="font-family:宋体"}]{#struct_0_12031_59956_567203957}

[[ttl]{lang="EN-US"}]{#struct_0_12031_59956_1608419758}

[[报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_12031_59956_408042709}[值]{style="font-family:宋体"}

[[prune indicator]{lang="EN-US"}]{#struct_0_12031_59956_1598013629}

[[Prune Indicator]{lang="EN-US"}]{#struct_0_12031_59956_x825689379}[标志位]{style="font-family:宋体"}

[[prune now]{lang="EN-US"}]{#struct_0_12031_59956_2132744974}

[[Prune Now]{lang="EN-US"}]{#struct_0_12031_59956_1607961007}[标志位]{style="font-family:宋体"}

[[assert override]{lang="EN-US"}]{#struct_0_12031_59956_x939354275}

[[Assert Override]{lang="EN-US"}]{#struct_0_12031_59956_999165901}[标志位]{style="font-family:宋体"}

[[Interval]{lang="EN-US"}]{#struct_0_12031_59956_1289641119}

[[状态刷新报文的发送间隔]{style="font-family:宋体"}]{#struct_0_12031_59956_138537930}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12031_59956_x903788712}

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_1607895471}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[PIM]{lang="EN-US"}[断言报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim assert received]{lang="EN-US"}]{#struct_0_12031_59956_591358447}

[\*Dec 10 13:53:28:147 2010 Sysname PIM/7/ASSERT: -MDC=1; Received assert packet for (2.1.1.1, 225.0.0.25), 5.1.1.10 -\> 224.0.0.13 on GigabitEthernet1/0/1, Rbit: 0, Preference: 10, Metric: 2. (SM141564)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_911722229}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到一个针对表项（]{style="font-family:宋体"}[2.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）的断言报文，报文源地址为]{style="font-family:宋体"}[5.1.1.10]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[224.0.0.13]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[标志为]{style="font-family:宋体"}[0]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[，度量值为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\*Dec 10 13:53:28:190 2010 Sysname PIM/7/ASSERT: -MDC=1; Assert (2.1.1.1, 225.0.0.25) GigabitEthernet1/0/1 FSM Loser-\>Loser, acceptable assert received from current Winner. (SM041341)]{lang="EN-US"}]{#struct_0_12031_59956_592132544}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x112016078}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的表项（]{style="font-family:宋体"}[2.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）的断言状态机保持]{style="font-family:宋体"}[Loser]{lang="EN-US"}[状态，此时从当前的]{style="font-family:宋体"}[Winner]{lang="EN-US"}[收到一个可接受的断言报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_1608092079}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[PIM]{lang="EN-US"}[断言报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim assert send]{lang="EN-US"}]{#struct_0_12031_59956_x752731462}

[\*Dec 10 13:54:04:921 2010 Sysname PIM/7/ASSERT: -MDC=1; PIM ver 2 assert packet sending 5.1.1.10 -\> 224.0.0.13 for (2.1.1.1, 225.0.0.25) through interface GigabitEthernet1/0/1, Rbit: 0, Preference: 10, Metric: 2. (SM04155)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_614497810}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送一个针对表项（]{style="font-family:宋体"}[2.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）的断言报文，报文源地址为]{style="font-family:宋体"}[5.1.1.10]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[224.0.0.13]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[标志为]{style="font-family:宋体"}[0]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[，度量值为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_1900923856}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例双向]{style="font-family:宋体"}[PIM DF]{lang="EN-US"}[选举的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim df]{lang="EN-US"}]{#struct_0_12031_59956_1608026543}

[\*Dec 27 12:02:01:846 2012 Sysname PIM/7/DF: -MDC=1; Start DF election on interface GigabitEthernet1/0/1 of RP 1.1.0.1 (BD012845)]{lang="EN-US"}

[\*Dec 27 12:02:01:846 2012 Sysname PIM/7/DF: -MDC=1; Create DFT for RP: 1.1.0.1 on interface GigabitEthernet1/0/1, expire time is 1880 msec (BD012050)]{lang="EN-US"}

[\*Dec 27 12:02:01:846 2012 Sysname PIM/7/DF: -MDC=1; Set MC to 0 for RP (1.1.0.1) on interface GigabitEthernet1/0/1 (BD01523)]{lang="EN-US"}

[\*Dec 27 12:02:02:803 2012 Sysname PIM/7/DF: -MDC=1; Send bidir-pim offer packet for RP (1.1.0.1) on interface GigabitEthernet1/0/1. (BD01200)]{lang="EN-US"}

[\*Dec 27 12:02:02:803 2012 Sysname PIM/7/DF: -MDC=1; DF FSM Offer-\>Offer for RP (1.1.0.1) on interface GigabitEthernet1/0/1, while DFT expires and MC is less than robustness (BD011974)]{lang="EN-US"}

[\*Dec 27 12:02:02:803 2012 Sysname PIM/7/DF: -MDC=1; Set MC to 1 for RP (1.1.0.1) on interface GigabitEthernet1/0/1 (BD01523)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x1126298333}*[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.0.1]{lang="EN-US"}[，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上触发]{style="font-family:宋体"}[DF]{lang="EN-US"}[选举。启动]{style="font-family:宋体"}[DF]{lang="EN-US"}[选举定时器并设置]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文的发送个数为]{style="font-family:宋体"}[0]{lang="EN-US"}[，该定时器超时后发送]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文，并设置]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文的发送个数为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Dec 27 12:02:03:882 2012 Sysname PIM/7/DF: -MDC=1; Send bidir-pim offer packet for RP (1.1.0.1) on interface GigabitEthernet1/0/1. (BD01200)]{lang="EN-US"}]{#struct_0_12031_59956_1318156965}

[\*Dec 27 12:02:03:952 2012 Sysname PIM/7/DF: -MDC=1; DF FSM Offer-\>Win for RP (1.1.0.1) on interface GigabitEthernet1/0/1, while DFT expires and MC is equal to robustness and we have path to RPA (BD011974)]{lang="EN-US"}

[\*Dec 27 12:02:03:952 2012 Sysname PIM/7/DF: -MDC=1; Set DF to 8.13.0.1 (pref: 0, metric: 0) for RP (1.1.0.1) on interface GigabitEthernet1/0/1 (BD01394)]{lang="EN-US"}

[\*Dec 27 12:02:03:952 2012 Sysname PIM/7/DF: -MDC=1; Send bidir-pim winner packet for RP (1.1.0.1) on interface GigabitEthernet1/0/1. (BD01200)]{lang="EN-US"}

[\*Dec 27 12:02:03:953 2012 Sysname PIM/7/DF: -MDC=1; Create WinTimer for RP: 1.1.0.1 on interface GigabitEthernet1/0/1, expire time is 5000 msec (BD012275)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x1749225922}*[定时器再次超时后发送]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文，]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文的发送个数等于健壮系数，接口的]{style="font-family:宋体"}[DF]{lang="EN-US"}[状态由]{style="font-family:宋体"}[Offer]{lang="EN-US"}[切换为]{style="font-family:宋体"}[Win]{lang="EN-US"}[。将]{style="font-family:宋体"}[DF]{lang="EN-US"}[设置为本接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[8.13.0.1]{lang="EN-US"}[，发送]{style="font-family:宋体"}[Winner]{lang="EN-US"}[报文并设置]{style="font-family:宋体"}[Winner]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_198179454}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[PIM]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim error]{lang="EN-US"}]{#struct_0_12031_59956_1608223151}

[\*Dec 10 13:57:31:714 2010 Sysname PIM/7/ERROR: -MDC=1; Received a PIM packet from unknown neighbor 6.1.1.3. Ignored. (PM08341)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_41791381}*[从未知邻居]{style="font-family:宋体"}[6.1.1.3]{lang="EN-US"}[收到一个]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文，将其忽略]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_x1006665778}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[PIM]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim event]{lang="EN-US"}]{#struct_0_12031_59956_90723236}

[\*Dec 14 18:24:27:191 2010 Sysname PIM/7/EVENT: -MDC=1; Receive No-Cache msg for (1.0.0.7,/225.0.0.25) with IIF GigabitEthernet1/0/1. (SM161073)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_2123274960}*[收到一个未知组播流消息，组播流源地址为]{style="font-family:宋体"}[1.0.0.7]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[，入接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_1608157615}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[PIM]{lang="EN-US"}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim join-prune received]{lang="EN-US"}]{#struct_0_12031_59956_1608354223}

[\*Dec 10 10:43:05:326 2010 Sysname PIM/7/JP: -MDC=1; PIM ver 2 JP received 6.1.1.5 -\> 224.0.0.13 on interface GigabitEthernet1/0/1 (SM141126)]{lang="EN-US"}

[\*Dec 10 10:43:05:331 2010 Sysname PIM/7/JP: -MDC=1;  Upstream: 6.0.0.10, Number of groups: 1, Holdtime: 210 (SM141128)]{lang="EN-US"}

[\*Dec 10 10:43:05:339 2010 Sysname PIM/7/JP: -MDC=1;  Group: 225.0.0.25 \-\-- 1 joins 0 prunes (SM141134)]{lang="EN-US"}

[\*Dec 10 10:43:05:349 2010 Sysname PIM/7/JP: -MDC=1;   Join: 3.0.0.5 \-\-- Flags: S (SM141138)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x1917389194}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}[的加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文，报文源地址为]{style="font-family:宋体"}[6.1.1.5]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[224.0.0.13]{lang="EN-US"}[，上游邻居为]{style="font-family:宋体"}[6.0.0.10]{lang="EN-US"}[，组数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒，组播组]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[的信息为：]{style="font-family:宋体"}[1]{lang="EN-US"}[个加入，]{style="font-family:宋体"}[0]{lang="EN-US"}[个剪枝；加入]{style="font-family:宋体"}[3.0.0.5]{lang="EN-US"}[，]{style="font-family:宋体"}[S]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_x1821633610}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[PIM]{lang="EN-US"}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim join-prune send]{lang="EN-US"}]{#struct_0_12031_59956_1608485295}

[\*Dec 10 10:43:06:415 2010 Sysname PIM/7/JP: -MDC=1; Send a JP packet to interface GigabitEthernet1/0/1. (PM09198)]{lang="EN-US"}

[\*Dec 10 10:43:06:416 2010 Sysname PIM/7/JP: -MDC=1;  Upstream: 5.0.0.10, Groups: 1, Holdtime: 210 (PM09200)]{lang="EN-US"}

[\*Dec 10 10:43:06:416 2010 Sysname PIM/7/JP: -MDC=1;  Group: 225.0.0.25 \-\-- 1 joins 0 prunes (PM09206)]{lang="EN-US"}

[\*Dec 10 10:43:06:417 2010 Sysname PIM/7/JP: -MDC=1;   Join: 3.0.0.5 \-\-- Flags: S (PM09210)  ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_781019765}*[向接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文，上游邻居为]{style="font-family:宋体"}[5.0.0.10]{lang="EN-US"}[，组数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒，组播组]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[的信息为：]{style="font-family:宋体"}[1]{lang="EN-US"}[个加入，]{style="font-family:宋体"}[0]{lang="EN-US"}[个剪枝；加入]{style="font-family:宋体"}[3.0.0.5]{lang="EN-US"}[，]{style="font-family:宋体"}[S]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_x1436524520}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[PIM Hello]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim neighbor receive]{lang="EN-US"}]{#struct_0_12031_59956_x1120922345}

[\*Dec 10 10:31:45:76 2010 Sysname PIM/7/NBR: -MDC=1; Received Hello packet from neighbor 3.0.0.5, incoming interface is GigabitEthernet1/0/1. (PM073099)]{lang="EN-US"}

[\*Dec 10 10:31:45:89 2010 Sysname PIM/7/NBR: -MDC=1; Holdtime: 105 (PM073147)]{lang="EN-US"}

[\*Dec 10 10:31:45:98 2010 Sysname PIM/7/NBR: -MDC=1; Tbit: 0, Lan delay: 500, Override interval: 2500 (PM073184)]{lang="EN-US"}

[\*Dec 10 10:31:45:101 2010 Sysname PIM/7/NBR: -MDC=1; DR priority: 1 (PM073207)]{lang="EN-US"}

[\*Dec 10 10:31:45:119 2010 Sysname PIM/7/NBR: -MDC=1; Genid: 0xB3DC0254 (PM073231)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_341325956}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上收到源地址为]{style="font-family:宋体"}[3.0.0.5]{lang="EN-US"}[的]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，保持时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒，]{style="font-family:宋体"}[T]{lang="EN-US"}[位没有设置，剪枝延迟时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒，剪枝否决时间为]{style="font-family:宋体"}[2500]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[DR]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0xB3DC0254]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_1880829084}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[PIM Hello]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim neighbor send]{lang="EN-US"}]{#struct_0_12031_59956_x1120856809}

[\*Dec 10 10:31:31:241 2010 Sysname PIM/7/NBR: -MDC=1; PIM ver 2 Hello sending 3.0.0.10 -\> 224.0.0.13 on GigabitEthernet1/0/1 (PM071410)]{lang="EN-US"}

[\*Dec 10 10:31:31:244 2010 Sysname PIM/7/NBR: -MDC=1; Holdtime: 105 s (PM071412)]{lang="EN-US"}

[\*Dec 10 10:31:31:247 2010 Sysname PIM/7/NBR: -MDC=1; Tbit: 0, Lan delay: 500 ms, Override interval: 2500 ms (PM071416)]{lang="EN-US"}

[\*Dec 10 10:31:31:249 2010 Sysname PIM/7/NBR: -MDC=1; DR priority: 1 (PM071418)]{lang="EN-US"}

[\*Dec 10 10:31:31:251 2010 Sysname PIM/7/NBR: -MDC=1; Genid: 0x7EF237CB (PM071420)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x461386880}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，源地址为]{style="font-family:宋体"}[3.0.0.10]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[224.0.0.13]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒，]{style="font-family:宋体"}[T]{lang="EN-US"}[位没有设置，剪枝延迟时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒，剪枝否决时间为]{style="font-family:宋体"}[2500]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[DR]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[为]{style="font-family:宋体"}[07EF237CB]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_1041554573}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[PIM]{lang="EN-US"}[注册报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim register]{lang="EN-US"}]{#struct_0_12031_59956_x1120660201}

[\*Dec 10 10:51:15:332 2010 Sysname PIM/7/REG: -MDC=1; (1.0.0.5, 225.0.0.25) register state transited from NoInfo to Join due to CouldRegister(S,G) == True. Add reg tunnel. (SM06512)]{lang="EN-US"}

[\*Dec 10 10:51:15:340 2010 Sysname PIM/7/REG: -MDC=1; Add register oiffor (1.0.0.5, 225.0.0.25) (SM061336)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x1905841443}*[表项（]{style="font-family:宋体"}[1.0.0.5]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）的注册状态机由]{style="font-family:宋体"}[NoInfo]{lang="EN-US"}[状态变为加入状态。添加注册通道，并为该表项添加注册出接口]{style="font-family:宋体"}*

[[\*Dec 10 10:51:25:382 2010 Sysname PIM/7/REG: -MDC=1; PIM ver 2 Reg-Stop received 5.0.0.10 -\> 1.0.0.10 for (1.0.0.5, 225.0.0.25) (SM061767)]{lang="EN-US"}]{#struct_0_12031_59956_x1120398057}

[\*Dec 10 10:51:25:391 2010 Sysname PIM/7/REG: -MDC=1; Received register-stop message for (1.0.0.5, 225.0.0.25). (SM061834)]{lang="EN-US"}

[\*Dec 10 10:51:25:399 2010 Sysname PIM/7/REG: -MDC=1; (1.0.0.5, 225.0.0.25) register state transited from Join to Prune due to received RegStop. Remove reg tunnel, set RST to 61s. (SM06695)]{lang="EN-US"}

[\*Dec 10 10:51:25:404 2010 Sysname PIM/7/REG: -MDC=1; RST(61s) create successfully for (1.0.0.5, 225.0.0.25). (SM06388)]{lang="EN-US"}

[\*Dec 10 10:51:25:425 2010 Sysname PIM/7/REG: -MDC=1; Delete register oif for (1.0.0.5, 225.0.0.25) (SM061428) ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x1013799146}*[从接口收到]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}[的表项（]{style="font-family:宋体"}[1.0.0.5]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）的注册终止报文，源地址为]{style="font-family:宋体"}[5.0.0.10]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[1.0.0.10]{lang="EN-US"}[。该表项的注册状态机由加入状态变为剪枝状态，删除注册通道。设置注册停止定时器时间为]{style="font-family:宋体"}[61]{lang="EN-US"}[秒，注册停止定时器被成功地创建。删除该表项的注册出接口]{style="font-family:宋体"}*

[[\*May  3 07:09:25:137 2013 Sysname PIM/7/REG: -MDC=1; Register packets of (7.11.0.123, 225.1.1.1) not forwarded because no active local RP exists. (SM06406)]{lang="EN-US"}]{#struct_0_12031_59956_x117865304}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x992268046}*[由于没有激活的本地]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[存在，不为（]{style="font-family:宋体"}[7.11.0.123]{lang="EN-US"}[，]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[）转发注册报文]{style="font-family:宋体"}*

[[\*May  3 07:09:25:137 2013 Sysname PIM/7/REG: -MDC=1; Register packets of (7.11.0.123, 225.1.1.1) not forwarded because the source address belongs to the Anycast-RP set. (SM061936)]{lang="EN-US"}]{#struct_0_12031_59956_x788954969}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_362354616}*[由于源地址在]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[集中，不为（]{style="font-family:宋体"}[7.11.0.123]{lang="EN-US"}[，]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[）转发注册报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_x993504988}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[RP]{lang="EN-US"}[相关报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim rp receive]{lang="EN-US"}]{#struct_0_12031_59956_x1120463593}

[\*Dec 10 10:55:41:438 2010 Sysname PIM/7/RP: -MDC=1; Received a C-RP-Adv Packet from self, prefix count 1, priority 192, holdtime 150, RP address 5.0.0.10. (RP03676)]{lang="EN-US"}

[\*Dec 10 10:55:41:438 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4, Bbit: 0, Zbit: 0 (RP03681)]{lang="EN-US"}

[*[// RP]{lang="EN-US"}*]{#struct_0_12031_59956_x1148447732}*[收到一个自已发送的]{style="font-family:宋体"}[RP]{lang="EN-US"}[宣告报文，前缀数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[192]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[150]{lang="EN-US"}[秒，]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5.0.0.10]{lang="EN-US"}[。组播组]{style="font-family:宋体"}[224.0.0.0/4]{lang="EN-US"}[的信息为：]{style="font-family:宋体"}[B]{lang="EN-US"}[位没有设置，]{style="font-family:宋体"}[Z]{lang="EN-US"}[位没有设置]{style="font-family:宋体"}*

[[\*Dec 10 10:54:55:54 2010 Sysname PIM/7/RP: -MDC=1; Received BSM packet on GigabitEthernet1/0/1 from 3.0.0.10. Scope Global, Nbit: 0, Fragment tag: 0x5e67, Hash mask len: 30, BSR Priority: 64, BSR address: 4.0.0.10. (RP04760)]{lang="EN-US"}]{#struct_0_12031_59956_x1120922344}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_1907409897}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到一个]{style="font-family:宋体"}[BSR]{lang="EN-US"}[自举报文，源地址为]{style="font-family:宋体"}[3.0.0.10]{lang="EN-US"}[，属全局域，]{style="font-family:宋体"}[N]{lang="EN-US"}[位没有设置，分片信息为]{style="font-family:宋体"}[0x5e67]{lang="EN-US"}[，哈希掩码长度为]{style="font-family:宋体"}[30]{lang="EN-US"}[，]{style="font-family:宋体"}[BSR]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[，]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址为]{style="font-family:宋体"}[4.0.0.10]{lang="EN-US"}*

[[\*Dec 10 10:54:55:55 2010 Sysname PIM/7/RP: -MDC=1; Scope \'Global\' receive an event of \'Receive Preferred BSM\' at state \'Accept Preferred\'. (RP042346)]{lang="EN-US"}]{#struct_0_12031_59956_x1120987880}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x1071651302}*[全局域内在]{style="font-family:宋体"}[Accept Preferred]{lang="EN-US"}[状态下收到一个更优]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的自举报文]{style="font-family:宋体"}*

[[\*Dec 10 10:54:55:56 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4 \-\-- RPCount: 1, Frag RP Count: 1 (RP05535)]{lang="EN-US"}]{#struct_0_12031_59956_x1120856808}

[\*Dec 10 10:54:55:56 2010 Sysname PIM/7/RP: -MDC=1;   RP: 5.0.0.10 \-\-- Holdtime 180, Priority 192 (RP05539)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x2027470821}*[组播组]{style="font-family:宋体"}[224.0.0.0/4]{lang="EN-US"}[的信息为：]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[个数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，分片信息为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5.0.0.10]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，优先级为]{style="font-family:宋体"}[192]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_784617994}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[RP]{lang="EN-US"}[相关报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim rp send]{lang="EN-US"}]{#struct_0_12031_59956_x1120725736}

[\*Dec 10 10:54:55:56 2010 Sysname PIM/7/RP: -MDC=1; Send out BSM packet to interface GigabitEthernet1/0/1. (PM09364)]{lang="EN-US"}

[\*Dec 10 10:54:55:57 2010 Sysname PIM/7/RP: -MDC=1;  Nbit: 0, Fragment tag: 0x5e67, Hash mask len: 30, BSR Priority: 64, BSR address: 4.0.0.10. (PM09368)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x542790373}*[向接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[BSR]{lang="EN-US"}[自举报文。]{style="font-family:宋体"}[N]{lang="EN-US"}[位没有设置，分片信息为]{style="font-family:宋体"}[0x5E67]{lang="EN-US"}[，哈希掩码长度为]{style="font-family:宋体"}[30]{lang="EN-US"}[，]{style="font-family:宋体"}[BSR]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[，]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址为]{style="font-family:宋体"}[4.0.0.10]{lang="EN-US"}*

[[\*Dec 10 10:54:55:57 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4, Bbit:0, Zbit: 0, RP Count: 1, Frag RP Count: 1 (PM09378)]{lang="EN-US"}]{#struct_0_12031_59956_x1120594664}

[\*Dec 10 10:54:55:57 2010 Sysname PIM/7/RP: -MDC=1;   RP: 5.0.0.10 \-\-- Holdtime 180, Priority 192 (PM09382)]{lang="EN-US"}

[\*Dec 10 10:54:55:105 2010 Sysname PIM/7/RP: -MDC=1; Set BST of scope Global to 130. (RP041140)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_3420793}*[组播组]{style="font-family:宋体"}[224.0.0.0/4]{lang="EN-US"}[的信息为：]{style="font-family:宋体"}[B]{lang="EN-US"}[位没有设置，]{style="font-family:宋体"}[Z]{lang="EN-US"}[位没有设置，]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[个数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，分片信息为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5.0.0.10]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，优先级为]{style="font-family:宋体"}[192]{lang="EN-US"}[。设置全局域自举定时器为]{style="font-family:宋体"}[130]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Dec 10 10:55:57:439 2010 Sysname PIM/7/RP: -MDC=1; Send BSM packet to all neighbor in scope Global. (RP011260)]{lang="EN-US"}]{#struct_0_12031_59956_x1120398056}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_1715084209}*[自举路由器向全局域内的所有邻居发送自举报文]{style="font-family:宋体"}*

[[\*Dec 10 10:55:57:443 2010 Sysname PIM/7/RP: -MDC=1; EBSR updates RPs by self in scope Global. (RP01984)]{lang="EN-US"}]{#struct_0_12031_59956_x1120987883}

[\*Dec 10 10:55:57:443 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4 \-\-- RP Count: 1, Frag RP Count: 1 (RP05535)]{lang="EN-US"}

[\*Dec 10 10:55:57:444 2010 Sysname PIM/7/RP: -MDC=1;   RP: 5.0.0.10 \-\-- Holdtime 180, Priority 192 (RP05539)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_494432639}*[被选中的自举路由器在全局域内更新]{style="font-family:宋体"}[RP]{lang="EN-US"}[，组播组]{style="font-family:宋体"}[224.0.0.0/4]{lang="EN-US"}[的信息为：]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[个数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，分片信息为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5.0.0.10]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，优先级为]{style="font-family:宋体"}[192]{lang="EN-US"}*

[[\*Dec 10 10:55:57:448 2010 Sysname PIM/7/RP: -MDC=1; Send out BSM packet to interface GigabitEthernet1/0/1. (PM09364)]{lang="EN-US"}]{#struct_0_12031_59956_x1120856811}

[\*Dec 10 10:55:57:448 2010 Sysname PIM/7/RP: -MDC=1;  Nbit: 0, Fragment tag: 0x5e67, Hash mask len: 30, BSR Priority: 64, BSR address: 4.0.0.10. (PM09368)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x105090984}*[向接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[BSR]{lang="EN-US"}[自举报文，]{style="font-family:宋体"}[N]{lang="EN-US"}[位没有设置，分片信息为]{style="font-family:宋体"}[0x5e67]{lang="EN-US"}[，哈希掩码长度为]{style="font-family:宋体"}[30]{lang="EN-US"}[，]{style="font-family:宋体"}[BSR]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[，]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址为]{style="font-family:宋体"}[4.0.0.10]{lang="EN-US"}*

[[\*Dec 10 10:55:57:452 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4, Bbit: 0, Zbit: 0, RP Count: 1, Frag RP Count: 1 (PM09378)]{lang="EN-US"}]{#struct_0_12031_59956_x1120529131}

[\*Dec 10 10:55:57:453 2010 Sysname PIM/7/RP: -MDC=1;   RP: 5.0.0.10 \-\-- Holdtime 180, Priority 192 (PM09382)]{lang="EN-US"}

[\*Dec 10 10:55:57:503 2010 Sysname PIM/7/RP: -MDC=1; Set BST of scope Global to 60. (RP041140)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x414577938}*[组播组]{style="font-family:宋体"}[224.0.0.0/4]{lang="EN-US"}[的信息为：]{style="font-family:宋体"}[B]{lang="EN-US"}[位没有设置，]{style="font-family:宋体"}[Z]{lang="EN-US"}[位没有设置，]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[个数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，分片信息为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5.0.0.10]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，优先级为]{style="font-family:宋体"}[192]{lang="EN-US"}[。设置全局域自举定时器为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_x1120594667}[接口上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[PIM]{lang="EN-US"}[组播路由表状态改变调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim routing-table]{lang="EN-US"}]{#struct_0_12031_59956_x1120398059}

[\*Dec 10 10:46:32:258 2010 Sysname PIM/7/ROUTE: -MDC=1; Creating (4.0.0.5, 225.0.0.25), flags: 0x00000004, down if protocol: 0 (SM134084)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x207230092}*[创建表项（]{style="font-family:宋体"}[4.0.0.5]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[），标志为]{style="font-family:宋体"}[0x00000004]{lang="EN-US"}[，下游接口协议号为]{style="font-family:宋体"}[0]{lang="EN-US"}[（表示]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Dec 10 10:46:32:272 2010 Sysname PIM/7/ROUTE: -MDC=1; ET(210s) create successfully for downstream (4.0.0.5, 225.0.0.25) on interface GigabitEthernet1/0/1 (6.0.0.10) (SM07344)]{lang="EN-US"}]{#struct_0_12031_59956_x1120463595}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_14351682}*[为表项（]{style="font-family:宋体"}[4.0.0.5]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）的出接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[6.0.0.10]{lang="EN-US"}[）创建超时定时器（]{style="font-family:宋体"}[210]{lang="EN-US"}[秒）成功]{style="font-family:宋体"}*

[[\*Dec 10 10:46:32:273 2010 Sysname PIM/7/ROUTE: -MDC=1; Downstream (4.0.0.5, 225.0.0.25) FSM on interface GigabitEthernet1/0/1 (6.0.0.10) transited from NoInfo to Join. Join Received (SM071418)]{lang="EN-US"}]{#struct_0_12031_59956_x1120922346}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x1224757985}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的表项（]{style="font-family:宋体"}[4.0.0.5]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）的下游状态机从]{style="font-family:宋体"}[NoInfo]{lang="EN-US"}[状态越迁到加入状态，原因是收到加入报文]{style="font-family:宋体"}*

[[\*Dec 10 10:46:46:515 2010 Sysname PIM/7/ROUTE: -MDC=1; Delete (3.0.0.5, 225.0.0.25) for inactive (SM12343)]{lang="EN-US"}]{#struct_0_12031_59956_x1120987882}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_2060516580}*[删除老化的表项（]{style="font-family:宋体"}[3.0.0.5]{lang="EN-US"}[，]{style="font-family:宋体"}[225.0.0.25]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_x1120791274}[在接口上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[PIM]{lang="EN-US"}[状态刷新报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim state-refresh receive]{lang="EN-US"}]{#struct_0_12031_59956_x1120856810}

[\*Mar 16 05:50:15:086 2012 Sysname PIM/7/SRM: -MDC=1; PIM ver 2 SRM receiving 8.12.0.1 -\> 224.0.0.13 for (7.11.0.100, 225.0.0.1) on GigabitEthernet1/0/1, Originator address: 7.11.0.1, preference: 0, metric: 0, mask length: 16, ttl: 255, prune indicator: unset, prune now: unset, assert override: set, interval: 60s (DM141415)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_x1671174925}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到状态刷新报文，报文的源地址是]{style="font-family:宋体"}[8.12.0.1]{lang="EN-US"}[，目的地址是]{style="font-family:宋体"}[224.0.0.13]{lang="EN-US"}[；组播组为]{style="font-family:宋体"}[225.0.0.1/32]{lang="EN-US"}[；组播源为]{style="font-family:宋体"}[7.11.0.100]{lang="EN-US"}[；产生状态刷新报文设备的地址为]{style="font-family:宋体"}[7.11.0.1]{lang="EN-US"}[；优先级和]{style="font-family:宋体"}[Metric]{lang="EN-US"}[值都是]{style="font-family:宋体"}[0]{lang="EN-US"}[；掩码长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[；]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[255]{lang="EN-US"}[，没有设置]{style="font-family:宋体"}[Prune Indicator]{lang="EN-US"}[和]{style="font-family:宋体"}[Prune Now]{lang="EN-US"}[标志位，设置了]{style="font-family:宋体"}[Assert Override]{lang="EN-US"}[标志位；发送间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12031_59956_1573218260}[在接口上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[PIM]{lang="EN-US"}[状态刷新报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pim state-refresh send]{lang="EN-US"}]{#struct_0_12031_59956_x1120660202}

[\*Mar 16 05:50:15:086 2012 Sysname PIM/7/SRM: -MDC=1; PIM ver 2 SRM sending 8.24.0.2 -\> 224.0.0.13 for (7.11.0.100, 225.0.0.1) on GigabitEthernet1/0/1, Originator address: 7.11.0.1, preference: 10, metric: 2, mask length: 16, ttl: 254, prune indicator: unset, prune now: unset, assert override: set, interval: 60s. (DM09330)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12031_59956_823041912}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送状态刷新报文，报文的源地址是]{style="font-family:宋体"}[8.24.0.2]{lang="EN-US"}[，目的地址是]{style="font-family:宋体"}[224.0.0.13]{lang="EN-US"}[；组播组为]{style="font-family:宋体"}[225.0.0.1/32]{lang="EN-US"}[；组播源为]{style="font-family:宋体"}[7.11.0.100]{lang="EN-US"}[；产生状态刷新报文设备的地址为]{style="font-family:宋体"}[7.11.0.1]{lang="EN-US"}[；优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[；]{style="font-family:宋体"}[Metric]{lang="EN-US"}[值为]{style="font-family:宋体"}[2]{lang="EN-US"}[；掩码长度都是]{style="font-family:宋体"}[16]{lang="EN-US"}[；]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}[254]{lang="EN-US"}[，没有设置]{style="font-family:宋体"}[Prune Indicator]{lang="EN-US"}[和]{style="font-family:宋体"}[Prune Now]{lang="EN-US"}[标志位，设置了]{style="font-family:宋体"}[Assert Override]{lang="EN-US"}[标志位；发送间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*
