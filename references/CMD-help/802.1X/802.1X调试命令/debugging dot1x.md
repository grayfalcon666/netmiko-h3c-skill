<!-- CMD-INDEX
  debugging dot1x                     | 用户视图             | L5
-->

**802.1X \-- 802.1X调试命令 \-- debugging dot1x**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging dot1x**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging dot1x**[ { **all** \| **error** \| **event** \| **packet** }]]

分布式设备：

**[debugging dot1x**[ { **all** \| **error** \| **event** \| **packet** } [ **slot** *slot-number* ]]]

**[undo debugging dot1x**[ { **all** \| **error** \| **event** \| **packet** } [ **slot** *slot-number* ]]]

分布式IRF设备：

**[debugging dot1x**[ { **all** \| **error** \| **event** \| **packet** } ]**chassis** *chassis-number***slot** *slot-number* ]

**[undo debugging dot1x**[ { **all** \| **error** \| **event** \| **packet** } ]**chassis** *chassis-number***slot** *slot-number* ]

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

**[slot ***slot-mumber*]：表示指定单板的调试信息开关，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-mumber*]：表示指定成员设备的调试信息开关，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-mumber*]：表示指定成员设备/PEX的调试信息开关，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：表示成员设备上指定单板的调试信息开关。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：表示指定单板的调试信息开关。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【描述】

**[debugging dot1x**]命令用来打开802.1X调试信息开关。**undo debugging dot1x**命令用来关闭802.1X调试信息开关。

缺省情况下，802.1X调试信息开关处于关闭状态。

表1-1 debugging dot1x error命令输出信息描述表

字段

描述

Failed to set unknown source MAC action on *interface-type interface-num.*

在接口*interface-type interface-num*上设置未知源MAC地址动作失败

Failed to find user by *mac* and *interface-type interface-num* when receiving authenticate response.

收到认证回应消息时，根据MAC地址*mac*和接口名*interface-type interface-num*无法找到对应的用户

Failed to find user by *mac* and *interface-type interface-num* when receiving authorization response.

收到授权回应消息时，根据MAC地址*mac*和接口名*interface-type interface-num*无法找到对应的用户

Failed to find user by *mac* and *interface-type interface-num* when receiving accounting response.

收到计费回应消息时，根据MAC地址*mac*和接口名*interface-type interface-num*无法找到对应的用户

Failed to set enable protocol packet to CPU.

设置使能协议报文上送CPU失败

Failed to open packet socket.

打开报文socket失败

Failed to set LogicState on *if_name*,*error_code*

在接口*interface-type interface-num*上设置接口逻辑状态失败，错误码为*error_code*

Failed to allocate memory for EAP challenge request.

为EAP challenge请求分配内存失败

Invalid password length.

密码长度无效

Failed to allocate memory for EAP Identifier request.

为EAP Identity请求分配内存失败

PAE entering Abort for BE process failed.

BE进程失败，PAE异常退出

Failed to process message for the message type is invalid.

消息类型无效，处理失败

Failed to accept connection on the global known port.

在全局知名端口接收连接失败

Failed to process the Set request message for the data type is invalid.

处理Set请求消息失败，数据类型无效

Failed to process the Get request message for the data type is invalid.

处理Get请求消息失败，数据类型无效

Failed to process the Getnext request message for the data type is invalid.

处理Getnext请求消息失败，数据类型无效

Failed to process the Getbulk request message for the data type is invalid.

处理Getbulk请求消息失败，数据类型无效

Failed to process the request message for the operation type is invalid.

处理请求消息失败，操作类型无效

Failed to connect to master.

连接到主控板失败

Failed to add socket to LPU connection table.

将socket加入长连接链表失败

The data type of Pull message is invalid.

Pull消息数据类型无效

The interface is invalid.

接口无效

Failed to get interface link status.

获取接口连接状态失败

The identifier is unmatched.

认证报文不匹配

Dropped received EAP packet for the packet length is invalid.

丢弃接收到的EAP报文，报文长度无效

Dropped received EAP packet for the packet is empty.

丢弃接收到的EAP报文，报文内容为空

Failed to get statistics.

获取统计信息失败

Invalid protocol version ID.

无效的协议版本ID

There is no EAP request  from authentication server.

没有来自于认证服务器的EAP请求

Failed to create a user timer.

创建用户定时器失败

User Failed to start acct-update period timer when receiving acct-start response terminate user session

当用户正在接收计费开始回应结束用户会话时，用户不能启动计费更新周期定时器

