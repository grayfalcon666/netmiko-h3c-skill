
**Event MIB \-- Event MIB调试命令 \-- debugging event-mib**

------------------------------------------------------------------------

【命令】

**[debugging event-mib **[{ **all** \| **error** \| **info** \| **warning** }]]

**[undo**[ **debugging event-mib** { **all** \| **error** \| **info** \| **warning** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示Event MIB模块所有级别调试信息开关。

**[error**]：表示调试信息等级为error的调试信息开关。

**[info**]：表示调试信息等级为info的调试信息开关。

**[warning**]：表示调试信息等级为warning的调试信息开关。

【描述】

**[debugging****event-mib**]命令用来打开Event MIB调试信息开关。

**[undo** **debugging** **event-mib**]命令用来关闭Event MIB调试信息开关。

缺省情况下，Event MIB调试信息开关处于关闭状态。

表1-1 debugging event-mib error命令输出信息描述表

字段

描述

*[Modulename*entry *index*: Insufficient memory.]

由于内存不足，导致内存分配失败

*[modulename*]：模块名，可取trigger、existence、boolean、threshold、event、set、notification

*[index*]：各表项索引

Object entry *index*: Insufficient memory.

Object表由于内存不足，导致内存分配失败

*[index*]：object表项索引

Trigger entry *index*: Failed to create a timer.

Trigger实例创建定时器失败

*[index*]：表项索引

Failed to initialize Event-MIB module.

Event MIB模块初始化失败

Failed to start a timer.

启动定时器失败

Failed to add sample records. Bucket is already full.

当前采样行数已达到系统支持的最大采样行数，新增的Trigger采样会失败

Value syntax of *mteEventSetObject* doesn\'t match the destination object\'s syntax.

事件设置对象*mteEventSetObject*取值与MIB对象SYNTAX定义的类型不匹配

*[mteEventSetObject*]：事件设置对象OID

Set target object failed because the set object is wildcarded but the trigger object is fully specified.

Set表设置对象属性为通配，但Trigger表中*mteTriggerValueID*属性为全匹配，则Set表中指定对象进行set操作会失败

Variable binding failed because the object *index* in the objects table is wildcarded but the trigger object is fully specified.

Object表设置对象属性为通配，但Trigger表中*mteTriggerValueID*属性为全匹配，则Object表中指定变量绑定失败

*[index*]：Object表项索引

Set failed because the set object\'s context name is wildcarded but the trigger context name is fully specified.

Set表设置对象上下文环境属性为通配，但Trigger表中对应监控对象所处上下文环境属性为全匹配，则Set操作失败

Failed to send LIPC message, errorcode = *errorcode*.

发送LIPC消息失败

*[errorcode*]：当前错误码

Failed to initialize timer instances.

初始化定时器实例失败

Failed to subscribe to SNMP port service.

订阅SNMP端口服务失败

Failed to add iFd handler to epoll, iFd = *iFd*.

加入epoll失败

*[iFd*]：加入的句柄

Event-MIB module binary recovery: Failed to get DBM handler.

Event MIB模块二进制恢复获取dbm句柄失败

Event-MIB module binary recovery: Obtained sortlist num = *num*.

Event MIB模块二进制恢复获取的链表数

*[num*]：获取的链表数

Failed to batch-create sortlists, iRet = *iRet*.

批量创建链表失败

*[iRet*]：返回错误码

Invalid OID length.

OID长度不合法

Invalid context name length.

OID上下文环境名长度不合法

Failed to set timer interval = *interval*.

设置全局定时器时间间隔失败

*[interval*]：时间间隔

Failed to create timer FD.

创建全局定时器失败

Failed to recover information about the *Modulename* module from DBM.

从DBM恢复三个主表数据失败

*[modulename*]：模块名，可取trigger、event、object

Failed to initialize timer submodule.

定时器子模块初始化失败

表1-2 debugging event-mib info命令输出信息描述表

字段

描述

Sample value is null.

采样值为空，或者无采样值

Condition to generate the *mteTriggerFired* notification occurred.

Existence表和Boolean表中触发条件满足，发送trap：*mteTriggerFired*

Condition to generate the *mteTriggerRising* notification occurred.

Threshold表中采样值大于上升阈值，触发条件满足，发送Trap：*mteTriggerRising*

Condition to generate the *mteTriggerFalling* notification occurred.

Threshold表中采样值小于下降阈值，触发条件满足，发送Trap：*mteTriggerFalling*

Condition to generate the *mteTriggerFailure* notification occurred.

触发失败，发送Trap：*mteTriggerFailure*

Condition to generate the *mteEventSetFailure* notification occurred.

Set动作失败，发送Trap：*mteEventSetFailure*

TriggerTest: *mteTriggerTest*

满足Trigger触发条件的测试类型

*[mteTriggerTest*]：有existence、boolean和threshold三种测试选择

SampleType: *mteTriggerSampleType*

Trigger实例采样值类型

*[mteTriggerSampleType*]：有absoluteValue和deltaValue两种选择

TriggerOwner: *TriggerOwner*

TriggerName: *TriggerName*

Trigger实例两级索引

*[TriggerOwner*]：Trigger拥有者

*[TriggerName*]：Trigger名

ValueID: *mteHotOID*

系统自动发Trap时的绑定对象

*[mteHotOID*]：对于触发告警时，取值监控对象*mteTriggerValueID*；对于Set动作失败，取值*mteEventSetObject*

Value of mteTriggerValueID: *mteHotValue*

系统自动发Trap时的绑定对象值

*[mteHotValue*]：监控对象的值

ContextName: *mteHotContextName*

对象所处上下文环境名

*[mteHotContextName*]：对于触发告警时是监控对象OID所在的上下文环境名*mteTriggerContextName*；对于Set动作是Set对象所处的上下文环境名*mteEventSetContextName*

Type of boolean comparison: *mteTriggerBooleanComparison*

Boolean参考值比较类型

*[mteTriggerBooleanComparison*]：有unequal、equal、less、lessOrEqual、greater、greaterOrEqual六种选择

Type of existence test: *mteTriggerExistenceTest*

Existence表测试类型

*[mteTriggerExistenceTest*]：有present、absent、changed三种选择

Boolean comparison value: *mteTriggerBoolCompValue*

Boolean表参考值

*[mteTriggerBoolCompValue*]：相应参考值

Rising: *mteTriggerThresholdRising*

Threshold表上升阈值参考值

*[mteTriggerThresholdRising*]：相应参考值

Falling: *mteTriggerThresholdFalling*

Threshold表下降阈值参考值

*[mteTriggerThresholdFalling*]：相应参考值

DeltaRising: *mteTriggerThresholdDeltaRising*

Threshold表差值上升阈值参考值

*[mteTriggerThresholdDeltaRising*]：相应参考值

DeltaFalling: *mteTriggerThresholdDeltaFalling*

Threshold表差值下降阈值参考值

*[mteTriggerThresholdDeltaFalling*]：相应参考值

SetTargetTag: *SetTargetTag*

配置Set对象处于远程或者本地

*[SetTargetTag*]：本项目只支持本地，取值为N/A

TriggerTargetTag: *TriggerTargetTag*

配置监控对象处于远程或者本地

*[TriggerTargetTag*]：本项目只支持本地，取值为N/A

FailedReason: *mteFailedReason*

触发失败的绑定原因

*[mteFailedReason*]：相应失败原因

表1-3 debugging event-mib warning命令输出信息描述表

字段

描述

Objects entry *index*: Nonexistent objects.

指定的绑定变量不存在时或者为空

*[index*]：表项索引

Event entry *index*: Nonexistent event.

执行Test条件满足时，无对应Event（Test表中指定的Event信息在Event表中不存在）

*[index*]：表项索引

Event entry *index*: Event disabled.

Test表中满足触发条件时，Event表中enable节点没有使能

*[index*]：表项索引

Sample value is not numeric.

采样值为非数值类型

Memory threshold was exceeded.

内存使用超过一级门限阈值，触发门限告警事件

Memory usage dropped below the memory threshold.

内存使用低于一级门限阈值，解除门限告警事件

【举例】

\# 在一台使能了SNMP trap发送功能的设备上打开等级为info的调试信息开关。当监控对象OID的值为60时，在命令行依次输入如下命令，则设备发送对应的Trap。

\<Sysname\> debugging event-mib info

\<Sysname\> system-view

Sysname snmp mib event trigger owner owner1 name triggerA

Sysname-trigger-owner1-triggerA oid ifIndex.3

Sysname-trigger-owner1-triggerA sample absolute

Sysname-trigger-owner1-triggerA context contextname1

Sysname-trigger-owner1-triggerA test threshold

Sysname-trigger-owner1-triggerA-threshold startup rising

Sysname-trigger-owner1-triggerA-threshold rising 50

Sysname-trigger-owner1-triggerA-threshold quit-view

Sysname-trigger-owner1-triggerA trigger enable

\*Jun 30 15:53:29:403 2013 Sysname Event-MIB/7/EVENTMIB_INFO:-

MDC=1; Condition to generate the mteTriggerRising notification occurred.

   TriggerOwner: owner1

   TriggerName: triggerA

   SampleType: absolute

   TriggerTest: threshold

   Rising: 50

   ValueID: 1.3.6.1.2.1.2.1.0

   Value of mteTriggerValueID: 60

   ContextName: contextname1

*// 第一次获取到的采样值不小于设置的上限阈值时，满足Threshold的上限阈值触发条件，则发送mteTriggerRising trap。*

【错误提示信息】

\# 进程没有启动的情况下，打开Event MIB的调试开关。

\<Sysname\> debugging event-mib all

Event-MIB is not configured.
