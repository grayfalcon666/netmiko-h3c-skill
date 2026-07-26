
**3G/4G Modem管理 \-- 3G/4G Modem管理调试命令 \-- debugging cellular**

------------------------------------------------------------------------

【命令】

**[debugging cellular**[ { **error** \| **event** }]]

**[undo debugging cellular**[ { **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging cellular**]命令用来打开cellular的调试信息开关。

**[undo debugging cellular**]命令用来关闭cellular的调试信息开关。

缺省情况下，cellular的调试信息开关处于关闭状态。

表1-1 debugging cellular error命令输出信息描述表

字段

描述

Failed to allocate memory

分配内存失败

Controller *controller-name*: No device plug-in found

接口名为*controller-name*的控制器接口没有找到对应的设备插件

Controller *controller-name*: Failed to get device major number

接口名为*controller-name*的控制器接口获取设备主设备号失败

Controller *controller-name*: Failed to initialize device

接口名为*controller-name*的控制器接口初始化设备失败

Controller *controller-name*: Failed to initialize device, error code is *error-code*

接口名为*controller-name*的控制器接口初始化设备失败，返回错误码*error-code*

Controller *controller-name*: Failed to open device *device-name*

接口名为*controller-name*的控制器接口打开名为*device-name*的设备失败

Controller *controller-name*: Failed to read data from device

接口名为*controller-name*的控制器接口从设备读取数据失败

Controller *controller-name*: Failed to write data to device

接口名为*controller-name*的控制器接口向设备写入数据失败

Controller *controller-name*: Failed to send IOCTL command *command* to device

接口名为*controller-name*的控制器接口向设备下发IOCTL命令字*command*失败

Controller *controller-name*: Failed to reboot device

接口名为*controller-name*的控制器接口重启设备失败

Controller *controller-name*: Failed to send command \"*command-name*\" to device plug-in, error code is *error-code*

接口名为*controller-name*的控制器接口向设备插件下发命令*command-name*失败，错误码为*error-code*

Controller *controller-name*: Failed to complete command \"*command-name*\", error code is *error-code*

接口名为*controller-name*的控制器接口执行名为*command-name*的命令失败，错误码为*error-code*

Controller *controller-name*: Failed to read data from device plug-in, error code is *error-code*

接口名为*controller-name*的控制器接口从设备插件读取数据失败，错误码为*error-code*

Controller *controller-name*: Failed to write data to device plug-in, error code is error-code

接口名为*controller-name*的控制器接口向设备插件写数据失败，错误码为*error-code*

Interface *interface-name*: Failed to send a link message.

接口*interface-name*发送链路消息失败

Interface *interface-name*: Failed to send a dialer message.

接口*interface-name*发送拨号消息失败

Interface *interface-index*: Invalid index in dialer message.

拨号消息中的接口索引*interface-index*非法

Interface *interface-name*: Failed to add new DNS address*.

接口*interface-name*添加新DNS地址失败

Interface *interface-name*: Failed to add new IP address*.

接口*interface-name*添加新IP地址失败

Interface *interface-name*: Failed to get interface information.

接口*interface-name*获取接口信息失败

表1-2 debugging cellular event命令输出信息描述表

字段

描述

Controller *controller-name*: Controller is activated

接口名为*controller-name*的控制器接口被激活

Controller *controller-name*: Controller is deactivated

接口名为*controller-name*的控制器接口被去激活

Controller *controller-name*: Controller is deleted

接口名为*controller-name*的控制器接口被删除

Controller *controller-name*: Opened device *device-name*

接口名为*controller-name*的控制器接口打开了设备名为*device-name*的设备

Controller *controller-name*: Closed device

接口名为*controller-name*的控制器接口关闭了设备

Controller *controller-name*: Device major No. is *major-number*

接口名为*controller-name*的控制器接口的设备的主设备号为*major-number*

Controller *controller-name*: Initializing device

接口名为*controller-name*的控制器接口正在初始化设备

Controller *controller-name*: Device initialization completed

接口名为*controller-name*的控制器接口的设备初始化完成

Controller *controller-name*: Device removing completed

接口名为*controller-name*的控制器接口的设备拔出完成

Controller *controller-name*: Device is rebooted

接口名为*controller-name*的控制器接口的设备被重启

Controller *controller-name*: Read *byte-counts* bytes of data from device

接口名为*controller-name*的控制器接从设备读取了*byte-counts*字节的数据

Controller *controller-name*: Wrote *byte-counts* bytes of data to device

接口名为*controller-name*的控制器接口向设备写了*byte-counts*字节的数据

Controller *controller-name*: Sent IOCTL command *command-value* to device

接口名为*controller-name*的控制器接口向设备发送值为*command-value*的IOCTL命令字

Controller *controller-name*: Read data from device plug-in

接口名为*controller-name*的控制器接口从设备插件读取了数据

Controller *controller-name*: Wrote *byte-counts* bytes of data to device plug-in

接口名为*controller-name*的控制器接口向设备插件写了*byte-counts*字节的数据

Sent command *command-name* to device plug-in (major No. *major-number*)

向主设备号为*major-number*的设备插件发送名为*command-name*的命令

Controller *controller-name*: Sent command *command-name* to device plug-in

接口名为*controller-name*的控制器接口向设备插件发送名为*command-name*的命令字

Controller *controller-name*: Command *command-name* completed

接口名为*controller-name*的控制器接口名为*command-name*的命令处理完成

Added timer *timer-id*, whose interval is *time-interval* seconds

创建ID为*timer-id*的定时器，超时时间为*time-interval*秒

Controller *controller-name*: Added timer *timer-id*, whose interval is *time-interval* seconds

接口名为*controller-name*的控制器接口创建ID为*timer-id*的定时器，超时时间为*time-interval*秒

Timer timed out

定时器超时

Controller *controller-name*: Timer timed out

接口名为*controller-name*的控制器接口下定时器超时

Suspended timer *timer-id*

ID为*timer-id*的定时器被挂起

Activated timer *timer-id*

ID为*timer-id*的定时器被激活

Refreshed timer *timer-id*\'s interval to *time-interval* seconds

修改ID为*timer-id*的定时器超时时间，超时时间为*time-interval*秒

Deleted timer *timer-id*

ID为*timer-id*的定时器被删除

Interface *interface-name*: Received event up.

接口*interface-name* up

Interface *interface-name*: Received event down.

接口*interface-name* down

Interface *interface-name*: Received event deactivated.

接口*interface-name*去激活

【举例】

\# 打开cellular的事件调试信息开关。

\<Sysname\> debugging cellular event

\# 重启cellular控制器上的3G modem。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 modem reboot

Sysname-Cellular2/4/0

\*Jun 19 16:56:02:074 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Device is rebooted

*[// 3G Modem*]*被重启*

%Jun 19 16:56:02:075 2012 Sysname CELLULAR/4/DEV_REMOVED: -MDC=1; Controller Cellular2/4/0: 3G Modem device is removed.

\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Sent IOCTL command 4302 to device

\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Device removing completed

*[// 3G Modem*]*被移除*

%Jun 19 16:56:02:075 2012 Sysname CELLULAR/4/DEV_INSERTED: -MDC=1; Controller Cellular2/4/0: 3G Modem device is inserted.

*[// 3G Modem*]*被插入*

\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Sent IOCTL command 80044300 to device

\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Device major No. is 1

*[// 3G Modem*]*主设备号为1*

\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Initializing device

*// 初始化3G Modem*

\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Added timer 0, interval is 30 seconds

\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Added timer 1, interval is 3 seconds

\*Jun 19 16:56:05:484 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Timer timed out

\*Jun 19 16:56:05:484 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Device initialization completed

\*Jun 19 16:56:05:484 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Deleted timer 1

*// 初始化3G Modem完成*

\# 以太网通道接口拨号成功。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 interface eth-channel 0

Sysname-Eth-channel2/4/0:0 dialer circular enable

Sysname-Eth-channel2/4/0:0 dialer number 1 autodial

Sysname-Eth-channel2/4/0:0 dialer timer autodial 10

\*Aug 20 20:34:36:543 2013 Sysname LTE/7/EVENT: -MDC=1; Interface Echannel2/4/0:0: Received event up.

*// 以太网通道接口Eth-channel2/4/0:0接口up*

\# 打开cellular的错误调试信息开关。

\<Sysname\> debugging cellular error

\# 在SIM卡被锁的3G Modem上启用PIN码认证功能。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 pin verification enable 666666

SIM card has been locked. Please verify PIN first.

Sysname-Cellular2/4/0

\*Jun 19 17:16:34:574 2012 Sysname CELLULAR/7/ERROR: -MDC=1; Controller Cellular2/4/0: Failed to complete command \"pin verification enable\", error code is 23670002

*// 下发命令行pin verification enable失败，错误码为23670002*

\# 以太网通道接口添加新DNS地址失败。

\<Sysname\> system-view

Sysname controller cellular 2/4/0

Sysname-Cellular2/4/0 interface eth-channel 0

Sysname-Eth-channel2/4/0:0 dialer circular enable

Sysname-Eth-channel2/4/0:0 dialer number 1 autodial

Sysname-Eth-channel2/4/0:0 dialer timer autodial 10

\*Aug 20 20:34:36:543 2013 Sysname LTE/7/ERROR: -MDC=1; Interface Echannel2/4/0:0: Failed to add new DNS address.

*// 以太网通道接口Eth-channel2/4/0:0接口添加新DNS地址失败*

**3G/4G Modem管理 \-- 3G/4G Modem管理调试命令 \-- debugging cellular plugin**

------------------------------------------------------------------------

【命令】

**[debugging cellular plugin**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging cellular plugin**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging cellular plugin**]命令用来打开插件的调试信息开关。

**[undo debugging cellular plugin**]命令用来关闭插件的调试信息开关。

缺省情况下，插件的调试信息开关处于关闭状态。

该命令的调试信息由3G/4G Modem产品插件输出，不同的3G/4G Modem插件输出信息不同。

