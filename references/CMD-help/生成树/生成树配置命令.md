<!-- CMD-INDEX
  active region-configuration         | MST域视图           | L60
  bpdu-drop any                       | 二层以太网接口视图        | L112
  check region-configuration          | MST域视图           | L154
  display stp                         | 任意视图             | L244
  display stp abnormal-port           | 任意视图             | L890
  display stp bpdu-statistics         | 任意视图             | L978
  display stp down-port               | 任意视图             | L1238
  display stp history                 | 任意视图             | L1290
  display stp ignored-vlan            | 任意视图             | L1628
  display stp region-configuration    | 任意视图             | L1674
  display stp root                    | 任意视图             | L1758
  display stp tc                      | 任意视图             | L1830
  instance                            | MST域视图           | L2024
  region-name                         | MST域视图           | L2088
  reset stp                           | 用户视图             | L2150
  revision-level                      | MST域视图           | L2184
  snmp-agent trap enable stp          | 系统视图             | L2246
  stp bpdu-protection                 | 系统视图             | L2292
  stp bridge-diameter                 | 系统视图             | L2328
  stp compliance                      | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口 | L2392
  stp config-digest-snooping          | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2442
  stp cost                            | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2496
  stp edged-port                      | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2572
  stp enable                          | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2628
  stp global config-digest-snooping   | 系统视图             | L2682
  stp global enable                   | 系统视图             | L2734
  stp global mcheck                   | 系统视图             | L2782
  stp ignored vlan                    | 系统视图             | L2824
  stp ignore-pvid-inconsistency       | 系统视图             | L2874
  stp loop-protection                 | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2924
  stp max-hops                        | 系统视图             | L2974
  stp mcheck                          | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3018
  stp mode                            | 系统视图             | L3066
  stp no-agreement-check              | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3134
  stp pathcost-standard               | 系统视图             | L3178
  stp point-to-point                  | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3232
  stp port priority                   | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3294
  stp port-log                        | 系统视图             | L3360
  stp priority                        | 系统视图             | L3422
  stp pvst-bpdu-protection            | 系统视图             | L3476
  stp region-configuration            | 系统视图             | L3520
  stp role-restriction                | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3562
  stp root primary                    | 系统视图             | L3606
  stp root secondary                  | 系统视图             | L3666
  stp root-protection                 | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3726
  stp tc-protection                   | 系统视图             | L3776
  stp tc-protection threshold         | 系统视图             | L3820
  stp tc-restriction                  | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3864
  stp tc-snooping                     | 系统视图             | L3908
  stp timer forward-delay             | 系统视图             | L3954
  stp timer hello                     | 系统视图             | L4016
  stp timer max-age                   | 系统视图             | L4078
  stp timer-factor                    | 系统视图             | L4140
  stp transmit-limit                  | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L4190
  stp vlan enable                     | 系统视图             | L4240
  vlan-mapping modulo                 | MST域视图           | L4298
-->

**生成树 \-- 生成树配置命令 \-- active region-configuration**

------------------------------------------------------------------------

**[active region-configuration**]命令用来激活MST域的配置。

【命令】

**[active** **region-configuration**]

【视图】

MST域视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在配置MST域的相关参数（特别是VLAN映射表）时，会引发生成树的重新计算，从而引起网络拓扑的振荡。为了减少网络振荡，新配置的MST域参数并不会马上生效，而是在使用本命令激活，或使用命令**stp global enable**全局开启生成树协议后才会生效。

·在执行本命令前，建议先使用**check region-configuration**命令查看MST域的预配置是否正确，当确认这些配置无误后再执行本命令。

【举例】

\# 将VLAN 2映射到MSTI 1上，并激活该配置。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region instance 1 vlan 2

Sysname-mst-region active region-configuration

【相关命令】

·**check region-configuration**

·**instance**

·**region-name**

·**revision-level**

·**stp global enable**

·**vlan-mapping modulo**

**生成树 \-- 生成树配置命令 \-- bpdu-drop any**

------------------------------------------------------------------------

![说明](生成树命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bpdu-drop any**]命令用来开启端口的BPDU拦截功能。

**[undo bpdu-drop any**]命令用来关闭端口的BPDU拦截功能。

【命令】

**[bpdu-drop any**]

**[undo bpdu-drop any**]

【缺省情况】

端口的BPDU拦截功能处于关闭状态。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在端口GigabitEthernet1/0/1上开启BPDU拦截功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bpdu-drop any

**生成树 \-- 生成树配置命令 \-- check region-configuration**

------------------------------------------------------------------------

**[check region-configuration**]命令用来显示MST域的预配置信息，包括域名、修订级别以及VLAN映射表。

【命令】

**[check region-configuration**]

【视图】

MST域视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·两台或多台开启了生成树协议的设备若要属于同一个MST域，必须同时满足以下两个条件：第一是选择因子（取值为0，不可配）、域名、修订级别和VLAN映射表的配置都相同；第二是这些设备之间的链路相通。

·建议在激活MST域的配置前，先使用本命令查看MST域的预配置是否正确，当确认这些配置无误后再激活MST域的配置。

【举例】

\# 显示MST域的预配置信息。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region check region-configuration

 Admin Configuration

   Format selector      : 0

   Region name          : 001122334400

   Revision level       : 0

   Configuration digest : 0x3ab68794d602fdf43b21c0b37ac3bca8

   Instance  VLANs Mapped

   0         1, 3 to 4094

   15        2

表1-1 check region-configuration命令显示信息描述表

字段

描述

Format selector

生成树协议规定的选择因子，取值为0，不可配

Region name

MST域的域名

Revision level

MST域的修订级别

Configuration digest

配置摘要

Instance   VLANs Mapped

MST域的VLAN与MSTI之间的映射关系，即VLAN映射表

【相关命令】

·**active region-configuration**

·**instance**

·**region-name**

·**revision-level**

·**vlan-mapping modulo**

**生成树 \-- 生成树配置命令 \-- display stp**

------------------------------------------------------------------------

**[display stp**]命令用来显示生成树的状态和统计信息。根据这些信息，可以对网络拓扑结构进行分析与维护，也可以用于查看生成树协议工作是否正常。

【命令】

集中式设备：

**[display stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ]  **interface** *interface-list*   **brief** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list*   **interface** *interface-list* \| **slot** *slot-number* ]  **brief** ]]

分布式设备－IRF模式：

**[display stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list*   **interface** *interface-list* \| **chassis** *chassis-number* **slot** *slot-number* ]  **brief** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[instance*** instance-list*]：显示指定MSTI的生成树状态和统计信息。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。

**[vlan*** vlan-id-list*]：显示指定VLAN的生成树状态和统计信息。*vlan-id-list*为VLAN列表，表示多个VLAN，表示方式为*vlan-id-list* = { *vlan-id* [ **to** vlan*-id*  }&\<1-10\>]。其中，vlan*-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

**[interface*** interface-list*]：显示指定端口上的生成树状态和统计信息。*interface-list*为端口列表，表示多个端口，表示方式为*interface-list* = { *interface-type interface-number* [ **to** *interface-type interface-number*  }&\<1-10\>]。其中，*interface-type*为端口类型，*interface-number*为端口编号。&\<1-10\>表示前面的参数最多可以输入10次。

**[brief**]：显示生成树状态和统计的简要信息。如果未指定本参数，将显示生成树状态和统计的详细信息。

**[slot** *slot-number*]：显示指定单板上的生成树状态和统计信息，*slot-number*表示单板所在的槽位号。如果不指定该参数，将显示所有单板上的生成树状态和统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的生成树状态和统计信息，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，将显示所有成员设备上的生成树状态和统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的生成树状态和统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，将显示所有成员设备/PEX上的生成树状态和统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的生成树状态和统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，将显示所有单板上的生成树状态和统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的生成树状态和统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，将显示所有单板上的生成树状态和统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

(1)在STP/RSTP模式下：

·如果未指定端口，则显示所有端口上的生成树状态和统计信息，显示信息按照端口名称的顺序排列。

·如果指定了端口，则显示该端口上的生成树状态和统计信息，显示信息按照端口名称的顺序排列。

(2)在PVST模式下：

·如果未指定VLAN和端口，则显示所有VLAN在所有端口上的生成树状态和统计信息，显示信息按照VLAN编号的顺序排列，各VLAN内部再按照端口名称的顺序排列。

·如果指定了VLAN但未指定端口，则显示指定VLAN在所有端口上的生成树状态和统计信息，显示信息按照VLAN编号的顺序排列，各VLAN内部再按照端口名称的顺序排列。

·如果指定了端口但未指定VLAN，则显示所有VLAN在指定端口上的生成树状态和统计信息，显示信息按照VLAN编号的顺序排列，各VLAN内部再按照端口名称的顺序排列。

·如果同时指定了VLAN和端口，则显示指定VLAN在指定端口上的生成树状态和统计信息，显示信息按照VLAN编号的顺序排列，各VLAN内部再按照端口名称的顺序排列。

(3)在MSTP模式下：

·如果未指定MSTI和端口，则显示所有MSTI在所有端口上的生成树状态和统计信息，显示信息按照MSTI编号的顺序排列，各MSTI内部再按照端口名称的顺序排列。

·如果指定了MSTI但未指定端口，则显示指定MSTI在所有端口上的生成树状态和统计信息，显示信息按照MSTI编号的顺序排列，各MSTI内部再按照端口名称的顺序排列。

·如果指定了端口但未指定MSTI，则显示所有MSTI在指定端口上的生成树状态和统计信息，显示信息按照MSTI编号的顺序排列，各MSTI内部再按照端口名称的顺序排列。

·如果同时指定了MSTI和端口，则显示指定MSTI在指定端口上的生成树状态和统计信息，显示信息按照MSTI编号的顺序排列，各MSTI内部再按照端口名称的顺序排列。

【举例】

\# 在MSTP模式下，显示MSTI 0在端口GigabitEthernet1/0/1～GigabitEthernet1/0/4上生成树状态和统计的简要信息。

\<Sysname\> display stp instance 0 interface gigabitethernet 1/0/1 to gigabitethernet 1/0/4 brief

 MST ID      Port                         Role  STP State     Protection

 0           GigabitEthernet1/0/1         ALTE  DISCARDING    LOOP

 0           GigabitEthernet1/0/2         DESI  FORWARDING    NONE

 0           GigabitEthernet1/0/3         DESI  FORWARDING    NONE

 0           GigabitEthernet1/0/4         DESI  FORWARDING    NONE

\# 在PVST模式下，显示VLAN 2在端口GigabitEthernet1/0/1～GigabitEthernet1/0/4上生成树状态和统计的简要信息。

\<Sysname\> system-view

Sysname stp mode pvst

Sysname display stp vlan 2 interface gigabitethernet 1/0/1 to gigabitethernet 1/0/4 brief

 VLAN ID     Port                         Role  STP State     Protection

 2           GigabitEthernet1/0/1         ALTE  DISCARDING    LOOP

 2           GigabitEthernet1/0/2         DESI  FORWARDING    NONE

 2           GigabitEthernet1/0/3         DESI  FORWARDING    NONE

 2           GigabitEthernet1/0/4         DESI  FORWARDING    NONE

表1-2 display stp brief命令显示信息描述表

字段

描述

MST ID

MSTI的编号

VLAN ID

VLAN的编号

Port

端口名称，和相应的MSTI对应

Role

端口角色：

·ALTE：表示替换端口

·BACK：表示备份端口

·ROOT：表示根端口

·DESI：表示指定端口

·MAST：表示主端口

·DISA：表示失效端口

STP State

端口状态：

·FORWARDING：表示可以接收和发送BPDU，也转发用户流量

·DISCARDING：表示可以接收和发送BPDU，但不转发用户流量

