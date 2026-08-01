<!-- CMD-INDEX
  display ipv6 multicast-vlan         | 任意视图             | L13
  display ipv6 multicast-vlan group   | 任意视图             | L91
  display ipv6 multicast-vlan forwarding-table | 任意视图             | L243
  ipv6 multicast-vlan                 | 系统视图             | L371
  ipv6 multicast-vlan entry-limit     | 系统视图             | L441
  ipv6 port multicast-vlan            | 以太网接口视图/二层聚合接口视图 | L489
  port (IPv6 multicast-VLAN view)     | IPv6组播VLAN视图     | L539
  reset ipv6 multicast-vlan group     | 用户视图             | L593
  subvlan (IPv6 multicast-VLAN view)  | IPv6组播VLAN视图     | L635
-->

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- display ipv6 multicast-vlan**

------------------------------------------------------------------------

**[display ipv6 multicast-vlan**]命令用来显示IPv6组播VLAN的信息。

【命令】

**[display ipv6 multicast-vlan** [ *vlan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vlan-id*]：显示指定IPv6组播VLAN的信息，取值范围为1～4094。如果未指定本参数，将显示所有IPv6组播VLAN的信息。

【举例】

\# 显示所有IPv6组播VLAN的信息。

\<Sysname\> display ipv6 multicast-vlan

Total 2 IPv6 multicast VLANs.

IPv6 multicast VLAN 100:

  Sub-VLAN list(3 in total):

    2-3, 6

  Port list(3 in total):

    GE1/0/1

    GE1/0/2

    GE1/0/3

IPv6 multicast VLAN 200:

  Sub-VLAN list(0 in total):

  Port list(0 in total):

表1-1 display ipv6 multicast-vlan命令显示信息描述表

字段

描述

Total 2 IPv6 multicast VLANs

IPv6组播VLAN的总数

IPv6 multicast VLAN 100

IPv6组播VLAN

Sub-VLAN list(3 in total)

IPv6组播VLAN的子VLAN列表及总数

Port list(3 in total)

IPv6组播VLAN的端口列表及总数

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- display ipv6 multicast-vlan group**

------------------------------------------------------------------------

**[display ipv6 multicast-vlan group**]命令用来显示IPv6组播VLAN的组播组表项信息。

【命令】

集中式设备：

**[display ipv6 multicast-vlan**[ **group** [ *ipv6-source-address* \| *ipv6-group-address* \| **cpu** *cpu-number* \| **verbose** \| **vlan** *vlan-id* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 multicast-vlan**[ **group** [ *ipv6-source-address* \| *ipv6-group-address* \| **slot** *slot-number* [ **cpu** *cpu-number* ] \| **verbose** \| **vlan** *vlan-id* ] \*]]

分布式设备－IRF模式：

**[display ipv6 multicast-vlan**[ **group** [ *ipv6-source-address* \| *ipv6-group-address* \| **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] \| **verbose** \| **vlan** *vlan-id* ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot***slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：[显示指定成员设备]/PEX上[的信息，]*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号[。如果未指定本参数，将显示主设备上的信息。（集中式]IRF设备）（支持IRF3的设备）

**[chassis***chassis-number***slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis***chassis-number***slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号[，]*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu***cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

【举例】

\# 显示IPv6组播VLAN的所有组播组表项的详细信息。

\<Sysname\> display ipv6 multicast-vlan group verbose

Total 6 entries.

IPv6 multicast VLAN 10: Total 3 entries.

  (2::2, FF0E::2)

    Flags: 0x70000020

    Sub-VLANs (1 in total):

      VLAN 40

  (22::22, FF0E::4)

    Flags: 0x70000030

    Sub-VLANs (1 in total):

      VLAN 40

  (::, FF0E::10)

    Flags: 0x10000030

    Sub-VLANs (1 in total):

      VLAN 40

IPv6 multicast VLAN 20: Total 3 entries.

  (2::2, FF0E::2)

    Flags: 0x70000010

    Sub-VLANs (0 in total):

  (22::22, FF0E::4)

    Flags: 0x70000010

    Sub-VLANs (0 in total):

  (::, FF0E::10)

    Flags: 0x50000010

    Sub-VLANs (0 in total):

表1-2 display ipv6 multicast-vlan group命令显示信息描述表

字段

描述

Total 6 entries

表项的总数

IPv6 multicast VLAN 10: Total 3 entries

IPv6组播VLAN 10的组播组表项总数

(::, FF0E::10)

（S，G）表项，::表示所有IPv6组播源

Flags

（S，G）表项的状态，通过将不同的比特位置位来表示不同的状态：

·0x10：表示表项由IPv6组播VLAN创建

·0x20：表示表项由子VLAN创建

·0x40：表示表项即将被删除

·0x10000000：表示表项新创建或在查询周期内收到过MLD查询报文

·0x20000000：表示表项在查询周期内没有收到过MLDv1/v2报告报文

·0x40000000：表示表项在查询周期内没有收到过MLDv2 IS_EX(NULL)报文

Sub-VLANs (1 in total)

IPv6组播VLAN的子VLAN列表及总数

【相关命令】

·**reset ipv6 multicast-vlan group**

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- display ipv6 multicast-vlan forwarding-table**

------------------------------------------------------------------------

**[display ipv6 multicast-vlan forwarding-table**]命令用来显示IPv6组播VLAN转发表的信息。

【命令】

集中式设备：

**[display ipv6 multicast-vlan forwarding-table** [ *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **cpu** *cpu-number* \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 multicast-vlan forwarding-table** [ *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **slot** *slot-number*  **cpu** *cpu-number*  \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

分布式设备－IRF模式：

**[display ipv6 multicast-vlan forwarding-table** [ *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **subvlan** *vlan-id* \| **vlan** *vlan-id* ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

*[prefix-length*]：指定IPv6组播源的前缀长度，取值范围为0～128，缺省值为128。

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

*[prefix-length*]：指定IPv6组播组的前缀长度，取值范围为8～128，缺省值为128。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：[显示指定成员设备]/PEX上[的信息，]*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号[。如果未指定本参数，将显示主设备上的信息。（集中式]IRF设备）（支持IRF3的设备）

**[chassis***chassis-number***slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis***chassis-number***slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号[，]*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局所有主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu***cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[subvlan*** vlan-id*]：显示指定子VLAN的信息。如果未指定本参数，将显示所有子VLAN的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

【举例】

\# 显示IPv6组播VLAN转发表的全部信息。

\<Sysname\> display ipv6 multicast-vlan forwarding-table

IPv6 multicast VLAN 100 Forwarding Table

Total 1 entries, 1 matched

00001. (1::1, FF0E::1)

     Flags: 0x10000

     IPv6 multicast VLAN: 100

     List of sub-VLANs (3 in total):

       1: VLAN 10

       2: VLAN 20

       3: VLAN 30

表1-3 display ipv6 multicast-vlan forwarding-table命令显示信息描述表

字段

描述

IPv6 multicast VLAN 100 Forwarding Table

IPv6组播VLAN 100的转发表

Total 1 entries, 1 matched

表项的总数和匹配数

00001

表示（S，G）项的序号

 (1::1, FF0E::1)

（S，G）表项，::表示所有IPv6组播源

Flags

（S，G）项的当前状态，使用不同的比特位来表示（S，G）项所处的不同状态，主要取值如下：

·0x1：表示表项处于Inactive状态

·0x4：表示表项下刷失败

·0x8：表示有子VLAN下刷失败

·0x200：表示表项处于平滑状态

·0x10000：表示IPv6组播VLAN表项

IPv6 multicast VLAN

IPv6组播VLAN

List of sub-VLANs (3 in total)

IPv6组播VLAN的子VLAN列表及总数

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- ipv6 multicast-vlan**

------------------------------------------------------------------------

**[ipv6 multicast-vlan**]命令用来配置指定VLAN为IPv6组播VLAN，并进入IPv6组播VLAN视图。

**[undo ipv6 multicast-vlan**]命令用来取消指定VLAN为IPv6组播VLAN。

【命令】

**[ipv6 multicast-vlan ***vlan-id*]

**[undo ipv6 multicast-vlan**[ { **all** \| *vlan-id* }]]

【缺省情况】

VLAN不是IPv6组播VLAN。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：指定VLAN的编号，取值范围为1～4094。

**[all**]：删除所有IPv6组播VLAN。

【配置指导】

·要配置为IPv6组播VLAN的指定VLAN必须存在。

·在已使能了IPv6组播路由的设备上不建议再配置IPv6组播VLAN。

·IPv6组播VLAN的总数不得超过系统限制，该限制值与设备的型号有关，请以设备的实际情况为准。

·对于基于子VLAN模式的IPv6组播VLAN，需在IPv6组播VLAN及其所有子VLAN内使能MLD Snooping；对于基于端口模式的IPv6组播VLAN，需在IPv6组播VLAN和所有用户VLAN内使能MLD Snooping。

【举例】

\# 在VLAN 100内使能MLD Snooping，将其配置为IPv6组播VLAN，并进入IPv6组播VLAN视图。

\<Sysname\> system-view

Sysname mld-snooping

Sysname-mld-snooping quit

Sysname vlan 100

Sysname-vlan100 mld-snooping enable

Sysname-vlan100 quit

Sysname ipv6 multicast-vlan 100

Sysname-ipv6-mvlan-100

【相关命令】

·**mld-snooping enable**（IP组播命令参考/MLD Snooping）

·**ipv6 multicast routing**（IP组播命令参考/IPv6组播路由与转发）

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- ipv6 multicast-vlan entry-limit**

------------------------------------------------------------------------

![说明](IPv6组播VLAN命令.files/image001.png)\

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 multicast-vlan entry-limit**]命令用来配置IPv6组播VLAN转发表项的最大数量。

**[undo ipv6 multicast-vlan entry-limit**]命令用来恢复缺省情况。

【命令】

**[ipv6 multicast-vlan entry-limit ***limit*]

**[undo ipv6 multicast-vlan entry-limit**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit*]：IPv6组播VLAN转发表项的最大数量，取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置IPv6组播VLAN转发表项的最大数量为512个。

\<Sysname\> system-view

Sysname ipv6 multicast-vlan entry-limit 512

【相关命令】

·**entry-limit** (MLD-Snooping view)（IP组播命令参考/MLD Snooping）

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- ipv6 port multicast-vlan**

------------------------------------------------------------------------

![说明](IPv6组播VLAN命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 port multicast-vlan**]命令用来指定端口所属的IPv6组播VLAN。

**[undo ipv6 port multicast-vlan**]命令用来恢复缺省情况。

【命令】

**[ipv6 port multicast-vlan ***vlan-id*]

**[undo ipv6 port multicast-vlan**]

【缺省情况】

端口不属于任何IPv6组播VLAN。

【视图】

以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：指定端口所属IPv6组播VLAN的编号，取值范围为1～4094。

【使用指导】

一个端口只能属于一个IPv6组播VLAN。

【举例】

\# 配置端口GigabitEthernet1/0/1属于IPv6组播VLAN 100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 port multicast-vlan 100

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- port (IPv6 multicast-VLAN view)**

------------------------------------------------------------------------

![说明](IPv6组播VLAN命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[port**]命令用来向IPv6组播VLAN内添加端口。

**[undo** **port**]命令用来删除IPv6组播VLAN内的端口。

【命令】

**[port ***interface-list*]

**[undo**]**port** **[all**[ \| ]*interface-list* }

【缺省情况】]

IPv6组播VLAN内没有端口。

【视图】

IPv6组播VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-list*]：端口列表，表示一个或多个端口。表示方式为*interface-list* = *[interface-type interface-number* \**[to***interface-type interface-number*  }]。其中，*interface-type*为接口类型，*interface-number*为接口编号。

**[all**]：删除当前IPv6组播VLAN内的所有端口。

【配置指导】]

·一个端口只能属于一个IPv6组播VLAN。

·只允许将以太网接口或二层聚合接口类型的用户端口配置为IPv6组播VLAN的端口。

【举例】

\# 将端口GigabitEthernet1/0/1到GigabitEthernet1/0/5添加到IPv6组播VLAN 100内。

\<Sysname\> system-view

Sysname ipv6 multicast-vlan 100

Sysname-ipv6-mvlan-100 port gigabitethernet 1/0/1 to gigabitethernet 1/0/5

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- reset ipv6 multicast-vlan group**

------------------------------------------------------------------------

**[reset ipv6 multicast-vlan group**]命令用来清除IPv6组播VLAN的组播组表项。

【命令】

**[reset ipv6 multicast-vlan** **group** [ *ipv6-group-address* [ *prefix-length*  \| *ipv6-source-address*  *prefix-length*  \| **vlan** *vlan-id* ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-group-address*]：清除指定IPv6组播组的表项，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将清除所有IPv6组播组的表项。

*[prefix-length*]：指定IPv6组播组的前缀长度，取值范围为8～128，缺省值为128。

*[ipv6-source-address*]：清除包含指定IPv6组播源的表项。如果未指定本参数，将清除包含所有IPv6组播源的表项。

*[prefix-length*]：指定IPv6组播源的前缀长度，取值范围为0～128，缺省值为128。

**[vlan** *vlan-id*]：清除指定VLAN的表项，取值范围为1～4094。如果未指定本参数，将清除所有VLAN的表项。

【举例】

\# 清除IPv6组播VLAN的所有组播组表项。

\<Sysname\> reset ipv6 multicast-vlan group

【相关命令】

·**display ipv6 multicast-vlan group**

**IPv6组播VLAN \-- IPv6组播VLAN配置命令 \-- subvlan (IPv6 multicast-VLAN view)**

------------------------------------------------------------------------

![说明](IPv6组播VLAN命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[subvlan**]命令用来向IPv6组播VLAN内添加子VLAN。

**[undo** **subvlan**]命令用来删除IPv6组播VLAN内的子VLAN。

【命令】

**[subvlan ***vlan-list*]

**[undo**]**subvlan****[all**[ \| ]*vlan-list* }

【缺省情况】]

IPv6组播VLAN内没有子VLAN。

【视图】

IPv6组播VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-list*]：指定子VLAN列表，表示多个子VLAN。其表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为指定子VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

**[all**]：删除当前IPv6组播VLAN内的所有子VLAN。

【使用指导】

要添加到IPv6组播VLAN内的子VLAN必须存在，且不能是IPv6组播VLAN或其它IPv6组播VLAN的子VLAN。

【举例】

\# 配置VLAN 10到VLAN 15为IPv6组播VLAN 100的子VLAN。

\<Sysname\> system-view

Sysname ipv6 multicast-vlan 100

Sysname-ipv6-mvlan-100 subvlan 10 to 15

