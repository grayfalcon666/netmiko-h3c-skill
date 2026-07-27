<!-- CMD-INDEX
  display mirroring-group             | 任意视图             | L16
  mirroring-group                     | 系统视图             | L184
  mirroring-group mirroring-cpu       |                  | L240
  mirroring-group mirroring-port (interface view) | 接口视图             | L324
  mirroring-group mirroring-port (system view) | 系统视图             | L404
  mirroring-group mirroring-vlan      | 系统视图             | L476
  mirroring-group monitor-egress      |                  | L548
  mirroring-group monitor-port (interface view) | 接口视图             | L634
  mirroring-group monitor-port (system view) | 系统视图             | L714
  mirroring-group reflector-port      |                  | L788
  mirroring-group remote-probe vlan   | 系统视图             | L880
  mirror-to                           |                  | L956
-->

**端口镜像 \-- 端口镜像配置命令 \-- display mirroring-group**

------------------------------------------------------------------------

**[display mirroring-group**]命令用来显示镜像组的信息。

【命令】

**[display mirroring-group **[{ *group-id* \| **all** \| **local** \| **remote-destination** \| **remote-source** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-id*]：显示指定镜像组的信息。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[all**]：显示所有镜像组的信息。

**[local**]：显示本地镜像组的信息。

**[remote-destination**]：显示远程目的镜像组的信息。

**[remote-source**]：显示远程源镜像组的信息。

【使用指导】

显示信息的显示顺序按照镜像组的编号顺序排列，显示内容包括镜像组的类型、状态和构成等信息。

【举例】

\# 显示所有镜像组的信息。

\<Sysname\> display mirroring-group all

Mirroring group 1:

    Type: Local

    Status: Active

    Sampler: samp (failed)

    Mirroring port:

        GigabitEthernet1/0/1  Inbound

    Monitor port: GigabitEthernet1/0/2

Mirroring group 3：

    Type: Local

    Status: Active

    Mirroring port:

        GigabitEthernet1/0/1  Inbound

        GigabitEthernet1/0/2  Both

    Mirroring VLAN:

        1-3, 5-7, 100-120, 130-1100, 1200-1300, 1400-1600, 1700-1800, 1950-2000  Inbound

        4, 8-9  Both

    Mirroring CPU:

        Slot 1, 2, 3  Both

        Slot 4  Inbound

    Monitor port: GigabitEthernet1/0/3

Mirroring group 6:

    Type: Remote source

    Status: Incomplete

    Mirroring port:

        GigabitEthernet1/0/4  Both

    Remote probe VLAN: 1900

Mirroring group 9:

    Type: Remote destination

    Status: Active

    Monitor port: GigabitEthernet1/0/6

    Remote probe VLAN: 1901

![说明](镜像命令.files/image001.png)

显示信息的内容与设备的型号有关，请以设备的实际情况为准。

表1-1  display mirroring-group命令显示信息描述表

字段

描述

Mirroring group

镜像组的编号

Type

镜像组的类型：

·Local：本地镜像组

·Remote source：远程源镜像组

·Remote destination：远程目的镜像组

Status

镜像组的状态：

·Active：表示镜像组已经生效

·Incomplete：表示镜像组没有配完，暂不生效

Sampler

采样器名称（若引用采样器失败，则在采样器名称后标识failed；若未配置引用的采样器，则不显示该字段）

Mirroring port

镜像源端口

Mirroring VLAN

镜像源VLAN

Mirroring CPU

镜像源CPU

Monitor port

镜像目的端口

Reflector port

镜像组反射端口

Remote probe VLAN

远程镜像VLAN

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group**

------------------------------------------------------------------------

**[mirroring-group**]命令用来创建一个镜像组。

**[undo mirroring-group**]命令用来删除已创建的镜像组。

【命令】

**[mirroring-group*** group-id*****[{ **local** \| **remote-destination** \| **remote-source** } [ **sampler** *sampler-name* ]]]

**[undo mirroring-group**[ { *group-id* \| **all** \| **local** \| **remote-destination** \| **remote-source** }]]

【缺省情况】

不存在任何镜像组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[local**]：表示本地镜像组。

**[remote-destination**]：表示远程目的镜像组。

**[remote-source**]：表示远程源镜像组。

**[sampler** *sampler-name*]：表示端口镜像引用的采样器。*sampler-name*为采样器的名称，为1～31个字符的字符串，不区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：表示所有镜像组。

【使用指导】

·每类镜像组可创建的数量与设备的型号有关，请以设备的实际情况为准。

·采样器用来从一组固定数量的报文中选出一个报文，端口镜像通过引用采样器，可以对镜像报文进行采样而减少镜像报文的数量。端口镜像支持引用一个未创建的采样器。如果在端口镜像多次配置采样器，新的配置将覆盖旧的配置。有关采样器的相关配置，请参见"网络管理和监控配置指导"中的"Sampler"。

【举例】

\# 创建本地镜像组1，并引用采样器samp。

\<Sysname\> system-view

Sysname mirroring-group 1 local sampler samp

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group mirroring-cpu**

------------------------------------------------------------------------

![说明](镜像命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mirroring-group mirroring-cpu**]命令用来为镜像组配置源CPU。

**[undo mirroring-group mirroring-cpu**]命令用来删除镜像组的指定源CPU。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[mirroring-group ***group-id*** mirroring-cpu slot ***slot-number-list*[ { **both** \| **inbound** \| **outbound** }]]

**[undo mirroring-group ***group-id*** mirroring-cpu slot ***slot-number-list*]

分布式设备－IRF模式：

**[mirroring-group ***group-id*** mirroring-cpu chassis**[ *chassis-number* **slot** *slot-number-list* { **both** \| **inbound** \| **outbound** }]]

**[undo mirroring-group ***group-id*** mirroring-cpu chassis** *chassis-number* **slot** *slot-number-list*]

【缺省情况】

镜像组没有源CPU。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[slot ***slot-number-list*]：源CPU所在单板的槽位号列表，表示多个槽位。表示方式为*slot-number-list *= { *slot-number* [ **to** *slot-number*  }&\<1-8\>]。其中，*slot-number*为单板所在的槽位号，&\<1-8\>表示前面的参数最多可以输入8次。当使用**to**参数配置单板范围时，终止单板的槽位号必须大于等于起始单板的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number-list*]：源CPU所在设备在IRF中的成员编号列表，表示多个成员。表示方式为*slot-number-list *= { *slot-number* [ **to** *slot-number*  }&\<1-8\>]。其中，*slot-number*为设备在IRF中的成员编号，&\<1-8\>表示前面的参数最多可以输入8次。当使用**to**参数配置设备范围时，终止设备的成员编号必须大于等于起始设备的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number-list*]：源CPU所在设备在IRF中的成员编号列表或者PEX的虚拟槽位号，表示多个成员。表示方式为*slot-number-list *= { *slot-number* [ **to** *slot-number*  }&\<1-8\>]。其中，*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号，&\<1-8\>表示前面的参数最多可以输入8次。当使用**to**参数配置设备范围时，终止设备的成员编号或者PEX的虚拟槽位号必须大于等于起始设备的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number-list*]：源CPU所在设备及单板的位置。*chassis-number*表示设备在IRF中的成员编号。*slot-number-list*表示单板的槽位号列表，表示方式为*slot-number-list *= { *slot-number* [ **to** *slot-number*  }&\<1-8\>]。其中，*slot-number*为单板所在的槽位号，&\<1-8\>表示前面的参数最多可以输入8次。当使用**to**参数配置单板范围时，终止单板的槽位号必须大于等于起始单板的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number-list*]：源CPU所在单板的位置。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号。*slot-number-list*表示单板或PEX的槽位号列表，表示方式为*slot-number-list *= { *slot-number* [ **to** *slot-number*  }&\<1-8\>]。其中，*slot-number*为单板或PEX所在的槽位号，&\<1-8\>表示前面的参数最多可以输入8次。当使用**to**参数配置单板范围时，终止单板或PEX的槽位号必须大于等于起始单板或PEX的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[both**]：表示对源CPU收发的报文都进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[inbound**]：表示仅对源CPU收到的报文进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outbound**]：表示仅对源CPU发出的报文进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

