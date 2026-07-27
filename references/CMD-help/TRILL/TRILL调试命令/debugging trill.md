<!-- CMD-INDEX
  debugging trill                     | ]                | L5
-->

**TRILL \-- TRILL调试命令 \-- debugging trill**

------------------------------------------------------------------------

【命令】

**[debugging**[ **trill** { **all** \| **error** \| **event** \| **graceful-restart** \| **ha** \| **self-originate-update** \| **timer** \| **vr** \| { **adj-packet** \| **snp-packet** \| **update-packet** } [ **receive** \| **send** ]  **verbose**   **interface** *interface-type* *interface-number*  \| **route**  **mrc** [ **thread-index** *thread-index*  \| **topo** \| **urc** ]  **verbose**  }]]

**[undo** **debugging** **trill** **[graceful-restart**[ \| **ha** \| **self-originate-update** \| **timer** \| **vr** \| { **adj-packet** \| **snp-packet** \| **update-packet** } [ **receive** \| **send** ] \| **route** [ **mrc** \| **topo** \| **urc** ] }]]

【视图】]

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示TRILL协议所有调试信息开关。

**[error**]：表示TRILL协议错误调试信息开关。

**[event**]：表示TRILL协议事件调试信息开关。

**[graceful-restart**]：表示TRILL协议平滑重启调试信息开关。

**[ha**]：表示TRILL协议HA调试信息开关。

**[self-originate-update**]：表示TRILL协议本地更新调试信息开关。

**[timer**]：表示TRILL协议定时器调试信息开关。

**[vr**]：表示TRILL协议VR（Virtual Router，虚拟路由器）调试信息开关。

**[adj-packet**]：表示TRILL协议邻居报文调试信息开关。

**[snp-packet**]：表示TRILL协议SNP报文调试信息开关。

**[update-packet**]：表示TRILL协议更新报文调试信息开关。

**[receive**]：表示接收的TRILL协议报文调试信息开关。

**[send**]：表示发送的TRILL协议报文调试信息开关。

**[verbose**]**：**表示TRILL协议的详细调试信息开关。

**[interface** *interface-type* *interface-number*]：指定接口类型和名称。如果未指定本参数，表示所有接口。

**[route**]：表示TRILL协议路由计算调试信息开关。

**[mrc**]：表示TRILL协议组播路由计算调试信息开关。

**[thread-index** *thread-index*]：指定组播路由的线程，*thread-index*为线程索引号，取值范围为1～当前最大线程数。如果未指定本参数，表示所有线程。

**[topo**]：表示TRILL协议路由调度和拓扑变化调试信息开关。

**[urc**]：表示TRILL协议单播路由计算调试信息开关。

【描述】

**[debugging** **trill**]命令用来打开TRILL协议的调试信息开关。**undo** **debugging** **trill**命令用来关闭TRILL协议的调试信息开关。

缺省情况下，TRILL协议的调试信息开关处于关闭状态。

需要注意的是，如果未指定**receive**和**send**参数，则同时打开接收和发送TRILL协议报文的调试信息开关。

表1-1 debugging trill error命令输出信息描述表

字段

描述

Get system\'s area address failed when encoding AREA

对AREA TLV进行编码时，未能获取到系统提供的区域地址

DRB/RB send HELLO failed on circuit(*port*) in VLAN *vlan-id*

DRB/RB在接口*port*的VLAN *vlan-id*内发送Hello报文失败

RB send HELLO failed on circuit(*port*) in designated VLAN *vlan-id*

RB在接口*port*的指定VLAN *vlan-id*内发送Hello报文失败

Failed to send TCN/MTU-ack on circuit(*port*) in VLAN *vlan-id*

在接口*port*的VLAN *vlan-id*内发送TCN/MTU-ack报文失败

LAN ADJ number has arrived max

邻居数量达到最大值

Get TRILL HELLO/MTU/BPDU socket failed

获取TRILL报文Hello/MTU/BPDU相关的socket失败

IF index *port* set *packet* option *index* failed

在接口*port*上设置报文Hello/MTU/BPDU的*index*选项失败

Level-1 Hello timer start failed

Level-1的Hello定时器启动失败

UPDT Module NBR TLV Modify Failed

修改UPDT模块的邻居TLV失败

Hold timer start failed

保持定时器启动失败

Get circuit(*port*)\'s *string* failed

获取接口*port*的*string*参数失败。*string*包括：

·priority：表示优先级

·MTU：表示最大报文长度

Get adj pointer failed when starting hello timer

当开启Hello定时器时，获取ADJ指针失败

Invalid adj pointer when getting designated vlan information

当获取指定VLAN时，ADJ指针无效

Hello packet send failed on circuit(*port*)

在接口*port*上发送Hello报文失败

Hello timer create failed on circuit(*port*)

在接口*port*上创建Hello定时器失败

Failed to create timer *string*

创建定时器失败，*string*为定时器创建失败的时机

Failed to get memory for *string*

创建数据时分配资源失败，*string*为分配资源失败的时机

Failed to get local DRB when filter the AVF

相同链路多端口识别时，无法找到本RB的DRB

Failed to create bit map for *string*

创建位图资源失败，*string*为创建失败的时机

Failed to get group router information when checking update

更新检查时获取组播路由器信息失败

Failed to get buffer when sending MTU-ack

发送MTU-ack报文时获取资源失败

Invalid NULL parameter in getting AVF information

入参数为空，错误

Failed to create nexthop attribute.

创建下一跳属性失败

Failed to notify next hop message.

通知下一跳信息失败

Failed to get SPF node.

获取SPF节点失败

Failed to create/get AVF node.

创建/获取AVF信息节点失败

Failed to create AVF attrib.

创建AVF属性失败

Failed to notify AVF message.

通知AVF信息失败

Failed to create IPv4 multicast router attrib.

创建IPv4组播路由器属性失败

Failed to notify IPv4 multicast router message.

通知IPv4组播路由器属性失败

Failed to create IPv6 multicast router attrib.

创建IPv6组播路由器属性失败

Failed to notify IPv6 multicast router message.

通知IPv6组播路由器属性失败

Failed to create multicast receiver attrib.

创建组播接收者属性失败

Failed to notify multicast receiver message.

通知组播接收者属性失败

Failed to create used tree attrib.

创建RB声明使用的分发树属性失败

Failed to notify used tree message.

通知RB声明使用的分发树属性失败

Failed to create spf node attrib.

创建SPFNode属性失败

Failed to notify spf node message.

通知SPFNode属性失败

Failed to create spf link attrib.

创建SPFLink属性失败

Failed to notify spf link message.

通知SPFLink属性失败

Failed to find D-node while adding D-link.

在添加D-link的时候查找D-node失败

Failed to load root D-node.

加载根D-node失败

Failed to add VN head, NBR id is *id*.

添加VN head失败，NBR ID为*id*

Failed to alloc VN head while caching prefix, NBR id is *id*.

缓存前缀时分配VN head失败，NBR ID为*id*

Failed to alloc prefix head while caching prefix, NBR id is *id*.

缓存前缀时分配prefix head失败，NBR ID为*id*

The flush table size is zero.

下刷表的大小是零

The flush table is not empty.

下刷表不为空

Failed to create Ingress/port/TVMac/TVlan/RPF/Tree entry.

创建Ingress/端口节点/TVMac/TVlan/RPF/组播分发树表项失败

Failed to create local entry attrib.

