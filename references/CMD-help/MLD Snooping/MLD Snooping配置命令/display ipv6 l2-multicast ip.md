<!-- CMD-INDEX
  display ipv6 l2-multicast ip        | 任意视图             | L55
  display ipv6 l2-multicast ip forwarding | 任意视图             | L235
  display ipv6 l2-multicast mac       | 任意视图             | L379
  display ipv6 l2-multicast mac forwarding | 任意视图             | L529
  display mld-snooping                | 任意视图             | L671
  display mld-snooping group          | 任意视图             | L901
  display mld-snooping router-port    | 任意视图             | L1101
  display mld-snooping static-group   | 任意视图             | L1253
  display mld-snooping static-router-port | 任意视图             | L1387
  display mld-snooping statistics     | 任意视图             | L1479
  dot1p-priority (MLD-Snooping view)  | MLD-Snooping视图   | L1571
  drop-unknown (MLD-Snooping view)    | MLD-Snooping视图   | L1621
  enable (MLD-Snooping view)          | MLD-Snooping视图   | L1671
  entry-limit (MLD-Snooping view)     | MLD-Snooping视图   | L1725
  fast-leave (MLD-Snooping view)      | MLD-Snooping视图   | L1767
  group-policy (MLD-Snooping view)    | MLD-Snooping视图   | L1819
  host-aging-time (MLD-Snooping view) | MLD-Snooping视图   | L1885
  last-listener-query-interval (MLD-Snooping view) | MLD-Snooping视图   | L1935
  max-response-time (MLD-Snooping view) | MLD-Snooping视图   | L1985
  mld-snooping                        | 系统视图             | L2039
  mld-snooping done source-ip         | VLAN视图           | L2083
  mld-snooping dot1p-priority         | VLAN视图           | L2141
  mld-snooping drop-unknown           | VLAN视图/VSI视图     | L2203
  mld-snooping enable                 | VLAN视图/VSI视图     | L2279
  mld-snooping fast-leave             | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2345
  mld-snooping general-query source-ip | VLAN视图/VSI视图     | L2397
  mld-snooping group-limit            | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2471
  mld-snooping group-policy           | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2519
  mld-snooping host-aging-time        | VLAN视图/VSI视图     | L2585
  mld-snooping host-join              | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2661
  mld-snooping last-listener-query-interval | VLAN视图/VSI视图     | L2727
  mld-snooping max-response-time      | VLAN视图/VSI视图     | L2803
  mld-snooping overflow-replace       | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L2885
  mld-snooping querier                | VLAN视图/VSI视图     | L2937
  mld-snooping query-interval         | VLAN视图/VSI视图     | L3009
  mld-snooping report source-ip       | VLAN视图           | L3089
  mld-snooping router-aging-time      | VLAN视图/VSI视图     | L3147
  mld-snooping router-port-deny       | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3223
  mld-snooping source-deny            | 二层以太网接口视图        | L3265
  mld-snooping special-query source-ip | VLAN视图/VSI视图     | L3315
  mld-snooping static-group           | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3389
  mld-snooping static-router-port     | 二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图 | L3449
  mld-snooping version                | VLAN视图/VSI视图     | L3493
  overflow-replace (MLD-Snooping view) | MLD-Snooping视图   | L3569
  report-aggregation (MLD-Snooping view) | MLD-Snooping视图   | L3621
  reset mld-snooping group            | 用户视图             | L3659
  reset mld-snooping router-port      | 用户视图             | L3701
  reset mld-snooping statistics       | 用户视图             | L3739
  router-aging-time (MLD-Snooping view) | MLD-Snooping视图   | L3769
  source-deny (MLD-Snooping view)     | MLD-Snooping视图   | L3819
  version (MLD-Snooping view)         | MLD-Snooping视图   | L3873
-->

**MLD Snooping \-- MLD Snooping配置命令 \-- display ipv6 l2-multicast ip**

------------------------------------------------------------------------

**[display ipv6 l2-multicast ip**]命令用来显示IPv6二层组播的IP组播组信息。

【命令】

集中式设备：

