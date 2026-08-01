<!-- CMD-INDEX
  debugging voice lgs                 | 用户视图             | L8
  debugging voice em                  | 用户视图             | L498
  debugging voice r2                  | 用户视图             | L1236
  debugging voice iva                 | 用户视图             | L1998
-->

**语音用户线 \-- 语音用户线调试命令 \-- debugging voice lgs**

------------------------------------------------------------------------

【命令】

**[debugging voice lgs **[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

**[undo debugging voice lgs**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示LGS所有消息类型的调试信息开关。

**[error**]：表示LGS的错误类型的消息调试信息开关。

**[event**]：表示LGS的事件类消息调试信息开关。

**[fsm**]：表示LGS的状态机类消息调试信息开关。

**[info**]：表示LGS的信息类消息调试信息开关。

**[timer**]：表示LGS的定时器消息调试信息开关。

【描述】

**[debugging voice lgs**]命令用来打开LGS调试信息开关。**undo debugging voice lgs**命令用来关闭LGS调试信息开关。

缺省情况下，LGS调试信息开关处于关闭状态。

表1-1 debugging voice lgs error令输出信息描述表

字段

描述

Failed to send *Type* message to CMC.

向CMC发送*Type*消息失败

*[Type*]为LGS发给驱动消息的类型，取值为：

·ACCP_SETUP：表示被叫给CMC发送建立新呼叫的信令

·ACCP_SETUP_ACK：表示主叫对CMC发起新呼叫的应答信令

·ACCP_RELEASE：表示主/被叫给CMC发送拆线信令

·ACCP_RELEASE_COMPLETE：表示主/被叫发送完成拆线信令

·ACCP_CONNECT：表示主叫给CMC发送通话连接信令

·ACCP_ALERTING：表示主叫给CMC发送振铃信令

·ACCP_CHANNEL_READY：表示主/被发送媒体通道准备就绪信令

·ACCP_INFORMATION：表示主/被叫发送的DTMF信令

Failed to send the *Type* command to driver.

LGS向驱动下发*Type*命令失败

*[Type*]为下发驱动的命令字类型

·VOICE_COM_INSTALL：表示下发接口占用命令字

·VOICE_COM_DTMF_DETECT_ON：表示下发开启DTMF检测命令字

·VOICE_COM_DTMF_DETECT_OFF：表示下发关闭DTMF检测命令字

·VOICE_NTE_ON：表示下发开启NTE命令字

·VOICE_FXS_ALERT_ON：表示下发开始振铃命令字

·VOICE_FXS_ALERT_OFF：表示下发关闭振铃命令字

Failed to allocate memory for CCB.

为CCB分配内存失败

Failed to get LGS private data from interface *interface*

从接口获取私有数据失败

Failed to deal with the install command.

处理install命令字失败

No local call index is available.

没有空闲的本地呼叫索引

Cannot find the CCB to be deleted.

找不到删除的CCB

Received an unexpected message.

收到一个不是预期的消息

Failed to check ACCP message which received from CMC.

从CMC收到ACCP消息检查失败

The call with call ID *call-id* already exist.

Call ID为call-id的呼叫已经存在

表1-2 debugging voice lgs event令输出信息描述表

字段

描述

 LGS \--\> CMC : *Message-type*

LGS进程向CMC进程成功发送*Message-type*消息

*[Type*]为LGS发给驱动消息的类型，取值为：

·ACCP_SETUP：表示被叫给CMC发送建立新呼叫的信令

·ACCP_SETUP_ACK：表示主叫对CMC发起新呼叫的应答信令

·ACCP_RELEASE：表示主/被叫给CMC发送拆线信令

·ACCP_RELEASE_COMPLETE：表示主/被叫发送完成拆线信令

·ACCP_CONNECT：表示主叫给CMC发送通话连接信令

·ACCP_ALERTING：表示主叫给CMC发送振铃信令

·ACCP_CHANNEL_READY：表示主/被发送媒体通道准备就绪信令

·ACCP_INFORMATION：表示主/被叫发送的DTMF信令

CMC\--\> LGS : *Message-type*

LGS进程收到CMC进程发送的*Message-type*消息

LGS \--\> DRV: *Command-type*

向驱动下发*Command-type*命令

DRV \--\> LGS: *Event-type*

LGS收到驱动上报的*Event-type*事件

Send DTMF characters *number* to driver.

发送DTMF号码给驱动

Caller number is null or exceeds the length limit.

主叫号码为空或超出长度限制

Caller name is null or exceeds the length limit.

主机名为空或超出长度限制

Send call number to CMC in *state* state.

在*state* e状态向CMC发送号码，*state*表示当前呼叫的状态

Begin to receive called number.

开始接收被叫号码

Received Event-type event from interface *index*.

从接口*index*收到驱动上报的事件类型

Inband information is unavailable. Play ring-back tone in two seconds.

带内信息不可用，两秒钟后播放回铃音

表1-3 debugging voice lgs fsm令输出信息描述表

字段

描述

State changes from *state1* to *state2*.

呼叫状态从*state1*切换到*state2*.

*[state1*]*和state2的*取值为：

·LGS_IDLE：LGS初始状态

·FXS_CALLER_INSTALLING：主叫使用的FXS语音用户线正在占用接口

·FXS_CALLER_NUM_RCVING：主叫使用的FXS语音用户线在收号

·FXS_CALLER_CONNECTING：主叫使用的FXS语音用户线正在连接呼叫

·FXS_CALLER_RING_BACK：主叫使用的FXS语音用户线在播放回铃音

·FXS_CALLER_TALKING：主叫使用的FXS语音用户线正在通话

·FXS_CALLED_INSTALLING：被叫使用的FXS语音用户线正在占用接口

·FXS_CALLED_ALERTING：被叫使用的FXS语音用户线在振铃

·FXS_CALLED_TALKING：被叫使用的FXS语音用户线在通话

·FXO_CALLER_INSTALLING：主叫使用的FXO语音用户线正在占用接口

·FXO_CALLER_NUM_RCVING：主叫使用的FXO语音用户线在收号

·FXO_CALLER_CONNECTING：主叫使用的FXO语音用户线正在连接呼叫

·FXO_CALLER_RING_BACK：主叫使用的FXO语音用户线在播放回铃音

·FXO_CALLER_TALKING：主叫使用的FXO语音用户线正在通话

·FXO_CALLED_INSTALLING：被叫使用的FXO语音用户线正在占用接口

·FXO_CALLED_TALKING：被叫使用的FXO语音用户线在通话

表1-4 debugging voice lgs info令输出信息描述表

字段

描述

 Reconnecting to HA daemon, Please wait\...

重连HA

Failed to connect to HA daemon.

连接{.TableTextChar}HA{.TableTextChar}失败{.TableTextChar}

表1-5 debugging voice lgs timer令输出信息描述表

字段

描述

 Submodel *name* init timed out, TimerID = *timerid* duration = *time-length* ms.

LGS子模块 *[name*]初始化超时，定时器ID为*timerID*，持续时间为*TimerLen*毫秒

Failed to get timer *Timer-name length*, state:State-type.

在*State-type*呼叫的状态，获取定时器时长失败

Succeed in starting the *Timer-name* timer, state: *State-typ*e, time length:*Timelengh*.

在*State-type*呼叫的状态，创建定时器*Timer-name*，持续时间为*TimerLen*毫秒

*[State-type*]取值同表1-3

Succeed in stopping the *Timer-name* timer,state:*State-type.*

在*State-type*呼叫的状态，LGS 删除定时器*Timer-name*

*[State-type*]取值同表1-3

*[Timer-name*] timer timed out in State-type state.

LGS *Timer-name*定时器在*State-type*状态下超时

*[State-type*]取值同表1-3

【举例】

\# 打开主叫侧LGS所有类型的调试信息输出开关。

\<Sysname\> debugging voice lgs all

\<Sysname\>\*Jan 20 08:59:33:731 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: DRV \--\> LGS:  VOICE_EVENT_FXS_OFF_HOOK

*[// LGS*]*收到驱动上报的摘机事件*

\*Jan 20 08:59:33:732 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 Find CCB for driver message VOICE_EVENT_FXS_OFF_HOOK ]

in LGS_IDLE state.

*// 根据事件找到相应的CCB，这时候LGS在初始IDLE状态*

\*Jan 20 08:59:33:732 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 LGS \--\> DRV: VOICE_COM_INSTALL]

*[// LGS*]*向驱动下发占用命令*

\*Jan 20 08:59:33:733 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Succeed in starting Wait_Install_ACK timer,]

state:LGS_IDLE, time length:3000ms.

*// 创建等待install_ACK的定时器，这时候状态是IDLE，定时器时长是3000ms*

\*Jan 20 08:59:33:733 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Fsm: [0x000005a3 State changes from LGS_IDLE to FXS_CALLER_INSTALLING]

*[//LGS*]*状态从LGS_IDLE转到FXS_CALLER_INSTALLING*

\*Jan 20 08:59:33:761 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: DRV \--\> LGS:  VOICE_EVENT_COM_INSTALL_ACK:  Success

*[//*]*收到驱动上报的INSTALL_ACK事件*

\*Jan 20 08:59:33:761 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 Find CCB for driver message VOICE_EVENT_COM_INSTALL_ACK ]

in FXS_CALLER_INSTALLING state.

\*Jan 20 08:59:33:761 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Succeed in stopping Wait_Install_ACK timer,]

state:FXS_CALLER_INSTALLING

\*Jan 20 08:59:33:761 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 Send play Dial tone command to driver in ]

FXS_CALLER_INSTALLING state.

*[//*]*向驱动发送播放拨号音的命令，在FXS_CALLER_INSTALLING状态下*

\*Jan 20 08:59:33:762 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 LGS \--\> DRV: VOICEL_COM_TONE_GEN_ON]

\*Jan 20 08:59:33:762 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Succeed in starting First Dial timer,]

state:FXS_CALLER_INSTALLING, time length:10000ms.

\*Jan 20 08:59:33:762 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 LGS \--\> DRV: VOICE_COM_DTMF_DETECT_ON]

\*Jan 20 08:59:33:762 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Fsm: [0x000005a3 State changes from FXS_CALLER_INSTALLING to FXS_CALLER_NUM_RCVING]

\*Jan 20 08:59:35:021 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: DRV \--\> LGS:  VOICE_EVENT_COM_DTMF_IND:  1

