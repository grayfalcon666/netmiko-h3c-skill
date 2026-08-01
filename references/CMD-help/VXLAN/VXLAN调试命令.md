<!-- CMD-INDEX
  debugging vxlan isis adj-packet     | 用户视图             | L20
  debugging vxlan isis all            | 用户视图             | L150
  debugging vxlan isis error          | 用户视图             | L186
  debugging vxlan isis event          | 用户视图             | L426
  debugging vxlan isis graceful-restart | 用户视图             | L592
  debugging vxlan isis ha             | 用户视图             | L750
  debugging vxlan isis local-mac      | 用户视图             | L852
  debugging vxlan isis misc           | 用户视图             | L910
  debugging vxlan isis route          | 用户视图             | L1046
  debugging vxlan isis self-originate-update | 用户视图             | L1134
  debugging vxlan isis snp-packet     | 用户视图             | L1270
  debugging vxlan isis timer          | 用户视图             | L1420
  debugging vxlan isis update-packet  | 用户视图             | L1516
  debugging vxlan neighbor-discovery client | 用户视图             | L1724
  debugging vxlan neighbor-discovery server | 用户视图             | L2042
  debugging vxlan tunnel              | 用户视图             | L2266
-->

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis adj-packet**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis adj-packet**[ [ **receive** \| **send** ]  **verbose** ]]

