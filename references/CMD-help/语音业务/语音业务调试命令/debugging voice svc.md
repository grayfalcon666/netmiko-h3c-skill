
**语音业务 \-- 语音业务调试命令 \-- debugging voice svc**

------------------------------------------------------------------------

【命令】

**[debugging voice svc **[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

**[undo debugging voice svc**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示SVC（语音业务）所有消息类型的调试信息开关。

**[error**]：表示SVC（语音业务）的错误类型的消息调试信息开关。

**[event**]：表示SVC（语音业务）的事件类消息调试信息开关。

**[fsm**]：表示SVC（语音业务）的状态机类消息调试信息开关。

**[info**]：表示SVC（语音业务）的信息类消息调试信息开关。

**[timer**]：表示SVC（语音业务）的定时器消息调试信息开关。

【描述】

**[debugging voice svc**]命令用来打开SVC（语音业务）调试信息开关。**undo debugging voice svc**命令用来关闭SVC（语音业务）调试信息开关。

缺省情况下，SVC（语音业务）调试信息开关处于关闭状态。

表1-1 debugging voice svc error令输出信息描述表

字段

描述

*service_type*: Failed to allocate memory for CCB.

为控制块分配内存失败

*[service_type*]取值为：

·CB：表示呼叫备份业务

·CFO：表示呼叫前转业务发起方

·CH：表示呼叫保持业务

·CONF：表示三方会议业务

·CTO：表示网关的呼叫转接发起方业务

·CTR：表示网关的呼叫转接接收方业务

·CTT：表示网关的呼叫转接目的方业务

·CW：表示呼叫等待业务

·FORWARD：表示TG的呼叫前转业务

·MCH：表示多方保持业务

·MOH：表示音乐保持业务

·TRANS：表示TG的呼叫转接业务

*service_type*: Failed to send router message to DPL

*[service_type*]类型的业务向路由查询模块发送路由消息失败

*[service_type*]取值同上。

*service_type*:  Failed to get CCB by index.

*[service_type*]类型的业务根据索引获取控制块失败

*[service_type*]取值同上。

*service_type*:  Received an invalid intramural message.

*[service_type*]类型的业务收到一个无效的内部消息

*[service_type*]取值同上

*service_type*:  Failed to send ACCP_RELEASE message to SPL.

*[service_type*]类型的业务向协议侧发送ACCP_RELEASE消息失败。

*[service_type*]取值同上

*service_type*: Failed to get CCB from leg.

*[service_type*]类型的业务从leg上获取控制块失败。

*[service_type*]取值同上

表1-2 debugging voice svc event令输出信息描述表

字段

描述

CW: Trigger CW service by INTRA_START message.

INTRA_START消息触发了CW业务

CB: Trigger CB service by ACCP_RELEASE.

ACCP_RELEASE消息触发了CB业务

*service_type*:Succeed in starting *service_type* service on call leg.

成功在呼叫leg上启动*service_type*类型的业务

*[service_type*]取值为：

·CB：表示呼叫备份业务

·CFO：表示呼叫前转业务发起方

·CH：表示呼叫保持业务

·CONF：表示三方会议业务

·CTO：表示网关的呼叫转接发起方业务

·CTR：表示网关的呼叫转接接收方业务

·CTT：表示网关的呼叫转接目的方业务

·CW：表示呼叫等待业务

·FORWARD：表示TG的呼叫前转业务

·MCH：表示多方保持业务

·MOH：表示音乐保持业务

·TRANS：表示TG的呼叫转接业务

*service_type*:CMC \--\> DPL : *MsgType*.

*[service_type*]类型的业务,CMC模块向DPL模块发送*MsgType*类型的消息

*[service_type*]取值同上

*[MsgType*]取值：

·DPL_ROUTE_REQ：路由查询消息

·DPL_NEXTENT_REQ：查询下一个路由消息

·DPL_CHANGE_CALLINFO_REQ：改变呼叫信息的请求消息

CH: Succeed in starting the timer for waiting ACCP_MODIFY_RSP.

呼叫保持业务，成功启动定时器去等待ACCP_MODIFY_RSP消息。

*service_type*: Succeed in creating a new leg.

*[service_type*]类型的业务,成功创建一个新的leg

*[service_type*]取值同上

*service_type*: Succeed in deleting *TimerType* timer; TimerId: *ulTimerID*

*[service_type*]类型的业务，成功删除*TimerType*类型的定时器，定时器ID为*ulTimerID*

*[service_type*]取值同上

*[TimerType*]取值为：

WAIT_ALERTING：等待ALERTING消息定时器

SEND_ALERTING：发送ALERTING消息定时器

WAIT_INFO：等待INFO消息定时器

WAIT_NOTIFY：等待NOTIFY消息定时器

CH: CMC \--\> LGS: ACCP_INFORMATION.

CH业务中，CMC模块向LGS模块发送ACCP_INFORMATION，该消息一般携带号码、NTE、DTMF等信息

*service_type*:  Succeed in removing remote call leg from new CMC CCB to old CCB.

*[service_type*]类型的业务，成功将远端leg从旧的控制块移动到新的控制块

CTT: Received failure modify response.

CTT业务，收到一个失败的modify响应消息

CH: Notify another leg to start CTO service.

CH业务中，通知另外的leg启动CTO业务

CH: Succeed in restarting dial interval timer.

CH业务中，成功重启拨号间隔定时器

表1-3 debugging voice svc fsm令输出信息描述表

字段

描述

MOH_LEG: Process the event of *EventType* in *StateType* state.

MOH业务leg，处理*EventType*类型的消息在*StateType*状态

*[EventType*]取值为：

·EVENT_MOH_START_MUSIC：开始放音事件

·EVENT_MOH_DISCONNECT_TIMER：DISCONNECT定时器超时

·EVENT_MOH_ACCP_SETUPACK：收到ACCP_SETUPACK消息

·EVEVT_MOH_ACCP_ALERTING:：收到ACCP_ALERTING消息

·EVEVT_MOH_ACCP_CONNECT：收到ACCP_CONNECT消息

·EVENT_MOH_ACCP_RELEASE：收到ACCP_RELEASE消息

·EVENT_MOH_INTRA_RELEASE：收到INTRA_RELEASE消息

·EVENT_MOH_ACCP_MODIFY：收到ACCP_MODIFY消息

*[StateType*]取值为：

·STATE_IDLE：MOH初始状态

·STATE_MOH_WAIT_FOR_MUSIC_INVITE_RSP：等待INVITE应答的状态

·STATE_MOHEP_LEG_CONNECTED：MOH放音已连接状态

CW: Process the event of *EventType* in *StateType* state.

CW业务，处理*EventType*类型的消息在*StateType*状态

*[EventType*]取值为：

·EVENT_EXTRA_START：收到外部触发启动业务的消息

·EVENT_INTRA_START：收到内部触发启动业务的消息

·EVENT_RELEASE_REMOTE：远端leg拆线

·EVENT_RELEASE_LOCAL：本地leg拆线

·EVENT_ACCP_MODIFY_REQ：收到ACCP_MODIFY_REQ消息

·EVENT_SEND_ALERTING_TIMEOUT：发送ALERTING定时器超时

·EVENT_RECV_ALERTING：收到ALERTING消息

·EVENT_WAIT_ALERTING_TIMEOUT等待ALERTING定时器超时

·EVENT_SEND_SETUP_TIMEOUT：发送SETUP定时器超时

*[StateType*]取值为：

·STATE_IDLE：CW业务初始状态

·STATE_WAIT_RELEASE：等待拆除呼叫状态

·STATE_WAIT_ALERTING：等待ALERTING消息状态

CH: Process the event of *EventType* in *StateType* state.

CH业务leg，处理*EventType*类型的消息在*StateType*状态

*[EventType*]取值为：

·EVENT_CH_START：收到CH业务开始事件

·EVENT_MODIFY_RSP：收到ACCP_MODIFY_RSP消息

·EVENT_RSP_TIMEOUT：等待响应消息超时

·EVENT_MODIFY_REQ：收到ACCP_MODIFY_REQ消息

·EVENT_INTRA_INFORMATION：收到INTRA_INFORMATION消息

·EVENT_INFORMATION：收到ACCP_INFORMATION消息

·EVENT_STARTDIAL_TIMEOUT：首次拨号定时器超时

*[StateType*]取值为：

·STATE_IDLE：CH业务初始状态

·STATE_CH_WAIT_RSP：等待应答状态

·STATE_CH：正在呼叫保持状态

·STATE_CUH_WAIT_RSP：等待保持恢复应答的状态

·STATE_WAIT_ROUTE_RSP：等待路由应答的状态

·STATE_CH_WAIT_BCT：等待启动无通知呼叫转接的状态

·STATE_CH_WAIT_CONNECT：等待新呼叫连接的状态

·STATE_CH_WAIT_MCH：准备进入MCH的状态

CTT: Process the event of *EventType* in *StateType* state.

CTT业务leg，处理*EventType*类型的消息在*StateType*状态

*[EventType*]取值为：

·EVENT_CTT_START：收到CTT业务启动的事件

·EVENT_MODIFY_RSP：收到ACCP_MODIFY_RSP消息的事件

·EVENT_CTT_ACCP_RELEASE：收到ACCP\_ RELEASE消息的事件

·EVENT_CTT_ACCP_CONNECTACK：收到ACCP\_ CONNECTACK消息的事件

*[StateType*]取值为：

·STATE_IDLE：CTT业务初始状态

·STATE_CTT_WAIT_RSP：等待响应消息状态

TRANS: Received a successful route response message.

TG的呼叫转接业务，收到一个成功的路由应答消息

TRANS: Send ACCP_SERVICE_ACK message to SIP.

TG的呼叫转接业务，向SIP发送ACCP_SERVICE_ACK消息

表1-4 debugging voice svc timer令输出信息描述表

字段

描述

CONF: Succeed to creating WAIT_INFO timer. TimerID = *ulTimer* duration = 5000ms

三方会议业务，创建WAIT_INFO定时器成功，ID为*ulTimer*，时长为5000毫秒

CTO: Succeed in stopping the timer for waiting CTT connect.

网关的呼叫转接发起方业务，成功停止等待转接目的方连接的定时器

CTO: Succeed in deleting the timer for waiting CTT release.

网关的呼叫转接发起方业务，成功删除等待转接目的方拆线的定时器

CW: Succeed in starting send ACCP_SETPUP timer; TimerID = *ulTimer* duration = 500ms. \"

呼叫等待业务，成功创建发送ACCP_SETUP消息定时器，ID为*ulTimer*，时长为500毫秒

表1-5 debugging voice svc info令输出信息描述表

字段

描述

MOH_LEG: Succeed in sending ACCP_SETUP message to music server.

音乐保持业务leg，成功向音乐服务器发送ACCP_SETUP消息

CB: Succeed in saving dial-peer information.

保存拨号信息成功

CFO: Trigger CFU service by DPL_ROUTE_RSP message.

呼叫前转业务，DPL_ROUTE_RSP消息触发CFU业务

CFO: Forward number is too many.

呼叫前转业务，太多的前转号码

CH: Failed to match entity.

匹配实体失败

CONF: Succeed in sending channel update message to local leg.

成功向本地leg发送媒体通道更新消息

FORWARD: This is the *n*th CF service messages are received,  and the contact header contain *num* address.

这是收到的第*n*个CF业务消息，并且contact头里面包含*num*个地址

【举例】

\# 本地LGS通过IP网络建立了呼叫，本端话机拍叉发起呼叫保持。保持成功后再拍叉恢复呼叫。打开主叫侧SVC所有类型的调试信息输出开关。

\<Sysname\> debugging voice svc all

\<Sysname\>\*Jan 15 14:40:08:535 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_CH_START in state STATE_IDLE.

*// 呼叫保持业务在初始状态下处理业务开始事件，32是CH的控制块索引，用来唯一标示这个业务*

\*Jan 15 14:40:08:535 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: Succeed in starting the timer for waiting ACCP_MODIFY_RSP.

*// 呼叫保持业务成功启动定时器等待ACCP_MODIFY_RSP回应*

\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_MODIFY_RSP in state STATE_CH_WAIT_RSP.

*// 呼叫保持业务在STATE_CH_WAIT_RSP状态下处理EVENT_MODIFY_RSP事件，也就是收到了ACCP_MODIFY_RSP回应*

\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: Succeed in stopping the timer for waiting ACCP_MODIFY_RSP.

*// 呼叫保持业务停止等待ACCP_MODIFY_RSP回应的定时器*

\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: Received successful modify response.

*// 呼叫保持业务收到的是成功的ACCP_MODIFY_RSP回应*

\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_REQ_SUCCESS in state STATE_CH_WAIT_RSP.

\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_NOT_EXIST_CW in state STATE_CH_WAIT_RSP.

\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_MCH_NOT_REQ in state STATE_CH_WAIT_RSP.

\*Jan 15 14:40:08:542 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: Succeed in starting the timer for first dial.

*// 呼叫保持业务启动首次拨号定时器，等待用户拨号*

\*Jan 15 14:40:08:543 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: CMC \--\> LGS: ACCP_INFORMATION.

*// 呼叫保持业务中向LGS模块发送ACCP_INFORMATION消息用来打开DTMF检测，也就是检测用户按键。至此，呼叫保持成功*

SVC FSM: CH32: Process the event of EVENT_MODIFY_REQ in state STATE_CH.

*// 在STATE_CH状态下处理EVENT_MODIFY_REQ事件，也就是在呼叫保持状态下收到了保持恢复的请求*

\*Jan 15 14:40:13:845 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_RECV_MODIFYREQ_LEG_NOT_DELETED in state STATE_CH.

*// 在STATE_CH状态下处理EVENT_RECV_MODIFYREQ_LEG_NOT_DELETED事件，用来判断被保持的那一侧是否已经挂机*

\*Jan 15 14:40:13:845 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: Succeed in deleting first dial timer.

*// 成功删除首次拨号定时器，当定时器存在的时候才会执行*

\*Jan 15 14:40:13:845 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: Succeed in starting the timer for waiting ACCP_MODIFY_RSP.

*// 启动定时器等待ACCP_MODIFY_RSP，也就是保持恢复请求的响应消息*

\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_MODIFY_RSP in state STATE_CUH_WAIT_RSP.

*// 收到响应消息，进入状态机处理*

\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: Succeed in stopping the timer for waiting ACCP_MODIFY_RSP.

\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: Received successful modify response.

*// 呼叫保持业务收到的是成功的ACCP_MODIFY_RSP回应*

\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_REQ_SUCCESS in state STATE_CUH_WAIT_RSP.

\*Jan 15 14:40:13:852 2014 Sysname CMC/7/CMCDBG:

SVC FSM: CH32: Process the event of EVENT_MCH_NOT_REQ in state STATE_CUH_WAIT_RSP.

\*Jan 15 14:40:13:853 2014 Sysname CMC/7/CMCDBG:

SVC EVENT: CH: CMC \--\> LGS: ACCP_INFORMATION.

*// 呼叫保持业务中向LGS模块发送ACCP_INFORMATION消息用来关闭DTMF检测。至此，呼叫保持业务结束，恢复到正常的呼叫*

