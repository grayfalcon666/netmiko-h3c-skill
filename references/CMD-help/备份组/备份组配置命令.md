<!-- CMD-INDEX
  bind                                | 备份组视图            | L7
  display failover group              | 任意视图             | L85
  failover group                      | 系统视图             | L161
-->

**备份组 \-- 备份组配置命令 \-- bind**

------------------------------------------------------------------------

**[bind**]命令用来将节点加入备份组。

**[undo bind**]命令用来删除备份组内的节点。

【命令】

分布式设备－独立运行模式：

**[bind slot ***slot-number ***cpu ***cpu-number*[ { **primary** \| **secondary** }]]

**[undo bind slot***slot-number***cpu ***cpu-number*]

分布式设备－IRF模式：

**[bind chassis**[ *chassis-number* **slot** *slot-number* **cpu** *cpu-number* { **primary** \| **secondary** }]]

**[undo bind chassis** *chassis-number* **slot** *slot-number* **cpu** *cpu-number*]

【缺省情况】

备份组下没有任何节点。

【视图】

备份组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[chassis** *chassis-number* **slot** *slot-number*]：表示单板在IRF中的位置。*chassis-number*表示设备在IRF中成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[primary**]：表示将节点配置成主节点。

**[secondary**]：表示将节点配置成备节点。

【使用指导】

每个备份组最多允许有两个节点：一个主节点和一个备节点。主节点处理业务，并将当前数据备份给备节点；备节点接收主节点的备份数据，当主节点故障时，接替主节点处理业务。

为了保证业务在主、备节点切换后，仍能正常运行，建议将不同单板上的性能相当的两个节点互为备份。

需要注意的是：

·不同备份组的主节点不能相同，同一备份组的主节点和备节点不能相同。

·只能将设备上已经存在的节点加入备份组。配置备份组后，对于拔出的节点，也需要使用**undo bind**命令将对应节点从备份组中删除。

【举例】

\# 将2号单板配置为备份组Group1的主节点。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname failover group Group1

Sysname-failover-group-Group1 bind slot 2 primary

\# 将成员设备1上的2号单板配置为备份组Group1的主节点。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname failover group Group1

Sysname-failover-group-Group1 bind chassis 1 slot 2 primary

**备份组 \-- 备份组配置命令 \-- display failover group**

------------------------------------------------------------------------

**[display failover group**]命令用来查看备份组的信息。

【命令】

**[display failover group** [ *group-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-name*]：表示备份组的名称，为1～63个字符的字符串，区分大小写。如果不指定该参数，将显示所有备份组的信息。

【举例】

\# 查看备份组的信息。

\<Sysname\> display failover group

Stateful failover group information:

ID  Name                            Primary      Secondary    Active Status

0   123                             1/2.1        1/3.1        Primary

1   aaa                             1/3.1        1/4.1        Secondary

2   bbb                             1/5.1        NA           Initial

表1-1 display failover group命令显示信息描述表

字段

描述

ID

备份组的编号

Name

备份组的名称

Primary

备份组的主节点，用*chassis-number*/*slot-number*.*cpu-number*来表示，如果该节点只有一个CPU，则不会显示*cpu-number*。当取值为NA时表示没有配置主节点

Secondary

备份组的备节点，用*chassis-number*/*slot-number*.*cpu-number*来表示，如果该节点只有一个CPU，则不会显示*cpu-number*。当取值为NA时表示没有配置备节点

Active Status

备份组的状态：

·Primary：备份组中主节点处理业务

·Secondary：备份组中备节点处理业务

·Initial：备份组中没有任何节点处理业务

**备份组 \-- 备份组配置命令 \-- failover group**

------------------------------------------------------------------------

**[failover group**]命令用来创建备份组，并进入备份组视图。

**[undo failover group**]命令用来删除指定备份组。

【命令】

**[failover group*** group-name*]

**[undo failover group*** group-name*]

【缺省情况】

未配置任何备份组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：备份组的名称，为1～63个字符的字符串，区分大小写。

【使用指导】

备份组用于实现特定业务（例如NAT业务）的数据备份，为特定业务的高可靠性运行提供保障。

通过配置多个备份组，可以实现业务的1:1备份、1+1备份、N:1备份或N+1备份。

【举例】

\# 创建备份组，名称为Group1，并进入该备份组的视图。

\<Sysname\> system-view

Sysname failover group Group1

Sysname-failover-group-Group1
