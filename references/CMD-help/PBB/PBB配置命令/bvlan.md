
**PBB \-- PBB配置命令 \-- bvlan**

------------------------------------------------------------------------

**[bvlan**]命令用来为PBB VSI实例指定B-VLAN。

**[undo bvlan**]命令用来删除PBB VSI实例的B-VLAN。

【命令】

**[bvlan*** vlan-id*]

**[undo bvlan**]

【缺省情况】

PBB VSI实例未指定B-VLAN。

【视图】

VSI PBB视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：B-VLAN的编号，取值范围1～4094。

【使用指导】

PBB VSI实例必须指定B-VLAN才能够生效，只有I-SID和B-VLAN都相同的PBB VSI实例才能互通。一个PBB VSI实例只能够指定一个B-VLAN，多个不同的VSI可以指定相同的B-VLAN。

【举例】

\# 使能L2VPN功能，创建PBB VSI实例web，其I-SID为100，指定该PBB VSI实例的B-VLAN为100。

\<Sysname\> system-view

Sysname l2vpn enable

Sysname vsi web

Sysname-vsi-web pbb i-sid 100

Sysname-vsi-web-100 bvlan 100

【相关命令】

·**vsi**

**PBB \-- PBB配置命令 \-- display l2vpn minm connection**

------------------------------------------------------------------------

**[display l2vpn minm connection**]命令用来显示MAC-in-MAC连接信息。

【命令】

**[display l2vpn minm connection ** **vsi** *vsi-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi*** vsi-name*]：显示指定VSI的MAC-in-MAC连接信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的MAC-in-MAC连接信息。

【举例】

\# 显示所有VSI的MAC-in-MAC连接信息。

\<Sysname\> display l2vpn minm connection

Total number of MinM connections: 2

Types: MC - multicast, UC - unicast

VSI name: 1

Link ID  I-SID     BMAC            BVLAN  Owner   Type  Interface

68       1         00e0-3948-0100  4001   PBB     UC    GE1/0/1

-        1         011e-8300-0001  4001   PBB     MC    GE1/0/1

VSI name: 2

Link ID  I-SID     BMAC            BVLAN  Owner   Type  Interface

69       2         00e0-3948-0300  4002   PBB     UC    GE1/0/2

-        2         011e-8300-0002  4002   PBB     MC    GE1/0/2

表1-1 display l2vpn minm connection命令显示信息描述表

字段

描述

VSI name

VSI名称

Link ID

MAC-in-MAC连接的链路标识符

I-SID

骨干网服务实例编号

BMAC

骨干网MAC

BVLAN

骨干网VLAN

Owner

表项生成者，取值为PBB或SPB

Type

MAC-in-MAC连接的属性标记，取值包括：

·MC：组播表项

·UC：单播表项

Interface

出接口

**PBB \-- PBB配置命令 \-- display l2vpn minm forwarding**

------------------------------------------------------------------------

**[display l2vpn minm forwarding**]命令用来显示MAC-in-MAC转发表项信息。

【命令】

集中式设备：

**[display l2vpn minm forwarding ** **vsi** *vsi-name* ]

分布式设备―独立运行模式/集中式IRF设备：

**[display l2vpn minm forwarding ** **vsi** *vsi-name* ] **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display l2vpn minm forwarding ** **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi*** vsi-name*]：显示指定VSI的MAC-in-MAC转发表项信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的MAC-in-MAC转发表项信息。

**[slot*** slot-number*]：显示指定单板上的MAC-in-MAC转发表项信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示主控板上的MAC-in-MAC转发表项信息。（分布式设备―独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的MAC-in-MAC转发表项信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，则显示Master设备上的MAC-in-MAC转发表项信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的MAC-in-MAC转发表项信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，则显示Master设备上的MAC-in-MAC转发表项信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定成员设备上指定单板的MAC-in-MAC转发表项信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示Master设备上主控板的MAC-in-MAC转发表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定单板的MAC-in-MAC转发表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，则显示Master设备上主控板的MAC-in-MAC转发表项信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的MAC-in-MAC转发表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示所有的MAC-in-MAC转发表项信息。

\<Sysname\> display l2vpn minm forwarding

Total number of MinM connections: 4

Types: MC - multicast, UC -- unicast

Status Flag: \* - inactive

VSI name: 1

Link ID I-SID     BMAC            BVLAN Owner Type Interface

68      1         00e0-3948-0100  4001  PBB   UC   GE1/0/1

-       1         011e-8300-0001  4001  PBB   MC   GE1/0/1

VSI name: 2

Link ID I-SID     BMAC            BVLAN Owner Type Interface

69      2         00e0-3948-0300  4002  PBB   UC   GE1/0/2

