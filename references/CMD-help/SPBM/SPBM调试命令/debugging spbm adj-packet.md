
**SPBM \-- SPBM调试命令 \-- debugging spbm adj-packet**

------------------------------------------------------------------------

【命令】

**[debugging spbm adj-packet **[[ **receive** \| **send** ]  **verbose** ]]

**[undo debugging spbm adj-packet **[[ **receive** \| **send** ]  **verbose** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：表示Hello报文接收调试信息开关。

**[send**]：表示Hello报文发送调试信息开关。

**[verbose**]：表示Hello报文详细信息调试信息开关。

【描述】

**[debugging spbm adj-packet**]命令用来打开SPBM Hello报文调试信息开关。**undo debugging spbm adj-packet**命令用来关闭SPBM Hello报文调试信息开关。

缺省情况下，SPBM Hello报文调试信息开关处于关闭状态。

表1-1 debugging spbm adj-packet命令输出信息描述表

字段

描述

ADJ: The MCID received from circuit *circuitName* is different from local value.

端口收到的MCID与本地值不一致，其中*circuitName*表示端口名

ADJ: The mapping between ECT and B-VLAN received from circuit *circuitName* is different from local value.

接收到的ECT与B-VLAN映射关系与本地值不一致，其中*circuitName*表示端口名

ADJ: The B-VLAN *bvlan-number* in the mapping between ECT and B-VLAN is different from local value.

接收到的ECT与B-VLAN映射关系与本地值不一致的B-VLAN，其中*bvlan-number*表示不一致的B-VLAN

ADJ: The neighbor\'s system ID changed on circuit *circuitName*.

ADJ邻居系统ID变化，其中*circuitName*表示端口名

ADJ: The neighbor changed from circuit *circuitName* to circuit *circuitName*.

ADJ邻居端口间迁移，其中*circuitName*表示端口名

ADJ: Discarded a P2P Hello packet. Reason: invalid protocol support.

P2P Hello报文被丢弃，原因是非法的协议支持信息

ADJ: Discarded a P2P Hello packet. Reason: packet length is too small.

P2P Hello报文被丢弃，原因是报文长度太小

ADJ: Discarded a P2P Hello packet. Reason: invalid packet length.

P2P Hello报文被丢弃，原因是非法的报文长度

ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: authentication failed.

P2P Hello报文被丢弃，原因是没有通过认证，其中*circuitName*表示端口名

ADJ: Discarded a P2P Hello packet. Reason: system is in disable state.

P2P Hello报文被丢弃，原因是SPBM进程处于disable状态

ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: circuit is being deleted.

P2P Hello报文被丢弃，原因是端口正在被删除，其中*circuitName*表示端口名

ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: circuit\'s link state is down.

P2P Hello报文被丢弃，原因是端口链路状态为DOWN，其中*circuitName*表示端口名

ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: circuit\'s protocol state is disable.

P2P Hello报文被丢弃，原因是端口的协议状态为disable，其中*circuitName*表示端口名

ADJ: Discarded a P2P Hello packet on circuit *circuitName*. Reason: circuit is in disable state.

P2P Hello报文被丢弃，原因是端口处于disable状态，其中*circuitName*表示端口名

ADJ: Discarded a P2P Hello packet. Reason: conflicted system ID.

P2P Hello报文被丢弃，原因是报文携带的system ID和本系统的相同

ADJ: Received a P2P Hello packet from *system-id* on circuit *circuitName*.

接收到Hello报文，其中：

·*system-id*：报文携带的系统ID

·*circuitName*：端口名称

ADJ: Discarded a P2P Hello packet. Reason: SPB area address check failed.

P2P Hello报文被丢弃，原因是区域地址与本系统不一致

ADJ: Discarded a P2P Hello packet. Reason: MSTP 4092 Instance not configured.

P2P Hello报文被丢弃，原因是没有配置MSTP 4092实例

ADJ: Discarded a P2P Hello packet. Reason: invalid protocol descriminator.

P2P Hello报文被丢弃，原因是报文头部的protocol descriminator字段非法

ADJ: Discarded a P2P Hello packet. Reason: invalid version.

P2P Hello报文被丢弃，原因是报文头部的version字段非法

ADJ: Discarded a P2P Hello packet. Reason: invalid protocol ID.

P2P Hello报文被丢弃，原因是报文头部的protocol ID字段非法

ADJ: Discarded a P2P Hello packet. Reason: invalid system ID length.

P2P Hello报文被丢弃，原因是报文头部的system ID长度字段非法

ADJ: Discarded a P2P Hello packet. Reason: invalid max area address number.

P2P Hello报文被丢弃，原因是报文头部的最大区域地址个数字段非法

ADJ: Discarded a P2P Hello packet. Reason: invalid packet type.

P2P Hello报文被丢弃，原因是报文头部的packet type字段非法

ADJ: Discarded a P2P Hello packet. Reason: invalid header length.

P2P Hello报文被丢弃，原因是报文头部长度值非法

ADJ: Discarded a P2P Hello packet. Reason: invalid circuit type.

P2P Hello报文被丢弃，原因是非法的链路类型

ADJ: Discarded a P2P Hello packet. Reason: area address TLV decode error.

P2P Hello报文被丢弃，原因是区域地址TLV解析错误

ADJ: Discarded a P2P Hello packet. Reason: protocol support TLV decode error.

P2P Hello报文被丢弃，原因是协议支持TLV解析错误

ADJ: Discarded a P2P Hello packet. Reason: authentication TLV decode error.

P2P Hello报文被丢弃，原因是认证TLV解析错误

ADJ: Discarded a P2P Hello packet. Reason: GR TLV decode error.

P2P Hello报文被丢弃，原因是GR TLV解析错误

ADJ: Discarded a P2P Hello packet. Reason: invalid MT-Port-Cap TLV length.

P2P Hello报文被丢弃，原因是MT-Port-Cap TLV长度非法

ADJ: Discarded a P2P Hello packet. Reason: invalid MT-Port-Cap sub-TLV length.

P2P Hello报文被丢弃，原因是MT-Port-Cap TLV的子TLV长度非法

ADJ: Discarded a P2P Hello packet. Reason: MT-Port-Cap TLV decode error.

P2P Hello报文被丢弃，原因是MT-Port-Cap TLV解析错误

ADJ: Discarded a P2P Hello packet. Reason: invalid multi topology ID of MT-Port-Cap TLV.

P2P Hello报文被丢弃，原因是MT-Port-Cap TLV的MTID非法

ADJ: Discarded a P2P Hello packet. Reason: invalid SPB MCID sub-TLV.

P2P Hello报文被丢弃，原因是SPB MCID sub-TLV的长度非法

ADJ: Discarded a P2P Hello packet. Reason: different MCIDs in SPB MCID sub-TLV.

P2P Hello报文被丢弃，原因是SPB MCID sub-TLV中含有多个不同的MCID

ADJ: Discarded a P2P Hello packet. Reason: invalid SPB Digest sub-TLV length.

P2P Hello报文被丢弃，原因是SPB Digest sub-TLV的长度非法

ADJ: Discarded a P2P Hello packet. Reason: different digests in SPB Digest sub-TLV.

P2P Hello报文被丢弃，原因是SPB MCID sub-TLV中含有多个不同的Digest

ADJ: Discarded a P2P Hello packet. Reason: invalid SPB Base VLAN-Identifiers sub-TLV length.

P2P Hello报文被丢弃，原因是SPB Base VLAN-Identifiers sub TLV的长度非法

ADJ: Discarded a P2P Hello packet. Reason: invalid B-VLAN in SPB Base VLAN-Identifiers sub-TLV.

P2P Hello报文被丢弃，原因是SPB Base VLAN-Identifiers sub TLV中含有非法B-VLAN

ADJ: Discarded a P2P Hello packet. Reason: invalid TLV length.

P2P Hello报文被丢弃，原因是TLV长度非法

ADJ: Sent a P2P Hello packet on circuit *circuitName*.

端口上发送P2P Hello报文，其中*circuitName*表示端口名

ADJ: The circuit *circuitName* is silent. IIH not sent.

端口处于silent状态，Hello报文发送失败，其中*circuitName*表示端口名

【举例】

\# 打开SPBM Hello报文调试信息开关。

\<Sysname\> debugging spbm adj-packet

\# 端口GigabitEthernet0/1/3下使能SPBM功能，输出下列调试信息。

\<Sysname\> sysem-view

Sysname interface gigabitethernet 0/1/3

Sysname-GigabitEthernet0/1/3 spbm enable

\*Sep 18 14:13:14:386 2012 Sysname SPBM/7/SPBM_1_ADJ: -MDC=1;

ADJ: Sent a P2P Hello packet on circuit(GigabitEthernet0/1/3).

*// 端口GigabitEthernet0/1/3上发送P2P Hello报文*

\*Sep 18 14:13:17:445 2012 Sysname SPBM/7/SPBM_1_ADJ: -MDC=1;

ADJ: Received a P2P Hello packet from 0011.2200.0a01 on circuit(GigabitEthernet0/1/3).

*// 端口GigabitEthernet0/1/3接收到系统ID为0011.2200.0a01的设备发送的Hello报文*

**SPBM \-- SPBM调试命令 \-- debugging spbm agreement-protocol**

------------------------------------------------------------------------

【命令】

**[debugging spbm agreement-protocol**[ { **all** \| **packet** \| **prt** \| **pst** \| **topology** }]]

**[undo debugging spbm agreement-protocol **[{ **all** \| **packet** \| **prt** \| **pst** \| **topology** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示SPBM AP所有的调试信息开关。

**[packet**]：表示SPBM AP的接收摘要报文调试信息开关。

**[prt**]：表示SPBM AP端口角色迁移的调试信息开关。

**[pst**]：表示SPBM AP端口状态迁移的调试信息开关。

**[topology**]：表示SPBM AP拓扑变化处理的调试信息开关。

【描述】

**[debugging spbm agreement-protocol**]命令用来打开SPBM AP的调试信息开关。**undo debugging spbm agreement-protocol**命令用来关闭SPBM AP的调试信息开关。

缺省情况下，SPBM AP的调试信息开关处于关闭状态。

表1-2 debugging spbm agreement-protocal packet命令输出信息描述表

字段

描述

FLUSH: Received a digest on port(*PortName*), RxAN is *an-value*, RxDAN is d*an-value*, RxDigest is *digest-value*{.TableTextChar}.

接收到摘要报文，包括端口名*PortName*、摘要信息*[digest-value*]{.TableTextChar}、收到的序列号RxAN为*an-value*以及 收到的确认序列号RxDAN为*dan-value*

表1-3 debugging spbm agreement-protocal prt命令输出信息描述表

字段

描述

FLUSH: Port(*PortName*) entered *state-value* state in ECT *ect-index*.

端口角色迁移信息，包括端口名*PortName*、新角色*state-value*以及ECT索引，新状态*state-value*的取值如下：

PRT%ROOT_PORT、PRT%ROOT_PROPOSED、PRT%ROOT_AGREED、PRT%ROOT_SYNCED、PRT%ROOT_REROOT、PRT%ROOT_REROOTED、PRT%ROOT_DISCARD、PRT%ROOT_FORWARD、PRT%DESIS_DESIPORT、PRT%DESIS_AGREED、PRT%DESIS_SYNCED、PRT%DESIS_RETIRED、PRT%DESIS_DISCARD、PRT%DESIS_FORWARD、PRT%STATE_INVALID

各字段%之前表示状态机名称，%之后表示具体状态

表1-4 debugging spbm agreement-protocal pst命令输出信息描述表

字段

描述

FLUSH: Port(*PortName*) entered *state-value* state in ECT *ect-index*.

端口状态迁移信息，包括端口名*PortName*、新状态*state-value*以及ECT索引*ect-index*，新状态*state-value*的取值以及含义如下：

·PST%PST_DISCARDING：丢弃状态

·PST%PST_LEARNING：学习状态

·PST%PST_FORWARDING：转发状态

·PST%PST_INVALID：非法状态

各字段%之前表示状态机名称，%之后表示具体状态

表1-5 debugging spbm agreement-protocal topo命令输出信息描述表

字段

描述

FLUSH: Topology change started, new digest is *digest-value*{.TableTextChar}, edge count is *edge-value*{.TableTextChar}.

接收到拓扑变化开始通知，包括新摘要以及拓扑边数

FLUSH: Topology change ended, new digest is *digest-value*{.TableTextChar}, edge count is *edge-value*{.TableTextChar}.

接收到拓扑变化结束通知，包括新摘要以及拓扑边数

FLUSH: Received a port role change message in ECT *ect-index* on port(*PortName*), the new port role is *role-name*{.TableTextChar}.

接收到端口角色变化通知，包括*ect-index*、端口名以及新的端口角色，端口角色名*[role-name*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·ROOT：根端口

·DESIGNATED：指定端口

·ALTERNATE：不在树上端口

【举例】

\# 使能SPBM功能，打开组播SPBM AP消息调试信息开关，当接收到拓扑变化通知时会输出下列调试信息。

\<Sysname\> debugging spbm agreement-protocal all

\*Sep 17 10:41:12:183 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Received a digest on port(GigabitEthernet0/1/3), RxAN is 1, RxDAN is 2,

 RxDigest is 0000000000000000000.

\*Sep 17 10:41:13:034 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Topology change started, new digest is 000000183d64c91f892, edge count is 0.

\*Sep 17 10:41:13:038 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Topology change ended, new digest is 000000183d64c91f892, edge count is 0.

\*Sep 17 10:41:15:876 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Received a port role change message in ECT 1 on port(GigabitEthernet0/1/3), the new port role is ROOT.

\*Sep 17 10:41:15:876 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_PORT state in ECT 1.

\*Sep 17 10:41:15:876 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_AGREED state in ECT 1.

\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_REROOT state in ECT 1.

\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_FORWARD state in ECT 1.

\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PST%PST_DISCARDING state in ECT 1.

\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PST%PST_FORWARDING state in ECT 1.

\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PRT%ROOT_REROOTED state in ECT 1.

\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Received a port role change message in ECT-Index 1 on circuit(GigabitEthernet0/1

/3), the new port role is DESIGNATED.

\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PRT%DESIS_DESIPORT state in ECT 1.

\*Sep 17 10:41:15:877 2012 Sysname SPBM/7/SPBM_1_AP: -MDC=1;

FLUSH: Port(GigabitEthernet0/1/3) entered PRT%DESIS_AGREED state in ECT 1.

**SPBM \-- SPBM调试命令 \-- debugging spbm error**

------------------------------------------------------------------------

【命令】

**[debugging spbm error**]

**[undo debugging spbm error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging spbm error**]命令用来打开SPBM错误调试信息开关。**undo debugging spbm error**命令用来关闭SPBM错误调试信息开关。

缺省情况下，SPBM错误调试信息开关处于关闭状态。

表1-6 debugging spbm error命令输出信息描述表

字段

描述

ADJ: IF index *if-index* set ADJ socket option *operation*{.TableTextChar} failed.

设置socket选项失败，其中：

·*if-index*：端口索引

·*[operation*]{.TableTextChar}：选项{.TableTextChar}

ADJ: Failed to start Level-1 Hello timer.

Hello定时器创建失败

ADJ: System state is disabled.

进程处于disable状态

ADJ: Failed to start hold timer.

邻居维持定时器创建失败

ADJ: Failed to encode SPB MCID sub-TLV.

封装SPB-MCID sub TLV失败

ADJ: Failed to encode SPB digest sub-TLV.

封装SPB-Digest sub TLV失败

ADJ: Failed to encode SPB Base VLAN-Identifiers sub-TLV.

封装SPB-Base VID sub TLV失败

ADJ: Failed to encode packet header on circuit *circuitName*.

封装专用报文头编码失败，其中*circuitName*表示端口名

ADJ: Failed to encode area address TLV on circuit *circuitName*.

封装区域地址TLV编码失败，其中*circuitName*表示端口名

ADJ: Failed to encode protocol support TLV on circuit *circuitName*.

封装协议支持TLV编码失败，其中*circuitName*表示端口名

ADJ: Failed to encode graceful restart TLV on circuit *circuitName*.

封装优雅重启TLV失败，其中*circuitName*表示端口名

ADJ: Failed to encode MT-Port-Cap TLV on circuit *circuitName*.

封装MT-Port-Cap TLV失败，其中*circuitName*表示端口名

ADJ: Failed to send P2P Hello packet. Reason: *reason*.

P2P Hello报文发送失败，其中*reason*表示失败原因

ADJ: Failed to send P2P Hello packet. Reason: socket not create.

P2P Hello报文因套接字未创建发送失败

ADJ: Failed to send P2P Hello packet. Reason: out of memory.

P2P Hello报文因内存不足发送失败

ADJ: Failed to create P2P Hello timer on circuit *circuitName*.

P2P hello定时器创建失败，其中*circuitName*表示端口名

UPDT: LSP with too long area address.

LSP报文中携带的区域地址长度超过最大区域地址长度，丢弃报文

UPDT:  LSP with wrong area address length.

LSP报文中携带的区域地址长度错误，丢弃报文

UPDT:  LSP with invalid area address.

LSP报文中携带的区域地址长度不合法，丢弃报文

MAIN: Failed to process the LSP lifetime change event.

处理LSP报文生存时间变化时间失败

MAIN: Failed to activate the interface *circuitName*.

端口激活失败，其中*circuitName*表示端口名

MAIN: Failed to process the circuit MTU change event.

端口MTU变化处理失败

MAIN: The event type and disable phase mismatched.

进程的Reset状态和阶段不一致

UPDT: Wrong format of neighbor TLV in LSP.

LSP报文中携带的邻居格式错误，丢弃报文

UPDT: Wrong format of I-SID TLV in LSP.

LSP报文中携带的I-SID格式错误，丢弃报文

UPDT: Wrong format of MT-Capability TLV in LSP.

LSP报文中携带的多拓扑能力格式错误，丢弃报文

UPDT: Wrong format of Instance sub-TLV in LSP.

LSP报文中携带的实例格式错误，丢弃报文

UPDT: Supported protocol wrong.

协议支持TLV中携带的协议支持与本系统不匹配

UPDT: Failed to create UPDT sockets.

创建UPDT套接字失败

UPDT: Bad TLV in the received LSP.

LSP报文中携带的TLV错误（该TLV没有长度字节），丢弃报文

UPDT: Bad TLV length in the received LSP.

LSP报文中携带的TLV长度错误，丢弃报文

UPDT: Failed to start CSNP timer on circuit *circuitName.*

端口CSNP定时器创建失败，其中*circuitName*表示端口名

UPDT: Failed to start PSNP timer on circuit *circuitName.*

端口PSNP定时器创建失败，其中*circuitName*表示端口名

UPDT: Failed to start P2P retransmit timer on circuit *circuitName*.

端口P2P重传定时器创建失败，其中*circuitName*表示端口名

UPDT: Failed to start LSP flood timer on circuit *circuitName*.

端口LSP泛洪定时器创建失败，其中*circuitName*表示端口名

UPDT: Failed to stop LSP flood timer on circuit *circuitName.*

关闭端口LSP泛洪定时器失败，其中*circuitName*表示端口名

UPDT: Failed to stop level-1 timer on circuit *circuitName.*

关闭端口level-1定时器失败，其中*circuitName*表示端口名

UPDT: LSP information update failed.

LSDB中的LSP信息更新失败

UPDT: LSP insert failed.

向LSP中添加邻居信息失败

UPDT: Bad TLV length in the process of LSP authentication.

认证LSP时TLV长度错误，丢弃报文

UPDT: LSP\'s sequence number is 0.

接收到的LSP报文的序列号为0，丢弃报文

UPDT: Illegal IS type in level-1 LSP.

Level-1 LSP报文的IS-TYPE字段非法，丢弃报文

UPDT: Checksum is zero.

LSP报文的校验和为0，丢弃报文

UPDT: Checksum error.

LSP报文的校验和错误，丢弃报文

UPDT: Failed to set UPDT socket option.

设置UPDT套接字失败

UPDT: The PDU was discarded because its size(*PDUSize*) is greater than received buffer size(*reveiveBufSize*).

LSP/SNP报文长度大于接收缓冲区大小，丢弃报文

UPDT: The PDU was discarded because its size(*PDUSize*) is less than common PDU header size(*PDUCommonHeaderSize*).

LSP/SNP报文长度小于公共报文头大小，丢弃报文

UPDT: The PDU was discarded because its size(*PDUSize*) is less than fixed PDU header size(*PDUFixedHeaderSize*).

LSP/SNP报文长度小于固定报文头大小，丢弃报文

UPDT: The PDU was discarded due to length mismatch: receive length= *recvLen*, encode length= *encodeLen.*

LSP/SNP报文长度和报文中的长度字段不相等，丢弃报文

UPDT: The PDU was discarded because the SPBM process is not available.

进程不可用，忽略LSP/SNP报文

UPDT: The PDU was discarded because circuit *circuitName* was being deleted.

端口正在删除，忽略LSP/SNP报文，其中*circuitName*表示端口名

UPDT: The PDU was discarded because circuit *circuitName* was not up.

端口链路状态没有UP，忽略LSP/SNP报文，其中*circuitName*表示端口名

UPDT: The PDU was discarded because circuit *circuitName* was in silence state.

端口处于Silence状态，忽略LSP/SNP报文，其中*circuitName*表示端口名

UPDT: The PDU was discarded due to LSP or SNP PDU common header error.

LSP/SNP公共报文头错误，丢弃报文

UPDT: The PDU was discarded because no active adjacency exist on cicuit *circuitName*.

端口上没有激活的邻居，忽略LSP/SNP报文

UPDT: Failed to process SNP PDU.

SNP报文处理失败

UPDT: Failed to process LSP PDU.

LSP报文处理失败

UPDT: The PDU was discarded because received PDU was not LSP or SNP.

接收到的报文不是LSP或SNP报文，丢弃报文

UPDT: LSP size(*LSPSize*) is larger than circuit MTU(*circuitMtu*).

LSP报文大小大于发送端口的MTU，其中：

·*LSPSize*：LSP报文大小

·*circuitMtu*：发送端口的MTU

UPDT: Failed to send LSP.

LSP报文发送失败

UPDT: Failed to send level-1 PSNP PDU.

level-1 PSNP发送失败

UPDT: Failed to send level-1 CSNP PDU.

level-1 CSNP发送失败

UPDT: Invalid LSP-ID reported in SNP.

SNP报文中的LSP ENTRY的LSP-ID错误

UPDT: Wrong LSP entry TLV length(*LSPEntryTlvLen*) in SNP.

SNP报文中的LSP ENTRY TLV长度错误，其中*LSPEntryTlvLen*表示LSP ENTRY TLV长度

UPDT: SNP contain too many LSP entries.

SNP报文中的LSP ENTRY个数多过

UPDT: Invalid TLV in SNP.

SNP报文中的TLV非法

UPDT: Wrong TLV length in SNP.

SNP报文中的TLV长度错误

UPDT: Failed to install LSP with seq number zero.

安装序列号为0的LSP失败

UPDT: Invalid type of SNP PDU.

SNP报文类型非法

UPDT: Failed to create zero-frag LSP.

创建零分片失败

UPDT: Failed to initiate zero-frag LSP.

初始化零分片失败

UPDT: LSP\'s PDU length is smaller than LSP\'s header length.

安装PDU长度小于头长度的LSP失败

UPDT: Illegal LSP level.

安装非Level-1的LSP失败

UPDT: Illegal IS type in level-1 LSP.

安装非IS_UPDT_LSP_L1_ISTYPE的LSP失败

UPDT: SNP\'s PDU length is smaller than SNP\'s header length.

SNP的PDU长度小于SNP的头长度

UPDT: Bad TLV in the received SNP.

收到的SNP里存在没有Length字节的TLV

UPDT: Bad TLV in the received LSP.

LSP里存在没有Length字节的TLV

UPDT: Failed to add area address *address.*

添加区域地址TLV失败，其中*address*表示区域地址

UPDT: Failed to add protocol support *protocol.*

添加协议支持TLV失败，其中*protocol*表示协议

UPDT: Failed to add host name *name.*

添加host name TLV失败，其中*name*表示主机名

UPDT: Failed to delete host name *name.*

删除host name TLV失败，其中*name*表示主机名

UPDT: Failed to add Instance sub-TLV: B-VLAN= *bvlan-number*, u-bit= *u-bit*, ECT-Algorithm= *ect-algorithm.*

添加Instance TLV失败，其中：

·*bvlan-number*：B-VLAN值

·*u-bit*：u比特位

·*ect-algorithm*：ECT算法

UPDT: Failed to modify Instance sub-TLV: B-VLAN= *bvlan-number*, u-bit= *u-bit*, ECT-Algorithm= *ect-algorithm.*

修改Instance TLV失败，其中：

·*bvlan-number*：B-VLAN值

·*u-bit*：u比特位

·*ect-algorithm*：ECT算法

UPDT: Failed to delete Instance sub-TLV: B-VLAN= *bvlan-number*

删除Instance TLV失败，其中*bvlan-number*表示B-VLAN值

UPDT: Failed to add I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid*, T-flag= *t-flag*, R-flag= *r-flag.*

添加I-SID TLV失败，其中：

·*bvlan-number*：B-VLAN值

·*i-sid*：I-SID值

·*t-flag*：T标志位

·*r-flag*：R标志位

UPDT: Failed to modify I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid*, T-flag= *t-flag*, R-flag= *r-flag.*

修改I-SID TLV失败，其中：

·*bvlan-number*：B-VLAN值

·*i-sid*：I-SID值

·*t-flag*：T标志位

·*r-flag*：R标志位

UPDT: Failed to delete I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid.*

删除I-SID TLV失败，其中：

·*bvlan-number*：B-VLAN值

·*i-sid*：I-SID值

UPDT: Failed to add neighbor TLV: neighbor system ID= *system-id*, cost= *cost.*

添加邻居TLV失败，其中：

·*system-id*：邻居系统ID

·*cost*：cost值

UPDT: Failed to modify neighbor TLV: neighbor system ID= *system-id*, cost= *cost.*

修改邻居TLV失败，其中：

·system-id：邻居系统ID

·*cost*：cost值

UPDT: Failed to delete neighbor TLV: neighbor system ID= *system-id.*

删除邻居TLV失败，其中*system-id*表示邻居系统ID

UPDT: Wrong format of authentication TLV in the SNP.

CSNP/PSNP报文中的认证TLV的长度或模式字段错误，报文丢弃

UPDT: Wrong format of authentication TLV in the LSP.

LSP报文中的认证TLV的长度或模式字段错误，报文丢弃

【举例】

\# 使能SPBM功能，打开SPBM错误信息调试信息开关，输出下列调试信息。

\<Sysname\> debugging spbm error

\*Sep 18 11:33:39:706 2012 Sysname SPBM/7/SPBM_1_ERR: -MDC=1;

UPDT: Failed to stop LSP flood timer on circuit GigabitEthernet0/1/3.

**SPBM \-- SPBM调试命令 \-- debugging spbm event**

------------------------------------------------------------------------

【命令】

**[debugging spbm event**]

**[undo debugging spbm event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging spbm event**]命令用来打开SPBM 事件的调试信息开关。**undo debugging spbm event**命令用来关闭SPBM 事件的调试信息开关。

缺省情况下，SPBM 事件的调试信息开关处于关闭状态。

表1-7 debugging spbm event命令输出信息描述表

字段

描述

ADJ: Received Hello timer reset event on interface *circuitName*.

ADJ模块端口重置Hello定时器，其中*circuitName*表示端口名

ADJ: Received digest change event on interface *circuitName*. Send speed is *state*.

ADJ模块摘要变化事件处理，其中：

·*circuitName*：端口名

·*state*：Hello定时器状态

ADJ: Received state change event on interface *circuitName*: *eventType*.

ADJ模块收到端口状态改变事件，其中：

·*circuitName*：端口名

·*eventType*：事件类型

ADJ: Received Instance 4092 delete event.

ADJ模块收到Instance 4092删除消息

ADJ: Received control address change event.

ADJ模块收到control address变化事件

FLUSH: Notified  MSTP B-VLAN change, message length= *length-value*.

FLUSH模块发送MSTP B-VLAN变化消息，其中*length-value*表示消息长度

FLUSH: *Operation*{.TableTextChar} SPBM on interface *circuitName*, result= *result*.

FLUSH模块发送接口使能/去使能SPBM信息，其中：

·*[operation*]{.TableTextChar}：使能或去使能

·*circuitName*：端口名

·*result*：处理结果

MAIN: Notified to modify P2P Hello timer on interface *circuitName*.

通知邻居模块端口Hello定时器配置发生变化，其中*circuitName*表示端口名

MAIN: Notified to modify SPB Base VLAN-Identifiers sub-TLV.

通知修改SPB Base VLAN-Identifiers sub-TLV

MAIN: *flag-value* SPBM PDU up to CPU on interface *circuitName*, control mac: *mac-addr*, result: *result*.

通知驱动使能报文上送CPU，其中：

·*flag-value*：是否使能标记

·*circuitName*：端口名

·*mac-addr*：MAC地址

·*result*：处理结果

MAIN: Notified metric change event on interface *circuitName*.

通知邻居模块端口cost配置发生变化，其中*circuitName*表示端口名

MAIN: Refreshed the SPBM interface parameter on interface *circuitName*.

刷新端口参数变化，其中*circuitName*表示端口名

MAIN: Received delete event on interface *circuitName*.

MAIN模块接收到端口删除事件，其中*circuitName*表示端口名

MAIN: Received pre-delete event on interface *circuitName*.

MAIN模块接收到端口删除前的Deactive事件，其中*circuitName*表示端口名

MAIN: Received active event on interface *circuitName*.

MAIN模块接收到板插入事件，其中*circuitName*表示端口名

MAIN: Received deactive event on interface *circuitName*.

MAIN模块接收到板拔出事件，其中*circuitName*表示端口名

MAIN: Received join aggregation group event on interface *circuitName*.

端口加入聚合组，清除配置，其中*circuitName*表示端口名

MAIN: Received leave aggregation group event on interface *circuitName*.

端口离开聚合组，清除配置，其中*circuitName*表示端口名

MAIN: Received up event on interface *circuitName*.

MAIN模块接收到物理端口DOWN到UP事件，其中*circuitName*表示端口名

MAIN: Received down event on interface *circuitName*.

MAIN模块接收到物理端口UP到DOWN事件，其中*circuitName*表示端口名

MAIN: Received speed change event on interface *circuitName*.

MAIN模块接收到物理端口速率变化事件，其中*circuitName*表示端口名

MAIN: Notified interface state change: *changestate*.

通知端口状态变化，其中*changestate*表示状态变化

MAIN: Received time message from SPBM to License daemon, ignored.

License Daemon接收到定时通知消息

MAIN: Started timer to reconnect to License daemon. Time value is *Millisecond* ms.

创建SPBM进程与License进程的重连定时器，其中*Millisecond*表示定时器的当前事件间隔

MAIN: Failed to start timer for reconnecting to License daemon.

SPBM进程与License进程的重连定时器创建失败

MAIN: Trying to connect with MSTP.

尝试与MSTP连接

MAIN: Connected with MSTP successfully.

与MSTP连接成功

MAIN: Reset finished, reset reason= *event-id.*

进程Reset结束事件，其中*event-id*表示触发reset的事件ID

MAIN: Processing with reset backinfo: module= *moudle-id*, event= *event-id*, phase= *phase-id*.

进程Reset的阶段信息，其中：

·*moudle**-id*：模块ID

·*event**-id*：触发reset的事件ID

·*phase**-id*：reset所处的阶段

MAIN: Invalid phase= *phase-id*, ignore event.

进程Reset的阶段错误，忽略消息，其中*phase-id*表示reset所处的阶段

MAIN: Reset change into phase *phase-id*.

进程Reset进入下一个阶段，其中*phase-id*表示reset所处的阶

MAIN: Received resetting message, triggered type= *event-id*.

进程收到Reset触发事件，其中*event-id*表示触发reset的事件ID

MAIN: Notified other module to enter reset process.

通知其他模块进入Reset处理

MAIN: LSP MTU changed from *oldLspBuf* to *newLspBuf*, notified UPDT MTU to change.

进程LSP缓冲区的大小改变，其中：

·*oldLspBuf*：LSP缓冲区之前的大小

·*newLspBuf*：新的LSP缓冲区的大小

MAIN: Notified to add SPB Instance sub-TLV: process-ID= *proc-id*, ECT-index= *ect-index*, B-VLAN= *bvlan-number*, u-bit= *u-bit*.

通知添加SPB Instance sub-TLV，其中：

·*proc**-id*：SPBM进程号

·*ect-index*：ECT索引

·*bvlan-number*：B-VLAN

·*u-bit*：B-VLAN下是否已配置I-SID

MAIN: Notified to modify SPB Instance sub-TLV: process-ID= *proc-id*, ECT-index= *ect-index*, B-VLAN= *bvlan-number*, u-bit= *bUsed*.

通知修改SPB Instance sub-TLV，其中：

·*proc**-id*：SPBM进程号

·*ect-index*：ECT索引

·*bvlan-number*：B-VLAN

·*bUsed*：B-VLAN下是否已配置I-SID

MAIN: Notified to delete SPB Instance sub-TLV: process-ID= *proc-id*, B-VLAN= *bvlan-number*.

通知删除SPB Instance sub-TLV，其中：

·*proc**-id*：SPBM进程号

·*bvlan-number*：B-VLAN

MAIN: Notified AP mode change to *ap-mode*.

通知FLUSH模块AP模式变化，其中*ap-mode*表示AP 模式

MAIN: Notified ADJ to reset Hello timer.

通知ADJ模块重置Hello定时器

MAIN: Received MSTP MCID change event.

接收到MSTP MCID变化事件

MAIN: Received MSTP B-VLAN change event.

接收到MSTP B-VLAN变化信息

MAIN: Trying to connect with SNMP.

尝试与SNMP建立连接

MAIN: Connected with SNMP successfully.

与SNMP建立连接成功

MAIN: Notified neighbor down event to UPDT.

通知UPDT模块邻居DOWN信息

MAIN: Notified neighbor up event to UPDT.

通知UPDT模块邻居UP信息

MAIN: Notified ADJ that Instance 4092 had been deleted.

通知ADJ模块4092实例被删除

MAIN: Started to set replicate mode on VSI *vsi-name*: VSI-index= *vsi-index*, replicate mode= *rep-mode*.

设置复制模式，其中：

·*vsi-name*：VSI名

·*vsi-index*：VSI索引

·*rep-mode*：模式值

MAIN： Ended to set replicate mode on VSI *vsi-name*: result= *result*

设置复制模式完成，其中：

·*vsi-name*：VSI名

·*re**sult*：返回值

MAIN: Started to create VSI control block: VSI-name *vsi-name*, VSI-index= *vsi-index,* I-SID= *i-sid.*

创建VSI控制块，其中：

·*vsi-name*：VSI名

·*vsi-index*：VSI索引

·*i-sid*：I-SID值

MAIN： Notified multicast replicate mode to change. SysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number.*

通知组播复制模式变化，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

MAIN： Notified to add SPBM Service Identifier sub-TLV. SysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*, replicate mode= *rep-mode*.

通知添加SPBM服务标识子TLV，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

·*rep-mode*：模式值

MAIN： Notified to modify SPBM Service Identifier sub-TLV. SysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number,* replicate mode= *rep-mode*.

通知修改SPBM服务标识子TLV，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

·*rep-mode*：模式值

MAIN： Notified to delete SPBM Service Identifier sub-TLV. SysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*.

通知删除SPBM服务标识子TLV，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

MAIN: VSI *vsi-name* link state changed from up to down.

VSI链路状态从UP到DOWN，其中*vsi-name*表示VSI名

MAIN: VSI *vsi-name* link state changed from down to up.

VSI链路状态从DOWN到UP，其中*vsi-name*表示VSI名

MAIN: Started to modify VSI control block: VSI-name *vsi-name*, VSI-index= *vsi-index*, I-SID= *i-sid*.

修改VSI控制块，其中：

·*vsi-name*：VSI名

·*vsi-index*：VSI索引

·*i-sid*：I-SID值

MAIN: Started to delete VSI control block: VSI-name *vsi-name*.

删除VSI控制块，其中*vsi-name*表示VSI名

MAIN: Received VSI add event.

接收到VSI添加事件

MAIN: Received VSI delete event.

接收到VSI删除事件

MAIN: Received VSI I-SID change event.

接收到VSI和I-SID变化事件

MAIN: Received VSI state change event.

接收到VSI状态变化事件

MAIN: Received VSI AC state change event.

接收到VSI AC侧状态变化事件

MAIN: Received L2VPN global disable event.

接收到L2VPN全局去使能事件

MAIN: L2VPN started to push VSI information.

L2VPN开始上报VSI事件

MAIN: L2VPN stopped to push VSI information.

L2VPN上报VSI事件结束

MAIN: Trying to connect with L2VPN.

尝试与L2VPN连接

UPDT: Received LSP change event.

UPDT模块收到LSP报文改变事件

UPDT: Received state change event on interface *circuitName*: *eventType*.

UPDT模块收到端口状态改变事件，其中：

·*circuitName*：端口名

·*eventType*：事件类型

UPDT: Received authentication change event.

UPDT模块收到认证改变事件

UPDT: Received level-1 fast flood event.

UPDT模块收到fast flood快速扩散事件

UPDT: Received control address change event. Socket recreated.

UPDT模块收到控制地址改变事件

UPDT: ECT migration All-no-T timer started. I-SID= *i-sid*.

ECT迁移的All-no-T定时器启动信息，其中：

·*i-sid*：I-SID值

·T：T-flag为1

UPDT: ECT migration All-R timer started. I-SID= *i-sid*.

ECT迁移的All-R定时器启动信息，其中：

·*i-sid*：I-SID值

·R：R-flag为1

UPDT: ECT migration Finish timer started. I-SID= *i-sid*.

ECT迁移的全网同步定时器启动信息，其中*i-sid*为I-SID

UPDT: ECT migration All-no-T timer stopped. I-SID= *i-sid*.

ECT迁移的All-no-T定时器停止信息，其中：

·*i-sid*：I-SID值

·T：T-flag为1

UPDT: ECT migration All-R timer stopped. I-SID= *i-sid*.

ECT迁移的All-R定时器停止信息，其中：

·*i-sid*：I-SID值

·R：R-flag为1

UPDT: ECT migration Finish timer stopped. I-SID= *i-sid*.

ECT迁移的全网同步定时器停止信息，其中*i-sid*表示I-SID

UPDT: Received I-SID FSM state change event: sysIndex= *sysindex*, I-SID= *i-sid*, event= *event type*.

I-SID状态机变化信息，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*event type*：事件类型

UPDT: I-SID FSM notified UPDT to add SPBM Service Identifier sub-TLV: sysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*.

创建I-SID状态机时通知UPDT模块添加Service Identifier sub-TLV，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

UPDT: I-SID FSM notified UPDT to add SPBM Service Identifier sub-TLV: sysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *transmit flag*, R-flag= *receive flag*.

I-SID状态机变化通知UPDT模块添加Service Identifier sub-TLV，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

·*transmit flag*：转发标记

·*receive flag*：接收标记

UPDT: I-SID FSM notified UPDT to delete SPBM Service Identifier sub-TLV: sysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*.

I-SID状态机变化通知UPDT模块删除Service Identifier sub-TLV，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

UPDT: I-SID FSM notified UPDT to modify SPBM Service Identifier sub-TLV: sysIndex= *sysindex*, I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *transmit flag*, R-flag= *receive flag*.

I-SID状态机变化通知UPDT模块修改Service Identifier sub-TLV，其中：

·*sysindex*：系统索引

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

·*transmit flag*：转发标记

·*receive flag*：接收标记

【举例】

\# 使能SPBM功能，打开SPBM事件调试信息开关。

\<Sysname\> debugging spbm event

\# 端口上去使能SPBM，会输出下列调试信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 0/1/3

Sysname-GigabitEthernet0/1/3 undo spbm enable

\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

MAIN: Disable SPBM PDU up to CPU on interface GigabitEthernet0/1/3, control mac= 0180-c200-002e, result= 0.

\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_EVT: -MDC=1;

MAIN: Disable VSI AC packet up to interface GigabitEthernet0/1/3, result= 0.

\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

MAIN: Notified interface state change: Enable \--\> Disable.

\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

MAIN: Notified interface state change: Up \--\> Down.

\*Dec 26 12:57:09:814 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

ADJ: Received state change event on interface GigabitEthernet0/1/3: Disable.

\*Dec 26 12:57:09:815 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

ADJ: Received state change event on interface GigabitEthernet0/1/3: Up\--\>Down.

%Dec 26 12:57:09:815 2012 Sysname SPBM/5/SPB_NBR_CHG: -MDC=1; SPBM 1, Level-1 adjace

ncy 0011.2200.0101 (GigabitEthernet0/1/3), state changed to DOWN.

\*Dec 26 12:57:09:816 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

UPDT: Received state change event on interface GigabitEthernet0/1/3: Disable.

\*Dec 26 12:57:09:816 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

UPDT: Received state change event on interface GigabitEthernet0/1/3: Up\--\>Down.

\*Dec 26 12:57:09:816 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

MAIN: Notified neighbor down event to UPDT.

\*Dec 26 12:57:09:816 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

UPDT: Received LSP change event.

**SPBM \-- SPBM调试命令 \-- debugging spbm flush**

------------------------------------------------------------------------

【命令】

**[debugging spbm flush**[ { **all** \| **event** \| **message** { **multicast-fib** \| **multicast-pw** \| **unicast-fib** \| **unicast-pw** } }]]

**[undo debugging spbm flush**[ { **all** \| **event** \| **message** { **multicast-fib** \| **multicast-pw** \| **unicast-fib** \| **unicast-pw** } }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示SPBM FLUSH所有的调试信息开关。

**[event**]：表示SPBM FLUSH的接收事件调试信息开关。

**[message**]：表示发送SPBM组播MAC添加、组播MAC删除、组播MAC出端口添加、组播MAC出端口删除、组播PW添加、组播PW删除、单播MAC刷新、单播MAC删除、单播PW添加、单播PW删除消息调试信息开关。

【描述】

**[debugging spbm flush**]命令用来打开SPBM FLUSH的调试信息开关。**undo debugging spbm flush**命令用来关闭SPBM FLUSH的调试信息开关。

缺省情况下，SPBM FLUSH的调试信息开关处于关闭状态。

表1-8 debugging spbm flush event命令输出信息描述表

字段

描述

FLUSH: Received topology message, state(*state-value*{.TableTextChar}), new digest(*digest-value*{.TableTextChar}), edge count(*edge-value*){.TableTextChar}.

接收到拓扑变化消息，状态为*[state-value*]{.TableTextChar}，新摘要为*[digest-value*]{.TableTextChar}，拓扑边数为*[edge-value*]{.TableTextChar}，*[state-value*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Start：拓扑变化开始

·End：拓扑变化结束

FLUSH: Received digest packet message, system ID (*system-id*), Port(*PortName*).

接收到摘要报文消息，包括系统ID为*system-id*和端口*PortName*

FLUSH: Received SPSource-ID change message, system ID(*system-id*), SPSource-ID(*spsource-id*).

接收到SPSource-ID变化消息，包括系统ID为*system-id*和最短路径源标识*spsource-id*

FLUSH: Received SPSource-ID delete message, system ID(*system-id*), SPSource-ID(*spsource-id*).

接收到SPSource-ID删除消息，包括系统ID为*system-id*和最短路径源标识*spsource-id*

FLUSH: Received ECT B-VLAN mapping message, Operation(*operation*{.TableTextChar}), B-VLAN(*bvlan-number*), ECT(*ect-index*{.TableTextChar}).

接收到ECT和B-VLAN映射关系变化消息，包括B-VLAN为*bvlan-number*，ECT为*[ect-index*]{.TableTextChar}，操作类型*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Refresh：刷新

·Delete：删除

FLUSH: Received BMAC message, system ID(*system-id*), Operation(*operation*{.TableTextChar}), BMAC(*macaddr-value*), B-VLAN(*bvlan-number*).

接收到BMAC变化消息，包括系统ID为*system-id*、{.TableTextChar}B[MAC{.TableTextChar}]为{.TableTextChar}*macaddr-value*、B-VLAN{.TableTextChar}为{.TableTextChar}*bvlan-number*、操作类型*operation*{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Refresh：刷新

·Delete：删除

FLUSH: Received port role message, system ID (*system-id*), ECT (*ect-index*{.TableTextChar}), PortRole(*role-name*{.TableTextChar}), Port(*PortName*).

接收到端口角色变化消息，包括系统ID为*system-id*、ECT为*[ect-index*]{.TableTextChar}、端口角色为*[role-name*]{.TableTextChar}和端口名*PortName*，端口角色名*[role-name*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·ROOT：根端口

·DESIGNATED：指定端口

·ALTERNATE：不在树上端口

FLUSH: Received reset message, type(*operation*{.TableTextChar}).

接收到reset过程中主线程和其他线程的交互消息，*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Stopwork：停止工作

·Disable：去使能

·Enable：使能

FLUSH: Received I-SID B-VLAN mapping message, I-SID(*i-sid*{.TableTextChar}), TRB-VLAN(*bvlan-number*), RB-VLAN(*bvlan-number*).

接收到拓扑中I-SID和B-VLAN映射关系变化消息，包括I-SID为*[i-sid*]{.TableTextChar}、TRB-VLAN为*bvlan-number*和RB-VLAN为*bvlan-number*

FLUSH: Received I-SID B-VLAN item message, system ID(*system-id*), Operation(*operation*{.TableTextChar}), I-SID(*i-sid*{.TableTextChar}), B-VLAN(*bvlan-number*).

接收到节点I-SID和B-VLAN映射关系变化消息，包括I-SID、system ID和B-VLAN，*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Refresh：刷新

·Delete：删除

FLUSH: Received AP mode message, AP mode(*value*{.TableTextChar}).

接收到AP模式变化消息，*[value*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Mcast：仅支持组播

·Both：两种都支持

·Off：AP关闭

FLUSH: Received configuration message. 

接收到命令行消息

FLUSH: Received thread message, type(*operation*{.TableTextChar}).

接收到线程操作消息，*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Stop_Work：停止工作

·Start_Work：开始工作

·Quit：退出

FLUSH: Received FDB smooth start message(support GR).

接收FDB表项平滑开始消息（支持GR）

FLUSH: Received FDB smooth start message(not support GR).

接收FDB表项平滑开始消息（不支持GR）

FLUSH:Received FDB smooth end message.

接收FDB表项平滑结束消息

FLUSH: Received PW smooth start message(support GR).

接收PW表项平滑开始消息（支持GR）

FLUSH: Received PW smooth start message(not support GR).

接收PW表项平滑开始消息（不支持GR）

FLUSH:Received PW smooth end message.

接收PW表项平滑结束消息

FLUSH: Received PW reflush message.

接收到PW表项重刷消息

FLUSH:Received set egress-flag message, system ID(*system-id*), Operation(*operation*{.TableTextChar}), I-SID(*i-sid*).

接收到设置egress-flag消息，包括系统ID为*system-id*、操作类型为*[operation*]{.TableTextChar}，I-SID为*i-sid*，*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Refresh：刷新

·Delete：删除

FLUSH: Received replicate mode change message, I-SID(*i-sid*), replicate mode (*rep-mode*).

接收到模式改变消息，包括I-SID为*i-sid*、工作模式为*rep-mode*，*rep-mode*的取值及含义如下：

·tandem：核心复制

·head-end：头端复制

表1-9 debugging spbm flush message unicast-fib命令输出信息描述表

字段

描述

FLUSH: Sent the message for *operation* {.TableTextChar}unicast MAC entry*,* {.TableTextChar} length= *length-value.*

具体某一个单播MAC表项消息的头部，包括消息长度为*length-value*（不包括本消息头）和消息操作类型*[operation*]{.TableTextChar}，*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·refreshing：刷新

·deleting：删除

Unicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*) Port(*PortName*) RouteFlag(*flag-value*).

具体某一个单播MAC表项消息的内容，MAC为*macaddr-value*，B-VLAN为*bvlan-number*，Port为*PortName*，RouteFlag为*flag-value*

Sent the message for starting to smooth FDB entry.

发送FDB平滑开始消息

Sent the message for ending to smooth FDB entry.

发送FDB平滑结束消息

表1-10 debugging spbm flush message multicast-fib命令输出信息描述表

字段

描述

FLUSH: Sent the message for *operation*{.TableTextChar} multicast MAC entry, length= *length-value.*

具体某一个组播MAC表项消息的头部，包括消息长度（不包括本消息头）和消息类型*[operation*]{.TableTextChar}，*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·refreshing：刷新

·deleting：删除

Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan -number*) OutIFNum(*number*) RouteFlag(*flag-value*).

具体某一个组播MAC表项消息的内容，MAC为*macaddr-value*，B-VLAN为*bvlan-number*，出端口数目为*number*，RouteFlag为*flag-value*

FLUSH: Port List:

         Port(*PortName*)

出端口列表，Port为*PortName*

FLUSH: Sent the message for *operation*{.TableTextChar} multicast MAC iflist, length= *length-value.*

具体某一个组播MAC出端口消息的头部，包括消息长度为*length-value*（不包括本消息头）和消息类型*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·adding：添加

·deleting：删除

Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*) Port(*PortName*) RouteFlag(*flag-value*).

具体某一个组播MAC出端口消息的内容，MAC为*macaddr-value*，B-VLAN为*bvlan-number*，出端口为*PortName*，RouteFlag为*flag-value*

Sent the message for starting to smooth FDB entry.

发送FDB平滑开始消息

Sent the message for ending to smooth FDB entry.

发送FDB平滑结束消息

表1-11 debugging spbm flush message unicast-pw命令输出信息描述表

字段

描述

FLUSH: Sent the message for *operation*{.TableTextChar} unicast MINM entry, I-SID(*i-sid*), B-VLAN(*bvlan-number*), Port(*PortName*) , VSI-name(*vsi-name*), Flag(*flag-value*),D-BMAC(*macaddr-value*), S-BMAC(*macaddr-value*), S-CMAC(*macaddr-value*).

发送单播PW表项消息，包括I-SID、B-VLAN、端口Port、VSI-name、Flag、MINM连接key信息中的DBMAC、MINM表项信息中骨干网源BMAC、用户源MAC，*flag-value*的取值以及含义如下：{.TableTextChar}

· MINM_SPB \| MINM_UNICAST \| MINM_COREREPLICATE：SPB单播核心复制

· MINM_SPB \| MINM_UNICAST \| MINM_HEADREPLICATE：SPB单播头端复制

*operation*{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·adding：添加

·deleting：删除

FLUSH: For receiving packet only, B-VLAN (*bvlan-number*), Port(*PortName*).

ECT迁移过程中只收报文的单播端口信息，包括B-VLAN *bvlan-number*和端口名*PortName*

Sent the message for starting to smooth PW entry.

发送平滑pw开始消息

Sent the message for ended to smooth PW entry.

发送平滑pw结束消息

表1-12 debugging spbm flush message multicast-pw命令输出信息描述表

字段

描述

FLUSH: Sent the message for *operation*{.TableTextChar} multicast MINM entry, I-SID (*i-sid*), B-VLAN(*bvlan-number*), Port number(*number*), VSI-name(*vsi-name*), Flag(*flag-value*), D-BMAC(*macaddr-value*), S-BMAC(*macaddr-value*), S-CMAC(*macaddr-value*).

发送组播PW表项消息，包括I-SID、B-VLAN、端口个数Port number、VSI-name、Flag、MINM连接key信息中的D-BMAC、MINM表项信息中骨干网源BMAC、用户源MAC，*flag-value*的取值以及含义如下：{.TableTextChar}

· MINM_SPB \| MINM_MULTICAST \| MINM_COREREPLICATE：SPB组播核心复制

· MINM_SPB \| MINM_MULTICAST \| MINM\_ HEADREPLICATE：SPB组播头端复制

*operation*{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·adding：添加

·deleting：删除

 FLUSH: Port List:

          Port(*PortName*)

出端口列表，Port为*PortName*

FLUSH: Sent the message for *operation*{.TableTextChar} multicast MINM port, I-SID (*i-sid*), B-VLAN(*bvlan-number*), Port (*PortName*) VSI-name(*name*), Flag(*flag-value*),

D-BMAC(*macaddr-value*), S-BMAC(*macaddr-value*), S-CMAC(*macaddr-value*).

发送组播PW出端口消息，包括I-SID、B-VLAN、端口名Port、VSI-name、Flag、MINM连接key信息中的DBMAC、MINM表项信息中骨干网源BMAC、用户源MAC，*flag-value*的取值以及含义如下：{.TableTextChar}

· MINM_SPB \| MINM_MULTICAST \| MINM_COREREPLICATE：SPB组播核心复制

· MINM_SPB \| MINM_MULTICAST \| MINM\_ HEADREPLICATE：SPB组播头端复制

*operation*{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·adding：添加

·deleting：删除

【举例】

\# 使能SPBM功能，打开单播组播SPBM FLUSH事件调试信息开关，当SPBM FLUSH接收到事件通知时会输出下列调试信息。

\<Sysname\> debugging spbm flush event

\<Sysname\> \*Sep 17 10:08:54:792 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received SPSource-ID change message, system ID(0011.2200.0001), SPSource-ID(90967).

\*Sep 17 10:08:54:793 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received ECT B-VLAN mapping message, Operation(Refresh), B-VLAN(1), ECT (1).

\*Sep 17 10:08:54:793 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received ECT B-VLAN mapping message, Operation(Refresh), B-VLAN(2), ECT (1).

\*Sep 17 10:08:54:794 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received BMAC message, system ID(0011.2200.0001), Operation(Refresh), BMAC(0011-2200-0001) , B-VLAN(1).

\*Sep 17 10:08:54:794 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received BMAC message, system ID(0011.2200.0001), Operation(Refresh), BMAC(0011-2200-0001), B-VLAN(2).

\*Sep 17 10:11:00:412 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received digest packet message, system ID(0011.2200.0a01), Port(GigabitEthernet0/1/3).

\*Sep 17 10:11:03:296 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received topology message, state(Start), new digest(000000365981264d9ff), edge count(2).

\*Sep 17 10:11:03:297 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received port role message, system ID(0011.2200.0a01), ECT (1), PortRole(ROOT), Port(GigabitEthernet0/1/3).

\*Sep 17 10:11:03:299 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received topology message, state(End), new digest(000000365981264d9ff), edge count(2).

\*Sep 17 10:16:54:461 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received I-SID B-VLAN item message, system ID(0011.2200.0a01), Operation(Refresh), I-SID (256), B-VLAN(1).

\*Sep 17 10:18:05:372 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received I-SID B-VLAN mapping message, I-SID(256), TRB-VLAN(1), RB-VLAN(65535).

\*Sep 17 10:18:08:625 2012 Sysname SPBM/7/SPBM_1_EVT: -MDC=1;

FLUSH: Received I-SID message, system ID(0011.2200.0001), I-SID(256), ECT(1), Port(GigabitEthernet0/1/3).

\*Sep 17 10:15:58:873 2012 Sysname SPBM/7/SPBM_EVT: -MDC=1;

FLUSH: Received configuration message.

\# 使能SPBM功能，打开单播组播SPBM FLUSH消息调试信息开关，当用户态进程向内核发送MAC消息时会输出下列调试信息。

\<Sysname\> debugging spbm flush message unicast-fib

\*Sep 17 10:11:03:329 2012 Sysname SPBM/7/SPBM_1_MSG: -MDC=1;

FLUSH: Sent the message for refreshing unicast MAC entry, length= 32.

Unicast MAC: MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T).

\<Sysname\> debugging spbm flush message multicast-fib

\*Sep 17 10:18:08:626 2012 Sysname SPBM/7/SPBM_1_MSG: -MDC=1;

FLUSH: Sent the message for adding multicast MAC iflist, length= 40.

Multicast MAC: MAC(1363-5700-0100) B-VLAN(1) Port(GE0/1/3) RouteFlag(TE).

\<Sysname\> debugging spbm flush message unicast-pw

\*Sep 17 10:18:05:372 2012 Sysname SPBM/7/SPBM_1_MSG: -MDC=1;

FLUSH: Sent the message for adding unicast MINM entry, I-SID(256), B-VLAN(1), Port(GE0/1/3)

[ VSI-name(1), Flag(MINM_SPB \| MINM_UNICAST \| MINM_COREREPLICATE), D-BMAC(0011-2200-0a01), S-BMAC(0011-2200-0001), S-CMAC(0011-2200-0001).]

**SPBM \-- SPBM调试命令 \-- debugging spbm graceful-restart**

------------------------------------------------------------------------

【命令】

**[debuging spbm graceful-restart**]

**[undo debuging spbm graceful-restart**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging spbm graceful-restart**]命令用来打开SPBM GR调试信息开关。**undo debugging spbm graceful-restart**命令用来关闭SPBM GR调试信息开关。

缺省情况下，SPBM GR调试信息开关处于关闭状态。

表1-13 debugging spbm graceful-restart命令输出信息描述表

字段

描述

ADJ: All T1 timers have stopped.

所有的T1定时器已停止

ADJ: All Level-1 T1 timers have stopped.

所有Level-1的T1定时器已停止

ADJ: Adjacency(*system-id*) on *circuitName* (Level-1) changed to normal mode.

邻居的GR状态发生变化，由GR状态变为非GR状态，其中：

·*system-id*：邻居的系统ID

·*circuitName*：端口名称

ADJ: Adjacency(*system-id*) on *circuitName* (Level-1) changed to restart mode.

邻居的GR状态发生变化，由非GR状态变为GR状态，其中：

·*system-id*：邻居的系统ID

·*circuitName*：端口名称

ADJ: Neighbor(*system-id*) SA bit set, adjacency not advertised.

邻居报文GRTLV中的SA比特位被设置上，其中*system-id*表示邻居的系统ID

ADJ: Neighbor(*system-id*) SA bit cleared, adjacency advertised.

邻居报文GRTLV中的SA比特位被清除，其中*system-id*表示邻居的系统ID

ADJ: Received P2P Hello with RR bit set from neighbor *system-id* on *circuitName*.

从邻居接收到RR比特位被置位的P2P Hello报文，其中：

·*system-id*：邻居的系统ID

·*circuitName*：端口名称

ADJ: Received P2P Hello with RA bit set from neighbor *system-id* on *circuitName*.

从邻居接收到RA比特位被置位的P2P Hello报文，其中：

·*system-id*：邻居的系统ID

·*circuitName*：端口名称

ADJ: Circuit(*circuitName*) Level-1 T1 timer expired count: *T1TimerExpCnt*.

端口的Level-1 T1定时器超时次数，其中：

·*circuitName*：端口名称

·*T1TimerExpCnt*：T1定时器超时的次数，超时10次之后取消T1定时器

ADJ: Circuit(*circuitName*) Level-1 timer expired count has arrived max.

T1定时器超时次数达到最大次数10次，其中*circuitName*表示端口名称

MAIN: Graceful restart completed.

GR完成

MAIN: Entered phase(*GrPhase*).

GR进入下一阶段，其中GrPhase表示GR阶段，包括LSDB同步阶段、第一次SPF计算阶段、引入计算阶段、第二次SPF计算阶段、LSP生成阶段、GR完成阶段

MAIN: Received Level-1 T2 timer cancel event(*T2StopEvent*).

收到触发T2停止的事件，事件类型包括"所有T1定时器停止"和"LSDB同步完成"。两个事件都发生时才真正停止T2定时器，其中*T2StopEvent*表示触发停止T2定时器的事件，包括"所有T1定时器停止"和"LSDB同步完成"

MAIN: Level-1 T2 timer stopped.

停止Level-1 T2定时器

MAIN: Level-1 T2 timer expired.

Level-1 T2定时器超时

MAIN: Graceful restart entered *GrTypeStr* phase(*LSDB synchronization*).

开始GR，GR方式*GrTypeStr*分为restarting方式和starting方式

MAIN: Received module(*module*) phase(*GrPhase*), current phase(*GrPhase*).

模块GR阶段结束信息，其中：

·*module*：模块名

·*GrPhase*：GR阶段

MAIN: Entered GR smooth process: sysIndex= *sysindex.*

进程进入GR平滑处理，其中*sysindex*表示系统索引

MAIN: Exited GR smooth process: sysIndex= *sysindex.*

进程离开GR平滑处理，其中*sysindex*表示系统索引

MAIN: Notified FLUSH to leave GR smooth process.

所有进程GR平滑都结束后，MAIN通知FLUSH平滑结束消息，开始下发表项

UPDT: Started to purge local Level-1 LSP.

GR完成，开始将本地原来生成、现在失效的LSP清除

UPDT: Purged Level-1 LSP *Lsp-id.*

GR完成，将本地原来生成、现在失效的LSP清除，其中*Lsp-id*为LSP-ID

UPDT: Ended to purge local Level-1 LSP.

清除失效LSP结束

UPDT: Synchronized CSNP from *Source-id* on circuit *circuitName*. LSP-ID ranges from *StartLspid* to *EndLspid.*

GR过程中收到Helper端发送的CSNP，其中：

·*Source-id*：Helper的系统ID

·*circuitName*：端口名

·*StartLspId*：CSNP报文中开始的LSP-ID

·*EndLspId*：CSNP报文中结束的LSP-ID

UPDT: Level-1 LSDB synchronization was complete.

GR过程中LSDB同步完成

UPDT: Level-1 CSNP set synchronization was complete on circuit *circuitName.*

GR过程中CSNP接收完全，其中*circuitName*表示端口名

【举例】

\# 打开SPBM GR调试信息开关。

\<Sysname\> debugging spbm graceful-restart

\# 执行SPBM GR操作，输出下列调试信息。

\<Sysname\> reset spbm all graceful-restart

Reset SPBM process? [Y/N:y]

\<Sysname\> \*Sep 10 00:24:19:183 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Graceful-restart enter restarting phase(Initialization).

\*Sep 10 00:24:19:201 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

ADJ: Interface(GigabitEthernet1/0/2) Level-1 T1 timer expired count: 1.

%Sep 10 00:24:19:208 2012 Sysname SPBM/5/SPB_NBR_CHG: -MDC=1; SPBM 1, Level-1 adjacency 0011.2200.1401 (GigabitEthernet1/0/2), state change to: UP.

\*Sep 10 00:24:19:209 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

ADJ: All T1 timers have stopped.

\*Sep 10 00:24:19:209 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

ADJ: Received p2p hello with RA bit set from nbr 0011.2200.1401, on GigabitEthernet1/0/2.

\*Sep 10 00:24:19:209 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

UPDT: Synchronized CSNP from 0011.2200.1401 on circuit GigabitEthernet1/0/2 range from 0000.0000.0000.00-00 to ffff.ffff.ffff.ff-ff

\*Sep 10 00:24:19:209 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

UPDT: Level-1 CSNP set synchronization is complete on circuit GigabitEthernet1/0/2

\*Sep 10 00:24:19:210 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

ADJ: All T1 timers have stopped.

\*Sep 10 00:24:19:211 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Received Level-1 T2 timer cancel event(All T1 stopped).

\*Sep 10 00:24:19:211 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Received Level-1 T2 timer cancel event(All T1 stopped).

\*Sep 10 00:24:19:267 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

UPDT: LSDB synchronization is complete

\*Sep 10 00:24:19:267 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Received Level-1 T2 timer cancel event(LSDB sync).

\*Sep 10 00:24:19:267 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Level-1 T2 timer stopped

\*Sep 10 00:24:19:267 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Entered phase(LSP stability)

\*Sep 10 00:24:19:269 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Received module(updt) phase(LSP stability), current phase(LSP stability).

MAIN: Entered phase(LSP generation)

\*Sep 10 00:24:19:272 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

UPDT: Started to purge local Level-1 LSP.

\*Sep 10 00:24:19:272 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

UPDT: Ended to purge local Level-1 LSP.

\*Sep 10 00:24:19:272 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Received module(updt) phase(LSP generation), current phase(LSP generation).

\*Sep 10 00:24:19:272 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Entered phase(First SPF computation)

\*Sep 10 00:24:20:902 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Received module(dec) phase(First SPF computation), current phase(First SPF computation).

\*Sep 10 00:24:20:902 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Entered phase(Finish)

\*Sep 10 00:24:20:902 2012 Sysname SPBM/7/SPBM_1_GR: -MDC=1;

MAIN: Graceful restart completed.

**SPBM \-- SPBM调试命令 \-- debugging spbm ha-event**

------------------------------------------------------------------------

【命令】

**[debuging spbm ha-event**]

**[undo debuging spbm ha-event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging spbm** **ha-event**]命令用来打开SPBM HA调试信息开关。**undo debugging spbm** **ha-event**命令用来关闭SPBM HA调试信息开关。

缺省情况下，SPBM HA调试信息开关处于关闭状态。

表1-14 debugging spbm ha-event命令输出信息描述表

字段

描述

Failed to send real-time SPBM backup data.

发送SPBM实时备份数据失败

Successful data batch backup for interface *interface-name*.

接口信息批量备份成功，其中*interface-name*表示接口名

Sequence number rollover timer backed up successfully.

成功备份序列号翻转定时器

SPBM process stopped because an HA stop event was received.

接收到HA停止事件，停止进程工作

Notified the ADJ, UPDT, DEC, and FLUSH threads to stop.

通知线程（ADJ/UPDT/DEC/FLUSH）停止工作

Threads exited incorrectly before SPBM stopped.

SPBM停止工作前，线程异常退出，这里的线程指ADJ/UPDT/DEC/FLUSH四个线程或其中若干

Active SPBM process changed to standby state, and all its SPBM data was deleted.

降级（主进程变为备进程），删除进程所有相关数据

Received HA upgrade event.

收到HA升级事件

Failed to send cached data.

发送缓存数据失败，这里的数据指系统反压机制当中用于暂存数据的反压数据链上的数据

Finished sending batch backup data in the cache.

缓存数据当中的批量备份相关数据已发送完毕

Batch backup event finished.

批量备份事件结束

Upgrade event finished.

升级事件结束

Stop event finished.

停止事件结束

Degrade event finished.

降级事件结束

Notified other threads to start batch backup. Thread ID: *thread id*.

通知其他线程进入批量备份流程，其中*thread id*表示线程编号，1为ADJ线程，2为UPDT线程，3为DEC线程，4为FLUSH线程

Batch backup of SPBM data started.

开始批量备份SPBM数据

Connected to L2VPN successfully.

与二层VPN连接成功

Failed to connect to L2VPN.

与二层VPN连接失败

Backup SPBM data, type: *type*

备份SPBM所有数据，*type*字段为数据类型，*type*取值为：

·process config(basic&ECT-BVLAN)（包括进程基本配置数据及ECT算法与BVLAN的映射关系数据）：进程全局配置

·interface config：接口配置

·hostname：动态主机名

·MSTP

·interface basic：接口激活、updown状态及接口类型

·sequence number rollover timer：序列号翻转定时器

·SPSourceID

·overload：过载机制，启动此项机能时，表示设备此时不具备处理流量数据的能力

Received Main event, type: type

收到main主线程事件，其中*type*表示事件类型，*type*取值为：

·delete interface：接口删除事件

·thread *threadname*reset process：进程重置事件，*threadname*取值为：MAIN/ADJ/UPDT/DEC/FLUSH

·thread *threadname*stop event：线程停止事件，*threadname*取值为：ADJ/UPDT/DEC/FLUSH

·thread *threadname* cancel T2 timer for GR：取消GR的T2定时器事件，*threadname*取值为：ADJ/UPDT

·the GR *phasename*phase completed：GR阶段结束事件，*phasename*取值为：LSP stability/LSP generation/SPF computation/Flush smooth

·start overload T2 for neighbour：开启overload的T2定时器事件

·GR smooth completed：GR平滑完成事件

·started flush smooth：内核数据平滑开始事件

·thread *threadname* NSR smooth completed：NSR平滑完成事件，*threadname*取值为：ADJ/UPDT

·the NSR *phasename* phase completed：NSR阶段结束事件，*phasename*取值为：LSP stability/LSP generation/SPF computation/Flush smooth

·continue to send cache data：继续发送缓存数据事件

·thread *threadname* NSR batch backup completed：NSR批量备份完成事件，*threadname*取值为：MAIN/ADJ/UPDT

·thread *threadname* GR batch backup completed：GR批量备份完成事件，*threadname*取值为：MAIN/ADJ/UPDT

·hostname backup：动态主机名备份事件

Backup data.

Data type: *Data type,* subtype: *subtype*

备份数据，*Data type*表示数据类型，*subtype*表示数据的具体子类型。

*[Data type*]取值为：

·SPBM config data：全局配置数据，其中所包含的子类型字段有以下：

SPBM status/bridge priority/ADJ log peer/LSP refresh timer/LSP max-age timer/flash flood/hostname/SPSource/SPBM agreement mode/overload/GR status/restart interval/suppress-sa/SPF calculating time interval/SPF generating time interval/bandwidth-reference/circuit cost/MAC address for SPBM multicast message/multicast BVLAN/(area-authentication-mode)/(area-authentication sendonly)/SNMP-agent trap/NSR status/reset standby/debug switch

·SPBM running data：全局运行数据，其中所包含的子类型字段为*hostname*

·interface config：接口配置数据，其中所包含的子类型字段有以下：

enable SPBM under the interface/SPBM cost on the basis of interface/hello timer/holding multiplier timer/LSP sending interval/(interface-authentication-mode)/(interface-authentication sendonly)

·interface basic running data：接口运行数据，其中包含的备份子类型字段有如下：

if SPBM enable, create circ info/delete the interface/interface active status/interface LAGG type/interface basic running data, circuit ID: *circuit ID*，*circuit ID*为端口ID（批量备份时subtype字段为interface basic running data）

·VSI config：VSI配置，其中所包含的子类型字段：ISID/multicast dup-mod

·VSI running data：VSI运行数据，其中所包含的子类型字段：added VSI data, VSI index: *vsi index*/deleted VSI data, VSI Index: *vsi index*/updated VSI data, VSI Index: *vsi index*，*vsi index*为VSI索引（批量备份时*subtype*字段为added VSI data）

·ECT-BVLAN：ECT与BVLAN的映射关系数据，其中子类型表示ECT算法编号

·overload：overload相关数据，子类型字段为overload

【举例】

\# 打开SPBM HA报文调试信息开关。启动一个备用主控板，触发数据批量备份。输出下列调试信息。

\<Sysname\> debugging spbm ha-event

\*Nov 30 22:00:00:166 2013 Sysname DEV/2/BOARD_STATE_FAULT: -MDC=1; Board state changes to FAULT on Slot 1, type is unknown.

\*Nov 30 22:00:02:105 2013 Sysname DEV/5/BOARD_STATE_NORMAL: -MDC=1; Board state changes to NORMAL on Slot 1, type is Simware.

\*Nov 30 22:00:02:205 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Batch backup of SPBM data started.

*// 开始批量备份SPBM数据*

\*Nov 30 22:00:02:206 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup SPBM data, type: MSTP.

\*Nov 30 22:00:02:206 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: VSI running data, subtype: added VSI data.

*// 备份SPBM全局运行数据*

\*Nov 30 22:00:02:210 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: SPBM config data, subtype: SPBM status.

\*Nov 30 22:00:02:210 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: SPBM config data, subtype: ADJ log peer.

\*Nov 30 22:00:02:210 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: SPBM config data, subtype: LSP refresh timer.

\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: SPBM config data, subtype: LSP max-age timer.

\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: SPBM config data, subtype: flash flood.

\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: SPBM config data, subtype: overload.

\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: SPBM config data, subtype: GR status.

\*Nov 30 22:00:02:211 2013 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Backup data. Data type: SPBM config data, subtype: restart interval.

*// 备份SPBM全局配置数据*

【举例】

\# 打开SPBM HA报文调试信息开关。

\<Sysname\> debugging spbm ha-event

\*Dec 12 20:56:47:926 2012 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Recieved HA stop event,stopped SPBM data.

\*Dec 12 20:56:47:943 2012 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Notifying thread to stop work.

\*Dec 12 20:56:47:954 2012 Sysname SPBM/7/SPBM_HA: -MDC=1;

MAIN: Degrade(master to slave), deleted SPBM data.

**SPBM \-- SPBM调试命令 \-- debugging spbm self-originate-update**

------------------------------------------------------------------------

【命令】

**[debugging spbm self-originate-update**]

**[undo debugging spbm self-originate-update**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging spbm self-originate-update**]命令用来打开SPBM本地更新的调试信息开关。**undo debugging spbm self-originate-update**命令用来关闭SPBM本地更新的调试信息开关。

缺省情况下，SPBM本地更新的调试信息开关处于关闭状态。

表1-15 debugging spbm self-originate-update命令输出信息描述表

字段

描述

UPDT: Started to rebuild all LSPs.

开始rebuild所有的LSP

UPDT: Stopped to rebuild all LSPs.

结束rebuild所有的LSP

UPDT: MTU change triggers rebuild.

MTU变化触发rebuild

UPDT: LSP lifetime change triggers rebuild.

LSP生存周期变化触发rebuild

UPDT: Attempting to exceed max sequence number.

生成LSP时，序列号达到最大

UPDT: Generating LSP= *lsp-id*, sequence number*= sequence-number*, length= *lsp-length*.

生成LSP结束，其中：

·*lsp-id*：生成LSP的ID

·*sequence-number*：生成LSP的序列号

·*lsp-length*：生成LSP的长度

UPDT: TLV change triggers rebuild.

TLV变化触发rebuild

UPDT: Purging LSP= *lsp-id*.

清除LSP报文，其中*lsp-id*表示被清除LSP报文的ID

UPDT: Added area address *address.*

添加区域地址TLV，其中*address*表示区域地址

UPDT: Added protocol support *protocol.*

添加协议支持TLV，其中*protocol*表示协议

UPDT: Added host name *name.*

添加host name TLV，其中*name*表示主机名

UPDT: Deleted host name *name.*

删除host name TLV，其中*name*表示主机名

UPDT: Added Instance sub-TLV: B-VLAN= *bvlan-number*, u-bit= *u-bit*, ECT-Algorithm= *ect-algorithm.*

添加Instance TLV，其中：

·*bvlan-number*：B-VLAN值

·*ubit*：u比特位

·*ect-algorithm*：ECT算法

UPDT: Modified Instance sub-TLV: B-VLAN= *bvlan-number*, u-bit= *u-bit*, ECT-Algorithm= *ect-algorithm.*

修改Instance sub-TLV，其中：

·*bvlan-number*：B-VLAN值

·*ubit*：u比特位

·*ect-algorithm*：ECT算法

UPDT: Deleted Instance sub-TLV: B-VLAN= *bvlan-number.*

删除Instance sub-TLV，其中*bvlan-number*表示B-VLAN值

UPDT: Added I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid*, T-flag= *t-flag*, R-flag= *r-flag.*

添加I-SID sub-TLV，其中：

·*bvlan-number*：B-VLAN值

·*i-sid*：I-SID值

·*t-flag*：T标志位

·*r-flag*：R标志位

UPDT: Modified I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid*, T-flag= *t-flag*, R-flag= *r-flag.*

修改I-SID sub-TLV，其中：

·*bvlan-number*：B-VLAN值

·*i-sid*：I-SID值

·*t-flag*：T标志位

·*r-flag*：R标志位

UPDT: Deleted I-SID sub-TLV: B-VLAN= *bvlan-number*, I-SID= *i-sid.*

删除I-SID sub-TLV，其中：

·*bvlan-number*：B-VLAN值

·*i-sid*：I-SID值

UPDT: Added neighbor TLV: neighbor system ID=  *system-id*, cost=  *cost.*

添加邻居TLV，其中：

·*system-id*：邻居系统ID

·*cost*：cost值

UPDT: Modified neighbor TLV: neighbor system ID= *system-id*, cost= *cost.*

修改邻居TLV，其中：

·*system-id*：邻居系统ID

·*cost*：cost值

UPDT: Deleted neighbor TLV: neighbor system ID=  *system-id.*

删除邻居TLV，其中*system-id*表示邻居系统ID

【举例】

\# 打开SPBM错误信息调试信息开关。

\<Sysname\> debugging spbm self-originate-update

\# 端口下使能SPBM功能，输出下列调试信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 0/1/3

Sysname-GigabitEthernet0/1/3 spbm enable

\*Sep 18 13:36:04:360 2012 Sysname SPBM/7/SPBM_1_ORG: -MDC=1;

UPDT: Added neighbor TLV: neighbor system ID= 0011.2200.1401, cost= 16777215.

Sysname-GigabitEthernet0/1/3 \*Sep 18 13:36:06:367 2012 Sysname SPBM/7/SPBM_1_ORG: -MDC=1;

UPDT: Generating LSP= 0011.2200.0001.00-01, sequence number= 0x0000000b, length= 76.

**SPBM \-- SPBM调试命令 \-- debugging spbm snp-packet**

------------------------------------------------------------------------

【命令】

**[debugging spbm snp-packet **[[ **receive** \| **send** ]  **verbose** ]]

**[undo debugging spbm snp-packet **[[ **receive** \| **send** ]  **verbose** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：表示接收SNP报文调试信息开关。

**[send**]：表示发送SNP报文调试信息开关。

**[verbose**]：表示SNP报文详细调试信息开关。

【描述】

**[debugging spbm snp-packet**]命令用来打开SPBM SNP报文的调试信息开关。**undo debugging spbm snp-packet**命令用来关闭SPBM SNP报文的调试信息开关。

缺省情况下，SPBM SNP报文的调试信息开关处于关闭状态。

表1-16 debugging spbm snp-packet命令输出信息描述表

字段

描述

UPDT: Received *psnp-type* from *system-id* on circuit *circuitName*.

收到PSNP报文，其中：

·*psnp-type*：PSNP报文类型，取值为L1 PSNP或L2 PSNP

·*system-id*：发送PSNP报文SPBM进程的系统ID

·*circuitName*：端口名称

UPDT: Received *csnp-type* from *source-id* on circuit *circuitName*. LSP-ID ranges from *start-lsp-id* to *end-lsp-id.*

收到CSNP报文，其中：

·*csnp-type*：CSNP报文类型，取值为L1 CSNP或L2 CSNP

·*source-id*：发送CSNP报文SPBM进程的SOURCE ID

·*circuitName*：端口名称

·*start-lsp-id*：LSP摘要的起始LSP-ID

·*end-lsp-id*：LSP摘要的结束LSP-ID

UPDT: Sent *snp-type* on circuit *circuitName.*

发送CSNP/PSNP报文，其中：

·*snp-type*：SNP报文类型，取值为L1 CSNP、L2 CSNP、L1 PSNP或L2 PSNP

·*circuitName*：端口名称

UPDT: No current LSP entry is found to build CSNP.

发送CSNP报文时，在LSDB中没有找到起始LSP-ID或第一个比起始LSP-ID大的LSP

UPDT: LSP entry *lsp-id* processed is newer than LSDB copy.

收到LSP摘要比LSDB中的新，其中*lsp-id*表示收到的LSP摘要ID

UPDT: LSP entry *lsp-id* processed is older than LSDB copy.

收到LSP摘要比LSDB中的旧，其中*lsp-id*表示收到的LSP摘要ID

UPDT: LSP entry *lsp-id* processed is the same as LSDB copy.

收到LSP摘要和LSDB中的新旧程度一样，其中*lsp-id*表示收到的LSP摘要ID

UPDT: LSP entry *lsp-id* processed does not exist in LSDB.

收到LSP摘要在LSDB中不存在，其中*lsp-id*表示收到的LSP摘要ID

UPDT: LSP entry *lsp-id* processed has not been loaded in CSNP.

收到LSP摘要在CSNP中没有安装，其中*lsp-id*表示收到的LSP摘要ID

UPDT: Received *pdutype* could not pass authentication, system ID= *system-id*, SNP has been ignored.

无法通过认证，SNP报文被丢弃，其中：

·*pdutype*：报文类型

·*system-id*：发送SNP报文SPBM进程的系统ID

【举例】

\# 打开SPBM Hello报文调试信息开关。

\<Sysname\> debugging spbm snp-packet

\# 端口下使能SPBM功能，输出下列调试信息。

\<Sysname\> sysem-view

Sysname interface gigabitethernet 0/1/3

Sysname-GigabitEthernet0/1/3 spbm enable

\*Sep 18 14:54:58:058 2012 Sysname SPBM/7/SPBM_1_SNP: -MDC=1;

UPDT: Received L1 CSNP from 0011.2200.0a01 on circuit GigabitEthernet0/1/3. LSP-ID ranges from 0000.0000.0000.00-00 to ffff.ffff.ffff.ff-ff.

\*Sep 18 14:54:58:059 2012 Sysname SPBM/7/SPBM_1_SNP: -MDC=1;

UPDT: Sent L1 CSNP on circuit GigabitEthernet0/1/3.

\*Sep 18 14:54:59:918 2012 Sysname SPBM/7/SPBM_1_SNP: -MDC=1;

UPDT: Received L1 PSNP from 0011.2200.0a01 on circuit GigabitEthernet0/1/3.

\*Sep 18 14:54:59:987 2012 Sysname SPBM/7/SPBM_1_SNP: -MDC=1;

UPDT: Sent L1 PSNP on circuit GigabitEthernet0/1/3.

**SPBM \-- SPBM调试命令 \-- debugging spbm spf**

------------------------------------------------------------------------

【命令】

**[debugging**]**spbm****spf **\**[verbose**]

**[undo**]**debugging****spbm****spf** \**[verbose**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[verbose**]：表示SPBM路由计算详细调试信息开关。

【描述】

**[debugging spbm spf**]命令用来打开SPBM路由计算调试信息开关。**undo debugging spbm spf**命令用来关闭SPBM路由计算调试信息开关。

缺省情况下，SPBM路由计算调试信息开关处于关闭状态。

表1-17 debugging spbm spf命令输出信息描述表

字段

描述

 

DEC: (MT*topology-id*) Calculating topology digest at Sec= *xxx*, MSec= *yyy*.

开始摘要计算，其中：

·*topology-id*：拓扑ID

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: Before calculating digest, the edge count is *count*.

计算摘要之前边得数目，其中*count*表示边的数目

 

DEC: Calculating digest: delete the link eigenvalue from digest, link Src= *source-id*, link Dst= *dest-id*.

从摘要中删除LINK的特征值，其中：

·*source-id*：源系统ID

·*dest-id*：目的系统ID

 

DEC: Calculating digest: add the link eigenvalue to digest, link Src= *source-id*, link Dst= *dest-id*.

添加LINK的特征值到摘要中，其中：

·*source-id*：源系统ID

·*dest-id*：目的系统ID

 

DEC: Calculating digest: update the link eigenvalue from digest, link Src= *source-id*, link Dst= *dest-id*.

更新摘要LINK的特征值，其中：

·*source-id*：源系统ID

·*dest-id*：目的系统ID

 

DEC: After calculating digest, the edge count is *count*.

拓扑摘要计算完成之后边的数目*count*

 

DEC: Deleted the link from eigenvalue change list, link Src= *source-id*, link Dst= *dest-id*.

将LINK从LINK特征值变化链中删除，其中：

·*source-id*：源系统ID

·*dest-id*：目的系统ID

 

DEC: Added the link to eigenvalue change list, link Src= *source-id*, link Dst= *dest-id.*

将LINK添加到LINK特征值变化链中，其中：

·*source-id*：源系统ID

·*dest-id*：目的系统ID

 

DEC: (MT*topology-id*) Invalid node (*system-id*) calculation. Then, FLUSH deleted all FDB entries. Run started at Sec= *xxx*, MSec= *yyy*.

计算节点无效，通知FLUSH删除所有的FDB表项，其中：

·*topology-id*：拓扑ID

·*system-id*：计算节点的系统ID

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) Local node started topology calculation at Sec= *xxx*, MSec= *yyy.*

当前节点开始进行拓扑计算，其中：

·*topology-id*：拓扑ID

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) Node(*system-id*) invalid and notified FLUSH to delete all multicast FDB entries at Sec= *xxx,* MSec= *yyy.*

组播源节点无效，通知FLUSH删除所有的组播FDB表项，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源节点的系统ID

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) Node(*system-id*) multicast FDB is calculating at Sec= *xxx*, MSec= *yyy.*

组播源节点进行组播计算，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源节点的系统ID

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) All phases of SPF work completed at Sec= *xxx,* MSec= *yyy.*

所有SPF计算完成，其中：

·*topology-id*：拓扑ID

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) Node(*system-id*) used ECT *ect-index*, worked out the circuit index at *circuit index.* Run started at Sec= *xxx*, MSec= *yyy*.

使用指定ECT算法计算出根节点到指定节点的出端口索引，其中：

·*topology-id*：拓扑ID

·*system-id*：指定节点系统ID

·*ect-index*：ECT算法索引

·*circuit index*：端口索引

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) Node(*system-id*) used ECT *ect-index* to calculate. Run started at Sec= *xxx*, MSec= *yyy.*

指定节点使用指定ECT算法进行选路计算，其中：

·*topology-id*：拓扑ID

·*system-id*：节点系统ID

·*ect-index*：ECT算法索引

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) There is no VLAN using the ECT *ect-index*. Notified FLUSH to delete the unicast FDB. Run started at Sec= *xxx*, MSec= *yyy*.

当期没有B-VLAN配置使用指定的ECT算法，通知FLUSH删除所有的单播表项，其中：

·*topology-id*：拓扑ID

·*ect-index*：ECT算法索引

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) DEC received B-VLAN ECT mapping changed message: operator type= *operatorId*, ECT-Index= *ect-index* ,B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.

DEC收到B-VLAN-ECT变化的消息，其中：

·*topology-id*：拓扑ID

·*operatorId*：添加，修改，删除操作标记

·*ect-index*：ECT算法索引

·*bvlan-number*：B-VLAN值

·*xxx*：秒值

·*yyy*：毫秒值

 

DEC: (MT*topology-id*) I-SID calculating: found a node in the I-SID hash: B-VLAN= *bvlan-number* I-SID= *i-sid*. Run started at Sec= *xxx*, MSec= *yyy*.

I-SID计算在全网I-SID哈希中查找定的I-SID和B-VLAN，其中：

·*topology-id*：拓扑ID

·*bvlan-number*：B-VLAN的值

·*i-sid*：I-SID值

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Added a new multicast source(*system-id*). Run started at Sec= *xxx*, MSec= *yyy*.

新增组播源，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) added a new T-flag: I-SID= *i-sid,* B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.

组播源节点新增一个置位T Flag的I-SID，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*bvlan-number*：B-VLAN的值

·*i-sid*：I-SID值

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) added a new T-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*, count= *count*. Run started at Sec= xxx, MSec= yyy.

显示组播源节点T Flag置位的I-SID个数，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN的值

·*count*：T Flag置位的I-SID的个数

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) changed to non-multicast source. Run started at Sec= *xxx*, MSec= *yyy*.

节点有组播源变成非组播源，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) deleted a T-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.

组播源节点删除一个置位T Flag的I-SID，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN的值

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) added a R-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.

组播源节点添加一个置位R Flag的I-SID，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN的值

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) deleted a R-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx*, MSec= *yyy*.

