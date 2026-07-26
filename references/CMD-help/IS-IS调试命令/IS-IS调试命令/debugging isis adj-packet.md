
**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis adj-packet**

------------------------------------------------------------------------

【命令】

**[debugging**[ **isis** **adj-packet** [ **receive** \| **send** ]  **verbose**   *process-id* ]]

**[undo**[ **debugging** **adj-packet** [ **receive** \| **send** ]  **verbose**   *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：打开Hello报文接收调试功能。

**[send**]：打开Hello报文发送调试功能。

**[verbose**]：打开Hello报文详细信息调试功能。

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【描述】

**[debugging isis adj-packet**]命令用来打开IS-IS Hello报文调试信息开关。**undo debugging isis adj-packet**命令用来关闭IS-IS Hello报文调试信息开关。

缺省情况下，IS-IS Hello报文调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的Hello报文调试信息开关。

表1-1 debugging isis adj-packet命令输出信息描述表

字段

描述

ISIS-*process-id*-ADJ: System is under disable state, IIH discarded.

收到Hello报文时，IS-IS进程处于disable状态，丢弃报文

·*process-id*：IS-IS进程号

ISIS*-process-id*-ADJ: Circuit (*circuitName*)\'s state is not up, IIH discarded.

收到Hello报文时，接口处于非up状态，丢弃报文

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

ISIS-*process-id*-ADJ: Circuit (*circuitName*) is under disable state, IIH discarded.

收到Hello报文时，接口处于silence状态，丢弃报文

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

ISIS-*process-id*-ADJ: Receive a packet from self, IIH discarded.

收到了自己发送的Hello报文，丢弃报文

·*process-id*：IS-IS进程号

ISIS-*process-id*-ADJ: Receive a invalid packet, IIH discarded.

收到了被截断或报文长度与实际长度不一致的Hello报文，丢弃报文

·*process-id*：IS-IS进程号

ISIS-*process-id*-ADJ: Receive a invalid packet, has the same SystemId, IIH discarded.

收到的Hello报文携带的System ID和本系统的相同，丢弃报文

·*process-id*：IS-IS进程号

ISIS-*process-id*-ADJ: Receive a *helloType* packet from (*systemId*) on circuit (*circuitName*).

接收到Hello报文

·*process-id*：IS-IS进程号

·*helloType*：取值为LAN L1、LAN L2、P2P

·*systemId*：报文携带的System ID

·*circuitName*：接口名称

ISIS-*process-id*-ADJ: IIH PDU type (*type*) with circuit (*circuitName*) mismatch.

Hello报文Level类型与接口配置不匹配

·*process-id*：IS-IS进程号

·*type*：取值为Level-1或Level-2

·*circuitName*：接口名称

ISIS-*process-id*-ADJ: IIH protocol support with circuit (*circuitName*) mismatch.

Hello报文携带的协议支持信息与本系统不匹配

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

ISIS-*process-id*-ADJ: IIH IP address with circuit (*circuitName*) mismatch.

Hello报文携带的IP地址与本系统不在同一网段或与本系统IP地址相同

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

ISIS-*process-id*-ADJ: IIH area address with the local system mismatch.

Hello报文携带的区域地址与本系统不匹配

·*process-id*：IS-IS进程号

ISIS-*process-id*-ADJ: IIH has the same SNPA with a NBR, but different SystemId. The NBR will be down.

收到的Hello报文，携带的SNPA与本系统已维护的邻居相同，但System ID不同，本系统维护的邻居down

·*process-id*：IS-IS进程号

ISIS-*process-id*-ADJ: IIH has the same SystemId with a NBR, but different SNPA. The IIH will be discarded.

收到的Hello报文，携带的System ID与本系统已维护的邻居相同，但SNPA不同，丢弃报文

·*process-id*：IS-IS进程号

ISIS- *process-id* -ADJ: IIH has the same LinkLocal address with circuit(*circuitName*).

Hello报文携带的IPv6地址与接收接口的IPv6地址相同。

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

ISIS- *process-id* -ADJ: IIH circuit(*circuitName*) contains No usable Ip addresses at all. IIH Ignored.

设备之间即不能建立IPv4邻居也不能建立IPv6邻居。

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

ISIS- *process-id* -ADJ: Rxed *type* can not pass authentication on circuit(*circuitName*). IIH Ignored

Hello报文没有通过认证

·*process-id*：IS-IS进程号

·*type*：LAN L1、LAN L2、P2P

·*circuitName*：接口名称

ISIS-*process-id*-ADJ: *type* NBR (*systemId*) two way pass.

邻居2-way检查成功

·*process-id*：IS-IS进程号

·*type*：取值为Level-1或Level-2

·*systemId*：邻居的System ID

ISIS-*process-id*-ADJ: *type* NBR (*systemId*) two way fail.

邻居2-way检查失败

·*process-id*：IS-IS进程号

·*type*：取值为Level-1或Level-2

·*systemId*：邻居的System ID

ISIS-*process-id*-ADJ:DIS type *type*, on *circuitName*, old DIS: *sourceId1*, new DIS: *sourceId2*.

DIS选举结果

·*process-id*：IS-IS进程号

·*type*：取值为Level-1或Level-2

·*circuitName*：接口名称

·*sourceId1*：原DIS-ID，为空，则原DIS不存在

·*sourceId2*：新DIS-ID，为空，则新DIS不存在

ISIS-*process-id*-ADJ: Send a *helloType* packet on circuit (*circuitName*)

发送Hello报文

·*process-id*：IS-IS进程号

·*helloType*：Hello报文类型，取值为LAN L1、LAN L2、P2P

·*circuitName*：接口名称

ISIS- *process-id* -ADJ: Small-Hello is enabled on circuit(*circuitName*)

接口使能Small-Hello功能。

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

ISIS- *process-id* -ADJ: The circuit(*circuitName*) is silent.IIH not sent.

接口状态为silent，接口不发送Hello报文。

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

ISIS- *process-id* -ADJ: The Extended circuit ID of IIH mismatch. IIH ignored.

扩展接口ID不匹配，忽略此IIH报文

·*process-id*：IS-IS进程号

ISIS- *process-id* -ADJ: Circuit(*circuitName*) is MPLS TE Tunnel interface, IIH discarded.

接收接口是MPLS TE隧道接口，忽略此IIH报文

·*process-id*：IS-IS进程号

·*circuitName*：接口名称

【举例】

\# Router A与Router B相连，在Router A上创建IS-IS进程，SystemID为3333.3333. 3333、路由器类型为**level-1-2**，并在GigabitEthernet1/0/2上使能IS-IS功能，接口的IP地址为3.3.3.166/24；在Router B上创建IS-IS进程，SystemID为FFFF.FFFF.FFFF、路由器类型为**level-1-2**，并在GigabitEthernet1/0/1使能IS-IS功能，接口的IP地址为3.3.3.89/24；Router A与Router B在同一个区域49。在Router A上打开IS-IS Hello报文调试信息开关。

\<RouterA\> debugging isis adj-packet

\*Apr  4 18:47:08:383 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: Send a Lan L2 Hello packet on circuit(GigabitEthernet1/0/2)

\*Apr  4 18:47:08:384 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: Send a Lan L1 Hello packet on circuit(GigabitEthernet1/0/2)

*// 在GigabitEthernet1/0/2上发送L1和L2类型的Hello报文*

\*Apr  4 18:47:08:385 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: Receive a Lan L2 Hello packet from(ffff.ffff.ffff) on circuit(GigabitEthernet1/0/2)

\*Apr  4 18:47:08:385 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: Level-2 NBR(ffff.ffff.ffff) two way pass.

\*Apr  4 18:47:08:385 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: Receive a Lan L1 Hello packet from(ffff.ffff.ffff) on circuit(GigabitEthernet1/0/2)

\*Apr  4 18:47:08:385 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: Level-1 NBR(ffff.ffff.ffff) two way pass.

*// 在GigabitEthernet1/0/2上接收L1和L2类型的Hello报文，对端SystemID为：FFFF.FFFF.FFFF，2-way检查通过，建立了邻居关系*

\*Apr  4 18:47:08:493 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: Send a Lan L1 Hello packet on circuit(GigabitEthernet1/0/2)

\*Apr  4 18:47:08:493 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: Send a Lan L2 Hello packet on circuit(GigabitEthernet1/0/2)

\*Apr  4 18:47:08:493 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: DIS type Level-1, on GigabitEthernet1/0/2, old DIS:, new DIS:3333.3333.3333.01.

\*Apr  4 18:47:08:493 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ADJ: DIS type Level-2, on GigabitEthernet1/0/2, old DIS:, new DIS:3333.3333.3333.01.

*// 在GigabitEthernet1/0/2上进行了DIS选举，在L1、L2上分别选出了DIS*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis all**

------------------------------------------------------------------------

【命令】

**[debuging isis all** [ *process-id* ]]

**[undo debuging isis all** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【描述】

**[debuging isis all**]命令用来打开IS-IS所有的调试信息开关。**undo debugging isis all**命令用来关闭IS-IS所有的调试信息开关。

缺省情况下，IS-IS所有的调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的调试信息开关。

【举例】

\# 打开IS-IS进程1所有的调试信息开关。

\<RouterA\> debugging isis all 1

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis bfd-event**

------------------------------------------------------------------------

【命令】

**[debugging isis bfd-event ** *process-id* ]

**[undo debugging isis bfd-event** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，范围为1～65535。

【描述】

**[debugging isis bfd-event**]命令用来打开IS-IS BFD事件调试信息开关。**undo debugging isis bfd-event**命令用来关闭IS-IS BFD事件调试信息开关。

缺省情况下，IS-IS BFD事件调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的BFD事件调试信息开关。

表1-1 debugging isis bfd-event命令输出信息描述表

字段

描述

ISIS- process-id -BFD: Success to send Sessiontype session Msg. DstIPAddr: XX.XX.XX.XX SrcIPAddr:

 YY.YY.YY.YY, NeighborType: leveltype

IS-IS协议通知BFD模块的BFD会话消息

·*process-id*：IS-IS进程号

·*Sessiontype*：消息类型

·*Sessiontype*：消息类型。值可以为：create，创建会话；delete，删除会话；disable，去使能会话

·DstIPAddr：会话目的IP地址

·SrcIPAddr：会话源IP地址

·NeighborType：邻居类型

·*leveltype*：级别类型。值可以为：Level-1，广播网Level-1邻居；Level-2，广播网Level-2邻居；P2P，P2P邻居

【举例】

\# Router A与Router B相连，分别在Router A和Router B上配置IS-IS功能。在Router A上打开IS-IS BFD事件调试信息开关。

\<Sysname\> debugging isis bfd-event

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 isis bfd enable

\*Jan  2 02:16:46:688 2000 Sysname ISIS/7/ISISDBG:

ISIS-1-BFD: Success to send create session Msg. DstIPAddr: 12.12.12.1, SrcIPAddr: 12.12.12.2, NeighborType: Level-1

*[// IS-IS*]*协议通知BFD模块创建BFD会话，会话目的IP为12.12.12.1，会话源地址为12.12.12.2，邻居类型为广播网Level-1*

Sysname-Vlan-interface100 undo isis bfd enable

\*Jan  2 02:17:14:968 2000 Sysname ISIS/7/ISISDBG:

ISIS-1-BFD: Success to send disable session Msg. DstIPAddr: 12.12.12.1, SrcIPAddr: 12.12.12.2, NeighborType: Level-1

*[// IS-IS*]*协议通知BFD模块去使能BFD会话，会话目的IP为12.12.12.1，会话源地址为12.12.12.2，邻居类型为广播网Level-1*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis error**

------------------------------------------------------------------------

【命令】

**[debuging isis error** [ *process-id* ]]

**[undo debuging isis error** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【描述】

**[debuging isis error**]命令用来打开IS-IS错误调试信息开关。**undo debugging isis error**命令用来关闭IS-IS错误调试信息开关。

缺省情况下，IS-IS错误调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的错误调试信息开关。

表1-2 debugging isis error命令输出信息描述表

字段

描述

ISIS-*procId*-ERR: LAN ADJ number has arrived max.

接口邻居数目达到最大值

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH contains invalid protocol descriminator. IIH discarded.

接收到的IIH报文协议鉴别字段错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH contains invalid version. IIH discarded.

接收到的IIH报文协议版本错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH contains invalid protocol ID. IIH discarded.

接收到的IIH报文协议ID错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH contains invalid system ID length. IIH discarded.

接收到的IIH报文system ID错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH contains invalid max area address number. IIH discarded.

接收到的IIH报文区域地址最大数错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH contains invalid packet Type. IIH discarded.

接收到的IIH报文类型错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH contains invalid head length. IIH discarded.

接收到的IIH报文头长度错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR:  Receive a LAN IIH contains invalid circuit Type. IIH discarded.

接收到的IIH报文接口类型错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR:  Receive a LAN IIH contains invalid priority. IIH discarded.

接收到的IIH报文dis优先级错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH neighbor TLV decode error. IIH discarded.

接收到的IIH报文邻居TLV解码错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR:  Receive a LAN IIH area address TLV decode error. IIH discarded.

接收到的IIH报文区域地址TLV解码错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH IP address TLV decode error. IIH discarded.

接收到的IIH报文IP地址TLV解码错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Receive a LAN IIH protocol support TLV decode error. IIH discarded.

接收到的IIH报文协议支持TLV解码错误，不处理接收到的Hello报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR:  System\'s state is disable.

进程处于disable状态

·*procId*：IS-IS进程号

ISIS-*procId*-ERR:  Socket ID leave muti-cast group failed.

将接口从组播组中删除失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: *adjLevel* Hello timer start failed.

Hello定时器创建失败

·*procId*：IS-IS进程号

·*adjLevel*：hello定时器的类型

ISIS-*procId*-ERR: Socket ID join mutiple broadcast group failed.

将接口加入到组播组中失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: UPDT Module NBR TLV Modify Failed.

邻居TLV更新失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Notify UPDT Module LSP Change Failed.

LSP重新生成失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: DEC Module ISPF Link Update Failed.

邻接链路更新失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Hold timer start failed.

邻居维持定时器创建失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Get SNPA address failed.

获取snpa地址失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Get circuit(*circuitName*)\'s priority failed.

获取接口DIS优先级失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Get system\'s area address failed.

获取接口系统区域地址失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: The circuit\'s MTU is too less.

接口mtu大小放不下当前TLV

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Get circuit(*circuitName*)\'s IP address failed.

获取接口IP地址失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: The circuit\'s MTU is too less to encode LAN IIH.

接口mtu大小放不下IIH报文

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Get circuit(*circuitName*)\'s MTU failed.

获取接口MTU失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Hello packet send failed on circuit(*circuitName*).

接口IIH报文发送失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Hello timer create failed on circuit(*circuitName*).

接口上的hello定时器创建失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error modifying the attributes of the route entry in RM.

更新路由属性失败

·*procId*：IS-IS进程号

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Error adding a new route entry in RM.

添加新路由失败

·*procId*：IS-IS进程号

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Error deleting a route entry in RM.

删除路由失败

·*procId*：IS-IS进程号

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*) Error getting *level* nexthop information for *systemId* from ISPF module.

获取路由发布源的下一条失败

·*procId*：IS-IS进程号

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

·*systemId*：系统ID

ISIS-*procId*-ERR: Error building nexthop list for route *ipAddr*/*mask*.

创建下一条链表失败

·*procId*：IS-IS进程号

·*ipAddr*：接口IP地址

·*mask*：IP地址掩码

ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error processing ipv4 route entry.

路由计算出错

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error adding the route source entry from the source list.

添加路由发布源失败

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error finding the routeEntry structure for address *ipAddr*/*mask*.

查找路由信息失败

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

·*ipAddr*：接口IP地址

·*mask*：IP地址掩码

ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Error deleting the route source entry from the source list.

删除路由发布源失败

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*)(*level*) Error modifying the route source entry in the source list.

更新路由发布源失败

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Add route to URT fails.

路由已满，添加路由失败

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*)(*level*) Modify route in URT failure.

更新路由失败

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: (MT*mtId*)(*level*)  Del route form URT fails.

删除路由失败

·*mtId*：拓扑号

·*level*：系统类型可为L1或L2

ISIS-*procId*-ERR: Resetting the system

进程正在reset状态

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: MTU Size Exceeds Max PDU Size *mtuSize*, Setting it to Max PDU Size.

接口mtu超过最大值

·*procId*：IS-IS进程号

·*mtuSize*：接口MTU大小

ISIS-*procId*-ERR: Processing the circuit MTU change event fails

接口mtu变化处理失败

·*procId*：IS-IS进程号

·*mtuSize*：接口MTU大小

ISIS-*procId*-ERR: Processing the physical circuit board insert error

接口板插入处理出错

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Processing the physical circuit delete error on circuit :*circuitName*

处理物理接口删除出错

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Processing the physical circuit UP \--\> Down error on circuit : *circuitName*

物理接口Up到down的处理出错

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Processing the physical circuit config error on circuit :  *circuitName*

物理接口配置的处理出错

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Processing board remove failed on circuit : *circuitName*

物理接口板拔出的处理出错

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Invalid phase *enDisablePhase*, ignore event.

进程不在reset的阶段

·*procId*：IS-IS进程号

·*enDisablePhase*：进程所处的状态阶段

ISIS-*procId*-ERR: The event type and disable phase mismatch.

进程的reset状态和阶段不一致

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Failed to add neighbor into *lspLevel* LSPs

向lsp中添加邻居信息失败

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型。可为Level-1或Level-2

ISIS-*procId*-ERR: Failed to add address *ipAddr*/*mask* into *lspleve* LSPs

向lsp中添加IP地址失败

·*ipAddr*：接口IP地址

·*mask*：IP地址掩码

·*lspLevel*：LSP类型。可为Level-1或Level-2

ISIS-*procId*-ERR: Failed to start csnp timer on circuit *circuitName*

接口CSNP定时器创建失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Failed to start psnp timer on circuit *circuitName*

接口PSNP定时器创建失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Failed to start flood timer on the circuit *circuitName*

接口lsp泛洪定时器创建失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Failed to stop lsp flood timer on circuit *circuitName*

关闭接口lsp泛洪定时器失败

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-ERR: Failed to stop *lspLevel* timer on circuit *circuitName*

关闭接口lsp生成定时器失败

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型。可为Level-1或Level-2

·*circuitName*：接口名

ISIS-*procId*-ERR: Parsed neighbor\'s metric(*systemId*) more than max metric value

接口邻居metric值大于允许的最大值

·*procId*：IS-IS进程号

·*systemId*：系统ID

ISIS-*procId*-ERR: Skip ip address prefix for mismatching with mask

接口IP地址前缀和掩码不匹配

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Skip the prefix for invalid ip prefix

IP地址前缀不正确

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型。可为Level-1或Level-2

ISIS-*procId*-ERR: Internal ip reach Tlv with external bit set encountered

内部可达IP TLV包含metric类型为外部的位

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Area addr tlv in non-zero fragment, skip this area addr tlv

非零分片中存在区域地址

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Area addr tlv in pseudo node lsp, skip this area addr tlv

伪节点LSP中存在区域地址

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Lsp info update failed

LSDB中的LSP信息更新失败

·*procId*：IS-IS进程号

ISIS-*procId*-ERR: Lsp insert failed

向lsp中添加邻居信息失败

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型。可为Level-1或Level-2

ISIS-*processId*-ERR: Lsp\'s seq number is 0

接收到的LSP报文的序列号为0，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Illegal is-type in level-1 lsp

Level-1 LSP报文的IS-TYPE字段非法，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Check sum is zero

LSP报文的校验和为0，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Check sum error

LSP报文的校验和错误，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Support protocol mismatch

LSP报文携带的协议支持和本地的不匹配，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Lsp with too long area addr

LSP报文中携带的区域地址长度超过最大区域地址长度，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Lsp with wrong area addr length

LSP报文中携带的区域地址长度错误，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Lsp with invalid area addr

LSP报文中携带的区域地址长度不合法，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Wrongly formatted interface ip address tlv in lsp

LSP报文中携带的接口地址TLV格式错误，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Wrongly formatted nbr tlv in lsp

LSP报文中携带的邻居TLV格式错误，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: IP Reachablity tlv occur in pseudonode lsp

伪节点LSP报文中携带的IP可达TLV，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Badly formatted ip reachablity tlv in lsp

LSP报文中携带的IP可达TLV格式错误，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Bad tlv len in the received lsp

LSP报文中携带的TLV长度错误，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Pdu size(*pduSize*) which is greater than receive buf size(*reveiveBufSize*)

LSP/SNP报文长度大于接收缓冲区大小，丢弃报文

·*processId*：IS-IS进程ID

·pduSize：LSP/SNP报文长度

·reveiveBufSize：接收缓冲区大小

ISIS-*processId*-ERR: Pdu size(*pduSize*) which is less than common pdu header size(*pduCommonHeaderSize*)

LSP/SNP报文长度小于公共报文头大小，丢弃报文

·*processId*：IS-IS进程ID

·*pduSize*：LSP/SNP报文长度

·*pduCommonHeaderSize*：公共报文头大小

ISIS-*processId*-ERR: Pdu size(*pduSize*) which is less than fixed pdu header size(*pduFixedHeaderSize*)

LSP/SNP报文长度小于固定报文头大小，丢弃报文

·*processId*：IS-IS进程ID

·pduSize：LSP/SNP报文长度

·pduFixedHeaderSize：固定报文头大小

ISIS-*processId*-ERR: Pdu length mismatch: recvLen = *recvLen*, encodeLen = *encodeLen*

LSP/SNP报文长度和报文中的长度字段不相等，丢弃报文

·*processId*：IS-IS进程ID

·*recvLen*：LSP/SNP报文长度

·*encodeLen*：报文中的长度字段

ISIS-*processId*-ERR: Lsp or snp pdu common header error

LSP/SNP公共报文头错误，丢弃报文

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Try to send pdu on loopback circuit

企图在环回接口上发送LSP，不发送

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Send pdu error, SENDTO return is *SentDataLen*, usBufLen is *bufDataLen*

LSP/SNP发送失败

·*processId*：IS-IS进程ID

·*SentDataLen*：发送出去的数据长度

·*bufDataLen*：需要发送的数据长度

ISIS-*processId*-ERR: Lsp size(*lspSize*) is larger than circuit mtu(*circuitMtu*)

LSP报文大小大于发送接口的MTU

·*processId*：IS-IS进程ID

·*lspSize*：LSP报文大小

·*circuitMtu*：发送接口的MTU

ISIS-*processId*-ERR: Wrong lsp entry tlv length(*lspEntryTlvLen*) in snp

SNP报文中的LSP ENTRY TLV长度错误

·*processId*：IS-IS进程ID

·*lspEntryTlvLen*：LSP ENTRY TLV长度

ISIS-*processId*-ERR: Snp contain too much lsp entry

SNP报文中的LSP ENTRY个数多过

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Invalid lsp id reported in snp

SNP报文中的LSP ENTRY的LSP-ID错误

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Failed to install lsp with seq number zero

安装序列号为0的LSP失败

·*processId*：IS-IS进程ID

ISIS-*processId*-ERR: Failed to add level-*Level* area address *areaAdress*

添加区域地址失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*areaAdress*：区域地址

ISIS-*processId*-ERR: Failed to delete level-*Level* area address *areaAdress*

删除区域地址失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*areaAdress*：区域地址

ISIS-*processId*-ERR: Failed to add level- *Level* protocol support *protocolSupport*

添加协议支持失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*protocolSupport*：协议支持

ISIS-*processId*-ERR: Failed to delete level- *Level* protocol support *protocolSupport*

删除协议支持失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*protocolSupport*：协议支持

ISIS-*processId*-ERR: Failed to add level-*Level* neighbour: System *SystemId* =\> Neighbour *nbrSourceId*

添加邻居失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*SystemId*：System ID

·*nbrSourceId*：邻居的SourceID

ISIS-*processId*-ERR: Failed to delete level-*Level* neighbour: System *SystemId* =\> Neighbour *nbrSourceId*

删除邻居失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*SystemId*：System ID

·*nbrSourceId*：邻居的SourceID

ISIS-*processId*-ERR: Failed to modify level-*Level* neighbour: System *SystemId* =\> Neighbour *nbrSourceId*

修改邻居失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*SystemId*：System ID

·*nbrSourceId*：邻居的SourceID

ISIS-*processId*-ERR: Failed to add level-*Level* Interface IP address: *ipAddress*/*mask*

添加接口IP地址失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*ipAddress*：接口IP地址

·*mask*：地址掩码

ISIS-*processId*-ERR: Failed to delete level-*Level* Interface IP address: *ipAddress*/*mask*

删除接口IP地址失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*ipAddress*：接口IP地址

·*mask*：地址掩码

ISIS-*processId*-ERR: Failed to add level-*Level* pseudo neighbour: Pseudo *pseudoNodeSourceId* =\> Neighbour *nbrSystemId*

添加伪节点邻居失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*pseudoNodeSourceId*：伪节点Source ID

·*nbrSystemId*：邻居System ID

ISIS-*processId*-ERR: Failed to delete level-*Level* pseudo neighbour: Pseudo *pseudoNodeSourceId* =\> Neighbour *nbrSystemId*

删除伪节点邻居失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*pseudoNodeSourceId*：伪节点Source ID

·*nbrSystemId*：邻居System ID

ISIS-*processId*-ERR: Failed to add level-*Level* IP prefix: *ipPrefix*/*mask*

添加IP前缀失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*ipPrefix*：IP前缀

·*mask*：前缀掩码

ISIS-*processId*-ERR: Failed to delete level-*Level* IP prefix: *ipPrefix* / *mask*

删除IP前缀失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*ipPrefix*：IP前缀

·*mask*：前缀掩码

ISIS-*processId*-ERR: Failed to modify level-*Level* IP prefix: *ipPrefix* / *mask*

修改IP前缀失败

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*ipPrefix*：IP前缀

·*mask*：前缀掩码

ISIS-*processId*-ERR: Level-*Level*, receive wrong extended nerghbor SubTlv, Type=*type*, Length=*len*

接收到错误的扩展邻居sub-tlv

·*processId*：IS-IS进程ID

·*Level*：Level-1/Level-2

·*type*：sub-tlv类型值

·*len*：sub-tlv长度

【举例】

\# Router A与Router B相连，在Router A上创建IS-IS进程，路由器类型为**level-1**，并在GigabitEthernet1/0/2上使能IS-IS功能，接口的IP地址为1.1.1.166/24；在Router B上创建IS-IS进程，SystemID为FFFF.FFFF.FFFF、路由器类型为**level-1**，并在GigabitEthernet1/0/1使能IS-IS功能，接口的IP地址为1.1.1.2/24；Router A与Router B在同一个区域49。在Router A上打开IS-IS错误调试信息开关。

\<RouterA\> debugging isis error

\*Apr  8 21:47:12:360 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ERR: Receive a LAN IIH contains invalid protocol discriminator. IIH discarded.

*// 在GigabitEthernet1/0/2上收到协议鉴别号不是0x83的Hello报文*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis event**

------------------------------------------------------------------------

【命令】

**[debuging isis event** [ *process-id* ]]

**[undo debuging isis event** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【描述】

**[debuging isis event**]命令用来打开IS-IS事件调试信息开关。**undo debugging isis event**命令用来关闭IS-IS事件调试信息开关。

缺省情况下，IS-IS事件调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的事件调试信息开关。

表1-3 debugging isis event命令输出信息描述表

字段

描述

ISIS-*procId*-EVT: Rib smooth start.

数据平滑开始

·*procId*：IS-IS进程号

ISIS-*procId*-EVT: Rt smooth end.

数据平滑结束

·*procId*：IS-IS进程号

ISIS-*procId*-EVT: LSP MTU change from *oldLspBuf* to *newLspBuf*, notify UPDT MTU change.

进程lsp缓冲区的大小改变

·*procId*：IS-IS进程号

·*oldLspBuf*：lsp缓冲区之前的大小

·*newLspBuf*：新的lsp缓冲区的大小

ISIS-*procId*-EVT: Processing the physical circuit board Insert event

处理接口板插入事件

·*procId*：IS-IS进程号

ISIS-*procId*-EVT: Processing the physical circuit add event on circuit : *circuitName*

物理接口添加事件

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-EVT: Processing the physical circuit delete event on circuit : *circuitName*

物理接口 删除事件

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-EVT: Processing Down \--\> Up event on circuit *circuitName*

接口down到Up事件

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-EVT: Processing Up \--\> Down event on circuit  *circuitName*

接口Up到down事件

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-EVT: Processing the physical circuit Param change event on circuit *circuitName*

接口配置改变处理事件

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-EVT: Processing board remove event on circuit  *circuitName*

接口板拔出事件

·*procId*：IS-IS进程号

·*circuitName*：接口名

ISIS-*procId*-EVT: Processing the logical address add event  : *ipAddr*

逻辑接口添加处理事件

·*procId*：IS-IS进程号

·*ipAddr*：IP地址

ISIS-*procId*-EVT: Processing the logical address delete event  : *ipAddr*

逻辑接口删除处理事件

·*procId*：IS-IS进程号

·*ipAddr*：IP地址

ISIS-*procId*-EVT: Reset processing with backinfo: module *moudleId*, event *eventId*, phase *phaseId*.

进程Reset的阶段信息

·*procId*：IS-IS进程号

·*moudleId*：模块ID

·*eventid*：触发reset的事件ID

·*phaseId*：reset所处的阶段

ISIS-*procId*-EVT: Reset change into phase *phaseId*

进程Reset进入下一个阶段

·*procId*：IS-IS进程号

·*moudleId*：模块ID

·*eventid*：触发reset的事件ID

·*phaseId*：reset所处的阶段

ISIS-*procId*-EVT: Reset processing receive event *eventId.*

进程收到reset触发事件

·*procId*：IS-IS进程号

·*eventid*：触发reset的事件ID

ISIS-*procId*-EVT: Reset begin

进程reset开始

·*procId*：IS-IS进程号

ISIS-*procId*-EVT: Reset finished, process with reset reason *eventId*

进程reset结束事件

·*procId*：IS-IS进程号

·*eventid*：触发reset的事件ID

ISIS-*procId*-EVT: Updt receive lsp change event.

UPDT模块收到LSP报文改变事件

·*procId*：IS-IS进程号

ISIS-*procId*-EVT:Updt receive interface : *circuitName* state change to state(*eventType*).

UPDT模块收到接口状态改变事件

·*procId*：IS-IS进程号

·*circuitName*：接口名

·*eventType*：事件类型

ISIS-*procId*-EVT:IS-IS ipv6 state change, inform DEC update ipv6 prefix.

UPDT模块通知路由模块更新IPv6前缀

·*procId*：IS-IS进程号

ISIS-*procId*-EVT:Updt receive authen change event.

UPDT模块收到认证改变事件

·*procId*：IS-IS进程号

ISIS-*procId*-EVT: Updt receive *lsplevel* fast flood event

UPDT模块收到fast-flood快速扩散事件

·*procId*：IS-IS进程号

·*lsplevel*：LSP类型，取值为L1或L2

ISIS-*procId*-EVT: Receive BGP convergence message, quit the overload state.

IS-IS进程收到BGP收敛消息，退出overload状态

·*procId*：IS-IS进程号

ISIS-*procId*-EVT: Receive IPv6 BGP convergence message, quit the overload state.

IS-IS进程收到IPv6 BGP收敛消息，退出overload状态

·*procId*：IS-IS进程号

【举例】

\# 在Router A上创建IS-IS进程1，路由器类型为**level-1-2**，并在GigabitEthernet1/0/2上使能IS-IS功能，接口的IP地址为1.1.1.1/24；在Router A上打开IS-IS消息事件调试信息开关。在接口GigabitEthernet1/0/2上配置IP地址为2.2.2.2/24。

\<RouterA\> debugging isis event

\*Apr  8 05:58:11:217 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-EVT: Processing the logical address delete event : 1.1.1.2/24

\*Apr  8 05:58:11:218 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-EVT: Processing the logical address add event : 2.2.2.2/24

*// 在GigabitEthernet1/0/2上删除主逻辑接口地址和添加新的主逻辑接口的事件*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis graceful-restart**

------------------------------------------------------------------------

【命令】

**[debuging isis graceful-restart** [ *process-id* ]]

**[undo debuging graceful-restart** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，范围为1～65535。

【描述】

**[debuging isis graceful-restart**]命令用来打开IS-IS GR调试信息开关。**undo debugging isis graceful-restart**命令用来关闭IS-IS GR调试信息开关。

缺省情况下，IS-IS进程的GR调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的GR调试信息开关。

表1-2 debugging isis graceful-restart命令输出信息描述表

字段

描述

ISIS-*procId*-GR: Temporary DIS type Level-*Level*, on  *CircName*, DIS: *DisStr*.

GR Helper端进行临时DIS选举

·*procId*：IS-IS进程号

·*Level*：进行DIS选举的Level，取值为1或2

·*CircName*：接口名

·DisStr：选举出来的临时DIS

ISIS-*procId*-GR: All Level-*Level* T1 timers have stopped.

T1定时器停止

·*procId*：IS-IS进程号

·*Level*：T1定时器所属的Level，取值为1或2

ISIS-*procId*-GR: Adjacency(*SystemIdr*) on *CircName*(Level-*level*) comes out RestartMode.

邻居的GR状态发生变化，由GR状态变为非GR状态

·*procId*：IS-IS进程号

·*SystemId*：邻居的系统ID

·*CircName*：接口名

·*Level*：邻居所属的Level，取值为1或2

ISIS-*procId*-GR: Adjacency(*SystemId*) on *CircName* (Level-*level*) comes in RestartMode.

邻居的GR状态发生变化，由非GR状态变为GR状态

·*procId*：IS-IS进程号

·*SystemId*：邻居的系统ID

·*CircName*：接口名

·*Level*：邻居所属的Level，取值为1或2

ISIS-*procId*-GR:Level-*Level* NBR(*SystemId*) SA bit set, adjacency not advertised.

邻居报文GR TLV中的SA比特位被设置上

·*procId*：IS-IS进程号

·*Level*：邻居所属的Level，取值为1或2

·*SystemId*：邻居的系统ID

ISIS-*procId*-GR:Level-*Level* NBR(*SystemId*) SA bit clear, adjacency advertised.

邻居报文GR TLV中的SA比特位被清除

·*procId*：IS-IS进程号

·*Level*：邻居所属的Level，取值为1或2

·*SystemId*：邻居的系统ID

ISIS-*procId*-GR:Receive restart request hello from *SystemId*, on *CircName* (Level-*Level*)

收到邻居的GR请求

·*procId*：IS-IS进程号

·*SystemId*：邻居的系统ID

·*CircName*：接口名

·*Level*：邻居所属的Level，取值为1或2

ISIS-*procId*-GR:Receive *helloType* hello with RR bit set from nbr *SystemId*, on *CircName*

收到RR置位的Hello报文：

·*procId*：IS-IS进程号

·*helloType*：取值为LAN L1、LAN L2、P2P

·*SystemId*：邻居的系统ID

·*CircName*：接口名

ISIS-*procId*-GR:RA received on circuit: Circ*Name* Level-*Level*

收到邻居的GR应答

·*procId*：IS-IS进程号

·*CircName*：接口名

·*Level*：邻居所属的Level，取值为1或2

ISIS-*procId*-GR:Interface(*CircName*) Level-*Level* T1 timer expired count: *T1TimerExpCnt*.

T1定时器超时

·*procId*：IS-IS进程号

·*CircName*：接口名

·*Level*：邻居所属的Level，取值为1或2

·*T1TimerExpCnt*：T1定时器超时的次数，超时10次之后取消T1定时器

ISIS-*procId*-GR:Interface(*CircName*) Level-*Level* T1 timer expired count has arrived max.

T1定时器超时次数达到最大次数10次

·*procId*：IS-IS进程号

·*CircName*：接口名

·*Level*：邻居所属的Level，取值为1或2

ISIS-*procId*-GR:Graceful-restart complete.

GR完成

·*procId*：IS-IS进程号

ISIS-*procId*-GR:Enter phase(*GrPhase*)

GR进入下一阶段

·*procId*：IS-IS进程号

·*GrPhase*：GR阶段，包括LSDB同步阶段、第一次SPF计算阶段、引入计算阶段、第二次SPF计算阶段、LSP生成阶段、GR完成阶段

ISIS-*procId*-GR:T3 timer stoped owe to all T2 timer stopped.

由于T2定时器停止，导致停止T3定时器

·*procId*：IS-IS进程号

ISIS-*procId*-GR:Received Level-*Level* T2 timer cancel event(*T2StopEvent*).

收到触发T2停止的事件，事件类型包括"所有T1定时器停止"和"LSDB同步完成"。两个事件都发生时才真正停止T2定时器

·*procId*：IS-IS进程号

·*Level*：GR的Level，取值为1或2

·*T2StopEvent*：触发停止T2定时器的事件，包括"所有T1定时器停止"和"LSDB同步完成"

ISIS-*procId*-GR:Level-*Level* T2 timer stopped

停止T2定时器

·*procId*：IS-IS进程号

·*Level*：GR的Level，取值为1或2

ISIS-*procId*-GR:Level-*Level* T2 timer expired

T2定时器超时

·*procId*：IS-IS进程号

·*Level*：GR的Level，取值为1或2

ISIS-*procId*-GR:T3 timer expired before T2 timer.

T3定时器先于T2定时器超时

·*procId*：IS-IS进程号

ISIS-*procId*-GR:Graceful-restart enter *GrTypeStr* phase(*LSDB synchronization*).

开始GR，分为restarting 方式和starting方式

·*procId*：IS-IS进程号

·*GrTypeStr*：GR方式，分为restarting和starting

ISIS-*procId*-GR:Begin to purge local Level-*Level*lsp

GR完成，将本地原来生成、现在失效的LSP清除

·*procId*：IS-IS进程号

·*Level*：LSP的Level，取值为1或2

ISIS-*procId*-GR:Purge Level-*Level* lsp L*spid*-*LspNum*

GR完成，将本地原来生成、现在失效的LSP清除

·*procId*：IS-IS进程号

·*Level*：LSP的Level，取值为1或2

·*Lspid*：LSP ID

·*LspNum*：LSP序号

ISIS-*procId*-GR: End to purge local Level-*Level* lsp

清除失效LSP结束

·*procId*：IS-IS进程号

·*Level*：LSP的Level，取值为1或2

ISIS-*procId*-GR: Synchronized Level-*Level* csnp from *SourceId* on circuit *CircName* range from *StartLspid* -*LspNum* to *EndLspidSysId* -*LspNum*

GR过程中收到Helper端发送的CSNP

·*procId*：IS-IS进程号

·*Level*：CSNP的Level，取值为1或2

·*SourceId*：Helper的系统ID

·*CircName*：接口名

·*StartLspId*：CSNP报文中开始的LSP ID

·*LspNum*：CSNP报文中LSP的序号

·*EndLspId*：CSNP报文中结束的LSPID

ISIS-*procId*-GR:Level-*Level* lsdb synchronization is complete

GR过程中LSDB同步完成

·*procId*：IS-IS进程号

·*Level*：LSDB的Level，取值为1或2

ISIS-*procId*-GR:Level-*Level* csnp set synchronization is complete on circuit *CircName*

GR过程中CSNP接收完全

·*procId*：IS-IS进程号

·*Level*：CSNP的Level，取值为1或2

·*CircName*：接口名

【举例】

\# Router A与Router B相连，在Router A上创建IS-IS进程，SystemID为0000.0000.0001、路由器类型为**level-1-2**，并在GigabitEthernet1/0/2上使能IS-IS功能，接口的IP地址为12.0.0.1/24；在Router B上创建IS-IS进程，SystemID为0000.0000.0002、路由器类型为**level-1-2**，并在GigabitEthernet1/0/2使能IS-IS功能，接口的IP地址为12.0.0.2/24；Router A与Router B在不同区域，建立Level-2类型的邻居。在Router B上打开IS-IS GR调试信息开关。

\<RouterB\> debugging isis graceful-restart

\<RouterB\> reset isis all graceful-restart

%Sep  5 16:09:47:646 2011 RouterB ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 100, Level-2 adjacency 0000.0000.0001 (GigabitEthernet1/0/2), state change to: DOWN.

\*Sep  5 16:09:47:735 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Graceful-restart enter restarting phase(LSDB synchronization).

*// 进入GR，方式为restarting，并进入LSDB同步阶段*

\*Sep  5 16:09:47:751 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-2 T1 timer expired count: 1.

\*Sep  5 16:09:47:751 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count: 1.

*// 接口GigabitEthernet1/0/2上Level-1的T1定时器超时1次*

%Sep  5 16:09:47:752 2011 RouterB ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 100, Level-2 adjacency 0000.0000.0001 (GigabitEthernet1/0/2), state change to: UP.

\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: RA received on circuit: GigabitEthernet1/0/2 Level-2

\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Synchronized Level-2 csnp from 0000.0000.0001.00 on circuit GigabitEthernet1/0/2 range from 0000.0000.0000.00-00 to ffff.ffff.ffff.ff-ff

*// 收到Helper端发送的Level-2的CSNP报文*

\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: RA received on circuit: GigabitEthernet1/0/2 Level-1

*// 收到Helper端的Level-2的GR回应报文*

\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Level-2 csnp set synchronization is complete on circuit GigabitEthernet1/0/2

*[// Level-2*]*的CSNP接收完全*

\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: All Level-2 T1 timers have stopped.

*// 关闭Level-2的T1定时器*

\*Sep  5 16:09:47:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Received Level-2 T2 timer cancel event(All T1 stopped).

*// 触发关闭Level-2的T2定时器，事件为所有T1定时器停止*

\*Sep  5 16:09:47:786 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Level-2 lsdb synchronization is complete

\*Sep  5 16:09:47:786 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Received Level-2 T2 timer cancel event(LSDB sync).

*// 触发关闭Level-2的T2定时器，事件为LSDB同步完成*

\*Sep  5 16:09:47:786 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Level-2 T2 timer stopped

*// 停止Level-2的T2定时器*

\<RouterB\>

\*Sep  5 16:09:50:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count: 2.

\*Sep  5 16:09:50:754 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: RA received on circuit: GigabitEthernet1/0/2 Level-1

\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count: 10.

\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count has arrived max.

*[// Level-1*]*的T1定时器超时次数达到10次*

\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: All Level-1 T1 timers have stopped.

*[// Level1*]*的T1定时器停止*

\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Received Level-1 T2 timer cancel event(All T1 stopped).

*// 触发关闭Level-1的T2定时器，事件为T1定时器停止*

\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Level-1 T2 timer stopped

*[// Level-2*]*的T2定时器停止*

\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: T3 timer stoped owe to all T2 timer stopped.

*// 两个Level的T2定时器都已停止，此时停止T3定时器*

\*Sep  5 16:10:14:752 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Enter phase(First SPF computation)

*// 进入GR的第一次SPF计算阶段*

\*Sep  5 16:10:14:825 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Enter phase(Redistribution)

*// 第一次SPF计算结束，进入GR的引入路由阶段*

\*Sep  5 16:10:14:825 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Enter phase(Second SPF computation)

*// 路由引入结束，进入GR的第二次SPF计算阶段*

\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Enter phase(LSP generation)

*// 第二次SPF计算结束，进入GR的LSP生成阶段*

\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Begin to purge local Level-1 lsp

*// 开始清除本地生成的Level-1的失效LSP*

\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: End to purge local Level-1 lsp

*// 本地生成的Level-1的失效LSP清除完成*

\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Begin to purge local Level-2 lsp

*// 开始清除本地生成的Level-2的失效LSP*

\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: End to purge local Level-2 lsp

*// 本地生成的Level-2的失效LSP清除完成*

\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Enter phase(Finish)

*[// LSP*]*生成完成，进入GR结束阶段*

\*Sep  5 16:10:14:914 2011 RouterB ISIS/7/ISISDBG: -MDC=1;

ISIS-100-GR: Graceful-restart complete.

*[// GR*]*完成*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis ha-event**

------------------------------------------------------------------------

【命令】

**[debuging isis ha-event**]

**[undo debuging isis ha-event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debuging isis ha-event**]命令用来打开IS-IS HA调试信息开关。**undo debugging isis ha-event**命令用来关闭IS-IS HA调试信息开关。

缺省情况下，IS-IS HA调试信息开关[处于关闭状态。]

如果未指定进程号，则打开所有IS-IS进程的HA调试信息开关。

表1-4 debugging isis ha-event命令输出信息描述表

字段

描述

ISIS-HA: RtBackup ISIS *datatype.*

实时备份ISIS 数据

·*datatype*：数据类型

ISIS-HA: Receive RIB reconnet event

收到重连RIB消息

ISIS-HA: Receive RIB pull-route event

收到更新路由消息

ISIS-HA: Receive ISIS RtData.

收到实时备份数据

ISIS-HA: Batch backup ISIS data.

批量备份

ISIS-HA: Stop ISIS data.

停止备份处理

ISIS-HA: Degrade (master to standby), delete ISIS data.

主板变为备板，删除IS-IS相关数据

ISIS-HA: Upgrade (standby to master), smooth ISIS data.

备板升级为主板，平滑IS-IS相关数据

ISIS-HA: Notify NBR smooth start

通知NBR平滑数据开始

ISIS-HA: Notify NBR smooth end

通知NBR平滑数据结束

ISIS-HA: Notify RIB disconnect start

通知与RIB连接断开处理开始

ISIS-HA: Notify RIB disconnect end

通知与RIB连接断开处理结束

ISIS-HA: Notify RIB smooth start

通知RIB平滑数据开始

ISIS-HA: Notify RIB smooth end

通知RIB平滑数据结束

ISIS-HA: Connect to RIB successfully.

跟RIB建立连接成功

ISIS-HA: Connect to RIB failed, try to reconnect later.

跟RIB建立连接失败，稍后重连

ISIS-HA: Receive SIGKILL Signal from SCM.

从SCM收到资源回退的消息

【举例】

\# 在Router A上创建IS-IS进程1，路由器类型为level-1-2，network-entity为10.7798.1111.1111.00，并在GigabitEthernet1/0/2上使能IS-IS功能，接口的IP地址为1.1.1.1/24；在Router A上打开IS-IS HA报文调试信息开关。

\<RouterA\> debugging isis ha-event

\*Apr  8 22:01:25:812 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-HA: RtBackup ISIS systemID.

\*Apr  8 22:01:25:813 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-HA: RtBackup ISIS Process Area Data.

*// 在GigabitEthernet1/0/2上删除network-entity*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis miscellaneous-errors**

------------------------------------------------------------------------

【命令】

**[debuging isis miscellaneous-errors**]

**[undo debuging miscellaneous-errors**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debuging isis miscellaneous-errors**]命令用来打开IS-IS进程无关调试信息开关。**undo debugging isis miscellaneous-errors**命令用来关闭IS-IS进程无关调试信息开关。

缺省情况下，IS-IS进程无关调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的进程无关调试信息开关。

表1-5 debugging isis miscellaneous-errors命令输出信息描述表

字段

描述

ISIS-ERR: Create all hello socket failed.

创建hello socket失败

ISIS-ERR: Destroy all hello socket failed.

删除hello socket失败

【举例】

\# 创建IS-IS进程。打开IS-IS进程无关调试信息开关。

\<RouterA\> debugging isis miscellaneous-errors

\*Apr  8 22:04:12:389 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-ERR: Create all hello socket failed

*// 收发Hello报文的socket创建失败*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis redistribute**

------------------------------------------------------------------------

【命令】

**[debugging isis redistribute** { **ipv4** [ **topology** *topo-name*  \| **ipv6** } { **event** \| **prefix**  *prefix* [ *mask-length*  ] }]]

**[undo debugging isis redistribute** { **ipv4** [ **topology** *topo-name*  \| **ipv6** } { **event** \| **prefix** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：打开IPv4路由引入开关。

**[topology** *topo-name*]：打开指定拓扑的引入开关。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则表示打开公网的IPv4路由引入开关。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6**]：打开IPv6路由引入开关。

**[event**]：打开路由引入事件开关。

**[prefix**]：打开IPv4路由引入前缀开关。

*[prefix* [ *mask-length* ]]：表示打开特定前缀开关。

【描述】

**[debuging isis redistribute ipv4 event**]命令用来打开IPv4引入事件调试信息开关。**undo** **debuging isis** **redistribute ipv4 event**命令用来关闭IPv4引入事件调试信息开关。

**[debuging isis redistribute ipv4 prefix**]命令用来打开IPv4引入前缀调试信息开关。**undo** **debuging isis** **redistribute ipv4 prefix**命令用来关闭IPv4引入前缀调试信息开关。

**[debuging isis redistribute ipv6 event**]命令用来打开IPv6引入事件调试信息开关。**undo** **debuging isis** **redistribute ipv6 event**命令用来关闭IPv6引入事件调试信息开关。

**[debuging isis redistribute ipv6 prefix**]命令用来打开IPv6引入前缀调试信息开关。**undo** **debuging isis** **redistribute ipv6 prefix**命令用来关闭IPv6引入前缀调试信息开关。

缺省情况下，IS-IS的引入事件和前缀调试信息开关处于关闭状态。

如果未指定前缀，则打开IS-IS的所有前缀调试信息开关。

表1-3 debugging isis redistribute ipv4 event命令输出信息描述表

字段

描述

ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* request rib to stop *rpaname* batch notify

通知RIB停止路由引入批量上报

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*procid*：IS-IS进程号

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* deregister *rpaname* notify to rib

通知RIB去注册路由引入

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*procid*：IS-IS进程号

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* request rib for *rpaname* query

向RIB查询路由

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*procid*：IS-IS进程号

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* register *rpaname* notify to rib

通知RIB注册路由引入

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*procid*：IS-IS进程号

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid*  is added to *rpaname* *batchtype* batch list

添加IS-IS进程到引入路由批量链表中

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*procid*：IS-IS进程号

·*rpaname*：路由协议名

·*batchtype*：批量类型，register或query

ISIS-RDM(TopoIndex *mtindex*): ISIS process *procid* is deleted from *rpaname* *batchtype* batch list

从引入路由批量链表中删除IS-IS进程

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*procid*：IS-IS进程号

·*rpaname*：路由协议名

·*batchtype*：批量类型，register或query

ISIS-RDM(TopoIndex *mtindex*): Reregister *rpaname* attr to rib

向RIB重新注册路由属性

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): Register *rpaname* attr to rib

向RIB注册路由属性

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): Deregister *rpaname* attr to rib

向RIB去注册路由属性

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): IS-IS instance *intsid* receive *batchmsgtype* message

接收到批量开始/结束消息

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*intsid*：实例号

·*batchmsgtype*：批量消息类型，批量开始/批量结束

ISIS-RDM(TopoIndex *mtindex*): Process protocol *rpaname* attr msg

处理路由属性消息

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): Process protocol *rpaname* smooth attr msg

处理路由属性平滑消息

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): Route redist process, schedule type: *schedtype*

处理引入调度消息

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*schedtype*：调度类型

表1-4 debugging isis redistribute ipv4 prefix命令输出信息描述表

字段

描述

ISIS-RDM(TopoIndex *mtindex*): Process common refresh message for redist prefix *prefix/masklen*, old protocol: *rpaname*, new protocol: *rpaname*,  flag: *flag*

处理引入路由刷新消息

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*prefix/masklen*：路由前缀和掩码长度

·*rpaname*：路由协议名

·*flag*：路由标记

ISIS-RDM(TopoIndex *mtindex*): Process common delete message for redist prefix *prefix/masklen*, old protocol:  *rpaname*

处理引入路由删除消息

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*prefix/masklen*：路由前缀和掩码长度

·*rpaname*：路由协议名

ISIS-RDM(TopoIndex *mtindex*): Process *procid* Adding redist prefix for *prefix/masklen*

添加上报的路由到本地路由表

·TopoIndex *mtindex*：指定拓扑的路由管理拓扑索引

·*procid*：IS-IS进程号

·*prefix/masklen*：路由前缀和掩码长度

【举例】

\# 创建IS-IS进程。打开IS-IS的IPv4引入事件开关。

\<RouterA\> debugging isis redistribute ipv4 event

\*Nov  1 12:51:08:773 2012 RouterAISIS/7/ISISDBG: -MDC=1;

ISIS-RDM(TopoIndex 0): ISIS process 1 is added to static register batch list

*// 添加IS-IS进程1到静态路由引入注册链表中*

\*Nov  1 12:51:08:774 2012 RouterAISIS/7/ISISDBG: -MDC=1;

ISIS-RDM(TopoIndex 0): ISIS process 1 register static notify to rib

*// 向RIB注册静态路由引入*

\*Nov  1 12:51:08:774 2012 RouterAISIS/7/ISISDBG: -MDC=1;

ISIS-RDM(TopoIndex 0): IS-IS instance 0 receive BatchStart message

*// 公网实例接收到RIB路由批量上报开始消息*

\*Nov  1 12:51:08:775 2012 RouterAISIS/7/ISISDBG: -MDC=1;

ISIS-RDM(TopoIndex 0): IS-IS instance 0 receive BatchEnd message

*// 公网实例接收到RIB路由批量上报结束消息*

\# 创建IS-IS进程。打开IS-IS的IPv4引入前缀开关。

\<RouterA\> debugging isis redistribute ipv4 prefix

\*Nov  1 13:17:07:637 2012 RouterAISIS/7/ISISDBG: -MDC=1;

ISIS-RDM(TopoIndex 0): Process common refresh message for redist prefix 200.0.0.0/24, old pro

tocol: static, new protocol: static, flag: 3.

*// 接收到RIB上报的静态路由200.0.0.0/24刷新消息*

\*Nov  1 13:17:07:637 2012 RouterAISIS/7/ISISDBG: -MDC=1;

ISIS-RDM(TopoIndex 0): (ProID 1): Adding redist prefix for 200.0.0.0/24.

*// 添加引入路由200.0.0.0/24*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis self-originate-update**

------------------------------------------------------------------------

【命令】

**[debugging** **isis** **self-originate-update** [ *process-id* ]]

**[undo** **debugging** **isis** **self-originate-update** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【描述】

**[debugging isis self-originate-update**]命令用来打开IS-IS本地更新的调试信息开关。**undo debugging isis self-originate-update**命令用来关闭IS-IS本地更新的调试信息开关。

缺省情况下，IS-IS本地更新的调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的本地更新的调试信息开关。

表1-6 debugging isis self-originate-update命令输出信息描述表

字段

描述

ISIS-*process-id*-ORG: Purging level-*level* LSP [*lsp-id*]

清除LSP报文

·*process-id*：IS-IS进程号

·*level*：LSP的Level，取值为1或2

·*lsp-id*：被清除LSP报文的ID

ISIS-*process-id*-ORG: *tlv-name ip-address* into level-*level* LSPs, TLV: *tlv-type*

添加TLV到LSP中

·*process-id*：IS-IS进程号

·*tlv-name*：TLV名称，取值为Adding neighbor或Adding address

·*ip-address*：IP地址，取值为空或IP地址

·*level*：LSP的Level，取值为1或2

·*tlv-type*：TLV类型，取值为协议规定的值

ISIS-*process-id*-ORG: Deleting address *ip-address* from level-*level* LSPs, TLV: *tlv-type*

从LSP中删除TLV

·*process-id*：IS-IS进程号

·*ip-address*：IP地址，取值为IP地址

·*level*：LSP的Level，取值为1或2

·*tlv-type*：TLV类型，取值为协议规定的值

ISIS-*process-id*-ORG: The remaining space of level-*level* fragment 0 LSP is shortage

往LSP 0分片中添加TLV时，剩余空间不足

·*process-id*：IS-IS进程号

·*level*：LSP的Level，取值为1或2

ISIS-*process-id*-ORG: ISIS(*process-id*) level-*level* LSP over flow

往LSP分片中添加TLV时，所有LSP分片空间已满

·*process-id*：IS-IS进程号

·*level*：LSP的Level，取值为1或2

ISIS-*process-id*-ORG: The remaining space of level-*level* fragment 0 LSP is shortage while adding area or protocol support

往LSP 0分片中添加区域地址或协议支持TLV时，剩余空间不足

·*process-id*：IS-IS进程号

·*level*：LSP的Level，取值为1或2

ISIS-*process-id*-ORG: Rebuilding all level-*level* LSPs Start

开始rebuild所有的LSP

·*process-id*：IS-IS进程号

·*level*：LSP的Level，取值为1或2

ISIS-*process-id*-ORG: Rebuilding all level-*level* LSPs End

结束rebuild所有的LSP

·*process-id*：IS-IS进程号

·*level*：LSP的Level，取值为1或2

ISIS-*process-id*-ORG: MTU Change triggers rebuild

MTU变化触发rebuild

·*process-id*：IS-IS进程号

ISIS-*process-id*-ORG: Attempting to exceed Max Seq Num

生成LSP时，序列号达到最大

·*process-id*：IS-IS进程号

ISIS-*process-id*-ORG: Generating Level-*level* LSP [*lsp-id*, Seq *sequence-number*, Length *lsp-length*]

生成LSP结束

·*process-id*：IS-IS进程号

·*level*：LSP的Level，取值为1或2

·*lsp-id*：生成LSP的ID

·*sequence-number*：生成LSP的序列号

·*lsp-length*：生成LSP的长度

ISIS-*process-id*-ORG: TLV Handle triggers rebuild

TLV变化触发rebuild

·*process-id*：IS-IS进程号

ISIS-*process-id*-ORG: Added level-*level* area address *area-address*

往TLV DB中添加区域地址

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*area-address*：区域地址

ISIS-*process-id*-ORG: Deleted level-*level* area address *area-address*

从TLV DB中删除区域地址

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*area-address*：区域地址

ISIS-*process-id*-ORG: Added level-*level* protocol support *protocol-support*

往TLV DB中添加协议支持

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*protocol-support*：协议支持

ISIS-*process-id*-ORG: Deleted level-*level* protocol support *protocol-support*

从TLV DB中删除协议支持

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*protocol-support*：协议支持

ISIS-*process-id*-ORG: Added level-*level* interface IP address: *ip-address/mask*

往TLV DB中添加接口地址

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*ip-address*：接口地址

·*mask*：接口地址掩码

ISIS-*process-id*-ORG: Deleted level-*level* interface IP address: *ip-address/mask*

从TLV DB中删除接口地址

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*ip-address*：接口地址

·*mask*：接口地址掩码

ISIS-*process-id*-ORG: Added level-*level* neighbour: System *system-id* =\> Neighbour *source-id*

往TLV DB中添加非伪节点到伪节点的邻居

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*system-id*：非伪节点System ID

·*source-id*：伪节点Source ID

ISIS-*process-id*-ORG: Deleted level-*level* neighbour: System *system-id* =\> Neighbour *source-id*

从TLV DB中删除非伪节点到伪节点的邻居

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*system-id*：非伪节点System ID

·*source-id*：伪节点Source ID

ISIS-*process-id*-ORG: Modified level-*level* neighbour: System *system-id* =\> Neighbour *source-id*

在TLV DB中修改非伪节点到伪节点的邻居

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*system-id*：非伪节点System ID

·*source-id*：伪节点Source ID

ISIS-*process-id*-ORG: Added level-*level* pseudo neighbour: Pseudo *source-id* =\> Neighbour *system-id*

往TLV DB中添加伪节点到非伪节点的邻居

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*system-id*：非伪节点System ID

·*source-id*：伪节点Source ID

ISIS-*process-id*-ORG: Deleted level-*level* pseudo neighbour: Pseudo *source-id* =\> Neighbour *system-id*

从TLV DB中删除伪节点到非伪节点的邻居

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*system-id*：非伪节点System ID

·*source-id*：伪节点Source ID

ISIS-*process-id*-ORG: Added level-*level* IP prefix: *ip-address/mask*

往TLV DB中添加IP前缀

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*ip-address*：IP前缀地址

·*mask*：IP前缀地址掩码

ISIS-*process-id*-ORG: Deleted level-*level* IP prefix: *ip-address/mask*

从TLV DB中删除IP前缀

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*ip-address*：IP前缀地址

·*mask*：IP前缀地址掩码

ISIS-*process-id*-ORG: Modified level-*level* IP prefix: *ip-address/mask*

在TLV DB中修改IP前缀

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*ip-address*：IP前缀地址

·*mask*：IP前缀地址掩码

ISIS-*process-id*-ORG: Added level-*Level* router ID *router-id.*

在TLV DB中添加Router ID

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

·*router-**id*：MPLS LSR ID，点分十进制格式

ISIS-*process-id*-ORG: Deleted level-*Level* router ID*.

在TLV DB中添加Router ID

·*process-id*：IS-IS进程号

·*level*：TLV DB的Level，取值为1或2

【举例】

\# Router A与Router B相连，在Router A上创建IS-IS进程，SystemID为7777.8888.1111、路由器类型为**level-1-2**，并在GigabitEthernet1/02上使能IS-IS功能，接口的IP地址为8.8.8.8/24；在Router B上创建IS-IS进程，SystemID为5555.1111.1111、路由器类型为**level-1-2**，并在GigabitEthernet1/0/4使能IS-IS功能，接口的IP地址为8.8.8.5/24；Router A与Router B在同一个区域18。在Router A上打开IS-IS本地更新的调试信息开关。

\<RouterA\> debugging isis self-originate-update

\<RouterA\> system-view

RouterA interface gigabitethernet 1/0/2

RouterA-GigabitEthernet1/0/2 ip address 8.8.8.7 24

RouterA-GigabitEthernet1/0/2

\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Deleted level-1 interface IP address: 8.8.8.8/255.255.255.0

\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Deleted level-2 interface IP address: 8.8.8.8/255.255.255.0

*// 从TLV DB中删除接口IP地址*

\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Deleted level-1 IP prefix: 8.8.8.0/255.255.255.0

\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Deleted level-2 IP prefix: 8.8.8.0/255.255.255.0

*// 从TLV DB中删除IP前缀*

\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Added level-1 interface IP address: 8.8.8.7/255.255.255.0

\*Apr  8 16:26:27:279 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Added level-2 interface IP address: 8.8.8.7/255.255.255.0

\*Apr  8 16:26:27:283 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

*// 在TLV DB中添加接口IP地址*

ISIS-1-ORG: Deleting address 8.8.8.0/24 from level-1 LSPs, TLV: 128

\*Apr  8 16:26:27:283 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Deleting address 8.8.8.0/24 from level-2 LSPs, TLV: 128

*// 从LSP中删除IP前缀*

%Apr  8 16:26:27:283 2011 RouterA ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 1, Level-1 adjacency 5555.1111.1111 (GigabitEthernet1/0/2), state change to: DOWN.

\*Apr  8 16:26:27:283 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Deleted level-1 pseudo neighbour: Pseudo 7777.8888.1111.01 =\> Neighbour 5555.1111.1111

%Apr  8 16:26:27:283 2011 RouterA ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 1, Level-2 adjacency 5555.1111.1111 (GigabitEthernet1/0/2), state change to: DOWN.

\*Apr  8 16:26:27:283 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Deleted level-2 pseudo neighbour: Pseudo 7777.8888.1111.01 =\> Neighbour 5555.1111.1111

*// 邻居down，从TLV DB中删除伪节点到非伪节点邻居*

%Apr  8 16:26:27:392 2011 RouterA ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 1, Level-2 adjacency 5555.1111.1111 (GigabitEthernet1/0/2), state change to: UP.

\*Apr  8 16:26:27:392 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Added level-2 pseudo neighbour: Pseudo 7777.8888.1111.01 =\> Neighbour 5555.1111.1111

%Apr  8 16:26:27:392 2011 RouterA ISIS/5/ISIS_NBR_CHG: -MDC=1;  IS-IS 1, Level-1 adjacency 5555.1111.1111 (GigabitEthernet1/0/2), state change to: UP.

\*Apr  8 16:26:27:392 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Added level-1 pseudo neighbour: Pseudo 7777.8888.1111.01 =\> Neighbour 5555.1111.1111

*// 邻居up，从TLV DB中添加伪节点到非伪节点邻居*

\*Apr  8 16:26:29:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Generating Level-2 LSP [7777.8888.1111.01-00, Seq 0x0000000a, Length 55]

\*Apr  8 16:26:29:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Generating Level-1 LSP [7777.8888.1111.01-00, Seq 0x0000000a, Length 55]

*// 生成伪节点LSP*

\*Apr  8 16:26:29:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Generating Level-2 LSP [7777.8888.1111.00-00, Seq 0x00000013, Length 54]

\*Apr  8 16:26:29:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Generating Level-1 LSP [7777.8888.1111.00-00, Seq 0x00000014, Length 54]

*// 生成LSP*

\*Apr  8 16:26:37:284 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Added level-1 IP prefix: 8.8.8.0/255.255.255.0

\*Apr  8 16:26:37:284 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Adding address 8.8.8.0/24 into level-1 LSPs, TLV: 128

\*Apr  8 16:26:37:284 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Added level-2 IP prefix: 8.8.8.0/255.255.255.0

\*Apr  8 16:26:37:284 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Adding address 8.8.8.0/24 into level-2 LSPs, TLV: 128

\*Apr  8 16:26:39:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

*// 在TLV DB中添加IP前缀，在LSP中添加IP前缀*

ISIS-1-ORG: Generating Level-2 LSP 7777.8888.1111.00-00, Seq 0x00000014, Length 68

\*Apr  8 16:26:39:290 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-ORG: Generating Level-1 LSP [7777.8888.1111.00-00, Seq 0x00000015, Length 68]

*// 生成LSP*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis snp-packet**

------------------------------------------------------------------------

【命令】

**[debugging**[ **isis** **snp-packet** [ **receive** \| **send** ]  **verbose**   *process-id* ]]

**[undo**[ **debugging** **isis** **snp-packet** [ **receive** \| **send** ]  **verbose**   *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：表示接收SNP报文调试信息开关。

**[send**]：表示发送SNP报文调试信息开关。

**[verbose**]：表示SNP报文详细调试信息开关。

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【描述】

**[debugging isis snp-packet**]命令用来打开IS-IS SNP报文的调试信息开关。**undo debugging isis snp-packet**命令用来关闭IS-IS SNP报文的调试信息开关。

缺省情况下，IS-IS SNP报文的调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的SNP报文的调试信息开关。

表1-7 debugging isis snp-packet命令输出信息描述表

字段

描述

ISIS-*process-id*-SNP:Receive *psnp-type* from *system-id* on circuit *circuit-name*

收到PSNP报文

·*process-id*：IS-IS进程号

·*psnp-type*：PSNP报文类型，取值为L1 PSNP或L2 PSNP

·*system-id*：发送PSNP报文IS-IS进程的System ID

·*circuit-name*：接口名称

ISIS-*process-id*-SNP:Receive *csnp-type* from *source-id* on circuit *circuit-name* range from *start-lsp-id* to *end-lsp-id*

收到CSNP报文

·*process-id*：IS-IS进程号

·*csnp-type*：CSNP报文类型，取值为L1 CSNP或L2 CSNP

·*source-id*：发送CSNP报文IS-IS进程的SOURCE ID

·*circuit-name*：接口名称

·*start-lsp-id*：LSP摘要的起始LSP ID

·*end-lsp-id*：LSP摘要的结束LSP ID

ISIS-*process-id*-SNP:Not find current lsp entry to build csnp

发送CSNP报文时，在LSDB中没有找到起始LSP ID或第一个比起始LSP ID大的LSP

·*process-id*：IS-IS进程号

ISIS-*process-id*-SNP:Circuit(*circuit-name*) silence, csnp NOT sent

接口配置silent，不发送CSNP

·*process-id*：IS-IS进程号

·*circuit-name*：接口名称

ISIS-*process-id*-SNP:Level-*level* csnp timer expired on a NOT dis circuit(*circuit-name*)

CSNP定时器在非DIS接口上超时

·*process-id*：IS-IS进程号

·*level*：接口的Level，取值为1或2

·*circuit-name*：接口名称

ISIS-*process-id*-SNP:Send *snp-type* on circuit *circuit-name*

发送CSNP/PSNP报文

·*process-id*：IS-IS进程号

·*snp-type*：SNP报文类型，取值为L1 CSNP、L2 CSNP、L1 PSNP或L2 PSNP

·*circuit-name*：接口名称

ISIS-*process-id*-SNP:Circuit(*circuit-name*) silence, psnp NOT sent

接口配置silent，不发送PSNP

·*process-id*：IS-IS进程号

·*circuit-name*：接口名称

ISIS-*process-id*-SNP:Level- *level* psnp timer expired on a dis circuit(*circuit-name*)

PSNP定时器在DIS接口上超时

·*process-id*：IS-IS进程号

·*level*：接口的Level，取值为1或2

·*circuit-name*：接口名称

ISIS-*process-id*-SNP:Lsp entry *lsp-id* processed, newer than lsdb copy

收到LSP摘要比LSDB中的新

·*process-id*：IS-IS进程号

·*lsp-id*：收到的LSP摘要ID

ISIS-*process-id*-SNP:Lsp entry *lsp-id* processed, older than lsdb copy

收到LSP摘要比LSDB中的旧

·*process-id*：IS-IS进程号

·*lsp-id*：收到的LSP摘要ID

ISIS-*process-id*-SNP:Lsp entry *lsp-id* processed, same as lsdb copy

收到LSP摘要和LSDB中的新旧程度一样

·*process-id*：IS-IS进程号

·*lsp-id*：收到的LSP摘要ID

ISIS-*process-id*-SNP:Lsp entry *lsp-id* processed, NO exist in lsdb

收到LSP摘要在LSDB中不存在

·*process-id*：IS-IS进程号

·*lsp-id*：收到的LSP摘要ID

ISIS-*process-id*-SNP:Psnp not processed before DIS election

在DIS选举完成之前不处理收到的PSNP报文

·process-id：IS-IS进程号

ISIS-*process-id*-SNP:Psnp not processed, current IS is NOT DIS

当前的IS不是DIS时不处理收到的PSNP报文

·process-id：IS-IS进程号

ISIS-*process-id*-SNP:Csnp not processed before DIS election

在DIS选举完成之前不处理收到的CSNP报文

·process-id：IS-IS进程号

ISIS-*process-id*-SNP:Csnp not processed on DIS

DIS不处理收到的CSNP报文

·process-id：IS-IS进程号

ISIS-*process-id*-SNP:Lsp entry *lsp-id* in csnp is not found in lsdb

收到CSNP报文中的LSP摘要在LSDB中不存在

·*process-id*：IS-IS进程号

·*lsp-id*：收到的LSP摘要ID

ISIS-*process-id*-SNP: *snp-content*

SNP报文的内容

·*process-id*：IS-IS进程号

·*snp-content*：SNP报文内容

【举例】

\# Router A与Router B相连，在Router A上创建IS-IS进程，SystemID为7777.8888.1111、路由器类型为**level-1-2**，并在GigabitEthernet1/0/2上使能IS-IS功能，接口的IP地址为8.8.8.8/24；在Router B上创建IS-IS进程，SystemID为5555.1111.1111、路由器类型为**level-1-2**，并在GigabitEthernet1/0/4使能IS-IS功能，接口的IP地址为8.8.8.5/24；Router A与Router B在同一个区域18。在Router A上打开IS-IS SNP报文的调试信息开关。

\<RouterA\> debugging isis snp-packet

\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-SNP:

0000: 83 21 01 06  18 01 00 00  00 63 55 55  11 11 11 11

0010: 00 00 00 00  00 00 00 00  00 ff ff ff  ff ff ff ff

0020: ff 09 40 04  a8 55 55 11  11 11 11 00  00 00 00 00

0030: 05 ff 6e 04  6b 55 55 11  11 11 11 00  01 00 00 00

0040: 01 49 95 04  a6 55 55 11  11 11 11 01  00 00 00 00

0050: 03 d8 b4 04  a7 77 77 88  88 11 11 00  00 00 00 00

0060: 05 f0 47

*[// SNP*]*报文内容*

\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-SNP: Receive L1 CSNP from 5555.1111.1111.00 on circuit GigabitEthernet1/0/2 range from 0000.0000.0000.00-00 to ffff.ffff.ffff.ff-ff

*// 收到CSNP报文*

\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-SNP: Lsp entry 5555.1111.1111.00-00 processed, same as lsdb copy

\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

*[// CSNP*]*报文上的LSP摘要和LSDB中的新旧程度一样*

ISIS-1-SNP: Lsp entry 5555.1111.1111.00-01 processed, NO exist in lsdb

\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

*[// CSNP*]*报文上的LSP摘要在LSDB中不存在*

ISIS-1-SNP: Lsp entry 5555.1111.1111.01-00 processed, same as lsdb copy

\*Apr  8 16:51:23:195 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-SNP: Lsp entry 7777.8888.1111.00-00 processed, same as lsdb copy

\*Apr  8 16:51:24:151 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-SNP: Send L1 PSNP on circuit GigabitEthernet1/0/2

*// 发送PSNP报文*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis spf**

------------------------------------------------------------------------

【命令】

**[debugging**[ **isis** **spf** [ **pic** \| **verbose** ]  *process-id* [ **ipv4** [ **topology** *topo-name*  \| **ipv6** ] ]]]

**[undo**[ **debugging** **spf** [ **pic** \| **verbose**]  *process-id* [ **ipv4** [ **topology** *topo-name*  \| **ipv6** ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pic**]：表示前缀无关收敛调试信息开关。

**[verbose**]：表示路由计算详细调试信息开关。

*[process-id*]：IS-IS进程号，取值范围为1～65535。

**[ipv4**]：打开IPv4路由计算调试信息开关。

**[topology** *topo-name*]：打开指定拓扑的路由计算调试信息开关。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则表示打开公网的IPv4路由计算调试信息开关。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6**]：打开IPv6路由计算调试信息开关。

【描述】

**[debugging isis** **spf**]命令用来打开IS-IS路由计算调试信息开关。**undo debugging isis** **spf**命令用来关闭IS-IS路由计算调试信息开关。

缺省情况下，IS-IS路由计算调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的路由计算调试信息开关。

表1-8 debugging isis spf命令输出信息描述表

字段

描述

ISIS- *process-id* -SPF: (MT *topoId*) Trigger SPF at  Sec =* xxx*, MSec = *yyy*

触发路由计算时间

·*process-id*：进程号

·*topoId*：拓扑号

·*xxx*：秒值

·*yyy*：毫秒值

ISIS-* process-id* -SPF: (MT *topoId*) SPF old scheduled event: *triggerType*, new trigger event: *triggerType*

开始新的触发，显示旧的和新的触发类型

·*process-id*：进程号

·topoId：拓扑号

·*triggerType*，触发类型，包括：全部路由计算、ISPF拓扑变化、区域地址变化、增量IP前缀计算、全部IP前缀计算、停止计算

ISIS-* process-id* -SPF: (MT *topoId*) Total IPv4 route number less then maximum, SPF will be resche

dule. 

需要进行路由前缀超规格恢复计算

·*process-id**：*进程号

·*topoId*：拓扑号

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) SPF node Create root node *sourceId* Dist:* distanceValue* Nextho

ps: *nexthopNum* Nbrs:* nbrNum* Parents:* parentNum* Tree

创建根节点SPFNODE

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

·*distanceValue*：到达根结点的cost值

·*nexthopNum*：节点的下一跳数

·*nbrNum*：节点的邻居数

·*parentNum*：父节点数

ISIS-* process-id* -SPF: SPF node (MT *topoId*)(L *sysLevel*) Adding system *sourceId*

创建SPF节点

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

ISIS-* process-id* -SPF: SPF node (MT *topoId*)(L *sysLevel*) Deleting system *sourceId*

删除SPF节点

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

ISIS-* process-id* -SPF: SPF node (MT *topoId*)(L *sysLevel*) Updating system *sourceId*Overload

更新SPF节点状态为Overload

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

ISIS-* process-id* -SPF: SPF node (MT *topoId*)(L *sysLevel*) Updating system *sourceId*

更新SPF节点状态从Overload中恢复

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) SPF node Set DIRECT flag on node. *sourceId*  Dist:

*[distanceValue* Nexthops:* nexthopNum* Nbrs:* nbrNum* Parents:* parentNum* Direct]

设置节点Direct标志

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

·*distanceValue*：到达根结点的cost值

·*nexthopNum*：节点的下一跳数

·*nbrNum*：节点的邻居数

·*parentNum*：父节点数

ISIS-* process-id* -SPF: SPF link (MT *topoId*)(L *sysLevel*) Adding link *sourceId* \--\> *destId*  Cost:*Cost*  

创建广播网Link

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

·*destId*：目的系统ID

·*Cost*：路径开销值

ISIS-* process-id* -SPF: SPF link (MT *topoId*)(L *sysLevel*) Deleting link *sourceId* \--\> *destId*  Cost:*Cost*

删除广播网Link

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

·*destId*：目的系统ID

·*Cost*：路径开销值

ISIS-* process-id* -SPF: SPF link (MT *topoId*)(L *sysLevel*) Updating link *sourceId* \--\> *destId*  Cost:*Cost*

更新广播网Link

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

·*destId*：目的系统ID

·*Cost*：路径开销值

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) I-SPF run started at  Sec = *xxx*, MSec = *yyy*.

ISPF路由计算开始时间

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*xxx*：秒值

·*yyy*：毫秒值

ISIS-* process-id* -SPF: Checking changed links.

处理变化Link，决定是否需要重构SPF树

·*process-id*：进程号

ISIS-* process-id* -SPF: Need rebuild SPT. 

需要重构SPF树

·*process-id*：进程号

ISIS-* process-id* -SPF: Processing links with change flags.

无需重构SPF树，仅处理协议使用、下一跳变化

·*process-id*：进程号

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Running full SPF.

开始全部SPF计算

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS-* process-id* -SPF: (MT *topoId*) Begin Level-* sysLevel* SPF from root node.

从根节点开始进行SPF计算

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) SPF node Node is added into SPT. *sourceId* Dist:* distanceValue* Nexthops:* nexthopNum* Nbrs:* nbrNum* Parents:* parentNum* Tree 

把TentList中的节点加入到SPT树中

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

·*distanceValue*：到达根结点的cost值

·*nexthopNum*：节点的下一跳数

·*nbrNum*：节点的邻居数

·*parentNum*：父节点数

ISIS-* process-id* -SPF:  New distance is *distanceValue*. 

到根结点的新Distance

·*process-id*：进程号

·*distanceValue*：到达根结点的cost值

ISIS-* process-id* -SPF:  Less cost, add node to TENT HEAP.

子结点到根结点的Distance小

·*process-id*：进程号

ISIS-* process-id* -SPF:  Equal cost, add node to TENT HEAP.

子结点到根结点的Distance相同

·*process-id*：进程号

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) SPF node Son node update to TENT list *sourceId* D

ist:* distanceValue* Nexthops:* nexthopNum* Nbrs:* nbrNum* Parents:* parentNum* Tent Direct

把节点加入到TentList中

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*sourceId*：源系统ID

·*distanceValue*：到达根结点的cost值

·*nexthopNum*：节点的下一跳数

·*nbrNum*：节点的邻居数

·*parentNum*：父节点数

ISIS-* process-id* -SPF: Link is backard link, ignore.

忽略回指Link的处理

·*process-id*：进程号

ISIS-* process-id* -SPF: Node is Overload. Ignore its nbrs.

当前节点Overload，则忽略其邻居

·*process-id*：进程号

ISIS-* process-id* -SPF: (MT *topoId*) Merge nexthop from root node IPV4:* nexthopNum1 */* nexthopNum2*

从根节点上继承下一跳

·*process-id*：进程号

·*topoId*：拓扑号

·*nexthopNum1*：根节点下Link上的下一跳数

·*nexthopNum2*：子节点上的下一跳数

ISIS-* process-id* -SPF: (MT *topoId*) Merge nexthop from parent node IPV4:* nexthopNum*

从父节点上继承下一跳

·*process-id*：进程号

·*topoId*：拓扑号

·*nexthopNum*：父节点上的下一跳数

ISIS-* process-id* -SPF: Inform SPF nodes change to PAC&PRC.

处理SpfNode节点变化提交PAC和PRC处理

·*process-id*：进程号

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) I-SPF run ended at  Sec = *xxx*, MSec = *yyy*.

·ISPF路由计算结束时间

·*process-id**：*进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*xxx*：秒值

·*yyy*：毫秒值

ISIS-* process-id* -SPF: AREA: Updating (L *sysLevel*) areas:                                        

          New areas: \*newareaAddress*\*newareaAddress* \*newareaAddress*.                                                          

          Old areas:\*oldareaAddress*\*oldareaAddress* \*oldareaAddress*.

更新区域地址，显示旧的和新的区域地址信息

·*process-id*：进程号

·*sysLevel*：系统级别

·*newareaAddress*：新区域地址

·*oldareaAddress*：旧区域地址

ISIS-* process-id* -SPF: (L *sysLevel*) Install one area: *areaAddress*.

加入一个新的区域地址

·*process-id*：进程号

·*sysLevel*：系统级别

·*areaAddress*：区域地址

ISIS-* process-id* -SPF: (L *sysLevel*) Remove one area: *areaAddress*. 

删除一个区域地址

·*process-id*：进程号

·*sysLevel*：系统级别

·*areaAddress*：区域地址

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) AREA run started at  Sec = *xxx*, MSec = *yyy*.

区域地址计算开始时间

·process-id：进程号

·topoId：拓扑号

·sysLevel：系统级别

·xxx：秒值

·yyy：毫秒值

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Processing increment area address calculating.

处理区域地址变化

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Area Addr: *areaAddress* is available.

区域地址有效

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*areaAddress*：区域地址

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Area Addr: *areaAddress* is available.

区域地址无效

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*areaAddress*：区域地址

ISIS-* process-id* -SPF: (MT *topoId*) Updating computed areas into L2 LSDB.

往L2的LSP中更新区域地址

·*process-id*：进程号

·*topoId*：拓扑号

ISIS-* process-id* -SPF: (MT *topoId*) Attach bit is set in running SPF.

区域地址计算中设置ATT位

·*process-id*：进程号

·*topoId*：拓扑号

ISIS-* process-id* -SPF: (MT *topoId*) Attach bit is cleared in running SPF.

区域地址计算中清除ATT位

·*process-id*：进程号

·*topoId*：拓扑号

ISIS-* process-id* -SPF: (MT *topoId*) Area Addr: *areaAddress* is adevertised to L2.

区域地址在L2LSP中的发布

·*process-id*：进程号

·*topoId*：拓扑号

·*areaAddress*：区域地址

ISIS-* process-id* -SPF: (MT *topoId*) Area Addr: *areaAddress* is not adevertised to L2.

区域地址撤销在L2LSP中的发布

·*process-id*：进程号

·*topoId*：拓扑号

·*areaAddress*：区域地址

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) AREA run ended at  Sec = *xxx*, MSec = *yyy*.

区域地址计算结束时间

·*process-id*：进程号

·topoId：拓扑号

·sysLevel：系统级别

·xxx：秒值

·yyy：毫秒值

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Adding prefix for *ipPrefix* / *subMask* from *sourceId*, into forwarding table.

往ISIS L1/L2路由表中加入当前节点的IP前缀

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*ipPrefix*：IP地址前缀

·*subMask*：子网掩码

·*sourceId*：源系统ID

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Deleting prefix for *ipPrefix* / *subMask*, from forw

arding table. 

从ISIS L1/L2路由表中删除IP前缀

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*ipPrefix*：IP地址前缀

·*subMask*：子网掩码

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Modifying prefix for *ipPrefix* / *subMask*, in forw

arding table.

往ISIS路由表中更改IP前缀

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*ipPrefix*：IP地址前缀

·*subMask*：子网掩码

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) PRC run started at  Sec = *xxx*, MSec = *yyy*.

PRC计算开始时间

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*xxx*：秒值

·*yyy*：毫秒值

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Processing increment IPV4 prefix calculating.

计算变化的IPv4路由前缀

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Processing full ipv4 prefix calculating.

处理IPv4路由前缀变化链表，计算全部IPv4路由前缀

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) PRC run ended at  Sec = *xxx*, MSec = *yyy*.

PRC计算结束时间

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*xxx*：秒值

·*yyy*：毫秒值

ISIS-* process-id* -SPF: (MT *topoId*) All phases of SPF work completed at  Sec = *xxx*, MSec = *yyy*.

路由计算所有阶段全部完成时间

·*process-id*：进程号

·*topoId*：拓扑号

·*xxx*：秒值

·*yyy*：毫秒值

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Exceeded SPF slice time while processing IPV4 PRC.

处理IP前缀路由计算时超过了IS-IS路由计算分片时间

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Number of IPV4 routes exceed limit!

路由条数超过规格限制

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Processing full prefix calculating.

处理全部前缀计算

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS-* process-id* -SPF: (MT *topoId*)(L *sysLevel*) Exceeded SPF slice time when full processing prefix calculating

处理全部前缀计算时间到达限制

·*process-id*：进程号

·*topoId*：拓扑号

·*sysLevel*：系统级别

ISIS- *process-id* -SPF: (MT *topoId*) Sync route*acction* *ipPrefix* / *subMask*  to rib

同步路由到路由表

·*topoId*：拓扑号

·*action*：添加，删除或修改路由

·*ipPrefix*：IP地址前缀

·*subMask*：子网掩码

(MT *topoId*)(L *sysLevel*) Deleted route *ipPrefix* / *subMask*  PIC backup flag in source *sourceId*.

删除PIC备份标记

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*ipPrefix*：IP地址前缀

·*subMask*：子网掩码

·*sourceId*：源系统ID

(MT *topoId*)(L *sysLevel*) Deleted PIC backup flag in source *sourceId* while route *ipPrefix* / *subMask* was deactivated.

当原路由无效时，删除PIC备份标记

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*ipPrefix*：IP地址前缀

·*subMask*：子网掩码

·*sourceId*：源系统ID

(MT *topoId*)(L *sysLevel*) Added route to RIB with relay NIB ID *nibId*, destination: *ipPrefix*.

添加路由信息至RIB

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*nibId*：NIB ID

·*ipPrefix*：IP地址前缀

(MT *topoId*)(L *sysLevel*) Modified route to RIB with relay NIB ID *nibId*, destination: *ipPrefix*.

修改路由信息至RIB

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*nibId*：NIB ID

·*ipPrefix*：IP地址前缀

(MT *topoId*)(L *sysLevel*) Deleted route to RIB with relay NIB ID *nibId*, destination: *ipPrefix*.

删除路由信息至RIB

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*nibId*：NIB ID

·*ipPrefix*：IP地址前缀

(MT *topoId*)(L *sysLevel*) Deleted relay NIB ID *nibId*, spfnode: *sourceId*, *ipFamily*.

删除NIB ID

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*nibId*：NIB ID

·*sourceId*：源系统ID

·*ipFamily*：IP地址族

(MT *topoId*)(L *sysLevel*) Added relay NIB ID *nibId*, spfnode: *sourceId*, *ipFamily*.

添加NIB ID

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*nibId*：NIB ID

·*sourceId*：源系统ID

·*ipFamily*：IP地址族

(MT *topoId*)(L *sysLevel*) Modified relay NIB ID *nibId*, spfnode: *sourceId*, *ipFamily*.

修改NIB ID

·*topoId*：拓扑号

·*sysLevel*：系统级别

·*nibId*：NIB ID

·*sourceId*：源系统ID

·*ipFamily*：IP地址族

【举例】

\# Router A与Router B相连，分别在Router A和Router B上配置IS-IS功能，建立Level-1-2邻居。在Router A上打开路由计算调试信息开关。

\<RouterA\> debugging isis spf verbose

\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: SPF link (MT0)(L1) Deleting link 0000.0000.0004.05 \--\> 0000.0000.0004.00 Cost:0

\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: SPF node (MT0)(L1) Deleting system 0000.0000.0004.05

\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Trigger SPF at  Sec = 23961, MSec = 527

\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) SPF old scheduled event: 0x00000000, new trigger event: 0x00000002.

\*Apr  8 13:25:27:527 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) SPF event 0x00000002 is scheduled.

\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

*// 删除Level1的Link和SPF节点，触发路由计算*

ISIS-13-SPF: SPF link (MT0)(L2) Deleting link 0000.0000.0004.05 \--\> 0000.0000.0004.00 Cost:0

\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: SPF node (MT0)(L2) Deleting system 0000.0000.0004.05

\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Trigger SPF at  Sec = 23961, MSec = 528

\*Apr  8 13:25:27:528 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) SPF old scheduled event: 0x00000002, new trigger event: 0x00000002.

*// 删除Level2的Link和SPF节点，触发路由计算*

\*Apr  8 13:25:27:571 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) Deleting prefix for 10.152.1.0/255.255.255.0, from forwarding table.

\*Apr  8 13:25:27:571 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) Deleting prefix for 10.152.1.0/255.255.255.0, from forwarding table.

\*Apr  8 13:25:33:892 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) Adding prefix for 10.152.1.0/255.255.255.0 from 0000.0000.0004.00, into forwarding table.

\*Apr  8 13:25:33:892 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Trigger SPF at  Sec = 23967, MSec = 892

\*Apr  8 13:25:33:892 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) SPF old scheduled event: 0x00000002, new trigger event: 0x00000008.

\*Apr  8 13:25:33:892 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) SPF event 0x0000000A is scheduled.

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) SPF Event:0xa, running Flag, old: 0, current: 0x16.

*// 删除Level1的IP路由前缀，触发路由计算*

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) I-SPF run started at  Sec = 23971, MSec = 529 .

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: Checking changed links.

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: SPF link (MT0)(L1) Destroy LINK 0000.0000.0004.05 \--\> 0000.0000.0004.00 Del

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: Need rebuild SPT.

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) Running full SPF.

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Begin Level-1 SPF from root node.

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) SPF node Node is added into SPT. 1000.0001.0003.00 Dist:0 Nexthops:0 Nbrs:1 Parents:0 Tree

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: SPF link (MT0)(L1) Check the link to one nbr. 1000.0001.0003.00 \--\> 0000.0000.0004.07 AttAdjs:1

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF:  New distance is 10.

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF:  Less cost, add node to TENT HEAP.

\*Apr  8 13:25:37:529 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) SPF node Son node update to TENT list 0000.0000.0004.07 Dist:10 Nexthops:0 Nbrs:2 Parents:0 Tent Direct     ;

ISIS-13-SPF: SPF link (MT0)(L1) Check the link to one nbr. 0000.0000.0004.07 \--\> 1000.0001.0003.00 AttAdjs:1 Back

\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: Link is backard link, ignore.

\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) SPF node Node is added into SPT. 0000.0000.0004.00 Dist:10 Nexthops:0 Nbrs:1 Parents:1 Tree

