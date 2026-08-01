<!-- CMD-INDEX
  debugging port-security             | 用户视图             | L5
-->

**端口安全 \-- 端口安全调试命令 \-- debugging port-security**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging port-security**[ { **all** \| **error** \| **event** }]]

**[undo debugging port-security**[ { **all** \| **error** \| **event** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging port-security**[ { **all** \| **error** \| **event** } [ **slot** *slot-number* ]]]

**[undo debugging port-security**[ { **all** \| **error** \| **event** } [ **slot** *slot-number* ]]]

分布式设备－IRF模式：

**[debugging port-security**[ { **all** \| **error** \| **event** } ]] **chassis** *chassis-number* **slot** *slot-number*

**[undo debugging port-security**[ { **all** \| **error** \| **event** } ]] **chassis** *chassis-number* **slot** *slot-number*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示端口安全的所有调试信息开关。

**[error**]：表示端口安全的错误调试信息开关。

**[event**]：表示端口安全的事件调试信息开关。

**[slot** *slot-number*]：表示指定单板的调试信息开关，*slot-number*表示单板所在槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示指定成员设备的调试信息开关，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示指定成员设备/PEX的调试信息开关，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：表示成员设备上指定单板的调试信息开关，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：表示指定单板的调试信息开关，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【描述】

**[debugging port-security**]命令用来打开端口安全调试信息开关。**undo debugging port-security**命令用来关闭端口安全调试信息开关。

缺省情况下，端口安全调试信息开关处于关闭状态。

表1-1 debug port-security error命令输出信息描述表

字段

描述

Failed to initialize the socket.

初始化socket失败

Failed to get socketFd by slot: *slot.*

通过板号获取socketFd失败

Failed to sync information.

同步信息失败

Failed to recover authentication session

恢复认证会话失败

User authorization failed

用户认证失败

表1-2 debug port-security event命令输出信息描述表

字段

描述

*[app* is being started.]

端口安全启动app模块

Notify *app* of portsec_enable event.

端口安全向app模块/线程通知端口安全使能事件

Notify *app* of portsec_portmode event*.

端口安全向app模块/线程通知端口模式设置事件

Notify *app* of authorization_info_deleted event.

端口安全向app模块/线程通知授权信息删除事件

Notify *app* of auth_fail_policy_proc event.

端口安全向app模块/线程通知认证失败处理事件

Notify *app* of if_vlan event*.

端口安全向app模块/线程通知接口VLAN事件

Notify *app* of HA event*.

端口安全向app模块/线程通知HA事件

Notify *app* of if_event*.

端口安全向app模块/线程通知接口事件

Notify *app* of authorization_success event.

端口安全向app模块/线程通知授权成功事件

Notify *app* of vctrl_success_rsp event.

端口安全向app模块/线程通知vctrl设置成功回应事件

Notify *app* of vctrl_fail_rsp event.

端口安全向app模块/线程通知vctrl设置失败回应事件

Notify *app* of vctrl_del_notify event.

端口安全向app模块/线程通知vctrl删除事件

Notify *app* of mac_vlan event.

端口安全向app模块/线程通知mac-vlan事件

Creating block-mac-aging timer, period is 3 minutes.

创建阻塞mac老化定时器，老化时间是3分钟

All authentication sessions on interface *interface-name* have been deleted.

接口上所有认证会话已经被删除

After the node is removed from the hash table, delete the corresponding timer.

节点从hash表中删除后，删除与其相关的定时器

Dealing with cfg queue message recevied from other threads.

端口安全主进程开始处理从其它线程接收的配置队列消息

IO board received and processed the message.

IO板接收和处理主控板发来的消息

Creating a timer which period is 1 second.

创建一个周期为1秒的定时器

Reconnection from IO board to master timed out.

IO板重连接主控板超时

IO board connected to master successfully. Close reconnection timer.

IO板连接主控板成功，关闭重连接定时器

IO board failed to connect to master.

IO板连接主控板失败

A MAC *mac-add* triggered intrusion protection.

一个源地址为*mac-add*的数据帧触发了入侵保护

Session created

创建会话

Session deleted

删除会话

Processing session-end msg, and attempt to free the session

处理会话结束信息并试图释放会话

Processing session-end msg, trigger intruction and free the session

处理会话结束信息，触发入侵检测并释放会话

New_mac processing finished

New-mac处理结束

Received new_mac notification result is *result*, flag is *flag*

收到new-mac处理的通知结果是*result*，标志是*flag*。其中，*result*的取值包括：

·PORTSEC_MAC_PROCESSING（正在处理）

·PORTSEC_MAC_HANDLED（已经处理）

·PORTSEC_MAC_NOTCONCERN（不关心）

·PORTSEC_MAC_DROP（丢弃）

Successfully recovered authentication session

成功恢复认证会话

New_mac finished, try auth-fail processing

New-mac处理结束，尝试认证失败处理

Received *msg* msg from user

收到用户消息*msg*

Notify new_mac event when user passed MAC authenticaiton

当用户通过MAC地址认证时，通知new-mac事件

【举例】

\# 在一台未启动端口安全功能的设备上，打开端口安全所有调试功能，输出以下调试信息。

\<Sysname\>debugging port-security all

\# 使能端口安全。

\<Sysname\> port-security enable

\*Jan  1 00:03:32:450 2011 Sysname PORTSEC/7/EVENT:

Notify 802.1X of portsec_enable event.

*// 端口安全向802.1X模块通知端口安全使能事件*

\*Jan  1 00:03:32:452 2011 Sysname PORTSEC/7/EVENT:

Notify 802.1X of portsec_enable event.

*// 端口安全向MAC地址认证模块通知端口安全使能事件*

\*Jan  1 00:03:32:456 2011 Sysname PORTSEC/7/EVENT:

Notify AutoLearn of portsec_enable event.

*// 端口安全向autolearn线程通知端口安全使能事件*

\# 配置端口安全模式为mac-else-userlogin-secure-ext。

Sysname-GigabitEthernet1/0 port-security port-mode mac-else-userlogin-secure-ext

\*Jan  1 01:33:45:369 2011 Sysname PORTSEC/7/EVENT:

Notify 802.1X of portsec_portmode event.

*// 端口安全向802.1X线程通知端口模式配置事件*

\*Jan  1 01:33:45:371 2011 Sysname PORTSEC/7/EVENT:

Notify MAC-Auth of portsec_portmode event.

*// 端口安全向MAC地址认证模块通知端口模式配置事件*

\# 当有802.1X用户上线时，输出以下调试信息。

\*Jan  1 02:30:05:947 2011 Sysname PORTSEC/7/EVENT:

MAC-Auth 1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Received new_mac notification result is PORTSEC_MAC_PROCESSING, flag is 0x80000000.

*[//*]*端口安全收到MAC地址认证模块对用户1cbd-b9e3-b0ed的new_mac事件处理结果为PORTSEC_MAC_PROCESSING*

\*Jan  1 02:30:05:948 2011 Sysname PORTSEC/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Session created.

*// 端口安全创建了用户1cbd-b9e3-b0ed的认证会话*

\*Jan  1 02:30:05:955 2011 Sysname PORTSEC/7/EVENT:

MAC-Auth 1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Received PS_QUEMSG_SESS_MSG_FAIL msg from user.

*[//*]*端口安全接收到MAC地址认证线程发出的对用户1cbd-b9e3-b0ed认证失败的队列消息*

\*Jan  1 02:30:05:956 2011 Sysname PORTSEC/7/EVENT:

MAC-Auth 1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Received PS_QUEMSG_SESS_MSG_END msg from user.

*// 端口安全接收到MAC地址认证线程发出的对用户1cbd-b9e3-b0ed结束认证的队列消息*

\*Jan  1 02:30:05:958 2011 Sysname PORTSEC/7/EVENT:

802.1X 1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Received new_mac notification result is PORTSEC_MAC_PROCESSING, flag is 0x80000000.

*[//*]*端口安全收到802.1X模块对用户1cbd-b9e3-b0ed的new_mac事件处理结果为PORTSEC_MAC_PROCESSING*

\*Jan  1 02:30:05:987 2011 Sysname PORTSEC/7/EVENT:

802.1X 1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Received PS_QUEMSG_SESS_MSG_SUCC msg from user.

*// 端口安全收到802.1X模块发出的对1cbd-b9e3-b0ed认证成功的队列消息*

\*Jan  1 02:30:05:997 2011 Sysname PORTSEC/7/EVENT:

802.1X 1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Received PS_QUEMSG_SESS_MSG_AUTZ msg from user.

*// 端口安全收到802.1X模块发出的对1cbd-b9e3-b0ed授权成功的队列消息*

\# 该802.1X用户下线时，输出以下调试信息。

\*Jan  1 02:30:14:658 2011 Sysname PORTSEC/7/EVENT:

802.1X 1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Received PS_QUEMSG_SESS_MSG_END msg from user.

*// 端口安全接收到802.1X模块发出的对用户1cbd-b9e3-b0ed结束认证的队列消息*

\*Jan  1 02:30:14:659 2011 Sysname PORTSEC/7/EVENT:

802.1X 1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Processing session-end msg, and attempt to free the session.

*// 端口安全处理认证结束消息，尝试释放认证会话*

\*Jan  1 02:30:14:663 2011 Sysname PORTSEC/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Session deleted.

*// 端口安全删除了认证会话*