组播源节点删除一个置位R Flag的I-SID，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN的值

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) I-SID incremental calculation started at Sec= *xxx*, MSec= *yyy*.

组播增量计算开始，其中：

·*topology-id*：拓扑ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) was calculating multicast FDB. Run started at Sec= *xxx*, MSec= *yyy*.

指定节点开始计算组播FDB，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) UPDT notified node(*system-id*) to add the I-SID change list: I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *T-flag*, R-flag= *R-flag*. Run started at Sec*= xxx,* MSec*= yyy.*

UPDT通知组播源节点增加I-SID,挂载到I-SID变化链，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN的值

·*T-**flag*：I-SID携带的T标记

·*R-**flag*：I-SID携带的R标记

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) UPDT notified node(*system-id*) to modify the T-flag and the R-flag: I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *T-flag*, R-flag= *R-flag*. Run started at Sec*= xxx,* MSec*= yyy.*

UPDT通知组播源节点修改指定I-SID，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN的值

·*T-**flag*：I-SID携带的T标记

·*R-**flag*：I-SID携带的R标记

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) On the node(*system-id*) was deleted from the I-SID change list: I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *T-flag*, R-flag= *R-flag*. Run started at Sec *= xxx,* MSec *= yyy.*

在组播源节点上从I-SID 变化链上删除I-SID，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN的值