**[display ipv6 l2-multicast ip **[[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 l2-multicast ip **[[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 l2-multicast ip **[[ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[group** *ipv6-group-address*]：显示指定IPv6组播组的信息。如果未指定本参数，将显示所有IPv6组播组的信息。

**[source*** ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN 2内IPv6二层组播的IP组播组信息。

\<Sysname\> display ipv6 l2-multicast ip vlan 2

Total 1 entries.

VLAN 2: Total 1 IP entries.

   (::, FF1E::101)

    Attribute: static, success

    Host slots (0 in total):

    Host ports (1 in total):

      GE1/0/1                             (S, SUC)

\# 显示VSI aaa内IPv6二层组播的IP组播组信息。

\<Sysname\> display ipv6 l2-multicast ip vsi aaa

Total 1 entries.

VSI aaa: Total 1 IP entries.

  (::, FF1E::101)

    Attribute: dynamic, success

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)         (D, SUC)

表1-1 display ipv6 l2-multicast ip命令显示信息描述表

字段

描述

Total 1 entries

表项总数

VLAN 2: Total 1 IP entries

VLAN 2内的表项总数

VSI aaa: Total 1 IP entries

VSI aaa内的表项总数

(::, FF1E::101)

（S，G）表项，::表示所有IPv6组播源

Attribute

表项属性，包括：

·dynamic：表示由动态协议创建的表项

·static：表示由静态协议创建的表项

·pim：表示由IPv6 PIM协议创建的表项

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

·P：表示IPv6 PIM端口

·K：表示从内核中获取的端口

·R：表示从（\*，\*）表项扩展的端口

·W：表示从（\*，G）表项扩展的端口

·SUC：表示处理成功

·F：表示处理失败

AC (VSI index 0, link ID 1)

AC（Attachment Circuit，接入电路）口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW（Network Pseudowire，网络侧伪线）口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW（User facing Pseudowire，用户侧伪线）口的VSI索引和链路标识符

**MLD Snooping \-- MLD Snooping配置命令 \-- display ipv6 l2-multicast ip forwarding**

------------------------------------------------------------------------

**[display ipv6 l2-multicast ip forwarding**]命令用来显示IPv6二层组播的IP转发表信息。

【命令】

集中式设备：

**[display ipv6 l2-multicast ip forwarding**[ [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 l2-multicast ip forwarding**[ [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 l2-multicast ip forwarding**[ [ **group** *ipv6-group-address* \| **source** *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[group** *ipv6-group-address*]：显示指定IPv6组播组的信息。如果未指定本参数，将显示所有IPv6组播组的信息。

**[source*** ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN 2内IPv6二层组播的IP转发表信息。

\<Sysname\> display ipv6 l2-multicast ip forwarding vlan 2

Total 1 entries.

VLAN 2: Total 1 IP entries.

   (::, FF1E::101)

    Host slots (0 in total):

    Host ports (3 in total):

      GE1/0/1

      GE1/0/2

      GE1/0/3

\# 显示VSI aaa内IPv6二层组播的IP转发表信息。

\<Sysname\> display ipv6 l2-multicast ip forwarding vsi aaa

Total 1 entries.

VSI aaa: Total 1 IP entries.

  (::, FF1E::101)

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)

表1-2 display ipv6 l2-multicast ip forwarding命令显示信息描述表

字段

描述

Total 1 entries

表项总数

VLAN 2: Total 1 IP entries

VLAN 2内的表项总数

VSI aaa: Total 1 IP entries

VSI aaa内的表项总数

(::, FF1E::101)

（S，G）表项，::表示所有IPv6组播源

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

**MLD Snooping \-- MLD Snooping配置命令 \-- display ipv6 l2-multicast mac**

------------------------------------------------------------------------

**[display ipv6 l2-multicast mac**]命令用来显示IPv6二层组播的MAC组播组信息。

【命令】

集中式设备：

**[display ipv6 l2-multicast mac **[ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 l2-multicast mac **[ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 l2-multicast mac **[ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

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

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN 2内IPv6二层组播的MAC组播组信息。

\<Sysname\> display ipv6 l2-multicast mac vlan 2

Total 1 MAC entries.

VLAN 2: Total 1 MAC entries.

  MAC group address: 3333-0000-0101

    Attribute: success

    Host slots (0 in total):

    Host ports (1 in total):

      GE1/0/1

\# 显示VSI aaa内IPv6二层组播的MAC组播组信息。

\<Sysname\> display ipv6 l2-multicast mac vsi aaa

Total 1 MAC entries.

VSI aaa: Total 1 MAC entries.

  MAC group address: 0100-5e01-0101

    Attribute: success

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)

表1-3 display ipv6 l2-multicast mac命令显示信息描述表

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

本字段的支持情况和具体描述与设备的型号有关，请以设备的实际情况为准：

·集中式设备：不支持本字段

·分布式设备－独立运行模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板的槽位号

·集中式IRF设备：除当前成员设备外，其它所有有成员端口的成员设备总数，以及各成员设备的编号

·分布式设备－IRF模式：除当前单板外，其它所有有成员端口的单板总数，以及各单板所在成员设备的编号和单板的槽位号

Host ports (1 in total)

成员端口及总数

AC (VSI index 0, link ID 1)

AC口的VSI索引和链路标识符

NPW (VSI index 0, link ID 1)

N-PW口的VSI索引和链路标识符

UPW (VSI index 0, link ID 1)

U-PW口的VSI索引和链路标识符

**MLD Snooping \-- MLD Snooping配置命令 \-- display ipv6 l2-multicast mac forwarding**

------------------------------------------------------------------------

**[display ipv6 l2-multicast mac forwarding**]命令用来显示IPv6二层组播的MAC转发表信息。

【命令】

集中式设备：

**[display ipv6 l2-multicast mac forwarding** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 l2-multicast mac forwarding** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 l2-multicast mac forwarding** [ *mac-address*  [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

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

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN 2内IPv6二层组播的MAC转发表信息。

\<Sysname\> display ipv6 l2-multicast mac forwarding vlan 2

Total 1 MAC entries.

VLAN 2: Total 1 MAC entries.

  MAC group address: 3333-0000-0101

    Host slots (0 in total):

    Host ports (3 in total):

      GE1/0/1

      GE1/0/2

      GE1/0/3

\# 显示VSI aaa内IPv6二层组播的MAC转发表信息。

\<Sysname\> display ipv6 l2-multicast mac forwarding vsi aaa

Total 1 MAC entries.

VSI aaa: Total 1 MAC entries.

  MAC group address: 0100-5e01-0101

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)

表1-4 display ipv6 l2-multicast mac forwarding命令显示信息描述表

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

Host slots (1 in total)

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

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping**

------------------------------------------------------------------------

**[display** **mld-snooping**]命令用来显示MLD Snooping的状态信息。

【命令】

**[display**[ **mld-snooping** [ **global** \| **vlan** *vlan-id* \| **vsi** *vsi-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示MLD Snooping的全局状态信息。

**[vlan** *vlan-id*]：显示MLD Snooping在指定VLAN内的状态信息。*vlan-id*为VLAN的编号，取值范围为1～4094。

**[vsi** *vsi-name*]：显示MLD Snooping在指定VSI内的状态信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

如果未指定任何可选参数，将显示MLD Snooping在全局以及所有VLAN和VSI内的状态信息。

【举例】

\# 显示MLD Snooping在全局以及所有VLAN和VSI内的状态信息。

\<Sysname\> display mld-snooping

MLD snooping information: Global

 MLD snooping: Enabled

 Drop-unknown: Disabled

 Host-aging-time: 260s

 Router-aging-time: 260s

 Max-response-time: 10s

 Last-listener-query-interval: 1s

 Report-aggregation: Enabled

 Dot1p-priority: \--

MLD snooping information: VLAN 1

 MLD snooping: Enabled

 Drop-unknown: Disabled

 Version: 1

 Host-aging-time: 260s

 Router-aging-time: 260s

 Max-response-time: 10s

 Last-listener-query-interval: 1s

 Querier: Disabled

 Query-interval: 125s

 General-query source IP: FE80::2FF:FFFF:FE00:1

 Special-query source IP: FE80::2FF:FFFF:FE00:1

 Report source IP: FE80::2FF:FFFF:FE00:2

 Done source IP: FE80::2FF:FFFF:FE00:3

 Dot1p-priority: 2

MLD snooping information: VLAN 10

 MLD snooping: Enabled

 Drop-unknown: Enabled

 Version: 2

 Host-aging-time: 260s

 Router-aging-time: 260s

 Max-response-time: 10s

 Last-listener-query-interval: 1s

 Querier: Disabled

 Query-interval: 125s

 General-query source IP: FE80::2FF:FFFF:FE00:1

 Special-query source IP: FE80::2FF:FFFF:FE00:1

 Report source IP: FE80::2FF:FFFF:FE00:2

 Done source IP: FE80::2FF:FFFF:FE00:3

 Dot1p-priority: \--

MLD snooping information: VSI aaa

 MLD snooping: Enabled

 Drop-unknown: Enabled

 Version: 1

 Host-aging-time: 260s

 Router-aging-time: 260s

 Max-response-time: 10s

 Last-listener-query-interval: 1s

 Querier: Disabled

 Query-interval: 125s

 General-query source IP: FE80::2FF:FFFF:FE00:1

 Special-query source IP: FE80::2FF:FFFF:FE00:1

表1-5 display mld-snooping命令显示信息描述表

字段

描述

MLD snooping information

MLD Snooping的状态信息

MLD snooping

MLD Snooping的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

Drop-unknown

丢弃未知组播数据报文功能的使能状态（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）：

·Enabled：表示已使能

·Disabled：表示未使能

Version

MLD Snooping的版本

Host-aging-time

动态成员端口的老化时间

Router-aging-time

动态路由器端口老化时间

Max-response-time

MLD普遍组查询的最大响应时间

Last-listener-query-interval

MLD特定组查询报文的发送间隔

Report-aggregation

MLD成员关系报告报文抑制功能的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

Dot1p-priority

MLD报文的802.1p优先级，"\--"表示没有配置

Querier

MLD Snooping查询器的使能状态：

·Enabled：表示已使能

·Disabled：表示未使能

Query-interval

MLD普遍组查询报文的发送间隔

General-query source IP

MLD普遍组查询报文的源IPv6地址

Special-query source IP

MLD特定组查询报文的源IPv6地址

Report source IP

MLD成员关系报告报文的源IPv6地址

Done source IP

MLD离开组报文的源IPv6地址

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping group**

------------------------------------------------------------------------

**[display mld-snooping group**]命令用来显示动态MLD Snooping转发表的信息。

【命令】

集中式设备：

**[display mld-snooping**]{.TableTextChar}**group**[[ *ipv6-group-address* \| *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **verbose**   **cpu** *cpu-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display mld-snooping**]{.TableTextChar}**group**[[ *ipv6-group-address* \| *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display mld-snooping**]{.TableTextChar}**group**[[ *ipv6-group-address* \| *ipv6-source-address* ] \* [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]  **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

*[ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[vsi** *vsi-name*]：显示指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VSI内的信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示简要信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN 2内动态MLD Snooping转发表的详细信息。

\<Sysname\> display mld-snooping group vlan 2 verbose

Total 1 entries.

VLAN 2: Total 1 entries.

  (::,FF1E::101)

    Attribute: local port

    FSM information: normal

    Host slots (0 in total):

    Host ports (1 in total):

      GE1/0/2                             (00:03:23)

\# 显示VSI aaa内动态MLD Snooping转发表的详细信息。

\<Sysname\> display mld-snooping group vsi aaa verbose

Total 1 entries.

VSI aaa: Total 1 entries.

  (::,FF1E::101)

    Attribute: global port

    FSM information: normal

    Host slots (0 in total):

    Host ports (1 in total):

      AC (VSI index 0, link ID 1)         (00:03:35)

        VLAN pairs (1 in total):

          Out VLAN 5     In VLAN 2        (00:03:35)

表1-6 display mld-snooping group命令显示信息描述表

字段

描述

Total 1 entries

表项总数

VLAN 2: Total 1 entries

VLAN 2内的表项总数

VSI aaa: Total 1 entries

VSI aaa内的表项总数

(::，FF1E::101)

（S，G）表项，::表示所有IPv6组播源

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

(00:03:23)

成员端口的老化剩余时间。需要注意的是，本字段对于全局口（包括二层聚合接口、AC口、N-PW口、U-PW口等）将无条件显示，而对于非全局口：

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

VLAN对及总数

Out VLAN 5, in VLAN 2

外层VLAN为5，内层VLAN为2

【相关命令】

·**reset mld-snooping group**

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping router-port**

------------------------------------------------------------------------

**[display mld-snooping router-port**]命令用来显示IPv6动态路由器端口的信息。

【命令】

集中式设备：

**[display mld-snooping**]{.TableTextChar}**router-port**[ [ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* [ **verbose** ] ]  **cpu** *cpu-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display mld-snooping**]{.TableTextChar}**router-port**[ [ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* [ **verbose** ] ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display mld-snooping**]{.TableTextChar}**router-port**[ [ **verbose** \| **vlan** *vlan-id* \| **vsi** *vsi-name* [ **verbose** ] ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

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

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN 2内IPv6动态路由器端口的信息。

\<Sysname\> display mld-snooping router-port vlan 2

VLAN 2:

  Router slots (0 in total):

  Router ports (2 in total):

    GE1/0/1                             (00:01:30)

    GE1/0/2                             (00:00:23)

\# 显示VSI aaa内IPv6动态路由器端口的详细信息。

\<Sysname\> display mld-snooping router-port vsi aaa verbose

VSI aaa:

  Router slots (0 in total):

  Router ports (1 in total):

    AC (VSI index 0, link ID 1)         (00:03:35)

      VLAN pairs (1 in total):

        Out VLAN 5     In VLAN 2        (00:03:35)

表1-7 display mld-snooping router-port命令显示信息描述表

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

·在分布式设备－独立运行模式上，若该口属于主控板，会显示；否则须指定其所在单板的槽位号（才会显示

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

·**reset mld-snooping router-port**

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping static-group**

------------------------------------------------------------------------

**[display mld-snooping static**]-{.TableTextChar}**group**命令用来显示静态MLD Snooping转发表的信息。

【命令】

集中式设备：

**[display mld-snooping**]{.TableTextChar}**static**-{.TableTextChar}**group**[[ *ipv6-group-address* \| *ipv6-source-address* ] \*  **vlan** *vlan-id*   **verbose**   **cpu** *cpu-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display mld-snooping**]{.TableTextChar}**static**-{.TableTextChar}**group**[[ *ipv6-group-address* \| *ipv6-source-address* ] \*  **vlan** *vlan-id*   **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display mld-snooping**]{.TableTextChar}**static**-{.TableTextChar}**group**[[ *ipv6-group-address* \| *ipv6-source-address* ] \*  **vlan** *vlan-id*   **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

*[ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示简要信息。

**[slot*** slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上维护的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上维护的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上维护的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN 2内静态MLD Snooping转发表的详细信息。

\<Sysname\> display mld-snooping static-group vlan 2 verbose

Total 1 entries.

VLAN 2: Total 1 entries.

  (::,FF1E::101)

    Attribute: local port

    FSM information: normal

    Host slots (0 in total):

    Host ports (1 in total):

      GE1/0/2

表1-8 display mld-snooping static-group命令显示信息描述表

字段

描述

Total 1 entries

表项总数

VLAN 2: Total 1 entries

VLAN 2内的表项总数

(::，FF1E::101)

（S，G）表项，::表示所有IPv6组播源

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

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping static-router-port**

------------------------------------------------------------------------

**[display mld-snooping static-router-port**]命令用来显示IPv6静态路由器端口的信息。

【命令】

集中式设备：

**[display mld-snooping**]{.TableTextChar}**static-router-port** [ **vlan** *vlan-id*   **cpu** *cpu-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display mld-snooping**]{.TableTextChar}**static-router-port** [ **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display mld-snooping**]{.TableTextChar}**static-router-port** [ **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

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

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN 2内IPv6静态路由器端口的信息。

\<Sysname\> display mld-snooping static-router-port vlan 2

VLAN 2:

  Router slots (0 in total):

  Router ports (2 in total):

    GE1/0/1

    GE1/0/2

表1-9 display mld-snooping static-router-port命令显示信息描述表

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

**MLD Snooping \-- MLD Snooping配置命令 \-- display mld-snooping statistics**

------------------------------------------------------------------------

**[display** **mld**-**snooping** **statistics**]命令用来显示MLD Snooping监听到的MLD报文统计信息。

【命令】

**[display mld-snooping statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示MLD Snooping监听到的MLD报文统计信息。

\<Sysname\> display mld-snooping statistics

Received MLD general queries:  0

Received MLDv1 specific queries:  0

Received MLDv1 reports:  0

Received MLD dones:  0

Sent     MLDv1 specific queries:  0

Received MLDv2 reports:  0

Received MLDv2 reports with right and wrong records:  0

Received MLDv2 specific queries:  0

Received MLDv2 specific sg queries:  0

Sent     MLDv2 specific queries:  0

Sent     MLDv2 specific sg queries:  0

Received error MLD messages:  0

表1-10 display mld-snooping statistics命令显示信息描述表

字段

描述

general queries

MLD普遍组查询报文的数量

specific queries

MLD特定组查询报文的数量

reports

MLD成员关系报告报文的数量

dones

MLD离开组报文的数量

reports with right and wrong records

包含错误和正确纪录的MLD成员关系报告报文数量

specific sg queries

MLD特定源组查询报文的数量

error MLD messages

错误MLD报文的数量

【相关命令】

·**reset mld-snooping statistics**

**MLD Snooping \-- MLD Snooping配置命令 \-- dot1p-priority (MLD-Snooping view)**

------------------------------------------------------------------------

**[dot1p-priority**]命令用来全局配置MLD报文的802.1p优先级。

**[undo dot1p-priority**]命令用来恢复缺省情况。

【命令】

**[dot1p-priority ***priority-number*]

**[undo dot1p-priority**]

【缺省情况】

没有配置MLD报文的802.1p优先级。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-number*]：MLD报文的802.1p优先级，取值范围为0～7。该数值越大，优先级越高。

【使用指导】

对于基于VLAN的配置，本命令与**mld-snooping dot1p-priority**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN都有效，VLAN视图下的配置只对当前VLAN有效，后者的配置优先级较高；对于基于VSI的配置，MLD-Snooping视图下的全局配置对所有VSI都有效。

【举例】

\# 全局配置MLD报文的802.1p优先级为3。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping dot1p-priority 3

【相关命令】

·**mld-snooping dot1p-priority**

**MLD Snooping \-- MLD Snooping配置命令 \-- drop-unknown (MLD-Snooping view)**

------------------------------------------------------------------------

![说明](MLD%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[drop-unknown**]命令用来全局使能丢弃未知IPv6组播数据报文功能。

**[undo drop-unknown**]命令用来全局关闭丢弃未知IPv6组播数据报文功能。

【命令】

**[drop-unknown**]

**[undo drop-unknown**]

【缺省情况】

丢弃未知IPv6组播数据报文功能处于关闭状态，即对未知IPv6组播数据报文进行广播。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令与**mld-snooping drop-unknown**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效。

【举例】

\# 全局使能丢弃未知IPv6组播数据报文功能。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping drop-unknown

【相关命令】

·**mld-snooping drop-unknown**

**MLD Snooping \-- MLD Snooping配置命令 \-- enable (MLD-Snooping view)**

------------------------------------------------------------------------

**[enable**]命令用来使能指定VLAN内的MLD Snooping。

**[undo enable**]命令用来关闭指定VLAN内的MLD Snooping。

【命令】

**[enable** **vlan** *vlan-list*]

**[undo enable** **vlan** *vlan-list*]

【缺省情况】

VLAN内的MLD Snooping处于关闭状态。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·在使能VLAN内的MLD Snooping之前，必须先全局使能MLD Snooping。

·对于基于VLAN的配置，本命令与**mld-snooping enable**命令的功能相同，只是作用范围不同：MLD-Snooping视图下可以对指定VLAN进行配置，VLAN视图下只能对当前VLAN进行配置，二者的配置优先级相同。

【举例】

\# 全局使能MLD Snooping，并使能VLAN 2～10内的MLD Snooping。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping enable vlan 2 to 10

【相关命令】

·**mld-snooping**

·**mld-snooping**** enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- entry-limit (MLD-Snooping view)**

------------------------------------------------------------------------

**[entry-limit**]命令用来配置MLD Snooping转发表项（包括动态表项和静态表项）的全局最大数量。

**[undo entry-limit**]命令用来恢复缺省情况。

【命令】

**[entry-limit ***limit*]

**[undo entry-limit**]

【缺省情况】

MLD Snooping转发表项的全局最大数量为4294967295。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit*]：表示MLD Snooping转发表项的全局最大数量，取值范围为0～4294967295。

【举例】

\# 配置MLD Snooping转发表项的全局最大数量为512个。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping entry-limit 512

**MLD Snooping \-- MLD Snooping配置命令 \-- fast-leave (MLD-Snooping view)**

------------------------------------------------------------------------

**[fast-leave**]命令用来全局使能IPv6端口快速离开功能。

**[undo fast-leave**]命令用来全局关闭IPv6端口快速离开功能。

【命令】

**[fast-leave** [ **vlan** *vlan-list* ]]

**[undo fast-leave** [ **vlan** *vlan-list* ]]

【缺省情况】

IPv6端口快速离开功能处于关闭状态。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN和VSI进行配置。

【使用指导】

·IPv6端口快速离开是指当端口收到主机发来的离开指定IPv6组播组的MLD离开组报文时，直接将该端口从相应转发表项的出端口列表中删除。

·本命令与**mld-snooping fast-leave**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 全局使能VLAN 2内的IPv6端口快速离开功能。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping fast-leave vlan 2

【相关命令】

·**mld-snooping fast-leave**

**MLD Snooping \-- MLD Snooping配置命令 \-- group-policy (MLD-Snooping view)**

------------------------------------------------------------------------

**[group-policy**]命令用来全局配置IPv6组播组过滤器，以限定主机所能加入的IPv6组播组。

**[undo group-policy**]命令用来删除全局IPv6组播组过滤器。

【命令】

**[group-policy** *acl6-number* [ **vlan** *vlan-list* ]]

**[undo group-policy** [ **vlan** *vlan-list* ]]

【缺省情况】

没有配置IPv6组播组过滤器，即主机可以加入任意合法的IPv6组播组。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本或高级ACL的编号，取值范围为2000～3999。主机只能加入该ACL规则所允许的IPv6组播组。当指定的ACL不存在或ACL中未配置有效规则，将过滤掉所有IPv6组播组。

**[vlan **]*vlan-list*：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN和VSI进行配置。

【使用指导】

·对于IPv6基本ACL，该ACL规则中的**source**参数用来指定MLD报文中的IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv6高级ACL，该ACL规则中的**source**参数用来指定MLD报文中的IPv6组播源地址（对于MLDv1报文和未携带IPv6组播源地址的IS_EX/TO_EX类型的MLDv2报文，视其IPv6组播源地址为0::0）范围，**destination**参数用来指定IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·可以为端口在不同的VLAN内配置不同的ACL规则，但在相同VLAN内所配置的新规则会取代旧规则。

·本命令只对IPv6动态组播组有效，对IPv6静态组播组无效。

·本命令与**mld-snooping group-policy**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 全局配置IPv6组播组过滤器，以限定VLAN 2内的主机只能加入IPv6组播组FF03::101。

\<Sysname\> system-view

Sysname acl ipv6 basic 2000

Sysname-acl-ipv6-basic-2000 rule permit source ff03::101 128

Sysname-acl-ipv6-basic-2000 quit

Sysname mld-snooping

Sysname-mld-snooping group-policy 2000 vlan 2

【相关命令】

·**mld-snooping ****group-policy**

**MLD Snooping \-- MLD Snooping配置命令 \-- host-aging-time (MLD-Snooping view)**

------------------------------------------------------------------------

**[host-aging-time**]命令用来全局配置IPv6动态成员端口的老化时间。

**[undo host-aging-time**]命令用来恢复缺省情况。

【命令】

**[host-aging-time** *interval*]

**[undo host-aging-time**]

【缺省情况】

IPv6动态成员端口的老化时间为260秒。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IPv6动态成员端口的老化时间，取值范围为200～1000，单位为秒。

【使用指导】

本命令与**mld-snooping host-aging-time**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 全局配置IPv6动态成员端口的老化时间为300秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping host-aging-time 300

【相关命令】

·**mld-snooping host-aging-time**

**MLD Snooping \-- MLD Snooping配置命令 \-- last-listener-query-interval (MLD-Snooping view)**

------------------------------------------------------------------------

**[last-listener-query-interval**]命令用来全局配置MLD特定组查询报文的发送间隔。

**[undo last-listener-query-interval**]命令用来恢复缺省情况。

【命令】

**[last-listener-query-interval ***interval*]

**[undo last-listener-query-interval**]

【缺省情况】

MLD特定组查询报文的发送间隔为1秒。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示MLD特定组查询报文的发送间隔，取值范围为1～5，单位为秒。

【使用指导】

本命令与**mld-snooping last-listener-query-interval**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 全局配置MLD特定组查询报文的发送间隔为3秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping last-listener-query-interval 3

【相关命令】

·**mld-snooping** **last-listener-query-interval**

**MLD Snooping \-- MLD Snooping配置命令 \-- max-response-time (MLD-Snooping view)**

------------------------------------------------------------------------

**[max-response-time**]命令用来全局配置MLD普遍组查询的最大响应时间。

**[undo max-response-time**]命令用来恢复缺省情况。

【命令】

**[max-response-time** *interval*]

**[undo max-response-time**]

【缺省情况】

MLD普遍组查询的最大响应时间为10秒。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示MLD普遍组查询的最大响应时间，取值范围为1～25，单位为秒。

【使用指导】

·为避免误删IPv6组播组成员，请确保MLD普遍组查询的最大响应时间小于MLD普遍组查询报文的发送间隔，否则配置虽能生效但系统会给出提示。

·本命令与**mld-snooping max-response-time**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 全局配置MLD普遍组查询的最大响应时间为5秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping max-response-time 5

【相关命令】

·**mld-snooping max-response-time**

·**mld-snooping query-interval**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping**

------------------------------------------------------------------------

**[mld-snooping**]命令用来全局使能MLD Snooping，并进入MLD-Snooping视图。

**[undo mld-snooping**]命令用来全局关闭MLD Snooping。

【命令】

**[mld-snooping**]

**[undo mld-snooping**]

【缺省情况】

MLD Snooping处于全局关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 全局使能MLD Snooping，并进入MLD-Snooping视图。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping done source-ip**

------------------------------------------------------------------------

**[mld-snooping done source-ip**]命令用来配置MLD离开组报文的源IPv6地址。

**[undo mld-snooping done source-ip**]命令用来恢复缺省情况。

【命令】

**[mld-snooping done source-ip** *ipv6-address*]

**[undo mld-snooping done source-ip**]

【缺省情况】

MLD离开组报文的源IPv6地址为当前VLAN接口的IPv6链路本地地址；若当前VLAN接口没有IPv6链路本地地址，则采用FE80::02FF:FFFF:FE00:0001。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：表示MLD离开组报文的源IPv6地址。

【使用指导】

在配置本命令之前，必须先在VLAN内使能MLD Snooping。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置MLD离开组报文的源IPv6地址为FE80:0:0:1::1。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping done source-ip fe80:0:0:1::1

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping dot1p-priority**

------------------------------------------------------------------------

**[mld-snooping dot1p-priority**]命令用来在VLAN内配置MLD报文的802.1p优先级。

**[undo mld-snooping dot1p-priority**]命令用来恢复缺省情况。

【命令】

**[mld-snooping dot1p-priority ***priority-number*]

**[undo mld-snooping dot1p-priority**]

【缺省情况】

没有配置MLD报文的802.1p优先级。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-number*]：MLD报文的802.1p优先级，取值范围为0～7。该数值越大，优先级越高。

【使用指导】

·在配置本命令之前，必须先在VLAN内使能MLD Snooping。

·对于基于VLAN的配置，本命令与**dot1p-priority**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN都有效，VLAN视图下的配置只对当前VLAN有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置MLD报文的802.1p优先级为3。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping dot1p-priority 3

【相关命令】

·**dot1p-priority** (MLD-Snooping view)

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping drop-unknown**

------------------------------------------------------------------------

![说明](MLD%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mld-snooping drop-unknown**]命令用来在VLAN/VSI内使能丢弃未知IPv6组播数据报文功能。

**[undo mld-snooping drop-unknown**]命令用来在VLAN/VSI内关闭丢弃未知IPv6组播数据报文功能。

【命令】

**[mld-snooping drop-unknown**]

**[undo mld-snooping drop-unknown**]

【缺省情况】

丢弃未知IPv6组播数据报文功能处于关闭状态，即对未知IPv6组播数据报文进行广播。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

·本命令与**drop-unknown**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能MLD Snooping，并使能丢弃未知IPv6组播数据报文功能。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping drop-unknown

\# 在VSI aaa内使能MLD Snooping，并使能丢弃未知IPv6组播数据报文功能。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping drop-unknown

【相关命令】

·**drop-unknown** (MLD-Snooping view)

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping enable**

------------------------------------------------------------------------

**[mld-snooping enable**]命令用来在VLAN/VSI内使能MLD Snooping。

**[undo mld-snooping enable**]命令用来在VLAN/VSI内关闭MLD Snooping。

【命令】

**[mld-snooping enable**]

**[undo mld-snooping enable**]

【缺省情况】

VLAN/VSI内的MLD Snooping处于关闭状态。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在VLAN/VSI内使能MLD Snooping之前，必须先全局使能MLD Snooping。

·对于基于VLAN的配置，本命令与**enable**命令的功能相同，只是作用范围不同：MLD-Snooping视图下可以对指定VLAN进行配置，VLAN视图下只能对当前VLAN进行配置，二者的配置优先级相同。

【举例】

\# 全局使能MLD Snooping，并在VLAN 2内使能MLD Snooping。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

\# 全局使能MLD Snooping，并在VSI aaa内使能MLD Snooping。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping fast-leave**

------------------------------------------------------------------------

**[mld-snooping fast-leave**]命令用来在端口上使能IPv6端口快速离开功能。

**[undo** **mld-snooping fast-leave**]命令用来在端口上关闭IPv6端口快速离开功能。

【命令】

**[mld-snooping fast-leave** [ **vlan** *vlan-list* ]]

**[undo mld-snooping fast-leave** [ **vlan** *vlan-list* ]]

【缺省情况】

IPv6端口快速离开功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

·IPv6端口快速离开是指当端口收到主机发来的离开指定IPv6组播组的MLD离开组报文时，直接将该端口从相应转发表项的出端口列表中删除。

·本命令与**fast-leave**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 将端口GigabitEthernet1/0/1在VLAN 2内使能IPv6端口快速离开功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld-snooping fast-leave vlan 2

【相关命令】

·**fast-leave** (MLD-Snooping view)

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping general-query source-ip**

------------------------------------------------------------------------

**[mld-snooping general-query source-ip**]命令用来配置MLD普遍组查询报文的源IPv6地址。

**[undo mld-snooping general-query source-ip**]命令用来恢复缺省情况。

【命令】

**[mld-snooping general-query source-ip** *ipv6-address*]

**[undo mld-snooping general-query source-ip**]

【缺省情况】

·在VLAN内，MLD普遍组查询报文的源IPv6地址为当前VLAN接口的IPv6链路本地地址；若当前VLAN接口没有IPv6链路本地地址，则采用FE80::02FF:FFFF:FE00:0001。

·在VSI内，MLD普遍组查询报文的源IPv6地址为FE80::02FF:FFFF:FE00:0001。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：表示MLD普遍组查询报文的源IPv6地址。

【使用指导】

在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置MLD普遍组查询报文的源IPv6地址为FE80:0:0:1::1。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping general-query source-ip fe80:0:0:1::1

\# 在VSI aaa内使能MLD Snooping，并配置MLD普遍组查询报文的源IPv6地址为FE80:0:0:1::1。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping general-query source-ip fe80:0:0:1::1

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping group-limit**

------------------------------------------------------------------------

**[mld-snooping group-limit**]命令用来[配置端口加入的]IPv6组播组最大数量。

**[undo **]**mld-snooping group-limit**命令用来恢复缺省情况。

【命令】

**[mld-snooping group-limit** *limit* [ **vlan** *vlan-list* ]]

**[undo mld-snooping group-limit** [ **vlan** *vlan-list* ]]

【缺省情况】

端口加入的IPv6组播组最大数量为4294967295。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit*]：表示端口加入的IPv6组播组最大数量，取值范围为0～4294967295。

**[vlan ***vlan-list*]：表示表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

本命令只对IPv6动态组播组有效，对IPv6静态组播组无效。

【举例】

\# 配置端口GigabitEthernet1/0/1在VLAN 2内加入的IPv6组播组最大数量为10个。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld-snooping group-limit 10 vlan 2

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping group-policy**

------------------------------------------------------------------------

**[mld-snooping group-policy**]命令用来[在端口上配置]IPv6组播组过滤器，以限定主机所能加入的IPv6组播组。

**[undo **]**mld-snooping group-policy**命令用来删除端口上的IPv6组播组过滤器。

【命令】

**[mld-snooping group-policy** *acl6-number* [ **vlan** *vlan-list* ]]

**[undo mld-snooping group-policy** [ **vlan** *vlan-list* ]]

【缺省情况】

没有配置IPv6组播组过滤器，即主机可以加入任意合法的IPv6组播组。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本或高级ACL的编号，取值范围为2000～3999。主机只能加入该ACL规则所允许的IPv6组播组。当指定的ACL不存在或ACL中未配置有效规则，将过滤掉所有IPv6组播组。

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

·对于IPv6基本ACL，该ACL规则中的**source**参数用来指定MLD报文中的IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv6高级ACL，该ACL规则中的**source**参数用来指定MLD报文中的IPv6组播源地址（对于MLDv1报文和未携带IPv6组播源地址的IS_EX/TO_EX类型的MLDv2报文，视其IPv6组播源地址为0::0）范围，**destination**参数用来指定IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·可以为端口在不同的VLAN内配置不同的ACL规则，但在相同VLAN内所配置的新规则会取代旧规则。

·本命令只对IPv6动态组播组有效，对IPv6静态组播组无效。

·本命令与**group-policy**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 在端口GigabitEthernet1/0/1上配置IPv6组播组过滤器，以限定端口GigabitEthernet1/0/1下VLAN 2内的主机只能加入IPv6组播组FF03::101。

\<Sysname\> system-view

Sysname acl ipv6 basic 2000

Sysname-acl-ipv6-basic-2000 rule permit source ff03::101 128

Sysname-acl-ipv6-basic-2000 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld-snooping group-policy 2000 vlan 2

【相关命令】

·**group-policy** (MLD-Snooping view)

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping host-aging-time**

------------------------------------------------------------------------

**[mld-snooping host-aging-time**]命令用来在VLAN/VSI内配置IPv6动态成员端口的老化时间。

**[undo mld-snooping host-aging-time**]命令用来恢复缺省情况。

【命令】

**[mld-snooping host-aging-time** *interval*]

**[undo mld-snooping host-aging-time**]

【缺省情况】

IPv6动态成员端口的老化时间为260秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IPv6动态成员端口的老化时间，取值范围为200～1000，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

·本命令与**host-aging-time**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置IPv6动态成员端口的老化时间为300秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping host-aging-time 300

\# 在VSI aaa内使能MLD Snooping，并配置IPv6动态成员端口的老化时间为300秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping host-aging-time 300

【相关命令】

·**enable** (MLD-Snooping view)

·**host-aging-time** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping host-join**

------------------------------------------------------------------------

**[mld-snoopinghost-join**]命令用来[配置模拟主机加入]IPv6组播组或IPv6组播源组。模拟主机加入就是将二层设备的端口配置为IPv6组播组的成员。

**[undo **]**mld-snoopinghost-join**命令用来删除模拟主机加入的配置。

【命令】

**[mld-snoopinghost-join ***ipv6-group-address* [ **source-ip** *ipv6-source-address*  **vlan** *vlan-id*]]

**[undo **]**mld-snoopinghost-join** { *ipv6-group-address* [ **source-ip** *ipv6-source-address*  **vlan** *vlan-id* \| **all** }]

【缺省情况】

没有配置模拟主机加入IPv6组播组或IPv6组播源组。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-group-address*]：表示模拟主机要加入的IPv6组播组的地址，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。

**[source-ip ***ipv6-source-address*]：表示模拟主机要加入的IPv6组播源的地址。如果指定了本参数，表示加入IPv6组播源组；如果未指定本参数，则表示加入IPv6组播组。配置有本参数的模拟主机，只在MLD Snooping版本2下生效。

**[vlan** *vlan-id*]：表示对指定VLAN进行配置。*vlan-id*为VLAN的编号，取值范围为1～4094。

**[all**]：表示对所有IPv6组播组和IPv6组播源组进行配置。

【使用指导】

·与静态成员端口不同，配置了模拟主机加入的端口将作为动态成员端口参与动态成员端口的老化过程。

·模拟主机所采用的MLD版本与MLD Snooping的版本一致。

【举例】

\# 在端口GigabitEthernet1/0/1上配置模拟主机加入VLAN 2内的IPv6组播源组（2002::22，FF3E::101）。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping version 2

Sysname-vlan2 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld-snooping host-join ff3e::101 source-ip 2002::22 vlan 2

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping last-listener-query-interval**

------------------------------------------------------------------------

**[mld-snooping last-listener-query-interval**]命令用来在VLAN/VSI内配置MLD特定组查询报文的发送间隔。

**[undo mld-snooping last-listener-query-interval**]命令用来恢复缺省情况。

【命令】

**[mld-snooping last-listener-query-interval ***interval*]

**[undo mld-snooping last-listener-query-interval**]

【缺省情况】

MLD特定组查询报文的发送间隔为1秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示MLD特定组查询报文的发送间隔，取值范围为1～5，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

·本命令与**last-listener-query-interval**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置MLD特定组查询报文的发送间隔为3秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping last-listener-query-interval 3

\# 在VSI aaa内使能MLD Snooping，并配置MLD特定组查询报文的发送间隔为3秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping last-listener-query-interval 3

【相关命令】

·**enable** (MLD-Snooping view)

·**last-listener-query-interval** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping max-response-time**

------------------------------------------------------------------------

**[mld-snooping max-response-time**]命令用来在VLAN/VSI内配置MLD普遍组查询的最大响应时间。

**[undo mld-snooping max-response-time**]命令用来恢复缺省情况。

【命令】

**[mld-snooping max-response-time** *interval*]

**[undo mld-snooping max-response-time**]

【缺省情况】

MLD普遍组查询的最大响应时间为10秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示MLD普遍组查询的最大响应时间，取值范围为1～25，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

·VLAN上的配置只对当前VLAN有效，但配置优先级高于全局配置。

·为避免误删IPv6组播组成员，请确保MLD普遍组查询的最大响应时间小于MLD普遍组查询报文的发送间隔，否则配置虽能生效但系统会给出提示。

·本命令与**max-response-time**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置MLD普遍组查询的最大响应时间为5秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping max-response-time 5

\# 在VSI aaa内使能MLD Snooping，并配置MLD普遍组查询的最大响应时间为5秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping max-response-time 5

【相关命令】

·**enable** (MLD-Snooping view)

·**max-response-time** (MLD-Snooping view)

·**mld-snooping enable**

·**mld-snooping query-interval**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping overflow-replace**

------------------------------------------------------------------------

**[mld-snooping overflow-replace**]命令用来在端口上使能IPv6组播组替换功能。

**[undo **]**mld-snooping overflow-replace**命令用来在端口上关闭IPv6组播组替换功能。

【命令】

**[mld-snooping overflow-replace** [ **vlan** *vlan-list* ]]

**[undo mld-snooping overflow-replace** [ **vlan** *vlan-list* ]]

【缺省情况】

IPv6组播组替换功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

·本命令只对IPv6动态组播组有效，对IPv6静态组播组无效。

·本命令与**overflow-replace**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 将端口GigabitEthernet1/0/1在VLAN2内使能IPv6组播组替换功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld-snooping overflow-replace vlan 2

【相关命令】

·**overflow-replace** (MLD-Snooping view)

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping querier**

------------------------------------------------------------------------

**[mld-snooping querier**]命令用来使能MLD Snooping查询器。

**[undo mld-snooping querier**]命令用来关闭MLD Snooping查询器。

【命令】

**[mld-snooping querier**]

**[undo mld-snooping querier**]

【缺省情况】

MLD Snooping查询器处于关闭状态。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

·如果在IPv6组播VLAN的子VLAN内配置了本命令，只有当该子VLAN被从IPv6组播VLAN中删除后，MLD Snooping查询器才会生效。

【举例】

\# 在VLAN 2内使能MLD Snooping，并使能MLD Snooping查询器。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping querier

\# 在VSI aaa内使能MLD Snooping，并使能MLD Snooping查询器。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping querier

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

·**subvlan** (IPv6 multicast-VLAN view)（IP组播命令参考/IPv6组播VLAN）

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping query-interval**

------------------------------------------------------------------------

**[mld-snooping query-interval**]命令用来在VLAN/VSI内配置MLD普遍组查询报文的发送间隔。

**[undo mld-snooping query-interval**]命令用来恢复缺省情况。

【命令】

**[mld-snooping query-interval** *interval*]

**[undo mld-snooping query-interval**]

【缺省情况】

MLD普遍组查询报文的发送间隔为125秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示MLD普遍组查询报文的发送间隔，取值范围为2～300，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

·为避免误删IPv6组播组成员，请确保MLD普遍组查询报文的发送间隔大于MLD普遍组查询的最大响应时间，否则配置虽能生效但系统会给出提示。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置MLD普遍组查询报文的发送间隔为20秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping query-interval 20

\# 在VSI aaa内使能MLD Snooping，并配置MLD普遍组查询报文的发送间隔为20秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping query-interval 20

【相关命令】

·**enable** (MLD-Snooping view)

·**max-response-time**

·**mld-snooping enable**

·**mld-snooping max-response-time**

·**mld-snooping querier**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping report source-ip**

------------------------------------------------------------------------

**[mld-snooping report source-ip**]命令用来配置MLD成员关系报告报文的源IPv6地址。

**[undo mld-snooping report source-ip**]命令用来恢复缺省情况。

【命令】

**[mld-snooping report source-ip** *ipv6-address*]

**[undo mld-snooping report source-ip**]

【缺省情况】

MLD成员关系报告报文的源IPv6地址为当前VLAN接口的IPv6链路本地地址；若当前VLAN接口没有IPv6链路本地地址，则采用FE80::02FF:FFFF:FE00:0001。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：表示MLD成员关系报告报文的源IPv6地址。

【使用指导】

在配置本命令之前，必须先在VLAN内使能MLD Snooping。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置MLD成员关系报告报文的源IPv6地址为FE80:0:0:1::1。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping report source-ip fe80:0:0:1::1

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping router-aging-time**

------------------------------------------------------------------------

**[mld-snooping router-aging-time**]命令用来在VLAN/VSI内配置IPv6动态路由器端口的老化时间。

**[undo mld-snooping router-aging-time**]命令用来恢复缺省情况。

【命令】

**[mld-snooping router-aging-time** *interval*]

**[undo mld-snooping router-aging-time**]

【缺省情况】

IPv6动态路由器端口的老化时间为260秒。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IPv6动态路由器端口的老化时间，取值范围为1～1000，单位为秒。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

·本命令与**router-aging-time**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置IPv6动态路由器端口的老化时间为100秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping router-aging-time 100

\# 在VSI aaa内使能MLD Snooping，并配置IPv6动态路由器端口的老化时间为100秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping router-aging-time 100

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

·**router-aging-time** (MLD-Snooping view)

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping router-port-deny**

------------------------------------------------------------------------

**[mld-snooping router-port-deny**]命令用来禁止端口成为动态路由器端口。

**[undo mld-snooping router-port-deny**]命令用来恢复缺省情况。

【命令】

**[mld-snooping router-port-deny** [ **vlan** *vlan-list* ]]

**[undo mld-snooping router-port-deny** [ **vlan** *vlan-list* ]]

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

Sysname-GigabitEthernet1/0/1 mld-snooping router-port-deny vlan 2

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping source-deny**

------------------------------------------------------------------------

![说明](MLD%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mld-snooping source-deny**]命令用来使能当前端口的IPv6组播数据报文源端口过滤功能。

**[undo **]**mld-snooping source-deny**命令用来关闭当前端口的IPv6组播数据报文源端口过滤功能。

【命令】

**[mld-snoopingsource-deny**]

**[undo mld-snooping source-deny**]

【缺省情况】

IPv6组播数据报文源端口过滤功能处于关闭状态。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令与**source-deny**命令的功能相同，只是作用范围不同：MLD-Snooping视图下可以对指定端口进行配置，端口视图下只能对当前端口进行配置，二者的配置优先级相同。

【举例】

\# 在端口GigabitEthernet1/0/1上使能IPv6组播数据报文源端口过滤功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld-snooping source-deny

【相关命令】

·**source-deny** (MLD-Snooping view)

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping special-query source-ip**

------------------------------------------------------------------------

**[mld-snooping special-query source-ip**]命令用来配置MLD特定组查询报文的源IPv6地址。

**[undo mld-snooping special-query source-ip**]命令用来恢复缺省情况。

【命令】

**[mld-snooping special-query source-ip** *ipv6-address*]

**[undo mld-snooping special-query source-ip**]

【缺省情况】

·在VLAN内，如果收到过MLD普遍组查询报文，则以其源IPv6地址作为MLD特定组查询报文的源IPv6地址；否则，采用当前VLAN接口的IPv6链路本地地址；若当前VLAN接口没有IPv6链路本地地址，则采用FE80::02FF:FFFF:FE00:0001。

·在VSI内，如果收到过MLD普遍组查询报文，则以其源IPv6地址作为MLD特定组查询报文的源IPv6地址；否则，采用FE80::02FF:FFFF:FE00:0001。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：表示MLD特定组查询报文的源IPv6地址。

【使用指导】

在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置MLD特定组查询报文的源IPv6地址为FE80:0:0:1::1。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping special-query source-ip fe80:0:0:1::1

\# 在VSI aaa内使能MLD Snooping，并配置MLD特定组查询报文的源IPv6地址为FE80:0:0:1::1。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping special-query source-ip fe80:0:0:1::1

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping static-group**

------------------------------------------------------------------------

**[mld-snooping static-group**]命令用来配置IPv6静态成员端口，即配置端口静态加入IPv6组播组或IPv6组播源组。

**[undo **]**mld-snooping static-group**命令用来删除静态成员端口的配置。

【命令】

**[mld-snooping**] **static-group** *ipv6-group-address* [ **source-ip** *ipv6-source-address*  **vlan** *vlan-id*]

**[undo mld-snooping static-group** { *ipv6-group-address* [ **source-ip** *ipv6-source-address*  **vlan** *vlan-id* \| **all** }]]

【缺省情况】

端口不是IPv6静态成员端口。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-group-address*]：表示静态加入的IPv6组播组地址，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。

**[source-ip ***ipv6-source-address*]：表示静态加入的IPv6组播源地址。如果指定了本参数，表示加入IPv6组播源组；如果未指定本参数，则表示加入IPv6组播组。配置有本参数的静态成员端口，只在MLD Snooping版本2下生效。

**[vlan** *vlan-id*]：表示对指定VLAN进行配置。*vlan-id*为VLAN的编号，取值范围为1～4094。

**[all**]：表示对所有IPv6组播组和IPv6组播源组进行配置。

【举例】

\# 将端口GigabitEthernet1/0/1配置为IPv6组播源组（2002::22，FF3E::101）在VLAN 2内的静态成员端口。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping version 2

Sysname-vlan2 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld-snooping static-group ff3e::101 source-ip 2002::22 vlan 2

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping static-router-port**

------------------------------------------------------------------------

**[mld-snooping static-router-port**]命令用来配置IPv6静态路由器端口。

**[undo **]**mld-snooping static-router-port**命令用来删除静态路由器端口的配置。

【命令】

**[mld-snooping static-router-port vlan ***vlan-id*]

**[undo**[ **mld-snooping** **static-router-port** { **all** \| **vlan** *vlan-id* }]]

【缺省情况】

端口不是IPv6静态路由器端口。

【视图】

二层以太网接口视图/二层聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示对所有VLAN进行配置。

**[vlan** *vlan-id*]：表示对指定VLAN进行配置。*vlan-id*为VLAN的编号，取值范围为1～4094。

【举例】

\# 将端口GigabitEthernet1/0/1配置为VLAN 2内的IPv6静态路由器端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld-snooping static-router-port vlan 2

**MLD Snooping \-- MLD Snooping配置命令 \-- mld-snooping version**

------------------------------------------------------------------------

**[mld-snooping version**]命令用来在VLAN/VSI内配置MLD Snooping的版本。

**[undo mld-snooping version**]命令用来恢复缺省情况。

【命令】

**[mld-snooping version ***version-number*]

**[undo mld-snooping version**]

【缺省情况】

VLAN/VSI内MLD Snooping的版本为1。

【视图】

VLAN视图/VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[version-number*]：表示MLD Snooping的版本号，取值范围为1～2。

【使用指导】

·在配置本命令之前，必须先在VLAN/VSI内使能MLD Snooping。

·对于基于VLAN的配置，本命令与**version**命令的功能相同，只是作用范围不同：MLD-Snooping视图下可以对指定VLAN进行配置，VLAN视图下只能对当前VLAN进行配置，二者的配置优先级相同。

【举例】

\# 在VLAN 2内使能MLD Snooping，并配置该VLAN内的MLD Snooping版本为2。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 2

Sysname-vlan2 mld-snooping enable

Sysname-vlan2 mld-snooping version 2

\# 在VSI aaa内使能MLD Snooping，并配置该VSI内的MLD Snooping版本为2。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vsi aaa

Sysname-vsi-aaa mld-snooping enable

Sysname-vsi-aaa mld-snooping version 2

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

·**version** (MLD-Snooping view)

**MLD Snooping \-- MLD Snooping配置命令 \-- overflow-replace (MLD-Snooping view)**

------------------------------------------------------------------------

**[overflow-replace**]命令用来全局使能IPv6组播组替换功能。

**[undo overflow-replace**]命令用来全局关闭IPv6组播组替换功能。

【命令】

**[overflow-replace** [ **vlan** *vlan-list* ]]

**[undo overflow-replace** [ **vlan** *vlan-list* ]]

【缺省情况】

IPv6组播组替换功能处于关闭状态。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，则表示对所有VLAN进行配置。

【使用指导】

·本命令只对IPv6动态组播组有效，对IPv6静态组播组无效。

·本命令与**mld-snooping overflow-replace**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有端口都有效，端口视图下的配置只对当前端口有效，后者的配置优先级较高。

【举例】

\# 全局使能VLAN 2内的IPv6组播组替换功能。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping overflow-replace vlan 2

【相关命令】

·**mld-snooping overflow-replace**

**MLD Snooping \-- MLD Snooping配置命令 \-- report-aggregation (MLD-Snooping view)**

------------------------------------------------------------------------

**[report-aggregation**]命令用来使能MLD成员关系报告报文抑制功能。

**[undo report-aggregation**]命令用来关闭MLD成员关系报告报文抑制功能。

【命令】

**[report-aggregation**]

**[undo report-aggregation**]

【缺省情况】

MLD成员关系报告报文抑制功能处于使能状态。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭MLD成员关系报告报文抑制功能。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping undo report-aggregation

**MLD Snooping \-- MLD Snooping配置命令 \-- reset mld-snooping group**

------------------------------------------------------------------------

**[reset **]**mld-snooping group**命令用来清除动态MLD Snooping转发表的信息。

【命令】

**[reset mld-snooping group** { *ipv6-group-address* [ *ipv6-source-address*  \| **all** } [ **vlan** *vlan-id* \| **vsi** *vsi-name* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-group-address*]：清除指定IPv6组播组的信息，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。

*[ipv6-source-address*]：清除指定IPv6组播源的信息。如果未指定本参数，将清除所有IPv6组播源的信息。

**[all**]：清除所有IPv6组播组的信息。

**[vlan*** vlan-id*]：清除指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将清除所有VLAN内的信息。

**[vsi** *vsi-name*]：清除指定VSI内的信息。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除所有VSI内的信息。

【举例】

\# 清除所有动态MLD Snooping转发表的信息。

\<Sysname\> reset mld-snoopinggroup all

【相关命令】

·**display mld-snooping group**

**MLD Snooping \-- MLD Snooping配置命令 \-- reset mld-snooping router-port**

------------------------------------------------------------------------

**[reset **]**mld-snoopingrouter-port**命令用来清除IPv6动态路由器端口的信息。

【命令】

**[reset mld-snooping router-port**[ { **all** \| **vlan** *vlan-id* \| **vsi** *vsi-name* }]]

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

\# 清除所有IPv6动态路由器端口的信息。

\<Sysname\> reset mld-snoopingrouter-port all

【相关命令】

·**display mld-snooping router-port**

**MLD Snooping \-- MLD Snooping配置命令 \-- reset mld-snooping statistics**

------------------------------------------------------------------------

**[reset mld-snooping statistics**]命令用来清除MLD Snooping监听到的MLD报文统计信息。

【命令】

**[reset mld-snooping statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除MLD Snooping监听到的MLD报文的信息。

\<Sysname\> reset mld-snooping statistics

【相关命令】

·**display mld-snooping statistics**

**MLD Snooping \-- MLD Snooping配置命令 \-- router-aging-time (MLD-Snooping view)**

------------------------------------------------------------------------

**[router-aging-time**]命令用来全局配置IPv6动态路由器端口的老化时间。

**[undo router-aging-time**]命令用来恢复缺省情况。

【命令】

**[router-aging-time** *interval*]

**[undo router-aging-time**]

【缺省情况】

IPv6动态路由器端口的老化时间为260秒。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示IPv6动态路由器端口的老化时间，取值范围为1～1000，单位为秒。

【使用指导】

本命令与**mld-snooping router-aging-time**命令的功能相同，只是作用范围不同：MLD-Snooping视图下的全局配置对所有VLAN和VSI都有效，VLAN视图/VSI视图下的配置只对当前VLAN/VSI有效，后者的配置优先级较高。

【举例】

\# 全局配置IPv6动态路由器端口的老化时间为100秒。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping router-aging-time 100

【相关命令】

·**mld-snooping router-aging-time**

**MLD Snooping \-- MLD Snooping配置命令 \-- source-deny (MLD-Snooping view)**

------------------------------------------------------------------------

![说明](MLD%20Snooping命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-deny**]命令用来使能指定端口的IPv6组播数据报文源端口过滤功能。

**[undo source-deny**]命令用来关闭指定端口的IPv6组播数据报文源端口过滤功能。

【命令】

**[source-deny port** *interface-list*]

**[undo source-deny port** *interface-list*]

【缺省情况】

IPv6组播数据报文源端口过滤功能处于关闭状态。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[port** *interface-list*]：表示对指定端口进行配置。*interface-list*为端口列表，表示一或多个端口，表示方式为*interface-list* = { *interface-type* *interface-number* [ **to** *interface-type* *interface-number*  }]，其中，*interface-type*为接口类型，*interface-number*为接口编号。

【使用指导】

本命令与**mld-snooping source-deny**命令的功能相同，只是作用范围不同：MLD-Snooping视图下可以对指定端口进行配置，端口视图下只能对当前端口进行配置，二者的配置优先级相同。

【举例】

\# 使能端口GigabitEthernet1/0/1～GigabitEthernet1/0/4上的IPv6组播数据报文源端口过滤功能。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping source-deny port gigabitethernet 1/0/1 to gigabitethernet 1/0/4

【相关命令】

·**mld-snoopingsource-deny**

**MLD Snooping \-- MLD Snooping配置命令 \-- version (MLD-Snooping view)**

------------------------------------------------------------------------

**[version**]命令用来配置指定VLAN内的MLD Snooping的版本。

**[undo version**]命令用来恢复缺省情况。

【命令】

**[version ***version-number* **vlan** *vlan-list*]

**[undo version** **vlan** *vlan-list*]

【缺省情况】

VLAN内MLD Snooping的版本为1。

【视图】

MLD-Snooping视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[version-number*]：表示MLD Snooping的版本号，取值范围为1～2。

**[vlan ***vlan-list*]：表示对指定VLAN进行配置。*vlan-list*为VLAN列表，表示一或多个VLAN，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·在配置本命令之前，必须先在VLAN内使能MLD Snooping。

·对于基于VLAN的配置，本命令与**mld-snooping version**命令的功能相同，只是作用范围不同：MLD-Snooping视图下可以对指定VLAN进行配置，VLAN视图下只能对当前VLAN进行配置，二者的配置优先级相同。

【举例】

\# 使能VLAN 2～10内的MLD Snooping，并配置这些VLAN内的MLD Snooping版本为2。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping enable vlan 2 to 10

Sysname-mld-snooping version 2 vlan 2 to 10

【相关命令】

·**enable** (MLD-Snooping view)

·**mld-snooping enable**

·**mld-snooping**** version**

