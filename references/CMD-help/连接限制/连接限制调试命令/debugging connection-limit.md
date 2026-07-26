
**连接限制 \-- 连接限制调试命令 \-- debugging connection-limit**

------------------------------------------------------------------------

【命令】

**[debugging connection-limit**  { **all** \| **event** \| **error** } [ **acl** [ **ipv6** ] *acl-number* ]]

**[undo debugging connection-limit ** { **all** \| **event** \| **error** }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示连接数限制的所有调试信息开关。

**[event**]：表示连接数限制的事件调试信息开关。

**[error**]：表示连接数限制的错误调试信息开关。

**[acl**]：指定仅输出匹配ACL规则的连接数限制相关的调试信息。若不指定该参数，则表示输出对所有连接数限制的相关调试信息。

**[ipv6**]：表示使用IPv6 ACL进行匹配。若不指定该参数，则表示使用IPv4 ACL进行匹配。

*[acl-number*]：ACL规则编号，取值范围为2000～3999。该参数可多次设置，但仅最后一次合法的配置生效。

【描述】

**[debugging connection-limit**]命令用来打开连接数限制调试信息开关。**undo debugging connection-limit**命令用来关闭连接数限制调试信息开关。

缺省情况下，连接数限制调试信息开关处于关闭状态。

表1-1 debugging connection-limit命令输出信息描述表

字段

描述

Connection(*src-ip*/*src-vpn*/*tunnel-id*:*src-port*\--\>*dst-ip*:*dst-port*(*protocol*)) matched limit *limit-id* of policy *policy-number* (*node*).

连接匹配到连接数限制规则，其中：

·*src-ip*/*src-vpn*/*tunnel-id*：源IP地址/源IP地址所属的MPLS L3VPN实例的名称/ DS Lite Tunnel ID。若不支持或未配置*src-vpn*、*tunnel-id*参数，则仅显示*src-ip*

·*src-port*：源端口号

·*dst-ip*：目的IP地址

·*dst-port*：目的端口号

·*protocol*：协议名称

·*limit-id*：连接数限制规则编号

·*policy-number*：连接数限制策略编号

·*node*：匹配标识（Global表示全局，*interface-type interface-number*表示具体接口）

Connection(*src-ip*/*src-vpn*/*tunnel-id*:*src-port*\--\>*dst-ip:dst-port*(*protocol*)) doesn't match policy (*node*).

连接不能匹配连接数限制规则，其中：

·*src-ip*/*src-vpn*/*tunnel-id*：源IP地址/源IP地址所属的MPLS L3VPN实例的名称/ DS Lite Tunnel ID。若不支持或未配置*src-vpn*、*tunnel-id*参数，则仅显示*src-ip*

·*src-port*：源端口号

·*dst-ip*：目的IP地址

·*dst-port*：目的端口号

·*protocol*：协议名称

·*node*：匹配标识（Global表示全局，*interface-type interface-number*表示具体接口）

An *protocol-version* statistic node of limit *limit-id* using ACL *acl-number* was created (*node*), parameters:

*[src-ip*]/*src-vpn*/*tunnel-id*\--\>*dst-ip*/*dst-vpn*:*dst-port*(*protocol*)

HighThres: *amount-max*,  LowThres: *amount-min*

连接数限制规则创建了一个统计节点，其中：

·*protocol-version*：IP协议版本（IPv4或IPv6）

·*src-ip*/*src-vpn*/*tunnel-id*：源IP地址/源IP地址所属的MPLS L3VPN实例的名称/ DS Lite Tunnel ID。若不支持或未配置*src-vpn*、*tunnel-id*参数，则仅显示*src-ip*

·*src-port*：源端口号

·*dst-ip*/*dst-vpn*：目的IP地址/目的IP地址所属的MPLS L3VPN实例的名称。若不支持或未配置*dst-vpn*参数，则仅显示*dst-ip*

·*dst-vpn*：目的IP地址所属的MPLS L3VPN实例的名称

·*dst-port*：目的端口号

·*protocol*：协议名称

·*limit-id*：连接数限制规则编号

·*acl-number*：规则引用的ACL编号

·*node*：匹配标识（Global表示全局，*interface-type interface-number*表示具体接口）

·*amount-max*：连接数上限值

·*amount-min*：连接数下限值

An *protocol-version* statistic node of limit*limit-id* using ACL *acl-number* was deleted (*node*), parameters:

*[src-ip*]/*src-vpn*/*tunnel*-*id*\--\>*dst-ip*/dst-vpn:*dst-port*(*protocol*)

删除了一个统计节点，其中：

·*protocol-version*：IP协议版本（IPv4或IPv6）

·*src-ip*/*src-vpn*/*tunnel-id*：源IP地址/源IP地址所属的MPLS L3VPN实例的名称/ DS Lite Tunnel ID。若不支持或未配置*src-vpn*、*tunnel-id*参数，则仅显示*src-ip*

·*src-port*：源端口号

·*dst-ip*/*dst-vpn*：目的IP地址/目的IP地址所属的MPLS L3VPN实例的名称。若不支持或未配置*dst-vpn*参数，则仅显示*dst-ip*

·*dst-port*：目的端口号

·*protocol*：协议名称

·*limit-id*：连接数限制规则编号

·*acl-number*：规则引用的ACL编号

·*node*：匹配标识（Global表示全局，*interface-type interface-number*表示具体接口）

An *protocol-version*  statistic node of limit *limit-id* using ACL *acl-number* was found (*node*), parameters:

*[src-ip*]/*src-vpn*/*tunnel-id*\--\>*dst-ip*/*dst-vpn*:*dst-port*(*protocol*)

找到了一个统计节点，其中：

·*protocol-version*：IP协议版本（IPv4或IPv6）

·*src-ip*/*src-vpn*/*tunnel-id*：源IP地址/源IP地址所属的MPLS L3VPN实例的名称/ DS Lite Tunnel ID。若不支持或未配置*src-vpn*、*tunnel-id*参数，则仅显示*src-ip*

·*src-port*：源端口号

·*dst-ip*/*dst-vpn*：目的IP地址/目的IP地址所属的MPLS L3VPN实例的名称。若不支持或未配置*dst-vpn*参数，则仅显示*dst-ip*

·*dst-port*：目的端口号

·*protocol*：协议名称

·*limit-id*：连接数限制规则编号

·*acl-number*：规则引用的ACL编号

·*node*：匹配标识（Global表示全局，*interface-type interface-number*表示具体接口）

Increased the count value of *node* *protocol-version* statistic node to *value*.

全局或接口下的某个统计节点中的连接计数增加：

·node：匹配标识（Global表示全局，*interface-type interface-number*表示具体接口）

·*protocol-version*：IP协议版本（IPv4或IPv6）

·*value*：更新后的统计节点连接计数

Decreased the count value of *node protocol-version* statistic node to *value*.

全局或接口下的的某统计节点中的连接计数减少：

·*node*：匹配标识（Global表示全局，*interface-type interface-number*表示具体接口）

·*protocol-version*：IP协议版本（IPv4或IPv6）

·*value*：更新后的统计节点连接计数

Failed to create *protocol-version* statistic node of limit *limit-id* (*node*)

创建统计节点失败，其中：

·*protocol-version*：IP协议版本（IPv4或IPv6）

·*limit-id*：连接数限制规则编号

·*node*：匹配标识（Global表示全局，*interface-type interface-number*表示具体接口）

【举例】

\# 在设备上配置采用连接限制策略0对设备的连接数进行统计与限制，其中规则0配置为对来自192.168.0.0/24网段的用户连接按源地址的方式进行统计与限制，其连接数上下限阈值分别为1000和900，并打开连接数限制事件调试信息开关。

\<Sysname\> debugging connection-limit event

\*Aug 18 21:08:14:237 2011 Sysname CONNLMT/7/PACKET:

 EVENT: Connection(192.168.0.210:1405\--\>2.2.2.2:21(tcp)) matched limit 0 of policy 0 (Global).

*// 匹配到连接数限制规则的用户连接：协议号为6（TCP），源IP地址为192.168.0.210，目的IP地址为2.2.2.2，源端口为1405，目的端口为21，源IP地址不属于任何MPLS L3VPN实例*

\*Aug 18 21:08:14:237 2011 Sysname CONNLMT/7/PACKET:

 EVENT: An IPv4 statistic node of limit 0 using ACL 3000 was created (Global), parameters:

 192.168.0.210\--\> Any:0(Any)

 HighThres: 1000, LowThres: 900

*// 创建了一个按源IP地址统计的统计节点，连接数上限为1000，连接数下限为900*

\*Aug 18 21:08:14:237 2011 Sysname CONNLMT/7/PACKET:

 EVENT: Increased the count value of Global IPv4 statistic node to 200

*// 增加IPv4统计节点的统计值到200*

\# 在设备上配置应用全局连接限制策略1对设备的连接数进行统计与限制，打开连接数限制事件调试信息开关。

\<Sysname\> debugging connection-limit error

\*Aug 18 21:08:14:237 2011 Sysname CONNLMT/7/PACKET:

 ERROR: Failed to create IPv6 statistic node of limit 5 (Global).

*// 在全局统计表中通过规则5创建IPv6统计节点失败*
