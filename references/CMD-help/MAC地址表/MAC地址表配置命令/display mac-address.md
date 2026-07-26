
**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address**

------------------------------------------------------------------------

**[display mac-address**]命令用来显示MAC地址表信息。

【命令】

**[display mac-address** [ *mac*-*address* [ **vlan** *vlan-id*  \| [ [ **dynamic** \| **static** ]  **interface** *interface-type interface-number*  \| **blackhole** \| **multiport** ]  **vlan** *vlan-id*   **count**  \| **nickname** *nickname* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[mac*-*address*]：显示指定MAC地址的MAC地址表项，*mac*-*address*的格式为H-H-H。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[vlan ***vlan*-*id*]：显示指定VLAN的MAC地址表项。*vlan*-*id*的取值范围为1～4094。

**[dynamic**]：显示动态MAC地址表项。

**[static**]：显示静态MAC地址表项。

**[interface*** interface*-*type interface*-*number*]：显示指定接口的MAC地址表项。*interface*-*type interface*-*number*为接口类型和接口编号。

**[blackhole**]：显示黑洞MAC地址表项。

**[multiport**]：显示多端口单播MAC地址表项。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示MAC地址表项的数量。如果配置本参数，将仅显示符合条件的（由**count**前面的参数决定）MAC地址表项的数量，而不显示MAC地址表项的具体内容。如果不指定本参数，则显示符合条件的MAC地址表的具体内容。

**[nickname** *nickname*]：显示报文离开TRILL网络的RB对应的MAC地址表项。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·使用本命令可以查看静态、动态、黑洞和多端口单播MAC地址表项，表项内容主要包括MAC地址、VLAN ID、接口等信息。

·如果不指定任何参数，将显示所有的MAC地址表项信息。

·对于聚合接口，需要有选中端口，该聚合接口对应的动态MAC地址才能在MAC地址表项中显示。

【举例】

\# 显示VLAN 100的MAC地址表项的信息。

\<Sysname\> display mac-address vlan 100

MAC Address      VLAN ID    State            Port/NickName            Aging

0001-0101-0101   100        Multiport        GE1/0/1                  N

                                             GE1/0/2

0033-0033-0033   100        Blackhole        N/A                      N

0000-0000-0002   100        Static           GE1/0/3                  N

00e0-fc00-5829   100        Learned          GE1/0/4                  Y

\# 显示MAC地址表项的数量。

\<Sysname\> display mac-address count

1 mac address(es) found.

\# 显示指定nickname为0x8c81的RB对应的MAC地址表信息。

\<Sysname\> display mac-address nickname 8c81

MAC Address      VLAN ID    State            Port/NickName            Aging

0000-3300-0001   10         Learned          0x8c81                   Y

0000-3300-0002   10         Learned          0x8c81                   Y

0000-3300-0003   10         Learned          0x8c81                   Y

表1-1 display mac-address命令显示信息描述表

字段

描述

MAC Address

MAC地址

VLAN ID

MAC地址对应接口所属的VLAN

State

MAC地址表项的状态，包括：

·Static：表示该表项是静态MAC地址表项

·Learned：动态MAC地址表项。可以手工配置也可以由设备学习获得

·Blackhole：表示该表项是黑洞MAC地址表项

·Multiport：表示该表项是多端口单播MAC地址表项

Port/NickName

MAC地址对应的接口名称或NickName。如果显示为接口名称，表示发往该MAC地址的报文将从此接口发出（黑洞MAC地址表项此处显示为N/A）；如果显示为NickName（长度为4的十六进制数字，例如0x12ab），表示发往该MAC地址的报文离开TRILL网络的RB。有关NickName、TRILL和RB的详细介绍，请参见"TRILL配置指导"中的"TRILL"

Aging

老化时间，该表项有两种取值：

·Y：表示该表项会被老化

·N：表示该表项不会被老化

*[n* mac address(es) found]

共有*n*个MAC地址表项

【相关命令】

·**mac-address**

·**mac-address timer**

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address aging-time**

------------------------------------------------------------------------

**[display mac-address aging-time**]命令用来显示MAC地址表动态表项的老化时间。

【命令】

**[display mac-address aging-time**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

动态MAC地址表项可以被老化，用户可以配置动态MAC地址表项的老化时间。使用本命令可以查看用户配置的动态MAC地址表项的老化时间。

【举例】

\# 显示MAC地址表中动态表项的老化时间。

\<Sysname\> display mac-address aging-time

MAC address aging time: 300s.

以上显示信息表示：MAC地址表中动态表项的老化时间为300秒。

【相关命令】

·**mac-address timer**

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address mac-learning**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display mac-address mac-learning**]命令用来显示MAC地址学习功能的使能状态。

【命令】

**[display mac-address mac-learning ** **interface** *interface*-*type interface*-*number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface*-*type interface*-*number*]：显示指定接口的MAC地址学习状态。*interface*-*type interface*-*number*为接口类型和接口编号。如果不指定本参数，则显示全局和所有接口的MAC地址学习状态。

【举例】

\# 显示全局和所有接口的MAC地址学习状态。

\<Sysname\> display mac-address mac-learning

Global MAC address learning status: Enabled.

Port                        Learning Status

GE1/0/1                     Enabled

GE1/0/2                     Enabled

GE1/0/3                     Enabled

GE1/0/4                     Enabled

表1-2 display mac-address mac-learning命令显示信息描述表

字段

描述

Global MAC address learning status

全局的MAC地址学习状态：Enabled为使能，Disabled为禁止

Port

接口名称

Learning Status

接口的MAC地址学习状态：Enabled为使能，Disabled为禁止

【相关命令】

·**mac-address mac-learning enable**

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address mac-move**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display mac-address mac-move**]命令用来显示设备启动后的MAC地址迁移记录。

【命令】

集中式设备：

**[display mac-address mac-move**]

分布式设备－独立运行模式/集中式IRF设备：

**[display mac-address mac-move** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display mac-address mac-move** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板上的MAC地址迁移记录，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的MAC地址迁移记录。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的MAC地址迁移记录，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的MAC地址迁移记录。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的MAC地址迁移记录，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的MAC地址迁移记录。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的MAC地址迁移记录，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定任何参数，则显示所有单板上的MAC地址迁移记录。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的MAC地址迁移记录，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定任何参数，则显示所有单板上的MAC地址迁移记录。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的MAC地址迁移记录。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如果MAC地址迁移频繁出现，且同一MAC地址总是在特定的两个接口之间迁移，那么网络中可能存在二层环路。可以通过查看MAC地址迁移记录，发现和定位环路。

需要注意的是：

·在迁移记录中，如果MAC地址、VLAN、源端口、新端口都一样，则视作一条表项。

·设备最多能保存20条最近发生的MAC地址迁移记录。当记录超过20条时，新的迁移记录将会根据上次迁移时间覆盖最早的记录。（集中式设备）

·每个单板最多能保存20条迁移记录；当记录超过20条时，新的迁移记录将会按照上次迁移时间覆盖最早的记录。（分布式设备－独立运行模式）

·每个成员设备最多能保存20条迁移记录；当记录超过20条时，新的迁移记录将会按照上次迁移时间覆盖最早的记录。（集中式IRF设备）

·每个成员设备的每个单板最多能保存20条迁移记录。当记录超过20条时，新的迁移记录将会按照上次迁移时间覆盖最早的记录。（分布式设备－IRF模式）

【举例】

\# 显示2号单板上的MAC地址迁移记录。（分布式设备－独立运行模式）

\<Sysname\> display mac-address mac-move slot 2

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--MAC address moving information\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

MAC address    VLAN Current port  Source port   Last time           Times

0000-0001-002c 1    GE1/0/1       GE1/0/2       2013-05-20 13:40:52 1

0000-0001-002c 1    GE1/0/2       GE1/0/1       2013-05-20 13:41:30 1

\-\--  2 MAC address moving records found  \-\--

\# 显示所有单板上的MAC地址迁移记录。（分布式设备－IRF模式）

\<Sysname\> display mac-address mac-move

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--chassis 1 slot 2 MAC address moving information\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

MAC address    VLAN Current port  Source port   Last time           Times

0000-0001-002c 1    GE1/0/1       GE1/0/2       2013-05-20 13:40:52 20

0000-0001-002c 1    GE1/0/2       GE1/0/1       2013-05-20 13:41:32 20

\-\--  2 MAC address moving records found  \-\--

表1-3 display mac-address mac-move命令显示信息描述表

字段

描述

MAC address

MAC地址

VLAN

MAC地址对应接口所属的VLAN

Current port

MAC地址迁移新接口

Source port

MAC地址迁移源接口

Last time

发生MAC地址迁移的最近一次时间

Times

设备启动后，MAC地址发生迁移的次数。对于同一MAC地址，仅当字段VLAN、Current port和Source port都相同时，次数才加1

【相关命令】

·**mac-address notification mac-move**

**MAC地址表 \-- MAC地址表配置命令 \-- display mac-address statistics**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display**]** mac-address statistics**命令用来显示MAC地址表的统计信息。

【命令】

**[display mac-address**] **statistics**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

本命令主要显示系统目前存在的各类MAC地址表项的数目、以及系统可以支持的各类表项的最大规格。

【举例】

\# 显示MAC地址表中的统计信息。

\<Sysname\> display mac-address statistics

MAC Address Count:

Dynamic Unicast Address (Learned) Count:                         3

Dynamic Unicast Address (Security-service-defined) Count:        4

Static Unicast Address (User-defined) Count:                     0

Static Unicast Address (System-defined) Count:                   3

Total Unicast MAC Addresses In Use:                              10

Total Unicast MAC Addresses Available:                           32768

Multicast and Multiport MAC Address Count:                       1

Static Multicast and Multiport MAC Address (User-defined) Count: 1

Total Multicast and Multiport MAC Addresses Available:           256

表1-4 display mac-address statistic命令显示信息描述表

字段

描述

Dynamic Unicast Address (Learned) Count

报文触发添加的动态单播MAC地址统计

Dynamic Unicast Address (Security-service-defined) Count

安全服务触发添加的动态单播MAC地址统计

Static Unicast Address (User-defined) Count

用户添加的静态单播MAC地址统计

Static Unicast Address (System-defined) Count

系统添加的静态单播MAC地址统计

Total Unicast MAC Addresses In Use

单播MAC地址统计

Total Unicast MAC Addresses Available

单播MAC地址规格

Multicast and Multiport MAC Address Count

组播和多端口单播MAC地址统计

Static Multicast and Multiport MAC Address (User-defined) Count

用户添加的静态组播和多端口单播MAC地址统计

Total Multicast and Multiport MAC Addresses Available

组播和多端口单播MAC地址规格

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address (interface view)**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address**]命令用来在当前接口下添加或者修改MAC地址表项。

**[undo mac-address**]命令用来删除当前接口下的MAC地址表项。

【命令】

二层以太网接口视图/二层聚合接口视图：

**[mac-address **[{ **dynamic** \| **multiport** \| **static** } *mac*-*address* **vlan** *vlan*-*id*]]

**[undo mac-address**[ { **dynamic** \| **multiport** \| **static** } *mac*-*address* **vlan** *vlan*-*id*]]

S通道接口视图/S通道聚合接口视图：

**[mac-address **[{ **dynamic** \| **static** } *mac*-*address* **vlan** *vlan*-*id*]]

**[undo mac-address**[ { **dynamic** \| **static** } *mac*-*address* **vlan** *vlan*-*id*]]

【缺省情况】

接口下没有配置任何MAC地址表项。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dynamic**]：动态MAC地址表项。

