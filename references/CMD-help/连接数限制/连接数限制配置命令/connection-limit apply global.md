
**连接数限制 \-- 连接数限制配置命令 \-- connection-limit apply global**

------------------------------------------------------------------------

**[connection-limit apply global**]命令用来在全局应用连接数限制策略。

**[undo connection-limit apply global**]命令用来在全局取消应用的连接数限制策略。

【命令】

**[connection-limit apply global **[{ **ipv6-policy** \| **policy** } *policy-id*]]

**[undo connection-limit apply global **[{ **ipv6-policy** \| **policy** }]]

【缺省情况】

全局没有应用任何连接数限制策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6-policy**]：指定IPv6连接数限制策略。

**[policy**]：指定IPv4连接数限制策略。

*[policy-id*]：连接数限制策略编号，取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

全局最多只能应用一个IPv4连接数限制策略和一个IPv6连接数限制策略，后配置的IPv4或IPv6连接数限制策略会覆盖已配置的对应类型的策略。

【举例】

\# 在全局应用编号为1的IPv4连接数限制策略。

\<Sysname\> system-view

Sysname connection-limit apply global policy 1

\# 在全局应用编号为12的IPv6连接数限制策略。

\<Sysname\> system-view

Sysname connection-limit apply global ipv6-policy 12

【相关命令】

·**connection-limit**

·**limit**

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit amount**

------------------------------------------------------------------------

**[connection-limit amount**]命令用来配置最大用户连接数。

**[undo connection-limit amount**]命令用来恢复缺省情况。

【命令】

**[connection-limit amount** *amount*]

**[undo connection-limit amount**]

【缺省情况】

不限制最大用户连接数。

【视图】

user-profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[amount*]：最大用户连接数，取值范围为1～10000。一个用户的连接数值超过此值时，将不能建立新的连接。

【使用指导】

最大用户连接数可以多次配置，最后一次生效，修改后的配置立即生效。

设备上的User Profile被删除后，被下发该配置的用户也将不受此User Profile的限制。

【举例】

\# 创建名称为abc的User Profile，并进入user-profile视图。

\<Sysname\> system-view

Sysname user-profile abc

\# 配置最大用户连接数为5，即一个用户的连接数超过5时，将不能建立新的连接。

Sysname-user-profile-abc connection-limit amount 5

【相关命令】

·**display user-profile**（安全命令参考/User Profile）

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit apply**

------------------------------------------------------------------------

![说明](连接数限制命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[connection-limit apply**]命令用来在接口上应用连接数限制策略。

**[undo connection-limit apply**]命令用来在接口上取消应用的连接数限制策略。

【命令】

**[connection-limit apply **[{ **ipv6-policy** \| **policy** } *policy-id*]]

**[undo connection-limit apply **[{ **ipv6-policy** \| **policy** }]]

【缺省情况】

接口上没有应用任何连接数限制策略。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6-policy**]：指定IPv6连接数限制策略。

**[policy**]：指定IPv4连接数限制策略。

*[policy-id*]：连接数限制策略编号，取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

同一个接口上同时只能应用一个IPv4连接数限制策略和一个IPv6连接数限制策略，后配置的IPv4或IPv6连接数限制策略会覆盖已配置的对应类型的策略。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上应用编号为1的IPv4连接数限制策略。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 connection-limit apply policy 1

\# 在接口GigabitEthernet1/0/1应用编号为12的IPv6连接数限制策略。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 connection-limit apply ipv6-policy 12

·交换应用

\# 在接口Vlan-interface2上应用编号为1的IPv4连接数限制策略。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 connection-limit apply policy 1

\# 在接口Vlan-interface2上应用编号为12的IPv6连接数限制策略。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 connection-limit apply ipv6-policy 12

【相关命令】

·**connection-limit**

·**limit**

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit**

------------------------------------------------------------------------

**[connection-limit**]命令用来创建连接数限制策略，并进入连接数限制策略视图。

**[undo connection-limit**]命令用来删除连接数限制策略。

【命令】

**[connection-limit **[{ **ipv6-policy** \| **policy** } *policy-id*]]

**[undo connection-limit **[{ **ipv6-policy** \| **policy** } *policy-id*]]

【缺省情况】

不存在任何连接数限制策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6-policy**]：指定IPv6连接数限制策略。

**[policy**]：指定IPv4连接数限制策略。

*[policy-id*]：连接数限制策略编号（IPv4、IPv6连接数限制策略的编号空间各自独立），取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\#创建编号为1的IPv4连接数限制策略，并进入IPv4连接数限制策略视图。

\<Sysname\> system-view

Sysname connection-limit policy 1

Sysname-connlmt-policy-1

\#创建编号为12的IPv6连接数限制策略，并进入IPv6连接数限制策略视图。

\<Sysname\> system-view

Sysname connection-limit ipv6-policy 12

Sysname-connlmt-ipv6-policy-12

【相关命令】

·**connection-limit apply**

·**connection-limit apply global**

·**display connection-limit**

·**limit**

**连接数限制 \-- 连接数限制配置命令 \-- connection-limit rate**

------------------------------------------------------------------------

**[connection-limit rate**]命令用来配置最大用户新建连接速率。

**[undo connection-limit rate**]命令用来恢复缺省情况。

【命令】

**[connection-limit rate*** rate*]

**[undo connection-limit rate**]

【缺省情况】

