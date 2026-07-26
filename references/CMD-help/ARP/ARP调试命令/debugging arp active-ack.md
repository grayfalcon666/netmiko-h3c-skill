
**ARP \-- ARP调试命令 \-- debugging arp active-ack**

------------------------------------------------------------------------

【命令】

**[debugging arp active-ack**]

**[undo debugging arp active-ack**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging arp active-ack**]命令用来打开ARP主动确认调试信息开关。**undo debugging arp active-ack**命令用来关闭ARP主动确认调试信息开关。

缺省情况下，ARP主动确认调试信息开关处于关闭状态。

表1-1 debugging arp active-ack命令输出信息描述表

字段

描述

ARP active-ack for new event :

event-type: IP *ip-address*, MAC: *mac-address*, Port: *port-name*.

新学习ARP表项主动确认信息：事件类型为*event-type*,事件相关节点的IP为*ip-address*,MAC为*mac-address*,端口名为*port-name*

事件类型：

·Add a node：添加探测节点

·Aging a node：老化探测节点

·Ack a node：确认探测节点

ARP active-ack for new event :

Modify a node: IP *ip-address*, Old MAC: *old mac-address*, Old port: *old port-name*. New MAC: *new mac-address*, New port: *new port-name*.

更新ARP表项主动确认信息：事件相关节点的IP为*ip-address,*更新前MAC为*old mac-address*,端口名为o*ld port-name.*更新后MAC为*new mac-address*，端口为*new port-name*.

ARP active-ack probe node is up to the limit

主动确认探测节点数目达到上限

ARP active-ack status changed (IP: *ip-address*,  VLAN ID:*vlan-id*):

State: *old state* \-\-\--\> *new state*

Trigger: received a changed packet. MAC: *mac-address*, Port: *port-name.*

ARP 主动确认表项状态变化信息：IP为*ip-address,* VLAN ID为*vlan-id.*状态从*old state*变为*new state。*触发条件为收到一个端口*port-name*或者*mac-address*变化的ARP报文

状态：

·NoAttack：无攻击状态

·OldSent ：原用户探测报文已发送

·NewSent：新用户探测报文已发送

ARP active-ack status changed (IP: *ip-address*,  VLAN ID:*vlan-id*):

State: *old state* \-\-\--\> *new state*

Trigger: received an unchanged packet. MAC: *MAC-address*, port: *port-name.*

ARP 主动确认表项状态变化信息：IP为*ip-address,*VLAN为*vlan-id.*状态从*old state*变为*new state。*触发条件为收到一个端口或者MAC无变化的ARP报文

状态：

·NoAttack：无攻击状态

·OldSent：原用户探测报文已发送

·NewSent：新用户探测报文已发送

ARP active-ack status changed (IP: *ip-address*, VLAN ID:*vlan-id*):

State: *old state* \-\-\--\> *new state*

Trigger: time out for old user.

ARP 主动确认表项状态变化信息：IP为*ip-address,*VLAN为*vlan-id.*状态从*old state*变为*new state。*触发条件为老用户发送探测报文后在超时时间没没有收到回应报文

状态：

·NoAttack：无攻击状态

·OldSent：原用户探测报文已发送

·NewSent：新用户探测报文已发送

ARP active-ack status changed (IP: *ip-address*, VLAN ID:*vlan-id*):

State: *old state* \-\-\--\> *new state*

Trigger: time out for new user.

ARP 主动确认表项状态变化信息：IP为*ip-address,*VLAN为*vlan-id.*状态从*old state*变为*new state。*触发条件为新用户发送探测报文后在超时时间内没有收到回应报文

状态：

·NoAttac：无攻击状态

·OldSent：原用户探测报文已发送

·NewSent：新用户探测报文已发送

ARP active-ack status changed (IP: *ip-address*, VLAN ID:*vlan-id*):

State: *old state* \-\-\--\> *new state*

Trigger: new send state received a reply with a different source MAC or port.

 New MAC: *MAC-address*, new port: *port-name.*

ARP 主动确认表项状态变化信息：IP为*ip-address,*VLAN为*vlan-id.*状态从*old state*变为*new state。*触发条件为新用户发送探测报文后收到MAC或者端口变化的ARP报文

状态：

·NoAttack：无攻击状态

