
**NQA \-- NQA调试命令 \-- debugging nqa**

------------------------------------------------------------------------

【命令】

**[debugging nqa**[ { **all** \| **error** \| **event** \| **reaction** }]]

**[undo debugging nqa**[ { **all** \| **error** \| **event** \| **reaction** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示NQA的所有调试信息开关。

**[error**]：表示NQA的错误调试信息开关。

**[event**]：表示NQA的事件调试信息开关。

**[reaction**]：表示NQA的联动项调试信息开关。

【使用指导】

**[debugging nqa**]命令用来打开NQA的调试信息开关。**undo debugging nqa **命令用来关闭NQA的调试信息开关。

缺省情况下，NQA的调试信息开关处于关闭状态。

表1-1 debugging nqa error命令输出信息描述表

字段

描述

Failed to allocate memory for creating NQA entry (*owner*-*tag*).

NQA测试组调度分配内存失败

Failed to allocate memory for creating NQA template *name*.

NQA模板分配内存失败

Failed to allocate memory for creating NQA entry (instance-*xxxxxxxxxxxxxxxx*?).

NQA实例分配内存失败

NQA entry (*owner*-*tag*): Failed to create start-time timer.

创建start-time定时器失败

NQA entry (*owner*-*tag*): Failed to create life-time timer.

创建life-time定时器失败

NQA entry (*owner*-*tag*): Failed to allocate memory for schedule.

创建调度项分配内存失败

NQA entry (*owner*-*tag*): Failed to receive packet (error code: *error-code*).

表项接收报文失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to receive packet (error code: *error-code*)

实例接收报文失败

NQA entry (*owner*-*tag*): Failed to send packet (error code: *error-code*).

表项发送报文失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to send packet (error code: *error-code*).

实例发送报文失败

NQA entry (*owner*-*tag*): Probe timed out.

表项探测超时

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Probe timed out.

实例探测超时

NQA entry (*owner*-*tag*): Failed to create statistics interval timer.

创建统计间隔定时器失败

NQA entry (*owner*-*tag*): Failed to create history keep-time timer.

创建历史老化定时器失败

NQA entry (*owner*-*tag*): Failed to create statistics hold-time timer.

创建统计老化定时器失败

NQA entry (*owner*-*tag*): Failed to create socket (error code: *error-code*).

表项创建socket失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to create socket (error code: *error-code*).

实例创建socket失败

NQA entry (*owner*-*tag*): Failed to set asynchronous socket (error code: *error-code*).

表项设置异步socket失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to set asynchronous socket (error code: *error-code*).

实例设置异步socket失败

NQA entry (*owner*-*tag*): Failed to set TTL option (error code: *error-code*).

表项设置TTL选项失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to set TTL option (error code: *error-code*).

实例设置TTL选项失败

NQA entry (*owner*-*tag*): Failed to set ToS option (error code: *error-code*).

表项设置ToS选项失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to set ToS option (error code: *error-code*).

实例设置ToS选项失败

NQA entry (*owner*-*tag*): Failed to set bypass-route option (error code: *error-code*).

设置路由表旁路选项失败

NQA entry (owner-tag): Failed to set socket sync pcb (error code: error-code).

设置同步pcb选项失败

NQA entry (owner-tag): Failed to set socket out interface (error code: error-code).

设置出接口失败

NQA entry (owner-tag): Failed to set socket send buffer (error code: error-code).

设置报文缓冲区长度失败

NQA entry (*owner*-*tag*): Failed to find FIB entry according to next hop address.

根据下一跳地址查找FIB表项失败

NQA entry (*owner*-*tag*): Failed to set next hop option (error code: *error-code*).

设置下一条选项失败

NQA entry (*owner*-*tag*): Failed to bind socket (error code: *error-code*).

表项socket绑定失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to bind socket (error code: *error-code*).

实例socket绑定失败

NQA entry (*owner*-*tag*): Failed to get interface index.

获取接口索引失败

NQA entry (*owner*-*tag*): Failed to get IP address from the source interface.

无法从源接口获取IP地址

NQA entry (*owner*-*tag*): Failed to get VRF index.

表项获取VRF索引失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to get VRF index.

实例获取VRF索引失败

NQA entry (*owner*-*tag*): Failed to allocate memory for sending packets.

表项为发送报文分配内存失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to allocate memory for sending packets.

实例为发送报文分配内存失败

NQA entry (*owner*-*tag*): Failed to register socket to epoll.

表项注册socket到epoll失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to register socket to epoll.

实例注册socket到epoll失败

NQA entry (*owner*-*tag*): Failed to create probe timeout timer.

表项创建探测定时器失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to create probe timeout timer.

实例创建探测定时器失败

NQA entry (*owner*-*tag*): Failed to create frequency timer.

表项创建frequency定时器失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to create frequency timer

实例创建frequency定时器失败

NQA entry (*owner*-*tag*): Failed to initialize statistics resources.

初始化统计资源失败

NQA entry (*owner*-*tag*): Failed to allocate memory for creating test resources.

创建测试资源失败

NQA entry (*owner*-*tag*): Failed to set socket port reuse option (error code: *error-code*).

设置socket端口重用选项失败

NQA entry (%s-%s): Failed to connect to the server (error code: *error-code*).

表项发起连接失败

NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to connect to the server (error code: *error-code*)

实例发起连接失败

NQA template *name* doesn\'t exist.

模板XXX不存在

Incomplete NQA operation parameters. Can\'t start NQA operation.

必配信息不全，无法启动测试

表1-2 debugging nqa event命令输出信息描述表

字段

描述

NQA entry (*owner*-*tag*): Create start-time timer successfully, interval is *number*s.

创建start-time定时器成功，定时器间隔时间为*number*秒.

NQA entry (*owner*-*tag*): Refresh start-time timer successfully, interval is *number*s.

刷新start-time定时器成功，定时器间隔时间为*number*秒

NQA entry (*owner*-*tag*): Create life-time timer successfully, interval is *number*s.

创建life-time定时器成功，定时器间隔时间为*number*秒

NQA entry (*owner*-*tag*): Refresh start-time timer successfully, interval is *number*s.

刷新life-time定时器成功，定时器间隔时间为*number*秒

NQA entry (*owner*-*tag*) schedule FSM: Create Schedule Event, status is *current-status*.

创建schedule事件，调度状态初始为*current-status*

NQA entry (*owner*-*tag*) schedule FSM: Delete Schedule Event, status is *current-status*.

表项删除schedule事件，当前调度状态为*current-status*

NQA entry (instance-*xxxxxxxxxxxxxxxx*?) schedule FSM: Delete Schedule Event, status is *current-status*.

实例删除schedule事件，当前调度状态为*current-status*

NQA entry (*owner*-*tag*) schedule FSM: *event*, status changed from *previous-status* to *current-status*.

状态机发生*event*事件，调度状态由*previous-status*变为*current-status*

NQA entry (*owner-tag*): Failed to start the NQA operation because the operation configurations are incomplete.

测试组配置参数不完整，无法启动测试。

NQA entry (*owner*-*tag*): Failed to start the UDP traceroute operation because the initial TTL is greater than the TTL.

初始化跳数大于最大跳数，无法启动UDP-tracert测试。

NQA reacts to system time changing.

响应系统时间修改

表1-3 debugging nqa reaction命令输出信息描述表

字段

描述

NQA entry (*owner*-*tag*): Trigger-only reaction (*number*) is created.

测试组（管理员名字为*owner*，操作标签为*tag*）联动项（序号为*number*）创建

NQA entry (*owner*-*tag*): Trigger-only reaction (*number*) is deleted.

测试组（管理员名字为*owner*，操作标签为*tag*）联动项（序号为*number*）删除

NQA entry (*owner*-*tag*) reaction (*number*): Status changed from *previous-status* to *current-status*.

联动项状态发生改变

NQA entry (*owner*-*tag*) reaction (*number*): Trigger notified.

触发联动通知

【举例】

\# 利用NQA进行ICMP-echo测试，打开所有NQA的调试信息开关。

\<Sysname\> terminal monitor

\<Sysname\> debugging nqa all

\# 创建Track项，NQA测试组，并配置测试类型、创建联动项。

\<Sysname\> system-view

Sysname track 1 nqa entry admin test reaction 1.

Sysname nqa entry admin test

Sysname-nqa-admin-test type icmp-echo

Sysname-nqa-admin-test-icmp-echo destination ip 10.2.2.1

Sysname-nqa-admin-test-icmp-echo reaction 1 checked-element probe-fail threshold-type consecutive 3 action-type trigger-only

\*Apr 29 21:47:25:630 2011 Sysname NQA/7/ Reaction: -VD=1; NQA entry (admin-test): Trigger-only reaction (1) is created.

*// 创建联动项。*

\# 删除联动项1。

Sysname-nqa-admin-test-icmp-echo undo reaction 1

Sysname-nqa-admin-test-icmp-echo quit

\*Apr 29 21:47:25:630 2011 Sysname NQA/7/ Reaction: -VD=1; NQA entry (admin-test): Trigger-only reaction (1) is deleted.

*// 联动项被删除。*

\# 调度NQA测试组，测试开始时间为21:48:25，当前系统时间为21:47:25。

Sysname nqa schedule admin test start-time 21:48:25lifetime 180

Sysname quit

\*Apr 29 21:47:25:630 2011 Sysname NQA/7/ Event: -VD=1; NQA entry (admin-test): Create start-time timer successfully, interval is 60s.

\*Apr 29 21:47:25:630 2011 Sysname NQA/7/ Event: -VD=1; NQA entry (admin-test) schedule FSM: Create Schedule Event, status is Waiting.

*// 已成功调度NQA测试组，等待启动测试。*

\# 将当前系统时间修改为21:49:00。

\<Sysname\>clock datetime 21:49:00 2011/04/29

\*Apr 29 21:49:00:206 2011 Sysname NQA/7/ Event: -VD=1; NQA reacts to system time changing.

*[// NQA*]*响应系统时间修改。*

\*Apr 29 21:49:01:206 2011 Sysname NQA/7/ Event: -VD=1; NQA entry (admin-test): Create life-time timer successfully, interval is 76s.

*// 创建life-time定时器。*

\*Apr 29 21:49:02:206 2011 Sysname NQA/7/ Event: -VD=1; NQA entry (admin-test) schedule FSM: System Time Change Event, status changed from Waiting to Running.

*// 启动NQA测试。*

\*Apr 29 21:49:25:630 2011 Sysname NQA/7/ Reaction: -VD=1; NQA entry (admin-test)  reaction (1): Status changed from invalid to over-threshold.

*// 联动项的状态改变，由invalid变为over-threshold。*