不限制最大用户新建连接速率。

【视图】

user-profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rate*]：最大新建连接速率，取值范围为5～1000，单位为每秒连接数。一个用户的新建连接速率超过此值时，将不能建立新的连接。

【使用指导】

最大用户连接速率可以多次配置，最后一次生效，修改后的配置立即生效。

设备上的User Profile被删除后，被下发该配置的用户也将不受此User Profile的限制。

【举例】

\# 创建名称为abc的User Profile，并进入user-profile视图。

\<Sysname\> system-view

Sysname user-profile abc

\# 配置最大用户新建连接速率为100，即一个用户的每秒新建连接数超过100个时，将不能建立新的连接。

Sysname-user-profile-abc connection-limit rate 100

【相关命令】

·**display user-profile**（安全命令参考/User Profile）

**连接数限制 \-- 连接数限制配置命令 \-- display connection-limit**

------------------------------------------------------------------------

![说明](连接数限制命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display connection-limit**]命令用来显示连接数限制策略的配置信息。

【命令】

**[display connection-limit ** { **ipv6-policy** \| **policy** } { *policy-id* \| **all** }]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6-policy**]：显示IPv6连接数限制策略。

**[policy**]：显示IPv4连接数限制策略。

*[policy-id*]：连接数限制策略编号，取值范围与设备的型号有关，请以设备的实际情况为准。**

**[all**]：显示所有指定类型的连接数限制[策略。]

【举例】

\# 显示所有IPv4连接数限制策略的配置信息。

\<Sysname\> display connection-limit policy all

3 policies in total:

 Policy  Rule     Stat Type  HiThres  LoThres  ACL

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

      0     1  Src-Dst-Port     2000     1800  3000

           12       Src-Dst      500       45  3001

          255            \--  1000000   980000  2001

      1     2      Dst-Port      800      70   3010

            3       Src-Dst      100      90   3000

           10  Src-Dst-Port       50      45   3003

           11           Src      200     200   3004

          200           \--    500000  498000   2002

     28     4          Port     1500    1400   3100

            5           Dst     3000     280   3101

           21       Src-Dst      200     180   3102

           25      Src-Port       50      35   3200

#  显示编号为1的IPv4连接数策略的配置信息。

\<Sysname\> display connection-limit policy 1

IPv4 connection limit policy 1 has been applied 5 times, and has 5 limit rules.

Limit rule list:

 Policy  Rule     Stat Type  HiThres  LoThres  ACL

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

      1     2      Dst-Port      800      700  3010

            3       Src-Dst      100       90  3000

           10  Src-Dst-Port       50       45  3003

           11           Src      200      200  3004

          200            \--   500000   498000  2002

 Application list:

     GigabitEthernet1/0/1

     GigabitEthernet1/0/2

     Vlan-interface1

     Tunnel0

     Global

#  显示所有IPv6连接数限制策略的配置信息。

\<Sysname\> display connection-limit ipv6-policy all

2 policies in total:

 Policy  Rule     Stat Type  HiThres  LoThres  ACL

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

      3     1       Src-Dst     1000      800  3010

            2           Dst      500      450  3001

      4     2  Src-Dst-Port      800      700  3010

            3           Src      100       90  3020

          200            \--   100000    89000  2005

#  显示编号为3的IPv6连接数限制策略的配置信息。

\<Sysname\> display connection-limit ipv6-policy 3

IPv6 connection limit policy 3 has been applied 3 times, and has 2 limit rules.

Limit rule list:

Policy  Rule     Stat Type  HiThres  LoThres  ACL

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

     3     1       Src-Dst     1000      800  3010 

           2           Dst      500      450  3001

Application list:

    GigabitEthernet1/0/1

    Vlan-interface1

    Tunnel0

表1-1 display connection-limit命令显示信息描述表

字段

描述

Limit rule list

连接数限制策略信息列表

Policy

连接数限制策略编号

Rule

连接数限制规则编号

Stat Type

统计方式，有如下取值：

·Src-Dst-Port：按源IP－目的IP－服务的组合进行统计和限制

·Src-Dst：按源IP－目的IP的组合进行统计和限制

·Src-Port：按源IP－服务的组合进行统计和限制

·Dst-Port：按目的IP－服务的组合进行统计和限制

·Src：按源IP进行统计和限制

·Dst：按目的IP进行统计和限制

·Port：按服务进行统计和限制

·Dslite：按DS-Lite隧道的B4设备进行统计和限制

·\--：不按照具体的IP地址、服务进行统计和限制，与本规则引用的ACL相匹配的所有连接将整体受到指定的阈值限制

HiThres

连接数上限

LoThres

连接数下限

ACL

规则引用的ACL编号或ACL名称

Application list

连接数限制策略应用列表，包括接口名称和Global，其中Global表示该连接数限制策略应用在全局

【相关命令】

·**connection-limit**

·**connection-limit apply**

·**connection-limit apply global**

·**limit**

**连接数限制 \-- 连接数限制配置命令 \-- display connection-limit ipv6-stat-nodes**

------------------------------------------------------------------------

![说明](连接数限制命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display connection-limit ipv6-stat-nodes**]命令用来显示连接数限制在全局或接口的IPv6统计节点列表。

【命令】

集中式设备：

**[display connection-limit ipv6-stat-nodes**  { **global** \| **interface** *interface-type interface-number* } [ **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* ] \*  **count** ]