只能为本地镜像组或远程源镜像组配置源CPU，不能为远程目的镜像组配置源CPU。

【举例】

\<Sysname\> system-view

Sysname mirroring-group 1 local

Sysname mirroring-group 1 mirroring-cpu slot 1 both

\# 创建远程源镜像组2，配置其源CPU为位于2号槽位单板上的CPU，并对该CPU收发的报文都进行镜像。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname mirroring-group 2 remote-source

Sysname mirroring-group 2 mirroring-cpu slot 2 both

【相关命令】

·**mirroring-group**

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group mirroring-port (interface view)**

------------------------------------------------------------------------

**[mirroring-group******mirroring-port**]命令用来配置当前端口为镜像组的源端口。

**[undo mirroring-group******mirroring-port**]命令用来取消当前端口为镜像组的源端口。

【命令】

**[mirroring-group*** group-id ***mirroring-port**[ { **both** \| **inbound** \| **outbound** }]]

**[undo mirroring-group*** group-id*** mirroring-port**]

【缺省情况】

端口不是任何镜像组的源端口。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[both**]：表示对端口收发的报文都进行镜像。

**[inbound**]：表示仅对端口收到的报文进行镜像。

**[outbound**]：表示仅对端口发出的报文进行镜像。

【使用指导】

只能为本地镜像组或远程源镜像组配置源端口，不能为远程目的镜像组配置源端口。

