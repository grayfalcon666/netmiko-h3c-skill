::: {#-915425326 .myid}
[]{#_Toc404791668}[]{#struct_0_15685_x2028_522974159}[]{#_Toc336422432}

**MPLS OAM \-- MPLS OAM调试命令 \-- debugging mpls bfd**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15685_x2028_828676119}

[**[debugging mpls bfd ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **hsb** \| **packet** \| **process** }]{lang="EN-US"}]{#struct_0_15685_x2028_x860486262}

[**[undo debugging mpls bfd ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **hsb** \| **packet** \| **process** }]{lang="EN-US"}]{#struct_0_15685_x2028_x2068718356}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15685_x2028_314750789}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15685_x2028_1034155179}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15685_x2028_196774733}

[[network-admin]{lang="EN-US"}]{#struct_0_15685_x2028_x323583061}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15685_x2028_x549036276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15685_x2028_1480829350}

[**[all]{lang="EN-US"}**]{#struct_0_15685_x2028_1752974896}[：表示]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_15685_x2028_246305156}[：表示]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_15685_x2028_536460268}[：表示]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[hsb:]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_15685_x2028_332606652}[表示]{style="font-family:
宋体"}[MPLS BFD]{lang="EN-US"}[热备份事件的调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_15685_x2028_1564754470}[：表示]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[消息调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_15685_x2028_314947397}[：表示]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[处理过程调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15685_x2028_1612695358}

[**[debugging mpls bfd]{lang="EN-US"}**]{#struct_0_15685_x2028_x1396940112}[命令用来打开]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging mpls bfd**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}]{#struct_0_15685_x2028_x218267793}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mpls bfd error]{lang="EN-US"}]{#struct_0_15685_x2028_1638221453}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2027709922}[[字段]{style="font-family:黑体"}]{#struct_0_15685_x2028_x2040028986}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15685_x2028_x1599572250}

[[No enough memory.]{lang="EN-US"}]{#struct_0_15685_x2028_906081248}

[[没有足够内存]{style="font-family:宋体"}]{#struct_0_15685_x2028_314881861}

[[Not enough resources are available to complete the operation..]{lang="EN-US"}]{#struct_0_15685_x2028_x714547517}

[[没有足够资源，如]{style="font-family:宋体"}[discriminator]{lang="EN-US"}]{#struct_0_15685_x2028_x2109847785}[或]{style="font-family:宋体"}[Session Index]{lang="EN-US"}[已全被占用]{style="font-family:宋体"}

[[Invalid parameter.]{lang="EN-US"}]{#struct_0_15685_x2028_614665857}

[[无效参数]{style="font-family:宋体"}]{#struct_0_15685_x2028_x1365915138}

[[Session (*session*) received wrong session event (*event*) in *state* state*.*]{lang="EN-US"}]{#struct_0_15685_x2028_89367630}

[[会话（]{style="font-family:宋体"}*[session]{lang="EN-US"}*]{#struct_0_15685_x2028_x680297793}[）在状态（]{style="font-family:宋体"}*[state]{lang="EN-US"}*[）时接收到错误的会话事件，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[*[session]{lang="EN-US"}*]{#struct_0_15685_x2028_315078469}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type: LSP]{lang="EN-US"}]{#struct_0_15685_x2028_785992255}[;]{lang="EN-US"}[ FEC: *addr*/*masklen*]{lang="EN-US"}[; ]{lang="EN-US"}[EntryKey: *entrykey*]{lang="EN-US"}[：表示该会话用来检测]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址和掩码长度为]{lang="EN-US" style="font-family:宋体"}*[addr]{lang="EN-US"}*[/*masklen*]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[EntryKey]{lang="EN-US"}[为]{style="font-family:宋体"}*[entrykey]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type: TE]{lang="EN-US"}]{#struct_0_15685_x2028_x1392565445}[;]{lang="EN-US"}[ IfIndex: *ifindex*]{lang="EN-US"}[; ]{lang="EN-US"}[EntryKey: *entrykey*]{lang="EN-US"}[：表示该会话用来检测]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道，]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道对应的隧道接口索引为]{lang="EN-US" style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[，]{lang="EN-US" style="font-family:宋体"}[EntryKey]{lang="EN-US"}[为]{style="font-family:宋体"}*[entrykey]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type: PW]{lang="EN-US"}]{#struct_0_15685_x2028_x582203529}[; ]{lang="EN-US"}[Peer: *peer-ip*]{lang="EN-US"}[; ]{lang="EN-US"}[PW]{lang="EN-US"}[ ]{lang="EN-US"}[ID: *pw-id*]{lang="EN-US"}[;]{lang="EN-US"}[ EntryKey: *key*]{lang="EN-US"}[：表示该会话用来检测]{lang="EN-US" style="font-family:
  宋体"}[PW]{lang="EN-US"}[，对端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[的地址为]{lang="EN-US" style="font-family:宋体"}*[peer-ip]{lang="EN-US"}*[，]{lang="EN-US" style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[，]{lang="EN-US" style="font-family:宋体"}[EntryKey]{lang="EN-US"}[为]{style="font-family:宋体"}*[entrykey]{lang="EN-US"}*

[[会话状态]{style="font-family:宋体"}*[state]{lang="EN-US"}*]{#struct_0_15685_x2028_626970538}[取值包括]{style="font-family:宋体"}[INIT]{lang="EN-US"}[、]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[和]{style="font-family:宋体"}[UP]{lang="EN-US"}

[[会话事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_15685_x2028_x549684161}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUEST_TIMEOUT]{lang="EN-US"}]{#struct_0_15685_x2028_315012933}[：表示]{lang="EN-US" style="font-family:
  宋体"}[request]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AGE_TIMEOUT]{lang="EN-US"}]{#struct_0_15685_x2028_x431076176}[：表示老化定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DELAYNTF_TIMEOUT]{lang="EN-US"}]{#struct_0_15685_x2028_1770649718}[：表示延迟通知定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CHGEN]{lang="EN-US"}]{#struct_0_15685_x2028_1666915154}[C]{lang="EN-US"}[AP_TIMEOUT]{lang="EN-US"}[：表示更新封装定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CREATE_SSN]{lang="EN-US"}]{#struct_0_15685_x2028_2078579118}[：表示创建会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UPDATE_SSN]{lang="EN-US"}]{#struct_0_15685_x2028_552013621}[：表示更新会话]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DELETE_SSN]{lang="EN-US"}]{#struct_0_15685_x2028_315209541}[：表示删除会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECEIVE_REPLY]{lang="EN-US"}]{#struct_0_15685_x2028_x1294936697}[：表示收到]{style="font-family:宋体"}[echo reply]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECEIVE_REQUEST]{lang="EN-US"}]{#struct_0_15685_x2028_264587729}[：表示收到]{style="font-family:宋体"}[echo request]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD_SSNUP]{lang="EN-US"}]{#struct_0_15685_x2028_x583930148}[：表示]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}[UP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD_SSNDOWN]{lang="EN-US"}]{#struct_0_15685_x2028_225133898}[：表示]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD_SSNADMINDOWN]{lang="EN-US"}]{#struct_0_15685_x2028_315144005}[：表示]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话被配置删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD_SSNINITFAIL]{lang="EN-US"}]{#struct_0_15685_x2028_756292886}[：表示]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话初始化失败]{style="font-family:宋体"}

[[Failed to connect to BFD.]{lang="EN-US"}]{#struct_0_15685_x2028_790664792}

[[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_15685_x2028_944072465}[进程建立连接失败]{style="font-family:宋体"}

[[Received an invalid signaling message.]{lang="EN-US"}]{#struct_0_15685_x2028_x580677866}

[[接收到一个无效消息]{style="font-family:宋体"}]{#struct_0_15685_x2028_315340613}

[[Failed to send an HA message (*message*).]{lang="EN-US"}]{#struct_0_15685_x2028_x499359378}

[[发送]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15685_x2028_177343576}[消息失败，消息类型为]{style="font-family:宋体"}*[message]{lang="EN-US"}*

[*[message]{lang="EN-US"}*]{#struct_0_15685_x2028_x2043899311}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_315275077}[：表示批量备份]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_x2100749131}[：表示实时备份]{lang="EN-US" style="font-family:宋体"}

[[Failed to respond to HA. Event: *event*]{lang="EN-US"}]{#struct_0_15685_x2028_x1432536368}

[[回应]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15685_x2028_866530631}[事件失败，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[*[event]{lang="EN-US"}*]{#struct_0_15685_x2028_314816322}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_1257817756}[：表示]{style="font-family:宋体"}[HA]{lang="EN-US"}[模块去激活完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_523563983}[：表示批量备份完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_15685_x2028_2049324311}[：表示备板升级完成]{lang="EN-US" style="font-family:宋体"}

[[Failed to activate HA.]{lang="EN-US"}]{#struct_0_15685_x2028_314750786}

[[HA]{lang="EN-US"}]{#struct_0_15685_x2028_1034155184}[模块激活失败]{style="font-family:宋体"}

[[Failed to create the timer.]{lang="EN-US"}]{#struct_0_15685_x2028_x1714500115}

[[创建定时器失败]{style="font-family:宋体"}]{#struct_0_15685_x2028_x1989642882}

[[Failed to set the timer value.]{lang="EN-US"}]{#struct_0_15685_x2028_314947394}

[[设置定时器时间间隔失败]{style="font-family:宋体"}]{#struct_0_15685_x2028_1612695361}

[[Failed to start the timer.]{lang="EN-US"}]{#struct_0_15685_x2028_x1396350291}

[[启动定时器失败]{style="font-family:宋体"}]{#struct_0_15685_x2028_x1097842590}

[[Failed to process state machine event (*event*)*.*]{lang="EN-US"}]{#struct_0_15685_x2028_314881858}

[[处理状态机事件失败，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_15685_x2028_2006441660}

[*[event]{lang="EN-US"}*]{#struct_0_15685_x2028_x169833338}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_315078466}[：表示下发创建]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_785992264}[：表示下发删除]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_15685_x2028_1328423738}[：表示下发更新]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_15685_x2028_1005687086}[：表示发送]{lang="EN-US" style="font-family:宋体"}[echo request]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_15685_x2028_315012930}[：表示发送]{lang="EN-US" style="font-family:宋体"}[echo reply]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_15685_x2028_x431076179}[：表示删除]{style="font-family:宋体"}[MBFD]{lang="EN-US"}[会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_15685_x2028_1770059894}[：表示获取封装信息]{style="font-family:宋体"}

[[Failed to process echo reply message because the reply return code is *code.*]{lang="EN-US"}]{#struct_0_15685_x2028_315209538}

[[处理]{style="font-family:宋体"}[echo reply]{lang="EN-US"}]{#struct_0_15685_x2028_x2104240752}[消息失败：]{style="font-family:宋体"}[reply]{lang="EN-US"}[返回码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Failed to process echo reply message. Can\'t get session through the message.]{lang="EN-US"}]{#struct_0_15685_x2028_x1955799575}

[[处理]{style="font-family:宋体"}[echo reply]{lang="EN-US"}]{#struct_0_15685_x2028_315144002}[消息失败：通过该消息未获取到相应会话]{style="font-family:宋体"}

[[Failed to process echo reply message because sequence number doesn't match.]{lang="EN-US"}]{#struct_0_15685_x2028_756292881}

[[处理]{style="font-family:宋体"}[echo reply]{lang="EN-US"}]{#struct_0_15685_x2028_790664789}[消息失败：]{style="font-family:宋体"}[Sequence number]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[Failed to process echo reply message because FEC doesn't match.]{lang="EN-US"}]{#struct_0_15685_x2028_315340610}

[[处理]{style="font-family:宋体"}[echo reply]{lang="EN-US"}]{#struct_0_15685_x2028_x499359375}[消息失败：]{style="font-family:宋体"}[FEC]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging mpls bfd event]{lang="EN-US"}]{#struct_0_15685_x2028_177671256}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1729873410}[[字段]{style="font-family:黑体"}]{#struct_0_15685_x2028_42737109}

[[描述]{style="font-family:黑体"}]{#struct_0_15685_x2028_983573676}

[[Responded HA with an event (*event*)*.*]{lang="EN-US"}]{#struct_0_15685_x2028_x62240366}

[[回应]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15685_x2028_315275074}[事件，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[*[event]{lang="EN-US"}*]{#struct_0_15685_x2028_x2100749130}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_133547573}[：表示]{style="font-family:宋体"}[HA]{lang="EN-US"}[模块去激活完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_x508899951}[：表示批量备份完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_15685_x2028_x1297740971}[：表示备板升级完成]{style="font-family:宋体"}

[[Received an HA event (*event*)*.*]{lang="EN-US"}]{#struct_0_15685_x2028_116529390}

[[接收到一个]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15685_x2028_x281562657}[事件，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[*[event]{lang="EN-US"}*]{#struct_0_15685_x2028_314816323}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_1257817757}[：表示]{style="font-family:宋体"}[HA]{lang="EN-US"}[模块去激活完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_523629519}[：表示批量备份完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_15685_x2028_x1597325991}[：表示备板升级完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_15685_x2028_1029253483}[：表示主板降级完成]{style="font-family:宋体"}

[[Session (*session*) received session event (*event*) in *state* state.]{lang="EN-US"}]{#struct_0_15685_x2028_179212779}

[[会话（]{style="font-family:宋体"}*[session]{lang="EN-US"}*]{#struct_0_15685_x2028_314750787}[）在状态（]{style="font-family:宋体"}*[state]{lang="EN-US"}*[）时接收到会话事件，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Received APP event (*event*)*.*]{lang="EN-US"}]{#struct_0_15685_x2028_1034155185}

[[接收到来自]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}]{#struct_0_15685_x2028_x1714434579}[应用（如]{style="font-family:宋体"}[LSM]{lang="EN-US"}[模块、]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[模块）的事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[*[event]{lang="EN-US"}*]{#struct_0_15685_x2028_2067261595}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[17]{lang="EN-US"}]{#struct_0_15685_x2028_x192824403}[：表示创建会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[18]{lang="EN-US"}]{#struct_0_15685_x2028_314947395}[：表示删除会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[19]{lang="EN-US"}]{#struct_0_15685_x2028_1612695360}[：表示设置]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[20]{lang="EN-US"}]{#struct_0_15685_x2028_x1396415827}[：表示]{style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[21]{lang="EN-US"}]{#struct_0_15685_x2028_x192633674}[：表示更新会话]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mpls bfd hsb]{lang="EN-US"}]{#struct_0_15685_x2028_x905066345}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1734928642}[[字段]{style="font-family:黑体"}]{#struct_0_15685_x2028_262265264}

[[描述]{style="font-family:黑体"}]{#struct_0_15685_x2028_x200077094}

[[Sent an HA message (*message).*]{lang="EN-US"}]{#struct_0_15685_x2028_314881859}

[[发送一个]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15685_x2028_2006441659}[消息，类型为]{style="font-family:宋体"}*[message]{lang="EN-US"}*

[*[message]{lang="EN-US"}*]{#struct_0_15685_x2028_x169374587}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_x205655209}[：表示]{style="font-family:宋体"}[批量备份]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_1763129515}[：表示]{style="font-family:宋体"}[实时备份]{lang="EN-US" style="font-family:宋体"}

[[Received an HA message (*message).*]{lang="EN-US"}]{#struct_0_15685_x2028_x183950482}

[[接收一个]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_15685_x2028_x694401705}[消息，类型为]{style="font-family:宋体"}*[message]{lang="EN-US"}*

[*[message]{lang="EN-US"}*]{#struct_0_15685_x2028_315078467}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_785992265}[：表示]{style="font-family:宋体"}[批量备份]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_1328423739}[：表示]{style="font-family:宋体"}[实时备份]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging mpls bfd packet]{lang="EN-US"}]{#struct_0_15685_x2028_1005752622}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1735924130}[[字段]{style="font-family:黑体"}]{#struct_0_15685_x2028_747780693}

[[描述]{style="font-family:黑体"}]{#struct_0_15685_x2028_x405612504}

[[Received message (*message*). *fec*; discriminator: *discriminator*]{lang="EN-US"}]{#struct_0_15685_x2028_2045053038}

[[为]{style="font-family:宋体"}*[fec]{lang="EN-US"}*]{#struct_0_15685_x2028_315012931}[接收到]{style="font-family:宋体"}*[message]{lang="EN-US"}*[消息，]{style="font-family:宋体"}[discriminator]{lang="EN-US"}[为]{style="font-family:宋体"}*[discriminator]{lang="EN-US"}*

[*[message]{lang="EN-US"}*]{#struct_0_15685_x2028_x431076178}[取值包括]{style="font-family:宋体"}[Request]{lang="EN-US"}[和]{style="font-family:宋体"}[Reply]{lang="EN-US"}

[*[fec]{lang="EN-US"}*]{#struct_0_15685_x2028_1769994358}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type: LSP]{lang="EN-US"}]{#struct_0_15685_x2028_534717715}[; ]{lang="EN-US"}[FEC: *addr*/*masklen*]{lang="EN-US"}[：表示通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址和掩码长度为]{style="font-family:宋体"}*[addr]{lang="EN-US"}*[/*masklen*]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type: TE]{lang="EN-US"}]{#struct_0_15685_x2028_1320545193}[; ]{lang="EN-US"}[IfIndex:]{lang="EN-US"}[ ]{lang="EN-US"}*[ifindex]{lang="EN-US"}*[：表示通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道，]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道对应的隧道接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type: PW]{lang="EN-US"}]{#struct_0_15685_x2028_1570493813}[; ]{lang="EN-US"}[Peer: *peer*]{lang="EN-US"}*[-]{lang="EN-US"}[ip]{lang="EN-US"}*[;]{lang="EN-US"}[ PW]{lang="EN-US"}[ ]{lang="EN-US"}[ID: *pw*]{lang="EN-US"}*[-]{lang="EN-US"}[id]{lang="EN-US"}*[：表示通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[，对端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}*[peer-ip]{lang="EN-US"}*[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*

[[Sent message (*message*). *fec*]{lang="EN-US"}]{#struct_0_15685_x2028_594323742}

[[为]{style="font-family:宋体"}*[fec]{lang="EN-US"}*]{#struct_0_15685_x2028_315209539}[发送]{style="font-family:宋体"}*[message]{lang="EN-US"}*[消息]{style="font-family:宋体"}

[*[message]{lang="EN-US"}*]{#struct_0_15685_x2028_x2104240753}[取值包括]{style="font-family:宋体"}[Request]{lang="EN-US"}[和]{style="font-family:宋体"}[Reply]{lang="EN-US"}

[[Sent message (*message*). *session*]{lang="EN-US"}]{#struct_0_15685_x2028_773083780}

[[为]{style="font-family:宋体"}*[session]{lang="EN-US"}*]{#struct_0_15685_x2028_x1297506613}[发送]{style="font-family:宋体"}*[message]{lang="EN-US"}*[消息]{style="font-family:宋体"}

[*[message]{lang="EN-US"}*]{#struct_0_15685_x2028_x1347072103}[取值包括]{style="font-family:宋体"}[Request]{lang="EN-US"}[和]{style="font-family:宋体"}[Reply]{lang="EN-US"}

[[Received an echo reply message. Returned information: *information*]{lang="EN-US"}]{#struct_0_15685_x2028_1441937778}

[[接收到]{style="font-family:宋体"}[Echo reply]{lang="EN-US"}]{#struct_0_15685_x2028_315144003}[消息，回应信息为]{style="font-family:宋体"}*[information]{lang="EN-US"}*

[[Received an echo reply message. Downstream information: *information*; nexthop: *nexthop*; label: *label*]{lang="EN-US"}]{#struct_0_15685_x2028_756292880}

[[接收到]{style="font-family:宋体"}[Echo reply]{lang="EN-US"}]{#struct_0_15685_x2028_790664790}[消息，下游信息为]{style="font-family:宋体"}*[information]{lang="EN-US"}*[，下一跳地址为]{style="font-family:宋体"}*[nexthop]{lang="EN-US"}*[，标签为]{style="font-family:宋体"}*[label]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging mpls bfd process]{lang="EN-US"}]{#struct_0_15685_x2028_944072463}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1732272482}[[字段]{style="font-family:黑体"}]{#struct_0_15685_x2028_x580677868}

[[描述]{style="font-family:黑体"}]{#struct_0_15685_x2028_x413031682}

[[Added session (*session*) to BFD.]{lang="EN-US"}]{#struct_0_15685_x2028_x828220138}

[[在]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_15685_x2028_315340611}[进程中创建]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}*[session]{lang="EN-US"}*

[[Deleted session (*session*) from BFD.]{lang="EN-US"}]{#struct_0_15685_x2028_x499359376}

[[从]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_15685_x2028_177736792}[进程中删除]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}*[session]{lang="EN-US"}*

[[Updated session (*session*) in BFD]{lang="EN-US"}]{#struct_0_15685_x2028_794983470}

[[更新]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_15685_x2028_614684908}[进程中的会话]{style="font-family:宋体"}*[session]{lang="EN-US"}*

[[Created MBFD session (*session*). Index: *index*]{lang="EN-US"}]{#struct_0_15685_x2028_x1738194748}

[[创建]{style="font-family:宋体"}[MBFD]{lang="EN-US"}]{#struct_0_15685_x2028_1803835286}[会话]{style="font-family:宋体"}*[session]{lang="EN-US"}*[，会话索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[Destroyed MBFD session (*session*). Index: *index*]{lang="EN-US"}]{#struct_0_15685_x2028_315275075}

[[删除]{style="font-family:宋体"}[MBFD]{lang="EN-US"}]{#struct_0_15685_x2028_x2100749129}[会话]{style="font-family:宋体"}*[session]{lang="EN-US"}*[，会话索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[Allocated local discriminator (*discriminator*).]{lang="EN-US"}]{#struct_0_15685_x2028_x1788832264}

[[分配本地标识符]{style="font-family:宋体"}*[discriminator]{lang="EN-US"}*]{#struct_0_15685_x2028_1450651685}

[[Freed local discriminator (*discriminator*).]{lang="EN-US"}]{#struct_0_15685_x2028_333885500}

[[释放本地标识符]{style="font-family:宋体"}*[discriminator]{lang="EN-US"}*]{#struct_0_15685_x2028_768918570}

[[Started timer (*type*). ID: *id*]{lang="EN-US"}]{#struct_0_15685_x2028_1784063187}

[[开启]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_15685_x2028_1880900267}[类型定时器，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[*[type]{lang="EN-US"}*]{#struct_0_15685_x2028_2121954893}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_171529121}[：表示]{style="font-family:宋体"}[request]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_x894463796}[：表示老化定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_15685_x2028_x1132935077}[：表示通知定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_15685_x2028_1880834731}[：表示更新封装定时器]{style="font-family:宋体"}

[[Session (*session*) state changed from *old* to *new.*]{lang="EN-US"}]{#struct_0_15685_x2028_1728596183}

[[会话]{style="font-family:宋体"}*[session]{lang="EN-US"}*]{#struct_0_15685_x2028_1122257422}[状态由]{style="font-family:宋体"}*[old]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[new]{lang="EN-US"}*

[*[old]{lang="EN-US"}*]{#struct_0_15685_x2028_16760709}[和]{style="font-family:宋体"}*[new]{lang="EN-US"}*[取值包括]{style="font-family:宋体"}[INIT]{lang="EN-US"}[、]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[和]{style="font-family:宋体"}[UP]{lang="EN-US"}

[[Sent message to BFD. VRF: *vrf*; type: *type*; entry key: *key*; result: *result*]{lang="EN-US"}]{#struct_0_15685_x2028_1109206346}

[[发送消息到]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_15685_x2028_636816742}[进程，]{style="font-family:宋体"}[VRF]{lang="EN-US"}[为]{style="font-family:宋体"}*[vrf]{lang="EN-US"}*[，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测的隧道类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，]{style="font-family:宋体"}[Entry Key]{lang="EN-US"}[为]{style="font-family:宋体"}*[key]{lang="EN-US"}*[，结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[*[type]{lang="EN-US"}*]{#struct_0_15685_x2028_1881031339}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_15685_x2028_x231543794}[：表示通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[64]{lang="EN-US"}]{#struct_0_15685_x2028_1116428056}[：表示通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[128]{lang="EN-US"}]{#struct_0_15685_x2028_1712499060}[：表示通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测]{style="font-family:宋体"}[PW]{lang="EN-US"}

[*[result]{lang="EN-US"}*]{#struct_0_15685_x2028_x1973406501}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15685_x2028_1880965803}[：表示]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[其他]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15685_x2028_1723579730}[值表示]{style="font-family:宋体"}[失败]{lang="EN-US" style="font-family:宋体"}

[[Sent session (*session*) state changed message to APP. Current session state: *state*]{lang="EN-US"}]{#struct_0_15685_x2028_697584816}

[[向]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}]{#struct_0_15685_x2028_x1183616080}[应用发送会话]{style="font-family:宋体"}*[session]{lang="EN-US"}*[状态变化消息，当前会话状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[*[state]{lang="EN-US"}*]{#struct_0_15685_x2028_1881162411}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_15685_x2028_1349815838}[：表示]{style="font-family:宋体"}[UP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_15685_x2028_x1645353730}[：表示]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[Echo request not send due to no LSR-ID.]{lang="EN-US"}]{#struct_0_15685_x2028_x1216969248}

[[由于没有]{style="font-family:宋体"}[LSR-ID]{lang="EN-US"}]{#struct_0_15685_x2028_1881096875}[，不发送]{style="font-family:宋体"}[echo request]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Ignored the received echo request message due to lack of LSR-ID.]{lang="EN-US"}]{#struct_0_15685_x2028_x1349820243}

[[由于没有]{style="font-family:宋体"}[LSR-ID]{lang="EN-US"}]{#struct_0_15685_x2028_733630882}[，接收到]{style="font-family:宋体"}[echo request]{lang="EN-US"}[消息不做任何操作]{style="font-family:宋体"}

[[Ignored the received echo request message because no route found for sending echo reply.]{lang="EN-US"}]{#struct_0_15685_x2028_x249257974}

[[由于没有路由发送]{style="font-family:宋体"}[echo reply]{lang="EN-US"}]{#struct_0_15685_x2028_1881293483}[，接收到]{style="font-family:宋体"}[echo request]{lang="EN-US"}[消息不做任何操作]{style="font-family:宋体"}

[[Added periodic trace route. *fec*]{lang="EN-US"}]{#struct_0_15685_x2028_x181468399}

[[开始]{style="font-family:宋体"}*[fec]{lang="EN-US"}*]{#struct_0_15685_x2028_265658393}[的周期性]{style="font-family:宋体"}[Trace route]{lang="EN-US"}

[[Deleted periodic trace route. *fec*]{lang="EN-US"}]{#struct_0_15685_x2028_1881227947}

[[结束]{style="font-family:宋体"}*[fec]{lang="EN-US"}*]{#struct_0_15685_x2028_x987048567}[的周期性]{style="font-family:宋体"}[Trace route]{lang="EN-US"}

[[Ingored periodic trace route due to no route.]{lang="EN-US"}]{#struct_0_15685_x2028_415342380}

[[由于没有路由，忽略周期性]{style="font-family:宋体"}[Trace route]{lang="EN-US"}]{#struct_0_15685_x2028_x89017663}[操作]{style="font-family:宋体"}

[[Started detecting. *fec*]{lang="EN-US"}]{#struct_0_15685_x2028_1881424555}

[[开始检测]{style="font-family:宋体"}*[fec]{lang="EN-US"}*]{#struct_0_15685_x2028_x1788589739}

[[Detection information: NextHop *nexthop*, attempt count: *count*, TTL *ttl*]{lang="EN-US"}]{#struct_0_15685_x2028_x483545748}

[[检测相应信息，下一跳地址为]{style="font-family:宋体"}*[nexthop]{lang="EN-US"}*]{#struct_0_15685_x2028_1881359019}[，尝试次数为]{style="font-family:宋体"}*[count]{lang="EN-US"}*[，]{style="font-family:宋体"}[TTL]{lang="EN-US"}[为]{style="font-family:宋体"}*[ttl]{lang="EN-US"}*

[[Periodic traceroute detected an LSP failure and notified BFD of the failure. *fec*; nexthop: *nexthop*.]{lang="EN-US"}]{#struct_0_15685_x2028_1364215641}

[[周期性]{style="font-family:宋体"}[Trace route]{lang="EN-US"}]{#struct_0_15685_x2028_x73950439}[检测到]{style="font-family:宋体"}*[fec]{lang="EN-US"}*[、下一跳地址为]{style="font-family:宋体"}*[nexthop]{lang="EN-US"}*[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[存在故障，并通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15685_x2028_2033520654}

[[\# ]{lang="PT-BR"}]{#struct_0_15685_x2028_1906247872}[打开]{style="font-family:宋体"}[MPLS BFD]{lang="PT-BR"}[的错误调试信息开关。关闭]{style="font-family:宋体"}[BFD]{lang="EN-US"}[进程时，设备上会打印如下调试信息]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls bfd error]{lang="EN-US"}]{#struct_0_15685_x2028_1880900268}

[\<Sysname\> process shutdown name bfdd]{lang="EN-US"}

[\*Jun 29 00:37:13:758 2012 Sysname MBFD/7/ERROR: -MDC=1; Failed to connect to BFD.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_2122413645}*[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[进程建立连接失败。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15685_x2028_x1561557584}[打开]{style="font-family:宋体"}[MPLS BFD]{lang="PT-BR"}[的事件调试信息开关，配置通过]{style="font-family:宋体"}[BFD]{lang="PT-BR"}[检测]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[后，]{style="font-family:宋体"}[如果设备上存在对应的]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[，则会打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls bfd event]{lang="EN-US"}]{#struct_0_15685_x2028_1994155292}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls bfd]{lang="EN-US"}

[\[Sysname\] mpls bfd 22.22.2.2 32]{lang="EN-US"}

[\*Jun 29 12:21:09:494 2012 Sysname MBFD/7/EVENT: -MDC=1; Received APP event (17).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_x951011752}*[接收到]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[应用的会话创建事件。]{style="font-family:宋体"}*

[[\*Jun 29 12:21:09:494 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (CREATE_SSN) in INIT state.]{lang="EN-US"}]{#struct_0_15685_x2028_110787845}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_414042045}*[检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址为]{style="font-family:宋体"}[22.22.2.2/32]{lang="EN-US"}[）的]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[会话在状态]{style="font-family:宋体"}[INIT]{lang="EN-US"}[时收到会话事件，事件类型为创建会话。]{style="font-family:宋体"}*

[[\*Jun 29 12:21:11:559 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (REQUEST_TIMEOUT) in INIT state. ]{lang="EN-US"}]{#struct_0_15685_x2028_x2083377316}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_1880834732}*[会话在状态]{style="font-family:宋体"}[INIT]{lang="EN-US"}[时收到会话事件，事件类型为]{style="font-family:宋体"}[request]{lang="EN-US"}[定时器超时。]{style="font-family:宋体"}*

[[\*Jun 29 12:21:11:562 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (RECEIVE_REPLY) in INIT state.]{lang="EN-US"}]{#struct_0_15685_x2028_1728399575}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_310922614}*[会话在状态]{style="font-family:宋体"}[INIT]{lang="EN-US"}[时收到会话事件，事件类型为收到]{style="font-family:宋体"}[echo reply]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Jun 29 12:21:11:569 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (BFD_SSNUP) in DOWN state.]{lang="EN-US"}]{#struct_0_15685_x2028_255525976}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_1752189064}*[会话在状态]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[时收到会话事件，事件类型为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}[UP]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 29 12:21:16:659 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (DELAYNTF_TIMEOUT) in UP state.]{lang="EN-US"}]{#struct_0_15685_x2028_1763005748}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_2120063702}*[会话在状态]{style="font-family:宋体"}[UP]{lang="EN-US"}[时收到会话事件，事件类型为延迟通知定时器超时。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_15685_x2028_x253393616}[打开]{style="font-family:宋体"}[MPLS BFD]{lang="PT-BR"}[的处理过程调试信息开关。配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[，如果设备上存在对应的]{style="font-family:宋体"}[PW]{lang="EN-US"}[，且该]{style="font-family:宋体"}[PW]{lang="EN-US"}[处于]{style="font-family:宋体"}[Up]{lang="EN-US"}[状态，则会打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls bfd process]{lang="EN-US"}]{#struct_0_15685_x2028_1881031340}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsi ttt]{lang="EN-US"}

[\[Sysname-vsi-ttt\] pwsignaling ldp]{lang="EN-US"}

[\[Sysname-vsi-ttt-ldp\] peer 22.22.2.2 pw-id 1 pw-class test]{lang="EN-US"}

[\*Jun 29 12:36:34:958 2012 Sysname MBFD/7/PROCESS: -MDC=1; Created MBFD session (Type: PW; Peer: 22.22.2.2; PWID: 1; EntryKey: 1082130432). Index:1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_x232133615}*[创建检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[会话。]{style="font-family:宋体"}[PW]{lang="EN-US"}[的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[22.22.2.2]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 29 12:36:34:958 2012 Sysname MBFD/7/PROCESS: -MDC=1; Started timer (0) , ID: 0]{lang="EN-US"}]{#struct_0_15685_x2028_x1345104212}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_87727865}*[开启]{style="font-family:宋体"}[request]{lang="EN-US"}[定时器，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 29 12:36:36:959 2012 Sysname MBFD/7/PROCESS: -MDC=1; Allocated local discriminator (513)]{lang="EN-US"}]{#struct_0_15685_x2028_525459890}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_1733933386}*[分配本地标识符]{style="font-family:宋体"}[513]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 29 12:36:38:962 2012 Sysname MBFD/7/PROCESS: -MDC=1; Added session (Type: PW; Peer: 22.22.2.2; PWID: 1; EntryKey: 1082130432) to BFD.]{lang="EN-US"}]{#struct_0_15685_x2028_887589014}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_x589475940}*[在]{style="font-family:宋体"}[BFD]{lang="EN-US"}[进程中创建检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。]{style="font-family:宋体"}*

[[\*Jun 29 12:36:38:966 2012 Sysname MBFD/7/PROCESS: -MDC=1; Sent message to BFD. VRF: 0; type: 128; entry key: 1082130432; result: 0.]{lang="EN-US"}]{#struct_0_15685_x2028_1880965804}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_1723252050}*[发送消息到]{style="font-family:宋体"}[BFD]{lang="EN-US"}[进程，]{style="font-family:宋体"}[VRF]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测隧道为]{style="font-family:宋体"}[PW]{lang="EN-US"}[，]{style="font-family:宋体"}[Entry Key]{lang="EN-US"}[为]{style="font-family:宋体"}[1082130432]{lang="EN-US"}[，结果为成功。]{style="font-family:宋体"}*

[[\*Jun 29 12:36:38:966 2012 Sysname MBFD/7/PROCESS: -MDC=1; Session (Type: PW; Peer: 22.22.2.2; PWID: 1; EntryKey: 1082130432) state changed from INIT to DOWN.]{lang="EN-US"}]{#struct_0_15685_x2028_735911260}

[*[// MPLS BFD]{lang="EN-US"}*]{#struct_0_15685_x2028_476324406}*[会话状态由]{style="font-family:宋体"}[init]{lang="EN-US"}[变为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 29 12:36:38:967 2012 Sysname MBFD/7/PROCESS: -MDC=1; Started timer (1), ID: 0]{lang="EN-US"}]{#struct_0_15685_x2028_1335169392}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_1413432626}*[开启会话老化定时器，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 29 12:36:44:159 2012 Sysname MBFD/7/PROCESS: -MDC=1; Sent session (Type: PW; Peer: 22.22.2.2; PWID: 1; EntryKey: 1082130432) state changed message to APP. Current session state: 1]{lang="EN-US"}]{#struct_0_15685_x2028_737614701}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_1127375466}*[向]{style="font-family:宋体"}[MPLS BFD]{lang="EN-US"}[应用发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话状态变化消息，当前会话状态为]{style="font-family:宋体"}[Up]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_15685_x2028_177329712}[打开]{style="font-family:宋体"}[MPLS BFD]{lang="PT-BR"}[热备份事件调试信息开关。配置通过]{style="font-family:宋体"}[BFD]{lang="PT-BR"}[检测]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[，创建]{style="font-family:宋体"}[MPLS BFD]{lang="PT-BR"}[会话后，插入备板，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls bfd hsb ]{lang="EN-US"}]{#struct_0_15685_x2028_1881162412}

[\*Jun 29 15:30:45:203 2012 Sysname MBFD/7/NULL: -MDC=1; Sent an HA message (0). ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_15685_x2028_1350012446}*[备板插入，进行批量备份]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
