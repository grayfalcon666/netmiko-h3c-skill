<!-- CMD-INDEX
  display ip urpf                     | 任意视图             | L8
  ip urpf                             | 系统视图/接口视图        | L128
  display ipv6 urpf                   | 任意视图             | L224
  ipv6 urpf                           | 系统视图/接口视图        | L336
-->

**IPv4 uRPF \-- IPv4 uRPF配置命令 \-- display ip urpf**

------------------------------------------------------------------------

![说明](uRPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **ip** **urpf**]命令用来显示uRPF的配置应用情况。

【命令】

集中式设备：

**[display** **ip** **urpf**  **interface** *interface-type* *interface-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **ip** **urpf**  **interface** *interface-type* *interface-number* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display** **ip** **urpf**  **interface** *interface-type* *interface-number* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type* *interface-number*]：接口类型和接口编号。

**[slot*** slot-number*]：显示指定单板上的uRPF配置应用情况。*slot-number*表示单板的槽位号。如果未指定本参数，则显示所有单板上的uRPF配置应用情况。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备uRPF配置应用情况。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的uRPF配置应用情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的uRPF配置应用情况。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的uRPF配置应用情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板上的uRPF配置应用情况。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。如果未指定本参数，则显示所有单板上的uRPF配置应用情况。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的uRPF配置应用情况。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号。如果未指定本参数，则显示所有单板上的uRPF配置应用情况。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的uRPF配置应用情况。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示单板slot 3上uRPF的应用情况。（分布式设备－独立运行模式）

\<Sysname\> display ip urpf slot 3

Global uRPF configuration information(failed):

   Check type: strict

   Allow default route

\# 显示接口GigabitEthernet1/0/1上已经应用的uRPF的配置情况。（集中式设备）

\<Sysname\> display ip urpf interface gigabitethernet 1/0/1

uRPF configuration information of interface GigabitEthernet1/0/1:

   Check type: strict

   Allow default route

   Link check

   Suppress drop ACL: 3000

表1-1 display ip urpf命令显示信息描述表

字段

描述

Global uRPF configuration information

全局uRPF配置应用情况

uRPF configuration information of interface

接口uRPF配置应用情况

(failed)

当前uRPF配置下发转发芯片失败，原因可能为芯片资源不足。没有该字段时表示下发成功

Check type

uRPF检查类型，包括：

·**loose**：松散型检查

·**strict**：严格型检查

Allow default route

允许缺省路由

Link check

使能**link-check**功能

Suppress drop ACL

配置了抑制丢弃，显示配置的ACL规则号

\

**IPv4 uRPF \-- IPv4 uRPF配置命令 \-- ip urpf**

------------------------------------------------------------------------

![说明](uRPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip** **urpf**]命令用来打开uRPF功能。

**[undo** **ip** **urpf**]命令用来关闭uRPF功能。

【命令】

**[ip** **urpf** { **loose** [ **allow-default-route**   **acl** *acl-number*  \| **strict**  **allow-default-route**   **acl** *acl-number*   **link-check**  }]]

**[undo** **ip** **urpf**]

【缺省情况】

uRPF功能处于关闭状态。

【视图】

系统视图/接口视图

![说明](uRPF命令.files/image001.png)

同一设备只能支持一种视图，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[loose**]：松散型检查。仅检查报文的源地址是否在转发表中存在，而不再检查报文的入接口与转发表是否匹配。

**[strict**]：严格型检查。不仅检查报文的源地址是否在转发表中存在，而且检查报文的入接口与转发表是否匹配。

**[allow-default-route**]：允许源地址查转发表时匹配缺省路由表项。

**[acl** *acl-number*]：访问控制列表，用来抑制报文丢弃。*acl-number*表示指定的ACL规则号，取值范围为2000～3999。其中：

·基本ACL的ACL规则号取值范围为2000～2999。

·高级ACL的ACL规则号取值范围为3000～3999。

**[link-check**]：允许对链路信息进行检查。目前仅支持以太网链路。

![说明](uRPF命令.files/image001.png)

各参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

uRPF功能一般部署在运营商网络接入客户侧设备的边缘位置，也可以部署在运营商网络对接其他运营商设备的边缘位置设备或部署在客户侧边缘位置设备。

建议在运营商网络接入客户侧设备的边缘位置的接口下配置严格uRPF，在运营商网络对接其他运营商网络的边缘位置的接口下配置松散uRPF。如果运营商是用一个三层以太网接口接入大量PC机用户时，建议接口下配置**link-check**功能。

选择严格或松散uRPF取决于当前组网中是否存在非对称路径，如果运营商设备上行流量的入接口和下行流量的出接口相同则是对称路径，此时建议用严格uRPF。一般运营商接入客户侧的组网中都是对称路径。运营商对接其他运营商的边缘位置可能出现非对称路径，此时建议用松散uRPF。

运营商网络边缘位置一般不会有缺省路由指向客户侧设备，所以一般不需要配置**allow-default-route**。如果在客户侧边缘设备接口上面启用uRPF，这时往往会有缺省路由指向运营商，此时需要配置**allow-default-route**。

配置**link-check**后，设备会根据源地址查转发表得到的下一跳后进一步查ARP表项来确定源MAC地址是否正确。如果运营商是用以太网接口接入客户，此时一个接口同时接多个不同客户，因此建议接口下配置**link-check**功能。

【举例】

\# 在全局下配置严格型uRPF检查。

\<Sysname\>system-view

Sysnameip urpf strict

\# 在接口GigabitEthernet1/0/2上配置严格型uRPF检查，同时允许匹配缺省路由，并配置ACL规则号为2999。

\<Sysname\>system-view

Sysnameinterface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2ip urpf strict allow-default-route acl 2999

