
**MSDP \-- MSDP配置命令 \-- cache-sa-enable**

------------------------------------------------------------------------

**[cache-sa-enable**]命令用来使能SA报文缓存机制，即缓存SA报文中所包含的（S，G）表项。

**[undo cache-sa-enable**]命令用来关闭SA报文缓存机制。

【命令】

**[cache-sa-enable**]

**[undo cache-sa-enable**]

【缺省情况】

SA报文缓存机制处于使能状态，即设备在收到SA报文后缓存其中包含的（S，G）表项。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在公网实例中使能SA报文缓存机制，使设备在收到SA报文后缓存其中包含的（S，G）表项。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp cache-sa-enable

【相关命令】

·**display msdp sa-cache**

·**display msdp sa-count**

**MSDP \-- MSDP配置命令 \-- display msdp brief**

------------------------------------------------------------------------

**[display msdp brief**]命令用来显示MSDP对等体的简要信息。

【命令】

**[display msdp** [ **vpn-instance** *vpn-instance-name*  **brief** [ **state** { **connect** \| **disabled** \| **established** \| **listen** \| **shutdown** } ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

**[state**]：显示处于指定状态下MSDP对等体的简要信息。如果未指定本参数，将显示处于所有状态下MSDP对等体的简要信息。

**[connect**]：表示连接状态。

**[disabled**]：表示连接失败状态。

**[established**]：表示会话状态。

**[listen**]：表示监听状态。

**[shutdown**]：表示手动关闭状态。

【举例】

\# 显示公网实例中处于所有状态下MSDP对等体的简要信息。

\<Sysname\> display msdp brief

Configured   Established  Listen       Connect      Shutdown     Disabled

1            1            0            0            0            0

Peer address    State       Up/Down time    AS         SA count   Reset count

20.20.20.20     Established 00:00:13        100        0          0

表1-1 display msdp brief命令显示信息描述表

字段

描述

Configured

已配置的MSDP对等体的数量

Established

处于Established状态的MSDP对等体的数量

Listen

处于Listen状态的MSDP对等体的数量

Connect

处于Connect状态的MSDP对等体的数量

Shutdown

处于Shutdown状态的MSDP对等体的数量

Disabled

处于Disabled状态的MSDP对等体的数量

Peer address

MSDP对等体的地址

State

MSDP对等体的状态：

·Established：连接建立，处于会话状态

·Listen：连接建立，本地作为服务器端，处于监听状态

·Connect：连接未建立，本地作为客户端，处于连接状态

·Shutdown：被关闭状态

·Disabled：连接失败状态

Up/Down time

MSDP对等体连接已建立/失败的时长

AS

MSDP对等体所在自治系统的号码，"?"表示无法获得自治系统号码

SA count

缓存中从该MSDP对等体获得的（S，G）表项的数量

Reset count

MSDP对等体连接复位的次数

**MSDP \-- MSDP配置命令 \-- display msdp peer-status**

------------------------------------------------------------------------

**[display msdp peer-status**]命令用来显示MSDP对等体的详细状态信息。

【命令】

**[display msdp ** **vpn-instance** *vpn-instance-name* ] **peer-status** [ *peer-address* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[peer-address*]：显示指定MSDP对等体的信息。如果未指定本参数，将显示所有MSDP对等体的信息。

【举例】

\# 显示公网实例MSDP对等体20.20.20.20的详细状态信息。

\<Sysname\> display msdp peer-status 20.20.20.20

MSDP peer 20.20.20.20; AS 100

 Description:

 Information about connection status:

   State: Disabled

   Up/down time: 14:41:08

   Resets: 0

   Connection interface: LoopBack0 (20.20.20.30)

   Received/sent messages: 867/867

   Discarded input messages: 0

   Discarded output messages: 0

   Elapsed time since last connection or counters clear: 14:42:40

   Mesh group peer joined: momo

   Last disconnect reason: Hold timer expired with truncated message

   Truncated packet: 5 bytes in buffer, type: 1, length: 20, without packet time: 75s

 Information about (Source, Group)-based SA filtering policy:

   Import policy: None

   Export policy: None

 Information about SA-Requests:

   Policy to accept SA-Requests: None

   Sending SA-Requests status: Disable

 Minimum TTL to forward SA with encapsulated data: 0

 SAs learned from this peer: 0, SA cache maximum for the peer: 4294967295

 Input queue size: 0, Output queue size: 0

 Counters for MSDP messages:

   RPF check failure: 0

   Incoming/outgoing SA: 0/0

   Incoming/outgoing SA-Request: 0/0

   Incoming/outgoing SA-Response: 0/0

   Incoming/outgoing Keepalive: 867/867

   Incoming/outgoing Notification: 0/0

   Incoming/outgoing Traceroutes in progress: 0/0

   Incoming/outgoing Traceroute reply: 0/0

   Incoming/outgoing Unknown: 0/0

   Incoming/outgoing data packet: 0/0

表1-2 display msdp peer-status命令显示信息描述表

字段

描述

MSDP peer

MSDP对等体的地址

AS

MSDP对等体所在自治系统的号码，"?"表示无法获得自治系统号码

State

MSDP对等体的状态：

·Established：连接建立，处于会话状态

·Listen：连接建立，本地作为服务器端，处于监听状态

·Connect：连接未建立，本地作为客户端，处于连接状态

·Shutdown：关闭状态

·Disabled：连接失败状态

Up/Down time

MSDP对等体连接已建立/失败的时长

Resets

MSDP对等体连接复位的次数

Connection interface

用于与对端对等体地址建立TCP连接的接口及其IP地址

Received/sent messages

MSDP通过该连接接收和发送的报文数目

Discarded input messages

丢弃的入报文数目

Discarded output messages

丢弃的出报文数目

Elapsed time since last connection or counters clear

最近一次清除该MSDP对等体信息时刻距现在的时间

Mesh group peer joined

该对等体加入全连接组的名称，注意如果未加入全连接组则不显示此行信息

Last disconnect reason

与该对等体的连接上一次断开的原因，如果为空表示与该对等体建立连接以来还没有断开过：

·Hold timer expired without message：Hold timer超时，且此时接收缓冲区中没有任何报文

·Hold timer expired with truncated message：Hold timer超时，且此时接收缓冲区中有不完整的报文：

a.bytes in buffer：断开连接时接收缓冲区中数据的实际长度

b.type：断开连接时接收缓冲区中报文的类型

c.length：断开连接时接收缓冲区中报文的长度，注意如果报文过小无法解析出这个字段则不显示该信息

d.without packet time：断开连接的时间到最后一次处理报文的时间间隔

·Remote peer has been closed：接收报文时发现对等体已经被关闭

·TCP ERROR/HUP event received：发送报文时TCP socket收到ERROR/HUP事件

·Illegal message received：接收到了不合法的报文

·Notification received：接收到了Notification报文

·Reset command executed：用户执行了**reset msdp peer**命令

·Shutdown command executed：用户执行了**shutdown**命令

·Interface downed：收到与对等体建立连接的接口down的事件

Information about (Source, Group)-based SA filtering policy

SA报文过滤列表信息：

·Import policy：接收指定MSDP对等体的SA报文的过滤列表

·Export policy：转发指定MSDP对等体的SA报文的过滤列表

Information about SA-Requests

SA请求报文信息：

·Policy to accept SA-Requests：针对来自指定MSDP对等体SA请求报文的过滤规则，None表示不对SA请求报文进行过滤

·Sending SA-Requests status：是否使能在收到一个新的组加入报文时，向其指定的MSDP对等体发送SA请求报文

Minimum TTL to forward SA with encapsulated data

封装在SA报文中的组播数据包的最小TTL值

SAs learned from this peer

已缓存从指定MSDP对等体学到的（S，G）表项的数量

SA cache maximum for the peer

可缓存从指定MSDP对等体学到的（S，G）表项的最大数量

Input queue size

接收缓冲区中所缓存的数据长度

Output queue size

发送缓冲区中所缓存的数据长度

Counters for MSDP messages

MSDP报文的统计数：

·RPF check failure：未通过RPF检查而被丢弃的SA报文的统计数

·Incoming/outgoing SA：接收和发送的SA报文的统计数

·Incoming/outgoing SA-Request：接收和发送的SA请求报文的统计数

·Incoming/outgoing SA-Response：接收和发送的SA回应报文的统计数

·Incoming/outgoing Keepalive：接收和发送的Keepalive报文的统计数

·Incoming/outgoing Notification：接收和发送的Notification报文的统计数

·Incoming/outgoing Traceroutes in progress：接收和发送的Traceroute in progress报文的统计数

·Incoming/outgoing Traceroute reply：接收和发送的Traceroute replys报文的统计数

·Incoming/outgoing Unknown：接收和发送的无法识别类型报文的统计数

·Incoming/outgoing data packet：接收和发送的封装有组播数据的SA报文的统计数

**MSDP \-- MSDP配置命令 \-- display msdp sa-cache**

------------------------------------------------------------------------

**[display msdp sa-cache**]命令用来显示SA缓存中的（S，G）表项信息。

【命令】

**[display msdp ** **vpn-instance** *vpn-instance-name* ] **sa-cache**[ [ *group-address* \| *source-address* \| *as-number* ] \*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[group-address*]：显示包含指定组播组地址的信息，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，将显示包含所有组播组地址的信息。

*[source-address*]：显示包含指定组播源地址的信息。如果未指定本参数，将显示包含所有组播源地址的信息。

*[as-number*]：显示指定自治系统的信息，取值范围为1～4294967295。如果未指定本参数，将显示所有自治系统的信息。

【使用指导】

只有配置了**cache-sa-enable**命令之后，执行本命令才会有相应的显示。

【举例】

\# 显示公网实例SA缓存中的（S，G）表项信息。

\<Sysname\> display msdp sa-cache

Total Source-Active Cache - 5 entries

Matched 5 entries

Source          Group           Origin RP       Pro  AS         Uptime   Expires

10.10.1.2       225.0.0.1       10.10.10.10     BGP  100        00:00:11 00:05:49

10.10.1.2       225.0.0.2       10.10.10.10     BGP  100        00:00:11 00:05:49

10.10.1.2       225.0.0.3       10.10.10.10     BGP  100        00:00:11 00:05:49

10.10.1.2       225.0.0.4       10.10.10.10     BGP  100        00:00:11 00:05:49

10.10.1.2       225.0.0.5       10.10.10.10     BGP  100        00:00:11 00:05:49

表1-3 display msdp sa-cache命令显示信息描述表

字段

描述

Total Source-Active Cache

SA缓存中组播源的总数

Matched

MSDP匹配的组播源总数

Source

组播源源地址

Group

组播源组地址

Origin RP

生成该（S，G）表项的源RP地址

Pro

源RP的自治系统号码来源于何种协议类型，"?"表示无法获得协议类型

AS

源RP的自治系统号码，"?"表示无法获得自治系统号码

Uptime

（S，G）表项缓存已存在的时间

Expires

（S，G）表项缓存超时剩余时间

【相关命令】

·**cache-sa-enable**

**MSDP \-- MSDP配置命令 \-- display msdp sa-count**

------------------------------------------------------------------------

**[display msdp sa-count**]命令用来显示SA缓存中（S，G）表项的数量。

【命令】

**[display msdp ** **vpn-instance** *vpn-instance-name* ] **sa-count** [ *as-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[as-number*]：显示指定自治系统的信息，取值范围为1～4294967295。如果未指定本参数，将显示所有自治系统的信息。

【使用指导】

只有配置了**cache-sa-enable**命令之后，执行本命令才会有相应的显示。

【举例】

\# 显示公网实例SA缓存中（S，G）表项的数量。

\<Sysname\> display msdp sa-count

(S, G) entries statistics, counted by peer

  Peer address       SA count

  10.10.10.10        5

(S, G) entries statistics, counted by AS

  AS         Source count        Group count

  ?          3                   3

5 (S, G) entries in total

表1-4 display msdp sa-count命令显示信息描述表

字段

描述

(S, G) entries statistics, counted by peer

按照对等体，统计缓存中（S，G）表项的数量

Peer address

发送SA报文的MSDP对等体地址

SA count

来自该对等体的（S，G）表项数量

(S, G) entries statistics, counted by AS

按照源RP所属的自治系统，统计缓存中（S，G）表项的数量

AS

自治系统号码，"?"表示无法获得自治系统号码

Source count

来自该自治系统的组播源的统计数

Group count

来自该自治系统的组播组的统计数

(S, G) entries in total

（S，G）表项的总数

【相关命令】

·**cache-sa-enable**

**MSDP \-- MSDP配置命令 \-- encap-data-enable**

------------------------------------------------------------------------

**[encap-data-enable**]命令用来使能在SA报文中封装组播数据报文。

**[undo encap-data-enable**]命令用来恢复缺省情况。

【命令】

**[encap-data-enable**]

**[undo encap-data-enable**]

【缺省情况】

在SA报文中只包含（S，G）表项，不封装组播数据报文。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在公网实例中使能在SA报文中封装组播数据报文。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp encap-data-enable

**MSDP \-- MSDP配置命令 \-- import-source**

------------------------------------------------------------------------

**[import-source**]命令用来配置SA报文的创建规则。

**[undo import-source**]命令用来取消SA报文的创建规则。

【命令】

**[import-source** [ **acl** *acl-number* ]]

**[undo import-source**]

【缺省情况】

在创建SA报文时，对其通告的（S，G）表项不作限制，即SA报文通告域内所有的（S，G）表项。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本或高级ACL的编号，取值范围为2000～3999。如果指定了本参数，则对通告的（S，G）表项进行过滤；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则过滤掉所有（S，G）表项。在进行规则匹配时，对ACL规则中的协议号将不作检查。

【使用指导】

·对于IPv4基本ACL，该ACL规则中的**source**参数用来指定组播组的地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv4高级ACL，该ACL规则中的**source**参数用来指定组播源的地址范围，**destination**参数用来指定组播组的地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·除了可以使用本命令控制SA报文的创建，还可以使用**peer sa-policy**命令控制SA报文的接收和转发。

【举例】

\# 在公网实例中配置MSDP对等体创建SA报文时，通告组播路由表中的特定的（S，G）表项：组播源在10.10.0.0/16网段，组播组地址为225.1.0.0/16。

\<Sysname\> system-view

Sysname acl advanced 3101

Sysname-acl-ipv4-adv-3101 rule permit ip source 10.10.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255

Sysname-acl-ipv4-adv-3101 quit

Sysname msdp

Sysname-msdp import-source acl 3101

【相关命令】

·**peer sa-policy**

**MSDP \-- MSDP配置命令 \-- msdp**

------------------------------------------------------------------------

**[msdp**]命令用来使能MSDP，并进入MSDP视图。

**[undo msdp**]命令用来关闭MSDP，并清除MSDP视图下的所有配置，以释放MSDP占用的资源。

【命令】

**[msdp** [ **vpn-instance** *vpn-instance-name* ]]

**[undo msdp** [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

MSDP处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

【使用指导】

只有在相应实例中先使能了IP组播路由，本命令才能生效。

【举例】

\# 使能公网实例中的IP组播路由，并使能公网实例中的MSDP、进入公网实例MSDP视图。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname msdp

Sysname-msdp

【相关命令】

·**multicast routing**（IP组播命令参考/组播路由与转发）

**MSDP \-- MSDP配置命令 \-- originating-rp**

------------------------------------------------------------------------

**[originating-rp**]命令用来将接口配置为创建SA报文的生成RP。

**[undo originating-rp**]命令用来恢复缺省情况。

【命令】

**[originating-rp** *interface-type interface-number*]

**[undo originating-rp**]

【缺省情况】

创建SA报文的RP为实际RP。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。

【举例】

·路由应用：

\# 在公网实例中将接口GigabitEthernet1/0/1配置为创建SA报文的生成RP。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp originating-rp gigabitethernet 1/0/1

·交换应用：

\# 在公网实例中将接口Vlan-interface100配置为创建SA报文的生成RP。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp originating-rp vlan-interface 100

**MSDP \-- MSDP配置命令 \-- peer**

------------------------------------------------------------------------

**[peer**]命令用来创建MSDP对等体。

**[undo** **peer**]命令用来删除MSDP对等体。

【命令】

**[peer ***peer-address* **connect-interface** *interface-type interface-number*]

**[undo peer ***peer-address*]

【缺省情况】

没有创建MSDP对等体。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

**[connect-interface** *interface-type interface-number*]：指定接口类型和接口编号，本地路由器以该接口的主地址为源IP与远端MSDP对等体建立TCP连接。

【使用指导】

在执行其它**peer**命令之前必须先执行本命令，否则系统将提示该MSDP对等体不存在。

【举例】

·路由应用：

\# 在公网实例中把使用IP地址125.10.7.6的路由器配置成为本地路由器的MSDP对等体，接口GigabitEthernet1/0/1为本地连接端口。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp peer 125.10.7.6 connect-interface gigabitethernet 1/0/1

·交换应用：

\# 在公网实例中把使用IP地址125.10.7.6的路由器配置成为本地交换机的MSDP对等体，接口Vlan-interface100为本地连接端口。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp peer 125.10.7.6 connect-interface vlan-interface 100

**MSDP \-- MSDP配置命令 \-- peer description**

------------------------------------------------------------------------

**[peer description**]命令用来配置MSDP对等体的描述信息。

**[undo peer description**]命令用来删除MSDP对等体的描述信息。

【命令】

**[peer ***peer-address ***description** *text*]

**[undo peer ***peer-address*** description**]

【缺省情况】

MSDP对等体没有描述信息。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

*[text*]：MSDP对等体的描述信息，为1～80个字符的字符串，可以包含空格，区分大小写。

【举例】

\# 在公网实例中为IP地址为125.10.7.6的MSDP对等体添加描述信息"CustomerA"。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp peer 125.10.7.6 description CustomerA

**MSDP \-- MSDP配置命令 \-- peer mesh-group**

------------------------------------------------------------------------

**[peer mesh-group**]命令用来把MSDP对等体加入全连接组。

**[undo** **peer mesh-group**]命令用来把MSDP对等体从全连接组中删除。

【命令】

**[peer ***peer-address*** mesh-group** *name*]

**[undo peer ***peer-address*** mesh-group**]

【缺省情况】

MSDP对等体不属于任何全连接组。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

*[name*]：全连接组的名称，为1～32个字符的字符串，不可以包含空格，区分大小写。

【举例】

\# 在公网实例中把IP地址为125.10.7.6的MSDP对等体加入到全连接组"Group1"。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp peer 125.10.7.6 mesh-group Group1

**MSDP \-- MSDP配置命令 \-- peer minimum-ttl**

------------------------------------------------------------------------

**[peer minimum-ttl**]命令用来配置封装在SA报文中组播数据报文的最小TTL值。

**[undo** **peer minimum-ttl**]命令用来恢复缺省情况。

【命令】

**[peer ***peer-address* **minimum-ttl** *ttl-value*]

**[undo** **peer** *peer-address* **minimum-ttl**]

【缺省情况】

封装在SA报文中组播数据报文的最小TTL值为0。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

*[ttl-value*]：指定最小TTL值，取值范围为0～255。

【举例】

\# 在公网实例中进行配置，使只有TTL值大于或等于10的组播数据报文才能被封装到SA报文中，并转发给MSDP对等体110.10.10.1。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp peer 110.10.10.1 minimum-ttl 10

**MSDP \-- MSDP配置命令 \-- peer password**

------------------------------------------------------------------------

**[peer password**]命令用来配置MSDP对等体建立TCP连接时进行MD5认证。

**[undo** **peer password**]命令用来恢复缺省情况。

【命令】

**[peer **]*peer-address*[ **password** { **cipher** \| **simple** } *password*]

**[undo** **peer** *peer-address* **password**]

【缺省情况】

MSDP对等体建立TCP连接时不进行MD5认证。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

**[cipher**]：表示以密文形式设置MD5认证密钥。

**[simple**]：表示以明文形式设置MD5认证密钥。

*[password*]：MD5认证密钥内容，区分大小写。如果以密文形式设置，则为33～137个字符的字符串；如果以明文形式设置，则为1～80个字符的字符串。

【使用指导】

·参与MD5认证的两端MSDP对等体必须配置相同的认证方式和密钥，否则将由于不能通过认证而无法建立TCP连接。

·以明文或密文方式设置的MD5认证密钥，均将以密文方式保存在配置文件中。

【举例】

\# 在公网实例中配置与MSDP对等体10.1.100.1建立TCP连接时进行MD5认证，并以明文方式设置密钥为aabbcc（在对端也要进行类似配置）。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp peer 10.1.100.1 password simple aabbcc

**MSDP \-- MSDP配置命令 \-- peer request-sa-enable**

------------------------------------------------------------------------

**[peer request-sa-enable**]命令用来使能发送SA请求报文，即当路由器收到新的组加入报文时，向其MSDP对等体发送SA请求报文。

**[undo peer request-sa-enable**]命令用来禁止发送SA请求报文。

【命令】

**[peer** *peer-address* **request-sa-enable**]

**[undo peer** *peer-address* **request-sa-enable**]

【缺省情况】

路由器收到新的组加入报文时，不向其MSDP对等体发送SA请求报文，而是等待下一周期SA报文的到来。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

【使用指导】

在使能发送SA请求报文功能之前，必须首先关闭SA报文缓存机制，否则设备不会向外发送SA请求报文。

【举例】

\# 在公网实例中关闭SA报文缓存机制，并配置当路由器收到新的组加入报文时，向其MSDP对等体125.10.7.6发送SA请求报文。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp undo cache-sa-enable

Sysname-msdp peer 125.10.7.6 request-sa-enable

【相关命令】

·**cache-sa-enable**

·**display msdp peer-status**

**MSDP \-- MSDP配置命令 \-- peer sa-cache-maximum**

------------------------------------------------------------------------

**[peer sa-cache-maximum**]命令用来配置可缓存从指定MSDP对等体学到的（S，G）表项的最大数量。

**[undo** **peer sa-cache-maximum**]命令用来恢复缺省情况。

【命令】

**[peer ***peer-address ***sa-cache-maximum** *sa-limit*]

**[undo peer ***peer-address ***sa-cache-maximum**]

【缺省情况】

可缓存从任一MSDP对等体学到的（S，G）表项的最大数量为4294967295。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

*[sa-limit*]：指定可缓存的（S，G）表项的最大数量，取值范围为1～4294967295。

【举例】

\# 在公网实例中配置最多可缓存100条从MSDP对等体125.10.7.6学到的（S，G）表项。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp peer 125.10.7.6 sa-cache-maximum 100

【相关命令】

·**display msdp brief**

·**display msdp peer-status**

·**display msdp sa-count**

**MSDP \-- MSDP配置命令 \-- peer sa-policy**

------------------------------------------------------------------------

**[peer sa-policy**]命令用来配置接收或转发SA报文的过滤规则。

**[undo** **peer sa-policy**]命令用来删除接收或转发SA报文的过滤规则。

【命令】

**[peer ***peer-address*** sa-policy**[ { **export** \| **import** } [ **acl** *acl-number* ]]]

**[undo peer ***peer-address*** sa-policy**[ { **export** \| **import** }]]

【缺省情况】

不对接收或转发的SA报文进行过滤，即接收或转发所有SA报文。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[import**]：表示对来自指定MSDP对等体的SA报文进行过滤。

**[export**]：表示对转发给指定MSDP对等体的SA报文进行过滤。

*[peer-address*]：指定MSDP对等体的地址。

*[acl-number*]：指定IPv4高级ACL的编号，取值范围为3000～3999。如果指定了本参数，则对SA报文进行过滤；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则过滤掉所有SA报文。

【使用指导】

·ACL规则中的**source**参数用来指定组播源的地址范围，**destination**参数用来指定组播组的地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·除了可以使用本命令控制SA报文的接收和转发，还可以使用**import-source**命令控制SA报文的创建。

【举例】

·路由应用：

\# 在公网实例中配置向MSDP对等体125.10.7.6只转发通过IPv4高级ACL 3100过滤的SA报文。

\<Sysname\> system-view

Sysname acl advanced 3100

Sysname-acl-ipv4-adv-3100 rule permit ip source 170.15.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255

Sysname-acl-ipv4-adv-3100 quit

Sysname msdp

Sysname-msdp peer 125.10.7.6 connect-interface gigabitethernet 1/0/1

Sysname-msdp peer 125.10.7.6 sa-policy export acl 3100

·交换应用：

\# 在公网实例中配置向MSDP对等体125.10.7.6只转发通过IPv4高级ACL 3100过滤的SA报文。

\<Sysname\> system-view

Sysname acl advanced 3100

Sysname-acl-ipv4-adv-3100 rule permit ip source 170.15.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255

Sysname-acl-ipv4-adv-3100 quit

Sysname msdp

Sysname-msdp peer 125.10.7.6 connect-interface vlan-interface 100

Sysname-msdp peer 125.10.7.6 sa-policy export acl 3100

【相关命令】

·**display msdp peer-status**

·**import-source**

**MSDP \-- MSDP配置命令 \-- peer sa-request-policy**

------------------------------------------------------------------------

**[peer sa-request-policy**]命令用来配置SA请求报文的过滤规则。

**[undo** **peer sa-request-policy**]命令用来删除SA请求报文的过滤规则。

【命令】

**[peer ***peer-address* **sa-request-policy** [ **acl** *acl-number* ]]

**[undo peer ***peer-address* **sa-request-policy**]

【缺省情况】

不对SA请求报文进行过滤。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

*[acl-number*]：指定IPv4基本ACL的编号，取值范围为2000～2999。如果指定了本参数，则对SA请求报文进行过滤；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则过滤掉所有SA请求报文。

【使用指导】

ACL规则中的**source**参数用来指定组播组的地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

\# 在公网实例中配置SA请求报文的过滤规则：在来自MSDP对等体175.58.6.5的SA请求报文中，除了来自组地址范围225.1.1.0/24的被接收外，其它的均被忽略。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit source 225.1.1.0 0.0.0.255

Sysname-acl-ipv4-basic-2001 quit

Sysname msdp

Sysname-msdp peer 175.58.6.5 sa-request-policy acl 2001

**MSDP \-- MSDP配置命令 \-- reset msdp peer**

------------------------------------------------------------------------

**[reset msdp peer**]命令用来重置与MSDP对等体的TCP连接，并清除MSDP对等体的所有统计信息。

【命令】

**[reset msdp** [ **vpn-instance** *vpn-instance-name*  **peer**  *peer-address* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：重置指定VPN实例的TCP连接，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将重置公网实例的TCP连接。

*[peer-address*]：重置与指定MSDP对等体的TCP连接。如果未指定本参数，将重置与所有MSDP对等体的TCP连接。

【举例】

\# 重置公网实例中与MSDP对等体125.10.7.6的TCP连接，并清除该MSDP对等体的所有统计信息。

\<Sysname\> reset msdp peer 125.10.7.6

**MSDP \-- MSDP配置命令 \-- reset msdp sa-cache**

------------------------------------------------------------------------

**[reset msdp sa-cache**]命令用来清除SA缓存中的（S，G）表项。

【命令】

**[reset msdp ** **vpn-instance** *vpn-instance-name* ] **sa-cache ** *group-address*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。

*[group-address*]：从SA缓存中清除指定组播组所对应的（S，G）表项，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，将从SA缓存中清除所有的（S，G）表项。

【举例】

\# 清除公网实例SA缓存中组播组225.5.4.3所对应的（S，G）表项。

\<Sysname\> reset msdp sa-cache 225.5.4.3

【相关命令】

·**cache-sa-enable**

·**display msdp sa-cache**

**MSDP \-- MSDP配置命令 \-- reset msdp statistics**

------------------------------------------------------------------------

**[reset msdp statistics**]命令用来在不重置MSDP对等体的情况下，清除MSDP对等体的统计信息。

【命令】

**[reset msdp ** **vpn-instance** *vpn-instance-name* ] **statistics** [ *peer-address* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。

*[peer-address*]：清除指定MSDP对等体的统计信息。如果未指定本参数，将清除所有MSDP对等体的统计信息。

【举例】

\# 清除公网实例MSDP对等体125.10.7.6的统计信息。

\<Sysname\> reset msdp statistics 125.10.7.6

**MSDP \-- MSDP配置命令 \-- shutdown (MSDP view)**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭MSDP对等体连接。

**[undo** **shutdown**]命令用来打开MSDP对等体连接。

【命令】

**[shutdown** *peer-address*]

**[undo shutdown** *peer-address*]

【缺省情况】

MSDP对等体的连接处于开启状态。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

【举例】

\# 在公网实例中关闭MSDP对等体125.10.7.6的连接。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp shutdown 125.10.7.6

【相关命令】

·**display msdp brief**

·**display msdp peer-status**

**MSDP \-- MSDP配置命令 \-- static-rpf-peer**

------------------------------------------------------------------------

**[static-rpf-peer**]命令用来配置静态RPF对等体。

**[undo static-rpf-peer**]命令用来删除静态RPF对等体。

【命令】

**[static-rpf-peer** *peer-address* [ **rp-policy** *ip-prefix-name* ]]

**[undo static-rpf-peer** *peer-address*]

【缺省情况】

不存在任何静态RPF对等体。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-address*]：指定MSDP对等体的地址。

**[rp-policy** *ip-prefix-name*]：指定基于SA报文中RP地址的过滤策略。*ip-prefix-name*表示过滤策略的名称，为1～63个字符的字符串，区分大小写。

【举例】

·路由应用：

\# 在公网实例中将130.10.7.6配置为静态RPF对等体，源RP的地址范围为130.10.0.0/16。

\<Sysname\> system-view

Sysname ip prefix-list list1 permit 130.10.0.0 16 great-equal 16 less-equal 32

Sysname msdp

Sysname-msdp peer 130.10.7.6 connect-interface gigabitethernet 1/0/1

Sysname-msdp static-rpf-peer 130.10.7.6 rp-policy list1

·交换应用：

\# 在公网实例中将130.10.7.6配置为静态RPF对等体，源RP的地址范围为130.10.0.0/16。

\<Sysname\> system-view

Sysname ip prefix-list list1 permit 130.10.0.0 16 great-equal 16 less-equal 32

Sysname msdp

Sysname-msdp peer 130.10.7.6 connect-interface vlan-interface 100

Sysname-msdp static-rpf-peer 130.10.7.6 rp-policy list1

【相关命令】

·**display msdp peer-status**

·**ip prefix-list**

**MSDP \-- MSDP配置命令 \-- timer keepalive**

------------------------------------------------------------------------

**[timer keepalive**]命令用来配置MSDP对等体会话的保活时间和保持时间。

**[undo timer keepalive**]命令用来恢复缺省情况。

【命令】

**[timer** **keepalive** *keepalive* *holdtime*]

**[undo timer keepalive**]

【缺省情况】

MSDP会话的保活时间为60秒，保持时间为75秒。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[keepalive*]：表示保活时间，取值范围为1～21845，单位为秒。

*[holdtime*]：表示保持时间，取值范围为1～65535，单位为秒。

【使用指导】

当MSDP对等体之间建立会话后，会定时互发Keepalive报文（其发送间隔被称为保活时间），以免对端认为会话已中断。如果一端在保持时间内未收到对端的Keepalive报文或其它报文，便断开此会话。由于MSDP对等体之间没有保活时间和保持时间的协商机制，因此必须为两端配置相同的保活时间和保持时间，且保活时间必须小于保持时间。

需要注意的是，本命令会对已建立的MSDP会话立即生效。

【举例】

\# 在公网实例中配置MSDP对等体会话的保活时间和保持时间分别为60秒和180秒。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp timer keepalive 60 180

**MSDP \-- MSDP配置命令 \-- timer retry**

------------------------------------------------------------------------

**[timer retry**]命令用来配置建立MSDP对等体连接的重试周期。

**[undo timer retry**]命令用来恢复缺省情况。

【命令】

**[timer retry ***interval*]

**[undo timer retry**]

【缺省情况】

建立MSDP对等体连接的重试周期为30秒。

【视图】

MSDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示重试周期，取值范围为1～60，单位为秒。

【举例】

\# 在公网实例中配置建立MSDP对等体连接的重试周期为60秒。

\<Sysname\> system-view

Sysname msdp

Sysname-msdp timer retry 60