·LEARNING：表示可以接收和发送BPDU，但不转发用户流量，是一种过渡状态

Protection

端口上的保护类型：

·ROOT：表示根保护

·LOOP：表示环路保护

·BPDU：表示BPDU保护

·NONE：表示无保护

\# 在MSTP模式下，显示所有MSTI在所有端口上的生成树状态和统计的详细信息。

\<Sysname\> display stp

\-\-\-\-\-\--[CIST Global InfoMode MSTP\-\-\-\-\-\--]

 Bridge ID           : 32768.0001-0000-0000

 Bridge times        : Hello 2s MaxAge 20s FwdDelay 15s MaxHops 20

 Root ID/ERPC        : 32768.0001-0000-0000, 0

 RegRoot ID/IRPC     : 32768.0001-0000-0000, 0

 RootPort ID         : 0.0

 BPDU-Protection     : Disabled

 Bridge Config-

 Digest-Snooping     : Disabled

 TC or TCN received  : 2

 Time since last TC  : 0 days 0h:0m:58s

\-\-\--[Port3(Ethernet0/0/2)FORWARDING\-\-\--]

 Port protocol       : Enabled

 Port role           : Designated Port (Boundary)

 Port ID             : 128.3

 Port cost(Legacy)   : Config=auto, Active=200

 Desg.bridge/port    : 32768.0001-0000-0000, 128.3

 Port edged          : Config=disabled, Active=disabled

 Point-to-Point      : Config=auto, Active=true

 Transmit limit      : 10 packets/hello-time

 TC-Restriction      : Disabled

 Role-Restriction    : Disabled

 Protection type     : Config=none, Active=none

 MST BPDU format     : Config=auto, Active=802.1s

 Port Config-

 Digest-Snooping     : Disabled

 Rapid transition    : True

 Num of VLANs mapped : 0

 Port times          : Hello 2s MaxAge 20s FwdDelay 15s MsgAge 0s RemHops 20

 BPDU sent           : 32

          TCN: 0, Config: 0, RST: 0, MST: 32

 BPDU received       : 2

          TCN: 0, Config: 0, RST: 0, MST: 2

\-\-\-\-\-\--[MSTI 1 Global Info\-\-\-\-\-\--]

 Bridge ID           : 32768.0001-0000-0000

 RegRoot ID/IRPC     : 32768.0001-0000-0000, 0

 RootPort ID         : 0.0

 Master bridge       : 32768.0001-0000-0000

 Cost to master      : 0

 TC received         : 0

\-\-\--[Port3(Ethernet0/0/2)FORWARDING\-\-\--]

 Port protocol       : Enabled

 Port role           : Designated Port (Boundary)

 Port ID             : 128.3

 Port cost(Legacy)   : Config=auto, Active=200

 Desg.bridge/port    : 32768.0001-0000-0000, 128.3

 Protection type     : Config=none, Active=none

 Rapid transition    : True

 Num of VLANs mapped : 64

 Port times          : RemHops 20

\# 在PVST模式下，显示所有VLAN在所有端口上的生成树状态和统计信息。

\<Sysname\> system-view

Sysname stp mode pvst

Sysname display stp

\-\-\-\-\-\--[VLAN 1 Global Info\-\-\-\-\-\--]

Protocol status     : Enabled

Bridge ID           : 32768.000f-e200-2200

Bridge times        : Hello 2s MaxAge 20s FwdDelay 15s

VlanRoot ID/RPC     : 0.00e0-fc0e-6554, 200200

RootPort ID         : 128.48

BPDU-Protection     : Disabled

TC or TCN received  : 2

Time since last TC  : 0 days 0h:5m:42s

 \-\-\--[Port1(GigabitEthernet1/0/1)FORWARDING\-\-\--]

 Port protocol       : Enabled

 Port role           : Designated Port

 Port ID             : 128.153

 Port cost(Legacy)   : Config=auto, Active=200

 Desg. bridge/port   : 32768.000f-e200-2200, 128.2

 Port edged          : Config=disabled, Active=disabled

 Point-to-Point      : Config=auto, Active=true

 Transmit limit      : 10 packets/hello-time

 Protection type     : Config=none, Active=none

 Rapid transition    : False

 Port times          : Hello 2s MaxAge 20s FwdDelay 15s MsgAge 2s

\-\-\-\-\-\--[VLAN 2 Global Info\-\-\-\-\-\--]

Protocol status      : Enabled

Bridge ID            : 32768.000f-e200-2200

Bridge times         : Hello 2s MaxAge 20s FwDly 15s

VlanRoot ID/RPC      : 0.00e0-fc0e-6554, 200200

RootPort ID          : 128.48

BPDU-Protection      : Disabled

TC or TCN received   : 2

Time since last TC   : 0 days 0h:5m:42s

\# 当生成树协议未开启时，在MSTP模式下显示生成树的状态和统计信息。

\<Sysname\> display stp

 Protocol status    : Disabled

 Protocol Std.      : IEEE 802.1s

 Version            : 3

 Bridge-Prio.       : 32768

 MAC address        : 000f-e200-8048

 Max age(s)         : 20

 Forward delay(s)   : 15

 Hello time(s)      : 2

 Max hops           : 20

 TC Snooping        : Disabled

\# 当生成树协议未开启时，在PVST模式下显示生成树的状态和统计信息。

\<Sysname\> display stp

 Protocol status    : Disabled

 Protocol Std.      : IEEE 802.1w (pvst)

 Version            : 2

 Bridge-Prio.       : 32768

 MAC address        : 3822-d69f-0800

 Max age(s)         : 20

 Forward delay(s)   : 15

 Hello time(s)      : 2

 TC Snooping        : Disabled

表1-3 display stp命令显示信息描述表

字段

描述

Bridge ID

网桥ID，由两部分构成："."之前和之后的内容分别表示为本设备的优先级和本设备的MAC地址。譬如，"32768.000f-e200-2200"表示本设备的优先级为32768，其MAC地址为000F-E200-2200

Bridge times

网桥相关的主要参数值：

·Hello：表示Hello time定时器值

·MaxAge：表示Max Age定时器值

·FwdDelay：表示Forward delay定时器值

·MaxHops：表示MST域的最大跳数

Root ID/ERPC

总根ID/外部路径开销（即本设备到总根的路径开销）

RegRoot ID/IRPC

域根ID/内部路径开销（即本设备到域根的路径开销）

VlanRoot ID/RPC

VLAN根桥ID/根路径开销（即本设备到该VLAN根桥的路径开销）

RootPort ID

根端口的端口ID。"0.0"表示本设备为根设备，没有根端口

BPDU-Protection

BPDU保护功能的全局开启状态

Bridge Config-

Digest-Snooping

摘要侦听功能的全局开启状态

TC or TCN received

MSTI或VLAN收到的TC及TCN报文数

Time since last TC

MSTI或VLAN最近一次拓扑变化时间

FORWARDING

端口状态为Forwarding状态

DISCARDING

端口状态为Discarding状态

LEARNING

端口状态为Learning状态

Port protocol

生成树协议在端口上的开启状态

Port role

端口角色，和MSTI相对应。具体角色分为：Alternate、Backup、Root、Designated、Master、Disabled

(Boundary)

表示该端口为域边界端口

Port ID

端口ID

Port cost(Legacy)

端口的路径开销（Legacy表示当前设备的路径开销的计算方法，此外还有dot1d-1998和dot1t两种计算方式）：

·Config：表示配置值

·Active：表示实际值

Desg.bridge/port

端口的指定桥ID和端口ID（对于不支持端口优先级的端口，这里显示的端口ID没有意义）

Port edged

端口是否为边缘端口：

·Config：表示配置值

·Active：表示实际值

Point-to-Point

端口是否与点对点链路相连：

·Config：表示配置值

·Active：表示实际值

Transmit limit

端口每个Hello Time时间间隔发送报文的上限

Protection type

端口是否开启保护：

·Config：表示配置值

·Active：表示实际值

端口遇到异常情况启动保护的类型：

·ROOT：表示根保护

·LOOP：表示环路保护

·BPDU：表示BPDU保护

·PVST BPDU：表示MSTP的PVST BPDU保护

·NONE：表示无保护

TC-Restriction

端口是否开启了TC-BPDU传播限制功能

Role-Restriction

端口是否开启了端口角色限制功能

MST BPDU format

端口发送MSTP报文的格式，取值为legacy和802.1s：

·Config：表示配置值

·Active：表示实际值

Port Config-

Digest-Snooping

摘要侦听功能在端口上的开启状态

Rapid transition

端口在当前MSTI或VLAN中是否快速迁移至转发状态

Num of VLANs mapped

端口在当前MSTI中的VLAN计数

Port times

端口相关的主要参数值：

·Hello：表示Hello time定时器值

·MaxAge：表示Max Age定时器值

·FwdDelay：表示Forward delay定时器值

·MsgAge：表示Message Age定时器值

·RemHops：表示剩余跳数

BPDU sent

端口发送报文计数

BPDU received

端口接收报文计数

RegRoot ID/IRPC

MSTI域根/内部路径开销

Root Type

MSTI域根类型：

·Primary root：表示根桥

·Secondary root：表示备份根桥

Master bridge

MSTI的Master桥ID

Cost to master

MSTI到Master桥的路径开销

TC received

MSTI收到的TC报文数

Protocol status

生成树协议的全局开启状态

Protocol Std.

生成树协议采用的协议标准

Version

生成树协议采用的协议版本

Bridge-Prio.

在MSTP模式下，表示本设备在CIST中的桥优先级；在PVST模式下，表示本设备在VLAN 1中的桥优先级

MAC address

本设备的MAC地址

Max age(s)

BPDU的最大生存时间（单位为秒，在PVST模式下为在VLAN 1中的配置）

Forward delay(s)

端口状态迁移的延时（单位为秒，在PVST模式下为在VLAN 1中的配置）

Hello time(s)

根设备发送BPDU的周期（单位为秒，在PVST模式下为在VLAN 1中的配置）

Max hops

MST域中的最大跳数

TC Snooping

TC Snooping开启状态

【相关命令】

·**reset stp**

**生成树 \-- 生成树配置命令 \-- display stp abnormal-port**

------------------------------------------------------------------------

**[display stp abnormal-port**]命令用来显示被生成树保护功能阻塞的端口信息。

【命令】

