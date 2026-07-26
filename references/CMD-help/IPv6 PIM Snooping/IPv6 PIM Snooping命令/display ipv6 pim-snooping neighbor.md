
**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- display ipv6 pim-snooping neighbor**

------------------------------------------------------------------------

**[display ipv6 pim-snooping neighbor**]命令用来显示IPv6 PIM Snooping的邻居信息。

【命令】

集中式设备：

**[display ipv6 pim-snooping neighbor**[ [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 pim-snooping neighbor**[ [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number*   **verbose** ]]

分布式设备－IRF模式：

**[display ipv6 pim-snooping neighbor**[ [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[verbose**]：显示详细信息。如果未指定本参数，将显示简要信息。

【举例】

\# 显示VLAN 2内IPv6PIM Snooping的邻居详细信息。

\<Sysname\> display ipv6 pim-snooping neighbor vlan 2 verbose

Total 2 neighbors.

VLAN 2: Total 2 neighbors.

  FE80::6401:101

    Slots (0 in total):

    Ports (1 in total):

      GE1/0/1                             (02:02:23)    LAN Prune Delay(T)

  FE80::C801:101

    Slots (0 in total):

    Ports (1 in total):

      GE1/0/2                             (02:02:25)

\# 显示VSI aaa内IPv6 PIM Snooping的邻居信息。

\<Sysname\> display ipv6 pim-snooping neighbor vsi aaa

Total 2 neighbors.

VSI aaa: Total 2 neighbors.

  FE80::1

    Slots (0 in total):

    Ports (1 in total):

      AC (VSI index 0 Link ID 2)          (00:02:04)

  FE80::2

    Slots (0 in total):

    Ports (1 in total):

      AC (VSI index 0 Link ID 1)          (00:02:13)

表1-1 display ipv6 pim-snooping neighbor命令显示信息描述表

字段

描述

Total 2 neighbors

IPv6 PIM Snooping邻居的总数

VLAN 2: Total 2 neighbors

VLAN 2内的表项总数

VSI aaa: Total 2 neighbors

VSI aaa内的表项总数

FE80::6401:101

IPv6 PIM Snooping邻居的IPv6地址

Slots (0 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有IPv6 PIM Snooping邻居的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有IPv6 PIM Snooping邻居的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有IPv6 PIM Snooping邻居的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Ports (1 in total)

IPv6 PIM Snooping邻居所在的端口及总数

(02:02:23)

IPv6 PIM Snooping邻居所在端口的老化剩余时间。需要注意的是，本字段对于全局口（包括二层聚合接口、AC口、N-PW口、U-PW口等）将无条件显示，而对于非全局口：

·在集中式设备上，将无条件显示

·在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示

·在集中式IRF设备上，若该口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示

·在分布式设备－IRF模式上，若该口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示

LAN Prune Delay

表示该邻居发出的PIM Hello报文中携带有LAN_Prune_Delay选项

(T)

表示该邻居已禁止加入报文抑制能力

AC (VSI index 0 Link ID 1)

AC（Attachment Circuit，接入电路）口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW（Network Pseudowire，网络侧伪线）口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW（User facing Pseudowire，用户侧伪线）口的VSI索引和链路标识符

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- display ipv6 pim-snooping router-port**

------------------------------------------------------------------------

**[display ipv6 pim-snooping router-port**]命令用来显示IPv6PIM Snooping的路由器端口信息。

【命令】

集中式设备：

**[display ipv6 pim-snooping router-port**[ [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 pim-snooping router-port**[ [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display ipv6 pim-snooping router-port**[ [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果不指定该参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果不指定该参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定该参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示VLAN 2内IPv6PIM Snooping的路由器端口信息。

\<Sysname\> display ipv6 pim-snooping router-port vlan 2

VLAN 2:

  Router slots (0 in total):

  Router ports (2 in total):

    GE1/0/1                             (00:01:30)

    GE1/0/2                             (00:01:32)

\# 显示VSI aaa 内IPv6 PIM Snooping的路由器端口信息。

\<Sysname\> display ipv6 pim-snooping router-port vsi aaa

VSI aaa:

  Router slots (0 in total):

  Router ports (2 in total):

    AC (VSI index 0 Link ID 0)          (00:02:43)

    AC (VSI index 0 Link ID 1)          (00:02:52)

表1-2 display ipv6 pim-snooping router-port命令显示信息描述表

字段

描述

VLAN 2

VLAN的编号

VSI aaa

VSI的名称

Router slots (1 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有路由器端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有路由器端口的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有路由器端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Router ports (2 in total)

路由器端口的及总数

(00:01:30)

路由器端口的老化剩余时间。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：

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

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- display ipv6 pim-snooping routing-table**

------------------------------------------------------------------------

**[display ipv6 pim-snooping routing-table**]命令用来显示IPv6 PIM Snooping路由表的信息。

【命令】

集中式设备：

**[display ipv6 pim-snooping routing-table **[[ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 pim-snooping routing-table **[[ **vlan** *vlan-id* \| **vsi** *vsi-name* ] slot *slot-number*   **verbose** ]]

分布式设备－IRF模式：

**[display ipv6 pim-snooping routing-table **[[ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上维护的信息。（分布式设备－独立运行模式）]

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[verbose**]：显示详细信息。如果未指定本参数，将显示简要信息。

【举例】

\# 显示VLAN 2内IPv6 PIM Snooping路由表的详细信息。

\<Sysname\> display ipv6 pim-snooping routing-table vlan 2 verbose

Total 1 entries.

FSM Flag: NI-no info, J-join, PP-prune pending

VLAN 2: Total 1 entries.

  (2000::1, FF1E::1)

    FSM information: normal

    Upstream neighbor: FE80::101

      Upstream Slots (0 in total):

      Upstream Ports (1 in total):

        GE1/0/1

      Downstream Slots (0 in total):

      Downstream Ports (2 in total):

        GE1/0/2

          Expires: 00:03:01, FSM: J

          Downstream Neighbors (2 in total):

            1001::1

              Expires: 00:59:19, FSM: J

            1001::2

              Expires: 00:59:20, FSM: J

        GE1/0/3

          Expires: 00:02:21, FSM: PP

\# 显示VSI aaa内IPv6 PIM Snooping路由表的信息。

\<Sysname\> display ipv6 pim-snooping routing-table vsi aaa

Total 1 entries.

FSM Flag: NI-no info, J-join, PP-prune pending

VSI aaa: Total 1 entries.

  (3000::1, FF1E::101)

    Upstream neighbor: FE80::1

      Upstream Slots (0 in total):

      Upstream Ports (1 in total):

        AC (VSI index 0 Link ID 0)

      Downstream Slots (0 in total):

      Downstream Ports (1 in total):

        AC (VSI index 0 Link ID 1)

           Expires: 00:02:41, FSM: J

表1-3 display ipv6 pim-snooping routing-table命令显示信息描述表

字段

描述

Total 1 entries

IPv6 PIM Snooping路由表中（S，G）与（\*，G）表项的总数

FSM Flag: NI-no info, J-join, PP-prune pending

下游端口的状态机标识：NI表示初始状态，J表示加入状态，PP表示剪枝未决状态

(2000::1, FF1E::1)

IPv6 PIM Snooping路由表中的（S，G）表项

FSM information

表项状态机，包括：

·delete：表示所有成员属性均已删除

·dummy：表示新创建的临时表项

·no info：表示没有表项存在

·normal：表示主控板通知创建的正式表项

Upstream neighbor

上游邻居

Upstream Slots (1 in total)

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有上游邻居的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有上游邻居的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有上游邻居的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Upstream Ports (1 in total)

上游邻居所在的端口及总数。需要注意的是，本字段：

·在集中式设备上，将无条件显示

·在分布式设备－独立运行模式上，若上游端口属于主控板，会显示；否则须指定其所在单板的槽位号才会显示

·在集中式IRF设备上，若上游端口属于主设备，会显示；否则须指定其所在成员设备的编号才会显示

·在分布式设备－IRF模式上，若上游端口属于主控板，会显示；否则须指定其所在成员设备的编号和单板的槽位号才会显示

Downstream Slots (2 in total)

除当前单板外其它所有有下游端口的单板的槽位及总数。本字段的支持情况与设备的型号有关，请以设备的实际情况为准

Downstream Ports (2 in total)

下游端口及总数

Downstream Neighbors (2 in total)

下游端口包含的下游邻居及总数

Expires: 00:03:01, FSM: J

下游端口或下游邻居的老化剩余时间和状态机。需要注意的是，本字段对于全局口将无条件显示，而对于非全局口：

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

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- display ipv6 pim-snooping statistics**

------------------------------------------------------------------------

**[display ipv6 pim-snooping statistics**]命令用来显示IPv6 PIM Snooping监听到的IPv6 PIM报文的统计信息。

【命令】

**[display ipv6 pim-snooping statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IPv6 PIM Snooping监听到的IPv6 PIM报文的统计信息。

\<Sysname\> display ipv6 pim-snooping statistics

Received IPv6 PIM hello:  100

Received IPv6 PIM join/prune:  100

Received IPv6 PIM error:  0

Received IPv6 PIM messages in total:  200

表1-4 display ipv6 pim-snooping statistics命令显示信息描述表

字段

描述

Received IPv6 PIM hello

收到的IPv6 PIM Hello报文数

Received IPv6 PIM join/prune

收到的IPv6 PIM加入/剪枝报文数

Received IPv6 PIM error

收到的错误IPv6 PIM报文数

Received IPv6 PIM messages in total

收到的IPv6 PIM报文总数

【相关命令】

·**reset ipv6 pim-snooping statistics**

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- ipv6 pim-snooping enable**

------------------------------------------------------------------------

**[ipv6 pim-snooping enable**]命令用来在VLAN/VSI内使能IPv6 PIM Snooping。

**[undo ipv6 pim-snooping enable**]命令用来在VLAN/VSI内关闭IPv6 PIM Snooping。

【命令】

**[ipv6 pim-snooping enable**]

**[undo ipv6 pim-snooping enable**]

【缺省情况】

VLAN/VSI内的IPv6 PIM Snooping处于关闭状态。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在VLAN/VSI内使能IPv6 PIM Snooping之前，必须先在全局以及该VLAN/VSI内使能MLD Snooping。

·在组播VLAN的子VLAN内使能IPv6 PIM Snooping无效。

【举例】

\# 全局使能MLD Snooping，并在VLAN 2内使能MLD Snooping和IPv6 PIM Snooping。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 ipv6 pim-snooping enable

\# 全局使能MLD Snooping，并在VSI aaa内使能MLD Snooping和IPv6 PIM Snooping。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa ipv6 pim-snooping enable

【相关命令】

·**mld-snooping**（IP组播命令参考/MLD Snooping）

·**mld-snooping enable**（IP组播命令参考/MLD Snooping）

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- ipv6 pim-snooping graceful-restart join-aging-time**

------------------------------------------------------------------------

![说明](IPv6%20PIM%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 pim-snooping graceful-restart join-aging-time**]命令用来配置主备倒换期间新主用主控板上IPv6 PIM Snooping全局下游端口和全局路由器端口的老化时间。

**[undo ipv6 pim-snooping graceful-restart join-aging-time**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim-snooping graceful-restart join-aging-time** *interval*]

**[undo ipv6 pim-snooping graceful-restart join-aging-time**]

【缺省情况】

主备倒换期间新主用主控板上IPv6 PIM Snooping全局下游端口和全局路由器端口的老化时间为210秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示老化时间，取值范围为210～18000，单位为秒。

【使用指导】

·全局端口包括二层聚合接口、AC口、N-PW口、U-PW口等，由全局端口担任的下游端口和路由器端口分别称为全局下游端口和全局路由器端口。

·在配置本命令之前，必须先在VLAN/VSI内使能IPv6 PIM Snooping。

【举例】

\#在VLAN 2内配置主备倒换期间新主用主控板上IPv6 PIM Snooping全局下游端口和全局路由器端口的老化时间为600秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 ipv6 pim-snooping enable

Sysname-vlan2 ipv6 pim-snooping graceful-restart join-aging-time 300

\# 在VSI aaa内配置主备倒换期间新主用主控板上IPv6 PIM Snooping全局下游端口和全局路由器端口的老化时间为600秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa ipv6 pim-snooping enable

Sysname-vsi-aaa ipv6 pim-snooping graceful-restart join-aging-time 600

【相关命令】

·**ipv6 pim-snooping enable**

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- ipv6 pim-snooping graceful-restart neighbor-aging-time**

------------------------------------------------------------------------

![说明](IPv6%20PIM%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 pim-snooping graceful-restart neighbor-aging-time**]命令用来配置主备倒换期间新主用主控板上IPv6 PIM Snooping全局邻居端口的老化时间。

**[undo ipv6 pim-snooping graceful-restart neighbor-aging-time**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim-snooping graceful-restart neighbor-aging-time** *interval*]

**[undo ipv6 pim-snooping graceful-restart neighbor-aging-time**]

【缺省情况】

主备倒换期间新主用主控板上IPv6 PIM Snooping全局邻居端口老化时间为105秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示老化时间，取值范围为105～18000，单位为秒。

【使用指导】

·全局端口包括二层聚合接口、AC口、N-PW口、U-PW口等，由全局端口担任的邻居端口称为全局邻居端口。

·在配置本命令之前，必须先在VLAN/VSI内使能IPv6 PIM Snooping。

【举例】

\# 在VLAN 2内配置主备倒换期间新主用主控板上IPv6 PIM Snooping全局邻居端口的老化时间为300秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 ipv6 pim-snooping enable

Sysname-vlan2 ipv6 pim-snooping graceful-restart neighbor-aging-time 300

\# 在VSI aaa内配置主备倒换期间新主用主控板上IPv6 PIM Snooping全局邻居端口的老化时间为300秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa ipv6 pim-snooping enable

Sysname-vsi-aaa ipv6 pim-snooping graceful-restart neighbor-aging-time 300

【相关命令】

·**ipv6 pim-snooping enable**

**IPv6 PIM Snooping \-- IPv6 PIM Snooping命令 \-- reset ipv6 pim-snooping statistics**

------------------------------------------------------------------------

**[reset ipv6 pim-snooping statistics**]命令用来清除IPv6 PIM Snooping监听到的IPv6 PIM报文的统计信息。

【命令】

**[reset ipv6 pim-snooping statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除IPv6 PIM Snooping监听到的IPv6 PIM报文的统计信息。

\<Sysname\> reset ipv6 pim-snooping statistics

【相关命令】

·**display ipv6 pim-snooping statistics**
