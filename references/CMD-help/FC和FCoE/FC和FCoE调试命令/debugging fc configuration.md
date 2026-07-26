
**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc configuration**

------------------------------------------------------------------------

【命令】

**[debugging fc configuration**[ { **all** \| **error** \| **event** \| **packet** \| **timer** } [ **vsan** *vsan-id* ]]]

**[undo debugging fc configuration**[ { **all** \| **error** \| **event** \| **packet** \| **timer** } [ **vsan** *vsan-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[timer**]：表示定时器调试信息开关。

**[vsan** *vsan-id*]：表示指定VSAN的调试信息开关，*vsan-id*的取值范围为1～3839。如果未指定本参数，表示所有VSAN的调试信息开关。

【描述】

**[debugging fc configuration**]命令用来打开Fabric配置模块的调试信息开关。**undo debugging fc configuration**命令用来关闭Fabric配置模块的调试信息开关。

缺省情况下，Fabric配置模块的调试信息开关处于关闭状态。

表1-1 debugging fc configuration error命令输出信息描述表

字段

描述

VSAN *id* memory is not enough.

VSAN *id*内存不足

VSAN *id* ignored the RDI request packet received from upstream link.

VSAN *id*内忽略从上游收到的RDI请求

VSAN *id* received RDI SW_ACC packet, but RDI session did not exist.

VSAN *id*内收到RDI SW_ACC报文，但RDI session不存在

VSAN *id* received RDI SW_RJT packet, but RDI session did not exist.

VSAN *id*内收到RDI SW_RJT报文，但RDI session不存在

Interface *interface-name* in VSAN *id* failed to be isolated.

接口*interface-name*在VSAN *id*内隔离失败

VSAN *id* failed to process a RDI request packet.

VSAN *id*内处理RDI请求报文失败

VSAN *id* received an error EFP packet for error record length *len*.

VSAN *id*内收到错误EFP报文，错误记录长度*len*

VSAN *id* received an error EFP packet for error payload length *len*, and total packet length was *tlen*.

VSAN *id*内收到错误EFP报文，错误负载长度*len*，报文总长度*tlen*

VSAN *id* received an error EFP packet for invalid principal switch priority *priority*.

VSAN *id*内收到错误EFP报文，主交换机优先级*priority*无效

VSAN *id* received an error EFP packet for invalid principal switch name.

VSAN *id*内收到错误EFP报文，主交换机名无效

VSAN *id* received an error DIA packet for error DIA length *len.*

VSAN *id*内收到错误DIA报文，错误DIA长度*len*

VSAN *id* received an error DIA packet for invalid switch name.

VSAN *id*内收到错误DIA报文，交换机名无效

VSAN *id* received an error RDI packet for error payload length *len*, and total packet length was *tlen*.

VSAN *id*内收到错误RDI报文，错误负载长度*len*，报文总长度*tlen*

VSAN *id* received an error RDI packet for invalid requesting switch name.

VSAN *id*内收到错误RDI报文，请求交换机名无效

VSAN *id* received an error RDI packet for invalid domain ID.

VSAN *id*内收到错误RDI报文，域ID无效

VSAN *id* failed to allocate the domain ID, and error code was *errcode*.

VSAN *id*内分配域ID失败，错误码为*errcode*。其中，*errcode*为1表示申请多个Domain ID时有已经被分出的Domain ID；为2表示Domain ID已经被申请完

VSAN *id* failed to send RDI packet because RDI session did not exist.

VSAN *id*内发送RDI报文失败，因为RDI session不存在

VSAN *id* ignored reconfiguration operation because the switch was isolated.

VSAN *id*内忽略重配置操作，因为交换机已经被隔离

Interface *interface-name* in VSAN *id* received packet on a wrong interface.

接口*interface-name*在VSAN *id*内从错误接口收到报文

Interface *interface-name* in VSAN *id* received RCF SW_RJT packet, and isolated the interface.

接口*interface-name*在VSAN *id*内收到RCF拒绝报文，并隔离端口

VSAN *id* received an error BF packet for error payload length *plen.*

VSAN *id*内收到错误BF报文，负载长度错误*plen*

VSAN *id* received an error RCF packet for error payload length *plen*.

VSAN *id*内收到错误RCF报文，负载长度错误*plen*

Interface *interface-name* in VSAN *id* rejected RCF packet.

接口*interface-name*在VSAN *id*内拒绝RCF报文

Interface *interface-name* in VSAN *id* failed to send *pkttype* packet from socket *id*, and cmdcode was *cmdcode*.

接口*interface-name*在VSAN *id*内从socket *id*发送*pkttype*（EFP、DIA、RDI、BF、RCF）报文失败，命令码字段为*cmdcode*

Interface *interface-name* in VSAN *id* dropped packet.

接口*interface-name*在VSAN *id*内丢弃报文

VSAN *id* failed to create socket.

VSAN *id*内创建socket失败

Interface *interface-name* in VSAN *id* failed to add port data of *pkttype* packet.

接口*interface-name*在VSAN *id*内添加*pkttype*（EFP、DIA、RDI、BF、RCF）报文的端口数据失败

VSAN *id* failed to bind socket *id*.

VSAN *id*内绑定socket *id*失败

VSAN *id* failed to start link up delay timer.

VSAN *id*内创建链路up定时器失败

表1-2 debugging fc configuration event命令输出信息描述表

字段

描述

VSAN *id* merged (*wwn, domain-id*) to local domain ID list.

VSAN *id*内合并报文中的*wwn*和*domain-id*对到本地

VSAN *id* deleted (*wwn, domain-id*) from local domain ID list.

VSAN *id*内从本地删除*wwn*和*domain-id*对

Interface *interface-name* in VSAN *id* received EPort up event.

接口*interface-name*在VSAN *id*内收到E端口up事件

Interface *interface-name* in VSAN *id* received EPort down event.

接口*interface-name*在VSAN *id*内收到E端口down事件

VSAN *id* fabric name changed from *wwn1* to *wwn2*.

VSAN *id*内fabric name从*wwn1*变为*wwn2*

VSAN *id* principal switch changed to (*switch-wwn*, *priority*).

VSAN *id*内主交换机变为（*switch-wwn*，*priority*）

VSAN *id* running domain ID changed from *domain-id1* to *domain-id2*.

VSAN *id*内运行域ID从*domain-id1*变为*domain-id2*

VSAN *id* sent EFP requests to all up ports.

VSAN *id*内向所有UP的接口发送EFP请求报文

VSAN *id* unisolated all isolated ports.

VSAN *id*内去隔离所有已隔离的接口

Interface *interface-name* in VSAN *id* was isolated because the switch was isolated.

由于交换机被隔离，所以接口*interface-name*在VSAN *id*内被隔离

Interface *interface-name* in VSAN *id* received DIA request packet from non-upstream principal link.

接口*interface-name*在VSAN *id*内从非上游主链路收到DIA请求报文

VSAN *id* received RDI RJT packet because the principal switch rejected allocating domain ID with reason code *reason-code.*

VSAN *id*内收到RDI拒绝报文因为主交换机拒绝分配域ID且原因码为*reason-code*

Interface *interface-name* in VSAN *id* rejected the allocated domain ID, and isolated the interface.

接口*interface-name*在VSAN *id*内拒绝分配的域ID，并隔离接口

VSAN *id* accepted the allocated domain ID *domain-id*.

VSAN *id*内接收分配的域ID *domain-id*

VSAN *id* successfully allocated domain ID *domain-id* for the downstream switch.

VSAN *id*内为下游交换机成功分配域ID *domain-id*

VSAN *id* started non-disruptive reconfiguration because principal switch conflicted.

VSAN *id*内发起不中断重配置因为记录的主交换机信息冲突

VSAN *id* updated the local domain ID list.

VSAN *id*内更新本地域ID列表

VSAN *id* processed *event (event-id)* event in *state (state-id)* state.

VSAN *id*内*state-id*状态下处理*event-id*事件。其中，

*[state-id*]与*state*取值及含义：

·0：INIT

·1：BF

·2：RCF

·3：EFP

·4：PRINCIPAL

·5：REQUEST

·6：SUBORDINATE

·7：STATIC

*[event-id*]与*event*取值及含义：

·0：EPort up ，EPort端口up事件

·1：PSST timed out ，PSST定时器超时

·2：DIA packet，收到DIA请求报文

·3：RDI packet，收到RDI请求

·4：RDI_RJT packet，收到RDI请求的SW_RJT回应报文

·5：RDI_ACC packet，收到RDI请求的SW_ACC回应报文

·6：FRT timed out ，FRT定时器超时

·7：BF packet，收到BF请求报文

·8：RCF packet，收到RCF请求报文

·9：non-disruptive domain restart，发起Non-disruptive重配置事件

·10：disruptive domain restart，发起Disruptive重配置事件

·11：overlapped EFP packet，收到EFP报文且Fabric合并域ID有重叠

·12：non-overlapped EFP packet，收到EFP报文且Fabric合并域ID不重叠且不为空

·13：empty EFP packet，收到Domain_ID_List为空EFP报文

·14：principal link down，主链路的EPort端口DOWN

·15：fabric enable，Fabric配置功能开启

·16：fabric disable，Fabric配置功能关闭

·17：switch isolate，交换机隔离

·18：switch unisolate，交换机去隔离

VSAN *id* isolated the switch.

VSAN *id*内隔离交换机

VSAN *id* unisolated the switch.

VSAN *id*内去隔离交换机

VSAN *id* started non-disruptive reconfiguration because local switch was principal switch.

VSAN *id*内发起不中断重配置因为本设备是主交换机

Interface *interface-name* in VSAN *id* was successfully isolated.

接口*interface-name*在VSAN *id*内隔离成功

Interface *interface-name* in VSAN *id* was successfully unisolated.

接口*interface-name*在VSAN *id*内去隔离成功

Interface *interface-name* in VSAN *id* was added to downstream principal link.

接口*interface-name*在VSAN *id*内被添加到下游主链路

Interface *interface-name* in VSAN *id* was deleted from downstream principal link.

接口*interface-name*在VSAN *id*内从下游主链路删除

Interface *interface-name* in VSAN *id* changed to the upstream principal link.

接口*interface-name*在VSAN *id*内变为上游主链路

VSAN *id* entered Init state.

VSAN *id*内状态机变迁为INIT状态

VSAN *id* entered BF state.

VSAN *id*内状态机变迁为BF状态

VSAN *id* entered RCF state.

VSAN *id*内状态机变迁为RCF状态

VSAN *id* entered EFP state.

VSAN *id*内状态机变迁为EFP状态

VSAN *id* entered Principal state.

VSAN *id*内状态机变迁为Principal状态

VSAN *id* entered Request state.

VSAN *id*内状态机变迁为Request状态

VSAN *id* entered Subordinate state.

VSAN *id*内状态机变迁为Subordinate状态

VSAN *id* entered Static state.

VSAN *id*内状态机变迁为Static状态

表1-3 debugging fc configuration packet命令输出信息描述表

字段

描述

Interface *interface-name* in VSAN *id* received SW_RJT packet from socket *socket-id*, reason was *RJTcode*, and explanation was *RJTexplanation*.

接口*interface-name*在VSAN *id*内从socket *socket-id*收到拒绝原因字段为*RJTcode*、解释码字段为*RJTexplanation*的拒绝报文

Interface *interface-name* in VSAN *id* received *pkttype* packet from socket *socket-id*, but the interface was isolated.

接口*interface-name*在VSAN *id*内从socket *socket-id*收到*pkttype*（BF、RCF、EFP、RDI、DIA）请求报文，但是接口处于隔离状态

Interface *interface-name* in VSAN *id* received RCF SW_RJT packet, and isolated the interface.

接口*interface-name*在VSAN *id*内收到RCF SW_RJT报文，并隔离接口

Interface *interface-name* in VSAN *id* received *pkttype* packet from socket *socket-id*, and cmdcode was *cmdcode*.

接口*interface-name*在VSAN *id*内从socket *socket-id*收到*pkttype*（BF、RCF、EFP、RDI、DIA）报文，命令码字段为*cmdcode*

Interface *interface-name* in VSAN *id* sent *pkttype* packet from socket *socket-id*, and cmdcode was *cmdcode*.

接口*interface-name*在VSAN *id*内从socket *socket-id*发送*pkttype*（EFP、DIA、RDI、BF、RCF）报文，命令码字段为*cmdcode*

表1-4 debugging fc configuration timer命令输出信息描述表

字段

描述

VSAN *id* deleted the PSST timer.

VSAN *id*内删除PSST定时器

VSAN *id* deleted the FRT timer.

VSAN *id*内删除FRT定时器

VSAN *id* PSST timer timed out.

VSAN *id*内PSST定时器超时

VSAN *id* failed to start the PSST timer.

VSAN *id*内启动PSST定时器失败

VSAN *id* successfully started the PSST timer.

VSAN *id*内启动PSST定时器成功

VSAN *id* FRT timer timed out.

VSAN *id*内FRT定时器超时

VSAN *id* failed to start the FRT timer.

VSAN *id*内启动FRT定时器失败

VSAN *id* successfully started the FRT timer.

VSAN *id*内启动FRT定时器成功

Interface *interface-name* in VSAN *id* failed to start the *pkttype* timer, and socket was *socket-id*.

接口*interface-name*在VSAN *id*内启动*pkttype*（EFP、DIA、RDI、BF、RCF）请求报文的定时器失败，且socket ID为*socket-id*

Interface *interface-name* in VSAN *id* *pkttype* timer timed out, and socket was *socket-id*.

接口*interface-name*在VSAN *id*内的*pkttype*（EFP、DIA、RDI、BF、RCF）请求报文定时器超时，且socket ID为*sock-id*

【举例】

\# 打开所有VSAN内Fabric配置模块的错误调试开关。在接口下配置拒绝RCF报文的情况下，当对端设备发起Fabric重配置时，系统将输出下列调试信息。

\<Sysname\> debugging fc configuration error

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 fc domain rcf-reject vsan 1

\*Jun 23 15:50:40:899 2011 Sysname FCFABRIC/7/ERROR: -MDC=1; Interface Fc1/0/1 in VSAN 1 rejected RCF packet.

*// 接口fc1/0/1在VSAN 1内拒绝RCF报文*

\# 打开所有VSAN内Fabric配置模块的事件调试开关。当发起Disruptive重配置时，系统将输出下列调试信息。

\<Sysname\> debugging fc configuration event

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 domain restart disruptive

The command may cause traffic interruption. Continue? [Y/N:y]

\*Jun 23 15:56:08:290 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 processed disruptive domain restart (10) event in INIT (0) state.

*[// VSAN 1*]*内 INIT状态下处理Disruptive重配置事件*

\*Jun 23 15:56:08:290 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 entered RCF state.

*[// VSAN 1*]*进入RCF状态*

\*Jun 23 15:56:08:290 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 running domain ID changed from 0x1 to 0.

*[// VSAN 1*]*运行域ID从1变为0 *

\*Jun 23 15:56:08:290 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 fabric name changed from 10:00:00:11:22:33:44:00 to 00:00:00:00:00:00:00:00.

*[// VSAN 1*]*的fabric name从10:00:00:11:22:33:44:00变为00:00:00:00:00:00:00:00 *

\*Jun 23 15:56:08:291 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 unisolated all isolated ports.

\*Jun 23 15:56:08:292 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; Interface Fc1/0/1 in VSAN 1 was successfully unisolated.

*[// VSAN 1*]*去隔离所有隔离接口，且接口fc1/0/1在VSAN1内去隔离*

\*Jun 23 15:56:08:294 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; Interface Fc1/0/1 in VSAN 1 received EPort up event.

\*Jun 23 15:56:08:325 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 processed EPort up (0) event in RCF (2) state.

*[// VSAN 1*]*收到EPORT up事件，在RCF状态下处理EPORT up事件*

\*Jun 23 15:56:13:325 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 entered EFP state.

\*Jun 23 15:56:13:325 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 sent EFP requests to all up ports.

*[// VSAN 1*]*进入EFP状态，并向所有UP的EPort发送EFP请求报文*

\*Jun 23 15:56:23:326 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 entered Principal state.

*[// VSAN 1*]*进入Principal状态*

\*Jun 23 15:56:23:326 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 running domain ID changed from 0 to 0x1.         

*[// VSAN 1*]*运行域ID从0变为1 *

\*Jun 23 15:56:23:326 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 principal switch changed to (10:00:00:11:22:33:44:00, 2).

*[// VSAN 1*]*主交换机变为(10:00:00:11:22:33:44:00, 2)*

\*Jun 23 15:56:23:326 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 fabric name changed from 00:00:00:00:00:00:00:00 to 10:00:00:11:22:33:44:00. 

*[// VSAN 1 fabric name*]*从00:00:00:00:00:00:00:00变为10:00:00:11:22:33:44:00*

\# 打开所有VSAN内Fabric配置模块的报文调试开关。当接口FC1/0/1变为UP时，系统将输出下列调试信息。

\<Sysname\> debugging fc configuration packet

\*Jun 23 16:24:11:854 2011 Sysname FCFABRIC/7/PACKET: -MDC=1; Interface Fc1/0/1 in VSAN 1 sent EFP packet from socket 102, and cmdcode was 0x11.

*[//*]*接口fc1/0/1在VSAN1内从socket 102发送EFP报文，命令字为0x11*

\*Jun 23 16:24:11:878 2011 Sysname FCFABRIC/7/PACKET: -MDC=1; Interface Fc1/0/1 in VSAN 1 received EFP packet from socket 102, and cmdcode was 0x2.

*// 接口fc1/0/1在VSAN1内从socket 102收到EFP报文，命令字为0x2*

\# 打开所有VSAN内Fabric配置模块的定时器调试开关。当发起Disruptive重配置时，系统将输出下列调试信息。

\<Sysname\> debugging fc configuration timer

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 domain restart disruptive

The command may cause traffic interruption. Continue? [Y/N:y]

\*Jun 23 16:30:01:410 2011 Sysname FCFABRIC/7/TIMER: -MDC=1; VSAN 1 successfully started the FRT timer.

*[// VSAN 1*]*内启动FRT定时器成功*

\*Jun 23 16:30:06:425 2011 Sysname FCFABRIC/7/TIMER: -MDC=1; VSAN 1 FRT timer timed out.

*[// VSAN 1*]*内FRT定时器超时*

\*Jun 23 16:30:06:425 2011 Sysname FCFABRIC/7/TIMER: -MDC=1; VSAN 1 successfully started the PSST timer.

*[// VSAN 1*]*内启动PSST定时器成功*

\*Jun 23 16:30:16:425 2011 Sysname FCFABRIC/7/TIMER: -MDC=1; VSAN 1 PSST timer timed out.

*[// VSAN 1*]*内PSST定时器超时*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc exchange**

------------------------------------------------------------------------

【命令】

**[debugging**[ **fc** **exchange** { **error** \| **packet** }]]

**[undo**[ **debugging** **fc** **exchange** { **error** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[error**]：表示错误调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging fc exchange**]命令用来打开FC Exchange调试信息开关。**undo debugging fc exchange**命令用来关闭FC Exchange调试信息开关。

缺省情况下，FC Exchange调试信息开关处于关闭状态。

表1-5 debugging fc exchange error命令输出信息描述表

字段

描述

Time(s)

时戳

FCEXCH Input

FC Exchange接收

FCEXCH Output

FC Exchange发送

VSAN ID

VSAN索引

Protocol

FC协议号（0为无效值）

Local

本端FC地址及Exchange ID

Remote

对端FC地址及Exchange ID

State

FC Exchange的连接状态，各种取值含义如下：

·PREPARE：表示协议Exchange绑定成功/连接Exchange等待回应报文

·LISTEN：表示协议Exchange监听连接

·ESTABLISHED：表示连接建立

·ABTS：表示连接超时或出错后发送了ABTS，正在等待ABTS ACK

·BA_ACC：表示收到了ABTS并回应了BA_ACC，正在等待ACC ACK

·ABTS_ACK：表示收到了ABTS ACK，正在等待BA_ACC

·CLOSED：表示连接关闭

Error: Failed to receive ACK for packet

没有收到对端ACK报文

Error: Failed to find exchange

查找Exchange失败

Error: Failed to process link exchange

连接Exchange校验修改失败

Error: Failed to accept connection

不允许建立连接

Error: Failed to create a socket for link exchange

连接Socket创建失败

Error: Failed to add link exchange

创建连接Exchange失败

Error: Invalid initiative

不具备发送主动权

Error: Failed to make memory continuously

报文内存连续失败

Error: Failed to build packet by packet type

Exchange协议报文生成失败

Error: Invalid seq ID

发送序号错误

Error: Failed to reassemble all fragments

分片报文重组失败

表1-6 debugging fc exchange packet命令输出信息描述表

字段

描述

Time(s)

时戳

FCEXCH Input

FC Exchange接收

FCEXCH Output

FC Exchange发送

state

FC Exchange的连接状态，各种取值含义如下：

·PREPARE：表示协议Exchange绑定成功/连接Exchange等待回应报文

·LISTEN：表示协议Exchange监听连接

·ESTABLISHED：表示连接建立

·ABTS：表示连接超时或出错后发送了ABTS，正在等待ABTS ACK

·BA_ACC：表示收到了ABTS并回应了BA_ACC，正在等待ACC ACK

·ABTS_ACK：表示收到了ABTS ACK，正在等待BA_ACC

·CLOSED：表示连接关闭

VSAN

VSAN索引

MngID

Exchange管理器ID

Protocol

FC协议号（0为无效值）

src

源FC地址及Exchange ID

dst

目的FC地址及Exchange ID

Seq_ID

Exchange报文序号

R_CTL

路由控制字段（Routing Control）

F_CTL

报文控制字段（Frame Control）

FC Class

FC连接服务级别

【举例】

\# 打开FC Exchange的错误调试信息开关。

\<Sysname\> debugging fc exchange error

\*Jun 10 14:23:07:630 2011 Sysname FCEXCH/7/FCEXCH_ERR: -MDC=1;

Time(s):1307715787  FCEXCH Output:

(Error: Failed to receive ACK for packet)

VSAN ID         : (1)

Protocol        : (14)

Local           : (0x040506:26)

Remote          : (0x010203:25)

State           : (ESTABLISHED)

*// 没有收到对端的ACK报文，打印错误信息和当前Exchange相关状态信息*

\# 打开FC Exchange的报文调试信息开关。客户端和服务器端收发报文调试信息如下。

\<Sysname\> debugging fc exchange packet

\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;

Time(s):1307717555  FCEXCH Output(state = PREPARE):

 FC Packet: src = 0x010203:35, dst = 0x040506:65535

            Seq_ID = 1, R_CTL = 0x02, F_CTL = 0x293000, FC Class = FC_CLASS_F

            Protocol = 14, MngID = 0, VSAN = 16

*// 客户端发送报文，打印报文基本信息和Exchange状态信息*

\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;

Time(s):1307717555  FCEXCH Input(state = ESTABLISHED):

 FC Packet: src = 0x010203:35, dst = 0x040506:65535

            Seq_ID = 1, R_CTL = 0x02, F_CTL = 0x293000, FC Class = FC_CLASS_F

            Protocol = 14, MngID = 0, VSAN = 16

*// 服务器端接收报文，打印报文基本信息和Exchange状态信息*

\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;

Time(s):1307717555  FCEXCH Output(state = ESTABLISHED):

 FC Packet: src = 0x040506:36, dst = 0x010203:35

            Seq_ID = 1, R_CTL = 0xc1, F_CTL = 0xe80000, FC Class = FC_CLASS_F

            Protocol = 0, MngID = 0, VSAN = 16

*// 服务器端回应ACK，打印报文基本信息和Exchange状态信息*

\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;

Time(s):1307717555  FCEXCH Input(state = PREPARE):

 FC Packet: src = 0x040506:36, dst = 0x010203:35

            Seq_ID = 1, R_CTL = 0xc1, F_CTL = 0xe80000, FC Class = FC_CLASS_F

            Protocol = 0, MngID = 0, VSAN = 16

*// 客户端接收ACK，打印报文基本信息和Exchange状态信息*

\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;

Time(s):1307717555  FCEXCH Output(state = ESTABLISHED):

 FC Packet: src = 0x040506:36, dst = 0x010203:35

            Seq_ID = 2, R_CTL = 0x02, F_CTL = 0xa93000, FC Class = FC_CLASS_F

            Protocol = 0, MngID = 0, VSAN = 16

*// 服务器端回应报文，打印报文基本信息和Exchange状态信息*

\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;

Time(s):1307717555  FCEXCH Input(state = ESTABLISHED):

 FC Packet: src = 0x040506:36, dst = 0x010203:35

            Seq_ID = 2, R_CTL = 0x02, F_CTL = 0xa93000, FC Class = FC_CLASS_F

            Protocol = 0, MngID = 0, VSAN = 16

*// 客户端接收报文，打印报文基本信息和Exchange状态信息*

\*Jun 10 14:52:35:382 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;

Time(s):1307717555  FCEXCH Output(state = ESTABLISHED):

 FC Packet: src = 0x010203:35, dst = 0x040506:36

            Seq_ID = 2, R_CTL = 0xc1, F_CTL = 0x680000, FC Class = FC_CLASS_F

            Protocol = 0, MngID = 0, VSAN = 16

*// 客户端回应ACK，打印报文基本信息和Exchange状态信息*

\*Jun 10 14:52:35:382 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;

Time(s):1307717555  FCEXCH Input(state = ESTABLISHED):

 FC Packet: src = 0x010203:35, dst = 0x040506:36

            Seq_ID = 2, R_CTL = 0xc1, F_CTL = 0x680000, FC Class = FC_CLASS_F

            Protocol = 0, MngID = 0, VSAN = 16

*// 服务器端接收ACK，打印报文基本信息和Exchange状态信息*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc forward**

------------------------------------------------------------------------

【命令】

**[debugging** **fc forward** **packet**]

**[undo** **debugging** **fc** **forward** **packet**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging fc forward**]命令用来打开FC转发调试信息开关。**undo debugging fc forward**命令用来关闭FC转发调试信息开关。

缺省情况下，FC转发调试信息开关处于关闭状态。

表1-7 debugging fc forward packet命令输出信息描述表

字段

描述

S_ID

源FC地址

D_ID

目的FC地址

Seq_Cnt

分片报文编号

Receiving the packet on interface *interface-name*

从指定接口接收报文

Sending the local packet out of interface *interface-name*

本机报文从指定接口发送

Sending the packet out of interface *interface-name*

报文从指定接口发送

【举例】

\# 打开FC转发报文调试信息开关。

\<Sysname\> debugging fc forward packet

\*Jun 10 16:04:43:021 2011 Sysname FCFWD/7/FCFWD_PKT: -MDC=1;

 FC Packet: S_ID = 0x040506, D_ID = 0x010203, Seq_Cnt = 0, Receiving the packet on interface Fc1/0/1

*// 从FC1/0/1接口接收报文，打印报文基本信息*

\*Jun 10 16:04:43:022 2011 Sysname FCFWD/7/FCFWD_PKT: -MDC=1;

 FC Packet: S_ID = 0x010203, D_ID = 0x040506, Seq_Cnt = 0, Sending the local packet out of interface Fc1/0/1

*// 本机报文从FC1/0/1接口发送，打印报文基本信息*

\*Jun 10 16:04:43:022 2011 Sysname FCFWD/7/FCFWD_PKT: -MDC=1;

 FC Packet: S_ID = 0x010203, D_ID = 0x040506, Seq_Cnt = 0, Sending the packet out of interface Fc1/0/1

*// 从FC1/0/1接口发送报文，打印报文基本信息*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc link**

------------------------------------------------------------------------

【命令】

FCF交换机/FCF-NPV交换机：

**[debugging fc link**[ { **all** \| **elp** \| **error** \| **esc** \| **event** \| **evfp** \| **login-out** \| **packet** \| **timer** } [ **interface** *interface-type interface-number* ]]]

**[undo debugging fc link**[{ **all** \| **elp** \| **error** \| **esc** \| **event** \| **evfp** \| **login-out** \| **packet** \| **timer** } [ **interface** *interface-type interface-number* ]]]

NPV交换机：

**[debugging fc link**[ { **all** \| **error** \| **event** \| **evfp** \| **login-out** \| **packet** \| **timer** } [ **interface** *interface-type interface-number* ]]]

**[undo debugging fc link**[{ **all** \| **error** \| **event** \| **evfp** \| **login-out** \| **packet** \| **timer** } [ **interface** *interface-type interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[elp**]：表示链路协商ELP协议调试信息开关。

**[error**]：表示错误调试信息开关。

**[esc**]：表示交换机能力协商ESC协议的调试信息开关。

**[event**]：表示事件调试信息开关。

**[evfp**]：表示VSAN参数协商EVFP协议的调试信息开关。

**[login-out**]：表示FLOGI/FDISC/LOGO协议的调试信息开关。

**[packet**]：表示报文调试信息开关。

**[timer**]：表示定时器调试信息开关。

**[interface ***interface-type interface-number*]：表示指定接口的调试信息开关。如果未指定本参数，表示所有接口的调试信息开关。

【描述】

**[debugging fc link**]命令用来打开FC链路调试信息开关。**undo debugging fc link**命令用来关闭FC链路调试信息开关。

缺省情况下，FC链路调试信息开关处于关闭状态。

需要注意的是，通过**interface**参数打开的指定接口的调试信息开关，只能通过在**undo**命令中指定**interface**参数来关闭。

表1-8 debugging fc link elp命令输出信息描述表

字段

描述

Interface *interface-name*: Successfully sent ELP request frames in VSAN *vsan-id*.

发送ELP请求报文成功

Interface *interface-name*: Failed to send ELP request frames in VSAN *vsan-id*.

发送ELP请求报文失败

Interface *interface-name*: Sent ELP RJT frames in VSAN *vsan-id*.

发送ELP拒绝报文

Interface *interface*-*name*: ELP negotiation succeeded and sent ACC frames in VSAN *vsan-id*.

ELP协商成功并发送响应报文

Interface *interface-name*: Received ELP request frames with invalid length in VSAN *vsan-id*.

收到长度不合法的ELP请求报文

Interface *interface-name*: Received ELP request frames in VSAN *vsan-id*.

收到ELP请求报文

Interface *interface*-*name*: Received ELP RJT frames in VSAN *vsan-id*.

收到ELP拒绝报文

Interface *interface-name*: Failed to receive ELP request ACK event in VSAN *vsan-id*.

接收ELP请求报文的ACK事件失败

Interface *interface-name*: Received ELP ACC frames in VSAN *vsan-id*.

收到ELP响应报文

Interface *interface*-*name*: Received ELP ACC frames with invalid length in VSAN *vsan-id*.

收到长度不合法的ELP响应报文

Interface *interface-name*: Received ELP RJT frames with invalid length in VSAN *vsan-id*.

收到长度不合法的ELP拒绝报文

Interface *interface-name*: Received exchange ACK event in VSAN *vsan-id*.

收到exchange ACK事件

Interface *interface-name*: Received exchange error event in VSAN *vsan-id*.

收到exchange error事件

Interface *interface-name:* The mode of the responder is F or NP in VSAN *vsan-id*.

响应端接口模式为F或NP模式

Interface *interface-name*: Failed to get ELP attributes in VSAN *vsan-id*.

获取ELP接口属性失败

Interface *interface-name*: Failed to get ELP local parameters.

获取ELP本地参数信息失败

Interface *interface-name*: The result of ELP parameter negotiation is *error-flag*.

ELP参数选择结果是*error-flag*，*error-flag*含义如下：

·0：参数协商成功

·1：获取本端接口参数失败

·2：流控参数协商失败

·3：协议版本不匹配

·4：对端非E端口

·5：定时器超时时间不匹配

·6：端口WWN相同

·7：交换机WWN相同

·8：class f参数协商失败，且不可二次协商

·9：class2\\class3参数协商失败，且不可二次协商

·10：class2\\class3参数协商失败，可二次协商

Interface *interface-name*: ELP flow control parameters are inconsistent.

ELP流控参数不一致

Interface *interface-name*: ELP versions are inconsistent.

ELP版本信息不一致

Interface *interface-name*: Peer ELP port is not a E_Port.

ELP对端不为E端口

Interface *interface-name*: R_A_TOV or E_D_TOV mismatched.

定时器不匹配

Interface *interface-name*: The names of two ports are equal

两端端口名相同

Interface *interface-name*: The names of two switches are equal

两端交换机名相同

Interface *interface-name*: Class F non-negotiable service parameters error.

ELP参数协商时CLASS F不可协商参数不一致

Interface *interface-name*: Class N non-negotiable service parameters error.

ELP参数协商时CLASS N不可协商参数不一致

Interface *interface-name*: Class N negotiable service parameters error.

ELP参数协商时CLASS N可协商参数不一致

Interface *interface-name*: ELP negotiation succeeded in VSAN *vsan-id*.

ELP协商成功

Interface *interface-name*: Started the second ELP negotiation in VSAN *vsan-id*.

发起ELP二次协商

Interface *interface-name*: ELP negotiation launches at two ports simultaneously in VSAN *vsan-id*.

两端同时发起ELP协商

Interface *interface-name*: ELP responder started R_A_TOV in VSAN *vsan-id*.

响应端启动资源分配定时器

Interface *interface-name*: The receiver is waiting for ACK of SW_ACC or SW_RJT, so the receiver should drop the ELP request packet.

当前正在等ACK，丢弃第二次收到的ELP请求报文

**

表1-9 debugging fc link error命令输出信息描述表

字段

描述

Interface *interface-name*: Failed to create ELP R_A_TOV in VSAN *vsan-id*.

创建ELP资源分配定时器失败

Interface *interface-name*: ELP failed to send ACC frames in VSAN *vsan-id*.

发送响应报文失败

Interface *interface-name*: Failed to start R_A_TOV for second negotiation in VSAN *vsan-id*.

二次协商启动资源分配定时器失败

Interface *interface-name*: Received an invalid event in VSAN *vsan-id*.

收到的事件不合法

Interface *interface-name*: Failed to get the state of state machine in VSAN *vsan-id*.

获取状态机状态失败

Interface *interface-name*: Failed to malloc memory in VSAN *vsan-id*.

申请内存失败

Interface *interface-name*: Failed to get the physical state machine.

获取物理状态机失败

Interface *interface-name*: Failed to send ESC request frames.

ESC发送请求报文失败

Interface *interface-name*: Failed to create ESC request timer.

ESC发起端创建定时器失败

Interface *interface-name*: Failed to create ESC responder timer.

ESC响应端创建定时器失败

Interface *interface-name*: EVFP failed to get local switch WWN.

EVFP获取本端交换机WWN值失败

Interface *interface-name*: Failed to add trunk list to driver.

将trunk list下驱动失败

Interface *interface-name*: Failed to set tag mode to kernel.

Tag模式下内核失败

Interface *interface-name*: EVFP failed to create a timer.

EVFP创建定时器失败

Interface *interface-name*: EVFP failed to create link socket.

EVFP创建link socket失败

Interface *interface-name*: Failed to send EVFP request frames.

发送EVFP请求报文失败

Interface *interface-name*: Failed to get WWN

获取端口WWN失败

Interface *interface-name*: Failed to allocate memory.

分配内存失败

Interface *interface-name*: Failed to add access VSAN to driver.

添加端口ACCESS VSAN ID到驱动失败

Interface *interface-name*: Failed to delete access VSAN from driver.

删除端口ACCESS VSAN ID到驱动失败

Interface *interface-name*: Failed to add trunk VSAN to driver.

添加端口Trunk VSAN ID到驱动失败

Interface *interface-name*: Failed to delete trunk VSAN from driver.

删除端口Trunk VSAN ID到驱动失败

Interface *interface-name*: Physical state is down, and it cannot send packet.

物理状态DOWN，发送失败

Interface *interface-name*: Failed to send packet in VSAN *vsan-id*.

端口*interface-name*发送报文失败

Interface *interface-name*: Failed to create login logical state machine in VSAN *vsan-id*.

创建login的逻辑状态机失败

Interface *interface-name*: Failed to create timer in VSAN *vsan-id*.

创建定时器失败

Interface *interface-name*: EEVFP failed to create link socket.

EEVFP创建link socket失败

Interface *interface-name*: EEVFP failed to send request frames.

EEVFP发送请求报文失败

Interface *interface-name*: EEVFP failed to create a timer.

EEVFP创建定时器失败

Failed to back up in batch for HA.

HA批备失败

Failed to upgrade for HA

HA升级失败

Failed to send real-time backup data.

发送实备数据失败

表1-10 debugging fc link esc命令输出信息描述表

字段

描述

Interface *interface-name*: Received ESC request frames.

收到ESC请求报文

Interface *interface-name*: Received RJT frames.

收到拒绝报文

Interface *interface-name*: Received ACK event.

接收到ACK事件

Interface *interface-name*: Received RJT frames of invalid size.

接收到的拒绝报文大小不合法

Interface *interface-name*: The ESC responder switch supports VSAN.

ESC响应端支持VSAN协议

Interface *interface-name*: The ESC responder switch doesn't support VSAN.

ESC响应端不支持VSAN协议

Interface *interface-name*: Failed to receive ESC ACC frames for invalid length.

收到的报文长度不合法

Interface *interface-name*: Failed to send ESC ACC frames.

发送ESC ACC报文失败

Interface *interface-name*: The state machine is in the EIsolate state.

状态机为E隔离状态

Interface *interface-name*: The ESC initiator switch doesn't support VSAN.

ESC发起端不支持VSAN协议

Interface *interface-name*: Received error ESC frames with partial descriptors.

收到描述符不完整的ESC报文

Interface *interface-name*: Received error ESC frames of invalid size.

收到大小错误的ESC报文

表1-11 debugging fc link event命令输出信息描述表

字段

描述

Interface *interface-name*: Received the failure of negotiation in init state and transited to Isolate state in VSAN *vsan-id*.

Init状态下收到了协商失败的事件并转化为isolate状态

Interface *interface-name*: Received the success of ELP negotiation in Init state and transited to E state in VSAN *vsan-id*.

Init状态下收到ELP协商成功事件并转化为E状态

Interface *interface-name*: Received logout in F state in VSAN *vsan-id*.

F状态下收到了logout的事件

Interface *interface-name*: Received the failure of login negotiation in Init state and transited to FIsolate state in VSAN *vsan-id*.

Init状态下收到login协商失败事件并转化为F隔离状态

Interface *interface-name*: Received the success of login negotiation in VSAN *vsan-id*.

收到login协商成功事件

Interface *interface-name*: Received the success of ESC negotiation in E state.

E状态下收到了ESC协商成功的事件

Interface *interface-name*: Received the success of ESC negotiation in F/NP state.

F或NP状态下收到了ESC协商成功的事件

Interface *interface-name*: Received ELP frames in Isolate or E state and transited to Init state in VSAN *vsan-id*.

在Isolate或E状态下收到了ELP报文并转化为Init状态

Interface *interface-name*: Received the success of EVFP negotiation in E state.

接口在E状态下收到EVFP协商成功的消息

Interface *interface-name*: Received the success of EEVFP negotiation in F or NP state.

接口在F或NP状态下收到EEVFP协商成功的消息

Interface *interface-name*: Received VSAN up message in VSAN *vsan-id*.

FCLINK模块收到VSAN up消息

Interface *interface-name*: Received VSAN down message in VSAN *vsan-id*.

FCLINK模块收到VSAN down消息

Interface *interface-name*: VSAN *vsan-id* does not exist or is not in trunk list.

当前VSAN不存在或者这个VSAN不在当前接口的trunk list内

Interface *interface-name*: Logical state machine does not exist in VSAN *vsan-id*.

当前接口当前VSAN的逻辑状态机不存在

Interface *interface-name*: Received all VSAN down message.

当前接口收到所有VSAN down的消息

Interface *interface-name*: Received getting trunk VSAN message.

当前接口收到获取trunk VSAN的消息

Interface *interface-name*: Sent valid trunk VSAN message.

当前接口要发送本接口trunk VSAN信息

Interface *interface-name*: FCoE module has not registered any event.

FCoE未注册任何事件

Interface *interface-name*: Set to *mode* and *linkstate* in VSAN *vsan-id*.

设置该VSAN内端口模式和链路状态

Interface *interface-name*: Isolated in VSAN *vsan-id*, reason id *reason-id*.

端口在指定VSAN内隔离，原因码为*reason-id*

Interface *interface-name*: Clear isolation info of all VSANs.

清除所有VSAN内的隔离信息

Interface *interface-name*: Unisolated in VSAN *vsan-id*, reason id *reason-id*.

端口在指定VSAN内去隔离，原因码为*reason-id reason-id*含义如下：

0：Fabric原因导致隔离

1：FC Zone原因导致隔离

Interface *interface-name:* Received the failure of EEVFP negotiation in F or NP state and transited to Isolate state.

当前接口在F/NP状态下收到EEVFP失败事件并隔离

Interface *interface-name*: Received VSAN deletion event in VSAN *vsan-id*.

收到VSAN删除事件

Interface *interface-name*: Received VSAN creation event in VSAN *vsan-id*.

收到VSAN创建事件

Interface *interface-name*: Received switch WWN change event in VSAN *vsan-id*.

收到交换机WWN变化事件

Interface *interface-name*: Received timer change event in VSAN *vsan-id*.

收到VSAN timer变化事件

Interface *interface-name*: Received domain ID change event in VSAN *vsan-id*.

收到domain ID变化事件

Interface *interface-name*: Received fabric name change event in VSAN *vsan-id*.

收到Fabric name变化事件

Interface *interface-name*: Failed to create LOGO request socket in VSAN *vsan-id*.

创建LOGO请求的socket失败

表1-12 debugging fc link evfp命令输出信息描述表

字段

描述

Interface *interface-name*: Launched EVFP_COMMIT negotiation.

发起EVFP COMMIT阶段协商

Interface *interface-name*: Encapsulated EVFP_SYNC request frames.

封装EVFP SYNC阶段的请求报文

Interface *interface-name*: Received EVFP_SYNC request frames.

收到EVFP SYNC阶段请求报文

Interface *interface-name*: Received EVFP_COMMIT request frames.

收到EVFP COMMIT阶段请求报文

Interface *interface-name*: Received EVFP_SYNC ACC frames.

收到EVFP SYNC阶段ACC报文

Interface *interface-name*: Received RJT frames.

收到拒绝报文

Interface *interface-name*: Successfully added trunk list to driver.

将trunk list下驱动成功

Interface *interface-name*: Received ACC frames.

接收到ACC报文

Interface *interface-name*: Received sync ACK event.

收到sync ACK事件

Interface *interface-name*: Received commit ACK event.

收到commit ACK事件

Interface *interface-name*: Responded to EVFP_SYNC request frames.

响应EVFP_SYNC请求报文

Interface *interface-name*: Responded to EVFP_COMMIT request frames.

响应EVFP_COMMIT请求报文

The WWN of the local end is greater than that of the peer end.

EVFP并发时本端的WWN比对端大

The WWN of the local end is smaller than that of the peer end.

EVFP并发时本端的WWN比对端小

The WWN of the local end equals that of the peer end.

EVFP并发时本端的WWN与对端相等

Interface *interface-name*: EVFP negotiated the VSAN tagging mode as non-tagging but the two ends had different access VSAN IDs.

两端EVFP协商后trunk模式为non-tagging，但两端的access VSAN不一致

Interface *interface-name:* Common trunk VSAN lists on both sides are empty after EVFP negotiation.

两端EVFP协商后公共VSAN列表为空

Interface *interface-name*: Local WWN is smaller than the peer WWN.

本端WWN小于对端

Interface *interface-name*: Rejected frames received in incorrect phase.

拒绝在错误阶段收到的报文

Interface *interface-name*: Rejected received frames with incorrect state.

拒绝收到的状态错误的报文

Interface *interface-name*: Rejected received frames with incorrect payload.

拒绝收到的负载错误的报文

Interface *interface-name*: Received frames with incorrect version.

收到的报文的版本错误

Interface *interface-name*: Received frames with incorrect switch WWN.

收到的报文WWN错误

Interface *interface-name*: Received frames with incorrect length.

收到的报文长度错误

Interface *interface-name*: Rejected received frames with incorrect transaction id.

拒绝transaction ID字段错误报文

Interface *interface-name*: Received type-unknown frames.

接收到未知类型的报文

Interface *interface-name*: Rejected EVFP_COMMIT frames received before the EVFP_SYNC phase.

拒绝在EVFP_SYNC阶段之前收到的EVFP_COMMIT报文

Interface *interface-name:* Discarded the EVFP reply frames received from the invalid interface.

丢弃从无效端口所接收到的EVFP回应报文

Interface *interface-name*: Successfully set tag mode to kernel.

Tag模式下内核成功

Interface *interface-name*: EVFP negotiation succeed.

EVFP协商成功

Interface *interface-name:* Sent EEVFP SYNC request frames.

发送EEVFP SYNC阶段请求报文

Interface *interface-name*: Received EEVFP_SYNC request frames.

EEVFP收到SYNC请求报文

Interface *interface-name:* Responded to EEVFP_SYNC request frames.

EEVFP响应SYNC请求报文

Interface *interface-name:* Received EEVFP_SYNC ACC frames.

EEVFP收到EEVFP SYNC ACC报文

Interface *interface-name:* EEVFP negotiated the VSAN tagging mode as non-tagging but the two ends had different access VSAN IDs.

EEVFP协商为non-tagging模式但是两端access VSAN不同

Interface *interface-name:* Common trunk VSAN lists on both sides are empty after EEVFP negotiation.

EEVFP两端协商出来的trunk VSAN list为空

Interface *interface-name:* Launched EEVFP_COMMIT negotiation.

EEVFP发起COMMIT协商

Interface *interface-name:* Sent EEVFP COMMIT request frames.

发送EEVFP COMMIT阶段请求报文

Interface *interface-name:* Received EEVFP_COMMIT request frames.

EEVFP收到COMMIT请求报文

Interface *interface-name:* Rejected EEVFP_COMMIT frames received before the EEVFP_SYNC phase.

EEVFP拒绝SYNC阶段之前收到的COMMIT报文

Interface *interface-name:* Responded to EEVFP_COMMIT request frames.

EEVFP响应COMMIT请求报文

Interface *interface-name:* Discarded the EEVFP reply frames received from the invalid interface.

丢弃从无效端口收到的EEVFP回应报文

表1-13 debugging fc link login-out命令输出信息描述表

字段

描述

Interface *interface-name*: Successfully sent FLOGI request in VSAN *vsan-id*.

发送FLOGI请求报文成功

Interface *interface-name*: Received FLOGI frame with wrong parameters and responded with a RJT frame in VSAN *vsan-id*.

收到FLOGI报文中的参数不合法，回拒绝报文

Interface *interface-name*: Received FLOGI request frame in VSAN *vsan-id*.

收到FLOGI请求报文

Interface *interface-name*: Received FLOGI request frame in wrong state and responded with a RJT frame in VSAN *vsan-id*.

收到FLOGI请求报文时，当前本端所处的模式不正确，回拒绝报文

Interface *interface-name*: Received FLOGI request frame of invalid length and responded with a RJT frame in VSAN *vsan-id*.

收到的FLOGI请求报文的长度不合法，回拒绝报文

Interface *interface-name*: Received FLOGI or FDISC ACC frame in VSAN *vsan-id*.

FLOGI或FDISC 报文请求端收到ACC报文

Interface *interface-name*: Received FLOGI ACC frame of invalid parameters in VSAN *vsan-id*.

端口收到的ACC报文中的参数不合法

Interface *interface-name*: Login succeeded in VSAN *vsan-id*.

端口在该VSAN内login成功

Interface *interface-name*: Sent FLOGI ACC frame in VSAN *vsan-id*.

端口发送ACC报文

Interface *interface-name*: Failed to get FCID in VSAN *vsan-id* and sent RJT frame.

获取FCID失败，回拒绝报文

Interface *interface-name*: Received FLOGI RJT packet in VSAN *vsan-id*.

收到FLOGI拒绝报文

Interface *interface-name*: The length of FLOGI RJT packet was invalid in VSAN *vsan-id*.

收到的FLOGI拒绝报文的长度不合法

Interface *interface-name*: F port was processing former login packet and rejected the FLOGI request packet in VSAN *vsan-id*.

F端口收到了FLOGI请求报文，但是当前正在处理之前的FLOGI

Interface *interface-name*: Received NP LOGO request packet in NP state in VSAN *vsan-id*.

NP端口收到了LOGO请求报文

Interface *interface-name*: Successfully cleared FCID in VSAN *vsan-id*.

清除FCID成功

Interface *interface-name*: Failed to clear FCID in VSAN *vsan-id*.

清除FCID失败

Interface *interface-name*: Successfully sent LOGO ACC packet in VSAN *vsan-id*.

发送LOGO ACC报文成功

Interface *interface-name*: Interface was terminated and deleted all login data in VSAN *vsan-id*.

端口终止协商且删除该VSAN内所有login数据

Interface *interface-name*: The length of LOGO request packet is invalid in VSAN *vsan-id*.

LOGO请求报文长度不合法

Interface *interface-name*: Failed to receive LOGO request packet in E state in VSAN *vsan-id*.

E状态下接收LOGO请求报文失败

Interface *interface-name*: Failed to receive LOGO request packet for invalid WWN or FCID in VSAN *vsan-id*.

WWN或FCID不合法导致接收LOGO请求报文失败

Interface *interface-name*: Successfully sent LOGO request packet in VSAN *vsan-id*.

发送LOGO请求报文成功

Interface *interface-name*: Successfully received LOGO ACC packet in VSAN *vsan-id*.

接收LOGO ACC报文成功

Interface *interface-name*: Successfully received LOGO RJT packet in VSAN *vsan-id*.

接收LOGO拒绝报文成功

Interface *interface-name*: Failed to receive LOGO request packet because the FC IDs are not equal in VSAN *vsan-id*.

FC ID不一致导致接收LOGO请求报文失败

Interface *interface-name*: Interface was not up in VSAN *vsan-id*.

端口在该VSAN没有up

Interface *interface-name*: Successfully sent FLOGI ACC packet in physic negotiation phase.

在物理协商阶段成功发送FLOGI ACC报文

Interface *interface-name*: Received FDISC request in VSAN *vsan-id*.

收到FDISC请求报文

Interface *interface-name*: Sent FLOGI or FDISC RJT frame in VSAN *vsan-id*.

发送FLOGI或者FDISC拒绝报文

表1-14 debugging fc link packet命令输出信息描述表

字段

描述

Interface *interface-name*: Sent packets in VSAN *vsan-id* successfully.

端口*interface-name*发送*vsan-id*内的报文成功

Interface *interface-name*: Received packets from VSAN *vsan-id*.

从端口*interface-name*的*vsan-id*上接收到报文

表1-15 debugging fc link timer命令输出信息描述表

字段

描述

Interface *interface-name*: R_A_TOV timed out and started the second ELP launch in VSAN *vsan-id.*

ELP资源分配定时器超时并发起二次协商

Interface *interface-name*: ELP E_D_TOV timed out and started R_A_TOV in VSAN *vsan-id.*

ELP错误检测定时器超时并启动资源分配定时器

Interface *interface-name*: Successfully created E_D_TOV in VSAN *vsan-id*.

创建错误检测定时器成功

Interface *interface-name*: ESC request timer timed out.

ESC请求端的定时器超时

Interface *interface-name*: ESC reply timer timed out.

ESC接收端的定时器超时

Interface *interface-name*: The timer waiting for EVFP SYNC ACC frames timed out.

EVFP等待SYNC ACC报文的定时器超时

Interface *interface-name*: The timer waiting for EVFP COMMIT ACC frames timed out.

EVFP等待COMMIT ACC报文的定时器超时

Interface *interface-name*: EVFP created or refreshed a timer to wait for EVFP_SYNC ACC frames.

创建或刷新等待EVFP_SYNC阶段ACC报文定时器

Interface *interface-name*: EVFP created or refreshed a timer to wait for EVFP_COMMIT ACC frames.

创建或刷新等待EVFP_COMMIT阶段ACC报文定时器

Interface *interface-name*: Successfully created ESC request timer.

ESC发起端创建定时器成功

Interface *interface-name*: Successfully created ESC responder timer.

ESC响应端创建定时器成功

Interface *interface-name*: EEVFP created or refreshed a timer to wait for EEVFP_SYNC ACC frames.

创建或刷新等待EEVFP_SYNC阶段ACC报文定时器

Interface *interface-name:* The timer waiting for EEVFP SYNC ACC frames timed out.

EEVFP等待SYNC ACC报文的定时器超时

Interface *interface-name:* EEVFP created or refreshed a timer to wait for EEVFP_COMMIT ACC frames.

创建或刷新等待EEVFP_COMMIT阶段ACC报文定时器

Interface *interface-name:* The timer waiting for EEVFP COMMIT ACC frames timed out.

EEVFP等待COMMIT ACC报文的定时器超时

Interface *interface-name*: The resource allocate timer timed out in VSAN *vsan-id* and a login negotiation was initiated again.

login资源分配定时器超时，再次发起login协商

Interface *interface-name*: The auto-load-balance timer will time out in *timeout* seconds.

自动负载均衡定时器将在*timeout*秒后超时

Interface *interface-name*: Failed to create auto-load-balance timer.

创建自动负载均衡定时器失败

Interface *interface-name*: The auto-load-balance timer timed out.

自动负载均衡定时器超时

【举例】

\# 启动FC设备，打开FC链路协商ELP协议的调试信息开关，会输出下列调试信息。

\<Sysname\> debugging fc link elp

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ELP: -MDC=1; Interface Fc1/0/1: Successfully sent ELP request frames in VSAN 2.

*// 发送ELP请求报文成功*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ELP: -MDC=1; Interface Fc1/0/1: Received exchange ACK event in VSAN 2.

*// 接收到对端ACK*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ELP: -MDC=1; Interface Fc1/0/1: Received ELP ACC frames in VSAN 2.

*// 接收到对端ELP ACC报文*

\# 启动FC设备，打开FC链路协商错误调试信息开关，会输出下列调试信息。

\<Sysname\> debugging fc link error

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ERROR: -MDC=1; Interface Fc1/0/1: Failed to create ELP R_A_TOV in VSAN 2.

*// 创建ELP资源分配定时器失败*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ERROR: -MDC=1; Interface Fc1/0/1: Failed to add trunk list to driver.

*// 将trunk list下驱动失败*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ERROR: -MDC=1; Interface Fc1/0/1: Failed to create login logical state machine in VSAN 1.

*// 创建login的逻辑状态机失败*

\# 启动FC设备，打开交换机能力协商ESC协议的调试信息开关，会输出下列调试信息。

\<Sysname\> debugging fc link esc

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ESC: -MDC=1; Interface Fc1/0/1: Received ACK event.

*// 接收到ESC请求报文的ACK*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ESC: -MDC=1; Interface Fc1/0/1: The ESC responder switch supports VSAN.

*[// ESC*]*响应端交换机支持VSAN协议*

\# 启动FC设备，打开FC链路协商事件调试信息开关，会输出下列调试信息。

\<Sysname\> debugging fc link event

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVENT: -MDC=1; Interface Fc1/0/1: Received the success of ESC negotiation in E state.

*[// E*]*模式下ESC协商成功*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVENT: -MDC=1; Interface Fc1/0/1: Received the success of EVFP negotiation in E state.

*[// E*]*模式下EVFP协商成功*

\# 启动FC设备，打开VSAN参数协商EVFP协议的调试信息开关，会输出下列调试信息。

\<Sysname\> debugging fc link evfp

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVFP: -MDC=1; Interface Fc1/0/1: Encapsulated EVFP_SYNC request frames.

*// 封装EVFP SYNC请求报文*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVFP: -MDC=1; Interface Fc1/0/1: Received sync ACK event.

*// 接收到SYNC报文的ACK*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVFP: -MDC=1; Interface Fc1/0/1: Received ACC frames.

*[// EVFP*]*接收到ACC报文*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVFP: -MDC=1; Interface Fc1/0/1: Received EVFP_SYNC ACC frames.

*// 接收到EVFP SYNC的ACC报文*

\# 启动FC设备，打开FC链路协商FLOGI/FDISC/LOGO协议的调试信息开关，会输出下列调试信息。

\<Sysname\> debugging fc link login-out

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/LOGINOUT: -MDC=1; Interface Fc1/0/1: Successfully sent FLOGI request in VSAN 1.

*// 发送FLOGI请求报文成功*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/LOGINOUT: -MDC=1; Interface Fc1/0/1: Received FLOGI request frame in wrong state and responded with a RJT frame in VSAN 2.

*// 收到FLOGI请求报文时，当前本端所处的模式不正确，回拒绝报文*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/LOGINOUT: -MDC=1; Interface Fc1/0/1: Successfully received LOGO ACC packet in VSAN 1.

*// 接收LOGO ACC报文成功*

\# 启动FC设备，打开FC链路协商报文调试信息开关，会输出下列调试信息。

\<Sysname\> debugging fc link packet

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/PACKET: -MDC=1; Interface Fc1/0/1: Sent packets in VSAN 1 successfully.

*// 端口FC1/0/1发送VSAN1内的报文成功*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/PACKET: -MDC=1; Interface Fc1/0/1: Received packets from VSAN 1.

*// 从端口FC1/0/1的VSAN1上接收到报文*

\# 打开FC链路协商定时器调试信息开关，会输出下列调试信息。

\<Sysname\> debugging fc link timer

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/TIMER: -MDC=1; Interface Fc1/0/1: Successfully created E_D_TOV in VSAN 2.

*// 创建错误检测定时器成功*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/TIMER: -MDC=1; Interface Fc1/0/1: Successfully created ESC request timer.

*// 创建ESC请求报文超时检测定时器*

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/TIMER: -MDC=1; Interface Fc1/0/1: EVFP created or refreshed a timer to wait for EVFP_SYNC ACC frames.

*// 创建或刷新等待EVFP_SYNC ACC报文的定时器*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc name-service**

------------------------------------------------------------------------

【命令】

**[debugging fc name-service**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging fc name-service**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging fc name-service**]命令用来打开FC名称服务调试信息开关。**undo debugging fc name-service**命令用来关闭FC名称服务调试信息开关。

缺省情况下，FC名称服务调试信息开关处于关闭状态。

表1-1 debugging fc name-service error命令输出信息描述表

字段

描述

VSAN *id* failed to find the CT session for socket *socket-id.*

VSAN *id*内查找socket *socket-id*的CT会话失败

VSAN *id* failed to find GMI session in domain ID *domain-id*, with source FCID *fc-id* and transaction ID *transaction-id*.

VSAN *id*内查找域ID *domain-id*，FCID *fc-id*，事务ID *transaction-id*的GMI会话失败

VSAN *id* failed to get CT register information.

VSAN *id*内获取CT注册信息失败

VSAN *id* failed to allocate socket or timer for sending SW_CT request in domain *domain-id*.

VSAN *id*内发送域*domain-id*内的SW_CT请求报文时申请socket或定时器失败

VSAN *id* failed to allocate session for sending SW_CT request in domain *domain-id*.

VSAN *id*内发送域*domain-id*内的SW_CT请求报文时申请会话失败

VSAN *id* failed to send SW_CT request for socket *socket-id* in domain *domain-id*.

VSAN *id*内通过socket *socket-id*发送域*domain-id*内的SW_CT请求失败

VSAN *id* failed to parse the ESS packet from domain *domain-id*.

VSAN *id*内解析从域*domain-id*发送的ESS报文失败

VSAN *id* received an invalid ESS packet from domain *domain-id*.

VSAN *id*内接收到从域*domain-id*发送的非法ESS报文

VSAN *id* failed to negotiate ESS with domain *domain-id*.

VSAN *id*内和域*domain-id* ESS协商失败

VSAN *id* domain *domain-id* data does not exist.

VSAN *id*内域*domain-id*相关的数据不存在

VSAN *id* failed to get port WWN.

VSAN *id*内获取端口WWN失败

VSAN *id* failed to add N port entry for the port *port-wwn*.

VSAN *id*内添加N端口*port-wwn*的表项失败

VSAN *id* failed to create N port.

VSAN *id*内创建N端口失败

VSAN *id* failed to create N node.

VSAN *id*内创建N节点失败

VSAN *id* failed to add N port.

VSAN *id*内添加N端口失败

VSAN *id* FCID *fc-id* has no PLOGI.

VSAN *id*内FCID *fc-id*没有PLOGI

VSAN *id* name service database is empty.

VSAN *id*内名称服务数据库为空

VSAN *id* rejected GET request packet with incorrect length in domain *domain-id*.

VSAN *id*内拒绝了域*domain*-id内的非法长度GET报文

VSAN *id* failed to parse entry when receiving GE_PT ACC packet.

VSAN *id*内解析GE_PT回应报文内的表项失败

VSAN *id* failed to add GMI session for GE_PT with source FCID *src-fc-id*, transaction ID *transaction-id*.

VSAN *id*内添加GE_PT的GMI会话失败，源FCID为*src-fc-id*，事务ID为*transaction-id*

VSAN *id* failed to add GMI session with source FCID *src-fc-id*, last FCID *last-fc-id*, and transaction ID *transaction-id*.

VSAN *id*内添加GMI会话失败，源FCID为*src-fc-id*，最后FCID为*last-fc-id*，事务ID为*transaction-id*

VSAN *id* fcping timer timed out.

VSAN *id*内fcping定时器超时

VSAN *id* source FCID of the fcping request was invalid.

VSAN *id*内fcping请求的源FCID非法

VSAN *id* payload length of the fcping request was incorrect, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内fcping请求的负载长度非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* version of the fcping request was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内fcping请求的版本非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* port tag of the fcping request was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内fcping请求的端口标签非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* port length of the fcping request was incorrect, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内fcping请求的端口长度非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*。

VSAN *id* FCID in the fcping frame was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内fcping请求的FCID非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* the fcping request was under process, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内fcping请求正在处理，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* WWN in the fcping frame was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内fcping请求的WWN非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* failed to send echo request, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内发送echo请求失败，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* token value of the fcping request was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内fcping请求的token值非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* failed to add fcping session, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.

VSAN *id*内添加fcping会话失败，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *id* does not exist.

VSAN *id*不存在

VSAN *id* failed to receive request packet from socket *socket-id*.

VSAN *id*内从socket *socket-id*接收请求失败

VSAN *id* failed to process response packet from socket *socket-id*.

VSAN *id*内从socket *socket-id*接收响应失败

VSAN *id* failed to create the socket for *packet-type* packet.

VSAN *id*内创建*packet-type*报文的socket失败

VSAN *id* failed to bind socket *socket-id* for *packet-type* packet.

VSAN *id*内*packet-type*报文的socket *socket-id*绑定失败

VSAN *id* failed to create *packet-type* timer for socket *socket-id*.

VSAN *id*内*packet-type*报文的socket *socket-id*创建定时器失败

VSAN *id* failed to send *packet-type* request/ACC/RJT packet to FCID *fc-id* with socket *socket-id*.

VSAN *id*内通过socket *socket-id*向FCID *fc-id*发送*packet-type*报文的（请求/回应/拒绝）失败

VSAN *id* failed to check PLOGI frame parameter.

VSAN *id*内检查PLOG报文参数失败

VSAN *id* FCID *fc-id* has no FLOGI.

VSAN *id*内FCID *fc-id*没有FLOGI

VSAN *id* failed to parse switch RSCN frame.

VSAN *id*内解析交换机RSCN报文失败

VSAN *id* failed to handle fabric enable event.

VSAN *id*内处理Fabric模式使能失败

VSAN *id* fragment ID *frag-id* of GMI request is invalid in domain ID *domain*-*id*, with source FC ID *src*-*fc*-*id* and transaction ID *transaction*-*id*, current fragment ID is *cur*-*frag*-*id*.

VSAN *id*内的域*domain-id*内收到分片ID为*frag-id*的无效GMI请求，源FCID为src-fc-id，事务ID为*transaction*-*id*，当前有效分片ID为*cur*-*frag*-*id*

VSAN *id* received request packet from interface which negotiation mode is invalid with socket *socket-id*.

VSAN *id*内从协商模式无效的接口接收到请求报文，socket ID为*socket-id*

VSAN *id* received response packet from interface which negotiation mode is invalid with socket *socket-id*.

VSAN *id*内从协商模式无效的接口接收到响应报文，socket ID为*socket-id*

表1-2 debugging fc name-service event命令输出信息描述表

字段

描述

VSAN *vsan-id* successfully deleted the GMI session in domain ID *domain-id*, with source FCID *src-fc-id*, last FCID *last-fc-id*, and transaction ID *transaction-id*.

VSAN *vsan-id*内成功删除域*domain-id*内的GMI会话，源FCID是*src-fc-id*，最后FCID是*last-fc-id*，事务ID是*transaction-id*

VSAN *vsan-id* successfully negotiated ESS with domain *domain-id*.

VSAN *vsan-id*内和域*domain-id* ESS协商通过

VSAN *vsan-id* ESS timer of domain *domain-id* timed out.

VSAN *vsan-id*内和域*domain-id* ESS协商定时器超时

VSAN *vsan-id* updated ESS capability list of domain *domain-id*.

VSAN *vsan-id*内更新和域*domain-id* ESS协商结果

VSAN *vsan-id* successfully deleted VSAN information.

成功删除VSAN *vsan-id*相关数据

VSAN *vsan-id* received domain ID change event, which changed from *old-domain-id* to *new-domain-id*.

VSAN *vsan-id*内域ID从*old-domain-id*变化为*new-domain-id*

VSAN *vsan-id* received route adding event of domain *domain-id*.

VSAN *vsan-id*内收到域*domain-id*的路由添加事件

VSAN *vsan-id* received route deleting event of domain *domain-id*.

VSAN *vsan-id*内收到域*domain-id*的路由删除事件

VSAN *vsan-id* received the FLOGI event of the port *port-wwn*.

VSAN *vsan-id*内收到端口*port-ww*n的FLOGI事件

VSAN *vsan-id* received the FLOGO event of the port *port-wwn*.

VSAN *vsan-id*内收到端口*port*-*wwn*的FLOGO事件

VSAN *vsan-id* FTR timer timed out, with S_ID *fc*-*id* and token value *token*-*value*.

VSAN *vsan-id*内FTR定时器超时，源FCID是*fc*-*id*，token值是*token*-*value*

VSAN *vsan-id* GE_ID frame timer timed out.

VSAN *vsan-id*内GE_ID报文定时器超时

VSAN *vsan-id* GE_PT frame timer timed out.

VSAN *vsan-id*内GE_PT报文定时器超时

VSAN *vsan-id* SW_CT GMI frame timer timed out.

VSAN *vsan-id*内SW_CT GMI报文定时器超时

VSAN *vsan-id* successfully sent GMI request for GE_PT/ GMI ACC.

VSAN *vsan-id*内收到GE_PT/GMI ACC后成功发送GMI请求

VSAN *vsan-id* successfully added GMI session for GE_PT with source FCID *src*-*fc*-*id*, last FCID *last*-*fc*-*id*, and transaction ID *transaction*-*id*.

VSAN *vsan-id*内添加GE_PT的GMI会话成功，源FCID为*src-fc-id*，最后FCID为*last*-*fc*-*id*，事务ID为*transaction*-*id*

VSAN *vsan-id* successfully received the GMI request for GE_PT with last FCID *fc*-*id*.

VSAN *vsan-id*内成功接收GE_PT的GMI请求，上次最后FCID为*f*c-*id*

VSAN *vsan-id* successfully added GMI session with source FCID *src-fc-id*, last FCID *last-fc-id*, and transaction ID *transaction-id.*

VSAN *vsan-id*内成功添加GMI会话成功，源FCID为*src*-*fc*-*id*，最后FCID为*last*-*fc*-*id*，事务ID为*transaction*-*id*

VSAN *vsan-id* successfully sent GE_PT request packet.

VSAN *vsan-id*内成功发送GE_PT请求

VSAN *vsan-id* successfully sent echo request frame.

VSAN *vsan-id*内成功发送echo请求

VSAN *vsan-id* received fcping request frame from source FCID *fc-id*.

VSAN *vsan-id*内收到从FCID *fc-id*发送的fcping请求

VSAN *vsan-id* received SW_RSCN request frame from FCID *fc-id.*

VSAN *vsan-id*内收到从FCID *fc-id*发送的SW_RSCN请求

VSAN *vsan-id* rejected SW_RSCN frame received from FCID *fc-id* for incorrect packet length.

由于报文长度非法，VSAN *vsan-id*内拒绝从FCID *fc-id*发送的SW_RSCN请求

VSAN *vsan-id* received SW_RSCN response frame from FCID *fc-id.*

VSAN *vsan-id*内收到从FCID *fc-id*发送的SW_RSCN回应

VSAN *vsan-id* notified FC ZONE local/remote N port realtime FLOGI/FLOGO, FCID: *fc-id*, WWN: *port-wwn*, FWWN: *Fport-wwn*.

VSAN *vsan-id*内实时通知FC ZONE本地/远端端口的FLOGI/FLOGO，FCID是*fc*-*id*，端口WWN是*port*-*wwn*，F端口的WWN是*Fport-wwn*

VSAN *vsan-id* notified FC ZONE batch N port FLOGI *n* times.

VSAN *vsan-id*内第*n*次批量通知FC ZONE N端口FLOGI

VSAN *vsan-id* filtered query requests to FCID *dst*-*fc*-*id* by FC ZONE, with the request source FCID: *src*-*fc*-*id*.

VSAN *vsan-id*内FC ZONE过滤了*src*-*fc*-*id*对*dst*-*fc*-*id*的查询请求

VSAN *vsan-id* filtered query requests to FCID *dst-fc-id* by FC ZONE, with the request source WWN: *src-port-wwn*.

VSAN *vsan-id*内FC ZONE过滤了*src*-*port*-*wwn*对*dst*-*fc*-*id*的查询请求

VSAN *vsan-id* received a VSAN mode change event, which changed from *old-mode* to *new-mode*.

VSAN *vsan-id*内收到VSAN模式从*old-mode*变为*new-mode*的事件

表1-3 debugging fc name-service packet命令输出信息描述表

字段

描述

VSAN *vsan-id* received *packet-type* request packet from socket *socket-id*.

VSAN *vsan-id*内从socket *socket*-*id*接收packet-type请求报文

VSAN *vsan-id* received *packet-type* response packet from socket *socket-id*.

VSAN *vsan-id*内从socket *socket*-*id*接收packet-type回应报文

VSAN *vsan-id* successfully sent *packet-type* request/ACC/RJT packet to FCID *fc-id* with socket *socket-id*.

VSAN *vsan-id* 内通过socket *socket*-*id*向*fc*-*id*发送*packet*-*type*请求/ACC/RJT

VSAN *vsan-id* successfully sent fcping ACC frame.

VSAN *vsan-id* 内成功发送fcping ACC报文

VSAN *vsan-id* sent fcping reject frame, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value.*

VSAN *vsan-id* 内发送fcping拒绝报文，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

【举例】

\# 打开FC名称服务错误调试信息开关。接收分片ID不合法的GMI报文时会输出下列调试信息。

\<Sysname\> debugging fc name-service error vsan 2

\*Jan 10 18:06:11:318 2012 Sysname FCGS_LOG/7/ERROR: -MDC=1; VSAN 2 fragment ID 3 of GMI request is invalid in domain ID 1, with source FCID 010001 and transaction ID 0, current fragment ID is 2.

*[// VSAN 2*]*内的域1内收到分片ID为3的无效GMI请求，源FCID为010001，事务ID为0，当前有效分片ID为2*

\# 打开FC名称服务事件调试信息开关。VSAN 2内有FLOGI或FLOGO时会输出下列调试信息。

\<Sysname\> debugging fc name-service event vsan 2

\*Jan 10 11:51:54:444 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 received the FLOGI event of the port 00:02:30:30:30:30:36:39.

*[// VSAN 2*]*内收到端口00:02:30:30:30:30:36:39的FLOGI事件*

\*Jan 10 11:51:54:444 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 notified FC ZONE local N port realtime FLOGI , FCID: 010000, WWN: 00:02:30:30:30:30:36:39.

*// 实时通知ZONE模块FLOGI，FCID为010000，端口WWN为00:02:30:30:30:30:36:39*

\*Jan 10 11:51:54:451 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 received SW_RSCN response frame from FCID fffc02. 

*// 接收到从fffc02发送的SW RSCN的回应报文*

\*Jan 10 11:51:43:230 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 received the FLOGO event of the port 00:02:30:30:30:30:36:39.

*[// VSAN 2*]*内收到端口00:02:30:30:30:30:36:39的FLOGO事件*

\*Jan 10 11:51:43:231 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 notified FC ZONE local N port realtime FLOGO , FCID: 010000, WWN: 00:02:30:30:30:30:36:39.

*// 实时通知ZONE模块FLOGO，FCID为010000，端口WWN为00:02:30:30:30:30:36:39*

\*Jan 10 11:51:43:238 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 received SW_RSCN response frame from FCID fffc02.

*// 接收到从fffc02发送的SW RSCN的回应报文*

\# 打开FC名称服务报文调试信息开关。VSAN 2内有FLOGI或FLOGO时会输出下列调试信息。

\<Sysname\> debugging fc name-service packet vsan 2

\*Jan 10 11:58:24:988 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 successfully sent SW_RSCN request packet to FCID fffc02 with socket 23.

*[// FLOGI*]*时向fffc02发送N节点上线的SW RSCN报文*

 \*Jan 10 11:58:24:992 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 received SW_RSCN response packet from socket 23.

*// 接收SW RSCN报文的回应报文*

\*Jan 10 11:58:25:023 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 received SW_CT request packet from socket 26.

*// 接收fffc02发送的获取所有名称服务数据库表项的GE_PT报文*

\*Jan 10 11:58:25:023 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 successfully sent SW_CT ACC packet to FCID fffc02 with socket 26.

*// 向fffc02发送GE_PT的ACC*

\*Jan 10 11:58:10:560 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 successfully sent SW_RSCN request packet to FCID fffc02 with socket 23.

*[// FLOGO*]*时向fffc02发送N节点下线的SW RSCN报文*

\*Jan 10 11:58:10:650 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 received SW_RSCN response packet from socket 23.

*// 接收SW RSCN报文的回应报文*

\*Jan 10 18:05:27:415 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 received ELS_CT request packet from socket 23.

*[// VSAN 2*]*内收到ELS_CT请求报文*

\*Jan 10 18:05:27:417 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 successfully sent ELS_CT ACC packet to FCID 010001 with socket 23.

*[// VSAN 2*]*内向010001成功发送ELS_CT ACC报文*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc nport**

------------------------------------------------------------------------

【命令】

**[debugging**[ **fc** **nport** { **all** \| **error** \| **event** \| **packet** [ **interface** *interface-type interface-number* ] }  **vsan** *vsan-id* ]]

**[undo**[ **debugging** **fc** **nport** { **all** \| **error** \| **event** \| **packet** [ **interface** *interface-type interface-number* ] }  **vsan** *vsan-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[interface ***interface*-*type* *interface*-*number*]：表示指定接口的调试信息开关，*interface*-*type*只能是FC接口、VFC接口或FC聚合接口。如果未指定本参数，表示所有FC接口、VFC接口和FC聚合接口的调试信息开关。只有被配置为NP模式的接口能打印出调试信息。

**[vsan** *vsan-id*]：表示指定VSAN的调试信息开关，*vsan-id*的取值范围为1～3839。如果未指定本参数，表示所有VSAN的调试信息开关。

【描述】

**[debugging** **fc** **nport**]命令用来打开模拟N_Port行为的调试信息开关。**undo** **debugging** **fc** **nport**命令用来关闭模拟N_Port行为的调试信息开关。

缺省情况下，模拟N_Port行为的调试信息开关处于关闭状态。

需要注意的是，只有NPV交换机和FCF-NPV交换机（NPV模式）支持本命令。

表1-16 debugging fc nport error命令输出信息描述表

字段

描述

Received an event for an invalid VSAN ID from Fabric.

从Fabric模块收到VSAN ID无效的事件通知

VSAN didn\'t exist. Deletion process terminated.

VSAN不存在，结束当前VSAN删除流程

Received an NPV FC ID addition event with invalid parameters.

收到参数无效的NPV FCID添加事件

Received an NPV FC ID deletion event with invalid parameters.

收到参数无效的NPV FCID删除事件

Failed to allocate memory for port data with FC ID *fcid-value*.

为FCID为*fcid-value*的Port数据分配内存失败

Failed to send a CT packet: packet type *packet-name*.

发送类型为*packet-name*的CT报文失败。*packet-name*包括：RFT_ID、RIP_NN、RSNN_NN、RSPN_ID和GMAL

Received a GMAL response of invalid length.

收到长度无效的GMAL回应报文

Failed to send a PLOGI packet: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.

发送Plogi请求失败，源地址为*source-fcid-value*，目的地址为*destination-fcid-value*

PLOGI registration failed, because the MTU was not obtained.

封装Plogi报文负载字段时获取MTU失败，Plogi注册终止

PLOGI registration failed, because the port WWN was not obtained.

获取接口WWN失败，Plogi注册终止

Failed to allocate memory for registration resources.

申请注册资源内存失败

Failed to receive a message.

接收消息失败

Failed to check the interface index and mode.

检查接收报文的端口索引和端口模式失败

Failed to check the FC ID of interface *interface-name* .

检查接收报文端口的FCID失败

Failed to get the VSAN ID.

获取报文中携带VSAN ID失败

Received an NPV FC ID event from interface *interface-name* with an invalid port mode.

从端口模式错误的接口收到NPV FCID事件

Failed to allocate memory for VSAN data.

为VSAN数据申请内存失败

Failed to allocate memory for interface data with FC ID *fcid-value.*

为指定FCID的接口数据申请内存失败

Invalid CT response received: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.

收到非法的CT回应报文，源地址为*source-fcid-value*，目的地址为*destination-fcid-value*

表1-17 debugging fc nport event命令输出信息描述表

字段

描述

Switch WWN successfully set to *wwn*.

成功将全局WWN值设置为*wwn*

VSAN *vsan-id* information deleted.

成功删除VSAN *vsan-id*的相关数据

Received an NPV FC ID addition event from interface *interface-name*: FC ID = *fcid-value*.

从接口*interface-name*收到FCID为*fcid-value*的NPV FCID添加事件

Received an NPV FC ID deletion event from interface *interface-name*.

从接口*interface-name*收到NPV FCID删除事件

Host name successfully set to *hostname*.

成功将主机名设置为*hostname*

Local IPv4 management address successfully set to *ip-address*.

成功将本机IPv4管理口地址设置为*ip-address*

Port data of FC ID *fcid-value* added.

成功添加FCID为*fcid-value*的Port数据

Port data of FC ID *fcid-value* deleted.

成功删除FCID为*fcid-value*的Port数据

NPV switch started registering parameters to FCF switch.

NPV交换机开始向FCF交换机进行参数注册

NPV registration was completed.

NPV交换机注册完成

Resent the *packet-type* registration request, because the registration timed out.

注册报文*packet-type*的注册请求超时，重发请求。*packet-type*包括：Plogi、RFT_ID、RIP_NN、RSNN_NN、RSPN_ID和GMAL

Terminated the *packet-type* registration, because the resent registration request timed out.

注册报文*packet-type*的注册请求重发超时，注册流程终止。*packet-type*包括：Plogi、RFT_ID、RIP_NN、RSNN_NN、RSPN_ID和GMAL

表1-18 debugging fc nport packet命令输出信息描述表

字段

描述

CT packet successfully sent: packet type = *packet-name*.

成功发送类型为*packet-name*的CT报文。*packet-name*包括：RFT_ID、RIP_NN、RSNN_NN、RSPN_ID和GMAL

Ready to register the FC-4 Type for FC ID *fcid-value*.

报文封装完成，即将为FCID为*fcid-value*的Port注册FC-4层协议类型

Ready to register an IP address *ip-address* for node *node-name*.

报文封装完成，即将为名为*node-name*的Node注册IP地址*ip-address*

Ready to register a symbolic node name *node-name* for node *node-name*.

报文封装完成，即将为名为*node-name*的Node注册描述名*node-name*

Ready to register a symbolic port name *port-name* for FC ID *fcid-value*.

报文封装完成，即将为FCID为*fcid-value*的Port注册描述名*port-name*

Ready to get a management address list of IE *ie-name*.

报文封装完成，即将获取名为*ie-name*的IE的管理口地址

Management address list successfully obtained.

成功获取管理口地址列表

PLOGI packet successfully sent: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.

成功发送Plogi请求，源地址为*source-fcid-value*，目的地址为*destination-fcid-value*

PLOGI response successfully received: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.

接收Plogi回应成功，源地址为*source-fcid-value*，目的地址为*destination-fcid-value*

CT reject packet received: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*, reason code = *reason-code-value*, explanation code = *reason-explanation-code-value*.

接收到CT拒绝报文，源地址为*source-fcid-value*，目的地址为*destination-fcid-value*，拒绝原因码为*reason-code-value*，拒绝原因解释码为*reason-explanation-code-value*

PLOGI reject packet received: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.

接收到Plogi拒绝报文，源地址为*source-fcid-value*，目的地址为*destination-fcid-value*

CT accept packet received: packet type = *packet-type*, source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.

接收到CT Accept回应报文，报文类型为*packet-type*，源地址为*source-fcid-value*，目的地址为*destination-fcid-value*

【举例】

\# 打开模拟N_Port行为的所有调试信息开关。

\<Sysname\> debugging fc nport all

%Jun 27 08:55:44:607 2014 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Physical state on the interface Vfc2 changed to down.

\*Jun 27 08:55:44:625 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2: Received an NPV FC ID deletion event from interface Vfc2.

\*Jun 27 08:55:44:625 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2 interface Vfc2: Port data of FC ID 0a0000 deleted.

%Jun 27 08:55:44:642 2014 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Physical state on the interface Vfc4 changed to down.

*// 关闭接口后，收到VSAN 2中Vfc2接口NPV下FC ID删除事件，删除当前接口数据*

\*Jun 27 08:55:47:145 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2: Received an NPV FC ID addition event from interface Vfc2: FC ID = 0a0000.

\*Jun 27 08:55:47:147 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2 interface Vfc2: Port data of FC ID 0a0000 added.

\*Jun 27 08:55:47:147 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2 interface Vfc2: NPV switch started registering parameters to FCF switch.

*// 打开接口后，收到VSAN 2中Vfc2接口NPV下FC ID添加事件，新增当前接口数据，触发注册流程*

\*Jun 27 08:55:47:148 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: PLOGI packet successfully sent: source FC ID = 0a0000, destination FC ID = fffffc.

\*Jun 27 08:55:47:149 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: PLOGI accept packet received: source FC ID = fffffc, destination FC ID = 0a0000.

*[// VSAN 2*]*中Vfc2接口上向对端FCF发送名字服务Plogi注册请求并成功接收回应报文*

\*Jun 27 08:55:47:150 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to register the FC-4 Type for FC ID 0a0000.

\*Jun 27 08:55:47:150 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = RFT_ID.

%Jun 27 08:55:47:153 2014 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Physical state on the interface Vfc4 changed to up.

\*Jun 27 08:55:47:155 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = RFT_ID, source FC ID = fffffc, destination FC ID = 0a0000.

*// 开始注册FC-4类型，VSAN 2中Vfc2接口向对端FCF发送RFT_ID CT注册请求并成功接收回应*

\*Jun 27 08:55:47:156 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to register an IP address \"192.168.56.152\" for Node 10:00:00:03:00:00:00:00.

\*Jun 27 08:55:47:156 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = RIP_NN.

\*Jun 27 08:55:47:158 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = RIP_NN, source FC ID = fffffc, destination FC ID = 0a0000.

*// 开始注册本机IP地址，VSAN 2中Vfc2接口向对端FCF发送RIP_NN CT注册请求并成功接收回应*

\*Jun 27 08:55:47:158 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to register a symbolic node name \"Sysname\" for node 10:00:00:03:00:00:00:00.

\*Jun 27 08:55:47:159 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = RSNN_NN.

\*Jun 27 08:55:47:160 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = RSNN_NN, source FC ID = fffffc, destination FC ID = 0a0000.

*// 开始注册本机Node描述名，VSAN 2中Vfc2接口向对端FCF发送RSNN_NN CT注册请求并成功接收回应*

\*Jun 27 08:55:47:160 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to register a symbolic port name \"Sysname:Vfc2\" for FC ID 0a0000.

\*Jun 27 08:55:47:161 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = RSPN_ID.

\*Jun 27 08:55:47:163 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = RSPN_ID, source FC ID = fffffc, destination FC ID = 0a0000.

*// 开始注册本机NP接口的Port描述名，VSAN 2中Vfc2接口向对端FCF发送RSPN_ID CT注册请求并成功接收回应*

\*Jun 27 08:55:47:163 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: PLOGI packet successfully sent: source FC ID = 0a0000, destination FC ID = fffffa.

\*Jun 27 08:55:47:165 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: PLOGI accept packet received: source FC ID = fffffa, destination FC ID = 0a0000.

*[// VSAN 2*]*中Vfc2接口向对端FCF发送管理服务Plogi注册请求并成功接收回应报文*

\*Jun 27 08:55:47:165 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to get a management address list of IE 10:00:00:01:00:00:00:00.

\*Jun 27 08:55:47:166 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = GMAL.

\*Jun 27 08:55:47:168 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = GMAL, source FC ID = fffffa, destination FC ID = 0a0000.

\*Jun 27 08:55:47:168 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Management address list successfully obtained.

*// 开始查询对端FCF上的管理口地址，VSAN 2中Vfc2接口向对端FCF发送GMAL CT查询请求并成功接收回应，记录查询结果*

\*Jun 27 08:55:47:169 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2 interface Vfc2: NPV registration was completed.

*[//*]*结束整个注册流程*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc npv**

------------------------------------------------------------------------

【命令】

**[debugging fc npv** [ **interface** *interface-type interface-number* ]]

**[undo debugging fc npv** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface ***interface-type interface-number*]：表示指定接口的调试信息开关。如果未指定本参数，表示所有接口的调试信息开关。

【描述】

**[debugging fc npv**]命令用来打开NPV协议的调试信息开关。**undo debugging fc npv**命令用来关闭NPV协议的调试信息开关。

缺省情况下，NPV协议的调试信息开关处于关闭状态。

需要注意的是，只有NPV交换机和FCF-NPV交换机（NPV模式）支持本命令。

表1-19 debugging fc npv命令输出信息描述表

字段

描述

Interface *interface-name*: Failed to send LOGO packet from external interface in VSAN *vsan-id*.

上行口发送LOGO报文失败

Interface *interface-name*: Successfully cleared NPV LOGIDB in VSAN *vsan-id*.

清除NPV login数据库成功

Interface *interface-name*: Failed to clear NPV LOGIDB in VSAN *vsan-id*.

清除NPV login数据库失败

Interface *interface-name*: NPV proxy FLOGI or FDISC packet in VSAN *vsan-id*.

NPV代理FLOGI或者FDISC报文

Interface *interface-name*: Failed to find the external interface in VSAN *vsan-id*.

查找上行口失败

Interface *interface-name*: Successfully sent FDISC packet in VSAN *vsan-id*.

发送FDISC报文成功

Interface *interface-name*: Received FDISC ACC frame of invalid parameter in VSAN *vsan-id*.

收到参数无效的FDISC ACC报文

Interface *interface-name*: Received FDISC ACC packet in VSAN *vsan-id*.

收到FDISC ACC报文

Interface *interface-name*: Successfully sent FLOGI or FDISC ACC packet in VSAN *vsan-id*.

发送FLOGI或FDISC ACC报文成功

Interface *interface-name*: Successfully updated NPV LOGIDB in VSAN *vsan-id*.

更新NPV login数据库成功

Interface *interface-name*: The main board received the request from server interface in VSAN *vsan-id*.

主控板收到下行口发送的请求报文

Interface *interface-name*: The external interface received the request from main board in VSAN *vsan-id*.

上行口收到主控板发送的请求报文

Interface *interface-name*: The main board received ACC packet from external interface in VSAN *vsan-id*.

主控板收到上行口发送的ACC报文

Interface *interface-name*: The main board received RJT packet from external interface in VSAN *vsan-id*.

主控板收到上行口发送的拒绝报文

Interface *interface-name*: The server interface received ACC packet from main board in VSAN *vsan-id*.

下行口收到主控板发送的ACC报文

Interface *interface-name*: The server interface received RJT packet from main board in VSAN *vsan-id*.

下行口收到主控板发送的拒绝报文

Interface *interface-name*: The server interface sent request to main board in VSAN *vsan-id*.

下行口发送请求报文到主控板

Interface *interface-name*: The main board sent request to external interface in VSAN *vsan-id*.

主控板发送请求报文到上行口

Interface *interface-name*: The external interface sent ACC to main board in VSAN *vsan-id*.

上行口发送ACC报文到主控板

Interface *interface-name*: The main board sent ACC to server interface in VSAN *vsan-id*.

主控板发送ACC报文到下行口

Interface *interface-name*: The external interface sent RJT packet to main board in VSAN *vsan-id*.

上行口发送拒绝报文到主控板

Interface *interface-name*: The main board sent RJT packet to server interface in VSAN *vsan-id*.

主控板发送拒绝报文到下行口

Interface *interface-name*: Could not find external interface in VSAN *vsan-id*.

找不到上行口

Interface *interface-name*: Received FDISC RJT packet in VSAN *vsan-id*.

收到FDISC拒绝报文

Interface *interface-name*: Could not find server interface in VSAN *vsan-id*.

找不到下行口

Interface *interface-name*: The length of FDISC RJT packet was invalid in VSAN *vsan-id*.

FDISC拒绝报文长度不合法

Interface *interface-name*: The server interface sent RJT packet to ENode in VSAN *vsan-id*.

下行口向ENode发送拒绝报文

Interface *interface-name*: The resource allocation timer for FDISC ACC timed out in VSAN *vsan-id*.

等待FDISC ACC报文的RA定时器超时

【举例】

\# 打开NPV协议的调试信息开关，NPV设备在收到登录请求时如果查找上行口失败会输出下列调试信息。

\<Sysname\> debugging fc npv

\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/NPV: -MDC=1; Interface FC1/0/1: Failed to find the external interface in VSAN *2*.

*// 在VSAN2内查找上行口失败*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc rm**

------------------------------------------------------------------------

【命令】

**[debugging fc rm**[ { **all** \| **error** \| **fib** \| **static** \| **table** } [ **vsan** *vsan-id* ]]]

**[undo debugging fc rm**[ { **all** \| **error** \| **fib** \| **static** \| **table** } [ **vsan** *vsan-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[fib**]：表示路由变化通知调试信息开关。

**[static**]：表示静态路由调试信息开关。

**[table**]：表示路由表调试信息开关。

**[vsan** *vsan-id*]：表示指定VSAN的调试信息开关，*vsan-id*的取值范围为1～3839。如果未指定本参数，表示所有VSAN的调试信息开关。

【描述】

**[debugging fc rm**]命令用来打开FC路由管理调试信息开关。**undo debugging fc rm**命令用来关闭FC路由管理调试信息开关。

缺省情况下，FC路由管理调试信息开关处于关闭状态。

表1-20 debugging fc rm error命令输出信息描述表

字段

描述

Failed to add a domain controller route.

添加域控制器路由失败

Failed to send a routing message to the forwarding module.

向转发模块发送路由消息失败

Failed to add a node to the static routing table.

添加静态路由节点失败

This VSAN already exists.

指定的VSAN已经存在

No module has registered domain event.

没有模块注册domain事件

Failed to send domain-id message.

发送domain ID信息失败

Failed to add an ENode direct route.

添加ENode直连路由失败

表1-21 debugging fc rm fib命令输出信息描述表

字段

描述

Notified flushing routes.

通知路由下刷

Successfully sent a routing message to the forwarding module.

向转发模块发送路由消息成功

Started to flush routes.

开始路由下刷

Prepared to flush route *fcid/mask-length*, with the operation type as *type*.

准备路由下刷，操作类型*type*取值为：modify（修改）、delete（删除）

Flushed route *fcid/mask-length*, with the operation type as *type*.

路由下刷，操作类型*type*取值为：modify（修改）、delete（删除）

表1-22 debugging fc rm static命令输出信息描述表

字段

描述

Added a static route *fcid/mask-length*.

添加了一条静态路由

Deleted a static route *fcid/mask-length*.

删除了一条静态路由

表1-23 debugging fc rm table命令输出信息描述表

字段

描述

Received VSAN *vsan-id* creation event.

接收VSAN创建事件

Received VSAN *vsan-id* deletion event.

接收VSAN删除事件

Received VSAN *vsan-id* domain-change event, from *domain-id* to *domain-id*.

接收VSAN domain变化事件

Got domain id list.

获取 domain id列表

Successfully sent domain-id message.

发送domain-id信息成功

Received ENode FlOGI event with FC ID *fcid* in VSAN *vsan-id*

接收VSAN内ENode注册事件

Received ENode FLOGO event with FC ID *fcid* in VSAN *vsan-id*.

接收VSAN内ENode注销事件

【举例】

\# 打开所有VSAN内FC路由管理模块的路由变化通知调试信息开关，在VSAN 1内添加一条静态路由，会输出下列调试信息。

\<Sysname\> debugging fc rm fib

\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; [VSAN 1 Prepared to flush route 010101/24, with the operation type as modify.]

*// 准备路由下刷*

\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; Started to flush routes.

*// 开始路由下刷*

\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; Notified flushing routes.

*// 通知路由下刷*

\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; VSAN 1 Flushed route 010101/24, with the operation type as modify.

*// 路由下刷*

\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; VSAN 1 Successfully sent a routing message to the forwarding module.

*// 成功向转发模块发送路由消息*

\# 打开所有VSAN内FC路由管理模块的静态路由调试信息开关，在VSAN 1内添加一条静态路由，会输出下列调试信息。

\<Sysname\> debugging fc rm static

\*May 11 15:50:08:596 2011 Sysname FCRM/7/static: -MDC=1; [VSAN 1 Added a static route 010202/24.]

*// 添加了一条静态路由*

\# 打开所有VSAN内FC路由管理模块的静态路由调试信息开关，在VSAN 1内删除一条静态路由，会输出下列调试信息。

\<Sysname\> debugging fc rm static

\*May 11 15:50:35:140 2011 Sysname FCRM/7/static: -MDC=1; [VSAN 1 Deleted a static route 010202/24.]

*// 删除了一条静态路由*

\# 打开所有VSAN内FC路由管理模块的路由表调试信息开关，在创建VSAN 2时，会输出下列调试信息。

\<Sysname\> debugging fc rm table

\*May 11 15:53:04:557 2011 Sysname FCRM/7/table: -MDC=1; Received VSAN 2 creation event.

*// 接收VSAN 2创建事件*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc zone**

------------------------------------------------------------------------

【命令】

**[debugging fc zone**[ { **all** \| **error** \| **event** \| **packet** } [ **vsan** *vsan-id* ]]]

**[undo debugging fc zone**[ { **all** \| **error** \| **event** \| **packet** } [ **vsan** *vsan-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[vsan** *vsan-id*]：表示指定VSAN的调试信息开关，*vsan-id*的取值范围为1～3839。如果未指定本参数，表示所有VSAN的调试信息开关。

【描述】

**[debugging fc zone**]命令用来打开FC Zone调试信息开关。**undo debugging fc zone**命令用来关闭FC Zone调试信息开关。

缺省情况下，FC Zone调试信息开关处于关闭状态。

表1-24 debugging fc zone error命令输出信息描述表

字段

描述

Failed to create socket for sending distribute packet in VSAN *vsan-id*

VSAN *vsan-id*内发送扩散报文时创建socket失败

Failed to allocate timer resource for distribute packet in VSAN *vsan-id*

VSAN *vsan-id*内扩散时分配定时器资源失败

The length of packet exceeds the limit.

报文长度超出规格上限

Failed to create timer for resending MRRA request frame, and the merge is over on interface *interface-name* in VSAN *vsan-id*.

创建MRRA请求重发定时器失败，合并终止

Failed to send MRRA request frame, because the E-Port is down or the specified VSAN doesn\'t exist on interface *interface-name* in VSAN *vsan-id*.

发送MRRA请求失败，E端口处于down状态或者指定VSAN不存在

Failed to send MRRA request frame on interface *interface-name* in VSAN *vsan-id*.

发送MRRA请求失败

Failed to send MRRA request frame, and the merge is over on interface *interface-name* in VSAN *vsan-id*.

发送MRRA请求报文失败，合并终止

Failed to send MRRA ACC frame on interface *interface-name* in VSAN *vsan-id*.

发送MRRA ACC失败

Failed to receive MR request frame on interface *interface-name* in VSAN *vsan-id*.

接收MR请求失败

Failed to create timer for waiting for MR request frame on interface *interface-name* in VSAN *vsan-id*.

创建等待MR请求定时器失败

Failed to receive MRRA response frame, and the merge is over on interface *interface-name* in VSAN *vsan-id*.

接收MRRA响应报文失败，合并结束

Failed to receive MR response frame and the merge is over on interface *interface-name* in VSAN *vsan-id*.

接收MR响应报文失败，合并结束

Failed to receive I/O sync message from master slot.

接收主板同步过来的消息数据失败

Failed to create clock for timer.

为定时器创建物理时钟失败

Failed to set clock for timer.

为定时器设置物理时钟失败

Failed to create walk handle for zone avl tree.

为Zone AVL Tree创建遍历句柄失败

Failed to create walk handle for zone alias avl tree.

为Zone Alias AVL Tree创建遍历句柄失败

Failed to create timer for retrying to initialize event.

创建事件注册初始化重试定时器失败

Failed to delete ACL rule.

删除ACL规则失败

Failed to delete ACL rule from driver.

从驱动删除ACL规则失败

Failed to add ACLrule to driver.

添加ACL规则到驱动失败

Failed to delete ACL rule, because the specified ACLrule doesn\'t exist.

删除ACL规则失败，指定规则不存在

Failed to get local domain ID.

获取本机domain ID失败

No reachable route exists.

没有可达路由

Failed to allocate timer resource for distribute request packet.

创建等待请求报文定时器失败

NNode already exists.

N节点已经存在

Failed to delete NNode, because the WWN of specified NNode and the WWN of hash NNode don\'t match.

删除N节点失败，指定N节点的WWN与hash N节点的WWN不匹配

Failed to delete NNode, because the specified NNode doesn\'t exist.

删除N节点失败，指定N节点不存在

The latter frag is not consistent with the first frag:  first's socket=*socket-id-1*, first's VSAN=*vsan-id-1*, latter's socket=*socket-id-2*, latter's VSAN=*vsan-id-2.*

后续分片与首片分片信息不一致：首片socket=*socket-id-1*，首片VSAN=*vsan-id-1*，后续socket=*socket-id-2*，后续VSAN=*vsan-id-2*

The latter frag is not consistent with the first frag: first's IF= *interface-name-1*, latter's IF= *interface-name-2.*

后续分片与首片分片信息不一致：首片接口名称为*interface-name -1*，后续接口名称为*interface-name -2*

Failed to get the MTU of interface *interface-name.*

获取接口*interface-name*的MTU失败

Failed to get the destination interface option of socket *socket-id*.

从值为*socket-id*的socket获取目的接口选项数据失败

Failed to send message to I/O slot by socket *socket-id*.

通过值为*socket-id*的socket发送消息到I/O板失败

表1-25 debugging fc zone event命令输出信息描述表

字段

描述

\"New Neighbor Event\" happened on interface *interface-name* in VSAN *vsan-id*.

发现新邻居事件

\"Delete Neighbor Event\" happened on interface *interface-name* in VSAN *vsan-id.*

发生删除邻居事件

Created timer for resending MRRA request frame on interface *interface-name* in VSAN *vsan-id*.

创建MRRA请求报文重发定时器

The timer of waiting for request packet timed out in VSAN *vsan-id*.

等待请求报文定时器超时

Refreshed the timer for waiting for request packet in VSAN *vsan-id*.

刷新请求报文等待定时器

The timer of waiting for ACA reply packet timed out in VSAN *vsan-id*.

ACA应答报文等待定时器超时

The timer of waiting for SFC reply packet timed out in VSAN *vsan-id*.

SFC应答报文等待定时器超时

The timer of waiting for UFC reply packet timed out in VSAN *vsan-id*.

UFC应答报文等待定时器超时

The timer of waiting for RCA reply packet timed out in VSAN *vsan-id*.

RCA应答报文等待定时器超时

The merge is over, because the MRRA request frame has been sent *times* times on interface *interface-name* in VSAN *vsan-id*.

在VSAN *vsan-id*内合并结束，MRRA请求报文已经被发送*times*次

The merge is over, because the MR request frame has been sent *times* times on interface *interface-name* in VSAN *vsan-id*.

在VSAN *vsan-id*内合并结束，MR请求报文已经被发送*times*次

The merge is over, because the neighbor has replied busy RJT packet *times* times on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).

在VSAN *vsan-id*内合并结束，该邻居回复busy RJT报文*times*次，原因码是*reason-code*，解释码是*code-explanation*

The size of packet is too large, and isolated the E-port on interface *interface-name* in VSAN *vsan-id*.

报文长度超出限制，隔离E端口

Failed to allocate the resource for merged zoning database.

合并Zone数据库时申请资源失败

Finished closing the service and reclaiming the resource for FCF.

FCF模式下的服务关闭和资源回收完成

Finished closing the service and reclaiming the resource for NPV.

NPV模式下的服务关闭和资源回收完成

Finished starting the service and allocating the resource for FCF.

FCF模式下的服务开启和资源申请完成

Failed to start the service and allocate the resource for FCF.

FCF模式下的服务开启和资源申请失败

Received the event notification for creating VSAN *vsan-id* from fcfabricd.

收到fcfabricd创建VSAN *vsan-id*的事件通知

Received the event notification for destroying VSAN *vsan-id* from fcfabricd.

收到fcfabricd删除VSAN *vsan-id*的事件通知

Received the event notification for changing domain ID in VSAN *vsan-id* from fcfabricd.

收到fcfabricd在VSAN *vsan-id*内domain id变化的事件通知

Received the event notification for changing switch mode to NPV from fcfabricd.

收到fcfabricd交换机变化到NPV模式的事件通知

Received the event notification for changing switch mode to FCF from fcfabricd.

收到fcfabricd交换机变化到FCF模式的事件通知

Registered fabric service for FCF successfully.

FCF模式下注册fabric服务成功

Finished starting the service for NPV.

NPV模式下服务开启完成

Frag waiting timer is timeout, socket=*socket-id* VSAN=*vsan-id*, IF= *interface-name.*

分片等待定时器超时，soket=*socket-id*, VSAN=*vsan-id*, IF= *interface-name*

Isolated interface *interface-name* in VSAN *vsan-id* successfully.

成功将接口*interface-name*在VSAN *vsan-id* 内隔离

The isolation status of interface *interface-name* is cleared in VSAN *vsan-id*.

清除接口*interface-name*在VSAN *vsan-id*内的隔离状态

Failed to isolate interface *interface-name* in VSAN *vsan-id*.

在VSAN *vsan-id*内隔离接口*interface-nam*失败

The isolation status of interface *interface-name* is cleared in all VSANs.

清除接口*interface-name*在所有VSAN内的隔离状态

The isolation status of interface *interface-name* is cleared for interface physical-layer event.

当接口上发生物理事件的时候，将接口*interface-name*的隔离状态清除

The specified VSAN *vsan-id* doesn\'t exist.

指定的VSAN *vsan-id*不存在

Received message *message-type*.

收到*message-type*消息

消息类型为：

\"FCZONE_SYNCMSG_TYPE_DEACTZNST\"

\"FCZONE_SYNCMSG_TYPE_ACTZNST\"

\"FCZONE_SYNCMSG_TYPE_BOARDSMOOTH\"

\"FCZONE_SYNCMSG_TYPE_NNODE_BATCH\"

\"FCZONE_SYNCMSG_TYPE_NNODE_LOGIN\"

\"FCZONE_SYNCMSG_TYPE_NNODE_LOGOUT\"

\"FCZONE_SYNCMSG_TYPE_DEFAULT_ENABLE\"

\"FCZONE_SYNCMSG_TYPE_DEFAULT_DISABLE\"

\"FCZONE_SYNCMSG_TYPE_VSAN_DELETE\"

\"FCZONE_SYNCMSG_TYPE_DOMAIN_CHANGE\"

\"FCZONE_SYNCMSG_TYPE_DEBUG_SET\"

\"FCZONE_SYNCMSG_TYPE_DEBUG_BATCH\"

表1-26 debugging fc zone packet命令输出信息描述表

字段

描述

The ACA packet has been sent three times to domain *domain-id* in VSAN *vsan-id*

VSAN *vsan-id*内ACA报文已向domain ID为*domain-id*的设备发送了三次

The SFC packet has been sent three times to domain *domain-id* in VSAN *vsan-id*

VSAN *vsan-id*内SFC报文已向domain ID为*domain-id*的设备发送了三次

The UFC packet has been sent three times to domain *domain-id* in VSAN *vsan-id*

VSAN *vsan-id*内UFC报文已向Domain ID为*domain-id*的设备发送了三次

The RCA packet has been sent three times to domain *domain-id* in VSAN *vsan-id*

VSAN *vsan-id*内RCA报文已向Domain ID为*domain-id*的设备发送了三次

The ACA packet has been sent in VSAN *vsan-id*

VSAN *vsan-id*内ACA报文已发送

The SFC packet has been sent in VSAN *vsan-id*

VSAN *vsan-id*内SFC报文已发送

The UFC packet has been sent in VSAN *vsan-id*

VSAN *vsan-id*内UFC报文已发送

The RCA packet has been sent in VSAN *vsan-id*

VSAN *vsan-id*内RCA报文已发送

The ACA packet has been received in VSAN *vsan-id*

VSAN *vsan-id*内接收到ACA报文

The SFC packet has been received in VSAN *vsan-id*

VSAN *vsan-id*内接收到SFC报文

The UFC packet has been received in VSAN *vsan-id*

VSAN *vsan-id*内接收到UFC报文

The RCA packet has been received in VSAN *vsan-id*

VSAN *vsan-id*内接收到RCA报文

The SFC packet is not sourced from the manager in VSAN *vsan-id*.

VSAN *vsan-id*内收到的SFC报文的地址不是管理交换机地址

Received SFC packet at neither ACA nor SFC phase  in VSAN *vsan-id*.

VSAN *vsan-id*内在非ACA或SFC阶段收到SFC报文

Received malformed SFC packet in VSAN *vsan-id*.

报文长度不合法

Received unknown Operation Request SFC packet in VSAN *vsan-id*.

收到操作请求不合法报文

Received conflict SFC packet in VSAN *vsan-id*.

收到的多个SFC报文之间冲突

The RJT reply packet has been sent for fabric changed in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).

VSAN *vsan-id*内RJT应答报文已发送，因为fabric网络发生了变化，原因码是*reason-code*，解释码是*code-explanation*

The RJT reply packet has been sent for switch is busy in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).

VSAN *vsan-id*内RJT应答报文已发送，因为fabric网络正忙，原因码是*reason-code*，解释码是*code-explanation*

The RJT reply packet has been sent for processing failed in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).

VSAN *vsan-id*内RJT应答报文已发送，因为处理失败，原因码是*reason-code*，解释码是*code-explanation*

Received RJT reply packet of *domain domain-id* for ACA packet in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*)

VSAN *vsan-id*内接收到来自domain ID为*domain-id*的ACA报文的拒绝回应报文，原因码是*reason-code*，解释码是*code-explanation*

Received RJT reply packet of *domain domain-id* for SFC packet in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*)

VSAN *vsan-id*内接收到来自domain ID为*domain-id*的SFC报文的拒绝回应报文，原因码是*reason-code*，解释码是*code-explanation*

Received RJT reply packet of *domain domain-id* for UFC packet in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*)

VSAN *vsan-id*内接收到来自domain ID为*domain-id*的UFC报文的拒绝回应报文，原因码是*reason-code*，解释码是*code-explanation*

The ACC reply packet for ACA packet has been sent in VSAN *vsan-id*

VSAN *vsan-id*内ACA报文的ACC回应报文已发送

The ACC reply packet for SFC or UFC packet has been sent in VSAN *vsan-id*

VSAN *vsan-id*内SFC或UFC报文的ACC回应报文已发送

The ACC reply packet for RCA packet has been sent in VSAN *vsan-id*

VSAN *vsan-id*内RCA报文的ACC回应报文已发送

Received all ACC reply packet for ACA packet in VSAN *vsan-id*

VSAN *vsan-id*内接收到所有ACA报文的ACC回应报文

Received all ACC reply packet for SFC packet in VSAN *vsan-id*

VSAN *vsan-id*内接收到所有SFC报文的ACC回应报文

Received all ACC reply packet for UFC packet in VSAN *vsan-id*

VSAN *vsan-id*内接收到所有UFC报文的ACC回应报文

Received all ACC reply packet for RCA packet in VSAN *vsan-id*

VSAN *vsan-id*内接收到所有RCA报文的ACC回应报文

The invalid ACA packet has been discarded in VSAN *vsan-id*.

VSAN *vsan-id*内丢弃无效的ACA报文

The invalid UFC packet has been discarded in VSAN *vsan-id*.

VSAN *vsan-id*内丢弃无效的UFC报文

The invalid RCA packet has been discarded in VSAN *vsan-id*.

VSAN *vsan-id*内丢弃无效的RCA报文

Sent MRRA request frame successfully on interface *interface-name* in VSAN *vsan-id*.

发送MRRA请求

Received MRRA request frame on interface *interface-name* in VSAN *vsan-id*.

收到MRRA请求

Sent MRRA request frame *times* times on interface *interface-name* in VSAN *vsan-id*.

发送*times*次MRRA请求报文

Sent MR request frame *times* times on interface *interface-name* in VSAN *vsan-id*.

发送*times*次MR请求报文

Sent MRRA ACC response frame successfully on interface *interface-name* in VSAN *vsan-id.*

发送MRRA ACC成功

Received MRRA ACC response frame on interface *interface-name* in VSAN *vsan-id*.

接收到MRRA ACC报文

Received MRRA RJT response frame because of neighbor\'s busyness, and resent MRRA request later on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*)*.

收到MRRA报文的忙碌状态拒绝报文，稍后重发MRRA请求，原因码是*reason-code*，解释码是*code-explanation*

Received MRRA ACC frame, but the neighbor can't accept so large packet waiting for receiving again on interface *interface-name* in VSAN *vsan-id*.

MRRA协商完成，但邻居没有足够资源处理报文数据

Sent MR request frame successfully on interface *interface-name* in VSAN *vsan-id*.

发送MR请求

Received MR request frame on interface *interface-name* in VSAN *vsan-id*.

收到MR请求

Sent MR ACC response frame successfully on interface *interface-name* in VSAN *vsan-id*.

发送MR ACC

Received MR ACC response frame on interface *interface-name* in VSAN *vsan-id*.

收到MR ACC，MR协商结束

Sent MR RJT response frame, because the zone mode is inconsistent on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

发送MR RJT响应报文，因为合并发起端的Zone模式和本地不一致，原因码是*reason-code*，解释码是*code-explanation*

Sent MR RJT response frame, because the zone Merge-Control or Default-Zone does not match on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

发送MR RJT响应报文，因为合并发起端的merge-control或default zone策略等和本地的不一致，原因码是*reason-code*，解释码是*code-explanation*

Sent MR RJT response frame, because the Hard Zone Attribute is inconsistent on interface *interface-name* in VSAN *vsan-id*. (reason code=*reason-code*, reason code explanation=*code-explanation*).

发送MR RJT响应报文，因为合并发起端的硬件Zone使能情况和本地的不一致，原因码是*reason-code*，解释码是*code-explanation*

Sent MR RJT response frame, because the Merge-Control setting is restrict and the adjacent zoning database is not the same as the local zoning database on interface *interface-name* in VSAN *vsan-id*. (reason code=*reason-code*, reason code explanation=*code-explanation*)

发送MR RJT响应报文，因为Merge-Control为restrict时，合并发起端和本地的数据不完全相同，原因码是*reason-code*，解释码是*code-explanation*

Sent MR RJT response frame, because failed to merge the active zoneset on interface *interface-name* in VSAN *vsan-id*. (reason code=*reason-code*, reason code explanation=*code-explanation*)

发送MR RJT响应报文，合并active zoneset失败，原因码是*reason-code*，解释码是*code-explanation*

Sent MR RJT response frame, because the size of the merged packet was too large on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).

发送MR RJT响应报文，合并后数据超出限制，原因码是*reason-code*，解释码是*code-explanation*

Sent MR RJT response frame, because the number of zoning objects exceeds the limit on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).

发送MR RJT响应报文，zoning对象个数超出限制，原因码是*reason-code*，解释码是*code-explanation*

Sent MR RJT response frame, because failed to merge the database on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).

发送MR RJT响应报文，合并database失败，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame because the zone mode is inconsistent, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

VSAN *vsan-id*内接收到MR RJT报文，因为合并时两端设备Zone模式不一致，结束合并，并隔离端口，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame because the Hard Zone Attribute is inconsistent, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

VSAN *vsan-id*内接收到MR RJT报文，因为合并时两端设备硬件Zone 使能情况不一致，隔离端口，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame because the zone Merge-Control or Default-Zone does not match, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

VSAN *vsan-id*内接收到MR RJT报文，因为在增强Zone模式下，合并时两端设备的merge-control、default zone策略等不一致，合并失败，隔离端口，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame because Merge-Control is restrict and the adjacent zoning database is not the same as the local zoning database on interface *interface-name* in VSAN *vsan-id*. (reason code=*reason-code*, reason code explanation=*code-explanation*)

VSAN *vsan-id*内接收到MR RJT报文，因为在增强zone模式下，merge-control为restrict时，合并两端的Zone数据库不完全相同，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame, failed to merge the active zoneset, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

接收到MR RJT报文，active zoneset合并失败，隔离端口，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame, and the number of zoning objects exceeded the limit on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

接收到MR RJT报文，Zone对象个数超出规格，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame, and failed to merge database on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

接收到MR RJT报文，合并database失败，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame, and failed to merge database in Basic Zoning on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

VSAN *vsan-id*内接收到MR RJT报文，在基本Zone模式下，数据库合并失败，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame, the size of the merged packet exceeded the limit, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

接收到MR RJT报文，合并后的数据超出限制，隔离端口，原因码是*reason-code*，解释码是*code-explanation*

Received MR RJT response frame, failed to merge the database in Enhanced Zoning, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

VSAN vsan-id内接收到MR RJT报文，在增强zone模式下，Zone数据库合并失败，隔离端口，原因码是*reason-code*，解释码是*code-explanation*

Discarded invalid MRRA request frame.

丢弃无效MRRA请求报文

Discarded invalid MRRA response frame.

丢弃无效MRRA应答报文

Discarded invalid MR request frame.

丢弃无效MR请求报文

Discarded invalid MR response frame.

丢弃无效MR应答报文

Failed to send MR request frame, because the E-Port is down on interface *interface-name* in VSAN *vsan-id*.

发送MR请求报文失败，E端口处于down状态

Failed to send MR request frame on interface *interface-name* in VSAN *vsan-id*.

发送MR请求报文失败

Received MRRA request frame again on interface *interface-name* in VSAN *vsan-id*.

接收到重发的MRRA请求

Sent MRRA RJT response frame, because local switch status is in busy on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).

发送MRRA RJT响应报文，本地交换机处于busy状态，原因码是*reason-code*，解释码是*code-explanation*

【举例】

\# 启动两台互联的FC设备，打开FC Zone错误调试信息开关。在两台设备的VSAN 1下都进行不重复的大规模Zone配置，重新连接设备端口，会输出下列合并后报文长度超长的错误调试信息。

\<Sysname\> debugging fc zone error

\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/ERROR: The size of packet is too large, and isolated the E-port on interface Fc1/0/1 in VSAN 1.

*[// VSAN 1*]*内，封装MRRA请求向端口Fc1/0/1端口进行发送时，发现报文长度超出限制，隔离E端口*

\# 启动两台互联的FC设备，打开FC Zone事件调试信息开关。在其中一台VSAN 1下进行Zone配置，重新连接设备端口，会输出下列链路事件以及MERGE流程的事件调试信息。

\<Sysname\> debugging fc zone event

\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/EVENT: \"Delete Neighbor Event\" happened on interface Fc1/0/1 in VSAN 1.

*// 在VSAN 1内，端口Fc1/0/1上报发生删除邻居事件*

\*Oct 27 11:19:53:360 2010 Sysname FCZONE/7/EVENT: \"New Neighbor Event\" happened on interface Fc1/0/1 in VSAN 1.

*// 在VSAN 1内，端口Fc1/0/1上报发现新邻居事件*

\# 启动两台互联的FC设备，打开FC Zone报文调试信息开关。在其中一台VSAN 1下进行Zone配置，重新连接设备端口，会输出下列MERGE流程相关的调试信息。

\<Sysname\> debugging fc zone packet

\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/PACKET: Sent MRRA request frame successfully on interface Fc1/0/1 in VSAN 1.

*// 在VSAN 1内，从端口Fc1/0/1发送MRRA请求报文成功*

\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/PACKET: Received MRRA ACC response frame on interface Fc1/0/1 in VSAN 1.

*// 在VSAN1内，接收到MRRA ACC回应报文*

\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/PACKET: Sent MR request frame successfully on interface Fc1/0/1 in VSAN 1.

*// 在VSAN 1内， Fc1/0/1上发送MR请求报文成功*

\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/PACKET: Received MR ACC response frame on interfaceFc 1/0/1 in VSAN 1.

*// 在VSAN 1内，接收到MR ACC回应报文*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fcoe**

------------------------------------------------------------------------

【命令】

**[debugging fcoe**[ { **all** \| **error** \| **event** \| **packet** [ **fcm** \| **fip**   **receive** \| **send** ]  **interface** *interface*-*type* *interface*-*number*  \| **timer** }]]

**[undo**[ **debugging** **fcoe** { **all** \| **error** \| **event** \| **packet** [ **fcm** \| **fip**   **receive** \| **send** ]  **interface** *interface*-*type* *interface*-*number*  \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[fcm**]：表示经过封装的FC报文调试信息开关。

**[fip**]：表示FIP协议报文调试信息开关。

**[receive**]：表示接收报文调试信息开关。

**[send**]：表示发送报文调试信息开关。

**[interface ***interface*-*type* *interface*-*number*]：表示指定接口的调试信息开关，*interface*-*type*只能是VFC接口。如果未指定本参数，表示所有VFC接口的调试信息开关。

**[timer**]：表示定时器调试信息开关。

【描述】

**[debugging fcoe**]命令用来打开FCoE调试信息开关。**undo debugging fcoe**命令用来关闭FCoE调试信息开关。

缺省情况下，FCoE调试信息开关处于关闭状态。

需要注意的是：

·如果未指定**fcm**和**fip**参数，表示同时指定这两类报文。

·如果未指定**receive**和**send**参数，表示同时指定接收和发送的报文。

·通过**interface**参数打开的指定接口的调试信息开关，只能通过在**undo**命令中指定**interface**参数来关闭。

表1-27 debugging fcoe error命令输出信息描述表

字段

描述

Failed to notify driver that FCoE is enabled for VLAN *vlan-id* in VSAN *vsan-id*.

VLAN使能FCoE通报驱动失败

Failed to notify driver that FCoE is disabled for VLAN *vlan-id* in VSAN *vsan-id.*

VLAN去使能FCoE通报驱动失败

PhyIoCtl cmd *cmd* is unknown.

物理控制命令不存在

FCoE Smooth: Failed to get smooth binding data.

FCoE获取平滑的绑定信息失败

FCoE Smooth: Failed to get smooth mapping data.

FCoE获取平滑的VLAN与VSAN的映射信息失败

FCoE Smooth: Failed to get smooth VFC interface state data.

FCoE获取平滑的VFC接口状态信息失败

表1-28 debugging fcoe event命令输出信息描述表

字段

描述

Successfully created *Interface-name.*

成功创建VFC接口

Successfully deleted *Interface-name.*

成功删除VFC接口

*[Interface-name* was deleted.]

VFC接口被删除

*[Interface-name* was created.]

VFC接口被创建

*[Interface-name* physically went up.]

VFC接口物理状态变为up

VSAN *vsan-id*, interface *Interface-name* trunked the

VSAN

VFC接口trunk指定VSAN

VSAN *vsan-id*, interface *Interface-name* did not trunk the VSAN..

VFC接口去trunk指定VSAN

Received shutdown event of *Interface-name.*

收到VFC接口shutdown事件

Received undo-shutdown event of *Interface-name*.

收到VFC接口undo shutdown事件

Received phyIoCtl cmd *cmd* of *Interface-name*

收到以太网接口的物理控制命令

Notified shutdown event of *Interface-name*.

通知以太网接口shutdown事件

Notified undo-shutdown event of *Interface-name*.

通知以太网接口undo shutdown事件

Failed to deal with *Interface-name* event.

处理VFC接口事件失败

*[Interface-name* physically went down.]

VFC接口物理状态变为down

Notified driver to clear *Interface-name* in VLAN *vlan-id*

通报驱动在指定vlan内删除VFC接口信息

Notified driver to set *Interface-name* in VLAN *vlan-id*

通报驱动在指定vlan内设置VFC接口信息

VSAN *vsan-id*, interface *Interface-name*, failed to create the dead timer.

在指定VSAN内创建VFC接口的超时定时器失败

VSAN *vsan-id*, interface *Interface-name*, failed to create the advertisement timer.

在指定VSAN内创建VFC接口的非请求发现通告报文定时器失败

VSAN *vsan-id*, interface *Interface-name*, became up.

VFC接口在指定VSAN内变为up状态

VSAN *vsan-id*, interface *Interface-name*, became attempt.

VFC接口在指定VSAN内变为attempt状态

VSAN *vsan-id*, interface *Interface-name*, became down.

VFC接口在指定VSAN内变为down状态

VSAN *vsan-id*, interface *Interface-name,* notified FCLINK VN *FCID* down.

通知FCLINK VN down

VSAN *vsan-id*, interface *Interface-name,* notified FCLINK to change VFC state into down.

通知FCLINK在指定VSAN内VFC状态down

VSAN *vsan-id*, interface *Interface-name,* notified FCLINK to change VFC state into up.

通知FCLINK在指定VSAN内VFC状态up

interface *Interface-name,* notified FCLINK to change VFC state into down in all vsan.

通知FCLINK在所有VSAN内VFC状态down

VSAN *vsan-id*, interface *Interface-name,* notified FCLINK to smooth VFC state.

通知FCLINK平滑VFC状态

VLAN *vlan-id*, received VLAN destroying event.

收到删除指定vlan事件，vlan id为65535时表示批量事件

VLAN *vlan-id*, interface *Interface-name*, received adding port to VLAN event.

收到以太网接口加入指定vlan事件，vlan id为65535时表示批量事件

VLAN *vlan-id*, interface *Interface-name*, received deleting port from VLAN event.

收到以太网接口退出指定vlan事件，vlan id为65535时表示批量事件

Received Sync Bind message.

接收Sync模块的绑定信息

Received Sync VSAN message.

接收Sync模块的VSAN信息

Received Sync Debug message.

接收Sync模块的Debug信息

Received Sync Mapping message.

接收Sync模块的VLAN与VSAN的映射信息

Received Sync Restart message.

接收Sync模块的重启动信息

Received Sync Batch Backup Finish message

接收Sync模块的批备完成信息

表1-29 debugging fcoe packet fcm命令输出信息描述表

字段

描述

*[Interface-name* sent FCoE packet.]

VFC接口发送FCoE报文

*[Interface-name* received FCoE packet.]

VFC接口接收FCoE报文

Failed to send packet because *Interface-name* is not up.

VFC接口物理状态为非up状态，发送FCM报文失败

FCM Send: Successfully sent packet.

发送FCM报文成功

FCM Send: VFC interface is not bound with Ethernet interface, and discarded the packet.

VFC接口没有绑定到以太网接口，丢弃FCM报文

FCM Send: The Ethernet interface is not in the corresponding VLAN, and discarded the packet.

以太网接口没有在相应的VLAN里，丢弃FCM报文

FCM Send: Failed to encapsulate the VFT extended header, and discarded the packet.

封装VFT扩展头失败，丢弃FCM报文

FCM Send: Failed to append memory for CRC, and discarded the packet.

申请添加循环冗余校验码内存失败，丢弃FCM报文

FCM Send: Failed to prepend memory for SOF, and discarded the packet.

预分报文帧头内存失败，丢弃FCM报文

FCM Send: MAC is invalid, and the packet was discarded.

MAC地址非法，丢弃FCM报文

FCM Send: Failed to prepend memory for Eth header, and discarded the packet.

预分以太网报文头内存失败，丢弃FCM报文

FCM Send: Failed to send the packet to Eth link, and discarded the packet.

发送报文到以太网链路失败，丢弃FCM报文

FCM Send: Ethernet failed to send the packet.

以太网发送报文失败

FCM Send: Failed to relay the packet from master board.

从主板透传报文失败

FCM Receive: Successfully received FCM packet.

成功收到FCM报文

FCM Receive: VFC interface is not found by Ethernet interface and source MAC, and discarded the packet.

根据以太网接口和报文源MAC地址没有找到匹配的VFC接口，丢弃FCM报文

FCM Receive: Remote MAC does not match source MAC, and discarded the packet.

对端MAC地址与源MAC地址不匹配，丢弃FCM报文

FCM Receive: The packet has extension header, and was discarded.

存在扩展头，丢弃FCM报文

FCM Receive: CRC is invalid, and discarded the packet.

循环冗余校验码非法，丢弃FCM报文

FCM Receive: Link failed to send the packet, and discarded the packet.

链路发送报文失败，丢弃FCM报文

FCM Receive: VFC state is not up, and discarded the packet.

VFC接口状态为非up状态，丢弃FCM报文

FCM Receive: VLAN is not enabled with FCoE, and discarded the packet.

VLAN没有使能FCoE，丢弃FCM报文

FCM Receive: VSAN is not up, and discarded the packet.

VSAN没有up，丢弃FCM报文

FCM Receive: Successfully relayed the packet to master board.

成功透传报文到主板

FCM Receive: Failed to relay the packet to master board.

透传报文到主板失败

FCM Send: Failed to relay the packet to slot *slot-id*.

透传报文到接口板失败

FCM Send: Successfully relayed the packet to slot *slot-id*.

成功透传报文到接口板

Slot *slot-id* successfully received relay packet.

接口板成功收到透传报文

Master board successfully received relay packet.

主板成功收到透传报文

表1-30 debugging fcoe packet fip命令输出信息描述表

字段

描述

*[Interface-name* sent FIP packet.]

VFC接口发送FIP报文

*[Interface-name* received FIP packet.]

VFC接口接收FIP报文

FIP Receive: Ethernet *Interface-name* is not bound with VFC interface, and discarded the packet.

VFC接口没有绑定以太网接口，丢弃FIP报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received packet.

成功接收FIP报文

VSAN *vsan-id*, interface *Interface-name* ,FIP Receive: Source MAC is not equal to bound MAC, and discarded the packet

FIP报文的源MAC地址不等于绑定的MAC地址，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Destination MAC is not equal to local MAC, and discarded the packet

FIP报文的目的MAC地址不等于本地MAC地址，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to get FIP frame, and discarded the packet.

获取FIP帧失败，丢弃FIP报文

Interface *Interface-name*, FIP Receive-The socket head is invalid, and discarded the packet.

socket头非法，丢弃FIP报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC state is down, and discarded the packet.

VFC接口down，丢弃FIP报文

VLAN *vlan-id* interface *Interface-name*, FIP Receive: The VLAN is not enabled with FCoE.

VLAN未使能FCoE

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to get local MAC, and discarded the packet.

获取本地MAC地址失败，丢弃FIP报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: The version of FIP header is invalid, and discarded the packet.

FIP报文头类型非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: The length of description of FIP header is invalid ,and discarded the packet

FIP报文头描述符的长度非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP Protocol Code and FIP Subcode are invalid, and discarded the packet

FIP报文协议号和子码非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name* FIP Receive: FIP FP bit is invalid, and discarded the packet.

FIP报文FP位非法，丢弃报文

VSAN *vsan-id,* interface *Interface-name*, FIP Receive: VFC mode does not match the FIP F bit, and discarded the packet

VFC模式不匹配FIP报文的F位，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP S bit is invalid, and discarded the packet.

FIP报文S位非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP Description type is unknown, and discarded the packet

FIP报文描述符类型未指明，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP Description length is invalid, and discarded the packet

FIP报文描述符的长度非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: The count of FIP Description is invalid, and discarded the packet

FIP报文描述符的数量非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: MAC in FIP MAC Description does not match Remote MAC, and discarded the packet

FIP报文MAC描述符中的MAC地址不匹配对端MAC地址，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAX_FCOE_SIZE Description is invalid, and discarded the packet

FIP报文MAX FCOE SIZE描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP solicited unicast discovery advertisement packet length is invalid, and discarded the packet

FIP单播请求通告报文长度不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC state is invalid, and discarded the packet

VFC接口状态不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP A bit is invalid, and discarded the packet

FIP报文A位不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: MAC in FIP MAC Description does not match ETH-Source MAC, and discarded the packet

FIP报文MAC描述符中的MAC地址不匹配源端以太口的MAC地址，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP NameID Description is invalid, and  discarded the packet

FIP报文NameID描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP Fabric Description is invalid, and discarded the packet

FIP报文Fabric描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP FKA ADV Description is invalid, and discarded the packet

FIP报文FKA ADV描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP VxPort Description is invalid, and discarded the packet

FIP报文VxPort描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC does not trunk VSAN.

VFC接口没有加入到VSAN中

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent packet.

FIP报文发送成功

VLAN *vlan-id*, interface *Interface-name*, FIP Send: Ethernet link failed to send FIP packet.

链路发送FIP报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Send: The VFC is invalid.

发送FIP报文，VFC接口非法

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to encapsulate packet

发送FIP报文，封装报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to get interface mode

发送FIP报文，获取接口模式失败

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to get Ethernet interface.

发送FIP报文，获取以太网接口失败

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to get VLAN.

发送FIP报文，获取VLAN失败

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent clear packet.

发送Clear报文成功

VLAN *vlan-id*, interface *Interface-name*, FIP Send: Successfully sent unsolicited multicast advertisement packet.

发送组播非请求通告报文成功

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received clear packet.

接收Clear报文成功

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received unsolicited multicast advertisement packet.

接收组播非请求通告报文成功

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FP bit of FLOGI request packet is invalid, and discarded the packet

FLOGI请求报文的FP位非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC is not F Mode, and discarded the VLINK packet

VFC接口不是F模式，丢弃虚链路报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FIP Keep Alive packet.

成功收到FIP保活报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: The ENode failed to login, and discarded the packet.

ENode没有LOGIN，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent ELP SW_ACC packet.

成功发送ELP SW_ACC报文

VSAN *vsan-id*, interface *Interface-name*, bound MAC is not equal to ENode MAC, and discarded the packet.

绑定MAC与ENode MAC不同，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to get destination MAC.

获取目的MAC失败

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent solicited unicast discovery advertisement packet.

成功发送单播的请求发现通告报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received multicast solicitation packet.

接收组播的发现请求报文成功

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent multicast solicitation packet.

成功发送组播发现请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received solicited unicast discovery advertisement packet.

成功接收单播发现通告报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FC-MAP in FIP FC-MAP Description does not match local FC-MAP, and discarded the packet

FCMAP描述符中的FCMAP值与本地FCMAP不一致，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGI request packet to FCLINK.

成功发送FLOGI请求报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive:  Successfully sent FLOGO request packet to FCLINK.

成功发送FLOGO请求报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGI-request packet to FCLINK.

发送FLOGI请求报文给FCLINK失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGO request packet to FCLINK.

发送FLOGO请求报文给FCLINK失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: First Description of Instantiation packet is invalid, and discarded the packet

FIP实例化报文的第一个描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received VLAN request packet.

成功接收vlan请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGI request packet.

成功接收FLOGI请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: First Description of VLAN request packet is not MAC Description, and discarded the packet

vlan请求报文的第一个描述符不是MAC描述符，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP FLOGI Description is invalid, and discarded the packet

FIP报文的FLOGI描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent VLAN notification packet.

成功发送vlan通告报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGI LS_ACC packet.

成功发送FLOGI LS_ACC报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send:  Successfully sent FLOGO LS_ACC packet.

成功发送FLOGO LS_ACC报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: MAC address in MAC Description of FLOGI  packet is not zero, and discarded the packet

FIP FLOGI 报文MAC描述符的MAC地址不是全0，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of FLOGO packet is invalid, and discarded the packet

FIP FLOGO报文MAC描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGO request packet.

成功接收FLOGO请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGI LS_RJT packet.

成功发送FLOGI LS_RJT报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGO LS_RJT packet.

成功发送FLOGO LS_RJT报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent ELP SW_RJT packet.

成功发送ELP SW_RJT报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent ELP request packet.

成功发送ELP 请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received ELP request packet.

成功接收ELP请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive-Successfully received ELP SW_ACC packet.

成功接收ELP SW_ACC报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received ELP SW_RJT packet.

成功接收ELP SW_RJT报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of ELP packet is invalid, and discarded the packet

FIP ELP报文的MAC描述符非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Type of Vlink instantiation packet is invalid, and discarded the packet

虚链路实例化报文类型非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Command Code of FIP packet is invalid, and discarded the packet

FIP报文的Command Code字段非法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: VFC is down in VSAN, and discarded the packet.

VFC在VSAN内down，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive:  Successfully sent ELP request packet to FCLINK.

成功发送ELP请求报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent ELP SW_ACCpacket to FCLINK.

成功发送ELP SW_ACC报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive:  Successfully sent ELP SW_RJT packet to FCLINK.

成功发送ELP SW_RJT报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send ELP request packet to FCLINK.

发送ELP请求报文给FCLINK失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send ELP SW_ACC packet to FCLINK.

发送ELP SW_ACC 报文给FCLINK失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send ELP SW_RJT packet to FCLINK.

发送ELP SW_RJT报文给FCLINK失败

FIP Send: Successfully output packet of *Interface-name* in VSAN *vsan-id*,

成功在VSAN内发出VFC口的报文

FIP Send: Failed to output packet of *Interface-name* in VSAN *vsan-id*,

在VSAN内发出VFC口的报文失败

FIP Receive: Failed to input packet of *Interface-name* in VSAN *vsan-id*.

输入VSAN内VFC的报文失败

FIP Receive: Successfully input packet of *Interface-name* in VSAN *vsan-id*.

成功输入VSAN内VFC的报文

Failed to send packet because *Interface-name* state is not up in VSAN *vsan-id*.

VFC在VSAN内不是up，发送报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: First Description of Fip Keep Alive packet is not MAC Description, and discarded the packet.

FIP保活报文的第一个描述符不是MAC描述符，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGI request packet.

成功发送FLOGI请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FDISC request packet.

成功发送FDISC请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FDISC ACC packet.

成功发送FDISC ACC报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGO request packet.

成功发送FLOGO请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FDISC RJT packet.

成功发送FDISC RJT报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of FLOGI ACC packet is invalid, and discarded the packet.

FLOGI ACC报文MAC描述符不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of FDISC ACC packet is invalid, and discarded the packet.

FDISC ACC报文MAC描述符不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FP bit of FLOGI ACC packet is invalid, and discarded the packet.

FLOGI ACC报文FP位不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FP bit of FDISC request packet is invalid, and discarded the packet.

FDISC请求报文FP位不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FP bit of FDISC ACC packet is invalid, and discarded the packet.

FDISC ACC报文FP位不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGI ACC packet.

成功接收FLOGI ACC 报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGI RJT packet.

成功接收FLOGI RJT 报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FDISC packet.

成功接收FDISC报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FDISC ACC packet.

成功接收FDISC ACC报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FDISC RJT packet.

成功接收FDISC RJT报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGO ACC packet.

成功接收FLOGO ACC报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGO RJT packet.

成功接收FLOGO RJT报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VN does not exist, discarded the packet.

VN不存在，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGI ACC packet to FCLINK.

成功发送FLOGI ACC报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGI RJT packet to FCLINK.

成功发送FLOGI RJT报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FDISC packet to FCLINK.

成功发送FDISC报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FDISC ACC packet to FCLINK.

成功发送FDISC ACC报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FDISC RJT packet to FCLINK.

成功发送FDISC RJT报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGO ACC packet to FCLINK.

成功发送FLOGO ACC报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGO RJT packet to FCLINK.

成功发送FLOGO RJT报文给FCLINK

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGI ACC packet to FCLINK.

向FCLINK发送FLOGI ACC报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGI RJT packet to FCLINK.

向FCLINK发送FLOGI RJT报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FDISC packet to FCLINK.

向FCLINK发送FDISC报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FDISC ACC packet to FCLINK.

向FCLINK发送FDISC ACC报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FDISC RJT packet to FCLINK.

向FCLINK发送FDISC RJT报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGO ACC packet to FCLINK.

向FCLINK发送FLOGO ACC报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGO RJT packet to FCLINK.

向FCLINK发送FLOGO RJT报文失败

VSAN *vsan-id*, interface *Interface-name*, NPV received the empty clear packet.

NPV接收空的clear报文

VSAN *vsan-id*, interface *Interface-name*, NPV received the clear packet.

NPV接收clear报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to send clear packet because the mode is incorrect.

由于模式不正确，发送clear报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to Send FKA packet because the mode is incorrect.

由于模式不正确，发送FKA报文失败

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: MAC address in MAC Description of FDISC packet is not zero, and discarded the packet.

FDISC报文MAC描述符中的MAC地址不为零，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is NP, and discarded the solicitation packet.

VFC不是NP模式，丢弃发现请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is F, and discarded the clear packet.

VFC不是F模式，丢弃clear报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not F, and discarded the FLOGI request packet.

VFC不是F模式，丢弃FLOGI请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not NP, and discarded the FLOGI notification packet.

VFC不是NP模式，丢弃FLOGI通告报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not F, and discarded the FDISC request packet.

VFC不是F模式，丢弃FDISC请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not NP, and discarded the FDISC notification packet.

VFC不是NP模式，丢弃FDISC通告报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not F, and discarded the FLOGO request packet.

VFC不是F模式，丢弃FLOGO请求报文

VSAN *vsan-id*, interface *Interface-name*,  FIP Receive: VFC mode is not NP, and discarded the FLOGO notification packet.

VFC不是NP模式，丢弃FLOGO通告报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not E, and discarded the ELP packet.

VFC不是E模式，丢弃ELP报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of FLOGO ACC packet is invalid, and discarded the packet.

FLOGO ACC报文中MAC描述符不合法，丢弃报文

FIP Receive-Ethernet *Interface-nam*e, FPMA MAC does not match VFC interface, and discarded the packet.

FPMA MAC不匹配VFC接口，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received unsolicited multicast  advertisement packet, and VFC state is attempt.

VFC是attempt状态，成功接收组播非请求通告报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode does not match the multicast destination MAC, and discarded the packet.

VFC模式不匹配组播目的MAC，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not E, and discarded the received VLAN request packet.

VFC不是E模式，丢弃VLAN请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not E, and discarded the received Fip Keep Alive packet.

VFC不是E模式，丢弃FIP保活报文

VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent unicast solicitation packet.

成功发送单播请求报文

VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received unicast solicitation packet.

成功接收单播请求报文

Discarded a packet, because the port mode of VFC interface *Interface-name* in VSAN *vsan-id* is incorrect.

VFC模式与当前VSAN模式不匹配，丢弃报文

![说明](FC和FCoE%20Debug.files/image001.png)

如果FIP报文收发打印信息中的*vsan-id*为65535，则表示该VSAN信息无效。例如：设备在某VLAN中收到vlan请求报文时，如果该VLAN没有对应的映射VSAN，此时，debug信息中的*vsan-id*会打印为65535，此情况属于正常。

表1-31 debugging fcoe timer命令输出信息描述表

字段

描述

VSAN *vsan-id*, interface *Interface-name*, successfully started the advertisement timer.

在指定VSAN内成功启动VFC接口的非请求发现通告定时器

VSAN *vsan-id*, interface *Interface-name*, successfully started the dead timer.

在指定VSAN内成功启动VFC接口的超时定时器

VSAN *vsan-id*, interface *Interface-name*, successfully deleted the advertisement timer.

在指定VSAN内成功删除VFC接口的非请求发现通告定时器

VSAN *vsan-id*, interface *Interface-name*, successfully deleted the dead timer.

在指定VSAN内成功删除VFC接口的超时定时器

VSAN *vsan-id*, interface *Interface-name*, failed to create the dead timer.

指定VSAN内创建VFC接口超时定时器失败

VSAN *vsan-id*, interface *Interface-name*, failed to create the advertisement timer.

指定VSAN内创建VFC接口的通告定时器失败

VSAN *vsan-id*, interface *Interface-name*, successfully started the solicitation timer.

在指定VSAN内成功启动VFC接口的发现请求定时器

VSAN *vsan-id*, interface *Interface-name*, failed to create the solicitation timer.

在指定VSAN内创建VFC接口的发现请求定时器失败

VSAN *vsan-id*, interface *Interface-name*, successfully deleted the solicitation timer.

在指定VSAN内成功删除VFC接口的发现请求定时器

VSAN *vsan-id*, interface *Interface-name*, successfully started the dispersion timer.

在指定VSAN内成功启动VFC接口的离散定时器

VSAN *vsan-id*, interface *Interface-name*, failed to create the dispersion timer.

在指定VSAN内创建VFC接口的离散定时器失败

VSAN *vsan-id*, interface *Interface-name*, successfully deleted the dispersion timer.

在指定VSAN内成功删除VFC接口的离散定时器

VSAN *vsan-id*, interface *Interface-name*, successfully started the ENode dead timer.

在指定VSAN内成功启动VFC接口的ENode超时定时器

VSAN *vsan-id*, interface *Interface-name*, failed to create the ENode dead timer.

在指定VSAN内创建VFC接口的ENode超时定时器失败

VSAN *vsan-id*, interface *Interface-name*, successfully deleted the ENode dead timer.

在指定VSAN内成功删除VFC接口的ENode超时定时器

VSAN *vsan-id*, interface *Interface-name*, successfully created VN FKA timer.

成功创建VN FKA定时器

VSAN *vsan-id*, interface *Interface-name*, failed to create VN FKA timer.

创建VN FKA定时器失败

VSAN *vsan-id*, interface *Interface-name*, successfully deleted VN FKA timer.

成功删除VN FKA定时器

VSAN *vsan-id*, interface *Interface-name*, successfully created VN dead timer.

成功创建VN dead定时器

VSAN *vsan-id*, interface *Interface-name*, failed to create VN dead timer.

创建VN dead定时器失败

VSAN *vsan-id*, interface *Interface-name*, ENode FKA timed out.

ENode FKA定时器超时

VSAN *vsan-id*, interface *Interface-name*, dispersion timer timed out.

离散定时器超时

VSAN *vsan-id*, interface *Interface-name*, dead timer timed out.

dead定时器超时

VSAN *vsan-id*, interface *Interface-name*, VN *FCID* FKA timed out.

VN FKA定时器超时

VSAN *vsan-id*, interface *Interface-name*, VN *FCID* dead timed out.

VN dead定时器超时

VSAN *vsan-id*, interface *Interface-name*, successfully started the NP FCF dead timer.

成功启动NP FCF dead定时器

VSAN *vsan-id*, interface *Interface-name*, successfully started the NP ENode FKA timer.

成功启动NP ENode FKA定时器

VSAN *vsan-id*, interface *Interface-name*, failed to create the NP FCF dead timer.

创建NP FCF dead定时器失败

VSAN *vsan-id*, interface *Interface-name*, failed to create the NP ENode FKA timer.

创建NP ENode FKA定时器失败

VSAN *vsan-id*, interface *Interface-name*, successfully deleted the NP FCF dead timer.

成功删除NP FCF dead定时器

VSAN *vsan-id*, interface *Interface-name*, successfully deleted the NP ENode FKA timer.

成功删除NP ENode FKA定时器

The FKA timer in VLAN *vlan-id* will time out in *timeout* seconds.

VLAN *vlan-id*下的FKA定时器将在*timeout*秒后超时

The FKA timer in VLAN *vlan-id* timed out.

VLAN *vlan-id*下的FKA定时器超时

【举例】

\# 打开FCoE的错误调试信息开关。当接收错误的接口控制字时会输出下列调试信息。

\<Sysname\> debugging fcoe error

\*May 11 16:17:17:188 2011 Sysname FCOEK/7/ERROR: -MDC=1; PhyIoCtl cmd 17301526 is unknown

*// 物理控制命令不存在*

\# 打开FCoE的事件调试信息开关。当关闭VFC接口10时会输出下列调试信息。

\<Sysname\> debugging fcoe event

\*May 11 16:17:23:616 2011 Sysname FCOE/7/EVENT: -MDC=1; Vfc10 physically went down.

*[// VFC*]*接口物理状态变为down*

\*May 11 16:17:18:192 2011 Sysname FCOEK/7/EVENT: -MDC=1; Successfully deleted Vfc100.

\*May 11 16:17:18:192 2011 Sysname FCOE/7/EVENT: -MDC=1; Vfc100 was deleted.

*[// VFC*]*接口被删除*

\*May 11 16:17:29:616 2011 Sysname FCOEK/7/EVENT: -MDC=1; Notified driver to clear Vfc10 in VLAN 2.

*// 通知驱动删除VFC接口信息*

\# 打开FCoE的经过封装的FC报文调试信息开关。当以太网接口没有Trunk相应的VLAN时，发送报文会输出下列调试信息。

\<Sysname\> debugging fcoe packet fcm

\*May 11 16:14:10:288 2011 Sysname FCOEK/7/PACKET: -MDC=1; FCM Send： The Ethernet interface is not in the corresponding VLAN, and discarded the packet.

*// 以太网接口没有在相应的VLAN里，丢弃FCM报文*

\# 打开FCoE的FIP协议报文调试信息开关。当FCoE配置完成后会输出下列调试信息。

\<Sysname\> debugging fcoe packet fip

\*Oct 20 14:57:45:386 2011 Sysname FCOE/7/PACKET: -MDC=1; VSAN 10, interface Vfc2, FIP Receive：Successfully received multicast solicitation packet.

*[// [vfc]*]*接口2在VSAN 10下成功接收组播的发现请求报文*

\*Oct 20 14:57:45:386 2011 Sysname FCOE/7/PACKET: -MDC=1; VSAN 10, interface Vfc2, FIP Send：Successfully sent solicited unicast discovery advertise packet.

*[// [vfc]*]*接口2在VSAN 10下成功发送单播的请求发现通告报文*

\# 打开FCoE的定时器调试信息开关。当VFC接口物理层up时会输出下列调试信息。

\<Sysname\> debugging fcoe timer

\*Oct 20 14:57:49:849 2011 Sysname FCOE/7/TIMER: -MDC=1; VSAN 10, interface Vfc2, successfully deleted the send-solicitation timer.

*// 在VSAN 10内成功删除VFC接口2的发现请求定时器*

\*Oct 20 14:57:49:849 2011 Sysname FCOE/7/TIMER: -MDC=1; VSAN 10, interface Vfc2, successfully started the dead timer.

*// 在VSAN 10内成功启动VFC接口2的超时定时器*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fcoemgr**

------------------------------------------------------------------------

【命令】

**[debugging fcoemgr**[ { **all** \| **error** \| **event** \| **timer** }]]

**[undo debugging fcoemgr**[ { **all** \| **error** \| **event** \| **timer** }]]

【视图】

用户视图

【缺省级别】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[timer**]：表示定时器调试信息开关。

【描述】

**[debugging fcoemgr**]命令用来打开FCoE管理模块调试信息开关。**undo debugging fcoemgr**命令用来关闭FCoE管理模块调试信息开关。

缺省情况下，FCoE管理模块调试信息开关处于关闭状态。

表1-32 debugging fcoemgr error命令输出信息描述表

字段

描述

Failed to start the process of *process-id*.

启动进程失败

Failed to reply to synchronous message.

回复同步消息失败

表1-33 debugging fcoemgr event命令输出信息描述表

字段

描述

Received a notification about disable fcoe-mode from Master.

收到主板去使能FCoE模式的通知

Received a notification about the fcoe-mode enabled from Master.

收到主板使能FCoE模式的通知

Received a notification about start-service from Master.

收到主板开启服务的通知

Received insertion slot *slot-id* event.

收到接口板插入的事件

Start to enable the processes concerning the current fcoe-mode.

开启与当前FCoE模式关联的进程

Notify all the boards to start the services concerning fcoe-mode.

通知所有板开启与当前FCoE模式关联的进程

Notify all the boards to enable fcoe-mode.

通知所有板使能FCoE模式

Start to enable fcoe-mode.

使能FCoE模式

Start to disable current fcoe-mode.

去使能当前FCoE模式

Notify all the processes to disable fcoe-mode.

通知所有进程FCoE模式去使能

Received all the replys about disable fcoe-mode from the boards notified.

收到所有板FCoE模式去使能的通知

Received all the replys to enabling fcoe-mode from boards notified.

收到所有板FCoE模式使能的通知

Received all the replys to starting service from boards notified.

收到所有板开启服务的通知

Notify all the boards to disable fcoe-mode.

通知所有板FCoE模式去使能

【举例】

\# 打开FCoE管理模块的错误调试信息开关。

\<Sysname\> debugging fcoemgr error

\*Nov 9 06:16:10:111 2012 Sysname FCOEMGR/7/ERROR: -MDC=1; Failed to reply to synchronous message.

*// 回复同步消息失败*

\# 打开FCoE管理模块的事件调试信息开关。

\<Sysname\> debugging fip-snooping event

\*Nov 9 06:16:12:647 2012 Sysname FCOEMGR/7/EVENT: -MDC=1; Received insertion slot 3 event.

*// 收到接口板3插入的事件*

\*Nov 9 06:16:14:861 2012 Sysname FCOEMGR/7/EVENT: -MDC=1-Slot=3; Start to enable fcoe-mode.

*// 使能FCoE模式*

\*Nov 9 06:16:14:862 2012 Sysname FCOEMGR/7/EVENT: -MDC=1-Slot=3; Start to enable the processes concerning the current fcoe-mode.

*// 开启与当前FCoE模式关联的进程*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc-port-security**

------------------------------------------------------------------------

【命令】

**[debugging fc-port-security**[ { **all** \| **error** \| **event** \| **notify** }]]

**[undo debugging fc-port-security**[ { **all** \| **error** \| **event** \| **notify** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[notify**]：表示通知调试信息开关。

【描述】

**[debugging fc-port-security**]命令用来打开FC端口安全调试信息开关。**undo debugging fc-port-security**命令用来关闭FC端口安全调试信息开关。

缺省情况下，FC端口安全调试信息开关处于关闭状态。

表1-34 debugging fc-port-security error命令输出信息描述表

字段

描述

Failed to back up data in batch.

批备数据失败

Failed to change the standby MPU to the active state.

备用主控板倒换为主用主控板失败

Failed to send a message for clearing violation entries.

发送清除非法登录的信息失败

Failed to back up violation entries in batch in VSAN *vsan-id*.

在VSAN *vsan-id*内批备非法登录信息失败

Failed to back up statistics in batch in VSAN *vsan-id*.

在VSAN *vsan-id*内批备统计信息失败

Failed to send a check reply message.

发送登录权限检查回应信息失败

Failed to send a notification message to FCLINK.

向FCLINK发送通知消息失败

Failed to create an event re-initialization timer.

创建重新初始化事件定时器失败

Failed to create a smooth aging timer.

创建平滑老化定时器失败

Failed to create a login database in VSAN *vsan-id*.

在VSAN *vsan-id*内创建登录数据库失败

Failed to add a node to the login database in VSAN *vsan-id*.

在VSAN *vsan-id*内将节点加入登录数据库失败

Failed to add a switch to the login database in VSAN *vsan-id*.

在VSAN *vsan-id*内将交换机加入登录数据库失败

Failed to add a policy in VSAN *vsan-id*.

在VSAN *vsan-id*内添加策略失败

Failed to allocate an index for a new policy in VSAN *vsan-id*.

在VSAN *vsan-id*内为新的策略申请索引失败

Failed to create a policy database in VSAN *vsan-id*.

在VSAN *vsan-id*内创建策略数据库失败

Failed to find a matched violation entry and to add a new violation entry in VSAN *vsan-id*.

在VSAN *vsan-id*内没有找到非法登录表项且添加表项失败

Failed to get violation info by index (index = *index*-*id*) in VSAN *vsan-id*.

在VSAN *vsan-id*内通过索引获取非法登录信息失败

Failed to find a matched violation entry and to add a new violation entry on the standby MPU in VSAN *vsan-id*.

在VSAN *vsan-id*内备板上没有找到非法登录表项且添加表项失败

Failed to add check result *result-id* to the queue in VSAN *vsan-id*.

在VSAN *vsan-id*内将权限检查的结果加入到队列失败

Failed to add a switch violation entry (*interface-name,* sWWN *swwn*) to the queue in VSAN *vsan-id*.

在VSAN *vsan-id*内将交换机的非法登录信息(接口，*swwn*)加入到队列失败

Failed to add a node violation entry (*interface-name,* pWWN *pwwn*, nWWN nwwn) to the queue in VSAN *vsan-id*.

在VSAN *vsan-id*内将节点的非法登录信息(接口，*pwwn nwwn*)加入到队列失败

Failed to create a statistics and violation database in VSAN *vsan-id*.

在VSAN *vsan-id*内创建统计和非法登录数据库失败

表1-35 debugging fc-port-security event命令输出信息描述表

字段

描述

Received an event for creating VSAN *vsan-id*.

接收VSAN创建事件

Received an event for deleting VSAN *vsan-id*.

接收VSAN删除事件

Received a port activation event.

收到端口激活事件

Received a port deactivation event.

收到端口去激活事件

Received an event for a port joining an aggregate interface.

收到端口加入聚合口事件

Received a smooth start message.

收到平滑开始消息

Received a smooth end message.

收到平滑结束消息

Finished policy aging.

策略老化结束

The node with pWWN *pwwn* (nWWN *nwwn*) is logging in through *interface-name* in VSAN *vsan-id*.

在VSAN *vsan-id*内节点*pwwn*(*nwwn*)正在接口*interface-name*上登录

The node with pWWN *pwwn* (nWWN *nwwn*) has logged out from *interface-name* in VSAN *vsan-id*.

在VSAN *vsan-id*内节点*pwwn*(*nwwn*)在接口*interface-name*上下线

Link is up because the switch with sWWN *swwn* is logging in through *interface-name* in VSAN *vsan-id*.

在VSAN *vsan-id*内由于交换机*swwn*正在接口*interface-name*上登录，链路状态up

Link is down because the switch with sWWN *swwn* has logged out from *interface-name* in VSAN *vsan-id*.

在VSAN *vsan-id*内由于交换机*swwn*在接口*interface-name*上下线，链路状态down

表1-36 debugging fc-port-security notify命令输出信息描述表

字段

描述

The node with pWWN *pwwn* (nWWN *nwwn*) was allowed to log in through *interface-name* in VSAN *vsan-id* when a FLOGI event was received.

当收到FLOGI事件时，在VSAN *vsan-id*内允许节点*pwwn*(*nwwn*)在接口*interface-name*上登录

The node with pWWN *pwwn* (nWWN *nwwn*) was refused to log in through *interface-name* in VSAN *vsan-id* when a FLOGI event was received.

当收到FLOGI事件时，在VSAN *vsan-id*内拒绝节点*pwwn*(*nwwn*)在接口*interface-name*上登录

The switch with sWWN *swwn* was allowed to log in through *interface-name* in VSAN *vsan-id* when a link up event was received.

当收到链路up事件时，在VSAN *vsan-id*内允许交换机*swwn*在接口*interface-name*上登录

The switch with sWWN *swwn* was refused to log in through *interface-name* in VSAN *vsan-id* when a link up event was received.

当收到链路up事件时，在VSAN *vsan-id*内拒绝交换机*swwn*在接口*interface-name*上登录

The node with pWWN *pwwn* (nWWN *nwwn*) was allowed to log in through *interface-name* in VSAN *vsan-id* when a check request was received.

当收到权限检查请求时，在VSAN *vsan-id*内允许节点*pwwn*(*nwwn*)在接口*interface-name*上登录

The node with pWWN *pwwn* (nWWN *nwwn*) was refused to log in through *interface-name* in VSAN *vsan-id* when a check request was received.

当收到权限检查请求时，在VSAN *vsan-id*内拒绝节点*pwwn*(*nwwn*)在接口*interface-name*上登录

The switch with sWWN *swwn* was allowed to log in through *interface-name* in VSAN *vsan-id* when a check request was received.

当收到权限检查请求时，在VSAN *vsan-id*内允许交换机*swwn*在接口*interface-name*上登录

The switch with sWWN *swwn* was refused to log in through *interface-name* in VSAN *vsan-id* when a check request was received.

当收到权限检查请求时，在VSAN *vsan-id*内拒绝交换机*swwn*在接口*interface-name*上登录

Notify FCLINK to force the node with pWWN *pwwn* (nWWN *nwwn*) to log out from *interface-name* in VSAN *vsan-id*.

在VSAN *vsan-id*内通知FCLINK将节点*pwwn*(*nwwn*)从接口*interface-name*下线

Notify FCLINK to isolate *interface-name* in VSAN *vsan-id*.

通知FCLINK在VSAN *vsan-id*内将接口*interface-name*隔离

Notify FCLINK to force all logged-in devices to log out in VSAN *vsan-id*.

在VSAN *vsan-id*内通知FCLINK将所有已登录的设备下线

【举例】

\# 打开FC端口安全的错误调试信息开关。

\<Sysname\> debugging fc-port-security error

\*Dec 25 09:21:56:925 2013 Sysname FCPS/7/ERROR: -MDC=1; Failed to back up violation entries in batch in VSAN 2.

*// 批备非法登录信息失败*

\# 打开FC端口安全的事件调试信息开关和通知调试信息开关，当交换机登录时会输出下列调试信息。

\<Sysname\> debugging fc-port-security event

\<Sysname\> debugging fc-port-security notify

\*Mar 28 03:09:55:468 2014 SysnameFCPS/7/NOTIFY: -MDC=1; The switch with sWWN 10:00:00:e0:02:00:00:00 was allowed to log in through Fc1/0/5 in VSAN 2when a check request was received.

*// 收到权限检查请求时，交换机10:00:00:e0:02:00:00:00在VSAN 2内通过权限检查，允许其在接口FC1/0/5上登录*

\*Mar 28 03:09:55:471 2014 SysnameFCPS/7/EVENT: -MDC=1; Link is up because the switch with sWWN 10:00:00:e0:02:00:00:00 is logging in through Fc1/0/5 in VSAN 2.

*// 在VSAN 2内由于交换机10:00:00:e0:02:00:00:00在接口FC1/0/5上登录，链路状态up*

\*Mar 28 03:09:55:473 2014 SysnameFCPS/7/NOTIFY: -MDC=1; The switch with sWWN 10:00:00:e0:02:00:00:00 was allowed to log in through Fc1/0/5 in VSAN 2 when a link up event was received.

*// 收到链路up事件时，交换机10:00:00:e0:02:00:00:00在VSAN 2内通过权限检查，允许其在接口FC1/0/5上登录*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fcs**

------------------------------------------------------------------------

【命令】

**[debugging fcs **[{ **all** \| **error** \| **event** \| **packet** } [ **vsan** *vsan-id* ]]]

**[undo debugging fcs **[{ **all** \| **error** \| **event** \| **packet** } [ **vsan** *vsan-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[vsan** *vsan-id*]：表示指定VSAN的调试信息开关，*vsan-id*的取值范围为1～3839。如果未指定本参数，表示所有VSAN的调试信息开关。

【描述】

**[debugging fcs**]命令用来打开FCS调试信息开关。**undo debugging fcs**命令用来关闭FCS调试信息开关。

缺省情况下，FCS调试信息开关处于关闭状态。

表1-37 debugging fcs error命令输出信息描述表

字段

描述

VSAN *vsan-id*: invalid source FCID for FC ping request

VSAN *vsan-id*内fcping请求的源FCID非法

VSAN *vsan-id*:**invalid payload length for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内fcping请求的负载长度非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id*: invalid version for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内fcping请求的版本非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id*: invalid port tag for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内fcping请求的端口标签非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id*: invalid port length for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内fcping请求的端口长度非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*。

VSAN *vsan-id*: invalid FCID for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内fcping请求的FCID非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id* was processing the FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内fcping请求正在处理，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id*: invalid WWN for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内fcping请求的WWN非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id* failed to send echo request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内发送echo请求失败，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id*: invalid token value for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内fcping请求的token值非法，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id* failed to add FC ping session (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id*内添加fcping会话失败，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id*: invalid source FCID for FTR request.

VSAN *vsan-id*内FTR请求报文中的源FCID无效

VSAN *vsan-id*: invalid payload length for FTR request (source FCID = *src-fc-id*).

VSAN *vsan-id*内FTR请求的负载长度错误，源FCID为*src-fc-id*

VSAN *vsan-id:* invalid version for FTR request (source FCID = *src-fc-id*).

VSAN *vsan-id*内FTR请求的版本无效，源FCID为*src-fc-id*

VSAN *vsan-id*: invalid port for FTR request (source FCID = *src-fc-id*).

VSAN *vsan-id*内FTR请求的端口无效，源FCID为*src-fc-id*

VSAN *vsan-id*: invalid token value for FTR request (source FCID = *src-fc-id*).

VSAN *vsan-id*内FTR请求的token值无效，源FCID为*src-fc-id*

VSAN *vsan-id* was processing the FTR request (source FCID = *src-fc-id,* token = *token-value*).

VSAN *vsan-id*内FTR请求正在被处理，源FCID为*src-fc-id*，token值为*token-value*

VSAN *vsan-id*: source FCID and destination FCID of FTR request were not in the same zone.

VSAN *vsan-id*内FTR请求报文中的源FCID和目的FCID不在一个zone内。

VSAN *vsan-id* failed to add port when *interface-name* was link/physically up.

VSAN *vsan-id*内当接口*interface-name*链路/物理UP时，添加端口失败

VSAN *vsan-id*: invalid payload length.

VSAN *vsan-id*内报文负载长度非法

VSAN *vsan-id:* The max size in packet was less than minimum length of ACC payload.

VSAN *vsan-id*内报文中的max size小于ACC负载的最小长度

VSAN *vsan-id* failed to send *packet-type* ACC frame to domain *domain-id.*

VSAN *vsan-id*内向域*domain-id*发送*packet-type *ACC失败

VSAN *vsan-id* failed to send *packet-type* request to domain *domain-id.*

VSAN *vsan-id*内向域*domain-id*发送*packet-type*请求失败

VSAN *vsan-id*: IE WWN in the frame did not match local IE WWN

VSAN *vsan-id*内报文中的IE WWN与本地IE WWN不匹配

VSAN *vsan-id* failed to get CT register information.

VSAN *vsan-id*内获取CT注册信息失败

VSAN *vsan-id* failed to parse CT header.

VSAN *vsan-id*内解析报文CT头部失败

VSAN *vsan-id*: invalid GMI request with fragment ID *fragment-id* in domain *domain-id* (source FCID = *src-fc-id*, transaction ID = *transaction-id*, expected fragment ID = *fragment-id*).

VSAN *vsan-id*内向域*domain-id*发送分片ID为*fragment-id*的GMI请求非法，源FCID为*src-fc-id*，事务ID为*transaction-id*，预期的分片ID为*fragment-id*

VSAN *vsan-id* failed to find GMI session in domain *domain-id* (source FCID = *src-fc-id*, transaction ID = *transaction-id*).

VSAN *vsan-id*中域*domain-id*内，查找GMI session失败，源FCID为*src-fc-id*，事务ID为*transaction-id*

VSAN *vsan-id* failed to send *packet-type* packet (socket = *socket-id*, destination FCID = *dst-fc-id*).

VSAN *vsan-id*内发送*packet-type*报文失败，目的FCID是*dst-fc-id*，socket是*socket-id*

VSAN *vsan-id* failed to receive response packet with socket *socket-id*.

VSAN *vsan-id*内接收回应报文失败，socket是*socket-id*

VSAN *vsan-id* failed to create the socket for *packet-type* packet.

VSAN *vsan-id*内为*packet-type*报文创建socket失败

VSAN *vsan-id* failed to bind socket *socket-id* for *packet-type* packet.

VSAN *vsan-id*内为*packet-typ*报文绑定socket失败，socket是*socket-id*

VSAN *vsan-id* failed to receive request packet with socket *socket-id*.

VSAN *vsan-id*内从socket为*socket-id*接收请求报文失败

VSAN *vsan-id* failed to create *packet-type* timer for socket *socket-id*.

VSAN *vsan-id*内为socket *socket-id*的*packet-type*报文创建定时器失败

表1-38 debugging fcs event命令输出信息描述表

字段

描述

VSAN *vsan-id* successfully sent *count-value* FCS requests to domain *domain-id*.

VSAN *vsan-id*内成功发送*count-value*个FCS请求到域*domain-id*

VSAN *vsan-id* received *receiverespcount-value* responses in total for *sentreqcount-value* requests in domain *domain-id*.

在域*domain-id*内，VSAN *vsan-id*在发送请求*sentreqcount-value*个数中接收到的响应个数*receiverespcount-value*

VSAN *vsan-id*: Topology discovery aging timer timed out.

VSAN *vsan-id*内拓扑发现老化定时器超时

VSAN *vsan-id* processed *event* (*event-id*) event in *topostatus* (*topostatus-id*) state.

VSAN *vsan-id*内处理当前*topostatus-id*拓扑发现状态下有关的*event-id*事件

*[topostatus-id*]与*topostatus*取值及含义：

·1：inProgress，拓扑发现进行中状态

·2：completed，拓扑发现完成状态

·3：localOnly，拓扑发现未开始状态

*[event-id*]与*event*取值及含义：

·0：discovery start，拓扑发现开始

·1：discovery stop，拓扑发现停止

·2：GIEIL ACC packet，收到GIEIL ACC回应报文

·3：GFN ACC packet，收到GFN ACC回应报文

·4：GIELN ACC packet，收到 GIELN ACC回应报文

·5：GMAL ACC packet，收到GMAL ACC回应报文

·6：GPPN ACC packet，收到GPPN ACC回应报文

·7：GPSC ACC packet，收到GPSC ACC回应报文

·8：GPS ACC packet，收到GPS ACC回应报文

·9：GAPNL ACC packet，收到GAPNL ACC回应报文

·10：GPL ACC packet，收到GPL ACC回应报文

·11：GSES ACC packet，收到GSES ACC回应报文

·12：RJT packet，收到RJT拒绝报文

·13：packet sending failure，报文发送失败

·14：route deletion，路由删除事件

VSAN *vsan-id* successfully added port *Interfacename* when it was physically/link up.

VSAN *vsan-id*内当接口*Interfacename*物理/链路UP时，成功添加端口

VSAN *vsan-id* successfully deleted port *Interfacename* when it was physically/link down.

VSAN *vsan-id*内当接口*Interfacename*物理/链路DOWN时，成功删除端口

VSAN *vsan-id* successfully updated link attributes when *Interfacename* is link *up/down*.

VSAN *vsan-id*内，当接口*Interfacename*链路up/down时成功更新链路属性

VSAN *vsan-id* successfully deleted attached port *portname* of *Interfacename*.

VSAN *vsan-id*内成功删除接口*Interfacename*的附属连接端口*portname*

VSAN *vsan-id* successfully added attached port *portname* of *Interfacename*.

VSAN *vsan-id*内成功添加接口*Interfacename*的附属连接端口*portname*

VSAN *vsan-id* successfully added management address *managmentaddr-value*.

VSAN *vsan-id*内成功添加管理地址*managmentaddr-value*

VSAN *vsan-id* successfully deleted management address *managmentaddr-value*.

VSAN *vsan-id*内成功删除管理地址*managmentaddr-value*

VSAN *vsan-id* successfully updated WWN of local IE to *switchWWN-value*.

VSAN *vsan-id*内成功更新本地IE的WWN *switchWWN-value*

VSAN *vsan-id*: The *frame-value* frame timer timed out.

VSAN *vsan-id*内*frame-value*帧定时器超时

VSAN *vsan-id*: FTR timer timed out (source FCID = *src-fc-id,* token = *token-value*).

VSAN *vsan-id*内FTR定时器超时，源FCID是*src-fc-id*，token值是*token-value*

VSAN *vsan-id* received FC ping request frame from source FCID *fc-id*.

VSAN *vsan-id*内收到从FCID *fc-id*发送的fcping请求报文

VSAN *vsan-id* received domain ID change event, which changed from *domain-id1* to *domain-id2.*

VSAN *vsan-id*内收到域ID变化事件，域ID从*domain-id1*变到*domain-id*2

VSAN *vsan-id* received switch WWN change event, which changed from *wwn1* to *wwn2.*

VSAN *vsan-id*内收到交换机WWN变化事件，从*wwn1 *变到*wwn2*

VSAN *vsan-id* received route adding event of domain *domain-id*.

VSAN *vsan-id*内收到域*domain-id*的路由添加事件

VSAN *vsan-id* received route deleting event of domain *domain-id*.

VSAN *vsan-id*内收到域*domain-id*的路由删除事件

VSAN *vsan-id* received FLOGI event of port *port-wwn*.

VSAN *vsan-id*内收到端口*port-wwn*的flogin事件

VSAN *vsan-id* received FLOGO event of port *port-wwn*.

VSAN *vsan-id*内收到端口*port-wwn*的flogout事件

表1-39 debugging fcs packet命令输出信息描述表

字段

描述

VSAN *vsan-id* received *packet-type* RJT frame from domain *domain-id.*

VSAN *vsan-id*内从域*domain-id*接收到*packet-type*拒绝报文

VSAN *vsan-id* received *packet-type* ACC frame from domain *domain-id*.

VSAN *vsan-id*内从域*domain-id*接收到*packet-type *ACC报文

VSAN *vsan-id* received *packet-type* request from domain *domain-id*.

VSAN *vsan-id* 内从域*domain-id*接收到*packet-type*请求报文

VSAN *vsan-id* sent *packet-type* RJT frame to domain *domain-id* (reason code = *reason-code*, reason code explanation = *code-explanation*).

VSAN *vsan-id*内向域*domain-id*发送*packet-type*拒绝报文，原因码是*reason-code*，解释码是*code-explanation*

VSAN *vsan-id* sent *packet-type* ACC frame to domain *domain-id.*

VSAN *vsan-id* 内向域*domain-id*发送*packet-type *ACC报文

VSAN *vsan-id* sent *packet-type* request to domain *domain-id*.

VSAN *vsan-id* 内向域*domain-id*发送*packet-type*请求报文

VSAN *vsan-id* successfully sent FC ping ACC frame.

VSAN *vsan-id* 内成功发送fcping ACC报文

VSAN *vsan-id* sent FC ping reject frame (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*)*.

VSAN *vsan-id* 内发送fcping拒绝报文，源FCID是*src-fc-id*，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id* sent FTR ACC frame (destination FCID = *dst-fc-id*, token = *token-value*).

VSAN *vsan-id* 内发送FTR ACC报文，目的FCID是*dst-fc-id*，token值是*token-value*

VSAN *vsan-id* sent FTR RJT frame (destination FCID = *dst-fc-id*, reason code = *reason-code*, reason code explanation = *code-explanation*).

VSAN *vsan-id* 内发送FTR RJT报文，目的FCID是*dst-fc-id*，原因码是*reason-code*，解释码是*code-explanation*

VSAN *vsan-id* received FTR request frame (source FCID = *src-fc-id*).

VSAN *vsan-id* 内接收FTR请求报文，源FCID是*src-fc-id*

VSAN *vsan-id* received *packet-type* request packet (socket = *socket-id*, source FCID = *src-fc-id*).

VSAN *vsan-id* 内从socket *socket-id*接收到*packet-type*请求报文，源FCID是*src-fc-id*

VSAN *vsan-id* received *packet-type* response packet (socket =*socket-id*, source FCID = *src-fc-id*).

VSAN *vsan-id* 内从socket *socket-id*接收到*packet-type*回应报文，源FCID是*src-fc-id*

VSAN *vsan-id* successfully sent *packet-type* packet (socket =*socket-id*, destination FCID = *dst-fc-id*).

VSAN *vsan-id* 内发送*packet-type*报文成功，目的FCID是*dst-fc-id，*socket是*socket-id*

VSAN *vsan-id* received *packet-type* request from FCID *src-fc-id*.

VSAN *vsan-id* 内接收到*packet-type*请求报文，源FCID是*src-fc-id*

【举例】

\# 打开FCS错误调试信息开关。

\<Sysname\> debugging fcs error vsan 1

\*Aug 23 11:17:17:522 2012 Sysname FCGS/7/ERROR: -MDC=1; VSAN 1 failed to get CT register information.

*[// VSAN 1*]*内获取CT注册信息失败*

\# 打开FCS事件调试信息开关。

\<Sysname\> debugging fcs event vsan 1

\*Aug 23 11:05:42:640 2012 Sysname FCGS/7/EVENT: -MDC=1; VSAN 1 successfully added management address snmp://111.111.111.111.

*[// VSAN 1*]*内成功添加管理地址snmp://111.111.111.111*

\# 打开FCS报文调试信息开关。VSAN 1内发起拓扑发现时会输出下列调试信息。

\<Sysname\> debugging fcs packet vsan 1

\*Aug 26 09:35:44:853 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 25, destination FCID = fffc02).

*// 拓扑发现开始时向fffc02发送CT请求报文以区分以下要发送的报文*

\*Aug 26 09:35:44:853 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GFN request to domain 2

*// 拓扑发现开始时向域2发送GFN请求报文*

\*Aug 26 09:35:44:854 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 26, destination FCID = fffc02).

\*Aug 26 09:35:44:854 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GIELN request to domain 2.

*// 向域2发送GIELN请求报文*

\*Aug 26 09:35:44:856 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 27, destination FCID = fffc02).  

\*Aug 26 09:35:44:856 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GMAL request to domain 2.

*// 向域2发送GMAL请求报文*

\*Aug 26 09:35:44:858 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 28, destination FCID = fffc02).  

\*Aug 26 09:35:44:858 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GIEIL request to domain 2.

*// 向域2发送GIEIL请求报文*

\*Aug 26 09:35:44:862 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 29, destination FCID = fffc02).  

\*Aug 26 09:35:44:862 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GPL request to domain 2

*// 向域2发送GPL请求报文*

\*Aug 26 09:35:44:869 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 25, source FCID = fffc02).

\*Aug 26 09:35:44:870 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GFN ACC frame from domain 2.

*// 从域2接收GFN ACC回应报文*

\*Aug 26 09:35:44:871 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 26, source FCID = fffc02).

\*Aug 26 09:35:44:871 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GIELN ACC frame from domain 2.

*// 从域2接收GIELN ACC回应报文*

\*Aug 26 09:35:44:872 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 27, source FCID = fffc02).

\*Aug 26 09:35:44:872 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GMAL ACC frame from domain 2.

*// 从域2接收GMAL ACC回应报文*

\*Aug 26 09:35:44:873 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 28, source FCID = fffc02).

\*Aug 26 09:35:44:873 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GIEIL ACC frame from domain 2.

*// 从域2接收GIEIL ACC回应报文*

\*Aug 26 09:35:44:874 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 29, source FCID = fffc02).

\*Aug 26 09:35:44:874 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GPL ACC frame from domain 2.

*// 从域2接收GPL ACC回应报文*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fdmi**

------------------------------------------------------------------------

【命令】

**[debugging fdmi **[{ **all** \| **error** \| **event** \| **packet** } [ **vsan** *vsan-id* ]]]

**[undo debugging fdmi **[{ **all** \| **error** \| **event** \| **packet** } [ **vsan** *vsan-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[vsan** *vsan-id*]：表示指定VSAN的调试信息开关，*vsan-id*的取值范围为1～3839。如果未指定本参数，表示所有VSAN的调试信息开关。

【描述】

**[debugging fdmi**]命令用来打开FDMI调试信息开关。**undo debugging fdmi**命令用来关闭FDMI调试信息开关。

缺省情况下，FDMI调试信息开关处于关闭状态。

表1-40 debugging fdmi error命令输出信息描述表

字段

描述

VSAN *vsan-id* failed to get CT register information.

VSAN *vsan-id*内查找CT注册信息失败

VSAN *vsan-id* failed to parse CT header.

VSAN *vsan-id*内解析报文CT头部失败

VSAN *vsan-id* failed to receive request packet with socket *socket-id*.

VSAN *vsan-id*内接收socket *socket-id*的请求报文失败

VSAN *vsan-id* failed to receive response packet with socket *socket-id*.

VSAN *vsan-id*内接收socket *socket-id*的回应报文失败

VSAN *vsan-id* failed to create the socket for *packet-type* packet.

VSAN *vsan-id*内为*packet-type*报文创建socket失败

VSAN *vsan-id* failed to bind socket *socket-id* for *packet-type* packet.

VSAN *vsan-id*内为*packet-typ*报文绑定socket失败

VSAN *vsan-id* failed to create *packet-type* timer for socket *socket-id*.

VSAN *vsan-id*内为socket *socket-id*的*packet-type*报文创建定时器失败

VSAN *vsan-id* failed to send *packet-type* packet with socket *socket-id* to FCID *dst-fc-id*.

VSAN *vsan-id*内向socket *socket-id*发送报文类型为*packet-type*、目的FCID为*dst-fc-id*的报文失败

VSAN *vsan-id*: invalid GMI request with fragment ID *fragment-id* (source FCID = *src-fc-id*, transaction ID = *transaction-id*, expected fragment ID = *fragment-id*).

VSAN *vsan-id*内分片ID为*fragment-id*的GMI请求非法，源FCID为*src-fc-id*，事务ID为*transaction-id*，当前的分片ID为*fragment-id*

VSAN *vsan-id* failed to find GMI session in domain *domain-id* (source FCID = *src-fc-id*, transaction ID = *transaction-id*).

VSAN *vsan-id*中域*domain-id*内，查找GMI session失败，源FCID为*src-fc-id*，事务ID为*transaction-id*

VSAN *vsan-id* failed to get CT register information.

VSAN *vsan-id*内查找CT注册信息失败

VSAN *vsan-id* failed to parse FDMI header.

VSAN *vsan-id* 内解析FDMI报文头失败

VSAN *vsan-id*: invalid command code *command-code* in HBA request.

VSAN *vsan-id*内HBA请求中命令码不合法

VSAN *vsan-id* failed to get switch WWN of domain *domain-id*.

VSAN *vsan-id*内获取域*domain-id*的交换机WWN失败

VSAN *vsan-id* failed to add GMI session (source FCID = *src-fc-id*, transaction ID = *transaction-id*, fragment ID = *fragment-id*).

VSAN *vsan-id*内添加GMI会话失败，报文源FCID为*src-fc-id*，事务ID为*transaction-id*，分片ID为*fragment-id*

表1-41 debugging fdmi event命令输出信息描述表

字段

描述

VSAN *vsan-id*: GMI frame timer timed out.

VSAN *vsan-id*内GMI报文定时器超时

VSAN *vsan-id* received FLOGO event of port *port-wwn*.

VSAN *vsan-id*内收到端口*port-wwn*的flogout事件

VSAN *vsan-id* received domain ID change event, which changed from *domain-id1* to *domain-id2*.

VSAN *vsan-id*内收到域ID变化事件，域ID从*domain-id1*变到*domain-id*2

VSAN *vsan-id* received route adding event of domain *domain-id*.

VSAN *vsan-id*内收到域*domain-id*的路由添加事件

VSAN *vsan-id* received route deleting event of domain *domain-id*.

VSAN *vsan-id*内收到域*domain-id*的路由删除事件

VSAN *vsan-id*: FETCH timer of domain *domain-id* timed out.

VSAN *vsan-id*内域*domain-id*下FETCH定时器超时

VSAN *vsan-id*: *packet-name* frame timer of domain *domain-id* timed out.

VSAN *vsan-id*内域*domain-id*下*packet-name*报文定时器超时

VSAN *vsan-id* successfully added GMI session (source FCID = *src-fc-id*, transaction ID = *transaction-id*, fragment ID = *fragment-id*).

VSAN *vsan-id*内添加GMI会话成功，报文源FCID为*src-fc-id*，事务ID为*transaction-id*，分片ID为*fragment-id*

VSAN *vsan-id* successfully deleted HBA *hba-id* in domain *domain-id* for principal switch conflict.

VSAN *vsan-id*内处理主管理交换机冲突，域*domain-id*中删除HBA为*hba-id*成功

表1-42 debugging fdmi packet命令输出信息描述表

字段

描述

VSAN *vsan-id*: The HBAPKT module sent *packet-type* RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).

VSAN *vsan-id*内HBA报文处理模块发送*packet-type*的拒绝报文到目的FCID *dst-fc-id*，错误原因码是*reasoncode-id*，错误原因解释码是*explain-id*，处理结果是*return-value*

VSAN *vsan-id*: The HBAREG module sent *packet-type* RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).

VSAN *vsan-id*内HBA注册报文处理模块发送*packet-type*的拒绝报文到目的FCID *dst-fc-id*，错误原因码是*reasoncode-id*，错误原因解释码是*explain-id*，处理结果是*return-value*

VSAN *vsan-id*: The FORWPKT module sent *packet-type (original-pkt-name)* RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).

VSAN *vsan-id*内转发报文处理模块发送*packet-type1(original-pkt-name)*的拒绝报文到目的FCID *dst-fc-id*，错误原因码是*reasoncode-id*，错误原因解释码是*explain-id*，处理结果是*return-value*

VSAN *vsan-id*: The HBAREG module sent *packet-type* ACC frame to FCID *dst-fc-id* (return value = *return-value*).

VSAN *vsan-id*内HBA注册报文处理模块发送*packet-type*的ACC报文到目的FCID *dst-fc-id*，处理结果是*return-value*

VSAN *vsan-id*: The FORWPKT module sent *packet-type* ACC frame to FCID *dst-fc-id* (return value = *return-value*).

VSAN *vsan-id*内转发报文处理模块发送*packet-type*的ACC报文到目的FCID *dst-fc-id*，处理结果是*return-value*

VSAN *vsan-id* received *packet-type* request packet with socket *socket-id* from FCID *src-fc-id*.

VSAN *vsan-id*内成功收到*packet-type*请求报文，socket ID为*socket-id*，源FCID是*src-fc-id*

VSAN *vsan-id* received *packet-type* response packet with socket *socket-id* from FCID *src-fc-id.*

VSAN *vsan-id*内成功收到*packet-type*回应报文，socket ID为*socket-id*，源FCID是*src-fc-id*

VSAN *vsan-id* successfully sent *packet-type* packet with socket *socket-id* to FCID *dst-fc-id*.

VSAN *vsan-id*内成功发送*packet-type*报文到目的FCID *dst-fc-id*，socket ID为*socket-id*

VSAN *vsan-id*: The HBAGET module sent *packet-type* ACC frame to FCID *dst-fc-id* (return value = *return-value*).

VSAN *vsan-id*内HBA报文处理模块发送*packet-type*的ACC报文到目的FCID *dst-fc-id*，处理结果是*return-value*

VSAN *vsan-id*: The HBAGET module sent *packet-type* RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).

VSAN *vsan-id*内HBA报文处理模块发送*packet-type*的拒绝报文到目的FCID *dst-fc-id*，错误原因码是*reasoncode-id*，错误原因解释码是*explain-id*，处理结果是*return-value*

VSAN *vsan-id* received *packet-type* request from FCID *src-fc-id*.

VSAN *vsan-id*内收到源FCID为*src-fc-id*的报文类型为*packet-type*的请求报文

VSAN *vsan-id* received *packet-type* ACC frame from FCID *src-fc-id.*

VSAN *vsan-id*内收到源FCID为*src-fc-id*的报文类型为*packet-type*的ACC报文

VSAN *vsan-id*: The NOTIPKT module sent *notify-pkt-name*(*original-pkt-name*) ACC frame to FCID *dst-fc-id* (return value = *return-value*).

VSAN *vsan-id*内通知报文处理模块发送*notify-pkt-name*(*original-pkt-name*)的ACC报文到目的FCID *dst-fc-id*，处理结果是*return-value*

VSAN *vsan-id*: The NOTIPKT module sent *notify-pkt-name*(*original-pkt-name*) RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).

VSAN *vsan-id*内通知报文处理模块发送*notify-pkt-name*(*original-pkt-name*)的RJT报文到目的FCID *dst-fc-id*，错误原因码是*reasoncode-id*，错误原因解释码是*explain-id*，处理结果是*return-value*

VSAN *vsan-id* received *packet-type* RJT frame from FCID *src-fc-id*.

VSAN *vsan-id* 内收到源FCID为src-fc-id的报文类型为*packet-type*的拒绝报文

VSAN *id*: The NOTIPKT module sent *packet-type* request to FCID *dst-fc-id* (return value = *return-value*).

VSAN *vsan-id*内通知报文处理模块发送报文类型为*packet-type*的通知报文，目的FCID是*dst-fc-id*，返回值是*return-value*

VSAN vsan-*id*: The FORWPKT module sent *packet-type* request to FCID *dst-fc-id* (return value = *return-value*).

VSAN *vsan-id*内转发报文处理模块发送报文类型为*packet-type*的转发报文，目的FCID是*dst-fc-id*，返回值是*return-value*

VSAN *vsan-id*: The FORWPKT module sent RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).

VSAN *vsan-id* 内转发报文处理模块发送拒绝报文，错误原因码是*reasoncode-id*，错误原因解释码是*explain-id*，目的FCID *dst-fc-id*，返回值是*return-value*

VSAN *vsan-id*: The FORWPKT module sent ACC frame to FCID *dst-fc-id* (return value = *return-value*).

VSAN *vsan-id*内转发报文处理模块发送ACC报文到目的FCID *dst-fc-id*，处理结果是*return-value*

VSAN *vsan-id* send FETCH request to domain *domain-id* (return value = *return-value*).

VSAN *vsan-id*内发送FETCH请求到域* domain-id*，处理结果是*return-value*

VSAN *vsan-id* send GHAT request to domain *domain-id* (HBA ID = *hba-id,* return value = *return-value*).

VSAN *vsan-id*内发送GHAT请求报文到域*domain-id*，HBA为*hba-id*，处理结果是*return-value*

VSAN *vsan-id* send GPAT request to domain *domain-id* (port name = *port-wwn*, return value = *return-value*).

VSAN *vsan-id*内发送GPAT请求报文到域*domain-id*，端口名为*port-wwn*，处理结果是*return-value*

【举例】

\# 打开FDMI错误调试信息开关。

\<Sysname\> debugging fdmi error vsan 2

\*Dec 25 09:21:56:925 2012 Sysname FDMI/7/ERROR: -MDC=1; VSAN 2: invalid command code 0x0220 in HBA request.

*[// VSAN 2*]*内，HBA请求中的命令码0x0220不合法*

\# 打开FDMI事件调试信息开关。

\<Sysname\> debugging fdmi event vsan 2

\*Dec 25 09:12:54:991 2012 Sysname FDMI/7/EVENT: -MDC=1; VSAN 2 received FLOGO event of port e2:01:00:11:22:00:03:01.

*[// VSAN 2*]*内，收到端口WWN为e2:01:00:11:22:00:03:01的端口的FLOGO事件*

\# 打开FDMI报文调试信息开关。

\<Sysname\> debugging fdmi packet vsan 2

\*Dec 25 09:03:47:325 2012 Sysname FDMI/7/PACKET: -MDC=1; VSAN 2 received HBA request packet with socket 13 from FCID 010000.

*[// VSAN 2*]*内，从FCID为010000的节点收到HBA请求报文*

\*Dec 25 09:03:47:325 2012 Sysname FDMI/7/PACKET: -MDC=1; VSAN 2 received RHBA request from FCID 010000.

*[// VSAN 2*]*内，从FCID为010000的节点收到RHBA请求报文*

\*Dec 25 09:03:47:330 2012 Sysname FDMI/7/PACKET: -MDC=1; VSAN 2 successfully sent ACC packet with socket 13 to FCID 010000.

*[// VSAN 2*]*内，成功向FCID为010000的节点发送ACC回应报文*

\*Dec 25 09:03:47:330 2012 Sysname FDMI/7/PACKET: -MDC=1; VSAN 2: The HBAREG module sent RHBA ACC frame to FCID 010000 (return value = 0).

*[// VSAN 2*]*内，成功向FCID为010000的节点发送RHBA ACC报文*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fip-snooping**

------------------------------------------------------------------------

【命令】

**[debugging fip-snooping**[ { **all** \| **error** \| **event** \| **packet** [ **receive** \| **send** ] \| **rule** \| **session** \| **timer** }  [ **vlan** *vlan-id* \| **interface** *interface-type* *interface-number* ]]]

**[undo debugging fip-snooping**[ { **all** \| **error** \| **event** \| **packet** [ **receive** \| **send** ] \| **rule** \| **session** \| **timer** } [ **vlan** *vlan-id* \| **interface** *interface-type* *interface-number* ]]]

【视图】

用户视图

【缺省级别】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[receive**]：表示接收报文调试信息开关。

**[send**]：表示发送报文调试信息开关。

**[rule**]：表示规则调试信息开关。

**[session**]：表示会话调试信息开关。

**[timer**]：表示定时器调试信息开关。

**[vlan ***vlan-id*]：表示指定VLAN的调试信息开关，*vlan-id*的取值范围为1～4094。如果未指定本参数，表示所有VLAN的调试信息开关。

**[interface ***interface*-*type* *interface*-*number*]：表示指定接口的调试信息开关，*interface*-*type*只能是二层以太网接口或二层聚合接口。如果未指定本参数，表示所有二层以太网接口和二层聚合接口的调试信息开关。

【描述】

**[debugging fip-snooping**]命令用来打开FIP Snooping调试信息开关。**undo debugging fip-snooping**命令用来关闭FIP Snooping调试信息开关。

缺省情况下，FIP Snooping调试信息开关处于关闭状态。

需要注意的是：

·如果未指定**receive**和**send**参数，表示同时指定接收和发送的报文。

·通过**interface**参数打开的指定接口的调试信息开关，只能通过在**undo**命令中指定**interface**参数来关闭。

表1-43 debugging fip-snooping error命令输出信息描述表

字段

描述

VLAN *vlan-id*, interface *Interface-name*, Discarded a packet for receiving interface mode was FCF.

丢弃源接口模式是FCF的报文

VLAN *vlan-id*, interface *Interface-name*, Received VLAN Request packet.

接收到VLAN请求报文

VLAN *vlan-id*, interface *Interface-name*, Discarded a packet for receiving interface mode was ENode.

丢弃源接口模式是ENode的报文

VLAN *vlan-id*, interface *Interface-name*, Received a packet with incorrect length.

接收到错误长度的报文

VLAN *vlan-id*, interface *Interface-name*, Discarded a packet for relevant VLAN was not enabled with FIP Snooping.

该VLAN的FIP Snooping功能没有开启，丢弃报文

VLAN *vlan-id*, interface *Interface-name*, Failed to send the packet.

发送报文失败

VLAN *vlan-id*, Failed to send the packet.

发送报文失败

VLAN *vlan-id*, interface *Interface-name*,  Discarded a Discovery Advertisement for the FCF-MAC had been saved under interface *Interface-name*.

丢弃FCF-MAC已经被接口储存的发现通告报文

VLAN *vlan-id*, interface *Interface-name*, Discarded a packet from FCF for the source and destination MAC addresses were both FCF-MAC.

丢弃源和目的MAC都是FCF-MAC的报文

VLAN *vlan-id*, interface *Interface-name*, Discarded a Discovery Advertisement for FC-MAP value was  different from that locally configured.

丢弃FC-MAP值和现有配置不同的发现通告报文

VLAN *vlan-id*, interface *Interface-name*, The Discovery Advertisement had incorrect FIP Name_Identifier descriptor length.

该发现通告报文有长度不正确的FIP名称描述符

VLAN *vlan-id*, interface *Interface-name*, The Discovery Advertisement had incorrect FIP Fabric descriptor length.

该发现通告报文有长度不正确的FIP Fabric描述符

VLAN *vlan-id*, interface *Interface-name*, The Discovery Advertisement had incorrect FIP FKA_ADV_Period descriptor length.

该发现通告报文有长度不正确的FKA_ADV_Period描述符

VLAN *vlan-id*, interface *Interface-name*, The sum of the FIP Descriptor lengths of the packets was longer than FIP Descriptor List Length.

这些报文的FIP描述符长度和长于FIP描述符表长度

VLAN *vlan-id*, interface *Interface-name*, The FIP Descriptor length of the packet is zero.

报文的FIP描述符长度是零

VLAN *vlan-id*, interface *Interface-name*, Invalid FKA_ADV_PERIOD in Discovery Advertisement.

发现通告报文有无效的FKA_ADV_PERIOD

VLAN *vlan-id*, interface *Interface-name*, Failed to create FCF maintenance timer.

创建FCF维护定时器失败

VLAN *vlan-id*, interface *Interface-name*, Discarded a packet from ENode for the source MAC was FCF-MAC.

丢弃从ENode端口来的源MAC是FCF-MAC的报文

VLAN *vlan-id*, interface *Interface-name*, Discarded a Discovery Advertisement for its version was not supported.

丢弃版本不支持的发现通告报文

VLAN *vlan-id*, interface *Interface-name*, Discarded a Discovery Advertisement for the D bit was set to 1 in FIP FKA_ADV_Period descriptor.

丢弃FIP FKA_ADV_Period 描述符D比特位设置为1的发现通告报文

VLAN *vlan-id*, interface *Interface-name*, Discarded a Discovery Advertisement for the number of FCF sessions had reached maximum.

丢弃FCF会话到达最大数目的发现通告报文

VLAN *vlan-id*, interface *Interface-name*, Failed to get FIP Name_Identifier descriptor.

获取FIP Name_Identifier描述符失败

VLAN *vlan-id*, interface *Interface-name*, Failed to get FIP Fabric descriptor.

获取FIP Fabric描述符失败

VLAN *vlan-id*, interface *Interface-name*, Failed to get FIP FKA_ADV_Period descriptor.

获取FIP FKA_ADV_Period描述符失败

VLAN *vlan-id*, interface *Interface-name*, Discarded a packet from ENode for the destination MAC was not All-FCF-MACs or FCF-MAC.

丢弃从ENode端口来的目的MAC不是ALL-FCF-MACs或FCF-MAC的报文

VLAN *vlan-id*, interface *Interface-name*, Discarded the packet from FCF for the destination MAC was not All-ENode-MACs and the source MAC was not FCF-MAC.

丢弃从FCF端口来的目的MAC不是ALL-ENode-MACs和源MAC不是FCF-MAC的报文

VLAN *vlan-id*, interface *Interface-name*, Failed to get FIP MAC address descriptor.

获取FIP MAC地址描述符失败

VLAN *vlan-id*, interface *Interface-name*, Discarded a FLOGI or FDISC ACC for the VN_Port MAC mismatched the FC-MAP configured.

丢弃 VN_Port MAC与FC-MAP配置不符的FLOGI 或FDISC ACC报文

VLAN *vlan-id*, interface *Interface-name*, Failed to get ENode WWN.

获取ENode WWN失败

VLAN *vlan-id*, interface *Interface-name*, Discarded Virtual Link Instantiation Request for the session had been saved under interface *Interface-name*.

会话已经被其它接口保存，丢弃此虚链路实例化请求

VLAN *vlan-id*, interface *Interface-name*, Unknown type of Virtual Link Instantiation packet.

虚链路实例化报文的类型是未知的

VLAN *vlan-id*, interface *Interface-name*, Discarded Virtual Link Instantiation Reply for the destination MAC was All-ENode-MACs.

丢弃目的MAC是ALL-ENode-MACs的虚链路实例化回应

VLAN *vlan-id*, interface *Interface-name*, Discarded Virtual Link Instantiation Request for the destination MAC was All-FCF-MACs.

丢弃目的MAC是ALL-FCF-MACs的虚链路实例化请求

VLAN *vlan-id*, interface *Interface-name*, Discarded FIP Keep Alive for the destination MAC was All-FCF-MACs.

丢弃目的MAC是ALL-FCF-MACs的FIP保活报文

VLAN *vlan-id*, interface *Interface-name*, Failed to create ENode maintenance timer.

创建ENode维护定时器失败

VLAN *vlan-id*, interface *Interface-name*, Discarded Discovery Solicitation for source MAC was FPMA.

丢弃源MAC是FPMA的请求发现报文

VLAN *vlan-id*, interface *Interface-name*, Discarded Virtual Link Instantiation Request for source MAC was FPMA.

丢弃源MAC是FPMA的虚链路实例化请求

VLAN *vlan-id*, interface *Interface-name*, Discarded the packet for the number of FLOGI sessions had reached maximum.

丢弃FLOGI会话达到最大值的报文

VLAN *vlan-id*, interface *Interface-name*, Discarded FIP VN Keep Alive packet for session was not found.

丢弃会话未找到的FIP VN保活报文

VLAN *vlan-id*, interface *Interface-name*, Failed to find outgoing interface for the packet.

未找到报文转发出接口

表1-44 debugging fip-snooping event命令输出信息描述表

字段

描述

Sent VLAN Request packet.

发送VLAN请求报文

VLAN *vlan-id*, Received deleting VLAN event.

接收VLAN删除事件

Interface *Interface-name*, Received VLAN events for deleting the interface from the VLANs.

接收批量的端口离开VLAN事件

VLAN *vlan-id*, interface *Interface-name*, Received a VLAN event for deleting the interface from the VLAN.

接收端口离开某个VLAN事件

Interface *Interface-name*, Received interface link down event.

接收到接口链路连接断开事件

Interface *Interface-name*, Received interface inactive event.

接收到接口不活跃事件

Interface *Interface-name*, Received interface joining aggregation group event.

接收到接口加入聚合组事件

Interface *Interface-name*, Received deleting interface event.

接收到删除接口事件

Interface *Interface-name*, The packet had incorrect FIP MAC address descriptor length.

报文包含不正确的FIP MAC地址描述符长度

表1-45 debugging fip-snooping packet命令输出信息描述表

字段

描述

Received a packet with invalid socket header and discarded it.

接收到并抛弃socket头无效的报文

VLAN *vlan-id*, interface *Interface-name*, Received VLAN Notification packet.

接收到VLAN通告报文

VLAN *vlan-id*, interface *Interface-name*, Received packet of unknown type.

接收到未知类型的报文

VLAN *vlan-id*, interface *Interface-name*, Received a packet with incorrect length

接收到长度错误的报文

VLAN *vlan-id*, Sent the packet.

发送报文

VLAN *vlan-id*, Sent VLAN Request packet.

发送VLAN请求报文

VLAN *vlan-id*,  Sent VLAN Notification packet.

发送VLAN通告报文

VLAN *vlan-id*, interface *Interface-name*, Received unsolicited multicast Discovery Advertisement packet.

接收到组播非请求发现通告报文

VLAN *vlan-id*, Sent Discovery Advertisement packet.

发送发现通告报文

VLAN *vlan-id*, interface *Interface-name*, Received multicast Discovery Solicitation packet.

收到组播发现请求报文

VLAN *vlan-id*, Sent multicast Discovery Solicitation packet.

发送组播发现请求报文

VLAN *vlan-id*, interface *Interface-name*, Discarded a packet for the source interface state was invalid.

丢弃源接口状态无效的报文

VLAN *vlan-id*, interface *Interface-name*, Sent unicast Discovery Solicitation packet.

发送单播发现请求报文

VLAN *vlan-id*, interface *Interface-name*, Sent Virtual Link Instantiation Request packet.

发送虚链路实例化请求报文

VLAN *vlan-id*, interface *Interface-name*, Sent Virtual Link Instantiation ACC packet.

发送虚链路实例化ACC报文

VLAN *vlan-id*, interface *Interface-name*, Received FLOGI ACC packet.

接收到FLOGI ACC报文

VLAN *vlan-id*, interface *Interface-name*, Sent FIP Keep Alive packet.

发送FIP保活报文

VLAN *vlan-id*, interface *Interface-name*, Received ENode FIP Keep Alive packet.

接收到ENode FIP保活报文

VLAN *vlan-id*, interface *Interface-name*, Received a packet with invalid source MAC and discarded it.

接收并丢弃源MAC无效的报文

VLAN *vlan-id*, interface *Interface-name*, Received a packet with invalid destination MAC and discarded it.

接收并丢弃目的MAC无效的报文

VLAN *vlan-id*, Sent Virtual Link Instantiation Reply packet.

发送虚链路实例化应答报文

VLAN *vlan-id*, interface *Interface-name*, Sent Virtual Link Instantiation Reply packet.

发送虚链路实例化应答报文

VLAN *vlan-id*, interface *Interface-name*, Received VN_Port FIP Keep Alive packet.

接收到VN_Port FIP保活报文

VLAN *vlan-id*, interface *Interface-name*, Received unicast Discovery Solicitation packet.

接收单播发现请求报文

VLAN *vlan-id*, interface *Interface-name*, Received solicited unicast Discovery Advertisement packet.

接收单播请求的发现通告报文

VLAN *vlan-id*, interface *Interface-name*, Received FLOGI Request packet.

接收FLOGI请求报文

VLAN *vlan-id*, interface *Interface-name*, Received FDISC Request packet.

接收FDISC请求报文

VLAN *vlan-id*, interface *Interface-name*, Received FLOGO Request packet.

接收FLOGO请求报文

VLAN *vlan-id*, interface *Interface-name*, Received FDISC ACC packet.

接收FDISC ACC报文

VLAN *vlan-id*, interface *Interface-name*, Received FLOGI RJT packet.

接收FLOGI RJT报文

VLAN *vlan-id*, interface *Interface-name*, Received FDISC RJT packet.

接收FDISC RJT报文

VLAN *vlan-id*, interface *Interface-name*, Received FLOGO ACC packet.

接收FLOGO ACC报文

VLAN *vlan-id*, interface *Interface-name*, Received FLOGO RJT packet.

接收FLOGO RJT报文

VLAN *vlan-id*, interface *Interface-name*, Discarded FIP Clear packet for the destination MAC was All-ENode-MACs

丢弃目的MAC是ALL-ENode-MAC的FIP Clear报文

VLAN *vlan-id*, interface *Interface-name*, Received FIP Clear packet.

接收FIP Clear报文

VLAN *vlan-id*, Sent FIP Clear packet.

发送FIP Clear报文

VLAN *vlan-id*, interface *Interface-name*, Sent FIP Clear packet.

发送FIP Clear报文

表1-46 debugging fip-snooping rule命令输出信息描述表

字段

描述

VLAN *vlan-id*, interface *Interface-name*, Prepared to add rule {SA: mac-*address* / *mask length*; DA: *mac-address* / *mask length*}

准备添加规则

VLAN *vlan-id*, interface *Interface-name*, Prepared to delete rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.

准备删除规则

VLAN *vlan-id*, interface *Interface-name*, Began to add rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.

开始添加规则

VLAN *vlan-id*, interface *Interface-name*, Began to delete rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.

开始删除规则

VLAN *vlan-id*, interface *Interface-name*, Failed to add rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.

添加规则失败

VLAN *vlan-id*, interface *Interface-name*, Successfully added rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.

成功添加规则

VLAN *vlan-id*, interface *Interface-name*, Successfully deleted rule {SA: *mac-address* / *mask length*, DA: *mac-address* / *mask length*}.

成功删除规则

VLAN *vlan-id*, interface *Interface-name*, Failed to delete rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.

删除规则失败

Received terminal event.

收到终端事件

表1-47 debugging fip-snooping session命令输出信息描述表

字段

描述

VLAN *vlan-id*, interface *Interface-name*, Added MAC *mac-address* to {FCFs}.

添加MAC到{FCFs}

VLAN *vlan-id*, interface *Interface-name*, Deleted MAC *mac-address* from {FCFs}.

从{FCFs}删除MAC

VLAN *vlan-id*, interface *Interface-name*, Refreshed ENode temp session with exchange *exchange-id.*

刷新ENode临时会话，exchange为*exchange-id*

VLAN *vlan-id*, interface *Interface-name*, Added ENode temp session with exchange *exchange-id.*

添加ENode临时会话，exchange为*exchange-id*

VLAN *vlan-id*, interface *Interface-name*, Deleted ENode temp session with exchange *exchange-id*.

删除ENode临时会话，exchange为*exchange-id*

VLAN *vlan-id*, interface *Interface-name*, Refreshed ENode FLOGI session with VN_Port MAC *mac-address*.

刷新ENode FLOGI会话，VN_Port MAC为*mac-address*

VLAN *vlan-id*, interface *Interface-name*, Added ENode FLOGI session with VN_Port MAC *mac-address.*

添加ENode FLOGI 会话，VN_Port MAC为*mac-address*

VLAN *vlan-id*, interface *Interface-name*, Deleted ENode FLOGI session with VN_Port MAC *mac-address.*

删除ENode FLOGI会话，VN_Port MAC为*mac-address*

VLAN *vlan-id*, interface *Interface-name*, Refreshed FCF session with FCF-MAC *mac-address.*

刷新FCF会话，FCF-MAC为*mac-address*

VLAN *vlan-id*, interface *Interface-name*, Refreshed to-be-reflushed ENode rule with [VN_Port MAC *mac-address.*]

刷新ENode正在下刷的规则，FCF-MAC为*mac-address*

VLAN *vlan-id*, interface *Interface-name*, Refreshed to-be-reflushed FCF rule with FCF-MAC *mac-address.*

刷新FCF正在下刷的规则，FCF-MAC为*mac-address*

表1-48 debugging fip-snooping timer命令输出信息描述表

字段

描述

VLAN *vlan-id*, interface *Interface-name*, Created FCF maintenance timer.

创建FCF维护定时器

VLAN *vlan-id*, interface *Interface-name*, Deleted FCF maintenance timer.

删除FCF维护定时器

VLAN *vlan-id*, interface *Interface-name*, FCF maintenance timer timed out with FCF-MAC *mac-address*.

FCF维护定时器超时

VLAN *vlan-id*, interface *Interface-name*, Age timer timed out.

Age定时器超时

VLAN *vlan-id*, interface *Interface-name*, Created ENode maintenance timer.

创建ENode维护定时器

VLAN *vlan-id*, interface *Interface-name*, Deleted ENode maintenance timer.

删除ENode维护定时器

VLAN *vlan-id*, interface *Interface-name*, ENode maintenance timer timed out.

ENode维护定时器超时

VLAN *vlan-id*, interface *Interface-name*, VN maintenance timer timed out.

VN维护定时器超时

【举例】

\# 打开FIP Snooping的错误调试信息开关。当shutdown接口时会输出下列调试信息。

\<Sysname\> debugging fip-snooping error

\*Aug 15 14:30:08:413 2012 Sysname FIPS/7/ERROR: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Failed to find outgoing interface for the packet.

*// 未找到报文转发出接口*

\*Aug 15 14:30:08:419 2012 Sysname FIPS/7/ERROR: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Discarded a packet from FCF for the source and destination MAC addresses were both FCF-MAC.

*// 丢弃FCF端口收到的目的MAC为FCF-MAC的报文*

\# 打开FIP Snooping的事件调试信息开关。当删除VLAN 3时会输出下列调试信息。

\<Sysname\> debugging fip-snooping event

\*Aug 15 14:21:06:778 2012 Sysname FIPS/7/EVENT: -MDC=1; VLAN 3, interface GigabitEthernet1/0/1, Received a VLAN event for deleting the interface from the VLAN.

*// 接收接口GigabitEthernet1/0/1离开VLAN 3事件*

\*Aug 15 14:21:06:778 2012 Sysname FIPS/7/EVENT: -MDC=1; VLAN 3, interface GigabitEthernet1/0/2, Received a VLAN event for deleting the interface from the VLAN.

*// 接收接口GigabitEthernet1/0/2离开VLAN 3事件*

\*Aug 15 14:21:06:778 2012 Sysname FIPS/7/EVENT: -MDC=1; VLAN 3, Received deleting VLAN event.

*// 接收删除VLAN 3事件*

\# 打开FIP Snooping报文调试信息开关。当VLAN 10内FIP Snooping下规则成功后会输出下列调试信息。

\<Sysname\> debugging fip-snooping packet

\*Aug 15 14:42:33:108 2012 Sysname FIPS/7/PACKET: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Received unsolicited multicast Discovery Advertisement packet.

*// 接收到组播非请求发现通告报文*

\*Aug 15 14:42:33:108 2012 Sysname FIPS/7/PACKET: -MDC=1; VLAN 10, Sent Discovery Advertisement packet.

*// 发送发现通告报文*

\*Aug 15 14:42:33:188 2012 Sysname FIPS/7/PACKET: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Received ENode FIP Keep Alive packet.

*// 收到ENode FIP保活报文*

\*Aug 15 14:42:33:188 2012 Sysname FIPS/7/PACKET: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Sent FIP Keep Alive packet.

*// 发送FIP保活报文*

\# 打开FIP Snooping的规则调试信息开关。当FIP Snooping配置完成后shutdown ENode模式的接口会输出下列调试信息。

\<Sysname\> debugging fip-snooping rule

\*Aug 15 14:38:10:785 2012 Sysname FIPS/7/RULE: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Prepared to delete rule {SA:0efc-0001-0001/48; DA:0000-1234-0a01/48}.

*// 准备删除规则*

\*Aug 15 14:38:10:785 2012 Sysname FIPS/7/RULE: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Began to delete rule {SA:0efc-0001-0001/48; DA:0000-1234-0a01/48}.

*// 开始删除规则*

\*Aug 15 14:38:10:785 2012 Sysname FIPS/7/RULE: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Successfully deleted rule {SA:0efc-0001-0001/48; DA:0000-1234-0a01/48}.

*// 成功删除规则*

\# 打开FIP Snooping会话调试信息开关。当VLAN 10下FIP Snooping下规则成功会一直输出下列调试信息。

\<Sysname\> debugging fip-snooping sessions

\*Aug 15 14:35:34:510 2012 Sysname FIPS/7/SESSION: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Refreshed FCF session with FCF-MAC 0000-1234-0a01.

*// 以FCF-MAC刷新FCF会话*

\# 打开FIP Snooping的定时器调试信息开关。当端口物理连接down时会输出下列调试信息。

\<Sysname\> debugging fip-snooping timer

\*Aug 15 14:09:07:591 2012 Sysname FIPS/7/TIMER: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Deleted ENode maintenance timer.

*// 删除接口GigabitEthernet1/0/2的ENode维护定时器*

\*Aug 15 14:09:07:592 2012 Sysname FIPS/7/TIMER: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Deleted FCF maintenance timer.

*// 删除接口GigabitEthernet1/0/1的FCF维护定时器*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fspf**

------------------------------------------------------------------------

【命令】

**[debugging fspf**[ { **all** \| **error** \| **event** \| **flood \| ha \| lsr** \| **packet \| spf \| timer** } [ **vsan** *vsan-id* ]]]

**[undo debugging fspf**[ { **all** \| **error** \| **event** \| **flood \| ha \| lsr** \| **packet \| spf \| timer** } [ **vsan** *vsan-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[flood**]：表示LSR泛洪调试信息开关。

**[ha**]：表示高可靠性调试信息开关。

**[lsr**]：表示LSR调试信息开关。

**[packet**]：表示报文调试信息开关。

**[spf**]**：**表示路由计算调试信息开关。

**[timer**]：表示定时器调试信息开关。

**[vsan** *vsan-id*]：表示指定VSAN的调试信息开关，*vsan-id*的取值范围为1～3839。如果未指定本参数，表示所有VSAN的调试信息开关。

【描述】

**[debugging fspf**]命令用来打开FSPF调试信息开关。**undo debugging fspf**命令用来关闭FSPF调试信息开关。

缺省情况下，FSPF调试信息开关处于关闭状态。

表1-49 debugging fspf error命令输出信息描述表

字段

描述

Failed to create VSAN *vsan-id*.

创建VSAN失败

Failed to process domain-change event because VSAN *vsan-id* does not exist.

由于VSAN不存在，处理domain变化事件失败

The checksum of the LSR is incorrect, and it should be *number* instead of *number.*

LSR校验和不正确

VSAN *vsan-id*, interface *Interface-name*, failed to process link-up event.

处理链路UP事件失败

表1-50 debugging fspf event命令输出信息描述表

字段

描述

VSAN *vsan-id*, successfully flushed LSR.

刷新LSR成功

VSAN *vsan-id*, the flag for generating LSR is cleaned up.

清除生成LSR的标记

VSAN *vsan-id*, failed to generate a new LSR.

生成新的LSR失败

VSAN *vsan-id*, failed to flush LSR.

刷新LSR失败

VSAN *vsan-id*, successfully generated a new LSR.

生成新的LSR成功

VSAN *vsan-id*, failed to generate a new LSR because the interval is less than Min_Ls_Interval.

由于时间间隔小于最小时间间隔，生成新的LSR失败

VSAN *vsan-id,* set up the flag for generating LSR.

设置生成LSR的标记

VSAN *vsan-id*, successfully installed the LSR which is the same as local LSR.

成功安装与本地相同的LSR

VSAN *vsan-id*, successfully installed the LSR and calculated route.

成功安装LSR，并且触发路由计算

VSAN *vsan-id*, the incarnation reaches the maximal number and the LSR will be flushed.

incarnation达到最大值，刷新该LSR

Received VSAN *vsan-id* creation event.

收到VSAN创建事件

Received VSAN *vsan-id* deletion event.

收到VSAN删除事件

VSAN *vsan-id*, received domain-change event from *domain-id1* to *domain-id2*.

收到domain变化事件

VSAN *vsan-id*, changed domain from *domain-id1* to *domain-id2*.

Domain从一个值变到另一个值

VSAN *vsan-id*, interface *Interface-name*, received link-up event in E-mode.

接口E模式下收到链路UP事件

VSAN *vsan-id*, interface *Interface-name*, received link-down event in E-mode.

接口E模式下收到链路down事件

VSAN *vsan-id*, interface *Interface-name*, received *event-type* event in *state* state.

在某种状态下收到某种事件

VSAN *vsan-id*, interface *Interface-name*, the neighbor entered *state* state.

邻居进入某种状态

VSAN *vsan-id*, interface *Interface-name*, successfully created the new interface.

成功创建新的接口

VSAN *vsan-id*, interface *Interface-name*, successfully deleted the interface.

成功删除接口

VSAN *vsan-id*, interface *Interface-name*, reset the neighbor and initialized the neighbor structure.

重启邻居并且初始化邻居结构

Interface *Interface-name*, received the baud rate change event.

收到波特率变化事件

Interface *Interface-name*, received interface deletion event.

收到接口删除事件

Interface *Interface-name*, received interface deactivation event.

收到接口去激活事件

VSAN *vsan-id*, failed to enable FSPF.

使能FSPF失败

VSAN *vsan-id*, terminated new LSR generation because of Graceful Restart.

由于平滑重启，终止新的LSR生成

表1-51 debugging fspf flood命令输出信息描述表

字段

描述

VSAN *vsan-id*, flooded the LSR with domain *domain-id*.

泛洪LSR

表1-52 debugging fspf ha命令输出信息描述表

字段

描述

VSAN *vsan-id*, interface *Interface-name*, cleared the flag for Restarter.

清除Restarter标志

VSAN *vsan-id*, entered GR Restarter role.

进入GR Restarter角色

VSAN *vsan-id*, exited from GR Restarter role.

退出GR Restarter角色

VSAN *vsan-id*, interface *Interface-name*, originating Domain_ID field of FSPF header is different from the locally saved one, and failed to enter GR Helper role.

FSPF头中originating Domain_ID字段和本地保存不一致，不能进入GR Helper角色

VSAN *vsan-id*, interface *Interface-name*, set up the flag for Restarter.

设置Restarter标志

VSAN *vsan-id*, interface *Interface-name*, cleared the flag for Helper.

清除Helper标志

VSAN *vsan-id*, interface *Interface-name*, set up the flag for Helper.

设置Helper标志

VSAN *vsan-id*, interface *Interface-name*, neighbor state was not full, and failed to enter GR Helper role.

邻居状态非full，不能进入GR Helper角色

VSAN *vsan-id*, interface *Interface-name*, already in GR Helper role.

已经是GR Helper角色

VSAN *vsan-id*, interface *Interface-name*, GR Helper was not enabled, and failed to enter GR Helper role.

GR Helper没有使能，不能进入GR Helper角色

表1-53 debugging fspf lsr命令输出信息描述表

字段

描述

VSAN *vsan-id*, cleared all LSR in LSDB.

清除链路状态数据库中所有的LSR

VSAN *vsan-id*, added a LSR to LSDB: Link State Identifier is *domain-id*, Number of Links is *number.*

向链路状态数据库中添加一条LSR，链路状态标识符为LSR所属交换机的域ID，链路数量为LSR中包含link的个数

VSAN *vsan-id*, Link ID is *number*, Output Port is *Interface-name*, Neighbor Port is *Interface-name*, Link Cost is n*umber*.

Link ID为对端交换机的域ID，Output Port为源接口索引，Neighbor port为目的端接口索引，Link Cost为链路的开销

VSAN *vsan-id*, deleted a LSR from LSDB: Link State Identifier is *domain-id*, Number of Links is *number.*

从链路状态数据库中删除一条LSR，链路状态标识符为LSR所属交换机的域ID，链路数量为LSR中包含link的个数

VSAN *vsan-id*, the LSR not in LSDB: Link State Identifier is *domain-id*.

链路状态数据库中不存在该LSR，链路状态标识符为LSR所属交换机的域ID

VSAN *vsan-id*, interface *Interface-name*, successfully added a LSR to acklist with domain *domain-id*.

成功向ACK列表中添加一条LSR

VSAN *vsan-id*, interface *Interface-name*, successfully added a LSR to retrlist with domain *domain-id*.

成功向重传列表添加一条LSR

表1-54 debugging fspf packet命令输出信息描述表

字段

描述

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Failed to find FSPF interface by VSAN and interface index, and discarded the packet.

根据VSAN和接口索引查找不到FSPF接口信息，丢弃报文

VSAN *vsan-id*, interface *Interface-name, packet-type* Receive: Neighbor state is down, and discarded the packet.

邻居状态为down，丢弃报文

VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: SID field of FC header is incorrect, and discarded the packet.

FC头的SID字段错误，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: DID field of FC header is incorrect, and discarded the packet.

FC头的DID字段错误，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: The length of FSPF header is incorrect, and discarded the packet.

FSPF头长度错误，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Command field of FSPF header is invalid, and discarded the packet.

FSPF头的命令字段不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Version field of FSPF header is incorrect, and discarded the packet.

FSPF头的版本字段错误，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Authentication Type field of FSPF header is incorrect, and discarded the packet.

FC头的认证类型错误，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Originating Domain_ID field of FSPF header is invalid, and discarded the packet.

FSPF头的源Domain_ID字段不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Originating Domain_ID field of FSPF header conflicts with local Domain_ID, and discarded the packet.

FSPF头的源Domain_ID和本地Domain_ID有冲突，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Originating Domain_ID field of FSPF header is different from the locally saved one, and discarded the packet.

FSPF头的源Domain_ID和本地保存的Domain_ID不同，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Authentication field of FSPF header is incorrect, and discarded the packet.

FSPF头的认证字段错误，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: The length of hello packet is incorrect, and discarded the packet.

Hello报文长度错误，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Recipient Domain_ID field of 2-way hello packet is invalid, and discarded the packet.

2-way hello报文的Recipient Domain_ID字段不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Hello_Interval field of hello packet mismatches the local Hello_Interval, and discarded the packet.

Hello报文的Hello_Interval不匹配本地的Hello_Interval，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Dead_Interval field of hello packet mismatches the local Dead_Interval, and discarded the packet.

Hello报文的Dead_Interval不匹配本地的Dead_Interval，丢弃报文

VSAN *vsan-id*, interface *Interface-name, packet-type* Receive: Originating Domain_ID field of 2-way hello is different from the locally save one, and discarded the packet.

2-way hello报文的源Domain_ID和本地保存的Domain_ID不相等，丢弃报文

VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: Originating Port Index field of 2-way hello is different from the locally saved one, and discarded the packet.

2-way hello报文的源端口索引和本地保存的不相等，丢弃报文

VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: Recipient Domain_ID field of 2-way hello is different from local Domain_ID, and discarded the packet.

2-way hello报文的Recipient Domain_ID和本地的 Domain_ID不相等，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: The length of LSU packet is incorrect, and discarded the packet.

LSU报文的长度错误，丢弃报文

VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: Flags filed of LSU packet mismatches the Number of LSRs field, and discarded the packet.

LSU报文的flags标记不匹配LSR的数量，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: The length of LSA packet is incorrect, and discarded the packet.

LSA报文的长度不合法，丢弃报文

VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: Flags filed of LSA packet mismatches the Number of LSRs field, and discarded the packet.

LSA报文的flags标记不匹配LSR数量，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Neighbor state was init, and discarded the packet.

邻居状态是init状态，丢弃报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Memory was not enough to complete the operation.

没有足够的内存去完成操作

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received 1-way Hello packet.

成功收到1-way hello报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received 1-way hello packet with GR flag.

成功收到带有GR标志的1-way hello报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received initialized LSU packet.

成功收到初始化的LSU报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received LSA with LSR headers packet.

成功收到带有LSR头的LSA报文

Packet Receive: The input interface index is invalid.

入接口索引无效

Packet Receive: VSAN ID is invalid.

VSAN无效

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent 1-way hello packet.

成功发送1-way hello报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent 1-way hello packet with GR flag.

成功发送带有GR标志的1-way hello报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Failed to create socket.

创建socket失败

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Failed to bind the socket.

绑定socket失败

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Failed to add to epoll.

加入epoll失败

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent 2-way hello packet.

成功发送2-way hello报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent 2-way hello packet with GR flag.

成功发送带有GR标志的2-way hello报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Failed to send the packet.

发送报文失败

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received 2-way hello packet.

成功接收2-way hello报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received 2-way hello packet with GR flag.

成功接收带有GR标志的2-way hello报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received empty LSU packet.

成功接收空LSU报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received update LSU packet.

成功接收更新LSU报文

VSAN *vsan-id*, interface *Interface-name*, successfully checked a received LSR.

检查接收的LSR成功

VSAN *vsan-id*, interface *Interface-name*, Length field of a received LSR is invalid, and discarded the LSR.

接收的LSR长度不合法，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, Checksum field of a received LSR is incorrect, and discarded the LSR.

接收的LSR校验和错误，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, LSR type field of a received LSR is incorrect, and discarded the LSR.

接收的LSR类型错误，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, Link State Identifier field of a received LSR is invalid, and discarded the LSR.

接收的LSR链路状态字段不合法，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, Advertising Domain_ID field of a received LSR is invalid, and discarded the LSR.

接收的LSR通告Domain_ID不合法，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, Link State Identifier field of a received LSR does not equal Advertising Domain_ID field, and discarded the LSR.

接收LSR的链路状态字段不等于通告Domain_ID，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, LSR Age field of a received LSR is invalid, and discarded the LSR.

接收的LSR age字段不合法，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, Incarnation Number field of a received LSR is invalid, and discarded the LSR.

接收的LSR Incarnation Numbe 字段不合法，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, Number of LSR links of a received LSR mismatches LSR Length field, and discarded the LSR.

接收的LSR数量不匹配LSR长度，丢弃该LSR

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent initialized LSU packet.

成功发送初始化的LSU报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent empty LSU packet.

成功发送空的LSU报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent updated LSU packet.

成功发送更新的LSU报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent LSA with LSR headers packet.

成功发送带有LSR头的LSA报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent empty LSA packet.

成功发送空的LSA报文

VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received empty LSA packet.

成功接收空的LSA报文

VSAN *vsan-id*, interface *Interface-name*, successfully checked a received LSR header.

成功检查接收的LSR头

VSAN *vsan-id*, interface *Interface-name*, LSR type field of a received LSR header is incorrect, and ignored the LSR.

接收的LSR头中LSR类型不正确，忽略该LSR

VSAN *vsan-id*, interface *Interface-name*, Link State Identifier field of a received LSR header is invalid, and ignored the LSR.

接收的LSR头中Link State Identifier字段不合法，忽略该LSR

VSAN *vsan-id*, interface *Interface-name*, Advertising Domain_ID field of a received LSR header is invalid, and ignored the LSR.

接收的LSR头中Advertising Domain_ID字段不正确，忽略该LSR

VSAN *vsan-id*, interface *Interface-name*, Link State Identifier field of a received LSR header does not equal Advertising Domain_ID field, and ignored the LSR.

接收的LSR头中Link State Identifier字段和Advertising Domain_ID字段不相等，忽略该LSR

VSAN *vsan-id*, interface *Interface-name*, LSR Age field of a received LSR header is invalid, and ignored the LSR.

接收的LSR头中LSR Age字段不合法，忽略该LSR

VSAN *vsan-id*, interface *Interface-name*, Incarnation Number field of a received LSR header is invalid, and ignored the LSR.

接收的LSR头中Incarnation Number字段不合法，忽略该LSR

VSAN *vsan-id*, interface *Interface-name*, packet-type Receive: Received empty LSA without having sent empty LSU, and discarded the packet.

没有发送空LSU报文却接收空LSA报文，丢弃该报文

VSAN *vsan-id*, interface *Interface-name*, the LSR is ignored because the interval is less than Min_LS_Arrival

接收间隔值没有达到最小间隔值，忽略该LSR

表1-55 debugging fspf spf命令输出信息描述表

字段

描述

VSAN *vsan-id*, interface *Interface-name*, *operate-type* a route: domain *domain-id.*

改变路由，操作类型取值为：add（添加）、modify（修改）、delete（删除）

VSAN *vsan-id*, failed to notify FSPF route.

通知FSPF路由失败

VSAN *vsan-id*, the hold timer timed out and calculated route.

路由计算间隔定时器超时，计算路由

VSAN *vsan-id*, successfully calculated the route.

成功计算路由

VSAN *vsan-id*, the age of local LSR is MAX_AGE, terminated the route calculation.

本地LSR的age是最大age，结束路由计算

VSAN *vsan-id*, failed to alloc memory, terminated the route calculation.

申请内存失败，停止路由计算

VSAN *vsan-id*, the age of relevant LSR (domain *domain-id*) is MAX_AGE, ignored the Link Descriptor (domain *domain-id)*.

相关LSR的age是最大age，忽略该链路描述符

VSAN *vsan-id*, the relevant LSR (domain *domain-id*) is nonexistent, ignored the Link Descriptor (domain *domain-id*).

相关LSR不存在，忽略该链路描述符

VSAN *vsan-id*, the relevant LSR (domain *domain-id*) has no peer Link Descriptor, ignored the Link Descriptor (domain *domain-id*).

相关LSR不存在对称的链路描述符，忽略该链路描述符

VSAN *vsan-id*, the type of peer Link Descriptor (domain *domain-id*) is invalid, ignored the Link Descriptor (domain *domain-id*).

对称链路描述符的类型不合法，忽略该链路描述符

VSAN *vsan-id*, the interface index of peer Link Descriptor (domain *domain-id*) is invalid, ignored the Link Descriptor (domain *domain-id*).

对称链路描述符的接口索引不合法，忽略该链路描述符

VSAN *vsan-id*, the relevant LSR (domain *domain-id*) has been in the spf-list, ignored the Link Descriptor (domain *domain-id*).

相关LSR存在路由计算列表，忽略该链路描述符

VSAN *vsan-id*, immediately calculated the route because the interval reached the hold-time.

间隔时间达到路由计算间隔，计算路由

VSAN *vsan-id* , successfully created the hold timer.

成功创建路由计算间隔定时器

VSAN *vsan-id*, failed to create the hold timer.

创建路由计算间隔定时器失败

VSAN *vsan-id*, terminated the route calculation because of Graceful Restart.

由于平滑重启，终止路由计算

VSAN *vsan-id*, calculated a fspf route: domain *domain-id*, interface *Interface-name*, cost *number*.

计算FSPF路由

VSAN vsan-id, immediately calculated the route because the interval reached the hold-time.

间隔时间达到路由计算间隔，计算路由

VSAN vsan-id , successfully created the hold timer.

成功创建路由计算间隔定时器

VSAN vsan-id, failed to create the hold timer.

创建路由计算间隔定时器失败

表1-56 debugging fspf timer命令输出信息描述表

字段

描述

VSAN *vsan-id*, interface *Interface-name*, successfully created the retransfer timer.

成功创建重传定时器

VSAN *vsan-id*, interface *Interface-name*, successfully created the hello timer.

成功创建hello定时器

VSAN *vsan-id*, interface *Interface-name*, successfully created the dead timer.

成功创建dead定时器

VSAN *vsan-id*, interface *Interface-name*, successfully created the empty LSU timer.

成功创建LSU定时器

VSAN *vsan-id*, interface *Interface-name*, failed to create the retransfer timer.

创建重传定时器失败

VSAN *vsan-id*, interface *Interface-name*, failed to create the hello timer.

创建hello定时器失败

VSAN *vsan-id*, interface *Interface-name*, failed to create the dead timer.

创建dead定时器失败

VSAN *vsan-id*, interface *Interface-name*, failed to create the empty LSU timer.

创建空LSU定时器失败

VSAN *vsan-id*, interface *Interface-name*, deleted the retransfer timer.

删除重传定时器

VSAN *vsan-id*, interface *Interface-name*, deleted the hello timer.

删除hello定时器

VSAN *vsan-id*, interface *Interface-name*, deleted the dead timer.

删除dead定时器

VSAN *vsan-id*, interface *Interface-name*, deleted the empty LSU timer.

创建空LSU定时器失败

VSAN *vsan-id*, interface *Interface-name*, refreshed the dead timer.

刷新dead定时器

VSAN *vsan-id*, successfully created the age timer.

成功创建age定时器

VSAN *vsan-id*, failed to create the age timer.

创建age定时器失败

VSAN *vsan-id*, deleted the age timer.

删除age定时器

VSAN *vsan-id*, interface *Interface-name*, refreshed the hello timer.

刷新hello定时器

VSAN *vsan-id*, successfully created the restarter timer.

成功创建重启定时器

VSAN *vsan-id*, failed to create the restarter timer.

创建重启定时器失败

VSAN *vsan-id*, the restarter timer timed out.

重启定时器超时

VSAN *vsan-id*, interface *Interface-name*, refreshed the empty LSU timer.

刷新空LSU定时器

VSAN *vsan-id*, deleted the restarter timer.

删除重启定时器

【举例】

\# 打开VSAN 2 内FSPF模块的错误调试信息开关。

\<Sysname\> debugging fspf error vsan 2

\*Nov 28 18:46:34:074 2011 Sysname FSPF/7/ERROR: -MDC=1; VSAN 2, interface Vfc2 failed to process link-up event.

*// 处理链路UP事件失败*

\# 打开VSAN 2 内FSPF模块的事件调试信息开关。

\<Sysname\> debugging fspf event vsan 2

\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/EVENT: -MDC=1; VSAN 2, successfully generated a new LSR.

*// 成功生成一个新LSR*

\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/EVENT: -MDC=1; VSAN 2, successfully installed the LSR and calculated route.

*// 成功安装LSR，并且计算路由*

\# 打开VSAN 2 内FSPF模块的LSR泛洪调试信息开关。

\<Sysname\> debugging fspf flood vsan 2

\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/FLOOD: -MDC=1; VSAN 2, flooded the LSR with domain 1.

*[//*]*泛洪LSR*

\# 打开VSAN 2 内FSPF模块的高可靠性调试信息开关。

\<Sysname\> debugging fspf ha vsan 2

\*Nov 28 18:42:34:629 2011 Sysname FSPF/7/HA: -MDC=1; VSAN 2, interface Fc1/0/1, cleared the flag for Restarter.

*// 清除Restarter标志*

\*Nov 28 18:42:51:486 2011 Sysname FSPF/7/HA: -MDC=1; VSAN 2, interface Fc1/0/1, GR Helper was not enabled, and failed to enter GR Helper role.

*[// GR Helper*]*没有使能，不能进入GR Helper角色*

\# 打开VSAN 2 内FSPF模块的LSR调试信息开关。

\<Sysname\> debugging fspf lsr vsan 2

\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/LSR: -MDC=1; VSAN 2, deleted a LSR from LSDB: Link State Identifier is 1, Number of Links is 1.

*// 从LSDB中删除一条LSR，链路描述符为1，链路个数是1*

\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/LSR: -MDC=1; VSAN 2, added a LSR to LSDB: Link State Identifier is 1, Number of Links is 1.

*// 向LSDB中添加一条LSR，链路描述符为1，链路个数是1*

\# 配置FC1/0/1接口up，打开VSAN 2 内FSPF模块的报文调试信息开关。

\<Sysname\> debugging fspf packet vsan 2

\*Nov 28 18:10:29:453 2011 Sysname FSPF/7/PACKET: -MDC=1; VSAN 2, interface Fc1/0/1, Hello Send: Successfully sent 1-way hello packet.

*// 成功发送1-way hello报文*

\*Nov 28 18:10:51:486 2011 Sysname FSPF/7/PACKET: -MDC=1; VSAN 2, interface Fc1/0/1, Hello Receive: Dead_Interval field of hello packet mismatches the local Dead_Interval,and discarded the packet.

*[// Hello*]*报文的Dead_Interval值不等于本地Dead_Interval值，丢弃报文*

\# 打开VSAN 2 内FSPF模块的路由计算调试信息开关。

\<Sysname\> debugging fspf spf vsan 2

\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/SPF: -MDC=1; VSAN 2, immediately calculated the route because the interval reached the hold-time.

*// 时间间隔到达路由计算间隔值，触发路由计算*

\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/SPF: -MDC=1; VSAN 2, successfully calculated the route.

*// 成功计算路由*

\# 打开VSAN 2 内FSPF模块的定时器调试信息开关。

\<Sysname\> debugging fspf timer vsan 2

\*Nov 28 18:42:51:486 2011 Sysname FSPF/7/TIMER: -MDC=1; VSAN 2, interface Fc1/0/1, deleted the retransfer timer.

*// 删除重传定时器*

\*Nov 28 18:42:51:486 2011 Sysname FSPF/7/TIMER: -MDC=1; VSAN 2, interface Fc1/0/1, refreshed the dead timer.

*// 刷新dead定时器*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging san-aggregation**

------------------------------------------------------------------------

【命令】

**[debugging san-aggregation**[ { **all** \| **error** \| **event** \| **selection** \| **packet** [ **receive** \| **send** ] }  **interface** **san-aggregation** *interface-number* ]]

**[undo debugging san-aggregation**[ { **all** \| **error** \| **event** \| **selection** \| **packet** [ **receive** \| **send** ] }  **interface** **san-aggregation** *interface-number* ]]

【视图】

用户视图

【缺省级别】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[selection**]：表示成员接口选中调试信息开关。

**[packet**]：表示报文调试信息开关。

**[receive**]：表示接收报文调试信息开关。

**[send**]：表示发送报文调试信息开关。

**[interface san-aggregation ***interface*-*number*]：表示指定FC聚合接口的调试信息开关。*interface*-*number*表示FC聚合接口的编号。如果未指定本参数，表示所有FC聚合接口的调试信息开关。

【描述】

**[debugging san-aggregation**]命令用来打开FC聚合组调试信息开关。**undo debugging san-aggregation**命令用来关闭FC聚合组调试信息开关。

缺省情况下，FC聚合组调试信息开关处于关闭状态。

需要注意的是：

·如果未指定**receive**和**send**参数，表示同时指定接收和发送的报文。

·通过**interface**参数打开的指定接口的调试信息开关，只能通过在**undo**命令中指定**interface**参数来关闭。

表1-57 debugging san-aggregation error命令输出信息描述表

字段

描述

PhyIoCtl event *event-id* is unknown.

物理控制事件*event-id*未知

Failed to add interface *fc*-*interface-name* to SAN aggregation group for interface *sagg-interface-name*.

FC接口*fc*-*interface-name*加入FC聚合组*sagg-interface-name*失败

Failed to create SAN aggregation group for interface *sagg-interface-name*.

创建FC聚合组*sagg-interface-name*失败

Failed to deal with interface event for interface *sagg-interface-name*.

FC聚合组*sagg-interface-name*处理接口事件失败

Failed to notify driver to block interface *fc-interface-name* of interface *sagg-interface-name*.

通知驱动阻塞成员接口*fc-interface-name*失败

Failed to notify driver to unblock interface *fc-interface-name* of interface *sagg-interface-name*.

通知驱动解除阻塞成员接口*fc-interface-name*失败

Failed to notify driver to create SAN aggregation group of interface *sagg-interface-name*.

通知驱动创建FC聚合组*sagg-interface-name*失败

Failed to notify driver to change Selected ports for  interface *sagg-interface-name*.

通知驱动FC聚合组*sagg-interface-name*选中端口变化失败

Failed to notify driver to delete SAN aggregation group for  interface *sagg-interface-name*.

通知驱动删除FC聚合组*sagg-interface-name*失败

Failed to notify driver to set local-first load sharing mode.

通知驱动设置本地转发优先模式失败

Notifying driver to set local-first load sharing mode is not supported.

不支持通知驱动设置本地转发优先模式

Failed to notify the physical state of  interface *sagg-interface-name* to become up.

通知FC聚合组*sagg-interface-name*物理UP失败

Failed to notify the physical state of  interface *sagg-interface-name* to become down.

通知FC聚合组*sagg-interface-name*物理DOWN失败

Failed to notify the speed of  interface *sagg-interface-name* to be changed.

通知FC聚合组*sagg-interface-name*速率变化失败

表1-58 debugging san-aggregation event命令输出信息描述表

字段

描述

Received an event for creating SAN aggregation group for  interface *sagg-interface-name*.

收到FC聚合组*sagg-interface-name*创建事件

Received an event for deleting SAN aggregation group for  interface *sagg-interface-name*.

收到FC聚合组*sagg-interface-name*删除事件

Received shutdown notification for interface *sagg-interface-name*.

收到FC聚合组*sagg-interface-name *shutdown通知

Received undo-shutdown notification for interface *sagg-interface-name*.

收到FC聚合组*sagg-interface-name *undo-shutdown通知

Notified interface *fc-interface-name* of interface *sagg-interface-name* to join the SAN aggregation group.

通知FC接口*fc-interface-name*加入FC聚合组*sagg-interface-name*

Notified interface *fc-interface-name* of interface *sagg-interface-name* to leave the SAN aggregation group.

通知成员接口*fc-interface-name*离开FC聚合组

Received a link up event for interface *fc-interface-name* of interface *sagg-interface-name*.

收到FC接口*fc-interface-name*链路UP事件

Received a link down event for interface *fc-interface-name* of interface *sagg-interface-name*.

收到FC接口*fc-interface-name*链路DOWN事件

Received an active event for interface *fc-interface-name* of interface *sagg-interface-name*.

收到FC接口*fc-interface-name*激活事件

Received a deactive event for interface *fc-interface-name* of interface *sagg-interface-name*.

收到FC接口*fc-interface-name*取消激活事件

Received an event for deleting  interface *fc-interface-name* of interface *sagg-interface-name*.

收到FC接口*fc-interface-name*删除事件

The physical state of interface *sagg-interface-name* became up with *fc-mode* mode.

FC聚合组*sagg-interface-name fc-mode*模式物理状态UP

The physical state of interface *sagg-interface-name* became down.

FC聚合组*sagg-interface-name*物理状态DOWN

The speed of interface *sagg-interface-name* changed to *speed-number* Gbps.

FC聚合组*sagg-interface-name*速率变为*speed-number Gbps*

Created a retransmission timer and retransmission began.

创建重传定时器并且开始重传

Deleted the retransmission timer and retransmission finished.

删除重传定时器并且结束重传

Successfully set local-first load sharing mode.

设置本地转发优先模式成功

Interface *fc-interface-name* joined the SAN aggregation group for interface *sagg-interface-name*.

FC接口*fc-interface-name*加入FC聚合组*sagg-interface-number*

Interface *fc-interface-name* leaved the SAN aggregation group for interface *sagg-interface-name*.

成员接口*fc-interface-name*离开FC聚合组*sagg-interface-name*

Successfully notified the physical state of interface sagg-interface-name to become up.

通知FC聚合组*sagg-interface-name*物理UP成功

Successfully notified the physical state of interface *sagg-interface-name* to become down.

通知FC聚合组*sagg-interface-name*物理DOWN成功

Successfully notified the speed of interface *sagg-interface-name* to be changed.

通知FC聚合组*sagg-interface-name*速率变化成功

Successfully notified shutdown event for interface *sagg-interface-name*.

通知FC聚合组*sagg-interface-name* shutdown事件成功

Successfully notified undo-shutdown event for interface *sagg-interface-name*.

通知FC聚合组*sagg-interface-name* undo-shutdown事件成功

Received phyIoCtl event *event-id*.

收到物理控制事件*event-id*

Successfully created the SAN aggregation group for interface *sagg-interface-name*.

创建FC聚合组*sagg-interface-name*成功

Successfully deleted the SAN aggregation group for interface *sagg-interface-name*.

删除FC聚合组*sagg-interface-name*成功

表1-59 debugging san-aggregation selection命令输出信息描述表

字段

描述

Began to determine Selected ports for interface *sagg-interface-name*.

FC聚合组*sagg-interface-name*开始进行成员接口选择

Interface *fc-interface-name* became Selected in interface *sagg-interface-name*.

成员接口*fc-interface-name*变为选中口

Interface *fc-interface-name* became Unselected in interface *sagg-interface-name*.

成员接口*fc-interface-name*变为非选中口

Notified Selected port change for interface *sagg-interface-name*.

FC聚合组*sagg-interface-name*通知选中口变化

Selected ports did not change for interface *sagg-interface-name*.

FC聚合组*sagg-interface-name*选中口没有变化

表1-60 debugging san-aggregation packet命令输出信息描述表

字段

描述

Interface *sagg-interface-name* sent a packet.

FC聚合组*sagg-interface-name*发送报文

Interface *sagg-interface-name* received a packet.

FC聚合组*sagg-interface-name*接收报文

The SAN aggregation group for interface *sagg-interface-name* had no selected member and discarded the packet.

FC聚合组*sagg-interface-name*没有选中口，因此丢弃该报文

Successfully relayed the packet from interface *sagg-interface-name* to the active MPU.

透传报文到主板成功

Failed to relay the packet from interface *sagg-interface-name* to the active MPU.

透传报文到主板失败

Received the packet from interface *sagg-interface-name* on slot *slot-number*.

*[slot-number*]板收到报文

The active MPU successfully received relayed packet from interface *sagg-interface-name*.

主板成功收到透传报文

The active MPU discarded the relayed packet from interface *sagg-interface-name*.

主板丢弃透传报文

【举例】

\# 打开FC聚合组的错误调试信息开关。当FC接口加入FC聚合组失败时会输出下列调试信息。

\<sysname\> debugging san-aggregation error

\*Feb  3 07:38:14:512 2013 Sysname FCAGG/7/ERROR: -MDC=1; Failed to add interface fc1/0/1 to SAN aggregation group for interface SAN-Aggregation1.

*[// FC*]*接口FC1/0/1加入FC聚合组1失败*

\# 打开FC聚合组的事件调试信息开关。当配置FC接口FC1/0/1加入FC聚合组1时会输出下列调试信息。

\<sysname\> debugging san-aggregation event

\*Feb  3 07:44:10:356 2013 Sysname FCAGG/7/EVENT: -MDC=1; Interface fc1/0/1 joined the SAN aggregation group for interface SAN-Aggregation1.

*[// FC*]*接口FC1/0/1加入FC聚合组1*

\# 打开FC聚合组的成员接口选中调试信息开关。当FC聚合组内成员接口链路UP时，会输出下列调试信息。

\<Sysname\> debugging san-aggregation selection

\*Feb  3 07:57:38:487 2013 Sysname FCAGG/7/SELECTION: -MDC=1; Began to determine Selected ports for interface SAN-Aggregation2.

*[// FC*]*聚合组2开始进行成员接口选择*

\# 打开FC聚合组的报文调试信息开关。当FC聚合组2和对端FC聚合组链路协商时，会输出下列调试信息。

\<Sysname\> debugging san-aggregation packet

\*Feb  3 07:57:38:488 2013 Sysname FCAGGK/7/PACKET: -MDC=1; Interface SAN-Aggregation2 sent a packet.

*[// FC*]*聚合组2发送协商报文*

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging vsan**

------------------------------------------------------------------------

【命令】

**[debugging vsan**[ { **all** \| **error** \| **event** }]]

**[undo debugging vsan**[ { **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging vsan**]命令用来打开VSAN调试信息开关。**undo debugging vsan**命令用来关闭VSAN调试信息开关。

缺省情况下，VSAN调试信息开关处于关闭状态。

表1-61 debugging vsan error命令输出信息描述表

字段

描述

Failed to add event *eventtype* notify node of module *module-id*.

为模块*module-id*添加事件*eventtype*通知结点失败

Failed to push *event* event in VSAN *vsan-id*.

推送VSAN *vsan-id*内的*event*事件失败

Failed to notify module *module-id* of *event* event with priority *priority* in VSAN *vsan-id* in user space.

向用户态模块*module-id*通知VSAN *vsan-id*内的优先级为*priority*的事件*event*失败

Failed to notify the driver of the VSAN *vsan-id* creation event, and error code *err-code*.

通知驱动VSAN *vsan-id*创建事件失败，且错误码为*err-code*

Failed to notify the driver of the VSAN *vsan-id* deletion event, and error code *err-code*.

通知驱动VSAN *vsan-id*删除事件失败，且错误码为*err-code*

Failed to receive FC response message from socket *socket-id*.

从socket *socket-id*接收FC响应消息失败

Failed to receive FC request message from socket *socket-id*.

从socket *socket-id*接收FC请求消息失败

Failed to reply to synchronous message.

回应同步消息失败

Failed to synchronize VSAN to IO board.

向IO板同步VSAN配置失败

Failed to synchronize VSAN debug to IO board.

向IO板同步VSAN debug配置失败

Failed to synchronize fabric debug to IO board.

向IO板同步Fabric debug配置失败

Failed to synchronize timer configuration to IO board.

向IO板同步定时器配置失败

Failed to synchronize the VSAN mode to the IO board.

向IO板同步VSAN模式失败

表1-62 debugging vsan event命令输出信息描述表

字段

描述

VSAN *vsan-id* was successfully created

VSAN *vsan-id*被成功创建

VSAN *vsan-id* was successfully deleted

VSAN *vsan-id*被成功删除

Successfully notified the driver of the VSAN *vsan-id* creation event.

通知驱动VSAN *vsan-id*创建事件成功

Notifying the driver of the VSAN creation event was not supported.

不支持通知驱动VSAN *vsan-id*创建事件

Successfully notified the driver of the VSAN *vsan-id* deletion event.

通知驱动VSAN *vsan-id*删除事件成功

Notifying the driver of the VSAN deletion event was not supported.

不支持通知驱动VSAN *vsan-id*删除事件

Notified module *module-id* of *event* event with priority *priority* in VSAN *vsan-id* in user space

向用户态模块*module-id*通知VSAN *vsan-id*内的优先级为*priority*的事件*event*

·0x01：VSAN创建事件

·0x02：VSAN删除事件

·0x04：域ID变化事件

·0x08：fabric name变化事件

Created kernel VSAN data in VSAN *vsan-id*

创建VSAN的内核数据

Destroyed kernel VSAN data in VSAN *vsan-id*

删除VSAN的内核数据

Notified the kernel module *module-id* of the VSAN *vsan-id* event *event*.

向内核模块*module-id*通知VSAN *vsan-id*内的事件*event*.

·0x01：VSAN创建事件

·0x02：VSAN删除事件

·0x04：域ID变化事件

·0x08：fabric name变化事件

Received EPort deletion event.

收到E端口删除事件

Received EPort active event.

收到E端口激活事件

Received EPort deactive event.

收到E端口去激活事件

【举例】

\# 打开VSAN错误调试信息开关。创建VSAN 2失败时会输出下列调试信息。

\<Sysname\> debugging vsan error

\*Jun 23 16:42:36:222 2011 Sysname FCFABRIC/7/ERROR: -MDC=1; Failed to notify module 134348800 of VSAN deletion event with priority 64 in VSAN 2 in user space.

*// 向用户态模块134348800通知VSAN 2内的优先级为64的VSAN删除事件失败*

\# 打开VSAN事件调试信息开关。删除VSAN 2时会输出下列调试信息。

\<Sysname\> debugging vsan event

\*Jun 23 16:42:36:222 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; Notified module 134348800 of VSAN deletion event with priority 64 in VSAN 2 in user space.

*[//*]*向用户态模块134348800通知VSAN 2内的优先级为64的VSAN删除事件*

\*Jun 23 16:42:36:222 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; Successfully notified the driver of the VSAN 2 deletion event.

*// 通知驱动VSAN 2被删除*

\*Jun 23 16:42:36:224 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 2 was successfully deleted.

*[// VSAN 2*]*被成功删除*
