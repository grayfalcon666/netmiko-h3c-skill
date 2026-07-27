<!-- CMD-INDEX
  display ipv6 fib                    | 任意视图             | L79
  display ipv6 icmp statistics        | 任意视图             | L207
  display ipv6 interface              | 任意视图             | L401
  display ipv6 interface prefix       | 任意视图             | L1141
  display ipv6 nd snooping            | 任意视图             | L1237
  display ipv6 nd snooping count      | 任意视图             | L1343
  display ipv6 nd suppression xconnect-group | 任意视图             | L1399
  display ipv6 neighbors              | 任意视图             | L1495
  display ipv6 neighbors count        | 任意视图             | L1647
  display ipv6 neighbors vpn-instance | 任意视图             | L1713
  display ipv6 pathmtu                | 任意视图             | L1805
  display ipv6 prefix                 | 任意视图             | L1899
  display ipv6 rawip                  | 任意视图             | L1991
  display ipv6 rawip verbose          | 任意视图             | L2095
  display ipv6 router-renumber statistics | 任意视图             | L2495
  display ipv6 statistics             | 任意视图             | L2649
  display ipv6 tcp                    | 任意视图             | L3047
  display ipv6 tcp-proxy              | 任意视图             | L3179
  display ipv6 tcp verbose            | 任意视图             | L3297
  display ipv6 udp                    | 任意视图             | L3793
  display ipv6 udp verbose            | 任意视图             | L3893
  ipv6 address                        | 接口视图             | L4291
  ipv6 address anycast                | 接口视图             | L4373
  ipv6 address auto                   | 接口视图             | L4449
  ipv6 address auto link-local        | 接口视图             | L4507
  ipv6 address eui-64                 | 接口视图             | L4573
  ipv6 address link-local             | 接口视图             | L4657
  ipv6 bandwidth-based-sharing        | 系统视图             | L4719
  ipv6 hop-limit                      | 系统视图             | L4761
  ipv6 hoplimit-expires enable        | 系统视图             | L4813
  ipv6 icmpv6 error-interval          | 系统视图             | L4857
  ipv6 icmpv6 multicast-echo-reply enable | 系统视图             | L4905
  ipv6 icmpv6 source                  | 系统视图             | L4947
  ipv6 mtu                            | 接口视图             | L4995
  ipv6 nd autoconfig managed-address-flag | 接口视图             | L5053
  ipv6 nd autoconfig other-flag       | 接口视图             | L5109
  ipv6 nd dad attempts                | 接口视图             | L5165
  ipv6 nd mode uni                    | VLAN接口视图         | L5229
  ipv6 nd ns retrans-timer            | 接口视图             | L5279
  ipv6 nd nud reachable-time          | 接口视图             | L5343
  ipv6 nd snooping enable global      | VLAN视图           | L5407
  ipv6 nd snooping enable link-local  | VLAN视图           | L5445
  ipv6 nd snooping glean source       | VLAN视图           | L5483
  ipv6 nd snooping max-learning-num   | 二层以太网接口视图/二层聚合接口视图 | L5527
  ipv6 nd ra halt                     | 接口视图             | L5565
  ipv6 nd ra hop-limit unspecified    | 接口视图             | L5615
  ipv6 nd ra interval                 | 接口视图             | L5673
  ipv6 nd ra no-advlinkmtu            | 接口视图             | L5739
  ipv6 nd ra prefix                   | 接口视图             | L5793
  ipv6 nd ra router-lifetime          | 接口视图             | L5881
  ipv6 nd route-direct advertise      | L3VE接口视图         | L5945
  ipv6 nd router-preference           | 接口视图             | L5983
  ipv6 nd suppression enable          | 交叉连接视图           | L6047
  ipv6 nd suppression push interval   | 系统视图             | L6095
  ipv6 neighbor                       | 系统视图             | L6143
  ipv6 neighbor link-local minimize   | 系统视图             | L6219
  ipv6 neighbor stale-aging           | 系统视图             | L6263
  ipv6 neighbors max-learning-num     | 二层接口视图/二层聚合接口视图/三层接口视图/三层聚合接口视图/S通道接口视图/S通道聚合接口视图/三层RPR逻辑接口视图 | L6309
  ipv6 pathmtu                        | 系统视图             | L6367
  ipv6 pathmtu age                    | 系统视图             | L6421
  ipv6 prefer temporary-address       | 系统视图             | L6471
  ipv6 prefix                         | 系统视图             | L6523
  ipv6 reassemble local enable        | 系统视图             | L6577
  ipv6 redirects enable               | 系统视图             | L6619
  ipv6 router-renumber enable         | 接口视图             | L6661
  ipv6 temporary-address              | 系统视图             | L6715
  ipv6 unreachables enable            | 系统视图             | L6789
  local-proxy-nd enable               | VLAN接口视图/三层以太网接口视图/三层以太网子接口视图 | L6837
  proxy-nd enable                     | VLAN接口视图/三层以太网接口视图/三层以太网子接口视图 | L6891
  reset ipv6 nd snooping              | 用户视图             | L6945
  reset ipv6 nd suppression xconnect-group | 用户视图             | L6971
  reset ipv6 neighbors                | 用户视图             | L7005
  reset ipv6 pathmtu                  | 用户视图             | L7089
  reset ipv6 router-renumber statistics | 用户视图             | L7127
  reset ipv6 statistics               | 用户视图             | L7161
-->

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 fib**

------------------------------------------------------------------------

**[display ipv6 fib**]命令用来显示IPv6 FIB信息。

【命令】