**[display stp abnormal-port**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 在MSTP模式下，显示被生成树保护功能阻塞的端口信息。

\<Sysname\> display stp abnormal-port

 MST ID      Blocked Port                 Reason

 1           GigabitEthernet1/0/1         Root-Protected

 2           GigabitEthernet1/0/2         Loop-Protected

 12          GigabitEthernet1/0/3         Loopback-Protected

\# 在PVST模式下，显示被生成树保护功能阻塞的端口信息。

\<Sysname\> system-view

Sysname stp mode pvst

Sysname display stp abnormal-port

 VLAN ID      Blocked Port                 Reason

 1            GigabitEthernet1/0/1         Root-Protected

 2            GigabitEthernet1/0/2         Loop-Protected

 2            GigabitEthernet1/0/3         Loopback-Protected

表1-4 display stp abnormal-port命令显示信息描述表

字段

描述

MST ID

被生成树保护功能阻塞的端口所在MSTI的编号

VLAN ID

被生成树保护功能阻塞的端口所在VLAN的编号

Blocked Port

被生成树保护功能阻塞的端口的名称

Reason

导致端口阻塞的原因：

·Root-Protected：表示发生了根保护

·Loop-Protected：表示发生了环路保护

·Loopback-Protected：表示发生了自环保护，即有实例端口收到了自己发出的协议报文

·Disputed：表示发生了Dispute保护，即端口收到了非阻塞指定端口发出的低优先级消息

·InconsistentPortType-Protected：表示发生了端口类型不一致保护

·InconsistentPvid-Protected：表示发生了PVID不一致保护

**生成树 \-- 生成树配置命令 \-- display stp bpdu-statistics**

------------------------------------------------------------------------

**[display stp bpdu-statistics**]命令用来显示端口上的BPDU统计信息。

【命令】

**[display stp bpdu-statistics** [ **interface** *interface-type interface-number* [ **instance** *instance-list*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：显示指定端口上的BPDU统计信息，*interface-type interface-number*表示端口类型和端口编号。

**[instance ***instance-list*]：显示指定MSTI在端口上的BPDU统计信息。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

(1)在MSTP模式下：

·如果未指定端口和MSTI，则显示所有MSTI在所有端口上的BPDU统计信息，显示信息按照端口名称的顺序排列，各端口内部再按照MSTI编号的顺序排列。

·如果指定了端口但未指定MSTI，则显示所有MSTI在该端口上的BPDU统计信息，显示信息按照MSTI编号的顺序排列。

·如果同时指定了MSTI和端口，则显示指定MSTI在指定端口上的BPDU统计信息。

(2)在STP/RSTP/PVST模式下：

·如果未指定端口，则显示所有端口上的BPDU统计信息，显示信息按照端口名称的顺序排列。

·如果指定了端口，则显示该端口上的BPDU统计信息。

【举例】

\# 在MSTP模式下，显示所有MSTI在端口GigabitEthernet1/0/1上的BPDU统计信息。

\<Sysname\> display stp bpdu-statistics interface gigabitethernet 1/0/1

 Port: GigabitEthernet1/0/1

 Instance-Independent:

 Type                        Count      Last Updated

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Invalid BPDUs               0

 Looped-back BPDUs           0

 Max-aged BPDUs              0

 TCN sent                    0

 TCN received                0

 TCA sent                    0

 TCA received                2          10:33:12 01/13/2011

 Config sent                 0

 Config received             0

 RST sent                    0

 RST received                0

 MST sent                    4          10:33:11 01/13/2011

 MST received                151        10:37:43 01/13/2011

 Instance 0:

 Type                        Count      Last Updated

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Timeout BPDUs               0

 Max-hoped BPDUs             0

 TC detected                 1          10:32:40 01/13/2011

 TC sent                     3          10:33:11 01/13/2011

 TC received                 0

\# 在PVST模式下，显示端口GigabitEthernet1/0/1上的BPDU统计信息。

\<Sysname\> system-view

Sysname stp mode pvst

Sysname display stp bpdu-statistics interface gigabitethernet 1/0/1

 Port: GigabitEthernet1/0/1

 Type                        Count      Last Updated

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Invalid BPDUs               0

 Looped-back BPDUs           0

 Max-aged BPDUs              0

 TCN sent                    0

 TCN received                0

 TCA sent                    0

 TCA received                2           10:33:12 01/13/2010

 Config sent                 0

 Config received             0

 RST sent                    0

 RST received                0

 MST sent                    4           10:33:11 01/13/2010

 MST received                151         10:37:43 01/13/2010

 Timeout BPDUs               0

 Max-hoped BPDUs             0

 TC detected                 511         10:32:40 01/13/2010

 TC sent                     8844        10:33:11 01/13/2010

 TC received                 1426        10:33:32 01/13/2010

 PVID inconsistency BPDUs    0

表1-5 display stp bpdu-statistics命令显示信息描述表

字段

描述

Port

端口名称

Instance-Independent

与MSTI无关的统计信息

Type

统计类型

Count

统计值

Last Updated

最后更新时间

Invalid BPDUs

无效BPDU的数量

Looped-back BPDUs

自环（即收到由本端口发出）的BPDU数量

Max-aged BPDUs

超过最大生存时间的BPDU数量

TCN sent

发出的TCN报文数量

TCN received

收到的TCN报文数量

TCA sent

发出的TCA报文数量

TCA received

收到的TCA报文数量

Config sent

发出的Configuration报文数量

Config received

收到的Configuration报文数量

RST sent

发出的RSTP BPDU数量

RST received

收到的RSTP BPDU数量

MST sent

发出的MSTP BPDU数量

MST received

收到的MSTP BPDU数量

Instance

与指定MSTI相关的统计信息

Timeout BPDUs

老化的BPDU数量

Max-hoped BPDUs

超过最大跳数的BPDU数量

TC detected

监测到的拓扑变化的次数

TC sent

发出的TC报文数量

TC received

收到的TC报文数量

PVID inconsistency BPDUs

收到的PVID不一致的PVST报文数量

**生成树 \-- 生成树配置命令 \-- display stp down-port**

------------------------------------------------------------------------

**[display stp down-port**]命令用来显示被生成树保护功能down掉的端口信息。

【命令】

**[display stp down-port**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示被生成树保护功能down掉的端口信息。

\<Sysname\> display stp down-port

 Down Port                     Reason

 GigabitEthernet1/0/1          BPDU protection

表1-6 display stp down-port命令显示信息描述表

字段

描述

Down Port

被生成树保护功能down掉的端口名称

Reason

导致端口down的原因：

·BPDUprotection：表示BPDU保护

·PVST BPDU protection：表示MSTP的PVST BPDU保护

**生成树 \-- 生成树配置命令 \-- display stp history**

------------------------------------------------------------------------

**[display stp history**]命令用来显示生成树端口角色计算的历史信息。

【命令】

集中式设备：

**[display stp **[[ **instance** *instance-list* \| **vlan** ]]*vlan-id-list * **history**]

分布式设备－独立运行模式/集中式IRF设备：

**[display stp **[[ **instance** *instance-list* \| **vlan** ]]*vlan-id-list* **history**  **slot** *slot-number* ]

分布式设备－IRF模式：

**[display stp **[[ **instance** *instance-list* \| **vlan** ]]*vlan-id-list* **history**  **chassis** *chassis-number* **slot** *slot-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[instance*** instance-list*]：显示指定MSTI中端口角色计算的历史信息。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。

**[vlan*** vlan-id-list*]：显示指定VLAN中端口角色计算的历史信息。*vlan-id-list*为VLAN的列表，表示多个VLAN，表示方式为*vlan-id-list* = { *vlan-id* [ **to** vlan*-id*  }&\<1-10\>]。其中，vlan*-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

**[slot** *slot-number*]：显示指定单板上端口角色计算的历史信息，*slot-number*表示单板所在的槽位号。如果不指定该参数，将显示所有单板上端口角色计算的历史信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上端口角色计算的历史信息，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，将显示所有成员设备上端口角色计算的历史信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上端口角色计算的历史信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，将显示所有成员设备/PEX上端口角色计算的历史信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上端口角色计算的历史信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，将显示所有单板上端口角色计算的历史信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上端口角色计算的历史信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，将显示所有单板上端口角色计算的历史信息。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

(1)在STP/RSTP模式下，显示信息按照端口角色计算的时间先后顺序排列。

(2)在PVST模式下：

·如果未指定VLAN，则显示所有VLAN中端口角色计算的历史信息，显示信息按照VLAN编号的顺序排列，各VLAN内部再按照端口角色计算的时间先后顺序排列。

·如果指定了VLAN，则显示指定VLAN中端口角色计算的历史信息，显示信息按照VLAN编号的顺序排列，各VLAN内部再按照端口角色计算的时间先后顺序排列。

(3)在MSTP模式下：

·如果未指定MSTI，则显示所有MSTI中端口角色计算的历史信息，显示信息按照MSTI编号的顺序排列，各MSTI内部再按照端口角色计算的时间先后顺序排列。

·如果指定了MSTI，则显示指定MSTI中端口角色计算的历史信息，显示信息按照MSTI编号的顺序排列，各MSTI内部再按照端口角色计算的时间先后顺序排列。

【举例】

·集中式设备应用

\# 在MSTP模式下，显示MSTI 2中端口角色计算的历史信息。

\<Sysname\> display stp instance 2 history

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  Instance 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Port GigabitEthernet1/0/1

   Role change         : ROOT-\>DESI (Aged)

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

 Port GigabitEthernet1/0/2

   Role change         : ALTER-\>ROOT

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

                         128.153

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

                         128.153

\# 在PVST模式下，显示VLAN 2中端口角色计算的历史信息。

\<Sysname\> display stp vlan 2 history

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  VLAN 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Port GigabitEthernet1/0/1

   Role change         : ROOT-\>DESI (Aged)

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

 Port GigabitEthernet1/0/2

   Role change         : ALTER-\>ROOT

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

·分布式设备－独立运行模式应用

\# 在MSTP模式下，显示1号单板上MSTI 2中端口角色计算的历史信息。

\<Sysname\> display stp instance 2 history slot 1

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 history trace \-\-\-\-\-\-\-\-\-\-\-\-\-\--

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  Instance 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Port GigabitEthernet1/0/1

   Role change         : ROOT-\>DESI (Aged)

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

 Port GigabitEthernet1/0/2

   Role change         : ALTER-\>ROOT

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

                         128.153

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

                         128.153

\# 在PVST模式下，显示1号单板上VLAN 2中端口角色计算的历史信息。

\<Sysname\> display stp vlan 2 history slot 1

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 history trace \-\-\-\-\-\-\-\-\-\-\-\-\-\--

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  VLAN 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Port GigabitEthernet1/0/1

   Role change         : ROOT-\>DESI (Aged)

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

 Port GigabitEthernet1/0/2

   Role change         : ALTER-\>ROOT

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

·集中式IRF设备应用

\# 在MSTP模式下，显示1号成员设备上MSTI 2中端口角色计算的历史信息。

\<Sysname\> display stp instance 2 history slot 1

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 history trace \-\-\-\-\-\-\-\-\-\-\-\-\-\--

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  Instance 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Port GigabitEthernet1/0/1

   Role change         : ROOT-\>DESI (Aged)

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

 Port GigabitEthernet1/0/2

   Role change         : ALTER-\>ROOT

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

                         128.153

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

                         128.153

\# 在PVST模式下，显示1号成员设备上VLAN 2中端口角色计算的历史信息。

\<Sysname\> display stp vlan 2 history slot 1

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 history trace \-\-\-\-\-\-\-\-\-\-\-\-\-\--

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  VLAN 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Port GigabitEthernet1/0/1

   Role change         : ROOT-\>DESI (Aged)

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

 Port GigabitEthernet1/0/2

   Role change         : ALTER-\>ROOT

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

·分布式设备－IRF模式应用

\# 在MSTP模式下，显示1号成员设备的1号单板上MSTI 2中端口角色计算的历史信息。

\<Sysname\> display stp instance 2 history chassis 1 slot 1

 \-\-\-\-\-\-\-\-\-- STP chassis 1 slot 1 history trace \-\-\-\-\-\-\--

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  Instance 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Port GigabitEthernet1/1/0/1

   Role change         : ROOT-\>DESI (Aged)

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

 Port GigabitEthernet1/1/0/2

   Role change         : ALTER-\>ROOT

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

                         128.153

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

                         128.153

\# 在PVST模式下，显示1号成员设备的1号单板上VLAN 2中端口角色计算的历史信息。

\<Sysname\> display stp vlan 2 history chassis 1 slot 1

 \-\-\-\-\-\-\-\-\-- STP chassis 1 slot 1 history trace \-\-\-\-\-\-\--

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--  VLAN 2   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Port GigabitEthernet1/1/0/1

   Role change         : ROOT-\>DESI (Aged)

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.1

 Port GigabitEthernet1/1/0/2

   Role change         : ALTER-\>ROOT

   Time                : 2009/02/08 00:22:56

   Port priority       : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

   Designated priority : 0.00e0-fc01-6510 0 0.00e0-fc01-6510 128.2

表1-7 display stp history命令显示信息描述表

字段

描述

Port

端口名称

Role change

显示端口的角色变化（Aged表示由于报文超时引起的角色变化）

Time

端口角色计算时间

Port priority

端口优先级

Designated priority

指定优先级

**生成树 \-- 生成树配置命令 \-- display stp ignored-vlan**

------------------------------------------------------------------------

![说明](生成树命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display stp ignored-vlan**]命令用来显示已开启VLAN Ignore功能的VLAN列表。

【命令】

**[display stp ignored-vlan**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示已开启VLAN Ignore功能的VLAN列表。

\<Sysname\> display stp ignored-vlan

 STP-Ignored VLANs: 1 to 2, 4

表1-8 display stp ignored-vlan命令显示信息描述表

字段

描述

STP-Ignored VLANs

已开启VLAN Ignore功能的VLAN，None表示尚无VLAN开启VLAN Ignore功能

**生成树 \-- 生成树配置命令 \-- display stp region-configuration**

------------------------------------------------------------------------

**[display stp region-configuration**]命令用来显示当前生效的MST域配置信息，包括域名、修订级别以及VLAN映射表。

【命令】

**[display stp region-configuration**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 在MSTP模式下，显示当前生效的MST域配置信息。

\<Sysname\> display stp region-configuration

 Oper Configuration

   Format selector      : 0

   Region name          : hello

   Revision level       : 0

   Configuration digest : 0x5f762d9a46311effb7a488a3267fca9f

   Instance   VLANs Mapped

   0          21 to 4094

   1          1 to 10

   2          11 to 20

表1-9 display stp region-configuration命令显示信息描述表

字段

描述

Format selector

生成树协议规定的选择因子，缺省值为0，不可配置

Region name

MST域的域名

Revision level

MST域的修订级别，可使用命令**revision-level**来配置，缺省为0级

Configuration digest

配置摘要

VLANs Mapped

映射到MSTI的VLAN

【相关命令】

·**instance**

·**region-name**

·**revision-level**

·**vlan-mapping modulo**

**生成树 \-- 生成树配置命令 \-- display stp root**

------------------------------------------------------------------------

**[display stp root**]命令用来显示所有生成树的根桥信息。

【命令】

**[display stp root**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 在MSTP模式下，显示所有生成树的根桥信息。

\<Sysname\> display stp root

 MST ID  Root Bridge ID        ExtPathCost IntPathCost Root Port

 0       0.00e0-fc0e-6554      200200      0           GigabitEthernet1/0/1

\# 在PVST模式下，显示所有生成树的根桥信息。

\<Sysname\> display stp root

 VLAN ID  Root Bridge ID        ExtPathCost IntPathCost Root Port

 1        0.00e0-fc0e-6554      200200      0           GigabitEthernet1/0/1

表1-10 display stp root命令显示信息描述表

字段

描述

MST ID

MSTI的编号

VLAN ID

VLAN的编号

Root Bridge ID

根桥的编号

ExtPathCost

外部路径开销。设备可自动计算端口的缺省路径开销，用户也可使用命令**stp cost**来配置端口的路径开销

IntPathCost

内部路径开销。设备可自动计算端口的缺省路径开销，用户也可使用命令**stp cost**来配置端口的路径开销

Root Port

根端口名称（若当前设备的某个端口是MSTI的根端口则显示，否则不显示）

**生成树 \-- 生成树配置命令 \-- display stp tc**

------------------------------------------------------------------------

**[display stp tc**]命令用来显示生成树所有端口收发的TC或TCN报文数。

【命令】

集中式设备：

**[display stp **[[ **instance** *instance-list* \| **vlan** ]]*vlan-id-list * **tc**]

分布式设备－独立运行模式/集中式IRF设备：

**[display stp **[[ **instance** *instance-list* \| **vlan** ]]*vlan-id-list* **tc**  **slot** *slot-number* ]

分布式设备－IRF模式：

**[display stp **[[ **instance** *instance-list* \| **vlan** ]]*vlan-id-list* **tc**  **chassis** *chassis-number* **slot** *slot-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[instance*** instance-list*]：显示指定MSTI中所有端口收发的TC或TCN报文数。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。

**[vlan*** vlan-id-list*]：显示指定VLAN中所有端口收发的TC或TCN报文数。*vlan-id-list*为VLAN列表，表示多个VLAN，表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

**[slot** *slot-number*]：显示指定单板上所有端口收发的TC或TCN报文数，*slot-number*表示单板所在的槽位号。如果不指定该参数，将显示所有单板上所有端口收发的TC或TCN报文数。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上所有端口收发的TC或TCN报文数，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，将显示所有成员设备上所有端口收发的TC或TCN报文数。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上所有端口收发的TC或TCN报文数，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定该参数，将显示所有成员设备/PEX上所有端口收发的TC或TCN报文数。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上所有端口收发的TC或TCN报文数，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，将显示所有单板上所有端口收发的TC或TCN报文数。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上所有端口收发的TC或TCN报文数，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定该参数，将显示所有单板上所有端口收发的TC或TCN报文数。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

(1)在STP/RSTP模式下，显示信息按照端口名称的顺序排列。

(2)在PVST模式下：

·如果未指定VLAN，则显示所有VLAN中所有端口收发的TC或TCN报文数，显示信息按照VLAN编号的顺序排列，各VLAN内部再按照端口名称的顺序排列。

·如果指定了VLAN，则显示指定VLAN中所有端口收发的TC或TCN报文数，显示信息按照VLAN编号的顺序排列，各VLAN内部再按照端口名称的顺序排列。

(3)在MSTP模式下：

·如果未指定MSTI，则显示所有MSTI中所有端口收发的TC或TCN报文数，显示信息按照MSTI编号的顺序排列，各MSTI内部再按照端口名称的顺序排列。

·如果指定了MSTI，则显示指定MSTI中所有端口收发的TC或TCN报文数，显示信息按照MSTI编号的顺序排列，各MSTI内部再按照端口名称的顺序排列。

【举例】

·集中式设备应用

\# 在MSTP模式下，显示MSTI 0中所有端口收发的TC或TCN报文数。

\<Sysname\> display stp instance 0 tc

 MST ID      Port                       Receive      Send

 0           GigabitEthernet1/0/1       6            4

 0           GigabitEthernet1/0/2       0            2

\# 在PVST模式下，显示VLAN 2中所有端口收发的TC或TCN报文数。

\<Sysname\> display stp vlan 2 tc

 VLAN ID     Port                       Receive      Send

 2           GigabitEthernet1/0/1       6            4

 2           GigabitEthernet1/0/2       0            2

·分布式设备－独立运行模式应用

\# 在MSTP模式下，显示1号单板上MSTI 0中所有端口收发的TC或TCN报文数。

\<Sysname\> display stp instance 0 tc slot 1

 \-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 TC or TCN count \-\-\-\-\-\-\-\-\-\-\-\--

 MST ID      Port                       Receive      Send

 0           GigabitEthernet1/0/1       6            4

 0           GigabitEthernet1/0/2       0            2

\# 在PVST模式下，显示1号单板上VLAN 2中所有端口收发的TC或TCN报文数。

\<Sysname\> display stp vlan 2 tc slot 1

 \-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 TC or TCN count \-\-\-\-\-\-\-\-\-\-\-\--

 VLAN ID     Port                       Receive      Send

 2           GigabitEthernet1/0/1       6            4

 2           GigabitEthernet1/0/2       0            2

·集中式IRF设备应用

\# 在MSTP模式下，显示1号成员设备上MSTI 0中所有端口收发的TC或TCN报文数。

\<Sysname\> display stp instance 0 tc slot 1

 \-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 TC or TCN count \-\-\-\-\-\-\-\-\-\-\-\--

 MST ID      Port                       Receive      Send

 0           GigabitEthernet1/0/1       6            4

 0           GigabitEthernet1/0/2       0            2

\# 在PVST模式下，显示1号成员设备上VLAN 2中所有端口收发的TC或TCN报文数。

\<Sysname\> display stp vlan 2 tc slot 1

 \-\-\-\-\-\-\-\-\-\-\-\-\-- STP slot 1 TC or TCN count \-\-\-\-\-\-\-\-\-\-\-\--

VLAN ID     Port                       Receive      Send

 2           GigabitEthernet1/0/1      6            4

 2           GigabitEthernet1/0/2      0            2

·分布式设备－IRF模式应用

\# 在MSTP模式下，显示1号成员设备的1号单板上MSTI 0中所有端口收发的TC或TCN报文数。

\<Sysname\> display stp instance 0 tc chassis 1 slot 1

 \-\-\-\-\-\-\-\-- STP chassis 1 slot 1 TC or TCN count \-\-\-\-\-\-\--

 MST ID      Port                       Receive      Send

 0           GigabitEthernet1/1/0/1     6            4

 0           GigabitEthernet1/1/0/2     0            2

\# 在PVST模式下，显示1号成员设备的1号单板上VLAN 2中所有端口收发的TC或TCN报文数。

\<Sysname\> display stp vlan 2 tc chassis 1 slot 1

 \-\-\-\-\-\-\-\-- STP chassis 1 slot 1 TC or TCN count \-\-\-\-\-\-\--

 VLAN ID     Port                       Receive      Send

 2           GigabitEthernet1/1/0/1     6            4

 2           GigabitEthernet1/1/0/2     0            2

表1-11 display stp tc命令显示信息描述表

字段

描述

MST ID

MSTI的编号

VLAN ID

VLAN的编号

Port

端口名称

Receive

端口收到的TC或TCN报文数

Send

端口发出的TC或TCN报文数

**生成树 \-- 生成树配置命令 \-- instance**

------------------------------------------------------------------------

**[instance**]命令用来将指定VLAN映射到指定的MSTI上。

**[undo instance**]命令用来删除指定VLAN与指定MSTI之间的映射关系，这些VLAN将重新映射到CIST（即MSTI 0）上。

【命令】

**[instance** *instance-id* **vlan** *vlan-id-list*]

**[undo instance** *instance-id* [ **vlan** *vlan-id-list* ]]

【缺省情况】

所有VLAN都映射到CIST（即MSTI 0）上。

【视图】

MST域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：表示MSTI的编号，取值范围为0～4094，0表示CIST。在执行**undo instance**命令时，*instance-id*的取值范围为1～4094。

**[vlan*** vlan-id-list*]：指定VLAN。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·如果**undo instance**命令中没有指定VLAN，则与指定MSTI有映射关系的所有VLAN都将重新映射到CIST上。

·不能将同一个VLAN映射到不同的MSTI上。如果将一个已映射到某MSTI的VLAN重新映射到另一个MSTI时，原先的映射关系将被取消。

·最多只能对65个MSTI配置VLAN映射关系。

·配置本命令后，必须执行**active region-configuration**命令才能激活本配置。

·配置全局摘要侦听功能后，如果要修改VLAN与MSTI间的映射关系，或执行**undo stp region-configuration**命令取消当前域配置，均可能因与邻接设备的VLAN和MSTI映射关系不一致而导致环路或流量中断，因此请谨慎操作。

【举例】

\# 将VLAN 2映射到MSTI 1上。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region instance 1 vlan 2

【相关命令】

·**active region-configuration**

·**check region-configuration**

·**display stp region-configuration**

**生成树 \-- 生成树配置命令 \-- region-name**

------------------------------------------------------------------------

**[region-name**]命令用来配置MST域的域名。

**[undo region-name**]命令用来恢复缺省情况。

【命令】

**[region-name** *name*]

**[undo region-name**]

【缺省情况】

MST域的域名为设备的MAC地址。

【视图】

MST域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[name*]：表示MST域的域名，为1～32个字符的字符串。

【使用指导】

·MST域名用来与MST域的VLAN映射表和MSTP的修订级别来共同确定设备所属的MST域。

·配置本命令后，必须执行**active region-configuration**命令才能激活本配置。

【举例】

\# 配置MST域的域名为hello。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region region-name hello

【相关命令】

·**active region-configuration**

·**check region-configuration**

·**display stp region-configuration**

·**instance**

·**revision-level**

·**vlan-mapping modulo**

**生成树 \-- 生成树配置命令 \-- reset stp**

------------------------------------------------------------------------

**[reset stp**]命令用来清除生成树的统计信息，包括端口收发的TCN BPDU、CONFIG BPDU、RST BPDU和MST BPDU的数量。

【命令】

**[reset stp** [ **interface** *interface-list* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-list*]：清除指定端口上的生成树统计信息。*interface-list*为端口列表，表示多个端口，表示方式为*interface-list* = { *interface-type interface-number* [ **to** *interface-type interface-number*  }&\<1-10\>]。其中，*interface-type*为端口类型，*interface-number*为端口编号。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，将清除所有端口上的生成树统计信息。

【举例】

\# 清除端口GigabitEthernet1/0/1到GigabitEthernet1/0/3上的生成树统计信息。

\<Sysname\> reset stp interface gigabitethernet 1/0/1 to gigabitethernet 1/0/3

【相关命令】

·**display stp**

**生成树 \-- 生成树配置命令 \-- revision-level**

------------------------------------------------------------------------

**[revision-level**]命令用来配置MSTP的修订级别。

**[undo revision-level**]命令用来恢复缺省情况。

【命令】

**[revision-level** *level*]

**[undo revision-level**]

【缺省情况】

MSTP的修订级别为0。

【视图】

MST域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[level*]：表示MSTP的修订级别，取值范围为0～65535。

【使用指导】

·MSTP的修订级别用来与MST域名和MST域的VLAN映射表来共同确定设备所属的MST域。修订级别可以在域名和VLAN映射表相同的情况下，来区分不同的域。

·配置本命令后，必须执行**active region-configuration**命令才能激活本配置。

【举例】

\# 配置设备的MSTP修订级别为5。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region revision-level 5

【相关命令】

·**active region-configuration**

·**check region-configuration**

·**display stp region-configuration**

·**instance**

·**region-name**

·**vlan-mapping modulo**

**生成树 \-- 生成树配置命令 \-- snmp-agent trap enable stp**

------------------------------------------------------------------------

**[snmp-agent trap enable stp**]命令用来开启生成树的告警功能。

**[undo snmp-agent trap enable stp**]命令用来关闭生成树的告警功能。

【命令】

**[snmp-agent trap enable stp**[ [ **new-root** \| **tc** ]]]

**[undo snmp-agent trap enable stp**[ [ **new-root** \| **tc** ]]]

【缺省情况】

生成树的new-root告警功能处于关闭状态。在MSTP模式下，生成树的TC告警功能在MSTI 0中处于开启状态，在其他MSTI中处于关闭状态；在PVST模式下，生成树的TC告警功能在所有VLAN中处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[new-root**]：在非PVST模式下，当设备在任意实例中由非根桥被选举为根桥后，打印Trap信息。

**[tc**]：在PVST模式下，当端口检测或接收到TC报文后，打印日志信息并打印Trap信息。该参数只能控制PVST模式下的TC告警功能。

【使用指导】

执行该命令时，如果未指定任何参数，表示开启或关闭生成树的new-root和TC告警功能。

【举例】

\# 配置当设备在任意实例中由非根桥被选举为根桥后，打印Trap信息。

\<Sysname\> system-view

Sysname snmp-agent trap enable stp new-root

**生成树 \-- 生成树配置命令 \-- stp bpdu-protection**

------------------------------------------------------------------------

**[stp bpdu-protection**]命令用来开启BPDU保护功能。

**[undo stp bpdu-protection**]命令用来关闭BPDU保护功能。

【命令】

**[stp bpdu-protection**]

**[undo stp** **bpdu-protection**]

【缺省情况】

BPDU保护功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启BPDU保护功能。

\<Sysname\> system-view

Sysname stp bpdu-protection

**生成树 \-- 生成树配置命令 \-- stp bridge-diameter**

------------------------------------------------------------------------

**[stp bridge-diameter**]命令用来配置交换网络的网络直径，即交换网络中任意两台终端设备间的最大设备数。

**[undo stp bridge-diameter**]命令用来恢复缺省情况。

【命令】

**[stp** **vlan** *vlan-id-list* ] **bridge-diameter** *diameter*

**[undo stp** [ **vlan** *vlan-id-list*  **bridge-diameter**]]

【缺省情况】

交换网络的网络直径为7。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan*** vlan-id-list*]：表示配置PVST交换网络中指定VLAN的网络直径。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，表示配置STP/RSTP/MSTP交换网络的网络直径。

*[diameter*]：表示交换网络的网络直径，取值范围为2～7。

【使用指导】

·选用合适的Hello Time、Forward Delay和Max Age时间参数，可以加快生成树收敛速度。上述三个时间参数的取值与网络规模有关，因此可以通过调整网络直径使生成树协议自动调整这三个时间参数的值。当网络直径为缺省值7时，这三个时间参数也分别取其各自的缺省值。

·在STP/RSTP/MSTP模式下，每个MST域将被视为一台设备，且网络直径配置只对CIST有效（即只能在总根上生效），而对MSTI无效。

·在PVST模式下，网络直径的配置只能在指定VLAN的根桥上生效。

【举例】

\# 在MSTP模式下，配置交换网络的网络直径为5。

\<Sysname\> system-view

Sysname stp bridge-diameter 5

\# 在PVST模式下，配置交换网络中VLAN 2的网络直径为5。

\<Sysname\> system-view

Sysname stp vlan 2 bridge-diameter 5

【相关命令】

·**stp timer forward-delay**

·**stp timer hello**

·**stp timer max-age**

**生成树 \-- 生成树配置命令 \-- stp compliance**

------------------------------------------------------------------------

**[stp compliance**]命令用来配置端口收发的MSTP报文格式。

**[undo stp compliance**]命令用来恢复缺省情况。

【命令】

**[stp compliance**[ { **auto** \| **dot1s** \| **legacy** }]]

**[undo stp compliance**]

【缺省情况】

端口会自动识别收到的MSTP报文格式并根据识别结果确定发送的报文格式。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示端口会自动识别收到的MSTP报文格式并根据识别结果确定发送的报文格式。

**[dot1s**]：表示端口只发送标准格式（符合802.1s协议）的MSTP报文。

**[legacy**]：表示端口只发送与非标准格式兼容的MSTP报文。

【使用指导】

二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置端口只发送标准格式的MSTP报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp compliance dot1s

**生成树 \-- 生成树配置命令 \-- stp config-digest-snooping**

------------------------------------------------------------------------

**[stp config-digest-snooping**]命令用来在端口上开启摘要侦听功能。

**[undo stp config-digest-snooping**]命令用来在端口上关闭摘要侦听功能。

【命令】

**[stp config-digest-snooping**]

**[undo stp config-digest-snooping**]

【缺省情况】

端口上的摘要侦听功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·只有当全局和端口上都开启了摘要侦听功能后，该功能才能生效。开启摘要侦听功能时，建议先在所有与第三方厂商设备相连的端口上开启该功能，再全局开启该功能，以一次性让所有端口的配置生效，从而减少对网络的冲击。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 先在端口GigabitEthernet1/0/1上开启摘要侦听功能，再全局开启摘要侦听功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp config-digest-snooping

Sysname-GigabitEthernet1/0/1 quit

Sysname stp global config-digest-snooping

【相关命令】

·**display stp**

·**stp global config-digest-snooping**

**生成树 \-- 生成树配置命令 \-- stp cost**

------------------------------------------------------------------------

**[stp cost**]命令用来配置端口的路径开销。

**[undo stp cost**]命令用来恢复缺省情况。

【命令】

**[stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **cost** *cost*]]

**[undo stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **cost**]]

【缺省情况】

自动按照相应的标准计算各生成树上的路径开销。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance*** instance-list*]：表示配置端口在MSTP指定MSTI的路径开销。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，表示配置端口在MSTP CIST或STP/RSTP的路径开销。

**[vlan*** vlan-id-list*]：表示配置端口在PVST指定VLAN的路径开销。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

*[cost*]：表示端口的路径开销值。取值范围由计算端口缺省路径开销所采用的计算方法来决定：

·当采用IEEE 802.1D-1998标准来计算时，取值范围为1～65535。

·当采用IEEE 802.1t标准来计算时，取值范围为1～200000000。

·当采用私有标准来计算时，取值范围为1～200000。

【使用指导】

·端口的路径开销是生成树计算的重要依据，可以影响端口的角色选择。在不同生成树上为同一端口配置不同的路径开销值，可以使不同VLAN的流量沿不同的物理链路转发，从而实现按VLAN的负载分担的功能。

·当端口的路径开销值改变时，系统将重新计算端口的角色并进行状态迁移。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

·如果未指定MSTI和VLAN，则表示配置端口在MSTP CIST或STP/RSTP的路径开销。

【举例】

\# 在MSTP模式下，配置端口GigabitEthernet1/0/3在MSTI 2上的路径开销值为200。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 stp instance 2 cost 200

\# 在PVST模式下，配置端口GigabitEthernet1/0/3在VLAN 2上的路径开销值为200。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 stp vlan 2 cost 200

【相关命令】

·**display stp**

·**stp pathcost-standard**

**生成树 \-- 生成树配置命令 \-- stp edged-port**

------------------------------------------------------------------------

**[stp edged-port**]命令用来配置当前端口为边缘端口。

**[undo stp edged-port**]命令用来恢复缺省情况。

【命令】

**[stp edged-port**]

**[undo stp******edged-port**]

【缺省情况】

端口为非边缘端口。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当端口直接与用户终端相连，而没有连接到其它设备或共享网段上，则该端口被认为是边缘端口。网络拓扑变化时，边缘端口不会产生临时环路。因此，如果将某个端口配置为边缘端口，则该端口可以快速迁移到转发状态。对于直接与用户终端相连的端口，为能使其快速迁移到转发状态，请将其设置为边缘端口。

·由于边缘端口不与其它设备相连，所以不会收到其它设备发过来的BPDU。在设备没有开启BPDU保护功能时，如果端口收到BPDU，即使用户设置该端口为边缘端口，该端口的实际运行状态也是非边缘端口。

·在同一个端口上，不允许同时配置边缘端口和环路保护功能。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置端口GigabitEthernet1/0/1为边缘端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp edged-port

【相关命令】

·**stp bpdu-protection**

·**stp loop-protection**

·**stp root-protection**

**生成树 \-- 生成树配置命令 \-- stp enable**

------------------------------------------------------------------------

**[stp** **enable**]命令用来在端口上开启生成树协议。

**[undo stp** **enable**]命令用来在端口上关闭生成树协议。

【命令】

**[stp** **enable**]

**[undo stp enable**]

【缺省情况】

端口上的生成树协议处于开启状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当生成树协议开启后，设备会根据用户配置的生成树工作模式来决定运行在STP模式、RSTP模式、PVST模式还是MSTP模式下。

·当生成树协议开启后，系统根据收到的BPDU动态维护相应VLAN的生成树状态；当生成树协议关闭后，系统将不再维护该状态。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上关闭生成树协议。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo stp enable

【相关命令】

·**stp global enable**

·**stp mode**

·**stp vlan enable**

**生成树 \-- 生成树配置命令 \-- stp global config-digest-snooping**

------------------------------------------------------------------------

**[stp global config-digest-snooping**]命令用来全局开启摘要侦听功能。

**[undo stp global config-digest-snooping**]命令用来全局关闭摘要侦听功能。

【命令】

**[stp global config-digest-snooping**]

**[undo stp global config-digest-snooping**]

【缺省情况】

摘要侦听功能处于全局关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有当全局和端口上都开启了摘要侦听功能后，该功能才能生效。开启摘要侦听功能时，建议先在所有与第三方厂商设备相连的端口上开启该功能，再全局开启该功能，以一次性让所有端口的配置生效，从而减少对网络的冲击。

【举例】

\# 先在端口GigabitEthernet1/0/1上开启摘要侦听功能，再全局开启摘要侦听功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp config-digest-snooping

Sysname-GigabitEthernet1/0/1 quit

Sysname stp global config-digest-snooping

【相关命令】

·**display stp**

·**stp config-digest-snooping**

**生成树 \-- 生成树配置命令 \-- stp global enable**

------------------------------------------------------------------------

**[stp** **global enable**]命令用来全局开启生成树协议。

**[undo stp** **global enable**]命令用来全局关闭生成树协议。

【命令】

**[stp** **global** **enable**]

**[undo stp global enable**]

【缺省情况】

生成树协议的全局状态与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当生成树协议开启后，设备会根据用户配置的生成树工作模式来决定运行在STP模式、RSTP模式、PVST模式还是MSTP模式下。

·当生成树协议开启后，系统根据收到的BPDU动态维护相应VLAN的生成树状态；当生成树协议关闭后，系统将不再维护该状态。

【举例】

\# 全局开启生成树协议。

\<Sysname\> system-view

Sysname stp global enable

【相关命令】

·**stp enable**

·**stp mode**

**生成树 \-- 生成树配置命令 \-- stp global mcheck**

------------------------------------------------------------------------

**[stp global mcheck**]命令用来全局执行mCheck操作。

【命令】

**[stp global mcheck**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在运行MSTP、RSTP或PVST的设备上，若某端口连接着运行STP协议的设备，该端口收到STP报文后会自动迁移到STP模式；但当对端运行STP协议的设备关机或撤走，而该端口又无法感知的情况下，该端口将无法自动迁移回原有模式，此时需要通过执行mCheck操作将其手工迁移回原有模式。

·设备会根据用户配置的生成树工作模式来决定运行在STP模式、RSTP模式、PVST模式还是MSTP模式下。

·只有当生成树的工作模式为MSTP模式、RSTP模式或PVST模式时执行本命令才有效。

【举例】

\# 全局执行mCheck操作。

\<Sysname\> system-view

Sysname stp global mcheck

【相关命令】

·**stp mcheck**

·**stp mode**

**生成树 \-- 生成树配置命令 \-- stp ignored vlan**

------------------------------------------------------------------------

![说明](生成树命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·可同时开启VLAN Ignore功能的VLAN最大数量与设备的型号有关，请以设备的实际情况为准。

**[stp ignored vlan**]命令用来在指定VLAN内开启VLAN Ignore功能。

**[undo stp ignored vlan**]命令用来在指定VLAN内关闭VLAN Ignore功能。

【命令】

**[stp ignored vlan ***vlan-id-list*]

**[undo stp ignored vlan** *vlan-id-list*]

【缺省情况】

VLAN内的VLAN Ignore功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

【举例】

\# 在VLAN 1～10内开启VLAN Ignore功能。

\<Sysname\> system-view

Sysname stp ignored vlan 1 to 10

【相关命令】

·**display stp ignored-vlan**

**生成树 \-- 生成树配置命令 \-- stp ignore-pvid-inconsistency**

------------------------------------------------------------------------

**[stp ignore-pvid-inconsistency**]命令用来关闭PVST的PVID不一致保护功能。

**[undo stp ignore-pvid-inconsistency**]命令用来恢复缺省情况。

【命令】

**[stp ignore-pvid-inconsistency**]

**[undo stp ignore-pvid-inconsistency**]

【缺省情况】

PVST的PVID不一致保护功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭PVST的PVID不一致保护功能后，如果链路两端端口PVID不一致，为了避免生成树的计算错误，需要注意：

·除了VLAN 1，本端所在设备不能创建对端PVID对应的VLAN，同样，对端也不能创建本端PVID对应的VLAN。

·本端端口的链路类型是Hybrid时，建议本端所在设备不创建以Untagged方式允许通过的VLAN，同样，对端也不创建本端Untagged方式允许通过的VLAN。

·建议链路对端设备也关闭PVST的PVID不一致保护功能。

·本配置在PVST工作模式下才能生效。

【举例】

\# 在PVST模式下，关闭PVST的PVID不一致保护功能。

\<Sysname\> system-view

Sysname stp mode pvst

Sysname stp ignore-pvid-inconsistency

**生成树 \-- 生成树配置命令 \-- stp loop-protection**

------------------------------------------------------------------------

**[stp loop-protection**]命令用来开启端口的环路保护功能。

**[undo stp loop-protection**]命令用来关闭端口的环路保护功能。

【命令】

**[stp loop-protection**]

**[undo stp** **loop-protection**]

【缺省情况】

端口的环路保护功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在同一个端口上，不允许同时配置边缘端口和环路保护功能，或者同时配置根保护功能和环路保护功能。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上开启环路保护功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp loop-protection

【相关命令】

·**stp edged-port**

·**stp root-protection**

**生成树 \-- 生成树配置命令 \-- stp max-hops**

------------------------------------------------------------------------

**[stp max-hops**]命令用来配置MST域的最大跳数，该跳数用来限制MST域的规模。

**[undo stp max-hops**]命令用来恢复缺省情况。

【命令】

**[stp max-hops** *hops*]

**[undo stp** **max-hops**]

【缺省情况】

MST域的最大跳数为20跳。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hops*]：表示最大跳数，取值范围为1～40。

【举例】

\# 配置MST域的最大跳数为35跳。

\<Sysname\> system-view

Sysname stp max-hops 35

【相关命令】

·**display stp**

**生成树 \-- 生成树配置命令 \-- stp mcheck**

------------------------------------------------------------------------

**[stp mcheck**]命令用来在端口上执行mCheck操作。

【命令】

**[stp mcheck**]

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在运行MSTP、RSTP或PVST的设备上，若某端口连接着运行STP协议的设备，该端口收到STP报文后会自动迁移到STP模式；但当对端运行STP协议的设备关机或撤走，而该端口又无法感知的情况下，该端口将无法自动迁移回原有模式，此时需要通过执行mCheck操作将其手工迁移回原有模式。

·当运行STP的设备A、未开启生成树协议的设备B和运行RSTP/MSTP/PVST的设备C三者顺次相连时，设备B将透传STP报文，设备C上连接设备B的端口将迁移到STP模式。在设备B上开启生成树协议后，若想使设备B与设备C之间运行RSTP/MSTP/PVST协议，除了要在设备B上配置生成树的工作模式为RSTP/MSTP/PVST外，还要在设备B与设备C相连的端口上都执行mCheck操作。

·设备会根据用户配置的生成树工作模式来决定运行在STP模式、RSTP模式、PVST模式还是MSTP模式下。

·只有当生成树的工作模式为MSTP模式、RSTP模式或PVST模式时执行本命令才有效。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上执行mCheck操作。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp mcheck

【相关命令】

·**stp global mcheck**

·**stp mode**

**生成树 \-- 生成树配置命令 \-- stp mode**

------------------------------------------------------------------------

**[stp mode**]命令用来配置生成树的工作模式。

**[undo stp mode**]命令用来恢复缺省情况。

【命令】

**[stp mode**[ { **mstp** \| **pvst** \| **rstp** \| **stp** }]]

**[undo stp mode**]

【缺省情况】

生成树工作模式为MSTP模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mstp**]：配置生成树的工作模式为MSTP模式。

**[pvst**]：配置生成树的工作模式为PVST模式。

**[rstp**]：配置生成树的工作模式为RSTP模式。

**[stp**]：配置生成树的工作模式为STP模式。

【使用指导】

MSTP模式兼容RSTP模式，RSTP模式兼容STP模式。

PVST模式与其他模式的兼容性如下：

·对于Access端口：PVST模式在任意VLAN中都能与其他模式互相兼容。

·对于Trunk端口或Hybrid端口：PVST模式仅在VLAN 1中能与其他模式互相兼容。

【举例】

\# 配置生成树的工作模式为STP模式。

\<Sysname\> system-view

Sysname stp mode stp

【相关命令】

·**stp enable**

·**stp global enable**

·**stp global mcheck**

·**stp mcheck**

·**stp vlan enable**

**生成树 \-- 生成树配置命令 \-- stp no-agreement-check**

------------------------------------------------------------------------

**[stp no-agreement-check**]命令用来在端口上开启No Agreement Check功能。

**[undo stp no-agreement-check**]命令用来在端口上关闭No Agreement Check功能。

【命令】

**[stp no-agreement-check**]

**[undo stp no-agreement-check**]

【缺省情况】

No Agreement Check功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当且仅当在根端口上开启本功能才生效。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上开启No Agreement Check功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp no-agreement-check

**生成树 \-- 生成树配置命令 \-- stp pathcost-standard**

------------------------------------------------------------------------

**[stp pathcost-standard**]命令用来配置缺省路径开销的计算标准。

**[undo stp pathcost-standard**]命令用来恢复缺省情况。

【命令】

**[stp**[ **pathcost-standard** { **dot1d-1998** \| **dot1t** \| **legacy** }]]

**[undo** **stp pathcost-standard**]

【缺省情况】

缺省路径开销的计算标准与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dot1d-1998**]：表示按照IEEE 802.1D-1998标准来计算缺省路径开销。

**[dot1t**]：表示按照IEEE 802.1t标准来计算缺省路径开销。

**[legacy**]：表示按照私有标准来计算缺省路径开销。

【使用指导】

改变缺省路径开销的计算标准，将使端口的路径开销值恢复为缺省值。

【举例】

\# 配置按照IEEE 802.1D-1998标准来计算缺省路径开销。

\<Sysname\> system-view

Sysname stp pathcost-standard dot1d-1998

【相关命令】

·**display stp**

·**stp cost**

**生成树 \-- 生成树配置命令 \-- stp point-to-point**

------------------------------------------------------------------------

**[stp point-to-point**]命令用来配置端口的链路类型。

**[undo stp point-to-point**]命令用来恢复缺省情况。

【命令】

**[stp point-to-point****[{ **auto** \| **force-false** \| **force-true** }]]

**[undo stp******point-to-point**]

【缺省情况】

端口的链路类型为**auto**，即由系统自动检测与本端口相连的链路是否为点对点链路。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示自动检测与本端口相连的链路是否为点对点链路。

**[force-false**]：表示与本端口相连的链路不是点对点链路。

**[force-true**]：表示与本端口相连的链路是点对点链路。

【使用指导】

·当端口与非点对点链路相连时，端口的状态无法快速迁移。

·如果某端口是二层聚合接口或其工作在全双工模式下，则可以将该端口配置为与点对点链路相连。通常建议使用缺省配置，由系统进行自动检测。

·在MSTP模式下，如果某端口被配置为与点对点链路（或非点对点链路）相连，那么该配置对该端口所属的所有MSTI都有效。

·如果某端口被配置为与点对点链路相连，但与该端口实际相连的物理链路不是点对点链路，则有可能引入临时回路。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置与端口GigabitEthernet1/0/3相连的链路是点对点链路。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 stp point-to-point force-true

【相关命令】

·**display stp**

**生成树 \-- 生成树配置命令 \-- stp port priority**

------------------------------------------------------------------------

**[stp port priority**]命令用来配置端口的优先级。端口优先级可以影响端口在生成树上的角色选择。

**[undo stp port priority**]命令用来恢复缺省情况。

【命令】

**[stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **port priority** *priority*]]

**[undo stp****[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **port priority**]]

【缺省情况】

端口的优先级为128。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance*** instance-list*]：表示配置端口在MSTP指定MSTI的优先级。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，表示配置端口在MSTP CIST或STP/RSTP的优先级。

**[vlan*** vlan-id-list*]：表示配置端口在PVST指定VLAN的优先级。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

*[priority*]：表示端口的优先级，取值范围为0～240，以16为步长，如0、16、32等。

【使用指导】

·通常，端口优先级的数值越小，端口的优先级就越高。如果设备的所有端口都采用相同的优先级数值，则端口优先级的高低就取决于该端口索引号的大小，即索引号越小优先级越高。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

·如果未指定MSTI和VLAN，则表示配置端口在MSTP CIST或STP/RSTP的优先级。

【举例】

\# 在MSTP模式下，配置端口GigabitEthernet1/0/3在MSTI 2上的优先级为16。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 stp instance 2 port priority 16

\# 在PVST模式下，配置端口GigabitEthernet1/0/3在VLAN 2上的优先级为16。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 stp vlan 2 port priority 16

【相关命令】

·**display stp**

**生成树 \-- 生成树配置命令 \-- stp port-log**

------------------------------------------------------------------------

**[stp** **port-log**]命令用来打开端口状态变化信息显示开关。

**[undo stp** **port-log**]命令用来关闭端口状态变化信息显示开关。

【命令】

**[stp**[ **port-log** { **all** \| **instance** *instance-list* \| **vlan** *vlan-id-list* }]]

**[undo**[ **stp** **port-log** { **all** \| **instance** *instance-list* \| **vlan** *vlan-id-list* }]]

【缺省情况】

端口状态变化信息显示开关处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示打开或关闭MSTP/PVST所有MSTI/VLAN中的端口状态变化信息显示开关。

**[instance*** instance-list*]：表示打开或关闭MSTP指定MSTI中的端口状态变化信息显示开关；如果指定了MSTI 0，则表示打开或关闭STP/RSTP的端口状态变化信息显示开关。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。

**[vlan*** vlan-id-list*]：表示打开或关闭PVST指定VLAN中的端口状态变化信息显示开关。*vlan-id-list*为VLAN列表，表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

【举例】

\# 在MSTP模式下，打开MSTI 2中的端口状态变化信息显示开关。

\<Sysname\> system-view

Sysname stp port-log instance 2

%Aug 16 00:49:41:856 2011 Sysname STP/3/STP_DISCARDING: Instance 2\'s port GigabitEthernet1/0/1 has been set to discarding state.

%Aug 16 00:49:41:856 2011 Sysname STP/3/STP_FORWARDING: Instance 2\'s port GigabitEthernet1/0/2 has been set to forwarding state.

*// 上述信息表明：在MSTI 2中，GigabitEthernet1/0/1的端口状态变为Discarding，GigabitEthernet1/0/2的端口状态变为Forwarding。*

\# 在PVST模式下，打开VLAN 1～4094中的端口状态变化信息显示开关。

\<Sysname\> system-view

Sysname stp port-log vlan 1 to 4094

%Aug 16 00:49:41:856 2006 Sysname STP/3/STP_DISCARDING: VLAN 2\'s GigabitEthernet1/0/1 has been set to discarding state.

%Aug 16 00:49:41:856 2006 Sysname STP/3/STP_FORWARDING: VLAN 2\'s GigabitEthernet1/0/2 has been set to forwarding state.

*// 上述信息表明：在VLAN 2中，GigabitEthernet1/0/1的端口状态变为Discarding，GigabitEthernet1/0/2的端口状态变为Forwarding。*

**生成树 \-- 生成树配置命令 \-- stp priority**

------------------------------------------------------------------------

**[stp priority**]命令用来配置设备的优先级。

**[undo stp priority**]命令用来恢复缺省情况。

【命令】

**[stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **priority** *priority*]]

**[undo stp**[ [ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **priority**]]

【缺省情况】

设备的优先级为32768。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance*** instance-list*]：表示配置设备在MSTP指定MSTI的优先级。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，表示配置设备在MSTP CIST或STP/RSTP的优先级。

**[vlan*** vlan-id-list*]：表示配置设备在PVST指定VLAN的优先级。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

*[priority*]：表示设备的优先级，该数值越小表示优先级越高。取值范围为0～61440，步长为4096，即设备可以设置16个优先级取值，如0、4096、8192等。

【使用指导】

如果未指定MSTI和VLAN，则表示配置设备在MSTP CIST或STP/RSTP中的优先级。

【举例】

\# 在MSTP模式下，配置设备在MSTI 1中的优先级为4096。

\<Sysname\> system-view

Sysname stp instance 1 priority 4096

\# 在PVST模式下，配置设备在VLAN 1中的优先级为4096。

\<Sysname\> system-view

Sysname stp vlan 1 priority 4096

**生成树 \-- 生成树配置命令 \-- stp pvst-bpdu-protection**

------------------------------------------------------------------------

**[stp pvst-bpdu-protection**]命令用来开启MSTP的PVST报文保护功能。

**[undo stp pvst-bpdu-protection**]命令用来恢复缺省情况。

【命令】

**[stp pvst-bpdu-protection**]

**[undo stp pvst-bpdu-protection**]

【缺省情况】

MSTP的PVST报文保护功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在MSTP模式下，设备上开启了PVST报文保护功能后，如果某些端口收到了PVST报文，系统就将这些端口关闭。被关闭的端口在经过一定时间间隔之后将被自动重新打开，关闭的时间间隔通过**shutdown-interval**命令配置。

【举例】

\# 在MSTP模式下，开启MSTP的PVST报文保护功能。

\<Sysname\> system-view

Sysname stp pvst-bpdu-protection

【相关命令】

·**shutdown-interval**（基础配置指导/设备管理）

**生成树 \-- 生成树配置命令 \-- stp region-configuration**

------------------------------------------------------------------------

**[stp region-configuration**]命令用来进入MST域视图。

**[undo stp region-configuration**]命令用来将MST域的配置恢复为缺省值。

【命令】

**[stp region-configuration**]

**[undo stp region-configuration**]

【缺省情况】

MST域的三个参数均取缺省值，即：MST域名为设备的桥MAC地址、所有VLAN都映射到CIST上、MSTP修订级别为0。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

进入MST域视图后，用户可以对MST域的相关参数（域名、VLAN映射表和修订级别）进行配置。

【举例】

\# 进入MST域视图。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region

**生成树 \-- 生成树配置命令 \-- stp role-restriction**

------------------------------------------------------------------------

**[stp role-restriction**]命令用来开启端口角色限制功能。

**[undo stp role-restriction**]命令用来关闭端口角色限制功能。

【命令】

**[stp role-restriction**]

**[undo stp role-restriction**]

【缺省情况】

端口角色限制功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当开启了某端口的端口角色限制功能之后，该端口将不能被计算为根端口。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 开启端口GigabitEthernet1/0/1的端口角色限制功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp role-restriction

**生成树 \-- 生成树配置命令 \-- stp root primary**

------------------------------------------------------------------------

**[stp root primary**]命令用来配置当前设备为根桥。

**[undo stp root**]命令用来恢复缺省情况。

【命令】

**[stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **root primary**]]

**[undo stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **root**]]

【缺省情况】

设备不是根桥。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance*** instance-list*]：表示配置当前设备为MSTP指定MSTI的根桥。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。

