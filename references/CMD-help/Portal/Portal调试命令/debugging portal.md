<!-- CMD-INDEX
  debugging portal                    | 用户视图             | L6
  debugging portal interface          | 用户视图             | L1156
-->

**Portal \-- Portal调试命令 \-- debugging portal**

------------------------------------------------------------------------

【命令】

**[debugging portal**[ { **all** \| **error** \| **event** \| **fsm** }]]

**[undo debugging portal **[{ **all** \| **error** \| **event** \| **fsm** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有Portal调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[fsm**]：表示状态机调试信息开关。

【描述】

**[debugging portal**]命令用来打开Portal调试信息开关。**undo debugging portal**命令用来关闭Portal调试信息开关。

缺省情况下，Portal调试信息开关处于关闭状态。

表1-1 debugging portal error命令输出信息描述表

字段

描述

Failed to create the detection timer for portal server *server-name*.

创建Portal服务器探测定时器失败，Portal服务器名称为*server-name*

User (IP:*user-ip*) will log off because of no IP address assigned by the DHCP server.

由于未能成功被DHCP服务器分配IP地址，用户将被强制下线，用户IP地址为*user-ip*

Portal server didn\'t confirm the new IP. User will logoff.

Portal服务器在指定时间内没有确认更新的用户IP地址，该用户将被强制下线

Failed to start the timer for waiting for a new IP.

开启等待更新IP地址定时器失败

Failed to open the timer for confirming new IP.

开启确认新IP地址定时器失败

Failed to open the timer for waiting for ACK_NTF_LOGOUT.

开启等待ACK_NTF_LOGOUT报文定时器失败

Failed to send user-rule result.

向主控板发送添加用户规则的结果失败

Failed to send user traffic info.

向主控板发送用户流量信息失败

Failed to send mesh messages to all cards.

向所有板发送Mesh消息失败

Failed to send mesh messages to LPU.

向接口板发送Mesh消息失败

Failed to send mesh messages to MPUs.

向主控板发送Mesh消息失败

Failed to look up FIB info.

查找快转信息失败

Packet validity check failed because packet length and version did not match.

报文长度和版本均不匹配，报文合法性检查失败

Packet validity check failed due to invalid authenticator.

authenticator字段非法，报文合法性检查失败

Packet validity check failed due to failure of getting user access interface by user IP.

无法通过用户IP地址找到用户接入的接口，报文合法性检查失败

Unknown source of packet.

报文源未知

Failed to receive ICMP packet.

无法收到ICMP报文

Failed to open ICMP socket.

无法打开ICMP的套接字

Failed to send ICMP6 packet.

发送ICMPv6的报文失败

Failed to get ARP refresh time.

获取ARP更新时间失败

Failed to send ARP request.

发送ARP请求失败

Failed to get ND refresh time.

获取ND更新时间失败

Failed to find user while receiving accounting-update response.

收到计费更新回应时查找用户信息失败

Failed to create user because the user count  reached the upper limit.

用户数量达到最大值，创建用户失败

Failed to create user for failing to get the physical info.

获取用户物理信息失败，创建用户失败

Failed to create user due to memory application failure.

申请用户资源失败，导致创建用户失败

Failed to find user for ACK_NTF_LOGOUT.

找不到用户信息来发送ACK_NTF_LOGOUT报文

Failed to find user for AFF_NTF_USERIPCHAN.

找不到用户信息来发送AFF_NTF_USERIPCHAN报文

ACL *acl-number* doesn\'t exist or ACL type is not supported.

ACL *acl-number*不存在，或ACL的类型不支持

Failed to set pam items for authentication.

设置用于认证的pam items失败

Failed to find user by MAC (*mac-addr*).

根据MAC地址没有找到用户

Failed to create PAM handle.

创建PAM handle失败

Failed to create DHCP client: Not enough memory.

内存不足导致创建DHCP租约表项失败

Failed to create DHCP client.

创建DHCP租约表项失败

Failed to create DHCPv6 client: Not enough memory.

因为内存不足，创建DHCPv6表项失败

Failed to create DHCPv6 client.

创建DHCPv6表项失败

Failed to create the pre-auth user: Not enough memory.

内存不足，创建认证前用户失败

Failed to create the pre-auth user: The user already existed.

用户已存在，创建认证前用户失败

Failed to create the pre-auth user: All-zero MAC address.

用户MAC地址为全0，创建认证前用户失败

Failed to get author info for pre-auth user.

无法获取认证前域中的授权信息，创建认证前用户失败

表1-2 debugging portal event 命令输出信息描述表

字段

描述

Portal server *server-name* turned to *newstate* state.

Portal服务器*server-name*状态变化为*newstate*，*newstate*包括以下取值：

·UP：服务器可达

·DOWN：服务器不可达

Portal server *server-name* started detection.

Portal服务器*server-name*开启可达性探测功能

Portal server *server-name* refreshed detection timer.

Portal服务器*server-name*刷新探测定时器

Portal server *server-name* refreshed detection action because status is down when configuration was changed.

修改配置时，因为服务器*server-name*状态为down，所以服务器刷新了探测动作

Portal server *server-name* stopped detection.

Portal服务器*server-name*停止探测

Portal web-server *server-name* turned to *newstate* state.

Portal重定向服务器*server-name*状态变化为*newstate*，*newstate*包括以下取值：

·UP：服务器可达

·DOWN：服务器不可达

Portal web-server *server-name* started detection.

Portal重定向服务器*server-name*开启可达性探测功能

Portal web-server *server-name* refreshed detection timer.

Portal重定向服务器*server-name*刷新探测定时器

Portal web-server *server-name* refreshed detection action for status is down when changing configuration.

修改配置时，因为重定向服务器*server-name*状态为down，所以服务器刷新了探测动作

Portal web-server *server-name* detecting stopped.

Portal重定向服务器*server-name*停止探测

Stopped the auth_sm timer.

关闭认证状态机定时器

The number of failures of receiving ACK_NTF_LOGOUTpacket reached the upper limit.

等待ACK_NTF_LOGOUT报文的次数达到最大值

Started the auth_sm timer, timeout=*time sec*.

打开认证状态机的定时器，定时器的值为*time*秒

User(IP:*ip-addr*) was not online when DHCP relay client information is deleted.

当DHCP relay用户表项被删除时，对应的用户不在线

Received an event *event-id* from VLAN *vlan-id* on interface *interface-type interface-num*.

接收到VLAN事件，事件ID为*event-id*，VLAN ID为*vlan-id*，*,*接口索引为*ifindex*

Portal Web server host name *host-name*, port *port-num*.

根据URL地址获取到Portal Web server的主机名为* host-name*,、端口号为*port-num*

User-SM *ip-addr*

用户状态机用户IP地址

User-SM *ip-addr*: Received ICMP response successfully.

接收ICMP回应报文成功

User-SM *ip-addr*: Sent ICMP request successfully.

发送ICMP请求报文成功

User-SM *ip-addr*: Received ICMPv6 response successfully.

接收ICMPv6回应报文成功

User-SM *ip-addr*: Sent ICMPv6 request successfully.

发送ICMPv6请求报文成功

User-SM *ip-addr*: Sent ARP request successfully.

发送ARP请求报文成功

User-SM *ip-addr*: Sent ND request successfully.

发送ND请求报文成功

User-SM *ip-addr*: ARP entry refreshed.

ARP表项已刷新

User-SM *ip-addr*: ND entry refreshed.

ND表项已刷新

User-SM *ip-addr*: Number of detection attempts reached the upper limit.

探测次数到达最大值

User-SM *ip-addr*: Detection timer timed out and sent packet again.

探测定时器超时，重发探测报文

User-SM *ip-addr*: Started detect idle timer, timeout=*time* sec.

开启闲置探测定时器

User-SM *ip-addr*: Started detect waiting-response timer, timeout=*time* sec.

开启等待探测回应定时器

User-SM *ip-addr*: Stopped detect timer.

关闭探测定时器

User-SM *ip-addr*: Started  detect function.

开启探测功能

User-SM *ip-addr*: Started  idle-cut timer, timeout=*time* sec.

开启闲置切断定时器，定时器超时时长为*time*秒

User-SM *ip-addr*: Stopped idle-cut timer.

关闭闲置切断定时器

User-SM *ip-addr*: Idle-cut timer timed out and user will logoff.

闲置切断定时器超时，用户被强制下线

User-SM *ip-addr*: Started session-timeout timer, timeout= *time*(s).

打开会话超时定时器，定时器超时时长为*time*秒

User-SM *ip-addr*: Stopped session-timeout timer.

关闭会话超时定时器

User-SM *ip-addr*: Session timer timeout and user will logoff.

会话定时器超时，用户将被强制下线

User-SM *ip-addr*: Started user-sync timer, timeout=*time* sec.

开启用户同步定时器，定时器超时时长为*time*秒

User-SM *ip-addr*: Stopped user-sync timer.

关闭用户同步定时器

User-SM *ip-addr*: User-sync timer time out and user will logoff.

用户同步定时器超时，用户将被强制下线

User-SM *ip-addr*: Number of accounting-update attempts reached the upper limit.

计费更新的失败次数达到最大值

User-SM *ip-addr*: open accounting-update timer, timeout=*time*(s)

开启实时计费定时器，定时器超时时长为*time*秒

User-SM *ip-addr*: Close accounting-update timer.

关闭实时计费定时器

User-SM *ip-addr*: Number of accounting-update attempts without responses reached the upper limit.

实时计费更新报文无响应次数达到最大值

User-SM *ip-addr*: Notified User-Detect-SM to start detection.

通知detect-sm模块开启探测

User-SM *ip-addr*: Notify User-Detect-SM to stop detection.

通知detect-sm模块停止探测

User-SM *ip-addr*: Failed to find physical info for ack_info.

封装ACK_INFO报文时查找用户物理信息

User-SM *ip-addr*: Notified auth-sm to process the REQ_CHALLENGE packet.

通知认证状态机模块处理REQ_CHALLENGE报文

User-SM *ip-addr*: Notified auth-sm to process the REQ_AUTH packet.

通知认证状态机模块处理REQ_AUTH报文

User-SM *ip-addr*: Notified  auth-sm to process the REQ_LOGOUT packet.

通知认证状态机模块处理REQ_LOGOUT报文

User-SM *ip-addr*: Notified  auth-sm to process the ACK_NTF_LOGOUT packet.

通知认证状态机模块处理ACK_NTF_LOGOUT报文

User-SM *ip-addr*: Notified  auth-sm to process the AFF_NTF_USERIPCHAN packet.

通知认证状态机模块处理AFF_NTF_USERIPCHAN报文

User-SM *ip-addr*: The new ACL *acl-number* authorized  by policy server is the same as the old one.

策略服务器授权给用户的ACL号和之前授权过的相同

User-SM *ip-addr*: AAA processed authentication request and returned *result-string*.

AAA处理了认证请求并返回认证结果*result-string*，包括以下取值：

·success：成功

·processing：处理中

·continue：继续

·failed：失败

·error：错误

User-SM *ip-addr*: AAA processed authorization request and returned *result-string*.

AAA处理了授权请求并返回授权结果*result-string*，包括以下取值：

·success：成功

·processing：处理中

·failed：失败

·error：错误

User-SM *ip-addr*: AAA processed accounting-start request and returned *result-string*.

AAA处理了开始计费请求并返回计费结果*result-string*，包括以下取值：

·processing：处理中

·非processing：成功

User-SM *ip-addr*: AAA processed accounting-update request and returned *result-string*.

AAA处理了实时计费请求并返回计费结果*result-string*，包括以下取值：

·success：成功

·processing：处理中

·failed：失败

User-SM *ip-addr*: AAA processed accounting-stop request and returned *result-string*.

AAA处理了停止计费请求并返回计费结果*result-string*，包括以下取值：

·processing：处理中

·非processing：成功

User-SM *ip-addr*: AUTH-SM logged out the user and notified USER-SM to do.  

认证状态机完成了用户下线处理，通知用户状态机继续处理

User-SM *ip-addr*: Auth-SM notified

 User-SM that user-ip updated.

认证状态机通知用户状态机，用户IP已更新

User-SM *ip-addr*: Received authentication response, RespCode=*resp-code*.

收到认证回应报文，回应代码为*resp-code*，包括以下取值：

·0：表示成功

·26：表示失败

User-SM *ip-addr*: Received authorization response, RespCode=*resp-code*.

收到授权回应报文回应代码为*resp-code*，包括以下取值：

·0：表示成功

·26：表示失败

User-SM *ip-addr*: Received accounting-start response.

收到开始计费回应报文

User-SM *ip-addr*: Received accounting-update response.

收到更新计费回应报文

User-SM *ip-addr*: Received accounting-stop response.

收到停止计费回应报文

User-SM *ip-addr*:  Detection failed and user logged off.

用户探测失败，用户被强制下线

User-SM *ip-addr*: Received rule result *result*.

接收到用户规则下发结果为*result*，包括以下取值：

·success：成功

·fail：失败

User-SM *ip-addr*: User is logging off now.

用户正在下线过程中

User-SM *ip-addr*: Notified Auth-SM to log user out.

通知认证状态机强制用户下线

User-SM *ip-addr*: Received set-policy COA/POD notification.

用户状态机接收到COA/POD通知，其中，COA用于授权变更，POD用于强制用户下线

User-SM *ip-addr*: Recover failed and user logged off.

获取用于恢复用户信息的数据失败，用户被强制下线

User-SM *ip-addr*: Receiving last traffic when user is logging off..

用户下线时，最后一次接收到流量更新消息

User-SM *ip-addr*: User IP changed.

用户IP变更

Received DHCP event: operation=*event*, IP=*ip-addr*, MAC=*mac-addr*, interface=*ifname*.

收到DHCP事件*event*，*event*包括以下取值：

·Add：DHCP租约添加事件

·Del：DHCP租约删除事件

·Get：DHCP租约获取事件

BUTT：DHCP租约平滑结束事件

USER: Received a message for adding DHCP client (MAC=*mac-addr*, IP=*ip-addr*, Interface=*ifname*, VPN instance=*vpn-instance*).

收到DHCP租约创建消息（MAC地址为*mac-addr*，IP地址为*ip-addr*，接入接口为*ifname*，所属VPN实例为*vpn-instance*）

User-SM*ip-addr*: Added ARP rule.

为用户添加对应的ARP规则

User-SM*ip-addr*: Started User-SM timer (*interval* sec).

开启用户状态机定时器，超时时间为*interval*秒

User-SM*ip-addr*: Received deployment results of all rules.

收到所有用户规则下发的结果

User-SM*ip-addr*: Stopped User-SM timer.

关闭用户状态机定时器

User-SM*ip-addr*: Entered state: *vsrp-state*.

用户进入VRSP状态*vsrp-state*，状态取值如下：

·vsrp_master：开始为VRSP双机主用户授权

·vsrp_master_ok：VRSP主用户授权完成

·vsrp_backup：开始为VRSP备用户授权

vsrp_backup_ok：VRSP备用户授权完成

Created pre-auth user for VSRP backup.

在VSRP备份设备上创建认证前用户

Can\'t create pre-auth user: Portal was disabled.

Portal未使能，不创建认证前用户

Can\'t create pre-auth user: No pre-auth domain configured.

接口未配置认证前域，不创建认证前用户

Inappropriate state. Dropped batch-user-backup message.

本机未处于VSRP双机稳态，丢弃批量备份用户数据的消息

Port and user not in the same VLAN.

接口所在VLAN与用户所属VLAN不一致

User-SM *ip-addr*: Deauthorized pre-auth user: User coming online.

用户认证上线，取消认证前域下发的授权

Can\'t create pre-auth user when user was offline because of unavailable port.

端口不可用，强制用户下线，且不创建认证前用户

Can\'t create pre-auth user: Unsupported portal-auth type.

Layer3方式的Portal认证不支持认证前域，不创建认证前用户

Can\'t create pre-auth user: Interface was not operating correctly.

接口工作状态不正常，不创建认证前用户

Can\'t create pre-auth user: VSRP was down on the interface.

VSRP状态为down，不创建认证前用户

****

表1-3 debugging portal fsm 命令输出信息描述表

字段

描述

AUTH_SM *ip-addr*: Entered *state* state.

认证状态机（用户IP地址为*ip-addr*）进入状态*state*，包括以下取值：

·Authenticating：正在认证

·Authenticated：认证成功

·Continue：认证持续

·AssigningNewIP：等待分配IP地址

·AssignedNewIP：分配到IP地址

·Online：在线

·Waiting：强制下线状态，等待NTF_LOGOUT响应

·Offline：下线处理状态

Auth-SM: Started to run.

认证状态机开始运转

User_Detect_SM *ip-addr*: Entered *state* state.

用户探测状态机（用户IP地址为*ip-addr*）进入状态*state*，包括以下取值：

·Detected：已探测状态

·Wait_Detect：等待探测状态

·Detecting：正在探测状态

·DetectFail：探测失败状态

User-SM *ip-addr*: State changed from *old-state* to *new-state*.

用户状态机状态发生变化（旧状态*old-state* -\> 新状态*new-state*），状态包括以下取值：

·Authenticating：正在认证

·Waiting_Author：等待授权结果

·Waiting_Rule_OK：等待规则下发结果

·Online：在线

·Offline_Waiting_Traffic：下线等待各板流量

·Offline_Waiting_Acctoff：等待停止计费回应

·Done：用户下线完成

User-SM *ip-addr*: Begin to run.

用户状态机开始运转

User-SM *ip-addr*: User deleted

用户被删除

****

【举例】

\# 在一台配置了Portal的设备上打开Portal状态机调试信息开关，当有Portal用户上线时，将输出以下调试信息。

\<Sysname\> debug portal fsm

\*Jan  7 00:06:44:214 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: Begin to run.]

*// 用户状态机开始运转，用户IP地址为197.197.197.1*

\*Jan  7 00:06:44:214 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: State changed from Initial to Authenticating.]

*// 用户状态机从Initial切换为Authenticating状态*

\*Jan  7 00:06:44:219 2011 Sysname PORTAL/7/FSM:

Auth-SM: Started to run.

*// 认证状态机开始运转*

\*Jan  7 00:06:44:220 2011 Sysname PORTAL/7/FSM:

Auth_SM[197.197.197.1: Entered state Authenticating.]

*// 认证状态机进入Authenticating状态*

User-SM197.197.197.1: Begin to run.

\*Jan  7 00:06:44:645 2011 Sysname PORTAL/7/FSM

*// 用户状态机不变*

Auth-SM: Started to run.

\*Jan  7 00:06:44:645 2011 Sysname PORTAL/7/FSM:

Auth_SM[197.197.197.1: Entered state Authenticated.]

*// 用户状态机进入Authenticated状态*

\*Jan  7 00:06:44:646 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: Begin to run.]