\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Merge nexthop from root node IPV4:1/1

\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Merge nexthop from parent node IPV4:0

ISIS-13-SPF: Inform SPF nodes change to PAC&PRC.

\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) SPF node Destroy node 0000.0000.0004.05 Dist:4294967295 Nexthops:0 Nbrs:0 Parents:0 Direct Del

\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) I-SPF run ended at  Sec = 23971, MSec = 530 .

\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) I-SPF run started at  Sec = 23971, MSec = 530 .

\*Apr  8 13:25:37:530 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: Checking changed links.

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: SPF link (MT0)(L2) Destroy LINK 0000.0000.0004.05 \--\> 0000.0000.0004.00 Del

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: Need rebuild SPT.

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) Running full SPF.

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Begin Level-2 SPF from root node.

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) SPF node Node is added into SPT. 1000.0001.0003.00 Dist:0 Nexthops:0 Nbrs:1 Parents:0 Tree

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: SPF link (MT0)(L2) Check the link to one nbr. 1000.0001.0003.00 \--\> 0000.0000.0004.07 AttAdjs:1

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) SPF node  NBR node found. 0000.0000.0004.07 Dist:4294967295 Nexthops:0 Nbrs:2 Parents:0 Direct

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF:  New distance is 10.

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF:  Less cost, add node to TENT HEAP.

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) SPF node Son node update to TENT list 0000.0000.0004.07 Dist:10 Nexthops:0 Nbrs:2 Parents:0 Tent Direct

