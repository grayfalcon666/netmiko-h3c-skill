<!-- CMD-INDEX
  community-vlan vlan                 | 隔离组视图            | L8
  display port-isolate group          | 任意视图             | L68
  port-isolate enable                 |                  | L186
  port-isolate group                  | 系统视图             | L304
-->

**端口隔离 \-- 端口隔离配置命令 \-- community-vlan vlan**

------------------------------------------------------------------------

![说明](端口隔离命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[community-vlan vlan**]命令用来配置当前隔离组中的非隔离VLAN。

**[undo community-vlan**]命令用来删除当前隔离组中的所有非隔离VLAN。

【命令】

**[community-vlan vlan**[ { *vlan-id-list* \| **all** }]]

**[undo community-vlan**]

【缺省情况】

隔离组中未配置非隔离VLAN。

【视图】

隔离组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，表示设置当前隔离组中非隔离VLAN的范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*的取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

**[all**]：表示设置当前隔离组中所有的VLAN为非隔离VLAN。

【使用指导】

·本命令仅适用于运行模式为独立运行模式、或处于IRF模式但没有配置IRF增强功能的设备。

·在执行**community-vlan vlan**命令时，如果当前隔离组中已存在非隔离VLAN，必须先执行**undo community-vlan**命令（重复配置除外）。

【举例】

\# 配置隔离组1中的VLAN 3为非隔离VLAN。

\<Sysname\> system-view

Sysname port-isolate group 1

Sysname-port-isolate-group1 community-vlan vlan 3

【相关命令】

·**display port-isolate group**

**端口隔离 \-- 端口隔离配置命令 \-- display port-isolate group**

------------------------------------------------------------------------

![说明](端口隔离命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display port-isolate group**]命令用来显示隔离组的信息。

【命令】

单隔离组设备：

**[display port-isolate group**]

多隔离组设备：

**[display port-isolate group ** *group-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-number*]：隔离组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。（多隔离组设备）

【举例】

\# 显示隔离组的信息。（单隔离组设备）

\<Sysname\> display port-isolate group

 Port isolation group information:

 Group ID: 1

 Group members:

    GigabitEthernet1/0/2

 Community VLAN ID: 3

\# 显示所有隔离组的信息。（多隔离组设备）

\<Sysname\> display port-isolate group

 Port isolation group information:

 Group ID: 2

 Group members:

    GigabitEthernet1/0/1

 Group ID: 5

 Group members:

    GigabitEthernet1/0/2            GigabitEthernet1/0/4

 Community VLAN ID: 3

\# 显示隔离组2的信息。（多隔离组设备）

\<Sysname\> display port-isolate group 2

 Port isolation group information:

 Group ID: 2

 Group members:

    GigabitEthernet1/0/1

 Community VLAN ID: 1(default), 2

表1-1 display port-isolate group命令显示信息描述表

字段

描述

Port isolation group information

端口隔离组的信息

Group ID

隔离组编号

Group members

隔离组中包含的成员端口，若显示为No ports表示没有成员端口

 

Community VLAN ID

非隔离VLAN的编号（default表示缺省VLAN），若显示为None表示不存在非隔离VLAN

【相关命令】

·**port-isolate enable**

**端口隔离 \-- 端口隔离配置命令 \-- port-isolate enable**

------------------------------------------------------------------------

![说明](端口隔离命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[port-isolate enable**]命令用来将当前端口加入到隔离组中。

**[undo port-isolate enable**]命令用来将当前端口从隔离组中删除。

【命令】

单隔离组设备：

**[port-isolate enable**]

**[undo port-isolate enable**]

多隔离组设备：

**[port-isolate enable group ***group-number*]

**[undo port-isolate enable**]

【缺省情况】

当前端口未加入隔离组。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group*** group-number*]：隔离组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·二层以太网接口视图下的配置只对当前端口生效。

·二层聚合接口视图下的配置对当前接口及其成员端口生效，若某成员端口配置失败，系统会跳过该端口继续配置其他成员端口，若二层聚合接口配置失败，则不会再配置成员端口。

·同一端口不能同时配置为业务环回组成员端口和隔离组端口，即业务环回组成员端口不能加入隔离组，而隔离组成员端口不能再配置为业务环回组的成员端口。

·在端口上执行该命令，会将当前端口加入系统缺省的隔离组1中。（单隔离组设备）

·在端口上执行该命令将当前端口加入到指定的隔离组中前，必须先完成该隔离组的创建。（多隔离组设备）

·一个端口最多只能加入一个隔离组。（多隔离组设备）

【举例】

\# 将端口GigabitEthernet1/0/1和GigabitEthernet1/0/2加入隔离组。（单隔离组设备）

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-isolate enable

Sysname-GigabitEthernet1/0/1 quit

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 port-isolate enable

\# 将二层聚合接口1以及其对应的成员端口加入隔离组。（单隔离组设备）

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-aggregation group 1

Sysname-GigabitEthernet1/0/1 quit

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 port link-aggregation group 1

Sysname-GigabitEthernet1/0/2 quit

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 port-isolate enable

\# 将端口GigabitEthernet1/0/1、GigabitEthernet1/0/2加入隔离组2。（多隔离组设备）

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-isolate enable group 2

Sysname-GigabitEthernet1/0/1 quit

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 port-isolate enable group 2

【相关命令】

·**display port-isolate group**

**端口隔离 \-- 端口隔离配置命令 \-- port-isolate group**

------------------------------------------------------------------------

![说明](端口隔离命令.files/image001.png)

本命令仅多隔离组设备支持。

**[port-isolate group**]命令用来创建隔离组。

**[undo port-isolate group**]命令用来删除指定隔离组及其配置。

【命令】

**[port-isolate group ***group-number*]

**[undo port-isolate group *******[group-number*****[\| **all** }]]

【缺省情况】]

未创建任何隔离组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：隔离组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[all**]：删除所有隔离组。

【举例】

\# 创建隔离组2。

\<Sysname\> system-view

Sysname port-isolate group 2

