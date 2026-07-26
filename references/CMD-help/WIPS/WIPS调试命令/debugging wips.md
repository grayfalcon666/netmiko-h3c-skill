
**WIPS \-- WIPS调试命令 \-- debugging wips**

------------------------------------------------------------------------

【命令】

**[debugging wips**[ { **all** \| **classification** \| **countermeasure** \| **detect** \| **event** }]]

**[undo debugging wips**[ { **all** \| **classification** \| **countermeasure** \| **detect** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示WIPS所有调试信息开关。

**[classification**]：表示WIPS的分类调试信息开关。

**[countermeasure**]：表示WIPS的反制调试信息开关。

**[detect**]：表示WIPS的检测调试信息开关。

**[event**]：表示WIPS的事件调试信息开关。

【描述】

**[debugging wips**]命令用来打开WIPS调试信息开关。**undo debugging wips**命令用来关闭WIPS调试信息开关。

缺省情况下，WIPS调试信息开关处于关闭状态。

表1-1 debugging wips classification命令输出信息描述表

字段

描述

Classified *device* (MAC: *mac-address*) in VSD *vsd-name.*

在名字为*vsd-name*的VSD内将MAC地址为*mac-address*的device设备进行分类，包括：

·AP：AP设备

·Client：客户端设备

Classified *device* as *type.*

将*device*设备分类成*type*类型

·*device*：设备类型，包括：

¡AP：AP设备

¡Client：客户端设备

·*type*：分类的类型，包括：

¡Auth：认证的AP

¡Mis(C)：错误配置的AP

¡Rogue：非法的AP

¡Ext：外部的AP

¡Ad-hoc：ad-hoc网络的AP

¡Auth(P)：潜在认证的AP

¡Rogue(P)：潜在非法的AP

¡Ext(P)：潜在外部的AP

¡Uncate：未分类的AP

¡Auth：授权的客户端

¡Unauth：未授权的客户端

¡Mis(A)：错误关联的客户端

¡Uncate：未分类的客户端

Failed to classify *device*.

分类*device*设备失败

·*device*为设备类型，包括：

¡AP：AP设备

¡Client：客户端设备

Created reclassify timer.

创建重分类定时器

表1-2 debugging wips countermeasure命令输出信息描述表

字段

描述

Stopped countermeasure timer.

停止反制定时器

Failed to add countermeasure record for sensor *sensor-id* on radio *radio-id.*

当用sensor *sensor-id*的radio *radio-id*反制时添加反制记录失败

·*sensor-id*：sensor的ID

·*radio-id*：radio的ID

Failed to set countermeasure plan for sensor *sensor-id* on radio *radio-id*.

通知sensor *sensor-id*的radio *radio-id*执行反制失败

·*sensor-id*：sensor的ID

·*radio-id*：radio的ID

Countermeasure timer expired.

反制定时器超时

Started countermeasure timer.

启动反制定时器

Failed to start countermeasure timer

启动反制定时器失败

表1-3 debugging wips detect命令输出信息描述表

字段

描述

Received AP *message-type* message from sensor *sensor-id* on radio *radio-id*.

从sensor *sensor-id*的radio *radio-id*收到AP的*message-type*事件

·*sensor-id*：sensor的ID

·*radio-id*：radio的ID

*[message-type*]的类型包括：

·update：AC收到AP更新事件

·delete：AC收到AP删除事件

Received the message for clearing clients associated with AP *mac-address* from sensor *sensor-id* on radio *radio-id*.

从sensor *sensor-id*的radio *radio-id*收到清除MAC地址为*mac-address*的AP设备下关联的client

·*sensor-id*：sensor的ID

·*radio-id*：radio的ID

·*mac-address*：AP设备的MAC地址**

Received AP status change message from sensor *sensor-id* on radio *radio-id*.

从sensor *sensor-id*的radio *radio-id*收到AP状态改变消息

·*sensor-id*：sensor的ID

·*radio-id*：radio的ID

Received AP critical memory gate message from sensor *sensor-id*.

从sensor *sensor-id*收到AP三级内存门限消息

·*sensor-id*：sensor的ID

表1-4 debugging wips event令输出信息描述表

字段

描述

Failed to send IOCTL message to the AP.

给AP发送IOCTL消息失败

Failed to create *timer-type* timer.

创建*timer-type*类型定时器失败，*timer-type*为定时器的类型，包括：

·reclassify：学习到的设备重新分类定时器

·memory threshold recover：内存门限恢复定时器

·scan：扫描列表定时器

·reconnect to APMGR：重连APMGR定时器

Created *timer-type* timer.

创建*timer-type*类型定时器，*timer-type*为定时器的类型，包括：

·reclassify：学习到的设备重新分类定时器

·memory threshold recover：内存门限恢复定时器

·scan：扫描列表定时器

·reconnect to APMGR：重连APMGR定时器

*[Timer-type*] timer expired.

*[Timer-type*]类型定时器超时，*Timer-type*为定时器的类型，包括：

·Reclassify：学习到的设备重新分类定时器

·Memory threshold recover：内存门限恢复定时器

·scan：扫描列表定时器

·Reconnect to APMGR：重连APMGR定时器

Deleted*Timer-type* timer.

删除*Timer-type*类型定时器，*Timer-type*为定时器的类型，包括：

·reclassify：学习到的设备重新分类定时器

·memory threshold recover：内存门限恢复定时器

·scan：扫描列表定时器

·reconnect to APMGR：重连APMGR定时器

Failed to recover configuration of key (Type: *type*).

DBM恢复类型为*type*的key的配置失败

·*type*：DBM存储的key的类型，取值为数值

Received HA *type* event.

收到HA *type*类型事件

·*type*为HA事件类型：

¡upgrade：备进程收到HA模块通知的升级事件

¡stop：主进程收到HA模块通知的停止事件

¡degrade：主进程收到HA模块通知的降级事件

Failed to process HA upgrade event.

处理HA升级事件失败

Failed to recover configuration from DBM.

从DBM中恢复配置失败

Failed to synchronize data from APMGR.

从APMGR模块同步获取数据失败

Processing system memory threshold alert stop event received by WIPS .

处理WIPS模块收到系统内存门限恢复事件

Processing system memory threshold event(Level *level*) received by WIPS.

处理WIPS模块收到系统内存门限事件，级别为*level*

·*level*：内存门限级别

Finished async get data from APMGR.

完成从APMGR异步获取数据

Processing AP *event-ype* event from APMGR.

处理来自APMGR模块AP的*event-type*事件

·*event-type*：APMGR上报AP的事件类型，包括：

¡down：AC收到AP的下线事件

¡up：AC收到AP的上线事件

¡delete：AC收到AP的删除事件

¡create：AC收到AP的创建事件

Processing radio *event-type* event for radio *radio-id* on AP *ap-id* from APMGR.

处理来自APMGR的AP *ap-id*上radio *radio-id*的*event-type*事件

·*event-type*：APMGR上报radio的事件类型，包括：

¡down：AC收到radio的下线事件

¡up：AC收到radio的上线事件

¡delete：AC收到radio的删除事件

¡create：AC收到radio的创建事件

·*ap-id*：AP的ID

·*radio-id*：radio的ID

Failed to async get data from APMGR: error code = *error-code*.

从APMGR异步获取数据失败，错误码为*error-code*

·*error-code*：失败的错误码

Failed to process APMGR message: error code = *error-code*.

处理APMGR的消息失败，错误码为*error-code*

·*error-code*：失败的错误码

Failed to *event-type* AP event: error code = *error-code*.

处理AP的*event-type*事件失败，错误码为*error-code*

·*event-type*：事件类型，包括：

¡register：AC上用户态模块注册接收AP事件

¡unregister：AC上用户态模块去注册接收AP事件

·*error-code*：失败的错误码

Failed to process *event-type* radio event: error code = *error-code*.

处理radio的*event-type*事件失败，错误码为*error-code*

·*event-type*：事件类型，包括：

¡register：AC上用户态模块注册接收APMGR事件

¡unregister：AC上用户态模块去注册接收APMGR事件

·*error-code*：失败的错误码

Failed to set scan *type* for AP *ap-id* on radio *radio-id*: error code = *error-code*.

在AP *ap-id*的radio *radio-id*上设置扫描*type*类型失败，错误码为*error-code*

·*type*：设置的类型，包括：

¡filter：过滤

¡plan：列表

·*ap-id*：AP的ID

·*radio-id*：radio的ID

·*error-code*：失败的错误码

Set scan *type* for AP *ap-id* on radio *radio-id* successfully.

在AP *ap-id*的radio *radio-id*上设置扫描*type*类型成功

·*type*：设置的类型，包括：

¡filter：过滤

¡plan：列表

·*ap-id*：AP的ID

·*radio-id*：radio的ID

Failed to clear scan filter for AP *ap-id* on radio *radio-id*: error code = *error-code*.

在AP *ap-id*的radio *radio-id*上清除射频的过滤类型失败，错误码为*error-code*

·*ap-id*：AP的ID

·*radio-id*：radio的ID

·*error-code*：失败的错误码

Failed to stop scan plan for AP *ap-id* on radio *radio-id*: error code = *error-code*.

在AP *ap-id*的radio *radio-id*上停止扫描列表失败，错误码为*error-code*

·*ap-id*：AP的ID

·*radio-id*：radio的ID

·*error-code*：失败的错误码

【举例】

\# 配置WIPS，并打开WIPS分类调试信息开关。

\<Sysname\> debugging wips classification

\*Apr  4 15:49:28:081 2014 Sysname WIPS/7/CLASS: -MDC=1; Classify AP as Rogue

*// 将AP分类为Rouge AP*

\# 配置WIPS，并打开WIPS反制调试信息开关。

\<Sysname\> debugging wips countermeasure

\*Apr  4 15:53:28:081 2014 Sysname WIPS/7/COUNTERMEASURE: -MDC=1; Failed to add countermeasure record for sensor 100 on radio 1

*// 使用sensor 100的radio 1对非法设备进行反制时，添加反制记录失败*

\# 配置WIPS，并打开WIPS检测调试信息开关。

\<Sysname\> debugging wips detect

\*Apr  4 15:55:28:081 2014 Sysname WIPS/7/DETECT: -MDC=1; Received AP status change message from sensor 100 on radio 1.

*// 从sensor 100的radio 1收到AP状态改变消息*

\# 配置WIPS，并打开WIPS事件调试信息开关。

\<Sysname\> debugging wips event

\*Apr  4 15:59:28:081 2014 Sysname WIPS/7/EVENT: -MDC=1; Process AP down event from APMGR

*// 处理来自APMGR模块的AP下线的事件*

