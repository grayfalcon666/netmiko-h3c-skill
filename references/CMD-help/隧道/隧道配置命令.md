<!-- CMD-INDEX
  bandwidth                           | Tunnel接口视图       | L24
  default                             | Tunnel接口视图       | L70
  description                         | Tunnel接口视图       | L106
  destination                         | Tunnel接口视图       | L158
  display ds-lite b4 information      | 任意视图             | L254
  display interface tunnel            | 任意视图             | L376
  ds-lite enable                      | 接口视图             | L756
  encapsulation-limit                 | Tunnel接口视图       | L812
  interface tunnel                    | 系统视图             | L868
  mtu                                 | Tunnel接口视图       | L966
  reset counters interface            | 用户视图             | L1018
  service                             |                  | L1062
  shutdown                            | Tunnel接口视图       | L1162
  source                              | Tunnel接口视图       | L1208
  tunnel dfbit enable                 | Tunnel接口视图       | L1304
  tunnel discard ipv4-compatible-packet | 系统视图             | L1348
  tunnel ipv6-fragmentation-check enable | 系统视图             | L1390
  tunnel tos                          | Tunnel接口视图       | L1434
  tunnel ttl                          | Tunnel接口视图       | L1484
  tunnel vpn-instance                 | Tunnel接口视图       | L1534
-->

**隧道 \-- 隧道配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的最大速率÷1000（kbit/s）。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值。具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 设置接口Tunnel1的期望带宽为100kbit/s。

\<Sysname\> system-view

Sysname interface tunnel 1

Sysname-Tunnel1 bandwidth 100

**隧道 \-- 隧道配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将接口Tunnel1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface tunnel 1

Sysname-Tunnel1 default

**隧道 \-- 隧道配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，如"Tunnel1 Interface"。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口的描述字符串，为1～255个字符的字符串，区分大小写。

【使用指导】

当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。

本命令仅用于标识某接口，并无特别的功能。使用**display interface**等命令可以看到设置的描述信息。

【举例】

\# 设置Tunnel1接口的描述信息为"tunnel1"。

\<Sysname\> system-view

Sysname interface tunnel 1

Sysname-Tunnel1 description tunnel1

【相关命令】

·**display interface tunnel**

**隧道 \-- 隧道配置命令 \-- destination**

------------------------------------------------------------------------

**[destination**]命令用来设置隧道的目的端地址。

**[undo destination**]命令用来删除设置的目的端地址。

【命令】

**[destination**[ { *ip-address* \| *ipv6-address* }]]

**[undo destination**]

【缺省情况】

没有设置隧道的目的端地址。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：隧道的目的端IPv4地址。

*[ipv6-address*]：隧道的目的端IPv6地址。

【使用指导】

配置手动隧道时，需要通过本命令设置隧道的目的端地址；配置自动隧道时，无需设置隧道的目的端地址。

隧道的目的端地址是对端接收报文的接口的地址，该地址将作为封装后隧道报文的目的地址。

在本端设备上为隧道指定的目的端地址，应该与在对端设备上为该隧道指定的源端地址相同；在本端设备上为隧道指定的源端地址，应该与在对端设备上为该隧道指定的目的端地址相同。

【举例】

·路由应用

\# Sysname1上接口GigabitEthernet1/0/1的IP地址是193.101.1.1，Sysname2上接口GigabitEthernet1/0/1的IP地址是192.100.1.1。配置Sysname1的源端地址为193.101.1.1，目的端地址为192.100.1.1。

\<Sysname1\> system-view

Sysname1 interface tunnel 1 mode gre

Sysname1-Tunnel1 source 193.101.1.1

Sysname1-Tunnel1 destination 192.100.1.1

\# 配置Sysname2的源端地址为192.100.1.1，目的端地址为193.101.1.1。

\<Sysname2\> system-view

Sysname2 interface tunnel 1 mode gre

Sysname2-Tunnel1 source 192.100.1.1

Sysname2-Tunnel1 destination 193.101.1.1

·交换应用

\# Sysname1上接口Vlan-int100的IP地址是193.101.1.1，Sysname2上接口Vlan-int100的IP地址是192.100.1.1。配置Sysname1的源端地址为193.101.1.1，目的端地址为192.100.1.1。

\<Sysname1\> system-view

Sysname1 interface tunnel 1 mode ipv6-ipv4

Sysname1-Tunnel1 source 193.101.1.1