\# 在接口GigabitEthernet1/0/1上配置松散型uRPF检查。

\<Sysname\>system-view

Sysnameinterface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1ip urpf loose

【相关命令】

·**display** **ip** **urpf**

**IPv6 uRPF \-- IPv6 uRPF配置命令 \-- display ipv6 urpf**

------------------------------------------------------------------------

![说明](uRPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display ipv6 urpf**]命令用来显示IPv6 uRPF的配置应用情况。

【命令】

集中式设备：

**[display ipv6 urpf ** **interface** *interface-type* *interface-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 urpf ** **interface** *interface-type* *interface-number* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display ipv6 urpf ** **interface** *interface-type* *interface-number* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type* *interface-number*]：接口类型和接口编号。

**[slot*** slot-number*]：显示指定单板IPv6 uRPF配置应用情况。*slot-number*表示单板的槽位号。如果未指定本参数，则显示所有单板上的IPv6 uRPF配置应用情况。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备IPv6 uRPF配置应用情况。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6 uRPF配置应用情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的IPv6 uRPF配置应用情况。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6 uRPF配置应用情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板上的IPv6 uRPF配置应用情况。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。如果未指定本参数，则显示所有单板上的IPv6 uRPF配置应用情况。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的IPv6 uRPF配置应用情况。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号。如果未指定本参数，则显示所有单板上的IPv6 uRPF配置应用情况。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的IPv6 uRPF配置应用情况。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示单板slot 3上IPv6 uRPF的应用情况。（分布式设备－独立运行模式）

\<Sysname\> display ipv6 urpf slot 3

Global IPv6 uRPF configuration information(failed):

   Check type: strict

   Allow default route

\# 显示接口GigabitEthernet1/0/1上的已经应用的IPv6 uRPF的配置情况。（集中式设备）

\<Sysname\> display ipv6 urpf interface gigabitethernet 1/0/1

IPv6 uRPF configuration information of interface GigabitEthernet1/0/1:

   Check type: loose

   Allow default route

   Suppress drop ACL: 2000

表2-1 display ipv6 urpf命令显示信息描述表

字段

描述

Global IPv6 uRPF configuration information

全局IPv6 uRPF配置应用情况

IPv6 uRPF configuration information of interface

接口IPv6 uRPF配置应用情况

(failed)

当前IPv6 uRPF配置下发转发芯片失败，原因可能为芯片资源不足。没有该字段时表示下发成功

Check type

IPv6 uRPF检查类型，包括：

·**loose**：松散型检查

·**strict**：严格型检查

Allow default route

允许缺省路由

Suppress drop ACL

配置了抑制丢弃，显示配置的IPv6 ACL规则号

**IPv6 uRPF \-- IPv6 uRPF配置命令 \-- ipv6 urpf**

------------------------------------------------------------------------

![说明](uRPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 urpf**]命令用来打开IPv6 uRPF功能。

**[undo ipv6 urpf**]命令用来关闭IPv6 uRPF功能。

【命令】

**[ipv6 urpf**[ { **loose** \| **strict** } [ **allow-default-route** ]  **acl** *acl-number* ]]

**[undo ipv6 urpf**]

【缺省情况】

IPv6 uRPF功能处于关闭状态。

【视图】

系统视图/接口视图

![说明](uRPF命令.files/image001.png)

同一设备只能支持一种视图，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[loose**]：松散型检查。仅检查报文的源地址是否在IPv6转发表中存在，而不再检查报文的入接口与IPv6转发表是否匹配。

**[strict**]：严格型检查。不仅检查报文的源地址是否在IPv6转发表中存在，而且检查报文的入接口与IPv6转发表是否匹配。

**[allow-default-route**]：允许源地址查IPv6转发时匹配缺省路由表项。

**[acl*** acl-number*]：访问控制列表，用来抑制报文丢弃。*acl-number*表示指定的ACL规则号，取值范围为2000～3999。其中：

·基本ACL的ACL规则号取值范围为2000～2999。

·高级ACL的ACL规则号取值范围为3000～3999。

![说明](uRPF命令.files/image001.png)

各参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

IPv6 uRPF功能一般部署在运营商网络接入客户侧设备的边缘位置，也可以部署在运营商网络对接其他运营商设备的边缘位置设备或部署在客户侧边缘位置设备。

建议在运营商网络接入客户侧设备的边缘位置的接口下配置严格IPv6 uRPF，在运营商网络对接其他运营商网络的边缘位置的接口下配置松散IPv6 uRPF。

选择严格或松散IPv6 uRPF取决于当前组网中是否存在非对称路径，如果运营商设备上行流量的入接口和下行流量的出接口相同则是对称路径，此时建议用严格IPv6 uRPF。一般运营商接入客户侧的组网中都是对称路径。运营商对接其他运营商的边缘位置可能出现非对称路径，此时建议用松散IPv6 uRPF。

运营商网络边缘位置一般不会有缺省路由指向客户侧设备，所以一般不需要配置**allow-default-route**。如果在客户侧边缘设备接口上面启用IPv6 uRPF，这时往往会有缺省路由指向运营商，此时需要配置**allow-default-route**。

【举例】

\# 在全局下配置严格型IPv6 uRPF检查。

\<Sysname\>system-view

Sysnameipv6 urpf strict

\# 在接口GigabitEthernet1/0/2上配置严格型IPv6 uRPF检查，同时允许匹配缺省路由，并配置ACL规则号为2999。

\<Sysname\>system-view

Sysnameinterface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2ipv6 urpf strict allow-default-route acl 2999

\# 在接口GigabitEthernet1/0/1上配置松散IPv6 uRPF检查。

\<Sysname\>system-view

Sysnameinterface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1ipv6 urpf loose

【相关命令】

·**display** **ipv6** **urpf**