对于源端口，需要注意的是：

·请不要将源端口加入到源VLAN中和远程镜像VLAN中，否则会影响镜像功能的正常使用。

·通常，一个端口只能被一个镜像组使用；而在支持多目的端口的设备上，一个端口可被多个镜像组用作源端口，但源端口不能再被用作本镜像组或其他镜像组的反射端口、出端口或目的端口。

![说明](镜像命令.files/image001.png)

·不同型号的设备支持为本地镜像组配置源端口的接口视图不同，请以设备的实际情况为准。

·不同型号的设备支持为远程源镜像组配置源端口的接口视图不同，请以设备的实际情况为准。

【举例】

\# 创建本地镜像组1，配置其源端口为GigabitEthernet1/0/1，并对该端口收发的报文都进行镜像。

\<Sysname\> system-view

Sysname mirroring-group 1 local

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mirroring-group 1 mirroring-port both

\# 创建远程源镜像组2，配置其源端口为GigabitEthernet1/0/2，并对该端口收发的报文都进行镜像。

\<Sysname\> system-view

Sysname mirroring-group 2 remote-source

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 mirroring-group 2 mirroring-port both

【相关命令】

·**mirroring-group**

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group mirroring-port (system view)**

------------------------------------------------------------------------

**[mirroring-group mirroring-port**]命令用来为镜像组配置源端口。

**[undo mirroring-group mirroring-port**]命令用来删除镜像组的指定源端口。

【命令】

**[mirroring-group ***group-id*** mirroring-port ***interface-list*[ { **both** \| **inbound** \| **outbound** }]]

**[undo mirroring-group ***group-id*** mirroring-port ***interface-list*]

【缺省情况】

镜像组没有源端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[interface-list*]：源端口列表，表示一个或多个源端口。表示方式为*interface-list *= { *interface-type interface-number* [ **to** *interface-type interface-number*  }&\<1-8\>]。其中，*interface-type interface-number*为端口类型和端口编号。&\<1-8\>表示前面的参数最多可以输入8次。当使用**to**参数配置端口范围时，起始端口和终止端口必须是相同单板上相同类型的端口，且终止端口的端口编号必须大于等于起始端口的端口编号。不同设备支持的本地镜像组源端口和远程源镜像组源端口的端口类型不同，请以设备的实际情况为准。