Sysname1-Tunnel1 destination 192.100.1.1

\# 配置Sysname2的源端地址为192.100.1.1，目的端地址为193.101.1.1。

\<Sysname2\> system-view

Sysname2 interface tunnel 1 mode ipv6-ipv4

Sysname2-Tunnel1 source 192.100.1.1

Sysname2-Tunnel1 destination 193.101.1.1

【相关命令】

·**display interface tunnel**

·**interface tunnel**

·**source**

**隧道 \-- 隧道配置命令 \-- display ds-lite b4 information**

------------------------------------------------------------------------

**[display ds-lite b4 information**]命令用来在AFTR端显示已连接的B4设备的信息，包括B4设备的IPv6地址与Tunnel ID的映射关系等。

【命令】

**[display ds-lite b4 information**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示已连接的B4设备的信息。（集中式设备）

\<Sysname\> display ds-lite b4 information

 B4 address                                     Tunnel ID  Tunnel interface  Idle time

 1234:5678:1234:5678:abcd:abcd:efff:1234  0x00000023          1           12

 2000::100:1                                    0x80000013          2           13

 3000::2                                         0x00000015          3           8

 3001::2                                         0x00000032          \--          15

\# 显示已连接的B4设备的信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display ds-lite b4 information

Slot 0 Cpu 0:

 B4 address                                     Tunnel ID  Tunnel interface  Idle time

 1234:5678:1234:5678:abcd:abcd:efff:1234  0x00000023          1           12

 2000::100:1                                    0x80000013          2           13

 3000::2                                         0x00000015          3           2

 3001::2                                         0x00000032          \--          \--

Slot 1 Cpu 0:

 B4 address                                     Tunnel ID  Tunnel interface  Idle time

 1234:5678:1234:5678:abcd:abcd:efff:ffff  0x00000125          1           12

 5000::100:1                                    0x80000010          5           13

\# 显示已连接的B4设备的信息。（分布式设备－IRF模式）

\<Sysname\> display ds-lite b4 information

Chassis 1 Slot 0 Cpu0:

 B4 address                                     Tunnel ID  Tunnel interface  Idle time

 1234:5678:1234:5678:abcd:abcd:efff:1234  0x00000023          1           12

 2000::100:1                                    0x80000013          2           13

 3000::2                                         0x00000015          3           2

 3001::2                                         0x00000032          \--          \--

Chassis 1 Slot 1 Cpu0:

 B4 address                                     Tunnel ID  Tunnel interface  Idle time

 1234:5678:1234:5678:abcd:abcd:efff:ffff  0x00000125          1           12

 5000::100:1                                    0x80000010          5           13

表1-1 display ds-lite b4 information命令显示信息描述表

字段

描述

Slot 0 Cpu0

指定单板指定CPU上的信息

Chassis 1 Slot 0 Cpu0

指定成员设备指定单板指定CPU上的信息

B4 address

B4设备的IPv6地址

Tunnel ID

B4设备IPv6地址对应的Tunnel ID

Tunnel interface

映射关系所属的DS-Lite隧道接口编号

当映射关系所属的隧道被删除或者删除后创建编号相同但模式不同的隧道时，本字段显示为"\--"

Idle time

Tunnel ID与B4设备IPv6地址映射关系的剩余有效时间，单位为分钟

当映射关系老化时间已到，但仍有会话引用该映射关系时，本字段显示为"\--"

**隧道 \-- 隧道配置命令 \-- display interface tunnel**

------------------------------------------------------------------------

**[display interface tunnel**]命令用来显示Tunnel接口的相关信息，包括源端地址、目的端地址、隧道模式等。

【命令】

**[display interface** [ **tunnel** [ *number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[number*]：显示指定Tunnel接口的信息。*number*表示Tunnel接口编号，取值为已创建的Tunnel接口的编号。

**[brief**]：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**tunnel**参数，将显示设备支持的所有接口的相关信息。

·如果指定**tunnel**参数，不指定*number*参数，将显示所有已创建的Tunnel接口的相关信息。

【举例】

\# 显示接口Tunnel1的详细信息。

\<Sysname\> display interface tunnel 1

Tunnel1

Current state: UP

Line protocol state: UP

Description: Tunnel1 Interface

Bandwidth: 64kbps

Maximum Transmit Unit: 1476

Internet Address is 10.1.2.1/24 Primary

Tunnel source 2002::1:1 (Vlan-interface10), destination 2001::2:1

Tunnel keepalive enabled, Period(50 s), Retries(3)

Tunnel TOS 0xC8, Tunnel TTL 255

Tunnel protocol/transport GRE/IPv6

    GRE key value is 1

    Checksumming of GRE packets disabled

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

表1-2 display interface tunnel命令显示信息描述表

字段

描述

Tunnel1

接口Tunnel1的相关信息

Current state

Tunnel接口的物理状态和管理状态，可能的取值及含义如下：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭

·DOWN ( Tunnel-Bundle administratively down )：表示该接口所属的Tunnel-Bundle接口已经通过**shutdown**命令被关闭

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

Tunnel接口的链路层协议状态。其值由链路层经过参数协商决定，取值为：

·UP：表示该接口的链路层协议状态为开启

·UP (spoofing)：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常NULL、LoopBack等接口会具有该属性

·DOWN：表示该接口的链路层协议状态为关闭

Description

Tunnel接口的描述信息

Bandwidth

Tunnel接口的期望带宽

Maximum Transmit Unit

Tunnel接口的最大传输单元

Internet Address

Tunnel接口的IP地址。如果没有为Tunnel接口配置IP地址，则该字段显示为Internet protocol processing: disabled，表示不能处理IP报文

Primary表示该IP地址为接口的主IP地址

Tunnel source

隧道的源端地址和源接口。如果为Tunnel接口配置的是隧道的源端地址，则该字段只显示源端地址

destination

隧道的目的端地址

Tunnel keepalive enabled, Period(50 s), Retries(3)

启用隧道的keepalive功能，本例中keepalive报文的发送周期为50秒，最大发送次数为3

如果没有启用隧道的keepalive功能，则显示为Tunnel keepalive disabled

Tunnel TOS

封装后隧道报文的ToS值

Tunnel TTL

封装后隧道报文的TTL值

Tunnel protocol/transport

隧道模式和传输协议，可能取值为：

·CR_LSP：表示MPLS TE隧道模式

·DSLITE：表示AFTR端的IPv4 over IPv6 DS-Lite隧道模式

·GRE/IP：表示GRE over IPv4隧道模式

·GRE/IPv6：表示GRE over IPv6隧道模式

·GRE_ADVPN/IP：表示GRE封装的IPv4 ADVPN隧道模式

·GRE_ADVPN/IPv6：表示GRE封装的IPv6 ADVPN隧道模式

·GRE_EVI/IP：表示GRE封装的IPv4 EVI隧道模式

·GRE_EVI/IPv6：表示GRE封装的IPv6 EVI隧道模式

·IP/IP：表示IPv4 over IPv4隧道模式

·IP/IPv6：表示IPv4 over IPv6隧道模式

·IPv6：表示IPv6隧道模式

·IPv6/IP：表示IPv6 over IPv4手动隧道模式

·IPv6/IP 6to4：表示IPv6 over IPv4 6to4隧道模式

·IPv6/IP auto-tunnel：表示IPv6 over IPv4自动隧道模式

·IPv6/IP ISATAP：表示IPv6 over IPv4 ISATAP隧道模式

·IPv6/IPv6：表示IPv6 over IPv6隧道模式

·UDP_ADVPN/IP：表示UDP封装的IPv4 ADVPN隧道模式

·UDP_ADVPN/IPv6：表示UDP封装的IPv6 ADVPN隧道模式

·UDP_VXLAN/IP：表示UDP封装的IPv4 VXLAN隧道模式

·NVE/IP：表示IPv4 NVE隧道模式

GRE key value is 1

GRE类型隧道接口的密钥为1

如果没有设置GRE类型隧道接口的密钥，则显示为GRE key disabled

Checksumming of GRE packets disabled

未使能GRE报文校验和功能

如果使能了GRE报文校验和功能，则显示为Checksumming of GRE packets enabled

Source port number is 18001

UDP封装的ADVPN类型隧道接口发送ADVPN报文使用的源端口号

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

输出队列的紧急队列中当前的消息数/最大可容纳的消息数/已丢弃的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

输出队列的协议队列中当前的消息数/最大可容纳的消息数/已丢弃的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

输出队列的先进先出队列中当前的消息数/最大可容纳的消息数/已丢弃的消息数。该显示信息与用户的配置有关，当配置为CBQ、WFQ等队列时则显示为CBQ/WFQ等队列的消息数。该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Last clearing of counters

最近一次清除计数的时间

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输入速率：

·bytes/sec表示平均每秒输入的字节数

·bits/sec表示平均每秒输入的比特数

·packets/sec表示平均每秒输入的包数

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输出速率：

·bytes/sec表示平均每秒输出的字节数

·bits/sec表示平均每秒输出的比特数

·packets/sec表示平均每秒输出的包数

Input: 0 packets, 0 bytes, 0 drops

总计输入的报文数, 总计输入的字节，总计丢弃的输入报文数

Output: 0 packets, 0 bytes, 0 drops

总计输出的报文数, 总计输出的字节，总计丢弃的输出报文数

\# 显示接口Tunnel1的概要信息。

\<Sysname\> display interface tunnel 1 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Tun1                  UP    UP       1.1.1.1          aaaaaaaaaaaaaaaaaaaaaaaaaaa

\# 显示接口Tunnel1的概要信息，包括用户配置的全部描述信息。

\<Sysname\> display interface tunnel 1 brief description

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Tun1                  UP    UP       1.1.1.1          aaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

\# 显示当前物理状态为down的接口的信息以及down的原因。

\<Sysname\> display interface tunnel brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Tun0                  DOWN Not connected

Tun1                  DOWN Not connected

表1-3 display interface tunnel brief命令显示信息描述表

字段

描述

Brief information on interface(s) under route mode

三层模式下（route）的接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"字符串，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LopBack等接口会具有该属性

Interface

接口名称缩写

Link

接口物理连接状态，取值为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准

Protocol

接口数据链路层协议状态，取值为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LoopBack等接口会取该值

Main IP

接口主IP地址

Description

接口的描述信息

Cause

接口物理连接状态为down的原因，取值为：

·Administratively：表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

·Not connected：表示未成功建立隧道

·DOWN ( Tunnel-Bundle administratively down )：表示隧道接口所属的Tunnel-Bundle接口被手工关闭了

【相关命令】

·**destination**

·**interface tunnel**

·**source**

**隧道 \-- 隧道配置命令 \-- ds-lite enable**

------------------------------------------------------------------------

**[ds-lite enable**]命令用来使能接口的DS-Lite隧道功能。

**[undo ds-lite enable**]命令用来关闭接口的DS-Lite隧道功能。

【命令】

**[ds-lite enable**]

**[undo ds-lite enable**]

【缺省情况】

接口的DS-Lite隧道功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在AFTR连接IPv4公网的接口上需要通过本命令使能DS-Lite隧道功能。只有使能该功能后，AFTR从公网接口接收到的IPv4报文才能够通过DS-Lite隧道正确地转发到B4设备。

不能在**ds-lite-aftr**模式的隧道接口上使能DS-Lite隧道功能。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上使能DS-Lite隧道功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ds-lite enable

·交换应用

\# 在接口Vlan-interface10上使能DS-Lite隧道功能。

\<Sysname1\> system-view

Sysname1 interface vlan-interface 10

Sysname1-Vlan-interface10 ds-lite enable

**隧道 \-- 隧道配置命令 \-- encapsulation-limit**

------------------------------------------------------------------------

![说明](隧道命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[encapsulation-limit**]命令用来设置隧道允许的最大嵌套封装次数。

**[undo encapsulation-limit**]用来恢复缺省情况。

【命令】

**[encapsulation-limit** *number*]

**[undo encapsulation-limit**]

【缺省情况】

不限制隧道的最大嵌套封装次数。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：隧道的最大嵌套封装次数，取值范围为0～10。

【使用指导】

对报文进行过多次的封装，在报文上增加过多的报文头，会造成报文过大。如果报文的大小超过了MTU值，则需要对报文进行分片处理，这会降低报文的转发速度，增加报文处理的复杂度。通过本命令可以限制报文被封装的次数，避免上述情况发生。

本命令只用于IPv6 over IPv6隧道。

【举例】

\# 设置隧道允许的最大嵌套封装次数为3。

\<Sysname\> system-view

Sysname interface tunnel 1 mode ipv6

Sysname-Tunnel1 encapsulation-limit 3

【相关命令】

·**display interface tunnel**

**隧道 \-- 隧道配置命令 \-- interface tunnel**

------------------------------------------------------------------------

**[interface tunnel**]命令用来创建一个Tunnel接口，指定隧道模式，并进入该Tunnel接口视图。

**[undo interface tunnel**]命令用来删除指定的Tunnel接口。

【命令】

**[interface tunnel*** number *[[ **mode** { **advpn** { **gre** \| **udp** } [ **ipv6** ] \| **ds-lite-aftr** \| **evi**  **ipv6**  \| **gre**  **ipv6**  \| **ipv4-ipv4** \| **ipv4-ipv6** \| **ipv6** \| **ipv6-ipv4** [ **6to4** \| **auto-tunnel** \| **isatap** ] \| **ipv6-ipv6** \| **mpls-te** \| **nve** \| **nvgre** \| **vxlan** } ]]]

**[undo interface tunnel*** number*]

【缺省情况】

设备上不存在任何Tunnel接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：Tunnel接口编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但实际可创建的Tunnel接口数目将受到接口总数及内存状况的限制。

**[mode advpn gre**]：指定隧道模式为GRE封装的IPv4 ADVPN隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode advpn udp**]：指定隧道模式为UDP封装的IPv4 ADVPN隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode advpn gre ipv6**]：指定隧道模式为GRE封装的IPv6 ADVPN隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode advpn udp ipv6**]：指定隧道模式为UDP封装的IPv6 ADVPN隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **ds-lite-aftr**]：指定隧道模式为AFTR端的DS-Lite隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **evi**]：指定隧道模式为IPv4 EVI隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **evi ipv6**]：指定隧道模式为IPv6 EVI隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **gre**]：指定隧道模式为GRE over IPv4隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **gre ipv6**]：指定隧道模式为GRE over IPv6隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **ipv4-ipv4**]：指定隧道模式为IPv4 over IPv4隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode ipv4 over ipv6**]：指定隧道模式为IPv4 over IPv6隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **ipv6**]：指定隧道模式为IPv6隧道。配置IPv4 over IPv6手动隧道、IPv6 over IPv6隧道时，需要将隧道模式指定为IPv6隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **ipv6-ipv4**]：指定隧道模式为IPv6 over IPv4手动隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode ipv6-ipv4 6to4**]：指定隧道模式为6to4隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode ipv6-ipv4 auto-tunnel**]：指定隧道模式为IPv4兼容IPv6自动隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode ipv6-ipv4 isatap**]：指定隧道模式为ISATAP隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode ipv6 over ipv6**]：指定隧道模式为IPv6 over IPv6隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode** **mpls-te**]：指定隧道模式为MPLS TE隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode nve**]：指定隧道模式为NVE（Network Virtualization Endpoint，网络虚拟端点）隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode nvgre**]：指定隧道模式为NVGRE隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode vxlan**]：指定隧道模式为VXLAN隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·通过本命令创建Tunnel接口时，必须携带**mode**关键字，指定隧道模式。通过本命令进入已经创建的Tunnel接口视图时，不需要携带**mode**关键字。

