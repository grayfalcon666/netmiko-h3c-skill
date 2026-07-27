<!-- CMD-INDEX
  allocate interface                  | MDC视图            | L19
  display mdc                         | 任意视图             | L119
  display mdc interface               | 任意视图             | L191
  display mdc resource                | 任意视图             | L243
  limit-resource cpu                  | MDC视图            | L469
  limit-resource disk                 |                  | L523
  limit-resource memory               |                  | L619
  location                            |                  | L713
  switchto mdc                        | 系统视图             | L783
  mdc                                 | 系统视图             | L841
  mdc start                           | MDC视图            | L899
  display mdc                         | 任意视图             | L945
  display mdc interface               | 任意视图             | L977
  display mdc resource                | 任意视图             | L1009
  switchback                          | 用户视图             | L1145
-->

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- allocate interface**

------------------------------------------------------------------------

**[allocate interface**]命令用来为MDC分配物理接口。

**[undo allocate interface**]命令用来将接口从MDC中删除。

【命令】

**[allocate interface***interface-list*]

**[undo allocate interface** *interface-list*]

【缺省情况】

物理设备上的所有接口都属于缺省MDC，不属于任何非缺省MDC。

【视图】

MDC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-list*]：接口列表，表示给MDC分配接口，表示方式为*interface-list*＝ { *interface-type interface-number* [ **to** *interface-type interface-number*  }&\<1-24\>]。其中*interface-type interface-number*表示接口类型和接口编号。&\<1-24\>表示前面的参数最多可以输入24次。当使用**to**关键字指定接口范围时（形如*interface-type interface-number1* **to** *interface-type interface-number2*），则**to**关键字左边[的接口（起始接口）和]**to**关键字右边的接口（结束接口）类型必须相同，并且处于同一接口板上，否则将配置失败。

【使用指导】

·将IRF中某成员设备上的接口分配给MDC的时候，请确保该成员设备上缺省MDC中至少要保留一个处于up状态的IRF物理端口，否则，会导致IRF分裂。

·物理设备的Console口和AUX口被缺省MDC独享，不能分配给非缺省MDC。

·物理设备的管理以太网口不能分配。缺省MDC上始终有管理以太网口，非缺省MDC的管理以太网口在MDC创建时由系统自动创建。不同MDC的管理以太网口名称和编号相同，共用物理设备上的同一个物理接口和物理链路，可以配置同网段或者不同网段的IP地址，以便不同MDC的管理员登录自己的MDC。

·一个物理接口只能属于一台MDC。物理接口分配给MDC后，需要登录该MDC后，才能对接口下的参数进行配置。

·多次使用**allocate interface**命令可以给同一MDC分配多个接口。

·由于硬件限制，某些接口板上的接口是按组划分的，每个组里包含几个接口。此时，请一次性将这组接口分配给某一MDC，而不能只分配这组接口中的部分接口。接口是否按组划分以及哪些接口分为一组与设备的型号有关，请以设备的实际情况为准。

·物理接口只能从缺省MDC分配到非缺省MDC。当某接口属于MDC A，要分配到MDC B时，需要先使用**undo allocate interface**命令，将该接口归还给缺省MDC，再使用**allocate interface**命令分配给MDC B。

·将物理接口分配给MDC或者从MDC中删除时，该接口下的所有配置都会恢复到缺省情况。

请确保缺省MDC和非缺省MDC用户对同一个接口的操作时序，在缺省MDC用户分配或删除接口时及时通知非缺省MDC用户，让其停止配置该接口，否则可能导致接口达不到非缺省MDC用户预期的配置效果。

·将IRF物理端口分配给其它MDC或者从当前MDC中删除时，必须先执行**undo port group interface**命令恢复到缺省情况，再执行分配或者删除操作，最后执行**save**命令保存当前配置文件。有关**undo port group interface**命令的详细使用，请参见"IRF命令参考"中的"IRF"。

【举例】

\# 将接口GigabitEthernet1/0/1和GigabitEthernet1/0/3分配给MDC sub1。

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 allocate interface gigabitethernet 1/0/1 gigabitethernet1/0/3

Configuration of the interfaces will be lost. Continue? Y/N:y{.TerminalDisplayChar}

