<!-- CMD-INDEX
  debugging esmc all                  | 用户视图             | L9
  debugging esmc error                | 用户视图             | L39
  debugging esmc event                | 用户视图             | L133
  debugging esmc packet               | 用户视图             | L187
  debugging esmc timer                | 用户视图             | L301
-->

**同步以太网 \-- 同步以太网调试命令 \-- debugging esmc all**

------------------------------------------------------------------------

【命令】

**[debugging esmc all**]

**[undo debugging esmc all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging esmc all**]命令用于打开ESMC的所有调试信息开关。**undo debugging esmc all**命令用于关闭ESMC的所有调试信息开关。

缺省情况下，ESMC的所有调试信息开关处于关闭状态。

**同步以太网 \-- 同步以太网调试命令 \-- debugging esmc error**

------------------------------------------------------------------------

【命令】

**[debugging esmc error**]

**[undo debugging esmc error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging esmc error**]命令用来打开ESMC错误调试信息开关。**undo debugging esmc error**命令用来关闭ESMC错误调试信息开关。

缺省情况下，ESMC错误调试信息开关处于关闭状态。

表1-1 debugging esmc error命令输出信息描述表

字段

描述

*[IfName* received an ESMC packet with invalid packet length.]

接口*IfName*收到一个报文长度无效的ESMC报文

*[IfName* received an ESMC packet with invalid ITU OUI.]

接口*IfName*收到一个ITU OUI无效的ESMC报文

*[IfName* received an ESMC packet with invalid ITU subtype.]

接口*IfName*收到一个ITU子类型无效的ESMC报文

*[IfName* received an ESMC packet with invalid version.]

接口*IfName*收到一个版本号无效的ESMC报文

*[IfName* received an ESMC packet with invalid TLV length.]

接口*IfName*收到一个TLV长度无效的ESMC报文

*[IfName* received an ESMC packet with the first TLV that is not QL TLV.]

接口*IfName*收到ESMC报文的第一个TLV不是QL TLV

*[IfName* received an ESMC packet with invalid QL value.]

接口*IfName*收到一个QL无效的ESMC报文

【举例】

 # 配置同步以太网功能，并打开ESMC错误调试信息开关。

\<Sysname\> debugging esmc error

\*Apr 07 14:23:58:531 2013 Sysname ESMC/7/ERROR: GigabitEthernet1/0/1 received an ESMC packet with invalid packet length.

*// 接口GigabitEthernet1/0/1收到一个报文长度无效的ESMC报文*

\*Apr 07 14:27:16:968 2013 Sysname ESMC/7/ERROR: GigabitEthernet1/0/1 received an ESMC packet with invalid ITU OUI.

*// 接口GigabitEthernet1/0/1收到一个ITU OUI无效的ESMC报文*

\*Apr 07 14:36:35:312 2013 Sysname ESMC/7/ERROR: GigabitEthernet1/0/1 received an ESMC packet with invalid ITU subtype.

*// 接口GigabitEthernet1/0/1收到一个ITU子类型无效的ESMC报文*

\*Apr 07 14:36:35:312 2013 Sysname ESMC/7/ERROR: GigabitEthernet1/0/1 received an ESMC packet with invalid version.

*// 接口GigabitEthernet1/0/1收到一个版本号无效的ESMC报文*

\*Apr 07 14:38:16:672 2013 Sysname ESMC/7/ERROR: GigabitEthernet1/0/1 received an ESMC packet with invalid TLV length.

*// 接口GigabitEthernet1/0/1收到一个TLV长度无效的ESMC报文*

\*Apr 07 14:38:35:672 2013 Sysname ESMC/7/ERROR: GigabitEthernet1/0/1 received an ESMC packet with the first TLV that is not QL TLV.

*// 接口GigabitEthernet1/0/1收到ESMC报文的第一个TLV不是QL TLV*

\*Apr 07 14:38:35:672 2013 Sysname ESMC/7/ERROR: GigabitEthernet1/0/1 received an ESMC packet with invalid QL value.

*// 接口GigabitEthernet1/0/1收到一个QL值无效的ESMC报文*

**同步以太网 \-- 同步以太网调试命令 \-- debugging esmc event**

------------------------------------------------------------------------

【命令】

**[debugging esmc event**]

**[undo debugging esmc event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging esmc event**]命令用来打开ESMC事件调试信息开关。**undo debugging esmc event**命令用来关闭ESMC 事件调试信息开关。

缺省情况下，ESMC事件调试信息开关处于关闭状态。

表1-2 debugging esmc event命令输出信息描述表

字段

描述

Received *IF_event_name* event for interface *IfName.*

收到接口*IfName*的*IF_event_name*事件，*IF*\_*event_name*包括IF_DELETE、IF_UP、IF_DOWN、IF_ACTIVE、IF_DEACTIVE、IF_HALFDUPLEX、IF_FULLDUPLEX

Received System Clock QL Changed event.

收到系统时钟质量等级变化事件

【举例】

\# 配置同步以太网功能，并打开ESMC事件调试信息开关。

\<Sysname\> debugging esmc event

\*Apr 07 14:23:58:531 2013 Sysname ESMC/7/EVENT: [Received IF_DEACTIVE event for interface GigabitEthernet1/0/1.{.TerminalDisplayChar}]

*// 收到接口去激活事件，接口为GigabitEthernet1/0/1*

\*Apr 07 14:27:16:968 2013 Sysname ESMC/7/EVENT: Received System Clock QL Changed event.

