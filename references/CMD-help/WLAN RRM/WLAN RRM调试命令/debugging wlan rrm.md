
**WLAN RRM \-- WLAN RRM调试命令 \-- debugging wlan rrm**

------------------------------------------------------------------------

【命令】

**[debugging**[ **wlan rrm** { **all** \| **error** \| **event** \| **timer** }]]

**[undo debugging**[ **wlan rrm** { **all** \| **error** \| **event** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示RRM所有调试信息开关。

**[error**]：表示RRM的错误调试信息开关。

**[event**]：表示RRM的事件调试信息开关。

**[timer**]：表示RRM的定时器调试信息开关。

【描述】

**[debugging wlan rrm**]命令用来打开RRM调试信息开关。**undo debugging wlan rrm**命令用来关闭RRM调试信息开关。

缺省情况下，RRM调试信息开关处于关闭状态。

表1-1 debugging wlan rrm error令输出信息描述表

字段

描述

Failed to get an algorithm for channel calibration.

获取调整信道算法失败

Failed to calibrate channel.

调整信道失败

Failed to get an algorithm for power calibration.

获取调整功率算法失败

Failed to calibrate power.

调整功率失败

Failed to add node to radar hash list.

向雷达事件调整链表添加节点失败

Failed to add node to radio-down hash list.

向射频断开调整链表添加节点失败

Failed to process radio down event.

处理射频断开事件失败

Failed to process radar event.

处理雷达事件失败

表1-2 debugging wlan rrm event令输出信息描述表

字段

描述

Don\'t calibrate power: Access is disabled.{.MsoCommentReference}

没有接入无线服务，不需要调整功率

No radio needs to be calibrated.

没有Raido需要调整

Didn\'t find information about the radio that detected the radar event.

和雷达冲突的Raido信息不存在

Found the following *radio-type* radios that need to be calibrated:

AP name: *apname*, Radio:*radioid*, Calibrated channel: *channel*, Calibrated power:*power.*

在Raido模式为*radio-type*时，所有需要调整的节点有：

AP name为*apname*，Radio ID为*radioid*，信道调整标记为*isClbChl*，功率调整标记为*isClbPwr*。其中信道调整标记为1/0，0代表不会进行信道调整，1代表会进行信道调整；功率调整标记为1/0，0代表不会进行功率调整，1代表会进行功率调整

Received a radio down event.

收到Radio down事件

Received a radio up event.

收到Radio up事件

Received a radio mode change event.

收到Radio模式变更事件

Received an inquiry for channel advice.

收到询问推荐信道事件

Received an AP create event.

收到AP创建事件

Received an AP delete event.

收到AP删除事件

Received an AP up event.

收到AP上线事件

Received a radio service on event.

收到Radio服务开始事件

Received a radio service off event.

收到Radio服务终止事件

表1-3 debugging wlan rrm timer命令输出信息描述表

字段

描述

Calibration timer expired.

调整定时器超时

Topology update timer expired.

拓扑更新定时器超时

【举例】

\# 在设备上打开RRM的调试信息开关。

\<Sysname\> debugging wlan rrm all

\<Sysname\>\*Apr 15 16:49:24:679 2014 Sysname RRM/7/RRM_DEBUG:

RRM_EVENT: Received an AP delete event.

*[// RRM*]*收到APMGR的AP删除事件*

\*Apr 15 16:49:24:679 2014 Sysname Sysname RRM/7/RRM_DEBUG:

RRM_TIMER: Calibration timer expired.

*// 信道和功率调整定时器超时*

**

\*Apr 15 16:49:24:680 2014 Sysname RRM/7/RRM_DEBUG:

RRM_ERROR: Failed to calibrate channel.

*// 调整信道失败*
