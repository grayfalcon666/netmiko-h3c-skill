<!-- CMD-INDEX
  debugging ipsec                     | ]                | L6
  debugging ike                       | 用户视图             | L1252
-->

**IPsec \-- IPsec调试命令 \-- debugging ipsec**

------------------------------------------------------------------------

【命令】

**[debugging ipsec**[ { **all** \| **error** \| **event** \| **packet** [ { **policy** \| **ipv6-policy** } *policy-name* [ *seq-number* ] \| **profile** *profile-name* \| **spi** { *ipv4-address \|* **ipv6** *ipv6-address* } { **ah** \| **esp** *spi-number* } \| **remote-address** { *ipv4-address \|* **ipv6** *ipv6-address* } }]]

**[undo**[ **debugging ipsec** { **all** \| **error** \| **event** \| **packet** }]]

【视图】]

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示IPsec所有调试信息开关。

**[error**]：表示IPsec错误调试信息开关。

**[event**]：表示IPsec事件调试信息开关。

**[packet**]：表示IPsec报文调试信息开关。

**[policy**]：指定IPsec安全策略。

**[ipv6-policy**]：指定IPv6 IPsec安全策略。

*[policy-name*]：表示IPsec安全策略的名称，为1～63个字符的字符串，不区分大小写。

*[seq-number*]：表示IPsec安全策略表项的顺序号，取值范围为1～6553。

**[profile ***profile-name*]：指定IPsec安全框架，*profile-name*表示IPsec安全框架的名称，为1～63个字符的字符串，不区分大小写。

**[spi**]：指定SPI的三元组信息（SPI、安全协议、IPsec隧道对端地址）。

*[ipv4-address*]：指定IPsec隧道对端的IPv4地址。

**[ipv6 ***ipv6-address*]：指定IPsec隧道对端的IPv6地址。

**[ah**]：指定AH协议。

**[esp**]：指定ESP协议。

*[spi-number*]：表示SPI的序号，取值范围为256～4294967295。

**[remote-address**]：指定IPsec隧道对端的IP地址。

*[ipv4-address*]：指定IPsec隧道对端的IPv4地址。

**[ipv6 ***ipv6-address*]：指定IPsec隧道对端的IPv6地址。

【描述】

**[debugging ipsec**]命令用来打开IPsec调试信息开关。**undo debugging ipsec**命令用来关闭IPsec调试信息开关。

缺省情况下，IPsec的调试信息开关处于关闭状态。

表1-1 debugging ipsec error命令输出信息描述表

字段

描述

Failed to allocate memory.

分配内存失败

Failed to set an IPv6 header variable to 0.

将IPv6头可变部分置零时出错

Failed to add SP entry in kernel.

向内核添加SP（Security Policy，安全策略） entry失败

Failed to find SP entry in kernel.

在内核中查找SP entry失败

The SP doesn\'t exist in kernel.

内核中不存在SP

The IPsec tunnel doesn\'t exist in kernel.

内核中不存在IPsec隧道

The DPD doesn\'t exist in kernel.

内核中不存在DPD（Dead Peer Detection，对等体存活检测）

Failed to require CCFJOB structure.

申请CCF JOB结构失败

Failed to encrypt CCF.

CCF加密失败

The SA doesn\'t exist.

SA不存在

Failed to decrypt CCF.

CCF解密失败

Failed to create CCF session.

创建CCF session失败

The packet hash values don't match.

解封装后的报文哈希值不匹配

No SA in IPsec tunnel.

IPsec隧道中没有SA

Can\'t find next SA in AH-ESP mode.

AH-ESP模式下，下一个SA找不到

IPsec tunnel has been deleted or updated when fast forwarding is performed.

快转时IPsec隧道已经被删除或更新

Packet should have been encrypted by IPsec.

报文本应该被IPsec保护

SA has been deleted or updated when fast forwarding is performed.

快转时SA已经被删除或更新

In transport mode, SA address doesn't match packet address.

传输模式下，报文中的地址与SA中的不一致

The packet is too big: size = *size.*

报文过大，报文大小为*size*

Failed to add outer IP header.

添加外部IP头失败

The packet is not an IPsec packet.

非IPsec报文

Can\'t find SP.

找不到SP

Can\'t find SA by SP.

根据SP查找不到对应的SA

Failed to add node to invalid SPI hash table.

向无效SPI哈希表添加节点失败

Failed to add SA to IPsec tunnel.

向IPsec隧道添加SA失败

Failed to connect to the IPsec daemon.

连接IPsec用户态守护进程失败

The block-flow-table doesn\'t exist.

阻流表不存在

The ACL mode is wrong.

ACL模式错误

Received replayed packet.

收到了重放包

Can't find SA when processing ICMP too big packet: SPI = *spi.*

在处理ICMP过大报文过程中找不到SA，SPI值为*spi*

No SA in IPsec tunnel.

IPsec隧道没有任何SA

Invalid IPsec profile index.

无效的IPsec profile索引

Failed to get IPsec profile name.

获取IPsec profile名称失败

After decryption, source address check failed.

解封装后源地址检查失败

Failed to create lipc socket.

创建lipc socket失败

The SP already exists.

SP已经存在

Failed to add SP in kernel.

向内核添加SP失败

Failed to add profile SP in kernel

向内核添加profile SP失败

Failed to add SA in kernel.

向内核添加SA失败

Failed to delete SA in kernel.

删除内核中的SA失败

Failed to add IPsec tunnel in kernel.

向内核添加IPsec隧道失败

Failed to delete tunnel in kernel.

删除内核中的IPsec隧道失败

Failed to add DPD in kernel.

向内核添加DPD失败

Failed to delete DPD in kernel.

删除内核中的DPD失败

The SP entry doesn\'t exist in kernel.

内核SP entry不存在

Number of SAs exceeded the limit.

SA数量超过最大值

Failed to create IPsec IF-CB.

创建IPsec接口控制块失败

Failed to set IPsec IF-CB to interface

(ifIndex = *ifindex*)

向接口上设置IPsec接口控制块失败，其接口索引为*ifindex*

Failed to change the aging timer for block-flow-table.

修改阻流表的老化时间失败

Failed to create policy/template.

由命令行创建策略/模板失败

Failed to create policy/template group.

由命令行创建策略组/模板组失败

Failed to initialize policy hash table.

策略哈希表初始化失败

Failed to recover policy/template.

恢复策略/模板失败

Failed to recover policy/template group.

恢复策略组/模板组失败

Failed to recover transform reference.

恢复提议的引用关系失败

Failed to save policy/template/profile info to DBM.

向DBM中保存策略/模板/profile信息失败

Failed to delete policy/template/profile info from DBM.

从DBM中删除策略/模板/profile信息失败

Failed to save system configuration to DBM.

向DBM中保存系统配置失败

Failed to save transform configuration to DBM.

向DBM中保存提议配置失败

Failed to get system configuration from DBM.

从DBM中读取系统配置失败

Failed to save source interface configuration to DBM.

向DBM中保存源接口配置失败

Failed to save interface configuration to DBM.

向DBM中保存接口配置失败

Failed to get interface name by ifIndex.

通过接口索引获取接口名称失败

Failed to start IPsec daemon.

启动IPsec进程失败

Failed to alloc SP index.

分配SP索引失败

Failed to malloc SP.

分配SP资源失败

Failed to malloc SP entry.

分配SP entry资源失败

Failed to update kernel SP entry.

更新内核的SP entry失败

Failed to find SP entry.

查找SP entry 失败

Failed to add SP to array.

将SP加入数组失败

Failed to find template group.

查找模板组失败

Failed to add policy SP to kernel

向内核添加policy SP失败

Failed to find policy SP.

查找policy SP失败

Failed to add profile SP to kernel.

向内核添加profile SP失败

Failed to get SP when filling ISAKMP SA data.

填充ISAKMP SA数据时获取SP失败

Failed to get DPD when filling ISAKMP SA data.

填充ISAKMP SA数据时获取DPD失败

Failed to add IPsec tunnel when adding manual SA.

添加手工SA时添加IPsec隧道失败

Failed to add IPsec tunnel during ISSU update process.

进行ISSU升级时，添加IPsec隧道失败

Failed to add SA when adding manual SA.

添加手工SA时添加SA失败

Failed to fill SA when adding ISAKMP SA.

添加ISAKMP方式SA时填充SA失败

Failed to add IPsec tunnel when adding ISAKMP SA.

添加ISAKMP方式SA时添加IPsec隧道失败

Failed to add timer when adding ISAKMP SA.

添加ISAKMP方式SA时添加定时器失败

Failed to alloc SPI.

分配SPI失败

Failed to alloc new SPI for ISAKMP SA.

分配ISAKMP方式SA的新SPI失败

Failed to alloc larva SA index when adding larva SA.

添加临时SA时分配临时SA索引失败

Failed to add larval SA.

添加临时SA失败

Failed to alloc SA index.

分配SA索引失败

Failed to alloc ISAKMP SA index.

分配ISAKMP方式SA的索引失败

Failed to alloc manual SA index.

分配手工方式SA的索引失败

Failed to add SA.

添加SA失败

Failed to add SA to kernel.

向内核添加SA失败

Failed to add SA to kernel during ISSU update process.

当进行ISSU升级时向内核添加SA失败

Failed to alloc DPD Index.

分配DPD索引失败

Failed to add DPD timer.

添加DPD定时器失败

Failed to add DPD to kernel.

向内核添加DPD失败

Failed to add DPD timer during smooth processing with IKE.

和IKE进行平滑处理时添加DPD定时器失败

Failed to add DPD to kernel during smooth processing with IKE.

和IKE进行平滑处理时向内核添加DPD数据失败

The same outbound profile SA has existed. SPI: *spi* Protocol: *protocol*.

已存在相同的出方向profile SA（IPsec profile生成的SA）。SPI值为*spi*，协议类型为*protocol*

The same outbound policy SA has existed. SPI: *spi*, Remote address: *remote-addr*, Protocol: *protocol*.

已存在相同出方向的policy SA（IPsec policy生成的SA）。SPI值为*SPI*，对端地址为*remote-addr*，协议类型为*protocol*

Failed to generate static route.

新建IPsec隧道时，生成路由信息失败

Failed to add static route.

新建IPsec隧道时，路由模块添加静态路由失败

Failed to delete static route.

删除IPsec隧道时，路由模块删除静态路由失败

Failed to notify route module of starting to smooth IPv4 static routes.

和路由模块平滑路由过程中通知路由模块开始平滑IPv4路由，通知失败

Failed to notify route module of starting to smooth IPv6 static routes.

和路由模块平滑路由过程中通知路由模块开始平滑IPv6路由，通知失败

Failed to subscribe service events.

订阅服务事件失败

表1-2 debugging ipsec event命令输出信息描述表

字段

描述

The IPsec IF-CB(ifIndex = *ifindex*) will be deleted in kernel.

内核中的IPsec的接口控制快（接口序号为*ifindex*）将要被删除掉

