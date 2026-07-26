
**IPv6快速转发 \-- IPv6快速转发配置命令 \-- display ipv6 fast-forwarding aging-time**

------------------------------------------------------------------------

**[display ipv6 fast-forwarding aging-time**]命令用来显示IPv6快速转发表项的老化时间。

【命令】

**[display ipv6 fast-forwarding aging-time**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IPv6快速转发表项的老化时间。

\<Sysname\> display ipv6 fast-forwarding aging-time

Aging time: 30s

表1-1 display ipv6 fast-forwarding aging-time命令显示信息描述表

字段

描述

Aging time

IPv6快转表项的老化时间

【相关命令】

·**ipv6 fast-forwarding aging-time**

**IPv6快速转发 \-- IPv6快速转发配置命令 \-- display ipv6 fast-forwarding cache**

------------------------------------------------------------------------

**[display ipv6 fast-forwarding cache**]命令用来显示IPv6快速转发表信息。

【命令】

集中式设备：

**[display ipv6 fast-forwarding cache** [ *ipv6-address* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 fast-forwarding cache** [ *ipv6-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 fast-forwarding cache** [ *ipv6-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-address*]：显示指定IPv6地址的IPv6快速转发表信息。如果不指定*ipv6-address*，将显示所有IPv6地址的IPv6快速转发表信息。

**[slot** *slot-number*]：显示指定单板的IPv6快速转发表信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6快速转发表信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6快速转发表信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6快速转发表信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的IPv6快速转发表信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

**[display ipv6 fast-forwarding cache**]命令用来显示IPv6快速转发表信息，包括每条数据流的源IPv6地址、源端口号、目的IPv6地址、目的端口号、协议号、VPN实例、报文入接口、报文出接口等信息。

【举例】

\# 显示IPv6快转表信息。

\<Sysname\> display ipv6 fast-forwarding cache

Total number of IPv6 fast-forwarding items: 2

Src IP: 2002::1                                        Src port: 129

Dst IP: 2001::1                                        Dst port: 65535

Protocol: 58

VPN instance: vpn1

Input interface: GE1/0/2

Output interface: GE1/0/1

Src IP: 2001::1                                        Src port: 128

Dst IP: 2002::1                                        Dst port: 0

Protocol: 58

VPN instance: vpn2

Input interface: GE1/0/1

Output interface: GE1/0/2

表1-2 display ipv6 fast-forwarding cache命令显示信息描述表

字段

描述

Total number of IPv6 fast-forwarding items

IPv6快速转发表项数目

Src IP

源IPv6地址

Src port

源端口号

Dst IP

目的IPv6地址

Dst Port

目的端口号

Protocol

协议号

VPN instance

VPN实例名称

Input interface

报文入接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及入接口，"-"表示接口不存在）

Output interface

报文出接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及出接口，"-"表示接口不存在）

【相关命令】

·**reset ipv6 fast-forwarding cache**

**IPv6快速转发 \-- IPv6快速转发配置命令 \-- ipv6 fast-forwarding aging-time**

------------------------------------------------------------------------

**[ipv6 fast-forwarding aging-time**]命令用来配置IPv6快速转发表项的老化时间。

**[undo ipv6 fast-forwarding aging-time**]命令用来恢复缺省情况。

【命令】

**[ipv6 fast-forwarding aging-time ***aging-time*]

**[undo ipv6 fast-forwarding aging-time**]

【缺省情况】

IPv6快速转发表项的老化时间为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[aging-time*]：IPv6快速转发表项的老化时间，取值范围为10～300，单位为秒。

【举例】

\# 配置IPv6快速转发表项的老化时间为20s。

\<Sysname\> system-view

Sysname ipv6 fast-forwarding aging-time 20

【相关命令】

·**display ipv6 fast-forwarding aging-time**

**IPv6快速转发 \-- IPv6快速转发配置命令 \-- ipv6 fast-forwarding load-shaing**

------------------------------------------------------------------------

**[ipv6 fast-forwarding load-sharing**]命令用来开启IPv6快转负载分担功能。

**[undo ipv6 fast-forwardingload-shaing**]命令用来关闭IPv6快转负载分担功能。

【命令】

**[ipv6 fast-forwarding load-sharing**]

**[undo ipv6 fast-forwarding load-sharing**]

【缺省情况】

IPv6快转负载分担功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭IPv6快速转发负载分担功能后，将会根据入接口的不同对五元组标识的数据流再次做出区分，即将入接口作为区分数据流的另一特征标识。

开启IPv6快速转发负载分担功能后，当一条数据流从不同入接口上来进行转发时，不再根据入接口不同区分数据流，根据五元组标识一条数据流。

【举例】

\# 开启IPv6快转负载分担功能。

\<Sysname\> system-view

Sysname ipv6 fast-forwarding load-sharing

**IPv6快速转发 \-- IPv6快速转发配置命令 \-- reset ipv6 fast-forwarding cache**

------------------------------------------------------------------------

**[reset ipv6 fast-forwarding cache**]命令用来清除IPv6快速转发表信息。

【命令】

集中式设备：

**[reset ipv6 fast-forwarding cache**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset ipv6 fast-forwarding cache** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset ipv6 fast-forwarding cache** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的IPv6快速转发表信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板的IPv6快速转发表信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则清除所有成员设备的IPv6快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备/PEX的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则清除所有成员设备/PEX的IPv6快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板的IPv6快速转发表信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则清除所有单板的IPv6快速转发表信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的IPv6快速转发表信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

执行**reset ipv6 fast-forwarding cache**命令后，IPv6快速转发表中不再有任何IPv6快速转发表项。

【举例】

\# 清除IPv6快速转发表信息。

\<Sysname\> reset ipv6 fast-forwarding cache

【相关命令】

·**display ipv6 fast-forwarding cache**