-       2         011e-8300-0002  4002  PBB   MC   GE1/0/2

                                                   GE1/0/3

                                                   GE1/0/4

表1-2 display l2vpn minm forwarding命令显示信息描述表

字段

描述

VSI name

VSI名称

Link ID

MAC-in-MAC连接的链路标识符

I-SID

骨干网服务实例编号

BMAC

骨干网MAC

BVLAN

骨干网VLAN

Owner

表项生成者，取值为PBB或SPB

Type

属性标记，取值包括：

·MC：组播表项

·UC：单播表项

Interface

出接口

如果接口后面带有"\*"，则表示该接口下刷驱动失败

**PBB \-- PBB配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

**[display l2vpn vsi**]命令用来显示VSI的信息。

【命令】

**[display**]**l2vpn****vsi** \****[name*** vsi-name* \**verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name**]* vsi-name*：显示指定VSI的信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的信息。

**[verbose**]：显示VSI的详细信息。如果不指定本参数，则显示VSI的简要信息。

【举例】

\# 显示所有VSI的详细信息。

\<Sysname\> display l2vpn vsi verbose

VSI Name: 1

  VSI Index               : 0

  VSI State               : Up

  MTU                     : 1500

  Bandwidth               : 102400 kbps

  Broadcast Restrain      : 5%

  Multicast Restrain      : 100%

  Unknown Unicast Restrain: 100%

  MAC Learning            : Enabled

  MAC Table Limit         : -

  Drop Unknown            : Disabled

  PBB I-SID               : 1

  PBB Connections:

    BMAC            BVLAN            Link ID    Type

    00e0-3948-0100  4001             68         Unicast

    011e-8300-0001  4001             -          Multicast

  ACs:

    AC                               Link ID    State

    BAGG1 srv1                       0          Down

VSI Name: 2

  VSI Index               : 1

  VSI State               : Up

  MTU                     : 1500

  Bandwidth               : 102400 kbps

  Broadcast Restrain      : 5%

  Multicast Restrain      : 100%

  Unknown Unicast Restrain: 100%

  MAC Learning            : Enabled

  MAC Table Limit         : -

  Drop Unknown            : Disabled

  PBB I-SID               : 2

  PBB Connections:

    BMAC            BVLAN            Link ID    Type

    00e0-3948-0300  4002             69         Unicast

    011e-8300-0002  4002             -          Multicast

表1-3 display l2vpn vsi命令显示信息描述表

字段

描述

VSI Name

VSI名称

VSI Index

VSI索引

VSI Description

VSI的描述信息，如果不配置，则此行不显示

VSI State

VSI的状态，取值包括

·Up：up状态

·Down：down状态

·Administratively down：通过{.TableTextChar}**shutdown**命令手工关闭{.TableTextChar}VSI

MTU

VSI上配置的最大传输单元

Bandwidth

VSI的带宽限制值，单位为kbps

Broadcast Restrain

VSI的广播抑制百分比。当VSI的广播流量速率超出特定值（带宽限制值×广播抑制百分比）时，该VSI会丢弃广播报文

Multicast Restrain

VSI的组播抑制百分比。当VSI的组播流量速率超出特定值（带宽限制值×组播抑制百分比）时，该VSI会丢弃组播报文

Unknown Unicast Restrain

VSI的未知单播抑制百分比。当VSI的未知单播流量速率超出特定值（带宽限制值×未知单播抑制百分比）时，该VSI会丢弃未知单播流量报文

MAC Learning

是否使能了MAC地址学习功能，取值包括：

·Enabled：使能了MAC地址学习功能

·Disabled：未使能{.TableTextChar}MAC地址学习功能{.TableTextChar}

MAC Table Limit

VSI内MAC地址表项的最大数目

取值为Unlimited{.ItemListinTableCharChar}，表示不限制VSI{.ItemListinTableCharChar}内MAC{.ItemListinTableCharChar}地址表项的最大数目

Drop Unknown

当VSI内学习到的MAC地址数达到最大值后，是否禁止转发源MAC地址不在MAC地址表里的报文：

·Enabled：表示禁止转发

·Disabled：表示允许转发{.TableTextChar}

Hub-Spoke

是否使能了Hub-spoke能力。取值为Enabled，表示使能了Hub-spoke能力；如果未使能Hub-spoke能力，则不显示该字段

Hub-spoke不适用于PBB，PBB不关心该字段取值

PBB I-SID

PBB骨干网服务实例编号

PBB Connections

PBB连接

BMAC

骨干网MAC

BVLAN

骨干网VLAN

Type

属性标记，取值包括：

·Multicast：组播表项

