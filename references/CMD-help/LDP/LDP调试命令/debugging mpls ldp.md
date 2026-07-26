::: {#-1296451632 .myid}
[]{#_Toc404790512}[]{#struct_0_10226_54647_x1233930428}[]{#_Toc131060009}

**LDP \-- LDP调试命令 \-- debugging mpls ldp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_10226_54647_1288062661}

[**[debugging mpls ldp ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **process** \[ { **ipv4** \| **ipv6** } \[ **prefix-list** *prefix-list-name* \] \] \| **socket** \| **timer** }]{lang="EN-US"}]{#struct_0_10226_54647_953257538}

[**[undo debugging mpls ldp ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **process** ** **\[ { **ipv4** \| **ipv6** } \| **socket** \| **timer** } \] }]{lang="EN-US"}]{#struct_0_10226_54647_x2077103216}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10226_54647_169105329}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10226_54647_166853332}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_10226_54647_1137160443}

[[1]{lang="EN-US"}]{#struct_0_10226_54647_1084953856}[：监控级]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10226_54647_x1724186187}

[**[all]{lang="EN-US"}**]{#struct_0_10226_54647_722804444}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_10226_54647_1623803890}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_10226_54647_x1233733820}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_10226_54647_2058677153}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}[过程调试信息开关。如果指定参数]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}[，]{style="font-family:宋体"}**[则表示创建]{style="font-family:宋体"}[IPv4 LSP]{lang="EN-US"}[的过程调试信息开关；如果指定参数]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}[，]{style="font-family:宋体"}**[则表示创建]{style="font-family:宋体"}[IPv6 LSP]{lang="EN-US"}[的过程调试信息开关；如果不指定]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[参数，则打开所有]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[维护过程调试信息开关。]{style="font-family:宋体"}

[**[prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_10226_54647_1996548250}[：指定通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表对调试信息进行过滤。只有]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表过滤时，才会打开该]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[建立过程的调试信息开关。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[socket]{lang="EN-US"}**]{#struct_0_10226_54647_126333743}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[套接字调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_10226_54647_x2088008657}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_10226_54647_x1979301564}

[**[debugging mpls ldp]{lang="EN-US"}**]{#struct_0_10226_54647_x552023961}[命令用来打开]{style="font-family:宋体"}[LDP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls ldp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[LDP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1183355857}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mpls ldp error]{lang="EN-US"}]{#struct_0_10226_54647_2065743513}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_549295878}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_x1233799356}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_x216644672}

[[Failed to process a configuration command.]{lang="EN-US"}]{#struct_0_10226_54647_588227916}

[[处理配置命令失败]{style="font-family:宋体"}]{#struct_0_10226_54647_x1114294675}

[[Failed to create the timer.]{lang="EN-US"}]{#struct_0_10226_54647_1444527818}

[[创建定时器失败]{style="font-family:宋体"}]{#struct_0_10226_54647_1142291501}

[[Failed to reset the timer.]{lang="EN-US"}]{#struct_0_10226_54647_x1067927373}

[[重设定时器失败]{style="font-family:宋体"}]{#struct_0_10226_54647_x1233602748}

[[Unsupported label type.]{lang="EN-US"}]{#struct_0_10226_54647_x138587705}

[[不支持的标签类型]{style="font-family:宋体"}]{#struct_0_10226_54647_x1049197405}

[[Unsupported address family.]{lang="EN-US"}]{#struct_0_10226_54647_1687269302}

[[不支持的地址协议族]{style="font-family:宋体"}]{#struct_0_10226_54647_x1462548618}

[[Failed to allocate a label for *destination*.]{lang="EN-US"}]{#struct_0_10226_54647_x683297570}

[[为目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*]{#struct_0_10226_54647_x1233668284}[的]{style="font-family:宋体"}[FEC]{lang="EN-US"}[分配标签失败]{style="font-family:宋体"}

[[Failed to create a TCP socket.]{lang="EN-US"}]{#struct_0_10226_54647_x1735538040}

[[在]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1633485292}[会话的被动方上创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[套接字失败]{style="font-family:宋体"}

[[Failed to create a UDP socket.]{lang="EN-US"}]{#struct_0_10226_54647_x65548904}

[[创建]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_10226_54647_x1307893047}[套接字失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging mpls ldp event]{lang="EN-US"}]{#struct_0_10226_54647_x970464153}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_542943346}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_x1233471676}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_x1131016175}

[*[Module-A]{lang="EN-US"}*[ created a connection to *Module-B*.]{lang="EN-US"}]{#struct_0_10226_54647_2013232746}

[*[Module-A]{lang="EN-US"}*]{#struct_0_10226_54647_x1315041496}[模块与]{style="font-family:宋体"}*[Module-B]{lang="EN-US"}*[模块建立一个连接]{style="font-family:宋体"}

[[Received an HA upgrade event.]{lang="EN-US"}]{#struct_0_10226_54647_x1388991321}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_10226_54647_1245945963}[升级事件]{style="font-family:宋体"}

[[Received an HA degrade event.]{lang="EN-US"}]{#struct_0_10226_54647_888399072}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_10226_54647_x1233537212}[降级事件]{style="font-family:宋体"}

[[Received the interface *event* event. Interface index: *index*.]{lang="EN-US"}]{#struct_0_10226_54647_356057701}

[[收到接口变化事件，事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_10226_54647_42302442}[，接口的索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mpls ldp process]{lang="EN-US"}]{#struct_0_10226_54647_1656173137}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_542082450}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_x973158623}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_1270635810}

[[Refreshed the LSP (*lsp-destination*) to LSM.]{lang="EN-US"}]{#struct_0_10226_54647_2133430933}

[[向]{style="font-family:宋体"}[LSM]{lang="EN-US"}]{#struct_0_10226_54647_x1233340604}[下发一条]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[lsp-destination]{lang="EN-US"}*

[[Added an LSP establishment triggering policy on the egress (VPN instance: *vpn-name*).]{lang="EN-US"}]{#struct_0_10226_54647_2129682286}

[[在]{style="font-family:宋体"}[Egress]{lang="EN-US"}]{#struct_0_10226_54647_x1619128113}[上添加一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[触发策略。]{style="font-family:宋体"}

[[如果不显示]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_1052331948}[实例名称，则表示公网。下文与此相同，不再赘述]{style="font-family:宋体"}

[[Notified LSM to delete the LSP (*lsp-destination*).]{lang="EN-US"}]{#struct_0_10226_54647_x1464815467}

[[通知]{style="font-family:宋体"}[LSM]{lang="EN-US"}]{#struct_0_10226_54647_2090718196}[删除一条]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[lsp-destination]{lang="EN-US"}*

[[Process the label distribution control mode change event. VPN instance: *vpn-name*.]{lang="EN-US"}]{#struct_0_10226_54647_998025004}

[[处理标签分发控制方式改变事件，]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_x1233406140}[实例名称为]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging mpls ldp socket]{lang="EN-US"}]{#struct_0_10226_54647_x1035227927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_543184150}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_x1444936926}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_552179309}

[[Accepted a new socket (*socket-id*).]{lang="EN-US"}]{#struct_0_10226_54647_x964918966}

[[接收一个新的套接字，套接字的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_10226_54647_x115704629}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[Created a new socket (*socket-id*) on the passive LSR.]{lang="EN-US"}]{#struct_0_10226_54647_1045472558}

[[在]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1233864891}[会话的被动方上创建一个新的套接字，套接字的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[Closed the socket (*socket-id*) on the passive LSR.]{lang="EN-US"}]{#struct_0_10226_54647_537602143}

[[在]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1609322647}[会话的被动方上关闭套接字，套接字的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[Created a new socket (*socket-id*) on the active LSR.]{lang="EN-US"}]{#struct_0_10226_54647_2120580409}

[[在]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1818941566}[会话的主动方上创建一个新的套接字，套接字的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[Closed the socket (*socket-id*) on the active LSR.]{lang="EN-US"}]{#struct_0_10226_54647_x299342360}

[[在]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x2067317612}[会话的主动方上关闭套接字，套接字的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[Created a new UDP socket (*socket-id*).]{lang="EN-US"}]{#struct_0_10226_54647_x1233930427}

[[创建一个新的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_10226_54647_1241008494}[套接字，套接字的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging mpls ldp timer]{lang="EN-US"}]{#struct_0_10226_54647_x877008731}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_538924610}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_x1847632700}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_332132002}

[[Created the *timer-type* timer (size: *timer-size*).]{lang="EN-US"}]{#struct_0_10226_54647_x403756293}

[[创建一个类型为]{style="font-family:宋体"}*[timer-type]{lang="EN-US"}*]{#struct_0_10226_54647_x1233733819}[的定时器，定时器的值为]{style="font-family:宋体"}*[timer-size]{lang="EN-US"}*

[[Reset the *timer-type* timer (size: *timer-size*).]{lang="EN-US"}]{#struct_0_10226_54647_136428388}

[[重置类型为]{style="font-family:宋体"}*[timer-type]{lang="EN-US"}*]{#struct_0_10226_54647_1132507607}[的定时器，定时器的值为]{style="font-family:宋体"}*[timer-size]{lang="EN-US"}*

[[Deleted the *timer-type* timer.]{lang="EN-US"}]{#struct_0_10226_54647_555333287}

[[删除类型为]{style="font-family:宋体"}*[timer-type]{lang="EN-US"}*]{#struct_0_10226_54647_x1942738190}[的定时器]{style="font-family:宋体"}

[*[timer-type]{lang="DA"}*]{#struct_0_10226_54647_1492969090}[ timer expired.]{lang="DA"}

[[类型为]{style="font-family:宋体"}*[timer-type]{lang="EN-US"}*]{#struct_0_10226_54647_214253084}[的定时器超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10226_54647_x1233799355}

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_1349439269}[打开]{style="font-family:宋体"}[LDP]{lang="PT-BR"}[的错误调试信息开关。配置一个不存在对应]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[实例，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp error]{lang="EN-US"}]{#struct_0_10226_54647_x114926397}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls ldp]{lang="EN-US"}

[\[Sysname-ldp\] vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-ldp\]]{lang="EN-US"}

[\*Mar 14 17:20:25:520 2011 Sysname LDP/7/ERROR: -MDC=1; Failed to process a configuration command.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x87311295}*[处理配置命令失败。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_x1241126097}[打开]{style="font-family:宋体"}[LDP]{lang="PT-BR"}[的事件调试信息开关。将一个使能了]{style="font-family:宋体"}[MPLS LDP]{lang="EN-US"}[能力的接口]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp event]{lang="EN-US"}]{#struct_0_10226_54647_x411696189}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] shutdown]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]]{lang="EN-US"}

[\*Jun 23 15:54:30:088 2011 Sysname LDP/7/EVENT: -MDC=1; Received the interface down event. Interface index: 66794.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x1233602747}*[收到接口]{style="font-family:宋体"}[down]{lang="EN-US"}[事件。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_1877834930}[打开]{style="font-family:宋体"}[LDP]{lang="PT-BR"}[的套接字调试信息开关。配置]{style="font-family:宋体"}[MPLS LDP]{lang="EN-US"}[实例，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp socket]{lang="EN-US"}]{#struct_0_10226_54647_x782301588}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls ldp]{lang="EN-US"}

[\[Sysname-ldp\] vpn-instance vpn2]{lang="EN-US"}

[\[Sysname-ldp\]]{lang="EN-US"}

[\*Mar 14 19:07:21:584 2011 Sysname LDP/7/SOCKET: -MDC=1; Created a new socket (32) on the active LSR.]{lang="EN-US"}

[\*Mar 14 19:07:21:584 2011 Sysname LDP/7/SOCKET: -MDC=1; Created a new UDP socket (33).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1646967099}*[在]{style="font-family:宋体"}[LDP]{lang="EN-US"}[会话的主动方上创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[服务套接字，创建]{style="font-family:宋体"}[UDP]{lang="EN-US"}[套接字。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_x1482097746}[打开]{style="font-family:宋体"}[LDP]{lang="PT-BR"}[的定时器调试信息开关。在接口上使能]{style="font-family:宋体"}[MPLS LDP]{lang="EN-US"}[能力后，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp timer]{lang="DA"}]{#struct_0_10226_54647_x1233668283}

[\<Sysname\> system-view]{lang="DA"}

[\[Sysname\] mpls ldp]{lang="EN-US"}

[\[Sysname-ldp\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mpls enable ]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mpls ldp enable]{lang="EN-US"}

[\*Mar 14 18:49:45:839 2011 Sysname LDP/7/TIMER: -MDC=1; Created a hello interval timer (size: 5000).]{lang="EN-US"}

[\*Mar 14 18:49:45:842 2011 Sysname LDP/7/TIMER: -MDC=1; Created a hello hold timer (size: 15000).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x976023153}*[创建一个]{style="font-family:宋体"}[5000ms]{lang="EN-US"}[的]{style="font-family:宋体"}[hello interval]{lang="EN-US"}[定时器，创建一个]{style="font-family:宋体"}[15000ms]{lang="EN-US"}[的]{style="font-family:宋体"}[hello hold]{lang="EN-US"}[定时器。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_1777628721}[打开]{style="font-family:宋体"}[LDP]{lang="EN-US"}[创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}[过程调试信息开关。配置]{style="font-family:宋体"}[标签]{style="font-family:宋体"}[分发]{style="font-family:宋体"}[控制方式]{style="font-family:宋体"}[为独立方式后，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp process]{lang="EN-US"}]{#struct_0_10226_54647_1309708266}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls ldp]{lang="EN-US"}

[\[Sysname-ldp\] label-distribution independent]{lang="EN-US"}

[\*Mar 14 19:25:40:030 2011 Sysname LDP/7/PROCESS: -MDC=1; Process the label distribution control mode change event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_2026424423}*[处理标签分发控制方式改变事件。]{style="font-family:宋体"}*

[[在]{style="font-family:宋体"}[Egress]{lang="EN-US"}]{#struct_0_10226_54647_1991990791}[上配置一条掩码长度为]{style="font-family:宋体"}[32]{lang="EN-US"}[位的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由，]{style="font-family:宋体"}[在]{style="font-family:宋体"}[Ingress]{lang="PT-BR"}[上]{style="font-family:宋体"}[打印如下信息。]{style="font-family:宋体"}

[[\*Jan 6 18:25:09:172 2014 H3C LDP/7/PROCESS: -MDC=1; Refreshed the LSP (2.2.2.2/32) to LSM.]{lang="EN-US"}]{#struct_0_10226_54647_1991794183}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_93792944}*[向]{style="font-family:宋体"}[LSM]{lang="EN-US"}[下刷]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSP]{lang="EN-US"}[对应的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2/32]{lang="EN-US"}[）。]{style="font-family:宋体"}*

[[在]{style="font-family:宋体"}[Egress]{lang="EN-US"}]{#struct_0_10226_54647_x1050806112}[上配置一条掩码长度为]{style="font-family:宋体"}[128]{lang="EN-US"}[位的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由，]{style="font-family:宋体"}[在]{style="font-family:宋体"}[Ingress]{lang="PT-BR"}[上]{style="font-family:宋体"}[打印如下信息。]{style="font-family:宋体"}

[[\*Jan 6 18:28:41:768 2014 H3C LDP/7/PROCESS: -MDC=1; LSP refresh job (type: 8) for 200::22/128.  ]{lang="EN-US"}]{#struct_0_10226_54647_960571667}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x1640224033}*[向]{style="font-family:宋体"}[LSM]{lang="EN-US"}[下刷]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSP]{lang="EN-US"}[对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[200::22/128]{lang="EN-US"}[）。]{style="font-family:宋体"}*

::: {#1667590062 .myid}
[]{#_Toc404790513}[]{#struct_0_10226_54647_x1589619335}

**LDP \-- LDP调试命令 \-- debugging mpls ldp peer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_10226_54647_x1372634732}

[**[debugging mpls ldp ]{lang="EN-US"}**[{ **advertisement  **\[ { **ipv4** \| **ipv6** } \[ **prefix-list** *prefix-list-name* \] \] **\| discovery** \[ **ipv4** \| **ipv6** \] \| **notification** \| **packet** { **received** \| **sent** } \| **session** } \[ **peer** *peer-prefix-list-name* \]]{lang="EN-US"}]{#struct_0_10226_54647_327380827}

[**[undo debugging mpls ldp ]{lang="EN-US"}**[{ **advertisement** \[ **ipv4** \| **ipv6** \] **\| discovery** \[ **ipv4** \| **ipv6** \] \| **notification** \| **packet** { **received** \| **sent** } \| **session** }]{lang="EN-US"}]{#struct_0_10226_54647_x1233471675}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10226_54647_x1534300702}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10226_54647_1725881193}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_10226_54647_261531515}

[[1]{lang="EN-US"}]{#struct_0_10226_54647_x1093052978}[：监控级]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10226_54647_243943434}

[**[advertisement]{lang="EN-US"}**]{#struct_0_10226_54647_x1911081298}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[标签通告和地址通告调试信息开关。如果指定参数]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}[，]{style="font-family:宋体"}**[则表示]{style="font-family:宋体"}[IPv4 LDP]{lang="EN-US"}[标签通告和地址通告调试信息开关；如果指定参数]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}[，]{style="font-family:宋体"}**[则表示]{style="font-family:宋体"}[IPv6 LDP]{lang="EN-US"}[标签通告和地址通告调试信息开关；如果不指定]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[参数，则表示打开所有]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的通告调试信息开关。]{style="font-family:宋体"}

[**[prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_10226_54647_x208762287}[：指定通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表对调试信息进行过滤。只有]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表过滤时，才会打开该]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应标签通告和地址通告的调试信息开关。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[discovery]{lang="EN-US"}**]{#struct_0_10226_54647_x836695977}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[发现过程调试信息开关。如果指定参数]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}[，]{style="font-family:宋体"}**[则表示]{style="font-family:宋体"}[IPv4 LDP]{lang="EN-US"}[发现过程调试信息开关；如果指定参数]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}[，]{style="font-family:宋体"}**[则表示]{style="font-family:宋体"}[IPv6 LDP]{lang="EN-US"}[发现过程调试信息开关；如果不指定]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[参数，则打开所有发现过程调试信息开关。]{style="font-family:宋体"}

[**[notification]{lang="EN-US"}**]{#struct_0_10226_54647_x1233537211}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通知消息调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_10226_54647_x47226826}[：表示除]{style="font-family:宋体"}[Hello]{lang="EN-US"}[消息以外其他所有]{style="font-family:宋体"}[LDP]{lang="EN-US"}[消息的调试信息开关。]{style="font-family:宋体"}

[**[received]{lang="EN-US"}**]{#struct_0_10226_54647_x78881537}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[接收消息调试信息开关。]{style="font-family:宋体"}

[**[sent]{lang="EN-US"}**]{#struct_0_10226_54647_1187744883}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[发送消息调试信息开关。]{style="font-family:宋体"}

[**[session]{lang="EN-US"}**]{#struct_0_10226_54647_x1357362827}[：表示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[会话调试信息开关。]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}***[peer-prefix-list-name]{lang="EN-US"}*]{#struct_0_10226_54647_388295287}[：表示指定对等体的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[调试信息开关。只有对等体通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀过滤时，才会打开该对等体相关的调试信息开关。]{style="font-family:宋体"}*[peer-prefix-list-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则打开所有对等体相关]{style="font-family:宋体"}[的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_10226_54647_76514458}

[**[debugging mpls ldp peer]{lang="EN-US"}**]{#struct_0_10226_54647_x1726165629}[命令用来打开]{style="font-family:宋体"}[LDP]{lang="EN-US"}[对等体的调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls ldp peer]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[LDP]{lang="EN-US"}[对等体的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_379901705}[对等体的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging mpls ldp advertisement]{lang="EN-US"}]{#struct_0_10226_54647_x1233340603}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_540650614}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_207367985}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_629870426}

[[Loop detected by hop count (hop count: *hops*, max hop count: *max-hops*).]{lang="EN-US"}]{#struct_0_10226_54647_x2078405493}

[[发现环路：]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_10226_54647_1190174483}[经过的跳数]{style="font-family:宋体"}*[hops]{lang="EN-US"}*[超过允许的最大跳数]{style="font-family:宋体"}*[max-hops]{lang="EN-US"}*

[[Received a label mapping message from peer (*peer-ldp-id*, VPN instance: *vpn-name*).]{lang="EN-US"}]{#struct_0_10226_54647_x1233406139}

[[从]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_887282982}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[收到标签映射消息]{style="font-family:宋体"}

[[The label mapping message from peer (*peer-ldp-id*: *space-id*) has *fec-destination/mask-length*, label (*label*)]{lang="EN-US"}]{#struct_0_10226_54647_1992056326}

[[来自对端]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*]{#struct_0_10226_54647_x844611099}[的标签映射消息，]{style="font-family:宋体"}[FEC]{lang="EN-US"}[为]{style="font-family:宋体"}*[fec-destination]{lang="EN-US"}[，]{style="font-family:宋体"}*[掩码长度为]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[，标签为]{style="font-family:宋体"}*[label]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging mpls ldp discovery]{lang="EN-US"}]{#struct_0_10226_54647_354104867}[命令信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_539655114}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_x841949146}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_908864290}

[[Created an adjacency (index *index*, source address *source-ip*, transport address *transport-ip*, destination address *destination-ip*) for peer (*peer-ldp-id*, VPN instance: *vpn-name*).]{lang="EN-US"}]{#struct_0_10226_54647_1808640930}

[[创建一个]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_10226_54647_917906341}[邻接体，邻接体索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[，传输地址为]{style="font-family:宋体"}*[transport-ip]{lang="EN-US"}[，]{style="font-family:宋体"}*[目的地址为]{style="font-family:宋体"}*[destination-ip]{lang="EN-US"}*[，对端]{style="font-family:宋体"}[LDP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*

[[Deleted an adjacency (index *index*, source address *source-ip*, transport address *transport-ip*, destination address *destination-ip*) for peer (*peer-ldp-id*, VPN instance: *vpn-name*).]{lang="EN-US"}]{#struct_0_10226_54647_x1233864894}

[[删除一个邻接体，邻接体索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_10226_54647_940886670}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[，传输地址为]{style="font-family:宋体"}*[transport-ip]{lang="EN-US"}[，]{style="font-family:宋体"}*[目的地址为]{style="font-family:宋体"}*[destination-ip]{lang="EN-US"}*[，对端]{style="font-family:宋体"}[LDP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*

[[Discovered a new peer (*peer-ldp-id*, VPN instance: *vpn-name*).]{lang="EN-US"}]{#struct_0_10226_54647_x1368839248}

[[在]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_1420276968}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内发现一个]{style="font-family:宋体"}[LDP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[的对端]{style="font-family:宋体"}

[[The peer (*peer-ldp-id*, VPN instance: *vpn-name*) is lost.]{lang="EN-US"}]{#struct_0_10226_54647_x1464972562}

[[与]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_1767184556}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内]{style="font-family:宋体"}[LDP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[的对端失去连接，删除该]{style="font-family:宋体"}[hello]{lang="EN-US"}[邻接体]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging mpls ldp notification]{lang="EN-US"}]{#struct_0_10226_54647_x1233930430}[命令描述表]{style="font-family:黑体"}

[]{#table_struct_0_567987022}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_1644227485}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_x993592056}

[[Received a notification message (*event*) from peer (*peer-ldp-id*, VPN instance: *vpn-name*).]{lang="EN-US"}]{#struct_0_10226_54647_x787858219}

[[从]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_x2088918890}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[收到]{style="font-family:宋体"}[Notification]{lang="EN-US"}[消息，通知的事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Sent a notification message (*event*) to peer (*peer-ldp-id*, VPN instance: *vpn-name*).]{lang="EN-US"}]{#struct_0_10226_54647_307154394}

[[向]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_x455368319}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Notification]{lang="EN-US"}[消息，通知的事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging mpls ldp packet]{lang="EN-US"}]{#struct_0_10226_54647_x1233733822}[命令描述表]{style="font-family:黑体"}

[]{#table_struct_0_566852902}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_895877739}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_1911623249}

[[Received a keepalive message from peer ([*peer-ldp-id*]{.TableTextChar}, VPN instance: *vpn-name*)[.]{.TableTextChar} message content: *content*]{lang="EN-US"}]{#struct_0_10226_54647_x1676237042}

[[收到]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_x1079732979}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[发送的]{style="font-family:宋体"}[Keepalive ]{lang="EN-US"}[消息，消息内容为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[[Sent a keepalive message to peer (]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10226_54647_x229219682}[*[peer-ldp-id]{lang="EN-US" style="font-size:9.0pt"}*]{.TableTextChar}[, VPN instance: *vpn-name*)]{lang="EN-US" style="font-size:9.0pt"}[. message content: ]{lang="EN-US" style="font-size:9.0pt"}[*[content]{lang="EN-US" style="font-size:9.0pt"}*]{.TableTextChar}

[[向]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_x379446751}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Keepalive ]{lang="EN-US"}[消息，消息内容为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging mpls ldp session]{lang="EN-US"}]{#struct_0_10226_54647_x1233799358}[命令描述表]{style="font-family:黑体"}

[]{#table_struct_0_569880350}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_946154742}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_269263244}

[[Stopped the socket (*socket-id*) to the peer ([*peer-ldp-id*]{.TableTextChar}, VPN instance: *vpn-name*). MD5 check is needed for the socket.]{lang="EN-US"}]{#struct_0_10226_54647_1228170043}

[[关闭到]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_424752069}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}[*[peer-ldp-id]{lang="EN-US"}*]{.TableTextChar}[的套接字，套接字的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*[，该套接字需要进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}[检查]{style="font-family:宋体"}

[[Started the socket (*socket-id*) to the peer ([*peer-ldp-id*]{.TableTextChar}, VPN instance: *vpn-name*). MD5 check is needed for the socket.]{lang="EN-US"}]{#struct_0_10226_54647_x811323667}

[[打开到]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_2054911089}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}[*[peer-ldp-id]{lang="EN-US"}*]{.TableTextChar}[的套接字，套接字的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*[，该套接字需要进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}[检查]{style="font-family:宋体"}

[[Created a new session (*peer-ldp-id*, VPN instance: *vpn-name*). Local transport address: *local-address*, peer transport address: *peer-address*.]{lang="EN-US"}]{#struct_0_10226_54647_x1233602750}

[[创建一个会话，对端]{style="font-family:宋体"}[LDP ID]{lang="EN-US"}]{#struct_0_10226_54647_x494752529}[为]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[，本端传输地址为]{style="font-family:宋体"}*[local-address]{lang="EN-US"}*[，对端传输地址为]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*

[[Deleted the session (*peer-ldp-id*, VPN instance: *vpn-name*).]{lang="EN-US"}]{#struct_0_10226_54647_1214528788}

[[删除与]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_x62609054}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[的会话]{style="font-family:宋体"}

[[MD5 check of the session (*peer-ldp-id*, VPN instance: *vpn-name*) failed.]{lang="EN-US"}]{#struct_0_10226_54647_x1662582673}

[[与]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_10226_54647_1350982817}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[内的对端]{style="font-family:宋体"}*[peer-ldp-id]{lang="EN-US"}*[的会话进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10226_54647_1427323573}

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_x1233668286}[打开]{style="font-family:宋体"}[LDP IPv4]{lang="EN-US"}[发现过程调试信息开关。在]{style="font-family:宋体"}[接口上使能]{style="font-family:宋体"}[MPLS LDP]{lang="PT-BR"}[支持]{style="font-family:宋体"}[IPv4]{lang="PT-BR"}[能力后]{style="font-family:宋体"}[，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp discovery ipv4]{lang="EN-US"}]{#struct_0_10226_54647_x572738626}

[\<Sysname\> system-view]{lang="DA"}

[\[Sysname\] mpls ldp]{lang="EN-US"}

[\[Sysname-ldp\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mpls enable ]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mpls ldp enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]]{lang="EN-US"}

[\*Jan 6 14:26:32:105 2014 H3C LDP/7/DISCOVERY: -MDC=1; Created an adjacency (index 4, source address 77.99.99.99, transport address 99.99.3.3, destination address 224.0.0.2) for peer (99.99.3.3:0).]{lang="EN-US"}

[\*Jan 6 14:26:32:105 2014 H3C LDP/7/DISCOVERY: -MDC=1; Discovered a new peer (99.99.3.3:0).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x1056940601}*[创建一个与对端]{style="font-family:宋体"}[99.99.3.3]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[邻接体，邻接体的索引为]{style="font-family:宋体"}[4]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[77.99.99.99]{lang="EN-US"}[，传输地址为]{style="font-family:宋体"}[99.99.3.3]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[224.0.0.2]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_1992121857}[打开]{style="font-family:宋体"}[LDP IPv6]{lang="EN-US"}[发现过程调试信息开关。在]{style="font-family:宋体"}[接口上使能]{style="font-family:宋体"}[MPLS LDP]{lang="PT-BR"}[支持]{style="font-family:宋体"}[Ipv6]{lang="PT-BR"}[能力后]{style="font-family:宋体"}[，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp discovery ipv6]{lang="EN-US"}]{#struct_0_10226_54647_x387783688}

[\<Sysname\> system-view]{lang="DA"}

[\[Sysname\] mpls ldp]{lang="EN-US"}

[\[Sysname-ldp\] quit]{lang="EN-US"}

[\[Sysname\] interface ethernet 1/1]{lang="EN-US"}

[\[Sysname-Ethernet1/1\] mpls enable ]{lang="EN-US"}

[\[Sysname-Ethernet1/1\] mpls ldp ipv6 enable]{lang="EN-US"}

[\[Sysname-Ethernet1/1\]]{lang="EN-US"}

[\*Jan 6 16:02:15:092 2014 H3C LDP/7/DISCOVERY: -MDC=1; Created an adjacency (index 5, source address FE80::20C:29FF:FEB3:BC0A, transport address 2001::2, destination address FF02::2) for peer (99.99.3.3:0).]{lang="EN-US"}

[\*Jan 6 16:02:15:093 2014 H3C LDP/7/DISCOVERY: -MDC=1; Discovered a new peer (99.99.3.3:0).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1991925249}*[创建一个与对端]{style="font-family:宋体"}[99.99.3.3]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[邻接体，邻接体的索引为]{style="font-family:宋体"}[5]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80::20C:29FF:FEB3:BC0A]{lang="EN-US"}[，传输地址为]{style="font-family:宋体"}[2001::2]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[FF02::2]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_789555193}[打开]{style="font-family:宋体"}[LDP]{lang="EN-US"}[标签通告和地址通告调试信息开关。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[Egress]{lang="EN-US"}]{#struct_0_10226_54647_71415131}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[触发策略为所有路由项都会触发]{style="font-family:宋体"}[LDP]{lang="EN-US"}[建立]{style="font-family:宋体"}[LSP]{lang="EN-US"}[后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp advertisement ipv4]{lang="EN-US"}]{#struct_0_10226_54647_x1233471678}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls ldp]{lang="EN-US"}

[\[]{lang="PT-BR"}[Sysname]{lang="EN-US"}[-ldp\] lsp-trigger all]{lang="PT-BR"}

[\*Jan 6 16:59:12:910 2014 H3C LDP/7/ADVERTISEMENT: -MDC=1; Received a label mapping message from peer (99.99.3.3:0).]{lang="EN-US"}

[\*Jan 6 16:59:12:910 2014 H3C LDP/7/ADVERTISEMENT: -MDC=1; The label mapping message from peer (99.99.3.3:0) has 20.1.1.2/32, label (3)]{lang="EN-US"}[.]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_10226_54647_x1581354869}*[接收到对端]{style="font-family:宋体"}[99.99.3.3]{lang="PT-BR"}[为]{style="font-family:宋体"}[IPv4]{lang="PT-BR"}[前缀路由]{style="font-family:宋体"}[20.1.1.2]{lang="PT-BR"}[发送的]{style="font-family:宋体"}[mapping]{lang="PT-BR"}[消息]{style="font-family:宋体"}*

[[在]{style="font-family:宋体"}]{#struct_0_10226_54647_1991663105}[Egress]{lang="PT-BR"}[上]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[触发策略为所有]{style="font-family:宋体"}[IPv6]{lang="PT-BR"}[路由项触发]{style="font-family:宋体"}[LDP]{lang="PT-BR"}[建立]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[后]{style="font-family:宋体"}[，在]{style="font-family:宋体"}[Ingress]{lang="PT-BR"}[上]{style="font-family:宋体"}[打印如下信息]{style="font-family:宋体"}[:]{lang="PT-BR"}

[[\<Sysname\> debugging mpls ldp advertisement ipv6]{lang="EN-US"}]{#struct_0_10226_54647_1991728641}

[[\*Jan 6 17:22:19:937 2014 H3C LDP/7/ADVERTISEMENT: -MDC=1; Received a label mapping message from peer (99.99.3.3:0).]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x646728840}

[[\*Jan 6 17:22:19:937 2014 H3C LDP/7/ADVERTISEMENT: -MDC=1; The label mapping message from peer (99.99.3.3:0) has 200::24/128, label (3).]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x1903774132}

[*[// ]{lang="PT-BR"}*]{#struct_0_10226_54647_1992580609}*[接收到对端]{style="font-family:宋体"}[99.99.3.3]{lang="PT-BR"}[为]{style="font-family:宋体"}[IPv6]{lang="PT-BR"}[前缀路由]{style="font-family:宋体"}[200::24]{lang="PT-BR"}[发送的]{style="font-family:宋体"}[mapping]{lang="PT-BR"}[消息]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_x1034554587}[打开]{style="font-family:宋体"}[LDP]{lang="PT-BR"}[通知消息调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}[hello]{lang="PT-BR"}[定时器超时如果仍未收到]{style="font-family:宋体"}[hello]{lang="PT-BR"}[消息]{style="font-family:宋体"}[，则]{style="font-family:宋体"}[打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp notification]{lang="EN-US"}]{#struct_0_10226_54647_1158957838}

[\<Sysname\>]{lang="EN-US"}

[\*Mar 16 09:56:21:076 2011 ]{lang="PT-BR"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[LDP/7/NOTIFICATION: -MDC=1; Sent a notification message (hold timer expired) to peer (100.100.100.6:0).]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_10226_54647_978056108}*[发送]{style="font-family:宋体"}[hello hold]{lang="PT-BR"}[定时器超时的]{style="font-family:宋体"}[notification]{lang="PT-BR"}[消息。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_x211416695}[打开]{style="font-family:宋体"}[LDP]{lang="PT-BR"}[接收消息调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}[收到]{style="font-family:宋体"}[keepalive]{lang="PT-BR"}[消息后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp packet received]{lang="EN-US"}]{#struct_0_10226_54647_x1233537214}

[\<Sysname\>]{lang="EN-US"}

[\*Mar 16 10:02:32:030 2011 ]{lang="PT-BR"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[LDP/7/PACKET RECEIVE: -MDC=1; Received a keepalive message from peer 100.100.100.6:0. message content:]{lang="PT-BR"}

[ 02 01 00 04 00 00 0d 67]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_10226_54647_x450511353}*[收到]{style="font-family:宋体"}[keepalive]{lang="PT-BR"}[消息]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_x866026028}[打开]{style="font-family:宋体"}[LDP]{lang="EN-US"}[发送消息调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[keepalive]{lang="PT-BR"}[消息后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp packet sent]{lang="EN-US"}]{#struct_0_10226_54647_x904012796}

[\<Sysname\>]{lang="EN-US"}

[\*Mar 16 10:06:01:976 2011 ]{lang="PT-BR"}[Sysname]{lang="EN-US"}[ ]{lang="EN-US"}[LDP/7/PACKET SEND: -MDC=1; Sent a keepalive message to peer 100.100.100.6:0. message content:]{lang="PT-BR"}

[ 02 01 00 04 00 00 00 ae]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_10226_54647_1836386111}*[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_10226_54647_x1326896119}[打开]{style="font-family:宋体"}[LDP]{lang="EN-US"}[会话调试信息开关]{style="font-family:宋体"}[。重启]{style="font-family:宋体"}[MPLS LDP]{lang="PT-BR"}[会话后，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls ldp session]{lang="EN-US"}]{#struct_0_10226_54647_x1752761521}

[\<Sysname\> ]{lang="EN-US"}[reset mpls ldp]{lang="PT-BR"}

[\<Sysname\>]{lang="EN-US"}[ ]{lang="EN-US"}

[\*Mar 15 16:27:01:686 2011 Sysname LDP/7/SESSION: -MDC=1; Deleted the session (100.100.100.6:0).]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_10226_54647_1666628779}*[删除会话。]{style="font-family:宋体"}*

[[\*Mar 15 16:27:03:997 2011 Sysname LDP/7/SESSION: -MDC=1; Created a new session (100.100.100.6:0): Local transport (100.100.100.66), peer transport (100.100.100.6). ]{lang="PT-BR"}]{#struct_0_10226_54647_x1233340606}

[*[// ]{lang="PT-BR"}*]{#struct_0_10226_54647_966882872}*[创建新会话。]{style="font-family:宋体"}*

::: {#-716408296 .myid}
[]{#_Toc404790514}[]{#struct_0_10226_54647_x504329395}[]{#_Toc358904298}[]{#_Toc355273095}[]{#_Toc350865778}[]{#_Toc345666324}

**LDP \-- LDP调试命令 \-- debugging isis mpls ldp sync**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_10226_54647_245959306}

[**[debugging isis mpls ldp sync ]{lang="EN-US"}**[\[ **event** \| **fsm** \| **query** \] ]{lang="EN-US"}]{#struct_0_10226_54647_x1816151324}

[**[undo debugging isis mpls ldp sync]{lang="EN-US"}**[ \[ **event** \| **fsm** \| **query** \]]{lang="EN-US"}]{#struct_0_10226_54647_x504394931}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10226_54647_x1686846583}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10226_54647_1361087765}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10226_54647_x1776581617}

[[network-admin]{lang="EN-US"}]{#struct_0_10226_54647_x503936179}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10226_54647_x1166353671}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10226_54647_x668938407}

[**[event]{lang="EN-US"}**]{#struct_0_10226_54647_x1537377072}[：表示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[收到的]{style="font-family:宋体"}[LDP-IGP]{lang="EN-US"}[同步]{style="font-family:宋体"}[事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_10226_54647_x504001715}[：表示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[LDP-IGP]{lang="EN-US"}[同步状态机调试开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[query]{lang="EN-US"}**]{#struct_0_10226_54647_649553177}[：表示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[向]{style="font-family:宋体"}[LDP]{lang="EN-US"}[进程发送消息队列的]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_10226_54647_420988353}

[**[debugging isis mpls ldp sync]{lang="EN-US"}**]{#struct_0_10226_54647_x60450589}[命令用来打开]{style="font-family:
宋体"}[LDP IS-IS]{lang="EN-US"}[同步]{style="font-family:
宋体"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging isis mpls ldp sync]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[LDP IS-IS]{lang="EN-US"}[同步]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_10226_54647_x504067251}[LDP IS-IS]{lang="EN-US"}[同步]{style="font-family:宋体"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定任何参数，则表示所有]{style="font-family:宋体"}]{#struct_0_10226_54647_x1277735349}[LDP IS-IS]{lang="EN-US"}[同步]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[表1-11 ]{lang="EN-US"}[debugging isis mpls ldp sync event]{lang="EN-US"}]{#struct_0_10226_54647_x1831254200}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x44674917}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_1416137341}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_x504132787}

[[ISIS-LDP-SYNC]{lang="EN-US"}]{#struct_0_10226_54647_1050544032}

[[LDP IS-IS]{lang="EN-US"}]{#struct_0_10226_54647_x503674035}[同步]{style="font-family:宋体"}[调试信息]{style="font-family:宋体"}

[[Subscribe LDP global famous port successfully.]{lang="EN-US"}]{#struct_0_10226_54647_x1951480818}

[[订阅]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x503739571}[端口成功]{style="font-family:宋体"}

[[Subscribe LDP global famous port failed.]{lang="EN-US"}]{#struct_0_10226_54647_1520110328}

[[订阅]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_627454914}[端口失败]{style="font-family:宋体"}

[[Unsubscribe LDP global famous port successfully.]{lang="EN-US"}]{#struct_0_10226_54647_x504198322}

[[注销]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1785959864}[端口成功]{style="font-family:宋体"}

[[LDP port state change to up.]{lang="EN-US"}]{#struct_0_10226_54647_x504263858}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x455967711}[端口状态变为]{style="font-family:宋体"}[up]{lang="EN-US"}

[[LDP port state change to down.]{lang="EN-US"}]{#struct_0_10226_54647_x504329394}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_245893770}[端口状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}

[[IS-IS connect LDP daemon successfully.]{lang="EN-US"}]{#struct_0_10226_54647_573826826}

[[ISIS]{lang="EN-US"}]{#struct_0_10226_54647_x504394930}[与]{style="font-family:宋体"}[LDP]{lang="EN-US"}[进程连接成功]{style="font-family:宋体"}

[[IS-IS disconnect from LDP daemon.]{lang="EN-US"}]{#struct_0_10226_54647_x1686781047}

[[ISIS]{lang="EN-US"}]{#struct_0_10226_54647_x503936178}[与]{style="font-family:宋体"}[LDP]{lang="EN-US"}[进程断开]{style="font-family:宋体"}

[[Receive LDP if-state message: *interfaceName*, ifIndex: *ifIndex*, ldpstate: ldp*State*, vrfIndex: *vrfIndex*.]{lang="EN-US"}]{#struct_0_10226_54647_x1166288135}

[[接收到]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x504001714}[接口状态信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interfaceName]{lang="EN-US"}*[,]{lang="EN-US"}]{#struct_0_10226_54647_649487641}[：接口名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ifIndex]{lang="EN-US"}*]{#struct_0_10226_54647_x504067250}[：接口索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ldpState]{lang="EN-US"}*]{#struct_0_10226_54647_x1277800885}[：]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vrfIndex]{lang="EN-US"}*]{#struct_0_10226_54647_x504132786}[：]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例索引]{lang="EN-US" style="font-family:宋体"}

[[Receive LDP if-state message: ifIndex(inactive): *ifIndex*, ldpstate: ldp*State*, vrfIndex: *vrfIndex*.]{lang="EN-US"}]{#struct_0_10226_54647_1050609568}

[[接收到没有接口索引的]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x503674034}[接口状态信息]{style="font-family:宋体"}

[[Receive LDP push-finish message.]{lang="EN-US"}]{#struct_0_10226_54647_x1951415282}

[[接收到]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1408467451}[平滑结束消息]{style="font-family:宋体"}

[[Receive LDP disable message.]{lang="EN-US"}]{#struct_0_10226_54647_x503739570}

[[接收到]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1520175864}[去使能消息]{style="font-family:宋体"}

[[Receive LDP unknown message.]{lang="EN-US"}]{#struct_0_10226_54647_x504198325}

[[接收到未知的]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1785501112}[消息]{style="font-family:宋体"}

[[Parse LDP message failed.]{lang="EN-US"}]{#struct_0_10226_54647_x504263861}

[[解析]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x455377890}[信息失败]{style="font-family:宋体"}

[[LDP waiting timer expired.]{lang="EN-US"}]{#struct_0_10226_54647_x504329397}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_246090378}[等待时间超时]{style="font-family:宋体"}

[[Create LDP waiting timer.]{lang="EN-US"}]{#struct_0_10226_54647_x504394933}

[[创建]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1686715511}[等待定时器]{style="font-family:宋体"}

[[Delete LDP waiting timer.]{lang="EN-US"}]{#struct_0_10226_54647_x503936181}

[[删除]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1166877948}[等待定时器]{style="font-family:宋体"}

[[LDP break the connection.]{lang="EN-US"}]{#struct_0_10226_54647_x504001717}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_649422105}[断开连接]{style="font-family:宋体"}

[[LDP send buffer is free.]{lang="EN-US"}]{#struct_0_10226_54647_x504067253}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1277604277}[发送缓冲区为空]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging isis mpls ldp sync fsm]{lang="EN-US"}]{#struct_0_10226_54647_623006278}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x258001522}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_x504132789}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_1051461536}

[[ISIS-LDP-SYNC]{lang="EN-US"}]{#struct_0_10226_54647_x503674037}

[[LDP IS-IS]{lang="EN-US"}]{#struct_0_10226_54647_x1951611890}[同步]{style="font-family:宋体"}[调试信息]{style="font-family:宋体"}

[[Circuit(*interfaceName*) received event(ldp*Event*), LDP_SYNC state changed from *ldpSyncState1* to *ldpSyncState2*.]{lang="EN-US"}]{#struct_0_10226_54647_x1184797909}

[[接口]{style="font-family:宋体"}*[interfaceName]{lang="EN-US"}*]{#struct_0_10226_54647_x503739573}[收到事件]{style="font-family:宋体"}[ldp*Event*]{lang="EN-US"}[后，触发]{style="font-family:宋体"}[LDP]{lang="EN-US"}[同步状态机变化，接口的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[同步状态由]{style="font-family:宋体"}*[ldpSyncState1]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[ldpSyncState2]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging isis mpls ldp sync query]{lang="EN-US"}]{#struct_0_10226_54647_1519979256}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x266653478}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_465122365}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_x504198324}

[[ISIS-LDP-SYNC]{lang="EN-US"}]{#struct_0_10226_54647_1785566648}

[[LDP IS-IS]{lang="EN-US"}]{#struct_0_10226_54647_x504263860}[同步]{style="font-family:宋体"}[调试信息]{style="font-family:宋体"}

[[Send LDP *msgType* message *resultState*: *interfaceName*, ifIndex: *ifIndex*.]{lang="EN-US"}]{#struct_0_10226_54647_x455443426}

[[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1890282310}[信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msgType]{lang="EN-US"}*]{#struct_0_10226_54647_x504329396}*[：]{style="font-family:宋体"}*[信息类型，取值为注册或注销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[resultState]{lang="EN-US"}*]{#struct_0_10226_54647_246024842}[：结果状态，]{lang="EN-US" style="font-family:
  宋体"}[取值为]{style="font-family:宋体"}[成功或失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interfaceName]{lang="EN-US"}*]{#struct_0_10226_54647_1501667887}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ifIndex]{lang="EN-US"}*]{#struct_0_10226_54647_x504394932}[：接口索引]{lang="EN-US" style="font-family:宋体"}

[[Resend LDP *msgType* message *resultState*: *interfaceName*, ifIndex: *ifIndex*.]{lang="EN-US"}]{#struct_0_10226_54647_x1686649975}

[[重新发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x503936180}[信息]{style="font-family:宋体"}

[[Send LDP smooth *msgType* message *resultState*.]{lang="EN-US"}]{#struct_0_10226_54647_x1166812412}

[[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x504001716}[平滑信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msgType]{lang="EN-US"}*]{#struct_0_10226_54647_649356569}[：信息类型，取值为平滑开始或结束]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[resultState]{lang="EN-US"}*]{#struct_0_10226_54647_x235694037}[：结果状态，]{lang="EN-US" style="font-family:
  宋体"}[取值为]{style="font-family:宋体"}[成功或失败]{lang="EN-US" style="font-family:宋体"}

[[Resend LDP smooth *msgType* message *resultState*.]{lang="EN-US"}]{#struct_0_10226_54647_x504067252}

[[重新发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1277669813}[平滑信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10226_54647_x924082818}

[[\# ]{lang="EN-US"}]{#struct_0_10226_54647_x504132788}[在设备上打开所有]{style="font-family:宋体"}[LDP IS-IS]{lang="EN-US"}[同步调试信息开关后，在设备上配置]{style="font-family:宋体"}[LDP IS-IS]{lang="EN-US"}[同步功能，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging isis mpls ldp sync]{lang="EN-US"}]{#struct_0_10226_54647_1051527072}

[[\*Jun 25 14:15:57:736 2013 Sysname ISIS/7/ISISDBG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x948636628}

[[ISIS-LDP-SYNC: Subscribe LDP global famous port successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_243422700}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x503674036}*[订阅]{style="font-family:宋体"}[LDP]{lang="EN-US"}[全局端口成功。]{style="font-family:宋体"}*

[[\*Jun 25 14:15:57:737 2013 Sysname ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x1951546354}

[[ISIS-LDP-SYNC: LDP port state change to up.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_912128229}

[*[// LDP]{lang="EN-US"}*]{#struct_0_10226_54647_1271151335}*[端口状态变为]{style="font-family:宋体"}[up]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 25 14:15:57:737 2013 Sysname ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x503739572}

[[ISIS-LDP-SYNC: IS-IS connect LDP daemon successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_1520044792}

[*[// IS-IS]{lang="EN-US"}*]{#struct_0_10226_54647_1846501740}*[进程与]{style="font-family:宋体"}[LDP]{lang="EN-US"}[进程连接成功。]{style="font-family:宋体"}*

[[\*Jun 25 14:15:57:737 2013 Sysname ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_2108274634}

[[ISIS-LDP-SYNC: Send LDP smooth start message successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_1813834130}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1061885620}*[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}[平滑开始信息成功。]{style="font-family:宋体"}*

[[\*Jun 25 14:15:57:737 2013 Sysname ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x248538675}

[[ISIS-LDP-SYNC: Send LDP register message successfully: GigabitEthernet1/0/2, ifIndex: 3.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x640109046}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1546660409}*[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}[注册信息成功：接口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 25 14:15:57:738 2013 Sysname ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_1061820084}

[[ISIS-LDP-SYNC: Send LDP smooth end message successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x612478260}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1347581818}*[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}[平滑结束信息成功。]{style="font-family:宋体"}*

[[\*Jun 25 14:17:23:883 2013 Sysname ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_71219151}

[[ISIS-LDP-SYNC: Receive LDP if-state message: GigabitEthernet1/0/2, ifIndex: 3, ldpstate: no-ldp, vrfIndex: 0.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_1906951573}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1061754548}*[接收]{style="font-family:宋体"}[LDP]{lang="EN-US"}[接口状态信息：接口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[LDP]{lang="EN-US"}[状态为]{style="font-family:宋体"}[no-ldp]{lang="EN-US"}[，实例索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 25 14:17:23:883 2013 Sysname ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x1397348901}

[[ISIS-LDP-SYNC: Circuit(GigabitEthernet1/0/2) received event(IGP_LDP_IF_UP), LDP_SYNC state changed from INIT to SYNC_ACHIEVED. ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_298388159}

[*[// GigabitEthernet1/0/2]{lang="EN-US"}*]{#struct_0_10226_54647_226614925}*[接口的]{style="font-family:
宋体"}[LDP]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[no-ldp]{lang="EN-US"}[触发]{style="font-family:宋体"}[LDP]{lang="EN-US"}[同步状态机变化，接口的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[同步状态由]{style="font-family:宋体"}[INIT]{lang="EN-US"}[变为]{style="font-family:宋体"}[SYNC_ACHIEVED]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 25 14:17:23:884 2013 Sysname ISIS/7/ISISDBG: -MDC=1; ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_1061689012}

[[ISIS-LDP-SYNC: Receive LDP push-finish message.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_1746805580}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x1733106428}*[接收到]{style="font-family:宋体"}[LDP push-finish]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

::: {#874550062 .myid}
[]{#_Toc404790515}[]{#struct_0_10226_54647_1533685275}[]{#_Toc358904299}[]{#_Toc355341531}

**LDP \-- LDP调试命令 \-- debugging ospf mpls ldp sync**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_10226_54647_x132919860}

[**[debugging ospf mpls ldp sync ]{lang="EN-US"}**[\[ **event** \| **fsm** \| **query** \] ]{lang="EN-US"}]{#struct_0_10226_54647_1062147764}

[**[undo debugging ospf mpls ldp sync ]{lang="EN-US"}**[ \[ **event** \| **fsm** \| **query** \]]{lang="EN-US"}]{#struct_0_10226_54647_x1549892628}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10226_54647_x216517362}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10226_54647_x1723119845}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10226_54647_1062082228}

[[network-admin]{lang="EN-US"}]{#struct_0_10226_54647_403717380}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10226_54647_2012836946}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10226_54647_x1302798122}

[**[event]{lang="EN-US"}**]{#struct_0_10226_54647_1062016692}[：表示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[收到的]{style="font-family:宋体"}[LDP-IGP]{lang="EN-US"}[同步]{style="font-family:宋体"}[事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_10226_54647_1979518821}[：表示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[LDP-IGP]{lang="EN-US"}[同步状态机调试开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[query]{lang="EN-US"}**]{#struct_0_10226_54647_x737243254}[：表示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[向]{style="font-family:宋体"}[LDP]{lang="EN-US"}[进程发送消息队列的]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_10226_54647_x531278200}

[**[debugging ospf mpls ldp sync]{lang="EN-US"}**]{#struct_0_10226_54647_1510115016}[命令用来打开]{style="font-family:
宋体"}[LDP OSPF]{lang="EN-US"}[同步]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf mpls ldp sync]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[LDP OSPF]{lang="EN-US"}[同步]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_10226_54647_1061951156} [LDP OSPF]{lang="EN-US"}[同步]{style="font-family:宋体"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定任何参数，则表示所有]{style="font-family:宋体"}]{#struct_0_10226_54647_x228473019}[LDP OSPF]{lang="EN-US"}[同步]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[表1-14 ]{lang="EN-US"}[debugging ospf mpls ldp sync event]{lang="EN-US"}]{#struct_0_10226_54647_20799272}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x243667873}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_1062409908}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_2056790795}

[[LDP waiting timer expired.]{lang="EN-US"}]{#struct_0_10226_54647_168368232}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1062344372}[等待定时器超时]{style="font-family:宋体"}

[[Create LDP waiting timer.]{lang="EN-US"}]{#struct_0_10226_54647_x381802918}

[[创建]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1703894071}[等待定时器]{style="font-family:宋体"}

[[Delete LDP waiting timer.]{lang="EN-US"}]{#struct_0_10226_54647_1061885621}

[[删除]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x248604211}[等待定时器]{style="font-family:宋体"}

[[Receive LDP if-state message: *interfaceName*, ifIndex: *ifIndex*, ldpstate: *state*, vrfIndex: *vrfIndex*.]{lang="EN-US"}]{#struct_0_10226_54647_1735540515}

[[接收到]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1061820085}[接口状态信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interfaceName]{lang="EN-US"}*]{#struct_0_10226_54647_x612543796}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ifIndex]{lang="EN-US"}*]{#struct_0_10226_54647_1061754549}[：接口索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[state]{lang="EN-US"}*]{#struct_0_10226_54647_x1397283365}[：]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vrfIndex]{lang="EN-US"}*]{#struct_0_10226_54647_1853290249}[：]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例索引]{lang="EN-US" style="font-family:宋体"}

[[Receive LDP if-state message: ifIndex(inactive): *ifIndex*, ldpstate: *state*, vrfIndex: *vrfIndex*.]{lang="EN-US"}]{#struct_0_10226_54647_1061689013}

[[接收到没有接口索引的]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1746740044}[接口状态信息]{style="font-family:宋体"}

[[LDP send buffer is free.]{lang="EN-US"}]{#struct_0_10226_54647_1062147765}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1549958164}[发送缓冲区为空]{style="font-family:宋体"}

[[LDP break the connection.]{lang="EN-US"}]{#struct_0_10226_54647_1018032493}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1062082229}[断开连接]{style="font-family:宋体"}

[[Receive LDP state message.]{lang="EN-US"}]{#struct_0_10226_54647_403651844}

[[接收到]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1895521001}[状态信息]{style="font-family:宋体"}

[[Receive LDP push-finish message.]{lang="EN-US"}]{#struct_0_10226_54647_1062016693}

[[接收到]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1979584357}[平滑结束消息]{style="font-family:宋体"}

[[Receive LDP disable message.]{lang="EN-US"}]{#struct_0_10226_54647_1061951157}

[[接收到]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x228407483}[去使能消息]{style="font-family:宋体"}

[[Receive LDP unknown message.]{lang="EN-US"}]{#struct_0_10226_54647_1062409909}

[[接收到未知的]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_2056725259}[消息]{style="font-family:宋体"}

[[Parse LDP message failed.]{lang="EN-US"}]{#struct_0_10226_54647_615108973}

[[解析]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1062344373}[信息失败]{style="font-family:宋体"}

[[OSPF connect LDP daemon successfully.]{lang="EN-US"}]{#struct_0_10226_54647_x381868454}

[[OSPF]{lang="EN-US"}]{#struct_0_10226_54647_1061885618}[与]{style="font-family:宋体"}[LDP]{lang="EN-US"}[进程连接成功]{style="font-family:宋体"}

[[OSPF disconnect from LDP daemon.]{lang="EN-US"}]{#struct_0_10226_54647_x248014390}

[[OSPF]{lang="EN-US"}]{#struct_0_10226_54647_1061820082}[与]{style="font-family:宋体"}[LDP]{lang="EN-US"}[断开连接]{style="font-family:宋体"}

[[LDP port state change to up.]{lang="EN-US"}]{#struct_0_10226_54647_x612609332}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_946537242}[端口状态变为]{style="font-family:宋体"}[up]{lang="EN-US"}

[[LDP port state change to down.]{lang="EN-US"}]{#struct_0_10226_54647_1061754546}

[[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1396431397}[端口状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Subscribe LDP global famous port successfully.]{lang="EN-US"}]{#struct_0_10226_54647_1061689010}

[[订阅]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1746936652}[端口成功]{style="font-family:宋体"}

[[Subscribe LDP global famous port failed.]{lang="EN-US"}]{#struct_0_10226_54647_1062147762}

[[订阅]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1549761556}[端口失败]{style="font-family:宋体"}

[[Unsubscribe LDP global famous port successfully.]{lang="EN-US"}]{#struct_0_10226_54647_1062082226}

[[注销]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_403324164}[端口成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[debugging ospf mpls ldp sync fsm]{lang="EN-US"}]{#struct_0_10226_54647_x830370877}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x213173208}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_1062016690}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_1979387749}

[[Circuit(*interfaceName*) received event(ldp*Event*), LDP_SYNC state changed from *ldpSyncState1* to *ldpSyncState2*. ]{lang="EN-US"}]{#struct_0_10226_54647_438008877}

[[接口]{style="font-family:宋体"}*[interfaceName]{lang="EN-US"}*]{#struct_0_10226_54647_1061951154}[收到事件]{style="font-family:宋体"}[ldp*Event*]{lang="EN-US"}[后，触发]{style="font-family:宋体"}[LDP]{lang="EN-US"}[同步状态机变化，接口的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[同步状态由]{style="font-family:宋体"}*[ldpSyncState1]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[ldpSyncState2]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[debugging ospf mpls ldp query]{lang="EN-US"}]{#struct_0_10226_54647_x228604091}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x214933011}[[字段]{style="font-family:黑体"}]{#struct_0_10226_54647_x1894764747}

[[描述]{style="font-family:黑体"}]{#struct_0_10226_54647_x291570439}

[[Send LDP *msgType* message *resultState*: *interfaceName*, ifIndex: *ifIndex*.]{lang="EN-US"}]{#struct_0_10226_54647_1062409906}

[[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_2057446155}[信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msgType]{lang="EN-US"}*]{#struct_0_10226_54647_240147823}[：信息类型，取值为注册或注销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[resultState]{lang="EN-US"}*]{#struct_0_10226_54647_1062344370}[：结果状态，]{lang="EN-US" style="font-family:
  宋体"}[取值为]{style="font-family:宋体"}[成功或失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interfaceName]{lang="EN-US"}*]{#struct_0_10226_54647_x381671846}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ifIndex]{lang="EN-US"}*]{#struct_0_10226_54647_x656819765}[：接口索引]{lang="EN-US" style="font-family:宋体"}

[[Resend LDP *msgType* message *resultState*: *circuitName*, ifIndex: *ifIndex*.]{lang="EN-US"}]{#struct_0_10226_54647_1061885619}

[[重新发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x248079926}[信息]{style="font-family:宋体"}

[[Send LDP smooth *msgType resultState*.]{lang="EN-US"}]{#struct_0_10226_54647_x1494210081}

[[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_1061820083}[平滑信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msgType]{lang="EN-US"}*]{#struct_0_10226_54647_x612674868}[：信息类型，取值为平滑开始或结束]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[resultState]{lang="EN-US"}*]{#struct_0_10226_54647_1404740940}[：结果状态，]{lang="EN-US" style="font-family:
  宋体"}[取值为]{style="font-family:宋体"}[成功或失败]{lang="EN-US" style="font-family:宋体"}

[[Resend LDP smooth *msgType resultState*.]{lang="EN-US"}]{#struct_0_10226_54647_1061754547}

[[重新发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_10226_54647_x1396365861}[平滑信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10226_54647_1756764883}

[[\# ]{lang="EN-US"}]{#struct_0_10226_54647_1061689011}[在设备上打开所有]{style="font-family:宋体"}[LDP OSPF]{lang="EN-US"}[同步调试信息开关后，在设备上配置]{style="font-family:宋体"}[LDP OSPF]{lang="EN-US"}[同步功能，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ospf mpls ldp sync]{lang="EN-US"}]{#struct_0_10226_54647_1746871116}

[[\*Jun 25 16:34:47:352 2013 Sysname OSPF/7/DEBUG: -MDC=1; Subscribe LDP global famous port successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x189548695}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x1057972228}*[订阅]{style="font-family:宋体"}[LDP]{lang="EN-US"}[全局端口成功。]{style="font-family:宋体"}*

[[\*Jun 25 16:34:47:353 2013 Sysname OSPF/7/DEBUG: -MDC=1; LDP port state change to up.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_427797804}

[*[// LDP]{lang="EN-US"}*]{#struct_0_10226_54647_1062147763}*[端口状态变为]{style="font-family:宋体"}[up]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 25 16:34:47:354 2013 Sysname OSPF/7/DEBUG: -MDC=1; OSPF connect LDP daemon successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x1549827092}

[*[// OSPF]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}*]{#struct_0_10226_54647_x233136577}*[进程与]{style="font-size:10.5pt;font-family:宋体"}[LDP]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[进程连接成功。]{style="font-size:10.5pt;font-family:宋体"}*

[[\*Jun 25 16:34:47:354 2013 Sysname OSPF/7/DEBUG: -MDC=1; Send LDP smooth start message successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x1349322539}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1822791167}*[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}[平滑开始信息成功。]{style="font-family:宋体"}*

[[\*Jun 25 16:34:47:354 2013 Sysname OSPF/7/DEBUG: -MDC=1; Send LDP register message successfully: GigabitEthernet1/0/2, ifIndex: 3.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_1062082227}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_403258628}*[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}[注册信息成功：接口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 25 16:34:47:354 2013 Sysname OSPF/7/DEBUG: -MDC=1; Send LDP smooth end message successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x56944899}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x862290828}*[发送]{style="font-family:宋体"}[LDP]{lang="EN-US"}[平滑结束信息成功。]{style="font-family:宋体"}*

[[\*Jun 25 16:36:13:707 2013 Sysname OSPF/7/DEBUG: -MDC=1; Receive LDP state message.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_x2135416672}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1062016691}*[接收]{style="font-family:宋体"}[LDP]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}*

[[\*Jun 25 16:36:13:707 2013 Sysname OSPF/7/DEBUG: -MDC=1; Receive LDP push-finish message.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_1979453285}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_1194043686}*[接收]{style="font-family:宋体"}[LDP push-finish]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

[[\*Jun 25 16:36:13:707 2013 Sysname OSPF/7/DEBUG: -MDC=1; Receive LDP if-state message: GigabitEthernet1/0/2, ifIndex: 3, ldpstate: no-ldp, vrfIndex: 0.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10226_54647_120126164}

[*[// ]{lang="EN-US"}*]{#struct_0_10226_54647_x1860069173}*[接收]{style="font-family:宋体"}[LDP]{lang="EN-US"}[接口状态信息：接口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[LDP]{lang="EN-US"}[状态为]{style="font-family:宋体"}[no-ldp]{lang="EN-US"}[，实例索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 25 16:36:43:508 2013 Sysname OSPF/7/DEBUG: -MDC=1; Circuit(GigabitEthernet1/0/2) received event(IGP_LDP_IF_UP), LDP_SYNC state changed from INIT to SYNC_ACHIEVED.]{lang="EN-US"}]{#struct_0_10226_54647_1061951155}

[*[// GigabitEthernet1/0/2]{lang="EN-US"}*]{#struct_0_10226_54647_x228538555}*[接口接收到]{style="font-family:
宋体"}[IGP_LDP_NO_LDP]{lang="EN-US"}[事件触发]{style="font-family:宋体"}[LDP]{lang="EN-US"}[同步状态机裱花，接口的]{style="font-family:宋体"}[LDP]{lang="EN-US"}[同步状态由]{style="font-family:宋体"}[INIT]{lang="EN-US"}[变为]{style="font-family:宋体"}[SYNC_ACHIEVED]{lang="EN-US"}*[。]{style="font-size:8.5pt;font-family:宋体"}

[ ]{lang="EN-US"}
