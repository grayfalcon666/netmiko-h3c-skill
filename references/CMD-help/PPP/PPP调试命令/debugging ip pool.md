::: {#-409330805 .myid}
[]{#_Toc404784817}[]{#struct_0_52071_x1881_x1422526222}[]{#_Toc340748465}

**PPP \-- PPP调试命令 \-- debugging ip pool**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_52071_x1881_2079638063}

[**[debugging ip pool]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_52071_x1881_1734312946}

[**[undo debugging ip pool]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_52071_x1881_x1955332489}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52071_x1881_2141066517}

[[用户视图]{style="font-family:宋体"}]{#struct_0_52071_x1881_1458469812}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52071_x1881_470963401}

[[network-admin]{lang="EN-US"}]{#struct_0_52071_x1881_x977018345}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52071_x1881_x1290445633}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x374395226}

[**[all]{lang="EN-US"}**]{#struct_0_52071_x1881_x713007119}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_52071_x1881_1563117140}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_52071_x1881_x1258585107}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1721676644}

[**[debugging ip pool]{lang="FR"}**]{#struct_0_52071_x1881_2141132053}[命令用来打开]{style="font-family:宋体"}[PPP]{lang="FR"}[地址池模块]{style="font-family:宋体"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging ip pool]{lang="FR"}**[命令用来关闭]{style="font-family:宋体"}[PPP]{lang="FR"}[地址池模块]{style="font-family:宋体"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_x1700901447}[地址池模块的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ip pool error]{lang="EN-US"}]{#struct_0_52071_x1881_x1071489587}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1886933011}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_356584313}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_990422961}

[[No IP address available in the IP pool *pool-name*]{lang="EN-US"}]{#struct_0_52071_x1881_x544253146}

[[分配]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_52071_x1881_x1457349620}[地址失败，地址池]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址已耗尽]{style="font-family:宋体"}

[[Failed to assgin IP address from the IP pool *pool-name* ]{lang="EN-US"}]{#struct_0_52071_x1881_x1037102897}

[[从地址池申请]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_52071_x1881_2141590806}[地址失败]{style="font-family:宋体"}

[[Invalid IP address assignment request]{lang="EN-US"}]{#struct_0_52071_x1881_x2088487048}

[[非法的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_52071_x1881_x2136655337}[地址分配请求]{style="font-family:宋体"}

[[Invalid IP address release request]{lang="EN-US"}]{#struct_0_52071_x1881_x1398919899}

[[非法的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_52071_x1881_2030896498}[地址释放请求]{style="font-family:宋体"}

[[Failed to create an expired timer]{lang="EN-US"}]{#struct_0_52071_x1881_x1470095771}

[[创建回收静默地址定时器失败]{style="font-family:宋体"}]{#struct_0_52071_x1881_x167602613}

[[IP pool *pool-name* dose not existed, failed to assign IP address]{lang="EN-US"}]{#struct_0_52071_x1881_2141656342}

[[地址池不存在，分配地址失败]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1700496391}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ip pool event]{lang="EN-US"}]{#struct_0_52071_x1881_x293585729}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1884591134}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_1845330901}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_1133986809}

[[Received an IP address assignment request]{lang="EN-US"}]{#struct_0_52071_x1881_x1390662978}

[[主控板收到地址分配请求消息]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1555084839}

[[Created an expired timer]{lang="EN-US"}]{#struct_0_52071_x1881_2141721878}

[[创建静默地址定时器]{style="font-family:宋体"}]{#struct_0_52071_x1881_667462614}

[[Destroyed an expired timer]{lang="EN-US"}]{#struct_0_52071_x1881_1552142841}

[[删除静默地址定时器]{style="font-family:宋体"}]{#struct_0_52071_x1881_1577925567}

[[Assigned an IP address *ip-address* from free-list]{lang="EN-US"}]{#struct_0_52071_x1881_1796772278}

[[从空闲地址列表中分配一个地址]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1615106290}

[[Assigned an IP address *ip-address* from expired-list]{lang="EN-US"}]{#struct_0_52071_x1881_2141787414}

[[从静默地址列表中分配一个地址]{style="font-family:宋体"}]{#struct_0_52071_x1881_x2077102034}

[[IP address *ip-address* successfully assigned]{lang="EN-US"}]{#struct_0_52071_x1881_1197883621}

[[分配地址成功]{style="font-family:宋体"}]{#struct_0_52071_x1881_x365626922}

[[Received an IP address release request]{lang="EN-US"}]{#struct_0_52071_x1881_x809444058}

[[主控板收到地址回收请求消息]{style="font-family:宋体"}]{#struct_0_52071_x1881_158974929}

[[Released the IP address *ip-address* to the free-list]{lang="EN-US"}]{#struct_0_52071_x1881_x2130491686}

[[回收地址到空闲地址列表中]{style="font-family:宋体"}]{#struct_0_52071_x1881_2141852950}

[[Released the IP address *ip-address* to the expired-list]{lang="EN-US"}]{#struct_0_52071_x1881_x1286714084}

[[回收地址到静默地址列表中]{style="font-family:宋体"}]{#struct_0_52071_x1881_x840782158}

[[IP address *ip-address* successfully released]{lang="EN-US"}]{#struct_0_52071_x1881_577972280}

[[回收地址成功]{style="font-family:宋体"}]{#struct_0_52071_x1881_x151319073}

[[Received a smooth-start message]{lang="EN-US"}]{#struct_0_52071_x1881_2141918486}

[[主控板收到接口板的地址池数据平滑开始消息]{style="font-family:宋体"}]{#struct_0_52071_x1881_x950281508}

[[Received a smooth-end message]{lang="EN-US"}]{#struct_0_52071_x1881_x658604724}

[[主控板收到接口板的地址池数据平滑结束消息]{style="font-family:宋体"}]{#struct_0_52071_x1881_32841820}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52071_x1881_974224958}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_x1127974118}[两台集中式设备用]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口连接，链路封装]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协议，本端配置通过地址池为对端分配地址和本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，对端配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址可协商属性，打开]{style="font-family:宋体"}[PPP]{lang="EN-US"}[地址池的事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ip pool event]{lang="EN-US"}]{#struct_0_52071_x1881_x771327259}

[\*Nov 21 15:58:48:129 2012 Sysname PPP/7/IPPOOL_EVENT: -MDC=1;]{lang="EN-US"}

[  Assigned an IP address 1.1.1.2 from free-list.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_2141984022}*[从空闲地址列表中分配一个地址]{style="font-family:宋体"}*

[[\*Nov 21 15:58:48:130 2012 Sysname PPP/7/IPPOOL_EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_1416061854}

[  IP address 1.1.1.2 successfully assigned.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_1317703821}*[地址池分配地址成功]{style="font-family:宋体"}*

::: {#-629131661 .myid}
[]{#_Toc404784818}[]{#struct_0_52071_x1881_x368924939}

**PPP \-- PPP调试命令 \-- debugging ppp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1551365140}

[**[debugging ppp ]{lang="EN-US"}**[{ **all** \| { **chap** \| **ipcp** \| **ipv6cp** \| **lcp** \| **mp** \| **mplscp** \| **osicp** \| **pap** } { **all** \| **error** \| **event** \| **packet** \| **state** } \| { **ip** \| **ipv6** \| **lqm** \| **mpls** \| **osi** } **packet** \| **external event** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_52071_x1881_1692393008}

[**[undo debugging ppp ]{lang="EN-US"}**[{ **all** \| { **chap** \| **ipcp** \| **ipv6cp** \| **lcp** \| **mp** \| **mplscp** \| **osicp** \| **pap** } { **all** \| **error** \| **event** \| **packet** \| **state** } \| { **ip** \| **ipv6** \| **lqm** \| **mpls** \| **osi** } **packet \| external event** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_52071_x1881_x757138690}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52071_x1881_341743316}

[[用户视图]{style="font-family:宋体"}]{#struct_0_52071_x1881_119709528}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x412895626}

[[network-admin]{lang="EN-US"}]{#struct_0_52071_x1881_2142049558}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52071_x1881_x696102707}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1715551339}

[**[all]{lang="EN-US"}**]{#struct_0_52071_x1881_1036357607}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[chap]{lang="FR"}**]{#struct_0_52071_x1881_x1475365011}[：]{style="font-family:宋体"}[质询握手认证协议调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipcp]{lang="FR"}**]{#struct_0_52071_x1881_1685419316}[：]{style="font-family:宋体"}[IP]{lang="FR"}[控制协议]{style="font-family:
宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipv6cp]{lang="FR"}**]{#struct_0_52071_x1881_x980924751}[：]{style="font-family:宋体"}[IPv6]{lang="FR"}[控制协议]{style="font-family:
宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[lcp]{lang="FR"}**]{#struct_0_52071_x1881_1521096632}[：]{style="font-family:宋体"}[链路]{style="font-family:宋体"}[控制协议]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[mp]{lang="FR"}**]{#struct_0_52071_x1881_x337966064}[：多条]{style="font-family:宋体"}[PPP]{lang="FR"}[链路捆绑协议调试信息开关。]{style="font-family:宋体"}

[**[mplscp]{lang="FR"}**]{#struct_0_52071_x1881_x2105587028}[：]{style="font-family:宋体"}[MPLS]{lang="FR"}[控制协议]{style="font-family:
宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[osicp]{lang="FR"}**]{#struct_0_52071_x1881_x1059765745}[：]{style="font-family:宋体"}[OSI]{lang="FR"}[控制协议]{style="font-family:
宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[pap]{lang="FR"}**]{#struct_0_52071_x1881_2141066518}[：]{style="font-family:宋体"}[密码认证协议调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_52071_x1881_1457486772}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_52071_x1881_x1207080728}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_52071_x1881_1701529707}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}

[**[state]{lang="EN-US"}**]{#struct_0_52071_x1881_x39437127}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[的状态调试信息开关。]{style="font-family:宋体"}

[**[ip]{lang="FR"}**]{#struct_0_52071_x1881_383562032}[：]{style="font-family:宋体"}[IP]{lang="FR"}[调试信息开关]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="FR"}**]{#struct_0_52071_x1881_333712605}[：]{style="font-family:宋体"}[IPv6]{lang="FR"}[调试信息开关]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[lqm]{lang="FR"}**]{#struct_0_52071_x1881_x1074824733}[：]{style="font-family:宋体"}[PPP]{lang="FR"}[链路质量监测协议]{style="font-family:
宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[mpls]{lang="FR"}**]{#struct_0_52071_x1881_540746569}[：]{style="font-family:宋体"}[MPLS]{lang="FR"}[调试信息开关]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[osi]{lang="FR"}**]{#struct_0_52071_x1881_370104936}[：]{style="font-family:宋体"}[OSI]{lang="FR"}[调试信息开关]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[external event]{lang="FR"}**]{#struct_0_52071_x1881_717567188}[：]{style="font-family:宋体"}[PPP]{lang="FR"}[外部事件调试信息开关。]{style="font-family:宋体"}

[**[interface ]{lang="FR"}**]{#struct_0_52071_x1881_2141132054}*[interface-type interface-number]{lang="FR"}*[：]{style="font-family:宋体"}[指定的接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1700442695}

[**[debugging ppp]{lang="FR"}**]{#struct_0_52071_x1881_x2045906051}[命令用来打开]{style="font-family:宋体"}[PPP]{lang="FR"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging ppp]{lang="FR"}**[命令用来关闭]{style="font-family:宋体"}[PPP]{lang="FR"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_1458973145}[的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_52071_x1881_x240597475}[[表1-3 ]{lang="EN-US"}[debugging ppp *protocol-type* error]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1889401693}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_1498925611}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1420970664}

[[PPP Error]{lang="EN-US"}]{#struct_0_52071_x1881_2141590803}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_x2088814728}[错误信息]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x2023329113}

[[接口名称]{style="font-family:宋体"}]{#struct_0_52071_x1881_1558065260}

[*[protocol-type]{lang="EN-US"}*]{#struct_0_52071_x1881_x28844529}

[[协议类型，取值为：]{style="font-family:宋体"}[LCP]{lang="EN-US"}]{#struct_0_52071_x1881_x662139912}[、]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[、]{style="font-family:宋体"}[OSICP]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6CP]{lang="EN-US"}[、]{style="font-family:宋体"}[MP]{lang="EN-US"}

[*[error-string]{lang="EN-US"}*]{#struct_0_52071_x1881_1631514754}

[[错误信息内容，取值及含义：]{style="font-family:宋体"}]{#struct_0_52071_x1881_78070278}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FSM ]{lang="EN-US"}[Illegal Event]{lang="EN-US"}]{#struct_0_52071_x1881_2141656339}[：]{style="font-family:宋体"}[状态机非法事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Received bad Confack Packet]{lang="EN-US"}]{#struct_0_52071_x1881_x1700168716}[：]{style="font-family:
  宋体"}[接收错误的]{lang="EN-US" style="font-family:宋体"}[配置确认]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Packet Id Error]{lang="EN-US"}]{#struct_0_52071_x1881_x1119967839}[：]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to send packet]{lang="EN-US"}]{#struct_0_52071_x1881_x2024044716}[：]{style="font-family:宋体"}[发送报文失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Received illegal event]{lang="EN-US"}]{#struct_0_52071_x1881_x902858202}[：]{style="font-family:宋体"}[接收错误的事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Serial line is looped back]{lang="EN-US"}]{#struct_0_52071_x1881_742168254}[：]{style="font-family:
  宋体"}[链路回环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Received wrong IPCP ACK]{lang="EN-US"}]{#struct_0_52071_x1881_2141721875}[：]{style="font-family:宋体"}[接收错误]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[配置确认]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_52071_x1881_667790294}[[表1-4 ]{lang="EN-US"}[debugging ppp *protocol-type* event]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1894105923}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_1421017442}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_470269769}

[[PPP Event]{lang="EN-US"}]{#struct_0_52071_x1881_x1689293452}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_1579721519}[事件]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_68337673}

[[接口名称]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1177377119}

[*[protocol-type]{lang="EN-US"}*]{#struct_0_52071_x1881_2141787411}

[[协议类型，取值为：]{style="font-family:宋体"}[LCP]{lang="EN-US"}]{#struct_0_52071_x1881_x2077298642}[、]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLSCP]{lang="EN-US"}[、]{style="font-family:宋体"}[OSICP]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6CP]{lang="EN-US"}[、]{style="font-family:宋体"}[MP]{lang="EN-US"}

[*[event]{lang="EN-US"}*]{#struct_0_52071_x1881_x1687119700}

[[状态机事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_52071_x1881_x2061764206}[的取值及含义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lower Up]{lang="EN-US"}]{#struct_0_52071_x1881_1524555329}[：]{style="font-family:宋体"}[底层]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lower Down]{lang="EN-US"}]{#struct_0_52071_x1881_1573836141}[：]{style="font-family:宋体"}[底层]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Open]{lang="EN-US"}]{#struct_0_52071_x1881_2141852947}[：]{style="font-family:宋体"}[链路可供使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Close]{lang="EN-US"}]{#struct_0_52071_x1881_x1286910693}[：]{style="font-family:宋体"}[链路不提供使用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TO+(Timeout with counter \> 0)]{lang="EN-US"}]{#struct_0_52071_x1881_176699929}[：]{style="font-family:
  宋体"}[超时重发事件（重传计数器大于]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[重发报文）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TO-(Timeout with counter expired)]{lang="EN-US"}]{#struct_0_52071_x1881_1539908206}[：]{style="font-family:宋体"}[超时重发事件（重传计数器不大于]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[，不重发报文）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCR+(Receive ]{lang="EN-US"}]{#struct_0_52071_x1881_x1390430005}[Good ]{lang="EN-US"}[Config]{lang="EN-US"}[ure]{lang="EN-US"}[ Request)]{lang="EN-US"}[：]{style="font-family:宋体"}[从对端收到]{lang="EN-US" style="font-family:宋体"}[Configure-Request]{lang="EN-US"}[报文时]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[触发此事件]{lang="EN-US" style="font-family:
  宋体"}[（]{style="font-family:宋体"}[RCR+]{lang="EN-US"}[事件指对端的配置请求可以接受]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[该事件发生时]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[发送]{lang="EN-US" style="font-family:
  宋体"}[Configure-Ack]{lang="EN-US"}[报文作为响应]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCR-(Receive ]{lang="EN-US"}]{#struct_0_52071_x1881_374751628}[Bad ]{lang="EN-US"}[Config]{lang="EN-US"}[ure]{lang="EN-US"}[ Request)]{lang="EN-US"}[：]{style="font-family:宋体"}[从对端收到]{lang="EN-US" style="font-family:宋体"}[Configure-Request]{lang="EN-US"}[报文时]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[触发此事件]{lang="EN-US" style="font-family:
  宋体"}[（]{style="font-family:宋体"}[RCR-]{lang="EN-US"}[事件指不接受对端的配置请求]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[该事件发生时]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[根据情况发送]{lang="EN-US" style="font-family:
  宋体"}[Configure-Nak]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Configure-Rej]{lang="EN-US"}[报文作为响应]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCA(Receive Config]{lang="EN-US"}]{#struct_0_52071_x1881_258179086}[ure]{lang="EN-US"}[ Ack)]{lang="EN-US"}[：]{style="font-family:宋体"}[收到对端对本端请求选项认可的]{lang="EN-US" style="font-family:宋体"}[Configure-Ack]{lang="EN-US"}[报文时事件发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RCN(Receive Config]{lang="EN-US"}]{#struct_0_52071_x1881_2141918483}[ure]{lang="EN-US"}[ Nak/Reject)]{lang="EN-US"}[：]{style="font-family:宋体"}[收到对端拒绝本端某些或全部请求选项的]{lang="EN-US" style="font-family:宋体"}[Configure-Nak/Rej]{lang="EN-US"}[报文时事件发生]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RTR(Receive Terminate Request)]{lang="EN-US"}]{#struct_0_52071_x1881_x950609188}[：]{style="font-family:
  宋体"}[收到对端]{lang="EN-US" style="font-family:宋体"}[Terminate-Request]{lang="EN-US"}[报文，表明对端想关闭连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RTA(Receive Terminate Ack)]{lang="EN-US"}]{#struct_0_52071_x1881_446046992}[：]{style="font-family:
  宋体"}[接收到对端]{lang="EN-US" style="font-family:宋体"}[Terminate-Ack]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RUC(Receive Unknown Code)]{lang="EN-US"}]{#struct_0_52071_x1881_1505234702}[：]{style="font-family:宋体"}[收到对端发送过来的本端无法解释的报文时触发此事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RXJ+(Receive permitted Code/Protocol Reject )]{lang="EN-US"}]{#struct_0_52071_x1881_1410659991}[：]{style="font-family:宋体"}[收到对端发送过来的]{lang="EN-US" style="font-family:宋体"}[Code-Reject]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Protocol-Reject]{lang="EN-US"}[时此事件发生。]{lang="EN-US" style="font-family:宋体"}[RXJ+]{lang="EN-US"}[：表明被拒绝的选项可接受，即在正常范围内]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RXJ-]{lang="EN-US"}]{#struct_0_52071_x1881_2141984019}[ ]{lang="EN-US"}[(Receive catastrophic Code/Protocol Reject )]{lang="EN-US"}[：]{style="font-family:宋体"}[收到对端发送过来的]{lang="EN-US" style="font-family:宋体"}[Code-Reject]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Protocol-Reject]{lang="EN-US"}[时此事件发生。]{lang="EN-US" style="font-family:宋体"}[RXJ-]{lang="EN-US"}[：表明被拒绝的选项对端不可接受，这将导致链接终止]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RXR(Receive EchoRequest/EchoReply/DiscardRequest)]{lang="EN-US"}]{#struct_0_52071_x1881_1416782751}[：]{style="font-family:宋体"}[当从对端接收到]{lang="EN-US" style="font-family:宋体"}[Echo-Request]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Echo-Reply]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Discard-Request]{lang="EN-US"}[报文时，事件发生。对]{lang="EN-US" style="font-family:宋体"}[Echo-Request]{lang="EN-US"}[报文回应]{lang="EN-US" style="font-family:宋体"}[Echo-Reply]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[*[state ]{lang="EN-US"}*]{#struct_0_52071_x1881_x719381613}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_x787784257}[状态机状态，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[取值见]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-4]{lang="EN-US"}](#aaa)

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ppp external event]{lang="EN-US"}]{#struct_0_52071_x1881_623646587}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1892074144}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1159548910}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x778552285}

[[PPP External Event]{lang="EN-US"}]{#struct_0_52071_x1881_2142049555}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_x696823603}[外部事件]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_947308759}

[[接口名称]{style="font-family:宋体"}]{#struct_0_52071_x1881_x157050467}

[*[event]{lang="EN-US"}*]{#struct_0_52071_x1881_791540131}

[[外部事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_52071_x1881_1976661535}[的取值及含义举例：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}[ negotiate down, start Reset-Timer]{lang="EN-US"}]{#struct_0_52071_x1881_1370996775}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商失败，启动]{lang="EN-US" style="font-family:宋体"}[Reset]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reset-Timer Expired, ]{lang="EN-US"}]{#struct_0_52071_x1881_2141066515}[IPCP]{lang="EN-US"}[ negotiate again]{lang="EN-US"}[：]{style="font-family:宋体"}[Reset]{lang="EN-US"}[定时器超时，]{lang="EN-US" style="font-family:宋体"}[IPCP]{lang="EN-US"}[重协商]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP create rundb]{lang="EN-US"}]{#struct_0_52071_x1881_1458338740}[ error]{lang="EN-US"}[：]{style="font-family:宋体"}[PPP]{lang="EN-US"}[创建运行]{lang="EN-US" style="font-family:宋体"}[DBM]{lang="EN-US"}[错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP update]{lang="EN-US"}]{#struct_0_52071_x1881_x1443640824}[ ]{lang="EN-US"}[rundb]{lang="EN-US"}[ error]{lang="EN-US"}[：]{style="font-family:宋体"}[更新运行]{lang="EN-US" style="font-family:宋体"}[DBM]{lang="EN-US"}[错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reset-Timer Expired, reset LCP and negotiate again]{lang="EN-US"}]{#struct_0_52071_x1881_1188874574}[：]{style="font-family:宋体"}[Reset]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}[，重启协商]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to f]{lang="EN-US"}[ree the User ID ]{lang="EN-US"}]{#struct_0_52071_x1881_x1074431514}*[user]{lang="EN-US"}*[-*id*.]{lang="EN-US"}[：释放]{style="font-family:宋体"}[User ID]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully f]{lang="EN-US"}[ree]{lang="EN-US"}]{#struct_0_52071_x1881_x313499766}[d]{lang="EN-US"}[ the User ID ]{lang="EN-US"}*[user]{lang="EN-US"}*[-*id*.]{lang="EN-US"}[：释放]{style="font-family:宋体"}[User ID]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to s]{lang="EN-US"}[end free User ID asynchronism message]{lang="EN-US"}]{#struct_0_52071_x1881_1401815776}[.]{lang="EN-US"}[：发送释放]{style="font-family:宋体"}[User ID]{lang="EN-US"}[异步消息失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to n]{lang="EN-US"}[otify]{lang="EN-US"}]{#struct_0_52071_x1881_x2010027538}[ User QoS of user logo]{lang="EN-US"}[n]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[User QoS]{lang="EN-US"}[模块用户上线失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully n]{lang="EN-US"}[otif]{lang="EN-US"}]{#struct_0_52071_x1881_x1074628122}[ied]{lang="EN-US"}[ ]{lang="EN-US"}[User QoS]{lang="EN-US"}[ ]{lang="EN-US"}[of user logo]{lang="EN-US"}[n]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[User QoS]{lang="EN-US"}[模块用户上线成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[nvalid User ID. User will ]{lang="EN-US"}]{#struct_0_52071_x1881_x734401427}[be logged off.]{lang="EN-US"}[：无效的]{style="font-family:宋体"}[User ID]{lang="EN-US"}[。用户将下线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to n]{lang="EN-US"}[otify ]{lang="EN-US"}]{#struct_0_52071_x1881_x1590530567}[User QoS of user logoff.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[User QoS]{lang="EN-US"}[模块用户下线失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully n]{lang="EN-US"}[otif]{lang="EN-US"}]{#struct_0_52071_x1881_x1312906685}[ied]{lang="EN-US"}[ ]{lang="EN-US"}[User QoS]{lang="EN-US"}[ ]{lang="EN-US"}[of user logoff.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[User QoS]{lang="EN-US"}[模块用户下线成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[There is no ]{lang="EN-US"}]{#struct_0_52071_x1881_79887427}[user profile configuration]{lang="EN-US"}[ ]{lang="EN-US"}[s]{lang="EN-US"}[o the user will ]{lang="EN-US"}[be logged ]{lang="EN-US"}[off]{lang="EN-US"}[.]{lang="EN-US"}[：没有用户配置，强制用户下线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Notif]{lang="EN-US"}]{#struct_0_52071_x1881_x1074562586}[ied User QoS of ]{lang="EN-US"}[authorization change]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[User QoS]{lang="EN-US"}[模块用户授权信息改变]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_52071_x1881_x1939808567}[d]{lang="EN-US"}[istribute]{lang="EN-US"}[d]{lang="EN-US"}[ the User ID]{lang="EN-US"}*[ user]{lang="EN-US"}*[-*id*.]{lang="EN-US"}[：分配]{style="font-family:宋体"}[User ID]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to distribute user ID because u]{lang="EN-US"}[ser ID]{lang="EN-US"}]{#struct_0_52071_x1881_x1286480079}[s]{lang="EN-US"}[ ha]{lang="EN-US"}[ve]{lang="EN-US"}[ been ]{lang="EN-US"}[used up.]{lang="EN-US"}[：]{style="font-family:宋体"}[User ID]{lang="EN-US"}[耗尽分配失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to s]{lang="EN-US"}[mooth User]{lang="EN-US"}]{#struct_0_52071_x1881_x2033921040}[ ]{lang="EN-US"}[Qo]{lang="EN-US"}[S]{lang="EN-US"}[ data]{lang="EN-US"}[.]{lang="EN-US"}[：平滑]{style="font-family:
  宋体"}[User QoS]{lang="EN-US"}[模块数据失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to n]{lang="EN-US"}[otify ]{lang="EN-US"}]{#struct_0_52071_x1881_x1074759194}[IP]{lang="EN-US"}[v4]{lang="EN-US"}[ multicast of user]{lang="EN-US"}[ ]{lang="EN-US"}[log]{lang="EN-US"}[on]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播用户上线失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully n]{lang="EN-US"}[otif]{lang="EN-US"}]{#struct_0_52071_x1881_x1877003200}[ied]{lang="EN-US"}[ ]{lang="EN-US"}[IP]{lang="EN-US"}[v4]{lang="EN-US"}[ multicast of user]{lang="EN-US"}[ ]{lang="EN-US"}[log]{lang="EN-US"}[on]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播用户上线成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to n]{lang="EN-US"}[otify ]{lang="EN-US"}]{#struct_0_52071_x1881_1962185211}[IP]{lang="EN-US"}[v6]{lang="EN-US"}[ multicast of user]{lang="EN-US"}[ ]{lang="EN-US"}[log]{lang="EN-US"}[on]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播用户上线失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully n]{lang="EN-US"}[otif]{lang="EN-US"}]{#struct_0_52071_x1881_320248501}[ied]{lang="EN-US"}[ ]{lang="EN-US"}[IP]{lang="EN-US"}[v6]{lang="EN-US"}[ multicast of user]{lang="EN-US"}[ ]{lang="EN-US"}[log]{lang="EN-US"}[on]{lang="EN-US"}[..]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播用户上线成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to n]{lang="EN-US"}[otify ]{lang="EN-US"}]{#struct_0_52071_x1881_318661362}[IP]{lang="EN-US"}[v4]{lang="EN-US"}[ multicast of user]{lang="EN-US"}[ ]{lang="EN-US"}[logoff.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播用户下线失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully n]{lang="EN-US"}[otif]{lang="EN-US"}]{#struct_0_52071_x1881_x1074693658}[ied]{lang="EN-US"}[ ]{lang="EN-US"}[IP]{lang="EN-US"}[v4]{lang="EN-US"}[ multicast of user]{lang="EN-US"}[ ]{lang="EN-US"}[logoff.]{lang="EN-US"}[：通知]{style="font-family:
  宋体"}[IPv4]{lang="EN-US"}[组播用户下线成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to n]{lang="EN-US"}[otify ]{lang="EN-US"}]{#struct_0_52071_x1881_516611311}[IP]{lang="EN-US"}[v]{lang="EN-US"}[6 multicast of user]{lang="EN-US"}[ ]{lang="EN-US"}[logoff.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播用户下线失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully n]{lang="EN-US"}[otif]{lang="EN-US"}]{#struct_0_52071_x1881_1131192443}[ied]{lang="EN-US"}[ ]{lang="EN-US"}[IP]{lang="EN-US"}[v]{lang="EN-US"}[6 multicast of user]{lang="EN-US"}[ ]{lang="EN-US"}[logoff.]{lang="EN-US"}[：通知]{style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[组播用户下线成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to n]{lang="EN-US"}[otify ]{lang="EN-US"}]{#struct_0_52071_x1881_1424948790}[IPv4 multicast of]{lang="EN-US"}[ authorization change]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播用户授权变更失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully n]{lang="EN-US"}[otif]{lang="EN-US"}]{#struct_0_52071_x1881_x1074890266}[ied]{lang="EN-US"}[ ]{lang="EN-US"}[IPv4 multicast of]{lang="EN-US"}[ authorization change]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播用户授权变更成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to n]{lang="EN-US"}[otify ]{lang="EN-US"}]{#struct_0_52071_x1881_1264567841}[IPv6 multicast of]{lang="EN-US"}[ authorization change]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播用户授权变更失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully n]{lang="EN-US"}[otif]{lang="EN-US"}]{#struct_0_52071_x1881_x611024030}[ied]{lang="EN-US"}[ ]{lang="EN-US"}[IPv6 multicast of]{lang="EN-US"}[ authorization change]{lang="EN-US"}[.]{lang="EN-US"}[：通知]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播用户授权变更成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to s]{lang="EN-US"}[mooth ]{lang="EN-US"}]{#struct_0_52071_x1881_x850746329}[IPv4 multicast]{lang="EN-US"}[ data]{lang="EN-US"}[.]{lang="EN-US"}[：平滑]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播数据失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to s]{lang="EN-US"}[mooth ]{lang="EN-US"}]{#struct_0_52071_x1881_x849922292}[IPv6 multicast]{lang="EN-US"}[ data]{lang="EN-US"}[.]{lang="EN-US"}[：平滑]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The user NAT seq is not equal to the local seq.]{lang="EN-US"}]{#struct_0_52071_x1881_1012253985}[：用户的]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[序号与本地的序号不一致]{lang="EN-US" style="font-family:宋体"}

*[ ]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully notified NAT of user logon.]{lang="EN-US"}]{#struct_0_52071_x1881_1012253987}[：通知]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[模块用户上线成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Successfully notified NAT of user logoff.]{lang="EN-US"}]{#struct_0_52071_x1881_x1708735202}[：通知]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[模块用户下线成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to notify NAT of user logon.]{lang="EN-US"}]{#struct_0_52071_x1881_x1708735200}[：通知]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[模块用户上线失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to notify NAT of user logoff.]{lang="EN-US"}]{#struct_0_52071_x1881_x1708735198}[：通知]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[模块用户下线失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Received an event to allocate a public IP address and port blocks.]{lang="EN-US"}]{#struct_0_52071_x1881_x1708735196}[：收到分配公网]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[及端口块事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Received an event to free a public IP address and port blocks.]{lang="EN-US"}]{#struct_0_52071_x1881_629916956}[：收到释放公网]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[及端口块事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to smooth NAT data.]{lang="EN-US"}]{#struct_0_52071_x1881_629916958}[：平滑]{lang="EN-US" style="font-family:宋体"}[NAT]{lang="EN-US"}[数据失败]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_52071_x1881_x1500886821}[]{#_Toc130718929}[]{#aaa}[表1-6 ]{lang="EN-US"}[debugging ppp *protocol-type* state]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1892763773}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_611791425}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x220939594}

[[PPP State Change]{lang="EN-US"}]{#struct_0_52071_x1881_x604366023}

[[链路层协议状态变化]{style="font-family:宋体"}]{#struct_0_52071_x1881_2141132051}

[*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x1700770375}

[[接口名称]{style="font-family:宋体"}]{#struct_0_52071_x1881_2119363461}

[*[protocol-type]{lang="EN-US"}*]{#struct_0_52071_x1881_x1926456786}

[[协议类型，取值为：]{style="font-family:宋体"}[LCP]{lang="EN-US"}]{#struct_0_52071_x1881_1661419404}[、]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLSCP]{lang="EN-US"}[、]{style="font-family:宋体"}[OSICP]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6CP]{lang="EN-US"}[、]{style="font-family:宋体"}[MP]{lang="EN-US"}

[*[state ]{lang="EN-US"}*[\--\> *state*]{lang="EN-US"}]{#struct_0_52071_x1881_569058058}

[*[state]{lang="EN-US"}*]{#struct_0_52071_x1881_143083525}[取值及含义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[initial]{lang="EN-US"}]{#struct_0_52071_x1881_2141590804}[：]{style="font-family:宋体"}[初始状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[starting]{lang="EN-US"}]{#struct_0_52071_x1881_x2088618120}[：]{style="font-family:宋体"}[启动状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[closed]{lang="EN-US"}]{#struct_0_52071_x1881_321441233}[：]{style="font-family:宋体"}[关闭状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stopped]{lang="EN-US"}]{#struct_0_52071_x1881_1943868398}[：]{style="font-family:宋体"}[停止状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[closing]{lang="EN-US"}]{#struct_0_52071_x1881_x2141198419}[：]{style="font-family:宋体"}[正]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[关闭状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stopping]{lang="EN-US"}]{#struct_0_52071_x1881_106490833}[：]{style="font-family:宋体"}[正]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[停止状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reqsent]{lang="EN-US"}]{#struct_0_52071_x1881_740077004}[：配置请求发送状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ackrcvd]{lang="EN-US"}]{#struct_0_52071_x1881_2141656340}[：收到对端确认状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[acksent]{lang="EN-US"}]{#struct_0_52071_x1881_x1700627463}[：对对端的确认报文已发送状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[opened]{lang="EN-US"}]{#struct_0_52071_x1881_x531010109}[：链路开启状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_52071_x1881_x1579621970}[[表1-7 ]{lang="EN-US"}[debugging ppp *protocol-type* packet]{lang="EN-US"}]{#_Toc130718930}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2134478947}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_x2064373331}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1841308347}

[[PPP Packet]{lang="EN-US"}]{#struct_0_52071_x1881_x44974362}

[[链路层协议]{style="font-family:宋体"}]{#struct_0_52071_x1881_2141721876}

[*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_667855830}

[[接口名称]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1802472988}

[[Output/Input]{lang="EN-US"}]{#struct_0_52071_x1881_x1798627527}

[[发送]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_52071_x1881_275029182}[接收报文]{style="font-family:宋体"}

[*[protocol-type ]{lang="EN-US"}*[Packet]{lang="EN-US"}]{#struct_0_52071_x1881_x395402316}

[[协议类型，取值为：]{style="font-family:宋体"}[LCP]{lang="EN-US"}]{#struct_0_52071_x1881_1161051374}[、]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLSCP]{lang="EN-US"}[、]{style="font-family:宋体"}[OSICP]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6CP]{lang="EN-US"}[、]{style="font-family:宋体"}[MP]{lang="EN-US"}[、]{style="font-family:宋体"}[LQM]{lang="EN-US"}

[[PktLen *number*]{lang="EN-US"}]{#struct_0_52071_x1881_2141787412}

[[报文长度]{style="font-family:宋体"}]{#struct_0_52071_x1881_x2077495250}

[[Current State *state*]{lang="EN-US"}]{#struct_0_52071_x1881_1202684390}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_313914907}[状态机当前状态，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[取值见]{style="font-family:宋体"}[[表]{style="font-family:
  宋体"}[1-4]{lang="EN-US"}](#aaa)

[[Code *packet-type*]{lang="EN-US"}]{#struct_0_52071_x1881_67386558}

[[报文类型，]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*]{#struct_0_52071_x1881_x2069643924}[取值及含义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ConfReq]{lang="EN-US"}]{#struct_0_52071_x1881_2141852948}[：]{style="font-family:宋体"}[配置请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ConfAck]{lang="EN-US"}]{#struct_0_52071_x1881_x1286189797}[：]{style="font-family:宋体"}[配置确认]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ConfNak]{lang="EN-US"}]{#struct_0_52071_x1881_x2074100441}[：]{style="font-family:宋体"}[配置否认]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ConfRej]{lang="EN-US"}]{#struct_0_52071_x1881_1689946061}[：]{style="font-family:宋体"}[配置拒绝]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TermReq]{lang="EN-US"}]{#struct_0_52071_x1881_642408326}[：]{style="font-family:宋体"}[终止请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TermAck]{lang="EN-US"}]{#struct_0_52071_x1881_x1383762902}[：]{style="font-family:宋体"}[终止确认]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CodeRej]{lang="EN-US"}]{#struct_0_52071_x1881_2141918484}[：]{style="font-family:宋体"}[代码拒绝]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ProtoRej]{lang="EN-US"}]{#struct_0_52071_x1881_x950412580}[：]{style="font-family:宋体"}[协议拒绝]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EchoRequest]{lang="EN-US"}]{#struct_0_52071_x1881_892733787}[：]{style="font-family:宋体"}[回音请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EchoReply]{lang="EN-US"}]{#struct_0_52071_x1881_x148973264}[：]{style="font-family:宋体"}[回音应答]{lang="EN-US" style="font-family:宋体"}

[[id *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1254333714}

[[报文]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_52071_x1881_x581974172}

[[len *number*]{lang="EN-US"}]{#struct_0_52071_x1881_2141984020}

[[排除]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_1416192926}[报文头后报文长度]{style="font-family:宋体"}

[[MagicNumber *magic-number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1073907226}

[[魔术字]{style="font-family:宋体"}]{#struct_0_52071_x1881_616060717}

[[LastOutLQRs *lqr-numer*]{lang="EN-US"}]{#struct_0_52071_x1881_x1074497051}

[[本端已发送的]{style="font-family:宋体"}[LQR]{lang="EN-US"}]{#struct_0_52071_x1881_x1325331162}[报文总数]{style="font-family:宋体"}

[[LastOutPackets *packets-number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1339175497}

[[本端已发送的报文总数]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1074431515}

[[LastOutOctets *octets-number*]{lang="EN-US"}]{#struct_0_52071_x1881_1252584175}

[[本端已发送的字节总数]{style="font-family:宋体"}]{#struct_0_52071_x1881_314855933}

[[PeerInLQRs *lqr-number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1074628123}

[[对端已收到的]{style="font-family:宋体"}[LQR]{lang="EN-US"}]{#struct_0_52071_x1881_1994481928}[报文总数]{style="font-family:宋体"}

[[PeerInPackets *packet-number*]{lang="EN-US"}]{#struct_0_52071_x1881_x2063801456}

[[对端已收到的报文总数]{style="font-family:宋体"}]{#struct_0_52071_x1881_x484026577}

[[PeerInDiscards *discard-number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1074562587}

[[对端已丢弃的报文总数]{style="font-family:宋体"}]{#struct_0_52071_x1881_789074788}

[[PeerInErrors *error-number*]{lang="EN-US"}]{#struct_0_52071_x1881_707244789}

[[对端已收到的错误报文总数]{style="font-family:宋体"}]{#struct_0_52071_x1881_x602316389}

[[PeerInOctets *octets-number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1074759195}

[[对端已收到的字节总数]{style="font-family:宋体"}]{#struct_0_52071_x1881_x310919259}

[[PeerOutLQRs *lqr-number*]{lang="EN-US"}]{#struct_0_52071_x1881_1940063036}

[[对端已发送的]{style="font-family:宋体"}[LQR]{lang="EN-US"}]{#struct_0_52071_x1881_x1074693659}[报文总数]{style="font-family:宋体"}

[[PeerOutPackets *packets-number*]{lang="EN-US"}]{#struct_0_52071_x1881_2082695252}

[[对端已发送的报文总数]{style="font-family:宋体"}]{#struct_0_52071_x1881_x895765953}

[[PeerOutOctets *octets-number*]{lang="EN-US"}]{#struct_0_52071_x1881_845644822}

[[对端已发送的字节总数]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1074890267}

[*[Negotiation type]{lang="EN-US"}*]{#struct_0_52071_x1881_903945166}

[[LCP]{lang="EN-US"}]{#struct_0_52071_x1881_x459227742}[协商选项见]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-6]{lang="EN-US"}](#jghgh)[，]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商选项见]{style="font-family:宋体"}[[表]{style="font-family:
  宋体"}[1-7]{lang="EN-US"}](#sdd)

[ ]{lang="EN-US"}

[]{#struct_0_52071_x1881_1741275558}[]{#jghgh}[表1-8 ]{lang="EN-US"}[debugging ppp lcp packet]{lang="EN-US"}[常用协商]{style="font-family:黑体"}[type]{lang="EN-US"}[值信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2137498360}[[字段值]{style="font-family:黑体"}]{#struct_0_52071_x1881_613082699}

[[描述（英文）]{style="font-family:黑体"}]{#struct_0_52071_x1881_2142049556}

[[描述（中文）]{style="font-family:黑体"}]{#struct_0_52071_x1881_x697020211}

[[1]{lang="EN-US"}]{#struct_0_52071_x1881_x201185983}

[[Maximum-Receive-Unit]{lang="EN-US"}]{#struct_0_52071_x1881_1265055710}

[[最大接收单元]{style="font-family:宋体"}]{#struct_0_52071_x1881_x658400558}

[[2]{lang="EN-US"}]{#struct_0_52071_x1881_x1553403251}

[[Async-Control-Character-Map]{lang="EN-US"}]{#struct_0_52071_x1881_x1300184005}

[[异步控制字符映射]{style="font-family:宋体"}]{#struct_0_52071_x1881_2141066516}

[[3]{lang="EN-US"}]{#struct_0_52071_x1881_1458404276}

[[Authentication-Protocol]{lang="EN-US"}]{#struct_0_52071_x1881_x1398517218}

[[验证协议]{style="font-family:宋体"}]{#struct_0_52071_x1881_1811839495}

[[4]{lang="EN-US"}]{#struct_0_52071_x1881_x1074824731}

[[Quality-Protocol]{lang="EN-US"}]{#struct_0_52071_x1881_x1869776936}

[[质量协议]{style="font-family:宋体"}]{#struct_0_52071_x1881_x565990473}

[[5]{lang="EN-US"}]{#struct_0_52071_x1881_x1096993695}

[[Magic-Number]{lang="EN-US"}]{#struct_0_52071_x1881_549302169}

[[魔术字]{style="font-family:宋体"}]{#struct_0_52071_x1881_1725027093}

[[7]{lang="EN-US"}]{#struct_0_52071_x1881_x337966066}

[[Protocol-Field-Compression]{lang="EN-US"}]{#struct_0_52071_x1881_x338031602}

[[协议域压缩]{style="font-family:宋体"}]{#struct_0_52071_x1881_x337834994}

[[8]{lang="EN-US"}]{#struct_0_52071_x1881_x1434840910}

[[Address-and-Control-Field-Compression]{lang="EN-US"}]{#struct_0_52071_x1881_x337900530}

[[地址控制域压缩]{style="font-family:宋体"}]{#struct_0_52071_x1881_x337703922}

[[13]{lang="EN-US"}]{#struct_0_52071_x1881_x664250541}

[[Callback]{lang="EN-US"}]{#struct_0_52071_x1881_x337769458}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_x1422519568}[回呼]{style="font-family:宋体"}

[[17]{lang="EN-US"}]{#struct_0_52071_x1881_x338228211}

[[Multilink Maximum Received Reconstructed Unit]{lang="EN-US"}]{#struct_0_52071_x1881_x338293747}

[[MP]{lang="EN-US"}]{#struct_0_52071_x1881_1128617608}[最大接收重组单元]{style="font-family:宋体"}

[[18]{lang="EN-US"}]{#struct_0_52071_x1881_x338097139}

[[Short Sequence Number Header Format]{lang="EN-US"}]{#struct_0_52071_x1881_x338162675}

[[MP]{lang="EN-US"}]{#struct_0_52071_x1881_1545521985}[报文协商序号长度]{style="font-family:宋体"}

[[19]{lang="EN-US"}]{#struct_0_52071_x1881_x337966067}

[[Endpoint Discriminator]{lang="EN-US"}]{#struct_0_52071_x1881_x338031603}

[[终端描述符]{style="font-family:宋体"}]{#struct_0_52071_x1881_1933536532}

[ ]{lang="EN-US"}

[]{#struct_0_52071_x1881_2141132052}[]{#sdd}[表1-9 ]{lang="EN-US"}[debugging ppp ipcp packet]{lang="EN-US"}[常用协商]{style="font-family:黑体"}[type]{lang="EN-US"}[值信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2135295066}[[字段值]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1700835911}

[[描述（英文）]{style="font-family:黑体"}]{#struct_0_52071_x1881_x2116055933}

[[描述（中文）]{style="font-family:黑体"}]{#struct_0_52071_x1881_1399347907}

[[2]{lang="EN-US"}]{#struct_0_52071_x1881_x1073907227}

[[IP CompressProt]{lang="EN-US"}]{#struct_0_52071_x1881_x1074497048}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_1047256297}[压缩类型及压缩参数协商]{style="font-family:宋体"}

[[3]{lang="EN-US"}]{#struct_0_52071_x1881_x1516122773}

[[IP Address]{lang="EN-US"}]{#struct_0_52071_x1881_x2045832520}

[[IP]{lang="EN-US"}]{#struct_0_52071_x1881_x873677506}[地址协商]{style="font-family:宋体"}

[[129]{lang="EN-US"}]{#struct_0_52071_x1881_639388104}

[[Primary DNS Server Address]{lang="EN-US"}]{#struct_0_52071_x1881_1752949978}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_x1747823573}[一端向另一端请求]{style="font-family:宋体"}[Primary DNS server]{lang="EN-US"}[地址或向另一端分配]{style="font-family:宋体"}[Primary DNS server]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[131]{lang="EN-US"}]{#struct_0_52071_x1881_x586125621}

[[Secondary DNS Server Address]{lang="EN-US"}]{#struct_0_52071_x1881_x67204241}

[[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_154725073}[一端向另一端请求]{style="font-family:宋体"}[Secondary DNS server]{lang="EN-US"}[地址或向另一端分配]{style="font-family:宋体"}[Secondary DNS server]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52071_x1881_794641430}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_375281408}[两台设备用]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口连接，链路封装]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协议，配置后链路开始协商。打开]{style="font-family:宋体"}[LCP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ppp lcp all]{lang="EN-US"}]{#struct_0_52071_x1881_1752884442}

[\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_EVENT_0: -MDC=1;]{lang="EN-US"}

[  PPP Event: ]{lang="EN-US"}

[      Serial2/1/0 LCP Open Event]{lang="EN-US"}

[      State initial]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_1045778848}*[接口的]{style="font-family:宋体"}[LCP]{lang="EN-US"}[状态机为]{style="font-family:宋体"}[open]{lang="EN-US"}[，状态为]{style="font-family:宋体"}[initial]{lang="EN-US"}*

[[\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_STATE_0: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x978130863}

[  PPP State Change:]{lang="EN-US"}

[      Serial2/1/0 LCP : initial \--\> starting]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_x1160838666}*[接口的]{style="font-family:宋体"}[LCP]{lang="EN-US"}[状态从]{style="font-family:宋体"}[initial]{lang="EN-US"}[状态切换到]{style="font-family:宋体"}[starting]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_EVENT_0: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_2038907004}

[  PPP Event:]{lang="EN-US"}

[      Serial2/1/0 LCP Lower Up  Event]{lang="EN-US"}

[      State starting]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_x2013812352}*[接口的]{style="font-family:宋体"}[LCP]{lang="EN-US"}[底层]{style="font-family:宋体"}[UP]{lang="EN-US"}[事件，]{style="font-family:宋体"}[LCP]{lang="EN-US"}[状态机状态为]{style="font-family:宋体"}[starting]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_STATE_0: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_1752818906}

[  PPP State Change:]{lang="EN-US"}

[      Serial2/1/0 LCP : starting \--\> reqsent]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_982960352}*[接口的]{style="font-family:宋体"}[LCP]{lang="EN-US"}[状态从]{style="font-family:宋体"}[starting]{lang="EN-US"}[状态切换到]{style="font-family:宋体"}[reqsent]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_PACKET_0: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x1650348267}

[  PPP Packet:]{lang="EN-US"}

[      Serial2/1/0 Output LCP(c021) Packet, PktLen 22]{lang="EN-US"}

[      Current State reqsent, code ConfReq(01), id 2a, len 18]{lang="EN-US"}

[      MRU(1), len 4, val 05 dc]{lang="EN-US"}

[      AuthProto(3), len 4, PAP c0 23]{lang="EN-US"}

[      MagicNumber(5), len 6, val 31 18 0c 00]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_x1074431512}*[接口发送长度]{style="font-family:宋体"}[35]{lang="EN-US"}[的]{style="font-family:宋体"}[LCP]{lang="EN-US"}[报文。]{style="font-family:宋体"}[LCP]{lang="EN-US"}[状态机状态为]{style="font-family:宋体"}[reqsent]{lang="EN-US"}[状态，报文类型为]{style="font-family:宋体"}[ConfReq]{lang="EN-US"}[报文，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2a]{lang="EN-US"}[，取掉报文头的报文长度为]{style="font-family:宋体"}[22]{lang="EN-US"}[。协商最大接收单元，字段长度]{style="font-family:宋体"}[4]{lang="EN-US"}[，协商长度]{style="font-family:宋体"}[05dc]{lang="EN-US"}[。协商验证协议，字段长度]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:宋体"}[PAP]{lang="EN-US"}[认证。魔术字，字段长度]{style="font-family:宋体"}[6]{lang="EN-US"}[，魔术字值]{style="font-family:宋体"}[31180c00]{lang="EN-US"}*

*[ ]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_x1120068820}[两台设备用]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口连接，链路封装]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协议]{style="font-family:宋体"}[，分别在两端接口下配置]{style="font-family:宋体"}[PPP LQM]{lang="EN-US"}[功能。打开]{style="font-family:宋体"}[PPP LQM]{lang="EN-US"}[的调试信息开关。待]{style="font-family:宋体"}[PPP]{lang="EN-US"}[链路成功建立后，两端开始交互报文。]{style="font-family:宋体"}

[[\<Syaname\> debugging ppp lqm packet]{lang="EN-US"}]{#struct_0_52071_x1881_x1074628120}

[\<Syaname\>]{lang="EN-US"}

[\*Oct 25 11:46:45:559 2013 Syaname PPP/7/LQM_PACKET_1: -MDC=1;]{lang="EN-US"}

[  PPP Packet:]{lang="EN-US"}

[      Serial2/1/3 Output LQM(c025) Packet, PktLen 52]{lang="EN-US"}

[      Current State opened, len 48, MagicNumber 0xc60dde76]{lang="EN-US"}

[      LastOutLQRs 1, LastOutPackets 110, LastOutOctets 163]{lang="EN-US"}

[      PeerInLQRs 1, PeerInPackets 103, PeerInDiscards 105]{lang="EN-US"}

[      PeerInErrors106, PeerInOctets 102]{lang="EN-US"}

[      PeerOutLQRs 2, PeerOutPackets 110, PeerOutOctets 163]{lang="EN-US"}

[*[// Serial2/1/3]{lang="EN-US"}*]{#struct_0_52071_x1881_x1897200841}*[接口发送长度为]{style="font-family:宋体"}[52]{lang="EN-US"}[的]{style="font-family:宋体"}[LQM]{lang="EN-US"}[报文。]{style="font-family:宋体"}[LCP]{lang="EN-US"}[当前状态机状态为]{style="font-family:宋体"}[opened]{lang="EN-US"}[状态，去掉]{style="font-family:宋体"}[PPP]{lang="EN-US"}[头的报文长度为]{style="font-family:宋体"}[48]{lang="EN-US"}[，魔术字值为]{style="font-family:宋体"}[0xc60dde76]{lang="EN-US"}[，本端已发送的]{style="font-family:宋体"}[LQR]{lang="EN-US"}[报文总数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，已发送的报文总数为]{style="font-family:宋体"}[110]{lang="EN-US"}[，已发送的字节总数为]{style="font-family:宋体"}[163]{lang="EN-US"}[，对端已收到的]{style="font-family:宋体"}[LQR]{lang="EN-US"}[报文总数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，已收到的报文总数为]{style="font-family:宋体"}[103]{lang="EN-US"}[，已丢弃的报文总数为]{style="font-family:宋体"}[105]{lang="EN-US"}[，已收到的错误报文总数为]{style="font-family:宋体"}[106]{lang="EN-US"}[，已收到的字节总数为]{style="font-family:宋体"}[102]{lang="EN-US"}[，已发送的]{style="font-family:宋体"}[LQR]{lang="EN-US"}[报文总数为]{style="font-family:宋体"}[2]{lang="EN-US"}[，已发送的报文总数为]{style="font-family:宋体"}[110]{lang="EN-US"}[，已发送的字节总数为]{style="font-family:宋体"}[163]{lang="EN-US"}*

[[\*Oct 25 11:46:45:561 2013 Syaname PPP/7/LQM_PACKET_1: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x1336366901}

[  PPP Packet:]{lang="EN-US"}

[      Serial2/1/3 Input LQM(c025) Packet, PktLen 52]{lang="EN-US"}

[      Current State opened, len 48, MagicNumber 0xef4f8337]{lang="EN-US"}

[      LastOutLQRs 2, LastOutPackets 110, LastOutOctets 163]{lang="EN-US"}

[      PeerInLQRs 2, PeerInPackets 103, PeerInDiscards 105]{lang="EN-US"}

[      PeerInErrors 106, PeerInOctets 102]{lang="EN-US"}

[      PeerOutLQRs 2, PeerOutPackets 110, PeerOutOctets 163]{lang="EN-US"}

[*[// Serial2/1/3]{lang="EN-US"}*]{#struct_0_52071_x1881_2063932114}*[接口收到长度为]{style="font-family:宋体"}[52]{lang="EN-US"}[的]{style="font-family:宋体"}[LQM]{lang="EN-US"}[报文。]{style="font-family:宋体"}[LCP]{lang="EN-US"}[当前状态机状态为]{style="font-family:宋体"}[opened]{lang="EN-US"}[状态，去掉]{style="font-family:宋体"}[PPP]{lang="EN-US"}[头的报文长度为]{style="font-family:宋体"}[48]{lang="EN-US"}[，魔术字值为]{style="font-family:宋体"}[0xef4f8337]{lang="EN-US"}[，本端已发送的]{style="font-family:宋体"}[LQR]{lang="EN-US"}[报文总数为]{style="font-family:宋体"}[2]{lang="EN-US"}[，已发送的报文总数为]{style="font-family:宋体"}[110]{lang="EN-US"}[，已发送的字节总数为]{style="font-family:宋体"}[163]{lang="EN-US"}[，对端已收到的]{style="font-family:宋体"}[LQR]{lang="EN-US"}[报文总数为]{style="font-family:宋体"}[2]{lang="EN-US"}[，已收到的报文总数为]{style="font-family:宋体"}[103]{lang="EN-US"}[，已丢弃的报文总数为]{style="font-family:宋体"}[105]{lang="EN-US"}[，已收到的错误报文总数为]{style="font-family:宋体"}[106]{lang="EN-US"}[，已收到的字节总数为]{style="font-family:宋体"}[102]{lang="EN-US"}[，已发送的]{style="font-family:宋体"}[LQR]{lang="EN-US"}[报文总数为]{style="font-family:宋体"}[2]{lang="EN-US"}[，已发送的报文总数为]{style="font-family:宋体"}[110]{lang="EN-US"}[，已发送的字节总数为]{style="font-family:宋体"}[163]{lang="EN-US"}*

::: {#756912521 .myid}
[]{#_Toc404784819}[]{#struct_0_52071_x1881_x1522585801}

**PPP \-- PPP调试命令 \-- debugging ppp compression iphc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_52071_x1881_459354755}

[**[debugging ppp compression iphc ]{lang="EN-US"}**[{ **rtp** \| **tcp** }]{lang="EN-US"}]{#struct_0_52071_x1881_734705772}

[**[undo debugging ppp compression iphc]{lang="EN-US"}**[ { **rtp** \| **tcp** }]{lang="EN-US"}]{#struct_0_52071_x1881_x1074562584}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1192359315}

[[用户视图]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1303691426}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1503484034}

[[network-admin]{lang="EN-US"}]{#struct_0_52071_x1881_x1982138924}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52071_x1881_188987622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1932156834}

[**[rtp]{lang="EN-US"}**]{#struct_0_52071_x1881_x1667290171}[：表示]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩调试信息开关。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_52071_x1881_2021308860}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩调试信息开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1216885870}

[**[debugging ppp compression iphc]{lang="EN-US"}**]{#struct_0_52071_x1881_x1482298005}[命令用来打开]{style="font-family:
宋体"}[IPHC]{lang="EN-US"}[压缩调试信息开关。]{style="font-family:宋体"}

[**[undo debugging ppp compression iphc]{lang="EN-US"}**]{#struct_0_52071_x1881_1309859223}[命令用来关闭]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PPP IPHC]{lang="EN-US"}]{#struct_0_52071_x1881_x1074759192}[的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[表1-10 ]{lang="EN-US"}[debugging ppp compression iphc]{lang="EN-US"}]{#struct_0_52071_x1881_x1070434146}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_399038407}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_1250641880}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1074693656}

[[RHC]{lang="EN-US"}]{#struct_0_52071_x1881_1679410725}

[[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_x1074890264}[头压缩信息]{style="font-family:宋体"}

[[THC]{lang="EN-US"}]{#struct_0_52071_x1881_x1867600041}

[[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_x112064876}[头压缩信息]{style="font-family:宋体"}

[[FULL_HEADER]{lang="EN-US"}]{#struct_0_52071_x1881_x1074824728}

[[未压缩的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_52471829}[或者]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文，解压端根据这个报文为解压后续的压缩报文创建或更新解压表项]{style="font-family:宋体"}

[[CONTEXT_STATE]{lang="EN-US"}]{#struct_0_52071_x1881_x1073972760}

[[一种由解压端发送给压缩端的特殊报文，用来传输已经或者可能已经失去同步的压缩和解压表项的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_52071_x1881_1566658949}[号来通知压缩端发送一个]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文来同步压缩和解压缩表项]{style="font-family:宋体"}

[[COMPRESSED_NON_TCP]{lang="EN-US"}]{#struct_0_52071_x1881_x1073907224}

[[压缩的]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_1778860131}[报文。接口下配置]{style="font-family:宋体"}**[ppp compression iphc enable]{lang="EN-US"}**[ **nonstandard**]{lang="EN-US"}[命令后，成功压缩时，压缩端会将]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文压缩成该格式的报文]{style="font-family:宋体"}

[[COMPRESSED_TCP]{lang="EN-US"}]{#struct_0_52071_x1881_x1074497049}

[[压缩的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_x1681627058}[报文。成功压缩时，压缩端会将]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文压缩成该格式的报文]{style="font-family:宋体"}

[[COMPRESSED_RTP_8]{lang="EN-US"}]{#struct_0_52071_x1881_x1074431513}

[[压缩的]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_446015121}[报文。当接口上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数小于等于]{style="font-family:宋体"}[256]{lang="EN-US"}[时，成功压缩时，压缩端会将]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文压缩成该种格式的报文]{style="font-family:宋体"}

[[COMPRESSED_RTP_16]{lang="EN-US"}]{#struct_0_52071_x1881_x1074628121}

[[压缩的]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_831682514}[报文。当接口上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数大于]{style="font-family:宋体"}[256]{lang="EN-US"}[时，成功压缩时，压缩端会将]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文压缩成该种格式的报文]{style="font-family:宋体"}

[[ERROR]{lang="EN-US"}]{#struct_0_52071_x1881_x1074562585}

[[IPHC]{lang="EN-US"}]{#struct_0_52071_x1881_x373724626}[压缩]{style="font-family:宋体"}[/]{lang="EN-US"}[解压缩过程的错误信息]{style="font-family:宋体"}

[[WARNING]{lang="EN-US"}]{#struct_0_52071_x1881_x1074759193}

[[IPHC]{lang="EN-US"}]{#struct_0_52071_x1881_495649795}[压缩]{style="font-family:宋体"}[/]{lang="EN-US"}[解压缩过程的提示信息]{style="font-family:宋体"}

[[received]{lang="EN-US"}]{#struct_0_52071_x1881_188145754}

[[接收报文]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1074693657}

[[sent]{lang="EN-US"}]{#struct_0_52071_x1881_x1049472630}

[[发送报文]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1074890265}

[[connect ID]{lang="EN-US"}]{#struct_0_52071_x1881_x301516100}

[[报文流标识，表示压缩]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_52071_x1881_x1074824729}[解压缩的某条流。压缩端和解压端根据这个]{style="font-family:宋体"}[ID]{lang="EN-US"}[号来查找压缩和解压缩表项]{style="font-family:宋体"}

[[checksum]{lang="EN-US"}]{#struct_0_52071_x1881_x1513612112}

[[校验和]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1073972761}

[[seq]{lang="EN-US"}]{#struct_0_52071_x1881_x1162224406}

[[Sequence Number]{lang="EN-US"}]{#struct_0_52071_x1881_x1073907225}[，报文的序列号]{style="font-family:宋体"}

[[gen]{lang="EN-US"}]{#struct_0_52071_x1881_212776190}

[[Generation Number]{lang="EN-US"}]{#struct_0_52071_x1881_847817249}[字段用来检测]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[报文压缩和解压缩的一致性]{style="font-family:宋体"}

[[Sent uncompressed packets]{lang="EN-US"}]{#struct_0_52071_x1881_1428961260}

[[发送了没有压缩的报文。压缩过程中，当检测到压缩表项为空，不能对报文进行压缩，为保证报文传输，会发送没有经过压缩的报文，并打印该条信息]{style="font-family:宋体"}]{#struct_0_52071_x1881_847882785}

[[The compression context of TCP is invalid]{lang="EN-US"}]{#struct_0_52071_x1881_x986081628}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847686177}[报文过程中检测到压缩表项无效。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[IP header mismatched]{lang="EN-US"}]{#struct_0_52071_x1881_1187371776}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847751713}[报文过程中检测到]{style="font-family:宋体"}[IP]{lang="EN-US"}[头与压缩表项中的不匹配。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[TCP header mismatched]{lang="EN-US"}]{#struct_0_52071_x1881_x366701229}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847555105}[报文过程中检测到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头与压缩表项中的不匹配。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta th_URG code error]{lang="EN-US"}]{#struct_0_52071_x1881_x1775576661}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847620641}[报文过程中检测到]{style="font-family:宋体"}[Delta URG]{lang="EN-US"}[字段编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[th_URG mismatched]{lang="EN-US"}]{#struct_0_52071_x1881_384371317}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847424033}[报文过程中检测到]{style="font-family:宋体"}[URG]{lang="EN-US"}[字段与压缩表项中的不匹配。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta th_win code error]{lang="EN-US"}]{#struct_0_52071_x1881_2123452117}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847489569}[报文过程中检测到]{style="font-family:宋体"}[Delta Window]{lang="EN-US"}[字段编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta th_ACK code error]{lang="EN-US"}]{#struct_0_52071_x1881_122400098}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_371209176}[报文过程中检测到]{style="font-family:宋体"}[Delta Acknowledgment Number]{lang="EN-US"}[字段编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta th_seq code error]{lang="EN-US"}]{#struct_0_52071_x1881_848341537}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_812636057}[报文过程中检测到]{style="font-family:宋体"}[Delta Sequence]{lang="EN-US"}[字段编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The flag bits of th_URG, th_seq, and th_win are set]{lang="EN-US"}]{#struct_0_52071_x1881_848407073}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847817248}[报文过程中检测到]{style="font-family:宋体"}[URG]{lang="EN-US"}[字段、]{style="font-family:宋体"}[Sequence Number]{lang="EN-US"}[字段和]{style="font-family:宋体"}[Window]{lang="EN-US"}[字段的标识位被置为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta IP ID code error]{lang="EN-US"}]{#struct_0_52071_x1881_1428961261}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847882784}[报文过程中检测到]{style="font-family:宋体"}[Delta IP ID]{lang="EN-US"}[编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The compression context of NON_TCP is invalid]{lang="EN-US"}]{#struct_0_52071_x1881_x986081629}

[[将]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_847686176}[报文压缩成]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[报文过程中检测到]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[的压缩表项无效。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[UDP checksum mismatched]{lang="EN-US"}]{#struct_0_52071_x1881_1187371775}

[[压缩]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_847751712}[报文过程中检测到]{style="font-family:宋体"}[UDP]{lang="EN-US"}[头的]{style="font-family:宋体"}[Checksum]{lang="EN-US"}[字段与压缩表项中的不匹配。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The number of compressed NON_TCP packets is out of range]{lang="EN-US"}]{#struct_0_52071_x1881_x366701228}

[[将]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_847555104}[报文压缩成]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[过程中检测到在两个]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文之间，发送的]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[报文的数量超出了规定的范围]{style="font-family:宋体"}

[[The time for compressing NON_TCP packet is lawless]{lang="EN-US"}]{#struct_0_52071_x1881_x1775576660}

[[将]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_847620640}[报文压缩成]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[报文的过程中检测到压缩的报文的时间段非法。这时压缩端会发送一个]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文来同步压缩端和解压端（在每发送一个]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文后的一段时间内压缩的]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[压缩报文是合法的，不在这个时间段内对报文进行压缩是非法的）]{style="font-family:宋体"}

[[The delta values of timestamp,sequence number, or IP ID are lawless]{lang="EN-US"}]{#struct_0_52071_x1881_384371316}

[[压缩]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_847424032}[报文的过程中检测到时间戳的]{style="font-family:宋体"}[delta]{lang="EN-US"}[值、报文序列号的]{style="font-family:宋体"}[delta]{lang="EN-US"}[值或者]{style="font-family:宋体"}[IP ID]{lang="EN-US"}[的]{style="font-family:宋体"}[delta]{lang="EN-US"}[值非法。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The compression context of RTP is invalid]{lang="EN-US"}]{#struct_0_52071_x1881_2123452116}

[[压缩]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_847489568}[报文的过程中检测到]{style="font-family:宋体"}[RTP]{lang="EN-US"}[的压缩表项无效。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The delta value of the IP ID is lawless]{lang="EN-US"}]{#struct_0_52071_x1881_122400097}

[[压缩]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_52071_x1881_848341536}[报文的过程中检测到]{style="font-family:宋体"}[IP]{lang="EN-US"}[头]{style="font-family:宋体"}[Delta ID]{lang="EN-US"}[值非法。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Connect ID xx out of range]{lang="EN-US"}]{#struct_0_52071_x1881_812636056}

[[解压过程中检测到报文流标识号]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_52071_x1881_848407072}[超出合法范围]{style="font-family:宋体"}

[[the decompression context is null]{lang="EN-US"}]{#struct_0_52071_x1881_688230649}

[[解压过程中检测到解压缩表项为空。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}]{#struct_0_52071_x1881_847817251}[报文]{style="font-family:宋体"}

[[the decompression context is  invalid]{lang="EN-US"}]{#struct_0_52071_x1881_x527353884}

[[解压过程中检测到解压缩表项无效。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}]{#struct_0_52071_x1881_847882787}[报文]{style="font-family:宋体"}

[[the TCP checksum is error]{lang="EN-US"}]{#struct_0_52071_x1881_x986081630}

[[解压过程中检测到]{style="font-family:宋体"}[TCP Checksum]{lang="EN-US"}]{#struct_0_52071_x1881_847686179}[字段错误。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[the generation number is mismatched]{lang="EN-US"}]{#struct_0_52071_x1881_1187371766}

[[解压缩过程中检测到]{style="font-family:宋体"}[Generation Number]{lang="EN-US"}]{#struct_0_52071_x1881_847751715}[字段不匹配。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[the time for receiving the packet is lawless]{lang="EN-US"}]{#struct_0_52071_x1881_x366701235}

[[解压过程中检测到接收]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}]{#struct_0_52071_x1881_847555107}[报文的时间非法。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[the sequence number is mismatched]{lang="EN-US"}]{#struct_0_52071_x1881_x1775576659}

[[解压过程中检测到]{style="font-family:宋体"}[Sequence Number]{lang="EN-US"}]{#struct_0_52071_x1881_847620643}[字段与解压表想中的不匹配。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52071_x1881_384371319}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_x330119467}[两台设备]{style="font-family:宋体"}[Rouetr A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[用]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口相连，两端都配置]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩，打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩调试信息开关。当]{style="font-family:宋体"}[Router A]{lang="EN-US"}[以]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[方式登录]{style="font-family:宋体"}[Router B]{lang="EN-US"}[时，]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩解压缩调试信息如下。]{style="font-family:宋体"}

[[\<RouterA\> debugging ppp compression iphc tcp]{lang="EN-US"}]{#struct_0_52071_x1881_1274483271}

[\*Dec  8 11:23:00:081 2013 RouterA IPHC/7/PACKET: -MDC=1;THC: sent FULL_HEADER, connect ID 4, checksum 0x40b8, seq 1872787448]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_52071_x1881_x1661425381}*[头压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0x40b8]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[1872787448]{lang="EN-US"}*

[[\*Dec  8 11:23:00:081 2013 RouterA PPP/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x1618033827}

[  PPP Packet:]{lang="EN-US"}

[      Serial2/1/0 output IPHC(0061) packet, pktLen 56]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_x926104853}*[接口发送]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[56]{lang="EN-US"}*

[[\*Dec  8 11:23:00:082 2013 RouterA IPHC/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_847424035}

[ THC: sent COMPRESSED_TCP, connect ID 4, checksum 0x016a, seq 1872787448]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_52071_x1881_2123452111}*[头压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，发送]{style="font-family:宋体"}[COMPRESSED_TCP]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0x016a]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[1872787448]{lang="EN-US"}*

[[\*Dec  8 11:23:00:082 2013 RouterA PPP/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x1176694502}

[  PPP Packet:]{lang="EN-US"}

[      Serial2/1/0 output IPHC(0063) packet, pktLen 38]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_206999925}*[接口发送]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[38]{lang="EN-US"}*

[[\*Dec  8 11:23:00:083 2013 RouterA PPP/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x765258304}

[  PPP Packet:]{lang="EN-US"}

[      Serial2/1/0 input IPHC(0061) packet, pktLen 56]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_1258388425}*[接口接收]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[56]{lang="EN-US"}*

[[\*Dec  8 11:23:00:083 2013 RouterA IPHC/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_1027000846}

[ THC: received FULL_HEADER, connect ID 52, checksum 0x40a6, seq 766841932]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_52071_x1881_x2005912604}*[头压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[52]{lang="EN-US"}[，接收]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0x40a6]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[766841932]{lang="EN-US"}*

[[\*Dec  8 11:23:00:088 2013 RouterA PPP/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_317586117}

[  PPP Packet:]{lang="EN-US"}

[      Serial2/1/0 input IPHC(0063) packet, pktLen 41]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_241284731}*[接口接收]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[41]{lang="EN-US"}*

[[\*Dec  8 11:23:00:088 2013 RouterA IPHC/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_847489571}

[ THC: received COMPRESSED_TCP, connect ID 4, checksum 0xed67, seq 766841932]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_52071_x1881_x1833915030}*[头压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，接收]{style="font-family:宋体"}[COMPRESSED_TCP]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0x40a6]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[766841932]{lang="EN-US"}*

[[\*Dec  8 11:23:00:088 2013 RouterA IPHC/7/IPHC Event: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x783286763}

[ THC ERROR: Delta th_win code error, connect ID 4]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_52071_x1881_1646538103}*[头压缩错误信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，在压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文过程中]{style="font-family:宋体"}[Delta Window]{lang="EN-US"}[字段编码错误]{style="font-family:宋体"}*

[[\*Dec  8 11:23:00:088 2013 RouterA IPHC/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_1962403850}

[ THC: sent FULL_HEADER, connect ID 4, checksum 0x4086, seq 1872787430]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_52071_x1881_1523364116}*[头压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0x4086]{lang="EN-US"}[，校验和为]{style="font-family:宋体"}[1872787430]{lang="EN-US"}*

[[\*Dec  8 11:23:00:088 2013 RouterA PPP/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x627678827}

[  PPP Packet:]{lang="EN-US"}

[      Serial2/1/0 output IPHC(0061) packet, pktLen 56]{lang="EN-US"}

[*[// Serial2/1/0]{lang="EN-US"}*]{#struct_0_52071_x1881_x2067159441}*[接口发送]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[56]{lang="EN-US"}*

[[\*Dec  8 11:23:00:088 2013 RouterA IPHC/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_52071_x1881_x788992679}

[ THC: sent COMPRESSED_TCP, connect ID 4, checksum 0x22fa, seq 1872787430]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_52071_x1881_472734741}*[头压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[，发送]{style="font-family:宋体"}[COMPRESSED_TCP]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0x016a]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[1872787448]{lang="EN-US"}*

*[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}*

::: {.Section3 style="layout-grid:15.75pt"}
:::

::: {#-1088750001 .myid}
[]{#_Toc404784822}[]{#struct_0_52071_x1881_x338228212}[]{#_Toc361305545}

**PPPoE \-- PPPoE Server调试命令 \-- debugging pppoe-server**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1494517448}

[**[debugging pppoe-server]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \[ **receive** \| **send** \] \| **timer** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_52071_x1881_x338293748}

[**[undo]{lang="EN-US"}**[ **debugging pppoe-server** { **all** \| **error** \| **event** \| **packet** \[ **receive** \| **send** \] \| **timer** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_52071_x1881_x338097140}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x49511462}

[[用户视图]{style="font-family:宋体"}]{#struct_0_52071_x1881_x338162676}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1545325377}

[[network-admin]{lang="EN-US"}]{#struct_0_52071_x1881_x337966068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52071_x1881_552008124}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x338031604}

[**[all]{lang="EN-US"}**]{#struct_0_52071_x1881_x337834996}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_52071_x1881_x1434709838}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_52071_x1881_x337900532}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet send]{lang="EN-US"}**]{#struct_0_52071_x1881_x1392188681}[：表示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[发送报文调试信息开关。]{style="font-family:宋体"}

[**[packet receive]{lang="EN-US"}**]{#struct_0_52071_x1881_x337703924}[：表示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[接收报文的调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_52071_x1881_x664119469}[：表示定时器调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_52071_x1881_x337769460}[：指定的接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x338228213}

[**[debugging pppoe-server]{lang="EN-US"}**]{#struct_0_52071_x1881_1494582984}[命令用来打开]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging pppoe-server]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_52071_x1881_x338293749}[的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[表2-1 ]{lang="EN-US"}[debugging pppoe-server error]{lang="EN-US"}]{#struct_0_52071_x1881_1128486536}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1670880217}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_x338097141}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x338162677}

[[Failed to start the PPPoE server process on slot *slotnum*.]{lang="EN-US"}]{#struct_0_52071_x1881_x337966069}

[[启动单板]{style="font-family:宋体"}*[slotnum]{lang="EN-US"}*]{#struct_0_52071_x1881_x337834997}[上的]{style="font-family:宋体"}[PPPoE server]{lang="EN-US"}[进程失败]{style="font-family:宋体"}

[[Received a packet with an invalid-length PPP-Max-Payload tag (len=*length*).]{lang="EN-US"}]{#struct_0_52071_x1881_x337900533}

[[收到的报文的]{style="font-family:宋体"}[PPP-Max-Payload Tag]{lang="EN-US"}]{#struct_0_52071_x1881_x337703925}[长度错误]{style="font-family:宋体"}

[[Wrong PPP-Max-Payload tag value (value=*value*).]{lang="EN-US"}]{#struct_0_52071_x1881_x337769461}

[[PPP-Max-Payload Tag]{lang="EN-US"}]{#struct_0_52071_x1881_2045107155}[的值错误]{style="font-family:宋体"}

[[Failed to assign a session ID.]{lang="EN-US"}]{#struct_0_52071_x1881_2045172691}

[[分配会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_52071_x1881_2045238227}[失败]{style="font-family:宋体"}

[[Failed to enable VLAN broadcast on VLAN interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_2045303763}

[[VLAN]{lang="EN-US"}]{#struct_0_52071_x1881_2044845011}[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[使能接收广播报文失败]{style="font-family:宋体"}

[[Interface *interface-name* received a packet with an invalid-length circuit-id tag (len=*length*).]{lang="EN-US"}]{#struct_0_52071_x1881_2044910547}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2044976083}[收到报文中]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的数据长度错误，数据长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Interface *interface-name* failed to parse the Enterprise Code in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2045041619}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045631443}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的企业码错误]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse port type in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2045696979}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045107154}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的接口类型失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse the frame number in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2045238226}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045303762}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的框号失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse the slot number in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2044845010}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2044910546}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的板号失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse the subslot number in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2044976082}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045041618}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的子卡号失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse the ATM port in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2045631442}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045696978}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口号失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse the ATM VPI in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2045107153}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045172689}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的]{style="font-family:宋体"}[ATM VPI]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse the ATM VCI in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2045238225}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045303761}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的]{style="font-family:宋体"}[ATM VCI]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse port in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2044910545}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2044976081}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的端口号失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse the VLAN ID in the circuit ID by using TR101.]{lang="EN-US"}]{#struct_0_52071_x1881_2045041617}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045631441}[解析]{style="font-family:宋体"}[TR-101]{lang="EN-US"}[格式的]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[号失败]{style="font-family:宋体"}

[[Interface *interface-name* received a packet with a zero-length remote-id tag.]{lang="EN-US"}]{#struct_0_52071_x1881_2045696977}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045107152}[接收的报文]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[的长度为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Interface *interface-name* failed to parse the remote ID by using format *format*.]{lang="EN-US"}]{#struct_0_52071_x1881_2045172688}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045238224}[以]{style="font-family:宋体"}*[format]{lang="EN-US"}*[格式解析]{style="font-family:宋体"}[remote-id]{lang="EN-US"}[失败。]{style="font-family:宋体"}*[format]{lang="EN-US"}*[为解析格式类型：]{style="font-family:宋体"}[1]{lang="EN-US"}[表示]{style="font-family:宋体"}[hex]{lang="EN-US"}[类型，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示]{style="font-family:宋体"}[ascii]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Interface *interface-name* failed to parse the Vendor-Specific tag.]{lang="EN-US"}]{#struct_0_52071_x1881_2045303760}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2044845008}[解析]{style="font-family:宋体"}[TAG Vendor Specify]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to send a PADS packet (sid=*sessionid*).]{lang="EN-US"}]{#struct_0_52071_x1881_2044910544}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045041616}[发送]{style="font-family:宋体"}[PADS]{lang="EN-US"}[报文失败（会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Interface *interface-name* received a PADR packet with an illegal-length Vendor-Specific tag (len=*length*).]{lang="EN-US"}]{#struct_0_52071_x1881_2045631440}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045696976}[收到的]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文中]{style="font-family:宋体"}[TAG Vendor-specify]{lang="EN-US"}[的长度非法（]{style="font-family:宋体"}[Tag]{lang="EN-US"}[的长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Interface *interface-name* received a PADR packet with a wrong Enterprise Code in the Vendor-Specific tag.]{lang="EN-US"}]{#struct_0_52071_x1881_2045107151}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045172687}[收到的]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文中]{style="font-family:宋体"}[TAG Vendor-specify]{lang="EN-US"}[的企业码错误]{style="font-family:宋体"}

[[Interface *interface-name* received a PADR packet with a format error for the Vendor-Specific tag.]{lang="EN-US"}]{#struct_0_52071_x1881_2045238223}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045303759}[收到的]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文中]{style="font-family:宋体"}[TAG Vendor-specify]{lang="EN-US"}[的格式错误]{style="font-family:宋体"}

[[Interface *interface-name* received a packet with  illegal tag length.]{lang="EN-US"}]{#struct_0_52071_x1881_2044845007}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2044910543}[收到报文中]{style="font-family:宋体"}[TAG]{lang="EN-US"}[的长度非法]{style="font-family:宋体"}

[[Interface *interface-name* received a packet with a nonzero- length End-Of-List tag.]{lang="EN-US"}]{#struct_0_52071_x1881_2045041615}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045631439}[收到报文中]{style="font-family:宋体"}[end-of-list tag]{lang="EN-US"}[长度不为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Interface *interface-name* received a packet containing an ERROR tag (type = *type*).]{lang="EN-US"}]{#struct_0_52071_x1881_2045696975}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045107150}[收到报文中包含类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的错误]{style="font-family:宋体"}[tag]{lang="EN-US"}

[[Interface *interface-name* received a packet with zero or more than one Service-Name tag.]{lang="EN-US"}]{#struct_0_52071_x1881_2045172686}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045238222}[收到报文中包含的]{style="font-family:宋体"}[service-name tag]{lang="EN-US"}[的个数不为]{style="font-family:宋体"}[1]{lang="EN-US"}

[[Interface *interface-name* received a PADI packet with wrong dest-MAC.]{lang="EN-US"}]{#struct_0_52071_x1881_2045303758}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2044845006}[收到的]{style="font-family:宋体"}[PADI]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址错误]{style="font-family:宋体"}

[[Interface *interface-name* received a PADI packet with wrong session-id *sessionid*.]{lang="EN-US"}]{#struct_0_52071_x1881_2044976078}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045041614}[收到的]{style="font-family:宋体"}[PADI]{lang="EN-US"}[报文的会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Interface *interface-name* throttled the client MAC address.]{lang="EN-US"}]{#struct_0_52071_x1881_2045631438}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2045696974}[扼制了对端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface *interface-name* failed to add the AC-Name tag.]{lang="EN-US"}]{#struct_0_52071_x1881_x683776200}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683710664}[向报文中添加]{style="font-family:宋体"}[ac-name tag]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to send a PADO packet.]{lang="EN-US"}]{#struct_0_52071_x1881_x683645128}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683579592}[发送]{style="font-family:宋体"}[PADO]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Interface *interface-name* received a PADR packet with wrong dest-MAC.]{lang="EN-US"}]{#struct_0_52071_x1881_x684038344}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683907272}[收到的]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址错误]{style="font-family:宋体"}

[[Interface *interface-name* received a PADR packet with non-zero session-id *sessionid*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683841736}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683251912}[收到的]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文的会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[不为]{style="font-family:宋体"}[0]{lang="EN-US"}[，为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*

[[Interface *interface-name* failed to add a session.]{lang="EN-US"}]{#struct_0_52071_x1881_x683186376}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683776201}[添加会话失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to send a PADS packet (sid=*sessionid*).]{lang="EN-US"}]{#struct_0_52071_x1881_x683710665}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683645129}[发送]{style="font-family:宋体"}[PADS]{lang="EN-US"}[报文失败（会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Interface *interface-name* received a PADT packet with illegal session-id *sessionid*.]{lang="EN-US"}]{#struct_0_52071_x1881_x684038345}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683972809}[收到的]{style="font-family:宋体"}[PADT]{lang="EN-US"}[报文的会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[非法，会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*

[[Interface *interface-name* received too small a packet of length *length*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683907273}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683841737}[收到的报文总长度过短，报文总长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Interface *interface-name* received a packet with too large a payload of length *length*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683251913}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683186377}[收到的报文负载长度过长，负载长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Interface *interface-name* received a packet with wrong length *length*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683776202}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683645130}[收到的报文总长度错误，报文总长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Interface *interface-name* received packet with wrong ETHER_TYPE *ether_type*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683579594}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x684038346}[收到的报文]{style="font-family:宋体"}[ETHER_TYPE]{lang="EN-US"}[字段错误，]{style="font-family:宋体"}[ETHER_TYPE]{lang="EN-US"}[字段的值为]{style="font-family:宋体"}*[ether_type]{lang="EN-US"}*

[[Interface *interface-name* received a packet with wrong source MAC address.]{lang="EN-US"}]{#struct_0_52071_x1881_x683972810}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683907274}[收到的报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址错误]{style="font-family:宋体"}

[[Interface *interface-name* received a packet with wrong version or type.]{lang="EN-US"}]{#struct_0_52071_x1881_x683841738}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683186378}[收到的报文的]{style="font-family:宋体"}[VERSION]{lang="EN-US"}[字段或者]{style="font-family:宋体"}[TYPE]{lang="EN-US"}[字段错误]{style="font-family:宋体"}

[[Interface *interface-name* failed to create a VA interface.]{lang="EN-US"}]{#struct_0_52071_x1881_x683776203}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683710667}[创建]{style="font-family:宋体"}[VA]{lang="EN-US"}[口失败]{style="font-family:宋体"}

[[Interface *interface-name* failed to get the local MAC address.]{lang="EN-US"}]{#struct_0_52071_x1881_x683645131}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683579595}[获取本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[The kernel of interface *interface-name* failed to get the local MAC address.]{lang="EN-US"}]{#struct_0_52071_x1881_x684038347}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683907275}[的内核获取本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[ VA of %u is invalid.]{lang="EN-US"}]{#struct_0_52071_x1881_x683841739}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683251915}[的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口索引非法]{style="font-family:宋体"}

[[Interface *interface-name* received a packet with a source MAC address mismatched with the peer MAC address stored in the local session.]{lang="EN-US"}]{#struct_0_52071_x1881_x683186379}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683776204}[收到的报文包含的对端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与本地会话中保存的对端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不匹配]{style="font-family:宋体"}

[[Interface *interface-name* received an invalid Ethernet packet with session id *sessionid*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683645132}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683579596}[收到了非法以太网报文，会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*

[[Interface *interface-name* failed to add the PPPoE header.]{lang="EN-US"}]{#struct_0_52071_x1881_x684038348}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683972812}[为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[报文添加]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文头失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表2-2 ]{lang="EN-US"}[debugging pppoe-server event]{lang="EN-US"}]{#struct_0_52071_x1881_x683907276}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2138525561}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_x683841740}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x683251916}

[[The standby MPU received an upgrade-to-active event.]{lang="EN-US"}]{#struct_0_52071_x1881_1499969763}

[[备板收到升级为主板事件]{style="font-family:宋体"}]{#struct_0_52071_x1881_x683186380}

[[Slot *number* inserted.]{lang="EN-US"}]{#struct_0_52071_x1881_x683776205}

[[插入单板]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_52071_x1881_x683710669}

[[Slot *number* removed.]{lang="EN-US"}]{#struct_0_52071_x1881_x683645133}

[[拔出单板]{style="font-family:宋体"}*[number]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_52071_x1881_x683579597}

[[An interface activation event occurred on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_x684038349}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683972813}[发生接口激活事件]{style="font-family:宋体"}

[[An interface deactivation event occurred on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683907277}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x683841741}[发生接口去激活事件]{style="font-family:宋体"}

[[An interface deletion event occurred on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683251917}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_1500035299}[发生接口删除事件]{style="font-family:宋体"}

[[An interface down event occurred on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_x683186381}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882307741}[发生接口]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[An interface shutdown event occurred on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_882373277}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882438813}[发生接口]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[A MAC address change event occurred on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_882504349}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882045597}[发生接口]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化事件]{style="font-family:宋体"}

[[Interface *interface-name* received a PVC down event (VEMap=*number*).]{lang="EN-US"}]{#struct_0_52071_x1881_882111133}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882176669}[接收到]{style="font-family:宋体"}[PVC down]{lang="EN-US"}[事件（]{style="font-family:宋体"}[VE]{lang="EN-US"}[接口映射为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Interface *interface-name* received a PPP down event (sid=*sessionid*).]{lang="EN-US"}]{#struct_0_52071_x1881_882242205}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882832029}[接收到]{style="font-family:宋体"}[PPP down]{lang="EN-US"}[事件（会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Interface *interface-name* was configured not to trust the access line ID.]{lang="EN-US"}]{#struct_0_52071_x1881_882897565}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882307740}[配置不信任接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[，忽略]{style="font-family:宋体"}[circuit-id]{lang="EN-US"}

[[Interface *interface-name* parsed the content of the access line ID as *content*.]{lang="EN-US"}]{#struct_0_52071_x1881_882373276}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882438812}[解析出的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[内容为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[[Interface *interface-name* ignored data of an known type in the Vendor-Specific tag (type=*type*).]{lang="EN-US"}]{#struct_0_52071_x1881_882504348}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882045596}[忽略未知类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的]{style="font-family:宋体"}[Vendor Specify]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[Interface *interface-name* ignored a tag (type=*type*).]{lang="EN-US"}]{#struct_0_52071_x1881_882111132}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882176668}[忽略类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的]{style="font-family:宋体"}[tag]{lang="EN-US"}

[[The session number reached per-card limit.]{lang="EN-US"}]{#struct_0_52071_x1881_882242204}

[[单板建立会话数达到上限]{style="font-family:宋体"}]{#struct_0_52071_x1881_882832028}

[*[T]{lang="EN-US"}*[he session number for VLAN *number* on the peer reached per-VLAN limit on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_882897564}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_317714627}[下对端]{style="font-family:宋体"}[VLAN *number*]{lang="EN-US"}[建立的会话数达到上限]{style="font-family:宋体"}

[[The session number reached the interface limit on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_882307739}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882373275}[下建立的会话数达到上限]{style="font-family:宋体"}

[[The session number for a client MAC reached per-MAC limit on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_882438811}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882504347}[下对端]{style="font-family:宋体"}[Client MAC]{lang="EN-US"}[建立的会话数达到上限]{style="font-family:宋体"}

[[PPPoE server was enabled on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_882045595}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882111131}[使能]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[PPPoE server was disabled on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_882176667}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882242203}[去使能]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Interface *interface-name* got session information successfully.]{lang="EN-US"}]{#struct_0_52071_x1881_882832027}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882897563}[获取会话信息成功]{style="font-family:宋体"}

[[Interface *interface-name* deleted all sessions successfully.]{lang="EN-US"}]{#struct_0_52071_x1881_882307738}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882373274}[删除会话信息成功]{style="font-family:宋体"}

[[The kernel of interface *interface-name* received an interface deletion event.]{lang="EN-US"}]{#struct_0_52071_x1881_882438810}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882504346}[的内核接收到接口删除事件]{style="font-family:宋体"}

[[The kernel of interface *interface-name* received an interface deactivation event.]{lang="EN-US"}]{#struct_0_52071_x1881_882045594}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882111130}[的内核接收到接口去激活事件]{style="font-family:宋体"}

[[The kernel of interface *interface-name* received an interface down event.]{lang="EN-US"}]{#struct_0_52071_x1881_882176666}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882242202}[的内核接收到接口]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[The kernel of interface *interface-name* received a MAC address change event.]{lang="EN-US"}]{#struct_0_52071_x1881_882832026}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882897562}[的内核接收到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化事件]{style="font-family:宋体"}

[[Connected to LICENSE module.]{lang="EN-US"}]{#struct_0_52071_x1881_x160664083}

[[PPPoES]{lang="EN-US"}]{#struct_0_52071_x1881_1405419858}[模块与]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}[模块的连接建立成功]{style="font-family:宋体"}

[[Failed to connect to LICENSE module.]{lang="EN-US"}]{#struct_0_52071_x1881_2041855188}

[[PPPoES]{lang="EN-US"}]{#struct_0_52071_x1881_2022299780}[模块与]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}[模块的连接建立失败]{style="font-family:宋体"}

[[Disconnected from LICENSE module.]{lang="EN-US"}]{#struct_0_52071_x1881_167133336}

[[PPPoES]{lang="EN-US"}]{#struct_0_52071_x1881_195500741}[模块与]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}[模块的连接断开成功]{style="font-family:宋体"}

[[Received LICENSE event: EventType=*event-type*.]{lang="EN-US"}]{#struct_0_52071_x1881_644609235}

[[PPPoES]{lang="EN-US"}]{#struct_0_52071_x1881_947666200}[收到]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}[的]{style="font-family:宋体"}[EventType]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[EventType]{lang="EN-US"}]{#struct_0_52071_x1881_1593392035}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Installed]{lang="EN-US"}]{#struct_0_52071_x1881_1761584682}[：安装]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Uninstalled]{lang="EN-US"}]{#struct_0_52071_x1881_714286492}[：卸载]{lang="EN-US" style="font-family:宋体"}[]{#_GoBack}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Expired]{lang="EN-US"}]{#struct_0_52071_x1881_1719097578}[：过期]{lang="EN-US" style="font-family:宋体"}

[[Changed the session limit from *old-value* to *new-value* per card.]{lang="EN-US"}]{#struct_0_52071_x1881_x967298673}

[**[步骤1[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[更新]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}]{#struct_0_52071_x1881_x1003258941}[定制的]{style="font-family:宋体"}[PPPoES]{lang="EN-US"}[单板会话限制数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[old-value]{lang="EN-US"}*]{#struct_0_52071_x1881_1272144253}[：旧的]{lang="EN-US" style="font-family:宋体"}[PPPoES]{lang="EN-US"}[单板会话限制数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[new-value]{lang="EN-US"}*]{#struct_0_52071_x1881_x1559034023}[：新的]{lang="EN-US" style="font-family:宋体"}[PPPoES]{lang="EN-US"}[单本会话限制数]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表2-3 ]{lang="EN-US"}[debugging pppoe-server packet send]{lang="EN-US"}]{#struct_0_52071_x1881_882307737}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1946860089}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_882373273}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x73058663}

[[Interface *interface-name* sent a PADT packet (sid=*sessionid*, err=*errcode*).]{lang="EN-US"}]{#struct_0_52071_x1881_882438809}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882504345}[发送]{style="font-family:宋体"}[PADT]{lang="EN-US"}[报文（会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[er-code]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Interface *interface-name* sent a PADS packet (sid=*sessionid*).]{lang="EN-US"}]{#struct_0_52071_x1881_882045593}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882111129}[发送]{style="font-family:宋体"}[PADS]{lang="EN-US"}[报文（会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Interface *interface-name* sent a PADO packet.]{lang="EN-US"}]{#struct_0_52071_x1881_882176665}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x1103272917}[发送]{style="font-family:宋体"}[PADO]{lang="EN-US"}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表2-4 ]{lang="EN-US"}[debugging pppoe-server packet receive]{lang="EN-US"}]{#struct_0_52071_x1881_882242201}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1970027673}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_882832025}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_882897561}

[[Interface *interface-name* received a PADI packet.]{lang="EN-US"}]{#struct_0_52071_x1881_317714622}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882307736}[接收到]{style="font-family:宋体"}[PADI]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name* received a PADR packet.]{lang="EN-US"}]{#struct_0_52071_x1881_882373272}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882438808}[接收到]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name* received a PADT packet (sid =*sessionid*)*.*]{lang="EN-US"}]{#struct_0_52071_x1881_882504344}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882045592}[接收到]{style="font-family:宋体"}[PADT]{lang="EN-US"}[报文，会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionid]{lang="EN-US"}*

[[Interface *interface-name* received an unknown packet (code=*code*).]{lang="EN-US"}]{#struct_0_52071_x1881_876932914}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882111128}[接收到未知报文，报文类型为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Interface *interface-name* dropped a multicast or broadcast PPPoE packet.]{lang="EN-US"}]{#struct_0_52071_x1881_882176664}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882242200}[丢弃目的地址不为单播的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name* dropped a PPPoE packet of incorrect length.]{lang="EN-US"}]{#struct_0_52071_x1881_882832024}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_882897560}[丢弃长度错误的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name* dropped an invalid PPPoE packet.]{lang="EN-US"}]{#struct_0_52071_x1881_317714623}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x1846575614}[丢弃非法]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name* received an error packet.]{lang="EN-US"}]{#struct_0_52071_x1881_x1846510078}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x1846444542}[接收到错误的报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表2-5 ]{lang="EN-US"}[debugging pppoe-server timer]{lang="EN-US"}]{#struct_0_52071_x1881_x1846379006}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2006830489}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1792264464}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1846837758}

[[Interface *interface-name* created aging timer for throttled MAC entries.]{lang="EN-US"}]{#struct_0_52071_x1881_x1846772222}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x1846706686}[创建]{style="font-family:宋体"}[MAC]{lang="EN-US"}[扼制老化定时器]{style="font-family:宋体"}

[[Interface *interface-name* started aging throttled MAC entries.]{lang="EN-US"}]{#struct_0_52071_x1881_x1846641150}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x1846051326}[开始进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[遏制表项老化]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1174440841}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_x1845985790}[打开]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[错误调试信息开关。在]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[，并绑定一个不存在的]{style="font-family:宋体"}[虚拟模板接口]{style="font-family:宋体"}[，当接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到会话请求后，系统将输出下列调试信息：]{style="font-family:宋体"}

[[\<Sysname\> debugging pppoe-server error]{lang="EN-US"}]{#struct_0_52071_x1881_x1080959673}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server bind virtual-template 3]{lang="EN-US"}

[\*May 21 16:46:23:365 2013 Sysname PPPOES/7/ERROR: -MDC=1-Slot=0; Interface GigabitEthernet1/0/1 failed to add a session.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_x1846575615}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[添加会话失败]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_x1845902761}[打开]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[事件调试信息开关。在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[。当]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[时，系统将输出下列调试信息：]{style="font-family:宋体"}

[[\<Sysname\> debugging pppoe-server event]{lang="EN-US"}]{#struct_0_52071_x1881_x1846510079}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server bind virtual-template 2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] shutdown]{lang="EN-US"}

[\*May 21 16:47:45:259 2013 Sysname PPPOES/7/EVENT: -MDC=1; An interface shutdown event occurred on interface GigabitEthernet1/0/1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_2143800955}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发生接口]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*May 21 16:47:45:264 2013 Sysname PPPOES/7/EVENT: -MDC=1; An interface down event occurred on interface GigabitEthernet1/0/1.]{lang="EN-US"}]{#struct_0_52071_x1881_x1846444543}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_x1322770777}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发生接口]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*May 21 16:47:45:279 2013 Sysname PPPOES/7/EVENT: -MDC=1; The kernel of interface GigabitEthernet1/0/1 received an interface down event.]{lang="EN-US"}]{#struct_0_52071_x1881_x1846379007}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_936618891}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的内核接收到接口]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_x1846837759}[打开]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文调试信息开关。在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[（绑定的虚拟模板接口存在），]{style="font-family:宋体"}[当接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到会话请求后，]{style="font-family:宋体"}[系统将输出下列调试信息：]{style="font-family:宋体"}

[[\<Sysname\> debugging pppoe-server packet]{lang="EN-US"}]{#struct_0_52071_x1881_2022686342}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server bind virtual-template 2]{lang="EN-US"}

[\*May 21 17:07:10:740 2013 Sysname PPPOES/7/PACKET_RECEIVE: -MDC=1; Interface GigabitEthernet1/0/1 received a PADR packet. ]{lang="EN-US"}

[\*May 21 17:07:10:751 2013 Sysname PPPOES/7/PACKET_SEND: -MDC=1; Interface GigabitEthernet1/0/1 sent a PADS packet (sid=1).]{lang="EN-US"}

[*[// ]{lang="SV"}*]{#struct_0_52071_x1881_x1846772223}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[接收到]{style="font-family:宋体"}[PADR]{lang="SV"}[报文]{style="font-family:宋体"}[，回复]{style="font-family:宋体"}[PADS]{lang="SV"}[报文]{style="font-family:宋体"}*

[ ]{lang="SV"}

[[\# ]{lang="SV"}]{#struct_0_52071_x1881_x2067212003}[打开]{style="font-family:宋体"}[PPPoE Server]{lang="SV"}[的]{style="font-family:宋体"}[PPPoE]{lang="SV"}[定时器调试信息开关。在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上使能]{style="font-family:宋体"}[PPPoE Server]{lang="SV"}[（]{style="font-family:宋体"}[绑定的虚拟模板接口存在]{style="font-family:宋体"}[），]{style="font-family:宋体"}[当接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[第一次]{style="font-family:宋体"}[收到会话请求时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[系统将输出下列调试信息]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[\<Sysname\> debugging pppoe-server timer]{lang="EN-US"}]{#struct_0_52071_x1881_x1846706687}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server bind virtual-template 2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server throttle per-mac 1 5 1000]{lang="EN-US"}

[\*May 21 17:07:10:740 2013 Sysname PPPOES/7/TIMER: -MDC=1; Interface GigabitEthernet1/0/1 created aging timer for throttled MAC entries.]{lang="EN-US"}

[*[// ]{lang="SV"}*]{#struct_0_52071_x1881_x1846641151}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[创建了]{style="font-family:宋体"}[MAC]{lang="EN-US"}[扼制老化定时器]{style="font-family:宋体"}*

::: {#-1104179909 .myid}
[]{#_Toc404784824}[]{#struct_0_52071_x1881_784572515}[]{#_Toc321035232}[]{#_Toc235970619}[]{#_Toc233077691}

**PPPoE \-- PPPoE Client调试命令 \-- debugging pppoe-client**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1752753370}

[**[debugging pppoe-client ]{lang="EN-US"}**[{ **all \| data \| error \| event \| packet** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_52071_x1881_x1359952169}

[**[undo debugging pppoe-client ]{lang="EN-US"}**[{ **all \| data \| error \| event \| packet** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_52071_x1881_58016561}

[[【视图】]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1324745499}

[[用户视图]{style="font-family:宋体"}]{#struct_0_52071_x1881_x1033654417}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1169181358}

[[network-admin]{lang="EN-US"}]{#struct_0_52071_x1881_1339017293}

[[mdc-admin]{lang="EN-US"}]{#struct_0_52071_x1881_x1206798527}

[[【参数】]{style="font-family:黑体"}]{#struct_0_52071_x1881_2029304062}

[**[all]{lang="EN-US"}**]{#struct_0_52071_x1881_1753212122}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[data]{lang="EN-US"}**]{#struct_0_52071_x1881_1394687002}[：表示]{style="font-family:宋体"}[session]{lang="EN-US"}[阶段的数据调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_52071_x1881_1912524038}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_52071_x1881_x652552467}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_52071_x1881_x1887237831}[：表示]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[协议报文调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_52071_x1881_1980195654}[：指定的接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1753146586}

[**[debugging pppoe-client]{lang="EN-US"}**]{#struct_0_52071_x1881_x168007353}[命令用来打开]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging pppoe-client]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}]{#struct_0_52071_x1881_x617197416}[的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[表2-6 ]{lang="EN-US"}[debugging pppoe-client error]{lang="EN-US"}]{#struct_0_52071_x1881_x430750029}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2141823246}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_196862648}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1269100748}

[[The attach process timed out for bundle *number* on interface *interface-name.*]{lang="EN-US"}]{#struct_0_52071_x1881_1999207788}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1497288066}[对应的客户端]{style="font-family:宋体"}[绑定处理超时，对应接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*

[[The detach process timed out for bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1753081050}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x2103922566}[对应的客户端]{style="font-family:宋体"}[去绑定处理超时]{style="font-family:宋体"}

[[Failed to create a session for client of bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x864768602}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x346063729}[对应的客户端]{style="font-family:宋体"}[创建会话失败]{style="font-family:宋体"}

[[The index *index* in dialer message is invalid.]{lang="EN-US"}]{#struct_0_52071_x1881_101358545}

[[拨号信息中的索引号无效]{style="font-family:宋体"}]{#struct_0_52071_x1881_x2143722928}

[[The index *index* in bundle message is invalid.]{lang="EN-US"}]{#struct_0_52071_x1881_1160854456}

[[绑定信息中的索引号无效]{style="font-family:宋体"}]{#struct_0_52071_x1881_1753015514}

[[The dialer message(*type*) is invalid, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x1731928566}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x558946530}[对应客户端的拨号信息无效，]{style="font-family:宋体"}[其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[ ]{lang="EN-US"}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_x805750964}[：建链请求]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_1694495107}[：建链成功指示]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_1042920953}[：断链请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_1753474266}[：断链指示]{lang="EN-US" style="font-family:宋体"}

[[Failed to process a dialer message(*type*), bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x2117643746}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_329232498}[对应的客户端]{style="font-family:宋体"}[处理拨号信息失败，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[ ]{lang="EN-US"}[类型如下：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_x2016075202}[：建链请求]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_x247871814}[：建链成功指示]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_1753408730}[：断链请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_x992425625}[：断链指示]{lang="EN-US" style="font-family:宋体"}

[[Failed to process bundle message(*type*), interface *interface-name*, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x1210285064}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_508369361}[对应的客户端处理绑定信息失败，]{style="font-family:宋体"}[对应接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[ ]{lang="EN-US"}[类型如下：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_BUNDLEPRIM_ATTACH]{lang="EN-US"}]{#struct_0_52071_x1881_695726744}[：绑定]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_BUNDLEPRIM_DETACH]{lang="EN-US"}]{#struct_0_52071_x1881_x621291759}[：去绑定]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to create a timer for connection to DDR daemon.]{lang="EN-US"}]{#struct_0_52071_x1881_1752949979}

[[创建用于与]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_52071_x1881_x1747758037}[守护进程连接的定时器失败]{style="font-family:宋体"}

[[Failed to send a bundle message (*type*) of bundle *number* on interface *interface-name.*]{lang="EN-US"}]{#struct_0_52071_x1881_x422387225}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1079020638}[对应的客户端]{style="font-family:宋体"}[发送绑定信息失败，对应接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[ ]{lang="EN-US"}[类型如下：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_BUNDLEPRIM_ATTACH]{lang="EN-US"}]{#struct_0_52071_x1881_1709782280}[：绑定]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to send a bundle message (*type*) of bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1752884443}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1045844384}[对应的客户端]{style="font-family:宋体"}[发送绑定信息失败，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[ ]{lang="EN-US"}[类型如下：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_BUNDLEPRIM_DETACH]{lang="EN-US"}]{#struct_0_52071_x1881_213610602}[：去绑定]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to send a dialer message (*type*), bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x96198911}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1752818907}[对应的客户端]{style="font-family:宋体"}[发送拨号信息失败，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_982894816}[：建链请求]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_x536479829}[：建链成功指示]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_1183257297}[：断链请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_2049955196}[：断链指示]{lang="EN-US" style="font-family:宋体"}

[[Failed to retransmit a PADR packet, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1752753371}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1360017705}[对应的客户端重传]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to retransmit a PADI packet, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_960925540}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1214286010}[对应的客户端重传]{style="font-family:宋体"}[PADI]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to disconnect the connection to DDR daemon, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1753212123}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1394621466}[对应的客户端]{style="font-family:宋体"}[向]{style="font-family:宋体"}[DDR]{lang="EN-US"}[拆链失败]{style="font-family:宋体"}

[[Failed to send a PADI packet, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1526850506}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1708641577}[对应的客户端]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[PADI]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to send a PADR packet, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1753146587}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x167941817}[对应的客户端]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to transfer the state of session, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x60582331}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x43156149}[对应的客户端]{style="font-family:宋体"}[迁移会话状态失败]{style="font-family:宋体"}

[[HA upgrade failed.]{lang="EN-US"}]{#struct_0_52071_x1881_1753081051}

[[HA]{lang="EN-US"}]{#struct_0_52071_x1881_x2103857030}[升级失败]{style="font-family:宋体"}

[[Failed to transfer the session state. Drop the PADS packet.]{lang="EN-US"}]{#struct_0_52071_x1881_x1449269890}

[[状态迁移失败。丢弃]{style="font-family:宋体"}[PADS]{lang="EN-US"}]{#struct_0_52071_x1881_1753015515}[报文]{style="font-family:宋体"}

[[Failed to transfer the session state. Drop the PADT packet.]{lang="EN-US"}]{#struct_0_52071_x1881_x1731994102}

[[状态迁移失败。丢弃]{style="font-family:宋体"}[PADT]{lang="EN-US"}]{#struct_0_52071_x1881_267241605}[报文]{style="font-family:宋体"}

[[Failed to create a timer for packet retransmission, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x1056447314}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1753474267}[对应的客户端]{style="font-family:宋体"}[创建报文重传定时器失败]{style="font-family:宋体"}

[[Failed to synchronize the data to slot *slot-id* cpu *cpu-id*.]{lang="EN-US"}]{#struct_0_52071_x1881_x2117709282}

[[同步数据到指定板（板号为]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_52071_x1881_x95109603}[）的指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[（]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号为]{style="font-family:宋体"}*[cpu-id]{lang="EN-US"}*[）失败]{style="font-family:宋体"}

[[Failed to synchronize the data to other slots.]{lang="EN-US"}]{#struct_0_52071_x1881_1753408731}

[[同步数据到各板失败]{style="font-family:宋体"}]{#struct_0_52071_x1881_x992360089}

[[Failed to synchronize the data to kernel.]{lang="EN-US"}]{#struct_0_52071_x1881_x432527924}

[[同步数据到内核失败]{style="font-family:宋体"}]{#struct_0_52071_x1881_1666483361}

[[Failed to add a duplicate session of session *id*.]{lang="EN-US"}]{#struct_0_52071_x1881_1752949976}

[[为]{style="font-family:宋体"}[session *id*]{lang="EN-US"}]{#struct_0_52071_x1881_x1747954645}[重复添加会话失败]{style="font-family:宋体"}

[[Not enough memory.]{lang="EN-US"}]{#struct_0_52071_x1881_x878785765}

[[内存不足]{style="font-family:宋体"}]{#struct_0_52071_x1881_1752884440}

[[PPPoE client is not in session stage on interface *interface-name.*]{lang="EN-US"}]{#struct_0_52071_x1881_1045647776}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x1750729594}[上]{style="font-family:宋体"}[PPPOE]{lang="EN-US"}[客户端未处于会话阶段]{style="font-family:宋体"}

[[Failed to get the session for interface *interface-name.*]{lang="EN-US"}]{#struct_0_52071_x1881_1752818904}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_983091424}[上获取会话失败]{style="font-family:宋体"}

[[Failed to process the PPP packet on link layer, session ID id, MAC mac-addr.]{lang="EN-US"}]{#struct_0_52071_x1881_x1730977372}

[[在链路层处理]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_52071_x1881_1752753368}[报文失败，对应]{style="font-family:宋体"}[SESSION_ID]{lang="EN-US"}[为]{style="font-family:宋体"}[id]{lang="EN-US"}[且源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[mac-addr]{lang="EN-US"}

[[Failed to delete a virtual-access interface.]{lang="EN-US"}]{#struct_0_52071_x1881_x1360476456}

[[删除]{style="font-family:宋体"}[Virtual-access]{lang="EN-US"}]{#struct_0_52071_x1881_1415347396}[接口失败]{style="font-family:宋体"}

[[Failed to create a virtual-access interface.]{lang="EN-US"}]{#struct_0_52071_x1881_1753212120}

[[创建]{style="font-family:宋体"}[Virtual-access]{lang="EN-US"}]{#struct_0_52071_x1881_1394818074}[接口失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表2-7 ]{lang="EN-US"}[debugging pppoe-client event]{lang="EN-US"}]{#struct_0_52071_x1881_x1162038574}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2116131355}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_893474693}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_938427752}

[[Received a bundle message(type) for bundle *number* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_595915531}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1753146584}[对应的客户端收到绑定信息，]{style="font-family:宋体"}[对应接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_BUNDLEPRIM_ATTACH]{lang="EN-US"}]{#struct_0_52071_x1881_x168138425}[：绑定]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_BUNDLEPRIM_DETACH]{lang="EN-US"}]{#struct_0_52071_x1881_x1323533337}[：去绑定]{lang="EN-US" style="font-family:
  宋体"}

[[Successfully created a virtual-access interface.]{lang="EN-US"}]{#struct_0_52071_x1881_x2023281848}

[[成功创建]{style="font-family:宋体"}[Virtual-access]{lang="EN-US"}]{#struct_0_52071_x1881_x1681966790}[接口]{style="font-family:宋体"}

[[Successfully deleted a virtual-access interface.]{lang="EN-US"}]{#struct_0_52071_x1881_648852527}

[[成功删除]{style="font-family:宋体"}[Virtual-access]{lang="EN-US"}]{#struct_0_52071_x1881_x800546776}[接口]{style="font-family:宋体"}

[[Successfully created a session, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1753081048}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x2104446855}[对应的客户端]{style="font-family:宋体"}[创建会话成功]{style="font-family:宋体"}

[[The session is already in PPPoE session stage, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_756354601}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1636960925}[对应的客户端的]{style="font-family:宋体"}[会话已处于]{style="font-family:宋体"}[SESSION]{lang="EN-US"}[阶段]{style="font-family:宋体"}

[[The session of bundle *number* does not exist.]{lang="EN-US"}]{#struct_0_52071_x1881_788861649}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_14108147}[对应的会话不存在]{style="font-family:宋体"}

[[Received a dialer message(*type*) of bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1753015512}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1732321782}[对应的客户端接收到]{style="font-family:宋体"}[拨号信息，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_850131303}[：建链请求]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_1304086839}[：建链成功指示]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_x745665247}[：断链请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_1753474264}[：断链指示]{lang="EN-US" style="font-family:宋体"}

[[PPPoE client function is not configured with bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x2117774818}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x831227156}[对应的客户端]{style="font-family:宋体"}[未配置]{style="font-family:宋体"}

[[The connection to DDR daemon disconnected. Try again.]{lang="EN-US"}]{#struct_0_52071_x1881_x183663589}

[[与]{style="font-family:宋体"}[DDR ]{lang="EN-US"}]{#struct_0_52071_x1881_x1456877415}[守护进程连接挂断。重建连接]{style="font-family:宋体"}

[[Successfully sent a bundle message (*type*) of bundle *number* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_1753408728}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x991901338}[对应的客户端]{style="font-family:宋体"}[发送绑定信息成功，对应接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[，其中]{style="font-family:宋体"}[Type]{lang="EN-US"}[类型为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_BUNDLEPRIM_ATTACH]{lang="EN-US"}]{#struct_0_52071_x1881_x302272018}[：绑定]{lang="EN-US" style="font-family:
  宋体"}

[[Successfully sent a bundle message (*type*) of bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x1795553399}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_112195694}[对应的客户端]{style="font-family:宋体"}[发送绑定信息成功，其中]{style="font-family:宋体"}[Type]{lang="EN-US"}[类型为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_BUNDLEPRIM_DETACH]{lang="EN-US"}]{#struct_0_52071_x1881_1752949977}[：去绑定]{lang="EN-US" style="font-family:
  宋体"}

[[Successfully sent a dialer message (*type*), bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x1747889109}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x1147294449}[对应的客户端]{style="font-family:宋体"}[发送拨号信息成功，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_x1561203593}[：建链请求]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_CONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_1752884441}[：建链成功指示]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_REQ]{lang="EN-US"}]{#struct_0_52071_x1881_1045713312}[：断链请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDR_DIALPRIM_DISCONN_IND]{lang="EN-US"}]{#struct_0_52071_x1881_x182661413}[：断链指示]{lang="EN-US" style="font-family:宋体"}

[[Successfully retransmitted a PADI packet, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x268125754}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1752818905}[对应的客户端重传]{style="font-family:宋体"}[PADI]{lang="EN-US"}[报文成功]{style="font-family:宋体"}

[[Successfully retransmitted a PADR packet, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_983025888}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_x204810299}[对应的客户端重传]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文成功]{style="font-family:宋体"}

[[The state of session transferred from *oldstate* to *newstate*, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x537464339}

[[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1752753369}[对应客户端的]{style="font-family:宋体"}[会话状态从]{style="font-family:宋体"}*[oldstate]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[oldstate]{lang="EN-US"}*[和]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_52071_x1881_x1360541992}[：初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADI SENT]{lang="EN-US"}]{#struct_0_52071_x1881_x273354020}[：已发送]{lang="EN-US" style="font-family:宋体"}[PADI]{lang="EN-US"}[报文、等待]{lang="EN-US" style="font-family:宋体"}[PADO]{lang="EN-US"}[报文状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADR SENT]{lang="EN-US"}]{#struct_0_52071_x1881_x1159474036}[：已发送]{lang="EN-US" style="font-family:宋体"}[PADR]{lang="EN-US"}[报文、等待]{lang="EN-US" style="font-family:宋体"}[PADS]{lang="EN-US"}[报文状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SESSION]{lang="EN-US"}]{#struct_0_52071_x1881_1753212121}[：会话协商成功]{lang="EN-US" style="font-family:宋体"}

[[Received an interface *event* event on interface *interface-name*.]{lang="EN-US"}]{#struct_0_52071_x1881_1394752538}

[[在]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_1143107353}[上收到接口]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件，事件类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_52071_x1881_546307253}[：接口激活事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deactive]{lang="EN-US"}]{#struct_0_52071_x1881_1753146585}[：接口去激活事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_52071_x1881_x168072889}[：接口删除事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_52071_x1881_x1813837426}[：接口]{lang="EN-US" style="font-family:宋体"}[Down]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set mac]{lang="EN-US"}]{#struct_0_52071_x1881_x1101069075}[：设置接口]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址事件]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表2-8 ]{lang="EN-US"}[debugging pppoe-client packet]{lang="EN-US"}]{#struct_0_52071_x1881_1753081049}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2121929229}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_x2104381319}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_878950090}

[[Successfully sent a PADI packet, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_x1551200075}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_1172412035}[对应的客户端]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[PADI]{lang="EN-US"}[报文成功]{style="font-family:宋体"}

[[Successfully sent a PADR packet, bundle *number*.]{lang="EN-US"}]{#struct_0_52071_x1881_1126178234}

[[为]{style="font-family:宋体"}[bundle *number*]{lang="EN-US"}]{#struct_0_52071_x1881_493410456}[对应的客户端]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[PADR]{lang="EN-US"}[报文成功]{style="font-family:宋体"}

[[Dropped the PADO packet for incorrect SESSION_ID (*id*).]{lang="EN-US"}]{#struct_0_52071_x1881_1753015513}

[[丢弃]{style="font-family:宋体"}[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_x1732387318}[报文，因为]{style="font-family:宋体"}[SESSION_ID(*id*)]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Dropped the PADO packet for incorrect End-of-List tag.]{lang="EN-US"}]{#struct_0_52071_x1881_x781502549}

[[丢弃]{style="font-family:宋体"}[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_x2110760040}[报文，因为]{style="font-family:宋体"}[End-of-List tag]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Dropped the PADO packet for Service-Name-Error, AC-System-Error, or Generic-Error tag.]{lang="EN-US"}]{#struct_0_52071_x1881_x418859456}

[[丢弃]{style="font-family:宋体"}[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_x1256389799}[报文，因为至少携带以下一种错误]{style="font-family:宋体"}[Tag]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service-Name-Error]{lang="EN-US"}]{#struct_0_52071_x1881_1060189586}[：表示没有理睬所请求的]{lang="EN-US" style="font-family:
  宋体"}[Service-Name]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC-System-Error]{lang="EN-US"}]{#struct_0_52071_x1881_1753474265}[：表示访问集中器在处理主机请求时出现了错误]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic-Error tag]{lang="EN-US"}]{#struct_0_52071_x1881_x2117840354}[：表示报文出错]{lang="EN-US" style="font-family:
  宋体"}

[[Dropped the PADO packet for incorrect Host-Uniq tag.]{lang="EN-US"}]{#struct_0_52071_x1881_1613404588}

[[丢弃]{style="font-family:宋体"}[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_2134234900}[报文，因为]{style="font-family:宋体"}[Host-Uniq tag]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[No Service-Name tag in the PADO packet.]{lang="EN-US"}]{#struct_0_52071_x1881_x716360212}

[[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_1286787674}[报文中未携带]{style="font-family:宋体"}[Service-Name tag]{lang="EN-US"}

[[No AC-Name tag in the PADO packet.]{lang="EN-US"}]{#struct_0_52071_x1881_1753408729}

[[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_x991835802}[报文中未携带]{style="font-family:宋体"}[AC-Name tag]{lang="EN-US"}

[[Dropped the PADO packet for no client is found.]{lang="EN-US"}]{#struct_0_52071_x1881_x1838971782}

[[丢弃]{style="font-family:宋体"}[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_x791714621}[报文，因为未找到会话对应的客户端]{style="font-family:宋体"}

[[Dropped the PADS packet for incorrect SESSION_ID (*id*).]{lang="EN-US"}]{#struct_0_52071_x1881_1100609713}

[[丢弃]{style="font-family:宋体"}[PADS]{lang="EN-US"}]{#struct_0_52071_x1881_1752949974}[报文，因为]{style="font-family:宋体"}[SESSION_ID(*id*)]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Dropped the PADS packet for incorrect End-of-List tag.]{lang="EN-US"}]{#struct_0_52071_x1881_x1748085717}

[[丢弃]{style="font-family:宋体"}[PADS]{lang="EN-US"}]{#struct_0_52071_x1881_39329630}[报文，因为]{style="font-family:宋体"}[End-of-List tag]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Dropped the PADS packet for Service-Name-Error, AC-System-Error, or Generic-Error tag.]{lang="EN-US"}]{#struct_0_52071_x1881_x1215858256}

[[丢弃]{style="font-family:宋体"}[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_x2135633215}[报文，因为至少携带以下一种错误]{style="font-family:宋体"}[Tag]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service-Name-Error]{lang="EN-US"}]{#struct_0_52071_x1881_1752884438}[：表示没有理睬所请求的]{lang="EN-US" style="font-family:
  宋体"}[Service-Name]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC-System-Error]{lang="EN-US"}]{#struct_0_52071_x1881_1045123487}[：表示访问集中器在处理主机请求时出现了错误]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic-Error tag]{lang="EN-US"}]{#struct_0_52071_x1881_x1758736620}[：表示报文出错]{lang="EN-US" style="font-family:
  宋体"}

[[Dropped the PADS packet for incorrect Host-Uniq tag.]{lang="EN-US"}]{#struct_0_52071_x1881_x1555794136}

[[丢弃]{style="font-family:宋体"}[PADS]{lang="EN-US"}]{#struct_0_52071_x1881_x1670386294}[报文，因为]{style="font-family:宋体"}[Host-Uniq tag]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[No Service-Name tag in the PADS packet.]{lang="EN-US"}]{#struct_0_52071_x1881_1752818902}

[[PADS]{lang="EN-US"}]{#struct_0_52071_x1881_982698208}[报文中未携带]{style="font-family:宋体"}[Service-Name tag]{lang="EN-US"}

[[No AC-Name tag in the PADS packet.]{lang="EN-US"}]{#struct_0_52071_x1881_1654275071}

[[PADS]{lang="EN-US"}]{#struct_0_52071_x1881_x447291826}[报文中未携带]{style="font-family:宋体"}[AC-Name tag]{lang="EN-US"}

[[Dropped the PADS packet for no client is found.]{lang="EN-US"}]{#struct_0_52071_x1881_1752753366}

[[丢弃]{style="font-family:宋体"}[PADS]{lang="EN-US"}]{#struct_0_52071_x1881_x1360345384}[报文，因为未找到会话对应的客户端]{style="font-family:宋体"}

[[Dropped the PADT packet for incorrect SESSION_ID (*id*).]{lang="EN-US"}]{#struct_0_52071_x1881_9647940}

[[丢弃]{style="font-family:宋体"}[PADT]{lang="EN-US"}]{#struct_0_52071_x1881_x1174194934}[报文，因为]{style="font-family:宋体"}[SESSION_ID(*id*)]{lang="EN-US"}[错误]{style="font-family:宋体"}

[[Dropped the PADT packet for no client is found.]{lang="EN-US"}]{#struct_0_52071_x1881_1753212118}

[[丢弃]{style="font-family:宋体"}[PADT]{lang="EN-US"}]{#struct_0_52071_x1881_1395342365}[报文，因为未找到会话对应的客户端]{style="font-family:宋体"}

[[Sent a *type* packet on interface *interface-name*, length *length*.]{lang="EN-US"}]{#struct_0_52071_x1881_1169125272}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_1729534647}[上发送长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[报文，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADI]{lang="EN-US"}]{#struct_0_52071_x1881_1753146582}[：]{lang="EN-US" style="font-family:宋体"}[PADI]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADR]{lang="EN-US"}]{#struct_0_52071_x1881_x168269497}[：]{lang="EN-US" style="font-family:宋体"}[PADR]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADT]{lang="EN-US"}]{#struct_0_52071_x1881_1403318364}[：]{lang="EN-US" style="font-family:宋体"}[PADT]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Received a *type* packet on interface *interface-name*, length *length*.]{lang="EN-US"}]{#struct_0_52071_x1881_x2145662749}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_1753081046}[上接收长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[报文，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADO]{lang="EN-US"}]{#struct_0_52071_x1881_x2104053639}[：]{lang="EN-US" style="font-family:宋体"}[PADO]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADS]{lang="EN-US"}]{#struct_0_52071_x1881_x757674894}[：]{lang="EN-US" style="font-family:宋体"}[PADS]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PADT]{lang="EN-US"}]{#struct_0_52071_x1881_329457767}[：]{lang="EN-US" style="font-family:宋体"}[PADT]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_52071_x1881_x1778465494}[[表2-9 ]{lang="EN-US"}[debugging pppoe-client data]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2122610825}[[字段]{style="font-family:黑体"}]{#struct_0_52071_x1881_1753015510}

[[描述]{style="font-family:黑体"}]{#struct_0_52071_x1881_x1732190710}

[[PPPoE Client is not configured on interface *interface-name.* ]{lang="EN-US"}]{#struct_0_52071_x1881_1982837140}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_208983103}[上未配置]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}

[[Dropped a multicast/broadcast PPPoE packet on interface *interface-name.*]{lang="EN-US"}]{#struct_0_52071_x1881_x1672159609}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_x1586746836}[上丢弃一个广播（多播）]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Dropped a PPPoE packet of incorrect length on interface *interface-name.*]{lang="EN-US"}]{#struct_0_52071_x1881_x587536042}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_1753474262}[上丢弃一个长度错误的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Dropped an invalid PPPoE packet on interface *interface-name.*]{lang="EN-US"}]{#struct_0_52071_x1881_x2117381602}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_52071_x1881_2008612337}[上丢弃一个非法的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_52071_x1881_1647390324}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_1605518326}[打开]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[错误调试信息开关，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置一个]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[，]{style="font-family:宋体"}[对应]{style="font-family:宋体"}[bundle number]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，如果]{style="font-family:宋体"}[DDR]{lang="EN-US"}[守护进程已关闭，复位会话后，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging pppoe-client error]{lang="EN-US"}]{#struct_0_52071_x1881_x1256601568}

[\<Sysname\> reset pppoe-client dial-bundle-number 1]{lang="EN-US"}

[\*Jun 23 15:50:40:899 2011 Sysname PPPOEC/7/ERROR: -MDC=1; Failed to disconnect the connection to DDR daemon, bundle 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_1990884689}*[为]{style="font-family:宋体"}[bundle 1]{lang="EN-US"}[对应的客户端]{style="font-family:宋体"}[向]{style="font-family:宋体"}[DDR]{lang="EN-US"}[拆链失败]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_1753408726}[打开]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[事件调试信息开关，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置一个]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[，]{style="font-family:宋体"}[对应]{style="font-family:宋体"}[bundle number]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，且会话处于]{style="font-family:宋体"}[session]{lang="EN-US"}[阶段，复位会话后，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging pppoe-client event]{lang="EN-US"}]{#struct_0_52071_x1881_x992556698}

[\<Sysname\> reset pppoe-client dial-bundle-number 1]{lang="EN-US"}

[\*Jun 23 15:50:40:899 2011 Sysname PPPOEC/7/EVENT: -MDC=1; The state of session transferred from SESSION to IDLE, bundle 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_346623813}*[会话从]{style="font-family:宋体"}[SESSION]{lang="EN-US"}[状态迁移到]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_52071_x1881_1102554673}[打开]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[协议报文调试信息开关。在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置一个]{style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging pppoe-client packet]{lang="EN-US"}]{#struct_0_52071_x1881_1440871854}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-client dial-bundle-number 1]{lang="EN-US"}

[\*Aug 21 11:05:25:202 2011 Sysname PPPOEC/7/PACKET: -MDC=1; Sent]{lang="EN-US"}[ a PADI packet on interface ]{lang="IT"}[GigabitEthernet1/0/1]{lang="EN-US"}[, length 16.]{lang="IT"}

[11 09 00 00 00 0a 01 01 00 00 01 03 00 02 02 00]{lang="SV"}

[*[// GigabitEthernet1/0/1]{lang="SV"}*]{#struct_0_52071_x1881_x193480852}*[接口发送]{style="font-family:宋体"}[PADI]{lang="SV"}[报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[报文长度为]{style="font-family:宋体"}[16]{lang="SV"}[。版本为]{style="font-family:宋体"}[0x01]{lang="SV"}[，]{style="font-family:宋体"}[类型为]{style="font-family:宋体"}[0x01]{lang="SV"}[，]{style="font-family:宋体"}[SESSION_ID]{lang="IT"}[为]{style="font-family:宋体"}[0]{lang="SV"}*

[ ]{lang="SV"}

[[\# ]{lang="SV"}]{#struct_0_52071_x1881_x1687017944}[打开]{style="font-family:宋体"}[PPPoE Client]{lang="SV"}[在]{style="font-family:宋体"}[session]{lang="SV"}[阶段的数据调试信息开关。接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[收到一个长度错误的]{style="font-family:宋体"}[PPPoE]{lang="SV"}[报文时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging pppoe-client data]{lang="EN-US"}]{#struct_0_52071_x1881_1752949975}

[\*Jun 23 15:50:40:899 2011 Sysname PPPOEC/7/DATA: -MDC=1; Dropped a PPPoE packet of incorrect length on interface GigabitEthernet1/0/1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_52071_x1881_x1748020181}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上丢弃一个长度错误的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