**[both**]：表示对端口收发的报文都进行镜像。

**[inbound**]：表示仅对端口收到的报文进行镜像。

**[outbound**]：表示仅对端口发出的报文进行镜像。

【使用指导】

只能为本地镜像组或远程源镜像组配置源端口，不能为远程目的镜像组配置源端口。

对于源端口，需要注意的是：

·请不要将源端口加入到源VLAN中和远程镜像VLAN中，否则会影响镜像功能的正常使用。

·通常，一个端口只能被一个镜像组使用；而在支持多目的端口的设备上，一个端口可被多个镜像组用作源端口，但源端口不能再被用作本镜像组或其他镜像组的反射端口、出端口或目的端口。

【举例】

\# 创建本地镜像组1，配置其源端口为GigabitEthernet1/0/1，并对该端口收发的报文都进行镜像。

\<Sysname\> system-view

Sysname mirroring-group 1 local

Sysname mirroring-group 1 mirroring-port gigabitethernet 1/0/1 both

\# 创建远程源镜像组2，配置其源端口为GigabitEthernet1/0/2，并对该端口收发的报文都进行镜像。

\<Sysname\> system-view

Sysname mirroring-group 2 remote-source

Sysname mirroring-group 2 mirroring-port gigabitethernet 1/0/2 both

【相关命令】

·**mirroring-group**

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group mirroring-vlan**

------------------------------------------------------------------------

![说明](镜像命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mirroring-group mirroring-vlan**]命令用来为镜像组配置源VLAN。

**[undo mirroring-group mirroring-vlan**]命令用来删除镜像组的指定源VLAN。

【命令】

**[mirroring-group ***group-id*** mirroring-vlan ***vlan-list*[ { **both** \| **inbound** \| **outbound** }]]

**[undo mirroring-group ***group-id*** mirroring-vlan ***vlan-list*]

【缺省情况】