·*T-**flag*：I-SID携带的T标记

·*R-**flag*：I-SID携带的R标记

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) DEC added the count(*count*) of I-SID T-flag. The new multicast flag is *flag*. Run started at Sec*= xxx,* MSec*= yyy.*

组播源节点新增一个置位T-flag的I-SID，其中：

·*topology-id*：拓扑ID

·*count*：T-flag置位的I-SID的个数

·*flag*：新增组播源标记

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) UPDT notified node(*system-id*) to add same I-SID and B-VLAN. Run started at Sec*= xxx,* MSec*= yyy.*

组播源节点新增一个相同I-SID，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) modified to add the count(*count*) of I-SID T-flag. The new multicast flag is *Flag*. Run started at Sec*= xxx,* MSec*= yyy.*

组播源修改I-SID，T Flag置位，计数增加，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*count*：T Flag置位的I-SID的个数

·*Flag*：新增组播源标记

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) modified to delete the count(*count*) of I-SID T-flag. Run started at Sec*= xxx,* MSec*= yyy.*

组播源修改I-SID，T Flag清零，计数减少，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*count*：T Flag置位的I-SID的个数

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) deleted I-SID T-flag count(*count*) .

组播源删除I-SID，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*count*：T Flag置位的I-SID的个数

 

DEC: Deleted the node from I-SID hash: B-VLAN= *bvlan-number*, I-SID= *i-sid*. Run at Sec*= xxx,* MSec*= yyy.*