\*Jan  7 00:06:44:646 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: State changed from Authenticating to Waiting_Author.]

\*Jan  7 00:06:44:657 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: State changed from Waiting_Author to Waiting_Rule_OK.]

*[//  *]*用户状态机首先切换为Waiting_Author，然后切换为Waiting_Rule_OK*

\*Jan  7 00:06:44:667 2011 Sysname PORTAL/7/FSM:

Auth-SM: Started to run.

\*Jan  7 00:06:44:668 2011 Sysname PORTAL/7/FSM:

Auth_SM[197.197.197.1: Entered state Online.]

*// 认证状态机进入Online状态*

\*Jan  7 00:06:44:670 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: Begin to run.]

\*Jan  7 00:06:44:671 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: State changed from Waiting_Rule_OK to Online.]

*// 用户状态机切换为Online*

\*Jan  7 00:21:31:710 2011 Sysname PORTAL/7/FSM:

User-Detect-SM[197.197.197.1: Entered state Initial.]

*// 用户状态机进入Iintial状态*

User-Detect-SM197.197.197.1: Entered state Detected.

\*Jan  7 00:21:32:469 2011 Sysname PORTAL/7/FSM:

*// 用户探测状态机进入Detected状态*

\*Jan  7 00:35:16:169 2011 Sysname PORTAL/7/FSM:

Auth-SM: Started to run.

\*Jan  7 00:35:16:170 2011 Sysname PORTAL/7/FSM:

Auth_SM[197.197.197.1: Entered state Offline.]

*// 认证状态机进入Offline状态*

\*Jan  7 00:35:16:171 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: Begin to run.]

\*Jan  7 00:35:16:172 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: State changed from Online to Offline_Waiting_Traffic.]

*// 用户状态机切换为Offline_Waiting_Traffic状态*

\*Jan  7 00:35:16:180 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: Begin to run.]

\*Jan  7 00:35:16:181 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: State changed from Offline_Waiting_Traffic to Offline_Waiting_Acctoff.]

*// 用户状态机切换为Offline_Waiting_Accoff状态*

\*Jan  7 00:35:16:758 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: Begin to run.]

\*Jan  7 00:35:16:759 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: State changed from Offline_Waiting_Acctoff to Done.]

*// 用户状态机切换为Done状态*

\*Jan  7 00:35:16:759 2011 Sysname PORTAL/7/FSM:

User-SM[197.197.197.1: User deleted.]

*// 用户被删除*

\# 在一台配置了Portal的设备上打开Portal事件调试信息开关，当有Portal用户上线时，将输出以下调试信息。

\<Sysname\> debug portal event

\*Jan  7 00:38:37:954 2011 Sysname PORTAL/7/EVENT:

Auth-SM[197.197.197.1: Started the auth_sm timer, timeout=15 sec.]

*// 开启认证状态机定时器，时长为15秒*

\*Jan  7 00:38:37:955 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Notified Auth-SM to process the REQ_CHALLENGE packet.]

*// 通知协议状态机处理REQ_CHALLENGE报文*

\*Jan  7 00:38:37:963 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Notified Auth-SM to process the REQ_AUTH packet.]

*// 通知协议状态机处理REQ_AUTH报文*

\*Jan  7 00:38:37:965 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: AAA processed authentication request and returned processing.]

*[// AAA*]*处理认证请求，并返回结果为正在处理*

\*Jan  7 00:38:38:425 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Received authentication response, RespCode=0.]

*// 收到AAA的认证回应消息，响应码为0*

\*Jan  7 00:38:38:436 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: AAA processed authorization request and returned success.]

*[// AAA*]*处理授权请求，返回结果为成功*

\*Jan  7 00:38:38:448 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Started User-SM timer, timeout=600 sec.]

*// 开启用户状态机定时器，时长为600秒*

\*Jan  7 00:38:38:451 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Received rule result success.]

*// 收到规则下发成功的消息*

\*Jan  7 00:38:38:452 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Stopped User-SM timer.]

*// 关闭用户状态机定时器*

\*Jan  7 00:38:38:453 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: AAA processed accounting-start request and returned proc]

essing.

*[// AAA*]*处理开始计费请求，并返回结果为正在处理*

\*Jan  7 00:38:38:455 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Started session-timeout timer, timeout=900902 sec.]

*// 开启会话超时定时器，时长为900902秒*

\*Jan  7 00:38:38:456 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Started idle-cut timer, timeout=600 sec.]

*// 开启Idle-cut定时器，时长为600秒*

\*Jan  7 00:38:38:457 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Notify User-Detect-SM detecting started.]

\*Jan  7 00:38:38:458 2011 Sysname PORTAL/7/EVENT:

User-Detect-SM[197.197.197.1: Start detect function.]

*// 通知用户探测状态机开启探测*

\*Jan  7 00:38:38:458 2011 Sysname PORTAL/7/EVENT:

User-Detect-SM[197.197.197.1: Started detect idle timer, length=60(sec).]

*// 开启探测闲置定时器，时长为60秒*

\*Jan  7 00:38:38:546 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Received accounting-start response.]