镜像组没有源VLAN。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[vlan-list*]：源VLAN列表，表示一个或多个源VLAN。表示方式为*vlan-list *= { *vlan-id* [ **to** *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。当使用**to**参数配置VLAN范围时，终止VLAN的编号必须大于等于起始VLAN的编号。

**[both**]：表示对源VLAN收发的报文都进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[inbound**]：表示仅对源VLAN收到的报文进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outbound**]：表示仅对源VLAN发出的报文进行镜像。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

只能为本地镜像组或远程源镜像组配置源VLAN，不能为远程目的镜像组配置源VLAN。

需要注意的是，一个VLAN只能配置为一个镜像组的源VLAN。

【举例】

\# 创建本地镜像组1，配置其源VLAN为VLAN 1，并对该VLAN收发的报文都进行镜像。

\<Sysname\> system-view

Sysname mirroring-group 1 local

Sysname mirroring-group 1 mirroring-vlan 1 both

\# 创建远程源镜像组2，配置其源VLAN为VLAN 2，并对该VLAN收发的报文都进行镜像。

\<Sysname\> system-view

Sysname mirroring-group 2 remote-source

Sysname mirroring-group 2 mirroring-vlan 2 both

【相关命令】

·**mirroring-group**

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group monitor-egress**

------------------------------------------------------------------------

![说明](镜像命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mirroring-group monitor-egress**]命令用来为远程源镜像组配置出端口。

**[undo mirroring-group monitor-egress**]命令用来删除远程源镜像组的指定出端口。

【命令】

在系统视图下：

**[mirroring-group ***group-id*** monitor-egress ***interface-type interface-number*]

**[undo mirroring-group ***group-id*** monitor-egress ***interface-type interface-number*]

在接口视图下：

**[mirroring-group*** group-id*** monitor-egress**]

**[undo mirroring-group*** group-id*** monitor-egress**]

【缺省情况】

镜像组没有出端口。

【视图】

系统视图/接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[interface-type interface-number*]：表示出端口。其中，*interface-type interface-number*为端口类型和端口编号。

【使用指导】

只能为远程源镜像组配置出端口，不能为本地镜像组和远程目的镜像组配置出端口。

对于出端口，需要注意的是：

·请不要将出端口加入到源VLAN中，否则会影响镜像功能的正常使用。

·请不要在出端口上配置下列功能：生成树协议、802.1X、IGMP Snooping、静态ARP和MAC地址学习，否则会影响镜像功能的正常使用。

·出端口不能是现有镜像组的成员端口。

![说明](镜像命令.files/image002.png)

出端口是否可以为聚合成员端口与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 创建远程源镜像组1，并在系统视图下配置其出端口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname mirroring-group 1 remote-source

Sysname mirroring-group 1 monitor-egress gigabitethernet 1/0/1

\# 创建远程源镜像组2，并在接口视图下配置其出端口为GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname mirroring-group 2 remote-source

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 mirroring-group 2 monitor-egress

【相关命令】

·**mirroring-group**

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group monitor-port (interface view)**

------------------------------------------------------------------------

**[mirroring-group******monitor-port**]命令用来配置当前端口为镜像组的目的端口。

**[undo mirroring-group******monitor-port**]命令用来取消当前端口为指定镜像组的目的端口。

【命令】

**[mirroring-group*** group-id ***monitor-port**]

**[undo** **mirroring-group** *group-id* **monitor-port**]

【缺省情况】

端口不是任何镜像组的目的端口。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：指定镜像组。*group-id*表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

只能为本地镜像组或远程目的镜像组配置目的端口，不能为远程源镜像组配置目的端口。

对于目的端口，需要注意的是：

·请不要将目的端口加入到源VLAN中，或在目的端口上使能生成树协议，否则会影响镜像功能的正常使用。

·当二层聚合接口作为目的端口时，请勿将其成员端口配置为源端口或将其加入源VLAN，否则会影响镜像功能的正常使用。

·从目的端口发出的报文包括镜像报文和其他端口正常转发来的报文。为了保证数据监测设备只对镜像报文进行分析，请将目的端口只用于端口镜像，不作其他用途。

·目的端口不能是现有镜像组的成员端口。

![说明](镜像命令.files/image001.png)

·不同型号的设备支持为本地镜像组配置目的端口的接口视图不同，请以设备的实际情况为准。

·不同型号的设备支持为远程目的镜像组配置目的端口的接口视图不同，请以设备的实际情况为准。

·目的端口是否可以为聚合成员端口，以及目的端口还存在其他何种限制与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 创建本地镜像组1，并配置其目的端口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname mirroring-group 1 local

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mirroring-group 1 monitor-port

\# 创建远程目的镜像组2，并配置其目的端口为GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname mirroring-group 2 remote-destination

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 mirroring-group 2 monitor-port

【相关命令】

·**mirroring-group**

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group monitor-port (system view)**

------------------------------------------------------------------------

**[mirroring-group monitor-port**]命令用来为镜像组配置目的端口。

**[undo mirroring-group monitor-port**]命令用来删除镜像组的指定目的端口。

【命令】

**[mirroring-group ***group-id*** monitor-port ***interface-type interface-number*]

**[undo mirroring-group ***group-id*** monitor-port ***interface-type interface-number*]

【缺省情况】

镜像组没有目的端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[interface-type interface-number*]：表示目的端口。其中，*interface-type interface-number*为端口类型和端口编号。不同设备支持的本地镜像组目的端口和远程目的镜像组目的端口的端口类型不同，请以设备的实际情况为准。

【使用指导】

只能为本地镜像组或远程目的镜像组配置目的端口，不能为远程源镜像组配置目的端口。

对于目的端口，需要注意的是：

·请不要将目的端口加入到源VLAN中，或在目的端口上使能生成树协议，否则会影响镜像功能的正常使用。

·当二层聚合接口作为目的端口时，请勿将其成员端口配置为源端口或将其加入源VLAN，否则会影响镜像功能的正常使用。

·从目的端口发出的报文包括镜像报文和其他端口正常转发来的报文。为了保证数据监测设备只对镜像报文进行分析，请将目的端口只用于端口镜像，不作其他用途。

·目的端口不能是现有镜像组的成员端口。

![说明](镜像命令.files/image003.png)

目的端口是否可以为聚合成员端口，以及目的端口还存在其他何种限制，与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 创建本地镜像组1，并配置其目的端口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname mirroring-group 1 local

Sysname mirroring-group 1 monitor-port gigabitethernet 1/0/1

\# 创建远程目的镜像组2，并配置其目的端口为GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname mirroring-group 2 remote-destination

Sysname mirroring-group 2 monitor-port gigabitethernet 1/0/2

【相关命令】

·**mirroring-group**

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group reflector-port**

------------------------------------------------------------------------

![说明](镜像命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mirroring-group reflector-port**]命令用来为远程源镜像组配置反射端口。

**[undo mirroring-group reflector-port**]命令用来删除远程源镜像组的指定反射端口。

【命令】

在系统视图下：

**[mirroring-group ***group-id*** reflector-port ***interface-type interface-number*]

**[undo mirroring-group ***group-id*** reflector-port ***interface-type interface-number*]

在接口视图下：

**[mirroring-group*** group-id*** reflector-port**]

**[undo mirroring-group*** group-id*** reflector-port**]

【缺省情况】

镜像组没有反射端口，端口不是任何镜像组的反射端口。

【视图】

系统视图/接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[interface-type interface-number*]：表示反射端口。其中，*interface-type interface-number*为端口类型和端口编号。

【使用指导】

只能为远程源镜像组配置反射端口，不能为本地镜像组和远程目的镜像组配置反射端口。

对于反射端口，需要注意的是：

·请不要将反射端口加入到源VLAN中，否则会影响镜像功能的正常使用。

·建议选择设备上未被使用的端口作为反射端口，并不要在该端口上连接网线，否则会影响镜像功能的正常使用。

·在将端口配置为反射端口时，该端口上已存在的所有配置都将被清除；在配置为反射端口后，该端口上不能再配置其他业务。

·对于某些型号的设备，只有当端口的双工模式、端口速率和MDI属性值均为缺省值时，才能将其配置为反射端口，请以设备的实际情况为准。当端口已配置为反射端口后，不能再修改其双工模式、端口速率和MDI属性值，即这些属性只能取缺省值。

![说明](镜像命令.files/image002.png)

反射端口是否可以为聚合成员端口与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 创建远程源镜像组1，并在系统视图下配置其反射端口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname mirroring-group 1 remote-source

Sysname mirroring-group 1 reflector-port gigabitethernet 1/0/1

This operation may delete all settings made on the interface. Continue? [Y/N: y]

\# 创建远程源镜像组2，并在接口视图下配置其反射端口为GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname mirroring-group 2 remote-source

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 mirroring-group 2 reflector-port

This operation may delete all settings made on the interface. Continue? [Y/N: y]

【相关命令】

·**mirroring-group**

**端口镜像 \-- 端口镜像配置命令 \-- mirroring-group remote-probe vlan**

------------------------------------------------------------------------

![说明](镜像命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mirroring-group remote-probe vlan**]命令用来为镜像组配置远程镜像VLAN。

**[undo mirroring-group remote-probe vlan**]命令用来删除镜像组的指定远程镜像VLAN。

【命令】

**[mirroring-group ***group-id ***remote-probe vlan ***vlan-id*]

**[undo mirroring-group ***group-id ***remote-probe vlan ***vlan-id*]

【缺省情况】

镜像组没有远程镜像VLAN。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示镜像组的编号，该镜像组必须存在。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[vlan-id*]：表示远程镜像VLAN的编号。

【使用指导】

只有为远程源镜像组和远程目的镜像组配置远程镜像VLAN，不能为本地镜像组配置远程镜像VLAN。

对于远程镜像VLAN，需要注意的是：

·当一个VLAN已被指定为远程镜像VLAN后，请不要将该VLAN再作其他用途。

·源设备和目的设备上的远程镜像组必须使用相同的远程镜像VLAN。

·只能将已存在的静态VLAN配置为远程镜像VLAN，且一个VLAN只能配置为一个镜像组的远程镜像VLAN。

·当某VLAN被配置为远程镜像VLAN后，必须先删除远程镜像VLAN的配置才能删除该VLAN。

【举例】

\# 创建远程源镜像组1，并为其配置远程镜像VLAN为VLAN 10。

\<Sysname\> system-view

Sysname mirroring-group 1 remote-source

Sysname mirroring-group 1 remote-probe vlan 10

\# 创建远程目的镜像组2，并为其配置远程镜像VLAN为VLAN 20。

\<Sysname\> system-view

Sysname mirroring-group 2 remote-destination

Sysname mirroring-group 2 remote-probe vlan 20

【相关命令】

·**mirroring-group**

\

**流镜像 \-- 流镜像配置命令 \-- mirror-to**

------------------------------------------------------------------------

![说明](镜像命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mirror-to**]命令用来在流行为中配置流量的目的地。

**[undo mirror-to**]命令用来取消流行为中流量的目的地的配置。

【命令】

集中式设备：

**[mirror-to**[ { **cpu** \| **interface** *interface-type* *interface-number* [ **backup-interface** *interface-type* *interface-number* ]  **sampler** *sampler-name*  \| **vlan** *vlan-id* }]]

**[undo mirror-to**[ { **cpu** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* }]]

分布式设备－独立运行模式/集中式IRF设备：

**[mirror-to**[ { **cpu** \| { **interface** *interface-type* *interface-number* [ **backup-interface** *interface-type* *interface-number* ] \| **slot** *slot-number*  **backup slot** *slot-number*  }  **sampler** *sampler-name*  \| **vlan** *vlan-id* }]]

**[undo mirror-to**[ { **cpu** \| **interface** *interface-type* *interface-number* \| **slot** *slot-number* \| **vlan** *vlan-id* }]]

分布式设备－IRF模式：

**[mirror-to**[ { **cpu** \| { **interface** *interface-type* *interface-number* [ **backup-interface** *interface-type* *interface-number* ] \| **chassis** *chassis-number* **slot** *slot-number*  **backup chassis** *chassis-number* **slot** *slot-number*  }  **sampler** *sampler-name*  \| **vlan** *vlan-id* }]]

**[undo mirror-to**[ { **cpu** \| **interface** *interface-type* *interface-number* \| **chassis** *chassis-number* **slot** *slot-number* \| **vlan** *vlan-id* }]]

【缺省情况】

流行为中未配置流量的目的地。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cpu**]：表示流镜像到CPU，这里的CPU是指报文进入的单板上的CPU。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface** *interface-type* *interface-number*]：表示流镜像到指定接口，*interface-type* *interface-number*为接口类型和接口编号。本参数的支持情况以及支持的接口类型都与设备的型号有关，请以设备的实际情况为准。