**[static**]：静态MAC地址表项。

**[multiport**]：多端口单播MAC地址表项。当报文的目的MAC地址与多端口单播MAC地址表项匹配时，将该报文从多个端口复制转发出去。

*[mac*-*address*]：MAC地址，格式为H-H-H，不支持组播MAC地址和全0的MAC地址。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[vlan*** vlan*-*id*]：[当前接口所属的]VLAN。*vlan-id*为指定VLAN的编号，取值范围为1～4094。该VLAN必须已经创建。

【使用指导】

一般情况下，设备通过源MAC地址学习过程自动建立MAC地址表。为了提高接口安全性，网络管理员可手工在MAC地址表中加入特定MAC地址表项，将用户设备与接口绑定，从而防止非法用户骗取数据。手工配置的静态MAC地址表项优先级高于自动生成的表项。

需要注意的是，如果不保存配置，设备重启后所有表项都会丢失；如果保存配置，静态MAC地址表项不会丢失，动态MAC地址表项会丢失。

【举例】

\# 在端口GigabitEthernet1/0/1下增加静态MAC地址表项000f-e201-0101，该端口属于VLAN 2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address static 000f-e201-0101 vlan 2

\# 在接口Bridge-Aggregation1下增加静态MAC地址表项000f-e201-0102，该接口属于VLAN 1。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 mac-address static 000f-e201-0102 vlan 1