\*Jan 20 08:59:35:021 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 Find CCB for driver message VOICE_EVENT_COM_DTMF_IND ]

in FXS_CALLER_NUM_RCVING state.

\*Jan 20 08:59:35:021 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Succeed in stopping First Dial timer,]

state:FXS_CALLER_NUM_RCVING

*// 停止First Dial定时器，状态是FXS_CALLER_NUM_RCVING状态*

\*Jan 20 08:59:35:022 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 LGS \--\> DRV: VOICE_COM_TONE_GEN_OFF]

\*Jan 20 08:59:35:022 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: LGS \--\> CMC : ACCP_SETUP

*[// LGS*]*向CMC发送ACCP_SETUP消息*

\*Jan 20 08:59:35:023 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Succeed in starting Dial_Interval timer,]

state:FXS_CALLER_NUM_RCVING, time length:10000ms.

\*Jan 20 08:59:35:024 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Fsm: [0x000005a3 State changes from FXS_CALLER_NUM_RCVING to FXS_CALLER_PREPARE]

\*Jan 20 08:59:35:681 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: DRV \--\> LGS:  VOICE_EVENT_COM_DTMF_IND:  0

\*Jan 20 08:59:35:681 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 Find CCB for driver message VOICE_EVENT_COM_DTMF_IND ]

in FXS_CALLER_PREPARE state.

\*Jan 20 08:59:35:681 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 Send call number to CMC in FXS_CALLER_PREPARE state.]

*// 向CMC发送被叫号码，在FXS_CALLER_PREPARE状态*

\*Jan 20 08:59:35:682 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: LGS \--\> CMC : ACCP_INFORMATION

*[// LGS*]*向CMC发送ACCP_INFORMATION消息*

**

\*Jan 20 08:59:35:684 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: CMC \--\> LGS : ACCP_SETUP_ACK

*[// LGS*]*收到CMC发送的ACCP_SETUP_ACK消息*

\*Jan 20 08:59:35:684 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Succeed in stopping Dial_Interval timer,]

state:FXS_CALLER_PREPARE

\*Jan 20 08:59:35:684 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 LGS \--\> DRV: VOICE_COM_DTMF_DETECT_OFF]

\*Jan 20 08:59:35:684 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Succeed in starting Wait_ACCP_ALERTING timer,]

state:FXS_CALLER_PREPARE, time length:35000ms.

\*Jan 20 08:59:35:685 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Fsm: [0x000005a3 State changes from FXS_CALLER_PREPARE to FXS_CALLER_CONNECTING]

\*Jan 20 08:59:35:716 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: CMC \--\> LGS : ACCP_ALERTING

\*Jan 20 08:59:35:716 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Delete timer Wait ACCP_ALERTING success,]

state:FXS_CALLER_CONNECTING

\*Jan 20 08:59:35:717 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: Inband information is unavailable. Play ring-back tone in two seconds.

*// 带内消息不可用，两秒钟后播放回铃音*

\*Jan 20 08:59:35:717 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: [0x000005a3 Create timer Delay Ring Back,]

state:FXS_CALLER_CONNECTING, time length:2000ms.

\*Jan 20 08:59:35:717 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Fsm: [0x000005a3 State changes from FXS_CALLER_CONNECTING to FXS_CALLER_RING_BACK]

\*Jan 20 08:59:37:758 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Timer: Delay ring back timer timed out in FXS_CALLER_RING_BACK state.

*[// Delay ring back*]*定时器在FXS_CALLER_RING_BACK状态下超时*

\*Jan 20 08:59:37:758 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 Send play RingBack tone command to driver in ]

FXS_CALLER_RING_BACK state.

\*Jan 20 08:59:37:758 2012 Sysname LGS/7/LGS_DEBUG:

LGS_Event: [0x000005a3 LGS \--\> DRV: VOICE_COM_TONE_GEN_ON]

**语音用户线 \-- 语音用户线调试命令 \-- debugging voice em**

------------------------------------------------------------------------

【命令】

**[debugging vioce em **[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

**[undo debugging voice em**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示EM所有消息类型的调试信息开关。

**[error**]：表示EM的错误类型的消息调试信息开关。

**[event**]：表示EM的事件类消息调试信息开关。

**[fsm**]：表示EM的状态机类消息调试信息开关。

**[info**]：表示EM的信息类消息调试信息开关。

**[timer**]：表示EM的定时器消息调试信息开关。

【描述】

**[debugging voice em**]命令用来打开EM调试信息开关。**undo debugging voice em**命令用来关闭EM调试信息开关。

缺省情况下，EM调试信息开关处于关闭状态。

表1-6 debugging voice em error令输出信息描述表

字段

描述

 Received unknown driver message!

收到EM不支持的驱动消息

Failed to wait message.

等待消息超时

Failed to get EM private data from interface *index*

获取EM接口*index*下配置失败

Failed to send message.

发送消息失败

表1-7 debugging voice em event令输出信息描述表

字段

描述

 Succeed in sending message-type  to CMC.

EM模块给CMC模块发送*message-type*消息

*[message-type*]取值为：

·ACCP_SETUP：表示被叫给CMC发送建立新呼叫的信令

·ACCP_SETUP_ACK：表示主叫对CMC发起新呼叫的应答信令

·ACCP_RELEASE：表示主/被叫给CMC发送拆线信令

·ACCP_RELEASE_COMPLETE：表示主/被叫给CMC发送完成拆线信令

·ACCP_CONNECT：表示主叫给CMC发送通话连接信令

·ACCP_ALERTING：表示主叫给CMC发送振铃信令

·ACCP_CHANNEL_READY：表示主/被给CMC发送媒体通道准备就绪信令

·ACCP_CHANNEL_UPDATE：表示主/被叫给CMC发送的媒体通道更新信令

·ACCP_INFORMATION：表示主/被叫给CMC发送DTMF信令

EM \--\> DRV: *command-type*

EM 模块给驱动下发命令字：

*[command-type*]取值为：

·VOICE_COM_INSTALL：表示给驱动下发发起呼叫的命令

·VOICE_COM_UNINSTALL：表示给驱动下发拆除呼叫的命令

·VOICE_AEM_SEIZE：表示给驱动下发占用信令

·VOICE_AEM_IDLE：表示给驱动下发示闲信令

·VOICE_COM_DTMF_GEN：表示给驱动下发发送号码的命令

·VOICE_COM_TONE_GEN_ON：表示给驱动下发播放提示音的命令

·VOICE_COM_TONE_GEN_OFF：表示给驱动下发停止播放提示音的命令

·VOICE_COM_DTMF_DETECT_ON：表示给驱动下发打开DTMF检测的命令

·VOICE_COM_DTMF_DETECT_OFF：表示给驱动下发关闭DTMF检测的命令

Received *message-type* message from CMC in state *call-state*.

EM在*call-state*状态下收到*message-type*消息

*[message-type*]取值为：

·ACCP_SETUP：表示CMC给主叫发送的建立新呼叫的消息

·ACCP_SETUP_ACK：表示CMC给被叫发送的建立新呼叫应答消息

·ACCP_RELEASE：表示收到了CMC拆除呼叫的消息

·ACCP_RELEASE_COMPLETE：表示CMC对E&M发送的拆除呼叫请求的应答

·ACCP_CONNECT：表示CMC连接建立的消息

·ACCP_ALERTING：表示被叫端已经开始振铃

·ACCP_CHANNEL_READY：表示主叫端收到CMC，已经准备好媒体通道的消息

Received *event-type* from DRV in * call-state*.

EM在*call-state*状态下收到驱动发的*event-type*事件

*[event-type*]取值为：

·VOICE_EVENT_COM_INSTALL_ACK：表示驱动给EM上报呼叫初始化的处理结果的事件

·VOICE_EVENT_COM_DTMF_IND：表示驱动给EM上报收到了DTMF被叫号码的应答事件

表1-8 debugging voice em fsm令输出信息描述表

字段

描述

 State changed from *current-state* to *next-state*.

呼叫状态从当前状态*current-state*切换到下一个状态*next-state*

*[current-state*]和*next-state*取值为：

·EM_IDLE ：表示通道空闲

·EMCALLER_WAIT_INSTALL_ACK：表示正在等待驱动建立连接

·EMCALLER_WAIT_OCCUPY：表示等待占用信号的上升沿

·EMCALLER_WAIT_SEND_NUMBER：表示等待发送被叫号码

·EMCALLER_SENDING_NUMBER：表示主叫端正在发送被叫号码

·EMCALLER_RINGING：表示主叫端正在听回铃音,即等待被叫应答

·EMCALLER_TALKING：表示主叫正在通话

·EMCALLER_ONHOOK：表示主叫先挂机

·EMCALLED_WAIT_SEND_OCCUPY：表示等待发送占用信号上升沿

·EMCALLED_WAIT_RECEIVE_NUMBER：表示等待接收被叫号码

·EMCALLED_RECEIVING_NUMBER：表示被叫端正在接收被叫号码

·EMCALLED_WAIT_SETUP_ACK：表示等待呼叫初始化完成

·EMCALLED_RINGING：表示被叫正在振铃

·EMCALLED_TALKING：表示被叫正在通话

·EMCALLED_ONHOOK：表示被叫先挂机

·EMCALLED_BUSYTONE：表示被叫正在播放忙音

表1-9 debugging voice em info令输出信息描述表

字段

描述

The current interface index*index* has been occupied.

当前的语音接口*index*被占用

Succeed in creating E&M CCB*id*

成功创建CCB{.TableTextChar}(呼叫控制块[)，]*[id*]{.TableTextChar}为呼叫控制块的标识

表1-10 debugging voice em timer令输出信息描述表

字段

描述

Deleted TimerId timer-id

删除特定的定时器

*[timer-id*]为定时器的唯一标示

Created message-waiting confirmation timer timer-id， [length is 50 ms]

创建示闲信号确认定时器，时长为*time-length*毫秒

Created message-occupied confirmation timer timer-id， [length is 50 ms.]

创建占用信号确认定时器，时长为*time-length*毫秒

**

【举例】

\# E&M语音用户线5/0为主叫，E&M语音用户线5/3为被叫，被叫号码为20。

\<Sysname\> debugging vioce em all

\*Feb 10 11:41:47:756 2012 Sysname EM/7/EM_DEBUG:

EM_Event: CMC \--\> EM : ACCP_SETUP

*// 主叫端CMC发来建立呼叫消息*

\*Feb 10 11:41:47:757 2012 Sysname EM/7/EM_DEBUG:

EM_Info: [subscriber-line5/0: Succeed in creating EM CCB0]

*// 创建呼叫控制块，控制块ID为0*

\*Feb 10 11:41:47:757 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Received ACCP_SETUP message from CMC on state EM_IDLE.]

\*Feb 10 11:41:47:758 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Created message wait timer0 to wait install ack, length is 1000ms.]

\*Feb 10 11:41:47:758 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_COM_INSTALL]