\*Apr  8 13:25:37:531 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: SPF link (MT0)(L2) Check the link to one nbr. 0000.0000.0004.07 \--\> 1000.0001.0003.00 AttAdjs:1 Back

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: Link is backard link, ignore.

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) SPF node Node is added into SPT. 0000.0000.0004.00 Dist:10 Nexthops:0 Nbrs:1 Parents:1 Tree

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Merge nexthop from root node IPV4:1/1

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Merge nexthop from parent node IPV4:0

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: Inform SPF nodes change to PAC&PRC.

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) SPF node Destroy node 0000.0000.0004.05 Dist:4294967295 N

exthops:0 Nbrs:0 Parents:0 Direct Del

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) I-SPF run ended at  Sec = 23971, MSec = 532 .

*// 进行Level1和Level2的ISPF计算*

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) AREA run started at  Sec = 23971, MSec = 532 .

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) Processing increment area address calculating.

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) Area Addr: 32 is available.

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) AREA run ended at  Sec = 23971, MSec = 532 .

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) AREA run started at  Sec = 23971, MSec = 532 .

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) Processing increment area address calculating.

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) Area Addr: 32 is available.

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) AREA run ended at  Sec = 23971, MSec = 532 .

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) Updating computed areas into L2 LSDB.

*// 进行Level1和Level2的区域地址计算*

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) PRC run started at  Sec = 23971, MSec = 532 .