·Tunnel接口编号只具有本地意义，隧道两端可以使用相同或不同的接口编号。

【举例】

\# 创建接口Tunnel1，指定隧道模式为GRE over IPv4隧道，并进入Tunnel接口视图。

\<Sysname\> system-view

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1

【相关命令】

·**destination**

·**display interface tunnel**

·**source**

**隧道 \-- 隧道配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来设置Tunnel接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

隧道接口的状态始终为Down时，本命令的缺省情况与设备的型号有关，请以设备的实际情况为准；隧道接口的状态当前为Up时，隧道的MTU值为根据隧道目的地址查找路由而得到的出接口的MTU值减隧道封装报文头长度。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：Tunnel接口的MTU值，取值范围为100～64000，单位为字节。

【使用指导】

如果没有手工配置隧道的MTU，则只有在隧道接口状态为Up时才会根据出接口的MTU计算、更新隧道的MTU，而在Down状态不会计算、更新。隧道的MTU被手工配置后，其值不受隧道接口状态和出接口MTU的影响，以手工配置为准。

为了防止隧道封装后的报文二次分片，手工配置隧道的MTU时，建议隧道的MTU与封装报文头长度之和不大于出接口的MTU。

【举例】

\# 设置接口Tunnel1的MTU值为10000字节。

