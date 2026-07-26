
**ATM \-- ATM调试命令 \-- debugging atm all**

------------------------------------------------------------------------

【命令】

**[debugging atm all** [ **interface** *interface-type* *interface-number* ]]

**[undo debugging atm all** [ **interface** *interface-type* *interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：表示指定接口的调试信息开关。支持ATM接口、ATM子接口。

【描述】

**[debugging atm all**]命令用来打开ATM的所有调试信息开关。**undo debugging atm all**命令用来关闭ATM的所有调试信息开关。

缺省情况下，所有的ATM调试信息开关均处于关闭状态。

如果不指定接口，则打开所有ATM接口的所有调试信息开关。

【举例】

\# 打开ATM的所有调试信息开关。

\<Sysname\> debugging atm all

**ATM \-- ATM调试命令 \-- debugging atm error**

------------------------------------------------------------------------

【命令】

**[debugging atm error**[ [ **interface** *interface-type* *interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

**[undo debugging atm error**[ [ **interface** *interface-type* *interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：表示指定接口的调试信息开关。支持ATM接口、ATM子接口。

*[pvc-name*]：PVC名，长度为1～15个字符的字符串，区分大小写，PVC名中不允许使用"/"和"-"，如"1/20"、"a-b"就不允许作为PVC名。

*[vpi/vci*]：*vpi*为VPI值，取值范围为0～255；*vci*为VCI值，取值范围与接口类型相关，请参见"[表]1-1(?-1864992396#_Ref337389143){.underline}[不同[接口[对应的]]]VCI[的取值范围](?-1864992396#_Ref57541113)"。*vpi*与*vci*不能同时为0。通常，*vci*取值0到31保留用于特定用途，建议用户不要使用。

表1-1 不同接口对应的VCI的取值范围

接口类型

VCI取值范围

ATM ADSL

\<0-255\>

ATM ADSL2+

\<0-255\>

ATM G.SHDSL

\<0-255\>

ATM SHDSL_4WIRE

\<0-255\>

ATM SHDSL_4WIRE_BIS

\<0-255\>

ATM SHDSL_8WIRE_BIS

\<0-255\>

ATM E1

\<0-511\>

ATM T1

\<0-511\>

ATM E3

\<0-1023\>

ATM T3

\<0-1023\>

ATM OC-3c/STM-1

\<0-1023\>

ATM OC-12c/STM-4

\<0-1023\>

ATM 25M

\<0-1023\>

ATM子接口

与ATM子接口所属ATM接口的取值范围相同

PVC-group

与PVC-group所属ATM接口的取值范围相同

【描述】

**[debugging atm error**]命令用来打开ATM的错误调试信息开关。**undo debugging atm error**命令用来关闭ATM的错误调试信息开关。

缺省情况下，ATM错误调试信息开关处于关闭状态。

如果不指定接口，则打开所有ATM接口的错误调试信息开关。如果不指定PVC名或者VPI/VCI值对，则打开指定接口的所有PVC的错误调试信息开关。

表1-2 debugging atm error命令输出信息描述表

字段

描述

Interface *interface-name* PVC *vpi/vci* : Failed to process InARP timeout event, as there is no InARP mapping.

接口*interface-name* PVC *vpi/vci*：InARP超时处理失败，没有InARP映射

Interface *interface-name* PVC-group *id* : Failed to process InARP timeout event, as there is no InARP mapping.

接口*interface-name* PVC-group *id*：InARP超时处理失败，没有InARP映射

Interface *interface-name* PVC *vpi/vci* : Sending InARP *type* packet failed, as the interface has no IP address.

接口*interface-name* PVC *vpi/vci*：发送InARP *type*报文失败，接口未配IP地址，其中*type*的类型如下：

·request：请求报文

·reply：应答报文

Interface *interface-name* PVC-group *id*: Sending InARP *type* packet failed, as the interface has no IP address.

接口*interface-name* PVC-group *id*：发送InARP *type*报文失败，接口未配IP地址，其中*type*的类型如下：

·request：请求报文

·reply：应答报文

Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed due to packet protocol is error.

接口*interface-name* PVC *vpi/vci*：InARP报文解析失败，报文协议字段错误

Interface *interface-name* PVC PVC-group *id* : InARP packet parse failed due to packet protocol error.

接口*interface-name* PVC-group *id*：InARP报文解析失败，报文协议字段错误

Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed, as the packet type is not reply or request.

接口*interface-name* PVC *vpi/vci*：InARP报文解析失败，报文类型不是请求或应答报文

Interface *interface-name* PVC-group *id* : InARP packet parse failed, as the packet type is not reply or request.

接口*interface-name* PVC-group *id*：InARP报文解析失败，报文类型不是请求或应答报文

Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed due to packet length field error.

接口*interface-name* PVC *vpi/vci*：InARP报文解析失败，报文长度字段错误

Interface *interface-name* PVC-group *id* : InARP packet parse failed due to packet length field error.

接口*interface-name* PVC-group *id*：InARP报文解析失败，报文长度字段错误

Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed, as packet length is too long.

接口*interface-name* PVC *vpi/vci*：InARP报文解析失败，报文长度太长

Interface *interface-name* PVC-group *id* : InARP packet parse failed, as packet length is too long.

接口*interface-name* PVC-group *id*：InARP报文解析失败，报文长度太长

Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed, as packet destination IP address is 0.0.0.0.

接口*interface-name* PVC *vpi/vci*：InARP报文解析失败，报文目的IP为0.0.0.0

Interface *interface-name* PVC-group *id* : InARP packet parse failed, as packet destination IP is 0.0.0.0.

接口*interface-name* PVC-group *id*：InARP报文解析失败，报文目的IP为0.0.0.0

Interface *interface-name* PVC *vpi/vci* : Failed to process an InARP reply packet, as there is no InARP mapping.

接口*interface-name* PVC *vpi/vci*：处理InARP应答报文失败，没有InARP映射

Interface *interface-name* PVC-group *id* : Failed to process an InARP reply packet, as there is no InARP mapping.

接口*interface-name* PVC-group *id*：处理InARP应答报文失败，没有InARP映射

Interface *interface-name* PVC *vpi/vci* : Failed to process an InARP reply packet, as InARP mapping state is not ATM_INARP_STATE_SNDREQUEST.

接口*interface-name* PVC *vpi/vci*：处理InARP应答报文失败，InARP映射的状态不为"发送请求等待应答"状态

Interface *interface-name* PVC-group *id*: Failed to process an InARP reply packet, as InARP mapping state is not ATM_INARP_STATE_SNDREQUEST.

接口*interface-name* PVC-group *id*：处理InARP应答报文失败，InARP映射的状态不为"发送请求等待应答"状态

Interface *interface-name* PVC *vpi/vci* : Failed to process an InARP reply packet, as packet destination IP is *ipaddress*, different from interface IP.

接口*interface-name* PVC *vpi/vci*：处理InARP应答报文失败，报文目的IP为*ipaddress*，与本端接口IP不一致

Interface *interface-name* PVC-group *id* : Failed to process an InARP reply packet, as packet destination IP is *ipaddress*, different from interface IP.

接口*interface-name* PVC-group *id*：处理InARP应答报文失败，报文目的IP为*ipaddress*，与本端接口IP不一致

OAM ping reply error due to invalid ping index.

OAM回应报文错误，索引无效

Interface *interface-name* PVC *vpi/vci* does not exist.

接口interface-name{.TableTextChar} PVC vpi/vci{.TableTextChar}不存在

Dropped a packet on interface *interface-name* due to absence of the link control block.

报文发送失败，链路控制块不存在

Failed to send a packet, as the physical control block of interface *interface-name* does not exist.

报文发送失败，接口interface-name{.TableTextChar}物理控制块不存在

Failed to send a packet, as the outbound EoA mapping is the same as inbound EoA mapping.

报文发送失败，报文的出EoA映射和入EoA映射相同

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as PVC state is down.

接口*interface-name* PVC *vpi/vci*：报文接收失败，PVC状态为down

Interface *interface-name* PVC *vpi/vci*: Failed to send a packet, as PVC state is down.

接口*interface-name* PVC *vpi/vci*：报文发送失败，PVC状态为down

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet due to packet de-encapsulation error.

接口interface-name PVC vpi/vci：报文接收失败，去封装错误

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as the packet is not an IP packet though IP transparent transmission is enabled.

接口*interface-name* PVC *vpi/vci*：报文接收失败，接口使能了IP透传但报文不是IP报文

Interface *interface-name* PVC *vpi/vci*: Failed to send a packet due to packet encapsulation error.

接口*interface-name* PVC *vpi/vci*：报文发送失败，封装错误

Interface *interface-name* PVC-group *id*: Failed to send a packet, as PVC-group has no appropriate sub PVC available.

接口*interface-name* PVC-group *id*：报文发送失败，PVC-group下没有合适的子PVC

Interface *interface-name* PVC *vpi/vci*: Failed to send a packet, as VPI *vpi-value* failed to get token.

接口*interface-name* PVC *vpi/vci*：报文发送失败，VPI *vpi-value*获取令牌失败

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as VPI *vpi-value* failed to get token.

接口*interface-name* PVC *vpi/vci*：报文接收失败，VPI *vpi-value*获取令牌失败

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as PPPoA mapping does not exist..

接口*interface-name* PVC *vpi/vci*：报文接收失败，PPPoA映射不存在

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as EoA mapping does not exist.

接口*interface-name* PVC *vpi/vci*：报文接收失败，EoA映射不存在

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as physical control block of interface *virtual-interface-name* does not exist.

接口*interface-name* PVC *vpi/vci*：报文接收失败，接口*virtual-interface-name*的物理控制块不存在

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as the state of interface *virtual-interface-name* is down.

接口*interface-name* PVC *vpi/vci*：报文接收失败，接口*virtual-interface-name*的状态为down

Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as the packet is a multicast one.

接口*interface-name* PVC *vpi/vci*：报文接收失败，报文是组播报文

Interface *interface-name*: Failed to receive a packet, as PVC *vpi/vci* does not exist.

接口*interface-name*：报文接收失败，PVC *vpi/vci*不存在

Interface *interface-name*: Failed to send an IP packet, as IPoA mapping for IP: *ipaddress* was not found.

接口*interface-name*：IP报文发送失败，未找到IP地址*ipaddress*对应的IPoA映射

Interface *interface-name*: Failed to change OAM state, as PVC *vpi/vci* does not exist.

接口*interface-name*：OAM状态改变失败，PVC *vpi/vci*不存在

Interface *interface-name*: Failed to receive OAM ping, as PVC *vpi/vci* does not exist.

接口*interface-name*：接收OAM ping失败，PVC *vpi/vci*不存在

Interface *interface-name*: Failed to receive a packet, as the network layer state of interface is down.

接口*interface-name*：报文接收失败，接口网络层状态为down

Interface *interface-name*: Failed to send a packet by IPoA mapping, as the packet type is unknown.

接口*interface-name*：IPoA映射发送报文失败，未知的报文类型

【举例】

\# Router A与Router B通过ATM接口连接，其中一端配置IP地址，另一端不配置IP地址，具体配置如下：

·Router A

\<Sysname\> system-view

Sysname interface atm 2/4/2

Sysname-ATM2/4/2 pvc 10/33

Sysname-ATM2/4/2-pvc-10/33 map ip inarp

·Router B

\<Sysname\> system-view

Sysname interface atm 2/4/3

Sysname-ATM2/4/3 pvc 10/33

Sysname-ATM2/4/3-pvc-10/33 map ip inarp

Sysname-ATM2/4/3-pvc-10/33 quit

Sysname-ATM2/4/3 ip address 100.1.1.2 255.255.255.0

\# 在Router A打开所有ATM接口的错误调试信息开关。

\<Sysname\> debugging atm error

\*Dec 24 08:04:05:125 2012 Sysname ATM/7/ERROR: -MDC=1;

Interface ATM2/4/3 PVC 10/33: Sending InARP request packet failed, as the interface has no IP address.

*// 由于没有找到IP地址，InARP请求报文发送失败*

**ATM \-- ATM调试命令 \-- debugging atm event**

------------------------------------------------------------------------

【命令】

**[debugging atm event**[ [ **interface** *interface-type* *interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

**[undo debugging atm event**[ [ **interface** *interface-type* *interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：表示指定接口的调试信息开关。支持ATM接口、ATM子接口。

*[pvc-name*]：PVC名，长度为1～15个字符的字符串，区分大小写，PVC名中不允许使用"/"和"-"，如"1/20"、"a-b"就不允许作为PVC名。

*[vpi/vci*]：*vpi*为VPI值，取值范围为0～255；*vci*为VCI值，取值范围与接口类型相关，请参见"[表]1-1(?-1864992396#_Ref337389143){.underline}[不同[接口[对应的]]]VCI[的取值范围](?-1864992396#_Ref57541113)"。*vpi*与*vci*不能同时为0。通常，*vci*取值0到31保留用于特定用途，建议用户不要使用。

【描述】

**[debugging atm event**]命令用来打开ATM的事件调试信息开关。**undo debugging atm event**命令用来关闭ATM的事件调试信息开关。

缺省情况下，ATM事件调试信息开关处于关闭状态。

如果不指定接口，则打开所有ATM接口的事件调试信息开关。如果不指定PVC名或者VPI/VCI值对，则打开指定接口的所有PVC的事件调试信息开关。

本命令将打开所有发生在ATM接口或者某条PVC上的事件调试信息开关，可以用来跟踪系统的一些关键事件，在查找网络故障时，这些信息可能会有参考作用。

表1-3 debugging atm event命令输出信息描述表

字段

描述

Received and dropped an InARP packet on interface *interface-name* PVC *vpi/vci*, as no local IP is configured.

本端未配IP地址，丢弃收到的InARP报文，对应接口为*interface-name*，对应PVC为*vpi/vci*

InARP mapping on interface *interface-name* PVC *vpi/vci* timed out.

接口*interface-name*下PVC *vpi/vci*的InARP映射超时

The InARP mapping state on interface *interface-name* PVC *vpi/vci*  changed from *oldstate* to *newstate*.

接口*interface-name*下PVC *vpi/vci* 的InARP映射状态从*oldstate*迁移到*newstate*，其中*oldstate*和*newstate*类型如下：

·ATM_INARP_STATE_INIT：初始化状态

·ATM_INARP_STATE_SNDREQUEST：已发送InARP请求报文、等待InARP应答报文状态

·ATM_INARP_STATE_RCVREPLY：已收到InARP应答报文状态

Deleted the adjacent table of IP *ip-address* on interface *interface-name* PVC *vpi/vci* because InARP mapping changed.

删除接口*interface-name*下PVC *vpi/vci*上IP为*ip-address*的邻接表，因为InARP映射改变

Refreshed the adjacent table of IP *ip-address* on interface *interface-name* PVC *vpi/vci* because InARP mapping changed, the old IP is *oldip-address*

刷新接口*interface-name*下PVC *vpi/vci*上IP为*ip-address*的邻接表，因为InARP映射改变，原IP为*oldip-address*

The kernel notified interface *interface-name* PVC *vpi/vci* to change to *newstate*.

内核通知接口*interface-name*下PVC *vpi/vci*状态变为*newstate*，*newstate*类型如下：

·up：开启状态

·down：关闭状态

Received create-PVC *vpi/vci* event on interface *interface-name* from kernel.

内核通知创建PVC *vpi/vci*

Received delete-PVC *vpi/vci* event on interface *interface-name* from kernel.

内核通知删除PVC *vpi/vci*

Received OAM ping reply from kernel with ping index being *value*.

收到OAM ping应答，对应索引为*value*

Interface *interface-name* PVC *vpi/vci* received QoS bandwidth change event from kernel(OutputPcr: *pcrvalue*, OutputScr: *scrvalue*, ServiceType: *type*).

接口*interface-name*下PVC *vpi/vci*收到内核通知QoS带宽变化，输出ATM信元的峰值速率为*pcrvalue*，输出ATM信元的可承受速率为*scrvalue*，业务类型为*type*，其中*type*类型如下：

·UBR：非确定速率

·CBR：恒定速率

·VBR-RT：实时可变速率

·VBR-NRT：非实时可变速率

Received add-IP-address *ip-address* event on interface *interface-name*.

收到添加IP地址ip-address{.TableTextChar}事件

Received delete-IP-address *ip-address* event on interface *interface-name*.

收到删除IP地址*ip-address*事件

PVC *vpi/vci* state changed to *newstate* on interface *interface-name*.

接口*interface-name*下PVC *vpi/vci*状态变为*newstate*，*newstate*类型如下：

·up：开启状态

·down：关闭状态

PVC-group *id* state changed to *newstate* on interface *interface-name*.

接口*interface-name*下PVC-group *id*状态变为*newstate*，*newstate*类型如下：

·up：开启状态

·down：关闭状态

PVC *vpi/vci* state changed to *newstate* on interface *interface-name*.

接口*interface-name*下PVC *vpi/vci*状态变为*newstate*，*newstate*类型如下：

·not shutdown：开启状态

·shutdown：关闭状态

Network layer state changed to *newstate* on interface *interface-name*.

接口*interface-name*网络层状态变为*newstate*，*newstate*类型如下：

·up：开启状态

·down：关闭状态

OAM state changed to *newstate* on interface *interface-name* PVC *vpi/vci*.

接口*interface-name*下PVC *vpi/vci*的OAM状态变为*newstate*，*newstate*类型如下：

·up：开启状态

·down：关闭状态

Notified driver to create a mapping on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*, MapType: *type*, IP Address: *ip-address*)

通知驱动在接口*interface-name*上创建映射，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，映射类型为*type*，IP地址为*ip-address*，其中*type*类型如下：

·STATIC IPoA：静态IPoA映射

·INARP IPoA：InARP IPoA映射

·DEFAULT IPoA：默认IPoA映射

·L3 EoA：三层EoA映射

·PPPoA：PPPoA映射

Notified driver to delete a mapping on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*, MapType: *type*, IP Address: *ip-address*)

通知驱动在接口*interface-name*上删除映射，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，映射类型为*type*，IP地址为*ip-address*，其中*type*类型如下：

·STATIC IPoA：静态IPoA映射

·INARP IPoA：InARP IPoA映射

·DEFAULT IPoA：默认IPoA映射

·L3 EoA：三层EoA映射

·PPPoA：PPPoA映射

Notified driver to send OAM AIS/RDI cell on interface *interface-name*, with *value* returned.

通知驱动在接口*interface-name*上发送OAM AIS/RDI告警信元，返回*value*

Notified driver to create a PVC on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*)

下驱动创建接口*interface-name*下PVC，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*

Notified driver to delete a PVC on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*)

下驱动删除接口*interface-name*下PVC，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*

Notified driver to clear PVC statistics on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*)

下驱动清除接口*interface-name*下PVC统计信息，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*

Notified driver to change PVC state on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* *State: newstate*)

通知驱动改变接口*interface-name*下PVC状态，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，状态为*newstate*。*newstate*类型如下：

·up：开启状态

·down：关闭状态

Notified driver to change PVC physical state on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* *State: newstate*)

通知驱动改变接口*interface-name*下PVC物理状态，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，状态为*newstate*。*newstate*类型如下：

·up：开启状态

·down：关闭状态

Notified driver to set service on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* ServiceType*: type* Output-pcr*: pcrvalue,* Output-scr*: scrvalue,* Output-mbs*: mbsvalue,* Cdvt_value*:  cdvtvalue* )

通知驱动设置接口*interface-name*下业务类型，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，业务类型为*type*，输出ATM信元的峰值速率为*pcrvalue*，输出ATM信元的可承受速率为*scrvalue*，输出ATM信元的最大突发长度为*mbsvalue*，信元时延变化容限为*cdvtvalue*，其中*type*类型如下：

·UBR：非确定速率

·CBR：恒定速率

·VBR-RT：实时可变速率

·VBR-NRT：非实时可变速率

Notified driver to set transmit-priority on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* ServiceType: *type,* Transmit-Priority: * privalue*)

通知驱动设置接口*interface-name*下传输优先级，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，业务类型为*type*，传输优先级为*privalue*，其中*type*类型如下：

·UBR：非确定速率

·CBR：恒定速率

·VBR-RT：实时可变速率

·VBR-NRT：非实时可变速率

Notified driver to set OAM loopback on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* interval: *interval*, up-count: *up-count*, down-count: *down-count*, retry-interval: *retry-interval*)

通知驱动设置接口*interface-name*下OAM F5 Loopback信元的发送以及重传检测，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，发送OAM F5 Loopback信元的间隔时间为*interval*，PVC状态转变为UP之前必须连续正确收到OAM F5 Loopback信元的数量为*up-count*，PVC状态转变为DOWN之前连续未收到的OAM F5 Loopback信元的数量为*down-count*，PVC状态改变前OAM F5 Loopback在进行重传验证时的信元发送间隔时间为*retry-interval*

Notified driver to set OAM CC on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* CheckType: *type*)

通知驱动设置接口*interface-name*下OAM连续性检测，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，启动方式类型为*type*。*type*类型如下：

·sink：作为接收端时启动

·source：作为发送端时启动

·both：作为接收端和发送端时启动

Notified driver to set OAM AIS/RDI cell detection parameters on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* up-count: *up-count*, down-count: *down-count*)

通知驱动修改接口*interface-name*下AIS/RDI告警信元检测的相关参数，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，连续没有收到AIS/RDI告警信元秒数为*up-count*，连续收到AIS/RDI告警信元个数为*down-count*

Notified driver to send OAM ping cell on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* PingIndex: *indexvalue*)

通知驱动在接口*interface-name*上发送OAM ping信元，返回*value*。下发数据如下：VPI为*vpi-value*，VCI为*vci-value*，驱动上下文为*drvcontext*，Ping索引为*indexvalue*

Get OAM statistics on interface *interface-name* PVC *vpi/vci* from driver, with *value* returned.

向驱动获取接口*interface-name*下PVC *vpi/vci*的OAM统计信息，返回*value*

Get PVC statistics on interface *interface-name* PVC *vpi/vci* from driver, with *value* returned.

向驱动获取接口*interface-name*下PVC *vpi/vci*的PVC统计信息，返回*value*

Refreshed the adjacent table of IP *ip-address* on interface *interface-name* PVC *vpi/vci*, with *value* returned.

刷新接口*interface-name*下PVC *vpi/vci*上IP为*ip-address*的邻接表，返回*value*

Deleted the adjacent table of IP *ip-address* on interface *interface-name* PVC *vpi/vci*, with *value* returned.

删除接口*interface-name*下PVC *vpi/vci*上IP为*ip-address*的邻接表，返回*value*

Notified *event-type* event  on interface *interface-name* to module *module-id*.  (VPI: *vpi-value*, VCI: *vci-value*)

通知模块*module-id*接口*interface-name*发生*event-type*事件，具体参数如下：VPI为*vpi-value*，VCI为*vci-value*。其中*event-type*类型如下：

·PVC_CREATE：创建PVC

·PVC_DELETE：删除PVC

Notified *event-type* event  on interface *interface-name* PVC *vpi/vci* to module *module-id* .

通知模块*module-id*接口*interface-name*下PVC *vpi/vci*发生*event-type*事件，其中*event-type*类型如下：

·PVC_UP：PVC状态UP

·PVC_DOWN：PVC状态DOWN

·PVC_SPEEDCHANGE：PVC带宽改变

【举例】

\# Router A和Router B通过ATM接口连接，具体配置如下：

·Router A

\<Sysname\> system-view

Sysname interface atm 2/4/2

Sysname-ATM2/4/2 pvc 10/33

·Router B

\<Sysname\> system-view

Sysname interface atm 2/4/3

Sysname-ATM2/4/3 pvc 10/33

\# 打开Router A所有ATM接口的事件调试信息开关。

\<Sysname\> debugging atm event

\# 将Router A的PVC 10/33进行**shutdown**操作。

Sysname-ATM0/2-pvc-10/33 shutdown

\*Dec 24 09:36:30:715 2012 Sysname ATM/7/EVENT:

PVC 10/33 state changed to shutdown on interface ATM2/4/2.

*[// ATM2/4/2*]*的PVC 10/33状态为shutdown*

**ATM \-- ATM调试命令 \-- debugging atm packet**

------------------------------------------------------------------------

【命令】

**[debugging atm packet**[ [ **interface** *interface-type* *interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

**[undo debugging atm packet**[ [ **interface** *interface-type* *interface-number* [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：表示指定接口的调试信息开关。支持ATM接口、ATM子接口。

*[pvc-name*]：PVC名，长度为1～15个字符的字符串，区分大小写，PVC名中不允许使用"/"和"-"，如"1/20"、"a-b"就不允许作为PVC名。

*[vpi/vci*]：*vpi*为VPI值，取值范围为0～255；*vci*为VCI值，取值范围与接口类型相关，请参见"[表]1-1(?-1864992396#_Ref337389143){.underline}[不同[接口[对应的]]]VCI[的取值范围](?-1864992396#_Ref57541113)"。*vpi*与*vci*不能同时为0。通常，*vci*取值0到31保留用于特定用途，建议用户不要使用。

【描述】

**[debugging atm packet**]命令用来打开ATM的报文调试信息开关。**undo debugging atm packet**命令用来关闭ATM的报文调试信息开关。

缺省情况下，ATM报文调试信息开关处于关闭状态。

如果不指定接口，则打开所有ATM接口的报文调试信息开关。如果不指定PVC名或者VPI/VCI值对，则打开指定接口的所有PVC的报文调试信息开关。

打开报文调试信息开关之后，就可以观察到ATM接口或者PVC上收发报文的具体信息，这对于系统排错具有很大的参考作用。对于接收的报文，显示所有接收报文的信息，它可以表明发送端是否正确封装了这些报文，这对于网络设备进行检测很有用处。

表1-4 debugging atm packet命令输出信息描述表

字段

描述

Received a packet (length=*length*) on interface *interface-name* PVC *vpi/vci*.

在接口*interface-name*下PVC *vpi/vci*上接收到长度为*length*的报文

Sent a packet (length=*length*) on interface *interface-name* PVC *vpi/vci*.

在接口*interface-name*下PVC *vpi/vci*上发送长度为*length*的报文

Received an IP InARP *type* packet on interface *interface-name* PVC *vpi/vci* (length=*length*, source IP=*source-ip*, target IP=*target-ip*).

在接口*interface-name*下PVC *vpi/vci*上接收到长度为*length*的InARP *type*报文，源IP地址为*source-ip*，目的IP地址为*target-ip*，其中*type*的类型如下：

·request：请求报文

·reply：应答报文

Received an IP InARP *type* packet on interface *interface-name* PVC-group *id* (length=*length*, source IP=*source-ip*, target IP=*target-ip*).

在接口*interface-name*下PVC-group *id*上接收到长度为*length*的InARP *type*报文，源IP地址为*source-ip*，目的IP地址为*target-ip*，其中*type*的类型如下：

·request：请求报文

·reply：应答报文

Sent an IP InARP *type* packet on interface *interface-name* PVC *vpi/vci* (length=*length*, source IP=*source-ip*, target IP=*target-ip*).

在接口*interface-name*下PVC *vpi/vci*上发送长度为*length*的InARP *type*报文，源IP地址为*source-ip*，目的IP地址为*target-ip*，其中*type*的类型如下：

·request：请求报文

·reply：应答报文

Sent an IP InARP *type* packet on interface *interface-name* PVC-group *id* (length=*length*, source IP=*source-ip*, target IP=*target-ip*).

在接口*interface-name*下PVC-group *id*上发送长度为*length*的InARP *type*报文，源IP地址为*source-ip*，目的IP地址为*target-ip*，其中*type*的类型如下：

·request：请求报文

·reply：应答报文

【举例】

\# Router A与Router B通过ATM接口连接，两端配置好IP地址，具体配置如下：

·Router A

\<Sysname\> system-view

Sysname interface atm 2/4/2

Sysname-ATM2/4/2 pvc 10/33

Sysname-ATM2/4/2-pvc-10/33 map ip inarp 1

Sysname-ATM2/4/2-pvc-10/33 quit

Sysname-ATM2/4/2 ip address 10.10.10.11 255.255.255.0

·Router B

\<Sysname\> system-view

Sysname interface atm2/4/3

Sysname-ATM2/4/3 pvc 10/33

Sysname-ATM2/4/3-pvc-10/33 map ip inarp 1

Sysname-ATM2/4/3-pvc-10/33 quit

Sysname-ATM2/4/3-pvc-10/33 ip address 10.10.10.10 255.255.255.0

\# 在Router A打开所有ATM接口的报文调试开关。

\<Sysname\> debugging atm packet

\*Dec 24 09:45:46:236 2012 Sysname ATM/7/PACKET: -MDC=1;

Sent an IP InARP request packet on interface ATM2/4/2 PVC 10/33 (length=16, source IP =10.10.10.11, target IP=0.0.0.0).

*// 发送了InARP请求报文，长度16，源IP地址为10.10.10.11，目的IP地址为0.0.0.0*