**[backup-interface** *interface-type* *interface-number*]：表示流镜像的备份接口，*interface-type* *interface-number*为接口类型和接口编号。只有当**interface** *interface-type* *interface-number*参数指定的接口出现故障时，流量才可以被镜像到备份接口。本参数的支持情况以及支持的接口类型都与设备的型号有关，请以设备的实际情况为准。

**[sampler** *sampler-name*]：表示流镜像引用的采样器，*sampler-name*为采样器的名称，为1～31个字符的字符串，不区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan** *vlan-id*]：表示流镜像到指定VLAN，*vlan-id*为VLAN的编号，取值范围为1～4094。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot ***slot-number*]：表示流镜像到指定单板。*slot-number*为单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示流镜像到指定成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示流镜像到指定成员设备/PEX。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[backup slot ***slot-number*]：表示流镜像的备份单板。*slot-number*为单板所在的槽位号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式）

**[backup slot ***slot-number*]：表示流镜像的备份成员设备。*slot-number*为设备在IRF中的成员编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（集中式IRF设备）（不支持IRF3的设备）

**[backup slot ***slot-number*]：表示流镜像的备份成员设备/PEX。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：表示流镜像到指定成员设备的指定单板。*chassis-number*为设备在IRF中的成员编号，*slot-number*为单板所在的槽位号。（分布式设备-IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：表示流镜像到指定单板。*chassis-number*为设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*为单板或PEX所在的槽位号。（分布式设备-IRF模式）（支持IRF3的设备）