\<Sysname\> system-view

Sysname interface tunnel 1

Sysname-Tunnel1 mtu 10000

【相关命令】

·**display interface tunnel**

**隧道 \-- 隧道配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除Tunnel接口的统计信息。

【命令】

**[reset counters interface** [ **tunnel** [ *number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：Tunnel接口编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

如果需要统计一定时间内Tunnel接口的流量来判断接口和链路工作是否正常，可以使用该命令先清除接口原有的统计信息，然后让接口自动重新统计。

·如果不指定**tunnel**和*number*，则清除所有接口的统计信息；

·如果指定**tunnel**而不指定*number*，则清除所有Tunnel接口的统计信息；

·如果同时指定**tunnel**和*number*，则清除指定Tunnel接口的统计信息。

【举例】

\# 清除接口Tunnel1的统计信息。

\<Sysname\> reset counters interface tunnel 1

【相关命令】

·**display interface tunnel**

**隧道 \-- 隧道配置命令 \-- service**

------------------------------------------------------------------------

![说明](隧道命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[service**]命令用来指定转发当前接口流量的业务处理板。

**[undo service**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[service slot*** slot-number*]

**[undo service slot**]

分布式设备－IRF模式：

**[service chassis ***chassis-number*** slot*** slot-number*]

**[undo service chassis**]

【缺省情况】

没有指定转发当前接口流量的业务处理板。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：指定单板所在的槽位号。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：指定设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：指定成员编号或PEX虚拟槽位号。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

没有通过**service**命令指定转发当前接口流量的业务处理板时，直接在接收报文的单板/成员设备上进行业务处理。而某些业务（如IPsec抗重放检测）要求同一个Tunnel接口的流量必须在同一个单板/成员设备上进行处理，此时可以在Tunnel接口下通过**service**命令指定转发当前接口流量的业务处理板。

需要注意的是，如果拔出指定的转发流量业务板，即使隧道UP，流量也转发不通；如果重新插入指定的转发流量业务板，则流量可以恢复在指定板正常转发。

【举例】

\# 指定2号单板转发Tunnel 200的流量。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname interface tunnel 200

Sysname-Tunnel200 service slot 2

\# 指定2号成员设备转发Tunnel 200的流量。（集中式IRF设备）（不支持IRF3的设备）

\<Sysname\> system-view

Sysname interface tunnel 200

Sysname-Tunnel200 service slot 2

\# 指定虚拟槽位为120的PEX设备转发Tunnel 200的流量。（集中式IRF设备）（支持IRF3的设备）

\<Sysname\> system-view

Sysname interface tunnel 200

Sysname-Tunnel200 service slot 120

\# 指定2号成员设备的2号单板转发Tunnel 200的流量。（分布式设备－IRF模式）（不支持IRF3的设备）

\<Sysname\> system-view

Sysname interface tunnel 200

Sysname-Tunnel200 service chassis2 slot 2

\# 指定虚拟框为20槽位为120的PEX设备转发Tunnel 200的流量。（分布式设备－IRF模式）（支持IRF3的设备）

\<Sysname\> system-view

Sysname interface tunnel 200

Sysname-Tunnel200 service chassis 20 slot 120

**隧道 \-- 隧道配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭Tunnel接口。

**[undo** **shutdown**]命令用来打开Tunnel接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**shutdown**命令会导致使用该接口建立的链路中断，请谨慎使用。

【举例】

\# 关闭接口Tunnel 1。

\<Sysname\> system-view

Sysname interface tunnel 1

Sysname-Tunnel1 shutdown

【相关命令】

·**display interface tunnel**

**隧道 \-- 隧道配置命令 \-- source**

------------------------------------------------------------------------

**[source**]命令用来设置隧道的源端地址或源接口。

**[undo source**]命令用来恢复缺省情况。

【命令】

**[source**[ { *ip-address* \| *ipv6-address* \| *interface-type interface-number* }]]

**[undo source**]

【缺省情况】

没有设置隧道的源端地址和源接口。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：隧道的源端IPv4地址。

*[ipv6-address*]：隧道的源端IPv6地址。

*[interface-type interface-number*]：隧道的源接口的接口类型及接口编号。

【使用指导】

如果设置的是隧道的源端地址，则该地址将作为封装后隧道报文的源地址；如果设置的是隧道的源接口，则该接口的地址将作为封装后隧道报文的源地址。通过**display interface tunnel**命令可以查看隧道的源端地址。

在本端设备上为隧道指定的目的端地址，应该与在对端设备上为该隧道指定的源端地址相同；在本端设备上为隧道指定的源端地址，应该与在对端设备上为该隧道指定的目的端地址相同。

需要注意的是：

·如果在同一个隧道接口下重复执行本命令指定源端地址或源接口，则新的配置会覆盖原有配置。

·指定的源接口需要是处于up状态、且已配置IP地址的接口。

·模式为AFTR端DS-Lite隧道的隧道接口不能指定为源接口。

【举例】

·路由应用

\# 配置接口Tunnel1的源接口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 source gigabitethernet 1/0/1

\# 配置接口Tunnel1的源IP地址为192.100.1.1。

\<Sysname\> system-view

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 source 192.100.1.1

·交换应用

\# 配置接口Tunnel1的源接口为Vlan-interface10。

\<Sysname\> system-view

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 source vlan-interface 10

\# 配置接口Tunnel1的源IP地址为192.100.1.1。

\<Sysname\> system-view

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 source 192.100.1.1

【相关命令】

·**destination**

·**display interface tunnel**

·**interface tunnel**

**隧道 \-- 隧道配置命令 \-- tunnel dfbit enable**

------------------------------------------------------------------------

**[tunnel dfbit enable**]命令用来设置封装后的隧道报文的DF（Don't Fragment，不分片）标志，即转发隧道报文时不允许分片。

**[undo tunnel dfbit enable**]命令用来恢复缺省情况。

【命令】

**[tunnel dfbit enable**]

**[undo** **tunnel dfbit enable**]

【缺省情况】

封装后的隧道报文未设置DF标志，即转发隧道报文时允许分片。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

转发报文时对报文进行分片、重组，可能会导致报文的转发延时较大。通过本命令设置封装后隧道报文的DF标志，不允许对隧道报文进行分片，可以避免引入分片延时。这种情况下，要求隧道报文转发路径上各个接口的MTU大于隧道报文长度，否则，会导致隧道报文被丢弃。如果无法保证转发路径上各个接口的MTU大于隧道报文长度，则建议不要设置DF标志。

模式为GRE over IPv6隧道和IPv6隧道的Tunnel接口不支持本命令。

【举例】

\# 在接口Tunnel1上设置封装后隧道报文的DF标志，不允许对隧道报文进行分片。

\<Sysname\> system-view

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 tunnel dfbit enable

**隧道 \-- 隧道配置命令 \-- tunnel discard ipv4-compatible-packet**

------------------------------------------------------------------------

![说明](隧道命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tunnel discard ipv4-compatible-packet**]命令用来配置丢弃含有IPv4兼容IPv6地址的IPv6报文。**undo tunnel discard ipv4-compatible-packet**命令用来恢复缺省情况。

【命令】

**[tunnel discard ipv4-compatible-packet**]

**[undo tunnel discard ipv4-compatible-packet**]

【缺省情况】

不会丢弃含有IPv4兼容IPv6地址的IPv6报文。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**tunnel discard ipv4-compatible-packet**命令后，对于从隧道接收的报文，如果解封装后原始IPv6报文的源或目的地址为IPv4兼容IPv6地址，则丢弃该报文。

【举例】

\# 配置丢弃含有IPv4兼容IPv6地址的IPv6报文。

\<Sysname\> system-view

Sysname tunnel discard ipv4-compatible-packet

**隧道 \-- 隧道配置命令 \-- tunnel ipv6-fragmentation-check enable**

------------------------------------------------------------------------

![说明](隧道命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tunnel ipv6-fragmentation-check enable**]命令用来使能隧道报文的分片检查功能。

**[undo tunnel ipv6-fragmentation-check enable**]命令用来关闭隧道报文的分片检查功能。

【命令】

**[tunnel ipv6-fragmentation-check enable**]

**[undo tunnel ipv6-fragmentation-check enable**]

【缺省情况】

隧道报文的分片检查功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行本命令后，对于将要通过IPv6 over IPv4隧道转发的报文，会在进行隧道封装前对IPv6报文进行分片检查。如果IPv6报文的大小超过了隧道出接口的MTU减去IPv4报文头长度的差值和IPv6要求的链路层所支持的最小MTU值（1280字节），则隧道向IPv6报文源发送报文过大的ICMP消息并丢弃该报文。

【举例】

\# 使能隧道报文的分片检查功能。

\<Sysname\> system-view

Sysname tunnel ipv6-fragmentation-check enable

**隧道 \-- 隧道配置命令 \-- tunnel tos**

------------------------------------------------------------------------

**[tunnel tos**]命令用来设置封装后隧道报文的ToS（Type of Service，服务类型）值。

**[undo tunnel tos**]命令用来恢复缺省情况。

【命令】

**[tunnel tos** *tos-value*]

**[undo** **tunnel tos**]

【缺省情况】

封装后隧道报文的ToS值与封装前原始报文的ToS值相同。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tos-value*]：封装后隧道报文的ToS值，取值范围为0～255。

【使用指导】

ToS值用于标识IP报文的服务类型。通过本命令设置封装后隧道报文的ToS值后，同一个隧道中转发的报文将具有相同的ToS值，即报文的业务类型都相同。关于ToS的详细介绍请参见"ACL和QoS配置指导"中的"QoS"。

【举例】

\# 在接口Tunnel1上设置封装后隧道报文的ToS值为20。

\<Sysname\> system-view

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 tunnel tos 20

【相关命令】

·**display interface tunnel**

**隧道 \-- 隧道配置命令 \-- tunnel ttl**

------------------------------------------------------------------------

**[tunnel ttl**]命令用来设置封装后隧道报文的TTL（Time to Live，生存时间）值，从而决定隧道报文的最大跳数。

**[undo tunnel ttl**]命令用来恢复缺省情况。

【命令】

**[tunnel ttl** *ttl-value*]

**[undo** **tunnel ttl**]

【缺省情况】

封装后隧道报文的TTL值为255。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ttl-value*]：封装后隧道报文的TTL值，取值范围为1～255。

【使用指导】

设置封装后隧道报文的TTL值用来限制报文在隧道中转发的最大跳数。当报文转发跳数大于设置的TTL值时，该隧道报文将被丢弃，以避免出现环路。

【举例】

\# 在接口Tunnel1上设置封装后隧道报文的TTL值为100。

\<Sysname\> system-view

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 tunnel ttl 100

【相关命令】

·**display interface tunnel**

**隧道 \-- 隧道配置命令 \-- tunnel vpn-instance**

------------------------------------------------------------------------

**[tunnel vpn-instance**]命令用来配置隧道目的端地址所属的VPN。

**[undo tunnel vpn-instance**]命令用来恢复缺省情况。

【命令】

**[tunnel vpn-instance **]*vpn-instance-name*

**[undo**] **tunnel vpn-instance**

【缺省情况】

隧道目的端地址属于公网，设备查找公网路由表转发隧道封装后的报文。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

通过本命令指定隧道目的端地址所属的VPN后，设备将查找指定VPN实例的路由表转发隧道封装后的报文。

在隧道的源接口上通过**ip binding vpn-instance**命令可以指定隧道源端地址所属的VPN。隧道的源端地址和目的端地址必须属于相同的VPN，否则隧道接口链路状态无法UP。

【举例】

·路由应用

\# 在接口Tunnel1上指定封装后的隧道报文在vpn10中进行路由发送。

\<Sysname\> system-view

Sysname ip vpn-instance vpn10

Sysname-vpn-instance-vpn10 route-distinguisher 1:1

Sysname-vpn-instance-vpn10 vpn-target 1:1

Sysname-vpn-instance-vpn10 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip binding vpn-instance vpn10

Sysname-GigabitEthernet1/0/1 ip address 1.1.1.1 24

Sysname-GigabitEthernet1/0/1 quit

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 source gigabitethernet 1/0/1

Sysname-Tunnel1 destination 1.1.1.2

Sysname-Tunnel1 tunnel vpn-instance vpn10

·交换应用

\# 在接口Tunnel1上指定封装后的隧道报文在vpn10中进行路由发送。

\<Sysname\> system-view

Sysname ip vpn-instance vpn10

Sysname-vpn-instance-vpn10 route-distinguisher 1:1

Sysname-vpn-instance-vpn10 vpn-target 1:1

Sysname-vpn-instance-vpn10 quit

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ip binding vpn-instance vpn10

Sysname-Vlan-interface10 ip address 1.1.1.1 24

Sysname-Vlan-interface10 quit

Sysname interface tunnel 1 mode gre

Sysname-Tunnel1 source vlan-interface 10

Sysname-Tunnel1 destination 1.1.1.2

Sysname-Tunnel1 tunnel vpn-instance vpn10

【相关命令】

·**ip binding vpn-instance**（MPLS命令参考/MPLS L3VPN）