**[vlan*** vlan-id-list*]：表示配置当前设备为PVST指定VLAN的根桥。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·当设备一旦被配置为根桥之后，便不能再修改该设备的优先级。

·如果未指定MSTI和VLAN，则表示配置当前设备为MSTP CIST或STP/RSTP的根桥。

【举例】

\# 在MSTP模式下，配置当前设备为MSTI 1的根桥。

\<Sysname\> system-view

Sysname stp instance 1 root primary

\# 在PVST模式下，配置当前设备为VLAN 1的根桥。

\<Sysname\> system-view

Sysname stp vlan 1 root primary

【相关命令】

·**stp priority**

·**stp root secondary**

**生成树 \-- 生成树配置命令 \-- stp root secondary**

------------------------------------------------------------------------

**[stp root secondary**]命令用来配置当前设备为备份根桥。

**[undo stp root**]命令用来恢复缺省情况。

【命令】

**[stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **root secondary**]]

**[undo stp **[[ **instance** *instance-list* \| **vlan** *vlan-id-list* ] **root**]]

【缺省情况】

设备不是备份根桥。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance*** instance-list*]：表示配置当前设备为MSTP指定MSTI的备份根桥。*instance-list*为MSTI列表，表示多个MSTI，表示方式为*instance-list* = { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。

**[vlan*** vlan-id-list*]：表示配置当前设备为PVST指定VLAN的备份根桥。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·当设备一旦被配置为备份根桥之后，便不能再修改该设备的优先级。

·如果未指定MSTI和VLAN，则表示配置当前设备为MSTP CIST或STP/RSTP的备份根桥。

【举例】

\# 在MSTP模式下，配置当前设备为MSTI 1的备份根桥。

\<Sysname\> system-view

Sysname stp instance 1 root secondary

\# 在PVST模式下，配置当前设备为VLAN 1的备份根桥。

\<Sysname\> system-view

Sysname stp vlan 1 root secondary

【相关命令】

·**stp priority**

·**stp root primary**

**生成树 \-- 生成树配置命令 \-- stp root-protection**

------------------------------------------------------------------------

**[stp root-protection**]命令用来开启端口的根保护功能。

**[undo stp root-protection**]命令用来关闭端口的根保护功能。

【命令】

**[stp root-protection**]

**[undo stp** **root-protection**]

【缺省情况】

端口上的根保护功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在同一个端口上，不允许同时配置根保护功能和环路保护功能。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上开启根保护功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp root-protection

【相关命令】

·**stp edged-port**

·**stp loop-protection**

**生成树 \-- 生成树配置命令 \-- stp tc-protection**

------------------------------------------------------------------------

**[stp tc-protection**]命令用来开启防TC-BPDU攻击保护功能。

**[undo** **stp tc-protection**]命令用来关闭防TC-BPDU攻击保护功能。

【命令】

**[stp tc-protection**]

**[undo stp** **tc-protection**]

【缺省情况】

防TC-BPDU攻击保护功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当开启了防TC-BPDU攻击保护功能后，如果设备在单位时间（固定为十秒）内收到TC-BPDU的次数大于**stp tc-protection threshold**命令所指定的最高次数（假设为N次），那么该设备在这段时间之内将只进行N次刷新转发地址表项的操作，而对于超出N次的那些TC-BPDU，设备会在这段时间过后再统一进行一次地址表项刷新的操作，这样就可以避免频繁地刷新转发地址表项。

【举例】

\# 关闭防TC-BPDU攻击保护功能。

\<Sysname\> system-view

Sysname undo stp tc-protection

【相关命令】

·**stp tc-protection threshold**

**生成树 \-- 生成树配置命令 \-- stp tc-protection threshold**

------------------------------------------------------------------------

**[stp tc-protection threshold**]命令用来配置在单位时间（固定为十秒）内，设备收到TC-BPDU后一定时间内，允许收到TC-BPDU后立即刷新转发地址表项的最高次数。

**[undo stp tc-protection threshold**]命令用来恢复缺省情况。

【命令】

**[stp tc-protection threshold ***number*]

**[undo stp tc-protection threshold**]

【缺省情况】

在单位时间（固定为十秒）内，设备收到TC-BPDU后立即刷新转发地址表项的最高次数为6。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：表示在单位时间（固定为十秒）内，设备收到TC-BPDU后立即刷新转发地址表项的最高次数，取值范围为1～255。

【举例】

\# 配置在单位时间（固定为十秒）内，设备收到TC-BPDU后一定时间内，允许收到TC-BPDU后立即刷新转发地址表项的最高次数为10。

\<Sysname\> system-view

Sysname stp tc-protection threshold 10

【相关命令】

·**stp tc-protection**

**生成树 \-- 生成树配置命令 \-- stp tc-restriction**

------------------------------------------------------------------------

**[stp tc-restriction**]命令用来开启TC-BPDU传播限制功能。

**[undo stp tc-restriction**]命令用来关闭TC-BPDU传播限制功能。

【命令】

**[stp tc-restriction**]

**[undo stp tc-restriction**]

【缺省情况】

TC-BPDU传播限制功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当开启了某端口的TC-BPDU传播限制功能之后，该端口将不再向其它端口传播TC-BPDU，也不删除本机的转发地址表项。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 开启端口GigabitEthernet1/0/1的TC-BPDU传播限制功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp tc-restriction

**生成树 \-- 生成树配置命令 \-- stp tc-snooping**

------------------------------------------------------------------------

**[stp tc-snooping**]命令用来开启TC Snooping功能。

**[undo stp** **tc-snooping**]命令用来关闭TC Snooping功能。

【命令】

**[stp tc-snooping**]

**[undo stp** **tc-snooping**]

【缺省情况】

TC Snooping功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

TC Snooping功能与生成树协议互斥，因此在开启TC Snooping功能之前必须全局关闭生成树协议。

【举例】

\# 全局关闭生成树协议，并开启TC Snooping功能。

\<Sysname\> system-view

Sysname undo stp global enable

Sysname stp tc-snooping

【相关命令】

·**stp ****global enable**

**生成树 \-- 生成树配置命令 \-- stp timer forward-delay**

------------------------------------------------------------------------

**[stp timer forward-delay**]命令用来配置Forward Delay时间参数。

**[undo stp timer forward-delay**]命令用来恢复缺省情况。

【命令】

**[stp** **vlan** *vlan-id-list* ] **timer forward-delay** *time*

**[undo stp** **vlan** *vlan-id-list* ] **timer forward-delay**

【缺省情况】

Forward Delay为15秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan*** vlan-id-list*]：表示配置PVST指定VLAN的Forward Delay时间参数。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，表示配置STP/RSTP/MSTP的Forward Delay时间参数。