分布式设备－独立运行模式/集中式IRF设备：

**[display connection-limit ipv6-stat-nodes**[ { **global** \| **interface** *interface-type interface-number* } [ **slot** *slot-number* [ **cpu** *cpu-number* ]   **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* ] \*  **count** ]]

分布式设备－IRF模式：

**[display connection-limit ipv6-stat-nodes**[ { **global** \| **interface** *interface-type interface-number* } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]   **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* ] \*  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示全局的IPv6统计节点列表[。]

**[interface** *interface-type interface-number*]：显示指定接口的IPv6统计节点列表，*interface-type interface-number*表示接口类型和接口编号[。]

**[slot*** slot-number*]：显示指定单板上全局或全局接口的IPv6统计节点列表，*slot-number*表示单板所在的槽位号。该参数仅在显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上全局或全局接口的IPv6统计节点列表，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上全局或全局接口的IPv6统计节点列表，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上全局或全局接口的IPv6统计节点列表，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上全局或全局接口的IPv6统计节点列表，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上全局或全局接口的IPv6统计节点列表，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[destination** *destination-ip*]：显示指定目的IP地址的IPv6统计节点列表。

**[service-port*** port-number*]：显示指定服务端口号的IPv6统计节点列表。

**[source** *source-ip*]：显示指定源IP地址的IPv6统计节点列表。

**[count**]：显示IPv6统计节点的个数。

【使用指导】

一个统计节点标识了连接数限制进行统计和限制的一个对象（一个连接或一类连接），包括该连接的报文特征（源/目的IP地址、服务端口号、传输层协议类型等）、对该连接所应用的连接限制策略、当前连接数目以及当前是否允许创建新的连接。

·如果指定**source**、**destination**、**service-port**中的一个或多个参数，则表示将按照多个条件来显示统计节点列表，比如指定了**source**和**destination**，则显示同时符合指定源IP地址和目的IP地址的统计节点列表。

·如果不指定**source**、**destination**、**service-port**中任何一个参数，则表示显示所有的统计节点列表。

【举例】

\# 显示接口GigabitEthernet1/0/1上的所有IPv6连接数限制统计节点列表。（集中式设备）

\<Sysname\> display connection-limit ipv6-stat-nodes interface gigabitethernet 1/0/1

 Src IP address          : Any

     VPN instance        : vpn5

 Dst IP address          : fe80::5ed9:98ff:feb1:69b6

     VPN instance        : abcdefghijklmnopqrstuvwxyzabcde

 Tunnel ID               : 9876543210

 Service                 : tcp/12345

 Limit rule ID           : 12345(ACL: 3184)

 Sessions threshold Hi/Lo: 1000000/90000

 Sessions count          : 150000

 New session flag        : Permit

\# 显示接口Vlan-interface2上的所有IPv6连接数限制统计节点列表。（集中式设备）

\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 2

 Src IP address          : Any

     VPN instance        : vpn5

 Dst IP address          : fe80::5ed9:98ff:feb1:69b6

     VPN instance        : abcdefghijklmnopqrstuvwxyzabcde

 Tunnel ID               : 9876543210

 Service                 : tcp/12345

 Limit rule ID           : 12345(ACL: 3184)

 Sessions threshold Hi/Lo: 1000000/90000

 Sessions count          : 150000

 New session flag        : Permit

\# 显示全局接口Vlan-interface10在2号单板上的所有IPv6连接数限制统计节点列表。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 10 slot 2

Slot 2:

 Src IP address          : 112::2

     VPN instance        : \--

 Dst IP address          : Any

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : udp/300

 Limit rule ID           : 0(ACL: 3571)

 Sessions threshold Hi/Lo: 3000/2900

 Sessions count          : 2002

 New session flag        : Permit

\# 显示2号成员设备上全局的IPv6连接数限制统计节点列表。（集中式IRF设备）

\<Sysname\> display connection-limit ipv6-stat-nodes global slot 2

Slot 2:

 Src IP address          : Any

     VPN instance        : \--

 Dst IP address          : Any

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : icmp/0

 Limit rule ID           : 22(ACL: 3666)

 Sessions threshold Hi/Lo: 3500/3000

 Sessions count          : 3100

 New session flag        : Permit

\# 显示接口GigabitEthernet1/1/0/2上的所有IPv6连接数限制统计节点列表。（分布式设备－IRF模式）

\<Sysname\> display connection-limit ipv6-stat-nodes interface gigabitethernet 1/1/0/2

Slot 1 in chassis 1:

 Src IP address          : 5::1

     VPN instance        : Vpn1

 Dst IP address          : Any

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : All

 Limit rule ID           : 21(ACL: 2988)

 Sessions threshold Hi/Lo: 2000/1500

 Sessions count          : 1988

 New session flag        : Deny

\# 显示全局源IP地址为2::1的IPv6连接数限制统计节点个数。（集中式设备）

\<Sysname\> display connection-limit ipv6-stat-nodes global source 2::1 count

       Current limit statistic nodes count is 16.

\# 显示全局接口Vlan-interface10在2号单板上的IPv6连接数限制统计节点个数。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 10 slot 2 count

Slot 2:

       Current limit statistic nodes count is 1.

\# 显示2号成员设备上的IPv6连接数限制统计节点个数。（集中式IRF设备）