\# 在S通道接口S-Channel1/1:10下增加静态MAC地址表项000f-e201-0102，该接口属于VLAN 1。

\<Sysname\> system-view

Sysname interface s-channel 1/1:10

Sysname-S-Channel1/1:10 mac-address static 000f-e201-0102 vlan 1

\# 在S通道聚合接口Schannel-Aggregation1:2下增加静态MAC地址表项000f-e201-0102，该接口属于VLAN 1。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:2

Sysname-Schannel-Aggregation1:2 mac-address static 000f-e201-0102 vlan 1

\# 在端口GigabitEthernet1/0/1和GigabitEthernet1/0/2下增加多端口单播MAC地址表项0001-0001-0101，两个端口均属于VLAN 2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address multiport 0001-0001-0101 vlan 2

Sysname-GigabitEthernet1/0/1 quit

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 mac-address multiport 0001-0001-0101 vlan 2

【相关命令】

·**display mac-address**

·**mac-address** (system view)

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address (system view)**

------------------------------------------------------------------------

**[mac-address**]命令用来添加或者修改MAC地址表项。

**[undo mac-address**]命令用来删除MAC地址表项。

【命令】

**[mac-address**[ { **dynamic** \| **static** } *mac*-*address* **interface** *interface*-*type interface*-*number* **vlan** *vlan*-*id*]]

**[mac-address** **blackhole** *mac*-*address* **vlan** *vlan*-*id*]

**[mac-address multiport ***mac*-*address* **interface** *interface-list* **vlan** *vlan-id*]

**[undo mac-address**[ [ [ **dynamic** \| **static** ] *mac*-*address* **interface** *interface*-*type interface*-*number* **vlan** *vlan*-*id* ]]]

**[undo mac-address**[ [ **blackhole** \| **dynamic** \| **static** ]  *mac*-*address*  **vlan** *vlan*-*id*]]

**[undo mac-address****[[ **dynamic** \| **static** ] **interface** *interface*-*type interface*-*number*]]

**[undo mac-address** **multiport** *mac-address* **interface** *interface-list* **vlan** *vlan-id*]

**[undo mac-address** [ **multiport**   [ *mac-address*  **vlan** *vlan-id* ]]]

**[undo mac-address** **nickname** *nickname*]

**[undo mac-address** *mac-address* **nickname** *nickname* **vlan** *vlan-id*]

【缺省情况】

系统没有配置任何MAC地址表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dynamic**]：动态MAC地址表项。

**[static**]：静态MAC地址表项。

**[blackhole**]：黑洞MAC地址表项。当报文的源MAC地址或目的MAC地址与黑洞MAC地址表项匹配时，该报文被丢弃。

**[multiport**]：多端口单播MAC地址表项。当报文的目的MAC地址与多端口单播MAC地址表项匹配时，将该报文从多个端口复制转发出去。

