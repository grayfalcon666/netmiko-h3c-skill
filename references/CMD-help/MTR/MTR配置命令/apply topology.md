<!-- CMD-INDEX
  apply topology                      | 多拓扑策略节点视图        | L16
  display mtr-policy                  | 任意视图             | L58
  display topology                    | 任意视图             | L148
  global-address-family ipv4          | 系统视图             | L250
  if-match ip acl                     | 多拓扑策略节点视图        | L296
  if-match ip dscp                    | 多拓扑策略节点视图        | L342
  if-match ip precedence              | 多拓扑策略节点视图        | L522
  mtr-policy                          | 系统视图             | L606
  routing-table limit                 | 多拓扑实例视图          | L654
  topology                            | 全局地址族视图          | L702
  topology ipv4                       | 接口视图             | L746
  topology-routing mtr-policy         | 全局地址族视图          | L798
-->

**MTR \-- MTR配置命令 \-- apply topology**

------------------------------------------------------------------------

**[apply topology**]命令用来配置多拓扑转发策略节点应用的拓扑。

**[undo apply topology**]命令用来取消该配置。

【命令】

**[apply topology** *topo-name*]

**[undo apply topology**]

【缺省情况】

没有配置多拓扑转发策略节点应用的拓扑。

【视图】

多拓扑策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[topo-name*]：拓扑名，为1～31个字符的字符串，区分大小写。

【举例】

\# 配置多拓扑转发策略mtr的节点0应用拓扑topo1。

\<Sysname\> system-view

Sysname mtr-policy mtr node 0

Sysname-mtr-policy-mtr-0 apply topology topo1

**MTR \-- MTR配置命令 \-- display mtr-policy**

------------------------------------------------------------------------

**[display mtr-policy**]命令显示多拓扑转发策略信息。

【命令】

