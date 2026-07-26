::: {#2015026023 .myid}
[]{#_Toc404784994}[]{#struct_0_17774_11526_1063468317}

**HDLC \-- HDLC调试命令 \-- debugging hdlc**

------------------------------------------------------------------------

[**[debugging ]{lang="EN-US"}[hdlc]{lang="EN-US"}**]{#struct_0_17774_11526_1332449732}[命令用来打开]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[undo debugging ]{lang="EN-US"}[hdlc]{lang="EN-US"}**]{#struct_0_17774_11526_x16104235}[命令用来关闭]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17774_11526_863940207}

[**[debugging hdlc ]{lang="EN-US"}**[{ **all** \| **event** \| { **ip** \| **ipv6** \| **isis** \| **keepalive** \| **mpls** } { **in** \| **in-out** \| **out** } } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_17774_11526_x901900430}

[**[undo debugging hdlc]{lang="EN-US"}**[ { **all** \| **event** \| { **ip** \| **ipv6** \| **isis** \| **keepalive** \| **mpls** } { **in** \| **in-out** \| **out** } } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_17774_11526_x240455226}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17774_11526_x1623520879}

[[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_1332449733}[调试信息开关处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17774_11526_x1242975361}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17774_11526_118046724}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17774_11526_x216287421}

[[network-admin]{lang="EN-US"}]{#struct_0_17774_11526_600327828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17774_11526_466266883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17774_11526_866359987}

[**[all]{lang="EN-US"}**]{#struct_0_17774_11526_56179921}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17774_11526_x1571484761}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_17774_11526_x1533624822}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_17774_11526_x498885247}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[isis]{lang="EN-US"}**]{#struct_0_17774_11526_x675969930}[：表示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[keepalive]{lang="EN-US"}**]{#struct_0_17774_11526_x1842288271}[：表示]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[mpls]{lang="EN-US"}**]{#struct_0_17774_11526_x216352957}[：表示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[in]{lang="EN-US"}**]{#struct_0_17774_11526_1054599435}[：表示报文方向为入方向。]{style="font-family:宋体"}

[**[in-out]{lang="EN-US"}**]{#struct_0_17774_11526_x898083670}[：表示包括入]{style="font-family:宋体"}[/]{lang="EN-US"}[出两个方向的报文。]{style="font-family:宋体"}

[**[out]{lang="EN-US"}**]{#struct_0_17774_11526_188204909}[：表示报文方向为出方向。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17774_11526_844187436}[：表示指定接口的调试信息开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17774_11526_x595162115}

[]{#struct_0_17774_11526_x658393304}[[表1-1 ]{lang="EN-US"}[debugging ]{lang="EN-US"}[hdlc event]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1146911525}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_x785804170}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_x215894205}

[[Interface *interface-name* keepalive timer started, timer ID = *id*.]{lang="EN-US"}]{#struct_0_17774_11526_329295245}

[[接口的定时器启动]{style="font-family:宋体"}]{#struct_0_17774_11526_1500669395}

[[Interface *interface-name* keepalive timer stopped, timer ID = *id*.]{lang="EN-US"}]{#struct_0_17774_11526_x281461469}

[[接口的定时器停止]{style="font-family:宋体"}]{#struct_0_17774_11526_315406731}

[[Interface *interface-name* keepalive timer reset, timer ID = *id*.]{lang="EN-US"}]{#struct_0_17774_11526_546171985}

[[接口的定时器重置]{style="font-family:宋体"}]{#struct_0_17774_11526_x51571921}

[[Interface *interface-name* keepalive timer expired, timer ID = *id*.]{lang="EN-US"}]{#struct_0_17774_11526_x412810501}

[[接口的定时器超时]{style="font-family:宋体"}]{#struct_0_17774_11526_x215959741}

[[Interface *interface-name* keepalive function is disabled, and the frame is dropped.]{lang="EN-US"}]{#struct_0_17774_11526_x1639578821}

[[关闭接口的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_17774_11526_2009795322}[机制，丢弃帧]{style="font-family:宋体"}

[[Interface *interface-name* failed to send keepalive packets.]{lang="EN-US"}]{#struct_0_17774_11526_423976531}

[[接口的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_17774_11526_x204424843}[报文发送失败]{style="font-family:宋体"}

[[Loopback is detected on interface *interface-name*.]{lang="EN-US"}]{#struct_0_17774_11526_647742418}

[[在接口上探测到环回]{style="font-family:宋体"}]{#struct_0_17774_11526_1349665451}

[[Interface *interface-name* added adjacency table.]{lang="EN-US"}]{#struct_0_17774_11526_365815230}

[[添加接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_17774_11526_1968255801}[邻接表]{style="font-family:宋体"}

[[Interface *interface-name* added IPv6 adjacency table.]{lang="EN-US"}]{#struct_0_17774_11526_x1716020459}

[[添加接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_17774_11526_x287198385}[邻接表]{style="font-family:宋体"}

[[Interface *interface-name* deleted adjacency table.]{lang="EN-US"}]{#struct_0_17774_11526_357146503}

[[删除接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_17774_11526_1349599915}[邻接表]{style="font-family:宋体"}

[[Interface *interface-name* deleted IPv6 adjacency table.]{lang="EN-US"}]{#struct_0_17774_11526_x1318232921}

[[删除接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_17774_11526_x1207799665}[邻接表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ]{lang="EN-US"}[hdlc ip]{lang="EN-US"}]{#struct_0_17774_11526_732352420}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1147776378}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_1451050827}

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_x830397165}

[[Interface *interface-name* received an IP packet.]{lang="EN-US"}]{#struct_0_17774_11526_x557939609}

[[接口收到一个]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17774_11526_1349534379}[报文]{style="font-family:宋体"}

[[Interface *interface-name* sent an IP packet.]{lang="EN-US"}]{#struct_0_17774_11526_725643458}

[[接口发送一个]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17774_11526_1635530803}[报文]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_17774_11526_x159312777}

[[报文长度]{style="font-family:宋体"}]{#struct_0_17774_11526_x1720317703}

[[Address]{lang="EN-US"}]{#struct_0_17774_11526_1292669789}

[[报文]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_x1989853440}[地址，]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[地址为单播地址]{style="font-family:宋体"}[0x0F]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ]{lang="EN-US"}[hdlc ipv6]{lang="EN-US"}]{#struct_0_17774_11526_1080656904}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1142725170}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_1349468843}

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_x1682315226}

[[Interface *interface-name* received an IPv6 packet.]{lang="EN-US"}]{#struct_0_17774_11526_x1613688938}

[[接口收到一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_17774_11526_93597533}[报文]{style="font-family:宋体"}

[[Interface *interface-name* sent an IPv6 packet.]{lang="EN-US"}]{#struct_0_17774_11526_413317226}

[[接口发送一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_17774_11526_2089019627}[报文]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_17774_11526_1887451830}

[[报文长度]{style="font-family:宋体"}]{#struct_0_17774_11526_x242422902}

[[Address]{lang="EN-US"}]{#struct_0_17774_11526_1349927595}

[[报文]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_1150417841}[地址，]{style="font-family:宋体"}[ IPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[地址为单播地址]{style="font-family:宋体"}[0x0F]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging ]{lang="EN-US"}[hdlc isis]{lang="EN-US"}]{#struct_0_17774_11526_820966476}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1141729555}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_1094389667}

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_1128283995}

[[Interface *interface-name* received an ISIS packet.]{lang="EN-US"}]{#struct_0_17774_11526_x483356182}

[[接口收到一个]{style="font-family:宋体"}[ISIS]{lang="EN-US"}]{#struct_0_17774_11526_1605971399}[报文]{style="font-family:宋体"}

[[Interface *interface-name* sent an ISIS packet.]{lang="EN-US"}]{#struct_0_17774_11526_1128961892}

[[接口发送一个]{style="font-family:宋体"}[ISIS]{lang="EN-US"}]{#struct_0_17774_11526_1349862059}[报文]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_17774_11526_x436119141}

[[报文长度]{style="font-family:宋体"}]{#struct_0_17774_11526_958075465}

[[Address]{lang="EN-US"}]{#struct_0_17774_11526_x1599510625}

[[报文]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_x75939441}[地址，]{style="font-family:宋体"}[ISIS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[地址为组播地址]{style="font-family:宋体"}[0x8F]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ]{lang="EN-US"}[hdlc keepalive]{lang="EN-US"}]{#struct_0_17774_11526_x1336991782}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1144928372}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_132197262}

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_383196141}

[[Interface *interface-name* received a KEEPALIVE packet.]{lang="EN-US"}]{#struct_0_17774_11526_1349796523}

[[接口收到一个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_17774_11526_x1595701291}[报文]{style="font-family:宋体"}

[[Interface *interface-name* sent a KEEPALIVE packet.]{lang="EN-US"}]{#struct_0_17774_11526_203766036}

[[接口发送一个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_17774_11526_x673576738}[报文]{style="font-family:宋体"}

[[Interface *interface-name* received a KEEPALIVE_REQ packet.]{lang="EN-US"}]{#struct_0_17774_11526_2077605378}

[[接口收到一个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_17774_11526_x1625913700}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name* sent a KEEPALIVE_REQ packet.]{lang="EN-US"}]{#struct_0_17774_11526_x31196844}

[[接口发送一个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_17774_11526_1349730987}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name* received an ADDR_REQ packet.]{lang="EN-US"}]{#struct_0_17774_11526_x97369235}

[[接口收到一个地址请求报文]{style="font-family:宋体"}]{#struct_0_17774_11526_x290919430}

[[Interface *interface-name* received an ADDR_REPLY packet.]{lang="EN-US"}]{#struct_0_17774_11526_x681833194}

[[接口收到一个地址应答报文]{style="font-family:宋体"}]{#struct_0_17774_11526_1594544347}

[[Interface *interface-name* sent an ADDR_REPLY packet. ]{lang="EN-US"}]{#struct_0_17774_11526_x946132367}

[[接口发送一个地址应答报文]{style="font-family:宋体"}]{#struct_0_17774_11526_1350189739}

[[Length]{lang="EN-US"}]{#struct_0_17774_11526_x1356376786}

[[报文长度]{style="font-family:宋体"}]{#struct_0_17774_11526_1277263343}

[[Address]{lang="EN-US"}]{#struct_0_17774_11526_1359522280}

[[报文]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_1241987904}[地址，]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[地址为组播地址]{style="font-family:宋体"}[0x8F]{lang="EN-US"}

[[RemoteSeq]{lang="EN-US"}]{#struct_0_17774_11526_x818414680}

[[远端当前协议报文序号]{style="font-family:宋体"}]{#struct_0_17774_11526_1350124203}

[[AckedLocalSeq]{lang="EN-US"}]{#struct_0_17774_11526_1423987334}

[[远端保存的本地上次协议报文序号]{style="font-family:宋体"}]{#struct_0_17774_11526_x1240220131}

[[LocalSeq]{lang="EN-US"}]{#struct_0_17774_11526_674121663}

[[本地协议报文序号]{style="font-family:宋体"}]{#struct_0_17774_11526_x545166739}

[[AckedRemoteSeq]{lang="EN-US"}]{#struct_0_17774_11526_x658352855}

[[本地保存的远端协议报文序号]{style="font-family:宋体"}]{#struct_0_17774_11526_1349665452}

[[line UP]{lang="EN-US"}]{#struct_0_17774_11526_365618622}

[[链路]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_17774_11526_1737449675}

[[line DOWN]{lang="EN-US"}]{#struct_0_17774_11526_x2102442798}

[[链路]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_17774_11526_x894164583}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging ]{lang="EN-US"}[hdlc mpls]{lang="EN-US"}]{#struct_0_17774_11526_1349599916}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1173362071}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_x1318298457}

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_90367172}

[[Interface *interface-name* received an MPLS packet.]{lang="EN-US"}]{#struct_0_17774_11526_1662756980}

[[接口收到一个]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_17774_11526_x1543500012}[报文]{style="font-family:宋体"}

[[Interface *interface-name* sent an MPLS packet.]{lang="EN-US"}]{#struct_0_17774_11526_1857215235}

[[接口发送一个]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_17774_11526_1140973129}[报文]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_17774_11526_x1720332782}

[[报文长度]{style="font-family:宋体"}]{#struct_0_17774_11526_1349534380}

[[Address]{lang="EN-US"}]{#struct_0_17774_11526_725184719}

[[报文]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_857332813}[地址，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[地址为单播地址]{style="font-family:宋体"}[0x0F]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17774_11526_2069342743}

[[Router A]{lang="EN-US"}]{#struct_0_17774_11526_x774033446}[的接口和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的接口上均封装]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[协议，且]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[链路]{style="font-family:宋体"}[UP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_x1002605007}[打开]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[的事件调试信息开关，可查看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterB\> debugging hdlc event]{lang="EN-US"}]{#struct_0_17774_11526_419643424}

[\*Jan 30 17:12:27:141 2012 RouterB HDLC/7/EVENT: -MDC=1; Interface Serial2/1/0 keepalive timer expired, timer ID = 354.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x1976691042}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_x970767638}[打开]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文调试信息开关，在接口下配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，并从]{style="font-family:宋体"}[Router A ping Router B]{lang="EN-US"}[，]{style="font-family:宋体"}[可查看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterB\> debugging hdlc ip in]{lang="EN-US"}]{#struct_0_17774_11526_1349468844}

[\*Jan 31 09:20:56:093 2012 RouterB HDLC/7/IP: -MDC=1; Interface Serial2/1/0 received an IP packet. Length: 88, Address: 0x0F]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x1681987546}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[收到]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_x620924019}[打开]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文调试信息开关，在接口下配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，并从]{style="font-family:宋体"}[Router A ping Router B]{lang="EN-US"}[，]{style="font-family:宋体"}[可查看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterB\> debugging hdlc ipv6 in]{lang="EN-US"}]{#struct_0_17774_11526_718155599}

[\*Jan 31 09:28:23:552 2012 RouterB HDLC/7/IPv6: -MDC=1; Interface Serial2/1/0 received an IPv6 packet. Length: 68, Address: 0x0F]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x539450279}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[收到]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_x1744575847}[打开]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[的]{style="font-family:宋体"}[ISIS]{lang="EN-US"}[报文调试信息开关，]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[两端都配置]{style="font-family:宋体"}[ISIS]{lang="EN-US"}[功能后，可查看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterB\> debugging hdlc isis in-out]{lang="EN-US"}]{#struct_0_17774_11526_x1192766042}

[\*Jan 31 09:55:49:015 2012 RouterB HDLC/7/ISIS: -MDC=1; Interface Serial2/1/0 received an ISIS packet. Length: 46, Address: 0x8F]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x57892936}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[收到]{style="font-family:宋体"}[ISIS]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jan 31 09:55:49:843 2012 RouterB HDLC/7/ISIS: -MDC=1; Interface Serial2/1/0 sent an ISIS packet. Length: 40, Address: 0x8F]{lang="EN-US"}]{#struct_0_17774_11526_x309925522}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_1349927596}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[发送]{style="font-family:宋体"}[ISIS]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_1150221233}[打开]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文调试信息开关，由于当前链路]{style="font-family:宋体"}[UP]{lang="EN-US"}[，]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[机制已启动，可查看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterB\> debugging hdlc keepalive in-out]{lang="EN-US"}]{#struct_0_17774_11526_1172353205}

[\*Jan 30 17:18:42:328 2012 RouterB HDLC/7/KEEPALIVE: -MDC=1; Interface Serial2/1/0 received a KEEPALIVE packet. Length: 22, Address: 0x8F]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x1229542971}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jan 30 17:18:42:328 2012 RouterB HDLC/7/KEEPALIVE: -MDC=1; Interface Serial2/1/0 received a KEEPALIVE_REQ packet. Length: 18, RemoteSeq: 830, AckedLocalSeq: 804]{lang="EN-US"}]{#struct_0_17774_11526_986782000}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_689205852}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Jan 30 17:18:48:610 2012 RouterB HDLC/7/KEEPALIVE: -MDC=1; Interface Serial2/1/0 sent ]{lang="EN-US"}]{#struct_0_17774_11526_995399250}

[a KEEPALIVE_REQ packet. Length: 18, LocalSeq: 804, AckedRemoteSeq: 830, line UP]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x1187161396}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Jan 30 17:18:48:610 2012 RouterB HDLC/7/KEEPALIVE: -MDC=1; Interface Serial2/1/0 sent a ]{lang="EN-US"}]{#struct_0_17774_11526_1349862060}

[KEEPALIVE packet. Length: 22, Address: 0x8F]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x435660386}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_x441326883}[打开]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文调试信息开关，]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[两端都配置]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[功能后，可查看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterB\> debugging hdlc mpls in]{lang="EN-US"}]{#struct_0_17774_11526_x1338616493}

[\*Jan 31 10:02:31:432 2012 RouterB HDLC/7/MPLS: -MDC=1; Interface Serial2/1/0 received an MPLS packet. Length: 92, Address: 0x0F]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x1850706088}*[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[收到]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#-766042994 .myid}
[]{#_Toc404784996}[]{#struct_0_17774_11526_1334258447}[]{#_Toc355686465}[]{#_Toc238526679}[]{#_Toc204610074}

**HDLC \-- HDLC链路捆绑调试命令 \-- debugging bundle**

------------------------------------------------------------------------

[**[debugging bundle]{lang="NO-BOK"}**]{#struct_0_17774_11526_1782495801}[命令用来打开]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口调试信息开关。]{style="font-family:宋体"}

[**[undo debugging bundle]{lang="NO-BOK"}**]{#struct_0_17774_11526_950112696}[命令用来关闭]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17774_11526_1334258446}

[**[debugging bundle]{lang="NO-BOK"}**]{#struct_0_17774_11526_1782561337}[ { **all** \| **error** \| **event** \| **packet** } \[ **hdlc-bundle** *bundle-id* \]]{lang="NO-BOK"}

[**[undo debugging bundle]{lang="NO-BOK"}**]{#struct_0_17774_11526_x1521095830}[ { **all** \| **error** \| **event** \| **packet** } \[ **hdlc-bundle** *bundle-id* \]]{lang="NO-BOK"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17774_11526_950112697}

[[HDLC]{lang="NO-BOK"}]{#struct_0_17774_11526_1334258445}[捆绑接口]{style="font-family:宋体"}[调试信息开关处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17774_11526_1782626873}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17774_11526_1267621984}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17774_11526_950112694}

[[network-admin]{lang="NO-BOK"}]{#struct_0_17774_11526_1334258444}

[[mdc-admin]{lang="NO-BOK"}]{#struct_0_17774_11526_1782692409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17774_11526_x278557191}

[**[all]{lang="DE"}**]{#struct_0_17774_11526_950112695}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="DE"}**]{#struct_0_17774_11526_1334258443}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="DE"}**]{#struct_0_17774_11526_1782233657}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="DE"}**]{#struct_0_17774_11526_x1483013347}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[报文调试信息开关。]{style="font-family:宋体"}

[**[hdlc-bundle]{lang="NO-BOK"}**]{#struct_0_17774_11526_x392738771}[ *bundle-id*]{lang="NO-BOK"}[：显示指定]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口的调试信息。]{style="font-family:宋体"}*[bundle-id]{lang="DE"}*[表示]{style="font-family:宋体"}[HDLC]{lang="DE"}[捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定本参数，将显示所有]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口的调试信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17774_11526_950112708}

[]{#_Toc130718926}[[表1-7 ]{lang="EN-US"}[debugging bundle error]{lang="EN-US"}]{#struct_0_17774_11526_x658792533}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2134393472}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_1560938866}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_950112709}

[[Failed to execute the *operation* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_17774_11526_x658792534}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17774_11526_x1006202436}[上执行]{style="font-family:宋体"}*[operation]{lang="EN-US"}*[操作失败，]{style="font-family:宋体"}*[operation]{lang="EN-US"}*[的取值及其含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17774_11526_x1271482973}[：接口激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deactive]{lang="EN-US"}]{#struct_0_17774_11526_1169979683}[：接口去激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create]{lang="EN-US"}]{#struct_0_17774_11526_x1006202435}[：接口创建]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_17774_11526_x868198446}[：接口删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[link_up]{lang="EN-US"}]{#struct_0_17774_11526_x1006202438}[：接口链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[link_down]{lang="EN-US"}]{#struct_0_17774_11526_247546801}[：接口链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[shutdown]{lang="EN-US"}]{#struct_0_17774_11526_x1006202437}[：接口]{lang="EN-US" style="font-family:宋体"}[shutdown]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[undo_shutdown]{lang="EN-US"}]{#struct_0_17774_11526_294600968}[：接口]{lang="EN-US" style="font-family:宋体"}[undo shutdown]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[speed_change]{lang="EN-US"}]{#struct_0_17774_11526_x80785216}[：接口速率变化]{lang="EN-US" style="font-family:宋体"}

[[Failed to block member *interface-name.*]{lang="EN-US"}]{#struct_0_17774_11526_x1006202440}

[[阻塞成员接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17774_11526_x109142311}[失败]{style="font-family:宋体"}

[[Failed to unblock member *interface-name.*]{lang="EN-US"}]{#struct_0_17774_11526_x1006202439}

[[去阻塞成员接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17774_11526_1813630742}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging bundle event]{lang="EN-US"}]{#struct_0_17774_11526_351339743}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1888145856}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_x1006202442}

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_1053657103}

[[Received event *event* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_17774_11526_x1006202441}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17774_11526_1456941630}[收到]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17774_11526_x861491378}[：接口激活事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deactive]{lang="EN-US"}]{#struct_0_17774_11526_x1006202428}[：接口去激活事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create]{lang="EN-US"}]{#struct_0_17774_11526_247481265}[：接口创建事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_17774_11526_x1006202427}[：接口删除事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[link_up]{lang="EN-US"}]{#struct_0_17774_11526_294535432}[：接口链路]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[link_down]{lang="EN-US"}]{#struct_0_17774_11526_500524104}[：接口链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[shutdown]{lang="EN-US"}]{#struct_0_17774_11526_1712624060}[：接口]{lang="EN-US" style="font-family:宋体"}[shutdown]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[undo_shutdown]{lang="EN-US"}]{#struct_0_17774_11526_x1585391800}[：接口]{lang="EN-US" style="font-family:宋体"}[undo shutdown]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[Received a speed-change event on interface *interface-name* (new speed: *speed*).]{lang="EN-US"}]{#struct_0_17774_11526_1712624061}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17774_11526_x1585326264}[速率变化，新速率为]{style="font-family:宋体"}*[speed]{lang="EN-US"}*

[[Interface *interface-name* started rechoosing Selected interfaces.]{lang="EN-US"}]{#struct_0_17774_11526_1712624058}

[]{#struct_0_17774_11526_x1584867509}[[HDLC]{lang="EN-US"}]{#OLE_LINK2}[捆绑接口]{style="font-family:
  宋体"}*[interface-name]{lang="EN-US"}*[开始重新选择选中接口]{style="font-family:宋体"}

[[Interface *interface-name* succeeded in rechoosing Selected interfaces and sent the rechoosing result to the kernel.]{lang="EN-US"}]{#struct_0_17774_11526_1833020974}

[[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_1712624059}[捆绑接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[重新选择选中接口成功，开始把重选结果下内核]{style="font-family:宋体"}

[[Succeeded in blocking member *interface-name*.]{lang="EN-US"}]{#struct_0_17774_11526_x1584801973}

[[阻塞成员接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17774_11526_1712624056}[成功]{style="font-family:宋体"}

[[Succeeded in unblocking member *interface-name*.]{lang="EN-US"}]{#struct_0_17774_11526_x1585260725}

[[去阻塞成员接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17774_11526_1712624057}[成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging bundle packet]{lang="EN-US"}]{#struct_0_17774_11526_x1585195189}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1882680628}[[字段]{style="font-family:黑体"}]{#struct_0_17774_11526_2670582}

[[描述]{style="font-family:黑体"}]{#struct_0_17774_11526_1712624054}

[*[bundle-name]{lang="EN-US"}*[ sent a packet out of member *interface-name* (packet length: *length*). *packet context*]{lang="EN-US"}]{#struct_0_17774_11526_x1585129653}

[[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_211620440}[捆绑接口]{style="font-family:宋体"}*[bundle-name]{lang="EN-US"}*[从成员接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[发送报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[。报文内容为]{style="font-family:宋体"}*[packet context]{lang="EN-US"}*

[*[bundle-name]{lang="EN-US"}*[ received a packet on member *interface-name* (packet length: *length*). *packet context*]{lang="EN-US"}]{#struct_0_17774_11526_1712624055}

[[HDLC]{lang="EN-US"}]{#struct_0_17774_11526_x1585064117}[捆绑接口]{style="font-family:宋体"}*[bundle-name]{lang="EN-US"}*[从成员接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[接收报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[。报文内容为]{style="font-family:宋体"}*[packet context]{lang="EN-US"}*

[[Sent a packet to slot *slot-num* cpu *cpu-id*.]{lang="EN-US"}]{#struct_0_17774_11526_197468159}

[[发送一个报文到指定板的指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_17774_11526_1712624068}[，目的板号为]{style="font-family:宋体"}*[slot-num]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号为]{style="font-family:宋体"}*[cpu-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17774_11526_x1584867512}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_x89227791}[打开]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口错误调试信息开关。当]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[POS2/2/1]{lang="EN-US"}[变为选中成员接口下驱动去阻塞失败时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bundle error]{lang="EN-US"}]{#struct_0_17774_11526_1712624069}

[\*Jan 30 17:18:48:610 2012 Sysname BUNDLE/7/ERROR: -MDC=1; Failed to unblock member POS2/2/1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17774_11526_x1584801976}*[去阻塞成员接口]{style="font-family:宋体"}[POS2/2/1]{lang="EN-US"}[失败]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_x1739412009}[打开]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:宋体"}[1]{lang="DE"}[的事件调试信息开关。将]{style="font-family:
宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口]{style="font-family:
宋体"}[1 **shutdown**]{lang="DE"}[时会输出下列调试信息。]{style="font-family:
宋体"}

[[\<Sysname\> debugging bundle event hdlc-bundle 1]{lang="EN-US"}]{#struct_0_17774_11526_x1966024441}

[\*Jan 30 18:18:48:610 2012 Sysname BUNDLE/7/EVENT: -MDC=1; Received event shutdown on interface HDLC-bundle1.]{lang="EN-US"}

[*[// HDLC]{lang="EN-US"}*]{#struct_0_17774_11526_x1442703834}*[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[发生]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17774_11526_x243691076}[设备上配置了]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑]{style="font-family:宋体"}[1]{lang="EN-US"}[中有选中成员接口]{style="font-family:宋体"}[POS2/2/1]{lang="EN-US"}[。打开]{style="font-family:宋体"}[HDLC]{lang="NO-BOK"}[捆绑接口报文调试信息开关。当在设备上]{style="font-family:宋体"}[ping]{lang="DE"}[其他设备时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging bundle packet hdlc-bundle 1]{lang="EN-US"}]{#struct_0_17774_11526_x1786345940}

[\*Jan 30 19:18:48:610 2012 Sysname BUNDLE/7/PACKET: -MDC=1; HDLC-bundle1 sent a packet out of member POS2/2/1 (packet length: 88).]{lang="EN-US"}

[    0f 00 08 00 45 00 00 54 00 20 00 00 ff 01 b7 84]{lang="EN-US"}

[    01 01 01 01 01 01 01 02 08 00 74 35 08 00 01 00]{lang="EN-US"}

[    da 87 76 00 00 00 00 00 00 01 02 03 04 05 06 07]{lang="EN-US"}

[    08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17]{lang="EN-US"}

[    18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25 26 27]{lang="EN-US"}

[    28 29 2a 2b 2c 2d 2e 2f]{lang="EN-US"}

[*[// HDLC]{lang="EN-US"}*]{#struct_0_17774_11526_632008101}*[捆绑接口]{style="font-family:宋体"}[1]{lang="EN-US"}[发送报文，报文的长度为]{style="font-family:宋体"}[88]{lang="EN-US"}[，发送报文的成员接口为]{style="font-family:宋体"}[POS2/2/1]{lang="EN-US"}*

[ ]{lang="EN-US"}
