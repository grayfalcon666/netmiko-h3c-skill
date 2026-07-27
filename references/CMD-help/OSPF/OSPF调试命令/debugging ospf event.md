<!-- CMD-INDEX
  debugging ospf event                | 用户视图             | L12
  debugging ospf lsa                  | 用户视图             | L532
  debugging ospf non-stop-routing     | 用户视图             | L860
  debugging ospf packet               | 用户视图             | L934
  debugging ospf policy               | 用户视图             | L1344
  debugging ospf redistribute         | 用户视图             | L1652
  debugging ospf spf                  | 用户视图             | L2008
  debugging ospf timer                | 用户视图             | L3244
-->

**OSPF \-- OSPF调试命令 \-- debugging ospf event**

------------------------------------------------------------------------

【命令】

**[debugging** **ospf** [ *process-id*  **event** [ **bfd** \| **error** \| **graceful-restart** \| **interface** \| **neighbor** ]]]

**[undo** **debugging** **ospf** [ *process-id*  **event** [ **bfd** \| **error** \| **graceful-restart** \| **interface** \| **neighbor** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

**[bfd**]：表示OSPF与BFD联动调试信息开关。

**[error**]：表示OSPF错误事件调试信息开关。

**[graceful**-restart]：表示平滑重启调试信息开关。

**[interface**]：表示接口事件调试信息开关。

**[neighbor**]：表示OSPF邻居事件调试信息开关。

【描述】

**[debugging ospf event**]命令用来打开OSPF事件调试信息开关。**undo debugging ospf event**命令用来关闭OSPF事件调试信息开关。

缺省情况下，OSPF事件调试信息开关处于关闭状态。

如果未指定进程号，则显示所有OSPF进程的事件调试信息。

表1-1 debugging ospf event bfd命令输出信息描述表

字段

描述

BFD service connected, smooth all session

BFD进程连接，开始平滑会话

BFD service disconnected, clear all session

BFD进程断开连接，清除本地保存的BFD信息

Receive BFD event *bfd-event*

接受到BFD进程发送的事件：

·*bfd-event*：BFD事件类型

Notify BFD smooth stop

通知BFD进程会话平滑结束

Create BFD session for OSPF *process-id*, *interface-name*, nbr *nbr-id*, src *src-ip-address*, dst *dst-ip-address*

通知BFD进程创建会话：

·*process*-id：进程ID

·*interface*-name：接口名

·*nbr-id*：邻居的路由器ID

·*src-ip-address*：BFD会话源地址

·*dst-ip-address*：BFD会话目的地址

Delete BFD session for OSPF *process-id*, *interface-name*, nbr *nbr-id*, src *src-ip-address*, dst *dst-ip-address*

通知BFD进程删除会话：

·*process*-id：进程ID

·*interface*-name：接口名

·*nbr-id*：邻居的路由器ID

·*src-ip-address*：BFD会话源地址

·*dst-ip-address*：BFD会话目的地址

Disable BFD session for OSPF *process-id*, *interface-name*, nbr *nbr-id*, src *src-ip-address*, dst *dst-ip-address*

通知BFD进程去使能会话：

·*process*-id：进程ID

·*interface*-name：接口名

·*nbr-id*：邻居的路由器ID

·*src-ip-address*：BFD会话源地址

·*dst-ip-address*：BFD会话目的地址

Total *num* OSPF process under GR

BFD进程连接时收集正在进行GR的OSPF进程

·*num*：正在进行GR的OSPF进程数量

OSPF *process-id* exit GR, reserved *num* OSPF process under GR

OSPF进程退出GR

·*process-id*：进程ID

·*num*：正在进行GR的OSPF进程数量

表1-2 debugging ospf event error命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

OSPF received packet having conflicted Router ID : *rt-id*

OSPF收到了Router ID冲突的报文：

·*rt-id*：邻居的Router ID

Received short IP packet  (*ip-pkt-len* bytes)

收到包长不正确的IP包：

·*ip-pkt-len*：IP包长

Received short Hello/DD/REQ/UPDATE packet (*ospf-pkt-len* bytes)

收到包长不正确的Hello/DD/REQ/UPDATE包：

·*ospf-pkt-len*：OSPF包长

Received short UPDATE/ACK packet (*ospf-pkt-len* bytes with *ls-count*  LSAs)

收到包长不正确的UPDATE/ACK包：

·*ospf-pkt-len*：OSPF包长

·*ls-count*：包含的LSA个数

Received short IP packet(*ip-pkt-len* bytes) containing *ospf-pkt-len* bytes OSPF data field (type *pkt-type*)

收到包长不正确的IP包，并说明其中OSPF包长：

·*ip-pkt-len*：IP包长

·*ospf-pkt-len*：OSPF包长

·*pkt-type*：包的类型，取值为Hello、DD、REQ、UPDATE、ACK

Received error packet *pkt-type* from interface *interface-type interface-number*

收到错误包：

·*pkt-type*：OSPF包类型，取值为Hello、DD、REQ、UPDATE、ACK

·*Interface-type interface-number*：接口类型和编号

OSPF received packet having bad authentication type : *auth-type*

OSPF收到包含错误认证类型的包：

·*auth-type*：OSPF包认证类型，取值为0表示无认证、为1表示认证方式为Simple认证、为2表示认证方式为MD5

OSPF received packet having bad authentication key

OSPF收到错误认证码的包

表1-3 debugging ospf event graceful-restart命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

nonstandard GR started for OSPF router

开始执行非标准GR

IETF GR started for OSPF router

开始执行IETF GR

created GR interval timer,timeout interval is *num*(s)

创建GR间隔定时器

·*num*：定时器间隔

deleted GR interval timer

删除GR间隔定时器

GR interval timer fired

GR间隔定时器超时

created GR wait timer,timeout interval is *num*(s)

创建GR等待定时器

·*num*：定时器间隔

deleted GR wait timer

删除GR等待定时器

GR wait timer fired

GR等待定时器超时

generate LSAs start

开始生成LSA

generate LSAs end

生成LSA结束

Flush stale area LSAs

老化AS内部LSA

Flush stale ASE and NSSA LSAs

老化AS外部LSA

*[(vlink) *neighbor : *nbr-id*,exit Restart reason : *reason*]

邻居退出GR Restart

·*nbr-id*：邻居neighbor ID

·*reason*：退出原因

interface: *if-name*,DR or BDR change : old DR:*ip-address*,old BDR: *ip-address*,new DR: *ip-address*,new BDR: *ip-address*.

DR,BDR变化：

·*if-name*：接口名

·*ip-address*：接口的IP地址

interface : *if-name*,exit Restart reason : *reason*.

接口退出Restart

·*reason*：退出原因

area:area-id vlink peer: *nbr-id* exit Restart reason : *reason*

vlink退出Restart

·*nbr-id*：邻居路由器ID

·*area-id*：区域号

·*reason*：退出原因

exit Restart reason : *reason*

退出GR Restart：

·*reason*：退出原因

（*vlink*）neighbor : *nbr-id*,exit Helper reason : *reason*

vlink退出Helper

·*nbr-id*：邻居路由器ID

·*reason*：退出原因

exit Helper Reason : *reason*

退出GR Helper

·*reason*：退出原因

Exit Restart,Reason : *reason*,for neighbor : *nbr-id*

退出GR Restart：

·*reason*：退出原因

·*nbr-id*：邻居路由器ID

Exit Restart,Reason : *reason*,for interface : *if-name*

退出GR Restart：

·*reason*：退出原因

·*if-name*：接口名

Exit Restart,Reason : *reason*

退出GR Restart：

·*reason*：退出原因

Exit Helper,Reason : *reason*,for neighbor : *nbr-id*

退出GR Helper：

·*reason*：退出原因

·*nbr-id*：邻居路由器ID

Exit Helper,Reason : *reason*

退出GR Helper：

·*reason*：退出原因

received new grace LSA from neighbor *nbr-id*

接受到邻居发送的GraceLsa：

·*nbr-id*：邻居路由器ID

received MaxAge grace LSA from neighbor *nbr-id*

接受到邻居发送的MaxAge GraceLsa：

·*nbr-id*：邻居路由器ID

exit IETF GR helper mode for （*vlink*）neighbor *nbr-id*

退出IETF GR Helper：

·*nbr-id*：邻居路由器ID

generated grace LSA for （*vlink*）interface *if-name*

生成GraceLsa：

·*if-name*：接口名

flush MaxAge grace LSA for （*vlink*）interface *if-name*

洪泛GraceLsa：

·*if-name*：接口名

created GR send grace lsa timer,timeout interval is *num*(s)

创建IETF GR GraceLsa发送定时器：

·*num*：定时器间隔

deleted GR send grace lsa timer

删除IETF GR GraceLsa发送定时器

created Grace Period timer for （*vlink*）neighbor *nbr-id*,timeout interval is *num*(s)

创建IETF GR周期定时器：

·*nbr-id*：邻居路由器ID

·*num*：定时器间隔

deleted Grace Period timer for （*vlink*）neighbor *nbr-id*

删除IETF GR周期定时器：

·*nbr-id*：邻居路由器ID

created OOB Progress timer for （*vlink*）neighbor *nbr-id*

创建非标准GR OOB定时器：

·*nbr-id*：邻居路由器ID

deleted OOB Progress timer for （*vlink*）neighbor *nbr-id*

删除非标准GR OOB定时器：

·*nbr-id*：邻居路由器ID

created Resync timer for neighbor *nbr-id*

创建非标准GR同步定时器：

·*nbr-id*：邻居路由器ID

deleted Resync timer for neighbor *nbr-id*

删除非标准GR同步定时器：

·*nbr-id*：邻居路由器ID

exit nonstandard GR helper mode for neighbor *nbr-id*

退出非标准GR Helper模式

·*nbr-id*：邻居路由器ID

GR all helpers completed for OSPF router

与所有GR Helper同步完成

表1-4 debugging ospf event interface命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

Interface *intf-ip* received *intf-event* and its state from *pre-state* -\> *cur-state*

接口状态变化的详细信息：

·*intf-ip*：接口IP地址

·*intf-event*：引起接口状态变化的事件，取值为InterfaceUp、WaitTimer、LoopInd、BackupSeen、NeighborChange、UnloopInd、InterfaceDown

·*pre-state*/*cur-state*：接口状态，取值为Down表示接口处于down、取值为Loopback表示接口是回环状态、Waiting表示接口处于waiting状态、Point-to-point接口连接点到点网络或者通过虚连接、DR表示路由器是DR、Backup表示路由器是BDR、DROther表示路由器非DR且非BDR

表1-5 debugging ospf event neighbor命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

Neighbor *nbr-ip* received *nbr-event* and its state from *original-state* -\> *current-state*

邻居状态变化的详细信息：

·*nbr-ip*：邻居接口IP地址

·*nbr-event*：引起邻居状态变化的事件，取值为HelloReceived、Start、2WayReceived、NegotiationDone、ExchangeDone、BadLSReq、LoadingDone、AdjOK?、1-Way、KillNbr、Inactivity Timer、LLDown

·*original-state*/*current-state*：邻居状态，取值为Down、Attempt、Init、2-Way、ExStart、Exchange、Loading、Full

【举例】

\# Router A通过GigabitEthernet1/0/1（IP地址为150.1.1.1/24）与Router B的GigabitEthernet1/0/1（IP地址为150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router B上创建OSPF进程1，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router A上打开OSPF接口事件调试信息开关。

\<RouterA\> debugging ospf event interface

%Nov  1 10:15:33:767 2012 RouterA IFNET/5/LINK_UPDOWN: -MDC=1;

Line protocol on the interface GigabitEthernet1/0/1 is UP

\*Nov  1 10:15:38:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1: Interface 150.1.1.1 received InterfaceUp and its state from Down -\> Waiting.

*// 接口状态由Down变为Waiting*

\*Nov  1 10:16:18:811 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1: Interface 150.1.1.1 received BackupSeen and its state from Waiting -\> BackupDR.

*// 接口状态由Waiting变为BackupDR*

\# Router A通过GigabitEthernet1/0/1（150.1.1.1/24）与Router B的GigabitEthernet1/0/1（150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router B上创建OSPF进程1，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router A上打开邻居事件调试信息开关。

\<RouterA\> debugging ospf event neighbor

\*Nov  1 10:14:18:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1: Neighbor 150.1.1.2 received KillNbr and its state from Full -\> Down.

\*Nov  1 10:15:48:098 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1: Neighbor 150.1.1.2 received HelloReceived and its state from Down -\> Init.

\*Nov  1 10:15:48:098 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1: Neighbor 150.1.1.2 received 2WayReceived and its state from Init -\> 2Way.

\*Nov  1 10:16:13:811 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1: Neighbor 150.1.1.2 received AdjOk? and its state from 2Way -\> ExStart.

\*Nov  1 10:16:18:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1: Neighbor 150.1.1.2 received NegotiationDone and its state from ExStart -\> Exchange.

\*Nov  1 10:16:18:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1: Neighbor 150.1.1.2 received ExchangeDone and its state from Exchange -\> Loading.

\*Nov  1 10:16:18:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1: Neighbor 150.1.1.2 received LoadingDone and its state from Loading -\> Full.

*[// OSPF*]*进程1与邻居150.1.1.2建立邻接关系的全过程*

**OSPF \-- OSPF调试命令 \-- debugging ospf lsa**

------------------------------------------------------------------------

【命令】

**[debugging** **ospf** [ *process-id*  **lsa** [ { **generate** \| **install** } [ **filter** { **ase** \| **opaque-as** \| [ **area** *area-id* ] { **asbr** \| **network** \| **nssa** \| **opaque-area** \| **opaque-link** \| **router** \| **summary** }   *link-state-id*  } ] ] ]]

**[undo** **debugging** **ospf** [ *process-id*  **lsa** [ { **generate** \| **install** } [ **filter** ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

**[generate**]：表示LSA生成调试信息开关。

**[install**]：表示LSA安装到LSDB库中的调试信息开关。

**[filter**]：表示打开过滤LSA的调试信息开关。

**[area** *area-id*]：表示数据库中指定区域的调试信息开关。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式*。*如果未指定本参数，将打开所有区域的调试信息开关。

**[asbr**]：表示ASBR Summary LSA的调试信息开关。

**[ase**]：表示AS External LSA的调试信息开关。

**[network**]：表示Network LSA的调试信息开关。

**[nssa**]：表示NSSA External LSA的调试信息开关。

**[opaque-area**]：表示Opaque-area LSA的调试信息开关。

**[opaque-as**]：表示Opaque-AS LSA的调试信息开关。

**[opaque-link**]：表示Opaque-link LSA的调试信息开关。

**[router**]：表示Router LSA的调试信息开关。

**[summary**]：表示Network Summary LSA的调试信息开关。

*[link-state-id*]：链路状态ID，IP地址格式。

【描述】

**[debugging ospf lsa**]命令用来打开OSPF LSA调试信息开关。**undo debugging ospf lsa**命令用来关闭OSPF LSA调试信息开关。

缺省情况下，OSPF LSA调试信息开关处于关闭状态。

如果未指定进程号，则显示所有OSPF进程的LSA调试信息。

表1-6 debugging ospf lsa命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

*[op-type*] LSA at x ms

对LSA进行操作：

·*op-type*：表示对LSA进行何种操作，取值为Generate表示生成LSA，Install表示安装LSA

LSA type: *ls-type* Link state ID: *link-state-id*

Advertising router*: rt-id*

LSA 头部信息：

·*ls-type*：LSA类型，*LSA-type*的取值为1表示Router LSA、2为network LSA、3为net-summary LSA、4为ASBR-summary LSA、5为AS-external --LSA、7为NSSA LSA、9/10/11为Opaque LSA

·*link-state-id*：LSA 标识

·*rt-id*：生成LSA 的路由器的标识

LSA age: *age*  Options : External routing: *ON/OFF*

LSA 头部信息：

·*age*：LSA年龄字段

·*ON/OFF*：表示支持或不支持外部路由

Length: *ls-len * Sequence number: *seq-num* Checksum:*checksum*

LSA头部信息；

·*Ls-len*：LS长度

·*Seq-num*：LS序列号

·*Checksum*：除LSA age字段外整个LSA的校验和

Capabilities: VBit: EBit: BBit: NtBit: Link count: *link-count* TOS# *tos-num*  Metric *cost*

Router LSA的内容：

·*VBit*：0x40，表示virtual link

·*EBit*：0x200，表示Exteranl LSA

·*BBit*：0x100，表示ABR

·NtBit：0x1000，表示该路由器无条件进行了Type-7 LSA到Type-5 LSA的转换

·*Link-count*：Router LSA描述的链路数

·*tos-num*：Router LSA中的TOS数

·*cost*：链路代价

Network mask: *net-mask* Neighbor router: *rt-id*

Network LSA内容：

·*net-mask*：网段掩码

·*rt-id*：路由器发现的邻居的标识符

Network mask: *net-mask* Metric: *cost*

Summary, ASBR-Summary LSA内容：

·*net-mask*：网段掩码

·*cost*：链路代价

Network mask: *net-mask* TOS: *tos* Metric: *cost* Forwarding address: *fwd-addr* External route tag: *rt-tag*

AS_External LSA, NSSA LSA内容：

·*net-mask*：网段掩码

·*tos*：服务类型

·*cost*：链路代价

·*fwd-addr*：转发地址

·*rt-tag*：外部路由标志

【举例】

\# Router A通过GigabitEthernet1/0/1（150.1.1.1/24）与Router B的GigabitEthernet1/0/1（150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router B上创建OSPF进程1，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router A上打开LSA安装到LSDB库中的调试信息开关。

\<RouterA\> debugging ospf lsa install

\<RouterA\>

\*Sep  8 17:51:02:234 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4796222 ms:

\*Sep  8 17:51:02:244 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.

\*Sep  8 17:51:02:244 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 201.1.1.1.

\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 201.1.1.1.

\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.

\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000008 CheckSum: 60445.

\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 512 BBit: 0 NtBit: 0 Link count: 1.

\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.0 LinkData: 255.255.2 55.0 LinkType: 3.

\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.

*[// OSPF*]*进程1安装由自己生成的Router-LSA*

\*Sep  8 17:51:06:766 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4800748 ms:

\*Sep  8 17:51:06:766 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.

\*Sep  8 17:51:06:766 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 202.1.1.1.

\*Sep  8 17:51:06:776 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 202.1.1.1.

\*Sep  8 17:51:06:776 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 5 Options: ExRouting:ON.

\*Sep  8 17:51:06:776 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000001 CheckSum: 5373.

\*Sep  8 17:51:06:776 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 512 BBit: 256 NtBit: 0 Link count: 1.

\*Sep  8 17:51:06:786 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.0 LinkData: 255.255.255.0 LinkType: 3.

\*Sep  8 17:51:06:786 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.

*[// OSPF*]*进程1安装由对端生成的Router-LSA*

\*Sep  8 17:51:06:786 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4800748 ms:

\*Sep  8 17:51:06:806 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 2.

\*Sep  8 17:51:06:806 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 150.1.1.1.

\*Sep  8 17:51:06:806 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 201.1.1.1.

\*Sep  8 17:51:06:806 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.

\*Sep  8 17:51:06:816 2006 RouterA OSPF/6/OSPFDEBUG:Length: 32 Seq# 80000001 CheckSum: 2890.

\*Sep  8 17:51:06:816 2006 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0.

\*Sep  8 17:51:06:816 2006 RouterA OSPF/6/OSPFDEBUG:Neighbor router: 202.1.1.1.

\*Sep  8 17:51:06:826 2006 RouterA OSPF/6/OSPFDEBUG:Neighbor router: 201.1.1.1.

*// 由于本端是DR，OSPF进程1安装由自己生成的Network-LSA*

\*Sep  8 17:51:07:238 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4801229 ms:

\*Sep  8 17:51:07:238 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.

\*Sep  8 17:51:07:238 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 201.1.1.1.

\*Sep  8 17:51:07:248 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 201.1.1.1.

\*Sep  8 17:51:07:248 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.

\*Sep  8 17:51:07:248 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000009 CheckSum: 34281.

\*Sep  8 17:51:07:258 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 512 BBit: 0 NtBit: 0 Link count: 1.

\*Sep  8 17:51:07:258 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.1 LinkData: 150.1.1.1 LinkType: 2.

\*Sep  8 17:51:07:258 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.

*[// OSPF*]*进程1安装由自己生成的Router-LSA。其中的stub link变为transit link*

\*Sep  8 17:51:11:710 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4805705 ms:

\*Sep  8 17:51:11:720 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.

\*Sep  8 17:51:11:720 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 202.1.1.1.

\*Sep  8 17:51:11:720 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 202.1.1.1.

\*Sep  8 17:51:11:720 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 1 Options: ExRouting:ON.

\*Sep  8 17:51:11:731 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000002 CheckSum: 47803.

\*Sep  8 17:51:11:731 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 512 BBit: 256 NtBit: 0 Link count: 1.

\*Sep  8 17:51:11:731 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.1 LinkData: 150.1.1.2 LinkType: 2.

\*Sep  8 17:51:11:741 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.

*[// OSPF*]*进程1安装对端的Router-LSA。其中的stub link变为transit link*

\*Sep  8 18:00:27:660 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 5361645 ms:

\*Sep  8 18:00:27:660 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 5.

\*Sep  8 18:00:27:670 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 123.1.1.0.

\*Sep  8 18:00:27:670 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 201.1.1.1.

\*Sep  8 18:00:27:670 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.

\*Sep  8 18:00:27:680 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000001 CheckSum: 25377.

\*Sep  8 18:00:27:680 2006 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0.

\*Sep  8 18:00:27:680 2006 RouterA OSPF/6/OSPFDEBUG:TOS: 128 Metric: 001 Forwarding address  0.0.0.0 External route tag 0.0.0.1.

*[// OSPF*]*进程1安装5类LSA，对应引入路由为123.1.1.0 255.255.255.0*

\# Router A通过GigabitEthernet1/0/1(150.1.1.1/24)与Router B的GigabitEthernet1/0/1(150.1.1.2/24)相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在GigabitEthernet1/0/1接口上使能OSPF功能并配置其属于区域0；在Router B上创建OSPF进程1，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router A上打开LSA生成调试信息开关。

\<RouterA\> debugging ospf lsa generate

\<RouterA\>

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Generate LSA at 6352610 ms:

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 1.1.1.1.

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 1.1.1.1.

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 8000002c CheckSum:  3185.

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 0 BBit: 0 NtBit: 0 Link count: 1.

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.0 LinkData: 255.255.255.0 LinkType: 3.

\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.

*// 生成Router LSA*

%Dec 12 11:07:33:708 2006 RouterA RM/3/RMLOG:OSPF-NBRCHANGE: Process 1, Neighbour 150.1.1.2(GigabitEthernet1/0/1) from Loading to Full

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Generate LSA at 6357625 ms:

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 1.1.1.1.

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 1.1.1.1.

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 8000002d CheckSum: 44595.

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 0 BBit:  0 NtBit: 0 Link count: 1.

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.2 LinkData: 150.1.1.1 LinkType: 2.

\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.

*// 邻居FULL之后生成Router LSA*

**OSPF \-- OSPF调试命令 \-- debugging ospf non-stop-routing**

------------------------------------------------------------------------

【命令】

**[debugging** **ospf** [ *process-id*  **non-stop-routing**]]

**[undo** **debugging** **ospf** [ *process-id*  **non-stop-routing**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

【描述】

**[debugging ospf non-stop-routing**]命令用来打开OSPF NSR调试信息开关。**undo debugging ospf non-stop-routing**命令用来关闭OSPF NSR调试信息开关。

缺省情况下，OSPF NSR调试信息开关处于关闭状态。

如果未指定进程号，则显示所有OSPF进程的NSR调试信息。

表1-7 debugging ospf non-stop-routing命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

begin to backup configuration data\...

开始批备配置数据

begin to backup running data\...

开始批备运行数据

begin to backup lsa data\...

开始批备LSA数据

【举例】

\# Router A开始进行主备倒换，在Router A上打开OSPF NSR的调试信息开关。

\<RouterA\> debugging ospf non-stop-routing

\<RouterA\>

\*Dec 13 04:47:30:586 2012 RouterA  OSPF/7/DEBUG: -MDC=1; OSPF 1 begin to backup configuration data\...

*[// OSPF*]*进程1开始批备配置数据*

\*Dec 13 04:47:30:590 2012 RouterA OSPF/7/DEBUG: -MDC=1; OSPF 1 begin to backup running data\...

*[// OSPF*]*进程1开始批备运行数据*

\*Dec 13 04:47:30:590 2012 RouterA OSPF/7/DEBUG: -MDC=1; OSPF 1 begin to backup lsa data\...

*[// OSPF*]*进程1开始批备LSA数据*

**OSPF \-- OSPF调试命令 \-- debugging ospf packet**

------------------------------------------------------------------------

【命令】

**[debugging** **ospf** [ *process-id*  **packet** [ **ack** \| **dd** \| **filter** { **interface** *interface-type interface-number* \| { **source** \| **destination** } { **acl** *acl-num* \| **prefix-list** *prefix-list-name* } } \* \| **hello** \| **request** \| **update** ]]]

**[undo** **debugging** **ospf** [ *process-id*  **packet** [ **ack** \| **dd** \| **filter** \| **hello** \| **request** \| **update** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

**[ack**]：表示LSAck报文调试信息开关。

**[dd**]：表示DD报文调试信息开关。

**[filter**]：表示打开过滤报文的开关。

**[interface** *interface-type interface-number*]：接口类型和编号。

**[source**]：指定报文的源IP地址。

**[destination**]：指定报文的目的IP地址。

**[acl ***acl-number*]：指定用于过滤的ACL号，*acl-number*的取值范围为2000～3999。

**[prefix-list** *prefix-list-name*]：指定用于过滤的地址前缀列表名称，*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[hello**]：表示Hello报文调试信息开关。

**[request**]：表示LSR报文调试信息开关。

**[update**]：表示LSU报文调试信息开关。

【描述】

**[debugging ospf packet**]命令用来打开OSPF报文调试信息开关。**undo debugging ospf packet**命令用来关闭OSPF报文调试信息开关。

缺省情况下，OSPF报文调试信息开关处于关闭状态。

如果未指定进程号，则显示所有OSPF进程的报文调试信息。

如果未指定任何参数，则表示打开所有报文的调试信息开关。

表1-8 debugging ospf packet命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

Sending packets

发送OSPF报文

Receiving packets

接收OSPF报文

Source address: *src-addr*

OSPF报文源IP地址

Destination address: *dst-addr*

OSPF报文目的IP地址

Version *ver*, Type*: pkt-type*, Length: *pkt-len*

OSPF报文头信息：

·*ver*：OSPF协议版本，当前为2

·*pkt-type*：OSPF报文类型，取值为1表示Hello报文、2表示DD报文、3表示LSR报文、4表示LSU报文、取值为5表示LSAck报文

·*pkt-len*：OSPF报文长度

Router: *rt-id*, Area: *area-id*, Checksum: *chksum*

OSPF报文头信息：

·*rt-id*：生成OSPF报文的路由器标识

·*area-id*：发送报文的接口所属的区域ID

·*chksum*：从OSPF报文头开始，除了64位的认证域外，整个报文的校验和

Authentication type: *auth-type*, Key(ASCII): *key*

OSPF报文头信息：

·*au-type*：OSPF报文认证类型，取值为00表示无认证，为01表示简单认证，为02表示MD5认证

·*key*：认证码

Network mask: *net-mask**，*Hello interval: *hello-interval**，*Option: *opt*

OSPF Hello报文信息：

·*net-mask*：发送报文的接口的网络掩码

·*hello-interval*：发送报文的时间间隔，单位为秒

·*opt*：路由器支持的可选能力、E bit为支持外部路由、N/P bit 为N表示NSSA能力、P表示支持7转5、L bit表示报文后带有扩展与GR有关的扩展数据

Router priority: *rt-pri,* Dead Interval: *dead-interval,* DR: *ip-addr, * BDR: *ip-addr*

OSPF Hello报文信息：

·*rt-pri*：路由器的优先级

·*dead-interval*：邻居失效的时间间隔，单位为秒

·*ip-addr*：接口网段上DR或BDR的IP地址

Neighbor ID: *rt-id*

OSPF Hello报文信息：

·*rt-id*：OSPF已发现的邻居的路由器标识符

Hello: hello timer mismatch

OSPF Hello报文信息：路由器与邻居Hello interval不一致

Hello: dead timer mismatch

OSPF Hello报文信息：路由器与邻居Dead interval不一致

Hello: netmask mismatch

OSPF Hello报文信息：路由器与邻居网段掩码不一致

Hello: option mismatch

OSPF Hello报文信息：路由器与邻居对可选能力的支持不一致

Extended options(LLS data): *option*

OSPF Hello、DD报文信息：

·*option*：与GR有关的选项、LR表示OOB协商、RS通知邻居进入GR（Graceful  Restart）。

MTU:*mtu-val,* Option:  *option,* R_I_M_MS Bit: *bits*

OSPF DD报文信息：

·*mtu-val*：接口不分片而能发送的最大IP包字节大小。如果接口没有配置DD报文中MTU域的值为发送该报文接口的MTU值,该值为0。

·*option*：路由器支持的可选能力，取值E bit表示支持外部路由N/P bti 为N表示NSSA能力、P表示支持7转5、L bit表示报文后带有扩展与GR有关的扩展数据

·*bits*：DD报文协商标志位，取值I bit表示协商开始、M bit表示还有DD包要交互、MS bit表示自己是Master、R bit表示开始进行OOB，可以是这几个值的组合

DD Sequence number: *seq-num*

OSPF DD报文信息：

·*seq-num*：DD报文的序号

LSA type: *ls-type,* Link state ID: *ls-id,* Advertising router: *rt-id*

OSPF DD、LSR、LSAck报文信息

OSPF报文中描述的LSDB中的LSA的内容：

·*ls-type*：**LSA的类型，取值为1表示Router LSA、2为network LSA、3为net-summary LSA、4为ASBR-summary LSA、5为AS-external --LSA、7为NSSA LSA，9、10、11为Opaque LSA

·*ls-id*：LSA的Link ID

·*rt-id*：**通告LSA的路由器的标识符

LSA age: *ls-age, * Options: External routing:ON/OFF

OSPF DD、LSAck报文信息：

·ls-age：LSA的age

·ON/OFF：路由器外部路由能力的支持

Length: *ls-len*, Sequence number: *seq-num,*  Checksum: *checksum*

OSPF DD、LSAck报文信息：

·*ls-len*：LSA的字节长度

·*seq-num*：LSA的序列号

·*checksum*：LSA中的校验和

LSA count: *ls-count*

OSPF LSU报文信息：

·*ls-count*：LSU报文中包含的LSA数

【举例】

\# Router A通过GigabitEthernet1/0/1（150.1.1.1/24）与Router B的GigabitEthernet1/0/1（150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router B上创建OSPF进程1，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router A上打开OSPF HELLO报文调试信息开关。

\<RouterA\> debugging ospf packet hello

\<RouterA\>

\*0.68908828 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Sending packets.

\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.1

\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 44.

\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Router: 201.1.1.1, Area: 0.0.0.0, Checksum: 39833.

\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.

\*0.68908828 RouterA OSPF/6/OSPFDEBUG: Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR: 0.0.0.0.

*[// OSPF*]*进程1发送Hello报文。目前为止，没有发现任何邻居*

\*0.68913955 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.

\*0.68913955 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 44.

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 12700.

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.

\*0.68913965 RouterA OSPF/6/OSPFDEBUG: Router priority: 1, Dead Interval: 40, DR: 0.0.0.0, BDR: 0.0.0.0.

*[// OSPF*]*进程1收到对方Hello报文。目前为止，对方也是没有发现任何邻居*

\*0.68918832 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Sending packets.

\*0.68918832 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.1

\*0.68918832 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68918842 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.

\*0.68918842 RouterA OSPF/6/OSPFDEBUG:Router: 201.1.1.1, Area: 0.0.0.0, Checksum: 53394.

\*0.68918842 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68918842 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.

\*0.68918852 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:

0.0.0.0.

\*0.68918852 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 202.1.1.1.

*[// OSPF*]*进程1发送Hello报文。已经发现邻居202.1.1.1*

\*0.68924260 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.

\*0.68924260 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2

\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.

\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 14735.

\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_

\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:

150.1.1.2.

\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 201.1.1.1.

*[// OSPF*]*进程1收到对方的Hello报文。选举150.1.1.1为DR，150.1.1.2为BDR*

\*0.68928827 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Sending packets.

\*0.68928827 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.1

\*0.68928827 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68928837 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.

\*0.68928837 RouterA OSPF/6/OSPFDEBUG:Router: 201.1.1.1, Area: 0.0.0.0, Checksum: 14735.

\*0.68928837 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68928837 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.

\*0.68928847 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:

150.1.1.2.

\*0.68928847 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 202.1.1.1.

*[// OSPF*]*进程1发送保持邻居关系的Hello报文*

\*0.68934274 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.

\*0.68934274 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2

\*0.68934274 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.

\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 14735.

\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.

\*0.68934294 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:

150.1.1.2.

\*0.68934294 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 201.1.1.1.

*[// OSPF*]*进程1收到对方为保持邻居关系发送的Hello报文*

\# 在Router A上打开OSPF的报文过滤调试信息开关。

\<RouterA\> debugging ospf packet filter source prefix-list pl1

\<RouterA\> system-view

RouterA ip prefix-list pl1 index 1 permit 150.1.1.2 32

RouterA

\*0.68913955 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.

\*0.68913955 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 44.

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 12700.

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.

\*0.68913965 RouterA OSPF/6/OSPFDEBUG: Router priority: 1, Dead Interval: 40, DR: 0.0.0.0, BDR: 0.0.0.0.

\*0.68924260 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.

\*0.68924260 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2

\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.

\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 14735.

\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_

\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:

150.1.1.2.

\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 201.1.1.1.

\*0.68934274 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.

\*0.68934274 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2

\*0.68934274 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5

\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.

\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 14735.

\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.

\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.

\*0.68934294 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:

150.1.1.2.

\*0.68934294 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 201.1.1.1.

*// 指定报文源IP地址150.1.1.2，通过地址前缀列表pl1过滤的报文信息*

**OSPF \-- OSPF调试命令 \-- debugging ospf policy**

------------------------------------------------------------------------

【命令】

**[debugging** **ospf** [ *process-id*  **policy** { **abr-filter** \| **all** \| **default-route** \| **event** \| **redistribute** \| **spf** }]]

**[undo** **debugging** **ospf** [ *process-id*  **policy** { **abr-filter** \| **all** \| **default-route** \| **event** \| **redistribute** \| **spf** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

**[abr-filter**]：打开Type-3 LSA过策略的调试开关。

**[all**]：打开OSPF所有策略的调试开关。

**[default-route**]：打开默认路由过策略的调试开关。

**[event**]：打开策略事件的调试开关。

**[redistribute**]：打开引入路由过策略的调试开关。

**[spf**]：打开路由过策略的调试开关。

【描述】

**[debugging ospf policy**]命令用来打开过策略的调试信息开关。**undo debugging ospf policy**用来关闭过策略的调试信息开关。

缺省情况下，过策略的调试信息开关处于关闭状态。

如果未指定进程号，则显示所有OSPF进程的过策略调试信息。

表1-9 debugging ospf policy****abr-filter命令输出信息描述表

字段

含义

OSPF *process-id* area *area-id* checked abr-filter *type*, dest: *address*, mask: *mask*, result: *result*, cost:*cost*

Type-3 LSA过策略结果

·*process**-id*：OSPF进程ID

·*area-**id*：区域ID

·*type*：策略类型，取值为import表示向本区域发布的Type-3 LSA进行过策略，export表示向其它区域发布的Type-3 LSA进行过策略

·*address*：IP地址

·*mask*：掩码

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

·*cost*：表示过策略后的开销

表1-10 debugging ospf policydefault-route命令输出信息描述表

字段

含义

OSPF *process-id* registered default-route policy: *policy-name*, result: *result*

注册默认路由策略

·*process**-id*：OSPF进程ID

·*policy-name*：策略名

·*result*：返回结果，success表示注册成功，fail表示注册失败

OSPF *process-id* deregistered default-route policy: *policy-name*, result: *result*

注销默认路由策略

·*process**-id*：OSPF进程ID

·*policy-name*：策略名

·*result*：返回结果，success表示注销成功，fail表示注销失败

OSPF *process-id* received default-route policy message, result: *result*, flag: *flag*, cost type: *type*, cost: *cost*, tag: *tag*, policy-name: *name*

接收到默认路由过策略消息

·*process**-id*：OSPF进程ID

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

·*flag*：标志位，0x0表示无应用，0x1表示应用cost，0x2表示应用cost type，0x8表示应用tag，若存在多个应用，该标志位为或的关系

·*type*：默认路由类型，type-1表示一类外部路由，type-2表示二类外部路由，unknown表示未知类型

·*cost*：默认路由开销

·*tag*：标签

·*name*：策略名

OSPF *process-id* checked default-route policy, result: permit, flag: *flag*, cost type: *type*, cost: *cost*, tag: *tag*

默认路由过策略通过后的结果

·*process**-id*：OSPF进程ID

·*flag*：标志位，0x0表示无应用，0x1表示应用cost，0x2表示应用cost type，0x8表示应用tag，若存在多个应用，该标志位为或的关系

·*type*：默认路由类型，type-1表示一类外部路由，type-2表示二类外部路由，unknown表示未知类型

·*cost*：默认路由开销

·*tag*：标签

OSPF *process-id* checked default-route policy,result: deny

默认路由过策略不通过

·*process**-id*：OSPF进程ID

表1-11 debugging ospf policy****event命令输出信息描述表

字段

含义

OSPF received acl *number* change event

OSPF收到ACL变化事件

·*number*：ACL号

OSPF received ip prefix-list *name* change event

OSPF收到IP前缀列表变化事件

·*name*：前缀列表名

OSPF received route policy *name* change event

OSPF收到路由策略变化事件

·*name*：路由策略名

OSPF *process-id* received policy change event (Import count: *importcnt*, calculate count: *calccnt*)

OSPF进程收到过策略变化事件

·*process**-id*：OSPF进程ID

·*importcnt*：该策略在路由引入中被引用次数

·*calccnt*：该策略在路由计算中被引用次数

OSPF *process-id* GR end trigger import

GR结束触发路由引入

·*process**-id*：OSPF进程ID

OSPF *process-id* GR end trigger calculation

GR结束触发路由计算

·*process**-id*：OSPF进程ID

OSPF *process-id* GR end trigger calculating priority

GR结束触发路由收敛优先级计算

·*process**-id*：OSPF进程ID

表1-12 debugging ospf policy****redistribute命令输出信息描述表

字段

含义

OSPF *process-id* checked export policy, dest: *dest*, mask: *mask*, protocol ID: *protocol-id*, process ID: *process-id*, result: *result*

引入路由过策略结果

·*process**-id*：OSPF进程ID

·*dest*：目的IP地址

·*mask*：掩码

·*protocol-id*：引入路由协议号

·*process-id*：引入路由的进程号

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

表1-13 debugging ospf policy****spf命令输出信息描述表

字段

含义

OSPF *process-id* checked preference policy, dest: *dest*, result: *result*, new preference: *preference*

路由优先级过策略的结果

·*process**-id*：OSPF进程ID

·*dest*：目的IP地址

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

·*preference*：路由优先级数值

OSPF *process-id* checked prefix-priority policy, dest: *dest*, result: *result*, priority: *priority*

前缀优先收敛过策略的结果

·*process**-id*：OSPF进程ID

·*dest*：目的IP地址

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

·*priority*：路由收敛优先级名，优先级从高到低取值为critical、high、medium和low

OSPF *process-id* checked fast reroute policy, dest: *dest*, result: *result*, ifindex: *ifindex*, nexthop: *nexthop*, bkifindex: *bkifindex*, bknexthop: *bknexthop*

FRR过策略结果

·*process**-id*：OSPF进程ID

·*dest*：目的IP地址

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

·*ifindex*：出接口索引

·*nexthop*：下一跳地址

·*bkifindex*：备份出接口索引

·*bknexthop*：备份下一跳地址

OSPF *process-id* checked import policy, dest: *dest*, mask: *mask*, nexthop: *nexthop*, ifindex: *ifindex*, subprotocol: *protocol-id*, metric: *metric*, tag: *tag*, result: *result*

OSPF向路由管理下发路由过策略的结果

·*process**-id*：OSPF进程ID

·*dest*：目的IP地址

·*mask*：掩码

·*nexthop*：下一跳地址

·*ifindex*：出接口索引

·*protocol-id*：子协议号

·*metric*：花销

·*tag*：标签

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

【举例】

\# Router A通过GigabitEthernet1/0/1（150.1.1.1/24）与Router B的GigabitEthernet1/0/1（150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；配置默认路由策略，在Router A上打开默认路由过策略的调试信息开关。

\<RouterA\> debugging ospf policy default-route

\*Nov  5 10:10:01:326 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 registered default-route policy r1, result: success.

*// 默认路由策略注册成功*

\*Nov  5 10:10:02:776 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 received default-route policy message, result: permit, flag: 0x8, cost type: type-1, cost: 0, tag: 333, policy-name: r1.

\*Nov  5 10:10:02:777 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 checked default-route policy, result: permit, flag: 0x8, cost type: type-1, cost: 0, tag: 333.

*// 默认路由过策略成功*

\# Router A通过GigabitEthernet1/0/1（150.1.1.1/24）与Router B的GigabitEthernet1/0/1（150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0，配置静态路由3.3.3.3/32，引入静态路由；在Router B上创建OSPF进程1，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router A上打开路由过策略的调试信息开关。

\<RouterA\> debugging ospf policy spf

\*Nov  5 10:10:03:777 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 checked import policy, dest: 3.3.3.3, mask: 32, nexthop: 150.1.1.1, ifindex: 0x2, subprotocol: 1, metric: 1, tag: 333, result: permit.

*[// OSPF*]*向路由管理下发路由过策略成功*

**OSPF \-- OSPF调试命令 \-- debugging ospf redistribute**

------------------------------------------------------------------------

【命令】

**[debugging** **ospf** [ *process-id*  **redistribute** { **event** \| **prefix**  *ip-address* *mask-length*  }]]

**[undo** **debugging** **ospf** [ *process-id*  **redistribute** { **event** \| **prefix** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：路由的目的IP地址。

*[mask-length*]：网络掩码长度，取值范围为0～32。

**[prefix**]：表示引入前缀调试信息开关。

**[event**]：表示引入事件调试信息开关。

【描述】

**[debugging ospf redistribute**]命令用来打开OSPF 路由引入调试信息开关。**undo debugging ospf redistribute**命令用来关闭OSPF 路由引入调试信息开关。

缺省情况下，OSPF 路由引入调试信息开关处于关闭状态。

如果未指定进程号，则显示所有OSPF进程的路由引入调试信息。

表1-14 debugging ospf redistribute event命令输出信息描述表

字段

描述

OSPF *process-id* triggered redistributed type *type*

触发路由引入，其中：

·*process-id*：OSPF进程号

·*type*：引入类型，1表示从RIB表引入，2表示从自身的引入表引入

OSPF received rib smooth start message

OSPF收到平滑开始消息

OSPF received rib smooth end message

OSPF收到平滑结束消息

OSPF received rib batch start message, instance: *instance-id* , user data: *data*

OSPF实例收到批量上报开始消息：

·*instance-id*：路由所在VPN

·*data*：协议注册时携带的私有数据

OSPF received rib batch end message, instance: *instance-id* , user data: *data*

OSPF实例收到批量上报开始消息：

·*instance-id*：路由所在VPN

·*data*：协议注册时携带的私有数据

OSPF received ECA *attr-id* change event:*event*

OSPF实例收到处理扩展团体属性变化消息：

·*attr-id*：扩展团体属性ID

·*event*：事件，取值为add或delete

表1-15 debugging ospf redistribute prefix命令输出信息描述表

字段

描述

OSPF *process-id* process redistributed entry, ifindex: *ifindex*, nexthop: *nexthop,* tag: *tag*, flag: *flag,* process ID: *process-id2,* attribute ID: *attr-id*

处理引入前缀的路由信息：

·*process-id*：OSPF进程号

·*ifindex*：出接口索引

·*nexthop*：下一跳IP地址

·*tag*：标签

·*flag*：路由标志，取值为：0x00000001、0x00000002、 0x00000004、0x00000008、0x00000010、0x00000020、0x00000040、0x00000080、0x00000100、0x00000200、0x00000400、0x00010000、0x00040000、0x00080000、0x00100000、0x00200000、0x00400000

·*process-id**2*：引入路由的进程号

·*attr-id*：扩展团体属性ID

OSPF *process-id* process route:*dest*/*mask-len*, redistributed type: *type,* metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count,* option: *option*, old option: *option*

查找该前缀原来是否被引入：

·*process-id*：OSPF进程号

·*dest*/*mask-len*：目的地址和掩码

·*type*：引入类型，1表示从自身引入表引入，2表示从RIB引入

·*metric*：开销

·*protocol-id*：协议号，1表示直连路由，2表示静态路由，3表示rip，4表示ospf，5表示isis，6表示bgp

·*subprotocol-id*：子协议号

·*count*：下一跳个数

·*option*：引入前缀属性，0x01表示3类(源自MBGP还原)，0x02表示ABR聚合，0x04表示5/7类(源自引入)，0x08表示ASBR聚合(VPN)

OSPF received prefix refresh message:*dest*/*mask-len*, instance: *instance-id*, user data: *data,* metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count*

收到前缀路由刷新消息：

·*dest*/*mask-len*：目的地址和掩码

·*instance-id*：路由所在VPN

·*data*：协议注册时携带的私有数据

·*metric*：开销

·*protocol-id*：协议号

·*subprotocol-id*：子协议号

·*count*：下一跳个数

OSPF received prefix delete message:*dest*/*mask-len*, instance: *instance-id*, user data: *data*, table ID: *table-id*, old protocol ID: *protocol-id*

收到前缀路由删除消息：

·*dest*/*mask-len*：目的地址和掩码

·*instance-id*：路由所在VPN

·*data*：协议注册时携带的私有数据

·*table-id*：路由所属路由表ID

·*protocol-id*：上次上报的协议类型

OSPF received rib refresh message:*dest*/*mask-len*, instance: *instance-id*, user data: *data,* metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count*

收到激活路由刷新消息：

·*dest*/*mask-len*：目的地址和掩码

·*instance-id*：路由所在VPN

·*data*：协议注册时携带的私有数据

·*metric*：开销

·*protocol-id*：协议号

·*subprotocol-id*：子协议号

·*count*：下一跳个数

OSPF received rib delete message:*dest*/*mask-len*, instance: *instance-id*, user data: *data*, table ID: *table-id*, old protocol ID: *protocol-id*

收到激活路由删除消息：

·*dest*/*mask-len*：目的地址和掩码

·*instance-id*：路由所在VPN

·*data*：协议注册时携带的私有数据

·*table-id*：路由所属路由表ID

·*protocol-id*：上次上报的协议类型

OSPF *process-id* added prefix: *dest*/*mask-len*, metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count*

将前缀添加到引入路由表，其中：

·*process-id*：OSPF进程号

·*dest*：目的地址

·*mask-len*：掩码长度

·*metric*：开销

·*protocol-id*：协议号

·*subprotocol-id*：子协议号

·*count*：下一跳个数

OSPF *process-id* deleted prefix: *dest*/*mask-len*, metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count*

将前缀从引入路由表删除，其中：

·*process-id*：OSPF进程号

·*dest*：目的地址

·*mask-len*：掩码长度

·*metric*：开销

·*protocol-id*：协议号

·*subprotocol-id*：子协议号

·*count*：下一跳个数

OSPF aged default route, instance: *instance-id*

老化默认路由：

·*instance-id*：路由所在VPN

OSPF *process-id* aged redistributed route *dest-addr*/*mask-len*

老化引入路由：

·*process-id*：OSPF进程号

·*dest-addr*：目的地址

·*mask-len*：掩码

【举例】

\# Router A通过Vlan-interface10（150.1.1.1/24）与Router B的Vlan-interface10（150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在Vlan-interface10上使能OSPF功能并配置其属于区域0；在Router B上创建OSPF进程1，在Vlan-interface10上使能OSPF功能并配置其属于区域0；在Router A上打开引入事件调试信息开关。

\<RouterA\> debugging ospf redistribute event

\*Nov  1 08:58:54:157 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 triggered redistributed type 2.

\*Nov  1 08:58:54:158 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 triggered redistributed type 2.

\*Nov  1 08:58:54:158 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 triggered redistributed type 2.

\*Nov  1 08:58:55:280 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 triggered redistributed type 2.

*[// OSPF*]*进程1通过查找自身的引入表进行路由引入*

\*Nov  1 08:58:57:109 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF received rib smooth start message.

\*Nov  1 08:58:57:112 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF received rib smooth end message.

*[// OSPF*]*进程收到平滑消息*

\*Nov  1 08:58:57:124 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF received rib batch start message, instance: 0, user data: 0x0.

\*Nov  1 08:58:57:126 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF received rib batch end message, instance: 0, user data: 0x0.

*[// OSPF*]*实例收到批量上报消息*

\# Router A通过Vlan-interface10（150.1.1.1/24）与Router B的Vlan-interface10（150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在Vlan-interface10上使能OSPF功能并配置其属于区域0，；在Router B上创建OSPF进程1，在Vlan-interface10上使能OSPF功能并配置其属于区域0；在Router A的进程1上配置引入静态路由，打开引入前缀调试信息开关。

\<RouterA\> debugging ospf redistribute prefix

\<RouterA\> system-view

RouterA ip route-static 2.1.1.1 24 null0

RouterA\*Nov  5 08:18:32:128 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF received rib refresh message:2.1.1.0/24, instance: 0, user data: 0x0,

metric: 0, protocol ID: 2, subprotocol ID: 1, nexthop count: 1.

\*Nov  5 08:18:32:128 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 process redistributed entry, ifindex: 0x14c1, nexthop: 0x0,

tag: 0, flag: 0x10000, process ID: 0, attribute ID: 0xffffffff.

\*Nov  5 08:18:32:128 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 process route:2.1.1.0/24, redistribute type:2

metric: 0, protocol ID: 2, subprotocol ID: 1, nexthop count:1,

option: 0x04, old option: 0x00.

\*Nov  5 08:18:32:128 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 added prefix: 2.1.1.0/24, metric: 0, protocol ID: 2, subprotocol ID: 1, nexthop count: 1.

*[// OSPF*]*进程1引入激活路由*

RouterA undo ip route-static 2.1.1.1 24

RouterA\*Nov  5 08:19:13:752 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF received rib delete message: 2.1.1.0/24, instance: 0, user data: 0x0, table ID: 2, old protocol ID: 2.

\*Nov  5 08:19:13:752 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 deleted prefix: 2.1.1.0/24, metric:0, protocol ID: 2, sub protocol ID: 1, nexthop count: 1.

*[// OSPF*]*进程1删除激活路由*

RouterA ip route-static 0.0.0.0 0 null0

RouterA\*Nov  5 08:19:31:558 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF received prefix refresh message: 0.0.0.0/0, instance: 0, user data: 0x0,

metric: 0, protocol ID: 2, subprotocol ID: 1, nexthop count: 1.

*[// OSPF*]*进程引入默认路由*

RouterA undo ip route-static 0.0.0.0 0

RouterA\*Nov  5 08:19:56:656 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF received prefix delete message: 0.0.0.0/0, instance: 0, user data: 0x0, table ID: 2, old protocol ID: 0.

\*Nov  5 08:19:56:656 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF receive rib delete message: 0.0.0.0/0, instance: 0, user data: 0x0, table ID: 2, old protocol ID: 2.

*[// OSPF*]*进程删除默认路由*

**OSPF \-- OSPF调试命令 \-- debugging ospf spf**

------------------------------------------------------------------------

【命令】

**[debugging ospf** [ *process-id*  **spf** { **all** \| **asbr** \| **brief** \| **external** \| **internal** \| **topology** \| **tree** }]]

**[undo debugging ospf** [ *process-id*  **spf** { **all** \| **asbr** \| **brief** \| **external** \| **internal** \| **topology** \| **tree** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

**[all**]：表示所有SPF调度与计算的调试信息开关。

**[asbr**]：表示SPF计算ASBR路由的调试信息开关。

**[brief**]：表示SPF的job调度调试信息开关。

**[external**]：表示SPF计算External AS路由的调试信息开关。

**[internal**]：表示SPF计算Internal AS路由的调试信息开关。

**[topology**]：表示SPF node和link变化的调试信息开关。

**[tree**]**：**表示生成树计算调试信息开关。

【描述】

**[debugging ospf spf**]命令用来打开OSPF SPF调试信息开关。**undo debugging ospf spf**命令用来关闭OSPF SPF调试信息开关。

缺省情况下，OSPF SPF调试信息开关处于关闭状态。

如果未指定进程号，则显示所有OSPF进程的SPF调试信息。

表1-16 debugging ospf spf brief命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

Schedule event: *schedule-event* at *x* ms

引起SPF调度的事件：

·*schedule-event*：产生调度的事件类型，取值为0x80000000、0x40000000、 0x10000000、 0x00008000、0x00004000、0x00000020、0x00000010

Schedule flag: *schedule-flag*, SPF is scheduled

显示SPF调度标志位：

·*schedule-flag*：调度标志，取值为0x80000000、0x40000000、0x20000000、0x10000000、0x08000000、0x00008000、0x00004000、0x00002000、0x00001000、0x00000080、0x00000020、0x00000010

Schedule flag: *schedule-flag*, SPF is stopped

显示停止SPF调度的标志位：

·*schedule-flag*：调度标志，取值为0x80000000、0x40000000、0x20000000、0x10000000、0x08000000、0x00008000、0x00004000、0x00002000、0x00001000、0x00000080、0x00000020、0x00000010

Pre Proc: Schedule: *schedule-flag*

当前SPF调度标志：

·*schedule--flag*：调度标志，取值为0x80000000、0x40000000、0x20000000、0x10000000、0x08000000、0x00008000、0x00004000、0x00002000、0x00001000、0x00000080、0x00000020、0x00000010

Pre Proc: Running: *running-flag*

当前SPF计算标志：

·*running-flag*：运行标志，取值为0x80000000、0x40000000、0x20000000、0x10000000、0x08000000、0x00008000、0x00004000、0x00002000、0x00001000、0x00000080、0x00000040、0x00000020、0x00000008、0x00000004，或者其中某些值的组合

SPF building SPT begins at x ms

SPF最短路径树计算开始

Build SPT for area *area-id* at x ms

计算区域号为*area-id*区域的最短路径树

SPF building SPT ends at x ms

SPF最短路径树计算结束

Router route calculation begins at x ms

Router类型路由计算开始

Router route calculation ends at x ms

Router类型路由计算结束

Type-7 to Type-5 LSA translator begins at x ms

七转五角色计算开始

Type-7 to Type-5 LSA translator ends at x ms

七转五角色计算结束

Internal route calculation begins at x ms

开始计算AS内部路由

SPF starts(full internal routes)

开始全部计算AS内部路由

SPF ends(full internal routes)

AS内部路由全部计算结束

SPF starts(incremental internal routes)

开始增量计算AS内部路由

SPF ends(incremental internal routes)

增量计算AS内部路由结束

Internal route calculation ends at x ms

AS内部路由计算结束

Forwarding address calculation begins at x ms

开始计算转发地址

Forwarding address calculation ends at x ms

计算转发地址结束

External route calculation begins at x ms

开始计算AS外部路由

SPF starts(full external routes)

开始全部计算AS外部路由

SPF ends(full external routes)

AS外部路由全部计算结束

SPF starts(incremental external routes)

开始增量计算AS外部路由

SPF ends(incremental external routes)

增量计算AS外部路由结束

External route calculation ends at x ms

AS外部路由计算结束

LFA nbr collect  begins

FRR 邻居信息收集开始

LFA nbr collect end

FRR邻居信息收集结束

LFA nbr SPF calculation begins

FRR邻居SPF计算开始

LFA nbr SPF calculation end

FRR邻居SPF计算结束

LFA nbr IntraRt cost calculation begins

FRR 邻居intra路由cost计算开始

LFA nbr IntraRt cost calculation end

FRR 邻居intra路由cost计算结束

LFA nbr ASBR cost calculation begins

FRR 邻居ASBR cost计算开始

LFA nbr ASBR cost calculation end

FRR 邻居ASBR cost计算结束

LFA SPF BkNextHop calculation begins

FRR SPF备份下一跳计算开始

LFA SPF BkNextHop calculation end

FRR SPF备份下一跳计算结束

表1-17 debugging ospf spf asbr命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

Full ASBR routes calculation begins at bucket x

全部ASBR路由计算开始

Full ASBR stops at bucket x

全部ASBR路由计算本次结束

SPF calculating route to ASBR, Destination ID *dest-addr*

计算到达*dest-addr*的ASBR路由：

·*dest-addr*：目的地址

Incremental ASBR routes calculation begins

开始增量计算ASBR路由

Incremental ASBR routes calculation ends

增量ASBR路由计算结束

Begin Calc Asbr LFA Dest:*Router-id* PriNexthop:*ipaddr*

开始计算Asbr备份下一跳

·*Router-id*：Asbr的Routerid

·*Ipaddr*：主下一跳ip地址

Succeed Calc Asbr LFA Dest: *Router-id*, PriNexthop: *ipaddr*, LFANexthopAddr: *Bkipaddr*

成功计算出Asbr备份下一跳

·*Bkipaddr*：备份下一跳

表1-18 debugging ospf spf internal命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF 进程号

Full internal routes calculation begins

全部AS内部路由计算开始

Full internal routes calculation ends

全部AS内部路由计算本次结束

SPF calculating route to internal route *dest-addr* /*mask-len*

计算到达*dest-addr*/*msk-lenr*的AS内部路由：

·*dest-addr*：目的地址

·*mask-len*：掩码

Advertising source *dest-id*, *src-type*, cost x

路由发布源信息，包括发布者，发布源类型，cost：

·*dest-id*：路由发布者

·*src-type*：发布源类型，取值stub、network、inter

Old route has no valid nexthop

计算之前，没有到达此路由的有效路径

Old route for *dest-addr*/*mask-len*, cost x

计算之前到达*dest-addr* /*mask-len*的cost：

·*dest-addr*：目的地址

·*mask-len*：掩码

stub route, nexthop *dest-addr*, Entry ID *entry-id*

计算之前路由的下一跳，Entry ID：

·*dest-addr*：下一跳

·*mask-len*：在路由表中的ID

Cannot find valid nexthop for current advertising source

不能查找到当前发布源的下一跳

Add new route. Outgoing interface: x, Nexthop: *dest-addr, %s NbrId ID 0x%*

增加一条新路由，包括出接口，下一跳地址，邻居类型和ID号：

·*dest-addr*：下一跳地址

Delete old route. Outgoing interface: x, Nexthop: d*est-addr, %s NbrId ID 0x%*

删除路由，路由出接口，下一跳地址，邻居类型和ID号：

·*dest-addr*：下一跳地址

Update old route. Outgoing interface: x, Nexthop: *dest-addr, %s NbrId ID 0x%*

更新路由出接口，下一跳地址，邻居类型和ID号：

·*dest-addr*：下一跳地址

No advertising source

无发布源

Incremental internal route calculation begins

开始增量计算

Incremental internal route calculation ends

增量计算结束

Begin Calc One IntraRt BNH, Dest: *dest-ip*, PNH: *dest-addr*,

开始计算一条intra路由备份下一跳：

·*dest-ip*：目的地址

·*dest-addr*：下一跳地址

Succeed Calc One IntraRt BNH, Dest: *dest-ip*, PNH:*dest-addr*. BNP: *dest-addr*,

成功计算出一条intra路由备份下一跳：

·*dest-ip*：目的地址

·*dest-addr*：下一跳地址

表1-19 debugging ospf spf external命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

Full SPF ASE routes calculation begins

开始完全ASE SPF计算

Full SPF ASE routes calculation stops

结束完全ASE SPF计算

SPF calculating external route *dest-addr/mask-len*

计算到达*dest-addr/msk-lenr*的AS外部路由：

·*dest-addr*：目的地址

·*mask-len*：掩码

Advertising source *dest-id*, *src-type* src, Cost: x

路由发布源信息，包括发布者，发布源类型，cost：

·*dest-id*：路由发布者

·s*rc-type*：发布源类型，取值ASE、NSSA

Old route has no valid nexthop

计算之前，没有到达此路由的有效路径

Old route for *dest-addr/mask-len*, cost x

计算之前到达*dest-addr/mask-len*的cost：

·*dest-addr*：目的地址

·*mask-len*：掩码

Cannot find ASBR route

不能查找到到达ASBR的路由

Begin Calc ExternalASRt Alt DestIpAddr:*dest-addr*, PriNextHopAddr:*ip-addr*

开始计算外部路由备份下一跳

·*dest-addr*：目的地址

·*ip-addr*：主下一跳地址

Succeed Calc ExternalASRt Alt DestIpAddr: *dest-addr* PriNextHopAddr: *ip-addr*, LFANexthopAddr:*bk-addr*

成功计算外部路由备份下一跳

·*dest-addr*：目的地址

·*ip-addr*：主下一跳地址

·*bk-addr*：备份下一跳地址

表1-20 debugging ospf spf topology命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

SPF node added, type: *type* , advertising source: *adv-id*, LsId: *lsid*

增加SPF节点：

·*type*：取值1、2

·*adv-id*：发布源ID

·*lsid*：发布源LsId

SPF node updated, type: *type*, advertising source: *adv-id*, LsId: *lsid*

更新SPF节点：

·*type*：取值1、2

·*adv-id*：发布源ID

·*lsid*：发布源LsId

SPF node deleted, type: *type*, advertising source: *adv-id*, LsId: *lsid*

删除SPF节点：

·*type*：取值1、2

·*adv-id*：发布源ID

·*lsid*：发布源LsId

SPF link added, type:*type*, link ID: *link-id*, LsId: *lsid*

增加SPF链路：

·*type*：取值1、2、3

·*link-id*：link ID

·*lsid*：发布源的LsId

SPF link updated, type:*type*, link ID: *link-id*, LsId: *lsid*

更新SPF链路：

·*type*：取值1、2、3

·*link-id*：link ID

·*lsid*：发布源的LsId

SPF link deleted, type:*type*, link ID: *link-id*, LsId: *lsid*

删除SPF链路：

·*type*：取值1、2、3

·*link-id*：link ID

·*lsid*：发布源的LsId

表1-21 debugging ospf spf tree命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

No delete flag on node.

节点上无删除标志

Set direct flag on node.

为节点打上直连标志

Delete node.

删除节点

Delete non-existent node.

删除不存在的节点

Set RMT flag on node.

为节点打上RMT标志

Set RMT flag on destination node.

为目的节点打上RMT标志

Set direct flag on destination node.

为目的节点打上直连标志

Cost is decreased. Destination node is deleted. 2-way check failed.

目的节点已删除，2-way检查失败

Link (new path)

增加新链路

Link (involved)

本次变化涉及此链路

Resume link

恢复被删除的链路

Delete link

删除链路

Backward link involved

回指链路变化

Create existing link

创建已存在的链路

Create new link

创建新链路

Delete link when deleting node

删除节点时删除链路

Cost is increased. Link has no effect on any node.

新增链路不影响任何节点

Cost is decreased. Backward link is deleted. 2-way check failed.

回指链路被删除，2-way检查失败

Cost is decreased The cost of backward link is out of range. 2-way check failed.

回指链路cost超大，2-way检查失败

Add root to candidate list of area *area-id*

区域最短路径树计算：

·*area-id*：区域ID

Destination node *dest-id*, Advertising source *adv-id*, Non-stub link count x

当前处理的节点信息：

·*dest-id*：目的节点

·*adv-id*：发布源ID

*[type* Link *link-id*, Data *link-data*, Cost x]

当前处理的链路信息：

·*type*：TransNet、p-2-p

·*link-id*：链路对应的link ID

·*link-data*：链路对应的data

SPF node TENT: neighbor node found

找到目的节点

SPF node TENT: neighbor node not found

没找到目的节点

Add vertex: *type* *dest-id*, Cost to root x, Nexthop: *dest-addr*

加入候选节点：

·*type*：取值1、2、3

·*dest-id*：目的节点

·*dest-addr*：下一跳地址

Get vertex: *type* *dest-id*, Cost to root x, Nexthop: *dest-addr*

加入候选节点：

·*type*：取值1、2、3

·*dest-id*：目的节点

·*dest-addr*：下一跳地址

Net-node *dest-id*, Advertising source *adv-id*, Router count x

网段节点信息以及包含的目的节点数：

·*dest-id*：目的节点

·*adv-id*：发布源ID

Attach router *dest-id*

网段节点中包含的目的节点：

·*dest-id*：目的节点

Remove vertex:*type* *dest-id*, Cost to root x, Nexthop: *dest-addr*

从候选链上移除候选节点：

·*type*：取值1、2、3

·*dest-id*：目的节点

·*dest-addr*：下一跳地址

Candidate list empty, SPF area *area-id* finished.

区域完成最短路径树计算：

·*area-id*：当前计算的区域

Delete SPF link

删除SPF链路

SPF link: Nexthop is changed\...

SPF链路下一跳变化

SPF link: Cost is increased\...

SPF链路的cost增大

SPF link: Cost is decreased\...

SPF链路的cost减小

SPF link: Cost is decreased, and backward link is found.

找到回指链路

SPF link Type: *type*,Link ID: link-id, LS ID: *ls_id* Neighbors:x  *Ingore2way*  whereTree(Back) change-type Incr(Decr) del NHop Involved NewPath

SPF链路描述信息：

·*type*：类型取值transit、p-2-p

·*link-id*：链路对应的link ID

·*ls_id*：发布源LS ID

·*Ingore2way*：忽略2-way检查

·*where*：状态，取值tree、back、init

·*change-type*：链路变化类型，取值del、nhop、involved newpath

Rebuilding Nbr *adv-id* Spf Tree for Area area-id

开始邻居SPF树计算：

·*adv-id*：邻居ID

·*area-id*：区域号

Add Node to Nbr htSpfHashTbl:Node *ls_id*, Mask *mask-len*, Cost to root *x*

将普通Rtr节点加入到邻居节点哈希表：

·*ls_id*：发布源LS ID

·*mask-len*：掩码长度

·x：开销

Add PnNode to Nbr PseudoNodeTbl:PnNode *ls_id*, Mask *mask-len*, Cost to root *x*

将网段节点加入到邻居网段哈希表：

·*ls_id*：发布源LS ID

·*mask-len*：掩码长度

·x：开销

LFA nbr SPF calculation error *x*

FRR邻居SPF计算错误码

·x：错误码

Area:*area-id* Begin Calc SPFNode LFA Lsid: *ls_id* Type:*type*

开始计算SPF节点的备份下一跳：

·*ls_id*：发布源LS ID

·*type*：1为RtrNode，2为TransitNode

Area: *area-id* Succeed Calc SPFNode LFA Lsid: *ls_id* Type:*type* PriNexthop:*Nexthop-addr*，LFANexthop: *BkNexthop-addr*

成功计算出SPFNode备份下一跳：

·*ls_id*：发布源LS ID

·*Nexthop-addr*：下一跳IP地址

·*BkNexthop-addr*：备份下一跳IP地址

CandNexthopN: *Nexthop-addr* S2AltN: *cost* AltN2D:*cost* N2S: *cost* N2D: *cost* N2E: *cost* S2N: *cost* S2D: *cost*

候选节点的cost：

·S2AltN：源节点到当前最优下一跳的距离

·AltN2D：当前最优下一跳到目的节点的距离

·N2S：备份下一跳到源节点的距离

·N2D：备份下一跳到目的节点的距离

·S2D：源节点到目的节点的距离

CandNexthopN: *Nexthop-addr*  is PriNexthop

候选备下一跳是主下一跳

CandNexthopN: *Nexthop-addr*  not Loop Free

候选备下一跳有环路

CandNexthopN: *Nexthop-addr* ExitIndex is PriExitIndex

候选备下一跳出接口与主下一跳出接口相同

CurrNexthopN: *Nexthop-addr* Node protect, CandNexthopN: *Nexthop-addr* Not

当前最优备下一跳为节点保护，但候选备下一跳不为节点保护

CurrNexthopN: *Nexthop-addr* Link protect, CandNexthopN: *Nexthop-addr* Not

当前最优备下一跳为链路保护，但候选备下一跳不为链路保护

Update SPF Node LFANexthop: *Nexthop-addr* Reason:*reason*

更新备选下一跳，*reason*取值为：

·Node Protect：备份下一跳节点保护

·Link Protect：备份下一跳链路保护

·Downstream alternate：备份下一跳下游保护

·Cost：备份下一跳S2N+N2D更小

·Different PriExitIndex：备份下一跳 出接口与主下一跳不同

·Nexthop IpAddr：备份下一跳IP地址更小

·NULL CurrNode：当前最优备份下一跳为NULL，直接更新

Rtr-node *dest-id*, Tunnel found, SPF cost x, TE cost x, Nexthop: *dest-addr*

从候选链上新发现隧道：

·*dest-id*：目的节点

·*dest-addr*：下一跳地址

【举例】

\# Router通过GigabitEthernet1/0/1（192.168.171.2/24）与Router A的GigabitEthernet1/0/1（192.168.171.10/24）在Area 0相连，接口类型为Broadcast，在Router上创建OSPF进程1，在OSPF进程1中创建区域0，打开调试开关并重启OSPF进程1。

\<Sysname\> debugging ospf spf all

\<Sysname\> reset ospf 1 process

Reset OSPF process? [Y/N:y]

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF Stop Schedule for process reset

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule event: 0x00000000 SPF is stopped, at 803994745 ms

  OSPF 1 SPF link Delete SPF link

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  SPF link Type:2, Link ID:192.168.171.10, LS ID:22.22.22.22 Neighbors:1 Back

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF link Delete SPF link

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  SPF link Type:2, Link ID:192.168.171.10, LS ID:192.168.171.2 Neighbors:1 Tree

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF link Delete SPF link

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  SPF link Type:3, Link ID:192.168.171.2, LS ID:192.168.171.10 Neighbors:1 Back

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF link Delete SPF link

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  SPF link Type:3, Link ID:22.22.22.22, LS ID:192.168.171.10 Neighbors:1 Tree

*// 停止SPF计算，删除SPF链路*

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF node added, Type:1, Advertising source:192.168.171.2, LS ID:192.168.171.2

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Add New Node.

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule event: 0x00000001 at 803994819 ms.

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule flag : 0x00000001 SPF is scheduled.

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule event: 0x00000080 at 803994821 ms.

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF Initial running flag

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Pre Proc : Schedule: 0x00000001.

\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Pre Proc : Running : 0x000006CD.

\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF building SPT begins at 804000440 ms

*// 创建新的SPF节点，SPF计算开始*

\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 \*\*\*\* Rebuilding Spf Tree for Area 0.0.0.0, at 804000440 ms. \*\*\*\*

\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF building SPT ends at 804000440 ms

*// 重建SPF树，SPF计算结束*

\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Router route calculation begins at 804000440 ms

\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Router route calculation ends at 804000440 ms

\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Router route calculation begins at 804000440 ms

\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Full ASBR routes calculation begins at bucket 0

\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Full ASBR stops at bucket 11

\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Router route calculation ends at 804000440 ms

\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Type-7 to Type-5 LSA translator begins at 804000440 ms

\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Type-7 to Type-5 LSA translator ends at 804000440 ms

\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Internal route calculation begins at 804000440 ms

*// 各种类型路由计算开始或结束*

\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 \*\*\*\*\*\*\*\*\* SPF starts(full internal routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Full internal routes calculation begins

\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF calculating route to internal route 192.168.171.0/24

\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Advertising source 192.168.171.2, Stub src, cost:1

\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Old route has no valid nexthop

\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Add new route. Outgoing interface:5, Nexthop:192.168.171.2, Normal NbrId ID

\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;

0x130003f2

\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Full internal routes calculation ends

*// 开始全部计算AS内部路由*

\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 \*\*\*\*\*\*\*\*\* SPF ends(full internal routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Internal route calculation ends at 804000441 ms

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Forwarding address calculation begins at 804000441 ms

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Forwarding address calculation ends at 804000441 ms

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 External route calculation begins at 804000441 ms

*[// AS*]*内部路由全部计算结束*

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 \*\*\*\*\*\*\*\*\* SPF starts(full external routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Full SPF ASE routes calculation begins

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Full SPF ASE routes calculation stops

*// 开始全部计算AS外部路由*

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 \*\*\*\*\*\*\*\*\* SPF ends(full external routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 External route calculation ends at 804000443 ms

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule event: 0x00000080 at 804000450 ms.

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule flag : 0x00000080 SPF is scheduled.

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF Initial running flag

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Pre Proc : Schedule: 0x00000080.

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Pre Proc : Running : 0x00000300.

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Internal route calculation begins at 804000667 ms

*[// AS*]*外部路由全部计算结束*

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 \*\*\*\*\*\*\*\*\* SPF starts(incremental internal routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Incremental internal route calculation begins

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF calculating route to internal route 120.1.1.0/24

\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Advertising source 192.168.171.2, Stub src, cost:10

\*Nov  1 10:10:51:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Old route has no valid nexthop

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Add new route. Outgoing interface:6, Nexthop:120.1.1.1

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Incremental internal route calculation ends

*// 开始增量计算AS内部路由*

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 \*\*\*\*\*\*\*\*\* SPF ends(incremental internal routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Internal route calculation ends at 804000798 ms

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Forwarding address calculation begins at 804000798 ms

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Forwarding address calculation ends at 804000798 ms

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF node added, Type:1, Advertising source:22.22.22.22, LS ID:22.22.22.22

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Add New Node.

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF link added, Type:2, Link ID:192.168.171.10, LS ID:192.168.171.2

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Create new link

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule event: 0x0000028C at 804002088 ms.

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule flag : 0x0000028C SPF is scheduled.

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule event: 0x00000001 at 804002211 ms.

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF node added, Type:2, Advertising source:22.22.22.22, LS ID:192.168.171.10

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Add New Node.

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Set direct flag on node.

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF link added, Type:3, Link ID:192.168.171.2, LS ID:192.168.171.10

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Create new link

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF link added, Type:3, Link ID:22.22.22.22, LS ID:192.168.171.10

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Create new link

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Schedule event: 0x00000002 at 804002406 ms.

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF link added, Type:2, Link ID:192.168.171.10, LS ID:22.22.22.22

\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Create new link

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF Initial running flag

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Pre Proc : Schedule: 0x00000001.

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Pre Proc : Running : 0x000006CD.

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF building SPT begins at 804007439 ms

*// 增量计算AS内部路由结束*

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 \*\*\*\* Rebuilding Spf Tree for Area 0.0.0.0, at 804007439 ms. \*\*\*\*

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF building SPT ends at 804007439 ms

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Router route calculation begins at 804007439 ms

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Router route calculation ends at 804007439 ms

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Router route calculation begins at 804007439 ms

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Full ASBR routes calculation begins at bucket 0

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 SPF calculating route to ASBR, Destiantion ID 22.22.22.22

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Full ASBR stops at bucket 11

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Router route calculation ends at 804007439 ms

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Type-7 to Type-5 LSA translator begins at 804007439 ms

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Type-7 to Type-5 LSA translator ends at 804007439 ms

\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;

  OSPF 1 Internal route calculation begins at 804007439 ms

*// 区域0重建SPF树，各种类型路由计算开始或结束*

**OSPF \-- OSPF调试命令 \-- debugging ospf timer**

------------------------------------------------------------------------

【命令】

**[debugging** **ospf** [ *process-id*  **timer** [ **lsa-generate** \| **spf** ]]]

**[undo debugging ospf **[ *process-id*  **timer** [ **lsa-generate** \| **spf** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

**[lsa-generate**]：表示LSA生成定时器调试信息开关。

**[spf**]：表示SPF计算定时器调试信息开关。

【描述】

**[debugging ospf timer**]命令用来打开OSPF定时器调试信息开关。**undo debugging ospf  timer**命令用来关闭OSPF定时器调试信息开关。

缺省情况下，OSPF定时器调试信息开关处于关闭状态。

如果未指定进程号，则显示所有OSPF进程的定时器调试信息。

表1-22 debugging ospf timer lsa-generate命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

Create LS timer, timeout value is *x* ms

创建LSA生成定时器，超时时间*x*毫秒

Delete LS timer

删除LSA生成定时器

Restart LS timer, timeout value is *x* ms

启动LSA生成定时器，超时时间*x*毫秒

Reset LS timer, timeout value is *x* ms

重置LSA生成定时器，超时时间*x*毫秒

表1-23 debugging ospf timer spf命令输出信息描述表

字段

描述

OSPF *process-id*

OSPF进程号

Create SPF timer, timeout value is *x* ms

创建SPF计算定时器，超时时间*x*毫秒

Delete SPF timer

删除SPF计算定时器

Restart SPF timer, timeout value is *x* ms

启动SPF计算定时器，超时时间x毫秒

Reset SPF timer, timeout value is *x* ms

重置SPF计算定时器，超时时间*x*毫秒

【举例】

\# Router A通过GigabitEthernet1/0/1（150.1.1.1/24）与Router B的GigabitEthernet1/0/1（150.1.1.2/24）相连，网络类型为Broadcast，在Router A上创建OSPF进程1，在OSPF进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router B上创建OSPF进程1，在GigabitEthernet1/0/1上使能OSPF功能并配置其属于区域0；在Router A上打开OSPF定时器调试信息开关并重启OSPF进程1。

\<RouterA\> debugging ospf timer

\<RouterA\> reset ospf 1 process

Reset OSPF process? [Y/N:y]

%Nov  1 10:51:04:589 2012 RouterA OSPF/5/OSPF_NBR_CHG: -MDC=1; OSPF 1 Neighbour 150.1.1.2 (GigabitEthernet1/0/1) from Full to Down

         \*Nov  1 10:51:04:598 2012 RouterA OSPF/7/DEBUG: -MDC=1;

           OSPF 1 Reset SPF timer,timeout value is 5000 ms

*// 重置SPF计算定时器，超时时间5000毫秒*

         \*Nov  1 10:51:04:634 2012 RouterA OSPF/7/DEBUG: -MDC=1;

           OSPF 1 Delete SPF timer

*// 删除SPF计算定时器*

         \*Nov  1 10:51:06:068 2012 RouterA OSPF/7/DEBUG: -MDC=1;

           OSPF 1 Create SPF timer,timeout value is 5000 ms

*// 创建SPF计算定时器，超时时间5000毫秒*

         \*Nov  1 10:51:11:553 2012 RouterA OSPF/7/DEBUG: -MDC=1;

OSPF 1 Create LS timer,timeout value is 5000 ms

*// 创建LSA生成定时器，超时时间5000毫秒*

         \*Nov  1 10:51:13:082 2012 RouterA OSPF/7/DEBUG: -MDC=1;

           OSPF 1 Reset LS timer,timeout value is 714 ms

*// 重置LSA生成定时器，超时时间714毫秒*