\*Feb 10 11:41:47:758 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/0: State changed from EM_IDLE to EMCALLER_WAIT_INSTALL_ACK.]

\*Feb 10 11:41:47:790 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Received VOICE_EVENT_COM_INSTALL_ACK from DRV on state EMCALLER_WAIT_INSTALL_ACK.]

\*Feb 10 11:41:47:790 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_COM_DTMF_DETECT_OFF.]

\*Feb 10 11:41:47:790 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId 0.]

\*Feb 10 11:41:47:790 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Created message wait timer0 to dialout delay, length is 300ms.]

\*Feb 10 11:41:47:791 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in sending ACCP_SETUP_ACK to CMC.]

\*Feb 10 11:41:47:791 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_AEM_SEIZE.]

*// 主叫端向驱动下发占用信号命令*

\*Feb 10 11:41:47:792 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in sending low-to-high level.]

\*Feb 10 11:41:47:792 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in sending ACCP_ALERTING to CMC.]

\*Feb 10 11:41:47:793 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/0: State changed from EMCALLER_WAIT_INSTALL_ACK to EMCALLER_WAIT_SEND_NUMBER.]

\*Feb 10 11:41:47:880 2012 Sysname EM/7/EM_DEBUG:

EM_Info: [subscriber-line5/3: Succeed in creating EM CCB1]

*// 被叫端创建呼叫控制块，控制块ID为1*

\*Feb 10 11:41:47:880 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received VOICE_EVENT_AEM_SEIZE from DRV on state EM_IDLE.]

*// 被叫端在空闲状态收到驱动上报的占用信号，准备建立呼叫*

\*Feb 10 11:41:47:881 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Created message wait timer1 to seize confirm, length is 50ms.]

\*Feb 10 11:41:47:925 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received EM_TIMER_SIGNAL_CONFIRM on state EM_IDLE.]

\*Feb 10 11:41:47:925 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId 1.]

\*Feb 10 11:41:47:925 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Created message wait timer1 to wait install ack, length is 1000ms.]

\*Feb 10 11:41:47:926 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: EM \--\> DRV: VOICE_COM_INSTALL]

\*Feb 10 11:41:47:926 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/3: State changed from EM_IDLE to EMCALLED_WAIT_RECEIVE_NUMBER.]

\*Feb 10 11:41:47:970 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received VOICE_EVENT_COM_INSTALL_ACK from DRV on state EMCALLED_WAIT_RECEIVE_NUMBER.]

\*Feb 10 11:41:47:970 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId 1.]

\*Feb 10 11:41:47:970 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Created message wait timer1 to wait dtmf ind, length is 5000ms.]

\*Feb 10 11:41:47:971 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: EM \--\> DRV: VOICE_COM_DTMF_DETECT_ON.]

\*Feb 10 11:41:47:971 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/3: State changed from EMCALLED_WAIT_RECEIVE_NUMBER to EMCALLED_RECEIVING_NUMBER.]

*// 被叫端呼叫状态从等待收号到进行收号*

\*Feb 10 11:41:48:125 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Received EM_TIMER_SIGNAL_WAIT on state EMCALLER_WAIT_SEND_NUMBER.]

\*Feb 10 11:41:48:125 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId 0.]

*// 删除定时器标示为1的定时器*

\*Feb 10 11:41:48:125 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_COM_DTMF_GEN]

DTMF Number is 20

\*Feb 10 11:41:48:126 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Created message wait timer0 to wait dtmf ack, length is 60000ms.]

\*Feb 10 11:41:48:126 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/0: State changed from EMCALLER_WAIT_SEND_NUMBER to EMCALLER_SENDING_NUMBER.]

\*Feb 10 11:41:48:260 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received VOICE_EVENT_COM_DTMF_IND from DRV on state EMCALLED_RECEIVING_NUMBER.]

\*Feb 10 11:41:48:260 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId 1.]

\*Feb 10 11:41:48:260 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Succeed in sending ACCP_SETUP to CMC, Number is 2]

\*Feb 10 11:41:48:260 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Begin to receive next called number.]

\*Feb 10 11:41:48:261 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Created message wait timer1 to inter digit, length is 10000ms.]

\*Feb 10 11:41:48:261 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/3: State changed from EMCALLED_RECEIVING_NUMBER to EMCALLED_RECEIVING_NUMBER_PREPARE.]

\*Feb 10 11:41:48:530 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received VOICE_EVENT_COM_DTMF_IND from DRV on state EMCALLED_RECEIVING_NUMBER_PREPARE.]

\*Feb 10 11:41:48:530 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [0x00000694: Send call number to CMC in EMCALLED_RECEIVING_NUMBER_PREPARE state.]

\*Feb 10 11:41:48:530 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Succeed in sending ACCP_INFORMATION to CMC]

\*Feb 10 11:41:48:530 2012 Sysname EM/7/EM_DEBUG:

EM_Event: DTMF Character 0

\*Feb 10 11:41:48:533 2012 Sysname EM/7/EM_DEBUG:

EM_Event: CMC \--\> EM : ACCP_SETUP_ACK

\*Feb 10 11:41:48:533 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received ACCP_SETUP_ACK message from CMC on state EMCALLED_RECEIVING_NUMBER_PREPARE.]

\*Feb 10 11:41:48:534 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId 1.]

\*Feb 10 11:41:48:534 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: EM \--\> DRV: VOICE_COM_DTMF_DETECT_OFF.]

*// 被叫端结束收号，向驱动下发停止收号命令*

**

\*Feb 10 11:41:48:534 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Created message wait timer1 to wait alerting, length is 40000ms.]

\*Feb 10 11:41:48:534 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/3: State changed from EMCALLED_RECEIVING_NUMBER_PREPARE to EMCALLED_RINGING.]

\*Feb 10 11:41:48:586 2012 Sysname EM/7/EM_DEBUG:

EM_Event: CMC \--\> EM : ACCP_ALERTING

\*Feb 10 11:41:48:586 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received ACCP_ALERTING message from CMC on state EMCALLED_RINGING.]

\*Feb 10 11:41:48:587 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId 1.]

\*Feb 10 11:41:48:587 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Succeed in sending ACCP_CHANNEL_READY to CMC.]

\*Feb 10 11:41:48:587 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Created message wait timer1 to wait connect, length is 60000ms.]

\*Feb 10 11:41:48:588 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: EM \--\> DRV: VOICE_COM_TONE_GEN_ON.]

Succeed in sending ringing to Driver.

\*Feb 10 11:41:48:680 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Received VOICE_EVENT_COM_DTMF_ACK from DRV on state EMCALLER_SENDING_NUMBER.]

\*Feb 10 11:41:48:680 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId 0.]

\*Feb 10 11:41:48:680 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Created message wait timer0 to seize signal, length is 60000ms.]

*// 主叫端创建等待被叫端占用信号的定时器，时长为60000毫秒*

\*Feb 10 11:41:48:684 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in sending ACCP_CHANNEL_READY to CMC.]

\*Feb 10 11:41:48:684 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/0: State changed from EMCALLER_SENDING_NUMBER to EMCALLER_RINGING.]

\*Feb 10 11:41:48:684 2012 Sysname EM/7/EM_DEBUG:

EM_Event: CMC \--\> EM : ACCP_CHANNEL_READY_ACK

\*Feb 10 11:41:50:788 2012 Sysname EM/7/EM_DEBUG:

EM_Event: CMC \--\> EM : ACCP_CHANNEL_READY_ACK

\*Feb 10 11:41:50:888 2012 Sysname EM/7/EM_DEBUG:

EM_Event: CMC \--\> EM : ACCP_CONNECT

*// 被叫端收到CMC连接建立的消息*

\*Feb 10 11:41:50:888 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received ACCP_CONNECT message from CMC on state EMCALLED_RINGING.]

\*Feb 10 11:41:50:889 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId 1.]

\*Feb 10 11:41:50:889 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: EM \--\> DRV: VOICE_COM_TONE_GEN_OFF]

\*Feb 10 11:41:50:889 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Succeed in stopping ringing.]

\*Feb 10 11:41:50:889 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: EM \--\> DRV: VOICE_AEM_SEIZE.]

\*Feb 10 11:41:50:890 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Succeed in sending low-to-high level.]

\*Feb 10 11:41:50:890 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/3: State changed from EMCALLED_RINGING to EMCALLED_TALKING.]

\*Feb 10 11:41:50:970 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Received VOICE_EVENT_AEM_SEIZE from DRV on state EMCALLER_RINGING.]

\*Feb 10 11:41:50:970 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in sending ACCP_CONNECT to CMC.]

\*Feb 10 11:41:50:971 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId 0.]

\*Feb 10 11:41:50:971 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/0: State changed from EMCALLER_RINGING to EMCALLER_TALKING.]

*// 主叫端从播放回铃音的状态切换到通话的状态*

\*Feb 10 11:41:55:597 2012 Sysname EM/7/EM_DEBUG:

EM_Event: CMC \--\> EM : ACCP_RELEASE

\*Feb 10 11:41:55:597 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Received ACCP_RELEASE message from CMC on state EMCALLER_TALKING.]

*// 主叫端在通话状态下从CMC收到挂机信号*

\*Feb 10 11:41:55:597 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Created message wait timer0 to busy tone end, length is 60000ms.]

\*Feb 10 11:41:55:598 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_COM_DTMF_DETECT_OFF.]

\*Feb 10 11:41:55:598 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_AEM_IDLE.]

*// 主叫端向驱动下发示闲信令，准备拆除呼叫*

\*Feb 10 11:41:55:599 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in sending high-to-low level.]

\*Feb 10 11:41:55:599 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_COM_TONE_GEN_ON.]

Succeed in sending busytone to Driver.

\*Feb 10 11:41:55:599 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/0: State changed from EMCALLER_TALKING to EMCALLER_CALLER_ONHOOK.]

\*Feb 10 11:41:55:599 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in sending ACCP_RELEASE_COMPLETE to CMC.]

