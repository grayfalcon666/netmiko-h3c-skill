::: {#-1266425426 .myid}
[]{#_Toc404785150}[]{#struct_0_19941_14702_x545852408}[]{#_Toc325546163}[]{#_Toc96758198}

**ISDN \-- ISDN配置命令 \-- display isdn active-channel**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **isdn active-channel**]{lang="EN-US"}]{#struct_0_19941_14702_x682153829}[命令用来显示]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口上]{style="font-family:宋体"}[Q.931]{lang="EN-US"}[呼叫成功的呼叫信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1891225549}

[**[display isdn active-channel]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_19941_14702_1081718468}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_1669321279}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19941_14702_1350124202}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_1423921798}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_707307357}

[[network-operator]{lang="EN-US"}]{#struct_0_19941_14702_2104266781}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x635109275}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19941_14702_x623111607}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1390316177}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_19941_14702_x587488377}[：显示指定]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口上]{style="font-family:宋体"}[Q.931]{lang="EN-US"}[呼叫成功的呼叫信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[接口类型和编号，可以是]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口或者]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口。如果不指定接口，则显示全部]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口上]{style="font-family:宋体"}[Q.931]{lang="EN-US"}[呼叫成功的呼叫信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_19941_14702_x286696}

[[本命令显示信息可以帮助用户进行]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1349665447}[呼叫的故障诊断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_365946303}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1930772672}[显示接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上]{style="font-family:宋体"}[Q.931]{lang="EN-US"}[呼叫成功的呼叫信息。]{style="font-family:宋体"}

[[\<Sysname\> display isdn active-channel interface bri 2/4/0]{lang="EN-US"}]{#struct_0_19941_14702_x1183113995}

[Bri 2/4/0]{lang="EN-US"}

[  Channel Info: B1]{lang="EN-US"}

[  Call Property: Analog]{lang="EN-US"}

[  Call Type: Out]{lang="EN-US"}

[  Calling Number: 1111]{lang="EN-US"}

[  Calling Subaddress:]{lang="EN-US"}

[  Called Number: 2222]{lang="EN-US"}

[  Called Subaddress:]{lang="EN-US"}

[  Start Time: 13-03-14 15:22:26]{lang="EN-US"}

[  Time Used: 00:01:10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_1060798100}[显示]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口上]{style="font-family:宋体"}[Q.931]{lang="EN-US"}[呼叫成功的呼叫信息。]{style="font-family:宋体"}

