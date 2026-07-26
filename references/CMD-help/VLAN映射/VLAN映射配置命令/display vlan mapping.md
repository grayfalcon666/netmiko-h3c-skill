
**VLAN映射 \-- VLAN映射配置命令 \-- display vlan mapping**

------------------------------------------------------------------------

**[display vlan mapping**]命令用来显示VLAN映射信息。

【命令】

**[display vlan mapping **\**[interface*** interface-type interface-number *]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口的VLAN映射信息，*interface-type interface-number*为接口类型和接口编号。如果未指定该参数，将显示所有接口的VLAN映射信息。

【举例】

\# 显示所有接口上的VLAN映射信息。

\<Sysname\> display vlan mapping

Interface GigabitEthernet1/0/1:

  Outer VLAN    Inner VLAN    Translated Outer VLAN    Translated Inner VLAN

  10            N/A           120                      N/A

Interface GigabitEthernet1/0/2:

  Outer VLAN    Inner VLAN    Translated Outer VLAN    Translated Inner VLAN

  4-4094        N/A           100                      N/A

Interface GigabitEthernet1/0/3:

  Outer VLAN    Inner VLAN    Translated Outer VLAN    Translated Inner VLAN

  12            N/A           110                      12

Interface GigabitEthernet1/0/4:

  Outer VLAN    Inner VLAN    Translated Outer VLAN    Translated Inner VLAN

  11            30            130                      40

表1-1 display vlan mapping命令显示信息描述表

字段

描述

Interface

接口信息

Outer VLAN

原始外层VLAN

当显示信息中Inner VLAN显示为N/A，此时Outer VLAN表示原始VLAN

Inner VLAN

原始内层VLAN

对于1:1 VLAN映射、N:1 VLAN映射和1:2 VLAN映射，显示信息中Inner VLAN无意义，显示为N/A

Translated Outer VLAN

转换后的外层VLAN

当显示信息中Translated Inner VLAN显示为N/A，此时Translated Outer VLAN表示转换后VLAN

Translated Inner VLAN

转换后的内层VLAN

对于1:1 VLAN映射和N:1 VLAN映射，显示信息中Translated Inner VLAN无意义，显示为N/A

【相关命令】

·**vlan mapping**

**VLAN映射 \-- VLAN映射配置命令 \-- vlan mapping**

------------------------------------------------------------------------

![说明](VLAN映射命令.files/image001.png)

本命令的参数支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan mapping**]命令用来在接口上配置VLAN映射。

**[undo vlan mapping**]命令用来取消VLAN映射配置。

【命令】

**[vlan mapping **[{ *vlan-id* **translated-vlan** *vlan-id* \| **nest** { **range** *vlan-range-list* \| **single** *vlan-id-list* } **nested-vlan** *vlan-id* \| **nni** \| **tunnel** *outer-vlan-id inner-vlan-id* **translated-vlan** *outer-vlan-id inner-vlan-id* \| **uni** { **range** *vlan-range-list* \| **single** *vlan-id-list* } **translated-vlan** *vlan-id* }]]

**[undo vlan mapping **[{ *vlan-id* **translated-vlan** *vlan-id* \| **all** \| **nest** { **range** *vlan-range-list* \| **single** *vlan-id-list* } **nested-vlan** *vlan-id* \| **nni** \| **tunnel** *outer-vlan-id inner-vlan-id* **translated-vlan** *outer-vlan-id inner-vlan-id* \| **uni** { **range** *vlan-range-list* \| **single** *vlan-id-list* } **translated-vlan** *vlan-id* }]]

【缺省情况】

接口上未配置VLAN映射。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*** translated-vlan*** vlan-id*]：表示1:1 VLAN映射的原始VLAN ID和转换后的VLAN ID。*vlan-id*取值范围为1～4094。原始VLAN ID和转换后的VLAN ID不允许相同。

**[uni** **range** *vlan-range-list* **translated-vlan** *vlan-id*]：表示N:1 VLAN映射的用户侧配置，指定映射的原始VLAN段列表和转换后的VLAN ID。其中*vlan-range-list* = { *vlan-id1* **to** *vlan-id2* }&\<1-10\>，*vlan*-*id2*的值要大于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。参数涉及的*vlan-id*取值范围都为1～4094。不同VLAN段之间不允许出现交叉重叠。原始VLAN与转换后VLAN不允许相同。

**[uni single** *vlan-id-list* **translated-vlan** *vlan-id*]：表示N:1 VLAN映射的用户侧配置，指定映射的原始VLAN ID列表和转换后的VLAN ID。其中*vlan-id-list* = { *vlan-id* }&\<1-10\>，&\<1-10\>表示前面的参数最多可以重复输入10次。参数涉及的*vlan-id*取值范围都为1～4094。原始VLAN与转换后VLAN不允许相同。