\*Feb 10 11:41:55:680 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received VOICE_EVENT_AEM_IDLE from DRV on state EMCALLED_TALKING.]

*// 被叫端在通话状态下收到主叫端的示闲信号，准备拆除呼叫*

\*Feb 10 11:41:55:680 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Created message wait timer1 to idle confirm, length is 50ms.]

\*Feb 10 11:41:55:725 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received EM_TIMER_SIGNAL_CONFIRM on state EMCALLED_TALKING.]

\*Feb 10 11:41:55:725 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId 1.]

\*Feb 10 11:41:55:725 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: EM \--\> DRV: VOICE_AEM_IDLE.]

\*Feb 10 11:41:55:725 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Succeed in sending high-to-low level.]

\*Feb 10 11:41:55:726 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Succeed in sending ACCP_RELEASE to CMC.]

\*Feb 10 11:41:55:726 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Created message wait timer1 to wait release complete, length is 3000ms.]

\*Feb 10 11:41:55:726 2012 Sysname EM/7/EM_DEBUG:

EM_Fsm: [subscriber-line5/3: State changed from EMCALLED_TALKING to EMCALLED_CALLED_ONHOOK.]

\*Feb 10 11:41:55:729 2012 Sysname EM/7/EM_DEBUG:

EM_Event: CMC \--\> EM : ACCP_RELEASE_COMPLETE

\*Feb 10 11:41:55:729 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Received ACCP_RELEASE_COMPLETE message from CMC on state EMCALLED_CALLED_ONHOOK.]

\*Feb 10 11:41:55:729 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId 1.]

\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: EM \--\> DRV: VOICE_COM_UNINSTALL.]

\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId -1.]

\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId -1.]

\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId -1.]

\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/3: Deleted TimerId -1.]

\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/3: Succeed in deleting EMCCB1.]

*// 被叫端删除控制块，表明已经拆除此路呼叫*

\*Feb 10 11:41:55:800 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Received VOICE_EVENT_AEM_IDLE from DRV on state EMCALLER_CALLER_ONHOOK.]

\*Feb 10 11:41:55:800 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Created message wait timer1 to idle confirm, length is 50ms.]

\*Feb 10 11:41:55:825 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Received EM_TIMER_SIGNAL_CONFIRM on state EMCALLER_CALLER_ONHOOK.]

\*Feb 10 11:41:55:825 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId 1.]

\*Feb 10 11:41:55:825 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_COM_TONE_GEN_OFF]

\*Feb 10 11:41:55:825 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in stopping busytone.]

\*Feb 10 11:41:55:826 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId 0.]

\*Feb 10 11:41:55:826 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_AEM_IDLE.]

\*Feb 10 11:41:55:826 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in sending high-to-low level.]

\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: EM \--\> DRV: VOICE_COM_UNINSTALL.]

*// 主叫端向驱动下发拆除呼叫命令，通知驱动拆线*

\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId -1.]

\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId -1.]

\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId -1.]

\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG:

EM_Timer: [subscriber-line5/0: Deleted TimerId -1.]

\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG:

EM_Event: [subscriber-line5/0: Succeed in deleting EMCCB0]

*// 主叫端删除控制块，表明呼叫完全拆除*

**语音用户线 \-- 语音用户线调试命令 \-- debugging voice r2**

------------------------------------------------------------------------

【命令】