创建本地端口列表属性失败

Failed to notify local entry message.

通知本地端口列表属性失败

Failed to get Ingress entry.

获取Ingress表项失败

Failed to find d-tree node *id*.

获取D-node失败，source ID为*id*

Failed to find self dtree node.

获取当前RB对应的D-node失败

Failed to get source id by nickname.

根据Nickname获取D-node失败

Failed to get port info of dtree link.

获取D-link的端口信息失败

Failed to create calc tree attrib.

创建待计算的分发树属性失败

Failed to notify calc tree message.

通知待计算的分发树属性失败

(N*id*) Failed to build nexthop head list.

（N*id*）构造nexthop head链表失败，*id*表示NBR ID

Failed to expand NBR array, error is *error*, index is *index*.

扩展NBR数组失败，错误码为*error*，索引为*index*

Failed to alloc NBR/id node memory.

申请NBR/id node内存失败

Create new TMFibNode error.

创建TMFibNode失败

(L*level*:P*prefix*) Failed to build nexthop list.

（L*level*:P*prefix*）构造nexthop链表失败。*level*表示级别，*prefix*表示前缀

(M*id*:L*level*) Failed to calculate unicast route, prefix is P*prefix*.

（M*id*:L*level*）计算单播路由失败。*id*表示拓扑ID，*level*表示级别，*prefix*表示前缀

Failed to create flush table.

创建下刷表失败

Get interface index failed.

没有获取到接口索引

Flush/Clean TMNG information failed.

下刷/清除TMNG信息失败

Interface(*port*) cost exceeds max value.

接口*port*的cost值超过最大值

MTU size exceeds max PDU size (*size*), setting it to max PDU size.

接口MTU超过最大PDU值*size*，设置其等于最大PDU

Create VLAN BITMAP failed.

创建VLAN位图资源失败

Get interface enable VLAN failed.

获取接口使能VLAN失败

Processing interface MTU change error.

处理接口MTU变化事件错误

The interface(*port*) active failed.

激活接口*port*失败

Notify interface delete error on interface: *port*

通知接口*port*删除事件错误

Invalid phase *phase*, ignore event.

无效的*phase*阶段，忽略该事件

The event type and disable phase mismatch.

事件类型与关闭阶段不匹配

Connect to *module* daemon failed.

连接到*module*模块失败。*module*包括：

·HA：表示高可用性模块

·IFM：表示接口管理模块

·KERNEL：表示内核模块

·DEV：表示设备管理模块

·MCS：表示二层组播模块

·VLAN：表示VLAN管理模块

Send HA response(*type*) error.

向HA模块发送*type*响应错误。*type*包括：

·BATCH_OVER：表示批量备份结束

·UPGRADE_OVER：表示升级结束

·STOP_OVER：表示停止结束

External init error.

升级时外部初始化错误

Invalid MAC type.

无效的MAC地址类型

Create BITMAP failed.

创建位图资源失败

Get/Set port enabled VLAN failed.

获取/设置端口使能VLAN失败

VLAN handle moved from epoll failed.

从EPOLL中移除VLAN句柄失败

Failed to create lsp change notify message.

创建LSP变化通知消息失败

Failed to set updt socket option.

设置updt的socket选项失败

Failed to start csnp/psnp/lsp flood timer on circuit *port*.

在接口*port*上启动CSNP/PSNP/LSP泛洪定时器失败

Failed to stop lsp flood/level-1 timer on circuit *port*.

在接口*port*上停止LSP泛洪/level-1定时器失败

Failed to insert neighbor/group record/nickname to list.

将邻居信息/组地址记录/Nickname加入列表失败

Lsp info update failed.

更新LSP信息失败

Lsp insert failed.

添加LSP失败

Failed to send pdu, returns *return*, buffer length is *length*.

发送报文失败，发送缓冲区大小为*length*，返回值为*return*

Lsp size(*size*) is larger than circuit mtu(*mtu*).

LSP的大小*size*大于接口的MTU值*mtu*

Lsp send failed.

发送LSP报文失败

Send level-1 CSNP/PSNP pdu failed.

发送level-1的CSNP/PSNP报文失败

Failed to install lsp with seq number zero.

安装序号为0的LSP失败

Failed to add/delete level-1 area address *address*.

添加/删除level-1的区域地址*address*失败

Failed to add/delete level-1 protocol support *ProNumber*(*ProString*).

添加/删除level-1支持的协议类型*ProNumber*(*ProString*)失败。*ProString*包括：

·TRILL：表示TRILL协议

·unknown：表示其它协议

Failed to create timer after sending TCN

发送TCN后定时器创建失败

Failed to add/delete/modify level-1neighbour: system *system* =\> neighbour *neighbour*.

添加/删除/更新level-1由*system*到*neighbour*的邻居信息失败

Failed to add/delete level-1 pseudo neighbour: pseudo *pseudo* =\> neighbour *neighbour*.

添加/删除level-1由*pseudo*到*neighbour*的伪节点邻居信息失败

Failed to insert local/other nickname to tree root list.

将本地/其它Nickname加入分发树树根列表失败

No valid nickname.

没有可用的Nickname

Failed to add remote nickname(*remote*) to db.

将远端Nickname *remote*加入Nickname数据库失败

PDU level(1) mismatch with circuit level(*level*).

PDU报文中的level(1)与接口级别*level*不匹配

表1-2 debugging trill event命令输出信息描述表

字段

描述

DRB changed on *port*: old DRB: *mac1*, new DRB: *mac2*

接口*port*所属网段的DRB发生改变，旧DRB和新DRB的MAC地址分别为*mac1*和*mac2*

System\'s state is disable

系统处于关闭状态

Update *string* to DBM

更新配置到DBM，*string*包括：proc enable/trill enable/trees calculate/tree root priority/lsp refresh timer/lsp max age timer/log peer change switch

Update *string* to DBM on the interface *port,* flag is *flag*.

更新接口*port*上的配置到DBM，*flag*为删除标记，*string*包括：HELLO holding multiplier/CSNP timer/hello timer/drb priority/trill link type/avf inhibited timer/Lsp throttle

Delete interface *name* data from DBM *active*.

删除DBM中的接口配置数据，*name*为接口名，*active*为DBM状态

No need to add receiver for it already exist

无需添加组播接收者信息，因为已存在相同的信息

No need to delete receiver for it is to be used

无需删除组播接收者信息，因为已不存在

None of the port is AVF when receiving MCS information

二层组播报文中的接口都不是AVF，无需处理此报文

Ready to process MCS information for circuit *port* AVF change

准备处理接口*port*收到的二层组播报文

Clear all AVF in circuit *port*

清除接口*port*上的所有AVF

The new AVF is same as the current, no neet to process

新分配的AVF与当前AVF相同，无需处理

VLAN *vlan-id* is already inhibited, reset the timer

VLAN *vlan-id*已被抑制，重置抑制定时器

Circuit *port* is already inhibited, no need to notify inhibit of VLAN *vlan-id*

接口*port*已经全局抑制，无需单独进行VLAN *vlan-id*的抑制

Circuit *port* is already inhibited, reset the timer.

接口*port*已经全局抑制，重启定时器

No need to filter for *string*

无需进行相同链路多端口识别，*string*为不进行该处理的原因

Enable the interface *port* packet send to CPU.

通知驱动在接口*port*上送/停止上送协议报文

Disable the interface *port* packet send to CPU.

通知驱动在接口*port*停止上送协议报文

