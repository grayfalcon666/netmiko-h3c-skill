<!-- CMD-INDEX
  debugging posa all                  | 用户视图             | L9
  debugging posa event                | 用户视图             | L57
  debugging posa timer                | 用户视图             | L531
  debugging posa error                | 用户视图             | L633
  debugging posa packet               | 用户视图             | L917
-->

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa all**

------------------------------------------------------------------------

【命令】

**[debugging posa all **[[ **terminal** *terminal-id* \| **app** *app-id* ]]]

**[undo debugging posa all **[[ **terminal** *terminal-id* \| **app** *app-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[terminal*** terminal-id*]：POS终端模板ID，取值范围为1～255。

**[app*** app-id*]：应用模板ID，取值范围为1～1024。

【描述】

**[debugging posa all**]命令用来打开POS接入所有调试开关。**undo debugging posa all**命令用来关闭POS接入所有调试开关。

缺省情况下，POS接入所有调试开关处于关闭状态。

【举例】

\# 打开POS接入所有调试开关，系统视图下，创建TCP接入方式的终端模板1，端口为3000。

\<System\> debugging posa all

System\*Aug  7 18:20:48:047 2012 System POSA/7/EVENT: -MDC=1; Recv LIPC message type:

SET, code:ADDTERM, sequence:0, length:13.

\*Aug  7 18:20:48:047 2012 System POSA/7/EVENT: -MDC=1; Terminal 1:Add template.

\*Aug  7 18:20:48:048 2012 System POSA/7/EVENT: -MDC=1; Terminal 1:Enable template.

*// 添加终端模板成功*

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa event**

------------------------------------------------------------------------

【命令】

**[debugging posa event**[ [ **terminal** *terminal-id* \| **app** *app-id* ]]]

**[undo debugging posa event**[ [ **terminal** *terminal-id* \| **app** *app-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[terminal*** terminal-id*]：终端模板ID，取值范围为1～255。

**[app*** app-id*]：应用模板ID，取值范围为1～1024。

【描述】

**[debugging posa event**]命令用来打开POS接入事件调试开关。**undo debugging posa event**命令用来关闭POS接入事件调试开关。

缺省情况下，POS接入事件调试开关处于关闭状态。

表1-1 debugging posa event命令输出信息描述表

字段

描述

Added map dest:*a*, src:*b*, app:*n*.

添加map节点，目的地址为a，源地址为b

Deleted map dest:*a*, src:*b*.

删除map节点，目的地址为a，源地址为b

Changed app of map(dest:*a*,src:*b*) from *m* to *n*.

修改map表，目的地址为a，源地址为b

Terminal *n*: Terminal instance m found matching app *n*.

终端*n*：终端实例匹配map表

App *n*: Sent AM-CID packet.

应用*n*：发送AM-CID报文

App *n*: Received response for AM-CID packet.

应用*n*：应用实例收到AM-CID的回应报文

App *n /* Terminal *n*: Enabled template.

应用*n / *终端*n*：使能模板

App *n /* Terminal *n*: Disabled template.

应用*n / *终端*n*：去使能模板

App *n / * Terminal *n*: Add template.

应用*n / *终端*n*：添加模板

App *n /* Terminal *n*: Deleted template.

应用*n / *终端*n*：删除模板

App *n*: Bound app to interface.

应用*n*：应用模板与接口绑定

App n:Unbound app from interface.

应用*n*：取消应用模板与接口的绑定

App *n /* Terminal *n*: Failed to add template, The template ID has existed.

应用*n / *终端*n*：由于模板已存在，导致添加模板失败

App *n /* Terminal *n*: Failed to bind interface,The interface has been bounded.

应用*n / *终端*n*：由于接口已被绑定，导致绑定接口失败

App *n*: Changed source IP from *p* to *q*.

应用*n*：修改源IP

App *n*: Changed source port from *m* to *n*.

应用*n*：修改源端口

App *n*: Changed app IP from *p* to *q*

应用*n*：修改前置机IP

App *n*: Changed app port from *m* to *n*.

应用*n*：修改前置机端口

App *n*: Changed hello interval from *m* to *n*.

应用*n*：修改Hello间隔时间

App *n*: Changed hello switch from *m* to *n*.

应用*n*：修改握手功能使能开关

App *n*: Changed sending caller-number switch from *m* to *n*.\"

应用*n*：修改主叫号码使能开关

App *n*:Changed mode to temporary.

应用*n*：修改连接方式为短连接

App *n*: Changed mode to permanent.

应用*n*：修改连接方式为长连接

App *n*:Changed TCP keepalive interval and number from (*m*, *n*) to (*m*, *n*).

应用*n*：修改保活报文发送的时间间隔和次数

App *n*: Changed app link-time from *p* to *q*.

应用*n*：修改连接请求超时时间

App *n*:Changed quiet time from *p* to *q*.

应用*n*：修改静默时间

App *n /* Terminal *n*: Changed description from *p* to *q*.

应用*n / *终端*n*：修改描述信息

App *n*:Changed backup app form *p* to *q*.

应用*n*：修改备份POS应用

App *n*: Changed TPDU-change-strategy source.

应用*n*：修改TPDU源地址

App *n*: Changed TPDU-change-strategy destination.

应用*n*：修改TPDU目的地址

App *n /* Terminal *n*: Created instance *m*.

应用*n / *终端*n*：创建实例*m*

App *n /* Terminal *n*: Deleted instance *m*.

应用*n / *终端*n*：删除实例*m*

App *n /* Terminal *n*: Reset instance *m*

应用*n / *终端*n*：重置实例*m*

App *n*: Reset the socket keepalive for instance *m*.

应用*n*：重置实例*m*保活socket

Terminal *n*: Accepted a new connecting request.

终端*n*：获取新的连接请求

App *n*: Connect to app.

应用*n*：连接到app

App *n /* Terminal *n*: Instance *m* received epollout event.

应用*n / *终端*n*：实例*m*收到epollout事件

App *n /* Terminal *n*: Instance *m* link error.

应用*n / *终端*n*：实例*m*收到epollup或epollerr事件

App *n /* Terminal *n*: Instance *m* received packet.

应用*n / *终端*n*：实例*m*报文

App *n /* Terminal *n*: Instance *m* sent packet.

应用*n / *终端*n*：实例*m*发送报文

App *n /* Terminal *n*: Instance link peer closed.

应用*n / *终端*n*：连接已关闭

App *n /* Terminal *n*: Received a completed packet, length=*m*.

应用*n / *终端*n*：接收到长度为*m*的完整报文

Failed to get terminal instance by handle(*n*).

通过handle(*n*)获取终端实例失败

App *n /* Terminal *n*: Interface *ifname*: event=*type*.

应用*n* / 终端*n*：接口名：事件。(其中*type*包括：insert、remove、up、down、delete、create、deactive)

App *n /* Terminal *n*:Interface *ifname* TTY event=*type*.

应用*n* / 终端*n*：收到接口(*ifname*)的tty事件。(其中*type*包括：ready、release)

Connected to TTYM.

连接到TTYM

App *n /* Terminal *n*: Registered interface *ifname* to with TTYM.

应用*n* / 终端*n*：向ttym注册接口(*ifname*)

App *n /* Terminal *n*: Unregistered interface *ifname* with TTYM.

应用*n* / 终端*n*：向ttym撤销注册接口(*ifname*)

App *n /* Terminal *n*: Got control TTY device for interface *ifname*.

应用*n* / 终端*n*：接口(*ifname)*获取tty设备控制权

App *n /* Terminal *n*: Released control over TTY device for interface *ifname*.

应用*n* / 终端*n*：接口(*ifname)*放弃tty设备控制权

App *n /* Terminal *n*: Opened device *s*.

应用*n* / 终端*n*：打开设备(*s*)

Batch backup for configurations started.

批备数据开始

Batch backup for configurations ended.

批备数据结束

Batched up app *n* configuration.

批备app *n*配置

Batched up terminal *n* configuration.

批备terminal *n*配置

Batched up terminal *n* description.

批备terminal *n*描述信息

Batched up global FCM configuration.

批备FCM全局配置

Batched up FCM negotiation and threshold configuration for interface *ifname*.

为接口(*ifname*)批备FCM协商和临界值配置

Batched up map (DST=*a*, SRC=*b*) configuration.

批备map配置，目的地址为*a*，源地址为*b*

Batched up trap configuration.

批备trap配置

Batched up caller-IP *n* configuration.

批备caller-IP *n*配置

Batched up caller-id *s* configuration.

批备caller-id *s*配置

Batched up posa server configuration.

批备posa服务配置

Receiving batch backup configurations finished.

批备完成

Sent batch backup request.

发送批备请求

Received LIPC message type=*a*, code=*b*, sequence=*c*, length=*d*.

收到LIPC消息，类型：*a*，操作：*b*，序列：*c*，长度：*d*

LIPC connected.

LIPC已连接

LIPC disconnected.

LIPC断开

Terminal *n*: Caller number was *s*.

终端*n*：主叫号码是*s*

App *n /* Terminal *n*: Waited to send packet.

应用*n* / 终端*n*：由于当前发送缓存区已存在数据，所以延迟发送当前报文

Kernel received FCM event: *n*, for interface *ifname*

内核收到fcm接口*ifname*的事件*n*

Kernel published the event to POSA daemon.

内核把事件传到posa后台进程

Kernel got interface *ifname* statistics and returned *m*

内核获取接口*ifname*的统计，返回*m*

Kernel hung up the interface *ifname* POS and returned *m*

内核挂起接口*ifname*下的pos机，返回*m*

Kernel got the interface *ifname* s POS calling number and returned *m*

内核获取接口*ifname*下的pos机，主机号码返回值*m*

Kernel set the interface *ifname* para (cmd=n value=d) and returned *m*

内核设置接口*ifname*值参数（命令字：n，值：d），返回*m*

Kernel set the FCM timer parameter (answer-time=a, trade-time=b) and returned *m*

内核设置fcm定时器参数，返回*m*

Added TPDU-replace entry: terminal*=**n*, destination=*0xaaaa* to , des-code=*0xbbbb*.

添加TPDU-replace配置：将终端为*n*且目的地址为*0xaaaa*的报文的目的地址替换为*0xbbbb*

Updated TPDU-replace entry (terminal=* n*, destination=*0xaaaa*) changed des-code from *0xbbbb* to *0xcccc*.

修改TPDU-replace配置：将终端为*n*且目的地址为*0xaaaa*的对应的替换目的地址由*0xbbbb*修改为*0xcccc*

Deleted TPDU-replace enty: terminal=*n*, destination=*0xaaaa*.

删除TPDU-replace配置：将终端为*n*且目的地址为0xaaaa的替换配置删除

Terminal *n*: Replaced des-code from *0xaaaa* to *0xbbbb*.

终端*n*：将报文的目的地址由*0xaaaa*替换为*0xbbbb*

Terminal *n*: Failed to match TPDU-replace table with destination *0xaaaa*.

终端*n*：由于找不到对应的替换策略而替换地址失败

Batched up TPDU-replace configuration: terminal=*n*, destination=*0xaaaa*, des-code=*0xbbbb*.

批备posa TPDU-replace配置

Started to close allTCP terminal listen ports.

开始关闭所有TCP终端的监听端口

Started to open all TCP terminal listen ports.

开始打开所有TCP终端的监听端口

Batched up posa auto-stop service configuration.

批备posa自动关闭终端服务的配置

App *n*: Changed auto-connect interval from *a* to *b* minutes.

应用*n*：将自动连接时长由*a*分钟修改为*b*分钟

App *n*: Enabled auto-connect.

应用*n*：开启自动连接功能

App *n*: Disabled auto-connect.

应用*n*：关闭自动连接功能

App *n*: Started auto-connect to server(IP: *x.x.x.x*, port: *a*).

应用*n*：开始自动向前置机（IP为*x.x.x.x*，端口为*a*）发起连接

Terminal *n*:Changed idle time from *a* to* b* minute(s).

终端*n*：将空闲时间由*a*分钟修改为*b*分钟

Terminal *n*:Instance *m* cleared idle-time count.

终端*n*：实例*m*将空闲计数器重置为0

Terminal *n*: Instance *m* has successfully got trade number *o*.

终端*n*：实例*m*成功获取到交易号*o*

Terminal *n*: Instance *m* released trade number *o*.

终端*n*：实例*m*释放交易号*o*

Changed the concurrent trades limit for each TCP connection from *m* to *n*.

将每条TCP连接的并发交易数上限值从*m*修改为*n*

Changed the trade timeout from *m* to *n* seconds.

将每笔交易的超时时间从*m*秒修改为*n*秒

Changed the TCP terminal concurrent connections threshold from *m* to *n*.

将TCP接入方式的终端的并发连接数阈值从*m*修改为*n*

Changed the FCM terminal concurrent connections threshold from *m* to *n*.

将FCM接入方式的终端的并发连接数阈值从*m*修改为*n*

Batched up the TCP terminal concurrent connections threshold configuration.

备份TCP接入方式的终端并发连接数阈值的配置到接口板

Batched up the FCM terminal concurrent connections threshold configuration.

备份FCM接入方式终端并发连接数阈值的配置到接口板

Batched up the concurrent trades limit for each TCP connection configuration.

备份TCP连接并发交易数上限的配置到接口板

Batched up the trade timeout configuration.

备份交易超时时间的配置到接口板

Backed up the TCP connection maximum number.

备份TCP终端的连接数最大值

Enabled a license.

使能一个License

Disabled a license.

去使能一个License

【举例】

\#打开事件调试信息开关，删除POS应用模板2。

\<System\> debugging posa event

System\*Aug  7 17:40:21:819 2012 System POSA/7/EVENT: -MDC=1; Recv LIPC message type:

SET, code:DELAPP, sequence:0, length:2.

\*Aug  7 17:40:21:819 2012 System POSA/7/EVENT: -MDC=1; App 2:Disable template.

\*Aug  7 17:40:21:819 2012 System POSA/7/EVENT: -MDC=1; App 2:Delete template.

*// 删除应用模板2*

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa timer**

------------------------------------------------------------------------

【命令】

**[debugging posa timer**[ [ **terminal** *terminal-id* \| **app** *app-id* ]]]

**[undo debugging posa timer**[ [ **terminal** *terminal-id* \| **app** *app-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[terminal*** terminal-id*]：终端模板ID，取值范围为1～255。

**[app*** app-id*]：应用模板ID，取值范围为1～1024。

【描述】

**[debugging posa timer**]命令用来打开定时器操作调试开关。**undo debugging posa timer**命令用来关闭定时器调试开关。

缺省情况下，定时器调试开关处于关闭状态。

表1-2 debugging posa timer命令输出信息描述表

字段

描述

App *n /* Terminal *n*: Failed to create *type* timer, key=*m*.

应用*n* / 终端*n*：创建*type*类型定时器失败。*type*和*key*取值及对应关系如下：

*[type*]：*key*

app connecting：应用实例

quiet：AppID

hello period：AppID

hello probe：AppID

app flush statistics：无效值

terminal flush statistics：无效值

caller-ID flush statistics：无效值

caller-IP flush statistics：无效值

terminal idle：终端实例

lipc connecting：无效值

resend：应用实例或终端实例

TTYM connect：无效值

app wait AM-CID response：应用实例

app auto-connect：应用模板

trade：交易号

App *n /* Terminal *n*:Created *type* timer, key=*m*.

应用*n* / 终端*n*：创建*type*类型定时器.( *type*类型及*key*取值同上)

App *n /* Terminal *n*: Triggered *type* timer, key=*m*.

应用*n* / 终端*n*：触发*type*类型定时器.( *type*类型及*key*取值同上)

App *n /* Terminal *n*: Deleted *type* timer, key=*m*.

应用*n* / 终端*n*：删除*ype*类型定时器.( *type*类型及*key*取值同上)

App *n /* Terminal *n*: Reset *type* timer interval from *p* to *q*, key=*m*.

应用*n* / 终端*n*：刷新t*ype*类型定时器，修改时间间隔。(*type*类型及*key*取值同上)

【举例】

\# 打开定时器调试信息开关，存在tcp类型的POS应用模板2，在应用视图下配置静默定时器时间。

\<System\> debugging posa timer

\*Aug  7 17:54:40:786 2012 System POSA/7/TIMER: -MDC=1; App 2:Trigger hello period t

imer, key:2.

*// 静默定时器时间已更改，hello定时器已触发*

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa error**

------------------------------------------------------------------------

【命令】

**[debugging posa error**[ [ **terminal** *terminal-id* \| **app** *app-id* ]]]

**[undo debugging posa error**[ [ **terminal** *terminal-id* \| **app** *app-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[terminal*** terminal-id*]：终端模板ID，取值范围为1～255。

**[app*** app-id*]：应用模板ID，取值范围为1～1024。

【描述】

**[debugging posa error**]命令用来打开POS接入错误调试开关。**undo debugging posa error**命令用来关闭POS接入错误调试开关。

缺省情况下，POS接入错误调试开关处于关闭状态。

表1-3 debugging posa error命令输出信息描述表

字段

描述

App *n*:Failed to trigger hello issue, A previous issue exist.

应用*n*：Hello已存在

Maximum number of maps has been reached.

Map表项已达到最大值

Failed to match map.

匹配map表失败

Failed to set data(CMD:*n*) to kernel.

向内核设置数据失败

App *n /* Terminal *n*:AM-CID response packet total length was wrong.

应用*n / *终端*n*：应答AM-CID报文总长度错误

App *n /* Terminal *n*:AM-CID response packet data length was wrong.

应用*n / *终端*n*：应答AM-CID报文数据长度错误

App *n /* Terminal *n*: AM-CID response packet data length was wrong.

应用*n / *终端*n*：应答AM-CID报文数据代码错误

App *n /* Terminal *n*: AM-CID response packet caller number length was wrong.

应用*n / *终端*n*：应答AM-CID报文数据主叫号码长度错误

App *n /* Terminal *n*: AM-CID response packet caller number was wrong.

应用*n / *终端*n*：应答AM-CID报文数据主叫号码错误

App *n /* Terminal *n*: AM-CID response packet CRC was wrong.

应用*n / *终端*n*：应答AM-CID报文数据CRC校验错误

App *n /* Terminal *n*: Maximum number of instances has been reached.

应用*n / *终端*n*：实例数达到最大值

Terminal *n*: Maximum number of TCP connections has been reached.

终端*n*：TCP终端的连接数达到最大值

Terminal *n*: Failed to accept socket error code=*m*.

终端*n*：accept   socket连接失败，错误码是*m*

Terminal *n*: Failed to listen socket error code=*m*

终端*n*：监听socket连接失败，错误码是*m*

App n / Terminal n: Failed to set socket option.

应用n / 终端n：设置socket选项失败

App *n*: Failed to get app instance for terminal.

应用*n*：为终端获取应用实例失败

App *n /* Terminal *n*: Failed to bind socket, error code=*m*.

应用*n / *终端*n*：绑定socket失败，错误码是*m*

App *n*: Failed to connect to app, error code=*m*.

应用*n / *终端*n*：连接到app失败，错误码是*m*

App *n /* Terminal *n*: Failed to send packet, error code=*m*

应用*n / *终端*n*：发送报文失败，错误码是*m*

App *n /* Terminal *n*: Received incompleted packet received length=*a*,expected length=*b*.

应用*n / *终端*n*：接受了长度为*a*不完整的报文，实际长度应为*b*

Terminal *n*: Failed to send to peer for *m* times.

*[m*]次重传失败

App *n*: Failed to distribute app packet.

分发app报文失败

App *n /* Terminal *n*: Invalid packet length(*m*).

应用*n / *终端*n*：报文长度(*m*)错误

App *n /* Terminal *n*: NO-HEAD-FCM packet checking failed. Invalid packet length (*m*).

应用*n / *终端*n*：检查无头FCM报文时报文长度(*m*)错误

App *n /* Terminal *n*: FCM packet checking failed. Invalid packet length (*m*).

应用*n / *终端*n*：检查FCM报文时报文长度(*m*)错误

App *n /* Terminal *n*: Flow packet checking failed. Invalid STX*(m)*.

应用*n / *终端*n*：检查异步报文时其特定域STX*(m)*错误

App *n /* Terminal *n*: Flow packet checking failed. Invalid TPDU-ID*(m)*.

应用*n / *终端*n*：检查异步报文时其TPDU ID*(m)*错误

App *n /* Terminal *n*: Flow packet checking failed. Invalid ETX(*m*).

应用*n / *终端*n*：检查异步报文时其特定域ETX*(m)*错误

App *n /* Terminal *n*: Flow packet checking failed. Invalid CRC(*p)*, should be *q*.

应用*n / *终端*n*：检查异步报文时其特定域CRC*(p)*错误，正确的CRC是(*q)*

Failed to get private data for interface *ifname*.

获取接口（*ifname*）私有数据块失败

App *n /* Terminal *n*: Failed to set non-block mode, error code=*m*.

应用*n / *终端*n*：设置连接为非阻塞失败，错误码为*m*

TTYM was lost.

断开与TTYM连接

Terminal *n*: Failed to enable nontcp terminal because instance has already existed

终端*n*：由于实例已经存在，导致使能非tcp类型终端失败

App *n /* Terminal *n*: Failed to register interface *ifname* to TTYM.

应用*n / *终端*n*：向ttym注册接口(*ifname*)失败

App *n /* Terminal *n*: Failed to unregister interface *ifname* toTTYM

应用*n / *终端*n*：撤销向ttym注册接口(*ifname*)失败

App *n /* Terminal *n*: Failed to put TTY device for interface *ifname*.

应用*n / *终端*n*：接口(*ifname)*放弃tty设备控制权失败

App *n /* Terminal *n*: Failed to read data from interface or socket.

应用*n / *终端*n*：从接口或socket中读取数据失败

Failed to connect to TTYM

连接到TTYM失败

App *n /* Terminal *n*:Failed to get TTY device for interface *ifname*.

应用*n / *终端*n*：接口(*ifname)*获取tty设备控制权失败

App *n /* Terminal *n*: Failed to open device *s* error code=*m*.

应用*n / *终端*n*：打开设备(*s*)失败，错误码为*m*

App *n*: Failed to create more instance. Source port is set.

应用*n*：由于配置了源端口的模板只允许一个实例，导致创建其他实例失败

Failed to add fd:*n* to epoll.

添加fd(*n*)到epoll失败

App *n /* Terminal *n*: Failed to get *s* attribute, error code=*m*.

应用*n / *终端*n*：获取tty设备(*s)*失败，错误码为*m*

App *n /* Terminal *n*: Failed to set *s* attribute, error code=*m*.

应用*n / *终端*n*：设置tty设备(*s)*失败，错误码为*m*

App *n /* Terminal *n*: Failed to get instance for tty event.

应用*n / *终端*n*：处理tty事件获取实例失败

App *n /* Terminal *n*: Failed to get fd for tty event.

应用*n / *终端*n*：处理tty事件获取句柄失败

App *n /* Terminal *n*: Failed to recevie data due to buffer overflow.

应用*n / *终端*n*：由于接受缓冲满，无法读取新的报文

App *n /* Terminal *n*: Failed to send data due to buffer overflow.

应用*n / *终端*n*：由于发送缓存满，无法发送新的报文

Failed to send Lipc message.

发送LIPC消息失败

Recevied invalid Lipc message.

收到无效的LIPC消息

App *n* : Socket (fd: *n*) received epoll event,event=*a*, error code=*b*.

应用*n*：socket *n* 接收到epoll事件*a*，错误码为*b*

App *n*: Instance *m* keep was down.

应用*n*：实例*m*报文保活失败

Terminal *n*: Number of concurrent trades for instance *m* exceeded the limit *o*.

终端*n*：实例*m*的并发交易数超过上限值*o*

Failed to allocate trade resources.

分配交易资源失败

Terminal *n*: Instance *m* failed to get a trade number due to trade resource allocation error.

终端*n*：实例*m*获取交易号失败，原因是交易资源申请失败

Terminal *n*: Instance *m* failed to get a trade number because no idle trade number was left.

终端*n*：实例*m*获取交易号失败，原因是无空闲交易号

Terminal *n*: Instance *m* failed to create timer for trade *o*.

终端*n*：实例*m*为交易*o*创建定时器失败

Trade number *o* has already been released.

交易号*o*已经被释放

Terminal *n*: FCM packet checking failed. Invalid TPDU-ID*(m)*.

终端*n*：检查FCM报文时其TPDU ID*(m)*错误

【举例】

\# 打开错误调试信息开关，在没有配置匹配的map表情况下，发起一次交易。

\<System\> debugging posa error

\*Aug  7 18:09:38:603 2012 System POSA/7/ERROR: -MDC=1; Failed to match map.

*// 显示匹配map表失败*

**POS终端接入 \-- POS终端接入调试命令 \-- debugging posa packet**

------------------------------------------------------------------------

【命令】

**[debugging posa packet**[ [ **receive** \| **send**   **terminal** *terminal-id* \| **app** *app-id* ]]]

**[undo debugging posa packet**[ [ **receive** \| **send**   **terminal** *terminal-id* \| **app** *app-id* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：表示接收报文的调试信息开关。

**[send**]：表示发送报文的调试信息开关。

**[terminal*** terminal-id*]：终端ID，取值范围为1～255。

**[app*** app-id*]：应用ID，取值范围为1～1024。

【描述】

**[debugging posa packet**]命令用来打开POS接入报文调试开关，可以使用**receive**、**send**参数来控制打开特定方向的报文调试开关；使用**terminal**、**app**参数来控制打开某个终端模板或应用模板的报文调试开关。

**[undo debugging posa packet**]命令用来关闭POS接入报文调试开关，可以使用**receive**、**send**、**terminal**、**app**参数来控制关闭某个终端或应用模板特定方向的报文调试开关。

POS报文特定域：STX 、PktLen(报文包长)、ID（传输协议数据单元ID，即TPDU  ID）、DST（TPDU 目的地址）、SRC（TPDU 源地址）、EXT、CRC（校验和）。

当接收到的报文不完整时，无报文数据的域显示为0。当本次收到的报文数据大于32字节时，只显示前32字节的报文内容。

缺省情况下，POS接入报文调试开关处于关闭状态。

表1-4 debugging posa packet命令输出信息描述表

字段

描述

Received *m* bytes from flow terminal *n*.

STX PktLen(a) ID(b) DST(c) SRC(d) ETX CRC(e)

Total length:x offset:y, partial data as follows:

·从flow类型的终端*n*收到*m*字节

·STX PktLen*(a)* ID(*b*) DST(*c*) SRC(*d*) ETX *CRC*(*e*)

·报文长度：*x*偏移量：*y*，部分报文内容如下：

Received *m* bytes from tcp terminal *n*.

PktLen(a) ID(b) DST(c) SRC(d)

Total length:x, offset: y, partial data as follows:

·从tcp类型的终端*n*收到*m*字节

·PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*)

·报文长度：*x*偏移量：*y*，部分报文内容如下：

Received *m* bytes from fcm terminal *n*.

ID(a) DST(b) SRC(c)

Total length:x, offset: y, partial data as follows:

·从fcm类型的终端*n*收到*m*字节

·ID(*a*) DST(*b*) SRC(*c*)

·报文长度：*x*偏移量：*y*，部分报文内容如下：

Received *m* bytes from fcm terminal *n*.

No head

Total length:x, offset: y, partial data as follows:

·从fcm类型的终端*n*收到*m*字节

·无头报文

·报文长度：*x*偏移量：*y*，部分报文内容如下：

Received *m* bytes from flow terminal *n*.

Transparent packet

Total length:x, offset: y, partial data as follows:

·从flow类型的终端*n*收到*m*字节

·透传报文

·报文长度：*x*偏移量：*y*，部分报文内容如下：

Received *m* bytes from fcm terminal *n*.

Transparent packet

Total length:x, offset: y, partial data as follows:

·从fcm类型的终端*n*收到*m*字节

·透传报文

·报文长度：*x*偏移量：*y*，部分报文内容如下：

Received *m* bytes from flow application *n*.

STX PktLen(a) ID(b) DST(c) SRC(d) ETX CRC(e)

Total length:x, offset: y

·从flow类型的应用*n*收到*m*字节

·STX PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*) ETX CRC(*e*)

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Received *m* bytes from tcp application *n*.

PktLen(a) ID(b) DST(c) SRC(d)

Total length:x, offset: y, partial data as follows:

·从tcp类型的应用n收到m字节

·PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*)

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Received *m* bytes from tcp application *n*.

Transparent packet

Total length:x, offset: y, partial data as follows:

·从tcp类型的应用*n*收到*m*字节

·透传报文

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Sent *m* bytes to flow terminal *n*.

STX PktLen(a) ID(b) DST(c) SRC(d) ETX CRC(e)

Total length:x, offset: y, partial data as follows:

·发送*m*字节到flow类型的终端*n*

·STX PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*) ETX CRC(*e*)

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Sent *m* bytes to tcp terminal *n*.

PktLen(a) ID(b) DST(c) SRC(d)

Total length:x, offset: y, partial data as follows:

·发送*m*字节到tcp类型的终端*n*

·PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*)

·报文长度：*x*偏移量：*y*，部分报文内容如下：

Sent *m* bytes to fcm terminal *n*.

ID(a) DST(b) SRC(c)

Total length:x, offset: y, partial data as follows:

·发送*m*字节到fcm类型的终端*n*

·ID(*a*) DST(*b*) SRC(*c*)

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Sent *m* bytes to fcm terminal *n*.

No head

Total length:x, offset: y, partial data as follows:

·发送*m*字节到fcm类型的终端*n*

·无头报文

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Sent *m* bytes to flow terminal *n*.

Transparent packet

Total length:x, offset: y, partial data as follows:

·发送*m*字节到flow类型的终端*n*

·透传报文

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Sent *m* bytes to fcm terminal *n*.

Transparent packet

Total length:x, offset: y, partial data as follows:

·发送*m*字节到fcm类型的终端*n*

·透传报文

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Sent *m* bytes to flow application *n*.

STX PktLen(a) ID(b) DST(c) SRC(d) ETX CRC(e)

Total length:x, offset: y, partial data as follows:

·发送*m*字节到flow类型的应用*n*

·STX PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*) ETX CRC(*e*)

·报文长度：*x *偏移量：*y*，部分报文内容如下：

Sent *m* bytes to tcp application *n*.

PktLen(a) ID(b) DST(c) SRC(d)

Total length:x, offset: y, partial data as follows:

·发送*m*字节到tcp类型的应用*n*

·PktLen(*a*) ID(*b*) DST(*c*) SRC(*d*)

·报文长度：x 偏移量：y，部分报文内容如下：

Sent *m* bytes to tcp application *n*.

Transparent packet

Total length:x, offset: y, partial data as follows:

·发送*m*字节到tcp类型的应用*n*

·透传报文

·报文长度：*x *偏移量：*y*，部分报文内容如下：

【举例】

\# 打开接受报文调试开关，发送一次完整报文。

\<System\>debugging posa packet receive

System\*Aug  7 18:15:58:136 2012 System POSA/7/PKTRECEIVE: -MDC=1; Received 9 bytes f

rom tcp terminal 1.

PktLen(0x0007) ID(0x60) DST(0x1111) SRC(0x2222)

Total length: 9 Offset: 0, partial data as follows:

0x000:  00 07 60 11 11 22 22 aa bb

*// 收到9字节的报文，报文的TPDU ID为0x60，目的地址为0x2222，源地址为0x1111，报文长度为9字节，偏移量为0*