\# 将接口GigabitEthernet1/0/1～GigabitEthernet1/0/8分配给MDC sub1。

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 allocate interface gigabitethernet 1/0/1 to gigabitethernet 1/0/8

Configuration of the interfaces will be lost. Continue? [Y/N:y]

\# 将接口GigabitEthernet1/0/4分配给MDC sub1。

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 allocate interface gigabitethernet 1/0/4

Configuration of the interfaces will be lost. Continue? [Y/N:y]

Group error: all interfaces of one group must be allocated to the same mdc.

  GigabitEthernet1/0/4

Port list of group 2:

  GigabitEthernet1/0/3               GigabitEthernet1/0/4

以上提示信息表明GigabitEthernet1/0/4必须和GigabitEthernet1/0/3一起分配给同一个MDC。执行如下命令，将GigabitEthernet1/0/3和GigabitEthernet1/0/4一起分配给MDC sub1：

Sysname-mdc-2-sub1 allocate interface gigabitethernet 1/0/3 gigabitethernet 1/0/4

Configuration of the interfaces will be lost. Continue? [Y/N:y]

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- display mdc**

------------------------------------------------------------------------

**[display mdc**]命令用来显示MDC的相关信息，包括MDC的编号、名称和状态。

【命令】

**[display mdc ** **name** ]*mdc-name *

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** mdc-name*]：显示指定MDC的相关信息。*mdc-name*表示MDC的名称，为1～15个字符的字符串。不指定该参数时，显示所有MDC的相关信息。

【举例】

\# 显示所有MDC的相关信息。

\<Sysname\> display mdc

ID         Name            Status

1          Admin           active

2          sub1            inactive

表1-1 display mdc命令显示信息描述表

字段

描述

ID

MDC的编号

Name

MDC的名称

Status

MDC的状态：

·inactive表示MDC处于未启动状态

·starting表示MDC正在启动中，即对MDC正在执行**mdc start**命令

·active表示MDC正常运行

·updating表示正在给MDC分配接口板，即对MDC执行**location**命令

·stopping表示MDC正在停止，即MDC正在执行**undo** **mdc start**命令

【相关命令】

·**mdc**

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- display mdc interface**

------------------------------------------------------------------------

**[display mdc interface**]命令用来显示MDC的接口列表。

【命令】

**[display mdc ** **name** *mdc-name* ] **interface**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** mdc-name*]：显示指定MDC的接口列表。*mdc-name*表示MDC的名称，为1～15个字符的字符串。不指定该参数时，显示所有MDC的接口列表。

【举例】

\# 显示所有MDC的接口列表。

\<Sysname\> display mdc interface

 MDC Admin\'s interface(s):

  M-Ethernet1/0/1                    Fc0/2/7

  FortyGigE0/1/8                     GigabitEthernet1/0/2

  GigabitEthernet1/0/3

 MDC sub1\'s interface(s):

  GigabitEthernet1/0/4                Ten-GigabitEthernet1/1/5

  Ten-GigabitEthernet1/1/6

【相关命令】

·**allocate interface**

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- display mdc resource**

------------------------------------------------------------------------

**[display mdc resource**]命令用来显示MDC对CPU/磁盘/内存资源的使用情况。

【命令】

集中式设备：

