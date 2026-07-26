
**Monitor Link \-- Monitor Link调试命令 \-- debugging monitor-link**

------------------------------------------------------------------------

【命令】

**[debugging monitor-link** [ **group** *group-id*  { **all** \| **error** \| **event** }]]

**[undo debugging monitor-link** [ **group** *group-id*  { **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group*** group-id*]：表示指定Monitor Link组的调试信息开关。如果未指定本参数，则表示所有Monitor Link组的调试信息开关。

**[all**]：表示Monitor Link组的所有调试信息开关。

**[error**]：表示Monitor Link组错误调试信息开关。

**[event**]：表示Monitor Link组事件调试信息开关。

【描述】

**[debugging monitor-link**]命令用来打开Monitor Link组调试信息开关。**undo debugging monitor-link**命令用来关闭Monitor Link组调试信息开关。

缺省情况下，Monitor Link组调试信息开关处于关闭状态。

表1-1 debugging monitor-link error命令输出信息描述表

字段

描述

Failed to allocate memory for batch backup

为批量备份分配内存失败

Failed to allocate memory for realtime backup

为实时备份分配内存失败

Failed to send batch backup message

发送批量备份消息失败

Failed to send realtime backup message

发送实时备份消息失败

Failed to allocate memory for the monitor link group

为Monitor Link组分配内存失败

Failed to allocate memory for the monitor link port

为Monitor Link组的成员端口分配内存失败

表1-2 debugging monitor-link event命令输出信息描述表

字段

描述

Monitor link group *group-id* is up

Monitor Link组*group-id*处于up状态

Monitor link group *group-id* is down

Monitor Link组*group-id*处于down状态

【举例】

\# 打开Monitor Link组1的事件调试信息开关。

\<Sysname\> debugging monitor-link group 1 event

\*Dec 28 19:37:47:543 2011 SysnameMTLK/7/Event:

 Monitor link group 1 is down

*[// Monitor Link*]*组1处于down状态*