Flush/Clean the TMNG information to interface *port*.

下刷/清除接口*port*的TRILL管理信息

Flush TMNG port link type/enable to interface *por*t.

下刷TMNG端口链路类型/enable到接口*por*t.

Set TRILL PDU/ BPDU up to CPU, flag is *flag*, ifindex is *ifindex*, Mac is *mac*, result is *result.*

向CPU上送TRILL报文，*flag*表示使能标记，*ifindex*表示索引，*mac*表示MAC地址，*result*表示返回值

Reset TMNG port enable/ link type to LAGG member interface *port.*

成员端口向内核重新下刷接口上的管理信息

Flush TMNG port enable/ link type/ AVF/ default VLAN to LAGG member interface *port*.

成员端口向内核下刷接口上的管理信息

Clean all TMNG information to LAGG member interface *port*..

清除成员端口的管理信息

Failed to get speed from interface *port.*

获取接口速率失败

MTU size is not equal to default PDU size (*size*), setting it to default PDU size.

当MTU大小不等于默认大小时，设置成默认值

Interface: *ifindex* leave LAGG, clean the initial TRILL config.

接口离开清除配置

Interface: *ifindex* leave LAGG, set the new TRILL config.

接口离开设置配置

TMNG smooth end.

设备平滑结束

Flush TMNG nickname *name*.

下刷设备名称

Start TMNG smooth.

开始平滑

(MT*index*) *string* level-1 compute tree root nickname *name* to dec.

向DEC更新level-1计算树根，*index*拓扑ID，*string*:Add/Delete/Modify，*name*表示名字

Notifing the TRILL interface state changed.

通知其它线程TRILL接口状态改变

Refresh the TRILL interface parameter on interface: *port*

刷新TRILL接口*port*下保存的接口的各种参数

LSP MTU change from *value1* to *value2*, notify UPDT MTU change.

通知UPDT模块LSP报文发送的MTU大小由*value1*变为*value2*

Receive *event* event on interface: *port.*

在接口*port*收到*event*事件。*event*包括：

·board insert event：表示板插入事件

·board remove event：表示板拔出事件

·interface add event：表示接口添加事件

·interface delete event：表示接口删除事件

·DOWN \--\> UP event：表示接口UP事件

·UP \--\> DOWN event：表示接口DOWN事件

·speed change event：表示接口速率变化事件

·MTU change event：表示MTU变化事件

·VLAN add event：表示接口加入VLAN事件

·VLAN delete event：表示接口离开VLAN事件

·AVF VLAN change event：表示接口AVF变化事件

·designated VLAN change event：表示接口指定VLAN变化事件

Receive IFM EPOLLHUP event.

收到接口管理模块的EPOLL异常事件

Reconnect to *module* daemon successful, Please wait\...

和*module*模块连接成功，请等待。*module*包括：

·IFM：表示接口管理模块

·KERNEL：表示内核模块

·DEV：表示设备管理模块

·MCS：表示二层组播模块

·VLAN：表示VLAN管理模块

Reset finished, process with reset code *code.*

复位完成，处理原因码*code*引起的复位。*code*包括：

·2：表示reset TRILL命令引起的复位

·3：表示LSP序列号翻转引起的复位

·6：表示TRILL源MAC地址变化引起的复位

·7：表示协议进程降级引起的复位

Reset processing with backinfo: module *module*, event *event*, phase *phase*.

处理*module*模块回复的reset完成事件，事件为*event*，阶段为*phase*。*module*包括：

·1：表示ADJ模块

·2：表示LSP模块

·3：表示DEC模块

*[event*]包括：

·1：表示STOP WORK事件

·2：表示DISABLE事件

·3：表示ENABLE事件

*[phase*]包括：

·1：表示STOP WORK阶段

·2：表示DISABLE阶段

Reset change into phase *phase*.

复位进入*phase*阶段。*phase*包括：

·1：表示STOP WORK阶段

·2：表示DISABLE阶段

·3：表示FINAL阶段

Reset processing receive event *event*.

收到复位事件*event*。*event*包括：

·2：表示reset TRILL命令引起的复位

·3：表示LSP序列号翻转引起的复位

·6：表示TRILL源MAC地址变化引起的复位

·7：表示协议进程降级引起的复位

Reset start up.

复位开始

Receive SIGKILL signal from SCM.

从SCM模块接收到SIGKILL信号

Receive *module* EPOLLHUP or EPOLLERR event.

从*module*模块接收到EPOLLHUP事件。*module*包括：

·IFM：表示接口管理模块

·KERNEL：表示内核模块

·DEV：表示设备管理模块

·MCS：表示二层组播模块

·VLAN：表示VLAN管理模块

·MemAlert：表示门限告警模块

*[Action* compute tree list to dec.]

向路由计算*Action*计算的分发树列表。*ActionType*包括：

·Add：表示添加

·Delete：表示删除

·Modify：表示更新

Get *TreeNum* nickname(s) for distribution tree root list.

为分发树树根列表获取*TreeNum*个Nickname

The highest priority tree root takes *NickNum* nickname(s), needs *Number*.

最高优先级树根携带*NickNum*个Nickname，需要*Number*个

表1-3 debugging trill graceful-restart命令输出信息描述表

字段

描述

Stop level-1 T1 timer.

停止level-1的T1定时器

Receive level-1 hello with RR bit set from circuit(*port*) in vlan 10, Ignored.

接口*port*上收到VLAN 10中RR位置位的Level-1 Hello报文（非指定VLAN下收到的），忽略该报文

Receive level-1 hello with RR bit set from circuit(*port*) in vlan 10.

接口*port*上收到VLAN 10中RR位置位的Level-1 Hello报文

Receive level-1 hello with RA bit set from circuit(*port*).

接口*port*上收到RA位置位的Level-1 Hello报文

Level-1 neighbor(*neighbor*) SA bit set, adjacency not advertised.

Level-1的邻居*neighbor*的SA位置位，抑制邻居路由发布

Level-1 neighbor(*neighbor*) SA bit clear, adjacency advertised.

Level-1的邻居*neighbor*的SA位未置位，不抑制邻居路由发布

Receive level-1 hello with SA bit changed from circuit(*port*) in VLAN 1.

接口*port*上收到VLAN 1中SA位置位情况已改变的Level-1 Hello报文

Interface(*port*) level-1 T1 timer expiration count: 2.

接口*port*上level-1的T1定时器超时次数为2次

Level-1T1 timer has stopped.

Level-1的T1定时器停止

Notify SPF calculate completed,Calc Type: *number*

通知SPF计算完毕。*number*包括：

·1：表示单播路由

·2：表示组播路由

·3：表示单播、组播路由一起通知

Notify SPF calculate,Calc Type: *number*

通知进行SPF计算。*number*包括：

·1：表示单播路由

·2：表示组播路由

·3：表示单播、组播路由一起通知

Failed to purge LSP

清除LSP失败

Begin to purge local LSP.

开始清除本地LSP

Purge LSP *id*.*pseudo*-n*um*.

清除LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

End to purge local LSP.

清除本地LSP结束

LSDB synchronization is complete

LSDB同步完成

CSNP set synchronization is complete on circuit  *port*.

接口*port*上CSNP同步完成

Graceful-restart complete.

平滑重启完成

T3 timer is stoped.

T3定时器停止

Enter MCS synchronization phase.

进入MCS同步阶段

Enter SPF phase.

