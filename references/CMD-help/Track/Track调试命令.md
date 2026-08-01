<!-- CMD-INDEX
  debugging track                     | 用户视图             | L5
-->

**Track \-- Track调试命令 \-- debugging track**

------------------------------------------------------------------------

【命令】

**[debugging track**]

**[undo debugging track**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging track**]命令用来打开Track的调试信息开关。

**[undo debugging track**]命令用来关闭Track的调试信息开关。

缺省情况下，Track的调试信息开关处于关闭状态。

表1-1 debugging track命令输出信息描述表

字段

描述

The state of track entry *entry-number* changed from *state1* to *state2*.

Track项*entry-number*的状态从*state1*转变为*state2*

状态取值包括：

·NotReady：表示无效值

·Positive：表示状态正常

·Negative：表示状态异常

Notified application process *process-id* in slot *slot-number* that the state of track entry *entry-number* had changed to *state1*.

通知应用进程*process-id*，Track项*entry-number*的状态变为*state1*，进程所在的板的板号为*slot-number*

Track entry *entry-number* registered with the NQA (*owner-tag*) reaction (*item-number*).

Track项*entry-number*向NQA注册联动

Track entry *entry-number* deregistered with the NQA (*owner-tag*) reaction (*item-number*).

Track项*entry-number*取消与NQA的联动注册

Received the notification that the state of NQA (*owner-tag*) reaction (*item-number*) had changed to *state*.

接收到NQA联动项状态转变的通知

Received the notification that the BFD session state had changed to *state*.

BFD info:

Session mode: *session-mode*

Outgoing interface: *interface-name*

VPN instance: *vpn-instance-name*

Remote IP: *remote-ip*

Local IP: *local-ip*

接收到BFD会话状态改变的通知，状态转到*state*

BFD会话信息为：

·会话模式为*session-mode*，取值为echo或control

·出接口名为*interface-name*

·出接口绑定的VPN实例为*vpn-instance-name*，如果出接口没有绑定VPN实例，则打印"-"

·对端IP地址为*remote-ip*

·本地IP地址为*local-ip*

Notified the BFD module to create a BFD session.

BFD info:

Session mode: *session-mode*

Outgoing interface: *interface-name*

VPN instance: *vpn-instance-name*

Remote IP: *remote-ip*

Local IP: *local-ip*

Track模块通知BFD模块创建BFD会话

BFD会话信息为：

·会话模式为*session-mode*，取值为echo或control

·出接口名为*interface-name*

·出接口绑定的VPN实例为*vpn-instance-name*，如果出接口没有绑定VPN实例，则打印"-"

·对端IP地址为*remote-ip*

·本地IP地址为*local-ip*

Notified BFD module to delete a BFD session.

BFD info:

Session mode: *session-mode*

Outgoing interface: *interface-name*

VPN instance: *vpn-instance-name*

Remote IP: *remote-ip*

Local IP: *local-ip*

Track模块通知BFD模块删除BFD会话

BFD会话信息为：

·会话模式为*session-mode*，取值为echo或control

·出接口名为*interface-name*

·出接口绑定的VPN实例为*vpn-instance-name*，如果出接口没有绑定VPN实例，则打印"-"

·对端IP地址为*remote-ip*

·本地IP地址为*local-ip*

Received the notification that application process *process-id* in slot *slot-number* had registered with track entry *entry-number*.

收到应用进程*process-id*向track项*entry-number*注册联动的通知，该进程所在板的板号为slot-number{.TableTextChar}

Received the notification that application process *process-id* in slot *slot-number* had deregistered with track entry *entry-number*.

收到应用进程*process-id*取消与track项*entry-number*注册联动的通知，该进程所在板的板号为*slot-number*{.TableTextChar}

Created delay timer for track entry *entry-number*. Delay time: *time*, State: *state*

为Track项*entry-number*创建延迟定时器，延迟时间为*time*，单位为秒，待通知的状态为*state*

Delay timer for track entry *entry-number* expired.

Track项*entry-number*的延迟定时器超时

Deleted the delay timer for track entry *entry-number*.

删除Track项*entry-number*的延迟定时器

Track *entry-number* registered with the CFD CC (service instance *service-id*, MEP *mep-id*).

Track项entry-number关联到CFD连续性检测功能（服务实例为*service-id*，MEP为*mep-id*）

Track *entry-number* deregistered with the CFD CC (service instance *service-id*, MEP *mep-id*).

Track项entry-number与CFD连续性检测功能（服务实例为*service-id*，MEP为*mep-id*）解除关联

Received the notification that the state of CFD CC (service instance *service-id,* MEP *mep-id*) had changed to *state*.

收到CFD服务实例*service-id*, MEP *mep-id* 的状态变化为*state*

【举例】

\# 打开Track的调试信息开关。配置Track模块监测接口物理状态，并将监测结果通知给VRRP模块。查看此时设备上打印的调试信息。

\<Sysname\> debugging track

\# 创建Track项1，监测接口GigabitEthernet1/0/1的物理状态。

\<Sysname\> system-view

Sysname track 1 interface gigabitethernet 1/0/1

\*May 28 13:19:26:421 2011 Sysname TRACK/7/debug: -MDC=1; The state of track entry 1 changed from NotReady to Positive.

*[// Track*]*项1的状态从NotReady转变为Positive。*

\# 创建VRRP备份组1，并关联Track项1。

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 vrrp vrid 1 priority 110

Sysname-GigabitEthernet1/0/2 vrrp vrid 1 virtual ip 10.1.1.1

Sysname-GigabitEthernet1/0/2 vrrp vrid 1 track 1 reduced 30

\*May 28 13:21:35:376 2011 Sysname TRACK/7/debug: -MDC=1; Received the notification that application process 952 had registered with track entry 1.

*// Track模块接收到VRRP向Track项1注册联动的通知。*

\*May 28 13:21:35:376 2011 Sysname TRACK/7/debug: -MDC=1; Notified application process 952 in slot 1 that the state of track entry 1 had changed to Positive.

*[// Track*]*模块通知VRRP*：*Track项1的状态为Positive。*

\# 改变接口状态。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 shutdown

\*May 28 13:25:24:427 2011 Sysname TRACK/7/debug: -MDC=1; The state of track entry 1 changed from Positive to Negative.

*[// Track*]*项1的状态为从Positive转变为Negative，表示监测的接口物理状态变为down。*

\*May 28 13:25:24:427 2011 Sysname TRACK/7/debug: -MDC=1; Notified application process 952 in slot 1 that the state of track entry 1 had changed to Negative.

*[// Track*]*模块通知VRRP*：*Track项1的状态变为Negative。*