**[backup chassis ***chassis-number*** slot ***slot-number*]：表示流镜像的指定成员设备的备份单板。*chassis-number*为设备在IRF中的成员编号，*slot-number*为单板所在的槽位号。本参数的支持情况以及支持的接口类型都与设备的型号有关，请以设备的实际情况为准。（分布式设备-IRF模式）（不支持IRF3的设备）

**[backup chassis ***chassis-number*** slot ***slot-number*]：表示流镜像的备份单板。*chassis-number*为设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*为单板或PEX所在的槽位号。本参数的支持情况以及支持的接口类型都与设备的型号有关，请以设备的实际情况为准。（分布式设备-IRF模式）（支持IRF3的设备）

【使用指导】

·如果设备支持流镜像到多个接口，则在同一流行为中可以通过多次配置将流镜像到不同接口；如果设备只支持流镜像到一个接口，则在同一流行为中新的配置将覆盖旧的配置。是否支持流镜像到多个接口与设备的型号有关，请以设备的实际情况为准。

·如果在同一流行为中多次配置流镜像到VLAN，新的配置将覆盖旧的配置。

·采样器用来从一组固定数量的报文中选出一个报文。流镜像通过引用采样器，可以对镜像报文进行采样而减少镜像报文的数量。流镜像支持引用一个未创建的采样器。如果在流镜像多次配置采样器，新的配置将覆盖旧的配置。有关采样器的相关配置，请参见"网络管理和监控配置指导"中的"Sampler"。

