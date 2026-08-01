<!-- CMD-INDEX
  debuggging mac-authentication       | 用户视图             | L5
-->

**MAC地址认证 \-- MAC地址认证调试命令 \-- debuggging mac-authentication**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging mac-authentication **[{ **all** \| **error** \| **event** }]]

**[undo debugging mac-authentication **[{ **all** \| **error** \| **event** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging mac-authentication **[{ **all** \| **error** \| **event** } [ **slot** *slot-number* ]]]

**[undo debugging mac-authentication **[{ **all** \| **error** \| **event** } [ **slot** *slot-number* ]]]

分布式设备－IRF模式：

**[debugging mac-authentication **[{ **all** \| **error** \| **event** } ]] **chassis** *chassis-number* **slot** *slot-number*

**[undo debugging mac-authentication **[{ **all** \| **error** \| **event** } ]] **chassis** *chassis-number* **slot** *slot-number*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[slot ***slot-mumber*]：表示指定单板的调试信息开关，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-mumber*]：表示指定成员设备的调试信息开关，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-mumber*]：表示指定成员设备/PEX的调试信息开关，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：表示成员设备上指定单板的调试信息开关。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：表示指定单板的调试信息开关。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【描述】

**[debug mac-authentication**]命令用来打开MAC地址认证调试信息开关。**undo debug mac-authentication**命令用来关闭MAC地址认证调试信息开关。

缺省情况下，MAC地址认证调试信息开关处于关闭状态。

表1-1 debugging mac-authentication error命令输出信息描述表

字段

描述

Failed to find user by *mac* and *interface-type interface-num* when receiving authenticate response.

收到认证回应消息时，根据MAC地址*mac*和接口名*interface-type interface-num*无法找到对应的用户

Failed to find user by *mac* and *interface-type interface-num* when receiving authorization response.

收到授权回应消息时，根据MAC地址*mac*和接口名*interface-type interface-num*无法找到对应的用户

Failed to find user by *mac* and *interface-type interface-num* when receiving accounting response.

收到计费回应消息时，根据MAC地址*mac*和接口名*interface-type interface-num*无法找到对应的用户

Failed to find user by *mac* and *interface-type interface-num* when receiving session control cut request.

收到包含Cut命令字的Session Control消息时，根据MAC地址*mac*和接口名*interface-type interface-num*无法找到对应的用户

Failed to set the interface driver.

设置接口的驱动失败

Failed to add socket to epoll.

socket加入epoll失败

Failed to create socket.

创建socket失败

Failed to connect to master.

连接主控板失败

Failed to write message to maca que. *msgtype*

写消息到maca队列失败，*msgtype*表示消息类型

Failed to accept connect.

接收连接失败

Failed to create global socket.

创建全局socket失败

Failed to process message for the message type is invalid.

消息处理失败因为消息类型非法

Failed to add socket to lpu connection table.

将socket加入长连接链表失败

Failed to accept connection with the global known port.

在全局知名端口接收连接失败

Failed to find online user\'s mac and add mac to driver again.

在线用户的MAC地址不存在，向驱动重新添加该MAC

Invalid queue message received.

接收到的队列消息不合法

Failed to create user for the number of users reached the maximum.

用户数已达最大值，创建用户失败

Failed to allocate memory for user.

为用户申请内存失败

Failed to start acct-update period timer when receiving acct-start response, terminate user session.

当收到计费开始响应消息时，打开计费更新周期定时器失败，结束用户会话

Failed to allocate memory for pam handle.

为pam handle分配内存失败

表1-2 debugging mac-authentication event命令输出信息描述表

字段

描述

Received EPOLLERR or EPOLLHUP event.

收到EPOLLERR或EPOLLHUP事件

Reconnect timer timeout, reconnecting to mpu.

重连定时器超时，向mpu重新发起连接

Successfully connected to master, closed reconnect timer.

和主控板连接成功，关闭重连定时器

Processing If_Delete event:

处理接口删除事件

Processing If_Deactive event:

处理接口去激活事件

Processing If_Active event:

处理接口激活事件

Processing If_Down event:

处理接口Down事件

Processing HA UPGRADE event.