*[mac*-*address*]：MAC地址，格式为H-H-H，不支持组播MAC地址和全0的MAC地址。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[vlan*** vlan*-*id*]：指定接口所属的VLAN。*vlan-id*为指定VLAN的编号，取值范围为1～4094。该VLAN必须已经创建。

**[interface*** interface*-*type interface*-*number*]：出接口。*interface*-*type interface*-*number*为接口类型和接口编号。

**[interface** *interface-list*]：接口列表，表示方式为*interface-list =* { *interface-type interface-number* [ **to** *interface-type interface-number*  }&\<1-n\>]。其中，*interface-type interface-number*为接口类型和接口编号，目前只支持二层以太网接口及二层聚合接口。&\<1-n\>表示前面的参数最多可以输入n次。n的取值范围和设备相关，请以设备的实际情况为准。

**[nickname** *nickname*]：报文离开TRILL网络的RB。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数。

【使用指导】

一般情况下，设备通过源MAC地址学习过程自动建立MAC地址表。为了提高接口安全性，网络管理员可手工在MAC地址表中加入特定MAC地址表项，将用户设备与接口绑定，从而防止非法用户骗取数据。手工配置的静态MAC地址表项优先级高于自动生成的表项。

如果需要丢弃指定源MAC地址或目的MAC地址的报文，可配置黑洞MAC地址表项。

多端口单播MAC地址表项用于目的是某个MAC地址的报文从多个端口复制转发出去。第一次执行命令配置某一MAC地址表项时，添加该表项，再次执行命令配置除接口外其余相同的MAC地址表项时，则会为该表项添加一个或多个接口。

需要注意的是：

·MAC地址表项的属性遵循如下原则：用户手工配置的静态MAC地址表项或黑洞MAC地址表项不会被动态MAC地址表项覆盖，而动态MAC地址表项可以被静态MAC地址表项和黑洞MAC地址表项覆盖。

·执行**undo mac-address**命令时若不指定任何参数，将删除所有单播MAC地址表项和静态组播MAC地址表项。

·可以删除指定VLAN的所有MAC地址表项（包括单播MAC地址表项和静态组播MAC地址表项）；可以选择删除动态MAC地址表项、静态MAC地址表项、黑洞MAC地址表项或者多端口单播MAC地址表项；可以按接口删除单播MAC地址表项，但不能按接口删除组播MAC地址表项；可以按报文离开TRILL网络的RB删除单播MAC地址表项。

·如果不保存配置，设备重启后所有表项都会丢失；如果保存配置，静态MAC地址表项和黑洞MAC地址表项不会丢失，动态表项会丢失。

【举例】

\# 添加静态地址表项，目的MAC地址为000f-e201-0101，出接口为GigabitEthernet1/0/1，且该接口属于VLAN 2。

\<Sysname\> system-view

Sysname mac-address static 000f-e201-0101 interface gigabitethernet 1/0/1 vlan 2

\# 添加多端口单播MAC地址表项，目的MAC地址为000f-e201-0101，出接口为GigabitEthernet1/0/1、GigabitEthernet1/0/2和GigabitEthernet1/0/3，且出接口属于VLAN 2。

\<Sysname\> system-view

Sysname mac-address multiport 000f-e201-0101 interface gigabitethernet 1/0/1 to gigabitethernet 1/0/3 vlan 2

【相关命令】

·**display mac-address**

·**mac-address** (interface view)

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address mac-learning enable**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address mac-learning enable**]命令用来打开设备全局、接口或者VLAN的MAC地址学习功能。

**[undo mac-address mac-learning enable**]命令用来关闭设备全局、接口或者VLAN的MAC地址学习功能。

【命令】

**[mac-address mac-learning enable**]

**[undo mac-address mac-learning enable**]

【缺省情况】

MAC地址学习功能处于开启状态。

【视图】

系统视图/VLAN视图/二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

有时为了保证设备的安全，需要关闭MAC地址学习功能。常见的危及设备安全的情况是：非法用户使用大量源MAC地址不同的报文攻击设备，导致设备MAC地址表资源耗尽，造成设备无法根据网络的变化更新MAC地址表。关闭MAC地址学习功能可以有效防止这种攻击。

关闭MAC地址学习功能后，设备就学不到新地址，从而影响设备及时刷新MAC地址表。用户可以根据实际情况关闭接口的MAC地址学习功能。

关闭MAC地址学习功能可能会导致广播，因此在关闭接口的MAC地址学习功能的同时，一般还要使用接口广播风暴抑制功能。有关广播风暴抑制功能的介绍，请参见"接口管理配置指导"中的"以太网接口"。

需要注意的是：

·全局MAC地址学习功能不能控制TRILL网络、EVB的S通道以及VPLS的VSI中MAC地址的学习。有关EVB和S通道的介绍，请参见"EVB配置指导"中的"EVB"。有关VPLS和VSI的介绍，请参见"MPLS配置指导"中的"VPLS"。

·关闭全局的MAC地址学习功能的同时也就关闭了全部接口的MAC地址学习功能。

·在开启全局的MAC地址学习功能的前提下，用户可以关闭设备上单个接口或指定VLAN的MAC地址学习功能。

·关闭MAC地址学习功能后，对于已经存在的动态MAC地址表项的处理情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 关闭全局MAC地址学习功能。

\<Sysname\> system-view

Sysname undo mac-address mac-learning enable