Invalid server string length *length.*

服务器下发的String属性信息长度非法，为*length*

Dropped received logoff packet for VLAN is not match, packet VLAN is *vlan-id*, user VLAN is *vlan-id*.

丢弃VLAN不匹配的logoff报文，报文所属VLAN为*vlan-id*，用户所属VLAN为*vlan-id*

Failed to allocate memory for EAP Notification request.

为EAP Notification请求报文分配内存失败

Failed to check smarton packet because of invalid prefix.

检查smarton报文失败，原因是前缀不合法

Failed to check smarton packet because of unmatched MD5 digest.

检查smarton报文失败，原因是MD5摘要不匹配

Failed to check smarton packet because of no switch ID information.

检查smarton报文失败，原因是报文中未携带设备ID

Failed to check smarton packet because of unmatched switch ID length.

检查smarton报文失败，原因是设备ID长度不匹配

Failed to check smarton packet because of unmatched switch ID.

检查smarton报文失败，原因是设备ID不匹配

Failed to check smarton packet because of no ID or Password information.

检查smarton报文失败，原因是报文中未携带设备ID或密码

Failed to check smarton packet bacause of invalid MD5 digest length.

检查smarton报文失败，原因是MD5摘要长度不匹配

Failed to check hash information.

检查hash信息失败

Failed to check smarton packet because of no device switch-ID or MD5 digest.

检查smarton报文失败，原因是设备上未配置Swich ID或未生成MD5摘要

表1-2 debugging dot1x event命令输出信息描述表

字段

描述

Got accounting-stop response by *mac* and *interface-type interface-num*, RespCode=*RespCode.*

通过MAC地址*mac*和接口名*interface-type interface-num*获取停止计费信息，响应码为*RespCode *

*[Interface-type interface-num* is redundant.]

接口*interface-type interface-num*多余

Received EAP Request packet.

接收到EAP请求消息的报文

Received EAP Success packet.

接收到EAP成功消息的报文

Received EAP Failure packet.

接收到EAP失败消息的报文

Received EAP packet of unknown type.

接收未知类型的报文

Sending EAP Packet (identifier *identifier*, type *type*)

正在发送EAP报文（匹配标识为*identifier*，类型为*type*）

Processing If_Delete event:

正在处理删除接口事件

Processing If_Deactive event:

正在处理接口去激活事件

Processing If_Active event:

正在处理接口激活事件

Processing If_Down event:

正在处理接口Down事件

Processing If_Up event:

正在处理接口Up事件

Multicasted Identity Request packets on interface *interface-type interface-num* of VLAN vlan-id.

在处于VLAN *vlan-id*中的接口*interface-type interface-num*上组播发送EAP Identity请求报文

Multicasted Identity Request packets on interface *interface-type interface-num.*

在接口*interface-type interface-num*上组播发送EAP Identity请求报文

PORT_SM*interface-type interface-num* entering init state\...

端口状态机进入初始状态

PORT_SM*interface-type interface-num* entering author-force state\...

端口状态机进入强制授权状态

PORT_SM*interface-type interface-num* entering unauthor-force state\....

端口状态机进入非强制授权状态

PORT_SM*interface-type interface-num* entering disconnected state\....

端口状态机进入断开连接状态

PORT_SM*interface-type interface-num* entering disconnected state\....

端口状态机进入断开连接状态

PORT_SM*interface-type interface-num* entering authenticating state\....

端口状态机进入正在认证状态

PORT_SM*interface-type interface-num* entering authored state\....

端口状态机进入已经授权的状态

PORT_SM*interface-type interface-num* received *event* event *t*

端口状态机接收事件*event*

Global switch or interface switch is off.

未打开全局或接口开关

Processing HA UPGRADE event.

正在处理HA升级事件

Processing HA DEGRADE event .

正在处理HA降级事件

Failed to find the specified unauthor user.

查找指定非授权用户失败

Reconnect timer timeout, reconnecting to mpu

重连定时器超时，向mpu重新发起连接

Successfully connected to master, closed reconnect timer.

成功连接到主控板，关闭重连接定时器

Processing the event of IFEVENT.

正在处理接口事件

Create reconnect timer successfully

成功创建重连接定时器

Failed to create reconnect timer

创建重连接定时器失败

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed authentication request and returned Processing.

对于用户（MAC地址为*mac*，所属VLAN ID为*vlan*，接入端口为*interface-type interface-num*），AAA处理认证请求并返回正在处理的结果

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed authorization request and returned Processing.