处理HA升级事件

Processing HA DEGRADE event.

处理HA降级事件

Processing the event of IFEVENT.

正在处理接口事件

User will log off for failing to change state.

用户因为状态变迁失败而下线

*mac*:VLAN*vlan*:*interface-type interface-num* User received stop accounting response, RespCode=*RespCode.*

用户（MAC地址为*mac*，所属VLAN ID为*vlan*，接入端口为*interface-type interface-num*）收到停止计费回应消息，响应码为*RespCode*

Processing new_mac event

处理new-mac事件

Notified PortSec of new_mac result

通知端口安全new-mac结果

*mac*:VLAN*vlan*:*interface-type interface-num* Processing unauthor event.

处理unauthor事件

Processing IfVlanDel event, interface Index is *index*, VLAN ID = *vlan-id*.

处理ifVlanDel事件，接口索引为*interface-type interface-num*，VLAN ID为*vlan-id*

Processing Auth_Fail_Proc notification

处理Auth_Fail_Proc 通知事件

Notified PortSec of Auth_Fail_Proc result

通知端口安全Auth_Fail_Proc结果

Added silent mac address

添加静默MAC地址

User server timer timeout and logged off

用户的服务器定时器超时，用户下线

User reauth timer timeout and was authenticated again

用户重认证定时器超时，重新认证

User state Initialize changed to Disconnect

用户状态从初始化转到断开连接

User state Disconnect changed to Authenticating

用户状态从断开连接转到开始认证

User state Authenticating changed to Authenticated

用户状态从开始认证转到认证成功

User state Authenticated changed to Initialize

用户状态从认证转到初始化

User was being authenticated with name *user-name* and password *string*

用户（名称为*user-name*，密码为*string*）进行认证

User started server timer, length *time*s

用户开启服务定时器，时长是*time*秒

User closed server timer

用户关闭服务定时器

User started reauth timer, length *time*s

用户开启重认证定时器，时长是*time*秒

User closed reauth timer

用户关闭重认证定时器

User closed session timer

用户关闭会话定时器

User session timer timeout and logged off

用户的会话定时器超时，用户下线

User started session timer, length *time*s

用户开启会话定时器，时长是*time*秒

The times of no-response accounting-update reached the maximum

无响应计费更新时间达到最大值

AAA processed accounting-update request and returned processing

AAA处理计费更新请求并返回结果

AAA processed accounting-update request and returned success

AAA处理计费更新请求并返回成功

AAA processed accounting-update request and returned fail

AAA处理计费更新请求并返回失败

User started update-accounting timer, length *time*s

用户开启更新计费定时器，时长是*time*秒

User closed update-accounting timer

用户关闭更新计费定时器

User closed offline-detect timer

用户关闭下线检测定时器

User mac not hitted and user logged off

没找到用户对应的MAC，用户下线

User started offline-detect timer, length *time*s

用户开启下线检测定时器，时长是*time*秒

AAA processed accounting-stop request and returned processing

AAA处理计费停止请求并返回正在处理

AAA processed accounting-stop request and returned success

AAA处理计费停止请求并返回成功

AAA processed authentication request and returned processing

AAA处理认证请求并返回正在处理

AAA processed authentication request and returned success

AAA处理认证请求并返回成功

AAA processed authentication request and returned fail

AAA处理认证请求并返回失败

AAA processed authentication request and returned error

AAA处理认证请求并返回错误

AAA processed authorization request and returned processing

AAA处理授权请求并返回正在处理

AAA processed authorization request and returned success

AAA处理授权请求并返回成功

AAA processed authorization request and returned failed

AAA处理授权请求并返回失败

User was deleted

用户被删除

A user was logging off. A accounting-start request for the new user with the same name will be send after the current user logged off.

有用户正在下线，此时如果有相同用户名的用户上线，则设备发为其发送的计费开始请求将在当前用户成功下线后发送

User received authentication response,

用户收到认证回应

User received authorization response

用户收到授权回应

User received start accounting response

用户收到计费开始回应

User received update accounting response

用户收到计费更新回应

*mac*:VLAN*vlanid*:*interface-type interface-num* Auth-delay timer time out.

