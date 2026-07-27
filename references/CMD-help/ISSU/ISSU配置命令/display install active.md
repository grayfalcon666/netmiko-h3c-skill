<!-- CMD-INDEX
  display install active              | 任意视图             | L35
  display install backup              | 任意视图             | L419
  display install committed           | 任意视图             | L565
  display install inactive            | 任意视图             | L713
  display install ipe-info            | 任意视图             | L803
  display install job                 | 任意视图             | L857
  display install log                 | 任意视图             | L909
  display install package             | 任意视图             | L1043
  display install rollback            | 任意视图             | L1137
  display install which               | 任意视图             | L1209
  display issu rollback-timer         | 任意视图             | L1293
  display issu state                  | 任意视图             | L1371
  display version comp-matrix         | ]                | L1805
  install abort                       | 用户视图             | L2791
  install activate                    | 用户视图             | L2827
  install add                         | 用户视图             | L3271
  install commit                      | 用户视图             | L3325
  install deactivate                  | 用户视图             | L3373
  install remove                      | 用户视图             | L3481
  install rollback to                 | 用户视图             | L3541
  install verify                      | 用户视图             | L3627
  issu accept                         | 用户视图             | L3837
  issu blade                          | 用户视图             | L3879
  issu commit                         |                  | L4043
  issu load                           |                  | L4327
  issu pex                            | 用户视图             | L5027
  issu rollback                       | 用户视图             | L5239
  issu rollback-timer                 | 系统视图             | L5303
  issu run switchover                 | 用户视图             | L5363
  reset install log-history oldest    | 用户视图             | L5695
  reset install rollback oldest       | 用户视图             | L5731
-->

**ISSU \-- ISSU配置命令 \-- display install active**

------------------------------------------------------------------------

**[display install active**]命令用来显示当前系统中处于激活状态的软件包的相关信息。

【命令】

集中式设备：