·OldSent：原用户探测报文已发送

·NewSen：新用户探测报文已发送

【举例】

\# 在系统视图下，使能ARP主动确认功能。

\<Sysname\> debugging arp active-ack

\*Aug  7 11:39:59:921 2011 Sysname ARP/7/ARP_ACTIVE_ACK: -MDC=1;

ARP active-ack for new event:

Ack a node: IP:192.168.80.203, MAC:2c41-3896-9424, Port:N/A

**ARP \-- ARP调试命令 \-- debugging arp entry**

------------------------------------------------------------------------

【命令】

**[debugging arp** **entry**]

**[undo debugging arp entry**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging arp entry**]命令用来打开ARP表项状态调试信息开关。**undo debugging arp entry**命令用来关闭ARP表项状态调试信息开关。

缺省情况下，ARP表项状态调试信息开关处于关闭状态。

表1-2 debugging ARP entry命令显示信息描述表

字段

描述

ARP entry status changed

ARP表项发生变化

MAC address

ARP表项的MAC地址

IP address

ARP表项的IP地址

*[state1*-\>*state2*]

从状态*state1*迁移到状态*state2*，共有四种状态：

·INITIALIZE：未解析状态

·NO_AGE：不老化状态

·AGING：老化处理状态

·AGED：老化待删除状态

【举例】

\# Router A和Router B相连，打开Router A的ARP表项状态调试信息开关，从Router A ping Router B，可查看到如下调试信息。

\<Sysname\> debugging arp entry

\<Sysname\> ping -c 1 192.168.111.188

PING 192.168.111.188 (192.168.111.188): 56 data bytes, press CTRL_C to break

56 bytes from 192.168.111.188: icmp_seq=0 ttl=128 time=1.000 ms

\-\-- 192.168.111.188 ping statistics \-\--

1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 1.000/1.000/1.000/0.000 ms

\*Dec 17 14:28:34:762 2012 H3C ARP/7/ARP_ENTRY: -MDC=1; ARP entry status ch

anged: MAC address: 000a-eb83-691e, IP address: 192.168.111.188, INITIALIZE -\> N

O_AGE