用户认证延迟定时器超时

*mac*:VLAN*vlanid*:*interface-type interface-num* Succeeded to add User to critical vlan *vlan-id*.

用户成功被添加到critical VLAN中

*mac*:VLAN*vlanid*:*interface-type interface-num* Succeeded to add User to guest vlan *vlan-id*.

用户成功被添加到guest VLAN中

*mac*:VLAN*vlanid*:*interface-type interface-num* Delete User from critical vlan *vlan-id*.

用户从critical VLAN中退出

*mac*:VLAN*vlanid*:*interface-type interface-num* Delete User from guest vlan *vlan-id*.

用户从guest VLAN中退出

Authorization ACL number is *acl-number*.

授权ACL编号是*acl-number*

Authorization VLAN ID is *vlan-id*.

授权VLAN ID是*vlan-id*

Processing MAC-authentication delay.

处理用户MAC认证延迟

【举例】

\# 在一台启动了MAC地址认证功能的设备上，打开MAC地址认证的所有调试功能，有用户上线时，将输出如下调试信息。

\<Sysname\> debugging mac-authentication all

\*Jan  1 14:48:13:347 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 Processing new_mac event.{.TerminalDisplayChar}

*// 处理new_mac事件，用户的MAC地址为1cbd-b9e3-c434，用户所在的VLAN ID为2，用户接入的接口名为GE1/0/1*

\*Jan  1 14:48:13:349 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User state changed from Initialize to Authenticating.

*// 用户状态从初始化变更为正在认证*

\*Jan  1 14:48:13:350 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User was being authenticated with name yangliping and

 password \*\*\*.

*// 用户使用用户名"yangliping"和密码\*\*\*\*正在进行认证*

\*Jan  1 14:48:13:351 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User started server timer, length=100(s).

*// 开启用户服务器超时定时器，时长为100秒*

\*Jan  1 14:48:13:354 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 AAA processed authentication request and returned processing.{.TerminalDisplayChar}

*[// AAA*]*处理用户的认证请求，返回处理结果为：正在处理*

\*Jan  1 14:48:13:355 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 Notified PortSec of new new_mac result: 1.

*// 通知端口安全new-mac结果为1*

\*Jan  1 14:48:14:400 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User received authentication response, RespCode=0.

*// 用户收到认证回应消息，响应码为1*

\*Jan  1 14:48:14:401 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User state changed from Authenticating to Authenticated.

*// 用户状态从认证中变更为已通过认证*

\*Jan  1 14:48:14:402 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User closed server timer.

*// 关闭用户服务器超时定时器*

\*Jan  1 14:48:14:404 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 AAA processed authorization request and returned success.

*[// AAA*]*处理用户授权请求，返回处理结果为：成功*

\*Jan  1 14:48:14:405 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User started session timer, length=86400(s)

*// 开启用户会话定时器，时长为86400秒*

\*Jan  1 14:48:14:409 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User started offline-detect timer, length=300(s).

*// 开启用户在线探测定时器，时长为300秒*

\*Jan  1 14:48:14:414 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User started update-accounting timer, length=600(s).

*// 开启用户实时计费定时器，时长为600秒*

\# 该用户下线时，将输出如下调试信息：

\*Jan  1 14:50:40:800 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User state Authenticated changed to Disconnect.

*// 用户状态从已认证变更为下线*

\*Jan  1 14:50:40:801 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User closed server timer.

*// 关闭用户服务器超时定时器*

\*Jan  1 14:50:40:802 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User closed update-accounting timer.

*// 关闭用户实时计费定时器*

\*Jan  1 14:50:40:803 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User closed session timer.

*// 关闭用户会话定时器*

\*Jan  1 14:50:40:804 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User closed offline-detect timer.

*// 关闭用户在线探测定时器*

\*Jan  1 14:50:40:808 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 AAA processed accounting-stop request and returned success.

*[// AAA*]*处理用户的计费停止请求，返回处理结果为：成功*

\*Jan  1 14:50:40:809 2011 Sysname MACA/7/EVENT:

1cbd-b9e3-c434:VLAN2:GE1/0/1 User was deleted.

*// 用户被删除*