Can\'t find block-flow-table.

找不到阻流表

Can\'t find an IPsec tunnel to match the flow.

找不到匹配流的IPsec隧道

IPsec daemon successfully connected.

成功连接到IPsec用户态守护进程

IPsec daemon disconnected.

与用户态守护进程失去连接

Sent SA-Acquire message: SP ID = *ID.*

发送SA协商请求，对应SP的ID为*ID*

Sent SA-Expire message: SP ID = *SPID*, tunnel ID = *TNLID.*

发送SA重协商请求，对应SP的ID为*SPID，*Tunnel ID为*TNLID*

Sent Invalid-SPI message: SPI = *spi.*

发送Invalid-SPI消息， SPI值为*spi*

Sent DPD-Request message: DPD ID = *DPDID*

发送DPD探测请求消息， DPD ID为*DPDID*

Updated outbound SA of IPsec tunnel: SA ID = *saindex.*

更新IPsec隧道出方向的SA，SA序号为*saindex*

Received an interface event message for interface *interface-type interface-num*, event: *event*.

收到响应接口事件消息，接口名称为*interface-type interface-num*，接口事件为*event*

Received interface network layer event message.

收到响应接口网络层事件消息

Received an event message for slot *slot-id*, event: *event*.

收到响应接口板事件消息，板号为*slot-number*，消息类型为*event*

Received an ACL message for ACL *acl-number*, event: *event*.

收到ACL消息，ACL编号为*acl-number*，消息类型为*event*

Received an address message for interface *interface-type interface-num*, event: *event*.

收到地址消息，接口名称为*interface-type interface-num*，消息类型为*event*

Sent notify message to kernel: slot *slot-id*, event: *event*.

发送notify消息给内核，板号为*slot-number*，消息类型为*event*

Sent *msg* to kernel.

向内核发送消息*msg*，msg是消息类型，包括以下几种：

·add SP entry：添加SP entry

·update SP entry：更新SP entry

·delete SP entry：删除SP entry

·add source-if SP entry：添加源接口SP entry

·delete source-if SP entry：删除源接口SP entry

·add SP：添加SP

·update SP：更新SP

·delete SP：删除SP

·add profile SP：添加profile SP

·delete profile SP：删除profile SP

·update profile SP：更新profile SP

Added SA to kernel successfully .

向内核添加SA成功

SA successfully added in kernel.

内核添加SA成功

SA successfully deleted in kernel.

删除内核中的SA成功

Added outbound SA to IPsec tunnel(SA ID = *sa-index*)

向IPsec隧道添加出方向SA(SA索引为*sa-index*)

Added tunnel to kernel successfully.

向内核添加IPsec隧道成功

IPsec tunnel successfully added in kernel.

内核添加IPsec隧道成功

IPsec tunnel successfully deleted in kernel.

删除内核中的IPsec隧道成功

IPsec tunnel successfully added to list.

向链表添加IPsec隧道成功

IPsec tunnel added to aggregation-hash

向聚合哈希表中添加IPsec隧道成功

Added SP entry.

添加SP entry

Added SP by policy.

根据策略添加SP

SP entry successfully added in kernel.

内核成功添加SP entry

SP successfully added in kernel.

内核成功添加SP

Added policy SA by manual SP, SP index: *index*, SP sequence number: *sp-seq*.

成功根据手工SP添加策略SA，SP索引为*sp-index*，SP序号为*sp-seq*

Successfully added an IPsec tunnel during ISSU update process.

在ISSU升级时成功添加IPsec隧道

Added an IPsec tunnel when adding manual SA: tunnel index = *tunnel-id*, tunnel sequence number = *tunnel_seq*.

添加手工SA过程中成功添加IPsec隧道。IPsec隧道索引是*tunnel-id*，IPsec隧道序号是*tunnel_seq*

Added manual SAs. Number of SAs added is *number*.

成功添加手工SA。添加的SA的个数*number*

No. *ordinal-number* SA: index = *sa-id,* sequence number = *sa-seq*.

第*ordinal-number*个SA的索引是*sa-id*，SA的序列号是*sa-seq*

Added SA context to SP.

成功向SP中添加SA内容

Added an IPsec tunnel when adding ISAKMP SA: tunnel index = *tunnel-id*, tunnel sequence number = *tunnel_seq*.

添加ISAKMP方式SA过程中成功添加IPsec隧道。IPsec隧道索引是*tunnel-id*，IPsec隧道序号是*tunnel_seq*

Added ISAKMP SAs. Number of SAs added is *number*. No. *ordinal-number* SA: index = *sa-id,* sequence number = *sa-seq*.

成功添加ISAKMP方式SA。添加的SA的个数*number*，第*ordinal-number*个的SA索引是*sa-id*，SA序号是*sa-seq*

Added SA context to IKE.

向IKE发送SA内容

Timer successfully added when adding ISAKMP SA.

添加ISAKMP方式SA时添加定时器成功

Started to smoothly process SA with IKE.

开始和IKE进行平滑SA

Finished smooth processing SA with IKE.

结束和IKE平滑SA

Started to smoothly process IPsec tunnel with IKE.

开始和IKE进行平滑IPsec隧道

Finished smooth processing IPsec tunnel with IKE.

结束和IKE平滑IPsec隧道

Started to smoothly process DPD with IKE.

开始和IKE进行平滑DPD

Finished smooth processing DPD with IKE.

结束和IKE平滑DPD

Sent *msg* message to slot:*slot-id*, message type is *type-id*.

向*slot-id*号接口板发送*msg*消息，消息ID是*type-id*

消息类型和其对应的类型ID如下：

·debug：调试，类型ID为3

·anti-replay check：抗重放检查，类型ID为4

·decryption check：解封装后检查，类型ID为5

·log switch：log开关，类型ID为6

·idle：空闲，类型ID为7

·global df-bit：全局df-bit设置，类型ID为8

·df-bit：接口df-bit设置，类型ID为9

·all global configuration：所有全局配置，类型ID为10

·add SP entry：添加SP entry，类型ID为11

·update SP entry：更新SP entry，类型ID为12

·delete SP entry：删除SP entry/类型ID为13

·add SP：添加SP/类型ID为14

·update SP：更新SP/类型ID为15

·delete SP：删除SP/类型ID为16

·add profile SP：添加profile SP，类型ID为17

·update profile SP：更新profile SP，类型ID为18

·delete profile SP：删除profile SP，类型ID为19

·add tunnel：添加tunnel，类型ID为20

·delete tunnel：删除tunnel，类型ID为21

·add SA：添加SA，类型ID为22

·delete SA：删除SA，类型ID为23

·update MTU：更新MTU，类型ID为24

·switch SA：切换SA，类型ID为25

·delete block-flow table：删除阻流表/类型ID为26

·add DPD：添加DPD/类型ID为27

·update DPD：更新DPD，类型ID为28

·delete DPD：删除DPD，类型ID为29

·update DPD index of SA：更新SA的DPD索引，类型ID为30

·reset statistics：重置统计计数，类型ID为31

·idle report：idle报告，类型ID为32

·smooth start：平滑开始，类型ID为32

·smooth end：平滑结束，类型ID为34

Adding route: Dest/Mask: *ip-address*/*mask-length*, Next hop: *ip-address* , Source vpn instance: *vpn-name*, Destination vpn instance: *vpn-name*, Tag: *tag-value*, Preference: *preference-num*

新建IPsec隧道时，即将添加一条静态路由信息

·Dest/Mask：目的IP地址/掩码长度

·Next hop：下一跳IP地址

·Source vpn instance：路由目的地址所属的VPN

·Destination vpn instance：路由下一跳地址所属的VPN

·Tag：路由标记

·Preference：路由优先级

Deleting route: Dest/Mask: *ip-address*/*mask-length*, Next hop: *ip-address*, Source vpn instance: *vpn-name*, Destination vpn instance: *vpn-name*, Tag: *tag-value*, Preference: *preference-num*

删除IPsec隧道时，即将删除一条静态路由信息

Successfully added a static route.

新建IPsec隧道时，路由模块添加静态路由成功

Only increased the reference count of the static route but didn\'t add it.

新建IPsec隧道时，发现已经向路由模块添加过相同的静态路由，则不再通知路由模块添加此路由仅增加该路由的引用计数

Successfully deleted a static route.

删除IPsec隧道时，路由模块删除静态路由成功

Only reduced the reference count of the static route but didn\'t delete it.

删除IPsec隧道时，发现两个以上IPsec隧道对应同一条静态路由，则不通知路由模块删除该静态路由仅减少该路由的引用计数

Started to smoothly process the IPv4 static routes.

开始对IPv4静态路由进行平滑处理

Started to smoothly process the IPv6 static routes.

开始对IPv6静态路由进行平滑处理

Finished smooth processing of the IPv4 static routes.

结束对IPv4静态路由的平滑处理

Finished smooth processing of the IPv6 static routes.

结束对IPv6静态路由的平滑处理

Successfully subscribed service events.

成功订阅所有的服务事件

Received a service event: the status of IPv4 route service is up.

接收到一个IPv4路由服务up事件

Received a service event: the status of IPv4route service is down.

接收到一个IPv4路由服务down事件

Received a service event: the status of IPv6 route service is up.

接收到一个IPv6路由服务up事件

Received a service event: the status of IPv6 route service is down.

接收到一个IPv6路由服务down事件

表1-3 debugging ipsec packet命令输出信息描述表

字段

描述

Packet will be sent to CCF for sync-encryption.

报文将被发送到CCF执行同步加密操作

Packet will be sent to CCF for sync-decryption

报文将被发送到CCF执行同步解密操作

Packet will be sent to CCF for asyn-encryption.

报文将被发送到CCF执行异步加密操作

Packet will be sent to CCF for asyn-decryption.

报文将被发送到CCF执行异步解密操作

Found SA with SPI *spi*.

已经找到SPI为*spi*的SA

Packet matches SP *spid*.

报文匹配SP，SP ID为*spid*.

Packet has been encrypted by SA whose SPI is *spi*.

报文已经被SPI为*spi*的SA加密

Packet has been decrypted by SA whose SPI is *spi*.

报文已经被SPI为*spi*的SA解密

ESP auth algorithm: *auth*, ESP encp algorithm: *encp*.

ESP采用的认证算法为*auth*，加密算法为*encp*

AH auth algorithm: *auth*

AH采用的认证算法为*auth*

Src : *src* Dst : *dst* SPI : *spi*

报文的源地址为，目的地址为，SPI值为*spi*

Received IPsec(AH) packet

入方向收到AH报文

Received IPsec(ESP) packet

入方向收到ESP报文

Received IPSec packet from fast forwarding

快转入方向收到IPsec报文

Sent routing protocol packet by IPsec

路由协议报文经由IPsec发送

Sent IPsec packet

报文经由IPsec发送

Sent packet by IPsec fast forwarding

报文经由IPsec快转发送

Added IP fast forwarding entry.

添加快转表项

Added IPv6 fast forwarding entry.

