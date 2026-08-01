<!-- CMD-INDEX
  affinity location-set               | 分布策略视图           | L15
  affinity location-type              | 分布策略视图           | L91
  affinity program                    | 分布策略视图           | L155
  affinity self                       | 分布策略视图           | L215
  display ha service-group            | 任意视图             | L277
  display placement location          | 任意视图             | L443
  display placement policy            | 任意视图             | L613
  display placement program           | 任意视图             | L695
  display placement reoptimize        | 任意视图             | L763
  placement program                   | 系统视图             | L853
  placement reoptimize                | 系统视图             | L919
-->

**进程分布优化 \-- 进程分布优化配置命令 \-- affinity location-set**

------------------------------------------------------------------------

**[affinity location-set**]命令用来设置进程对于节点位置的偏好。

**[undo affinity location-set**]命令用来取消设置。

【命令】

**[affinity location-set **{ **slot** *slot-number* [ **cpu** *cpu-number*  }&\<1-5\> { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]]

**[undo affinity location-set **{ **slot** *slot-number* [ **cpu** *cpu-number*  }&\<1-5\>]]

分布式设备－IRF模式：

**[affinity location-set **{ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  }&\<1-5\> { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]]

**[undo affinity location-set **{ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  }&\<1-5\>]]

【缺省情况】

系统未配置进程对节点位置的偏好。

【视图】

分布策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

{ **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  }&\<1-5\>：表示当前进程在指定CPU上运行的偏好。其中：

·**chassis*** chassis-number*：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

·**slot*** slot-number*：暂无意义，取值始终为0。（集中式设备）

·**slot*** slot-number*：表示单板所在的槽位号。（分布式设备－独立运行模式/分布式设备－IRF模式）

·**slot*** slot-number*：表示设备在IRF中的成员编号。（集中式IRF设备）

·**cpu*** cpu-number*：表示CPU的编号。如果单板上存在多个CPU（比如主CPU、辅助CPU等），需要使用该参数指定CPU的编号。如果不指定该参数，则表示主CPU。

·&\<1-5\>：表示前面的参数最多可以输入5次。

**[attract ***strength*]：正向偏好程度，表示希望运行在该位置。*strength*表示偏好程度，取值范围为1～100000。值越大表示进程运行在该位置的可能性越大。

**[default**]：缺省偏好，取值为正向偏好200。

**[none**]：设置偏好为0，即主进程对具体节点没有偏好，主进程的运行位置由系统来决定。

**[repulse***strength*]：反向偏好程度，表示不希望运行在该位置。*strength*表示偏好程度，取值范围为1～100000。值越大表示进程运行在该位置的可能性越小。

【举例】

\# 设置BGP对于3号槽位的正向偏好为500。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> system-view

Sysname placement program bgp

Sysname-program-bgp affinity location-set slot 3 attract 500

\# 设置BGP对于1号成员设备的3号槽位的正向偏好为500。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname placement program bgp

Sysname-program-bgp affinity location-set chassis 1 slot 3 attract 500

**进程分布优化 \-- 进程分布优化配置命令 \-- affinity location-type**

------------------------------------------------------------------------

**[affinity location-type**]命令用来设置进程对于位置类型的偏好。

**[undo affinity location-type**]命令用来恢复缺省情况。

【命令】

