
**MPLS TE \-- MPLS TE调试命令 \-- debugging mpls te management**

------------------------------------------------------------------------

【命令】

**[debugging mpls te management **[[ **all \| error \| event \| process** ]]]

**[undo debugging mpls te management**[ [ **all \| error \| event \| process** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示TE management所有的调试信息开关。

**[error**]：表示TE management的错误调试信息开关。

**[event**]：表示TE management的事件调试信息开关。

**[process**]：表示TE management的CRLSP创建、处理调试信息开关。

【描述】

**[debugging mpls te manatement**]命令用来打开MPLS TE management调试信息开关。**undo debugging mpls te manatement**命令用来关闭MPLS TE management调试信息开关。

缺省情况下，MPLS TE management调试信息开关处于关闭状态。

表1-1 debugging mpls te management error命令输出信息描述表

字段

描述

Failed to reply configurations.

配置处理消息回复失败

Failed to update tunnel configurations (tunnel ID: *tunnel-id*) to DBM.

更新tunnel ID为*tunnel-id*的隧道配置到DBM失败

Failed to register protocol with interface management.

向接口管理模块注册失败

Failed to send bypass tunnel message.

发送备隧道消息失败

Failed to send the ingress CRLSP creation message to RSVP: ingress LSR ID *ingress-lsr-id*, egress LSR ID *egress-lsr-id*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction-value*.

向RSVP发送Ingress CRLSP创建消息失败。Ingress CRLSP头节点LSR ID为*ingress-lsr-id*，尾节点LSR ID为*egress-lsr-id*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，direction为*direction-value*

Not enough resources are available to complete the operation.

申请内存失败

表1-2 debugging mpls te management event命令输出信息描述表

字段

描述

Disconnected from tunnel management unexpectedly.

与Tunnel管理的链接由于异常断开

Registered protocol with interface management.

向接口管理注册成功

Sent the ingress CRLSP creation message to RSVP: ingress LSR ID *ingress-lsr-id*, egress LSR ID *egress-lsr-id*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction-value*.

向RSVP发送Ingress CRLSP创建消息成功。Ingress CRLSP头节点LSR ID为*ingress-lsr-id*，尾节点LSR ID为*egress-lsr-id*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，direction为*direction-value*

Received an ingress CRLSP up notification: ingress LSR ID *ingress-lsr-id*, egress LSR ID *egress-lsr-id*, tunnel ID *tunnel-id*, LSP ID *lsp-id*.

收到Ingress CRLSP UP消息。Ingress CRLSP头节点LSR ID为*ingress-lsr-id*，尾节点LSR ID为*egress-lsr-id*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*

Protocol registered events (*event-value*).

协议注册事件类型为*event-value*的事件

表1-3 debugging mpls te management process命令输出信息描述表

字段

描述

Status of CRLSP (tunnel ID *tunnel-id*, LSP ID *lsp-id*) changed from *old-state* to *new-state*

Tunnel ID为*tunnel-id*，LSP ID为*lsp-id*的CRLSP从状态*old-state*切换到新状态*new-state*

Status of TE tunnel (tunnel ID *tunnel-id*) changed from *old-state* to *new-state*.

Tunnel ID为*tunnel-id*的TE隧道口从状态*old-state*切换到新状态*new-state*

Sent the batch backup message.

发送批备消息成功

Created a local NHLFE entry: tunnel interface *tunnel-interface-name*, destination IP address *destination-ip*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, source IP address *source-ip*, direction *direction-value*.

创建local NHLFE表项成功。Tunnel接口名为*tunnel-interface-name*，目的地址为*destination-ip*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id，*源地址为*source-ip*，direction为*direction-value*

Setting up timer of CRLSP (tunnel ID *tunnel-id*, LSP ID *lsp-id*) expired.

Tunnel ID为*tunnel-id*， LSP ID为*lsp-id*的CRLSP setting up定时器超时

【举例】

\# 设备上打开MPLS TE management错误调试信息开关。TE模块向RSVP发送消息，失败时打印如下调试信息。

\<Sysname\> debugging mpls te management error

\*Mar 12 05:31:02:030 2014 Sysname TE/7/ERROR: -MDC=1; Failed to send the ingress CRLSP creation message to RSVP: ingress LSR ID 1.1.1.1; egress LSR ID 2.2.2.2; tunnel ID 1; LSP ID 34265; direction 0.

*// 向RSVP发送头节点LSR ID为1.1.1.1，尾节点LSR ID为2.2.2.2，tunnel ID为1，LSP ID为34265，direction为0的Ingress CRLSP创建消息失败。*

\# 设备上打开MPLS TE management事件调试信息开关。向RSVP模块发送或从RSVP模块接收消息时，打印如下调试信息。

\*Mar 17 06:16:53:910 2014 Sysname TE/7/EVENT: -MDC=1; Sent the ingress CRLSP creation message to RSVP: ingress LSR ID 1.1.1.1; egress LSR ID 2.2.2.2; tunnel ID 1; LSP ID 20432; direction 0.

*// 向RSVP发送头节点LSR ID为1.1.1.1，尾节点LSR ID为2.2.2.2，tunnel ID为1，LSP ID为20432，direction为0的Ingress CRLSP创建消息成功。*

\*Mar 17 06:16:53:913 2014 Sysname TE/7/EVENT: -MDC=1; Received an ingress CRLSP up notification: ingress LSR ID 1.1.1.1; egress LSR ID 2.2.2.2; tunnel ID 1; LSP ID 20432.

*// 收到头节点LSR ID为1.1.1.1，尾节点LSR ID为2.2.2.2，tunnel ID为1，LSP ID为20432 的ingress CRLSP UP消息。*

\# 设备上打开MPLS TE management处理过程调试信息开关。TE隧道创建时，打印如下调试信息。

\*Mar 17 06:16:53:912 2014 Sysname TE/7/PROCESS: -MDC=1; Status of CRLSP (tunnel ID 1; LSP ID 20432) changed from SETUP to READY.

*[// Tunnel ID*]*为1，LSP ID为20432的CRLSP从状态SETUP切换到新状态READY。*

\*Mar 17 06:16:53:912 2014 Sysname TE/7/PROCESS: -MDC=1; Status of TE tunnel (tunnel ID 1) changed from HBK MAINSETUP to HBK BKSETUP.

*[// Tunnel ID*]*为1的TE隧道口从状态HBK MAINSETUP切换到新状态HBK BKSETUP。*

**MPLS TE \-- MPLS TE调试命令 \-- debugging mpls te cspf**

------------------------------------------------------------------------

【命令】

**[debugging mpls te cspf **[[ **all \| computation \| error \| event \| tedb** ] ]]

**[undo debugging mpls te cspf**[ [ **all \| computation \| error \| event \| tedb** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示TE CSPF所有的调试信息开关。

**[computation**]：表示TE CSPF的路径计算调试信息开关

**[error**]：表示TE CSPF的错误调试信息开关。

**[event**]：表示TE CSPF的事件调试信息开关。

**[tedb**]：表示TE CSPF的TEDB数据库维护调试信息开关。

【描述】

**[debugging mpls te cspf**]命令用来打开MPLS TE CSPF调试信息开关。**undo debugging mpls te cspf**命令用来关闭MPLS TE CSPF调试信息开关。

缺省情况下，MPLS TE CSPF调试信息开关处于关闭状态。

表1-4 debugging mpls te cspf computation命令输出信息描述表

字段

描述

Received a computation request message: tunnel ID *tunnel-id*, LSP ID *lsp-id*.

收到tunnel ID为*tunnel-id*，LSP ID为*lsp-id*的路径计算请求消息

Can\'t decode the computation request message.

无法解析该计算请求消息

Added a path node to the shortest path list: LSR ID *lsr-id*, area ID *area-value*, pre-LSR ID *prelsr-id*, in interface IP *in-interface-ip*, metric m*etric-value*, min bandwidth *min-bandwidth*, bandwidth *bandwidth,*hop count number *ho-count*.

向最短路径表中添加一个path节点：LSR ID为*lsr-id*，area ID为*area-value*，pre-LSR ID为*prelsr-id*，入接口IP地址为*in-interface-ip*，metric为m*etric-value*，最小带宽为*min-bandwidth*，实际带宽为*bandwidth，*下一跳个数为*ho-count*

Computed a path in IGP *igp-type*.

在类型为*igp-type*的IGP域成功计算一条路径

表1-5 debugging mpls te cspf error命令输出信息描述表

字段

描述

Failed to reply configurations.

配置处理消息回复失败

Failed to upgrade the thread.

PCE进程升级失败

Failed to activate the service.

PCE激活服务端口失败

The loose hop address was invalid.

松散地址是无效值

表1-6 debugging mpls te cspf event命令输出信息描述表

字段

描述

Can\'t process a node with an invalid link type

无法处理无效链路类型节点

Entered the critical memory alert threshold.

进入critical内存门限

Quitted the severe memory alert threshold.

退出severe内存门限

表1-7 debugging mpls te cspf tedb命令输出信息描述表

字段

描述

Updated a link node.

成功更新链路信息节点

Created an IGP mapping node: IGP type *igp-type*, LSR ID *lsr-id*, VRF index *vrf-index*, process ID *process-id*, area ID *area-value*.

创建一个IGP映射节点：IGP type为*igp-type*，LSR ID为*lsr-id*，VRF索引为*vrf-index*，进程号为*process-id*，area ID为*area-value*

Created a network node.

成功创建一个网络信息节点

Deleted an IGP mapping node: IGP type *igp-type*, LSR ID *lsr-id*, VRF index *vrf-index*, process ID *process-id*, area ID *area-value*.

成功删除一个IGP映射节点：IGP type为*igp-type*，LSR ID为*lsr-id*，VRF索引为*vrf-index*，进程号为*process-id*，area ID为*area-value*的

Failed to update the mapping node.

更新映射节点失败

Received an invalid IGP message.

收到一个无效IGP消息

【举例】

\# 设备上打开MPLS TE CSPF计算调试信息开关。TE隧道创建时，打印如下调试信息。

\<Sysname\> debugging mpls te cspf computation

\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Received a computation request message：tunnel ID 1, LSP ID 20432.

\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Added a path node to the shortest path list: LSR ID 1.1.1.1; area ID 0; pre-LSR ID 0.0.0.0; in interface IP 0.0.0.0; metric 0; min bandwidth 4294967295; bandwidth 0; hop count number 0.

\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Added a path node to the heap: LSR ID 2.2.2.2; area ID 0; pre-LSR ID 1.1.1.1, in interface IP 12.1.22.2; metric 1; min bandwidth 0; bandwidth 0; hop count number 1.

\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Added a path node to the shortest path list: LSR ID 2.2.2.2; area ID 0; pre-LSR ID 1.1.1.1; in interface IP 12.1.22.2; metric 1; min bandwidth 0; bandwidth 0; hop count number 1.

\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Computed a path in IGP OSPF.

*// 成功计算一条TE隧道路径。*

\# 设备上打开MPLS TE CSPF错误调试信息开关。配置响应发送失败时，打印如下调试信息。

\<Sysname\> debugging mpls te cspf error

\*Mar 17 06:30:21:538 2014 Sysname PCE/7/ERROR: -MDC=1; Failed to reply configurations.

*// 配置消息回应失败。*

\# 设备上打开MPLS TE CSPF TE事件调试信息开关。当内存进入三级门限时，打印如下调试信息。

\<Sysname\> debugging mpls te cspf event

\*Mar 17 06:30:21:537 2014 Sysname PCE/7/EVENT: -MDC=1; Entered the critical memory alert threshold.

*// 进入内存门限告警。*

\# 设备上打开MPLS TE CSPF TE数据库调试信息开关。新增加TEDB数据信息时，打印如下调试信息。

\<Sysname\> debugging mpls te cspf tedb

\*Mar 17 06:30:21:534 2014 Sysname PCE/7/TEDB: -MDC=1; Created an IGP mapping node: IGP type OSPF; LSR ID 1.1.1.1; VRF index 0; process ID 1; area ID 0.

*// 创建一个IGP类型为OSPF, LSR ID为1.1.1.1，VRF索引为0，进程ID为1，Area ID为0的IGP映射节点。*

**MPLS TE \-- MPLS TE调试命令 \-- debugging mpls te pce**

------------------------------------------------------------------------

【命令】

**[debugging mpls te pce **[{ **all** \| **brpc** { **all** \| **pcreq** \| **pcrep** [ **peer** *ip-address* ] \| **process** } \| **cspf** { **all** \| **computation** \| **process** } \| **epc** { **all** \| **pcreq** \| **pcrep**  **peer** *ip-address*  \| **process** } \| **error** \| **event** \| **pcep** { **all** \| **packet** { **received** \| **sent** } \| **pcerr** \| **pcntf** \| **session** \| **fsm** \| **socket**  **peer** *ip-address*  } \| **process** \|]  **tedb** \| **timer** }]

**[undo debugging mpls te pce **[{ **all** \| **brpc** { **all** \| **pcreq** \| **pcrep** [ **peer** *ip-address* ] \| **process** } \| **cspf** { **all** \| **computation** \| **process** } \| **epc** { **all** \| **pcreq** \| **pcrep**  **peer** *ip-address*  \| **process** } \| **error** \| **event** \| **pcep** { **all** \| **packet** { **received** \| **sent** } \| **pcerr** \| **pcntf** \| **session** \| **fsm** \| **socket**  **peer** *ip-address*  } \| **process** \| **tedb** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示PCE的所有调试信息开关。

**[brpc**]**：**表示跨域计算的调试信息开关。

·**all****：**表示跨域计算的所有调试信息开关。

·**pcreq****：**表示跨域计算请求消息的调试信息开关。

·**pcrep****：**表示跨域计算回复消息的调试信息开关。

·**peer ***ip-address***：**表示指定对等体的调试信息开关。如果不指定本参数，则打开所有对等体的调试信息开关。

·**process****：**表示跨域计算的处理过程调试信息开关。

**[cspf**]**：**表示CSPF的调试信息开关。

·**all****：**表示CSPF的所有调试信息开关。

·**computation****：**表示CSPF计算的调试信息开关。

·**process****：**表示CSPF处理过程调试信息开关。

**[epc**]**：**表示域内计算的调试信息开关。

·**all****：**表示域内计算的所有调试信息开关。

·**pcreq****：**表示域内计算请求消息的调试信息开关。

·**pcrep****：**表示域内计算回复消息的调试信息开关。

·**peer ***ip-address***：**表示指定对等体的调试信息开关。如果不指定本参数，则打开所有对等体的调试信息开关。

·**process****：**表示域内计算处理过程调试信息开关。

**[error**]：表示PCE的错误调试信息开关。

**[event**]：表示PCE的事件调试信息开关。

**[pcep**]**：**表示PCEP的调试信息开关

·**all****：**表示PCEP的所有调试信息开关。

·**packet**：表示所有PCEP消息调试信息开关。

·**received**：表示PCEP接收消息调试信息开关。

·**sent**：表示PCEP发送消息调试信息开关。

·**pcerr**：表示PCEP PCErr消息调试信息开关。

·**pcntf**：表示PCEP PCNtf消息调试信息开关。

·**session**：表示PCEP会话调试信息开关。

·**fsm****：**表示PCEP状态机调试信息开关。

·**socket**：表示PCEP套接字调试信息开关。

·**peer ***ip-address*：表示指定对等体的PCEP调试信息开关。如果不指定本参数，则打开所有对等体的PCEP调试信息开关。

**[process**]：表示PCE处理过程调试信息开关。

**[tedb**]**：**表示TEDB调试信息开关。

**[timer**]：表示PCE定时器调试信息开关。

【描述】

**[debugging mpls te pce**]命令用来打开PCE的调试信息开关。**undo debugging mpls te pce**命令用来关闭PCE的调试信息开关。

缺省情况下，PCE调试信息开关处于关闭状态。

表1-8 debugging mpls te pce error命令输出信息描述表

字段

描述

Failed to encode message: message type=*msg-type*.

消息编码失败

·*msg**-type*：消息类型

Failed to decode message: message type=*msg-type*, length=*msg-len*.

消息解码失败

·*msg**-type*：消息类型

·*msg**-len*：消息长度

Not enough resources are available to complete the operation.

socket buffer分配内存失败

Failed to delete PCE configurations from DBM: PCE address=*pce-address*, instance ID= *instance-id*.

从DBM中删除本地PCE的配置失败

·*pce-address*：PCE地址

·*instance-id*：实例号

Failed to delete PCE peer configurations from DBM: PCE address= *pce-address*, instance ID= *instance-id*.

从DBM中删除PCE peer的配置失败

·*pce-address*：PCE地址

·*instance-id*：实例号

Failed to send configuration response message.

发送配置回应消息失败

Failed to send display respond message.

发送显示回应消息失败

Failed to write message to queue: message type=*msg-type,* sub message type=*sub-msg-type*.

往队列里写消息失败

·*msg**-type*：消息类型

·*sub**-msg-type*：子消息类型

Failed to write an event.

写事件失败

Failed to set parameter: type name=*type-name,* option type=*option-type*.

设置参数失败

·*type-name*：参数名称

·*option-type*：选择类型

Failed to get parameter *type-name*.

获取参数失败

·*type-name*：参数名称

Failed to create a TCP socket.

创建socket失败

Failed to bind a socket: error=*error-info*.

绑定socket失败

·*error**-info*：错误信息

Failed to listen to a TCP socket: error=*error-info*.

监听socket失败

·*error**-info*：错误信息

Failed to receive TCP data from socket *socket-id*: error=*error-info*.

从socket接收TCP数据失败

·*socket-id*：套接字ID

·*error**-info*：错误信息

Failed to create TCP accept socket: error=*error-info*.

创建TCP接收socket失败

·*error**-info*：错误信息

Failed to establish a connection to RIB.

连接RIB失败

Failed to create the timer.

定时器创建失败

Failed to set the timer: sec=*sec,* nsec=*nsec*.

设置定时器时间失败

·*sec*：秒

·*nsec*：微秒

Failed to reset the timer.

重置定时器失败

Failed to get the configuration: instance=*instance-id*.

获取配置失败

·*instance-id*：实例号

Failed to save request-id-number to DBM.

保存request-id-number到数据库失败

Received an invalid message: type=*msg-type*, length=*msg-len*.

接收到不合法消息

·msg-type：消息类型

·msg-len：消息长度

表1-9 debugging mpls te pce event命令输出信息描述表

字段

描述

Sent an event to IGP: event type=*event-type*, result=*result.*

发送*event-type*事件到IGP

·*event-type*：事件类型

·*result*：发送结果

Failed to keep current connection (found same protocol).

当前连接断开 （发现相同协议的连接）

Received an event from IGP: event type=*event-type*.

接收来自IGP的*event-type*事件

·*event-type*：事件类型

Received a message with unknown TLV type=*tlv-type*.

收到含有未知消息类型的TLV

·*tlv-type*：TLV类型

Received a PCUpd message.

接收到一个PCUpd消息

Received a PCRpt message.

接收到一个PCRpt消息

Received a PCRpt message from a stateless session.

从无状态会话收到一个PCRpt消息

Received a PCUpd message from a stateless session.

从无状态会话收到一个PCUpd消息

Sent an event to IGP: event type=*event-type*, result=*result.*

发送*event-type*事件到IGP

·*event-type*：事件类型

·*result*：发送结果

Sent an event to IGP: event type=*event-type*, instance=*instance-id*, process ID=*process-id*.

成功发送*event-type*事件到IGP

·*event-type*：事件类型

·*instance-id*：实例号

·*process-id*：OSPF进程号

表1-10 debugging mpls te pce process命令输出信息描述表

字段

描述

Added a new PCE *pce-address* to synchronization group.

添加新的PCE到同步组

·*p**ce-address*：PCE地址

Can\'t find matched request: reply ID=*reply-id*.

没有找到匹配的请求

·*reply-id*：回复消息ID

Received an invalid CSPF result: reply ID=*reply-id*.

接收到一个不合法的CSPF结果

·*reply-id*：回复消息ID**

Received a reply from CSPF: reply ID=*reply-id*.

从CSPF接收到一个回复消息

·*reply-id*：回复消息ID

Received a request from CSPF: source address=*source-address*, dest address=*dest-address*, tunnel ID=*tunnel-id*, local LSP ID=*local-lsp-id*.

从CSPF接收到一个请求消息

·*source-address*：源地址

·*dest-address*：目的地址

·*tunnel-id*：隧道ID

·*local-lsp-id*：本地LSP ID

Received a request cancellation from CSPF: source address=*source-address*, dest address=*dest-address*, tunnel ID=*tunnel-id*, local LSP ID=*local-lsp-id*.

从CSPF接收到一个请求取消消息

·*source-address*：源地址

·*dest-address*：目的地址

·*tunnel-id*：隧道ID

·*local-lsp-id*：本地LSP ID

Received a cancellation of all requests from CSPF.

从CSPF接收到一个取消所有请求的消息

Received a synchronization start message from CSPF.

从CSPF接收到一个开始同步的消息

Received a synchronization end message from CSPF.

从CSPF接收到一个同步结束的消息

Sent an event to PCECP: event type=*event-type*, sub event type=*sub-event-type*.

发送一个事件给PCECP

·*event-type*：事件类型

·*sub-event-type*：子事件类型

Sent an event to CSPF: event type=*event-type*.

发送一个事件给CSPF

·*event-type*：事件类型

Sent a result to CSPF: source address=*source-address*, dest address=*dest-address*, tunnel ID=*tunnel-id*, local LSP ID=*local-lsp-id.*

发送计算结果给CSPF

·*source-address*：源地址

·*dest-address*：目的地址

·*tunnel-id*：隧道ID

·*local-lsp-id*：本地LSP ID

Sent a request to CSPF: source address=*source-address*, dest address=*dest-address*, reply ID=*reply-id*.

发送请求消息到CSPF

·*source-address*：源地址

·*dest-address*：目的地址

·*reply-id*：回复消息ID

Sent a request cancellation to CSPF: reply ID=*reply-id*.

发送请求取消消息到CSPF

·*reply-id*：回复消息ID

Sent an update message to CSPF.

发送update消息到CSPF

Sent a report message to CSPF.

发送report消息到CSPF

表1-11 debugging mpls te pce timer命令输出信息描述表

字段

描述

Created the *timer-name* timer (*sec-count* sec) for a session: peer=*peer-address:instance-id*, session role=*session-role*.

会话创建*timer-name*定时器成功

·*timer-name*：定时器的名字

·*sec-count*：定时器设置时间，单位为秒

·*peer-address*：对端的地址

·*instance-id*：实例号

·*session-role*：本地会话的角色

Created the request timer: PCE address=*pce-address,* request ID=*request-id*.

创建请求定时器成功

·*pce-address*：PCE的地址

·*request-id*：请求消息ID

Created the *timer-name* timer: instance=*instance-id*.

创建*timer-name*定时器成功

·*timer-name*：定时器的名字

·*instance-id*：实例号

Deleted the *timer-name* timer for a session: peer=*peer-address:instance-id*, session role=*session-role*.

会话删除*timer-name*定时器成功

·*timer-name*：定时器的名字

·*peer-address*：对端的地址

·*instance-id*：实例号

·*session-role*：本地会话的角色

Deleted the request timer: PCE address=*pce-address,* request ID=*request-id*.

删除请求定时器成功

·*pce-address*：PCE的地址

·*request-id*：请求消息ID

Request timer expired: PCE address=*pce-address,* request ID=*request-id.*

请求定时器超时

·*pce-address*：PCE的地址

·*request-id*：请求消息ID

The *timer-name* timer expired for a session: peer=*peer-address:instance-id*, session role=*session-role*.

会话*timer-name*定时器超时

·*timer-name*：定时器的名字

·*peer-address*：对端的地址

·*instance-id*：实例号

·*session-role*：本地会话的角色

The *timer-name* timer expired: instance=*instance-id*.

*[timer-name*]定时器超时

·*timer-name*：定时器的名字

·*instance-id*：实例号

表1-12 debugging mpls te pce pcep packet命令输出信息描述表

字段

描述

Received *msg-type* message from a peer: peer=*peer-address:instance-id*, message content: .

接收来自对等体的*msg-type*消息

·*msg**-type*：消息类型

·*instance-id*：实例号

·*peer-address*：对端地址

Sent *msg-type* message to a peer: peer=*peer-address:instance-id*, message content: .

发送*msg-type*消息给对等体

·*msg**-type*：消息类型

·*instance-id*：实例号

·*peer-address*：对端地址

表1-13 debugging mpls te pce pcep pcerr命令输出信息描述表

字段

描述

Received a PCEP error from peer: error info=*error-info,* peer=*peer-address:instance-id*.

接收来自对等体的PCErr消息

·*error**-info*：错误信息

·*instance-id*：实例号

·*peer-address*：对端地址

Sent a PCEP error to peer: error info=*error-info,* peer=*peer-address:instance-id*.

发送PCErr消息给对等体

·*error**-info*：错误信息

·*instance-id*：实例号

·*peer-address*：对端地址

表1-14 debugging mpls te pce pcep fsm命令输出信息描述表

字段

描述

Session received an event: peer=*peer-address:instance-id,* session role*=session-role,* event type=*event-type,* state=*session-state*.

会话接收*event-type*类型事件

·*peer-address*：对端地址

·*instance-id*：实例号

·*session-role*：会话角色

·*event-type*：事件类型

·*session-state*：会话状态

Status of the session changed from *presession-state* to *cursession-state*: peer=*peer-address:instance-id,* session role*=session-role*.

会话状态改变

·*peer-address*：对端地址

·*instance-id*：实例号

·*session-role*：会话角色

·*presession-state*：改变之前会话状态

·*cursession-state*：当前的会话状态

表1-15 debugging mpls te pce pcep session命令输出信息描述表

字段

描述

Created a new session: peer=*peer-address:instance-id,* session role*=session-role*.

创建新的会话

·*peer-address*：对端地址

·*instance-id*：实例号

·*session-role*：会话角色

Destroyed the session: peer=*peer-address:instance-id,* session role*=session-role*.

释放会话资源成功

·*peer-address*：对端地址

·*instance-id*：实例号

·*session-role*：会话角色

Failed to get the local address for session: peer=*peer-address:instance-id,* session role*=session-role*.

会话获取本地地址失败

·*peer-address*：对端地址

·*instance-id*：实例号

·*session-role*：会话角色

Opened a TCP connection: socket=*socket-id*, peer=*peer-address:instance-id*.

打开TCP连接

·*peer-address*：对端地址

·*instance-id*：实例号

·*socket-id*：套接字ID

表1-16 debugging mpls te pce pcep socket命令输出信息描述表

字段

描述

Accepted a new socket *socket-id*.

接收新的socket连接

·*socket-id*：套接字ID

Closed the TCP server: socket=*socket-id*.

关闭TCP服务端成功

·*socket-id*：套接字ID

Failed to create a TCP connection to transport address *transport-address*: error=*error-info*.

创建TCP连接传输地址失败

·*transport-address*：传输地址

·*error**-info*：错误信息

Failed to send TCP data: peer *peer-address:instance-id*.  Error=*error-info*

给对端发送TCP数据失败

·*peer-address*：对端地址

·*instance-id*：实例号

·*error**-info*：错误信息

Opened the TCP server: socket=*socket-id*.

打开TCP服务端成功

·*socket-id*：套接字ID

TCP is down abnormally: socket=*socket-id*.

TCP 异常关闭

·*socket-id*：套接字ID

The message might be too large for peer *peer-address* to process.

消息太大对端可能不能处理

·*peer-address*：对端地址

表1-17 debugging mpls te pce brpc pcreq命令输出信息描述表

字段

描述

Received a PCReq from peer (*peer-address*, *instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* END-POINTS: source=*source-address*, destination=*dest-address*

从对端接收到一个请求消息

·*peer-address*：对端地址

·*instance-id*：实例号

·*request-id*：请求ID

·*VSPT-flag*：BRPC计算标志位

·*O-flag*：松散、严格路径标志位

·*B-flag*：双向、单向路径标志位

·*R-flag*：重优化路径标志位

·*priority-value*：计算优先级

·*source-address*：源地址

·*dest-address*：目的地址

Sent a PCReq to peer (*peer-address*, *instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* END-POINTS: source=*source-address*, destination=*dest-address*

发送一个请求消息到对端

·*peer-address*：对端地址

·*instance-id*：实例号

·*request-id*：请求ID

·*VSPT-flag*：BRPC计算标志位

·*O-flag*：松散、严格路径标志位

·*B-flag*：双向、单向路径标志位

·*R-flag*：重优化路径标志位

·*priority-value*：计算优先级

·*source-address*：源地址

·*dest-address*：目的地址

表1-18 debugging mpls te pce brpc pcrep命令输出信息描述表

字段

描述

PCE list: *pce-list* Sent a PCRep to peer (*peer-address, instance-id*): Request-ID-number: *request-id* Flags: SPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* Path: *interfere-address-list*

发送一个回复消息到对端

·*pce-list*：PCE地址列表

·*peer-address*：传输地址

·*instance-id*：实例号

·*request-id*：请求ID

·*VSPT-flag*：BRPC计算标志

·*O-flag*：松散、严格路径标志位

·*B-flag*：双向、单向路径标志位

·*R-flag*：重优化路径标志位

·*priority-value*：计算优先级

·*i**nterfere-address-list*：接口地址列表

PCE list: *pce-list* Received a PCRep from peer: (*peer-address, instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* Path: *interfere-address-list*

从对端接收一个回复消息

·*pce-list*：PCE地址列表

·*peer-address*：传输地址

·*instance-id*：实例号

·*request-id*：请求ID

·*VSPT-flag*：BRPC计算标志位

·*O-flag*：松散、严格路径标志位

·*B-flag*：双向、单向路径标志位

·*R-flag*：重优化路径标志位

·*priority-value*：计算优先级

·*i**nterfere-address-list*：接口地址列表

表1-19 debugging mpls te pce brpc process命令输出信息描述表

字段

描述

Failed to get the external PCE for inter-domain request.

域间路径计算请求获取PCE失败

Number of requests reached the limit.

请求数目达到最大数目

表1-20 debugging mpls te pce epc pcreq命令输出信息描述表

字段

描述

Received a PCReq from peer (*peer-address*, *instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* END-POINTS: source=*source-address*, destination=*dest-address*

从对端接收一个请求消息

·*peer-address*：对端地址

·*instance-id*：实例号

·*request-id*：请求ID

·*VSPT-flag*：BRPC计算标志位

·*O-flag*：松散、严格路径标志位

·*B-flag*：双向、单向路径标志位

·*R-flag*：重优化路径标志位

·*priority-value*：优先级

·*source-address*：源地址

·*dest-address*：目的地址

Sent a PCReq to peer (*peer-address*, *instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* END-POINTS: source=*source-address*, destination=*dest-address*

发送一个请求消息到对端

·*peer-address*：对端地址

·*instance-id*：实例号

·*request-id*：请求ID

·*VSPT-flag*：BRPC计算标志位

·*O-flag*：松散、严格路径标志位

·*B-flag*：双向、单向路径标志位

·*R-flag*：重优化路径标志位

·*priority-value*：计算优先级

·*source-address*：源地址

·*dest-address*：目的地址

表1-21 debugging mpls te pce epc pcrep命令输出信息描述表

字段

描述

Received a PCRep from peer (*peer-address, instance-id*):

Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* Path: *interfere-address-list*

从对端接收一个回复消息

·*peer-address*：传输地址

·*instance-id*：实例号

·*request-id*：请求ID

·*VSPT-flag*：BRPC计算标志位

·*O-flag*：松散、严格路径标志位

·*B-flag*： 双向、单向路径标志位

·*R-flag*：重优化路径标志位

·*priority-value*：优先级

·*Interfere-address**-list*：接口地址列表

Sent a PCRep to peer (*peer-address, instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* Path: *interfere-address-list*

发送一个回复消息到对端

·*peer-address*：传输地址

·*instance-id*：实例号

·*request-id*：请求ID

·*VSPT-flag*：BRPC计算标志位

·*O-flag*：松散、严格路径标志位

·*B-flag*：双向、单向路径标志位

·*R-flag*：重优化路径标志位

·*priority-value*：优先级

·*Interfere-address**-list*：接口地址列表

表1-22 debugging mpls te pce epc process命令输出信息描述表

字段

描述

Failed to get an external PCE for intra-domain request.

域内路径计算请求获取PCE失败

Number of requests reached the limit.

请求消息达到最大个数

【举例】

\# 打开PCE事件调试信息开关，配置本地PCE的地址为10.10.10.1后，设备上打印如下调试信息。

\<Sysname\> debugging mpls te pce event

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce address 10.10.10.1

\*Dec 20 12:24:00:581 2013 Sysname PCECP/7/EVENT: -MDC=1; Sent an event (advertise local PCE) to IGP successfully. Instance: 0, process ID: 1.

*// 向IGP通告本地PCE，实例号为0，OSPF进程号为1。*

\# 打开PCE定时器调试信息开关，配置本地PCE的地址为1.1.1.1后，设备上打印如下调试信息。

\<Sysname\> debugging mpls te pce timer

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce address 1.1.1.1

\*Dec 20 13:10:30:215 2013 PE1 PCECP/7/TIMER: -MDC=1; Created the OpenWait timer (60 sec) successfully for session (3.3.3.1:0, passive).

*// 会话创建OpenWait定时器成功，对端地址为3.3.3.1，实例号为：0，会话角色为：passive。*

\*Dec 20 13:10:30:215 2013 PE1 PCECP/7/TIMER: -MDC=1; Deleted the OpenWait timer successfully for session (3.3.3.1:0, passive).

*// 会话删除OpenWait定时器成功，对端地址为3.3.3.1，实例号为：0，会话角色为：passive。*

\# 打开PCEP的发送消息调试信息开关，设备上会话处于up状态时，如果Keepalive定时器超时，设备上打印如下调试信息。

\<Sysname\> debugging mpls te pcep packet sent

\*Dec 20 13:53:00:668 2013 PE1 PCECP/7/PACKET SENT: -MDC=1; Sent a Keepalive message to peer (3.3.3.1:0). Message content: 20 02 00 04.

*// 给对端发送Keepalive消息，对端的地址为3.3.3.1，实例号为0，消息内容为20 02 00 04。*

\# 打开PCEP的接收消息调试信息开关，收到对等体的Keepalive消息时，设备上打印如下调试信息。

\<Sysname\> debugging mpls te pcep packet received

\*Dec 20 13:11:29:438 2013 P2 PCECP/7/PACKET RECEIVED: -MDC=1; Received a Keepalive message from peer (1.1.1.1:0). Message content: 20 02 00 04.

*// 接收来自对端的Keepalive消息，对端的地址为1.1.1.1，实例号为0，消息内容为20 02 00 04。*

\# 打开PCEP的状态机调试信息开关，配置PCE的IP地址为1.1.1.1后，设备上打印如下调试信息。

\<Sysname\> debugging mpls te pcep fsm

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce address 1.1.1.1

\*Dec 21 08:17:39:968 2013 P1 PCECP/7/FSM: -MDC=1; Session (4.4.4.1:0, active) received event (TCP connect), state: Idle.

*// 会话接收到TCP连接事件，当前会话状态为Idle。*

\*Dec 21 06:24:37:073 2013 PE1 PCECP/7/FSM: -MDC=1; Changed the session (3.3.3.1:0, passive) state from Idle to TCPPending.

*// 会话状态由Idle变为TCPPending。*

\# 打开PCEP套接字调试信息开关，执行撤销本地PCE地址命令后，设备上将打印如下调试信息。

\<Sysname\> debugging mpls te pcep socket

\<Sysname\> system-view

Sysname mpls te

Sysname-te undo pce address

\*Dec 20 14:27:52:634 2013 PE1 PCECP/7/SOCKET: -MDC=1; Closed the TCP server (socket: 35) successfully.

*[//*]*成功关闭了TCP服务端，socket资源为35。*

\# 打开PCEP会话调试信息开关，配置PCE的地址为1.1.1.1后，设备上将打印如下调试信息。

\<Sysname\> debugging mpls te pcep session

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce address 1.1.1.1

\*Dec 21 06:24:37:073 2013 PE1 PCECP/7/SESSION: -MDC=1; Created a new session (3.3.3.1:0, passive).

*// 创建新的会话，对端地址3.3.3.1，实例号0，会话角色passive。*

\# 打开BRPC请求消息调试信息开关，在Tunnel接口下执行**mpls te path**命令后，设备上将打印如下调试信息。

\<Sysname\> debugging mpls te pce brpc pcreq

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 destination 3.3.3.3

Sysname-Tunnel0 mpls te path preference 1 dynamic pce 2.2.2.2 3.3.3.3

\*Jun 27 03:20:31:406 2014 H3C PCE/7/PCREQ: -MDC=1; PCE list: 2.2.2.2         3.3.3.3 Sent a request to peer (2.2.2.2:0): Request-ID-number: 0x2 Flags: VSPT=1, O=1, B=0, R=0, Pri=6 END-POINTS: source=1.1.1.1, destination=3.3.3.3.

*// 给对端peer发送请求消息，PCE地址为2.2.2.2，3.3.3.3，对端peer地址2.2.2.2，实例号为 0，请求ID为0x2，VSPT标志位为1，O标志位为1，B标志位为0，R标志位为0，优先级为6，源地址为1.1.1.1，目的地址为3.3.3.3。*

\# 打开BRPC回复消息调试信息开关，在Tunnel接口下执行**mpls te path**命令后，设备上将打印如下调试信息。

\<Sysname\> debugging mpls te pce brpc pcrep

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 destination 3.3.3.3

Sysname-Tunnel0 mpls te path preference 1 dynamic pce 2.2.2.2 3.3.3.3

\*Jun 27 03:20:31:408 2014 PCE2 PCE/7/PCREP: -MDC=1; Received a reply from peer (3.3.3.3:0): Request-ID-number: 0x2 Flags: VSPT=1, O=1, B=0, R=0, Pri=6 Path: 20.1.1.1 \--\> 20.1.1.2 \--\> 2.2.2.2 \--\> 30.1.1.1 \--\> 30.1.1.2.

*// 给对端peer发送回复消息，对端peer地址2.2.2.2，实例号为0，请求ID为0x2，VSPT标志位为1，O标志位为1，B标志位为0，R标志位为0，优先级为6，接口地址列表为20.1.1.1，20.1.1.2，2.2.2.2，30.1.1.1，30.1.1.2。*

\# 打开EPC请求消息调试信息开关，在Tunnel接口下执行**mpls te path**命令后，设备上将打印如下调试信息。

\<Sysname\> debugging mpls te pce epc pcreq

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 destination 3.3.3.3

Sysname-Tunnel0 mpls te path preference 1 dynamic pce 3.3.3.3

\*Jun 27 03:13:40:741 2014 H3C PCE/7/PCREQ: -MDC=1; Sent a request to peer (3.3.3.3:0): Request-ID-number: 0x1 Flags: VSPT=0, O=1, B=0, R=1, Pri=7 END-POINTS: source=2.2.2.2, destination=3.3.3.3.

*// 给对端peer发送请求消息，PCE地址3.3.3.3，对端peer地址3.3.3.3，实例号为0，请求ID为0x1，VSPT标志位为0，O标志位为1，B标志位为0，R标志位为1，优先级为7，源地址为2.2.2.2，目的地址为3.3.3.3。*

\# 打开EPC回复消息调试信息开关，在Tunnel接口下执行**mpls te path**命令后，设备上将打印如下调试信息。

\<Sysname\> debugging mpls te pce epc pcrep

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 destination 3.3.3.3

Sysname-Tunnel0 mpls te path preference 1 dynamic pce 3.3.3.3

\*Jun 27 03:13:40:743 2014 H3C PCE/7/PCREP: -MDC=1; Received a reply  from peer (3.3.3.3:0): Request-ID-number: 0x1 Flags: VSPT=0, O=1, B=0, R=1, Pri=7 Path: 20.1.1.1 \--\> 20.1.1.2.

*// 给对端peer发送回复消息，对端peer地址3.3.3.3，实例号为0，请求ID为0x1，VSPT标志位为0，O标志位为1，B标志位为0，R标志位为1，优先级为7，接口地址列表为20.1.1.1，20.1.1.2。*

**MPLS TE \-- MPLS TE调试命令 \-- debugging isis mpls te**

------------------------------------------------------------------------

【命令】

**[debugging isis mpls te **[[ **advertisement** \| **event** \| **map** ]  *process-id* ]]

**[undo debugging isis mpls te **[[ **advertisement** \| **event \| map** ]  *process-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advertisement**]：表示链路或节点TE信息调试信息开关。

**[event**]：表示IS-IS TE的事件调试信息开关。

**[map**]：表示隧道目的地址与隧道目的端设备System ID映射关系的调试信息开关。

*[process-id*]：表示指定IS-IS进程的调试信息开关。*process-id*为IS-IS进程号，取值范围为1～65535。如果不指定本参数，则表示所有IS-IS进程的调试信息开关。

【描述】

**[debugging isis mpls te**]命令用来打开IS-IS TE调试信息开关。**undo debugging isis mpls te**命令用来关闭IS-IS TE调试信息开关。

缺省情况下，IS-IS TE调试信息开关处于关闭状态。

执行本命令时，如果没有指定任何参数，则表示所有IS-IS TE调试信息开关。

表1-23 debugging isis mpls te advertisement命令输出信息描述表

字段

描述

ISIS-*process-id*-TE

IS-IS进程*process-id*的TE调试信息

Updated level-*Level* LSR ID *lsr-id* in TEDB.

更新LSR ID到TEDB

*[Level*]：系统级别，取值为1或2

*[lsr-id*]：MPLS LSR ID，点分十进制格式

Deleted level-*Level* LSR ID *lsr-id* from TEDB.

删除TEDB中的LSR ID信息

*[Level*]：系统级别，取值为1或2

*[lsr-id*]：MPLS LSR ID，点分十进制格式

Updated TE node overload state (*state*).{.MsoCommentReference} level-*Level*, system ID: *system-id.*

更新TEDB中节点的Overload状态

*[state*]：节点的Overload状态，取值为TRUE或者FALSE

*[Level*]：系统级别，取值为1或2

*[system-id*]：节点的System ID

Updated TE link. level-*Level*, type: *type*, neighbor ID: *nbr-id*, local address count: *count_l*, remote address count: *count_r*.

更新TEDB中的TE Link信息

*[Level*]：系统级别，取值为1或2

*[nbr-id*]：扩展IS邻居的ID

*[type*]：链路类型

*[count_l*]：本地接口的IP址个数

*[count_r*]：邻居的IP址个数

Deleted TE link. level-*Level*, type: *type*, neighbor ID: *nbr-id*, local address count: *count_l*, remote address count: *count_r*.

从TEDB中删除TE Link信息

*[Level*]：系统级别，取值为1或2

*[nbr-id*]：扩展IS邻居的ID

*[count_l*]：本地接口的IP址个数

*[count_r*]：邻居的IP址个数

Updated TE network. level-*Level*, source ID: *source-id*.

更新TEDB中的网络信息

*[Level*]：系统级别，取值为1或2

*[source-id*]：LSP生成路由器的System ID

Deleted TE network. level-*Level*, source ID: *source-id*.

从TEDB中删除网络信息

*[Level*]：系统级别，取值为1或2

*[source-id*]：LSP生成路由器的System ID

Deleted all information in Level-*Level* TEDB.

删除指定Level的TEDB中的信息

*[Level*]：系统级别，取值为1或2

表1-24 debugging isis mpls te event命令输出信息描述表

字段

描述

ISIS-*process-id*-TE

IS-IS进程*process-id*的TE调试信息

Received a TE enable state change event.

IS-IS接收到TE使能状态变化事件

Received an interface TE information change event.

IS-IS接收到接口TE信息变化事件

Received a TE tunnel interface information update event.

IS-IS接收到TE隧道接口信息更新事件

Received a TE tunnel interface information delete event.

IS-IS接收到TE隧道接口信息删除事件

Received an MPLS LSR ID change event.

IS-IS接收到TE上报的MPLS LSR ID变化事件

Received a level-*Level* tunnel destination address update event.

IS-IS接收到TE隧道目的地址更新事件

*[Level*]：系统级别，取值为1或2

表1-25 debugging isis mpls te map命令输出信息描述表

字段

描述

ISIS-*process-id*-TE

IS-IS进程*process-id*的TE调试信息

Notified TEDB to add a mapping for the destination *ip-address* of tunnel *tunnel-name* in level-*Level*.

通知TEDB为某个Tunnel的目的地址生成映射

*[Level*]：系统级别，取值为1或2

*[tunnel-name*]：隧道接口名

*[ip-address*]：隧道接口的目的地址

Notified TEDB to delete the mapping for the destination *ip-address* of tunnel *tunnel-name* in level-*Level*.

通知TEDB删除某个Tunnel的目的地址的映射

*[Level*]：系统级别，取值为1或2

*[tunnel-name*]：隧道接口名

*[ip-address*]：隧道接口的目的地址

(MT*topoId*) (L*Level*) Added a mapping in IS-IS. TE tunnel: *tunnel-name*, destination address: *ip-address*, SPF node: *system-id*.

在IS-IS模块添加一条映射信息，这条映射信息是将隧道*tunnel-name*的目的地址*ip-address*映射到SPF节点*system-id。*

*[topoId*]：拓扑号

*[Level*]：系统级别，取值为1或2

*[tunnel-name*]：隧道接口名

*[ip-address: *]隧道接口目的地址

*[system-id*]：SPF节点的System ID

(MT*topoId*) (L*Level*) Updated the mapping in IS-IS. TE tunnel: *tunnel-name*, destination address: *ip-address*, SPF node: *system-id*.

在IS-IS模块更新一条映射信息，这条映射信息是将隧道*tunnel-name*的目的地址*ip-address*映射到SPF节点*system-id*。

*[topoId*]：拓扑号

*[Level*]：系统级别，取值为1或2

*[tunnel-name*]：隧道接口名

*[ip-address: *]隧道接口目的地址

*[system-id*]：SPF节点的System ID

(MT*topoId*) (L*Level*) Deleted the mapping in IS-IS. TE tunnel: *tunnel-name*, destination address: *ip-address*, SPF node: *system-id*.

在IS-IS模块删除一条映射信息，这条映射信息是将隧道*tunnel-name*的目的地址*ip-address*映射到SPF节点*system-id*。

*[topoId*]：拓扑号

*[Level*]：系统级别，取值为1或2

*[tunnel-name*]：隧道接口名

*[ip-address*]：隧道接口目的地址

*[system-id*]：SPF节点的System ID

【举例】

\# 设备上打开所有IS-IS TE调试信息开关。在设备上全局、接口使能IS-IS TE和关闭IS-IS TE功能时，打印如下调试信息。

\<Sysname\> debugging isis mpls te 1

%May 7 11:01:22:257 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Received an MPLS LSR ID change event.

%May 7 11:01:22:260 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Updated level-1 LSR ID 7.0.0.2 in TEDB.

%May 7 11:01:22:269 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Updated level-2 LSR ID 7.0.0.1 in TEDB.

*// 全局使能IS-IS TE，更新TEDB信息*。*

%May 7 11:01:22:278 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Received an interface TE information change event.

%May 7 11:01:22:286 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Updated TE link. level-1, type: Broadcast, neighbor ID: 0000.0000.0001.01, local address count: 1, remote address count: 0.

%May 7 11:01:22:299 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Updated TE link. level-2, type: Broadcast, neighbor ID: 0000.0000.0001.01, local address count: 1, remote address count: 0.

*//接口使能IS-IS TE，增加TEDB信息*。

%May 7 11:01:22:310 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Received an interface TE information change event.

%May 7 11:01:22:326 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Deleted TE link. level-1, type: Broadcast, neighbor ID: 0000.0000.0001.01, local address count: 1, remote address count: 0.

%May 7 11:01:22:345 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Deleted TE link. level-2, type: Broadcast, neighbor ID: 0000.0000.0001.01, local address count: 1, remote address count: 0.

*//接口关闭IS-IS TE功能，删除TEDB信息*。

%May 7 11:01:22:390 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Received a TE enable state change event.

%May 7 11:01:22:410 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Deleted all information in Level-1 TEDB.

%May 7 11:01:22:540 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Deleted all information in Level-2 TEDB.

*// 全局关闭IS-IS TE功能，删除TEDB信息。*

**MPLS TE \-- MPLS TE调试命令 \-- debugging ospf mpls te**

------------------------------------------------------------------------

【命令】

**[debugging** **ospf** [ *process-id*  **mpls te** [ **advertisement** \| **event** \| **pce** ]]]

**[undo debugging ospf **[ *process-id*  **mpls te** [ **advertisement** \| **event** \| **pce** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：表示指定OSPF进程的调试信息开关。*process-id*为OSPF进程号，取值范围为1～65535。如果不指定本参数，则表示所有OSPF进程的调试信息开关。

**[advertisement**]：表示OSPF TE通告调试信息开关。

**[event**]：表示OSPF TE事件调试信息开关。

**[pce**]：表示OSPF PCE通告调试信息开关。

【描述】

**[debugging ospf mpls te**]命令用来打开OSPF TE调试信息开关。**undo debugging ospf mpls te**命令用来关闭OSPF TE调试信息开关。

缺省情况下，OSPF TE调试信息开关处于关闭状态。

表1-26 debugging ospf mpls te advertisement命令输出信息描述表

字段

描述

Notify CSPF to update one link of node *node-id*. Result: *result*, link type: *link-type*, link ID: *link-id*.

通知CSPF更新节点*node-id*的Link信息

·*node-id*：OSPF中为Router ID；IS-IS中为systemID

·*result*：更新结果，取值为success或者fail

·*link-type*：链路类型，1为P2P，2为广播网，3为NBMA，4为P2MP

·*link-id*：链路ID

Notify CSPF to delete one link of node *node-id*. Result: *result*, link type: *link-type*, link ID: *link-id*.

通知CSPF删除节点*node-id*的Link信息

Notify CSPF to delete the LSR ID of node *node-id*. Result: *result*.

通知CSPF删除节点*node-id*的LSR ID

Notify CSPF to update the LSR ID of node *node-id*. Result: *result*, new LSR ID: *lsr-id*.

通知CSPF更新节点*node-id*的LSR ID

Notify CSPF to update the network information of node *node-id*. Result: *result*, attatched router number: *number*.

通知CSPF更新节点*node-id*的network信息，其中，*number*表示相连路由器的个数

Notify CSPF to delete the network information of node *node-id*. Result: *result*, attatched router number: *number*.

通知CSPF删除节点*node-id*的network信息

Notify CSPF of the smooth event *event*. Result: *result*.

通知CSPF平滑事件*event*，*event*取值包括：

·9：表示平滑开始

·10：表示平滑结束

Notify CSPF of the process GR event *event*. Result: *result*, process: *process-id*.

通知CSPF进程GR事件*event*，*event*取值包括：

·6：表示GR开始

·7：表示GR结束

Notify CSPF of the area delete event. Result: *result*, process: *process-id*, area: *area-id*.

通知CSPF进程*process-id*的区域*area-id*删除

表1-27 debugging ospf mpls te event命令输出信息描述表

字段

描述

OSPF *process-id* area *area-id*

·{.TableTextChar}*process-id*：OSPF进程号

·*area-id*：区域ID

MPLS TE is enabled.

OSPF区域使能TE功能

MPLS TE is disabled.

OSPF区域去使能TE功能

Updated the router TLV in TEDB.

更新TEDB中的Router TLV信息

Deleted the router TLV in TEDB.

删除TEDB中的Router TLV信息

Updated the link TLV in TEDB.

更新TEDB中的Link TLV信息

Deleted the link TLV in TEDB.

删除TEDB中的Link TLV信息

Deleted all information in TEDB.

删除TEDB中的所有信息

Link TLV invalid.

因Link TLV信息错误没有更新TEDB

Advertising router

发布者的Router ID

Opaque ID

Opaque ID

LSR ID

发布信息的路由器的LSR ID

Link type

链路类型，取值包括：

·1：表示P2P链路

·2：表示广播链路

·3：表示NBMA链路

·4：表示P2MP链路

Link ID

链路ID

Local interface address number

本地接口地址个数

Remote interface address number

远端接口地址个数

Updated the network information in TEDB.

更新TEDB的Network信息

Deleted the network information in TEDB.

删除TEDB的Network信息

DR address

广播网DR的IP地址

Updated the TE information of the interface.

更新接口的TE信息

Deleted the TE information of the interface.

删除接口的TE信息

Updated the tunnel interface information.

更新Tunnel接口信息

Deleted the tunnel interface information.

删除Tunnel接口信息

Interface index: *index*.

接口索引

TE metric

接口的TE度量值

Administrative Group

接口的管理组属性

Bandwidth constrain model

接口使用的带宽约束模型

Maximum bandwidth

链路的最大带宽

maximum reservable bandwidth

链路的最大可预留带宽

Destination

Tunnel接口的目的地址

Tunnel metric

Tunnel接口的metric

Route flag

路由标记

表1-28 debugging ospf mpls te pce命令输出信息描述表

字段

描述

OSPF instance *vrfIndex*, process *process-id*:

*[vrfIndex*]： VRF实例索引

*[process-id*]：OSPF进程号

Updated PCED TLV information in area(*area-id*) PCEDB. LSA type=*type*, router ID=*router-id*, PCE address=*pce-address*.

更新LSA中的PCED TLV信息到PCEDB

*[area-id*]：OSPF区域ID

*[type*]：TLV所属LSA的类型，取值包括：

·Opq-AS：表示Opaque-AS类型的LSA

·Opq-Area：表示Opaque-Area类型的LSA

*[router-id*]：TLV所属LSA的生成路由器ID

*[pce-address*]：TLV中携带的PCE地址值

Deleted PCED TLV information in area(*area-id*) PCEDB. LSA type=*type*, router ID=*router-id*, PCE address=*pce-address*.

删除PCEDB中的PCED TLV信息

*[area-id*]：OSPF区域ID

*[type*]：TLV所属LSA的类型，取值包括：

·Opq-AS：表示Opaque-AS类型的LSA

·Opq-Area：表示Opaque-Area类型的LSA

*[router-id*]：TLV所属LSA的生成路由器ID

*[pce-address*]：TLV中携带的PCE地址值

Parsed all the PCE information when global PCEP was enabled.

全局PCEP使能时解析所有PCE信息

Deleted all the PCE information when global PCEP was disabled.

全局PCEP去使能时删除所有PCE信息

Created the PCEDB in process.

创建进程下的PCEDB

Deleted the PCEDB in process.

删除进程下的PCEDB

Cleared the PCEDB in process.

清空进程下PCEDB中的数据

Created the PCEDB in area(*area-id*).

创建区域下的PCEDB

*[area-id*]：OSPF区域ID

Deleted the PCEDB in area(*area-id*).

删除区域下的PCEDB

*[area-id*]：OSPF区域ID

Cleared the PCEDB in area(*area-id*).

清空区域下PCEDB中的数据

*[area-id*]：OSPF区域ID

Updated the PCE information when the TE area was enabled.

区域使能TE时更新PCE信息

Updated the PCE information when the TE area was disabled.

区域去使能TE时更新PCE信息

【举例】

\# Router A通过GigabitEthernet1/0/1（197.168.1.1/24）与Router B的GigabitEthernet1/0/1（197.168.1.2/24）相连，网络类型为Broadcast，Router A为DR。在Router A和Router B上配置OSPF TE。在Router A上打开OSPF TE的调试信息开关后，打印如下信息。

\<RouterA\> debugging ospf 1 mpls te

OSPF process 1 area 0.0.0.1 : MPLS TE is enabled.

OSPF process 1 area 0.0.0.1 : Updated the router TLV in TEDB.

Advertising router: 7.7.7.12. Opaque ID: 0.

LSR ID: 12.1.1.2.

Notify CSPF to update the LSR ID of node 7.7.7.12. Result: success, new LSR ID: 12.1.1.2.

*// 区域使能TE，更新TEDB信息。*

OSPF process 1 : Updated the TE information of the interface.

Interface index: 7.

TE metric: 0. Administrative group: 0. Bandwidth constrain model: 0.

Maximum bandwidth: 10000000. Maximum reservable bandwidth: 0.

OSPF process 1 area 0.0.0.0 : Updated the link TLV in TEDB.

Advertising router: 7.7.7.12. Opaque ID: 1.

Link type: 1. Link ID: 2.2.2.2.

Local interface address number = 3. Remote interface address number = 1.

Notify CSPF to update one link of node 7.7.7.12. Result: success, link type: 1, link ID:7.7.7.12.

*// 接口使能TE，增加TEDB信息。*

OSPF process 1 : Deleted the TE information of the interface.

Interface index: 7.

OSPF process 1 area 0.0.0.0 : Delete the link TLV in TEDB.

Advertising router: 7.7.7.12. Opaque ID: 1.

Link type: 1. Link ID: 2.2.2.2.

Local interface address number = 3. Remote interface address number = 1.

Notify CSPF to delete one link of node 7.7.7.12. Result: success, link type: 1,

link ID:7.7.7.12.

*// 接口和全局去使能TE，删除TEDB信息*

OSPF process 1 area 0.0.0.1 : Deleted all information in TEDB.

OSPF process 1 area 0.0.0.1 : MPLS TE is disabled.

Notify CSPF of the area delete event. Result: success, process: 1, area: 0.0.0.1.

*// 区域去使能TE，删除TEDB信息*

OSPF instance 0, process 1: Created the PCEDB in process.

OSPF instance 0, process 1: Created the PCEDB in area(0.0.0.0).

OSPF instance 0, process 1: Parsed all the PCE information when global PCEP was enabled.

OSPF instance 0, process 1: Updated PCED TLV information in area(0.0.0.0) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.

*// 进程下第一个区域使能TE，解析所有PCE信息并更新PCEDB*

OSPF instance 0, process 1: Updated the PCE information when the TE area was enabled.

OSPF instance 0, process 1: Created the PCEDB in area(0.0.0.1).

OSPF instance 0, process 1: Updated PCED TLV information in area(0.0.0.0) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.

OSPF instance 0, process 1: Updated PCED TLV information in area(0.0.0.1) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.

*// 区域使能TE，更新PCEDB信息。*

OSPF instance 0, process 1: Updated the PCE information when the TE area was disabled.

OSPF instance 0, process 1: Deleted PCED TLV information in area(0.0.0.1) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.

OSPF instance 0, process 1: Cleared the PCEDB in area(0.0.0.1).

OSPF instance 0, process 1: Deleted the PCEDB in area(0.0.0.1).

OSPF instance 0, process 1: Updated PCED TLV information in area(0.0.0.0) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.

*// 区域去使能TE，删除区域下PCEDB信息，并更新其他区域PCEDB信息。*

OSPF instance 0, process 1: Deleted PCED TLV information in area(0.0.0.0) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.

*[// MPLS*]*撤销发布PCE信息，删除PCEDB信息*

OSPF instance 0, process 1: Cleared the PCEDB in area(0.0.0.0).

OSPF instance 0, process 1: Cleared the PCEDB in process.

OSPF instance 0, process 1: Deleted all the PCE information when global PCEP was disabled.

*// 全局去使能TE，清空所有PCEDB信息OSPF instance 0, process 1: Cleared the PCEDB in area(0.0.0.0).*

OSPF instance 0, process 1: Deleted the PCEDB in area(0.0.0.0).

OSPF instance 0, process 1: Cleared the PCEDB in process.

OSPF instance 0, process 1: Deleted the PCEDB in process.

*// 进程下最后一个区域去使能TE，删除所有PCEDB信息*