进入SPF阶段

T3 timer expired before T2 timer.

T3定时器比T2定时器提前超时

Level-1 T2 timer expired.

Level-1的T2定时器超时

Graceful-restart enter *type*.

开始*type*类型的平滑重启。*type*包括：

·Starting

·Restarting

Receive T2 timer cancel event

收到停止T2定时器的事件

Level-1 T2 timer is stopped.

Level-1的T2定时器停止

Receive Mcs notify back flag: *number*

收到获取二层组播数据完毕。*number*包括：

·1：表示IPv4

·2：表示IPv6

Enter LSP generation phase.

进入LSP生成阶段

表1-4 debugging trill ha命令输出信息描述表

字段

描述

RtBackup TRILL *string.*

实时备份TRILL的各种配置和属性信息。*string*包括：

·process enable：表示TRILL协议进程使能

·Debugging information：调试信息

·HA Debugging information：HA调试信息

·interface enable：表示接口使能TRILL

·distribution tree number：表示分发树数量

·distribution tree priority：表示分发树优先级

·LSP refresh Interval：表示LSP刷新间隔

·LSP life time：表示LSP生命周期

·log peer change：表示TRILL邻接状态输出开关

·HELLO time interval：表示Hello报文的发送时间间隔

·CSNP interval：表示发送CSNP报文的时间间隔

·HELLO lapse number：表示邻居的Hello报文失效数目

·DRB priority：表示接口DRB优先级

·link type：表示TRILL端口类型

·AVF inhibited time：表示AVF检测到冲突时抑制自己的时间

·LSP throttle time and LSP throttle count：表示发送链路状态报文的最小时间间隔和一次最多发送的链路状态报文的数目

·Nickname：表示RB的Nickname

·interface delete：表示删除接口

Reconnect to HA daemon successful.

重新连接HA守护进程成功

Receive HA EPOLLHUP or EPOLLERR event.

收到HAEPOLLHUP或EPOLLERR事件

HA upgrade, start TMNG smooth.

HA升级，开始平滑

Receive TRILL real-time backup data.

收到TRILL实备数据

Receive TRILL batch backup data.

收到TRILL批量备份数据

Receive HA *event* event.

收到HA通知事件*event*。*event*包括：

·batch backup：表示批量备份事件

·stop：表示进程停止事件

·degrade：表示降级事件

·upgrade：表示升级事件

Receive Memory High/Low Threshold event.

收到内存高/低门限事件

Send batch backup data to slave board.

发送批量备份数据到备板

Notifying thread to stop work.

通知线程停止工作

Processing the HA upgrade.

处理HA升级事件

Notifying thread to start work.

通知线程开始工作

Start up TRILL protocol process.

开始启动TRILL协议进程

表1-5 debugging trill self-originate-update命令输出信息描述表

字段

描述

Purging level-1 LSP \*id*.*pseudo*-*num*.

清除level-1的LSP。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

*[String* into level-1 LSPs, TLV: *TlvType*.]

在level-1的LSP中*type* TLV。*type*包括：

·Adding router capability：表示添加路由能力

·Adding neighbor：表示添加邻居

·Adding group address：表示添加组地址

The remaining space of level-1 fragment 0 LSP is shortage.

level-1的零分片LSP中剩余空间不足

level-1 LSP over flow.

level-1的LSP已满

LSP lifetime change triggers rebuild.

LSP生存事件改变出发重建

The remaining space of level-1 fragment 0 LSP is shortage while adding area or protocol support.

当添加区域地址或协议支持时level-1的零分片LSP中剩余空间不足

Rebuilding all level-1 LSPs Start.

开始对level-1的所有LSP进行Rebuild操作

Rebuilding all level-1 LSPs end.

level-1所有LSP的Rebuild操作结束

MTU change triggers rebuild.

MTU改变触发Rebuild操作

Attempting to exceed max sequence number.

LSP的序列号超过最大值（需要反转）

Generating level-1 LSP *id*.*pseudo*-*num*, Seq *number*, length *length*.

生成序列号为*number*、长度为*length*的level-1的LSP。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

TLV handle triggers rebuild.

LSP处理触发Rebuild操作

Added level-1 area address *String*.

为level-1添加区域地址String

Deleted level-1 area address *String.*

为level-1添加区域地址String

Added/Deleted level-1 protocol support *ProNumber*(*ProString*).

为level-1添加/删除支持的协议类型*ProNumber*(*ProString*)

Added/Deleted/Modified level-1 neighbour: system *system* =\> neighbour *neighbour*.

为level-1添加/删除/更新由*system*到*neighbour*的邻居信息

Added/Deleted level-1 pseudo neighbour: pseudo *pseudo* =\> neighbour *neighbour*.

为level-1添加/删除由*pseudo*到*neighbour*的伪节点邻居信息

Added/Deleted group address for vlan *vlan-id*.

添加/删除VLAN *vlan-id*的组地址信息

Deleted all group address for vlan *vlan-id*.

删除VLAN *vlan-id*下的所有组地址信息

Failed to delete all group address for vlan *vlan-id*

删除VLAN *vlan-id*下的所有组地址信息失败

Added trill version.

添加TRILL版本信息

Failed to add trill version.

添加TRILL版本信息失败

Added/Deleted/Modified local nickname *local*.

添加/删除/更新本地Nickname *local*

Failed to add/delete/modify local nickname *local*.

添加/删除/更新本地Nickname *local*失败

Modified trees information.

更新分发树计算信息

Failed to modify trees information.

更新分发树计算信息失败

Added/Deleted tree root nickname *local*.

添加/删除树根Nickname *local*

Failed to add/delete tree root nickname *local*.

添加/删除树根Nickname *local*失败

Added/Deleted/Modified interested vlan(start *start*, end *end*).

添加/删除/更新关注的VLAN，VLAN范围为*start*到*end*

Failed to add/delete/modify interested vlan(start *start*, end *end*).

添加/删除/更新关注的VLAN失败，VLAN范围为*start*到*end*

Modified nickname in all interested vlans.

更新所有关注VLAN中的Nickname

Failed to modify nickname in all interested vlans.

更新所有关注VLAN中的Nickname失败

Failed to add MAC TLV for VLAN *vlan-id*.

为VLAN *vlan-id*添加MAC TLV失败

Delete GMAC TLV for VLAN *vlan-id*.

为VLAN *vlan-id*删除GMAC TLV

Generated nickname is *local*.

生成的Nickname为*local*

Local nickname is valid, nickname is *local*.

本地Nickname为有效值，为*local*

表1-6 debugging trill timer命令输出信息描述表

字段

描述

Level-1 adjacency *SystemId* hold timer expired on the circuit *CircName*.

在链路*CircName*上的Level-1邻居Holdtime定时器

(M*Number*) Start SPF timer, value is *value* ms.

（拓扑*Number*）启动SPF定时器，其值为*value*毫秒

(M*Number*) Stop SPF timer.

（拓扑*Number*）停止SPF定时器

(M*Number*) SPF timer expired.

（拓扑*Number*）的SPF定时器超时

Starting timer for reconnect to HA/IFM daemon, time value is *value* ms.

开启重连HA/IFM定时器，其值为*value*毫秒

Starting HA upgrade waiting timer for reset complete.

为重启开始HA升级等待定时器

Stop waiting timer for max sequence number exceed/smooth end, timer ID is *value*.

超过最大序列号/平滑结束停止等待定时器，定时器ID为*value*