*[time*]：表示Forward Delay的时间值，取值范围为400～3000，步长为100，单位为0.01秒。

【使用指导】

·Forward Delay用于确定状态迁移的延迟时间。为了防止产生临时环路，生成树协议在端口由Discarding状态向Forwarding状态迁移的过程中设置了Learning状态作为过渡，并规定状态迁移需要等待Forward Delay时间，以保持与远端的设备状态切换同步。

·通常情况下不建议使用本命令直接调整Forward Delay时间参数。由于该时间参数的取值与网络规模有关，因此建议通过使用**stp bridge-diameter**命令调整网络直径，使生成树协议自动调整该时间参数的值。当网络直径取缺省值时，该时间参数也取缺省值。

【举例】

\# 在MSTP模式下，配置Forward Delay为20秒。

\<Sysname\> system-view

Sysname stp timer forward-delay 2000

\# 在PVST模式下，配置VLAN 2的Forward Delay为20秒。

\<Sysname\> system-view

Sysname stp vlan 2 timer forward-delay 2000

【相关命令】

·**stp bridge-diameter**

·**stp timer hello**

·**stp timer max-age**

**生成树 \-- 生成树配置命令 \-- stp timer hello**

------------------------------------------------------------------------

**[stp ** **vlan** *vlan-id-list* ] **timer hello**命令用来配置Hello Time时间参数。