\# 关闭VLAN 10的MAC地址学习功能。

\<Sysname\> system-view

Sysname vlan 10

Sysname-vlan10 undo mac-address mac-learning enable

\# 关闭端口GigabitEthernet1/0/1的MAC地址学习功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo mac-address mac-learning enable

\# 关闭接口Bridge-Aggregation1的MAC地址学习功能。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 undo mac-address mac-learning enable

\# 关闭S通道接口S-Channel1/1:10的MAC地址学习功能。

\<Sysname\> system-view

Sysname interface s-channel 1/1:10

Sysname-S-Channel1/1:10 undo mac-address mac-learning enable

\# 关闭S通道聚合接口Schannel-Aggregation1:2的MAC地址学习功能。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:2

Sysname-Schannel-Aggregation1:2 undo mac-address mac-learning enable

【相关命令】

·**display mac-address mac-learning**

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address mac-learning priority**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address mac-learning priority**]命令用来配置接口的MAC地址学习优先级。

**[undo mac-address mac-learning priority**]命令用来恢复缺省情况。

【命令】

**[mac-address mac-learning priority**[ { **high** \| **low** }]]

**[undo mac-address mac-learning priority**]

【缺省情况】

MAC地址学习优先级为低优先级。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[high**]：配置MAC地址学习优先级为高优先级。

**[low**]：配置MAC地址学习优先级为低优先级。

【使用指导】

·接口的MAC地址学习功能分为两个优先级：高优先级和低优先级。对于高优先级的接口，可以学习任何MAC地址；对于低优先级的接口，在学习MAC地址时需要查看高优先级接口是否已经学到该MAC地址，如果已经学到，则不允许学习该MAC地址。

·为了预防攻击，可以将上行接口的MAC地址学习优先级配置为高优先级，下行接口的MAC地址学习优先级配置为低优先级，那么，下行接口就不会学到网关等上层设备的MAC地址，避免了攻击。

【举例】

\# 配置端口GigabitEthernet1/0/1的MAC地址学习优先级为高优先级。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address mac-learning priority high

\# 配置接口Bridge-Aggregation1的MAC地址学习优先级为高优先级。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 mac-address mac-learning priority high

\# 配置S通道接口S-Channel1/1:10的MAC地址学习优先级为高优先级。

\<Sysname\> system-view

Sysname interface s-channel 1/1:10

Sysname-S-Channel1/1:10 mac-address mac-learning priority high

\# 配置S通道聚合接口Schannel-Aggregation1:2的MAC地址学习优先级为高优先级。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:2

Sysname-Schannel-Aggregation1:2 mac-address mac-learning priority high

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address mac-roaming enable**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address mac-roaming enable**]命令用来开启全局的MAC地址同步功能。

**[undo mac-address mac-roaming enable**]命令用来恢复缺省情况。

【命令】

**[mac-address mac-roaming enable**]

**[undo mac-address mac-roaming enable**]

【缺省情况】

全局的MAC地址同步功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·若不同IRF成员设备上的端口为同一聚合组的选中端口，则不论全局的MAC地址同步功能是否开启，这些选中端口所在成员设备间都会进行MAC地址同步。有关聚合组的相关介绍和配置内容，请参见"二层技术-以太网交换配置指导"中的"以太网链路聚合"。（集中式IRF设备）

·开启全局的MAC地址同步功能后，若不同IRF成员设备的MAC地址规格不同，会造成超过成员设备规格的MAC地址无法同步成功。（集中式IRF设备）

·若设备不同单板上的端口为同一聚合组的选中端口，则不论全局的MAC地址同步功能是否开启，这些选中端口所在单板间都会进行MAC地址同步。有关聚合组的相关介绍和配置内容，请参见"二层技术-以太网交换配置指导"中的"以太网链路聚合"。（分布式设备－独立运行模式/分布式设备－IRF模式）

·开启全局的MAC地址同步功能后，若设备上不同单板的MAC地址规格不同，会造成超过单板规格的MAC地址无法同步成功。（分布式设备－独立运行模式/分布式设备－IRF模式）

【举例】

\# 开启全局的MAC地址同步功能。

\<Sysname\> system-view

Sysname mac-address mac-roaming enable

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address max-mac-count (interface view)**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address max-mac-count**]命令用来配置接口的MAC地址数学习上限。

**[undo mac-address max-mac-count**]命令用来恢复缺省情况。

【命令】

**[mac-address max-mac-count** *count*]

**[undo mac-address max-mac-count**]

【缺省情况】

接口的MAC地址数学习上限与设备的型号有关，请以设备的实际情况为准。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：接口的MAC地址数学习上限，为0即表示不允许该接口学习MAC地址。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

通过配置接口的MAC地址数学习上限，用户可以控制设备维护的MAC地址表的表项数量。如果MAC地址表过于庞大，可能导致设备的转发性能下降。当接口学习到的MAC地址数达到上限时，该接口将不再对MAC地址进行学习。

【举例】

\# 配置端口GigabitEthernet1/0/1的MAC地址数学习上限为600。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address max-mac-count 600

【相关命令】

·**mac-address**

·**mac-address max-mac-count enable-forwarding** (interface view)

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address max-mac-count (VLAN view)**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address max-mac-count**]命令用来配置VLAN的MAC地址数学习上限。

**[undo mac-address max-mac-count**]命令用来恢复缺省情况。