**[display ipv6 fib ** **vpn-instance** *vpn-instance-name* ]  *ipv6-address* [ *prefix-length*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的IPv6 FIB信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

*[ipv6-address*]：显示目的地址为指定IPv6地址的IPv6 FIB信息。

*[prefix-length*]：目的地址的前缀长度，取值范围为0～128。

【使用指导】

本命令可以用来查看IPv6 FIB信息，包括转发的目的地址、前缀长度、转发的下一跳地址、转发报文的出接口等内容。

需要注意的是：

·如果不指定**vpn-instance**参数，将显示公网的IPv6 FIB信息；如果指定**vpn-instance**参数，将显示指定VPN实例的IPv6 FIB信息。

·如果不指定前缀长度，将显示与指定目的IPv6地址最长匹配的IPv6 FIB信息；如果指定前缀长度时，将显示与指定目的IPv6地址和前缀长度精确匹配的IPv6 FIB信息。

·如果不指定任何参数，则显示公网所有的IPv6 FIB信息。

【举例】

\# 显示公网所有的IPv6 FIB信息。

\<Sysname\> display ipv6 fib

Destination count: 1 FIB entry count: 1

Flag:

  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static

  R:Relay     F:FRR

Destination: ::1                                            Prefix length: 128

Nexthop     : ::1                                            Flags: UH

Time stamp : 0x1                                            Label: Null

Interface  : InLoop0                                        Token: Invalid

表1-1 display ipv6 fib命令显示信息描述表

字段

描述

Destination count

目的地址的个数

FIB entry count

IPv6 FIB表项数目

Destination

转发的目的地址

Prefix length

转发的目的地址的前缀长度

Nexthop

向目的地址转发报文的下一跳地址

Flags

路由的标志：

·U：表示路由可用

·G：表示网关路由

·H：表示主机路由

·B：表示黑洞路由

·D：表示动态路由

·S：表示静态路由

·R：表示迭代路由

·F：表示快速重路由

Time stamp

IPv6 FIB表项的生成时间

Label

MPLS内层标签

Interface

转发报文的出接口

Token

LSP索引号

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 icmp statistics**

------------------------------------------------------------------------

**[display ipv6 icmp statistics**]命令用来显示ICMPv6流量统计信息。

【命令】

集中式设备：

**[display ipv6 icmp statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 icmp statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 icmp statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板的ICMPv6流量统计信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的ICMPv6流量统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的ICMPv6流量统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的ICMPv6流量统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的ICMPv6流量统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的ICMPv6流量统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ICMPv6流量统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的ICMPv6流量统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ICMPv6流量统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的ICMPv6流量统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的ICMPv6流量统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以用来查看设备接收和发送的各类ICMPv6流量统计信息。

【举例】

\# 显示ICMPv6流量统计信息。

\<Sysname\> display ipv6 icmp statistics

  Input: bad code                0           too short                  0

         checksum error          0           bad length                 0

         path MTU changed        0          destination unreachable  0

         too big                  0           parameter problem         0

         echo request            0           echo reply                  0

         neighbor solicit        0           neighbor advertisement   0

         router solicit          0           router advertisement      0

         redirect                 0           router renumbering         0

 output: parameter problem     0           echo request                0

         echo reply               0           unreachable no route       0

         unreachable admin       0           unreachable beyond scope 0

         unreachable address    0           unreachable no port        0

         too big                   0           time exceed transit       0

         time exceed reassembly 0           redirect                    0

         ratelimited               0           other errors               0

表1-2 display ipv6 icmp statistics命令显示信息描述表

字段

描述

bad code

接收的代码错误的报文数

too short

接收的长度过小的报文数

checksum error

接收的校验和错误的报文数

bad length

接收的长度错误的报文数

path MTU changed

接收的路径MTU改变报文数

destination unreachable

接收的目标不可达报文数

too big

接收/发送的数据包超长报文数

parameter problem

接收/发送的参数错误报文数

echo request

接收/发送的回显请求报文数

echo reply

接收/发送的回应响应报文数

neighbor solicit

接收的邻居请求报文数

neighbor advertisement

接收的邻居通告报文数

router solicit

接收的路由请求报文数

router advertisement

接收的路由通告报文数

redirect

接收/发送的重定向报文数

router renumbering

接收的路由器重计数报文数

unreachable no route

发送的路由不可达报文数

unreachable admin

发送的与目标的通信被管理策略禁止的报文数

unreachable beyondscope

发送的源地址超出范围的报文数

unreachable address

发送的地址不可达报文数

unreachable no port

发送的端口不可达报文数

time exceed transit

发送的传输超时报文数

time exceed reassembly

发送的重组超时报文数

ratelimited

因速率超过限制而未发送的报文数

other errors

发送的其他的错误报文数

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 interface**

------------------------------------------------------------------------

**[display ipv6 interface**]命令用来显示接口的IPv6信息。

【命令】

**[display ipv6 interface** [ *interface-type* [ *interface-number*  ]  **brief** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type*]：显示指定类型接口的IPv6信息。

*[interface-number*]：显示指定接口的IPv6信息。

**[brief**]：显示接口摘要信息。

【使用指导】

如果配置命令时指定了**brief**关键字，则显示接口的摘要信息，包括接口的物理状态、链路层协议状态以及IPv6地址信息；否则，将显示接口的详细信息，包括接口上和IPv6相关的配置以及运行信息，以及IPv6报文统计信息。

需要注意的是：

·如果不指定接口类型和接口编号，则显示所有接口的IPv6信息；

·如果只指定接口类型，不指定接口编号，则显示所有指定类型接口的IPv6信息；

·如果同时指定接口类型和接口编号，则显示指定接口的IPv6信息。

【举例】

·路由应用

\# 查看接口GigabitEthernet1/0/1上的IPv6信息。

\<Sysname\> display ipv6 interface gigabitethernet 1/0/1

GigabitEthernet1/0/1 current state: UP

Line protocol current state: UP

IPv6 is enabled, link-local address is FE80::200:1FF:FE04:5D00 [TENTATIVE]

  Global unicast address(es):

    10::1234:56FF:FE65:4322, subnet is 10::/64 [TENTATIVE AUTOCFG]

      valid lifetime 4641s/preferred lifetime 4637s

    20::1234:56ff:fe65:4322, subnet is 20::/64 [TENTATIVE EUI-64]

    30::1, subnet is 30::/64 [TENTATIVE ANYCAST]

    40::2, subnet is 40::/64 [TENTATIVE DHCP]

    50::3, subnet is 50::/64 [TENTATIVE]

  Joined group address(es):

    FF02::1

    FF02::2

    FF02::1:FF00:1

    FF02::1:FF04:5D00

  MTU is 1500 bytes

  ND DAD is enabled, number of DAD attempts: 1

  ND reachable time is 30000 milliseconds

  ND retransmit interval is 1000 milliseconds

  Hosts use stateless autoconfig for addresses

IPv6 Packet statistics:

  InReceives:                       0

  InTooShorts:                      0

  InTruncatedPkts:                0

  InHopLimitExceeds:              0

  InBadHeaders:                    0

  InBadOptions:                    0

  ReasmReqds:                       0

  ReasmOKs:                     0

  InFragDrops:                      0

  InFragTimeouts:                  0

  OutFragFails:                    0

  InUnknownProtos:                 0

  InDelivers:                       0

  OutRequests:                      0

  OutForwDatagrams:               0

  InNoRoutes:                       0

  InTooBigErrors:                  0

  OutFragOKs:                       0

  OutFragCreates:                  0

  InMcastPkts:                      0

  InMcastNotMembers:              0

  OutMcastPkts:                    0

  InAddrErrors:                    0

  InDiscards:                       0

  OutDiscards:                      0

表1-3 display ipv6 interface命令显示信息描述表

字段

描述

GigabitEthernet1/0/1 current state

接口的物理状态，可能的状态及含义如下：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭（可能因为没有连接好或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Line protocol current state

接口的链路层协议状态，可能的状态及含义如下：

·DOWN：该接口的协议状态为关闭

·UP：该接口的协议状态为开启

IPv6 is enabled

接口的IPv6转发功能状态（为某接口配置任一IPv6地址后系统将自动使能该接口的IPv6功能，此例中处于使能状态）

link-local address

接口上配置的链路本地地址

Global unicast address(es)

接口上配置的全球单播地址

可能的IPv6地址状态及含义如下：

·TENTATIVE：该状态为地址初始化状态，此时该地址可能正在进行DAD检测或准备进行DAD检测，处于该状态的地址不能作为报文的源地址或者目的地址

·DUPLICATE：该状态表明地址DAD检测已经结束，由于该地址在链路上不唯一，因此不能使用

·PREFERRED：该状态表明地址处于首选生命期以内。该状态的地址可以作为报文的源地址或者目的地址。为该状态时，不显示地址的状态标识

·DEPRECATED：该状态表明地址超过首选生命期，但是在有效生命期以内。该状态地址有效，但不应作为新建连接报文的源地址，目的地址是该地址的报文还可以被正常处理

如果地址来源不为手工配置的全球单播地址，则会标记地址来源。可能的地址来源及含义如下：

·AUTOCFG：表示无状态自动配置的全球单播地址

·DHCP：表示DHCPv6服务器分配的全球单播地址

·EUI-64：表示手工配置的EUI-64格式全球单播地址

·RANDOM：表示自动生成的临时地址

如果地址为手工配置的任播地址，则会标记ANYCAST

valid lifetime

接口上无状态自动配置的全球单播地址的有效生命期

preferred lifetime

接口上无状态自动配置的全球单播地址的首选生命期

Joined group address(es)

接口加入的组播组地址

MTU

接口的最大传输单元

ND DAD is enabled, number of DAD attempts

重复地址检测功能是否使能（该例中使能）

若处于使能状态则同时显示重复地址检测时发送邻居请求消息的次数（可通过**ipv6 nd dad attempts**命令进行配置）

若处于关闭状态则显示"ND DAD is disabled"（可通过配置重复地址检测时发送邻居请求消息的次数为0关闭该功能）

ND reachable time

保持邻居可达的时间

ND retransmit interval

邻居请求消息重传时间间隔

Hosts use stateless autoconfig for addresses

主机采用无状态自动配置的方式获取IPv6地址

InReceives

接口接收到的所有IPv6报文，包括各种错误的报文

InTooShorts

接口接收到的太短的IPv6报文，譬如报文长度不足40字节

InTruncatedPkts

接口接收到的IPv6报文，其实际长度小于报文内容中所指出的报文长度

InHopLimitExceeds

接口接收到的IPv6报文，其跳数超出限制

InBadHeaders

接口接收到的IPv6报文，其基本报文头错误

InBadOptions

接口接收到的IPv6报文，其扩展报文头错误

ReasmReqds

接口接收到的IPv6分片报文

ReasmOKs

接口接收到的IPv6分片，被组装好的报文，这里指的不是分片个数，是组装好的报文数

InFragDrops

接口接收到的IPv6分片报文，该分片报文由于错误被丢弃

InFragTimeouts

接口接收到的IPv6分片报文，该分片停留在系统缓冲中时间超过指定时间，被丢弃

OutFragFails

出接口上分片失败的报文

InUnknownProtos

接口接收到的IPv6报文，其协议类型不能被识别或不能被支持

InDelivers

接口接收到的IPv6报文，该报文被上送到IPv6的用户协议处（如ICMPv6、TCP、UDP等）

OutRequests

IPv6本地出报文，即各IPv6的用户协议层要求IPv6发送出去的报文

OutForwDatagrams

出接口上被转发的报文

InNoRoutes

接口接收到的IPv6报文，找不到匹配的路由被丢弃

InTooBigErrors

接口接收到的IPv6报文，转发时，由于超过链路MTU被丢弃

OutFragOKs

出接口上分片成功的报文

OutFragCreates

出接口上成功分片后的分片报文，指分片数

InMcastPkts

接口接收到的IPv6组播报文

InMcastNotMembers

接口接收到的IPv6组播报文，但该接口却没有加入对应组播组，报文被丢弃

OutMcastPkts

接口发送的IPv6组播报文

InAddrErrors

接口接收到的IPv6报文，其目的地址不合法，报文被丢弃

InDiscards

接口接收到的IPv6报文，由于资源问题被丢弃的报文，而不是由于报文内容等被丢弃的报文

OutDiscards

接口需要发送的报文，由于资源问题被丢弃的报文，而不是由于报文内容等被丢弃的报文

\# 查看所有接口的IPv6摘要信息。

\<Sysname\> display ipv6 interface brief

\*down: administratively down

(s): spoofing

Interface                                 Physical Protocol IPv6 Address

GigabitEthernet1/0/1                    up        up         2001::1

GigabitEthernet1/0/2                    up        up         Unassigned

表1-4 display ipv6 interface brief命令显示信息描述表

字段

描述

\*down: administratively down

接口处于管理down状态，即采用shutdown命令关闭了该接口

(s): spoofing

接口的欺骗属性，即接口的链路协议状态显示是up的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立的

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

·up：该接口的协议状态为开启

IPv6 Address

接口的IPv6地址，接口上有全球单播地址时，显示地址最小的全球单播地址，没有全球单播地址则显示链路本地地址，没有链路本地地址则显示"Unassigned"

·交换应用

\# 查看VLAN接口2上的IPv6信息。

\<Sysname\> display ipv6 interface vlan-interface 2

Vlan-interface2 current state: UP

Line protocol current state: UP

IPv6 is enabled, link-local address is FE80::1234:56FF:FE65:4322 [TENTATIVE]

  Global unicast address(es):

    10::1234:56FF:FE65:4322, subnet is 10::/64 [TENTATIVE AUTOCFG]

      valid lifetime 4641s/preferred lifetime 4637s

    20::1234:56ff:fe65:4322, subnet is 20::/64 [TENTATIVE EUI-64]

    30::1, subnet is 30::/64 [TENTATIVE ANYCAST]

    40::2, subnet is 40::/64 [TENTATIVE DHCP]

    50::3, subnet is 50::/64 [TENTATIVE]

  Joined group address(es):

    FF02::1

    FF02::2

    FF02::1:FF00:1

    FF02::1:FF65:4322

  MTU is 1500 bytes

  ND DAD is enabled, number of DAD attempts: 1

  ND reachable time is 30000 milliseconds

  ND retransmit interval is 1000 milliseconds

  Hosts use stateless autoconfig for addresses

IPv6 Packet statistics:

  InReceives:                       0

  InTooShorts:                      0

  InTruncatedPkts:                0

  InHopLimitExceeds:              0

  InBadHeaders:                    0

  InBadOptions:                    0

  ReasmReqds:                       0

  ReasmOKs:                     0

  InFragDrops:                      0

  InFragTimeouts:                  0

  OutFragFails:                    0

  InUnknownProtos:                 0

  InDelivers:                       0

  OutRequests:                      0

  OutForwDatagrams:               0

  InNoRoutes:                       0

  InTooBigErrors:                  0

  OutFragOKs:                       0

  OutFragCreates:                  0

  InMcastPkts:                      0

  InMcastNotMembers:              0

  OutMcastPkts:                    0

  InAddrErrors:                    0

  InDiscards:                       0

  OutDiscards:                      0

表1-5 display ipv6 interface命令显示信息描述表

字段

描述

Vlan-interface2 current state

接口的物理状态，可能的状态及含义如下：

·Administratively DOWN：表示该VLAN接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该VLAN接口的管理状态为开启，但物理状态为关闭，即该接口对应的VLAN内没有处于UP状态的端口（可能因为没有连接好或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Line protocol current state

接口的链路层协议状态，可能的状态及含义如下：

·DOWN：该VLAN接口的协议状态为关闭

·UP：该VLAN接口的协议状态为开启

IPv6 is enabled

接口的IPv6转发功能状态（为某接口配置任一IPv6地址后系统将自动使能该接口的IPv6功能，此例中处于使能状态）

link-local address

接口上配置的链路本地地址

Global unicast address(es)

接口上配置的全球单播地址

可能的IPv6地址状态及含义如下：

·TENTATIVE：该状态为地址初始化状态，此时该地址可能正在进行DAD检测或准备进行DAD检测，处于该状态的地址不能作为报文的源地址或者目的地址

·DUPLICATE：该状态表明地址DAD检测已经结束，由于该地址在链路上不唯一，因此不能使用

·PREFERRED：该状态表明地址处于首选生命期以内。该状态的地址可以作为报文的源地址或者目的地址。为该状态时，不显示地址的状态标识

·DEPRECATED：该状态表明地址有效，但不应作为新建连接报文的源地址，目的地址是该地址的报文还需要被正常处理

如果地址来源不为手工配置的全球单播地址，则会标记地址来源。可能的地址来源及含义如下：

·AUTOCFG：表示无状态自动配置的全球单播地址

·DHCP：表示DHCPv6服务器分配的全球单播地址

·EUI-64：表示手工配置的EUI-64格式全球单播地址

·RANDOM：表示自动生成的临时地址

如果地址为手工配置的任播地址，则会标记ANYCAST

valid lifetime

接口上无状态自动配置的全球单播地址的有效生命期

preferred lifetime

接口上无状态自动配置的全球单播地址的首选生命期

Joined group address(es)

接口加入的组播组地址

MTU

接口的最大传输单元

ND DAD is enabled, number of DAD attempts

重复地址检测功能是否使能（该例中使能）

若处于使能状态则同时显示重复地址检测时发送邻居请求消息的次数（可通过**ipv6 nd dad attempts**命令进行配置）

若处于关闭状态则显示"ND DAD is disabled"（可通过配置重复地址检测时发送邻居请求消息的次数为0关闭该功能）

ND reachable time

保持邻居可达的时间

ND retransmit interval

邻居请求消息重传时间间隔

Hosts use stateless autoconfig for addresses

主机采用无状态自动配置的方式获取IPv6地址

InReceives

接口接收到的所有IPv6报文，包括各种错误的报文

InTooShorts

接口接收到的太短的IPv6报文，譬如报文长度不足40字节

InTruncatedPkts

接口接收到的IPv6报文，其实际长度小于报文内容中所指出的报文长度

InHopLimitExceeds

接口接收到的IPv6报文，其跳数超出限制

InBadHeaders

接口接收到的IPv6报文，其基本报文头错误

InBadOptions

接口接收到的IPv6报文，其扩展报文头错误

ReasmReqds

接口接收到的IPv6分片报文

ReasmOKs

接口接收到的IPv6分片，被组装好的报文，这里指的不是分片个数，是组装好的报文数

InFragDrops

接口接收到的IPv6分片报文，该分片报文由于错误被丢弃

InFragTimeouts

接口接收到的IPv6分片报文，该分片停留在系统缓冲中时间超过指定时间，被丢弃

OutFragFails

出接口上分片失败的报文

InUnknownProtos

接口接收到的IPv6报文，其协议类型不能被识别或不能被支持

InDelivers

接口接收到的IPv6报文，该报文被上送到IPv6的用户协议处（如ICMPv6、TCP、UDP等）

OutRequests

IPv6本地出报文，即各IPv6的用户协议层要求IPv6发送出去的报文

OutForwDatagrams

出接口上被转发的报文

InNoRoutes

接口接收到的IPv6报文，找不到匹配的路由被丢弃

InTooBigErrors

接口接收到的IPv6报文，转发时，由于超过链路MTU被丢弃

OutFragOKs

出接口上分片成功的报文

OutFragCreates

出接口上成功分片后的分片报文，指分片数

InMcastPkts

接口接收到的IPv6组播报文

InMcastNotMembers

接口接收到的IPv6组播报文，但该接口却没有加入对应组播组，报文被丢弃

OutMcastPkts

接口发送的IPv6组播报文

InAddrErrors

接口接收到的IPv6报文，其目的地址不合法，报文被丢弃

InDiscards

接口接收到的IPv6报文，由于资源问题被丢弃的报文，而不是由于报文内容等被丢弃的报文

OutDiscards

接口需要发送的报文，由于资源问题被丢弃的报文，而不是由于报文内容等被丢弃的报文

\# 查看所有接口的IPv6摘要信息。

\<Sysname\> display ipv6 interface brief

\*down: administratively down

(s): spoofing

Interface                                 Physical Protocol IPv6 Address

Vlan-interface1                          down       down      Unassigned

Vlan-interface2                          up         up         2001::1

Vlan-interface100                        up         up        Unassigned

表1-6 display ipv6 interface brief命令显示信息描述表

字段

描述

\*down: administratively down

接口处于管理down状态，即采用**shutdown**命令关闭了该接口

(s): spoofing

接口的欺骗属性，即接口的链路协议状态显示是up的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立的

Interface

接口的名称

Physical

接口的物理状态，可能的状态及含义如下：

·\*down：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·down：该接口的管理状态为开启，但物理状态为关闭，即该接口对应的VLAN内没有处于UP状态的端口（可能因为没有连接好或者线路故障）

·up：该接口的管理状态和物理状态均为开启

Protocol

接口的链路层协议状态，可能的状态及含义如下：

·down：该接口的协议状态为关闭

·up：该接口的协议状态为开启

IPv6 Address

接口的IPv6地址，接口上有全球单播地址时，显示地址最小的全球单播地址，没有全球单播地址则显示链路本地地址，没有链路本地地址则显示"Unassigned"

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 interface prefix**

------------------------------------------------------------------------

**[display ipv6 interface prefix**]命令用来显示接口的IPv6前缀信息。

【命令】

**[display ipv6 interface** *interface-type interface-number* **prefix**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。

【举例】

\# 查看VLAN接口10的IPv6前缀信息。

\<Sysname\> display ipv6 interface Vlan-interface 10 prefix

Prefix: 1001::/65                                          Origin: ADDRESS

Age:    -                                                     Flag:   AL

Lifetime(Valid/Preferred): 2592000/604800

Prefix: 2001::/64                                          Origin: STATIC

Age:    -                                                     Flag:   L

Lifetime(Valid/Preferred): 3000/2000

Prefix: 3001::/64                                          Origin: RA

Age:    600                                                   Flag:   A

Lifetime(Valid/Preferred): -

表1-7 display ipv6 interface prefix命令显示信息描述表

字段

描述

Prefix

IPv6地址前缀

Origin

前缀来源，包括：

·STATIC：手工配置前缀（命令**ipv6 nd ra prefix**）

·RA：使能无状态地址自动配置功能后根据RA报文生成的前缀

·ADDRESS：由手工配置的地址产生的前缀

Age

老化时间（单位为秒），"-"表示前缀不会老化

Flag

前缀随RA报文公告时携带的标记，"-"表示没有标记

·L：表示前缀是直接可达的。没有此标记，则表示前缀不是该链路上直连可达的

·A：表示前缀用于无状态自动配置。没有此标记，则表示前缀不用于无状态自动配置

Lifetime

前缀随RA报文公告时携带的生存时间（单位为秒），"-"表示前缀不需要公告

·Valid：前缀的有效生命期

·Preferred：前缀的首选生命期

【相关命令】

·**ipv6 nd ra prefix**

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 nd snooping**

------------------------------------------------------------------------

**[display ipv6 nd snooping**]命令用来显示ND Snooping表项信息。

【命令】

**[display ipv6 nd snooping **[[ [ [ **vlan** *vlan-id \|* **interface** *interface-type interface-number*   **global** \| **link-local** ] ] **\|** *ipv6-address* ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-id*]：显示指定VLAN的ND Snooping表项。*vlan-id*的取值范围为1～4094。

**[interface*** interface-type interface-number*]：显示指定接口的ND Snooping表项。*interface-type interface-number*表示接口类型和接口编号

*[ipv6-address *]：显示指定IPv6地址的ND Snooping表项。

**[global**]：显示表项地址类型为全球单播地址的ND Snooping表项

**[link-local**]：显示表项地址类型为链路本地地址的ND Snooping表项

**[verbose**]**：**显示ND Snooping表项的详细信息

【举例】

\# 显示VLAN 1的ND Snooping表项信息。

\<Sysname\> display ipv6 nd snooping vlan 1

IPv6 address              MAC address     VID  Interface     Status       Age

1::2                       0000-1234-0c01  1    GE1/0/2        VALID        57

\<Sysname\> display ipv6 nd snooping vlan 1 verbose

IPv6 address: 1::2

MAC address: 0000-1234-0c01

Interface: GE0/0/2

First VLAN ID: 1   Second VLAN ID: N/A

Status: VALID   Age: 57

表1-8 display ipv6 nd snooping命令显示信息描述表

字段

描述

IPv6 address

ND Snooping表项的IPv6地址

MAC address

ND Snooping表项的MAC地址

VID

ND Snooping表项所属VLAN的编号

First VLAN ID

ND Snooping表项所属外层VLAN的编号

Second VLAN ID

ND Snooping表项所属内层VLAN的编号，当不存在内层VLAN信息时，则显示N/A。外层VLAN和内层VLAN的描述，请参见"二层技术-以太网交换配置指导"中的"QinQ"

Interface

ND Snooping表项所对应的入端口

Status

ND Snooping表项的显示的状态，选项如下：

·TENTATIVE：临时非生效状态；

·VALID：生效状态；

·TESTING_TPLT：从信任端口收到对应源地址的报文，或者表项到达老化，触发向该表项所在端口进行探测；

·TESTING_VP：从其他非信任端口收到对应源地址的报文，触发向该表项所在接口进行探测；

Age

ND Snooping表项的老化时间，单位为秒

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 nd snooping count**

------------------------------------------------------------------------

**[display ipv6 nd snooping count**]命令用来显示ND Snooping表项的数目。

【命令】

**[display ipv6 nd snooping count ** **interface** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口的ND Snooping表项数目。*interface-type interface-number*表示接口类型和接口编号

【举例】

\# 显示设备上的ND Snooping表项数目。

\<Sysname\> display ipv6 nd snooping count 

Total number of entries: 5

\# 显示接口GigabitEthernet1/0/1的ND Snooping表项数目。

\<Sysname\> display ipv6 nd snooping count interface gigabit 1/0/1

Total number of entries on interface: 2

表1-9 display ipv6 nd snooping count命令显示信息描述表

字段

描述

Total number of entries

设备的ND Snooping表项数目

Total number of entries on interface: *number*

接口下的ND Snooping表项数目

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 nd suppression xconnect-group**

------------------------------------------------------------------------

**[display ipv6 nd suppression xconnect-group**]命令用来显示ND泛洪抑制表项。

【命令】

集中式设备：

**[display** **ipv6 nd** **suppression xconnect-group** [ **name** *group-name*   **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **ipv6 nd** **suppression xconnect-group** [ **name** *group-name*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display** **ipv6 nd** **suppression xconnect-group** [ **name** *group-name*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** group-name*]：交叉连接组的名称，取值为1～31个字符的字符串，不能包含字符"-"，区分大小写。

**[count**]：当前ND泛洪抑制表项的数目。

**[slot*** slot-number*]：显示指定单板的ND泛洪抑制表项。*slot-number*表示单板所在的槽位号。如果未指定本参数，则表示所有单板上的ND泛洪抑制表项（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的ND泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的ND泛洪抑制表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的ND泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的ND泛洪抑制表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ND泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的ND泛洪抑制表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ND泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的ND泛洪抑制表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ND泛洪抑制表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示所有交叉连接组下的ND泛洪抑制表项。

\<Sysname\> display ipv6 nd suppression xconnect-group

IPv6 address            MAC address     Xconnect-group   Connection       Aging 

2001::1                 000c-29fe-5a8f  vpna                svc               25    

2001::2                 000c-29fe-5aa3  vpna                svc               2      

\# 显示当前ND泛洪抑制表项的计数。

\<Sysname\> display ipv6 nd suppression xconnect-group count

Total entries: 2

表1-10 display ipv6 nd suppression xconnect-group命令显示信息描述表

字段

描述

IPv6 address

ND泛洪抑制表项的IPv6地址

MAC address

ND泛洪抑制表项的MAC地址

Xconnect-group

ND泛洪抑制表项的Xconnect-group名称

Connection

ND泛洪抑制表项的Connection名称

Aging

ND泛洪抑制表项的老化时间，单位为分钟

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 neighbors**

------------------------------------------------------------------------

**[display ipv6 neighbors**]命令用来显示邻居信息。

【命令】

集中式设备：

**[display ipv6 neighbors**[ { *ipv6-address \|* **all** *\|* **dynamic** \| **interface** *interface-type interface-number* \| **static** \| **vlan** *vlan-id* } [ **verbose** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 neighbors**[ { { *ipv6-address \|* **all** *\|* **dynamic** \| **static** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ] \| **interface** *interface-type interface-number* \| **vlan** *vlan-id* }  **verbose** ]]

分布式设备－IRF模式：

**[display ipv6 neighbors**[ { { *ipv6-address \|* **all** *\|* **dynamic** \| **static** } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ] \| **interface** *interface-type interface-number* \| **vlan** *vlan-id* }  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-address*]：显示指定IPv6地址的邻居信息。

**[all**]：显示所有邻居的信息，包括公网和所有私网下动态获取的和静态配置的邻居信息。

**[dynamic**]：显示所有动态获取的邻居信息。

**[static**]：显示所有静态配置的邻居信息。

**[slot ***slot-number*]：显示指定单板的邻居信息。*slot-number*表示单板所在的槽位号。如果未配置本参数，则显示所有单板上的邻居信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的邻居信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的邻居信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的邻居信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的邻居信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的邻居信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的邻居信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的邻居信息。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的邻居信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的邻居信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[interface*** interface-type interface-number*]：显示指定接口的邻居信息。*interface-type interface-number*为接口类型和接口编号。

**[vlan** *vlan-id*]：显示指定VLAN的邻居信息。*vlan-id*的取值范围为1～4094。

**[verbose**]：显示邻居的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以通过**reset ipv6 neighbors**命令清除指定的IPv6邻居信息。

【举例】

\# 查看所有的邻居信息。

\<Sysname\> display ipv6 neighbors all

         Type: S-Static    D-Dynamic    O-Openflow    R-Rule    I-Invalid

IPv6 Address                   Link Layer     VID  Interface      State T  Age

FE80::200:5EFF:FE32:B800    0000-5e32-b800 N/A  GE1/0/1        REACH D  10

\# 查看所有邻居的详细信息。

\<Sysname\> display ipv6 neighbors all verbose

          Type: S-Static    D-Dynamic    O-Openflow    R-Rule    I-Invalid

IPv6 Address: FE80::200:5EFF:FE32:B800

Link layer  : 0000-5e32-b800      VID : N/A  Interface: GE1/0/1

State        : REACH                 Type: IS   Age      : -

Vpn-instance: vpn1

NickName    : 0x0001

表1-11 display ipv6 neighbors命令显示信息描述表

字段

描述

IPv6 Address

邻居的IPv6地址

Link Layer

邻居的链路层地址（MAC地址）

VID

与邻居相连的接口所属的VLAN

Interface

与邻居相连的接口

State

邻居的状态，包括：

·INCMP：正在解析地址，邻居的链路层地址尚未确定

·REACH：邻居可达

·STALE：未确定邻居是否可达，设备不会再验证邻居的可达性，除非有数据发送给该邻居

·DELAY：未确定邻居是否可达，延迟一段时间发送邻居请求报文

·PROBE：未确定邻居是否可达，发送邻居请求报文来验证邻居的可达性

Type

邻居信息的类型，S表示静态配置，D表示动态获取，O表示从OpenFlow特性获取，R表示从IPoE或Portal等特性获取，I表示无效

Age

静态项显示"--"，动态项显示上次可达以来经过的时间（单位为秒），如果始终不可达则显示"\#"（只适用于动态项）

Vpn-instance

VPN实例名称，No Vrf表示没有配置相应表项的VPN实例

NickName

邻居表项的NickName（长度为4的十六进制数字，例如0x012a），关于NickName的详细介绍，请参见"TRILL配置指导"中的"TRILL"

【相关命令】

·**ipv6 neighbor**

·**reset ipv6 neighbors**

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 neighbors count**

------------------------------------------------------------------------

**[display ipv6 neighbors count**]命令用来显示邻居表项的个数。

【命令】

集中式设备：

**[display ipv6 neighbors**[ { **all** *\|* **dynamic** \| **interface** *interface-type interface-number* \| **static** \| **vlan** *vlan-id* } **count**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 neighbors**[ { { **all** *\|* **dynamic** \| **static** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ] \| **interface** *interface-type interface-number* \| **vlan** *vlan-id* } **count**]]

分布式设备－IRF模式：

**[display ipv6 neighbors**[ { { **all** *\|* **dynamic** \| **static** } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ] \| **interface** *interface-type interface-number* \| **vlan** *vlan-id* } **count**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有邻居表项的总个数，包括动态获取的和静态配置的邻居信息。

**[dynamic**]：显示所有动态获取的邻居表项的总个数。

**[static**]：显示所有静态配置的邻居表项的总个数。

**[slot ***slot-number*]：显示指定单板的邻居表项的总个数。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的邻居表项的总个数。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的邻居表项的总个数。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的邻居表项的总个数。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的邻居表项的总个数。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的邻居表项的总个数。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的邻居表项的总个数。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的邻居表项的总个数。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的邻居表项的总个数。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的邻居表项的总个数。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的邻居表项的总个数。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[interface*** interface-type interface-number*]：显示指定接口的邻居表项的总个数。*interface-type interface-number*为接口类型和接口编号。

**[vlan** *vlan-id*]：显示指定VLAN的邻居表项的总个数。*vlan-id*的取值范围为1～4094。

【举例】

\# 显示动态获取的邻居表项的总个数。

\<Sysname\> display ipv6 neighbors dynamic count

 Total number of dynamic entries: 2

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 neighbors vpn-instance**

------------------------------------------------------------------------

![说明](IPv6基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display ipv6 neighbors vpn-instance**]命令用来显示指定VPN的邻居信息。

【命令】

**[display ipv6 neighbors vpn-instance ***vpn-instance-name***** **count** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vpn-instance-name*]：指定ND表项所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。该VPN实例必须已经存在。

**[count**]：显示指定VPN中的邻居表项的总数。

【举例】

\# 显示名为vpn1的VPN实例中的邻居信息。

\<Sysname\> display ipv6 neighbors vpn-instance vpn1

         Type: S-Static    D-Dynamic    O-Openflow    I-Invalid

IPv6 Address                   Link Layer      VID  Interface      State T  Age

FE80::200:5EFF:FE32:B800    0000-5e32-b800  N/A  GE1/0/1        REACH IS -

表1-12 display ipv6 neighbors vpn-instance命令显示信息描述表

字段

描述

IPv6 Address

邻居的IPv6地址

Link-layer

邻居的链路层地址（MAC地址）

VID

与邻居相连的接口所属的VLAN

Interface

与邻居相连的接口

State

邻居的状态，包括：

·INCMP：正在解析地址，邻居的链路层地址尚未确定；

·REACH：邻居可达；

·STALE：未确定邻居是否可达，设备不会再验证邻居的可达性，除非有数据发送给该邻居；

·DELAY：未确定邻居是否可达，延迟一段时间发送邻居请求报文；

·PROBE：未确定邻居是否可达，发送邻居请求报文来验证邻居的可达性。

T

邻居信息的类型，S表示静态配置，D表示动态获取，O表示通过OpenFlow特性获取，I表示无效

Age

静态项显示"--"，动态项显示上次可达以来经过的时间（单位为秒），如果始终不可达则显示"\#"（只适用于动态项）

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 pathmtu**

------------------------------------------------------------------------

**[display ipv6 pathmtu**]命令用来显示IPv6的PMTU信息。

【命令】

**[display ipv6 pathmtu** [ **vpn-instance** *vpn-instance-name*  { *ipv6-address \|* { **all** \| **dynamic** \| **static** }  **count**  }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN的IPv6 PMTU信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的IPv6 PMTU信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ipv6-address*]：显示到达指定IPv6地址的PMTU信息。

**[all**]：显示所有公网的PMTU信息。

**[dynamic**]：显示所有动态PMTU信息。

**[static**]：显示所有静态PMTU信息。

**[count**]：显示PMTU表项数目。

【使用指导】

通过本命令可以查看IPv6的PMTU信息，包括动态创建的PMTU信息和静态配置的PMTU信息。

【举例】

\# 显示所有PMTU信息。

\<Sysname\> display ipv6 pathmtu all

IPv6 destination address                PathMTU   Age   Type

1:2::3:2                                   1800       -      Static

1:2::4:2                                   1400       10     Dynamic

1:2::5:2                                   1280       10     Dynamic

\# 显示所有PMTU表项数目。

\<Sysname\> display ipv6 pathmtu all count

Total number of entries: 3

表1-13 display ipv6 pathmtu命令显示信息描述表

字段

描述

IPv6 destination address

IPv6目的地址

PathMTU

对应IPv6地址的PMTU值

Age

PMTU老化时间（单位为分钟），如果是静态表项则显示为"-"

Type

PMTU类型，Dynamic表示动态协商的PMTU，Static表示静态配置的PMTU

Total number of entries

PMTU表项数目

【相关命令】

·**ipv6 pathmtu**

·**reset ipv6 pathmtu**

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 prefix**

------------------------------------------------------------------------

**[display ipv6 prefix**]命令用来显示IPv6前缀信息，包括静态和动态前缀。

【命令】

**[display ipv6 prefix** [ *prefix-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[prefix-number*]：显示指定的IPv6前缀信息。*prefix-number*表示IPv6前缀编号，取值范围为1～1024。如果不指定本参数，则显示所有IPv6前缀的信息。

【使用指导】

·静态IPv6前缀指的是通过ipv6 prefix命令创建的前缀。

·动态IPv6前缀指的是设备作为DHCPv6客户端获取到前缀后，自动创建的指定编号的IPv6前缀。详细介绍请参见"三层技术-IP业务命令参考/DHCPv6"中的命令**ipv6 dhcp client pd**。

【举例】

\# 显示所有IPv6前缀的信息。

\<Sysname\> display ipv6 prefix

Number  Prefix                                     Type

1        1::/16                                     Static

2        11:77::/32                                Dynamic

\# 显示IPv6前缀编号1的信息。

\<Sysname\> display ipv6 prefix 1

Number: 1

Type  : Dynamic

Prefix: ABCD:77D8::/32

Preferred lifetime 90 sec, valid lifetime 120 sec

表1-14 display ipv6 prefix命令显示信息描述表

字段

描述

Number

前缀编号

Type

前缀的类型，取值包括：

·Static：表示静态IPv6前缀

·Dynamic：表示动态IPv6前缀

Prefix

前缀及其长度。"Not-available"表示目前尚未获取到前缀

Preferred lifetime 90 sec

首选生命期，单位为秒。如果是静态IPv6前缀，则不显示

valid lifetime 120 sec

有效生命期，单位为秒。如果是静态IPv6前缀，则不显示

【相关命令】

·**ipv6 prefix**

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 rawip**

------------------------------------------------------------------------

**[display ipv6 rawip**]命令用来显示IPv6 RawIP连接摘要信息。

【命令】

集中式设备：

**[display ipv6 rawip**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 rawip** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 rawip** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板的IPv6 RawIP连接摘要信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 RawIP连接摘要信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6 RawIP连接摘要信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6 RawIP连接摘要信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6 RawIP连接摘要信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6 RawIP连接摘要信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6 RawIP连接摘要信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 RawIP连接摘要信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 RawIP连接摘要信息。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 RawIP连接摘要信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6 RawIP连接摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以用来查看IPv6 RawIP连接摘要信息，包括本端IPv6地址、对端IPv6地址、使用IPv6 RawIP socket的协议号等信息。

【举例】

\# 显示IPv6 RawIP连接摘要信息。（分布式设备－IRF模式）

\<Sysname\> display ipv6 rawip

Local Addr            Foreign Addr        Protocol Chassis Slot  CPU PCB

2001:2002:2003:2     3001:3002:3003:3   58        1         1     0    0x0000000000000009

004:2005:2006:20     004:3005:3006:30

07:2008                07:3008

2002::100             2002::138            58        1         2     0    x0000000000000008

::                     ::                     58        1         5     0    0x0000000000000002

表1-15 {.FigureDescriptionChar}display ipv6 rawip命令显示信息描述表{.FigureDescriptionChar}

字段

描述

Local Addr

本端IPv6地址

Foreign Addr

对端IPv6地址

Protocol

使用IPv6 RawIP socket的协议号

Chassis

设备在IRF中的成员编号

Slot

单板所在的槽位号

CPU

节点所在的CPU编号

PCB

协议控制块索引

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 rawip verbose**

------------------------------------------------------------------------

**[display ipv6 rawip verbose**]命令用来显示IPv6 RawIP连接详细信息。

【命令】

集中式设备：

**[display ipv6 rawip verbose** [ **pcb** *pcb-index* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 rawip verbose** [ **slot** *slot-number* [ **cpu** *cpu-number*   **pcb** *pcb-index*  ]]]

分布式设备－IRF模式：

**[display ipv6 rawip verbose** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*   **pcb** *pcb-index*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pcb** *pcb-index*]：显示指定协议控制块索引的IPv6 RawIP连接详细信息。*pcb-index*表示协议控制块索引，取值范围请以设备的实际情况为准。

**[slot** *slot-number*]：显示指定单板的IPv6 RawIP连接详细信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 RawIP连接详细信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6 RawIP连接详细信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6 RawIP连接详细信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6 RawIP连接详细信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6 RawIP连接详细信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6 RawIP连接详细信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 RawIP连接详细信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 RawIP连接详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 RawIP连接详细信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6 RawIP连接详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以用来查看IPv6 RawIP连接详细信息，包括socket的创建者、状态、选项、类型、使用的协议号等，以及IPv6 RawIP连接的源IPv6地址和目的IPv6地址等信息。

【举例】

\# 显示IPv6 RawIP连接详细信息。（集中式设备）

\<Sysname\> display ipv6 rawip verbose

Total RawIP socket number: 1

 Creator: ping ipv6[320]

 State: N/A

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A

 Type: 3

 Protocol: 58

 Connection info: src = ::, dst = ::

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Send VRF: 0xffff

 Receive VRF: 0xffff

\# 显示Ipv6 RawIP连接详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display ipv6 rawip verbose

Total RawIP socket number: 1

 Slot: 6 Cpu: 0

 Creator: ping ipv6[320]

 State: N/A

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A

 Type: 3

 Protocol: 58

 Connection info: src = ::, dst = ::

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Send VRF: 0xffff

 Receive VRF: 0xffff

\# 显示IPv6 RawIP连接详细信息。（分布式设备－IRF模式）

\<Sysname\> display ipv6 rawip verbose

Total RawIP socket number: 1

 Chassis: 2 Slot: 6 Cpu: 0

 Creator: ping ipv6[320]

 State: N/A

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 9216 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A

 Type: 3

 Protocol: 58

 Connection info: src = ::, dst = ::

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Send VRF: 0xffff

 Receive VRF: 0xffff

表1-16 display ipv6 rawip verbose命令显示信息描述表

字段

描述

Total RawIP socket number

IPv6 RawIP socket总数

Chassis

设备在IRF中的成员编号（分布式设备－IRF模式）

Slot

单板所在的槽位号（分布式设备－独立运行模式/分布式设备－IRF模式）

Slot

设备在IRF中的成员编号（集中式IRF设备）

Cpu

节点所在的CPU编号

Creator

创建socket的任务名称，括号中为创建者的进程号

State

socket的状态，可能的状态如下：

·NOFDREF：用户已经关闭

·ISCONNECTED：连接已经建立

·ISCONNECTING：正在建立连接

·ISDISCONNECTING：正在断开连接

·ASYNC：异步方式

·ISDISCONNECTED：连接已经断开

·PROTOREF：协议强关联

·N/A：不处于上述状态

Options

socket的选项，有以下几种：

·SO_DEBUG：记录套接字的调试信息

·SO_ACCEPTCONN：server端监听连接请求

·SO_REUSEADDR：允许本地地址重复使用

·SO_KEEPALIVE：协议需要查询空闲的连接

·SO_DONTROUTE：设置不查路由表，由于目的地址是直连网络的情况

·SO_BROADCAST：套接字支持广播报文

·SO_LINGER：套接字关闭但仍发送剩余数据

·SO_OOBINLINE：带外数据采用内联方式存储

·SO_REUSEPORT：允许本地端口重复使用

·SO_TIMESTAMP：记录入报文时间戳，只对非连接的协议有效，时间精确到毫秒

·SO_NOSIGPIPE：socket不能发送数据导致返回失败时不创建SIGPIPE

·SO_TIMESTAMPNS：和时戳选项功能类似，时间可以精确到纳秒

·SO_KEEPALIVETIME：设置空闲探测时间，TCP支持此选项

·SO_FILTER：设置报文过滤条件，OSI Socket和RawIP支持此选项

·N/A：没有设置选项

Error

影响socket连接的错误码

Receiving buffer (cc/hiwat/lowat/state)

接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态

状态的取值有：

·CANTSENDMORE：不能发送数据到对端

·CANTRCVMORE：不能从对端接收数据

·RCVATMARK：接收标记

·N/A：不处于上述状态

Sending buffer (cc/hiwat/lowat/state)

发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间和状态

状态的取值有：

·CANTSENDMORE：不能发送数据到对端

·CANTRCVMORE：不能从对端接收数据

·RCVATMARK：接收标记

·N/A：不处于上述状态

Type

使用的socket类型，类型的取值有：

·1：SOCK_STREAM，流模式，提供可靠的字节流。TCP协议使用此类型

·2：SOCK_DGRAM，数据报模式的通信。UDP协议使用此类型

·3：SOCK_RAW，RAW模式的通信方式

·N/A：不是上述类型

Protocol

使用IPv6 RawIP socket的协议号，58表示ICMP协议

Connection info

连接信息，分别为源IPv6地址、目的IPv6地址

Inpcb flags

Internet协议控制块中的标记，标记的取值有：

·INP_RECVOPTS：接收传入的IPv6选项

·INP_RECVRETOPTS：接收回应的IPv6选项

·INP_RECVDSTADDR：接收目的IPv6地址

·INP_HDRINCL：用户提供整个IPv6头

·INP_REUSEADDR：重复使用地址

·INP_REUSEPORT：重复使用端口号

·INP_ANONPORT：用户未指定端口

·INP_PROTOCOL_PACKET：标识报文为协议报文

·INP_RCVVLANID：接收报文的VLAN ID，仅UDP和RawIP支持

·IN6P_IPV6_V6ONLY：仅支持IPv6协议栈

·IN6P_PKTINFO：接收报文的源地址和入接口

·IN6P_HOPLIMIT：接收报文hoplimit

·IN6P_HOPOPTS：接收报文的逐跳扩展头信息

·IN6P_DSTOPTS：接收报文的目的扩展头信息

·IN6P_RTHDR：接收报文的路由扩展头信息

·IN6P_RTHDRDSTOPTS：接收报文的路由头前的目的扩展头信息

·IN6P_TCLASS：接收报文的优先级信息

·IN6P_AUTOFLOWLABEL：使用随机流标签

·IN6P_RFC2292：使用RFC2292 API

·IN6P_MTU：感知路径MTU的变化，TCP不支持

·INP_RCVMACADDR：接收报文的MAC

·INP_USEICMPSRC：使用配置的ICMPv6地址作为源地址

·INP_SYNCPCB：阻塞等待inpcb同步

·N/A：不是上述标记

Inpcb extflag

Internet协议控制块中的扩展标记，标记的取值有：

·INP_EXTRCVPVCIDX：接收报文时记录报文的PVC索引

·INP_RCVPWID：接收报文时记录报文的PW ID

·N/A：不是上述标记

Inpcb vflag

Internet协议控制块中的IP版本标记，标记的取值有：

·INP_IPV4：运用与IPv4通信

·INP_IPV6：运用与IPv6通信

·INP_IPV6PROTO：运用IPv6协议创建的inpcb

·INP_TIMEWAIT：处于等待状态

·INP_ONESBCAST：发送广播报文

·INP_DROPPED：协议丢弃标志

·INP_SOCKREF：socket强关联

·INP_DONTBLOCK：inpcb同步时不能被阻塞

·N/A：不是上述标记

Hop limit(minimum hop limit)

Internet协议控制块中的跳数限制，括号中为最小跳数限制

Send VRF

发送实例

Receive VRF

接收实例

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 router-renumber statistics**

------------------------------------------------------------------------

**[display ipv6 router-renumber statistics**]命令用来显示路由器重编号的统计信息。

【命令】

**[display ipv6 router-renumber statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

使用本命令可以查看路由器重编号流量统计信息、记录的序列号、重置序列号和分段号信息。

【举例】

\# 显示路由器重编号的统计信息。

\<Sysname\> display ipv6 router-renumber statistics

Enabling/disabling protocol failed:         0

Packets with sequence number error:         2

Packets with segment number error:           1

PCO check failed:                                  0

Packets with T-flag set and R-flag unset:      1

Router-renumber function disable:            0

Packets too short:                              0

Packets with invalid destinations:           0

Create result packets failed:                 0

Sent result packets failed:                   0

Received command packets:                      7

Received reset packets:                          3

Sent result packets:                            9

SequenceNumber:                                   0x2

ResetSequenceNumber:                             0x2

SegmentNumber[0:                             0x1]

SegmentNumber[1:                             0x0]

SegmentNumber[2:                             0x0]

SegmentNumber[3:                             0x0]

SegmentNumber[4:                             0x0]

SegmentNumber[5:                             0x0]

SegmentNumber[6:                             0x0]

SegmentNumber[7:                             0x0]

表1-17 display ipv6 router-renumber statistics命令显示信息描述表

字段

描述

Enabling/disabling protocol failed

使能协议报文上送CPU失败的个数

Packets with sequence number error

序列号错误的报文个数

Packets with segment number error

分段号错误的报文个数

PCO check failed

PCO信息块检测错误的报文个数

Packet s with T-flag set and R-flag unset

设置了T标志位、没有设置R标志位的消息，即不需要回应的测试报文个数

Router-renumber function disable

接口没有使能重编号路由协议的报文个数

Packets too short

报文长度小于正常值的报文个数

Packets with invalid destinations

无效目的地址的报文个数

Create result packets failed

创建Result消息失败的报文个数

Sent result packets failed

发送Result报文失败个数

Received command packets

接收Command报文的个数

Received reset packets

接收Reset报文的个数

Sent result packets

发送Result报文的个数

SequenceNumber

记录序列号

ResetSequenceNumber

记录重置序列号

SegmentNumber0 - 7

组成记录分段号

【相关命令】

·**reset ipv6 router-renumber statistics**

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 statistics**

------------------------------------------------------------------------

**[display ipv6 statistics**]命令用来显示IPv6报文及ICMPv6报文的统计信息。

【命令】

集中式设备：

**[display ipv6 statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 statistics** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板的IPv6报文及ICMPv6报文统计信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示所有单板上的IPv6报文及ICMPv6报文统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6报文及ICMPv6报文统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6报文及ICMPv6报文统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6报文及ICMPv6报文统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6报文及ICMPv6报文统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6报文及ICMPv6报文统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6报文及ICMPv6报文统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6报文及ICMPv6报文统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或者PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6报文及ICMPv6报文统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6报文及ICMPv6报文统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以用来查看设备接收和发送IPv6报文及ICMPv6报文的统计信息。

用户可以通过**reset ipv6 statistics**命令清除所有的IPv6报文及ICMPv6报文统计信息。

【举例】

\# 查看IPv6报文及ICMPv6报文的统计信息。

\<Sysname\> display ipv6 statistics

  IPv6 statistics:

    Sent packets:

      Total:      0

        Sent locally:         0            Forwarded:              0

        Raw packets:          0            Discarded:              0

        Fragments:            0            Fragments failed:      0

        Routing failed:       0

    Received packets:

      Total:      0

        Received locally:     0            Hop limit exceeded:  0

        Fragments:             0            Reassembled:           0

        Reassembly failures:  0            Reassembly timeout:  0

        Format errors:         0            Option errors:        0

        Protocol errors:      0

  ICMPv6 statistics:

    Sent packets:

      Total:      0

        Unreachable:           0             Too big:                0

        Hop limit exceeded:   0             Reassembly timeouts: 0

        Parameter problems:   0

        Echo requests:         0             Echo replies:          0

        Neighbor solicits:    0             Neighbor adverts:     0

        Router solicits:      0             Router adverts:        0

        Redirects:             0              Router renumbering:   0

      Send failed:

        Rate limitation:      0             Other errors:          0

    Received packets:

      Total:      0

        Checksum errors:      0             Too short:              0

        Bad codes:             0

        Unreachable:           0             Too big:                 0

        Hop limit exceeded:   0             Reassembly timeouts:   0

        Parameter problems:   0             Unknown error types:   0

        Echo requests:         0             Echo replies:           0

        Neighbor solicits:    0             Neighbor adverts:      0

        Router solicits:       0             Router adverts:        0

        Redirects:              0             Router renumbering:   0

        Unknown info types:   0

      Deliver failed:

        Bad length:           0

表1-18 display ipv6 statistics命令显示信息描述表

字段

描述

IPv6 statistics:

IPv6报文统计信息

Sent packets:

  Total:

    Sent locally:

    Forwarded:

    Raw packets:

    Discarded:

    Fragments:

    Fragments failed:

    Routing failed:

发送IPv6报文的统计信息，包括：

·本地发送报文和转发报文的总数

·本地发送报文数

·转发报文数

·使用raw socket发送的报文数

·丢弃报文数

·发送分片报文数

·分片报文发送失败的个数

·路由失败报文数

Received packets:

  Total:

    Received locally:

    Hop limit exceeded:

    Fragments:

    Reassembled:

    Reassembly failures:

    Reassembly timeout:

    Format errors:

    Option errors:

    Protocol errors:

接收IPv6报文的统计信息，包括：

·接收报文总数

·本地接收报文数，即目的地是本机的报文数

·超出跳数范围的报文数

·接收的分片报文数

·重组报文数

·重组失败的报文数

·重组超时的报文数

·格式错误的报文数

·选项错误的报文数

·协议错误的报文数

ICMPv6 statistics:

ICMPv6报文的统计信息

Sent packets:

  Total:

    Unreached:

    Too big:

    Hop limit exceeded:

    Reassembly timeouts:

    Parameter problems:

    Echo requests:

    Echo replies:

    Neighbor solicits:

    Neighbor adverts:

    Router solicits:

    Router adverts:

    Redirects:

    Router Renumbering

  Sent failed:

    Rate limitation:

    Other errors:

发送ICMPv6报文的统计信息，包括：

·发送报文总数

·目的不可达报文数

·报文太长的报文数

·超出跳数限制的报文数

·分片重组超时报文数

·参数错误报文数

·回应请求报文数

·回应响应报文数

·邻居请求报文数

·邻居通告报文数

·路由器请求报文数

·路由器通告报文数

·重定向报文数

·路由器重编号报文数

·本机发送失败的报文数

·因速率超过限制而未发送的报文数

·其他错误的报文数

Received packets:

  Total:

    Checksum errors:

    Too short:

    Bad codes:

    Unreachable:

    Too big:

    Hop limit exceeded:

    Reassembly timeouts:

    Parameter problems:

    Unknown error types:

    Echo requests:

    Echo replies:

    Neighbor solicits:

    Neighbor adverts:

    Router solicits:

    Router adverts:

    Redirects:

    Router renumbering:

    Unknown info types:

  Deliver failed:

    Bad length:

接收ICMPv6报文的统计信息，包括：

·接收报文总数

·校验和错误的报文数

·报文太短的报文数

·错误代码的报文数

·不可达报文数

·报文太长的报文数

·超出跳数限制的报文数

·分片重组超时的报文数

·参数错误报文数

·未知错误报文数

·回应请求报文数

·回应响应报文数

·邻居请求报文数

·邻居通告报文数

·路由器请求报文数

·路由器通告报文数

·重定向报文数

·路由器重编号报文数

·未知信息报文数

·上送本机失败的报文数

·长度错误的报文数

【相关命令】

·**reset ipv6 statistics**

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 tcp**

------------------------------------------------------------------------

**[display ipv6 tcp**]命令用来显示IPv6 TCP连接摘要信息。

【命令】

集中式设备：

**[display ipv6 tcp**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 tcp** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 tcp** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板的IPv6 TCP连接摘要信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 TCP连接摘要信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6 TCP连接摘要信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6 TCP连接摘要信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6 TCP连接摘要信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备或PEX上的IPv6 TCP连接摘要信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6 TCP连接摘要信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 TCP连接摘要信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 TCP连接摘要信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 TCP连接摘要信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6 TCP连接摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以用来查看IPv6 TCP连接摘要信息，包括本端IPv6地址及端口号、对端IPv6地址及端口号、TCP连接的状态等信息。

【举例】

\# 显示IPv6 TCP连接摘要信息。（分布式设备－IRF模式）

\<Sysname\> display ipv6 tcp

\*: TCP MD5 Connection

 LAddr-\>port         FAddr-\>port       State       Chassis Slot  CPU PCB

\*2001:2002:2003:2   3001:3002:3003:3 ESTABLISHED 1       1     0    0x000000000000c387

004:2005:2006:20    004:3005:3006:30

07:2008-\>1200        07:3008-\>1200

2001::1-\>23          2001::5-\>1284     ESTABLISHED 1       2     0    0x0000000000000008

2003::1-\>25          2001::2-\>1283     LISTEN       1       3     0    0x0000000000000009

表1-19 {.FigureDescriptionChar}display ipv6 tcp命令显示信息描述表{.FigureDescriptionChar}

字段

描述

\*

如果某个连接前有此标识，则表示该TCP连接是采用MD5加密算法认证的连接

LAddr-\>port

本端IPv6地址及端口号

FAddr-\>port

对端IPv6地址及端口号

State

TCP连接状态，可能的状态如下：

·CLOSED：服务器收到客户端的关闭连接请求回应后所处的状态

·LISTEN：服务器在等待连接请求时所处的状态

·SYN_SENT：客户端发出连接请求等待服务器回应时所处的状态

·SYN_RCVD：服务器收到客户端连接请求时所处的状态

·ESTABLISHED：服务器和客户端双方建立连接并能进行双向数据传递的状态

·CLOSE_WAIT：服务器收到客户端关闭连接请求时所处的状态

·FIN_WAIT_1：客户端发出关闭连接请求等待服务器回应时所处的状态

·CLOSING：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态

·LAST_ACK：服务器向客户端发出关闭连接请求等待回应时所处的状态

·FIN_WAIT_2：客户端收到服务器关闭连接回应后所处的状态

·TIME_WAIT：客户端收到服务器的关闭连接请求后所处的状态

Chassis

设备在IRF中的成员编号

Slot

单板所在的槽位号

CPU

节点所在的CPU编号

PCB

协议控制块索引

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 tcp-proxy**

------------------------------------------------------------------------

![说明](IPv6基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display ipv6 tcp-proxy**]命令用来显示IPv6 TCP代理连接的简要信息。

【命令】

集中式设备：

**[display ipv6 tcp-proxy**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 tcp-proxy slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display ipv6 tcp-proxy chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板的IPv6 TCP代理连接的简要信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6 TCP代理连接的简要信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6 TCP代理连接的简要信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6 TCP代理连接的简要信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 TCP代理连接的简要信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6 TCP代理连接的简要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

IPv6 TCP代理是一种与传统定义的IPv6 TCP相比更快速更灵活的IPv6 TCP实现。用于支持负载分担或WAAS业务。能够提供比普通IPv6 TCP传输更灵活的控制，从而达到传输优化的目的。

【举例】

\# 显示IPv6 TCP代理连接的简要信息。

\<Sysname\> display ipv6 tcp-proxy

LAddr-\>port            FAddr-\>port              State        Service type

2001::1-\>45            11:22:33:44-\>54602      ESTABLISHED WAAS

11:22:33:44-\>54602    2001::1-\>45              ESTABLISHED WAAS

表1-20 display ipv6 tcp-proxy命令显示信息描述表

字段

描述

LAddr-\>port

本端IPv6地址及端口号

Faddr-\>port

对端IPv6地址及端口号

State

IPv6 TCP代理连接状态，可能的状态如下：

·CLOSED：服务器收到客户端的关闭连接请求回应后所处的状态

·LISTEN：服务器在等待连接请求时所处的状态

·SYN_SENT：客户端发出连接请求等待服务器回应时所处的状态

·SYN_RECEIVED：服务器收到客户端连接请求时所处的状态

·ESTABLISHED：服务器和客户端双方建立连接并能进行双向数据传递的状态

·CLOSE_WAIT：服务器收到客户端关闭连接请求时所处的状态

·FIN_WAIT_1：客户端发出关闭连接请求等待服务器回应时所处的状态

·CLOSING：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态

·LAST_ACK：服务器向客户端发出关闭连接请求等待回应时所处的状态

·FIN_WAIT_2：客户端收到服务器关闭连接回应后所处的状态

·TIME_WAIT：客户端收到服务器的关闭连接请求后所处的状态

Service type

服务类型，可能的取值如下：

·LB：负载均衡服务

·WAAS：WAAS服务

·SSL VPN：SSL VPN服务

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 tcp verbose**

------------------------------------------------------------------------

**[display ipv6 tcp verbose**]命令用来显示IPv6 TCP连接详细信息。

【命令】

集中式设备：

**[display ipv6 tcp verbose** [ **pcb** *pcb-index* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 tcp verbose** [ **slot** *slot-number* [ **cpu** *cpu-number*   **pcb** *pcb-index*  ]]]

分布式设备－IRF模式：

**[display ipv6 tcp verbose** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*   **pcb** *pcb-index*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pcb** *pcb-index*]：显示指定协议控制块索引的IPv6 TCP连接详细信息。*pcb-index*表示协议控制块索引，取值范围请以设备的实际情况为准。

**[slot** *slot-number*]：显示指定单板的IPv6 TCP连接详细信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 TCP连接详细信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6 TCP连接详细信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6 TCP连接详细信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6 TCP连接详细信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6 TCP连接详细信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6 TCP连接详细信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 TCP连接详细信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 TCP连接详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 TCP连接详细信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6 TCP连接详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以用来查看IPv6 TCP连接详细信息，包括socket的创建者、状态、选项、类型、使用的协议号等，以及IPv6 TCP连接的源IPv6地址及端口号、目的IPv6地址及端口号、状态等信息。

【举例】

\# 显示IPv6 TCP连接详细信息。（集中式设备）

\<Sysname\> display ipv6 tcp verbose

TCP inpcb number: 1(tcpcb number: 1)

 Creator: bgpd[199]

 State: ISCONNECTED

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 65536 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 65536 / 512 / N/A

 Type: 1

 Protocol: 6

 Connection info: src = 2001::1-\>179 ,  dst = 2001::2-\>4181

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Connection state: ESTABLISHED

 TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR

 NSR state: READY(M)

 Send VRF: 0x0

 Receive VRF: 0x0

\# 显示IPv6 TCP连接详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display ipv6 tcp verbose

TCP inpcb number: 1(tcpcb number: 1)

 Slot: 6 Cpu: 0

 NSR standby: N/A

 Creator: bgpd[199]

 State: ISCONNECTED

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 65536 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 65536 / 512 / N/A

 Type: 1

 Protocol: 6

 Connection info: src = 2001::1-\>179 ,  dst = 2001::2-\>4181

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Connection state: ESTABLISHED

 TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR

 NSR state: READY(M)

 Send VRF: 0x0

 Receive VRF: 0x0

\# 显示IPv6 TCP连接详细信息。（分布式设备－IRF模式）

\<Sysname\> display ipv6 tcp verbose

TCP inpcb number: 1(tcpcb number: 1)

 Chassis: 2 Slot: 6 Cpu: 0

 NSR standby: N/A

 Creator: bgpd[199]

 State: ISCONNECTED

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 65536 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 65536 / 512 / N/A

 Type: 1

 Protocol: 6

 Connection info: src = 2001::1-\>179 ,  dst = 2001::2-\>4181

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Connection state: ESTABLISHED

 TCP options: TF_REQ_SCALE TF_REQ_TSTMP TF_SACK_PERMIT TF_NSR

 NSR state: READY(M)

 Send VRF: 0x0

 Receive VRF: 0x0

表1-21 {.FigureDescriptionChar}display ipv6 tcp verbo[se{.FigureDescriptionChar}]命令显示信息描述表{.FigureDescriptionChar}

字段

描述

TCP inpcb number

IPv6 TCP类型Internet协议控制块个数

tcpcb number

IPv6 TCP控制块个数（处于TIME_WAIT状态的TCP则不列入计数）

Chassis

设备在IRF中的成员编号（分布式设备－IRF模式）

Slot

单板所在的槽位号（分布式设备－独立运行模式/分布式设备－IRF模式）

Slot

设备在IRF中的成员编号（集中式IRF设备）

Cpu

节点所在的CPU编号

NSR standby::

NSR备所在IRF中的成员编号和槽位号，如果不存在NSR备，则显示"N/A"

Creator

创建socket的任务名称，括号中为创建者的进程号

State

socket的状态，可能的状态如下：

·NOFDREF：用户已经关闭

·ISCONNECTED：连接已经建立

·ISCONNECTING：正在建立连接

·ISDISCONNECTING：正在断开连接

·ASYNC：异步方式

·ISDISCONNECTED：连接已经断开

·PROTOREF：协议强关联

·N/A：不处于上述状态

Options

socket的选项，有以下几种：

·SO_DEBUG：记录套接字的调试信息

·SO_ACCEPTCONN：server端监听连接请求

·SO_REUSEADDR：允许本地地址重复使用

·SO_KEEPALIVE：协议需要查询空闲的连接

·SO_DONTROUTE：设置不查路由表，由于目的地址是直连网络的情况

·SO_BROADCAST：套接字支持广播报文

·SO_LINGER：套接字关闭但仍发送剩余数据

·SO_OOBINLINE：带外数据采用内联方式存储

·SO_REUSEPORT：允许本地端口重复使用

·SO_NOSIGPIPE：socket不能发送数据导致返回失败时不创建SIGPIPE

·SO_TIMESTAMPNS：和时戳选项功能类似，时间可以精确到纳秒

·SO_KEEPALIVETIME：设置空闲探测时间，TCP支持此选项

·SO_FILTER：设置报文过滤条件，OSI Socket和RawIP支持此选项

·N/A：没有设置选项

Error

影响socket连接的错误码

Receiving buffer(cc/hiwat/lowat/state)

接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态

状态的取值有：

·CANTSENDMORE：不能发送数据到对端

·CANTRCVMORE：不能从对端接收数据

·RCVATMARK：接收标记

·N/A：不处于上述状态

Sending buffer(cc/hiwat/lowat/state)

发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态

状态的取值有：

·CANTSENDMORE：不能发送数据到对端

·CANTRCVMORE：不能从对端接收数据

·RCVATMARK：接收标记

·N/A：不处于上述状态

Type

使用的socket类型，类型的取值有：

·1：SOCK_STREAM，流模式，提供可靠的字节流。TCP协议使用此类型

·2：SOCK_DGRAM，数据报模式的通信。UDP协议使用此类型

·3：SOCK_RAW，RAW模式的通信方式

·N/A：不是上述类型

Protocol

使用TCP socket的协议号，6表示运用TCP协议

Connection info

连接信息，分别为源IPv6地址及端口号、目的IPv6地址及端口号

Inpcb flags

Internet协议控制块中的标记，标记的取值有：

·INP_RECVOPTS：接收传入的IPv6选项

·INP_RECVRETOPTS：接收回应的IPv6选项

·INP_RECVDSTADDR：接收目的IPv6地址

·INP_HDRINCL：用户提供整个IPv6头

·INP_REUSEADDR：重复使用地址

·INP_REUSEPORT：重复使用端口号

·INP_ANONPORT：用户未指定端口

·INP_PROTOCOL_PACKET：标识报文为协议报文

·INP_RCVVLANID：接收报文的VLAN ID，仅UDP和RawIP支持

·IN6P_IPV6_V6ONLY：仅支持IPv6协议栈

·IN6P_PKTINFO：接收报文的源地址和入接口

·IN6P_HOPLIMIT：接收报文hoplimit

·IN6P_HOPOPTS：接收报文的逐跳扩展头信息

·IN6P_DSTOPTS：接收报文的目的扩展头信息

·IN6P_RTHDR：接收报文的路由扩展头信息

·IN6P_RTHDRDSTOPTS：接收报文的路由头前的目的扩展头信息

·IN6P_TCLASS：接收报文的优先级信息

·IN6P_AUTOFLOWLABEL：使用随机流标签

·IN6P_RFC2292：使用RFC2292 API

·IN6P_MTU：感知路径MTU的变化，TCP不支持

·INP_RCVMACADDR：接收报文的MAC

·INP_SYNCPCB：阻塞等待inpcb同步

·N/A：不是上述标记

Inpcb extflag

Internet协议控制块中的扩展标记，标记的取值有：

·INP_EXTRCVPVCIDX：接收报文时记录报文的PVC索引

·INP_RCVPWID：接收报文时记录报文的PW ID

·N/A：不是上述标记

Inpcb vflag

Internet协议控制块中的IP版本标记：

·INP_IPV4：运用与IPv4通信

·INP_IPV6：运用与IPv6通信

·INP_IPV6PROTO：运用IPv6协议创建的inpcb

·INP_TIMEWAIT：处于等待状态

·INP_ONESBCAST：发送广播报文

·INP_DROPPED：协议丢弃标志

·INP_SOCKREF：socket强关联

·INP_DONTBLOCK：inpcb同步时不能被阻塞

·N/A：不是上述标记

Hop limit(minimum hop limit)

Internet协议控制块中的跳数限制，括号中为最小跳数限制

Connection state

TCP连接状态，可能的状态如下：

·CLOSED：服务器收到客户端的关闭连接请求回应后所处的状态

·LISTEN：服务器在等待连接请求时所处的状态

·SYN_SENT：客户端发出连接请求等待服务器回应时所处的状态

·SYN_RCVD：服务器收到客户端连接请求时所处的状态

·ESTABLISHED：服务器和客户端双方建立连接并能进行双向数据传递的状态

·CLOSE_WAIT：服务器收到客户端关闭连接请求时所处的状态

·FIN_WAIT_1：客户端发出关闭连接请求等待服务器回应时所处的状态

·CLOSING：连接双方在向对端发出关闭连接请求后等待对端回应过程中收到对端发出的关闭连接请求时所处的状态

·LAST_ACK：服务器向客户端发出关闭连接请求等待回应时所处的状态

·FIN_WAIT_2：客户端收到服务器关闭连接回应后所处的状态

·TIME_WAIT：客户端收到服务器的关闭连接请求后所处的状态

TCP options

TCP的选项类型，有以下几种：

·TF_MD5SIG：使能密钥

·TF_PASSWORD：已经设置密钥

·TF_NODELAY：关闭延时ACK

·TF_NOOPT：TCP不使用选项

·TF_NOPUSH：对写入的最后部分不进行PUSH操作

·TF\_BINDFOREIGNADDR：绑定对端IP地址

·TF_NSR：使能TCP NSR

·TF_REQ_SCALE：使能窗口缩放因子选项

·TF_REQ_TSTMP：使能事件戳选项

·TF_SACK_PERMIT：使能选择性ACK选项

NSR state

TCP连接NSR状态，可能的状态如下：

·CLOSED：关闭（初始）状态

·CLOSING：连接待关闭状态

·ENABLED：使能备份功能状态

·OPEN：连接开始同步状态

·PENDING： 连接判定状态

·READY：连接备份就绪状态

·SMOOTH：连接平滑状态

角色：M表示主连接、S表示备份连接

Send VRF

发送实例

Receive VRF

接收实例

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 udp**

------------------------------------------------------------------------

**[display ipv6 udp**]命令用来显示IPv6 UDP连接摘要信息。

【命令】

集中式设备：

**[display ipv6 udp**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 udp** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 udp** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板的IPv6 UDP连接摘要信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 UDP连接摘要信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6 UDP连接摘要信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6 UDP连接摘要信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6 UDP连接摘要信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6 UDP连接摘要信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6 UDP连接摘要信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 UDP连接摘要信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 UDP连接摘要信息。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 UDP连接摘要信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6 UDP连接摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以用来查看IPv6 UDP连接摘要信息，包括本端IPv6地址及端口号、对端IPv6地址及端口号等信息。

【举例】

\# 显示IPv6 UDP连接摘要信息。（分布式设备－IRF模式）

\<Sysname\> display ipv6 udp

 LAddr-\>port         FAddr-\>port         Chassis  Slot  CPU PCB

 2001:2002:2003:2   3001:3002:3003:3   1         1      0   0x000000000000c387

 004:2005:2006:20   004:3005:3006:30

 07:2008-\>1200      07:3008-\>1200

 2001::1-\>23         2001::5-\>1284       1         2      0   0x0000000000000008

 2003::1-\>25         2001::2-\>1283       1         3      0   0x0000000000000009

表1-22 display ipv6 udp命令显示信息描述表

字段

描述

LAddr-\>port

本端IPv6地址及端口号

FAddr-\>port

对端IPv6地址及端口号

Chassis

设备在IRF中的成员编号

Slot

单板所在的槽位号

CPU

节点所在的CPU编号

PCB

协议控制块索引

**IPv6基础 \-- IPv6基础配置命令 \-- display ipv6 udp verbose**

------------------------------------------------------------------------

**[display ipv6 udp verbose**]命令用来显示IPv6 UDP连接详细信息。

【命令】

集中式设备：

**[display ipv6 udp verbose** [ **pcb** *pcb-index* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 udp verbose** [ **slot** *slot-number* [ **cpu** *cpu-number*   **pcb** *pcb-index*  ]]]

分布式设备－IRF模式：

**[display ipv6 udp verbose** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*   **pcb** *pcb-index*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pcb** *pcb-index*]：显示指定协议控制块索引的IPv6 UDP连接详细信息。*pcb-index*表示协议控制块索引，取值范围请以设备的实际情况为准。

**[slot** *slot-number*]：显示指定单板的IPv6 UDP连接详细信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 UDP连接详细信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6 UDP连接详细信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6 UDP连接详细信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6 UDP连接详细信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6 UDP连接详细信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6 UDP连接详细信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 UDP连接详细信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 UDP连接详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6 UDP连接详细信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的IPv6 UDP连接详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以用来查看IPv6 UDP连接详细信息，包括socket的创建者、状态、选项、类型、使用的协议号等，以及IPv6 UDP连接的源IPv6地址及端口号、目的IPv6地址及端口号等信息。

【举例】

\# 显示IPv6 UDP连接详细信息。（集中式设备）

\<Sysname\> display ipv6 udp verbose

Total UDP socket number: 1

 Creator: sock_test_mips[250]

 State: N/A

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 41600 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A

 Type: 2

 Protocol: 17

 Connection info: src = ::-\>69, dst = ::-\>0

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Send VRF: 0xffff

 Receive VRF: 0xffff

\# 显示IPv6 UDP连接详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display ipv6 udp verbose

Total UDP socket number: 1

 Slot: 6 Cpu: 0

 Creator: sock_test_mips[250]

 State: N/A

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 41600 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A

 Type: 2

 Protocol: 17

 Connection info: src = ::-\>69, dst = ::-\>0

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Send VRF: 0xffff

 Receive VRF: 0xffff

\# 显示IPv6 UDP连接详细信息。（分布式设备－IRF模式）

\<Sysname\> display ipv6 udp verbose

Total UDP socket number: 1

 Chassis: 2 Slot: 6 Cpu: 0

 Creator: sock_test_mips[250]

 State: N/A

 Options: N/A

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 41600 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 9216 / 512 / N/A

 Type: 2

 Protocol: 17

 Connection info: src = ::-\>69, dst = ::-\>0

 Inpcb flags: N/A

 Inpcb extflag: N/A

 Inpcb vflag: INP_IPV6

 Hop limit: 255 (minimum hop limit: 0)

 Send VRF: 0xffff

 Receive VRF: 0xffff

表1-23 {.FigureDescriptionChar}display ipv6 udp verbose命令显示信息描述表{.FigureDescriptionChar}

字段

描述

Total UDP socket number

IPv6 UDP socket总数

Chassis

设备在IRF中的成员编号（分布式设备－IRF模式）

Slot

单板所在的槽位号（分布式设备－独立运行模式/分布式设备－IRF模式）

Slot

设备在IRF中的成员编号（集中式IRF设备）

Cpu

节点所在的CPU编号

Creator

创建socket的任务名称，括号中为创建者的进程号

State

socket的状态，可能的状态如下：

·NOFDREF：用户已经关闭

·ISCONNECTED：连接已经建立

·ISCONNECTING：正在建立连接

·ISDISCONNECTING：正在断开连接

·ASYNC：异步方式

·ISDISCONNECTED：连接已经断开

·PROTOREF：协议强关联

·N/A：不处于上述状态

Options

socket的选项，有以下几种：

·SO_DEBUG：记录套接字的调试信息

·SO_ACCEPTCONN：server端监听连接请求

·SO_REUSEADDR：允许本地地址重复使用

·SO_KEEPALIVE：协议需要查询空闲的连接

·SO_DONTROUTE：设置不查路由表，由于目的地址是直连网络的情况

·SO_BROADCAST：套接字支持广播报文

·SO_LINGER：套接字关闭但仍发送剩余数据

·SO_OOBINLINE：带外数据采用内联方式存储

·SO_REUSEPORT：允许本地端口重复使用

·SO_TIMESTAMP：入报文记录时间戳，只对非连接的协议有效，时间精确到毫秒

·SO_NOSIGPIPE：socket不能发送数据导致返回失败时不创建SIGPIPE

·SO_TIMESTAMPNS：和时戳选项功能类似，时间可以精确到纳秒

·SO_KEEPALIVETIME：设置空闲探测时间，TCP支持此选项

·SO_FILTER：设置报文过滤条件，OSI Socket和RawIP支持此选项

·N/A：没有设置选项

Error

影响socket连接的错误码

Receiving buffer(cc/hiwat/lowat/state)

接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态

状态的取值有：

·CANTSENDMORE：不能发送数据到对端

·CANTRCVMORE：不能从对端接收数据

·RCVATMARK：接收标记

·N/A：不处于上述状态

Sending buffer(cc/hiwat/lowat/state)

发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态

状态的取值有：

·CANTSENDMORE：不能发送数据到对端

·CANTRCVMORE：不能从对端接收数据

·RCVATMARK：接收标记

·N/A：不处于上述状态

Type

使用的socket类型，类型的取值有：

·1：SOCK_STREAM，流模式，提供可靠的字节流。TCP协议使用此类型

·2：SOCK_DGRAM，数据报模式的通信。UDP协议使用此类型

·3：SOCK_RAW，RAW模式的通信方式

·N/A：不是上述类型

Protocol

使用UDP socket的协议号，17表示运用UDP协议

Connection info

连接信息，分别为源IPv6地址及端口号、目的IPv6地址及端口号

Inpcb flags

Internet协议控制块中的标记，标记的取值有：

·INP_RECVOPTS：接收传入的IPv6选项

·INP_RECVRETOPTS：接收回应的IPv6选项

·INP_RECVDSTADDR：接收目的IPv6地址

·INP_HDRINCL：用户提供整个IPv6头

·INP_REUSEADDR：重复使用地址

·INP_REUSEPORT：重复使用端口号

·INP_ANONPORT：用户未指定端口

·INP_PROTOCOL_PACKET：标识报文为协议报文

·INP_RCVVLANID：接收报文的VLAN ID，仅UDP和RawIP支持

·IN6P_IPV6_V6ONLY：仅支持IPv6协议栈

·IN6P_PKTINFO：接收报文的源地址和入接口

·IN6P_HOPLIMIT：接收报文hoplimit

·IN6P_HOPOPTS：接收报文的逐跳扩展头信息

·IN6P_DSTOPTS：接收报文的目的扩展头信息

·IN6P_RTHDR：接收报文的路由扩展头信息

·IN6P_RTHDRDSTOPTS：接收报文的路由头前的目的扩展头信息

·IN6P_TCLASS：接收报文的优先级信息

·IN6P_AUTOFLOWLABEL：使用随机流标签

·IN6P_RFC2292：使用RFC2292 API

·IN6P_MTU：感知路径MTU的变化，TCP不支持

·INP_RCVMACADDR：接收报文的MAC

·INP_SYNCPCB：阻塞等待inpcb同步

·N/A：不是上述标记

Inpcb extflag

Internet协议控制块中的扩展标记，标记的取值有：

·INP_EXTRCVPVCIDX：接收报文时记录报文的PVC索引

·INP_RCVPWID：接收报文时记录报文的PW ID

·N/A：不是上述标记

Inpcb vflag

Internet协议控制块中的IP版本标记，标记的取值有：

·INP_IPV4：运用与IPv4通信

·INP_IPV6：运用与IPv6通信

·INP_IPV6PROTO：运用IPv6协议创建的inpcb

·INP_TIMEWAIT：处于等待状态

·INP_ONESBCAST：发送广播报文

·INP_DROPPED：协议丢弃标志

·INP_SOCKREF：socket强关联

·INP_DONTBLOCK：inpcb同步时不能被阻塞

·N/A：不是上述标记

Hop limit(minimum hop limit)

Internet协议控制块中的跳数限制，括号中为最小跳数限制

Send VRF

发送实例

Receive VRF

接收实例

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address**

------------------------------------------------------------------------

**[ipv6 address**]命令用来手工配置接口的IPv6全球单播地址。

**[undo ipv6 address**]命令用来删除接口的IPv6地址。

【命令】

**[ipv6 address**[ { *ipv6-address prefix-length* \| *ipv6-address***/***prefix-length* }]]

**[undo ipv6 address**[[ *ipv6-address prefix-length* \| *ipv6-address***/***prefix-length* ]]]

【缺省情况】

接口上没有配置IPv6全球单播地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：IPv6地址。

*[prefix-length*]：前缀长度，取值范围为1～128。

【使用指导】

IPv6全球单播地址等同于IPv4公网地址，提供给网络服务提供商。这种类型的地址允许路由前缀的聚合，从而限制了全球路由表项的数量。

需要注意的是，**undo ipv6 address**命令不带参数则删除该接口的所有IPv6地址。

【举例】

·路由应用

\# 指定GigabitEthernet1/0/1接口的IPv6全球单播地址为2001::1，前缀长度为64。

方法一：

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address 2001::1/64

方法二：

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address 2001::1 64

·交换应用

\# 指定VLAN接口100的IPv6全球单播地址为2001::1，前缀长度为64。

方法一：

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address 2001::1/64

方法二：

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address 2001::1 64

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address anycast**

------------------------------------------------------------------------

**[ipv6 address anycast**]命令用来给接口配置IPv6任播地址。

**[undo ipv6 address anycast**]命令用来删除接口上已配置的IPv6任播地址。

【命令】

**[ipv6 address****[{ *ipv6-address prefix-length* \| *ipv6-address/prefix-length* } **anycast**]]

**[undo ipv6 address****[{ *ipv6-address prefix-length* \| *ipv6-address/prefix-length* } **anycast**]]

【缺省情况】

接口上没有配置IPv6任播地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-addres*s]：指定IPv6任播地址。

*[prefix-length*]：前缀长度，取值范围为1～128。

【举例】

·路由应用

\# 指定GigabitEthernet1/0/1接口的IPv6任播地址为2001::1，前缀长度为64。

方法一：

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address 2001::1/64 anycast

方法二：

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address 2001::1 64 anycast

·交换应用

\# 指定VLAN接口100的IPv6任播地址为2001::1，前缀长度为64。

方法一：

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address 2001::1/64 anycast

方法二：

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address 2001::1 64 anycast

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address auto**

------------------------------------------------------------------------

![说明](IPv6基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 address auto**]命令用来使能无状态地址自动配置功能，使接口通过无状态自动配置方式生成全球单播地址。

**[undo ipv6 address auto**]命令用来关闭无状态地址自动配置功能。

【命令】

**[ipv6 address auto**]

**[undo ipv6 address auto**]

【缺省情况】

无状态地址自动配置功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过无状态自动配置方式生成全球单播地址时，会自动生成链路本地地址，生成的全球单播地址和链路本地地址可以通过执行**undo ipv6 address auto**命令或**undo ipv6 address**命令删除。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1通过无状态自动配置方式生成全球单播地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address auto

·交换应用

\# 配置VLAN接口100通过无状态自动配置方式生成全球单播地址。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address auto

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address auto link-local**

------------------------------------------------------------------------

**[ipv6 address auto link-local**]命令用来配置系统自动为接口生成链路本地地址。

**[undo ipv6 address auto link-local**]命令用来删除接口自动生成的链路本地地址。

【命令】

**[ipv6 address auto link-local**]

**[undo ipv6 address auto link-local**]

【缺省情况】

接口上没有链路本地地址。当接口配置了IPv6全球单播地址后，会自动生成链路本地地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

链路本地地址用于邻居发现协议和无状态自动配置中链路本地上节点之间的通信。使用链路本地地址作为源或目的地址的数据报文不会被转发到其他链路上。

需要注意的是：

·接口配置了IPv6全球单播地址后，所自动生成的链路本地地址与采用**ipv6 address auto link-local**命令生成的链路本地地址相同。

·**undo ipv6 address auto link-local**命令只能删除使用**ipv6 address auto link-local**命令生成的链路本地地址。即如果此时接口已配置了IPv6全球单播地址，则接口仍有链路本地地址；如果此时接口没有配置任何IPv6全球单播地址，则接口没有链路本地地址。

·配置链路本地地址时，手工指定方式的优先级高于自动生成方式。即如果先采用自动生成方式，之后手工指定，则手工指定的地址会覆盖自动生成的地址；如果先手工指定，之后采用自动生成的方式，则自动配置不生效，接口的链路本地地址仍是手工指定的。此时，如果删除手工指定的地址，则自动生成的链路本地地址会生效。关于手工指定方式的介绍请参见命令**ipv6 address link-local**。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口自动生成链路本地地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address auto link-local

·交换应用

\# 配置VLAN接口100自动生成链路本地地址。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address auto link-local

【相关命令】

·**ipv6 address link-local**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address eui-64**

------------------------------------------------------------------------

**[ipv6 address** **eui-64**]命令用来给接口配置EUI-64格式的全球单播地址。

**[undo ipv6 address eui-64**]命令用来删除接口上已配置的EUI-64格式的全球单播地址。

【命令】

**[ipv6 address**[ { *ipv6-address prefix-length* \| *ipv6-address***/***prefix-length* } **eui-64**]]

**[undo ipv6 address**[ [ *ipv6-address prefix-length* \| *ipv6-address***/***prefix-length* ] **eui-64**]]

【缺省情况】

接口上没有配置EUI-64格式的全球单播地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address***/***prefix-length*]：IPv6地址/前缀长度，共同指定采用EUI-64格式形成的IPv6地址的前缀。前缀长度*prefix-length*的取值范围为1～64。

【使用指导】

EUI-64格式的地址由指定的地址前缀和自动产生的接口标识符生成，最终生成的地址可以通过**display ipv6 interface**命令查看。

需要注意的是，在配置EUI-64地址时前缀长度取值不能大于64。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口采用EUI-64格式形成IPv6地址，其地址前缀与2001::1/64的前缀相同，接口标识符由设备的MAC地址生成。

方法一：

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address 2001::1/64 eui-64

方法二：

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address 2001::1 64 eui-64

·交换应用

\# 配置VLAN接口100采用EUI-64格式形成IPv6地址，其地址前缀与2001::1/64的前缀相同，接口标识符由设备的MAC地址生成。

方法一：

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address 2001::1/64 eui-64

方法二：

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address 2001::1 64 eui-64

【相关命令】

·**display ipv6 interface**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 address link-local**

------------------------------------------------------------------------

**[ipv6 address link-local**]命令用来手动配置指定接口的链路本地地址。

**[undo ipv6 address link-local**]命令用来删除接口上手动配置的链路本地地址。

【命令】

**[ipv6 address** *ipv6-address* **link-local**]

**[undo ipv6 address ***ipv6-address* **link-local**]

【缺省情况】

接口上没有手动配置的链路本地地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：IPv6链路本地地址，地址前面10位必须为1111111010（二进制标识），即地址最前面的一组十六进制数为FE80～FEBF。

【使用指导】

配置链路本地地址时，手工指定方式的优先级高于自动生成方式。即如果先采用自动生成方式，之后手工指定，则手工指定的地址会覆盖自动生成的地址；如果先手工指定，之后采用自动生成的方式，则自动配置不生效，接口的链路本地地址仍是手工指定的。此时，如果删除手工指定的地址，则自动生成的链路本地地址会生效。关于自动生成方式的介绍请参见命令**ipv6 address auto link-local**。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口的链路本地地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address fe80::1 link-local

·交换应用

\# 配置VLAN接口100的链路本地地址。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address fe80::1 link-local

【相关命令】

·**ipv6 address auto link-local**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 bandwidth-based-sharing**

------------------------------------------------------------------------

**[ipv6 bandwidth-based-sharing**]命令用来配置IPv6基于带宽的负载分担功能。

**[undo ipv6 bandwidth-based-sharing**]命令用来关闭IPv6基于带宽的负载分担功能。

【命令】

**[ipv6 bandwidth-based-sharing**]

**[undo ipv6 bandwidth-based-sharing**]

【缺省情况】

IPv6基于带宽的负载分担功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在设备上配置了IPv6基于带宽的负载分担后，如果IPv6报文转发时查到多个出接口/下一跳，则按照接口的带宽值计算出各个接口应该分配的报文比例，然后按照带宽比例对报文进行转发。

支持负载分担协议（如LISP）的设备，无论是否配置了负载分担命令，负载分担比例都以协议定义的负载分担比例为准。

【举例】

\# 配置IPv6基于带宽的负载分担功能。

\<Sysname\> system-view

Sysname ipv6 bandwidth-based-sharing

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 hop-limit**

------------------------------------------------------------------------

**[ipv6 hop-limit**]命令用来配置设备的跳数限制。

**[undo ipv6 hop-limit**]命令用来恢复缺省情况。

【命令】

**[ipv6 hop-limit** *value*]

**[undo ipv6 hop-limit**]

【缺省情况】

设备的跳数限制为64跳。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：跳数值，取值范围为1～255。

【使用指导】

设备的跳数限制有以下两个作用：

·决定了设备发送的IPv6数据报文的跳数，即IPv6数据报文的Hop Limit字段的值。

·设备发送的RA消息中将携带此处配置的跳数限制值。收到该RA消息之后，主机在发送IPv6报文时，将使用该跳数值填充IPv6报文头中的Hop Limit字段。配置命令**ipv6 nd ra hop-limit unspecified**可以配置RA消息中不指定跳数限制。

【举例】

\# 配置设备的跳数限制为100跳。

\<Sysname\> system-view

Sysname ipv6 hop-limit 100

【相关命令】

·**ipv6 nd hop-limit******unspecified**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 hoplimit-expires enable**

------------------------------------------------------------------------

**[ipv6 hoplimit-expires enable**]命令用来开启设备的ICMPv6超时报文的发送功能。

**[undo ipv6 hoplimit-expires enable**]命令用来关闭设备的ICMPv6超时报文的发送功能。

【命令】

**[ipv6 hoplimit-expires enable**]

**[undo ipv6 hoplimit-expires enable**]

【缺省情况】

ICMPv6超时报文发送功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

ICMPv6超时报文发送功能是在设备收到IPv6数据报文后，如果发生超时（Hop limit超时或者重组超时）差错，则将报文丢弃并给源端发送ICMPv6超时差错报文。

如果接收到大量需要发送ICMPv6差错报文的恶意攻击报文，设备会因为处理大量该类报文而导致性能降低。为了避免该现象发生，可以关闭设备的ICMPv6超时报文发送功能，从而减少网络流量、防止遭到恶意攻击。

需要注意的是，关闭ICMPv6超时报文发送功能后，设备不会再发送"Hop-Limit超时"ICMPv6差错报文，但"重组超时"ICMPv6差错报文仍会正常发送。

【举例】

\# 关闭设备的ICMPv6超时报文发送功能。

\<Sysname\> system-view

Sysname undo ipv6 hoplimit-expires enable

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 icmpv6 error-interval**

------------------------------------------------------------------------

**[ipv6 icmpv6 error-interval**]命令用来配置发送ICMPv6差错报文对应的令牌桶容量和令牌刷新周期。

**[undo ipv6 icmpv6 error-interval**]命令用来恢复缺省情况。

【命令】

**[ipv6 icmpv6 error-interval**]*milliseconds *\*[bucketsize *]

**[undo ipv6 icmpv6 error-interval**]

【缺省情况】

令牌桶容量为10，令牌刷新周期为100毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[milliseconds*]：令牌刷新周期，取值范围0\~2147483647，缺省值为100，单位为毫秒。取值为0时，表示不限制ICMPv6差错报文的发送。

*[bucketsize*]：令牌桶中容纳的令牌数，取值范围1\~200，缺省值为10。

【使用指导】

如果网络中短时间内发送的ICMPv6差错报文过多，将可能导致网络拥塞。为了避免这种情况，用户可以控制在指定时间内发送ICMPv6差错报文的最大个数，目前采用令牌桶算法来实现。

用户可以设置令牌桶的容量，即令牌桶中可以同时容纳的令牌数；同时可以设置令牌桶的刷新周期，即每隔多长时间发放一个令牌到令牌桶中，直到令牌桶中的令牌数达到配置的容量。一个令牌表示允许发送一个ICMPv6差错报文，每当发送一个ICMPv6差错报文，则令牌桶中减少一个令牌。如果连续发送的ICMPv6差错报文超过了令牌桶的容量，则后续的ICMPv6差错报文将不能被发送出去，直到按照所设置的刷新频率将新的令牌放入令牌桶中。

【举例】

\# 配置设备发送ICMPv6差错报文对应的令牌桶容量为40，令牌刷新时间为200毫秒。

\<Sysname\> system-view

Sysname ipv6 icmpv6 error-interval 200 40

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 icmpv6 multicast-echo-reply enable**

------------------------------------------------------------------------

**[ipv6 icmpv6 multicast-echo-reply enable**]命令用来配置允许设备回复组播形式的Echo request报文。

**[undo ipv6 icmpv6 multicast-echo-reply enable**]命令用来配置不允许设备回复组播形式的Echo request报文。

【命令】

**[ipv6 icmpv6 multicast-echo-reply enable**]

**[undo ipv6 icmpv6 multicast-echo-reply enable**]

【缺省情况】

不允许设备回复组播形式的Echo request报文。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果主机B允许回复组播形式的Echo request报文，则主机A可以构造目的地址为组播地址、源地址为主机B的Echo request报文，使该组播组中所有的主机都向主机B发送Echo reply报文，从而达到攻击主机B的目的。因此，为了避免主机利用设备达到攻击的目的，缺省情况下，不允许设备回复组播形式的Echo request报文。

但在某些应用场景下，可能需要使用组播形式的Echo request报文来获取信息，此时可以配置允许设备回复组播形式的Echo request报文。

【举例】

\# 配置允许设备回复组播形式的Echo request报文。

\<Sysname\> system-view

Sysname ipv6 icmpv6 multicast-echo-reply enable

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 icmpv6 source**

------------------------------------------------------------------------

**[ipv6 icmpv6 source**]命令用来配置ICMPv6报文指定源地址功能。

**[undo ipv6 icmpv6 source**]命令用来关闭ICMPv6报文指定源地址功能。

【命令】

**[ipv6 icmpv6 source ** **vpn-instance** *vpn-instance-name* ] *ipv6-address*

**[undo ipv6 icmpv6 source ** **vpn-instance** *vpn-instance-name* ]

【缺省情况】

ICMPv6报文指定源地址功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定地址所在的VPN实例。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。指定的VPN实例必须已经存在。如果不指定本参数，则表示公网内的IPv6地址。

*[ipv6-address*]：表示设备发送ICMPv6报文时指定的源地址。

【使用指导】

在网络中IPv6地址配置较多的情况下，收到ICMPv6报文时，用户很难根据报文的源IPv6地址判断报文来自哪台设备。为了简化这一判断过程，可以配置ICMPv6报文指定源地址功能。用可配置特定地址（如环回口地址）为ICMPv6报文的源地址，可以简化判断。

设备发送ICMPv6差错报文（TTL超时、报文过大、端口不可达和参数错误等）和ping echo request报文时，都可以通过上述命令指定报文的源地址。

【举例】

\# 配置设备发送ICMPv6报文时指定的源地址为1::1。

\<Sysname\> system-view

Sysname ipv6 icmpv6 source 1::1

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 mtu**

------------------------------------------------------------------------

**[ipv6 mtu**]命令用来配置接口上发送IPv6报文的MTU。

**[undo ipv6 mtu**]命令用来恢复缺省情况。

【命令】

**[ipv6 mtu**] *mtu-size*

**[undo ipv6 mtu**]

【缺省情况】

没有配置接口MTU。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mtu-size*]：接口MTU的大小，取值范围为1280～10240，单位为字节。

【使用指导】

由于IPv6路由器不支持对报文进行分片，当路由器接口收到一个报文后，如果发现报文长度比转发接口的MTU值大，则会将其丢弃；同时将转发接口的MTU值通过ICMPv6报文的"Packet Too Big"消息发给源端主机，源端主机以该值重新发送IPv6报文。为减少报文被丢弃带来的额外流量开销，需要根据实际组网环境设置合适的接口MTU值。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口上发送IPv6报文的MTU为1280字节。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 mtu 1280

·交换应用

\# 配置VLAN接口100上发送IPv6报文的MTU为1280字节。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 mtu 1280

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd autoconfig managed-address-flag**

------------------------------------------------------------------------

**[ipv6 nd autoconfig managed-address-flag**]命令用来配置被管理地址的配置标志位为1，即主机通过有状态自动配置（例如DHCPv6服务器）获取IPv6地址。

**[undo** **ipv6 nd autoconfig managed-address-flag**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd autoconfig managed-address-flag**]

**[undo ipv6 nd autoconfig managed-address-flag**]

【缺省情况】

被管理地址的配置标志位为0，即主机通过无状态自动配置获取IPv6地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

被管理地址配置标志位（M flag）用于确定主机是否采用有状态自动配置获取IPv6地址。

如果设置该标志位为1，主机将通过有状态自动配置（例如DHCPv6服务器）来获取IPv6地址；否则，将通过无状态自动配置获取IPv6地址，即根据自己的链路层地址及路由器发布的前缀信息生成IPv6地址。

【举例】

·路由应用

\# 配置主机通过有状态自动配置获取IPv6地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd autoconfig managed-address-flag

·交换应用

\# 配置主机通过有状态自动配置获取IPv6地址。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd autoconfig managed-address-flag

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd autoconfig other-flag**

------------------------------------------------------------------------

**[ipv6 nd autoconfig other-flag**]命令用来配置其他信息配置标志位为1，即主机通过有状态自动配置（例如DHCPv6服务器）获取除IPv6地址外的其他信息。

**[undo ipv6 nd autoconfig other-flag**]命令用来恢复该缺省情况。

【命令】

**[ipv6 nd autoconfig other-flag**]

**[undo ipv6 nd autoconfig other-flag**]

【缺省情况】

其他信息配置标志位为0，即主机通过无状态自动配置获取其他信息。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

其他信息配置标志位（O flag）用于确定主机是否采用有状态自动配置获取除IPv6地址外的其他信息。

如果设置该标志位为1，主机将通过有状态自动配置（例如DHCPv6服务器）来获取除IPv6地址外的其他信息；否则，将通过无状态自动配置获取其他信息。

【举例】

·路由应用

\# 配置主机通过无状态自动配置来获取除IPv6地址外的其他信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo ipv6 nd autoconfig other-flag

·交换应用

\# 配置主机通过无状态自动配置来获取除IPv6地址外的其他信息。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 undo ipv6 nd autoconfig other-flag

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd dad attempts**

------------------------------------------------------------------------

**[ipv6 nd dad attempts**]命令用来配置进行重复地址检测时发送邻居请求消息的次数。

**[undo ipv6 nd dad attempts**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd dad attempts ***value*]

**[undo ipv6 nd dad attempts**]

【缺省情况】

进行重复地址检测时发送邻居请求消息的次数为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：进行重复地址检测时发送邻居请求消息的次数，取值范围为0～600。当配置为0时，表示禁止重复地址检测。

【使用指导】

接口获得IPv6地址后，将发送邻居请求消息进行重复地址检测，如果在指定的时间内（通过**ipv6 nd ns retrans-timer**命令配置）没有收到响应，则继续发送邻居请求消息，当发送的次数达到所设置的次数后，仍未收到响应，则认为该地址可用。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口进行重复地址检测时发送邻居请求消息的次数为20次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd dad attempts 20

·交换应用

\# 配置VLAN接口100进行重复地址检测时发送邻居请求消息的次数为20次。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd dad attempts 20

【相关命令】

·**display ipv6 interface**

·**ipv6 nd ns retrans-timer**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd mode uni**

------------------------------------------------------------------------

![说明](IPv6基础命令.files/image001.png)

本特性支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 nd mode uni**]命令用来配置接口为用户侧接口。

**[undo ipv6 nd mode**]命令用来恢复接口为网络侧接口。

【命令】

**[ipv6 nd mode uni**]

**[undo ipv6 nd mode**]

【缺省情况】

接口为网络侧接口。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口为用户侧接口的情况，说明此接口的邻居都为终端主机。对于此种接口上学习到的ND表项，驱动软件可以不为其分配下一跳资源。

接口角色为网络侧接口的情况，说明此接口的邻居可能是转发报文的下一跳，因此学习在此接口上的ND表项，驱动软件需要为其分配下一跳资源。

通过实际使用情况，正确配置接口的工作模式，可以适当的节省硬件资源。

【举例】

\# 配置VLAN接口2为用户侧接口。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 ipv6 nd mode uni

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ns retrans-timer**

------------------------------------------------------------------------

**[ipv6 nd ns retrans-timer**]命令用来配置邻居请求消息的重传时间间隔。

**[undo ipv6 nd ns retrans-timer**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd ns retrans-timer**] *value*

**[undo ipv6 nd ns retrans-timer**]

【缺省情况】

接口发送NS消息的时间间隔为1000毫秒；接口发布的RA消息中Retrans Timer字段的值为0，即不对主机进行指定。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：NS消息重传时间间隔，取值范围为1000～4294967295，单位为毫秒。

【使用指导】

设备发送NS消息后，如果未在指定的邻居请求消息重传时间间隔内收到响应，则会重新发送NS消息。

本命令配置的时间间隔既用于本接口发送NS消息的时间间隔，同时也作为本接口发布的RA消息中Retrans Timer字段的值。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口发送NS消息的时间间隔为10000毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd ns retrans-timer 10000

·交换应用

\# 配置VLAN接口100发送NS消息的时间间隔为10000毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd ns retrans-timer 10000

【相关命令】

·**display ipv6 interface**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd nud reachable-time**

------------------------------------------------------------------------

**[ipv6 nd nud reachable-time**]命令用来配置接口保持邻居可达状态的时间。

**[undo ipv6 nd nud reachable-time**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd nud reachable-time ***value*]

**[undo ipv6 nd nud reachable-time**]

【缺省情况】

接口保持邻居可达状态的时间为30000毫秒；接口发布的RA消息中Reachable Timer字段的值为0，即不对主机进行指定。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：保持邻居可达状态的时间，取值范围为1～3600000，单位为毫秒。

【使用指导】

当通过邻居可达性检测确认邻居可达后，在所设置的接口保持邻居可达状态的时间内，设备认为邻居可达；超过设置的时间后，如果需要向邻居发送报文，会重新确认邻居是否可达。

本命令配置的时间既用于本接口保持邻居可达状态的时间，同时也作为本接口发布的RA消息中Reachable Timer字段的值。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口上保持邻居可达状态的时间为10000毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd nud reachable-time 10000

·交换应用

\# 配置VLAN接口100上保持邻居可达状态的时间为10000毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd nud reachable-time 10000

【相关命令】

·**display ipv6 interface**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd snooping enable global**

------------------------------------------------------------------------

**[ipv6 nd snooping enable global**]命令用来开启学习表项地址类型为全球单播地址的ND Snooping表项的功能。

**[undo ipv6 nd snooping enable global**]命令用来关闭学习表项地址类型为全球单播地址的ND Snooping表项的功能。

【命令】

**[ipv6 nd snooping enable global**]

**[undo ipv6 nd snooping enable global**]

【缺省情况】

学习表项地址类型为全球单播地址的ND Snooping表项的功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在VLAN 2下开启学习表项地址类型为全球单播地址的ND Snooping表项的功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 ipv6 nd snooping enable global

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd snooping enable link-local**

------------------------------------------------------------------------

**[ipv6 nd snooping enable link-local**]命令用来开启学习表项地址类型为链路本地地址的ND Snooping表项的功能。

**[undo ipv6 nd snooping enable link-local**]命令用来关闭学习表项地址类型为链路本地地址的ND Snooping表项的功能。

【命令】

**[ipv6 nd snooping enable link-local**]

**[undo ipv6 nd snooping enable link-local**]

【缺省情况】

学习表项地址类型为链路本地地址的ND Snooping表项的功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在VLAN 2下开启学习表项地址类型为链路本地地址的ND Snooping表项的功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 ipv6 nd snooping enable link-local

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd snooping glean source**

------------------------------------------------------------------------

**[ipv6 nd snooping glean source**]命令用来开启通过IPv6数据报文学习ND Snooping表项的功能。

**[undo ipv6 nd snooping glean source**]命令用来关闭通过IPv6数据报文学习ND Snooping表项的功能。

【命令】

**[ipv6 nd snooping glean source**]

**[undo ipv6 nd snooping glean source**]

【缺省情况】

通过数据报文学习ND Snooping表项的功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·至少配置了**ipv6 nd snooping enable global**和**ipv6 nd snooping enable link-local**这两条命令其中之一后，本功能才能生效。

·本命令开启后，VLAN内非信任口必须开启IP Source Guard功能，否则会导致该口的报文不能正常转发。

【举例】

\# 开启VLAN 2的接口通过IPv6数据报文学习ND Snooping表项的功能。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 ipv6 nd snooping glean source

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd snooping max-learning-num**

------------------------------------------------------------------------

**[ipv6 nd snooping max-learning-num ***number*]命令用来配置接口下学习ND Snooping表项的最大数目。

**[undo ipv6 nd snooping max-learning-num**]命令用来取消接口下学习ND Snooping表项最大数目的限制。

【命令】

**[ipv6 nd snooping max-learning-num ***number*]

**[undo ipv6 nd snooping max-learning-num**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置接口GigabitEthernet1/0/1学习ND Snooping表项的最大数目为64。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-Gigabitethernet1/0/1 ipv6 nd snooping max-learning-num 64

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra halt**

------------------------------------------------------------------------

**[ipv6 nd ra halt**]命令用来抑制RA消息的发布。

**[undo ipv6 nd ra halt**]命令用来取消对RA消息发布的抑制。

【命令】

**[ipv6 nd ra halt**]

**[undo ipv6 nd ra halt**]

【缺省情况】

抑制发布RA消息。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 取消对接口GigabitEthernet1/0/1发布RA消息的抑制。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo ipv6 nd ra halt

·交换应用

\# 取消对VLAN接口100发布RA消息的抑制。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 undo ipv6 nd ra halt

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra hop-limit unspecified**

------------------------------------------------------------------------

**[ipv6 nd ra hop-limit unspecified**]命令用来配置RA消息中不指定跳数限制。

**[undo ipv6 nd ra hop-limit unspecified**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd ra hop-limit unspecified**]

**[undo ipv6 nd ra hop-limit unspecified**]

【缺省情况】

RA消息中发布本设备的跳数限制。本设备的跳数限制默认为64跳。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本设备的跳数限制默认为64跳，可以通过命令**ipv6 hop-limit**进行配置。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口上RA消息中不指定跳数限制。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd ra hop-limit unspecified

·交换应用

\# 配置VLAN接口100上RA消息中不指定跳数限制。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd ra hop-limit unspecified

【相关命令】

·**ipv6 hop-limit**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra interval**

------------------------------------------------------------------------

**[ipv6 nd ra interval**]命令用来配置RA消息发布的最大时间间隔和最小时间间隔。

**[undo ipv6 nd ra interval**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd ra interval** *max-interval-value min-interval-value*]

**[undo ipv6 nd ra interval**]

【缺省情况】

RA消息发布的最大时间间隔为600秒，最小时间间隔为200秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-interval-value*]：指定RA消息发布的最大时间间隔，取值范围是4～1800，单位为秒。

*[min-interval-value*]：指定RA消息发布的最小时间间隔，取值范围是3～（*max-interval-value* \* 3/4），单位为秒。

【使用指导】

RA消息周期性发布时，设备在最大时间间隔与最小时间间隔之间随机选取一个值作为周期性发布RA消息的时间间隔。

需要注意的是，RA消息发布的最大实际间隔应该小于或等于RA消息中路由器的生存时间。

【举例】

·路由应用

\# 设备周期性发布RA消息的最大时间间隔为1000秒，最小时间间隔为700秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd ra interval 1000 700

·交换应用

\# 配置设备周期性发布RA消息的最大时间间隔为1000秒，最小时间间隔为700秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd ra interval 1000 700

【相关命令】

·**ipv6 nd ra router-lifetime**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra no-advlinkmtu**

------------------------------------------------------------------------

**[ipv6 nd ra no-advlinkmtu**]命令用来配置RA消息中不携带MTU选项。

**[undo ipv6 nd ra no-advlinkmtu**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd ra no-advlinkmtu**]

**[undo ipv6 nd ra no-advlinkmtu**]

【缺省情况】

RA消息中携带MTU选项。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

RA消息中携带的MTU选项可以用来发布链路的MTU，用于确保同一链路上的所有节点采用相同的MTU值。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口上RA消息中不携带MTU选项。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd ra no-advlinkmtu

·交换应用

\# 配置VLAN接口100上RA消息中不携带MTU选项。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd ra no-advlinkmtu

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra prefix**

------------------------------------------------------------------------

**[ipv6 nd ra prefix**]命令用来配置RA消息中的前缀信息。

**[undo ipv6 nd ra prefix**]命令用来取消RA消息中前缀信息的配置。

【命令】

**[ipv6 nd ra prefix**[ { *ipv6-prefix* *prefix-length \| ipv6-prefix***/***prefix-length* } *valid-lifetime preferred-lifetime* [ **no-autoconfig** \| **off-link** ] \*]]

**[undo ipv6 nd ra prefix **[{ *ipv6-prefix* *\| ipv6-prefix***/***prefix-length* }]]

【缺省情况】

没有配置RA消息中的前缀信息，此时将使用发送RA消息的接口IPv6地址作为RA中的前缀信息，其手工配置地址的有效生命期是2592000秒（30天），首选生命期是604800（7天）；其他自动分配地址（如DHCPv6分配地址）的有效生命期和首选生命期与地址本身的生命期相同。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-prefix*]：IPv6地址前缀。

*[prefix-length*]：前缀长度。

*[valid-lifetime*]：前缀的有效存活时间，即有效生命期。取值范围为0～4294967295，单位为秒。

*[preferred-lifetime*]：前缀用于无状态地址配置的优选项的存活时间，即首选生命期。取值范围为0～4294967295，单位为秒。*preferred-lifetime*的值要小于等于*valid-lifetime*的值。

**[no-autoconfig**]：指定前缀不用于无状态地址配置。如果不选择该参数，则指定前缀用于无状态地址配置。

**[off-link**]：指定前缀不是该链路上直连可达的。如果不选择该参数，则表示指定前缀是直连可达的。

【使用指导】

在同一链路上的主机收到设备发布的RA消息中后，可以根据RA消息中的前缀信息进行无状态自动配置等操作。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口上RA消息中的前缀信息。

方法一：

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd ra prefix 2001:10::100/64 100 10

方法二：

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd ra prefix 2001:10::100 64 100 10

·交换应用

\# 配置VLAN接口100上RA消息中的前缀信息。

方法一：

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd ra prefix 2001:10::100/64 100 10

方法二：

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd ra prefix 2001:10::100 64 100 10

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd ra router-lifetime**

------------------------------------------------------------------------

**[ipv6 nd ra router-lifetime**]命令用来配置RA消息中路由器的生存时间。

**[undo ipv6 nd ra router-lifetime**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd ra router-lifetime** *value*]

**[undo ipv6 nd ra router-lifetime**]

【缺省情况】

RA消息中路由器的生存时间为1800秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：RA消息中路由器的生存时间，取值范围为0～9000，单位为秒。当配置为0时，表示本设备不作为默认路由器。

【使用指导】

RA消息中路由器的生存时间用于设置发布RA消息的路由器作为主机的默认路由器的时间。主机根据接收到的RA消息中的路由器生存时间参数值，就可以确定是否将发布该RA消息的路由器作为默认路由器。发布RA消息中路由器生存时间为0的路由器不能作为默认路由器。

需要注意的是，RA消息中路由器的生存时间应该大于或等于RA消息的发布时间间隔。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口上RA消息中路由器的生存时间为1000秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd ra router-lifetime 1000

·交换应用

\# 配置VLAN接口100上RA消息中路由器的生存时间为1000秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd ra router-lifetime 1000

【相关命令】

·**ipv6 nd ra interval**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd route-direct advertise**

------------------------------------------------------------------------

**[ipv6 nd route-direct advertise**]命令用来配置ND直连路由通告功能。

**[undo ipv6 route-direct advertise**]命令用来关闭ND直连路由通告功能。

【命令】

**[ipv6 nd route-direct advertise**]

**[undo ipv6 nd route-direct advertise**]

【缺省情况】

ND直连路由通告功能处于关闭状态。

【视图】

L3VE接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在L3VE接口1下配置ND直连路由通告功能。

\<Sysname\> system-view

Sysname interface ve-l3vpn 1

Sysname-VE-L3VPN1 ipv6 nd route-direct advertise

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd router-preference**

------------------------------------------------------------------------

**[ipv6 nd router-preference**]命令用来配置接口下发送的RA消息中的路由器优先级。

**[undo ipv6 nd router-preference**]命令用来恢复缺省情况。

【命令】

**[ipv6 nd router-preference**[ { **high** \| **low** \| **medium** }]]

**[undo ipv6 nd router-preference**]

【缺省情况】

设备发送的RA消息中的路由器优先级为**medium**。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[high**]：设置发布RA的路由器为高优先级。

**[low**]：设置发布RA的路由器为低优先级。

**[medium**]：设置发布RA的路由器为中优先级。

【使用指导】

主机根据接收到的RA消息中的路由器优先级，可以选择优先级最高的路由器作为默认网关。

在路由器的优先级相同的情况下，遵循"先来先用"的原则，优先选择先接收到的RA消息对应的发送路由器作为默认网关。

【举例】

·路由应用

\# 配置GigabitEthernet1/0/1接口下发送的RA消息中的路由优先级为**low**。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 nd router-preference low

·交换应用

\# 配置VLAN接口100下发送的RA消息中的路由优先级为**high**。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 nd router-preference high

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd suppression enable**

------------------------------------------------------------------------

**[ipv6 nd suppression enable**]命令用来开启ND泛洪抑制功能。

**[undo ipv6 nd suppression enable**]命令用来关闭ND泛洪抑制功能。

【命令】

**[ipv6 nd suppression enable**]

**[undo ipv6 nd suppression enable**]

【缺省情况】

ND泛洪抑制功能处于关闭状态。

【视图】

交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置交叉连接视图时，需要先配置L2VPN功能。

【举例】

\# 开启交叉连接组1，交叉连接2下的ND泛洪抑制功能。

\<Sysname\> system-view

Sysname xconnect-group 1

Sysname-xcg-1 connection 2

Sysname-xcg-1-2 ipv6 nd suppression enable

【相关命令】

·**ipv6 nd suppression push interval**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 nd suppression push interval**

------------------------------------------------------------------------

**[ipv6 nd suppression push interval**]命令配置主动推送ND泛洪抑制表项功能，并配置推送时间间隔。

**[undo ipv6 nd suppression push interval**]命令用来关闭设备主动推送ND泛洪抑制表项的功能。

【命令】

**[ipv6 nd suppression push interval ***interval*]

**[undo ipv6 nd suppression push interval**]

【缺省情况】

设备不会主动推送ND泛洪抑制表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：主动推送ND泛洪抑制表项信息的时间间隔，取值范围为1～1440，单位为分钟**。**

【使用指导】

使用**ipv6 nd suppression push interval**命令用来设置主动推送ND泛洪抑制表项信息的时间间隔，如果当前主动推送ND泛洪抑制表项信息的功能未开启，将会同时开启主动推送功能。

【举例】

\# 配置主动推送ND泛洪抑制表项功能，将主动推送ND泛洪抑制表项信息的时间设为2分钟。

\<Sysname\> system-view

Sysnameipv6 nd suppression push interval 2

【相关命令】

·**ipv6 nd suppression enable**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 neighbor**

------------------------------------------------------------------------

**[ipv6 neighbor**]命令用来配置静态邻居表项。

**[undo** **ipv6 neighbor**]命令用来删除静态邻居表项。

【命令】

**[ipv6 neighbor ***ipv6-address mac-address*[ { *vlan-id port-type* *port-number* \| **interface** *interface-type interface-number* } ] **vpn-instance** *vpn-instance-name* ]

**[undo ipv6 neighbor** *ipv6-address interface-type interface-number*]

【缺省情况】

设备上不存在静态邻居表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：静态邻居表项中的IPv6地址。

*[mac-address*]：静态邻居表项中的链路层地址（48位，格式为H-H-H）。

*[vlan-id*]：静态邻居表项所对应的VLAN ID，取值范围为1～4094。

*[port-type* *port-number*]：静态邻居表项所对应的二层端口类型和端口号。

**[interface** *interface-type interface-number*]：静态邻居表项所对应的三层接口类型和接口号。

**[vpn-instance** *vpn-instance-name*]：指定静态邻居表项所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示静态邻居表项属于公网。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

邻居表项保存的是设备在链路范围内的邻居信息，设备邻居表项可以通过邻居请求消息NS及邻居通告消息NA来动态创建，也可以通过手工配置来静态创建。

设备根据邻居节点的IPv6地址和与此邻居节点相连的三层接口号来唯一标识一个静态邻居表项。目前，静态邻居表项有两种配置方式：

·配置本节点的三层接口相连的邻居节点的IPv6地址和链路层地址；

·配置本节点VLAN中的二层端口相连的邻居节点的IPv6地址和链路层地址。

对于VLAN接口，可以采用上述两种方式来配置静态邻居表项：

·采用第一种方式配置静态邻居表项后，该邻居表项处于INCMP状态。设备解析该VLAN下的二层端口信息后，该邻居表项才会进入REACH状态。

·采用第二种方式配置静态邻居表项，需要保证*port-type* *port-number*指定的二层端口属于*vlan-id*指定的VLAN，且该VLAN已经创建了VLAN接口。在配置后，设备会将VLAN所对应的VLAN接口与IPv6地址相对应来唯一标识一个静态邻居表项，并且该表项处于REACH状态。

在删除VLAN接口对应的静态邻居表项时，只需要指定VLAN对应的VLAN接口即可。

当以太网冗余接口的成员接口包含子接口时，不能指定该以太网冗余接口为IPv6静态邻居表项所对应的接口。关于以太网冗余接口的详细介绍，请参见"可靠性配置指导"中的"冗余备份"。

【举例】

\# 配置三层以太网接口GigabitEthernet1/0/1对应的静态邻居表项。

\<Sysname\> system-view

Sysname ipv6 neighbor 2000::1 fe-e0-89 interface gigabitethernet 1/0/1

【相关命令】

·**display ipv6 neighbors**

·**reset ipv6 neighbors**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 neighbor link-local minimize**

------------------------------------------------------------------------

**[ipv6 neighbor link-local minimize**]命令用来配置链路本地ND表项资源占用最小化。

**[undo ipv6 neighbor link-local minimize**]命令用来恢复缺省情况。

【命令】

**[ipv6 neighbor link-local minimize**]

**[undo ipv6 neighbor link-local minimize**]

【缺省情况】

所有ND表项均会下发硬件表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本功能可以对链路本地ND表项（该ND表项的IPv6地址为链路本地地址）占用的资源进行优化。

缺省情况下，所有ND表项均会下发硬件表项。配置本功能后，新学习的、未被引用的链路本地ND表项（该ND表项的链路本地地址不是某条路由的下一跳）不下发硬件表项，以节省资源。

本功能只对后续新学习的ND表项生效，已经存在的ND表项不受影响。

【举例】

\# 配置链路本地ND表项资源占用最小化。

\<Sysname\> system-view

Sysname ipv6 neighbor link-local minimize

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 neighbor stale-aging**

------------------------------------------------------------------------

**[ipv6 neighbor** **stale-aging**]命令用来配置STALE状态ND表项的老化时间。

**[undo ipv6 neighbor stale-aging**]命令用来恢复缺省情况。

【命令】

**[ipv6 neighbor stale-aging*** aging-time*]

**[undo ipv6 neighbor** **stale-aging**]

【缺省情况】

STALE状态ND表项的老化时间为240分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[aging-time*]：STALE状态ND表项的老化时间，取值范围为1～1440，单位为分钟。

【使用指导】

为适应网络的变化，ND表需要不断更新。ND表中的STALE状态ND表项并非永远有效，每一条记录都有一个老化时间。到达老化时间的STALE状态ND表项将迁移到DELAY状态。5秒钟后DELAY状态超时，ND表项将迁移到PROBE状态，并发送3次NS报文进行可达性探测。若邻居已经下线，则收不到回应的NA报文，此时会将该ND表项删除。

用户可以根据网络实际情况调整老化时间。

【举例】

\# 配置STALE状态ND表项的老化时间为120分钟。

\<Sysname\> system-view

Sysname ipv6 neighbor stale-aging 120

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 neighbors max-learning-num**

------------------------------------------------------------------------

**[ipv6 neighbors max-learning-num**]命令用来配置接口上允许学习的动态邻居表项的最大个数。

**[undo** **ipv6 neighbors** **max-learning-num**]命令用来恢复缺省情况。

【命令】

**[ipv6 neighbors max-learning-num*** number*]

**[undo ipv6 neighbors max-learning-num**]

【缺省情况】

不同型号的设备支持的缺省情况不同，请以设备的实际情况为准。

【视图】

二层接口视图/二层聚合接口视图/三层接口视图/三层聚合接口视图/S通道接口视图/S通道聚合接口视图/三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：接口上允许学习的动态邻居表项的最大个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

设备可以通过NS消息和NA消息来动态获取邻居节点的链路层地址，并将其加入到邻居表中。为了防止部分接口下的用户占用过多的资源，可以通过设置接口学习动态邻居表项的最大数目来进行限制。当接口学习到的动态邻居表项的个数达到所设置的最大值时，该接口将不再学习动态邻居表项。

【举例】

·路由应用

\# 指定GigabitEthernet1/0/1接口上允许动态学习的邻居的最大个数为10个。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1ipv6 neighbors max-learning-num 10

·交换应用

\# 配置VLAN接口100上允许动态学习的邻居的最大个数为10个。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 neighbors max-learning-num 10

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 pathmtu**

------------------------------------------------------------------------

**[ipv6 pathmtu**]命令用来配置指定IPv6地址对应的静态PMTU。

**[undo ipv6 pathmtu**]命令用来删除指定IPv6地址的PMTU配置。

【命令】

**[ipv6 pathmtu** **vpn-instance** *vpn-instance-name* ] *ipv6-address* *value*

**[undo ipv6 pathmtu** [ **vpn-instance** *vpn-instance-name*  *ipv6-address*]]

【缺省情况】

没有配置静态PMTU值。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：指定PMTU所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示公网。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ipv6-address*]：指定的IPv6地址。

*[value*]：指定IPv6地址对应的PMTU值，取值范围为1280～10240，单位为字节。

【使用指导】

用户可以为指定的目的IPv6地址配置静态的PMTU值。当源端主机从接口发送报文时，将比较该接口的MTU与指定目的IPv6地址的静态PMTU，如果报文长度大于二者中的最小值，则采用此最小值对报文进行分片。

【举例】

\# 配置指定IPv6地址对应的静态PMTU值。

\<Sysname\> system-view

Sysname ipv6 pathmtu fe80::12 1300

【相关命令】

·**display ipv6 pathmtu**

·**reset ipv6 pathmtu**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 pathmtu age**

------------------------------------------------------------------------

**[ipv6 pathmtu age**]命令用来配置动态PMTU的老化时间。

**[undo ipv6 pathmtu age**]命令用来恢复缺省情况。

【命令】

**[ipv6 pathmtu age** *age-time*]

**[undo ipv6 pathmtu age**]

【缺省情况】

动态PMTU的老化时间为10分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[age-time*]：PMTU老化时间，取值范围为10～100，单位为分钟。

【使用指导】

动态确定源端主机到目的端主机的PMTU后，源端主机将使用这个MTU值发送后续报文到目的端主机。当PMTU老化时间超时后，源端主机会通过PMTU机制重新确定发送报文的MTU值。

需要注意的是，该配置对静态PMTU不起作用。

【举例】

\# 配置动态PMTU的老化时间为40分钟。

\<Sysname\> system-view

Sysname ipv6 pathmtu age 40

【相关命令】

·**display ipv6 pathmtu**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 prefer temporary-address**

------------------------------------------------------------------------

![说明](IPv6基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 prefer temporary-address**]命令用来开启优先选择临时地址作为报文的源地址功能。

**[undo ipv6 prefer temporary-address**]命令用来恢复缺省情况。

【命令】

**[ipv6 prefer temporary-address**]

**[undo ipv6 prefer temporary-address**]

【缺省情况】

优先选择临时地址作为报文的源地址功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在配置了优先选择临时地址功能前提下发送报文，系统将优先选择临时地址作为报文的源地址。如果生成的临时地址因为DAD冲突不可用，就采用公共地址作为报文的源地址。

【举例】

\# 开启优先选择临时地址作为报文的源地址功能。

\<Sysname\> system-view

Sysname ipv6 prefer temporary-address

【相关命令】

·**ipv6 address auto**

·**ipv6 nd ra prefix**

·**ipv6 temporary-address**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 prefix**

------------------------------------------------------------------------

**[ipv6 prefix**]命令用来手工配置静态IPv6前缀。

**[undo ipv6 prefix**]命令用来用来删除指定的静态IPv6前缀。

【命令】

**[ipv6 prefix** *prefix-number ipv6-prefix/prefix-length*]

**[undo ipv6 prefix ***prefix-number*]

【缺省情况】

设备上不存在任何静态IPv6前缀。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prefix-number*]：前缀编号，取值范围为1～1024。

*[ipv6-prefix/prefix-length*]：前缀和前缀长度。*prefix-length*的取值范围为1～128。

【使用指导】

·不允许通过重复执行ipv6 prefix命令来修改已经创建的静态IPv6前缀。

·不允许手工修改和删除从DHCPv6服务器获取的动态IPv6前缀。

·手工配置的静态IPv6前缀与动态生成的IPv6前缀编号允许相同，静态IPv6前缀优先。

【举例】

\# 创建IPv6静态前缀编号为1，前缀为2001:0410::/32。

\<Sysname\> system-view

Sysname ipv6 prefix 1 2001:0410::/32

【相关命令】

·**display ipv6 prefix**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 reassemble local enable**

------------------------------------------------------------------------

**[ipv6 reassemble local enable**]命令用来开启设备的IPv6分片报文本地重组功能。

**[undo ipv6 reassemble local enable**]命令用来关闭设备的IPv6分片报文本地重组功能。

【命令】

**[ipv6 reassemble local enable**]

**[undo ipv6 reassemble local enable**]

【缺省情况】

IPv6分片报文本地重组功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当分布式设备的某块单板收到目的为本设备的IPv6分片报文时，需要把分片报文送到主用主控板进行重组，这样会导致报文重组性能较低的问题。当开启IPv6分片报文本地重组功能后，分片报文会在该单板上直接进行报文重组，这样就能提高分片报文的重组性能。

需要说明的是，开启IPv6分片报文本地重组功能后，如果分片报文是从设备上不同的单板进入的，会导致IPv6分片报文本地无法重组成功。

【举例】

\# 开启设备的IPv6分片报文本地重组功能。

\<Sysname\> system-view

Sysname ipv6 reassemble local enable

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 redirects enable**

------------------------------------------------------------------------

**[ipv6 redirects enable**]命令用来开启设备的ICMPv6重定向报文的发送功能。

**[undo ipv6 redirects enable**]命令用来关闭设备的ICMPv6重定向报文的发送功能。

【命令】

**[ipv6 redirects enable**]

**[undo ipv6 redirects enable**]

【缺省情况】

ICMPv6重定向报文发送功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

主机启动时，它的路由表中可能只有一条到缺省网关的缺省路由。当满足一定的条件时，作为缺省网关的设备会向源主机发送ICMPv6重定向报文，通知主机重新选择正确的下一跳进行后续报文的发送。

ICMPv6重定向报文发送功能可以简化主机的管理，使具有很少选路信息的主机逐渐建立较完善的路由表，从而找到最佳路由。但是由于重定向功能会在主机的路由表中增加主机路由，当增加的主机路由很多时，会降低主机性能。因此默认情况下设备的ICMPv6重定向报文发送功能是关闭的。

【举例】

\# 开启设备的ICMPv6重定向报文发送功能。

\<Sysname\> system-view

Sysname ipv6 redirects enable

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 router-renumber enable**

------------------------------------------------------------------------

**[ipv6 router-renumber enable**]命令用来配置接口的路由器重编号功能。

**[undo ipv6 router-renumber enable**]命令用来恢复缺省情况。

【命令】

**[ipv6 router-renumber enable**]

**[undo ipv6 router-renumber enable**]

【缺省情况】

路由器重编号功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

设备接收到合法的路由器重编号报文时，会根据报文的内容对本设备上所有使能该功能的三层接口下配置的前缀和地址进行重新配置。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置路由器重编号功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 router-renumber enable

·交换应用

\# 在VLAN接口2上配置路由器重编号功能。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 ipv6 router-renumber enable

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 temporary-address**

------------------------------------------------------------------------

**[ipv6 temporary-address**]命令用来配置系统生成临时地址。

**[undo ipv6 temporary-address**]命令用来取消系统生成临时地址功能，同时会删除已经存在的临时地址。

【命令】

**[ipv6 temporary-address** [ *valid-lifetime preferred-lifetime* ]]

**[undo ipv6 temporary-address**]

【缺省情况】

系统不生成临时地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[valid-lifetime*]：临时地址的有效生命期，取值范围为600～4294967295，单位为秒，缺省值为604800秒（7天）。

*[preferred-lifetime*]：临时地址的首选生命期，取值范围为600～4294967295，单位为秒，缺省值为86400秒（1天）。*preferred-lifetime*的值要小于等于*valid-lifetime*的值。

【使用指导】

在配置了无状态自动配置IPv6地址功能后，接口会根据接收到的RA报文中携带的地址前缀信息和接口ID，自动生成IPv6全球单播地址。如果接口是IEEE 802类型的接口（例如，以太网接口、VLAN接口），其接口ID是由MAC地址根据一定的规则生成，此接口ID具有全球唯一性。对于不同的前缀，接口ID部分始终不变，攻击者通过接口ID可以很方便的识别出通信流量是由哪台设备产生的，并分析其规律，会造成一定的安全隐患。

如果在地址无状态自动配置时，自动生成接口ID不断变化的IPv6地址，就可以加大攻击的难度，从而保护网络。为此，设备提供了临时地址功能，使得系统可以生成临时地址。

配置该功能后，通过地址无状态自动配置，IEEE 802类型的接口可以同时生成两类地址：

·公共地址：地址前缀采用RA报文携带的前缀，接口ID由MAC地址产生。接口ID始终不变。

·临时地址：地址前缀采用RA报文携带的前缀，接口ID由系统根据MD5算法计算产生。接口ID不断变化。

当临时地址的有效生命期过期后，这个临时地址将被删除，同时，系统会通过MD5算法重新生成一个接口ID不同的临时地址。所以，该接口发送报文的源地址的接口ID总是在不停变化。

需要注意的是：

·配置本功能时需要打开地址无状态自动配置功能。

·配置的临时地址的有效生命期要大于或等于首选生命期。

·临时地址的首选生命期是如下两个值之中的较小者：RA前缀中的首选生命期和（配置的临时地址首选生命期减去DESYNC_FACTOR）。DESYNC_FACTOR是一个0～600秒的随机值。

·临时地址的有效生命期是如下两个值之中的较小者：RA前缀中的有效生命期和配置的临时地址有效生命期。

【举例】

\# 配置系统生成临时地址。

\<Sysname\> system-view

Sysname ipv6 temporary-address

【相关命令】

·**ipv6 address auto**

·**ipv6 nd ra prefix**

·**ipv6 prefer temporary-address**

**IPv6基础 \-- IPv6基础配置命令 \-- ipv6 unreachables enable**

------------------------------------------------------------------------

![说明](IPv6基础命令.files/image001.png)

本特性的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ipv6 unreachables enable**]命令用来开启设备的ICMPv6目的不可达报文的发送功能。

**[undo ipv6 unreachables enable**]命令用来关闭设备的ICMPv6目的不可达报文的发送功能。

【命令】

**[ipv6 unreachables enable**]

**[undo ipv6 unreachables enable**]

【缺省情况】

ICMPv6目的不可达报文发送功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

ICMPv6目的不可达报文发送功能是在设备收到IPv6数据报文后，如果发生目的不可达的差错，则将报文丢弃并给源端发送ICMPv6目的不可达差错报文。

由于ICMPv6目的不可达报文传递给用户进程的信息为不可达信息，如果有用户恶意攻击，可能会影响终端用户的正常使用。为了避免上述现象发生，可以关闭设备的ICMPv6目的不可达报文发送功能，从而减少网络流量、防止遭到恶意攻击。

【举例】

\# 开启设备的ICMPv6目的不可达报文发送功能。

\<Sysname\> system-view

Sysname ipv6 unreachables enable

**IPv6基础 \-- IPv6基础配置命令 \-- local-proxy-nd enable**

------------------------------------------------------------------------

**[local-proxy-nd enable**]命令用来开启本地ND Proxy功能。

**[undo local-proxy-nd enable**]命令用来恢复缺省情况。

【命令】

**[local-proxy-nd enable**]

**[undo local-proxy-nd enable**]

【缺省情况】

本地ND Proxy功能处于关闭状态。

【视图】

VLAN接口视图/三层以太网接口视图/三层以太网子接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 在GigabitEthernet1/0/1接口上开启本地ND Proxy功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 local-proxy-nd enable

·交换应用

\# 在VLAN接口100上开启本地ND Proxy功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 local-proxy-nd enable

【相关命令】

·**proxy-nd enable**

**IPv6基础 \-- IPv6基础配置命令 \-- proxy-nd enable**

------------------------------------------------------------------------

**[proxy-nd enable**]命令用来开启ND Proxy功能。

**[undo proxy-nd enable**]命令用来恢复缺省情况。

【命令】

**[proxy-nd enable**]

**[undo proxy-nd enable**]

【缺省情况】

ND Proxy功能处于关闭状态。

【视图】

VLAN接口视图/三层以太网接口视图/三层以太网子接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 在GigabitEthernet1/0/1接口上开启ND Proxy功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 proxy-nd enable

·交换应用

\# 在VLAN接口100上开启ND Proxy功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 proxy-nd enable

【相关命令】

·**local-proxy-nd enable**

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 nd snooping**

------------------------------------------------------------------------

**[reset ipv6 nd snooping**]命令用来清除设备的ND Snooping表项。

【命令】

**[reset ipv6 nd snooping** { [ **vlan** *vlan-id*  [ **global** \| **link-local** ] \| **vlan** *vlan-id ipv6-address* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除设备上的ND Snooping表项。

\<Sysname\> reset ipv6 nd snooping

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 nd suppression xconnect-group**

------------------------------------------------------------------------

**[reset ipv6 nd suppression xconnect-group**]命令用来清除ND泛洪抑制表项。

【命令】

**[reset ipv6 nd suppression xconnect-group** [ **name** *group-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name*** group-name*]：交叉连接组的名称，取值为1\~31个字符的字符串，不能包含字符"-"，区分大小写。

【举例】

\# 清除所有交叉连接组下的ND泛洪抑制表项。

\<Sysname\> reset ipv6 nd suppression xconnect-group

【相关命令】

·**display ****ipv6 nd suppression xconnect-group**

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 neighbors**

------------------------------------------------------------------------

**[reset ipv6 neighbors**]命令用来清除IPv6邻居信息。

【命令】

集中式设备：

**[reset ipv6 neighbors **[{ **all** *\|* **dynamic** *\|* **interface** *interface-type interface-number* \| **static** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset ipv6 neighbors **[{ **all** *\|* **dynamic** *\|* **interface** *interface-type interface-number* \| **slot** *slot-number* [ **cpu** *cpu-number* ] \| **static** }]]

分布式设备－IRF模式：

**[reset ipv6 neighbors **[{ **all** *\|* **dynamic** *\|* **interface** *interface-type interface-number* \| **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] \| **static** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：清除所有接口上的静态与动态邻居信息。

**[dynamic**]：清除所有接口上的动态邻居信息。

**[interface*** interface-type interface-number*]：清除指定接口上的动态邻居信息。*interface-type interface-number*为接口类型和接口编号

**[slot ***slot-number*]：清除指定单板上的动态邻居信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板上的动态邻居表项。（分布式设备－独立运行模式）

**[slot ***slot-number*]：清除指定成员设备的动态邻居信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则清除所有成员设备上的动态邻居表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX的动态邻居信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则清除所有成员设备/PEX上的动态邻居表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的动态邻居信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板上的动态邻居表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的动态邻居信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则清除所有单板上的动态邻居表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：清除指定CPU的动态邻居信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[static**]：清除所有接口上的静态邻居信息。

【使用指导】

当前的IPv6邻居信息可以通过**display ipv6 neighbors**命令查看。

【举例】

\# 清除所有接口上的所有邻居信息。

\<Sysname\> reset ipv6 neighbors all

This will delete all the entries. Continue? [Y/N:Y]

\# 清除所有接口上的动态邻居信息。

\<Sysname\> reset ipv6 neighbors dynamic

This will delete all the dynamic entries. Continue? [Y/N:Y]

\# 清除接口GigabitEthernet1/0/1上的所有邻居信息。

\<Sysname\> reset ipv6 neighbors interface gigabitethernet 1/0/1

This will delete all the dynamic entries by the interface you specified. Contin

ue? [Y/N:Y]

【相关命令】

·**display ipv6 neighbors**

·**ipv6 neighbor**

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 pathmtu**

------------------------------------------------------------------------

**[reset ipv6 pathmtu**]命令用来清除PMTU信息。

【命令】

**[reset ipv6 pathmtu**[ { **all** \| **dynamic** \| **static** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：清空所有的PMTU信息。

**[dynamic**]：清空所有动态创建的PMTU信息。

**[static**]：清空所有的静态PMTU信息。

【举例】

\# 清除所有PMTU信息。

\<Sysname\> reset ipv6 pathmtu all

【相关命令】

·**display ipv6 pathmtu**

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 router-renumber statistics**

------------------------------------------------------------------------

**[reset ipv6 router-renumber statistics**]命令用来清除路由器重编号统计信息。

【命令】

**[reset ipv6 router-renumber statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使用本命令可以清除路由器重编号功能的统计信息，但序列号、重置序列号和分段号不受本命令影响。

【举例】

\# 清除路由器重编号的统计信息。

\<Sysname\> reset ipv6 router-renumber statistics

【相关命令】

·**display ipv6 router-renumber statistics**

**IPv6基础 \-- IPv6基础配置命令 \-- reset ipv6 statistics**

------------------------------------------------------------------------

**[reset ipv6 statistics**]命令用来清除IPv6报文及ICMPv6报文的统计信息。

【命令】

集中式设备：

**[reset ipv6 statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset ipv6 statistics ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset ipv6 statistics ** **chassis**] *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的IPv6报文及ICMPv6报文统计信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板上的IPv6报文及ICMPv6报文统计信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：清除指定成员设备的IPv6报文及ICMPv6报文统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则清除所有成员设备上的IPv6报文及ICMPv6报文统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX的IPv6报文及ICMPv6报文统计信息。*slot-number*表示设备在IRF中的成员编号或PEX的虚拟槽位号。如果未指定本参数，则清除所有成员设备/PEX上的IPv6报文及ICMPv6报文统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的IPv6报文及ICMPv6报文统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板上的IPv6报文及ICMPv6报文统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的IPv6报文及ICMPv6报文统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则清除所有单板上的IPv6报文及ICMPv6报文统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：清除指定CPU的IPv6报文及ICMPv6报文统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

【举例】

\# 清除IPv6报文及ICMPv6报文的统计信息。

\<Sysname\> reset ipv6 statistics

【相关命令】

·**display ipv6 statistics**