**[undo stp ** **vlan** *vlan-id-list* ] **timer hello**命令用来恢复缺省情况。

【命令】

**[stp****timer hello** *time*]

**[undo stp****timer hello**]

【缺省情况】

Hello Time为2秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan*** vlan-id-list*]：表示配置PVST指定VLAN的Hello Time时间参数。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，表示配置STP/RSTP/MSTP的Hello Time时间参数。

*[time*]：表示Hello Time的时间值，取值范围为100～1000，步长为100，单位为0.01秒。

【使用指导】

·Hello Time用于检测链路是否存在故障。生成树协议每隔Hello Time时间会发送BPDU，以确认链路是否存在故障。如果设备在Hello Time时间内没有收到BPDU，则会由于消息超时而重新计算生成树。

·通常情况下不建议使用本命令直接调整Hello Time时间参数。由于该时间参数的取值与网络规模有关，因此建议通过使用**stp bridge-diameter**命令调整网络直径，使生成树协议自动调整该时间参数的值。当网络直径取缺省值时，该时间参数也取缺省值。

【举例】

\# 在MSTP模式下，配置Hello Time为4秒。

\<Sysname\> system-view

Sysname stp timer hello 400

\# 在PVST模式下，配置VLAN 2的Hello Time为4秒。

\<Sysname\> system-view