Starting waiting timer for max seq num exceed/smooth end, time value is *value* ms.

启动LSP序列号达到最大值/smooth end的翻转等待定时器，其值为*value*毫秒

Level-1 *type* timer expired on the circuit CSNP/PSNP.

接口*port*下的level-1的CSNP/PSNP定时器超时

Level-1 flood timer expired on the circuit *String*.

接口*String*下的level-1泛洪定时器超时

Level-1 LSP *id*.*pseudo*-*num* gen timer expired.

level-1的LSP生成定时器超时。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

Start level-1 LSP *id*.*pseudo*-*num* gen timer, time vlaue is *value*(ms).

启动level-1的LSP生成定时器，其值为*value*毫秒。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

Stop level-1 LSP *id*.*pseudo*-*num* gen timer.

停止level-1的LSP生成定时器。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

表1-7 debugging trill vr命令输出信息描述表

字段

描述

Interface state is down, ignore *event* event.

接口状态为down，忽略*event*事件。*event*包括：

·track positive：探测到链路有效

·track negative：探测到链路无效

·track notready：探测到链路尚未就绪

*[Event* track event on VLAN interface: *ifindex*.]

在VLAN接口收到*event*探测事件，接口索引为*ifindex*。*event*包括：

·Deregister：撤消注册

·Register：注册

Batch deregister track event on VLAN interface: *ifindex.*

在VLAN接口收到批量撤销注册探测事件，接口索引为*ifindex*

Flush TMNG the *role* role.

向TMNG下刷*role*角色。role包括：

·normal：普通RB

·gateway：网关设备

·access：二层接入设备

Current system\'s role is not gateway.

当前系统角色不是网关

All gateway TLVs have been deleted.

所有网关TLV已被删除

Clean TRILL virtual IP information.

清除TRILL虚拟IP地址信息

Receive *event* event.

收到*event*事件。*event*包括：

·track positive：探测到链路有效

·track negative：探测到链路无效

·track notready：探测到链路尚未就绪

Real-time backup TRILL VLAN interface *ifname* delete.

删除实时备份的TRILL VLAN接口*Ifname*

Delete *ifname* data from DBM.

从DBM中删除VLAN接口*Ifname*的数据

Receive MAC changing event, disable VR on last VLAN interface: *ifindex*.

在最后一个VLAN接口上收到MAC变化事件，接口索引为*ifindex*

Receive MAC changing event on VLAN interface: *ifindex*.

在VLAN接口上收到MAC变化事件，接口索引为*ifindex*

Receive *event* event on VLAN interface: *ifindex*, VR type: *vrtype*.

在VLAN接口上收到*event*事件，接口索引为*ifindex*，VR类型为*vrtype*。*event*包括：

·UP \--\> DOWN：接口由up变为down

·DOWN \--\> UP：接口由down变为up

·delete：删除接口

The role change: *event*

角色变化事件为*event*。*event*包括：

·normal \--\> gateway：由普通RB变为网关设备

·normal \--\> access：由普通RB变为二层接入设备

·gateway \--\> access：由网关设备变为二层接入设备

·gateway \--\> normal：由网关设备变为普通RB

·access \--\> normal：由二层接入设备变为普通RB

·access \--\> gateway：由二层接入设备变为网关设备

Flush TMNG, VLAN *vlanid* enable/disable VR.

下刷在VLAN *vlanid*上使能/去使能VR

Add/Delete/Batch delete virtual IP to address daemon.

向IP地址模添加/删除/批量删除虚拟IP地址

Flush TMNG, add/delete/batch delete virtual IP address.

向内核下刷TMNG消息，添加/删除/批量删除虚拟IP地址

Start/End to flush virtual IP address to *type* address deamon.

开始/结束下刷虚拟IP地址到IPv4/IPv6地址模块

Start/End to flush *event-type*.

开始/结束下刷*event*。*event*包括：

·VLAN enable VR：VLAN使能VR

·virtyal IP address：虚拟IP地址

Notify UPDT to add/delete *info* information.

通知UPD添加/删除*info*信息。*info*包括：

·virtual IP：虚拟IP信息

·gateway：网关信息

No valid gateway is elected as main gateway on VR *vrid* (*vrtype*).

在VR上没有有效的网关被选举为主网关，VR ID为*vrid*（VR类型为*vrtype*）

The first time elected main gateway on VR *vrid* (*vrtype*), main gateway: *systemid*.

在VR上第一次选举主网关，VR ID为*vrid*（VR类型为*vrtype*），主网关的system ID为*systemid*

Main gateway changed on VR *vrid* (*vrtype*), old gateway: *systemid1*, new gateway: *systemid2*.

在VR上主网关改变，VR ID为*vrid*（VR类型为*vrtype*），旧的主网关system ID为*systemid1，*新的主网关system ID为*systemid2*

表1-8 debugging trill adj-packet命令输出信息描述表

字段

描述

Receive a *type* contains invalid *string*. IIH discarded

收到*type*报文解析报文头时，*string*的合法性检查失败，丢弃该报文。s*tring*为报文头中的字段，*type*包括：

·LAN IIH：表示Hello报文

·BPDU：表示BPDU报文

·STP：表示生成树报文

·RSTP：表示快速生成树报文

·MSTP：表示多实例生成树报文

Receive a LAN IIH *string* error. IIH discarded

收到Hello报文解析TLV时发生错误，*string*为错误原因

IIH area address with the local system mismatch.

Hello报文区域地址同本地系统不匹配

IIH *string* with circuit(*port*) mismatch

收到的Hello报文的特征与接口*port*的特征不匹配，*string*为Hello报文与接口不匹配的特征

IIH has the same SNPA with a NBR, but different System ID. The NBR will be down

收到的Hello报文与已有邻居有相同的MAC地址，但是系统ID不同，将这个邻居置DOWN状态

IIH has the same System ID with a NBR, but different SNPA. The IIH will be discarded

收到的Hello报文与已有邻居有相同的系统ID，但是MAC地址不同，丢弃该Hello报文

Level-1 NBR(*mac*) two way *string*

Level-1的邻居2-Way检查的结果，*mac*为邻居的MAC地址，*string*为检查结果。s*tring*包括：

·pass：表示通过

·fail：表示不通过

·pend：表示邻居信息未收集完整，需继续等待

No VLAN-FLAGS sub-TLV in the MP-CAP TLV

在收到的Hello报文中，Multi-Topology Aware Port Capability TLV里没有包含VLAN-Flags子TLV，与协议不符

System is under disable state, ADJ packet discarded

系统处于关闭状态，丢弃ADJ模块收到的报文

Circuit state is not up, ADJ packet discarded

接口处于非up状态，丢弃ADJ模块收到的报文

Receive a packet from self, ADJ packet discarded

收到的是自己的报文，丢弃ADJ模块收到的报文

Receive a invalid packet, ADJ packet discarded

报文合法性检查不通过，丢弃ADJ模块收到的报文

Receive a *type* packet from(a*ddress*) on circuit(*port*)

在接口*port*上从地址*address*收到了*type*类型报文。*type*包括：

·Lan L1 Hello：表示Hello报文

·MTU-prob：表示MTU-prob报文

Receive unsupport packet *type*, ADJ packet discarded

收到不支持的报文，丢弃ADJ模块收到的报文，*type*为报文的PDU类型值

Receive a packet with invalid length, BPDU packet discarded

丢弃收到的BPDU报文，因为其长度不合法