\<Sysname\> display connection-limit ipv6-stat-nodes global slot 2 count

Slot 2:

       Current limit statistic nodes count is 0.

\# 显示1号成员设备的2号单板上的IPv6连接数限制统计节点个数。（分布式设备－IRF模式）

\<Sysname\> display connection-limit ipv6-stat-nodes global chassis 1 slot 2 count

Slot 2 in chassis 1:

       Current limit statistic nodes count is 0.

\# 显示全局接口Vlan-interface10在2号单板的0号CPU上的所有IPv6连接数限制统计节点列表。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 10 slot 2 cpu 0

CPU 0 on slot 2:

 Src IP address          : 112::2

     VPN instance        : \--

 Dst IP address          : Any

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : udp/300

 Limit rule ID           : 0(ACL: 3571)

 Sessions threshold Hi/Lo: 3000/2900

 Sessions count          : 2002

 New session flag        : Permit

\# 显示2号成员设备的0号CPU上全局的IPv6连接数限制统计节点列表。（集中式IRF设备）

\<Sysname\> display connection-limit ipv6-stat-nodes global slot 2 cpu 0

CPU 0 on slot 2:

 Src IP address          : Any

     VPN instance        : \--

 Dst IP address          : Any

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : icmp/0

 Limit rule ID           : 22(ACL: 3666)

 Sessions threshold Hi/Lo: 3500/3000

 Sessions count          : 3100

 New session flag        : Permit

\# 显示接口GigabitEthernet1/1/0/2在1号成员设备的1号单板的0号CPU上的所有IPv6连接数限制统计节点列表。（分布式设备－IRF模式）

\<Sysname\> display connection-limit ipv6-stat-nodes interface gigabitethernet 1/1/0/2 chassis 1 slot 1 cpu 0

CPU 0 on slot 1 in chassis 1:

 Src IP address          : 5::1

     VPN instance        : Vpn1

 Dst IP address          : Any

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : All

 Limit rule ID           : 21(ACL: 2988)

 Sessions threshold Hi/Lo: 2000/1500

 Sessions count          : 1988

 New session flag        : Deny

\# 显示全局接口Vlan-interface10在2号单板的0号CPU上的IPv6连接数限制统计节点个数。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit ipv6-stat-nodes interface vlan-interface 10 slot 2 cpu 0 count

CPU 0 on slot 2:

       Current limit statistic nodes count is 1.

\# 显示2号成员设备的0号CPU上的IPv6连接数限制统计节点个数。（集中式IRF设备）

\<Sysname\> display connection-limit ipv6-stat-nodes global slot 2 cpu 0 count

CPU 0 on slot 2:

       Current limit statistic nodes count is 0.

\# 显示1号成员设备的2号单板的0号CPU上的IPv6连接数限制统计节点个数。（分布式设备－IRF模式）

\<Sysname\> display connection-limit ipv6-stat-nodes global chassis 1 slot 2 cpu 0 count

CPU 0 on slot 2 in chassis 1:

       Current limit statistic nodes count is 0.

表1-2 display connection-limit stat-nodes命令显示信息描述表

字段

描述

Src IP address

源IP地址

Dst IP address

目的IP地址

VPN instance

该地址所属的MPLS L3VPN的VPN实例名称，"\--"表示属于公网

Tunnel ID

DS Lite隧道ID，"\--"表示不属于任何DS Lite Tunnel

Service

协议名及服务端口号。如果不是知名协议则显示为"unknown(xx)"，xx为协议编号，此时不显示服务端口号。其中，对于ICMP协议，括弧内的数字为ICMP的type和code字段组合表示的十六进制数所对应的十进制数

Limit rule ID

匹配的规则编号，括号里为匹配的ACL编号

Sessions threshold Hi/Lo

连接数限制的上限值及下限值

Sessions count

当前连接计数

New session flag

是否允许创建新连接，Permit表示允许创建，Deny表示不允许创建

【相关命令】

·**connection-limit apply global ipv6-policy**

·**connection-limit apply ipv6-policy**

·**connection-limit ipv6-policy**

·**limit**

**连接数限制 \-- 连接数限制配置命令 \-- display connection-limit statistics**

------------------------------------------------------------------------

![说明](连接数限制命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display connection-limit statistics**]命令用来显示连接数限制在全局或接口的统计信息。

【命令】

集中式设备：