添加IPv6快转表项

Failed to find SA by SP.

根据SP找不到对应的SA

The packet is too big, mtu = *mtu*, packet len = *len*.

报文过大，MTU值为*mtu*，长度为*len*

The reason of dropping packet is *reason*.

报文被丢弃的原因为*reason*，包括以下几种：

·Packet too long：报文太长

·Invalid SPI：无效SPI

·No available SA：找不到SA

·No available IPsec tunnel：找不到IPsec隧道

·Encryption failed：加密失败

·Decryption failed：解密失败

·Loop too many times：本机循环次数过多

·ACL check failed：ACL检查失败

·Address does not match with SA：报文地址与SA中的地址不匹配

·Anti-replay sequence number reached the max：抗重放序号达到最大值

·The encapsulation mode does not match：封装类型不匹配

·Receive a ESP dummy packet：收到ESP保活报文

·Memory alloc failed：内存分配失败

·Packet length wrong：长度长度错误

·Replayed packet：重放报文

·Authentication failed：认证失败

·Security protocol set of SA does not match：SA的安全协议组合与对端不匹配

Inbound IPsec AH processing: Authentication succeeded.

入方向IPsec AH处理：认证成功

Outbound IPsec AH processing: Authentication finished, anti-replay SN is *sn* .

出方向IPsec AH处理：认证完成，抗重放序号为*sn*

Inbound IPsec ESP processing: Decryption succeeded.

入方向IPsec ESP处理：解密成功

Outbound IPsec ESP processing: Encryption succeeded, anti-replay SN is *sn*.

出方向IPsec ESP处理：加密成功，抗重放序号为*sn*

Outbound IPsec processing: Sent packet back to IP forwarding.

出方向IPsec处理：将报文重新发送给IP转发

Inbound IPsec processing: Sent packet back to IP forwarding.

入方向IPsec处理：将报文重新发送给IP转发

Outbound IPsec processing: Sent packet back to IP forwarding for following process.

出方向IPsec处理：将报文返回转发继续处理后续业务

IPsec processing: Tunnel mode

采用隧道模式

IPsec processing: Transport mode

采用传输模式

【举例】

\# 设备上已存在满配的SP，配置手工方式的IPsec安全策略mypolicy，并打开IPsec错误调试信息开关。当将策略mypolicy应用于接口GigabitEthernet1/0/1上的时候，输出如下IPsec错误调试信息。

\<Sysname\> debugging ipsec error

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipsec policy mypolicy

\*Jul 14 16:45:16:157 2012 Sysname IPSEC/7/ERROR: -MDC=1;

Failed to alloc SP index.

*// 分配SP索引失败*

\# 在设备上配置手工方式的IPsec安全策略mypolicy，并打开IPsec事件调试开关。当将策略mypolicy应用于接口GigabitEthernet1/0/1上时，会生成SP和SA，输出如下IPsec事件调试信息。

\<Sysname\> debugging ipsec event

\*Jul 18 15:28:55:020 2012 Sysname IPSEC/7/event:

SP entry successfully added in kernel.

*// 内核成功添加SP entry*

\*Jul 18 15:28:55:020 2012 Sysname IPSEC/7/ERROR:

Sent add SP entry message to kernel.

*// 向内核发送添加SP entry的消息*

\*Jul 18 15:28:55:020 2012 Sysname IPSEC/7/ERROR:

Added SP entry.

*// 添加SP entry*

\*Jul 18 15:28:55:022 2012 Sysname IPSEC/7/event:

SP successfully added in kernel.

*// 内核成功添加SP*

\*Jul 18 15:28:55:022 2012 Sysname IPSEC/7/ERROR:

Sent add SP message to kernel.

*// 向内核发送添加SP的消息*

\*Jul 18 15:28:55:023 2012 Sysname IPSEC/7/ERROR:

Added SP by policy.

*// 根据策略添加SP*

\*Jul 18 15:28:55:024 2012 Sysname IPSEC/7/ERROR:

Added policy SA by manual SP, SP index is 0, SP sequence number is 2.

*// 成功根据手工SP添加策略SA，SP索引为0，SP序号为2*

\*Jul 18 15:28:55:026 2012 Sysname IPSEC/7/event:

IPsec tunnel added to aggregation-hash.

*// 向聚合哈希表中添加IPsec隧道成功*

\*Jul 18 15:28:55:026 2012 Sysname IPSEC/7/event:

IPsec tunnel successfully added in kernel.

*// 内核添加IPsec隧道成功*

\*Jul 18 15:28:55:026 2012 Sysname IPSEC/7/ERROR:

Added tunnel to kernel successfully.

*// 向内核添加IPsec隧道成功*

\*Jul 18 15:28:55:026 2012 HP IPSEC/7/ERROR:

Added an IPsec tunnel when adding manual SA: tunnel index = 0, tunnel sequence number = 2.

*// 添加手工SA过程中添加IPsec隧道，隧道索引为0，隧道序号为2*

\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:

SA succussfully added in kernel.

*// 内核成功添加SA*

\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:

SA succussfully added in kernel.

*// 内核成功添加SA*

\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:

Added outbound SA to IPsec tunnel(SA ID = 1).

*// 成功向IPsec隧道添加出方向SA（SA索引为1）*

\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:

SA succussfully added in kernel.

*// 内核成功添加SA*

\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:

SA succussfully added in kernel.

*// 内核成功添加SA*

\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/ERROR:

Added SA to kernel successfully.

*// 成功向内核添加SA*

\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/ERROR:

Added manual SAs. Number of SAs added is 4.

*// 成功添加手工SA，SA的个数为4*

\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/ERROR:

No.1 SA: index = 3, sequence number = 2.

\*Jul 18 15:28:55:028 2012 Sysname IPSEC/7/ERROR:

No.2 SA: index = 2, sequence number = 2.

\*Jul 18 15:28:55:028 2012 Sysname IPSEC/7/ERROR:

No.3 SA: index = 1, sequence number = 2.

\*Jul 18 15:28:55:028 2012 Sysname IPSEC/7/ERROR:

No.4 SA: index = 0, sequence number = 2.

*// 第一个SA的索引为3，SA的序号为2*

*// 第二个SA的索引为2，SA的序号为2*

*// 第三个SA的索引为1，SA的序号为2*

*// 第四个SA的索引为0，SA的序号为2*

\*Jul 18 15:28:55:029 2012 Sysname IPSEC/7/ERROR:

Added SA context to SP.

*// 成功向SP添加SA上下文*

\# 在设备上配置手工方式的IPsec安全策略，应用于接口GigabitEthernet1/0/1上，并打开IPsec的报文调试信息开关。当从本机ping对端的时候，输出如下IPsec报文调试信息。

\<Sysname\> debugging ipsec packet

\<Sysname\> ping -c 1 10.10.10.2

PING 10.10.10.2 (10.10.10.2): 56 data bytes, press CTRL_C to break

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

\-\-- Sent IPsec packet \-\--

*// 出方向发送IPsec处理的报文*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Added IP fast forwarding entry.

*// 添加快转表项*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Outbound IPsec processing: Src : 10.10.10.1 Dst : 10.10.10.2 SPI : 1114

*// 出方向IPsec处理：源地址：10.10.10.1，目的地址：10.10.10.2，SPI: 1114*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Outbound IPsec processing: ESP auth algorithm: SHA1, ESP encp algorithm: DES-CBC.

*// 出方向IPsec处理：ESP认证算法为SHA1，ESP加密算法为DES-CBC*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Packet will be sent to CCF for sync-encryption.

*// 报文将被发送到CCF执行同步加密操作*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Outbound IPsec ESP processing: Encryption succeeded, anti-replay SN is 0.

*// 出方向IPsec ESP处理：加密完成，抗重放序号为0*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Outbound IPsec processing: AH auth algorithm: MD5.

*// 出方向IPsec处理：AH认证算法为MD5*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Packet will be sent to CCF for sync-encryption.

*// 报文将被发送到CCF执行同步加密操作*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Outbound IPsec AH processing: Authentication finished, anti-replay SN is 0.

*// 出方向IPsec AH处理：认证完成，抗重放序号为0*

\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;

Outbound IPsec processing: Sent packet back to IP forwarding.

*// 出方向IPsec处理：将报文重新发送给IP转发*

**

\

**IKE \-- IKE调试命令 \-- debugging ike**

------------------------------------------------------------------------

【命令】