**[debugging voice r2 **[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

**[undo debugging voice r2 **[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示R2所有消息类型的调试信息开关。

**[error**]：表示R2的错误类型的消息调试信息开关。

**[event**]：表示R2的事件类消息调试信息开关。

**[fsm**]：表示R2的状态机类消息调试信息开关。

**[info**]：表示R2的信息类消息调试信息开关。

**[timer**]：表示R2的定时器消息调试信息开关。

【描述】

**[debugging voice r2**]命令用来打开R2调试信息开关。**undo debugging voice r2**命令用来关闭R2调试信息开关。

缺省情况下，R2调试信息开关处于关闭状态。

表1-11 debugging voice r2 error令输出信息描述表

字段

描述

Failed to send *message-type* to cmc.

R2向CMC 模块发送消息失败

*[message-type *]取值为：

·ACCP_SETUP：表示入局端给CMC发送建立新呼叫信令

·ACCP_SETUP_ACK：表示出局端对CMC发起新呼叫的应答信令

·ACCP_ALERTING：表示出局端给CMC发送振铃信令

·ACCP_CONNECT：表示出局端给CMC发送通话连接信令

Failed to send *command-type* to driver.

R2向驱动下发命令字失败

*[command-type *]命令字类型取值为：

·VOICE_COM_INSTALL：表示出局端给驱动下发安装呼叫准备工作的命令

·VOICE_COM_DTMF_GEN：表示出局端通过DTMF方式给驱动下发被叫号码

·VOICE_CAS_LINESIG：表示出局端给驱动下发线路信令

·VOICE_COM_MFC_GEN_ON：表示出局端给驱动下发MFC信令

Failed to send VOICE \_CAS_LINESIG *lineSig-type* to driver.

R2向驱动下发线路信令失败，其中线路信令值为*lineSig-type *取值为：

·IDLE：表示当前线路处于空闲状态

·BLOCK：表示当前线路处于被阻塞状态

·SEIZURE：表示当前线路处于被占用状态

·CLEARFORWARD：表示当前线路处于前向拆线状态

·SEIZUREACK：表示当前线路处于占用应答状态

·ANSWER：表示当前线路处于接通回应状态

·CLEARBACK：表示当前线路处于后向拆线状态

·RELEASEGUARD：表示当前线路处于后向释放监控状态

Invalid register signal.

记发器信令无效

Failed to allocate memory to R2 CCB.

给R2控制块分配内存失败

Failed to initialize R2 CCB.

初始化R2控制块数据失败

Failed to get free time slot.

获取空闲线路时隙失败

Received an unexpected message.

收到了无效的消息

Called number length exceed length limit.

被叫号码长度超过了长度限制

表1-12 debugging voice r2 event令输出信息描述表

字段

描述

R2 \--\> CMC: *message-type*.

R2 模块给CMC 模块发送 *[message-type *]消息

*[message-type*]取值为：

·ACCP_SETUP：表示入局端给CMC发送建立新呼叫信令

·ACCP_SETUP_ACK：表示出局端对CMC发起新呼叫的应答信令

·ACCP_RELEASE：表示出(入)局端给CMC发送拆线信令

·ACCP_RELEASE_COMPLETE：表示出(入)局端给CMC发送完成拆线信令

·ACCP_CONNECT：表示出局端给CMC发送通话连接信令

·ACCP_ALERTING：表示出局端给CMC发送振铃信令

·ACCP_CHANNEL_READY：表示出(入)局端给CMC发送媒体通道准备就绪信令

·ACCP_INFORMATION：表示出(入)局端给CMC发送DTMF信令

CMC \--\> R2: *message-type*.

CMC 模块给R2模块发送*message-type*消息

*[message-type*]取值为：

·ACCP_SETUP：表示CMC给出局端发送建立新呼叫信令

·ACCP_RELEASE：表示CMC给出(入)局端发送拆线信令

·ACCP_SETUP_ACK：表示CMC给入局端发送建立新呼叫的应答信令

·ACCP_ALERTING：表示CMC给入局端发送振铃信令

·ACCP_CONNECT：表示CMC给入局端发送通话连接信令

·ACCP_INFORMATION：表示CMC给出(入)局端发送DTMF信令

R2 \--\> DRV: *command-type*.

R2 模块给驱动下发命令字

*[command-type *]取值为：

·VOICE_COM_INSTALL ：表示给驱动下发安装呼叫准备工作的命令

·VOICE_COM_MFC_DETECT_ON ：表示给驱动下发打开检测MFC信令的开关

·VOICE_COM_TONE_GEN_ON ：表示给驱动下发打开播放提示音的开关

·VOICE_RECEIVE_GAIN ：表示给驱动下发设置输入增益的命令

·VOICE_COM_EC_ON ：表示给驱动下发打开回波抵消的开关

·VOICE_COM_EC_OFF ：表示给驱动下发关闭回波抵消的开关

·VOICE_TRANSMIT_GAIN ：表示给驱动下发设置输出增益的命令

·VOICE_COM_DTMF_DETECT_OFF ：表示给驱动下发关闭DTMF信令检测的开关

·VOICE_COM_MFC_DETECT_OFF ：表示给驱动下发关闭MFC信令检测的开关

·VOICE_COM_UNINSTALL ：表示给驱动下发卸载呼叫准备的命令

·VOICE_CAS_LINESIG ：表示给驱动下发各种线路信令

·VOICE_COM_TONE_GEN_OFF ：表示给驱动下发关闭播放提示音的开关

·VOICE_COM_MFC_GEN_ON ：表示给驱动下发打开接收MFC信令的开关

·VOICE_COM_MFC_GEN_OFF ：表示给驱动下发关闭接收MFC信令的开关

DRV \--\> R2: *event-type*.

驱动给 R2模块上报的事件

*[event-type*]取值为：

·VOICE_EVENT_COM_INSTALL_ACK ：表示驱动给出局端上报安装呼叫准备结果的事件

·VOICE_EVENT_COM_DTMF_ACK ：表示驱动给出局端上报接收到了DTMF被叫号码的应答事件

·VOICE_EVENT_E1T1_SUB_CAS_LINESIG ：表示驱动上报的用户线路信令事件

Set reg status to *stage-type* successfully.

在 MFC方式下，把记发器REG的状态设置为*stage-type*阶段

*[stage-type*]取值为：

·R2_REG_STAGE_SEND_CALLEDNUMBER ：表示出局端发送被叫号码

·R2_REG_STAGE_SEND_CALLERNUMBER：表示出局端发送主叫号码

·R2_REG_STAGE_OVER_CALLERNUMBER ：表示出局端把主叫号码发送完毕

·R2_REG_STAGE_SEND_BILLINGCATEGORY：表示出局端处于发送计费业务类别阶段

·R2_REG_STAGE_WAIT_CALLEDNUMBER：表示入局端处于等待接收被叫号码阶段

·R2_REG_STAGE_WAIT_CALLERNUMBER：表示入局端处于等待接收主叫号码阶段

·R2_REG_STAGE_WAIT_BILLINGCATEGORY：表示入局端处于等待接收计费业务类别阶段

表1-13 debugging voice r2 fsm令输出信息描述表

字段

描述

The *event-type* event processed in *state-type* state.

在 *[state-type *]状态下，处理*event-type *事件

 *event-type* 取值为：

·R2_CTL_EVENT_ACCP_SETUP：表示新呼叫发起

·R2_CTL_EVENT_ACCP_SETUP_ACK：表示安装新呼叫准备工作的应答事件

·R2_CTL_EVENT_ACCP_ALERTING：表示回铃音事件

·R2_CTL_EVENT_ACCP_CONNECT：表示建立通话连接事件

·R2_CTL_EVENT_ACCP_RELEASE：表示通话拆线事件

·R2_CTL_EVENT_ACCP_INFORMATION：表示通话中收到DTMF消息事件

·R2_CTL_EVENT_DL_TKO_SEIZURE_ACK：表示出局端的线路占用信令应答事件

·R2_CTL_EVENT_DL_TKO_ANSWER：表示出局端的线路接通回应事件

·R2_CTL_EVENT_DL_TKO_RELEASE：表示出局端的线路拆线事件

·R2_CTL_EVENT_DL_TKO_CLEAR_BACK：表示出局端的后向主动拆线事件

·R2_CTL_EVENT_DL_TKI_SEIZURE：表示入局端的线路占用信令事件

·R2_CTL_EVENT_DL_TKI_CLEAR_FORWARD：表示入局端的线路前向拆线事件

·R2_CTL_EVENT_REG_TKO_END_SUCCESS：表示出局端记发器拨号正确结束事件

·R2_CTL_EVENT_REG_TKO_END_BUSY：表示出局端记发器因入局端线路忙，结束

·R2_CTL_EVENT_REG_TKO_END_NULLNUMBER：表示出局端记发器因被叫号码为空号，错误结束

·R2_CTL_EVENT_REG_TKI_END_SUCCESS：表示入局端记发器收到完整被叫号码，正确结束

·R2_CTL_EVENT_REG_TKI_END_NULLNUM：表示入局端记发器收到非法号码，错误终止

·R2_CTL_EVENT_NOTIFY_REG_START：表示发送启动记发器信令事件

·R2_CTL_EVENT_NOTIFY_DTMF_START：表示发送启动DTMF拨号事件

·R2_CTL_EVENT_NO_RECEIVED_ANSWER：表示出局端未收到入局端的接通回应事件

·R2_CTL_EVENT_RECEIVED_ANSWER：表示出局端收到了入局端的接通回应事件

·R2_CTL_EVENT_RECEIVED_ACCP_CONNECT：表示出局端收到了入局端的建立通话连接事件

·R2_CTL_EVENT_NO_RECEIVED_ACCP_CONNECT：表示出局端未收到入局端的建立通话连接事件

·R2_CTL_EVENT_RING_TIMEOUT：表示出局端接收回铃音超时事件

·R2_CTL_EVENT_DTMF_TKO_END：表示出局端停止拨号

·R2_CTL_EVENT_DTMF_TKI_END：表示入局端停止收号

*[state-type*]取值上一栏已列举

表1-14 debugging voice r2 info令输出信息描述表

字段

描述

Succeed in deleting R2 CCB.

删除呼叫控制块CCB成功

Succeed in creating R2 CCB.

创建呼叫控制块CCB成功

No call in current timeslot.

当前线路时隙上没有电话呼叫，即空闲状态

Succeed in creating and initializing R2 CCB.

成功创建并初始化呼叫控制块CCB

Time slot blocked by local commands.

当前线路时隙，由本地配置的命令所阻塞

Succeed in releasing the time slot.

成功释放时隙资源

表1-15 debugging voice r2 timer令输出信息描述表

字段

描述

*[timer-type*] timed out.

定时器超时

*[timer-type*]取值为：

·CTL_DTMF_DELAY_TIMER ：延时DTMF拨号定时器

·CTL_RING_TIMER ：播放回铃音定时器

·DL_TAKE_TIMER ：线路占用定时器

·DL_TAKEACK_TIMER ：线路占用应答定时器

·DL_HANGUP_TIMER ：线路挂起定时器

·REG_GROUP_I_TIMER ：记发器前向 I 组信令定时器

·REG_GROUP_II_TIMER ：记发器前向 II 组信令定时器

·REG_GROUP_A_TIMER ：记发器后向 A 组信令定时器

·REG_GROUP_B_TIMER ：记发器后向 B 组信令定时器

·REG_END_TIMER ：记发器拨号结束定时器

Succeed in starting the timer *timer-type*. Timer ID = *timerID*, Timer length = *length* ms.

启动定时器，定时器类型为 *[timer-type*]，定时器标识为 *[timerID*]*，*定时器时长为 *[length*]毫秒。*timer-type *取值上一栏已列举

Failed to start the timer *timer-type*.

启动定时器失败，定时器类型为 timer-type, timer-type 取值上一栏已列举

Succeed in deleting the timer. TimerID = *timerID*.

删除定时器，定时器的标识为 *[timerID*]

【举例】

\# 主叫方采用DTMF方式拨打被叫方电话2222。打开主叫侧R2事件类型的调试信息输出开关。

\<Sysname\> debugging vioce r2 event

\*May 18 20:56:16:922 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[D-Invalid: CMC \--\> R2: ACCP_SETUP.]

*[// CMC*]*向R2发送ACCP_SETUP消息*

**

\*May 18 20:56:16:924 2023 Sysname R2/7/R2_DEBUG:

R2_INFO[D-6/0:1.0: Succeed in creating R2 CCB.]

*// 创建R2控制块成功*

\*May 18 20:56:16:925 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_ACCP_SETUP event processed in R2_CTL_STATE_IDLE state.]

*[// R2 *]*在R2_CTL_STATE_IDLE 空闲状态下，处理R2_CTL_EVENT_ACCP_SETUP 事件*

\*May 18 20:56:16:925 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> DRV: VOICE \_COM_INSTALL.]

*[// R2 *]*给驱动下发安装新呼叫准备工作的命令字*

\*May 18 20:56:16:926 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in starting the timer CTL_VI_INSTALL_TIMER. Timer ID = 0x0, Timer length = 3000.]

*// 启动R2 等待驱动安装新呼叫准备应答的定时器，timerID = 0，timerLen = 3 s*

\*May 18 20:56:16:927 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of CTL module changes from R2_CTL_STATE_IDLE to R2_CTL_STATE_OUT_INIT.]

*[// CTL *]*模块的状态由R2_CTL_STATE_IDLE  空闲状态变为R2_CTL_STATE_OUT_INIT 出局端初始化状态*

\*May 18 20:56:16:932 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_VI_INSTALL_ACK event processed in R2_CTL_STATE_OUT_INIT state.]

*[// CTL *]*模块在R2_CTL_STATE_OUT_INIT 出局端初始化状态下，处理R2_CTL_EVENT_VI_INSTALL_ACK 收到驱动上报的安装结果的应答事件*

\*May 18 20:56:16:932 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in deleting the timer. TimerID = 0x0.]

*// 删除等待驱动上报 INSTALL_ACK事件的定时器，timerID = 0*

\*May 18 20:56:16:933 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: DRV \--\> R2: VOICE_EVENT_COM_INSTALL_ACK. The Result: SUCCESS.]

*// 驱动给R2 上报 INSTALL \_ACK 事件，结果：安装成功，新呼叫准备就绪*

\*May 18 20:56:16:933 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> CMC: ACCP_SETUP_ACK.]

*[// R2 *]*给出局端的 CMC 模块应答 ACCP_SETUP_ACK 消息*

\*May 18 20:56:16:934 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DL_EVENT_CTL_SEIZURE event processed in R2_DL_STATE_IDLE state.]

*[// DL *]*模块在R2_DL_STATE_IDLE 空闲状态下，处理R2_DL_EVENT_CTL_SEIZURE 线路占用事件*

\*May 18 20:56:16:935 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> DRV: VOICE_CAS_LINESIG Seizure.]

*[// R2 *]*给驱动下发线路信令，信令为：Seizure占用信令*

\*May 18 20:56:16:936 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in starting the timer DL_TAKE_TIMER. Timer ID = 0x0, Timer length = 1000.]

*// 启动线路占用定时器， timerID = 0， timerLen = 1000 ms*

\*May 18 20:56:16:936 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of DL module changes from R2_DL_STATE_IDLE to R2_DL_STATE_TAKE.]

*[// DL *]*模块的状态由R2_DL_STATE_IDLE 线路空闲变为R2_DL_STATE_TAKE 线路占用状态*

\*May 18 20:56:16:937 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of CTL module changes from R2_CTL_STATE_OUT_INIT to R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK.]

*[// CTL *]*模块的状态由R2_CTL_STATE_OUT_INIT 初始化状态变为R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK 等待线路占用应答状态*

\*May 18 20:56:16:993 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: DRV \--\> R2: VOICE_EVENT_E1T1_SUB_CAS_LINESIG 1101.]

*[// R2 *]*收到驱动上报的用户线路信令，信令值为： 1101*

\*May 18 20:56:16:994 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DL_EVENT_SIGNALFROMDRV event processed in R2_DL_STATE_TAKE state.]

*[// DL*]*模块在R2_DL_STATE_TAKE 线路占用的状态下，处理R2_DL_EVENT_SIGNALFROMDRV 来自驱动上报的用户线路信令事件*

\*May 18 20:56:16:995 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DL_EVENT_SEIZUREACKSIGNAL event processed in R2_DL_STATE_TAKE state.]

*[// DL *]*模块在R2_DL_STATE_TAKE 线路占用状态下，处理R2_DL_EVENT_SEIZUREACKSIGNAL 线路占用应答事件*

\*May 18 20:56:16:995 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in deleting the timer. TimerID = 0x0.]

*// 删除线路占用定时器，timerID = 0*

**

\*May 18 20:56:16:996 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in starting the timer DL_TAKEACK_TIMER. Timer ID = 0x0, Timer length = 60000.]

*// 启动DL_TAKEACK_TIMER 线路占用应答定时器，timerID = 0，timerLen = 60 s*

\*May 18 20:56:16:996 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_DL_TKO_SEIZURE_ACK event processed in R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK state.]

*[// CTL *]*模块在R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK 等待线路占用应答状态下，处理R2_CTL_EVENT_DL_TKO_SEIZURE_ACK 出局端收到线路占用应答的事件*

\*May 18 20:56:16:997 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in starting the timer CTL_DTMF_DELAY_TIMER. Timer ID = 0x1, Timer length = 50.]