在I-SID哈希中删除指定的I-SID和B-VLAN，其中：

·*bvlan-number*：B-VLAN的值

·*i-**sid*：I-SID值

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) added I-SID and B-VLAN to I-SID hash. Run started at Sec*= xxx,* MSec*= yyy.*

I-SID哈希中添加相同的I-SID和B-VLAN，其中：

·*topology-id*：拓扑ID

·*system-id*：组播源的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) received I-SID change message: operator type= *operator type*, I-SID= *i-sid*, B-VLAN= *bvlan-number*, T-flag= *T-flag*, R-flag= *R-flag*. Run started at Sec*= xxx,* MSec*= yyy.*

DEC收到I-SID变化的消息，显示消息内容，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*operator type*：操作类型

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN的值

·*T-**flag*：I-SID携带的T标记

·*R-**flag*：I-SID携带的R标记

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) *Operation* link *linksrc*{.TableTextChar} \--\> *linkdst*, with attribute *Link-flag*1*,*{.TableTextChar} *Link-flag*2{.TableTextChar}.

DEC处理LINK变化链时的LINK相关的调试信息，其中：

·*topology-id*：拓扑ID

·*[Operation*]{.TableTextChar}：LINK的变化情况，有有Increased、Decreased和Destroyed。

·*[linksrc*]{.TableTextChar}：LINK的源节点

