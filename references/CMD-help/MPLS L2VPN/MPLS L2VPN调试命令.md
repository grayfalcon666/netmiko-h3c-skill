<!-- CMD-INDEX
  debugging bgp update l2vpn          | 用户视图             | L10
  debugging bgp update-group l2vpn    | 用户视图             | L196
  debugging l2vpn management          | 用户视图             | L362
  debugging l2vpn packet              | ]                | L776
  debugging mpls ldpvc                | 用户视图             | L1112
  debugging mpls bgpvc                | 用户视图             | L1516
-->

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging bgp update l2vpn**

------------------------------------------------------------------------

【命令】

**[debugging bgp update** *ip-address* [ *mask-length*  **l2vpn** [ **receive** \| **send** ]]]

**[undo debugging bgp update** *ip-address* [ *mask-length*  **l2vpn** [ **receive** \| **send** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：对等体的IP地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

**[receive**]：表示接收的BGP报文。

**[send**]：表示发送的BGP报文。

【描述】

**[debugging bgp update l2vpn**]命令用来打开BGP L2VPN的Update报文调试信息开关。**undo** **debugging bgp l2vpn**命令用来关闭BGP L2VPN的Update报文调试信息开关。

缺省情况下，BGP L2VPN的Update报文调试信息开关处于关闭状态。

表1-1 debugging bgp update l2vpn命令输出信息描述表

字段

描述

BGP_L2VPN.: Recv UPDATE from peer *ip-address* with following destinations

从对等体*ip-address*接收到Update消息

BGP_L2VPN.: Send UPDATE to peer *ip-address* for following destinations

向对等体*ip-address*发送Update消息

Update message length

Update消息的长度，单位为字节

Origin

Origin属性，即信息的来源，取值包括：

·IGP：表示产生于本AS内

·EGP：表示是通过EGP学到的

·Incomplete：表示来源无法确定

AS path

AS Path属性，即从本地到目的地所要经过的所有AS号

Next hop

下一跳地址

Local pref

本地优先级

MED

MED（Multi-Exit Discriminator，多出口区分）值

Ext-Community

扩展团体属性，包括：

·RT：Route Target属性

·L2VPN info：L2VPN相关信息，包括MTU值、封装类型（Encap type）

·VPLS ID：用来标识该PE所属的VPLS实例

AFI/SAFI

地址族/子地址族

RD

路由标识符

Site ID

VPN内站点的编号

Label offset

标签块偏移量

Label base

标签块的初始标签值

Label range

标签块大小

CSV

接入链路状态

PE address

PE的地址

【举例】

\# 打开对等体1.1.1.3的BGP L2VPN的Update报文调试信息开关。从对等体1.1.1.3接收到BGP L2VPN的Update报文时打印如下调试信息。

\<Sysname\> debugging bgp update 1.1.1.3 l2vpn receive

\*Sep 24 06:44:31:368 2012 Sysname BGP/7/DEBUG: -MDC=1;                             

         BGP_L2VPN.: Recv UPDATE from peer 1.1.1.3 with following destinations:

         Update message length : 87                                            

         Origin       : IGP                                                    

         AS path      : 100                                                    

         Next hop     : 1.1.1.3                                                

         Ext-Community: \<RT: 3:2\>, \<L2VPN info: MTU 1500, Encap type ATM AAL5 VCC transport\>

         AFI/SAFI     : 196/128 (L2VPN Draft)                                    

         RD           : 9:8                                                    

         Site ID      : 9                                                      

         Label offset : 0                                                      

         Label base   : 775000                                                 

         Label range  : 10

         CSV          : 0x01000AFFFF

*// 从对等体1.1.1.3接收到BGP L2VPN的Update消息，消息长度为87字节，标签块信息产生于本AS内，AS路径为100，下一跳为1.1.1.3，Route Target属性为3:2，MTU为1500字节，封装类型为ATM AAL5 VCC transport，地址族为196，子地址族为128，路由标识符为9:8，VPN内站点编号为9，标签块偏移量为0，标签块的初始标签值为775000，标签块大小为10，接入链路状态值为0x01000AFFFF。*

\# 打开对等体2.2.2.3的BGP L2VPN的Update报文调试信息开关。从对等体2.2.2.3接收到BGP L2VPN的Update报文时打印如下调试信息。

\<Sysname\> debugging bgp update 2.2.2.3 l2vpn receive

\*Sep 25 04:32:32:336 2012 Sysname BGP/7/DEBUG: -MDC=1;                             

         BGP_L2VPN.: Recv UPDATE from peer 2.2.2.3 with following destinations:

         Update message length : 82                                            

         Origin       : IGP                                                    

         AS path      : 100                                                       

         Next hop     : 2.2.2.3                                                

         Local pref   : 100                                                    

         Ext-Community: \<RT: 3:2\>, \<VPLS ID: 5:67\>                             

         AFI/SAFI     : 25/65 (L2VPN)                                    

         RD           : 5:1                                                    

         PE address   : 1.2.3.4

*// 从对等体2.2.2.3接收到BGP L2VPN的Update消息，消息长度为82字节，邻居自动发现信息产生于本AS内，AS路径为100，下一跳为2.2.2.3， Route Target属性为3:2，VPLS ID为5:67*，*地址族为**25，子地址族为65，RD为5:1，PE的地址为1.2.3.4。*

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging bgp update-group l2vpn**

------------------------------------------------------------------------

【命令】

**[debugging bgp update-group l2vpn**]

**[undo debugging bgp update-group l2vpn**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bgp update-group l2vpn**]命令用来打开BGP L2VPN地址族的打包组调试信息开关。**undo debugging bgp update-group l2vpn**命令用来关闭BGP L2VPN地址族的打包组调试信息开关。

缺省情况下，BGP L2VPN地址族的打包组调试信息开关处于关闭状态。

表1-2 debugging bgp update-group l2vpn命令输出信息描述表

字段

描述

Send UPDATE to update-group *group-id* for following destinations

向BGP打包组*group-id*发送L2VPN信息更新

Send UPDATE(Withdraw) to update-group *group-id* for following destinations

向BGP打包组*group-id*发送L2VPN信息撤销

Origin

Origin属性

AS path

AS Path属性

Next hop

下一跳地址

Local Pref

本地优先级

MED

MED（Multi-Exit Discriminator，多出口区分）值

Ext-Community

扩展团体属性，包括：

·RT：Route Target属性

·L2VPN info：L2VPN相关信息，包括MTU值、封装类型（Encap type）

·VPLS ID：用来标识该PE所属的VPLS实例

 

AFI/SAFI

地址族/子地址族

RD

路由标识符

Site ID

VPN内站点的编号

Label offset

标签块的偏移量

Label base

标签块的初始标签值

Label range

标签块大小

CSV

接入链路状态

PE address

PE的地址

【举例】

\# 打开BGP L2VPN地址族的打包组调试信息开关，发布BGP L2VPN标签块信息时，设备上将打印如下信息。

\<Sysname\> debugging bgp update-group l2vpn

\*Sep 24 06:44:31:370 2012 Sysname BGP/7/DEBUG: -MDC=1;                             

         BGP_L2VPN.: Send UPDATE to update-group 0 for following destinations: 

         Origin       : IGP                                                    

         AS path      : 200                                                

         Next hop     : 1.1.1.3                                                

         Ext-Community: \<RT: 3:2\>, \<L2VPN info: MTU 1500, Encap type BGP VPLS\> 

         AFI/SAFI     : 25/65 (L2VPN)                                    

         RD           : 9:8                                                     

         Site ID      : 9                                                      

         Label offset : 0                                                      

         Label base   : 775000                                                  

         Label range  : 10  

*// 向BGP打包组0发送L2VPN信息更新，标签块信息产生于本AS内，AS路径为200，下一跳为1.1.1.3，Route Target属性为3:2，MTU为1500字节，封装类型为BGP VPLS，地址族为25，子地址族为65，路由标识符为9:8，VPN内站点编号为9，标签块偏移量为0，标签块的初始标签值为775000，标签块大小为10。*

\# 打开BGP L2VPN地址族的打包组调试信息开关，发布BGP L2VPN邻居自动发现信息时，设备上将打印如下信息。

\<Sysname\> debugging bgp update-group l2vpn

\*Sep 25 22:29:54:489 2012 Sysname BGP/7/DEBUG: -MDC=1;

BGP_L2VPN.: Send UPDATE to update-group 0 for following destinations: 

         Origin       : IGP                                                     

         AS path      : 200                                                       

         Next hop     : 0.0.0.0                                                

         Local pref   : 100                                                     

         Ext-Community: \<RT: 3:2\>, \<VPLS ID: 5:67\>                             

         AFI/SAFI     : 25/65(l2VPN)                                    

         RD           : 5:1                                                     

         PE address   : 1.2.3.4 

*// 向BGP打包组0发送L2VPN信息更新，邻居自动发现信息产生于本AS内，AS路径为200，下一跳地址为0.0.0.0，扩展团体属性RT为3:2，VPLS ID为5:67，地址族为25，子地址族为65，路由标识符为5:1，PE的地址为1.2.3.4。*

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging l2vpn management**

------------------------------------------------------------------------

【命令】

**[debugging l2vpn management**[ { **all** \| **error** \| **event** \| **hsb** \| **process** }]]

**[undo debugging l2vpn management**[ { **all** \| **error** \| **event** \| **hsb** \| **process** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示L2VPN的所有调试信息开关。

**[error**]：表示L2VPN的错误调试信息开关。

**[event**]：表示L2VPN的事件调试信息开关。

**[hsb**]**：**表示L2VPN备份调试信息开关。

**[process**]：表示L2VPN创建PW过程调试信息开关。

【描述】

**[debugging l2vpn management**]命令用来打开L2VPN的调试信息开关。**undo debugging l2vpn management**命令用来关闭L2VPN的调试信息开关。

缺省情况下，L2VPN调试信息开关处于关闭状态。

表1-3 debugging l2vpn management error命令输出信息描述表

字段

描述

Failed to save vsi (*vsi-index*) to DBM.

保存VSI到DBM失败，此VSI索引为*vsi-index*

Failed to save peer to DBM.

保存peer到DBM失败

Failed to save the configuration of binding a VSI with an interface. Interface index: *if-index.*

保存接口绑定配置到DBM失败，接口索引为*if-index*

Failed to free link ID (*link-id*) because it has been requested by another protocol. VSI index: *vsi-index*, new protocol: *new-protocol*, old protocol: *old-protocol*.

释放链路的标识*link-id*失败，因为此*link-id*已经被其他协议申请，对应的VSI索引为*vsi-index*，申请该*link-id*的新协议为*new-protocol*，旧协议为*old-protocol*

Encapsulation mode not supported.

不支持的链路封装类型

Invalid VSI index (*vsi-index*).

非法的VSI索引*vsi-index*

Failed to send response message (*message type*).

向应用回应消息失败，消息类型为*message-type*

Failed to send VSI notification.

向应用通告VSI信息失败

Failed to start license reconnect timer for *feature-name.*

启动特性*feature-name*的license重连定时器失败

The *feature-name* feature failed to receive messages from license daemon.

特性*feature-name*接收来自License进程的消息失败

The *feature-name* feature failed to get license data from license daemon.

特性*feature-name*向License进程获取License数据失败

表1-4 debugging l2vpn management event命令输出信息描述表

字段

描述

Received protocol (*protocol*) GR event (*event-type*).

收到协议GR事件，协议号为*protocol*，事件类型为*event-type*

Received interface event (*event-type*). Interface index: *if-index*.

收到接口事件，事件类型为*event-type*，接口索引为*if-index*

Received VSI (*vsi-index*) deleted notification from L2VFIB.

从L2VFIB收到VSI已删除的通告，VSI索引为*vsi-index*

Received L2VPN-disabled notification from L2VFIB.

从L2VFIB收到L2VPN已去使能的通告

Received L2VPN-disabled notification from application. Socket: *socket- id*.

从应用收到L2VPN已去使能的通告，应用对应的套接字ID为*socket- id*

Received VSI (*vsi-index*) deleted notification from application. Socket: *socket- id*.

从应用收到VSI已删除的通告，VSI索引为*vsi-index*，应用对应的套接字ID为*socket- id*

Received batch request for VSIs.

收到VSI批量请求事件

Received batch request for peers.

收到peer批量请求事件

Notified VSI event (*event-type*) successfully. VSI index: *vsi-index*

通告VSI事件*event-type*成功，VSI索引为*vsi-index*

Notified peer event (*event-type*) successfully.

通告peer事件*event-type*成功

Notified AC state successfully. VSI index: *vsi-index*

通告AC状态成功，VSI索引为*vsi-index*

Notified PW class event (*event-type*) successfully. PW class name: *pw-class-name*

通告PW模板事件*event-type*成功，PW模板名字为*pw-class-name*

Notified L2VPN-disabled event successfully.

通告L2VPN去使能事件成功

Notified batch response event (*event-type*).

通告批量回应事件*event-type*

Sent GR start to L2VFIB.

向L2VFIB发送GR开始事件

Sent GR end to L2VFIB.

向L2VFIB发送GR结束事件

Responded HA with an event (*event-type*).

向HA回应一个事件*event type*

Received an HA event (*event-type*).

收到一个HA事件*event type*

表1-5 debugging l2vpn management hsb命令输出信息描述表

字段

描述

Sent an HA message (*message-type*).

发送HA消息，消息类型为*message-type*

Received an HA message (*message-type*).

收到HA消息，消息类型为*message-type*

表1-6 debugging l2vpn management process命令输出信息描述表

字段

描述

Downloaded VSI binding to L2VFIB. Configuration type: *type*, VSI index: *vsi-index*, Interface index: *if-index*, service instance ID: *srv-id*

向L2VFIB下发VSI绑定，配置类型为*type*，VSI索引为*vsi-index*，接口索引为*if-index*，服务实例ID为*srv-id*

Downloaded VSI to L2VFIB. Configuration type: *type*, VSI name: *vsi-name*

向L2VFIB下发VSI信息，配置类型为*type*，VSI名字为*vsi-name*

Downloaded AC to L2VFIB. Operation type: *oper-type*, VSI index: *vsi-index*, link ID: *link-id*

向L2VFIB下发AC表项，操作类型为*oper-type*，VSI索引为*vsi-index*，链路ID为*link-id*

Downloaded PW to L2VFIB. Operation type: *oper-type*, VSI index: *vsi-index*, link ID: *link-id*, result: *result*

向L2VFIB下发PW表项，操作类型为*oper-type*，VSI索引为*vsi-index*，链路ID为*link-id*，处理结果为*result*

Received MPLS PW addition notification. Protocol: *protocol*, VSI index: *vsi-index*, link ID: *link-id*, state: *state*

收到添加MPLS PW消息，信令协议号为*protocol*，VSI索引为*vsi-index*，链路ID为*link-id*，PW状态为*state*

Received MPLS PW update notification. Protocol: *protocol*, VSI index: *vsi-index*, link ID: *link-id*, state: *state*

收到更新MPLS PW消息，信令协议号为*protocol*，VSI索引为*vsi-index*，链路ID为*link-id*，PW状态为*state*

Received PW deletion notification. VSI index: *vsi-index*, link ID: *link-id*, backup flag: *flag*

收到删除一条PW的通知，VSI索引为*vsi-index*，链路ID为*link-id*，备份标记为*flag*

Processed PW switchover. Peer: *lsr-id*, PW ID: *pw-id*.

处理PW切换，要切换的PW对端的LSR ID为*lsr-id，*PW ID为*pw-id*

Updated PW\'s VN info. Result: *result*, old VN ID: *old-vnid*, old FRR VN ID: *old-frr-vnid*, new VN ID: *new-vnid*, new FRR VN ID: *new-frr-vnid*

更新PW的VN信息，处理结果为*result*，旧的VN ID为*old-vnid*，旧的FRR VN ID为*old-frr-vnid*，新的VN ID为*new-vnid*，新的FRR VN ID为*new-frr-vnid*

Sent VN smooth start to FIB.

向FIB发送VN平滑开始

Sent VN smooth end to FIB.

向FIB发送VN平滑结束

Sent VN to FIB. VN ID: *vnid*, event: *event*-*type*, peer: *peer-lsrid*, nexthop number: *number*

向FIB下发VN，VN ID为*vnid*，事件类型为*event*-*type*，对端LSR ID为*peer-lsrid*，等价下一跳个数为*number*

Sent dual VNs to FIB. VN ID: *vnid*, event: *event*-*type*, peer: *peer-lsrid*, NID: *nid*, backup peer: *backup-peer-lsrid*, backup NID: *backup-nid*

向FIB下发主备类型的VN，VN ID为*vnid*，事件类型为*event*-*type*，主隧道的对端LSR ID为*peer-lsrid*，主隧道的NID为*nid*，备份隧道的对端LSR ID为*backup-peer-lsrid*，备隧道NID为*backup-nid*

Notified the application to send MAC withdraw message. Peer: *lsr-id*, PW ID: *pw-id*

通知应用发送MAC地址回收消息，需要发送消息的对端为*lsr-id*，PW ID为*pw-id*

VN switchover paused.

VN切换处理暂停

VN switchover completed.

VN切换处理完成

Sent VSI deletion event to L2VFIB. VSI index: *vsi-index*.

向L2VFIB发送VSI删除事件，VSI索引为*vsi-index*

Processed GR event (*type*) for protocol (*protocol*). VSI index: *vsi-index*

处理协议GR事件，事件类型为*type*，协议号为*protocol*，VSI索引为*vsi-index*

Received PW statistics disabling event. Total number is *number.*

收到关闭PW统计功能事件，当前使能了统计功能的PW总数为*number*

Received PW statistics enabling event. Total number is *number.*

收到关闭PW统计功能事件，当前使能了统计功能的PW总数为*number*

Timer (15 minutes) for PW MIB statistics timed out.

PW MIB统计定时器超时，定时器时长为十五分钟

Started license reconnect timer for *feature-name*.

启动特性*feature-name*的License 重连定时器

Stopped license reconnect timer for *feature-name*.

停止特性*feature-name*的License 重连定时器

【举例】

\# 打开L2VPN的错误调试信息开关。关闭LSM进程时，设备上会打印如下调试信息。

\<Sysname\> debugging l2vpn management error

\<Sysname\> process shutdown name lsmd

\*Aug 27 13:02:23:947 2011 Sysname L2VPN/7/ERROR: -MDC=1; Failed to connect to LSM.

*// 和LSM进程连接失败*

\# 打开L2VPN的事件调试信息开关。创建一个VSI，配置信令协议为LDP，并在LDP信令视图下配置一条PW，设备上会打印如下调试信息。

\<Sysname\> debugging l2vpn management event

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1

\*Sep  5 08:56:16:960 2011 Sysname L2VPN/7/EVENT: -MDC=1; Notified VSI event (0) successfully. VSI index: 0xa.

*// 向应用通告VSI创建事件成功，事件类型为0，VSI索引为0xa。*

Sysname-vsi-vpn1 pwsignaling ldp

Sysname-vsi-vpn1-ldp

\*Sep  5 08:56:41:652 2011 Sysname L2VPN/7/EVENT: -MDC=1; Notified VSI event (3) successfully. VSI index: 0xa.

*// 向应用通告信令视图创建事件成功，事件类型为3，VSI索引为0xa。*

Sysname-vsi-vpn1-ldp peer 1.1.1.1 pw-id 1234

Sysname-vsi-vpn1-ldp-1.1.1.1-1234

\*Sep  5 08:57:07:365 2011 Sysname L2VPN/7/EVENT: -MDC=2; Notified peer event (8) successfully.

*// 向应用通告peer创建事件成功，事件类型为8。*

\# 在三层以太网接口GigabitEthernet1/0/1上绑定VSI，打印如下调试信息。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 xconnect vsi vpn1

\*Sep  5 08:58:32:680 2011 Sysname L2VPN/7/EVENT: -MDC=1; Notified AC state successfully. VSI index: 0xa.

*// 向应用通告AC状态成功，VSI索引为0xa。*

\# 打开L2VPN创建PW过程调试信息开关。在设备上创建一个VSI，打印如下调试信息。

\<Sysname\> debugging l2vpn management process

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1

\*Sep  5 09:02:17:781 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Downloaded VSI to L2VFIB. Configuration type: 4, VSI name: vpn1.

*// 创建VSI，向内核下发VSI配置。*

\# 设备两端创建PW ID相同的PW，然后再绑定此VSI，打印如下信息。

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling ldp

Sysname-vsi-vpn1-ldp peer 1.1.1.1 pw-id 222

\*Sep  5 09:08:27:343 2011 SysnameL2VPN/7/PROCESS: -MDC=1; Received MPLS PW addition notification. Protocol: 3, VSI index: 0xa, link ID: 8, state: 3.

\*Sep  5 09:08:27:343 2011 SysnameL2VPN/7/PROCESS: -MDC=1; Updated PW\'s VN info. Result: 0, old VN ID: 0x0, old FRR VN ID: 0x0, new VN ID: 0x60000000, new FRR VN ID:

 0x0.

*[// peer*]*创建时生成down状态的PW，并关联VN*

Sysname-GigabitEthernet1/0/4 xconnect vsi vpn1

\*Sep  5 09:09:24:648 2011 SysnameL2VPN/7/PROCESS: -MDC=1; Downloaded xconnect to L2VFIB. Configuration type: 7, VSI index: 0xa, Interface index: 341, service instance ID: 0.

\*Sep  5 09:09:24:650 2011 SysnameL2VPN/7/PROCESS: -MDC=1; Downloaded AC to L2VFIB. Operation type: 3, VSI index: 0xa, link ID: 0.

\*Sep  5 09:09:24:650 2011 SysnameL2VPN/7/PROCESS: -MDC=1; Received MPLS PW update notification. Protocol: 3, VSI index: 0xa, link ID: 8, state: 3.

\*Sep  5 09:10:32:568 2011 SysnameL2VPN/7/PROCESS: -MDC=1; Downloaded PW to L2VFIB. Operation type: 1, VSI index: 0xa, link ID: 8, result: 0.

*// 绑定VSI后AC状态变为up，L2VPN收到PW更新，PW状态变为up，向内核下发绑定配置和AC表项，并向内核下发up的PW。*

\# 创建备份LDP PW。

Sysname-vsi-hvpls-ldp-1.1.1.1-222 backup-peer 4.4.4.9 pw-id 444

\*Sep  5 09:11:46:960 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Received MPLS PW addition notification. Protocol: 3, VSI index: 0x3, link ID: 8, state: 3.

\*Sep  5 09:11:46:961 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Sent dual VNs to FIB. VN ID: 0x860000002, event: 0, peer: 1.1.1.1, NID: 0x408, backup peer: 4.4.4.9, backup NID: 0xffffffff.

\*Sep  5 09:11:46:961 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Sent dual VNs to FIB. VN ID: 0x960000003, event: 0, peer: 4.4.4.9, NID: 0xffffffff, backup peer: 1.1.1.1, backup NID: 0x408.

\*Sep  5 09:11:46:962 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Updated PW\'s VN info. Result: 0, old VN ID: 0x60000000, old FRR VN ID: 0x0, new VN ID: 0x860000002, new FRR VN ID: 0x960000003.

\*Sep  5 09:11:46:962 2011 Sysname L2VPN/7/PROCESS: -MDC=1; Downloaded PW to L2VFIB. Operation type: 1, VSI index: 0x3, link ID: 8, result: 0.

*// 创建备份PW，L2VPN收到PW更新，并更新PW关联的VN信息，将新的VN信息向内核下发。L2VPN向内核下发PW更新。*

\# 打开L2VPN的备份调试信息开关。创建VSI，并创建LDP PW后，插入备板，设备上打印如下调试信息。

\<Sysname\> debugging l2vpn management hsb

\*Aug 27 12:43:43:143 2011 Sysname L2VPN/7/HSB: -MDC=1; Send an HA message, type(0).

*// 备板插入，进行批量备份。*

\# 备板在位时，创建PW，进行实时备份。

\<Sysname\> system-view

Sysname vsi test

Sysname-vsi-test pwsignaling ldp

Sysname-vsi-test-ldp peer 23.2.2.2 pw-id 12345

Sysname-vsi-test-ldp-23.2.2.2-12345

\*Aug 27 12:45:26:332 2011 Sysname L2VPN/7/HSB: -MDC=1; Sent an HA message (1).

\*Aug 27 12:45:26:353 2011 Sysname L2VPN/7/HSB: -MDC=1; Sent an HA message (1).

*// 创建PW时会进行link ID申请和VN创建，对link ID和VN进行实时备份。*

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging l2vpn packet**

------------------------------------------------------------------------

【命令】

**[debugging l2vpn packet ****xconnect-group ***group-name* **[connection ***connection-name *[\| **site** *site-id* **remote-site-id** *remote-site-id* }  \| **vsi** *vsi-name*]**]

**[undo debugging l2vpn packet ****xconnect-group ***group-name* **[connection ***connection-name *[\| **site** *site-id* **remote-site-id** *remote-site-id* }  \| **vsi** *vsi-name* ]]

【视图】]

用户视图]

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[xconnect-group **]*group-name*：表示指定交叉连接组的L2VPN报文调试信息开关。*group-name*表示交叉连接组的名称，为1～31个字符的字符串，区分大小写。

**[connection ***connection-name*]：表示指定交叉连接的L2VPN报文调试信息开关。*connection-name*表示交叉连接的名称，为1～20个字符的字符串，不能包含字符"-"，区分大小写。

**[site** *site-id*]：指定本地站点ID。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[remote-site-id** *remote-site-id*]：指定远端站点ID。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。同时指定**site-id** *site-id*和**remote-site-id** *remote-site-id*参数，则表示本端站点和指定远端站点之间交叉连接的L2VPN报文调试信息开关。

**[vsi** *vsi-name*]：表示指定VSI的L2VPN报文调试信息开关。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。

【描述】

**[debugging l2vpn packet**]命令用来打开L2VPN报文调试信息开关。**undo debugging l2vpn packet**命令用来关闭L2VPN报文调试信息开关。

缺省情况下，L2VPN报文调试信息开关处于关闭状态。

执行本命令时，如果不指定任何参数，则表示所有VSI和交叉连接组的L2VPN报文调试信息开关。

表1-7 debugging l2vpn packet命令输出信息描述表

字段

描述

L2VPN input:

收到L2VPN报文

L2VPN output:

发送L2VPN报文

L2VPN fsinput:

收到L2VPN快转报文

L2VPN fsoutput:

发送L2VPN快转报文

Received a packet from interface *interface-name* Service Instance *Service-Instance-ID*

从接口*interface-name*收到数据包。如果是从二层以太网接口的服务实例（Service Instance）收到的报文，则*Service-Instance-ID*为接收报文的服务实例ID*。*

Sent a packet to interface *interface-name*

发送数据包到接口*interface-name*

Sent a packet to chassis *chassis-number* slot *slot-number* cpu *cpu-number*, PktLen = *length*, result *result*.

发送数据包到成员设备*chassis-number*单板*slot-number*的编号为*cpu-number*的CPU，数据包长度为*length*，发送结果为*result*

Received a packet from the PW

从PW接收报文

Connection-ID

PW的Connection ID

Link-ID

PW的LINK ID

Control-Word

如果有控制字，则显示其内容

VC-Label

PW收发报文时，对应的VC标签

PktLen

数据包的长度

Label

标签（包括私网内层标签和公网外层标签）

EXP

MPLS报文的EXP值

TTL

MPLS报文的TTL值

Packet discarded because the PW isn't up.

PW没有处于UP状态，报文被丢弃。主备PW中处于block状态(当前不被使用)的PW接收到的报文，无法被转发。

Packet discarded because the AC isn't up.

AC没有处于UP状态，报文被丢弃。

Packet discarded because the Tunnel isn't up.

Tunnel没有处于UP状态，报文被丢弃

Packet discarded because the forwarding type isn\'t VPWS.

报文不是VPWS转发，报文被丢弃。

Packet discarded because interface *interface-name* Service Instance *Service-Instance-ID* isn't an AC.

根据接口*interface-name*和服务实例（Service Instance）没有找到AC，报文被丢弃

Packet discarded because failed to find a PW with Connection-ID *connection-id* Link-ID *link-id*.

根据Connection-ID和Link ID没有找到PW，报文被丢弃

Packet discarded because the packet should include the control word field.

PW支持控制字，而报文不含控制字，丢弃报文

Packet discarded because no corresponding AC or PW exists.

找不到对应的表项，丢弃报文。

Removed the control word field.

砍掉控制字

Removed the P-tag

砍掉P-Tag字段，该Tag是一个服务提供商网络为了区分用户而要求用户压入的"服务定界符"

Added the P-tag: priority *priority*, CFI *cfi-value*, VLAN ID *vlan-id.*

添加P-Tag字段，优先级为*priority，*CFI为*cfi-value*，VLAN ID为*vlan-id *

Swapped the P-tag: priority *priority*, CFI *cfi-value*, VLAN ID *vlan-id.*

交换P-Tag字段，交换后的优先级为*priority*，CFI为*cfi-value*，VLAN ID为*vlan-id *

Packet discarded because no forwarding information exists for the PW.

PW没有对应的转发信息，报文被丢弃

Processed L2VPN service. *interface-name*, service phase: *phase*, service result: *result.*

接口*interface-name*L2VPN转发业务

*[phase*]为业务处理阶段，取值如下：

·input：入报文阶段

·output：出报文阶段

*[result*]为业务处理结果，取值如下：

·continue：报文继续转发

·stop：报文被业务截获，不用继续转发

·stop err：业务处理失败，不用继续转发

·continue with new data：报文被业务修改，继续转发

Sent a VCCV packet through the PW.

通过PW发送VCCV报文

Packet discarded because the CC type of the PW isn't contrl word, or the CV type isn't Raw-BFD.

报文不是UDP封装，但PW CC类型不是控制字方式或CV类型不是Raw-BFD

Packet discarded because the PW doesn't support ping operation.

PW不支持lsp ping， 丢弃报文

Packet discarded because the PW doesn't support BFD detection.

PW不支持BFD检测，丢弃报文

Packet discarded because the UDP destination port is invalid.

UDP封装的报文，目的端口无效，丢弃报文

Packet discarded because adding the ACH failed.

封装关联信道头失败，丢弃报文

Received a VCCV packet. The CC type is *type*.

收到VCCV报文，CC类型是*type*

Packet discarded because CC type in the packet is different from the PW.

报文中CC类型与PW不一致（报文攻击时出现），丢弃报文

Packet discarded because the packet contains ACH, but the PW doesn't support control word function.

PW 不支持控制字，但是报文携带关联信道头，丢弃报文

A Raw-BFD VCCV packet discarded because the CV type of the PW isn't Raw-BFD.

PW CV类型不是Raw-BFD，而报文为Raw-BFD VCCV，丢弃报文

Packet discarded because the IP field of the packet is invalid.

IP 无效，丢弃报文

KLSPV failed to process the echo request packet.

 KLSPV处理echo request报文失败

Packet discarded because no suitable control channel for the PW.

PW没有控制通道支持报文转发，丢弃报文

A BFD UDP packet discarded because the CV type of PW isn\'t BFD.

 PW CV类型不是BFD方式，而报文采用BFD UDP封装，丢弃报文

L2L3: Received a packet from interface *interface-name*, PktLen=*packet-len*.

从L2VE/L3VE接口*interface-name*收到报文，报文长度是*packet-len*

L2L3: Sent a packet to interface *interface-name*, PktLen=*packet-len*.

发送报文给L2VE/L3VE接口*interface-name*，报文长度是*packet-len*

Received a packet from interface *interface-name*, KeyType=*keytype*, KeyID=*keyid*, PktLen=*packet-len*.

从接口*interface-name*收到数据包，该数据包为*keytype*报文，KeyID为*keyid*，数据包长度为*packet-len*字节

*[Keytype*]取值为VXLAN，表示数据包为VXLAN报文

Sent a packet on interface *interface-name*, KeyType=*keytype*, KeyID=*keyid*, PktLen=*packet-len*.

从接口*interface-name*发送数据包，该数据包为*keytype*报文，KeyID为*keyid*，数据包长度为*packet-len*字节

*[Keytype*]取值为VXLAN，表示数据包为VXLAN报文

Packet discarded because the Tunnel doesn\'t exist.

找不到对应的隧道，报文被丢弃

Packet discarded because the Tunnel isn\'t up.

隧道没有处于UP状态，报文被丢弃

Packet broadcast to VSI (*vsi-index*).

报文广播到VSI中，VSI索引为*vsi-index*

Packet delivered to the VSI gateway interface of VSI (*vsi-index*), Result=*result*.

报文上送给VSI索引为*vsi-index*的VSI网关接口，上送结果为*result*

*[result*]取值包括：

· 0{.TableTextChar}：{.TableTextChar}表示成功

· 588840961{.TableTextChar}：{.TableTextChar}表示快转上送成功

· 1073807361{.TableTextChar}：{.TableTextChar}表示失败

Packet discarded because VSI index (*vsi-index*) or LinkID (*link-id*) is invalid.

VSI索引*vsi-index*或链路ID *link-id*无效，报文被丢弃

Packet discarded because the VSI gateway interface isn\'t up, ifIndex=*ifIndex*.

VSI网关接口没有处于UP状态，报文被丢弃，网关接口的接口索引为*ifIndex*

VSI gateway interface *interface-name* transmitted a packet, VSI=*vsi-index*, Link-ID=*link-id*, PktLen=*packet-len*.

VSI网关接口*interface-name*传输了一个数据包，该数据包从VSI索引为*vsi-index*，Link-ID为*link-id*的链路发送，数据包长度为*packet-len*字节

Failed to send a packet, VSI=*vsi-index*, Link-ID=*link-id*.

从VSI索引为*vsi-index*，Link-ID为*link-id*的链路发送数据包失败

VTEP doesn\'t reply to the ARP request on behalf of the remote-site host because ARP flooding suppression is disabled.

ARP泛洪抑制功能未使能，不进行ARP代答

【举例】

\# 打开L2VPN报文调试信息开关，从AC接口收到报文，并通过PW转发该报文时，设备上打印如下调试信息。

\<Sysname\> debugging l2vpn packet

\*Oct 19 09:13:03:979 2010 Sysname L2VFW/7/PACKET:Slot=2;

L2VPN Input: Received a packet from interface GE1/0/1 Service Instance 0, PktLen=70.

*// 从接口GigabitEthernet1/0/1的以太网服务实例0接收到报文，报文长度为70字节。*

\*Dec 18 17:29:37:708 2012 Sysname L2VFW/7/PACKET: -MDC=1;

PUSH Label=1151, EXP=0, TTL=255.

*// 为报文添加PW标签1151，标签的EXP为0，TTL为255。*

\*Dec 18 17:29:37:708 2012 Sysname L2VFW/7/PACKET: -MDC=1;

PUSH Label=1150, EXP=0, TTL=255.

*// 为报文添加公网隧道标签1150，标签的EXP为0，TTL为255。*

\# 打开L2VPN报文调试信息开关，将报文发送到L2VE接口时，打印如下调试信息。

\<Sysname\> debugging l2vpn packet

\*Jul  8 15:47:10:062 2013 Sysname L2VFW/7/PACKET: -Slot=2;

L2L3: Sent a packet to interface L2VE130, PktLen=98.

*// 将报文发送到L2VE130接口，报文长度为98字节。*

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging mpls ldpvc**

------------------------------------------------------------------------

【命令】

**[debugging mpls ldpvc **[{ **advertisement** \| **all** \| **error** \| **event** \| **hsb** }]]

**[undo debugging mpls ldpvc**[ { **advertisement** \| **all** \| **error** \| **event** \| **hsb** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advertisement**]：表示用来通告PW标签的LDP消息的调试信息开关。

**[all**]：表示MPLS LDP VC的所有调试信息开关。

**[error**]：表示MPLS LDP VC的错误调试信息开关。

**[event**]：表示MPLS LDP VC的事件调试信息开关。

**[hsb**]：表示MPLS LDP VC备份调试信息开关。

【描述】

**[debugging mpls ldpvc**]命令用来打开MPLS LDP VC的调试信息开关。**undo debugging mpls ldpvc**命令用来关闭MPLS LDP VC的调试信息开关。

缺省情况下，MPLS LDP VC调试信息开关处于关闭状态。

表1-8 debugging mpls ldpvc advertisement命令输出信息描述表

字段

描述

Received a *message-type* message.

Message content:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSR ID of peer PE:             *peer-lsrid*

VC ID:                                 *vc-id*

VC type:                             *vc-type*

Label:                                 *label*

LDP status code:     *         status-code*

PW status code:            *    pw-status-code*

C-bit:                               *   c-Bit*

收到一个*message-type*消息，

消息内容如下：

·对端PE的LSR ID为*peer-lsrid*

·VC ID为*vc-id*

·VC类型为*vc-type*

·标签为*label*

·LDP状态码为*status-code*

·PW状态码为*pw-status-code*

·是否携带控制字比特为*c-Bit*

Received a *message-type* message.

Message content:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSR ID of peer PE:             *peer-lsrid*

VPLS ID:                            *vpls-id*

SAII:                                   *saii*

TAII:                                   *taii*

VC type:                             *vc-type*

Label:                                 *label*

LDP status code:   *            status-code*

PW status code:            *    pw-status-code*

C-bit:                               *   c-Bit*

收到一个*message-type*消息，

消息内容如下：

·对端PE的LSR ID为*peer-lsrid*

·VPLS ID为*vpls-id*

·SAII为*saii*

·TAII为*taii*

·VC类型为*vc-type*

·标签为*label*

·LDP状态码为*status-code*

·PW状态码为*pw-status-code*

·是否携带控制字比特为*c-Bit*

Sent a *message-type* message.

Message content:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSR ID of peer PE:             *peer-lsrid*

VC ID:                                 *vc-id*

VC type:                             *vc-type*

Label:                                 *label*

LDP status code:             *          status-code*

PW status code:            *    pw-status-code*

C-bit:                               *   c-Bit*

发送一个*message-type*消息，

消息内容如下：

·对端PE的LSR ID为*peer-lsrid*

·VC ID为*vc-id*

·VC类型为*vc-type*

·标签为*label*

·LDP状态码为*status-code*

·PW状态码为*pw-status-code*

·是否携带控制字比特为*c-Bit*

Sent a *message-type*  message.

Message content:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSR ID of peer PE:             *peer-lsrid*

VPLS ID:                            *vpls-id*

SAII:                                   *saii*

TAII:                                   *taii*

VC type:                             *vc-type*

Label:                                 *label*

LDP status code:          *     status-code*

PW status code:            *    pw-status-code*

C-bit:                               *   c-Bit*

发送一个*message-type*消息，

消息内容如下：

·对端PE的LSR ID为*peer-lsrid*

·VPLS ID为*vpls-id*

·SAII为*saii*

·TAII为*taii*

·VC类型为*vc-type*

·标签为*label*

·LDP状态码为*status-code*

·PW状态码为*pw-status-code*

·是否携带控制字比特为*c-Bit*

表1-9 debugging mpls ldpvc error命令输出信息描述表

字段

描述

Received an invalid VSI event (*event-type*).

LDP收到一个非法的VSI事件*event-type*

Failed to add a peer because VSI doesn't exist.

LDP添加peer失败，因为VSI不存在

表1-10 debugging mpls ldpvc event命令输出信息描述表

字段

描述

Received an event (*event-type*) from L2VPN.

收到一个L2VPN事件*event-type*

Received a session event (*event-type*) from LDP.

收到一个LDP会话事件*event-type*

Notified L2VPN to add a PW. VSI index: *vsi-index*, link ID: *link-id*

通知L2VPN添加一条PW，PW所属的VSI索引为*vsi-index*，PW的link ID为*link-id*

Notified L2VPN to delete a PW. VSI index: *vsi-index*, link ID: *link-id*

通知L2VPN删除一条PW， PW所属的VSI索引为*vsi-index*，PW的link ID为*link-id*

【举例】

\# 打开MPLS LDP VC的错误调试信息开关。将L2VPN去使能，打印如下调试信息。

\<Sysname\> debugging mpls ldpvc error

\<Sysname\> system-view

Sysname undo l2vpn enable

Info: This command will delete L2VPN globally. Continue? [Y/N:y]

Info: L2VPN is deleting, please wait \....Finished!

\*Sep  5 08:39:18:619 2011 Sysname LDPVC/7/ERROR: -MDC=1; Failed to connect to L2VPN.

*// 和L2VPN进程连接失败*

\# 打开MPLS LDP VC的事件调试信息开关。在设备上创建一个VSI，配置信令协议为LDP，并在LDP信令视图下配置一条PW，设备上会打印如下调试信息。

\<Sysname\> debugging mpls ldpvc event

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling ldp

Sysname-vsi-vpn1-ldp peer 1.1.1.1 pw-id 100

\*Sep  5 08:41:34:541 2011 Sysname LDPVC/7/EVENT: -MDC=1; Received an event (8) from L2VPN.

\*Sep  5 08:41:34:541 2011 Sysname LDPVC/7/EVENT: -MDC=1; Notified L2VPN to add a PW. VSI index: 0xa, link ID: 8.

*// 从L2VPN收到Peer添加事件，事件类型为8。向L2VPN添加一条PW。该PW对应的VSI索引为0x0a，link ID为8。*

\# 打开用来通告PW标签的LDP消息调试信息开关。在一个三层以太网接口GigabitEthernet1/0/1下绑定已经创建的VSI，设备上打印如下调试信息。

\<Sysname\> debugging mpls ldpvc advertisement

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 xconnect vsi vpn1

\*Sep  5 08:48:37:706 2011 Sysname LDPVC/7/ADVER: -MDC=1; Sent a mapping message.

Message content:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSR ID of peer PE:            1.1.1.1

VC ID:                        100

VC type:                      4

Label:                        775253

Status code:                  0xFFFFFFFF

PW status code:               0x0

C-bit:                        0

*// 发送FEC 128方式的mapping消息*

\# 在设备的对端2.2.2.2上也进行同样的配置，则本端设备上会打印如下调试信息。

\*Sep  5 08:50:38:254 2011 Sysname LDPVC/7/ADVER: -MDC=1; Received a mapping message.

Message content:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSR ID of peer PE:            2.2.2.2

VC ID:                        100

VC type:                      4

Label:                        775121

Status code:                  0xFFFFFFFF

PW status code:               0x0

C-bit:                        0

*// 收到FEC 128方式的mapping消息*

\# 打开用来通告PW标签的LDP消息调试信息开关。在三层以太网接口GigabitEthernet1/0/1下绑定已经创建的auto-discovery类型的VSI，设备上打印如下调试信息。

\<Sysname\> debugging mpls ldpvc advertisement

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 xconnect vsi vpn1

\*Sep  5 08:48:37:706 2011 Sysname LDPVC/7/ADVER: -VD=1; Sent a mapping message.

Message content:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSR ID of peer PE:            2.2.2.9

VPLS ID:                      100:100

SAII:                         1010109

TAII:                         2020209

VC type:                      4

Label:                        775120

LDP status code:                  0xFFFFFFFF

PW status code:               0x0

C-bit:                        0

*// 发送FEC 129方式的mapping消息*

\# 在设备的对端2.2.2.9上也进行同样的配置，则本端设备上会打印如下调试信息。

\*Sep  5 08:50:38:254 2011 Sysname LDPVC/7/ADVER: -VD=1; Received a mapping message.

Message content:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSR ID of peer PE:            2.2.2.9

VPLS ID:                      100:100

SAII:                         2020209

TAII:                         1010109

VC type:                      4

Label:                        775120

LDP status code:                  0xFFFFFFFF

PW status code:               0x0

C-bit:                        0

*// 收到FEC 129方式的mapping消息*

**MPLS L2VPN \-- MPLS L2VPN调试命令 \-- debugging mpls bgpvc**

------------------------------------------------------------------------

【命令】

**[debugging mpls bgpvc **[{ **advertisement** \| **all** \| **error** \| **event** }]]

**[undo debugging mpls bgpvc**[ { **advertisement** \| **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advertisement**]：表示MPLS BGP VC的网络可达消息调试信息开关。

**[all**]：表示MPLS BGP VC的所有调试信息开关。

**[error**]：表示MPLS BGP VC的错误调试信息开关。

**[event**]：表示MPLS BGP VC的事件调试信息开关。

【描述】

**[debugging mpls bgpvc**]命令用来打开MPLS BGP VC的调试信息开关。**undo debugging mpls bgpvc**命令用来关闭MPLS BGP VC的调试信息开关。

缺省情况下，MPLS BGP VC调试信息开关处于关闭状态。

表1-11 debugging mpls bgpvc advertisement命令输出信息描述表

字段

描述

Received a label MP_REACH_NLRI:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nexthop:                       *nexthop*

RD:                               *rd*

Site ID:                         *site-id*

Label base:                  *label-base*

Label range:               * range*

Label offset:                * offset*

Route Target:               *rt*

MTU:                           * mtu*

Control flag:                 *flag*

Encaps type:               *EncapType*

收到一个带有标签块的BGP Update消息

消息内容如下：

·下一跳属性（即远端PE的地址）为*nexthop*

·RD为*rd*

·Site标识为*site-id*

·为该Site分配的标签块的初始标签值为*label-base*

·为该Site分配的标签块大小为*range*

·为该Site分配的标签块的偏移量为*offset*

·RT属性为*rt*

·MTU为*mtu*

·是否携带控制字标记为为*flag*

·封装类型为EncapType

Received a neighbor MP_REACH_NLRI:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nexthop:                       *nexthop*

VPLS ID:                      *vpls-id*

RD:                              * rd*

PE address:                 *pe-address*

Route Target:              * rt*

收到一个带有远端PE信息的BGP Update消息

消息内容如下：

·下一跳属性（即远端PE的地址）为*nexthop*

·VPLS ID为*vpls-id*

·RD为*rd*

·对端在VPLS实例内的标识为*pe-address*

·RT为*rt*

Sent a label MP_REACH_NLRI:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nexthop:                       

RD:                               *rd*

Site ID:                         *site-id*

Label base:                  *label-base*

Label range:               * range*

Label offset:                * offset*

Route Target:              *ert*

MTU:                           * mtu*

Control flag:                 *flag*

Encaps type:                *EncapType*

发送一个带有标签块的BGP Update消息

消息内容如下：

·RD为*rd*

·Site标识为*site-id*

·为该Site分配的标签块的初始标签值为*label-base*

·为该Site分配的标签块大小为*range*

·为该Site分配的标签块的偏移量为*offset*

·RT属性为*rt*

·MTU为*mtu*

·是否携带控制字标记为为*flag*

·封装类型为EncapType

Sent a neighbor MP_REACH_NLRI:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nexthop:                       

VPLS ID:                      *vpls-id*

RD:                              * rd*

PE address:                 *pe_address*

Route Target:             * ert*

发送一个带有远端PE信息的BGP Update消息

消息内容如下：

·VPLS ID为*vpls-id*

·RD为*rd*

·本端在VPLS实例内的标识为*pe-address*

·RT为*rt*

表1-12 debugging mpls bgpvc error命令输出信息描述表

字段

描述

Received an invalid VSI event (*event-type*).

BGP VC收到一个非法的VSI事件*event-type*

Failed to send an event.

向BGPVC线程队列写事件失败

The received PE-addr *pe-address* is the same as an existing remote PE-addr. The received RD is *rd*.

收到的PE_Addr地址*pe-address*和已经存在的某个远端PE_Addr相同，此次收到的RD为*rd*

The received PE-addr *pe-address* is the same as the local PE-addr. The received RD is *rd*.

收到的PE_Addr地址*pe-address*和本地配置的PE_Addr相同，此次收到的RD为*rd*

The received site ID *site-id* is the same as the ID of an existing remote site. The received RD is *rd.*

收到的site-id值*site-id*和已经存在的某个远端site-id相同，此次收到的RD为*rd*

The received site ID *site-id* is the same as the ID of the local site. The received RD is *rd*.

收到的site-id值 *site-id*和本地配置的site-id相同，此次收到的RD为*rd*

表1-13 debugging mpls bgpvc event命令输出信息描述表

字段

描述

Received an event (*event-type*) from L2VPN.

收到一个L2VPN事件*event-type*

Received an event (*event-type*) from BGP.

收到一个BGP事件*event-type*

Sent an event (*event-type*) to BGP.

向BGP发送事件*event-type*

Notified L2VPN to add a PW. VSI index: *vsi-index*, link ID: *link-id*

通知L2VPN添加一条BGP PW，PW所属的VSI索引为*vsi-index*，PW的link ID为*link-id*

Notified L2VPN to delete a PW. VSI index: *vsi-index*, link ID: *link-id*

通知L2VPN删除一条BGP PW，PW所属的VSI索引为*vsi-index*，PW的link ID为*link-id*

Notified L2VPN to add an auto-discovered peer. VSI index: *vsi-index*, peer: *peer-address*

通知L2VPN添加一个自动发现peer，该peer所属的VSI索引为*vsi-index*，地址为*peer-address*

Notified L2VPN to delete an auto-discovered peer. VSI index: *vsi-index*, peer: *peer-address*

通知L2VPN删除一个自动发现peer，该peer所属的VSI索引为*vsi-index*，地址为*peer-address*

【举例】

\# 打开MPLS BGP VC的错误调试信息开关。在设备上创建一个VSI，配置auto-discovery，并配置信令协议为BGP，本端Site标识为10。然后，在对端设备上配置两个VSI：两个VSI的RD不同，RT相同，使用的信令协议为BGP，Site标识均为20。两端均在接口上绑定VSI后，本端设备会打印如下信息。

\<Sysname\> debugging mpls bgpvc error

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 auto-discovery bgp

Sysname-vsi-vpn1-auto route-distinguisher 100:1

Sysname-vsi-vpn1-auto vpn-target 1:1

Sysname-vsi-vpn1-auto signaling-protocol bgp

Sysname-vsi-vpn1-auto-bgp site 10 range 30

Sysname-vsi-vpn1-auto-bgp interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 xconnect vsi vpn1

\*Nov 24 09:15:15:046 2012 Sysname BGPVC/7/ERROR: -MDC=1; The received site ID 20 is the same as the ID of an existing remote site. The received RD is 100:2.

\# 打开MPLS BGP VC的事件调试信息开关。在设备上创建一个VSI，配置auto-discovery，并配置信令协议为BGP，本端Site标识为10。在对端设备上也进行相应配置。两端均在接口上绑定VSI后，设备上会打印如下调试信息。

\<Sysname\> debugging mpls bgpvc event

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 auto-discovery bgp

Sysname-vsi-vpn1-auto route-distinguisher 100:1

Sysname-vsi-vpn1-auto vpn-target 1:1

Sysname-vsi-vpn1-auto signaling-protocol bgp

Sysname-vsi-vpn1-auto-bgp site 10 range 30

Sysname-vsi-vpn1-auto-bgp interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 xconnect vsi vpn1

\*Nov 24 09:27:54:334 2012 Sysname BGPVC/7/EVENT: -MDC=1; Notified L2VPN to add a PW. VSI index: 0x0, link ID: 27.

*// 通知L2VPN添加一条BGP PW。该PW对应的VSI索引为0x0，link ID为27。*

\# 打开MPLS BGP VC的事件调试信息开关。在设备上创建一个VSI，配置auto-discovery，并配置信令协议为LDP，VPLS ID为100:100。对端设备上也进行相应的配置。两端均在接口上绑定VSI后，设备上会打印如下调试信息。

\<Sysname\> debugging mpls bgpvc event

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 auto-discovery bgp

Sysname-vsi-vpn1-auto route-distinguisher 100:1

Sysname-vsi-vpn1-auto vpn-target 1:1

Sysname-vsi-vpn1-auto signaling-protocol ldp

Sysname-vsi-vpn1-auto-bgp vpls-id 100:100

Sysname-vsi-vpn1-auto-bgp interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 xconnect vsi vpn1

\*Nov 24 09:36:24:622 2012 Sysname BGPVC/7/EVENT: -MDC=1; Notified L2VPN to add a peer. VSI index: 0x1, peer: 2.2.2.9.

*// 通知L2VPN添加一个自动发现peer。该peer对应的VSI索引为0x1，地址为2.2.2.9。*

\# 打开MPLS BGP VC的网络可达消息调试信息开关。在一个三层以太网接口GigabitEthernet1/0/1下绑定已经创建的auto-discovery类型VSI后，设备上打印如下调试信息。

\<Sysname\> debugging mpls ldpvc advertisement

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 xconnect vsi vpn1

\*Nov 24 09:31:42:182 2012 PE1 BGPVC/7/ADVER: -MDC=1; Sent a label MP_REACH_NLRI:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nexthop:

RD:                           100:1

Site ID:                      10

Label Base:                   775158

Label Range:                  30

Label Offset:                 0

ERT:                          3:3 1:1

MTU:                          1500

Control Flag:                 0

EncapType:                    19

*// 发送一个带有标签块的BGP Update消息。*

\*Nov 24 09:32:18:193 2012 PE1 BGPVC/7/ADVER: -MDC=1; Received a label MP_REACH_NLRI:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nexthop:                      2.2.2.9

RD:                           100:2

Site ID:                      20

Label Base:                   775128

Label Range:                  30

Label Offset:                 0

ERT:                          1:1 2:2

MTU:                          1500

Control Flag:                 0

EncapType:                    19

*// 收到一个带有标签块的BGP Update消息。*

\# 打开MPLS BGP VC的网络可达消息调试信息开关。创建auto-discovery类型的VSI，并配置信令协议为LDP，在接口上绑定该VSI后，设备上打印如下调试信息。

\<Sysname\> debugging mpls ldpvc advertisement

\*Nov 24 09:38:26:744 2012 PE1 BGPVC/7/ADVER: -MDC=1; Sent a neighbor MP_REACH_NLRI:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nexthop:

VPLS-ID:                      100:100

RD:                           101:1

PE_address:                   1.1.1.9

ERT:                          11:11

*// 发送一个带有远端PE信息的BGP Update消息。*

\*Nov 24 09:38:58:732 2012 PE1 BGPVC/7/ADVER: -MDC=1; Received a neighbor MP_REACH_NLRI:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Nexthop:                      2.2.2.9

VPLS-ID:                      100:100

RD:                           102:1

PE_address:                   2.2.2.9

ERT:                          11:11 22:22

*// 收到一个带有远端PE信息的BGP Update消息。*
