
**IP地址 \-- IP地址配置命令 \-- display ip interface**

------------------------------------------------------------------------

**[display** **ip** **interface**]命令用来显示三层接口与IP相关的配置和统计信息。

【命令】

**[display** **ip** **interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：显示指定接口的相关信息。

【使用指导】

**[display** **ip** **interface**]命令用来查看三层接口与IP相关的配置和统计信息，包括接口上接收和发送的单播报文数、字节数和组播报文数，以及接口上收到的TTL无效报文数和ICMP报文数等。

通过对显示信息中报文收发情况的分析，可以初步判断网络是否遭到攻击和攻击的可能来源。

如果不指定参数，则显示所有三层接口的相关信息。

【举例】

·路由应用

\# 显示接口GigabitEthernet1/0/1与IP相关的配置和统计信息。

\<Sysname\> display ip interface gigabitethernet 1/0/1

GigabitEthernet1/0/1 current state: DOWN

Line protocol current state: DOWN

Internet Address is 1.1.1.1/8 Primary

Broadcast address: 1.255.255.255

The Maximum Transmit Unit: 1500 bytes

input packets : 0, bytes : 0, multicasts : 0

output packets : 0, bytes : 0, multicasts : 0

TTL invalid packet number:         0

ICMP packet input number:          0

  Echo reply:                      0

  Unreachable:                     0

  Source quench:                   0

  Routing redirect:                0

  Echo request:                    0

  Router advert:                   0

  Router solicit:                  0

  Time exceed:                     0

  IP header bad:                   0

  Timestamp request:               0

  Timestamp reply:                 0

  Information request:             0

  Information reply:               0

  Netmask request:                 0

  Netmask reply:                   0

  Unknown type:                    0

·交换应用

\# 显示VLAN接口10与IP相关的配置和统计信息。

\<Sysname\> display ip interface vlan-interface 10

Vlan-interface10 current state: DOWN

Line protocol current state: DOWN

Internet Address is 1.1.1.1/8 Primary

Broadcast address: 1.255.255.255

The Maximum Transmit Unit: 1500 bytes

input packets : 0, bytes : 0, multicasts : 0

output packets : 0, bytes : 0, multicasts : 0

TTL invalid packet number:         0

ICMP packet input number:          0

  Echo reply:                      0

  Unreachable:                     0

  Source quench:                   0

  Routing redirect:                0

  Echo request:                    0

  Router advert:                   0

  Router solicit:                  0

  Time exceed:                     0

  IP header bad:                   0

  Timestamp request:               0

  Timestamp reply:                 0

  Information request:             0

  Information reply:               0

  Netmask request:                 0

  Netmask reply:                   0

  Unknown type:                    0

表1-1 display ip interface命令显示信息描述表

字段

描述

current state

接口当前的物理状态，可能的状态及含义如下：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭（可能因为没有连接好或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Line protocol current state

链路层协议当前状态，可能的状态及含义如下：

·DOWN：该接口的协议状态为关闭

·UP：该接口的协议状态为开启

·UP (spoofing)：该接口的协议状态为欺骗性开启，即虽然接口的链路层协议状态显示是开启的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立的

Internet Address

接口的IP地址，IP地址后可携带如下参数：

·Primary：表示手动配置的主IP地址

·Sub：表示手动配置的从IP地址

·MTunnel：表示MTunnel口IP地址

·SSLVPN：表示SSL VPN虚接口IP地址

·PPP-Negotiated：表示PPP动态协商IP地址

·Unnumbered：表示借用IP地址

·DHCP-Allocated：表示DHCP动态分配IP地址

·BOOTP-Allocated：表示BOOTP动态分配IP地址

·Cluster：表示集群IP地址

·Mad：表示MAD IP地址

Broadcast address

接口所在网段的广播地址

The Maximum Transmit Unit

接口的最大传输单元，单位为字节

input packets, bytes, multicasts

output packets, bytes, multicasts

接口上接收和发送的单播报文数、字节数以及组播报文数（设备启动后就开始统计此信息）

TTL invalid packet number

接口上收到的TTL无效的报文个数（设备启动后就开始统计此信息）

ICMP packet input number:

  Echo reply:

  Unreachable:

  Source quench:

  Routing redirect:

  Echo request:

  Router advert:

  Router solicit:

  Time exceed:

  IP header bad:

  Timestamp request:

  Timestamp reply:

  Information request:

  Information reply:

  Netmask request:

  Netmask reply:

  Unknown type:

接口上收到的ICMP报文的总数（设备启动后就开始统计此信息），包括如下报文：

·Echo应答报文

·不可达报文

·源站抑制报文

·路由重定向报文

·Echo请求报文

·路由器通告报文

·路由器请求报文

·超时报文

·IP报文头错误报文

·时间戳请求报文

·时间戳响应报文

·信息请求报文

·信息响应报文

·掩码请求报文

·掩码响应报文

·未知类型报文

【相关命令】

·**display** **ip** **interface** **brief**

·**ip** **address**

**IP地址 \-- IP地址配置命令 \-- display ip interface brief**

------------------------------------------------------------------------

**[display** **ip** **interface** **brief**]命令用来显示三层接口与IP相关的简要信息。

【命令】

**[display** **ip** **interface** [ *interface-type* [ *interface-number*  ] **brief**  **description** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type*]：显示指定类型接口的IP基本配置信息。

*[interface-number*]：显示指定接口的IP基本配置信息。

**[description**]：显示接口完整的描述信息。如果不指定该参数，则最多可以显示16个字符，如果超过16个字符，那么则显示前14个字符和"..."。

【使用指导】

**[display** **ip** **interface** **brief**]命令用来查看三层接口与IP相关的简要信息，包括接口的物理和链路层协议状态、IP地址、描述信息等。

需要注意的是：

·如果不指定接口类型和接口编号，则显示所有三层接口的IP基本配置信息；

·如果只指定接口类型，不指定接口编号，则显示该类型所有三层接口的IP基本配置信息；

·如果同时指定接口类型和接口编号，则显示指定接口的IP基本配置信息。

【举例】

·路由应用

\# 显示GigabitEthernet接口的基本配置信息。

\<Sysname\> display ip interface gigabitethernet brief

\*down: administratively down

(s): spoofing  (l): loopback

Interface                Physical Protocol IP Address      Description

GE1/0/1                  up       up       5.5.5.1         Link to CoreRo\...

\<Sysname\> display ip interface gigabitethernet brief description

\*down: administratively down

(s): spoofing  (l): loopback

Interface                Physical Protocol IP Address      Description

GE1/0/1                  up       up       5.5.5.1         Link to CoreRouter

·交换应用

\# 显示VLAN接口的基本配置信息。

\<Sysname\> display ip interface vlan-interface brief

\*down: administratively down

(s): spoofing  (l): loopback

Interface                Physical Protocol IP Address      Description

Vlan10                   down     down     6.6.6.1         Link to CoreRo\...

Vlan2                    down     down     7.7.7.1         \--

\<Sysname\> display ip interface vlan-interface brief description

\*down: administratively down

(s): spoofing  (l): loopback

Interface                Physical Protocol IP Address      Description

Vlan10                   down     down     6.6.6.1         Link to CoreRouter

Vlan2                    down     down     7.7.7.1         \--

表1-2 display ip interface brief命令显示信息描述表

字段

描述

\*down: administratively down

接口处于管理down状态，即采用**shutdown**命令关闭了该接口

(s) : spoofing

接口的欺骗属性，即接口的链路层协议状态显示是up的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立的

Interface

接口的名称

Physical

接口的物理状态，可能的状态及含义如下：

·\*down：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·down：该接口的管理状态为开启，但物理状态为关闭（可能因为没有连接好或者线路故障）

·up：该接口的管理状态和物理状态均为开启

Protocol

接口的链路层协议状态，可能的状态及含义如下：

·down：该接口的协议状态为关闭

·down(l)：该接口的协议状态为loopback down

·up：该接口的协议状态为开启

·up(l)：该接口的协议状态为loopback up

·up(s)：该接口的协议状态为spoofing up

IP Address

接口的IP地址（如果未配置则显示"\--"）

Description

接口的描述信息（如果未配置则显示"\--"）

【相关命令】

·**display** **ip** **interface**

·**ip** **address**

**IP地址 \-- IP地址配置命令 \-- ip address**

------------------------------------------------------------------------

**[ip** **address**]命令用来配置接口的IP地址。

**[undo** **ip** **address**]命令用来删除接口的IP地址。

【命令】

**[ip**[ **address** *ip-address* { *mask-length* \| *mask* } [ **sub** ]]]

**[undo**[ **ip** **address** [ *ip-address* { *mask-length \| mask* } [ **sub** ] ]]]

【缺省情况】

没有为接口配置IP地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：接口的IP地址，为点分十进制格式。

*[mask-length*]：子网掩码长度，即掩码中连续"1"的个数，取值范围为1～31，当接口为LoopBack接口时，取值范围为1～32。

*[mask*]：接口IP地址相应的子网掩码，为点分十进制格式。

**[sub**]：表示该地址为接口的从IP地址。为了实现一个接口下的多个子网之间能够通信，需要在接口上配置从IP地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

**[ip** **address**]命令用来配置接口的IP地址。设备的每个接口可以配置多个IP地址，其中一个为主IP地址，其余为从IP地址。一般情况下，一个接口只需配置一个主IP地址，有时为了实现一个接口下的多个子网之间能够通信，需要在接口上配置从IP地址。

当配置主IP地址时，如果接口上已经有主IP地址，则新配置的地址将覆盖原有的主IP地址，成为新的主IP地址。

当接口被配置为通过BOOTP或DHCP动态获取、通过PPP协商分配或借用其他接口的IP地址后，不能再给该接口配置从IP地址。

**[undo** **ip** **address**]命令中不指定任何参数表示删除该接口的所有IP地址。**undo**[ **ip** **address** *ip-address* { *mask* \| *mask-length* }]表示删除主IP地址。**undo**[ **ip** **address** *ip-address* { *mask* \| *mask-length* } **sub**]表示删除指定的从IP地址。在单独删除主IP地址前必须先删除对应的所有从IP地址。

同一接口的主、从IP地址可以在同一网段，但不同接口之间、主接口及其子接口之间、同一主接口下不同子接口之间的IP地址不可以在同一网段。

【举例】

·路由应用

\# 为接口GigabitEthernet1/0/1配置主IP地址为129.102.0.1，从IP地址为202.38.160.1，子网掩码都为255.255.255.0。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-Ethernet1/1 ip address 129.102.0.1 255.255.255.0

Sysname-Ethernet1/1 ip address 202.38.160.1 255.255.255.0 sub

·交换应用

\# 指定VLAN接口10的主IP地址为129.12.0.1，从IP地址为202.38.160.1，子网掩码都为255.255.255.0。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ip address 129.12.0.1 255.255.255.0

Sysname-Vlan-interface10 ip address 202.38.160.1 255.255.255.0 sub

【相关命令】

·**display** **ip** **interface**

·**display** **ip** **interface** **brief**

**IP地址 \-- IP地址配置命令 \-- ip address unnumbered**

------------------------------------------------------------------------

![说明](IP地址命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ip** **address** **unnumbered**]命令用来配置本接口借用指定接口的IP地址。

**[undo** **ip** **address** **unnumbered**]命令用来取消借用其它接口的IP地址。

【命令】

**[ip** **address** **unnumbered** **interface** *interface-type interface-number*]

**[undo** **ip** **address** **unnumbered**]

【缺省情况】

不借用其它接口的IP地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：被借用接口的接口类型及接口编号。

【使用指导】

所谓"IP地址借用"，是指一个接口上没有配置IP地址，但为了使该接口能正常使用，就向同一设备上其它有IP地址的接口借用一个IP地址。

IP地址借用的使用场景如下：

·在IP地址资源比较匮乏的环境下，为了节约IP地址资源，可以配置某个接口借用其他接口的IP地址。

·如果某个接口只是偶尔使用，可以配置该接口借用其他接口的IP地址，而不必让其一直占用一个单独的IP地址。

Loopback接口的IP地址可被其它接口借用，但本身不能借用其它接口的地址。

一个接口的地址可以借给多个接口。如果被借用接口有多个手动配置的IP地址，则只有手动配置的主IP地址能被借用。

由于借用方接口本身没有IP地址，无法在此接口上启用动态路由协议。所以必须手动配置一条到对端网段的静态路由，才能实现设备间的连通。

【举例】

·路由应用

\# 配置Tunnel接口Tunnel0借用以太网接口GigabitEthernet1/0/1的IP地址。

\<Sysname\> system-view

Sysname interface tunnel 0 mode gre

Sysname-Tunnel0 ip address unnumbered interface gigabitethernet 1/0/1

·交换应用

\# 配置POS接口POS2/1/1借用VLAN接口100的IP地址。

\<Sysname\> system-view

Sysname interface pos 2/1/1

Sysname-Pos2/1/1 ip address unnumbered interface vlan-interface 100
