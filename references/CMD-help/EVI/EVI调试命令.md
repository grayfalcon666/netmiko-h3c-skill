<!-- CMD-INDEX
  debugging evi isis adj-packet       | 用户视图             | L20
  debugging evi isis all              | 用户视图             | L166
  debugging evi isis error            | 用户视图             | L204
  debugging evi isis event            | 用户视图             | L500
  debugging evi isis graceful-restart | 用户视图             | L756
  debugging evi isis ha               | 用户视图             | L886
  debugging evi isis local-mac        | 用户视图             | L1040
  debugging evi isis misc             | 用户视图             | L1106
  debugging evi isis route            | 用户视图             | L1302
  debugging evi isis self-originate-update | 用户视图             | L1382
  debugging evi isis snp-packet       | 用户视图             | L1522
  debugging evi isis timer            | 用户视图             | L1686
  debugging evi isis update-packet    | 用户视图             | L1784
  debugging evi mac-address           | 用户视图             | L1998
  debugging evi neighbor-discovery client | 用户视图             | L2134
  debugging evi neighbor-discovery server | 用户视图             | L2398
-->

**EVI \-- EVI调试命令 \-- debugging evi isis adj-packet**

------------------------------------------------------------------------

【命令】

**[debugging evi isis adj-packet**[ [ **receive** \| **send** ]  **verbose**   *process-id* ]]

