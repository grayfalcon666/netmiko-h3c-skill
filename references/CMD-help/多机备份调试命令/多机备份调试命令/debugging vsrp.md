<!-- CMD-INDEX
  debugging vsrp                      | 用户视图             | L8
  debugging ppp vsrp                  | 用户视图             | L90
  debugging pppoe-server vsrp         | 用户视图             | L334
  debugging l2tp vsrp                 | ]                | L520
-->

**多机备份调试命令 \-- 多机备份调试命令 \-- debugging vsrp**

------------------------------------------------------------------------

【命令】

**[debugging vsrp**]

**[undo debugging vsrp**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging vsrp**]命令用来打开多机备份调试信息开关。**undo debugging vsrp**命令用来关闭多机备份调试信息开关。

缺省情况下，多机备份调试信息开关处于关闭状态。

表1-1 debugging vsrp命令输出信息列表

字段

含义

The node with backup ID *backup-id* was deleted from the retransmission list: data length*: data-length*, list node total number: *total-num*, VSRP peer name*: peer-name*.

删除重传链中编号为*backup-id*结点，该结点数据长度为*data-length*，该重传链结点个数为*node-num*，该重传链所属的VSRP对端名为：*peer-name*

The node with backup ID *backup-id* was refreshed in the retransmission list: data length: *data-length*, list node total number: *total-num*, VSRP peer name: *peer-name*.

更新重传链中编号为*backup-id*结点，该结点数据长度为*data-length*，该重传链结点个数为*node-num*，该重传链所属的VSRP对端名为：*peer-name*

The status of VSRP instance name *instance-name* changed to *new-status*.

VSRP实例*instance-name*的状态变化为*new-status*，状态取值包括：

·Master：表示主用设备

·Backup：表示备用设备

·Down：表示设备不可用

The TCP connection status of VSRP peer *peer-name* changed, new TCP connection status: *tcp-status*.

VSRP对端*peer-name*的TCP状态变为*tcp-status*，取值包含：

·Disconnected：连接已断开

·Connected：连接已建立

【举例】

\# 刷新多机备份对端pname内Backup ID为207的重传链结点。

\<Sysname\> debugging vsrp

\<Sysname\> \*May 25 10:26:08:418 2013 Sysname VSRP/7/DEBUG: -MDC=1; The node with backup ID 207 was refreshed in the retransmission list, data length: 20, list node total number: 1024, VSRP peer name: pname.

\# VSRP 对端pname的TCP状态由Connetced变成Disconnected。

\<Sysname\> debugging vsrp

\<Sysname\> \*May 25 09:06:11:953 2013 H3C VSRP/7/DEBUG: -MDC=1; The TCP connection status of

 VSRP peer pname changed, new TCP connection status: Disconnected.

\# VSRP 实例aaa的状态变成Down。

\<Sysname\> debugging vsrp

\<Sysname\> \*May 25 09:11:44:649 2013 H3C VSRP/7/DEBUG: -MDC=1; The status of VSRP

instance name aaa changed to Down.

**多机备份调试命令 \-- PPPoE支持多机备份功能调试命令 \-- debugging ppp vsrp**

------------------------------------------------------------------------

【命令】

**[debugging ppp vsrp**]

