
**接口备份 \-- 接口备份调试命令 \-- debugging interface-backup**

------------------------------------------------------------------------

【命令】

**[debugging interface-backup**[ { **event** \| **track** }]]

**[undo debugging interface-backup**[ { **event** \| **track** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

vd-admin

【参数】

**[event**]：表示接口备份事件调试信息开关。

**[track**]：表示接口备份Track项调试信息开关。

【描述】

**[debugging interface-backup**]命令用来打开接口备份调试信息开关。

**[undo debugging interface-backup**]命令用来关闭接口备份调试信息开关。

缺省情况下，接口备份调试信息开关处于关闭状态。

表1-1 debugging interface-backup event命令输出信息描述表

字段

描述

Deactivated the primary interface *interface-name.*

去激活主接口

Deleted the primary interface *interface-name.*

删除主接口

Deactivated the backup interface *interface-name*.

去激活备份接口

Deleted the backup interface *interface-name*.

删除备份接口

Activated the backup interface *interface-name*.

激活备份接口

Activated the primary interface *interface-name*.

激活主接口

Primary interface *interface-name* came up.

主接口链路up

Backup interface *interface-name* came up.

备份接口链路up

Primary interface *interface-name* went down.

主接口链路down

Backup interface *interface-name* went down.

备份接口链路down

Bandwidth of primary interface *interface-name* changed.

主接口带宽发生变化

Added a backup interface for primary interface *interface-name.*

在主接口上添加一个备份接口

Deleted a backup interface from primary interface *interface-name.*

在主接口上删除一个备份接口

Enabled load balancing of primary interface *interface-name*.

启动主接口的负载分担模式

Disabled load balancing of primary interface *interface-name*.

停止主接口的负载分担模式

Changed the priority of backup interface *interface-name*.

修改备份接口的优先级

Changed the UP_DELAY timer interval of interface *Interface-name*.

修改接口的UP_DELAY定时器参数

Changed the DOWN_DELAY timer interval of interface *Interface-name*.

修改接口的DOWN_DELAY定时器参数

Changed the flow check interval of primary interface *interface-name*.

修改主接口的流量检测间隔

DOWN_DELAY timer on primary interface *interface-name* expired.

主接口DOWN_DELAY定时器超时

DOWN_DELAY timer on backup interface *interface-name* expired.

备份接口DOWN_DELAY定时器超时

UP_DELAY timer on backup interface *interface-name* expired.

备份接口UP_DELAY定时器超时

UP_DELAY timer on primary interface *interface-name* expired.

主接口UP_DELAY定时器超时

Load balancing timer on primary interface *interface-name* expired.

主接口上的负载分担定时器超时

Traffic amount reached the upper limit of primary interface *interface-name*, and it is required to activate a backup interface.

主接口的流量达到了主接口下配置的阈值上限，需要启用一个备份接口

Total traffic amount reached the lower limit of primary interface *interface-name*, and it is required to deactivate a backup interface.

主接口和备份接口的流量总和小于主接口下配置的阈值下限，需要关闭一个备份接口

Interface *interface-name* transitioned from *state1* to *state2.*

接口状态由*state1*迁移到*state2*，可能的状态如下：

·INVALID：初始无效状态

·STANDBY：备用状态

·UP：UP状态

·DOWN：DOWN状态

·UP_DELAY：延时UP状态

·DOWN_DELAY：延时DOWN状态

表1-2 debugging interface-backup track命令输出信息描述表

字段

描述

Track add: Interface *interface-name* was associated with track entry *number*.

配置了一个关联track项的备份接口

Track modify: Track entry *number* associated with interface *interface-name* transitioned to *state*.

Track项*number*的状态变为*state*，可能的状态如下：

·Positive：Track项跟踪的主链路正常

·Negative：Track项跟踪的主链路故障

·Not ready：Track项未生效

Track delete: Association between interface *interface-name* and track entry *number* was removed.

删除接口与track项的关联

【举例】

\# 打开接口备份的事件调试信息开关，当在主接口GigabitEthernet1/0/2下添加一个备份接口GigabitEthernet1/0/4时，将输出如下调试信息。

\<Sysname\> debugging interface-backup event

\<Sysname\> terminal monitor

\<Sysname\> terminal  debugging

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 backup interface gigabitethernet 1/0/4

\*Feb 27 21:12:49:639 2013 Sysname IB/7/EVENT: -MDC=1; Added a backup interface for primary interface GigabitEthernet1/0/2.

\*Feb 27 21:12:49:640 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/2 transitioned from INVALID to UP.

\*Feb 27 21:12:49:640 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/4 transitioned from INVALID to UP.

\*Feb 27 21:12:49:650 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/4 transitioned from UP to STANDBY.

\*Feb 27 21:12:49:650 2013 Sysname IB/7/EVENT: -MDC=1; Backup interface GigabitEthernet1/0/4 went down.

*// 主接口GigabitEthernet1/0/2下添加了一个备份接口，由于主接口当前处于UP状态，备份接口GigabitEthernet1/0/4直接被shutdown，当前备份接口处于STANDBY状态*

\# 配置主备接口的切换延时为10秒，当将主接口shutdown时，将输出如下调试信息。

Sysname-GigabitEthernet1/0/2 backup timer delay 10 10

Sysname-GigabitEthernet1/0/2 shutdown

\*Feb 27 21:15:42:912 2013 Sysname IB/7/EVENT: -MDC=1; Primary interface GigabitEthernet1/0/2 went down.

\*Feb 27 21:15:42:913 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/2 transitioned from UP to DOWN_DELAY.

%Feb 27 21:15:42:914 2013 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; GigabitEthernet1/0/2 link status is down.

%Feb 27 21:15:42:915 2013 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface GigabitEthernet1/0/2 is down.

\*Feb 27 21:15:53:914 2013 Sysname IB/7/EVENT: -MDC=1; DOWN_DELAY timer on primary interface GigabitEthernet1/0/2 expired.

\*Feb 27 21:15:53:914 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/2 transitioned from DOWN_DELAY to DOWN.

\*Feb 27 21:15:54:136 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/4 transitioned from STANDBY to UP_DELAY.

\*Feb 27 21:15:55:474 2013 Sysname IB/7/EVENT: -MDC=1; Backup interface GigabitEthernet1/0/4 came up.

%Feb 27 21:15:55:475 2013 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; GigabitEthernet1/0/4 link status is up.

%Feb 27 21:15:55:475 2013 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface GigabitEthernet1/0/4 is up.

\*Feb 27 21:16:03:914 2013 Sysname IB/7/EVENT: -MDC=1; UP_DELAY timer on backup interface GigabitEthernet1/0/4 expired.

\*Feb 27 21:16:03:914 2013 Sysname IB/7/EVENT: -MDC=1; Interface GigabitEthernet1/0/4 transitioned from UP_DELAY to UP.

*// 主接口报链路down事件，主接口的状态由UP切换到DOWN_DELAY，待主接口的DOWN_DELAY定时器超时后，主接口的状态由DOWN_DELAY切换到DOWN，备份接口由STANDBY切换到UP_DELAY，待备份接口上的UPDELAY定时器超时后，备份接口状态由UP_DELAY切换到UP*

\# 打开接口备份的Track项调试信息开关，配置接口GigabitEthernet1/0/4与Track项1关联时，将输出如下调试信息。

\<Sysname\> debugging standby track

\<Sysname\> terminal monitor

\<Sysname\> terminal debugging

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/4

Sysname-GigabitEthernet1/0/4 backup track 1

\*Feb 27 21:20:46:614 2013 Sysname IB/7/TRACK: -MDC=1; Track add: Interface GigabitEthernet1/0/4 was associated with track entry 1.

\*Feb 27 21:20:46:616 2013 Sysname IB/7/TRACK: -MDC=1; Track modify: Track entry 1 associated with interface GigabitEthernet1/0/4 transitioned to Not ready.

*// 添加一个关联Track的备份接口，由于Track项当前未建立，Track项的状态为Not ready，此时备份接口的链路状态保持原始状态不变*

\# 配置Track项1跟踪的主链路为接口GigabitEthernet1/0/2时，将输出如下调试信息。

Sysname-GigabitEthernet1/0/4 quit

Sysname track 1 interface GigabitEthernet1/0/2

\*Feb 27 21:37:00:144 2013 Sysname IB/7/TRACK: -MDC=1; Track modify: Track entry 1 associated with interface GigabitEthernet1/0/4 transitioned to Positive.

%Feb 27 21:37:00:153 2013 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; GigabitEthernet1/0/4 link status is down.

%Feb 27 21:37:00:154 2013 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface GigabitEthernet1/0/4 is down.

*// 新创建Track项关联时，由于Track项1跟踪的主接口GigabitEthernet1/0/2处于UP状态，Track状态变为positive，此时需要将备份接口GigabitEthernet1/0/4 shutdown，备份接口状态转换为STANDBY状态*
