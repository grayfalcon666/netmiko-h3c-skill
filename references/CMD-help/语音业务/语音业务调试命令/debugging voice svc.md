::: {#121635035 .myid}
[]{#_Toc404794473}[]{#struct_0_10834_51625_x135634702}[]{#_Toc375832081}

**语音业务 \-- 语音业务调试命令 \-- debugging voice svc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_10834_51625_x1933438871}

[**[debugging voice svc ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_10834_51625_x1379044815}

[**[undo debugging voice svc]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_10834_51625_x1409170439}

[[【视图】]{style="font-family:黑体"}]{#struct_0_10834_51625_504943788}

[[用户视图]{style="font-family:宋体"}]{#struct_0_10834_51625_1839852615}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_10834_51625_x359400120}

[[network-admin]{lang="EN-US"}]{#struct_0_10834_51625_x311889269}

[[mdc-admin]{lang="EN-US"}]{#struct_0_10834_51625_x817036452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_10834_51625_x1053639958}

[**[all]{lang="EN-US"}**]{#struct_0_10834_51625_x1097738637}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SVC]{lang="EN-US"}[（语音业务）]{style="font-family:宋体"}[所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_10834_51625_x2096150306}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SVC]{lang="EN-US"}[（语音业务）]{style="font-family:宋体"}[的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_10834_51625_2095568559}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SVC]{lang="EN-US"}[（语音业务）的]{style="font-family:宋体"}[事件类消息调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_10834_51625_x1605392518}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SVC]{lang="EN-US"}[（语音业务）的状态机类消息调试信息开关。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_10834_51625_1723881720}[：表示]{style="font-family:宋体"}[SVC]{lang="EN-US"}[（语音业务）的信息类消息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_10834_51625_375891828}[：表示]{style="font-family:宋体"}[SVC]{lang="EN-US"}[（语音业务）的定时器消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_10834_51625_925876311}

[**[debugging voice svc]{lang="EN-US"}**]{#struct_0_10834_51625_x107944728}[命令用来打开]{style="font-family:宋体"}[SVC]{lang="EN-US"}[（语音业务）]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice svc]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SVC]{lang="EN-US"}[（语音业务）]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SVC]{lang="EN-US"}]{#struct_0_10834_51625_x336083919}[（语音业务）调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#OLE_LINK25}[[表1-1 ]{lang="EN-US"}[debugging voice svc error]{lang="EN-US"}]{#struct_0_10834_51625_153507401}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_80112438}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_10834_51625_x1017429329}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10834_51625_x1172652288}

[[\[*service_type*\]: Failed to allocate memory for CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_1309914366}

[[为控制块分配内存失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_1649997105}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_1826487207}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CB]{lang="EN-US"}]{#struct_0_10834_51625_x1858158911}[：表示呼叫备份业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CFO]{lang="EN-US"}]{#struct_0_10834_51625_x1036088435}[：表示呼叫前转业务发起方]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CH]{lang="EN-US"}]{#struct_0_10834_51625_x554662941}[：表示呼叫保持业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CONF]{lang="EN-US"}]{#struct_0_10834_51625_x106296936}[：表示三方会议业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CTO]{lang="EN-US"}]{#struct_0_10834_51625_1996937715}[：表示网关的呼叫转接发起方业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CTR]{lang="EN-US"}]{#struct_0_10834_51625_2032913442}[：表示网关的呼叫转接接收方业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CTT]{lang="EN-US"}]{#struct_0_10834_51625_x1588691992}[：表示网关的呼叫转接目的方业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CW]{lang="EN-US"}]{#struct_0_10834_51625_x1290307176}[：表示呼叫等待业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FORWARD]{lang="EN-US"}]{#struct_0_10834_51625_x796790590}[：表示]{style="font-family:
  宋体"}[TG]{lang="EN-US"}[的呼叫前转业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MCH]{lang="EN-US"}]{#struct_0_10834_51625_x1997593010}[：表示多方保持业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MOH]{lang="EN-US"}]{#struct_0_10834_51625_x258820250}[：表示音乐保持业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TRANS]{lang="EN-US"}]{#struct_0_10834_51625_x2120746882}[：表示]{style="font-family:宋体"}[TG]{lang="EN-US"}[的呼叫转接业务]{style="font-family:宋体"}

[[\[*service_type*\]: Failed to send router message to DPL]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1452614408}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x992036393}[类型的业务向路由查询模块发送路由消息失败]{style="font-size:9.0pt;font-family:
  宋体"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x833810834}[取值同上。]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[*service_type*\]:  Failed to get CCB by index.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_500163352}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x1303994609}[类型的业务根据索引获取控制块失败]{style="font-size:9.0pt;font-family:
  宋体"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x1738212685}[取值同上。]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[*service_type*\]:  Received an invalid intramural message.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_728256616}

[]{#OLE_LINK20}[]{#OLE_LINK19}[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_1332823685}[类型的业务收到一个无效的内部消息]{style="font-size:9.0pt;font-family:
  宋体"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x198498117}[取值同上]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[*service_type*\]:  Failed to send ACCP_RELEASE message to SPL.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x2126479028}

[]{#OLE_LINK24}[]{#OLE_LINK23}[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x287409405}[类型的业务向协议侧发送]{style="font-size:9.0pt;font-family:
  宋体"}[ACCP_RELEASE]{lang="EN-US" style="font-size:9.0pt"}[消息失败。]{style="font-size:9.0pt;font-family:宋体"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_766579885}[取值同上]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[*service_type*\]: Failed to get CCB from leg.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_1890030755}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_707221680}[类型的业务从]{style="font-size:9.0pt;font-family:
  宋体"}[leg]{lang="EN-US" style="font-size:9.0pt"}[上获取控制块失败。]{style="font-size:9.0pt;font-family:宋体"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_2137380577}[取值同上]{style="font-size:9.0pt;font-family:
  宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging voice svc event]{lang="EN-US"}]{#struct_0_10834_51625_x1266677772}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_82348066}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_10834_51625_x1046325322}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10834_51625_x1764582058}

[[\[CW\]: Trigger CW service by INTRA_START message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x2103530261}

[[INTRA_START]{lang="EN-US"}]{#struct_0_10834_51625_300499203}[消息触发了]{style="font-family:宋体"}[CW]{lang="EN-US"}[业务]{style="font-family:宋体"}

[[\[CB\]: Trigger CB service by ACCP_RELEASE.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1190973170}

[[ACCP_RELEASE]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_1356256516}[消息触发了]{style="font-size:9.0pt;font-family:宋体"}[CB]{lang="EN-US" style="font-size:9.0pt"}[业务]{style="font-size:9.0pt;
  font-family:宋体"}

[[\[*service_type*\]:Succeed in starting *service_type* service on call leg.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_262039984}

[[成功在呼叫]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_281493546}[leg]{lang="EN-US" style="font-size:9.0pt"}[上启动]{style="font-size:9.0pt;font-family:宋体"}*[service_type]{lang="EN-US" style="font-size:9.0pt"}*[类型的业务]{style="font-size:9.0pt;
  font-family:宋体"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x2143070938}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CB]{lang="EN-US"}]{#struct_0_10834_51625_x969246103}[：表示呼叫备份业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CFO]{lang="EN-US"}]{#struct_0_10834_51625_x2073174972}[：表示呼叫前转业务发起方]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CH]{lang="EN-US"}]{#struct_0_10834_51625_x1209255235}[：表示呼叫保持业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CONF]{lang="EN-US"}]{#struct_0_10834_51625_x1319936342}[：表示三方会议业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[CTO]{lang="EN-US"}]{#struct_0_10834_51625_964301297}[：表示网关的呼叫转接发起方业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CTR]{lang="EN-US"}]{#struct_0_10834_51625_x1223329746}[：表示网关的呼叫转接接收方业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CTT]{lang="EN-US"}]{#struct_0_10834_51625_x1014400889}[：表示网关的呼叫转接目的方业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CW]{lang="EN-US"}]{#struct_0_10834_51625_1635634904}[：表示呼叫等待业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FORWARD]{lang="EN-US"}]{#struct_0_10834_51625_x528530836}[：表示]{style="font-family:
  宋体"}[TG]{lang="EN-US"}[的呼叫前转业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MCH]{lang="EN-US"}]{#struct_0_10834_51625_1605304633}[：表示多方保持业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MOH]{lang="EN-US"}]{#struct_0_10834_51625_x476383627}[：表示音乐保持业务]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[TRANS]{lang="EN-US"}]{#struct_0_10834_51625_x13732165}[：表示]{style="font-family:宋体"}[TG]{lang="EN-US"}[的呼叫转接业务]{style="font-family:宋体"}

[[\[*service_type*\]:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x2020971108}[  ]{lang="EN-US" style="font-size:
  9.0pt"}[CMC \--\> DPL : *MsgType*.]{lang="EN-US" style="font-size:9.0pt"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_1849767815}[类型的业务]{style="font-size:9.0pt;font-family:
  宋体"}[,CMC]{lang="EN-US" style="font-size:9.0pt"}[模块向]{style="font-size:9.0pt;font-family:宋体"}[DPL]{lang="EN-US" style="font-size:9.0pt"}[模块发送]{style="font-size:9.0pt;font-family:
  宋体"}*[MsgType]{lang="EN-US" style="font-size:9.0pt"}*[类型的消息]{style="font-size:9.0pt;font-family:宋体"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x601782644}[取值同上]{style="font-size:9.0pt;font-family:
  宋体"}

[*[MsgType]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x1758656430}[取值：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DPL_ROUTE_REQ]{lang="EN-US"}]{#struct_0_10834_51625_1038611388}[：路由查询消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DPL_NEXTENT_REQ]{lang="EN-US"}]{#struct_0_10834_51625_2127100711}[：查询下一个路由消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DPL_CHANGE_CALLINFO_REQ]{lang="EN-US"}]{#struct_0_10834_51625_1359161085}[：改变呼叫信息的请求消息]{style="font-family:宋体"}

[[\[CH\]: Succeed in starting the timer for waiting ACCP_MODIFY_RSP.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x697454513}

[[呼叫保持业务，成功启动定时器去等待]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_x594282351}[ACCP_MODIFY_RSP]{lang="EN-US" style="font-size:9.0pt"}[消息。]{style="font-size:9.0pt;
  font-family:宋体"}

[[\[*service_type*\]: Succeed in creating a new leg.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x171951031}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_2036764232}[类型的业务]{style="font-size:9.0pt;font-family:
  宋体"}[,]{lang="EN-US" style="font-size:9.0pt"}[成功创建一个新的]{style="font-size:9.0pt;font-family:宋体"}[leg]{lang="EN-US" style="font-size:9.0pt"}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x676579824}[取值同上]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[*service_type*\]: Succeed in deleting *TimerType* timer; TimerId: *ulTimerID*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_x22157074}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_1382154557}[类型的业务，成功删除]{style="font-size:9.0pt;font-family:
  宋体"}*[TimerType]{lang="EN-US" style="font-size:9.0pt"}*[类型的定时器，定时器]{style="font-size:9.0pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:
  宋体"}*[ulTimerID]{lang="EN-US" style="font-size:9.0pt"}*

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_561016770}[取值同上]{style="font-size:9.0pt;font-family:
  宋体"}

[*[TimerType]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_x34314084}[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[WAIT_ALERTING]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1934683961}[：等待]{style="font-size:9.0pt;font-family:宋体"}[ALERTING]{lang="EN-US" style="font-size:9.0pt"}[消息定时器]{style="font-size:
  9.0pt;font-family:宋体"}

[[SEND_ALERTING]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1619961184}[：发送]{style="font-size:9.0pt;font-family:宋体"}[ALERTING]{lang="EN-US" style="font-size:9.0pt"}[消息定时器]{style="font-size:
  9.0pt;font-family:宋体"}

[[WAIT_INFO]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x889747575}[：等待]{style="font-size:9.0pt;font-family:宋体"}[INFO]{lang="EN-US" style="font-size:9.0pt"}[消息定时器]{style="font-size:9.0pt;
  font-family:宋体"}

[[WAIT_NOTIFY]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_1176150749}[：等待]{style="font-size:9.0pt;font-family:宋体"}[NOTIFY]{lang="EN-US" style="font-size:9.0pt"}[消息定时器]{style="font-size:9.0pt;
  font-family:宋体"}

[[\[CH\]: CMC \--\> LGS: ACCP_INFORMATION.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x318753556}

[[CH]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x507874068}[业务中，]{style="font-size:9.0pt;font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[模块向]{style="font-size:9.0pt;
  font-family:宋体"}[LGS]{lang="EN-US" style="font-size:9.0pt"}[模块发送]{style="font-size:9.0pt;font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US" style="font-size:9.0pt"}[，该消息一般携带号码、]{style="font-size:9.0pt;
  font-family:宋体"}[NTE]{lang="EN-US" style="font-size:9.0pt"}[、]{style="font-size:9.0pt;font-family:宋体"}[DTMF]{lang="EN-US" style="font-size:9.0pt"}[等信息]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[*service_type*\]:  Succeed in removing remote call leg from new CMC CCB to old CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1005067171}

[*[service_type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_10834_51625_1572420048}[类型的业务，成功将远端]{style="font-size:9.0pt;font-family:
  宋体"}[leg]{lang="EN-US" style="font-size:9.0pt"}[从旧的控制块移动到新的控制块]{style="font-size:9.0pt;font-family:宋体"}

[[\[CTT\]: Received failure modify response.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x312134530}

[[CTT]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_267691141}[业务，收到一个失败的]{style="font-size:9.0pt;font-family:宋体"}[modify]{lang="EN-US" style="font-size:9.0pt"}[响应消息]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[CH\]: Notify another leg to start CTO service.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1678527838}

[[CH]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_1294117626}[业务中，通知另外的]{style="font-size:9.0pt;font-family:宋体"}[leg]{lang="EN-US" style="font-size:9.0pt"}[启动]{style="font-size:9.0pt;
  font-family:宋体"}[CTO]{lang="EN-US" style="font-size:9.0pt"}[业务]{style="font-size:9.0pt;font-family:宋体"}

[[\[CH\]: Succeed in restarting dial interval timer.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_1723816184}

[[CH]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_373442985}[业务中，成功重启拨号间隔定时器]{style="font-size:9.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging voice svc fsm]{lang="EN-US"}]{#struct_0_10834_51625_759250270}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_79431646}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_10834_51625_x419342995}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10834_51625_695200015}

[[\[MOH_LEG\]: Process the event of *EventType* in *StateType* state.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1205860471}

[[MOH]{lang="EN-US"}]{#struct_0_10834_51625_723527837}[业务]{style="font-family:宋体"}[leg]{lang="EN-US"}[，处理]{style="font-family:宋体"}*[EventType]{lang="EN-US"}*[类型的消息在]{style="font-family:宋体"}*[StateType]{lang="EN-US"}*[状态]{style="font-family:宋体"}

[*[EventType]{lang="EN-US"}*]{#struct_0_10834_51625_47620144}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MOH_START_MUSIC]{lang="EN-US"}]{#struct_0_10834_51625_14423512}[：开始放音事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MOH_DISCONNECT_TIMER]{lang="EN-US"}]{#struct_0_10834_51625_1858119863}[：]{style="font-family:
  宋体"}[DISCONNECT]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MOH_ACCP_SETUPACK]{lang="EN-US"}]{#struct_0_10834_51625_1253987633}[：收到]{style="font-family:宋体"}[ACCP_SETUPACK]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVEVT_MOH_ACCP_ALERTING:]{lang="EN-US"}]{#struct_0_10834_51625_x454298708}[：收到]{style="font-family:宋体"}[ACCP_ALERTING]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVEVT_MOH_ACCP_CONNECT]{lang="EN-US"}]{#struct_0_10834_51625_x554728477}[：收到]{style="font-family:宋体"}[ACCP_CONNECT]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MOH_ACCP_RELEASE]{lang="EN-US"}]{#struct_0_10834_51625_1359845252}[：收到]{style="font-family:宋体"}[ACCP_RELEASE]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MOH_INTRA_RELEASE]{lang="EN-US"}]{#struct_0_10834_51625_1658379525}[：收到]{style="font-family:宋体"}[INTRA_RELEASE]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MOH_ACCP_MODIFY]{lang="EN-US"}]{#struct_0_10834_51625_379147630}[：收到]{style="font-family:宋体"}[ACCP_MODIFY]{lang="EN-US"}[消息]{style="font-family:宋体"}

[*[StateType]{lang="EN-US"}*]{#struct_0_10834_51625_x1648018972}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_IDLE]{lang="EN-US"}]{#struct_0_10834_51625_x1419910351}[：]{style="font-family:宋体"}[MOH]{lang="EN-US"}[初始状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_MOH_WAIT_FOR_MUSIC_INVITE_RSP]{lang="EN-US"}]{#struct_0_10834_51625_x612999239}[：等待]{style="font-family:宋体"}[INVITE]{lang="EN-US"}[应答的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_MOHEP_LEG_CONNECTED]{lang="EN-US"}]{#struct_0_10834_51625_x1409940673}[：]{style="font-family:宋体"}[MOH]{lang="EN-US"}[放音已连接状态]{style="font-family:宋体"}

[[\[CW\]: Process the event of *EventType* in *StateType* state.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_1435635981}

[[CW]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_1171443162}[业务，处理]{style="font-size:9.0pt;font-family:宋体"}*[EventType]{lang="EN-US" style="font-size:9.0pt"}*[类型的消息在]{style="font-size:9.0pt;font-family:宋体"}*[StateType]{lang="EN-US" style="font-size:9.0pt"}*[状态]{style="font-size:9.0pt;
  font-family:宋体"}

[*[EventType]{lang="EN-US"}*]{#struct_0_10834_51625_867215644}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_EXTRA_START]{lang="EN-US"}]{#struct_0_10834_51625_x2120812418}[：收到外部触发启动业务的消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_INTRA_START]{lang="EN-US"}]{#struct_0_10834_51625_x1218942493}[：收到内部触发启动业务的消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_RELEASE_REMOTE]{lang="EN-US"}]{#struct_0_10834_51625_x328388596}[：远端]{style="font-family:宋体"}[leg]{lang="EN-US"}[拆线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_RELEASE_LOCAL]{lang="EN-US"}]{#struct_0_10834_51625_2134418904}[：本地]{style="font-family:宋体"}[leg]{lang="EN-US"}[拆线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_ACCP_MODIFY_REQ]{lang="EN-US"}]{#struct_0_10834_51625_1961405942}[：收到]{style="font-family:宋体"}[ACCP_MODIFY_REQ]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_SEND_ALERTING_TIMEOUT]{lang="EN-US"}]{#struct_0_10834_51625_863607371}[：发送]{style="font-family:
  宋体"}[ALERTING]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_RECV_ALERTING]{lang="EN-US"}]{#struct_0_10834_51625_x1512070339}[：收到]{style="font-family:宋体"}[ALERTING]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_WAIT_ALERTING_TIMEOUT]{lang="EN-US"}]{#struct_0_10834_51625_x185801963}[等待]{style="font-family:
  宋体"}[ALERTING]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_SEND_SETUP_TIMEOUT]{lang="EN-US"}]{#struct_0_10834_51625_1979365895}[：发送]{style="font-family:宋体"}[SETUP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[*[StateType]{lang="EN-US"}*]{#struct_0_10834_51625_x198563653}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_IDLE]{lang="EN-US"}]{#struct_0_10834_51625_x538458054}[：]{style="font-family:宋体"}[CW]{lang="EN-US"}[业务初始状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_WAIT_RELEASE]{lang="EN-US"}]{#struct_0_10834_51625_1741129583}[：等待拆除呼叫状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_WAIT_ALERTING]{lang="EN-US"}]{#struct_0_10834_51625_x986686175}[：等待]{style="font-family:宋体"}[ALERTING]{lang="EN-US"}[消息状态]{style="font-family:宋体"}

[[\[CH\]: Process the event of *EventType* in *StateType* state.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1973080477}

[[CH]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_848767487}[业务]{style="font-size:9.0pt;font-family:宋体"}[leg]{lang="EN-US" style="font-size:9.0pt"}[，处理]{style="font-size:9.0pt;font-family:
  宋体"}*[EventType]{lang="EN-US" style="font-size:9.0pt"}*[类型的消息在]{style="font-size:9.0pt;font-family:宋体"}*[StateType]{lang="EN-US" style="font-size:9.0pt"}*[状态]{style="font-size:9.0pt;
  font-family:宋体"}

[*[EventType]{lang="EN-US"}*]{#struct_0_10834_51625_x1420991700}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_CH_START]{lang="EN-US"}]{#struct_0_10834_51625_x1590847925}[：收到]{style="font-family:宋体"}[CH]{lang="EN-US"}[业务开始事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MODIFY_RSP]{lang="EN-US"}]{#struct_0_10834_51625_x1764647594}[：收到]{style="font-family:宋体"}[ACCP_MODIFY_RSP]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_RSP_TIMEOUT]{lang="EN-US"}]{#struct_0_10834_51625_1787753574}[：等待响应消息超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MODIFY_REQ]{lang="EN-US"}]{#struct_0_10834_51625_1407713902}[：收到]{style="font-family:宋体"}[ACCP_MODIFY_REQ]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_INTRA_INFORMATION]{lang="EN-US"}]{#struct_0_10834_51625_1511304942}[：收到]{style="font-family:宋体"}[INTRA_INFORMATION]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_INFORMATION]{lang="EN-US"}]{#struct_0_10834_51625_x495265865}[：收到]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_STARTDIAL_TIMEOUT]{lang="EN-US"}]{#struct_0_10834_51625_x1876262066}[：首次拨号定时器超时]{style="font-family:宋体"}

[*[StateType]{lang="EN-US"}*]{#struct_0_10834_51625_x681326000}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_IDLE]{lang="EN-US"}]{#struct_0_10834_51625_964235761}[：]{style="font-family:宋体"}[CH]{lang="EN-US"}[业务初始状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_CH_WAIT_RSP]{lang="EN-US"}]{#struct_0_10834_51625_1890261752}[：等待应答状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_CH]{lang="EN-US"}]{#struct_0_10834_51625_x2034768809}[：正在呼叫保持状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_CUH_WAIT_RSP]{lang="EN-US"}]{#struct_0_10834_51625_x1554915634}[：等待保持恢复应答的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_WAIT_ROUTE_RSP]{lang="EN-US"}]{#struct_0_10834_51625_x2127156628}[：等待路由应答的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_CH_WAIT_BCT]{lang="EN-US"}]{#struct_0_10834_51625_x1945288408}[：等待启动无通知呼叫转接的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_CH_WAIT_CONNECT]{lang="EN-US"}]{#struct_0_10834_51625_1124436667}[：等待新呼叫连接的状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_CH_WAIT_MCH]{lang="EN-US"}]{#struct_0_10834_51625_x1284421084}[：准备进入]{style="font-family:宋体"}[MCH]{lang="EN-US"}[的状态]{style="font-family:宋体"}

[[\[CTT\]: Process the event of *EventType* in *StateType* state.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x601848180}

[[CTT]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_2131531461}[业务]{style="font-size:9.0pt;font-family:宋体"}[leg]{lang="EN-US" style="font-size:9.0pt"}[，处理]{style="font-size:9.0pt;
  font-family:宋体"}*[EventType]{lang="EN-US" style="font-size:9.0pt"}*[类型的消息在]{style="font-size:9.0pt;font-family:宋体"}*[StateType]{lang="EN-US" style="font-size:9.0pt"}*[状态]{style="font-size:9.0pt;
  font-family:宋体"}

[*[EventType]{lang="EN-US"}*]{#struct_0_10834_51625_1849725988}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_CTT_START]{lang="EN-US"}]{#struct_0_10834_51625_1160963484}[：收到]{style="font-family:宋体"}[CTT]{lang="EN-US"}[业务启动的事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_MODIFY_RSP]{lang="EN-US"}]{#struct_0_10834_51625_1520742526}[：收到]{style="font-family:宋体"}[ACCP_MODIFY_RSP]{lang="EN-US"}[消息的事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_CTT_ACCP_RELEASE]{lang="EN-US"}]{#struct_0_10834_51625_2127035175}[：收到]{style="font-family:宋体"}[ACCP\_ RELEASE]{lang="EN-US"}[消息的事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVENT_CTT_ACCP_CONNECTACK]{lang="EN-US"}]{#struct_0_10834_51625_x1387411051}[：收到]{style="font-family:宋体"}[ACCP\_ CONNECTACK]{lang="EN-US"}[消息的事件]{style="font-family:宋体"}

[*[StateType]{lang="EN-US"}*]{#struct_0_10834_51625_x1905041359}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_IDLE]{lang="EN-US"}]{#struct_0_10834_51625_x968176715}[：]{style="font-family:宋体"}[CTT]{lang="EN-US"}[业务初始状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATE_CTT_WAIT_RSP]{lang="EN-US"}]{#struct_0_10834_51625_679205988}[：等待响应消息状态]{style="font-family:宋体"}

[[\[TRANS\]: Received a successful route response message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1685904964}

[[TG]{lang="EN-US"}]{#struct_0_10834_51625_560951234}[的呼叫转接业务，收到一个成功的路由应答消息]{style="font-family:宋体"}

[[\[TRANS\]: Send ACCP_SERVICE_ACK message to SIP.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1908332008}

[[TG]{lang="EN-US"}]{#struct_0_10834_51625_x152026415}[的呼叫转接业务，向]{style="font-family:宋体"}[SIP]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_SERVICE_ACK]{lang="EN-US"}[消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging voice svc timer]{lang="EN-US"}]{#struct_0_10834_51625_297874946}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_73311434}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_10834_51625_2038304506}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10834_51625_1126118795}

[[\[CONF\]: Succeed to creating WAIT_INFO timer. TimerID = *ulTimer* duration = 5000ms]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x693446510}

[[三方会议业务，]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_x761196709}[创建]{style="font-size:9.0pt;font-family:
  宋体"}[WAIT_INFO]{lang="EN-US" style="font-size:9.0pt"}[定时器成功，]{style="font-size:9.0pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:
  宋体"}*[ulTimer]{lang="EN-US" style="font-size:9.0pt"}*[，时长为]{style="font-size:9.0pt;font-family:宋体"}[5000]{lang="EN-US" style="font-size:9.0pt"}[毫秒]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[CTO\]: Succeed in stopping the timer for waiting CTT connect.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x468657054}

[[网关的呼叫转接发起方业务，成功停止等待转接目的方连接的定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_1652183494}

[[\[CTO\]: Succeed in deleting the timer for waiting CTT release.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1005132707}

[[网关的呼叫转接发起方业务，成功删除等待转接目的方拆线的定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_142559393}

[[\[CW\]: Succeed in starting send ACCP_SETPUP timer; TimerID = *ulTimer* duration = 500ms. \"]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_211718413}

[[呼叫等待业务，成功创建发送]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_2102577836}[ACCP_SETUP]{lang="EN-US" style="font-size:
  9.0pt"}[消息定时器，]{style="font-size:9.0pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;
  font-family:宋体"}*[ulTimer]{lang="EN-US" style="font-size:9.0pt"}*[，时长为]{style="font-size:9.0pt;font-family:宋体"}[500]{lang="EN-US" style="font-size:9.0pt"}[毫秒]{style="font-size:9.0pt;font-family:
  宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging voice svc info]{lang="EN-US"}]{#struct_0_10834_51625_1863808346}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_74789364}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_10834_51625_1372696048}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_10834_51625_x1001852829}

[[\[MOH_LEG\]: Succeed in sending ACCP_SETUP message to music server.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_91077746}

[[音乐保持业务]{style="font-family:宋体"}]{#struct_0_10834_51625_1811474304}[leg]{lang="EN-US"}[，成功向音乐服务器发送]{style="font-family:宋体"}[ACCP_SETUP]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[\[CB\]: Succeed in saving dial-peer information.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1892493555}

[[保存拨号信息成功]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_x212705242}

[[\[CFO\]: Trigger CFU service by DPL_ROUTE_RSP message.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_862728333}

[[呼叫前转业务，]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_1723750648}[DPL_ROUTE_RSP]{lang="EN-US" style="font-size:9.0pt"}[消息触发]{style="font-size:9.0pt;font-family:宋体"}[CFU]{lang="EN-US" style="font-size:9.0pt"}[业务]{style="font-size:9.0pt;font-family:
  宋体"}

[[\[CFO\]: Forward number is too many.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_x45075590}

[[呼叫前转业务，太多的前转号码]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_x34165851}

[[\[CH\]: Failed to match entity.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_872592999}

[[匹配实体失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_x936548357}

[[\[CONF\]: Succeed in sending channel update message to local leg.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_10834_51625_340559697}

[[成功向本地]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_10834_51625_2060125442}[leg]{lang="EN-US" style="font-size:9.0pt"}[发送媒体通道更新消息]{style="font-size:9.0pt;font-family:宋体"}

[[\[FORWARD\]: This is the *n*th CF service messages are received,  and the contact header contain *num* address.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_10834_51625_x1401778707}

[[这是收到的第]{style="font-size:9.0pt;font-family:
  宋体"}]{#struct_0_10834_51625_52643253}*[n]{lang="EN-US" style="font-size:9.0pt"}*[个]{style="font-size:9.0pt;font-family:宋体"}[CF]{lang="EN-US" style="font-size:9.0pt"}[业务消息，并且]{style="font-size:9.0pt;font-family:
  宋体"}[contact]{lang="EN-US" style="font-size:9.0pt"}[头里面包含]{style="font-size:9.0pt;font-family:宋体"}*[num]{lang="EN-US" style="font-size:9.0pt"}*[个地址]{style="font-size:9.0pt;
  font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_10834_51625_1452313237}

[[\# ]{lang="EN-US"}]{#struct_0_10834_51625_960218982}[本地]{style="font-family:宋体"}[LGS]{lang="EN-US"}[通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[网络建立了呼叫，本端话机拍叉发起呼叫保持。保持成功后再拍叉恢复呼叫。打开主叫侧]{style="font-family:宋体"}[SVC]{lang="EN-US"}[所有类型的调试信息输出开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging voice svc all]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_829446983}

[[\<Sysname\>\*Jan 15 14:40:08:535 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x554794013}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_CH_START in state STATE_IDLE.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x2112937922}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_x1932669924}*[呼叫保持业务在初始状态下处理业务开始事件，]{style="font-family:宋体"}[32]{lang="EN-US"}[是]{style="font-family:宋体"}[CH]{lang="EN-US"}[的控制块索引，用来唯一标示这个业务]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:535 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_238253101}

[[SVC EVENT: \[CH\]: Succeed in starting the timer for waiting ACCP_MODIFY_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_348315566}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_x370362914}*[呼叫保持业务成功启动定时器等待]{style="font-family:宋体"}[ACCP_MODIFY_RSP]{lang="EN-US"}[回应]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_1535699797}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_MODIFY_RSP in state STATE_CH_WAIT_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_2009416990}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_1991442716}*[呼叫保持业务在]{style="font-family:宋体"}[STATE_CH_WAIT_RSP]{lang="EN-US"}[状态下处理]{style="font-family:宋体"}[EVENT_MODIFY_RSP]{lang="EN-US"}[事件，也就是收到了]{style="font-family:宋体"}[ACCP_MODIFY_RSP]{lang="EN-US"}[回应]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_491679474}

[[SVC EVENT: \[CH\]: Succeed in stopping the timer for waiting ACCP_MODIFY_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x912866569}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_x249971627}*[呼叫保持业务停止等待]{style="font-family:宋体"}[ACCP_MODIFY_RSP]{lang="EN-US"}[回应的定时器]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1021737396}

[[SVC EVENT: \[CH\]: Received successful modify response.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_1817695134}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_122774193}*[呼叫保持业务收到的是成功的]{style="font-family:宋体"}[ACCP_MODIFY_RSP]{lang="EN-US"}[回应]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1770346467}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_REQ_SUCCESS in state STATE_CH_WAIT_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_2067556374}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x2120877954}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_NOT_EXIST_CW in state STATE_CH_WAIT_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_513802896}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_1598269677}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_MCH_NOT_REQ in state STATE_CH_WAIT_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x311426}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_1055776022}

[[SVC EVENT: \[CH\]: Succeed in starting the timer for first dial.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1990104816}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_x1489737400}*[呼叫保持业务启动首次拨号定时器，等待用户拨号]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:08:543 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_817486629}

[[SVC EVENT: \[CH\]: CMC \--\> LGS: ACCP_INFORMATION.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x959050957}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_1850929568}*[呼叫保持业务中向]{style="font-family:宋体"}[LGS]{lang="EN-US"}[模块发送]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息用来打开]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[检测，也就是检测用户按键。至此，呼叫保持成功]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_MODIFY_REQ in state STATE_CH.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x113159127}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_1168966229}*[在]{style="font-family:宋体"}[STATE_CH]{lang="EN-US"}[状态下处理]{style="font-family:宋体"}[EVENT_MODIFY_REQ]{lang="EN-US"}[事件，也就是在呼叫保持状态下收到了保持恢复的请求]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:845 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1394471355}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_RECV_MODIFYREQ_LEG_NOT_DELETED in state STATE_CH.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_716864941}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_1395394786}*[在]{style="font-family:宋体"}[STATE_CH]{lang="EN-US"}[状态下处理]{style="font-family:宋体"}[EVENT_RECV_MODIFYREQ_LEG_NOT_DELETED]{lang="EN-US"}[事件，用来判断被保持的那一侧是否已经挂机]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:845 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_1096821556}

[[SVC EVENT: \[CH\]: Succeed in deleting first dial timer.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_191619853}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_x198629189}*[成功删除首次拨号定时器，当定时器存在的时候才会执行]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:845 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x533197572}

[[SVC EVENT: \[CH\]: Succeed in starting the timer for waiting ACCP_MODIFY_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x159415237}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_1786293123}*[启动定时器等待]{style="font-family:宋体"}[ACCP_MODIFY_RSP]{lang="EN-US"}[，也就是保持恢复请求的响应消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_1794638614}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_MODIFY_RSP in state STATE_CUH_WAIT_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1068977261}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_1825299914}*[收到响应消息，进入状态机处理]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_227757460}

[[SVC EVENT: \[CH\]: Succeed in stopping the timer for waiting ACCP_MODIFY_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1765541099}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x2116922859}

[[SVC EVENT: \[CH\]: Received successful modify response.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1344753419}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_773055742}*[呼叫保持业务收到的是成功的]{style="font-family:宋体"}[ACCP_MODIFY_RSP]{lang="EN-US"}[回应]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x537158338}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_REQ_SUCCESS in state STATE_CUH_WAIT_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x794720536}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_2014455364}

[[SVC FSM: \[CH\]\[32\]: Process the event of EVENT_MCH_NOT_REQ in state STATE_CUH_WAIT_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1458284809}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Jan 15 14:40:13:853 2014 Sysname CMC/7/CMCDBG: ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x1764713130}

[[SVC EVENT: \[CH\]: CMC \--\> LGS: ACCP_INFORMATION.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_10834_51625_x727488849}

[*[// ]{lang="EN-US"}*]{#struct_0_10834_51625_2023990835}*[呼叫保持业务中向]{style="font-family:宋体"}[LGS]{lang="EN-US"}[模块发送]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息用来关闭]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[检测。至此，呼叫保持业务结束，恢复到正常的呼叫]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
