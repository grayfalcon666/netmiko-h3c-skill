
**静态CRLSP \-- 静态CRLSP调试命令 \-- debugging mpls static-cr-lsp management**

------------------------------------------------------------------------

【命令】

**[debugging mpls static-cr-lsp **[[ **all \| error \| event \| process** ] ]]

**[undo debugging mpls static-cr-lsp**[ [ **all \| error \| event \| process** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示静态CRLSP所有的调试信息开关。

**[error**]：表示静态CRLSP的错误调试信息开关。

**[event**]：表示静态CRLSP的事件调试信息开关。

**[process**]：表示静态CRLSP的创建、处理调试信息开关。

【描述】

**[debugging mpls static-cr-lsp**]命令用来打开静态CRLSP调试信息开关。**undo debugging mpls static-cr-lsp**命令用来关闭静态CRLSP调试信息开关。

缺省情况下，静态CRLSP调试信息开关处于关闭状态。

表1-1 debugging mpls static-cr-lsp error命令输出信息描述表

字段

描述

Failed to reply configuration.

配置处理消息回复失败

Not enough resources are available to complete the operation.

申请内存失败

Failed to process a configuration command.

处理配置失败

Failed to add the static CRLSP (*crlsp-name*) to DBM.

保存名为*crlsp-name*的静态CRLSP的配置失败

Failed to send the GR start message to LSM.

向LSM模块发送GR start消息失败

Failed to send the GR end message to LSM.

向LSM模块发送GR end消息失败

表1-2 debugging mpls te static-cr-lsp event命令输出信息描述表

字段

描述

Received an interface next hop changed event from route management.

收到路由管理下一跳变化事件

Registered to L3VPN.

向L3VPN模块注册成功

Failed to register to L3VPN.

向L3VPN模块注册失败

Failed to send a batch backup message.

发送批备消息失败

Received an HA upgrade event.

收到HA升级事件

Received an HA degrade event.

收到HA降级事件

表1-3 debugging mpls te static-cr-lsp process命令输出信息描述表

字段

描述

Status of CRLSP (name *crlsp-name*, role *role*) changed from down to up.

名为*crlsp-name**，*角色为*role*的静态CRLSP状态从down变为up。其中，*role*的取值包括ingress、transit和egress

Status of CRLSP (name *crlsp-name*, role *role*) changed from up to down.

名为*crlsp-name**，*角色为*role*的静态CRLSP状态从up变为down。其中，*role*的取值包括ingress、transit和egress

Created an LSM entry for the static CRLSP: name *crlsp-name*, role *role*, in label *in-label*, out label *out-label*, out interface index *out-interface-index*.

向LSM创建静态CRLSP成功，静态CRLSP的名称为*crlsp-name，*角色为*role*，入标签为*in-label*，出标签为*out-label*，出接口索引为*out-interface-index*的表项。其中，*role*的取值包括ingress、transit和egress

Failed to create an LSM entry for the static CRLSP: name *crlsp-name*, role *role*, in label *in-label*, out label *out-label*, out interface index *out-interface-index*.

向LSM创建静态CRLSP失败，静态CRLSP的名称为*crlsp-name，*角色为*role*，入标签为*in-label*，出标签为*out-label*，出接口索引为*out-interface-index*的表项。其中，*role*的取值包括ingress、transit和egress

【举例】

\# 设备上打开静态CRLSP错误调试信息开关。配置消息失败时，打印如下调试信息。

\<Sysname\> debugging mpls te management error

\*Mar 17 09:12:30:026 2014 Sysname SCRLSP/7/ERROR: -MDC=1; Failed to process a configuration command.

*// 处理配置失败。*

\# 设备上打开静态CRLSP事件调试信息开关。路由消息变化时，打印如下调试信息。

\<Sysname \>debugging mpls static-cr-lsp event

\*Mar 17 09:07:56:064 2014 Sysname SCRLSP/7/EVENT: -MDC=1; Received an interface next hop changed event from route management.

*// 收到路由管理的路由变化通知消息。*

\# 设备上打开静态CRLSP处理过程调试信息开关。Egress LSP隧道创建时，打印如下调试信息。

\<Sysname \>debugging mpls static-cr-lsp process

\*Mar 17 09:05:21:898 2014 Sysname SCRLSP/7/PROCESS: -MDC=1; Status of CRLSP (name egress1; role egress) changed from down to up.

*// 静态CRLSP名为egress1，角色为role为egress的状态从down变化为up。*

\*Mar 17 09:05:21:898 2014 Sysname SCRLSP/7/PROCESS: -MDC=1; Created an LSM entry for the static CRLSP: name egress1; role egress; in label 100; out label 4294967295; out interface index 0.

*// 向LSM创建静态CRLSP成功，静态CRLSP名为egress1，角色为role为egress，入标签为100，出标签为无效（4294967295），出接口索引为无效值（0）的表项。*
