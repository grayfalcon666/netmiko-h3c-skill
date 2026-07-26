
**DCN \-- DCN配置命令 \-- auto-report**

------------------------------------------------------------------------

**[auto-report**]命令用来开启网元上下线自动上报功能。

**[undo auto-report**]命令用来关闭网元上下线自动上报功能。

【命令】

**[auto-report**]

**[undo auto-report**]

【缺省情况】

网元上下线自动上报功能处于关闭状态。

【视图】

DCN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启网元上下线自动上报功能。

\<Sysname\> system-view

Sysname dcn

Sysname-dcn auto-report

**DCN \-- DCN配置命令 \-- dcn**

------------------------------------------------------------------------

**[dcn**]命令用来开启DCN功能，并进入DCN视图。

**[undo dcn**]命令用来关闭DCN功能。

【命令】

**[dcn**]

**[undo dcn**]

【缺省情况】

DCN功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启DCN功能后，网元信息将在OSPF扩展的10类LSA中携带，并在OSPF区域内扩散，自动生成网元信息，从而实现设备的互通。

关闭DCN功能后，设备将不生成对应OSPF的10类LSA。

【举例】

\# 开启DCN功能，并进入DCN视图。

\<Sysname\> system-view

Sysname dcn

Sysname-dcn

**DCN \-- DCN配置命令 \-- display dcn**

------------------------------------------------------------------------

**[display dcn**]命令用来显示本地设备上的DCN概要信息。

【命令】

**[display dcn**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示本地设备上的DCN概要信息。

\<Sysname\> display dcn

              DCN Brief Information

 NE ID        : 0x5801

 NE IP        : 129.0.88.1

 Mask         : 255.255.255.255

 DCN interface: LoopBack1023

 Auto report  : Enabled

表1-1 display dcn命令显示信息描述表

字段

描述

NE ID

网元的NE ID

NE IP

网元的NE IP

Mask

网元的子网掩码

DCN interface

网元设备使用的LoopBack接口

Auto report

是否使能网元上下线自动上报功能

·Enabled：使能

·Disabled：关闭

**DCN \-- DCN配置命令 \-- display dcn ne-info**

------------------------------------------------------------------------

**[display dcn ne-info**]命令用来显示DCN网络中已上线的网元信息。

【命令】

**[display dcn ne-info**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示DCN网络中已上线的网元信息。

\<Sysname\> display dcn ne-info

              DCN Network Elements Information

 NE ID          NE IP            Metric   Device Type

 0x10001        3.3.3.3          0        HP 5900AF-48XG-4QSFP+ Switch

 Total number: 1

表1-2 display dcn ne-info命令显示信息描述表

字段

描述

NE ID

网元的NE ID

NE IP

网元的NE IP

Metric

从本端网元到达目的网元的开销

Device Type

网元的设备类型

Total number

上线的网元总数

**DCN \-- DCN配置命令 \-- ne-id**

------------------------------------------------------------------------

**[ne-id**]命令用来配置NE ID。

**[undo ne-id**]命令用来恢复缺省情况。

【命令】

**[ne-id **]*[id-number*]{.varname}

**[undo ne-id**]

【缺省情况】

NE ID根据设备的桥MAC地址自动生成（取桥MAC地址的低24位）。

【视图】

DCN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*id-number*{.varname}：设备的NE ID由子网号和基本ID两部分组成，共24位，取值范围为0x010001～0xFEFFFE。其中，高8位为子网号，低16位为基本ID。

【使用指导】

DCN网络中的设备通过唯一的NE ID进行标识。NE ID用于生成网元的缺省NE IP地址。

【举例】

\# 配置NE ID为0x112233。

\<Sysname\> system-view

Sysname dcn

Sysname-dcn ne-id 112233

【相关命令】

·**ne-ip**

**DCN \-- DCN配置命令 \-- ne-ip**

------------------------------------------------------------------------

**[ne-ip**]命令用来指定网元IP地址。

**[undo ne-ip**]命令用来恢复缺省情况。

【命令】

**[ne-ip ***ip-address *[{ *mask-length* \| *mask* }]]

**[undo ne-ip**]

【缺省情况】

NE IP根据NE ID自动生成，格式为：129.子网号.基本ID，且NE IP随着NE ID的变化而变化，掩码长度缺省为32。

【视图】

DCN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定的网元IP地址。

*[mask-length*]：NE IP的网络掩码长度，取值范围为1～32。

*[mask*]：NE IP的网络掩码，点分十进制形式。

【使用指导】

当开启DCN功能后，设备会占用最大编号的LoopBack接口，并将NE IP作为该接口的地址，可以用于LLDP的管理地址。当手动配置NE IP之后，NE ID与NE IP之间失去联动关系。

【举例】

\# 配置网元IP地址为100.1.1.1/24。

\<Sysname\> system-view

Sysname dcn

Sysname-dcn ne-ip 100.1.1.1 24

【相关命令】

·**ne-id**

