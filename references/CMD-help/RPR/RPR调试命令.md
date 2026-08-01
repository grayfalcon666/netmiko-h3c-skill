<!-- CMD-INDEX
  debugging rpr error                 | 用户视图             | L9
  debugging rpr event                 | 用户视图             | L107
  debugging rpr fsm                   | 用户视图             | L211
  debugging rpr packet                | 用户视图             | L323
  debugging rpr timer                 | 用户视图             | L419
-->

**RPR \-- RPR调试命令 \-- debugging rpr error**

------------------------------------------------------------------------

【命令】

**[debugging**[ **rpr** **error** [ **interface** { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

**[undo** **debugging** **rpr** **error** [ **interface** [{ **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：指定RPR逻辑接口的接口类型和编号。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【描述】

**[debugging** **rpr** **error**]命令用来打开RPR错误调试信息开关。**undo** **debugging** **rpr** **error**命令用来关闭RPR错误调试信息开关。

缺省情况下，RPR错误调试信息开关处于关闭状态。

表1-1 debugging rpr error命令输出信息描述表

字段

描述

On interface *interface*, at east/west, *string*.

接口*interface*在东向/西向上收到错误报文，错误原因为*string*。*string*包括：

·received a control frame with invalid head content：收到无效帧头的控制帧

·received a TP frame with invalid west protection state and discard it：收到带有无效的西向保护状态的TP帧，将其丢弃

·received a TP frame with invalid east protection state and discard it：收到带有无效的东向保护状态的TP帧，将其丢弃

·received a TP frame with invalid version：收到带有无效版本号的TP帧

·received a TP frame with invalid FCS：收到带有无效帧检查序列的TP帧

·received a TC frame with invalid version：收到带有无效版本号的TC帧

·received a TC frame with invalid FCS：收到带有无效帧检查序列的TC帧

·received an ATD frame with invalid version：收到带有无效版本号的ATD帧

·received an ATD frame with invalid FCS：收到带有无效帧检查序列的ATD帧

·received an ATD frame with invalid Resv Rate property：收到带有无效保留速率值的ATD帧

·received an ATD frame with invalid Manage IP property：收到带有无效IP地址的ATD帧

·received an ATD frame from unknown station：收到来自未知站点的ATD帧

·received a TP frame with invalid length：收到无效长度的TP帧

·received a TC frame with invalid length：收到无效长度的TC帧

·received an echo request with invalid FCS：收到带有无效校验和的Echo请求报文

·received an echo response with invalid FCS：收到带有无效校验和的Echo回应报文

·received an unexpected echo response：没有进行Echo操作却收到了Echo回应报文

·received a control frame with invalid type：收到类型无效的控制帧

On interface *interface*, *string*.

接口*interface*在拓扑计算时发生错误，错误原因为*string*。*string*包括：

·MAC duplicate error: ringlet *ringlet_id* hop *hop_id* duplicate with local station：子环*ringlet_id*第*hop_id*跳的MAC地址与本站点重复

·MAC duplicate error: ringlet *ringlet_id1* hop *hop_id1* duplicate with ringlet *ringlet_id2* hop *hop_id2*：子环*ringlet_id1*第*hop_id1*跳的MAC地址与子环*ringlet_id2*第*hop_id2*跳的MAC地址重复

·IP duplicate error: ringlet *ringlet_id* hop *hop_id* duplicate with local station：子环*ringlet_id*第*hop_id*跳的IP地址与本站点重复

·IP duplicate error: ringlet *ringlet_id1* hop *hop_id1* duplicate with ringlet *ringlet_id2* hop *hop_id2*：子环*ringlet_id1*第*hop_id1*跳的IP地址与子环*ringlet_id2*第*hop_id2*跳的IP地址重复

【举例】

\# 两个站点组成RPR环网，且为闭环。在接口RPR-Router1上打开RPR异常调试信息开关，把两个站点的IP配置相同。

\<Sysname\> debugging rpr error interface rpr-router1

\*Apr  1 09:40:54:540 2014 Sysname RPR/7/ERROR: -MDC=1; On interface RPR-Router1, IP duplicate error: ringlet 1 hop 1 duplicate with local station.

*// 接口RPR-Router1在拓扑计算时发生IP地址重复错误，子环1第一跳的IP地址与本站点重复*

**RPR \-- RPR调试命令 \-- debugging rpr event**

------------------------------------------------------------------------

【命令】

**[debugging**[ **rpr** **event** [ **general** \| **ringlet-selection** ]  **interface** [{ **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

**[undo**[ **debugging** **rpr** **event** [ **general** \| **ringlet-selection** ]  **interface** [{ **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[general**]：表示RPR通用事件调试信息开关，包括保护状态变化、错纤变化、接口up/down等。

**[ringlet-selection**]：表示RPR选环表事件调试信息开关。

**[interface**[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：指定RPR逻辑接口的接口类型和编号。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【描述】

**[debugging** **rpr** **event**]命令用来打开RPR事件调试信息开关。**undo** **debugging** **rpr** **event**命令用来关闭RPR事件调试信息开关。

缺省情况下，RPR事件调试信息开关处于关闭状态。

表1-2 debugging rpr event命令输出信息描述表

字段

描述

On interface *interface*, *string* ringlet selection table was updated.

在接口*interface*上更新*string*选环表结束。*string*包括：

·default：默认选环表

·dynamic：动态选环表

·overall：综合选环表

·MAC-learning：MAC地址学习选环表

On interface *interface*, *string*.

在接口*interface*上发生了*string*事件。*string*包括：

·interface_active：逻辑接口激活

·interface_deactive：逻辑接口去激活

·interface_up：逻辑接口up

·interface_down：逻辑接口down

·notify linkstatus_up：通知接口管理逻辑口链路up

·notify linkstatus_down：通知接口管理逻辑口链路down

On interface *interface*, at east/west span, *string*.

在接口*interface*的东向/西向段上发生了*string*事件。*string*包括：

·mistake cable is occurred：发生错纤

·protection status is changed：保护状态改变

·MATE status is changed：MATE口状态改变

On interface *interface*, at ringlet *ringlet_id*(*port*), *string*.

接口*interface*在环*ringlet_id*（物理接口为*port*）上发生*string*事件。*string*包括：

·interface_active：物理接口激活

·interface_deactive：物理接口去激活

·interface_up：物理接口链路up

·interface_down：物理接口链路down

On interface *interface*,received IPv4/IPv6address change event, IPv4/IPv6 address is *address*.

在接口*interface*上收到IPv4/IPv6地址改变事件，IPv4/IPv6地址变为*address*

【举例】

\# 两个站点组成RPR环网，且为闭环。打开RPR事件开关，配置IP地址。

\<Sysname\> debugging rpr event general

\*Apr  1 09:44:38:177 2014 Sysname RPR/7/EVENT: -MDC=1; On interface RPR-Router1, received IPv4 address change event, IPv4 address is 1.5.3.6.

*[//*]*在接口RPR-Router1上发生IPv4地址改变事件，IPv4地址变为1.5.3.6*

**RPR \-- RPR调试命令 \-- debugging rpr fsm**

------------------------------------------------------------------------

【命令】

**[debugging** **rpr** **fsm** [ **interface** [{ **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

**[undo** **debugging** **rpr** **fsm** [ **interface** [{ **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：指定RPR逻辑接口的接口类型和编号。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【描述】

**[debugging** **rpr** **fsm**]命令用来打开RPR状态机调试信息开关。**undo** **debugging** **rpr** **fsm**命令用来关闭RPR状态机调试信息开关。

缺省情况下，RPR状态机调试信息开关处于关闭状态。

表1-3 debugging rpr fsm命令输出信息描述表

字段

描述

On interface *interface*, at east/west span, *string* protection switch is current.

在接口*interface*的东向/西向段上发生了*string*保护事件。*string*包括：

·TP_RCVD：收到TP帧

·WTR_EXP：WTR定时器溢出

·AUTO_IDLE：链路恢复

·AUTO_SD：信号减弱

·AUTO_SF：信号消失

·ADMIN_IDLE：手动恢复

·ADMIN_MS：手动保护

·ADMIN_FS：强制保护

·MATE_IDLE：MATE口恢复

·MATE_SF：MATE口SF

On interface *interface*, *state* state machine is running.

接口*interface*上正在运行*state*状态机。*state*包括：

·topology validation：TopologyValidation状态机

On interface *interface*, at east/west span, *state* state machine is running.

接口*interface*的东向/西向段上正在运行*state*状态机。*state*包括：

·receive TP：ReceiveTpFrame状态机

·topology control：TopologyControl状态机

·parse TP：ParseTpFrame状态机

·protection update：ProtectionUpdate状态机

·secondary update：SecondaryUpdate状态机

On interface *interface*, *state* state machine: in stage *stage*.

在接口*interface*上，*state*状态机正处于*stage*阶段。*state*包括：

·topology validation：TopologyValidation状态机

*[stage*]包括：START、UNSTABLE、STABLE、VALID和INVALID

On interface *interface*, at east/west span, *state* state machine: in stage *stage*.

在接口*interface*的东向/西向段上，*state*状态机正处于*stage*阶段。*state*包括：

·parse tp：ParseTpFrame状态机

·protection update：ProtectionUpdate状态机

*[stage*]包括：START、ADMIN、MAIN、MARK、IDLE、WTRC、CLEAR、CHECK、FINAL、NEXT、TEST、DIFF、EXEC、CC和NEAR

【举例】

\# 两个站点组成RPR环网，为站点执行绑定操作。

\<Sysname\> debugging rpr fsm

\*Apr  1 09:52:11:783 2014 Sysname RPR/7/FSM: -MDC=1; On interface RPR-Router1, topology control state machine is running.

*[//*]*接口RPR-Router1上正在运行TopologyControl状态机*

\*Apr  1 09:52:11:783 2014 Sysname RPR/7/FSM: -MDC=1; On interface RPR-Router1, protection update state machine is running.

*[//*]*接口RPR-Router1上正在运行ProtectionUpdate状态机*

**RPR \-- RPR调试命令 \-- debugging rpr packet**

------------------------------------------------------------------------

【命令】

**[debugging** **rpr** **packet** [ \**[atd**[ \| **echo-request** \| **echo-response** \| **tc** \| **tp**   **receive** \| **send** ] \| { **tc** \| **tp** } **burst-send**   **interface** { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

**[undo** **debugging** **rpr** **packet** [ \**[atd**[ \| **echo-request** \| **echo-response** \| **tc** \| **tp**   **receive** \| **send** ] \| { **tc** \| **tp** } **burst-send**   **interface** { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[atd**]：表示RPR报文ATD帧调试信息开关。

**[echo-request**]：表示RPR报文Echo请求报文调试信息开关。

**[echo-response**]：表示RPR报文Echo响应报文调试信息开关。

**[tc**]：表示RPR报文TC帧调试信息开关。

**[tp**]：表示RPR报文TP帧调试信息开关。

**[receive**]：表示接收的RPR报文调试信息开关。

**[send**]：表示发送的RPR报文调试信息开关。

**[burst-send**]：表示RPR快发报文调试信息开关。

**[verbose**]：显示RPR报文的详细信息。如果未指定本参数，将显示RPR报文的摘要信息。

**[interface**[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：指定RPR逻辑接口的接口类型和编号。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【描述】

**[debugging** **rpr** **packet**]命令用来打开RPR报文调试信息开关。**undo** **debugging** **rpr** **packet**命令用来关闭RPR报文调试信息开关。

缺省情况下，RPR报文调试信息开关处于关闭状态。

需要注意的是：

·如果未指定任何报文类型，表示所有类型的RPR报文。

·如果未指定**receive**或**send**参数，表示所有快发的、接收的和发送的RPR报文。

表1-4 debugging rpr packet命令输出信息描述表

字段

描述

On interface *interface*, at east/west span, *packet* packet was received/sent/burst-sent. *string*

在接口*interface*的东向/西向段上，*packet*类型的RPR报文被接收/发送/快发，报文内容为*string*。*packet*包括：TP、TC、ATD、ECHO REQUEST和ECHO RESPONSE

【举例】

\# 两个站点组成RPR环网，且为闭环。为站点1配置站点名称。

\<Sysname\>debugging rpr packet atd verbose

\*Apr  1 09:54:59:728 2014 Sysname RPR/7/PKT: -MDC=1; On interface RPR-Router1, at west span, ATD packet was sent.

 ttl:255  ri:0  fe:0  ft:1  sc:3  we:0  parity:0

 DA:ffff-ffff-ffff  SA:00e0-0100-0002

 ttlBase:255  ef:0  fi:0  ps:0  so:0  res:0

 controlType:1  controlVersion:0

 Ringlet0 weight: 1, ringlet1 weight: 1

 Ringlet0 reserveband: 0, ringlet1 reserveband: 0

 Station setting: mulitichoke-user 0;conversative 0;badfcs-user 0

 Station name: test

 Manage address: 1.5.3.6

 Ifindex: 450

 Secondary mac1: 0000-0000-0000 Secondary mac2: 0000-0000-0000

*[//*]*在接口RPR-Router1的西向段上，发送的ATD报文的全部内容*

**RPR \-- RPR调试命令 \-- debugging rpr timer**

------------------------------------------------------------------------

【命令】

**[debugging** **rpr** **timer** [ **interface** [{ **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

**[undo** **debugging** **rpr** **timer** [ **interface** [{ **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：指定RPR逻辑接口的接口类型和编号。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【描述】

**[debugging** **rpr** **timer**]命令用来打开RPR定时器调试信息开关。**undo** **debugging** **rpr** **timer**命令用来关闭RPR定时器调试信息开关。

表1-5 debugging rpr timer命令输出信息描述表

字段

描述

On interface *interface*, *timer* timer *string*.

在接口*interface*上，*timer*定时器发生了*string*动作。

*[timer*]包括：

·Fast TP：TP帧快发定时器

·Slow TP：TP帧慢发定时器

·FastTC：TC帧快发定时器

·Slow TC：TC帧慢发定时器

·ATD：ATD帧发送定时器

·WTR：WTR定时器

·HoldOff：HoldOff定时器

·Stability：稳定定时器

·OAM：站点间连通性检测定时器

·Report Defect：缺陷检测定时器

*[string*]包括：

·starts：启动

·stops：停止

·expires：超时

【举例】

\# 两个站点组成RPR环网，且为闭环。打开RPR定时器调试信息开关。

\<Sysname\> debugging rpr timer

\*May 19 05:53:58:088 2014 Sysname RPR/7/TIMER: -MDC=1; On interface RPR-Router1, Report Defect timer expires.

*// 在接口RPR-Router1上，缺陷检测定时器超时*