·*[linkdst*]{.TableTextChar}：LINK的目的节点

另外*Link-flag*可能有多个，含义分别是：

·Tree：在SPF树上

·Back：回指链路

·Increase：cost变大

·Decrease：cost变小

·Delete：待删除

·Involve：受影响

·NewPath：新增路径

 

DEC: (MT*topology-id*) SRC node found,{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, with attribute {.TableTextChar}*Node-flag*1, {.TableTextChar}*Node-flag*2{.TableTextChar}.

找到源节点，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*nbrcount*：邻居个数

·*parentcount*：父节点个数

另外*Node-flag*可能有多个，含义分别是：

·RmtNbr：忽略2-way检查邻居

·Tree：在树上

·Tent：在备选链表上

·Direct：与根节点直连

·Overload：Overload标志

·Delete：待删除

 

DEC: (MT*topology-id*) DST node found,{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, with attribute {.TableTextChar}*Node-flag*1, {.TableTextChar}*Node-flag*2{.TableTextChar}.

找到目的节点，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*nbrcount*：邻居个数

·*parentcount*：父节点个数

另外*Node-flag*可能有多个，含义分别是：

·RmtNbr：忽略2-way检查邻居

·Tree：在树上

·Tent：在备选链表上

·Direct：与根节点直连

·Overload：Overload标志

·Delete：待删除

 

DEC: (MT*topology-id*) Destroyed node,{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, with attribute {.TableTextChar}*Node-flag*1, {.TableTextChar}*Node-flag*2{.TableTextChar}.

销毁节点，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*nbrcount*：邻居个数

·*parentcount*：父节点个数

另外*Node-flag*可能有多个，含义分别是：

·RmtNbr：忽略2-way检查邻居

·Tree：在树上

·Tent：在备选链表上

·Direct：与根节点直连

·Overload：Overload标志

·Delete：待删除

 

DEC: (MT*topology-id*) Changed node o{.TableTextChar}verload flag,{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, with attribute {.TableTextChar}*Node-flag*1, {.TableTextChar}*Node-flag*2{.TableTextChar}.

改变overload标志，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*nbrcount*：邻居个数

·*parentcount*：父节点个数

另外*Node-flag*可能有多个，含义分别是：

·RmtNbr：忽略2-way检查邻居

·Tree：在树上

·Tent：在备选链表上

·Direct：与根节点直连

·Overload：Overload标志

·Delete：待删除

 

DEC: (MT*topology-id*) Created(new) node,{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, with attribute {.TableTextChar}*Node-flag*1, {.TableTextChar}*Node-flag*2{.TableTextChar}.

创建新节点，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*nbrcount*：邻居个数

·*parentcount*：父节点个数

另外*Node-flag*可能有多个，含义分别是：

·RmtNbr：忽略2-way检查邻居

·Tree：在树上

·Tent：在备选链表上

·Direct：与根节点直连

·Overload：Overload标志

·Delete：待删除

 

DEC: (MT*topology-id*) Created(exist) node,{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, with attribute {.TableTextChar}*Node-flag*1, {.TableTextChar}*Node-flag*2{.TableTextChar}.

节点已存在，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*nbrcount*：邻居个数

·*parentcount*：父节点个数

另外*Node-flag*可能有多个，含义分别是：

·RmtNbr：忽略2-way检查邻居

·Tree：在树上

·Tent：在备选链表上

·Direct：与根节点直连

·Overload：Overload标志

·Delete：待删除

 

DEC: (MT*topology-id*) Set overload flag on node,{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, with attribute {.TableTextChar}*Node-flag*1, {.TableTextChar}*Node-flag*2{.TableTextChar}.

设置overload标志，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*nbrcount*：邻居个数

·*parentcount*：父节点个数

另外*Node-flag*可能有多个，含义分别是：

·RmtNbr：忽略2-way检查邻居

·Tree：在树上

·Tent：在备选链表上

·Direct：与根节点直连

·Overload：Overload标志

·Delete：待删除

 

DEC: (MT*topology-id*) Set direct flag on node,{.TableTextChar} system ID= *system-id,* neighbour count= *nbrcount,* parent count= *parentcount*, with attribute {.TableTextChar}*Node-flag*1, {.TableTextChar}*Node-flag*2{.TableTextChar}.

设置和父节点直连的标志，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*nbrcount*：邻居个数

·*parentcount*：父节点个数

另外*Node-flag*可能有多个，含义分别是：

·RmtNbr：忽略2-way检查邻居

·Tree：在树上

·Tent：在备选链表上

·Direct：与根节点直连

·Overload：Overload标志

·Delete：待删除

 

DEC: Affected node not found.

处理LINK变化量过程中，LINK变化受影响的节点没有找到

 

DEC: DST node not found. 2-way check failed.

目的系统ID没有找到，双向LINK检查失败

 

DEC: DST node was to be deleted. 2-way check failed.

目的系统ID即将被删除，双向LINK检查失败

 

DEC: Src & Dst node were both in INIT state. 2-way check failed.

源系统ID和目的系统ID都处于初始化状态，双向LINK检查失败

 

DEC: Backward link not found. 2-way check failed.

回指LINK没有找到，双向LINK检查失败

 

DEC: Checking changed links.

处理LINK变化链上的LINK

 

DEC: Need rebuild SPT.

ISPF决策出需要重新计算拓扑树

 

DEC: (MT*topology-id*) Link(Src= *source-id*, Dst= *dest-id*) moved from parent list. Run started at Sec*= xxx,* MSec*= yyy.*

将指定的LINK源节点的父节点LIST中删除，其中：

·*topology-id*：拓扑ID

·*source-id*：源系统ID

·*dest-id*：目的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) added to candidate list. Run started at Sec*= xxx,* MSec*= yyy.*

将指定节点加入拓扑树中的候选链，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Link(Src = *source-id*, Dst = *dest-id*) added to parent list. Run started at Sec*= xxx,* MSec*= yyy.*

将指定的LINK加入到源节点的父节点LIST中，其中：

·*topology-id*：拓扑ID

·*source-id*：源系统ID

·*dest-id*：目的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) The link is invalid. Run started at Sec*= xxx,* MSec*= yyy.*

拓扑计算过程中判断出LINK是无效LINK，其中：

·*topology-id*：拓扑ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) The node(*system-id*) is invalid. Run started at Sec*= xxx,* MSec*= yyy.*

拓扑计算过程中判断出NODE是无效的，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Set SPF flag on link(Src = *source-id*, Dst = *dest-id*). Run started at Sec*= xxx,* MSec*= yyy.*

将指定LINK打上IS_SPF_LINK标记，标明在SPF树上，其中：

·*topology-id*：拓扑ID

·*source-id*：源系统ID

·*dest-id*：目的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Running Dijkstra algorithm, current calculating root node is *system-id*. Run started at Sec*= xxx,* MSec*= yyy*.

指定根节点正在执行Dijkstra算法计算拓扑树，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) added to order list. Run started at Sec*= xxx,* MSec*= yyy.*

指定节点加入orderlist，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) The node(*system-id*) will be deleted. Run started at Sec*= xxx,* MSec*= yyy*.

在拓扑计算过程中将要删除节点，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Checked reachability of node(*system-id*). Run started at Sec*= xxx,* MSec*= yyy*.

检查节点拓扑是否可达，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Topology calculation ISPF decision at Sec*= xxx,* MSec*= yyy*.

拓扑增量决策，其中：

·*topology-id*：拓扑ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Checked link(Src= *source-id*, Dst= *dest-id,* validCost*= cost*). Run started at Sec*= xxx,* MSec*= yyy.*

检查LINK是否有效，其中：

·*topology-id*：拓扑ID

·*source-id*：源系统ID

·*dest-id*：目的系统ID

·*cost*：有效度量值

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Reset SPF link information. Run started at Sec*= xxx,* MSec*= yyy*.

重置所有LINK拓扑计算的标志位，其中：

·*topology-id*：拓扑ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) I-SID pruning calculation root node(*system-id*), destination node(*system-id*), calculate I-SID= *i-sid*, ECT-Index= *ect-index*, circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*

在I-SID全计算过程中添加组播出端口，其中：

·*topology-id*：拓扑ID

·*i-sid*：I-SID值

·*ect-index*：ECT算法索引

·*circuit index*：端口索引

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) I-SID incremental calculation root node(*system-id*), destination node(*system-id*), calculate I-SID= *i-sid*, ECT-Index= *ect-index*, circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*