【命令】

**[mac-address max-mac-count** *count*]

**[undo mac-address max-mac-count**]

【缺省情况】

VLAN的MAC地址数学习上限与设备的型号有关，请以设备的实际情况为准。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：VLAN的MAC地址数学习上限，0即表示不允许该VLAN学习MAC地址。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·通过配置VLAN的MAC地址数学习上限，用户可以控制设备维护的VLAN的MAC地址表的表项数量。如果MAC地址表过于庞大，可能导致设备的转发性能下降。当VLAN学习到的MAC地址数达到上限时，该VLAN将不再对MAC地址进行学习。

·由于Super VLAN没有实际的二层物理端口，学习的MAC地址数永远为0，所以在Super VLAN下配置MAC地址数学习上限没有意义。有关Super VLAN的详细介绍，请参见"二层技术-以太网交换"中的"VLAN"。

【举例】

\# 配置VLAN 10的MAC地址数学习上限为600。

\<Sysname\> system-view

Sysname vlan 10

Sysname-vlan10 mac-address max-mac-count 600

【相关命令】

·**mac-address**

·**mac-address max-mac-count enable-forwarding** (VLAN view)

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address max-mac-count enable-forwarding (interface view)**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address max-mac-count enable-forwarding**]命令用来配置当达到接口的MAC地址数学习上限时，允许转发源MAC地址不在MAC地址表里的报文。

**[undo mac-address max-mac-count enable-forwarding**]命令用来配置当达到接口的MAC地址数学习上限时，禁止转发源MAC地址不在MAC地址表里的报文。

【命令】

**[mac-address max-mac-count enable-forwarding**]

**[undo mac-address max-mac-count** **enable-forwarding**]

【缺省情况】

当达到接口的MAC地址数学习上限时，允许转发源MAC地址不在MAC地址表里的报文。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置端口GigabitEthernet1/0/1的MAC地址数学习上限为600，当端口学习的MAC地址数达到600时，禁止转发源MAC地址不在MAC地址表里的报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address max-mac-count 600

Sysname-GigabitEthernet1/0/1 undo mac-address max-mac-count enable-forwarding

【相关命令】

·**mac-address**

·**mac-address max-mac-count** (interface view)

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address max-mac-count enable-forwarding (VLAN view)**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address max-mac-count enable-forwarding**]命令用来配置当达到VLAN的MAC地址数学习上限时，允许转发源MAC地址不在MAC地址表里的报文。

**[undo mac-address max-mac-count enable-forwarding**]命令用来配置当达到VLAN的MAC地址数学习上限时，禁止转发源MAC地址不在MAC地址表里的报文。

【命令】

**[mac-address max-mac-count enable-forwarding**]

**[undo mac-address max-mac-count enable-forwarding**]

【缺省情况】

当达到VLAN的MAC地址数学习上限时，允许转发源MAC地址不在MAC地址表里的报文。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置VLAN 10的MAC地址数学习上限为600，当VLAN 10学习的MAC地址数达到600时，禁止转发源MAC地址不在MAC地址表里的报文。

\<Sysname\> system-view

Sysname vlan 10

Sysname-vlan10 mac-address max-mac-count 600

Sysname-vlan10 undo mac-address max-mac-count enable-forwarding

【相关命令】

·**mac-address**

·**mac-address max-mac-count** (VLAN view)

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address notification mac-move**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address notification mac-move**]命令用来开启MAC地址迁移上报功能。

**[undo mac-address notification mac-move**]命令用来恢复缺省情况。

【命令】

**[mac-address notification mac-move ** **interval** *interval-value* ]

**[undo mac-address notification mac-move**]

【缺省情况】

MAC地址迁移上报功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：MAC地址迁移检测周期，单位为分钟，取值范围为1～60。如果未指定该参数，将采用缺省MAC地址迁移检测周期1分钟。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

开启MAC地址迁移上报功能后，当系统检测到地址迁移，会显示MAC地址迁移日志，包括MAC地址、该MAC地址所在VLAN ID、MAC地址迁移源接口和新接口，以及该MAC地址在一个MAC地址迁移检测周期内的迁移次数。

需要注意的是：

·执行本命令后，必须同时通过**snmp-agent trap enable mac-address**命令开启MAC地址表的告警功能，系统才会显示MAC地址迁移日志

·开启MAC地址迁移上报功能后，系统按照MAC地址迁移检测周期的间隔显示上一个MAC地址迁移检测周期内发生的MAC地址迁移日志。

·一个MAC地址迁移检测周期内，最多能显示20条最新的MAC地址的迁移日志；新发生的迁移日志会覆盖最旧的日志，旧的日志信息将丢弃。（集中式设备）

·一个MAC地址迁移检测周期内，每台成员设备最多能显示20条最新的MAC地址的迁移日志；新发生的迁移日志会覆盖最旧的日志，旧的日志信息将丢弃。（集中式IRF设备）

·一个MAC地址迁移检测周期内，每个单板最多能显示20条最新的MAC地址的迁移日志。新发生的迁移日志会覆盖最旧的日志，旧的日志信息将丢弃。（分布式设备－独立运行模式/分布式设备－IRF模式）

【举例】

\# 开启MAC地址迁移上报功能。

\<Sysname\> system-view

Sysname mac-address notification mac-move

Sysname

