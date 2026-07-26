
**IPoE调试命令 \-- IPoE调试命令 \-- debugging ip subscriber**

------------------------------------------------------------------------

【命令】

**[debugging ip subscriber **[{ **all** \| **error** \| **event** \| **timer** }]]

**[undo debugging ip subscriber **[{ **all** \| **error** \| **event** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示IPoE的所有调试信息开关

**[error**]：表示IPoE的错误调试信息开关。

**[event**]：表示IPoE的事件调试信息开关。

**[timer**]：表示IPoE的定时器调试信息开关。

【描述】

**[debugging ip subscriber**]命令用来打开基于IPv4协议的IPoE的调试信息开关。**undo debugging ip subscriber**命令用来关闭基于IPv4协议的IPoE的调试信息开关。

缺省情况下，基于IPv4协议的IPoE的调试信息开关处于关闭状态。

表1-1 debugging ip subscriber error命令输出信息描述表

字段

描述

Failed to set an ANCP policy: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*, Reason=*reason*.

设置ANCP（Access Node Control Protocol）策略失败

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

·Reason：原因，包括以下取值：

¡Success：成功

¡Line down：链路断掉

¡Invalid ID：无效的id

¡Not implement：未生效

¡No enough resource：资源不足

¡Process timeout：处理超时

¡Other reason：其他原因

Failed to send an ARP request: Interface= interface-name, IP=ip, VLAN=vlan, CVLAN= cvlan.

发送ARP失败

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Failed to select srcAddr: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

选择IPv4源地址失败

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Failed to send an ICMP packet: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

发送ICMP报文失败

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Failed to get ARP refresh time: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

获取ARP表项时间戳失败

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Failed to enable the user detection function: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN =*cvlan*.

使能用户探测功能失败

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Received an error ICMP reply.

接收到错误的ICMP回复报文

Failed to get info from an ICMP reply.

从ICMP回复报文中提取信息失败

Failed to enable the interface detection function.

使能接口探测功能失败

Invalid IP(0.0.0.0) for an ARP rule.

(0.0.0.0)为ARP非法地址

Failed to reconnect to ARP, and returned Code=*code*.

重连ARP失败.:返回值为code

HA upgrading failed

备升主升级失败

Malloc failure for muliticast addresses..

给组播地址分配内存失败

Failed to set DSL line characters.

设置DSL line失败

Failed to update ANCP policy *name*.

更新ANCP策略（名字为*name*）失败.

Failed to open the session-timeout timer.

打开session-timeout定时器失败

Failed to open the idle-cut timer.

打开idle-cut定时器失败

Failed to open the accounting-update timer.

打开accounting-update定时器失败

VPN doesn\'t exist and session will be offline..

下发的授权VPN属性在设备上不存在，强制会话处于下线状态

Failed to set pam items during authentication.

认证时设置pam items属性失败

Can\'t insert NAS information, because the Circuit ID option is invalid.

由于Circuit ID无效，不能插入NAS信息

Failed to find sessions (UserID=*userid*).

根据userid查找session失败（用户ID为*userid*）

Userprofile has been deleted (UserID=*userid*).

Userprofile已经被删除了（用户ID为*userid*）

Failed to notify the kernel to get traffic.

通知内核获取流量失败

Failed to send a traffic message.

流量消息发送失败

Failed to send VSRP batch session messages (VSRP instance=*vsrp-instance-name*).

发送VSRP批备会话消息失败（VSRP实例名称为*vsrp-instance-name*）

Failed to process a VSRP MAC event.

处理VSRP虚MAC变化事件失败

Failed to connect to the peer of VSRP instance (VSRP instance=*vsrp-instance-name*).

连接到VSRP（VSRP实例名称为*vsrp-instance-name*）对端失败

Failed to synchronize a VSRP event to IO.

同步VSRP事件到接口板失败

Failed to send a control message to IO (VSRP instance=*vsrp-instance-name*).

往接口板发送控制消息失败（VSRP实例名称为*vsrp-instance-name*）

Failed to process the packet.

处理报文失败

表1-2 debugging ip subscriber timer命令输出信息描述表

字段

描述

Session-timer expired and session was offline.

会话定时器超时，用户下线.

Failed to find sessions after a session-timer expired.

会话超时定时器超时时未找到会话

Check session expired: current time=*time1*, old stamp=*time2* sec.

检查会话超时，当前时间为*time1*，会话开始时间为*time2*

Refreshed a session-timeout timer, current time=*time*, timeout=*timeout* sec.

更新会话定时器，当前时间为*time*，超时时间为*timeout*.

Opened a session-timeout timer, current time=*time*, timeout=*timeout* sec.

打开会话定时器，当前时间为*time*， 超时时间为*timeout*.

Closed the idle-cut timer.

关闭空闲定时器.

Failed to find sessions after an idle-timer expired.

空闲定时器超时后未找到会话

Idle-cut timer expired and session was offline.

空闲定时器超时用户下线

Opened an idle-cut timer: timeout = * timeout* sec.

打开空闲定时器， 超时时间为*timeout*

Closed an accounting-update timer.

关闭计费更新定时器

Failed to find sessions after an accounting-update timer expired (IP=*ip*).

计费更新定时器超时后（IP地址为*ip*）未找到会话

Refreshed an accounting-update timer: timeout=*timeout* sec.

重刷计费更新定时器， 超时时间为*timeout*

Opened an accounting-update timer: timeout=*timeout* sec.

打开计费更新定时器， 超时时间为*timeout*

Created timer *tid*, which will expire in *time* sec.

创建一个定时器（定时器ID为*tid*），*times*秒后超时

Deleted timer *tid*.

删除一个定时器（定时器ID为*tid*）

Refreshed timer *tid*: timeout=*timeout* sec.

重刷定时器（定时器ID为*tid*），超时时间为*timeout*

Sent an ICMP packet successfully: Interface=*interface**-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*

发送ICMP报文成功

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

User detection timer expired: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

用户探测定时器超时

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Closed a session-timeout timer.

关闭会话超时定时器

表1-3 debugging ip subscriber event命令输出信息描述表

字段

描述

ARP/ND Rule thread processed request msg(MsgType=*type*).

ARP/ND Rule线程处理请求消息（消息类型为*type*）

Sent an ARP request successfully: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN =*cvlan*.

发送ARP成功

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Added user detection entry successfully: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

添加探测用户成功

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Deleted user detection entry: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

删除探测用户

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Enabled user detection: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

开启用户探测

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Received an ICMP reply: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

接收ICMP回复报文

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Refreshed user detection: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

重刷用户探测

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

FSM EVT: Deleted a session, Event=OTHER, Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

状态机事件：删除会话

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: Got a session offline, Event=OTHER, Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

状态机事件：强制会话下线

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: In INITIAL state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

状态机事件：当前为INIT状态，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: DHCP lease expired, Event=OFFLINE, Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

状态机事件：会话的DHCP租约超时，用户下线

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: In ONLINE state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

状态机事件：当前为用户在线状态，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: In ASSIGNEDIP state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

状态机事件：当前为会话已具备IP地址状态，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: In AUTHPASS state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

状态机事件：当前为认证通过状态，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，*type*包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，*state*包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: In AUTHFAIL state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

状态机事件：当前为认证失败状态，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: In INVALID state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

状态机事件：当前为无效状态，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: In AUTH state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

状态机事件：当前为认证中状态，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: In BACKUP state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

状态机事件：当前为备份状态，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: Went on fsm, Event=OTHER, Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

状态机事件：session平滑后，将状态机继续走下去

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

FSM EVT: Triggered the fsm, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

状态机事件：触发状态机，收到了*event*事件

·Event：事件名称，包括以下取值：

¡CREATEANDGO：配置创建

¡INIT：报文触发

¡AUTH：进行认证的条件已经满足（静态需要此事件）

¡AUTHPASS：认证通过

¡AUTHFAIL：认证失败

¡ASSIGNIP：地址分配成功（动态dhcp session）

¡AGE：老化（动态session）

¡RULEOK：规则下发成功

¡RULEFAIL：规则下发失败

¡OFFLINE：用户下线事件

¡QUIET：静默定时器超时

¡DESTROY：删除session

¡CHANGE OF AUTHORIZATION：AAA授权属性变更

¡USERPROFILE OK：User Profile下发驱动成功

¡USERPROFILE FAIL：User Profile下发驱动失败

¡BACKUP：收到VSRP对端设备发送过来的session

¡BACKUP to ONLINE：收到VSRP backup变master的事件

¡OTHER：无事件触发

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Added an ARP rule successfully: Interface=*interface-name,* VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node**.

添加一条ARP规则成功，

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Deleted an ARP rule successfully: IP=*ip*.

删除一条ARP规则成功，IP地址为*ip*

Successfully notified DHCP to release a client.

通知DHCP释放DHCPv4用户信息成功

Failed to notify DHCP to release the IP address of the client and returned Code=*code*.

通知DHCP释放DHCPv4用户信息失败，返回值为*code*

Deleted a session by DHCPv4 event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

因DHCPv4事件删除session

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

User ID

用户ID

Flag

支持的网络特征掩码

·0x01：接口有效

·0x02：用户MAC有效

·0x04：用户IP地址有效

·0x08：用户PVC ID有效

·0x10：用户VPN索引有效

·0x20：用户SVLAN有效

·0x40：用户CVLAN有效

Interface

用户使用的接口索引

VPN instance

用户VPN实例

Src IP

用户的IP地址

PVC ID

ATM接口的PVC ID

SVLAN ID

用户的服务器端VLAN

CVLAN ID

用户的客户端VLAN

MAC address

用户的MAC地址

Service type

用户的服务类型，包括以下取值：

·0：HSI

·1：STB（机顶盒）

Access limit

用户可点播的组播节目数目

User profile

授权下发的User Profile名字

Username

用户名

Username len

用户名长度

Max multicasts

最大组播数

Sent a mcast user *type* message.

发送组播用户事件类型是*type*的消息，*type*包括以下取值：

·online：用户上线

·offline：用户下线

·authchange：授权属性变更

·smooth：平滑

Sent a mcast user smooth start message.

发送组播用户平滑开始消息

Sent a mcast user smooth end message.

发送组播用户平滑结束消息

AAA processed *type* request and returned *result.*

AAA处理*type*类型请求并返回结果为*result*，*type*包括以下取值：

·authentication：认证

·authorization：授权

·accounting-start：计费开始

·accounting-update：实时计费

·accounting-stop：计费停止

*[result*]包括以下取值：

·success：成功

·processing：处理中

·fail(Errcode = *code*) ：失败（错误码为*code*）

Received AAA *type* response and returned *result,* the traffic level is *level.*.

接收AAA*type*类型回复并返回结果为*result*，流量级别为*level*，*type*包括以下取值：

·authentication：认证

·authorization： 授权

·accounting-start： 计费开始

·accounting-update：实时计费

·accounting-stop： 计费停止

*[result*]包括以下取值：

·success：成功

·processing ：处理中

·fail(Errcode = *code*)：失败（错误码为*code*）

Set an ANCP policy.

设置ANCP策略

Setting ANCP policy *name* failed.

设置ANCP策略（名字为*name*）失败

Updated an ANCP policy.

更新ANCP策略

Session timeout is zero in the accounting-update reply.

在计费更新报文回应报文中，最新下发的session-timeout值为0

Session authentication info: domain=*domain*.

会话认证信息： 认证域名为*domain*

Session (IP=*ip*) processed reconnected to AAA.

会话（IP地址为*ip*）与AAA模块进行重连接

Remanent_Volume is zero and session will be offline.

用户的剩余流量为0，强制会话下线

Session requested offline: state=*state*

会话请求下线，状态值为state，*state*包括以下取值：

·0：初始化状态

·1：认证状态

·2：等待授权状态

·3：在线状态

·4：计费状态

·5：计费停止状态

Session state error in the authentication response, state=*state*.

认证回应中的会话状态错误，状态值为state，*state*包括以下取值：

·0：初始化状态

·1：认证状态

·2：等待授权状态

·3：在线状态

·4：计费状态

·5：计费停止状态

Session state error in the authorization response, state=*state*.

授权回应中的会话状态错误，状态值为state，*state*包括以下取值：

·0：初始化状态

·1：认证状态

·2：等待授权状态

·3：在线状态

·4：计费状态

·5：计费停止状态

Session state error in the accounting-start response, state=*state*.

开始计费回应中的会话状态错误，状态值为state，*state*包括以下取值：

·0：初始化状态

·1：认证状态

·2：等待授权状态

·3：在线状态

·4：计费状态

·5：计费停止状态

Updated VPN info in session.

更新会话信息中的VPN属性

Updated session-timeout in session.

更新会话信息中的session-timeout属性

Session timeout is zero in COA and session will be offline.

在COA报文中session-timeout属性为0，强制会话下线

Updated the user profile in session.

更新会话信息中的User Profile属性

Received a notification message for setting AAA COA.

接收到设置策略COA通知消息

Received a notification message for setting policy POD.

接收到设置策略POD通知消息

Received an ACK Reply packet: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

接收到一个ACK回应报文

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，*type*包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

¡State：会话状态，state包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Received an ACK Reply packet to assign IP address: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*Received*.

接收到一个已分配IP地址的ACK回应报文

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Received a Renew Reply packet: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

接收到一个renew回应报文

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Received a NAK Reply packet: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

接收到一个NAK回应报文

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Received a sync session message: Interface=*interface-name,* VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node,* type=*type.*

接收到同步过来的会话信息

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

·type：消息类型

Received a sync message from node *node*.

从节点号是*node*的单板接收到同步消息

Begun to batch sessions.

开始批备会话信息

Begun to age and process all sessions.

开始 老化和处理所有会话

Requested to add a user-profile/Car rule (UserID=*id*).

请求添加User Profile规则（用户ID为*id*）

Requested to delete a user-profile/Car rule (UserID=*id*).

请求删除User Profile规则（用户ID为*id*）

Received result of setting user profile (UserID=*id*, Result=*result*).

接收设置User Profile的结果（用户ID为*id*， 结果为*result*）

Rule thread processed request messages (MessageType=*type*).

Rule线程处理请求消息（消息类型为*type*）

Remanent volume has been exhausted and session will be offline.

剩余流量已经耗尽，会话下线

Deleted cache sessions successfully: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.

成功删除缓存中的会话

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

IPoE Channel is connecting to the peer of instance *name*.

本实例和实例名字是*name*的对端建立备份通道

IPoE Channel is listening to the peer of instance *name*.

IPoE通道正在监听实例名字是*name*的对端

Synchronized VSRP event to IO successfully.

同步VSRP事件到接口板成功

Received a VSRP event(*type*) of instance *name* on IO.

接收到接口板上*type*类型的VSRP（VSRP实例名称为*name*）事件

Received a VSRP status event(status=*status*) of instance *name*.

接收到VSRP（VSRP实例名称为*name*）状态事件（状态值为*status*）

Received a VSRP backupmode event(mode=*mode*) of instance *name*.

接收到VSRP（VSRP实例名称为*name*）备份方式事件（备份方式为*mode*）

Received a VSRP interval event(interval=*interval*) of instance *name*.

接收到VSRP（VSRP实例名称为*name*）的流量备份间隔事件（间隔时长是*interval*）

Received a VSRP traffic threshold event(value=*val*) of instance *name*.

接收VSRP（VSRP实例名称为*name*）的流量备份阈值事件（阈值为*value*）

Received a VSRP VMAC event(mac=*mac*) of instance *name*.

接收到VSRP（VSRP实例名称为*name*）的虚MAC事件（MAC地址是*mac*）

Sent a VSRP control message to IO successfully, instance=*name*.

发送VSRP控制信息到接口板成功，VSRP实例名称为*name*

Added cache sessions for VSRP successfully: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node,*

成功添加了VSRP缓冲会话

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Channel is connected.

通道连接建立

Channel is disconnected.

通道连接断开

Dropped a DHCP packet from *mac* because of invalid state *state*.

由于会话状态 （状态值为*state*）无效，丢弃MAC地址是*mac*的DHCP报文

Started to authenticate unclassified IP packets from *ip*.

开始对IP地址是*ip*的未知源IP报文进行认证

Dropped IP packets from *ip* because of invalid state *state*.

由于会话状态（状态值为*state*）无效，丢弃IP地址是*ip*的报文

Dropped a DHCP packet from *mac* which is in state *state*.

丢弃处于会话状态（状态值是*state*）的MAC地址是*mac*的DHCP报文

Started to authenticate packets because of init state of interface leased.

接口专线处于Init状态，开始认证报文

Dropped the packet because of invalid state *state* of interface leased.

接口专线处于无效状态（状态值是*state*），丢弃报文

Tried to add a session, but IPoE is not enabled on interface.

添加会话时，接口上没有使能IPoE

Connected to LICENSE module.

IPoE模块与LICENSE模块的连接建立成功

Failed to connect to LICENSE module.

IPoE模块与LICENSE模块的连接建立失败

Disconnected from LICENSE module.

IPoE模块与LICENSE模块的连接断开成功

Received LICENSE event: EventType=*event-type*.

IPoE收到LICENSE的EventType事件

EventType类型如下：

·Installed：安装

·Uninstalled：卸载

·Expired：过期

Changed the session limit from old-value to new-value per card.

更新LICENSE定制的IPoE单板会话限制数

·*old-value*：旧的IPoE单板会话限制数

·*new-value*：新的IPoE单本会话限制数

【举例】

\# 打开IPv4 IPoE的所有调试信息开关。未知源IPv4的报文触发IPoE认证时，设备上将打印如下调试信息。

\<Sysname\> terminal monitor

\<Sysname\> terminal debugging

\<Sysname\> debugging ip subscriber all

\<Sysname\> \*Dec  1 16:43:12:878 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

Started to authenticate unclassified IP packets from 1.2.3.4.

*//开始对ip地址是*1.2.3.4*的未知源ip报文进行认证*

\*Dec  1 16:43:12:879 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, Event = INIT, Interface=GE5/2/2, VRF=0, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=INVALID, UserID=0xffffffff, Service node=slot 5 cpu 0.

*//状态机事件处理：触发，事件：初始化，接口是GE5/2/2，显示具体的session信息(非堆叠设备)*

\*Dec  1 16:43:12:879 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, EVENT = INIT, Interface=GE5/2/2, VRF=0, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=INVALID, UserID= 0xffffffff, Service node = slot 5 cpu 0\...

*//状态机事件处理：触发，事件：初始化，接口是GE5/2/2，显示具体的session信息(堆叠设备)*

\*Dec  1 16:43:12:880 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state INVALID, EVENT =INIT, Interface=GE5/2/2, VRF=0, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=INVALID, UserID=0xffffffff, Service node=chassis 1 slot 5 cpu 0.

*//状态机事件处理：无效状态，事件：初始化，接口是GE5/2/2，显示具体的session信息*

\*Dec  1 16:43:12:880 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state INIT, EVENT =AUTH, Interface=GE5/2/2, VRF=0, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=INVALID, UserID=0xffffffff, Service node=slot 5 cpu 0.

*//状态机事件处理：初始状态，事件：认证请求，接口是GE5/2/2，显示具体的session信息*

\*Dec  1 16:43:12:880 2013 Sysname IPOE/7/TIMER: -MDC=1-Slot=5;

Created a timer(TID=3), which will expire in 600s.

*//创建一个定时器（定时器id是3），600秒钟后超时*

\*Dec  1 16:43:12:880 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

Session authentication info: domain=radius.

*//session认证信息：域* *是 radius*

\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

AAA processed authentication requests and returned success.

*//接收到AAA的认证回应结果是成功*

\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

AAA processed authorization requests and returned success.

*//AAA处理授权请求返回结果是成功*

\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state AUTH, EVENT = AUTHPASS, Interface = GE5/2/2, VRF=1, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=AUTH, UserID=0xffffffff, Service node=slot 5 cpu 0..

*//状态机事件处理：触发，事件：认证通过，接口是GE5/2/2，显示具体的session信息*

\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state AUTHPASS, EVENT=ASSIGNIP, Interface=GE5/2/2, VRF=1, IP =1.2.3.4, Type=UNKNOWN-IP-PKT, State=AUTHPASS, UserID=0xffffffff, Service node=slot 5 cpu 0.

*//状态机事件处理：认证通过状态，事件：分配ip地址，接口是GE5/2/2，显示具体的session信息*

\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/TIMER: -MDC=1-Slot=5;

Deleted a timer(TID=3)

*//删除一个定时器（定时器id是3）*

\*Dec  1 16:43:12:883 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

Rule thread processed request message(MessageType=0).

*//rule线程处理请求下发userprofile消息（消息类型是0）*

\*Dec  1 16:43:12:883 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

Requested to add a user-profile rule(UserID=0x30000007).

*//请求添加userprofile规则（用户id是0x30000007）*

\*Dec  1 16:43:12:886 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

Received result of user profile settings(UserID=0x30000007, Result=0).

*//接收设置userprofile的结果（用户id是0x30000007，结果是0）*

\*Dec  1 16:43:12:888 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, EVENT = USERPROFILE OK, Interface=GE5/2/2, VRF= 1, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=ASSIGNEDIP, UserID=0x30000007, Service node=slot 5 cpu 0.

*//状态机事件处理：触发，事件：下发userprofile成功，接口是GE5/2/2，显示具体的session信息*

\*Dec  1 16:43:12:888 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state ASSIGNEDIP, EVENT=USERPROFILE OK, Interface= GE5/2/2, VRF=1, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=ASSIGNEDIP, UserID=0x30000007, Service node=slot 5 cpu 0

*//状态机事件处理：分配IP状态，事件：下发userprofile成功，接口是GE5/2/2，显示具体的session信息*

\*Dec  1 16:43:12:890 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

Added an ARP entry successfully, Interface=GE5/2/2, VRF=1, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=ONLINE, UserID=0x30000007, Service node=slot 5 cpu 0.

*//添加ARP规则成功*

\*Dec  1 16:43:12:890 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

AAA processed accounting-start requests and returned success.

*//AAA处理计费开始请求，返回结果是处理成功*

\*Dec  1 16:43:12:890 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

Added a detection user successfully, Interface=GigabitEthernet5/2/2, IP=1.2.3.4, VLAN=65535, CVLAN=65535.

*//添加探测用户成功*

\*Dec  1 16:43:12:890 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;

Sent mcast user online message.

*//发送组播用户在线消息*

\*Dec  1 16:43:12:891 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=1;

 User ID            : 0x30000007

 Flag               : 23

 Interface          : GE1/0/1

 VPN instance       : 1

 Src IP             : 1.2.3.4

 PVC ID             : 0

 SVLAN ID           : N/A

 CVLAN ID           : N/A

 MAC address        : aaaa-aaaa-aaaa

 Service type       : 0

 Access limit       : 4

 User profile       : a

 User name          : 1.2.3.4

 User name len      : 7

 Max multicast num  : 0

*// 打印传给可控组播的消息*

**IPoE调试命令 \-- IPoE调试命令 \-- debugging ipv6 subscriber**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 subscriber **[{ **all** \| **error** \| **event** \| **timer** }]]

**[undo debugging ipv6 subscriber **[{ **all** \| **error** \| **event** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示IPoE的所有调试信息开关

**[error**]：表示IPoE的错误调试信息开关。

**[event**]：表示IPoE的事件调试信息开关。

**[timer**]：表示IPoE的定时器调试信息开关。

【描述】

**[debugging ipv6 subscriber**]命令用来打开基于IPv6协议的IPoE的调试信息开关。**undo debugging ipv6 subscriber**命令用来关闭基于IPv6协议的IPoE的调试信息开关。

缺省情况下，基于IPv6协议的IPoE的调试信息开关处于关闭状态。

需要注意的是，与IPv4协议的IPoE的调试信息开关相同的信息以下不再列出，可参考"1.1.1  (?1845972079#_Ref380667585)debugging ip subscriber(?1845972079#_Ref380667589)"输出信息描述表。

表1-4 debugging ipv6 subscriber error命令输出信息描述表

字段

描述

Failed to receive an ICMPv6 reply..

接收到错误的ICMPv6回应报文

Failed to receive info from an ICMP6 reply.

从ICMPv6回复报文中提取信息失败

Failed to reconnect to ND and returned Code = *code**.

重连ND失败.返回值为*code*

Failed to select srcAddr6: Interface=interface: IP=ip, VLAN=vlan, CVLAN=cvlan.

选择IPv6源地址失败

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Failed to send an ICMP6 packet: Interface=*interface*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

发送ICMPv6报文失败

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Failed to get ND refresh time: Interface=*interface*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

获取ND表项时间戳失败

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Invalid DHCPv6 message (hop=*hop*).

非法的DHCPv6消息（跳数为*hop*）

Invalid DHCPv6 Relay message (level=*level*, length=*len*).

非法的DHCPv6中继消息（值为*level*，协议长度为*len*）

**

表1-5 debugging ip subscriber event命令输出信息描述表

字段

描述

Added a ND rule successfully: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

添加一条ND规则成功

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Deleted a ND rule successfully, IP=*ip*.

删除一条ND规则成功，IP地址为IP

Deleted a session by DHCPv6 event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*

因DHCPv6事件删除session

·Interface：接口名

·VPN：VPN索引

·IP：用户的IP地址

·Type：IPoE会话的创建类型，包括以下取值：

¡INVALID：无效类型

¡IF-LEASE：接口专线

¡SUBNET-LEASE：子网专线

¡STATIC：静态配置

¡DHCP-PKT：DHCP报文触发创建

¡UNKNOWN-IP-PKT：未知源IP报文触发创建

¡RS-PKT：RS报文触发创建

·State：会话状态，包括以下取值：

¡INVALID：无效状态

¡INIT：初始化

¡OFFLINE：正在下线中

¡AUTH：认证中

¡AUTHFAIL：认证失败

¡AUTHPASS：认证成功

¡ASSIGNEDIP：会话已具备IP地址

¡ONLINE：用户在线

¡BACKUP：备份状态

¡UNKNOWN：未知状态

·UserID：用户ID

·Service node：服务板卡号

Sent an NS packet successfully: Interface=interface, IP=ip, VLAN=vlan, CVLAN =cvlan.

发送NS报文成功

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Sent an ICMP6 packet successfully: Interface=*interface*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

发送ICMPv6报文成功.

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

Received an ICMP6 reply: Interface=*interface*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.

接收ICMPv6回复报文

·Interface：接口名

·IP：用户的IP地址

·VLAN：外层VLAN ID

·SecVLAN：内层VLAN ID

【举例】

\# 打开基于IPv6协议的IPoE的所有调试信息开关。配置静态IPv6 IPoE会话，当接口GigabitEthernet1/0/1上收到对应的IPv6报文时，设备上将打印如下调试信息。

\<Sysname\> terminal monitor

\<Sysname\> terminal debugging

\<Sysname\> debugging ipv6 subscriber all

\<Sysname\>\*Dec  1 17:23:05:900 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=1; FSM EVT: Trigger, EVENT=CREATEANDGO, Interface=GE5/2/2, VRF=65535, IP=2::1, Type=STATIC, State=INVALID, UserID=0xffffffff, Service node=0x8000.

*// 状态机事件处理：触发，事件：命令行配置，接口是GE1/0/1，显示具体的会话信息*

\*Dec  1 17:23:05:900 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state INVALID, EVENT=CREATEANDGO, Interface=GE5/2/2, VRF=65535, IP=2::1, Type=STATIC, State=INVALID, UserID=0xffffffff, Service node=0x8000..

*[//*]*状态机事件处理：无效状态，事件：命令行配置，接口是GE1/0/1，显示具体的会话信息*

\*Dec  1 17:23:25:683 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Started to authen

ticate unclassified IP packets from 2::1.

*// 接收IPv6地址为2::1的IPv6报文*

\*Dec  1 17:23:25:684 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, EVENT = AUTH, Interface=GE5/2/2, VRF=65535, IP=2::1, Type=STATIC, State=INIT, UserID=0xffffffff, Service node=slot 5 cpu 0..

*// 状态机事件处理：触发，事件：认证请求，接口是GE1/0/1，显示具体的会话信息*

\*Dec  1 17:23:25:685 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state INIT, EVENT =AUTH, Interface=GE5/2/2, VRF=65535, IP=2::1, Type=STATIC, State=INIT, UserID=0xffffffff, Service node=slot 5 cpu 0.

*// 状态机事件处理：初始状态，事件：认证请求，接口是GE1/0/1，显示具体的会话信息*

\*Dec  1 17:23:25:685 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Session authentication info: domain=radius.

*// 会话认证信息：认证域* *是 radius*

\*Dec  1 17:23:25:686 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; AAA processed authentication requests and returned success.

*// 接收到AAA的认证回应结果是成功*

\*Dec  1 17:23:25:686 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; AAA processed authorization requests and returned success.

*[// AAA*]*处理授权请求返回结果是成功*

\*Dec  1 17:23:25:686 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state AUTH, EVENT=AUTHPASS, Interface=GE5/2/2, VRF=0, IP=2::1, Type=STATIC, State=AUTH, UserID=0xffffffff, Service node=slot 5 cpu 0.

*// 状态机事件处理：状态是认证中，事件：认证成功，接口是GE1/0/1，显示具体的会话信息*

\*Dec  1 17:23:25:687 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state AUTHPASS, EVENT=ASSIGNIP, Interface=GE5/2/2, VRF=0, IP=2::1, Type=STATIC, State=AUTHPASS, UserID=0xffffffff, Service node=slot 5 cpu 0.

*// 状态机事件处理：状态是认证成功，事件：分配ip地址，接口是GE1/0/1，显示具体的会话信息*

\*Dec  1 17:23:25:688 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Rule thread processed request message (MessageType=0).

*[// rule*]*线程处理请求下发userprofile消息（消息类型是0）*

\*Dec  1 17:23:25:688 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Requested to add a user-profile rule(UserID=0x40000001).

*// 请求添加userprofile规则（用户id是0x40000001）*

\*Dec  1 17:23:25:691 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5;

Received result of user profile settings (UserID=0x40000001, Result=0).

*// 接收设置userprofile的结果（用户id是0x40000001，结果是0）*

\*Dec  1 17:23:25:693 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, EVENT=USERPROFILE OK, Interface=GE5/2/2, VRF=0, IP=2::1, Type=STATIC, State=ASSIGNEDIP, UserID=0x40000001, Service node=slot 5 cpu 0.

*// 状态机事件处理：触发，事件：userprofile下发成功，接口是GE1/0/1，显示具体的会话信息*

\*Dec  1 17:23:25:693 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state ASSIGNEDIP, EVENT=USERPROFILE OK, Interface=GE5/2/2, VRF=0, IP =2::1, Type=STATIC, State=ASSIGNEDIP, UserID=0x40000001, Service node=slot 5 cpu 0.

*// 状态机事件处理：分配到ip地址状态，事件：userprofile下发成功，接口是GE1/0/1，显示具体的会话信息*

\*Dec  1 17:23:25:696 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; AAA processed accounting-start requests and returned success..

*[// AAA*]*处理计费开始请求，返回结果是处理成功*

Added a detection user successfully, Interface=GigabitEthernet5/2/2, IP=2::1, VLAN=65535, CVLAN=65535.

*// 添加探测用户成功*

\*Dec  1 17:23:25:697 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Sent mcast user online message.

*// 发送组播用户在线消息*

\*Dec  1 17:23:25:697 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=1;

 User ID            : 0x40000001

 Flag               : 21

 Interface          : GE1/0/1

 VPN instance       : N/A

 Src IP             : 2::1

 PVC ID             : 0

 SVLAN ID           : N/A

 CVLAN ID           : N/A

 MAC address        : N/A

 Service type       : 0

 Access limit       : 4

 User profile       : a

 User name          : a

 User name len      : 1

 Max multicast num  : 0

*// 打印传给可控组播的消息*
