<!-- CMD-INDEX
  debugging mpls bfd                  | 用户视图             | L5
-->

**MPLS OAM \-- MPLS OAM调试命令 \-- debugging mpls bfd**

------------------------------------------------------------------------

【命令】

**[debugging mpls bfd **[{ **all** \| **error** \| **event** \| **hsb** \| **packet** \| **process** }]]

**[undo debugging mpls bfd **[{ **all** \| **error** \| **event** \| **hsb** \| **packet** \| **process** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示MPLS BFD的所有调试信息开关。

**[error**]：表示MPLS BFD的错误调试信息开关。

**[event**]：表示MPLS BFD的事件调试信息开关。

**[hsb:**]表示MPLS BFD热备份事件的调试信息开关。

**[packet**]：表示MPLS BFD消息调试信息开关。

**[process**]：表示MPLS BFD处理过程调试信息开关。

【描述】

**[debugging mpls bfd**]命令用来打开MPLS BFD的调试信息开关。**undo** **debugging mpls bfd**命令用来关闭MPLS BFD的调试信息开关。

缺省情况下，MPLS BFD的调试信息开关处于关闭状态。

表1-1 debugging mpls bfd error命令输出信息描述表

字段

描述

No enough memory.

没有足够内存

Not enough resources are available to complete the operation..

没有足够资源，如discriminator或Session Index已全被占用

Invalid parameter.

无效参数

Session (*session*) received wrong session event (*event*) in *state* state*.

会话（*session*）在状态（*state*）时接收到错误的会话事件，事件类型为*event*

*[session*]取值包括：

·Type: LSP; FEC: *addr*/*masklen*; EntryKey: *entrykey*：表示该会话用来检测LSP，FEC目的地址和掩码长度为*addr*/*masklen*，EntryKey为*entrykey*

·Type: TE; IfIndex: *ifindex*; EntryKey: *entrykey*：表示该会话用来检测MPLS TE隧道，MPLS TE隧道对应的隧道接口索引为*ifindex*，EntryKey为*entrykey*

·Type: PW; Peer: *peer-ip*; PWID: *pw-id*; EntryKey: *key*：表示该会话用来检测PW，对端PE的地址为*peer-ip*，PW ID为*pw-id*，EntryKey为*entrykey*

会话状态*state*取值包括INIT、DOWN和UP

会话事件*event*取值包括：

·REQUEST_TIMEOUT：表示request定时器超时

·AGE_TIMEOUT：表示老化定时器超时

·DELAYNTF_TIMEOUT：表示延迟通知定时器超时

·CHGENCAP_TIMEOUT：表示更新封装定时器超时

·CREATE_SSN：表示创建会话

·UPDATE_SSN：表示更新会话

·DELETE_SSN：表示删除会话

·RECEIVE_REPLY：表示收到echo reply报文

·RECEIVE_REQUEST：表示收到echo request报文

·BFD_SSNUP：表示BFD会话UP

·BFD_SSNDOWN：表示BFD会话DOWN

·BFD_SSNADMINDOWN：表示BFD会话被配置删除

·BFD_SSNINITFAIL：表示BFD会话初始化失败

Failed to connect to BFD.

与BFD进程建立连接失败

Received an invalid signaling message.

接收到一个无效消息

Failed to send an HA message (*message*).

发送HA消息失败，消息类型为*message*

*[message*]取值包括：

·0：表示批量备份

·1：表示实时备份

Failed to respond to HA. Event: *event*

回应HA事件失败，事件类型为*event*

*[event*]取值包括：

·0：表示HA模块去激活完成

·1：表示批量备份完成

·2：表示备板升级完成

Failed to activate HA.

HA模块激活失败

Failed to create the timer.

创建定时器失败

Failed to set the timer value.

设置定时器时间间隔失败

Failed to start the timer.

启动定时器失败

Failed to process state machine event (*event*)*.

处理状态机事件失败，事件类型为*event*

*[event*]取值包括：

·0：表示下发创建BFD会话

·1：表示下发删除BFD会话

·2：表示下发更新BFD会话

·3：表示发送echo request消息

·4：表示发送echo reply消息

·5：表示删除MBFD会话

·6：表示获取封装信息

Failed to process echo reply message because the reply return code is *code.*

处理echo reply消息失败：reply返回码为*code*

Failed to process echo reply message. Can\'t get session through the message.

处理echo reply消息失败：通过该消息未获取到相应会话

Failed to process echo reply message because sequence number doesn't match.

处理echo reply消息失败：Sequence number不匹配

Failed to process echo reply message because FEC doesn't match.

处理echo reply消息失败：FEC不匹配

表1-2 debugging mpls bfd event命令输出信息描述表

字段

描述

Responded HA with an event (*event*)*.

回应HA事件，事件类型为*event*

*[event*]取值包括：

·0：表示HA模块去激活完成

·1：表示批量备份完成

·2：表示备板升级完成

Received an HA event (*event*)*.

接收到一个HA事件，事件类型为*event*

*[event*]取值包括：

·0：表示HA模块去激活完成

·1：表示批量备份完成

·2：表示备板升级完成

·3：表示主板降级完成

Session (*session*) received session event (*event*) in *state* state.

会话（*session*）在状态（*state*）时接收到会话事件，事件类型为*event*

Received APP event (*event*)*.

接收到来自MPLS BFD应用（如LSM模块、L2VPN模块）的事件*event*

*[event*]取值包括：

·17：表示创建会话

·18：表示删除会话

·19：表示设置LSR ID

·20：表示GR

·21：表示更新会话

表1-3 debugging mpls bfd hsb命令输出信息描述表

字段

描述

Sent an HA message (*message).*

发送一个HA消息，类型为*message*

*[message*]取值包括：

·0：表示批量备份

·1：表示实时备份

Received an HA message (*message).*

接收一个HA消息，类型为*message*

*[message*]取值包括：

·0：表示批量备份

·1：表示实时备份

表1-4 debugging mpls bfd packet命令输出信息描述表

字段

描述

Received message (*message*). *fec*; discriminator: *discriminator*

为*fec*接收到*message*消息，discriminator为*discriminator*

*[message*]取值包括Request和Reply

*[fec*]取值包括：

·Type: LSP; FEC: *addr*/*masklen*：表示通过BFD会话检测LSP，FEC目的地址和掩码长度为*addr*/*masklen*

·Type: TE; IfIndex:*ifindex*：表示通过BFD会话检测MPLS TE隧道，MPLS TE隧道对应的隧道接口索引为*ifindex*

·Type: PW; Peer: *peer**-ip*; PWID: *pw**-id*：表示通过BFD会话检测PW，对端PE的地址为*peer-ip*，PW ID为*pw-id*

Sent message (*message*). *fec*

为*fec*发送*message*消息

*[message*]取值包括Request和Reply

Sent message (*message*). *session*

为*session*发送*message*消息

*[message*]取值包括Request和Reply

Received an echo reply message. Returned information: *information*

接收到Echo reply消息，回应信息为*information*

Received an echo reply message. Downstream information: *information*; nexthop: *nexthop*; label: *label*

接收到Echo reply消息，下游信息为*information*，下一跳地址为*nexthop*，标签为*label*

表1-5 debugging mpls bfd process命令输出信息描述表

字段

描述

Added session (*session*) to BFD.

在BFD进程中创建BFD会话*session*

Deleted session (*session*) from BFD.

从BFD进程中删除BFD会话*session*

Updated session (*session*) in BFD

更新BFD进程中的会话*session*

Created MBFD session (*session*). Index: *index*

创建MBFD会话*session*，会话索引为*index*

Destroyed MBFD session (*session*). Index: *index*

删除MBFD会话*session*，会话索引为*index*

Allocated local discriminator (*discriminator*).

分配本地标识符*discriminator*

Freed local discriminator (*discriminator*).

释放本地标识符*discriminator*

Started timer (*type*). ID: *id*

开启*type*类型定时器，定时器ID为*id*

*[type*]取值包括：

·0：表示request定时器

·1：表示老化定时器

·2：表示通知定时器

·3：表示更新封装定时器

Session (*session*) state changed from *old* to *new.*

会话*session*状态由*old*变为*new*

*[old*]和*new*取值包括INIT、DOWN和UP

Sent message to BFD. VRF: *vrf*; type: *type*; entry key: *key*; result: *result*

发送消息到BFD进程，VRF为*vrf*，BFD检测的隧道类型为*type*，Entry Key为*key*，结果为*result*

*[type*]取值包括：

·32：表示通过BFD会话检测LSP

·64：表示通过BFD会话检测MPLS TE隧道

·128：表示通过BFD会话检测PW

*[result*]取值包括：

·0：表示成功

·其他值表示失败

Sent session (*session*) state changed message to APP. Current session state: *state*

向MPLS BFD应用发送会话*session*状态变化消息，当前会话状态为*state*

*[state*]取值包括：

·1：表示UP

·2：表示DOWN

Echo request not send due to no LSR-ID.

由于没有LSR-ID，不发送echo request消息

Ignored the received echo request message due to lack of LSR-ID.

由于没有LSR-ID，接收到echo request消息不做任何操作

Ignored the received echo request message because no route found for sending echo reply.

由于没有路由发送echo reply，接收到echo request消息不做任何操作

Added periodic trace route. *fec*

开始*fec*的周期性Trace route

Deleted periodic trace route. *fec*

结束*fec*的周期性Trace route

Ingored periodic trace route due to no route.

由于没有路由，忽略周期性Trace route操作

Started detecting. *fec*

开始检测*fec*

Detection information: NextHop *nexthop*, attempt count: *count*, TTL *ttl*

检测相应信息，下一跳地址为*nexthop*，尝试次数为*count*，TTL为*ttl*

Periodic traceroute detected an LSP failure and notified BFD of the failure. *fec*; nexthop: *nexthop*.

周期性Trace route检测到*fec*、下一跳地址为*nexthop*的LSP存在故障，并通知BFD

【举例】

\# 打开MPLS BFD的错误调试信息开关。关闭BFD进程时，设备上会打印如下调试信息

\<Sysname\> debugging mpls bfd error

\<Sysname\> process shutdown name bfdd

\*Jun 29 00:37:13:758 2012 Sysname MBFD/7/ERROR: -MDC=1; Failed to connect to BFD.

*// 与BFD进程建立连接失败。*

\# 打开MPLS BFD的事件调试信息开关，配置通过BFD检测LSP后，如果设备上存在对应的LSP，则会打印如下调试信息。

\<Sysname\> debugging mpls bfd event

\<Sysname\> system-view

Sysname mpls bfd

Sysname mpls bfd 22.22.2.2 32

\*Jun 29 12:21:09:494 2012 Sysname MBFD/7/EVENT: -MDC=1; Received APP event (17).

*// 接收到MPLS BFD应用的会话创建事件。*

\*Jun 29 12:21:09:494 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (CREATE_SSN) in INIT state.

*// 检测LSP（FEC目的地址为22.22.2.2/32）的MPLS BFD会话在状态INIT时收到会话事件，事件类型为创建会话。*

\*Jun 29 12:21:11:559 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (REQUEST_TIMEOUT) in INIT state.

*// 会话在状态INIT时收到会话事件，事件类型为request定时器超时。*

\*Jun 29 12:21:11:562 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (RECEIVE_REPLY) in INIT state.

*// 会话在状态INIT时收到会话事件，事件类型为收到echo reply报文。*

\*Jun 29 12:21:11:569 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (BFD_SSNUP) in DOWN state.

*// 会话在状态DOWN时收到会话事件，事件类型为BFD会话UP。*

\*Jun 29 12:21:16:659 2012 Sysname MBFD/7/EVENT: -MDC=1; Session (Type: LSP; FEC: 22.22.2.2/32; EntryKey: 1031) received session event (DELAYNTF_TIMEOUT) in UP state.

*// 会话在状态UP时收到会话事件，事件类型为延迟通知定时器超时。*

\# 打开MPLS BFD的处理过程调试信息开关。配置通过BFD检测VPLS的PW，如果设备上存在对应的PW，且该PW处于Up状态，则会打印如下调试信息。

\<Sysname\> debugging mpls bfd process

\<Sysname\> system-view

Sysname vsi ttt

Sysname-vsi-ttt pwsignaling ldp

Sysname-vsi-ttt-ldp peer 22.22.2.2 pw-id 1 pw-class test

\*Jun 29 12:36:34:958 2012 Sysname MBFD/7/PROCESS: -MDC=1; Created MBFD session (Type: PW; Peer: 22.22.2.2; PWID: 1; EntryKey: 1082130432). Index:1

*// 创建检测PW的MPLS BFD会话。PW的远端PE地址为22.22.2.2，PW ID为1，BFD会话索引为1。*

\*Jun 29 12:36:34:958 2012 Sysname MBFD/7/PROCESS: -MDC=1; Started timer (0) , ID: 0

*// 开启request定时器，定时器ID为0。*

\*Jun 29 12:36:36:959 2012 Sysname MBFD/7/PROCESS: -MDC=1; Allocated local discriminator (513)

*// 分配本地标识符513。*

\*Jun 29 12:36:38:962 2012 Sysname MBFD/7/PROCESS: -MDC=1; Added session (Type: PW; Peer: 22.22.2.2; PWID: 1; EntryKey: 1082130432) to BFD.

*// 在BFD进程中创建检测PW的BFD会话。*

\*Jun 29 12:36:38:966 2012 Sysname MBFD/7/PROCESS: -MDC=1; Sent message to BFD. VRF: 0; type: 128; entry key: 1082130432; result: 0.

*// 发送消息到BFD进程，VRF为0，BFD检测隧道为PW，Entry Key为1082130432，结果为成功。*

\*Jun 29 12:36:38:966 2012 Sysname MBFD/7/PROCESS: -MDC=1; Session (Type: PW; Peer: 22.22.2.2; PWID: 1; EntryKey: 1082130432) state changed from INIT to DOWN.

*[// MPLS BFD*]*会话状态由init变为down。*

\*Jun 29 12:36:38:967 2012 Sysname MBFD/7/PROCESS: -MDC=1; Started timer (1), ID: 0

*// 开启会话老化定时器，定时器ID为0。*

\*Jun 29 12:36:44:159 2012 Sysname MBFD/7/PROCESS: -MDC=1; Sent session (Type: PW; Peer: 22.22.2.2; PWID: 1; EntryKey: 1082130432) state changed message to APP. Current session state: 1

*// 向MPLS BFD应用发送BFD会话状态变化消息，当前会话状态为Up。*

\# 打开MPLS BFD热备份事件调试信息开关。配置通过BFD检测LSP，创建MPLS BFD会话后，插入备板，设备上打印如下调试信息。

\<Sysname\> debugging mpls bfd hsb

\*Jun 29 15:30:45:203 2012 Sysname MBFD/7/NULL: -MDC=1; Sent an HA message (0).

*// 备板插入，进行批量备份*