Receive a BPDU packet on circuit(*port*)

在接口*port*上收到了BPDU报文

No enough PDU space for *string*

PDU长度已达到最大值，无法继续编码，*string*为PDU达到最大值的时机

No enable VLAN to fill the enable VLAN TLV

没有任何使能VLAN，所以无法对Enabled-VLANs子TLV进行编码

Get adj pointer failed for string

VLAN FLAGS子TLV获取ADJ指针失败，string为获取失败的时机

No need to encode AVF sub-TLV.

不需要编码AVF子TLV

No need to set forward VLAN if not DRB

不是DRB，无需携带Appointed Forwarders子TLV

DRB/RB send a HELLO on circuit(*port*) in VLAN *vlan-id*

DRB/RB在接口*port*的VLAN *vlan-id*内发送了Hello报文

RB send a HELLO on circuit(*port*) in designated VLAN *vlan-id*

RB在接口*port*的指定VLAN *vlan-id*内发送了Hello报文

Success to send a TCN/MTU-ack packet on circuit(*port*) in VLAN *vlan-id*

成功在接口*port*的VLAN *vlan-id*内发送了TCN/MTU-ack报文

Receive invalid/NULL MCS message *type*

收到非法/空的二层组播信息，*type*为二层组播报文的类型值

Unsupported MTU size(*size*) in MTU-prob, received length: *length*

收到的MTU-prob报文携带的MTU大小*size*与设备收到的长度*length*无法匹配

Invalid ACK source ID(*id*) in MTU-prob

收到的MTU-prob报文中的ACK source ID（*id*）非法

Circuit(*port*) is not AVF, BPDU discarded

接口*port*不作为AVF，丢弃收到的BPDU报文

Received TCA BPDU on circuit(*port*)

在接口*port*上收到TCA应答报文

Received NULL MCS information

收到的二层组播信息为空

Received MCS information:

type= *type*, INET family= *number*, VLAN= *vlan-id*, MAC= *mac*

收到二层组播信息的具体内容，二层组播报文的类型为*type*，*number*表示IPv4或IPv6，涉及的VLAN为*vlan-id，*如果是组播信息的话，其MAC地址为*mac*

表1-9 debugging trill snp-packet命令输出信息描述表

字段

描述

Not find current lsp entry to build csnp.

没有找到当前的LSP来创建CSNP

Circuit(*port*) silence, CSNP/PSNP not send.

接口*port*被配置为silence，不发送CSNP/PSNP

Level-1 csnp timer expired on a not DRB circuit(*port*).

非DRB的接口*port*上level-1的CSNP定时器超时

Send L1 CSNP/PSNP on circuit *port*.

接口*port*发送L1 CSNP/PSNP

Level-1 psnp timer expired on a DRB circuit(*port*).

DRB接口*port*上level-1的PSNP定时器超时

Wrong lsp entry tlv length(*TlvLen*) in snp.

SNP中携带错误的LSP摘要TLV长度

Snp contain too much lsp entry.

SNP中包含LSP摘要的个数超过限制

Invalid lsp id reported in snp.

SNP中包含无效的LSP ID

Wrong tlv length in snp.

SNP中携带错误的TLV长度

Invalid tlv in snp.

SNP中携带无效的TLV

Lsp entry *id*.*pseudo*-n*um* processed, newer/older/same than lsdb copy.

处理LSP摘要*id*.*pseudo*-n*um*比LSDB中保存的新/旧/相同。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

Lsp entry *id*.*pseudo*-n*um* processed, not exist in lsdb.

处理LSP摘要*id*.*pseudo*-n*um*，在LSDB中不存在。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

CSNP/PSNP not processed before DRB election.

在DRB选举前不处理CSNP/PSNP报文

Psnp not processed, current RB is not DRB.

当前RB不是DRB，不处理PSNP报文

Csnp not processed on DRB.

DRB上不处理CSNP报文

Lsp entry *LSPId*.*PseudoId* -*LspNum* is not loaded in csnp.

在CSNP中没有LSP *id*.*pseudo*-n*um*的摘要。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

Invalid type of SNP PDU.

无效的SNP PDU类型

SNP PDU process failed.

处理SNP PDU失败

表1-10 debugging trill update-packet命令输出信息描述表

字段

描述

Flooding L1 LSP/CSNP/PSNP *id*.*pseudo*-n*um* on circuit *port*.

在接口port上扩散L1 LSP/CSNP/PSNP *id*.*pseudo*-n*um*。LSP ID为*id*，伪节点ID为*pseudo*，分片号为*num*

Parsed neighbor *neighbour*.

解析出邻居*neighbour*

Parse group mac address, group record number is *number*.

解析组MAC地址，组记录个数为*number*

Parsed *number1* group record(s), tlv takes *number2*.

解析出*number1*个组记录，TLV携带了*number2*个

Parsed trill version is *value*.

解析TRILL版本，版本值为value

Parsed nickname *remote*.

解析出Nickname *remote*

Parsed trees info.

解析出分发树计算信息

Parsed trees list, startnum is *start*.

解析出分发树列表，起始数为*start*

Parsed interest vlans, start vlan *start*, end vlan *end*.

解析出关注VLAN信息，范围为*start*到*end*

Add/Delete/Modify Level-1 spf node(*Source*).

添加/删除/更新ID为*Source*的Level-1 SPF节点

(MT*id*) string level-1 group address(vlan *id*: MAC *mac*).

Add/Delete/Modify主地址，VLAN为*id*，MAC地址为*mac*

Lsp\'s seq number is 0.

LSP的序号为0

Illegal is-type in level-1 lsp.

Level-1的LSP内的无效的is类型

Check sum is zero.

校验和为0

Check sum error.

校验和错误

Invalid extended is reachability tlv.

无效可达TLV

Unsupported trill version(*id*)

不支持的TRILL版本（版本号）

Invalid nickname/ trees/ tree identifiers/ interested vlans subtlv.

无效的Nickname/trees/tree identifiers/interested vlans子TLV

Support protocol mismatch.

支持协议不匹配

Lsp with more than *number* area addr(es).

LSP携带多于*number*个区域地址

Lsp with wrong area addr length *length*.

LSP携带长度为*length*的错误区域地址

Lsp with wrong area addr *number*.

LSP携带错误区域地址*number*

Bad tlv len in the received lsp.

收到的LSP中的错误TLV长度

Wrong encoding of area address tlv in lsp.

LSP中的错误区域地址编码

Pdu size(*size*) is greater than receive buffer size(*size*),ignoring pdu.

PDU长度比收到的缓冲区长度大，忽略PDU

Pdu size(*size*) is less than common/fixed pdu header size(*size*),ignoring pdu.

PDU长度比一般/固定PDU头长度小，忽略PDU

Pdu length mismatch: recvLen = *length1*, encodeLen = *length2*,ignoring pdu

PDU长度不匹配：收到长度为*length1*，编码长度为*length2*，忽略PDU

LSP or SNP PDU common header error, ignoring pdu.

LSP或SNP PDU通用头错误，忽略PDU

Received PDU level mismatch.

收到PDU级别不匹配

No active neighbour with such snpa(*addr*) on the cicuit(*name*), ignoring pdu.

在链路上没有带有这种SNPA的激活邻居，忽略PDU

LSP PDU process failed.

LSP PDU处理失败

Received pdu is not lsp or snp, ignoring pdu.