AAA处理授权请求并返回正在处理的结果

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed accounting request and returned Processing.

AAA处理计费请求并返回正在处理的结果

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed authentication request and returned Success.

AAA处理认证请求并返回成功的结果

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed authorization request and returned Success.

AAA处理授权请求并返回成功的结果

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed accounting request and returned Success.

AAA处理计费请求并返回成功的结果

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed authentication request and returned Failure code *code*.

AAA处理认证请求并返回失败的结果，错误码为*code*

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed authentication request and returned Continuing.

AAA处理认证请求并返回继续认证的结果

*mac*:VLAN*vlan*:*interface-type interface-num* AAA processed authorization request and returned Failure.

AAA处理授权请求并返回失败的结果

*mac*:VLANvlan: *interface-type interface-num* AAA processed accounting-update request and returned Failure.

AAA处理计费更新请求并返回失败的结果

Succeeding in notifying port-mode to 8021x thread.

端口模式下设置802.1X线程成功

BE is in Idle state

BE进入闲置状态

BE is in Initialize state

BE进入初始化状态

BE is in request state

BE进入请求状态

BE is in Response state

BE进入回应状态

BE is in Fail state

BE进入失败状态

User sent authentication request

用户发出认证请求

User sent authorization request

用户发出授权请求

User sent accounting-start request

用户发出开始计费请求

User sent accounting-stop request

用户发出停止计费请求

User sent accounting-update request

用户发出更新计费请求

Server timed out

服务器超时

PAE is in Initialize state

PAE处于初始化状态

PAE is in Disconnect state

PAE处于断开连接状态

PAE is in Connecting state

PAE处于连接状态

PAE is in Authenticating state

PAE进入正在认证状态

PAE is in Authenticated state

PAE进入认证状态

PAE is in Aborting state

PAE进入丢弃状态

PAE is in Held state

PAE进入Held状态

PAE is in Restart state

PAE进入重启状态

Failed to create server timeout timer

创建服务器超时定时器失败

Create server timeout timer successfully

创建服务器超时定时器成功

Processing new mac event

处理新mac事件

Notified Portsec of new mac result:

通知端口安全新mac的结果

Processing the event of unauthor

处理unauthor事件

Processing the event of IfVlanDel

处理ifvlanDel事件

Processing the event of AuthenFail

处理认证失败事件

Notified PortSec of AuthenFail result:

通知端口安全认证失败结果

The maximum number of accounting attempts has been reached

达到最大计费尝试次数

AAA processed accounting-update request and returned processing

AAA处理计费更新请求并返回正在处理

AAA processed accounting-update request and returned success

AAA处理计费更新请求并返回成功

AAA processed accounting-update request and returned fail

AAA处理计费更新请求并返回失败

User received authentication response

用户收到认证回应

AAA processed authorization request and returned processing

AAA处理授权请求并返回正在处理

AAA processed authorization request and returned sucess

AAA处理授权请求并返回成功

AAA processed authorization request and returned fail

AAA处理授权请求并返回失败

*mac*:VLAN*vlan*: *interface-type interface-num* Delete User from critical vlan *c-vlan*.

用户（MAC地址为*mac*，所属VLAN ID为*vlan*，接入端口为*interface-type interface-num*）退出Critical VLAN *c-vlan*

*mac*:VLAN*vlan*: *interface-type interface-num* Succeeded to add User to critical vlan *c-vlan*.

用户成功加入Critical VLAN *c-vlan*

*mac*:VLAN*vlan*: *interface-type interface-num* Failed to add User to critical *c-vlan*.

用户加入Critical VLAN *c-vlan*失败

Receive Unknown IP type.

收到不能识别的IP类型

*mac*:VLAN*vlan*: *interface-type interface-num* Delete User from auth-fail vlan *a-vlan*.

用户退出Auth-Fail VLAN *a-vlan*

*mac*:VLAN*vlan*: *interface-type interface-num*  Succeeded to add User to auth-fail vlan *a-vlan*.

用户成功加入Auth-Fail VLAN *a-vlan*

*mac*:VLAN*vlan*: *interface-type interface-num* Failed to add User to auth-fail vlan *a-vlan*.

用户加入Auth-Fail VLAN *a-vlan*失败

*mac*:VLAN*vlan*: *interface-type interface-num* Delete User from guest vlan *a-vlan*.

用户退出Guest VLAN *a-vlan*

