
**OAP \-- OAP配置命令 \-- display oap client info**

------------------------------------------------------------------------

![说明](OAP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display oap client info**]命令用来显示OAP client的信息。

【命令】

**[display oap client info** [ *client-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[client-id*]：要显示的OAP client的Client ID，Client ID由OAP manager分配，取值范围为1～255。如果不指定参数则显示所有OAP client的信息。

【使用指导】

显示多个OAP client信息的时候按照Client ID由小到大顺序排列。OAP client信息从OAP client发送的信息通告报文中获得，当OAP client字段信息不存在时该字段不显示。

【举例】

\# 显示Client ID为1的OAP client的信息。

\<Sysname\> display oap client info 1

 Client ID: 1

 CPU: Intel(R) Pentium(R) M processor 1.40GHz

PCB Version: 3.00

 CPLD Version: 1.00

 Bootrom Version: 1.12

 Storage Card: 256 MB

 Memory: 512 MB

 Harddisk: 40.0 GB

\# 显示所有OAP client的信息。

\<Sysname\> display oap client info

 Client ID: 1

 CPU: Intel(R) Pentium(R) M processor 1.40GHz

 PCB Version: 3.00

 CPLD Version: 1.00

 Bootrom Version: 1.12

 Storage Card: 256 MB

 Memory: 512 MB

 Harddisk: 40.0 GB

 Client ID: 2

 CPU: Intel(R) Pentium(R) M processor 1.40GHz

 PCB Version: 3.00

 CPLD Version: 1.00

 Bootrom Version: 1.12

 Storage Card: 256 MB

 Memory: 512 MB

 Harddisk: 40.0 GB

表1-1 display oap client info命令显示信息描述表

字段

描述

Client ID

OAP client的Client ID

Client Description

OAP client的描述字符串

Hardware

OAP client的硬件版本

System Software

OAP client的系统软件名称与版本

Application Software

OAP client的应用软件版本

CPU

OAP client的CPU信息

PCB Version

OAP client的PCB版本信息

CPLD Version

OAP client的CPLD版本信息

Bootrom Version

OAP client的Boot ROM版本信息

Storage Card

OAP client的存储卡的空间大小，单位为MB

Memory

OAP client的内存大小，单位为MB

Harddisk

OAP client的硬盘大小，单位为MB

【相关命令】

·**display oap client summary**

**OAP \-- OAP配置命令 \-- display oap client summary**

------------------------------------------------------------------------

![说明](OAP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display oap client summary**]命令用来显示OAP client的摘要信息。

【命令】

**[display oap client summary** [ *client-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[client-id*]：要显示摘要信息的Client ID，Client ID由OAP manager分配，取值范围为1～255。如果不指定参数则显示所有OAP client的摘要信息。

【使用指导】

显示多个OAP client摘要信息的时候按照Client ID由小到大顺序排列。

【举例】

\# 显示Client ID为1的OAP client的摘要信息。

\<Sysname\> display oap client summary 1

 Client ID: 1

 Status: Registered

 MAC Address: 00e0-fc0a-c3ef

 Interface: GigabitEthernet1/0/1

 Last registered: 02/08/2011 12:00:00

\# 显示所有OAP client的摘要信息。

\<Sysname\> display oap client summary

 Client ID: 1

 Status: Registered

 MAC Address: 00e0-fc0a-c3ef

 Interface: GigabitEthernet1/0/1

 Last registered: 02/08/2011 12:00:00

 Client ID: 2

 Status: Registered

 MAC Address: 00e0-fa1e-03da

 Interface: GigabitEthernet1/0/2

 Last registered: 02/08/2011 13:00:00

表1-2 display oap client summary命令显示信息描述表

字段

描述

Client ID

OAP client的Client ID

Status

OAP client的状态，取值包括：Registered：已注册。

MAC Address

OAP client的MAC地址

Interface

OAP client的承载接口

Last registered

OAP client的最近注册时间

【相关命令】

·**display oap client info**

**OAP \-- OAP配置命令 \-- oap client close**

------------------------------------------------------------------------

![说明](OAP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[oap client close**]命令用来关闭指定的OAP client。

【命令】

**[oap client close** *client-id*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[client-id*]：要关闭的OAP client的Client ID，取值范围为1～255。

【使用指导】

若指定的Client为Registered状态，OAP manager会发送一条关闭操作的通告报文给指定的OAP client，OAP client收到此报文后将执行关闭操作。若指定的Client不存在，则会打印提示信息。

OAP manager给OAP client分配ID，用于保证各OAP client的唯一性。

需要注意的是，该命令仅对运行Linux系统的OAP client生效。

【举例】

\# 关闭Client ID为1的OAP client。

\<Sysname\> system-view

Sysname oap client close 1

【相关命令】

·**display oap client summary**

·**oap client reboot**

**OAP \-- OAP配置命令 \-- oap client reboot**

------------------------------------------------------------------------

![说明](OAP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[oap client reboot**]命令用来重启OAP client。

【命令】

**[oap client reboot** *client-id*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[client-id*]：要重启的OAP client的Client ID，取值范围为1～255。

【使用指导】

输入该命令后，若指定的Client为Registered状态，OAP manager会发送一条重启的通告报文给指定的OAP client，OAP client收到此报文后将执行重启操作。若指定的Client不存在，则会打印提示信息。

OAP manager给OAP client分配ID，用于保证各OAP client的唯一性。

【举例】

\# 重启Client ID为1的OAP client。

\<Sysname\> system-view

Sysname oap client reboot 1

【相关命令】

·**display oap client summary**

·**oap client close**

**OAP \-- OAP配置命令 \-- oap enable**

------------------------------------------------------------------------

[**[![说明](OAP命令.files/image001.png)]**]

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[oap enable**]命令用来启用OAP功能。

**[undo oap enable**]命令用来关闭OAP功能。

【命令】

**[oap enable**]

**[undo oap enable**]

【缺省情况】

接口下OAP协议功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在接口GigabitEthernet1/0/1下启用OAP功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oap enable

**OAP \-- OAP配置命令 \-- oap timer clock-sync**

------------------------------------------------------------------------

![说明](OAP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[oap timer clock-sync**]命令用来配置OAP manager到OAP client时钟同步定时器的值。

**[undo oap timer clock-sync**]命令用来恢复OAP manager到OAP client时钟同步定时器的值为缺省值。

【命令】

**[oap timer clock-sync** *minutes*]

**[undo oap timer clock-sync**]

【缺省情况】

OAP manager到OAP client的时钟同步定时器的值为5分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：OAP manager到OAP client的时钟同步定时器的值，取值范围为0～1440，单位为分钟。0表示OAP manager不会对OAP client进行时钟同步。

【举例】

\# 配置OAP manager到OAP client的时钟同步定时器的值为20分钟。

\<Sysname\> system-view

Sysname oap timer clock-sync 20

**OAP \-- OAP配置命令 \-- oap timer monitor**

------------------------------------------------------------------------

![说明](OAP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[oap timer monitor**]命令用来配置OAP manager到OAP client监控定时器的值。

**[undo oap timer monitor**]命令用来恢复OAP manager到OAP client监控定时器的值为缺省值。

【命令】

**[oap timer monitor** *seconds*]

**[undo oap timer monitor**]

【缺省情况】

OAP manager对OAP client的监控定时器的值为5秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：OAP manager对OAP client的监控定时器的值，取值范围为0～10，单位为秒。0表示禁止OAP manager对OAP client的监控。

【举例】

\# 配置OAP manager对OAP client的监控定时器的值为6秒。

\<Sysname\> system-view

Sysname oap timer monitor 6
