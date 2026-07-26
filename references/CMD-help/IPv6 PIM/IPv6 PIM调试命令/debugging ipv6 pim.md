::: {#2102252583 .myid}
[]{#_Toc404790269}[]{#struct_0_20343_19272_x1826475172}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**IPv6 PIM \-- IPv6 PIM调试命令 \-- debugging ipv6 pim**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20343_19272_1271391447}

[**[debugging ipv6 pim]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **df** \| **error** \| { **event** \| **register** \| **routing-table** } \[ *advanced-acl6-number* \] \| { **assert** \| **join-prune** \| **rp** \| **state-refresh** } \[ *advanced-acl6-number* \] \[ **receive** \| **send** \] \| **neighbor** \[ *basic-acl6-number* \] \[ **receive** \| **send** \] }]{lang="EN-US"}]{#struct_0_20343_19272_1335083147}

[**[undo debugging ipv6 pim]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **df** \| **error** \| **event** \| **register** \| **routing-table** \| { **assert** \| **join-prune** \| **neighbor** \| **rp** \| **state-refresh** } \[ **receive** \| **send** \] }]{lang="EN-US"}]{#struct_0_20343_19272_1816627642}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20343_19272_1634040186}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20343_19272_x1363733230}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20343_19272_443767003}

[[network-admin]{lang="EN-US"}]{#struct_0_20343_19272_1781399777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20343_19272_1817462616}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20343_19272_520493930}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_20343_19272_597175122}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_20343_19272_1271456983}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[df]{lang="EN-US"}**]{#struct_0_20343_19272_162459693}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM DF]{lang="EN-US"}[选举调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_20343_19272_x1092204025}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_20343_19272_x1495771414}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[register]{lang="EN-US"}**]{#struct_0_20343_19272_x1376655279}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[注册报文调试信息开关。]{style="font-family:宋体"}

[**[routing-table]{lang="EN-US"}**]{#struct_0_20343_19272_1261454091}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[组播路由表状态改变调试信息开关。]{style="font-family:宋体"}

[*[advanced-acl6-number]{lang="EN-US"}*]{#struct_0_20343_19272_1563829691}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[assert]{lang="EN-US"}**]{#struct_0_20343_19272_1923490447}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[断言报文调试信息开关。]{style="font-family:宋体"}

[**[join-prune]{lang="EN-US"}**]{#struct_0_20343_19272_1294021464}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文调试信息开关。]{style="font-family:宋体"}

[**[rp]{lang="EN-US"}**]{#struct_0_20343_19272_1271522519}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[RP]{lang="EN-US"}[相关报文的调试信息开关。]{style="font-family:宋体"}

[**[state-refresh]{lang="EN-US"}**]{#struct_0_20343_19272_x1383981669}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[状态刷新报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_20343_19272_x245970700}[：表示接收的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_20343_19272_x1131277901}[：表示发送的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[neighbor]{lang="EN-US"}**]{#struct_0_20343_19272_x100441916}[：表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[与邻居信息相关的调试信息开关。]{style="font-family:宋体"}

[*[basic-acl6-number]{lang="EN-US"}*]{#struct_0_20343_19272_x1521064452}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20343_19272_1038974311}

[**[debugging ipv6 pim]{lang="EN-US"}**]{#struct_0_20343_19272_1493385609}[命令用来打开]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 pim]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_20343_19272_1270539479}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ipv6 pim assert]{lang="EN-US"}]{#struct_0_20343_19272_215816940}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1922035498}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_x1759295380}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_272115516}

[[Assert FSM]{lang="EN-US"}]{#struct_0_20343_19272_1663879462}

[[断言状态机]{style="font-family:宋体"}]{#struct_0_20343_19272_x1915411828}

[*[state1]{lang="EN-US"}*[-\>*state2*]{lang="EN-US"}]{#struct_0_20343_19272_x472559060}

[[断言状态机从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*]{#struct_0_20343_19272_1270605015}[转换到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[[loser/winner/noinfo]{lang="EN-US"}]{#struct_0_20343_19272_x634285419}

[[断言状态机处于]{style="font-family:宋体"}[Loser/Winner/Noinfo]{lang="EN-US"}]{#struct_0_20343_19272_564501226}[状态]{style="font-family:宋体"}

[[timeout of the winner]{lang="EN-US"}]{#struct_0_20343_19272_x1000191591}

[[Winner]{lang="EN-US"}]{#struct_0_20343_19272_x508526376}[老化]{style="font-family:宋体"}

[[Rbit]{lang="EN-US"}]{#struct_0_20343_19272_x810427779}

[[RPT]{lang="EN-US"}]{#struct_0_20343_19272_x1457819585}[标识位]{style="font-family:宋体"}

[[Preference]{lang="EN-US"}]{#struct_0_20343_19272_689028422}

[[优先级字段]{style="font-family:宋体"}]{#struct_0_20343_19272_1476922704}

[[Metric]{lang="EN-US"}]{#struct_0_20343_19272_778312982}

[[Metric]{lang="EN-US"}]{#struct_0_20343_19272_x1036571251}[字段]{style="font-family:宋体"}

[[assert timer expired]{lang="EN-US"}]{#struct_0_20343_19272_947081759}

[[断言定时器超时]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457754049}

[[insufficient memory]{lang="EN-US"}]{#struct_0_20343_19272_1844539337}

[[内存不足]{style="font-family:宋体"}]{#struct_0_20343_19272_669605029}

[[inferior assert]{lang="EN-US"}]{#struct_0_20343_19272_x217105618}

[[度量值比自身差的断言报文]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457688513}

[[acceptable assert]{lang="EN-US"}]{#struct_0_20343_19272_x1321159145}

[[来自断言获胜路由器的度量值比自身好的断言报文]{style="font-family:宋体"}]{#struct_0_20343_19272_x991358452}

[[preferred assert]{lang="EN-US"}]{#struct_0_20343_19272_x1037860623}

[[比当前断言获胜路由器具备更优开销的断言报文]{style="font-family:宋体"}]{#struct_0_20343_19272_71782617}

[[NIIF]{lang="EN-US"}]{#struct_0_20343_19272_x1457622977}

[[入接口为空]{style="font-family:宋体"}]{#struct_0_20343_19272_x871608051}

[[OIF]{lang="EN-US"}]{#struct_0_20343_19272_834690540}

[[出接口]{style="font-family:宋体"}]{#struct_0_20343_19272_505544885}

[[(\*,G) Entry is not exist]{lang="EN-US"}]{#struct_0_20343_19272_328513900}

[[（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_20343_19272_x1457557441}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项不存在]{style="font-family:宋体"}

[[self metric]{lang="EN-US"}]{#struct_0_20343_19272_1350093549}

[[自身到源的路由度量值]{style="font-family:宋体"}]{#struct_0_20343_19272_1796458308}

[[unknown neighbor]{lang="EN-US"}]{#struct_0_20343_19272_1534440272}

[[未知邻居]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457491905}

[[wrong packet length]{lang="EN-US"}]{#struct_0_20343_19272_1366780362}

[[报文长度非法]{style="font-family:宋体"}]{#struct_0_20343_19272_1762218865}

[[bad group address]{lang="EN-US"}]{#struct_0_20343_19272_640593719}

[[错误的组地址]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457426369}

[[invalid group address]{lang="EN-US"}]{#struct_0_20343_19272_x962006899}

[[非法的组地址]{style="font-family:宋体"}]{#struct_0_20343_19272_1120656377}

[[group boundary]{lang="EN-US"}]{#struct_0_20343_19272_x259241375}

[[组边界]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457360833}

[[bad source address]{lang="EN-US"}]{#struct_0_20343_19272_1931828916}

[[错误的源地址]{style="font-family:宋体"}]{#struct_0_20343_19272_x1961707286}

[[invalid source address]{lang="EN-US"}]{#struct_0_20343_19272_1398333002}

[[非法的源地址]{style="font-family:宋体"}]{#struct_0_20343_19272_x1458343873}

[[SSM group]{lang="EN-US"}]{#struct_0_20343_19272_x809722721}

[[SSM]{lang="EN-US"}]{#struct_0_20343_19272_x1752758191}[组]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ipv6 pim df]{lang="EN-US"}]{#struct_0_20343_19272_1340892980}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1919261098}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_x1458278337}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_x2064985561}

[[DF election/DF-Election]{lang="EN-US"}]{#struct_0_20343_19272_x228669532}

[[DF]{lang="EN-US"}]{#struct_0_20343_19272_790567690}[选举]{style="font-family:宋体"}

[[DFT]{lang="EN-US"}]{#struct_0_20343_19272_x1648758156}

[[DF]{lang="EN-US"}]{#struct_0_20343_19272_x1095089631}[选举定时器]{style="font-family:宋体"}

[[WinTimer]{lang="EN-US"}]{#struct_0_20343_19272_x1457819584}

[[Winner]{lang="EN-US"}]{#struct_0_20343_19272_x877055519}[定时器]{style="font-family:宋体"}

[[expire time]{lang="EN-US"}]{#struct_0_20343_19272_x1513988245}

[[定时器的超时时间]{style="font-family:宋体"}]{#struct_0_20343_19272_x993327814}

[[MC]{lang="EN-US"}]{#struct_0_20343_19272_1558813280}

[[Offer]{lang="EN-US"}]{#struct_0_20343_19272_1114621503}[或]{style="font-family:宋体"}[Winner]{lang="EN-US"}[报文的发送个数]{style="font-family:宋体"}

[[robustness]{lang="EN-US"}]{#struct_0_20343_19272_x1457754048}

[[DF]{lang="EN-US"}]{#struct_0_20343_19272_278455396}[选举健壮系数，缺省值为]{style="font-family:宋体"}[3]{lang="EN-US"}

[[RPL]{lang="EN-US"}]{#struct_0_20343_19272_x27199878}

[[RPL]{lang="EN-US"}]{#struct_0_20343_19272_1752260116}[链路]{style="font-family:宋体"}

[[Offer]{lang="EN-US"}]{#struct_0_20343_19272_2142643539}

[[DF]{lang="EN-US"}]{#struct_0_20343_19272_x1457688512}[选举的初始状态]{style="font-family:宋体"}

[[Lose]{lang="EN-US"}]{#struct_0_20343_19272_244924796}

[[DF]{lang="EN-US"}]{#struct_0_20343_19272_x773459962}[选举失败]{style="font-family:宋体"}

[[Win]{lang="EN-US"}]{#struct_0_20343_19272_1949100305}

[[DF]{lang="EN-US"}]{#struct_0_20343_19272_x594984009}[选举胜出]{style="font-family:宋体"}

[[Backoff]{lang="EN-US"}]{#struct_0_20343_19272_1359608053}

[[处于]{style="font-family:宋体"}[Win]{lang="EN-US"}]{#struct_0_20343_19272_x1457622976}[状态的]{style="font-family:宋体"}[DF]{lang="EN-US"}[收到更优的]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[DF FSM]{lang="EN-US"}]{#struct_0_20343_19272_694475890}

[[DF]{lang="EN-US"}]{#struct_0_20343_19272_868993570}[选举状态]{style="font-family:宋体"}

[[Receive better Backoff/Pass/Offer/Win]{lang="EN-US"}]{#struct_0_20343_19272_1807866152}

[[收到更优的]{style="font-family:宋体"}[Backoff/Pass/Offer/Win]{lang="EN-US"}]{#struct_0_20343_19272_x1457557440}[报文]{style="font-family:宋体"}

[[Receive worse Backoff/Pass/Offer/Win]{lang="EN-US"}]{#struct_0_20343_19272_x215990392}

[[收到更差的]{style="font-family:宋体"}[Backoff/Pass/Offer/Win]{lang="EN-US"}]{#struct_0_20343_19272_x40447221}[报文]{style="font-family:宋体"}

[[Receive Backoff/Pass for us]{lang="EN-US"}]{#struct_0_20343_19272_x1837168597}

[[收到通告自己的]{style="font-family:宋体"}[Backoff/Pass]{lang="EN-US"}]{#struct_0_20343_19272_1492516116}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ipv6 pim error]{lang="EN-US"}]{#struct_0_20343_19272_x1457491904}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1914797642}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_x199303579}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_x1707096070}

[[IPC data]{lang="EN-US"}]{#struct_0_20343_19272_x1851411872}

[[用于进程间通信的数据]{style="font-family:宋体"}]{#struct_0_20343_19272_1579780432}

[[Mfib]{lang="EN-US"}]{#struct_0_20343_19272_813315234}

[[组播转发信息库]{style="font-family:宋体"}]{#struct_0_20343_19272_x253945859}

[[Reference]{lang="EN-US"}]{#struct_0_20343_19272_x1457426368}

[[引用计数]{style="font-family:宋体"}]{#struct_0_20343_19272_604077042}

[[config info]{lang="EN-US"}]{#struct_0_20343_19272_x1888737972}

[[配置信息]{style="font-family:宋体"}]{#struct_0_20343_19272_398448705}

[[insufficient memory]{lang="EN-US"}]{#struct_0_20343_19272_x1847800504}

[[内存不足]{style="font-family:宋体"}]{#struct_0_20343_19272_434457327}

[[secondary address node]{lang="EN-US"}]{#struct_0_20343_19272_x1457360832}

[[二级地址节点]{style="font-family:宋体"}]{#struct_0_20343_19272_x797054439}

[[unsupported PIM packet type]{lang="EN-US"}]{#struct_0_20343_19272_1514534831}

[[不支持的]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_20343_19272_1592973038}[数据包类型]{style="font-family:宋体"}

[[checksum error]{lang="EN-US"}]{#struct_0_20343_19272_x800327243}

[[检验和字段错误]{style="font-family:宋体"}]{#struct_0_20343_19272_x1458343872}

[[invalid pim interface]{lang="EN-US"}]{#struct_0_20343_19272_756361220}

[[非法的]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_20343_19272_x60743083}[接口]{style="font-family:宋体"}

[[unknown neighbor]{lang="EN-US"}]{#struct_0_20343_19272_2146365796}

[[未知邻居]{style="font-family:宋体"}]{#struct_0_20343_19272_x926492440}

[[CRPT]{lang="EN-US"}]{#struct_0_20343_19272_x1458278336}

[[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_663897794}[发送定时器]{style="font-family:宋体"}

[[Blank Group]{lang="EN-US"}]{#struct_0_20343_19272_1437702767}

[[不存在]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_x545260042}[的组]{style="font-family:宋体"}

[[Fail to get ifindex]{lang="EN-US"}]{#struct_0_20343_19272_x272691033}

[[获取接口索引失败]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457819587}

[[best route]{lang="EN-US"}]{#struct_0_20343_19272_x473770992}

[[最优路由]{style="font-family:宋体"}]{#struct_0_20343_19272_1106969259}

[[Assert_Timer]{lang="EN-US"}]{#struct_0_20343_19272_x784188357}

[[断言定时器]{style="font-family:宋体"}]{#struct_0_20343_19272_x771317879}

[[invalid event]{lang="EN-US"}]{#struct_0_20343_19272_x1457754051}

[[非法事件]{style="font-family:宋体"}]{#struct_0_20343_19272_1488243441}

[[MRIB]{lang="EN-US"}]{#struct_0_20343_19272_x360250595}

[[组播路由信息库]{style="font-family:宋体"}]{#struct_0_20343_19272_x168484711}

[[valid RPF interface]{lang="EN-US"}]{#struct_0_20343_19272_x1457688515}

[[合法的]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_20343_19272_x2127728199}[邻居]{style="font-family:宋体"}

[[Ifstate]{lang="EN-US"}]{#struct_0_20343_19272_150712527}

[[接口状态]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457622979}

[[negotiation]{lang="EN-US"}]{#struct_0_20343_19272_x421269357}

[[协商]{style="font-family:宋体"}]{#struct_0_20343_19272_804198948}

[[wrong flag]{lang="EN-US"}]{#struct_0_20343_19272_1973909489}

[[错误标识]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457557443}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging ipv6 pim event]{lang="EN-US"}]{#struct_0_20343_19272_187294135}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1944781994}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_661372746}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_581851953}

[[PIM mrt]{lang="EN-US"}]{#struct_0_20343_19272_1862018242}

[[PIM]{lang="EN-US"}]{#struct_0_20343_19272_x596594952}[组播路由表]{style="font-family:宋体"}

[[No-Cache msg]{lang="EN-US"}]{#struct_0_20343_19272_x1855653772}

[[未知组播消息]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457491907}

[[Wrong-If msg]{lang="EN-US"}]{#struct_0_20343_19272_203980948}

[[从非入接口收到组播流消息]{style="font-family:宋体"}]{#struct_0_20343_19272_x478857257}

[[SPT msg]{lang="EN-US"}]{#struct_0_20343_19272_1411205637}

[[SPT]{lang="EN-US"}]{#struct_0_20343_19272_470967093}[切换消息]{style="font-family:宋体"}

[[Active msg]{lang="EN-US"}]{#struct_0_20343_19272_174395305}

[[MFIB]{lang="EN-US"}]{#struct_0_20343_19272_x1457426371}[上报新的组播流消息]{style="font-family:宋体"}

[[Inactive msg]{lang="EN-US"}]{#struct_0_20343_19272_x605711003}

[[MFIB]{lang="EN-US"}]{#struct_0_20343_19272_x1222285793}[上报流老化消息]{style="font-family:宋体"}

[[Reg-Timeout msg]{lang="EN-US"}]{#struct_0_20343_19272_x1181446489}

[[注册定时器超时消息]{style="font-family:宋体"}]{#struct_0_20343_19272_1305581142}

[[reset forwarding-table msg]{lang="EN-US"}]{#struct_0_20343_19272_794662878}

[[MIFB]{lang="EN-US"}]{#struct_0_20343_19272_x1457360835}[转发表重置消息]{style="font-family:宋体"}

[[Received BFD event: *type*, *source* -\> *destination*, *interface*]{lang="EN-US"}]{#struct_0_20343_19272_x1556569326}

[[收到]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_20343_19272_x1849221028}[会话消息：类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ipv6 pim join-prune]{lang="EN-US"}]{#struct_0_20343_19272_x1720948526}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1941008042}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_1717659669}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_x1825295079}

[[JP]{lang="EN-US"}]{#struct_0_20343_19272_x1458343875}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20343_19272_x1972522135}[剪枝报文]{style="font-family:宋体"}

[[Upstream]{lang="EN-US"}]{#struct_0_20343_19272_1417233105}

[[报文中的上游邻居信息]{style="font-family:宋体"}]{#struct_0_20343_19272_118466454}

[[Groups]{lang="EN-US"}]{#struct_0_20343_19272_x833926760}

[[报文中的组数目信息]{style="font-family:宋体"}]{#struct_0_20343_19272_x1100023364}

[[Holdtime]{lang="EN-US"}]{#struct_0_20343_19272_2085798889}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20343_19272_x1458278339}[剪枝报文的保持时间字段]{style="font-family:宋体"}

[[Group: *addr*/*mask* \-\-- *m* joins *n* prunes]{lang="EN-US"}]{#struct_0_20343_19272_x545955787}

[[报文中的组信息：组地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20343_19272_x1071533079}[掩码长度------]{style="font-family:宋体"}*[m]{lang="EN-US"}*[个加入]{style="font-family:宋体"}*[n]{lang="EN-US"}*[个剪枝]{style="font-family:宋体"}

[[Join: *addr/mask* flag]{lang="EN-US"}]{#struct_0_20343_19272_x99393107}

[[加入：源地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20343_19272_1926607338}[掩码，标志位]{style="font-family:宋体"}

[[RP change]{lang="EN-US"}]{#struct_0_20343_19272_x1457819586}

[[RP]{lang="EN-US"}]{#struct_0_20343_19272_x2039854933}[发生变化]{style="font-family:宋体"}

[[the packet is received from interface *A*, but destination is *B*. Ignored.]{lang="EN-US"}]{#struct_0_20343_19272_x1102350067}

[[从接口]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_20343_19272_x1410913212}[上收到一个发给]{style="font-family:宋体"}[B]{lang="EN-US"}[的报文，将其丢弃]{style="font-family:宋体"}

[[Message Truncated]{lang="EN-US"}]{#struct_0_20343_19272_x343867230}

[[报文长度非法]{style="font-family:宋体"}]{#struct_0_20343_19272_x1548367156}

[[multicast boundary]{lang="EN-US"}]{#struct_0_20343_19272_x1457754050}

[[组播边界]{style="font-family:宋体"}]{#struct_0_20343_19272_x77840500}

[[Join/Prune received from non-local neighbor]{lang="EN-US"}]{#struct_0_20343_19272_268525647}

[[从不属于本接口网段的上游邻居收到一个加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20343_19272_540300257}[剪枝报文]{style="font-family:宋体"}

[*[Address ]{lang="EN-US"}*[is not a valid multicast address]{lang="EN-US"}]{#struct_0_20343_19272_x1457688514}

[*[Address]{lang="EN-US"}*]{#struct_0_20343_19272_x561644258}[是一个非法组播地址]{style="font-family:宋体"}

[[Message from unknown neighbor]{lang="EN-US"}]{#struct_0_20343_19272_1612379126}

[[从未知邻居收到报文]{style="font-family:宋体"}]{#struct_0_20343_19272_574895490}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging ipv6 pim neighbor]{lang="EN-US"}]{#struct_0_20343_19272_1181769566}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1933794506}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_x1457622978}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_1144814584}

[[hello packet]{lang="EN-US"}]{#struct_0_20343_19272_x12685206}

[[PIM Hello]{lang="EN-US"}]{#struct_0_20343_19272_914615056}[报文]{style="font-family:宋体"}

[[invalid secondary address]{lang="EN-US"}]{#struct_0_20343_19272_x1722129983}

[[非法二级地址]{style="font-family:宋体"}]{#struct_0_20343_19272_x19370496}

[[Holdtime]{lang="EN-US"}]{#struct_0_20343_19272_x1457557442}

[[PIM Hello]{lang="EN-US"}]{#struct_0_20343_19272_x1378789806}[报文的保持时间字段]{style="font-family:宋体"}

[[Tbit]{lang="EN-US"}]{#struct_0_20343_19272_x358948699}

[[T]{lang="EN-US"}]{#struct_0_20343_19272_460167119}[位选项]{style="font-family:宋体"}

[[Lan delay]{lang="EN-US"}]{#struct_0_20343_19272_212567102}

[[剪枝延迟时间选项]{style="font-family:宋体"}]{#struct_0_20343_19272_x1293706182}

[[Override interval]{lang="EN-US"}]{#struct_0_20343_19272_x1457491906}

[[剪枝否决时间选项]{style="font-family:宋体"}]{#struct_0_20343_19272_x1362102993}

[[DR priority]{lang="EN-US"}]{#struct_0_20343_19272_601792111}

[[DR]{lang="EN-US"}]{#struct_0_20343_19272_1565815723}[优先级选项]{style="font-family:宋体"}

[[Genid]{lang="EN-US"}]{#struct_0_20343_19272_x1006528052}

[[Generation ID]{lang="EN-US"}]{#struct_0_20343_19272_x1457426370}[选项]{style="font-family:宋体"}

[[Discarding Hello packet from *address* without Generation ID.]{lang="EN-US"}]{#struct_0_20343_19272_960372938}

[[丢弃没有]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}]{#struct_0_20343_19272_443439899}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[the neighbor information being refreshed]{lang="EN-US"}]{#struct_0_20343_19272_1873519832}

[[更新邻居信息]{style="font-family:宋体"}]{#struct_0_20343_19272_1145772784}

[[Too many neighbors, ignoring new neighbor *address*.]{lang="EN-US"}]{#struct_0_20343_19272_x1457360834}

[[邻居过多，忽略新的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20343_19272_9514615}[报文]{style="font-family:宋体"}

[[secondary address list]{lang="EN-US"}]{#struct_0_20343_19272_x112896993}

[[二级地址列表]{style="font-family:宋体"}]{#struct_0_20343_19272_x1529955234}

[[bad secondary address]{lang="EN-US"}]{#struct_0_20343_19272_x1458343874}

[[错误的二级地址]{style="font-family:宋体"}]{#struct_0_20343_19272_x406438194}

[[Received Hello packet from invalid source: *address*]{lang="EN-US"}]{#struct_0_20343_19272_x1634298303}

[[收到来自非法源地址的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20343_19272_x1996941462}[报文]{style="font-family:宋体"}

[[Received Hello packet on *interface* from non-local source: *address*]{lang="EN-US"}]{#struct_0_20343_19272_x1572222606}

[[收到非本地主机的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20343_19272_x1458278338}[报文]{style="font-family:宋体"}

[[Received Hello packet with short data from *address*]{lang="EN-US"}]{#struct_0_20343_19272_x2112039728}

[[收到数据不完整的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20343_19272_409295404}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with wrong Holdtime length:]{lang="EN-US"}]{#struct_0_20343_19272_1601508553}

[[收到]{style="font-family:宋体"}[Holdtime]{lang="EN-US"}]{#struct_0_20343_19272_x1457819589}[选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with invalid LAN Prune Delay length:]{lang="EN-US"}]{#struct_0_20343_19272_x1992800766}

[[收到]{style="font-family:宋体"}[LAN Prune Delay]{lang="EN-US"}]{#struct_0_20343_19272_x2036045429}[选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with invalid DR Priority length:]{lang="EN-US"}]{#struct_0_20343_19272_x1457754053}

[[收到]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_20343_19272_325444027}[优先级选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with invalid Generation ID length:]{lang="EN-US"}]{#struct_0_20343_19272_192552212}

[[收到]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}]{#struct_0_20343_19272_x390914959}[选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with invalid State Refresh length:]{lang="EN-US"}]{#struct_0_20343_19272_x1457688517}

[[收到状态更新选项长度非法的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20343_19272_1004439683}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with Bidir option]{lang="EN-US"}]{#struct_0_20343_19272_x843825951}

[[收到带有双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_20343_19272_1262990332}[选项的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with unsupported option:]{lang="EN-US"}]{#struct_0_20343_19272_x1457622981}

[[收到带有错误选项的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20343_19272_x66022037}[报文]{style="font-family:宋体"}

[[Received Hello packet from *address* with wrong data length]{lang="EN-US"}]{#struct_0_20343_19272_136847516}

[[收到长度错误的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20343_19272_x1457557445}[报文]{style="font-family:宋体"}

[[Notify create/delete/disable BFD session *source* -\> *destination*, *interface*]{lang="EN-US"}]{#struct_0_20343_19272_x975505279}

[[通知创建]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20343_19272_1496408116}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging ipv6 pim register]{lang="EN-US"}]{#struct_0_20343_19272_1517663056}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1933145930}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_x1457491909}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_x602588106}

[[probe]{lang="EN-US"}]{#struct_0_20343_19272_1965266458}

[[探测报文]{style="font-family:宋体"}]{#struct_0_20343_19272_167120819}

[[no route to RP]{lang="EN-US"}]{#struct_0_20343_19272_1864274025}

[[没有通往]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_20343_19272_1959470712}[的路由]{style="font-family:宋体"}

[[not knowing RP]{lang="EN-US"}]{#struct_0_20343_19272_x1457426373}

[[未知]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_20343_19272_557088411}

[[register packet]{lang="EN-US"}]{#struct_0_20343_19272_x234883833}

[[注册报文]{style="font-family:宋体"}]{#struct_0_20343_19272_2051299251}

[[Bbit]{lang="EN-US"}]{#struct_0_20343_19272_x1031714680}

[[边界位]{style="font-family:宋体"}]{#struct_0_20343_19272_2131217605}

[[Nbit]{lang="EN-US"}]{#struct_0_20343_19272_x1457360837}

[[空位]{style="font-family:宋体"}]{#struct_0_20343_19272_x393769912}

[[RST]{lang="EN-US"}]{#struct_0_20343_19272_1358040278}

[[注册停止定时器]{style="font-family:宋体"}]{#struct_0_20343_19272_868558102}

[[register state]{lang="EN-US"}]{#struct_0_20343_19272_1313604946}

[[注册状态机状态]{style="font-family:宋体"}]{#struct_0_20343_19272_x1458343877}

[[reg tunnel]{lang="EN-US"}]{#struct_0_20343_19272_1159645747}

[[注册通道]{style="font-family:宋体"}]{#struct_0_20343_19272_x1319969340}

[[reg-stop packet]{lang="EN-US"}]{#struct_0_20343_19272_539666002}

[[注册停止报文]{style="font-family:宋体"}]{#struct_0_20343_19272_x530233235}

[[invalid RPF interface]{lang="EN-US"}]{#struct_0_20343_19272_x1458278341}

[[非法的]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_20343_19272_x902644899}[接口]{style="font-family:宋体"}

[[RP changed]{lang="EN-US"}]{#struct_0_20343_19272_797230103}

[[RP]{lang="EN-US"}]{#struct_0_20343_19272_2034214532}[发生变化]{style="font-family:宋体"}

[[Null-Register]{lang="EN-US"}]{#struct_0_20343_19272_1787573739}

[[空注册报文]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457819588}

[[register oif]{lang="EN-US"}]{#struct_0_20343_19272_736082589}

[[注册出接口]{style="font-family:宋体"}]{#struct_0_20343_19272_1772716620}

[[the group address *address* is not valid.]{lang="EN-US"}]{#struct_0_20343_19272_x1653936059}

[[组地址非法]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457754052}

[[Received register-stop message with bad group masks from *address* for *address/mask*.]{lang="EN-US"}]{#struct_0_20343_19272_x1240639914}

[[收到组掩码错误的注册终止报文]{style="font-family:宋体"}]{#struct_0_20343_19272_775798137}

[[the source address is not valid]{lang="EN-US"}]{#struct_0_20343_19272_2463705}

[[源地址非法]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457688516}

[[RP for group *address* is unknown.]{lang="EN-US"}]{#struct_0_20343_19272_x1724443672}

[[相关组的]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_20343_19272_x2066180456}[未知]{style="font-family:宋体"}

[[RP dispute for *address*]{lang="EN-US"}]{#struct_0_20343_19272_x1464035414}

[[RP]{lang="EN-US"}]{#struct_0_20343_19272_x1457622980}[映射错误]{style="font-family:宋体"}

[[no matching entry for *(S,G)*]{lang="EN-US"}]{#struct_0_20343_19272_1500061904}

[[没有相关的（]{style="font-family:宋体"}*[S]{lang="EN-US"}*]{#struct_0_20343_19272_x1784768380}*[，]{style="font-family:宋体"}[G]{lang="EN-US"}*[）表项]{style="font-family:宋体"}

[[Anycast-RP timer]{lang="EN-US"}]{#struct_0_20343_19272_x2028907415}

[[Anycast-RP]{lang="EN-US"}]{#struct_0_20343_19272_x712026100}[定时器]{style="font-family:宋体"}

[[the source address belongs to the Anycast-RP set]{lang="EN-US"}]{#struct_0_20343_19272_x409552146}

[[源地址在]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}]{#struct_0_20343_19272_x107051861}[集中]{style="font-family:宋体"}

[[Notify MFIB not to suppress register packets]{lang="EN-US"}]{#struct_0_20343_19272_780297495}

[[通知]{style="font-family:宋体"}[MFIB]{lang="EN-US"}]{#struct_0_20343_19272_x107117397}[不要抑制注册报文]{style="font-family:宋体"}

[[no active local RP exists]{lang="EN-US"}]{#struct_0_20343_19272_1996770985}

[[没有激活的本地]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_20343_19272_x107182933}[存在]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging ipv6 pim rp]{lang="EN-US"}]{#struct_0_20343_19272_x1131496109}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1961041322}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_x1450513450}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_x245146003}

[[auto-RP announce packet]{lang="EN-US"}]{#struct_0_20343_19272_x1457557444}

[[自动]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_20343_19272_1753378076}[宣告报文]{style="font-family:宋体"}

[[Truncated bootstrap message]{lang="EN-US"}]{#struct_0_20343_19272_946522636}

[[长度非法的自举报文]{style="font-family:宋体"}]{#struct_0_20343_19272_1166290234}

[[BSM packet]{lang="EN-US"}]{#struct_0_20343_19272_x439921653}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x739348902}[自举报文]{style="font-family:宋体"}

[[Nbit]{lang="EN-US"}]{#struct_0_20343_19272_x1457491908}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_2126295249}[报文段禁止转发标志位]{style="font-family:宋体"}

[[Fragment tag]{lang="EN-US"}]{#struct_0_20343_19272_528206152}

[[用于]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_2134235915}[报文的分片]{style="font-family:宋体"}

[[Hash mask len]{lang="EN-US"}]{#struct_0_20343_19272_849920338}

[[哈希掩码长度]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457426372}

[[BSR Priority]{lang="EN-US"}]{#struct_0_20343_19272_2123172352}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x1554771921}[优先级]{style="font-family:宋体"}

[[BSR address]{lang="EN-US"}]{#struct_0_20343_19272_x328557382}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x549286746}[地址]{style="font-family:宋体"}

[[Group]{lang="EN-US"}]{#struct_0_20343_19272_x1358342907}

[[组地址]{style="font-family:宋体"}]{#struct_0_20343_19272_x1457360836}

[[Zbit]{lang="EN-US"}]{#struct_0_20343_19272_1172314029}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x2006775912}[报文段自治域标志位]{style="font-family:宋体"}

[[RP Count]{lang="EN-US"}]{#struct_0_20343_19272_x624376125}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x1458343876}[报文中表示服务这个组播组范围的]{style="font-family:宋体"}[RP]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[Frag RP Count]{lang="EN-US"}]{#struct_0_20343_19272_x1569237608}

[[表示]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x594959477}[分片报文中服务这个组播组范围的]{style="font-family:宋体"}[RP]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[RP: *address* \-\-- Holdtime *holdtime*, Priority *priority*]{lang="EN-US"}]{#struct_0_20343_19272_1035210003}

[[RP]{lang="EN-US"}]{#struct_0_20343_19272_x1458278340}[：地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[------保持时间为]{style="font-family:宋体"}*[holdtime]{lang="EN-US"}*[，优先级为]{style="font-family:宋体"}*[priority]{lang="EN-US"}*

[[Truncated crp packet]{lang="EN-US"}]{#struct_0_20343_19272_1826238456}

[[长度非法的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_1594087677}[宣告报文]{style="font-family:宋体"}

[[C-RP-Adv]{lang="EN-US"}]{#struct_0_20343_19272_2145373518}

[[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_x18365930}[宣告报文]{style="font-family:宋体"}

[[Prefix count]{lang="EN-US"}]{#struct_0_20343_19272_108264356}

[[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_1109852815}[宣告报文中包含的组地址个数]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_20343_19272_1781414315}

[[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_x1777055398}[宣告报文的优先级字段]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_20343_19272_108329892}

[[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_x1181953318}[宣告报文的保持时间字段]{style="font-family:宋体"}

[[RP address]{lang="EN-US"}]{#struct_0_20343_19272_882655363}

[[RP]{lang="EN-US"}]{#struct_0_20343_19272_1211411190}[地址]{style="font-family:宋体"}

[[Failed to build BSM pkt because MTU is too small]{lang="EN-US"}]{#struct_0_20343_19272_108395428}

[[构造]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_699222207}[自举报文失败，原因是]{style="font-family:宋体"}[MTU]{lang="EN-US"}[太小了]{style="font-family:宋体"}

[[BSR boundary]{lang="EN-US"}]{#struct_0_20343_19272_x1584115277}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_108460964}[边界]{style="font-family:宋体"}

[[multicast boundary]{lang="EN-US"}]{#struct_0_20343_19272_1001211631}

[[组播边界]{style="font-family:宋体"}]{#struct_0_20343_19272_x1711826748}

[[EBSR]{lang="EN-US"}]{#struct_0_20343_19272_1529298406}

[[最优]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_108526500}

[[EBSR updates RPs by self in scope]{lang="EN-US"}]{#struct_0_20343_19272_x223232325}

[[最优]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x1474827798}[在域内自动更新了]{style="font-family:宋体"}[RP]{lang="EN-US"}

[[Protocol conflict while updating group *address* for crp *address*.]{lang="EN-US"}]{#struct_0_20343_19272_108592036}

[[更新]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_1364555341}[地址时使用组地址，与协议冲突]{style="font-family:宋体"}

[[Invalid group address]{lang="EN-US"}]{#struct_0_20343_19272_1508678188}

[[非法组地址]{style="font-family:宋体"}]{#struct_0_20343_19272_x1233270649}

[[multicast boundary]{lang="EN-US"}]{#struct_0_20343_19272_108657572}

[[组播边界]{style="font-family:宋体"}]{#struct_0_20343_19272_x1546601004}

[[Received an invalid length C-RP-Adv packet]{lang="EN-US"}]{#struct_0_20343_19272_927504200}

[[收到一个长度非法的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_108723108}[的宣告报文]{style="font-family:宋体"}

[[The length of C-RP-Adv packet is wrong]{lang="EN-US"}]{#struct_0_20343_19272_2024729671}

[[C-RP]{lang="EN-US"}]{#struct_0_20343_19272_x1124122440}[宣告报文长度出错]{style="font-family:宋体"}

[[Received BSR packet with bad bsr address]{lang="EN-US"}]{#struct_0_20343_19272_107740068}

[[收到]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_348730507}[地址非法的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received BSR packet with non-unicast bsr address *address*]{lang="EN-US"}]{#struct_0_20343_19272_x227953263}

[[收到]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_107805604}[地址不是单播地址的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received a BSM with bad first group address from BSR *address*]{lang="EN-US"}]{#struct_0_20343_19272_496758957}

[[收到的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x229634380}[自举报文中第一个组地址错误]{style="font-family:宋体"}

[[Unable to pass multicast boundary check for *address/mask*]{lang="EN-US"}]{#struct_0_20343_19272_108264357}

[[由于组地址和掩码问题无法通过组播边界检查]{style="font-family:宋体"}]{#struct_0_20343_19272_1109852814}

[[no route to BSR *address*]{lang="EN-US"}]{#struct_0_20343_19272_1781479851}

[[没有通往]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_108329893}[的路由信息]{style="font-family:宋体"}

[[BSM from BSR *address* comes from wrong interface *interface*]{lang="EN-US"}]{#struct_0_20343_19272_x1181953319}

[[收到来自错误接口的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x1846227992}[报文]{style="font-family:宋体"}

[[Source address *address1* is not next hop to BSR %A (next hop is*address2*)]{lang="EN-US"}]{#struct_0_20343_19272_108395429}

[[源地址不是通往]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_699222208}[的下一跳地址]{style="font-family:宋体"}

[[Received a BSR packet from other PIM-SM domain from *address* on *interface*]{lang="EN-US"}]{#struct_0_20343_19272_x1584115272}

[[收到来自其他]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}]{#struct_0_20343_19272_108460965}[域的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received a BSR packet from *address* with too short length ]{lang="EN-US"}]{#struct_0_20343_19272_1001211630}

[[收到长度过短的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_108526501}[报文]{style="font-family:宋体"}

[[Received BSR packet with bad hash mask length]{lang="EN-US"}]{#struct_0_20343_19272_x223232326}

[[收到哈希掩码长度错误的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x1474762262}[报文]{style="font-family:宋体"}

[[Received a BSR packet from unknown neighbor *address*]{lang="EN-US"}]{#struct_0_20343_19272_108592037}

[[收到来自未知邻居的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_20343_19272_1364555342}[报文]{style="font-family:宋体"}

[[Scope]{lang="EN-US"}]{#struct_0_20343_19272_108657573}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_x1546601003}[域]{style="font-family:宋体"}

[[Group: *address*/*mask* \-\-- RP Count: *m*, Frag RP Count: *n*]{lang="EN-US"}]{#struct_0_20343_19272_167989313}

[[BSR]{lang="EN-US"}]{#struct_0_20343_19272_108723109}[自举报文中的组]{style="font-family:宋体"}*[address]{lang="EN-US"}*[/*length*]{lang="EN-US"}[对应的]{style="font-family:宋体"}[Frag]{lang="EN-US"}[字段的数目为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[，]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的数目为]{style="font-family:宋体"}*[m]{lang="EN-US"}*

[[RP count *m* differs from previous *n*,  or  accumulative frag count *k* is wrong]{lang="EN-US"}]{#struct_0_20343_19272_2024729670}

[[RP]{lang="EN-US"}]{#struct_0_20343_19272_107740069}[数量与之前不同，或者累计分片数量错误]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging ipv6 pim routing-table]{lang="EN-US"}]{#struct_0_20343_19272_348730506}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1953489290}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_x227953264}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_x179740792}

[[RPF Interface]{lang="EN-US"}]{#struct_0_20343_19272_x842595669}

[[RPF]{lang="EN-US"}]{#struct_0_20343_19272_x302730400}[接口]{style="font-family:宋体"}

[[multicast boundary]{lang="EN-US"}]{#struct_0_20343_19272_107805605}

[[组播边界]{style="font-family:宋体"}]{#struct_0_20343_19272_496758956}

[[Claim the route]{lang="EN-US"}]{#struct_0_20343_19272_x229634379}

[[组播表项声明使用某条单播路由]{style="font-family:宋体"}]{#struct_0_20343_19272_1229795119}

[[Unclaim the route]{lang="EN-US"}]{#struct_0_20343_19272_x739191377}

[[组播表项声明放弃使用某条单播路由]{style="font-family:宋体"}]{#struct_0_20343_19272_1644391793}

[[Wrong IIF]{lang="EN-US"}]{#struct_0_20343_19272_108264354}

[[错误的入接口]{style="font-family:宋体"}]{#struct_0_20343_19272_1109852817}

[[Assert state machine]{lang="EN-US"}]{#struct_0_20343_19272_1781545387}

[[断言状态机]{style="font-family:宋体"}]{#struct_0_20343_19272_949796317}

[[reg oif]{lang="EN-US"}]{#struct_0_20343_19272_x1614538288}

[[注册出接口]{style="font-family:宋体"}]{#struct_0_20343_19272_108329890}

[[ET]{lang="EN-US"}]{#struct_0_20343_19272_x1181953316}

[[下游超时定时器]{style="font-family:宋体"}]{#struct_0_20343_19272_432316669}

[[Downstream FSM]{lang="EN-US"}]{#struct_0_20343_19272_x907791027}

[[下游接口状态机]{style="font-family:宋体"}]{#struct_0_20343_19272_x218864094}

[[PPT]{lang="EN-US"}]{#struct_0_20343_19272_108395426}

[[下游剪枝否决定时器]{style="font-family:宋体"}]{#struct_0_20343_19272_699222201}

[[Upstream FSM]{lang="EN-US"}]{#struct_0_20343_19272_x1584115279}

[[上游接口状态机]{style="font-family:宋体"}]{#struct_0_20343_19272_1845283310}

[[NotJoined]{lang="EN-US"}]{#struct_0_20343_19272_331992956}

[[PIM-SM]{lang="EN-US"}]{#struct_0_20343_19272_108460962}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）、（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）上游状态机处于未加入状态]{style="font-family:宋体"}

[[Joined]{lang="EN-US"}]{#struct_0_20343_19272_1001211633}

[[PIM-SM]{lang="EN-US"}]{#struct_0_20343_19272_x1711695676}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）上游状态机处于加入状态]{style="font-family:宋体"}

[[Join]{lang="EN-US"}]{#struct_0_20343_19272_x724133142}

[[PIM-SM]{lang="EN-US"}]{#struct_0_20343_19272_994598561}[下游状态机处于加入状态]{style="font-family:宋体"}

[[Prune-Pending]{lang="EN-US"}]{#struct_0_20343_19272_108526498}

[[下游状态机处于剪枝未决状态]{style="font-family:宋体"}]{#struct_0_20343_19272_1769818648}

[[RPF\'(\*,G)]{lang="EN-US"}]{#struct_0_20343_19272_x589386257}

[[（]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_20343_19272_925183449}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的上游邻居]{style="font-family:宋体"}

[[RPF\'(S,G)]{lang="EN-US"}]{#struct_0_20343_19272_108592034}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_20343_19272_1364555343}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的上游邻居]{style="font-family:宋体"}

[[Join suppressed]{lang="EN-US"}]{#struct_0_20343_19272_1508547116}

[[从入接口收到给上游邻居的加入，抑制自己的加入]{style="font-family:宋体"}]{#struct_0_20343_19272_x1990098666}

[[genid changed]{lang="EN-US"}]{#struct_0_20343_19272_108657570}

[[Generation ID]{lang="EN-US"}]{#struct_0_20343_19272_x1546601002}[变化]{style="font-family:宋体"}

[[override interval]{lang="EN-US"}]{#struct_0_20343_19272_1734073254}

[[剪枝否决时间]{style="font-family:宋体"}]{#struct_0_20343_19272_x1592161862}

[[NoInfo]{lang="EN-US"}]{#struct_0_20343_19272_108723106}

[[下游状态机处于]{style="font-family:宋体"}[Noinfo]{lang="EN-US"}]{#struct_0_20343_19272_2024729681}[状态]{style="font-family:宋体"}

[[NotPruned]{lang="EN-US"}]{#struct_0_20343_19272_x1124122453}

[[PIM-SM]{lang="EN-US"}]{#struct_0_20343_19272_107740066}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）上游状态机处于非剪枝状态]{style="font-family:宋体"}

[[Pruned]{lang="EN-US"}]{#struct_0_20343_19272_348730497}

[[PIM-SM]{lang="EN-US"}]{#struct_0_20343_19272_528826614}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）上游状态机处于剪枝状态]{style="font-family:宋体"}

[[override timer]{lang="EN-US"}]{#struct_0_20343_19272_x1828499486}

[[剪枝覆盖定时器]{style="font-family:宋体"}]{#struct_0_20343_19272_107805602}

[[PruneTmp]{lang="EN-US"}]{#struct_0_20343_19272_496758955}

[[PIM-SM]{lang="EN-US"}]{#struct_0_20343_19272_x229634382}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）下游状态机处于]{style="font-family:宋体"}[Prune Tmp]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[PrunePendingTmp]{lang="EN-US"}]{#struct_0_20343_19272_108264355}

[[PIM-SM]{lang="EN-US"}]{#struct_0_20343_19272_1109852816}[的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[）下游状态机处于]{style="font-family:宋体"}[Prune Pending Tmp]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[RP changed, no RP is available for*(\*,G)* now]{lang="EN-US"}]{#struct_0_20343_19272_1781610923}

[[RP]{lang="EN-US"}]{#struct_0_20343_19272_108329891}[变化，没有当前（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项可用的]{style="font-family:宋体"}[RP]{lang="EN-US"}

[[RP changed, update the upstream state of *(\*,G)*]{lang="EN-US"}]{#struct_0_20343_19272_x1181953317}

[[RP]{lang="EN-US"}]{#struct_0_20343_19272_1998400610}[变化，更新（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的上游状态]{style="font-family:宋体"}

[[SPT switch]{lang="EN-US"}]{#struct_0_20343_19272_108395427}

[[SPT]{lang="EN-US"}]{#struct_0_20343_19272_699222202}[切换]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging ipv6 pim state-refresh]{lang="EN-US"}]{#struct_0_20343_19272_x1584115282}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1978912202}[[字段]{style="font-family:黑体"}]{#struct_0_20343_19272_1797377175}

[[描述]{style="font-family:黑体"}]{#struct_0_20343_19272_339791211}

[[SRM]{lang="EN-US"}]{#struct_0_20343_19272_108460963}

[[状态刷新报文]{style="font-family:宋体"}]{#struct_0_20343_19272_1001211632}

[[Drop SRM for (S, G) because of rate limit]{lang="EN-US"}]{#struct_0_20343_19272_x1711761212}

[[由于对状态刷新报文的接收进行限速，因此丢弃此期间收到的状态刷新报文]{style="font-family:宋体"}]{#struct_0_20343_19272_10277783}

[[Drop SRM for (S, G) because of invalid hoplimit(0) or interval(0)]{lang="EN-US"}]{#struct_0_20343_19272_x2007971590}

[[丢弃]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}]{#struct_0_20343_19272_1959779684}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或发送间隔为]{style="font-family:宋体"}[0]{lang="EN-US"}[的状态刷新报文]{style="font-family:宋体"}

[[Originator address]{lang="EN-US"}]{#struct_0_20343_19272_x90483483}

[[产生状态刷新报文的地址]{style="font-family:宋体"}]{#struct_0_20343_19272_108526499}

[[preference]{lang="EN-US"}]{#struct_0_20343_19272_1769818647}

[[报文的优先级字段]{style="font-family:宋体"}]{#struct_0_20343_19272_x589845009}

[[metric]{lang="EN-US"}]{#struct_0_20343_19272_171674740}

[[报文的]{style="font-family:宋体"}[Metric]{lang="EN-US"}]{#struct_0_20343_19272_110655838}[字段]{style="font-family:宋体"}

[[mask length]{lang="EN-US"}]{#struct_0_20343_19272_x1183594457}

[[报文的掩码长度字段]{style="font-family:宋体"}]{#struct_0_20343_19272_108592035}

[[hoplimit]{lang="EN-US"}]{#struct_0_20343_19272_1364555344}

[[报文的]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}]{#struct_0_20343_19272_1509005868}[值]{style="font-family:宋体"}

[[prune indicator]{lang="EN-US"}]{#struct_0_20343_19272_x860853514}

[[Prune Indicator]{lang="EN-US"}]{#struct_0_20343_19272_271679384}[标志位]{style="font-family:宋体"}

[[prune now]{lang="EN-US"}]{#struct_0_20343_19272_108657571}

[[Prune Now]{lang="EN-US"}]{#struct_0_20343_19272_x1546601001}[标志位]{style="font-family:宋体"}

[[assert override]{lang="EN-US"}]{#struct_0_20343_19272_1330788727}

[[Assert Override]{lang="EN-US"}]{#struct_0_20343_19272_1654700436}[标志位]{style="font-family:宋体"}

[[Interval]{lang="EN-US"}]{#struct_0_20343_19272_108723107}

[[状态刷新报文的发送间隔]{style="font-family:宋体"}]{#struct_0_20343_19272_2024729680}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20343_19272_x1124056917}

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_x894358291}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[断言报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim assert]{lang="EN-US"}]{#struct_0_20343_19272_107740067}

[%Sep  7 16:40:52:195 2011 Sysname PIM6/7/ASSERT: -MDC=1; IPv6: Received assert packet for (8:12::2, FFE3::101), FE80:8:12::2 -\> FF02::D on GigabitEthernet1/0/1, Rbit: 0, Preference: 100, Metric: 100. (SM141628)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_348730496}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到一个针对表项（]{style="font-family:宋体"}[8:12::2, FFE3::101]{lang="EN-US"}[）的断言报文，报文源地址为]{style="font-family:宋体"}[FE80:8:12::2]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[FF02::D]{lang="EN-US"}[，]{style="font-family:宋体"}[RPT]{lang="EN-US"}[标志为]{style="font-family:宋体"}[0]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[，花销为]{style="font-family:宋体"}[100]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_528826613}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM DF]{lang="EN-US"}[选举的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim df]{lang="EN-US"}]{#struct_0_20343_19272_x1828499485}

[\*Dec 27 13:04:50:371 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Start DF election on interface GigabitEthernet1/0/1 of RP 1:1::1 (BD012845)]{lang="EN-US"}

[\*Dec 27 13:04:50:371 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Create DFT for RP: 1:1::1 on interface GigabitEthernet1/0/1, expire time is 1530 msec (BD012050)]{lang="EN-US"}

[\*Dec 27 13:04:50:371 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Set MC to 0 for RP (1:1::1) on interface GigabitEthernet1/0/1 (BD01523)]{lang="EN-US"}

[\*Dec 27 13:04:50:908 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Send bidir-pim offer packet for RP (1:1::1) on interface GigabitEthernet1/0/1. (BD01200)]{lang="EN-US"}

[\*Dec 27 13:04:51:907 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: DF FSM Offer-\>Offer for RP (1:1::1) on interface GigabitEthernet1/0/1, while DFT expires and MC is lessthan robustness (BD011974)]{lang="EN-US"}

[\*Dec 27 13:04:51:908 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Set MC to 1 for RP (1:1::1) on interface GigabitEthernet1/0/1 (BD01523)]{lang="EN-US"}

[\*Dec 27 13:04:51:908 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Create DFT for RP: 1:1::1 on interface GigabitEthernet1/0/1, expire time is 60 msec (BD012050)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_2001232205}*[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[为]{style="font-family:宋体"}[1:1::1]{lang="EN-US"}[，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上触发]{style="font-family:宋体"}[DF]{lang="EN-US"}[选举。启动]{style="font-family:宋体"}[DF]{lang="EN-US"}[选举定时器并设置]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文的发送个数为]{style="font-family:宋体"}[0]{lang="EN-US"}[，该定时器超时后发送]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文，并设置]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文的发送个数为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Dec 27 13:04:52:048 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Send bidir-pim offer packet for RP (1:1::1) on interface GigabitEthernet1/0/1. (BD01200)]{lang="EN-US"}]{#struct_0_20343_19272_107805603}

[\*Dec 27 13:04:52:117 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: DF FSM Offer-\>Win for RP (1:1::1) on interface GigabitEthernet1/0/1, while DFT expires and MC is equal to robustness and we have path to RPA (BD011974)]{lang="EN-US"}

[\*Dec 27 13:04:52:117 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Set DF to FE80:8:13::1 (pref: 0, metric: 0) for RP (1:1::1) on interface GigabitEthernet1/0/1 (BD01394)]{lang="EN-US"}

[\*Dec 27 13:04:52:118 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Send bidir-pim winner packet for RP (1:1::1) on interface GigabitEthernet1/0/1. (BD01200)]{lang="EN-US"}

[\*Dec 27 13:04:52:118 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Create WinTimer for RP:1:1::1 on interface GigabitEthernet1/0/1, expire time is 5000 msec (BD012275)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_496758954}*[定时器再次超时后发送]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文，]{style="font-family:宋体"}[Offer]{lang="EN-US"}[报文的发送个数等于健壮系数，接口的]{style="font-family:宋体"}[DF]{lang="EN-US"}[状态由]{style="font-family:宋体"}[Offer]{lang="EN-US"}[切换为]{style="font-family:宋体"}[Win]{lang="EN-US"}[。将]{style="font-family:宋体"}[DF]{lang="EN-US"}[设置为本接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[FE80:8:13::1]{lang="EN-US"}[，发送]{style="font-family:宋体"}[Winner]{lang="EN-US"}[报文并设置]{style="font-family:宋体"}[Winner]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_x229634381}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim error]{lang="EN-US"}]{#struct_0_20343_19272_1230319414}

[%Sep  7 16:40:01:700 2011 Sysname PIM6/7/ERROR: -MDC=1; IPv6: Dropping received pkt from FE80:8:12::2 to FF02::D with type 5, for checksum error (PM08321)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1489323388}*[从]{style="font-family:宋体"}[FE80:8:12::2]{lang="EN-US"}[收到一个]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文，因为校验和错误，将其忽略]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_x780270862}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim event]{lang="EN-US"}]{#struct_0_20343_19272_108264352}

[%Sep  7 16:36:06:845 2011 Sysname PIM6/7/EVENT: -MDC=1; IPv6: Recv Rt refresh msg with prefix: 8:12::/64, Nexthop: ::, OutIf: GigabitEthernet1/0/1, Pref: 0, Metric: 0, ProtoID: 1, Flags: 0x10800 (PR03338)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1109852819}*[收到前缀为]{style="font-family:宋体"}[8:12::/64]{lang="EN-US"}[、下一跳为]{style="font-family:宋体"}[::]{lang="EN-US"}[、出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的路由刷新消息，该路由优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[，花销为]{style="font-family:宋体"}[0]{lang="EN-US"}[，协议号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，标志]{style="font-family:宋体"}[0x10800]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_1782200747}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim join-prune]{lang="EN-US"}]{#struct_0_20343_19272_108329888}

[Sep  7 16:38:24:393 2011 Sysname PIM6/7/JP: -MDC=1; IPv6: PIM ver 2 JP received FE80:8:12::4 -\> FF02::D on interface GigabitEthernet1/0/1 (SM141190)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1156698836}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}[的加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文，报文源地址为]{style="font-family:宋体"}[FE80:8:12::4]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[FF02::D]{lang="EN-US"}*

[[%Sep  7 16:38:24:395 2011 Sysname PIM6/7/JP: -MDC=1; IPv6:  Upstream: FE80:8:12::1, Number of groups: 1, Holdtime: 1800 (SM141192)]{lang="EN-US"}]{#struct_0_20343_19272_x408958556}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_x1787783524}*[上游邻居为]{style="font-family:宋体"}[8:12::1]{lang="EN-US"}[，组数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[，保持时间为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[%Sep  7 16:38:24:395 2011 Sysname PIM6/7/JP: -MDC=1; IPv6:  Group: FFE3::101 \-\-- 1 joins 0 prunes (SM141198)]{lang="EN-US"}]{#struct_0_20343_19272_108395424}

[*[// IPv6]{lang="EN-US"}*]{#struct_0_20343_19272_699222203}*[组播组]{style="font-family:宋体"}[FFE3::101]{lang="EN-US"}[的信息为：]{style="font-family:宋体"}[1]{lang="EN-US"}[个加入，]{style="font-family:宋体"}[0]{lang="EN-US"}[个剪枝]{style="font-family:宋体"}*

[[%Sep  7 16:38:24:395 2011 Sysname PIM6/7/JP: -MDC=1; IPv6:   Join: 8:12::1 \-\-- Flags: SWR (SM141202)]{lang="EN-US"}]{#struct_0_20343_19272_108460960}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1001211635}*[加入]{style="font-family:宋体"}[8:12::1]{lang="EN-US"}[，标志为]{style="font-family:宋体"}[SWR]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_x1712088892}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[IPv6 PIM Hello]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim neighbor receive]{lang="EN-US"}]{#struct_0_20343_19272_108526496}

[\* %Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Received Hello packet from neighbor FE80:7:12::1, incoming interface is Vlan-interface11. (PM073562)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1769818658}*[从接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[上收到源地址为]{style="font-family:宋体"}[FE80:7:12::1]{lang="EN-US"}[的]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Holdtime: 105 (PM073298)]{lang="EN-US"}]{#struct_0_20343_19272_108723104}

[%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Tbit: 0, Lan delay: 500, Override interval: 2500 (PM073340)]{lang="EN-US"}

[%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: DR priority: 1 (PM073365)]{lang="EN-US"}

[%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Genid: 0xDF424DC2 (PM073391)]{lang="EN-US"}

[%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Secondary address: 7:12::1 (PM073235)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_2024729683}*[保持时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒，]{style="font-family:宋体"}[T]{lang="EN-US"}[位没有设置，剪枝延迟时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒，剪枝否决时间为]{style="font-family:宋体"}[2500]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[DR]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0xDF424DC2]{lang="EN-US"}[，二级地址]{style="font-family:宋体"}[7:12::1]{lang="EN-US"}*

[[%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Received hello packet from neighbor FE80:7:12::1 and refreshed it. (PM072623)]{lang="EN-US"}]{#struct_0_20343_19272_x1123991381}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_107740064}*[从邻居]{style="font-family:宋体"}[FE80:7:12::1]{lang="EN-US"}[收到]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，并刷新]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_348730495}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[IPv6 PIM Hello]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim neighbor send]{lang="EN-US"}]{#struct_0_20343_19272_107805600}

[%Sep  7 16:59:13:914 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: PIM ver 2 Hello sending FE80:8:12::1 -\> FF02::D on GigabitEthernet1/0/1 (PM071570)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_496758953}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[PIMv2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，源地址为]{style="font-family:宋体"}[FE80:8:12::1]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[FF02::D]{lang="EN-US"}*

[[%Sep  7 16:59:13:917 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Holdtime: 105 s (PM071572)]{lang="EN-US"}]{#struct_0_20343_19272_108395425}

[%Sep  7 16:59:13:921 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Tbit: 0, Lan delay: 500 ms, Override interval: 2500 ms (PM071576)]{lang="EN-US"}

[%Sep  7 16:59:13:924 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: DR priority: 1 (PM071578)]{lang="EN-US"}

[%Sep  7 16:59:13:926 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Genid: 0xCEA8757C (PM071580)]{lang="EN-US"}

[%Sep  7 16:59:13:928 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Secondary Address: 8:12::1 (PM071303)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_699222204}*[保持时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒，]{style="font-family:宋体"}[T]{lang="EN-US"}[位没有设置，剪枝延迟时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒，剪枝否决时间为]{style="font-family:宋体"}[2500]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[DR]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0xCEA8757C]{lang="EN-US"}[，二级地址为]{style="font-family:宋体"}[8:12::1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_108460961}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[注册报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim register]{lang="EN-US"}]{#struct_0_20343_19272_108526497}

[%Sep  7 17:34:08:801 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: (7:11::8, FF1E::1) register state transited from NoInfo to Join due to CouldRegister(S,G) == True. Add reg tunnel. (SM06507)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1769818657}*[表项（]{style="font-family:宋体"}[7:11::8]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）注册状态机从]{style="font-family:宋体"}[NoInfo]{lang="EN-US"}[跃迁到]{style="font-family:宋体"}[Join]{lang="EN-US"}[，添加注册口]{style="font-family:宋体"}*

[[%Sep  7 17:34:08:804 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: Add register oif for (7:11::8, FF1E::1) (SM061560)]{lang="EN-US"}]{#struct_0_20343_19272_108592033}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1364555338}*[为表项（]{style="font-family:宋体"}[7:11::8]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）添加注册出接口]{style="font-family:宋体"}*

[[%Sep  7 17:34:08:838 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: (7:11::8, FF1E::1) register state transited from Join to Prune due to received RegStop. Remove reg tunnel, set RST to 48s. (SM06690)]{lang="EN-US"}]{#struct_0_20343_19272_108657569}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_409714143}*[收到注册停止报文，表项（]{style="font-family:宋体"}[7:11::8]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）状态从]{style="font-family:宋体"}[Jolin]{lang="EN-US"}[跃迁到]{style="font-family:宋体"}[Prune]{lang="EN-US"}[，删除注册口，设置注册停止定时器为]{style="font-family:宋体"}[48]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[%Sep  7 17:34:08:840 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: RST(48s) create successfully for (7:11::8, FF1E::1). (SM06384)]{lang="EN-US"}]{#struct_0_20343_19272_108723105}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_2024729682}*[成功为表项（]{style="font-family:宋体"}[7:11::8]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）创建注册停住定时器为]{style="font-family:宋体"}[48]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[%Sep  7 17:34:08:840 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: Delete register oif for (7:11::8, FF1E::1) (SM061655)]{lang="EN-US"}]{#struct_0_20343_19272_107740065}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_348730494}*[为表项（]{style="font-family:宋体"}[7:11::8]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）删除注册出接口]{style="font-family:宋体"}*

[[\*May  3 07:22:49:773 2013 Sysname PIM6/7/REG: -MDC=1; IPv6: Register packets of (7:11::123, FF1E::1) not forwarded because no active local RP exists. (SM06406)]{lang="EN-US"}]{#struct_0_20343_19272_x106789719}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_x1987769607}*[由于没有激活的本地]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[存在，不为（]{style="font-family:宋体"}[7:11::123]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）转发注册报文]{style="font-family:宋体"}*

[[\*May  3 07:22:49:773 2013 Sysname PIM6/7/REG: -MDC=1; IPv6: Register packets of (7:11::123, FF1E::1) not forwarded because the source address belongs to the Anycast-RP set. (SM061936)]{lang="EN-US"}]{#struct_0_20343_19272_x106855255}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1174616296}*[由于源地址在]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[集中，不为（]{style="font-family:宋体"}[7:11::123]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）转发注册报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_528826615}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[RP]{lang="EN-US"}[相关报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim rp receive]{lang="EN-US"}]{#struct_0_20343_19272_1674348297}

[%Sep  7 17:09:12:835 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Received a msg (C-BSR enable). (RP08321)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_x710700984}*[收到]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[使能的消息]{style="font-family:宋体"}*

[[%Sep  7 17:09:12:835 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Scope \'Global\' receive an event of \'Router changes to C-BSR\' at state \'Accept Any\'. (RP042440)]{lang="EN-US"}]{#struct_0_20343_19272_1674479369}

[%Sep  7 17:09:12:835 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Set BST of scope Global to 5. (RP041233)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_x1099425011}*[全局域收到在]{style="font-family:宋体"}[AA]{lang="EN-US"}[状态路由变成]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[事件，设置全局域的]{style="font-family:宋体"}[BST]{lang="EN-US"}[为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_1233001063}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[RP]{lang="EN-US"}[相关报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim rp send]{lang="EN-US"}]{#struct_0_20343_19272_1674544905}

[%%Sep  7 17:10:18:051 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Send out BSM packet to interface Vlan-interface11. (PM09430)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_x1132329265}*[向接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[发送]{style="font-family:宋体"}[BSM]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[%Sep  7 17:10:18:051 2011 Sysname PIM6/7/RP: -MDC=1; IPv6:  Nbit: 0, Fragment tag: 0x6732, Hash mask len: 126, BSR Priority: 64, BSR address: 8:12::1. (PM09430)]{lang="EN-US"}]{#struct_0_20343_19272_1674675977}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_435786384}*[报文]{style="font-family:宋体"}[B]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，分片标志]{style="font-family:宋体"}[0x6732]{lang="EN-US"}[，哈希长度]{style="font-family:宋体"}[126]{lang="EN-US"}[，优先级]{style="font-family:宋体"}[64]{lang="EN-US"}[，]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址]{style="font-family:宋体"}[8:12::1]{lang="EN-US"}*

[[%Sep  7 17:10:18:051 2011 Sysname PIM6/7/RP: -MDC=1; IPv6:  Group: FF00::/8, Bbit: 0, Zbit: 0, RP Count: 1, Frag RP Count: 1 (PM09436)]{lang="EN-US"}]{#struct_0_20343_19272_1673824009}

[%Sep  7 17:10:18:051 2011 Sysname PIM6/7/RP: -MDC=1; IPv6:   RP: 8:12::2 \-\-- Holdtime 180, Priority 192 (PM09440)]{lang="EN-US"}

[%Sep  7 17:10:18:052 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Set BST of scope Global to 60. (RP041233)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_x1429469590}*[组范围]{style="font-family:宋体"}[FF00::/8]{lang="EN-US"}[，]{style="font-family:宋体"}[B]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[Z]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[RP]{lang="EN-US"}[数量为]{style="font-family:宋体"}[1]{lang="EN-US"}[，分片中]{style="font-family:宋体"}[RP]{lang="EN-US"}[数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，组下]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[8:12::2,]{lang="EN-US"}[保持时间]{style="font-family:宋体"}[180S]{lang="EN-US"}[，优先级]{style="font-family:宋体"}[192]{lang="EN-US"}[，设置全局域的]{style="font-family:宋体"}[BST]{lang="EN-US"}[为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_188386431}[接口上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[组播路由表状态改变调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim routing-table]{lang="EN-US"}]{#struct_0_20343_19272_1674348298}

[%Sep  7 17:23:53:839 2011 Sysname PIM6/7/ROUTE: -MDC=1; IPv6: Creating (7:11::8, FF1E::1), flags: 0x00000000, down if protocol: 0 (SM134265)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_x711552952}*[创建表项（]{style="font-family:宋体"}[7:11::8]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[），标志为]{style="font-family:宋体"}[x00000000]{lang="EN-US"}[，下游接口协议号为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[%Sep  7 17:23:53:839 2011 Sysname PIM6/7/ROUTE: -MDC=1; IPv6: Claim the IIF route for (7:11::8, FF1E::1) (SM151621)]{lang="EN-US"}]{#struct_0_20343_19272_1674413834}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_1216129312}*[为表项（]{style="font-family:宋体"}[7:11::8]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）声明路由]{style="font-family:宋体"}*

[[%Sep  7 17:23:53:839 2011 Sysname PIM6/7/ROUTE: -MDC=1; IPv6: Add iif: Vlan-interface11 for (7:11::8, FF1E::1) (SM131961)]{lang="EN-US"}]{#struct_0_20343_19272_1674544906}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_x1132132657}*[为表项（]{style="font-family:宋体"}[7:11::8]{lang="EN-US"}[，]{style="font-family:宋体"}[FF1E::1]{lang="EN-US"}[）添加出接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_2018191856}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，并打开公网实例接收]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[状态刷新报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim state-refresh receive]{lang="EN-US"}]{#struct_0_20343_19272_1674610442}

[\*Mar 16 08:36:12:644 2012 Sysname PIM6/7/SRM: -MDC=1; IPv6: PIM ver 2 SRM receiving FE80:8:12::1 -\> FF02::D for (7:11::100, FF0E::1) on GigabitEthernet1/0/1, Originator address: FE80:7:11::1, preference: 0, metric: 0, mask length: 64, hoplimit: 255, prune indicator: unset, prune now: unset, assert override: set, interval: 60s (DM141415)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_781399232}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到状态刷新报文，报文的源地址是]{style="font-family:宋体"}[FE80:8:12::1]{lang="EN-US"}[，目的地址是]{style="font-family:宋体"}[FF02::D]{lang="EN-US"}[；组播组为]{style="font-family:宋体"}[FF0E::1/128]{lang="EN-US"}[；组播源为]{style="font-family:宋体"}[7:11::100]{lang="EN-US"}[；产生状态刷新报文设备的地址为]{style="font-family:宋体"}[FE80:7:11::1]{lang="EN-US"}[；优先级和]{style="font-family:宋体"}[Metric]{lang="EN-US"}[值都是]{style="font-family:宋体"}[0]{lang="EN-US"}[；掩码长度为]{style="font-family:宋体"}[64]{lang="EN-US"}[；]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}[为]{style="font-family:宋体"}[255]{lang="EN-US"}[，没有设置]{style="font-family:宋体"}[Prune Indicator]{lang="EN-US"}[和]{style="font-family:宋体"}[Prune Now]{lang="EN-US"}[标志位，设置了]{style="font-family:宋体"}[Assert Override]{lang="EN-US"}[标志位；发送间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20343_19272_1674675978}[在接口上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，并打开公网实例发送]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[状态刷新报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 pim state-refresh send]{lang="EN-US"}]{#struct_0_20343_19272_1674741514}

[\*Mar 16 08:36:12:645 2012 Sysname PIM6/7/SRM: -MDC=1; IPv6: PIM ver 2 SRM sending FE80:8:24::2 -\> FF02::D for (7:11::100, FF0E::1) on GigabitEthernet1/0/1, Originator address: FE80:7:11::1, preference: 10, metric: 2, mask length: 64, hoplimit: 254, prune indicator: unset, prune now: unset, assert override: set, interval: 60s. (DM09330)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20343_19272_402243593}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送状态刷新报文，报文的源地址是]{style="font-family:宋体"}[FE80:8:24::2]{lang="EN-US"}[，目的地址是]{style="font-family:宋体"}[FF02::D]{lang="EN-US"}[；组播组为]{style="font-family:宋体"}[FF0E::1/128]{lang="EN-US"}[；组播源为]{style="font-family:宋体"}[7:11::100]{lang="EN-US"}[；产生状态刷新报文设备的地址为]{style="font-family:宋体"}[FE80:7:11::1]{lang="EN-US"}[；优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[；]{style="font-family:宋体"}[Metric]{lang="EN-US"}[值为]{style="font-family:宋体"}[2]{lang="EN-US"}[；掩码长度都是]{style="font-family:宋体"}[64]{lang="EN-US"}[；]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}[为]{style="font-family:宋体"}[254]{lang="EN-US"}[，没有设置]{style="font-family:宋体"}[Prune Indicator]{lang="EN-US"}[和]{style="font-family:宋体"}[Prune Now]{lang="EN-US"}[标志位，设置了]{style="font-family:宋体"}[Assert Override]{lang="EN-US"}[标志位；发送间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*