**[affinity location-type**[ { **current** \| **paired** \| **primary** } { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]]

**[undo affinity location-type**[ { **current** \| **paired** \| **primary** }]]

【缺省情况】

系统未配置进程对位置类型的偏好。

【视图】

分布策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[current**]：用来设置对主控进程当前运行位置的偏好。主控进程当前运行位置可以通过**display placement program**命令查看。

**[paired**]：用来设置对所有备份进程当前运行位置的偏好。

**[primary**]：用来设置对主用主控板的偏好。（分布式设备－独立运行模式）

**[primary**]：用来设置对主设备的偏好。（集中式IRF设备）

**[primary**]：用来设置对全局主用主控板的偏好。（分布式设备－IRF模式）

**[attract ***strength*]：正向偏好程度，表示希望运行在该位置。*strength*表示偏好程度，取值范围为1～100000。值越大表示进程运行在该位置类型的可能性越大。

**[default**]：缺省偏好，取值为正向偏好200。

**[none**]：设置偏好为0，即主进程对位置类型没有偏好，主进程的运行位置由系统来决定。

**[repulse***strength*]：反向偏好程度，表示不希望运行在该位置。*strength*表示偏好程度，取值范围为1～100000。值越大表示进程运行在该位置类型的可能性越小。

【举例】

\# 设置BGP对于当前位置的正向偏好为500。

\<Sysname\> system-view

Sysname placement program bgp

Sysname-program-bgp affinity location-type current attract 500

【相关命令】

·**affinity location-set**

·**affinity program**

**进程分布优化 \-- 进程分布优化配置命令 \-- affinity program**

------------------------------------------------------------------------

**[affinity program**]命令用来设置本进程和其它进程运行在同一位置的偏好。

**[undo affinity program**]命令用来取消设置。

【命令】

**[affinity program**[ *program-name* { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]]

**[undo affinity program ***program-name*]

【缺省情况】

进程未配置和其它进程运行在同一位置的偏好。

【视图】

分布策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[program-name*]：为当前设备上正在运行的进程的名称，为1～15个字符的字符串，不区分大小写。用户可以通过**display placement program all**命令查看设备上正在运行的进程。

**[attract ***strength*]：正向偏好程度，表示希望运行在该位置。*strength*表示偏好程度，取值范围为1～100000。值越大表示进程运行于同一位置的可能性越大。

**[default**]：缺省偏好，取值为正向偏好200。

**[none**]：设置偏好为0，即主进程对于是否和其它其它进程运行在同一位置没有偏好，主进程的运行位置由系统来决定。

**[repulse***strength*]：反向偏好程度，表示不希望运行在该位置。*strength*表示偏好程度，取值范围为1～100000。值越大表示进程运行于同一位置的可能性越小。

【使用指导】

该配置方式以其它进程通过进程分布策略计算出来的预测位置为参照物，配置的是本进程和其它进程运行在同一位置的偏好。

【举例】

\# 设置OSPF和BGP运行于同一位置的偏好为反向200。

\<Sysname\> system-view

Sysname placement program ospf

Sysname-program-ospf affinity program bgp repulse 200

【相关命令】

·**affinity location-set**

·**affinity location-type**

**进程分布优化 \-- 进程分布优化配置命令 \-- affinity self**

------------------------------------------------------------------------

**[affinity self**]命令用来设置本进程所有实例运行于同一位置的偏好。

**[undo affinity self**]命令用来取消设置。

【命令】

**[affinity self**[ { **attract** *strength* \| **default** \| **none** \| **repulse** *strength* }]]

**[undo affinity self**]

【缺省情况】

进程未配置所有实例运行于同一位置的偏好。

【视图】

分布策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[attract ***strength*]：正向偏好程度，表示希望运行在该位置。*strength*表示偏好程度，取值范围为1～100000。值越大表示进程运行于同一位置的可能性越大。

**[default**]：缺省偏好，取值为正向偏好200。

**[none**]：设置偏好为0，即进程对所有实例是否运行于同一位置没有偏好，运行位置由系统来决定。

**[repulse***strength*]：反向偏好程度，表示不希望运行在该位置。*strength*表示偏好程度，取值范围为1～100000。值越大表示进程运行于同一位置的可能性越小。

【使用指导】

该配置用以决定一个进程的多个实例是否运行于同一个位置上，如果进程只有一个实例，则该配置不会产生作用。

本命令在进程的分布策略视图和进程任意实例的分布策略视图下配置效果相同，均对所有实例生效。多次配置该命令，最新配置生效。

进程是否包含多个实例可以通过**display placement program all**命令查看。

【举例】

\# 设置BGP进程所有实例运行于同一位置的偏好为反向200。

\<Sysname\> system-view

Sysname placement program bgp

Sysname-program-bgp affinity self repulse 200

【相关命令】

·**affinity location-set**

·**affinity location-type**

**进程分布优化 \-- 进程分布优化配置命令 \-- display ha service-group**

------------------------------------------------------------------------

**[display ha service-group**]命令用来显示服务组的当前位置和状态等信息。

【命令】

**[display ha service-group **{ *program-name* [ **instance** *instance-name*  \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[program-name*]：为当前设备上正在运行的服务组的名称，为1～15个字符的字符串，不区分大小写。

**[all**]：表示当前设备上运行的所有服务组。

**[instance ***instance-name*]：表示实例名，为1～15个字符的字符串，不区分大小写。一个服务组是否存在多个实例，由系统软件决定。

【举例】

\# 显示所有服务组主控进程的位置和状态信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display ha service-group all

Service Group                     Current Location      State

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ospf                              0/0                   Realtime Backup

bgp                               1/0                   Batch Backup

isis                              0/0                   Stopping

rip                               1/0                   Realtime Backup

ripng                             1/0                   Upgrading

staticroute                       1/0                   Batch Backup

\# 显示指定服务组主控进程的位置和状态信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display ha service-group staticroute

Service Group                     Current Location      State

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

staticroute                       1/0 (Active)          Batch Backup

  Detailed information about services of the program:

  Service           PID    Type      Location   State

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  ifm               200    Standby   0/0        Realtime Backup

  staticroute       200    Standby   0/0        Batch Backup

  ifm               200    Active    1/0        Realtime Backup

  staticroute       200    Active    1/0        Batch Backup

以上显示信息表明（以staticroute为例），服务组staticroute的主控进程当前运行于1号槽位单板的0号CPU上，当前状态是批量备份状态。服务组staticroute的备用进程当前运行于0号槽位单板的0号CPU上。服务组staticroute下有ifm和staticroute两个服务，PID分别是200和200，ifm当前状态是实时备份状态，staticroute当前状态是批量备份状态。

\# 显示所有服务组主控进程的位置和状态信息。（分布式设备－IRF模式）

\<Sysname\> display ha service-group all

Service Group                     Current Location      State

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ospf                              1/0/0                 Realtime Backup

bgp                               1/1/0                 Batch Backup

isis                              1/1/0                 Stopping

rip                               1/0/0                 Realtime Backup

ripng                             2/0/0                 Upgrading

staticroute                       1/0/0                 Batch Backup

\# 显示指定进程主备身份及当前状态。（分布式设备－IRF模式）

\<Sysname\>display ha service-group staticroute

Service Group                     Current Location      State

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

staticroute                       1/0/0 (Active)        Batch Backup

  Detailed information about services of the program:

  Service           PID    Type      Location   State

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  ifm               200    Active    1/0/0      Realtime Backup

  staticroute       200    Active    1/0/0      Batch Backup

  ifm               200    Standby   1/1/0      Realtime Backup

  staticroute       200    Standby   1/1/0      Batch Backup

  ifm               200    Standby   2/0/0      Realtime Backup

  staticroute       200    Standby   2/0/0      Batch Backup

以上显示信息表明（以staticroute为例），服务组staticroute的主控进程当前运行于设备1的0号槽位单板的0号CPU上，当前状态是批量备份状态。服务组staticroute的备用进程当前运行于设备1的1号槽位单板的0号CPU上和设备2的0号槽位单板的0号CPU上。服务组staticroute下有ifm和staticroute两个服务，PID分别是200和200，ifm当前状态是实时备份状态，staticroute当前状态是批量备份状态。

表1-1 display ha service-group命令显示信息描述表

字段

描述

Service Group

服务组的名称

Type

进程的主备身份，取值为：

·Active：表示服务组主控进程

·Standby：表示服务组备用进程

Service

服务组内的服务的名称

State

进程的状态：

·Realtime Backup：实时备份状态

·Batch Backup：批量备份状态

·Stopping：停止状态

·Degrading：降级状态

·Upgrading：升级状态

**进程分布优化 \-- 进程分布优化配置命令 \-- display placement location**

------------------------------------------------------------------------

**[display placement location**]命令用来显示具体位置上正在运行的进程信息。

【命令】

**[display placement location **[{ **all** \| **slot** *slot-number* [ **cpu** *cpu-number* ] }]]

分布式设备－IRF模式：

**[display placement location **[{ **all** \| **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：表示当前设备上运行的所有进程。

**[slot*** slot-number*]：暂无意义，取值始终为0。（集中式设备）

**[slot*** slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number ***slot*** slot-number*]：表示指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示所有主控板。（分布式设备－IRF模式）

**[cpu*** cpu-number*]：表示CPU的编号，该参数的取值范围与设备的型号有关，请以设备的实际情况为准。如果单板上存在多个CPU（比如主CPU、辅助CPU等），需要使用该参数指定CPU的编号。如果不指定该参数，则表示主CPU。

【举例】

\# 显示设备上正在运行的进程信息。（集中式设备）

\<Sysname\> display placement location slot 0

Program(s) placed at location: 0/0

  l3vpn

  lsm

  aaa

  lauth

  track

  bfd

  rm6

  rm

  rpm

  usr6

  ipaddr

  ip6addr

  slsp

  usr

  ethbase

  ip6base

  ipbase

  eth

\# 显示1号槽单板上正在运行的进程信息。（分布式设备－独立运行模式）

\<Sysname\> display placement location slot 1

Program(s) placed at location: 1/0

  l3vpn

  lsm

  aaa

  lauth

  track

  bfd

  rm6

  rm

  rpm

  usr6

  ipaddr

  ip6addr

  slsp

  usr

  ethbase

  ip6base

  ipbase

  eth

\# 显示成员设备1的0号槽位单板上正在运行的进程信息。（分布式设备－IRF模式）

\<Sysname\> display placement location chassis 1 slot 0

Program(s) placed at location: 1/0/0

  l3vpn

  lsm

  aaa

  lauth

  track

  bfd

  rm6

  rm

  rpm

  usr6

  ipaddr

  ip6addr

  slsp

  usr

  ethbase

  ip6base

  ipbase

  eth

**进程分布优化 \-- 进程分布优化配置命令 \-- display placement policy**

------------------------------------------------------------------------

**[display placement policy**]命令用来显示进程的分布策略。

【命令】

**[display placement policy program **[{ *program-name* \| **all** \| **default** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[program-name*]：显示指定进程的分布策略，为1～15个字符的字符串，不区分大小写。

**[all**]：显示所有配置的进程分布策略。

**[default**]：显示用户配置的缺省分布策略的信息。如果没有通过**placement program default**配置，则没有显示信息。

【使用指导】

只有为进程成功配置分布策略后，才会输出相应的显示信息。

【举例】

\# 显示缺省分布策略的信息。

\<Sysname\> display placement policy program default

Program: [default                                : source]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  affinity location-set slot 0 cpu 0 attract      : system [default]

\# 显示aaa进程的分布策略。

\<Sysname\> display placement policy program aaa

Program: aaa                                      : source

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  affinity location-set slot 0 cpu 7 attract      : system aaa

   100

  affinity location-set slot 0 cpu 1 attract      : system aaa

   100

  affinity location-set slot 0 cpu 0 attract      : system [default]

   100

表1-2 display placement policy命令显示信息描述表

字段

描述

Program

进程的名称以及进程的分布策略

source

进程分布策略的来源，其中：system [default]表示采用系统缺省分布策略，该策略是通过**placement program default**命令进入缺省分布策略视图后再配置的；system aaa表示采用AAA进程分布策略，该策略是通过**placement program ***program-name*命令进入AAA的分布策略视图后再配置的

**进程分布优化 \-- 进程分布优化配置命令 \-- display placement program**

------------------------------------------------------------------------

**[display placement program**]命令用来显示主控进程的当前运行位置。

【命令】

**[display placement program**[ { *program-name* \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[program-name*]：为当前设备上正在运行的进程的名称，为1～15个字符的字符串，不区分大小写。

**[all**]：表示当前设备上运行的所有进程。

【举例】

\# 显示AAA主控进程的当前运行位置。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display placement program aaa

Program                           Placed at location

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

aaa                               0/0

\# 显示AAA主控进程的当前运行位置。（分布式设备－IRF模式）

\<Sysname\> display placement program aaa

Program                          Placed at Location

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

aaa                              1/0/0

表1-3 display placement program命令显示信息描述表

字段

描述

Program

进程的名称

Placed at location

主进程运行的位置

当显示为NA时表示该业务当前没有主进程（没有主进程的原因可能为：业务异常；主进程正在启动；主进程被关闭等）

**进程分布优化 \-- 进程分布优化配置命令 \-- display placement reoptimize**

------------------------------------------------------------------------

**[display placement reoptimize**]命令用来显示进程分布优化后的预测位置。

【命令】

**[display placement reoptimize program **{ *program-name* [ **instance** *instance-name*  \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[program-name*]：为当前设备上正在运行的、支持进程优化配置的进程的名称，为1～15个字符的字符串，不区分大小写。

**[instance ***instance-name*]：表示实例名，为1～15个字符的字符串，不区分大小写。一个进程是否存在多个实例，由系统软件决定。

**[all**]：表示当前设备上运行的、支持进程优化配置的所有进程。

【举例】

\# 显示分布优化后所有进程的预测位置。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display placement reoptimize program all

Predicted changes to the placement

Program                           Current location       New location

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

rm6                               1/0                    1/0

rm                                1/0                    1/0

rpm                               1/0                    1/0

usr                               1/0                    1/0

usr6                              1/0                    1/0

bgp                               1/0                    1/0

pim                               1/0                    1/0

igmp                              1/0                    1/0  

以上显示信息中，Program表示进程的名称，Current location表示主进程当前运行的位置，New location表示分布优化后，主进程将运行的位置。

\# 显示分布优化后所有进程的预测位置。（分布式设备－IRF模式）

\<Sysname\> display placement reoptimize program all

Predicted changes to the placement

Program                           Current location       New location

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

rm6                               1/0/0                  1/0/0

rm                                1/0/0                  1/0/0

rpm                               1/0/0                  1/0/0

usr                               1/0/0                  1/0/0

usr6                              1/0/0                  1/0/0

bgp                               1/0/0                  1/0/0

pim                               1/0/0                  1/0/0

igmp                              1/0/0                  1/0/0

以上显示信息中，Program表示进程的名称，Current location表示主进程当前运行的位置，New location表示分布优化后，主进程将运行的位置。

**进程分布优化 \-- 进程分布优化配置命令 \-- placement program**

------------------------------------------------------------------------

**[placement program**]命令用来进入指定进程的分布策略视图。

**[undo placement program**]命令用来删除指定进程的分布策略。

【命令】

**[placement program **{ *program-name* [ **instance** *instance-name*  \| **default** }]]

**[undo placement program** { *program-name* [ **instance** *instance-name*  \| **default** }]]

【缺省情况】

所有进程均未配置分布策略。所有进程的主控进程都在主用主控板上运行。（分布式设备－独立运行模式）

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[program-name*]：用来进入指定进程的分布策略视图。*program-name*表示当前设备上正在运行的进程的名称，为1～15个字符的字符串，不区分大小写。

**[instance ***instance-name*]：用来进入指定进程指定实例的分布策略视图。*instance-name*表示实例名，为1～15个字符的字符串，不区分大小写。一个进程是否存在多个实例，由系统软件决定。

**[default**]：用来进入缺省分布策略视图。进入该视图后，配置的是所有进程（所有实例）的缺省分布策略。

【使用指导】

为了提高系统的可靠性，系统在运行过程中会对进程进行1:N备份。当启动某个业务时，系统会自动同时为该业务运行一个主控进程和多个备份进程。

对于一些业务，其主控进程只能运行在主用主控板，这样的进程不支持进程分布优化配置（配置时会提示失败）。当主控进程异常时，系统会自动重启该主控进程。备份进程主要用于主备倒换和ISSU升级环境。

另一些业务，其主控进程可以运行在主用主控板上，也可以运行在备用主控板上。当主控进程异常时，需要从备份进程中选举一个新的主控进程，从而保证业务不受影响。在众多的备份进程中到底选用哪个作为新的主控进程，由该进程的分布策略决定。

分布策略的内容包括**affinity location-type**、**affinity location-set**、**affinity program和affinity self**，这些命令从不同角度表达了用户对进程在某个位置运行的期望。

一个进程对应一个分布策略，所有的**affinity**命令可以同时设置。系统将根据用户的配置按照一定的算法，最后决定主控进程的预测位置（可以通过**display placement reoptimize**命令查看）。当发生主备倒换时，该位置的进程就能当选为主控进程，其它位置的进程则均为备份进程。

【举例】

\# 进入BGP分布策略视图。

\<Sysname\> system-view

Sysname placement program bgp

Sysname-program-bgp

\# 进入缺省分布策略视图。

\<Sysname\> system-view

Sysname placement program default

Sysname-program-default

**进程分布优化 \-- 进程分布优化配置命令 \-- placement reoptimize**

------------------------------------------------------------------------

**[placement reoptimize**]命令用来优化进程运行位置，使进程分布策略生效。

【命令】

**[placement reoptimize**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行该命令后，系统会根据当前硬件的在位情况、主进程的运行位置和状态、分布策略的配置来综合计算主进程的新位置，并将该位置上的进程当选为主控进程，其它位置上的进程均为备份进程。如果新当选的主进程和原主进程不同，则会触发进程的主备倒换。因为只是主备进程间角色的转换，进程不需要重启，所以进程的主备倒换不会造成业务中断。

执行此命令时请保持系统的稳定性，不建议在执行此命令的过程中进行任务涉及进程重启的操作。

【举例】

\# 手工进行进程分布优化。

\<Sysname\> system-view

Sysname placement reoptimize

Predicted changes to the placement

Program                           Current location       New location

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

syslog                            0/0                    0/0

l3vpn                             0/0                    0/0

aaa                               0/0                    0/0

lauth                             0/0                    0/0

lsm                               0/0                    0/0

ip6addr                           0/0                    0/0

ip6base                           0/0                    0/0

rm                                0/0                    0/0

ipcfg                             0/0                    0/0

acl                               0/0                    0/0

tunnel                            0/0                    0/0

lagg                              0/0                    0/0

qos                               0/0                    0/0

ipcim                             0/0                    0/0

ipbase                            0/0                    0/0

eth                               0/0                    0/0

ipen                              0/0                    0/0

Continue? [y/n:y]

Re-optimization of the placement start. You will be notified on completion

Re-optimization of the placement complete. Use \'display placement\' to view the new placement