Sysname stp vlan 2 timer hello 400

【相关命令】

·**stp bridge-diameter**

·**stp timer forward-delay**

·**stp timer max-age**

**生成树 \-- 生成树配置命令 \-- stp timer max-age**

------------------------------------------------------------------------

**[stp timer max-age**]命令用来配置Max Age时间参数。

**[undo stp timer max-age**]命令用来恢复缺省情况。

【命令】

**[stp** **vlan** *vlan-id-list* ] **timer max-age** *time*

**[undo stp** **vlan** *vlan-id-list* ] **timer max-age**

【缺省情况】

Max Age为20秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan*** vlan-id-list*]：表示配置PVST指定VLAN的Max Age时间参数。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，表示配置STP/RSTP/MSTP的Max Age时间参数。

*[time*]：表示Max Age的时间值，取值范围为600～4000，步长为100，单位为0.01秒。

【使用指导】

·Max Age用于确定BPDU是否超时。在MSTP的CIST上，设备根据Max Age时间来确定端口收到的BPDU是否超时。如果端口收到的BPDU超时，则需要对该MSTI重新计算。Max Age时间对MSTP的MSTI无效。

·通常情况下不建议使用本命令直接调整Max Age时间参数。由于该时间参数的取值与网络规模有关，因此建议通过使用**stp bridge-diameter**命令调整网络直径，使生成树协议自动调整该时间参数的值。当网络直径取缺省值时，该时间参数也取缺省值。