收到的PDU不是LSP或SNP，忽略PDU

Check received packet failed.

检查收到报文失败

Starting to calculate distribution tree.

开始计算分发树

(MT*id*) *string* level-1 used tree root nickname *name* to dec.

Add/Modify/Delete level-1 树根到dec

Modify nickname node(*name*): tree used identifiers.

修改Nickname节点：树使用标示

Modify nickname node(*name*): trees info.

修改Nickname节点：树信息

Process local nickname change.

处理本地Nickname的改变

Add/Delete nickname node(nickname: *name*, system id: *string*).

增加/删除Nickname节点

Modify nickname node(*name*): priority.

修改Nickname节点：优先级

Received nickname has lower /higher priority.

收到的Nickname有低/高优先级

local nickname has lower /higher priority.

本地Nickname有低/高优先级

Receive invalid nickname *name*.

收到无效Nickname

Update distribution tree info, failed to get nickname node.

更新分发树信息：获取Nickname节点失败

表1-11 debugging trill route命令输出信息描述表

字段

描述

(M*id*) Set trigger event at *time*

（M*id*）在*time*时间设置触发事件，*id*表示拓扑ID

(M*id*) Old scheduled event is *value*, new trigger event is *event*.

（M*id*）旧的调度标记是*value，*新的触发事件是*event*，*id*表示拓扑ID

(M*id*) The event *event* is scheduled.

（M*id*）调度事件*event*已设置，*id*表示拓扑ID

*[(*M*id) Not allowed to calculate topology for inactive state.*]

（M*id*）Inactive状态下不允许进行拓扑计算，*id*表示拓扑ID

(M*id*) Current running event is revent, trigger event is tevent.

（M*id*）当前运行事件是*revent，*触发事件是*tevent*，*id*表示拓扑ID

(M*id*) Stop current calculation work.

（M*id*）停止当前的计算工作，*id*表示拓扑ID

(M*id*) Need to restart SPF calculation work, current running event is revent, new trigger event: tevent

（M*id*）需要重启SPF计算工作，当前运行事件是*revent，*触发事件是*tevent*，*id*表示拓扑ID

(M*id*) All phases of SPF work completed at time.\"

（M*id*）所有SPF阶段于*time*时间完成，*id*表示拓扑ID

(M*id*) Begin SPF calculation work from root node.

（M*id*）从根节点开始SPF计算，*id*表示拓扑ID

(M*id*)Merge nexthop from root node, count: *num1*/*num2*.

（M*id*）从根节点合并下一跳，数量：*num1/num2*，*id*表示拓扑ID

(M*id*)) Merge nexthop from parent node, count: *num*.

（M*id*）从父节点合并下一跳，数量：*num*，*id*表示拓扑ID

Parent node not found.

没有找到父节点

Spf node not found.

没有找到SPF节点

Back link not found.

没有找到回指链路

New distance is *value*.

新的距离是*value*

New distance exceeds max.

新的距离超过最大值

Greater cost.

更大的Cost

Less cost, add node to tent heap.

较小的Cost，将node加入到tent中

Equal cost, do nothing.

相等的Cost，不处理

Node update to tent list.

节点更新到tent中

Node is added into SPT path.

节点已经加入到SPT路径中

Node has no nexthop. Ignore its nbrs.

节点没有下一跳信息，忽略其邻居

Node is Overload, ignore its nbrs.

节点已经overload，忽略其邻居

Link is to be deleted.

链路被删除

Link is backward link, ignore it.

链路是回指链路，忽略

2-way check failed while no backward link found.

当没有发现回指链路，2-way检查失败

Link\'s valid check failed.

链路的有效性检查失败

Dest node not found.

没有发现目标节点

(M*id*:L*level*) Running full SPF calculation work.

（M*id*:L*level*）开始进行全部SPF计算，*id*表示拓扑ID，*level*表示级别

Link exceeds max limits

链路超出最大限制

Link is to be deleted.

链路将要被删除

Link with max metric.

带有最大metric值的链路

Link is same with backlink.

链路和回退链路相同

MReceiver info (M*id*:L*level*) add(new) multi-reciever *source* *vlan* *mac*

(M*id*:L*level*)添加组播接收者，源ID为*source*，VLAN为*vlan*，组播地址为*mac*

SPF link (M*id*:L*level*) Create(New) link *source* *\--\>* *dest* AttAdjs: *number* Tree Back Usage Nhop

(M*id*:L*level*)创建SPFLink，源节点为*source*，目的节点为*dest*，ATT邻居数为*number*

The D-Node pointer is NULL.

D-node指针为空

Node is updated in tent heap.

Tent中的node已经更新

D-tree calculation started/ended at *time*.

D-tree计算开始/于结束于*time*

Failed to flush prefix/VN head, NBR Id is *id*, error is *errno*.

下刷prefix head/VN head失败，邻居id为*id*错误码是*errno*

Failed to occupy/alloc NBR id *id*.

占用/分配NBR ID *id*失败

The NBR *id* is added, type is  normal/ecmp/unknown.

NBR *id*已添加，类型为normal/ecmp/unknown

Deleting/Add NBR *id*, refer is *refcnt*, type is normal/ecmp/unknown.

删除/添加NBR *id*，引用计数为*refcnt*，类型为normal/ecmp/unknown

NBR node to be deleted.

NBR node将被删除

NBR node is root node, don\'t process.

NBR节点是跟节点，不能处理

NBR node is already on SPT.

NBR节点已在SPT上

(M*id*) Begin SPF from root node.

（M*id*）从根节点开始SPF，*id*表示拓扑ID

Flush prefix message, nickname is *name*, NBR ID is *id*, action is *value*.

下刷前缀信息：Nickname为*name*，NBRID为*id*，action为*value*

Flush VN message, NBR ID is *id*, action is *value*.

下刷VN信息，NBR ID为*id*，action为*value*

Flush TFIB smooth start/end message.

下刷平滑开始/结束信息

Flush adj message, nickname is *name*, action is *value*, ifindex is *index*, MAC is *mac*.

下刷adj信息，Nickname为*name*，action为*action*，ifindex为*index*，MAC是*mac*

INGRESS run canceled, no used tree finded.

INGRESS运行取消，没有找到有用的树

Create(new) Ingress entry, vlan: *id*.

创建Ingress条目，VLAN为*id*

Add/Delete/ Update Remote entry, vlan: *id*, root:*root.*

添加/删除/更新远端条目，VLAN为*id*，根为*root*

Add port entry to Ingress entry(new), vlan: *id*,, ifIndex: *index*.

向Ingress列表添加端口列表，VLAN为*id*，ifIndex为*index*

Ingress entry not found, vlan: *id*.

没有找到Ingress列表，VLAN为*id*

Port entry not found in ingress entry, vlan: *id*, ifIndex: *index*.

在ingress列表中，没有发现端口列表

Set local flag of TVMac entry, root: *root,* vlan: *id*, mac: *mac*.

设置本地TVMAC列表的标记，根为*root*，VLAN为*id*，MAC地址为*mac*

Add port entry to TVMac entry, root: *root*, vlan: *id*, mac: *mac*., ifIndex: *index*..

向TVMAC列表添加端口列表，根为*root*，VLAN为*id*，MAC地址为*mac*，ifIndex:*index*

Update TVMac entry, root: *root*,, vlan: *id*, mac: *mac*.

更新TVMAC列表，根为*root*，VLAN为*id*，MAC地址为*mac*

Process local multicast info.

处理本地组播信息

Find local IPv4 multicast router.

发现本地IPv4组播路由

Find local IPv6 multicast router.

发现本地IPv6组播路由

Add port entry to TVlan entry, root: *root*, vlan: *id*, ifIndex: *index*.

向TVlan列表添加端口列表，根为*root*，VLAN为*id*，ifIndex为*index*

Create RPF entry, root: *root*,, ingress:*ingress*, ifIndex: *index*.

创建RPF列表，根为*root*，ingress为*ingress*，ifIndex为*index*

Match the filter source id and stop.

匹配过滤的source id，并且停止

Process remote multicast info along the d-tree link, ifIndex: *index*..

沿着d-tree链路处理远端组播信息，ifIndex为*index*

Update port list of IPv4/ IPv6 multi-router in TVlan entry, root: *root*,, vlan: *id*,.

更新TVlan列表中的IPv4路由的端口列表，根为*root*，VLAN为*id*

Add/Update/Delete RPF entry, root: *root*, ingress: *ingress.*

添加/更新/删除RPF列表，根为*root*，ingress为*ingress*

Add NBR *id*, new refer count is *count*, type is *type*, result is *result*.

添加邻居，新的引用计数为*count*，类型为*type*，结果为*result*

NBR *id* has been deleted, type is normal/ecmp/unknown.

NBR *id*已被删除，类型为normal/ecmp/unknown

Failed to add id node for NBR *id*.

为NBR *id*添加id node失败

(M*id*:P*prefix*) Failed to generate normal NBR.

（M*id*:P*prefix*）产生普通NBR失败，*id*表示拓扑ID，*prefix*表示前缀

(M*id*:L*level*:P*prefix*) Failed to generate NBR.

（M*id*:L*level*:P*prefix*）产生NBR失败，*id*表示拓扑ID，*level*表示级别，*prefix*表示前缀

(M*id*:L*level*:P*prefix*) Failed to get nexthop from ISPF module.

（M*id*:L*level*:P*prefix*）从ISPF模块获取下一跳失败，*id*表示拓扑ID，*level*表示级别，*prefix*表示前缀

(M*id*::P*prefix*) The nexthop number is zero.

（M*id*:P*prefix*）下一跳的数量为零，*id*表示拓扑ID，*prefix*表示前缀

(M*id*::P*prefix*) Failed to generate normal nbr.

（M*id*:P*prefix*)）产生普通邻居失败，*id*表示拓扑ID，*prefix*表示前缀

(M*id*:L*level*) Failed to get nexthop for *string* from ISPF module, prefix is *prefix*.

（M*id*:L*level*）ISPF模块由于某种原因获取下一跳失败，*id*表示拓扑ID，*prefix*表示前缀

(M*id*:L*level*) Processing unicast route entry *prefix*.

（M*id*:L*level*）处理*prefix*的单播路由，*id*表示拓扑ID，*level*表示级别

(M*id*:L*level*) URC run started/ended at *time*.

（M*id*:L*level*）URC开始/结束于*time*，*id*表示拓扑ID，*level*表示级别

(M*id*:L*level*) URC flush ended at *time*.

（M*id*:L*level*）URC下刷结束于*time*，*id*表示拓扑ID，*level*表示级别

(P*prefix*:N*id*) Destroy route entry successfully, source id is *source*.

（P*prefix*:N*id*）成功删除一条路由表项，源ID为*source*，*id*表示拓扑ID，*prefix*表示前缀

Failed to add self route entry, nickname is invalid.

添加本机路由表项失败，Nickname为无效值

Failed to add route entry, nickname is invalid.

添加路由表项失败，Nickname为无效值

(P*prefix*) Failed to add route entry, the SPF node doesn\'t exist.

（P*prefix*）添加路由表项失败，SPF节点不存在，*prefix*表示前缀

(P*prefix*)Failed to alloc route entry.

（P*prefix*）分配路由表项失败，*prefix*表示前缀

(P*prefix*:N*id*) Add or update route entry successfully, source id is *source*.

（P*prefix*:N*id*）成功添加或更新路由表项，源ID为*source*，*id*表示拓扑ID，*prefix*表示前缀

Failed to create route attribute.

添加路由属性信息失败

Add or update route entry, nickname is *name*, NBR ID is *id*, source id is *id*

添加或更新路由表，Nickname为*name*，NBR ID为*id*，源ID为*id*

【举例】

\# 打开TRILL协议错误调试信息开关。

\<Sysname\> debugging trill error

\*Mar 18 14:28:41:744 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-ERR: Send level-1 csnp pdu failed.

*// 发送Level-1的CSNP报文失败*

