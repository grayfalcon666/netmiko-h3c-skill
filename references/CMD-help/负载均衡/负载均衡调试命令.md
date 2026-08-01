<!-- CMD-INDEX
  debugging lb                        | 用户视图             | L5
-->

**负载均衡 \-- 负载均衡调试命令 \-- debugging lb**

------------------------------------------------------------------------

【命令】

**[debugging**[ **lb** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

**[undo**[ **debugging** **lb** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示负载均衡所有调试信息开关。

**[error**]：表示负载均衡错误调试信息开关。

**[event**]：表示负载均衡事件调试信息开关。

**[fsm**]：表示负载均衡状态机调试信息开关。

**[packet**]：表示负载均衡报文调试信息开关。

【描述】

**[debugging** **lb**]命令用来打开负载均衡调试信息开关。**undo** **debugging** **lb**命令用来关闭负载均衡调试信息开关。

缺省情况下，负载均衡调试信息开关处于关闭状态。

表1-1 debugging lb error命令输出信息描述表

字段

描述

Failed to delete virtual server (*name*) instance from kernel.

从内核删除虚服务*name*的实例失败

 

Failed to add virtual server (*name*) instance to kernel.

向内核添加虚服务*name*的实例失败

 

Failed to switch server farm (*name1*) of the virtual server to master/backup server farm (*name2*).

虚服务下的实服务组*name1*转为主用/备份实服务组*name2*失败

 

Failed to modify the IPv4/IPv6 address of virtual server (*name*).

修改虚服务*name*的IPv4/IPv6地址失败

 

Failed to instantiate virtual server (*name*) by *reason*.

由于*reason*，导致虚服务*name*实例化失败。*reason*包括：

·IPv4/IPv6 address change：IPv4/IPv6地址变化

·port change：端口变化

·default or backup server farm change：默认或备份实服务组变化

·enabling the server：使能虚服务

 

Failed to modify virtual server (*name*) by *reason*.

由于*reason*，导致虚服务*name*的配置修改失败。*reason*包括：

·enabling UDP forced LB：使能UDP强制负载均衡

·connection limit change：连接数限制变化

·rate limit change：连接速率变化

·bandwidth change：连接带宽变化

·ssl-server-policy change：SSL服务器策略变化

·ssl-client-policy change：SSL客户端策略变化

·redirect change：重定向内容变化

·return code change：重定向返回码变化

 

Failed to add/delete/modify an instance of the virtual server.

添加/删除/修改虚服务器实例失败

 

Failed to add the server farm due to insufficient memory in kernel.

由于内核中内存不足，导致添加实服务组失败

 

Failed to modify online state of the server farm due to failure to modify the predictor algorithm.

由于修改调度算法失败，导致修改实服务组的在线状态失败

 

Failed to modify the NAT of server farm *name*.

修改实服务组*name*的NAT功能失败

 

Failed to instantiate server farm *name* due to *reason*.

由于*reason*，导致实服务组*name*实例化失败。*reason*包括：

·insufficient memory：内存不足

·ID conflict：编号冲突

 

Failed to add server farm *name* instance to kernel.

向内核添加实服务组*name*的数据失败

 

Failed to create instance for real server *name1* associated with server farm *name2*.

被实服务组*name2*引用的实服务器*name1*实例化失败

 

Failed to modify the predictor algorithm of server farm *name* instance.

修改实服务组*name*实例的调度算法失败

 

Failed to modify the fail-action of server farm *name* instance.

修改实服务组*name*实例的故障处理失败

 

Failed to modify the active real server number of server farm *name*.

修改实服务组*name*的活动实服务器数失败

 

Failed to modify the SNAT of server farm *name*.

修改实服务组*name*的SNAT功能失败

 

Not enough memory to create server farm (*name*).

创建实服务组*name*时内存不足

 

Failed to add the real server (*name*) instance in kernel.

向内核添加实服务器*name*实例失败

 

Not enough memory to create real server (*name*).

创建实服务器*name*时内存不足

 

Failed to delete/modify the real server instance in kernel.

在内核中删除/修改实服务器实例失败

 

Failed to write real server (*name*) to DBM.

向实服务器*name*写DBM失败

 

Not enough memory to create instance for real server (*name*).

在用户态中创建实服务器*name*实例时内存不足

 

Failed to send real server instance to kernel.

向内核发送实服务器实例失败

 

Not enough memory to initialize sticky method in sticky group (*name*).

初始化持续性组*name*的持续性方法时内存不足

 

Failed to modify sticky group (*name1*) in real server farm (*name2*) instance to kernel.

修改实服务组*name2*实例中的持续性组*name1*下发内核失败

 

Failed to delete sticky group (*name*) instance from kernel.

从内核删除持续性组*name*实例失败

 

Failed to create instance for sticky group (*name*).

为持续性组*name*创建实例失败

 

Not enough memory to add sticky group (*name*).

添加持续性组*name*时内存不足

 

Failed to recover DBM of sticky group (*name)*.

恢复持续性组*name*的DBM失败

 

Failed to add sticky group (*name*).

添加持续性组*name*失败

 

Not enough memory to allocate memory for sticky entries.

为持续性表项申请内存时内存不足

 

Failed to get sticky entry due to improper sticky group configuration.

由于持续性组的配置原因，导致获取持续性表项失败

 

Not enough memory to add sticky group to kernel.

向内核添加持续性组时内存不足

 

Failed to get real server by sticky entry.

根据持续性表项查找实服务器失败

 

Failed to get valid real server by sticky entry.

根据持续性表项查找可用的实服务器失败

 

Not enough memory to generate sticky entries.

生成持续性表项时内存不足

 

Failed to add policy due to *reason*.

由于*reason*，导致添加策略数据失败。*reason*包括：

·insufficient memory in kernel：内核中内存不足

·ID conflict in kernel：内核中编号冲突

 

Failed to add rule node for policy *policy* due to *reason*.

由于*reason*，导致策略*policy*添加规则节点失败。*reason*包括：

·failure to instantiate action *action*：动作*action*实例化失败

·insufficient memory：内存不足

 

Failed to modify policy *policy* to kernel.

在内核中修改策略*policy*数据失败

 

Failed to add policy *policy* due to insufficient memory.

由于内存不足，导致添加策略*policy*失败

 

Failed to recover policy *policy* from DBM due to insufficient memory.

由于内存不足，导致策略*policy*从DBM中恢复失败

 

Failed to instantiate policy *policy* due to *reason*.

由于*reason*，导致策略*policy*实例化失败。*reason*包括：

·insufficient memory：内存不足

·invalid ID：编号无效

 

Failed to add policy *policy* to kernel.

向内核添加策略*policy*失败

 

Not enough memory to create class *class*.

创建类*class*时内存不足

 

Not enough memory to add match rule of the class.

为类添加匹配规则时内存不足

 

Failed to add match rule of the class to kernel.

向内核添加类的匹配规则失败

 

Failed to add class (*class*) to kernel.

向内核添加类*class*失败

 

Failed to add class to kernel.

向内核添加类失败

 

Failed to delete class (*class*) from kernel.

从内核删除类*class*失败

 

Failed to write class (*class*) to DBM.

写类*class*到DBM失败

 

Not enough memory to add action (*action*).

创建动作*action*时内存不足

 

Not enough memory to create action (*action*) instance.

创建动作*action*实例时内存不足

 

Failed to modify/instantiate server farm of action (*action*).

修改/实例化动作*action*引用的实服务组失败

 

Failed to reference action (*action*) sticky group.

动作*action*引用持续性组失败

 

Failed to add action (*action*) instance to kernel.

向内核添加动作*action*实例失败

 

Failed to delete action (*action*) instance from kernel.

从内核删除动作*action*实例失败

 

Failed to modify action (*action*) instance in kernel.

在内核中修改动作*action*实例失败

 

Failed to modify action (*action*) instance.

修改动作*action*实例失败

 

Failed to resume master server farm (*name*) of action (*action*).

恢复动作*action*引用的主用实服务组为在线实服务组失败

 

Failed to switch backup server farm (*action*) of action (*action*).

切换动作*action*引用的备份实服务组为在线实服务组失败

 

Failed to write action (*action*) to DBM.

写动作*action*到DBM失败

 

Failed to add parameter profile (*profile*).

添加参数模板*profile*失败

 

Failed to delete the parameter profile (*profile*) from kernel.

从内核删除参数模板*profile*失败

 

Failed to modify the parameter profile (*profile*).

修改参数模板*profile*失败

 

Failed to reference parameter profile (*profile*) by virtual server (*name*).

虚服务器*name*引用参数模板*profile*失败

 

Failed to cancel the reference of parameter profile by virtual server (*name*).

虚服务器*name*解除引用参数模板*profile*失败

 

Failed to add SNAT pool (*name*) instance.

添加SNAT地址池*name*实例失败

 

Failed to add new SNAT pool (*name*).

添加新的SNAT地址池*name*失败

 

SNAT pool (*name*) does not exist.

SNAT地址池*name*不存在

 

Failed to delete/modify SNAT pool (*name*) instance.

删除/修改SNAT地址池*name*实例失败

 

Pro=*protocol*, Src=*sip*/*sport*, Dst=*dip*/*dport*, ID=*id*

收到的报文信息，其中报文协议号为*protocol*，源IPv4/IPv6地址和端口号为*sip*/*sport*，目的IPv4/IPv6地址和端口号为*dip*/*dport*，编号为*id*

 

Failed to process first/subsequent packet with NAT disabled.

NAT未使能时处理首个/后续报文失败

 

Not enough memory to create control information when enabling SNAT.

SNAT使能时，由于内存耗尽而无法创建控制信息

 

Failed to process first packet with SNAT enabled.

SNAT使能时处理首报文失败

 

Failed to disconnect the TCP connection to the client.

实服务器故障且选择断开连接方式处理故障时，由于发送报文失败而未与客户端断开TCP连接

 

Failed to start NQA job *job* of real server *name* by IPv4/IPv6.

实服务器*name*开启IPv4/IPv6健康检测*job*失败

 

Failed to stop NQA job (handle: *num*) of real server *name*.

实服务器*name*停止健康检测*job*失败

 

Failed to refresh start NQA job *job* of real server *name* by IPv4/IPv6.

实服务器*name*刷新开启IPv4/IPv6健康检测*job*失败

 

Failed to add action SSL rewrite data.

添加SSL重写数据的动作失败

 

Failed to modify action (*name*) instance.

修改动作*name*实例失败

 

Failed to modify server farm of action (*name*).

修改动作*name*的实服务组配置失败

 

Failed to delete match rule of the class from kernel.

从内核中删除类匹配规则失败

 

Failed to add policy due to insufficient memory in kernel.

由于内核中内存不足，导致添加策略失败

 

Failed to add policy due to ID conflict in kernel.

由于内核中编号冲突，导致添加策略失败

 

Not enough memory to create *info* information.

由于内存不足，导致创建*info*信息失败。*info*包括：

·session control：会话扩展

·UDP per-packet control：UDP强制负载均衡扩展

·sticky control：持续性扩展

 

Failed to accept SSL server connection *id*.

与服务器端确立建立编号为*id*的SSL连接失败

 

Failed to distribute packet: *packet*.

上送报文*packet*失败

 

Transaction *id* failed to receive request: Return value=*value*, Event=User-Input/Server-Output.

编号为*id*的事务接收请求失败，返回值*value*，事件为User-Input/Server-Output

 

Transaction *id* failed to receive response: Return value=*value*, Event=User-Output/Server-Input.

编号为*id*的事务接收应答失败，返回值*value*，事件为User-Output/Server-Input

 

Transaction *id*: Direction=Request/Response, Parse result=Failed, Parse length=*length*.

编号为*id*的事务，方向为请求/应答方向，解析结果为失败，解析长度为*length*

 

Transaction *id* binding failed.

编号为*id*的事务绑定失败

 

Transaction *id* failed to be connected to the real server.

编号为*id*的事务连接实服务器失败

 

The real server selected by Transaction *id* doesn't existed.

编号为*id*的事务所选择的实服务器不存在

 

The real server selected by Transaction *id* was invalid.

编号为*id*的事务所选择的实服务器不可用

 

Transaction *id* failed to re-create send-request queue.

编号为*id*的事务重新创建发送队列失败

 

Failed to merge *length* data to one data information.

长度为*length*的数据信息合并失败

 

Failed to combine *length1* data with the previous *length2* data.

将当前数据（长度为*length1*）与之前数据（长度为*length2*）合并失败

 

Failed to create SSL server connection *connection* .

与服务器建立SSL连接失败（连接信息为*connection*）

 

Local=*address1*/*port1,* Peer=*address2*/*port2*

建立的连接信息，源IP为*address1*，源端口为*port1*，目的IP为*address2*，目的端口为*port2*

 

Transaction *id* failed to create a handle for connecting the real server.

编号为*id*的事务创建连接实服务器的句柄失败

 

Virtual server *name* failed to create handle.

虚服务*name*创建句柄失败

 

Virtual server *name* failed to bind handle.

虚服务*name*绑定句柄失败

 

Virtual server *name* failed to listen to handle.

虚服务*name*监听句柄失败

 

Virtual server *name* failed to accept a new handle.

虚服务*name*接收新句柄失败

 

Virtual server *name* failed to create a new SSL connection.

虚服务*name*创建新的SSL连接失败

 

Not enough memory to create session tack information.

内存不足导致创建会话附加信息失败

 

Not enough memory to create session sticky information.

内存不足导致创建会话持续性信息失败

 

Failed to search FIB information: *packet*.

查找FIB信息失败，报文信息为*packet*

 

Failed to create a TCP SYN packet: *packet*.

创建TCP SYN报文失败，报文信息为*packet*

 

Dropped an error packet TCP ACK from client: *packet*.

丢弃客户端回的TCP ACK错误报文，报文信息为*packet*

 

Failed to create a TCP RST packet: *connection*.

创建TCP RST报文失败，报文信息为*packet*

 

Failed to process first packet when SNAT was enabled: *packet*.

SNAT使能时处理首报文失败，报文信息为*packet*

 

Failed to select real server according to predictor: *packet*.

根据调度算法选择实服务器失败，报文信息为*packet*

 

Failed to send the data of SSL policy *SSLPolicy*, error code *errorcode*, total length *totallen*, sent length *sentlen*, sending length *sendinglen*.

发送SSL策略*SSLPolicy*的数据失败，错误码为*errorcode*，总数据长度为*totallen*，已发送数据长度为*sentlen*，本次发送数据长度为*sendinglen*

 

Failed to create the data of SSL policy *SSLPolicy*.

创建SSL策略*SSLPolicy*的数据失败

 

Failed to create SSL policy *SSLPolicy* context.

创建SSL策略*SSLPolicy*的上下文失败

 

Failed to sync instance (type: *type*).

类型为*type*的实例化信息同步失败。*type*包括：

·0：添加虚服务器

·1：删除虚服务器

·2：修改虚服务器

·3：添加实服务组

·4：删除实服务组

·5：修改虚服务器

·6：添加实服务器

·7：删除实服务器

·8：修改虚服务器

·9：设置debug开关

·10：虚服务器统计

·11：实服务器统计

·12：添加持续性组

·13：删除持续性组

·14：修改持续性组

·15：添加类

·16：删除类

·17：添加匹配规则

·18：删除匹配规则

·19：添加动作

·20：删除动作

·21：修改动作

·22：添加参数

·23：删除参数

·24：修改参数

·25：添加策略

·26：删除策略

·27：修改策略

·28：添加SNAT

 

·29：删除SNAT

·30：修改SNAT

·31：平滑参数

·32：平滑策略

·33：平滑持续性组

·34：平滑类

·35：平滑SNAT

·36：平滑动作

·37：平滑实服务组

·38：平滑实服务器

·39：平滑虚服务器

·40：策略下的规则

·41：动作下的规则

·42：实服务组统计信息

 

表1-2 debugging lb event命令输出信息描述表

字段

描述

Not enough memory resource.

内存资源不足

 

Memory resource is restored.

内存资源恢复

 

Received NQA notify health *job* *result* of real server *name* by IPv4/IPv6.

收到实服务器*name*下的IPv4/IPv6健康检测*job*通知的结果*result*。*result*包括：

·failed：失败

·invalid：非法

·succeeded：成功

 

Succeeded in starting NQA job *job* (handle: *num*) of real server *name* by IPv4/IPv6.

开启实服务器*name*下的IPv4/IPv6健康检测*job*成功

 

Add the start NQA job *job* of real server *name* to refresh list by IPv4/IPv6.

将开启实服务器*name*下的IPv4/IPv6健康检测*job*添加到重刷链中

 

Stop the NQA job (handle: *num*) of real server *name*.

停止实服务器*name*下的健康检测

 

Succeeded in refreshing start NQA job *job* (handle: *num*) of real server *name* by IPv4/IPv6.

成功刷新开启实服务器*name*下IPv4/IPv6健康检测

 

LB started in slot *slotid*.

负载均衡特性在槽位*slotid*上启动

 

Connection  *connection*  state is changed to idle.

连接*connection*的状态变为空闲状态

 

Transaction *id* received request successfully: Event=User-Input.

编号为*id*的事务接收请求数据成功，事件为User-Input

 

Transaction *id* received response successfully: Event=User-Output.

编号为*id*的事务接收应答数据成功，事件为User-Output

 

Transaction *id*: Event=*event*.

编号为*id*的事务，事件为*event*。*event*包括：

·User-Age：用户超时

·User-Error：用户错误

·Server-OutPut：服务器输出

·Server-Age：服务器超时

·Server-Error：服务器错误

 

Transaction *id* received response data successfully: Event=Server-Input.

编号为*id*的事务接收应答数据成功，事件为Server-Input

 

Transaction *id* got an idle connection successfully.

编号为*id*的事务获取空闲连接成功

 

Transaction *id* created a new connection *connection* successfully.

编号为*id*的事务创建连接*connection*成功

 

Transaction *id* selected real server ID: *id* by predictor.

编号为*id*的事务根据调度算法选择编号为*id*的实服务器成功

 

Transaction *id* selected real server in *state* state by sticky.

编号为*id*的事务根据持续性选择的实服务器状态为*state*。*state*包括：

·OK：实服务器可用

·OVERLOAD：实服务器超载

 

Transaction *id* used the previous real server.

编号为*id*的事务使用上次的实服务器

 

Transaction *id* forwarding method is *type*.

编号为*id*的事务转发方法为*type*。*type*包括：

·None：默认

·Drop：丢包

·Forward：转发

·Server-farm：由实服务组处理

·Unknown：未知

 

Transaction *id* needs to select another real server.

编号为*id*的事务需要重新选择一个实服务器

 

Transaction *id* needs to send redirect response.

编号为*id*的事务需要发送重定向报文

 

Transaction *id* has been deleted.

编号为*id*的事务已被删除

 

Transaction *id* sent request/response successfully *connection*.

编号为*id*的事务发送请求/应答成功，连接信息为*connection*

 

Virtual server *name* created a new transaction *id*: *connection*.

虚服务*name*成功创建一个编号为*id*的事务，连接信息为*connection*

 

SSL client connection *connection* accepted successfully.

接收SSL客户端连接*connection*成功

 

Virtual server *name* created a new SSL connection.

虚服务*name*创建了一个SSL连接

 

SSL server connection  *connection*  established successfully.

与SSL服务器端建立连接*connection*成功

 

SSL client/server connection  *connection*  was not ready.

SSL客户端/服务器端连接*connection*尚未就绪

 

Local=*address1*/*port1,* Peer=*address2*/*port2*

建立的连接信息，源IP为*address1*，源端口为*port1*，目的IP为*address2*，目的端口为*port2*

 

Succeed to receive the data of ssl policy *SSLpolicy*, total length *totallen*, received length *recevlen*, receiving length *receivinglen*.

接收SSL策略*SSLpolicy*的数据成功，总长度*totallen*，已接收数据长度*recevlen*，本次接收数据长度*receivinglen*

 

Succeeded to create the data of SSL policy *SSLpolicy*, total length *totallen*.

创建SSL策略*SSLpolicy*的数据成功，总长度为*totallen*

 

表1-3 debugging lb fsm命令输出信息描述表

字段

描述

Transaction *id*: State=*state1* -\> *state2*, Direction=Request/Response.

在请求/应答方向上，编号为*id*的事务状态由*state1*迁移到*state2*。*state*包括：

·WAITING：等待状态

·CONNECTING：连接状态

·TRANSMITTING：转发状态

·FINISH：应答数据接收完成状态

 

Transaction *id* reset: State=*state* -\> WAITING.

重置编号为*id*的事务，其状态由*state*迁移到WAITING。*state*包括：

·WAITING：等待状态

·CONNECTING：连接状态

·TRANSMITTING：转发状态

·FINISH：应答数据接收完成状态

 

表1-4 debugging lb packet命令输出信息描述表

字段

描述

Pro=*protocol*, Src=*sip*/*sport*, Dst=*dip*/*dport*, ID=*id*

收到的报文信息，其中报文协议号为*protocol*，源IPv4/IPv6地址和端口号为*sip*/*sport*，目的IPv4/IPv6地址和端口号为*dip*/*dport*，编号为*id*

 

Input packet matched virtual server *name*

收到匹配虚服务器*name*的报文

 

Server farm/Forwarding/Dropping is selected according to default server farm/policy

根据虚服务器配置的缺省实服务组/策略来选择实服务组/转发/丢弃

 

Real server *name* is selected according to sticky method

根据持续性方式获取实服务器*name*

 

Real server *name* is selected according to predictor

根据调度算法获取实服务器*name*

 

Succeeded in processing first/subsequent packet with NAT/SNAT enabled: *packet*.

NAT/SNAT使能时首个/后续报文处理成功，报文信息为*packet*

 

Succeeded in processing first/subsequent packet with NAT disabled: *packet*.

NAT未使能时首个/后续报文处理成功，报文信息为*packet*

 

Succeeded in processing reverse packet with NAT/SNAT enabled: *packet*.

NAT/SNAT使能时反向报文处理成功，报文信息为*packet*

 

Virtual/Real server (*name*) is not available now.

虚/实服务器*name*当前不可用或已失效

 

Session conflict, try to use source port *port*.

由于会话冲突，尝试选择源端口*port*

 

Session conflict, try to use ID *id*.

由于会话冲突，尝试选择编号*id*

 

TTL or hop limit of the packet expires.

报文中的TTL或Hop Limit值超时

 

Real server *(name)* is in fault, use KEEP/RESCHEDULE/RESET processing.

实服务器*name*故障，使用保持已有连接/重定向连接/断开已有连接的方式处理报文

 

Real server *name1* is rescheduled while real server *name2* is in fault.

实服务器*name2*故障，实服务器*name1*被重定向连接

 

Can't find any other real server to reschedule while real server *name* is in fault.

实服务器*name*故障，无法找到其它实服务器参与重定向连接

 

The UDP/TCP/ICMP connection to the client was disconnected.

某实服务器故障，且选择断开连接方式处理故障，与客户端的UDP/TCP/ICMP连接被断开

 

The received packet exceeded MSS, dropped it.

收到的报文超出了TCP MSS，将其丢弃

 

Real server *name* is *state* according to *method*: *packet*.

根据*method*找到的实服务器*name*的状态为*state*，报文信息为*packet*。

*[state*]包括：

·selected：可用

·overload：超载

·not found：未找到

*[method*]包括：

·sticky method：持续性方法

·predictor：调度算法

 

Real server is *state* according to *method*: *packet*.

根据*method*找到的实服务器的状态为*state*，报文信息为*packet*。

*[state*]包括：

·selected：可用

·overload：超载

·not found：未找到

*[method*]包括：

·sticky method：持续性方法

·predictor：调度算法

 

Server farm is not found according to *type*: *packet*.

根据类型*type*未找到实服务组，报文信息为*packet*。*type*包括：

·default server farm：默认实服务组

·policy：策略

 

Server farm is selected according to *type*: *packet*.

根据类型*type*找到实服务组，报文信息为*packet*。*type*包括：

·default server farm：默认实服务组

·policy：策略

 

Server farm is changed by *type*: *packet*.

根据类型*type*找到实服务组已经改变，报文信息为*packet*。*type*包括：

·default server farm：默认实服务组

·policy：策略

 

Inserted a cookie *cookie* with length *length*: *timeout*: *insert-length*: *packet*.

插入一个cookie，字符内容为*cookie*，字符长度为*length*，超时长度为*timeout*，插入长度为*insert-length*，报文信息为*packet*

 

Sent a packet TCP SYN/TCP RST/HTTP to real server *name*, result *result*: *packet*.

发送一个TCP SYN/TCP RST/HTTP报文到实服务器*name*，结果为*result*，报文信息为*packet*

 

Sent a packet HTTP to real server, result *result*: *packet*.

发送一个HTTP报文到实服务器，结果为*result*，报文信息为*packet*

 

Received a packet TCP SYN from client and sent a packet SYN ACK to client: *packet*.

从客户端收到一个TCP SYN报文，并回一个SYN ACK报文给客户端，报文信息为*packet*

 

Successfully created a packet TCP SYN/TCP RST: *packet*.

创建TCP SYN/TCP RST报文成功，报文信息为*packet*

 

Received a packet TCP ACK from client: *packet*.

从客户端收到一个TCP ACK报文，报文信息为*packet*

 

Received a packet HTTP from client: *packet*.

从客户端收到一个HTTP报文，报文信息为*packet*

 

Received a duplicate packet HTTP form client: *packet*.

从客户端收到一个重复的HTTP报文，报文信息为*packet*

 

Received a packet TCP from real server: *packet*.

从实服务器收到一个TCP报文，报文信息为*packet*

 

Received a packet SYN ACK from real server: *packet*.

从实服务器收到一个SYN ACK报文，报文信息为*packet*

 

Rewrote a cookie *value* with length *length*: *packet*.

重写了一个值为*value*、长度为*length*的cookie，报文信息为*packet*

 

Inserted a header *name*: *value*: *packet*

插入了一个名为*name*、值为*value*的头部，报文信息为*packet*

 

Input packet matched virtual server *name*: *packet*.

输入报文匹配上虚服务*name*，报文信息为*packet*

 

Transaction *id*: Direction=Request/Response, State=*state1* -\> *state2*, Parse Length=*length*.

在请求/应答方向上，编号为*id*的事务解析状态由*state1*迁移到*state2*，解析长度为*length*。*state*包括：

·Request_line：请求行

·Headers：报文头部

·Body：报文体

·Chunked：报文体为Chunked

·Done：解析完成

 

【举例】

\# 打开负载均衡错误调试信息开关。

\<Sysname\> debugging lb error

\*Aug 29 00:09:45:746 2012 Sysname LB/7/ERROR: -MDC=1; Failed to process first packet with NAT disabled: Pro=6, Src=2.2.2.1/0, Dst=2.2.2.2/0, ID=10850.

*[// NAT*]*未使能时处理首报文失败：报文协议号为6，源IPv4地址和端口号为2.2.2.1/0，目的IPv4地址和端口号为2.2.2.2/0，编号为10850*

\# 打开负载均衡事件调试信息开关。

\<Sysname\> debugging lb event

\*Aug 29 00:13:58:003 2012 Sysname LB/7/EVENT: -MDC=1; Received NQA notify health n failed of real server rs by IPv4.

*// 收到实服务器rs下的IPv4健康检测n通知的失败结果*

\# 打开负载均衡状态机调试信息开关。

\<Sysname\> debugging lb fsm

\*Jan 18 03:24:59:671 2014 Sysname LB/7/FSM: -MDC=1; Transaction [6: State=CONNECTING -\> TRANSMITTING, Direction=Request.]

*// 在请求方向上，编号为6的事务的状态由CONNECTING迁移到TRANSMITTING*

\# 打开负载均衡报文调试信息开关。

\<Sysname\> debugging lb packet

\*Aug 29 00:09:45:746 2012 Sysname LB/7/PACKET: -MDC=1; Input packet matched virtual server vs: Pro=6, Src=2.2.2.1/0, Dst=2.2.2.2/0, ID=10850.

*// 收到匹配虚服务器vs的报文：报文协议号为6，源IPv4地址和端口号为2.2.2.1/0，目的IPv4地址和端口号为2.2.2.2/0，编号为10850*

\*Aug 29 00:09:45:746 2012 Sysname LB/7/PACKET: -MDC=1; Server farm is selected according to default server farm: Pro=6, Src=2.2.2.1/0, Dst=2.2.2.2/0, ID=10850.

*// 根据虚服务器配置的缺省实服务组来选择实服务组：报文协议号为6，源IP地址和端口号为2.2.2.1/0，目的IP地址和端口号为2.2.2.2/0，编号为10850*

\*Aug 29 00:09:45:746 2012 Sysname LB/7/PACKET: -MDC=1; Real server rs is selected according to predictor: Pro=6, Src=2.2.2.1/0, Dst=2.2.2.2/0, ID=10850.

*// 根据调度算法获取实服务器rs：报文协议号为6，源IPv4地址和端口号为2.2.2.1/0，目的IPv4地址和端口号为2.2.2.2/0，编号为10850*