**[display install active** [ **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display install active** [ **slot** *slot-number*   **verbose** ]]

分布式设备－IRF模式：

**[display install active** [ **chassis** *chassis-number* **slot** *slot-number*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示IRF中的所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示IRF中的所有成员设备/PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[verbose**]：显示处于激活状态的软件包的详细信息，包括软件包的名称、基本信息和所包含的组件。不指定该参数时，仅显示软件包的名称。

【举例】

\# 显示设备上处于激活状态的软件包的简要信息。（集中式设备）

\<Sysname\> display install active

Active packages on the device:

  flash:/boot.bin

  flash:/system.bin

  flash:/feature.bin

\# 显示设备上处于激活状态的软件包的简要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display install active

Active packages on slot 1:

  flash:/boot.bin

  flash:/system.bin

  flash:/feature.bin

\# 显示设备上处于激活状态的软件包的简要信息。（分布式设备－IRF模式）

\<Sysname\> display install active

Active packages on chassis 1 slot 1:

  flash:/boot.bin

  flash:/system.bin

  flash:/feature.bin

\# 显示设备上处于激活状态的软件包的详细信息。（集中式设备）

\<Sysname\> display install active verbose

Active packages on the device:

  flash:/boot.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: boot

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: cen

 Component

 Component: boot

 Description: boot package

flash:/system.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: system

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: cen

 Component

 Component: system

 Description: system package

flash:/feature.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: test

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: cen

 Component

 Component: test

 Description: test package

\# 显示设备上处于激活状态的软件包的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display install active verbose

Active packages on slot 1:

flash:/boot.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: boot

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: mpu

 Component

 Component: boot

 Description: boot package

flash:/system.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: system

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: mpu

 Component

 Component: system

 Description: system package

flash:/feature.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: test

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: mpu

 Component

 Component: test

 Description: test package

\# 显示设备上处于激活状态的软件包的详细信息。（分布式设备－IRF模式）

\<Sysname\> display install active verbose

Active packages on chassis 1 slot 1:

flash:/boot.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: boot

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: mpu

 Component

 Component: boot

 Description: boot package

flash:/system.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: system

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: mpu

 Component

 Component: system

 Description: system package

flash:/feature.bin

 Package

 Vendor: XXX

 Product: xxxx

 Service name: test

 Platform version: 7.1.022

 Product version: Test 2201

 Supported board: mpu

 Component

 Component: test

 Description: test package

表1-1 display install active命令显示信息描述表

字段

描述

Active packages on the device

设备上处于激活状态的软件包的相关信息（集中式设备）

Active packages on slot *n*

某单板上处于激活状态的软件包的相关信息，其中*n*表示该单板所在的槽位号（分布式设备－独立运行模式）

Active packages on slot *n*

某成员设备上处于激活状态的软件包的相关信息，其中*n*表示设备在IRF中的成员编号（集中式IRF设备）

Active packages on chassis *m* slot *n*

某单板上处于激活状态的软件包的相关信息，其中*m*表示设备在IRF中的成员编号，*n*表示成员设备上该单板所在的槽位号（分布式设备－IRF模式）

flash:/boot.bin

软件包的名称

Package

软件包的信息

Vendor

生产厂商

Product

产品名称

Service name

软件包所包含的服务名称：

·如果显示为boot，表示该软件包为Boot包

·如果显示为system，表示该软件包为System包

·如果显示为patch，表示该软件包为补丁包

·如果显示为其它值，则表示该软件包为提供某项功能的Feature包

Platform version

平台软件版本号

Product version

产品软件版本号

Supported board

软件包支持的单板类型（本字段的取值与设备的型号有关，请以设备的实际情况为准）：

·cen表示集中式设备

·mpu表示主控板

·lc表示业务板

·sfc表示网板

Component

组件信息，表示软件包的组成部分

Component

组件的名称

Description

组件的描述信息

【相关命令】

·**install active**

**ISSU \-- ISSU配置命令 \-- display install backup**

------------------------------------------------------------------------

**[display install backup**]命令用来显示设备下次启动时使用的备用软件包的相关信息。

【命令】

集中式设备：

**[display install backup** [ **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display install backup** [ **slot** *slot-number* **cpu***cpu-number*  ]  **verbose** ]

分布式设备－IRF模式：

**[display install backup** [ **chassis** *chassis-number* **slot** *slot-number* **cpu***cpu-number*  ]  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示IRF中的所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者本地有存储介质的PEX的虚拟槽位号。不指定该参数时，表示IRF中的所有成员设备和本地有存储介质的PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者本地有存储介质的PEX对应的虚拟框号，*slot-number*表示单板/本地有存储介质的PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板和本地有存储介质的PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示安全引擎的CPU编号。本参数专用于显示安全引擎下次启动时使用的备用软件包的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[verbose**]：显示详细信息，包括软件包的名称、基本信息和所包含的组件。不指定该参数时，仅显示软件包的名称。

【使用指导】

设备下次启动时使用的软件包的名称会记录在启动软件包列表中，启动软件包列表分为主用启动软件包列表和备用启动软件包列表，可以分别配置。

·当设备启动时，优先使用主用启动软件包列表中的软件包。

·如果主用启动软件包列表中的Boot包或System包不存在或者损坏，再使用备用启动软件包列表中的软件包。

执行**boot-loader file**命令可以修改设备下次启动时使用的备用软件包列表。

【举例】

\# 显示设备下次启动时使用的备用软件包的相关信息。（集中式设备）

\<Sysname\> display install backup

Backup startup software images on the device:

  flash:/boot-a0201.bin

  flash:/system-a0201.bin

\# 显示设备下次启动时使用的备用软件包的相关信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display install backup

Backup startup software images on slot 1:

  flash:/boot-a0201.bin

  flash:/system-a0201.bin

\# 显示设备下次启动时使用的备用软件包的相关信息。（分布式设备－IRF模式）

\<Sysname\> display install backup

Backup startup software images on chassis 1 slot 1:

  flash:/boot-a0201.bin

  flash:/system-a0201.bin

\# 显示设备下次启动时使用的备用软件包的详细信息。

\<Sysname\> display install backup verbose

Backup startup software images on slot 1:

 flash:/boot-a0201.bin

 Package

 Vendor: H3C

 Product: xxxx

 Service name: boot

 Platform version: 7.1

 Product version: Beta 1330

 Supported board: mpu

 Component

 Component: boot

 Description: boot package

 flash:/system-a0201.bin

 Package

 Vendor: H3C

 Product: xxxx

 Service name: system

 Platform version: 7.1

 Product version: Beta 1330

 Supported board: mr, lc, sfc

 Component

 Component: system

 Description: system package

本命令显示信息的描述请参见 表1-1(?2076033456#_Ref302142357)。

【相关命令】

·**boot-loader file**（基础配置命令参考/软件升级）

·**display install committed**

**ISSU \-- ISSU配置命令 \-- display install committed**

------------------------------------------------------------------------

**[display install committed**]命令用来显示设备下次启动时使用的主用软件包的相关信息。

【命令】

集中式设备：

**[display install committed** [ **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display install committed** [ **slot** *slot-number* **cpu***cpu-number*  ]  **verbose** ]

分布式设备－IRF模式：

**[display install committed** [ **chassis** *chassis-number* **slot** *slot-number* **cpu***cpu-number*  ]  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示IRF中的所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示IRF中的所有成员设备/PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示安全引擎的CPU编号。本参数专用于显示安全引擎下次启动时使用的主用软件包的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[verbose**]：显示详细信息，包括软件包的名称、基本信息和所包含的组件。不指定该参数时，仅显示软件包的名称。

【使用指导】

在设备上执行**install commit**命令确认运行当前的软件包后，这些软件包会被列入主用下次启动软件包，以便设备重启后，这些软件包能够继续生效。

执行**boot-loader file**命令可以修改设备下次启动时使用的主用软件包列表。

【举例】

\# 显示设备下次启动时使用的主用软件包的相关信息。

\<Sysname\> display install committed

Committed packages on slot 1:

 flash:/boot-a0201.bin

 flash:/system-a0201.bin

 flash:/feature.bin

\# 显示设备下次启动时使用的主用软件包的详细信息。

\<Sysname\> display install committed verbose

Committed packages on slot 1:

 flash:/boot-a0201.bin

 Package

 Vendor: H3C

 Product: xxxx

 Service name: boot

 Platform version: 7.1

 Product version: Beta 1330

 Supported board: mr, lc, sfc

 Component

 Component: boot

 Description: boot package

 flash:/system-a0201.bin

 Package

 Vendor: H3C

 Product: xxxx

 Service name: system

 Platform version: 7.1

 Product version: Beta 1330

 Supported board: mr, lc, sfc

 Component

 Component: system

 Description: system package

flash:/ssh-feature.bin

 Package

 Vendor: H3C

 Product: xxxx

 Service name: ssh

 Platform version: 7.1

 Product version: Beta 1330

 Supported board: mr, lc, sfc

 Component

 Component: ssh

 Description: ssh package

本命令显示信息的描述请参见 表1-1(?2076033456#_Ref302142357)。

【相关命令】

·**boot-loader file**（基础配置命令参考/软件升级）

·**display install backup**

·**install commit**

**ISSU \-- ISSU配置命令 \-- display install inactive**

------------------------------------------------------------------------

**[display install inactive**]命令用来显示存储介质根目录下、没有被激活的所有软件包的相关信息。

【命令】

集中式设备：

**[display install inactive** [ **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display install inactive** [ **slot** *slot-number* **cpu***cpu-number*  ]  **verbose** ]

分布式设备－IRF模式：

**[display install inactive** [ **chassis** *chassis-number* **slot** *slot-number* **cpu***cpu-number*  ]  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示IRF中的所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者本地有存储介质的PEX的虚拟槽位号。不指定该参数时，表示IRF中的所有成员设备和本地有存储介质的PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者本地有存储介质的PEX对应的虚拟框号，*slot-number*表示单板/本地有存储介质的PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板和本地有存储介质的PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示安全引擎的CPU编号。本参数专用于显示安全引擎存储介质根目录下、没有被激活的所有软件包的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[verbose**]：显示详细信息，包括软件包的名称、基本信息和所包含的组件。不指定该参数时，仅显示软件包的名称。

【举例】

\# 显示存储介质根目录下、没有被激活的所有软件包的简要信息。

\<Sysname\> display install inactive

Inactive packages on slot 1:

 flash:/ssh-feature.bin

\# 显示存储介质根目录下、没有被激活的所有软件包的详细信息。

\<Sysname\> display install inactive verbose

Inactive packages on slot 1:

flash:/ssh-feature.bin

 Package

 Vendor: H3C

 Product: XXXX

 Service name: ssh

 Platform version: 7.1

 Product version: Beta 1330

 Supported board: mr, lc, sfc

 Component

 Component: ssh

 Description: ssh package

本命令显示信息的描述请参见 表1-1(?2076033456#_Ref302142357)。

【相关命令】

·**install deactivate**

**ISSU \-- ISSU配置命令 \-- display install ipe-info**

------------------------------------------------------------------------

**[display install ipe-info**]命令用来显示IPE文件包含的软件包列表。

【命令】

**[display install ipe-info** *ipe-filename*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[ipe-filename*]：表示IPE文件名，以.ipe作为后缀名，从存储介质名开始为1～63个字符的字符串（包括存储介质名在内），不区分大小写。如果该IPE文件不存在，命令执行失败。

【使用指导】

IPE文件是一个或多个软件包的集合。用户获得该IPE文件后，可以选择其中的软件包进行升级。

当配置该命令时，命令中指定的IPE文件必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.ipe。（集中式设备）

当配置该命令时，命令中指定的IPE文件必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.ipe或者slot*n*#flash:/xx.ipe，*n*为备用主控板所在的槽位号或者PEX设备的虚拟槽位号。（分布式设备－独立运行模式）

当配置该命令时，命令中指定的IPE文件必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.ipe或者slot*n*#flash:/xx.ipe，*n*为从设备的成员编号或者PEX设备的虚拟槽位号。（集中式IRF设备）

当配置该命令时，命令中指定的IPE文件必须放在存储介质的根目录下，文件名中必须含存储介质的名称，形如flash:/xx.ipe或者chassis*m*#slot*n*#flash:/startup-boot.ipe，chassis*m*#slot*n*用于指定全局备用主控板或者PEX设备的虚拟槽位号。（分布式设备－IRF模式）

【举例】

\# 显示flash:/test.ipe的IPE信息。

\<Sysname\> display install ipe-info flash:/test.ipe

Verifying the file flash:/test.ipe on the device\...\...\...\...\....Done.

H3C Device images in IPE:

  boot.bin

  system.bin

【相关命令】

·**display install package**

**ISSU \-- ISSU配置命令 \-- display install job**

------------------------------------------------------------------------

**[display install job**]命令用来显示系统中正在执行的激活、卸载或回滚操作。

【命令】

**[display install job**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【举例】

\# 显示系统中正在执行的激活、卸载、回滚三种ISSU操作。（集中式设备）

\<Sysname\> display install job

 JobID:5

  Action:install activate flash:/ssh-feature.bin on the device

以上显示信息表明：设备正在执行**install activate flash:/ssh-feature.bin**操作。

\# 显示系统中正在执行的激活、卸载、回滚三种ISSU操作。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display install job

 JobID:5

  Action:install activate flash:/ssh-feature.bin on slot 1

以上显示信息表明：设备正在执行**install activate flash:/ssh-feature.bin slot 1**操作。

\# 显示系统中正在执行的激活、卸载、回滚三种ISSU操作。（分布式设备－IRF模式）

\<Sysname\> display install job

 JobID:5

  Action:install activate flash:/ssh-feature.bin on chassis 1 slot 1

以上显示信息表明：设备正在执行**install activate flash:/ssh-feature.bin chassis 1 slot 1**操作。

**ISSU \-- ISSU配置命令 \-- display install log**

------------------------------------------------------------------------

**[display install log**]命令用来显示与ISSU升级相关的日志。

【命令】

**[display install log** [ *log-id*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[log-id*]：显示指定升级日志的信息。*log-id*表示升级日志的编号，不指定该参数时，则显示所有升级日志的信息。

**[verbose**]：表示显示日志的详细信息。不指定该参数时，仅显示日志的摘要信息。

【使用指导】

ISSU日志记录了软件包历史操作信息，每当用户执行一次安装、升级、卸载、删除、取消或回滚操作时，都会自动产生一条日志信息，记录下该操作的过程，以及操作结果是成功还是失败。每条日志均分配一个全局唯一的ID。

设备最多可保存50条ISSU日志，超出该规格时新日志会覆盖最老的日志。

【举例】

\# 显示所有显示与软件包升级相关的日志。

\<Sysname\> display install log

Install job 1 started by user root at 04/28/2001 08:39:29.

Job 1 completed successfully at 04/28/2001 08:39:30.

Install job 1 started by user root at 04/28/2001 08:39:29.

    Install activate flash:/ssh.bin on slot 1

Job 1 completed successfully at 04/28/2001 08:39:30.

Install job 1 started by user root at 04/28/2001 08:39:29.

Job 1 completed successfully at 04/28/2001 08:39:30.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Install job 2 started by user root at 04/28/2001 08:40:29.

Job 2 completed successfully at 04/28/2001 08:40:30.

Install job 2 started by user root at 04/28/2001 08:40:29.

    Install activate flash:/route.bin on slot 1

Job 2 completed successfully at 04/28/2001 08:40:30.

Install job 2 started by user root at 04/28/2001 08:40:29.

Job 2 completed successfully at 04/28/2001 08:40:30.

\# 显示系统中编号为1的软件包升级日志的详细信息。

\<Sysname\> display install log 1 verbose

Install job 1 started by user root at 04/28/2001 08:39:29.

Job 1 completed successfully at 04/28/2001 08:39:30.

Install job 1 started by user root at 04/28/2001 08:39:29.

    Install activate flash:/ssh.bin on slot 1

Job 1 completed successfully at 04/28/2001 08:39:30.

Install job 1 started by user root at 04/28/2001 08:39:29.

Job 1 completed successfully at 04/28/2001 08:39:30.

Detail of activating packages on slot 1.

    Get upgrade policy successfully.

Detail of activating packages on slot 1.

    Uncompress package to system successfully.

    Remove files from system successfully.

表1-2  display install log{.FigureDescriptionChar}命令显示信息描述{.FigureDescriptionChar}表

字段

描述

Install job 1 started by user root at 04/28/2001 08:39:29.

ISSU动作的执行者和执行时间

Job 1 completed successfully at 04/28/2001 08:39:30.

ISSU动作的完成时间

Install activate flash:/ssh.bin on slot 1

执行的ISSU动作

Detail of activating packages on slot 1.

激活包动作的详细信息

Get upgrade policy successfully

表示升级决策处理成功

Uncompress package to system successfully

解压软件包文件到系统成功

Remove files from system successfully

从系统中删除文件成功

【相关命令】

·**reset install log-history oldest**

**ISSU \-- ISSU配置命令 \-- display install package**

------------------------------------------------------------------------

**[display install package**]命令用来显示软件包的相关信息。

【命令】

**[display install package**[ { *filename* \| **all** } [ **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[filename*]：表示软件包的文件名，以.bin作为后缀名，为1～63个字符的字符串，不区分大小写。

**[all**]：表示设备上存储介质根目录下的所有软件包。（集中式设备）

**[all**]：表示主用主控板上存储介质根目录下的所有软件包。（分布式设备－独立运行模式）

**[all**]：表示主设备上存储介质根目录下的所有软件包。（集中式IRF设备）

**[all**]：表示全局主用主控板上存储介质根目录下的所有软件包。（分布式设备－IRF模式）

**[verbose**]：显示软件包的基本信息和软件包所包含的组件。不指定该参数时，仅显示软件包的基本信息。

【使用指导】

当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin。（集中式设备）

当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin或者slot*n*#flash:/xx.bin，*n*为备用主控板所在的槽位号或者PEX设备的虚拟槽位号。（分布式设备－独立运行模式）

当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin或者slot*n*#flash:/xx.bin，*n*为从设备的成员编号或者PEX设备的虚拟槽位号。（集中式IRF设备）

当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须含存储介质的名称，形如flash:/xx.bin或chassis*m*#slot*n*#flash:/startup-boot.bin，chassis*m*#slot*n*用于指定全局备用主控板或者PEX设备的虚拟槽位号。（分布式设备－IRF模式）

【举例】

\# 显示软件包system.bin的相关信息。

\<Sysname\> display install package flash:/system.bin

  flash:/system.bin

  Package

  Vendor: H3C

  Product: xxxx

  Service name: system

  Platform version: 7.1.022

  Product version: Beta 1330

  Supported board: mpu

\# 显示软件包system.bin的详细信息。

\<Sysname\> display install package flash:/system.bin verbose

  flash:/system.bin

  Package

  Vendor: H3C

  Product: xxxx

  Service name: system

  Platform version: 7.1.022

  Product version: Beta 1330

  Supported board: mpu

  Component

  Component: system

  Description: system package

本命令显示信息的描述请参见 表1-1(?2076033456#_Ref302142357)。

**ISSU \-- ISSU配置命令 \-- display install rollback**

------------------------------------------------------------------------

**[display install rollback**]命令用来显示回滚点的相关信息。

【命令】

**[display install rollback** [ *point-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[point-id*]：回滚点的编号。

【使用指导】

可以通过这个命令查看回滚点信息，以便进行相应的回滚操作。

issu命令升级过程中不会记录回滚点，因此，在issu命令升级过程中执行该命令，没有信息可显示。

【举例】

\# 显示回滚点的相关信息。

\<Sysname\> display install rollback

Install rollback information 1 on slot 1:

  Updating from flash:/route-1.bin

         to flash:/route-2.bin.

Install rollback information 2 on slot 1:

   Deactivating flash:/route-2.bin

以上显示信息表明：设备上共有两个回滚点，回滚点1是将flash:/route-1.bin升级到了flash:/route-2.bin，回滚点2是将flash:/route-2.bin卸载了。

表1-3 display install rollback命令显示信息描述表

字段

描述

Install rollback information *n*

回滚点信息，*n*为回滚点编号

Updating from *A* to *B*

从软件包*A*升级到软件包*B*，*A*和*B*为软件包的名称

Deactivating *A*

卸载软件包*A*，*A*为软件包的名称

【相关命令】

·**install rollback**

·**reset install rollback oldest**

**ISSU \-- ISSU配置命令 \-- display install which**

------------------------------------------------------------------------

**[display install which**]命令用来显示一个组件或文件的所属软件包，以及该软件包的相关信息。

【命令】

集中式设备：

**[display install which**[ { **component** *name* \| **file** *filename* }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display install which**[ { **component** *name* \| **file** *filename* } [ **slot** *slot-number* ]**cpu***cpu-number*  ]]

分布式设备－IRF模式：

**[display install which**[ { **component** *name* \| **file** *filename* } [ **chassis** *chassis-number* **slot** *slot-number* ]**cpu***cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[component*** name*]：软件包所包含的组件的名称。

**[file** *filename*]：软件包所包含的文件的名称，为1～63个字符的字符串，不区分大小写。必须为纯文件名的形式。系统查询时，只有名称完全相同（除了大小写），才认为匹配成功。

**[slot ***slot-number*]：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示IRF中的所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者本地有存储介质的PEX的虚拟槽位号。不指定该参数时，表示IRF中的所有成员设备和本地有存储介质的PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者本地有存储介质的PEX对应的虚拟框号，*slot-number*表示单板/本地有存储介质的PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板和本地有存储介质的PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示安全引擎的CPU编号。本参数专用于显示安全引擎上一个组件或文件属于哪个软件包以及该软件包的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

【使用指导】

当软件包运行错误，系统提示xx组件或者xx文件运行错误的时候，可以根据组件/文件的名字使用该命令查找它属于哪个软件包，从而帮助进一步定位是否是软件包本身有缺陷。

执行该命令后，系统会扫描指定slot存储介质的根目录下所有软件包，将包含该组件/文件的软件包都依次显示。

【举例】

\# 显示文件sshc.cli属于哪个软件包以及该软件包的相关信息。

\<Sysname\> display install which file sshc.cli

Verifying the file flash:/system.bin on the device\...Done. 

Verifying the file flash:/boot.bin on the device\...Done. 

File sshc.cli is in following packages on slot 1:

  flash:/system.bin

  Package

  Vendor: xxx

  Product: xxxx

  Service name: ssh

  Platform version: 7.1.022

  Product version: Beta 1330

  Supported board: mr, lc, sfc

本命令显示信息的描述请参见 表1-1(?2076033456#_Ref302142357)。

**ISSU \-- ISSU配置命令 \-- display issu rollback-timer**

------------------------------------------------------------------------

**[display issu rollback-timer**]命令用来显示回滚定时器的相关信息。

【命令】

**[display issu rollback-timer**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【使用指导】

因为新设置的回滚定时器时长会在下次ISSU升级中生效，因此，可能出现剩余时间大于定时器时长的情况。

【举例】

\# 执行**issu run switchover**命令后，显示回滚定时器的相关信息。

\<Sysname\> display issu rollback-timer

Rollback timer: Working

Rollback interval：45 minutes

Rollback time remaining : 40 minutes

\# 执行**issu accept**命令后，显示回滚定时器的相关信息。

\<Sysname\> display issu rollback-timer

Rollback timer: Not working

Rollback interval：30 minutes

\# 当前没有进行ISSU升级，显示回滚定时器的相关信息。

\<Sysname\> display issu rollback-timer

Rollback timer: Not working

Rollback interval：45 minutes

表1-4 display issu rollback-timer命令显示信息描述表

字段

描述

Rollback timer

回滚定时器是否处于工作状态：

·Working：回滚定时器已经启动

·Not working：回滚定时器没有启动或者已经超时

Rollback interval

用户配置的回滚定时器的时间，单位为分钟

Rollback time remaining

距离回滚定时器超时的时间，单位为分钟

【相关命令】

·**issu rollback-timer**

**ISSU \-- ISSU配置命令 \-- display issu state**

------------------------------------------------------------------------

**[display issu state**]命令用来显示当前ISSU升级所处的状态，以及ISSU升级的相关信息。

【命令】

**[display issu state**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【使用指导】

**[issu**]命令升级需要经过一系列的操作步骤，升级过程中有严格的步骤要求，执行升级步骤会导致ISSU状态的变化，通过该命令的显示信息可以帮助管理员确定下一步需执行的操作。

该命令不能显示**install**命令升级过程中设备所处的状态，因为**install**命令升级过程没有用到状态机。

【举例】

\# 当前设备没有ISSU升级，显示ISSU状态。（集中式设备）

\<Sysname\> display issu state

ISSU state: Init

Compatibility: Unknown

Work state: Normal

Current version list:

  boot: 7.1.041, Demo 2402

  system: 7.1.041, Demo 2402

  ssh: 7.1.041, Demo 2402

Current software images:

  flash:/boot.bin

  flash:/system.bin

  flash:/ssh.bin

\# 当前设备没有ISSU升级，显示ISSU状态。（集中式IRF设备/分布式设备－独立运行模式/分布式设备－IRF模式单成员设备）

\<Sysname\> display issu state

ISSU state: Init

Compatibility: Unknown

Work state: Normal

Upgrade method: Card by card

Upgraded slot: None

Current upgrading slot: None

Current version list:

  boot: 7.1.041, Demo 2402

  system: 7.1.041, Demo 2402

  ssh: 7.1.041, Demo 2402

Current software images:

  flash:/boot.bin

  flash:/system.bin

  flash:/ssh.bin

\# **issu load**命令执行过程中，显示ISSU状态。（集中式设备）

\<Sysname\> display issu state

ISSU state: Loading

Compatibility: Incompatible

Work state: Normal

Previous version list:

  boot: 7.1.041, Demo 2402

  system: 7.1.041, Demo 2402

  ssh: 7.1.041, Demo 2402

Previous software images:

  flash:/boot.bin

  flash:/system.bin

  flash:/ssh.bin

Upgrade version list:

  boot: 7.1.042, Demo 2403

  system: 7.1.042, Demo 2403

  ssh: 7.1.042, Demo 2403

Upgrade software images：

  flash:/boot02.bin

  flash:/system04.bin

  flash:/ssh04.bin

\# **issu load**命令执行过程中，显示ISSU状态。（集中式IRF设备/分布式设备－独立运行模式）

\<Sysname\> display issu state

ISSU state: Loading

Compatibility: Incompatible

Work state: Normal

Upgrade method: Card by card

Upgraded slot: None

Current upgrading slot:

  slot 1

Previous version list:

  boot: 7.1.041, Demo 2402

  system: 7.1.041, Demo 2402

  ssh: 7.1.041, Demo 2402

Previous software images:

  flash:/boot.bin

  flash:/system.bin

  flash:/ssh.bin

Upgrade version list:

  boot: 7.1.041, Demo 2403

  system: 7.1.041, Demo 2403

  ssh: 7.1.041, Demo 2403

Upgrade software images：

  flash:/boot02.bin

  flash:/system04.bin

  flash:/ssh04.bin

\# **issu load**命令执行过程中，显示ISSU状态。（分布式设备－IRF模式单成员设备）

\<Sysname\> display issu state

ISSU state: Loading

Compatibility: Incompatible

Work state: Normal

Upgrade method: Card by card

Upgraded slot: None

Current upgrading slot:

  chassis 1 slot 1

Previous version list:

  boot: 7.1.041, Demo 2402

  system: 7.1.041, Demo 2402

  ssh: 7.1.041, Demo 2402

Previous software images:

  flash:/boot.bin

  flash:/system.bin

  flash:/ssh.bin

Upgrade version list:

  boot: 7.1.041, Demo 2403

  system: 7.1.041, Demo 2403

  ssh: 7.1.041, Demo 2403

Upgrade software images：

  flash:/boot02.bin

  flash:/system04.bin

  flash:/ssh04.bin

\# 执行**issu load**命令后，在全局主用主控板上显示ISSU状态。（分布式设备－IRF模式单成员设备）

\<Sysname\> display issu state

ISSU state: Loaded

Compatibility: Compatible

Work state: Normal

Upgrade method: Card by card

Upgraded slot:

  chassis 1 slot 1

Current upgrading slot: None

Previous version list:

  boot: 7.1.041, Demo 2402

  system: 7.1.041, Demo 2402

  ssh: 7.1.041, Demo 2402

Previous software images:

  flash:/boot.bin

  flash:/system.bin

  flash:/ssh.bin

Upgrade version list:

  system: 7.1.041, Demo 2403

  ssh: 7.1.041, Demo 2403

Upgrade software images:

  flash:/system02.bin

  flash:/ssh02.bin

\# 执行**issu load**命令后，在原主设备上显示ISSU状态。（分布式设备－IRF模式多成员设备）

\<Sysname\> display issu state

ISSU state: Loaded

Compatibility: Incompatible

Work state: Independent active

Upgrade method: Chassis by chassis

Upgraded chassis:

  chassis 2

Current upgrading chassis: None

Previous version list:

  boot: 7.1.041, Demo 2402

  system: 7.1.041, Demo 2402

  ssh: 7.1.041, Demo 2402

Previous software images:

  flash:/boot.bin

  flash:/system.bin

  flash:/ssh.bin

Upgrade version list:

  system: 7.1.041, Demo 2403

  ssh: 7.1.041, Demo 2403

Upgrade software images:

  flash:/system04.bin

  flash:/ssh04.bin

表1-5 display issu state命令显示信息描述表

字段

描述

ISSU state

ISSU升级状态，取值可能为：

·Init：表示还没有开始ISSU升级或者ISSU升级已经完成

·Loading：表示正在执行**issu load**操作

·Loaded：表示**issu load**操作完成

·Switching：表示正在执行**issu run switchover**操作

·Switchover：表示**issu run switchove**r操作完成

·Accepted：表示**issu accept**操作完成

·Committing：表示正在执行**issu commit**操作

·Rollbacking：表示系统正在回滚中

·Unknown：在非原主用主控板上查看，表示设备正在升级过程中

Compatibility

版本兼容性检查结果，取值可能为：

·Compatible：表示兼容升级

·Incompatible：表示不兼容升级

·Unknown：没有升级

Work state

设备的工作模式，取值可能为：

·Normal：表示正常模式

·Independent active：表示独立主控模式。当升级到不兼容版本时，先升级的备用主控板就会进入独立主控模式。该模式使得同一设备上的不同主控板可以运行不同的软件版本

Upgrade method

升级方式，取值可能为：

·Card by card：表示以主控板为单位进行升级，升级完一块主控板再升级另一块主控板

·Chassis by chassis：在IRF中多成员设备运行的情况下，表示以成员设备为单位进行升级，先升级备设备，再升级原主设备（分布式设备－IRF模式）

Upgraded slot

完成升级的单板。取值为Unknown时，表示设备处于回滚过程中（分布式设备－独立运行模式）

Current upgrading slot

正在升级的单板。取值为Unknown时，表示设备处于回滚过程中（分布式设备－独立运行模式）

Upgraded chassis

完成升级的成员设备。取值为Unknown时，表示设备处于回滚过程中（分布式设备－IRF模式）

Current upgrading chassis

正在升级的成员设备。取值为Unknown时，表示设备处于回滚过程中（分布式设备－IRF模式单成员设备）

Current version list

设备没有升级，表示当前系统软件版本

Current software images

设备没有升级，表示当前运行软件包的名称

Previous version list

进行ISSU升级前的系统软件版本

Unknown：不兼容升级的时候，在非原主用主控板上查看，表示设备正在升级过程中

Previous software images

进行ISSU升级前版本文件

Unknown：不兼容升级的时候，在非原主用主控板上查看，表示设备正在升级过程中

Upgrade version list

正在ISSU升级的目标版本

Unknown：不兼容升级的时候，在非原主用主控板上查看，表示设备正在升级过程中

Upgrade software images

正在ISSU升级中用到的目标文件

Unknown：不兼容升级的时候，在非原主用主控板上查看，表示设备正在升级过程中

【相关命令】

·**issu accept**

·**issu commit**

·**issu load**

·**issu rollback**

·**issu run switchover**

**ISSU \-- ISSU配置命令 \-- display version comp-matrix**

------------------------------------------------------------------------

**[display version comp-matrix**]命令用来显示软件版本兼容信息。

【命令】

**[display version comp-matrix**]

**[display version comp-matrix file ***[filename*[\| **system** ]*filename*[\| **feature** ]*filename*&\<1-30\> } **\***]

**[display version comp-matrix file ipe ***ipe-filename*]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[boot**]：表示Boot包。

**[system**]：表示System包。

**[feature**]：表示Feature包。

*[filename*]：表示软件包的文件名，以.bin作为后缀名，为1～63个字符的字符串，不区分大小写。&\<1-30\>表示前面的参数最多可以输入30次。

**[ipe***ipe-filename*]：IPE文件名，以.ipe作为后缀名，为1～63个字符的字符串，不区分大小写。

【使用指导】

·当配置该命令时，命令中指定的软件包/IPE文件必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin（flash:/xx.ipe）。（集中式设备）

·当配置该命令时，命令中指定的软件包/IPE文件必须放在主用主控板存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含slot的信息，形如flash:/xx.bin（flash:/xx.ipe）。（分布式设备－独立运行模式）

·当配置该命令时，命令中指定的软件包/IPE文件必须放在主设备存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含slot的信息，形如flash:/xx.bin（flash:/xx.ipe）。（集中式IRF设备）

·当配置该命令时，命令中指定的软件包/IPE文件必须放在全局主用主控板存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含chassis和slot的信息，形如flash:/xx.bin（flash:/xx.ipe）。（分布式设备－IRF模式）

·如果指定文件名，则显示指定软件包的兼容性信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式；如果不指定文件名，则显示设备当前运行版本的兼容性信息。（不支持IRF3/安全引擎的设备）

·该命令只能显示父设备的软件包之间的兼容性，以及PEX设备的软件包之间的兼容性，不能判断父设备和PEX设备的软件包是否兼容。请通过软件版本说明书来判断父设备和PEX设备的软件包是否兼容。（支持IRF3的设备）

·该命令只能显示设备的软件包之间的兼容性，以及安全引擎的软件包之间的兼容性，不能判断设备和安全引擎的软件包是否兼容。请通过软件版本说明书来判断设备和安全引擎的软件包是否兼容。（支持安全引擎的设备）

·在IRF3组网环境，本设备下挂PEX设备的情况下，使用该命令，如果不指定文件名，则分别显示父设备以及PEX设备当前运行版本的兼容性信息。（支持IRF3的设备）

·当设备中安装了防火墙插卡，使用该命令，如果不指定文件名，则分别显示设备以及安全引擎当前运行版本的兼容性信息。（支持安全引擎的设备）

·在IRF3组网环境下，要显示PEX设备升级软件包的兼容信息时，请先使用**issu pex**命令指定PEX设备的升级软件包，再使用该命令，并且*filename*指定为父设备上的升级软件包。此时，会显示父设备上该软件包的兼容性信息，PEX设备上**issu pex**命令指定软件包的兼容性信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。只要父设备上有一个软件包不兼容，或者PEX设备上有一个软件包不兼容，均判定为不兼容升级方式，需要重启整个IRF3系统。（支持IRF3的设备）

·要显示安全引擎升级软件包的兼容信息时，请先使用**issu blade**命令指定安全引擎的升级软件包，再使用该命令，并且*filename*指定为设备上的升级软件包。此时，会显示设备上该软件包的兼容性信息，安全引擎上**issu blade**命令指定软件包的兼容性信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。只要设备上有一个软件包不兼容，或者安全引擎上有一个软件包不兼容，均判定为不兼容升级方式，需要重启整个系统。（支持安全引擎的设备）

【举例】

\# 显示设备当前正在使用的软件包的兼容信息。

\<Sysname\> display version comp-matrix

Boot image: flash:/cmw710-boot-a7122.bin

  Version:

  7.1.031

System image: flash:/cmw710-system-a7122.bin

  Version:

  V700R001B31D001

  Version compatibility list:

  V700R001B31D001

  Version dependency boot list:

  7.1.031

Feature image: flash:/cmw710-cfa-a7124.bin

  Version:

  V700R001B31D003

  Version compatibility list:

  V700R001B31D003

  Version dependency system list:

  V700R001B31D001

  V700R001B31D002

\# 显示文件flash:/boot-e2205.bin、flash:/system-e2205.bin、flash:/dhcp-e2205.re.bin和当前运行软件包的兼容信息。（不兼容版本显示信息举例）（集中式设备）

\<Sysname\> display version comp-matrix file boot flash:/boot-e2205.bin system flash:/system-e2205.bin feature flash:/dhcp-e2205.re.bin

Verifying the file flash:/dhcp-e2205.re.bin on the device\.....Done.

Verifying the file flash:/boot-e2205.bin on the device\.....Done.

Verifying the file flash:/system-e2205.bin on the device\.....Done.

Boot image: flash:/boot-e2205.bin

  Version:

  7.1.035

System image: flash:/system-e2205.bin

  Version:

  V200R001B02D012

  Version compatibility list:

  V200R001B02D012

  Version dependency boot list:

  7.1.035

Feature image: flash:/dhcp-e2205.re.bin

  Version:

  V200R001B02D012

  Version compatibility list:

  V200R001B02D012

  Version dependency system list:

  V200R001B02D012

  V200R001B02D014

Incompatible upgrade.

\# 显示文件flash:/boot-e2205.bin、flash:/system-e2205.bin、flash:/dhcp-e2205.incom.bin和当前运行软件包的兼容信息。（兼容版本显示信息举例）（集中式IRF设备）

\<Sysname\> display version comp-matrix file boot flash:/boot-e2205.bin system flash:/system-e2205.bin feature flash:/dhcp-e2205.incom.bin

Verifying the file flash:/dhcp-e2205.incom.bin on slot 2\.....Done.

Verifying the file flash:/boot-e2205.bin on slot 2\.....Done.

Verifying the file flash:/system-e2205.bin on slot 2\.....Done.

Boot image: flash:/boot-e2205.bin

  Version:

  7.1.035

System image: flash:/system-e2205.bin

  Version:

  V200R001B02D012

  Version compatibility list:

  V200R001B02D012

  Version dependency boot list:

  7.1.035

Feature image: flash:/dhcp-e2205.incom.bin

  Version:

  V200R001B02D014

  Version compatibility list:

  V200R001B02D014

  Version dependency system list:

  V200R001B02D012

  V200R001B02D014

  Slot     Upgrade Way

  2        File Upgrade

\# 查看当前软件版本和cmw710-cfa-a7125.bin软件版本的兼容性信息。（兼容版本显示信息举例）（分布式设备－独立运行模式）

\<Sysname\> display version comp-matrix file feature flash:/cmw710-cfa-a7125.bin

Verifying the file flash:/cmw710-cfa-a7125.bin on slot 0\.....Done.

Feature image: flash:/cmw710-cfa-a7125.bin

  Version:

  V700R001B31D002

  Version compatibility list:

  V700R001B31D001

  V700R001B31D002

  Version dependency system list:

  V700R001B31D001

  V700R001B31D002

  Slot                        Upgrade Way

  0                           Service Upgrade

  1                           Service Upgrade

  1.1                         Service Upgrade

  4                           Service Upgrade

Influenced service according to following table on slot 0:

flash:/cmw710-cfa-a7125.bin

    CFA

Influenced service according to following table on slot 4:

flash:/cmw710-cfa-a7125.bin

    CFA

Influenced service according to following table on slot 1:

flash:/cmw710-cfa-a7125.bin

    CFA

Influenced service according to following table on slot 1.1:

flash:/cmw710-cfa-a7125.bin

CFA

\# 查看当前软件版本和cmw710-cfa-a7122.bin软件版本的兼容性信息。（兼容版本显示信息举例）（分布式设备－IRF模式）

\<Sysname\> display version comp-matrix file feature flash:/cmw710-cfa-a7122.bin

Verifying the file flash:/cmw710-cfa-a7122.bin on chassis 1 slot 0\.....Done.

Feature image: flash:/cmw710-cfa-a7122.bin

  Version:

  V700R001B31D002

  Version compatibility list:

  V700R001B31D001

  V700R001B31D002

  Version dependency system list:

  V700R001B31D001

  V700R001B31D002

  Chassis   Slot              Upgrade Way

  1         0                 Service Upgrade

  1         0.1               Service Upgrade

  1         7                 Service Upgrade

  1         9                 Service Upgrade

  2         0                 Service Upgrade

  2         0.1               Service Upgrade

  2         1                 Service Upgrade

  2         6                 Service Upgrade

Influenced service according to following table on chassis 1 slot 0:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 1 slot 7:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 1 slot 9:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 1 slot 0.1:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 2 slot 0:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 2 slot 1:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 2 slot 6:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 2 slot 0.1:

flash:/cmw710-cfa-a7122.bin

    CFA

\# 显示父设备和PEX设备当前正在使用的软件包的兼容信息。

\<Sysname\> display version comp-matrix

Boot image: flash:/s5820v2_5830v2-cmw710-boot-d2404001.bin

  Version:

  7.1.046

System image: flash:/s5820v2_5830v2-cmw710-system-d2404001.bin

  Version:

  D2404001

  Version compatibility list:

  D2404001

  Version dependency boot list:

  7.1.046

Feature image: flash:/s5820v2_5830v2-cmw710-devkit-d2404001-b01-base.bin

  Version:

  D2404001

  Version compatibility list:

  D2402003

  D2404001

  Version dependency system list:

  D2404001

Compatible info of S5120HI:

Boot image: flash:/rpu-s5120hi-boot.bin

  Version:

  7.1.041

System image: flash:/rpu-s5120hi-system.bin

  Version:

  T2206

  Version compatibility list:

  T2206

  Version dependency boot list:

  7.1.041

Feature image: flash:/rpu-s5120hi-devkit-b46-b01-base.bin

  Version:

  T2206

  Version compatibility list:

  T2206

  Version dependency system list:

  T2206

\# 显示父设备文件flash:/boot-d2404.bin、flash:/system-d2404.bin、flash:/http-d2404.bin的兼容信息，PEX设备（设备型号S5120HI）文件flash:/s5120hi-boot-d2404.bin、flash:/s5120hi-system-d2404.bin、flash:/s5120hi-http-d2404.bin的兼容信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。（不兼容版本显示信息举例）（集中式IRF设备）（支持IRF3的设备）

\<Sysname\> issu pex PEX-S5120HI file boot flash:/s5120hi-boot-d2404.bin system flash:/s5120hi-system-d2404.bin feature flash:/s5120hi-http-d2404.bin

Verifying the file flash:/s5120hi-http-d2404.bin on slot 1\...Done.

Verifying the file flash:/s5120hi-boot-d2404.bin on slot 1\...Done.

Verifying the file flash:/s5120hi-system-d2404.bin on slot 1\...Done.

\<Sysname\> display version comp-matrix file boot flash:/boot-d2404.bin system flash:/system-d2404.bin feature flash:/http-d2404.bin

Verifying the file flash:/http-d2404.bin on slot 1\.....Done.

Verifying the file flash:/boot-d2404.bin on slot 1\.....Done.

Verifying the file flash:/system-d2404.bin on slot 1\.....Done.

Verifying the file flash:/s5120hi-boot-d2404.bin on slot 1\...Done.

Verifying the file flash:/s5120hi-system-d2404.bin on slot 1\...Done.

Verifying the file flash:/s5120hi-http-d2404.bin on slot 1\...Done.

Boot image: flash:/boot-d2404.bin

  Version:

  7.1.041

System image: flash:/system-d2404.bin

  Version:

  D2404

  Version compatibility list:

  D2404

  Version dependency boot list:

  7.1.041

Feature image: flash:/http-d2404.bin

  Version:

  D2404

  Version compatibility list:

  D2404

  Version dependency system list:

  D2402

  D2404

Compatible info of S5120HI:

Boot image: flash:/rpu-s5120hi-boot-d2404.bin

  Version:

  7.1.041

System image: flash:/rpu-s5120hi-system-d2404.bin

  Version:

  D2404

  Version compatibility list:

  D2404

  Version dependency boot list:

  7.1.041

Feature image: flash:/s5120hi-http-d2404.bin

  Version:

  D2404

  Version compatibility list:

  D2404

  Version dependency system list:

  D2402

  D2404

Incompatible upgrade.

\# 显示父设备文件flash:/boot-d2403.bin、flash:/system-d2403.bin、flash:/http-d2403.bin的兼容信息，PEX设备（设备型号S5120HI）文件flash:/s5120hi-http-d2403.bin的兼容信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。（兼容版本显示信息举例）（集中式IRF设备）（支持IRF3的设备）

\<Sysname\> issu pex PEX-S5120HI file feature flash:/s5120hi-http-d2403.bin

Verifying the file flash:/s5120hi-http-d2403.bin on slot 1\.....Done.

\<Sysname\> display version comp-matrix file boot flash:/boot-d2403.bin system flash:/system-d2403.bin feature flash:/http-d2403.bin

Verifying the file flash:/http-d2403.bin on slot 1\.....Done.

Verifying the file flash:/boot-d2403.bin on slot 1\.....Done.

Verifying the file flash:/system-d2403.bin on slot 1\.....Done.

Verifying the file flash:/s5120hi-http-d2403.bin on slot 1\.....Done.

Boot image: flash:/boot-d2403.bin

  Version:

  7.1.041

System image: flash:/system-d2403.bin

  Version:

  D2403

  Version compatibility list:

  D2402

  D2403

  Version dependency boot list:

  7.1.041

Feature image: flash:/http-d2403.bin

  Version:

  D2403

  Version compatibility list:

  D2402

  D2403

  Version dependency system list:

  D2402

  D2403

Compatible info of S5120HI:

Feature image: flash:/s5120hi-http-d2403.bin

  Version:

  D2403

  Version compatibility list:

  D2402

  D2403

  Version dependency system list:

  D2402

  D2403

  Slot     Upgrade Way

  1        File Upgrade

  102      File Upgrade

\# 查看父设备文件cmw710-cfa-a0042.bin的兼容信息，PEX设备（设备型号S5120HI）文件flash:/s5120hi-http-d2403.bin的兼容信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。（兼容版本显示信息举例）（分布式设备－独立运行模式）（支持IRF3的设备）

\<Sysname\> issu pex PEX-S5120HI file feature flash:/s5120hi-http-d2403.bin

Verifying the file flash:/s5120hi-http-d2403.bin on slot 0\.....Done.

\<Sysname\> display version comp-matrix file feature flash:/cmw710-cfa-a0042.bin

Verifying the file flash:/cmw710-cfa-a0042.bin on slot 0\.....Done.

Verifying the file flash:/s5120hi-http-d2403.bin on slot 0\.....Done.

Feature image: flash:/cmw710-cfa-a0042.bin

  Version:

  A0042

  Version compatibility list:

  A0041

  A0042

  Version dependency system list:

  A0041

Compatible info of S5120HI:

Feature image: flash:/s5120hi-http-d2403.bin

  Version:

  D2403

  Version compatibility list:

  D2402

  D2403

  Version dependency system list:

  D2402

  Slot                        Upgrade Way

  0                           Service Upgrade

  1                           Service Upgrade

  1.1                         Service Upgrade

  4                           Service Upgrade

  102                         Service Upgrade

Influenced service according to following table on slot 0:

flash:/cmw710-cfa-a0042.bin

    CFA

Influenced service according to following table on slot 4:

flash:/cmw710-cfa-a7125.bin

    CFA

Influenced service according to following table on slot 1:

flash:/cmw710-cfa-a0042.bin

    CFA

Influenced service according to following table on slot 1.1:

flash:/cmw710-cfa-a0042.bin

    CFA

Influenced service according to following table on slot 102:

flash:/cmw710-cfa-d2403.bin

    HTTP

\# 查看父设备文件cmw710-cfa-a0041.bin的兼容信息，PEX设备（设备型号S5120HI）文件flash:/s5120hi-http-d2403.bin的兼容信息，以及从当前运行版本升级到指定软件包版本需要采用的升级方式。（兼容版本显示信息举例）（分布式设备－IRF模式）（支持IRF3的设备）

\<Sysname\> issu pex PEX-S5120HI file feature flash:/s5120hi-http-d2403.bin

Verifying the file flash:/s5120hi-http-d2403.bin on chassis 1 slot 0\.....Done.

Copying file flash:/s5120hi-http-d2403.bin to chassis2#slot0#flash:/s5120hi-http-d2403.bin\...Done.

\<Sysname\> display version comp-matrix file feature flash:/cmw710-cfa-a0041.bin

Verifying the file flash:/cmw710-cfa-a0041.bin on chassis 1 slot 0\.....Done.

Verifying the file flash:/s5120hi-http-d2403.bin on chassis 1 slot 0\.....Done.

Feature image: flash:/cmw710-cfa-a0041.bin

  Version:

  A0042

  Version compatibility list:

  A0041

  A0042

  Version dependency system list:

  A0041

Compatible info of S5120HI:

Feature image: flash:/s5120hi-http-d2403.bin

  Version:

  D2403

  Version compatibility list:

  D2402

  D2403

  Version dependency system list:

  D2402

  Chassis   Slot              Upgrade Way

  1         0                 Service Upgrade

  1         0.1               Service Upgrade

  1         7                 Service Upgrade

  1         9                 Service Upgrade

  2         0                 Service Upgrade

  2         0.1               Service Upgrade

  2         1                 Service Upgrade

  2         6                 Service Upgrade

  101       0                 Service Upgrade

Influenced service according to following table on chassis 1 slot 0:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 1 slot 7:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 1 slot 9:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 1 slot 0.1:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 2 slot 0:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 2 slot 1:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 2 slot 6:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 2 slot 0.1:

flash:/cmw710-cfa-a7122.bin

    CFA

Influenced service according to following table on chassis 101 slot 0:

flash:/cmw710-cfa-a7122.bin

    HTTP

表1-6 display version comp-matrix命令显示信息描述表

字段

描述

Verifying the file flash:/xx.bin on chassis 1 slot 0\.....Done.

验证文件是否合法

Boot image: flash:/cmw710-boot-a7122.bin

  Version:

要显示的Boot包的相关信息，包括：

·Boot包的名称

·Version：Boot包的版本

System image: flash:/cmw710-system-a7122.bin

  Version:

  V700R001B31D001

  Version compatibility list:

  V700R001B31D001

  Version dependency boot list:

  7.1.031

要显示的System包的相关信息，包括：

·System包的名称

·Version：System包的版本

·Version compatibility list：和该System包兼容的System包版本列表

·Version dependency boot list：依赖的Boot包版本列表，即安装该System包前，必须先安装如下版本的Boot包中的任意一个

Feature image: flash:/cmw710-cfa-a7124.bin

  Version:

  V700R001B31D003

  Version compatibility list:

  V700R001B31D003

  Version dependency system list:

  V700R001B31D001

  V700R001B31D002

要显示的Feature包的相关信息，包括：

·Feature包的名称

·Version：Feature包的版本

·Version compatibility list：和该Feature包兼容的Feature包版本列表

·Version dependency system list：依赖的System包版本列表，即安装该Feature包前，必须先安装如下版本的System包中的任意一个

Compatible info of S5120HI:

Boot image: flash:/rpu-s5120hi-boot.bin

  Version:

  7.1.041

System image: flash:/rpu-s5120hi-system.bin

  Version:

  D2402

  Version compatibility list:

  D2402

  Version dependency boot list:

  7.1.041

Feature image: flash:/s5120hi-http-d2402.bin

  Version:

  D2404

  Version compatibility list:

  D2404

  Version dependency system list:

  D2402

要显示的PEX设备的相关信息，包括：

要显示的Boot包的相关信息：

·Boot包的名称

·Version：Boot包的版本

要显示的System包的相关信息：

·System包的名称

·Version：System包的版本

·Version compatibility list：和该System包兼容的System包版本列表

·Version dependency boot list：依赖的Boot包版本列表，即安装该System包前，必须先安装如下版本的Boot包中的任意一个

要显示的Feature包的相关信息：

·Feature包的名称

·Version：Feature包的版本

·Version compatibility list：和该Feature包兼容的Feature包版本列表

·Version dependency system list：依赖的System包版本列表，即安装该Feature包前，必须先安装如下版本的System包中的任意一个

Influenced service according to following table

如果升级，受影响的功能模块。只有版本兼容时，才会显示该信息

Incompatible upgrade

如果升级指定的软件包，则升级的方式为不兼容升级

Chassis

设备在IRF中的成员编号。只有版本兼容时，才会显示该信息（分布式设备－IRF模式）

Slot

单板所在的槽位号。只有版本兼容时，才会显示该信息（分布式设备－独立运行模式/分布式设备－IRF模式）

设备在IRF中的成员编号。只有版本兼容时，才会显示该信息（集中式IRF设备）

Upgrade Way

兼容升级策略。只有版本兼容时，才会显示该信息。取值可能为：

·Service Upgrade：表示服务级增量升级，该方式下，仅对本业务模块有影响，对系统以及其他业务模块没有影响

·File Upgrade：表示文件级增量升级。该方式下，仅对系统内的、用户不可见的程序文件进行升级，对系统以及业务模块没有影响

·ISSU Reboot：表示通过软重启方式升级

·Reboot：表示通过重启方式升级

·Sequence Reboot：表示逐次重启方式。只有网板支持该升级方式，当网板需要重启升级时，为了避免重启升级过程中流量中断，系统会自动升级完毕一块网板后，再自动升级下一块网板，直到所有网板升级完毕后，再自动升级主控板。该字段的支持情况与网板的型号有关，请以设备的实际情况为准

【相关命令】

·**issu load**

**ISSU \-- ISSU配置命令 \-- install abort**

------------------------------------------------------------------------

**[install abort**]命令用来取消正在执行中的ISSU操作。

【命令】

**[install** **abort** [ *job-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[job-id*]：任务ID。不指定该参数时，则取消正在执行中的操作。

【使用指导】

当用户执行**install activate**、**install add**、**install commit**、**install deactivate**、**install remove**或**install rollback to**命令时，系统会创建相应的任务。为了管理和监控这些任务，系统会给每个任务分配一个任务ID。一个任务ID代表一条命令。其中，只有正在进行的激活或卸载操作可以使用**install abort**命令进行取消操作，取消后回退到操作前状态。

【举例】

\# 取消正在执行中的操作。

\<Sysname\> install abort

【相关命令】

·**display install job**

**ISSU \-- ISSU配置命令 \-- install activate**

------------------------------------------------------------------------

**[install activate**]命令用来激活软件包。

【命令】

集中式设备：

**[install activate**[ { **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \* [ **test** ]]]

**[install activate patch ***filename*]

分布式设备－独立运行模式/集中式IRF设备：

**[install activate**[ { **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \* **slot** *slot-number* ]**cpu***cpu-number*   **test** ]

**[install activate patch ***filename ***cpu***cpu-number*  }]

分布式设备－IRF模式：

**[install activate**[ { **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \* **chassis** *chassis-number* **slot** *slot-number* ]**cpu***cpu-number*   **test** ]

**[install** **activate patch** *filename* **cpu***cpu-number*  }]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[boot**]：表示Boot包。

**[system**]：表示System包。

**[feature**]：表示Feature包。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[patch**]：表示补丁包。用于快速修复系统Bug。

*[filename*]：表示软件包的文件名，以.bin作为后缀名，从存储介质名开始为1～63个字符的字符串（包括存储介质名在内），不区分大小写。&\<1-30\>表示前面的参数最多可以输入30次。

**[slot ***slot-number*]：*slot-number*取值为0，无特殊意义。（集中式设备）

**[all**]：升级补丁包对应的所有单板。（分布式设备－独立运行模式）

**[all**]：升级补丁包对应的所有成员设备。（集中式IRF设备）

**[all**]：升级补丁包对应的所有成员设备或者PEX。（集中式IRF设备）（支持IRF3的设备）

**[all**]：升级补丁包对应的所有单板。（分布式设备－独立运行模式）（不支持IRF3的设备）

**[all**]：升级补丁包对应的所有单板或者PEX。（分布式设备－独立运行模式）（支持IRF3的设备）

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示待升级的安全引擎的CPU编号。本参数专用于升级防火墙插卡上的安全引擎，其它单板以及防火墙插卡上其它CPU升级时，不需要指定该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[test**]：查看指定软件包的升级策略。不带该参数时，表示直接执行升级操作。

【使用指导】

·只有进行激活处理后，软件包才能生效。

·被激活的软件包只在本次运行的系统中生效。要使被激活的软件包在设备重启后继续生效，还需要执行**install commit**命令。

·请先查看软件包版本发布说明书，如果某软件包需要License才能运行，且设备当前没有对应的有效的License时，需安装对应的License，再执行该命令。否则，会导致命令执行失败。

(1)集中式设备

·当配置该命令时，命令中指定的软件包必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin。

(2)分布式设备－独立运行模式

当配置该命令时：

·命令中指定的软件包必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin或slot1#flash:/xx.bin。

·执行命令行时，如果*filename*不是存放在待升级主控板上的文件，则系统会先将该文件拷贝到待升级主控板上，再执行升级动作。

·对于安全引擎，执行命令行时，如果*filename*不是存放在待升级安全引擎上的文件，则系统会先将该文件拷贝到待升级安全引擎上，再执行升级动作。

·如果指定的**slot**参数为主用主控板所在的槽位号，则执行该命令，会同时升级主用主控板和业务板。

·如果指定的**slot**参数为备用主控板所在的槽位号，则执行该命令，只会升级备用主控板。

(3)集中式IRF设备

当配置该命令时：

·命令中指定的软件包必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin或slot2#flash:/xx.bin。

·如果指定的**slot**参数为成员设备的成员编号，则执行该命令，如果指定的不是该成员设备上的软件包，会先将软件包拷贝到该成员设备上，再升级该成员设备。

·从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过**display device**、**display mdc**和**display system internal ha service-group**命令查看到所有单板处于normal状态、所有MDC处于active状态和所有服务的action显示为0后，再执行**install activate**命令，否则，命令会执行失败。

(4)分布式设备－IRF模式

当配置该命令时：

·命令中指定的软件包必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin或chassis1#slot1#flash:/xx.bin。

·执行命令行时，如果*filename*不是存放在待升级主控板上的文件，则系统会先将该文件拷贝到待升级主控板上，再执行升级动作。

·对于安全引擎，执行命令行时，如果*filename*不是存放在待升级安全引擎上的文件，则系统会先将该文件拷贝到待升级安全引擎上，再执行升级动作。

·如果指定的**chassis** *chassis-number* **slot** *slot-number*参数为全局主用主控板所在的槽位号，则执行该命令，会同时升级该主控板和所有业务板。

·如果指定的**chassis** *chassis-number* **slot** *slot-number*参数为全局备用主控板所在的槽位号，则执行该命令，只会升级该主控板。

·从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过**display device**、**display mdc**和**display system internal ha service-group**命令查看到所有单板处于normal状态、所有MDC处于active状态和所有服务的action显示为0后，再执行**install activate**命令，否则，命令会执行失败。

【举例】

\# 显示Feature包ssh2.bin的升级策略。（集中式设备）

\<Sysname\> install activate feature flash:/ssh2.bin test

Verifying the file flash:/ssh2.bin on the device\.....Done.

Upgrade summary according to following table:

flash:/ssh2.bin

  Running Version             New Version

  Beta 1330                   Beta 1331

Upgrade Way: Service Upgrade

Influenced service according to following table:

flash:/ssh2.bin

     SSH       IFMGR     CFA       LAGG

以上显示信息表明，该软件将采用增量方式升级。并且升级过程中会重启功能模块SSH、IFMGR、CFA和LAGG。

\# 显示备用主控板1上的Feature包ssh2.bin的升级策略。（分布式设备－独立运行模式）

\<Sysname\> install activate feature flash:/ssh2.bin slot 1 test

Copying file flash:/ssh2.bin to slot1#flash:/ssh2.bin\...\...Done.

Verifying the file flash:/ssh2.bin on slot 1\.....Done.

Upgrade summary according to following table:

flash:/ssh2.bin

  Running Version             New Version

  Beta 1330                   Beta 1331

  Slot                        Upgrade Way

  1                           Service Upgrade

Influenced service according to following table:

flash:/ssh2.bin

     SSH       IFMGR     CFA       LAGG

以上显示信息表明，该软件将采用增量方式升级。并且升级过程中会重启功能模块SSH、IFMGR、CFA和LAGG。

\# 显示从设备2上的Feature包ssh2.bin。的升级策略（集中式IRF设备）

\<Sysname\> install activate feature flash:/ssh2.bin slot 2 test

Copying file flash:/ssh2.bin to slot2#flash:/ssh2.bin\...\...Done.

Verifying the file flash:/ssh2.bin on slot 2\.....Done.

Upgrade summary according to following table:

flash:/ssh2.bin

  Running Version             New Version

  Beta 1330                   Beta 1331

  Slot                        Upgrade Way

  2                           Service Upgrade

Influenced service according to following table:

flash:/ssh2.bin

     SSH       IFMGR     CFA       LAGG

以上显示信息表明，该软件将采用增量方式升级。并且升级过程中会重启功能模块SSH、IFMGR、CFA和LAGG。

\# 显示成员设备1的1号单板（全局备用主控板）上的feature包ssh2.bin的升级策略。（分布式设备－IRF模式）

\<Sysname\> install activate feature flash:/ssh2.bin chassis 1 slot 1 test

Copying file flash:/ssh2.bin to chassis1#slot1#flash:/ssh2.bin\...\...Done.

Verifying the file flash:/ssh2.bin on chassis 1 slot 1\.....Done.

Upgrade summary according to following table:

flash:/ssh2.bin

  Running Version             New Version

  Beta 1330                   Beta 1331

  Chassis   Slot              Upgrade Way

  1         1                 Service Upgrade

Influenced service according to following table:

flash:/ssh2.bin

     SSH       IFMGR     CFA       LAGG

以上显示信息表明，该软件将采用增量方式升级。并且升级过程中会重启功能模块SSH、IFMGR、CFA和LAGG。

\# 激活System包system.bin和Feature包feature.bin。（集中式设备）

\<Sysname\> install activate system flash:/system.bin feature flash:/feature.bin

Verifying the file flash:/feature.bin on the device\.....Done.

Verifying the file flash:/system.bin on the device\.....Done.

Upgrade summary according to following table:

flash:/system.bin

  Running Version             New Version

  Beta 1330                   Beta 1331

flash:/feature.bin

  Running Version             New Version

  NONE                        Beta 1330

Upgrade Way: Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

This operation maybe take several minutes, please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.

\# 激活备用主控板1上的System包system.bin和Feature包feature.bin。（分布式设备－独立运行模式）

\<Sysname\> install activate system flash:/system.bin feature flash:/feature.bin slot 1

Copying file flash:/system.bin to slot1#flash:/system.bin\...\...Done.

Verifying the file flash:/system.bin on slot 1\.....Done.

Copying file flash:/feature.bin to slot1#flash:/feature.bin\...\...Done.

Verifying the file flash:/feature.bin on slot 1\.....Done.

Verifying the file flash:/feature.bin on slot 0\.....Done.

Verifying the file flash:/system.bin on slot 0\.....Done.

Upgrade summary according to following table:

flash:/system.bin

  Running Version             New Version

  Beta 1330                   Beta 1331

flash:/feature.bin

  Running Version             New Version

  None                        Beta 1330

  Slot                        Upgrade Way

  1                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

This operation maybe take several minutes, please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.

\# 激活从设备2上的System包system.bin和Feature包feature.bin。（集中式IRF设备）

\<Sysname\> install activate system flash:/system.bin feature flash:/feature.bin slot 2

Copying file flash:/system.bin to slot2#flash:/system.bin\...\...Done.

Verifying the file flash:/system.bin on slot 2\.....Done.

Copying file flash:/feature.bin to slot2#flash:/feature.bin\...\...Done.

Verifying the file flash:/feature.bin on slot 2\.....Done.

Upgrade summary according to following table:

flash:/system.bin

  Running Version             New Version

  Beta 1330                   Beta 1331

flash:/feature.bin

  Running Version             New Version

  None                        Beta 1330

  Slot                        Upgrade Way

  2                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

This operation maybe take several minutes, please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.

\# 激活成员设备1的1号单板（全局备用主控板）上的Feature包feature.bin。（分布式设备－IRF模式）

\<Sysname\> install activate feature flash:/feature.bin chassis 1 slot 1

Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...\...Done.

Verifying the file flash:/feature.bin on chassis 1 slot 1\.....Done.

Upgrade summary according to following table:

flash:/route-feature.bin

  Running Version             New Version

  None                        Beta 1330

  Chassis   Slot              Upgrade Way

  1         1                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

This operation maybe take several minutes, please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....Done.

表1-7 install activate命令显示信息描述表

字段

描述

Copying file *A* to *B*\...\...Done.

将文件从位置*A*拷贝到位置*B*。当配置备用主控板时才有该提示信息（分布式设备－独立运行模式）

将文件从位置*A*拷贝到位置*B*。当配置从设备时才有该提示信息（集中式IRF设备）

将文件从位置*A*拷贝到位置*B*。当配置全局备用主控板时才有该提示信息（分布式设备－IRF模式）

Verifying the file flash:/xx.bin on chassis 1 slot 0\.....Done.

验证文件是否合法

Upgrade summary according to following table

升级摘要信息

Running Version

设备当前运行的相同类型软件包的产品版本号

New Version

目标软件包的产品版本号

Chassis

设备在IRF中的成员编号（分布式设备－IRF模式）

Slot

单板所在的槽位号（分布式设备－独立运行模式/分布式设备－IRF模式）

设备在IRF中的成员编号（集中式IRF设备）

Upgrade Way

兼容升级策略，取值可能为：

·Service Upgrade：表示服务级增量升级，该方式下，仅对本业务模块有影响，对系统以及其他业务模块没有影响

·File Upgrade：表示文件级增量升级。该方式下，仅对系统内的、用户不可见的程序文件进行升级，对系统以及业务模块没有影响

·ISSU Reboot：表示通过软重启方式升级

·Reboot：表示通过重启方式升级

·Sequence Reboot：表示逐次重启方式。只有网板支持该升级方式，当网板需要重启升级时，为了避免重启升级过程中流量中断，系统会自动升级完毕一块网板后，再自动升级下一块网板，直到所有网板升级完毕后，再自动升级主控板。该字段的支持情况与网板的型号有关，请以设备的实际情况为准

Influenced service according to following table

将受影响的功能模块

Upgrading software images to compatible versions. Continue? Y/N

询问用户是否执行兼容升级操作

This operation maybe take several minutes, please wait

升级操作需要花费一定时间，请等待

Done.

表示激活成功

Operation failed.

表示激活失败

Install command does not support incompatible upgrade.

不能使用**install**命令来升级不兼容版本

【相关命令】

·**display install active**

·**install commit**

·**install deactivate**

**ISSU \-- ISSU配置命令 \-- install add**

------------------------------------------------------------------------

**[install** **add**]命令用来解压缩IPE文件。

【命令】

**[install** **add** *ipe-filename* *medium-name*:]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[ipe-filename*]：IPE文件名，以.ipe作为后缀名，从存储介质名开始为1～63个字符的字符串（包括存储介质名在内），不区分大小写。

*[medium-name*]：存储介质的名称，形如flash。（集中式设备）

*[medium-name*]：存储介质的名称。如果是解压缩到主用主控板上，则为flash；如果是解压缩到备用主控板上，则为slot*n*#flash，*n*为备用主控板所在的槽位号；如果是解压缩到本地有存储介质的PEX设备上，则为slot*n*#flash，*n*为PEX设备的虚拟槽位号；如果是解压缩到安全引擎上，则为slot*n*.*x*#flash，*n*为防火墙插卡所在的槽位号，*x*为安全引擎的CPU编号。（分布式设备－独立运行模式）

*[medium-name*]：存储介质的名称。如果是解压缩到主设备上，则为flash；如果是解压缩到从设备上，则为slot*n*#flash，*n*为从设备的成员编号。（集中式IRF设备）

*[medium-name*]：存储介质的名称。如果是解压缩到全局主用主控板上，则为flash；如果是解压缩到全局备用主控板上，则为chassis*m*#slot*n*#flash，*m*为设备的成员编号，*n*为成员设备上主控板所在的槽位号；如果是解压缩到本地有存储介质的PEX设备上，则为chassis*m*#slot*n*#flash，*m*为设备的成员编号，*n*为PEX设备的虚拟槽位号；如果是解压缩到安全引擎上，则为chassis*m*#slot*n.x*#flash，*m*为防火墙插卡所在设备的成员编号，*n*为防火墙插卡所在的槽位号，*x*为安全引擎的CPU编号。（分布式设备－IRF模式）

【使用指导】

IPE文件是多个软件包的集合。将多个软件包整合成一个IPE文件对外发布，以便减少BIN包之间的版本管理问题。

用户获取IPE文件后，可以使用**display install ipe-info**命令查看该IPE文件中包含了哪些软件包，可以通过**install add**命令将IPE文件解压生成软件包，再利用生成的软件包更新设备软件。

当配置该命令时，命令中指定的IPE文件必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.ipe。（集中式设备）

当配置该命令时，命令中指定的IPE文件必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.ipe或slot1#flash:/xx.ipe。（分布式设备－独立运行模式/集中式IRF设备）

当配置该命令时，命令中指定的IPE文件必须放在存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.ipe或chassis1#slot1#flash:/xx.ipe。（分布式设备－IRF模式）

【举例】

\# 解压缩all.ipe文件到存储介质flash上。

\<Sysname\> install add flash:/all.ipe flash:

Verifying the file flash:/all.ipe on the device\...Done.

Decompressing file boot.bin to flash:/boot.bin\...\...\...\...\...\...\.....Done.

Decompressing file system.bin to flash:/system.bin\...\...\...\...\...\...\...\...\...\...\...Done.

**ISSU \-- ISSU配置命令 \-- install commit**

------------------------------------------------------------------------

**[install commit**]命令用来确认软件包更改。

【命令】

**[install commit**]

【视图】

用户视图

【缺省用户角色】

network-admin

【使用指导】

执行**install activate**、**install deactivate**、**install rollback**命令会修改设备当前运行的软件包列表，使得只有符合用户需求的软件运行，不符合要求的不运行。

·当执行**install activate**命令，且为增量升级方式时，这些修改只在设备的本次运行过程有效，要使这个修改结果在设备下次重启后继续生效，需要再执行**install commit**命令进行确认，确认后的软件包会列入设备主用下次启动软件包列表。

·当执行**install activate**命令，且为软重启或重启升级方式时，因为用户在执行**install activate**命令时，系统已经修改了下次启动软件列表，所以，即便不再执行**install** **commit**命令，升级软件包也会在系统重启后继续生效。

·当执行**install deactivate**或**install rollback**命令，这些修改只在设备的本次运行过程有效，要使这个修改结果在设备下次重启后继续生效，需要再执行**install commit**命令进行确认。

**[boot-loader file**]命令和**install commit**命令都可以变更主用下次启动软件包列表，最新的配置生效。两条命令的不同之处在于，**install commit**命令自动使用当前激活的软件包列表作为主用下次启动软件包列表。而**boot-loader file**命令还可以指定其它当前未激活的软件包，可以配置为主用或者备用下次启动软件包列表。

请先查看软件包版本发布说明书，如果某软件包需要License才能运行，且设备当前没有对应的有效的License时，需安装对应的License，再执行该命令。否则，会导致命令执行失败。

【举例】

\# 确认软件包更改。

\<Sysname\> install commit

This operation will take several minutes, please wait\...\...\...\...\...\...\...\...\...Done.

【相关命令】

·**install activate**

·**install deactivate**

·**install rollback**

**ISSU \-- ISSU配置命令 \-- install deactivate**

------------------------------------------------------------------------

**[install deactivate**]命令用来卸载Feature包或补丁包。

【命令】

集中式设备：

**[install deactivate** **feature** *filename*&\<1-30\>]

**[install deactivate patch ***filename*]

分布式设备－独立运行模式/集中式IRF设备：

**[install deactivate** **feature** *filename*&\<1-30\> **slot** *slot-number* **cpu***cpu-number* ]

**[install deactivate patch ***filename*******cpu***cpu-number*  }]

分布式设备－IRF模式：

**[install deactivate** **feature** *filename*&\<1-30\> **chassis** *chassis-number* **slot** *slot-number* **cpu***cpu-number* ]

**[install** **deactivate patch** *filename* **cpu***cpu-number*  }]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[filename*]：表示需要卸载Feature包或补丁包的文件名，以.bin作为后缀名，为1～63个字符的字符串，不区分大小写。&\<1-30\>表示前面的参数最多可以输入30次。

**[all**]：表示安装了该补丁包的所有单板。（分布式设备－独立运行模式）

**[all**]：表示安装了该补丁包的所有成员设备。（集中式IRF设备）

**[all**]：表示安装了该补丁包的所有成员设备或者PEX。（集中式IRF设备）（支持IRF3的设备）

**[all**]：表示安装了该补丁包的所有单板。（分布式设备－独立运行模式）（不支持IRF3的设备）

**[all**]：表示安装了该补丁包的所有单板或者PEX。（分布式设备－独立运行模式）（支持IRF3的设备）

**[slot ***slot-number*]：*slot-number*取值为0，无特殊意义。（集中式设备）

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示安全引擎的CPU编号。本参数专用于卸载防火墙插卡上安全引擎的Feature包或补丁包，卸载其它单板以及防火墙插卡上其它CPU的Feature包或补丁包时，不需要指定该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

【使用指导】

该命令只能对已经激活的软件包进行卸载操作。卸载的软件包的特性功能在本次系统运行中失效。如果要使卸载的软件包在设备重启后继续失效，请执行**install commit**命令对卸载操作进行确认。

当配置该命令时，文件名中必须包含存储介质的名称，形如flash:/xx.bin。（集中式设备）

当配置该命令时，文件名中必须且只能包含存储介质的名称，不能包含slot的信息，形如flash:/xx.bin。（分布式设备－独立运行模式）

当配置该命令时，文件名中必须且只能包含存储介质的名称，不能包含slot的信息，形如flash:/xx.bin。（集中式IRF设备）

当配置该命令时，文件名中必须且只能包含存储介质的名称，不能包含chassis和slot的信息，形如flash:/xx.bin。（分布式设备－IRF模式）

从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过**display device**、{.ItemListCharChar}**display mdc**和**display system internal ha service-group**命令{.ItemListCharChar}查看到所有单板处于normal状态、所有MDC处于active状态和所有服务的action显示为0后，再执行**install deactivate**命令，否则，命令会执行失败。（集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 卸载设备上的patch包route-patch.bin。（集中式设备）

\<Sysname\> install deactivate patch flash:/route-patch.bin

\# 卸载0号单板上的patch包route-patch.bin。（分布式设备－独立运行模式）

\<Sysname\> install deactivate patch flash:/route-patch.bin slot 0

\# 卸载成员设备1上的patch包route-patch.bin。（集中式IRF设备）

\<Sysname\> install deactivate patch flash:/route-patch.bin slot 1

\# 卸载成员设备1的0号槽位的单板上的feature包route-feature.bin。（分布式设备－IRF模式）

\<Sysname\> install deactivate feature flash:/route-feature.bin chassis 1 slot 0

\# 卸载安全引擎上的feature包flash:/issu.bin，安全引擎所在槽位号为7，CPU编号为1。（分布式设备－独立运行模式）

\<Sysname\> install deactivate feature flash:/issu.bin slot 7 cpu 1

\# 卸载安全引擎上的feature包flash:/issu.bin，安全引擎所在设备的成员编号为1，槽位号为7，CPU编号为1。（分布式设备－IRF模式）

\<Sysname\> install deactivate feature flash:/issu.bin chassis 1 slot 7 cpu 1

【相关命令】

·**display install active**

·**display install inactive**

**ISSU \-- ISSU配置命令 \-- install remove**

------------------------------------------------------------------------

**[install remove**]命令用来删除指定的软件包。

【命令】

集中式设备：

**[install remove**[ { *filename \|* **inactive** }]]

分布式设备－独立运行模式*/*集中式IRF设备：

**[install remove ** **slot** *slot-number* ]**cpu***cpu-number*   { *filename \|* **inactive** }

分布式设备－IRF模式：

**[install remove ** **chassis** *chassis-number* **slot** *slot-number* ]**cpu***cpu-number*   { *filename \|* **inactive** }

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。不指定该参数时，表示设备上的所有单板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示IRF中的所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者本地有存储介质的PEX的虚拟槽位号。不指定该参数时，表示IRF中的所有成员设备和本地有存储介质的PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者本地有存储介质的PEX对应的虚拟框号，*slot-number*表示单板/本地有存储介质的PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板和本地有存储介质的PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：表示安全引擎的CPU编号。本参数专用于删除安全引擎上的指定软件包，操作其它单板以及防火墙插卡上其它CPU时，不需要指定该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/分布式设备－IRF模式）

*[filename*]：表示软件包的文件名，以.bin作为后缀名，为1～63个字符的字符串，不区分大小写。

**[inactive**]：表示将删除指定存储介质根目录下、没有被激活的所有软件包。

【使用指导】

·该命令只能删除存储介质根目录下、没有被激活的软件包。

·当配置该命令时，命令中指定的软件包必须放在存储介质的根目录下，文件名中必须且只能包含存储介质的名称，不能包含chassis和slot的信息，形如flash:/xx.bin。（分布式设备－IRF模式）

·执行该命令后，指定的软件包将从设备上被彻底删除，用户将不能使用该软件包进行回滚或回退操作。

【举例】

\# 删除软件包flash:/ssh-feature.bin。

\<Sysname\> install remove flash:/ssh-feature.bin

**ISSU \-- ISSU配置命令 \-- install rollback to**

------------------------------------------------------------------------

**[install rollback to**]命令用来回滚到指定的回滚点，即按回滚点上记录的信息，进行回滚操作。

【命令】

**[install rollback to**[ { *point-id* \| **original** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[point-id*]：回滚点的编号，当系统中至少存在两个回滚点的时候，才能输入该参数。可以用**display install rollback**命令查看系统中存在的回滚点。

**[original**]：回滚到ISSU升级初始状态。

【使用指导】

每次激活或者卸载软件包之后，系统中将运行着不同的软件包，系统将这些变化记录为回滚点。通过回滚功能，可将系统回滚到某个历史状态，或者恢复到ISSU升级初始状态。

当升级方式为增量升级时，软件包回滚只在设备本次运行过程中生效，用户只有通过**install commit**命令确认软件包的更改后，才能使此次的回滚操作在系统重启后生效。系统最多支持50个回滚点，当回滚点超过最大值时，旧的回滚点会被删除，新的回滚点会被保存。

当升级方式为软重启或重启升级时，系统不会保留任何回滚点，只支持回滚到系统升级初始状态。

补丁包不支持回滚操作。

【举例】

\# 回滚到回滚点1。

\<Sysname\> install rollback to 1

\# 回滚到original回滚点。可通过观察active列表和回滚点的变化看出执行的结果。

\<Sysname\> display install active

Active packages on slot 1:

  flash:/boot-a0201.bin

  flash:/system-a0201.bin

  flash:/ssh-feature-a0201.bin

\<Sysname\> display install rollback

Install rollback information 1 on slot 1:

  Updating from no package

         to flash:/ssh-feature-a0201.bin.

以上显示信息表明，当前激活的包有三个，但是确认的只有两个，回滚点1是激活了flash:/ssh-feature-a0201.bin。

\<Sysname\> install rollback to original

\<Sysname\> display install active

Active packages on slot 1:

  flash:/boot-a0201.bin

  flash:/system-a0201.bin

\<Sysname\> display install committed

Committed packages on slot 1:

  flash:/boot-a0201.bin

  flash:/system-a0201.bin

执行**install rollback to original**命令后，设备运行的软件集恢复到ISSU升级初始状态，flash:/ssh-feature-a0201.bin被卸载。

【相关命令】

·**display install rollback**

**ISSU \-- ISSU配置命令 \-- install verify**

------------------------------------------------------------------------

**[install verify**]命令用来执行软件包检验。

【命令】

**[install verify**]

【视图】

用户视图

【缺省用户角色】

network-admin

【使用指导】

正常情况下，设备上运行的软件必须完整并且处于激活状态的软件包应该和已确认的软件包一致，否则，会导致设备重启前后运行的软件版本不一致，甚至不能正常启动。（集中式设备）

正常情况下，设备上各主控板运行的软件必须完整并且版本应该一致，各主控板上处于激活状态的软件包应该和已确认的软件包一致，否则，会影响设备的主备倒换，以及导致主控板重启前后运行的软件版本不一致甚至不能正常启动。（分布式设备－独立运行模式）

正常情况下，IRF中上各成员设备运行的软件必须完整并且版本应该一致，各成员设备上处于激活状态的软件包应该和已确认的软件包一致，否则，会影响主设备和从设备的倒换，以及导致成员设备重启前后运行的软件版本不一致甚至不能正常启动。（集中式IRF设备）

正常情况下，IRF中各主控板运行的软件必须完整并且版本应该一致，各主控板上处于激活状态的软件包应该和已确认的软件包一致，否则，会影响主控板的主备倒换，以及导致主控板重启前后运行的软件版本不一致甚至不能正常启动。（分布式设备－IRF模式）

使用该命令，能帮助用户进行软件包检查，

·当系统提示软件包不完整时，请重新下载并安装软件包。

·当系统提示软件包不一致时，请使用**install activate**、**install deactivate**以及**install commit**命令来确保它们的一致。

【举例】

\# 检验软件包信息。（集中式设备）

\<Sysname\> install verify

Active packages on the device are the reference packages.

Packages will be compared with the reference packages.

This operation will take several minutes, please wait\...

  Verifying packages on the device:

  Start to check active package completeness.

Verifying the file flash:/boot-a0101.bin on the device\...\...\.....Done.

   flash:/boot-a0101.bin verification successful.

Verifying the file flash:/system-a0101.bin on the device\...\...\...\...Done.

   flash:/system-a0101.bin verification successful.

  Start to check active package consistency.

    Active packages are consistent with committed packages on their own board.

    Active packages are consistent with the reference packages.

Verification is done.

\# 检验设备各个单板上的软件包信息。（分布式设备－独立运行模式）

\<Sysname\> install verify

Active packages on slot 1 are the reference packages.

Packages will be compared with the reference packages.

This operation will take several minutes, please wait\...

  Verifying packages on slot 0:

  Start to check active package completeness.

Verifying the file flash:/boot-a0101.bin on slot 0\...\...\...\...\...\...\...Done.

    flash:/boot-a0101.bin verification successful.

Verifying the file flash:/system-a0101.bin on slot 0\...\...\...\...\...\...\...Done.

    flash:/system-a0101.bin verification successful.

  Start to check active package consistency.

    Active packages are consistent with committed packages on their own board.

    Active packages are consistent with the reference packages.

  Verifying packages on slot 1:

  Start to check active package completeness.

Verifying the file flash:/boot-a0101.bin on slot 1\...\...\...\...\...\...\...Done.

    flash:/boot-a0101.bin verification successful.

Verifying the file flash:/system-a0101.bin on slot 1\...\...\...\...\...\...\...Done.

    flash:/system-a0101.bin verification successful.

  Start to check active package consistency.

    Active packages are consistent with committed packages on their own board.

    Active packages are consistent with the reference packages.

Verification is done.

\# 检验设备各个单板上的软件包信息。（集中式IRF设备）

\<Sysname\> install verify

Active packages on slot 1 are the reference packages.

Packages will be compared with the reference packages.

This operation will take several minutes, please wait\...

  Verifying packages on slot 1:

  Start to check active package completeness.

Verifying the file flash:/boot-a0101.bin on slot 1\...\...\...\...\...\...\...Done.

    flash:/boot-a0101.bin verification successful.

Verifying the file flash:/system-a0101.bin on slot 1\...\...\...\...\...\...\...Done.

    flash:/system-a0101.bin verification successful.

  Start to check active package consistency.

    Active packages are consistent with committed packages on their own board.

    Active packages are consistent with the reference packages.

  Verifying packages on slot 2:

  Start to check active package completeness.

Verifying the file flash:/boot-a0101.bin on slot 2\...\...\...\...\...\...\...Done.

    flash:/boot-a0101.bin verification successful.

Verifying the file flash:/system-a0101.bin on slot 2\...\...\...\...\...\...\...Done.

    flash:/system-a0101.bin verification successful.

  Start to check active package consistency.

    Active packages are consistent with committed packages on their own board.

    Active packages are consistent with the reference packages.

Verification is done.

\# 检验设备各个单板上的软件包信息。（分布式设备－IRF模式）

\<Sysname\> install verify

Active packages on slot 1 are the reference packages.

Packages will be compared with the reference packages.

This operation will take several minutes, please wait\...

  Verifying packages on chassis 1 slot 0:

  Start to check active package completeness.

Verifying the file flash:/boot-a0101.bin on chassis 1 slot 0\...\...\...\...\...\...\...Done.

    flash:/boot-a0101.bin verification successful.

Verifying the file flash:/system-a0101.bin on chassis 1 slot 0\...\...\...\...\...\...\...Done.

    flash:/system-a0101.bin verification successful.

  Start to check active package consistency.

    Active packages are consistent with committed packages on their own board.

    Active packages are consistent with the reference packages.

  Verifying packages on chassis 1 slot 1:

  Start to check active package completeness.

Verifying the file flash:/boot-a0101.bin on chassis 1 slot 1\...\...\...\...\...\...\...Done.

    flash:/boot-a0101.bin verification successful.

Verifying the file flash:/system-a0101.bin on chassis 1 slot 1\...\...\...\...\...\...\...Done.

    flash:/system-a0101.bin verification successful.

  Start to check active package consistency.

    Active packages are consistent with committed packages on their own board.

    Active packages are consistent with the reference packages.

Verification is done.

**ISSU \-- ISSU配置命令 \-- issu accept**

------------------------------------------------------------------------

![说明](ISSU命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[issu accept**]命令用来确认ISSU兼容升级，接受已升级的软件版本，并删除回滚定时器。

【命令】

**[issu accept**]

【视图】

用户视图

【缺省用户角色】

network-admin

【使用指导】

执行本命令后，系统会删除回滚定时器，本次ISSU升级过程中不会再进行自动回滚，用户可以执行**issu rollback**命令进行手动回滚。

此命令为可选命令，可以不执行此命令，直接执行后面的**issu commit**命令完成升级过程。

ISSU不兼容升级时，不需要执行该命令，执行该命令会提示失败。

【举例】

\# 版本兼容情况下，确认升级步骤。

\<Sysname\> issu accept

【相关命令】

·**issu load**

·**issu run switchover**

**ISSU \-- ISSU配置命令 \-- issu blade**

------------------------------------------------------------------------

![说明](ISSU命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[issu blade**]命令用来设置安全引擎的升级软件包。

【命令】

**[issu blade ***blade-model*** file **[{ **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \*]]

**[issu blade ***blade-model*** file ipe ***ipe-filename*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[blade ***blade-model*]：设备支持的安全引擎的型号，该参数必须完整输入，不区分大小写。可输入**boot-loader blade ？**，来获取该参数的取值。

**[boot**]：表示Boot包。

**[system**]：表示System包。

**[feature**]：表示Feature包。

*[filename*]：表示软件包的文件名，以.bin作为后缀名，从存储介质名开始为1～63个字符的字符串（包括存储介质名在内），不区分大小写。&\<1-30\>表示前面的参数最多可以输入30次。

**[ipe*** ipe-filename*]：IPE文件名，以.ipe作为后缀名，从存储介质名开始为1～63个字符的字符串（包括存储介质名在内），不区分大小写。

【使用指导】

该命令只是指定安全引擎的升级软件包，并不执行升级动作，等主控板升级时，安全引擎使用这些升级软件包启动来完成升级。组网环境不同，安全引擎的具体升级时机不同，具体描述请参见"基础配置指导"中的"ISSU"。如果不进行ISSU升级，而仅仅是重启安全引擎，该命令配置的软件包将不会生效。

当配置该命令时，命令中指定的软件包/IPE文件必须放在存储介质主分区的根目录下。

输入该命令后，系统将自动执行以下操作：

·进行命令行合法性检查。

·将升级文件全部拷贝到系统中所有的主控板和该类型的安全引擎上。如果指定的是IPE文件，则会自动解压到所有该类型的安全引擎上。

·如果源软件包放在主控板的存储介质上，拷贝完成后，提示用户是否需要删除源软件包。如果用户确认，则自动删除源软件包，以便释放空间。

【举例】

\# 配置型号为Blade-m9k的安全引擎的升级软件包为flash:/test.bin。（分布式设备－独立运行模式）

\<Sysname\> issu blade Blade-m9k file feature flash:/test.bin

Verifying the file flash:/test.bin on slot 1\...Done.

File flash:/test.bin already exists on slot 2.1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/test.bin to slot2.1#flash:/test.bin\...Done.

File flash:/test.bin already exists on slot 3.1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/test.bin to slot3.1#flash:/test.bin\...Done.

Delete flash:/test.bin from slot 5? [Y/N:N]

\# 配置型号为Blade-m9k的安全引擎的升级软件包为slot2.1#flash:/test.bin）。（分布式设备－独立运行模式）

\<Sysname\> issu blade Blade-m9k file feature slot2.1#flash:/test.bin

Verifying the file flash:/test.bin on slot 1\...Done.

File flash:/test.bin already exists on slot 3.1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/test.bin to slot3.1#flash:/test.bin\...Done.

\# 配置型号为Blade-m9k的安全引擎的升级软件包为flash:/test.ipe。（分布式设备－独立运行模式）

\<Sysname\> issu blade Blade-m9k file ipe flash:/test.ipe

Verifying the file flash:/test.ipe on slot 0\...Done.

File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on slot 5.

Overwrite the existing files? [Y/N:Y]

Decompressing file blade3fwm9k-cmw710-test-a0002.bin to flash:/blade3fwm9k-cmw710-test-a0002.bin\...Done.

File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on slot 2.1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/blade3fwm9k-cmw710-test-a0002.bin to slot2.1#flash:/blade3fwm9k-cmw710-test-a0002.bin\...Done.

File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on slot 3.1.

Overwrite the existing files? [Y/N:N]

Delete flash:/blade3fwm9k-cmw710-test-a0002.bin from slot 5? [Y/N:N]

Delete flash:/test.ipe from slot 5? [Y/N:N]

\# 配置型号为Blade-m9k的安全引擎的升级软件包为flash:/test.bin。（分布式设备－IRF模式）

\<Sysname\>issu blade Blade-m9k file feature flash:/test.bin

Verifying the file flash:/test.bin on chassis 1 slot 0\...Done.

File flash:/test.bin already exists on chassis 1 slot 2.1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/test.bin to chassis1#slot2.1#flash:/test.bin\...Done.

File flash:/test.bin already exists on chassis 1 slot 3.1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/test.bin to chassis1#slot3.1#flash:/test.bin\...Done.

Delete flash:/test.bin from chassis 1 slot 5? [Y/N:N]

\# 配置型号为Blade-m9k的安全引擎的升级软件包为chassis1#slot2.1#flash:/test.bin。（分布式设备－IRF模式）

\<Sysname\>issu blade Blade-m9k file feature chassis1#slot2.1#flash:/test.bin

Verifying the file flash:/test.bin on chassis 1 slot 0\...Done.

File flash:/test.bin already exists on chassis 1 slot 3.1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/test.bin to chassis1#slot3.1#flash:/test.bin\...Done.

\# 配置型号为Blade-m9k的安全引擎的升级软件包为chassis1#slot3.1#flash:/test.ipe。（分布式设备－IRF模式）

\<Sysname\>issu blade Blade-m9k file ipe chassis1#slot3.1#flash:/test.ipe

Verifying the file flash:/test.ipe on chassis 1 slot 0\...Done.

File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on chassis 1 slot 3.1.

Overwrite the existing files? [Y/N:Y]

Decompressing file blade3fwm9k-cmw710-test-a0002.bin to chassis1#slot3.1#flash:/blade3fwm9k-cmw710-test-a0002.bin\...Done

File flash:/blade3fwm9k-cmw710-test-a0002.bin already exists on chassis 1 slot 2.1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/blade3fwm9k-cmw710-test-a0002.bin to chassis1#slot2.1#flash:/blade3fwm9k-cmw710-test-a0002.bin\...Done.

**ISSU \-- ISSU配置命令 \-- issu commit**

------------------------------------------------------------------------

![说明](ISSU命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

(1)集中式设备

**[issu commit**]命令用来完成升级，升级完成后ISSU回到初始状态。执行此命令后，不能再通过ISSU回滚命令或者回滚定时器进行回滚操作。

(2)分布式设备－独立运行模式

**[issu commit**]命令用来对原主用主控板进行兼容版本升级，升级完成后ISSU回到初始状态。执行此命令后，不能再通过ISSU回滚命令或者回滚定时器进行回滚操作。

(3)集中式IRF设备

**[issu commit**]命令用来对原主设备及未升级的从设备进行兼容版本升级。所有成员设备完成升级后，本次升级结束，ISSU回到初始状态。执行此命令后，不能再通过ISSU回滚命令或者回滚定时器进行回滚操作。多个从设备的情况下应该在一个备设备启动完成并重新加入IRF后再对下一个从设备执行该命令，否则可能引起升级错误。

(4)分布式设备－IRF模式

对于单成员设备双主控的情况，**issu commit**命令用来对原主用主控板进行兼容版本升级，升级完成后ISSU回到初始状态。执行此命令后，不能再通过ISSU回滚命令或者回滚定时器进行回滚操作。

对于多成员设备的情况，**issu commit**命令用来对原主设备及未升级的从设备进行兼容版本升级。所有成员设备完成升级后，本次升级结束，ISSU回到初始状态。执行此命令后不能再通过ISSU回滚命令或者回滚定时器进行回滚操作。如果有多个成员设备需要通过**issu commit**命令进行升级，需要等到一个成员设备重启、重新加入IRF后再进行下一个成员设备的升级，否则可能造成升级错误。

【命令】

集中式设备：

**[issu commit**]

分布式设备－独立运行模式：

**[issu commit slot** *slot-number*]

集中式IRF设备：

**[issu commit slot** *slot-number*]

分布式设备－IRF模式单成员设备：

**[issu commit chassis** *chassis-number* **slot** *slot-number*]

分布式设备－IRF模式多成员设备：

**[issu commit chassis ***chassis-number*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[slot ***slot-number*]：原主用主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：待升级的原主设备以及其它从设备的成员编号。（集中式IRF设备）

**[chassis ***chassis-number* **slot** *slot-number*]：原主用主控板所在的槽位号。（分布式设备－IRF模式单成员设备）

**[chassis ***chassis-number*]：待升级的原主设备以及其它从设备的成员编号。（分布式设备－IRF模式多成员设备）

【使用指导】

从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过**display device**、{.ItemListCharChar}**display mdc**和**display system internal ha service-group**命令{.ItemListCharChar}查看到所有单板处于normal状态、所有MDC处于active状态和所有服务的action显示为0后，再执行**issu commit**命令，否则，命令会执行失败。（集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 版本兼容情况下，确认升级。（集中式设备）

\<Sysname\> issu commit

\# 版本兼容情况下，成员2已经升级完成成为新的主设备，升级原主设备（假设成员编号为3）和其他成员（假设成员编号为4和1）。（集中式IRF设备）

\<Sysname\> issu commit slot 3

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  3                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\<Sysname\> issu commit slot 4

Copying file flash:/feature.bin to slot4#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on slot 4\...\...\...\.....Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  4                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\<Sysname\> issu commit slot 1

Copying file flash:/feature.bin to slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on slot 1\...\...\...\.....Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  1                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 在双主控板，版本兼容情况下，升级原主用主控板。（分布式设备－独立运行模式）

\<Sysname\> issu commit slot 0

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  0                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 在单主控板，版本兼容情况下，确认原主用主控板的升级。（分布式设备－独立运行模式）

\<Sysname\> issu commit slot 0

\# 在多成员设备，版本兼容情况下，升级原主设备（假设成员编号为3）和其他成员（假设成员编号为4和1）。（分布式设备－IRF模式）

\<Sysname\> issu commit chassis 3

Copying file flash:/feature.bin to chassis3#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 3 slot 1\...\...\...\.....Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  3         0                 Service Upgrade

  3         1                 Service Upgrade

  3         2                 Service Upgrade

  3         3                 Service Upgrade

  3         4                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\<Sysname\> issu commit chassis 4

Copying file flash:/feature.bin to chassis4#slot0#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 4 slot 0\...\...\...\.....Done.

Copying file flash:/feature.bin to chassis4#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 4 slot 1\...\...\...\.....Done

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  4         0                 Service Upgrade

  4         1                 Service Upgrade

  4         2                 Service Upgrade

  4         3                 Service Upgrade

  4         4                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\<Sysname\> issu commit chassis 1

Copying file flash:/feature.bin to chassis1#slot0#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 1 slot 0\...\...\...\.....Done.

Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 1 slot 1\...\...\...\.....Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  1         0                 Service Upgrade

  1         1                 Service Upgrade

  1         2                 Service Upgrade

  1         3                 Service Upgrade

  1         4                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 在单成员设备双主控板，版本兼容情况下，升级原主用主控板。（分布式设备－IRF模式）

\<Sysname\> issu commit chassis 1 slot 0

Verifying the file flash:/feature.bin on chassis 1 slot 1\...\...\...\.....Done.

Upgrade summary according to following table:

  flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  1         0                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 在单成员设备单主控板，版本兼容情况下，确认升级。（分布式设备－IRF模式）

\<Sysname\> issu commit chassis 1 slot 0

本命令显示信息的描述请参见 表1-8(?270907887#_Ref329853865)。

【相关命令】

·**issu accept**

·**issu load**

·**issu run switchover**

**ISSU \-- ISSU配置命令 \-- issu load**

------------------------------------------------------------------------

**[issu load**]命令用来升级设备的启动软件包并将设备的主用下次启动软件包设置为指定的软件包。（集中式设备）

**[issu load**]命令用来升级备用主控板的启动软件包并将备用主控板的主用下次启动软件包设置为指定的软件包。（分布式设备－独立运行模式）

**[issu load**]命令用来升级从设备的启动软件包并将从设备的主用下次启动软件包设置为指定的软件包。（集中式IRF设备）

**[issu load**]命令用来升级全局备用主控板的启动软件包并将全局备用主控板的下次启动软件包设置为指定的软件包。（分布式独立设备－IRF模式单成员设备）

**[issu load**]命令用来升级从设备的启动软件包并将从设备的主用下次启动软件包设置为指定的软件包。（分布式独立设备－IRF模式多成员设备）

【命令】

集中式设备：

**[issu load file**[ { **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } \*]]

**[issu load file ipe ***ipe-filename*]

分布式设备－独立运行模式：

**[issu load file ***[filename*[\| **system** ]*filename*[\| **feature** ]*filename*&\<1-30\> } **\* slot** *slot-number*]

**[issu load file ipe ***ipe-filename*** slot ***slot-number*]

集中式]IRF设备：

**[issu load file ***[filename*[\| **system** ]*filename*[\| **feature** ]*filename*&\<1-30\> } **\* slot** *slot-number*&\<1-9\>]

**[issu load file ipe ***ipe-filename*** slot ***slot-number*&\<1-9\>]

分布式独立设备－]IRF模式单成员设备：

**[issu load file ***[filename*[\| **system** ]*filename*[\| **feature** ]*filename*&\<1-30\> } **\* chassis** *chassis-number* **slot** *slot-number*]

**[issu load file ipe ***ipe-filename*** chassis ***chassis-number ***slot ***slot-number*]

分布式独立设备－]IRF模式多成员设备：

**[issu load file **[{ **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } **\* chassis** *chassis-number*&\<1-3\>]]

**[issu load file ipe ***ipe-filename*** chassis** *chassis-number*&\<1-3\>]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[boot**]：表示Boot包。

**[system**]：表示System包。

**[feature**]：表示Feature包。

*[filename*]：表示软件包的文件名，以.bin作为后缀名，为1～63个字符的字符串，不区分大小写。&\<1-30\>表示前面的参数最多可以输入30次。（集中式设备）

**[ipe***ipe-filename*]：IPE文件名，以.ipe作为后缀名，为1～63个字符的字符串，不区分大小写。

**[slot ***slot-number*]：表示备用主控板的槽位号。如果设备只有一块主控板，则输入主用主控板的槽位号，用来完成整个设备的升级。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示从设备在IRF中的成员编号。&\<1-9\>表示前面的参数最多可以输入9次。（集中式IRF设备）

·如果IRF中只有一个成员设备，则输入该成员设备的编号，用来完成整个IRF的升级。

·如果IRF中有多个成员设备：

¡当要升级的软件包的版本和设备当前运行的软件包的版本兼容时，只允许输入一个*slot-number*。

¡当要升级的软件包的版本和设备当前运行的软件包的版本不兼容时，可以输入多个*slot-number*，一次升级多个从设备。

**[chassis ***chassis-number* **slot** *slot-number*]：如果IRF中只有一块主控板，则输入主用主控板所在设备的成员编号以及该主控板所在的槽位号，用来完成整个IRF的升级；如果设备上有两块主控板，则输入备用主控板所在设备的成员编号以及备用主控板所在的槽位号。（分布式独立设备－IRF模式单成员设备）

**[chassis ***chassis-number*]：表示从设备在IRF中的成员编号。&\<1-3\>表示前面的参数最多可以输入3次。（分布式设备－IRF模式多成员设备）

·当要升级的软件包的版本和设备当前运行的软件包的版本兼容时，只允许输入一个*chassis-number*；

·当要升级的软件包的版本和设备当前运行的软件包的版本不兼容时，可以输入多个*chassis-number*，一次升级多个成员设备。

【使用指导】

(1)集中式设备

当配置该命令时，命令中指定的软件包/IPE文件必须放在设备存储介质主分区的根目录下，文件名中必须包含存储介质的名称，形如flash:/xx.bin（flash:/xx.ipe）。

输入该命令后，系统将自动执行以下操作：

·进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。

·确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级会对CPU进行重启升级；重启升级会自动重启设备。

·按照升级策略进行升级，并将设备主用下次启动软件包设置为**issu load**命令中指定的包，以便指定的包在设备重启后能够继续生效。增量升级方式时是升级前进行设置，软重启和重启升级方式时是升级后进行设置。

(2)分布式设备－独立运行模式

当配置该命令时，命令中指定的软件包/IPE文件必须放在主用主控板存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含slot的信息，形如flash:/xx.bin（flash:/xx.ipe）。

当设备上有两块主控板时，**slot ***slot-number*请指定为备用主控板的槽位号。输入该命令后，系统将自动执行以下操作：

·进行版本兼容性检查。分为兼容版本的升级和不兼容版本的升级。

·确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级会对CPU进行重启升级；重启升级会自动重启指定主控板。

·按照升级策略进行升级备用主控板，并将备用主控板的主用下次启动软件包设置为issu load命令中指定的包。

当设备上只有一块主控板时，**slot ***slot-number*指定为主用主控板的槽位号。输入该命令后，系统将自动执行以下操作：

·进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。

·确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级会对CPU进行重启升级；重启升级会以指定的软件包为下次启动软件包自动重启设备。

·按照升级策略进行升级主用主控板，并将主用主控板的主用下次启动软件包设置为issu load命令中指定的包。

(3)集中式IRF设备

当配置该命令时，命令中指定的软件包/IPE文件必须放在主设备存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含slot的信息，形如flash:/xx.bin（flash:/xx.ipe）。

从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过**display device**、{.ItemListCharChar}**display mdc**和**display system internal ha service-group**命令{.ItemListCharChar}查看到所有单板处于normal状态、所有MDC处于active状态和所有服务的action显示为0后，再执行**issu load**命令，否则，命令会执行失败。

当IRF中只有一个成员设备时，**slot ***slot-number*请指定为该设备的成员编号。输入该命令后，系统将自动执行以下操作：

·进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。

·确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级会对CPU进行重启升级；重启升级会自动重启对应的成员设备。

·按照升级策略进行升级，并将该成员设备的主用下次启动软件包设置为**issu load**命令中指定的包。

当IRF中有多个成员设备时，可一次指定一个或者多个**slot ***slot-number*，**slot ***slot-number*均应为从设备的成员编号。如果IRF为环形连接，建议一次升级一半数量的物理上邻接的成员设备（也称为对半升级），以便尽量减少升级对整个IRF业务的影响。输入该命令后，系统将自动执行以下操作：

·进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。

·确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级对CPU进行重启升级；重启升级会自动重启对应的成员设备。

·按照升级策略进行升级从设备，并将指定成员设备的主用下次启动软件包设置为**issu load**命令中指定的包。

(4)分布式设备－IRF模式

当配置该命令时，命令中指定的软件包/IPE文件必须放在全局主用主控板存储介质主分区的根目录下，文件名中必须且只能包含存储介质的名称，不能包含chassis和slot的信息，形如flash:/xx.bin（flash:/xx.ipe）。

从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过**display device**、{.ItemListCharChar}**display mdc**和**display system internal ha service-group**命令{.ItemListCharChar}查看到所有单板处于normal状态、所有MDC处于active状态和所有服务的action显示为0后，再执行**issu load**命令，否则，命令会执行失败。

当IRF中只有一个成员设备且只有一块主控板时，**chassis ***chassis-number* **slot** *slot-number*请指定为主用主控板所在的槽位号。输入该命令后，系统将自动执行以下操作：

·进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。

·确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级对CPU进行重启升级；重启升级会自动重启主用主控板。

·按照升级策略进行升级主用主控板，并将主用主控板的主用下次启动软件包设置为**issu load**命令中指定的包。

当IRF中只有一个成员设备且有两块主控板时，**chassis ***chassis-number* **slot** *slot-number*请指定为备用主控板所在的槽位号。输入该命令后，系统将自动执行以下操作：

·进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。

·确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级对CPU进行重启升级；重启升级会自动重启备用主控板。

·按照升级策略进行升级备用主控板，并将备用主控板的主用下次启动软件包设置为**issu load**命令中指定的包。

当IRF中有多个成员设备时，**chassis ***chassis-number*请指定为从设备的成员编号。输入该命令后，系统将自动执行以下操作：

·进行版本兼容性检查，分为兼容版本的升级和不兼容版本的升级。

·确定升级策略。兼容升级的策略包括增量、软重启和重启升级。不兼容升级的策略只有重启升级。其中，增量升级会升级对应的进程；软重启升级对CPU进行重启升级；重启升级会自动重启对应的成员设备。

·按照升级策略进行升级从设备，并将从设备的主用下次启动软件包设置为**issu load**命令中指定的包**。**

【举例】

**[\# **]版本兼容情况下，使用flash:/boot.bin升级Boot包，使用flash:/system.bin升级System包，使用flash:/ssh.bin和flash:/http.bin升级Feature包。（集中式设备）

\<Sysname\> issu load file boot flash:/boot.bin system flash:/system.bin feature flash:/ssh.bin flash:/http.bin

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/boot.bin on the device\...Done.

Verifying the file flash:/system.bin on the device\...Done.

Verifying the file flash:/ssh.bin on the device\...Done.

Verifying the file flash:/http.bin on the device\...Done.

Upgrade summary according to following table:

flash:/boot.bin

  Running Version             New Version

  1.0.2                       1.0.3

flash:/system.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

flash:/ssh.bin

  Running Version             New Version

  None                        Alpha 7123

flash:/http.bin

  Running Version             New Version

  None                        Alpha 7123

Upgrade Way: Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，使用flash:/boot.bin升级Boot包，使用flash:/system.bin升级System包，使用flash:/ssh.bin和flash:/http.bin升级Feature包。（集中式设备）

\<Sysname\> issu load file boot flash:/boot.bin system flash:/system.bin feature flash:/ssh.bin flash:/http.bin

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/boot.bin on the device\...Done.

Verifying the file flash:/system.bin on the device\...Done.

Verifying the file flash:/ssh.bin on the device\...Done.

Verifying the file flash:/http.bin on the device\...Done.

Upgrade summary according to following table:

flash:/boot.bin

  Running Version             New Version

  1.0.2                       1.0.3

flash:/system.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

flash:/ssh.bin

  Running Version             New Version

  None                        Alpha 7123

flash:/http.bin

  Running Version             New Version

  None                        Alpha 7123

Upgrade Way: Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

\# 版本兼容情况下，使用flash:/feature.bin升级从设备2上的Feature包。（集中式IRF设备）

\<Sysname\> issu load file feature flash:/feature.bin slot 2

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on slot 1\...Done.

Copying file flash:/feature.bin to slot2#flash:/feature.bin\...\...Done.

Verifying the file flash:/feature.bin on slot 2\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  2                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，使用flash:/feature.bin升级从设备3和4上的Feature包。（集中式IRF设备）

\<Sysname\> issu load file feature flash:/feature.bin slot 3 4

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on slot 1\...Done.

Copying file flash:/feature.bin to slot3#flash:/feature.bin\...\...Done.

Verifying the file flash:/feature.bin on slot 3\...Done.

Copying file flash:/feature.bin to slot4#flash:/feature.bin\...\...Done.

Verifying the file flash:/feature.bin on slot 4\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  3                           Reboot

  4                           Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

\# 版本兼容情况下，使用flash:/feature.bin升级备用主控板1上的Feature包。（分布式设备－独立运行模式双主控）

\<Sysname\> issu load file feature flash:/feature.bin slot 1

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on slot 0\...Done.

Copying file flash:/feature.bin to slot1#flash:/feature.bin\...\...Done.

Verifying the file flash:/feature.bin on slot 1\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  1                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，使用flash:/feature.bin升级备用主控板1上的Feature包。（分布式设备－独立运行模式双主控）

\<Sysname\> issu load file feature flash:/feature.bin slot 1

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on slot 0\...Done.

Copying file flash:/feature.bin to slot1#flash:/feature.bin\...\...Done.

Verifying the file flash:/feature.bin on slot 1\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  1                           Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

\# 版本兼容情况下，使用flash:/feature.bin升级slot 0上的Feature包。（分布式设备－独立运行模式单主控）

\<Sysname\>issu load file feature flash:/feature.bin slot 0

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on slot 0\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  0                           Service Upgrade

  2                           Service Upgrade

  3                           Service Upgrade

  4                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，使用flash:/feature.bin升级主用主控板slot 0上的Feature包。（分布式设备－独立运行模式单主控）

\<Sysname\> issu load file feature flash:/feature.bin slot 0

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on slot 0\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  0                           Reboot

  2                           Reboot

  3                           Reboot

  4                           Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

\# 版本兼容情况下，使用flash:/feature.bin升级成员2上的Feature包。（分布式设备－IRF模式多成员设备）

\<Sysname\> issu load file feature flash:/feature.bin chassis 2

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.

Copying file flash:/feature.bin to chassis2#slot0#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 2 slot 0\...Done.

Copying file flash:/feature.bin to chassis2#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 2 slot 1\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  2         0                 Service Upgrade

  2         1                 Service Upgrade

  2         2                 Service Upgrade

  2         3                 Service Upgrade

  2         4                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，使用flash:/feature.bin升级从设备3和从设备4上的Feature包。（分布式设备－IRF模式多成员设备）

\<Sysname\>issu load file feature flash:/feature.bin chassis 3 4

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.

Copying file flash:/feature.bin to chassis3#slot0#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 3 slot 0\...Done.

Copying file flash:/feature.bin to chassis3#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 3 slot 1\...Done.

Copying file flash:/feature.bin to chassis4#slot0#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 4 slot 0\...Done.

Copying file flash:/feature.bin to chassis4#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 4 slot 1\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  3         0                 Reboot

  3         1                 Reboot

  3         2                 Reboot

  3         3                 Reboot

  3         4                 Reboot

  4         0                 Reboot

  4         1                 Reboot

  4         2                 Reboot

  4         3                 Reboot

  4         4                 Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

\# 版本兼容情况下，使用flash:/feature.bin升级成员设备1的备用主控板slot 1上的Feature包。（分布式设备－IRF模式单成员设备双主控）

\<Sysname\>issu load file feature flash:/feature.bin chassis 1 slot 1

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.

Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 1 slot 1\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  1         1                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，使用flash:/feature.bin升级成员设备1的备用主控板slot 1上的Feature包。（分布式设备－IRF模式单成员设备双主控）

\<Sysname\>issu load file feature flash:/feature.bin chassis 1 slot 1

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.

Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 1 slot 1\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  1         1                 Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

\# 版本兼容情况下，使用flash:/feature.bin升级成员设备1的主用主控板slot0上的Feature包。（分布式设备－IRF模式单成员设备单主控）

\<Sysname\>issu load file feature flash:/feature.bin chassis 1 slot 0

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  1         0                 Service Upgrade

  1         2                 Service Upgrade

  1         3                 Service Upgrade

  1         4                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，使用flash:/feature.bin升级成员设备1的主用主控板slot0上的Feature包。（分布式设备－IRF模式单成员设备单主控）

\<Sysname\>issu load file feature flash:/feature.bin chassis 1 slot 0

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:Y]

Verifying the file flash:/feature.bin on chassis 1 slot 0\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  1         0                 Reboot

  1         2                 Reboot

  1         3                 Reboot

  1         4                 Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

表1-8 issu load命令显示信息描述表

字段

描述

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? Y/N

当前操作会删除上一次ISSU升级的日志信息和回滚点，并且未保存的配置可能会丢失，询问用户是否继续执行升级操作

Verifying the file flash:/xx.bin on chassis 1 slot 0\...\...\...\...\...\...\...\...\...\...\....Done.

验证文件是否合法

Decompressing file *A* to *B*\...\...\...\...\...\...\...\...\...Done.

将文件从位置*A*解压缩到位置*B*。只有使用IPE文件升级时，才显示该信息

Copying file *B* to *C*\...\...Done.

将文件从位置*B*拷贝到位置*C*。当配置备用主控板时才有该提示信息（分布式设备－独立运行模式）

将文件从位置*B*拷贝到位置*C*。当配置从设备时才有该提示信息（集中式IRF设备）

将文件从位置*B*拷贝到位置*C*。当配置全局备用主控板时才有该提示信息（分布式设备－IRF模式）

Upgrade summary according to following table

升级信息摘要

Running Version

设备当前运行的相同类型软件包的产品版本号

New Version

将要升级的软件包的产品版本号

Chassis

设备在IRF中的成员编号（分布式设备－IRF模式）

Slot

单板所在的槽位号（分布式设备－独立运行模式/分布式设备－IRF模式）

设备在IRF中的成员编号（集中式IRF设备）

Upgrade Way

升级策略，取值可能为：

·Service Upgrade：表示服务级增量升级，该方式下，仅对本业务模块有影响，对系统以及其他业务模块没有影响

·File Upgrade：表示文件级增量升级。该方式下，仅对系统内的、用户不可见的程序文件进行升级，对系统以及业务模块没有影响

·ISSU Reboot：表示通过软重启方式升级

·Reboot：表示通过重启方式升级

·Sequence Reboot：表示逐次重启方式。只有网板支持该升级方式，当网板需要重启升级时，为了避免重启升级过程中流量中断，系统会自动升级完毕一块网板后，再自动升级下一块网板，直到所有网板升级完毕后，再自动升级主控板。该字段的支持情况与网板的型号有关，请以设备的实际情况为准

Upgrading software images to compatible versions. Continue? Y/N

询问用户是否执行兼容升级操作

Upgrading software images to incompatible versions. Continue? Y/N

询问用户是否执行不兼容升级操作

**ISSU \-- ISSU配置命令 \-- issu pex**

------------------------------------------------------------------------

![说明](ISSU命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[issu pex**]命令用来指定PEX设备的升级软件包。

【命令】

**[issu pex ***pex-model*** file **[{ **boot** *filename* \| **system** *filename* \| **feature** *filename*&\<1-30\> } **\***]]

**[issu pex ***pex-model*** file ipe ***ipe-filename*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[pex-model*]：设备支持的PEX设备的型号，该参数必须完整输入，不区分大小写。可输入**boot-loader pex ？**，回车，来获取该参数的取值。

**[boot**]：表示Boot包。

**[system**]：表示System包。

**[feature**]：表示Feature包。

*[filename*]：表示软件包的文件名，以.bin作为后缀名，为1～63个字符的字符串，不区分大小写。&\<1-30\>表示前面的参数最多可以输入30次。

**[ipe*** ipe-filename*]：IPE文件名，以.ipe作为后缀名，为1～63个字符的字符串，不区分大小写。

【使用指导】

该命令只是指定PEX设备的升级软件包，并不执行升级动作，而是等主控板升级时，PEX设备使用这些升级软件包启动来完成升级。组网环境不同，PEX设备的具体升级时机不同，具体描述请参见"基础配置指导"中的"ISSU"。如果不进行ISSU升级，而仅仅是重启PEX设备，该命令配置的软件包将不会生效。

当配置该命令时，命令中指定的软件包/IPE文件必须放在存储介质主分区的根目录下。

对于本地无存储介质的PEX设备，输入该命令后，系统将自动执行以下操作：

·进行命令行合法性检查。

·将升级文件全部拷贝到系统中所有的主控板上。如果指定的是IPE文件，那么会自动解压到所有主控板上。

对于本地有存储介质的PEX设备，输入该命令后，系统将自动执行以下操作：

·进行命令行合法性检查。

·将升级文件全部拷贝到系统中所有的主控板和该类型的PEX设备上。如果指定的是IPE文件，则会自动解压到所有该类型的PEX设备上。

·拷贝完成后，提示用户是否需要删除源软件包。如果用户确认，则自动删除源软件包，以便释放空间。

【举例】

\# 指定型号为PEX-S5120HI的PEX设备的升级软件包为flash:/devkit.bin（本地无存储介质的PEX设备）。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> issu pex PEX-S5120HI file feature flash:/devkit.bin

Verifying the file flash:/devkit.bin on slot 1\...Done.

File flash:/devkit.bin already exists on slot 1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/devkit.bin to slot1#flash:/devkit.bin\...Done.

\<Sysname\>

\# 指定型号为PEX-S5120HI的PEX设备的升级软件包为flash:/devkit.bin（本地有存储介质的PEX设备）。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> issu pex PEX-S5500 file feature flash:/devkit.bin

Verifying the file flash:/devkit.bin on slot 1\...Done.

File flash:/devkit.bin already exists on slot 110.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/devkit.bin to slot110#flash:/devkit.bin\...Done.

Delete flash:/devkit.bin from slot 1? [Y/N:Y]

\# 指定型号为PEX-S5120HI的PEX设备的升级软件包为flash:/test.ipe（本地无存储介质的PEX设备）。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> issu pex PEX-S5120HI file ipe flash:/test.ipe

Verifying the file flash:/test.ipe on slot 1\...\...\...\...Done.

File flash:/devkit.bin already exists on slot 1.

File flash:/manufacture.bin already exists on slot 1.

Overwrite the existing files? [Y/N:Y]

Decompressing file devkit.bin to flash:/devkit.bin. \.....Done.

Decompressing file manufacture.bin to flash:/manufacture.bin\.....Done.

File flash:/devkit.bin already exists on slot 2.

File flash:/manufacture.bin already exists on slot 2.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/devkit.bin to slot2#flash:/devkit.bin. \...Done.

Copying file flash:/manufacture.bin to slot2#flash:/manufacture.bin\....Done.

\# 指定型号为PEX-S5120HI的PEX设备的升级软件包为flash:/test.ipe（本地有存储介质的PEX设备）。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> issu pex PEX-S5120HI file ipe flash:/test.ipe

Verifying the file flash:/test.ipe on slot 1\...\...\.....Done.

Decompressing file devkit-patch.bin to flash:/devkit-patch.bin\...Done.

Decompressing file manufacture.bin to flash:/manufacture.bin\.....Done.

Copying file flash:/devkit-patch.bin to slot110#flash:/devkit-patch.bin\...Done.

Copying file flash:/manufacture.bin to slot110#flash:/manufacture.bin\...Done.

Delete flash:/devkit-patch.bin from slot 1? [Y/N:Y]

Delete flash:/manufacture.bin from slot 1? [Y/N:Y]

Delete flash:/test.ipe from slot 1? [Y/N:Y]

\# 指定型号为PEX-S5120HI的PEX设备的升级软件包为flash:/devkit.bin（本地无存储介质的PEX设备）。（分布式设备－IRF模式）

\<Sysname\> issu pex PEX-S5120HI file feature flash:/devkit.bin

Verifying the file flash:/devkit.bin on chassis 1 slot 0\...\...\...\...Done.

File flash:/devkit.bin already exists on chassis 1 slot 1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/devkit.bin to chassis1#slot1#flash:/devkit.bin\...Done.

\# 指定型号为PEX-S5120HI的PEX设备的升级软件包为flash:/devkit.bin（本地有存储介质的PEX设备）。（分布式设备－IRF模式）

\<Sysname\> issu pex PEX-S5120HI file feature flash:/devkit.bin

Verifying the file flash:/devkit.bin on chassis 1 slot 0\...\...\...\...Done.

File flash:/devkit.bin already exists on chassis 101 slot 0.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/devkit.bin to chassis101#slot0#flash:/devkit.bin\...Done.

Delete flash:/devkit.bin from chassis 1 slot 1? [Y/N:Y]

\# 指定型号为PEX-S5120HI的PEX设备的升级软件包为flash:/test.ipe（本地无存储介质的PEX设备）。（分布式设备－IRF模式）

\<Sysname\> issu pex PEX-S5120HI file ipe flash:/test.ipe

Verifying the file flash:/test.ipe on chassis 1 slot 0\...\...\...\...Done.

File flash:/devkit.bin already exists on chassis 1 slot 0.

File flash:/manufacture.bin already exists on chassis 1 slot 0.

Overwrite the existing files? [Y/N:Y]

Decompressing file devkit.bin to flash:/devkit.bin. \.....Done.

Decompressing file manufacture.bin to flash:/manufacture.bin\.....Done.

File flash:/devkit.bin already exists on chassis 1 slot 1.

File flash:/manufacture.bin already exists on chassis 1 slot 1.

Overwrite the existing files? [Y/N:Y]

Copying file flash:/devkit.bin to chasis1#slot1#flash:/devkit.bin. \...Done.

Copying file flash:/manufacture.bin to chassis1#slot1#flash:/manufacture.bin\....Done.

\# 指定型号为PEX-S5120HI的PEX设备的升级软件包为flash:/test.ipe（本地有存储介质的PEX设备）。（分布式设备－IRF模式）

\<Sysname\> issu pex PEX-S5120HI file ipe flash:/test.ipe

Verifying the file flash:/test.ipe on chassis 1 slot 0\...\...\...\...Done.

Decompressing file devkit.bin to flash:/devkit.bin\...Done.

Decompressing file manufacture.bin to flash:/manufacture.bin\.....Done.

Copying file flash:/devkit.bin to chassis101#slot0#flash:/devkit.bin\...Done.

Copying file flash:/manufacture.bin to chassis101#slot0#flash:/manufacture.bin\...Done.

Delete flash:/devkit.bin from chassis 1 slot 1? [Y/N:Y]

Delete flash:/manufacture.bin from chassis 1 slot 1? [Y/N:Y]

Delete flash:/test.ipe from chassis 1 slot 1? [Y/N:Y]

【相关命令】

·**issu load**

**ISSU \-- ISSU配置命令 \-- issu rollback**

------------------------------------------------------------------------

![说明](ISSU命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[issu rollback**]命令用来回滚到升级前的版本。

【命令】

**[issu **]**rollback**

【视图】

用户视图

【缺省用户角色】

network-admin

【使用指导】

设备支持自动回滚和手动回滚，自动回滚定时器的时长由**issu rollback-timer**命令配置；手工回滚由**issu rollback**命令触发。

·不兼容版本升级时，不会启动回滚定时器，即不支持自动回滚。兼容版本只有执行**issu run switchover**命令时才会创建回滚定时器，因此，自动回滚只有在兼容版本ISSU升级状态为Swtiching后才生效。

·单主控兼容升级不支持自动回滚。（分布式设备－独立运行模式/分布式设备－IRF模式）

·当ISSU升级状态为Loading时进行手工回滚，可能会回滚失败。回滚操作结束后，请使用**display version**命令来查看设备当前运行的版本，验证回滚结果。

·当ISSU升级状态为Loaded和Accepted时，支持手工回滚。

·兼容升级、ISSU升级状态为Switching和Switchover时，支持手工回滚。

·不兼容升级、ISSU升级状态为Switching时，不支持手工回滚。

·不管兼容升级还是不兼容升级，Switching状态时如果进行手工回滚或者发生自动回滚，整个系统是会重启。

·当ISSU升级状态为Commiting时，不允许进行手工和自动回滚操作。

·多成员设备的情况下，执行**issu run switchover**后，再进行回滚操作，回滚保证版本回到升级前，并且主备状态也会和升级前一致。（集中式IRF设备）

·多成员设备的情况下，执行**issu run switchover**后，再进行回滚操作，回滚只保证版本回到升级前，但不能保证主备状态和升级前一致。（分布式设备－IRF模式）

【举例】

\# 回滚到升级之前的版本。

\<Sysname\> issu rollback

This command will quit the ISSU process and roll back to the previous version. Continue? [Y/N:y]

【相关命令】

·**issu accept**

·**issu commit**

·**issu load**

·**issu run switchover**

**ISSU \-- ISSU配置命令 \-- issu rollback-timer**

------------------------------------------------------------------------

![说明](ISSU命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[issu rollback-timer**]命令用来设置回滚定时器时长。

**[undo issu rollback-timer**]命令用来恢复缺省情况。

【命令】

**[issu** **rollback-timer** *minutes*]

**[undo issu rollback-timer**]

【缺省情况】

回滚定时器的时长为45分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

*[minutes*]：回滚定时器的时长，取值范围为0～120，单位为分钟。如果时长设置为0，则表示关闭自动回滚功能。

【使用指导】

兼容版本升级的情况下，执行**issu run switchover**命令后系统会自动启动回滚定时器。如果在指定的时间内（回滚定时器超时前）未执行**issu accept**或者**issu commit**命令，则系统会自动回滚到升级前的版本。

设备进行升级时，不会启动回滚定时器。（集中式设备）

当系统中只配备了一块主控板并进行升级时，不会启动回滚定时器。（分布式设备－独立运行模式/分布式设备－IRF模式）

当系统中只有一台成员设备并进行升级时，不会启动回滚定时器。（集中式IRF设备）

不兼容升级不会启动回滚定时器。

新设置的时长会在下次ISSU升级中生效。

【举例】

\# 设置回滚定时器时长为50分钟。

\<Sysname\> system-view

Sysname issu rollback-timer 50

【相关命令】

·**issu rollback**

**ISSU \-- ISSU配置命令 \-- issu run switchover**

------------------------------------------------------------------------

![说明](ISSU命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

分布式设备－独立运行模式：

**[issu run switchover**]命令在升级兼容软件包的情况下，用来进行ISSU倒换，并且升级业务板和网板。升级不兼容软件包的情况下，用来进行ISSU倒换，并且将剩余待升级的所有单板进行升级。

集中式IRF设备：

**[issu run switchover**]命令在升级兼容软件包的情况下，用来进行ISSU倒换。在升级不兼容软件包的情况下，用来进行ISSU倒换，并且升级剩余的成员设备。

分布式设备－IRF模式单成员设备：

**[issu run switchover**]命令在升级兼容软件包的情况下，用来进行ISSU倒换，并且升级业务板和网板。升级不兼容软件包的情况下，用来进行ISSU倒换，并且将剩余待升级的所有单板进行升级。

分布式设备－IRF模式多成员设备：

**[issu run switchover**]命令在升级兼容软件包的情况下，用来进行ISSU倒换。升级不兼容软件包的情况下，用来进行ISSU倒换，并且将剩余待升级的成员设备进行升级。

【命令】

**[issu run switchover**]

【视图】

用户视图

【缺省用户角色】

network-admin

【使用指导】

(1)分布式设备－独立运行模式

当设备上有两块主控板时，输入该命令后，系统将自动执行以下操作：

·兼容升级：增量升级时系统会将升级的进程进行进程级主备倒换；软重启或者重启升级时系统会将当前主用主控板使用原版本重新启动，将刚使用**issu load**命令升级的备用主控板上倒换成主用主控板。并升级业务板和网板。

·不兼容升级：当前主用主控板、业务板和网板以新版本重新启动，刚使用**issu load**命令升级的备用主控板倒换成主用主控板，原有主用主控板、业务板和网板重启完成后即完成升级过程。

当设备上只有一块主控板并需要升级时，不需要使用此命令。

(2)集中式IRF设备

从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过**display device**、{.ItemListCharChar}**display mdc**和**display system internal ha service-group**命令{.ItemListCharChar}查看到所有单板处于normal状态、所有MDC处于active状态和所有服务的action显示为0后，再执行**issu run switchover**命令，否则，命令会执行失败。

输入该命令后，系统将自动执行以下操作：

·兼容升级：增量升级时系统会对升级的进程进行了进程级主备倒换；软重启或者重启升级时系统会将当前主设备使用原版本重新启动，将刚使用issu load命令升级的从设备选举为新主设备。

·不兼容版本升级：执行**issu load**后IRF分裂，生成两个的IRF。执行**issu run switchover**重启并升级原IRF，原IRF组重启后加入新的IRF即完成升级过程，系统选择新IRF的主设备为合并后IRF的主设备。

当设备上只有一个成员并需要升级时，不需要使用此命令。

(3)分布式设备－IRF模式

从设备重启后，会自动批量备份主设备的配置和状态数据。请等待批量备份完成后，即分别通过**display device**、{.ItemListCharChar}**display mdc**和**display system internal ha service-group**命令{.ItemListCharChar}查看到所有单板处于normal状态、所有MDC处于active状态和所有服务的action显示为0后，再执行**issu run switchover**命令，否则，命令会执行失败。

当设备上只有一个成员设备，多个主控板时，输入该命令后，系统将自动执行以下操作：

·兼容升级：增量升级时系统会将升级的进程进行进程级主备倒换；软重启或者重启升级时系统会将当前主用主控板使用原版本重新启动，将刚使用**issu load**命令升级的备用主控板上倒换成主用主控板。同时升级业务板和网板。

·不兼容升级：当前主用主控板、业务板和网板以新版本重新启动，刚使用**issu load**命令升级的备用主控板倒换成主用主控板，原有主用主控板、业务板和网板重启完成后即完成升级过程。

当设备上只有一个成员并且只有一个主控板且需要升级时，不需要使用此命令。

当设备上有多个成员设备时，输入该命令后，系统将自动执行以下操作：

·兼容版本升级：增量升级时系统会对升级的进程进行了进程级主备倒换；软重启或者重启升级时系统会将当前主设备的主控板使用原版本重新启动，将刚使用**issu load**命令升级完成的从设备选举为IRF的主设备。

·不兼容版本升级：执行**issu load**后IRF分裂，生成两个的IRF。执行**issu run switchover**重启并升级原IRF，原IRF重启后加入新的IRF即完成升级过程，系统选择新IRF的主设备为合并后IRF的主设备。

需要注意的是：

·兼容版本升级时，如果在回滚定时器超时时仍未执行**issu accept**或者**issu commit**命令，则系统会自动回滚到升级前的版本。

·兼容版本升级时，如果业务板和网板无法使用增量或者软重启升级，这种情况下业务板和网板会重启，并从新主控板加载最新的软件包，途经此业务板和网板的流量会中断，流量恢复时间是"业务板和网板启动时间+业务板和网板状态恢复时间"。

·不兼容版本升级执行**issu run switchover**之后，即完成升级过程。

【举例】

\# 版本兼容情况下，进行主备倒换，同时升级业务板和网板。（分布式设备－独立运行模式双主控）

\<Sysname\> issu run switchover

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Switchover Way

  0                           Active standby process switchover

  Slot                        Upgrade Way

  2                           Service Upgrade

  3                           Service Upgrade

  4                           Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:]

\# 版本不兼容情况下，进行主备倒换，同时升级原主板、业务板和网板。（分布式设备－独立运行模式双主控）

\<Sysname\> issu run switchover

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  0                           Reboot

  2                           Reboot

  3                           Reboot

  4                           Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:]

\# 版本兼容情况下，进行主备倒换。（集中式IRF设备）

\<Sysname\> issu run switchover

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Switchover Way

  1                           Active standby process switchover

Upgrading software images to compatible versions. Continue? [Y/N:]

\# 版本不兼容情况下，进行主备倒换，同时升级成员设备1（主设备）和成员设备2（从设备）。（集中式IRF设备）

\<Sysname\> issu run switchover

Copying file flash:/feature.bin to slot2#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on slot 2\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Slot                        Upgrade Way

  1                           Reboot

  2                           Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:]

\# 版本兼容情况下，进行主备倒换。（分布式设备－IRF模式多成员设备）

\<Sysname\> issu run switchover

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

Chassis   Slot              Switchover Way

  1         0                 Active standby process switchover

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，进行主备倒换，同时升级成员设备1（主设备）和成员设备2（从设备）。（分布式设备－IRF模式多成员设备）

\<Sysname\> issu run switchover

Copying file flash:/feature.bin to chassis1#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 1 slot 1\...Done.

Copying file flash:/feature.bin to chassis2#slot0#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 2 slot 0\...Done.

Copying file flash:/feature.bin to chassis2#slot1#flash:/feature.bin\...Done.

Verifying the file flash:/feature.bin on chassis 2 slot 1\...Done.

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  1         0                 Reboot

  1         1                 Reboot

  1         2                 Reboot

  1         3                 Reboot

  1         4                 Reboot

  2         0                 Reboot

  2         1                 Reboot

  2         2                 Reboot

  2         3                 Reboot

  2         4                 Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

\# 版本兼容情况下，进行主备倒换，同时升级业务板和网板。（分布式设备－IRF模式单成员设备双主控）

\<Sysname\> issu run switchover

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Switchover Way

  1         0                 Active standby process switchover

  Chassis   Slot              Upgrade Way

  1         2                 Service Upgrade

  1         3                 Service Upgrade

  1         4                 Service Upgrade

Upgrading software images to compatible versions. Continue? [Y/N:y]

\# 版本不兼容情况下，进行主备倒换，同时升级原主控板、业务板和网板。（分布式设备－IRF模式单成员设备双主控）

\<Sysname\> issu run switchover

Upgrade summary according to following table:

flash:/feature.bin

  Running Version             New Version

  Alpha 7122                  Alpha 7123

  Chassis   Slot              Upgrade Way

  1         0                 Reboot

  1         2                 Reboot

  1         3                 Reboot

  1         4                 Reboot

Upgrading software images to incompatible versions. Continue? [Y/N:y]

表1-9 issu load命令显示信息描述表

字段

描述

Copying file *A* to *B*\...\...Done.

将文件从位置*A*拷贝到位置*B*。只有不兼容升级其它从设备时才有该提示信息（集中式IRF设备）

将文件从位置*A*拷贝到位置*B*。只有不兼容升级其它全局备用主控板时才有该提示信息（分布式设备－IRF模式）

Verifying the file flash:/xx.bin on chassis 1 slot 0\.....Done.

验证文件是否合法

Switchover Way

倒换方式，取值可能为：

·Active standby process switchover：表示主备进程的倒换

·Active standby MPU switchover：表示主备主控板之间的倒换（分布式设备－独立运行模式）

·Global active standby MPU switchover：表示全局主备主控板之间的倒换（分布式设备－IRF模式）

·Master subordinate switchover：表示主设备和从设备之间的倒换（集中式IRF）

其它字段

请参见 表1-8(?270907887#_Ref329853865)

【相关命令】

·**issu load**

**ISSU \-- ISSU配置命令 \-- reset install log-history oldest**

------------------------------------------------------------------------

**[reset install log-history oldest**]命令用来清除ISSU日志。

【命令】

**[reset install log-history oldest ***log-number*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[log-number*]：ISSU日志的数量。

【使用指导】

使用该命令，系统将清除指定数量的、时间最早的、与ISSU升级相关的日志。

【举例】

\# 清除2条最早的ISSU日志。

\<Sysname\> reset install log-history oldest 2

【相关命令】

·**display install log**

**ISSU \-- ISSU配置命令 \-- reset install rollback oldest**

------------------------------------------------------------------------

**[reset install rollback oldest**]命令用来清除ISSU回滚点。

【命令】

**[reset install rollback oldest** *point-id*]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

*[point-id*]：系统存储的回滚点的编号。

【使用指导】

使用该命令，系统将清除指定回滚点[以及比该回滚点更老的回滚点。]

【举例】

\# 清除编号为2以及比2号回滚点更老的回滚点。

\<Sysname\> reset install rollback oldest 2

【相关命令】

·**display install rollback**