**[nni**]：表示N:1 VLAN映射的网络侧配置，用于指导网络侧发往用户侧的流量进行三层转发，并将报文的VLAN Tag替换为对应的N:1 VLAN映射前的VLAN Tag。

**[nest range** *vlan-range-list* **nested-vlan** *vlan-id*]：表示1:2 VLAN映射的原始VLAN段列表和添加的外层VLAN ID。其中*vlan-range-list* = { *vlan-id1* **to** *vlan-id2* }&\<1-10\>，*vlan*-*id2*的值要大于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。参数涉及的*vlan-id*取值范围都为1～4094。不同VLAN段之间不允许出现交叉重叠。

**[nest single*** vlan-id-list*** nested-vlan*** vlan-id*]：表示1:2 VLAN映射的原始VLAN ID列表和添加的外层VLAN ID。其中*vlan-id-list* = { *vlan-id* }&\<1-10\>，&\<1-10\>表示前面的参数最多可以重复输入10次。参数涉及的*vlan-id*取值范围都为1～4094。

**[tunnel*** outer-vlan-id inner-vlan-id ***translated-vlan*** outer-vlan-id inner-vlan-id*]：表示2:2 VLAN映射的原始外层VLAN ID、内层VLAN ID和转换后的外层VLAN ID、内层VLAN ID。*outer-vlan-id*和*inner-vlan-id*的取值范围为1～4094。

**[all**]：表示删除接口上所有的VLAN映射配置。

【使用指导】

·同一接口上不同类型映射表项的原始VLAN及转换后VLAN不允许重复；同一类型映射表项中，1:1或2:2 VLAN映射表项的转换后VLAN不允许重复，若1:1或2:2 VLAN映射表项的原始VLAN重复，则以最新配置为准。

·同一接口上透传VLAN和映射表项的原始VLAN及转换后VLAN（对于携带两层VLAN Tag的报文，原始VLAN及转换后VLAN都仅指外层VLAN）不允许相同。有关透传VLAN的详细介绍，请参见"二层技术-以太网交换配置指导"中的"QinQ"。

·如果N:1 VLAN映射用户侧配置和网络侧配置不成对配置，则N:1 VLAN映射功能不能正确执行。同一个接口不能同时配置为N:1 VLAN映射的用户侧接口和网络侧接口。接口配置为N:1 VLAN映射网络侧接口后，不建议再配置其他类型的映射表项。

·开启或关闭QinQ功能之前，要先清除已有的VLAN映射表项。

·QinQ功能和2:2 VLAN映射功能互斥。开启QinQ功能后，接口只能识别一层VLAN Tag，所以该接口无法再实现2:2 VLAN映射功能。

·配置N:1 VLAN映射时需要注意的是，该功能不能与uRPF（Unicast Reverse Path Forwarding，单播反向路径转发）功能同时使用，否则会造成网络侧发往用户侧的流量不能正常转发。有关uRPF的详细介绍，请参见"安全配置指导"中的"uRPF"。

·配置1:2 VLAN映射时需要注意的是，1:2 VLAN映射为报文加上外层VLAN Tag后，内层VLAN Tag将被当作报文的数据部分进行传输，报文长度将增加4个字节。因此建议用户适当增加映射后报文传输路径上各接口的MTU（Maximum Transmission Unit，最大传输单元）值（至少为1504字节）。

·VLAN映射功能只对接口收到的携带VLAN Tag的报文生效。

【举例】

\# 在接口GigabitEthernet1/0/1上配置1:1 VLAN映射：原始VLAN为1，映射后VLAN为101。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vlan mapping 1 translated-vlan 101

\# 将接口GigabitEthernet1/0/2配置为N:1 VLAN映射用户侧接口：原始VLAN范围为1～50、80，映射后VLAN为101。同时将接口GigabitEthernet1/0/3配置为N:1 VLAN映射网络侧接口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 vlan mapping uni range 1 to 50 translated-vlan 101

Sysname-GigabitEthernet1/0/2 vlan mapping uni single 80 translated-vlan 101

Sysname-GigabitEthernet1/0/2 quit

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 vlan mapping nni

\# 在接口GigabitEthernet1/0/4上配置1:2 VLAN映射：原始VLAN范围为1～10、80，映射后添加的外层VLAN为101。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/4

Sysname-GigabitEthernet1/0/4 vlan mapping nest range 1 to 10 nested-vlan 101

Sysname-GigabitEthernet1/0/4 vlan mapping nest single 80 nested-vlan 101

\# 在接口GigabitEthernet1/0/5上配置2:2 VLAN映射：原始外层VLAN为101、内层VLAN为1，映射后外层VLAN为201、内层VLAN为10。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/5

Sysname-GigabitEthernet1/0/5 vlan mapping tunnel 101 1 translated-vlan 201 10

【相关命令】

·**display vlan mapping**