【举例】

\# 在MSTP模式下，配置Max Age为10秒。

\<Sysname\> system-view

Sysname stp timer max-age 1000

\# 在PVST模式下，配置VLAN 2的Max Age为10秒。

\<Sysname\> system-view

Sysname stp vlan 2 timer max-age 1000

【相关命令】

·**stp bridge-diameter**

·**stp timer forward-delay**

·**stp timer hello**

**生成树 \-- 生成树配置命令 \-- stp timer-factor**

------------------------------------------------------------------------

**[stp timer-factor**]命令用来配置超时时间因子，该因子用来确定设备的超时时间：超时时间 = 超时时间因子 × 3 × Hello Time。

**[undo stp timer-factor**]命令用来恢复缺省情况。

【命令】

**[stp timer-factor ***factor*]

**[undo** **stp timer-factor**]

【缺省情况】

超时时间因子为3。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[factor*]：表示超时时间因子，取值范围为1～20。

【使用指导】

·当网络拓扑结构稳定后，非根桥设备会每隔Hello Time时间向周围相连设备转发根桥发出的BPDU以确认链路是否存在故障。通常如果设备在9倍的Hello Time时间内没有收到上游设备发来的BPDU，就会认为上游设备已经故障，从而重新进行生成树的计算。

·有时设备在较长时间内收不到上游设备发来的BPDU，可能是由于上游设备的繁忙导致的，在这种情况下一般不应重新进行生成树的计算。因此在稳定的网络中，可以通过延长超时时间来减少网络资源的浪费。在一个稳定的网络中，建议将超时时间因子配置为5～7。

【举例】

\# 配置超时时间因子为7。

\<Sysname\> system-view

Sysname stp timer-factor 7

【相关命令】

·**stp timer hello**

**生成树 \-- 生成树配置命令 \-- stp transmit-limit**

------------------------------------------------------------------------

**[stp transmit-limit**]命令用来配置端口发送BPDU的速率。

**[undo stp transmit-limit**]命令用来恢复缺省情况。

【命令】

**[stp transmit-limit ***limit*]

**[undo stp******transmit-limit**]

【缺省情况】

端口发送BPDU的速率为10。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit*]：表示端口发送BPDU的速率，取值范围为1～255。

【使用指导】

·每Hello Time时间内端口能够发送的BPDU的最大数目＝端口发送BPDU的速率＋Hello Time时间值。

·端口发送BPDU的速率越高，每个Hello Time内可发送的BPDU数量就越多，占用的系统资源也越多。适当配置发送速率一方面可以限制端口发送BPDU的速度，另一方面还可以防止在网络拓扑动荡时，生成树协议占用过多的带宽资源。建议用户采用缺省配置。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置只对当前接口生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置端口GigabitEthernet1/0/1发送BPDU的速率为5。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 stp transmit-limit 5

**生成树 \-- 生成树配置命令 \-- stp vlan enable**

------------------------------------------------------------------------

**[stp** **vlan** **enable**]命令用来在VLAN中开启生成树协议。

**[undo stp** **enable**]命令用来在VLAN中关闭生成树协议。

【命令】

**[stp** **vlan** *vlan-id-list* **enable**]

**[undo stp vlan** *vlan-id-list* **enable**]

【缺省情况】

生成树协议在VLAN中的开启状态与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan*** vlan-id-list*]：开启或关闭指定VLAN上的生成树协议。*vlan-id-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。如果不指定该参数，将开启或关闭全局的（不包括VLAN上的）生成树协议。

【使用指导】

·当生成树协议开启后，设备会根据用户配置的生成树工作模式来决定运行在STP模式、RSTP模式、MSTP模式还是PVST模式下。

·当生成树协议开启后，系统根据收到的BPDU动态维护相应VLAN的生成树状态；当生成树协议关闭后，系统将不再维护该状态。

【举例】

\# 在PVST模式下，先全局开启生成树协议，再开启VLAN 2中的生成树协议。

\<Sysname\> system-view

Sysname stp mode pvst

Sysname stp global enable

Sysname stp vlan 2 enable

【相关命令】

·**stp enable**

·**stp global enable**

·**stp mode**

**生成树 \-- 生成树配置命令 \-- vlan-mapping modulo**

------------------------------------------------------------------------

**[vlan-mapping modulo**]命令用来快速配置VLAN映射表，使当前MST域内的所有VLAN按指定的模值映射到不同的MSTI上。

【命令】

**[vlan-mapping modulo** *modulo*]

【缺省情况】

所有VLAN都映射到CIST（即MSTI 0）上。

【视图】

MST域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[modulo*]：表示模值，取值范围为1到设备支持的最大值（最大值与设备的型号有关，请以设备的实际情况为准）。

【使用指导】

·不能将同一个VLAN映射到不同的MSTI上。如果将一个已映射到某MSTI的VLAN重新映射到另一个MSTI时，原先的映射关系将被取消。

·本命令将VLAN映射到编号为 (VLAN ID - 1) % *modulo* + 1的MSTI上。其中，(VLAN ID - 1) % *modulo*表示对 (VLAN ID - 1) 进行求模运算，如模值为15，则VLAN 1映射到MSTI 1、VLAN 2映射到MSTI 2、......、VLAN 15映射到MSTI 15、VLAN 16映射到MSTI 1，依次类推。

【举例】

\# 将所有VLAN按照模8映射到不同的MSTI上。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region vlan-mapping modulo 8

【相关命令】

·**active region-configuration**

·**check region-configuration**

·**display stp region-configuration**

·**region-name**

·**revision-level**
