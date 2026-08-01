<!-- CMD-INDEX
  debugging sslvpn                    | 用户视图             | L6
  debugging khttp                     | 用户视图             | L2182
-->

**SSL VPN \-- SSL VPN调试命令 \-- debugging sslvpn**

------------------------------------------------------------------------

【命令】

**[debugging**[ **sslvpn** { **all** \| **aaa** \| **error** \| **event** \| **fsm** \| **packet** [ **verbose** ] \| **timer** }]]

**[undo**[ **debugging sslvpn** { **all** \| **aaa** \| **error** \| **event** \| **fsm** \| **packet** [ **verbose** ] \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示SSL VPN所有调试信息开关。

**[aaa**]：表示SSL VPN认证调试信息开关

**[error**]：表示SSL VPN错误调试信息开关。

**[event**]：表示SSL VPN事件调试信息开关。

**[fsm**]：表示SSL VPN状态机调试信息开关。

**[packet**]：表示SSL VPN报文调试信息开关。

**[verbose**]：表示SSL VPN报文详细信息调试信息开关。如果不指定本参数，则表示SSL VPN报文简要信息调试信息开关。

**[timer**]：表示SSL VPN定时器调试信息开关。

【描述】

**[debugging** **sslvpn**]命令用来打开SSL VPN调试信息开关。**undo** **debugging** **sslvpn**命令用来关闭SSL VPN调试信息开关。

缺省情况下，SSL VPN调试信息开关处于关闭状态。

表1-1 debugging sslvpn aaa命令输出信息描述表

字段

描述

Failed to send offline request to kernel. contextID: *contextID*; onlineID: *onlineID.*

通知内核下线请求失败，*contextID*为下线请求所属的Context，*onlineID*为需要下线的在线用户ID

 

Parse the private information in the authentication request. original length: *original-length*, decode length: *decode-length*.

解析认证请求中的私有信息，*original-length*为私有信息的原始长度，*decode-length*为私有信息解码后的长度

 

Set pam user IPv4 *ipv4-address*. result: *result*.

向pam设置用户的IPv4地址，*ipv4-address*为设置的IPv4地址，*result*为设置结果

 

Set pam user IPv6 *ipv6-address*. result: *result*.

向pam设置用户的IPv6地址，*ipv6-address*为设置的IPv6地址，*result*为设置结果

 

Set pam server string. length: *length*; result: *result*.

向pam设置服务属性，*length*为服务属性的长度，*result*为设置结果

 

Set pam user MAC *mac-address*. result: *result*.

向pam设置用户的MAC地址，*mac-address*为设置的MAC地址，*result*为设置结果

 

Authorizing policy group: *name*.

认证的policy group名称

 

Deleted accounting update timer. contextID: *contextID*; onlineID: *onlineID*.

删除计费更新定时器，*contextID*为定时器所属的Context，*onlineID*为定时器对应的在线用户ID

 

Deleted accounting session timer. contextID: contextID; onlineID: *onlineID*.

删除计费会话定时器，*contextID*为定时器所属的Context，*onlineID*为定时器对应的在线用户ID

 

Succeeded in updating accounting. contextID: *contextID*; onlineID: *onlineID*.

更新计费成功，*contextID*为更新计费所属的Context，*onlineID*为对应的在线用户ID

 

Failed to update accounting. contextID: *contextID*; onlineID: *onlineID*.

更新计费失败，*contextID*为更新计费所属的Context，*onlineID*为对应的在线用户ID

 

Accounting update timer timed out. contextID: *contextID*; onlineID: *onlineID*.

计费更新定时器超时，*contextID*为定时器所属的Context，*onlineID*为定时器对应的在线用户ID

 

Succeeded in creating accounting update timer. contextID: *contextID*; onlineID: *onlineID*.

创建计费更新定时器成功，*contextID*为定时器所属的Context，*onlineID*为定时器对应的在线用户ID

 

Failed to create accounting update time. contextID: *contextID*; onlineID: *onlineID*.

创建计费更新定时器失败，*contextID*为定时器所属的Context，*onlineID*为定时器对应的在线用户ID

 

Accounting session timer timed out. contextID: *contextID*; onlineID: *onlineID*.

计费会话定时器超时，*contextID*为定时器所属的Context，*onlineID*为定时器对应的在线用户ID

 

Succeeded in creating accounting session timer. contextID: *contextID*; onlineID: *onlineID*.

创建计费会话定时器成功，*contextID*为定时器所属的Context，*onlineID*为定时器对应的在线用户ID

 

Failed to create accounting session timer. contextID: *contextID*; onlineID: *onlineID*.

创建计费会话定时器失败，*contextID*为定时器所属的Context，*onlineID*为定时器对应的在线用户ID

 

Accounting started. contextID: *contextID*; onlineID: *onlineID*.

开始计费，*contextID*为所属的Context，*onlineID*为对应的在线用户ID

 

Processed asynchronous authentication response. contextID: *contextID*; requestID: *requestID*; result: *result*.

处理异步认证应答，*contextID*为认证应答所属的Context，*requestID*为认证应答对应的上线请求ID， *result*为认证应答消息的处理结果

 

Processed asynchronous authorization response. contextID: *contextID*; onlineID: *onlineID*; result: *result*.

处理异步授权应答，*contextID*为授权应答所属的Context，*onlineID*为授权应答对应的在线用户ID，*result*为授权应答消息的处理结果

 

Processed asynchronous accounting start response. contextID: *contextID*; onlineID: *onlineID*; result: *result*.

处理异步计费开始应答，*contextID*为计费开始应答所属的Context，*onlineID*为计费开始应答对应的在线用户ID，*result*为计费开始应答消息的处理结果

 

Processed asynchronous accounting stop response. contextID: *contextID*; onlineID: *onlineID*; result: *result*.

处理异步计费结束应答，*contextID*为计费结束应答所属的Context，*onlineID*为计费结束应答对应的在线用户ID，*result*为计费结束应答消息的处理结果

 

Processed asynchronous accounting update response. contextID: *contextID*; onlineID: *onlineID*; result: *result*.

处理异步计费更新应答，*contextID*为计费更新应答所属的Context，*onlineID*为计费更新应答对应的在线用户ID，*result*为计费更新应答消息的处理结果

 

Authentication timeout. contextID: *contextID*; requestID: *requestID*.

认证请求超时，*contextID*为认证请求所属的Context，*requestID*为认证请求对应的上线请求ID

 

Begin to add request online node. contextID: *contextID*; requestID: *requestID*.

开始进行上线请求处理，*contextID*为上线请求所属的Context，*requestID*为上线请求对应的上线请求ID

 

Succeeded in adding request online node. contextID: *contextID*; requestID: *requestID*; username: *username*.

成功添加上线请求节点，*contextID*为上线请求所属的Context，*requestID*为上线请求对应的上线请求ID，*username*为上线请求的用户名

 

Deleted online node. contextID: *contextID*; onlineID: *onlineID*.

删除上线节点，*contextID*为上线节点所属的Context，*onlineID*为上线节点对应的在线用户ID

 

Move online node. contextID: *contextID*; requestID: *requestID*; onlineID: *onlineID*.

上线请求节点转为上线节点，*contextID*为上线请求节点所属的Context，*requestID*为上线请求节点的上线请求ID，*onlineID*为上线节点的上线ID。

 

Activated Context *contextID*.

激活Context，*contextID*为对应的Context

 

Inactivated Context *contextID*.

去激活Context，*contextID*为对应的Context

 

Send offline request to daemon. contextID: *contextID*; onlineID: *onlineID*; result: *result*.

向守护进程发送下线请求，*contextID*为下线请求所属的Context，*onlineID*为请求下线的在线ID，*result*为发送请求结果

 

Send online request to daemon. contextID: *contextID*; requestID: *requestID*; result: *result*.

向守护进程发送上线请求，*contextID*为上线请求所属的Context，*requestID*为请求上线的请求ID，*result*为发送请求结果

 

Send client IP info to daemon. contextID: *contextID*; onlineID: *onlineID*; result: *result*.

向守护进程发送客户端IP，*contextID*为所属的Context，*onlineID*为客户端对应的在线ID，*result*为发送结果

 

Failed to get the common name from the certificate.

从证书中获取common name失败

 

Certificate common name is *name*.

证书中的common name为*name*

 

Certificate authentication succeeded. contextID: *contextID*; onlineID: *onlineID*.

证书认证成功，*contextID*为所属的Context，*onlineID*为对应的在线ID

 

User *name* authentication request.

用户认证请求，*name*为发起认证请求的用户名

 

Web login request.

通过浏览器发起登录请求

 

Failed to get request content from web.

处理浏览器登录请求，获取请求信息失败

 

Web logout request.

通过浏览器发起登出请求

 

Online check. No session ID.

上线检查处理，获取SSL VPN会话信息失败

 

Online check. sessionID: *sessionID*.

上线检查处理，SSL VPN会话ID为*sessionID*

 

Online check. onlineID: *onlineID*.

上线检查处理，用户上线ID为*onlineID*

 

Failed to get MIME when log in.

处理客户端登录请求时，分配MIME失败

 

Failed to get request content when log in.

处理客户端登录请求时，获取请求信息失败

 

Authentication request. result: *result*; client MAC: *mac-address*; private info length: *length*.

认证请求信息，*result*为获取请求信息的结果，*mac-address*为客户端MAC地址，*length*为私有信息长度

 

Client login request.

通过客户端发起登录请求

 

Client logout request.

通过客户端发起登出请求

 

Client online check. onlineID: *onlineID*.

客户端上线检查，*onlineID*客户端对应的用户在线ID

 

Authentication success. context: *contextID*; requestID: *requestID*.

认证成功，*contextID*为认证所在的Context，*requestID*认证成功的请求ID

 

The number of online users has reached the limit. context: *contextID*; requestID: *requestID*.

在线用户数目已经达到最大数，*contextID*为达到在线用户数上限的Context，*requestID*为当前请求上线的请求ID

 

Authentication failed. context: *contextID*; requestID: *requestID*; result: *result*.

认证失败，*contextID*为认证失败的Context，*requestID*为当前请求上线的请求ID，*result*为失败原因

 

Authorization succeeded context: *contextID*; onlineID: *onlineID*; policy group: *PGroupid*.

授权成功，*contextID*为授权成功的Context，*onlineID*为当前在线用户ID，*PGroupid*为授权的策略组ID

 

Succeeded in refreshing authorization information. context: *contextID*; onlineID: *onlineID*; policy group: *PGroupid*.

成功更新授权信息，*contextID*为授权的Context，*onlineID*为当前在线用户ID，*PGroupid*为授权更新后的策略组ID

 

Authorization failed. context: *contextID*; onlineID: *onlineID*; result: *result*.

授权失败，*contextID*为授权失败的Context，*onlineID*为当前在线用户ID，*result*为失败原因

 

Accounting succeeded. context: *contextID*; onlineID: *onlineID*.

计费成功，*contextID*为计费成功的Context，*onlineID*为当前在线用户ID

 

Accounting failed. context: *contextID*; onlineID: *onlineID*; result: *result*.

计费失败，*contextID*为计费失败的Context，*onlineID*为当前请求上线的ID，*result*为失败原因

 

Offline process. context: *contextID*; onlineID: *onlineID*.

下线处理，*contextID*为下线处理的Context，*onlineID*为当前在线的ID

 

Failed to allocate onlineID. context: *contextID*; requestID: *requestID*.

分配在线用户ID失败，*contextID*为分配在线用户ID的Context，*requestID*为当前请求上线的请求ID

 

表1-2 debugging sslvpn error命令输出信息描述表

字段

描述

Failed to send authentication error to kernel. contextID: *contextID*; requestID: *requestID*.

通知内核认证失败时发生错误，*contextID*为认证请求的Context，*requestID*为请求上线的请求ID

 

Failed to send context *contextID* idle timer to kernel.

空闲定时器超时，通知内核失败，*contextID*为定时器所在的Context

 

Failed to send context *contextID* authentication exception timer to kernel.

认证请求异常定时器超时，通知内核失败，*contextID*为定时器所在的Context

 

DNS query *hostname* failed.

DNS查找失败，*hostname*为要查找的主机名

 

DNS connection closed.

与DNS的连接断开

 

Failed to create the data of SSL server policy *ssl-policy*.

根据服务器策略生成SSL数据失败，*ssl-policy*为SSL服务器端策略名

 

Failed to send the data of SSL server policy *ssl-policy*. error code: *error-code*; total length: *length1*; sent length: *length2*; sending length *length3*.

SSL数据下内核失败，*ssl-policy*为SSL策略名，*error-code*为下内核失败原因，*length1*为SSL数据的总长度，*length2*为已经下内核的SSL数据长度，*length3*为发生失败时下内核的SSL数据长度。

 

Failed to add port forward list to kernel.

通知内核添加端口转发列表失败

 

Failed to delete port forward list from kernel.

通知内核删除端口转发列表失败

 

Failed to add local port to kernel.

通知内核添加local port配置失败

 

Failed to delete local port from kernel.

通知内核删除local port配置失败

 

Failed to add refer port forward to kernel.

通知内核添加port forward list引用配置失败

 

Failed to delete refer port forward from kernel.

通知内核删除port forward list引用配置失败

 

Failed to send validated code timer to kernel.

验证码定时器超时，通知内核失败

 

Failed to update input statistic.

更新input方向统计信息失败

 

Link output with invalid index.

IPAC转发业务中收到报文的出接口为非法接口索引

 

The number of loops (*LoopTimes*) reached the limit.

报文在本机环回的次数达到上限，*LoopTimes*为报文在本机的环回次数

 

Failed to load result *ResultCode* (*language*) string.

加载输出信息失败，*ResultCode*为错误码，*language*为加载语言

 

Failed to set cookie svpnuid *sessionID*.

设置Cookie失败，*sessionID*为要设置到Cookie中的会话ID

 

Failed to set the header of client connection response.

设置客户端连接应答报文的首部失败

 

Failed to add a context.

添加Context失败

 

Failed to add a refrenced gateway for the context.

添加Context引用Gateway失败

 

Failed to delete a reference gateway from the context.

删除Context引用Gateway失败。

 

Failed to modify context gateway..

修改Context引用Gateway失败。

 

Failed to enable a context.

Context使能失败

 

Failed to enable validated code.

验证码使能失败

 

Failed to enable dynamic password.

动态口令使能失败

 

Failed to disable dynamic password.

动态口令去使能失败

 

Failed to enable certificate anthentication function.

使能证书认证功能失败

 

Failed to disable certificate anthentication function.

关闭证书认证功能失败

 

Failed to add default policy group.

添加缺省策略组失败

 

Failed to delete default policy group.

删除缺省策略组失败

 

Failed to modify the max number of users.

修改最大用户数失败

 

Failed to process vpn instance in context.

Context下处理**vpn-instance**命令失败

 

Failed to add an EMO (Endpoint Mobile Office) server.

添加EMO服务器失败

 

Failed to delete an EMO (Endpoint Mobile Office) server.

删除EMO服务器失败

 

Failed to enable context log.

使能Context下的syslog失败

 

Failed to disable context log.

去使能Context下的syslog失败

 

Failed to set redirect response of client.

设置客户端重定向应答报文失败

 

Failed to set the header of client domain list. response

设置客户端domain list应答报文的首部失败

 

Failed to get gateway when getting client information.

处理客户端信息时，获取Gateway失败

 

Failed to get the match context when getting client information.

处理客户端信息时，获取匹配的Context失败

 

Failed to get URL when processing domain list request.

处理domain list请求报文，获取URL失败

 

Failed to get gateway when checking web query.

浏览器登录，检查请求信息时，获取Gateway失败

 

Failed to match context when checking web query.

浏览器登录，检查请求信息时，匹配Context失败

 

Failed to get URL when processing input header.

处理报文首部时，获取URL失败

 

Failed to get URL when processing error web.

浏览器请求error页面，获取URL失败。

 

Failed to get URL when checking context for web.

浏览器访问，检查Context是否使能时，获取URL失败

 

Failed to get gateway when match context.

匹配Context时获取Gateway失败

 

Failed to deliver parse body.

分发解析报文体失败

 

Failed to find pattern for deliver.

报文分发时，查找匹配模式失败

 

Failed to build pattern string *string*.

构建模式匹配信息失败，*string*为要匹配的字符串

 

Failed to set HTTP header field.

封装HTTP报文头域失败

 

Invalid method in request.

请求报文中的方法非法

 

Failed to get user name.

获取用户名失败

 

Failed to add user name.

添加用户名失败

 

Failed to get host header.

获取host首部失败

 

Failed to add host header.

添加host首部失败

 

Failed to get host name.

获取主机名失败

 

Failed to add host name.

添加主机名失败

 

Failed to add time data.

添加时间信息失败

 

Failed to add data to MBUF.

向MBUF添加数据失败

 

Failed to get file becaust user had no authority.

获取文件失败，失败原因是用户没有权限

 

Failed to open file.

打开文件失败

 

Failed to get file state.

获取文件状态失败

 

Failed to read file file.

读取文件失败

 

Failed to add a gateway.

添加Gateway失败

 

Failed to set gateway IP address.

设置Gateway的IP地址失败

 

Failed to enable a gateway.

Gateway使能失败

 

Failed to set SSL server policy.

设置SSL服务器端策略失败

 

Failed to set HTTP redirect.

设置HTTP重定向失败

 

Failed to clear HTTP redirect.

清除HTTP重定向失败

 

Failed to process vpn instance in gateway.

Gateway下处理**vpn-instance**命令失败

 

Failed to find context *id*.

查找Context失败，*id*为要查找的Context ID

 

Failed to add a route list *id*.

添加路由列表失败，*id*为路由列表的ID

 

Failed to add a route to route list *id*.

向路由列表添加路由失败，*id*为路由列表的ID

 

Failed to update output statistics.

更新出方向统计信息失败

 

IPAC: Failed to get IP packet information.

IP代理：获取报文IP信息失败

 

IPAC: Failed to get match IP form ACL.

IP代理：获取匹配的ACL规则失败

 

IPAC: Failed to check ip tunnel acl.

IP代理：ACL规则检查失败

 

IPAC: IP connection error.

IP代理：连接错误

 

IPAC: Failed to receive data from IP connection.

IP代理：从连接上接收数据失败

 

IPAC: Failed to add data to packet. length: *length*; value: *value*.

IP代理：向报文中添加数据失败，*length*为要添加的数据长度，*value*为要添加的数据内容

 

IPAC: Failed to get gateway address.

IP代理：获取Gateway地址失败

 

IPAC: Failed to get server.

IP代理：获取Server失败

 

IPAC: Failed to get IP resource.

IP代理：获取IP代理资源失败

 

IPAC: Failed to hand shake because VPN instance does not exist.

IP代理：握手协商失败，原因是VPN不存在

 

IPAC: Failed to allocate IP address.

IP代理：分配IP地址失败

 

IPAC: Failed to add peer.

IP代理：添加Peer数据失败

 

IPAC: Failed to send reply packet.

IP代理：发送应答报文失败

 

Failed to reference an address pool.

引用地址池失败

 

Failed to add a policy group.

添加策略组失败

 

Failed to add an address pool.

添加地址池失败

 

Failed to add a port forward list *id*.

添加端口转发列表失败，*id*为端口转发列表的ID

 

Failed to add a local port *port*.

添加local port失败，*port*为要添加的本地端口

 

Failed to add local port node in kernel resource.

内核资源添加local port失败

 

HTTP Redirect: Failed to get gateway.

HTTP重定向：获取Gateway失败

 

HTTP Redirect: Failed to get gateway port.

HTTP重定向：获取Gateway的端口失败

 

HTTP Redirect: Received request without host.

HTTP重定向：接收的请求报文中没有host首部

 

HTTP Redirect: Received request without URI.

HTTP重定向：接收的请求报文中没有URI信息

 

HTTP Redirect: Failed to create response packet.

HTTP重定向：创建应答报文失败

 

HTTP Redirect: Failed to set header.

HTTP重定向：封装首部信息失败

 

Failed to find resource list: *id*.

获取资源列表失败，*id*为列表ID

 

Failed to add resource list in kernel. listID: *id*.

内核资源添加资源列表失败，*id*为列表ID

 

Loading other SSL server policy *name*.

正在下发其他SSL服务器端策略，*name*为正在下发的SSL服务器端策略名

 

Updating SSL server policy *name* with invalid offset.

下发更新SSL服务器端策略时，数据偏移错误，*name*为正在下发的SSL服务器端策略名

 

Failed to set SSL server context.

设置SSL服务策略上下文数据失败

 

Invalid SSL data length.

SL服务策略文数据长度非法

 

Failed to create SSL server policy *name.*

创建SSL服务器端策略失败，*name*为要创建的SSL服务器端策略名

 

Static redirect error.

静态页面重定向错误

 

Static set head field failed.

静态页面设置头域错误

 

Static receive request with invalid method.

静态页面收到的请求报文携带了非法的方法

 

Failed to set login message.

设置login信息失败

 

Failed to set title message.

设置title信息失败

 

Failed to set logo.

设置logo失败

 

Failed to add VPN instance *id*.

添加VPN实例失败，*id*为VPN实例ID

 

WebAC: Failed to get source IP address.

Web代理：获取源IP地址失败

 

WebAC: Failed to get match ip form acl.

Web代理：匹配ACL规则失败

 

WebAC: Failed to check authorization.

Web代理：检查授权失败

 

WebAC: Failed to connect server.

Web代理：连接服务器失败

 

WebAC: Failed to create FTCP connection.

Web代理：创建FTCP连接失败

 

WebAC: Failed to resolve server name.

Web代理：解析服务器域名失败

 

WebAC: Failed to get request URL.

Web代理：获取请求URL失败

 

WebAC: Failed to parse request URL.

Web代理：解析请求URL失败

 

WebAC: Server host name was too long.

Web代理：服务器主机名超长

 

WebAC: Failed to allocate WebAC.

Web代理：申请Web代理节点失败

 

WebAC: Failed to run finite state machine.

Web代理：运行有限状态机失败

 

TCPAC: Failed to get TCPAC node index.

TCP代理：获取TCP代理节点索引失败

 

TCPAC: Failed to response TCP client.

TCP代理：向TCP客户端回复应答失败

 

TCPAC: Failed to connect remote server.

TCP代理：连接远端服务器失败

 

TCPAC: Client connection error.

TCP代理：与客户端的连接发送错误

 

TCPAC: Failed to resolve server name.

TCP代理：解析服务器域名失败

 

TCPAC: Failed to get server from HTTP header.

TCP代理：从HTTP头域中获取服务器信息失败

 

TCPAC: Failed to get server by resource *id.*

TCP代理：根据资源ID获取服务器信息失败

 

TCPAC: Failed to parse resource.

TCP代理：解析资源信息失败

 

TCPAC: Failed to check authorization in handshake.

TCP代理：握手过程中检查授权失败

 

TCPAC: Failed to get source IP address.

TCP代理：获取源IP地址失败

 

TCPAC: Failed to get match ip form acl.

TCP代理：匹配ACL规则失败

 

TCPAC: Failed to get remote server.

TCP代理：获取远端服务器失败

 

TCPAC: Failed to get VPN instance.

TCP代理：获取VPN实例失败

 

TCPAC: No authority for TCP access.

TCP代理：TCP接入没有被授权

 

TCPAC: Failed to create TCPAC.

TCP代理：创建TCP代理节点失败

 

TCPAC: Failed to connect remote server.

TCP代理：连接远端服务器失败

 

TCPAC: Failed to handshake.

TCP代理：TCP握手失败

 

Failed to get context by context ID.

根据ID查找Context失败

 

Failed to get context by context name.

根据名字查找Context失败

 

表1-3 debugging sslvpn event命令输出信息描述表

字段

描述

Succeeded in creating the data of SSL server policy *name*, total length *length*..

成功创建SSL服务器端策略数据，*name*为SSL服务器端策略名，*length*为创建的数据长度

 

TCPAC connection hasn\'t been created.

TCP代理连接还没有完成

 

Succeeded in adding wadj for *interface-name*.

成功添加指定出接口的邻接表，* interface-name*为出接口名称

 

Failed to add wadj for *interface-name*.

添加指定出接口的邻接表失败，*interface-name*为出接口名称

 

Succeeded in deleting adj for *interface-name*.

成功删除指定出接口的邻接表，*interface-name*为出接口名称

 

Failed to delete adj for *interface-name*.

删除指定出接口的邻接表失败，*interface-name*为出接口名称

 

Succeeded in adding a context.

添加Context成功

 

Succeeded in adding context gateway.

添加Context引用Gateway成功

 

Succeeded in deleting context gateway.

删除Context引用Gateway成功

 

Succeeded in modifying context gateway.

修改Context引用Gateway成功

 

Succeeded in enabling a context.

Context使能成功

 

Succeeded in enabling validated code.

验证码使能成功

 

Succeeded in enabling dynamic password.

动态口令使能成功

 

Succeeded in disabling dynamic password.

动态口令去使能成功

 

Succeeded in enabling certificate anthentication.

证书认证使能成功

 

Succeeded in disabling certificate anthentication.

证书认证去使能成功

 

Succeeded in adding a default policy group.

添加缺省策略组成功

 

Succeeded in deleting the default policy group.

删除缺省策略组成功

 

Succeeded in modifying the max number of users.

修改最大用户数成功

 

Succeeded in processing VPN instance in context.

Context下处理vpn instance命令成功

 

Succeeded in adding an EMO (Endpoint Mobile Office) server.

添加EMO服务器成功

 

Succeeded in deleting the EMO (Endpoint Mobile Office) server.

删除EMO服务器成功

 

Succeeded in enabling context log.

使能Context下的syslog成功。

 

Succeeded to disabling context log.

去使能Context下的syslog成功。

 

Request domain list when checking context for web.

浏览器请求domain list页面

 

Request error when checking context for web.

浏览器请求error页面

 

Succeeded in matching the only context.

成功匹配到唯一引用的Context

 

Succeeded in matching context by virtual-host *host-name*.

通过虚拟主机名*host-name*成功匹配到Context

 

Succeeded in matching context by domain *domain-name*.

通过域名*domain-name*成功匹配到Context

 

Succeeded in matching default context.

成功匹配到默认Context

 

Succeeded in saving dynamic web file information.

成功保存动态Web页面信息

 

Succeeded in adding a user name *name*.

成功添加用户名*name*

 

Succeeded in adding time *time*.

成功添加时间信息*time*

 

Succeeded in deleting a user customized file.

成功删除用户自定义文件

 

Succeeded in reading file. read length: *length*.

成功读取文件，文件长度为*length*

 

Succeeded in enabling a gateway.

Gateway使能成功

 

Succeeded in disabling a gateway.

Gateway去使能成功

 

Succeeded in adding a gateway.

添加Gateway成功

 

Succeeded in setting gateway IP address.

设置Gateway的IP地址成功

 

Succeeded in enabling a gateway.

Gateway使能成功

 

Succeeded in setting SSL server policy.

设置SSL服务器端策略成功

 

Succeeded in clearing SSL server policy.

删除SSL服务器端策略成功

 

Succeeded in setting HTTP redirect.

设置HTTP重定向成功

 

Succeeded in clearing HTTP redirect.

删除HTTP重定向成功

 

Succeeded in processing VPN instance in gateway.

Gateway下处理vpn instance命令成功

 

Succeeded in adding a route list *id*.

添加路由列表成功，*id*为路由列表ID

 

Succeeded in adding a route to route list *id*.

向路由列表添加路由成功，*id*为路由列表ID

 

IPAC: No IP tunnel acl resource.

IP代理：没有配置IP代理ACL规则

 

IPAC: The ACL check result is *result*.

IP代理：ACL规则检查结果为*result*

 

The IP address range is from *start-address* to *end-address* and the mask is *mask*.

分配的IP地址范围为从*start-address*到*end-address*，IP地址的掩码为*mask*

 

The first subnet address range is from *start-address* to *end-address*.

第一个地址子区间

 

Succeeded in allocating address *ip-address* from *start-address* to *end-address*.

从IP地址范围*start-address*到*end-address*中成功分配地址*ip-address*

 

Succeeded in referring all routes.

成功引用所有路由

 

Succeeded in referring a route.

成功引用一条路由

 

Succeeded in refering a route list.

成功引用一个路由列表

 

Succeeded in refering an address pool.

成功引用一个地址池

 

Succeeded in clearing an address pool.

成功清除一个地址池

 

Succeeded in adding a policy group.

成功添加一个策略组

 

Succeeded in adding an address pool.

成功添加一个地址池

 

Succeeded in deleting an address pool.

成功删除一个地址池

 

Succeeded in adding a port forward list *id*.

添加端口转发列表*id*成功

 

Succeeded in deleting a port portfwd list *id*.

删除端口转发列表*id*成功

 

Succeeded in adding a local port *port*.

添加本地端口*port*成功

 

Succeeded in receiving the data of SSL server policy *name*. total length: *length1*; received length: *length2*; receiving length: *length3*.

成功接收到SSL服务器端策略*name*的数据，*length1*为SSL数据的总长度，*length2*为已经接收的SSL数据长度，*length3*为正在接收的SSL数据长度

 

Succeeded in setting SSL server context.

设置SSL服务策略上下文数据成功

 

Succeeded in setting login message.

设置login信息成功

 

Succeeded in setting title message.

设置title信息成功

 

Succeeded in setting logo.

设置logo成功

 

Deleted context *context-id* from VPN *vpn-id*.

从VPN实例*vpn-id*内删除Context *context-id*

 

Failed to get VPN instance *id*.

获取VPN实例*vpn-id*失败

 

WebAC: No web ACL resource.

Web代理：没有配置Web代理ACL规则

 

WebAC: The acl check result *result*

Web代理：ACL规则检查结果为*result*

 

TCPAC: Succeeded in connecting remote server.

TCP代理：成功连接远端服务器

 

TCPAC: Connecting remote server *server.*

TCP代理：连接远端服务器，*server*为远端服务器域名或者IP地址

 

TCPAC: Get a local port resource %u from list %u.

TCP代理：从资源列表中获取资源节点

 

TCPAC: Get resource description *description*.

TCP代理：获取资源描述信息*description*

 

TCPAC: No TCP ACL resource.

TCP代理：没有配置TCP代理ACL规则

 

TCPAC: The acl check result *result*.

TCP代理：ACL规则检查结果为*result*

 

表1-4 debugging sslvpn timer命令输出信息描述表

字段

描述

Offline for idle timeout. contextID: *id*; onlineID: *id*.

空闲定时器超时，触发下线，*contextID*为下线请求所属的Context，*onlineID*为需要下线的在线用户ID

 

Failed to log in for exception timeout. contextID: *id*; requestID: *id*.

异常定时器超时，登录失败，*contextID*为上线请求所属的Context，*requestID*为上线请求ID

 

表1-5 debugging sslvpn packet命令输出信息描述表

字段

描述

IPAC: Failed to input packet for interface link status was down.

IP代理：Input报文失败，原因是接口链路状态是Down

 

IPAC: Failed to forward packet by IP.

IP代理：通过IP转发报文失败

 

Client connection request.

客户端连接请求

 

Default context receive request body.

默认Context接收请求报文体。

 

Match domain of context is *domain*.

匹配到Context下的Domain。

 

Deliver receive body overflow.

分发时接收的报文体长度超过最大长度

 

Deliver to *pattern*.

分发到特定模式，*pattern*为模式描述

 

Deliver receive a body.

分发时接收报文体

 

Deliver receive a request without URL.

分发时接收的请求报文中没有URL信息

 

Deliver receive request. method: *method*; URL: *url*.

分发时接收到请求报文，报文中的方法为*method*、URL为*url*

 

Deliver receive a request with bad body type.

分发时接收的请求报文中携带的报文体类型是非法值

 

DNS resolved host *host* to address *ip-address*.

DNS将主机名*host*解析为IP地址*ip-address*

 

Received a client request with invalid file, and redirected it to a new file.

客户端请求的文件不存在，重定向到新的文件

 

The URL in the request is *url*.

请求报文中的URL为*url*

 

IPAC: Failed to output.

IP代理：Output报文失败

 

IPAC: Failed to get interface referenced by context *id*.

IP代理：获取Context引用的SSLVPN-AC接口失败

 

IPAC: *interface* is not associated with the context *id*.

IP代理：报文的入接口与Context引用的接口不同

 

IPAC: Failed to get VPN instance.

IP代理：获取VPN实例失败

 

IPAC: Failed to get connect from peer.

IP代理：从连接上获取peer数据失败

 

IPAC: Failed to prepend packet.

IP代理：预处理报文失败

 

IPAC: Failed to forward packet.

IP代理：转发报文失败

 

IPAC: Failed to output IPAC packet for interface link status was down.

IP代理：Output报文失败，原因是接口链路状态是Down

 

IPAC: Failed to get peer data.

IP代理：获取Peer数据失败

 

IPAC: Received a keepalive packet from *ip-address*.

IP代理：收到IP地址为*ip-address*.的客户端发送的保活报文

 

IPAC: Received a data packet fragmentation with *length1* bytes. totle length: *length2*.

IP代理：接收到IP数据报文的分片，长度为*length1*，报文的总长度为*length2*

 

IPAC: Failed to input packet by interface *interface-name*.

IP代理：通过指定接口Input报文失败

 

IPAC: Received an incomplete network extended packet with *length* bytes.

IP代理：收到的网络扩展报文长度没有达到最小长度

 

IPAC: Received a packet with unknown type from client.

IP代理：从客户端收到报文的扩展类型是未知的类型

 

IPAC: Added data to packet. length: *length*; value: *value*.

IP代理：向报文中添加数据，*length*为要添加的数据长度，*value*为要添加的数据内容

 

IPAC: Received a packet without authentication.

IP代理：接收报文未认证

 

IPAC: Received a packet with invalied User-Agent.

IP代理：接收到的报文携带非法的User-Agent字段

 

Failed to allocate peer node because VPN instance doesn\'t exist.

申请peer节点失败，原因是VPN实例不存在

 

Added peer *peer-address*. VPN instance: *id*.

在VPN实例内添加peer节点*peer-address*

 

Found peer *peer-address*.

查找到peer节点*peer-address*

 

Failed to find peer *peer-address* in VPN instance *id*.

在VPN实例内查找peer节点*peer-address*失败

 

Delete peer *peer-address*.

删除peer节点*peer-address*

 

HTTP Redirect: Recvived a request. host: *host*; URI: *uri*.

HTTP重定向：接收到请求报文

 

HTTP Redirect: Set location *uri*.

HTTP重定向：设置重定向路径为*uri*

 

Static receive request. url: *url*.

静态页面接收请求

 

The validate code was not needed.

没有打开验证码功能

 

Failed to get validate code.

获取验证码失败

 

The validate code was timed out.

验证码超时

 

The validate code was invalide.

验证码错误

 

Found VPN instance *id*.

查找VPN实例

 

WebAC: Return *result* to trans for down write event.

Web代理：向KHTTP模块返回down连接写事件处理结果，处理结果为*result*

 

WebAC: Response Header: *header.*

Web代理：应答报文首部信息为*header*

 

WebAC: Received a request. URL: *url*.

Web代理：接收到请求报文，请求报文的URL为*url*

 

表1-6 debugging sslvpn packet verbose命令输出信息描述表

字段

描述

*[Interface*] *operator* packet: *string*

接收或发送IP接入的报文

*[Interface*]为处理报文的接口名，如SSLVPN-AC1

*[operator*]用来说明报文的方向，取值包括：

·input：IP代理从客户端接收报文，转发到服务器

·output：IP代理从服务器接收报文，转发到客户端

*[string*]为报文具体内容

 

表1-7 debugging sslvpn fsm命令输出信息描述表

字段

描述

WebAC: State changed from *state1* to *state2*.

Web代理：状态从*state1*切换到*state2*

 

WebAC: Handle event *event* in *state* state.

Web代理：在状态*state*处理事件*event*

 

【举例】

\# 打开SSL VPN AAA调试信息开关。使用IP客户端连接SSL VPN网关时，打印以下调试信息。

\<Sysname\> debugging sslvpn aaa

Authentication request. result: 0x0; client MAC: 1cbd-b9e3-b142; private info length: 32.

*[//*]*解析认证请求中的信息*

\# 打开SSL VPN ERROR调试信息开关。创建SSL VPN Context，如果发生错误，打印以下调试信息。

\<Sysname\> debugging sslvpn error

\*Oct 11 06:50:45:602  2014 H3C SSLVPN/7/SSLVPN_ERROR: -MDC=1; Failed to add a context.

*// 创建Context失败*

\# 打开SSL VPN EVENT调试信息开关。使用IP客户端连接SSL VPN网关时，打印以下调试信息。

\<Sysname\> debugging sslvpn event

\*Oct 11 06:50:45:602 2014 H3C SSLVPN/7/SSLVPN_EVENT: -MDC=1; Succeed in matching default context.

*// 连接请求报文匹配到默认Context*

\# 打开SSL VPN TIMER调试信息开关。创建SSL VPN Context，如果发生错误，打印以下调试信息。

\<Sysname\> debugging sslvpn timer

\*Oct 11 06:50:45:602  2014 H3C SSLVPN/7/SSLVPN_TIMER: -MDC=1; Offline for idle timeout. contextID: 0x3; onlineID: 0x1.

*// 空闲定时器检查到用户老化，请求下线*

\# 打开SSL VPN PACKET调试信息开关。使用IP客户端连接SSL VPN网关时，打印以下调试信息。

\<Sysname\> debugging sslvpn packet

\*Oct 11 06:59:57:747 2014 H3C SSLVPN/7/SSLVPN_PACKET: -MDC=1; Deliver receive request, method:NET_EXTEND, url:/

*[//*]*分发时接收到请求报文，报文中的方法为NET_EXTEND，请求的URL为"/"*

\# 打开SSL VPN PACKET VERBOSE调试信息开关。使用IP客户端连接SSL VPN网关时，打印以下调试信息。

\<Sysname\> debugging sslvpn packet verbose

\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1;  SSLVPN-AC1 input packet:                                            

\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 45 00 00 60  00 0c 00 00  80 11 11 6e  0a 0a 0a 01                   

\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 0a 0a 0a ff  00 89 00 89  00 4c 90 54  fd 47 29 10                    

\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 00 01 00 00  00 00 00 01  20 45 4d 44  41 44 49 44                   

\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 46 44 43 44  47 45 42 43  41 43 41 43  41 43 41 43                   

\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 41 43 41 43  41 43 41 43  41 00 00 20  00 01 c0 0c                   

\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 00 20 00 01  00 04 93 e0  00 06 60 00  0a 0a 0a 01

*[// SSLVPN-AC1*]*接收到input报文及具体报文内容。*

\# 打开SSL VPN [FSM]调试信息开关。使用Web代理方式连接SSL VPN网关时，打印以下调试信息。

\<Sysname\> debugging sslvpn fsm

\*Oct 11 06:50:45:602 2014 H3C SSLVPN/7/SSLVPN_EVENT: -MDC=1; WebAC: Handle event UP OUT in state Connecting.

*[// Web*]*代理，在Connecting状态处理UP OUT事件*

**SSL VPN \-- SSL VPN调试命令 \-- debugging khttp**

------------------------------------------------------------------------

【命令】

**[debugging**[ **khttp** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

**[undo**[ **debugging** **khttp** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示KHTTP所有调试信息开关。

**[error**]：表示KHTTP错误调试信息开关。

**[event**]：表示KHTTP事件调试信息开关。

**[fsm**]：表示KHTTP状态机调试信息开关。

**[packet**]：表示KHTTP报文调试信息开关。

【描述】

**[debugging** **khttp**]命令用来打开KHTTP调试信息开关。**undo** **debugging** **khttp**命令用来关闭KHTTP调试信息开关。

缺省情况下，KHTTP调试信息开关处于关闭状态。

表1-8 debugging khttp error命令输出信息描述表

字段

描述

Failed to close server *server-address/port* in VPN *id*.

关闭VPN实例下的服务器失败，服务器的地址为*server-address*、端口号为*port*

 

Failed to set SSL context to server *server-address/port* in VPN *id*.

设置VPN实例下服务器使用的SSL上下文失败

 

Repeated to open server *server-address/port* in VPN *id*.

重复打开VPN实例下的服务器

 

Failed to listen server *server-address/port* in VPN *id*.

监听VPN实例下的服务器失败

 

Failed to add server* server-address/port* in VPN *id*.

在VPN下添加服务器失败

 

Failed to create a new SSL connection.

创建新的SSL连接失败

 

SSL connect failed because SSL handle is invalid.

由于SSL句柄非法，SSL连接失败

 

Failed to connect SSL server.

连接SSL服务器失败

 

Failed to accept SSL connection because SSL handle is invalid.

由于SSL句柄非法，接受SSL连接失败

 

Failed to accept SSL connection.

接受SSL连接失败

 

Failed to connect to server *server-address/port*in VPN*id*.

连接VPN实例内的服务器失败

 

Failed to connect to SSL server*server-address/port *in VPN *id*.

连接VPN实例内的SSL服务器失败

 

Failed to accept a new FTCP handle.

接受新FTCP句柄失败

 

Failed to create a connection. TCP: *handle*.

从TCP创建连接失败

 

Failed to accept a new handle.

接受新句柄失败

 

Failed to create a connection: TCP= *handle* SSL= *handle*.

创建连接失败

 

Failed to bind TCP handle:* X.X.X.X/port* in VPN *id*.

绑定TCP句柄失败

 

Failed to listen: *X.X.X.X/port* in VPN *id*..

监听失败

 

Failed to create TCP handle..

创建TCP句柄失败。

 

Failed to set service type tcp*handle*.

设置TCP服务类型失败。

 

Failed to create a connection tcp*handle*.

创建TCP连接失败。

 

Failed to add server for the MDC is invalid.

MDC非法，添加服务器失败

 

Failed to add server for the data of MDC is invalid.

MDC下数据非法，添加服务失败

 

Failed to add server because of insufficient resource.

内存不足，添加服务失败

 

Body receive: There is not a dispatch.

体接收，没有注册分发处理函数。

 

State(*state*) of transaction could not run phase.

Transaction的当前状态不能进行状态切换

 

Receive HTTP request with invalid content-length.

接收HTTP请求报文携带了无效的Content-length字段

 

Transaction, Direction=Request, Parse result=Failed, Parse length=*length*.

Transaction解析报文异常信息

 

Failed to merge packet data (*length*).

合并Mbuf失败

 

Failed to combine data(*length*) with the previous data(*length*).

连接Mbuf失败

 

Head send: Failed to analyse sending type.

头发送，判断发送类型失败

 

Body send: Failed to prepend buffer.

体发送，扩展MBuf失败

 

Body send: Failed to fill chunk.

体发送，填充chunk封装失败。

 

表1-9 debugging sslvpn event命令输出信息描述表

字段

描述

Succeeded in setting SSL context to server: *server-address/port* in VPN *id*.

设置VPN实例下服务器使用的SSL上下文成功

 

Succeeded in closing server: %s in VPN *id*.

关闭VPN实例下的服务器成功

 

Succeeded in adding server: %s in VPN *id*.

添加VPN下的服务成功。

 

Succeeded in creating a new SSL connection: %#lx.

创建新的SSL连接成功

 

Succeeded in connecting SSL server.

连接SSL服务器成功

 

SSL connection(write) was not completed.

SSL连接写操作过程中

 

SSL connection(read) was not completed.

SSL连接读操作过程中

 

Succeeded in accepting SSL connection.

成功接受SSL连接

 

SSL connection is being created.

SSL连接建立过程中

 

Connection received input event: TCP *handle* *string*.

TCP连接接收到Input事件

 

Connection received output event: TCP *handle* *string*.

TCP连接接收到Output事件

 

Succeeded in connecting server *server-address/port*.

连接服务器成功

 

Connection received error event *error*. TCP *handle* *string*.

TCP连接接收到Error事件

 

Connected to server *server-address/port* in VPN *id*.

连接VPN实例内的服务器成功

 

Connected to SSL server *server-address/port* in VPN *id*.

连接VPN实例内的SSL服务器成功

 

Succeeded in accepting a connection: *string*.

成功接受一个连接

 

Succeeded in accepting a SSL connection: *string* SSL=*handle*.

成功接受一个SSL连接

 

Succeeded in listening a connection: %s in VPN %u.

监听VPN实例下的服务连接成功

 

Connection closed.

连接关闭

 

Connection has been deleted.

连接已经被删除

 

Not enough memory resource.

内存不足

 

Memory resource is restored.

内存资源恢复

 

Body send: Succeeded in sending body.

体发送，发送体成功

 

Transaction has been deleted.

Transaction已经被删除

 

表1-10 debugging sslvpn packet命令输出信息描述表

字段

描述

Body receive: the dispatch result of body-in(*result*) event is *event*.

体接收，body-in事件的分发结果。

 

Body receive: Received a null body.

体接收：接收到空体

 

Body receive: Received body.

体接收：接收到体

 

Header receive: the dispatch result of head-ok event is *result*.

头接收，head-ok事件的分发结果

 

Parse a header: *string*, value: *string*.

解析一个HTTP首部

 

Delete old header: *string*, value: *string*.

删除旧的HTTP首部

 

Encapsulate a header: *string*, value: *string*.

封装HTTP首部

 

Encapsulate response code: *id* *string*.

封装HTTP应答码

 

Received a packet with *length* bytes on the conncetion.

在连接上接收到*length*字节的报文

 

Query: *string*.

HTTP报文的请求信息为*string*

 

URI: *uri*.

HTTP报文的URI为*uri*

 

Transaction, Direction=Request, State=%s \--\> %s, Parse Length=%ld.

Transaction状态切换及解析报文信息

 

Header send: Succeeded in sending header.

头发送：发送头成功

 

Transaction finished.

Transaction结束

 

Transaction has been closed.

Transaction已经关闭

 

【举例】

\# 打开KHTTP ERROR调试信息开关。配置冲突时重复打开一个server，打印以下调试信息。

\<Sysname\> debugging khttp error

\*Sep 19 09:55:52:338 2014 H3C KHTTP/7/ERROR: Repeated to open server: 192.168.10.109/443 in VPN 0.

*// 提示相应server已经打开*

\# 打开KHTTP EVENT调试信息开关。连接SSL VPN服务时，打印以下调试信息。

\<Sysname\> debugging khttp event

\*Oct 11 09:30:27:572 2014 H3C KHTTP/7/EVENT: -MDC=1; Connection received input event: [TCP e9e94000 Local=192.168.10.109:443, Peer=0.0.0.0:0.]

*// 连接接收到Input事件。*

\#打开KHTTP PACKET调试信息开关。连接SSL VPN服务时，打印以下调试信息。

\<Sysname\> debugging khttp packet

\*Oct 11 09:30:31:609 2014 H3C KHTTP/7/PACKET: -MDC=1; Parse a Head: Accept, value: application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, \*/\*.

*[//*]*显示HTTP报文Accept首部信息。*

**