**[undo**[ **debugging vxlan isis adj-packet** [ **receive** \| **send** ]  **verbose** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

**[receive**]：表示接收VXLAN IS-IS邻居报文的调试信息开关。

**[send**]：表示发送VXLAN IS-IS邻居报文的调试信息开关。

**[verbose**]：表示详细调试信息，即打印报文的内容。

【描述】

**[debugging vxlan isis adj-packet**]命令用来打开VXLAN IS-IS邻居报文调试信息开关。**undo debugging vxlan isis adj-packet**命令用来关闭VXLAN IS-IS邻居报文调试信息开关。

缺省情况下，VXLAN IS-IS的邻居报文调试信息开关处于关闭状态。

执行本命令时，如果未指定**receive**和**send**参数，则表示接收和发送VXLAN IS-IS邻居报文调试信息开关。

表1-1 debugging vxlan isis adj-packet命令输出信息描述表

字段

描述

IIH discarded: *String* error.

收到Hello报文解析TLV时发生错误。*String*为错误原因，取值包括：

·protocol support TLV decode：协议支持TLV解码错误

·area address TLV decode：区域地址TLV解码错误

·neighbor TLV decode：邻居TLV解码错误

·system：系统错误

IIH contained *String* that is not supported by the interface *interface-name*.

收到的Hello报文的特征与接口*interface-name*的特征不匹配。*String*为Hello报文与接口不匹配的特征，取值包括：

·PDU type(Level-*number*)：Level-*number*的PDU类型

·supported protocol：支持的协议

Neighbor entry set to down state: IIH contains the same SNPA as the entry, but their system IDs are different.

收到的Hello报文与已有邻居有相同的SNPA地址，但是系统ID不同，将这个邻居置down状态

IIH discarded: The packet has the same System ID as a neighbor entry, but their SNPAs are different.

收到的Hello报文与已有邻居有相同的系统ID，但是SNPA地址不同，丢弃该Hello报文

Level-*Number* neighbor(*Address*)\'s two-way check *String*.

Level-*Number*的邻居2-Way检查结果为*String*。*Address*表示邻居的MAC地址；*String*的取值包括：

·passed：通过

·failed：不通过

·was pending：邻居信息没有收集完整，需要继续等待

ADJ discarded packet: The system was in disabled state.

系统处于去使能状态，丢弃ADJ模块收到的报文

ADJ discarded packet: The interface was not up.

接口处于非up状态，丢弃ADJ模块收到的报文

ADJ discarded packet: The packet was sent by the local device.

收到的是本设备自己的报文，丢弃ADJ模块收到的报文

*[String* sent LAN L1 IIH on interface *interface-name*.]

边缘设备在接口*interface-name*上发送了LAN L1 Hello类型报文，*String*的取值包括：

·ED

·DED

Received LAN L1 IIH from *Address* on interface *interface-name*.

在接口*interface-name*上从地址*Address*收到了LAN L1 Hello类型报文

ADJ discarded packet: PDU type *Number* not supported.

收到了不支持的报文，丢弃ADJ模块收到的报文，*Number*为报文的PDU类型值

Not enough PDU space for area address TLV.

PDU长度已经达到最大值，没有空间保存区域地址TLV

【举例】

\# 打开接收VXLAN IS-IS邻居报文的调试信息开关。

\<Sysname\> debugging vxlan isis adj-packet receive

\*Feb 24 19:12:29:731 2014 SwitchB OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-ADJ: Received LAN L1 IIH from 0011-2200-0001 on interface Tunnel500.

*// 从接口Tunnel500上接收到地址为0011-2200-0001的邻居发送的LAN L1 Hello报文。*

\*Feb 24 19:12:29:732 2014 SwitchB OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-ADJ: Level-1 neighbor (0011.2200.0001)\'s two-way check passed.

*[// L1*]*邻居0011.2200.0001通过Two-way检查。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis all**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis all**]

**[undo debugging vxlan isis all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis all**]命令用来打开所有与VXLAN IS-IS相关的调试信息开关。**undo debugging vxlan isis all**命令用来关闭所有与VXLAN IS-IS相关的调试信息开关。

缺省情况下，所有与VXLAN IS-IS相关的调试信息开关均处于关闭状态。

【举例】

\# 打开VXLAN IS-IS的所有调试信息开关。

\<Sysname\> debugging vxlan isis all

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis error**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis error**]

**[undo debugging vxlan isis error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis error**]命令用来打开VXLAN IS-IS错误调试信息开关。**undo debugging vxlan isis error**命令用来关闭VXLAN IS-IS错误调试信息开关。

缺省情况下，VXLAN IS-IS错误调试信息开关处于关闭状态。

表1-2 debugging vxlan isis error命令输出信息描述表

字段

描述

Failed to get local MAC addresses of VXLAN *Number*.

获取VXLAN *Number*的本地MAC地址失败

Failed to add remote MAC address *mac-address* to VXLAN *number*.

在VXLAN *number*中添加远端MAC地址*mac-address*失败

Failed to create local MAC attribute.

创建本地MAC地址属性失败

Failed to notify the DEC module to handle local MAC conflict.

通知DEC模块（路由维护模块）处理本地MAC地址冲突失败

LAN ADJ data reached the limit.

LAN ADJ数据已达最大值

Failed to get ADJ pointer when starting hello timer.

当启动Hello定时间器时，获取ADJ维护数据失败

Failed to start level-*Number* hello timer.

启动Level-*Number*的Hello定时器失败

Failed to start hold timer.

启动Hold定时器失败

Failed to get system\'s area address when encoding area address TLV.

编码区域地址TLV时获取区域地址失败

Failed to get interface *interface-name*\'s MTU.

获取接口*interface-name*的MTU失败

Failed to send IIH on interface *interface-name*.

在接口*interface-name*上发送Hello报文失败

Failed to create hello timer on interface *interface-name*.

在接口*interface-name*上创建Hello定时器失败

Failed to process interface MTU change event.

处理接口MTU变化事件失败

Failed to activate interface *interface-index*.

激活接口*interface-index*失败

Error occurred when sending notification that interface *interface-index* was removed.

通知接口*interface-index*删除事件错误

Invalid startup phase *phase-number*. Event ignored.

无效的重启阶段，忽略该事件，*phase-number*取值包括：

·0：表示系统处于非重启阶段

·1：表示系统处于重启停止阶段

·2：表示系统处于重启清除数据阶段

·3：表示系统处于清除数据后的后续处理阶段

Failed to create LSP change notification message.

创建LSP变化通知消息失败

PDU\'s level(1) did not match the interface\'s level (*CirLevel*) setting.

PDU报文中的level（1）与接口level（*CirLevel*）不匹配

Failed to set UPDT socket option.

设置UPDT的socket选项失败

Failed to start *Type* timer on interface *interface-name*.

在接口*interface-name*上启动定时器失败。*Type*为定时器类型，取值包括：

·CSNP

·PSNP

·LSP

·LSP flooding

Failed to stop LSP flooding timer on interface *interface-name*.

在接口*interface-name*上停止LSP泛洪定时器失败

Failed to stop level-1 timer on interface *interface-name*.

在接口*interface-name*上停止Lever-1定时器失败

Failed to add MAC address to list.

向链表中添加MAC地址失败

Failed to update LSP information.

更新LSP信息失败

Failed to add LSP information.

添加LSP信息失败

PDU ignored: Interface *interface-name* was not operational.

接口*interface-name*处于不可操作状态，忽略PDU

Failed to obtain interface index.

获取接口索引失败

Failed to send packet: transmit buffer length=*Length*, return length=*ReturnLength*.

发送报文失败，发送缓冲区大小为*Length*，返回值为*ReturnLength*

LSP size *LspSize* exceeded interface\'s MTU size (*CirMtu*).

LSP的大小*LspSize*大于接口的MTU（*CirMtu*）

Failed to send LSP.

发送LSP报文失败

Failed to send level-*Number Type* packet.

发送level-*Number*的*Type*类型报文失败，*Type*取值包括：

·CSNP

·PSNP

Failed to install LSP with sequence number 0.

安装序号为0的LSP失败

Failed to *Type* level-*Number* area address *address*.

操作level-*Number*区域地址*address*失败，操作类型为*Type*，*Type*取值包括：

·add：添加

·delete：删除

Failed to *Type* level-*Number* supported protocol *ProNumber*(*ProString*).

操作level-*Number*的支持的协议类型*ProNumber*（*ProString*）失败，操作类型为*Type*

*[ProString*]取值包括：

·OVERLAY-ISIS：OVERLAY IS-IS协议

·unknown：其它协议

*[Type*]的具体取值可以如下：

·add：添加

·delete：删除

Failed to add level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.

添加level-*Number*由*systemID*到*neighborID*的邻居信息失败

Failed to delete level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.

删除level-*Number*由*systemID*到*neighborID*的邻居信息失败

Failed to modify level-*Number*  neighbor: system *systemID* -\> neighbor *neighborID*.

更新level-*Number*由*systemID*到*neighborID*的邻居信息失败

Failed to add level-*Number* pseudo neighbor: pseudo *pseudoID* -\> neighbor *neighborID*.

添加level-*Number*由*pseudoID*到*neighborID*的伪节点邻居信息失败

Failed to delete level-*Number* pseudo neighbor: pseudo *pseudoID* -\> neighbor *neighborID.*

删除level-*Number*由*pseudoID*到*neighborID*的伪节点邻居信息失败

【举例】

\# 打开VXLAN IS-IS的错误调试信息开关。

\<Sysname\> debugging vxlan isis error

\*Mar 18 14:28:41:744 2013 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-ERR: Failed to send level-1 CSNP PDU.

*// 发送Level-1的CSNP报文失败。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis event**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis event**]

**[undo debugging vxlan isis event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis event**]命令用来打开VXLAN IS-IS事件调试信息开关。**undo debugging vxlan isis event**命令用来关闭VXLAN IS-IS事件调试信息开关。

缺省情况下，VXLAN IS-IS事件调试信息开关处于关闭状态。

表1-3 debugging vxlan isis event命令输出的信息描述表

字段

描述

DED changed on *interface-name*: old DED=*old-ded-mac*, new DED=*new-ded-mac*.

接口*interface-name*所属网段的DED发生改变，原来的DED为*old-ded-mac*，新的DED为*new-ded-mac*

System was in disabled state.

系统处于去使能状态

Main thread notified other threads of tunnel interface status change.

主线程通知其他线程Tunnel接口状态改变

Refreshed interface parameters on interface *interface-index*.

刷新VXLAN IS-IS接口*interface-index*下保存的接口的各种参数

Interface *interface-name* created successfully.

接口*interface-name*创建成功

Interface *interface-name* deleted successfully.

接口*interface-name*删除成功

Notified UPDT thread that LSP MTU size changed from *value1* to *value2*.

通知UPDT线程LSP报文发送的MTU大小由*value1*变为*value2*

Received interface delete acknowledge event. Flag: *bDel*.

收到一个删除接口应答事件，标志为*bDel*

Reset finished: reason code=*reason-code.*

*[reason-code*]引起的复位完成。*reason-code*为原因码，取值包括：

·2：**reset vxlan isis**命令引起的复位

·3：LSP序列号翻转引起的复位

·6：VXLAN IS-IS源MAC地址变化引起的复位

·7：协议进程降级引起的复位

Received *string* on interface *interface-index.*

在接口*interface-index*上收到如下事件：

·interface active event：接口激活事件

·interface deactive event：接口去激活事件

·interface create event：接口创建事件

·interface delete event：接口删除事件

·DOWN \--\> UP event：接口UP事件

·UP \--\> DOWN event：接口DOWN事件

·speed change event：接口速率变化事件

·MTU change event：MTU变化事件

Reset entered phase *phase-code*.

复位进入*phase-code*阶段

·1：表示重启停止阶段

·2：表示重启清除数据阶段

·3：表示清除数据后的后续处理阶段

Processed reset event reply: sender module ID=*module-number*, event ID=*event-number*, reset phase code=*phase-code*.

处理模块*module-number*回复的reset事件*event-number*，当前重启阶段为*phase-code*

*[module-number*]取值如下：

·1：ADJ模块

·2：LSP模块

·3：DEC模块

·4：DATA模块

*[event-number*]取值如下：

·1：停止工作事件

·2：清除数据事件

·3：重启恢复事件

*[phase-code*]取值如下：

·1：重启停止阶段

·2：重启清除数据阶段

Reset processing module received reset event *event-type*.

复位处理模块收到复位事件*event-type*。*event-type*取值包括：

·2：**reset vxlan isis**命令引起的复位

·3：LSP序列号翻转引起的复位

·6：VXLAN IS-IS源MAC地址变化引起的复位

·7：协议进程降级引起的复位

Reset started.

复位开始

【举例】

\# 打开VXLAN IS-IS的事件调试信息开关。

\<Sysname\> debugging vxlan isis event

\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-EVT: Main thread notified other threads of tunnel interface status change.

*// 主线程通知其他线程Tunnel接口状态改变。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis graceful-restart**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis graceful-restart**]

**[undo debugging vxlan isis graceful-restart**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis graceful-restart**]命令用来打开VXLAN IS-IS的平滑重启调试信息开关。**undo debugging vxlan isis graceful-restart**命令用来关闭VXLAN IS-IS的平滑重启调试信息开关。

缺省情况下，VXLAN IS-IS的平滑重启调试信息开关处于关闭状态。

表1-4 debugging vxlan isis graceful-restart命令输出信息描述表

字段

描述

Graceful restart completed.

平滑重启完成

T3 timer stopped.

T3定时器停止

T3 timer expired before T2 timer.

T3定时器在T2定时器之前失效

Level-*Number* T2 timer expired.

Level-*Number*的T2定时器失效

Graceful restart entered *Type* phase.

平滑重启进入*Type*阶段，*Type*指示了类型可以取值如下：

·starting：启动

·restarting：重启

Received T2 timer cancel event.

收到T2定时器取消事件

Level-*Number* T2 timer stopped.

Level-*Number*的T2定时器停止

Received module\'s GR phase: module=Mid, module\'s phase=*Phase,* system\'s current GR phase=*GrPhase*.

收到模块*Mid*的GR状态*Phase*，当前GR状态是*GrPhase*

正常情况下模块的GR与系统的GR状态应当一致，否则视为异常

*[Mid*]取值包括：

·0：主模块

·1：ADJ模块

·2：Update模块

·3：DEC模块

·4：DATA模块

*[Phase*]和*GrPhase*取值包括：

·0：初始阶段

·1：LSDB同步阶段

·2：路由计算阶段

·3：接收本地MAC地址上报的阶段

·4：LSP生成的阶段

·5：LSP刷新和泛洪的阶段

·6：GR完成的阶段

Stopped level-*Number* T1 timer.

停止level-*Number*的T1定时器

Interface *interface-name* received level-*Number* IIH with *Type* bit set.

从接口*interface-name*收到level-*Number* hello报文，报文中的*Type*位置位，*Type*位取值包括：

·RR：重启请求位

·RA：重启抑制位

Failed to purge level-*Number* LSP.

清除level-*Number*的LSP报文失败

Started purging local level-*Number* LSP.

开始清除本地的level-*Number*的LSP报文

Purged level-*Number* LSP *PseudoId*-*FragNum*.

清除level-*Number*的LSP *PseudoId*-*FragNum*报文

Finished purging local level-*Number* LSPs.

结束清除本地的level-*Number* LSP报文

Level-*Number* LSDB synchronization completed.

Level-*Number*的LSDB同步完成

Level-*Number* CSNP setting synchronization completed on interface *interface-name*.

在接口*interface-name*上Level-*Number*的CSNP设置同步完成

Level-*Number* LSDB synchronization completed.

Level-*Number*的LSDB同步完成

Level-*Number* T1 timer expired *Number* times on interface *interface-index*

接口*interface-index*下，Level-*Number*的T1定时器超时*Number*次

【举例】

\# 打开VXLAN IS-IS的平滑重启调试信息开关。

\<Sysname\> debugging vxlan isis graceful-restart

\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-GR: Level-1 LSDB synchronization completed.

*[// Level-1*]*的LSDB同步完成。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis ha**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis ha**]

**[undo debugging vxlan isis ha**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis ha**]命令用来打开VXLAN IS-IS的HA调试信息开关。**undo debugging vxlan isis ha**命令用来关闭VXLAN IS-IS的HA调试信息开关。

缺省情况下，VXLAN IS-IS的HA调试信息开关处于关闭状态

表1-5 debugging vxlan isis ha命令输出信息描述表

字段

描述

Received HA *event* event.

收到HA通知事件*event*。*event*取值包括：

·EPOLLUP：epoll挂起事件

·batch backup：批量备份事件

·stop：进程停止事件

·degrade：降级事件

·upgrade：升级事件

Received real-time backup data.

收到实备数据

Received batch backup data.

收到批量备份数据

Notified thread to stop work.

通知线程停止工作

Processed HA upgrade.

处理HA升级事件

HA smooth ended.

HA平滑结束

HA smooth started.

HA平滑开始

No process found. HA smooth ended.

不存在任何进程，HA平滑结束

External initialization for HA.

HA时进行外部初始化

Notified thread to start work.

通知线程开始工作

Started VXLAN-ISIS process during HA upgrade.

当HA升级时开始启动VXLAN IS-IS进程

【举例】

\# 打开VXLAN IS-IS的高可用性调试信息开关。

\<Sysname\> debugging vxlan isis ha

\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-HA: Received HA upgrade event.

*// 收到HA升级事件*。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis local-mac**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis local-mac**]

**[undo debugging vxlan isis local-mac**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis local-mac**]命令用来打开VXLAN IS-IS的本地MAC地址调试信息开关。**undo** **debugging vxlan isis local-mac**命令用来关闭VXLAN IS-IS的本地MAC地址调试信息开关。

缺省情况下，VXLAN IS-IS的本地MAC地址调试信息开关处于关闭状态。

表1-6 debugging vxlan isis local-mac命令输出信息描述表

字段

描述

Received local MAC address information: operation type=O*pType*, MAC type=*MacType*, VSI=*vsi-index*, MAC=*MacAddr*.

收到本地MAC地址信息，VSI索引为*vsi-index*，MAC地址为*MacAddr*，操作类型为*OpType*，*OpType*的取值包括：

·add：添加

·delete：删除

MAC地址类型为*MacType*，*MacType*的取值为dynamic，表示动态MAC地址

【举例】

\# 打开VXLAN IS-IS的本地MAC地址调试信息开关。

\<Sysname\> debugging vxlan isis local-mac

\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-LMAC: Received local MAC address information: operation type=add, MAC type=dynamic, VSI=2, MAC=aa-bb-cc.

*// 收到本地MAC，在VSI 2内添加动态的本地MAC地址aa-bb-cc。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis misc**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis misc**]

**[undo debugging vxlan isis misc**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis misc**]命令用来打开与VXLAN IS-IS进程无关的其它调试信息开关。**undo debugging vxlan isis misc**命令用来关闭与VXLAN IS-IS进程无关的其它调试信息开关。

缺省情况下，与VXLAN IS-IS进程无关的其它调试信息开关处于关闭状态。

表1-7 debugging vxlan isis misc命令输出信息描述表

字段

描述

Failed to receive local MAC message.

接收本地MAC消息失败

Process created successfully.

进程创建成功

Failed to connect to DEV module.

连接DEV模块失败

Error occurred when sending HA response (UPGRADE_OVER).

发送HA升级完成应答错误

Started HA upgrade-wait timer to wait for the reset operation to complete.

为了等待重启结束，启动HA升级等待定时器为了

Error occurred during external initialization for HA.

HA时外部初始化错误

Delivery of global packet to CPU was *Type*.

全局的报文是否允许发送到CPU，*Type*表示操作的类型，取值包括：

·Enabled：允许

·Disabled：不允许

Process *ProcessID* is deleted successfully.

进程*ProcessID*删除成功，*ProcessID*为进程索引号

Failed to get system node *Number*.

获取系统节点失败，*Number*为系统索引

Received DEV EPOLLHUP event.

收到DEV模块发送过来的EPOLLHUP事件

Service port event triggered IS-IS module to connect to L2VPN module.

服务端口事件触发IS-IS与L2VPN模块建立连接

Received VXLAN *Type* event.

收到VXLAN事件。*Type*为事件的类型，取值包括：

·create：创建事件

·delete：删除事件

·EPOLLHUP：EPOLL挂起事件

Received VSI *Type* event.

收到VSI事件。*Type*为事件的类型，取值包括：

·create：创建事件

·delete：删除事件

·shutdown：关闭事件

Received L2VPN *Type* event.

收到VSI事件。*Type*为事件的类型，取值包括：

·batch begin：批量通告开始

·batch end：批量通告结束

·global disable：L2VPN全局去使能

Received L2VIF *Type* event.

收到L2VIF事件。*Type*为事件的类型，取值包括：

·create：创建事件

·delete：删除事件

·interface type *interface**-type*：接口类型事件

【举例】

\# 打开与VXLAN IS-IS进程无关的其它调试信息开关。

\<Sysname\> debugging vxlan isis misc

\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-MISC: Received VXLAN create event.

*// 收到VXLAN创建事件。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis route**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis route ** **verbose** ]

**[undo debugging vxlan isis route** **verbose** ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

**[verbose**]：表示VXLAN IS-IS路由计算的详细调试信息开关。

【描述】

**[debugging vxlan isis route**]命令用来打开VXLAN IS-IS的路由计算调试信息开关。**undo** **debugging vxlan isis route**命令用来关闭VXLAN IS-IS的路由计算调试信息开关。

缺省情况下，VXLAN IS-IS的路由计算调试信息开关处于关闭状态。

表1-8 debugging vxlan isis route命令输出信息描述表

字段

描述

Flush remote MAC entry: VXLAN=*Number*, MAC=*MacAddr*, operation=*Type*.

下刷MAC表项，VXLAN为*Number*，MAC地址为*MacAddr*，操作类型为*Type*，*Type*的取值包括：

·none：无

·add：添加

·delete：删除

·update：更新

Failed to flush remote MAC entry: VXLAN=*Number*, MAC=*MacAddr*, error=*ErrorId*.

下刷MAC表项失败，VXLAN为*Number*，MAC地址为*MacAddr*，错误ID为*ErrorId*

*[Type* remote MAC entry: VXLAN=*Number*, MAC=*MacAddr*, flag=*bConflictFlag*, conf=*ucConfidence*.]

操作远端MAC地址表项，操作类型为*Type*，具体取值包括：

·Added：添加

·Deleted：删除

·Updated：更新

MAC地址为*MacAddr*，所属VXLAN为*Number*，冲突标记为*bConflictFlag*，优先级标记为*ucConfidence*

Queried remote MAC entry: VXLAN=*Number*, MAC=*MacAddr*.

查询远端MAC表项：VXLAN为*Number*，MAC地址为*MacAddr*

Added remote MAC entry to the flush table: VSI=*vsi-index*, MAC=*MacAddr*.

将远端MAC表项添加至下刷表：VSI索引为*vsi-index*，MAC地址为*MacAddr*

Found remote MAC entry in the flush table: VSI=*vsi-index*, MAC=*MacAddr*.

在下刷表中找到要处理的远端MAC：VSI索引为*vsi-index*，MAC地址为*MacAddr*

【举例】

\# 打开VXLAN IS-IS的路由计算调试信息开关。

\<Sysname\> debugging vxlan isis route

\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-ROUTE: Updated remote MAC entry: VXLAN=1, MAC=aa-bb-cc, flag=0, conf=1.

*// 更新远端MAC地址表项：VXLAN为5，MAC地址为aa-bb-cc，冲突标记为0，MAC优先级为1。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis self-originate-update**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis self-originate-update**]

**[undo debugging vxlan isis self-originate-update**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis self-originate-update**]命令用来打开VXLAN IS-IS的本地更新调试信息开关。**undo debugging vxlan isis self-originate-update**命令用来关闭VXLAN IS-IS的本地更新调试信息开关。

缺省情况下，VXLAN IS-IS的本地更新调试信息开关处于关闭状态。

表1-9 debugging vxlan isis self-originate-update命令输出信息描述表

字段

描述

Purged level-*Number* LSP *LSPId*.*PseudoId*-*FragNum*.

清除level-*Number*的LSP（LSPID.伪节点ID-分片号）

VXLAN-ISIS level-*Number* LSP overflowed.

VXLAN IS-IS的level-*Number* LSP已满

Failed to add area address or supported protocol: remaining space of level-*Number* LSP fragment 0 was not enough.

当添加区域地址或协议支持时level-*Number*的零分片LSP中剩余空间不足

Started rebuilding all level-*Number* LSPs on Tunnel *tunnel-number*.

开始对Tunnel *tunnel-number*、level-*Number*的所有LSP进行Rebuild操作

Finished rebuilding all level-*Number* LSPs on Tunnel *tunnel-number*.

Tunnel *tunnel-number*、level-*Number*所有LSP的Rebuild操作结束

MTU change triggered rebuilding.

MTU改变触发Rebuild操作

LSP sequence number exceeded the limit.

LSP的序列号超过最大值（需要反转）

Generated level-*Number* LSP *LSPId*.*PseudoId*-*FragNum*: sequence number=*SeqNumi,* length=*LspLen*.

生成序列号为*SeqNum*、长度为*LspLen*的level-*Number* LSP（LSPID.伪节点ID-分片号）

LSP processing triggered rebuilding on Tunnel *tunnel-number*.

在Tunnel *tunnel-number*上的LSP处理触发Rebuild操作

LSP lifetime change triggered rebuilding on all Tunnels.

LSP生存时间触发在所有Tunnel上的Rebuild操作

*[Type *level-*Number* area address *address*.]

操作level-*Number*的区域地址*address*

*[Type*]的取值包括：

·1：Added：添加

·2：Deleted：删除

Added level-*Number* supported protocol type *ProNumber*(*ProString*).

为level-*Number*添加支持的协议类型*ProNumber*（*ProString*）

Removed level-*Number* supported protocol type *ProNumber*(*ProString*).

为level-*Number*删除支持的协议类型*ProNumber*（*ProString*）

Added level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.

为level-*Number*添加由*systemID*到*neighborID*的邻居信息

Removed level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.

为level-*Number*删除由*systemID*到*neighborID*的邻居信息

Modified level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.

为level-*Number*更新由*systemID*到*neighborID*的邻居信息

Added level-*Number* pseudo neighbor: pseudo *pseudoID* -\> neighbor *neighborID*.

为level-*Number*添加由*pseudoID*到*neighborID*的伪节点邻居信息

Removed level-*Number* pseudo neighbor: pseudo *pseudoID* -\> neighbor *neighborID*.

为level-*Number*删除由*pseudoID*到*neighborID*的伪节点邻居信息

Failed to add MAC address to VXLAN *Number*.

为VXLAN *Number*添加MAC地址失败

Removed MAC address from VXLAN *Number*.

为VXLAN *Number*删除MAC地址

Removed all MAC addresses from VXLAN *Number*.

删除VXLAN *Number*的所有MAC地址

【举例】

\# 打开VXLAN IS-IS的本地更新调试信息开关。

\<Sysname\> debugging vxlan isis self-originate-update

OVERLAYISIS---0-ORG: Generated level-1 LSP [0011.2233.4401.00-00: sequence number=0x00000001, length=71.]

*// 生成序列号为0x00000001、长度为71的L1 LSP（0011.2233.4401.00-00*）。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis snp-packet**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis snp-packet **[[ **receive** \| **send** ]  **verbose** ]]

**[undo debugging vxlan isis snp-packet **[[ **receive** \| **send** ]  **verbose** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

**[receive**]：表示接收VXLAN IS-IS SNP报文的调试信息开关。

**[send**]：表示发送VXLAN IS-IS SNP报文的调试信息开关。

**[verbose**]：表示详细调试信息，即打印报文的内容。

【描述】

**[debugging vxlan isis snp-packet**]命令用来打开VXLAN IS-IS的SNP报文调试信息开关。**undo** **debugging vxlan isis snp-packet**命令用来关闭VXLAN IS-IS的SNP报文调试信息开关。

缺省情况下，VXLAN IS-IS的SNP报文调试信息开关处于关闭状态。

执行本命令时，如果未指定**receive**和**send**参数，则表示接收和发送VXLAN IS-IS SNP报文的调试信息开关。

表1-10 debugging evi isis snp-packet命令输出信息描述表

字段

描述

Received *PduName* from *SourceId* on interface *interface-name*.

在接口*interface-name*上收到来自于*SourceId*的*PduName*，*PduName*的具体取值包括：

·L1 CSNP

·L1 PSNP

Received *PduName* from *SourceId* on interface *interface-name:* LSP range=*StartLSPId*.*StartPseudoId*-*StartFragNum* to *EndLSPId*.*EndPseudoId*-*EndFragNum.*

在接口*interface-name*上收到来自于*SourceId*的*PduName*，*PduName*取值包括L1 CSNP和L1 PSNP，PDU包括的LSP范围为起始LSP（*StartLSPId*.*StartPseudoId*-*StartFragNum*）到结束LSP（*EndLSPId*.*EndPseudoId*-*EndFragpNum*）

Failed to process SNP packet.

处理SNP报文失败

Failed to find current LSP\'s digest to create CSNP.

没有找到当前的LSP摘要来创建CSNP

Level-*Number* CSNP timer expired on a non-DED interface (*interface-name*).

非DED的接口*interface-name*上lever-*Number*的CSNP定时器超时

Sent *PduName* on interface *interface-name*.

在接口*interface-name*上发送*PduName*。*PduName*的取值包括：

·L1 CSNP

·L1 PSNP

Level-*Number* PSNP timer expired on a DED interface (*interface-name*).

DED接口*interface-name*上lever-*Number*的PSNP定时器超时

Invalid LSP ID in SNP.

SNP中包含无效的LSPID

Incorrect LSP digest TLV length(*TlvLen*) in SNP.

SNP中携带错误的LSP摘要TLV长度

Number of LSP digests in SNP exceeded the limit.

SNP中包含LSP摘要的个数超过限制

Incorrect TLV length in SNP.

SNP中携带错误的TLV长度

Invalid TLV in SNP.

SNP中携带无效的TLV

Processed LSP digest *LSPId*.*PseudoId*--*FragNum*. Result: Older than the digest in LSDB.

处理LSP摘要*LSPId*.*PseudoId*-*FragNum*，比LSDB中保存的旧

Processed LSP digest *LSPId*.*PseudoId*--*FragNum*. Result: Newer than the digest in LSDB.

处理LSP摘要*LSPId*.*PseudoId*-*FragNum*，比LSDB中保存的新

Processed LSP digest *LSPId*.*PseudoId*--*FragNum*. Result: Same as the digest in LSDB.

处理LSP摘要*LSPId*.*PseudoId*-*FragNum*，与LSDB中保存的新旧相同

Processed digest of *LSPId*.*PseudoId*--*FragNum*: digest not contained in LSDB.

处理LSP摘要*LSPId*.*PseudoId*-*FragNum*，在LSDB中不存在

PSNP not processed: current ED was not a DED.

当前ED不是DED，不处理PSNP报文

*[SNPType* can\'t be processed before DED election.]

在DED选举前不处理*SNPType*报文，*SNPType*的取值包括：

·CSNP

·PSNP

CSNP didn\'t contain digest for LSP *LSPId*.*PseudoId*-*FragNum*.

在CSNP中没有LSP *LSPId*.*PseudoId*-*FragNum*的摘要

DED doesn\'t process CSNP.

DED上不处理CSNP报文

Invalid SNP PDU type.

无效的SNP PDU类型

【举例】

\# 打开VXLAN IS-IS的 SNP报文调试信息开关。

\<Sysname\> debugging vxlan isis snp-packet send

\*Dec 19 15:40:51:337 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-SNP: Sent L1 CSNP on interface Tunnel1.

*// 在Tunnel1上发送Level-1的CSNP报文。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis timer**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis timer**]

**[undo debugging vxlan isis timer**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

无

【描述】

**[debugging vxlan isis timer**]命令用来打开VXLAN IS-IS的定时器调试信息开关。**undo debugging vxlan isis timer**命令用来关闭VXLAN IS-IS的定时器调试信息开关。

缺省情况下，VXLAN IS-IS的定时器调试信息开关处于关闭状态。

表1-11 debugging vxlan isis timer命令输出信息描述表

字段

描述

Started *Type* timer: value=*value*.

启动*Type*定时器，时间为*value*，*Type*的取值包括：

·T2

·T3

Reset *Type* timer: value=*value*.

重置*Type*定时器，重置后的时间为*value*，*Type*的取值包括：

·T2

·T3

Level-*Number* adjacency *SystemId* hold timer expired on interface *interface-name*.

接口*interface-name*下的level-*Number*的邻居*SystemId*定时器超时

Level-*Number* hello timer expired on interface *interface-name*.

接口*interface-name*下的level-*Number*的Hello定时器超时

Started sequence number wrap delay timer: value=*value* ms.

启动LSP序列号达到最大值的翻转等待定时器，定时器时长为*value*毫秒

Level-*Number* CSNP timer expired on interface *interface-name*.

接口*interface-name*下的level-*Number* CSNP定时器超时

Level-*Number* flood timer expired on interface *interface-name*.

接口*interface-name*下的level-*Number*泛洪定时器超时

Level-*Number* LSP *LSPId*.*PseudoId*-*FragNum* generation timer expired.

level-*Number*的LSP（LSPID.伪节点ID-分片号）生成定时器超时

Started level-*Number* LSP *LSPId*.*PseudoId*-*FragNum* generation timer: value= *TimeValue* (ms).

启动level-*Number* 的LSP（LSPID.伪节点ID-分片号）生成定时器，定时器时长为*TimeValue*毫秒

Stopped level-*Number* LSP *LSPId*.*PseudoId*-*FragNum* generation timer.

停止level-*Number*的LSP（LSPID.伪节点ID-分片号）生成定时器

【举例】

\# 打开VXLAN IS-IS的定时器调试信息开关。

\<Sysname\> debugging vxlan isis timer

\*Dec 20 10:18:29:955 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-TMR: Level-1 hello timer expired on interface Tunnel1.

*[// Tunnel1*]*上的Lever-1 Hello报文发送定时器超时。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis update-packet**

------------------------------------------------------------------------

【命令】

**[debugging vxlan isis update-packet**[ [ **receive** \| **send** ]  **verbose** ]]

**[undo debugging vxlan isis update-packet **[[ **receive** \| **send** ]  **verbose** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admim

【参数】

**[receive**]：表示接收VXLAN IS-IS LSP报文的调试信息开关。

**[send**]：表示发送VXLAN IS-IS LSP报文的调试信息开关。

**[verbose**]：表示详细调试信息，即打印报文内容。

【描述】

**[debugging vxlan isis update-packet**]命令用来打开VXLAN IS-IS的LSP报文调试信息开关。**undo** **debugging vxlan isis update-packet**命令用来关闭VXLAN IS-IS的LSP报文调试信息开关。

缺省情况下，VXLAN IS-IS的LSP报文调试信息开关处于关闭状态。

执行本命令时，如果未指定**receive**和**send**参数，则表示接收和发送VXLAN IS-IS LSP报文调试信息开关。

表1-12 debugging vxlan isis update-packet命令输出信息描述表

字段

描述

Flooded *PduName* *LSPId*.*PseudoId*-*FragNum* on interface *interface-name*.

在接口*interface-name*上泛洪*PduName*的LSP（*LSPId*.*PseudoId*-*FragNum*），*PduName*的取值包括：

·L1 LSP

·L1 CSNP

·L1 PSNP

L1 LSP *Type* on interface *interface-name*: SNPA=*SnpaAddr*, LSP ID=*LSPId*.*PseudoId*--*FragNum*, sequence number=*Sequence*, hold time=*HoldTime*.

在接口*interface-name*上从地址*SnpaAddr*接收到或向该地址发送的LSP ID为*LSPId*.*PseudoId*-*FragNum*、序列号为*Sequence*、时间为*HoldTime*的L1 LSP报文

*[Type*]的取值包括：

·Received：接收

·Sent：发送

*[Type *remote address: VXLAN*=Number*, MAC*=MacAddr*.]

对远端MAC地址进行操作，VXLAN为*Number*，MAC地址为*MacAddr*。*Type*取值包括：

·Added：添加

·Deleted：删除

·Modified：修改

LSP\'s sequence number was 0.

LSP报文的序列号为0

Illegal IS type in level-1 LSP.

Level-1的LSP报文中存在无效的IS类型

Checksum was 0.

校验和为0

Checksum error.

校验和错误

Invalid extended IS reachability TLV.

不支持的扩展IS可达性TLV

Supported protocol mismatch.

支持的协议不匹配

LSP had more than *Count* area addresses.

LSP中区域地址数量超过最大值

LSP had incorrect area address length (*Length*).

LSP中区域地址长度错误，长度为*Length*

LSP had incorrect area address (*AreaAddr*).

LSP中区域地址错误，地址为*AreaAddr*

Invalid VXLAN TLV.

无效的VXLAN TLV

Invalid MAC reachability TLV.

无效的MAC可达性TLV

Incorrect area address TLV in LSP.

在LSP报文中存在错误的区域地址TLV

Incorrect TLV length in the received LSP.

收到LSP报文中TLV长度错误

A version of local LSP *LSPId*.*PseudoId*-*FragNum* was generated with a newer sequence number (Seq) than the version in the LSDB.

本地生成的LSP的序列号比LSDB中新

A new version of non-local LSP *LSPId*.*PseudoId*-*FragNum* was received with a newer sequence number (Seq) than the version in the LSDB.

非本地生成的LSP的序列号比LSDB中新

The new version of LSP *LSPId*.*PseudoId*-*FragNum* contained a sequence number (*Seq*) older than the version in the LSDB.

LSP的序列号比LSDB中旧

The new version of LSP *LSPId*.*PseudoId*-*FragNum* contained the same sequence number (*Seq*) as the version in the LSDB.

LSP的序列号比LSDB中相同

*[LspType* LSP *LSPId*.*PseudoId*-*FragNum Seq* didn\'t exist in LSDB.]

LSDB中不存在LSP ID为*LSPId*.*PseudoId*-*FragNum*、序列号为*Seq*的LSP。*LspType*为LSP类型，取值包括：

·Non-local：非本地的

·Local：本地的

PDU discarded: PDU size (*Size*) exceeded receive buffer size (*SizeBuf*).

收到的PDU大小*Size*大于接收缓冲区大小*SizeBuf*，丢弃PDU

PDU discarded: PDU size (*Size*) smaller than common header\'s length (*Length*).

收到的PDU大小*Size*小于PDU通用报文头长度*Length*，丢弃PDU

PDU discarded: PDU size (*Size*) smaller than value (*Length*) in the Length Indicator field.

收到的PDU大小*Size*小于PDU填充的报文头长度*Length*，丢弃PDU

PDU discarded: PDU length mismatch, recvLen=*RecvLength*, encodeLen=*EncodeLenght*.

收到的PDU长度*RecvLength*与报文中指示的长度*EncodeLenght*不匹配，丢弃PDU

PDU discarded on interface (*interface-name*): PDU contained the same SNPA address as local system.

在接口*interface-name*上收到的PDU报文中SNPA的地址与本地一样，丢弃PDU

PDU discarded: VXLAN-ISIS process was disabled.

VXLAN IS-IS进程处于disabled状态，丢弃PDU

Failed to check received packet.

检查接收到的报文失败

PDU discarded: LSP or SNP common header error.

LSP或SNP通用报文头错误，丢弃PDU

PDU level mismatch.

收到的PDU报文级别不匹配

PDU discarded: no active neighbor with SNPA (*SnpaAddr*) existed on the interface (*interface-name*).

在接口*interface-name*上不存在激活的邻居*SnpaAddr*，丢弃PDU

Failed to process LSP.

处理LSP报文失败

PDU discarded: the PDU was not LSP or SNP.

收到的PDU报文不是LSP或SNP报文，丢弃PDU

【举例】

\# 打开VXLAN IS-IS update-packet调试信息开关。

\<Sysname\> debugging vxlan isis update-packet receive

\*Jun  8 08:31:21:994 2011 Sysname OLISIS/7/DEBUG: -MDC=1;

OVERLAYISIS-0-UPDT: PDU level mismatch.

*// 收到的PDU报文级别不匹配。*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan neighbor-discovery client**

------------------------------------------------------------------------

【命令】

**[debugging vxlan neighbor-discovery client**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]]

**[undo debugging vxlan neighbor-discovery client**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示ENDC所有调试信息开关。

**[entry**]：表示ENDC表项调试信息开关。

**[error**]：表示ENDC错误调试信息开关。

**[event**]：表示ENDC事件调试信息开关。

**[packet**]：表示ENDC报文调试信息开关。

【描述】

**[debugging vxlan neighbor-discovery client**]命令用来打开ENDC调试信息开关。**undo debugging vxlan neighbor-discovery client**命令用来关闭ENDC调试信息开关。

缺省情况下，ENDC调试信息开关处于关闭状态。

表1-13 debugging vxlan neighbor-discovery client entry命令输出信息描述表

字段

描述

Failed to find the server node.

查找服务器节点失败

 

*[operate-name*: interface= *interface-name*, network ID= *netid-value*, IP address= *ipaddr-value*.]

操作表项信息，接口为{.TableTextChar}*interface-name*，网络ID{.TableTextChar}为{.TableTextChar}*netid-value*，IP{.TableTextChar}地址为{.TableTextChar}*ip-address*

*[operate-name*]的取值可能为：{.TableTextChar}

·Added neighbor：添加邻居节点

·Deleted neighbor：删除邻居节点

·Added server node：添加服务器节点

·Deleted server node：删除服务器节点

·Added dummy：添加Dummy节点

·Deleted dummy：删除Dummy节点

 

Added tunnel: interface= *interface-name*, peer address= *ipaddr-value*.

添加隧道：接口为*interface-name*，对端IP地址为*ipaddr-value*

 

Deleted tunnel: interface= *interface-name*, peer address= *ipaddr-value*.

删除隧道：接口为*interface-name*，对端IP地址为*ipaddr-value*

 

表1-14 debugging vxlan neighbor-discovery client error命令输出信息描述表

字段

描述

Failed to create run info.

创建运行信息失败

 

Failed to create hash.

创建hash失败

 

Failed to start ENDP service.

启动ENDP服务失败

 

Failed to create tunnel connection.

创建与隧道的连接失败

 

表1-15 debugging vxlan neighbor-discovery client event命令输出信息描述表

字段

描述

Created *timer-name* timer: timer interval= *time-value*, timer ID= *id-value*.

创建*timer-name*定时器，时间间隔为*time-value*，定时器ID为*id-value*

*[timer-name*]的取值可能为：

·register：注册定时器

·LIPC reconnect：LIPC重连定时器

·neighbor aging：邻居老化定时器

 

Modified register timer: timer interval= *time-value*.

修改注册定时器的时间间隔为*time-value*

 

Deleted *timer-name* timer: timer ID= *id-value*.

删除*timer-name*定时器，定时器ID为*id-value*

*[timer-name*]的取值可能为：

·register：注册定时器

·LIPC reconnect：LIPC重连定时器

·neighbor aging：邻居老化定时器

 

Received tunnel restart event.

收到隧道重启事件

 

Started ENDP service.

启动ENDP服务

 

Started smoothing neighbor information.

开始平滑邻居信息

 

Finished smoothing neighbor information.

邻居信息平滑结束

 

Stopped ENDP service.

停止ENDP服务

 

*[interface-name *received interface *event-name*.]

接口*interface-name*收到接口事件，事件类型为*event-name*

*[event-name*]的取值可能为：

·up event：接口up

·down event：接口down

·create event：接口创建

·delete event：接口删除

 

表1-16 debugging vxlan neighbor-discovery client packet命令输出信息描述表

字段

描述

Interface *interface-name* received a packet: packet type= *type-value*, network ID= *netid-value*, server address= *ipaddr-value*.

接口*interface-name*收到一个报文：报文类型为*type-value*，对应的网络ID为*netid-value*，服务器IP地址为*ipaddr-value*

*[type-value*]的取值可能为：

·3：注册报文

·4：注册应答报文

·5：注销报文

·6：错误指示报文

 

Interface *interface-name s*ent a packet: packet type= *type-value*, network ID= *netid-value*, server address= *ipaddr-value*.

接口*interface-name*发送一个报文：报文类型为*type-value*，对应的网络ID为*netid-value*，服务器IP地址为*ipaddr-value*

*[type-value*]的取值可能为：

·3：注册报文

·4：注册应答报文

·5：注销报文

·6：错误指示报文

 

Peer info: IP address= *ipaddr-value*, system ID= *macaddr-value*.

对端信息：IP地址为*ipaddr-value*，MAC地址为*macaddr-value*

 

Invalid peer info: IP address= *ipaddr-value*.

失效的对端信息：IP地址为*ipaddr-value*

 

Packet failed header check.

报文头检测失败

 

Packet failed fixed header check.

报文固定头检测失败

 

Packet failed required content check.

报文强制部分检测失败

 

Packet failed extended content check.

报文扩展部分检测失败

 

Transaction ID mismatch.

事务ID不相等

 

Packet failed authentication.

认证失败

 

【举例】

\# 使能ENDC功能，打开ENDC表项调试信息开关，当ENDC收到ENDS的应答报文后会输出下列调试信息。

\<Sysname\> debugging vxlan neighbor-discovery client entry

\*Sep  6 17:14:34:243 2011 Sysname ENDC/7/ENTRY: -MDC=1; Add neighbor: interface= Tunnel1, network ID= 1; IP address= 1.1.1.1.

*// 添加邻居节点，接口为Tunnel1，网络ID为1，邻居的IP地址为1.1.1.1*

\*Sep  6 17:14:34:246 2011 Sysname ENDC/7/ENTRY: -MDC=1; Added tunnel: interface= Tunnel1, ieer address= 1.1.1.1.

*// 添加隧道，接口为Tunnel1，对端IP地址为1.1.1.1*

\# 使能ENDC功能，打开ENDC事件调试信息开关，当ENDC发送注册报文后会输出下列调试信息。

\<Sysname\> debugging vxlan neighbor-discovery client event

\*Sep  8 15:21:38:814 2011 Sysname ENDS/7/EVENT: -MDC=1; Created register timer: time interval= 15s, timer ID= 10.

*// 创建注册定时器，时间间隔为15秒，定时器ID为10*

\# 使能ENDC功能，打开ENDC报文调试信息开关，当ENDC收到ENDS的应答报文后会输出下列调试信息。

\<Sysname\> debugging vxlan neighbor-discovery client packet

\*Sep  6 17:22:10:772 2011 Sysname ENDC/7/PACKET: -MDC=1; Interface Tunnel1 received a packet: packet type= 4, network ID= 1, server address= 1.1.1.1.

*// 接口Tunnel1收到一个报文，报文类型为注册应答报文，对应的网络ID为1，服务器IP地址为1.1.1.1*

\*Sep  6 17:22:10:773 2011 Sysname ENDC/7/PACKET: -MDC=1; Peer info: IP address= 1.1.1.1, system ID= 0011-2200-0101.

*// 对端信息：IP地址为1.1.1.1，MAC地址为0011-2200-0101*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan neighbor-discovery server**

------------------------------------------------------------------------

【命令】

**[debugging vxlan neighbor-discovery server**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]]

**[undo debugging vxlan neighbor-discovery server**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示ENDS所有调试信息开关。

**[entry**]：表示ENDS表项调试信息开关。

**[error**]：表示ENDS错误调试信息开关。

**[event**]：表示ENDS事件调试信息开关。

**[packet**]：表示ENDS报文调试信息开关。

【描述】

**[debugging vxlan neighbor-discovery server**]命令用来打开ENDS调试信息开关。**undo debugging vxlan neighbor-discovery server**命令用来关闭ENDS调试信息开关。

缺省情况下，ENDS调试信息开关处于关闭状态。

表1-17 debugging vxlan neighbor-discovery server entry命令输出信息描述表

字段

描述

Added client: interface= *interface-name*, network ID= *netid-value*, IP address= *ipaddr-value*.

增加客户，接口为*interface-name*，网络ID为*netid-value*，客户的IP地址为*ip-address*

 

Deleted client: interface= *interface-name*, network ID= *netid-value*, IP address= *ipaddr-value*.

删除客户，接口为*interface-name*，网络ID为*netid-value*，客户的IP地址为*ip-address*

 

表1-18 debugging vxlan neighbor-discovery server error命令输出信息描述表

字段

描述

Failed to create run info.

创建运行信息失败

 

表1-19 debugging vxlan neighbor-discovery server event命令输出信息描述表

字段

描述

Created aging timer: timer interval= *time-value*, timer ID= *id-value*.

创建老化定时器，时间间隔为*time-value*，定时器ID为*id-value*

 

Modified aging timer: timer interval= *time-value*.

修改老化定时器的时间间隔为*time-value*

 

Deleted aging timer: timer id= *id-value*.

删除ID为*id-value*的老化定时器

 

*[interface-name *received interface *event-name*.]

接口*interface-name*收到接口事件，事件类型为*event-name*

*[event-name*]的取值可能为：

·up event：接口up

·down event：接口down

·create event：接口创建

·delete event：接口删除

 

表1-20 debugging vxlan neighbor-discovery server packet命令输出信息描述表

字段

描述

Packet failed authentication.

认证失败

 

Interface *interface-name* received a packet: packet type= *type-value*, network ID= *netid-value*, client address= *ipaddr-value*.

接口*interface-name*收到一个报文：报文类型为*type-value*，对应的网络ID为*netid-value*，客户端服务器IP地址为*ipaddr-value*

*[type-value*]的取值可能为：

·3：注册报文

·4：注册应答报文

·5：注销报文

·6：错误指示报文

 

Interface *interface-name* sent a packet:

packet type= *type-value*, network ID= {.TableTextChar}*netid-value*, client address= {.TableTextChar}*ipaddr-value*.{.TableTextChar}

接口*interface-name*发送一个报文：报文类型为*type-value*，对应的网络ID为*netid-value*，客户端IP地址为*ipaddr-value*

*[type-value*]的取值可能为：

·3：注册报文

·4：注册应答报文

·5：注销报文

·6：错误指示报文

 

Client info: IP address= *ipaddr-value*, system ID= *macaddr-value*, register interval= *time-value*.

报文中携带的客户信息：IP地址为*ipaddr-value*，桥MAC地址为*macaddr-value*，注册时间间隔为*time-value*

 

Packet failed validity check.

合法性检测失败

 

Packet failed header check.

报文头检测失败

 

Packet failed fixed header check.

报文固定头检测失败

 

Packet failed required content check.

报文强制部分检测失败

 

Packet failed extended content check.

报文扩展部分检测失败

 

【举例】

\# 使能ENDS功能，打开ENDS表项调试信息开关，当ENDS收到ENDC的注册报文后会输出下列调试信息。

\<Sysname\> debugging vxlan neighbor-discovery server entry

\*Sep  6 16:49:49:180 2011 Sysname ENDS/7/ENTRY: -MDC=1; Added client: interface= Tunnel0, network ID= 1, IP address= 1.1.1.2.

*// 增加客户，接口为Tunnel0，网络ID为1，客户的IP地址为1.1.1.2*

\# 使能ENDS功能，打开ENDS事件调试信息开关，当ENDS收到ENDC的注册报文后会输出下列调试信息。

\<Sysname\> debugging vxlan neighbor-discovery server event

\*Sep  8 15:21:38:814 2011 Sysname ENDS/7/EVENT: -MDC=1; Created aging timer: time interval= 75s, timer ID= 1.

*// 创建老化定时器，时间间隔为75秒，定时器ID为1*

\# 使能ENDS功能，打开ENDS报文调试信息开关，当ENDS收到ENDC的注册报文后会输出下列调试信息。

\<Sysname\> debugging vxlan neighbor-discovery server packet

\*Sep  6 16:58:30:600 2011 Sysname ENDS/7/PACKET: -MDC=1; Interface Tunnel0 received a packet: packet type= 3, network ID= 1, client address= 1.1.1.2.

*// 接口Tunnel0收到一个报文：报文类型为注册报文，对应的网络ID为1，客户端IP地址为1.1.1.2*

\*Sep  6 17:01:02:276 2011 Sysname ENDS/7/PACKET: -MDC=1; Client info: IP address= 1.1.1.2, system ID= 0011-2200-0101, register interval= 5s.

*// 报文中携带的客户信息：IP地址为1.1.1.2，桥MAC地址为0011-2200-0101，注册时间间隔为5秒*

\*Sep  6 16:58:30:604 2011 Sysname ENDS/7/PACKET: -MDC=1; Interface Tunnel0 sent a packet: packet type= 4, network ID= 1, client address= 1.1.1.2.

*// 接口Tunnel0发送一个报文：报文类型为注册应答报文，对应的网络ID为1，客户端IP地址为1.1.1.2*

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan tunnel**

------------------------------------------------------------------------

【命令】

**[debugging vxlan**[ **tunnel** { **all** \| **error** \| **packet** } [ **interface** **tunnel** *tunnel-number* ]]]

**[undo debugging vxlan**[ **tunnel** { **all** \| **error** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示VXLAN隧道所有调试信息开关。

**[error**]：表示VXLAN隧道错误调试信息开关。

**[packet**]：表示VXLAN隧道报文调试信息开关。

**[interface tunnel** *tunnel-number*]：表示指定Tunnel接口的调试信息开关。*tunnel-number*为Tunnel接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【描述】

**[debugging vxlan tunnel**]命令用来打开VXLAN隧道的调试信息开关。**undo debugging vxlan tunnel**命令用来关闭VXLAN隧道的调试信息开关。

缺省情况下，VXLAN隧道的调试信息开关处于关闭状态。

表1-21 debugging vxlan tunnel error命令输出信息描述表

字段

描述

Packet dropped because the destination tunnel interface was not found.

对出隧道报文进行解封装时，找不到对应的隧道接口，报文被丢弃

Packet dropped because the number of packet loops exceeded six.

本机环回次数超过6次，就丢弃报文

Incorrect VXLAN header.

VXLAN报文头错误

表1-22 debugging vxlan tunnel packet命令输出信息描述表

字段

描述

Tunnel*number* packet: After de-encapsulation, length is *length*

隧道Tunnel*number*报文处理：解封装后，报文长度为*length*字节

Tunnel*number* packet: After encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*number*报文处理：加封装后，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*字节

Before de-encapsulation, *source*-\>*destination* (length = *length*)

解封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*字节

【举例】

\# 打开本端的VXLAN报文调试信息开关。在两台设备之间建立VXLAN隧道，并分别配置参数使隧道接口up。在接收端收到一个经过VXLAN加封装的IP报文，打印如下调试信息。

\<Sysname\> debugging vxlan tunnel packet

\*Sep  6 11:49:46:053 2011 Sysname VXLAN/7/packet: -MDC=1;

 Before de-encapsulation,

   1.1.1.2-\>1.1.1.1 (length = 120)

*// 接收到的报文解封装前，源IP地址为1.1.1.2，目的IP地址为1.1.1.1，报文长度为120字节*

\*Sep  6 11:49:46:053 2011 Sysname VXLAN/7/packet: -MDC=1;

 Tunnel0 packet: After de-encapsulation, length is 84

*// 接收到的报文解封装后，报文长度为84字节*