*// 收到系统时钟质量等级变化事件*

**同步以太网 \-- 同步以太网调试命令 \-- debugging esmc packet**

------------------------------------------------------------------------

【命令】

**[debugging esmc packet**]

**[undo debugging esmc packet**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging esmc packet**]命令用来打开ESMC报文调试信息开关。**undo debugging esmc packet**命令用来关闭ESMC 报文调试信息开关。

缺省情况下，ESMC报文调试信息开关处于关闭状态。

表1-3 debugging esmc packet命令输出信息描述表

字段

描述

*[IfName* received an ESMC packet with a length of *ulMsgTotal* Bytes.]

接口*IfName*收到ESMC报文，报文长度为*ulMsgTotal*字节

*[IfName* sent an ESMC packet with a length of *ulMsgTotal* Bytes.]

接口*IfName*发送ESMC报文，报文长度为*ulMsgTotal*字节

ITU-OUI

ITU组织唯一标识

ITU subtype

ITU子类型

Version

协议版本

Event flag

报文是否为事件报文：

·0：是信息报文

·1：是事件报文

SSM code

SSM码取值，代表时钟源的质量等级：

·QL-UNK：SSM级别为UNKNOWN（时钟源的同步质量未知）

·QL-PRC：SSM级别为PRC（G.811时钟信号）

·QL-SSU-A：SSM级别为SSU-A（G.812转接节点时钟信号）

·QL-SSU-B：SSM级别为SSU-B（G.812本地节点时钟信号）

·QL-SEC：SSM级别为SEC（SDH设备时钟源信号）

·QL-DNU：SSM级别为DNU（不应用作同步）

【举例】

\# 配置同步以太网功能，并打开ESMC报文调试信息开关。

\<Sysname\> debugging esmc packet

\*Apr 07 14:23:58:531 2013 Sysname ESMC/7/PACKET:

GigabitEthernet1/0/1 {.TerminalDisplayChar}received an ESMC packet with a length of 64 Bytes.

ITU-OUI         : 00-19-A7

ITU subtype     : 0x0001

Version         : 0x1

Event flag      : 0

SSM code        : 0x02(QL-PRC)

*// 接口GigabitEthernet1/0/1接收报文的具体内容，长度为64字节*

\*Apr 07 14:27:16:968 2013 Sysname ESMC/7/PACKET:

GigabitEthernet1/0/1 {.TerminalDisplayChar}sent an ESMC packet with a length of 64 Bytes.

ITU-OUI         : 00-19-A7

ITU subtype     : 0x0001

Version         : 0x1

Event flag      : 1

SSM code        : 0x02(QL-PRC)

*// 接口GigabitEthernet1/0/1发送报文的具体内容，长度为64字节*

**同步以太网 \-- 同步以太网调试命令 \-- debugging esmc timer**

------------------------------------------------------------------------

【命令】

**[debugging esmc timer**]

**[undo debugging esmc timer**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging esmc timer**]命令用来打开ESMC定时器调试信息开关。**undo debugging esmc timer**命令用来关闭ESMC 定时器调试信息开关。

缺省情况下，ESMC定时器调试信息开关处于关闭状态。

表1-4 debugging esmc timer命令输出信息描述表

字段

描述

Timer for periodically sending ESMC packets was successfully created on *IfName,* with the timer ID *TimerID.*

接口*IfName*创建ESMC报文周期性发送定时器成功，定时器ID为*TimerID*

Timer for periodically sending ESMC packets was successfully destroyed on *IfName*, with the timer ID *TimerID*.

接口*IfName*删除ESMC报文周期性发送定时器成功，定时器ID为*TimerID*

Timer for receiving ESMC packets was successfully created on *IfName*, with the timer ID *TimerID*.

接口*IfName*创建ESMC报文接收超时定时器成功，定时器ID为*TimerID*

Timer for receiving ESMC packets was successfully destroyed on *IfName*, with the timer ID *TimerID*.

接口*IfName*删除ESMC报文接收超时定时器成功，定时器ID为*TimerID*

【举例】

\# 配置同步以太网功能，并打开ESMC定时器调试信息开关。

\<Sysname\> debugging esmc timer

\*Apr 07 14:23:58:531 2013 Sysname ESMC/7/TIMER: Timer for periodically sending ESMC packets was successfully created on GigabitEthernet1/0/1，with the timer ID 3.

*// 接口GigabitEthernet1/0/1创建ESMC报文周期性发送定时器，定时器ID为3*

\*Apr 07 14:27:16:968 2013 Sysname ESMC/7/TIMER: Timer for periodically sending ESMC packets was successfully destroyed on GigabitEthernet1/0/1, with the timer ID 3.

*// 接口GigabitEthernet1/0/1删除ESMC报文周期性发送定时器，定时器ID为3*

\*Apr 07 14:31:55:221 2013 Sysname ESMC/7/TIMER: Timer for receiving ESMC packets was successfully created on GigabitEthernet1/0/1, with the timer ID 4.

*// 接口GigabitEthernet1/0/1创建ESMC报文接收超时定时器，定时器ID为4*

\*Apr 07 14:38:11:857 2013 Sysname ESMC/7/TIMER: Timer for receiving ESMC packets was successfully destroyed on GigabitEthernet1/0/1, with the timer ID 4.

*// 接口GigabitEthernet1/0/1删除ESMC报文接收超时定时器，定时器ID为4*