·Unicast：单播表项，该表项的支持情况与产品型号有关，请以产品的实际情况为准

ACs

VSI的AC列表

AC

接入电路，取值有如下两种：

·三层接口名称：如GE0/1/4。在三层接口下关联VSI时，AC取值为此方式

· 二层接口名称和以太网服务实例：如{.TableTextChar}GE0/1/3 srv1。在以太网服务实例下关联{.TableTextChar}VSI时，{.TableTextChar}AC取值为此方式{.TableTextChar}

Link ID

AC在VSI内的链路ID

State

AC的状态，取值包括Up和Down

**PBB \-- PBB配置命令 \-- display pbb connection**

------------------------------------------------------------------------

**[display pbb connection**]命令用来显示PBB VSI实例的连接信息。

【命令】

**[display pbb connection ** **vsi** *vsi-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi ***vsi-name*]：显示指定PBB VSI实例的连接信息。*vsi-name*为PBB VSI实例的名称，为1～31个字符的字符串，区分大小写。如果未指定该参数，将显示所有PBB VSI实例的连接信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

【举例】

![说明](PBB命令.files/image001.png)

本命令具体的显示信息与设备的实际情况有关，请以设备的实际情况为准。

\# 显示所有PBB VSI实例的连接信息。

\<Sysname\> display pbb connection

VSIIndex  I-SID   BMAC            BVLAN  Port       Type  Aging

0         1       011e-8300-0001  4001   GE1/0/1    MC    N

0         1       00e0-3948-0100  4001   GE1/0/1    UC    Y

1         2       011e-8300-0002  4002   GE1/0/2    MC    N

                                         GE1/0/3

                                         GE1/0/4

1         2       00e0-3948-0300  4002   GE1/0/2    UC    Y

表1-4 display pbb connection命令显示信息描述表

字段

描述

VSIIndex

VSI实例的索引

I-SID

骨干网服务实例编号

BMAC

B-MAC地址

BVLAN

B-VLAN的编号

Port

出接口的名称

Type

表项类型：

·UC：单播表项

·MC：组播表项

Aging

老化标记：

·Y：支持老化

·N：不支持老化

【相关命令】

·**reset pbb connection**

**PBB \-- PBB配置命令 \-- encapsulation**

------------------------------------------------------------------------

**[encapsulation**]命令用来配置当前PBB VSI实例对应的数据封装类型。

**[undo encapsulation**]命令用来恢复缺省情况。

【命令】

**[encapsulation **[{ **ethernet** \| **vlan** }]]

**[undo encapsulation**]

【缺省情况】

数据封装类型为VLAN。

【视图】

VSI PBB视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ethernet**]：数据封装类型为Ethernet。

**[vlan**]：数据封装类型为VLAN。

【举例】

\# 配置PBB VSI实例web对应的数据封装类型为Ethernet。

\<Sysname\> system-view

Sysname l2vpn enable

Sysname vsi web

Sysname-vsi-web pbb i-sid 100

Sysname-vsi-web-100 encapsulation ethernet

【相关命令】

·**pbb i-sid**

·**vsi**

**PBB \-- PBB配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

**[l2vpn enable**]命令用来使能L2VPN功能。

**[undo l2vpn enable**]命令用来关闭L2VPN功能。

【命令】

**[l2vpn enable**]

**[undo l2vpn enable**]

【缺省情况】

L2VPN功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能L2VPN功能。

\<Sysname\> system-view

Sysname l2vpn enable

**PBB \-- PBB配置命令 \-- pbb i-sid**

------------------------------------------------------------------------

**[pbb i-sid**]命令用来创建PBB VSI实例，并进入VSI PBB视图。

**[undo pbb i-sid**]命令用来恢复缺省情况。

【命令】

**[pbb i-sid** *i-sid*]

**[undo pbb i-sid**]

【缺省情况】

未创建PBB VSI实例。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[i-sid*]：指定PBB的骨干网服务实例编号，取值范围为1～16777215。

【使用指导】

·创建PBB VSI实例就是创建一个PBB类型的VSI，并同时指定其I-SID。

·在同一个VSI视图下，PBB和SPB的I-SID不能相同。有关SPB的详细介绍，请参见"SPB配置指导"中的"SPBM"。

·在PBBN中同一PBB VSI实例必须指定相同的I-SID，不同PBB VSI实例的I-SID不能相同。

【举例】

\# 创建PBB VSI实例vpn1，其I-SID为100，并进入VSI PBB视图。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pbb i-sid 100

Sysname-vsi-vpn1-100

【相关命令】

·**display l2vpn ****minm connection**

·**display l2vpn minm forwarding**

**PBB \-- PBB配置命令 \-- pbb uplink**