**[display mtr-policy** [ **name** *mtr-policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***mtr-policy-name*]：多拓扑转发策略名，为1～63个字符的字符串，区分大小写。如果未指定本参数，将显示所有的信息。

【举例】

\# 显示所有的多拓扑转发策略。

\<Sysname\> display mtr-policy

MTR-policy: mtr

  Node: 0

        if-match ip precedence critical

        if-match ip acl 3333

        apply topology 1

MTR-policy: p

  Node: 1

        if-match ip precedence routine

        if-match ip dscp cs1

        if-match ip acl 3501

MTR-policy: q

  Node: 0

        if-match ip precedence network

        if-match ip dscp ef

        if-match ip acl 3001

        apply topology 1

  Node: 1

MTR-policy: w

  Node: 0

        if-match ip precedence routine

        if-match ip dscp 3

表1-1 display mtr-policy命令显示信息描述表

字段

描述

MTR-policy

多拓扑策略名称

Node

多拓扑策略节点

**MTR \-- MTR配置命令 \-- display topology**

------------------------------------------------------------------------

**[display topology**]命令用来显示多拓扑实例的信息。

【命令】

**[display topology ** **name** *topo-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** topo-name*]：显示指定拓扑详细信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有拓扑的概要信息。

【举例】

\# 显示所有拓扑的概要信息。

\<Sysname\> display topology

  Total topologies : 4

  Topology                        Address-family         VRF

  base                            IPv4                   default

  mt1                             IPv4                   default

  mt2                             IPv4                   default

  mt3                             IPv4                   default

\# 显示拓扑mt1的详细信息。

\<Sysname\> display topology name mt1

Topology Name and Index: mt1, 1

Address-family: IPv4

Interfaces: LoopBack0, Vlan-interface1000,

            Vlan-interface1001, Vlan-interface1002,

            Vlan-interface1003

Maximum routes limit : 100

Threshold value(%): 90

表1-2 display topology命令显示信息描述表

字段

描述

Total topologies

已配置的拓扑数量

Topology

拓扑名

Address-family

拓扑所在地址族

VRF

所属VPN

Topology Name and Index

拓扑名和索引号

Interfaces

拓扑关联的接口

Maximum routes limit

拓扑的路由最大路由前缀数

Threshold value(%)

拓扑的路由告警门限值

**MTR \-- MTR配置命令 \-- global-address-family ipv4**

------------------------------------------------------------------------

**[global-address-family ipv4**]命令用来进入全局地址族视图。

**[undo global-address-family ipv4**]命令用来删除全局地址族视图。

【命令】

**[global-address-family ipv4** [ **unicast** ]]

**[undo global-address-family ipv4 ** **unicast** ]

【缺省情况】

没有配置全局地址族视图。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[unicast**]：表示进入IPv4单播视图。如果未指定本参数，也进入IPv4单播视图。

【使用指导】

如果要配置一个多拓扑，首先要通过该命令进入全局地址族视图。

【举例】

\# 进入全局地址族视图。

\<Sysname\> system-view

Sysname global-address-family ipv4 unicast

Sysname-global-ipv4

**MTR \-- MTR配置命令 \-- if-match ip acl**

------------------------------------------------------------------------

**[if-match ip acl**]命令用来配置ACL的匹配条件。

**[undo if-match ip acl**]命令用来取消该配置。

【命令】

**[if-match ip acl** *acl-number*]

**[undo if-match ip acl**]

【缺省情况】

没有配置ACL的匹配条件。

【视图】

多拓扑策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：配置的作为匹配条件的ACL。*acl-number*为高级ACL，取值范围为3000～3999。

【使用指导】

匹配原则：多个匹配条件（ACL、DSCP、IP优先级可以同时配置）之间是"或"的关系，即该节点的匹配条件任何一个满足，则该多拓扑转发策略节点匹配通过，该多拓扑转发策略也匹配通过。反之，该策略节点匹配失败，继续匹配其它节点。

【举例】

\# 创建一个名为mtr的多拓扑策略，其节点序列号为0。定义一条if-match子句，允许ACL 3333的报文通过。

\<Sysname\> system-view

Sysname mtr-policy mtr node 0

Sysname-mtr-policy-mtr-0 if-match ip acl 3333

**MTR \-- MTR配置命令 \-- if-match ip dscp**

------------------------------------------------------------------------

**[if-match ip dscp**]命令用来配置DSCP的匹配条件。

**[undo if-match ip dscp**]命令用来取消该配置。

【命令】

**[if-match ip dscp** *dscp-value*]

**[undo if-match ip dscp**]

【缺省情况】

没有配置DSCP的匹配条件。

【视图】

多拓扑策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DSCP优先级，取值范围为0～63，也可以是关键字，如[表]1-3(?608583865#_Ref378259523)所示。

表1-3 DSCP关键字与值的对应表

关键字

DSCP值（二进制）

DSCP值（十进制）

default

000000

0

af11

001010

10

af12

001100

12

af13

001110

14

af21

010010

18

af22

010100

20

af23

010110

22

af31

011010

26

af32

011100

28

af33

011110

30

af41

100010

34

af42

100100

36

af43

100110

38

cs1

001000

8

cs2

010000

16

cs3

011000

24

cs4

100000

32

cs5

101000

40

cs6

110000

48

cs7

111000

56

ef

101110

46

【使用指导】

匹配原则：多个匹配条件（ACL、DSCP、IP优先级可以同时配置）之间是"或"的关系，即该节点的匹配条件任何一个满足，则该多拓扑转发策略节点匹配通过，该多拓扑转发策略也匹配通过。反之，该策略节点匹配失败，继续匹配其它节点。

【举例】

\# 创建一个名为mtr的多拓扑策略，其节点序列号为0。定义一条if-match子句，允许DSCP值为5的报文通过。

\<Sysname\> system-view

Sysname mtr-policy mtr node 0

Sysname-mtr-policy-mtr-0 if-match ip dscp 5

**MTR \-- MTR配置命令 \-- if-match ip precedence**

------------------------------------------------------------------------

**[if-match ip precedence**]命令用来配置IP优先级的匹配条件。

**[undo if-match ip precedence**]命令用来取消该配置。

【命令】

**[if-match ip precedence** *prec-value*]

**[undo if-match** **ip precedence**]

【缺省情况】

没有配置IP优先级的匹配条件。

【视图】

多拓扑策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prec-value*]：IP优先级，取值范围为0～7，也可以是关键字，如[表]1-4(#_0_29682_x5097_983027819)所示。

表1-4 IP优先级关键字与值的对应表

关键字

IP优先级值

routine

0

priority

1

immediate

2

flash

3

flash-override

4

critical

5

internetwork

6

network

7

【使用指导】

匹配原则：多个匹配条件（ACL、DSCP、IP优先级可以同时配置）之间是"或"的关系，即该节点的匹配条件任何一个满足，则该多拓扑转发策略节点匹配通过，该多拓扑转发策略也匹配通过。反之，该策略节点匹配失败，继续匹配其它节点。

【举例】

\# 创建一个名为mtr的多拓扑策略，其节点序列号为0。定义一条if-match子句，允许IP优先级值为5的报文通过。

\<Sysname\> system-view

Sysname mtr-policy mtr node 0

Sysname-mtr-policy-mtr-0 if-match ip precedence 5

**MTR \-- MTR配置命令 \-- mtr-policy**

------------------------------------------------------------------------

**[mtr-policy**]命令用来创建多拓扑策略节点，并进入多拓扑策略节点视图。如果指定的节点已创建，则该命令直接用来进入该节点的视图。

**[undo mtr-policy**]命令用来删除已创建的多拓扑策略节点。

【命令】

**[mtr-policy** *policy-name* **node** *node-value*]

**[undo mtr-policy** *policy-name* [ **node** *node-value* ]]

【缺省情况】

没有创建多拓扑策略节点。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：多拓扑转发策略名，为1～63个字符的字符串，区分大小写。

**[node** *node-value*]：配置的该多拓扑转发策略的节点，取值范围为0～255，每个多拓扑转发策略可以有多个节点，各个节点之间是或的关系，匹配上该多拓扑转发策略的其中任何一个节点，即匹配上该多拓扑转发策略。

【使用指导】

**[undo mtr-policy ***policy-name*** node ***node-value*]命令用来删除多拓扑转发策略*policy-name*上的值为*node-value*的节点，如果该节点为多拓扑转发策略上的最后一个节点，则删除该多拓扑转发策略。**undo mtr-policy** *policy-name*命令用来删除该多拓扑转发策略。

【举例】

\# 创建多拓扑策略mtr，节点为0，并进入多拓扑策略节点视图。

\<Sysname\> system-view

Sysname mtr-policy mtr node 0

Sysname-mtr-policy-mtr-0

**MTR \-- MTR配置命令 \-- routing-table limit**

------------------------------------------------------------------------

**[routing-table limit**]命令用来配置拓扑支持的最大激活路由前缀数。

**[undo routing-table limit**]命令用来恢复缺省情况。

【命令】

**[routing-table limit**[ *number* { *warn-threshold* \| **simply-alert** }]]

**[undo routing-table limit**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

多拓扑实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：最大激活路由前缀数。不同设备支持的取值范围不同，请以设备的实际情况为准。

*[warn-threshold*]：告警门限值，取值范围为1～100，单位为百分比。当（多拓扑实例中的激活路由前缀数/最大支持激活路由前缀数×100）达到告警门限值时，产生一条告警信息，但仍然允许激活路由前缀。当多拓扑实例中的激活路由前缀数达到最大支持激活路由前缀数目时，不再激活新的路由前缀。

**[simply-alert**]：指定当多拓扑实例的激活路由前缀数超过支持的最大激活路由前缀数目时，可以继续激活新的路由前缀，但会产生一条系统日志信息。

【举例】

\# 配置多拓扑mt1最大可支持1000条激活路由前缀，并且当激活路由前缀数超过最大支持激活路由前缀数时，可以继续激活新的路由前缀，但是会产生一条系统日志信息。

\<Sysname\> system-view

Sysname global-address-family ipv4 unicast

Sysname-global-ipv4 topology mt1

Sysname-af-topology-mt1 routing-table limit 1000 simply-alert

**MTR \-- MTR配置命令 \-- topology**

------------------------------------------------------------------------

**[topology**]命令用来创建一个拓扑，并进入多拓扑视图。

**[undo topology**]命令用来删除一个拓扑。

【命令】

**[topology***topo-name*]

**[undo topology***topo-name*]

【缺省情况】

没有创建拓扑。

【视图】

全局地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[topo-name*]：拓扑名，为1～31个字符的字符串，区分大小写。

【举例】

\# 配置一个拓扑mt。

\<Sysname\> system-view

Sysname global-address-family ipv4 unicast

Sysname-global-ipv4 topology mt

Sysname-af-topology-mt

**MTR \-- MTR配置命令 \-- topology ipv4**

------------------------------------------------------------------------

**[topology ipv4**]命令用来创建并进入接口IPv4单播拓扑视图，将接口与指定拓扑进行关联。

**[undo topology ipv4**]命令用来取消该配置。

【命令】

**[topology ipv4** [ **unicast**  *topo-name*]]

**[undo topology ipv4** [ **unicast**  *topo-name*]]

【缺省情况】

接口与没有关联到任何拓扑。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[unicast**]：单播方式。如果未指定本参数，也表示单播方式。

*[topo-name*]：拓扑名，为1～31个字符的字符串，区分大小写。

【使用指导】

接口关联的拓扑必须已经创建成功。

当拓扑名为"unicast"时，参数**unicast**必须配置，否则命令无法正常下发。

【举例】

\# 将接口LoopBack 0与拓扑mt1进行关联。

\<Sysname\> system-view

Sysname interface loopback 0

Sysname-LoopBack0 topology ipv4 unicast mt1

Sysname-LoopBack0-topology-1

**MTR \-- MTR配置命令 \-- topology-routing mtr-policy**

------------------------------------------------------------------------

**[topology-routing mtr-policy**]命令使能多拓扑转发策略。

**[undo topology-routing mtr-policy**]命令用来关闭多拓扑转发策略。

【命令】

**[topology-routing mtr-policy** *policy-name*]

**[undo topology-routing mtr-policy**]

【缺省情况】

多拓扑转发策略处于关闭状态。

【视图】

全局地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：多拓扑转发策略名，为1～63个字符的字符串，区分大小写。

【举例】

\# 使能多拓扑转发策略mtr。

\<Sysname\> system-view

Sysname global-address-family ipv4

Sysname-global-ipv4 topology-routing mtr-policy mtr