*// 启动CTL_DTMF_DELAY_TIMER 延时DTMF拨号定时器， timerID = 1，timerLen = 50 ms*

\*May 18 20:56:16:998 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of DL module changes from R2_DL_STATE_TAKE to R2_DL_STATE_TAKEACK.]

*[// DL *]*模块由R2_DL_STATE_TAKE 线路占用状态变为R2_DL_STATE_TAKEACK 线路占用应答状态*

\*May 18 20:56:17:017 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: CTL_DTMF_DELAY_TIMER timed out.]

*[// CTL_DTMF_DELAY_TIMER *]*延时DTMF拨号定时器超时，超时后开始使用DTMF方式发送被叫号码*

\*May 18 20:56:17:017 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in deleting the timer. TimerID = 0x1.]

*// 删除延时DTMF拨号定时器， timerID = 1*

\*May 18 20:56:17:018 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_NOTIFY_DTMF_START event processed in R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK state.]

*[// CTL *]*模块在R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK 出局端等待线路占用应答的状态下，处理R2_CTL_EVENT_NOTIFY_DTMF_START 通知启动DTMF模块事件*

\*May 18 20:56:17:018 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DTMF_EVENT_CTL_TKO_START event processed in R2_DTMF_STATE_IDLE state.]

*[// DTMF *]*模块在R2_DTMF_STATE_IDLE 空闲状态下，处理 R2_DTMF_EVENT_CTL_TKO_START 出局端启动DTMF模块的事件*

\*May 18 20:56:17:019 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> DRV: VOICE_COM_DTMF_GEN. Dtmf: 2222]

*[// R2 *]*给驱动下发 DTMF 信号，也就是被叫号码 2222*

\*May 18 20:56:17:020 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in starting the timer DTMF_WAIT_TIMER. Timer ID = 0x1, Timer length = 10000.]

\*May 18 20:56:17:020 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of DTMF module changes from R2_DTMF_STATE_IDLE to R2_DTMF_STATE_WAIT.]

*[// DTMF*]*模块由R2_DTMF_STATE_IDLE空闲状态变为R2_DTMF_STATE_WAIT等待 DTMF 消息的状态*

\*May 18 20:56:17:021 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of CTL module changes from R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK to R2_CTL_STATE_OUT_WAIT_DTMF_END.]

*[// CTL *]*模块由R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK 等待线路占用应答的状态变为R2_CTL_STATE_OUT_WAIT_DTMF_END 结束等待 DTMF消息* *的状态*

\*May 18 20:56:17:983 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: DRV \--\> R2: VOICE_EVENT_COM_DTMF_ACK. Result = Success.]

*// 驱动给 R2 上报VOICE_EVENT_COM_DTMF_ACK 发送DTMF 消息应答的事件，* *结果：成功发送被叫号码*

\*May 18 20:56:17:983 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DTMF_EVENT_DTMF_ACK event processed in R2_DTMF_STATE_WAIT state.]

*[// DTMF *]*模块在R2_DTMF_STATE_WAIT 等待DTMF消息状态下，处理R2_DTMF_EVENT_DTMF_ACK 收到 DTMF_ACK的事件*

\*May 18 20:56:17:984 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in deleting the timer. TimerID = 0x1.]

\*May 18 20:56:17:984 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_DTMF_TKO_END event processed in R2_CTL_STATE_OUT_WAIT_DTMF_END state.]

*[// CTL *]*模块在R2_CTL_STATE_OUT_WAIT_DTMF_END 结束等待DTMF 消息的状态下，处理R2_CTL_EVENT_DTMF_TKO_END 发送被叫号码结束的事件*

\*May 18 20:56:17:985 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_NO_RECEIVED_ANSWER event processed in R2_CTL_STATE_OUT_WAIT_DTMF_END state.]

*[// CTL *]*模块在R2_CTL_STATE_OUT_WAIT_DTMF_END 结束等待 DTMF 消息的状态下，处理R2_CTL_EVENT_NO_RECEIVED_ANSWER 未收到入局端发送的 ANSWER 信号事件*

\*May 18 20:56:17:985 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> CMC: ACCP_ALERTING.]

*[// R2 *]*向出局端 CMC 模块发送 ACCP_ALERTING 播放回铃音消息*

\*May 18 20:56:17:987 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> CMC: ACCP_CHANNEL_READY.]

*[// R2 *]*给 CMC 模块发送ACCP_CHANNEL_READY 语音通道准备就绪的消息*

\*May 18 20:56:17:990 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of CTL module changes from R2_CTL_STATE_OUT_WAIT_DTMF_END to R2_CTL_STATE_OUT_WAIT_ANSWER.]

*[// CTL *]*模块由R2_CTL_STATE_OUT_WAIT_DTMF_END 结束等待DTMF 消息的状态变为R2_CTL_STATE_OUT_WAIT_ANSWER 等待入局端发 ANSWER 的状态*

\*May 18 20:56:17:991 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of DTMF module changes from R2_DTMF_STATE_WAIT to R2_DTMF_STATE_IDLE.]

*[// DTMF *]*模块由R2_DTMF_STATE_WAIT 等待DTMF消息的状态变为R2_DTMF_STATE_IDLE 空闲状态*

\*May 18 20:56:21:235 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: DRV \--\> R2: VOICE_EVENT_E1T1_SUB_CAS_LINESIG 0101.]

*// 驱动给 R2 模块上报用户线路信令，信令值为： 0101*

\*May 18 20:56:21:236 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DL_EVENT_SIGNALFROMDRV event processed in R2_DL_STATE_TAKEACK state.]

*[// DL *]*模块在R2_DL_STATE_TAKEACK 线路占用应答的状态下，处理R2_DL_EVENT_SIGNALFROMDRV 来自驱动上报的线路信令事件*

\*May 18 20:56:21:236 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DL_EVENT_ANSWERSIGNAL event processed in R2_DL_STATE_TAKEACK state.]

*[// DL *]*模块在R2_DL_STATE_TAKEACK 线路占用应答的状态下，处理R2_DL_EVENT_ANSWERSIGNAL 收到驱动上报来的ANSWER 信令事件*

\*May 18 20:56:21:237 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in deleting the timer. TimerID = 0x0.]

\*May 18 20:56:21:237 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_DL_TKO_ANSWER event processed in R2_CTL_STATE_OUT_WAIT_ANSWER state.]

*[// CTL *]*模块在R2_CTL_STATE_OUT_WAIT_ANSWER 等待入局端发ANSWER信号的状态下，处理R2_CTL_EVENT_DL_TKO_ANSWER 来自DL模块透传的 ANSWER 信令事件*

**

\*May 18 20:56:21:238 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> CMC: ACCP_CONNECT.]

*[// R2 *]*给CMC 模块发送 ACCP_CONNECT建立通话连接的消息*

\*May 18 20:56:21:239 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of CTL module changes from R2_CTL_STATE_OUT_WAIT_ANSWER to R2_CTL_STATE_ACTIVE.]

*[// CTL *]*模块由R2_CTL_STATE_OUT_WAIT_ANSWER 等待入局端发 ANSWER 信号的状态变为R2_CTL_STATE_ACTIVE 已激活的状态*

\*May 18 20:56:21:240 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of DL module changes from R2_DL_STATE_TAKEACK to R2_DL_STATE_ANSWER.]

*[// DL *]*模块由R2_DL_STATE_TAKEACK 线路占用应答的状态变为R2_DL_STATE_ANSWER 收到入局端发的应答的状态*

\*May 18 20:56:26:862 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: CMC \--\> R2: ACCP_RELEASE.]

*[// CMC *]*给 R2 发送ACCP_RELEASE 前向拆线信号*

\*May 18 20:56:26:863 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> CMC: ACCP_RELEASE_COMPLETE.]

*[// R2 *]*给 CMC 回复ACCP_RELEASE_COMPLETE 前向拆线完成的信号*

\*May 18 20:56:26:864 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_ACCP_RELEASE event processed in R2_CTL_STATE_ACTIVE state.]

*[// CTL *]*模块在R2_CTL_STATE_ACTIVE 已激活的状态下，处理R2_CTL_EVENT_ACCP_RELEASE 收到前线拆线信令的事件*

\*May 18 20:56:26:864 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DL_EVENT_CTL_TKO_RELEASE event processed in R2_DL_STATE_ANSWER state.]

*[// DL *]*模块在R2_DL_STATE_ANSWER 收到入局端的应答状态下，处理R2_DL_EVENT_CTL_TKO_RELEASE 出局端主动拆线的信令事件*

\*May 18 20:56:26:865 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> DRV: VOICE_CAS_LINESIG ClearForward.]

*[// R2 *]*向驱动下发线路信令命令字，即前向拆线信令*

\*May 18 20:56:26:865 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in starting the timer DL_END_TIMER. Timer ID = 0x0, Timer length = 10000.]

\*May 18 20:56:26:866 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of DL module changes from R2_DL_STATE_ANSWER to R2_DL_STATE_END.]

*[// DL *]*模块由R2_DL_STATE_ANSWER 收到入局端应答的状态变为R2_DL_STATE_END 结束占用的状态*

\*May 18 20:56:26:867 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The state of CTL module changes from R2_CTL_STATE_ACTIVE to R2_CTL_STATE_RELEASE.]

*[// CTL *]*模块由R2_CTL_STATE_ACTIVE 已激活的状态变为R2_CTL_STATE_RELEASE 主动拆线状态*

\*May 18 20:56:26:873 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: DRV \--\> R2: VOICE_EVENT_E1T1_SUB_CAS_LINESIG 1001.]

*// 驱动给 R2 模块上报用户线路信令，信令值为： 1001，* *表示前向拆线*

\*May 18 20:56:26:874 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DL_EVENT_SIGNALFROMDRV event processed in R2_DL_STATE_END state.]

*[// DL *]*模块在R2_DL_STATE_END 线路结束被占用的状态下，处理R2_DL_EVENT_SIGNALFROMDRV 来自驱动上报的前向拆线信令事件*

\*May 18 20:56:26:875 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_DL_EVENT_RELEASEGUARDSIGNAL event processed in R2_DL_STATE_END state.]

*[// DL *]*模块在R2_DL_STATE_END 线路结束被占用的状态下，处理R2_DL_EVENT_RELEASEGUARDSIGNAL 后向释放监控信令事件*

\*May 18 20:56:26:875 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> DRV: VOICE_CAS_LINESIG Idle.]