*// 收到开始计费回应消息*

\*Jan  7 00:38:38:549 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Started accounting-update timer, timeout=720 sec.]

*// 开启实时计费定时器，时长为720秒*

\*Jan  7 00:39:38:686 2011 Sysname PORTAL/7/EVENT:

User-Detect-SM[197.197.197.1: Stopped detect timer.]

*// 关闭探测定时器*

\*Jan  7 00:39:39:687 2011 Sysname PORTAL/7/EVENT:

User-Detect-SM[197.197.197.1: Sent ICMP request successfully.]

*// 发送ICMP请求报文成功*

\*Jan  7 00:58:49:689 2011 Sysname PORTAL/7/EVENT:

User-Detect-SM[197.197.197.1: Started detect waiting-response timer, timeout=3 sec.]

*// 开启等待探测回应定时器，时长为3秒*

\*Jan  7 00:58:52:687 2011 Sysname PORTAL/7/EVENT:

User-Detect-SM[197.197.197.1: ARP entry refreshed.]

*// 用户ARP表项刷新*

User-Detect-SM197.197.197.1: Stopped detect timer.

\*Jan  7 00:58:52:689 2011 Sysname PORTAL/7/EVENT:

*// 关闭探测定时器*

\*Jan  7 01:00:36:547 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Notified Auth-SM to process the REQ_LOGOUT packet.]

*// 通知认证状态机处理REQ_LOGOUT报文*

\*Jan  7 01:00:36:549 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Auth-SM logged out the user and notified User-SM to proce.]

*// 认证状态机处理完成，通知用户状态机处理*

\*Jan  7 01:00:36:556 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Started User-SM timer, timeout=60 sec.]

*// 开启用户状态机定时器，时长为60秒*

\*Jan  7 01:00:36:562 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Receiving last traffic when offline.]

*// 获取用户的流量信息*

\*Jan  7 01:00:36:562 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Stopped User-SM timer.]

*// 关闭用户状态机定时器*

\*Jan  7 01:00:36:563 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: AAA processed accounting-stop request and returned processing.]

*// AAA处理停止计费请求，并返回结果为正在处理*

\*Jan  7 01:00:36:563 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Started User-SM timer, timeout=60 sec.]

*// 开启用户状态机定时器，时长为60秒*

\*Jan  7 01:00:37:169 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Received accounting-stop response.]

*// 收到计费停止响应报文*

\*Jan  7 01:00:37:170 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Stopped User-SM timer.]

*// 关闭用户状态机定时器*

\*Jan  7 01:00:37:172 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Stopped session-timeout timer.]

*// 关闭会话超时定时器*

\*Jan  7 01:00:37:172 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Stopped idle-cut timer.]

*// 关闭Idle-cut定时器*

\*Jan  7 01:00:37:173 2011 Sysname PORTAL/7/EVENT:

User-SM[197.197.197.1: Notify User-Detect-SM detecting stopped.]

*// 通知用户探测状态机关闭探测功能*

\*Jan  7 01:00:37:174 2011 Sysname PORTAL/7/EVENT:

User-Detect-SM[197.197.197.1: Stopped detect timer.]

*// 关闭探测定时器*

\# 在一台指定了Portal认证前域的设备上打开Portal事件调试信息开关，当有用户申请地址时，因为指定的Portal认证前域不存在，将输出以下调试信息。

\<Sysname\> debug portal event

\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;

Received DHCP event: operation=Add, IP=0x12120001, MAC=1cbd-b9e3-b0ed, interface=GigabitEthernet1/0/3.

\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;

USER: Received a message for adding DHCP client (MAC=1cbd-b9e3-b0ed, IP=18.18.0.1, Interface=GigabitEthernet1/0/3, VPN instance=).

*// 收到DHCP上报的租约创建事件*

\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/ERROR: -MDC=1;

Failed to find user by MAC (1cbd-b9e3-b0ed).

*// 根据上报租约的MAC地址找不到用户*

\*Sep 24 06:29:31:933 2014 Sysname PORTAL/7/ERROR: -MDC=1;

Failed to get author info for pre-auth user.

*// 获取认证前域授权信息失败，创建认证前用户失败*

\# 在一台配置了Portal认证前域的设备上打开Portal事件调试信息开关，当有用户申请地址时，将输出以下调试信息。

\<Sysname\> debug portal event

\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;

Received DHCP event: operation=Add, IP=0x12120001, MAC=1cbd-b9e3-b0ed, interface=GigabitEthernet1/0/3.

*// 收到DHCP上报的租约创建事件*

\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;

USER: Received a message for adding DHCP client (MAC=1cbd-b9e3-b0ed, IP=18.18.0.1, Interface=GigabitEthernet1/0/3, VPN instance=).

*// 收到DHCP上报的租约创建事件*

\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/ERROR: -MDC=1;

Failed to find user by MAC (1cbd-b9e3-b0ed).

*// 根据租约找不到对应用户*

\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;

User-SM[18.18.0.1: Added ARP rule.]

*// 添加ARP规则*

\*Sep 24 06:29:31:924 2014 Sysname PORTAL/7/EVENT: -MDC=1;

User-SM[18.18.0.1: Added user rule.]

*// 添加认证前用户规则*

\*Sep 24 06:29:31:933 2014 Sysname PORTAL/7/EVENT: -MDC=1;

User-SM[18.18.0.1: Started User-SM timer (600 sec). ]

*// 开启规则等待定时器*

\*Sep 24 06:29:31:944 2014 Sysname PORTAL/7/EVENT: -MDC=1;

User-SM[18.18.0.1: Received deployment results of all rules.]

*// 收到规则下发结果*

\*Sep 24 06:29:31:945 2014 Sysname PORTAL/7/EVENT: -MDC=1;

User-SM[18.18.0.1: Stopped User-SM timer.]

*// 停止规则等待定时器*

\*Sep 24 06:29:31:945 2014 Sysname PORTAL/7/EVENT: -MDC=1;

User-SM[18.18.0.1: Entered state vsrp_master.]

*// 进入授权下发状态*