**[debugging ike **[{ **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging ike **[{ **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

vd-admin

【参数】

**[all**]：表示所有IKE调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging ike **]命令用来打开IKE调试开关。**undo debugging ike**命令用来关闭IKE调试信息开关。

缺省情况下，IKE调试信息开关处于关闭状态。

表2-1 debugging ike error命令输出信息描述表

字段

描述

Failed to verify the peer signature.

对端签名验证失败

HASH payload is missing.

未在IKE报文中找到HASH载荷

Failed to verify the peer HASH.

对端HASH验证失败

Signature payload is missing.

未在IKE报文中找到签名载荷

Invalid SPI length (*length*) in DPD packet.

DPD报文中的SPI长度无效，长度为*length*

Invalid I-Cookie in DPD packet: *I-Cookie*

DPD报文中的I-Cookie无效，I-Cookie的值为*I-Cookie*

Invalid R-Cookie in DPD packet: *R-Cookie*

DPD报文：R-Cookie无效，R-Cookie的值为*R-Cookie*

The length (*length*) of DPD sequence number is invalid.

DPD序列号的长度无效，长度为*length*

Invalid DPD sequence number (*number*).

DPD序列号无效，序列号的值为*number*

DPD packet retransmission timed out.

DPD报文的重传已超时

Invalid IPv4 address length (*length*).

无效的IPv4地址长度，长度为*length*

Invalid IPv6 address length (*length*).

无效的IPv6地址长度，长度为*length*

Invalid ID of IPv4 address type: *ID-IPv4*

IPv4地址类型的身份无效，身份的值为*ID-IPv4*

Invalid ID of IPv6 address type: *ID-IPv6*

IPv6地址类型的身份无效，身份的值为*ID-IPv6*

Invalid FQDN ID length (*length*).

FQDN类型的身份长度无效，长度为*length*

Invalid user FQDN ID length (*length*).

User FQDN类型的长度身份无效，长度为*length*

Failed to get DN because the certificate doesn\'t exist.

获取DN失败，因为证书不存在

Failed to get ID data for constructing ID payload.

构造ID载荷时获取ID数据失败

Invalid ID payload with protocol *protocol-number* and port *port-number*.

无效的ID载荷，ID载荷中的协议号为*protocol-number*，端口号为*port-number*

Invalid ID type (*ID-type*).

身份类型无效，身份类型值为*ID-type*

Failed to find proposal *proposal-number* in profile *profile-name*.

在名称为*profile-name*的IKE profile中没有找到编号为*proposal-number*的proposal

Failed to verify HASH for informational exchange.

验证informational exchange报文中的HASH失败

Failed to construct delete payload.

构造delete载荷失败

Invalid SPI length.

SPI长度无效

Protocol ID (*ID*) in delete payload is invalid.

delete载荷中的协议ID无效，协议号为*ID*

KE payload doesn't exist.

KE载荷不存在

Invalid KE payload length (*length*).

KE载荷的长度无效，长度为*length*

Failed to construct notification payload for keepalive.

发送keepalive报文时构造notification载荷失败

Length (*length*) of the sequence number in keepalive packet is invalid.

Keepalive报文中的序列号长度无效，长度为*length*

Length (*length*) of the HASH payload in keepalive packet is invalid.

Keepalive报文中的HASH载荷长度无效，长度为*length*

Failed to calculate HASH for verification of keepalive packet.

验证keepalive报文时，本端计算HASH失败

Failed to add sequence number to keepalive packet.

构造keepalive报文时，添加序列号失败

Failed to calculate HASH for keepalive.

构造keepalive报文时，计算HASH失败

Failed to float port.

切换端口失败

Length (*length*) of the nonce payload is invalid.

Nonce载荷的长度无效，长度为*length*

Failed to parse the certificate request payload.

解析证书请求载荷失败

No available proposal.

没有找到可用的proposal

Failed to get certificate.

获取证书失败

Failed to get private key.

获取私钥失败

Failed to construct ID payload.

构造IPsec身份载荷失败

Failed to calculate *hash-name*.

计算HASH失败，HASH名称为*hash-name*

Failed to validate *hash-name*.

验证HASH失败，HASH名称为*hash-name*

Failed to compute key material.

计算密钥材料失败

Failed to install IPsec SA.

安装IPsec SA失败

The nonce payload doesn\'t exist.

Nonce载荷不存在

The KE payload doesn\'t exist.

KE载荷不存在

No valid DH group description in SA payload.

SA载荷中没有有效的DH group

There are too many KE payloads.

KE载荷太多，

The length of the KE payload does\'t match the DH group description.

KE载荷的长度和用于PFS的DH group描述不匹配

Failed to construct NAT-OA payload.

构造NAT-OA载荷失败

Failed to construct RESPONDER_LIFETIME payload.

构造RESPONDER_LIFETIME载荷失败

Failed to construct KE payload.

构造KE载荷失败

Failed to pad for encryption.

加密报文前的填充失败

Failed to send data. Reason: *error-reason.*

发送报文失败，错误原因为*error-reason*

No enough space in the packet for Non-ESP marker.

报文超大，不能添加Non-ESP标记

Failed to decrypt the packet.

解密报文失败

Non-zero message ID (*Message-ID*) in phase 1.

一阶段的Message ID不为0，其值为*Message-ID*

I-Cookie must not be zero.

I-Cookie不能为0

The first packet of phase 1 is invalid: Encryption bit is set.

一阶段的第一条报文无效：报文的加密标识为已使能

The first packet of phase 1 is invalid: Non-zero R-Cookie.

一阶段的第一条报文无效：报文的R-Cookie不为0

Failed to parse phase 1 packet. Reason *reason*.

解析一阶段的IKE报文失败，原因为*reason*，可能的取值包括：

·INVALID_PAYLOAD_TYPE：载荷类型无效

·DOI_NOT_SUPPORTED：不支持的DOI字段

·SITUATION_NOT_SUPPORTED：不支持的situation字段

·INVALID_COOKIE：cookie无效

·INVALID_MAJOR_VERSION：主版本号无效

·INVALID_MINOR_VERSION：次版本号无效

·INVALID_EXCHANGE_TYPE：交换类型无效

·INVALID_FLAGS：标识无效

·INVALID_MESSAGE_ID：message ID无效

·INVALID_PROTOCOL_ID：提议号无效

·INVALID_SPI：SPI无效

·INVALID_TRANSFORM_ID：transform ID无效

·ATTRIBUTES_NOT_SUPPORTED：不支持的属性

·NO_PROPOSAL_CHOSEN：没有匹配的提议

·BAD_PROPOSAL_SYNTAX：提议语法错误

·PAYLOAD_MALFORMED：载荷格式错误

·INVALID_KEY_INFORMATION：密钥信息无效

·INVALID_ID_INFORMATION：身份无效

·INVALID_CERT_ENCODING：证书编码无效

·INVALID_CERTIFICATE：证书无效

·CERT_TYPE_UNSUPPORTED：不支持的证书类型

·INVALID_CERT_AUTHORITY：证书认证失败

·INVALID_HASH_INFORMATION：HASH无效

·AUTHENTICATION_FAILED：认证失败

·INVALID_SIGNATURE：签名无效

·ADDRESS_NOTIFICATION：地址通知

·NOTIFY_SA_LIFETIME：SA生命周期通知

·CERTIFICATE_UNAVAILABLE：证书不可用

·UNSUPPORTED_EXCHANGE_TYPE：不支持的交换类型

·UNEQUAL_PAYLOAD_LENGTHS：载荷长度不相等

The packet is dropped because of not being encrypted

丢弃报文，因为报文没有加密

Failed to parse informational exchange packet. Reason *reason*.

解析informational exchange报文失败，原因是*reason*

*[reason*]取值同上

Failed to parse keepalive packet because of *reason*.

解析keepalive报文失败，原因是*reason*

*[reason*]取值同上

Unsupported exchange type (*type*) in packet.

不支持的交换类型*type*，取值包括：

·None：不存在的交换类型

·Base：基础交换类型

·Main：主模式交换类型

·AO：Authenticaton Only交换类型

·Aggressive：野蛮模式交换类型

·Info：infomational exchange交换类型

·Mode cfg：配置模式交换类型

Invalid Non-ESP marker: *marker*.

无效的Non-ESP标识：*marker*

The received packet is too short, which is *length* bytes.

收到报文的长度太小，长度为*length*

Failed to receive packet.

接收报文失败

Failed to bind UDP port *port-number*. Reason: *reason*.

绑定UDP端口失败，端口号为*port-number*，错误原因为*reason*

Failed to set UDP port *port-number*. Reason: *reason*.

设置UDP端口失败，端口号为*port-number*，错误原因为*reason*

Failed to add UDP port *port-number* to epoll.

添加UDP端口到epoll失败，端口号为：*port-number*

Failed to initiate UDP port *port-number*. Error code: *error-number*.

初始化UDP端口失败，端口号为*port-number*，错误码为*error-number*

*[byte-number*th byte of the structure *struct-name* must be 0.]

结构*struct-name*的第*byte-number*个字节必须为0

*[Field-name* of *struct-name* has an unknown value: *value*.]

结构*struct-name*的域*field-name*的值*value*无效

*[field-name* of *struct-name* has unknown members.]

结构*struct-name*的域*field-name*包含未知的成员

No enough bytes to get *data2* from *data1*.

没有足够的空间来保存从数据*data1*中获取的数据*data2*

No enough space in output packet for *struct-name*.

报文中没有足够的空间用于保存结构*struct-name*

No enough space to place *length* bytes of *data-name* in *struct-name*.

结构*struct-name*中没有足够的空间用于保存*length*字节的数据

No enough space to place *data-name* in *struct-name.*

结构*struct-name*中没有足够的空间保存数据*data-name*

Failed to add the HASH payload.

添加HASH载荷失败

Ignored the certificate request of type *type-id*.

忽略证书请求，证书请求的类型为*type-id*

Failed to get the certificate and key by certificate request.

根据证书请求获取证书和密钥失败

Failed to verify the peer certificate. Reason: *error-string*.

验证对端证书失败，错误原因为*error-string*

Failed to find keychain *keychain-name* in profile *profile-name*.

在IKE profile *profile-name*中查找keychain *keychain-name*失败

Failed to create IKE SA with core data.

根据核心数据创建一阶段SA失败

Failed to create IPsec SA with core data.

根据核心数据创建二阶段SA失败

Failed to receive smooth SA ACK from IPsec.

从IPsec接收SA平滑处理的应答失败

Number of negotiating IKE SAs exceeded the limit.

正在协商的IKE SA的数目超出限制

Number of established IKE SAs exceeded the limit.

已经建立的IKE SA的数目超出限制

Attribute *attribute-name* is repeated.

属性重复，属性名称为*attribute-name*

Failed to construct situation.

构造situaton字段失败

Failed to construct proposal payload.

构造proposal载荷失败

Failed to construct transform payload.

构造transform载荷失败

Failed to construct attributes.

构造属性失败

Unsupported DOI *doi*

不支持的DOI *doi*

Proposal payload must be the last payload in SA payload, but *payload-name* payload is found following proposal payload.

proposal载荷必须是SA载荷中的最后一个载荷，但在proposal载荷之后还有*payload-name*载荷

Unexpected protocol ID (*ID-type*) found in proposal payload.

proposal载荷中的协议ID无效，协议ID号为*ID-type*

Invalid SPI length (*SPI-length*) in proposal payload.

proposal载荷中的SPI长度无效

No transform payload in proposal payload.

proposal载荷中没有transform载荷

Transform number is not monotonically increasing.

Transform号不是单调递增的

Invalid transform ID: *id*.

无效的transform ID：*id*

No acceptable transform.

没有可以接受的transform

Unexpected *payload-name* payload in proposal.

proposal载荷中有不期望出现的载荷*payload-name*

Only one transform is permitted in one proposal, but *trans-count* transforms are found.

在选中的proposal载荷中只允许有一个transform，但实际有*trans-count*个

Failed to parse the IKE SA payload.

解析IKE SA载荷失败

Proposal payload has more transforms than specified in the proposal payload.

proposal载荷中的transform载荷数量比proposal载荷中指定的数量多

Proposal payload has fewer transforms than specified in the proposal payload.

proposal载荷中的transform载荷数量比proposal载荷中指定的数量少

Invalid next payload (*payload-type*) in transform payload.

transform载荷中的next payload字段无效，载荷类型为*payload-type*

SA_LIFE_TYPE attribute must be in front of the SA_LIFE_DURATION attribute.

SA_LIFE_TYPE属性必须在SA_LIFE_DURATION属性前面

Attribute *attribute-type* is repeated in IPsec transform *trans-number*.

属性类型为的*attribute-type*属性在IPsec transform中重复，transform号为*trans-number*

SA_LIFE_TYPE attribute is repeated in packet.

属性SA_LIFE_TYPE在报文中重复

Unsupported IPsec attribute *attribute*.

不支持的IPsec属性*attribute*

SA_LIFE_TYPE IPsec attribute not followed by SA_LIFE_DURATION attribute in message.

报文中的IPsec属性SA_LIFE_TYPE后面没有SA_LIFE_DURATION属性

Encapsulation mode must be specified in IPsec transform.

IPsec transform中必须指定封装模式

AUTH_ALGORITHM attribute is missing in AH transform.

在AH协议的transform中没有AUTH_ALGORITHM属性

Transform ID (*id*) in transform *trans-number* doesn\'t match authentication algorithm *auth-algo-name* (*auth-algo-value*).

transform中的transform ID和认证算法不匹配，transform号为*trans-number*，transform ID为*id*，认证算法为*auth-algo-name*，其值为*auth-algo-value*

Neither encryption algorithm nor authentication algorithm is specified in ESP proposal, which is not permitted.

ESP proposal中既没有加密算法也没有认证算法，这是不允许的

Unsupported ESP transform.

不支持的ESP transform

Unsupported ESP authentication algorithm.

不支持的ESP认证算法

IPsec proposal with improper SPI size (*size*).

IPsec proposal中的SPI大小错误，SPI大小为*size*

IPsec proposal contains invalid SPI (*SPI*).

IPsec proposal中的SPI无效，其值为*SPI*

Failed to get SPI from IPsec proposal.

从IPsec proposal中获取SPI失败

No transform in IPsec proposal.

IPsec proposal中没有transform

SA payload contains more than one AH proposal with the same proposal number.

SA载荷中有多个AH协议的proposal对应同一个proposal号

SA payload contains more than one ESP proposal with the same proposal number.

SA载荷中有多个ESP协议的proposal对应同一个proposal号

Invalid next payload (*payload-type-num*) in proposal.

Proposal载荷中的next payload字段无效，其类型值为*payload-type-num*

Unsupported IPsec DOI situation (*situation-num*).

不支持的IPsec DOI situation，其类型值为*situation-num*

Invalid IPsec proposal *proposal-number*.

无效的IPsec proposal，proposal号为*proposal-number*

Failed to get IPsec policy when renegotiating IPsec SA. Delete IPsec SA.

在重协商IPsec SA时获取IPsec策略失败，删除 IPsec SA

Failed to get IPsec policy for phase 2 responder. Delete IPsec SA.

作为二阶段协商的响应方时，获取IPsec策略失败，删除IPsec SA

No HASH in notification payload.

在notification载荷中没有HASH

Failed to send message to IPsec when getting SPI.

获取SPI时向IPsec发消息失败

Failed to send message to IPsec when adding SA.

添加SA时向IPsec发消息失败

Failed to send message to IPsec when deleting SA.

删除SA时向IPsec发消息失败

Failed to send message to IPsec when getting SP.

获取SP时向IPsec发消息失败

Failed to send message to IPsec when adding DPD.

添加DPD时向IPsec发消息失败

Failed to send message to IPsec when updating DPD.

升级DPD时向IPsec发消息失败

Failed to send message to IPsec when deleting DPD.

删除DPD时向IPsec发消息失败

Failed to send message to IPsec when switching SA.

切换SA时向IPsec发消息失败

Failed to negotiate IKE SA.

协商IKE SA失败

Failed to negotiate IPsec SA.

协商IPsec SA失败

*[Errstring*. Attribute *attribute-name*.]

错误原因为*errstring*。相关的属性名称为*attribute-name*

*[Errstring*]的内容包括：

·Unsupported encryption algorithm: enc-alg：不支持的加密算法enc-alg

·Unsupported HASH algorithm: hash-alg：不支持的HASH算法hash-alg

·Unsupported authentication method: auth-meth：不支持的认证方法auth-meth

·Unsupported DH group: group-name：不支持的DH group group-name

·Unsupported lifetime type: lifetime-type：不支持的生命周期类型lifetime-type

·OAKLEY_LIFE_DURATION attribute not preceded by OAKLEY_LIFE_TYPE attribute.：OAKLEY_LIFE_DURATION属性没有在OAKLEY_LIFE_TYPE属性之前

·OAKLEY_KEY_LENGTH attribute not preceded by OAKLEY_ENCRYPTION_ALGORITHM attribute：OAKLEY_KEY_LENGTH属性没有在OAKLEY_ENCRYPTION_ALGORITHM属性之前

·OAKLEY_KEY_LENGTH attribute not match OAKLEY_ENCRYPTION_ALGORITHM.：OAKLEY_KEY_LENGTH属性和OAKLEY_ENCRYPTION_ALGORITHM属性不匹配

·Failed to get encryption algorithm：获取加密算法失败

·Unsupported OAKLEY attribute attribute：不支持的OAKLEY属性attribute

Failed to match the proposal.

匹配proposal失败

Received invalid SPI message from IPsec, but no IKE SA exists.

收到IPsec的invalid SPI消息，但是没有IKE SA

Failed to get subject name from certificate.

从证书中获取主题名失败

Failed to get local certificate.

获取本地证书失败

Failed to send notification packet for deleting IPsec SA, because of no corresponding IKE SA.

删除IPsec SA时发送notification报文失败，因为没有找到对应的IKE SA

Failed to construct certificate request payload.

构造证书请求载荷失败

Unsupported attribute *attribute-type*.

不支持的属性，属性类型为*attribute-type*

Invalid major version(*version*).

主版本号无效，主版本号为*version*

表2-2 debugging ike event命令输出信息描述表

字段

描述

Signature verification succeeded.

验证签名成功

HASH verification succeeded.

验证HASH成功

Delete IPsec SAs.

删除IPsecSA

Delete IKE SA with connection ID *id*.

删除IKE SA，connection ID为*id*

Update DPD configuration in IKE SA.

更新一阶段SA中的DPD配置

Notify IPsec to add DPD.

通知IPsec添加DPD

Notify IPsec to delete DPD.

通知IPsec删除DPD

Notify IPsec to update DPD.

通知IPsec更新DPD

Process interface *interface-type interface-num* active event.

处理接口激活事件，接口名为*interface-type interface-num*

Process interface *interface-name* deactive event.

处理接口去激活事件，接口名为*interface-type interface-num*

Process interface *interface-name* delete event.

处理接口删除事件，接口名为*interface-type interface-num*

The board chassis *chassis-num* slot *slot-num* is inserted.

单板插入*chassic-number*号成员设备的*slot-number*号槽位中

Protocol/port in phase 1 ID payload is *protocol-number*/*port-number*, which is acceptable.

一阶段ID载荷中的协议号/端口号为*protocol-number*/*port-number*，它们是可接受的

Begin to construct IPsec SA delete packet.

开始构造二阶段SA delete报文

Delete IKE SA with connection ID *id*.

删除一阶段SA，connection ID为*id*

Received IPsec SA delete packet.

收到二阶段SA delete报文

Process delete payload.

处理delete载荷

Ignore delete payload: packet not encrypted or IKE SA not established.

忽略delete载荷：报文没有加密或者一阶段SA没有建立

Received SA acquire message from IPsec.

收到IPsec的SA请求消息

Received IPsec capability.

收到IPsec规格

Received smooth IPsec SA ACK.

收到平滑IPsec SA的应答

IKE keepalive timed out. Delete IKE SA with connection ID *id*.

IKE Keepalive定时器超时，删除一阶段SA，connection ID为*id*

Reset IKE keepalive timeout timer. New time value is *time*

重置IKE Keepalive超时定时器，新的时间值为*time*

I am behind NAT.

我在NAT设备之后

Peer is behind NAT.

对端在NAT设备之后

No need to float port.

不需要切换端口

Float port to local port *local-port* and remote port *remote-port*

切换端口，本端端口为*local-port*，对端端口为*remote-port*

Sending DPD packet of type *type* with sequence number *seq-no*.

发送*type*类型的DPD报文，序列号为*seq-no*

Delete IKE SA by received notification.

根据错误通知报文删除一阶段SA

INITIAL-CONTACT message is dropped because of not being encrypted.

INITIAL-CONTACT未加密，丢弃它

Delete redundant SA.

删除多余的SA

Length (*length*) of notification packet is invalid.

notification报文的长度无效，长度为*length*

Protocol-ID (*ID*) of notification packet is unsupported.

不支持notification报文中的协议号：*ID*

Notification *notification-name* is received.

收到通知报文*notification-name*

Inbound flow: *dst-addr-\>src-addr*

入方向流量：目的地址-\>源地址

Outbound flow: *src-addr-\>dst-addr*

出方向流量：源地址-\>目的地址

Validated *hash-name* successfully.

验证HASH成功，HASH名称为*hash-name*

Getting IPsec message timed out. Delete IPsec SA.

获取IPsec消息超时，删除二阶段SA

Protocol: *protocol*

安全协议为*protocol*（AH或ESP）

Inbound SPI: *in-spi*

入方向SPI值为*in-spi*

Outbound SPI: *out-spi*

出方向SPI值为*out-spi*

Install IPsec SAs.

下发IPsec SA

Lifetime in seconds: *seconds*

SA的生命周期为*seconds*秒

Lifetime in kilobytes: *bytes*

SA的生命周期为*bytes*字节

Phase 2 Exchange chooses role: Local is initiator.

二阶段协商选择角色：本端为发起方

Phase 2 Exchange chooses role: Local is responder.

二阶段协商选择角色：本端为响应方

Begin Quick mode exchange.

开始进行快速模式协商过程

No enough space to send packet.

没有足够的空间来发送报文

Retransmittion of phase 1 packet timed out.

重传一阶段报文超时

Ignore phase 1 packet retransmit timeout event.

忽略一阶段报文重传超时事件

Retransmittion of  phase 2 packet timed out.

重传二阶段报文超时

Ignore phase 2 packet retransmit timeout event.

忽略二阶段报文重传超时事件

Phase 1 Exchange chooses role: Local is initiator.

一阶段协商选择角色：本端为发起方

Phase 1 Exchange chooses role: Local is responder.

一阶段协商选择角色：本端为响应方

Phase 1 packet is malformed: Not starting with an SA payload.

一阶段报文格式错误：没有以SA载荷开始

Phase2 packet is malformed: Not starting with an HASH payload.

二阶段报文格式错误：没有以HASH载荷开始

Quick mode packet is received, but IKE SA does not exist.

收到快速模式的报文，但一阶段SA不存在

Quick mode packet is received, but IKE SA is incomplete.

收到快速模式的报文，但一阶段SA不完整

Ignored delete SA payload because the IKE SA is not established.

忽略删除SA的报文，因为IKE SA不存在

Ignored delete SA payload because the packet is not encrypted.

忽略删除SA的报文，因为报文没有加密

Received informational exchange packet, but IKE SA is inexistent or incomplete.

收到information exchange报文，但是一阶段SA不存在或者不完整

Received keepalive packet, but IKE SA is not existed.

收到IKE keepaclive报文，但是一阶段SA不存在

Received keepalive packet, but it is not encrypted.

收到IKE keepaclive报文，但是它没有加密

Received keepalive packet, but IKE SA is incomplete.

收到IKE keepaclive报文，但是一阶段SA不完整

Ignore NAT keepalive packet.

忽略NAT keepalive报文

Initialize UDP port.

初始化UDP端口

PKI data had been changed.

PKI数据已经有所变化

Found pre-shared key that matches address *address* in keychain *keychain-name*.

在keychain *keychain-name*中找到了预共享密钥，该预共享密钥与地址*address*匹配

Pre-shared key matching address *address* not found.

根据地址*address*无法找到匹配的预共享密钥

Found keychain *keychain-name* in profile *profile-name* successfully.

成功在IKE profile *profile-name*中找到keychain *keychain-name*

Get profile *profile-name*.

获取IKE profile *profile-name*

Initiator created an SA for peer *address*, local port *local-port*, remote port *remote-port*.

发起方创建SA，对端地址为*address*，本端端口为*local-port*，对端端口为*remote-port*

Set IKE SA state to *state-name*.

设置一阶段SA状态为*state-name*

IKE SA state changed from *state1* to *state2*.

一阶段SA状态从*state1*转换到*state2*

Set IPsec SA state to *state-name*.

设置二阶段SA状态为*state-name*

IPsec SA state changed from *state1* to *state2*.

二阶段SA状态从*state1*转换到*state2*

Responder created an SA for peer *address*, local port *local-port*, remote port *remote-port*.

发起方创建SA，对端地址为*address*，本端端口为*local-port*，对端端口为*remote-port*

Delete IPsec SA.

删除二阶段SA

Oakley transform *trans-number* is acceptable.

Oakley transform是可接受的，transform号为*trans-number*

Begin *mode* mode exchange.

开始*mode*模式的IKE协商

IKE SA not found. Initiate IKE SA negotiation.

没有一阶段SA，发起一阶段SA的协商

IKE SA is prepared for renegotiation.

一阶段SA已经准备好进行重协商

IKE SA is expired.

一阶段SA生命周期到达

Renegotiation has already started for this IKE SA.

该IKE SA的重协商已经开始

IKE SA with connection ID *connection-id* has expired, and it will be deleted.

一阶段SA生命周期到达，将其删除，connection ID为*connection-id*

IPsec SA is being negotiated.

二阶段SA正在协商

IPsec SA has expired and will be deleted.

生命周期到达，删除二阶段SA

IKE thread *thread-id* processes a job.

IKE线程*thread-id*处理一个job

IKE thread *thread-id* processes a CTL-Queue msg.

IKE线程*thread-id*处理一个控制队列消息

Vendor ID *verdor-id* is matched.

匹配上vendor ID *verdor-id*

No vendor ID is matched.

没有匹配的verdor ID

表2-3 debugging pki packet命令输出信息描述表

字段

描述

Construct authentication data by pre-shared key.

根据预共享密钥生成认证数据

Verify HASH{.MsoCommentReference} payload.

验证HASH载荷

Construct authentication data by private key.

根据私钥生成认证数据

Verify signature payload.

验证签名载荷

DPD packet with sequence number *sequence-number* is received.

收到DPD报文，序列号为：*sequence-number*

Retransmit DPD packet.

重传DPD报文

Peer ID value: address *address*.

对端ID值：地址*address*

Peer ID value: FQDN *fqdn*.

对端ID值：FQDN *fqdn*

Peer ID value: User FQDN *user-fqdn*.

对端ID值：User FQDN *user-fqdn*

Peer ID value: DN *DN-value*

对端ID值：DN，DN的内容为*DN-value*

Peer ID type: *ID-type* (*value*).

对端ID类型：*ID-type*，类型的值为*value*

Local ID type: *ID-type* (*value*).

本端ID类型：*ID-type*，类型的值为*value*

Local ID value: *ID-value*.

本端ID值：*ID-value*

Construct ID payload.

构造ID载荷

The profile *profile-name* is matched.

匹配到profile为*profile-name*

No profile is matched.

没有匹配到profile

Process ID payload.

处理ID载荷

Construct notification packet: *notification-type*.

构造notification报文：*notification-type*

Construct delete payload.

构造delete载荷

The phase 1 delete packet is received.

收到一阶段delete报文

The cookies\' length (*length*) is invalid.

Cookies的长度*length*无效

Construct KE payload.

构造KE载荷

Process KE payload.

处理KE载荷

Send keepalive packet with sequence number *sequence-number*.

发送IKE keepalive报文，序列号为*sequence-number*

Process keepalive packet with sequence number *sequence-number*.

处理IKE keepalive报文，序列号为*sequence-number*

Construct NAT-D payload.

构造NAT-D载荷

Received *count* NAT-D payloads.

收到NAT-D载荷，数量为*count*

Construct NONCE payload.

构造NONCE载荷

Process NONCE payload.

处理NONCE载荷

Construct INITIAL-CONTACT payload.

构造INITIAL-CONTACT载荷

Construct SA payload.

构造SA载荷

Construct IPsec ID payload.

构造IPsec ID载荷

Process HASH payload.

处理HASH载荷

Construct IPsec SA payload.

构造IPsec SA载荷

Construct HASH(3) payload.

构造HASH(3)载荷

Process IPsec ID payload.

处理IPsec ID载荷

Construct NAT-OA payload.

构造NAT-OA载荷

Process NAT-OA payload: *address*.

处理NAT-OA载荷，地址为*address*

Received *count* NAT-OA payloads.

收到NAT-OA载荷，数量为*count*

Construct IPsec RESPONDER_LIFETIME payload.

构造IPsec RESPONDER_LIFETIME载荷

Construct HASH(1) payload.

构造HASH(1)载荷

Collision of phase 2 negotiation is found.

二阶段协商发生碰撞

Construct HASH(2) payload.

构造HASH(2)载荷

I-Cookie: *icookie*

R-Cookie: *rcookie*

next payload: *next-payload*

version: *version*

exchange mode: *mode*

flags: *flag*

message ID: *mid*

length: *length*

·发起方cookie：icookie

·响应方cookie：rcookie

·下一个载荷：next-payload

·ISAKMP版本：version

·协商模式：mode

·标识为：flag

·Message ID：mid

·报文长度：length

Encrypt the packet.

对报文进行加密

Received *payload-name*.

收到载荷*payload-name*

Sending packet to *address*, remote port *remote-port*, local port *local-port*.

发送报文到地址*address*，对端端口号为*remote-port*，本端端口号为*local-port*

Sending an IPv4 packet.

发送一个IPv4报文

Sending an IPv6 packet.

发送一个IPv6报文

Retransmit phase 1 packet.

重传一阶段报文

Retransmit phase 2 packet.

重传二阶段报文

Retransmit in response to duplicate packet.

针对对端重发的报文，重传对应的响应报文

Discard duplicate packet because of exhausted retransmission.

本端重传次数已达到最大，不再响应该重复的报文，将其丢弃

Discard duplicate packet with no response.

丢弃对端重复发送的报文，不进行响应

Collision of phase 1 negotiation is found.

一阶段协商发生碰撞

Decrypt the packet.

对报文进行解密

Begin a new phase 1 negotiation as responder.

做为响应方，开始加入一个新的一阶段协商过程

Parse informational exchange packet successfully.

成功解析informational exchange报文

Received packet from *address* source port *source-port* destination port *des-port*.

收到的来自*address*的报文，源端口为*source-port*，目的端口为*des-port*

Skipping *length* raw bytes of *name1* to get *name2*.

跳过载荷name1的*length*字节，去获取下一个载荷*name2*

Add certificate request payload *subjectname*.

添加证书请求载荷，主题名为*subjectname*

Construct certificate request payload.

构造证书请求载荷

Received certificate request payload that contains issuer name *issuer-name*.

收到证书请求载荷，签发者名为*issuer-name*

Process certificate request payload.

处理证书请求载荷

The certificate request payload is empty.

证书请求载荷是空的

Construct certificate payload.

构造证书载荷

The profile *profile-name is matched* by remote certificate.

通过对端证书匹配到一个IKE profile *profile-name*

Process certificate payload.

处理证书载荷

Encryption algorithm is *enc-algo*.

加密算法为*enc-algo*

HASH algorithm is *hash-algo*.

HASH算法为*hash-algo*

Authentication method is *auth-method*.

认证方法为*auth-method*

DH group is *group*.

DH group为*group*

Lifetime type is *type*.

生命周期类型为*type*，*type*值为：

·in seconds：时间生命周期

·in kilobytes：字节生命周期

Life duration is *value*.

生命周期为*value*

Key length is *length* bytes.

密钥长度为*length*字节

Check ISAKMP transform *trans-number*.

检查ISAKMP transform，transform号为*trans-number*

Attributes is acceptable.

属性是可接受的

Construct transfrom payload for transform *trans-number*.

构造transform载荷，transform号为*trans-number*

Encapsulation mode is *mode*.

封装模式为*mode*，*mode*取值包括：

·Tunnel：隧道模式

·Transport：传输模式

·Tunnel-UDP：UDP封装的隧道模式

·Transport-UDP：UDP封装的传输模式

Set attributes according to phase 2 transform.

根据二阶段transform设置属性

Transform ID is *id*.

Transform ID为*id*

Construct transform 1.

构造transform 1

Construct IPsec proposal *proposal-number*.

构造IPsec proposal，proposal号为*proposal-number*

Parse transform *trans-number*.

解析transform，transform号为*trans-number*

The SA_LIFE_TYPE attribute is repeated in packet.

SA_LIFE_TYPE属性在报文中重复

Number of key rounds is *round*.

密钥轮数为*round*

Process IPsec SA payload.

处理IPsec SA载荷

The attributes are unacceptable.

属性不可接受

Construct *vid-name* vendor ID payload.

构造vendor id载荷，vendor ID名称为*vid-name*

Process vendor ID payload.

处理vendor ID载荷

HASH:*value*

HASH为*value*

SKEYID:*value*

SKEYID为*value*

Extended Skeyid_e:*value*

扩展的Skeyid_e为*value*

Local generated new IV: *value*

本地新生成的IV为*value*

SKEYID_a: *value*

SKEYID_a为*value*

SKEYID_d: *value*

SKEYID_d为*value*

SKEYID_e: *value*

SKEYID_e为*value*

Encrypt IV: *value*

加密IV为*value*

Encryption generated new IV: *value*

加密新生成的IV为*value*

Decrypt IV: *value*

解密IV为*value*

Remote new IV: *value*

对端新IV为*value*

The proposal is acceptable.

提议是可以接受的

The proposal is unacceptable.

提议是不能接受的

【举例】

\#在两个安全网关上配置了IKE协商类型的IPsec策略，在一阶段IKE协商过程中，若未找到匹配的IKE proposal，则打开IKE错误调试信息开关后将输出以下调试信息。

\<Sysname\> debugging ike error

\*Aug 20 19:19:44:543 2012 Sysname IKE/7/ERROR: -MDC=1; No acceptable transform.

*// 没有可以接受的transform*

\*Aug 20 19:19:44:543 2012 Sysname IKE/7/ERROR: -MDC=1; Failed to parse the IKE SA payload.

*// 解析SA载荷失败*

\#在两个安全网关上配置了IKE协商类型的IPsec策略，若配置一阶段协商模式为主模式，认证方法为预共享密钥认证，则当有流量触发协商时，打开IKE事件调试信息开关后将输出以下调试信息。

\<Sysname\> debugging ike event

\<Sysname\> ping -c 1 192.168.222.5

PING 192.168.222.5 (192.168.222.5): 56 data bytes, press CTRL_C to break

\*Aug 20 19:10:37:509 2012 Sysname IKE/7/EVENT: -MDC=1; Received SA acquire message from IPsec.

*// 收到IPsec的SA请求消息*

\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Set IPsec SA state to IKE_P2_STA

TE_INIT.

*// 设置二阶段SA状态为IKE_P2_STATE_INIT*

\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; No IKE SA found, initiate IKE SA negotiation.

*// 没有一阶段SA，发起一阶段SA的协商*

\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Get profile profile1.

*// 获取profile profile1*

\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Initiator create a SA for peer 192.168.222.5, local port 500, remote port 500.

*// 发起方创建SA，对端地址为192.168.222.5，本端端口为500，对端端口为500*

\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Set IKE SA state to IKE_P1_STATE_INIT.

*// 设置一阶段SA状态为IKE_P1_STATE_INIT*

\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3083549648 processes a job.

*[// IKE*]*线程3083549648处理一个job*

\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Begin Main mode exchange.

*// 开始主模式协商*

\*Aug 20 19:10:37:511 2012 Sysname IKE/7/EVENT: -MDC=1; Found pre-shared key that matches address 192.168.222.5 in keychain keychain1.

*// 在keychain keychain1中找到了预共享密钥，预共享密钥匹配地址192.168.222.5*

\*Aug 20 19:10:37:511 2012 Sysname IKE/7/EVENT: -MDC=1; IKE SA state changed from IKE_P1_STATE_INIT to IKE_P1_STATE_SEND1.

*// 一阶段SA状态从IKE_P1_STATE_INIT到IKE_P1_STATE_SEND1*

\*Aug 20 19:10:37:520 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3008052176 processes a job.

*[// IKE*]*线程3008052176处理一个job*

\*Aug 20 19:10:37:520 2012 Sysname IKE/7/EVENT: -MDC=1; Oakley transform 1 is acceptable.

*[// Oakley transform*]*是可接受的，transform号为1*

\*Aug 20 19:10:37:520 2012 Sysname IKE/7/EVENT: -MDC=1; Match the vendor ID NAT-T rfc3947.

*// 匹配上vendor ID NAT-T rfc3947*

\*Aug 20 19:10:37:533 2012 Sysname IKE/7/EVENT: -MDC=1; IKE SA state changed from IKE_P1_STATE_SEND1 to IKE_P1_STATE_SEND3.

*// 一阶段SA状态从IKE_P1_STATE_SEND1到IKE_P1_STATE_SEND3*

\*Aug 20 19:10:37:533 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.

*[// IKE*]*线程3087980192处理一个控制队列消息*

\*Aug 20 19:10:37:566 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3083549648 processes a job.

*[// IKE*]*线程3083549648处理一个job*

\*Aug 20 19:10:37:580 2012 Sysname IKE/7/EVENT: -MDC=1; Match the vendor ID DPD.

*// 匹配上vendor ID DPD*

\*Aug 20 19:10:37:580 2012 Sysname IKE/7/EVENT: -MDC=1; IKE SA state changed from IKE_P1_STATE_SEND3 to IKE_P1_STATE_SEND5.

*// 一阶段SA状态从IKE_P1_STATE_SEND3到IKE_P1_STATE_SEND5*

\*Aug 20 19:10:37:580 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.

*[// IKE*]*线程3087980192处理一个控制队列消息*

\*Aug 20 19:10:37:584 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3075161040 processes a job.

*[// IKE*]*线程3075161040处理一个job*

\*Aug 20 19:10:37:584 2012 Sysname IKE/7/EVENT: -MDC=1; Verify HASH successfully.

*// 验证HASH成功*

\*Aug 20 19:10:37:585 2012 Sysname IKE/7/EVENT: -MDC=1; IKE SA state changed from IKE_P1_STATE_SEND5 to IKE_P1_STATE_ESTABLISHED.

*// 一阶段SA状态从IKE_P1_STATE_SEND5到IKE_P1_STATE_ESTABLISHED*

\*Aug 20 19:10:37:585 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3075161040 process

es a job.

*[// IKE*]*线程3075161040处理一个job*

\*Aug 20 19:10:37:585 2012 Sysname IKE/7/EVENT: -MDC=1; Begin Quick mode exchange.

*// 开始快速模式协商*

\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.

*[// IKE*]*线程3087980192处理一个控制队列消息*

\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IPsec SA state changed from IKE_P2_STATE_INIT to IKE_P2_STATE_GETSPI.

*// 二阶段SA状态从IKE_P2_STATE_INIT到IKE_P2_STATE_GETSPI*

\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.

*[// IKE*]*线程3087980192处理一个控制队列消息*

\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3066772432 processes a job.

*[// IKE*]*线程3066772432处理一个job*

\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IPsec SA state changed from IKE_P2_STATE_GETSPI to IKE_P2_STATE_SEND1.

*// 二阶段SA状态从IKE_P2_STATE_GETSPI到IKE_P2_STATE_SEND1*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.

*[// IKE*]*线程3087980192处理一个控制队列消息*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3033218000 processes a job.

*[// IKE*]*线程3033218000处理一个job*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; Validate HASH(2) successfully.

*// 验证HASH(2)成功*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; Install IPsec SAs.

*// 下发IPsecSA*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   inbound flow: 192.168.222.5/32-\>192.168.222.71/32

*// 入流量为192.168.222.5/32-\>192.168.222.71/32*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   outbound flow: 192.168.222.

71/32-\>192.168.222.5/32

*// 出流量为192.168.222.71/32-\>192.168.222.5/32*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   Lifetime second: 3600

*// 生命周期为3600秒*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   Lifetime kilobytes: 1843200

*// 生命周期为1843200字节*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   protocol: 51

  inbound SPI: 54e4913

   outbound SPI: 44213487

*// 协议为51，入方向SPI为：54e4913，出方向SPI为：44213487*

\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; IPsec SA state changed from IKE_P2_STATE_SEND1 to IKE_P2_STATE_SA_CREATED.

*// 二阶段SA状态从IKE_P2_STATE_SEND1到IKE_P2_STATE_SA_CREATED*

\*Aug 20 19:10:37:593 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.

*[// IKE*]*线程3087980192处理一个控制队列消息*

\*Aug 20 19:10:37:594 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3041606608 processes a job.

*[// IKE*]*线程3041606608处理一个job*

\*Aug 20 19:10:37:594 2012 Sysname IKE/7/EVENT: -MDC=1; IPsec SA state changed from IKE_P2_STATE_SA_CREATED to IKE_P2_STATE_ESTABLISHED.

*// 二阶段SA状态从IKE_P2_STATE_SA_CREATED到IKE_P2_STATE_ESTABLISHED*

\#在两个安全网关上配置了IKE协商类型的IPsec策略，若配置一阶段协商模式为主模式，认证方法为预共享密钥认证，则当有流量触发协商时，打开IKE报文调试信息开关后将输出以下调试信息。

\<Sysname\> debugging ike packet

\<Sysname\> ping -c 1  192.168.222.5

PING 192.168.222.5 (192.168.222.5): 56 data bytes, press CTRL_C to break

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Encryption algorithm is 3DES-CBC.

*// 加密算法为3DES-CBC*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Hash algorithm is HMAC-MD5.

*[// HASH*]*算法为HMAC-MD5*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   DH group 1.

*[// DH group*]*为1*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Authentication method is Pre-shared key.

*// 认证方法为Pre-shared key*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Lifetime type is Life type in seconds.

*// 生命周期类型为Life type in seconds*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 86400.

*// 生命周期为86400*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct transform payload 1.

*// 构造transform载荷，transform号为1*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct SA payload.

*// 构造SA载荷*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-T rfc3947 vendor ID payload.

*// 构造vendor id载荷，vendor ID名称为NAT-T rfc3947*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-T draft3 vendor ID payload.

*// 构造vendor id载荷，vendor ID名称为NAT-T draft3*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-T draft2 vendor ID payload.

*// 构造vendor id载荷，vendor ID名称为NAT-T draft2*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-T draft1 vendor ID payload.

*// 构造vendor id载荷，vendor ID名称为NAT-T draft1*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.222.5 local port 500, remote port 500.

*// 发送报文到地址192.168.222.5，本端端口号为500，对端端口号为500*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-Cookie: 3519bdda65bfeaaa

  R-Cookie: 0000000000000000

  next payload: SA

  version: ISAKMP Version 1.0

  exchange mode: Main

  flags: [ ]

  message ID: 0

  length: 164

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：0000000000000000*

*// 下一个载荷为：SA*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Main*

*// 标识为： *

*[// Message ID*]*为：0*

*// 长度为：164*

\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.

*// 发送一个IPv4报文*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Received packet from 192.168.

222.5 source port 500 destination port 500.

*// 收到的192.168.222.5报文，源端口为500，目的端口为500*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-Cookie: 3519bdda65bfeaaa

  R-Cookie: 078711749a32520c

  next payload: SA

  version: ISAKMP Version 1.0

  exchange mode: Main

  flags: [ ]

  message ID: 0

  length: 104

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：078711749a32520c*

*// 下一个载荷为：SA*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Main*

*// 标识为： *

*[// Message ID*]*为：0*

*// 长度为：104*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Received IKE Security Association Payload.

*// 收到SA载荷*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Vendor ID Payload.

*// 收到Vendor ID载荷*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Process SA payload.

*// 处理SA载荷*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Check ISAKMP transform 1.

检查ISAKMP transform，transform号为*1*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   Encryption algorithm is 3DES-CBC.

*// 加密算法为3DES-CBC*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   HASH algorithm is HMAC-MD5.

*[// HASH*]*算法为HMAC-MD5*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   DH group is 1.

*[// DH group*]*为1*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   Authentication method is Pre-shared key.

*// 认证方法为Pre-shared key*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   Lifetime type is Life type in seconds.

*// 生命周期类型为Life type in seconds*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 86400.

*// 生命周期为86400*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Attribuites is acceptable.

*// 属性是可接受的*

\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Process vendor ID payload.

*// 处理vendor ID载荷*

\*Aug 20 19:18:34:137 2012 Sysname IKE/7/PACKET: -MDC=1; Construct KE payload.

*// 构造IKE载荷*

\*Aug 20 19:18:34:137 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NONCE payload.

*// 构造NONCE载荷*

\*Aug 20 19:18:34:137 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-D payload.

*// 构造NAT-D载荷*

\*Aug 20 19:18:34:138 2012 Sysname IKE/7/PACKET: -MDC=1; Construct DPD vendor ID payload.

*// 构造DPD vendor ID载荷*

\*Aug 20 19:18:34:138 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.22

2.5 , remote port 500 ,local port 500.

*// 发送报文到地址192.168.222.5，对端端口号为500，本端端口号为500*

\*Aug 20 19:18:34:138 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-Cookie: 3519bdda65bfeaaa

  R-Cookie: 078711749a32520c

  next payload: KE

  version: ISAKMP Version 1.0

  exchange mode: Main

  flags: [ ]

  message ID: 0

  length: 208

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：078711749a32520c*

*// 下一个载荷为：KE*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Main*

*// 标识为： *

*[// Message ID*]*为：0*

*// 长度为：208*

\*Aug 20 19:18:34:138 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.

*// 发送一个IPv4报文*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received packet from 192.168.222.5 source port 500 destination port 500.

*// 收到的192.168.222.5报文，源端口为500，目的端口为500*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-Cookie: 3519bdda65bfeaaa

  R-Cookie: 078711749a32520c

  next payload: KE

  version: ISAKMP Version 1.0

  exchange mode: Main

  flags: [ ]

  message ID: 0

  length: 208

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：078711749a32520c*

*// 下一个载荷为：KE*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Main*

*// 标识为： *

*[// Message ID*]*为：0*

*// 长度为：208*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Key ExchangePayload.

*// 收到ISAKMP Key Exchange载荷*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Nonce Payload.

*// 收到ISAKMP Nonce载荷*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP NAT-D Payload.

*// 收到ISAKMP NAT-D载荷*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP NAT-D Payload.

*// 收到ISAKMP NAT-D载荷*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Vendor ID Payload.

*// 收到ISAKMP Vendor ID载荷*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Process KE payload.

*// 处理KE载荷*

\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Process NONCE payload.

*// 处理NONCE载荷*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; SKEYID:

 989e79e1 620ff603 a76bb9b9 7d88a19c

*[// SKEYID*]*为989e79e1 620ff603 a76bb9b9 7d88a19c*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; SKEYID_d:

 6fd7bd8f faf8480a af6c4813 4011cadd

*[// SKEYID_d*]*为6fd7bd8f faf8480a af6c4813 4011cadd*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; SKEYID_a:

 cd0aeaf8 6bb94aa3 3ad50fe4 7fb0464f

*[// SKEYID_a*]*为cd0aeaf8 6bb94aa3 3ad50fe4 7fb0464f*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; SKEYID_e:

 795d3765 91083053 65cacc69 000ffe09

*[// SKEYID_e*]*为795d3765 91083053 65cacc69 000ffe09*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Extended SKEYID_e:

 d554084f a2a9237a 9c141dac a41c86e9 8aa14807 14db45be

*// 扩展的SKEYID_e为d554084f a2a9237a 9c141dac a41c86e9 8aa14807 14db45be*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Local generated new IV:

 add7096a 4b961742

*// 本地新生成的IV为add7096a 4b961742*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Received 2 NAT-D payload.

*// 收到NAT-D载荷，数量为2*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Local ID type: IPV4_ADDR.

*// 本地ID类型为：IPV4_ADDR*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Local ID value: 192.168.222.

71.

*// 本端ID值为：192.168.222.71*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Construct ID payload.

*// 构造ID载荷*

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Hash:

 c5d733fa e6d1a6af ded56c05 de989aad

// HASH为c5d733fa e6d1a6af ded56c05 de989aad

\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Construct authentication by pre-shared key.

*// 根据预共享密钥生成认证数据*

\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Construct INITIAL-CONTACT payload.

*// 构造INITIAL-CONTACT载荷*

\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt the packet.

*// 加密报文*

\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt IV:

 add7096a 4b961742

*// 加密IV为add7096a 4b961742*

\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Encryption generated New IV: ae230a1d 7cb77287

*// 加密时新生成的IV为ae230a1d 7cb77287*

\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Process vendor ID payload.

*// 处理vendor ID载荷*

\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.222.5, remote port 500, local port 500.

*// 发送报文到地址192.168.222.5，对端端口号为500，本端端口号为500*

\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-Cookie: 3519bdda65bfeaaa

  R-Cookie: 078711749a32520c

  next payload: ID

  version: ISAKMP Version 1.0

  exchange mode: Main

  flags: [ENCRYPT]

  message ID: 0

  length: 92

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：078711749a32520c*

*// 下一个载荷为：ID*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Main*

*// 标识为：ENCRYPT*

*[// Message ID*]*为：0*

*// 长度为：92*

\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.

*// 发送一个IPv4报文*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Received packet from 192.168.

222.5, source port 500 destination port 500.

*// 收到的192.168.222.5报文，源端口为500，目的端口为500*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-cookie: 3519bdda65bfeaaa

  R-Cookie: 078711749a32520c

  next payload: ID

  version: ISAKMP Version 1.0

  exchange mode: Main

  flags: [ENCRYPT]

  message ID: 0

  length: 60

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：078711749a32520c*

*// 下一个载荷为：ID*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Main*

*// 标识为：ENCRYPT*

*[// Message ID*]*为：0*

*// 长度为：60*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Decrypt the packet.

*// 解密报文*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Decrypt IV:

 ae230a1d 7cb77287

*// 解密IV为ae230a1d 7cb77287*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Remote New IV:

 4c788f75 c7ad88ab

*// 对端新IV为4c788f75 c7ad88ab*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Identification Payload.

*// 收到ISAKMP Identification载荷*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Hash Payload.

*// 收到ISAKMP Hash载荷*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Process ID payload.

*// 处理ID载荷*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Peer ID type: IPV4_ADDR.

*// 对端ID类型为IPV4_ADDR*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Peer ID value: address 192.168.222.5.

*// 对端ID值为192.168.222.5*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Verify HASH payload.

*// 验证HASH载荷*

\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; HASH:

 f510f1f8 1d205e1c 9aa31c42 00b3ab9a

*[// HASH*]*为f510f1f8 1d205e1c 9aa31c42 00b3ab9a*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Set attributes by phase 2 transform.

*// 根据二阶段transform设置属性*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Encapsulation mode is Tunnel.

*// 封装模式为Tunnel*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Life type in seconds

*// 生命周期类型为Life type in seconds*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 3600.

*// 生命周期为3600*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Life type in kilobytes

*// 生命周期类型为Life type in kilobytes*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 1843200.

*// 生命周期为1843200*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Authentication algorithm is HMAC-SHA1

*// 认证算法为HMAC-SHA1*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Transform ID is HMAC-SHA1.

*[// Transform ID*]*为HMAC-SHA1*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct transform 1.

*// 构造transform 1*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct IPsec proposal 1.

*// 构造IPsec proposal，proposal号为1*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct IPsec SA payload.

*// 构造IPsec SA载荷*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NONCE payload.

*// 构造NONCE载荷*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct IPsec ID payload.

*// 构造IPsec ID载荷*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct IPsec ID payload.

*// 构造IPsec ID载荷*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct HASH(1) payload.

*// 构造HASH(1)载荷*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt packet.

*// 加密报文*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt IV:

 836eddd9 ed30acf7

*// 加密IV为836eddd9 ed30acf7*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypted Generate New IV:

 3b143591 5c647ff2

*// 加密时新生成的IV为3b143591 5c647ff2*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.22

2.5, remote port 500, local port 500.

*// 发送报文到地址192.168.222.5，对端端口号为500，本端端口号为500*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-Cookie: 3519bdda65bfeaaa

  R-Cookie: 078711749a32520c

  next payload: HASH

  version: ISAKMP Version 1.0

  exchange mode: Quick

  flags: [ENCRYPT]

  message ID: 8a9c07c1

  length: 156

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：078711749a32520c*

*// 下一个载荷为：HASH*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Quick*

*// 标识为：ENCRYPT*

*[// Message ID*]*为：8a9c07c1*

*// 长度为：156*

\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.

*// 发送一个IPv4报文*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received packet from 192.168.222.5 source port 500 destination port 500.

*// 收到的192.168.222.5报文，源端口为500，目的端口为500*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-Cookie: 3519bdda65bfeaaa

  R-Cookie: 078711749a32520c

  next payload: HASH

  version: ISAKMP Version 1.0

  exchange mode: Quick

  flags: [ENCRYPT]

  message ID: 8a9c07c1

  length: 156

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：078711749a32520c*

*// 下一个载荷为：HASH*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Quick*

*// 标识为：ENCRYPT*

*[// Message ID*]*为：8a9c07c1*

*// 长度为：156*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Decrypt the packet.

*// 加密报文*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Decrypt IV:

 3b143591 5c647ff2

*// 解密IV为3b143591 5c647ff2*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Remote New IV:

 4914de5c 11d57f5c

*// 对端新IV为4914de5c 11d57f5c*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Hash Payload.

*// 收到ISAKMP Hash 载荷*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Security Asso

ciation Payload.

*// 收到ISAKMP Security Association载荷*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Nonce Payload.

*// 收到ISAKMP Nonce载荷*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Identification Payload (IPsec DOI).

*// 收到ISAKMP Identificatio载荷(IPsec DOI)*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Identification Payload (IPsec DOI).

*// 收到ISAKMP Identificatio载荷(IPsec DOI)*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Process HASH payload.

*// 处理HASH载荷*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Process IPsec SA payload.

*// 处理IPsec SA载荷*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Check IPsec proposal 1.

*// 检查IPsec proposal，proposal号为1*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Parse transform 1.

*// 解析transform，transform号为1*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Encapsulation mode is Tunnel.

*// 封装模式为Tunnel*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Lifetime type is Life type in seconds.

*// 生命周期类型为Life type in seconds*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 3600.

*// 生命周期为3600*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Lifetime type is Life type in kilobytes.

*// 生命周期类型为Life type in kilobytes*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 1843200.

*// 生命周期为1843200*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Authentication algorithm is HMAC-SHA1.

*// 认证算法为HMAC-SHA1*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Transform ID is HMAC-SHA1.

*[// Transform ID*]*为HMAC-SHA1*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; The attributes are unacceptable.

*// 属性是可接受的*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Process IPsec ID Payload.

*[//  *]*处理IPsec ID载荷*

\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Process IPsec ID Payload.

*// 处理IPsec ID载荷*

\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Construct HASH(3) payload.

*// 构造HASH(3)载荷*

\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt the packet.

*// 加密报文*

\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt IV:

 4914de5c 11d57f5c

*// 加密IV为4914de5c 11d57f5c*

\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypted Generate New IV:

 ecfa444e ed72ab05

*// 加密时新生成的IV为ecfa444e ed72ab05*

\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.222.5, remote port 500, local port 500.

*// 发送报文到地址192.168.222.5，对端端口号为500，本端端口号为500*

\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1;

  I-Cookie: 3519bdda65bfeaaa

  R-Cookie: 078711749a32520c

  next payload: HASH

  version: ISAKMP Version 1.0

  exchange mode: Quick

  flags: [ENCRYPT]

  message ID: 8a9c07c1

  length: 52

*// 发起方cookie为：3519bdda65bfeaaa*

*// 响应方cookie为：078711749a32520c*

*// 下一个载荷为：HASH*

*// 版本为：ISAKMP Version 1.0*

*// 协商模式为：Quick*

*// 标识为：ENCRYPT*

*[// Message ID*]*为：8a9c07c1*

*// 长度为：52*

\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.

*// 发送一个IPv4报文*