*[// R2 *]*给驱动下发线路信令命令字，设置其状态为 Idle 空闲状态*

\*May 18 20:56:26:876 2023 Sysname R2/7/R2_DEBUG:

R2_TIMER[O-6/0:1.0: Succeed in deleting the timer. TimerID = 0x0.]

\*May 18 20:56:26:876 2023 Sysname R2/7/R2_DEBUG:

R2_FSM[O-6/0:1.0: The R2_CTL_EVENT_DL_TKO_RELEASE event processed in R2_CTL_STATE_RELEASE state.]

*[// CTL *]*模块在R2_CTL_STATE_RELEASE 前向拆线的状态下，处理R2_CTL_EVENT_DL_TKO_RELEASE 收到出局端主动拆线信令的事件*

\*May 18 20:56:26:877 2023 Sysname R2/7/R2_DEBUG:

R2_EVENT[O-6/0:1.0: R2 \--\> DRV: VOICE_COM_UNINSTALL.]

*[// R2 *]*给驱动下发卸载命令字，即卸载新呼叫所需的底层支撑部件*

\*May 18 20:56:26:877 2023 Sysname R2/7/R2_DEBUG:

R2_INFO[O-6/0:1.0: Succeed in freeing the time slot.]

*[// R2 *]*模块释放线路时隙成功*

\*May 18 20:56:26:878 2023 Sysname R2/7/R2_DEBUG:

R2_INFO[O-6/0:1.0: Succeed in deleting R2 CCB.]

*[// R2 *]*模块删除控制块，释放资源*

**语音用户线 \-- 语音用户线调试命令 \-- debugging voice iva**

------------------------------------------------------------------------

【命令】

**[debugging voice iva**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

**[undo debugging voice iva**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示IVA（ISDN Voice Adapter）所有消息类型的调试信息开关。

**[error**]：表示EM的错误类型的消息调试信息开关。

**[event**]：表示EM的事件类消息调试信息开关。

**[fsm**]：表示EM的状态机类消息调试信息开关。

**[info**]：表示EM的信息类消息调试信息开关。

**[timer**]：表示EM的定时器消息调试信息开关。

【描述】

**[debugging voice iva**]命令用来打开IVA调试信息开关。**undo debugging voice iva**命令用来关闭IVA调试信息开关。

缺省情况下，IVA调试信息开关处于关闭状态。

表1-16 debugging voice iva error令输出信息描述表

字段

描述

Failed to send *message-type* to cmc.

IVA向CMC 模块发送消息失败

*[message-type *]取值为：

·ACCP_SETUP：表示网络侧给CMC发送建立新呼叫信令

·ACCP_SETUP_ACK：表示IVA模块对CMC发起新呼叫的应答信令

·ACCP_ALERTING：表示网络侧给CMC发送振铃信令

·ACCP_CONNECT：表示网络侧给CMC发送通话连接信令

Failed to send *command-type* to driver.

IVA向驱动下发命令字失败

*[command-type *]命令字类型取值为：

·VOICE \_COM_INSTALL：表示IVA给驱动下发装配B通道的命令

·VOICE\_ COM_UNINSTALL：表示IVA给驱动下发去装配B通道的命令

·VOICE \_COM_DTMF_GEN：表示IVA通过DTMF方式给驱动下发被叫号码

Received *message-type* but failed to find the CCB.

IVA收到了CMC消息，但是获取相应的呼叫控制块失败

*[message-type *]取值为：

·ACCP_SETUP_ACK ：表示CMC模块对网络侧发起新呼叫的应答信令

·ACCP_ALERTING ：表示CMC给网络侧发送振铃信令

·ACCP_CONNECT：表示CMC给网络侧发送呼叫建立信令

·ACCP_RELEASE：表示CMC给网络侧发送释放呼叫信令

Failed to send ISDN *message-type* message.

IVA向ISDN发送消息失败

*[message-type *]取值为：

·SETUP_REQUEST：表示IVA模块向ISDN发送建立新呼叫的请求信令

·ALERTING_REQUEST ：表示IVA模块向ISDN发送振铃请求信令

·CONNECT_REQUEST：表示IVA模块向ISDN发送呼叫连接请求信令

·DISCONNECT_RESPOND：表示IVA模块向ISDN发送释放呼叫应答信令

The subscriber-line channel D is down.

语音用户线D通道关闭了

The physical Channel D is down.

物理D通道关闭了

Failed to release B channel.

释放B通道失败

Failed to get interface name by index.

通过接口索引获取接口名字失败

Failed to get physical status of interface by index.

通过接口索引获取接口物理状态失败

Failed to get physical interface type by index.

通过接口索引获取接口物理类型失败

表1-17 debugging voice iva event令输出信息描述表

字段

描述

 IVA \--\> CMC : *Message-type* message is sent to CMC Successfully.

IVA向CMC发送消息成功

*[Message-type*]取值为：

·ACCP_SETUP ：表示网络侧给CMC发送建立新呼叫信令

·ACCP_SETUP_ACK ：表示IVA模块对CMC发起新呼叫的应答信令

·ACCP_ALERTING ：表示网络侧给CMC发送振铃信令

·ACCP_CONNECT ：表示网络侧给CMC发送通话连接信令

IVA \--\> ISDN : *Message-type* message is sent to ISDN Successfully.

IVA向ISDN发送消息成功

*[message-type *]取值为：

·SETUP_REQUEST：表示IVA模块向ISDN发送建立新呼叫的请求信令

·ALERTING_REQUEST ：表示IVA模块向ISDN发送振铃请求信令

·CONNECT_REQUEST：表示IVA模块向ISDN发送呼叫连接请求信令

·DISCONNECT_RESPOND：表示IVA模块向ISDN发送释放呼叫应答信令

*ifindex* IVA \--\> DRV: *Command-type* command is sent to DRV.

IVA向驱动下发命令字成功

*[command-type *]命令字类型取值为：

·VOICE \_COM_INSTALL ：表示IVA给驱动下发装配B通道的命令

·VOICE\_ COM_UNINSTALL：表示IVA给驱动下发去装配B通道的命令

·VOICE \_COM_DTMF_GEN ：表示IVA通过DTMF方式给驱动下发被叫号码

CMC \--\> IVA : Received *message-type* message from CMC.

IVA收到CMC{.TableTextChar}消息

*[message-type *]取值为：

·ACCP_SETUP_ACK ：表示CMC模块对网络侧发起新呼叫的应答信令

·ACCP_ALERTING ：表示CMC给网络侧发送振铃信令

·ACCP_CONNECT：表示CMC给网络侧发送呼叫建立信令

·ACCP_RELEASE：表示CMC给网络侧发送释放呼叫信令

ISDN \--\> IVA : Received *message-type* message from ISDN.

IVA收到ISDN发送的消息

*[message-type*]取值为：

·IVA_SETUP_IND：表示ISDN向IVA发送建立新呼叫的请求信令

·IVA_CONN_IND ：表示ISDN向IVA发送呼叫连接请求信令

·IVA_DISC_IND：表示ISDN向IVA发送释放呼叫请求信令

DRV \--\> IVA : Received *message-type* message from driver, BchIfIndex= *ifindex.*

IVA收到驱动发送的消息，并且B通道的索引是*ifindex*

*[message-type*]取值为：

·INSTALL_BCH_ACK：表示驱动装配B通道成功

·INBAND_DTMF：表示驱动获取带外传输号码成功

Succeeded in installing channel B.

装配B通道成功

表1-18 debugging voice iva fsm令输出信息描述表

字段

描述

 Change state from *state-type* to *state-type*, CallID=*callId*.

呼叫状态改变，且对应的呼叫ID为*callId*

*[state-type *]取值为：

·IVA_IDLE：表示正处于空闲状态

·IVA_INCONNECTBCH ：表示正处于装配B通道的状态

·IVA_TALK：表示正处于通话

·IVA_CMC_RELEASING：表示正处于CMC拆线状态

表1-19 debugging voice iva info令输出信息描述表

字段

描述

 Succeeded in deleting CCB, CallID= *callId.*

删除CCB(呼叫控制块)成功，其所对应的CallID(呼叫标识)为callId

Succeeded in creating CCB, CallID= *callId.*

创建CCB(呼叫控制块)成功，其所对应的CallID(呼叫标识)为callId

Failed to find CCB by CmcId *cmcid*.

通过CmcId(cmc全局标识符)cmcid查找CCB(呼叫控制块)失败

Failed to find CCB by ifIndex *ifIndex*.

通过ifIndex(接口索引)ifIndex查找CCB(呼叫控制块)失败

Failed to find CCB by IsdnId *isdnid*.

通过IsdnId(Isdn全局标识符)isdnid查找CCB(呼叫控制块)失败

Received an unexpected message.

收到错误的信息

The called number does not exist.

被叫号码不存在

Received called number from ISDN.

收到ISDN发送的被叫号码

Succeed in sending messages to ISDN.

向ISDN进程发送消息成功

表1-20 debugging voice iva timer令输出信息描述表

字段

描述

 Succeed in starting the timer *timer-type*.

启动定时器成功

*[timer-type*]取值为：

·TIMER_INSTALLBCH：表示等待装配B通道的定时器

·TIMER_CMCALERTING：表示等待CMC发送振铃消息的定时器

·TIMER_CONN_IND：表示等待ISDN发送呼叫建立请求的定时器

·TIMER_DISC_CFM：表示等待ISDN发送呼叫释放确认消息的定时器

Succeed in deleting the timer %s.TimerID: *timerid.*

成功删除定时器，定时器标识为*timerid*

*[Timer-type*] timed out.

定时器超时

*[Timer-type*]取值为：

·TIMER_INSTALLBCH：表示等待装配B通道的定时器

·TIMER_CMCALERTING ：表示等待CMC发送振铃消息的定时器

·TIMER_CONN_IND：表示等待ISDN发送呼叫建立请求的定时器

·TIMER_DISC_CFM：表示等待ISDN发送呼叫释放确认消息的定时器

Failed to get timer length

获取定时器时长失败

**

【举例】

\# 使用BSV语音用户线发起呼叫，主叫号码为1000，被叫号码为2000，打开被叫侧IVA debug开关，输出调试信息如下：

\<Sysname\> debugging vioce iva all

\*Mar 26 04:32:39:829 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ISDN \--\> IVA : Received IVA_SETUP_IND message from ISDN.

*[// IVA*]*收到ISDN侧发送的呼叫建立请求消息*

\*Mar 26 04:32:39:830 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ifDChannelIndex:0x000001e1

           ifBChannelIndex:0x00011a01

           IsdnID                :0xffff0002

           ucCapability       :0x00000000

           Rate                   :0x00000010

           enStatusType    :0x0009

           ucStatusValue   :0x0000

           ucIsComplete    :0x0001

           CalledNum        :2000

           CallerNum         :1000

\*Mar 26 04:32:39:830 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Info: Failed to find CCB by IsdnId [0xffff0002.]

\*Mar 26 04:32:39:830 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Info: Create CCB succeeded, CallID=0x0001ffff

\*Mar 26 04:32:39:831 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: [0x000001e1 IVA \--\> DRV: VOICE_COMMON_GET_BSV_RELATED_IF command is sent to driver.]

*[// IVA*]*向驱动下发VOICE_COMMON_GET_BSV_RELATED_IF命令获取B通道索引*

\*Mar 26 04:32:39:831 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: [0x00011a01 IVA \--\> DRV: VOICE_COMMON_GET_BSV_RELATED_IF command is sent to driver.]

\*Mar 26 04:32:39:832 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: [0x00011a09 IVA \--\> DRV: VOICE_COM_INSTALL command is sent to driver.]

*[// IVA*]*向驱动下发VOICE_COM_INSTALL命令装配B通道*

\*Mar 26 04:32:39:832 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Fsm: Change state from [IVA_IDLE to IVA_INCONNECTBCH, CallID=0x0001ffff]

*// 改变呼叫状态，由空闲状态切换到装配B通道状态*

\*Mar 26 04:32:39:833 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Create timer TIMER_INSTALLBCH succeeded.

TimerID: 0 state:IVA_INCONNECTBCH, time length:60000ms.

\*Mar 26 04:32:39:860 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: DRV \--\> IVA : Received INSTALL_BCH_ACK message from driver, BchIfIndex=0x00011a09.

*// 收到驱动装配B通道成功的消息*

\*Mar 26 04:32:39:860 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Delete timer TIMER_INSTALLBCH success.

TimerID: 0 state:IVA_INCONNECTBCH

\*Mar 26 04:32:39:860 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: Install B channel succeeded.

\*Mar 26 04:32:39:861 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: IVA \--\> ISDN : IVA_CALLPROC_REQ message is sent to ISDN Successfully.

*[// IVA*]*向ISDN发送IVA_CALLPROC_REQ消息*

\*Mar 26 04:32:39:861 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ifDChannelIndex:0x000001e1

           ifBChannelIndex:0x00011a01

           IsdnID                :0xffff0002

           ucCapability       :0x00000000

           Rate                   :0x00000000

           enStatusType    :0x0000

           ucStatusValue   :0x0000

           ucIsComplete    :0x0000

           CalledNum        :

           CallerNum         :

\*Mar 26 04:32:39:862 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Info: Succeed in sending message to ISDN.

\*Mar 26 04:32:39:864 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: IVA \--\> CMC : ACCP_SETUP message is sent to CMC successfully.

*[// IVA*]*向CMC发送呼叫建立请求消息*

\*Mar 26 04:32:39:865 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Create timer TIMER_CMCSETUPACK succeeded.

TimerID: 0 state:IVA_INCONNECTBCH, time length:10000ms.

\*Mar 26 04:32:39:865 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Fsm: Change state from [IVA_INCONNECTBCH to IVA_INSETUP, CallID=0x0001ffff]

\*Mar 26 04:32:39:865 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: CMC \--\> IVA : Received ACCP_SETUP_ACK message from CMC.

*[// IVA*]*收到CMC发送呼叫建立请求应答消息*

\*Mar 26 04:32:39:865 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Delete timer TIMER_CMCSETUPACK successfully.

*[// IVA*]*删除等待CMC呼叫请求应答消息的定时器*

TimerID: 0 state:IVA_INSETUP

\*Mar 26 04:32:39:866 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: IVA \--\> CMC : ACCP_CHANNEL_READY message is sent to CMC successfully.

*[// IVA*]*向CMC发送ACCP_CHANNEL_READY消息*

\*Mar 26 04:32:39:866 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Create timer TIMER_CMCALERTING successfully.

TimerID: 0 state:IVA_INSETUP, time length:150000ms.

\*Mar 26 04:32:39:892 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: CMC \--\> IVA : Received ACCP_ALERTING message from CMC.

*[// IVA*]*收到CMC发送的振铃消息*

\*Mar 26 04:32:39:892 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Delete timer TIMER_CMCALERTING successfully.

TimerID: 0 state:IVA_INSETUP

\*Mar 26 04:32:39:892 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: [0x00011a09 IVA \--\> DRV: VOICE_COM_TONE_GEN_ON command is sent to driver.]

\*Mar 26 04:32:39:893 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: IVA \--\> ISDN : IVA_ALERTING_REQ message is sent to ISDN successfully.

*[// IVA*]*向ISDN发送振铃消息*

\*Mar 26 04:32:39:893 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ifDChannelIndex:0x000001e1

           ifBChannelIndex:0x00011a01

           IsdnID                :0xffff0002

           ucCapability       :0x00000001

           Rate                  :0x00000000

           enStatusType    :0x0000

           ucStatusValue   :0x0000

           ucIsComplete    :0x0000

           CalledNum        :

           CallerNum         :

\*Mar 26 04:32:39:894 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Info: Succeed in sending message to ISDN.

\*Mar 26 04:32:39:894 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Fsm: Change state from [IVA_INSETUP to IVA_INALERT, CallID=0x0001ffff]

*// 改变呼叫状态，由呼叫建立状态切换到振铃状态*

\*Mar 26 04:32:39:894 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Create timer TIMER_CMCCONNECT successfully.

TimerID: 0 state:IVA_INALERT, time length:240000ms.

\*Mar 26 04:32:42:132 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: CMC \--\> IVA : Received ACCP_CHANNEL_READY_ACK message from CMC.

\*Mar 26 04:32:42:561 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: CMC \--\> IVA : Received ACCP_CONNECT message from CMC.

*[// IVA*]*收到CMC的连接建立消息*

\*Mar 26 04:32:42:561 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Delete timer TIMER_CMCCONNECT success.

TimerID: 0 state:IVA_INALERT

\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: [0x00011a09 IVA \--\> DRV: VOICE_COM_TONE_GEN_OFF command is sent to driver.]

\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: IVA \--\> ISDN : IVA_CONN_REQ message is sent to ISDN successfully.

*[// IVA*]*向ISDN发送连接建立请求消息*

\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ifDChannelIndex:0x000001e1

           ifBChannelIndex        :0x00011a01

           IsdnID                        :0xffff0002

           ucCapability              :0x00000001

           Rate                          :0x00000000

           enStatusType           :0x0000

           ucStatusValue           :0x0000

           ucIsComplete           :0x0000

           CalledNum               :

           CallerNum                :

\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Info: Succeed in sending message to ISDN.

\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Create timer TIMER_CONN_CFM successfully.

TimerID: 0 state:IVA_INALERT, time length:6000ms.

\*Mar 26 04:32:42:589 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ISDN \--\> IVA : Received IVA_CONN_CFM message from ISDN.

\*Mar 26 04:32:42:589 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ifDChannelIndex:0x000001e1

           ifBChannelIndex:0x00011a01

           IsdnID                :0xffff0002

           ucCapability       :0x00000000

           Rate                   :0x00000000

           enStatusType    :0x0000

           ucStatusValue   :0x0000

           ucIsComplete    :0x0000

           CalledNum        :

           CallerNum         :

\*Mar 26 04:32:42:590 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Delete timer TIMER_CONN_CFM successfully.

TimerID: 0 state:IVA_INALERT

\*Mar 26 04:32:42:590 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Fsm: Change state from [IVA_INALERT to IVA_TALK, CallID=0x0001ffff]

*// 改变呼叫状态，由振铃状态切换到通话状态*

\*Mar 26 04:32:45:982 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: CMC \--\> IVA : Received ACCP_RELEASE message from CMC.

*// 收到被叫释放呼叫消息*

\*Mar 26 04:32:45:983 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: [0x00011a09 IVA \--\> DRV: VOICE_COM_UNINSTALL command is sent to driver.]

\*Mar 26 04:32:45:983 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: IVA \--\> ISDN : IVA_DISC_REQ message is sent to ISDN successfully.

*[// IVA*]*向ISDN发送释放呼叫请求消息*

\*Mar 26 04:32:45:983 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ifDChannelIndex:0x000001e1

           ifBChannelIndex:0x00011a01

           IsdnID                :0xffff0002

           ucCapability       :0x00000001

           Rate                  :0x00000000

           enStatusType    :0x0001

           ucStatusValue   :0x0010

           ucIsComplete    :0x0000

           CalledNum        :

           CallerNum         :

\*Mar 26 04:32:45:985 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Info: Succeed in sending message to ISDN.

\*Mar 26 04:32:45:985 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Fsm: Change state from [IVA_TALK to IVA_CMC_RELEASING, CallID=0x0001ffff]

\*Mar 26 04:32:45:985 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Create timer TIMER_DISC_CFM successfully.

TimerID: 0 state:IVA_CMC_RELEASING, time length:30000ms.

\*Mar 26 04:32:46:012 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ISDN \--\> IVA : Received IVA_DISC_CFM message from ISDN.

*// 收到ISDN释放呼叫确认消息*

\*Mar 26 04:32:46:012 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: ifDChannelIndex:0x000001e1

           ifBChannelIndex:0x00011a01

           IsdnID                :0xffff0002

           ucCapability       :0x00000000

           Rate                   :0x00000000

           enStatusType    :0x0001

           ucStatusValue   :0x0010

           ucIsComplete    :0x0000

           CalledNum         :

           CallerNum         :

\*Mar 26 04:32:46:013 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Event: IVA \--\> CMC : ACCP_RELEASE_COMPLETE message is sent to CMC Successfully.

\*Mar 26 04:32:46:013 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Info: Delete CCB successfully, CallID=0x0001ffff.

\*Mar 26 04:32:46:013 2027 Sysname IVA/7/IVA_DEBUG:

IVA_Timer: Delete timer TIMER_DISC_CFM successfully.

TimerID: 0 state:IVA_CMC_RELEASING