\*Apr  8 13:25:37:532 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) Processing increment IPV4 prefix calculating.

\*Apr  8 13:25:37:533 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L1) PRC run ended at  Sec = 23971, MSec = 533 .

\*Apr  8 13:25:37:544 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) PRC run started at  Sec = 23971, MSec = 544 .

\*Apr  8 13:25:37:544 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) Processing increment IPV4 prefix calculating.

\*Apr  8 13:25:37:544 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0)(L2) PRC run ended at  Sec = 23971, MSec = 544 .

*// 进行Level1和Level2的Prc计算*

\*Apr  8 13:25:37:544 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-13-SPF: (MT0) All phases of SPF work completed at  Sec = 23971, MSec = 544

*// 路由计算所有阶段完成*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis timer**

------------------------------------------------------------------------

【命令】

**[debuging isis timer** [ *process-id* ]]

**[undo debuging isis timer** [ *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【描述】

**[debuging isis timer**]命令用来打开IS-IS定时器调试信息开关。**undo debugging isis timer**命令用来关闭IS-IS定时器调试信息开关。

缺省情况下，IS-IS定时器调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的定时器调试信息开关。

表1-9 debugging isis timer命令输出信息描述表

字段

描述

ISIS-*procId*-TMR: *adjLevel* adjacency *systemId* hold timer expired on the circuit *circuitName.*

hold time定时器超时

·*process-id*：进程号

·*adjLevel*：邻居类型，取值为L1或L2

·*systemId*：邻居system id

·*circuitName*：接口名

ISIS-*procId*-TMR: *adjLevel* hello timer expired on the circuit *circuitName*.

Hello定时器超时

·*process-id*：进程号

·*adjLevel*：邻居类型，取值为L1或L2

·*circuitName*：接口名

ISIS-*procId*-TMR: Starting waiting timer for max seq num exceed, time value is *timer* ms.

LSP序列号反转处理的定时器启动

·*procId*：IS-IS进程号

·*timer*：LSP序列号反转需要等待的处理时间秒数（LSP老化时间+LSP删除时间）

ISIS-*procId*-TMR: *lspLevel* LSP *lspId*gen timer expired

LSP生成定时器超时

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型，取值为L1或L2

·*lspId*：LSPID

ISIS-*procId*-TMR: Start *lspLevel* LSP *lspid* gen timer, time vlaue is *Second*(ms)

启动LSP生成时间间隔定时器

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型，取值为L1或L2

·*lspid*：LSPID

·*Second*：Lsp生成定时器的当前时间间隔

ISIS-*procId*-TMR: Stop *lspLevel* LSP *lspid * gen timer

关闭LSP生成时间间隔定时器

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型，取值为L1或L2

·*lspid*：LSPID

ISIS-*procId*-TMR: *lspLevel* flood timer expired on the circuit *circuitName*

LSP报文发送定时器超时

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型，取值为L1或L2

·*circuitName*：接口名

ISIS-*procId*-TMR: *lspLevel* fast flood timer expired

LSP快速扩散定时器超时

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型，取值为L1或L2

ISIS-*procId*-TMR: *lspLevel* csnp timer expired on the circuit *circuitName*

CSNP报文发送定时器超时

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型，取值为L1或L2

·*circuitName*：接口名

ISIS-*procId*-TMR: *lspLevel* psnp timer expired on the circuit *circuitName*

PSNP报文发送定时器超时

·*procId*：IS-IS进程号

·*lspLevel*：LSP类型，取值为L1或L2

·*circuitName*：接口名

ISIS-*procId*-TMR: (MT*mtIId*) Stop SPF timer.

关闭SPF定时器停止SPF计算调度

·*procId*：IS-IS进程号

·*mtIId*：拓扑号

ISIS-*procId*-TMR: (MT*mtIId*) SPF timer expired.

关闭SPF定时器超时

·*procId*：IS-IS进程号

·*mtIId*：拓扑号

【举例】

\# Router A与Router B相连，在Router A上创建IS-IS进程，路由器类型为**level-1**，并在GigabitEthernet1/0/2上使能IS-IS功能，接口的IP地址为1.1.1.166/24；在Router B上创建IS-IS进程，SystemID为FFFF.FFFF.FFFF、路由器类型为**level-1**，并在GigabitEthernet1/0/1使能IS-IS功能，接口的IP地址为1.1.1.2/24；Router A与Router B在同一个区域49。在Router A上打开IS-IS定时器调试信息开关。

\<RouterA\> debugging isis timer

\*Apr  8 22:04:12:389 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-TMR: Level-1 hello timer expired on the circuit GigabitEthernet1/0/2.

\*Apr  8 22:04:15:039 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-TMR: Level-2 hello timer expired on the circuit GigabitEthernet1/0/2.

*[// Level-1*]*的邻居邻接超时，Level-2的邻居邻接超时*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging isis update-packet**

------------------------------------------------------------------------

【命令】

**[debugging**[ **isis** **update-packet** [ **receive** \| **send** ]  **verbose**  *process-id* ]]

**[undo**[ **debugging** **isis** **update-packet** [ **receive** \| **send** ]  **verbose**  *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：表示接收LSP报文调试信息开关。

**[send**]：表示发送LSP报文调试信息开关。

**[verbose**]：表示LSP报文详细调试信息开关。

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【描述】

**[debugging isis**]命令用来打开IS-IS LSP报文的调试信息开关。**undo debugging isis**命令用来关闭IS-IS LSP报文的调试信息开关。

缺省情况下，IS-IS LSP报文的调试信息开关处于关闭状态。

如果未指定进程号，则打开所有IS-IS进程的LSP报文的调试信息开关。

表1-10 debugging isis update-packet命令输出信息描述表

字段

描述

ISIS-*processId*-UPDT: PDU level(*pduLevel*) mismatch with circuit level(*circuitLevel*)

接收到的LSP/SNP报文的Level和接口Level不匹配

·*processId*：IS-IS进程ID

·*pduLevel*：LSP/SNP报文的Level

·*circuitLevel*：接口Level

ISIS-*processId*-UPDT: Lsp with more than three area addr(es)

LSP报文中携带的区域地址个数多于3个

·*processId*：IS-IS进程ID

ISIS-*processId*-UPDT: Receive *pduName* lspid=*systemId*. *pseudonodeNumber*-*lspNumber* seq=*lspSequenceNumber* ht=*holdTime* from snpa *mac-address* on circuit *circuitName*

接收到LSP报文

·*processId*：IS-IS进程ID

·*pduName*：L1 LSP/L2 LSP

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

·*lspSequenceNumber*：LSP报文的序列号

·*holdTime*：LSP报文的存活时间

·*mac-address*：LSP报文接收接口的MAC地址

·*circuitName*：LSP报文接收接口名

ISIS-*processId*-UPDT: Snpa address of pdu is the same as the local circuit(*circuitName*)

LSP/SNP报文的源MAC地址和接收接口的MAC一样

·*processId*：IS-IS进程ID

·*circuitName*：LSP/SNP报文接收接口名

ISIS-*processId*-UPDT: ISIS process is under disable, ignoring pdu

ISIS进程处于disable状态, 丢弃LSP/SNP报文

·*processId*：IS-IS进程ID

ISIS-*processId*-UPDT: Circuit(*circuitName*) is not operationally on, ignoring pdu

LSP/SNP报文接收接口处于非工作状态, 丢弃LSP/SNP报文

·*processId*：IS-IS进程ID

·*circuitName*：LSP/SNP报文接收接口名

ISIS-*processId*-UPDT: Circuit(*circuitName*) is silence, ignoring pdu

LSP/SNP报文接收接口处于silence状态, 丢弃LSP/SNP报文

·*processId*：IS-IS进程ID

·*circuitName*：LSP/SNP报文接收接口名

ISIS-*processId*-UPDT: No active adjacency entry with such snpa(*mac-address*) on the cicuit(*circuitName*)

LSP/SNP报文发送端不是接收接口上的活动邻居

·*processId*：IS-IS进程ID

·*mac-address*：LSP/SNP报文发送端MAC地址

·*circuitName*：LSP/SNP报文接收接口名

ISIS-*processId*-UPDT: Parsed area address *areaAddress*

从LSP报文中解析区域地址

·*processId*：IS-IS进程ID

·*areaAddress*：区域地址

ISIS-*processId*-UPDT: Parsed neighbor *neighborSourceId*

从LSP报文中解析邻居

·*processId*：IS-IS进程ID

·*neighborSourceId*：邻居的Source ID

ISIS-*processId*-UPDT: Parsed ip prefix *ipAddressPair*

从LSP报文中解析IP前缀

·*processId*：IS-IS进程ID

·*ipAddressPair*：IP地址地址和掩码长度

ISIS-*processId*-UPDT: (MT *topologyId*) *updateType* *Level* spf node(*nodeSourceId*)

向路由计算模块更新SPF节点

·*processId*： IS-IS进程ID

·*topologyId*：SPF节点所在的拓扑ID

·*updateType*：更新类型（添加/删除/修改）

·*Level*：Level-1/Level-2

·*nodeSourceId*：SPF节点的Source ID

ISIS-*processId*-UPDT: (MT *topologyId*) *updateType* *Level* att route advertised by *advertisednodeSourceId*

向路由计算模块更新默认路由

·*processId*：IS-IS进程ID

·*topologyId*：发布默认路由的SPF节点所在的拓扑ID

·*updateType*：更新类型（添加/删除）

·*Level*：Level-1/Level-2

·*advertisednodeSourceId*：发布默认路由的SPF节点的Source ID

ISIS-*processId*-UPDT: (MT *topologyId*) Update *Level*  area address advertised by *advertisednodeSourceId*

向路由计算模块更新区域地址

·*processId*：IS-IS进程ID

·*topologyId*：发布默认路由的SPF节点所在的拓扑ID

·*Level*：Level-1/Level-2

·*advertisednodeSourceId*：发布默认路由的SPF节点的Source ID

ISIS-*processId*-UPDT: (MT *topologyId*) *updateType* *Level* spf link(*sourceId*-\>*destId*)

向路由计算模块更新SPF Link

·*processId*：IS-IS进程ID

·*topologyId*：发布默认路由的SPF节点所在的拓扑ID

·*updateType*：更新类型（添加/删除）

·*Level*：Level-1/Level-2

·*sourceId*：源Source ID

·*destId*：目的Source ID

ISIS-*processId*-UPDT: (MT *topologyId*) *updateType* *Level*  ip prefix(*ipAddressPair*) advertised by *advertisednodeSourceId*  in tlv type *tlvType*

向路由计算模块更新路由前缀

·*processId*：IS-IS进程ID

·*topologyId*：发布默认路由的SPF节点所在的拓扑ID

·*updateType*：更新类型（添加/删除）

·*Level*：Level-1/Level-2

·*ipAddressPair*：IP路由前缀

·*advertisednodeSourceId*：发布路由前缀的SPF节点的Source ID

·*tlvType*：发布路由前缀的TLV类型

ISIS-*processId*-UPDT: Own lsp *systemId*. *pseudonodeNumber*-*lspNumber* processed, newer than lsdb copy

处理比LSDB中新的本地生成的LSP报文

·*processId*：IS-IS进程ID

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

ISIS-*processId*-UPDT: Other lsp *systemId*. *pseudonodeNumber*-*lspNumber* processed, newer than lsdb copy

处理比LSDB中新的非本地生成的LSP报文

·*processId*：IS-IS进程ID

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

ISIS-*processId*-UPDT: Lsp *systemId*. *pseudonodeNumber*-*lspNumber* processed, older than lsdb copy

处理比LSDB中旧的LSP报文

·*processId*：IS-IS进程ID

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

ISIS-*processId*-UPDT: Lsp *systemId*. *pseudonodeNumber*-*lspNumber* processed, same as lsdb copy

处理和LSDB中新旧一样的LSP报文

·*processId*：IS-IS进程ID

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

ISIS-*processId*-UPDT: Own lsp *systemId*. *pseudonodeNumber*-*lspNumber* processed, no exist in lsdb

处理LSDB中不存在的本地生成的LSP报文

·*processId*：IS-IS进程ID

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

ISIS-*processId*-UPDT: Other lsp *systemId*. *pseudonodeNumber*-*lspNumber* processed, no exist in lsdb

处理LSDB中不存在的非本地生成的LSP报文

·*processId*：IS-IS进程ID

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

ISIS-*processId*-UPDT: *lspContent*

接收到LSP报文

·*processId*：IS-IS进程ID

ISIS-*processId*-UPDT: Lsp seq number is ZERO

发送序列号为0的LSP报文

·*processId*：IS-IS进程ID

ISIS-*processId*-UPDT: Flooding *pduName* *systemId*. *pseudonodeNumber*-*lspNumber* on the circuit *circuitName*

扩散LSP报文

·*processId*：IS-IS进程ID

·*pduName*：L1 LSP/L2 LSP

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

·*circuitName*：扩散接口名

ISIS-*processId*-UPDT: Circuit(*circuitName*) is silence, lsp not sent

接口处于silence状态, LSP不在这个接口上进行扩散

·*processId*：IS-IS进程ID

·*circuitName*：扩散接口名

ISIS-*processId*-UPDT: Send *pduName* lspid=*systemId*. *pseudonodeNumber*-*lspNumber* seq=*lspSequenceNumber* ht=*holdTime* from snpa *mac-address* on circuit *circuitName*

发送LSP报文

·*processId*：IS-IS进程ID

·*pduName*：L1 LSP/L2 LSP

·*systemId*：LSP发送设备的System ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*lspNumber*：LSP报文的分片号

·*lspSequenceNumber*：LSP报文的序列号

·*holdTime*：LSP报文的存活时间

·*mac-address*：LSP报文发送接口的MAC地址

·*circuitName*：LSP报文发送接口名

ISIS-*processId*-UPDT: *lspContent*

发送LSP报文

·*processId*：IS-IS进程ID

【举例】

\# Router A与Router B相连，在Router A上创建IS-IS进程，SystemID为3333.3333.3333、路由器类型为**level-1-2**，并在GigabitEthernet1/0/2上使能IS-IS功能，接口的IP地址为3.3.3.166/24；在Router B上创建IS-IS进程，SystemID为FFFF.FFFF.FFFF、路由器类型为**level-1-2**，并在GigabitEthernet1/0/1使能IS-IS功能，接口的IP地址为3.3.3.89/24；Router A与Router B在同一个区域49。在Router A上打开IS-IS LSP报文调试信息开关。

\<RouterA\> debugging isis update-packet

\*Apr  8 03:39:05:325 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-UPDT: Receive L1 LSP lspid=ffff.ffff.ffff.00-01 seq=0x00000002 ht=1061 from snpa 0000-5e14-0200 on circuit GigabitEthernet1/0/2

\*Apr  8 03:39:06:051 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-UPDT: Receive L2 LSP lspid=ffff.ffff.ffff.00-01 seq=0x00000002 ht=1059 from snpa 0000-5e14-0200 on circuit GigabitEthernet1/0/2

*// 在接口GigabitEthernet1/0/2上接收到Level-1 lspid=ffff.ffff.ffff.00-01的LSP报文和Level-2 lspid=ffff.ffff.ffff.00-01的LSP报文*

\*Apr  8 03:39:10:571 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-UPDT: Flooding L2 LSP 3333.3333.3333.00-00 on the circuit GigabitEthernet1/0/2

\*Apr  8 03:39:10:571 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-UPDT: Flooding L1 LSP 3333.3333.3333.00-00 on the circuit GigabitEthernet1/0/2

\*Apr  8 03:39:10:601 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-UPDT: Send L1 LSP lspid=3333.3333.3333.00-00 seq=0x00000004 ht=1199 from snpa 0000-0e16-0200 on circuit GigabitEthernet1/0/2

\*Apr  8 03:39:10:601 2011 RouterA ISIS/7/ISISDBG: -MDC=1;

ISIS-1-UPDT: Send L2 LSP lspid=3333.3333.3333.00-00 seq=0x00000004 ht=1199 from snpa 0000-0e16-0200 on circuit GigabitEthernet1/0/2

*// 在接口GigabitEthernet1/0/2上发送Level-1 lspid=3333.3333.3333.00-00的LSP报文和Level-2 lspid=3333.3333.3333.00-00的LSP报文*

**IS-IS调试命令 \-- IS-IS调试命令 \-- debugging osi**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging osi**]

**[undo debugging osi**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging osi ** **slot** ]slot-number{.commandparameterChar}

**[undo debugging osi** [ **slot** ]slot-number ]{.commandparameterChar}

分布式设备－独立运行模式/集中式IRF设备：

**[debugging osi** [ **chassis** ]chassis-number]{.commandparameterChar} **slot** *slot-number*

**[undo debugging osi** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：单板所在的槽位号。如果未指定本参数，将打开所有单板OSI连接的报文调试信息开关。（分布式设备－独立运行模式）

**[slot ***slot-number*]：设备在IRF中的成员编号。如果未指定本参数，将打开所有成员设备OSI连接的报文调试信息开关。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将打开所有成员设备/PEX的OSI连接的报文调试信息开关。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将打开所有成员设备上所有单板OSI连接的报文调试信息开关。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或者PEX所在的槽位号。如果未指定本参数，将打开所有单板OSI连接的报文调试信息开关。（分布式设备－IRF模式）（支持IRF3的设备）

【描述】

**[debugging osi**]命令用来打开OSI连接的报文调试信息开关。**undo debugging osi**命令用来关闭OSI连接的报文调试信息开关。

缺省情况下，OSI连接的报文调试信息开关处于关闭状态。

表1-11 debugging osi命令输出信息描述表

字段

描述

OSI Input

接收报文

OSI Output

发送报文

IN IF

接收报文的入接口

OUT IF

发送报文的出接口

Packet Length

报文的长度

DstMac

报文的目的MAC地址

First 32 bytes

报文的前32字节内容

The packet is dropped(Service slot is invalid)

没有OSI连接时，接收到的报文因为没有业务板处理而被丢弃

The packet is dropped(No match mac found)

接收到的报文因为MAC地址匹配失败而被丢弃

【举例】

\# Router A与Router B相连，分别在Router A和Router B上配置IS-IS功能。在Router A上打开OSI连接报文调试信息开关。

\<RouterA\> debugging osi

\*Nov  7 14:34:14:913 2012 RouterA SOCKET/7/OSI: -MDC=1-Slot=2;

OSI Input:

 IN IF = GigabitEthernet1/0/1, Packet Length = 1497

 DstMac = 0180-c200-0014

 First 32 bytes:

 831b0106 0f010000 01000000 00000200

 1e05d940 00000000 00010101 02011084

\*Nov  7 14:34:14:913 2012 RouterA SOCKET/7/OSI: -MDC=1;

OSI Input:

 IN IF = GigabitEthernet1/0/1, Packet Length = 1497

 DstMac = 0180-c200-0014

 First 32 bytes:

 831b0106 0f010000 01000000 00000200

 1e05d940 00000000 00010101 02011084

\*Nov  7 14:34:16:854 2012 RouterA SOCKET/7/OSI: -MDC=1;

OSI Output:

 OUT IF = GigabitEthernet1/0/1, Packet Length = 1497

 DstMac = 0180-c200-0014

 First 32 bytes:

 831b0106 0f010000 01000000 00000100

 1e05d940 00000000 00010101 02011084

*// 在接口GigabitEthernet1/0/1上接收和发送报文，报文长度为1497，目的MAC地址为0180-c200-0014*

