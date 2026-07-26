
**SNMP \-- SNMP调试命令 \-- debugging snmp agent packet**

------------------------------------------------------------------------

【命令】

**[debugging snmp agent**[ **packet** { **header** \| **receive** \| **send** }]]

**[undo debugging snmp agent packet**[ { **header** \| **receive** \| **send** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[header**]：表示SNMP Agent数据包消息头调试信息开关。向信息中心输出SNMP请求报文头的版本、团体名或用户名等信息。

**[receive**]：表示接收到的SNMP数据包调试信息开关。向信息中心输出Agent接收到的SNMP请求报文的类型、request-id、error-status、error-index和绑定节点列表等信息。

**[send**]：表示发送的SNMP数据包调试信息开关。向信息中心输出Agent发送的SNMP响应消息的类型、request-id、error-status、error-index和绑定节点列表等信息。

【描述】

**[debugging snmp agent** **packet**]命令用来打开SNMP消息报文内容的调试开关。**undo debugging snmp agent packet**命令用来关闭SNMP消息报文内容的调试开关。

缺省情况下，SNMP消息报文内容的调试开关处于关闭状态。

表1-1 debugging snmp agent packet header命令输出信息描述表

字段

描述

Incoming *SNMP-version* packet

接收到SNMP报文

*[SNMP-version*]：SNMP版本（取值SNMPv1、SNMPv2c和SNMPv3）

Community name: *community-name*

SNMP（v1/v2c）访问团体名

Security model: v3

SNMP v3安全模型

Security level: *security-level*

SNMP v3安全级别，*security-level*取值为以下3种：

·*NoAuthNoPriv**：*无认证无加密

·*AuthNoPriv**：*有认证无加密

·*AuthPriv**：*有认证有加密

User name: *user-name*

SNMP v3用户名

SnmpEngineID: *engineID*

SNMP引擎ID

SnmpEngineBoots: *n*

SNMP引擎重启的次数

SnmpEngineTime: *n*

SNMP引擎运行的时间（单位：s）

表1-2 debugging snmp agent packet receive命令输出信息描述表

字段

描述

PACKET

报文包含的信息

PACKET_SRC

报文源地址信息

Packet received from *address* via UDP

通过UDP协议从*address*接收到的SNMP报文

*[address*]：SNMP报文的源地址

Request ID: *request-id*

SNMP请求报文的编号（用于匹配SNMP响应报文）

Error status: *error-status*

SNMP请求报文中的错误状态

Error index: *error-index*

SNMP请求报文中的错误索引

VBLIST

变量绑定对列表

Get request

SNMP get请求

Set request

SNMP set请求

Get-next request

SNMP get-next请求

Get-bulk request

SNMP get-bulk请求

Non-repeaters: *non-repeaters*

get-bulk请求操作的non-repeaters字段

Max-repetitions: *max-repetitions*

get-bulk请求操作的max-repetitions字段

表1-3 debugging snmp agent packet send命令输出信息描述表

字段

描述

PACKET

报文包含的信息

PACKET_DES

报文目的地址信息

Packet sent to *address* via UDP

通过UDP协议发送给*address*的SNMP报文

*[address*]：SNMP报文的目的地址

Request ID: *request-id*

SNMP响应报文的编号（用于匹配SNMP请求报文）

Error status: *error-status*

SNMP响应报文中的错误状态

Error index: error-index

SNMP响应报文中的错误索引

VBLIST

变量绑定对列表

Response

SNMP响应报文

【举例】

\# 在一台启动了SNMP v1功能并配置相应读写团体名的设备上打开信息中心调试开关和SNMP报文消息头调试开关，使用网管软件访问设备。

\<Sysname\> terminal debugging

\<Sysname\> terminal monitor

\<Sysname\> debugging snmp agent packet header

\*Jul 27 08:37:26:313 2007 Sysname SNMP/7/HEADER:

   Incoming SNMPv1 packet

   Community name: public

*// 设备接收到版本为v1的请求报文，团体名为public*

\# 在一台启动了SNMP v2c功能并配置相应读写团体名的设备上打开信息中心调试开关和SNMP报文消息头调试开关，使用网管软件访问设备。

\<Sysname\> terminal debugging

\<Sysname\> terminal monitor

\<Sysname\> debugging snmp agent packet header

\*Jul 27 08:37:26:313 2007 Sysname SNMP/7/HEADER:

   Incoming SNMPv2c packet

   Community name: private

*// 设备接收到版本为v2c的请求报文，团体名为private*

\# 在一台启动了SNMP v3功能并配置相应组、用户名的设备上打开信息中心调试开关和SNMP报文消息头调试开关，使用网管软件访问设备。

\<Sysname\> terminal debugging

\<Sysname\> terminal monitor

\<Sysname\> debugging snmp agent packet header

\*Jul 27 08:51:00:563 2007 Sysname SNMP/7/HEADER:

   Incoming SNMPv3 packet

   Security model: v3

   Security level: AuthNoPriv

   User name: v3user1

   SnmpEngineID: 000063A27F00000100001707

   SnmpEngineBoots: 1

   SnmpEngineTime: 54591

*// 设备接收到版本为v3的请求报文，安全模型为v3，安全级别为认证不加密，用户名为v3user1， SNMP引擎ID为000063A27F00000100001707，其重启次数为1，运行时间为54591秒*

\# 在一台启动了SNMPv2c功能并配置相应读写团体名的设备上打开信息中心调试开关和接收到的SNMP数据包调试信息开关，使用网管软件对设备上的sysUpTime.0对象进行get操作。

\<Sysname\> terminal debugging

\<Sysname\> terminal monitor

\<Sysname\> debugging snmp agent packet receive

\*Jul 27 08:58:52:594 2007 Sysname SNMP/7/PACKET_SRC:

   Packet received from 10.165.81.75 via UDP

\*Jul 27 08:58:52:594 2007 Sysname SNMP/7/PACKET:

   Get request

   Request ID: 13

   Error status: 0

   Error index: 0

\*Jul 27 08:58:52:594 2007 Sysname SNMP/7/VBLIST:

   sysUpTime.0:

*// 设备接收到来自10.165.81.75，通过UDP报文传递的SNMP请求报文，消息的操作类型为get请求，请求ID为13，错误状态为0，错误索引为0，绑定变量为sysUpTime.0。*

\# 在一台启动了SNMPv2c功能并配置相应读写团体名的设备上打开信息中心调试开关和发送的SNMP数据包调试信息开关，使用网管软件对设备上的sysUpTime.0对象进行get操作。

\<Sysname\> terminal debugging

\<Sysname\> terminal monitor

\<Sysname\> debugging snmp agent packet send

\*Jul 27 09:08:21:563 2007 Sysname SNMP/7/PACKET:

   Response

   Request ID: 16

   Error status: 0

   Error index: 0

\*Jul 27 09:08:21:563 2007 Sysname SNMP/7/VBLIST:

   sysUpTime.0: 5563114

\*Jul 27 09:08:21:563 2007 Sysname SNMP/7/PACKET_DES:

   Packet sent to 10.165.81.75 via UDP

*// 设备向IP地址为10.165.81.75的网管发送SNMP响应报文，报文类型为response，对应的请求报文ID为16，错误状态为0，错误索引为0，绑定变量为sysUpTime.0，值为5563114*。*

**SNMP \-- SNMP调试命令 \-- debugging snmp agent process**

------------------------------------------------------------------------

【命令】

**[debugging snmp agent**[ **process** { **all** \| **decode** \| **stack** \| **txrx** } [ **error** \| **info** \| **warning** ]]]

**[undo debugging snmp agent process**[ { **all** \| **decode** \| **stack** \| **txrx** } [ **error** \| **info** \| **warning** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示Agent运行时各阶段（包括**decode**、**stack**和**txrx**）的调试信息开关。

**[decode**]：表示Agent解析SNMP请求报文时的调试信息开关。

**[stack**]：表示Agent处理SNMP请求报文中PDU时的调试信息开关。

**[txrx**]：表示Agent收发SNMP消息时的调试信息开关。

**[error**]：表示调试信息等级为error的调试信息开关，输出级别为error的调试信息。该类调试信息指的是SNMP协议栈或系统运行时的错误信息。

**[info**]：表示调试信息等级为info的调试信息开关，输出级别为info的调试信息。该类调试信息指的是SNMP协议栈或系统运行时的提示信息。

**[warning**]：表示调试信息等级为warning的调试信息开关，输出级别为warning的调试信息。该类调试信息指的是SNMP协议栈或系统运行时的重要信息。

若在调试开关命令中不指定输出调试信息的等级，则输出/关闭所有等级的调试信息。

【描述】

**[debugging snmp agent process**]命令用来打开Agent的调试信息开关。**undo debugging snmp agent process**命令用来关闭Agent的调试信息开关。缺省情况下，Agent的调试信息开关都处于关闭状态。缺省情况下，Agent的调试信息开关都处于关闭状态。

表1-4 debugging snmp agent process decode命令输出信息描述表

字段

描述

DECODE_INFO

解码SNMP请求报文时调试级别为info的调试信息

DECODE_WARNING

解码SNMP请求报文时调试级别为warning的调试信息

DECODE_ERROR

解码SNMP请求报文时调试级别error的调试信息

Decode SNMP request

解码SNMP请求

Failed to parse ASN.1 data while decoding SNMP request

解析SNMP请求报文中的ASN.1数据失败

Failed to decode SNMPv3 message version (*version*)

解码SNMPv3消息版本失败

*[version*]：解析出的版本

Failed to decode SNMPv3 PDU

解码SNMPv3 PDU（protocol data unit，协议数据单元）失败

Failed to decode SNMPv1/v2c PDU

解码SNMPv1/v2c PDU失败

Failed to decode SNMP message version

解码SNMP消息版本失败

Decode SNMPv1/v2c request PDU

解码SNMPv1/v2c请求PDU

Failed to decode community and version

解码团体名和版本失败

Failed to decode PDU type, request ID, error status, and error index

解码PDU类型、请求报文ID、错误状态和错误索引失败

Failed to decode variable-bindings

解码变量绑定列表失败

Parse community and version

解析团体名和版本

Parse PDU type, request ID, error status, and error index

解析PDU类型、请求报文ID、错误状态和错误索引

Decode variable-binding

解码变量绑定对

Failed to parse value while decoding variable-binding

解码变量绑定对时解析其绑定值失败

Failed to parse OID while decoding variable-binding

解码变量绑定对时解析其绑定OID（object identifier，对象标识符）失败

Parse value in variable-binding

解析变量绑定对中的绑定值

Parse OID in variable-binding

解析变量绑定对中的绑定OID

Decode SNMP message version

解析SNMP消息版本

SNMP message version decoding failure: Invalid version.

解析出的版本无效

Decode SNMPv3 message version

解码SNMPv3消息版本

Decode SNMPv3 PDU

解码SNMPv3 PDU

Failed to parse message ID while decoding SNMPv3 PDU

解码SNMPv3 PDU时解析消息ID失败

SNMPv3 PDU decoding failure: PDU size (*max-size*)smaller than the required minimum PDU size(*min-size*).

解码SNMPv3 PDU时消息最大数据长度小于系统设定的最小值

·*max-size*：接收消息的最大数据长度

·*min-size*：系统设定的消息最小数据长度

Failed to parse message flags while decoding SNMPv3 PDU

解码SNMPv3 PDU时解析消息标志位失败

Failed to parse security model (*security-model*)

解析消息安全模型失败

*[security-model*]：安全模型值

Failed to parse authoritative engine ID

解析权威引擎ID失败

Unknown engine ID

未知的引擎ID

Failed to authenticate SNMPv3 message

认证SNMPv3消息失败

Failed to decrypt SNMPv3 message

解密SNMPv3消息失败

SNMPv3 message not in time window

SNMPv3消息不在时间窗内

Unknown security model (*security-model*)

未知的安全模型

*[security-model*]：安全模型值

SNMPv3 PDU decoding failure: Unknown PDU handler.

解码SNMPv3 PDU时解析出未知的PDU处理者

Decrypt security parameters in SNMPv3 message

解密SNMPv3消息中的安全参数

SNMPv3 message decoding failure: Wrong security level (*security-level*).

解析出错误的安全级别

*[security-level*]：安全级别值

Failed to decode security parameters

解码安全参数失败

Decode security parameters in SNMPv3 message

解码SNMPv3消息中的安全参数

Authoritative engine ID in SNMPv3 message doesn\'t match entity engine ID.

SNMPv3消息中的权威引擎ID与实体引擎ID不匹配

Failed to validate authentication protocol version

认证协议版本验证失败

SNMPv3 message decoding failure: Unsupported security level (*security-level*).

解码安全参数时解析出不支持的安全级别

*[security-level*]：安全级别值

SNMPv3 message decoding failure: Unknown username.

解码安全参数时解析出未知的用户名

SNMPv3 message decoding failure: Invalid USM parameter.

解码安全参数时解析出无效的USM（User-based Security Model，基于用户的安全模型）参数

SNMPv3 message decoding failure: Invalid authoritative engine ID.

解码安全参数时解析出无效的权威引擎ID

Failed to parse authentication parameters while decoding security parameters

解码安全参数时解析认证参数失败

Failed to parse authoritative engine uptime while decoding security parameters

解码安全参数时解析权威引擎运行时间失败

Failed to parse number of authoritative engine boots while decoding security parameters

解码安全参数时解析权威引擎启动次数失败

Failed to parse authoritative engine ID while decoding security parameters

解码安全参数时解析权威引擎ID失败

Decode scoped PDU

解码加密的PDU

Failed to parse context engineID while decoding scoped PDU

解码加密的PDU时解析上下文引擎ID失败

SNMP scoped PDU decoding failure: PDU size (*[parsed-PDU-size*]{.ItemListinTableCharChar}) larger than the required maximum PDU size (*[max-PDU-size*]{.ItemListinTableCharChar}).

解码加密的PDU时解析出的PDU大小大于系统预设的最大值

·*parsed-PDU-size**：*解析出的PDU大小

·*max-PDU-size**：*系统预设的最大PDU大小

Failed to decode variable-bindings while decoding scoped PDU

解码加密的PDU时解码变量绑定列表失败

SNMP scoped PDU decoding failure: Wrong PDU size.

解码加密的PDU时加密PDU大小有误

Failed to parse context name while decoding scoped PDU

解码加密的PDU时解析上下文名字失败

Decrypt SNMPv3 message

解密SNMPv3消息

Check time window

检查时间窗

SNMP request successfully decoded

SNMP请求报文解码成功

表1-5 debugging snmp agent process txrx命令输出信息描述表

字段

描述

TXRX_INFO

收发SNMP消息时调试级别为info的调试信息

TXRX_WARNING

收发SNMP消息时调试级别为warning的调试信息

TXRX_ERROR

收发SNMP消息时调试级别为error的调试信息

Create IPv4 socket

创建IPv4 socket

Failed to create IPv4 socket

创建IPv4 socket失败

Failed to set IPv4 socket to nonblocking while creating IPv4 socket

创建IPv4 socket时设置IPv4 socket属性为非阻塞失败

Failed to set IPv4 socket to asynchronizing while creating IPv4 socket

创建IPv4 socket时设置IPv4 socket属性为异步失败

Failed to bind IP address and port while creating IPv4 socket

创建IPv4 socket时绑定IP地址和端口号失败

Create IPv6 socket

创建IPv6 socket

Failed to create IPv6 socket

创建IPv6 socket失败

Failed to set IPv6 socket to nonblocking while creating IPv6 socket

创建IPv6 socket时设置IPv6 socket属性为非阻塞时失败

Failed to set IPv6 socket to asynchronizing while creating IPv6 socket

创建IPv6 socket时设置IPv6 socket属性为异步失败

Failed to set IPv6 socket option while creating IPv6 socket (error code: *error-code*)

创建IPv6 socket时设置IPv6 socket属性失败（该属性控制本socket使用的IP地址和端口号能否再与其他socket绑定）

*[error-code*]：错误码

Failed to bind IP address and port while creating IPv6 socket

创建IPv6 socket时绑定IP地址和端口号失败

Create socket

创建socket

Failed to create IPv4 socket while initializing socket

初始化socket时创建IPv4 socket失败

Send PDU through IPv4 socket at  *time-hour:time-minute:time-second* (PDU size: *PDU-size*)

通过IPv4 socket发送PDU并打出时间戳显示发送时间

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：{.TableTextChar}秒

·*PDU-size*：PDU大小

Failed to send PDU through IPv4 socket at *time-hour:time-minute:time-second* (error code: *error-code*)

通过IPv4 socket发送PDU失败并打出时间戳显示发送时间

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

·*error-code**：*错误码

Sending PDU through IPv6 socket failure: Invalid interface index.

通过IPv6 socket发送PDU的接口索引无效

Send PDU through IPv6 socket at  *time-hour:time-minute:time-second* (PDU size*: PDU-size*)

通过IPv6 socket发送PDU并打出时间戳显示发送时间

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

·PDU-size：PDU大小

Failed to send PDU through IPv6 socket at *time-hour:time-minute:time-second* (error code: *error-code*)

通过IPv6 socket发送PDU失败并打出时间戳显示发送时间

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

·*error-code**：*错误码

PDU sending failure: Invalid destination address.

发送PDU时目的地址无效

Failed to set IPv4 socket option while receiving PDU through IPv4 socket

通过IPv4 socket接收PDU时设置IPv4 socket属性失败（该属性控制是否能从收到的报文里解析出目的IP地址）

System is busy while receiving PDU through IPv4 socket.

通过IPv4 socket接收PDU时系统正忙

Receive PDU (*PDU-size*) when SNMP agent is disabled

接收到PDU，但是SNMP服务器没有使能

*[PDU-size*]：PDU大小

Receive PDU through IPv4 socket at *time-hour:time-minute:time-second* (PDU size: *PDU-size*)

通过IPv4 socket接收PDU并打出时间戳显示接收时间

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

·*PDU-size**：*PDU大小

Failed to receive PDU through IPv4 socket at *time-hour:time-minute:time-second*  (error code: *error-code*)

通过IPv4 socket接收PDU失败并打出时间戳显示接收时间

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

·*error-code*：错误码

Receive PDU through IPv6 socket at *time-hour:time-minute:time-second* (PDU size: *PDU-size*)

通过IPv6 socket接收PDU并打出时间戳显示接收时间

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

·*PDU-size**：*PDU大小

Failed to receive PDU through IPv6 socket at *time-hour:time-minute:time-second* (error code: *error-code*)

通过IPv6 socket接收PDU失败并打出时间戳显示接收时间

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

·*error-code*：错误码

Failed to read queue while receiving PDU

接收PDU时读队列失败

Close SNMP agent IPv4/IPv6 socket

关闭SNMP agent socket

表1-6 debugging snmp agent process stack命令输出信息描述表

字段

描述

STACK_INFO

处理SNMP请求报文中PDU时调试级别为info的调试信息

STACK_WARNING

处理SNMP请求报文中PDU时调试级别为warning的调试信息

STACK_ERROR

处理SNMP请求报文中PDU时调试级别为error的调试信息

Create MOR message for get-request and parse MOR messageMOR message for response

创建get请求报文，解析响应消息

Get-request processing failure: Invalid variable-bindings.

处理get请求时变量绑定列表无效

Get-request processing failure: No such node.

处理get请求时无此节点

Failed to create MOR message while handling get-request (node name: *node-name*, error code: *error-code*)

处理get请求时创建MOR（Managed Object Repository，配置管理对象）消息失败

·*node-name**：*节点名

·*error-code**：*错误码

Failed to send command or get response while handling get-request (node name: *node-name*, error code: *error-code*)

处理get请求时发送命令或获取响应失败

·*node-name*：节点名

·*error-code*：错误码

Create MOR message for set-request and parse MOR message for response

创建set请求报文，解析响应消息

Failed to create MOR message while handling set-request (node name: *node-name*, error code: *error-code*)

处理set请求时创建MOR消息失败

·*node-name*：节点名

·*error-code*：错误码

Failed to send command or get response while handling set-request (node name: *node-name*, error code: * error-code*)

处理set请求时发送命令或取得响应失败

·*node-name*：节点名

·*error-code*：错误码

Create MOR message for get-next-request and parse MOR message for response

创建get-next请求报文，解析响应消息

Create MOR message

创建MOR请求消息

MOR message building failure: Invalid node.

构造MOR消息时节点无效

Failed to create MOR message for leaf node *node-name* while building MOR message (error code: *err-code*)

构造MOR消息时创建叶子节点的MOR消息失败

·*node-name*：节点名

·*error-code*：错误码

Failed to append index node *node-name*'s value to MOR message while building MOR message (error code: *error-code*)

构造MOR消息时向MOR消息添加索引节点值失败

·*node-name*：节点名

·*error-code*：错误码

Failed to append column node *node-name*'s value to MOR message while building MOR message (error code: *error-code*)

构造MOR消息时向MOR消息添加列节点值失败

·*node-name*：节点名

·*error-code*：错误码

Append index node's value to MOR message

向MOR消息添加索引节点值

Failed to get index node *node-name*'s value  by OID while appending index value to MOR message (error code: *error-code*)

向MOR消息添加索引值时通过OID（object identifier，对象标识符）获取索引节点值失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to check validity of *node-name*\'s value while appending index value to MOR message (error code: *error-code*)

向MOR消息添加索引值时数据有效性检查失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to append index node *node-name*'s value to MOR message (error code: *error-code*)

向MOR消息添加索引节点值失败

·*node-name*：节点名

·*error-code**：*错误码

Append column node's value to MOR message

向MOR消息添加列节点值

Set instance *instance* in batches

以批量处理的方式设置实例

*[instance*]：实例

Set instance * instance* in batches

以批量处理的方式获取实例

*[instance*]：实例

Get *instance*'s next instance in batches

以批量处理的方式获取下一个实例

*[instance*]：实例

Failed to get *node-name*\'s brother node while appending column node's value to MOR message

向MOR消息添加列节点值时取兄弟节点失败

*[node-name*]：节点名

Instance *instance* doesn't exist while appending column node's value to MOR message

向MOR消息添加列节点值时实例不存在

*[instance*]：实例

Failed to check *node-name*\'s access permission or VACM while appending column node's value to MOR message

向MOR消息添加列节点值时访问权限或VACM（View-based Access Control Model，基于视图的访问控制模型）检查失败

*[node-name*]：节点名

Failed to check validity of *node-name*\'s value while appending column node's value to MOR message (error code: *error-code*)

向MOR消息添加列节点值时数据有效性检查失败

·*node-name*：节点名

·*err-code**：*错误码

Failed to handle index node *node-name* while appending column node's value to MOR message (error code: *error-code*)

向MOR消息添加列节点值时处理索引节点失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to append column node *node-name'*s value to MOR message (error code: *error-code*)

向MOR消息添加列节点值失败

·*node-name*：节点名

·*error-code**：*错误码

Fill variable-bindings

填充变量绑定列表

Get value from MOR message (MOR type: *MOR-type*)

从MOR消息中取值

*[MOR-type*]：MOR类型

Parse MOR message and fill variable-bindings

解析MOR响应消息，填充变量绑定列表

Failed to get *node-name*\'s MOR while parsing MOR message

解析MOR消息时取节点对应MOR失败

*[node-name*]：节点名

Failed to get *node-name*\'s value from MOR message (error code: *error-code*)

从MOR响应消息中取节点值失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to check validity of *node-name*\'s value while parsing MOR message (error code: *error-code*)

解析MOR消息时数据有效性检查失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to convert *node-name*\'s data type from MOR message (error code: *error-code*)

从MOR消息中转换数据类型失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to check validity of *node-name*\'s value while parsing MOR message (error code: *error-code*)

解析MOR消息时，数据有效性检查失败

·*node-name*：节点名

·*error-code**：*错误码

Convert data type *data-type* from MOR message

从MOR消息中转换数据类型

*[data-type*]：数据类型

Invalid node while handling get-next-request

处理get-next请求时节点无效

Failed to create MOR message while handling get-next-request (node name: *node-name*, error code: *error-code*)

处理get-next请求时创建MOR消息失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to send command or get response while handling get-next-request (node name: *node-name*, error code: *error-code*)

处理get-next请求时发送命令或取得响应失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to append column node *node-name*'s value to MOR message (error code: *error-code*)

添加列节点值至MOR消息失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to append index node *node-name*'s value to MOR message (error code: *error-code*)

向MOR消息添加索引节点值失败

·*node-name*：节点名

·*error-code**：*错误码

Failed to append column node *node-name*'s value to MOR message (error code: *error-code*)

向MOR消息添加列节点值失败

·*node-name*：节点名

·*error-code**：*错误码

MOR message processing failure: Parameter number *parameter-number* smaller than index number *index-number*.

从MOR消息中取得的参数个数小于索引个数

·*parameter-number**：*参数个数

·*index-number**：*索引个数

Failed to get value from MOR message (error code: *error-code*)

从MOR消息中取值失败

*error-code*{.ItemListinTableCharChar}*[：*]{.ItemListinTableCharChar}错误码{.ItemListinTableCharChar}

Failed to get *node-name*\'s MOR from MOR message

从MOR消息中取节点的mor失败

*node-name*{.ItemListinTableCharChar}*[：*]{.ItemListinTableCharChar}节点名{.ItemListinTableCharChar}

Failed to get *node-name*\'s value from MOR message (error code: *err-code*)

从MOR消息中取节点值失败

·*node-name*：节点名

·*error-code*：错误码

Failed to check validity of *node-name*\'s value from MOR message (error code: *error-code*)

解析MOR消息时，数据有效性检查失败

·*node-name*：节点名

·*error-code*：错误码

Failed to convert *node-name*\'s data type from MOR message (error code: *error-code*)

转换MOR消息中的数据类型失败

·*node-name*：节点名

·*error-code*：错误码

Failed to get *node-name*\'s OID from MOR message

从MOR消息中取节点的OID失败

*[node-name*]：节点名

Failed to allocate memory

内存分配失败

Create MOR message for leaf node

为叶子节点创建MOR消息

Get instance *instance*.0 in batches

批量取节点实例.0

*[instance*]：实例

Set instance *instance*.0 in batches

批量设置节点实例.0

*[instance*]：实例

Getting ASN variable failure: Unknown ASN data type *data-type*.

从ASN变量取值时ASN数据类型未知

*[data-typ*e]：数据类型

Variable-binding value converting failure: Unknown convert type *convert-type*.

转换变量绑定值时转换类型未知

*[convert-type*]：转换类型

Failed to complexly convert ASN value (error code: *error-code*)

执行ASN值复杂转换失败

*[error-code*]：错误码

Complex ASN value converting failure: Invalid node *node-name*.

执行ASN值复杂转换时节点无效

*[node-name*]：节点名

Complex ASN value converting failure: Unknown relation (*relation*) between registered node and index.

执行ASN值复杂转换时注册节点与索引的关系未知

*[relation*]：关系值

Failed to check community *community* \'s acl *acl-number*

检查团体名ACL（Access Control List，访问控制列表）失败

·*community*：团体名

·a*cl-number*：访问控制列表编号

Failed to check user *user-name*\'s acl *acl-number*

检查用户ACL失败

·*user-name*：用户名

·*acl-number*：访问控制列表编号

Failed to check group\'s acl *acl-number*

检查组ACL失败

*[acl-number*]：访问控制列表编号

Failed to check context name

上下文名字检查失败

Failed to read SNMP socket asynchronous events

读SNMP socket异步事件失败

Failed to create socket

创建socket失败

Community name is null.

团体名为空

Invalid community name *community-name*

团体名无效

*[community-name*]：团体名

Failed to check community name *community-name*\'s access right (PDU type: *pdu-type*, error code: *error-code*)

团体名访问权限检查失败

·community-name：团体名

·*pdu-type*：PDU类型

·*error-code**：*错误码

Invalid variable-bindings

变量绑定列表无效

PDU type *PDU-type* not consistent with PDU version *PDU-version*

PDU类型和PDU版本不兼容

·PDU-type：PDU类型

·*PDU-version**：*PDU版本

PDU type is *PDU-type* and PDU version is *PDU-version*.

显示PDU类型和PDU版本

·PDU-type：PDU类型

·*PDU-version**：*PDU版本

No such PDU type (*PDU-type*)

无此PDU类型

*[PDU-type*]：PDU类型

Get-next request processing failure: Invalid request.

处理get-next请求时请求无效

Failed to append necessary OID for *node-name* while processing request for get-next (error code: *error-code*)

处理get-next请求时为节点添加OID失败

·*node-name*：节点名

·*error-code*：错误码

Get *node-name*\'s next instance

取当前节点的下一个实例

*[node-name*]：节点名

Get-next request processing failure: Finding *next-node* from *[cur-node *]{.ItemListinTableCharChar}timed out (*time* ms).

处理get-next请求时从当前节点查找下一节点超时

·*time**：*时间

·*cur-node**：*当前节点名

·*next-node**：*下一个节点名

Get-next request processing failure: The table that contains *[node-name*]{.ItemListinTableCharChar} might be empty.

处理get-next请求时包含*[node-name*]{.ItemListinTableCharChar}*[节点的*]{.ItemListinTableCharChar}表可能为空

*[node-name*]：节点名

Failed to pass checking*node-name*\'s access permission while processing request for get-next

处理get-next请求时访问权限检查失败

*[node-name*]：节点名

Process request

处理请求

Invalid request

请求无效

Request processing failure: Invalid message entry.

处理请求时消息表项无效

Failed to check \'.0\' at the end of leaf node while processing request for get/set (error status: *error-status*)

处理get/set请求时叶子节点尾部'.0'字符检查失败

*[error-status*]：错误状态

Get/set request processing failure (error status: *error-status*): No index for column node.

处理get/set请求时列节点无索引

*[error-status*]：错误状态

Failed to append necessary OID while processing request for get/set (error status: *error-status*)

处理get/set请求时为节点添加OID失败

*[error-status*]：错误状态

Get/set request processing failure (error status: *error-status*): Incomplete index.

处理get/set请求时索引不完整

*[error-status*]：错误状态

Failed to check validity of index while processing request for get/set (error status: *error-status*)

处理get/set请求时索引的合法性检查失败

*[error-status*]：错误状态

Failed to process request for get/set (error status: *error-status*)

处理get/set请求失败

*[error-status*]：错误状态

PDU type is *PDU-type*, PDU version is *PDU-version*, non-repeaters is *non-repeaters*, max-repetitions is *max-repetitions*.

显示PDU类型和get-bulk参数

·*PDU-type**：*PDU类型

·*PDU-version**：*PDU版本

·*non-repeaters**：*get-bulk操作参数

·*max-repetitions**：*get-bulk操作参数

PDU type is *PDU-type*, non-repeaters is 0, max-repetitions is 0.

显示PDU类型，参数N为0，参数M为0

*[PDU-type*]：PDU类型

Request processing failure: Invalid message table.

处理请求时消息表无效

Request processing failure: Non leaf or column node (node name: *node-name*, node type: *node-type*).

非叶子节点或列节点

·*node-name**：*节点名

·*node-type**：*节点类型

Request processing failure: No node can pass VACM chek.

处理请求时无节点可通过VACM检查

Request processing failure: No index memory space.

处理请求时无索引的存储空间

Failed to check VACM (error code: *error-code*)

VACM检查失败

*[error-code*]：错误码

Processing error (error status: *error-status*, error index: *error-index*)

错误处理

·*error-status**：*错误状态

·*error-index**：*错误索引

Read request

读请求

Request reading failure: Invalid PDU version (*PDU-version*).

读请求时PDU版本无效

*PDU-version*{.ItemListinTableCharChar}*[：*PDU]{.ItemListinTableCharChar}版本{.ItemListinTableCharChar}

Failed to add new entry to global message table while reading request

读请求时在全局消息列表中增加一行失败

Failed to decode SNMP request while reading request (error code: *error-code*)

读请求时解码SNMP请求报文失败

*error-code*{.ItemListinTableCharChar}*[：*]{.ItemListinTableCharChar}错误码{.ItemListinTableCharChar}

Make request

构造请求

Failed to update request (node name: *node-name*)

更新请求失败

*node-name*{.ItemListinTableCharChar}*[：*]{.ItemListinTableCharChar}节点名{.ItemListinTableCharChar}

Send response to NMS (error status: *error-status*, error index: *error-index*)

向网管发送响应报文

·*error-status**：*错误状态

·*error-index**[：*]{.ItemListinTableCharChar}错误索引{.ItemListinTableCharChar}

Response sending failure: PDU size (*PDU-size*) greater than max PDU size (*max-PDU-size*).

发送响应时PDU超大

·*PDU-size*：当前PDU的大小

·*max-PDU-size*：系统PDU的最大值

Response sending failure: PDU size (*PDU-size*) greater than max PDU size (*max-PDU-size*) or SNMPv3 max PDU size (*v3- max-PDU-size)*.

发送响应时PDU超大

·*PDU-size**：*当前PDU的大小

·*max-PDU-size**：*系统PDU的最大值

·{.ItemListinTableCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCha1}*v3- max-PDU-size**：*SNMPv3版本PDU最大值

Failed to allocate memory while sending response

发送响应时申请空间失败

Failed to execute set operation in reserve 1 (error status: *error-status*, error index: *error-index*)

执行set原子操作reserve 1失败（set操作细分为多个处理步骤，每个步骤会对应一个原子操作）

·*error-status*：错误状态

·*error-index**：*错误索引

Failed to execute set operation in reserve 2 (error status: *[err*]{.ItemListinTableCharChar}*or-s**[tatus*]{.ItemListinTableCharChar}, error index: *error-index*)

执行set原子操作reserve 2失败

·*error-status**：*错误状态

·*error-index**：*错误索引

Failed to execute set operation in action (error status: *[err*]{.ItemListinTableCharChar}*or-s**[tatus*]{.ItemListinTableCharChar}, error index: *error-index*)

执行set原子操作action失败

·*error-status**：*错误状态

·*error-index**：*错误索引

Failed to execute set operation in commit (error status: *[err*]{.ItemListinTableCharChar}*or-s**[tatus*]{.ItemListinTableCharChar}, error index: *error-index*)

执行set原子操作commit失败

·*error-status**：*错误状态

·*error-index**：*错误索引

Failed to execute set operation in undo (error status: *[err*]{.ItemListinTableCharChar}*or-s**[tatus*]{.ItemListinTableCharChar}, error index: *error-index*)

执行set原子操作undo失败

·*error-status**：*错误状态

·*error-index**：*错误索引

Failed to execute set operation in free (error status: *[err*]{.ItemListinTableCharChar}*or-s**[tatus*]{.ItemListinTableCharChar}, error index: *error-index*)

执行set原子操作free失败

·*error-status**：*错误状态

·*error-index**：*错误索引

Send report message to NMS

向网管发送报文信息

【举例】

\# 在一台启动了SNMPv2c功能并配置相应读写团体名的设备上打开信息中心调试开关和SNMP处理请求报文PDU级别为info的调试开关，使用网管软件对设备上的sysUpTime对象进行get操作。

\<Sysname\> terminal debugging

\<Sysname\> terminal monitor

\<Sysname\> debugging snmp agent process stack info

\<Sysname\>

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Read request

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   PDU type is 160 and PDU version is 1.

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Make request

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Process request

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Get instance sysUpTime.0

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Create MOR message for get-request and parse MOR message for response

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Create MOR message

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Create MOR message for leaf node

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Get instance sysUpTime.0 in batches

\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:

   Parse MOR message and fill variable-bindings

\*Jul 27 09:42:13:594 2007 Sysname SNMP/7/STACK_INFO:

   Get value from MOR message (MOR type: 3)

\*Jul 27 09:42:13:594 2007 Sysname SNMP/7/STACK_INFO:

   Convert data type 43 from MOR message

\*Jul 27 09:42:13:594 2007 Sysname SNMP/7/STACK_INFO:

   Fill variable-bindings

\*Jul 27 09:42:13:594 2007 Sysname SNMP/7/STACK_INFO:

   Send response to NMS (error status: 0, error index: 0)

*// 设备处理SNMP请求报文PDU并生成响应消息过程的info级调试信息*

**SNMP \-- SNMP调试命令 \-- debugging snmp trap packet**

------------------------------------------------------------------------

【命令】

**[debugging snmp trap packet**]

**[undo debugging snmp trap** **packet**]

【缺省情况】

SNMP 告警调试信息开关处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging snmp trap packet**]命令用来打开告警报文的调试开关。**undo debugging snmp trap packet**命令用来关闭告警报文的调试开关。缺省情况下，SNMP告警调试信息开关处于关闭状态。

表1-7 debugging snmp trap packet命令输出信息描述表

字段

描述

TRAP_PACKET

告警报文调试信息

*[trap-name* *version* send to: *address*]

系统发送trap-name 告警到address

·*trap-name*：告警报文的名称

·*version*：报警版本（取值为trap\<v1\>、trap\<v2\>和inform三种）

·*address*：目的IP地址

Request ID: *request-id*

告警报文PDU中的request-id字段，*request-id*取值恒为0

Error status: *error-status*

告警报文PDU中的error-status字段，*error-status*取值恒为0

Error index: *error-index*

告警报文PDU中的error-index字段，*error-index*取值恒为0

UDP port: *port-number*

目的主机接收告警信息的UDP端口号

*[port-number*]：UDP端口号

Trap successfully sent.

告警发送成功

VBLIST

告警报文中变量绑定对列表

【举例】

\# 在一台使能了SNMP trap发送功能的设备上打开信息中心调试开关和SNMP 告警报文调试开关。在系统视图下依次执行**undo snmp-agent**和**snmp-agent**两条命令，设备发送warmStart告警。

\<Sysname\> terminal debugging

\<Sysname\> terminal monitor

\<Sysname\> debugging snmp trap packet

Sysname undo snmp-agent

Sysname snmp-agent

Sysname

\*Jul 27 10:10:35:297 2007 Sysname SNMP/7/TRAP_PACKET:

   warmStart trap\<v2\> send to: 10.165.81.75

   Request ID: 0

   Error status: 0

   Error index: 0

   UDP port: 162

Trap successfully sent.

\*Jul 27 10:10:35:297 2007 Sysname SNMP/7/VBLIST:

   sysUpTime.0: 5936387

\*Jul 27 10:10:35:297 2007 Sysname SNMP/7/VBLIST:

   snmpTrapOID.0: 1.3.6.1.6.3.1.1.5.2

*// 设备向IP地址为10.165.81.75的主机发送v2版的trap告警报文，告警节点名为warmStart，报文PDU中的请求ID为0，错误状态为0，错误索引为0，目的主机的UDP端口号为162，发送成功，绑定变量sysUpTime.0和snmpTrapOID.0的值分别是5936387和1.3.6.1.6.3.1.1.5.2。*

**SNMP \-- SNMP调试命令 \-- debugging snmp trap process**

------------------------------------------------------------------------

**[debugging snmp trap process**]命令用来打开告警处理的调试信息开关。

**[undo debugging snmp trap process**]命令用来关闭告警处理的调试信息开关。

【命令】

**[debugging snmp trap**[ **process** [ **error** \| **info** \| **warning** ]]]

**[undo debugging snmp trap**[ **process** [ **error** \| **info** \| **warning** ]]]

【视图】

用户视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

**[error**]：表示调试信息等级为error的调试信息开关，输出级别为error的调试信息。该类调试信息指的是SNMP协议栈或系统运行时的错误信息。

**[info**]：表示调试信息等级为info的调试信息开关，输出级别为info的调试信息。该类调试信息指的是SNMP协议栈或系统运行时的提示信息。

**[warning**]：表示调试信息等级为warning的调试信息开关，输出级别为warning的调试信息。该类调试信息指的是SNMP协议栈或系统运行时的重要信息。

【描述】

**[debugging snmp trap process**]命令用来打开告警处理的调试信息开关。**undo debugging snmp trap process**命令用来关闭告警处理的调试信息开关。缺省情况下，SNMP告警调试信息开关处于关闭状态。

表1-8 debugging snmp trap process命令输出信息描述表

字段

描述

TRAP_INFO

告警处理时级别为info的调试信息

TRAP_WARNING

告警处理时级别为warning的调试信息

TRAP_ERROR

告警处理时级别为error的调试信息

Failed to create trap socket

创建告警socket失败

Trap socket is closed.

告警socket被关闭

No available remote configuration parameters for generating traps

远端的参数配置无效，不能生成告警信息

Trap message timed out

告警消息超时

Create trap IPv4 socket

创建发送告警的IPv4 socket

Failed to create trap IPv4 socket

创建发送告警的IPv4 socket失败

Failed to bind trap IPv4 socket

绑定发送告警的IPv4 socket失败

Create trap IPv6 socket

创建发送告警的IPv6 socket

Failed to create trap IPv6 socket

创建发送告警的IPv6 socket失败

Failed to bind trap IPv6 socket

绑定发送告警的IPv6 socket失败

Close trap IPv4/IPv6 socket

关闭发送告警的IPv4/IPv6 socket

Send trap through IPv4 socket

通过IPv4 socket发送告警

Failed to get source IP address while sending trap through IPv4 socket

通过IPv4 socket发送告警时获取IPv4源地址失败

Trap sending through IPv4 socket failure: Invalid VPN index.

通过IPv4 socket发送告警时VPN索引无效

Failed to send trap through IPv4 socket

通过IPv4 socket发送告警失败

Send trap through IPv6 socket

通过IPv6 socket发送告警

Trap sending through IPv6 socket failure: Invalid IPv6 interface index.

通过IPv6 socket发送告警时IPv6接口索引无效

Failed to send trap through IPv6 socket

通过IPv6 socket发送告警失败

Send trap message to trap queue

发送告警消息至告警队列

Failed to get the number of messages in trap queue

取告警队列中消息个数失败

Trap queue is full.

告警队列满

Failed to read trap queue

读告警队列失败

Failed to write trap event

写告警事件失败

Failed to add trap message to trap queue

向告警队列添加告警消息失败

Process trap message in trap queue at * time-hour:time-minute*:*time-second*

在time-hour：time-minute：time-second时间处理告警队列中的一个告警消息

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

Failed to parse trap message

解析告警消息失败

Parse trap message

解析告警消息

Wrong data type of 1st parameter in trap message

告警消息中的第一个参数数据类型错误

Failed to parse data value of 1st parameter in trap message

解析告警消息中第一个参数的数值失败

Failed to find trap node specified in trap message

查找告警消息中指定告警节点失败

Node specified in trap message is not trap-type.

告警消息中指定的节点不是trap类型

Failed to get trap\'s index-lists

取告警绑定节点的索引列表失败

Failed to build trap\'s variable-bindings

构造告警变量绑定列表失败

Failed to get trap\'s generic trap type

取告警的generic类型失败

Get trap\'s index-lists

取告警绑定节点的索引列表

Failed to search *trap-name\'s* binding node

查找告警绑定节点失败

*[trap-name*]：告警节点名

Get index-list of *trap-name*\'s binding node *node-name*

取告警绑定节点的索引列表

·*trap-name*：告警节点名

·*node-name*：绑定节点名

Wrong number of parameters in *trap-name*\'s trap message

告警消息中参数个数错误

*[trap-name*]：告警节点名

The parameter type in *trap-name*\'s trap message doesn\'t match its binding node *node-name*\'s.

告警消息中参数类型与其绑定节点的参数类型不匹配

·*trap-name*：告警节点名

·*node-name*：绑定节点名

Failed to get *node-name*\'s value from *trap-name*\'s trap message

从告警消息中取绑定节点的实例值失败

·*trap-name*：告警节点名

·*node-name*：绑定节点名

Failed to check *node-name*\'s value from *trap-name*\'s trap message

告警消息中绑定节点的实例值数据检查失败

·*trap-name*：告警节点名

·*node-name*：绑定变量节点名

Build *trap-name*\'s variable-bindings

构造trap的变量绑定列表失败

*[trap-name*]：告警节点名

Empty binding node for *trap-name*

告警绑定节点为空

*[trap-name*]：告警节点名

Wrong binding node *node-name* for *trap-name*

错误的告警绑定节点

·*trap-name*：告警节点名

·*node-name*：绑定节点名

Failed to copy *node-name*\'s value

拷贝*node-name*节点实例值失败

*[node-name*]：绑定节点名

Failed to convert binding node *node-name*\'s index value to OID

转换绑定节点*node-name*的索引值为OID失败

*[node-name*]：绑定节点名

Prepare to generate and send trap *trap-name*

准备生成并发送告警

*[trap-name*]：告警节点名

Failed to get *trap-name*\'s OID

取告警节点OID失败

*[trap-name*]：告警节点名

Failed to build *trap-name*\'s v2 variable-bindings

构造trap的绑定变量列表失败

*[trap-name*]：告警节点名

Invalid snmpNotifyType

无效的SNMP告警类型

No valid entries in snmpTargetAddrTable for sending trap

没有有效的snmpTargetAddrTable配置表项发送告警

Filter address *address* for sending *trap-name*

发送告警消息时过滤掉目的地址为*address*的trap信息

·*trap-name*：告警节点名

·*address*：发送告警的目的IP地址

No entry in snmpTargetParamsTable matches snmpTargetAddrParams *value*.

在snmpTargetParamsTable表中没有与节点snmpTargetAddrParams的实例值匹配的表项

*[value*]：snmpTargetAddrParams节点的一个实例值

Wrong message processing model (*message-processing-model*) or unsupported SNMP version (*version*)

错误的消息处理模型或不支持的SNMP版本

·*message-processing-model*：消息处理模型值

·*version*：SNMP版本

Failed to check trap *trap-name*\'s VACM (security model: *security-model*, security name: *security-name*, security level: *security-level*)

*[Trap-name*]告警的VACM检查失败

·*trap-name*：告警节点名

·*security-model*：安全模型值

·*security-name*：安全名

·*security-level*：安全等级值

Failed to get *trap-name*\'s source IP address

获取*trap-name*告警的源IP地址失败

*[trap-name*]：告警节点名

Failed to create *trap-name* packet

创建*trap-name*告警报文失败

*[trap-name*]：告警节点名

Unknown destination IP type (*type*) for sending *trap-name*

发送的*trap-name*告警报文目的IP类型未知

·*type*：目的IP类型

·*trap-name*：告警节点名

Trap-name successfully sent at *time-hour*:*time-minute*:*time-second*

Trap-name告警于time-hour：time-minute：time-second时间成功发送

·*trap-name*：告警节点名

·*time-hour*：小时

·*time-minute*：分钟

·*time-second*：秒

Failed to create *trap-name* packet (PDU size: *pdu-size*)

创建*trap-name*的告警报文失败

·*trap-name*：告警节点名

·*pdu-size*：PDU大小

Search entries in snmpTargetAddrTable to match snmpNotifyTag *value*

在snmpTargetAddrTable表中寻找与节点snmpNotifyTag的实例值匹配的表项

*[value*]：snmpNotifyTag节点的一个实例值

Search entries in snmpTargetParamsTable to match snmpTargetAddrParams *value*

在 snmpTargetParamsTable表中寻找与节点snmpTargetAddrParams的实例值匹配的表项

*[value*]：snmpTargetAddrParams节点的一个实例值

Create *trap-name* packet

创建*trap-name*的告警报文

*[trap-name*]：告警节点名

Encode *SNMP-version* trap

编码告警报文

*[SNMP-version*]：SNMP版本（取值SNMPv1和SNMPv2c）

Get generic trap type

获取告警类型

Get enterprise OID

获取企业OID

Failed to get sysObjectID while getting enterprise OID

获取企业OID时，获取sysObjectID节点值失败

Check trap *trap-name*\'s VACM

检查*trap-name*告警的VACM

*[trap-name*]：告警节点名

Failed to get binding node *node-name*\'s OID

获取绑定节点*node-name*的OID失败

*[node-name*]：绑定节点名

Failed to check *node-name*\'s VACM

*[Node-name*]节点的VACM检查失败

*[node-name*]：MIB节点名

Get source IPv4 address for sending trap

获取发送告警的源IPv4地址

Get source IPv6 address for sending trap

获取发送告警的源IPv6地址

Failed to get source IPv4 address for sending trap

获取发送告警的源IPv4地址失败

Failed to get source IPv6 address for sending trap

获取发送告警的源IPv6地址失败

Unknown destination IP type (*type*) for sending trap

发送告警时目的IP类型未知

*[type*]：类型

【举例】

\# 在一台使能了SNMP告警发送功能的设备上打开信息中心调试开关和SNMP告警子模块级别为info的调试开关。在系统视图下依次执行**undo snmp-agent**和**snmp-agent**两条命令，设备发送warmStart告警。

\<Sysname\> terminal debugging

\<Sysname\> terminal monitor

\<Sysname\> debugging snmp trap process info

Sysname undo snmp-agent

Sysname snmp-agent

Sysname

\*Jul 27 10:21:22:938 2007 Sysname SNMP/7/TRAP_INFO:

   Send trap message to trap queue

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Create trap IPv4 socket

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Create trap IPv6 socket

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Process trap message in trap queue at 10:21:22

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Parse trap message

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Get trap\'s index-lists

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Build warmStart\'s variable-bindings

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Get generic trap type

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Prepare to generate and send trap warmStart

\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:

   Search entries in snmpTargetAddrTable to match snmpNotifyTag TrapHost

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Search entries in snmpTargetParamsTable to match snmpTargetAddrParams traphost.u2.192.168.123.123

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Check trap warmStart\'s VACM

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Get source IPv4 address for sending trap

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Search entries in snmpTargetParamsTable to match snmpTargetAddrParams traphost.uu.10.165.81.75

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Check trap warmStart\'s VACM

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Get source IPv4 address for sending trap

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Create warmStart packet

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Get enterprise OID

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Encode SNMPv2c trap

\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:

   Send trap through IPv4 socket

\*Jul 27 10:21:23:16 2007 Sysname SNMP/7/TRAP_INFO:

   warmStart successfully sent at 10:21:22

*[// SNMP*]*告警子模块处理告警消息，发送warmStart告警报文，输出级别为info的调试信息。*