**[display mdc **[ **name** *mdc-name*  **resource** [ **cpu** \| **disk** \| **memory**]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mdc **[ **name** *mdc-name*  **resource** [ **cpu** \| **disk** \| **memory**]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display mdc **[ **name** *mdc-name*  **resource** [ **cpu** \| **disk** \| **memory** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** mdc-name*]：显示指定MDC对CPU/磁盘/内存资源的使用情况。*mdc-name*表示MDC的名称，为1～15个字符的字符串。不指定该参数时，显示所有MDC对CPU/磁盘/内存资源的使用情况。

**[cpu**]：显示MDC的CPU使用情况。

**[disk**]：显示MDC的磁盘使用情况。

**[memory**]：显示MDC的内存使用情况。

**[slot** *slot-number*]：显示MDC对指定单板上CPU/磁盘/内存资源的使用情况，*slot-number*表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示MDC对指定成员设备上CPU/磁盘/内存资源的使用情况，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示MDC对指定成员设备指定单板上CPU/磁盘/内存资源的使用情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示MDC对指定CPU的CPU/磁盘/内存资源的使用情况，*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示所有MDC对CPU/磁盘/内存资源的使用情况。（集中式设备/分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display mdc resource

Memory usage:

Slot 0 CPU 0:

Used 207.2MB, Free 288.7MB, Total 495.9MB

  ID    Name             Quota(MB)    Used(MB)    Available(MB)

  1     Admin            495.9        172.1        288.7

  2     sub1             495.9        17.9         288.7

  3     sub2             495.9        17.2         288.7

CPU usage:

Slot 0 CPU 0:

  ID    Name             Weight       Usage(%)

  1     Admin            10           1

  2     sub1             10           0

  3     sub2             10           0

Disk usage:

Slot 0 CPU 0:

flash: Used 0.7MB, Free 461.2MB, Total 461.9MB

  ID    Name             Quota(MB)    Used(MB)     Available(MB)

  1     Admin            461.9        0.5          461.2

  2     sub1             461.9        0.1          461.2

  3     sub2             461.9        0.1          461.2

\# 显示所有单板上MDC对CPU/磁盘/内存资源的使用情况。（分布式设备－IRF模式）

\<Sysname\> display mdc resource

Memory usage:

Chassis 1 slot 0 CPU 0:

Used 238.1MB, Free 249.3MB, Total 487.4MB

  ID    Name             Quota(MB)    Used(MB)    Free(MB)

  1     Admin            487.4        206.0       249.3

  2     MyDevice         487.4        32.1        249.3

Chassis 1 slot 1 CPU 0:

Used 218.3MB, Free 270.1MB, Total 487.4MB

  ID    Name             Quota(MB)    Used(MB)    Free(MB)

  1     Admin            487.4        188.2       270.1

  2     MyDevice         487.4        30.1        270.1

CPU usage:

Chassis 1 slot 0 CPU 0:

  ID    Name             Weight       Usage(%)

  1     Admin            10           24

  2     MyDevice         10           0  

Chassis 1 slot 1 CPU 0:

  ID    Name             Weight       Usage(%)

  1     Admin            10           24

  2     MyDevice         10           0

Disk usage:

Chassis 1 slot 0 CPU 0:

cfa0: Used 83.4MB, Free 163.1MB, Total 246.5MB

  ID    Name             Quota(MB)    Used(MB)    Free(MB)

  1     Admin            221.9        83.4        138.5

  2     MyDevice         46.3         0.1         46.2

Chassis 1 slot 1 CPU 0:

cfa0: Used 44.8MB, Free 201.7MB, Total 246.5MB

  ID    Name             Quota(MB)    Used(MB)    Free(MB)

  1     Admin            410.5        44.8        201.7

  2     MyDevice         40           0.0         40

表1-2 display mdc resource命令显示信息描述表

字段

描述

Memory usage

表示下面显示的是内存的使用情况

CPU usage

表示下面显示的是CPU的使用情况

Disk usage

表示下面显示的是磁盘的使用情况

Slot 0 CPU 0

表示MDC在指定CPU上资源的使用情况（集中式设备/分布式设备－独立运行模式/集中式IRF设备）

Chassis 1 slot 0 CPU 0

表示MDC在指定CPU上资源的使用情况（分布式设备－IRF模式）

Used 238.1MB, Free 249.3MB, Total 487.4MB

内存的使用情况，Used表示内存已使用空间的大小（单位为MB），Free表示当前空闲内存的大小（单位为MB），Total表示整个内存大小（单位为MB）

Cfa0:: Used 0,  Free 61, Total 61

Cfa0表示磁盘的名称，Used表示整个磁盘已使用空间的大小（单位为MB），Free表示整个磁盘当前空闲空间的大小（单位为MB），Total表示整个磁盘空间大小（单位为MB）

ID

MDC的编号

Name

MDC的名称

Weight

MDC使用CPU的权重值

Usage(%)

指定MDC对指定单板上CPU的实际占用率（用百分比表示）

Quota(MB)

MDC使用磁盘/内存的限制值，单位MB

Used(MB)

MDC当前已使用的磁盘/内存空间的大小，单位MB

Available(MB)

MDC还可以使用的磁盘/内存空间的大小，单位MB

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- limit-resource cpu**

------------------------------------------------------------------------

**[limit-resource cpu**]命令用来配置MDC的CPU权重。

**[undo limit-resource cpu**]命令用来恢复缺省情况。

【命令】

**[limit-resource cpu** **weight** *weight-value*]

**[undo** **limit-resource cpu**]

【缺省情况】

各MDC的CPU权重均为10。（集中式设备）

各MDC在所有成员设备上的CPU权重均为10（集中式IRF设备）

缺省MDC在所有单板上的CPU权重均为10（不能修改）。非缺省MDC在所有具有使用权限的单板上的CPU权重均为10（分布式设备－独立运行模式/分布式设备－IRF模式）

【视图】

MDC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[weight ***weight-value*]：表示MDC在指定单板上的CPU权重，取值范围为1～10。

【使用指导】

系统根据MDC的CPU权重为MDC分配CPU资源。比如当系统CPU较忙时，3个MDC运行都需要占用较多CPU，且其权重分别为10、10、5，则系统为第一个MDC分配的CPU时间和为第二个MDC分配的时间近似都是为第三个MDC分配的CPU时间的2倍，此时和配置权重值分别为2、2、1效果一致。

配置本命令后，MDC在主控板和自己拥有的接口板上都将获得相同的CPU权重。MDC拥有的接口板需要通过**location**命令来分配。（分布式设备－独立运行模式/分布式设备－IRF模式）

配置本命令后，MDC在IRF所有成员设备上都将获得相同的CPU权重。（集中式IRF设备）

【举例】

\# 配置MDC sub1的CPU权重为2。

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 limit-resource cpu weight 2

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- limit-resource disk**

------------------------------------------------------------------------

**[limit-resource disk**]命令用来配置MDC可使用的磁盘空间上限（用百分比表示）。

**[undo limit-resource disk**]命令用来恢复到缺省情况。

【命令】

集中式设备：

**[limit-resource disk ratio ***limit-ratio*]

**[undo limit-resource disk**]

分布式设备－独立运行模式/集中式IRF设备：

**[limit-resource disk slot** *slot-number* [ **cpu** *cpu-number*  **ratio** *limit-ratio*]]

**[undo limit-resource disk** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[limit-resource disk chassis*** chassis-number ***slot ***slot-number***** **cpu** *cpu-number* ] **ratio** *limit-ratio*

**[undo limit-resource disk** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【缺省情况】

所有MDC共享物理设备上的所有磁盘空间，每个MDC可使用的磁盘空间上限为空闲磁盘空间值。

【视图】

MDC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：表示IRF中指定成员设备上的指定主控板。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ratio ***limit-ratio*]：表示MDC最多可使用的磁盘空间大小与设备整个磁盘空间大小的百分比，取值范围为1～100。（集中式设备）

**[ratio ***limit-ratio*]：表示MDC在指定单板上最多可使用的磁盘空间大小与该单板整个磁盘空间大小的百分比，取值范围为1～100。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[ratio ***limit-ratio*]：表示MDC在指定成员设备上最多可使用的磁盘空间大小与该成员设备整个磁盘空间大小的百分比，取值范围为1～100。（集中式IRF设备）

【使用指导】

执行**limit-resource disk**命令前，请使用**display mdc resource**命令可查看MDC当前实际已经使用的磁盘空间大小。配置值应大于MDC当前实际已经使用的磁盘空间大小，否则，会导致MDC申请新的磁盘空间失败，从而无法进行文件夹创建、文件拷贝和保存等操作。

【举例】

\# 配置MDC sub1最多可使用设备磁盘空间的30%。（集中式设备）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 limit-resource disk ratio 30

\# 配置MDC sub1最多可使用1号主控板磁盘空间的30%。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 limit-resource disk slot 1 ratio 30

\# 配置MDC sub1最多可使用2号成员设备磁盘空间的30%。（集中式IRF设备）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 limit-resource disk slot 2 ratio 30

\#配置MDC sub1最多可使用2号成员设备1号主控板磁盘空间的30%。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 limit-resource disk chassis 2 slot 1 ratio 30

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- limit-resource memory**

------------------------------------------------------------------------

**[limit-resource memory**]命令用来配置MDC可使用的内存上限（用百分比表示）。

**[undo limit-resource memory**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[limit-resource memory ratio ***limit-ratio*]

**[undo limit-resource memory**]

分布式设备－独立运行模式/集中式IRF设备：

**[limit-resource memory** **slot** *slot-number* [ **cpu** *cpu-number*  **ratio** *limit-ratio*]]

**[undo limit-resource memory** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[limit-resource memory** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  **ratio** *limit-ratio*]]

**[undo limit-resource memory** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【缺省情况】

所有MDC共享物理设备上的内存，每个MDC可使用的内存上限为空闲内存大小。

【视图】

MDC视图

【缺省用户角色】

network-admin

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：表示IRF中指定成员设备上的指定单板。（分布式设备－IRF模式）

**[cpu ***cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ratio ***limit-ratio*]：表示MDC在指定单板上最多可使用的内存大小与该设备整个内存大小的百分比，取值范围为1～100。（集中式设备）

**[ratio ***limit-ratio*]：表示MDC在指定单板上最多可使用的内存大小与该单板整个内存大小的百分比，取值范围为1～100。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[ratio ***limit-ratio*]：表示MDC在指定单板上最多可使用的内存大小与该成员设备整个内存大小的百分比，取值范围为1～100。（集中式IRF设备）

【使用指导】

使用本命令相当于给一台MDC分配内存，如果内存分配过小，会影响MDC启动，请保证所配置内存限制大于MDC启动所需内存。

【举例】

\# 配置MDC sub1最多可使用设备内存的30%。（集中式设备）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-MDC-2-sub1 limit-resource memory ratio 30

\# 配置MDC sub1最多可使用1号单板内存的30%。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-MDC-2-sub1 limit-resource memory slot 1 ratio 30

\# 配置MDC sub1最多可使用2号成员设备内存的30%。（集中式IRF设备）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-MDC-2-sub1 limit-resource memory slot 2 ratio 30

\#配置MDC sub1最多可使用2号成员设备1号单板内存的30%。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-MDC-2-sub1 limit-resource memory chassis 2 slot 1 ratio 30

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- location**

------------------------------------------------------------------------

![说明](MDC命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[location**]命令用来将接口板的使用权限分配给MDC。

**[undo** **location**]命令用来取消分配。

【命令】

分布式设备－独立运行模式：

**[location slot** *slot-number*]

**[undo** **location slot** *slot-number*]

分布式设备－IRF模式：

**[location chassis** *chassis-number* **slot** *slot-number*]

**[undo** **location chassis** *chassis-number* **slot** *slot-number*]

【缺省情况】

缺省MDC可以使用物理设备上的所有接口板，非缺省MDC不能使用。

【视图】

MDC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[chassis** *chassis-number* **slot** *slot-number*]：表示IRF中指定成员设备上的指定单板。（分布式设备－IRF模式）

【使用指导】

只有将接口板的使用权限分配给MDC后，才能将接口板上的接口分配给MDC。

在不同MDC视图下执行该命令可以将同一接口板的使用权限分配给多个MDC。

【举例】

\# 将3号接口板的使用权限分配给MDC sub1。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 location slot 3

\# 将2号成员设备的3号接口板的使用权限分配给MDC sub1。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 location chassis 2 slot 3

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- switchto mdc**

------------------------------------------------------------------------

**[switchto mdc**]命令用来登录指定MDC，命令行视图将从缺省MDC的系统视图切换到指定MDC的用户视图。

【命令】

**[switchto mdc **]*[mdc-name*]{.ItemListChar}

【视图】

系统视图

【缺省用户角色】

network-admin

network-operator

【参数】

*mdc-name*{.ItemListChar}：MDC的名称，为1～15个字符的字符串。必须是当前设备上已经启动的MDC的名称。

【使用指导】

只有MDC处于active状态时，才允许使用该命令来登录MDC。

【举例】

\# 切换到MDC sub1。

\<Sysname\> system-view

Sysname switchto mdc sub1

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2011 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*

\* Without the owner\'s prior written consent,                                 \*

\* no decompiling or reverse-engineering shall be allowed.                    \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\<Sysname\>

\<Sysname\> display mdc

ID         Name            Status

2          sub1            active

【相关命令】

·**switchback**

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- mdc**

------------------------------------------------------------------------

**[mdc**]命令用来创建MDC，并进入MDC视图（如果指定的MDC已经存在，则直接进入MDC视图）。

**[undo mdc**]命令用来删除一个已经存在的MDC。

【命令】

**[mdc **]*[mdc-name*]{.ItemListChar} [ **id** *mdc-id* ]

**[undo** **mdc** ]*[mdc-name*]{.ItemListChar}

【缺省情况】

设备上有一个MDC（缺省MDC），该MDC的名称为Admin，编号为1。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

*mdc-name*{.ItemListChar}：MDC的名称，为1～15个字符的字符串，区分大小写。

**id*** mdc-id*{.ItemListChar}：MDC{.ItemListChar}的编号，取值范围与设备的型号有关，请以设备的实际情况为准。不指定该参数时，系统会给MDC{.ItemListChar}自动分配一个目前可用的最小的编号。{.ItemListChar}

【使用指导】

·缺省MDC不需要创建，不能删除。

·多次执行该命令可以创建多个MDC，不同型号的设备支持的MDC总个数不同，请以设备的实际情况为准。

·进入指定MDC视图时，可以不输入*[mdc-id*]{.ItemListChar}。但如果输入，则必须和MDC当前的编号一致，否则会提示错误信息。

·删除MDC后，该MDC下的磁盘文件以及配置都会丢失，并且不能恢复，请谨慎使用删除MDC功能。

【举例】

\# 创建MDC，名称为sub1。

\<Sysname\> system-view

Sysname mdc sub1

It will take some time to create MDC\...

MDC created successfully.

【相关命令】

·**display mdc**

**MDC \-- 缺省MDC上支持的MDC配置命令 \-- mdc start**

------------------------------------------------------------------------

**[mdc **]**[start**]{.ItemListChar}命令用来启动当前MDC。

**[undo mdc **]**[start**]{.ItemListChar}命令用来停止当前MDC。

【命令】

**[mdc **]**[start**]{.ItemListChar}

**[undo** **mdc** ]**[start**]{.ItemListChar}

【视图】

MDC视图

【缺省用户角色】

network-admin

【使用指导】

创建MDC相当于构造了一台新的物理设备。创建后需要执行**mdc ****[start**]{.ItemListChar}命令，才能完成新MDC的初始化，相当于上电启动。启动后，用户可以登录到该MDC执行配置以及查看操作。

需要注意的是：

·停止MDC会导致该MDC的业务中断，登录该MDC的用户自动退出，请谨慎使用该功能。

·停止MDC前请保存MDC的配置，否则，直接停止MDC可能导致MDC的当前配置丢失。

【举例】

\# 启动MDC sub1。

\<Sysname\> system-view

Sysname mdc sub1

Sysname-mdc-2-sub1 mdc start

It will take some time to start MDC\...

MDC started successfully.

**MDC \-- 非缺省MDC上支持的MDC配置命令 \-- display mdc**

------------------------------------------------------------------------

**[display mdc**]命令用来显示本MDC的相关信息，包括本MDC的编号、名称和状态。

【命令】

**[display mdc**]

【视图】

任意视图

【缺省用户角色】

mdc-admin

mdc-operator

【举例】

\# 显示本MDC的相关信息。

\<sub1\> display mdc

ID      Name         Status

2       sub1         active

显示信息描述请参见 表1-1(#_0_11418_x2016_x2090198087)。

**MDC \-- 非缺省MDC上支持的MDC配置命令 \-- display mdc interface**

------------------------------------------------------------------------

**[display mdc interface**]命令用来显示本MDC的接口列表。

【命令】

**[display mdc interface**]

【视图】

任意视图

【缺省用户角色】

mdc-admin

mdc-operator

【举例】

\# 显示本MDC的接口列表。

\<sub1\> display mdc interface

 MDC sub1\'s interface(s):

  M-Ethernet1/0/1                    GigabitEthernet1/0/2

  Ten-GigabitEthernet1/1/5           Ten-GigabitEthernet1/1/6

**MDC \-- 非缺省MDC上支持的MDC配置命令 \-- display mdc resource**

------------------------------------------------------------------------

**[display mdc resource**]命令用来显示MDC对CPU/磁盘/内存资源的使用情况。

【命令】

集中式设备：

**[display mdc**[ **resource** [ **cpu** \| **disk** \| **memory**]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mdc resource **[ **cpu** [\| **disk** \| **memory** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display mdc resource **[ **cpu** [\| **disk** \| **memory** ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

mdc-admin

mdc-operator

【参数】

**[cpu**]：显示MDC的CPU使用情况。

**[disk**]：显示MDC的磁盘使用情况。

**[memory**]：显示MDC的内存使用情况。

**[slot** *slot-number*]：显示MDC对指定单板上CPU/磁盘/内存资源的使用情况，*slot-number*表示单板所在的槽位号。不指定该参数时，显示MDC对所有单板上CPU/磁盘/内存资源的使用情况。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示MDC对指定成员设备上CPU/磁盘/内存资源的使用情况，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示MDC对所有成员设备上CPU/磁盘/内存资源的使用情况。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示MDC对指定成员设备指定单板上CPU/磁盘/内存资源的使用情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，显示MDC对IRF中所有单板上CPU/磁盘/内存资源的使用情况。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示MDC对指定CPU的CPU/磁盘/内存资源的使用情况，*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示MDC对CPU/磁盘/内存资源的使用情况。（集中式设备/分布式设备－独立运行模式/集中式IRF设备）

\<sub1\> display mdc resource

Memory usage:

Slot 0 CPU 0:

Used 232.3MB, Free 263.6MB, Total 495.9MB

  ID    Name             Quota(MB)    Used(MB)    Available(MB)

  2     sub1             495.9        42.7         263.6

CPU usage:

Slot 0 CPU 0:

  ID    Name             Weight       Usage(%)

  2     sub1             10           0

Disk usage:

Slot 0 CPU 0:

flash: Used 0.7MB, Free 461.2MB, Total 461.9MB

  ID    Name             Quota(MB)    Used(MB)     Available(MB)

  2     sub1             461.9        0.1          461.2

\# 显示MDC对CPU/磁盘/内存资源的使用情况。（分布式设备－IRF模式）

\<sub1\> display mdc resource

Memory usage:

Chassis 1 slot 0 CPU 0:

Used 238.1MB, Free 249.3MB, Total 487.4MB

  ID    Name             Quota(MB)    Used(MB)    Free(MB)

  2     sub1             487.4        32.1        249.3

Chassis 1 slot 1 CPU 0:

Used 218.3MB, Free 270.1MB, Total 487.4MB

  ID    Name             Quota(MB)    Used(MB)    Free(MB)

  2     sub1             487.4        30.1        270.1

CPU usage:

Chassis 1 slot 0 CPU 0:

  ID    Name             Weight       Usage(%)

  2     MyDevice         10           0  

Chassis 1 slot 1 CPU 0:

  ID    Name             Weight       Usage(%)

  2     sub1             10           0

Disk usage:

Chassis 1 slot 0 CPU 0:

cfa0: Used 83.4MB, Free 163.1MB, Total 246.5MB

  ID    Name             Quota(MB)    Used(MB)    Free(MB)

  2     sub1             46.3         0.1         46.2

Chassis 1 slot 1 CPU 0:

cfa0: Used 44.8MB, Free 201.7MB, Total 246.5MB

  ID    Name             Quota(MB)    Used(MB)    Free(MB)

  2     sub1             40           0.0         40

显示信息描述请参见 表1-2(#_0_11418_x2016_x1071380629)。

**MDC \-- 非缺省MDC上支持的MDC配置命令 \-- switchback**

------------------------------------------------------------------------

**[switchback**]命令用来从当前MDC切换回缺省MDC，命令行视图将从当前MDC的用户视图返回到缺省MDC的系统视图。

【命令】

**[switchback**]

【视图】

用户视图

【缺省用户角色】

mdc-admin

mdc-operator

【使用指导】

network-admin/network-operator使用**switchto**命令登录MDC后角色变为mdc-admin/mdc-operator。

只有通过执行**switchto**命令登录MDC的情况下可以使用**switchback**命令切换回缺省MDC。使用其它方式（比如通过MDC的以太网口直接Telnet）登录的情况不能使用该命令切换回缺省MDC。

【举例】

\# 由本MDC返回缺省MDC。

\<sub1\> switchback

Sysname

【相关命令】

·**switchto mdc**
