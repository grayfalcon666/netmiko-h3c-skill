
**MFF \-- MFF配置命令 \-- display mac-forced-forwarding interface**

------------------------------------------------------------------------

**[display mac-forced-forwarding interface**]命令用来显示MFF端口配置信息。

【命令】

**[display mac-forced-forwarding interface**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示MFF端口配置信息。

\<Sysname\> display mac-forced-forwarding interface

Network Port:

GE1/0/1                  GE1/0/2

User Port:

GE1/0/3                  GE1/0/4                  GE1/0/5

GE1/0/6                  GE1/0/7                  GE1/0/8

GE1/0/9                  GE1/0/10                 GE1/0/11

GE1/0/12                 GE1/0/13                 GE1/0/14

GE1/0/15                 GE1/0/16                 GE1/0/17

GE1/0/18                 GE1/0/19                 GE1/0/20

GE1/0/21                 GE1/0/22                 GE1/0/23

GE1/0/24                 GE1/0/25                 GE1/0/26

GE1/0/27                 GE1/0/28                 GE1/0/29

GE1/0/30                 GE1/0/31                 GE1/0/32

GE1/0/33                 GE1/0/34                 GE1/0/35

GE1/0/36                 GE1/0/37                 GE1/0/38

GE1/0/39                 GE1/0/40                 GE1/0/41

GE1/0/42                 GE1/0/43                 GE1/0/44

GE1/0/45                 GE1/0/46                 GE1/0/47

GE1/0/48

表1-1 display mac-forced-forwarding interface命令显示信息描述表

字段

描述

Network Port

配置为网络端口的端口列表

User Port

配置为用户端口的端口列表

【相关命令】

·**mac-forced-forwarding**** network-port**

**MFF \-- MFF配置命令 \-- display mac-forced-forwarding vlan**

------------------------------------------------------------------------

**[display mac-forced-forwarding vlan**]命令用来显示指定VLAN的MFF信息。

【命令】

**[display mac-forced-forwarding vlan ***vlan-id*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vlan-id*]：显示指定VLAN的MFF信息。

【举例】

\# 显示VLAN 2的MFF信息。

\<Sysname\> display mac-forced-forwarding vlan 2

VLAN 2

Mode: Auto/Single

Gateway:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

192.168.1.42         000f-e200-8046

Server:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

192.168.1.48         192.168.1.49

表1-2 display mac-forced-forwarding vlan命令显示信息描述表

字段

描述

VLAN 2

网关IP所对应的VLAN ID

Mode

MFF运行模式，分为自动方式（Auto）和手动方式（Manual）以及单网关模式（Single）

Gateway

网关IP地址和网关MAC地址，未学习到则显示"N/A"

Server

服务器的IP地址

【相关命令】

·**mac-forced-forwarding**

·**mac-forced-forwarding server**

**MFF \-- MFF配置命令 \-- mac-forced-forwarding**

------------------------------------------------------------------------

**[mac-forced-forwarding**]命令用来启用MFF功能，同时配置MFF的工作方式，如果是手工方式，必须指定缺省网关。

**[undo mac-forced-forwarding**]命令用来关闭MFF功能。

【命令】

**[mac-forced-forwarding **[{ **auto** \| **default-gateway** *gateway-ip* }]]

**[undo mac-forced-forwarding**]

【缺省情况】

MFF功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：自动方式。

**[default-gateway ***gateway-ip*]：手工方式下MFF的缺省网关IP地址。

【使用指导】

·自动方式下要求设备启用DHCP Snooping功能并配置相应的DHCP Snooping信任端口；

·手工方式下要求设备启用ARP Snooping功能。

·对于用户手动配置IP地址的网络（或者VLAN），网关的IP地址必须是手工配置，MFF只检查手工配置的网关是否是全0或全1的IP地址，全0或全1的IP地址不能作为网关地址进行配置；对于用户通过DHCP协议动态获取IP地址的网络，网关的IP地址可以通过手动配置，也可以通过对DHCP报文中的Option字段解析获取。

·多次配置此命令，新的配置会覆盖已有的配置。

【举例】

\# 启用VLAN 2下的自动方式MFF功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 mac-forced-forwarding auto

【相关命令】

·**mac-forced-forwarding server**

**MFF \-- MFF配置命令 \-- mac-forced-forwarding gateway probe**

------------------------------------------------------------------------

**[mac-forced-forwarding gateway probe**]命令用来启动对MFF维护的网关进行定时探测，以便感知网关MAC地址的变化。

**[undo mac-forced-forwarding gateway probe**]命令用来恢复缺省情况。

【命令】

**[mac-forced-forwarding gateway probe**]

**[undo mac-forced-forwarding gateway probe**]

【缺省情况】

网关定时探测功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在配置**mac-forced-forwarding gateway probe**命令之前需要启用**mac-forced-forwarding**功能。对网关进行定时探测的时间间隔为30秒。手工方式和自动方式都支持对网关的定时探测功能。

【举例】

\# 启用网关定时探测功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 mac-forced-forwarding gateway probe

【相关命令】

·**mac-forced-forwarding**

**MFF \-- MFF配置命令 \-- mac-forced-forwarding network-port**

------------------------------------------------------------------------

**[mac-forced-forwarding network-port**]命令用来配置端口为网络端口。

**[undo mac-forced-forwarding network-port**]命令用来恢复缺省情况。

【命令】

**[mac-forced-forwarding network-port**]

**[undo mac-forced-forwarding network-port**]

【缺省情况】

端口为用户端口。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·上行连接网关的端口，级联组网（多个MFF设备连接在一起的组网）时连接其他MFF设备的端口，或者环型组网时设备之间的端口，都应该配置为网络端口。可以设置多个端口为网络端口。

·不论端口所属VLAN是否启用了MFF功能，都可以配置端口的MFF角色。不过只有启用了MFF功能后，配置的MFF端口角色才真正生效。

·网络端口支持链路聚合，用户端口不支持链路聚合。当网络端口加入了链路聚合组，且所属VLAN启用了MFF功能时，如果用户想取消网络端口的配置，则需要先将网络端口从链路聚合组中退出，然后再取消网络端口的配置。关于链路聚合的介绍，请参见"二层技术-以太网交换"中的"以太网链路聚合配置"。

【举例】

\# 配置GigabitEthernet1/0/1端口为网络端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-forced-forwarding network-port

【相关命令】

·**mac-forced-forwarding**

**MFF \-- MFF配置命令 \-- mac-forced-forwarding server**

------------------------------------------------------------------------

**[mac-forced-forwarding server**]命令用来配置网络中部署的服务器的IP地址。

**[undo mac-forced-forwarding server**]命令用来删除服务器的IP地址。

【命令】

**[mac-forced-forwarding server ***server-ip*&\<1-10\>]

**[undo mac-forced-forwarding server** *server-ip*&\<1-10\>]

【缺省情况】

没有配置网络中部署的服务器的IP地址。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-ip*&\<1-10\>]：网络中部署的服务器的IP地址，&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

如果网络中部署了服务器，就需要在启用MFF功能的设备的服务器列表中添加此服务器的IP地址，否则，客户端与服务器之间不能进行通信。

服务器IP地址可以是DHCP Server的IP地址，也可以是其他业务的服务器的IP地址或者是VRRP备份组中某个路由器的接口IP地址。

如果MFF设备的网络端口收到了源IP地址为服务器IP地址的ARP请求，则查询本设备记录的用户信息，利用查询到的用户信息代替客户端应答给服务器。即客户端发送给服务器的报文，都会通过网关进行转发，而服务器发送给客户端的报文，则不需经过网关转发。

MFF不检查服务器的IP地址和网关IP地址是否在同一个网段，只检查是否是全0或全1的IP地址，全0或全1的IP地址不能作为服务器IP地址进行配置。

在手工方式和自动方式下都可以配置本功能。

需要注意的是，在配置**mac-forced-forwarding server**命令之前需要启用MFF功能。

【举例】

\# 配置网络中部署的服务器的IP地址为192.168.1.100。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 mac-forced-forwarding server 192.168.1.100

【相关命令】

·**mac-forced-forwarding**
