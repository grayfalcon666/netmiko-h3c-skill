<!-- CMD-INDEX
  display udp-helper interface        | 任意视图             | L11
  reset udp-helper statistics         | 用户视图             | L97
  udp-helper broadcast-map            | 接口视图             | L127
  udp-helper enable                   | 系统视图             | L189
  udp-helper multicast-map            | 接口视图             | L239
  udp-helper port                     | 系统视图             | L311
  udp-helper server                   | 接口视图             | L369
-->

**UDP Helper \-- UDP Helper配置命令 \-- display udp-helper interface**

------------------------------------------------------------------------

**[display udp-helper interface**]命令用来显示指定接口下广播转单播中继转发的相关信息。

【命令】

**[display udp-helper** **interface** *interface-type interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：接口类型和接口编号。

【使用指导】

通过本命令可以查看指定接口配置的广播转单播中继转发的目的服务器信息以及广播转单播中继转发处理的报文数目。

【举例】

·路由应用

\# 显示GigabitEthernet1/0/1接口的UDP中继转发相关信息。

\<Sysname\> display udp-helper interface gigabitethernet 1/0/1

Interface                Server VPN instance            Server address   Packets sent

GigabitEthernet1/0/1     abc                           192.1.1.2        0

GigabitEthernet1/0/1     N/A                           192.1.1.2        0

·交换应用

\# 显示VLAN接口1的UDP中继转发相关信息。

\<Sysname\> display udp-helper interface vlan-interface 1

Interface                Server VPN instance           Server address Packets sent

Vlan-interface1          abc                           192.1.1.2      0

Vlan-interface1          N/A                           192.1.1.2      0

表1-1 display udp-helper interface命令显示信息描述表

字段

描述

Interface

接口名

Server VPN instance

中继转发目的服务器所在的VPN实例名

Server address

中继转发目的服务器地址

Packets sent

广播转单播UDP Helper 处理的报文数目

【相关命令】

·**reset udp-helper statistics**

·**udp-helper server**

**UDP Helper \-- UDP Helper配置命令 \-- reset udp-helper statistics**

------------------------------------------------------------------------

**[reset udp-helper statistics**]命令用来清除广播转单播中继转发的报文统计数目。

【命令】

**[reset udp-helper statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除广播转单播中继转发的报文统计数目。

\<Sysname\> reset udp-helper statistics

【相关命令】

·**display udp-helper interface**

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper broadcast-map**

------------------------------------------------------------------------

**[udp-helper broadcast-map**]命令用来配置广播转组播中继转发。

**[undo **]**udp-helper broadcast-map**命令用来取消广播转组播中继转发。

【命令】

**[udp-helper broadcast-map**] *multicast-address* [ **acl** *acl-number* ]

**[undo **]**udp-helper broadcast-map** *multicast-address*

【缺省情况】

没有配置广播转组播中继转发。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[multicast-address*]：组播地址。中继处理UDP广播报文时，将其目的IP地址从广播地址修改为指定的组播地址。

**[acl*** acl-number*]：ACL的编号。通过指定ACL来实现对接口入方向的报文进行过滤，符合条件的才会按照配置的组播中继进行转发。支持基本ACL（2000～2999）与高级ACL（3000～3999）。

【使用指导】

·请在接收广播报文的入接口上配置广播转组播中继转发。

·一个接口上最多可以配置的广播中继个数为20个（包括广播转单播和广播转组播）。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置广播转组播映射。

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname-GigabitEthernet1/0/1 udp-helper broadcast-map 225.0.0.1

·交换应用

\# 在VLAN接口上配置广播转组播映射。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-vlan-interface 100 udp-helper broadcast-map 225.0.0.1

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper enable**

------------------------------------------------------------------------

**[udp-helper enable**]命令用来使能UDP Helper功能。

**[undo udp-helper enable**]命令用来关闭UDP Helper功能。

【命令】

**[udp-helper enable**]

**[undo udp-helper enable**]

【缺省情况】

UDP Helper功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能UDP Helper功能后，只有当全局配置了需要中继转发的UDP端口号，并且接口下配置了UDP Helper相关配置时，UDP Helper功能才会生效。

【举例】

\# 使能UDP Helper功能。

\<Sysname\> system-view

Sysname udp-helper enable

【相关命令】

·**udp-helper port**

·**udp-helper server**

·**udp-helper multicast-map**

·**udp-helper broadcast-map**

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper multicast-map**

------------------------------------------------------------------------

![说明](UDP%20Helper命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[udp-helper multicast-map**]命令用于配置组播MAP映射。

**[undo **]**udp-helper multicast-map**命令用来取消组播MAP映射。

【命令】

**[udp-helper multicast-map**] *multicast-address ip-address***[[ **global** \| **vpn-instance** *vpn-instance-name* ]]** **acl** *acl-number*

**[undo udp-helper multicast-map **]*multicast-address ip-address *[[ **global** \| **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

没有配置组播MAP映射。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[multicast-address*]：组播地址。需要做中继处理的UDP组播报文的目的地址。

*[ip-address*]：IP地址，只能为单播地址或定向广播地址，不支持配置为受限广播地址。中继处理UDP组播报文时，将其目的地址从组播地址修改为指定的IP地址。

**[global**]：表示在公网中转发组播中继的报文。

**[vpn-instance*** vpn-instance -name*]：表示在指定VPN实例中转发组播中继的报文，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

**[acl*** acl*]*-number*：ACL的编号。通过指定ACL来实现对接口入方向的报文进行过滤，符合条件的才会按照配置的组播中继进行转发。支持基本ACL（2000～2999）与高级ACL（3000～3999）。

【使用指导】

·组播MAP包括组播转广播和组播转单播两种情况，当*ip-address*为单播地址时，则将组播报文转换为单播报文，当*ip-address*为广播地址时，则将组播报文转换为广播报文。

·请在接收组播报文的入接口上配置组播MAP映射，配置指定了VPN时在配置指定的私网内转发中继后的报文，当配置指定了global时在公网中转发中继后的报文，当两者都未指定时在当前接口绑定的VPN中转发中继后的报文，若接口未绑定VPN，则在公网中转发。

·接口下配置组播MAP映射时，同一个组播地址可以映射给16个IP地址。配置成功的组播MAP映射，同一个组播报文会同时转发给配置的单播地址和配置的定向广播地址。

【举例】

\# 在接口GigabitEthernet1/0/1上配置目地地址为225.0.0.1的组播报文转为地址为192.168.1.0网段的子网的广播地址。

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname-GigabitEthernet1/0/1 udp-helper multicast-map 225.0.0.1 192.168.1.255

\# 在接口GigabitEthernet1/0/1上配置目地地址为225.0.0.1的组播报文转为VPN实例a内的服务器192.168.1.3。

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname- GigabitEthernet1/0/1 udp-helper multicast-map 225.0.0.1 192.168.1.255 vpn-instance a

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper port**

------------------------------------------------------------------------

**[udp-helper port**]命令用来配置需要中继转发的UDP端口。

**[undo udp-helper port**]命令用来取消对需要中继转发的UDP端口的配置。

【命令】

**[udp-helper port **[{ *port-number* **\| dns \| netbios-ds \| netbios-ns \| tacacs \| tftp \| time** }]]

**[undo udp-helper port **[{ *port-number* **\| dns \| netbios-ds \| netbios-ns \| tacacs \| tftp \| time** }]]

【缺省情况】

没有配置中继转发的UDP端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：需要中继转发的UDP端口号，取值范围为1～65535（不支持67和68）。有些UDP端口号在某些设备上不支持，请以设备的实际情况为准。

**[dns**]：对DNS报文进行中继转发，对应的UDP端口号为53。

**[netbios-ds**]：对NetBIOS数据服务报文进行中继转发，对应的UDP端口号为138。

**[netbios-ns**]：对NetBIOS名字服务报文进行中继转发，对应的UDP端口号为137。

**[tacacs**]：对终端访问控制器访问控制系统报文进行中继转发，对应的UDP端口号为49。

**[tftp**]：对简单文件传输协议报文进行中继转发，对应的UDP端口号为69。

**[time**]：对时间服务报文进行中继转发，对应的UDP端口号为37。

【使用指导】

需要中继转发的UDP端口有两种配置方法：指定端口号配置和指定参数配置。例如：**udp-helper port** 53和**udp-helper port** **dns**的效果是一样的。

设备上最多可以配置256个需要中继转发的UDP端口。

【举例】

\# 配置对目的UDP端口号为100的广播报文进行中继转发。

\<Sysname\> system-view

Sysname udp-helper port 100

**UDP Helper \-- UDP Helper配置命令 \-- udp-helper server**

------------------------------------------------------------------------

**[udp-helper server**]命令用来配置广播转单播中继转发的目的服务器。

**[undo udp-helper server**]命令用来删除广播转单播中继转发的目的服务器的配置。

【命令】

**[udp-helper server** *ip-address***[[ **global** \| **vpn-instance** *vpn-instance-name* ]]]

**[undo udp-helper server** [ *ip-address* [[ **global** \| **vpn-instance** *vpn-instance-name* ] ]]]

【缺省情况】

没有配置广播转单播中继转发的目的服务器。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：目的服务器的IP地址，为点分十进制形式。

**[global**]：指定只在公网中转发中继后的报文。

**[vpn-instance*** vpn-instance-name*]：表示在指定的VPN实例中转发。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

·请在接收广播报文的入接口上配置中继转发的目的服务器。一个接口上最多可以配置的广播中继个数为20个（包括广播转单播和广播转组播）。

·配置**undo udp-helper server**命令时如果不指定IP地址，将会删除该接口下配置的所有广播转单播中继转发的目的服务器。

·带**vpn-instance**关键字的server配置与带**global**关键字的相同的server配置不互相覆盖，当配置指定了VPN实例时在配置的VPN中转发，配置指定了**global**时在公网中转发，两者均未指定时默认在接口下绑定的VPN中转发，若接口未绑定VPN，则在公网中转发。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置广播转单播中继转发的目的服务器为192.1.1.2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 udp-helper server 192.1.1.2

\# 在接口GigabitEthernet1/0/1上配置广播转单播中继转发的目的服务器为VPN实例a内的192.1.1.2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 udp-helper server 192.1.1.2 vpn-instance a

·交换应用

\# 在VLAN接口100上配置广播转单播中继转发的目的服务器为192.1.1.2。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 udp-helper server 192.1.1.2

\# 在VLAN接口100上配置广播转单播中继转发的目的服务器为公网内的192.1.1.2。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 udp-helper server 192.1.1.2 global

【相关命令】

·**display udp-helper interface**

