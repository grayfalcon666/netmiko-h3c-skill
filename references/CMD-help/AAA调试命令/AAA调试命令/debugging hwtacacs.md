
**AAA调试命令 \-- AAA调试命令 \-- debugging hwtacacs**

------------------------------------------------------------------------

【命令】

**[debugging hwtacacs **[{ **all** \| **error** \| **event** \| **receive-packet** \| **send-packet** }]]

**[undo debugging hwtacacs **[{ **all** \| **error** \| **event** \| **receive-packet** \| **send-packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[receive-packet**]：表示接收报文调试信息开关。

**[send-packet**]：表示发送报文调试信息开关。

【描述】

**[debugging hwtacacs**]命令用来打开HWTACACS调试信息开关。**undo debugging hwtacacs**命令用来表示关闭HWTACACS调试信息开关。

缺省情况下，HWTACACS调试信息开关处于关闭状态。

表1-1 debugging hwtacacs error命令输出信息描述表

字段

描述

PAM_TACACS: Failed to connect to server.

PAM_TACACS：连接服务器失败

PAM_TACACS: Failed to encapsulate request packet.

PAM_TACACS：封装请求报文失败

PAM_TACACS: Failed to send request data.

PAM_TACACS：发送请求数据失败

PAM_TACACS: Failed to process reply data.

PAM_TACACS：处理应答数据失败

PAM_TACACS: Failed to get available server.

PAM_TACACS：获取可用的服务器失败

PAM_TACACS: Failed to encapsulate authentication continue request packet.

PAM_TACACS：封装认证持续请求报文失败

PAM_TACACS: Failed to receive *type* reply data.

PAM_TACACS：接收类型为*type*的应答数据失败

PAM_TACACS: Failed to process request data.

PAM_TACACS：处理请求数据失败

PAM_TACACS: Failed to set scheme name to pam-module-data.

PAM_TACACS：保存方案名到PAM数据中失败

PAM_TACACS: Failed to set authentic.

PAM_TACACS：设置Authentic属性失败

PAM_TACACS: Item length too long.

PAM_TACACS：数据项长度超长

PAM_TACACS: Failed to find sequence for *type* packet.

PAM_TACACS：查找类型为*type*的报文序列号失败

PAM_TACACS: Failed to decrypt reply packet.

PAM_TACACS：解密应答报文失败

PAM_TACACS: Failed to encrypt packet.

PAM_TACACS：加密报文失败

PAM_TACACS: Invalid length of reply packet.

PAM_TACACS：应答报文长度非法

PAM_TACACS: Failed to instruct aaad to set server in block state.

PAM_TACACS：通知aaad进程服务器状态block失败

PAM_TACACS: Invalid reply packet.

PAM_TACACS：应答报文无效

PAM_TACACS: Failed to send packet, errorCode=*error-number*.

PAM_TACACS：发送报文失败，返回错误码*error-number*.

表1-2 debugging hwtacacs event命令输出信息描述表

字段

描述

PAM_TACACS: Processing authentication reply packet.

PAM_TACACS：处理认证回应报文

PAM_TACACS: Processing authorization reply packet.

PAM_TACACS：处理授权回应报文

PAM_TACACS: Processing accounting reply packet.

PAM_TACACS：处理计费回应报文

PAM_TACACS: Encapsulating authentication request packet.

PAM_TACACS：封装认证请求报文

PAM_TACACS: Encapsulating authorization request packet.

PAM_TACACS：封装授权请求报文

PAM_TACACS: Encapsulating accounting request packet.

PAM_TACACS：封装计费请求报文

PAM_TACACS: Encapsulating authentication continue request packet.

PAM_TACACS：封装认证持续请求报文

PAM_TACACS: Sending authentication continue request packet.

PAM_TACACS：发送认证持续请求报文

PAM_TACACS: Session successfully created.

PAM_TACACS：创建会话成功

PAM_TACACS: Getting available server, server-ip=*server-ip*; server-port=*server-port*; VPN instance=*vpn-instance*.

PAM_TACACS：获取可用的服务器，服务器IP地址为*server-ip*，端口号为*server-port*，服务器所属的MPLS L3VPN为*vpn-instance*

PAM_TACACS: Connection succeeded, server-ip=*server-ip*, port=*server-port*, VPN instance=*vpn-instance*

PAM_TACACS：连接服务器成功，服务器IP地址为*server-ip*，端口号为*server-port*，服务器所属的MPLS L3VPN为*vpn-instance*

PAM_TACACS: Dispatching request, Primitive: *primitive-name*.

PAM_TACACS：分发请求，表示请求类型的原语为*primitive-name*

PAM_TACACS: Creating request data, data type: *request-type.*

PAM_TACACS：创建请求数据，数据类型为*request-type*

PAM_TACACS: Processing reply data, Reply Type: *type.*

PAM_TACACS：处理应答输入，应答类型为*type*

PAM_TACACS: Processed authentication reply message, resultCode: *code*.

PAM_TACACS：处理了认证应答消息，结果码为*code*

PAM_TACACS: Processed authorization reply message, resultCode: *code*.

PAM_TACACS：处理了授权应答消息，结果码为*code*

PAM_TACACS: Processing TACACS authentication.

PAM_TACACS：处理TACACS认证

PAM_TACACS: Processing TACACS authorization.

PAM_TACACS：处理TACACS授权

PAM_TACACS: Processing TACACS start-accounting.

PAM_TACACS：处理TACACS开始计费

PAM_TACACS: Processing TACACS stop-accounting.

PAM_TACACS：处理TACACS结束计费

PAM_TACACS: Processing TACACS update-accounting.

PAM_TACACS：处理TACACS实时计费

PAM_TACACS: TACACS authentication succeeded..

PAM_TACACS：处理TACACS认证成功

PAM_TACACS: TACACS authorization succeeded.

PAM_TACACS：处理TACACS授权成功

PAM_TACACS: TACACS start-accounting succeeded.

PAM_TACACS：处理TACACS开始计费成功

PAM_TACACS: TACACS stop-accounting succeeded.

PAM_TACACS：处理TACACS结束计费成功

PAM_TACACS: TACACS update-accounting succeeded.

PAM_TACACS：处理TACACS实时计费成功

PAM_TACACS: Received packet, length=*packet-len*, errorCode=*error-number*.

PAM_TACACS：接收报文，获取到的报文长度错误，报文长度为*packet-len*，错误码为*error-number*

PAM_TACACS: Received socket close event.

PAM_TACACS：收到关闭socket事件，本端也要关闭socket

PAM_TACACS: Response timed out.

PAM_TACACS：响应报文超时

PAM_TACACS: Connection timed out.

PAM_TACACS：连接超时

PAM_TACACS: Connecting to server\...

PAM_TACACS：连接服务器

PAM_TACACS: Reply SocketFd received *event* event.

PAM_TACACS：回应报文套接字接收到*event*事件

PAM_TACACS: Reply message successfully sent.

PAM_TACACS：成功发送回应消息

表1-3 debugging hwtacacs receive-packet命令输出信息描述表

字段

描述

The reply packet body is invalid

报文主体不合法

version

协议版本号

type

报文类型

·AUTHEN_REQUEST：认证请求报文

·AUTHEN_REPLY：认证回应报文

·AUTHEN_CONTINUE：持续认证报文

·AUTHOR_REQUEST：授权请求报文

·AUHTOR_REPLY：授权回应报文

·ACCOUNT_REQUEST：计费请求报文

·ACCOUNT_REPLY：计费回应报文

seq_no

报文序列号，每个会话的第一个报文其序列号必为1，后续的报文递增

flag

报文主体是否加密的标志

·UNENCRYPTED_FLAG：非加密

·ENCRYPTED_FLAG：加密

session-id

会话ID，随机生成，在会话过程中此值不变

length of payload

报文主体的长度

status

当前认证、授权和计费状态

flags

用户输入的用户名和密码是否回显（认证响应包中）

server_msg len

显示给用户的信息长度

data len

服务器返回用于说明用户失败原因的信息的长度

server-msg

服务器返回给登录用户的信息，需要输出到用户端

data

服务器返回的信息，用于说明失败原因

arg_cnt

授权属性个数

argN_len

第N个授权属性的长度

argN:

第N个授权属性

表1-4 debugging hwtacacs send-packet命令输出信息描述表

字段

描述

version

协议版本号

type

报文类型

·AUTHEN_REQUEST：认证请求报文

·AUTHEN_REPLY：认证回应报文

·AUTHEN_CONTINUE：持续认证报文

·AUTHOR_REQUEST：授权请求报文

· AUHTOR_REPLY：授权回应报文

·ACCOUNT_REQUEST：计费请求报文

·ACCOUNT_REPLY：计费回应报文

seq_no

报文序列号，每个会话的第一个报文其序列号必为1，后续的报文递加

flag

报文主体是否加密的标志

·UNENCRYPTED_FLAG：非加密

·ENCRYPTED_FLAG：加密

session-id

会话ID，随机生成，在会话过程中此值不变

length of payload

报文主体的长度

version

报文的序列号

type

报文类型

·AUTHEN_REQUEST：认证请求报文

·AUTHEN_REPLY：认证回应报文

·AUTHEN_CONTINUE：持续认证报文

·AUTHOR_REQUEST：授权请求报文

· AUHTOR_REPLY：授权回应报文

·ACCOUNT_REQUEST：计费请求报文

·ACCOUNT_REPLY：计费回应报文

seq_no

报文序列号，每个会话的第一个报文其序列号必为1，后续的报文递加

flag

报文主体是否加密的标志

·UNENCRYPTED_FLAG，非加密

·ENCRYPTED_FLAG，加密

session-id

会话ID，随机生成，在会话过程中此值不变

action

需要对用户执行的认证动作

priv_lvl

用户级别，取值为0～15

authen_type

认证类型

service

服务类型

user_len

请求的用户名的长度

port_len

用户发起认证的端口名的长度

rem_len

用户的地址长度

data_len

向服务器发送的数据长度

user

用户名

port

用户发起认证的端口名称

rem_addr

用户的地址

data

向服务器发送的数据，具体数据和报文类型以及各个字段的内容有关

user_msg len

用户输入的字符串长度

flags

对于持续认证报文，表示将要执行的动作：

·ABORT：退出

·CONTINUE：继续认证

对于计费报文，表示计费报文的类型：

·START：计费开始

·STOP：计费结束

·WATCHDOG：计费更新

authen_method

认证采用的方法

authen_service

用户申请的服务类型

arg_cnt

授权请求属性个数

argN_len

第N个授权请求属性长度

argN

第N个授权属性内容

【举例】

\# 在设备上进行HWTACACS的相关配置，打开HWTACACS的事件调试信息开关。当用户从Console口登录设备时，设备上输出如下调试信息。

\<Sysname\> debugging hwtacacs event

\*Sep 14 03:00:26:951 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing TACACS authentication.

*// 处理TACACS认证请求*

\*Sep 14 03:00:26:951 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Dispatching request, Primitive: authentication.

*// 分发请求，请求类型为认证*

\*Sep 14 03:00:26:951 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: START

*// 创建请求数据，数据类型为START*

\*Sep 14 03:00:26:952 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Session successfully created.

*// 创建会话成功*

\*Sep 14 03:00:26:952 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Getting available server, server-ip=192.168.0.111, server-port=49, VPN instance=\--(public).

*// 获取到可用的服务器，服务器IP地址为192.168.0.111，端口号为49，位于公网*

\*Sep 14 03:00:26:953 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connecting to server\...

*// 连接服务器*

\*Sep 14 03:00:26:954 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLOUT event.

*// 应答报文套接字接收到EPOLLOUT事件*

\*Sep 14 03:00:26:954 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connection succeeded, server-ip=192.168.0.111, port=49, VPN instance=\--(public).

*// 连接服务器成功，服务器IP地址为192.168.0.111，端口号为49，位于公网*

\*Sep 14 03:00:26:954 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating authentication request packet.

*// 封装认证请求报文*

\*Sep 14 03:00:27:125 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.

*// 应答报文套接字接收到EPOLLIN事件*

\*Sep 14 03:00:27:126 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing authentication reply packet.

*// 处理认证回应报文*

\*Sep 14 03:00:27:126 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.

*// 成功发送回应消息*

\*Sep 14 03:00:27:127 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed authentication reply message, resultCode: 2.

*// 处理认证回应数据，回应类型为持续认证*

\*Sep 14 03:00:27:127 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: CONTINUE

\*Sep 14 03:00:27:127 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating authentication continue request packet.

\*Sep 14 03:00:27:127 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Sending authentication continue request packet.

*// 创建持续认证报文并组装发送*

\*Sep 14 03:00:27:824 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.

*// 回应报文套接字接收到EPOLLIN事件*

\*Sep 14 03:00:27:824 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing authentication reply packet.

*// 处理认证回应报文*

\*Sep 14 03:00:27:824 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.

*// 回应消息发送成功*

\*Sep 14 03:00:27:825 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed authentication reply message, resultCode: 0

*// 处理了认证回应消息，结果码为0*

\*Sep 14 03:00:27:825 2012 Sysname TACACS/7/EVENT: PAM_TACACS: TACACS authentication succeeded.

*// 处理TACACS认证成功*

\*Sep 14 03:00:27:832 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing TACACS authorization.

*// 处理TACACS授权请求*

\*Sep 14 03:00:27:832 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Dispatching request, Primitive: authorization.

*// 分发请求，请求类型为授权*

\*Sep 14 03:00:27:832 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: START

*// 创建请求数据，数据类型为START*

\*Sep 14 03:00:27:833 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Session successfully created.

*// 创建会话成功*

\*Sep 14 03:00:27:833 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Getting available server, server-ip=192.168.0.111, server-port=49, VPN instance=\--(public).

*// 获取到可用的服务器，服务器IP地址为192.168.0.111，端口号为49，位于公网*

\*Sep 14 03:00:27:834 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connecting to server\...

*// 连接服务器*

\*Sep 14 03:00:27:834 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLOUT event.

*// 回应报文套接字接收到EPOLLOUT事件*

\*Sep 14 03:00:27:834 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connection succeeded, server-ip=192.168.0.111, port=49, VPN instance=\--(public).

*// 连接服务器成功，服务器IP地址为192.168.0.111，端口号为49，位于公网*

\*Sep 14 03:00:27:835 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating authorization request packet.

*// 封装授权请求报文*

\*Sep 14 03:00:28:014 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.

*// 回应报文套接字接收到EPOLLIN事件*

\*Sep 14 03:00:28:014 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing authorization reply packet.

*// 处理授权回应报文*

\*Sep 14 03:00:28:014 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.

*// 成功发送应答消息*

\*Sep 14 03:00:28:015 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed authorization reply message, resultCode: 0

*// 处理了授权回应消息，结果码为0，表示授权成功*

\*Sep 14 03:00:28:016 2012 Sysname TACACS/7/EVENT: PAM_TACACS: TACACS authorization succeeded.

*// 处理TACACS授权成功*

\*Sep 14 03:00:28:024 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing TACACS start-accounting.

*// 处理TACACS开始计费请求*

\*Sep 14 03:00:28:024 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Dispatching request, Primitive: accounting-start.

*// 分发请求，请求类型为开始计费*

\*Sep 14 03:00:28:024 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: START

*// 创建请求数据，数据类型为START*

\*Sep 14 03:00:28:025 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Session successfully created.

*// 创建会话成功*

\*Sep 14 03:00:28:025 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Getting available server, server-ip=192.168.0.111, server-port=49, VPN instance=\--(public).

*// 获取到可用的服务器，服务器IP地址为192.168.0.111，端口号为49，位于公网*

\*Sep 14 03:00:28:026 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connecting to server\...

*// 连接服务器*

\*Sep 14 03:00:28:026 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLOUT event.

*// 回应报文套接字接收到EPOLLOUT事件*

\*Sep 14 03:00:28:026 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connection succeeded, server-ip=192.168.0.111, port=49, VPN instance=\--(public).

*// 连接服务器成功，服务器IP地址为192.168.0.111，端口号为49*

\*Sep 14 03:00:28:026 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating accounting request packet.

*// 封装计费请求报文*

\*Sep 14 03:00:28:082 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.

\*Sep 14 03:00:28:083 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing accounting reply packet.

*// 处理计费回应报文*

\*Sep 14 03:00:28:083 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.

*// 成功发送回应消息*

\*Sep 14 03:00:28:084 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed accounting-start reply message, resultCode: 0

*// 处理了认证回应消息，结果码为0，表示开始计费成功*

\*Sep 14 03:00:28:084 2012 Sysname TACACS/7/EVENT: PAM_TACACS: TACACS start-accounting succeeded.

*// 处理TACACS开始计费成功*

\# 在设备上进行HWTACACS的相关配置，打开HWTACACS的事件调试信息开关。当从Console口登录到设备的用户进行logout操作时，设备上输出如下调试信息。

\<Sysname\> debugging hwtacacs event

\*Sep 14 03:10:31:210 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing TACACS stop-accounting.

*// 处理TACACS停止计费请求*

\*Sep 14 03:10:31:211 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Dispatching request, Primitive: accounting-stop.

*// 分发请求，请求类型为停止计费*

\*Sep 14 03:10:31:211 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: START

*// 创建请求数据，数据类型为START*

\*Sep 14 03:10:31:211 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Session successfully created.

*// 创建会话成功*

\*Sep 14 03:10:31:211 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Getting available server, server-ip=192.168.0.111, server-port=49, VPN instance=\--(public).

*// 获取到可用的服务器，服务器IP地址为192.168.0.111，端口号为49，位于公网*

\*Sep 14 03:10:31:212 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connecting to server\...

*// 连接服务器*

\*Sep 14 03:10:31:214 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd receive

d EPOLLOUT event.

*// 回应报文套接字接收到EPOLLOUT事件*

\*Sep 14 03:10:31:214 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connection succeeded,

server-ip=192.168.0.111, port=49, VPN instance=\--(public).

*// 连接服务器成功，服务器IP地址为192.168.0.111，端口号为49，位于公网*

\*Sep 14 03:10:31:214 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating accounting request packet.

*// 封装计费请求报文*

\*Sep 14 03:10:31:376 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.

*// 回应报文套接字接收到EPOLLIN事件*

\*Sep 14 03:10:31:376 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing accounting

reply packet.

*// 处理计费回应报文*

\*Sep 14 03:10:31:377 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.

*// 成功发送回应消息*

\*Sep 14 03:10:31:377 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed accounting-stop reply message, resultCode: 0

*// 处理了结束计费回应消息，结果码为，表示结束计费成功*

\*Sep 14 03:10:31:377 2012 Sysname TACACS/7/EVENT: PAM_TACACS: TACACS stop-accounting succeeded.{.MsoCommentReference}

*// 处理TACACS结束计费成功*

\# 在设备上进行HWTACACS的相关配置，打开HWTACACS的发送报文调试信息开关。当用户从Console口登录设备时，设备上输出如下调试信息。

\<Sysname\> debugging hwtacacs send-packet

\*Apr 17 11:48:51:342 2010 Sysname TACACS/7/send_packet:Slot=1;

version: 0xc0  type: AUTHEN_REQUEST  seq_no: 1  flag: ENCRYPTED_FLAG

session-id: 0x763657e2

length of payload: 23

action: LOGIN  priv_lvl: 0  authen_type: ASCII  service: LOGIN

user_len: 5    port_len: 0   rem_len: 5   data_len: 0

user: usera

port:

rem_addr: async

data:

*// 发送认证请求报文，携带用户名*

\*Apr 17 11:23:46:672 2010 Sysname TACACS/7/send_packet:Slot=1;

version: 0xc0  type: AUTHEN_CONTINUE  seq_no: 3  flag: ENCRYPTED_FLAG

session-id: 0x7eae3416

length of payload: 11

user_msg len: \*\*\*\*\*\*  data_len: 0  flags: CONTINUE AUTHEN

user_msg: \*\*\*\*\*\*

data:

*// 发送认证持续报文，携带用户密码*

\*Apr 17 11:48:53:11 2010 Sysname TACACS/7/send_packet:Slot=1;

version: 0xc0  type: AUTHOR_REQUEST  seq_no: 1  flag: ENCRYPTED_FLAG

session-id: 0x7fc6570e

length of payload: 42

authen_method: TACACSPLUS  priv_lvl: 0  authen_type: ASCII  authen_service: LOGIN

user_len: 5    port_len: 0    rem_len: 5    arg_cnt: 2

arg0_len: 13    arg1_len: 4 

user: usera

port:

rem_addr: async

arg0: service=shell  arg1: cmd\*

*// 发送授权请求报文*

\*Apr 17 11:48:53:94 2010 Sysname TACACS/7/send_packet:Slot=1;

version: 0xc0  type: ACCOUNT_REQUEST  seq_no: 1  flag: ENCRYPTED_FLAG

session-id: 0x6e38fb96

length of payload: 59

flags: START

authen_method: TACACSPLUS  authen_service: LOGIN

user_len: 5   port_len: 0   rem_len: 5   arg_cnt: 3

arg0_len: 9     arg1_len: 10    arg2_len: 13

user: usera

port:

rem_addr: async

arg0: task_id=0  arg1: timezone=0

arg2: service=shell

*// 发送计费开始报文*

**

\# 在设备上进行HWTACACS的相关配置，打开HWTACACS的发送报文调试信息开关。当从Console口登录设备的用户进行logout操作时，设备上输出如下调试信息。

\<Sysname\> debugging hwtacacs send-packet

\*Apr 17 11:49:06:724 2010 Sysname TACACS/7/send_packet:Slot=1;

version: 0xc0  type: ACCOUNT_REQUEST  seq_no: 1  flag: ENCRYPTED_FLAG

session-id: 0x6fe71ef7

length of payload: 179

flags: STOP

authen_method: TACACSPLUS  authen_service: LOGIN

user_len: 5   port_len: 0   rem_len: 5   arg_cnt: 12

arg0_len: 9     arg1_len: 10    arg2_len: 13    arg3_len: 12

arg4_len: 16    arg5_len: 10    arg6_len: 11    arg7_len: 9 

arg8_len: 10    arg9_len: 15    arg10_len: 14    arg11_len: 14

user: usera

port:

rem_addr: async

arg0: task_id=0  arg1: timezone=0

arg2: service=shell  arg3: disc_cause=0

arg4: disc_cause_ext=0  arg5: bytes_in=0

arg6: bytes_out=0  arg7: paks_in=0

arg8: paks_out=0  arg9: elapsed_time=13

arg10: nas_rx_speed=0  arg11: nas_tx_speed=0

*// 发送计费结束报文*

**

\# 在设备上进行HWTACACS的相关配置，打开HWTACACS的接收报文调试信息开关。当用户从Console口登录设备时，设备上输出如下调试信息。

\<Sysname\> debugging hwtacacs receive-packet

\*Apr 17 11:52:20:318 2010 Sysname TACACS/7/recv_packet:Slot=1;

version: 0xc0  type: AUTHEN_REPLY  seq_no: 2  flag: ENCRYPTED_FLAG

session-id: 0x2a1186eb

length of payload: 16

status: STATUS_GETPASS  flags: NOECHO

server_msg len: 10  data len: 0

server_msg: Password:

data:

*// 接收认证回应报文，回应类型为获取密码*

\*Apr 17 11:52:22:959 2010 Sysname TACACS/7/recv_packet:Slot=1;

version: 0xc0  type: AUTHEN_REPLY  seq_no: 4  flag: ENCRYPTED_FLAG

session-id: 0x2a1186eb

length of payload: 6

status: STATUS_PASS  flags: ECHO

server_msg len: 0  data len: 0

server_msg:

data:

*// 接收认证回应报文，回应类型为认证通过*

\*Apr 17 11:52:22:982 2010 Sysname TACACS/7/recv_packet:Slot=1;

version: 0xc0  type: AUTHOR_REPLY  seq_no: 2  flag: ENCRYPTED_FLAG

session-id: 0x7339c2a3

length of payload: 18

Status: STATUS_PASS_ADD  arg_cnt: 1  server_msg len: 0  data len: 0

arg0_len: 11

server_msg:

data:

arg0: priv-lvl=15 

*// 接收授权回应报文，回应类型为授权成功*

\*Apr 17 11:52:23:68 2010 Sysname TACACS/7/recv_packet:Slot=1;

version: 0xc0  type: ACCOUNT_REPLY  seq_no: 2  flag: ENCRYPTED_FLAG

session-id: 0xeede416

length of payload:  5

server_msg len: 0  data len: 0  status: STATUS_SUCCESS

server_msg:

data:

*// 接收计费回应报文，回应类型为计费成功*

\# 在设备上进行HWTACACS的相关配置，打开HWTACACS的接收报文调试信息开关。当从Console口登录设备的用户进行logout操作时，设备上输出如下调试信息。

\*Apr 17 11:52:26:670 2010 Sysname TACACS/7/recv_packet:Slot=1;

version: 0xc0  type: ACCOUNT_REPLY  seq_no: 2  flag: ENCRYPTED_FLAG

session-id: 0x69522f6

length of payload: 5

server_msg len: 0  data len: 0  status: STATUS_SUCCESS

server_msg:

data:

*// 接收计费回应报文，回应类型为计费成功*

**AAA调试命令 \-- AAA调试命令 \-- debugging ldap**

------------------------------------------------------------------------

【命令】

**[debugging ldap **[{ **all** \| **error** \| **event** }]]

**[undo debugging ldap**[{ **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging ldap**]命令用来打开LDAP的调试信息开关。**undo debugging ldap**命令用来关闭LDAP的调试信息开关。

缺省情况下，LDAP的调试信息开关处于关闭状态。

表1-5 debugging ldap error命令输出信息列表

字段

描述

PAM_LDAP: Failed to create LDAP session.

创建LDAP会话失败

PAM_LDAP: Failed to save LDAP session.

保存LDAP会话失败

PAM_LDAP: Failed to initialize LDAP.

初始化LDAP失败

PAM_LDAP: Failed to set LDAP options.

设置LDAP协议版本选项失败

PAM_LDAP: Anonymous binding not supported.

不支持匿名绑定

PAM_LDAP: Password not set.

未设置口令

PAM_LDAP: Bind operation failed.

绑定操作失败

PAM_LDAP: Failed to get bind result.

获取绑定结果失败

PAM_LDAP: User DN is invalid.

用户DN无效

PAM_LDAP: Failed to get DN from the search result.

从查找结果获取DN失败

PAM_LDAP: Failed to allocate user DN resource.

分配用户DN资源失败

PAM_LDAP: Failed to get user\'s filter.

获取用户的过滤器失败

PAM_LDAP: Search operation failed.

查找操作失败

PAM_LDAP: Failed to get configuration data.

获取配置数据失败

PAM_LDAP: Failed to get user information.

获取用户信息失败

PAM_LDAP: Failed to perform binding operation as administrator.

管理员身份的绑定操作失败

PAM_LDAP: Failed to perform binding operation as user.

用户身份的绑定操作失败

PAM_LDAP: Failed to create response timeout timer.

创建响应超时定时器失败

PAM_LDAP: Failed to send reply message.

发送应答消息失败

PAM_LDAP: Password decryption failed.

解析密码失败

PAM_LDAP: Failed to search users.

查询用户失败

PAM_LDAP: Failed to add session to buffer.

将Session加入到缓冲表中失败

PAM_LDAP: Failed to create connection resource.

创建连接资源失败

PAM_LDAP: Failed to start state machine.

启动状态机失败

PAM_LDAP: Failed to create reply message.

创建响应信息失败

PAM_LDAP: Failed to find *primitivesname* sequence.

查询*primitivesname*原语序列失败

PAM_LDAP: Failed to find *primitivesname* reply data.

查询*primitivesname*原语响应数据失败

表1-6 debugging ldap event命令输出信息列表

字段

描述

PAM_LDAP: Processing LDAP authenticaion.

LDAP认证操作

PAM_LDAP: Creating LDAP session.

创建LDAP会话

PAM_LDAP: Sending authentication request.

发送认证请求

PAM_LDAP: Opening LDAP session, LDAP server IP = *server-ip*, VPN instance = *vpn-instance*.

打开LDAP会话，服务器IP地址为*server-ip*，服务器所属的MPLS L3VPN为*vpn-instance*

PAM_LDAP: Executing bind operation, DN is *dn*.

执行绑定操作，DN是*dn*

PAM_LDAP: Updating user DN.

更新用户DN

PAM_LDAP: Username is *name*.

用户名是*name*

PAM_LDAP: User\'s filter is *filter*.

用户过滤器是*filter*

PAM_LDAP: Executing search operation.

执行搜索操作

PAM_LDAP: Getting search result.

获取搜索结果

PAM_LDAP: Executing bind operation, user\'s DN is *dn*.

执行绑定操作，用户DN是*dn*

PAM_LDAP: Binding as administrator.

以管理员身份绑定

PAM_LDAP: Getting user information.

获取用户信息

PAM_LDAP: Reopening connection to server.

重新打开到服务器的连接

PAM_LDAP: Binding as user.

以用户身份绑定

PAM_LDAP: Closed connection.

关闭连接

PAM_LDAP: Response timeout timer successfully created.

成功创建响应超时定时器

PAM_LDAP: Administrator\'s binding operation completed.

绑定管理员结束

PAM_LDAP: Reply Socket received EPOLLERR/EPOLLHUP event.

收到EPOLL-ERR或EPOLL-UP事件

PAM_LDAP: Created new connection.

创建新连接

PAM_LDAP: Deleted socket.

删除socket连接

PAM_LDAP: Server response timed out, status=*cur-state*

服务器响应超时，状态为*status*，取值包括：

·1：管理员绑定

·2：用户查询

·3：用户绑定

PAM_LDAP: Performing binding operation as administrator.

正在绑定管理员

PAM_LDAP: Performing binding operation as user.

正在绑定用户

PAM_LDAP: Processing AAA request data.

处理AAA请求数据

PAM_LDAP: Number of buffered sessions reached the maximum.

缓存表项达到最大值

PAM_LDAP: Data of *primitiveName* reply successfully obtained, resultCode: code.

成功获取原语*primitiveName*响应数据，应答码为*code*

PAM_LDAP: Data of *operation* request successfully sent.

成功发送*operation*请求

【举例】

\# 一台主机通过Console口连接设备，设备使用LDAP作为认证方案对登录用户进行身份认证，并打开LDAP的事件调试信息开关。用户通过Console口登录设备的操作时，设备上输出如下调试信息。

\<Sysname\> debugging ldap event

\*Mar 19 05:21:25:177 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Processing LDAP authenticaion.

*[// LDAP*]*认证操作*

\*Mar 19 05:21:25:177 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Creating LDAP session.

*// 创建LDAP会话*

\*Mar 19 05:21:25:177 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Sending authentication request.

*// 发送认证请求*

\*Mar 19 05:21:25:178 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Opening LDAP session, LDAP server = 192.168.0.111, VPN instance = \--(public).

*// 打开LDAP会话，服务器IP地址为192.168.0.111，位于公网*

\*Mar 19 05:21:25:178 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Binding as administrator.

*// 以管理员身份进行绑定*

\*Mar 19 05:21:25:178 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Executing bind operation, DN is cn=administrator,cn=users,dc=secalgnbt,dc=com.

*// 执行绑定操作，用户DN是cn=administrator,cn=users,dc=secalgnbt,dc=com*

\*Mar 19 05:21:25:293 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Getting user information.

*// 获取用户信息*

\*Mar 19 05:21:25:293 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Username is usera.

*// 用户名是usera*

\*Mar 19 05:21:25:293 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:User\'s filter is (&(objectClass=person)(cn=usera)).

*// 用户过滤器是"(&(objectClass=person)(cn=usera))"*

\*Mar 19 05:21:25:293 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Executing search operation.

*// 执行查询操作*

\*Mar 19 05:21:25:336 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Getting search result.

*// 获取查找结果*

\*Mar 19 05:21:25:336 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Updating user DN.

*// 更新用户DN*

\*Mar 19 05:21:25:338 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Reopening connection to server.

*// 重新打开到服务器的连接*

\*Mar 19 05:21:25:338 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Opening LDAP session, LDAP server = 192.168.0.111, VPN instance = \--(public).

*// 开启LDAP会话*

\*Mar 19 05:21:25:338 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Binding as user.

*// 以用户身份进行绑定操作*

\*Mar 19 05:21:25:338 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Executing bind operation, user\'s DN is CN=usera,CN=Users,DC=secalgnbt,DC=com.

*// 执行绑定操作，用户DN为CN=usera,CN=Users,DC=secalgnbt,DC=com*

\*Mar 19 05:21:25:356 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Closed connection.

*// 关闭连接*

\# 一台主机通过二层端口连接设备，设备使用LDAP作为认证方案对认证用户进行身份认证，并打开LDAP的事件调试信息开关。用户发起认证时，设备上输出如下调试信息。

\<Sysname\> debugging ldap event

\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Processing LDAP authenticaion.

*// 处理LDAP认证操作*

\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Processing AAA request data.

*// 处理AAA请求数据*

\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:LDAP server is: 192.168.0.111.

*[// LDAP*]*服务器IP为192.168.0.111*

\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Created new connection.

*// 创建新的连接*

\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Executing bind operation, DN is cn=administrator,cn=users,dc=secalgnbt,dc=com.

*// 执行绑定操作*

\*Mar 19 05:28:29:776 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Data of authentication request successfully sent.

\*Mar 19 05:28:29:777 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Performing binding operation as administrator.

*// 以管理员身份进行绑定操作进行中*

\*Mar 19 05:28:30:878 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Administrator\'s binding operation completed.

*// 以管理员身份进行绑定完成*

\*Mar 19 05:28:30:878 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Response timeout timer successfully created.

*// 成功创建响应超时定时器*

\*Mar 19 05:28:30:939 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Username is usera.

*// 用户名是usera*

\*Mar 19 05:28:30:939 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:User\'s filter is (&(objectClass=person)(cn=usera)).

*// 用户过滤器是"(&(objectClass=person)(cn=usera))"*

\*Mar 19 05:28:30:986 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Updating user DN.

*// 更新用户DN*

\*Mar 19 05:28:30:989 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Performing binding operation as user.

*// 以用户身份进行绑定操作*

\*Mar 19 05:28:32:877 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Finish bind as user.

*// 以用户身份进行绑定完成*

\*Mar 19 05:28:32:902 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Processing LDAP

 authenticaion.

*// LDAP认证操作*

\*Mar 19 05:28:32:902 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Data of authent

ication reply successfully obtained, resultCode: 0.

*// LDAP认证成功*

\# 一台主机通过Console口连接设备，设备使用LDAP作为认证方案对登录用户进行身份认证，但是未配置login-dn，打开LDAP的错误调试信息开关。用户通过Console口登录设备的操作时，设备输出如下调试信息。

\<Sysname\> debugging ldap error

\*Jan  1 07:57:03:173 2011 Sysname LDAP/7/ERROR:

PAM_LDAP: Anonymous binding not supported.

*// 不支持匿名绑定*

\*Jan  1 07:57:03:174 2011 Sysname LDAP/7/ERROR:

PAM_LDAP:Failed to get user information.

*// 获取用户信息失败*

**AAA调试命令 \-- AAA调试命令 \-- debugging local-server**

------------------------------------------------------------------------

【命令】

**[debugging local-server**[ { **all** \| **error** \| **event** }]]

**[undo debugging local-server **[{ **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging local-serve**r]命令用来打开Local-Server的调试信息开关。**undo debugging  local-server**命令用来关闭Local-Server的调试信息开关。

缺省情况下，Local-Server的调试信息开关处于关闭状态。

表1-7 debugging local-server error命令输出信息列表

字段

描述

Authentication request processing error: Failed to parse authentication attribute.

认证处理错误：解析认证属性失败

Authentication processing error: Failed to encapsulate reply message.

认证处理错误：封装应答消息失败

Authentication processing error: Failed to send reply message.

认证处理错误：发送应答消息失败

Authorization processing error: Failed to encapsulate reply message.

授权处理错误：封装应答消息失败

Authorization processing error: Failed to get user authorization attribute.

授权处理错误：获取用户授权属性失败

Authorization request processing error: Failed to parse request message.

授权处理错误：解析请求消息失败

Authorization processing error: Failed to send reply message.

授权处理错误：发送应答消息失败

表1-8 debugging local-server event命令输出信息描述表

字段

描述

Authentication failed, unexpected caller number *call-num1* (expected = *call-num2*).

认证失败，*call-num1*不是期望的主叫号码，期望的主叫号码是*call-num2*

Authentication failed, unexpected MAC address *mac1* (expected = *mac2*).

认证失败，*mac1*不是期望的MAC地址，期望的MAC地址是*mac2*

Authentication failed, unexpected VLAN ID *vlan-id1* (expected = *vlan-id2*).

认证失败，*vlan-id1*不是期望的VLAN ID，期望的VLAN ID是*vlan-id2*

Authentication failed, unexpected IP address *ip-addr1* (expected = *ip-addr2*).

认证失败，*ip-addr1*不是期望的IP地址，期望的IP地址是*ip-addr2*

Authentication failed, unexpected port *port1* (expected = *port2*).

认证失败，*port1*不是期望的端口，期望的端口是*port2*

Authentication failed, unexpected slot number *slot-num1* (expected = *slot-num2*).

认证失败，*slot-num1*不是期望的槽位号，期望的槽位号是*slot-num2*

Authentication failed, unexpected subslot number *subslot-num1* (expected = *subslot-num2*).

认证失败，*subslot-num1*不是期望的子槽号，期望的子槽号是*subslot-num2*

Authentication succeeded.

认证成功

Authentication failed, user *user-name* doesn\'t exist.

认证失败，用户*user-name*不存在

Authentication failed, user\'s state is block.

认证失败，用户的状态是阻塞

Authentication failed, user password is wrong.

认证失败，用户口令错误

Authentication failed, unexpected user service type *service1* (expected = *service2*).

认证失败，*service1*不是期望的服务类型，期望的服务类型是*service2*

Authorization succeeded.

授权成功

Authorization failed, user *user-name* doesn\'t exist.

授权失败，用户*user-name*不存在

Authorization failed, the user\'s state is block

授权失败，用户的状态是阻塞

Authorization failed, unexpected user service type *service1* (expected = *service2*).

授权失败，*service1*不是期望的服务类型，期望的服务类型是*service2*

Received authentication request message.

收到认证请求消息

Received authorization request message.

收到授权请求消息

【举例】

\# 在设备上配置Telnet类型的本地用户test，对其使用本地认证方案进行身份认证，并打开Local-Server的事件调试信息开关。当用户test使用Telnet登录设备时，设备上输出如下调试信息：

\<Sysname\> debugging local-server event

\*Jun 11 15:30:20:805 2011 Sysname LOCALSRV/7/EVENT: -MDC=1;

*// 本地服务器接受到认证请求消息*

 Received authentication request message.

\*Jun 11 15:30:20:805 2011 Sysname LOCALSRV/7/EVENT: -MDC=1;

 Authentication succeeded.

*// 认证成功*

\*Jun 11 15:30:20:806 2011 Sysname LOCALSRV/7/EVENT: -MDC=1;

 Received authorization request message.

*// 本地服务器接收到授权请求消息*

\*Jun 11 15:30:20:806 2011 Sysname LOCALSRV/7/EVENT: -MDC=1;

 Authorization succeeded.

*// 授权成功*

**

\# 在设备上配置Telnet类型的本地用户test，对其使用本地认证方案进行身份认证，并打开Local-Server的错误调试信息开关。当用户test使用SSH登录设备时，设备解析认证属性失败，输出如下调试信息。

\<Sysname\> debugging local-server error

\*Jun 11 15:33:21:002 2011 Sysname LOCALSRV/7/ERROR: -MDC=1;

  Authentication request processing error: Failed to parse authentication attribute.

*// 解析认证属性失败*

**AAA调试命令 \-- AAA调试命令 \-- debugging radius**

------------------------------------------------------------------------

【命令】

**[debugging radius ** { **all** \| **event** \| **error** \| **packet** }  [ **acl** *acl-number* \| **user** *username* ]]

**[undo debugging radius ** { **all** \| **event** \| **error** \| **packet** }]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

**[all**]：所有调试信息开关。

**[event**]：表示事件调试信息开关。

**[error**]：表示错误调试信息开关。

**[packet**]：表示报文调试信息开关。

**[acl ***acl-number*]：指定匹配RADIUS调试信息的ACL规则。其中，*acl-number*表示ACL编号，取值范围为2000～3999。该参数可多次设置，但仅最后一次合法的配置生效。指定的ACL规则中仅源IP地址信息用于匹配用户IP，其他信息不做匹配项。

**[user ***username*]：指定匹配RADIUS调试信息的部分用户名。其中，*username*表示部分用户名，为1～80个字符的字符串，区分大小写。该参数用于匹配上线用户的完整用户名中的部分连续字符串。

【描述】

**[debugging radius**]命令用来打开RADIUS调试信息开关。**undo debugging radius**命令用来关闭RADIUS调试信息开关。

缺省情况下，RADIUS调试信息开关处于关闭状态。

表1-9 debugging radius event命令输出信息描述表

字段

描述

Processing AAA request data.

处理AAA请求数据

Got request data successfully, primitive: *primitive_name*.

成功获取请求数据，原语是*primitive_name*

Getting local server info.

获取本地服务器信息

Getting RADIUS server info.

获取远端RADIUS服务器信息

Got RADIUS server info successfully.

成功获取服务器信息

Sent request packet and create request context successfully.

成功发送请求报文并创建请求上下文

Added request context to global table successfully.

成功将请求上下文加入全局上下文信息表

Created request context successfully.

成功创建请求上下文

Composed request packet successfully.

成功构建请求报文

Created response timeout timer successfully.

成功创建应答超时定时器

Sent request packet successfully.

成功发送请求报文

Created request packet successfully, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id.*

成功创建请求报文，目的IP地址是*dst-ip*，目的端口是*dst-port*，套接字是*fd*，报文ID是*id*

Added packet socketfd to epoll successfully, socketFd: *fd*.

成功添加报文套接字到epoll控制变量中，套接字是*fd*

Mapped PAM item to RADIUS attribute successfully.

成功将PAM数据项映射为RADIUS属性

Filled RADIUS attributes in packet successfully.

成功填充RADIUS报文属性

Got RADIUS username format successfully.

成功获取RADIUS用户名格式

Added attribute user-name successfully, user-name: *name*.

成功添加用户名属性，属性值是*name*

Response timed out.

应答超时

Found request context, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id*.

成功查找到请求上下文，目的IP地址是*dst-ip*，目的端口是*dst-port*，套接字是*fd*，报文ID是*id*

Retransmitting request packet, currentTries: *n*, maxTries: *max*.

重传请求报文，当前是第*n*次重传，最大重传次数是*max*

Sent reply error message to PAM.

发送应答错误消息给PAM

Reached the maximum retries.

达到最大重传次数

Sent packet to next server successfully.

成功发送报文到下一个服务器

Failed to get next server.

获取下一个服务器失败

Got next server successfully, serverIP: *svr-ip*, serverPort: *svr-port*.

成功获取下一个服务器，服务器IP地址为*svr-ip*，服务器端口为*svr-port*

Set status of server to block successfully.

成功将服务器状态设置为阻塞

Set status of server to active successfully.

成功将服务器状态设置为激活

Reply SocketFd recieved EPOLLIN event.

应答报文套接字接收到EPOLLIN事件

Reply SocketFd recieved EPOLLERR/EPOLLHUP event.

应答报文套接字接收到EPOLLERR/EPOLLHUP事件

Sent reply message successfully.

成功发送应答消息

Received reply packet succuessfully.

成功接收应答报文

Found request context, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id*.

成功查找到请求上下文，目的IP地址是*dst-ip*，目的端口是*dst-port*，套接字是*fd*，报文ID是*id*

The reply packet is valid.

应答报文有效

Decoded reply packet successfully.

应答报文解码成功

PAM_RADIUS: Processing RADIUS authentication.

进行RADIUS认证

PAM_RADIUS: Processing RADIUS authorization.

进行RADIUS授权

PAM_RADIUS: RADIUS authorization successful.

RADIUS授权成功

PAM_RADIUS: RADIUS accounting started.

RADIUS计费开始

PAM_RADIUS: RADIUS accounting stopped.

RADIUS计费结束

PAM_RADIUS: RADIUS accounting updated.

RADIUS计费更新

PAM_RADIUS: Sent *type* request successfully.

成功发送认证/授权/计费请求

PAM_RADIUS: Received authentication reply message, resultCode: *code*.

接收到认证应答消息，结果码为*code*

PAM_RADIUS: Received authorization reply message, resultCode: *code*.

接收到授权应答消息，结果码为*code*

PAM_RADIUS: Received accounting-start reply message, resultCode: *code*.

接收到计费开始应答消息，结果码为*code*

PAM_RADIUS: Received accounting-stop reply message, resultCode: *code*.

接收到计费停止应答消息，结果码为*code*

PAM_RADIUS: Received accounting-update reply message, resultCode: *code*.

接收到计费更新应答消息，结果码为*code*

Processed session-control packet successfully.

处理session-control报文成功

Processed session-control message successfully.

处理session-control消息成功

Sent session-control reply packet successfully.

成功发送session-control应答报文

Sent DAE reply packet successfully.

成功发送DAE 应答报文

Received DAE request packet successfully.

成功接收DAE请求报文

Failed to distinguish DAE request packet.

识别DAE请求报文失败

The length of DAE request packet is invalid.

DAE请求报文长度无效

The type of DAE request packet is unknown.

DAE请求报文类型未知

The authenticator of DAE request packet is invalid.

DAE请求报文校验字无效

Created detection request packet successfully, dstIP: *dst-ip*, dstPort: *dst-port*, VPN instance: *vpn-instance*, socketFd: *fd*, pktID: *id*.

成功创建探测请求报文，目的IP地址是*dst-ip*，目的端口是*dst-port*，所属的MPLS L3VPN实例是*vpn-instance*，套接字是*fd*，报文ID是*id*

Found detection request context, dstIP: *dst-ip*, dstPort: *dst-port*, pktID: *id*.

成功查找到探测请求上下文，目的IP地址是*dst-ip*，目的端口是*dst-port*，报文ID是*id*

Opened RADIUS server detection successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

成功开启RADIUS服务器探测，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to open RADIUS server detection, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

开启RADIUS服务器探测失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Created detection request context successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

成功创建探测请求上下文，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to create detection request context, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

创建探测请求上下文失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Composed detection request packet successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

成功构建探测请求报文，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Sent detection request packet successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

成功发送探测请求报文，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to send detection request packet, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

发送探测请求报文失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to save  packet ID of detection request, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

保存探测请求报文ID失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Random timer of server detection timed out, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

服务器探测的随机定时器超时，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to clear flag of sending trap, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

清除发送trap标记失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to clear count of block state, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

清除block状态计数失败， RADIUS方案名是*scheme-name*，服务器IP地址是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to update count of block state, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

更新block状态计数失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

No detection reply packet received, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

没有接收到探测应答报文，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Server detection timer timed out, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

服务器探测定时器超时，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Sent trap successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

发送trap成功，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to set flag of sending trap, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

设置发送trap标记失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Closed RADIUS server detection successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

成功关闭RADIUS服务器探测，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to close RADIUS server detection, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

关闭RADIUS服务器探测失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Can't open RADIUS server detection because the specified test profile doesn\'t exist, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

不能开启RADIUS服务器探测，指定的探测模版不存在，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Opened RADIUS server quiet function successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

成功开启RADIUS服务器静默，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to open RADIUS server quiet function,  RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

开启RADIUS服务器静默失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Closed RADIUS server quiet function successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

成功关闭RADIUS服务器静默，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to close RADIUS server quiet function, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

关闭RADIUS服务器静默失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Aaad Sent the notification about the change of server status to application process successfully, server state:*server-state*.

Aaad发送了服务器状态转换的通知给应用进程，服务器状态是*server-state*

Application process received the notification about the change of server status from aaad process, server state:*server-state*. 

应用进程接收了来自aaad进程的服务器状态转换的通知，服务器状态是*server-state*

表1-10 debugging radius error命令输出信息描述表

字段

描述

Failed to get request data.

获取请求数据失败

Failed to get server info.

获取服务器信息失败

Failed to send request packet and create request context.

发送请求报文和创建请求上下文失败

Failed to create request context.

创建请求上下文失败

Failed to compose request packet.

组装请求报文失败

Failed to create response timeout timer.

创建应答超时定时器失败

Failed to send request packet, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id.*

发送请求报文失败，目的IP地址是*dst-ip*，目的端口是*dst-port*，套接字是*fd*，报文ID是*id*

Failed to create request packet.

创建请求报文失败

Failed to add packet socketfd to epoll, socketFd: *fd*.

将报文套接字加入epoll控制变量失败，套接字是*fd*

Failed to map PAM item to attribute.

将PAM数据项映射到RADIUS属性失败

Failed to fill attribute in packet.

填充报文属性失败

Failed to get RADIUS username format.

获取RADIUS用户名格式失败

Faild to get domain item.

获取ISP域数据项失败

The username length exceeded the upper limt.

用户名长度超过最大值

Failed to retransmit request packet *n* times.

第*n*次重发请求报文失败

Failed to set the status of server to active.

设置服务器到激活状态失败

Failed to fill reply data.

填充应答数据失败

Failed to send reply message.

发送应答消息失败

Failed to recieve reply packet.

发送应答报文失败

Failed to find request context, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id*.

查找请求上下文失败，目的IP地址是*dst-ip*，目的端口是*dst-port*，套接字是*fd*，报文ID是*id*

The reply packet is invalid.

应答报文无效

Failed to decode reply packet.

解码应答报文失败

Reply packet: Unknown type.

应答报文：未知类型

Reply packet: Invalid packet length.

应答报文：无效的报文长度

Reply packet: Invalid packet authenticator.

应答报文：无效的报文验证字

Failed to map attribute to PAM item.

将RADIUS属性映射成PAM数据项失败

PAM_RADIUS: Failed to set scheme name to pam-module-data.

PAM_RADIUS：设置方案名称到PAM数据失败

PAM_RADIUS: Local authorization failed.

PAM_RADIUS：本地授权失败

PAM_RADIUS: Failed to get reply data from pam-module-data.

PAM_RADIUS：从PAM数据获取应答数据失败

PAM_RADIUS: Authorization scheme is RADIUS, but authentication is local.

PAM_RADIUS：授权方案是RADIUS，但认证方案是local

PAM_RADIUS: Authorization scheme is different from authentication scheme.

PAM_RADIUS：授权方案与认证方案不同

PAM_RADIUS: Authorization failed for setting PAM item.

PAM_RADIUS：设置PAM数据项失败导致授权失败

PAM_RADIUS: Failed to find sequence.

PAM_RADIUS：查找序列失败

PAM_RADIUS: Failed to find reply data.

PAM_RADIUS：查找应答数据失败

PAM_RADIUS: Failed to send *type* request.

PAM_RADIUS：发送认证/授权/计费请求失败

PAM_RADIUS: Failed to set port item.

PAM_RADIUS：设置端口数据项失败

PAM_RADIUS: Failed to accept connection for receiving *type* reply data.

PAM_RADIUS：接收认证/授权/计费应答数据的连接失败

PAM_RADIUS: Failed to select available socket for receiving *type* reply data.

PAM_RADIUS：选择可用的套接字失败

PAM_RADIUS: Failed to receive *type* reply data.

PAM_RADIUS：接收认证/授权/计费应答数据失败

PAM_RADIUS: Failed to process reply data.

PAM_RADIUS：处理应答数据失败

PAM_RADIUS: Failed to open socket when processing *type* request.

处理认证/授权/计费请求时，打开套接字失败

PAM_RADIUS: Failed to send *type* request.

发送认证/授权/计费请求失败

Failed to process session-control packet.

处理session-control报文失败

Failed to process session-control message.

处理session-control消息失败

Failed to receive session-control packet.

接收session-control报文失败

Session-control packet is invalid.

session-control报文无效

Checking session-control packet failed.

检查session-control报文失败

Failed to decode session-control packet.

解码session-control报文失败

Failed to find attribute hw-command.

查找hw-command属性失败

Failed to send session-control message to aaad.

向aaad发送session-control消息失败

Failed to decode session-control reply message.

解码session-control应答消息失败

Failed to send session-control reply packet.

发送session-control应答报文失败

Failed to send DAE reply packet.

发送DAE应答报文失败

Failed to decode DAE reply message.

解码DAE应答报文失败

Failed to receive DAE request packet.

接收DAE请求报文失败

Failed to decode DAE request packet.

解码DAE请求报文失败

Failed to send server state notify message for multi RADIUS scheme name.

发送多个RADIUS方案名称的server state通知消息失败。

Failed to send server state notify message for single RADIUS scheme name, RADIUS scheme name: scheme-name.

发送单个RADIUS方案名称的server state通知消息失败，RADIUS方案名称: scheme-name。

Failed to create detection request packet, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

创建探测请求报文失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to fill RADIUS attributes in detection request  packet, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

向探测请求报文中填充RADIUS报文属性失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

Failed to get NAS-IP, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*

获取NAS-IP失败，RADIUS方案名是*scheme-name*，服务器IP地址是*server-ip*，服务器端口号是*server-port*，服务器所属的MPLS L3VPN实例是*vpn-instance*

表1-11 debugging radius packet命令输出信息描述表

字段

描述

RADIUS attribute name = *attribute value*

报文中包含的RADIUS属性及其取值。

其中RADIUS属性遵从RFC2865/2866/2869/3580描述，不再赘述；另外还支持一些厂商定制属性（Vender Specific Attribute），在下面单独描述

3Com-User-Access-Level = *level*

3Com用户访问级别为*level*，取值为0～3

H3c-Ftp-Directory = *dir*

H3c-Ftp用户工作路径为*dir*

H3c-Exec-Privilege = *level*

H3c-Exec用户访问级别为*level*，取值为0～15

Hw-Ftp-Directory = *dir*

H3c-Ftp用户工作路径为*dir*

Hw-Exec-Privilege = *level*

Hw-Exec用户访问级别为*level*，取值为 0～15

H3c-Local-Service-Type = *type*

Type取值及其涵义为：

·1：DVPN

·2：FTP

·3：网络接入类型（802.1X、MAC地址认证）

·4：PAD

·5：SSH

·6：Telnet

·7：Terminal

·8：Portal

·9：PPP

·10：L2TP

·11：命令行

【举例】

\# 在一台设备上配置Login用户的认证方案为RADIUS认证、授权，并打开RADIUS事件调试信息开关。当有一个Console用户登录本设备时，输出如下调试信息。

\<Sysname\> debugging radius event

\*Dec 31 16:04:36:438 2009 Sysname RADIUS/7/EVENT:

PAM_RADIUS: Processing RADIUS authentication.

*// 进行RADIUS认证*

\*Jan  3 02:17:27:660 2011 Sysname RADIUS/7/EVENT:

PAM_RADIUS: Sent authentication request successfully.

*// 成功发送认证请求*

\*Jan  3 02:17:27:667 2011 Sysname RADIUS/7/EVENT:

Processing AAA request data.

*// 处理AAA请求数据*

\*Jan  3 02:17:27:667 2011 Sysname RADIUS/7/EVENT:

Got request data successfully, primitive: authentication.

*// 成功接收到用户的认证请求，原语是认证*

\*Jan  3 02:17:27:668 2011 Sysname RADIUS/7/EVENT:

Getting RADIUS server info.

\*Jan  3 02:17:27:669 2011 Sysname RADIUS/7/EVENT:

Got RADIUS server info successfully.

*// 成功获取RADIUS服务器信息*

\*Jan  3 02:17:27:669 2011 Sysname RADIUS/7/EVENT:

Created request context successfully.

*// 成功创建请求上下文*

\*Jan  3 02:17:27:670 2011 Sysname RADIUS/7/EVENT:

Created request packet successfully, dstIP: 192.168.0.244, dstPort: 1812, VPN in

stance: \--(public), socketFd: 23, pktID: 61.

*// 成功创建认证请求报文，目的地址是192.168.0.244，目的端口是1812，VPN实例是public，套接字是23，报文ID是61*

\*Jan  3 02:17:27:671 2011 Sysname RADIUS/7/EVENT:

Added packet socketfd to epoll successfully, socketFd: 23.

\*Jan  3 02:17:27:672 2011 Sysname RADIUS/7/EVENT:

Mapped PAM item to RADIUS attribute successfully.

*// 成功将PAM数据项映射为RADIUS属性*

\*Jan  3 02:17:27:673 2011 Sysname RADIUS/7/EVENT:

Got RADIUS username format successfully, format: 2.

\*Jan  3 02:17:27:674 2011 Sysname RADIUS/7/EVENT:

Added attribute user-name successfully, user-name: test.

*// 成功添加用户名属性，属性值是test*

\*Jan  3 02:17:27:674 2011 Sysname RADIUS/7/EVENT:

Filled RADIUS attributes in packet successfully.

*// 成功填充报文属性，并构建认证请求报文*

\*Jan  3 02:17:27:675 2011 Sysname RADIUS/7/EVENT:

Composed request packet successfully.

\*Jan  3 02:17:27:675 2011 Sysname RADIUS/7/EVENT:

Created response timeout timer successfully.

*// 成功创建应答超时定时器*

\*Jan  3 02:17:27:679 2011 Sysname RADIUS/7/EVENT:

Sent request packet successfully.

\*Jan  3 02:17:27:679 2011 Sysname RADIUS/7/EVENT:

Sent request packet and create request context successfully.

*// 成功发送认证请求报文，并创建请求上下文*

\*Jan  3 02:17:27:680 2011 Sysname RADIUS/7/EVENT:

Added request context to global table successfully.

*// 成功将请求上下文加入全局上下文信息表*

\*Jan  3 02:17:27:714 2011 Sysname RADIUS/7/EVENT:

Reply SocketFd recieved EPOLLIN event.

\*Jan  3 02:17:27:715 2011 Sysname RADIUS/7/EVENT:

Received reply packet succuessfully.

*// 接收到应答报文*

\*Jan  3 02:17:27:716 2011 Sysname RADIUS/7/EVENT:

Found request context, dstIP: 192.168.0.244, dstPort: 1812, VPN instance: \--(pub

lic), socketFd: 23, pktID: 61.

*// 查找到请求上下文*

\*Jan  3 02:17:27:717 2011 Sysname RADIUS/7/EVENT:

The reply packet is valid.

\*Jan  3 02:17:27:718 2011 Sysname RADIUS/7/EVENT:

Decoded reply packet successfully.

*// 应答报文有效，对应答报文解码成功*

\*Jan  3 02:17:27:719 2011 Sysname RADIUS/7/EVENT:

Sent reply message successfully.

*[//*]*成功发送应答消息*

\*Jan  3 02:17:27:719 2011 Sysname RADIUS/7/EVENT:

PAM_RADIUS: Fetched authentication reply-data successfully, resultCode: 0

\*Jan  3 02:17:27:720 2011 Sysname RADIUS/7/EVENT:

PAM_RADIUS: Received authentication reply message, resultCode: 0

*// 收到认证应答消息*

\*Jan  3 02:17:27:721 2011 Sysname RADIUS/7/EVENT:

PAM_RADIUS: Processing RADIUS authorization.

*// 开始进行RADIUS授权*

\*Jan  3 02:17:27:724 2011 Sysname RADIUS/7/EVENT:

PAM_RADIUS: RADIUS Authorization successfully.

*[// RADIUS*]*授权请求成功*

\*Jan  3 02:17:27:743 2011 Sysname RADIUS/7/EVENT:

PAM_RADIUS: RADIUS accounting started.

*[// RADIUS*]*计费开始*

\*Jan  3 02:17:27:744 2011 Sysname RADIUS/7/EVENT:

Processing AAA request data.

\*Jan  3 02:17:27:744 2011 Sysname RADIUS/7/EVENT:

PAM_RADIUS: Sent accounting-start request successfully.

\*Jan  3 02:17:27:744 2011 Sysname RADIUS/7/EVENT:

Got request data successfully, primitive: accounting-start.

*// 成功获取计费请求数据，原语是开始计费*

\*Jan  3 02:17:27:745 2011 Sysname RADIUS/7/EVENT:

Getting RADIUS server info.

\*Jan  3 02:17:27:745 2011 Sysname RADIUS/7/EVENT:

Got RADIUS server info successfully.

*// 成功获取服务器信息*

\*Jan  3 02:17:27:746 2011 Sysname RADIUS/7/EVENT:

Created request context successfully.

\*Jan  3 02:17:27:747 2011 Sysname RADIUS/7/EVENT:

Created request packet successfully, dstIP: 192.168.0.244, dstPort: 1813, VPN in

stance: \--(public), socketFd: 23, pktID: 184.

*// 成功创建计费开始请求报文，目的IP地址是192.168.0.244，目的端口号是1813，VPN实例是public，套接字是23，报文ID是184*

\*Jan  3 02:17:27:747 2011 Sysname RADIUS/7/EVENT:

Added packet socketfd to epoll successfully, socketFd: 23.

\*Jan  3 02:17:27:749 2011 Sysname RADIUS/7/EVENT:

Mapped PAM item to RADIUS attribute successfully.

\*Jan  3 02:17:27:749 2011 Sysname RADIUS/7/EVENT:

Got RADIUS username format successfully, format: 2.

\*Jan  3 02:17:27:750 2011 Sysname RADIUS/7/EVENT:

Added attribute user-name successfully, user-name: test.

*// 成功添加用户名属性，属性值是test*

\*Jan  3 02:17:27:751 2011 Sysname RADIUS/7/EVENT:

Filled RADIUS attributes in packet successfully.

\*Jan  3 02:17:27:751 2011 Sysname RADIUS/7/EVENT:

Composed request packet successfully.

*// 成功填充报文属性，并构建请求报文*

\*Jan  3 02:17:27:752 2011 Sysname RADIUS/7/EVENT:

Created response timeout timer successfully.

*// 成功创建应答超时定时器*

\*Jan  3 02:17:27:754 2011 Sysname RADIUS/7/EVENT:

Sent request packet successfully.

\*Jan  3 02:17:27:754 2011 Sysname RADIUS/7/EVENT:

Sent request packet and create request context successfully.

\*Jan  3 02:17:27:755 2011 Sysname RADIUS/7/EVENT:

Added request context to global table successfully.

\*Jan  3 02:17:27:755 2011 Sysname RADIUS/7/EVENT:

Reply SocketFd recieved EPOLLIN event.

\*Jan  3 02:17:27:756 2011 Sysname RADIUS/7/EVENT:

Received reply packet succuessfully.

*// 成功接收到计费应答报文*

\*Jan  3 02:17:27:757 2011 Sysname RADIUS/7/EVENT:

Found request context, dstIP: 192.168.0.244, dstPort: 1813, VPN instance: \--(pub

lic), socketFd: 23, pktID: 184.

*// 成功查找到计费应答报文对应的请求上下文，目的IP地址是192.168.0.244；目的端口号是1646；套接字是14；报文ID是0*

\*Jan  3 02:17:27:758 2011 Sysname RADIUS/7/EVENT:

The reply packet is valid.

\*Jan  3 02:17:27:759 2011 Sysname RADIUS/7/EVENT:

Decoded reply packet successfully.

*// 计费应答报文有效，对计费应答报文解码成功*

\# 在一台设备上配置Login用户的认证方案为RADIUS认证、授权、计费，并打开RADIUS报文调试信息开关。当有一个Console用户登录本设备时，输出如下调试信息。

\<Sysname\> debugging radius packet

\*Jan  3 02:33:18:686 2011 Sysname RADIUS/7/PACKET:

    User-Name=\"rbac\"

    User-Password=\*\*\*\*\*\*

    Service-Type=Login-User

    Framed-IP-Address=192.168.0.17

    NAS-IP-Address=192.168.0.16

*// 认证请求报文中的属性列表*

\*Jan  3 02:33:18:690 2011 Sysname RADIUS/7/PACKET:

 01 ed 00 3e 44 13 50 f2 54 58 6f e8 39 e9 05 ff

 6c 7e 18 a3 01 06 72 62 61 63 02 12 71 a1 e1 46

 cc a2 77 97 a4 95 57 54 db f6 3b 0b 06 06 00 00

 00 01 08 06 c0 a8 00 11 04 06 c0 a8 00 10

*// 发送的access-request报文原始信息*

\*Jan  3 02:33:18:707 2011 Sysname RADIUS/7/PACKET:

    Service-Type=Login-User

    Session-Timeout=86400

    Login-Service=Telnet

*[// access-accept*]*应答报文的属性列表*

\*Jan  3 02:33:18:708 2011 Sysname RADIUS/7/PACKET:

 02 ed 00 26 71 d9 71 09 75 7b af d9 2d fc 10 59

 4d ee 66 ae 06 06 00 00 00 01 1b 06 00 01 51 80

 0f 06 00 00 00 00

*[// access-accept*]*报文的原始数据*

\*Jan  3 02:33:18:727 2011 Sysname RADIUS/7/PACKET:

    User-Name=\"rbac\"

    Framed-IP-Address=192.168.0.17

    Acct-Session-Id=\"000000032011-01-03:02:33:18-0000000101\"

    Login-Service=Telnet

    Acct-Authentic=RADIUS

    NAS-IP-Address=192.168.0.16

    Acct-Status-Type=Start

    Acct-Delay-Time=0

    Event-Timestamp=\"Jan  3 2011 02:33:18 UTC\"

*// 计费开始请求报文中的属性列表*

\*Jan  3 02:33:18:729 2011 Sysname RADIUS/7/PACKET:

 04 3c 00 6c 21 aa 18 4e 38 c8 60 f1 12 76 97 26

 e2 04 d8 28 01 06 72 62 61 63 08 06 c0 a8 00 11

 2c 28 30 30 30 30 30 30 30 33 32 30 31 31 2d 30

 31 2d 30 33 3a 30 32 3a 33 33 3a 31 38 2d 30 30

 30 30 30 30 30 31 30 31 0f 06 00 00 00 00 2d 06

 00 00 00 01 04 06 c0 a8 00 10 28 06 00 00 00 01

 29 06 00 00 00 00 37 06 4d 21 35 6e

*// 计费开始请求报文原始数据*

\*Jan  3 02:33:18:731 2011 Sysname RADIUS/7/PACKET:

 05 3c 00 14 5f 8f 2f e7 21 86 a7 db 52 b3 39 09

 86 92 80 b0

*// 计费应答报文原始数据*

**

\# 在一台设备上配置Login用户的认证方案为本地认证、RADIUS授权，并打开RADIUS错误调试信息开关。当有一个Console用户登录本设备时，输出如下调试信息。

\<Sysname\> debugging radius error

\*Dec 31 16:04:41:324 2009 Sysname RADIUS/7/ERROR:

PAM_RADIUS: Failed to get reply-data from pam-module-data..

*// 从PAM数据获取应答数据失败*