*[// IP*]*地址为192.168.111.188的ARP表项的状态由INITIALIZE迁移为NO_AGE。*

**ARP \-- ARP调试命令 \-- debugging arp error**

------------------------------------------------------------------------

【命令】

**[debugging arp** **error**]

**[undo debugging arp** **error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging arp error**]命令用来打开ARP的错误调试信息开关。**undo debugging arp error**命令用来关闭ARP的错误调试信息开关。

缺省情况下，ARP的错误调试信息开关处于关闭状态。

表1-3 debugging arp error命令显示信息描述表

字段

描述

Packet discarded for the network state of receiving interface is down.

接收接口网络层状态down，报文被丢弃

Packet discarded for the ARP packet is too short.

ARP报文长度太短，报文被丢弃

Packet discarded for the ARP packet is error.

ARP报文错误，报文被丢弃

Packet discarded for the link state of the port is down.

端口链路层状态down，报文被丢弃

Packet discarded for the sender IP is invalid.

报文源IP地址无效，报文被丢弃

Packet discarded for the sender IP is a broadcast IP.

报文源IP地址为广播IP，报文被丢弃

Packet discarded for the target IP is invaild.

报文请求的IP地址无效，报文被丢弃

Packet discarded for the target IP is a broadcast IP.

报文请求的IP地址为广播IP，报文被丢弃

Failed to get the source MAC of the ARP reply.

获取应答报文的源MAC失败

Packet discarded for the source MAC is a multicast address.

源MAC是组播MAC，报文被丢弃

Packet discarded for the source MAC is a broadcast address.

源MAC是广播MAC，报文被丢弃

Packet discarded for the sender MAC address is the same as the receiving interface.

源MAC和接口MAC相同，报文被丢弃

Packet discarded for the number of ARP entries reaches the limit.

ARP表项数目达到上限，报文被丢弃

Packet discarded for ARP packet is not necessary to concerned.

ARP不需要被学习，报文被丢弃

Packet discarded for the type of receiving interface is L2VE.

报文入端口是L2VE口，报文被丢弃

Packet discarded for conflict with static entry.

和静态配置冲突，报文被丢弃

sender IP

源IP地址

target IP

目的IP地址

MDC

逻辑设备号

Interface

接口名

【举例】

\# 开启ARP错误调试信息开关，在报文目的IP地址无效时，调试信息如下。

\<Sysname\> debugging arp error

\*Oct 30 22:44:44:559 2012 Sysname ARP/7/ ARP_ERROR: -MDC=1;    

Packet discarded for target IP is invalid. Interface: M-E1/0/1  sender IP: 192.168.239.1  target IP : 192.168.239.251

*[//*]*目的IP地址无效，报文被丢弃。接口为M-E1/0/1，报文的源IP地址为192.168.239.1，目的IP地址为192.168.239.251*

**ARP \-- ARP调试命令 \-- debugging arp fast-reply**

------------------------------------------------------------------------

【命令】

**[debugging arp fast-reply**]

**[undo debugging arp fast-reply**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging arp fast-reply**]命令用来打开ARP快速应答调试信息开关。**undo debugging arp fast-reply**命令用来关闭ARP快速应答调试信息开关。

缺省情况下，ARP快速应答调试信息开关处于关闭状态。

表1-4 debugging arp fast-reply命令显示信息描述表

字段

描述

Src Interface

源VLAN下的端口

VLAN ID

VLAN ID

SenderMAC

ARP报文携带的源MAC

SenderIP

源IP地址

TargetMAC

ARP报文携带的目标MAC

TargetIP

目的IP地址

SrcEthMAC

以太层源MAC

DstEthMAC

以太层目的MAC

Packet type

报文类型：

·REQUEST： ARP请求报文

·REPLY:ARP：应答报文

·GRATUITOUS：免费ARP报文

Return: TargetIP is same as the local IP address of the VLAN interface.

处理结果：收到报文的目的IP为本地VLAN接口的[IP地址]

Return: Get info from ARP snooping:

VLAN: *vlan-id*, port: *port-name* IP: *ip-address*, MAC: *MAC-address*

处理结果：从ARP snooping查到代答表项，VLAN为 *vlan-id*,端口为 *port-name* ,IP为 *ip-address*, MAC为 *MAC-address*

Return: Get info from DHCP snooping:

 VLAN: *vlan-id*, port: *port-name* IP: *ip-address*, MAC: *MAC-address*

处理结果：从DHCPsnooping查到代答表项，VLAN为 *vlan-id*,端口为 *port-name* ,IP为 *ip-address*, MAC为 *MAC-address*

【举例】

\# 在VLAN 299下使能快速应答功能。

\<Sysname\> debugging arp fast-reply

\*Aug  7 11:55:26:906 2011 Sysname ARP/7/ARP_FAST_REPLY: -MDC=1-Chassis=1-Slot=3;

Received ARP packet:

 Src Interface :GE1/0/2           VLAN ID   :299

 SenderMAC     :000a-eb83-691e    SenderIP  :192.168.20.188

 TargetMAC     :0000-0000-0000    TargetIP  :192.168.20.120

 SrcEthMAC     :000a-eb83-691e    DstEthMAC :ffff-ffff-ffff

 PacketType    :REQUEST

 Return: TargetIP is the same as the interface VLAN.

**ARP \-- ARP调试命令 \-- debugging arp packet**

------------------------------------------------------------------------

【命令】

**[debugging arp packet**]

**[undo debugging arp packet**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging arp packet**]命令用来打开ARP的报文调试信息开关。**undo debugging arp packet**命令用来关闭ARP的报文调试信息开关。

缺省情况下，ARP的报文调试信息开关处于关闭状态。

表1-5 debugging arp packet命令输出信息描述表

字段

描述

ARP_SEND: Send an ARP packet

发送ARP报文

ARP_RCV: Receive an ARP packet

收到ARP报文

operation

报文类型（1：Request报文；2：Reply报文）

sender MAC

源MAC地址

sender IP

源IP地址

target MAC

目标MAC地址

target IP

目标IP地址

【举例】

\# Router A和Router B相连，打开Router A的ARP报文调试信息开关，从Router A ping Router B，可查看到如下调试信息：

\<Sysname\> debugging arp packet

\<Sysname\> ping -c 1 2.253.253.1

\*Apr 19 16:02:20:832 2006 Sysname ARP/7/ARP_SEND: -MDC=1;Sent an ARP message, operation: 1, sender MAC: 0000-0000-0001, sender IP: 2.2.1.1, target MAC: 0000-0000-0000, target IP: 2.253.253.1

*// 发送一个ARP请求报文，目标IP地址为2.253.253.1，源IP地址为2.2.1.1*

\*Apr 19 16:02:21:422 2006 Sysname ARP/7/ARP_RCV: -MDC=1; Received an ARP message, operation: 2, sender MAC:00e0-fc5a-ed28, sender IP:2.253.253.1, target MAC: 0000-0000-0001, target IP: 2.2.1.1

*// 收到一个ARP应答报文，目标IP地址为2.2.1.1，源IP地址为2.253.253.1*

**ARP \-- ARP调试命令 \-- debugging arp pnp**

------------------------------------------------------------------------

【命令】

**[debugging arp pnp**]

**[undo debugging arp pnp**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging arp pnp**]命令用来打开即插即用网关的调试信息开关。**undo debugging arp pnp**命令用来关闭即插即用网关的调试信息开关。

缺省情况下，即插即用网关的调试信息开关处于关闭状态。

表1-6 debugging arp pnp命令显示信息描述表

字段

描述

PACKET: (*interface-type* *interface-number-direction*)

报文信息：（接口名-报文方向）

*[OrgSrcIP*  -  *OrgDstIP* \-\-\-\-\--\>]

*[NewSrcIP*  -  *NewDstIP*]

IP转换前的报文原始二元组：

·*OrgSrcIP*：原始源IP地址；

·*OrgDstIP*：原始目的IP地址；

IP转换后的报文新二元组：

·*NewSrcIP*：新源IP地址；

·*NewDstIP*：新目的IP地址；

The number of ARP PNP entries on the interface *interface-type interface-num* has reached the maximum.

接口*interface-type interface-num*下的即插即用网关用户表项达到最大数量，报文将被丢弃

【举例】

\# 在启用了即插即用网关功能的接口上，打开该设备ARP PNP调试信息开关，有IP报文通过该接口时输出如下调试信息。

\<Sysname\> debugging arp pnp

\*Jan 30 17:18:48:610 2012 Sysname ARP/7/ARP_PNP: -MDC=1;

PACKET: (GigabitEthernet1/0/2-in)

   192.168.1.100  -  2.2.2.100\-\-\-\-\--\>

   2.2.2.254  -  2.2.2.100

*// 在GigabitEthernet1/0/2收到[IP报文进行了]IP地址转换（转换了源IP地址）*

\# 当用户表项满时会输出下列调试信息。

The number of ARP PNP entries on the interface GigabitEthernet 1/0/2 has reached the maximum.

**ARP \-- ARP调试命令 \-- debugging arp source-mac**

------------------------------------------------------------------------

【命令】

**[debugging arp source-mac**]

**[undo debugging arp source-mac**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging arp source-mac**]命令用来打开源MAC地址固定的ARP攻击检测调试信息开关。**undo debugging arp source-mac**命令用来关闭源MAC地址固定的ARP攻击检测调试信息开关。

缺省情况下，源MAC地址固定的ARP攻击检测调试信息开关处于关闭状态。

表1-7 debugging arp source-mac命令显示信息描述表

字段

描述

Failed to add the node MAC: *MAC-address*, VLAN:* vlan-id*because the number of entries reaches the limit.

表项达到上限，添加节点, MAC:* MAC-address*,VLAN:* vlan-id *失败

*[Action-type *]an entry to hardware. MAC: *MAC-address.* VLAN: *vlan-id.* Port:*portIfIndex.* The result is *result.*

添加表项到驱动的调试信息，动作为*Action-type，MAC*为*MAC-address*，端口索引为*portIfIndex。*返回值为*result*

*[Action-type:*]

·Add：下驱动增加

·Del：下驱动删除

【举例】

\# 在系统视图下，使能源MAC固定ARP攻击检测功能，并选择过滤模式。

\<Sysname\> debugging arp source-mac

%Aug  7 11:16:22:466 2011 Sysname ARP/6/ARP SOURCE-MAC: -MDC=1; Failed to add the node MAC: 2c41-3896-9424, VLAN: 2 because the number of entries reaches the limit.