%May 14 17:16:45:688 2013 H3C MAC/4/MAC_FLAPPING: MAC address 0000-0012-0034 in VLAN 500 has moved from port GE1/0/1 to port GE1/0/2 for 1 times

以上显示信息表明：MAC地址0000-0012-0034所在VLAN ID为500，MAC地址迁移源接口为GigabitEthernet1/0/1，MAC地址迁移新接口为GigabitEthernet1/0/2，该MAC地址在一个MAC地址迁移检测周期内的迁移次数为1。

【相关命令】

·**display mac-address mac-move**

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address notification mac-move suppression (interface view)**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address notification mac-move suppression**]命令用来开启当前接口上的MAC地址迁移抑制功能。

**[undo mac-address notification mac-move suppression**]命令用来恢复缺省情况。

【命令】

**[mac-address notification mac-move suppression**]

**[undo mac-address notification mac-move suppression**]

【缺省情况】

MAC地址迁移抑制功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启MAC地址迁移抑制功能后，当监测到一个MAC地址迁移检测周期内某个MAC地址从某端口上迁移出或者迁移到该端口的次数超过MAC地址迁移抑制的检测阈值，则将该端口down，用户可以执行命令**shutdown**和**undo shutdown**将该端口恢复，也可以等MAC地址迁移抑制时间间隔后让该端口自行恢复up。

【举例】

\# 开启MAC地址迁移抑制功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address notification mac-move suppression

【相关命令】

·**mac-address notification mac-move suppression** (system view)

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address notification mac-move suppression (system view)**

------------------------------------------------------------------------

**[mac-address notification mac-move suppression**]命令用来配置MAC地址迁移抑制功能的相关参数。

**[undo mac-address notification mac-move suppression**]命令用来恢复缺省情况。

【命令】

**[mac-address notification mac-move suppression**[{ **interval** *interval-value* \| **threshold** *threshold-value* }]]

**[undo mac-address notification mac-move suppression**[ { **interval** \| **threshold** }]]

【缺省情况】

MAC地址迁移抑制功能的相关参数未配置，采用缺省抑制时间间隔30秒和缺省阈值3次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval-value*]：MAC地址迁移抑制时间间隔（检测攻击后，端口保持down状态的持续时间），单位为秒，取值范围为30～86400。如果未指定该参数，将采用缺省抑制时间间隔30秒。

**[threshold*** threshold-value*]：MAC地址迁移抑制的检测阈值（一个MAC地址迁移检测周期内允许MAC地址迁移的最大的迁移次数），取值范围为0～1024。如果未指定该参数，将采用缺省阈值3次。

【使用指导】

·配置本命令后，当接口上开启了MAC地址迁移抑制功能时，本命令配置的参数才能生效。

·本命令可多次配置，配置**interval*** interval-value*和**threshold*** threshold-value*时互不影响

【举例】

\# 配置MAC地址迁移抑制功能的抑制间隔为40s，检测阈值为1。

\<Sysname\> system-view

Sysname mac-address notification mac-move suppression interval 40

Sysname mac-address notification mac-move suppression threshold 1

【相关命令】

·**mac-address notification mac-move suppression** (interface view)

**MAC地址表 \-- MAC地址表配置命令 \-- mac-address timer**

------------------------------------------------------------------------

**[mac-address timer**]命令用来配置动态MAC地址表项的老化时间。

**[undo mac-address timer**]命令用来恢复缺省情况。

【命令】

**[mac-address timer **[{ **aging** *seconds* \| **no-aging** }]]

**[undo mac-address timer**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aging*** seconds*]：动态MAC地址表项的老化时间，单位为秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[no-aging**]：不老化。

【使用指导】

当网络拓扑改变后，动态MAC地址表项不会及时自动更新。这样，由于设备学习不到新的MAC地址，会导致用户流量不能正常转发。因此，需要配置动态MAC地址表项老化时间。超出设定的老化时间，动态MAC地址表项被自动删除，设备重新进行MAC地址学习，构建新的动态MAC地址表项。

用户配置的老化时间过长或者过短，都可能影响设备的运行性能：

·如果用户配置的老化时间过长，设备可能会保存许多过时的MAC地址表项，从而耗尽MAC地址表资源，导致设备无法根据网络的变化更新MAC地址表。

·如果用户配置的老化时间太短，设备可能会删除有效的MAC地址表项，可能导致设备广播大量的数据报文，影响设备的运行性能。

所以用户需要根据实际情况，配置合适的老化时间来有效的实现MAC地址老化功能。

【举例】

\# 配置动态MAC地址表项的老化时间为500秒。

\<Sysname\> system-view

Sysname mac-address timer aging 500

【相关命令】

·**display mac-address aging-time**

**MAC地址表 \-- MAC地址表配置命令 \-- snmp-agent trap enable mac-address**

------------------------------------------------------------------------

**[snmp-agent trap enable mac-address**]命令用来开启MAC地址表的告警功能。

**[undo snmp-agent trap enable mac-address**]命令用来关闭MAC地址表的告警功能。

【命令】

**[snmp-agent trap enable mac-address ** **mac-move** ]

**[undo snmp-agent trap enable mac-address ** **mac-move** ]

【缺省情况】

MAC地址表的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mac-move**]：打开MAC地址表模块的MAC地址迁移上报的告警功能。如果未指定该参数，则表示打开MAC地址模块所有的告警功能。

