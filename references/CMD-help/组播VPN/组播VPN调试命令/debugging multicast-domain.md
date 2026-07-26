::: {#-1487042254 .myid}
[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}[]{#_Toc404789825}[]{#struct_0_75372_x1062_x459196799}[]{#_Toc327804447}

**组播VPN \-- 组播VPN调试命令 \-- debugging multicast-domain**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_75372_x1062_160642653}

[**[debugging]{lang="EN-US"}**[ **multicast-domain** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **event** \[ *advanced-acl-number* \] \| **packet** \| **timer** }]{lang="EN-US"}]{#struct_0_75372_x1062_x197981026}

[**[undo]{lang="EN-US"}**[ **debugging** **multicast-domain** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **event** \| **packet** \| **timer** }]{lang="EN-US"}]{#struct_0_75372_x1062_1944236525}

[[【视图】]{style="font-family:黑体"}]{#struct_0_75372_x1062_1614252462}

[[用户视图]{style="font-family:宋体"}]{#struct_0_75372_x1062_474225714}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_75372_x1062_84862985}

[[network-admin]{lang="EN-US"}]{#struct_0_75372_x1062_852673448}

[[mdc-admin]{lang="EN-US"}]{#struct_0_75372_x1062_x2081588495}

[[【参数】]{style="font-family:黑体"}]{#struct_0_75372_x1062_13276893}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_75372_x1062_710032788}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_75372_x1062_1608280028}[：表示]{style="font-family:宋体"}[MD]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_75372_x1062_403645481}[：表示]{style="font-family:宋体"}[MD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[*[advanced-acl-number]{lang="EN-US"}*]{#struct_0_75372_x1062_1709911601}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_75372_x1062_1614580142}[：表示]{style="font-family:宋体"}[MD]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_75372_x1062_x1113914243}[：表示]{style="font-family:宋体"}[MD]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_75372_x1062_1739602479}

[**[debugging]{lang="EN-US"}**[ **multicast-domain**]{lang="EN-US"}]{#struct_0_75372_x1062_x1872626167}[命令用来打开]{style="font-family:宋体"}[MD]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **multicast-domain**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[MD]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_75372_x1062_x86635358}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging multicast-domain event]{lang="EN-US"}]{#struct_0_75372_x1062_x1691910468}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1068671701}[[字段]{style="font-family:黑体"}]{#struct_0_75372_x1062_x1127459823}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_75372_x1062_1735613093}

[[create msg]{lang="EN-US"}]{#struct_0_75372_x1062_1614645678}

[[MTI]{lang="EN-US"}]{#struct_0_75372_x1062_853041838}[接口创建消息]{style="font-family:宋体"}

[[destroy msg]{lang="EN-US"}]{#struct_0_75372_x1062_x2006789361}

[[MTI]{lang="EN-US"}]{#struct_0_75372_x1062_1054108175}[接口删除消息]{style="font-family:宋体"}

[[up msg]{lang="EN-US"}]{#struct_0_75372_x1062_x870463027}

[[MTI]{lang="EN-US"}]{#struct_0_75372_x1062_x1170180324}[接口生效消息]{style="font-family:宋体"}

[[down msg]{lang="EN-US"}]{#struct_0_75372_x1062_x189298606}

[[MTI]{lang="EN-US"}]{#struct_0_75372_x1062_1614449070}[接口失效消息]{style="font-family:宋体"}

[[join]{lang="EN-US"}]{#struct_0_75372_x1062_x1498139428}

[[加入]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_75372_x1062_x1038535060}[组消息]{style="font-family:宋体"}

[[prune]{lang="EN-US"}]{#struct_0_75372_x1062_x1752515108}

[[离开]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_75372_x1062_x1232223947}[组消息]{style="font-family:宋体"}

[[smooth]{lang="EN-US"}]{#struct_0_75372_x1062_124388251}

[[MD]{lang="EN-US"}]{#struct_0_75372_x1062_1614514606}[数据平滑]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging multicast-domain packet]{lang="EN-US"}]{#struct_0_75372_x1062_x723593491}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1072453829}[[字段]{style="font-family:黑体"}]{#struct_0_75372_x1062_x41722096}

[[描述]{style="font-family:黑体"}]{#struct_0_75372_x1062_1243599349}

[[send/receive]{lang="EN-US"}]{#struct_0_75372_x1062_144333986}

[[发送]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_75372_x1062_1206672746}[接收]{style="font-family:宋体"}[MD]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[MDT-Join packet]{lang="EN-US"}]{#struct_0_75372_x1062_x1862911378}

[[MD]{lang="EN-US"}]{#struct_0_75372_x1062_1614842286}[切换报文（由切换消息"]{style="font-family:宋体"}[MDT Join-TLV]{lang="EN-US"}["构成）]{style="font-family:宋体"}

[[from/to]{lang="EN-US"}]{#struct_0_75372_x1062_x670229778}

[[报文的源]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_75372_x1062_1889658980}[目的地址]{style="font-family:宋体"}

[[type]{lang="EN-US"}]{#struct_0_75372_x1062_x773139872}

[[切换消息中的类型，具体请参见]{style="font-family:宋体"}[RFC 6037]{lang="EN-US"}]{#struct_0_75372_x1062_x4724603}

[[(1.1.1.1, 225.1.1.1) -\> 239.1.1.1]{lang="EN-US"}]{#struct_0_75372_x1062_x1805638718}

[[切换消息中的私网（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_75372_x1062_1614907822}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）地址及公网]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[ignoring the packet]{lang="EN-US"}]{#struct_0_75372_x1062_2065528986}

[[忽略报文]{style="font-family:宋体"}]{#struct_0_75372_x1062_x6053234}

[[ignoring this MDT-Join]{lang="EN-US"}]{#struct_0_75372_x1062_x1605394935}

[[忽略该]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_75372_x1062_x2081727567}[切换报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging multicast-domain timer]{lang="EN-US"}]{#struct_0_75372_x1062_x1931935054}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1069973237}[[字段]{style="font-family:黑体"}]{#struct_0_75372_x1062_1614317999}

[[描述]{style="font-family:黑体"}]{#struct_0_75372_x1062_107641305}

[[reconnect]{lang="EN-US"}]{#struct_0_75372_x1062_x852186855}

[[重新连接定时器]{style="font-family:宋体"}]{#struct_0_75372_x1062_251803233}

[[smooth]{lang="EN-US"}]{#struct_0_75372_x1062_x1837756566}

[[平滑相关定时器]{style="font-family:宋体"}]{#struct_0_75372_x1062_x1463651240}

[[reflush]{lang="EN-US"}]{#struct_0_75372_x1062_475152138}

[[失败重刷定时器（如]{style="font-family:宋体"}[MTI]{lang="EN-US"}]{#struct_0_75372_x1062_1614383535}[接口创建失败等）]{style="font-family:宋体"}

[[memory]{lang="EN-US"}]{#struct_0_75372_x1062_53585779}

[[内存门限恢复相关定时器]{style="font-family:宋体"}]{#struct_0_75372_x1062_x1167072104}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_75372_x1062_x654041836}

[[\# ]{lang="EN-US"}]{#struct_0_75372_x1062_346979596}[打开]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[的]{style="font-family:宋体"}[MD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging multicast-domain vpn-instance mvpn event]{lang="EN-US"}]{#struct_0_75372_x1062_439456374}

[\*Nov  6 14:03:00:840 2012 Sysname MD/7/EVENT: -MDC=1; (mvpn): Send MTunnel0 create msg to IPv4 MBR. (D04211)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_75372_x1062_x1968708096}*[向]{style="font-family:宋体"}[IPv4 MBR]{lang="EN-US"}[发送]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[内]{style="font-family:宋体"}[MTI0]{lang="EN-US"}[接口的创建消息]{style="font-family:宋体"}*

[[\*Nov  6 14:03:11:286 2012 Sysname MD/7/EVENT: -MDC=1; (mvpn): Send MTunnel0 up msg to IPv4 MBR. (D04224)]{lang="EN-US"}]{#struct_0_75372_x1062_1614186927}

[*[// ]{lang="EN-US"}*]{#struct_0_75372_x1062_x1480790467}*[向]{style="font-family:宋体"}[IPv4 MBR]{lang="EN-US"}[发送]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[内]{style="font-family:宋体"}[MTI0]{lang="EN-US"}[接口的生效消息]{style="font-family:宋体"}*

[[\*Nov  6 14:03:11:286 2012 Sysname MD/7/EVENT: -MDC=1; (mvpn): Send MD join (\*, 239.1.1.1) on MTunnel0 to IPv4 MBR. (D04229)]{lang="EN-US"}]{#struct_0_75372_x1062_1202779163}

[*[// ]{lang="EN-US"}*]{#struct_0_75372_x1062_702233858}*[向]{style="font-family:宋体"}[IPv4 MBR]{lang="EN-US"}[发送]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[内]{style="font-family:宋体"}[MTI0]{lang="EN-US"}[接口上的加入]{style="font-family:宋体"}[MD]{lang="EN-US"}[组（]{style="font-family:宋体"}[\*, 239.1.1.1]{lang="EN-US"}[）的消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_75372_x1062_1364901593}[打开]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[的]{style="font-family:宋体"}[MD]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging multicast-domain vpn-instance mvpn packet]{lang="EN-US"}]{#struct_0_75372_x1062_328058697}

[\*Jan 21 12:42:03:480 2013 Sysname MD/7/PACKET: -MDC=1; (mvpn): Send a packet from 1.1.0.1 to 224.0.0.13, length: 16. (D11511)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_75372_x1062_x477276022}*[从]{style="font-family:宋体"}[1.1.0.1]{lang="EN-US"}[向]{style="font-family:宋体"}[224.0.0.13]{lang="EN-US"}[发送了一个长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节的]{style="font-family:宋体"}[MD]{lang="EN-US"}[切换报文]{style="font-family:宋体"}*

[[\*Jan 21 13:12:49:026 2013 Sysname MD/7/PACKET: -MDC=1; (mvpn): Receive a packet from 1.1.0.1 to 224.0.0.13, length: 16. (D111858)]{lang="EN-US"}]{#struct_0_75372_x1062_408993149}

[*[// ]{lang="EN-US"}*]{#struct_0_75372_x1062_1858131384}*[收到了一个从]{style="font-family:宋体"}[1.1.0.1]{lang="EN-US"}[发向]{style="font-family:宋体"}[224.0.0.13]{lang="EN-US"}[的、长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节的]{style="font-family:宋体"}[MD]{lang="EN-US"}[切换报文]{style="font-family:宋体"}*

[[\*Jan 21 12:42:03:480 2013 Sysname MD/7/PACKET: -MDC=1; (mvpn): Type 1, length 16, (7.11.0.7, 225.1.1.1) -\> 239.1.2.0 (D11409)]{lang="EN-US"}]{#struct_0_75372_x1062_1614252463}

[*[// ]{lang="EN-US"}*]{#struct_0_75372_x1062_474291250}*[切换消息的类型为]{style="font-family:宋体"}[1]{lang="EN-US"}[（表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[，具体请参见]{style="font-family:宋体"}[RFC 6037]{lang="EN-US"}[），长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节，私网数据流为]{style="font-family:宋体"}[(7.11.0.7, 225.1.1.1)]{lang="EN-US"}[，切换到公网的组地址为]{style="font-family:宋体"}[239.1.2.0]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_75372_x1062_x1074445229}[打开公网实例]{style="font-family:宋体"}[MD]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging multicast-domain timer]{lang="EN-US"}]{#struct_0_75372_x1062_1364460255}

[\*Nov  6 14:25:11:171 2012 Sysname MD/7/TIMER: -MDC=1; Create reconnet IPv4 MBR timer success. (D08282)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_75372_x1062_x1587063997}*[成功创建重新连接]{style="font-family:宋体"}[IPv4 MBR]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

[[\*Nov  6 14:25:14:684 2012 Sysname MD/7/TIMER: -MDC=1; Create smooth end timer (90s). (D021269)]{lang="EN-US"}]{#struct_0_75372_x1062_x204726199}

[*[// ]{lang="EN-US"}*]{#struct_0_75372_x1062_x942417212}*[创建等待平滑结束定时器，超时时间为]{style="font-family:宋体"}[90]{lang="EN-US"}[秒]{style="font-family:宋体"}*
