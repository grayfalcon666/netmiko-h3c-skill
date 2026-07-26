::: {#432711772 .myid}
[]{#_Toc404794394}[]{#struct_0_44918_15685_x2094468048}[]{#_Toc375832075}

**SIP \-- SIP调试命令 \-- debugging voice sip**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_44918_15685_2079609697}

[**[debugging voice sip ]{lang="EN-US"}**[{ **all** \| **error** **\| event \| fsm \| info \| message \| stack \| timer }**]{lang="EN-US"}]{#struct_0_44918_15685_x1370419378}

[**[undo debugging voice sip]{lang="EN-US"}**[ { **all** \| **error** \| **event \| fsm \| info \| message \| stack \| timer** }]{lang="EN-US"}]{#struct_0_44918_15685_556770858}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44918_15685_531930766}

[[用户视图]{style="font-family:宋体"}]{#struct_0_44918_15685_639854821}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44918_15685_x666397302}

[[network-admin]{lang="EN-US"}]{#struct_0_44918_15685_x686337729}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44918_15685_1173135991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44918_15685_775131826}

[**[all]{lang="EN-US"}**]{#struct_0_44918_15685_1073131527}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_44918_15685_949272651}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_44918_15685_1729388427}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[的事件类消息调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_44918_15685_328456408}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[的状态机类消息调试信息开关。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_44918_15685_424755641}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[的信息类消息调试信息开关。]{style="font-family:宋体"}

[**[message]{lang="EN-US"}**]{#struct_0_44918_15685_366768979}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[的报文类消息调试信息开关。]{style="font-family:宋体"}

[**[stack]{lang="EN-US"}**]{#struct_0_44918_15685_x1366746297}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[协议栈类消息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_44918_15685_x1697993470}[：表示]{style="font-family:宋体"}[SIP]{lang="EN-US"}[的定时器消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_44918_15685_224115127}

[**[debugging voice sip]{lang="EN-US"}**]{#struct_0_44918_15685_x1662211192}[命令用来打开]{style="font-family:宋体"}[SIP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice sip]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SIP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SIP]{lang="EN-US"}]{#struct_0_44918_15685_2122854799}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging voice sip error]{lang="EN-US"}]{#struct_0_44918_15685_x1153608716}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1563186973}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_44918_15685_603480013}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_x947717983}

[[Failed to allocate memory for CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x803812750}

[[为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x2110977877}[CCB]{lang="EN-US" style="font-size:9.0pt"}[分配内存失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to get CCB when binding source address.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1038460096}

[[源地址绑定时获取]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_1864504478}[CCB]{lang="EN-US" style="font-size:9.0pt"}[失败]{style="font-size:9.0pt;font-family:宋体"}

[[Received INVITE request: Failed to get SDP media description.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1565579888}

[[收到]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1757164327}[INVITE]{lang="EN-US" style="font-size:9.0pt"}[请求：获取]{style="font-size:9.0pt;font-family:宋体"}[SDP]{lang="EN-US" style="font-size:9.0pt"}[媒体描述信息失败]{style="font-size:9.0pt;font-family:
  宋体"}

[[Received  ALERTING message: Failed to save brother codec.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x2130401618}

[[收到]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_597773088}[ALERTING]{lang="EN-US" style="font-size:9.0pt"}[消息：保存兄弟编解码类型失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to get SIP CCB in normal call back.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x606028556}

[[在正常回调中获取]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1001810606}[SIP CCB]{lang="EN-US" style="font-size:9.0pt"}[失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to set Request-Line when building INVITE message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1178005213}

[[构建]{style="font-size:9.0pt;font-family:
  宋体"}]{#struct_0_44918_15685_49659518}[INVITE]{lang="EN-US" style="font-size:9.0pt"}[消息时设置请求行失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to create DNS CCB.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_732739582}

[[创建]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1977893850}[DNS CCB]{lang="EN-US" style="font-size:9.0pt"}[失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to process DNS response before registration because the source or destination IP address cannot be obtained.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_446901257}

[[因为无法获取源]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1433982982}[/]{lang="EN-US" style="font-size:9.0pt"}[目的地址，处理注册前的]{style="font-size:9.0pt;font-family:宋体"}[DNS]{lang="EN-US" style="font-size:9.0pt"}[应答消息失败]{style="font-size:9.0pt;font-family:
  宋体"}

[[Failed to decode SDP.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1227383083}

[[解码]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1991209101}[SDP]{lang="EN-US" style="font-size:9.0pt"}[失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to negotiate brother and local codec set.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1316285745}

[[协商兄弟和本地编码集失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x20225220}

[[Invalid message body.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1210513526}

[[无效的消息体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_748000957}

[[Failed to send ACK message for SIP connect.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1371811248}

[[发送]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x2009350296}[SIP connect]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[ACK]{lang="EN-US" style="font-size:9.0pt"}[消息失败]{style="font-size:9.0pt;font-family:
  宋体"}

[[Session Expires(*Expires-Value*) value is smaller than Min-Se(*Min-Value*)]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1300244781}

[[会话有效时间小于最小有效时间]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1488778836}

[*[Expires-Value]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_x1412597610}[：]{style="font-size:9.0pt;font-family:
  宋体"}[Expires]{lang="EN-US" style="font-size:9.0pt"}[头域的值]{style="font-size:9.0pt;font-family:宋体"}

[*[Min-Value]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_x1191078262}[：]{style="font-size:9.0pt;font-family:宋体"}[Min-Se]{lang="EN-US" style="font-size:9.0pt"}[头域的值]{style="font-size:9.0pt;
  font-family:宋体"}

[[TLS: Failed to create listener.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x720311250}

[[创建]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_874411436}[TLS listener]{lang="EN-US" style="font-size:9.0pt"}[失败]{style="font-size:9.0pt;font-family:宋体"}

[[TLS: Failed to set connection to no-block mode.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1587115241}

[[设置]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x2093519127}[TLS]{lang="EN-US" style="font-size:9.0pt"}[连接为非阻塞模式失败]{style="font-size:9.0pt;font-family:宋体"}

[[TPTD:Failed to allocate memory for contex CB]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x208108057}

[[TPTD]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1069782452}[：为上下文控制块申请内存失败]{style="font-size:9.0pt;font-family:宋体"}

[[TPTD: Failed to generate hash key by address.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_153486331}

[[TPTD]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_916555950}[：由地址产生]{style="font-size:9.0pt;font-family:宋体"}[hash key]{lang="EN-US" style="font-size:9.0pt"}[失败]{style="font-size:9.0pt;
  font-family:宋体"}

[[Build Contact header: Failed to set param for Contact.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_502087956}

[[建立]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x477611291}[ Contact ]{lang="EN-US" style="font-size:9.0pt"}[头域：为]{style="font-size:9.0pt;font-family:宋体"}[Contact]{lang="EN-US" style="font-size:9.0pt"}[设置参数失败]{style="font-size:9.0pt;
  font-family:宋体"}

[[Build Allow header: Failed to create Allow header.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1899786707}

[[建立]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1116831758}[ Allow ]{lang="EN-US" style="font-size:9.0pt"}[头域：创建]{style="font-size:9.0pt;font-family:宋体"}[Allow]{lang="EN-US" style="font-size:9.0pt"}[头域失败]{style="font-size:9.0pt;font-family:
  宋体"}

[[Build Allow header: Failed to add *method* method to Allow.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1719570272}

[[建立]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1623784322}[ Allow ]{lang="EN-US" style="font-size:9.0pt"}[头域：添加]{style="font-size:9.0pt;font-family:宋体"}*[method]{lang="EN-US" style="font-size:9.0pt"}*[方法到]{style="font-size:9.0pt;
  font-family:宋体"}[Allow]{lang="EN-US" style="font-size:9.0pt"}[头域失败]{style="font-size:9.0pt;font-family:宋体"}

[[Allow]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1823301303}[头域支持的方法如下]{style="font-size:9.0pt;font-family:宋体"}[(*method*]{lang="EN-US" style="font-size:9.0pt"}[的取值非如下值]{style="font-size:9.0pt;font-family:宋体"}[)]{lang="EN-US" style="font-size:9.0pt"}[：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[METHOD_TYPE_ACK]{lang="EN-US"}]{#struct_0_44918_15685_828543352}[：]{lang="EN-US" style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[ACK]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[METHOD_TYPE_BYE]{lang="EN-US"}]{#struct_0_44918_15685_x1113908230}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[BYE]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[METHOD_TYPE_CANCEL]{lang="EN-US"}]{#struct_0_44918_15685_850044623}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[CANCEL]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[METHOD_TYPE_INFO]{lang="EN-US"}]{#struct_0_44918_15685_x1365543443}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[INFO]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[METHOD_TYPE_INVITE]{lang="EN-US"}]{#struct_0_44918_15685_1024229139}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[INVITE]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[METHOD_TYPE_NOTIFY]{lang="EN-US"}]{#struct_0_44918_15685_831671698}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[NOTIFY]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[METHOD_TYPE_PRACK]{lang="EN-US"}]{#struct_0_44918_15685_x1118828583}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[PRACK]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[METHOD_TYPE_REFER]{lang="EN-US"}]{#struct_0_44918_15685_735901064}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[REFER]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[METHOD_TYPE_REGISTER]{lang="EN-US"}]{#struct_0_44918_15685_200540498}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[REGISTER]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[METHOD_TYPE_UPDATE]{lang="EN-US"}]{#struct_0_44918_15685_x771429807}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[UPDATE]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[METHOD_TYPE_SUBSCRIBE]{lang="EN-US"}]{#struct_0_44918_15685_x266082037}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[SUBSCRIBE]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[METHOD_TYPE_OPTIONS]{lang="EN-US"}]{#struct_0_44918_15685_413993367}[：]{style="font-family:宋体"}[Allow]{lang="EN-US"}[头域支持]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}[操作方法]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging voice sip event]{lang="EN-US"}]{#struct_0_44918_15685_502428519}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1587496721}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_x1865693868}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_x452995078}

[[ CMC \--\> SIP : *message-type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x602166302}

[[SIP]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1104225772}[收到]{style="font-size:9.0pt;font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[发来的]{style="font-size:9.0pt;
  font-family:宋体"}*[message-type]{lang="EN-US" style="font-size:9.0pt"}*[消息]{style="font-size:9.0pt;font-family:宋体"}

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_x1009378619}[的取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_44918_15685_1192078694}[：表示]{lang="EN-US" style="font-family:宋体"}[出]{style="font-family:宋体"}[局端]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[CMC]{lang="EN-US"}[向]{style="font-family:宋体"}[SIP]{lang="EN-US"}[发送建立新呼叫信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CHANNEL_READY_ACK]{lang="EN-US"}]{#struct_0_44918_15685_x1673743412}[：表示出局端]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[CMC]{lang="EN-US"}[对]{style="font-family:宋体"}[SIP ]{lang="EN-US"}[ACCP_CHANNEL_READY]{lang="EN-US"}[的]{style="font-family:
  宋体"}[应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_INDICATE]{lang="EN-US"}]{#struct_0_44918_15685_1979253301}[：表示出局端]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{lang="EN-US" style="font-family:宋体"}[指示]{style="font-family:宋体"}[信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE_COMPLETE]{lang="EN-US"}]{#struct_0_44918_15685_x1144346140}[：]{style="font-family:宋体"}[表示出局端]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{lang="EN-US" style="font-family:宋体"}[释放结束信令]{style="font-family:宋体"}

[[SIP \--\> CMC : *message-type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x640497895}

[[SIP]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_450349647}[向]{style="font-size:9.0pt;font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[发送]{style="font-size:9.0pt;font-family:
  宋体"}*[message-type]{lang="EN-US" style="font-size:9.0pt"}*[消息]{style="font-size:9.0pt;font-family:宋体"}

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_1915943077}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_44918_15685_x1534810576}[：]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话建立的确认信令]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_44918_15685_763076356}[：]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃信令]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_CHANNEL_READY]{lang="EN-US"}]{#struct_0_44918_15685_556705322}[：]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送媒体通道就绪信令]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_INFORMATION]{lang="EN-US"}]{#struct_0_44918_15685_x1082613606}[：]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信令]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_44918_15685_x2028859132}[：]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送连接信令]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_44918_15685_1834091655}[：]{lang="EN-US" style="font-family:宋体"}[SIP]{lang="EN-US"}[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话释放信令]{style="font-family:宋体"}

[[Adapter \--\> Stack : *message_type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x815882109}

[[适配层向协议栈发送]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x911218197}*[message_type]{lang="EN-US" style="font-size:
  9.0pt"}*[消息]{style="font-size:9.0pt;font-family:宋体"}

[*[message_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_x151882038}[取值如下：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Setup ]{lang="EN-US"}]{#struct_0_44918_15685_x411498024}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：适配层向协议栈发送呼叫建立请求]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[PRACK ]{lang="EN-US"}]{#struct_0_44918_15685_1594193783}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：适配层向协议栈发送]{style="font-family:宋体"}[PRACK]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Connect ]{lang="EN-US"}]{#struct_0_44918_15685_2122789263}[ack]{lang="EN-US"}[ ]{lang="EN-US"}[r]{lang="EN-US"}[equest]{lang="EN-US"}[：适配层向协议栈发送连接确认请求]{style="font-family:宋体"}

[[Stack \--\> Adapter : *message_type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1614659399}

[[协议栈向适配层发送]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1749442704}*[message_type]{lang="EN-US" style="font-size:
  9.0pt"}*[消息]{style="font-size:9.0pt;font-family:宋体"}

[*[message_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_13205544}[取值如下：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Setup ack]{lang="EN-US"}]{#struct_0_44918_15685_x36023884}[：协议栈向适配层发送连接确认消息]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Alerting ]{lang="EN-US"}]{#struct_0_44918_15685_654801862}[i]{lang="EN-US"}[ndication]{lang="EN-US"}[：协议栈向适配层发送振铃指示]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_44918_15685_x1000027354}[rack]{lang="EN-US"}[ ]{lang="EN-US"}[r]{lang="EN-US"}[esponse]{lang="EN-US"}[：协议栈向适配层发送]{style="font-family:宋体"}[Prack]{lang="EN-US"}[应答]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Connect ]{lang="EN-US"}]{#struct_0_44918_15685_x606094092}[i]{lang="EN-US"}[ndication]{lang="EN-US"}[：协议栈向适配层发送连接指示]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Release ]{lang="EN-US"}]{#struct_0_44918_15685_2137899746}[i]{lang="EN-US"}[ndication]{lang="EN-US"}[：协议栈向适配层发送通话释放指示]{style="font-family:宋体"}

[[The Content-Type header does not exist.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_267139027}

[[Content-Type]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_631384033}[头域不存在]{style="font-size:9.0pt;font-family:宋体"}

[[Get first address by ip (*ip*)]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1257707349}

[[通过]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x385551923}[ip]{lang="EN-US" style="font-size:9.0pt"}[的获取第一个地址]{style="font-size:9.0pt;font-family:宋体"}

[*[ip]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_1838791012}[为用于地址查询的]{style="font-size:9.0pt;font-family:宋体"}[ip]{lang="EN-US" style="font-size:9.0pt"}

[[Get *signaling/media* address by global configuration.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x332029920}

[[通过全局配置获取*信令*]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_1316220209}*[/]{lang="EN-US" style="font-size:9.0pt"}[媒体]{style="font-size:9.0pt;
  font-family:宋体"}*[地址]{style="font-size:9.0pt;font-family:宋体"}

[[Set SDP media field: *MediaNumber*  media description(s) to be set.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1587938663}

[[设置]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_1595396472}[SDP]{lang="EN-US" style="font-size:9.0pt"}[媒体域：]{style="font-size:9.0pt;font-family:宋体"}*[MediaNumber]{lang="EN-US" style="font-size:9.0pt"}*[个媒体行被设置]{style="font-size:9.0pt;
  font-family:宋体"}

[[Codec negotiated result is voice media update.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1748124166}

[[编解码协商的结果是语音媒体更新]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x337809072}

[[DNS queried done, now the state is *state*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x661515439}

[[DNS]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1412663146}[查询完成，目前状态为]{style="font-size:9.0pt;font-family:宋体"}*[state]{lang="EN-US" style="font-size:9.0pt"}*

[[Audio media takes different media ip address or port]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_139687088}

[[语音媒体携带了不同的媒体地址或端口]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x2061740115}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging voice sip info]{lang="EN-US"}]{#struct_0_44918_15685_x951027297}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1588096357}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_x272187041}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_778717439}

[[Get loopback address for local using FIB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1750519745}

[[使用]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_1133709304}[FIB]{lang="EN-US" style="font-size:9.0pt"}[表为本地获取]{style="font-size:9.0pt;font-family:宋体"}[loopback]{lang="EN-US" style="font-size:9.0pt"}[地址]{style="font-size:9.0pt;
  font-family:宋体"}

[[SIP service(Call-Waiting) is processing.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_519783671}

[[SIP]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1928515722}[业务]{style="font-size:9.0pt;font-family:宋体"}[(]{lang="EN-US" style="font-size:9.0pt"}[呼叫等待]{style="font-size:9.0pt;
  font-family:宋体"}[)]{lang="EN-US" style="font-size:9.0pt"}[正在处理]{style="font-size:9.0pt;font-family:宋体"}

[[Local ringing.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_153420795}

[[本地振铃]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_1725937552}

[[There is no SDP in SIP message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x164643296}

[[SIP]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1861320866}[消息中不存在]{style="font-size:9.0pt;font-family:宋体"}[SDP]{lang="EN-US" style="font-size:9.0pt"}

[[Reconnecting to HA daemon, Please wait\...]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_575707167}

[[重连]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_1544003440}[HA]{lang="EN-US" style="font-size:9.0pt"}[守护进程，请等待]{style="font-size:9.0pt;font-family:宋体"}[......]{lang="EN-US" style="font-size:9.0pt"}

[[Failed to connect to HA daemon.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1260965694}

[[连接]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x1927243339}[HA]{lang="EN-US" style="font-size:9.0pt"}[守护进程失败]{style="font-size:9.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging voice sip timer]{lang="EN-US"}]{#struct_0_44918_15685_x984953861}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1581760925}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_1719504736}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_1910429422}

[[\[*module*\] start timer, Group id = *number1*, Index = *number2*, Duration = *number3*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x2088684320}

[*[module]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_x1909858576}[启动定时器，]{style="font-size:9.0pt;font-family:宋体"}[Group id ]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:
  9.0pt;font-family:宋体"}*[number1]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:宋体"}*[Index]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:
  宋体"}*[number2]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:宋体"}*[Duration]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;
  font-family:宋体"}*[number3]{lang="EN-US" style="font-size:9.0pt"}*

[[Deleting timer within RCB *rcb_id* server *server_index* before sending unregistration message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x2085994581}

[[在发送去注册之前删除注册控制块]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x781614681}*[server_index]{lang="EN-US" style="font-size:9.0pt"}*[服务器]{style="font-size:9.0pt;
  font-family:宋体"}*[rcb_id]{lang="EN-US" style="font-size:9.0pt"}*[控制块内的定时器]{style="font-size:9.0pt;font-family:宋体"}

[[Timer for sending REGISTER messages will be created ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x203352161}

[[before adding RCB *rcb_id* to message-sending list.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_1146488785}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x986585038}*[rcb_id]{lang="EN-US" style="font-size:9.0pt"}*[控制块添加到消息发送链表之前注册报文发送定时器将被创建]{style="font-size:9.0pt;font-family:宋体"}

[[\[SIP_REGISTER\] The message sending list is empty.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x420901935}

[[SIP]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_44918_15685_x1870367145}[注册：消息发送链表为空]{style="font-size:9.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging voice sip fsm]{lang="EN-US"}]{#struct_0_44918_15685_1548244110}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1585445153}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_x1365608979}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_44918_15685_424743158}

[[\[SIP_CALL\]\[*id*\]: Process the event of *event_type* in state *state_type*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_44918_15685_x36592662}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_44918_15685_x92414647}*[state_type]{lang="EN-US" style="font-size:9.0pt"}*[状态下处理]{style="font-size:9.0pt;font-family:宋体"}*[event_type]{lang="EN-US" style="font-size:9.0pt"}*[事件]{style="font-size:9.0pt;
  font-family:宋体"}

[*[id]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_x410183782}[用于标识一路呼叫]{style="font-size:9.0pt;font-family:宋体"}

[*[state_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_2044228673}[取值如下：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EVENT_ACCP_SETUP]{lang="EN-US"}]{#struct_0_44918_15685_159767526}[：建立连接事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EVENT_NO_FEATURE_SETUP]{lang="EN-US"}]{#struct_0_44918_15685_x668092875}[：非特性连接事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EVENT_ADDR_IN_DAILPEER]{lang="EN-US"}]{#struct_0_44918_15685_x2039477868}[：]{style="font-family:宋体"}[Dial peer]{lang="EN-US"}[获取地址事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EVENT_LOOKUP_SUCCESS]{lang="EN-US"}]{#struct_0_44918_15685_1962752217}[：地址查询成功事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EVENT_GET_ADDRINFO_SUCCESS]{lang="EN-US"}]{#struct_0_44918_15685_701447330}[：获取地址成功事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EVENT_SIP_ALERTING]{lang="EN-US"}]{#struct_0_44918_15685_200474962}[：振铃事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EVENT_EXIST_SDP_BODY]{lang="EN-US"}]{#struct_0_44918_15685_x849203009}[：存在]{style="font-family:宋体"}[SDP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EVENT_SIP_CONNECT]{lang="EN-US"}]{#struct_0_44918_15685_x1157653487}[：连接建立事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EVENT_SIP_RELEASE]{lang="EN-US"}]{#struct_0_44918_15685_614381674}[：释放连接事件]{style="font-family:宋体"}

[*[event_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_44918_15685_x1423152205}[取值如下：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_44918_15685_1814719646}[TATE_IDLE]{lang="EN-US"}[：空闲状态]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[STATE_CALL_ORIGINATING]{lang="EN-US"}]{#struct_0_44918_15685_x194562811}[：呼叫发起等待应答状态]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[STATE_CONNECTED]{lang="EN-US"}]{#struct_0_44918_15685_942095569}[：呼叫建立状态]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[STATE_CALL_TERMINATING]{lang="EN-US"}]{#struct_0_44918_15685_x1849297671}[：呼叫终止状态]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[STATE_MEDIA_IDLE]{lang="EN-US"}]{#struct_0_44918_15685_x1047841896}[：媒体空闲状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44918_15685_x1009444155}

[[\# ]{lang="EN-US"}]{#struct_0_44918_15685_x822207306}[本地]{style="font-family:宋体"}[LGS]{lang="EN-US"}[通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[网络建立了呼叫。打开主叫侧]{style="font-family:宋体"}[SIP]{lang="EN-US"}[所有类型的调试信息输出开关。]{style="font-family:宋体"}

[[\<Sysname\>debugging voice sip all]{lang="EN-US"}]{#struct_0_44918_15685_x72315877}

[\<Sysname\>\*Jan 23 10:21:15:262 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: CMC \--\> SIP : ACCP_SETUP.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_x2028034647}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发来的启动呼叫（]{style="font-family:宋体"}[ACCP_SETUP]{lang="EN-US"}[）消息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_730810687}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_ACCP_SETUP in state STATE_IDLE.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_x1102515334}*[呼叫状态机在初始状态下处理]{style="font-family:宋体"} [ACCP_SETUP]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_556639786}

[SIP EVENT: Do not exist content type.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: The header of ReferredBy does not exist.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_NO_FEATURE_SETUP in state STATE_IDLE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_ADDR_IN_DAILPEER in state STATE_IDLE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Get first address by ip (192.168.4.16).]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_LOOKUP_SUCCESS in state STATE_IDLE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:264 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Get signalling address by global.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:264 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP INFO: Get address from GigabitEthernet0/0(192.168.4.66).]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:264 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_GET_ADDRINFO_SUCCESS in state STATE_IDLE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:264 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SIP \--\> CMC : ACCP_SETUP_ACK.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_x713985247}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[回复]{style="font-family:宋体"}[ACCP_SETUP_ACK]{lang="EN-US"}*[消息]{style="font-size:8.5pt;font-family:
宋体"}

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:265 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_403910862}

[SIP EVENT: SIP set SDP media field: total 1 media description(s) to be set.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:271 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Adapter \--\> Stack : Setup Request.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_x1662606191}*[适配层向协议栈发送]{style="font-family:宋体"}[SETUP]{lang="EN-US"}[请求]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:272 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_2122723727}

[SIP EVENT: SrcAddr: 192.168.4.66, SrcPort: 5060, DestAddr: 192.168.4.16, DestPort: 5060, Protocol: UDP]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:272 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[Stack\-\--\>NetWork:]{lang="EN-US"}

[INVITE sip:444@192.168.4.16:5060;user=phone SIP/2.0]{lang="EN-US"}

[Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK607a839c51b]{lang="EN-US"}

[Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66]{lang="EN-US"}

[From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c]{lang="EN-US"}

[To: \<sip:444@192.168.4.16;user=phone\>]{lang="EN-US"}

[CSeq: 1 INVITE]{lang="EN-US"}

[Contact: \<sip:666@192.168.4.66:5060;user=phone\>]{lang="EN-US"}

[Supported: timer,100rel]{lang="EN-US"}

[Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,REGISTER,INFO,PRACK,SUBSCRIBE,NOTIFY,UPDATE,REFER]{lang="EN-US"}

[Date: Thu, 23 Jan 2014 10:21:15 GMT]{lang="EN-US"}

[Remote-Party-ID: \<sip:666@192.168.4.66;user=phone\>;party=calling;privacy=off]{lang="EN-US"}

[Max-Forwards: 70]{lang="EN-US"}

[Content-Length: 238]{lang="EN-US"}

[Content-Type: application/sdp]{lang="EN-US"}

[ ]{lang="EN-US"}

[v=0]{lang="EN-US"}

[o=H3C 1390472475 1390472475 IN IP4 192.168.4.66]{lang="EN-US"}

[s=Sip Call]{lang="EN-US"}

[c=IN IP4 192.168.4.66]{lang="EN-US"}

[t=0 0]{lang="EN-US"}

[m=audio 16302 RTP/AVP 18 8 0 4]{lang="EN-US"}

[a=rtpmap:18 G729/8000]{lang="EN-US"}

[a=fmtp:18 annexb=no]{lang="EN-US"}

[a=rtpmap:8 PCMA/8000]{lang="EN-US"}

[a=rtpmap:0 PCMU/8000]{lang="EN-US"}

[a=rtpmap:4 G723/8000]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_787514643}*[协议栈向网络侧发送]{style="font-family:宋体"}[INVITE]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:272 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_1679152903}

[SIP EVENT: Get signalling address by global.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:272 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TPT\] Start Timer, Group id = 2, Index = 411, Duration = 30000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Start Timer, Group id = 3, Index = 50, Duration = 500.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Start Timer, Group id = 4, Index = 50, Duration = 32000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Start Timer, Group id = 9, Index = 1, Duration = 600000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Stack \--\> Adapter : Setup Ack.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_2028805661}*[协议栈向适配层发送]{style="font-family:宋体"}[SETUP]{lang="EN-US"}[请求的应答消息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_x170145652}

[SIP TIMER: \[SIP_COMP_TPT\] Stop Timer, Group id = 2, Index = 411.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:277 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SrcAddr: 192.168.4.16, SrcPort: 64135, DestAddr: 192.168.4.66, DestPort: 5060, Protocol: UDP]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:278 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[NetWork\-\--\>Stack:]{lang="EN-US"}

[SIP/2.0 100 Trying]{lang="EN-US"}

[Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK607a839c51b]{lang="EN-US"}

[From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c]{lang="EN-US"}

[To: \<sip:444@192.168.4.16;user=phone\>]{lang="EN-US"}

[Date: Thu, 23 Jan 2014 02:25:36 GMT]{lang="EN-US"}

[Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66]{lang="EN-US"}

[CSeq: 1 INVITE]{lang="EN-US"}

[Allow-Events: telephone-event]{lang="EN-US"}

[Server: Cisco-SIPGateway/IOS-15.2.4.M2]{lang="EN-US"}

[Content-Length: 0]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_x606159628}*[协议栈从网络侧收到]{style="font-family:宋体"}[100trying]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:278 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_x227079597}

[SIP TIMER: \[SIP_COMP_TXN\] Stop Timer, Group id = 3, Index = 50.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:323 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SrcAddr: 192.168.4.16, SrcPort: 64135, DestAddr: 192.168.4.66, DestPort: 5060, Protocol: UDP]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[NetWork\-\--\>Stack:]{lang="EN-US"}

[SIP/2.0 183 Session Progress]{lang="EN-US"}

[Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK607a839c51b]{lang="EN-US"}

[From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c]{lang="EN-US"}

[To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D]{lang="EN-US"}

[Date: Thu, 23 Jan 2014 02:25:36 GMT]{lang="EN-US"}

[Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66]{lang="EN-US"}

[CSeq: 1 INVITE]{lang="EN-US"}

[Require: 100rel]{lang="EN-US"}

[RSeq: 8]{lang="EN-US"}

[Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER]{lang="EN-US"}

[Allow-Events: telephone-event]{lang="EN-US"}

[Remote-Party-ID: \<sip:444@192.168.4.16\>;party=called;screen=no;privacy=off]{lang="EN-US"}

[Contact: \<sip:444@192.168.4.16:5060\>]{lang="EN-US"}

[Supported: sdp-anat]{lang="EN-US"}

[Server: Cisco-SIPGateway/IOS-15.2.4.M2]{lang="EN-US"}

[Content-Type: application/sdp]{lang="EN-US"}

[Content-Disposition: session;handling=required]{lang="EN-US"}

[Content-Length: 191]{lang="EN-US"}

[ ]{lang="EN-US"}

[v=0]{lang="EN-US"}

[o=CiscoSystemsSIP-GW-UserAgent 2464 7928 IN IP4 192.168.4.16]{lang="EN-US"}

[s=SIP Call]{lang="EN-US"}

[c=IN IP4 192.168.4.16]{lang="EN-US"}

[t=0 0]{lang="EN-US"}

[m=audio 20306 RTP/AVP 8]{lang="EN-US"}

[c=IN IP4 192.168.4.16]{lang="EN-US"}

[a=rtpmap:8 PCMA/8000]{lang="EN-US"}

[a=pti]{lang="EN-US"}

[\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG: continuing\...]{lang="EN-US"}

[me:20]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_592714206}*[协议栈从网络侧收到]{style="font-family:宋体"}[100trying]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_1316154673}

[SIP TIMER: \[SIP_COMP_TXN\] Stop Timer, Group id = 4, Index = 50.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Start Timer, Group id = 4, Index = 50, Duration = 256000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Start Timer, Group id = 5, Index = 1, Duration = 128000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Stop Timer, Group id = 9, Index = 1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Start Timer, Group id = 9, Index = 1, Duration = 600000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Stack \--\> Adapter : Alerting Indication.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_389076853}*[协议栈向适配层上报]{style="font-family:宋体"}[Alerting]{lang="EN-US"}[指令]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_721136501}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_SIP_ALERTING in state STATE_CALL_ORIGINATING.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_989022480}*[状态机处理]{style="font-family:宋体"}[EVENT_SIP_ALERTING]{lang="EN-US"}[事件在]{style="font-family:宋体"}[STATE_CALL_ORIGINATING]{lang="EN-US"}[状态下]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_x1412728682}

[SIP EVENT: Get signalling address by global.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP INFO: Get address from GigabitEthernet0/0(192.168.4.66).]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:326 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP INFO: Get address from GigabitEthernet0/0(192.168.4.66).]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:326 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Adapter \--\> Stack: PRACK Request.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:327 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SrcAddr: 192.168.4.66, SrcPort: 5060, DestAddr: 192.168.4.16, DestPort: 5060, Protocol: UDP]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:327 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[Stack\-\--\>NetWork:]{lang="EN-US"}

[PRACK sip:444@192.168.4.16:5060;user=phone SIP/2.0]{lang="EN-US"}

[Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK6132dbdbd71;rport]{lang="EN-US"}

[Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66]{lang="EN-US"}

[From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c]{lang="EN-US"}

[To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D]{lang="EN-US"}

[CSeq: 2 PRACK]{lang="EN-US"}

[Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,REGISTER,INFO,PRACK,SUBSCRIBE,NOTIFY,UPDATE,REFER]{lang="EN-US"}

[Date: Thu, 23 Jan 2014 10:21:15 GMT]{lang="EN-US"}

[Max-Forwards: 70]{lang="EN-US"}

[RAck: 8 1 INVITE]{lang="EN-US"}

[Supported: timer]{lang="EN-US"}

[Content-Length: 0]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_x1551646165}*[协议栈从网络侧收到]{style="font-family:宋体"}[183]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:327 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_153355259}

[SIP EVENT: Get signalling address by global.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:328 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TPT\] Start Timer, Group id = 2, Index = 412, Duration = 30000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:328 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Start Timer, Group id = 3, Index = 51, Duration = 500.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:328 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Start Timer, Group id = 4, Index = 51, Duration = 32000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP STACK: ]{lang="EN-US"}

[  SIP STACK DEBUG LOG: Component = User Agent]{lang="EN-US"}

[  Additional Code: 2404-2547 ]{lang="EN-US"}

[  Additional Info: Invalid Paramter(s)  ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_EXIST_SDP_BODY in state STATE_CALL_ORIGINATING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Codec negotiated result is voice update.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Audio media take different media ip address or port.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Receive Response: The Status Code = 183.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:330 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SIP \--\> CMC : ACCP_ALERTING.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_624885172}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_ALERTING]{lang="EN-US"}[消息，通知对方已振铃]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:331 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_x235496458}

[SIP EVENT: SIP \--\> CMC : ACCP_CHANNEL_READY.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_1236072800}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_CHANNEL_READY]{lang="EN-US"}[消息，准备建立媒体通道]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:15:332 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_x1365674515}

[SIP EVENT: SrcAddr: 192.168.4.16, SrcPort: 64135, DestAddr: 192.168.4.66, DestPort: 5060, Protocol: UDP]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:332 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[NetWork\-\--\>Stack:]{lang="EN-US"}

[SIP/2.0 200 OK]{lang="EN-US"}

[Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK6132dbdbd71;rport]{lang="EN-US"}

[From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c]{lang="EN-US"}

[To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D]{lang="EN-US"}

[Date: Thu, 23 Jan 2014 02:25:36 GMT]{lang="EN-US"}

[Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66]{lang="EN-US"}

[Server: Cisco-SIPGateway/IOS-15.2.4.M2]{lang="EN-US"}

[CSeq: 2 PRACK]{lang="EN-US"}

[Content-Length: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:332 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Stop Timer, Group id = 4, Index = 51.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:333 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Stop Timer, Group id = 3, Index = 51.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Stack \--\> Adapter : Ssn Response.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Stack \--\> Adapter : Prack Response.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Receive Prack Response: The Status Code = 200.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Start Timer, Group id = 3, Index = 51, Duration = 5000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TPT\] Stop Timer, Group id = 2, Index = 412.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:335 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: CMC \--\> SIP : ACCP_CHANNEL_READY_ACK.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:15:335 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SIP \--\> CMC : ACCP_INFORMATION.]{lang="EN-US"}

[   Disable Outband Sip]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:093 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SrcAddr: 192.168.4.16, SrcPort: 64135, DestAddr: 192.168.4.66, DestPort: 5060, Protocol: UDP]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:093 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[NetWork\-\--\>Stack:]{lang="EN-US"}

[SIP/2.0 200 OK]{lang="EN-US"}

[Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK607a839c51b]{lang="EN-US"}

[From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c]{lang="EN-US"}

[To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D]{lang="EN-US"}

[Date: Thu, 23 Jan 2014 02:25:36 GMT]{lang="EN-US"}

[Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66]{lang="EN-US"}

[CSeq: 1 INVITE]{lang="EN-US"}

[Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER]{lang="EN-US"}

[Allow-Events: telephone-event]{lang="EN-US"}

[Remote-Party-ID: \<sip:444@192.168.4.16\>;party=called;screen=no;privacy=off]{lang="EN-US"}

[Contact: \<sip:444@192.168.4.16:5060\>]{lang="EN-US"}

[Supported: replaces]{lang="EN-US"}

[Supported: sdp-anat]{lang="EN-US"}

[Server: Cisco-SIPGateway/IOS-15.2.4.M2]{lang="EN-US"}

[Supported: timer]{lang="EN-US"}

[Content-Type: application/sdp]{lang="EN-US"}

[Content-Disposition: session;handling=required]{lang="EN-US"}

[Content-Length: 191]{lang="EN-US"}

[ ]{lang="EN-US"}

[v=0]{lang="EN-US"}

[o=CiscoSystemsSIP-GW-UserAgent 2464 7928 IN IP4 192.168.4.16]{lang="EN-US"}

[s=SIP Call]{lang="EN-US"}

[c=IN IP4 192.168.4.16]{lang="EN-US"}

[t=0 0]{lang="EN-US"}

[m=audio 20306 RTP/AVP 8]{lang="EN-US"}

[c=IN IP4 192.168.4.16]{lang="EN-US"}

[a=rtpmap:8 PCMA/8000]{lang="EN-US"}

[a=ptim]{lang="EN-US"}

[\*Jan 23 10:21:17:093 2014 Sysname SIP/7/SIPDBG: continuing\...]{lang="EN-US"}

[e:20]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_1284430691}*[协议栈从网络侧收到]{style="font-family:宋体"}[200ok]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:17:093 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_x1508673803}

[SIP TIMER: \[SIP_COMP_UA\] Stop Timer, Group id = 5, Index = 1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Start Timer, Group id = 5, Index = 1, Duration = 64000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Stop Timer, Group id = 9, Index = 1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Start Timer, Group id = 9, Index = 1, Duration = 600000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Stack \--\> Adapter : Connect Indication.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_x1677633992}*[协议栈向适配层上报]{style="font-family:宋体"}[Connect]{lang="EN-US"}[指令]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_200409426}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_SIP_CONNECT in state STATE_CALL_ORIGINATING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_EXIST_SIP_BODY in state STATE_CALL_ORIGINATING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:095 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Codec negotiated result is voice update.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:095 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP FSM: \[SIP_CALL\]\[1\]: Process the event of EVENT_OFFERMODE_PROC in state STATE_CALL_ORIGINATING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:095 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SIP \--\> CMC : ACCP_CONNECT.]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_1915087323}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_ALERTING]{lang="EN-US"}[消息，通知对方已摘机]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:17:097 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_x1141409342}

[SIP INFO: Get address from GigabitEthernet0/0(192.168.4.66).]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:097 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: Adapter \--\> Stack : Connect Ack Request.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:097 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP EVENT: SrcAddr: 192.168.4.66, SrcPort: 5060, DestAddr: 192.168.4.16, DestPort: 5060, Protocol: UDP]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[Stack\-\--\>NetWork:]{lang="EN-US"}

[ACK sip:444@192.168.4.16:5060;user=phone SIP/2.0]{lang="EN-US"}

[Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bKf608efafee9]{lang="EN-US"}

[Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66]{lang="EN-US"}

[From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c]{lang="EN-US"}

[To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D]{lang="EN-US"}

[CSeq: 1 ACK]{lang="EN-US"}

[Date: Thu, 23 Jan 2014 10:21:17 GMT]{lang="EN-US"}

[Max-Forwards: 70]{lang="EN-US"}

[Content-Length: 0]{lang="EN-US"}

[*[// SIP]{lang="EN-US"}*]{#struct_0_44918_15685_x40780428}*[协议栈向网络侧发送]{style="font-family:宋体"}[200ok]{lang="EN-US"}[的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，呼叫建立成功]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}]{#struct_0_44918_15685_x1009509691}

[SIP EVENT: Get signalling address by global.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TPT\] Start Timer, Group id = 2, Index = 413, Duration = 30000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Stop Timer, Group id = 5, Index = 1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Stop Timer, Group id = 9, Index = 1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_UA\] Start Timer, Group id = 9, Index = 1, Duration = 1800000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:099 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP TIMER: \[SIP_COMP_TXN\] Stop Timer, Group id = 4, Index = 50.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 23 10:21:17:099 2014 Sysname SIP/7/SIPDBG: ]{lang="EN-US"}

[SIP STACK: ]{lang="EN-US"}

[  SIP STACK INFORMATIONAL LOG: Component = Transaction]{lang="EN-US"}

[  Additional Code: 1100-441 ]{lang="EN-US"}

[  Additional Info: Transaction block is destroyed   ]{lang="EN-US"}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}
