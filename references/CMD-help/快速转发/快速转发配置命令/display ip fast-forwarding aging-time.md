
**快速转发 \-- 快速转发配置命令 \-- display ip fast-forwarding aging-time**

------------------------------------------------------------------------

**[display ip fast-forwarding aging-time**]命令用来显示快速转发表项的老化时间。

【命令】

**[display ip fast-forwarding aging-time**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示快速转发表项的老化时间。

\<Sysname\> display ip fast-forwarding aging-time

 Aging time: 30s

表1-1 display ip fast-forwarding aging-time命令显示信息描述表

字段

描述

Aging time

快转表项的老化时间

【相关命令】

·**ip fast-forwarding aging-time**

**快速转发 \-- 快速转发配置命令 \-- display ip fast-forwarding cache**

------------------------------------------------------------------------

**[display ip fast-forwarding cache**]命令用来显示快速转发表信息。

【命令】

集中式设备：

**[display ip fast-forwarding cache** [ *ip-address* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ip fast-forwarding cache** [ *ip-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ip fast-forwarding cache** [ *ip-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定IP地址的快速转发表信息。如果不指定*ip-address*，将显示所有快速转发表信息。

**[slot** *slot-number*]：显示指定单板的快速转发表信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的快速转发表信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备的快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX的快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的快速转发表信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板的快速转发表信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的快速转发表信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

**[display ip fast-forwarding cache**]命令用来显示快速转发表信息，包括每条数据流的源IP地址、源端口号、目的IP地址、目的端口号、协议号、输入接口号、输出接口号、内部标记等信息。

【举例】

\# 显示所有快速转发表的信息。

\<Sysname\> display ip fast-forwarding cache

Total number of fast-forwarding entries: 3

SIP            SPort DIP            DPort Pro Input_If   Output_If   Flg

7.0.0.13       68    8.0.0.1        67    17  GE1/0/3    GE1/0/1      5

8.0.0.1        67    7.0.0.13       68    17  GE1/0/1    GE1/0/3      5

8.0.0.1        8     7.0.0.13       0     1   GE1/0/2    GE1/0/3      5

表1-2 display ip fast-forwarding cache命令显示信息描述表

字段

描述

Total number of fast-forwarding entries

快速转发表项数目

SIP

源IP地址

SPort

源端口号

DIP

目的IP地址

DPort

目的端口号

Pro

协议号

Input_If

报文入接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及入接口，"-"表示接口不存在）

Output_If

报文出接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及出接口，"-"表示接口不存在）

Flg

内部标记，主要是标记分片等内部操作信息

【相关命令】

·**reset ip fast-forwarding cache**

**快速转发 \-- 快速转发配置命令 \-- display ip fast-forwarding fragcache**

------------------------------------------------------------------------

**[display ip fast-forwarding fragcache**]命令用来显示分片报文快速转发表信息。

【命令】

集中式设备：

**[display ip fast-forwarding fragcache** [ *ip-address* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ip fast-forwarding fragcache** [ *ip-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ip fast-forwarding fragcache** [ *ip-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定IP地址的分片报文快速转发表信息。如果不指定*ip-address*，将显示所有分片报文快速转发表信息。

**[slot** *slot-number*]：显示指定单板的分片报文快速转发表信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的分片报文快速转发表信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的分片报文快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备的分片报文快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的分片报文快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX的分片报文快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的分片报文快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的分片报文快速转发表信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的分片报文快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板的分片报文快速转发表信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的分片报文快速转发表信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

**[display ip fast-forwarding fragcache**]命令用来显示分片报文快速转发表信息，包括分片报文的源IP地址、源端口号、目的IP地址、目的端口号、协议号、输入接口号、分片IP报文ID信息。

【举例】

\# 显示所有分片报文快速转发表信息。

\<Sysname\> display ip fast-forwarding fragcache

Total number of fragment fast-forwarding entries: 3

SIP             SPort DIP             DPort Pro Input_If    ID

7.0.0.13        68    8.0.0.1         67    17  GE1/0/3     2

8.0.0.1         67    7.0.0.13        68    17  GE1/0/1     3

8.0.0.1         8     7.0.0.13        0     1   GE1/0/2     5

表1-3 display ip fast-forwarding fragcache命令显示信息描述表

字段

描述

Total number of fragment fast-forwarding entries

分片报文快速转发表项数目

SIP

源IP地址

SPort

源端口号

DIP

目的IP地址

DPort

目的端口号

Pro

协议号

Input_If

报文入接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及入接口，"-"表示接口不存在）

ID

分片IP报文ID

【相关命令】

·**reset ip fast-forwarding cache**

**快速转发 \-- 快速转发配置命令 \-- ip fast-forwarding aging-time**

------------------------------------------------------------------------

**[ip fast-forwarding aging-time**]命令用来配置快速转发表项的老化时间。

**[undo ip fast-forwarding aging-time**]命令用来恢复缺省情况。

【命令】

**[ip fast-forwarding aging-time ***aging-time*]

**[undo ip fast-forwarding aging-time**]

【缺省情况】

快速转发表项的老化时间为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[aging-time*]：快速转发表项的老化时间，取值范围为10～300，单位为秒。

【举例】

\# 配置快速转发表项的老化时间为20s。

\<Sysname\> system-view

Sysname ip fast-forwarding aging-time 20

【相关命令】

·**display ip fast-forwarding aging-time**

**快速转发 \-- 快速转发配置命令 \-- ip fast-forwarding load-shaing**

------------------------------------------------------------------------

**[ip fast-forwarding load-sharing**]命令用来开启快转负载分担功能。

**[undo ip fast-forwardingload-shaing**]命令用来关闭快转负载分担功能。

【命令】

**[ip fast-forwarding load-sharing**]

**[undo ip fast-forwarding load-sharing**]

【缺省情况】

快转负载分担功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭快速转发负载分担功能后，将会根据入接口的不同对五元组标识的数据流再次做出区分，即将入接口作为区分数据流的另一特征标识。

开启快速转发负载分担功能后，当一条数据流从不同入接口上来进行转发时，不再根据入接口不同区分数据流，根据五元组标识一条数据流。

【举例】

\# 开启快转负载分担功能。

\<Sysname\> system-view

Sysname ip fast-forwarding load-sharing

**快速转发 \-- 快速转发配置命令 \-- reset ip fast-forwarding cache**

------------------------------------------------------------------------

**[reset ip fast-forwarding cache**]命令用来清除快速转发表中的信息。

【命令】

集中式设备：

**[reset ip fast-forwarding cache**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset ip fast-forwarding cache** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset ip fast-forwarding cache** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的快速转发表信息。*slot-number*表示单板的槽位号。如果未指定本参数，则清除所有单板的快速转发表信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备的快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则清除所有成员设备的快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备/PEX的快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则清除所有成员设备/PEX的快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则清除所有单板的快速转发表信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则清除所有单板的快速转发表信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU上的快速转发表信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

执行**reset ip fast-forwarding cache**命令后，快速转发表中不再有任何快速转发表项。

【举例】

\# 清除快速转发表信息。

\<Sysname\> reset ip fast-forwarding cache

【相关命令】

·**display ip fast-forwarding cache**

·**display ip fast-forwarding fragcache**