在I-SID增量计算过程中添加组播出端口，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*i-sid*：I-SID值

·*ect-index*：ECT算法索引

·*circuit index*：端口索引

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) I-SID incremental calculation. DEC notified FLUSH to add designated port index= *circuit index,*ECT-Index= *ect-index*. Run started at Sec*= xxx,* MSec*= yyy.*

在I-SID增量计算过程中DEC通知FLUSH添加指定端口，其中：

·*topology-id*：拓扑ID

·*ect-index*：ECT算法索引

·*circuit index*：端口索引

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) I-SID incremental calculation. DEC notified FLUSH to add I-SID= *i-sid*, B-VLAN= *bvlan-number*, ECT-Index= *ect-index,* circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*

在I-SID增量计算过程中通知FLUSH添加组播转发表项，其中：

·*topology-id*：拓扑ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

·*ect-index*：ECT算法索引

·*index*：端口索引

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Node(*system-id*) is calculating I-SID(*i-sid*) pruning*,* ECT-Index= *ect-index*, circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*

在I-SID全计算过程中添加组播出端口，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*i-sid*：I-SID值

·*ect-index*：ECT算法索引

·*circuit index*：端口索引

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) I-SID pruning calculation. DEC notified FLUSH to delete I-SID= *i-sid*, B-VLAN= *bvlan-number*, ECT-Index= *ect-index,* circuit index= *circuit index.* Run started at Sec*= xxx,* MSec*= yyy.*

在I-SID剪枝中通知FLUSH删除组播转发表项，其中：

·*topology-id*：拓扑ID

·*i-sid*：I-SID值

·*ect-index*：ECT算法索引

·*bvlan-number*：B-VLAN

·*circuit index*：端口索引

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) I-SID pruning calculation. DEC notified FLUSH to delete designated port index= *circuit index,* ECT-Index= *ect-index.* Run started at Sec*= xxx,* MSec*= yyy.*

在I-SID剪枝中DEC通知FLUSH删除端口角色，其中：

·*topology-id*：拓扑ID

·*ect-index*：ECT算法索引

·*circuit index*：端口索引

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Cleared all multicast FDB of the node(*system-id*). Run started at Sec*= xxx,* MSec*= yyy.*

清除节点下的所有指定端口信息，其中：

·*topology-id*：拓扑ID

·*system-id*：节点的系统ID

·*xxx*：秒数

·*yyy*：毫秒数

 

DEC: (MT*topology-id*) Cleared all information of the node(*system-id*). Run started at Sec= *xxx,* MSec= *yyy.*

拓扑计算过程中清除NODE上的所有信息：包括节点的父节点LIST，节点到根节点的跳数以及到根节点的距离，其中：

·*topology-id*：拓扑ID

·*system-id*：拓扑节点系统ID

·*xxx*：秒数

·*yyy*：毫秒数

DEC: (MT*topology-id*) Reset SPF node information.  Run started at Sec= *xxx,* MSec= *yyy.*

清除节点上的所有标记

DEC: (MT*topology-id*) Triggered SPF at Sec= *xxx,* MSec= *yyy*, scheduled event, old= *trigger  event*, new= *trigger* *event.*

开始新的触发，显示旧的和新的触发类型，其中：

·*topology-id*：拓扑ID

·*trigger event*：触发事件包括摘要计算、拓扑全计算、拓扑增量计算、B-VLAN-ECT变化处理、I-SID-B-VLAN变化处理、停止计算

·*xxx*：秒值

·*yyy*：毫秒值

DEC: (MT*topology-id*) SPF event *trigger-event* was scheduled.

新旧触发类型合并后的触发类型，其中：

·*topology-id*：拓扑ID

·*trigger event*：合并之后的触发事件

DEC: (MT*topology-id*) SPF was not allowed to run for inactive topology state.

当前系统处于RESET阶段，不允许拓扑计算

DEC: (MT*topology-id*) SPF stopped current running work.

