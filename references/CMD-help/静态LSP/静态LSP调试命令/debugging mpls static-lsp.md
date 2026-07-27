<!-- CMD-INDEX
  debugging mpls static-lsp           | 用户视图             | L5
-->

**静态LSP \-- 静态LSP调试命令 \-- debugging mpls static-lsp**

------------------------------------------------------------------------

【命令】

**[debugging mpls static-lsp **[{ **all** \| **error** \| **event** \| **process** }]]

**[undo debugging mpls static-lsp**[ { **all** \| **error** \| **event** \| **process** }]]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

**[all**]：表示静态LSP的所有调试信息开关。

**[error**]：表示静态LSP的错误调试信息开关。

**[event**]：表示静态LSP的事件调试信息开关。

**[process**]：表示静态LSP创建和删除过程调试信息开关。

【描述】

**[debugging mpls static-lsp**]命令用来打开静态LSP的调试信息开关。**undo debugging mpls static-lsp**命令用来关闭静态LSP的调试信息开关。

缺省情况下，静态LSP调试信息开关处于关闭状态。

表1-1 debugging mpls static-lsp error命令输出信息描述表

字段

描述

Failed to process a configuration command.

处理配置命令失败

Failed to activate a static LSP on the ingress.

在Ingress上激活静态LSP失败

表1-2 debugging mpls static-lsp event命令输出信息描述表

字段

描述

*[Module-A* created a connection to *Module-B*.]

*[Module-A*]模块与*Module-B*建立一个连接

Received a message from LSM: The MPLS enable state changed on an interface.

从LSM接收到接口上MPLS使能状态变化事件

Received an HA upgrade event.

收到HA升级事件

Received an HA degrade event.

收到HA降级事件

表1-3 debugging mpls static-lsp process命令输出信息描述表

字段

描述

Activated the static LSP (*lsp-destination*/*destination-mask*).

激活一条静态LSP，LSP的目的地址为*lsp-destination*，目的地址掩码为*destination-mask*

Deactivated the static LSP (*lsp-destination*/*destination-mask*).

去激活一条静态LSP，LSP的目的地址为*lsp-destination*，目的地址掩码为*destination-mask*

Added the label of the static LSP (*lsp-destination*/*destination-mask*, next hop count: *count-num*) to the corresponding routes.

将静态LSP（FEC的目的地址为*lsp-destination*，目的地址掩码为*destination-mask*）的标签添加到对应的路由表项中，静态LSP的下一跳数目为*count-num*

【举例】

\# 打开静态LSP的错误调试信息开关。在设备上配置一条本节点作为Egress节点的静态LSP，该LSP使用的标签已经被其他的LSP使用。

\<Sysname\> debugging mpls static-lsp error

\<Sysname\> system-view

Sysname static-lsp egress test2 in-label 100

Sysname

\*May 21 16:12:57:279 2011 Sysname SLSP/7/ERROR: -MDC=1; Failed to process a configuration command.

*// 处理命令失败。*

\# 打开静态LSP事件调试信息开关。在设备上配置一条本节点作为Ingress节点的静态LSP，设备上存在该LSP下一跳地址对应的激活路由。在该静态LSP对应的出接口上关闭MPLS能力，设备上会打印如下信息。

\<Sysname\> debugging mpls static-lsp event

\<Sysname\> system-view

Sysname static-lsp ingress test1 destination 100.100.100.2 32 nexthop 172.168.1.2 out-label 30

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo mpls enable

Sysname-GigabitEthernet1/0/1

\*Jun 22 17:09:18:012 2011 Sysname SLSP/7/EVENT: -MDC=1; Received a message from LSM:

The MPLS enable state changed on an interface.

*// 从LSM接收到接口上MPLS使能状态变化事件。*

\# 打开静态LSP创建和删除过程调试信息开关。在设备上删除一条本节点作为Ingress节点的静态LSP时，打印如下信息。

\<Sysname\> debugging mpls static-lsp process

\<Sysname\> system-view

Sysname undo static-lsp ingress test1

Sysname

\*Jun 22 17:21:07:821 2011 Sysname SLSP/7/PROCESS: -MDC=1; Deactivated the static LSP (100.100.100.2/32).

*// 去激活一条静态LSP。*

\*Jun 22 17:21:07:822 2011 Sysname SLSP/7/PROCESS: -MDC=1; Added the label of the static LSP (100.100.100.2/32, next hop count: 0) to the corresponding routes.

*// 将静态LSP（FEC的目的地址为100.100.100.2/32）的标签添加到对应的路由表项中，静态LSP的下一跳数目为0。*