*mac*:VLAN*vlan*: *interface-type interface-num* Succeeded to add User to guest vlan *vlan*.

用户成功加入Guest VLAN

*mac*:VLAN*vlan*: *interface-type interface-num* Failed to add User to guest vlan *vlan*.

用户加入Guest VLAN失败

Succeed to get hash information from server.

成功从服务器获取hash信息

Succeeded to send smarton notification-request packet.

成功发送SmartOn notification-request报文

Succeeded to check smarton notification-response.

成功检查SmartOn notification-response报文

*interface-type interface-num*EAP-REQ/ID Multicast timed out.

组播发送EAP-REQ/ID报文超时

表1-3 debugging dot1x packet命令输出信息描述表

字段

描述

Received a packet on interface *interface-type interface-num*

\-\--Verbose information of the packet\-\--

Destination Mac Address: *dst-mac*

Source Mac Address: *src-mac*

Mac Frame Type: *fram-type*

Protocol Version ID: *version-id*

Packet Type: *type-num*

Packet Length: *length*

接收来自接口*interface-type interface-num*的报文，包括如下信息：

·源MAC地址

·目的MAC地址

·MAC帧类型

·协议版本号

·报文类型

·报文长度

【举例】

\# 在一台启动了802.1X功能的设备上，打开802.1X所有调试功能。当有802.1X用户上线时，将输出以下调试信息。

\<Sysname\> debugging dot1x all

\*Jan  1 02:44:12:154 2011 Sysname 802.1X/7/PACKET:

Received a packet on interface GE1/0/1/1.

\-\--Verbose information of the packet\-\--

Destination Mac Address: 0180-c200-0003

Source Mac Address: 1cbd-b9e3-b0ed

Mac Frame Type: 888e

Protocol Version ID: 1

Packet Type: 1

Packet Length: 0

*// 接口Gigabitethernet1/0接收了一个报文*

\*Jan  1 02:44:12:156 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 PAE is in Disconnect state.