当前来了优先级更高的拓扑触发事件，停止当前的操作，其中*topology-id*表示拓扑ID

DEC: (MT*topology-id*) SPF needed to restart, current running flag= *trigger-event*, new trigger flag= *trigger-event*.

拓扑事件能够合并，合并之前的事件，合并之后的事件，其中：

·*topology-id*：拓扑ID

·*trigger event*：合并之后的触发事件

DEC: (MT*topology-id*) Node(*system-id*) notified FLUSH to add ECT-Index= *ect-index* output port index= *circuit index*. Run started at Sec= *xxx,* MSec= *yyy*.

通知FLUSH删除当前节点到指定节点在指定ECT算法下的出端口索引，其中：

·*topology-id*：拓扑ID

·*system-id*：指定系统ID

·*ect-index*：指定ECT算法索引

·*circuit index*：出端口索引

·*xxx*：秒数

·*yyy*：毫秒数

DEC: (MT*topology-id*) Notified node(*system-id*) to add egress FDB: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx,* MSec= *yyy*.

通知节点添加egress表项，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

·*xxx*：秒数

·*yyy*：毫秒数

DEC: (MT*topology-id*) Notified node(*system-id*) to delete egress FDB: I-SID= *i-sid*, B-VLAN= *bvlan-number*. Run started at Sec= *xxx,* MSec= *yyy*.

通知节点删除egress表项，其中：

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*i-sid*：I-SID值

·*bvlan-number*：B-VLAN

·*xxx*：秒数

·*yyy*：毫秒数

DEC: (MT*topology-id*) SPF node(*system-id*) was *updatedType*.

通知DEC模块添加/修改/删除节点

·*topology-id*：拓扑ID

·*system-id*：系统ID

·*updatedType*：更新类型（添加/删除/修改）

DEC: (MT*topology-id*) SPF link *source-id* \--\> *dest-id* was *updatedType*: cost*= cost*.

通知DEC模块添加/修改/删除link

·*topology-id*：拓扑ID

·*source-id*：源系统ID

·*dest-id*：目的系统ID

·*updatedType*：更新类型（添加/删除/修改）link

·*cost*：cost值

【举例】

\# 两台设备建邻居DUT1和DUT2，在DTU1上配置I-SID 300、VLAN 1，打开SPF调试信息\
在DUT2上同样配置I-SID 300、VLAN 1输出如下调试信息。

\<Sysname\> debugging spbm spf

\*Jan 29 15:22:32:612 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Create(new) link 0011.2200.0001 \--\> 0011.2200.0a01.

\*Jan 29 15:22:32:612 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Adding new source entry for Link 0011.2200.0001 \--\> 0011.2200.0a01.

\*Jan 29 15:22:32:652 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Node(0011-2200-0a01) received I-SID change message: operator type= 1, I-SID= 300, B-VLAN= 1, T-flag= 1, R-flag= 1. Run started at Sec= 23513, MSec= 652.

\*Jan 29 15:22:32:652 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Create(new) link 0011.2200.0a01 \--\> 0011.2200.0001.

\*Jan 29 15:22:32:653 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Adding new source entry for Link 0011.2200.0a01 \--\> 0011.2200.0001.

\*Jan 29 15:22:32:653 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: Added the link to eigenvalue change list, link Src= 0011-2200-0a01, link Dst=  0011-2200-0001.

\*Jan 29 15:22:32:716 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Node(0011-2200-0001) received I-SID change message: operator type= 1, I-SID= 300, B-VLAN= 1, T-flag= 1, R-flag= 1. Run started at Sec= 23513, MSec= 716.

\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Topology digest is calculating at Sec= 23513, MSec= 907.

\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Local node topology is calculating at Sec= 23513, MSec= 907.

\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Running Dijkstra algorithm, current calculating root node is 0011-2200-0001. Run started at Sec= 23513, MSec= 907.

\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Node(0011-2200-0a01) multicast FDB is calculating at Sec= 23513, MSec= 907.

\*Jan 29 15:22:32:907 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) Running Dijkstra algorithm, current calculating root node is 0011-2200-0a01. Run started at Sec= 23513, MSec= 907.

\*Jan 29 15:22:32:908 2013 Sysname SPBM/7/SPBM_1_SPF: -MDC=1;

DEC: (MT0) All phases of SPF work completed at Sec= 23513, MSec= 908.

**SPBM \-- SPBM调试命令 \-- debugging spbm timer**

------------------------------------------------------------------------

【命令】

**[debugging spbm timer**]

**[undo debugging spbm timer**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging spbm timer**]命令用来打开SPBM定时器的调试信息开关。**undo debugging spbm timer**命令用来关闭SPBM定时器的调试信息开关。

缺省情况下，SPBM定时器的调试信息开关处于关闭状态。

表1-18 debugging spbm timer命令输出信息描述表

字段

描述

ADJ: Level-1 adjacency *system-id* hold timer expired on circuit *circuitName*.

Level-1邻居hold time定时器超时，其中：

·*system-id*：邻居系统ID

·*circuitName*：端口名

ADJ: P2P Hello timer expired on circuit *circuitName*.

P2P Hello定时器超时，其中*circuitName*表示端口名

DEC: (MT*topology-id)* Started SPF timer, timer value is *Millisecond* ms.

开启SPF定时器进行SPF计算调度，其中：

·*topology-id*：拓扑号

·*Millisecond*：定时器的当前时间间隔

DEC: (MT*topology-id*) Stopped SPF timer.

关闭SPF定时器停止SPF计算调度，其中*topology-id*表示拓扑ID

DEC: (MT*topology-id*) SPF timer expired.

关闭SPF定时器超时，其中*topology-id*表示拓扑ID

MAIN: Hostname timer expired.

动态主机名刷新定时器超时

MAIN: Stopped hostname timer.

关闭动态主机名刷新定时器

MAIN: Started waiting timer for exceeded max sequence number, timer value is *Millisecond* ms.

LSP序列号反转等待定时器启动，其中*Millisecond*表示定时器的当前时间间隔

UPDT: Level-1 CSNP timer expired on circuit *circuitName*.

Level-1 CSNP报文发送定时器超时，其中*circuitName*表示端口名

UPDT: Level-1 PSNP timer expired on circuit *circuitName*.

Level-1 PSNP报文发送定时器超时，其中circuitName表示端口名

UPDT: Level-1 P2P retransmit timer expired on circuit *circuitName*.

Level-1 P2P重传定时器超时，其中circuitName表示端口名

UPDT: Level-1 flood timer expired on circuit *circuitName*.

Level-1 LSP报文发送定时器超时，其中circuitName表示端口名

UPDT: Level-1 fast flood timer expired.

Level-1 LSP快速扩散定时器超时，其中*circuitName*表示端口名

UPDT: LSP *lsp-id* generate timer expired.

LSP生成定时器超时，其中*lsp-id*表示LSP-ID

UPDT: Started Level-1 LSP *lsp-id* generate timer, timer value is *Millisecond* ms.

启动Level-1 LSP生成时间间隔定时器，其中

·*lsp-id*：LSP-ID

·*Millisecond*：LSP生成定时器的当前时间间隔

UPDT: Stopped level-1 LSP *lsp-id* generate timer.

关闭Level-1 LSP生成时间间隔定时器，其中*lsp-id*表示LSP-ID

【举例】

\# 使能SPBM功能，打开SPBM定时器调试信息开关，会输出下列调试信息。

\<Sysname\> debugging spbm timer

\*Sep 17 13:35:52:192 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;

UPDT: Level-1 P2P retransmit timer expired on circuit GigabitEthernet0/1/3.

\*Sep 17 13:35:52:440 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;

ADJ: P2P hello timer expired on circuit GigabitEthernet0/1/3.

\*Sep 17 13:35:54:612 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;

UPDT: Level-1 PSNP timer expired on circuit GigabitEthernet0/1/3.

\*Sep 17 13:46:14:240 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;

UPDT: Started Level-1 LSP 0011.2200.0001.00-00 generate timer, timer value is 2000 ms.

\*Sep 17 13:46:16:242 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;

UPDT: LSP 0011.2200.0001.00-00 generate timer expired.

\*Sep 17 13:46:16:242 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;

DEC: (MT0) Started SPF timer, timer value is 450 ms.

\*Sep 17 13:46:16:694 2012 Sysname SPBM/7/SPBM_1_TMR: -MDC=1;

DEC: (MT0) SPF timer expired.

**SPBM \-- SPBM调试命令 \-- debugging spbm update-packet**

------------------------------------------------------------------------

【命令】

**[debugging**]**spbm****update-packet** \**[ receive **[\|]** send ** \**verbose**]