**[display connection-limit statistics **[{ **global** \| **interface** *interface-type interface-number* } ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display connection-limit statistics **[{ **global** \| **interface** *interface-type interface-number* } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[display connection-limit statistics **[{ **global** \| **interface** *interface-type interface-number* } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示全局的连接数限制统计信息[。]

**[interface** *interface-type interface-number*]：显示指定接口的连接数限制统计信息，*interface-type interface-number*表示接口类型和接口编号[。]

**[slot*** slot-number*]：显示指定单板上全局或全局接口的连接数限制统计信息，*slot-number*表示单板所在的槽位号。该参数仅在指定显示[全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上全局或全局接口的连接数限制统计信息，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定显示[全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（集中式IRF模式）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上全局或全局接口的连接数限制统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定显示[全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（集中式IRF模式）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上全局或全局接口的连接数限制统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定显示[全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上全局或全局接口的连接数限制统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定显示[全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上全局或全局接口的连接数限制统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示全局[的连接数限制统计信息。（集中式设备）]

\<Sysname\> display connection-limit statistics global

Connection limit statistics (Global, slot 0):

    Dropped IPv4 packets:   54781

    Dropped IPv6 packets:   11457

\# 显示2号单板上的全局的连接数限制统计信息。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit statistics global slot 2

Connection limit statistics (Global, slot 2):

    Dropped IPv4 packets:   74213

    Dropped IPv6 packets:   58174

\# 显示2号成员设备上全局的连接数限制统计信息。（集中式IRF设备）

\<Sysname\> display connection-limit statistics global slot 2

Connection limit statistics (Global, slot 2):

    Dropped IPv4 packets:   74213

    Dropped IPv6 packets:   58174

\# 显示全局接口Vlan-interface10在2号成员设备的1号单板上的连接数限制统计信息。（分布式设备－IRF模式）

\<Sysname\> display connection-limit statistics interface vlan-interface 10 chassis 2 slot 1

Connection limit statistics (Vlan-interface10, slot 1 in chassis 2):

    Dropped IPv4 packets:   12345

    Dropped IPv6 packets:   55239

\# 显示2号单板的0号CPU上的全局的连接数限制统计信息。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit statistics global slot 2 cpu 0

Connection limit statistics (Global, CPU 0 on slot 2):

    Dropped IPv4 packets:   74213

    Dropped IPv6 packets:   58174

\# 显示2号成员设备的0号CPU上全局的连接数限制统计信息。（集中式IRF设备）

\<Sysname\> display connection-limit statistics global slot 2 cpu 0

Connection limit statistics (Global, CPU 0 on slot 2):

    Dropped IPv4 packets:   74213

    Dropped IPv6 packets:   58174

\# 显示全局接口Vlan-interface10在2号成员设备的1号单板的0号CPU上的连接数限制统计信息。（分布式设备－IRF模式）

\<Sysname\> display connection-limit statistics interface vlan-interface 10 chassis 2 slot 1 cpu 0

Connection limit statistics (Vlan-interface10, CPU 0 on slot 1 in chassis 2):

    Dropped IPv4 packets:   12345

    Dropped IPv6 packets:   55239

表1-3 display connection-limit statistics命令显示信息描述表

字段

描述

Dropped IPv4 packet

匹配全局或接口IPv4连接数限制策略，因连接数超过指定上限而被丢弃的报文个数

Dropped IPv6 packet

匹配全局或接口IPv6连接数限制策略，因连接数超过指定上限而被丢弃的报文个数

【相关命令】

·**connection-limit **

·**connection-limit apply**

·**connection-limit apply global**

·**limit**

**连接数限制 \-- 连接数限制配置命令 \-- display connection-limit stat-nodes**

------------------------------------------------------------------------

![说明](连接数限制命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display connection-limit stat-nodes**]命令用来显示连接数限制在全局或接口的IPv4统计节点列表。

【命令】

集中式设备：

**[display connection-limit stat-nodes ** { **global** \| **interface** *interface-type interface-number* } [ **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* ] \*  **count** ]

**[display connection-limit stat-nodes ** { **global** \| **interface** *interface-type interface-number* } **dslite-peer** *b4-address* [ **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display connection-limit stat-nodes **[{ **global** \| **interface** *interface-type interface-number* } [ **slot** *slot-number* [ **cpu** *cpu-number* ]   **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* ] \*  **count** ]]

**[display connection-limit stat-nodes ** { **global** \| **interface** *interface-type interface-number* } ] **slot** *slot-number*  **cpu** *cpu-number*   **dslite-peer*** b4-address* [ **count** ]

分布式设备－IRF模式：

**[display connection-limit stat-nodes **[{ **global** \| **interface** *interface-type interface-number* } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]   **destination** *destination-ip* \| **service-port** *port-number* \| **source** *source-ip* ] \*  **count** ]]

**[display connection-limit stat-nodes ** { **global** \| **interface** *interface-type interface-number* } ] **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*   **dslite-peer*** b4-address* [ **count** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示全局的IPv4统计节点列表[。]

**[interface** *interface-type interface-number*]：显示指定接口的IPv4统计节点列表，*interface-type interface-number*表示接口类型和接口编号[。]

**[slot*** slot-number*]：显示指定单板上全局或全局接口的IPv4统计节点列表，*slot-number*表示单板所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上全局或全局接口的IPv4统计节点列表，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上全局或全局接口的IPv4统计节点列表，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上全局或全局接口的IPv4统计节点列表，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上全局或全局接口的IPv4统计节点列表，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定显示全局统计节点列表，或上述指定的接口为全局类型的接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上全局或全局接口的IPv4统计节点列表，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[destination** *destination-ip*]：显示指定目的IP地址的IPv4统计节点列表。

**[service-port*** port-number*]：显示指定服务端口号的IPv4统计节点列表。

**[source** *source-ip*]：显示指定源IP地址的IPv4统计节点列表。

**[dslite-peer**]* b4-address*：显示指定DS-Lite B4设备的IPv4统计节点列表，*b4-address*表示B4设备的IPv6地址。

**[count**]：显示IPv4统计节点的个数。

【使用指导】

一个统计节点标识了连接数限制进行统计和限制的一个对象（一个连接或一类连接），包括该连接的报文特征（源/目的IP地址、服务端口号、传输层协议类型等）、对该连接所应用的连接限制策略、当前连接数目的统计值，以及当前是否允许创建新的连接。

·如果指定**source**、**destination**、**service-port**中的一个或多个参数，则表示将按照多个条件来显示统计节点列表，比如指定了**source **和**destination**，则显示同时符合指定源IP地址和目的IP地址的统计节点列表。.

·如果不指定**source**、**destination**、**service-port**中任何一个参数，则表示显示所有的统计节点列表。

【举例】

\# 显示接口GigabitEthernet1/0/1上的所有IPv4连接数限制统计节点列表。（集中式设备）

\<Sysname\> display connection-limit stat-nodes interface gigabitethernet 1/0/1

 Src IP address          : 100.100.100.100

     VPN instance        : 0123456789012345678901234567890

 Dst IP address          : 200.200.200.200

     VPN instance        : abcdefghijklmnopqrstuvwxyzabcde

 Tunnel ID               : 1234567890

 Service                 : tcp/12345

 Limit rule ID           : 12345(ACL: 3001)

 Sessions threshold Hi/Lo: 1100000/980000

 Sessions count          : 1050000

 New session flag        : Permit

\# 显示接口Vlan-interface2上的所有IPv4连接数限制统计节点列表。（集中式设备）

\<Sysname\> display connection-limit stat-nodes interface vlan-interface 2

 Src IP address          : 100.100.100.100

     VPN instance        : 0123456789012345678901234567890

 Dst IP address          : 200.200.200.200

     VPN instance        : abcdefghijklmnopqrstuvwxyzabcde

 Tunnel ID               : 1234567890

 Service                 : tcp/12345

 Limit rule ID           : 12345(ACL: 3001)

 Sessions threshold Hi/Lo: 1100000/980000

 Sessions count          : 1050000

 New session flag        : Permit

\# 显示所有单板上全局的所有IPv4连接数限制统计节点列表。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit stat-nodes global

Slot 0:

Slot 1:

 Src IP address          : Any

     VPN instance        : Vpn1

 Dst IP address          : Any

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : All

 Limit rule ID           : 21(ACL: 2002)

 Sessions threshold Hi/Lo: 2000/1500

 Sessions count          : 1988

 New session flag        : Deny

\# 显示2号成员设备上全局的IPv4连接数限制统计节点列表。（集中式IRF设备）

\<Sysname\> display connection-limit stat-nodes global slot 2

Slot 2:

 Src IP address          : Any

     VPN instance        : Vpn1

 Dst IP address          : 202.113.16.117

     VPN instance        : Vpn2

 Tunnel ID               : \--

 Service                 : icmp/0

 Limit rule ID           : 7(ACL: 3102)

 Sessions threshold Hi/Lo: 4000/3800

 Sessions count          : 1001

 New session flag        : Permit

\# 显示接口GigabitEthernet1/1/0/2上的所有IPv4连接数限制统计节点列表。（分布式设备－IRF模式）

\<Sysname\> display connection-limit stat-nodes interface gigabitethernet 1/1/0/2

Slot 1 in chassis 1:

 Src IP address          : Any

     VPN instance        : \--

 Dst IP address          : 110.23.1.44

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : udp/333

 Limit rule ID           : 19(ACL: 3307)

 Sessions threshold Hi/Lo: 10000/9900

 Sessions count          : 1001

 New session flag        : Permit

\# 显示全局的IPv4连接数限制统计节点个数。（集中式设备）

\<Sysname\> display connection-limit stat-nodes global count

       Current limit statistic nodes count is 5.

\# 显示全局接口Vlan-interface10在2号单板上的IPv4连接数限制统计节点个数。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit stat-nodes interface vlan-interface 10 slot 2 count

Slot 2:

       Current limit statistic nodes count is 1.

\# 显示2号成员设备上源IP地址为1.1.1.1的IPv4连接数限制统计节点个数。（集中式IRF设备）

\<Sysname\> display connection-limit stat-nodes global slot 2 source 1.1.1.1 count

Slot 2:

       Current limit statistic nodes count is 0.

\# 显示1号成员设备的2号单板上的IPv4连接数限制统计节点个数。（分布式设备－IRF模式）

\<Sysname\> display connection-limit stat-nodes global chassis 1 slot 2 count

Slot 2 in chassis 1:

       Current limit statistic nodes count is 0.

\# 显示1号单板的0号CPU上全局的所有IPv4连接数限制统计节点列表。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit stat-nodes global slot 1 cpu 0

CPU 0 on slot 1:

 Src IP address          : Any

     VPN instance        : Vpn1

 Dst IP address          : Any

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : All

 Limit rule ID           : 21(ACL: 2002)

 Sessions threshold Hi/Lo: 2000/1500

 Sessions count          : 1988

 New session flag        : Deny

\# 显示2号成员设备的0号CPU上全局的IPv4连接数限制统计节点列表。（集中式IRF设备）

\<Sysname\> display connection-limit stat-nodes global slot 2 cpu 0

CPU 0 on slot 2:

 Src IP address          : Any

     VPN instance        : Vpn1

 Dst IP address          : 202.113.16.117

     VPN instance        : Vpn2

 Tunnel ID               : \--

 Service                 : icmp/0

 Limit rule ID           : 7(ACL: 3102)

 Sessions threshold Hi/Lo: 4000/3800

 Sessions count          : 1001

 New session flag        : Permit

\# 显示接口GigabitEthernet1/1/0/2在1号成员设备的1号单板的0号CPU上的所有IPv4连接数限制统计节点列表。（分布式设备－IRF模式）

\<Sysname\> display connection-limit stat-nodes interface gigabitethernet 1/1/0/2 chassis 1 slot 1 cpu 0

CPU 0 on slot 1 in chassis 1:

 Src IP address          : Any

     VPN instance        : \--

 Dst IP address          : 110.23.1.44

     VPN instance        : \--

 Tunnel ID               : \--

 Service                 : udp/333

 Limit rule ID           : 19(ACL: 3307)

 Sessions threshold Hi/Lo: 10000/9900

 Sessions count          : 1001

 New session flag        : Permit

\# 显示全局接口Vlan-interface10在2号单板的0号CPU上的IPv4连接数限制统计节点个数。（分布式设备－独立运行模式）

\<Sysname\> display connection-limit stat-nodes interface vlan-interface 10 slot 2 cpu 0 count

CPU 0 on slot 2:

       Current limit statistic nodes count is 1.

\# 显示2号成员设备的0号CPU上源IP地址为1.1.1.1的IPv4连接数限制统计节点个数。（集中式IRF设备）

\<Sysname\> display connection-limit stat-nodes global slot 2 cpu 0 source 1.1.1.1 count

CPU 0 on slot 2:

       Current limit statistic nodes count is 0.

\# 显示1号成员设备的2号单板的0号CPU上的IPv4连接数限制统计节点个数。（分布式设备－IRF模式）

\<Sysname\> display connection-limit stat-nodes global chassis 1 slot 2 cpu 0 count

CPU 0 on slot 2 in chassis 1:

       Current limit statistic nodes count is 0.

表1-4 display connection-limit stat-nodes命令显示信息描述表

字段

描述

Src IP address

源IP地址

Dst IP address

目的IP地址

VPN instance

该地址所属的MPLS L3VPN的VPN实例名称，"\--"表示不属于任何VPN

Tunnel ID

DS Lite隧道ID，"\--"表示不属于任何DS Lite Tunnel

Service

协议名及服务端口号。如果不是知名协议则显示为"unknown(xx)"，xx为协议编号，此时不显示服务端口号。其中，对于ICMP协议，括弧内的数字为ICMP的type和code字段组合表示的十六进制数所对应的十进制数

Limit rule ID

匹配的规则编号，括号里为匹配的ACL编号

Sessions threshold Hi/Lo

连接数限制的上限值及下限值

Sessions count

当前连接计数

New session flag

是否允许创建新连接，Permit表示允许创建，Deny表示不允许创建

【相关命令】

·**connection-limit policy**

·**connection-limit apply global policy**

·**connection-limit apply policy**

·**limit**

**连接数限制 \-- 连接数限制配置命令 \-- limit**

------------------------------------------------------------------------

**[limit**]命令用来配置连接数限制规则。

**[undo limit**]命令用来删除指定的连接数限制规则。

【命令】

IPv4连接数限制策略视图：

**[limit** *limit-id* **acl** [ **ipv6**  { *acl-number* \| **name** *acl-name* } [ **per-destination** \| **per-service** \| **per-source** ] \* **amount** *max-amount* *min-amount*]]

**[limit** *limit-id* **acl**]**ipv6**[ { *acl-number* \| **name** *acl-name* } **per-ds-lite-b4 amount** *max-amount* *min-amount*]

**[undo limit ***limit-id*]

IPv6连接数限制策略视图：

**[limit**[ *limit-id* **acl** **ipv6** { *acl-number* \| **name** *acl-name* } [ **per-destination** \| **per-service** \| **per-source** ] \* **amount** *max-amount* *min-amount*]]

**[undo limit ***limit-id*]

【缺省情况】

连接数策略中不存在任何规则。

【视图】

IPv4连接数限制策略视图/IPv6连接数限制策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit-id*]：连接数限制规则编号，取值范围与设备的型号有关，请以设备的实际情况为准。

**[acl**]：指定用于匹配用户范围的ACL。该连接限制规则仅对匹配ACL规则的用户连接数进行统计和限制。

**[ipv6**]：表示引用I[Pv6 ACL]。若不指定该参数，则表示引用IPv4 ACL。

*[acl-number*]：引用的ACL编号，取值范围为2000～3999。

**[name**]*acl-name*：引用的ACL名称。

**[per-destination**]：表示按目的地址进行统计和限制。

**[per-service**]：表示按服务（即按传输层协议和服务端口）进行统计和限制。

**[per-source**]：表示按源地址进行统计和限制。

**[per-ds-lite-b4**]：[表示按照]DS-Lite隧道的B4设备IPv6地址来进行统计和限制。该参数仅在IPv4连接数限制策略视图下存在。

*[max-amount*]：指定的连接数上限，取值范围为1～1000000。某范围或某种类型的连接数值超过此值时，用户将不能建立新的连接。

*[min-amount*]：指定的连接数下限，取值范围为1～1000000，不能大于*max-amount*的取值。连接数的统计值降到此值之下时，允许用户建立新的连接。

【使用指导】

每个连接数限制策略中可以定义多个规则，每个规则中需要指定引用的ACL、规则的类型以及统计的上下门限值。对于**per-destination**、**per-source**、**per-service**类型，可以在一条规则中单独指定其中之一或指定它们的组合。例如，同时指定**per-destination**和**per-source**，就表示同时按照连接的报文源地址和目的地址进行统计和限制，具有相同源和目的的连接属于同一类连接，该类连接的数目将受到指定的阈值的限制。对于**per-ds-lite-b4**类型，只能在一条规则中单独指定。

需要注意的是：

·同一个连接数限制策略中的不同规则必须引用不同的ACL。

·如果**per-destination**、**per-service**、**per-source**三个参数都不指定，则表示与本规则引用的ACL相匹配的所有连接将整体受到指定的阈值限制。

·**per-ds-lite-b4**参数用于限制DS-Lite隧道每个B4设备连接的IPv4用户连接数，每个规则限制的B4设备由规则中指定的IPv6 ACL来匹配。

·在DS-Lite隧道组网环境中，若AFTR设备上采用了Endpoint-Independent Mapping模式的NAT配置，则要基于B4设备来限制从IPv4外网主动访问IPv4内网的连接，配置了**per-ds-lite-b4**类型规则的连接数限制策略必须应用在DS-Lite隧道接口上或者应用在全局。

·对设备上建立的连接与某连接数限制策略进行匹配时，将按照规则编号从小到大的顺序依次遍历该策略中的所有规则，直到找到一条匹配的规则为止。

·当引用的ACL内容发生改变时，设备将按照新的连接数限制策略重新对已有连接进行统计和限制。

【举例】

\# 在lPv4连接数限制策略1中创建一条规则，规则编号为1，引用ACL 3000，对匹配ACL 3000的连接同时按照报文的源地址和目的地址进行统计和限制，连接数的上限值为2000、下限值为1800。该规则用于限制192.168.0.0/24网段的每台主机最多只能同时向外网的同一个目的IP地址发起2000条连接，超过2000条时，需要等待连接数下降到1800以下之后，才允许新建连接。

\<Sysname\> system-view

Sysname acl number 3000

Sysname-acl-adv-3000 rule permit ip source 192.168.0.0 0.0.0.255

Sysname-acl-adv-3000 quit

Sysname connection-limit policy 1

Sysname-connlmt-policy-1 limit 1 acl 3000 per-destination per-source amount 2000 1800

\# 在lPv6连接数限制策略12中创建一条规则，规则编号为2，引用ACL 2001，对匹配ACL 2001的连接按照报文的目的地址进行统计和限制，连接数的上限值为200、下限值为100。该规则用于限制2:1::/96网段的主机最多只能同时向外网的同一个目的IP地址发起200条连接，超过200条时，需要等待连接数下降到100以下之后，才允许新建连接。

\<Sysname\> system-view

Sysname acl ipv6 number 2001

Sysname-acl6-basic-2001 rule permit source 2:1::/96

Sysname-acl6-basic-2001 quit

Sysname connection-limit ipv6-policy 12

Sysname-connlmt-ipv6-policy-12 limit 2 acl ipv6 2001 per-destination amount 200 100

【相关命令】

·**connection-limit**

·**display connection-limit**

**连接数限制 \-- 连接数限制配置命令 \-- reset connection-limit statistics**

------------------------------------------------------------------------

**[reset connection-limit statistics**]命令用来清除连接数限制在全局或接口的统计信息。

【命令】

集中式设备：

**[reset connection-limit statistics **[{ **global** \| **interface** *interface-type interface-number  *}]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset connection-limit statistics **[{ **global** \| **interface** *interface-type interface-number* } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[reset connection-limit statistics **[{ **global** \| **interface** *interface-type interface-number* } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：清除全局的连接数限制统计信息[。]

**[interface** *interface-type interface-number*]：清除指定接口上的连接数限制统计信息，*interface-type interface-number*表示接口类型和接口编号[。]

**[slot*** slot-number*]：清除指定单板上全局或全局接口应用的连接数限制统计信息，*slot-number*表示单板所在的槽位号。该参数仅在指定[清除全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（分布式设备－独立运行模式）

**[slot*** slot-number*]：清除指定成员设备上全局或全局接口应用的连接数限制统计信息，*slot-number*表示设备在IRF中的成员编号。该参数仅在指定[清除全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：清除指定成员设备/PEX上全局或全局接口应用的连接数限制统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定[清除全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备的指定单板上全局或全局接口应用的连接数限制统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定[清除全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板上全局或全局接口应用的连接数限制统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定[清除全局的连接数限制统计信息，或上述指定的接口为全局类型的接口（例如]VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU上全局或全局接口的连接数限制统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除接口GigabitEthernet1/0/1上的连接数限制统计信息。（集中式设备）

\<Sysname\> reset connection-limit statistics interface gigabitethernet 1/0/1

\# 清除接口Vlan-interface2上的连接数限制统计信息。（集中式设备）

\<Sysname\> reset connection-limit statistics interface vlan-interface 2

\# 清除2号单板上全局应用的连接数限制统计信息。（分布式设备－独立运行模式）

\<Sysname\> reset connection-limit statistics global slot 2

\# 清除2号成员设备上全局应用的连接数限制统计信息。（集中式IRF设备）

\<Sysname\> reset connection-limit statistics global slot 2

\# 清除1号成员设备上3号单板上全局应用的连接数限制统计信息。（分布式设备－IRF模式）

\<Sysname\> reset connection-limit statistics global chassis 1 slot 2

【相关命令】

·**display connection-limit statistics**