*[// PAE*]*进入断开连接状态*

\*Jan  1 02:44:12:157 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 BE is in Initialize state.

*[// PAE*]*进入初始状态*

\*Jan  1 02:44:12:158 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 PAE is in Restart state.

*[// PAE*]*进入重启状态*

\*Jan  1 02:44:12:159 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 BE is in Idle state.

*[// BE*]*进入Idle状态*

\*Jan  1 02:44:12:160 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 PAE is in Connecting state.

*[// PAE*]*进入连接状态*

\*Jan  1 02:44:12:161 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 PAE is in Authenticating state.

*[// PAE*]*进入认证状态*

\*Jan  1 02:44:12:162 2011 Sysname 802.1X/7/EVENT:

PORT_SM[GE1/0/1 received event DOT1X_PSM_E_START_AUTH.]

*// 接口接收到DOT1X_PSM_E_START_AUTH事件*

\*Jan  1 02:44:12:163 2011 Sysname 802.1X/7/EVENT:

PORT_SM[GE1/0/1 entering authenticating state\...]

*// 接口进入认证状态*

\*Jan  1 02:44:12:166 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 BE is in Request state.

*[// BE*]*进入请求状态*

\*Jan  1 02:44:12:166 2011 Sysname 802.1X/7/EVENT:

Sending EAP Packet (identifier 1, type 1)

*// 正在发送EAP报文（匹配标识为1，类型为1）*

\*Jan  1 02:44:12:170 2011 Sysname 802.1X/7/PACKET:

Transmitted a packet on interface GE1/0/1.

\-\--Verbose information of the packet\-\--

Destination Mac Address: 1cbd-b9e3-b0ed

Source Mac Address: 00e0-fc00-5830

Mac Frame Type: 888e

Protocol Version ID: 1

Packet Type: 0

Packet Length: 5

\-\-\-\--Packet Body\-\-\-\--

Code: 1

Identifier: 1

Length: 5

*// 接口Gigabitethernet1/0发送了一个报文*

\*Jan  1 02:44:12:174 2011 Sysname 802.1X/7/PACKET:

Received a packet on interface GE1/0/1.

\-\--Verbose information of the packet\-\--

Destination Mac Address: 0180-c200-0003

Source Mac Address: 1cbd-b9e3-b0ed

Mac Frame Type: 888e

Protocol Version ID: 1

Packet Type: 0

Packet Length: 16

\-\-\-\--Packet Body\-\-\-\--

Code: 2

Identifier: 1

Length: 16

*// 接口Gigabitethernet1/0接收了一个报文*

\*Jan  1 02:44:12:175 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 BE is in Response state.

*[// BE*]*进入响应状态*

\*Jan  1 02:44:12:176 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Create server timeout timer successfully.

*// 成功创建服务器超时定时器*

\*Jan  1 02:44:12:178 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 BE is in Request state.

*[// BE*]*进入请求状态*

\*Jan  1 02:44:12:178 2011 Sysname 802.1X/7/EVENT:

Sending EAP Packet (identifier 2, type 4)

*// 正在发送EAP报文（匹配标识为2，类型为4）*

\*Jan  1 02:44:12:183 2011 Sysname 802.1X/7/PACKET:

Transmitted a packet on interface GE1/0/1.

\-\--Verbose information of the packet\-\--

Destination Mac Address: 1cbd-b9e3-b0ed

Source Mac Address: 00e0-fc00-5830

Mac Frame Type: 888e

Protocol Version ID: 1

Packet Type: 0

Packet Length: 22

\-\-\-\--Packet Body\-\-\-\--

Code: 1

Identifier: 2

Length: 22

*// 接口Gigabitethernet1/0/1发送了一个报文*

\*Jan  1 02:44:12:185 2011 Sysname 802.1X/7/PACKET:

Received a packet on interface GE1/0/1.

\-\--Verbose information of the packet\-\--

Destination Mac Address: 0180-c200-0003

Source Mac Address: 1cbd-b9e3-b0ed

Mac Frame Type: 888e

Protocol Version ID: 1

Packet Type: 0

Packet Length: 33

\-\-\-\--Packet Body\-\-\-\--

Code: 2

Identifier: 2

Length: 33

*// 接口Gigabitethernet1/0/1接收了一个报文*

\*Jan  1 02:44:12:186 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 BE is in Response state.

*[// BE*]*进入响应状态*

\*Jan  1 02:44:12:187 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 Create server timeout timer successfully.

*// 成功创建服务器超时定时器*

\*Jan  1 02:44:12:190 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 User sent authentication request.

*// 用户发送认证请求*

\*Jan  1 02:44:12:191 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 AAA processed authentication request and returned Processing.

*[// AAA*]*处理认证请求并返回正在处理的结果*

\*Jan  1 02:44:12:205 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 User received authentication response, RespCode=0.

*// 用户收到认证响应，响应码为0*

\*Jan  1 02:44:12:206 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1: GE1/0/1 BE is in Success state.

*[// BE*]*进入成功状态*

\*Jan  1 02:44:12:211 2011 Sysname 802.1X/7/PACKET:

Transmitted a packet on interface GE1/0/1.

\-\--Verbose information of the packet\-\--

Destination Mac Address: 1cbd-b9e3-b0ed

Source Mac Address: 00e0-fc00-5830

Mac Frame Type: 888e

Protocol Version ID: 1

Packet Type: 0

Packet Length: 4

\-\-\-\--Packet Body\-\-\-\--

Code: 3

Identifier: 3

Length: 4

*// 接口Gigabitethernet1/0/1发送了一个报文*

\*Jan  1 02:44:12:212 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 PAE is inAuthenticated state.

*[// PAE*]*进入认证状态*

\*Jan  1 02:44:12:213 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 User sent authorization request.

*// 用户发送授权请求*

\*Jan  1 02:44:12:214 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 AAA processed authorization request and returned Success.

*[// AAA*]*处理授权请求并返回成功的结果*

\*Jan  1 02:44:12:216 2011 Sysname 802.1X/7/EVENT:

PORT_SM[GE1/0/1 received event DOT1X_PSM_E_USER_AUTHORED.]

*// 接口接收到DOT1X_PSM_E_USER_AUTHORED事件*

\*Jan  1 02:44:12:219 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 User sent accounting-start request.

*// 用户发送计费开始请求*

\*Jan  1 02:44:12:220 2011 Sysname 802.1X/7/EVENT:

PORT_SM[GE1/0/1 received event DOT1X_PSM_E_END_AUTH.]

*// 接口接收到DOT1X_PSM_E_END_AUTH事件*

\*Jan  1 02:44:12:222 2011 Sysname 802.1X/7/EVENT:

PORT_SM[GE1/0/1 entering disconnected state\...]

*// 接口进入断开连接状态*

\*Jan  1 02:44:12:583 2011 Sysname 802.1X/7/EVENT:

1cbd-b9e3-b0ed:VLAN1:GE1/0/1 BE is in Idle state.

*[// BE*]*进入Idle状态*

**
