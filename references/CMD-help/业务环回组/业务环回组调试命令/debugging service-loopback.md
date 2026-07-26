
**业务环回组 \-- 业务环回组调试命令 \-- debugging service-loopback**

------------------------------------------------------------------------

【命令】

**[debugging service-loopback**[ { **all** \| **error** \| **event** }]]

**[undo debugging service-loopback**[ { **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示业务环回组的所有调试信息开关。

**[error**]：表示业务环回组错误调试信息开关。

**[event**]：表示业务环回组事件调试信息开关。

【描述】

**[debugging service-loopback**]命令用来打开业务环回组调试信息开关。**undo debugging service-loopback**命令用来关闭业务环回组调试信息开关。

缺省情况下，业务环回组调试信息开关处于关闭状态。

表1-1 debugging service-loopback error命令输出信息描述表

字段

描述

Failed to get group information when processing update-group message.

非主用主控板处理主用主控板发来的组数据时读取组信息失败

Failed to send the information of group *GroupID*.

发送组*GroupID*的信息失败

Failed to send the information of the debug switch status.

发送调试开关信息失败

Failed to set driver.

设置内核驱动失败

Failed to switch over member port type.

业务环回组切换成员端口类型失败

Failed to send sync group data.

发送同步组数据失败

Failed to create group *GroupID*, which arealdy exists.

创建业务环回组*GroupID*失败，因为该组已存在

Failed to mofidy group *GroupID*, which does not exist.

修改业务环回组*GroupID*失败，因为该组不存在

Failed to mofidy group *GroupID*, the type of which is invalid.

修改业务环回组*GroupID*失败，因为组类型非法

Failed to delete group *GroupID*, which does not exist.

删除业务环回组*GroupID*失败，因为该组已不存在

No group can process set-intftype result.

没有任何组能够处理切换接口类型结果

Failed to switch over interface type when deleting the group.

删除业务环回组时切换接口类型失败

No group can process set-loopback result.

没有任何组能处理设置接口自环结果

Can't process set-loopback result because of invliad interface indexes.

由于接口索引非法而不能处理设置接口自环结果

No group can process interface-up

没有任何组能够处理接口up事件

Can't process interface-up because of invalid group operation flag.

由于无效组操作标记而不能处理接口up事件

Can't process interface-up for non-operation members.

不能处理非操作成员的接口up事件

No group can process expiration of wait-up timer.

没有组能处理等待接口up事件定时器超时

Can't process expiration of wait-up timer because of invalid group operation flag.

由于无效组操作标记而不能处理等待接口up事件定时器超时

Can't process the response message from the slot because the group does not exsit.

由于环回组不存在而不能处理接口板回应消息

表1-2 debugging service-loopback event命令输出信息描述表

字段

描述

Processing *usMsgType* message succeeded.

处理*usMsgType*消息成功

Setting driver succeeded.

设置内核驱动成功

Synchronized group *GroupID* to other slots.

同步业务环回组*GroupID*的数据到其它接口板

Processed group *GroupID* set-intftype result.

处理业务环回组*GroupID*切换接口类型结果

Processed port *IFIndex* set-loopback result.

处理接口*IFIndex*的自环结果

Processed port *IFIndex* up.

处理接口*IFIndex*的up事件

Processed the wait-up timer expiration of group *GroupID*.

处理业务环回组*GroupID*等待接口up事件定时器超时

Received a response from slot *SlotID*.

收到接口板*SlotID*的回应

Received responses from all slots.

收到所有接口板回应

Processed group *GroupID* sync data.

处理业务环回组*GroupID*同步数据

Completed upgrading backup daemon.

备用守护进程升级完成

Received a change type result *ResultType.*

接收切换接口类型结果

Received *EventType* interface-event of port *IFIndex*.

接收到接口*IFIndex*的接口事件*EventType*

Adding interface *IFIndex* node to the setLB list succeeded.

成功添加接口*IFIndex*节点到设置自环状态并设置自环链表

Processing interface *IFIndex* in setLB list succeeded.

从设置接口自环链表中成功处理接口*IFIndex*

Adding interface *IFIndex* node to pending list succeeded.

成功添加接口*IFIndex*节点到待处理接口事件链表

Processing interface *IFIndex* in pending list succeeded.

从待处理接口事件链表中成功处理接口*IFIndex*

Completed processing pending list interface node *IFIndex.*

完成处理待处理接口链表的节点接口*IFIndex*

Creating thread succeeded.

创建线程成功

Switch over a dissociating loopback interface *IFIndex*.

切换游离口*IFIndex*的接口类型成功

【举例】

\# 打开业务环回组错误调试信息开关。

\<Sysname\> debugging service-loopback error

\*Nov  3 19:29:12:860 2010 Sysname SLBG/7/Error:

Failed to create wait response timer.

*// 创建等待回应定时器失败*

\# 打开业务环回组事件调试信息开关。

\<Sysname\> debugging service-loopback event

\*Nov  3 19:29:12:860 2010 Sysname SLBG/7/Event:

Received responses from all slots.

*// 主控板收到其它所有板的回应消息*
