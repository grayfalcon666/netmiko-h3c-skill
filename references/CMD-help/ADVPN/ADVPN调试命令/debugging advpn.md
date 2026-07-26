
**ADVPN \-- ADVPN调试命令 \-- debugging advpn**

------------------------------------------------------------------------

【命令】

**[debugging advpn**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging advpn**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示ADVPN所有调试信息开关。

**[error**]：表示ADVPN错误调试信息开关。

**[event**]：表示ADVPN事件调试信息开关。

**[packet**]：表示ADVPN报文调试信息开关。

【描述】

**[debugging advpn**]命令用来打开ADVPN的调试信息开关。**undo debugging advpn**命令用来关闭ADVPN的调试信息开关。

缺省情况下，ADVPN的调试信息开关处于关闭状态。

表1-1 debugging advpn error命令输出信息描述表

字段

描述

Connection request was from hub to spoke. Discarded the message.

连接请求自Hub到Spoke，丢弃该消息

Failed to add data flow rule: sequence number = *sequence-number*.

添加序号为*sequence-number*的数据流规则失败

Failed to add next hop.

添加下一跳地址失败

Failed to add route.

添加路由失败

Failed to add route entry.

添加路由表项失败

Failed to add session *destination-address* to kernel.

添加目的地址为*destination-address*的会话到内核失败

Failed to allocate memory.

分配内存失败

Failed to bind port *port*.

绑定端口*port*失败

Failed to calculate digest for NAT detection attribute.

计算NAT检测属性的摘要值错误

Failed to create idle timer.

创建空闲定时器失败

Failed to create keepalive timer.

创建保活定时器失败

Failed to create new session.

创建新会话失败

Failed to create retransimssion timer.

创建报文重传定时器失败

Failed to create route delay timer.

创建路由延迟定时器失败

Failed to create route update timer.

创建路由更新定时器失败

Failed to delete all data flow rules on interface *interface-index*.

删除接口*interface-index*上的所有数据流规则失败

Failed to delete data flow rule: sequence number = *sequence-number*.

删除序号为*sequence-number*的数据流规则失败

Failed to delete IPsec session.

删除IPsec会话失败

Failed to delete route.

删除路由失败

Failed to delete session *destination-private-address* from kernel.

从内核中删除目的私网地址为*destination-private-address*的会话失败

Failed to get the source address of Tunnel*num* interface.

取接口Tunnel*num*的源地址失败

Failed to learn the route.

学习路由失败

Failed to clear the statistics for kernel.

重置内核的统计信息失败

Failed to send connection request.

发送连接请求失败

Failed to send keepalive request.

发送保活报文失败

Failed to start IPsec negotiation.

开始IPsec协商失败

Failed to update dumb timer.

更新静默定时器失败

Failed to update idle timer.

更新空闲定时器失败

Failed to update keepalive timer.

更新保活定时器失败

Invalid source address of tunnel interface.

无效的隧道接口地址

Socket of Tunnel*num* was closed.

接口Tunnel*num*的Socket关闭

Tunnel*num* failed to create socket.

接口Tunnel*num*创建Socket失败

Tunnel*num* failed to send packet.

接口Tunnel*num*发送报文失败

表1-2 debugging advpn event命令输出信息描述表

字段

描述

Added data flow rule: sequence number = *sequence--number*.

添加序号为*sequence-number*的数据流规则

Added route: destination = *destination-address*/*mask-len*, next hop = *nexthop*, preference = *preference*.

添加路由：目的地址为*destination-address*，掩码为*mask-len*，下一跳地址为*nexthop*，优先级为*preference*

Added session *destination-address* to kernel.

添加目的私网地址为*destination-address*的会话到内核

Deleted all data flow rules on interface *interface-index.*

删除接口*interface-index*上的所有数据流规则

Deleted data flow rule, sequence number = *sequence--number*.

删除序号为*sequence-number*的数据流规则

Deleted route: destination = *destination-address*/*mask-len*, next hop = *nexthop*, preference = *preference*.

删除路由：目的地址为*destination--address*，掩码为*mask-len*，下一跳地址为*nexthop*，优先级为*preference*

Deleted session *destination-address* from kernel.

从内核删除目的私网地址为*destination-address*的会话

Invalid destination address.

无效目的地址

Invalid IPsec flags.

无效IPsec标志

Invalid IP version.

无效IP版本

Invalid packet type for major version 0.

主版本号为0的报文类型错误

Invalid role ID.

无效角色ID

Invalid source address.

无效源地址

IPsec session was created.

IPsec会话被创建

Low memory.

低内存

Packet length was too short.

报文长度太短

Peer flags were changed.

对端标志位改变

Peer port was changed.

对端端口改变

Peer private address: *address*

对端私网地址：*address*

Peer public address: *address*

对端公网地址：*address*

*[Peer-private-address*: Connection request was from hub to spoke. Discarded the message.]

对端私网地址*Peer-private-address*：连接请求从Hub到Spoke，丢弃该消息

*[Peer-private-address*: Deleted IPsec session.]

对端私网地址*Peer-private-address*：删除IPsec会话

*[Peer-private-address*: Discarded the message.]

对端私网地址*Peer-private-address*：丢弃报文

*[Peer-private-address*: IPsec session was deleted.]

对端私网地址*Peer-private-address*：IPsec会话删除

*[Peer-private-address*: Peer was behind NAT.]

对端私网地址*Peer-private-address*：对端在NAT后面

*[Peer-private-address*: Received a route with an invalid gateway. Discarded it.]

对端私网地址*Peer-private-address*：收到一条网关无效的路由，丢弃

*[Peer-private-address*: Received connection request.]

对端私网地址*Peer-private-address*：收到连接请求消息

*[Peer-private-address*: Received connection response.]

对端私网地址*Peer-private-address*：收到连接响应消息

*[Peer-private-address*: Received delete request.]

对端私网地址*Peer-private-address*：收到删除请求消息

*[Peer-private-address*: Received keepalive request.]

对端私网地址*Peer-private-address*：收到保活请求消息

*[Peer-private-address*: Received keepalive response.]

对端私网地址*Peer-private-address*：收到保活响应消息

*[Peer-private-address*: Received redirection request.]

对端私网地址*Peer-private-address*：收到重定向请求消息

*[Peer-private-address*: Received route update.]

对端私网地址*Peer-private-address*：收到路由更新消息

*[Peer-private-address*: Received self route was newer than own. Discarded the message.]

对端私网地址*Peer-private-address*：接收到比本地更新的路由，丢弃该消息

*[Peer-private-address*: Received unknown message type *code*.]

对端私网地址*Peer-private-address*：收到编号为*code*的未知类型报文

*[Peer-private-address*: Received version upgrade request.]

对端私网地址*Peer-private-address*：收到版本更新请求消息

*[Peer-private-address*: Send connection response.]

对端私网地址*Peer-private-address*：发送连接响应消息

*[Peer-private-address*: Sent connection request.]

对端私网地址*Peer-private-address*：发送连接请求消息

*[Peer-private-address*: Sent delete request.]

对端私网地址*Peer-private-address*：发送删除请求消息

*[Peer-private-address*: Sent keepalive request.]

对端私网地址*Peer-private-address*：发送保活请求消息

*[Peer-private-address*: Sent keepalive response.]

对端私网地址*Peer-private-address*：发送保活响应消息

*[Peer-private-address*: Sent *length* bytes to *peer-address* by Tunnel*num*.]

对端私网地址*Peer-private-address*：在隧道接口Tunnel*num*向对端地址*peer-address*发送*length*字节的报文

*[Peer-private-address*: Sent route update.]

对端私网地址*Peer-private-address*：发送路由更新消息

*[Peer-private-address*: Sent version upgrade request.]

对端私网地址*Peer-private-address*：发送版本更新请求消息

*[Peer-private-address*: Session data was changed. Recreated it.]

对端私网地址*Peer-private-address*：会话数据改变，重建会话

*[Peer-private-address*: Session state is *state-code*. Discarded the message.]

对端私网地址*Peer-private-address*：会话状态为*state-code*，丢弃该消息

*[state-code*]的取值包括：

·0：初始状态

·1：静默状态

·2：成功状态

*[Peer-private-address*: Session state wasn\'t establish. Discarded the message.]

对端私网地址*Peer-private-address*：会话状态非建立态，丢弃消息

*[Peer-private-address*: Session state wasn\'t success. Discarded the message.]

对端私网地址*Peer-private-address*：会话状态非成功，丢弃消息

*[Peer-private-address*: Session type is not S-S. Discarded the message.]

对端私网地址*Peer-private-address*：会话类型非S-S，丢弃该消息

*[Peer-private-address*: Session version was changed. Recreated it.]

对端私网地址*Peer-private-address*：会话版本改变，重建会话

*[Peer-private-address*: Session was created.]

对端私网地址*Peer-private-address*：创建会话

*[Peer-private-address*: Session was deleted.]

对端私网地址*Peer-private-address*：删除会话

*[Peer-private-address*: Status changed from Dumb to Establishing.]

对端私网地址*Peer-private-address*：状态由静默变为建立

*[Peer-private-address*: Status changed from Dumb to Success.]

对端私网地址*Peer-private-address*：状态由静默变为成功

*[Peer-private-address*: Status changed from Establishing to Dumb.]

对端私网地址*Peer-private-address*：状态由建立变为静默

*[Peer-private-address*: Status changed from Establishing to Success.]

对端私网地址*Peer-private-address*：状态由建立变为成功

*[Peer-private-address*: Status changed from Success to Dumb.]

对端私网地址*Peer-private-address*：状态由成功变为静默

*[Peer-private-address*: Status changed from Success to Establishing.]

对端私网地址*Peer-private-address*：状态由成功变为建立

*[Peer-private-address*: Version wasn\'t matched.]

对端私网地址*Peer-private-address*：版本不匹配

*[Peer-private-address*: Waiting for IPsec negotiation.]

对端私网地址*Peer-private-address*：等待IPsec协商

Peer role was changed.

对端角色改变

Received connection request on interface Tunnel*num* from *source-address*.

从接口Tunnel*num*收到源地址为*source-address*的连接请求报文

Received *length* bytes from *peer-address* by Tunnel*num*.

从接口Tunnel*num*的对端地址*peer-address*收到长度为*length*的报文

Requested the public address for destination *private-address.*

请求目的私网地址*private-address*对应的公网地址

Requested the public address for next hop *nexthop.*

请求下一跳*nexthop*对应的公网地址

Session version was changed.

会话版本改变

The route already existed for redirected destination.

重定向目的地址的路由已经存在

The session already existed for redirected destination.

重定向目的地址的会话已经存在

Updated peer information to server.

向服务器更新对端地址

表1-3 debugging advpn packet命令输出信息描述表

字段

描述

Address: *address*

目的路由地址为*address*

Age: *age-time*

老化时间为*age-time*

Control message head

控制报文头

Destination IP: *destination-address*

目的IP地址为*destination-address*

Domain ID: *ID*

所在域ID为*ID*

Flags: *flags*

标志位为*flags*

Hash value: *hash-value*

Hash值为*hash-value*

IP version: *IP-version*

IP版本号为*IP-version*

Length: *length*

长度为*length*

Major version: *major-version*

主版本号为*major-version*

Minor version: *minor-version*

次版本号为*minor-version*

NAT detection attribute

NAT检测属性

Network number: *number*

子网个数为*number*

Network route data

子网路由数据

Next hop address: *address*

下一跳地址为*address*

Option: *code*

路由选项为*code*

Preference: *preference*

路由优先级为*preference*

Prefix: *mask-length*

路由前缀为*mask-length*

Redirection attribute

重定向属性

Reserved: *reserved*

保留字段为*reserved*

Role ID: *ID*

角色ID为*ID*

Route attribute

路由属性

Sequence: *sequence*

路由序列号为*sequence*

Source IP: *source-address*

源IP地址为*source-address*

Time: *sending-time*

报文发送时间为*sending-time*

Type: *code*

报文类型码为*code*

Unknown attribute

未知属性

【举例】

\# 打开ADVPN错误调试信息开关。系统达到内存门限时，配置Tunnel接口建立新隧道，设备上会打印如下调试信息。

\<Sysname\> debugging advpn event

\*Oct 24 19:47:25:914 2013 Sysname ADVPN/7/EVENT: Failed to create new session.

*// 创建新会话失败。*

\# 打开ADVPN事件调试信息开关。ADVPN在Tunnel1接口建立会话。Tunnel1接口shutdown时，设备上会打印如下调试信息。

\<Sysname\> debugging advpn event

\*Oct 24 19:47:25:914 2013 Sysname ADVPN/7/EVENT: 10.0.1.4: Session was deleted.

*// 私网10.0.1.4：会话被删除。*

\*Oct 24 19:47:25:915 2013 Sysname ADVPN/7/EVENT: Deleted session 10.0.1.4 from kernel.

*// 将私网10.0.1.4会话从内核删除。*

\# 打开ADVPN报文调试信息开关。设备上私网地址为10.0.0.2的VAM client向私网地址为10.0.0.1的对端发起隧道连接，并且收到对端响应。设备上打印如下调试信息。

\<Sysname\> debugging advpn packet

\*Oct 24 19:14:46:790 2013 Sysname ADVPN/7/PACKET: Control message head:

\*Oct 24 19:14:46:791 2013 Sysname ADVPN/7/PACKET:   Type            : 1

\*Oct 24 19:14:46:791 2013 Sysname ADVPN/7/PACKET:   Flags           : 10

\*Oct 24 19:14:46:791 2013 Sysname ADVPN/7/PACKET:   Role ID        : 2

\*Oct 24 19:14:46:791 2013 Sysname ADVPN/7/PACKET:   Major version : 1

\*Oct 24 19:14:46:791 2013 Sysname ADVPN/7/PACKET:   Minor version : 0

\*Oct 24 19:14:46:791 2013 Sysname ADVPN/7/PACKET:   IP version     : 4

\*Oct 24 19:14:46:791 2013 Sysname ADVPN/7/PACKET:   Domain ID      : 1

\*Oct 24 19:14:46:792 2013 Sysname ADVPN/7/PACKET:   Reserved       : 0

\*Oct 24 19:14:46:792 2013 Sysname ADVPN/7/PACKET:   Destination IP: 10.0.0.1

\*Oct 24 19:14:46:792 2013 Sysname ADVPN/7/PACKET:   Source IP      : 10.0.0.2

\*Oct 24 19:14:46:792 2013 Sysname ADVPN/7/PACKET:   Time            : 31539

\*Oct 24 19:14:46:792 2013 Sysname ADVPN/7/PACKET: NAT detection attribute:

\*Oct 24 19:14:46:792 2013 Sysname ADVPN/7/PACKET:   Hash value : e0fe4fd6cb9c895

*[// VAM client*]*向对端发起隧道连接，ADVPN报文的控制报文头内容：报文类型为1，标志位为10，角色ID为2，主版本号为1，次版本号为0，IP版本号为4，所属域ID为1，保留字段为0，目的IP地址为10.0.0.1，源IP地址为10.0.0.2，报文发送时间为31539；报文的NAT检测属性：Hash值为e0fe4fd6cb9c895。*

**ADVPN \-- ADVPN调试命令 \-- debugging vam client**

------------------------------------------------------------------------

【命令】

**[debugging vam client**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging vam client**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示VAM Client所有调试信息开关。

**[error**]：表示 VAM Client错误调试信息开关。

**[event**]：表示 VAM Client事件调试信息开关。

**[packet**]：表示VAM Client报文调试信息开关。

【描述】

**[debugging vam client**]命令用来打开VAM Client的调试信息开关。**undo debugging vam client**命令用来关闭VAM Client的调试信息开关。

缺省情况下，VAM Client的调试信息开关处于关闭状态。

表1-4 debugging vam client error命令输出信息描述表

字段

描述

Failed to allocate memory.

分配内存失败

Failed to encrypt/decrypt packet.

加解密失败

Not supported integrity authentication algorithm:  *integrity-name*.

不支持的完整性验证算法*integrity-name*

*[Private-address **server-index*]: Failed to bind the socket.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：绑定Socket失败

*[server-index*]为0表示主服务器，为1表示备服务器，以下不再赘述

*[Private-address **server-index*]: Failed to calculate the integrity value.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：计算完整性验证数据失败

*[Private-address **server-index*]: Failed to create a socket.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：创建Socket失败

*[Private-address **server-index*]: Failed to create the connection key.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：创建连接密钥失败

*[Private-address **server-index*]: Failed to create the dumb timer.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：创建静默定时器失败

*[Private-address **server-index*]: Failed to create the initialization key.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：创建初始密钥失败

*[Private-address **server-index*]: Failed to create the keepalive timer.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：创建保活定时器失败

*[Private-address **server-index*]: Failed to create the packet resending timer.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：创建报文重传定时器超时

*[Private-address **server-index*]: Failed to encrypt packet.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：加密报文失败

*[Private-address **server-index*]: Failed to get the socket options.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：获取Socket选项失败

*[Private-address **server-index*]: Failed to receive packet.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：接收报文失败

*[Private-address **server-index*]: Failed to resolve address for server *host-name.*

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：解析服务器主机名*host-name*失败

*[Private-address **server-index*]: Failed to send packet.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：发送报文失败

*[Private-address **server-index*]: Failed to update the dumb timer.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：更新静默定时器失败

*[Private-address **server-index*]: Failed to update the packet resending timer.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：更新报文重传定时器失败

*[Private-address **server-index*]: Socket error.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：套接字错误

*[Private-address **server-index*]: The address family of VAM server and ADVPN source interface aredifferent.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：VAM服务器地址类型和ADVPN源接口的不相同

*[Private-address **server-index*]: The ADVPN domain was not configured.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：ADVPN域未配置

*[Private-address **server-index*]: The mode of tunnel interface was invalid.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：隧道接口模式无效

*[Private-address **server-index*]: The net protocol of tunnel interface was down.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：隧道接口网络协议没有开启

*[Private-address **server-index*]: The pre-shared key was not configured.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：预共享密钥没有配置

*[Private-address **server-index*]: The VAM client was not enabled.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：VAM客户端没有使能

The encryption algorithm *encryption-name* was not supported.

加密算法*encryption-name*不支持

The integrity authentication algorithm *integrity-name* was not supported.

完整性验证算法*integrity-name*不支持

表1-5 debugging vam client event命令输出信息描述表

字段

描述

Encryption expected, but E flag was not set.

期望加密，但E标志位没有置位

Failed to allocate memory.

分配内存失败

Failed to calculate the integrity value.

计算完整性验证数据失败

Failed to get networks from packet.

从报文中获取子网失败

Failed to read ADVPN/IPsec updated information attribute from packet.

从报文中读取ADVPN/IPsec信息失败

Failed to read authentication information attribute from packet.

从报文中读取认证信息失败

Failed to read authentication request attribute from packet.

从报文中读取认证请求失败

Failed to read connection identifier attribute from packet.

从报文中读取连接属性失败

Failed to read data flow information attribute from packet.

从报文中读取数据流属性失败

Failed to read data operation attribute from packet.

从报文中读取数据操作属性失败

Failed to read destination node attribute from packet.

从报文中读取目的节点属性失败

Failed to read encryption parameter attribute from packet.

从报文中读取加密参数失败

Failed to read host/peer address attribute from packet.

从报文中读本端/对端地址属性失败

Failed to read hub digest attribute from packet.

从报文中读取Hub摘要信息失败

Failed to read integrity parameter attribute from packet.

从报文中读取完整性参数属性失败

Failed to read keepalive parameter attribute from packet.

从报文中读取保活参数失败

Failed to read network information attribute from packet.

从报文中读取子网信息失败

Failed to read node information attribute from packet.

从报文中读取节点信息失败

Failed to read random number attribute from packet.

从报文中读取随机数失败

Failed to read security request attribute from packet.

从报文中读取安全请求失败

Integrity expected, but A flag was not set.

期望完整性验证，但A标志位没有置位

*[message* *attribute* attribute not found.]

*[message* *attribute*]属性没有找到

Not supported authentication method *code.*

认证算法*code*不支持，*code*的取值包括：

·0：Unknown

·1：None

·2：PAP

·3：CHAP

·4：RSA

·5：DSS

*[Private-address **server-index*]: Added flow rule *sequence-number*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：添加序号为sequence-number的数据流规则

*[server-index*]为0表示主服务器，为1表示备服务器，以下不再赘述

*[Private-address **server-index*]: Added hub *private-address*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：添加私网地址为*private-address*的Hub

*[Private-address **server-index*]: Address resolution request for *address* was already in queue.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：地址*address*的解析请求已经在队列中

*[Private-address **server-index*]: Changed to active.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：服务器的配置变为激活

*[Private-address **server-index*]: Deleted all hubs.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：删除所有Hub

*[Private-address **server-index*]: Deleted flow rule *sequence-number*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：删除序号为*sequence-number*的数据流规则

*[Private-address **server-index*]: Deleted hub *private-address*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：删除私网地址为*private-address*的Hub

*[Private-address **server-index*]: Encryption algorithm list was not found.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：加密算法列表没有找到

*[Private-address **server-index*]: Failed to add flow rule *sequence-number*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：添加序号为*sequence-number*的数据流规则失败

*[Private-address **server-index*]: Failed to check integrity.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：完整性验证失败

*[Private-address **server-index*]: Failed to create connection key.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：创建连接密钥失败

*[Private-address **server-index*]: Failed to decrypt the packet.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：解报文失败

*[Private-address **server-index*]: Failed to delete all flow rules.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：删除所有数据流规则失败

*[Private-address **server-index*]: Failed to delete flow rule *sequence-number*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：删除序号为*sequence-number*的数据流规则失败

*[Private-address **server-index*]: Failed to resolve address for server *host-name*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：解析主机域名为*host-name*的服务器地址失败

*[Private-address **server-index*]: Flow rule *sequence-number* was not found.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：序号为*sequence-number*的数据流规则没有找到

*[Private-address **server-index*]: FSM status changed from *pre-state* to *current-state*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：状态机的状态由*pre-state*转变为*current-state*

状态机的状态包括：

·OFFLINE：离线

·INIT：初始

·REG：注册

·ONLINE：在线

·DUMB：静默

*[Private-address **server-index*]: Hub *private-address* was not found.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：私网地址为*private-address*的Hub没有找到

*[Private-address **server-index*]: Ignored hub *private-address*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：忽略私网地址为*private-address*的Hub

*[Private-address **server-index*]: Ignored the event.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：忽略事件

*[Private-address **server-index*]: Ignored the packet.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：忽略报文

*[Private-address **server-index*]: Integrity authentication algorithm list was not found.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：完整性验证算法没有找到

*[Private-address **server-index*]: Invalid authentication method.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：认证算法无效

*[Private-address **server-index*]: Invalid client cookie.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：客户端Cookie无效

*[Private-address **server-index*]: Invalid connection identifier.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：连接标识无效

*[Private-address **server-index*]: Invalid data operation.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：数据操作无效

*[Private-address **server-index*]: Invalid domain ID.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：域ID无效

*[Private-address **server-index*]: Invalid encryption algorithm.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：加密算法无效

*[Private-address **server-index*]: Invalid integrity authentication algorithm.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：完整性验证算法无效

*[Private-address **server-index*]: Invalid keep alive parameter.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：保活参数无效

*[Private-address **server-index*]: Invalid message ID.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：消息ID无效

*[Private-address **server-index*]: Invalid packet length.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：报文长度无效

*[Private-address **server-index*]: Invalid packet type.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：报文类型无效

*[Private-address **server-index*]: Invalid private address.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：私网地址无效

*[Private-address **server-index*]: Invalid sequence number.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：序列号无效

*[Private-address **server-index*]: Invalid version.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：版本无效

*[Private-address **server-index*]: Low memory, request denied.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：内存低，请求拒绝

*[Private-address **server-index*]: Low memory.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：内存低

*[Private-address **server-index*]: No address resolution request found.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：无地址解析请求

*[Private-address **server-index*]: No node updating request found.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：无节点更新请求

*[Private-address **server-index*]: Queued address resolution request for *address*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：将地址*address*的解析请求放入队列

*[Private-address **server-index*]: Received *type* message.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：收到*type*消息

*[Private-address **server-index*]: Resolved address was invalid.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：地址解析失败

*[Private-address **server-index*]: Sent *type* message.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：发送*type*消息

*[Private-address **server-index*]: Started to resolve address for server *host-name*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：开始解析主机名为*host-name*的服务器的地址

*[Private-address **server-index*]: Added flow rule *sequence-number* successfully.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：添加序号为*sequence-number*的数据流规则成功

*[Private-address **server-index*]: Deleted all flow rules successfully.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：删除所有数据流规则成功

*[Private-address **server-index*]: Deleted flow rule *sequence-number* successfully.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：删除序号为*sequence-number*的数据流成功

*[Private-address **server-index*]: The address for server *host-name* is *ip-address*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：主机名为*host-name*的服务器的地址为*ip-address*

*[Private-address **server-index*]: The address of primary and secondary server are the same.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：主备服务器的地址相同

*[Private-address **server-index*]: The address type or link protocol was not matched.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：地址类型和链路协议不匹配

*[Private-address **server-index*]: The dumb interval was *dumb-length* seconds.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：静默间隔是*dumb-length*秒

*[Private-address **server-index*]: The dumb timer expired.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：静默定时器超时

*[Private-address **server-index*]: The flow type was not redirection.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：流类型非重定向

*[Private-address **server-index*]: The hub *private-address* already existed.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：私网地址为*private-address*的Hub已经存在

*[Private-address **server-index*]: The information of hub *private-address* was changed.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：私网地址为*private-address*的Hub信息改变

*[Private-address **server-index*]: The keepalive timer expired.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：保活定时器超时

*[Private-address **server-index*]: The next hop for *request address* was *nexthop*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：地址*request address*的下一跳地址为*nexthop*

*[Private-address **server-index*]: The packet resending timer expired.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：重传报文定时器超时

*[Private-address **server-index*]: The packet was resent *count* times.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：报文已经重传*count*次

*[Private-address **server-index*]: The public address for *nexthop* was *public-address*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：下一跳地址*nexthop*的公网地址为*public-address*

*[Private-address **server-index*]: The role changed from *role* to *current-role*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：角色由*role*变为*current-role*

*[Private-address **server-index*]: The role changed to *role*.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：角色变为*role*

*[Private-address **server-index*]: Tried the version *number* protocol to send request to server.

私网地址为*Private-address*，注册的服务器索引为*server-index*的客户端：尝试版本为*number*的协议发送到服务器

The packet was too short.

报文太短

Wrong encryption algorithm, *expected-algorithm* was expected, but actually was *actual-algorithm.*

错误的加密算法，期望为*expected-algorithm*，而实际为*actual-algorithm*

Wrong integrity authentication algorithm, *expected-algorithm* was expected, but actually was *actual-algorithm*.

错误的验证算法，期望为*expected-algorithm*，而实际为*actual-algorithm*

Wrong integrity value length, *expected-ength* was expected, but actually was *actual-length*.

错误的完整性验证长度，期望为*expected-length*, 实际为*actual-length*

Wrong integrity value.

错误的完整性验证值

表1-6 debugging vam client packet命令输出信息描述表

字段

描述

Address: *address*

地址为*address*

Address: *address*: *port*

地址为*address*:*port*

Address length: *length*

地址长度为*length*

Address protocol: *protocol-code*

地址协议号为*protocol-code*

Address type: *type*

地址类型为*type*

Address type: *type* (*type name*)

地址类型为*type*，类型的名称为*type-name*

ADVPN domain ID: *ID*

ADVPN域名ID为*ID*

Age: *age*

老化时间为*age*

Attribute type: *type* (*type-name*), length: *length*, values:

属性类型为*type*，类型的名称为*type--name*，属性长度为*length*，属性值为：

Authentication method: *authentication-method* (*authentication-name*)

认证方法为*authentication-method*（名称为*authentication-name*）

Challenge data: *data*

挑战数据为*data*

Challenge ID: *ID*

挑战ID为*ID*

Challenge length: *length*

挑战码长度为*length*

Challenge response data: *data*

挑战响应数据为*data*

Challenge response length: *length*

挑战响应数据长度为*length*

Client cookie: *cookie*

客户端Cookie值为*cookie*

Code: *code*

错误码为*code*

Crypto IV: *IV-data*

加密向量数据为*IV-data*

Data operation: *operation-type* (*operation-name*)

数据操作类型为*operation-type*，数据操作名称为*operation-name*

Destination private address: *address*

目的私网地址为*address*

Destination private address: *address:port*

目的私网地址和端口为*address:port*

*[encryption-algorithm* (*algorithm-name*)]

加密算法*encryption-algorithm*（算法名称为*algorithm-name*）

Encryption algorithm list:

加密算法列表

Encryption algorithm: *algorithm-code*

加密算法为*algorithm-code*

Ending destination address: *address*

目的终止地址为*address*

Ending destination port: *port*

目的终止端口为*port*

Ending source address: *address*

源终止地址为*address*

Ending source port: *port*

源终止端口为*port*

ExtFlags: *flag*

扩展标志位为*flag*

Flags: *data-operating-flag*

标志位为数据操作标志位*data-operating-flag*

Flags: *packet-head-flag*

标志位为报文头标志位*packet-head-flag*

Flow action: *action-code* (*action-name*)

流动作的动作码为*action-code*，动作名称为*action-name*

Flow sequence number: *sequence*

数据流序列号为*sequence*

Flow type: *type* (*type-name*)

数据流类型为*type*，数据流名称为*type-name*

Holding time: *length*

存活时长为*length*

Hub information digest: *digest-value*

Hub摘要信息为*digest-value*

Integrity algorithm: *algorithm*

验证算法为*algorithm*

Integrity authentication algorithm list:

验证算法列表

*[Integrity-algorithm* (*algorithm-name*)]

验证算法为*Integrity-algorithm*（算法名称为*algorithm-name*）

Integrity value: *value*

验证值为*value*

Interval: *value*

时间间隔为*value*

IP protocol: *protocol*

IP协议类型为*protocol*

Length: *length*

长度为*length*

Length of VPN ID: *length*

VPN名长度为*length*

Link protocol: *protocol* (*protocol name*)

链路层协议为*protocol*（协议名称为*protocol-name*）

Message ID: *ID*

消息ID值为*ID*

MTU: *value*

MTU值为*value*

Network *index*

子网*index*，*index*为子网的索引

Network number: *count*

子网个数为*count*

Next hop address: *address*

下一跳地址为*address*

Node flags: *flag*

节点标志位为*flag*

Not supported

不支持

Number: *number*

保活次数为*number*

Number of network: *number*

子网个数为*number*

Options: *option*

子网选项为*option*

Packet head:

报文头信息

Password: \*\*\*

密码

Password length: \*\*\*

密码长度

Preference: *preference*

优先级为*preference*。该字段在子网属性中表示子网优先级，在节点属性中表示客户端优先级

Prefix length: *length*

前缀长度为*length*

Private address: *address*

私网地址为*address*

Private address: *address*:*port*

私网地址和端口为*address*:*port*

Private address type: *type* (*type-name*)

私网地址类型为*type*（地址类型的名称为*type-name*）

Private network address: *address*

子网地址为*address*

Private next hop address: *address*

私网下一跳地址为*address*

Private next hop address: *address*:*port*

私网下一跳地址和端口为*address*:*port*

Public address: *address*

公网地址为*address*

Public address: *address*:*port*

公网地址和端口为*address*:*port*

Public address type: *type* (*type-name*)

公网地址类型为*type*（地址类型名称为*type-name*）

Public port: *port-number*

公网端口为*port-number*

Random number: *number*

随机值为*number*

Reserved: *value*

保留字段值为*value*

Sequence: *sequence-number*

序列号为*sequence-number*。该字段在报文头中表示报文序列号，在子网属性中表示子网序列号

Starting destination address: *address*

起始目的地址为*address*

Starting destination port: *port-number*

起始目的端口为*port-number*

Starting source address: *address*

起始源地址为*address*

Starting source port: *port-number*

起始源端口号为*port-number*

Type: *type* (*type-name*)

报文类型为*type*，报文类型名称为*type-name*）

Username: *username*

用户名为*username*

Username length: *length*

用户名长度为*length*

Version: *version*

版本号为*version*

ADVPN domain ID: *advpn-domain-ID*

ADVPN域标识为*advpn-domain-ID*

【举例】

\# 打开VAM Client错误调试信息开关。在VAM Client上配置IPv6的VAM Server地址，隧道口引用该Client，隧道口源接口为IPv4地址，开始注册，设备上将出现如下调试信息。

\<client\> debugging vam client error

\*Oct 24 17:01:21:668 2013 client VAMC/7/ERROR: -MDC=1; 10.1.1.1[0: The address family of VAM server and ADVPN source interface are not same.]

*[// VAM Server*]*地址和源接口地址不属于相同的地址族。*

\# 打开VAM Client事件调试信息开关。私网地址为10.1.1.1的客户端从主服务器下线，设备上将出现如下调试信息。

\<client\> debugging vam client event

\*Oct 24 17:09:20:179 2013 client VAMC/7/EVENT: -MDC=1; 10.1.1.1[0: Sent Logout request message.]

*// 私网地址为10.0.0.1、注册于主服务器的客户端发送离线请求消息*。*

\*Oct 24 17:09:20:179 2013 client VAMC/7/EVENT: -MDC=1; 10.1.1.10: The role changed to Unknown.

*// 私网地址为10.0.0.1、注册于主服务器的客户端角色变为未知。*

\*Oct 24 17:09:20:179 2013 client VAMC/7/EVENT: -MDC=1; 10.1.1.10: Deleted all hubs.

*// 私网地址为10.0.0.1、注册于主服务器的客户端删除所有Hub。*

\*Oct 24 17:09:20:179 2013 client VAMC/7/EVENT: -MDC=1; 10.1.1.10: FSM state changed from ONLINE to OFFLINE.

*// 私网地址为10.0.0.1、注册于主服务器的客户端状态机由在线变为离线。*

\# 打开VAM Client报文调试信息开关。设备发出Keepalive报文，打印如下调试信息。

\<client\> debugging vam client packet

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1; Packet head:

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Version : 5

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Type    : 13 (Keepalive)

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Length  : 28

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Sequence: 8

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Flags   : 0

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Code    : 0

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   ExtFlags: 0

*[// Keepalive*]*报文头的内容：版本为5，类型为13（表示是Keepalive报文），长度为28，标志位为0，序列号为8，错误码为0，扩展标志位为0。*

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1; Attribute type: 20 (Connection identifier), length: 12, values:

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Client cookie       : 109a1440

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   ADVPN domain ID     : 1

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Private address type: 1 (IPv4)

\*Oct 24 17:20:28:668 2013 client VAMC/7/PACKET: -MDC=1;   Private address     : 10.1.1.1

*// 属性类型为20（连接标识），属性长度为12，属性值：客户端Cookie为109a1440，ADVPN域ID为1，私网地址类型为1（IPv4），私网地址为10.1.1.1。*

**ADVPN \-- ADVPN调试命令 \-- debugging vam server**

------------------------------------------------------------------------

【命令】

**[debugging vam server**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging vam server**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示VAM Server所有调试信息开关。

**[error**]：表示 VAM Server错误调试信息开关。

**[event**]：表示 VAM Server事件调试信息开关。

**[packet**]：表示VAM Server报文调试信息开关。

【描述】

**[debugging vam server**]命令用来打开VAM Server的调试信息开关。**undo debugging vam server**命令用来关闭VAM Server的调试信息开关。

缺省情况下，VAM Server的调试信息开关处于关闭状态。

表1-7 debugging vam server error命令输出信息描述表

字段

描述

*[ACL-type *name *group-name* ACL group: Failed to convert rule *sequence* content to data flow.]

类型为*ACL-type*名称为*group-name*的ACL组：将编号为*sequence*的规则内容转换为数据流失败

*[ACL-type *name *group-name* ACL group: Failed to get rule *sequence* content.]

类型为*ACL-type*名称为*group-name*的ACL组：获取编号为*sequence*的规则内容失败

*[ACL-type *number *group-number* ACL group: Failed to convert rule *sequence* content to data flow.]

类型为*ACL-type*编号为*group-number*的ACL组：将编号为*sequence*的规则内容转换为数据流失败

*[ACL-type *number *group-number* ACL group: Failed to get rule *sequence* content.]

类型为*ACL-type*编号为*group-number*的ACL组：获取编号为*sequence*的规则内容失败

*ADVPN-ID* *private-address*: Authentication algorithm method was not supported.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：认证算法不支持

*ADVPN-ID* *private-address*: Failed to create aging timer.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：创建老化定时器失败

*ADVPN-ID* *private-address*: Failed to create authentication timer.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：创建认证定时器失败

*ADVPN-ID* *private-address*: Failed to create connect key.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：创建连接密钥失败

*ADVPN-ID* *private-address*: Failed to create data flow resend timer.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：创建数据流重传定时器失败

*ADVPN-ID* *private-address*: Failed to create HA ACK timer.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：创建HA ACK响应定时器失败

*ADVPN-ID* *private-address*: Failed to create offline timer.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：创建下线定时器失败

*ADVPN-ID* *private-address*: Failed to create resend hub message timer.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：创建Hub重传定时器失败

*ADVPN-ID* *private-address*: Failed to create version 5 client.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：创建VAM 5版本的客户端失败

*ADVPN-ID* *private-address*: Failed to de-encapsulate authentication response.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装认证响应失败

*ADVPN-ID* *private-address*: Failed to de-encapsulate initialization request.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装初始化请求失败

*ADVPN-ID* *private-address*: Failed to de-encapsulate register request.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装注册请求失败

*ADVPN-ID* *private-address*: Failed to decrypt initialization request message.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：解密初始化请求失败

*ADVPN-ID* *private-address*: Failed to decrypt *message-name* packet.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：解密*message-name*报文失败

*ADVPN-ID* *private-address*: Failed to encrypt *message-name* packet.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：加密*message-name*报文失败

*ADVPN-ID* *private-address*: Failed to get initial integrity key.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：获取初始验证密钥失败

*ADVPN-ID* *private-address*: Failed to get node identifier attribute.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：获取节点连接属性失败

*ADVPN-ID* *private-address*: Failed to integrate *message-name* packet.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：验证*message-name*报文失败

*ADVPN-ID* *private-address*: Failed to process initialization request.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：处理初始化请求所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：失败

*ADVPN-ID* *private-address*: Failed to send packet.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：发送报文失败

*ADVPN-ID* *private-address*: Invalid packet head.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：无效报文头

*ADVPN-ID* *private-address*: Pre-shared key was not configured.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：预共享密钥没有配置

*ADVPN-ID* *private-address*: Server was not enabled.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：服务器没有使能

*ADVPN-ID* *private-address*: The client did not exist. Discarded the packet.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：客户端不存在，丢弃报文

*ADVPN-ID* *private-address*: The client was not a hub or spoke.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：客户端既不是Hub也不是Spoke

*ADVPN-ID* *private-address*: Received unknown packet.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：收到未知报文

*ADVPN-ID* *private-address*: Received invalid initialization request packet.

所属ADVPN域为*ADVPN-ID*，私网地址为*private-address*的客户端：收到无效的初始化请求报文

Invalid challenge ID.

无效挑战码ID

Failed to create IPv4 socket.

创建IPv4 Socket失败

Failed to create IPv6 socket.

创建IPv6 Socket失败

Failed to create version 3/4 client for *public-address*:*port*.

创建公网地址为*address*:*port*的VAM 3/4版本的客户端失败

Failed to receive packet.

接收报文失败

*[Private-address* client was not in the ADVPN domain *advpn-name*.]

私网地址*private-address*的客户端不在名为*advpn-name*的ADVPN域中

Received a packet with the public address *public-address*:*port*, but failed to get the node identifier attribute*.

收到公网地址为*public-address*:*port*的报文，获取连接标识失败

Received a packet with invalid version 3/4 from the public address *public-address*:*port*.

从公网地址*public-addres:port*收到无效的版本3/4报文

表1-8 debugging vam server event命令输出信息描述表

字段

描述

Disconnected to AAA module.

与AAA模块断开连接

Disconnected to ACL module.

与ACL模块断开连接

Encryped data was empty.

加密数据为空

Encryped packet was too long.

加密报文过长

Failed to get encryption algorithm attribute from packet.

获取加密算法失败

Failed to get integrity algorithm attribute from packet.

获取完整性验证算法失败

Failed to get integrity algorithm data from packet.

获取完整性验证数据失败

Failed to read ADVPN/IPsec updated information attribute from packet.

读取ADVPN/IPsec更新信息失败

Failed to read authentication information from packet.

读取认证信息失败

Failed to read authentication request attribute from packet.

读取认证请求属性失败

Failed to read challenge response data from CHAP authentication packet.

从CHAP认证报文中读取挑战响应数据失败

Failed to read data flow information attribute from packet.

读取数据流信息失败

Failed to read data operation attribute from packet.

读取数据操作属性失败

Failed to read destination node attribute from packet.

读取目的节点属性失败

Failed to read host/peer address attribute from packet.

读取本端/对端属性失败

Failed to read hub digest attribute from packet.

读取Hub摘要属性失败

Failed to read keepalive parameter attribute from packet.

读取保活参数失败

Failed to read network information attribute from packet.

读取子网信息失败

Failed to read network information of node from packet.

读取节点中的子网失败

Failed to read node identifier attribute from packet.

读取节点标识属性失败

Failed to read node information attribute from packet.

读取节点信息失败

Failed to read random number attribute from packet.

读取随机数失败

Failed to read security request attribute from packet.

读取安全请求属性失败

Failed to read user name from CHAP authentication packet.

从CHAP认证报文中读取用户名失败

Failed to read user name from PAP authentication packet.

从PAP认证报文中读取用户名失败

Failed to read user password from PAP authentication packet.

从PAP认证报文中读取用户密码失败

Invalid network address type.

无效的子网地址类型

Invalid encryption type.

无效加密类型

*[Attribute-name* attribute was not found.]

名称为*Attribute-name*的属性没有找到

Node identifier length was too long.

节点标识长度太长

Packet head was too short.

报文头太短

Received AAA asynchronism response: result code =  *result*, response code = *response.*

收到AAA的异步响应，结果码为*result*，响应码为*response*

Received AAA session control request: operation code = *code*.

收到AAA的会话控制请求，操作码为*code*

Reconnected to AAA module successfully.

成功重连AAA模块

Reconnected to ACL module successfully.

成功重连ACL模块

*[ACL-type* name *group-name* ACL group: Received an ACL event with the code *event-code*.]

类型为*ACL-type*名称为*group-name*的ACL组：收到ACL事件，事件码为*event-code*

*[ACL-type* number *group-number* ACL group: Received an ACL event with the code *event-code*.]

类型为*ACL-type*编号为*group-number*的ACL组：收到ACL事件，事件码为*event-code*

*ADVPN-ID* *private-address*: AAA accounting failed.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：AAA计费失败

*ADVPN-ID* *private-address*: AAA authentication failed.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：AAA认证失败

*ADVPN-ID* *private-address*: AAA authentication succeeded.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：AAA认证成功

*ADVPN-ID* *private-address*: Added *network*/*mask-length* network to address map.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：添加子网/掩码*network*/*mask-length*到地址表中

*ADVPN-ID* *private-address*: Address query result = no result.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：地址查询无结果

*ADVPN-ID* *private-address*: Address query result = network *network*/*mask-length*.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：地址查询结果为查到子网*network*/*mask-length*

*ADVPN-ID* *private-address*: Address query result = next hop *address*.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：地址查询结果为查到下一跳地址*address*

*ADVPN-ID* *private-address*: Found noonline spoke for update node information.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：收到节点更新信息，但无法找到在线Spoke

*ADVPN-ID* *private-address*: Deleted *network*/*mask-length* network from address map.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：从地址表中删除*network*/*mask-length*子网

*ADVPN-ID* *private-address*: Deleting client.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：删除客户端

*ADVPN-ID* *private-address*: Failed to de-encapsulate address resolution request.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装地址解析请求失败

*ADVPN-ID* *private-address*: Failed to de-encapsulate data flow response.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装数据流响应消息失败

*ADVPN-ID* *private-address*: Failed to de-encapsulate hub response.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装Hub响应消息失败

*ADVPN-ID* *private-address*: Failed to de-encapsulate logout request.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装下线请求失败

*ADVPN-ID* *private-address*: Failed to de-encapsulate network request.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装子网请求失败

*ADVPN-ID* *private-address*: Failed to de-encapsulate node update request.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：解封装节点更新请求失败

*ADVPN-ID* *private-address*: Failed to encrypt or integrate packet.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：加密或验证报文失败

*ADVPN-ID* *private-address*: Failed to match authentication algorithm.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：匹配认证算法失败

*ADVPN-ID* *private-address*: Failed to match encryption algorithm.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：匹配加密算法失败

*ADVPN-ID* *private-address*: FSM received *message* message in *state* state.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：状态机在*state*状态收到*message*消息

*[state*]的取值包括：

·INIT1：初始化状态1

·INIT2：初始化状态2

·REG1：注册状态1

·REG2：注册状态2

·ONLINE：在线状态

·OFFLINE：离线状态

*ADVPN-ID* *private-address*: FSM status changed from *pre-state* to *state*.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：状态机由*prestate*状态转换为*state*状态

*ADVPN-ID* *private-address*: Ignored the event.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：忽略事件

*ADVPN-ID* *private-address*: Ignored the packet.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：忽略报文

*ADVPN-ID* *private-address*: Invalid address type.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效地址类型

*ADVPN-ID* *private-address*: Invalid ADVPN port.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效ADVPN端口

*ADVPN-ID* *private-address*: Invalid extern flags.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效外部标识位

*ADVPN-ID* *private-address*: Invalid link protocol.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效链路层协议

*ADVPN-ID* *private-address*: Invalid packet head.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效报文头

*ADVPN-ID* *private-address*: Invalid private address type.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效私网地址类型

*ADVPN-ID* *private-address*: Invalid private address.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效私网地址

*ADVPN-ID* *private-address*: Invalid public address.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效公网地址

*ADVPN-ID* *private-address*: Invalid public address type.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效公网地址类型

*ADVPN-ID* *private-address*: Invalid sequence number.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效序列号

*ADVPN-ID* *private-address*: Invalid version.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：无效版本

*ADVPN-ID* *private-address*: Next hop address was different from the client\'s private address.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：下一跳地址与客户端私网地址不同

*ADVPN-ID* *private-address*: Pre-shared key was not configured.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：预共享密钥没有配置

*ADVPN-ID* *private-address*: Register ADVPN port was different from the configured one.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：注册的ADVPN端口号与配置不相同

*ADVPN-ID* *private-address*: Register ADVPN public address was different from configured.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：注册ADVPN公网地址与配置不相同

*ADVPN-ID* *private-address*: Sent *message* message in *state* state.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：在*state*状态发送*message*消息

*ADVPN-ID* *private-address*: Server was not enabled.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：服务器没有使能

*ADVPN-ID* *private-address*: Starting AAA accounting request.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：开始请求AAA计费

*ADVPN-ID* *private-address*: Starting AAA authentication request.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：开始请求AAA认证

*ADVPN-ID* *private-address*: The aging timer expired.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：老化定时器超时

*ADVPN-ID* *private-address*: The authentication timer expired.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：认证定时器超时

*ADVPN-ID* *private-address*: The client was not a hub or spoke.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：该客户端非Hub也非Spoke

*ADVPN-ID* *private-address*: The data flow resend timer expired.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：数据流重传定时器超时

*ADVPN-ID* *private-address*: The HA ACK timer expired.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：HA ACK等待定时器超时

*ADVPN-ID* *private-address*: The hub information resend timer expired.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：Hub信息重传定时器超时

*ADVPN-ID* *private-address*: The offline timer expired.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：下线定时器超时

*ADVPN-ID* *private-address*: Old client. To be deleted.

所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*的客户端：老客户端，被删除

表1-9 debugging vam server packet命令输出信息描述表

字段

描述

*ADVPN-ID* *private-address*: Received packet.

收到来自Client的报文，该Client所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*

*ADVPN-ID* *private-address*: Sent packet.

向Client发送报文，该Client所属ADVPN域ID为*ADVPN-ID*，私网地址为*private-address*

Address: *address*

地址为*address*

Address: *address*:*port*

地址和端口为*address*:*port*

Address length: *length*

地址长度为*length*

Address protocol: *protocol-code*

地址协议号为*protocol-code*

Address type: *type*

地址类型为*type*

Address type: *type* (*type-name*)

地址类型为*type*（地址类型名称为*type-name*）

ADVPN domain ID: *ID*

ADVPN域名ID为*ID*

Age: *age*

老化时间为*age*

Attribute type: *type* (*type-name*), length: *length*, values:

属性类型为*type*（属性类型名称为*type-name*），属性长度为*length*，属性值为：

Authentication method: *authentication-method* (*authentication-name*)

认证方法为*authentication-method*（认证方法名称为*authentication-name*）

Challenge data: *data*

挑战数据为*data*

Challenge ID: *ID*

挑战ID为*ID*

Challenge length: *length*

挑战码长度为*length*

Challenge response data: *data*

挑战响应数据为*data*

Challenge response length: *length*

挑战响应数据长度为*length*

Client cookie: *cookie*

客户端Cookie值为*cookie*

Code: *code*

错误码为*code*

Crypto IV: *IV-data*

加密向量数据为*IV-data*

Data operation: *operating-type* (*operating name*)

数据操作类型为*operating-type*（名称为*operating-name*）

Destination private address: *address*

目的私网地址为*address*

Destination private address: *address*:*port*

目的私网地址和端口为*address*:*port*

*[encryption-algorithm* (*algorithm-name*)]

加密算法*encryption-algorithm*（算法名称为*algorithm-name*）

Encryption algorithm list:

加密算法列表

Encryption algorithm: *algorithm-code*

加密算法为*algorithm-code*

Ending destination address: *address*

目的终止地址为*address*

Ending destination port: *port*

目的终止端口为*port*

Ending source address: *address*

源终止地址为*address*

Ending source port: *port*

源终止端口为*port*

ExtFlags: *flag*

扩展标志位为*flag*

Flags: *data-operating-flag*

标志位为数据操作标志位*data-operating-flag*

Flags: *packet-head-flag*

标志位为报文头标志位*packet-head-flag*

Flow action: *action-code* (*action-name*)

流动作的动作码为*action-code*（动作名称为*action-name*）

Flow sequence number: *sequence*

数据流序列号为*sequence*

Flow type: *type* (*type-name*)

数据流类型为*type*（数据流类型名称为*type-name*）

Holding time: *length*

存活时长为*length*

Hub information digest: *digest-value*

Hub摘要信息为*digest value*

Integrity algorithm: *algorithm*

验证算法为*algorithm*

Integrity authentication algorithm list:

验证算法列表

*[Integrity-algorithm* (*algorithm-name*)]

验证算法*Integrity algorithm*（验证算法名称为*algorithm name*）

Integrity value: *value*

验证值为*value*

Interval: *value*

时间间隔为*value*

IP protocol: *protocol*

IP协议类型为*protocol*

Length: *length*

长度为*length*

Length of ADVPN domain name: *length*

ADVPN域名称长度：*length*

Link protocol: *protocol* (*protocol-name*)

链路层协议为*protocol*（协议名称为*protocol-name*）

Message ID: *ID-value*

消息ID值为*ID-value*

MTU: *value*

MTU值为*value*

Network *index*

子网*index*，*index*为子网的索引

Next hop address: *address*

下一跳地址为*address*

Node flags: *flag*

节点标志位为*flag*

Not supported

不支持

Number: *number*

保活次数为*count*

Number of networks: *number*

子网个数为*number*

Options: *option*

子网选项为*option*

Packet head:

报文头：

Password: \*\*\*

密码

Password length: \*\*\*

密码长度

Preference: *preference*

优先级为*preference*。该字段在子网属性中表示子网优先级，在节点属性中表示客户端优先级

Prefix length: *length*

前缀长度为*length*

Private address: *address*

私网地址为*address*

Private address: *address*:*port*

私网地址和端口为*address*:*port*

Private address type: *type* (*type-name*)

私网地址类型为*type*（地址类型的名称为*type-name*）

Private network address: *address*

子网地址为*address*

Private next hop address: *address*

私网下一跳地址为*address*

Private next hop address: *address*:*port*

私网下一跳地址为*address*:*port*

Public address: *address*

公网地址为*address*

Public address: *address*:*port*

公网地址和端口为*address*:*port*

Public address type: *type* (*type-name*)

公网地址类型为*type*（地址类型的名称为*type-name*）

Public port: *port-number*

公网端口为*port-number*

Random number: *number*

随机值为*number*

Reserved: *value*

保留字段值为*value*

Sequence: *sequence-number*

序列号：*sequence--number*。该字段在报文头中表示报文序列号，在子网属性中表示子网序列号

Starting destination address: *address*

起始目的地址为*address*

Starting destination port: *port-number*

起始目的端口为*port-number*

Starting source address: *address*

起始源地址为*address*

Starting source port: *port-number*

起始源端口号为*port-number*

Type: *type* (*type-name*)

报文类型为*type*（报文类型的名称为*type-name*）

Username: *user*-*name*

用户名为*user-name*

Username length: *length*

用户名长度为*length*

Version: *version*

版本号为*version*

ADVPN domain ID: *advpn-domain-ID*

ADVPN域标识为*advpn-domain-ID*

【举例】

\# 打开VAM Server错误调试信息开关。ID为1的ADVPN域未使能，私网地址为10.1.1.1的VAM Client向设备发送注册请求报文，设备上将出现如下调试信息。

\<server\> debugging vam server error

\*Oct 24 16:26:42:638 2013 server VAMS/7/ERROR: -MDC=1; [1 10.1.1.1: Server was not enabled.]

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：服务器未使能。*

\*Oct 24 16:26:42:638 2013 server VAMS/7/ERROR: -MDC=1; 1 10.1.1.1: Failed to create version 5 client.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：创建VAM 5版本的客户端失败。*

\# 打开VAM server事件调试信息开关。客户端上线，设备上将出现如下调试信息。

\<server\> debugging vam server event

\*Oct 24 16:11:17:668 2013 server VAMS/7/EVENT: -MDC=1; [1 10.1.1.1: FSM received Initialization request message in INIT1 state.]

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机在INIT1状态收到初始化请求报文。*

\*Oct 24 16:11:17:668 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: FSM status changed from INIT1 to INIT1.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机由INIT1状态变为INIT1状态。*

\*Oct 24 16:11:17:668 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: Sent Initialization response message in INIT1 state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：在INIT1状态发送初始化响应报文。*

\*Oct 24 16:11:17:669 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: FSM receive Initialization complete message in INIT1 state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机在INIT1状态收到初始化完成消息。*

\*Oct 24 16:11:17:669 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: FSM status changed from INIT1 to INIT2.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机由INIT1状态变为INIT2状态。*

\*Oct 24 16:11:17:669 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: Sent Initialization complete message in INIT2 state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：在INIT2状态发送初始化完成消息。*

\*Oct 24 16:11:17:669 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: FSM received Register request message in INIT2 state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机在INIT2状态收到注册请求消息。*

\*Oct 24 16:11:17:669 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: FSM status changed from INIT2 to REG2.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机由INIT2状态转变为REG2状态。*

\*Oct 24 16:11:17:669 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1:Sent Register response message in REG2 state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：在REG2状态发送注册响应消息。*

\*Oct 24 16:11:17:670 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: FSM received Keepalive message in REG2 state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机在REG2状态接收到保活报文。*

\*Oct 24 16:11:17:670 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: FSM status changed from REG2 to ONLINE.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机由REG2状态变为ONLINE状态。*

\*Oct 24 16:11:17:670 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: Sent Keepalive message in ONLINE state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：在ONLINE状态发送Keepalive报文。*

\*Oct 24 16:11:17:670 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: Sent Hub information request message in ONLINE state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：在ONLINE状态发送Hub信息请求消息。*

\*Oct 24 16:11:17:670 2013 server VAMS/7/EVENT: -MDC=1; 1 10.1.1.1: FSM received Hub information response message in ONLINE state.

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：状态机在ONLINE状态接收Hub信息响应消息。*

\# 打开VAM server报文调试信息开关。设备收到客户端发送的子网请求报文时，打印如下调试信息。

\<server\> debugging vam server packet

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1; [1 10.1.1.1 Receive packet.]

*// 所属ADVPN域ID为1，私网地址为10.1.1.1的客户端：接收报文。*

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1; Packet head:

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   Version : 5

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   Type    : 15 (Network registing request)

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   Length  : 56

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   Sequence: 7

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   Flags   : 0

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   Code    : 0

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   ExtFlags: 0

*// 报文头内容：版本为5，类型为15（表示子网注册请求），长度为56，序列号为7，标志位为0，错误码为0，扩展标志位为0，。*

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1; Attribute type: 20 (Connection identifier), length: 12, values:

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   Client cookie         : 0x677b63c1

\*Oct 24 16:19:46:774 2013 server VAMS/7/PACKET: -MDC=1;   ADVPN domain ID: 1

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;   Address Type   : 1 (IPv4)

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;   Private address: 10.1.1.1

*// 属性类型为20（连接属性），属性长度为12，属性值：客户端Cookie为0x677b63c1，ADVPN域ID为1，地址类型为1（IPv4），私网地址为10.1.1.1。*

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1; Attribute type: 15 (Network information), length: 24, values:

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;   Network Number         : 1

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;   Address type           : 4

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;   Next hop address       : 10.1.1.1

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;   Network 0

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;     Private network address: 10.1.3.0

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;     Sequence Number        : 1

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;     Age                    : 0

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;     Prefix length          : 24

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;     Preference             : 12

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;     Option                 : 0

\*Oct 24 16:19:46:775 2013 server VAMS/7/PACKET: -MDC=1;     Reserved               : 0

*// 属性类型为15（子网信息），属性长度为24，属性值：子网数量为1，地址类型为4，下一跳地址为10.1.1.1，第0个子网，私网子网地址为10.1.3.0，序列号为1，老化时间为0，前缀长度为24，优先级为12，子网选项为0，保留字段值为0。*
