
**可定制IVR \-- 可定制IVR调试命令 \-- debugging voice mps**

------------------------------------------------------------------------

【命令】

**[debugging voice mps **[{ **all** \| **error** \| **event** \| **info** \| **timer** }]]

**[undo debugging voice mps**[ { **all** \| **error** \| **event** \| **info** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：表示MPS（Media Play System，媒体播放系统）所有消息类型的调试信息开关。

**[error**]：表示MPS的错误类型的消息调试信息开关。

**[event**]：表示MPS的事件类消息调试信息开关。

**[fsm**]：表示MPS的状态机类消息调试信息开关。

**[info**]：表示MPS的信息类消息调试信息开关。

**[timer**]：表示MPS的定时器消息调试信息开关。

【描述】

**[debugging voice mps**]命令用来打开MPS调试信息开关。**undo debugging voice mps**命令用来关闭MPS调试信息开关。

缺省情况下，MPS调试信息开关处于关闭状态。

表1-1 debugging voice mps error命令输出信息描述表

字段

描述

Failed to start media play, media-id number is zero.

媒体放音失败，媒体文件个数为零

Failed to create MPSCB.

创建放音控制块失败

Failed to initialize MPSCB.

初始化放音控制块失败

Failed to create *timre-type* timer.

创建定时器失败，*Message-type*取值为：

·MPS_TIMER_START_PLAYMEDIA：表示媒体放音定时器

·MPS_TIMER_PSTN_WAITDELAY：表示PSTN侧延时等待定时器

·MPS_TIMER_WAIT_RELEASEMSG：表示等待释放消息定时器

Failed to get MPSCB, MPSID is invalid.

无效的MPSID值，不能得到MPS放音控制块

Failed to get PlayCB.

获取播放控制块失败

Cannot update MPSCB, it\'s playing now, PlayID = *media-id*,  UsrCallID = *caller-id*.

正在播放文件，不能更新放音控制块，媒体文件ID为*media-id*，用户ID为*caller-id*

Failed to read config, invalid DBM data type.

无效的DBM数据类型，导致读取配置失败

Fail to write DBM.

向DBM写数据失败

CodecType is invalid.

编码类型无效

Failed to get media resource by media ID, CodecType = *codetype*, MediaID = *media-id*.

根据媒体名称获取对应媒体资源失败，媒体编码类型为：*codetype*，媒体ID为：*media-id*

Failed to Get default work directory.

获取当前默认工作路径失败

Default working dir = *path*

当前默认工作路径为*path*

Failed to create cache.

创建缓冲区失败

Failed to read voice data.

读取语音数据失败

Pointer of resource control block in read control block is null.

读取控制块中的媒体资源控制块为空

Failed to delete cache node from cache-array.

从缓冲区数组中删除缓冲区节点失败

Failed to malloc for resource control block.

为资源控制块申请内存失败

Failed to send *ack-type*.

发送ACK消息失败

*[ack-type*]取值为：

·MSG_TYPE_MEDIA_PLAY_ACK：表示回复放音请求

·MSG_TYPE_MEDIA_PAUSE_ACK：表示回复暂停请求

·MSG_TYPE_MEDIA_UPDATE_ACK：表示回复更新请求

·MSG_TYPE_MEDIA_RESUM_ACK：表示回复恢复放音请求

·MSG_TYPE_MEDIA_NOTIFY_CHANGEFILE：表示切换文件

·MSG_TYPE_MEDIA_NOTIFY_OVER：表示文件播放结束

Failed to handle media-request.

处理媒体放音操作失败

表1-2 debugging voice mps event命令输出信息描述表

字段

描述

IVR\--\>MPS :*message-type*

         MPSID :*mps-id*

         Protocol : *protocol*

         SPLID : *spl-id*

         MSCID : *msc-id*

         MediaID : *media-id*

         PlayTimes : *times*

         PloadSize : *size*

         PlayType: *type*

         IfIndex : *ifindex*

         Codec : *codetype*

IVR向MPS发送消息成功

*[Message-type*]取值为：

·PLAY_MEDIA：开始放音消息

·PAUSE_MEDIA：暂停放音消息

·RESUM_MEDIA：恢复放音消息

·UPDATA_MEDIA：更新媒体消息

·NOTIFY_MEDIA_CHANGEFILE：媒体放音结束消息

·NOTIFY_MEDIA_OVER：媒体放音结束消息

·UNKNOWN_MSG：未知消息

*[SPLID*]为业务模块ID

*[MSCID*]为Media Stream Control模块ID

*[PlayTimes*]为每秒发送的编码字节数

PlayType为放音的接入方式，*PloadSize*为，*type*取值为：

·PSTN

·VoIP

Codec为音频编码类型。*codetype*取值为：

·g729r8

·g711alaw

·g711ulaw

·g723r53

MPS\--\>IVR :*message-type*

         MPSID :*mps-id*

         Protocol : *protocol*

         SPLID : *spl-id*

         MSCID : *msc-id*             

MPS向IVR发送消息成功

*[message-type *]取值为：

·PLAY_MEDIA_ACK ：开始放音消息确认

·PAUSE_MEDIA_ACK ：暂停放音消息确认

·RESUM_MEDIA_ACK：恢复放音消息确认

·UPDATA_MEDIA_ACK：更新媒体消息确认

·NOTIFY_MEDIA_CHANGEFILE：媒体放音结束消息

·NOTIFY_MEDIA_OVER：媒体放音结束消息

·UNKNOWN_MSG：未知消息

Start to play media, MediaID = *media-id*, UsrCallID = *user-id*.

开始放音 媒体文件ID为*media-id*，用户编号为*user-id*

Delete MPSCB, MPSID = *mps-id*, UsrCallID = *user-id*.

删除放音控制块，ID为*mps-id*，用户名为*user-id*

Resume playing media, MPSID = *mps-id*, MediaID = *media-id*, UsrCallID = *user-id*.

正在恢复放音，放音控制块ID为*mps-id*，媒体文件ID为*media-id*，用户编号为*user-id*

Pause to play media, MPSID = *mps-id*, MediaID = *media-id*, UsrCallID = *user-id*.

暂停放音，控制块ID为*mps-id*， 媒体文件ID为*media-id*，用户编号为*user-id*

Update media resource, MPSID = *mps-id*, MediaID = *media-id*, UsrCallID = *user-id*.

更新媒体文件，控制块ID为*mps-id*，媒体文件ID为*media-id *，用户编号为*user-id*

End playing media, MPSID = *mps-id*, MediaID = *media-id*, UsrCallID = *user-id*.

停止放音，控制块ID为*mps-id*，**媒体文件ID为*media-id*，用户编号为*user-id*

Create resource control block, CodecType = *codetype*, FileName = *file-name*.

创建文件资源控制块成功，文件编码类型为*codetype*，文件名为*file-name*

Free resource control block, CodecType = *codetype*, FileName = *file-name*

释放文件资源控制块成功，文件编码类型为*codetype*，文件名为*file-name*

Create read-control-block, CodecType = *codetype*, FileName = *file-name*

创建文件读取控制块成功，文件编码类型为*codetype*，文件名为*file-name*

表1-3 debugging voice mps info命令输出信息描述表

字段

描述

Create MPSID successfully, MPSID = *mps-id*.

创建放音控制块成功，放音控制块ID为*mps-id*

Init MPSCB successfully, MPSCB ID = *mps-id*.

初始化放音控制块成功，放音控制块ID为*mps-id*

Release  playing media successfully.

成功释放放音请求

Finish reading the data of media-file.

读取文件数据结束

Receive data from MSC.

接收到MSC模块发送的数据

Change media file. MediaId = *media-id.*

切换媒体文件，媒体文件ID为*media-id.*

表1-4 debugging voice mps timer命令输出信息描述表

字段

描述

 Create timer, TIMERID: *timer-id*, TIMERType: *timer-type*, TIMERLEN: *timer-length.*

启动定时器成功

定时器标识为*timerid*

*[timer-type*]取值为：

·MPS_TIMER_START_PLAYMEDIA：开始放音定时器

·MPS_TIMER_PSTN_WAITDELAY：PSTN侧等待线路连接延时

·MPS_TIMER_WAIT_RELEASEMSG：播放结束等待release消息*timer-length*取值为：

·MPS_TIMER_MEDIAPLAY_LEN：正在放音状态定时器时间间隔

·MPS_TIMER_WAITRELEASE_LEN：等待release消息定时器时长

·MPS_TIMER_PSTN_INIT_INTERVAL：WAITDELAY状态超时时间间隔（非R2协议）

·MPS_TIMER_PSTN_R2WAITDEL_INTERVAL：WAITDELAY状态超时时间间隔（R2协议）

Delete timer, TIMERID: *timer-id*, TIMERType: *timer-type*, TIMERLEN: *timer-length.*

成功删除定时器

定时器标识为*timerid*

*[timer-type*]取值为：

·MPS_TIMER_START_PLAYMEDIA：开始放音定时器

·MPS_TIMER_PSTN_WAITDELAY：PSTN侧等待延时

·MPS\_TIMER\_WAIT_RELEASEMSG：播放结束等待release消息*timer-length*取值为：

·MPS_TIMER_MEDIAPLAY_LEN：正在放音状态定时器时间间隔

·MPS_TIMER_WAITRELEASE_LEN：等待release消息定时器时长

·MPS_TIMER_PSTN_INIT_INTERVAL：WAITDELAY状态超时时间间隔（非R2协议）

·MPS_TIMER_PSTN_R2WAITDEL_INTERVAL：WAITDELAY状态超时时间间隔（R2协议）

【举例】

\# 使用SIP协议进行呼叫，主叫号码为987，IVR接入号为177，根节点为service节点，配置放音操作。打开被叫侧MPS debug开关，输出调试信息如下：

\<Sysname\> debugging voice mps all

*[// MPS*]*收到IVR侧发送的播放媒体文件请求消息*

\<Sysname\>\*Dec 24 19:41:23:616 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: IVR\--\>MPS : PLAY_MEDIA

         MPSID : 4294967295

         Protocol : SPL_DISCRIM_LGS

         SPLID : 1

         MSCID : 0x20100000

         MediaID : 10001

         PlayTimes : 1

         PloadSize : 30

         PlayType : PSTN

         IfIndex : 8/1

         Codec : g729r8

\*Dec 24 19:41:23:616 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: IVR\--\>MPS : PLAY_MEDIA

  MPSID : 4294967295

 Protocol : SPL_DISCRIM_LGS

         SPLID : 1

         MSCID : 0x20100000

         MediaID : 10001

         PlayTimes : 1

         PloadSize : 30

         PlayType : PSTN

         IfIndex : 8/1

         Codec : g729r8

\*Dec 24 19:41:23:616 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Start to play media, MediaID = 10001 UsrCallID = 1.

\*Dec 24 19:41:23:616 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: Create MpsCb successfully, MpsCb id = 1.

\*Dec 24 19:41:23:617 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

*// 创建资源控制块*

\*Dec 24 19:41:23:617 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Create resource control block, CodecType = 0, FileName = cfa0:/g729r8

/i_g729r8.wav.

*// 创建读取控制块*

\*Dec 24 19:41:23:618 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Create read-control-block, CodecType = 0, PayloadSize = 30, MediaName

 = cfa0:/g729r8/i_g729r8.wav.

\*Dec 24 19:41:23:618 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Timer: Create timer, TmrId: 0, TmrType: MPS_TIMER_PSTN_WAITDELAY, TmrLen: 30

0.

\*Dec 24 19:41:23:618 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: Init MpsCb successfully, MpsCb id = 1.

*// 创建放音定时器*

\*Dec 24 19:41:23:618 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Timer: Create timer, TmrId: 1, TmrType: MPS_TIMER_START_PLAYMEDIA, TmrLen: 1

0.

\*Dec 24 19:41:23:921 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Timer: Delete timer after PSTN wait delay, TmrId: 0, TmrType: MPS_TIMER_PSTN

\_WAITDELAY, TmrLen: 300.

\*Dec 24 19:41:23:921 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Wait delay process successfully, Play state = 1, Pstn state = 2

\*Dec 24 19:41:23:941 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

*// 开始发送语音数据包，每500个包输出一次信息*

**

\*Dec 24 19:41:23:942 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 1, MediaID = 1000

1, UsrCallID = 1.

\*Dec 24 19:41:38:911 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 500, MediaID = 10

001, UsrCallID = 1.

\*Dec 24 19:41:53:911 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 1000, MediaID = 1

0001, UsrCallID = 1.

\*Dec 24 19:42:08:911 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 1500, MediaID = 1

0001, UsrCallID = 1.

\*Dec 24 19:42:23:911 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 2000, MediaID = 1

0001, UsrCallID = 1.

\*Dec 24 19:42:38:911 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 2500, MediaID = 1

0001, UsrCallID = 1.

\*Dec 24 19:42:53:911 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 3000, MediaID = 1

0001, UsrCallID = 1.

\*Dec 24 19:42:56:101 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

*// 文件数据读取结束*

\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: Finish reading the data of media-file.

*// 释放读取控制块*

\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Free reading control block, CodecType = 0, MediaName = cfa0:/g729r8/i

\_g729r8.wav.

*// 释放资源控制块*

\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Free resource control block, CodecType = 0, MediaName = cfa0:/g729r8/

i_g729r8.wav.

\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

*[// MPS*]*向IVR发送播放当前文件成功播放结束的MPCP消息*

\*Dec 24 19:43:07:022 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Media file has been played completely.

*// 发送播放结束消息*

\*Dec 24 19:43:07:022 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: MPS\--\>IVR : NOTIFY_MEDIA_OVER

         MPSID = 1

         SPLID = 1

         ProcResult: Success

\*Dec 24 19:43:07:022 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Timer: Create timer, TmrType: MPS_TIMER_WAIT_RELEASEMSG, TmrLen: 10000.

*[// MPS*]*接收IVR发送的更新媒体文件的MPCP消息，MPS接受到消息后开始更新文件*

\*Dec 24 19:43:07:023 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: IVR\--\>MPS : UPDATE_MEDIA

         MPSID : 1

         Protocol : SPL_DISCRIM_LGS

         SPLID : 1

         MSCID : 0x20100000

         MediaID : 10002

         PlayTimes : 2

         PloadSize : 30

         PlayType : PSTN

         IfIndex : 8/1

         Codec : g729r8

\*Dec 24 19:43:07:023 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: IVR\--\>MPS : UPDATE_MEDIA

         MPSID : 1

         Protocol : SPL_DISCRIM_LGS

         SPLID : 1

         MSCID : 0x20100000

         MediaID : 10002

         PlayTimes : 2

         PloadSize : 30

         PlayType : PSTN

         IfIndex : 8/1

         Codec : g729r8

\*Dec 24 19:43:07:023 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Update media resource, MpsId = 1, MediaID = 10002, UsrCallID = 1.

\*Dec 24 19:43:07:023 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

\*Dec 24 19:43:07:024 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Create resource control block, CodecType = 0, FileName = cfa0:/g729_o

p2.wav.

\*Dec 24 19:43:07:024 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Create read-control-block, CodecType = 0, PayloadSize = 30, MediaName

 = cfa0:/g729_op2.wav.

*[// MPS*]*接收IVR发送的恢复放音的MPCP消息，MPS放音标志置位，开始准备放音*

\*Dec 24 19:43:07:027 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: IVR\--\>MPS : RESUM_MEDIA

         MPSID : 1

         Protocol : SPL_DISCRIM_LGS

         SPLID : 1

         ResumeType : reset

         MSCID : 0x20100000

         MediaID : 10002

         PlayTimes : 2

         PloadSize : 30

         PlayType : PSTN

         IfIndex : 8/1

         Codec : g729r8

\*Dec 24 19:43:07:027 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: IVR\--\>MPS : RESUM_MEDIA

         MPSID : 1

         Protocol : SPL_DISCRIM_LGS

         SPLID : 1

         ResumeType : reset

         MSCID : 0x20100000

         MediaID : 10002

         PlayTimes : 2

         PloadSize : 30

         PlayType : PSTN

         IfIndex : 8/1

         Codec : g729r8

\*Dec 24 19:43:07:027 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Resume playing media, MpsId = 1, MediaID = 10002, UsrCallID = 1.

\*Dec 24 19:43:07:051 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

\*Dec 24 19:43:07:051 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 1, MediaID = 1000

2, UsrCallID = 1.

\*Dec 24 19:43:17:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Timer: Delete timer, TmrId: 0, TmrType: MPS_TIMER_WAIT_RELEASEMSG, TmrLen: 0

.

\*Dec 24 19:43:22:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 500, MediaID = 10

002, UsrCallID = 1.

\*Dec 24 19:43:37:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 1000, MediaID = 1

0002, UsrCallID = 1.

\*Dec 24 19:43:52:021 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Send voice packet by media-channel 9, PacketCount = 1500, MediaID = 1

0002, UsrCallID = 1.

\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: Finish reading the data of media-file.

\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Free reading control block, CodecType = 0, MediaName = cfa0:/g729_op2

.wav.

\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Free resource control block, CodecType = 0, MediaName = cfa0:/g729_op

2.wav.

\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: No elements in array.

\*Dec 24 19:44:06:962 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Media file has been played completely.

*[// MPS*]*向IVR发送MPCP消息，表示结束播放当前文件*

\*Dec 24 19:44:06:962 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: MPS\--\>IVR : NOTIFY_MEDIA_OVER

 MPSID = 1

         SPLID = 1

         ProcResult: Success

\*Dec 24 19:44:06:965 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: Receive data from Msc.

\*Dec 24 19:44:06:965 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Timer: Delete timer, TmrId: 1, TmrType: MPS_TIMER_START_PLAYMEDIA, TmrLen: 1

0.

*[// MPS*]*接收IVR发送的释放放音消息*

\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: IVR\--\>MPS : RELEASE_MEDIA

         MPSID : 1

         Protocol : SPL_DISCRIM_LGS

         SPLID : 1

\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: IVR\--\>MPS : RELEASE_MEDIA

         MPSID : 1

         Protocol : 0

         SPLID : 1

\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: End playing media, MpsId = 1, MediaID = 10002, UsrCallID = 1.

*// 删除放音定时器*

\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Timer: Delete timer, TmrId: 0, TmrType: MPS_TIMER_WAIT_RELEASEMSG, TmrLen: 0

*// 删除放音控制块*

.

\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Event: Delete MpsCb, MpsId = 1, UsrCallID = 1.

*// 释放放音请求成功，停止放音*

\*Dec 24 19:44:06:967 2013 Sysname MPS/7/MPS_DEBUG:

MPS_Info: Release playing media successfully.

**可定制IVR \-- 可定制IVR调试命令 \-- debugging voice ivr**

------------------------------------------------------------------------

【命令】

**[debugging vioce ivr **[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

**[undo debugging voice ivr**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：表示IVR所有消息类型的调试信息开关。

**[error**]：表示IVR的错误类型的消息调试信息开关。

**[event**]：表示IVR的事件类消息调试信息开关。

**[fsm**]：表示IVR的状态机类消息调试信息开关。

**[info**]：表示IVR的信息类消息调试信息开关。

**[timer**]：表示IVR的定时器消息调试信息开关。

【描述】

**[debugging voice ivr**]命令用来打开IVR调试信息开关。**undo debugging voice ivr**命令用来关闭IVR调试信息开关。

缺省情况下，IVR调试信息开关处于关闭状态。

表1-5 debugging voice ivr error命令输出信息描述表

字段

描述

Failed to allocate memory for *module*.

为*module*分配内存失败

Protocal is not supported, Protocal = *protocal*.

不支持协议类型，该协议类型为*protocal.*

表1-6 debugging voice ivr event命令输出信息描述表

字段

描述

CMC \--\> IVR : ACCP_CHANNEL_READY_ACK.

IVR收到CMC发送的Accp Channel Ready Ack消息

CMC \--\> IVR : ACCP_FAX_VOICE_SWITCH.

IVR收到CMC发送的Accp Fax Voice Switch消息

CMC \--\> IVR : ACCP\_INFORMATION.

IVR收到CMC发送的Accp Information消息

CMC \--\> IVR : ACCP\_SERVICE.

IVR收到CMC发送的Accp Service消息

CMC \--\> IVR : ACCP_SERVICE_ACK.

IVR收到CMC发送的Accp Service Ack消息

CMC \--\> IVR : ACCP_RELEASE.

IVR收到CMC发送的Accp Release消息

CMC \--\> IVR : ACCP_RELEASE_COMPLETE.

IVR收到CMC发送的Accp Release Complete消息

IVR \--\> CMC: ACCP_SETUPACK.

IVR发送Accp Setup Ack消息到CMC

IVR \--\> CMC: ACCP\_ ALERT.

IVR发送Accp Alerting消息到CMC

IVR \--\> CMC: ACCP_CONNECT.

IVR发送Accp Connect消息到CMC

IVR \--\> CMC: ACCP_INFORMATION.

IVR发送Accp Information消息到CMC

IVR \--\> CMC: ACCP_RELEASE.

IVR发送Accp Release消息到CMC

IVR \--\> CMC: ACCP_RELCOMP.

IVR发送Accp Release Complete消息到CMC

IVR \--\> CMC: ACCP_CHANNEL_READY.

IVR发送Accp Channel Ready消息到CMC

IVR \--\> CMC: ACCP_FAXVOCSWCH_ACK.

IVR发送Accp Fax Voice Switch Ack消息到CMC

IVR \--\> CMC: ACCP_SERVICE.

IVR发送Accp Service消息到CMC

IVR \--\> CMC: ACCP_SRVACK.

IVR发送Accp Service Ack消息到CMC

CMC \--\> IVR : ACCP_SETUP.

IVR收到CMC发送的Accp Setup消息

IVR \--\> DPL : DPL_ROUTE_REQ.

IVR向DPL发送查询实体的请求

IVR \--\> MPS : End playing media.

IVR向MPS发送结束放音的请求

Send synchronized-request to MPU.

发送主备倒换响应给主控板

DPL \--\> IVR : DPL_ROUTE_RSP.

DPL将查询实体的结果发给IVR

表1-7 debugging voice ivr fsm命令输出信息描述表

字段

描述

*[statusA* \--\> *statusB*, CallId = *idA*, LocalId = *idB*.]

IVR呼叫状态变迁：由*statusA*状态变迁到*statusB*状态，CallId为*idA*，LocalId为*idB*

*[state-type *]取值为：

·IVA_IDLE：表示正处于空闲状态

·IVA_INCONNECTBCH ：表示正处于装配B通道的状态

·IVA_TALK：表示正处于通话

·IVA_CMC_RELEASING：表示正处于CMC拆线状态

表1-8 debugging voice ivr info命令输出信息描述表

字段

描述

Cannot get entity by number, LocalId = *localId*.

本地呼叫ID达到最大值，LocalId为localId

Input error, RepeatTimes = *repeatTimes*, InputErrorTimes = *errorTimes*.

输入错误，可重试次数为*repeatTimes*次，输入错误次数为*errorTimes*次

Call state is invalid, CallId = id.

呼叫状态是无效状态，CallId为id

Timeout, RepeatTimes = *repeat-time*, TimeoutTimes ＝*error-times*.

等待输入超时，可重复超时次数为*repeat-times*,，已经超时次数为*error-times*

Jump configure is invalid, NodeId = id.

Jump节点配置无效

Call configure is invalid, NodeId = id.

Call节点配置无效

Service configure is invalid, NodeId = id.

Service节点配置无效

表1-9 debugging voice ivr timer命令输出信息描述表

字段

描述

Failed to create timer *type*.

创建定时器失败，该定时器类型为*type*

*[type*]的类型为：

·IVR_TIMER_INVALID_TYPE：呼叫定时器

·IVR_TIMER_WAIT_CHYACK：IVR等待CHANNEL_READY消息定时器

·IVR_TIMER_WAIT_SRVACK：IVR等待SERVICE_ACK消息定时器

·IVR_TIMER_WAIT_RELCOM：IVR等待RELEASE_COMPLATE消息定时器

·IVR_TIMER_OMIT_INFORMATION：IVR忽略INFORMATION消息定时器节点定时器类型

·IVR_TIMER_JUMP_WAIT_INPUT：Jump节点下等待用户按键

·IVR_TIMER_CALL_FIRST_DIAL：Call节点下首次按键定时器

·IVR_TIMER_CALL_DIAL_INTERVAL：Call节点下按键间隙定时器

·WAIT_MPS_ACK：等待MPS响应定时器

Start timer, TmrId = *id*, TmrType = *type*, TmrLength = *length*.

启动定时器，定时器Id为*id*，定时器类型为*type*，定时器间隔为*length*毫秒

*[type*]的类型为：

·IVR_TIMER_INVALID_TYPE：呼叫定时器

·IVR_TIMER_WAIT_CHYACK：IVR等待CHANNEL_READY消息定时器

·IVR_TIMER_WAIT_SRVACK：IVR等待SERVICE_ACK消息定时器

·IVR_TIMER_WAIT_RELCOM：IVR等待RELEASE_COMPLATE消息定时器

·IVR_TIMER_OMIT_INFORMATION：IVR忽略INFORMATION消息定时器节点定时器类型

·IVR_TIMER_JUMP_WAIT_INPUT：Jump节点下等待用户按键

·IVR_TIMER_CALL_FIRST_DIAL：Call节点下首次按键定时器

·IVR_TIMER_CALL_DIAL_INTERVAL：Call节点下按键间隙定时器

·WAIT_MPS_ACK：等待MPS响应定时器

Delete timer, TmrId = *id,* TmrType = *type*.

删除定时器，定时器Id为*id*，定时器类型为*type*

*[type*]的类型为：

·IVR_TIMER_INVALID_TYPE：呼叫定时器

·IVR_TIMER_WAIT_CHYACK：IVR等待CHANNEL_READY消息定时器

·IVR_TIMER_WAIT_SRVACK：IVR等待SERVICE_ACK消息定时器

·IVR_TIMER_WAIT_RELCOM：IVR等待RELEASE_COMPLATE消息定时器

·IVR_TIMER_OMIT_INFORMATION：IVR忽略INFORMATION消息定时器节点定时器类型

·IVR_TIMER_JUMP_WAIT_INPUT：Jump节点下等待用户按键

·IVR_TIMER_CALL_FIRST_DIAL：Call节点下首次按键定时器

·IVR_TIMER_CALL_DIAL_INTERVAL：Call节点下按键间隙定时器

·WAIT_MPS_ACK：等待MPS响应定时器

**

【举例】

\#用户0101003先拨打IVR接入号915，再二次呼叫号码为914的用户。IVR的根节点是Call节点，节点ID为103，并配置以 \# 为结束符的普通二次呼叫。打开IVR所有调试开关，用户0101003拨打IVR接入号915，debug信息显示如下。

\<Sysname\> debugging vioce ivr all

\*Dec 24 10:48:07:086 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: CMC \--\> IVR : ACCP_SETUP      CallID = 0x00000009 LocalID = 0xfffffff

f

      Called Number\...915

      Caller Number\...0101003

      Source IfIndex..0x00000281

      InfoTableIndex..0x00000000

      DialPeer Info\...None Codec Transport

                      Entity   Index: 915

                      DialPeer  Type: IVR

                      Codec     Type: G729r8 G711a G711u G723-53

*[// IVR*]*接收到CMC发送的ACCP_SETUP消息*

\*Dec 24 10:48:07:087 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> CMC : ACCP_SETUP_ACK  CallID = 0x00000009 LocalID = 0x0000000

2

*[// IVR*]*向CMC发送ACCP_SETUP_ACK消息*

\*Dec 24 10:48:07:087 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> CMC : ACCP_ALERTING   CallID = 0x00000009 LocalID = 0x0000000

2

      Target IfIndex..0x00000281

      Inband info\.....Avail

      InfoTableIndex..0x00000000

*[// IVR*]*向CMC发送ACCP_ALERTING消息*

\*Dec 24 10:48:07:087 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> CMC : ACCP_CONNECT    CallID = 0x00000009 LocalID = 0x0000000

2

      Target IfIndex..0x00000000

      Inband info\.....Unavail

      InfoTableIndex..0x00000000

*[// IVR*]*向CMC发送ACCP_CONNECT消息*

\*Dec 24 10:48:07:088 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> CMC : ACCP_CHANNEL_READY      CallID = 0x00000009 LocalID = 0

x00000002

      DecodeProtocol..G729r8

      EncodeProtocol..G729r8

      Vad Switch\...\...Disable

      Local Ecan\...\...Off

      Distance Ecan\...None

      PT Type\...\...\...None

      PayLoadSize\.....30

      IP media DSCP\...0

      Update type\.....MEDIA_CHANNEL_CONNECT

*[// IVR*]*向CMC发送ACCP_CHANNEL_READY消息，用来通知CMC，IVR的媒体通道已经准备完成*

\*Dec 24 10:48:07:088 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_CHYACK, TmrLength =

150000.

*[// IVR*]*启动等待ACCP_CHANNEL_READY_ACK消息定时器，用来防止CMC无响应*

\*Dec 24 10:48:07:088 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Fsm: IDLE \--\> WAIT_CHY_ACK, CallId = 9, LocalId = 2.

*[// IVR*]*的状态由初始状态转变为等待ACCP_CHANNEL_READY_ACK消息状态*

\*Dec 24 10:48:07:094 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: CMC \--\> IVR : ACCP_CHANNEL_READY_ACK  CallID = 0x00000009 LocalID = 0

x00000002

      DecodeProtocol..G729r8

      EncodeProtocol..G729r8

      Vad Switch\...\...Disable

      Local Ecan\...\...None

      Distance Ecan\...None

      PT Type\...\...\...None

      PayLoadSize\.....30

      IP media DSCP\...0

      DialPeer Info\...None Codec Transport

                      Entity   Index: 915

                      DialPeer  Type: IVR

                      Codec     Type: G729r8 G711a G711u G723-53

*[// IVR*]*收到CMC发送过来的ACCP_CHANNEL_READY_ACK 消息，IVR收到CMC发送ACK，表示媒体通道准备完成*

\*Dec 24 10:48:07:094 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_CHYACK.

*[// IVR*]*删除等待ACCP_CHANNEL_READY_ACK消息定时器*

\*Dec 24 10:48:07:094 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> CMC : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0

x00000002

*[// IVR*]*收到CMC发送ACCP_INFORMATION 消息*

\*Dec 24 10:48:07:095 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Fsm: WAIT_CHY_ACK \--\> ACTIVE, CallId = 9, LocalId = 2.

*[// IVR*]*的状态由等待ACCP_CHANNEL_READY_ACK消息状态转变为通话已建立状态*

\*Dec 24 10:48:07:095 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_OMIT_INFORMATION, TmrLeng

th = 500.

*[// IVR*]*启动忽略按键消息定时器*

\*Dec 24 10:48:07:610 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: IVR_TIMER_OMIT_INFORMATION timer timed out in NODE_IDLE state.

*[// IVR*]*忽略按键消息定时器在执行流程初始状态超时*

\*Dec 24 10:48:07:610 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_OMIT_INFORMATION.

*[// IVR*]*删除忽略按键消息定时器*

\*Dec 24 10:48:07:610 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Info: The node id is not in the stack, NodeId = 103.

*[//*]*节点id不在栈中，即该节点尚未保存在临时空间里*

\*Dec 24 10:48:07:611 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_FIRST_DIAL, TmrLengt

h = 3000.

*[// IVR*]*启动首次按键定时器*

\*Dec 24 10:48:07:611 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Info: NODE_IDLE \--\> CALL_WAIT_INPUT, LocalId = 2.

*[// IVR*]*节点状态由初始状态转变为Call节点等待输入状态*

\*Dec 24 10:48:09:665 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: CMC \--\> IVR : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0

x00000002

      DTMF Character..9

*[// IVR*]*收到CMC发送的ACCP_INFORMATION消息，输入按键号码为9*

\*Dec 24 10:48:09:665 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_FIRST_DIAL.

*[// IVR*]*删除首次按键定时器*

\*Dec 24 10:48:09:665 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL, TmrLe

ngth = 10000.

*[// IVR*]*启动按键间隔定时器*

\*Dec 24 10:48:09:665 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Info: CALL_WAIT_INPUT \--\> CALL_WAIT_INPUT, LocalId = 2.

*[// IVR*]*节点状态保持call节点等待输入状态*

\*Dec 24 10:48:10:415 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: CMC \--\> IVR : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0

x00000002

      DTMF Character..1

*[// IVR*]*收到CMC发送过来的ACCP_INFORMATION消息，输入按键号码为1*

\*Dec 24 10:48:10:415 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL.

*[// IVR*]*删除按键间隔定时器*

\*Dec 24 10:48:10:415 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL, TmrLe

ngth = 10000.

*[// IVR*]*启动按键间隔定时器*

\*Dec 24 10:48:10:416 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Info: CALL_WAIT_INPUT \--\> CALL_WAIT_INPUT, LocalId = 2.

*[// IVR*]*节点状态保持call节点等待输入状态*

\*Dec 24 10:48:11:585 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: CMC \--\> IVR : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0

x00000002

      DTMF Character..4

*[// IVR*]*收到CMC发送过来的ACCP_INFORMATION消息，此时二次呼叫号码914已全部输入*

\*Dec 24 10:48:11:585 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL.

*[// IVR*]*删除按键间隔定时器*

\*Dec 24 10:48:11:585 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL, TmrLe

ngth = 10000.

*[// IVR*]*启动按键间隔定时器*

\*Dec 24 10:48:11:585 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Info: CALL_WAIT_INPUT \--\> CALL_WAIT_INPUT, LocalId = 2.

*[// IVR*]*节点状态保持Call节点等待输入状态*

\*Dec 24 10:48:15:215 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: CMC \--\> IVR : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0

x00000002

      DTMF Character..#

*[// IVR*]*收到CMC发送过来的ACCP_INFORMATION消息，输入按键号码为\#*

\*Dec 24 10:48:15:215 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL.

*[// IVR*]*删除按键间隔定时器*

\*Dec 24 10:48:15:216 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> DPL : DPL_ROUTE_REQ.

*[// IVR*]*向DPL发出查询实体请求*

\*Dec 24 10:48:15:216 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL, TmrLe

ngth = 10000.

*[// IVR*]*启动按键间隔定时器，来等待DPL查询结果*

\*Dec 24 10:48:15:216 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Info: CALL_WAIT_INPUT \--\> CALL_WAIT_ENTITY, LocalId = 2.

*[// IVR*]*状态由call节点等待输入状态转变为等待查询实体状态*

\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: DPL \--\> IVR : DPL_ROUTE_RSP.

*[// IVR*]*收到DPL返回的查询实体结果*

\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL.

*[// IVR*]*删除按键间隔定时器*

\*Dec 24 12:46:20:881 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Info: CALL_WAIT_INPUT \--\> CALL, LocalId = 5.

*[// IVR*]*节点状态由等待按键输入转变为二次呼叫状态*

\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_SRVACK, TmrLength =

20000.

*[// IVR*]*启动等待SERVICE_ACK定时器*

\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> CMC : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0

x00000002

*[// IVR*]*向CMC发送ACCP_INFORMATION消息*

\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> CMC : ACCP_SERVICE    CallID = 0x00000009 LocalID = 0x0000000

2

*[// IVR*]*向CMC发送ACCP_SERVICE消息，向CMC请求语音业务*

\*Dec 24 10:48:15:219 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Fsm: ACTIVE \--\> WAIT_SERVICE_ACK, CallId = 9, LocalId = 2.

*[// IVR*]*状态由活动状态变为等待WAIT_SERVICE_ACK消息状态*

\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: CMC \--\> IVR : ACCP_SERVICE_ACK        CallID = 0x00000009 LocalID = 0

x00000002

*[// IVR*]*收到CMC发送的ACCP_SERVICE_ACK消息*

\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_SRVACK.

*[// IVR*]*删除等待SERVICE_ACK定时器*

\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Info: Service response status is ok, CallId = 9.

*// 语音业务请求成功*

****

\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> CMC : ACCP_RELEASE    CallID = 0x00000009 LocalID = 0x0000000

2

      ReleaseCause\....Normal clearing!

*[// IVR*]*向CMC发送ACCP_RELEASE消息，发送ACCP_RELEASE消息的原因是正常释放*

\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_RELCOM, TmrLength =

6000.

*// 启动等待Accp Release Complete消息的定时器*

\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Fsm: ACTIVE \--\> RELEASE, CallId = 9, LocalId = 2.

*// 呼叫状态机由WAIT_SERVICE_ACK改变为RELEASE*

\*Dec 24 10:48:15:225 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: CMC \--\> IVR : ACCP_RELEASE_COMPLETE   CallID = 0x00000009 LocalID = 0

x00000002

*// 接收到CMC模块向IVR模块发送Accp Release Complete消息*

\*Dec 24 10:48:15:225 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_RELCOM.

*// 删除等待Accp Release Complete消息的定时器*

\*Dec 24 10:48:15:225 2013 Sysname IVR/7/IVR_DEBUG:

IVR_Event: IVR \--\> DPL : DPL_DELETE_TABINDEX.

*// IVR向DPL发送DPL_DELETE_TABINDEX消息，DPl可以删除临时查询表*

**