·如果设备支持流镜像到多个单板，则在同一流行为中可以通过多次配置将流镜像到不同单板；如果设备只支持流镜像到一个单板，则在同一流行为中新的配置将覆盖旧的配置。（分布式设备－独立运行模式/分布式设备-IRF模式）

·如果设备支持流镜像到多台设备，则在同一流行为中可以通过多次配置将流镜像到不同设备；如果设备只支持流镜像到一台设备，则在同一流行为中新的配置将覆盖旧的配置。（集中式IRF设备）

【举例】

\# 配置流行为1，并在该流行为中配置流镜像到CPU。

\<Sysname\> system-view

Sysname traffic behavior 1

Sysname-behavior-1 mirror-to cpu

\# 配置流行为1，并在该流行为中配置流镜像到接口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname traffic behavior 1

Sysname-behavior-1 mirror-to interface gigabitethernet 1/0/1

\# 配置流行为1，并在该流行为中配置流镜像到VLAN 100。

\<Sysname\> system-view

Sysname traffic behavior 1

Sysname-behavior-1 mirror-to vlan 100

\# 配置流行为1，在该流行为中配置流镜像到接口GigabitEthernet1/0/1并引用采样器samp。

\<Sysname\> system-view

Sysname traffic behavior 1

Sysname-behavior-1 mirror-to interface gigabitethernet 1/0/1 sampler samp

\# 配置流行为1，在该流行为中配置流镜像到单板1并引用采样器samp。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname traffic behavior 1

Sysname-behavior-1 mirror-to slot 1 sampler samp