------------------------------------------------------------------------

**[pbb uplink**]命令用来将接口指定为PBB VSI实例的上行口。

**[undo pbb uplink**]命令用来取消接口作为PBB VSI实例的上行口。

【命令】

**[pbb uplink **[{ **all** \| **vsi** *vsi-name-list* }]]

**[undo pbb uplink **[{ **all** \| **vsi** *vsi-name-list* }]]

【缺省情况】

接口不是任何PBB VSI实例的上行口。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：配置接口为所有VSI的上行口。

**[vsi ***vsi-name-list*]：VSI名字列表，配置接口为某个或多个VSI的上行口。表示方式为*vsi-name-list* = { *vsi-name* }&\<1-10\>。*vsi-name*为PBB VSI实例的名称，为1～31个字符的字符串，区分大小写。&\<1-10\>表示前面的参数最多可以重复输入10次。

【使用指导】

·PBB VSI实例需要指定上行口后才能够正常工作。

·若接口是所有PBB VSI实例的上行口，此时若需要将其改为某个PBB VSI实例的上行口，需先取消该接口是所有PBB VSI实例的上行口的配置，否则配置不生效；若接口是某些PBB VSI实例的上行口，此时还可以将其改为是所有PBB VSI实例的上行口。

·可以指定PBB VSI实例的名称后，再创建对应的PBB VSI实例。

·聚合接口配置为上行口时，必须所有的聚合成员端口都支持PBB。否则，配置不成功。

·聚合接口先配置为上行口，之后将某个接口加入该聚合组，若该接口不支持PBB，则该接口加入聚合成功，但是会打印日志信息提示用户该接口不支持PBB。

【举例】

\# 使能L2VPN功能，创建PBB VSI实例web和PBB VSI实例mail，将接口GigabitEthernet1/0/1、GigabitEthernet1/0/2指定为PBB VSI实例web和PBB VSI实例mail的上行口。

\<Sysname\> system-view

Sysname l2vpn enable

Sysname vsi web

Sysname-vsi-web pbb i-sid 100

Sysname-vsi-web-100 bvlan 100

Sysname-vsi-web-100 quit

Sysname-vsi-web quit

Sysname vsi mail

Sysname-vsi-mail pbb i-sid 200

Sysname-vsi-mail-200 bvlan 200

Sysname-vsi-mail-200 quit

Sysname-vsi-mail quit

Sysname interface range gigabitethernet 1/0/1 to gigabitethernet 1/0/2

Sysname-if-range pbb uplink vsi web mail

【相关命令】

·**vsi**

**PBB \-- PBB配置命令 \-- reset pbb connection**

------------------------------------------------------------------------

**[reset pbb connection**]命令用来清除PBB VSI实例的连接信息。

【命令】

**[reset pbb connection** [ *[vlan-id*[ \| **interface** ]*interface-type* *interface-number*[ } \* \| **vsi** ]*vsi-name *]]

【视图】]

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bvlan***vlan-id*]：清除指定B-VLAN内PBB VSI实例的连接信息。*vlan-id*为B-VLAN的编号，取值范围为1～4094。如果未指定该参数，将清除所有B-VLAN内PBB VSI实例的连接信息。

**[interface***interface-type* *interface-number*]：清除指定接口上PBB VSI实例的连接信息。*interface-type* *interface-number*为接口名称和接口编号。如果未指定该参数，将清除所有接口上PBB VSI实例的连接信息。

**[vsi***vsi-name*]：清除指定PBB VSI实例的连接信息。*vsi-name*为PBB VSI实例的名称，为1～31个字符的字符串，区分大小写。如果未指定该参数，将清除所有PBB VSI实例的连接信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

【使用指导】

只有PBB VSI连接信息中的单播表项可以通过本命令进行清除。

【举例】

\# 清除PBB VSI实例web的连接信息。

\<Sysname\> reset pbb connection vsi web

【相关命令】

·**display pbb connection**

**PBB \-- PBB配置命令 \-- vsi**

------------------------------------------------------------------------

**[vsi**]命令用来创建一个VSI，并进入VSI视图。如果指定的VSI已经存在，则直接进入VSI视图。

**[undo** **vsi**]命令用来删除指定的VSI。

【命令】

**[vsi**] *vsi-name*

**[undo**]**vsi** *vsi-name*

【缺省情况】

设备上不存在任何VSI。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-name*]：VSI的名称，为1～31个字符的字符串，区分大小写。

【举例】

\# 创建名为test的VSI，并进入VSI视图。

\<Sysname\> system-view

Sysname vsi test

Sysname-vsi-test

【相关命令】

·**display l2vpn vsi**

