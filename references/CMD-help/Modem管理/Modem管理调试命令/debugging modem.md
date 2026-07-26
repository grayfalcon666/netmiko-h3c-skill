
**Modem管理 \-- Modem管理调试命令 \-- debugging modem**

------------------------------------------------------------------------

【命令】

**[debugging modem**[ { **all** \| **error** \| **event** } [ **interface** *interface-type* *interface-number* ]]]

**[undo debugging modem**[ { **all** \| **error** \| **event** } [ **interface** *interface-type* *interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[interface ***interface-type interface-number*]：表示指定接口的调试信息开关，不指定该参数时，表示所有接口的调试信息开关。

【描述】

**[debugging modem **]命令用来打开Modem管理的调试信息开关。

**[undo debugging modem**]命令用来关闭Modem管理的调试信息开关。

缺省情况下，Modem管理的调试信息开关处于关闭状态。

表1-1 debugging modem error命令输出信息描述表

字段

描述

Failed to allocate memory

分配内存失败

Failed to send message to IO board

向IO板发送消息失败

Failed to create timer

创建定时器失败

Failed to connect to dialer

连接dialer失败

Failed to connect to TTY

连接TTY失败

Interface *interface-name*: Failed to get TTY name

接口名为*interface-name*的接口获取TTY名称失败

Interface *interface-name*: Failed to open TTY *tty-name*

接口名为*interface-name*的接口打开名字为*tty-name*的TTY失败

Interface *interface-name*: Failed to send message *message-name* to TTY

接口名为*interface-name*的接口向TTY发送内容为*message-name*的消息失败

Interface *interface-name*: Failed to send message *message-name* to dialer

接口名为*interface-name*的接口向dialer发送内容为*message-name*的消息失败

Interface *interface-name*: Call-in is not enabled

接口名为*interface-name*的接口没有启用呼入功能

Interface *interface-name*: Call-out is not enabled

接口名为*interface-name*的接口没有启用呼出功能

Interface *interface-name*: A call is active now on this interface

接口名为*interface-name*的接口已经存在一路呼叫

Interface *interface-name*: Interface has been shut down

接口名为*interface-name*的接口已经被关闭

Interface *interface-name*: Interface is not working in protocol mode

接口名为*interface-name*的接口没有工作在协议模式

Interface *interface-name*: Interface is not working in flow mode

接口名为*interface-name*的接口没有工作在流模式

Interface *interface-name*: Failed to create asynchronous modem

接口名为*interface-name*的接口创建异步modem失败

Interface *interface-name*: Failed to delete asynchronous modem

接口名为*interface-name*的接口删除异步modem失败

Interface *interface-name*: Failed to enable modem

接口名为*interface-name*的接口启用modem失败

Interface *interface-name*: Failed to disable modem

接口名为*interface-name*的接口关闭modem失败

Interface *interface-name*: Failed to send AT command *at-string* to modem

接口名为*interface-name*的接口向modem发送内容为*at-string*的AT指令失败

Interface *interface-name*: Failed to configure modem to work in flow mode

接口名为*interface-name*的接口设置modem为流模式失败

Interface *interface-name*: Failed to configure modem to work in protocol mode

接口名为*interface-name*的接口设置modem为协议模式失败

Interface *interface-name*: Failed to configure modem to work in AT mode

接口名为*interface-name*的接口设置modem为AT指令模式失败

Interface *interface-name*: Failed to set modem country code to *country-name*

接口名为*interface-name*的接口设置modem的国家码为*country-name*国家失败

Interface *interface-name*: Failed to enable modem caller number resolving

接口名为*interface-name*的接口启用modem获取终端主叫号码功能失败

Interface *interface-name*: Failed to disable modem caller number resolving

接口名为*interface-name*的接口关闭modem获取终端主叫号码功能失败

表1-2 debugging modem event命令输出信息描述表

字段

描述

Interface *interface-name*: Enabled modem

接口名为*interface-name*的接口启用modem功能

Interface *interface-name*: Disabled modem

接口名为*interface-name*的接口关闭modem功能

Interface *interface-name*: Created asynchronous modem

接口名为*interface-name*的接口创建异步modem

Interface *interface-name*: Deleted asynchronous modem

接口名为*interface-name*的接口删除异步modem

Interface *interface-name*: Configured modem to work in flow mode

接口名为*interface-name*的接口设置modem的工作模式为流模式

Interface *interface-name*: Configured modem to work in protocol mode

接口名为*interface-name*的接口设置modem的工作模式为协议模式

Interface *interface-name*: Configured modem to work in AT mode

接口名为*interface-name*的接口设置modem的工作模式为AT指令模式

Interface *interface-name*: Set modem country code to *country-name*

接口名为*interface-name*的接口设置modem的国家码为*country-name*国家

Interface *interface-name*: Enabled modem caller number resolving

接口名为*interface-name*的接口启用modem获取终端主叫号码功能

Interface *interface-name*: Disabled modem caller number resolving

接口名为*interface-name*的接口关闭modem获取终端主叫号码功能

Interface *interface-name*: Sent AT command *at-string* to modem

接口名为*interface-name*的接口向modem发送内容为*at-string*的AT指令

Interface *interface-name*: Started call-in processing

接口名为*interface-name*的接口开始呼入处理

Interface *interface-name*: Started call-out processing

接口名为*interface-name*的接口开始呼出处理

Interface *interface-name*: Started baud rate negotiation

接口名为*interface-name*的接口开始波特率协商

Interface *interface-name*: Stopped baud rate negotiation

接口名为*interface-name*的接口停止波特率协商

Interface *interface-name*: Waiting to resolve caller number for *time-interval* ms

接口名为*interface-name*的接口等待*time-interval*毫秒以获取终端主叫号码

Interface *interface-name*: Waiting carrier detection for *time-interval* ms

接口名为*interface-name*的接口等待*time-interval*毫秒以进行载波检测

Interface *interface-name*: Resolved caller number

接口名为*interface-name*的接口获取到终端主叫号码

Interface *interface-name*: Waiting for resolving caller number timed out

接口名为*interface-name*的接口获取终端主叫号码超时

Interface *interface-name*: Waiting for carrier detection timed out

接口名为*interface-name*的接口载波检测超时

Interface *interface-name*: Modem would be restarted in *time-interval* ms

接口名为*interface-name*的接口将于*time-interval*毫秒后重启modem

Interface *interface-name*: FSM state changed from *pre-state* to *next-state*

接口名为*interface-name*的接口状态机从*pre-state*状态迁移到*next-state*状态

Interface *interface-name*: Interface has been shut down

接口名为*interface-name*的接口已经被关闭

Interface *interface-name*: Interface is turned on

接口名为*interface-name*的接口被启用

Interface *interface-name*: Interface is shut down

接口名为*interface-name*的接口被关闭

Interface *interface-name*: Interface is deleted

接口名为*interface-name*的接口被删除

Interface *interface-name*: Interface is deactivated

接口名为*interface-name*的接口被去激活

Interface *interface-name*: Interface is activated

接口名为*interface-name*的接口被激活

Interface *interface-name*: Interface physical mode is changed to asynchronous mode

接口名为*interface-name*的接口物理模式被切换为异步模式

Interface *interface-name*: Interface physical mode is changed to synchronous mode

接口名为*interface-name*的接口物理模式被切换为同步模式

Interface *interface-name*: Discarded message *at-string* from modem

接口名为*interface-name*的接口丢弃了来自modem的AT消息，消息内容为*at-string*

Interface *interface-name*: Received message *at-string* from modem

接口名为*interface-name*的接口接收到来自modem的AT消息，消息内容为*at-string*

Interface *interface-name*: Opened TTY *tty-name*

接口名为*interface-name*的接口打开了名字为*tty-name*的TTY

Interface *interface-name*: Closed TTY

接口名为*interface-name*的接口关闭了

Interface *interface-name*: Received message *message-name* from TTY

接口名为*interface-name*的接口收到了来自TTY内容为*message-name*的消息

Interface *interface-name*: Sent message *message-name* to TTY

接口名为*interface-name*的接口向TTY发送内容为*message-name*的消息

Interface *interface-name*: Received message *message-name* from dialer

接口名为*interface-name*的接口收到了来自dialer内容为*message-name*的消息

Interface *interface-name*: Sent message *message-name* to dialer

接口名为*interface-name*的接口向dialer发送内容为*message-name*的消息

【举例】

\# 配置DDR拨号。

\<Sysname\> system-view

Sysname dialer-group 1 rule ip permit

Sysname interface dialer 1

Sysname-Dialer1 ip address 1.0.0.1 24

Sysname-Dialer1 dialer circular enable

Sysname-Dialer1 dialer-group 1

Sysname-Dialer1 dialer number 123456

Sysname-Dialer1 quit

Sysname interface serial 2/1/2

Sysname-Serial2/1/2 physical-mode async

Sysname-Serial2/1/2 dialer circular enable

Sysname-Serial2/1/2 dialer circular-group 1

Sysname-Serial2/1/2 return

\# 打开Modem管理的事件调试信息开关。

\<Sysname\> debugging modem event

\# 启用modem呼出功能。

\<Sysname\> system-view

Sysname line tty 2

Sysname-line-tty2 modem enable call-out

\*Jun 13 09:39:27:799 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message MODEM_ENABLED to TTY

*// 通知TTY启用modem功能*

\*Jun 13 09:39:27:799 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message GET_TTY to TTY

\*Jun 13 09:39:27:799 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message TTY_READY from TTY

*// 向TTY获取TTY控制权限*

\*Jun 13 09:39:27:800 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Open TTY /dev/tty6

*// 打开TTY*

\*Jun 13 09:39:27:800 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Created asynchronous modem

*// 创建异步modem*

\*Jun 13 09:39:27:801 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Set modem to AT mode

*// 设置modem工作在AT指令模式*

\*Jun 13 09:39:27:801 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from INVALID to DISCONNECT

*// 进入DISCONNECT状态*

\*Jun 13 09:39:27:801 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Disabled modem

*// 关闭modem *

\*Jun 13 09:39:27:802 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Modem would be restarted in 2000 ms

*[// 2*]*秒后重新启用modem *

\*Jun 13 09:39:30:803 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Enabled modem

\*Jun 13 09:39:30:803 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from DISCONNECT to IDLE

\*Jun 13 09:39:30:803 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Started baud rate negotiation

*// 进入IDLE状态，开始波特率协商*

Sysname-line-tty2 return

\*Jun 13 09:39:36:809 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command AT to modem

\*Jun 13 09:39:41:804 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command AT to modem

*// 发送AT指令进行波特率协商*

\# 通过ping命令触发DDR进行拨号。

\<Sysname\> ping -c 1 1.0.0.2

Ping 1.0.0.2 (1.0.0.2): 56 data bytes, press CTRL_C to break

\*Jun 13 09:39:52:949 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message DDR_DIALPRIM_CONN_REQ from dialer

*// 收到DDR拨号请求*

\*Jun 13 09:39:52:949 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Stopped baud rate negotiation

*// 停止波特率协商*

\*Jun 13 09:39:52:949 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Started call-out processing

*// 开始呼出处理*

\*Jun 13 09:39:52:949 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command ATDT123456 to modem

*// 发送拨号指令*

\*Jun 13 09:39:52:951 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from IDLE to CONNECT

\*Jun 13 09:39:52:951 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Waiting carrier detection for 60000 ms

*// 进入CONNECT状态，等待检测载波信号*

\*Jun 13 09:39:52:952 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message CD UP from modem

*// 收到CD UP消息，链路建立成功*

\*Jun 13 09:39:52:952 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Set modem to protocol mode

*// 设置modem工作在协议模式*

\*Jun 13 09:39:52:953 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Close TTY

\*Jun 13 09:39:52:953 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message PUT_TTY to TTY

*// 关闭TTY，释放TTY权限*

\*Jun 13 09:39:52:953 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from CONNECT to ACTIVE

*// 进入ACTIVE状态*

\*Jun 13 09:39:52:953 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message DDR_DIALPRIM_CONN_IND to dialer

*// 通知DDR拨号完成*

%Jun 13 09:39:52:954 2012 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Serial2/1/2 link status is UP.

Request time out

\-\-- Ping statistics for 1.0.0.2 \-\--

1 packet(s) transmitted, 0 packet(s) received, 100.0% packet loss

%Jun 13 09:39:56:050 2012 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface Serial2/1/2 is UP.

\<Sysname\>

\<Sysname\>

\<Sysname\>

\*Jun 13 09:40:33:158 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message CD DOWN from modem

*// 收到CD DOWN消息，对端拆链*

\*Jun 13 09:40:33:158 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message GET_TTY to TTY

\*Jun 13 09:40:33:159 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message TTY_READY from TTY

*// 向TTY获取TTY控制权限*

\*Jun 13 09:40:33:159 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Open TTY /dev/tty6

*// 打开TTY*

*// 设置modem工作在AT指令模式*

\*Jun 13 09:40:33:159 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command +++ to modem

*// 向modem发送拆链指令+++*

\*Jun 13 09:40:33:160 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message DDR_DIALPRIM_DISCONN_IND to dialer

*// 通知DDR连接断开*

%Jun 13 09:40:33:161 2012 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Serial2/1/2 link status is DOWN.

%Jun 13 09:40:33:161 2012 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface Serial2/1/2 is DOWN.

\*Jun 13 09:40:33:161 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from ACTIVE to DISCONNECT

*// 进入DISCONNECT状态*

\*Jun 13 09:40:33:161 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Disabled modem

*// 关闭modem*

\*Jun 13 09:40:33:162 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Modem would be restarted in 2000 ms

*[// 2*]*秒后重新启用modem*

\*Jun 13 09:40:36:163 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Enabled modem

\*Jun 13 09:40:36:163 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from DISCONNECT to IDLE

\*Jun 13 09:40:36:163 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Started baud rate negotiation

*// 进入IDLE状态，开始波特率协商*

\*Jun 13 09:40:42:164 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command AT to modem

\*Jun 13 09:40:47:164 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command AT to modem

*// 发送AT指令进行波特率协商*

\# 打开Modem管理的错误调试信息开关。

\<Sysname\> debugging modem error

\# 启用modem呼入功能。

\<Sysname\> system-view

Sysname line tty 2

Sysname-line-tty2 modem enable call-in

Sysname-line-tty2 return

\# 通过ping命令触发DDR进行拨号。

\<Sysname\> ping -c 1 1.0.0.2

Ping 1.0.0.2 (1.0.0.2): 56 data bytes, press CTRL_C to break

\*Jun 19 09:44:44:288 2012 Sysname MODEM/7/ERROR: -MDC=1; Interface Serial2/1/2: Call-out is not enabled

*[// Modem*]*呼出功能未启用*

Request time out

\-\-- Ping statistics for 1.0.0.2 \-\--

1 packet(s) transmitted, 0 packet(s) received, 100.0% packet loss

