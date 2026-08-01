<!-- CMD-INDEX
  display igmp-snooping               | 任意视图             | L55
  display igmp-snooping group         | 任意视图             | L285
  display igmp-snooping router-port   | 任意视图             | L485
  display igmp-snooping static-group  | 任意视图             | L637
  display igmp-snooping static-router-port | 任意视图             | L771
  display igmp-snooping statistics    | 任意视图             | L863
  display l2-multicast ip             | 任意视图             | L957
  display l2-multicast ip forwarding  | 任意视图             | L1137
  display l2-multicast mac            | 任意视图             | L1281
  display l2-multicast mac forwarding | 任意视图             | L1423
  dot1p-priority (IGMP-Snooping view) | IGMP-Snooping视图  | L1565
  drop-unknown (IGMP-Snooping view)   | IGMP-Snooping视图  | L1615
  enable (IGMP-Snooping view)         | IGMP-Snooping视图  | L1665
  entry-limit (IGMP-Snooping view)    | IGMP-Snooping视图  | L1719
  fast-leave (IGMP-Snooping view)     | IGMP-Snooping视图  | L1761
  group-policy (IGMP-Snooping view)   | IGMP-Snooping视图  | L1813
  host-aging-time (IGMP-Snooping view) | IGMP-Snooping视图  | L1879
  igmp-snooping                       | 系统视图             | L1929
  igmp-snooping dot1p-priority        | VLAN视图           | L1973
  igmp-snooping drop-unknown          | VLAN视图/VSI视图     | L2035
  igmp-snooping enable                | VLAN视图/VSI视图     | L2111
  igmp-snooping fast-leave            | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2177
  igmp-snooping general-query source-ip | VLAN视图/VSI视图     | L2229
  igmp-snooping group-limit           | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2303
  igmp-snooping group-policy          | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2351
  igmp-snooping host-aging-time       | VLAN视图/VSI视图     | L2417
  igmp-snooping host-join             | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2493
  igmp-snooping last-member-query-interval | VLAN视图/VSI视图     | L2559
  igmp-snooping leave source-ip       | VLAN视图           | L2635
  igmp-snooping max-response-time     | VLAN视图/VSI视图     | L2693
  igmp-snooping overflow-replace      | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2773
  igmp-snooping querier               | VLAN视图/VSI视图     | L2825
  igmp-snooping query-interval        | VLAN视图/VSI视图     | L2897
  igmp-snooping report source-ip      | VLAN视图           | L2977
  igmp-snooping router-aging-time     | VLAN视图/VSI视图     | L3035
  igmp-snooping router-port-deny      | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3111
  igmp-snooping source-deny           | 二层以太网接口视图        | L3153
  igmp-snooping special-query source-ip | VLAN视图/VSI视图     | L3203
  igmp-snooping static-group          | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3277
  igmp-snooping static-router-port    | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3337
  igmp-snooping version               | VLAN视图/VSI视图     | L3381
  last-member-query-interval (IGMP-Snooping view) | IGMP-Snooping视图  | L3457
  max-response-time (IGMP-Snooping view) | IGMP-Snooping视图  | L3507
  overflow-replace (IGMP-Snooping view) | IGMP-Snooping视图  | L3561
  report-aggregation (IGMP-Snooping view) | IGMP-Snooping视图  | L3613
  reset igmp-snooping group           | 用户视图             | L3651
  reset igmp-snooping router-port     | 用户视图             | L3693
  reset igmp-snooping statistics      | 用户视图             | L3731
  router-aging-time (IGMP-Snooping view) | IGMP-Snooping视图  | L3761
  source-deny (IGMP-Snooping view)    | IGMP-Snooping视图  | L3811
  version (IGMP-Snooping view)        | IGMP-Snooping视图  | L3865
-->

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping**

------------------------------------------------------------------------

**[display** **igmp-snooping**]命令用来显示IGMP Snooping的状态信息。

【命令】