[[\<Sysname\> display isdn active-channel interface serial 2/3/0:15]{lang="EN-US"}]{#struct_0_19941_14702_1349599911}

[Serial2/3/0:15]{lang="EN-US"}

[  Serial2/3/0:15]{lang="EN-US"}

[  Channel Info: B2]{lang="EN-US"}

[  Call Property: Digital]{lang="EN-US"}

[  Call Type: Out]{lang="EN-US"}

[  Calling Number: 8306001]{lang="EN-US"}

[  Calling Subaddress:]{lang="EN-US"}

[  Called Number: 8306002]{lang="EN-US"}

[  Called Subaddress:]{lang="EN-US"}

[  Start Time: 13-02-14 12:22:26]{lang="EN-US"}

[  Time Used: 00:11:20]{lang="EN-US"}

[]{#struct_0_19941_14702_x1317970777}[]{#_Toc28140020}[]{#_Toc95359212}[]{#_Toc85604322}[]{#_Toc81386701}[]{#_Toc74661824}[]{#_Toc72589787}[]{#_Toc72589514}[]{#_Toc72588999}[]{#_Toc65921169}[]{#_Toc65919117}[]{#_Toc65919092}[]{#_Toc65910726}[]{#_Toc65909971}[]{#_Toc60125181}[]{#_Toc60111180}[]{#_Toc35242430}[]{#_Toc34733773}[]{#_Toc34733524}[]{#_Toc33587019}[表1-1 ]{lang="EN-US"}[display isdn active-channel]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1462237656}[[字段]{style="font-family:黑体"}]{#struct_0_19941_14702_x1565956348}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19941_14702_505994438}

[[Channel Info]{lang="EN-US"}]{#struct_0_19941_14702_x1914421102}

[[呼叫使用的]{style="font-family:宋体"}]{#struct_0_19941_14702_x257360107}[B]{lang="EN-US"}[通道]{style="font-family:宋体"}

[[Call Property]{lang="EN-US"}]{#struct_0_19941_14702_1349534375}

[[呼叫性质：]{style="font-family:宋体"}]{#struct_0_19941_14702_724857026}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Digital]{lang="EN-US"}]{#struct_0_19941_14702_x239064653}[：数字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Analog]{lang="EN-US"}]{#struct_0_19941_14702_x193589442}[：模拟]{lang="EN-US" style="font-family:宋体"}

[[Call Type]{lang="EN-US"}]{#struct_0_19941_14702_1816857751}

[[呼叫类型：]{style="font-family:宋体"}]{#struct_0_19941_14702_x320309061}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In]{lang="EN-US"}]{#struct_0_19941_14702_1904876144}[：入呼叫]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Out]{lang="EN-US"}]{#struct_0_19941_14702_1349468839}[：出呼叫]{lang="EN-US" style="font-family:宋体"}

[[Calling Number]{lang="EN-US"}]{#struct_0_19941_14702_x1682708437}

[[主叫号码]{style="font-family:宋体"}]{#struct_0_19941_14702_x1912193366}

[[Calling Subaddress]{lang="EN-US"}]{#struct_0_19941_14702_x414790296}

[[主叫子地址]{style="font-family:宋体"}]{#struct_0_19941_14702_607310537}

[[Called Number]{lang="EN-US"}]{#struct_0_19941_14702_2130867443}

[[被叫号码]{style="font-family:宋体"}]{#struct_0_19941_14702_1349927591}

[[Called Subaddress]{lang="EN-US"}]{#struct_0_19941_14702_1150679985}

[[被叫子地址]{style="font-family:宋体"}]{#struct_0_19941_14702_x1590274796}

[[Start Time]{lang="EN-US"}]{#struct_0_19941_14702_x1403544628}

[[呼叫成功建立时间]{style="font-family:宋体"}]{#struct_0_19941_14702_x393002864}

[[Time Used]{lang="EN-US"}]{#struct_0_19941_14702_1320107017}

[[呼叫建立后已经使用的时间]{style="font-family:宋体"}]{#struct_0_19941_14702_1349862055}

[]{#_Toc96758199}[]{#_Toc54583756}[]{#_Toc35242896}[]{#_Toc16936660}[]{#_Toc15876338}[ ]{lang="EN-US"}

::: {#-860213790 .myid}
[]{#_Toc404785151}[]{#struct_0_19941_14702_x435332709}[]{#_Toc325546164}[]{#_Toc153009846}

**ISDN \-- ISDN配置命令 \-- display isdn call-info**

------------------------------------------------------------------------

[**[display isdn call-info]{lang="EN-US"}**]{#struct_0_19941_14702_1475660648}[命令用来显示]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口的呼叫信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_2096444609}

[**[display isdn call-info]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_19941_14702_x1009443044}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_1504940368}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19941_14702_1459299016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x297773681}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1349796519}

[[network-operator]{lang="EN-US"}]{#struct_0_19941_14702_x1596094508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1320209164}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19941_14702_x1807841429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_2065160739}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_19941_14702_x1277016345}[：显示指定]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口的呼叫信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示]{style="font-family:
宋体"}[接口类型和编号，可以是]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口或者]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口。如果不指定接口，则显示全部]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口的呼叫信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_1277996694}

[[本命令输出的信息中包括接口上]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x616501365}[协议各层的信息，包括]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[、]{style="font-family:宋体"}[Q.931]{lang="EN-US"}[和]{style="font-family:宋体"}[CC]{lang="EN-US"}[，用户可以根据此命令进行故障诊断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_1125408232}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_1349730983}[显示接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[的呼叫信息。]{style="font-family:宋体"}

[[\<Sysname\> display isdn call-info interface bri 2/4/0]{lang="EN-US"}]{#struct_0_19941_14702_x97107091}

[Bri2/4/0(User-side): ACTIVE]{lang="EN-US"}

[  Link Layer 1:  TEI = 65, State = MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  Link Layer 2:  TEI = NONE, State = TEI_UNASSIGNED]{lang="EN-US"}

[  Link Layer 3:  TEI = NONE, State = TEI_UNASSIGNED]{lang="EN-US"}

[  Link Layer 4:  TEI = NONE, State = TEI_UNASSIGNED]{lang="EN-US"}

[  Link Layer 5:  TEI = NONE, State = TEI_UNASSIGNED]{lang="EN-US"}

[  Link Layer 6:  TEI = NONE, State = TEI_UNASSIGNED]{lang="EN-US"}

[  Link Layer 7:  TEI = NONE, State = TEI_UNASSIGNED]{lang="EN-US"}

[  Link Layer 8:  TEI = NONE, State = TEI_UNASSIGNED]{lang="EN-US"}

[  Network Layer: 1 connections]{lang="EN-US"}

[    Connection 1:]{lang="EN-US"}

[      CallID: 0x0001, State: ACTIVE, CES: 1, Channel: 0x00000001]{lang="EN-US"}

[      TEI: 65]{lang="EN-US"}

[      Calling_Num\[:Sub\]: 2014:1325]{lang="EN-US"}

[      Called_Num\[:Sub\]: 50401:24136]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_1404830106}[显示]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口的呼叫信息。]{style="font-family:宋体"}

[[\<Sysname\> display isdn call-info interface serial 2/3/0:15]{lang="EN-US"}]{#struct_0_19941_14702_1350189735}

[Serial2/3/0:15(User-side):]{lang="EN-US"}

[  Link Layer 1: TEI = 0, State = MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  Network Layer: 1 connections]{lang="EN-US"}

[    Connection 1:]{lang="EN-US"}

[      CallID: 0x0000ffff, State: ACTIVE, CES: 1, Channel: 0x00200000]{lang="EN-US"}

[      TEI: 0]{lang="EN-US"}

[      Calling_Num\[:Sub\]: 8306001]{lang="EN-US"}

[      Called_Num\[:Sub\]: 8305001]{lang="EN-US"}

[]{#struct_0_19941_14702_x1356638930}[[表1-2 ]{lang="EN-US"}[display isdn call-info]{lang="EN-US"}]{#_Toc95359213}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1761204091}[[字段]{style="font-family:黑体"}]{#struct_0_19941_14702_1778932099}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19941_14702_1827544348}

[[Bri2/4/0(User-side): ACTIVE]{lang="EN-US"}]{#struct_0_19941_14702_496328909}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1956835641}[接口物理层的激活状态（]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上有呼叫时才激活物理层；]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口只要物理]{style="font-family:宋体"}[UP]{lang="EN-US"}[就可以使用，不需要激活）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACTIVE]{lang="EN-US"}]{#struct_0_19941_14702_1278595231}[：接口处于激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEACTIVE]{lang="EN-US"}]{#struct_0_19941_14702_1350124199}[：接口处于去激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[User-side]{lang="EN-US"}]{#struct_0_19941_14702_x149335425}[表示]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口工作在]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议用户侧模式]{lang="EN-US" style="font-family:宋体"}

[[Link Layer]{lang="EN-US"}]{#struct_0_19941_14702_502313758}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_210808362}[接口二层链路的呼叫连接，协议将为每个终端建立一个呼叫连接，用]{style="font-family:宋体"}[TEI]{lang="EN-US"}[来区分不同的呼叫连接（]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口上只能建立一个呼叫连接，]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上最多可以建立]{style="font-family:宋体"}[8]{lang="EN-US"}[个呼叫连接）]{style="font-family:宋体"}

[[TEI]{lang="EN-US"}]{#struct_0_19941_14702_1044816592}

[[一个]{style="font-family:宋体"}[TEI]{lang="EN-US"}]{#struct_0_19941_14702_x961509581}[（]{style="font-family:宋体"}[Terminal Endpoint Identifier]{lang="EN-US"}[，终端设备标识符）标识一个终端（比如]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[电话），一个用户侧设备就是一个终端。]{style="font-family:宋体"}[TEI]{lang="EN-US"}[由网络侧设备分配]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_19941_14702_1349665448}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_365225407}[接口二层链路的当前状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TEI_UNASSIGNED]{lang="DE"}]{#struct_0_19941_14702_2010466783}[：]{lang="EN-US" style="font-family:宋体"}[TEI]{lang="DE"}[未分配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASSIGN_AWAITING_TEI]{lang="EN-US"}]{#struct_0_19941_14702_x1194925482}[：]{lang="EN-US" style="font-family:
  宋体"}[等待]{style="font-family:宋体"}[分配]{lang="EN-US" style="font-family:宋体"}[TEI]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISH_AWAITING_TEI]{lang="EN-US"}]{#struct_0_19941_14702_896237682}[：等待分配]{lang="EN-US" style="font-family:宋体"}[TEI]{lang="EN-US"}[并等待多帧建链]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TEI_ASSIGNED]{lang="DE"}]{#struct_0_19941_14702_1116744022}[：]{lang="EN-US" style="font-family:宋体"}[TEI]{lang="DE"}[已分配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AWAITING_ESTABLISHMENT]{lang="EN-US"}]{#struct_0_19941_14702_1349599912}[：等待]{lang="EN-US" style="font-family:宋体"}[多帧建链]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}]{#struct_0_19941_14702_x1318036313}[：多帧]{lang="EN-US" style="font-family:宋体"}[建链成功（]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[报文收发序号已同步）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIMER_RECOVER]{lang="EN-US"}]{#struct_0_19941_14702_486169023}[：定时器]{lang="EN-US" style="font-family:宋体"}[超时尝试]{style="font-family:宋体"}[恢复]{lang="EN-US" style="font-family:宋体"}[链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AWAITING_RELEASE]{lang="EN-US"}]{#struct_0_19941_14702_291979154}[：等待]{lang="EN-US" style="font-family:
  宋体"}[多帧连接断开]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TEI_ASSIGNED_EXT1]{lang="EN-US"}]{#struct_0_19941_14702_1710654446}[：]{lang="EN-US" style="font-family:
  宋体"}[存在]{style="font-family:宋体"}[TEI]{lang="EN-US"}[的情况下]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[接口收到底层去激活指示]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TEI_ASSIGNED_EXT2]{lang="EN-US"}]{#struct_0_19941_14702_1668142922}[：]{lang="EN-US" style="font-family:
  宋体"}[存在]{style="font-family:宋体"}[TEI]{lang="EN-US"}[的情况下]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[有新的呼叫，发起多帧]{style="font-family:宋体"}[建链]{lang="EN-US" style="font-family:
  宋体"}

[[Network Layer: 1 connections]{lang="EN-US"}]{#struct_0_19941_14702_1349534376}

[[网络层上有一个呼叫连接]{style="font-family:宋体"}]{#struct_0_19941_14702_725053634}

[[CallID]{lang="EN-US"}]{#struct_0_19941_14702_x1477619894}

[[呼叫在]{style="font-family:宋体"}[CC]{lang="EN-US"}]{#struct_0_19941_14702_1534472684}[层的索引]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_19941_14702_2068512212}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_1349468840}[接口三层链路的当前状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NULL]{lang="EN-US"}]{#struct_0_19941_14702_x1682249690}[：初始状态，不存在呼叫]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CALL_INITIATED]{lang="EN-US"}]{#struct_0_19941_14702_x1029903879}[：]{lang="EN-US" style="font-family:宋体"}[发起]{style="font-family:宋体"}[呼叫]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OVERLAP_SENDING]{lang="EN-US"}]{#struct_0_19941_14702_1363136317}[：重叠发送]{lang="EN-US" style="font-family:
  宋体"}[被叫号码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OUTGOING_CALL_PROCEEDING]{lang="EN-US"}]{#struct_0_19941_14702_63377232}[：]{lang="EN-US" style="font-family:宋体"}[正在进行出呼叫]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CALL_DELIVERED]{lang="EN-US"}]{#struct_0_19941_14702_1349927592}[：]{lang="EN-US" style="font-family:宋体"}[出]{style="font-family:宋体"}[呼叫]{lang="EN-US" style="font-family:宋体"}[时，远端已振铃，但未摘机]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CALL_PRESENT]{lang="EN-US"}]{#struct_0_19941_14702_1150483377}[：]{lang="EN-US" style="font-family:宋体"}[发出]{style="font-family:宋体"}[呼叫]{lang="EN-US" style="font-family:宋体"}[请求，但未收到应答]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CALL_RECEIVED]{lang="EN-US"}]{#struct_0_19941_14702_x1968388423}[：]{lang="EN-US" style="font-family:宋体"}[入呼叫时，本端已振铃，但未摘机]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CONNECT_REQUEST]{lang="EN-US"}]{#struct_0_19941_14702_x154272440}[：]{lang="EN-US" style="font-family:
  宋体"}[入呼叫已摘机，并发送]{style="font-family:宋体"}[连接请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INCOMING_CALL_PROCEEDING]{lang="EN-US"}]{#struct_0_19941_14702_1349862056}[：]{lang="EN-US" style="font-family:宋体"}[正在进行入呼叫]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACTIVE]{lang="EN-US"}]{#struct_0_19941_14702_x435529317}[：]{lang="EN-US" style="font-family:宋体"}[呼叫成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISCONNECT_REQUEST]{lang="EN-US"}]{#struct_0_19941_14702_1471746738}[：断开]{lang="EN-US" style="font-family:
  宋体"}[呼叫]{style="font-family:宋体"}[请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISCONNECT_INDICATION]{lang="EN-US"}]{#struct_0_19941_14702_1185607755}[：断开]{lang="EN-US" style="font-family:
  宋体"}[呼叫]{style="font-family:宋体"}[指示]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SUSPEND_REQUEST]{lang="EN-US"}]{#struct_0_19941_14702_1523963132}[：暂停请求]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RESUME_REQUEST]{lang="EN-US"}]{#struct_0_19941_14702_1349796520}[：恢复请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RELEASE_REQUEST]{lang="EN-US"}]{#struct_0_19941_14702_x1595504683}[：释放请求]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OVERLAP_RECEIVING]{lang="EN-US"}]{#struct_0_19941_14702_x561623070}[：重叠接收]{lang="EN-US" style="font-family:
  宋体"}

[[CES]{lang="EN-US"}]{#struct_0_19941_14702_x1502642343}

[[连接端点后缀（]{style="font-family:宋体"}[Q.931]{lang="EN-US"}]{#struct_0_19941_14702_1349730984}[和]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[协议之间用]{style="font-family:宋体"}[CES]{lang="EN-US"}[来标识呼叫连接）]{style="font-family:宋体"}

[[Channel]{lang="EN-US"}]{#struct_0_19941_14702_x97434771}

[[呼叫占用的]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}]{#struct_0_19941_14702_x87209690}[通道的位图（位图中每个]{style="font-family:宋体"}[2]{lang="EN-US"}[进制位表示一个]{style="font-family:宋体"}[B]{lang="EN-US"}[通道，如果对应的]{style="font-family:宋体"}[2]{lang="EN-US"}[进制位值是]{style="font-family:宋体"}[1]{lang="EN-US"}[，表示]{style="font-family:宋体"}[B]{lang="EN-US"}[通道被占用）]{style="font-family:宋体"}

[[Calling_Num\[:Sub\]]{lang="EN-US"}]{#struct_0_19941_14702_700103997}

[[主叫号码]{style="font-family:宋体"}[\[:]{lang="EN-US"}]{#struct_0_19941_14702_1350189736}[主叫子地址]{style="font-family:宋体"}[\]]{lang="EN-US"}

[[Called_Num\[:Sub\]]{lang="EN-US"}]{#struct_0_19941_14702_x1356573394}

[[被叫号码]{style="font-family:宋体"}[\[:]{lang="EN-US"}]{#struct_0_19941_14702_x1197447391}[被叫子地址]{style="font-family:宋体"}[\]]{lang="EN-US"}

[[ ]{lang="EN-US"}]{#_Toc54583760}

::: {#-727530074 .myid}
[]{#_Toc350155457}[]{#_Toc342653636}[]{#_Toc404785152}[]{#struct_0_19941_14702_1362639835}[]{#_Toc353443098}[]{#_Toc352068895}[]{#_Toc54583757}

**ISDN \-- ISDN配置命令 \-- display isdn call-record**

------------------------------------------------------------------------

[**[display isdn call-record]{lang="EN-US"}**]{#struct_0_19941_14702_1350124200}[命令用来显示]{style="font-family:
宋体"}[ISDN]{lang="EN-US"}[的呼叫历史记录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1424052870}

[**[display isdn call-record]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_19941_14702_x937616101}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1150289505}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19941_14702_x1949428815}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379217904}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_213261342}

[[network-operator]{lang="EN-US"}]{#struct_0_19941_14702_x1801880203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_1829654905}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19941_14702_x1283759822}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379283440}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_19941_14702_1801266392}[：显示指定]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口的呼叫历史记录。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[接口类型和编号，可以是]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口或者]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口。如果不指定接口，则显示全部]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口的呼叫历史记录。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x70251175}

[[本命令显示自设备启动后到目前为止的呼叫成功的历史记录，最多可显示最新的]{style="font-family:宋体"}[100]{lang="EN-US"}]{#struct_0_19941_14702_x530749984}[条记录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1573514502}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1379348976}[显示]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[的呼叫历史记录。]{style="font-family:宋体"}

[[\<Sysname\> display isdn call-record]{lang="EN-US"}]{#struct_0_19941_14702_873800139}

[Type Caller    Called    Start time        End time          Duration(s)]{lang="EN-US"}

[Out  -         232303    13-03-20 14:10:12 -                 273]{lang="EN-US"}

[In   -         262609    13-03-20 14:04:50 13-03-20 14:08:54 244]{lang="EN-US"}

[Out  -         232303    13-03-20 14:00:47 13-03-20 14:04:07 200]{lang="EN-US"}

[In   232303    262609    13-03-20 13:48:15 13-03-20 13:49:06 51]{lang="EN-US"}

[Out  262609    232303    13-03-20 13:46:39 13-03-20 13:47:31 52]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display isdn call-record]{lang="EN-US"}]{#struct_0_19941_14702_463911439}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1756572995}[[字段]{style="font-family:黑体"}]{#struct_0_19941_14702_x2049495725}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379414512}

[[Type]{lang="EN-US"}]{#struct_0_19941_14702_x1364118820}

[[呼叫类型：]{style="font-family:宋体"}]{#struct_0_19941_14702_x2091431604}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In]{lang="EN-US"}]{#struct_0_19941_14702_x1378955760}[：入呼叫]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Out]{lang="EN-US"}]{#struct_0_19941_14702_x1843058215}[：出呼叫]{lang="EN-US" style="font-family:宋体"}

[[Caller]{lang="EN-US"}]{#struct_0_19941_14702_x372518486}

[[主叫号码]{style="font-family:宋体"}]{#struct_0_19941_14702_x1300865648}

[[Called]{lang="EN-US"}]{#struct_0_19941_14702_x1379021296}

[[被叫号码]{style="font-family:宋体"}]{#struct_0_19941_14702_x736025586}

[[Start time]{lang="EN-US"}]{#struct_0_19941_14702_x1313826145}

[[呼叫成功建立时间]{style="font-family:宋体"}]{#struct_0_19941_14702_x1379086832}

[[End time]{lang="EN-US"}]{#struct_0_19941_14702_x933360102}

[[呼叫停止时间]{style="font-family:宋体"}]{#struct_0_19941_14702_x529210830}

[[Duration]{lang="EN-US"}]{#struct_0_19941_14702_x1379152368}

[[呼叫建立后已经使用的时间，单位为]{style="font-family:宋体"}]{#struct_0_19941_14702_x1871196524}[秒]{style="font-family:
  宋体"}

[]{#_Toc96758201}[]{#_Toc54583758}[]{#_Toc42687971}[]{#_Toc42688897}[ ]{lang="EN-US"}

::: {#-1092053817 .myid}
[]{#_Toc404785153}[]{#struct_0_19941_14702_x1829674937}[]{#_Toc353443099}[]{#_Toc352068896}[]{#_Toc153009848}

**ISDN \-- ISDN配置命令 \-- display isdn parameters**

------------------------------------------------------------------------

[**[display isdn parameters]{lang="EN-US"}**]{#struct_0_19941_14702_286043063}[命令用来显示]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议二层和三层系统参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2043000878}

[**[display isdn parameters]{lang="EN-US"}**[ { *protocol* \| **interface** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_19941_14702_x1378693616}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1722306080}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19941_14702_x1968254290}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_604174536}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1890924681}

[[network-operator]{lang="EN-US"}]{#struct_0_19941_14702_x1378759152}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_2020283153}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19941_14702_1090094315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1014813928}

[]{#struct_0_19941_14702_x1659932115}[*[protocol]{lang="EN-US"}*]{#_Toc32639374}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议类型，可以取的值包括]{style="font-family:宋体"}**[5ess]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ansi]{lang="EN-US"}**[、]{style="font-family:宋体"}**[at&t]{lang="EN-US"}**[、]{style="font-family:宋体"}**[dss1]{lang="EN-US"}**[、]{style="font-family:宋体"}**[etsi]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ni]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ni2]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ntt]{lang="EN-US"}**[、]{style="font-family:宋体"}**[qsig]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_19941_14702_2138912608}[：指定接口类型和编号，可以是]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口或者]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379217903}

[[本命令可以显示]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1779345283}[协议二层和三层系统参数，包括各种系统定时器时长以及滑动窗口尺寸信息。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_1429574386}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_19941_14702_1087660249}*[protocol]{lang="EN-US"}*[，显示的是该协议的缺省系统参数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口，显示的是该接口下的系统参数。]{style="font-family:宋体"}]{#struct_0_19941_14702_x1093699796}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_167661866}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1379283439}[显示]{style="font-family:宋体"}[DSS1 ISDN]{lang="EN-US"}[协议的缺省系统参数。]{style="font-family:宋体"}

[[\<Sysname\> display isdn parameters dss1]{lang="EN-US"}]{#struct_0_19941_14702_x570927851}

[DSS1 ISDN Layer 2 system parameters:]{lang="EN-US"}

[  T200(sec)   T201(sec)   T202(sec)    T203(sec)   N200   K(BRI)    K(PRI)]{lang="EN-US"}

[  1           1           2            10          3      1         7]{lang="EN-US"}

[ ]{lang="EN-US"}

[DSS1 ISDN Layer 3 system timers(default values):]{lang="EN-US"}

[  Timer                 Value(sec)]{lang="EN-US"}

[  T301                  240]{lang="EN-US"}

[  T302                  15]{lang="EN-US"}

[  T303                  4]{lang="EN-US"}

[  T304                  30]{lang="EN-US"}

[  T305                  30]{lang="EN-US"}

[  T308                  4]{lang="EN-US"}

[  T309                  90]{lang="EN-US"}

[  T310                  40]{lang="EN-US"}

[  T313                  4]{lang="EN-US"}

[  T322                  4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1379348975}[显示]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口的系统参数。]{style="font-family:宋体"}

[[\<Sysname\> display isdn parameters interface serial 2/3/0:15]{lang="EN-US"}]{#struct_0_19941_14702_1277084666}

[Serial2/3/0:15(Network-side):]{lang="EN-US"}

[QSIG ISDN Layer 2 system parameters:]{lang="EN-US"}

[  T200(sec)   T201(sec)   T202(sec)    T203(sec)   N200   K(PRI)]{lang="EN-US"}

[  1           1           2            10          3      7]{lang="EN-US"}

[ ]{lang="EN-US"}

[QSIG ISDN Layer 3 system timers:]{lang="EN-US"}

[  Timer                 Value(sec)]{lang="EN-US"}

[  T301                  35]{lang="EN-US"}

[  T302                  37]{lang="EN-US"}

[  T303                  8]{lang="EN-US"}

[  T304                  50]{lang="EN-US"}

[  T305                  20]{lang="EN-US"}

[  T308                  3]{lang="EN-US"}

[  T309                  130]{lang="EN-US"}

[  T310                  130]{lang="EN-US"}

[  T313                  6]{lang="EN-US"}

[  T322                  8]{lang="EN-US"}

[]{#struct_0_19941_14702_x1777137799}[]{#_Toc49930020}[]{#_Toc95359214}[]{#_Toc85604324}[]{#_Toc81386703}[]{#_Toc74661826}[]{#_Toc72589789}[]{#_Toc72589516}[]{#_Toc72589001}[]{#_Toc65921171}[]{#_Toc65919119}[]{#_Toc65919094}[]{#_Toc65910728}[]{#_Toc65909973}[]{#_Toc60125183}[]{#_Toc60111182}[表1-4 ]{lang="EN-US"}[display isdn parameters]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1747066087}[[字段]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379414511}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19941_14702_201965121}

[[T200(sec)]{lang="EN-US"}]{#struct_0_19941_14702_587760716}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1378955759}[二层协议的重传定时器，单位为秒]{style="font-family:宋体"}

[[T201(sec)]{lang="EN-US"}]{#struct_0_19941_14702_1241858892}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1652758611}[二层协议的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[检测请求的重发定时器，单位为秒]{style="font-family:宋体"}

[[T202(sec)]{lang="EN-US"}]{#struct_0_19941_14702_x185825964}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1379021295}[二层协议的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[请求消息的重发定时器，单位为秒]{style="font-family:宋体"}

[[T203(sec)]{lang="EN-US"}]{#struct_0_19941_14702_1992857769}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x43660218}[二层协议的链路最大空闲时间，单位为秒]{style="font-family:宋体"}

[[N200]{lang="EN-US"}]{#struct_0_19941_14702_197381139}

[[最大重传次数]{style="font-family:宋体"}]{#struct_0_19941_14702_x1379086831}

[[K(BRI)]{lang="EN-US"}]{#struct_0_19941_14702_x530075575}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_802200230}[接口上允许的最大未确认帧数（滑动窗口尺寸）]{style="font-family:宋体"}

[[K(PRI)]{lang="EN-US"}]{#struct_0_19941_14702_x1379152367}

[[ISDN PRI]{lang="EN-US"}]{#struct_0_19941_14702_x661342943}[接口上允许的最大未确认帧数（滑动窗口尺寸）]{style="font-family:宋体"}

[[Timer]{lang="EN-US"}]{#struct_0_19941_14702_561842740}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1378693615}[三层定时器]{style="font-family:宋体"}

[[Value(sec)]{lang="EN-US"}]{#struct_0_19941_14702_x156222139}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1967130798}[三层定时器时长，单位为秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1018587713 .myid}
[]{#_Toc404785154}[]{#struct_0_19941_14702_1296782246}

**ISDN \-- ISDN配置命令 \-- display isdn spid**

------------------------------------------------------------------------

[**[display isdn spid]{lang="EN-US"}**]{#struct_0_19941_14702_x1118998758}[命令用来显示采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上]{style="font-family:宋体"}[SPID]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1939316364}

[**[display isdn spid]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_19941_14702_x1378759151}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x708600202}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19941_14702_x164236893}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_890166331}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_132827287}

[[network-operator]{lang="EN-US"}]{#struct_0_19941_14702_x1382671015}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_351239434}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19941_14702_1260048041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1900105992}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_19941_14702_1596734387}[：指定接口类型和编号。只能是采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口。如果不指定接口，则查看所有采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379217906}

[[在]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1376060756}[运行过程中，当需要查看]{style="font-family:宋体"}[SPID]{lang="EN-US"}[的类型、]{style="font-family:宋体"}[SPID]{lang="EN-US"}[取值等信息的时候，可以使用本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x442485494}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x1513049212}[显示]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[NI]{lang="SV"}[协议的接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[上的]{style="font-family:宋体"}[SPID]{lang="SV"}[信息]{style="font-family:宋体"}[（]{style="font-family:宋体"}[SPID]{lang="SV"}[类型为]{style="font-family:宋体"}[AUTO]{lang="SV"}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display isdn spid interface bri 2/4/0]{lang="SV"}]{#struct_0_19941_14702_x1044137191}

[Interface Bri2/4/0:]{lang="DA"}

[  SPID Type: AUTO]{lang="DA"}

[ ]{lang="EN-US"}

[  SPID B1:]{lang="DA"}

[    ]{lang="DA"}[SPID Num: 235]{lang="EN-US"}

[    Neg State: SPID_UNASSIGNED]{lang="EN-US"}

[    Init State: INIT_NULL]{lang="EN-US"}

[ ]{lang="EN-US"}

[  ]{lang="EN-US"}[SPID B2:]{lang="DA"}

[    SPID Num: 326]{lang="DA"}

[    Neg State: SPID_UNASSIGNED]{lang="DA"}

[    ]{lang="DA"}[Init State: INIT_NULL]{lang="EN-US"}

[ ]{lang="EN-US"}

[  SPID timer: 30 seconds]{lang="EN-US"}

[  SPID resend: 1 times]{lang="EN-US"}

[]{#OLE_LINK12}[[\# ]{lang="SV"}]{#struct_0_19941_14702_x1379283442}[显示]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[NI]{lang="SV"}[协议的接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[上的]{style="font-family:宋体"}[SPID]{lang="SV"}[信息（]{style="font-family:宋体"}[SPID]{lang="SV"}[类型为]{style="font-family:宋体"}[STATIC]{lang="SV"}[）。]{style="font-family:宋体"}

[[\<Sysname\> display isdn spid interface bri 2/4/0]{lang="SV"}]{#struct_0_19941_14702_x1330901490}

[Interface Bri2/4/0:]{lang="EN-US"}

[  SPID Type: STATIC]{lang="EN-US"}

[ ]{lang="EN-US"}

[  SPID B1:]{lang="EN-US"}

[    SPID Num: 134]{lang="EN-US"}

[    LDN: 3251]{lang="EN-US"}

[    Init State: INIT_NULL]{lang="EN-US"}

[ ]{lang="EN-US"}

[  SPID B2:]{lang="EN-US"}

[    SPID Num: 257]{lang="EN-US"}

[    LDN: 3657]{lang="EN-US"}

[    Init State: INIT_NULL]{lang="EN-US"}

[ ]{lang="EN-US"}

[  SPID timer: 30 seconds]{lang="EN-US"}

[  SPID resend: 1 times]{lang="EN-US"}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x566774532}[显示]{style="font-family:宋体"}[支持]{style="font-family:宋体"}[NI]{lang="SV"}[协议的接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[上的]{style="font-family:宋体"}[SPID]{lang="SV"}[信息（]{style="font-family:宋体"}[SPID]{lang="SV"}[类型为]{style="font-family:宋体"}[NIT]{lang="SV"}[）。]{style="font-family:宋体"}

[[\<Sysname\> display isdn spid interface bri 2/4/0]{lang="SV"}]{#struct_0_19941_14702_56095695}

[Interface Bri2/4/0:]{lang="EN-US"}

[  SPID Type: NIT]{lang="EN-US"}

[]{#struct_0_19941_14702_1206725921}[[表1-5 ]{lang="EN-US"}[display isdn spid]{lang="EN-US"}]{#_Toc60111183}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1769122381}[[字段]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379348978}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19941_14702_x1902137383}

[[SPID Type]{lang="EN-US"}]{#struct_0_19941_14702_1004308655}

[[SPID]{lang="EN-US"}]{#struct_0_19941_14702_728877282}[类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NIT]{lang="EN-US"}]{#struct_0_19941_14702_x666274833}[：非初始化终端模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC]{lang="EN-US"}]{#struct_0_19941_14702_x209915124}[：静态模式，只包括]{lang="EN-US" style="font-family:宋体"}[L3]{lang="EN-US"}[初始化过程]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTO]{lang="EN-US"}]{#struct_0_19941_14702_x83674932}[：动态模式，包括协商和]{style="font-family:宋体"}[L3]{lang="EN-US"}[初始化两个过程]{style="font-family:宋体"}

[[SPID B1]{lang="EN-US"}]{#struct_0_19941_14702_x1379414514}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x201319406}[接口]{style="font-family:宋体"}[B1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[SPID B2]{lang="EN-US"}]{#struct_0_19941_14702_x1880618380}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_1514012051}[接口]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[SPID Num]{lang="EN-US"}]{#struct_0_19941_14702_x370402317}

[[SPID]{lang="EN-US"}]{#struct_0_19941_14702_x1616385100}[值，可能是静态配置，也可能是动态协商获取，依赖于]{style="font-family:宋体"}[SPID Type]{lang="EN-US"}

[[LDN]{lang="EN-US"}]{#struct_0_19941_14702_x1378955762}

[[本地拨号号码]{style="font-family:宋体"}]{#struct_0_19941_14702_x680258801}

[[Neg State]{lang="EN-US"}]{#struct_0_19941_14702_x298344593}

[[SPID]{lang="EN-US"}]{#struct_0_19941_14702_x127535047}[的协商状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPID_UNASSIGNED]{lang="EN-US"}]{#struct_0_19941_14702_951100268}[：]{style="font-family:宋体"}[SPID]{lang="EN-US"}[还未分配或分配失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASSIGN_AWAITING_SPID]{lang="EN-US"}]{#struct_0_19941_14702_x501008002}[：终端已经发起]{style="font-family:宋体"}[Auto-SPID]{lang="EN-US"}[请求，但]{style="font-family:宋体"}[SPID]{lang="EN-US"}[还未分配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPID_ASSIGNED]{lang="EN-US"}]{#struct_0_19941_14702_x1379021298}[：]{style="font-family:宋体"}[程控]{lang="EN-US" style="font-family:宋体"}[交换机已经完成]{style="font-family:宋体"}[SPID]{lang="EN-US"}[的分配且终端自动选择了一个]{style="font-family:宋体"}[SPID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASSIGN_AWAITING_CALL_CLEAR]{lang="EN-US"}]{#struct_0_19941_14702_2039911936}[：当前存在呼叫时，收到]{style="font-family:
  宋体"}[Auto-SPID]{lang="EN-US"}[请求后进入该状态]{style="font-family:宋体"}

[[Init State]{lang="EN-US"}]{#struct_0_19941_14702_x878734669}

[[SPID]{lang="EN-US"}]{#struct_0_19941_14702_x1305357044}[的]{style="font-family:宋体"}[L3]{lang="EN-US"}[初始化状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INIT_NULL]{lang="EN-US"}]{#struct_0_19941_14702_1227261706}[：]{style="font-family:宋体"}[L3]{lang="EN-US"}[还未初始化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INIT_IND]{lang="EN-US"}]{#struct_0_19941_14702_x1379086834}[：]{style="font-family:宋体"}[程控]{lang="EN-US" style="font-family:宋体"}[交换机发起]{style="font-family:宋体"}[L3]{lang="EN-US"}[初始化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INIT_PROCEEDING]{lang="EN-US"}]{#struct_0_19941_14702_229439312}[：]{style="font-family:宋体"}[L3]{lang="EN-US"}[初始化正在进行]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INIT_END]{lang="EN-US"}]{#struct_0_19941_14702_2134240698}[：]{style="font-family:宋体"}[L3]{lang="EN-US"}[初始化成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INIT_AWAITING_CALL_CLEAR]{lang="EN-US"}]{#struct_0_19941_14702_1176176737}[：当前存在呼叫时，收到]{style="font-family:宋体"}[L3]{lang="EN-US"}[初始化请求后进入该状态]{style="font-family:宋体"}

[[SPID timer]{lang="EN-US"}]{#struct_0_19941_14702_x1121914743}

[[定时器]{style="font-family:宋体"}[TSPID]{lang="EN-US"}]{#struct_0_19941_14702_x1379152370}[的时长]{style="font-family:宋体"}

[[SPID resend]{lang="EN-US"}]{#struct_0_19941_14702_2067474876}

[[SPID]{lang="EN-US"}]{#struct_0_19941_14702_x260498886}[消息重传次数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-443233799 .myid}
[]{#_Toc404785155}[]{#struct_0_19941_14702_855014516}[]{#_Toc325546165}

**ISDN \-- ISDN配置命令 \-- isdn bch-local-manage**

------------------------------------------------------------------------

[**[isdn bch-local-manage]{lang="EN-US"}**]{#struct_0_19941_14702_1283258295}[命令用来配置本地管理]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[**[undo isdn bch-local-manage]{lang="EN-US"}**]{#struct_0_19941_14702_x2126589229}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2111260919}

[**[isdn bch-local-manage]{lang="EN-US"}**[ \[ **exclusive** \]]{lang="EN-US"}]{#struct_0_19941_14702_x1378693618}

[**[undo isdn bch-local-manage]{lang="EN-US"}**]{#struct_0_19941_14702_x559506666}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1987103027}

[[未配置本地管理]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}]{#struct_0_19941_14702_735239922}[通道，由程控交换机负责]{style="font-family:宋体"}[B]{lang="EN-US"}[通道的管理。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1903805595}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1141913687}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x596220007}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x669375102}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1203279863}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_95770394}

[**[exclusive]{lang="EN-US"}**]{#struct_0_19941_14702_x1378759154}[：强制本地管理]{style="font-family:宋体"}[B]{lang="EN-US"}[通道模式，这种模式下如果程控交换机指示的]{style="font-family:宋体"}[B]{lang="EN-US"}[通道与本地的要求不一致时，将会导致呼叫失败。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1468115089}

[[在呼叫过程中，对呼叫所用]{style="font-family:宋体"}[B]{lang="EN-US"}]{#struct_0_19941_14702_581977702}[通道进行适当的管理是很重要的，尤其是在]{style="font-family:宋体"}[PRI]{lang="EN-US"}[方式下，适当的通道管理可以提高呼叫效率，减小呼叫损耗。一般来说，由程控交换机统一对]{style="font-family:宋体"}[B]{lang="EN-US"}[通道进行管理是比较合适的方式，所以虽然设备提供了]{style="font-family:宋体"}[B]{lang="EN-US"}[通道本地管理功能，但建议还是以程控交换机为主。]{style="font-family:宋体"}

[[当用户配置了]{style="font-family:宋体"}**[isdn bch-local-manage]{lang="EN-US"}**]{#struct_0_19941_14702_1865640293}[命令后，设备将工作于本地管理]{style="font-family:宋体"}[B]{lang="EN-US"}[通道的模式，由本地自主选择空闲的]{style="font-family:宋体"}[B]{lang="EN-US"}[通道。但即使设置了本地管理]{style="font-family:宋体"}[B]{lang="EN-US"}[通道，程控交换机仍然享有优先权。即：如果程控交换机选定了一条与本地指定的]{style="font-family:宋体"}[B]{lang="EN-US"}[通道不同的空闲通道，设备还是会按照程控交换机的指示完成通信。]{style="font-family:宋体"}

[[当用户配置了]{style="font-family:宋体"}**[isdn bch-local-manage exclusive]{lang="EN-US"}**]{#struct_0_19941_14702_798184337}[命令后，设备将工作于强制本地管理]{style="font-family:宋体"}[B]{lang="EN-US"}[通道的模式。即：在出呼叫]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息的]{style="font-family:宋体"}[Channel ID]{lang="EN-US"}[信息单元中会指示]{style="font-family:宋体"}[B]{lang="EN-US"}[通道为"必选，不可更改"，由本地来分配一条空闲的]{style="font-family:宋体"}[B]{lang="EN-US"}[通道，如果程控交换机指示的]{style="font-family:宋体"}[B]{lang="EN-US"}[通道与之前本地的要求不一致时，将会导致呼叫失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1612256678}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1111545300}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[工作于本地管理]{style="font-family:宋体"}[B]{lang="EN-US"}[通道的模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x107690346}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn bch-local-manage]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379217905}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn bch-select-way]{lang="EN-US"}**]{#struct_0_19941_14702_x1352822599}
:::

::: {#-510998259 .myid}
[]{#_Toc404785156}[]{#struct_0_19941_14702_x1353703333}[]{#_Toc325546166}[]{#_Toc54583761}

**ISDN \-- ISDN配置命令 \-- isdn bch-select-way**

------------------------------------------------------------------------

[**[isdn bch-select-way]{lang="EN-US"}**]{#struct_0_19941_14702_587374268}[命令用来配置]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}[通道的选择方式。]{style="font-family:宋体"}

[**[undo isdn bch-select-way]{lang="EN-US"}**]{#struct_0_19941_14702_x1296560680}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1735221865}

[**[isdn bch-select-way]{lang="EN-US"}**[ { **ascending** \| **descending** }]{lang="EN-US"}]{#struct_0_19941_14702_x1872001698}

[**[undo isdn bch-select-way]{lang="EN-US"}**]{#struct_0_19941_14702_1337715798}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_1754975660}

[[如果用]{style="font-family:宋体"}**[isdn bch-local-manage]{lang="EN-US"}**]{#struct_0_19941_14702_x302981912}[命令配置了本地管理]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}[通道，则按照升序方式选择]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379283441}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x927616963}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x924772250}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_773712558}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_1850193014}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_1115997986}

[**[ascending]{lang="EN-US"}**]{#struct_0_19941_14702_705919137}[：按照升序方式选择]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}[通道，即按照]{style="font-family:宋体"}[B]{lang="EN-US"}[通道编号从小到大的顺序循环进行选择。]{style="font-family:宋体"}

[**[descending]{lang="EN-US"}**]{#struct_0_19941_14702_1970771664}[：按照降序方式选择]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}[通道，即按照]{style="font-family:宋体"}[B]{lang="EN-US"}[通道编号从大到小的顺序循环进行选择。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_615825425}

[[在程控交换机管理]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}]{#struct_0_19941_14702_x1379348977}[通道的情况下，本命令不起作用。]{style="font-family:宋体"}

[[如果用户侧不配置]{style="font-family:宋体"}**[isdn bch-local-manage]{lang="EN-US"}**]{#struct_0_19941_14702_x1855083216}[命令，则配置]{style="font-family:宋体"}**[isdn bch-select-way]{lang="EN-US"}**[命令无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1179216325}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1116021471}[设置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[B]{lang="EN-US"}[通道选择方式为降序方式。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1347154919}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn bch-select-way descending]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_107930918}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn bch-local-manage]{lang="EN-US"}**]{#struct_0_19941_14702_965024687}
:::

::: {#-202045296 .myid}
[]{#_Toc325546167}[]{#_Toc54583763}[]{#_Toc404785157}[]{#struct_0_19941_14702_x951613637}[]{#_Toc350155460}[]{#_Toc342653624}

**ISDN \-- ISDN配置命令 \-- isdn bri-slipwnd-size**

------------------------------------------------------------------------

[**[isdn bri-slipwnd-size]{lang="EN-US"}**]{#struct_0_19941_14702_1286837495}[命令用来配置]{style="font-family:宋体"}[ISDN BRI]{lang="EN-US"}[接口的滑动窗口的大小。]{style="font-family:宋体"}

[**[undo isdn bri-slipwnd-size]{lang="EN-US"}**]{#struct_0_19941_14702_x1379414513}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1364764535}

[**[isdn bri-slipwnd-size]{lang="EN-US"}**[ *window-size*]{lang="EN-US"}]{#struct_0_19941_14702_x70769190}

[**[undo isdn bri-slipwnd-size]{lang="EN-US"}**]{#struct_0_19941_14702_x1959500226}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2108498126}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_1528634648}[接口的滑动窗口大小为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_899244333}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1604971520}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_2012976629}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1792336015}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1378955761}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_885825140}

[*[window-size]{lang="EN-US"}*]{#struct_0_19941_14702_x1406154175}[：滑动窗口大小，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1923388098}

[[Q.921]{lang="EN-US"}]{#struct_0_19941_14702_870681205}[缓冲区中的帧是按序号发送的，每个发送出去的帧都要被接收端确认。系统在发送时会连续发送几帧，但在发送时会判断未确认帧的个数，如果]{style="font-family:宋体"}[V]{lang="EN-US"}[（]{style="font-family:宋体"}[A]{lang="EN-US"}[）]{style="font-family:宋体"} [＋]{style="font-family:宋体"}[ K ]{lang="EN-US"}[＝]{style="font-family:宋体"}[ V]{lang="EN-US"}[（]{style="font-family:宋体"}[S]{lang="EN-US"}[），则不再进行发送。其中，]{style="font-family:
宋体"}[V]{lang="EN-US"}[（]{style="font-family:宋体"}[A]{lang="EN-US"}[）是已确认帧的序号，]{style="font-family:宋体"}[V]{lang="EN-US"}[（]{style="font-family:宋体"}[S]{lang="EN-US"}[）是下次要发送帧的序号，]{style="font-family:宋体"}[K]{lang="EN-US"}[是滑动窗口大小。]{style="font-family:宋体"}

[[滑动窗机制使得系统在发送帧时不必等待上一帧的确认，提高了发送效率。滑动窗口的大小决定了未确认帧的最大个数。]{style="font-family:宋体"}]{#struct_0_19941_14702_x1548200633}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_310726785}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_1950710002}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[的滑动窗口大小为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1379021297}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn bri-slipwnd-size 7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_830058355}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[isdn pri-slipwnd-size]{lang="EN-US"}**]{#struct_0_19941_14702_x2073311090}
:::

::: {#552878459 .myid}
[]{#_Toc404785158}[]{#struct_0_19941_14702_1807237512}[]{#_Toc350155461}[]{#_Toc342653609}

**ISDN \-- ISDN配置命令 \-- isdn caller-number**

------------------------------------------------------------------------

[**[isdn caller-number]{lang="EN-US"}**]{#struct_0_19941_14702_x1967357444}[命令用来配置允许呼入的主叫号码。]{style="font-family:宋体"}

[**[undo isdn caller-number]{lang="EN-US"}**]{#struct_0_19941_14702_x1772500275}[用来删除配置的允许呼入的主叫号码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_316735552}

[**[isdn caller-number]{lang="EN-US"}**[ *caller-number*]{lang="EN-US"}]{#struct_0_19941_14702_1922339310}

[**[undo isdn caller-number]{lang="EN-US"}**]{#struct_0_19941_14702_1243172215}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1752212862}

[[不对呼入的主叫号码进行检查。]{style="font-family:宋体"}]{#struct_0_19941_14702_x1379086833}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_632723839}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1967342854}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_1605564820}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1155134900}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x597011834}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1096306520}

[*[caller-number]{lang="EN-US"}*]{#struct_0_19941_14702_x1010655528}[：表示允许呼入的主叫号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2120464519}

[[配置本命令后，如果收到的呼叫建立消息中未携带主叫号码或者携带的主叫号码和本命令配置的不一样，都将导致呼叫失败。]{style="font-family:宋体"}]{#struct_0_19941_14702_x1379152369}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_857686831}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1700746562}[配置允许呼入的主叫号码为]{style="font-family:宋体"}[400]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1110075991}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn caller-number 400]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_451305569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn calling]{lang="EN-US"}**]{#struct_0_19941_14702_1297436153}
:::

::: {#66022165 .myid}
[]{#_Toc404785159}[]{#struct_0_19941_14702_x710983334}

**ISDN \-- ISDN配置命令 \-- isdn calling**

------------------------------------------------------------------------

[**[isdn calling]{lang="EN-US"}**]{#struct_0_19941_14702_x1797819087}[命令用来配置在出呼叫中携带主叫号码。]{style="font-family:宋体"}

[**[undo isdn calling]{lang="EN-US"}**]{#struct_0_19941_14702_1390307027}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1378693617}

[**[isdn calling ]{lang="EN-US"}***[calling-number]{lang="EN-US"}*]{#struct_0_19941_14702_1006577275}

[**[undo isdn calling]{lang="EN-US"}**]{#struct_0_19941_14702_221741331}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x115565736}

[[语音业务的出呼叫中携带主叫号码，其他业务的出呼叫中不携带主叫号码。]{style="font-family:宋体"}]{#struct_0_19941_14702_269430862}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x851925326}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1246450715}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1241096566}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1533918312}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x498021321}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1378759153}

[*[calling-number]{lang="EN-US"}*]{#struct_0_19941_14702_454199212}[：主叫号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x50445227}

[[主叫方配置该命令把主叫号码发送给被叫方后，被叫方通过查看]{style="font-family:宋体"}**[display isdn call-info]{lang="EN-US"}**]{#struct_0_19941_14702_x2046949326}[命令就可以看到主叫方号码。如果被叫方配置了允许呼入的主叫号码，则被叫方会对主叫方发送过来的主叫号码进行检查。]{style="font-family:宋体"}

[[需要注意：]{style="font-family:宋体"}]{#struct_0_19941_14702_293105602}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[需要注意的是，配置了]{lang="EN-US" style="font-family:宋体"}**[isdn calling]{lang="EN-US"}**]{#struct_0_19941_14702_x273778080}[命令后，如果电话网络中的程控交换机可以携带主叫号码，那么主叫号码可以发送给被叫方，如果电话网络中的程控交换机不能携带主叫号码，那么主叫号码也不能发送给被叫方。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于语音业务，不建议通过本命令配置出呼叫中携带的主叫号码。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19941_14702_375398246}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_457989586}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1589805974}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[在出呼叫中携带主叫号码]{style="font-family:宋体"}[8060170]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x41052300}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn calling 8060170]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_868840621}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display isdn call-info]{lang="EN-US"}**]{#struct_0_19941_14702_x1379217908}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn caller-number]{lang="EN-US"}**]{#struct_0_19941_14702_1826399450}
:::

::: {#539778276 .myid}
[]{#_Toc325546168}[]{#_Toc153009856}[]{#_Toc404785160}[]{#struct_0_19941_14702_49499507}[]{#_Toc350155463}[]{#_Toc342653611}[]{#_Toc261877518}

**ISDN \-- ISDN配置命令 \-- isdn carry calling-name**

------------------------------------------------------------------------

[**[isdn carry calling-name]{lang="EN-US"}**]{#struct_0_19941_14702_x2039598227}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议在出方向报文中携带]{style="font-family:宋体"}[calling-name]{lang="EN-US"}[字段。]{style="font-family:宋体"}

[**[undo isdn carry calling-name]{lang="EN-US"}**]{#struct_0_19941_14702_1915471490}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_399347725}

[**[isdn carry calling-name]{lang="EN-US"}**]{#struct_0_19941_14702_x1596537523}

[**[undo isdn carry calling-name]{lang="EN-US"}**]{#struct_0_19941_14702_1414624733}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_1755961164}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1379283444}[协议在出方向报文中不携带]{style="font-family:宋体"}[calling-name]{lang="EN-US"}[字段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x168102076}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_962136562}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x441191369}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_142247264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x61662066}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2013146400}

[[在主叫方配置本命令后，被叫方可以看到主叫方的名字。]{style="font-family:宋体"}]{#struct_0_19941_14702_x510411230}

[[当]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1440636420}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379348980}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_2036009729}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[在出方向报文中携带]{style="font-family:宋体"}[calling-name]{lang="SV"}[字段。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_x1903019815}

[\[Sysname\] interface bri 2/4/0]{lang="SV"}

[\[Sysname-Bri2/4/0\] isdn carry calling-name]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x166088773}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[isdn carry connected-name]{lang="SV"}**]{#struct_0_19941_14702_x1981777019}
:::

::: {#1920342885 .myid}
[]{#_Toc404785161}[]{#struct_0_19941_14702_244641051}[]{#_Toc350155464}[]{#_Toc342653612}

**ISDN \-- ISDN配置命令 \-- isdn carry connected-name**

------------------------------------------------------------------------

[**[isdn carry connected-name]{lang="EN-US"}**]{#struct_0_19941_14702_x1784858662}[命令用来配置]{style="font-family:
宋体"}[ISDN]{lang="EN-US"}[协议在出方向报文中携带]{style="font-family:宋体"}[connected-name]{lang="EN-US"}[字段。]{style="font-family:宋体"}

[**[undo isdn carry connected-name]{lang="EN-US"}**]{#struct_0_19941_14702_992225489}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_158039877}

[**[isdn carry connected-name]{lang="EN-US"}**]{#struct_0_19941_14702_x1379414516}

[**[undo isdn carry connected-name]{lang="EN-US"}**]{#struct_0_19941_14702_961480008}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_862725036}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1913015724}[协议在出方向报文中不携带]{style="font-family:宋体"}[connected-name]{lang="EN-US"}[字段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x261332232}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_796396060}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_326187823}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x730356473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x2102396652}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x697897383}

[[在被叫方配置本命令后，主叫方可以看到被叫方的名字。]{style="font-family:宋体"}]{#struct_0_19941_14702_x1378955764}

[[当]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_126310253}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x897696542}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x816181343}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[在出方向报文中携带]{style="font-family:宋体"}[connected-name]{lang="SV"}[字段。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_2066505083}

[\[Sysname\] interface bri 2/4/0]{lang="SV"}

[\[Sysname-Bri2/4/0\] isdn carry connected-name]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_170233453}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[isdn carry calling-name]{lang="SV"}**]{#struct_0_19941_14702_x1320683915}
:::

::: {#1609759153 .myid}
[]{#_Toc404785162}[]{#struct_0_19941_14702_x1575815690}[]{#_Toc353443108}[]{#_Toc350155465}[]{#_Toc261877520}

**ISDN \-- ISDN配置命令 \-- isdn check-called-number**

------------------------------------------------------------------------

[**[isdn check-called-number]{lang="EN-US"}**]{#struct_0_19941_14702_x1379021300}[命令用来设置入呼叫时需要检查的被叫号码或子地址。]{style="font-family:
宋体"}

[**[undo isdn check-called-number]{lang="EN-US"}**]{#struct_0_19941_14702_x1898366247}[命令用来取消已有的设置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x550175366}

[**[isdn check-called-number ]{lang="EN-US"}***[check-index called-party-number]{lang="EN-US"}*]{#struct_0_19941_14702_902146812}

[**[undo isdn check-called-numbe]{lang="EN-US"}**[r *check-index*]{lang="EN-US"}]{#struct_0_19941_14702_x2042300962}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379086836}

[[入呼叫时不对被叫号码或子地址进行检查。]{style="font-family:宋体"}]{#struct_0_19941_14702_1392238726}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_522302485}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_522473579}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1602304597}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1379152372}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1064693006}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_773309983}

[*[check-index]{lang="EN-US"}*]{#struct_0_19941_14702_1294937040}[：被叫号码或子地址检查的索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[called-party-number]{lang="EN-US"}*]{#struct_0_19941_14702_2141768741}[：被叫号码和子地址，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[个字符的字符串，区分大小写。被叫号码和子地址之间以冒号分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1378693620}

[[本命令用于设置入呼叫时的检查项。可以只配置被叫号码，也可以同时配置被叫号码和子地址。]{style="font-family:宋体"}]{#struct_0_19941_14702_x915671490}

[[只要设定了被叫号码或者子地址，当对方未发送或发送错被叫号码或者子地址时，设备就会拒绝该呼叫。]{style="font-family:宋体"}]{#struct_0_19941_14702_399334987}

[[同时配置被叫号码和子地址时，被叫号码和子地址之间以冒号分隔。]{style="font-family:宋体"}]{#struct_0_19941_14702_30226002}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x580115485}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_1501662053}[设置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[数字入呼叫时检查号码为]{style="font-family:宋体"}[66668888]{lang="EN-US"}[，子地址为]{style="font-family:宋体"}[13525]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1378759156}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn check-called-number 1 66668888:13525]{lang="EN-US"}
:::

::: {#1270560392 .myid}
[]{#_Toc404785163}[]{#struct_0_19941_14702_x305315675}

**ISDN \-- ISDN配置命令 \-- isdn crlength**

------------------------------------------------------------------------

[**[isdn crlength]{lang="EN-US"}**]{#struct_0_19941_14702_x1973536753}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口发起呼叫时所使用呼叫参考的长度。]{style="font-family:宋体"}

[**[undo isdn crlength]{lang="EN-US"}**]{#struct_0_19941_14702_x400049865}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_733678063}

[**[isdn crlength]{lang="EN-US"}**[ ]{lang="EN-US"}*[call-reference-length]{lang="EN-US"}*]{#struct_0_19941_14702_2053569231}

[**[undo isdn crlength]{lang="EN-US"}**]{#struct_0_19941_14702_x1522382611}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x197184891}

[[CE1 PRI]{lang="EN-US"}]{#struct_0_19941_14702_x61933561}[接口和]{style="font-family:宋体"}[CT1 PRI]{lang="EN-US"}[接口的呼叫参考的长度为]{style="font-family:宋体"}[2]{lang="EN-US"}[字节，]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的呼叫参考的长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1379217907}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x190023185}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_1554040680}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_625157384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x296245006}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x733707436}

[*[call-reference-length]{lang="EN-US"}*]{#struct_0_19941_14702_2057798881}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口发起呼叫时所使用呼叫参考的长度，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x647447231}

[[呼叫参考相当于协议为每个呼叫分配的序列号，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19941_14702_x1084241335}[或]{style="font-family:宋体"}[2]{lang="EN-US"}[字节，循环使用。]{style="font-family:
宋体"}

[[通常情况下，当设备收到呼叫时，可以自动识别呼叫参考的长度。但是网络上的某些设备不能自动识别呼叫参考的长度，当本地设备与这种设备对接并向其发出呼叫时，就需要配置本地设备呼叫时所使用的呼叫参考长度与对端一致。]{style="font-family:宋体"}]{#struct_0_19941_14702_x1379283443}

[[当]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_235182451}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x516078307}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x144476528}[配置]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[Serial2/3/0:15]{lang="EN-US"}[上]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[消息所带的呼叫参考的长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1179560530}

[\[Sysname\] interface serial 2/3/0:15]{lang="EN-US"}

[\[Sysname-Serial2/3/0:15\] isdn crlength 1]{lang="EN-US"}
:::

::: {#1614020913 .myid}
[]{#_Toc404785164}[]{#struct_0_19941_14702_x1320408031}[]{#_Toc325546169}[]{#_Toc54583766}

**ISDN \-- ISDN配置命令 \-- isdn ignore connect-ack**

------------------------------------------------------------------------

[**[isdn ignore connect-ack incoming]{lang="EN-US"}**]{#struct_0_19941_14702_x1283577445}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议在发送了]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后无需等待程控交换机的]{style="font-family:宋体"}[CONNECT ACK]{lang="EN-US"}[消息，直接切换到]{style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态，并开始数据和语音业务的通信。]{style="font-family:宋体"}

[**[undo isdn ignore connect-ack incoming]{lang="EN-US"}**]{#struct_0_19941_14702_1942973920}[命令用来恢复]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议在发送]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后的缺省处理方式。]{style="font-family:宋体"}

[**[isdn ignore connect-ack outgoing]{lang="EN-US"}**]{#struct_0_19941_14702_1818545682}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议在收到]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后，不向对端发送]{style="font-family:宋体"}[CONNECT ACK]{lang="EN-US"}[消息，直接切换到]{style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[**[undo isdn ignore connect-ack outgoing]{lang="EN-US"}**]{#struct_0_19941_14702_x1379348979}[命令用来恢复]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议在收到]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后的缺省处理方式。]{style="font-family:宋体"}

[**[isdn ignore connect-ack]{lang="EN-US"}**]{#struct_0_19941_14702_x336053442}[命令的作用相当于同时配置命令]{style="font-family:宋体"}**[isdn ignore connect-ack incoming]{lang="EN-US"}**[和]{style="font-family:
宋体"}**[isdn ignore connect-ack outgoing]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[undo isdn ignore connect-ack]{lang="EN-US"}**]{#struct_0_19941_14702_127751750}[命令用来恢复]{style="font-family:
宋体"}[ISDN]{lang="EN-US"}[协议在发送和收到]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后的缺省处理方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x988644501}

[**[isdn ignore connect-ack]{lang="EN-US"}**[ \[ **incoming** \| **outgoing** \]]{lang="EN-US"}]{#struct_0_19941_14702_x1000990824}

[**[undo isdn ignore connect-ack]{lang="EN-US"}**[ \[ **incoming** \| **outgoing** \]]{lang="EN-US"}]{#struct_0_19941_14702_x1150731826}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_963657846}

[[当设备和程控交换机互通时：]{style="font-family:宋体"}]{#struct_0_19941_14702_1984223093}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_105644816}[协议在发送了]{lang="EN-US" style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后，需要等待接收到程控交换机的]{lang="EN-US" style="font-family:宋体"}[CONNECT ACK]{lang="EN-US"}[消息后才切换到]{lang="EN-US" style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态，并开始数据和语音业务的通信。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1379414515}[协议在收到]{lang="EN-US" style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后，需要向对端回应]{lang="EN-US" style="font-family:宋体"}[CONNECT ACK]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}[，并]{style="font-family:宋体"}[切换到]{lang="EN-US" style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1767403347}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_981723712}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1062430840}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1775448393}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1727885389}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1929138927}

[**[incoming]{lang="EN-US"}**]{#struct_0_19941_14702_x315925458}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议在发送]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后，无需等待程控交换机的]{style="font-family:宋体"}[CONNECT ACK]{lang="EN-US"}[消息，直接切换到]{style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[**[outgoing]{lang="EN-US"}**]{#struct_0_19941_14702_2083139792}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议在收到]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息之后，不向对端发送]{style="font-family:宋体"}[CONNECT ACK]{lang="EN-US"}[消息，直接切换到]{style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x824559014}

[[当设备和程控交换机互通时，应与程控交换机的设置一致。]{style="font-family:宋体"}]{#struct_0_19941_14702_x1378955763}

[[当]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_2048624554}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x464362192}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1931408862}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上呼叫过程无需等待]{style="font-family:宋体"}[CONNECT ACK]{lang="EN-US"}[消息直接切换到]{style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1681638379}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn ignore connect-ack incoming]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_164944037}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上呼叫过程不发送]{style="font-family:宋体"}[CONNECT ACK]{lang="EN-US"}[消息直接切换到]{style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1303690416}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn ignore connect-ack outgoing]{lang="EN-US"}
:::

::: {#-241370587 .myid}
[]{#_Toc404785165}[]{#struct_0_19941_14702_1637308546}[]{#_Toc325546170}[]{#_Toc54583767}

**ISDN \-- ISDN配置命令 \-- isdn ignore hlc**

------------------------------------------------------------------------

[**[isdn ignore hlc]{lang="EN-US"}**]{#struct_0_19941_14702_x1379021299}[命令用来配置在]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[发起语音呼叫时]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息中不携带高层兼容性信息单元。]{style="font-family:宋体"}

[**[undo isdn ignore hlc]{lang="EN-US"}**]{#struct_0_19941_14702_x688971419}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_661699048}

[**[isdn ignore hlc]{lang="EN-US"}**]{#struct_0_19941_14702_1880025150}

[**[undo isdn ignore hlc]{lang="EN-US"}**]{#struct_0_19941_14702_1303101052}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1412130709}

[[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x669799970}[I]{lang="SV"}[SDN]{lang="EN-US"}[协议为]{style="font-family:宋体"}[5ESS]{lang="SV"}[、]{style="font-family:宋体"}[QSIG]{lang="SV"}[时都不携带]{style="font-family:
宋体"}[高层兼容性信息单元，在其他]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议下都携带高层兼容性信息单元。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_1910894890}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1859770000}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1424743248}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1379086835}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_1795523253}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_480574003}

[[当设备和程控交换机互通时，应与程控交换机的设置一致。]{style="font-family:宋体"}]{#struct_0_19941_14702_1264062281}

[[当]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x223527686}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_2034142374}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x173018776}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上发起语音呼叫时在]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息中不携带高层兼容性单元。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1564975936}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn ignore hlc]{lang="EN-US"}
:::

::: {#-241370583 .myid}
[]{#_Toc404785166}[]{#struct_0_19941_14702_x597016855}[]{#_Toc325546171}[]{#_Toc54583768}

**ISDN \-- ISDN配置命令 \-- isdn ignore llc**

------------------------------------------------------------------------

[**[isdn ignore llc]{lang="EN-US"}**]{#struct_0_19941_14702_x1379152371}[命令用来配置在]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[发起语音呼叫时]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息中不携带低层兼容性信息单元。]{style="font-family:宋体"}

[**[undo isdn ignore llc]{lang="EN-US"}**]{#struct_0_19941_14702_501390935}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1008477012}

[**[isdn ignore llc]{lang="EN-US"}**]{#struct_0_19941_14702_437551414}

[**[undo isdn ignore llc]{lang="EN-US"}**]{#struct_0_19941_14702_860222103}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_2024190540}

[[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x1503189254}[I]{lang="SV"}[SDN]{lang="EN-US"}[协议为]{style="font-family:宋体"}[5ESS]{lang="SV"}[、]{style="font-family:宋体"}[QSIG]{lang="SV"}[时都不携带]{style="font-family:
宋体"}[低层兼容性信息单元，在其他]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议下都携带低层兼容性信息单元。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_353669279}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1115158025}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2085770788}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1378693619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x2125590607}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2026723363}

[[当设备和程控交换机互通时，应与程控交换机的设置一致。]{style="font-family:宋体"}]{#struct_0_19941_14702_210841867}

[[当]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x149898044}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_1198372518}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_610430875}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上发起语音呼叫时在]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息中不携带低层兼容性单元。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1440568675}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn ignore llc]{lang="EN-US"}
:::

::: {#1246379512 .myid}
[]{#_Toc404785167}[]{#struct_0_19941_14702_158656776}[]{#_Toc325546172}[]{#_Toc54583769}

**ISDN \-- ISDN配置命令 \-- isdn ignore sending-complete**

------------------------------------------------------------------------

[**[isdn ignore sending-complete]{lang="EN-US"}**]{#struct_0_19941_14702_x1378759155}[命令用来配置]{style="font-family:
宋体"}[ISDN]{lang="EN-US"}[协议在入呼叫和出呼叫方向上对发送完全信息单元（]{style="font-family:宋体"}[Sending Complete Information Element]{lang="EN-US"}[）的处理。]{style="font-family:
宋体"}

[**[undo isdn ignore sending-complete]{lang="EN-US"}**]{#struct_0_19941_14702_1260768266}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_2016521881}

[**[isdn ignore sending-complete]{lang="EN-US"}**[ \[ **incoming** \| **outgoing** \]]{lang="EN-US"}]{#struct_0_19941_14702_1594197028}

[**[undo isdn ignore sending-complete]{lang="EN-US"}**[ \[ **incoming** \| **outgoing** \]]{lang="EN-US"}]{#struct_0_19941_14702_1764871466}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_1981335396}

[[当设备和程控交换机互通时，对于入呼叫，检查接收到的]{style="font-family:宋体"}[Setup]{lang="EN-US"}]{#struct_0_19941_14702_1888140949}[消息是否携带发送完全信息单元，对于出呼叫，发送]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息时携带发送完全信息单元。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x823429289}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x876602669}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_186866037}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1844030589}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1854161338}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_90288965}

[**[incoming]{lang="EN-US"}**]{#struct_0_19941_14702_581909469}[：对于入呼叫，不检查接收到的]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息是否携带发送完全信息单元。]{style="font-family:宋体"}

[**[outgoing]{lang="EN-US"}**]{#struct_0_19941_14702_1110296212}[：对于出呼叫，发送]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息时不携带发送完全信息单元。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_1305669276}

[[发送完全信息单元的作用如下：]{style="font-family:宋体"}]{#struct_0_19941_14702_x401457900}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[出呼叫发送]{style="font-family:宋体"}]{#struct_0_19941_14702_x16625869}[Setup]{lang="EN-US"}[消息时，如果]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息中携带发送完全信息单元，表示号码完全发送，否则，表示号码没有完全发送。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[入呼叫收到]{style="font-family:宋体"}]{#struct_0_19941_14702_186800501}[Setup]{lang="EN-US"}[消息时，如果]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息中携带发送完全信息单元，表示号码完全接收，否则，表示号码没有完全接收。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_1267112658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置命令时不指定]{lang="EN-US" style="font-family:宋体"}**[incoming]{lang="EN-US"}**]{#struct_0_19941_14702_65420520}[和]{lang="EN-US" style="font-family:宋体"}**[outgoing]{lang="EN-US"}**[参数，表示对于入呼叫和出呼叫都进行处理。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备和程控交换机互通时，应与程控交换机的设置一致。]{style="font-family:宋体"}]{#struct_0_19941_14702_1872579070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只能在接口]{style="font-family:宋体"}]{#struct_0_19941_14702_1880103660}[ISDN]{lang="EN-US"}[协议为]{style="font-family:宋体"}[DSS1]{lang="EN-US"}[、]{style="font-family:宋体"}[QSIG]{lang="SV"}[或者]{style="font-family:
宋体"}[ETSI]{lang="SV"}[时有意义，其他协议不支持该信息单元]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x1371667782}[ISDN]{lang="EN-US"}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1698025269}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x1859534402}[配置]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[接口对于入呼叫，不检查接收到的]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息是否携带发送完全信息单元。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x782742350}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn ignore sending-complete incoming]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_186734965}[配置]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[接口对于出呼叫，发送]{style="font-family:宋体"}[Setup]{lang="EN-US"}[消息时不携带发送完全信息单元。]{style="font-family:宋体"}

[[\[Sysname-Bri2/4/0\] isdn ignore sending-complete outgoing]{lang="EN-US"}]{#struct_0_19941_14702_1910514607}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2069834002}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn protocol-type]{lang="EN-US"}**]{#struct_0_19941_14702_x1833624690}
:::

::: {#1004680360 .myid}
[]{#_Toc404785168}[]{#struct_0_19941_14702_x1920004886}[]{#_Toc350155471}[]{#_Toc342653618}

**ISDN \-- ISDN配置命令 \-- isdn l3-timer**

------------------------------------------------------------------------

[**[isdn l3-timer]{lang="EN-US"}**]{#struct_0_19941_14702_x341743288}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议三层定时器的时长。]{style="font-family:宋体"}

[**[undo isdn l3-timer]{lang="EN-US"}**]{#struct_0_19941_14702_1277926622}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x593236096}

[**[isdn l3-timer]{lang="DA"}**]{#struct_0_19941_14702_734662321}[ *timer-name time-interval*]{lang="DA"}

[**[undo isdn l3-timer]{lang="DA"}**]{#struct_0_19941_14702_186669429}[ { *timer-name* \| **all** }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1658051075}

[[不同类型]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1213487340}[协议的三层定时器时长的缺省值不同，用户可以通过]{style="font-family:宋体"}**[display isdn parameters]{lang="EN-US"}**[命令查看各]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议的三层定时器时长的缺省值。]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-6]{lang="EN-US"}](?1004680360#_Ref350177789)[中列出的是]{style="font-family:
宋体"}[DSS1 ISDN]{lang="EN-US"}[协议的三层定时器时长的缺省值。]{style="font-family:宋体"}[]{#_Ref247971311}[]{#_Toc95359216}[]{#_Toc85604326}[]{#_Toc81386705}[]{#_Toc74661828}[]{#_Toc72589791}[]{#_Toc72589518}[]{#_Toc72589003}[]{#_Toc65921173}[]{#_Toc65919121}[]{#_Toc65919096}[]{#_Toc65910730}[]{#_Toc65909975}[]{#_Toc60125185}[]{#_表1-6_ISDN协议三层定时器说明}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_1658157368}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1207170234}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_510731210}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1620322771}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_1102716217}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_1051659456}

[*[timer-name]{lang="DA"}*]{#struct_0_19941_14702_2125223175}[：]{style="font-family:宋体"}[ISDN]{lang="DA"}[协议三层定时器名字，取值范围见]{style="font-family:
宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-6]{lang="EN-US"}](?1004680360#_Ref350177789)[。]{style="font-family:宋体"}

[*[time-interval]{lang="DA"}*]{#struct_0_19941_14702_187128181}[：定时器时长，取值范围见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-6]{lang="EN-US"}](?1004680360#_Ref350177789)[。]{style="font-family:宋体"}

[**[all]{lang="DA"}**]{#struct_0_19941_14702_1248182445}[：用于恢复所有三层定时器的缺省时长。]{style="font-family:宋体"}

[]{#struct_0_19941_14702_x1795990907}[[表1-6 ]{lang="EN-US"}[ISDN]{lang="EN-US"}]{#_Ref350177789}[协议三层定时器说明]{style="font-family:黑体"}

[]{#table_struct_0_1762075975}[*[timer-name]{lang="EN-US"}*]{#struct_0_19941_14702_x845011262}
:::

[[定时器名]{style="font-family:黑体"}]{#struct_0_19941_14702_x472349437}

[[取值范围（单位：秒）]{style="font-family:黑体"}]{#struct_0_19941_14702_347728046}

[[缺省值（单位：秒）]{style="font-family:黑体"}]{#struct_0_19941_14702_428289089}

[[t301]{lang="EN-US"}]{#struct_0_19941_14702_187062645}

[[T301]{lang="EN-US"}]{#struct_0_19941_14702_x1165430686}

[[30]{lang="EN-US"}]{#struct_0_19941_14702_976830789}[～]{style="font-family:宋体"}[1200]{lang="EN-US"}

[[240]{lang="EN-US"}]{#struct_0_19941_14702_x1475435974}

[[t302]{lang="EN-US"}]{#struct_0_19941_14702_x875683403}

[[T302]{lang="EN-US"}]{#struct_0_19941_14702_942241628}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1626904634}[～]{style="font-family:宋体"}[60]{lang="EN-US"}

[[15]{lang="EN-US"}]{#struct_0_19941_14702_186997109}

[[t303]{lang="EN-US"}]{#struct_0_19941_14702_x285292727}

[[T303]{lang="EN-US"}]{#struct_0_19941_14702_812014352}

[[2]{lang="EN-US"}]{#struct_0_19941_14702_121351003}[～]{style="font-family:宋体"}[10]{lang="EN-US"}

[[4]{lang="EN-US"}]{#struct_0_19941_14702_1666581633}

[[t304]{lang="EN-US"}]{#struct_0_19941_14702_x1459894332}

[[T304]{lang="EN-US"}]{#struct_0_19941_14702_186931573}

[[10]{lang="EN-US"}]{#struct_0_19941_14702_x667706631}[～]{style="font-family:宋体"}[60]{lang="EN-US"}

[[30]{lang="EN-US"}]{#struct_0_19941_14702_2108022021}

[[t305]{lang="EN-US"}]{#struct_0_19941_14702_x512217547}

[[T305]{lang="EN-US"}]{#struct_0_19941_14702_532366993}

[[4]{lang="EN-US"}]{#struct_0_19941_14702_187390325}[～]{style="font-family:宋体"}[30]{lang="EN-US"}

[[30]{lang="EN-US"}]{#struct_0_19941_14702_x486496128}

[[t308]{lang="EN-US"}]{#struct_0_19941_14702_1714302498}

[[T308]{lang="EN-US"}]{#struct_0_19941_14702_258481160}

[[2]{lang="EN-US"}]{#struct_0_19941_14702_860020259}[～]{style="font-family:宋体"}[10]{lang="EN-US"}

[[4]{lang="EN-US"}]{#struct_0_19941_14702_187324789}

[[t309]{lang="EN-US"}]{#struct_0_19941_14702_683441223}

[[T309]{lang="EN-US"}]{#struct_0_19941_14702_x2002001845}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1207085342}[～]{style="font-family:宋体"}[240]{lang="EN-US"}

[[90]{lang="EN-US"}]{#struct_0_19941_14702_1297024017}

[[t310]{lang="EN-US"}]{#struct_0_19941_14702_186866038}

[[T310]{lang="EN-US"}]{#struct_0_19941_14702_x1844030574}

[[10]{lang="EN-US"}]{#struct_0_19941_14702_2038242327}[～]{style="font-family:宋体"}[240]{lang="EN-US"}

[[40]{lang="EN-US"}]{#struct_0_19941_14702_692646284}

[[t313]{lang="EN-US"}]{#struct_0_19941_14702_186800502}

[[T313]{lang="EN-US"}]{#struct_0_19941_14702_1267112661}

[[2]{lang="EN-US"}]{#struct_0_19941_14702_66010341}[～]{style="font-family:宋体"}[10]{lang="EN-US"}

[[4]{lang="EN-US"}]{#struct_0_19941_14702_x189733452}

[[t322]{lang="EN-US"}]{#struct_0_19941_14702_488689775}

[[T322]{lang="EN-US"}]{#struct_0_19941_14702_186734966}

[[2]{lang="EN-US"}]{#struct_0_19941_14702_1910514608}[～]{style="font-family:宋体"}[10]{lang="EN-US"}

[[4]{lang="EN-US"}]{#struct_0_19941_14702_x2069637394}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1415290901}

[[T302]{lang="EN-US"}]{#struct_0_19941_14702_1155533751}[、]{style="font-family:宋体"}[T304]{lang="EN-US"}[定时器和重叠发送有关，如果当前]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[网络层协议不支持重叠发送则不支持该定时器配置。]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[、]{style="font-family:宋体"}[NTT]{lang="EN-US"}[、]{style="font-family:宋体"}[NI2]{lang="EN-US"}[、]{style="font-family:宋体"}[5ESS]{lang="EN-US"}[协议不支持]{style="font-family:宋体"}[T302]{lang="SV"}[、]{style="font-family:宋体"}[T304]{lang="SV"}[定时器配置。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_186669430}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_680601078}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议的]{style="font-family:宋体"}[T301]{lang="EN-US"}[定时器的时长为]{style="font-family:宋体"}[160]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_19941_14702_x50657683}

[\[Sysname\] interface bri 2/4/0]{lang="DA"}

[\[Sysname-Bri2/4/0\] isdn l3-timer t301 160]{lang="DA"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x596256135}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display isdn parameters]{lang="EN-US"}**]{#struct_0_19941_14702_x1465184585}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn overlap-sending]{lang="EN-US"}**]{#struct_0_19941_14702_702312831}

::: {#-144768435 .myid}
[]{#_Toc350155473}[]{#_Toc342653621}[]{#_Toc153009863}[]{#_Toc404785169}[]{#struct_0_19941_14702_2146746132}[]{#_Toc353443115}[]{#_Toc350155472}

**ISDN \-- ISDN配置命令 \-- isdn link-mode p2p**

------------------------------------------------------------------------

[**[isdn ]{lang="EN-US"}**]{#struct_0_19941_14702_187128182}[**[link-mode]{lang="EN-US"}**]{#OLE_LINK5}**[ p2p]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口工作在点到点模式下。]{style="font-family:宋体"}

[**[undo isdn link-mode]{lang="EN-US"}**]{#struct_0_19941_14702_1248182444}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1795925371}

[**[isdn link-mode p2p]{lang="EN-US"}**]{#struct_0_19941_14702_x282896447}

[**[undo isdn link-mode]{lang="EN-US"}**]{#struct_0_19941_14702_187062646}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1165430687}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x589253152}[接口工作在点到多点模式下。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1366175831}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_186997110}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_1671022400}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_669785660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_200353125}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_186931574}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x667706638}[接口有两种工作模式：点到点、点到多点。工作在点到点模式下的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口只能连接一台终端设备，工作在点到多点的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口可以连接多台终端设备。]{style="font-family:宋体"}

[[某些程控交换机只能工作在点到点模式下，为了互通，需要配置]{style="font-family:宋体"}[BRI]{lang="EN-US"}]{#struct_0_19941_14702_2108611845}[接口工作在点到点模式下。当一个]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口通过程控交换机连接多台]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[电话时，需要配置]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口工作在点到多点模式下。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_603294794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}]{#struct_0_19941_14702_187390326}[接口配置了]{lang="EN-US" style="font-family:宋体"}**[isdn two-tei]{lang="EN-US"}**[命令时，不]{lang="EN-US" style="font-family:宋体"}[能]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[接口工作在点到点模式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x486496131}[BRI]{lang="EN-US"}[接口上存在呼叫时，]{style="font-family:宋体"}[不能配置]{style="font-family:宋体"}[本]{style="font-family:宋体"}[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_1713843745}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x389044657}[配置]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口工作在点到点模式下。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_187324790}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn link-mode p2p]{lang="NL"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1655210928}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn two-tei]{lang="EN-US"}**]{#struct_0_19941_14702_x1174484707}
:::

::: {#1303654043 .myid}
[]{#_Toc404785170}[]{#struct_0_19941_14702_747121513}

**ISDN \-- ISDN配置命令 \-- isdn number-property**

------------------------------------------------------------------------

[**[isdn number-property]{lang="EN-US"}**]{#struct_0_19941_14702_1962113297}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[入呼叫或出呼叫时的主叫号码或被叫号码的号码类型和编码方案。]{style="font-family:宋体"}

[**[undo isdn number-property]{lang="EN-US"}**]{#struct_0_19941_14702_x857558665}[命令用来恢复缺省的]{style="font-family:
宋体"}[ISDN]{lang="EN-US"}[入呼叫或出呼叫时的主叫号码或被叫号码的号码类型和编码方案处理方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1483904836}

[**[isdn number-property]{lang="EN-US"}**[ *number-property* \[ **calling** \| **called** \] \[ **in** \| **out** \]]{lang="EN-US"}]{#struct_0_19941_14702_186866035}

[**[undo isdn number-property]{lang="EN-US"}**[ \[ **calling** \| **called** \] \[ **in** \| **out** \]]{lang="EN-US"}]{#struct_0_19941_14702_x1844030587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_1634236904}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_232598566}[号码类型和编码方案的缺省处理方式为：根据上层具体业务的不同，系统采用相应的号码类型和编码方案。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_1669122111}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x806798111}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x823028130}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1267292851}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x476542809}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_70904726}

[*[number-property]{lang="EN-US"}*]{#struct_0_19941_14702_186800499}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[号码的号码类型和编码方案，取值范围为十六进制的]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7F]{lang="EN-US"}[。用]{style="font-family:宋体"}[8]{lang="EN-US"}[比特的格式表示时，其中]{style="font-family:宋体"}[1-4]{lang="EN-US"}[位为编码方案，]{style="font-family:宋体"}[5-7]{lang="EN-US"}[位为号码类型，第]{style="font-family:宋体"}[8]{lang="EN-US"}[位为保留位。号码类型和编码方案的值见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-7]{lang="EN-US"}](?1303654043#_Ref350178785)[，更加详细的定义请参考相关协议中的描述。]{style="font-family:宋体"}

[**[calling]{lang="EN-US"}**]{#struct_0_19941_14702_x1888737745}[：配置主叫号码所固定使用的号码类型以及编码方案。]{style="font-family:宋体"}

[**[called]{lang="EN-US"}**]{#struct_0_19941_14702_x360869584}[：配置被叫号码所固定使用的号码类型以及编码方案。]{style="font-family:宋体"}

[**[in]{lang="EN-US"}**]{#struct_0_19941_14702_x2088701549}[：配置入呼叫时的]{style="font-family:宋体"}[calling]{lang="EN-US"}[、]{style="font-family:宋体"}[called]{lang="EN-US"}[号码所固定使用的号码类型以及编码方案。]{style="font-family:宋体"}

[**[out]{lang="EN-US"}**]{#struct_0_19941_14702_470667087}[：配置出呼叫时的]{style="font-family:宋体"}[calling]{lang="EN-US"}[、]{style="font-family:宋体"}[called]{lang="EN-US"}[号码所固定使用的号码类型以及编码方案。]{style="font-family:宋体"}

[]{#struct_0_19941_14702_x1927737427}[]{#_Ref350178785}[[表1-7 ]{lang="EN-US"}[ISDN]{lang="EN-US"}]{#_Toc60111185}[号码的号码类型和编码方案]{style="font-family:黑体"}

[]{#table_struct_0_1793785869}[[协议]{style="font-family:黑体"}]{#struct_0_19941_14702_x1257743393}
:::

[[字段（位）值]{style="font-family:黑体"}]{#struct_0_19941_14702_186734963}

[[定义]{style="font-family:黑体"}]{#struct_0_19941_14702_1910514613}

[ ]{lang="EN-US"}

[[号码类型]{style="font-family:黑体"}]{#struct_0_19941_14702_x2070096145}

[[编码方案]{style="font-family:黑体"}]{#struct_0_19941_14702_586299861}

[[8]{lang="EN-US"}]{#struct_0_19941_14702_x1345151766}

[[7]{lang="EN-US"}]{#struct_0_19941_14702_x249455145}

[[6]{lang="EN-US"}]{#struct_0_19941_14702_x1013664895}

[[5]{lang="EN-US"}]{#struct_0_19941_14702_186669427}

[[4]{lang="EN-US"}]{#struct_0_19941_14702_x1658051089}

[[3]{lang="EN-US"}]{#struct_0_19941_14702_x756602024}

[[2]{lang="EN-US"}]{#struct_0_19941_14702_x803862126}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1784285362}

[[AT&T]{lang="EN-US"}]{#struct_0_19941_14702_187128179}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_56541349}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x1202109851}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1389377540}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_333043042}

[[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x650638053}

[[号码类型：]{style="font-family:宋体"}]{#struct_0_19941_14702_187062643}

[[编码方案：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_x1165430684}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x185968625}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x389635979}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_186997107}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x285292733}

[[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_811752207}

[[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_974468400}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan( Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_771002063}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_186931571}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x667706633}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2108153093}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x2097634700}

[[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x1981956742}

[[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_187390323}

[[编码方案：]{style="font-family:宋体"}[Data numbering plan( Recommendation X.121)]{lang="EN-US"}]{#struct_0_19941_14702_x486496134}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1714040353}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1691024087}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_187324787}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_683441233}

[[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_336650315}

[[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_990620029}

[[编码方案：]{style="font-family:宋体"}[Telex numbering plan( Recommendation F.69)]{lang="EN-US"}]{#struct_0_19941_14702_186866036}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1844030588}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x288077397}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_519610830}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_186800500}

[[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1267112659}

[[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_65486056}

[[编码方案：]{style="font-family:宋体"}[National standard numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_x869870243}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_186734964}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1910514606}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x2069768466}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_186669428}

[[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x1658051074}

[[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_x352596601}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_187128180}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1248182446}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1795794299}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_187062644}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1165430685}

[[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x1752052566}

[[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_771862071}

[[编码方案：]{style="font-family:宋体"}[Reserved for extension]{lang="EN-US"}]{#struct_0_19941_14702_186997108}

[[ANSI]{lang="EN-US"}]{#struct_0_19941_14702_x285292728}

[[ETSI]{lang="EN-US"}]{#struct_0_19941_14702_812342032}

[[DSS1]{lang="EN-US"}]{#struct_0_19941_14702_186931572}

[[NTT]{lang="EN-US"}]{#struct_0_19941_14702_x667706632}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2108218629}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_187390324}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x486496129}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1714368034}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_187324788}

[[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_683441224}

[[编码方案：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_x2002001844}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_186866033}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x1844030585}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_186800497}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1888737731}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1964794780}

[[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_186734961}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan( Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_1910514611}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x2070227217}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_186669425}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1658051087}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1919401438}

[**[步骤1[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_187128177}

[**[步骤2[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_56541359}

[[编码方案：]{style="font-family:宋体"}[Data numbering plan( Recommendation X.121)]{lang="EN-US"}]{#struct_0_19941_14702_187062641}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x1165430682}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_186997105}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x285292731}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_811883279}

[**[步骤3[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_186931569}

[**[步骤4[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_1670945519}

[[编码方案：]{style="font-family:宋体"}[Telex numbering plan( Recommendation F.69)]{lang="EN-US"}]{#struct_0_19941_14702_187390321}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x486496132}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1713909281}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_187324785}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_683441235}

[**[步骤5[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_186866034}

[**[步骤6[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_x1844030586}

[[编码方案：]{style="font-family:宋体"}[National standard numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_x1094646451}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_186800498}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x1888737744}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_186734962}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1910514612}

[**[步骤7[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_186669426}

[**[步骤8[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_x1658051088}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_187128178}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_56541350}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_187062642}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1165430683}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1736345676}

[**[步骤9[    ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_186997106}

[**[步骤10[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_x285292734}

[[编码方案：]{style="font-family:宋体"}[Reserved for extension]{lang="EN-US"}]{#struct_0_19941_14702_186931570}

[[NI]{lang="EN-US"}]{#struct_0_19941_14702_x667706634}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_187390322}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x486496135}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_187324786}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_683441234}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109180338}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x542894331}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109114802}

[**[步骤11[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_983951732}

[**[步骤12[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_2109049266}

[[编码方案：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_593637602}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2108983730}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x908353150}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109442482}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x506057041}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109376946}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1772617720}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109311410}

[**[步骤13[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x906917024}

[**[步骤14[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_2109245874}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan( Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x584819159}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109704626}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x921376328}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109639090}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_218312983}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109180339}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x542828795}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109114803}

[**[步骤15[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_983886196}

[**[步骤16[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_2109049267}

[[编码方案：]{style="font-family:宋体"}[Data numbering plan( Recommendation X.121)]{lang="EN-US"}]{#struct_0_19941_14702_2108983731}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x908287614}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109442483}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x505991505}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109376947}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1772552184}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109311411}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x906982560}

[**[步骤17[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_2109245875}

[**[步骤18[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_2109704627}

[[编码方案：]{style="font-family:宋体"}[Telex numbering plan (Recommendation F.69)]{lang="EN-US"}]{#struct_0_19941_14702_x921310792}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109639091}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_218247447}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109180336}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x543287547}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109114800}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109049264}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_593768674}

[**[步骤19[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_2108983728}

[**[步骤20[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_x907828861}

[[编码方案：]{style="font-family:宋体"}[National standard numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_2109442480}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109376944}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1772748792}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109311408}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x907441311}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109245872}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109704624}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x921245256}

[**[步骤21[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_2109639088}

[**[步骤22[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_2109180337}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_x543222011}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109114801}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109049265}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_593834210}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2108983729}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x907763325}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109442481}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109376945}

[**[步骤23[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1772683256}

[**[步骤24[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_2109311409}

[[编码方案：]{style="font-family:宋体"}[Reserved for extension]{lang="EN-US"}]{#struct_0_19941_14702_2109245873}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x584622551}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109704625}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109639089}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_217723158}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109180334}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109114798}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1027926395}

[**[步骤25[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_2109049262}

[**[步骤26[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[National number]{lang="EN-US"}]{#struct_0_19941_14702_2108983726}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan( Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x908222077}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109442478}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109376942}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1772879864}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109311406}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109245870}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x584557015}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109704622}

[**[步骤27[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_2109639086}

[**[步骤28[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Network specific number]{lang="EN-US"}]{#struct_0_19941_14702_2109180335}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan( Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x543090939}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109114799}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109049263}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_593965282}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2108983727}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109442479}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_2109376943}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1772814328}

[**[步骤29[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_2109311407}

[**[步骤30[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_2109245871}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan( Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_2109704623}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x921572936}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_2109639087}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619703017}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1376160531}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619768553}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619834089}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619899625}

[**[步骤31[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x256703649}

[**[步骤32[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Abbreviated number]{lang="EN-US"}]{#struct_0_19941_14702_x619440873}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_x619506409}

[[NI2]{lang="EN-US"}]{#struct_0_19941_14702_x619571945}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619637481}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_187320193}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619178729}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619244265}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619703016}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x1376094995}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619768552}

[**[步骤33[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x619834088}

[**[步骤34[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_x619899624}

[[编码方案：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_x619440872}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x241118557}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619506408}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619571944}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619637480}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619178728}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_161380083}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619244264}

[**[步骤35[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x619703019}

[**[步骤36[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[International number]{lang="EN-US"}]{#struct_0_19941_14702_x619768555}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan (Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x619834091}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_548709781}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619899627}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619440875}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619506411}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619571947}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619637483}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_187451265}

[**[步骤37[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x619178731}

[**[步骤38[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[National number]{lang="EN-US"}]{#struct_0_19941_14702_x619244267}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan (Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x619703018}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619768554}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619834090}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_548644245}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619899626}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619440874}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619506410}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619571946}

[**[步骤39[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x619637482}

[**[步骤40[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Subscriber number]{lang="EN-US"}]{#struct_0_19941_14702_x619178730}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan (Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x619244266}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_937731168}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619703021}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619768557}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619834093}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619899629}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619440877}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619506413}

[**[步骤41[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x1381057614}

[**[步骤42[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[International number]{lang="EN-US"}]{#struct_0_19941_14702_x619571949}

[[编码方案：]{style="font-family:宋体"}[Data numbering plan (Recommendation X.121)]{lang="EN-US"}]{#struct_0_19941_14702_x619637485}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619178733}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619244269}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619703020}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619768556}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619834092}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619899628}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619440876}

[**[步骤43[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x619506412}

[**[步骤44[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Subscriber number]{lang="EN-US"}]{#struct_0_19941_14702_x1380992078}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_x619571948}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619637484}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x619178732}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x619244268}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1759306970}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759372506}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759438042}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1759503578}

[**[步骤45[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759044826}

[**[步骤46[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Abbreviated number]{lang="EN-US"}]{#struct_0_19941_14702_1759110362}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_1759175898}

[[5ESS]{lang="EN-US"}]{#struct_0_19941_14702_1759241434}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759831258}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759896794}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759306971}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[**[步骤47[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759372507}

[**[步骤48[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_1759438043}

[[编码方案：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_1759503579}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759044827}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759110363}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1759175899}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[**[步骤49[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759241435}

[**[步骤50[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[International number]{lang="EN-US"}]{#struct_0_19941_14702_1759831259}

[[编码方案：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_x615469198}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759306968}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1739090323}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759372504}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[**[步骤51[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759438040}

[**[步骤52[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[National number]{lang="EN-US"}]{#struct_0_19941_14702_1759044824}

[[编码方案：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_1759110360}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759175896}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1759241432}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1759831256}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[**[步骤53[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759896792}

[**[步骤54[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Network specific number]{lang="EN-US"}]{#struct_0_19941_14702_1759306969}

[[编码方案：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_1759372505}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1759438041}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759503577}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759044825}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[**[步骤55[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759110361}

[**[步骤56[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Subscriber number]{lang="EN-US"}]{#struct_0_19941_14702_1759175897}

[[编码方案：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_1759241433}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759831257}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759896793}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759372502}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759438038}

[**[步骤57[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759503574}

[**[步骤58[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_1759044822}

[[编码方案：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_1759110358}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759175894}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759241430}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759831254}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1759896790}

[**[步骤59[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759306967}

[**[步骤60[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_1759372503}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan (Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_1759503575}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759044823}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759110359}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_1759175895}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_1759241431}

[**[步骤61[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_1759831255}

[**[步骤62[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_1759896791}

[[编码方案：]{style="font-family:宋体"}[Data numbering plan (Recommendation X.121)]{lang="EN-US"}]{#struct_0_19941_14702_x969576385}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x969510849}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969445313}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969379777}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x969772993}

[**[步骤63[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x969707457}

[**[步骤64[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_19941_14702_x969641921}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_x969052097}

[[QSIG]{lang="EN-US"}]{#struct_0_19941_14702_x968986561}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969576384}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969445312}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969379776}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969838528}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969772992}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969707456}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969641920}

[**[步骤65[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x969052096}

[**[步骤66[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.5pt"}**[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_x969576387}

[[编码方案：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_x969510851}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969445315}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969379779}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969838531}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969772995}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969641923}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969052099}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x968986563}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x969576386}

[[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_x969510850}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan (Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x969379778}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969838530}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969772994}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x969641922}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969052098}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969576389}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969510853}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x969445317}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x969838533}

[[号码类型：]{style="font-family:宋体"}[International number]{lang="EN-US"}]{#struct_0_19941_14702_x969772997}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan (Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x969707461}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969052101}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x968986565}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969576388}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969510852}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969445316}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x969838532}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x969772996}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x969707460}

[[号码类型：]{style="font-family:宋体"}[National number]{lang="EN-US"}]{#struct_0_19941_14702_x969052100}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan (Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_x968986564}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596507556}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596573092}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596704164}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596245412}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596310948}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596376484}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_597031844}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_597097380}

[[号码类型：]{style="font-family:宋体"}[Network specific number]{lang="EN-US"}]{#struct_0_19941_14702_596507557}

[[编码方案：]{style="font-family:宋体"}[ISDN/telephony numbering plan (Recommendation E.164)]{lang="EN-US"}]{#struct_0_19941_14702_596638629}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596704165}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596245413}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596310949}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596442021}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_597031845}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_597097381}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596573090}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_596638626}

[[号码类型：]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_19941_14702_596704162}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_596310946}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596376482}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596442018}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_597097378}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596507555}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596573091}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596704163}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596245411}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_596310947}

[[号码类型：]{style="font-family:宋体"}[International number]{lang="EN-US"}]{#struct_0_19941_14702_596442019}

[[编码方案：]{style="font-family:宋体"}[Level 2 regional number in private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_597031843}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_597097379}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596573088}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596638624}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596245408}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596310944}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596376480}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_597031840}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_597097376}

[[号码类型：]{style="font-family:宋体"}[National number]{lang="EN-US"}]{#struct_0_19941_14702_596507553}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_596638625}

[ ]{lang="EN-US"}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_596704161}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596245409}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596376481}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_596442017}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_597097377}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x2132375799}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x2132310263}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x2132179191}

[[号码类型：]{style="font-family:宋体"}[Network specific number]{lang="EN-US"}]{#struct_0_19941_14702_x2132637943}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_x2132572407}

[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x2132441335}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x2131851511}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x2131785975}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x2132310262}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x2132244726}

[[0]{lang="EN-US"}]{#struct_0_19941_14702_x2132637942}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x2132572406}

[[主叫号码信息单元或者被叫号码信息单元]{style="font-family:宋体"}]{#struct_0_19941_14702_x2132506870}

[[号码类型：]{style="font-family:宋体"}[Subscriber number]{lang="EN-US"}]{#struct_0_19941_14702_x2131851510}

[[编码方案：]{style="font-family:宋体"}[Private numbering plan]{lang="EN-US"}]{#struct_0_19941_14702_x2131785974}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_548869136}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x798303279}[设置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[入呼叫时主叫号码的号码类型为未知]{style="font-family:宋体"}[(Unknown)]{lang="EN-US"}[，编码方案为未知]{style="font-family:宋体"}[(Unknown)]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x2132375801}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn number-property 0 calling in]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x303210332}[设置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[出呼叫时被叫号码的号码类型为未知，编码方案为未知。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_1721299133}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn number-property 0 called out]{lang="EN-US"}

::: {#-1702795099 .myid}
[]{#_Toc404785171}[]{#struct_0_19941_14702_75451795}[]{#_Toc350155474}[]{#_Toc342653622}[]{#_Toc54583773}

**ISDN \-- ISDN配置命令 \-- isdn overlap-sending**

------------------------------------------------------------------------

[**[isdn overlap-sending]{lang="EN-US"}**]{#struct_0_19941_14702_1303465159}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口被叫号码的发送方式为重叠发送。]{style="font-family:宋体"}

[**[undo isdn overlap-sending]{lang="EN-US"}**]{#struct_0_19941_14702_x1421448600}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_39361418}

[**[isdn overlap-sending]{lang="EN-US"}**[ \[ *digits* \]]{lang="EN-US"}]{#struct_0_19941_14702_922390658}

[**[undo isdn overlap-sending]{lang="EN-US"}**]{#struct_0_19941_14702_1636329875}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132310265}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1944945080}[接口被叫号码的发送方式为整体发送。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_176271970}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1733942483}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_1420430032}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1119734947}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_2034379526}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_1727019062}

[*[digits]{lang="EN-US"}*]{#struct_0_19941_14702_x1094759080}[：重叠发送的时候每次最多能发送的号码位数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，缺省每次最多发送]{style="font-family:宋体"}[10]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132244729}

[[当]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1393006132}[接口采用"重叠发送"方式发送被叫号码时，被叫号码将会分几次发送，每次最多发送此命令设置的位数。当]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口采用"整体发送"方式发送被叫号码时，被叫号码将会一次发送完成。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_x1458683420}

[]{#struct_0_19941_14702_202779410}[]{#OLE_LINK43}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
10.0pt;font-family:Symbol"}[AT&T]{lang="EN-US"}]{#OLE_LINK42}[、]{lang="EN-US" style="font-family:宋体"}[NTT]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[NI2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[5ESS]{lang="EN-US"}[协议不支持重叠发送。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_372004052}[ISDN]{lang="EN-US"}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_96414555}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_853727020}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[采用重叠发送方式发送被叫号码，每次最多发送]{style="font-family:宋体"}[12]{lang="EN-US"}[位被叫号码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_1193619173}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn overlap-sending 12]{lang="EN-US"}
:::

::: {#-956626879 .myid}
[]{#_Toc404785172}[]{#struct_0_19941_14702_x1275314447}[]{#_Toc350155475}[]{#_Toc342653623}[]{#_Toc352075889}[]{#_Toc352767330}[]{#_Toc353262574}[]{#_Toc353435941}[]{#_Toc353443120}[]{#_Toc354507424}[]{#_Toc354507888}[]{#_Toc354507924}[]{#_Toc352075890}[]{#_Toc352767331}[]{#_Toc353262575}[]{#_Toc353435942}[]{#_Toc353443121}[]{#_Toc354507425}[]{#_Toc354507889}[]{#_Toc354507925}[]{#_Toc54583774}

**ISDN \-- ISDN配置命令 \-- isdn pri-slipwnd-size**

------------------------------------------------------------------------

[**[isdn pri-slipwnd-size]{lang="EN-US"}**]{#struct_0_19941_14702_x2132179193}[命令用来配置]{style="font-family:宋体"}[ISDN PRI]{lang="EN-US"}[接口的滑动窗口的大小。]{style="font-family:宋体"}

[**[undo isdn pri-slipwnd-size]{lang="EN-US"}**]{#struct_0_19941_14702_135886709}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x678366253}

[**[isdn pri-slipwnd-size]{lang="EN-US"}**[ *window-size*]{lang="EN-US"}]{#struct_0_19941_14702_x291389990}

[**[undo isdn pri-slipwnd-size]{lang="EN-US"}**]{#struct_0_19941_14702_1278544986}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1234893096}

[[ISDN PRI]{lang="EN-US"}]{#struct_0_19941_14702_x1025686498}[接口的滑动窗口大小为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1356711560}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1117079945}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132637945}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1447029981}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_1444165530}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1644042779}

[*[window-size]{lang="EN-US"}*]{#struct_0_19941_14702_x1154559693}[：滑动窗口大小，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x382016027}

[[Q.921]{lang="EN-US"}]{#struct_0_19941_14702_x1214960322}[缓冲区中的帧是按序号发送的，每个发送出去的帧都要被接收端确认。系统在发送时会连续发送几帧，但在发送时会判断未确认帧的个数，如果]{style="font-family:宋体"}[V]{lang="EN-US"}[（]{style="font-family:宋体"}[A]{lang="EN-US"}[）]{style="font-family:宋体"} [＋]{style="font-family:宋体"}[ K ]{lang="EN-US"}[＝]{style="font-family:宋体"}[ V]{lang="EN-US"}[（]{style="font-family:宋体"}[S]{lang="EN-US"}[），则不再进行发送。其中，]{style="font-family:
宋体"}[V]{lang="EN-US"}[（]{style="font-family:宋体"}[A]{lang="EN-US"}[）是已确认帧的序号，]{style="font-family:宋体"}[V]{lang="EN-US"}[（]{style="font-family:宋体"}[S]{lang="EN-US"}[）是下次要发送帧的序号，]{style="font-family:宋体"}[K]{lang="EN-US"}[是滑动窗口大小。]{style="font-family:宋体"}

[[滑动窗机制使得系统在发送帧时不必等待上一帧的确认，提高了发送效率。滑动窗口的大小决定了未确认帧的最大个数。]{style="font-family:宋体"}]{#struct_0_19941_14702_416253578}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_1380419051}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x2132572409}[配置接口]{style="font-family:宋体"}[CE1/PRI2/3/0]{lang="SV"}[的滑动窗口大小为]{style="font-family:宋体"}[10]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_709494144}

[\[Sysname\] controller e1 2/3/0]{lang="SV"}

[\[Sysname-E1 2/3/0\] using ce1]{lang="SV"}

[\[Sysname-E1 2/3/0\] pri-set]{lang="SV"}

[\[Sysname-E1 2/3/0\] quit]{lang="EN-US"}

[\[Sysname\] interface serial 2/3/0:15]{lang="EN-US"}

[\[Sysname-Serial2/3/0:15\] isdn pri-slipwnd-size 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1872284529}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn bri-slipwnd-size]{lang="EN-US"}**]{#struct_0_19941_14702_296093619}
:::

::: {#1282364247 .myid}
[]{#_Toc350155477}[]{#_Toc342653620}[]{#_Toc404785173}[]{#struct_0_19941_14702_430637467}[]{#_Toc353443123}[]{#_Toc350155476}[]{#_Toc266810206}

**ISDN \-- ISDN配置命令 \-- isdn progress-indicator**

------------------------------------------------------------------------

[**[isdn progress-indicator]{lang="EN-US"}**]{#struct_0_19941_14702_x2132506873}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[信令中的]{style="font-family:宋体"}[Progress indicator]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo isdn progress-indicator]{lang="EN-US"}**]{#struct_0_19941_14702_1403662825}[命令用来恢复缺省情况]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1828207216}

[**[isdn progress-indicator]{lang="EN-US"}**[ *indicator*]{lang="EN-US"}]{#struct_0_19941_14702_x2041987194}

[**[undo isdn progress-indicator]{lang="PT-BR"}**]{#struct_0_19941_14702_599329661}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132441337}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x726260666}[信令使用上层语音业务指示的]{style="font-family:宋体"}[Progress indicator]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_464912559}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x2051747671}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2131851513}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1093163508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1113589059}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2059422104}

[*[indicator]{lang="EN-US"}*]{#struct_0_19941_14702_x2131785977}[：]{style="font-family:宋体"}[Progress indicator]{lang="EN-US"}[值，取值范围如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-8]{lang="EN-US"}](?1282364247#_Ref350179519)[所示。]{style="font-family:宋体"}

[]{#struct_0_19941_14702_2114953077}[[表1-8 ]{lang="EN-US"}[Progress indicator]{lang="EN-US"}]{#_Ref350179519}[值]{style="font-family:黑体"}

[]{#table_struct_0_1854174094}[[取值]{style="font-family:黑体"}]{#struct_0_19941_14702_1472371075}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132375800}

[[1]{lang="EN-US"}]{#struct_0_19941_14702_x1869294273}

[[呼叫不是端到端的]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x2132310264}[呼叫；进一步的呼叫进展信息可能在带内提供]{style="font-family:宋体"}

[[2]{lang="EN-US"}]{#struct_0_19941_14702_783938275}

[[终点设备不是]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1619321967}[设备]{style="font-family:宋体"}

[[3]{lang="EN-US"}]{#struct_0_19941_14702_x2132244728}

[[源设备不是]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1335877223}[设备]{style="font-family:宋体"}

[[4]{lang="EN-US"}]{#struct_0_19941_14702_x2132179192}

[[呼叫已返回到]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1430197232}[网]{style="font-family:宋体"}

[[5]{lang="EN-US"}]{#struct_0_19941_14702_1661119770}

[[互通发生，导致通信服务改变（比如由]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x2132637944}[网进入]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[网）]{style="font-family:宋体"}

[[8]{lang="EN-US"}]{#struct_0_19941_14702_1281853374}

[[D]{lang="EN-US"}]{#struct_0_19941_14702_x2132572408}[信道上有除]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[信令之外的其他业务信息（例如]{style="font-family:宋体"}[X.25]{lang="EN-US"}[的虚呼叫信令）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x856589797}

[[Progress indicator]{lang="SV"}]{#struct_0_19941_14702_x1671945552}[值描述了在呼叫期间发生的事件。为了跟某些程控交换机互通]{style="font-family:宋体"}[，]{style="font-family:宋体"}[需要配置该值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2060647924}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x2132506872}[配置]{style="font-family:宋体"}[ISDN]{lang="SV"}[信令中的]{style="font-family:宋体"}[Progress indicator]{lang="SV"}[值为]{style="font-family:宋体"}[8]{lang="SV"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_x1325220530}

[\[Sysname\] interface bri 2/4/0]{lang="SV"}

[\[Sysname-Bri2/4/0\] isdn progress-indicator 8]{lang="SV"}

::: {#736071087 .myid}
[]{#_Toc404785174}[]{#struct_0_19941_14702_x1057700416}

**ISDN \-- ISDN配置命令 \-- isdn progress-to-alerting enable**

------------------------------------------------------------------------

[**[isdn progress-to-alerting enable]{lang="EN-US"}**]{#struct_0_19941_14702_x555198549}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口上把接收到的]{style="font-family:宋体"}[Progress]{lang="EN-US"}[消息转义成]{style="font-family:宋体"}[Alerting]{lang="EN-US"}[消息的功能。]{style="font-family:宋体"}

[**[undo isdn progress-to-alerting enable]{lang="EN-US"}**]{#struct_0_19941_14702_x221735207}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_601334698}

[**[isdn progress-to-alerting enable]{lang="EN-US"}**]{#struct_0_19941_14702_x906702789}

[**[undo isdn progress-to-alerting enable]{lang="EN-US"}**]{#struct_0_19941_14702_x2132441336}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_839823275}

[[Progress]{lang="EN-US"}]{#struct_0_19941_14702_85887295}[消息转义成]{style="font-family:宋体"}[Alerting]{lang="EN-US"}[消息的功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1650444226}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1172188132}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x97685048}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1757545227}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x6824600}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_1861510701}

[[在]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x2131851512}[进行语音业务呼叫流程中，按照标准协议由]{style="font-family:宋体"}[Alerting]{lang="EN-US"}[消息来表示振铃。但也有一些设备通常采用]{style="font-family:宋体"}[Progress]{lang="EN-US"}[消息来表示振铃指示，这种使用环境下需要把接收到]{style="font-family:宋体"}[Progress]{lang="EN-US"}[消息转义成]{style="font-family:宋体"}[Alerting]{lang="EN-US"}[消息处理。因此为灵活适用各种情况，可以通过命令来控制是否把]{style="font-family:宋体"}[Progress]{lang="EN-US"}[消息转义成]{style="font-family:宋体"}[Alerting]{lang="EN-US"}[消息，当跟采用]{style="font-family:宋体"}[Progress]{lang="EN-US"}[消息来表示振铃的设备对接时需要该转义操作，否则不需要进行该消息的转义操作。]{style="font-family:宋体"}

[[和友商设备互通时可能需要配置本命令。]{style="font-family:宋体"}]{#struct_0_19941_14702_x472920433}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x875101469}

[[\# PRI]{lang="SV"}]{#struct_0_19941_14702_x237204133}[接口]{style="font-family:宋体"}[Serial2/3/0:15]{lang="SV"}[上配置]{style="font-family:宋体"}[Progress]{lang="SV"}[消息转义成]{style="font-family:宋体"}[Alerting]{lang="SV"}[消息的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_1551568770}

[\[Sysname\] interface serial 2/3/0:15]{lang="SV"}

[\[Sysname-Serial2/3/0:15\] isdn progress-to-alerting enable]{lang="EN-US"}
:::

::: {#1896812969 .myid}
[]{#_Toc404785175}[]{#struct_0_19941_14702_x1869166270}[]{#_Toc350155478}[]{#_Toc322966327}

**ISDN \-- ISDN配置命令 \-- isdn protocol-mode**

------------------------------------------------------------------------

[**[isdn protocol-mode]{lang="EN-US"}**]{#struct_0_19941_14702_x1058533681}[命令用来配置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口所使用的协议模式。]{style="font-family:宋体"}

[**[undo isdn protocol-mode]{lang="EN-US"}**]{#struct_0_19941_14702_x1237271078}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2131785976}

[**[isdn protocol-mode]{lang="EN-US"}**[ { ]{lang="EN-US"}**[network]{lang="EN-US"}**[ ]{lang="EN-US"}[\| **user** }]{lang="EN-US"}]{#struct_0_19941_14702_x613930278}

[**[undo isdn protocol-mode]{lang="EN-US"}**]{#struct_0_19941_14702_1001509630}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1353630535}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_1467326437}[接口所使用的协议模式为用户侧模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1666314348}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1571894926}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x359011042}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x708608762}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_1765971581}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132375803}

[**[network]{lang="EN-US"}**]{#struct_0_19941_14702_x1466009746}[：]{style="font-family:宋体"}[网络侧模式。]{style="font-family:宋体"}

[**[user]{lang="EN-US"}**]{#struct_0_19941_14702_x559932909}[：]{style="font-family:宋体"}[用户侧模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x89650761}

[[协议模式分为两种：用户侧模式、网络侧模式。当两台]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x99378526}[设备互通时，必须一端工作在用户侧模式，另一端工作在网络侧模式。]{style="font-family:宋体"}

[[当语音]{style="font-family:宋体"}[BSV]{lang="EN-US"}]{#struct_0_19941_14702_x409959401}[板卡上的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口和]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[电话直接相连时，]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口需要配置为网络侧模式，在其它场景下，设备上的]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口通常都需要配置为用户侧模式。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_x613348550}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[运行数据业务的]{style="font-family:宋体"}]{#struct_0_19941_14702_172980014}[BRI]{lang="EN-US"}[接口不支持网络侧模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANSI]{lang="EN-US"}]{#struct_0_19941_14702_x1622134053}[、]{lang="EN-US" style="font-family:宋体"}[AT&T]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ETSI]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[NI]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[NTT]{lang="EN-US"}[协议不支持网络侧模式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x2132310267}[ISDN]{lang="EN-US"}[接口上存在呼叫时，]{style="font-family:宋体"}[不能配置]{style="font-family:宋体"}[本]{style="font-family:宋体"}[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x782145666}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_2007468907}[配置]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[接口的协议模式为网络侧模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_575651013}

[\[Sysname\] interface bri 2/4/0]{lang="SV"}

[\[Sysname-Bri2/4/0\] isdn protocol-mode network]{lang="SV"}
:::

::: {#63758688 .myid}
[]{#_Toc404785176}[]{#struct_0_19941_14702_x1602415502}[]{#_Toc350155479}[]{#_Toc342653625}[]{#_Toc352075895}[]{#_Toc352767336}[]{#_Toc353262580}[]{#_Toc353435947}[]{#_Toc353443126}[]{#_Toc354507429}[]{#_Toc354507893}[]{#_Toc354507929}[]{#_Toc352075896}[]{#_Toc352767337}[]{#_Toc353262581}[]{#_Toc353435948}[]{#_Toc353443127}[]{#_Toc354507430}[]{#_Toc354507894}[]{#_Toc354507930}

**ISDN \-- ISDN配置命令 \-- isdn protocol-type**

------------------------------------------------------------------------

[**[isdn protocol-type]{lang="EN-US"}**]{#struct_0_19941_14702_1703141887}[命令用来设置]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[接口所使用的]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **isdn protocol-type**]{lang="EN-US"}]{#struct_0_19941_14702_1059690589}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x742775593}

[**[isdn protocol-type ]{lang="EN-US"}***[protocol]{lang="EN-US"}*]{#struct_0_19941_14702_479769510}

[**[undo isdn protocol-type]{lang="EN-US"}**]{#struct_0_19941_14702_x2132244731}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_1749170956}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x389332039}[的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[和]{style="font-family:宋体"}[PRI]{lang="EN-US"}[接口都是使用]{style="font-family:宋体"}[DSS1]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1626317994}

[[ISDN]{lang="EN-US"}]{#struct_0_19941_14702_x1800198323}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1241954016}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_937087583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_1920381289}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_1821288598}

[*[protocol]{lang="EN-US"}*]{#struct_0_19941_14702_x2132179195}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[协议类型，可以取的值包括]{style="font-family:宋体"}**[5ess]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ansi]{lang="EN-US"}**[、]{style="font-family:宋体"}**[at&t]{lang="EN-US"}**[、]{style="font-family:宋体"}**[dss1]{lang="EN-US"}**[、]{style="font-family:宋体"}**[etsi]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ni]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ni2]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ntt]{lang="EN-US"}**[、]{style="font-family:宋体"}**[qsig]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1026912705}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANSI]{lang="EN-US"}]{#struct_0_19941_14702_x1608618048}[协议可以在]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AT&T]{lang="EN-US"}]{#struct_0_19941_14702_858150172}[协议可以在]{lang="EN-US" style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5ESS]{lang="EN-US"}]{#struct_0_19941_14702_x1992686254}[协议可以在]{lang="EN-US" style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DSS1]{lang="EN-US"}]{#struct_0_19941_14702_537006830}[协议可以在]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[以及]{lang="EN-US" style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ETSI]{lang="EN-US"}]{#struct_0_19941_14702_1160281899}[协议可以在]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[以及]{lang="EN-US" style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NI]{lang="EN-US"}]{#struct_0_19941_14702_x419379040}[（]{lang="EN-US" style="font-family:
宋体"}[National ISDN]{lang="EN-US"}[）协议可以在]{lang="EN-US" style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NI2]{lang="EN-US"}]{#struct_0_19941_14702_288096893}[协议可以在]{lang="EN-US" style="font-family:
宋体"}[CT1/PRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[QSIG]{lang="EN-US"}]{#struct_0_19941_14702_x1347500851}[协议可以在]{lang="EN-US" style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[以及]{lang="EN-US" style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NTT]{lang="EN-US"}]{#struct_0_19941_14702_x2132637947}[协议可以在]{lang="EN-US" style="font-family:
宋体"}[BRI]{lang="EN-US"}[和]{lang="EN-US" style="font-family:
宋体"}[CT1/PRI]{lang="EN-US"}[接口上配置]{lang="EN-US" style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[工作在网络侧模式时，不可以配置]{style="font-family:宋体"}]{#struct_0_19941_14702_1685137901}[ANSI]{lang="EN-US"}[、]{style="font-family:宋体"}[AT&T]{lang="EN-US"}[、]{style="font-family:宋体"}[ETSI]{lang="EN-US"}[、]{style="font-family:宋体"}[NI]{lang="EN-US"}[、]{style="font-family:宋体"}[NTT]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x1368795869}[ISDN]{lang="EN-US"}[接口上存在呼叫时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_989007803}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x850669218}[设置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[使用]{style="font-family:宋体"}[ISDN ETSI]{lang="SV"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_x2077089017}

[\[Sysname\] interface bri 2/4/0]{lang="SV"}

[\[Sysname-Bri2/4/0\] isdn protocol-type etsi]{lang="NO-BOK"}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_431688738}[设置接口]{style="font-family:宋体"}[Serial2/3/0:23]{lang="SV"}[使用]{style="font-family:宋体"}[ISDN 5ESS]{lang="SV"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_x1951177907}

[\[Sysname\] interface serial 2/3/0:23]{lang="SV"}

[\[Sysname-Serial2/3/0:23\] isdn protocol-type 5ess]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132572411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn protocol-mode]{lang="EN-US"}**]{#struct_0_19941_14702_353329320}
:::

::: {#-1194781817 .myid}
[]{#_Toc350155480}[]{#_Toc54583777}[]{#_Toc404785177}[]{#struct_0_19941_14702_x938311439}[]{#_Toc353443129}[]{#_Toc352068920}

**ISDN \-- ISDN配置命令 \-- isdn q921-permanent**

------------------------------------------------------------------------

[**[isdn q921-permanent]{lang="EN-US"}**]{#struct_0_19941_14702_x1327796838}[命令用来使能]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[常建链功能。]{style="font-family:宋体"}

[**[undo isdn q921-permanent]{lang="EN-US"}**]{#struct_0_19941_14702_982478804}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132506875}

[**[isdn q921-permanent]{lang="EN-US"}**]{#struct_0_19941_14702_240863411}

[**[undo isdn q921-permanent]{lang="EN-US"}**]{#struct_0_19941_14702_934472216}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_241334349}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x2132441339}[接口的]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[常建链功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_2049676856}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x899122182}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1807008668}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x2131851515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x2039004374}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_1469435019}

[[当在]{style="font-family:宋体"}[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x2131785979}[接口下配置了该命令，该]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口会自动建立链路层连接并一直维持，不论其是否承载网络层呼叫。若]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口配置了]{style="font-family:宋体"}**[isdn two-tei]{lang="EN-US"}**[命令，]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[常建链功能会自动建立两条链路层连接并一直维持。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[BRI]{lang="EN-US"}]{#struct_0_19941_14702_952153663}[接口工作在网络侧模式时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2085132241}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_379269586}[使能接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[常建链功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x2132375802}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn q921-permanent]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1262873609}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn protocol-mode]{lang="EN-US"}**]{#struct_0_19941_14702_x2059816811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn two-tei]{lang="EN-US"}**]{#struct_0_19941_14702_x2124886597}
:::

::: {#-1904257423 .myid}
[]{#_Toc404785178}[]{#struct_0_19941_14702_x1623941118}

**ISDN \-- ISDN配置命令 \-- isdn spid auto-trigger**

------------------------------------------------------------------------

[**[isdn spid auto-trigger]{lang="EN-US"}**]{#struct_0_19941_14702_x2132310266}[命令用来对采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口触发一次]{style="font-family:宋体"}[SPID]{lang="EN-US"}[的协商请求。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1946737689}

[**[isdn spid auto-trigger]{lang="EN-US"}**]{#struct_0_19941_14702_373226598}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_139642199}

[[没有呼叫触发时，]{style="font-family:宋体"}[BRI]{lang="EN-US"}]{#struct_0_19941_14702_1836508053}[接口不会主动发起]{style="font-family:宋体"}[SPID]{lang="EN-US"}[的协商请求。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_2131016013}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x118677659}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x773175427}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_669278158}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x2132244730}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x979712399}

[[对于采用]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_19941_14702_1591602145}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口，通常需要在协商或者初始化]{style="font-family:宋体"}[SPID]{lang="EN-US"}[之后才能发起呼叫。]{style="font-family:宋体"}[SPID]{lang="EN-US"}[信息的获取可以通过静态配置，也可以通过动态协商。当用户采用动态协商而协商失败，或者为了测试需要的时候，可以采用此命令手动重新触发一次]{style="font-family:宋体"}[SPID]{lang="EN-US"}[的协商请求。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_99839792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在采用]{style="font-family:宋体"}]{#struct_0_19941_14702_362100841}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上可以使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[未配置为动态协商]{style="font-family:宋体"}]{#struct_0_19941_14702_x883568586}[SPID]{lang="EN-US"}[时，]{style="font-family:宋体"}[不能配置本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[配置的接口存在呼叫时，不能配置]{style="font-family:宋体"}]{#struct_0_19941_14702_1614782459}[本]{style="font-family:宋体"}[命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的接口正在进行]{style="font-family:宋体"}]{#struct_0_19941_14702_443554696}[SPID]{lang="EN-US"}[协商时，不]{style="font-family:宋体"}[能]{style="font-family:宋体"}[配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_779949835}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x2132179194}[设置在接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上手动触发一次]{style="font-family:宋体"}[SPID]{lang="EN-US"}[的协商请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_1701970650}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn spid auto-trigger]{lang="EN-US"}
:::

::: {#1139818536 .myid}
[]{#_Toc404785179}[]{#struct_0_19941_14702_x799006011}[]{#_Toc350155481}[]{#_Toc54583778}[]{#_Toc95359215}[]{#_Toc85604325}[]{#_Toc81386704}[]{#_Toc74661827}[]{#_Toc72589790}[]{#_Toc72589517}[]{#_Toc72589002}[]{#_Toc65921172}[]{#_Toc65919120}[]{#_Toc65919095}[]{#_Toc65910729}[]{#_Toc65909974}[]{#_Toc60125184}

**ISDN \-- ISDN配置命令 \-- isdn spid nit**

------------------------------------------------------------------------

[**[isdn spid nit]{lang="EN-US"}**]{#struct_0_19941_14702_1728056951}[命令用来对采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口，将其]{style="font-family:宋体"}[SPID]{lang="EN-US"}[处理设置为]{style="font-family:宋体"}[NIT]{lang="EN-US"}[（]{style="font-family:宋体"}[Not Initial Terminal]{lang="EN-US"}[，非初始化终端）模式。]{style="font-family:宋体"}

[**[undo isdn spid nit]{lang="EN-US"}**]{#struct_0_19941_14702_x1667085650}[命令用来取消]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的]{style="font-family:宋体"}[NIT]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1368129433}

[**[isdn spid nit]{lang="EN-US"}**]{#struct_0_19941_14702_1260069743}

[**[undo isdn spid nit]{lang="EN-US"}**]{#struct_0_19941_14702_2024612755}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x705621796}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x2132637946}[接口不采用]{style="font-family:宋体"}[NIT]{lang="EN-US"}[模式，使用动态协商]{style="font-family:宋体"}[SPID]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_119053960}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x1130152297}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x798938108}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1753448881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x574043796}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_1115518510}

[[对于采用]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_19941_14702_644196699}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口，通常需要在协商或者初始化]{style="font-family:宋体"}[SPID]{lang="EN-US"}[之后才能发起呼叫。如果当设备与采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议但不支持]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商的程控交换机互通时，就采用此命令将其]{style="font-family:宋体"}[SPID]{lang="EN-US"}[处理设置为]{style="font-family:宋体"}[NIT]{lang="EN-US"}[模式，从而使设备和程控交换机忽略]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商和初始化的过程。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_623143757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在采用]{style="font-family:宋体"}]{#struct_0_19941_14702_x2132572410}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上可以使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x1212754621}[ISDN]{lang="EN-US"}[接口上]{style="font-family:宋体"}[存在呼叫时，不能配置]{style="font-family:宋体"}[本]{style="font-family:宋体"}[命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_1226649611}[ISDN]{lang="EN-US"}[接口正在进行]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商时，不]{style="font-family:宋体"}[能]{style="font-family:宋体"}[配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x238727920}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_1715504359}[设置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[忽略]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商和初始化的过程，即采用]{style="font-family:宋体"}[NIT]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_1809962728}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn spid nit]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1759757941}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display isdn spid]{lang="EN-US"}**]{#struct_0_19941_14702_x400398267}
:::

::: {#2146570940 .myid}
[]{#_Toc404785180}[]{#struct_0_19941_14702_x875915809}[]{#_Toc350155482}[]{#_Toc96758223}

**ISDN \-- ISDN配置命令 \-- isdn spid resend**

------------------------------------------------------------------------

[**[isdn spid resend]{lang="EN-US"}**]{#struct_0_19941_14702_x2132506874}[命令用来对采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口，设置其协商或者初始化的]{style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息的重发次数。]{style="font-family:宋体"}

[**[undo isdn spid resend]{lang="EN-US"}**]{#struct_0_19941_14702_1806947352}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1230602087}

[**[isdn spid resend]{lang="EN-US"}**[ *times*]{lang="EN-US"}]{#struct_0_19941_14702_1877048360}

[**[undo isdn spid resend]{lang="EN-US"}**]{#struct_0_19941_14702_x1089433547}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x991606497}

[[INFORMATION]{lang="EN-US"}]{#struct_0_19941_14702_485756836}[消息重发次数为]{style="font-family:宋体"}[1]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x97929969}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x1066538911}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2132441338}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x679206499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_97959287}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1632459511}

[*[times]{lang="EN-US"}*]{#struct_0_19941_14702_x1862665744}[：]{style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息的重发次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_19941_14702_1402921007}[]{#OLE_LINK2}[[使用指导]{style="font-family:黑体"}]{#OLE_LINK1}[】]{style="font-family:黑体"}

[[对于采用]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_19941_14702_x2133747874}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口，通常需要在协商或者初始化]{style="font-family:宋体"}[SPID]{lang="EN-US"}[之后才能发起呼叫。当设备采用]{style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息发起]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商或者初始化请求之后，将启用]{style="font-family:宋体"}[TSPID]{lang="EN-US"}[定时器，若协商或初始化请求无响应，当]{style="font-family:宋体"}[TSPID]{lang="EN-US"}[定时器超时后设备将重发]{style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息。可以采用此命令修改]{style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[的重发次数。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_1737529645}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在采用]{style="font-family:宋体"}]{#struct_0_19941_14702_x2098117456}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上可以使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x2131851514}[ISDN]{lang="EN-US"}[ BRI]{lang="EN-US"}[接口正在进行]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_689878981}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x620683091}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[的]{style="font-family:宋体"}[INFORMATION]{lang="SV"}[消息的]{style="font-family:宋体"}[重发次数为]{style="font-family:宋体"}[5]{lang="SV"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1682940045}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn spid resend 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x611671304}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[isdn spid timer]{lang="SV"}**]{#struct_0_19941_14702_734748227}
:::

::: {#-1072363598 .myid}
[]{#_Toc404785181}[]{#struct_0_19941_14702_x1440858065}

**ISDN \-- ISDN配置命令 \-- isdn spid service**

------------------------------------------------------------------------

[**[isdn spid service]{lang="EN-US"}**]{#struct_0_19941_14702_x905352167}[命令用来配置]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商时设备可接受的业务类型。]{style="font-family:宋体"}

[**[undo isdn spid service]{lang="EN-US"}**]{#struct_0_19941_14702_1848575953}[命令用来配置设备可接受任意业务类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2131785978}

[**[isdn spid service]{lang="EN-US"}**[ \[ **audio** \| **data** \| **speech** \]]{lang="EN-US"}]{#struct_0_19941_14702_x1776729692}

[**[undo isdn spid service]{lang="EN-US"}**]{#struct_0_19941_14702_x1301123345}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x421720995}

[[设备可接受程控交换机发送的支持语音（]{style="font-family:宋体"}[speech]{lang="EN-US"}]{#struct_0_19941_14702_93061508}[）和数据（]{style="font-family:宋体"}[data]{lang="EN-US"}[）业务的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1684400874}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x1242456791}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_817246218}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x831441062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x210061498}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_1413373205}

[**[audio]{lang="EN-US"}**]{#struct_0_19941_14702_1548396407}[：音频业务。]{style="font-family:宋体"}

[**[data]{lang="EN-US"}**]{#struct_0_19941_14702_x183793578}[：数据业务。]{style="font-family:宋体"}

[**[speech]{lang="EN-US"}**]{#struct_0_19941_14702_x1475227535}[：语音业务。]{style="font-family:宋体"}

[[三种业务类型可以选择其一，不选择表示所有业务都接受。]{style="font-family:宋体"}]{#struct_0_19941_14702_x574199919}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_1948838023}

[[动态协商]{style="font-family:宋体"}[SPID]{lang="EN-US"}]{#struct_0_19941_14702_939386792}[时，如果程控交换机提供了多个]{style="font-family:宋体"}[SPID]{lang="EN-US"}[给设备，则设备根据每个]{style="font-family:宋体"}[SPID]{lang="EN-US"}[提供的业务类型是否满足当前配置的可接受业务类型来决定选择哪一个]{style="font-family:宋体"}[SPID]{lang="EN-US"}[。缺省情况下，设备优先接受程控交换机发送的同时支持语音（]{style="font-family:宋体"}[speech]{lang="EN-US"}[）和数据（]{style="font-family:宋体"}[data]{lang="EN-US"}[）业务的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[。如果仅配置了]{style="font-family:宋体"}**[isdn spid service data]{lang="EN-US"}**[，设备优先接受程控交换机发送的支持数据业务的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[多次配置本命令，其结果是取合集，例如先后配置]{style="font-family:宋体"}**[isdn spid service]{lang="EN-US"}**[ **audio**]{lang="EN-US"}]{#struct_0_19941_14702_x1420891174}[、]{style="font-family:宋体"}**[isdn spid service]{lang="EN-US"}**[ **data**]{lang="EN-US"}[两条命令，其结果是优先接受同时支持]{style="font-family:宋体"}[音频和数据业务的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_x209995962}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在采用]{style="font-family:宋体"}]{#struct_0_19941_14702_1427978440}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上可以使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_67950485}[ISDN BRI]{lang="EN-US"}[接口正在进行]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2014928077}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x443284680}[配置设备可接受程控交换机发送的支持音频业务的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_1984314936}

[\[Sysname\] interface bri 2/4/0]{lang="SV"}

[\[Sysname-Bri2/4/0\] isdn service audio]{lang="SV"}
:::

::: {#-864206396 .myid}
[]{#_Toc404785182}[]{#struct_0_19941_14702_1672366596}[]{#_Toc350155484}[]{#_Toc54583779}

**ISDN \-- ISDN配置命令 \-- isdn spid timer**

------------------------------------------------------------------------

[**[isdn spid timer]{lang="EN-US"}**]{#struct_0_19941_14702_531624130}[命令用来配置采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的]{style="font-family:宋体"}[TSPID]{lang="EN-US"}[定时器的时长。]{style="font-family:宋体"}

[**[undo isdn spid timer]{lang="EN-US"}**]{#struct_0_19941_14702_1206943688}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x209930426}

[**[isdn spid timer]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_19941_14702_734720453}

[**[undo isdn spid timer]{lang="EN-US"}**]{#struct_0_19941_14702_x1012377693}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_2143566445}

[[TSPID]{lang="EN-US"}]{#struct_0_19941_14702_1299151834}[定时器的时长为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x150019086}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_1900421594}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x247818232}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_306230955}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1476126039}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x209864890}

[*[seconds]{lang="EN-US"}*]{#struct_0_19941_14702_1052886105}[：]{style="font-family:宋体"}[TSPID]{lang="EN-US"}[定时器的时长，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x705206169}

[[对于采用]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_19941_14702_x1039148561}[的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口，通常需要在协商或者初始化]{style="font-family:宋体"}[SPID]{lang="EN-US"}[之后才能发起呼叫。]{style="font-family:宋体"}[SPID]{lang="EN-US"}[信息的获取可以通过静态配置，也可以通过动态协商。当设备采用]{style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息发起协商或者初始化请求之后，将启用]{style="font-family:宋体"}[TSPID]{lang="EN-US"}[定时器，若协商或初始化请求无响应，当]{style="font-family:宋体"}[TSPID]{lang="EN-US"}[定时器超时后设备将重发]{style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息。用户可以采用此命令修改]{style="font-family:宋体"}[TSPID]{lang="EN-US"}[定时器的时长。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_2034846278}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在采用]{style="font-family:宋体"}]{#struct_0_19941_14702_x541516189}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上可以使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_1935627668}[ISDN]{lang="EN-US"}[ BRI]{lang="EN-US"}[接口正在进行]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商时，不能配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x658393342}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x785673102}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[TSPID]{lang="EN-US"}[定时器的时长为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_19941_14702_x210323642}

[\[Sysname\] interface bri 2/4/0]{lang="DA"}

[\[Sysname-Bri2/4/0\] isdn spid timer 50]{lang="DA"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x123767697}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn spid resend]{lang="EN-US"}**]{#struct_0_19941_14702_1958776041}
:::

::: {#-1078266173 .myid}
[]{#_Toc404785183}[]{#struct_0_19941_14702_x1607702254}[]{#_Toc350155485}[]{#_Toc54583781}

**ISDN \-- ISDN配置命令 \-- isdn spid1**

------------------------------------------------------------------------

[**[isdn spid1]{lang="EN-US"}**]{#struct_0_19941_14702_21011782}[命令用来配置采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[B1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo isdn spid1]{lang="EN-US"}**]{#struct_0_19941_14702_568113315}[命令用来删除采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[B1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1595339182}

[**[isdn spid1 ]{lang="EN-US"}***[spid ]{lang="EN-US"}*[\[ *ldn* \]]{lang="EN-US"}]{#struct_0_19941_14702_x1288880300}

[**[undo isdn spid1]{lang="EN-US"}**]{#struct_0_19941_14702_x210258106}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x995395885}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x1290108003}[接口]{style="font-family:宋体"}[B1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[和]{style="font-family:宋体"}[LDN]{lang="EN-US"}[值均为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_1617710740}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x1570044737}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_996075557}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_1219082369}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x334750731}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x912530759}

[*[spid]{lang="EN-US"}*]{#struct_0_19941_14702_x1019882877}[：]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[Service Profile Identification]{lang="EN-US"}[，业务轮廓标识），为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[个数字的数字串。]{style="font-family:宋体"}

[*[ldn]{lang="EN-US"}*]{#struct_0_19941_14702_x210192570}[：]{style="font-family:宋体"}[LDN]{lang="EN-US"}[（]{style="font-family:宋体"}[Local Dialing Number]{lang="EN-US"}[，本地拨号号码），为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个数字的数字串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_1007610079}

[[对于采用]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_19941_14702_1039410081}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口，通常需要在协商或者初始化]{style="font-family:宋体"}[SPID]{lang="EN-US"}[之后才能发起呼叫。]{style="font-family:宋体"}[SPID]{lang="EN-US"}[信息的获取可以通过静态配置，也可以通过动态协商。通过哪种方式获取，由程控交换机决定。]{style="font-family:宋体"}

[[缺省情况下，设备采用动态协商方式获取]{style="font-family:宋体"}[SPID]{lang="EN-US"}]{#struct_0_19941_14702_x1635314529}[。]{style="font-family:宋体"}

[[静态配置]{style="font-family:宋体"}[SPID]{lang="EN-US"}]{#struct_0_19941_14702_x1963472615}[时，用户可以通过]{style="font-family:宋体"}**[isdn spid1]{lang="EN-US"}**[命令配置]{style="font-family:宋体"}[B1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值，通过]{style="font-family:宋体"}**[isdn spid2]{lang="EN-US"}**[命令配置]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值。配置的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值要与程控交换机上的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值相同。程控交换机的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值是由运营商在规划网络时配置的。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_1901342456}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置了]{lang="EN-US" style="font-family:宋体"}[LDN]{lang="EN-US"}]{#struct_0_19941_14702_x1410188588}[后，]{lang="EN-US" style="font-family:宋体"}**[isdn calling]{lang="EN-US"}**[命令的配置将失效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在采用]{style="font-family:宋体"}]{#struct_0_19941_14702_x1461167642}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上可以使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x1593775771}[ISDN]{lang="EN-US"}[ BRI]{lang="EN-US"}[接口上]{style="font-family:宋体"}[存在呼叫时，不能配置]{style="font-family:宋体"}[本]{style="font-family:宋体"}[命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x210127034}[ISDN]{lang="EN-US"}[ BRI]{lang="EN-US"}[接口正在进行]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商时，不]{style="font-family:宋体"}[能]{style="font-family:宋体"}[配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x945731916}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x637499891}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[的]{style="font-family:宋体"}[B1]{lang="SV"}[通道的]{style="font-family:
宋体"}[SPID]{lang="SV"}[为]{style="font-family:宋体"}[012345]{lang="SV"}[，]{style="font-family:宋体"}[LDN]{lang="SV"}[为]{style="font-family:宋体"}[54321]{lang="SV"}[（实际应用中，要根据程控交换机的要求来配置这两个值）]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_774836952}

[\[Sysname\] interface bri 2/4/0]{lang="SV"}

[\[Sysname-Bri2/4/0\] isdn spid1 012345 54321]{lang="SV"}

[[【相关命令】]{style="font-family:
黑体"}]{#struct_0_19941_14702_1327971}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[isdn calling]{lang="EN-US"}**]{#struct_0_19941_14702_1839110327}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}**[isdn spid2]{lang="SV"}**]{#struct_0_19941_14702_1207047418}
:::

::: {#-1078462781 .myid}
[]{#_Toc404785184}[]{#struct_0_19941_14702_x276921926}[]{#_Toc350155486}

**ISDN \-- ISDN配置命令 \-- isdn spid2**

------------------------------------------------------------------------

[**[isdn spid2]{lang="EN-US"}**]{#struct_0_19941_14702_x1342992825}[命令用来配置采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo isdn spid2]{lang="EN-US"}**]{#struct_0_19941_14702_x209537210}[命令用来删除采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1478577941}

[**[isdn spid2 ]{lang="EN-US"}***[spid ]{lang="EN-US"}*[\[ *ldn* \]]{lang="EN-US"}]{#struct_0_19941_14702_1362393959}

[**[undo isdn spid2]{lang="EN-US"}**]{#struct_0_19941_14702_x1093291587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x318716477}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x2096251915}[接口]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[和]{style="font-family:宋体"}[LDN]{lang="EN-US"}[值均为空。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_1832465546}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_2042875276}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x72099709}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x209471674}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x457284094}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19941_14702_x853729422}

[*[spid]{lang="EN-US"}*]{#struct_0_19941_14702_128918251}[：]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[Service Profile Identification]{lang="EN-US"}[，业务轮廓标识），为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[个数字的数字串。]{style="font-family:宋体"}

[*[ldn]{lang="EN-US"}*]{#struct_0_19941_14702_x235106786}[：]{style="font-family:宋体"}[LDN]{lang="EN-US"}[（]{style="font-family:宋体"}[[Local Dialing Number]{lang="EN-US"}]{#OLE_LINK51}[，本地拨号号码]{style="font-family:宋体"}[），为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个数字的数字串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x701040430}

[[对于采用]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_19941_14702_x1172770688}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口，通常需要在协商或者初始化]{style="font-family:宋体"}[SPID]{lang="EN-US"}[之后才能发起呼叫。]{style="font-family:宋体"}[SPID]{lang="EN-US"}[信息的获取可以通过静态配置，也可以通过动态协商。通过哪种方式获取，由程控交换机决定。]{style="font-family:宋体"}

[[缺省情况下，设备采用动态协商方式获取]{style="font-family:宋体"}[SPID]{lang="EN-US"}]{#struct_0_19941_14702_1319150852}[。]{style="font-family:宋体"}

[[静态配置]{style="font-family:宋体"}[SPID]{lang="EN-US"}]{#struct_0_19941_14702_x172030709}[时，用户可以通过]{style="font-family:宋体"}**[isdn spid1]{lang="EN-US"}**[命令配置]{style="font-family:宋体"}[B1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值，通过]{style="font-family:宋体"}**[isdn spid2]{lang="EN-US"}**[命令配置]{style="font-family:宋体"}[B2]{lang="EN-US"}[通道的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值。配置的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值要与程控交换机上的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值相同。程控交换机的]{style="font-family:宋体"}[SPID]{lang="EN-US"}[（]{style="font-family:宋体"}[LDN]{lang="EN-US"}[）值是由运营商在规划网络时配置的。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_1923219867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置了]{lang="EN-US" style="font-family:宋体"}[LDN]{lang="EN-US"}]{#struct_0_19941_14702_x210061497}[后，]{lang="EN-US" style="font-family:宋体"}**[isdn calling]{lang="EN-US"}**[命令的配置将失效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只在采用]{style="font-family:宋体"}]{#struct_0_19941_14702_1412390165}[NI]{lang="EN-US"}[协议的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口上可以使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x1234500282}[ISDN]{lang="EN-US"}[ BRI]{lang="EN-US"}[接口上]{style="font-family:宋体"}[存在呼叫时，不能配置]{style="font-family:宋体"}[本]{style="font-family:宋体"}[命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x1935817707}[ISDN]{lang="EN-US"}[ BRI]{lang="EN-US"}[接口正在进行]{style="font-family:宋体"}[SPID]{lang="EN-US"}[协商时，不]{style="font-family:宋体"}[能]{style="font-family:宋体"}[配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_257464622}

[[\# ]{lang="SV"}]{#struct_0_19941_14702_x1231559573}[配置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="SV"}[的]{style="font-family:宋体"}[B2]{lang="SV"}[通道的]{style="font-family:
宋体"}[SPID]{lang="SV"}[为]{style="font-family:宋体"}[012345]{lang="SV"}[，]{style="font-family:宋体"}[LDN]{lang="SV"}[为]{style="font-family:宋体"}[54321]{lang="SV"}[（实际应用中，要根据程控交换机的要求来配置这两个值）]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_19941_14702_x993650333}

[\[Sysname\] interface bri 2/4/0]{lang="SV"}

[\[Sysname-Bri2/4/0\] isdn spid2 012345 54321]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_1924736612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn calling]{lang="EN-US"}**]{#struct_0_19941_14702_x209995961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn spid1]{lang="SV"}**]{#struct_0_19941_14702_1428175048}
:::

::: {#2100051765 .myid}
[]{#_Toc404785185}[]{#struct_0_19941_14702_693229044}[]{#_Toc353443137}[]{#_Toc352068928}

**ISDN \-- ISDN配置命令 \-- isdn two-tei**

------------------------------------------------------------------------

[**[isdn two-tei]{lang="EN-US"}**]{#struct_0_19941_14702_283244376}[命令用来配置]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的每一个]{style="font-family:宋体"}[B]{lang="EN-US"}[通道呼叫之前向交换机申请一个新的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo isdn two-tei]{lang="EN-US"}**]{#struct_0_19941_14702_1624145335}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x209930425}

[**[isdn two-tei]{lang="EN-US"}**]{#struct_0_19941_14702_734654917}

[**[undo isdn two-tei]{lang="EN-US"}**]{#struct_0_19941_14702_475022119}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x841835589}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x209864889}[接口所有]{style="font-family:宋体"}[B]{lang="EN-US"}[通道的呼叫都使用同一个]{style="font-family:宋体"}[TEI]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_1053344858}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_1677546181}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x210323641}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x123702161}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1161565521}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x526141794}

[[一个]{style="font-family:宋体"}]{#struct_0_19941_14702_x210258105}[TEI]{lang="SV"}[（]{style="font-family:宋体"}[Terminal Endpoint Identifier]{lang="SV"}[，]{style="font-family:宋体"}[终端设备标识符]{style="font-family:宋体"}[）]{style="font-family:宋体"}[标识一个终端]{style="font-family:宋体"}[（]{style="font-family:宋体"}[比如]{style="font-family:宋体"}[ISDN]{lang="SV"}[电话]{style="font-family:宋体"}[），]{style="font-family:宋体"}[一个用户侧设备就是一个终端。]{style="font-family:宋体"}[TEI]{lang="EN-US"}[由网络侧设备分配。]{style="font-family:宋体"}

[[在设备的]{style="font-family:宋体"}[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x995199277}[接口与部分程控交换机（如北美的采用]{style="font-family:宋体"}[NI]{lang="EN-US"}[协议的程控交换机]{style="font-family:宋体"}[DMS100]{lang="EN-US"}[）进行互通的时候，程控交换机要求不同的]{style="font-family:宋体"}[B]{lang="EN-US"}[通道采用不同的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[值呼叫，否则]{style="font-family:宋体"}[MP]{lang="EN-US"}[呼叫无法成功（现象为只能呼起一个]{style="font-family:宋体"}[B]{lang="EN-US"}[通道），这时就需要使用本命令使每一个]{style="font-family:宋体"}[B]{lang="EN-US"}[通道呼叫之前向程控交换机申请一个新的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_x2060121046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_2139232542}[ISDN BRI]{lang="EN-US"}[接口上存在呼叫时，不]{style="font-family:宋体"}[能]{style="font-family:
宋体"}[配置本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_x210192569}[ISDN BRI]{lang="EN-US"}[接口工作在点到点模式下时，不]{style="font-family:宋体"}[能]{style="font-family:宋体"}[配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_1008199902}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_x800047810}[配置每一个]{style="font-family:宋体"}[ISDN B]{lang="EN-US"}[通道呼叫之前向交换机申请一个新的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x1989194162}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Router-Bri2/4/0\] isdn two-tei]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x210127033}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[i]{lang="EN-US"}[sdn link-mode p2p]{lang="EN-US"}**]{#struct_0_19941_14702_x946190668}
:::

::: {#-2117461249 .myid}
[]{#_Toc404785186}[]{#struct_0_19941_14702_1144721605}[]{#_Toc353443138}[]{#_Toc352068929}

**ISDN \-- ISDN配置命令 \-- permanent-active**

------------------------------------------------------------------------

[**[permanent-active]{lang="EN-US"}**]{#struct_0_19941_14702_x209537209}[命令用来使能]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的物理层常激活功能。]{style="font-family:宋体"}

[**[undo permanent-active]{lang="EN-US"}**]{#struct_0_19941_14702_1478119188}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_278469485}

[**[permanent-active]{lang="EN-US"}**]{#struct_0_19941_14702_x1580384863}

[**[undo permanent-active]{lang="EN-US"}**]{#struct_0_19941_14702_x209471673}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x457349630}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x2015288728}[接口的物理层常激活功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_x621725321}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x210061500}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_x543466210}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x116370004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_1341116988}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x209995964}

[[当工作在网络侧模式下的]{style="font-family:宋体"}[BRI]{lang="EN-US"}]{#struct_0_19941_14702_1428371656}[接口配置了该命令，]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[协议不会再给物理层发送去激活请求，如果]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口已经处于激活状态并且物理连接没有异常，则激活状态会一直维持下去。]{style="font-family:宋体"}

[[使用本命令时注意和]{style="font-family:宋体"}**[isdn q921-permanent]{lang="EN-US"}**]{#struct_0_19941_14702_1872472219}[命令的区别。]{style="font-family:宋体"}**[isdn q921-permanent]{lang="EN-US"}**[的作用是使]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[工作在常建链状态（只能在用户侧使用），如果]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[未建链时配置该命令则]{style="font-family:宋体"}[Q.921]{lang="EN-US"}[会试图进行链路层建链操作；而]{style="font-family:宋体"}**[permanent-active]{lang="EN-US"}**[的作用是维持物理层的激活状态（只能在网络侧使用），物理层处于去激活时配置该命令并不会触发底层激活。]{style="font-family:宋体"}

[[物理层常激活功能只能供工作在网络侧模式下的]{style="font-family:宋体"}[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x2080039496}[接口使用，目前只有语音]{style="font-family:宋体"}[BSV]{lang="EN-US"}[板卡上的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口可以工作在网络侧模式。当]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口工作在用户侧模式时，不]{style="font-family:宋体"}[能]{style="font-family:宋体"}[配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x209930428}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_734327237}[使能工作在网络侧模式的]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[（]{style="font-family:宋体"}[BSV]{lang="EN-US"}[）接口的物理层常激活功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x638755}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn protocol-mode network]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] permanent-active]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x209864892}

[]{#OLE_LINK24}[]{#OLE_LINK21}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[isdn protocol-mode]{lang="EN-US"}**]{#struct_0_19941_14702_1052755033}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn q921-permanent]{lang="EN-US"}**]{#struct_0_19941_14702_x308355668}
:::

::: {#-82160098 .myid}
[]{#_Toc404785187}[]{#struct_0_19941_14702_117717006}[]{#_Toc353443139}[]{#_Toc352068930}

**ISDN \-- ISDN配置命令 \-- power-source**

------------------------------------------------------------------------

[**[power-source]{lang="EN-US"}**]{#struct_0_19941_14702_x210323644}[命令用来使能]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口的远程供电功能。]{style="font-family:宋体"}

[**[undo power-source]{lang="EN-US"}**]{#struct_0_19941_14702_x123374481}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x1557451117}

[**[power-source]{lang="EN-US"}**]{#struct_0_19941_14702_197914923}

[**[undo power-source]{lang="EN-US"}**]{#struct_0_19941_14702_x210258108}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19941_14702_x994478381}

[[BRI]{lang="EN-US"}]{#struct_0_19941_14702_1438810453}[接口的远程供电功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19941_14702_825627670}

[[ISDN BRI]{lang="EN-US"}]{#struct_0_19941_14702_x210192572}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19941_14702_1007479007}

[[network-admin]{lang="EN-US"}]{#struct_0_19941_14702_x183288615}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19941_14702_x1435066513}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19941_14702_x210127036}

[[当]{style="font-family:宋体"}[BRI]{lang="EN-US"}]{#struct_0_19941_14702_x945862988}[接口工作在网络侧模式时可以提供远程供电功能，比如工作在网络侧模式下的]{style="font-family:宋体"}[BSV]{lang="EN-US"}[接口和]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[数字电话相连时，]{style="font-family:宋体"}[BSV]{lang="EN-US"}[接口可以为数字电话供电。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19941_14702_x244504412}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[远程供电功能只能供工作在网络侧模式下的]{style="font-family:宋体"}]{#struct_0_19941_14702_x209537212}[BRI]{lang="EN-US"}[接口使用，目前只有语音]{style="font-family:宋体"}[BSV]{lang="EN-US"}[板卡上的]{style="font-family:宋体"}[BRI]{lang="EN-US"}[接口可以工作在网络侧模式。当]{style="font-family:宋体"}[BRI]{lang="SV"}[接口工作在用户侧模式时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不]{style="font-family:宋体"}[能]{style="font-family:宋体"}[配置本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19941_14702_1478709013}[BRI]{lang="SV"}[接口上存在呼叫时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不]{style="font-family:宋体"}[能]{style="font-family:宋体"}[配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19941_14702_x2057823436}

[[\# ]{lang="EN-US"}]{#struct_0_19941_14702_1979390497}[使能工作在网络侧模式的]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[（]{style="font-family:宋体"}[BSV]{lang="EN-US"}[）接口的远程供电功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19941_14702_x209471676}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] isdn protocol-mode network]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] power-source]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19941_14702_x457153022}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isdn protocol-mode]{lang="EN-US"}**]{#struct_0_19941_14702_1905759283}

[ ]{lang="EN-US"}
:::
