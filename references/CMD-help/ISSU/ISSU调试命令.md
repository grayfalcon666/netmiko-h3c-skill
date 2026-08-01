<!-- CMD-INDEX
  debugging issu-keep-alive all       | 用户视图             | L7
  debugging issu-keep-alive error     | 用户视图             | L31
  debugging issu-keep-alive event     | 用户视图             | L101
-->

**ISSU \-- ISSU调试命令 \-- debugging issu-keep-alive all**

------------------------------------------------------------------------

【命令】

**[debugging issu-keep-alive all**]

**[undo debugging issu-keep-alive all**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging issu-keep-alive all**]命令用来打开ISSU代理发包的所有调试开关。**undo debugging issu-keep-alive all**命令用来关闭ISSU代理发包的所有调试开关。

缺省情况下，代理发包的所有调试开关处于关闭状态。

**ISSU \-- ISSU调试命令 \-- debugging issu-keep-alive error**

------------------------------------------------------------------------

【命令】

**[debugging issu-keep-alive error**]

**[undo debugging issu-keep-alive error**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging issu-keep-alive error**]命令用来打开ISSU代理发包的错误调试开关。**undo debugging issu-keep-alive error**命令用来关闭ISSU代理发包的错误调试开关。

缺省情况下，代理发包的错误调试开关处于关闭状态。

表1-1 debugging issu-keep-alive error命令输出信息描述表

字段

描述

Failed to add some task nodes for protocol *protocol-name* on slot *slot-number*.

为板号*slot-number*上的协议*protocol-name*添加部分代理发包任务节点失败

Failed to delete some task nodes for protocol *protocol-name* on slot *slot-number*.

为板号*slot-number*上的协议*protocol-name*删除部分代理发包任务节点失败

Failed to send response message to client.

主进程向协议进程客户端发送应答消息失败

Failed to add a task node for protocol *protocol-name* on slot *slot-number*. Reason: Failed to create node.

为板号*slot-number*上的协议*protocol-name*添加一个代理发包任务节点失败，因为创建发包任务节点失败

Failed to add a task node for protocol *protocol-name* on slot *slot-number*. Reason: Failed to create timer.

为板号*slot-number*上的协议*protocol-name*添加一个代理发包任务节点失败，因为创建定时器失败

Failed to send the packet. Check the link.

协议代理发包失败，请检查链路

The interval to send packets must be multiple of 100.

发包间隔必须是100ms的整数倍

**

【举例】

\# 在一台进行ISSU软重启升级的设备上开启ISSU-KEEP-ALIVE错误调试开关

\<Sysname\> debugging issu-keep-alive error

\*Dec 6 10:54:12:978 2011 Sysname ISSU-KA/7/Error: Failed to add a task node for protocol LACP on slot 3. Reason: Failed to create timer.

*[//*]*为3号板上的LACP协议添加代理发包任务失败。*

**ISSU \-- ISSU调试命令 \-- debugging issu-keep-alive event**

------------------------------------------------------------------------

【命令】

**[debugging issu-keep-alive event**]

**[undo debugging issu-keep-alive event**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging issu-keep-alive event**]命令用来打开ISSU代理发包的事件调试开关。**undo debugging issu-keep-alive event**命令用来关闭ISSU代理发包的事件调试开关。

缺省情况下，代理发包的事件调试开关处于关闭状态。

表1-2 debugging issu-keep-alive event命令输出信息描述表

字段

描述

Successfully deleted all task nodes for protocol *protocol-name* on slot *slot-number*.

成功为板号*slot-number*上的协议*protocol-name*删除了所有代理发包任务

Successfully added all task nodes for protocol *protocol-name* on slot *slot-number*.

成功为板号*slot-number*上的协议*protocol-name*添加了所有代理发包任务

Successfully added a task node for protocol *protocol-name* on slot *slot-number*.

成功为板号*slot-number*上的协议*protocol-name*添加了一个代理发包任务节点

Successfully sent protocol *protocol-name* packet. Packet length: %d.

发送一个协议*protocol-name*的代理包成功，包的长度是%d

Sending timer already exists.

发包定时器已经存在

【举例】

\# 在一台进行ISSU软重启升级的设备上开启ISSU-KEEP-ALIVE事件调试开关

\<Sysname\> debugging issu-keep-alive event

\*Dec 6 10:54:12:978 2011 Sysname ISSU-KA/7/Event: Successfully added a task node for protocol STP on slot 3.

*[//*]*成功为3号板上的STP协议添加代理发包任务节点。*