【使用指导】

·当MAC地址表的告警功能关闭后，将采用Syslog方式上报信息。

·目前MAC地址表模块仅有MAC地址迁移上报的告警功能，所以打开或关闭MAC地址迁移上报的告警功能，就相当于打开或关闭MAC地址表所有的告警功能。

【举例】

\# 配置采用Syslog方式上报MAC地址迁移。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable mac-address mac-move

【相关命令】

·**mac-address notification mac-move**

\

**MAC Information \-- MAC Information配置命令 \-- mac-address information enable (interface view)**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address information enable**]命令用来使能当前接口的MAC Information功能。

**[undo mac-address information enable**]命令用来关闭当前接口的MAC Information功能。

【命令】

**[mac-address information enable **[{ **added** \| **deleted** }]]

**[undo mac-address information enable **[{ **added** \| **deleted** }]]

【缺省情况】

接口的MAC Information功能处于关闭状态。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[added**]：表示配置接口在学习到新的MAC地址时记录MAC变化信息。本参数的支持情况与设备的型号相关，请以设备的实际情况为准。

**[deleted**]：表示配置接口在删除MAC地址时记录MAC变化信息。本参数的支持情况与设备的型号相关，请以设备的实际情况为准。

【使用指导】

必须同时使能全局和接口的MAC Information功能，MAC Information功能才会生效。

【举例】

\# 使能端口GigabitEthernet1/0/1的MAC Information功能，使端口在学习到新的MAC时记录MAC变化信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address information enable added

\# 使能S通道接口S-Channel1/1:10的MAC Information功能，使接口在学习到新的MAC时记录MAC变化信息。

\<Sysname\> system-view

Sysname interface s-channel 1/1:10

Sysname-S-Channel1/1:10 mac-address information enable added

\# 使能S通道聚合接口Schannel-Aggregation1:2的MAC Information功能，使接口在学习到新的MAC时记录MAC变化信息。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:2

Sysname-Schannel-Aggregation1:2 mac-address information enable added

【相关命令】

·**mac-address information enable** (system view)

**MAC Information \-- MAC Information配置命令 \-- mac-address information enable (system view)**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address information enable**]命令用来使能全局MAC Information功能。

**[undo mac-address information enable**]命令用来关闭全局MAC Information功能。

【命令】

**[mac-address information enable**]

**[undo mac-address information enable**]

【缺省情况】

全局MAC Information功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

必须同时使能全局和接口的MAC Information功能，MAC Information功能才会生效。

【举例】

\# 使能全局MAC Information功能。

\<Sysname\> system-view

Sysname mac-address information enable

【相关命令】

·**mac-address information enable** (interface view)

**MAC Information \-- MAC Information配置命令 \-- mac-address information interval**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address information interval**]命令用来配置发送MAC变化通知的时间间隔。

**[undo mac-address information interval**]命令用来恢复缺省情况。

【命令】

**[mac-address information interval ***interval-time*]

**[undo mac-address information interval**]

【缺省情况】

发送MAC变化通知的时间间隔为1秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-time*]：发送MAC变化通知的时间间隔，取值范围为1～20000，单位为秒。

【使用指导】

为了防止过于频繁发送的MAC变化通知干扰用户，可以将此时间间隔调整为较大值。

【举例】

\# 配置设备发送MAC变化通知的时间间隔为200秒。

\<Sysname\> system-view

Sysname mac-address information interval 200

**MAC Information \-- MAC Information配置命令 \-- mac-address information mode**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address information mode**]命令用来配置发送MAC变化通知的方式。

**[undo mac-address information mode**]命令用来恢复缺省情况。

【命令】

**[mac-address information mode**[ { **syslog** \| **trap** }]]

**[undo mac-address information mode**]

【缺省情况】

采用Trap方式发送MAC变化通知。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[syslog**]：表示采用Syslog方式发送MAC变化通知。

**[trap**]：表示采用Trap方式发送MAC变化通知。

【举例】

\# 配置设备采用Trap方式发送MAC变化通知。

\<Sysname\> system-view

Sysname mac-address information mode trap

**MAC Information \-- MAC Information配置命令 \-- mac-address information queue-length**

------------------------------------------------------------------------

![说明](MAC地址表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address information queue-length**]命令用来配置MAC Information缓存队列长度。

**[undo mac-address information queue-length**]命令用来恢复缺省情况。

【命令】

**[mac-address information queue-length ***value*]

**[undo mac-address information queue-length**]

【缺省情况】

MAC Information缓存队列长度为50。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：MAC Information缓存队列长度，取值范围为0～1000，表示可存放的MAC地址变化信息条数。

【使用指导】

·如果MAC Information缓存队列长度为0，则当接口学习到或删除掉一条MAC地址时会立即发送日志或SNMP告警信息。

·如果MAC Information缓存队列长度不为0，则将MAC地址变化信息存放在缓存队列中。当未达到发送MAC变化通知的时间间隔，此时若缓存队列被写满，新的MAC地址变化信息将覆盖缓存队列中最后一条写入的信息；当达到发送MAC变化通知的时间间隔时，不论此时缓存队列是否已被写满，都发送日志或SNMP告警信息。

【举例】

\# 配置MAC Information缓存队列长度为600。

\<Sysname\> system-view

Sysname mac-address information queue-length 600