**[undo**]**debugging****spbm****update-packet **\**[ receive **[\|]** send ** \**verbose**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：表示接收LSP报文调试信息开关。

**[send**]：表示发送LSP报文调试信息开关。

**[verbose**]：表示LSP报文详细调试信息开关。

【描述】

**[debugging spbm **]**update-packet**命令用来打开SPBM LSP报文的调试信息开关。**undo debugging spbm update-packet**命令用来关闭SPBM LSP报文的调试信息开关。

缺省情况下，SPBM LSP报文的调试信息开关处于关闭状态。

表1-19 debugging spbm update-packet命令输出信息描述表

字段

描述

UPDT: LSP with more than three area addresses.

LSP报文中携带的区域地址个数多于3个

UPDT: Parsed dynamic host name *HostName*.

解析动态主机名

UPDT: Updated dynamic host name advertised by *system-id*.

更新由*system-id*宣告的动态主机名

UPDT: (MT*topology-id*) *updatedType* SPF link(*source-id-\>dest-id*).

向路由计算模块更新SPF Link，其中：

·*topology-id*：发布默认路由的SPF节点所在的拓扑ID

·*updateType*：更新类型（添加/删除/修改）

·*source-id*：源Source ID

·*dest-id*：目的Source ID

UPDT: (MT*topology-id*) *updatedType* SPF node(*nodesource-id*).

向路由计算模块更新SPF节点，其中：

·*topology-id*：SPF节点所在的拓扑ID

·*updateType*：更新类型（添加/删除/修改）

·*node**source-id*：SPF节点的Source ID

UPDT: *PDUName system-id.pseudonodeNumber-LSPNumber* would be flooded on circuit *circuitName*.

扩散LSP报文，其中：

·*PDUName*：L1 LSP/L2 LSP

·*system-id*：LSP发送设备的系统ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*LSPNumber*：LSP报文的分片号

·*circuitName*：扩散端口名

UPDT: Sent *PDUName* *system-id*.*pseudonodeNumber-LSPNumber* sequence number= *LSPSequenceNumber* holdtime= *holdTime* from snpa *mac-address* on circuit *circuitName*.

发送LSP报文，其中：

·*PDUName*：L1 LSP/L2 LSP

·*system-id*：LSP发送设备的系统ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*LSPNumber*：LSP报文的分片号

·*LSPSequenceNumber*：LSP报文的序列号

·*holdTime*：LSP报文的存活时间

·snpa：子网接入点

·*mac-address*：LSP报文发送端口的MAC地址

·*circuitName*：LSP报文发送端口名

UPDT: Received *pdutype* could not pass authentication, LSP-ID= *lsp-id*, LSP has been ignored.

无法通过认证，LSP报文被丢弃，其中：

·*pdutype*：报文类型

·*lsp**-id*：LSP-ID

UPDT: Local LSP *system-id*. *pseudonodeNumber*-*LSPNumber* processed is newer than LSDB copy.

处理比LSDB中新的本地生成的LSP报文，其中：

·*system-id*：LSP发送设备的系统ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*LSPNumber*：LSP报文的分片号

UPDT: Other LSP *system-id*. *pseudonodeNumber*-*LSPNumber* processed is newer than LSDB copy.

处理比LSDB中新的非本地生成的LSP报文，其中：

·*system-id*：LSP发送设备的系统ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*LSPNumber*：LSP报文的分片号

UPDT: LSP *system-id*. *pseudonodeNumber*-*LSPNumber* processed is older than LSDB copy.

处理比LSDB中旧的LSP报文，其中：

·*system-id*：LSP发送设备的系统ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*LSPNumber*：LSP报文的分片号

UPDT: LSP *system-id*. *pseudonodeNumber*-*LSPNumber* processed is the same as LSDB copy.

处理和LSDB中新旧一样的LSP报文，其中：

·*system-id*：LSP发送设备的系统ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*LSPNumber*：LSP报文的分片号

UPDT: Own LSP *system-id*.*pseudonodeNumber*-*LSPNumber* processed does not exist in LSDB.

处理LSDB中不存在的本地生成的LSP报文，其中：

·*system-id*：LSP发送设备的系统ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*LSPNumber*：LSP报文的分片号

UPDT: Other LSP *system-id*.*pseudonodeNumber*-*LSPNumber* processed does not exist in LSDB.

处理LSDB中不存在的非本地生成的LSP报文，其中：

·*system-id*：LSP发送设备的系统ID

·*pseudonodeNumber*：LSP发送设备的伪节点ID

·*LSPNumber*：LSP报文的分片号

UPDT: Fast flooded level-1 *number* LSPs on interface *circuitName*.

端口上快速泛洪的LSP报文个数，其中：

·*number*：报文个数

·*circuitName*：端口名

【举例】

\# 打开SPBM Hello报文调试信息开关。

\<Sysname\> debugging spbm update-packet

\# 端口下使能SPBM功能，输出下列调试信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 0/1/3

Sysname-GigabitEthernet0/1/3 spbm enable

\*Sep 18 15:36:07:918 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: L1 LSP 0011.2200.0001.00-00 would be flooded on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:07:918 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: L1 LSP 0011.2200.0001.00-01 would be flooded on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:07:919 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: L1 LSP 0011.2200.0a01.00-00 would be flooded on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:07:919 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: L1 LSP 0011.2200.0a01.00-01 would be flooded on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:07:957 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: Sent L1 LSP 0011.2200.0001.00-00 sequence number= 0x00000012 holdtime= 992 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:07:958 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: Sent L1 LSP 0011.2200.0001.00-01 sequence number= 0x00000018 holdtime= 1175 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:07:958 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: Sent L1 LSP 0011.2200.0a01.00-00 sequence number= 0x00000012 holdtime= 829 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:07:959 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: Sent L1 LSP 0011.2200.0a01.00-01 sequence number= 0x00000015 holdtime= 530 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:09:927 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: L1 LSP 0011.2200.0001.00-01 would be flooded on circuit GigabitEthernet0/1/3.

\*Sep 18 15:36:09:957 2012 Sysname SPBM/7/SPBM_1_UPDT: -MDC=1;

UPDT: Sent L1 LSP 0011.2200.0001.01 sequence number= 0x00000019 holdtime= 1199 from snpa 0000-0000-0000 on circuit GigabitEthernet0/1/3.

**SPBM \-- SPBM调试命令 \-- debugging spbm-fdb bvlan-info**

------------------------------------------------------------------------

【命令】

**[debugging spbm-fdb bvlan-info**[ { **all** \| **driver** \| **message** }]]

**[undo debugging spbm-fdb bvlan-info**[ { **all** \| **driver** \| **message** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示SPBM FDB的bvlan-info相关的所有调试信息开关。

**[driver**]：表示SPBM FDB的bvlan-info下发驱动调试信息开关。

**[message**]：表示接收SPBM FDB的bvlan-info消息调试信息开关。

【描述】

**[debugging spbm-fdb bvlan-info**]命令用来打开SPBM FDB的bvlan-info调试信息开关。**undo debugging spbm-fdb bvlan-info**命令用来关闭SPBM FDB的bvlan-info调试信息开关。

缺省情况下，SPBM FDB的bvlan-info调试信息开关处于关闭状态。

表1-20 debugging spbm-fdb bvlan-info message命令输出信息描述表

字段

描述

B-VLANChange VLANBitMap:

BitMap(      0- 127): *value*

BitMap(  128- 255): *value*

BitMap(  256- 383): *value*

BitMap(  384- 511): *value*

BitMap(  512- 639): *value*

BitMap(  640- 767): *value*

BitMap(  768- 895): *value*

BitMap(  896-1023): *value*

BitMap(1024-1151): *value*

BitMap(1152-1279): *value*

BitMap(1280-1407): *value*

BitMap(1408-1535): *value*

BitMap(1536-1663): *value*

BitMap(1664-1791): *value*

BitMap(1792-1919): *value*

BitMap(1920-2047): *value*

BitMap(2048-2175): *value*

BitMap(2176-2303): *value*

BitMap(2304-2431): *value*

BitMap(2432-2559): *value*

BitMap(2560-2687): *value*

BitMap(2688-2815): *value*

BitMap(2816-2943): *value*

BitMap(2944-3071): *value*

BitMap(3072-3199): *value*

BitMap(3200-3327): *value*

BitMap(3328-3455): *value*

BitMap(3456-3583): *value*

BitMap(3584-3711): *value*

BitMap(3712-3839): *value*

BitMap(3840-3967): *value*

BitMap(3968-4095): *value*

消息中携带的VLAN位图内容

表1-21 debugging spbm-fdb bvlan-info driver命令输出信息描述表

字段

描述

Before flush(CMD: SPBM ACTION, PARAM: *operation*{.TableTextChar})

Driver Information: B-VLAN(*bvlan-number*)

下驱动之前，下驱动命令字、参数以及B-VLAN，B-VLAN为*bvlan-number*，参数*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Enable：添加

·Disable：删除

After flush(CMD: SPBM ACTION, PARAM: *operation*{.TableTextChar}) result *value*{.TableTextChar}

 Driver Information: B-VLAN(*bvlan-number*)

下驱动之后，下驱动命令字、参数、B-VLAN以及结果，B-VLAN为*bvlan-number*，参数*[operation*]{.TableTextChar}的取值以及含义如下：{.TableTextChar}

·Enable：添加

·Disable：删除

返回值*value*的含义为下驱动的结果

Refresh B-VLAN, result is 0x0, B-VLAN list is:

BitMap(2048-2175):00000000 00000000 00000000 00000000

BitMap(2176-2303):00000000 00000000 00000000 00000000

BitMap(2304-2431):00000000 00000000 00000000 00000000

BitMap(2432-2559):00000000 00000000 00000000 00000000

BitMap(2560-2687):00000000 00000000 00000000 00000000

BitMap(2688-2815):00000000 00000000 00000000 00000000

BitMap(2816-2943):00000000 00000000 00000000 00000000

BitMap(2944-3071):00000000 00000000 00000000 00000000

BitMap(3072-3199):00000000 00000000 00000000 00000000

BitMap(3200-3327):00000000 00000000 00000000 00000000

BitMap(3328-3455):00000000 00000000 00000000 00000000

BitMap(3456-3583):00000000 00000000 00000000 00000000

BitMap(3584-3711):00000000 00000000 00000000 00000000

BitMap(3712-3839):00000000 00000000 00000000 00000000

BitMap(3840-3967):00000000 00000000 00000000 00000000

BitMap(3968-4095):00000000 00000000 00000000 00000000

下驱动的消息中携带的VLAN位图内容

【举例】

\# 使能SPBM功能，打开组播SPBM FDB的bvlan-info消息调试信息开关，当SPBM FDB收到SPBM下发的bvlan-info变化消息会输出下列调试信息。

\<Sysname\> debugging spbm-fdb bvlan-info message

\# 下发添加VLAN ID 1～4094。

\*Sep 13 14:34:08:191 2012 Sysname SPBM FDB/7/SPBM FDB B-VLAN: -MDC=1;

B-VLANChange VlanBitMap:

BitMap(   0- 127):feffffff ffffffff ffffffff ffffffff

BitMap( 128- 255):ffffffff ffffffff ffffffff ffffffff

BitMap( 256- 383):ffffffff ffffffff ffffffff ffffffff

BitMap( 384- 511):ffffffff ffffffff ffffffff ffffffff

BitMap( 512- 639):ffffffff ffffffff ffffffff ffffffff

BitMap( 640- 767):ffffffff ffffffff ffffffff ffffffff

BitMap( 768- 895):ffffffff ffffffff ffffffff ffffffff

BitMap( 896-1023):ffffffff ffffffff ffffffff ffffffff

BitMap(1024-1151):ffffffff ffffffff ffffffff ffffffff

BitMap(1152-1279):ffffffff ffffffff ffffffff ffffffff

BitMap(1280-1407):ffffffff ffffffff ffffffff ffffffff

BitMap(1408-1535):ffffffff ffffffff ffffffff ffffffff

BitMap(1536-1663):ffffffff ffffffff ffffffff ffffffff

BitMap(1664-1791):ffffffff ffffffff ffffffff ffffffff

BitMap(1792-1919):ffffffff ffffffff ffffffff ffffffff

BitMap(1920-2047):ffffffff ffffffff ffffffff ffffffff

\*Sep 13 14:34:08:191 2012 Sysname SPBM FDB/7/SPBM FDB B-VLAN: -MDC=1;

B-VLANChange VlanBitMap:

BitMap(2048-2175):ffffffff ffffffff ffffffff ffffffff

BitMap(2176-2303):ffffffff ffffffff ffffffff ffffffff

BitMap(2304-2431):ffffffff ffffffff ffffffff ffffffff

BitMap(2432-2559):ffffffff ffffffff ffffffff ffffffff

BitMap(2560-2687):ffffffff ffffffff ffffffff ffffffff

BitMap(2688-2815):ffffffff ffffffff ffffffff ffffffff

BitMap(2816-2943):ffffffff ffffffff ffffffff ffffffff

BitMap(2944-3071):ffffffff ffffffff ffffffff ffffffff

BitMap(3072-3199):ffffffff ffffffff ffffffff ffffffff

BitMap(3200-3327):ffffffff ffffffff ffffffff ffffffff

BitMap(3328-3455):ffffffff ffffffff ffffffff ffffffff

BitMap(3456-3583):ffffffff ffffffff ffffffff ffffffff

BitMap(3584-3711):ffffffff ffffffff ffffffff ffffffff

BitMap(3712-3839):ffffffff ffffffff ffffffff ffffffff

BitMap(3840-3967):ffffffff ffffffff ffffffff ffffffff

BitMap(3968-4095):ffffffff ffffffff ffffffff ffffff7f

\# 使能SPBM功能，打开组播SPBM FDB的bvlan-info驱动调试信息开关，当SPBM FDB收到SPBM下发的bvlan-info变化消息会输出下列调试信息。

\<Sysname\> debugging spbm-fdb bvlan-info driver

\# 下发删除VLAN ID 4094。

\*Sep 13 15:03:51:127 2012 Sysname SPBM FDB/7/SPBM FDB B-VLAN DRV: -MDC=1;

Before flush(CMD: SPBM ACTION, PARAM: Disable)

Driver Information: B-VLAN(4094)

\*Sep 13 15:03:51:127 2012 Sysname SPBM FDB/7/SPBM FDB B-VLAN DRV: -MDC=1;

After flush(CMD: SPBM ACTION, PARAM: Disable) result 0x0

Driver Information: B-VLAN(4094)

**SPBM \-- SPBM调试命令 \-- debugging spbm-fdb multicast-fib**

------------------------------------------------------------------------

【命令】

**[debugging spbm-fdb multicast-fib**[ { **all** \| **driver** \| **message** }]]

**[undo debugging spbm-fdb multicast-fib**[ { **all** \| **driver** \| **message** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示组播SPBM FDB所有的调试信息开关。

**[driver**]：表示组播SPBM FDB表项下发驱动调试信息开关。

**[message**]：表示接收SPBM组播MAC添加、删除、出端口添加和删除消息调试信息开关。

【描述】

**[debugging spbm-fdb multicast-fib**]命令用来打开组播SPBM FDB调试信息开关。**undo debugging spbm-fdb multicast-fib**命令用来关闭组播SPBM FDB调试信息开关。

缺省情况下，组播SPBM FDB调试信息开关处于关闭状态。

表1-22 debugging spbm-fdb multicast-fib message命令输出信息描述表

字段

描述

Received the message for *operation*{.TableTextChar} multicast MAC entry, length= *length-value.*

具体某一个组播表项消息的头部，包括操作类型*[operation*]{.TableTextChar}和消息长度*length-value*（不包括本消息头），*[operation*]{.TableTextChar}的取值以及含义如下：

·refreshing：刷新

·deleting：删除

Received the message for *operation*{.TableTextChar} multicast MAC iflist, length= *length-value*.

具体某一个组播出端口消息的头部，包括操作类型*[operation*]{.TableTextChar}和消息长度*length-value*（不包括本消息头），*[operation*]{.TableTextChar}的取值以及含义如下：

·adding：添加

·deleting：删除

Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*) OutIFNum(*number*) RouteFlag(*flag-value*)

                         MulticastMACContext(*context-value*)

具体某一个组播表项消息的内容，MAC为*macaddr-value*，B-VLAN为*bvlan-number*，出端口数目为*number*，RouteFlag为*flag-value*，表项中保存的驱动上下文为*context-value*，

Port List:

Port(*PortName*) OutIFContext(*context-value*)

出端口列表，Port为*PortName*，出端口驱动上下文

Started to smooth.

开始平滑

Ended to smooth.

结束平滑

Received multicast MAC resource recovery message.

驱动资源恢复时通知组播重新下驱动信息

Port(*PortName*) Operation(*operation*{.TableTextChar}).

端口是否使能SPBM，Port为*PortName*，*[operation*]{.TableTextChar}的取值以及含义如下：

·Disable：去使能

·Enable：使能

表1-23 debugging spbm-fdb multicast-fib driver命令输出信息描述表

字段

描述

Before flush(Operation: *operation{.TableTextChar}*)

下驱动之前，操作类型*[operation*]{.TableTextChar}的取值以及含义如下：

·AddEntry：添加

·DeleteEntry：删除

After flush(Operation: *operation{.TableTextChar}*) result *value*

下驱动之后，操作类型*[operation*]{.TableTextChar}的取值以及含义如下：

·AddEntry：添加

·DeleteEntry：删除

返回值*value*的含义为下驱动的结果

Before flush(Operation: *operation*{.TableTextChar} Port: *PortName*)

下驱动之前，端口下的操作类型*[operation*]{.TableTextChar}的取值以及含义如下：

·Disable：去使能

·Enable：使能

After flush(Operation: *operation*{.TableTextChar} Port: *PortName*)  result *value*

下驱动之后，端口下的操作类型*[operation*]{.TableTextChar}的取值以及含义如下：

·Disable：去使能

·Enable：使能

返回值*value*的含义为下驱动的结果

Old Driver Information:

MAC(*macaddr-value*) B-VLAN(*bvlan-number*) OutIFNum(*number*) RouteFlag(*flag-value*)

Driver Context(*context-value*)

下驱动前信息，MAC为*macaddr-value*，B-VLAN为*bvlan-number*，出端口数目为*number*，RouteFlag为*flag-value*，驱动上下文为*context-value*

Port List:

Port(*PortName*) OutIFContext(*context-value*)

出端口列表，Port为*PortName*，出端口驱动上下文

Added Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*). Refreshed driver node for insufficient resource.

资源不足重刷节点组播添加操作的信息，MAC为*macaddr-value*，B-VLAN为*bvlan-number*

Deleted Multicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*). Refreshed driver node for insufficient resource.

资源不足重刷节点组播删除操作的信息，MAC为*macaddr-value*，B-VLAN为*bvlan-number*

【举例】

\# 使能SPBM功能，打开组播SPBM FDB调试信息开关，当SPBM FDB收到SPBM下发的组播MAC出端口添加消息会输出下列调试信息。

\<Sysname\> debugging spbm-fdb multicast-fib all

\*Sep 13 11:09:14:213 2012 Sysname SPBM FDB/7/SPBM FDB MMAC: -MDC=1;

Received the message for adding multicast MAC iflist, length= 40.

Multicast MAC: MAC(0362-3600-0100) B-VLAN(1) OutIFNum(1) RouteFlag(TE)

               MulticastMACContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)

\*Sep 13 11:09:14:213 2012 Sysname SPBM FDB/7/SPBM FDB MMAC: -MDC=1;

Port List:

Port(GE0/1/3) OutIFContext(0xffffffff,0xffffffff)

\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC DRV: -MDC=1;

Before flush(Operation: AddEntry)

\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC DRV: -MDC=1;

Driver Information:

MAC(0362-3600-0100) B-VLAN(1) OutIFNum(1) RouteFlag(TE)

DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)

\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC: -MDC=1;

Port List:

Port(GE0/1/3) OutIFContext(0xffffffff,0xffffffff)

\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC DRV: -MDC=1;

After flush(Operation:AddEntry) result 0x40010001

\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC DRV: -MDC=1;

Driver Information:

MAC(0362-3600-0100) B-VLAN(1) OutIFNum(1) RouteFlag(TE)

DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)

\*Sep 13 11:09:14:214 2012 Sysname SPBM FDB/7/SPBM FDB MMAC: -MDC=1;

Port List:

Port(GE0/1/3) OutIFContext(0xffffffff,0xffffffff)

**SPBM \-- SPBM调试命令 \-- debugging spbm-fdb unicast-fib**

------------------------------------------------------------------------

【命令】

**[debugging spbm-fdb unicast-fib**[ { **all** \| **driver** \| **message** }]]

**[undo debugging spbm-fdb unicast-fib**[ { **all** \| **driver** \| **message** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示单播SPBM FDB所有的调试信息开关。

**[driver**]：表示单播SPBM FDB表项下发驱动调试信息开关。

**[message**]：表示接收SPBM单播MAC添加和删除消息调试信息开关。

【描述】

**[debugging spbm-fdb unicast-fib**]命令用来打开单播SPBM FDB调试信息开关。**undo debugging spbm-fdb unicast-fib**命令用来关闭单播SPBM FDB调试信息开关。

缺省情况下，单播SPBM FDB调试信息开关处于关闭状态。

表1-24 debugging spbm-fdb unicast-fib message命令输出信息描述表

字段

描述

Received the message for *operation*{.TableTextChar} unicast MAC entry, length= *length-value.*

具体某一个单播表项消息的头部，包括操作类型和消息长度（不包括本消息头），*[operation*]{.TableTextChar}的取值以及含义如下：

·refreshing：刷新

·deleting：删除

Unicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan- number*) Port(*PortName*) RouteFlag(*flag-value*)

                       UnicastMACContext(*context-value*)

具体某一个单播表项消息的内容，MAC为*macaddr-value*，B-VLAN为*bvlan-number*，Port为*PortName*，RouteFlag为*flag-value*，表项中保存的驱动上下文为*context-value*

Started to smooth.

开始平滑

Ended to smooth.

结束平滑

Received unicast MAC resource recovery message.

驱动资源恢复时通知单播重新下驱动

Port(*PortName*) Operation(*operation*{.TableTextChar}）.

端口是否使能SPBM，Port为*PortName*，*[operation*]{.TableTextChar}的取值以及含义如下：

·Disable：去使能

·Enable：使能

表1-25 debugging spbm-fdb unicast-fib driver命令输出信息描述表

字段

描述

Before flush(Operation: *operation{.TableTextChar}*)

下驱动之前，操作类型*[operation*]{.TableTextChar}的取值以及含义如下：

·Add：添加

·Delete：删除

After flush(Operation: *operation{.TableTextChar}*) result *value*

下驱动之后，操作类型*[operation*]{.TableTextChar}的取值以及含义如下：

·Add：添加

·Delete：删除

返回值*value*的含义为下驱动的结果

Before flush(Operation: *operation*{.TableTextChar} Port: *PortName*)

下驱动之前，端口*PortName*下的操作类型*[operation*]{.TableTextChar}的取值以及含义如下：

·Disable：去使能

·Enable：使能

After flush(Operation: *operation*{.TableTextChar} Port: *PortName*) result *value*

下驱动之后，端口下的操作类型*[operation*]{.TableTextChar}的取值以及含义如下：

·Disable：去使能

·Enable：使能

返回值*value*的含义为下驱动的结果

Driver Information:

MAC(*macaddr-value*) B-VLAN(*bvlan-number*) Port(*PortName*) RouteFlag(*flag-value*)

DriverContext(*context-value*)

下发驱动时携带的信息，MAC为*macaddr-value*，B-VLAN为*bvlan-number*，Port为*PortName*，RouteFlag为*flag-value*，驱动上下文为*context-value*

Old Driver Information:

MAC(*macaddr-value*) B-VLAN(*bvlan-number*) Port(*PortName*) RouteFlag(*flag-value*)

DriverContext(*context-value*)

下驱动前携带的信息，MAC为*macaddr-value*，B-VLAN为*bvlan-number*，Port为*PortName*，RouteFlag为*flag-value*，驱动上下文为*context-value*

Added Unicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*). Refreshed driver node for insufficient resource.

资源不足重刷节点单播添加操作的信息，MAC为*macaddr-value*，B-VLAN为*bvlan-number*

Deleted Unicast MAC: MAC(*macaddr-value*) B-VLAN(*bvlan-number*). Refreshed driver node for insufficient resource.

资源不足重刷节点单播删除操作的信息，MAC为*macaddr-value*，B-VLAN为*bvlan-number*

【举例】

\# 使能SPBM功能，打开单播SPBM FDB调试信息开关，当SPBM FDB收到SPBM下发的单播MAC刷新消息会输出下列调试信息。

\<Sysname\> debugging spbm-fdb unicast-fib all

\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC: -MDC=1;

Received the message for refreshing unicast MAC entry, ength= 32.

Unicast MAC: MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)

             UnicastMACContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)

\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;

Before flush(Operation: Add)

\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;

Driver Information:

MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)

DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)

\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;

After flush(Operation:Add) result 0x40010001

\*Sep 13 10:44:37:114 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;

Driver Information:

MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)

DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)

\# 使能SPBM功能，打开单播SPBM FDB调试信息开关，当SPBM FDB收到SPBM下发的单播MAC删除消息会输出下列调试信息。

\<Sysname\> debugging spbm-fdb unicast-fib all

\*Sep 13 10:00:40:772 2012 Sysname SPBM FDB/7/SPBM FDB UMAC: -MDC=1;

Received the message for deleting unicast MAC entry, length= 32.

Unicast MAC: MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)

             UnicastMACContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)

\*Sep 13 10:00:40:772 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;

Before flush(Operation: Delete)

\*Sep 13 10:00:40:772 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;

Driver Information:

MAC(0011-2200-0a01) B-VLAN(1) Port(GE0/1/3) RouteFlag(T)

DriverContext(0xffffffff,0xffffffff,0xffffffff,0xffffffff)

\*Sep 13 10:00:40:772 2012 Sysname SPBM FDB/7/SPBM FDB UMAC DRV: -MDC=1;

After flush(Operation:Delete) result 0x40010001