\# 打开TRILL协议事件调试信息开关。

\<Sysname\> debugging trill event

\*Jun  8 08:29:44:658 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-Event: Notifing the TRILL interface state changed.

*// 通知TRILL接口状态改变*

\# 打开TRILL协议平滑重启调试信息开关。

\<Sysname\> debugging trill graceful-restart

\*Jun  3 09:56:15:006 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-GR: T3 timer is stoped.

*[// T3*]*定时器已停止*

\# 打开TRILL协议HA调试信息开关。

\<Sysname\> debugging trill ha

\*Jun  3 09:56:15:006 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-HA: RtBackup TRILL Nickname.

*// 实时备份TRILL的Nickname*

\# 打开TRILL协议本地更新调试信息开关。

\<Sysname\> debugging trill self-originate-update

\*May 27 15:46:13:289 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-ORG: Generating level-1 LSP [0011.2233.4401.00-00, Seq 0x00000001, length 71.]

*// 生成序列号为0x00000001、长度为71的L1 LSP[0011.2233.4401.00-00]*

\# 打开TRILL协议定时器调试信息开关。

\<Sysname\> debugging trill timer

\*Mar 18 14:28:41:744 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-Timer: Level-1 hello timer expired on the circuit GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1下的Level-1 Hello报文发送定时器超时*

\# 打开TRILL协议VR调试信息开关。

\<Sysname\> debugging trill vr

\*Jul  2 17:16:36:406 2013 Sysname TRILL/7/TRILLDBG: -MDC=1; TRILL-VR: The role change: normal \--\> access.

*// 设备角色由普通RB变为二层接入设备*

\# 打开TRILL协议邻居报文调试信息开关。

\<Sysname\> debugging trill adj-packet

\*Jun  3 09:56:12:666 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-ADJ: Level-1 NBR(0011.2233.4401) two way pass.

*[// Level-1*]*的邻居（0011.2233.4401）双向连接检查通过*

\# 打开接收的TRILL协议SNP报文调试信息开关。

\<Sysname\> debugging trill snp-packet receive

\*Mar 18 14:28:41:744 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-SNP: Send L1 CSNP on circuit GigabitEthernet1/0/1.

*// 在接口GigabitEthernet1/0/1上发送Level-1的CSNP报文*

\# 打开接收的TRILL协议更新报文调试信息开关。

\<Sysname\> debugging trill update-packet receive

\*Jun  8 08:31:21:994 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-UPDT: Parsed nickname 63.

*// 解析出Nickname为63*

\# 打开TRILL协议路由计算调试信息开关。

\<Sysname\> debugging trill route

\*Jun  3 09:56:15:911 2011 Sysname TRILL/7/TRILLDBG: -MDC=1;

TRILL-ROUTE: (M0) The event 0X00001F is scheduled.

*// 调度事件0x00001F已设置*