**[undo debugging evi isis adj-packet**[ [ **receive** \| **send** ]  **verbose**   *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：打开接收EVI IS-IS邻居报文的调试信息开关。

**[send**]：打开发送EVI IS-IS邻居报文的调试信息开关。

**[verbose**]：表示显示详细信息，对报文来说显示报文内容。

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis adj-packet**]命令用来打开EVI IS-IS邻居报文调试信息开关。**undo debugging evi isis adj-packet**命令用来关闭EVI IS-IS邻居报文调试信息开关。

缺省情况下，EVI IS-IS进程的邻居报文调试信息开关处于关闭状态。

需要注意的是：

·如果未指定**receive**和**send**参数，则同时显示打开接收和发送EVI IS-IS邻居报文调试信息开关。

·如果未指定进程号，则表示打开所有进程的邻居报文调试信息开关。

表1-1 debugging evi isis adj-packet命令输出信息描述表

字段

描述

Receive a LAN IIH *String* error. IIH discarded

收到Hello报文解析TLV时发生错误，*String*描述了错误原因

IIH *String* with circuit(*PortName*) mismatch

收到的Hello报文的特征与接口*PortName*的特征不匹配，*String*描述了Hello报文与接口不匹配的特征

IIH has the same SNPA with a NBR, but different System ID. The NBR will be down

收到的Hello报文与已有邻居有相同的SNPA地址，但是系统ID不同，将这个邻居置down状态

IIH has the same System ID with a NBR, but different SNPA. The IIH will be discarded

收到的Hello报文与已有邻居有相同的系统ID，但是SNPA地址不同，丢弃该Hello报文

Level-*Number* NBR(*Address*) two way *String*

Level-*Number* 的邻居2-Way检查的结果，*Address*描述了邻居的MAC地址，*String*描述了检查结果，*String*的具体取值包括：

·pass：通过

·fail：不通过

·pend：邻居信息没有收集完整，需要继续等待

System is under disable state, ADJ packet discarded

系统处于去使能状态，丢弃ADJ模块收到的报文

Circuit state is not up, ADJ packet discarded

接口处于非up状态，丢弃ADJ模块收到的报文

Receive a packet from self, ADJ packet discarded

收到的是本设备自己的报文，丢弃ADJ模块收到的报文

Failed to get source MAC address

获取源MAC地址失败

Receive a *String* packet from(*Address*) on circuit(*PortName*)

在接口*PortName*上从地址*Address*收到了*String*类型报文，*String*的具体取值包括：

·Lan L1 Hello：Hello报文

Receive unsupport packet *Number*, ADJ packet discarded

收到了不支持的报文，丢弃ADJ模块收到的报文，*Number*描述了报文的PDU类型值

No enough PDU space for *String*

PDU长度已经达到最大值，无法继续编码，*String*描述了PDU达到最大值的时机

Failed to get ADJ pointer failed for *String*

获取邻居维护的接口下数据指针失败，*String*描述了失败的时机

No extend VLAN to fill the extend VLAN TLV

没有任何扩展VLAN，所以无法对Extend-VLAN TLV进行编码

No need to set AVF VLAN if not DED

不是DED，无需携带AVF VLAN子TLV

*[String* send a hello on circuit(*PortName*) in VLAN *Number*]

DED在接口*PortName*，VLAN *Number*上发送了Hello报文

*[String*]的取值如下：

·DED

·ED

DED send hello failed on circuit(*PortName*) in VLAN *Number*

DED在接口*PortName*，VLAN *Number*上发送Hello报文失败

Failed to get circuit data for Multiport Capability TLV.

无法获取邻居接口数据，封装多端口能力集TLV失败

【举例】

\# 打开所有进程的接收EVI IS-IS邻居报文调试信息开关。

\<Sysname\> debugging evi isis adj-packet

\*Dec 19 11:39:36:066 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-0-ADJ: Level-1 NBR(0011.2200.0201) two way pass.

*[// Level-1*]*的邻居(0011.2200.0201)双向连接检查通过*

**EVI \-- EVI调试命令 \-- debugging evi isis all**

------------------------------------------------------------------------

【命令】

**[debugging evi isis** **all** [ *process-id* ]]

**[undo debugging evi isis all ** *process-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis all**]命令用来打开所有与EVI IS-IS进程相关的调试信息开关。**undo debugging evi isis all**命令用来关闭所有与EVI IS-IS进程相关的调试信息开关。

缺省情况下，所有与EVI IS-IS进程相关的调试信息开关处于关闭状态。

需要注意的是，如果未指定进程号，则表示打开所有进程的所有调试信息开关。

【举例】

\# 打开所有进程的所有与EVI IS-IS进程相关的调试信息开关。

\<Sysname\> debugging evi isis all

**EVI \-- EVI调试命令 \-- debugging evi isis error**

------------------------------------------------------------------------

【命令】

**[debugging evi isis** **error** [ *process-id* ]]

**[undo debugging evi isis error ** *process-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis error**]命令用来打开EVI IS-IS进程错误调试信息开关。**undo debugging evi isis error**命令用来关闭EVI IS-IS进程错误调试信息开关。

缺省情况下，EVI IS-IS进程的错误调试信息开关处于关闭状态。

需要注意的是，如果未指定进程号，则表示打开所有进程的错误调试信息开关。

表1-2 debugging evi isis error命令输出信息描述表

字段

描述

Failed to create *Type* bitmap when *String*

创建bitmap资源失败，* String*描述了失败的时机，*Type*描述了bitmap资源的类型，*Type*的取值可以如下：

·inactive：不活动的

·note：记录的

·add：添加的

·delete：删除的

·saved：保存的

Failed to get mac by vlan, ADJ system data is NULL

通过vlan获取MAC地址失败，邻居维护的系统数据为空

Failed to add local mac entry, ADJ system data is NULL

添加本地MAC地址失败，邻居维护的系统数据为空

Failed to get local MAC of VLAN *Number*

获取VLAN *Number*的本地MAC地址失败

Failed to create new LAV node

创建新的LAV结点失败

Failed to create bitmap to operate *String*

创建一个操作类型为*String*的位图失败

Failed to get extend VLAN

获取扩展VLAN失败

Invalid NULL parameter in getting all AVF information

获取所有AVF信息时无效的NULL参数

Failed to get current LAV when GR finished

获取当前LAV失败，当GR完成时

Failed to alloc r-mac head while *String*

分配r-mac头空间失败，*String*描述了失败的时机

Failed to add r-mac vlan entry, vlan: *Number*

添加r-mac表项失败，VLAN为*Number*

Failed to create r-mac attribute

创建r-mac属性失败

Failed to notify r-mac message

通知r-mac信息失败

LAN ADJ number has arrived max

LAN ADJ数据已达最大值

Failed to get ADJ pointer when starting hello timer

当启动Hello定时间器时，获取ADJ维护数据失败

Failed to start Level-*Number* Hello timer

启动Level *Number*的Hello定时器失败

Failed to start hold timer

启动Hold定时器失败

Failed to get circuit(*PortName*)\'s priority

获取接口*PortName*优先级失败

Failed to get system\'s area address when encoding AREA

获取区域地址失败

Failed to get circuit(*PortName*)\'s MTU

获取接口*PortName*的MTU失败

*[Type* send hello failed on circuit(*PortName*) in VLAN *Number*]

设备类型为*Type*的设备在接口*PortName*，VLAN *Number*上发送Hello报文失败。*Type*的取值可以如下：

·DED

·ED

Failed to send hello packet on circuit(*PortName*)

在接口*PortName*上发送Hello报文失败

Failed to create hello timer  on circuit(*PortName*)

在接口*PortName*上创建Hello定时器失败

Failed to notify LAV change message

通知LAV改变消息失败

Processing interface MTU change error.

处理接口MTU变化事件错误

Failed to active the interface(*interface index*).

激活接口(*interface index*)失败

Notify interface delete error on interface: *interface index*

通知接口*interface index*删除事件错误

Invalid phase *phase-number*, ignore event.

无效的reset阶段，忽略该事件

Failed to create LSP change notify message.

创建LSP变化通知消息失败

PDU level(1) mismatch with circuit level(*CirLevel*).

PDU报文中的level(1)与接口level(*CirLevel*)不匹配

Failed to set updt socket option.

设置updt的socket选项失败

Failed to start *Type* timer on circuit *String*.

在接口*String*上启动定时器失败，*String*的具体取值包括：接口名，*Type*描述了定时器类型：

·CSNP

·PSNP

·LSP

·LSP flooding

Failed to stop LSP  flood timer on circuit *String*.

在接口*String*上停止LSP泛洪定时器失败，*String*的具体取值包括：接口名

Failed to stop level-1 timer on circuit *String*.

在接口*String*上停止Lever-1定时器失败，*String*的具体取值包括：接口名

Failed to insert mac to list

向链表中添加MAC地址失败

Failed to update LSP information

更新LSP信息失败

Failed to insert LSP information

添加LSP信息失败

Circuit(*PortName*) is not operationally on, ignoring PDU

接口*PortName*处于不可操作状态，忽略PDU

Failed to obtain IF net index

获取IF net 索引失败

Failed to send PDU, returns *ReturnLength*, buffer length is *Length*.

发送报文失败，发送缓冲区大小为*Length*，返回值为*ReturnLength*

LSP size(*LspSize*) is larger than circuit MTU(*CirMtu*).

LSP的大小(*LspSize*)大于接口的MTU(*CirMtu*)

Failed to send LSP

发送LSP报文失败

Failed to send level-*Number*  *Type* PDU

发送level-*Number*的*Type*类型报文失败，*Type*的具体取值可以如下：

·CSNP

·PSNP

Failed to install LSP with sequence number zero

安装序号为0的LSP失败

Failed to *Type*  level-*Number* area address *String*

操作level-*Number*区域地址*String*失败,操作类型为*Type*，*Type*的具体取值可以如下

·add：添加

·delete：删除

Failed to *Type* level- *Number* protocol support *ProNumber*(*ProString*).

操作level-*Number*的支持的协议类型*ProNumber*(*ProString*)失败，操作类型为*Type*。

*[ProString*]的具体取值包括：

·EVI-ISIS：EVIIS-IS协议

·unknown：其它协议

*[Type*]的具体取值可以如下：

·add：添加

·delete：删除

Failed to add level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.

添加level- *Number*由*systemID*到*neighbourID*的邻居信息失败

Failed to delete level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.

删除level- *Number*由*systemID*到*neighbourID*的邻居信息失败

Failed to modify level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.

更新level- *Number*由*systemID*到*neighbourID*的邻居信息失败

Failed to add level- *Number* pseudo neighbour: pseudo *pseudoID* =\> neighbour *neighbourID*.

添加level- *Number*由*pseudoID*到*neighbourID*的伪节点邻居信息失败

Failed to delete level- *Number* pseudo neighbour: pseudo *pseudoID* =\> neighbour *neighbourID.*

删除level- *Number*由*pseudoID*到*neighbourID*的伪节点邻居信息失败

【举例】

\# 打开EVI IS-IS协议错误调试信息开关。

\<Sysname\> debugging evi isis error

\*Mar 18 14:28:41:744 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-101-ERR: Failed to send level-1 CSNP PDU.

*// 发送Level-1的CSNP报文失败*

**EVI \-- EVI调试命令 \-- debugging evi isis event**

------------------------------------------------------------------------

【命令】

**[debugging evi isis** **event** [ *process-id* ]]

**[undo debugging evi isis** **event** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis event**]命令用来打开EVI IS-IS进程事件调试信息开关。**undo debugging evi isis event**命令用来关闭EVI IS-IS进程事件调试信息开关。

缺省情况下，EVI IS-IS进程的事件调试信息开关处于关闭状态。

需要注意的是，如果未指定进程号，则表示打开所有进程的事件调试信息开关。

表1-3 debugging evi isis event命令输出的信息描述表

字段

描述

Failed to get local MAC of VLAN *Number*

在VLAN *Number*上获取本地MAC失败

Clear all AVF in circuit *PortName*

清除接口*PortName*上所有 的AVF

DED changed on *PortName*: old DED: *String*, new DED: *String*

接口*PortName*所属网段的DED发生改变，*String*描述了以前的DED和新的DED的MAC地址

System\'s state is disable

系统处于去使能状态

Update proccess(*Number*) configuration to DBM

更新进程(*Number*)的配置数据到DBM

Notify extended VLAN configuration

通知配置扩展VLAN

Evilink Interface is deleted successfully

EVI-Link接口删除成功

Notifing the tunnel interface state changed

通知Tunnel接口状态改变

Notifing the evi-link interface state changed

通知EVI-Link接口状态改变

Refresh the interface parameter on interface: *interface-index*

刷新EVI IS-IS接口*interface-index*下保存的接口的各种参数

Interface *Portname* is created successfully

接口*Portname*创建成功

Interface *Portname* is deleted successfully

接口*Portname*删除成功

LSP MTU change from *value1* to *value2*, notify UPDT MTU change.

通知UPDT模块LSP报文发送的MTU大小由*value1*变为*value2*

Delete interface *interface-index* data from DBM *bActive*

从DBM删除接口*interface-index*下的参数，接口的状态为*bActive*

Receive Delete circuit ack event, flag is *bDel*

收到一个删除接口应答事件，标志为bDel

Reset finished, process with reset code *reason-code.*

复位完成，处理原因码*reason-code*引起的复位。目前存在如下原因码：

·2：reset evi isis命令引起的复位

·3：LSP序列号翻转引起的复位

·6：EVIIS-IS源MAC地址变化引起的复位

·7：协议进程降级引起的复位

Receive *string* event on interface: *interface-index.*

在接口*interface-index*上收到如下事件：

·board insert  event：板插入事件

·board remove event：板拔出事件

·interface add event：接口添加事件

·interface delete event：接口删除事件

·DOWN \--\> UP event：接口UP事件

·UP \--\> DOWN event：接口DOWN事件

·speed change event：接口速率变化事件

·MTU change event：MTU变化事件

·VLAN add event：接口加入VLAN事件

·VLAN delete event：接口离开VLAN事件

·AVF VLAN change event：接口的AVF变化事件

·designated VLAN change event：接口的指定VLAN变化事件

Reset change into phase *phase-code*.

复位进入*phase-code*阶段

·1：STOP WORK

·2：DISABLE

·3：FINAL

Reset processing with backinfo: module *module-number*, event *event-number*, phase *phase-code*.

处理其他模块回复的reset完成事件。

*[module-number*]取值如下：

·1：ADJ模块

·2：LSP模块

·3：DEC模块

*[event-number*]取值如下：

·1：STOP WORK

·2：DISABLE

·3：ENABLE

*[phase-code*]取值如下：

·1：STOP WORK

·2：DISABLE

Reset processing receive event *event-type*.

收到复位事件，事件类型码为*event-type*。目前存在如下复位类型码：

·2：reset evi isis all命令引起的复位

·3：LSP序列号翻转引起的复位

·6：EVIIS-IS源MAC地址变化引起的复位

·7：协议进程降级引起的复位

VLAN config change notify

VLAN配置改变

Reset start up.

复位开始

Flushed Delete_Map event { *interface-name* Remote VLAN *IDR* \--\> Local VLAN *IDL* } to driver

下刷驱动删除接口上的VLAN映射

·*interface-name*：接口名称

·*IDR*：远端VLAN ID

·*IDL*：本地VLAN ID

Flushed Add_Map event { *interface-name* Remote VLAN *IDR* \--\> Local VLAN *IDL* } to driver

下刷驱动添加接口上的VLAN映射

·*interface-name*：接口名称

·*IDR*：远端VLAN ID

·*IDL*：本地VLAN ID

Associated with a track entry

关联了Track

Static MAC filtering policy changed

本地静态MAC地址的过滤规则发生改变

Dynamic MAC filtering policy changed

本地动态MAC地址的过滤规则发生改变

Updated VLAN mapping data to DBM.

更新VLAN映射数据到DBM

Updated RMAC {SiteID *IDS* Remote VLAN *IDR* \--\> Local VLAN *IDL*}

根据VLAN映射更新远端MAC

·*IDS*：站点ID

·*IDR*：远端VLAN ID

·*IDL*：本地VLAN ID

Notified other modules of preferred VLAN configuration change.

通知AEF优先级配置变化

【举例】

\# 打开EVI IS-IS协议事件调试信息开关。

\<Sysname\> debugging evi isis event

\*Jun  8 08:29:44:658 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-101-EVT: Notifing the tunnel interface state changed.

*// 通知Tunnel接口状态改变*

**EVI \-- EVI调试命令 \-- debugging evi isis graceful-restart**

------------------------------------------------------------------------

【命令】

**[debugging evi isis graceful-restart ** *process-id* ]

**[undo debugging evi isis graceful-restart ** *process-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis graceful-restart**]命令用来打开进程的平滑重启调试信息开关。**undo debugging evi isis graceful-restart**命令用来关闭进程的平滑重启调试信息开关。

缺省情况下，EVI IS-IS进程的平滑重启调试信息开关处于关闭状态。

需要注意的是，如果未指定进程号，则表示打开所有进程的平滑重启调试信息开关。

表1-4 debugging evi isis graceful-restart命令输出信息描述表

字段

描述

Graceful-restart complete

平滑重启完成

T3 timer is stoped

T3定时器停止

T3 timer expired before T2 timer

T3定时器在T2定时器之前失效

Level-*Number* T2 timer expired

Level-*Number*的T2定时器失效

Graceful-restart enter *Type*

平滑重启进入*Type*阶段，*Type*指示了类型可以取值如下：

·starting：启动

·restarting：重启

Recieve T2 timer cancel event

收到T2定时器取消事件

Level-*Number* T2 timer is stopped

Level-*Number*的T2定时器停止

Receive module(*Mid*) phase(*Phase*), current phase(*GrPhase*)

收到模块*Mid*的状态*Phase*，当前GR状态是*GrPhase*

Stop level-*Number* T1 timer

停止level-*Number*的T1定时器

Recieve hello with *Type* bit set from circuit: *PortName* Level- *Number*

从接口*PortName*收到hello报文中level- *Number*的*Type*位置位，*Type*位可以取值如下：

·RR：重启请求位

·RA：重启抑制位

Failed to purge level-*Number* LSP

清除level-*Number*的LSP报文失败

Begin to purge local level-*Number* LSP

开始清除本地的level-*Number*的LSP报文

Purge level-*Number* LSP *PseudoId*-*LspNum*

清除level-*Number*的LSP *PseudoId*-*LspNum*报文

End to purge local level-*Number* LSP

结束清除本地的level-*Number* LSP报文

Level-*Number* LSDB synchronization is complete

Level-*Number*的LSDB同步完成

Level-*Number* CSNP set synchronization is complete on circuit *PortName*

Level-*Number*的CSNP设置同步完成在接口*PortName*上

Level-*Number* LSDB synchronization is complete

Level-*Number*的LSDB同步完成

EVIISIS-*Number*-GR: Interface(*interface-index*) level-*Number* T1 timer expired count: *Number*

接口*interface-index*下，Level-*Number*的T1定时器超时*Number*次

【举例】

\# 打开EVI IS-IS进程的平滑重启调试信息开关。

\<Sysname\> debugging evi isis graceful-restart

\*Mar 17 14:25:11:744 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-101-GR: Level- 1  LSDB synchronization is complete.

*[// Level-1*]*的LSDB同步完成*

**EVI \-- EVI调试命令 \-- debugging evi isis ha**

------------------------------------------------------------------------

【命令】

**[debugging evi isis ha**]

**[undo debugging evi isis ha**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging evi isis ha**]命令用来打开EVI IS-IS协议HA调试信息开关。**undo debugging evi isis ha**命令用来关闭EVI IS-IS协议HA调试信息开关。

缺省情况下，EVI IS-IS HA调试信息开关处于关闭状态。

表1-5 debugging evi isis ha命令输出信息描述表

字段

描述

Failed to initialize the PUBLISH when HA

初始化发布事件失败，当HA时

Real time backup *string.*

实时备份EVI IS-IS的各种配置和属性信息。*String*列表：

·eviisis(*Number*) process debugging information：进程调试信息，*Number*：为进程ID

·eviisis system debugging information：系统调试信息

·process(*Number*)：进程配置，*Number*：为进程ID

·interface：接口配置

·process view：进程视图

·process enable：EVIIS-IS进程使能

·designated vlan：指定VLAN

·graceful-restart：平滑重启

·graceful-restart Interval：平滑重启时间间隔

·LSP life time：LSP生命周期

·LSP refresh interval：LSP刷新间隔

·log peer change：邻居状态显示信息

·extend vlan：扩展VLAN

·DED priority：DED优先级

·hello  time interval：Hello报文的发送时间间隔

·CSNP interval：发送CSNP报文的时间间隔

·Hello lapse number：邻居的Hello报文失效数目

·LSP throttle time and LSP throttle count：发送链路状态报文的最小时间间隔和一次最多发送的链路状态报文的数目

Receive HA *string* event.

收到HA *string*通知事件，事件列表：

·EPOLLUP：epoll HUP事件

·batch backup：批量备份事件

·stop：进程停止事件

·degrade：降级事件

·upgrade：升级事件

Reconnecting to HA daemon, Please wait\...

重新连接HA模块，请等待...

Receive EVI-ISIS real-time backup data.

收到EVI IS-IS实备数据

Receive EVI-ISIS batch backup data.

收到EVI IS-IS批量备份数据

Send batch backup data to slave board.

发送批量备份数据到备板

External Deinit

去初始化

Notifying thread to stop work.

通知线程停止工作

Processing the HA upgrade.

处理HA升级事件

HA smooth end

HA平滑结束

HA smooth start

HA平滑开始

No process found. HA smooth ended

不存在任何进程实例，HA平滑结束

External init when HA

初始化HA时

Notifying thread to start work.

通知线程开始工作

Start up EVI-ISIS protocol process when HA upgrade.

开始启动EVI IS-IS协议进程当HA升级时

【举例】

\# 打开EVI IS-IS HA的调试信息开关。

\<Sysname\> debugging evi isis ha

\*Jun  3 09:56:15:006 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-101-HA: Receive HA upgrade event.

*// 收到HA升级事件*

**EVI \-- EVI调试命令 \-- debugging evi isis local-mac**

------------------------------------------------------------------------

【命令】

**[debugging evi isis local-mac** [ *process-id* ]]

**[undo debugging evi isis local-mac** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis local-mac**]命令用来打开EVI IS-IS进程的本地MAC地址信息调试信息开关。用于调试驱动上报的本地MAC地址信息使用。**undo** **debugging evi isis local-mac**命令用来关闭EVI IS-IS进程的本地MAC地址信息调试信息开关。

缺省情况下，EVI IS-IS进程的本地MAC地址信息调试信息开关处于关闭状态。

需要注意的是，如果未指定进程号，则表示打开所有进程的本地MAC地址信息调试信息开关。

表1-6 debugging evi isis local-mac命令输出信息描述表

字段

描述

Receive local MAC, Operation type:O*pType*, MAC type:*MacType*, ifIndex:*ifIndex*, VLAN: *Number*, MAC: *MacAddr*.

收到本地MAC地址信息，VLAN为*Number*，MAC地址为*MacAddr*，操作类型为*OpType*，*OpType*的取值可以如下：

·add：添加

·delete：删除

MAC地址类型为*MacType*，*MacType*的取值可以如下：

·dynamic：动态MAC地址

·static：静态MAC地址

·nonadvertised：非发布MAC地址

【举例】

\# 打开EVI IS-IS进程的本地MAC地址信息调试信息开关。

\<Sysname\> debugging evi isis local-mac

\*Jun  3 09:56:15:911 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

Receive local MAC, Operation type:add, MAC type:dynamic, ifIndex:0x1111, VLAN: 2, MAC: aa-bb-cc.

*// 收到本地MAC，操作类型为add，MAC类型为dynamic，ifIndex为0x1111，VLAN为2，MAC地址为aa-bb-cc*

**EVI \-- EVI调试命令 \-- debugging evi isis misc**

------------------------------------------------------------------------

【命令】

**[debugging evi isis misc**]

**[undo debugging evi isis misc**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging evi isis misc**]命令用来打开与进程无关的其它调试信息开关。**undo debugging evi isis misc**命令用来关闭与进程无关的其它调试信息开关。

缺省情况下，EVI IS-IS的与进程无关的其它调试信息开关处于关闭状态。

表1-7 debugging evi isis misc命令输出信息描述表

字段

描述

Failed to receive local mac message

接收本地MAC消息失败

Failed to create bitmap for publishing LAV

发布LAV时创建位图资源失败

Publish batch Lav info

批量下发LAV信息

Send Lav notify message, event: *EventType*, tunnel index: *TunnelIndex*

发送LAV通知事件消息，事件类型为*EventType*，tunnel接口索引为*TunnelIndex*，*EventType*的取值可以如下：

·ADD：添加

·DEL：删除

Failed to *Opt* VLAN on port, error: *ErrorCode*, EVI link index:* IfIndex*

在接口上操作VLAN失败，错误码为*ErrorCode*，EVI-Link索引为*IfIndex*，操作类型为*Opt*，*Opt*的取值可以如下：

·add：添加

·delete：删除

Process(*PorcId*) is created successfully

进程(*进程ID*)创建成功

Update EVI-ISIS Designated Vlan  to DBM

更新指定VLAN数据到DBM

Failed to create bitmap

创建bitmap资源失败

Failed to connect to *String*

连接*String*模块失败，*String*描述了模块的类型

Send HA response(*String*) error

发送HA应答错误，*String*指示了应答的内容

Starting HA upgrade waiting timer for reset complete

启动HA升级等待定时器为了重启完成

External init error when HA

HA时外部初始化错误

*[Type * the global packet up to CPU]

操作全局的报文是否允许发送到CPU，*Type*描述了操作的类型，Type的取值可以如下：

·enable：允许

·disable：不允许

Receive IFM EPOLLHUP event

收到接口管理的EPOLLHUP事件

Receive SIGKILL signal from SCM

从SCM收到SIGKILL信号

Process is deleted successfully

进程删除成功

Tunnel is deleted successfully

Tunnel接口删除成功

Failed to get system node *Number*

获取系统结点失败，*Number*为系统索引

Receive DEV EPOLLHUP event

收到设备模块发送过来的EPOLLHUP事件

Reconnecting to *String*, please wait\...

重新连接*String*模块，请等待，*String*描述了要连接的模块

Receive VLAN *Type*  event

收到VLAN事件。*Type*描述了事件的类型：

·create

·delete

·EPOLLHUP

External connection of system index *SysINDEX* failed, connectivity set to false.

系统实例索引为*SysINDEX*的外部连接断开，连通性检查失败

Connectivity test passed, connectivity set to true.

连通性检查成功

Neighbor count optType is *type*, current value is *value*.

邻居计数的操作类型为*type*，当前邻居个数为*value*

*[type*]的取值可以如下：

·1：计数加操作

·2：计数减操作

·3：统计清零

The callback track entry doesn\'t match local configuration.

Track模块回调通知的Entry同配置中保存的不一致

Track status: *state*.

Track的连通状态为*state*，*state*的取值可以如下：

·Not ready：监测结果未就绪

·Negative：监测对象工作异常

·Positive：监测对象工作正常

·Unknown：未识别状态

Transport-side connectivity of the intra-site neighbor changed to *value.*

邻居公网侧连通性改变

*[value*]的取值可以如下：

·1：邻居公网侧连通

·0：邻居公网侧不连通

Failed to initialize the TRACK while HA was being performed.

HA的时候Track初始化失败

【举例】

\# 打开接收EVI IS-IS 其它错误调试信息开关。

\<Sysname\> debugging evi isis misc

\*Dec 20 12:24:03:012 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-MISC: Receive VLAN create event.

*// 收到VLAN创建事件*

**EVI \-- EVI调试命令 \-- debugging evi isis route**

------------------------------------------------------------------------

【命令】

**[debugging evi isis route** [ **verbose**   *process-id* ]]

**[undo debugging evi isis route ** **verbose** ]  *process-id*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[verbose**]：打开路由详细调试信息开关。

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis route**]命令用来打开EVI IS-IS进程的路由计算调试信息开关。**undo** **debugging evi isis route**命令用来关闭EVI IS-IS进程的路由计算调试信息开关。

缺省情况下，EVI IS-IS进程路由计算调试信息开关处于关闭状态。

需要注意的是，如果未指定进程号，则表示打开所有进程的路由计算调试信息开关。

表1-8 debugging evi isis route命令输出信息描述表

字段

描述

Flush r-mac, vlan: *Number*, mac: *MacAddr*, action: *Type*

下刷MAC表项，VLAN为*Number*，MAC地址为*MacAddr*，操作类型为*Type*，*Type*的取值可以如下：

·none：无

·add：添加

·delete：删除

·update：更新

Failed to flush r-mac, vlan: *Number*, mac: *MacAddr*, error: *ErrorId*

下刷MAC表项失败，MAC地址为*MacAddr*，错误ID为*ErrorId*

*[Type*]  r-mac entry, vlan: *Number*, mac: *MacAddr*

操作r-mac表项，操作类型为*Type*，具体取值如下：

·Add：添加

·Delete：删除

·Update：更新

·Query：查询

【举例】

\# 打开EVI IS-IS路由计算调试信息开关。

\<Sysname\> debugging evi isis route

\*Jun  3 09:56:15:911 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-101- ROUTE: Updater-mac entry, vlan: 5, mac: aa-bb-cc.

*// 更新r-mac表项，VLAN为5，MAC地址为aa-bb-cc*

**EVI \-- EVI调试命令 \-- debugging evi isis self-originate-update**

------------------------------------------------------------------------

【命令】

**[debugging evi isis self-originate-update ** *process-id* ]

**[undo** **debugging evi isis self-originate-update** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis self-originate-update**]命令用来打开EVI IS-IS进程的本地更新调试信息开关。**undo debugging evi isis self-originate-update**命令用来关闭EVI IS-IS进程的本地更新调试信息开关。

缺省情况下，EVI IS-IS进程的本地更新调试信息开关处于关闭状态。

需要注意的是，如果未指定进程号，则表示打开所有进程的本地更新调试信息开关。

表1-9 debugging evi isis self-originate-update命令输出信息描述表

字段

描述

Purging level-*Number* LSP *LSPId*.*PseudoId* -*LspNum*.

清除level- *Number*的LSP[LSPID.伪节点ID-分片号]

EVI-ISIS(*ProcID*) level- *Number* LSP overflow.

EVIIS-IS进程ID为*ProcID*的level- *Number* LSP已满

The remaining space of level- *Number* fragment 0 LSP is shortage while adding area or protocol support.

当添加区域地址或协议支持时level- *Number*的零分片LSP中剩余空间不足

Rebuilding all level- *Number* LSPs Start.

开始对level- *Number*的所有LSP进行Rebuild操作

Rebuilding all level-*Number* LSPs end.

level-*Number*所有LSP的Rebuild操作结束

MTU change triggers rebuild.

MTU改变触发Rebuild操作

Attempting to exceed max sequence number.

LSP的序列号超过最大值（需要反转）

Generating level- *Number* LSP *LSPId*.*PseudoId* -*LspNum*, Seq *SeqNum*, length *LspLen*.

生成序列号为*SeqNum*长度为*LspLen*的level- *Number* LSP[LSPID.伪节点ID-分片号]

TLV handle triggers rebuild.

LSP处理触发Rebuild操作

LSP lifetime change triggers rebuild.

LSP生存时间触发Rebuild操作

*[Type * level- *Number* area address *String*.]

为level- *Number*操作区域地址，操作类型为*String*

*[Type*]的取值如下：

·1：Added：添加

·2：Deleted：删除

Added level- *Number* protocol support *ProNumber*(*ProString*).

为level- *Number*添加支持的协议类型*ProNumber*(*ProString*)

Deleted level- *Number* protocol support *ProNumber*(*ProString*).

为level- *Number*删除支持的协议类型*ProNumber*(*ProString*)

Added level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.

为level- *Number*添加由*systemID*到*neighbourID*的邻居信息

Deleted level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.

为level- *Number*删除由*systemID*到*neighbourID*的邻居信息

Modified level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.

为level- *Number*更新由*systemID*到*neighbourID*的邻居信息

Added level- *Number* pseudo neighbour: pseudo *pseudoID* =\> neighbour *neighbourID*.

为level- *Number*添加由*pseudoID*到*neighbourID*的伪节点邻居信息

Deleted level- *Number* pseudo neighbour: pseudo *pseudoID* =\> neighbour *neighbourID*.

为level- *Number*删除由*pseudoID*到*neighbourID*的伪节点邻居信息

Failed to add mac address for vlan *Number*

添加VLAN为*Number*的MAC地址失败

Delete mac address for vlan *Number*

删除VLAN为*Number*MAC地址

Delete all mac address for vlan *Number*

删除VLAN为*Number*所有的MAC地址

【举例】

\# 打开EVI IS-IS本地更新调试信息开关。

\<Sysname\> debugging evi isis self-originate-update

\*May 27 15:46:13:289 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-101-ORG: Generating level-1 LSP [0011.2233.4401.00-00, Seq 0x00000001, length 71.]

*// 生成序列号为0x00000001，长度为71的L1 LSP[0011.2233.4401.00-00]*

**EVI \-- EVI调试命令 \-- debugging evi isis snp-packet**

------------------------------------------------------------------------

【命令】

**[debugging evi isis snp-packet **[[ **receive** \| **send** ]  **verbose**   *process-id* ]]

**[undo debugging evi isis snp-packet**[ [ **receive** \| **send** ]  *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：打开接收EVI IS-IS SNP报文的调试信息开关。

**[send**]：打开发送EVI IS-IS SNP报文的调试信息开关。

**[verbose**]：表示显示详细信息，对报文来说显示报文内容。

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis snp-packet**]命令用来打开EVI IS-IS进程的SNP报文调试信息开关。**undo** **debugging evi isis snp-packet**命令用来关闭EVI IS-IS进程的SNP报文调试信息开关。

缺省情况下，EVI IS-IS进程的SNP报文调试信息开关处于关闭状态。

需要注意的是：

·如果未指定**receive**和**send**参数，则同时显示打开接收和发送EVI IS-IS进程的SNP报文调试信息开关。

·如果未指定进程号，则表示打开所有进程的SNP报文调试信息开关。

表1-10 debugging evi isis snp-packet命令输出信息描述表

字段

描述

Receive *PduName* from *SourceId* on circuit *CirName*.

在接口CirName上收到来自于SourceId 的PduName，PduName的具体取值包括：

·L1 CSNP

·L1 PSNP

Receive *PduName* from *SourceId* on circuit *CirName* range from * StartLSPId*.*StartPseudoId* -*StartLspNum* to *EndLSPId*.*EndPseudoId* -*EndLspNum.*

在接口*CirName*上收到来自于*SourceId*的*PduName*，范围为起始LSPID.伪节点ID-分片号，结束LSPID.伪节点ID-分片号

*[PduName*]的具体取值包括：

·L1 CSNP

·L1 PSNP

Failed  to process SNP PDU.

处理SNP 报文失败

Not  find current  LSP entry to build CSNP.

没有找到当前的LSP摘要来创建CSNP

Level-*Number* CSNP  timer expired on a not DED circuit(*String*).

非DED的接口*String*上lever- *Number*的CSNP定时器超时，*String*的具体取值包括：接口名

Send *PduName* on circuit *String*.

在接口*String*上发送*PduName*，*String*的具体取值包括：接口名

*[PduName*]的具体取值包括：

·L1 CSNP

·L1 PSNP

Level-*Number* PSNP timer expired on a DED circuit(*String*).

DED接口*String*上lever- *Number*的PSNP定时器超时，*String*的具体取值包括：接口名

Invalid LSPID  reported in SNP.

SNP中包含无效的LSPID

Wrong LSP entry TLV length(*TlvLen*) in SNP.

SNP中携带错误的LSP摘要TLV长度

SNP contain too much LSP entry.

SNP中包含LSP摘要的个数超过限制

Wrong TLV length in SNP.

SNP中携带错误的TLV长度

Invalid TLV in SNP.

SNP中携带无效的TLV

LSP entry *LSPId*.*PseudoId* -*LspNum* processed, older than LSDB copy.

处理LSP摘要*LSPId*.*PseudoId* --*LspNum*，比LSDB中保存的旧

LSP  entry *LSPId*.*PseudoId* -*LspNum* processed, newer than LSDB  copy.

处理LSP摘要*LSPId*.*PseudoId* --*LspNum*，比LSDB中保存的新

LSP  entry *LSPId*.*PseudoId* -*LspNum* processed, same as LSDB copy.

处理LSP摘要*LSPId*.*PseudoId* --*LspNum*，与LSDB中保存的新旧相同

LSP  entry *LSPId*.*PseudoId* -*LspNum* processed, not exist in LSDB.

处理LSP摘要*LSPId*.*PseudoId* --*LspNum*，在LSDB中不存在

PSNP not processed, current ED is not DED.

当前ED不是DED，不处理PSNP报文

*[SNPType *not processed before DED election.]

在DED选举前不处理*SNPType*报文，*SNPType*的具体取值包括：

·CSNP

·PSNP

Lsp entry *LSPId*.*PseudoId* -*LspNum* is not loaded in CSNP.

在CSNP中没有LSP *LSPId*.*PseudoId* --*LspNum*的摘要

CSNP not processed on DED.

DED上不处理CSNP报文

Invalid type of SNP PDU.

无效的SNP PDU类型

【举例】

\# 打开接收EVI IS-IS SNP报文调试信息开关。

\<Sysname\> debugging evi isis snp-packet receive

\*Dec 19 15:40:51:337 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-0-SNP: Send L1 CSNP on circuit Evi-Link0.

*// 在EVI-Link0上发送Level-1的CSNP报文*

**EVI \-- EVI调试命令 \-- debugging evi isis timer**

------------------------------------------------------------------------

【命令】

**[debugging evi isis** **timer** [ *process-id* ]]

**[undo debugging evi isis timer ** *process-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis timer**]命令用来打开EVI IS-IS进程的定时器调试信息开关。**undo debugging evi isis timer**命令用来关闭EVI IS-IS进程的定时器调试信息开关。

缺省情况下，EVI IS-IS进程的定时器调试信息开关处于关闭状态。

需要注意的是，如果未指定进程号，则表示打开所有进程的定时器调试信息开关。

表1-11 debugging evi isis timer命令输出信息描述表

字段

描述

Start *Type* timer, value is *value*

启动*Type*定时器，时间为*value*，*Type*的取值可以如下：

·T2

·T3

Reset *Type* timer, value is *value*

重置*Type*定时器，时间为*value*，*Type*的取值可以如下：

·T2

·T3

Level-*Number* adjacency hold SystemId timer expired on the circuit *PortName*

接口*PortName*下的level-*Number*的邻居定时器超时

Level-*Number*  hello timer expired on the circuit *PortName*

接口*PortName*下的level-*Number*的Hello定时器超时

Starting waiting timer for max sequence num exceed, time value is *value* ms.

启动LSP序列号达到最大值的翻转等待定时器，定时器时长为value毫秒

Level-*Number* CSNP * *timer expired on the circuit *String*.

接口*String*下的level- *Number* CSNP定时器超时，*String*的具体取值包括：接口名

Level- *Number* flood timer expired on the circuit *String*.

接口*String*下的level-* Number*泛洪定时器超时，*String*的具体取值包括：接口名

Level- *Number* LSP *LSPId*.*PseudoId* -*LspNum* gen timer expired.

level-* Number*的LSP[LSPID.伪节点ID-分片号]生成定时器超时

Start level- *Number* LSP *LSPId*.*PseudoId* -*LspNum* gen timer, time vlaue is *TimeValue*(ms).

启动level-* Number *的LSP[LSPID.伪节点ID-分片号]生成定时器，定时器时长为*TimeValue*(单位毫秒)

Stop level- *Number* LSP *LSPId*.*PseudoId* -*LspNum* gen timer.

停止level-* Number*的LSP[LSPID.伪节点ID-分片号]生成定时器

【举例】

\# 打开EVI IS-IS定时器调试信息开关。

\<Sysname\> debugging evi isis timer

\*Dec 20 10:18:29:955 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-0-TMR: Level-1 hello timer expired on the circuit Evi-Link0.

*[// EVI-Link0*]*上的Lever-1 Hello报文发送定时器超时*

**EVI \-- EVI调试命令 \-- debugging evi isis update-packet**

------------------------------------------------------------------------

【命令】

**[debugging evi isis update-packet**[ [ **receive** \| **send** ]  **verbose**   *process-id* ]]

**[undo debugging evi isis update-packet**[ [ **receive** \| **send** ]  *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：打开接收EVI IS-IS更新模块报文的调试信息开关。

**[send**]：打开发送EVI IS-IS更新模块报文的调试信息开关。

**[verbose**]：表示显示详细信息，对报文来说显示报文内容。

*[process-id*]：要打开的调试信息开关的进程ID。

【描述】

**[debugging evi isis update-packet**]命令用来打开EVI IS-IS进程的更新模块报文调试信息开关。**undo** **debugging evi isis update-packet**命令用来关闭EVI IS-IS进程的更新模块报文调试信息开关。

缺省情况下，EVI IS-IS进程的更新模块报文调试信息开关处于关闭状态。

需要注意的是：

·如果未指定**receive**和**send**参数，则同时打开接收和发送EVI IS-IS进程更新模块报文调试信息开关。

·如果未指定进程，则表示打开所有进程的更新模块报文调试信息开关。

表1-12 debugging evi isis update-packet命令输出信息描述表

字段

描述

Flooding *PduName* *LSPId*.*PseudoId* -*LspNum* on circuit *String*.

在接口*String*上泛洪*PduName*（*LSPId*.*PseudoId* -*LspNum*），*String*的具体取值包括：接口名，*PduName*的具体取值包括：

·L1 LSP

·L1 CSNP

·L1 PSNP

*[Type* *PduName* lspid= *LSPId*.*PseudoId* -*LspNum* seq=*Sequence* ht=*HoldTime* from snpa *SnpaAddr* on circuit *String*.]

在接口*String*上从地址*SnpaAddr* *type*序列号为*Sequence*，时间为*HoldTime*的*PduName*，lspid= *LSPId*.*PseudoId* -*LspNum* seq，*String*的具体取值包括：接口名，

*[type*]的具体取值包括：

·Receive：接收

·Send：发送

*[PduName*]的具体取值包括：

·L1 LSP

*[Type remot*e address*(*vlan *Number:* MAC *MacAddr)*]

对远程地址操作，VLAN为*Number*，MAC地址为*MacAddr*。其中*Type*可以取值如下：

·Add：添加

·Delete：删除

·Modify：修改

LSP\'s sequence number is 0

LSP报文的序列号为0

Illegal is-type in level-1 LSP

无效的类型在Level-1的LSP报文

Check sum is zero

校验和为0

Check sum error

校验和错误

Invalid extended is reachability TLV

不支持的TLV

Support protocol mismatch

支持的协议不匹配

LSP with more than *Count* area addr(es)

LSP中区域地址数量超过最大值

LSP with wrong area addr length *Length*

LSP中区域地址长度错误，长度为*Length*

Lsp with wrong area addr *AreaAddr*

LSP中区域地址错误，地址为*AreaAddr*

Invalid mac reachability TLV

无效的mac TLV

Wrong encoding of area address TLV in LSP

错误的区域地址TLV在LSP报文中

Bad TLV length in the received LSP

收到LSP报文中错误的TLV长度

Own LSP *LSP ID*-*LSP Seq* processed, newer than LSDB copy

处理本地生成的LSP报文序列号比LSDB中新

Other LSP *LSP ID*-*LSP Seq*  processed, newer than LSDB copy

处理非本地的LSP报文,序列号比LSDB中新

LSP  *LSP ID*-*LSP Seq* processed, older than LSDB copy

处理LSP报文，序列号比LSDB中旧

LSP *LSP ID*-*LSP Seq*  processed, same as LSDB copy

处理LSP报文，序列号与LSDB中相同

*[String * LSP *LSP ID*-*LSP Seq* processed, no exist in LSDB]

处理LSP报文，LSDB中不存在，报文类型为*String*，*Sting*的取值可以为：

·other：非本地的

·own：本地的

PDU size(*Size*) is greater than receive buffer size(*SizeBuf*),ignoring PDU

收到的PDU大小(*Size*)大于接收缓冲区大小(*SizeBuf*)，丢弃报文

PDU size(*Size*) is less than common PDU header size(*Len*),ignoring PDU

收到的PDU大小(*Size*)小于PDU正常的报文头长度(*Length)*，丢弃PDU报文

PDU size *Size*) is less than fixed PDU header size(*Len*),ignoring PDU

收到的PDU大小(*Size*)小于PDU填充的报文头长度(*Length)*，丢弃PDU报文

PDU length mismatch: recvLen = *RecvLength*, encodeLen = *EncodeLenght*,ignoring PDU

收到的PDU长度*RecvLength*与报文中指示的长度*EncodeLenght*不匹配，丢弃报文

SNPA address of PDU is the same as the local circuit(*PortName*), ignoring PDU

在接口*PortName*上收到的PDU报文中SNPA的地址与本地一样，丢弃PDU报文

EVI-ISIS process is under disable, ignoring PDU

EVI IS-IS进程处于disable状态，丢弃PDU报文

Failed to Check received packet

检测接收到的报文失败

LSP or SNP PDU common header error, ignoring  PDU

LSP或SNP通用报文头错误，丢弃报文

Received PDU level mismatch

收到的PDU报文级别不匹配

No active neighbour with such snpa(*SnpaAddr*) on the cicuit(*PortName*), ignoring PDU

没有激活的邻居地址是*SnpaAddr*在接口*PortName*上，丢弃报文

Failed to processLSP PDU

处理LSP报文失败

Received PDU is not LSP or SNP, ignoring PDU

收到的PDU报文不是LSP或SNP报文，丢弃报文

【举例】

\# 打开接收EVI IS-IS 更新模块报文调试信息开关。

\<Sysname\> debugging evi isis update-packet receive

\*Jun  8 08:31:21:994 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;

EVIISIS-101-UPDT: Received PDU level mismatch.

*// 收到的PDU报文级别不匹配*

**EVI \-- EVI调试命令 \-- debugging evi mac-address**

------------------------------------------------------------------------

【命令】

**[debugging evi mac-address**  { **info** \| **isis** }]

**[undo debugging evi mac-address**  { **info** \| **isis** }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[info**]：表示下驱动调试信息开关。

**[isis**]：表示来自EVI IS-IS模块消息的调试信息开关。

【描述】

**[debugging evi **]**mac-address**命令用来打开EVI MAC模块的调试信息开关。**undo debugging evi mac-address**命令用来关闭EVI MAC模块的调试信息开关。

缺省情况下，EVI MAC的所有调试信息开关均处于关闭状态。

表1-13 debugging evi mac-address info命令输出信息描述表

字段

描述

*[interface-name*: Set selective-flooding MAC address *mac-address* successfully.]

设置隧道接口*interface-name*的泛洪MAC信息成功

*[interface-name*: Failed to set selective-flooding MAC address *mac-address*.]

设置隧道接口*interface-name*的泛洪MAC信息失败

*[interface-name*: Failed to set selective-flooding MAC address *mac-address* due to insufficient hardware resources.]

由于硬件资源不足，设置隧道接口*interface-name*的泛洪MAC信息失败

*[interface-name*: Set *type* information successfully.]

设置隧道接口*interface-name* *type*信息成功，*type*的取值以及含义如下：

·extern VLAN：扩展VLAN

·active VLAN：激活VLAN

·inactive VLAN：非激活VLAN

·MAC request：本地MAC地址请求

*[interface-name*: Failed to set *type* information.]

设置隧道接口*interface-name type*信息失败，*type*的取值以及含义如下：

·extern VLAN：扩展VLAN

·active VLAN：激活VLAN

·inactive VLAN：非激活VLAN

·MAC request：本地MAC地址请求

*[interface-name*: Failed to set *type* information due to insufficient hardware resources.]

由于硬件资源不足，设置隧道接口*interface-name type*信息失败，*type*的取值以及含义如下：

·extern VLAN：扩展VLAN

·active VLAN：激活VLAN

·inactive VLAN：非激活VLAN

·MAC request：本地MAC地址请求

表1-14 debugging evi mac-address isis命令输出信息描述表

字段

描述

*[interface-name*: Received a(an) *type* message from ISIS.]

隧道接口*interface-name*从EVI IS-IS接收到*type*消息，*type*的取值以及含义如下：

·extern VLAN：扩展VLAN

·active VLAN：激活VLAN

·inactive VLAN：非激活VLAN

·MAC request：本地MAC地址请求

【举例】

\# 打开EVI MAC模块来自EVI IS-IS模块消息的调试信息开关，如果接收到激活VLAN的信息，则会打印如下信息：

\<Sysname\> debugging evi mac-address isis

\*Feb 24 10:50:19:644 2011 Sysname EVIMAC/7/ISIS: -MDC=1; Tunnel101: Received an active VLAN message from ISIS.

*// 隧道接口Tunnel101从EVI IS-IS接收到激活VLAN消息*

\# 打开EVI MAC模块下驱动调试信息开关，配置泛洪MAC时会打印如下驱动信息：

\<Sysname\> debugging evi mac-address info

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 evi selective-flooding mac-address 1113-1113-1113 vlan 1

\*Feb 24 10:50:19:644 2011 Sysname EVIMAC/7/INFO: -MDC=1; Tunnel101: Set selective-flooding MAC address 1113-1113-1113 successfully.

*// 设置隧道接口Tunnel101的泛洪MAC信息成功*

\# 打开EVI MAC模块下驱动调试信息开关，如果激活VLAN的信息下发驱动，则会打印如下信息：

\<Sysname\> debugging evi mac-address info

\*Feb 24 10:50:19:644 2011 Sysname EVIMAC/7/INFO: -MDC=1; Tunnel101: Set an active VLAN information successfully.

*// 设置隧道接口Tunnel101激活VLAN信息成功*

**EVI \-- EVI调试命令 \-- debugging evi neighbor-discovery client**

------------------------------------------------------------------------

【命令】

**[debugging evi neighbor-discovery client**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]]

**[undo debugging evi neighbor-discovery client**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[entry**]：表示表项调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging evi neighbor-discovery client**]命令用来打开ENDC调试信息开关。**undo debugging evi neighbor-discovery client **命令用来关闭ENDC调试信息开关。

缺省情况下，ENDC调试信息开关处于关闭状态。

表1-15 debugging evi neighbor-discovery client entry命令输出信息描述表

字段

描述

Failed to find the server node.

查找服务器节点失败

*[operate-name*: interface= *if-name*, network ID= *netid-value*, IP address= *ipaddr-value.*]

操作表项信息，接口为*if-name*，网络ID为*netid-value*，IP地址为*ip-address*

*[operate-name*]的取值可能为：

·Added neighbor：添加邻居节点

·Deleted neighbor：删除邻居节点

·Added server node：添加服务器节点

·Deleted server node：删除服务器节点

·Added dummy：添加Dummy节点

·Deleted dummy：删除Dummy节点

Added tunnel: interface= *if-name*, peer address= *ipaddr-value.*

添加隧道：接口为*if-name*，对端IP地址为*ipaddr-value*

Deleted tunnel: interface= *if-name*, peer address= *ipaddr-value.*

删除隧道：接口为*ii-name*，对端IP地址为*ipaddr-value*

表1-16 debugging evi neighbor-discovery client error命令输出信息描述表

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

表1-17 debugging evi neighbor-discovery client event命令输出信息描述表

字段

描述

Created *timer-name* timer: timer interval= *time-value*; timer ID= *id-value*.

创建*timer-name*定时器，时间间隔为*time-value*，定时器ID为*id-value*

*[timer-name*]的取值可能为：

·register：注册定时器

·LIPC reconnect：LIPC重连定时器

·neighbor aging：邻居老化定时器

Modified register timer: timer interval= *time-value.*

修改注册定时器的时间间隔为*time-value*

Deleted *timer-name* timer: timer ID= *id-value*.

删除*timer-name*定时器，定时器ID为*id-value*

*[timer-name*]的取值可能为：

·register：注册定时器

·LIPC reconnect：LIPC重连定时器

·neighbor aging：邻居老化定时器

Received EVI tunnel restart event.

收到EVI隧道重启事件

Started ENDP service.

启动ENDP服务

Started smoothing neighbor information.

开始平滑邻居信息

Finished smoothing neighbor information.

邻居信息平滑结束

Stopped ENDP service.

停止ENDP服务

*[if-name* received interface *event-name*.]

接口*if-name*收到接口事件，事件类型为*event-name*

*[event-name*]的取值可能为：

·up event：接口up

·down event：接口down

·create event：接口创建

·delete event：接口删除

表1-18 debugging evi neighbor-discovery client packet命令输出信息描述表

字段

描述

Interface *if-name* received a packet: packet type= *type-value*, networkID= *netid-value*, server address= *ipaddr-value*.

接口*if-name*收到一个报文：报文类型为*type-value*，对应的网络ID为*netid-value*，服务器IP地址为*ipaddr-value*

*[type-value*]的取值可能为：

·3：注册报文

·4：注册应答报文

·5：注销报文

·6：错误指示报文

Interface *if-name* Sent a packet: packet type= *type-value*, networkID= *netid-value*, server address= *ipaddr-value*.

接口*if-name*发送一个报文：报文类型为*type-value*，对应的网络ID为*netid-value*，服务器IP地址为*ipaddr-value*

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

\<Sysname\> debugging evi neighbor-discovery client entry

\*Sep  6 17:14:34:243 2011 Sysname ENDC/7/ENTRY: -MDC=1; Add neighbor: interface= Tunnel1, network ID= 1, IP address= 1.1.1.1.

*// 添加邻居节点，接口为Tunnel1，网络ID为1，邻居的IP地址为1.1.1.1*

\*Sep  6 17:14:34:246 2011 Sysname ENDC/7/ENTRY: -MDC=1; Added Tunnel: interface= Tunnel1, peer address= 1.1.1.1.

*// 添加隧道，接口为Tunnel1，对端IP地址为1.1.1.1*

\# 使能ENDC功能，打开ENDC事件调试信息开关，当ENDC发送注册报文后会输出下列调试信息。

\<Sysname\> debugging evi neighbor-discovery client event

\*Sep  8 15:21:38:814 2011 Sysname ENDS/7/EVENT: -MDC=1; Created register timer: time interval= 15s, timer ID= 10.

*// 创建注册定时器，时间间隔为15秒，定时器ID为10*

\# 使能ENDC功能，打开ENDC报文调试信息开关，当ENDC收到ENDS的应答报文后会输出下列调试信息。

\<Sysname\> debugging evi neighbor-discovery client packet

\*Sep  6 17:22:10:772 2011 Sysname ENDC/7/PACKET: -MDC=1; Interface Tunnel1 received a packet: packet type= 4, network ID= 1, server address= 1.1.1.1.

*// 接口Tunnel1收到一个报文，报文类型为注册应答报文，对应的网络ID为1，服务器IP地址为1.1.1.1*

\*Sep  6 17:22:10:773 2011 Sysname ENDC/7/PACKET: -MDC=1; Peer info: IP address= 1.1.1.1, system ID= 0011-2200-0101.

*// 对端信息：IP地址为1.1.1.1，MAC地址为0011-2200-0101*

**EVI \-- EVI调试命令 \-- debugging evi neighbor-discovery server**

------------------------------------------------------------------------

【命令】

**[debugging evi neighbor-discovery server**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]]

**[undo debugging evi neighbor-discovery server**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[entry**]：表示表项调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging evi neighbor-discovery server**]命令用来打开ENDS调试信息开关。**undo debugging evi neighbor-discovery server**命令用来关闭ENDS调试信息开关。

缺省情况下，ENDS调试信息开关处于关闭状态。

表1-19 debugging evi neighbor-discovery server entry命令输出信息描述表

字段

描述

Added client: interface= *if-name*, network ID= *netid-value*, IP address= *ipaddr-value.*

增加客户，接口为*if-name*，网络ID为*netid-value*，客户的IP地址为*ip-address*

Deleted client: interface= *if-name*, network ID= *netid-value*, IP address= *ipaddr-value.*

删除客户，接口为*if-name*，网络ID为*netid-value*，客户的IP地址为*ip-address*

表1-20 debugging evi neighbor-discovery server error命令输出信息描述表

字段

描述

Failed to create run info.

创建运行信息失败

表1-21 debugging evi neighbor-discovery server event命令输出信息描述表

字段

描述

Created aging timer: timer interval= *time-value*, timer ID= *id-value*.

创建老化定时器，时间间隔为*time-value*，定时器ID为*id-value*

Modified aging timer: timer interval= *time-value*

修改老化定时器的时间间隔为*time-value*

Deleted aging timer: timer id= *id-value*.

删除ID为*id-value*的老化定时器

*[if-name* received interface *event-name*.]

接口*if-name*收到接口事件，事件类型为*event-name*

*[event-name*]的取值可能为：

·up event：接口up

·down event：接口down

·create event：接口创建

·delete event：接口删除

表1-22 debugging evi neighbor-discovery server packet命令输出信息描述表

字段

描述

Packet failed authentication.

认证失败

Interface *if-name* received a packet: packet type= *type-value*, network ID= *netid-value*, client address= *ipaddr-value*.

接口*if-name*收到一个报文：报文类型为*type-value*，对应的网络ID为*netid-value*，客户端服务器IP地址为*ipaddr-value*

*[type-value*]的取值可能为：

·3：注册报文

·4：注册应答报文

·5：注销报文

·6：错误指示报文

Interface *if-name s*ent a packet:

packet type= *type-value*, network ID= *netid-value*, client address= *ipaddr-value*.

接口*if-name*发送一个报文：报文类型为*type-value*，对应的网络ID为*netid-value*，客户端IP地址为*ipaddr-value*

*[type-value*]的取值可能为：

·3：注册报文

·4：注册应答报文

·5：注销报文

·6：错误指示报文

Client info: IP address= *ipaddr-value*, system ID= *macaddr-value*, register interval= *time-value*

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

\<Sysname\> debugging evi neighbor-discovery server entry

\*Sep  6 16:49:49:180 2011 Sysname ENDS/7/ENTRY: -MDC=1; Added client: interface= Tunnel0, network ID= 1, IP address= 1.1.1.2.

*// 增加客户，接口为Tunnel0，网络ID为1，客户的IP地址为1.1.1.2*

\# 使能ENDS功能，打开ENDS事件调试信息开关，当ENDS收到ENDC的注册报文后会输出下列调试信息。

\<Sysname\> debugging evi neighbor-discovery server event

\*Sep  8 15:21:38:814 2011 Sysname ENDS/7/EVENT: -MDC=1; Created aging timer: time interval= 75s, timer ID= 1.

*// 创建老化定时器，时间间隔为75秒，定时器ID为1*

\# 使能ENDS功能，打开ENDS报文调试信息开关，当ENDS收到ENDC的注册报文后会输出下列调试信息。

\<Sysname\> debugging evi neighbor-discovery server packet

\*Sep  6 16:58:30:600 2011 Sysname ENDS/7/PACKET: -MDC=1; Interface Tunnel0 received a packet: packet type= 3, network ID= 1, client address= 1.1.1.2.

*// 接口Tunnel0收到一个报文：报文类型为注册报文，对应的网络ID为1，客户端IP地址为1.1.1.2*

\*Sep  6 17:01:02:276 2011 Sysname ENDS/7/PACKET: -MDC=1; Client info: IP address= 1.1.1.2, system ID= 0011-2200-0101, register interval= 5s.

*// 报文中携带的客户信息：IP地址为1.1.1.2，桥MAC地址为0011-2200-0101，注册时间间隔为5秒*

\*Sep  6 16:58:30:604 2011 Sysname ENDS/7/PACKET: -MDC=1; Interface Tunnel0 sent a packet: packet type= 4, network ID= 1, client address= 1.1.1.2.

*// 接口Tunnel0发送一个报文：报文类型为注册应答报文，对应的网络ID为1，客户端IP地址为1.1.1.2*