**[undo debugging ppp vsrp**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

**[debugging ppp vsrp**]命令用来打开PPP的多机备份调试信息开关。**undo debugging ppp vsrp**命令用来关闭PPP的多机备份调试信息开关。

缺省情况下，PPP的多机备份调试信息开关处于关闭状态。

表1-2 debugging ppp vsrp命令输出信息描述表

字段

描述

Received a bind VSRP event: interface=*interface-name*, VSRP instance=*vsrp-instance-name*.

PPP收到接口绑定事件，接口*interface-name*绑定的多机备份实例名为*vsrp-instance-name*

Received an unbind VSRP event: interface=*interface-name*, VSRP instance=*vsrp-instance-name*.

PPP收到接口去绑定事件，接口*interface-name*去绑定的多机备份实例名为*vsrp-instance-name*

Received a VSRP status event: VSRP instance=*vsrp-instance-name*, from *OldStatus* to *NewStatus.*

PPP收到实例*vsrp-instance-name*状态变化事件，其中*OldStatus*和*NewStatus*类型如下：

·Master：实例状态为主

·Backup：实例状态为备

·Down：实例状态为不运行

Received a VSRP mode event: VSRP instance=*vsrp-instance-name*, from *OldMode* to *NewMode.*

PPP收到实例*vsrp-instance-name*备份模式变化事件信息，其中*OldMode*和*NewMode*类型如下：

·Hot：热备份

·Warm：温备份

·N/A：未知备份模式

Received a VSRP NAS IP event: VSRP instance=*vsrp-instance-name*, from *OldAddr* to *NewAddr.*

PPP收到实例*vsrp-instance-name* NAS IP地址从*OldAddr*变为*NewAddr*事件信息

Received a VSRP NAS port event: VSRP instance=*vsrp-instance-name*, from *OldNasPortName to NewNasPortName.*

PPP收到实例*vsrp-instance-name* NAS端口从*OldNasPortName*变为*NewNasPortName*事件信息，NAS端口名为N/A表示未知NAS端口

Received a VSRP NAS ID event: VSRP instance=*vsrp-instance-name*, from *OldNasSysName to NewNasSysName.*

PPP收到实例*vsrp-instance-name* NAS ID从*OldNasSysName*变为*NewNasSysName*事件信息，NAS ID为N/A表示未知NAS ID

Received a VA up event: VA interface=*interface-name.*

PPP收到VA接口up事件信息

Received a VA down event: VA interface=*interface-name.*

PPP收到VA接口down事件信息

Succeeded to *operate* session node for VSRP instance *vsrp-instance-name*: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.

对多机备份实例下的会话操作成功，其中*number*为VLAN ID，取值为65535时表示不带VLAN tag

*[operate*]类型如下：

·create：创建

·delete：删除

·update：更新

Failed to *operate* session node for VSRP instance *vsrp-instance-name*: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.

对多机备份实例下的会话操作失败，其中*number*为VLAN ID，取值为65535时表示不带VLAN tag

*[operate*]类型如下：

·create：创建

·delete：删除

·update：更新

Sent *operate* PPP session message to *Device*: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.

发送PPP会话的*operate*消息给*Device*，其中*number*为VLAN ID，取值为65535时表示不带VLAN tag

*[operate*]类型如下：

·create：创建

·delete：删除

·update：更新

·update coa of：更新授权信息

·update flow of：更新流量信息

*[Device*]类型如下：

·primary device：主设备

·backup device：备设备

·master board：主控板

·IO board：接口板

Failed to recover PPP session on VA interface *interface-name* of VSRP instance *vsrp-instance-name*: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.

PPP模块恢复VA接口*interface-name*下指定会话失败，其中*number*为VLAN ID，取值为65535时表示不带VLAN tag

Failed to allocate memory to *operate* PPP session: session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.

*[operate* PPP]会话时分配内存失败，其中*number*为VLAN ID，取值为65535时表示不带VLAN tag

*[operate*]类型如下：

·create：创建

·update：更新

Primary thread *Result* to send *operate* session to worker thread: VA interface=*interface-name*, session ID=*id*, service VLAN=*number*, customer VLAN=*number*, MAC address=*mac-addr*.

PPP发送*operate*指定会话成功或失败信息，其中*number*为VLAN ID，取值为65535时表示不带VLAN tag。

*[operate*]类型如下：

·create：创建

·update：更新

·delete：删除

·activate：激活

·deactivate：去激活

·update coa of：更新授权信息

·update flow of：更新流量信息

*[Result*]类型如下：

·succeeded：成功

·failed：失败

VSRP *vsrp-instance-name*: Establishing TCP channel timed out.

PPP备份TCP通道重连超时

VSRP *vsrp-instance-name*: Successfully established VSRP TCP channel.

多机备份的备份TCP通道建立成功

VSRP *vsrp-instance-name*: Failed to establish VSRP TCP channel.

多机备份的备份TCP通道建立失败

VSRP *vsrp-instance-name*: Destroyed VSRP TCP channel.

销毁多机备份的备份TCP通道

VSRP *vsrp-instance-name*: Received a repeated VA up event.

重复收到VA up事件

Received a backup end event: VSRP instance=*vsrp-instance-name*..

PPP收到PPPoE通知的备份结束事件

Primary device sent a smooth start message to backup device: VSRP instance=*vsrp-instance-name*.

主设备发送平滑开始消息给备设备

Backup device received a smooth start message: VSRP instance=*vsrp-instance-name*.

备设备接收到主设备发送的平滑开始消息

Primary device sent a smooth end message to backup device: VSRP instance=*vsrp-instance-name*.

主设备发送平滑结束消息给备设备

Backup device received a smooth end message: VSRP instance=*vsrp-instance-name*.

备设备接收到主设备发送的平滑结束消息

Sent a backup end message to new primary device: VSRP instance=*vsrp-instance-name*.

备设备发送备份结束消息到新主设备

New primary device received a backup end message: VSRP instance=*vsrp-instance-name*.

新主设备接收到备设备发送的备份结束消息

Sent a batch deleting message to backup device: VSRP instance=*vsrp-instance-name*.

主设备发送批量会话删除消息到备设备

Received a batch deleting message: VSRP instance=*vsrp-instance-name*.

备设备收到主设备发送的批量会话删除消息

Backup device sent a smooth request message to primary device: VSRP instance=*vsrp-instance-name*.

备设备发送平滑请求消息到主设备

VSRP *vsrp-instance-name* started to allow access.

多机备份实例*vsrp-instance-name*允许用户上线

【举例】

\# 打开PPP的多机备份调试信息开关。IPCP协商通过后会创建会话，系统将输出下列调试信息。

\<Sysname\> debugging ppp vsrp

\*Jun 10 15:16:33:398 2013 Sysname PPP/7/VSRP: -MDC=1;Succeeded to create session node for VSRP instance 1: session ID=1, service VLAN=65535, customer VLAN=65535, MAC address=0050-56c0-0009.

*// 在多机备份实例1中成功创建了SID为1，MAC地址为0050-56c0-0009且不带VLAN tag的PPP会话*

**多机备份调试命令 \-- PPPoE支持多机备份功能调试命令 \-- debugging pppoe-server vsrp**

------------------------------------------------------------------------

【命令】

**[debugging pppoe-server vsrp**]

**[undo debugging pppoe-server vsrp**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

**[debugging pppoe-server vsrp**]命令用来打开PPPoE Server的多机备份调试信息开关。**undo debugging pppoe-server vsrp**命令用来关闭PPPoE Server的多机备份调试信息开关。

缺省情况下，PPPoE Server的多机备份调试信息开关处于关闭状态。

表1-3 debugging pppoe-server vsrp命令输出信息描述表

字段

描述

VSRP *vsrp-instance-name*: Primary device MPU created a backup session.

主设备主控板创建备份会话

VSRP *vsrp-instance-name*: MPU deleted a backup session.

主控板删除备份会话

VSRP *vsrp-instance-name*: Destroyed VSRP TCP channel.

销毁多机备份TCP通道

VSRP *vsrp-instance-name*: Established VSRP TCP channel.

创建多机备份TCP通道

VSRP *vsrp-instance-name*: Failed to establish VSRP TCP channel.

多机备份功能备份TCP通道创建失败

VSRP *vsrp-instance-name*: Deleted a session by command.

命令行执行导致的会话删除

VSRP *vsrp-instance-name*: VSRP channel changed.

注册多机备份服务后PPPoE Server接收到多机备份通知的通道变化事件信息

VSRP *vsrp-instance-name*: VSRP backup mode changed from O*ldMode* to N*ewMode*.

多机备份功能备份模式变化，其中*OldMode*和*NewMode*类型如下：

·Hot：热备份

·Warm：温备份

·N/A：未知备份模式

VSRP *vsrp-instance-name*: VSRP status changed from O*ldStatus* to N*ewStatus*.

多机备份状态变化，其中*OldStatus*和*NewStatus*类型如下：

·Master：实例状态为主

·Backup：实例状态为备

·Down：实例状态为不运行

VSRP *vsrp-instance-name*: Received a VSRP *event* event.

PPPoE Server响应VSRP事件信息，其中*event*类型如下：

·status：VSRP实例状态事件

·backup mode：VSRP实例备份模式事件

·traffic backup interval：VSRP实例流量备份间隔事件

·traffic backup threshold：VSRP实例流量备份阈值事件

·virtual MAC：VSRP实例虚MAC事件peer info：多机备份实例数据通道所需信息

·status over：多机备份实例状态结束事件

VSRP *vsrp-instance-name*: Primary device MPU deleted a backup session.

主设备主控板删除备份会话

VSRP *vsrp-instance-name*: Primary device MPU updated a backup session.

主设备主控板更新备份会话

VSRP *vsrp-instance-name*: Backup device MPU deleted a backup session.

备设备主控板删除备份会话

VSRP *vsrp-instance-name*: Backup device MPU failed to recover a session.

备设备主控板恢复会话失败

VSRP *vsrp-instance-name*: Backup device MPU failed to create a backup session.

备设备主控板创建备份会话失败

VSRP *vsrp-instance-name*: Primary device sent a smooth start message to backup device.

主设备向备设备发送平滑开始消息

VSRP *vsrp-instance-name*: Primary device sent a smooth end message to backup device.

主设备向备设备发送平滑结束消息

VSRP *vsrp-instance-name*: Backup device received a smooth start message.

备设备收到主设备的平滑开始消息

VSRP *vsrp-instance-name*: Backup device received a smooth end message.

备设备收到主设备的平滑结束消息

VSRP *vsrp-instance-name*: New primary device received a real backup end message.

新的主设备收到实时备份结束消息

VSRP *vsrp-instance-name*: Backup device sent a smooth request message to primary device.

备设备向主设备发送平滑请求消息

VSRP *vsrp-instance-name*: Primary device sent a backup session creating message to backup device.

主设备向备设备发送创建备份会话消息

VSRP *vsrp-instance-name*: Primary device sent a backup session deleting message to backup device.

主设备向备设备发送删除备份会话消息

VSRP *vsrp-instance-name*: Primary device sent a backup session batch deleting message to backup device.

主设备向备设备发送批量删除备份会话消息

VSRP *vsrp-instance-name*: Failed to create VSRP CB due to lack of memory space.

申请内存失败导致创建VSRP控制块失败

VSRP *vsrp-instance-name*: Failed to create VSRP CB due to the failure to add VSRP data.

添加VSRP数据失败导致创建VSRP控制块失败

VSRP *vsrp-instance-name*: Failed to create VSRP CB due to VSRP initialization failure.

初始化VSRP控制块失败导致创建VSRP控制块失败

VSRP *vsrp-instance-name*: Virtual MAC changed from *oldMacAddr* to *newMacAddr.*

虚MAC从*oldMacAddr*变为n*ewMacAddr*

VSRP *vsrp-instance-name*: Sent a backup end message to primary device.

备设备向主设备发送备份结束消息

【举例】

*[\# *]打开PPPoE Server的多机备份备份调试信息开关，接口绑定多机备份实例，主设备和备设备TCP通道已建立。默认TCP端口号为60032，如果将TCP端口号改为100，系统将输出下列调试信息。

\<master\> debugging pppoe-server vsrp

\<master\> system-view

master pppoe-server vsrp-port 100

master\*Jun 17 18:25:47:287 2013 master PPPOES/7/VSRP: -MDC=1; VSRP master: Destroyed VSRP TCP channel.

*// 本端通道号与对端通道号不一致，销毁多机备份的备份TCP通道*

**多机备份调试命令 \-- L2TP支持多机备份功能调试命令 \-- debugging l2tp vsrp**

------------------------------------------------------------------------

【命令】

**[debugging l2tp**]** vsrp**[ **error** [\|] **event** }

**[undo debugging l2tp**]** vsrp**[ **error** [\|] **event** }

【视图】]

用户视图]

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[error**]：表示L2TP VSRP的错误调试信息开关。

**[event**]：表示L2TP VSRP的事件调试信息开关。

【描述】

**[debugging l2tp vsrp**]命令用来打开L2TP VSRP的调试信息开关。**undo** **debugging l2tp vsrp**命令用来关闭L2TP VSRP的调试信息开关。

缺省情况下，L2TP VSRP的调试信息开关处于关闭状态。

表1-4 debugging l2tp vsrp error命令输出信息描述表

字段

描述

Failed to create VSRP channel.

数据备份通道创建失败

Failed to create L2TP VSRP reconcile PPP timer.

创建L2TP VSRP与PPP平滑定时器失败

Received a PULL_REQUEST packet in wrong status.

在错误的状态收到同步信息请求报文

Received a BEGIN_RECONCILE or END_RECONCILE packet in wrong status.

在错误的状态收到平滑开始或平滑结束报文

Received a REAL_TIME_TUNNEL packet in wrong status.

在错误的状态收到实时隧道信息报文

Received a too short *message-type* packet.

收到*message-type*类型的报文，报文长度太短。报文类型包括：

·0：本端备份组状态

·1：同步信息请求

·2：平滑开始

·3：平滑结束

·4：添加隧道

·5：实时隧道信息

·6：删除隧道

·7：添加会话

·8：删除会话

Received a *message-type* packet that had failed to pass the check.

收到*message-type*类型的报文，报文未通过检测。报文类型包括：

·0：本端备份组状态

·1：同步信息请求

·2：平滑开始

·3：平滑结束

·4：添加隧道

·5：实时隧道信息

·6：删除隧道

·7：添加会话

·8：删除会话

Received a packet with a wrong local tunnel ID.

收到报文携带错误的本地隧道ID

Received a packet with a wrong group ID.

收到报文携带错误的L2TP组ID

Failed to add a tunnel after receiving the packet.

收到报文后添加隧道失败

Received a packet with a wrong local session ID.

收到报文携带错误的本地会话ID

VSRP service registration failed.

VSRP服务注册失败

Failed to create the VSRP retransmit timer.

重传定时器创建失败

表1-5 debugging l2tp vsrp event命令输出信息描述表

字段

描述

PPPLogStatus

PPP用户登录状态，包括：

·Logged in：已登录

·Logged out：已退出

VSRPName

VSRP实例名

LocalVSRPStatus

本端VSRP状态，包括：

·Master/Up：主/开启

·Backup/Up：备/开启

·Master/Down：主/关闭

·Backup/Down：备/关闭

·Error：错误

RemoteVSRPStatus

对端VSRP状态，包括：

·Master：主

·Backup：备

·Error：错误

VSRPBackupMode

VSRP备份模式，包括：

·Hot：热备

·Warm：温备

·Error：错误

VSRPChannelStatus

数据备份通道状态，包括：

·Connected：已连接

·Disconnected：已断开

·Error：错误

NeedReconcilePeer

是否需要平滑

IsSwitching

是否正在切换

VRFIndexLocal

本端VRF索引

VRFIndexPeer

对端VRF索引

InstanceID

VSRP实例ID

LocalAddr

本端IP地址

PeerAddr

对端IP地址

LocalTunnelID

本端隧道ID

RemoteTunnelID

对端隧道ID

Updated Ns and Nr to remote peer.

通知备用设备更新发送报文的序号（Ns）和期望接收到的下一个控制报文中Ns字段的值（Nr）

SendMessageType

发送信息类型，包括：

·L2TPV2_VSRP_MSG_TYPE_LOCAL_STATUS：表示本端备份组状态

·L2TPV2_VSRP_MSG_TYPE_PULL_REQUEST：表示同步信息请求

·L2TPV2_VSRP_MSG_TYPE_BEGIN_RECONCILE：表示平滑开始

·L2TPV2_VSRP_MSG_TYPE_END_RECONCILE：表示平滑结束

·L2TPV2_VSRP_MSG_TYPE_ADD_TUNNEL：表示添加隧道

·L2TPV2_VSRP_MSG_TYPE_REAL_TIME_TUNNEL：表示实时隧道信息

·L2TPV2_VSRP_MSG_TYPE_DELETE_TUNNEL：表示删除隧道

·L2TPV2_VSRP_MSG_TYPE_ADD_SESSION：表示添加会话

·L2TPV2_VSRP_MSG_TYPE_DELETE_SESSION：表示删除会话

RecvMessageType

接收信息类型，包括：

·L2TPV2_VSRP_MSG_TYPE_LOCAL_STATUS：表示本端备份组状态

·L2TPV2_VSRP_MSG_TYPE_PULL_REQUEST：表示同步信息请求

·L2TPV2_VSRP_MSG_TYPE_BEGIN_RECONCILE：表示平滑开始

·L2TPV2_VSRP_MSG_TYPE_END_RECONCILE：表示平滑结束

·L2TPV2_VSRP_MSG_TYPE_ADD_TUNNEL：表示添加隧道

·L2TPV2_VSRP_MSG_TYPE_REAL_TIME_TUNNEL：表示实时隧道信息

·L2TPV2_VSRP_MSG_TYPE_DELETE_TUNNEL：表示删除隧道

·L2TPV2_VSRP_MSG_TYPE_ADD_SESSION：表示添加会话

·L2TPV2_VSRP_MSG_TYPE_DELETE_SESSION：表示删除会话

MessageDataLen

信息长度

MessageInfo

信息内容

VSRP_EVENT_STATUS

VSRP实例状态事件，包括：

·Master：切换为主用设备

·Backup：切换为备用设备

·Down：主用和备用设备皆不可用

VSRP_EVENT_BACKUPMODE

VSRP实例备份方式事件，包括：

·Hot：切换为热备模式

·Warm：切换为温备模式

VSRP_EVENT_PEERINFO

VSRP实例数据通道所需信息，其中：

·VRFIndexLocal：表示本端VRF索引

·VRFIndexPeer：表示对端VRF索引

·InstanceID：表示VSRP实例ID

·LocalAddr：表示本端IP地址

·PeerAddr：表示对端IP地址

VSRP_EVENT_STATUS_OVER

VSRP实例状态结束事件，包括：

·Over：切换已结束

Updated a backup tunnel.

更新备份隧道

Added a source IP.

源IP生成路由：

·VPNID：表示生成路由所属VPN

·IPAddress：表示源IP地址

·Result：表示路由添加结果

Deleted a source IP.

删除源IP路由：

·VPNID：表示删除路由所属VPN

·IPAddress：表示源IP地址

·Result：表示路由删除结果

Notified remote peer of adding a tunnel.

通知备用设备添加隧道

Notified remote peer of deleting a tunnel.

通知备用设备删除隧道

Notified remote peer of adding a session.

通知备用设备添加会话

Notified remote peer of deleting a session.

通知备用设备删除会话

LocalSessionID

会话本端ID

RemoteSessionID

会话对端ID

PPPUserID

PPP用户ID，12个字节，由PPPoE Server模块告知L2TP

IfName

接口名

Slot

槽位号

Deleted an old session after receiving a L2TPV2_VSRP_MSG_TYPE_END_RECONCILE packet.

备用设备平滑结束删除旧的会话

Deleted an old tunnel after receiving a L2TPV2_VSRP_MSG_TYPE_END_RECONCILE packet.

备用设备平滑结束删除旧的隧道

Deleted an old tunnel due to conflicts.

备用设备运行信息冲突，删除旧的隧道

Updated a backup tunnel.

备用设备更新一条备份隧道

Deleted a backup tunnel.

备用设备删除一条备份隧道

Created a backup tunnel.

备用设备添加一条备份隧道

Associated the PPP user info with the session.

将PPP用户信息和会话关联

Session changed to unassociated state.

会话变为未关联状态

Deleted unassociated sessions upon timeout.

因为超时删除未关联上接口索引的会话

Deleted exceeded sessions.

会话下驱动过程中，删除超出热备规格范围的会话

Deleted exceeded tunnels.

隧道下驱动过程中，删除超出热备规格范围的隧道

Deleted a session from driver.

驱动删除会话

Added a tunnel to driver.

通知驱动添加隧道

Deleted a tunnel to driver.

通知驱动删除隧道

VSRP channel closed.

数据备份通道关闭

Created a VSRP channel.

创建数据备份通道

VSRP channel connected.

数据备份通道连接成功

VSRP channel disconnected.

数据备份通道断开成功

【举例】

\# 主用LAC设备上打开L2TP VSRP的事件和错误调试信息开关。当主用LAC设备新建L2TP隧道和会话时，打印如下调试信息。

\<LAC1\> debugging l2tp vsrp event

\<LAC1\> debugging l2tp vsrp error

%Aug 22 11:37:08:345 2013 LAC1 L2TPV2/1/VSRP: -MDC=1;

 PPPLogStatus: Logged in

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 IfName: Virtual-Access0

 VSRPName: msr_a

 PPPUserID: 0001ffffffff000c2988aac6

*[// PPP*]*用户上线。*

\*Aug 22 11:37:08:348 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 LocalTunnelID: 65127

 RemoteTunnelID: 1

 LocalIPAddr: 5.6.7.8

 RemoteIPAddr: 2.2.2.5

 Notified remote peer of adding a tunnel.

*// 主用LAC设备通知备用LAC设备添加L2TP隧道，隧道ID为65127。*

\*Aug 22 11:37:08:348 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 SendMessageType: L2TPV2_VSRP_MSG_TYPE_ADD_TUNNEL

 MessageDataLen: 696

 MessageInfo: 04 00 02 b4 02 02 02 05 00 00 00 00 00 00 00 00 00 01 fe 67 00 01 06 a5 ff ff 00 02 00 01 6c 6e 73 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

*// 主用LAC设备向备用LAC设备发送实时隧道消息。*

\*Aug 22 11:37:08:349 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 LocalTunnelID: 65127

 RemoteTunnelID: 1

 LocalIPAddr: 5.6.7.8

 RemoteIPAddr: 2.2.2.5

 Added a tunnel to driver.

*// 主用LAC设备通知驱动添加隧道*。*

\*Aug 22 11:37:08:351 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 IfName: Virtual-Access0

 Slot: 65535

 LocalTunnelID: 65127

 LocalSessionID: 545

 RemoteSessionID: 618

 PPPUserID: 0001ffffffff000c2988aac6

 Added a session to driver.

*// 主用LAC设备通知驱动添加会话。*

\*Aug 22 11:37:08:351 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 LocalTunnelID: 65127

 RemoteTunnelID: 1

 LocalIPAddr: 5.6.7.8

 RemoteIPAddr: 2.2.2.5

 Updated Ns and Nr to remote peer.

*[//*]*主用LAC设备通知备用LAC设备更新Ns和Nr。*

\*Aug 22 11:37:08:351 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 SendMessageType: L2TPV2_VSRP_MSG_TYPE_REAL_TIME_TUNNEL

 MessageDataLen: 10

 MessageInfo: 05 00 00 06 fe 67 00 03 00 02

*[//*]*主用LAC设备发送流控更新消息到备用LAC设备。*

\*Aug 22 11:37:08:352 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 IfName: Virtual-Access0

 Slot: 65535

 LocalTunnelID: 65127

 LocalSessionID: 545

 RemoteSessionID: 618

 PPPUserID: 0001ffffffff000c2988aac6

 Notified remote peer of adding a session.

*[//*]*主用LAC设备通知备用LAC设备添加会话，本端会话ID为545，远端会话ID为618。*

\*Aug 22 11:37:08:352 2013 LAC1 L2TPV2/7/VSRP: -MDC=1;

 VSRPName: msr_a

 LocalVSRPStatus: Master/Up

 RemoteVSRPStatus: Backup

 VSRPBackupMode: Hot

 VSRPChannelStatus: Connected

 NeedReconcilePeer: No

 IsSwitching: No

 VRFIndexLocal: 0

 VRFIndexPeer: 0

 InstanceID: 5

 LocalAddr: 2.2.2.1

 PeerAddr: 2.2.2.2

 SendMessageType: L2TPV2_VSRP_MSG_TYPE_ADD_SESSION

 MessageDataLen: 176

 MessageInfo: 07 00 00 ac 00 00 00 00 00 00 00 00 ff ff fe 67 02 21 02 6a 00 00 00 00 00 00 00 00 ff ff ff ff 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0c 29 88 aa c6 00 00

*// 主用LAC设备向备用LAC设备发送实时会话备份消息。*