\*Sep 24 06:29:31:946 2014 Sysname PORTAL/7/EVENT: -MDC=1;

User-SM[18.18.0.1: Entered state vsrp_master_ok.]

*// 授权下发完成*

**Portal \-- Portal调试命令 \-- debugging portal interface**

------------------------------------------------------------------------

【命令】

**[debugging portal**[ { **all** \| **packet** [ **acl** *acl-number* ] \| **rule** } **interface** *interface-type interface-number*]]

**[undo debugging portal**[ { **all** \| **packet** [ **acl** *acl-number* ] \| **rule** } **interface** *interface-type interface-number*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有Portal调试信息开关。

**[packet**]：表示Portal协议报文调试信息开关。

**[rule**]：表示Portal 规则调试信息开关。

**[acl ***acl-number*]：表示仅输出与指定ACL的permit规则匹配的Portal协议报文的调试信息开关。

**[interface** *interface-type interface-number*]：表示指定接口的调试信息开关。*interface-type interface-number*为接口类型和接口编号。

【描述】

**[debugging portal interface**]命令用来打开指定接口的Portal调试信息开关。**undo debugging portal interface**命令用来关闭指定接口的Portal调试信息开关。

缺省情况下，接口上的Portal调试信息开关处于关闭状态。

表1-4 debugging portal packet interface命令输出信息描述表

字段

描述

Portal received *pkt-num* bytes of packet Type: *type-name*(*type-num*) ErrCode: *err-code*, IP: *user-ip*

Portal接收到报文，字节数为*pkt-num*，报文类型为*type-name*（类型代码为*type-num*），错误码为*err-code*，IP地址为user-ip

Portal sent *pkt-num* bytes of packet Type: *type-name*(*type-num*), ErrCode: *err-code*, IP: *user-ip*

Portal发送报文，字节数为*pkt-num*，报文类型为*type-name*（类型代码为*type-num*），错误码为*err-code*，IP地址为*user-ip*

 *attr-type-code attr-type-name*   a*ttr-length*   *attr-data*

Portal协议属性列表信息

·*attr-type-code*：属性类型编号

·*attr-type-name*：属性类型名称

·*attr-length*：属性值长度

·*attr-data*：属性值内容

****

表1-5 debugging portal rule interface命令输出信息描述表

字段

描述

L3 Interface = *interface-name*, L2 Interface= *port-name*, VLAN= *src-vlan-id*, SrcMac = *src-mac*, SrcIP = *src-ip*, DstIP = *dst-ip,* Protocol = *protocol-name*, SrcPort = *src-port-num*, DstPort = *dst-port-num*, VPN Instance = *vpn-index*

符合匹配规则的报文信息

·L3 Interface：用户接入的三层接口名

·L2 Interface：用户接入的二层端口名

·VLAN：用户接入的VLAN

·SrcMac：报文的源MAC地址

·DstMac: 报文的目的mac地址

·SrcIP：报文的源IP地址

·DstIP：报文的目的IP地址

·Protocol：报文的传输层协议类型

·SrcPort：报文的源端口号

·DstPort：报文的目的端口号

·Vpn Instance：报文所属的VPN索引

DRV_FREE_RULE:

Interface= *interface-name*

VLAN             = *vlan-id*

SrcMAC           = *src-mac*

SrcIP            = *src-ip*

SrcMask          = *src-mask*

DstIP            = *dst-ip*

DstMask          = *dst-mask*

L4Protocol       = *protocol-name*

SrcPortMin       = *min-src-port-num*

SrcPortMax       = *max-src-port-num*

DstPortMin       = *min-dst-port-num*

DstPortMax       = *max-dst-port-num*

Operation        = *operation*

下发给驱动的免认证规则的内容：

·Interface：用户接入的接口名

·VLAN：用户接入的VLAN

·SrcMac：用户的源MAC地址

·SrcIP：用户报文的源IP地址

·SrcMask：报文源IP地址掩码

·DstIP：用户报文的目的IP地址

·DstMask：用目的IP地址掩码

·L4Protocol：报文的传输层协议号

·SrcPortMax：最大源端口号

·SrcPortMin：最小源端口号

·DstPortMin：最小目的端口号

·DstPortMax：最大目的端口号

·Operation：规则的动作，包括add（添加）和delete（删除）

DRV_USER_RULE:

L2 Interface           = *interface-name*

L3 Interface = *nterface-name*

VLAN             = *vlan-id*

SrcIP            = *src-ip*

SrcMac           = *src-mac*

AuthorACL        = *acl-num*

Operation        = *operation*

SetDrvFlag    =  *operation*

下发给驱动的用户规则的内容：

· L2 Interface：用户接入的二层接口名

·L3 Interface：用户接入的三层接口名

·VLAN：用户接入的VLAN

·SrcIP：用户报文的的源IP地址

·SrcMac：用户报文的源MAC地址

·AuthorACL：用户的授权ACL号

·Operation：规则的动作，包括add（添加）和delete（删除）

·SetDrvFlag：下发驱动的动作，包括需要下发和不需要下发

DRV_REDIRECT_RULE:

Interface = *interface-name*

VLAN             = *vlan-id*

Protocol         = *protocol-name*

SrcIP            = *src-ip*

SrcMask          = *src-mask*

DstIP            = *dst-ip*

DstMask          = *dst-mask*

L4 Protocol       = *protocol-name*

DstPort          = *dst-port-num*

Operation        = *operation*

下发给驱动的重定向规则的内容：

·Interface：用户接入的接口名

·VLAN：用户接入的VLAN

·Protocol：用户报文的传输层协议号

·SrcIP：用户报文的源IP地址

·SrcMask：报文的源IP地址掩码

·DstIP：用户报文的目的IP地址

·DstMask：报文的目的IP地址掩码

·L4Protocol：报文的传输层协议号

·DstPort：报文的目的端口号

·Operation：规则的动作，包括add（添加）和delete（删除）

DRV_DENY_RULE:

Interface          = *interface-name*

VLAN             = *vlan-id*

Protocol         = *protocol-name*

SrcIP            = *src-ip*

SrcMask          = *src-mask*

DstIP            = *dst-ip*

DstMask          = *dst-port-num*

Operation        = *operation*

下发给驱动的deny规则的内容：

·Interface：用户接入的接口名

·VLAN：用户接入的VLAN

·Protocol：用户报文的传输层协议号

·SrcIP：用户报文的源IP地址

·SrcMask：报文的源IP地址掩码

·DstIP：用户报文的目的IP地址

·DstMask：报文的目的IP地址掩码

·Operation：规则的动作，包括add（添加）和delete（删除）

IN Matching free rule.

入方向匹配到免认证规则

Out Matching free rule.

出方向匹配到免认证规则

IN Matching Redirect rule.

入方向匹配到重定向规则

Out Matching Redirect rule.

出方向匹配到重定向规则

IN Matching deny rule.

入方向匹配到deny规则

Out Matching deny rule.

出方向匹配到deny规则

IN Matching User rule.

入方向匹配到用户规则

Out Matching User rule.

出方向匹配到用户规则

【举例】

\# 在一台配置了Portal的设备上打开接口GigabitEthernet 1/0/1上的Portal报文调试信息开关，当有Portal用户上线时，将输出以下调试信息。

\<Sysname\> debug portal packet interface gigabitethernet 1/0/1

\*Nov  1 09:23:02:146 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal received 34 bytes of packet[Type:req_info(9) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:23:02:146 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 09 00 00 05 c9 00 00 09 09 00 02 00 00 00 01

02 5c 3a 80 b3 dd 5e 16 72 4a 62 91 7e b2 31 47

08 02

*// 设备收到REQ_INFO报文*

\*Nov  1 09:23:02:147 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal sent 62 bytes of packet[Type:ack_info(10) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:23:02:147 2012 Sysname PORTAL/7/PACKET: -MDC=1;

  8 PORT                  24 Sysname-vlan-00-65535@vlan

 10 BASIP                  6 9.9.0.1

\*Nov  1 09:23:02:147 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 0a 00 00 05 c9 00 00 09 09 00 02 00 00 00 02

a3 28 68 91 2b 15 b0 d3 f4 e3 22 ae 7f 01 e3 26

08 18 48 33 43 2d 76 6c 61 6e 2d 30 30 2d 36 35

35 33 35 40 76 6c 61 6e 0a 06 09 09 00 01

*// 设备向Portal服务器回应ACK_INFO报文*

\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal received 32 bytes of packet[Type:req_challenge(1) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 01 00 00 05 c9 00 00 09 09 00 02 00 00 00 00

5d 68 8d 7c 58 67 51 6f d8 1a f9 d8 ed ae 35 90

*// 设备收到Portal服务器发来的REQ_CHALLENGE报文*

\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal sent 56 bytes of packet[Type:ack_challenge(2) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;

  3 CHALLENGE             18 a89c5701492727bed97dbb09ac1d821f

 10 BASIP                  6 9.9.0.1

\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 02 00 00 05 c9 00 04 09 09 00 02 00 00 00 02

d0 a1 65 24 b2 8f c0 1d c0 bb a1 39 1f 5b cb 42

03 12 a8 9c 57 01 49 27 27 be d9 7d bb 09 ac 1d

82 1f 0a 06 09 09 00 01

*// 设备向Portal服务器回应ACK_CHALLENGE报文*

\*Nov  1 09:23:02:155 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal received 86 bytes of packet[Type:req_auth(3) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:23:02:155 2012 Sysname PORTAL/7/PACKET: -MDC=1;

  1 USERNAME              12 yangliping

  4 CHAPPWD               18 10271c91c981016ca0b7df2ab21af265

  3 CHALLENGE             18 a89c5701492727bed97dbb09ac1d821f

 10 BASIP                  6 9.9.0.1

\*Nov  1 09:23:02:155 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 03 00 00 05 c9 00 04 09 09 00 02 00 00 00 04

ee 86 98 7e 66 5e c1 41 46 96 15 cc a3 7f 51 5f

01 0c 79 61 6e 67 6c 69 70 69 6e 67 04 12 10 27

1c 91 c9 81 01 6c a0 b7 df 2a b2 1a f2 65 03 12

a8 9c 57 01 49 27 27 be d9 7d bb 09 ac 1d 82 1f

0a 06 09 09 00 01

*// 设备收到Portal服务器发来的REQ_AUTH报文*

%Nov  1 09:23:02:338 2012 Sysname PORTAL/6/PORTAL_USER_LOGON_SUCCESS: -MDC=1; -UserName=yangliping-IPAddr=9.9.0.2-IfName=Ethernet1/1-VlanID=65535-MACAddr=

0200-4c4f-4f50:User got online successfully.

\*Nov  1 09:23:02:339 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal sent 63 bytes of packet[Type:ack_auth(4) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:23:02:339 2012 Sysname PORTAL/7/PACKET: -MDC=1;

 11 SESSIONID              8 0200-4c4f-4f50

 33 RELAYMSG               4 6

 10 BASIP                  6 9.9.0.1

\*Nov  1 09:23:02:339 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 04 00 00 05 c9 00 04 09 09 00 02 00 00 00 05

bf 6a eb d9 38 48 6e 90 06 06 31 a4 72 72 f3 79

0b 08 02 00 4c 4f 4f 50 21 04 36 06 21 09 09 6c

69 70 69 6e 67 21 04 21 29 0a 06 09 09 00 01

*// 设备向Portal服务器回应ACK_AUTH报文*

\*Nov  1 09:23:02:357 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal received 32 bytes of packet[Type:aff_ack_auth(7) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:23:02:357 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 07 00 00 05 c9 00 04 09 09 00 02 00 00 00 00

70 4b cd 55 1a cc ec fe 0f ce eb bf c0 c2 3c a5

*// 设备收到Portal服务器发来的AFF_ACK_AUTH报文*

\*Nov  1 09:23:02:441 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal sent 53 bytes of packet[Type:ntf_user_notify(19) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:23:02:441 2012 Sysname PORTAL/7/PACKET: -MDC=1;

 33 RELAYMSG              15 =M4BzIltI\>o

 10 BASIP                  6 9.9.0.1

\*Nov  1 09:23:02:441 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 13 00 00 05 c9 00 04 09 09 00 02 00 00 00 02

e9 fe 48 a0 10 ed e3 65 fb 11 2f 2e 77 32 e3 21

21 0f 3d 0a 4d 34 42 7a 49 6c 74 49 3e 06 6f 0a

06 09 09 00 01

*// 设备向Portal服务器发送NTF_USER_NOTIFY报文*

\<Sysname\>\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal received 44 bytes of packet[Type:req_logout(5) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;

 10 BASIP                  6 9.9.0.1

\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 05 00 00 05 ca 00 00 09 09 00 02 00 00 00 02

b2 8a 69 17 fe 31 df 51 fa 47 26 f6 56 93 a6 0a

0a 06 09 09 00 01 0c 06 00 00 00 00

*// 设备收到Portal服务器发来的REQ_LOGOUT报文*

\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;

Portal sent 46 bytes of packet[Type:ack_logout(6) ErrCode:0 IP:9.9.0.2]

\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;

 11 SESSIONID              8 0200-4c4f-4f50

 10 BASIP                  6 9.9.0.1

\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;

02 06 00 00 05 ca 00 00 09 09 00 02 00 00 00 02

57 25 4e 31 a7 c1 61 a0 76 e0 26 8e 46 aa 4f 3a

0b 08 02 00 4c 4f 4f 50 0a 06 09 09 00 01

*// 设备向Portal服务器回应ACK_LOGOUT报文*

\# 打开接口Vlan-interface6上的Portal规则调试信息开关，当该接口上使能Portal认证时，将输出以下调试信息。

\<Sysname\> debug portal rule interface vlan-interface 6

\*Nov  1 09:30:18:689 2012 Sysname PORTAL/7/RULE: -MDC=1;

 DRV_FREE_RULE:

    Interface        = GigabitEthernet 1/0/1

    VLAN             = 6

    SrcMAC           = 0000-0000-0000

    SrcIP            = 0.0.0.0

    SrcMask          = 0.0.0.0

    DstIP            = 192.168.0.111

    DstMask          = 255.255.255.255

    L4Protocol       = 0

    SrcPortMin       = 0

    SrcPortMax       = 0

    DstPortMin       = 0

    DstPortMax       = 0

    Operation        = 1

*// 使能Portal后添加的免认证规则内容*

\*Nov  1 09:30:18:689 2012 Sysname PORTAL/7/RULE: -MDC=1;

 DRV_REDIRECT_RULE:

    Interface        = GigabitEthernet 1/0/1

    VLAN             = 6

    Protocol         = 2

    SrcIP            = 0.0.0.0

    SrcMask          = 0.0.0.0

    DstIP            = 0.0.0.0

    DstMask          = 0.0.0.0

    L4Protocol       = 6

    DstPort          = 80

    Operation        = 1

*// 使能Portal后添加的重定向规则内容*

\*Nov  1 09:30:18:689 2012 Sysname PORTAL/7/RULE: -MDC=1;

 DRV_DENY_RULE:

    Interface        = GigabitEthernet 1/0/1

    VLAN             = 6

    Protocol         = 2

    SrcIP            = 0.0.0.0

    SrcMask          = 0.0.0.0

    DstIP            = 0.0.0.0

    DstMask          = 0.0.0.0

    Operation        = 1

*// 使能Portal后添加的deny规则内容*

\*Jan  6 20:17:06:382 2011 Sysname PORTAL/7/RULE:

 DRV_USER_RULE:

    L2 Interface     = N/A

    L3 Interface     = GigabitEthernet 1/0/1

    VLAN             = 6

    SrcIP            = 9.9.0.1

    SrcMAC           = 0200-4c4f-4f50

    AuthorACL        = 3000

    Operation        = 0

    SetDrvFlag       = 1

*// 用户上线后添加的用户规则内容*

Out Matching free rule

*// 出方向匹配到free规则*

L3 Interface = GigabitEthernet1/0/2, L2 Interface = \--, VLAN = \--, DstMAC = 0000-0000-0000, SrcIP = 9.9.0.2, DstIP = 192.168.0.34

 L4Protocol = 6, SrcPort = 1699, DstPort = 23, VPN Instance = 0

\*Nov  1 09:30:19:967 2012 Sysname PORTAL/7/RULE: -MDC=1;

*// 符合匹配规则的报文信息*

 IN Matching free rule

*// 入方向匹配到free规则*

L3 Interface = GigabitEthernet1/0/2, L2 Interface = \--, VLAN = \--, SrcMac = 0200-4c4f-4f50,SrcIP = 9.9.0.2, DstIP = 192.168.0.34

 L4Protocol = 6, SrcPort = 1699, DstPort = 23, VPN Instance = 0

\*Nov  1 09:30:20:088 2012 Sysname PORTAL/7/RULE: -MDC=1;

*// 符合匹配规则的报文信息*

OUT Matching Deny rule

*// 出方向匹配到deny规则*

L3 Interface = GigabitEthernet1/0/2, L2 Interface = \--, VLAN = \--, DstMAC = 0200-4c4f-4f50,SrcIP = 9.9.0.2, DstIP = 9.9.0.1

 L4Protocol = 1, SrcPort = 0, DstPort = 0, VPN Instance = 0

\*Nov  1 09:30:31:603 2012 Sysname PORTAL/7/RULE: -MDC=1;

*// 符合匹配规则的报文信息*

**

 IN Matching Deny rule

 L3 Interface = GigabitEthernet1/0/2, L2 Interface = \--, VLAN = \--, SrcMac = 14d6-4d14-bd9b,

SrcIP = 10.153.72.116, DstIP = 239.255.255.250

 L4Protocol = 17, SrcPort = 49159, DstPort = 1900, VPN Instance = 0

\*Nov  1 09:30:31:683 2012 Sysname PORTAL/7/RULE: -MDC=1;

*// 报文经过设备访问外网*