**[display**[ **igmp-snooping** [ **global** \| **vlan** *vlan-id* \| **vsi** *vsi-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示IGMP Snooping的全局状态信息。

**[vlan** *vlan-id*]：显示IGMP Snooping在指定VLAN内的状态信息。*vlan-id*为VLAN的编号，取值范围为1～4094。

**[vsi** *vsi-name*]：显示IGMP Snooping在指定VSI内的状态信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

如果未指定任何可选参数，将显示IGMP Snooping在全局以及所有VLAN和VSI内的状态信息。

【举例】

\# 显示IGMP Snooping在全局以及所有VLAN和VSI内的状态信息。

\<Sysname\> display igmp-snooping

IGMP snooping information: Global

 IGMP snooping: Enabled

 Drop-unknown: Disabled

 Host-aging-time: 260s

 Router-aging-time: 260s

 Max-response-time: 10s

 Last-member-query-interval: 1s

 Report-aggregation: Enabled

 Dot1p-priority: \--

IGMP snooping information: VLAN 1

 IGMP snooping: Enabled

 Drop-unknown: Disabled

 Version: 2

 Host-aging-time: 260s

 Router-aging-time: 260s

 Max-response-time: 10s

 Last-member-query-interval: 1s

 Querier: Disabled

 Query-interval: 125s

 General-query source IP: 1.1.1.1

 Special-query source IP: 2.2.2.2

 Report source IP: 3.0.0.3

 Leave source IP: 1.0.0.1

 Dot1p-priority: 2

IGMP snooping information: VLAN 10

 IGMP snooping: Enabled

 Drop-unknown: Enabled

 Version: 3

 Host-aging-time: 260s

 Router-aging-time: 260s

 Max-response-time: 10s

 Last-member-query-interval: 1s

 Querier: Disabled

 Query-interval: 125s

 General-query source IP: 1.1.1.1

 Special-query source IP: 2.2.2.2

 Report source IP: 3.0.0.3

 Leave source IP: 1.0.0.1

 Dot1p-priority: \--

IGMP snooping information: VSI aaa

 IGMP snooping: Enabled

 Drop-unknown: Enabled

 Version: 2

 Host-aging-time: 260s

 Router-aging-time: 260s

 Max-response-time: 10s

 Last-member-query-interval: 1s

 Querier: Disabled

 Query-interval: 125s

 General-query source IP: 1.1.1.1

 Special-query source IP: 2.2.2.2

表1-1 display igmp-snooping命令显示信息描述表

字段

描述

IGMP snooping information

IGMP Snooping的状态信息

IGMP snooping

IGMP Snooping的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

Drop-unknown

丢弃未知组播数据报文功能的使能状态（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）：

·Enabled：表示已使能

·Disabled：表示未使能

Version

IGMP Snooping的版本

Host-aging-time

动态成员端口的老化时间

Router-aging-time

动态路由器端口老化时间

Max-response-time

IGMP普遍组查询的最大响应时间

Last-member-query-interval

IGMP特定组查询报文的发送间隔

Report-aggregation

IGMP成员关系报告报文抑制功能的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

Dot1p-priority

IGMP报文的802.1p优先级，"\--"表示没有配置

Querier

IGMP Snooping查询器的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

Query-interval

IGMP普遍组查询报文的发送间隔

General-query source IP

IGMP普遍组查询报文的源IP地址

Special-query source IP

IGMP特定组查询报文的源IP地址

Report source IP

IGMP成员关系报告报文的源IP地址

Leave source IP

IGMP离开组报文的源IP地址

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping group**

------------------------------------------------------------------------

**[display igmp-snooping group**]命令用来显示动态IGMP Snooping转发表的信息。

【命令】

集中式设备：

**[display igmp-snooping**[ **group** [ *group-address* \| *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **verbose**   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display igmp-snooping**]{.TableTextChar}**group**[[ *group-address* \| *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display igmp-snooping**]{.TableTextChar}**group**[[ *group-address* \| *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-address*]：显示指定组播组的信息，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，将显示所有组播组的信息。

*[source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示简要信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【举例】

\# 显示VLAN 2内动态IGMP Snooping转发表的详细信息。

\<Sysname\> display igmp-snooping group vlan 2 verbose

Total 1 entries.

VLAN 2: Total 1 entries.

  (0.0.0.0, 224.1.1.1)

    Attribute: local port

    FSM information: normal

    Host slots (0 in total):

    Host ports (1 in total):

      GE1/0/2                             (00:03:23)

\# 显示VSI aaa内动态IGMP Snooping转发表的详细信息。

\<Sysname\> display igmp-snooping group vsi aaa verbose

Total 1 entries.

VSI aaa: Total 1 entries.

  (0.0.0.0, 224.1.1.1)

    Attribute: global port

    FSM information: normal

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)         (00:03:35)

        VLAN pairs (1 in total):

          Out VLAN 5     In VLAN 2        (00:03:35)

表1-2 display igmp-snooping group命令显示信息描述表

字段

描述

Total 1 entries

表项总数

VLAN 2: Total 1 entries

VLAN 2内的表项总数

VSI aaa: Total 1 entries

VSI aaa内的表项总数

(0.0.0.0, 224.1.1.1)

（S，G）表项，0.0.0.0表示所有组播源

Attribute

表项属性，包括：

·global port：表示表项中存在全局口

·local port：表示表项中存在本单板的端口

·slot：表示表项中存在其它单板的端口

FSM information

表项状态机，包括：

·delete：表示所有成员属性均已删除

·dummy：表示新创建的临时表项

·no info：表示没有表项存在

·normal：表示主控板通知创建的正式表项

Host slots (0 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有成员端口的设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Host ports (1 in total)

成员端口及总数

(00:03:23)

成员端口的老化剩余时间。需要注意的是，本字段对于全局口（包括二层聚合接口、AC口、N-PW口、U-PW口等）将无条件显示，而对于非全局口：

·在集中式设备上，将无条件显示

·在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示

·在集中式IRF设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示

·在分布式设备－IRF模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示

AC (VSI index 0, link ID 1)

AC（Attachment Circuit，接入电路）口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW（Network Pseudowire，网络侧伪线）口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW（User facing Pseudowire，用户侧伪线）口的VSI索引和链路标识符

VLAN pairs (1 in total)

VLAN对及总数

Out VLAN 5, in VLAN 2

外层VLAN为5，内层VLAN为2

【相关命令】

·**reset igmp-snooping group**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping router-port**

------------------------------------------------------------------------

**[display igmp-snooping router-port**]命令用来显示动态路由器端口的信息。

【命令】

集中式设备：

**[display igmp-snooping**]{.TableTextChar}**router-port**[ [ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* [ **verbose** ] ]  **cpu** *cpu-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display igmp-snooping**]{.TableTextChar}**router-port**[ [ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* [ **verbose** ] ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display igmp-snooping**]{.TableTextChar}**router-port**[ [ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* [ **verbose** ] ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[verbose**]：显示详细信息。如果未指定本参数，将显示简要信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【举例】

\# 显示VLAN 2内动态路由器端口的信息。

\<Sysname\> display igmp-snooping router-port vlan 2

VLAN 2:

  Router slots (0 in total):

  Router ports (2 in total):

    GE1/0/1                             (00:01:30)

    GE1/0/2                             (00:00:23)

\# 显示VSI aaa内动态路由器端口的详细信息。

\<Sysname\> display igmp-snooping router-port vsi aaa verbose

VSI aaa:

  Router slots (0 in total):

  Router ports (1 in total):

    AC (VSI index 0, link ID 1)         (00:03:35)

      VLAN pairs (1 in total):

        Out VLAN 5     In VLAN 2        (00:03:35)

表1-3 display igmp-snooping router-port命令显示信息描述表

字段

描述

VLAN 2

VLAN的编号

VSI aaa

VSI的名称

Router slots (0 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有动态路由器端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有动态路由器端口的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有动态路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Router ports (2 in total)

动态路由器端口及总数

(00:01:30)

动态路由器端口的老化剩余时间。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：

·在集中式设备上，将无条件显示

·在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示

·在集中式IRF设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示

·在分布式设备－IRF模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示

AC (VSI index 0, link ID 1)

AC口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW口的VSI索引和链路标识符

VLAN pairs (1 in total)

VLAN及总数

Out VLAN 5, in VLAN 2

外层VLAN为5，内层VLAN为2

【相关命令】

·**reset igmp-snooping router-port**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping static-group**

------------------------------------------------------------------------

**[display igmp-snooping static**]-{.TableTextChar}**group**命令用来显示静态IGMP Snooping转发表的信息。

【命令】

集中式设备：

**[display igmp-snooping** **static**]-{.TableTextChar}**group**[[ *group-address* \| *source-address* ] \*  **vlan** *vlan-id*   **verbose**   **cpu** *cpu-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display igmp-snooping** **static**]-{.TableTextChar}**group**[[ *group-address* \| *source-address* ] \*  **vlan** *vlan-id*   **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display igmp-snooping** **static**]-{.TableTextChar}**group**[[ *group-address* \| *source-address* ] \*  **vlan** *vlan-id*   **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-address*]：显示指定组播组的信息，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，将显示所有组播组的信息。

*[source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示简要信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【举例】

\# 显示VLAN 2内静态IGMP Snooping转发表的详细信息。

\<Sysname\> display igmp-snooping static-group vlan 2 verbose

Total 1 entries.

VLAN 2: Total 1 entries.

  (0.0.0.0, 224.1.1.1)

    Attribute: local port

    FSM information: normal

    Host slots (0 in total):

    Host ports (1 in total):

      GE1/0/2

表1-4 display igmp-snooping static-{.TableTextChar}group命令显示信息描述表

字段

描述

Total 1 entries

表项总数

VLAN 2: Total 1 entries

VLAN 2内的表项总数

(0.0.0.0, 224.1.1.1)

（S，G）表项，0.0.0.0表示所有组播源

Attribute

表项属性，包括：

·global port：表示表项中存在全局口

·local port：表示表项中存在本单板的端口

·slot：表示表项中存在其它单板的端口

FSM information

表项状态机，包括：

·delete：表示所有成员属性均已删除

·dummy：表示新创建的临时表项

·no info：表示没有表项存在

·normal：表示主控板通知创建的正式表项

Host slots (0 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Host ports (1 in total)

成员端口及总数

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping static-router-port**

------------------------------------------------------------------------

**[display igmp-snooping static-router-port**]命令用来显示静态路由器端口的信息。

【命令】

集中式设备：

**[display igmp-snooping**]{.TableTextChar}**static-router-port** [ **vlan** *vlan-id*   **cpu** *cpu-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display igmp-snooping**]{.TableTextChar}**static-router-port** [ **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display igmp-snooping**]{.TableTextChar}**static-router-port** [ **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【举例】

\# 显示VLAN 2内静态路由器端口的信息。

\<Sysname\> display igmp-snooping static-router-port vlan 2

VLAN 2:

  Router slots (0 in total):

  Router ports (2 in total):

    GE1/0/1

    GE1/0/2

表1-5 display igmp-snooping static-router-port命令显示信息描述表

字段

描述

VLAN 2

VLAN的编号

Router slots (0 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有静态路由器端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有静态路由器端口的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有静态路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Router ports (2 in total)

静态路由器端口及总数

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display igmp-snooping statistics**

------------------------------------------------------------------------

**[display** **igmp**-**snooping** **statistics**]命令用来显示IGMP Snooping监听到的IGMP报文统计信息。

【命令】

**[display igmp-snooping statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IGMP Snooping监听到的IGMP报文统计信息。

\<Sysname\> display igmp-snooping statistics

Received IGMP general queries:  0

Received IGMPv1 reports:  0

Received IGMPv2 reports:  19

Received IGMP leaves:  0

Received IGMPv2 specific queries:  0

Sent     IGMPv2 specific queries:  0

Received IGMPv3 reports:  1

Received IGMPv3 reports with right and wrong records:  0

Received IGMPv3 specific queries:  0

Received IGMPv3 specific sg queries:  0

Sent     IGMPv3 specific queries:  0

Sent     IGMPv3 specific sg queries:  0

Received error IGMP messages:  19

表1-6 display igmp-snooping statistics命令显示信息描述表

字段

描述

general queries

IGMP普遍组查询报文的数量

specific queries

IGMP特定组查询报文的数量

reports

IGMP成员关系报告报文的数量

leaves

IGMP离开组报文的数量

reports with right and wrong records

包含错误和正确纪录的IGMP成员关系报告报文数量

specific sg queries

IGMP特定源组查询报文的数量

error IGMP messages

错误IGMP报文的数量

【相关命令】

·**reset igmp-snooping statistics**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display l2-multicast ip**

------------------------------------------------------------------------

**[display l2-multicast ip**]命令用来显示二层组播的IP组播组信息。

【命令】

集中式设备：

**[display l2-multicast ip**[ [ **group** *group-address* \| **source** *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display l2-multicast ip**[ [ **group** *group-address* \| **source** *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display l2-multicast ip**[ [ **group** *group-address* \| **source** *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[group** *group-address*]：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。

**[source*** source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【举例】

\# 显示VLAN 2内二层组播的IP组播组信息。

\<Sysname\> display l2-multicast ip vlan 2

Total 1 entries.

VLAN 2: Total 1 IP entries.

  (0.0.0.0, 224.1.1.1)

    Attribute: static, success

    Host slots (0 in total):

    Host ports (1 in total):

      GE1/0/1                             (S, SUC)

\# 显示VSI aaa内二层组播的IP组播组信息。

\<Sysname\> display l2-multicast ip vsi aaa

Total 1 entries.

VSI aaa: Total 1 IP entries.

  (0.0.0.0, 224.1.1.1)

    Attribute: dynamic, success

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)         (D, SUC)

表1-7 display l2-multicast ip命令显示信息描述表

字段

描述

Total 1 entries

表项总数

VLAN 2: Total 1 IP entries

VLAN 2内的表项总数

VSI aaa: Total 1 IP entries

VSI aaa内的表项总数

(0.0.0.0, 224.1.1.1)

（S，G）表项，0.0.0.0表示所有组播源

Attribute

表项属性，包括：

·dynamic：表示由动态协议创建的表项

·static：表示由静态协议创建的表项

·pim：表示由PIM协议创建的表项

·kernel：表示从内核中获取的表项

·success：表示处理成功

·fail：表示处理失败

Host slots (0 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Host ports (1 in total)

成员端口及总数

(S, SUC)

端口属性，包括：

·D：表示动态端口

·S：表示静态端口

·P：表示PIM端口

·K：表示从内核中获取的端口

·R：表示从（\*，\*）表项扩展的端口

·W：表示从（\*，G）表项扩展的端口

·SUC：表示处理成功

·F：表示处理失败

AC (VSI index 0, link ID 1)

AC口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW口的VSI索引和链路标识符

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display l2-multicast ip forwarding**

------------------------------------------------------------------------

**[display l2-multicast ip forwarding**]命令用来显示二层组播的IP转发表信息。

【命令】

集中式设备：

**[display l2-multicast ip forwarding**[ [ **group** *group-address* \| **source** *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display l2-multicast ip forwarding**[ [ **group** *group-address* \| **source** *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display l2-multicast ip forwarding**[ [ **group** *group-address* \| **source** *source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[group** *group-address*]：显示指定组播组的信息。如果未指定本参数，将显示所有组播组的信息。

**[source*** source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【举例】

\# 显示VLAN 2内二层组播的IP转发表信息。

\<Sysname\> display l2-multicast ip forwarding vlan 2

Total 1 entries.

VLAN 2: Total 1 IP entries.

  (0.0.0.0, 224.1.1.1)

    Host slots (0 in total):

    Host ports (3 in total):

      GE1/0/1

      GE1/0/2

      GE1/0/3

\# 显示VSI aaa内二层组播的IP转发表信息。

\<Sysname\> display l2-multicast ip forwarding vsi aaa

Total 1 entries.

VSI aaa: Total 1 IP entries.

  (0.0.0.0, 224.1.1.1)

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)

表1-8 display l2-multicast ip forwarding命令显示信息描述表

字段

描述

Total 1 entries

表项总数

VLAN 2: Total 1 IP entries

VLAN 2内的表项总数

VSI aaa: Total 1 IP entries

VSI aaa内的表项总数

(0.0.0.0, 224.1.1.1)

（S，G）表项，0.0.0.0表示所有组播源

Host slots (0 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Host ports (3 in total)

成员端口及总数

AC (VSI index 0, link ID 1)

AC口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW口的VSI索引和链路标识符

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display l2-multicast mac**

------------------------------------------------------------------------

**[display l2-multicast mac**]命令用来显示二层组播的MAC组播组信息。

【命令】

集中式设备：

**[display l2-multicast mac** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display l2-multicast mac** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display l2-multicast mac** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[mac-address*]：显示指定MAC组播组的信息。如果未指定本参数，将显示所有MAC组播组的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【举例】

\# 显示VLAN 2内二层组播的MAC组播组信息。

\<Sysname\> display l2-multicast mac vlan 2

Total 1 MAC entries.

VLAN 2: Total 1 MAC entries.

  MAC group address: 0100-5e01-0101

    Attribute: success

    Host slots (0 in total):

    Host ports (1 in total):

      GE1/0/1

\# 显示VSI aaa内二层组播的MAC组播组信息。

\<Sysname\> display l2-multicast mac vsi aaa

Total 1 MAC entries.

VSI aaa: Total 1 MAC entries.

  MAC group address: 0100-5e01-0101

    Attribute: success

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)

表1-9 display l2-multicast mac命令显示信息描述表

字段

描述

Total 1 MAC entries

表项总数

VLAN 2: Total 1 MAC entries

VLAN 2内的表项总数

VSI aaa: Total 1 MAC entries

VSI aaa内的表项总数

MAC group address

MAC组播组的地址

Attribute

表项属性，包括：

·success：表示处理成功

·fail：表示处理失败

Host slots (0 in total)

除当前单板外其它所有有成员端口的单板的槽位及总数。本字段的支持情况与设备的型号有关，请以设备的实际情况为准

Host ports (1 in total)

成员端口及总数

AC (VSI index 0, link ID 1)

AC口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW口的VSI索引和链路标识符

**IGMP Snooping \-- IGMP Snooping配置命令 \-- display l2-multicast mac forwarding**

------------------------------------------------------------------------

**[display l2-multicast mac forwarding**]命令用来显示二层组播的MAC转发表信息。

【命令】

集中式设备：

**[display l2-multicast mac forwarding** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display l2-multicast mac forwarding** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display l2-multicast mac forwarding** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[mac-address*]：显示指定MAC组播组的信息。如果未指定本参数，将显示所有MAC组播组的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

【举例】

\# 显示VLAN 2内二层组播的MAC转发表信息。

\<Sysname\> display l2-multicast mac forwarding vlan 2

Total 1 MAC entries.

VLAN 2: Total 1 MAC entries.

  MAC group address: 0100-5e01-0101

    Host slots (0 in total):

    Host ports (3 in total):

      GE1/0/1

      GE1/0/2

      GE1/0/3

\# 显示VSI aaa内二层组播的MAC转发表信息。

\<Sysname\> display l2-multicast mac forwarding vsi aaa

Total 1 MAC entries.

VSI aaa: Total 1 MAC entries.

  MAC group address: 0100-5e01-0101

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)

表1-10 display l2-multicast mac forwarding命令显示信息描述表

字段

描述

Total 1 MAC entries

表项总数

VLAN 2: Total 1 MAC entries

VLAN 2内的表项总数

VSI aaa: Total 1 MAC entries

VSI aaa内的表项总数

MAC group address

MAC组播组的地址

Host slots (0 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Host ports (3 in total)

成员端口及总数

AC (VSI index 0, link ID 1)

AC口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW口的VSI索引和链路标识符

**IGMP Snooping \-- IGMP Snooping配置命令 \-- dot1p-priority (IGMP-Snooping view)**

------------------------------------------------------------------------

**[dot1p-priority**]命令用来全局配置IGMP报文的802.1p优先级。

**[undo dot1p-priority**]命令用来恢复缺省情况。

【命令】

**[dot1p-priority ***priority-number*]

**[undo dot1p-priority**]

【缺省情况】

没有配置IGMP报文的802.1p优先级。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-number*]：IGMP报文的802.1p优先级，取值范围为0～7。该数值越大，优先级越高。

【使用指导】

对于基于VLAN的配置，本命令与**igmp-snooping dot1p-priority**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN都有效，VLAN视图下的配置只对当前VLAN有效，后者的配置优先级较高；对于基于VSI的配置，IGMP-Snooping视图下的全局配置对所有VSI都有效。

【举例】

\# 全局配置IGMP报文的802.1p优先级为3。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping dot1p-priority 3

【相关命令】

·**igmp-snooping dot1p-priority**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- drop-unknown (IGMP-Snooping view)**

------------------------------------------------------------------------

![说明](IGMP%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[drop-unknown**]命令用来全局使能丢弃未知组播数据报文功能。

**[undo drop-unknown**]命令用来全局关闭丢弃未知组播数据报文功能。

【命令】

**[drop-unknown**]

**[undo drop-unknown**]

【缺省情况】

丢弃未知组播数据报文功能处于关闭状态，即对未知组播数据报文进行广播。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令与**igmp-snooping drop-unknown**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效。

【举例】

\# 全局使能丢弃未知组播数据报文功能。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping drop-unknown

【相关命令】

·**igmp-snooping drop-unknown**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- enable (IGMP-Snooping view)**

------------------------------------------------------------------------

**[enable**]命令用来使能指定VLAN内的IGMP Snooping。

**[undo enable**]命令用来关闭指定VLAN内的IGMP Snooping。

【命令】

**[enable** **vlan** *vlan-list*]

**[undo enable** **vlan** *vlan-list*]

【缺省情况】

VLAN内的IGMP Snooping处于关闭状态。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·在使能VLAN内的IGMP Snooping之前，必须先全局使能IGMP Snooping。

·对于基于VLAN的配置，本命令与**igmp-snooping enable**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下可以对指定VLAN进行配置，VLAN视图下只能对当前VLAN进行配置，二者的配置优先级相同。

【举例】

\# 全局使能IGMP Snooping，并使能VLAN 2～10内的IGMP Snooping。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping enable vlan 2 to 10

【相关命令】

·**igmp-snooping**

·**igmp-snooping**** enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- entry-limit (IGMP-Snooping view)**

------------------------------------------------------------------------

**[entry-limit**]命令用来配置IGMP Snooping转发表项（包括动态表项和静态表项）的全局最大数量。

**[undo entry-limit**]命令用来恢复缺省情况。

【命令】

**[entry-limit ***limit*]

**[undo entry-limit**]

【缺省情况】

IGMP Snooping转发表项的全局最大数量为4294967295。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit*]：表示IGMP Snooping转发表项的全局最大数量，取值范围为0～4294967295。

【举例】

\# 配置IGMP Snooping转发表项的全局最大数量为512个。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping entry-limit 512

**IGMP Snooping \-- IGMP Snooping配置命令 \-- fast-leave (IGMP-Snooping view)**

------------------------------------------------------------------------

**[fast-leave**]命令用来全局使能端口快速离开功能。

**[undo fast-leave**]命令用来全局关闭端口快速离开功能。

【命令】

**[fast-leave** [ **vlan** *vlan-list* ]]

**[undo fast-leave** [ **vlan** *vlan-list* ]]

【缺省情况】

端口快速离开功能处于关闭状态。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN和VSI进行配置。

【使用指导】

·端口快速离开是指当端口收到主机发来的离开指定组播组的IGMP离开组报文时，直接将该端口从相应转发表项的出端口列表中删除。

·本命令与**igmp-snooping fast-leave**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 全局使能VLAN 2内的端口快速离开功能。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping fast-leave vlan 2

【相关命令】

·**igmp-snooping fast-leave**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- group-policy (IGMP-Snooping view)**

------------------------------------------------------------------------

**[group-policy**]命令用来全局配置组播组过滤器，以限定主机所能加入的组播组。

**[undo group-policy**]命令用来删除全局组播组过滤器。

【命令】

**[group-policy** *acl-number* [ **vlan** *vlan-list* ]]

**[undo group-policy** [ **vlan** *vlan-list* ]]

【缺省情况】

没有配置组播组过滤器，即主机可以加入任意合法的组播组。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本或高级ACL的编号，取值范围为2000～3999。主机只能加入该ACL规则所允许的组播组。当指定的ACL不存在或ACL中未配置有效规则，将过滤掉所有组播组。

**[vlan **]*vlan-list*：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN和VSI进行配置。

【使用指导】

·对于IPv4基本ACL，该ACL规则中的**source**参数用来指定IGMP报文中的组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv4高级ACL，该ACL规则中的**source**参数用来指定IGMP报文中的组播源地址（对于IGMPv1/v2报文和未携带组播源地址的IS_EX/TO_EX类型的IGMPv3报文，视其组播源地址为0.0.0.0）范围，**destination**参数用来指定组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·可以为端口在不同的VLAN内配置不同的ACL规则，但在相同VLAN内所配置的新规则会取代旧规则。

·本命令只对动态组播组有效，对静态组播组无效。

·本命令与**igmp-snooping ****group-policy**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 全局配置组播组过滤器，以限定VLAN 2内的主机只能加入组播组225.1.1.1。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 225.1.1.1 0

Sysname-acl-ipv4-basic-2000 quit

Sysname igmp-snooping

Sysname-igmp-snooping group-policy 2000 vlan 2

【相关命令】

·**igmp-snooping ****group-policy**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- host-aging-time (IGMP-Snooping view)**

------------------------------------------------------------------------

**[host-aging-time**]命令用来全局配置动态成员端口的老化时间。

**[undo host-aging-time**]命令用来恢复缺省情况。

【命令】

**[host-aging-time** *interval*]

**[undo host-aging-time**]

【缺省情况】

动态成员端口的老化时间为260秒。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示动态成员端口的老化时间，取值范围为200～1000，单位为秒。

【使用指导】

本命令与**igmp-snooping host-aging-time**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 全局配置动态成员端口的老化时间为300秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping host-aging-time 300

【相关命令】

·**igmp-snooping host-aging-time**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping**

------------------------------------------------------------------------

**[igmp-snooping**]命令用来全局使能IGMP Snooping，并进入IGMP-Snooping视图。

**[undo igmp-snooping**]命令用来全局关闭IGMP Snooping。

【命令】

**[igmp-snooping**]

**[undo igmp-snooping**]

【缺省情况】

IGMP Snooping处于全局关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 全局使能IGMP Snooping，并进入IGMP-Snooping视图。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping dot1p-priority**

------------------------------------------------------------------------

**[igmp-snooping dot1p-priority**]命令用来在VLAN内配置IGMP报文的802.1p优先级。

**[undo igmp-snooping dot1p-priority**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping dot1p-priority ***priority-number*]

**[undo igmp-snooping dot1p-priority**]

【缺省情况】

没有配置IGMP报文的802.1p优先级。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-number*]：IGMP报文的802.1p优先级，取值范围为0～7。该数值越大，优先级越高。

【使用指导】

·在配置本命令之前，必须先在VLAN内使能IGMP Snooping。

·对于基于VLAN的配置，本命令与**dot1p-priority**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN都有效，VLAN视图下的配置只对当前VLAN有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置IGMP报文的802.1p优先级为3。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping dot1p-priority 3

【相关命令】

·**dot1p-priority** (IGMP-Snooping view)

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping drop-unknown**

------------------------------------------------------------------------

![说明](IGMP%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[igmp-snooping drop-unknown**]命令用来在VLAN/VSI内使能丢弃未知组播数据报文功能。

**[undo igmp-snooping drop-unknown**]命令用来在VLAN/VSI内关闭丢弃未知组播数据报文功能。

【命令】

**[igmp-snooping drop-unknown**]

**[undo igmp-snooping drop-unknown**]

【缺省情况】

丢弃未知组播数据报文功能处于关闭状态，即对未知组播数据报文进行广播。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

·本命令与**drop-unknown**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并使能丢弃未知组播数据报文功能。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping drop-unknown

\# 在VSI aaa内使能IGMP Snooping，并使能丢弃未知组播数据报文功能。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping drop-unknown

【相关命令】

·**drop-unknown** (IGMP-Snooping view)

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping enable**

------------------------------------------------------------------------

**[igmp-snooping enable**]命令用来在VLAN/VSI内使能IGMP Snooping。

**[undo igmp-snooping enable**]命令用来在VLAN/VSI内关闭IGMP Snooping。

【命令】

**[igmp-snooping enable**]

**[undo igmp-snooping enable**]

【缺省情况】

VLAN/VSI内的IGMP Snooping处于关闭状态。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在VLAN/VSI内使能IGMP Snooping之前，必须先全局使能IGMP Snooping。

·对于基于VLAN的配置，本命令与**enable**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下可以对指定VLAN进行配置，VLAN视图下只能对当前VLAN进行配置，二者的配置优先级相同。

【举例】

\# 全局使能IGMP Snooping，并在VLAN 2内使能IGMP Snooping。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

\# 全局使能IGMP Snooping，并在VSI aaa内使能IGMP Snooping。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

【相关命令】

·**enable**(IGMP-Snooping view)

·**igmp-snooping**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping fast-leave**

------------------------------------------------------------------------

**[igmp-snooping fast-leave**]命令用来在端口上使能端口快速离开功能。

**[undo igmp-snooping fast-leave**]命令用来在端口上关闭端口快速离开功能。

【命令】

**[igmp-snooping fast-leave** [ **vlan** *vlan-list* ]]

**[undo igmp-snooping fast-leave** [ **vlan** *vlan-list* ]]

【缺省情况】

端口快速离开功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

·端口快速离开是指当端口收到主机发来的离开指定组播组的IGMP离开组报文时，直接将该端口从相应转发表项的出端口列表中删除。

·本命令与**fast-leave**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 将端口GigabitEthernet1/0/1在VLAN 2内使能端口快速离开功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping fast-leave vlan 2

【相关命令】

·**fast-leave** (IGMP-Snooping view)

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping general-query source-ip**

------------------------------------------------------------------------

**[igmp-snooping general-query source-ip**]命令用来配置IGMP普遍组查询报文的源IP地址。

**[undo igmp-snooping general-query source-ip**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping general-query source-ip** *ip-address*]

**[undo igmp-snooping general-query source-ip**]

【缺省情况】

·在VLAN内，IGMP普遍组查询报文的源IP地址为当前VLAN接口的IP地址；若当前VLAN接口没有IP地址，则采用0.0.0.0。

·在VSI内，IGMP普遍组查询报文的源IP地址为0.0.0.0。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：表示IGMP普遍组查询报文的源IP地址。

【使用指导】

在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置IGMP普遍组查询报文的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping general-query source-ip 10.1.1.1

\# 在VSI aaa内使能IGMP Snooping，并配置IGMP普遍组查询报文的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping general-query source-ip 10.1.1.1

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping group-limit**

------------------------------------------------------------------------

**[igmp-snooping group-limit**]命令用来[配置端口加入的组播组最大数量。]

**[undo **]**igmp-snooping group-limit**命令用来恢复缺省情况。

【命令】

**[igmp-snooping group-limit** *limit* [ **vlan** *vlan-list* ]]

**[undo igmp-snooping group-limit** [ **vlan** *vlan-list* ]]

【缺省情况】

端口加入的组播组最大数量为4294967295。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit*]：表示端口加入的组播组最大数量，取值范围为0～4294967295。

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

本命令只对动态组播组有效，对静态组播组无效。

【举例】

\# 配置端口GigabitEthernet1/0/1在VLAN 2内加入的组播组最大数量为10个。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping group-limit 10 vlan 2

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping group-policy**

------------------------------------------------------------------------

**[igmp-snooping group-policy**]命令用来[在端口上配置组播组过滤器]，以限定主机所能加入的组播组。

**[undo **]**igmp-snooping group-policy**命令用来删除端口上的组播组过滤器。

【命令】

**[igmp-snooping group-policy** *acl-number* [ **vlan** *vlan-list* ]]

**[undo igmp-snooping group-policy** [ **vlan** *vlan-list* ]]

【缺省情况】

没有配置组播组过滤器，即主机可以加入任意合法的组播组。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本或高级ACL的编号，取值范围为2000～3999。主机只能加入该ACL规则所允许的组播组。当指定的ACL不存在或ACL中未配置有效规则，将过滤掉所有组播组。

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

·对于IPv4基本ACL，该ACL规则中的**source**参数用来指定IGMP报文中的组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv4高级ACL，该ACL规则中的**source**参数用来指定IGMP报文中的组播源地址（对于IGMPv1/v2报文和未携带组播源地址的IS_EX/TO_EX类型的IGMPv3报文，视其组播源地址为0.0.0.0）范围，**destination**参数用来指定组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·可以为端口在不同的VLAN内配置不同的ACL规则，但在相同VLAN内所配置的新规则会取代旧规则。

·本命令只对动态组播组有效，对静态组播组无效。

·本命令与**group-policy**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 在端口GigabitEthernet1/0/1上配置组播组过滤器，以限定VLAN 2内的主机只能加入组播组225.1.1.1。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 225.1.1.1 0

Sysname-acl-ipv4-basic-2000 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping group-policy 2000 vlan 2

【相关命令】

·**group-policy** (IGMP-Snooping view)

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping host-aging-time**

------------------------------------------------------------------------

**[igmp-snooping host-aging-time**]命令用来在VLAN/VSI内配置动态成员端口的老化时间。

**[undo igmp-snooping host-aging-time**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping host-aging-time** *interval*]

**[undo igmp-snooping host-aging-time**]

【缺省情况】

动态成员端口的老化时间为260秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示动态成员端口的老化时间，取值范围为200～1000，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

·本命令与**host-aging-time**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置动态成员端口的老化时间为300秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping host-aging-time 300

\# 在VSI aaa内使能IGMP Snooping，并配置动态成员端口的老化时间为300秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping host-aging-time 300

【相关命令】

·**enable** (IGMP-Snooping view)

·**host-aging-time** (IGMP-Snooping view)

·**igmp-snooping enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping host-join**

------------------------------------------------------------------------

**[igmp-snoopinghost-join**]命令用来[配置模拟主机加入组播组或组播源组。模拟主机加入就是将二层设备的端口配置为组播组的成员。]

**[undo **]**igmp-snoopinghost-join**命令用来删除模拟主机加入的配置。

【命令】

**[igmp-snoopinghost-join ***group-address* [ **source-ip** *source-address*  **vlan** *vlan-id*]]

**[undo **]**igmp-snoopinghost-join** { *group-address* [ **source-ip** *source-address*  **vlan** *vlan-id* \| **all** }]

【缺省情况】

没有配置模拟主机加入组播组或组播源组。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：表示模拟主机要加入的组播组的地址，取值范围为224.0.1.0～239.255.255.255。

**[source-ip ***source-address*]：表示模拟主机要加入的组播源的地址。如果指定了本参数，表示加入组播源组；如果未指定本参数，则表示加入组播组。配置有本参数的模拟主机，只在IGMP Snooping版本3下生效。

**[vlan** *vlan-id*]：表示对指定VLAN进行配置。*vlan-id*为VLAN的编号，取值范围为1～4094。

**[all**]：表示对所有组播组和组播源组进行配置。

【使用指导】

·与静态成员端口不同，配置了模拟主机加入的端口将作为动态成员端口参与动态成员端口的老化过程。

·模拟主机所采用的IGMP版本与IGMP Snooping的版本一致。

【举例】

\# 在端口GigabitEthernet1/0/1上配置模拟主机加入VLAN 2内的组播源组（1.1.1.1，232.1.1.1）。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping version 3

Sysname-vlan2 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping host-join 232.1.1.1 source-ip 1.1.1.1 vlan 2

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping last-member-query-interval**

------------------------------------------------------------------------

**[igmp-snooping last-member-query-interval**]命令用来在VLAN/VSI内配置IGMP特定组查询报文的发送间隔。

**[undo igmp-snooping last-member-query-interval**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping last-member-query-interval ***interval*]

**[undo igmp-snooping last-member-query-interval**]

【缺省情况】

IGMP特定组查询报文的发送间隔为1秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IGMP特定组查询报文的发送间隔，取值范围为1～5，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

·本命令与**last-member-query-interval**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置IGMP特定组查询报文的发送间隔为3秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping last-member-query-interval 3

\# 在VSI aaa内使能IGMP Snooping，并配置IGMP特定组查询报文的发送间隔为3秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping last-member-query-interval 3

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

·**last-member-query-interval** (IGMP-Snooping view)

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping leave source-ip**

------------------------------------------------------------------------

**[igmp-snooping leave source-ip**]命令用来配置IGMP离开组报文的源IP地址。

**[undo igmp-snooping leave source-ip**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping leave source-ip** *ip-address*]

**[undo igmp-snooping leave source-ip**]

【缺省情况】

IGMP离开组报文的源IP地址为当前VLAN接口的IP地址；若当前VLAN接口没有IP地址，则采用0.0.0.0。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：表示IGMP离开组报文的源IP地址。

【使用指导】

在配置本命令之前，必须先在VLAN内使能IGMP Snooping。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置IGMP离开组报文的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping leave source-ip 10.1.1.1

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping max-response-time**

------------------------------------------------------------------------

**[igmp-snooping max-response-time**]命令用来在VLAN/VSI内配置IGMP普遍组查询的最大响应时间。

**[undo igmp-snooping max-response-time**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping max-response-time** *interval*]

**[undo igmp-snooping max-response-time**]

【缺省情况】

IGMP普遍组查询的最大响应时间为10秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IGMP普遍组查询的最大响应时间，取值范围为1～25，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

·为避免误删组播组成员，请确保IGMP普遍组查询的最大响应时间小于IGMP普遍组查询报文的发送间隔，否则配置虽能生效但系统会给出提示。

·本命令与**max-response-time**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置IGMP普遍组查询的最大响应时间为5秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping max-response-time 5

\# 在VSI aaa内使能IGMP Snooping，并配置IGMP普遍组查询的最大响应时间为5秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping max-response-time 5

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

·**igmp-snooping query-interval**

·**max-response-time** (IGMP-Snooping view)

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping overflow-replace**

------------------------------------------------------------------------

**[igmp-snooping overflow-replace**]命令用来在端口上使能组播组替换功能。

**[undo **]**igmp-snooping overflow-replace**命令用来在端口上关闭组播组替换功能。

【命令】

**[igmp-snooping overflow-replace** [ **vlan** *vlan-list* ]]

**[undo igmp-snooping overflow-replace** [ **vlan** *vlan-list* ]]

【缺省情况】

组播组替换功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

·本命令只对动态组播组有效，对静态组播组无效。

·本命令与**overflow-replace**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 将端口GigabitEthernet1/0/1在VLAN 2内使能组播组替换功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping overflow-replace vlan 2

【相关命令】

·**overflow-replace** (IGMP-Snooping view)

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping querier**

------------------------------------------------------------------------

**[igmp-snooping querier**]命令用来使能IGMP Snooping查询器。

**[undo igmp-snooping querier**]命令用来关闭IGMP Snooping查询器。

【命令】

**[igmp-snooping querier**]

**[undo igmp-snooping querier**]

【缺省情况】

IGMP Snooping查询器处于关闭状态。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

·如果在组播VLAN的子VLAN内配置了本命令，只有当该子VLAN被从组播VLAN中删除后，IGMP Snooping查询器才会生效。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并使能IGMP Snooping查询器。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping querier

\# 在VSI aaa内使能IGMP Snooping，并使能IGMP Snooping查询器。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping querier

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

·**subvlan** (multicast-VLAN view)（IP组播命令参考/组播VLAN）

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping query-interval**

------------------------------------------------------------------------

**[igmp-snooping query-interval**]命令用来在VLAN/VSI内配置IGMP普遍组查询报文的发送间隔。

**[undo igmp-snooping query-interval**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping query-interval** *interval*]

**[undo igmp-snooping query-interval**]

【缺省情况】

IGMP普遍组查询报文的发送间隔为125秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IGMP普遍组查询报文的发送间隔，取值范围为2～300，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

·为避免误删组播组成员，请确保IGMP普遍组查询报文的发送间隔大于IGMP普遍组查询的最大响应时间，否则配置虽能生效但系统会给出提示。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置IGMP普遍组查询报文的发送间隔为20秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping query-interval 20

\# 在VSI aaa内使能IGMP Snooping，并配置IGMP普遍组查询报文的发送间隔为20秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping query-interval 20

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

·**igmp-snooping max-response-time**

·**igmp-snooping querier**

·**max-response-time**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping report source-ip**

------------------------------------------------------------------------

**[igmp-snooping report source-ip**]命令用来配置IGMP成员关系报告报文的源IP地址。

**[undo igmp-snooping report source-ip**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping report source-ip** *ip-address*]

**[undo igmp-snooping report source-ip**]

【缺省情况】

IGMP成员关系报告报文的源IP地址为当前VLAN接口的IP地址；若当前VLAN接口没有IP地址，则采用0.0.0.0。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：表示IGMP成员关系报告报文的源IP地址。

【使用指导】

在配置本命令之前，必须先在VLAN内使能IGMP Snooping。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置IGMP成员关系报告报文的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping report source-ip 10.1.1.1

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping router-aging-time**

------------------------------------------------------------------------

**[igmp-snooping router-aging-time**]命令用来在VLAN/VSI内配置动态路由器端口的老化时间。

**[undo igmp-snooping router-aging-time**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping router-aging-time** *interval*]

**[undo igmp-snooping router-aging-time**]

【缺省情况】

动态路由器端口的老化时间为260秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示动态路由器端口的老化时间，取值范围为1～1000，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

·本命令与**router-aging-time**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置动态路由器端口的老化时间为100秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping router-aging-time 100

\# 在VSI aaa内使能IGMP Snooping，并配置动态路由器端口的老化时间为100秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping router-aging-time 100

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

·**router-aging-time** (IGMP-Snooping view)

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping router-port-deny**

------------------------------------------------------------------------

**[igmp-snooping router-port-deny**]命令用来禁止端口成为动态路由器端口。

**[undo igmp-snooping router-port-deny**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping router-port-deny** [ **vlan** *vlan-list* ]]

**[undo igmp-snooping router-port-deny** [ **vlan** *vlan-list* ]]

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省情况】

允许端口成为动态路由器端口。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示多个VLAN。其表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果指定了本参数，只有当该端口属于指定VLAN时，本配置才生效；如果未指定本参数，则本配置将对该端口所属的所有VLAN和VSI都生效。

【举例】

\# 禁止端口GigabitEthernet1/0/1在VLAN 2内成为动态路由器端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping router-port-deny vlan 2

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping source-deny**

------------------------------------------------------------------------

![说明](IGMP%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[igmp-snoopingsource-deny**]命令用来使能当前端口的组播数据报文源端口过滤功能。

**[undo **]**igmp-snoopingsource-deny**命令用来关闭当前端口的组播数据报文源端口过滤功能。

【命令】

**[igmp-snoopingsource-deny**]

**[undo igmp-snooping source-deny**]

【缺省情况】

组播数据报文源端口过滤功能处于关闭状态。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令与**source-deny**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下可以对指定端口进行配置，端口视图下只能对当前端口进行配置，二者的配置优先级相同。

【举例】

\# 在端口GigabitEthernet1/0/1上使能组播数据报文源端口过滤功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping source-deny

【相关命令】

·**source-deny** (IGMP-Snooping view)

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping special-query source-ip**

------------------------------------------------------------------------

**[igmp-snooping special-query source-ip**]命令用来配置IGMP特定组查询报文的源IP地址。

**[undo igmp-snooping special-query source-ip**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping special-query source-ip** *ip-address*]

**[undo igmp-snooping special-query source-ip**]

【缺省情况】

·在VLAN内，如果收到过IGMP普遍组查询报文，则以其源IP地址作为IGMP特定组查询报文的源IP地址；否则，采用当前VLAN接口的IP地址；若当前VLAN接口没有IP地址，则采用0.0.0.0。

·在VSI内，如果收到过IGMP普遍组查询报文，则以其源IP地址作为IGMP特定组查询报文的源IP地址；否则，采用0.0.0.0。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：表示IGMP特定组查询报文的源IP地址。

【使用指导】

在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置IGMP特定组查询报文的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping special-query source-ip 10.1.1.1

\# 在VSI aaa内使能IGMP Snooping，并配置IGMP特定组查询报文的源IP地址为10.1.1.1。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping special-query source-ip 10.1.1.1

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping static-group**

------------------------------------------------------------------------

**[igmp-snooping static-group**]命令用来配置静态成员端口，即配置端口静态加入组播组或组播源组。

**[undo **]**igmp-snooping static-group**命令用来删除静态成员端口的配置。

【命令】

**[igmp-snooping static-group** *group-address* [ **source-ip** *source-address*  **vlan** *vlan-id*]]

**[undo igmp-snooping static-group** { *group-address* [ **source-ip** *source-address*  **vlan** *vlan-id* \| **all** }]]

【缺省情况】

端口不是静态成员端口。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：表示静态加入的组播组地址，取值范围为224.0.1.0～239.255.255.255。

**[source-ip ***source-address*]：表示静态加入的组播源地址。如果指定了本参数，表示加入组播源组；如果未指定本参数，则表示加入组播组。配置有本参数的静态成员端口，只在IGMP Snooping版本3下生效。

**[vlan** *vlan-id*]：表示对指定VLAN进行配置。*vlan-id*为VLAN的编号，取值范围为1～4094。

**[all**]：表示对所有组播组和组播源组进行配置。

【举例】

\# 将端口GigabitEthernet1/0/1配置为组播源组（1.1.1.1，225.0.0.1）在VLAN 2内的静态成员端口。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping version 3

Sysname-vlan2 quit

Sysname interface Gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping static-group 225.0.0.1 source-ip 1.1.1.1 vlan 2

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping static-router-port**

------------------------------------------------------------------------

**[igmp-snooping static-router-port**]命令用来配置静态路由器端口。

**[undo **]**igmp-snooping static-router-port**命令用来删除静态路由器端口的配置。

【命令】

**[igmp-snooping static-router-port vlan ***vlan-id*]

**[undo igmp-snooping static-router-port**[ { **all** \| **vlan** *vlan-id* }]]

【缺省情况】

端口不是静态路由器端口。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示对所有VLAN进行配置。

**[vlan** *vlan-id*]：表示对指定VLAN进行配置。*vlan-id*为VLAN的编号，取值范围为1～4094。

【举例】

\# 将端口GigabitEthernet1/0/1配置为VLAN 2内的静态路由器端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp-snooping static-router-port vlan 2

**IGMP Snooping \-- IGMP Snooping配置命令 \-- igmp-snooping version**

------------------------------------------------------------------------

**[igmp-snooping version**]命令用来在VLAN/VSI内配置IGMP Snooping的版本。

**[undo igmp-snooping version**]命令用来恢复缺省情况。

【命令】

**[igmp-snooping version ***version-number*]

**[undo igmp-snooping version**]

【缺省情况】

VLAN/VSI内IGMP Snooping的版本为2。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[version-number*]：表示IGMP Snooping的版本号，取值范围为2～3。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能IGMP Snooping。

·对于基于VLAN的配置，本命令与**version**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下可以对指定VLAN进行配置，VLAN视图下只能对当前VLAN进行配置，二者的配置优先级相同。

【举例】

\# 在VLAN 2内使能IGMP Snooping，并配置该VLAN内的IGMP Snooping版本为3。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vlan 2

Sysname-vlan2 igmp-snooping enable

Sysname-vlan2 igmp-snooping version 3

\# 在VSI aaa内使能IGMP Snooping，并配置该VSI内的IGMP Snooping版本为3。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa igmp-snooping enable

Sysname-vsi-aaa igmp-snooping version 3

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

·**version** (IGMP-Snooping view)

**IGMP Snooping \-- IGMP Snooping配置命令 \-- last-member-query-interval (IGMP-Snooping view)**

------------------------------------------------------------------------

**[last-member-query-interval**]命令用来全局配置IGMP特定组查询报文的发送间隔。

**[undo last-member-query-interval**]命令用来恢复缺省情况。

【命令】

**[last-member-query-interval ***interval*]

**[undo last-member-query-interval**]

【缺省情况】

IGMP特定组查询报文的发送间隔为1秒。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IGMP特定组查询报文的发送间隔，取值范围为1～5，单位为秒。

【使用指导】

本命令与**igmp-snooping last-member-query-interval**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 全局配置IGMP特定组查询报文的发送间隔为3秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping last-member-query-interval 3

【相关命令】

·**igmp-snooping** **last-member-query-interval**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- max-response-time (IGMP-Snooping view)**

------------------------------------------------------------------------

**[max-response-time**]命令用来全局配置IGMP普遍组查询的最大响应时间。

**[undo max-response-time**]命令用来恢复缺省情况。

【命令】

**[max-response-time** *interval*]

**[undo max-response-time**]

【缺省情况】

IGMP普遍组查询的最大响应时间为10秒。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IGMP普遍组查询的最大响应时间，取值范围为1～25，单位为秒。

【使用指导】

·为避免误删组播组成员，请确保IGMP普遍组查询的最大响应时间小于IGMP普遍组查询报文的发送间隔，否则配置虽能生效但系统会给出提示。

·本命令与**igmp-snooping max-response-time**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 全局配置IGMP普遍组查询的最大响应时间为5秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping max-response-time 5

【相关命令】

·**igmp-snooping max-response-time**

·**igmp-snooping query-interval**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- overflow-replace (IGMP-Snooping view)**

------------------------------------------------------------------------

**[overflow-replace**]命令用来全局使能组播组替换功能。

**[undo overflow-replace**]命令用来全局关闭组播组替换功能。

【命令】

**[overflow-replace** [ **vlan** *vlan-list* ]]

**[undo overflow-replace** [ **vlan** *vlan-list* ]]

【缺省情况】

组播组替换功能处于关闭状态。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

·本命令只对动态组播组有效，对静态组播组无效。

·本命令与**igmp-snooping overflow-replace**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 全局使能VLAN 2内的组播组替换功能。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping overflow-replace vlan 2

【相关命令】

·**igmp-snooping overflow-replace**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- report-aggregation (IGMP-Snooping view)**

------------------------------------------------------------------------

**[report-aggregation**]命令用来使能IGMP成员关系报告报文抑制功能。

**[undo report-aggregation**]命令用来关闭IGMP成员关系报告报文抑制功能。

【命令】

**[report-aggregation**]

**[undo report-aggregation**]

【缺省情况】

IGMP成员关系报告报文抑制功能处于使能状态。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭IGMP成员关系报告报文抑制功能。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping undo report-aggregation

**IGMP Snooping \-- IGMP Snooping配置命令 \-- reset igmp-snooping group**

------------------------------------------------------------------------

**[reset **]**igmp-snooping group**命令用来清除动态IGMP Snooping转发表的信息。

【命令】

**[reset igmp-snooping group** { *group-address* [ *source-address*  \| **all** } [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：清除指定组播组的信息，取值范围为224.0.1.0～239.255.255.255。

*[source-address*]：清除指定组播源的信息。如果未指定本参数，将清除所有组播源的信息。

**[all**]：清除所有组播组的信息。

**[vlan*** vlan-id*]：清除指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将清除所有VLAN内的信息。

**[vsi** *vsi-name*]：清除指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除所有VSI内的信息。

【举例】

\# 清除所有动态IGMP Snooping转发表的信息。

\<Sysname\> reset igmp-snoopinggroup all

【相关命令】

·**display igmp-snooping group**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- reset igmp-snooping router-port**

------------------------------------------------------------------------

**[reset **]**igmp-snoopingrouter-port**命令用来清除动态路由器端口的信息。

【命令】

**[reset igmp-snooping router-port**[ { **all** \| **vlan** *vlan-id* \| **vsi** *vsi-name* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：清除所有动态路由器端口的信息。

**[vlan*** vlan-id*]：清除指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将清除所有VLAN内的信息。

**[vsi** *vsi-name*]：清除指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除所有VSI内的信息。

【举例】

\# 清除所有动态路由器端口的信息。

\<Sysname\> reset igmp-snoopingrouter-port all

【相关命令】

·**display igmp-snooping router-port**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- reset igmp-snooping statistics**

------------------------------------------------------------------------

**[reset igmp-snooping statistics**]命令用来清除IGMP Snooping监听到的IGMP报文统计信息。

【命令】

**[reset igmp-snooping statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除IGMP Snooping监听到的IGMP报文统计信息。

\<Sysname\> reset igmp-snooping statistics

【相关命令】

·**display igmp-snooping statistics**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- router-aging-time (IGMP-Snooping view)**

------------------------------------------------------------------------

**[router-aging-time**]命令用来全局配置动态路由器端口的老化时间。

**[undo router-aging-time**]命令用来恢复缺省情况。

【命令】

**[router-aging-time** *interval*]

**[undo router-aging-time**]

【缺省情况】

动态路由器端口的老化时间为260秒。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示动态路由器端口的老化时间，取值范围为1～1000，单位为秒。

【使用指导】

本命令与**igmp-snooping router-aging-time**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 全局配置动态路由器端口的老化时间为100秒。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping router-aging-time 100

【相关命令】

·**igmp-snooping router-aging-time**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- source-deny (IGMP-Snooping view)**

------------------------------------------------------------------------

![说明](IGMP%20Snooping命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-deny**]命令用来使能指定端口的组播数据报文源端口过滤功能。

**[undo source-deny**]命令用来关闭指定端口的组播数据报文源端口过滤功能。

【命令】

**[source-deny port** *interface-list*]

**[undo source-deny port** *interface-list*]

【缺省情况】

组播数据报文源端口过滤功能处于关闭状态。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[port** *interface-list*]：表示对指定端口进行配置。*interface-list*为端口列表，表示一或多个端口，表示方式为*interface-list* = { *interface-type* *interface-number* [ **to** *interface-type* *interface-number*  }]，其中，*interface-type*为接口类型，*interface-number*为接口编号。

【使用指导】

本命令与**igmp-snooping source-deny**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下可以对指定端口进行配置，端口视图下只能对当前端口进行配置，二者的配置优先级相同。

【举例】

\# 使能端口GigabitEthernet1/0/1～GigabitEthernet1/0/4上的组播数据报文源端口过滤功能。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping source-deny port gigabitethernet 1/0/1 to gigabitethernet 1/0/4

【相关命令】

·**igmp-snoopingsource-deny**

**IGMP Snooping \-- IGMP Snooping配置命令 \-- version (IGMP-Snooping view)**

------------------------------------------------------------------------

**[version**]命令用来配置指定VLAN内的IGMP Snooping的版本。

**[undo version**]命令用来恢复缺省情况。

【命令】

**[version ***version-number* **vlan** *vlan-list*]

**[undo version** **vlan** *vlan-list*]

【缺省情况】

VLAN内IGMP Snooping的版本为2。

【视图】

IGMP-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[version-number*]：表示IGMP Snooping的版本号，取值范围为2～3。

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·在配置本命令之前，必须先在VLAN内使能IGMP Snooping。

·对于基于VLAN的配置，本命令与**igmp-snooping version**命令的功能相同，只是作用范围不同：IGMP-Snooping视图下可以对指定VLAN进行配置，VLAN视图下只能对当前VLAN进行配置，二者的配置优先级相同。

【举例】

\# 使能VLAN 2～10内的IGMP Snooping，并配置这些VLAN内的IGMP Snooping版本为3。

\<Sysname\> system-view

Sysname igmp-snooping

Sysname-igmp-snooping enable vlan 2 to 10

Sysname-igmp-snooping version 3 vlan 2 to 10

【相关命令】

·**enable** (IGMP-Snooping view)

·**igmp-snooping enable**

·**igmp-snooping**** version**

