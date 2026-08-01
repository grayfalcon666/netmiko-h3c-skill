<!-- CMD-INDEX
  chassis convert mode irf            | 系统视图             | L79
  display irf                         | 任意视图             | L147
  display irf configuration           | 任意视图             | L271
  display irf link                    | 任意视图             | L365
  display irf topology                | 任意视图             | L517
  display irf-port load-sharing mode  | 任意视图             | L605
  display mad                         | 任意视图             | L739
  easy-irf                            | 系统视图             | L881
  irf auto-merge enable               | 系统视图             | L1043
  irf auto-update enable              | 系统视图             | L1103
  irf domain                          | 任意视图             | L1151
  irf link-delay                      | 系统视图             | L1199
  irf isolate member                  | 系统视图             | L1243
  irf mac-address persistent          | 系统视图             | L1289
  irf member                          | 系统视图             | L1347
  irf member description              | 系统视图             | L1403
  irf member priority                 | 系统视图             | L1449
  irf member renumber                 | 系统视图             | L1499
  irf priority                        | 系统视图             | L1557
  irf-port                            | 系统视图             | L1613
  irf-port global load-sharing mode   | 系统视图             | L1677
  irf-port load-sharing mode          | IRF端口视图          | L1767
  irf-port port-number                | 系统视图             | L1857
  irf-port-configuration active       | 系统视图             | L1907
  mad arp enable                      | VLAN接口视图         | L1987
  mad bfd enable                      | VLAN接口视图         | L2049
  mad enable                          | 聚合接口视图           | L2105
  mad exclude interface               | 系统视图             | L2189
  mad ip address                      | VLAN接口视图         | L2245
  mad nd enable                       | VLAN接口视图         | L2313
  mad restore                         | 系统视图             | L2375
  port group interface                | IRF端口视图          | L2417
  chassis convert mode irf            | 系统视图             | L2495
  display irf                         | 任意视图             | L2571
  display irf configuration           | 任意视图             | L2687
  display irf link                    | 任意视图             | L2761
  display irf topology                | 任意视图             | L2913
  display irf-port load-sharing mode  | 任意视图             | L2991
  display mad                         | 任意视图             | L3147
  display port restricted             | 任意视图             | L3301
  easy-irf                            | 系统视图             | L3359
  irf auto-merge enable               | 系统视图             | L3521
  irf auto-update enable              | 系统视图             | L3579
  irf domain                          | 系统视图             | L3633
  irf link-delay                      | 系统视图             | L3681
  irf isolate member                  | 系统视图             | L3727
  irf mac-address persistent          | 系统视图             | L3773
  irf member                          | 系统视图             | L3833
  irf member description              | 系统视图             | L3885
  irf member priority                 | 系统视图             | L3931
  irf member renumber                 | 系统视图             | L3985
  irf mode enhanced                   | 系统视图             | L4055
  irf priority                        | 系统视图             | L4123
  irf slot member                     | 用户视图             | L4175
  irf-port load-sharing mode          | 系统视图/IRF端口视图     | L4225
  irf-port member-id/port-number      | 系统视图             | L4321
  irf-port port-number                | 系统视图             | L4371
  irf-port-configuration active       | 系统视图             | L4417
  mad arp enable                      | 三层接口视图           | L4497
  mad bfd enable                      | 三层接口视图           | L4553
  mad enable                          | 聚合接口视图           | L4609
  mad exclude interface               | 系统视图             | L4683
  mad ip address                      | 三层接口视图           | L4733
  mad nd enable                       | VLAN接口视图         | L4795
  mad restore                         | 系统视图             | L4857
  port group interface                | IRF端口视图          | L4897
  associate                           | PEX端口视图          | L4991
  description                         | PEX端口视图          | L5057
  display pex working-mode (Centralized IRF devices) | 任意视图             | L5099
  display pex working-mode (Distributed devices--In IRF mode) | 任意视图             | L5191
  display pex-port                    | 任意视图             | L5265
  pex working-mode (Centralized IRF devices) | 系统视图             | L5433
  pex working-mode (Distributed devices--In IRF mode) | 系统视图             | L5491
  port group interface                | PEX端口视图          | L5561
  pex-port                            | 系统视图             | L5649
-->

**IRF \-- IRF2配置命令（集中式IRF设备） \-- chassis convert mode irf**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[chassis convert mode irf**]命令用来将设备的运行模式切换到IRF模式。

**[undo chassis convert mode**]命令用来将设备的运行模式切换到独立运行模式。

【命令】

**[chassis convert mode irf**]

**[undo chassis convert mode**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

设备出厂时处于独立运行模式。如果在本次运行过程中，没有修改设备的运行模式，则下次启动会延用本次启动的运行模式；如果在本次运行过程中，修改了设备的运行模式，则设备会自动重启，切换到新的模式。

请根据组网需要来配置设备的运行模式。当设备从独立运行模式切换到IRF模式后，即便只有一台设备也会形成IRF。因为管理和维护IRF需要耗费一定的系统资源，所以，如果当前组网中设备不需要和别的设备组成IRF时，建议将运行模式配置为独立运行模式。

设备从独立运行模式切换到IRF模式时，需要使用成员编号进行配置文件的自动转换。如果模式切换前没有配置成员编号，则系统会自动使用1作为成员编号。

需要注意的是，确认模式切换操作后，设备会自动重启，完成运行模式的切换。

【举例】

\# 设备当前处于独立运行模式时，将设备切换到IRF模式。

\<Sysname\> system-view

Sysname chassis convert mode irf

The device will switch to IRF mode and reboot. You are recommended to save the current running configuration and specify the configuration file for the next startup. Continue? [Y/N:y]

Do you want to convert the content of the next startup configuration file flash:/startup.cfg to make it available in IRF mode? [Y/N:y]

Now rebooting, please wait\...

Saving the converted configuration file to the main board succeeded.

\# 设备当前处于IRF模式时，将设备切换到独立运行模式。

\<Sysname\> system-view

Sysname undo chassis convert mode

The device will switch to stand-alone mode and reboot。 You are recommended to save the current running configuration and specify the configuration file for the next startup. Continue? [Y/N:y]

Do you want to convert the content of the next startup configuration file flash:/startup.cfg to make it available in stand-alone mode? [Y/N:y]

Now rebooting, please wait\...

Saving the converted configuration file to the main board succeeded.

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf**

------------------------------------------------------------------------

**[display irf**]命令用来显示IRF的相关信息，包括：成员编号、角色、优先级、CPU MAC地址以及描述信息。

【命令】

**[display irf**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IRF的相关信息。

\<Sysname\> display irf

MemberID  Role     Priority    CPU-Mac           Description

   1      Loading  1           00e0-fcbe-3102    F1Num001

 \*+2      Master   1           00e0-fcb1-ade2    F1Num002

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 \* indicates the device is the master.

 + indicates the device through which the user logs in.

 The Bridge MAC of the IRF is: 00e0-fc00-1000

 Auto upgrade                   : yes

 Mac persistent                 : always

 Domain ID                      : 30

表1-1 display irf命令显示信息描述表

字段

描述

MemberID

成员设备的编号

·如果编号前带"\*"，表示该设备是主设备

·如果编号前带"+"，表示该设备是用户当前登录的、正在操作的设备

Role

成员设备的角色，可能为：

·Standby：从设备

·Master：主设备

·Loading：正在自动加载系统启动文件

Priority

成员设备的优先级

CPU-MAC

设备的CPU MAC地址

Description

设备的描述信息

·没有描述信息时，Description字段显示为\"\-\-\-\--\"

·如果描述信息较多，无法在一行中完全显示，则以"..."结尾，省略后面的信息。此时可以使用**display current-configuration**来查询完整的描述信息

Bridge MAC of the IRF is

IRF的桥MAC

Auto upgrade

是否使能自动加载系统启动文件功能

·yes表示使能

·no表示未使能

MAC persistent

是否使能IRF桥MAC保留功能

·6 min表示IRF的桥MAC保留时间为6分钟

·always表示IRF的桥MAC永久保留不改变

·no表示立即改变IRF的桥MAC

Domain ID

IRF的域编号

当网络中存在多个IRF时，用来唯一标识一个IRF

【相关命令】

·**display irf configuration**

·**display irf topology**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf configuration**

------------------------------------------------------------------------

**[display irf configuration**]命令用来显示IRF中所有成员设备的配置信息，显示信息包括：当前成员编号、新配置的成员编号、IRF端口的物理端口。

【命令】

**[display irf configuration**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 设备工作在独立运行模式时，显示所有成员设备上重启以后生效的IRF配置。

\<Sysname\> display irf configuration

 MemberID Priority IRF-Port1                   IRF-Port2

 1        1        disable                     disable

\# 设备工作在IRF模式时，显示IRF中所有成员设备的配置信息。

\<Sysname\> display irf configuration

 MemberID  NewID    IRF-Port1                   IRF-Port2

 2         2        Ten-GigabitEthernet2/0/25   Ten-GigabitEthernet2/0/26

 5         5        Ten-GigabitEthernet5/0/25   Ten-GigabitEthernet5/0/26

                    Ten-GigabitEthernet5/0/27

                    Ten-GigabitEthernet5/0/28

 10        10       Ten-GigabitEthernet10/0/25  Ten-GigabitEthernet10/0/26

                                                Ten-GigabitEthernet10/0/27

                                                Ten-GigabitEthernet10/0/28

表1-2 display irf configuration命令显示信息描述表

字段

描述

MemberID

设备当前的成员编号

Priority

成员优先级。该字段只有设备处于独立运行模式时，才会显示

NewID

配置的成员编号，设备重启后将会生效

IRF-Port1

IRF端口1的配置

·如果显示信息中包含多个物理端口则表示该IRF端口由多个IRF物理端口聚合而成

·如果显示为disable则表示该IRF端口还没有和IRF物理端口绑定

IRF-Port2

IRF端口2的配置

·如果显示信息中包含多个物理端口则表示该IRF端口由多个IRF物理端口聚合而成

·如果显示为disable则表示该IRF端口还没有和IRF物理端口绑定

【相关命令】

·**display irf**

·**display irf topology**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf link**

------------------------------------------------------------------------

**[display irf link**]命令用来显示IRF链路信息。

【命令】

**[display irf link**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IRF链路信息。

\<Sysname\> display irf link

Member 1

 IRF Port    Interface                           Status

 1           disable                             \--

 2           Ten-GigabitEthernet1/0/1(MDC1)      UP

             Ten-GigabitEthernet1/0/2(MDC2)      ADM

             Ten-GigabitEthernet1/0/3(MDC3)      DOWN

Member 2(IRF-Link-Down: MDC2, MDC3)

 IRF Port    Interface                           Status

 1           Ten-GigabitEthernet2/0/1(MDC1)      UP

             Ten-GigabitEthernet2/0/2(MDC2)      DOWN

             Ten-GigabitEthernet2/0/3(MDC3)      ADM

 2           disable                          \--

\# 显示IRF链路信息（支持MDC但不支持IRF链路检测功能的设备）。

\<Sysname\> display irf link

Member 1

 IRF Port    Interface                          Status

 1           disable                             \--

 2           Ten-GigabitEthernet1/0/1(MDC1)      UP

             Ten-GigabitEthernet1/0/2(MDC2)      ADM

             Ten-GigabitEthernet1/0/3(MDC3)      DOWN

Member 2

 IRF Port    Interface                           Status

 1           Ten-GigabitEthernet2/0/1(MDC1)      UP

             Ten-GigabitEthernet2/0/2(MDC2)      DOWN

             Ten-GigabitEthernet2/0/3(MDC3)      ADM

 2           disable                          \--

\# 显示IRF链路信息（不支持MDC也不支持IRF链路检测功能的设备）。

\<Sysname\> display irf link

Member 1

 IRF Port    Interface                           Status

 1           disable                             \--

 2           Ten-GigabitEthernet1//0/1           UP

             Ten-GigabitEthernet1/0/2            ADM

             Ten-GigabitEthernet1/0/3            DOWN

Member 2

 IRF Port    Interface                           Status

 1           Ten-GigabitEthernet2/0/1            UP

             Ten-GigabitEthernet2/0/2            DOWN

             Ten-GigabitEthernet2/0/3            ADM

 2           disable                             \--

表1-3 display irf link命令显示信息描述表

字段

描述

Member *ID*

成员编号

(IRF-Link-Down: MDC2, MDC3)

表示IRF链路检测功能检测到该成员设备上MDC2和MDC3中的IRF链路状态为Down，于是将该成员设备上这两个MDC的业务口状态也变为down，不能转发报文（只有支持MDC且支持IRF链路检测功能的设备支持该显示信息）

IRF Port

IRF端口号，其中：

·1表示IRF端口1

·2表示IRF端口2

Interface

对应的IRF物理端口的名称和该物理接口所属的MDC，用MDC的编号表示（如果设备不支持MDC则不显示MDC信息）

·如果显示信息中包含多个物理端口则表示该IRF端口由多个IRF物理端口聚合而成

·如果显示为disable则表示该IRF端口还没有和IRF物理端口绑定

Status

IRF端口的物理接口的链路状态

·UP：链路up

·DOWN：链路down

·ADM：用户在接口下执行了**shutdown**命令

·ABSENT：接口不存在，没有插入接口模块

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf topology**

------------------------------------------------------------------------

**[display irf topology**]命令用来查看IRF的拓扑信息，显示信息包含：成员编号、IRF端口状态以及IRF端口的邻接信息。

【命令】

**[display irf topology**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IRF的拓扑信息。

\<Sysname\> display irf topology

                           Topology Info

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

               IRF-Port1                  IRF-Port2

 MemberID   Link        neighbor      Link        neighbor     Belong To

 1          DOWN        \-\--           UP          2            000f-cbb8-1a82

 2          UP          1             UP          3            000f-cbb8-1a82

 3          UP          2             DIS         \-\--          000f-cbb8-1a82

表1-4 display irf topology命令显示信息描述表

字段

描述

MemberID

成员编号

IRF-Port1

IRF-Port1的信息，包括Link和neighbor信息

IRF-Port2

IRF-Port2的信息，包括Link和neighbor信息

Link

IRF端口的链路状态，包括：

·UP：链路up

·DOWN：链路down，可能因为物理上不连通，或者没有执行**irf-port-configuration active**命令激活IRF端口

·DIS：表示该IRF端口还没有和任何IRF物理端口绑定，请使用**port group interface**命令绑定

·TIMEOUT：IRF报文超时

neighbor

与该IRF端口直连的设备的成员编号（显示为"\-\--"表示该端口没有连接其它成员设备）

Belong To

IRF中当前主设备的CPU MAC

【相关命令】

·**display irf**

·**display irf configuration**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display irf-port load-sharing mode**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display irf-port load-sharing mode**]命令用来显示IRF链路的负载分担模式。

【命令】

**[display irf-port load-sharing mode ** **irf-port**  *member-id*/*port-number*  ]

【缺省情况】

本命令的缺省情况与设备的型号有关，以设备的实际情况为准。

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[irf-port**]：显示指定IRF链路的负载分担模式。不指定该参数时，显示全局IRF链路的负载分担模式。

*[member-id*/*port-number*]：表示IRF端口编号。其中，*member-id*表示设备在IRF中的成员编号；*port-number*表示IRF端口索引，取值为1或2。不指定该参数时，显示所有连通的IRF链路的负载分担模式，如果当前没有连通的IRF链路，则显示"No IRF link exists."。

【使用指导】

需要注意的是：

·如果未指定**irf-port**参数时，则显示全局采用的IRF链路负载分担模式。

·如果仅指定**irf-port**参数而未指定IRF端口编号，则显示所有IRF端口下分别采用的负载分担模式。

·如果指定了IRF端口编号，则显示该IRF端口下采用的负载分担模式。

【举例】

\# 显示全局采用的IRF链路负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display irf-port load-sharing mode

irf-port Load-Sharing Mode:

Layer 2 traffic: destination-mac address, source-mac address

Layer 3 traffic: destination-ip address,  source-ip address

Layer 4 traffic: destination-port,        source-port

MPLS traffic   : mpls-label1,             mpls-label2,

                    mpls-label3

\# 显示IRF端口1/1下采用的负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display irf-port load-sharing mode irf-port 1/1

irf-port1/1 Load-Sharing Mode:

Layer 2 traffic: destination-mac address, source-mac address

Layer 3 traffic: destination-ip address,  source-ip address

Layer 4 traffic: destination-port,        source-port

MPLS traffic   : mpls-label1,             mpls-label2,

                    mpls-label3

\# （配置按报文目的MAC地址实现IRF端口1/1下IRF链路的负载分担模式后）显示IRF端口1/1下采用的负载分担模式。

\<Sysname\> display irf-port load-sharing mode irf 1/1

irf-port1/1 Load-Sharing Mode:

  destination-mac address

表1-5 display irf-port load-sharing mode命令显示信息描述表

字段

描述

irf-port Load-Sharing Mode

全局采用的IRF链路负载分担类型：

·缺省情况下显示：二层报文、三层报文、四层报文、MPLS报文采用的负载分担类型（各设备支持的报文类型不同，请以设备的实际情况为准）

·非缺省情况下显示：用户配置后采用的负载分担类型

irf-port1/1 Load-Sharing Mode

IRF端口1/1下采用的负载分担类型：

·缺省情况下显示：全局采用的负载分担类型

·非缺省情况下显示：用户配置后采用的负载分担类型

Layer 2 traffic: destination-mac address, source-mac address

二层报文缺省采用的负载分担类型：按照源MAC地址和目的MAC地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

Layer 3 traffic: destination-ip address,  source-ip address

三层报文缺省采用的负载分担类型：按照源IP地址和目的IP地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

Layer 4 traffic: destination-port,        source-port

四层报文缺省采用的负载分担类型：按照源端口和目的端口进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

MPLS traffic   : mpls-label1,             mpls-label2,                 mpls-label3

MPLS报文缺省采用的负载分担类型：按照第1～3层的MPLS标签进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

destination-mac address, source-mac address

用户配置后采用的负载分担类型：按照源MAC地址和目的MAC地址进行负载分担（此字段的显示内容与用户的配置相关）

**IRF \-- IRF2配置命令（集中式IRF设备） \-- display mad**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display mad**]命令用来显示MAD配置信息。

【命令】

**[display mad ** **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[verbose**]：显示MAD详细配置信息。如果不使用该参数，则显示简要配置信息。

【举例】

\# 显示MAD简要配置信息。

\<Sysname\> display mad

MAD ARP enabled.

MAD ND enabled.

MAD LACP disabled.

MAD BFD enabled.

\# 显示MAD详细配置信息。

\<Sysname\> display mad verbose

Current MAD status: Detect

Excluded ports(configurable):

Excluded ports(can not be configured):

MAD ARP enabled interface:

  Vlan-interface3

MAD ND enabled interface:

  Vlan-interface3

MAD LACP disabled.

MAD BFD enabled interface:

  Vlan-interface100

    mad ip address 223.255.255.202 255.255.255.0 member 2

    mad ip address 223.255.255.205 255.255.255.0 member 5

表1-6 display mad命令显示信息描述表

字段

描述

MAD LACP enabled.

是否使能LACP MAD检测功能

·enabled表示已经使能

·disabled表示没有使能

MAD ARP enabled.

是否使能ARP MAD检测功能

·enabled表示已经使能

·disabled表示没有使能

MAD ND enabled.

是否使能ND MAD检测功能

·enabled表示已经使能

·disabled表示没有使能

Current MAD status

MAD当前的状态，包括：

·Detect：检测状态，即IRF处于正常状态

·Recovery：发生多Active冲突时，失败的一方进入Recovery状态，该状态下设备会自动关闭所有非保留的业务接口

·Detect to Recovery：从检测状态迁移到Recovery状态过程的中间状态

·Recovery to Detect：从Recovery状态迁移到检测状态过程的中间状态

Excluded ports(configurable)

用户配置的保留接口

Excluded ports(can not be configured)

系统默认保留的接口（不需要用户配置，自动保留）

MAD ARP enabled interface:

  Vlan-interface2

使能了ARP MAD的接口

MAD ND enabled  interface:

  Vlan-interface2

使能了ND MAD的接口

MAD LACP disabled

LACP MAD没有使能

**IRF \-- IRF2配置命令（集中式IRF设备） \-- easy-irf**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

只在IRF模式下支持该命令。

**[easy-irf**]命令用于快速配置堆叠环境。

【命令】

**[easy-irf** [ **member** *member-id* [ **renumber** *new-member-id*  **domain** *domain-id*  **priority** *priority*   **irf-port1** *interface-list1*   **irf-port2** *interface-list2*  ]]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[member** *member-id*]：表示设备当前的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[renumber** *new-member-id*]：表示新成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。不指定该参数时，表示不修改成员编号。

**[domain** *domain-id*]：表示设备所属的IRF域编号，取值范围为0～4294967295。同一IRF中成员设备域编号应配置为相同值。

**[priority** *priority*]：表示IRF成员的优先级，取值范围为1～32。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。

**[irf-port1** *interface-list1*]：表示和IRF端口1绑定的IRF物理端口。表示方式为*interface-list1* = { *interface-type interface-number* }&\<1-n\>。其中*interface-type interface-number*表示接口类型和接口编号。&\<1-n\>表示前面的参数最多可以输入n次。n的取值与设备的型号有关，请以设备的实际情况为准。

**[irf-port2 ***interface-list2*]：表示和IRF端口2绑定的IRF物理端口。表示方式为*interface-list2* = { *interface-type interface-number* }&\<1-n\>。其中*interface-type interface-number*表示接口类型和接口编号。&\<1-n\>表示前面的参数最多可以输入n次。n的取值与设备的型号有关，请以设备的实际情况为准。同一物理端口只能一个IRF端口绑定。

【使用指导】

使用该功能，用户可以通过一条命令配置IRF的基本参数，包括新成员编号、域编号、绑定物理端口，简化了配置步骤，达到快速配置IRF的效果。

在配置该功能时，有两种方式：

·交互模式：用户输入**easy-irf**，回车，在交互过程中输入具体参数的值。

·非交互模式，在输入命令行时直接指定所需参数的值。

两种方式的配置效果相同，如果用户对本功能不熟悉，建议使用交互模式。

配置时，需要注意的是：

·如果给成员设备指定新的成员编号，该成员设备会立即自动重启，以使新的成员编号生效。

·多次使用该功能，修改域编号/优先级/IRF物理端口时，域编号和优先级的新配置覆盖旧配置，IRF物理端口的配置会新旧进行叠加。如需删除旧的IRF物理端口配置，需要在IRF端口视图下，执行**undo port group interface**命令。一个IRF端口最多可绑定多少个IRF物理端口与设备的型号有关，请以设备的实际情况为准。

·在交互模式下，为IRF端口指定物理端口时，请注意：

¡接口类型和接口编号间不能有空格。

¡不同物理接口之间用英文逗号分隔，逗号前后不能有空格。

¡有些接口板出厂时已将接口分组，如果要将该组内的某接口和IRF端口绑定，需要将该组的所有接口都和IRF端口绑定。

【举例】

\# 通过非交互模式配置成员设备2的新成员编号为3，域编号为10，优先级为10，IRF端口1和Ten-GigabitEthernet2/0/21、Ten-GigabitEthernet2/0/22、Ten-GigabitEthernet2/0/23和Ten-GigabitEthernet2/0/24绑定。

\<Sysname\> system-view

Sysname easy-irf member 1 renumber 2 domain 10 priority 10 irf-port1 ten-gigabitethernet 2/0/21 ten-gigabitethernet 2/0/22 ten-gigabitethernet 2/0/23 ten-gigabitethernet 2/0/24

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

                  Configuration summary for member 2

IRF new member ID: 3

IRF domain ID    : 10

IRF priority     : 10

IRF-port 1       : Ten-GigabitEthernet2/0/21, Ten-GigabitEthernet2/0/22

                   Ten-GigabitEthernet2/0/23, Ten-GigabitEthernet2/0/24

IRF-port 2       : Disabled

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Are you sure to use these settings to set up IRF? [Y/N y]

Starting to configure IRF\...

Configuration succeeded.

The device will reboot for the new member ID to take effect. Continue? [Y/N y]

\# 通过交互模式配置成员设备3的新编号为5，域编号为10，优先级为10，IRF端口1和Ten-GigabitEthernet3/0/21、Ten-GigabitEthernet3/0/22、Ten-GigabitEthernet3/0/23和Ten-GigabitEthernet3/0/24绑定。

\<Sysname\> system-view

Sysname easy-irf

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  

Welcome to use easy IRF.                                                       

To skip the current step, enter a dot sign (.).                                

To return to the previous step, enter a minus sign (-).                        

To use the default value (enclosed in [) for each parameter, press Enter withou]

t entering a value.                                                            

To quit the setup procedure, press CTRL+C.                                     

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  

Select a member by its ID \<3\> [3:3                                             ]

Specify a new member ID \<1\~10\> [1: 5                                           ]

Specify a domain ID \<0\~4294967295\> [0: 10                                      ]

Specify a priority \<1\~32\> [1: 10                                               ]

Specify IRF-port 1 bindings (a physical interface or a comma-separated physical

interface list)[Disabled: ten-gigabitethernet3/0/21,ten-gigabitethernet3/0/22,ten-gigabitethernet3/0/23,ten-gigabitethernet3/0/24]

Specify IRF-port 2 bindings (a physical interface or a comma-separated physical

interface list)[Disabled:                                                      ]

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  

                  Configuration summary for member 3                           

IRF new member ID: 5                                                           

IRF domain ID    : 10                                                          

IRF priority     : 10                                                          

IRF-port 1       : Ten-GigabitEthernet3/0/21, Ten-GigabitEthernet3/0/22        

                   Ten-GigabitEthernet3/0/23, Ten-GigabitEthernet3/0/24        

IRF-port 2       : Disabled                                                    

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  

Are you sure to use these settings to set up IRF? [Y/N y                       ]

Starting to configure IRF\...

Configuration succeeded.                                                       

The device will reboot for the new member ID to take effect. Continue? Y/N y

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf auto-merge enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image003.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

****

**[irf auto-merge enable**]命令用来使能IRF合并自动重启功能。

**[undo irf auto-merge enable**]命令用来关闭IRF合并自动重启功能。

【命令】

**[irf auto-merge enable**]

**[undo irf auto-merge enable**]

【缺省情况】

IRF合并自动重启功能处于使能状态。即两台IRF合并时，竞选失败方会自动重启。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

IRF合并时，两台IRF会遵照角色选举的规则进行竞选，竞选失败方IRF的所有成员设备需要重启才能加入获胜方IRF。其中：

·如果没有使能IRF合并自动重启功能，则合并过程中的重启需要用户根据系统提示手工完成。

·如果使能IRF合并自动重启功能，则合并过程中的重启由系统自动完成。

需要注意的是：

·当IRF模式下，IRF端口状态为DOWN或DIS时，配置IRF物理端口和IRF端口绑定，引起IRF端口状态变为UP，从而触发IRF合并，此时，即便使能了IRF合并自动重启功能，该功能也暂时不生效，系统会提示用户必须手工重启竞选失败方才能完成合并。此时，请使用**save**命令将当前配置（尤其是IRF端口的配置）保存到下次启动配置文件后，再重启失败方。否则，失败方重启后，会因为没有IRF配置信息而不能合并。

·其它情况下触发的IRF合并（比如IRF连接故障恢复后引起的合并；两台IRF的启动配置文件中已经绑定了IRF物理端口和IRF端口，然后建立IRF物理连接引起IRF端口状态变为UP，触发的IRF合并等），如果合并时已使能了IRF合并自动重启功能，则竞选失败方会自动重启加入获胜方，合并为一个IRF。

·要使IRF合并自动重启功能正常运行，请在即将合并的两台IRF上都使能IRF合并自动重启功能。

·本命令只在IRF模式下支持。配置**irf auto-merge enable**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

【举例】

\# 使能IRF合并自动重启功能。

\<Sysname\> system-view

Sysname irf auto-merge enable

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf auto-update enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

****

**[irf auto-update enable**]命令用来使能启动文件自动加载功能。

**[undo irf auto-update enable**]命令用来关闭启动文件自动加载功能。

【命令】

**[irf auto-update enable**]

**[undo irf auto-update enable**]

【缺省情况】

IRF系统启动文件的自动加载功能处于使能状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能启动文件自动加载功能后，当新加入IRF的设备和主设备的软件版本不同时，新加入的设备会自动同步主设备的软件版本，再重新加入IRF。

需要注意的是，为了能够自动加载成功，请确保从设备存储介质上有足够的空闲空间用于存放新的启动文件。如果从设备存储介质上空闲空间不足，系统会自动删除从设备的当前启动文件来完成加载。如果删除从设备的当前启动文件后空间仍然不足，从设备将无法进行自动加载。此时，需要管理员重启从设备并进入从设备的Boot ROM菜单，删除一些不重要的文件后，再让从设备重新加入IRF。

【举例】

\# 使能启动文件自动加载功能。

\<Sysname\> system-view

Sysname irf auto-update enable

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf domain**

------------------------------------------------------------------------

**[irf domain**]命令用来配置IRF域编号。

**[undo irf domain**]命令用来恢复缺省情况。

【命令】

**[irf domain ***domain-id*]

**[undo irf domain**]

【缺省情况】

IRF的域编号为0。

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-id*]：IRF的域编号，取值范围为0～4294967295。

【使用指导】

为了适应各种组网应用，同一个网络里可以部署多个IRF。IRF之间使用不同的域编号以示区别。

在LACP MAD和ARP MAD检测组网中，如果中间设备本身也是一个IRF系统，则必须配置该命令确保本IRF和中间设备组成的IRF的域编号不同，否则可能造成检测异常，甚至导致业务中断。

IRF域编号是一个全局变量，IRF中的所有成员设备、所有MDC都共用这个IRF域编号。缺省MDC上通过**irf domain**命令，或者在任意MDC上通过**mad enable**、**mad arp enable**、**mad nd enable**命令均可修改全局IRF域编号。因此，请按照网络规划来修改IRF域编号，不要随意修改。

【举例】

\# 配置IRF的域编号为10。

\<Sysname\> system-view

Sysname irf domain 10

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf link-delay**

------------------------------------------------------------------------

**[irf link-delay**]命令用来配置IRF链路down延迟上报时间。

**[undo irf link-delay**]命令用来恢复缺省情况。

【命令】

**[irf link-delay ***interval*]

**[undo irf link-delay**]

【缺省情况】

不同型号的设备支持的缺省情况不同，以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示延迟上报IRF链路down的时间间隔，取值范围为0～10000，单位为毫秒。取值为0时，表示不延迟。

【使用指导】

在IRF环境中使用CFD、BFD功能时，请保证IRF链路down延迟上报时间小于CFD、BFD的超时时间，关于CFD、BFD功能的介绍，请参见"可靠性配置指导"中的"CFD" 、"BFD"。

【举例】

\# 配置IRF链路down延迟上报时间为300毫秒。

\<Sysname\> system-view

Sysname irf link-delay 300

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf isolate member**

------------------------------------------------------------------------

![说明](IRF命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[irf isolate member**]命令用来隔离某成员设备，即丢弃指定成员设备发送的所有报文。

**[undo irf isolate member**]命令用来取消隔离。

【命令】

**[irf isolate member** *member-id*]

**[undo irf isolate member** *member-id*]

【缺省情况】

不隔离任何成员设备。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当使用**display interface**命令查看到物理IRF接口的CRC错误报文较多，或者IRF中出现网络风暴时，可多次使用**irf isolate member**命令，将所有空闲的成员编号都隔离，再进行修复。成员设备被隔离后，其它成员设备收到该成员设备发送的报文时，会直接丢弃。如果后续需要扩充IRF，需先执行**undo**命令取消隔离。

【举例】

\# 隔离成员设备3。

\<Sysname\> system-view

Sysname irf isolate member 3

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf mac-address persistent**

------------------------------------------------------------------------

**[irf mac-address persistent**]命令用来配置IRF的桥MAC的保留时间。

**[undo irf mac-address persistent**]命令用来配置IRF的桥MAC不保留，立即变化。

【命令】

**[irf mac-address persistent **[{ **timer** \| **always** }]]

**[undo irf mac-address persistent**]

【缺省情况】

IRF的桥MAC会保留6分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[timer**]：用来配置IRF的桥MAC保留时间为6分钟。

**[always**]：用来配置IRF的桥MAC永久保留不改变。

【使用指导】

如果配置了桥MAC保留时间为6分钟，则当主设备离开IRF时，IRF桥MAC在6分钟内不变化。如果主设备在6分钟内重新又加入IRF，则IRF桥MAC不会变化。如果6分钟后主设备没有回到IRF，则会使用新选举的主设备的桥MAC作为IRF桥MAC。

·如果配置了MAC地址永久保留，则不管主设备是否离开IRF，IRF桥MAC始终保持不变。

·如果配置了MAC地址不保留，立即变化，当主设备离开IRF时，系统立即会使用新选举的主设备的桥MAC做IRF桥MAC。

需要注意的是：

·如果两个IRF的桥MAC相同，则它们不能合并为一个IRF。

·当使用ARP MAD和MSTP组网时，需要将IRF配置为MAC地址立即改变，即配置**undo irf mac-address persistent**命令。

·如果在IRF中启用了TRILL协议，则强烈建议用户配置IRF桥MAC地址保留时间为永久保留，否则，可能会导致一系列问题。

【举例】

\# 配置IRF的桥MAC永久保留。

\<Sysname\> system-view

Sysname irf mac-address persistent always

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf member**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[irf member**]命令用来在独立运行模式下配置设备的成员编号。

**[undo irf member**]命令用来恢复缺省情况。

【命令】

**[irf member** *member-id*]

**[undo irf member**]

【缺省情况】

设备处于独立运行状态时，成员编号为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*]：表示设备在IRF中的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

成员编号有以下作用：

·设备从独立运行模式切换到IRF模式时，需要使用成员编号进行配置文件的自动转换。建议在独立运行模式下规划和修改设备的成员编号，以免成员编号冲突，设备切换到IRF模式后，不能加入已有的IRF。

·IRF系统使用成员编号来唯一标识一台成员设备。如果在独立运行模式下，请使用**irf member**命令来配置，这种方式下配置的成员编号在设备切换到IRF模式后生效；如果在IRF模式下，请使用**irf member ***member-id*** renumber ***new-member-id*命令来配置，这种方式下配置的成员编号需要重启设备才能生效。

【举例】

\# 在独立运行模式下配置设备的成员编号为2。

\<Sysname\> system-view

sysname irf member 2.

【相关命令】

·**irf member renumber**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf member description**

------------------------------------------------------------------------

**[irf member description**]命令用来配置IRF中指定成员设备的描述信息。

**[undo irf member description**]命令用来恢复缺省情况。

【命令】

**[irf member*** member-id ***description*** text*]

**[undo irf member** *member-id* **description**]

【缺省情况】

成员设备没有描述信息。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*]：表示设备在IRF中的成员编号。

*[text*]：设备的描述信息，为1～127个字符的字符串。

【使用指导】

当网络中存在多个IRF或者同一IRF中存在多台成员设备且物理位置比较分散（比如在不同楼层甚至不同建筑）时，为了确认成员设备的物理位置，在组建IRF时可以将物理位置设置为成员设备的描述信息，以便后期维护。

【举例】

\# 配置成员设备1的描述信息为F1Num001。

\<Sysname\> system-view

Sysname irf member 1 description F1Num001

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf member priority**

------------------------------------------------------------------------

**[irf member priority**]命令用来配置IRF中指定成员设备的优先级。

**[undo irf member priority**]命令用来恢复缺省情况。

【命令】

**[irf member** *member-id* **priority** *priority*]

**[undo irf member*** member-id* **priority**]

【缺省情况】

设备的成员优先级均为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*]**：**表示设备在IRF中的成员编号。

*[priority*]**：**表示优先级，取值范围为1～32。

【使用指导】

优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。

【举例】

\# 配置IRF中ID为2的设备的优先级为32。

\<Sysname\> system-view

Sysname irf member 2 priority 32

【相关命令】

·**irf priority**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf member renumber**

------------------------------------------------------------------------

**[irf member renumber**]命令用来配置设备的成员编号。

**[undo irf member renumber**]命令用来取消成员编号的设置。

【命令】

**[irf member ***member-id* **renumber** *new-member-id*]

**[undo irf member** *member-id* **renumber**]

【缺省情况】

设备切换到IRF模式后，使用的是独立运行模式下预配置的成员编号。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*]：表示设备在IRF中的成员编号。

*[new-member-id*]：表示修改后的成员编号。

【使用指导】

设备处于独立运行状态时，成员编号为1；切换到IRF模式后，使用的是独立运行模式下预配置的成员编号；如果模式切换前没有配置成员编号，则系统会自动使用1作为成员编号。

当新加入的设备的编号和IRF中已有成员设备的编号相同时，设备不能加入IRF。此时，请使用该命令修改设备的成员编号后，重新加入IRF。

·该配置需要重启*member-id*标志的设备才能生效；

·在IRF中以设备编号标志设备，配置IRF端口和优先级也是根据设备编号来配置的，所以，修改设备成员编号可能导致设备配置发生变化或者丢失，请慎重处理。

【举例】

\# 将成员设备1的成员编号修改为3。

\<Sysname\> diplay irf

Sysname irf member 1 renumber 3

Renumbering the member ID may result in configuration change or loss. Continue?[Y/NY]

【相关命令】

·**irf member**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf priority**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[irf priority**]命令用来在独立运行模式下配置设备的成员优先级。

**[undo irf priority**]命令用来恢复缺省情况。

【命令】

**[irf priority** *priority*]

**[undo irf priority**]

【缺省情况】

设备的成员优先级为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：表示优先级，取值范围为1～32。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。

【使用指导】

成员优先级有两种配置方式：

·在独立运行模式下，使用**irf priority**命令来配置。如果在IRF形成过程中，想让某台设备当选为主设备，请使用这种方式配置。

·在IRF模式下，使用**irf member ***member-id*** priority ***priority*命令来配置，这种方式下配置的成员优先级会影响IRF运行过程中的角色选举过程。比如当前主设备离开IRF时，优先级高的成员设备会当选为新的主设备；当发生IRF合并的时候，主设备成员优先级高的IRF会竞选成功。

【举例】

\# 在独立运行模式下将本设备的成员优先级设置为32。

\<Sysname\> system-view

sysname irf priority 32

【相关命令】

·**irf member priority**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port**

------------------------------------------------------------------------

**[irf-port**]命令用来创建IRF端口并进入IRF端口视图，如果IRF端口已经创建，则直接进入IRF端口视图。

**[undo irf-port**]用来删除IRF端口。

【命令】

·**irf-port ***member-id/port-number*

·**undo irf-port*** member-id/port-number*

【缺省情况】

设备上没有创建IRF端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*/*port-number*]：表示IRF端口编号。其中，*member-id*表示设备在IRF中的成员编号；*port-number*表示IRF端口索引，取值为1时表示IRF-port1，为2时表示IRF-port2。

【使用指导】

在组建IRF前，必须进入IRF端口视图，并绑定IRF物理端口才能使能该IRF端口，从而进行IRF连接。

【举例】

\# 为成员编号为3的设备创建IRF端口1，并将其与Ten-GigabitEthernet3/0/1绑定。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 3/0/1

Sysname-Ten-GigabitEthernet3/0/1 shutdown

Sysname-Ten-GigabitEthernet3/0/1 quit

Sysname irf-port 3/1

Sysname-irf-port3/1 port group interface ten-gigabitethernet 3/0/1

Sysname-irf-port3/1 quit

Sysname interface ten-gigabitethernet 3/0/1

Sysname-Ten-GigabitEthernet3/0/1 undo shutdown

【相关命令】

·**port group interface**

·**irf-port*** port-number*

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port global load-sharing mode**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[irf-port global load-sharing mode**]命令用来配置全局IRF链路的负载分担模式。

**[undo irf-port global load-sharing** **mode**]命令用来恢复缺省情况。

【命令】

**[irf-port global load-sharing mode**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-port** \| **source-ip** \| **source-mac** \| **vlan-id** } \* \| **flexible** }]]

**[undo irf-port global load-sharing mode**]

【缺省情况】

本命令的缺省情况则与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination-ip**]：表示按报文的目的IP地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[destination-mac**]：表示按报文的目的MAC地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[destination-port**]：表示按报文的目的端口号进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ingress-port**]：表示按报文的入端口号进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip-protocol**]：表示按报文的IP协议类型进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label1**]：表示按MPLS报文第一层（最外层）标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label2**]：表示按MPLS报文第二层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label3**]：表示按MPLS报文第三层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-port**]：表示按报文的源端口号进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-ip**]：表示按报文的源IP地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-mac**]：表示按报文的源MAC地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan-id**]：表示按报文所属的VLAN进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flexible**]：表示系统自动根据报文的类型（L2、IPv4、IPv6、MPLS等）去匹配缺省负载分担模式，来灵活实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以通过全局配置（系统视图下）和端口下（IRF端口视图下）的配置方式设置IRF链路的负载分担模式：

·在系统视图的配置对所有IRF链路生效；

·在IRF端口视图下的配置只对当前IRF端口下的IRF链路生效；

·IRF链路会优先采用端口下的配置。如果端口下没有配置，则采用全局配置。

需要注意的是：

·在同一视图下多次配置该命令，以最新的配置为准。

·对于设备不支持的负载分担模式，系统将提示用户不支持。

【举例】

\# 配置全局按照报文目的MAC地址进行负载分担。

\<Sysname\> system-view

Sysname irf-port global load-sharing mode destination-mac

【相关命令】

·**irf-port load-sharing mode**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port load-sharing mode**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[irf-port load-sharing mode**]命令用来配置端口下IRF链路的负载分担模式。

**[undo irf-port load-sharing** **mode**]命令用来恢复缺省情况。

【命令】

**[irf-port load-sharing mode**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-port** \| **source-ip** \| **source-mac** \| **vlan-id** } \* \| **flexible** }]]

**[undo irf-port load-sharing mode**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

IRF端口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination-ip**]：表示按报文的目的IP地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[destination-mac**]：表示按报文的目的MAC地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[destination-port**]：设置按报文的目的端口号实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ingress-port**]：设置按报文的入端口实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip-protocol**]：表示按报文的IP协议类型进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label1**]：表示按MPLS报文第一层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label2**]：表示按MPLS报文第二层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label3**]：表示按MPLS报文第三层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-port**]：设置按报文的源端口号实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-ip**]：表示按报文的源IP地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-mac**]：表示按报文的源MAC地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan-id**]：表示按报文所属的VLAN进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flexible**]：表示系统自动根据报文的类型（L2、IPv4、IPv6、MPLS等）去匹配缺省负载分担模式，来灵活实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以通过全局配置（系统视图下）和端口下（IRF端口视图下）的配置方式设置IRF链路的负载分担模式：

·在系统视图的配置对所有IRF链路生效；

·在IRF端口视图下的配置只对当前IRF端口下的IRF链路生效；

·IRF链路会优先采用端口下的配置。如果端口下没有配置，则采用全局配置。

需要注意的是：

·在配置负载分担模式前，请先将IRF端口和IRF物理端口绑定。否则，负载分担模式将配置失败。

·在同一视图下多次配置该命令，以最新的配置为准。

·对于设备不支持的负载分担模式，系统将提示用户不支持。

【举例】

\# 配置按报文目的MAC地址实现IRF端口1/1下IRF链路的负载分担模式。

\<Sysname\> system-view

Sysname irf-port 1/1

Sysname-irf-port1/1 irf-port load-sharing mode destination-mac

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port port-number**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[irf-port*** port-number*]命令用来在独立运行模式下创建IRF端口并进入IRF端口视图（如果该IRF端口已经创建，则直接进入该IRF端口视图）。

**[undo** **irf-port** *port-number*]用来删除指定IRF端口。

【命令】

**[irf-port ***port-number*]

**[undo irf-port ***port-number*]

【缺省情况】

设备上没有创建IRF端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：表示IRF端口编号，取值为1或2。

【举例】

\# 在处于独立运行模式下创建IRF端口1。

\<Sysname\> system-view

Sysname irf-port 1

Sysname-irf-port1

【相关命令】

·**port group interface**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- irf-port-configuration active**

------------------------------------------------------------------------

**[irf-port-configuration active**]命令用于来激活设备上所有IRF端口下的配置。

【命令】

**[irf-port-configuration active**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

IRF物理线缆连接好，并将IRF物理端口添加到IRF端口后，必须通过该命令手工激活IRF端口的配置才能形成IRF。

系统启动，通过配置文件将IRF物理端口加入IRF端口，或者IRF形成后再加入新的IRF物理端口时，IRF端口下的配置会自动激活不再需要使用该命令来激活。

【举例】

\# 激活IRF端口。

·配置IRF端口1/2，将它和IRF物理端口Ten-GigabitEthernet1/0/1绑定。

\<Sysname\> system-view

Sysname interface ten-gigabitEthernet 1/0/1

Sysname-Ten-GigabitEthernet1/0/1 shutdown

Sysname-Ten-GigabitEthernet1/0/1 quit

Sysname irf-port 1/2

Sysname-irf-port1/2 port group interface Ten-GigabitEthernet 1/0/1

 Info : You are recommended to save the configuration now; otherwise, it will be lost after system reboot.

Sysname-irf-port1/2 quit

Sysname interface ten-gigabitEthernet 1/0/1

Sysname-Ten-GigabitEthernet1/0/1 undo shutdown

Sysname-Ten-GigabitEthernet1/0/1 quit

·将当前配置保存到下次启动配置文件，以便IRF端口的配置在设备重启后能继续生效。

Sysname save

The current configuration will be written to the device. Are you sure? [Y/N:y]

Please input the file name(\*.cfg)[flash:/startup.cfg]

(To leave the existing filename unchanged, press the enter key):

flash:/aa.cfg exists, overwrite? [Y/N:y]

 Validating file. Please wait\...\...\...\...\...\...\...\...\....

 Saved the current configuration to mainboard device successfully.

Slot 1:

 Save next configuration file successfully.

 Configuration is saved to device successfully.

·激活IRF端口的配置。

Sysname irf-port-configuration active

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad arp enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mad arp enable**]命令用来使能ARP MAD检测功能。

**[undo mad arp enable**]用来关闭ARP MAD检测功能。

【命令】

**[mad arp enable**]

**[undo mad arp enable**]

【缺省情况】

ARP MAD检测功能处于关闭状态。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了防止IRF级联组网时，本IRF的MAD检测报文转发到邻居IRF中影响邻居IRF的MAD检测，执行**mad arp enable**命令时，系统会要求用户输入IRF域编号。IRF域编号是一个全局变量，IRF中的所有成员设备、所有MDC都共用这个IRF域编号。缺省MDC上通过**irf domain**命令，或者在任意MDC上通过**mad enable**、**mad arp enable**、**mad nd enable**命令均可修改全局IRF域编号。因此，请按照网络规划来修改IRF域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。

VLAN 1不能用于MAD检测，因此，不能在VLAN接口1下使能ARP MAD检测功能。

BFD MAD、ARP MAD、ND MAD这三种检测方式独立工作，可以同时配置，但不能和LACP MAD方式同时配置。

【举例】

\# 在VLAN接口3上启用ARP MAD检测功能。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-Vlan-interface3 mad arp enable

You need to assign a domain ID (range: 0-4294967295)

Current domain is: 0: 1

The assigned  domain ID is: 1

【相关命令】

·**irf domain**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad bfd enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mad bfd enable**]命令用来使能BFD MAD检测功能。

**[undo mad bfd enable**]用来关闭BFD MAD检测功能。

【命令】

**[mad bfd enable**]

**[undo mad bfd enable**]

【缺省情况】

BFD MAD检测功能处于关闭状态。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·VLAN 1不能用于MAD检测，因此，不能在VLAN接口1下使能BFD MAD检测功能。

·BFD MAD、ARP MAD、ND MAD这三种检测方式独立工作，可以同时配置，但不能和LACP MAD方式同时配置。

·使能BFD检测功能的三层接口只能专用于BFD检测，不允许运行其它业务。如果用户配置了其它业务，可能会影响该业务以及BFD检测功能的运行。

·BFD MAD检测功能与VPN功能互斥，请不要将使能了BFD MAD检测功能的三层接口与VPN实例进行绑定。

·BFD MAD检测功能与生成树功能互斥，在使能了BFD MAD检测功能的三层接口对应VLAN内的端口上，请不要使能生成树协议。

【举例】

\# 在VLAN接口3上启用BFD MAD检测功能。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-Vlan-interface3 mad bfd enable

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mad enable**]命令用来使能LACP MAD方式检测功能。

**[undo mad enable**]用来关闭LACP MAD方式检测功能。

【命令】

**[mad enable**]

**[undo mad enable**]

【缺省情况】

LACP MAD检测功能处于关闭状态。

【视图】

聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

请在动态聚合接口下使能LACP MAD方式检测功能。聚合接口创建后，可使用**link-aggregation mode dynamic**命令将该接口配置为动态接口。

为了防止IRF级联组网时，本IRF的MAD检测报文转发到邻居IRF中影响邻居IRF的MAD检测，执行**mad enable**命令时，系统会要求用户输入IRF域编号。IRF域编号是一个全局变量，IRF中的所有成员设备、所有MDC都共用这个IRF域编号。缺省MDC上通过**irf domain**命令，或者在任意MDC上通过**mad enable**、**mad arp enable**、**mad nd enable**命令均可修改全局IRF域编号。因此，请按照网络规划来修改IRF域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。

需要注意的是，BFD MAD、ARP MAD、ND MAD这三种检测方式独立工作，可以同时配置，但不能和LACP MAD方式同时配置。

【举例】

\# 在二层动态聚合接口1下启用LACP MAD方式检测功能。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 link-aggregation mode dynamic

Sysname-Bridge-Aggregation1 mad enable

 You need to assign a domain ID (range: 0-4294967295)

 Current domain is: 0: 1

 The assigned  domain ID is: 1

MAD LACP only enable on dynamic aggregation interface.

\# 在三层动态聚合接口1下启用LACP MAD方式检测功能。

\<Sysname\> system-view

Sysname interface route-aggregation 1

Sysname-Route-Aggregation1 link-aggregation mode dynamic

Sysname-Bridge-Aggregation1 mad enable

 You need to assign a domain ID (range: 0-4294967295)

 Current domain is: 0: 1

 The assigned  domain ID is: 1

MAD LACP only enable on dynamic aggregation interface.

【相关命令】

·**irf domain**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad exclude interface**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mad exclude interface**]命令用来配置保留接口，当设备进入Recovery状态时，该接口不会被关闭。

**[undo mad exclude interface**]命令用来恢复缺省情况。

【命令】

**[mad exclude interface*** interface-type interface-number*]

**[undo mad exclude interface*** interface-type interface-number*]

【缺省情况】

IRF物理端口是保留接口，设备进入Recovery状态时会自动关闭本设备上所有的业务接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：表示接口类型和接口编号。

【使用指导】

IRF电缆断开后，网络中会存在多台全局配置完全相同的设备，这些设备连接到网络时可能会引起网络故障。为了防止这种情况发生，系统会进行多Active检测，最终只保留一台Active设备，其它设备都进入Recovery状态，并且关闭Recovery状态设备上的所有业务接口。使用该命令可以让指定的端口不被关闭，具体哪些接口需要保留由用户决定。建议除了Telnet登录接口以及用于多Active检测的接口外，其他接口均关闭。

当分裂的IRF恢复时，处于Recovery状态的设备重启后重新加入IRF，关闭的接口会自动恢复。也可以通过命令行**mad restore**对处于Recovery状态的设备进行恢复，关闭的接口也会恢复正常。

【举例】

\# 配置GigabitEthernet1/0/1为保留接口，即当设备进入Recovery状态时，该接口不会被关闭。

\<Sysname\> system-view

Sysname mad exclude interface gigabitethernet 1/0/1

【相关命令】

·**mad restore**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad ip address**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mad ip address**]命令用来给指定成员设备配置MAD IP地址。

**[undo mad ip address**]命令用来删除相应的MAD IP地址。

【命令】

**[mad ip address*** ip-address *[{ *mask* \| *mask-length* } **member** *member-id*]]

**[undo mad ip address*** ip-address *[{ *mask* \| *mask-length* } **member** *member-id*]]

【缺省情况】

没有为接口配置MAD IP地址。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：接口的IP地址，为点分十进制格式。

*[mask*]：接口IP地址相应的子网掩码，为点分十进制格式。

*[mask-length*]：子网掩码长度，即掩码中连续"1"的个数，取值范围为0～32。

**[member ***member-id*]：表示成员在IRF中的成员编号。

【使用指导】

当使用BFD MAD检测时，IRF中的所有成员设备都需要配置MAD IP地址，这些IP地址与成员编号绑定，且必须为同一网段。但只有主设备的MAD IP地址生效，从设备的MAD IP地址不生效。当IRF链路分裂时，IRF中的原从设备变为主设备，配置的MAD IP地址生效，BFD会话被激活，设备将认为在网络中检测到存在配置冲突的IRF。

需要注意的是，在用于BFD MAD检测的接口下必须使用本命令配置MAD IP地址，而不要配置其它IP地址（包括使用**ip addres**s命令配置的普通IP地址、VRRP虚拟IP地址等），以免影响MAD检测功能。

【举例】

\# 配置VLAN接口3在成员设备1上的MAD IP地址。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-Vlan-interface3 mad ip address 192.168.0.1 255.255.255.0 member 1

配置VLAN接口3在成员设备2上的MAD IP地址。

Sysname-Vlan-interface3 mad ip address 192.168.0.2 255.255.255.0 member 2

【相关命令】

·**mad bfd enable**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad nd enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mad nd enable**]命令用来使能ND MAD检测功能。

**[undo mad nd enable**]用来关闭ND MAD检测功能。

【命令】

**[mad nd enable**]

**[undo mad nd enable**]

【缺省情况】

ND MAD检测功能处于关闭状态。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了防止IRF级联组网时，本IRF的MAD检测报文转发到邻居IRF中影响邻居IRF的MAD检测，执行**mad nd enable**命令时，系统会要求用户输入IRF域编号。IRF域编号是一个全局变量，IRF中的所有成员设备、所有MDC都共用这个IRF域编号。缺省MDC上通过**irf domain**命令，或者在任意MDC上通过**mad enable**、**mad arp enable**、**mad nd enable**命令均可修改全局IRF域编号。因此，请按照网络规划来修改IRF域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。

VLAN 1不能用于MAD检测，因此，不能在VLAN接口1下使能ND MAD检测功能。

BFD MAD、ARP MAD、ND MAD这三种检测方式独立工作，可以同时配置，但不能和LACP MAD方式同时配置。

【举例】

\# 在VLAN接口3上启用ND MAD检测功能。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-Vlan-interface3 mad nd enable

 You need to assign a domain ID (range: 0-4294967295)

 Current domain is: 0: 1

 The assigned  domain ID is: 1

【相关命令】

·**irf domain**

**IRF \-- IRF2配置命令（集中式IRF设备） \-- mad restore**

------------------------------------------------------------------------

![说明](IRF命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mad restore**]命令用来将设备从Recovery状态恢复到正常状态。

【命令】

**[mad restore**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当IRF链路故障会导致多Active冲突，原IRF分裂为多个IRF，为了防止网络中配置冲突，IRF系统会通过多Active检测机制，让其中一个IRF继续正常工作，其它IRF的状态修改为Recovery（处于该状态的IRF不能处理业务报文）。如果继续正常工作的IRF也发生故障不能工作，此时可以通过本命令将处于Recovery状态的IRF恢复到正常工作状态接替原IRF工作，以便保证业务尽量少受影响。

【举例】

\# 将IRF从Recovery状态恢复到正常状态。

\<Sysname\> system-view

Sysname mad restore

   This command will restore the device from multi-active conflict state. Continue? [Y/N:Y]

Restoring from multi-active conflict state, please wait\...

**IRF \-- IRF2配置命令（集中式IRF设备） \-- port group interface**

------------------------------------------------------------------------

**[port group interface**]命令用来绑定设备的IRF端口和IRF物理端口，在IRF端口上第一次绑定IRF物理端口的同时相当于开启了IRF端口的IRF功能。

**[undo port group interface**]命令用来取消设备的IRF端口和IRF物理端口的绑定关系。

【命令】

**[port group interface**[ *interface-type interface-number* [ **mode** { **enhanced** \| **normal** } ]]]

**[undo port group interface*** interface-name*]

【缺省情况】

IRF端口没有与任何IRF物理端口进行绑定。

【视图】

IRF端口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：表示IRF物理端口的类型和编号。各型号设备上可用作IRF物理端口的端口请参见产品的相关手册。

*[interface-name*]：IRF物理端口的名称，格式为*interface-type+interface-number*。

**[mode**]：设置IRF物理端口的工作模式。该参数的支持情况以及缺省情况与设备的型号有关，请以实际情况为准。

·**enhanced**：将接口的工作模式设置为增强模式。本参数的支持情况与设备的的型号有关，请以实际情况为准。

·**normal**：将接口的工作模式设置为普通模式。本参数的支持情况与设备的的型号有关，请以实际情况为准。

【使用指导】

需要注意的是：

·多次执行该命令可以将同一IRF端口与多个IRF物理端口绑定，最多可绑定的物理端口数与设备型号有关，请以设备的实际情况为准。

·配置的工作模式只在接口作为IRF物理端口时生效，作为普通端口使用时不生效。IRF中直接相连的两个IRF物理端口的模式必须相同，否则，报文无法互通。当用于VPLS（Virtual Private LAN Service，虚拟专用局域网服务）组网时，请设置为**enhanced**。

·需要先使用**shutdown**命令关闭相应的物理端口，才能执行**port group interface**命令将IRF端口与该物理端口绑定。再使用**undo shutdown**命令开启该物理端口，该物理端口才能用作IRF物理端口建立IRF连接。

·需要先使用**shutdown**命令关闭相应的IRF物理端口，才能执行**undo port group interface**命令取消IRF端口与该IRF物理端口的绑定关系。再使用**undo shutdown**命令开启该IRF物理端口，该物理端口才能用于报文的转发。

·有些接口板出厂时已将接口分组，同一组内的接口只能都作为IRF物理端口，或者都不作为IRF物理端口。当将某组中的一个接口和IRF端口绑定时，系统要求先将该组中的所有接口都关闭，否则，绑定失败；当绑定后，将其中一个接口激活时，系统会判断该组中的其它接口是否已经和IRF端口绑定（可以绑定到同一IRF端口，也可以绑定到不同IRF端口），如果没有绑定，则不允许激活。

配置本命令后，即便热插拔接口板导致绑定的IRF物理端口不存在了，但绑定关系仍然存在，使用**undo port group interface**命令可以取消绑定关系。

【举例】

\# 将成员设备3的IRF物理端口Ten-GigabitEthernet3/0/1和IRF端口IRF-port1绑定。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 3/0/1

Sysname-Ten-GigabitEthernet3/0/1 shutdown

Sysname-Ten-GigabitEthernet3/0/1 quit

Sysname irf-port 3/1

Sysname-irf-port3/1 port group interface ten-gigabitethernet 3/0/1

Sysname-irf-port3/1 quit

Sysname interface ten-gigabitethernet 3/0/1

Sysname-Ten-GigabitEthernet3/0/1 undo shutdown

**IRF \-- IRF2配置命令（分布式设备） \-- chassis convert mode irf**

------------------------------------------------------------------------

**[chassis convert mode irf**]命令用来将设备的运行模式切换到IRF模式。

**[undo chassis convert mode**]命令用来将设备的运行模式切换到独立运行模式。

【命令】

**[chassis convert mode irf**]

**[undo chassis convert mode**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

设备出厂时处于独立运行模式。如果在本次运行过程中，没有修改设备的运行模式，则下次启动会延用本次启动的运行模式；如果在本次运行过程中，修改了设备的运行模式，则设备会自动重启，切换到新的模式。

请根据组网需要来配置设备的运行模式。当设备从独立运行模式切换到IRF模式后，即便只有一台设备也会形成IRF。因为管理和维护IRF需要耗费一定的系统资源，所以，如果当前组网中设备不需要和别的设备组成IRF时，建议将运行模式配置为独立运行模式。

设备从独立运行模式切换到IRF模式时，需要使用成员编号进行配置文件的自动转换。如果模式切换前没有配置成员编号，则系统会自动使用1作为成员编号。

需要注意的是，确认模式切换操作后，设备会自动重启，完成运行模式的切换。

【举例】

\# 设备当前处于独立运行模式时，将设备切换到IRF模式。

\<Sysname\> system-view

Sysname chassis convert mode irf

The device will switch to IRF mode and reboot. You are recommended to save the current running configuration and specify the configuration file for the next startup. Continue? [Y/N:y]

Do you want to convert the content of the next startup configuration file flash:/startup.cfg to make it available in IRF mode? [Y/N:y]

Now rebooting, please wait\...

Saving the converted configuration file to the main board succeeded.

Slot 1:

 Saving the converted configuration file succeeded.

 Now rebooting, please wait\...

\# 设备当前处于IRF模式时，将设备切换到独立运行模式。

\<Sysname\> system-view

Sysname undo chassis convert mode

The device will switch to stand-alone mode and reboot。 You are recommended to save the current running configuration and specify the configuration file for the next startup. Continue? [Y/N:y]

Do you want to convert the content of the next startup configuration file flash:/startup.cfg to make it available in stand-alone mode? [Y/N:y]

Now rebooting, please wait\...

Saving the converted configuration file to the main board succeeded.

Chassis 2 Slot 1:

Saving the converted configuration file succeeded.

Now rebooting, please wait\...

**IRF \-- IRF2配置命令（分布式设备） \-- display irf**

------------------------------------------------------------------------

**[display irf**]命令用来显示IRF中所有成员设备的相关信息。

【命令】

**[display irf**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IRF中所有成员设备的相关信息。

\<Sysname\> display irf

MemberID  Slot  Role   Priority  CPU-Mac         Description

 \*+1      0    Master  1         0210-fc03-0007  \-\-\-\--

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 \* indicates the device is the master.

 + indicates the device through which the user logs in.

 The Bridge MAC of the IRF is: 3ce5-a6b8-3800

 Auto upgrade                : yes

 Mac persistent              : always

 Domain ID                   : 0

 Auto merge                  : no

表1-7 display irf命令显示信息描述表

字段

描述

MemberID

本IRF中成员设备的编号（如果编号前带"\*"，表示该设备是主设备；如果编号前带"+"，表示该设备是用户当前登录的、正在操作的设备）

Slot

成员设备上主控板所在的槽位号

Role

该主控板在IRF中的角色，取值可能为：

·Standby：全局备用主控板

·Master：全局主用主控板

·Loading：正在自动加载系统启动文件的全局备用主控板

Priority

成员设备的优先级

CPU-MAC

设备的CPU MAC地址

Description

设备的描述信息（没有描述信息时，Description字段显示为\"\-\-\-\--\"。如果描述信息较多，无法在一行中完全显示，则以"..."结尾，省略后面的信息。此时可以使用**display current-configuration**命令来查询完整的描述信息）

Bridge MAC of the IRF is

IRF的桥MAC地址

Auto upgrade

是否使能自动加载系统启动文件功能（yes表示使能，no表示未使能）

MAC persistent

IRF桥MAC地址保留功能的配置信息：

·6 min表示IRF桥MAC地址保留时间为6分钟

·always表示IRF桥MAC地址永久保留不改变

·no表示立即改变IRF桥MAC地址

Domain ID

IRF的域编号

Auto merge

IRF合并自动重启功能是否使能：

·yes：表示已经使能

·no：表示没有使能

**IRF \-- IRF2配置命令（分布式设备） \-- display irf configuration**

------------------------------------------------------------------------

**[display irf configuration**]命令用来显示所有成员设备上重启以后生效的IRF配置。

【命令】

**[display irf configuration**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 设备工作在独立运行模式时，显示所有成员设备上重启以后生效的IRF配置。

\<Sysname\> display irf configuration

 MemberID Priority IRF-Port1                   IRF-Port2

 1        1        disable                     disable

\# 设备工作在IRF模式时，显示所有成员设备上重启以后生效的IRF配置。

\<Sysname\> display irf configuration

 MemberID  NewID  IRF-Port1                     IRF-Port2

  1        1      Ten-GigabitEthernet1/1/0/1    disable

                  Ten-GigabitEthernet1/1/0/2

  2        2      disable                       Ten-GigabitEthernet2/1/0/1

                                                Ten-GigabitEthernet2/1/0/2

表1-8 display irf configuration命令显示信息描述表

字段

描述

MemberID

设备当前的成员编号

Priority

成员优先级。该字段只有设备处于独立运行模式时，才会显示

NewID

配置的成员编号，设备重启后将会使用。该字段只有设备处于IRF模式时，才会显示

IRF-Port1

IRF端口1的配置（如果显示为多个端口，则表示该IRF端口由这些IRF物理端口聚合而成；如果显示为disable，则表示该IRF端口没有使能）

IRF-Port2

IRF端口2的配置（如果显示为多个端口，则表示该IRF端口由这些IRF物理端口聚合而成；如果显示为disable，则表示该IRF端口没有使能）

**IRF \-- IRF2配置命令（分布式设备） \-- display irf link**

------------------------------------------------------------------------

**[display irf link**]命令用来显示IRF链路信息。

【命令】

**[display irf link**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IRF链路信息。

\<Sysname\> display irf link

Member 1

 IRF Port    Interface                       Status

 1           disable                         \--

 2           GigabitEthernet1/3/0/1(MDC1)    UP

             GigabitEthernet1/5/0/1(MDC2)    ADM

             GigabitEthernet1/6/0/1(MDC3)    DOWN

Member 2(IRF-Link-Down: MDC2, MDC3)

 IRF Port    Interface                       Status

 1           GigabitEthernet2/3/0/1(MDC1)    UP

             GigabitEthernet2/5/0/1(MDC2)    DOWN

             GigabitEthernet2/6/0/1(MDC3)    ADM

 2           disable                         \--

\# 显示IRF链路信息（支持MDC但不支持IRF链路检测功能的设备）。

\<Sysname\> display irf link

Member 1

 IRF Port    Interface                       Status

 1           disable                         \--

 2           GigabitEthernet1/3/0/1(MDC1)    UP

             GigabitEthernet1/5/0/1(MDC2)    ADM

             GigabitEthernet1/6/0/1(MDC3)    DOWN

Member 2

 IRF Port    Interface                       Status

 1           GigabitEthernet2/3/0/1(MDC1)    UP

             GigabitEthernet2/5/0/1(MDC2)    DOWN

             GigabitEthernet2/6/0/1(MDC3)    ADM

 2           disable                         \--

\# 显示IRF链路信息（不支持MDC也不支持IRF链路检测功能的设备）。

\<Sysname\> display irf link

Member 1

 IRF Port    Interface                       Status

 1           disable                         \--

 2           GigabitEthernet1/3/0/1          UP

             GigabitEthernet1/5/0/1          ADM

             GigabitEthernet1/6/0/1          DOWN

Member 2

 IRF Port    Interface                       Status

 1           GigabitEthernet2/3/0/1          UP

             GigabitEthernet2/5/0/1          DOWN

             GigabitEthernet2/6/0/1          ADM

 2           disable                         \--

表1-9 display irf link命令显示信息描述表

字段

描述

MemberID

成员编号

(IRF-Link-Down: MDC2, MDC3)

表示IRF链路检测功能检测到该成员设备上MDC2和MDC3中的IRF链路状态为Down，于是将该成员设备上这两个MDC的业务口状态也变为down，不能转发报文（如果设备不支持IRF链路检测功能则不显示该信息）

IRF Port

IRF端口号，其中：

·1表示IRF端口1

·2表示IRF端口2

Interface

对应的IRF物理端口的名称和该物理接口所属的MDC，用MDC的编号表示（如果设备不支持MDC则不显示MDC信息）

·如果显示信息中包含多个物理端口则表示该IRF端口由多个IRF物理端口聚合而成

·如果显示为disable则表示该IRF端口还没有和IRF物理端口绑定

Status

IRF端口的物理接口的链路状态

·UP：链路up

·DOWN：链路down

·ADM：用户在接口下执行了**shutdown**命令

·ABSENT：接口不存在，没有插入接口模块

**IRF \-- IRF2配置命令（分布式设备） \-- display irf topology**

------------------------------------------------------------------------

**[display irf topology**]命令用来显示IRF的拓扑信息。

【命令】

**[display irf topology**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示当前IRF的拓扑信息。

\<Sysname\> display irf topology

                           Topology Info

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

               IRF-Port1                IRF-Port2

 MemberID    Link       neighbor      Link       neighbor    Belong To

 3           DIS        \-\--           DOWN       \-\--         0210-fc03-0007

表1-10 display irf topology命令显示信息描述表

字段

描述

MemberID

成员编号

IRF-Port1

IRF端口1的信息，包括Link和neighbor

IRF-Port2

IRF端口2的信息，包括Link和neighbor

Link

IRF端口的链路状态，包括：

·UP：IRF链路up

·DOWN：IRF链路down

·DIS：没有将IRF端口与IRF物理端口绑定

·TIMEOUT：IRF报文超时

neighbor

与该IRF端口直连的设备的成员编号（显示为"\-\--"表示该端口没有连接其它成员设备）

Belong To

所属IRF，用当前IRF中主设备的CPU MAC地址来表示

**IRF \-- IRF2配置命令（分布式设备） \-- display irf-port load-sharing mode**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display irf-port load-sharing mode**]命令用来显示IRF链路的负载分担模式。

【命令】

**[display irf-port load-sharing mode ** **irf-port**  *member-id*/*port-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[irf-port**]：显示指定IRF链路的负载分担模式。不指定该参数时，显示全局IRF链路的负载分担模式。

*[member-id*/*port-number*]：表示IRF端口编号。其中，*member-id*表示设备在IRF中的成员编号；*port-number*表示IRF端口索引，取值为1或2。不指定该参数时，显示所有连通的IRF链路的负载分担模式，如果当前没有连通的IRF链路，则显示"No IRF link exists."。

【使用指导】

需要注意的是：

·如果未指定**irf-port**参数，则显示全局采用的IRF链路负载分担模式。

·如果仅指定**irf-port**参数而未指定IRF端口编号，则显示所有IRF端口下分别采用的负载分担模式。

·如果指定了IRF端口编号，则显示该IRF端口下采用的负载分担模式。

【举例】

\# 显示缺省情况下全局采用的IRF链路负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display irf-port load-sharing mode

irf-port Load-Sharing Mode:

Layer 2 traffic: destination-mac address, source-mac address

Layer 3 traffic: destination-ip address,  source-ip address

Layer 4 traffic: destination-port,        source-port

MPLS traffic   : mpls-label1,             mpls-label2,

                 mpls-label3

\# 显示非缺省情况下全局采用的IRF链路负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display irf-port load-sharing mode

irf-port Load-Sharing Mode:

destination-mac address, source-mac address

\# 显示缺省情况下IRF端口1/1下采用的负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display irf-port load-sharing mode irf-port 1/1

irf-port 1/1 Load-Sharing Mode:

Layer 2 traffic: destination-mac address, source-mac address

Layer 3 traffic: destination-ip address,  source-ip address

Layer 4 traffic: destination-port,        source-port

MPLS traffic   : mpls-label1,             mpls-label2,

                 mpls-label3

\# 显示非缺省情况下IRF端口1/1下采用的负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display irf-port load-sharing mode irf-port 1/1

irf-port 1/1 Load-Sharing Mode:

destination-mac address, source-mac address

\# 显示所有IRF端口下分别采用的负载分担模式。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display irf-port load-sharing mode irf-port

irf-port 1/1 Load-Sharing Mode:

  destination-ip address,  source-ip address,       mpls-label1

irf-port 1/2 Load-Sharing Mode:

Layer 2 traffic: destination-mac address, source-mac address

Layer 3 traffic: destination-ip address,  source-ip address

Layer 4 traffic: destination-port,        source-port

MPLS traffic   : mpls-label1,             mpls-label2,

                 mpls-label3

表1-11 display irf-port load-sharing mode命令显示信息描述表

字段

描述

irf-port Load-Sharing Mode

全局采用的IRF链路负载分担类型：

·缺省情况下显示：二层报文、三层报文、四层报文、MPLS报文采用的负载分担类型（各设备支持的报文类型不同，请以设备的实际情况为准）

·非缺省情况下显示：用户配置后采用的负载分担类型

irf-port 1/1 Load-Sharing Mode

IRF端口1/1下采用的负载分担类型：

·缺省情况下显示：全局采用的负载分担类型

·非缺省情况下显示：用户配置后采用的负载分担类型

Layer 2 traffic: destination-mac address, source-mac address

二层报文缺省采用的负载分担类型：按照源MAC地址和目的MAC地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

Layer 3 traffic: destination-ip address,  source-ip address

三层报文缺省采用的负载分担类型：按照源IP地址和目的IP地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

Layer 4 traffic: destination-port,        source-port

四层报文缺省采用的负载分担类型：按照源端口和目的端口进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

MPLS traffic   : mpls-label1,             mpls-label2,                 mpls-label3

MPLS报文缺省采用的负载分担类型：按照第1～3层的MPLS标签进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

destination-mac address, source-mac address

用户配置后采用的负载分担类型：按照源MAC地址和目的MAC地址进行负载分担（此字段的显示内容与用户的配置相关）

**IRF \-- IRF2配置命令（分布式设备） \-- display mad**

------------------------------------------------------------------------

![说明](IRF命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **mad**]命令用来显示MAD配置信息。

【命令】

**[display mad** [ **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[verbose**]：表示显示MAD详细配置信息。如果不使用该参数，则显示的是MAD的简要信息。

【举例】

\# 显示MAD简要配置信息。

\<Sysname\> display mad

MAD ARP disabled.

MAD ND disabled.

MAD LACP disabled.

MAD BFD disabled.

\# 显示MAD详细配置信息。

\<Sysname\> display mad verbose

Excluded ports(configurable):

  Ten-GigabitEthernet2/1/0/2

  Ten-GigabitEthernet2/1/0/3

Excluded ports(can not be configured):

  Ten-GigabitEthernet2/2/0/25

  Ten-GigabitEthernet3/2/0/26

MAD enabled aggregation port:

  Bridge-Aggregation2

MAD BFD enabled interface:

  Vlan-interface2

    mad ip address 10.0.0.2 255.255.0.0 member 2

    mad ip address 10.0.0.3 255.255.0.0 member 3

表1-12 display mad命令显示信息描述表

字段

描述

MAD ARP disabled

没有使能ARP MAD检测功能

MAD ND disabled

没有使能ND MAD检测功能

MAD LACP disabled

没有使能LACP MAD检测功能

MAD BFD disabled

没有使能BFD MAD检测功能

MAD ARP enabled.

已经使能了ARP MAD检测功能

MAD ND enabled

已经使能了ND MAD检测功能

MAD LACP enabled

已经使能了LACP MAD检测功能

MAD BFD enabled

已经使能了BFD MAD检测功能

Current MAD status

MAD当前的状态，包括：

·Detect：检测状态，即IRF处于正常状态

·Recovery：发生多Active冲突时，失败的一方进入Recovery状态，该状态下设备会自动关闭所有非保留的业务接口

·Detect to Recovery：检测状态到Recovery状态的中间状态

·Recovery to Detect：Recovery状态到检测状态的中间状态

Excluded ports(configurable)

用户配置的保留接口

Excluded ports(can not be configured)

系统默认保留的接口（不需要用户配置，自动保留）

MAD enabled aggregation port

使能了LACP MAD的聚合口

MAD BFD enabled interface

使能了BFD MAD的接口

MAD BFD enabled interface:

  Vlan-interface2

    mad ip address 10.0.0.2 255.255.0.0 member 2

    mad ip address 10.0.0.3 255.255.0.0 member 3

IRF中MAD IP的配置，包括在哪个三层接口下配置了MAD IP，各成员设备上的MAD IP配置

MAD ARP enabled interface:

使能ARP MAD的接口（该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准）

**IRF \-- IRF2配置命令（分布式设备） \-- display port restricted**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display port restricted**]命令用来显示系统中被限制端口的信息。

【命令】

**[display port restricted** [ **chassis** *chassis-number* [ **slot** *slot-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis** *chassis-number*]：表示IRF中指定成员设备上被限制端口的信息。*chassis-number*表示设备在IRF中的成员编号，不指定该参数时，显示IRF中所有被限制端口的信息。

**[slot** *slot-number*]：表示指定接口板上被限制端口的信息。*slot-number*表示接口板所在的槽位号，不指定该参数时，显示指定成员设备上的所有接口板上被限制端口的信息。

【使用指导】

与IRF物理端口处于同一接口板上接口，被配置为三层聚合接口的成员端口的三层物理口时称为被限制端口。

被限制端口可以正常收发单播和广播报文，但是对于组播报文，只能发送，不能接收。

该命令用于在IRF模式下帮助用户了解当前设备上哪些接口被限制了。

【举例】

\# 显示成员设备1的4号接口板上的被限制端口的信息。

\<Sysname\> display port restricted chassis 1 slot 4

Chassis: 1

Slot: 4

Restricted ports:

  GigabitEthernet1/4/0/1 GigabitEthernet1/4/0/2

**IRF \-- IRF2配置命令（分布式设备） \-- easy-irf**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

只在IRF模式下支持该命令。

**[easy-irf**]命令用于快速配置堆叠环境。

【命令】

**[easy-irf** [ **member** *member-id* [ **renumber** *new-member-id*  **domain** *domain-id*  **priority** *priority*   **irf-port1** *interface-list1*   **irf-port2** *interface-list2*  ]]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[member** *member-id*]：表示设备当前的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[renumber** *new-member-id*]：表示新成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。不指定该参数时，表示不修改成员编号。

**[domain** *domain-id*]：表示设备所属的IRF域编号，取值范围为0～4294967295。同一IRF中成员设备域编号应配置为相同值。

**[priority** *priority*]：表示IRF成员的优先级，取值范围为1～32。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。

**[irf-port1** *interface-list1*]：表示和IRF端口1绑定的IRF物理端口。表示方式为*interface-list1* = { *interface-type interface-number* }&\<1-n\>。其中*interface-type interface-number*表示接口类型和接口编号。&\<1-n\>表示前面的参数最多可以输入n次。n的取值与设备的型号有关，请以设备的实际情况为准。

**[irf-port2 ***interface-list2*]：表示和IRF端口2绑定的IRF物理端口。表示方式为*interface-list2* = { *interface-type interface-number* }&\<1-n\>。其中*interface-type interface-number*表示接口类型和接口编号。&\<1-n\>表示前面的参数最多可以输入n次。n的取值与设备的型号有关，请以设备的实际情况为准。同一物理端口只能一个IRF端口绑定。

【使用指导】

使用该功能，用户可以通过一条命令配置IRF的基本参数，包括新成员编号、域编号、绑定物理端口，简化了配置步骤，达到快速配置IRF的效果。

在配置该功能时，有两种方式：

·交互模式：用户输入**easy-irf**，回车，在交互过程中输入具体参数的值。

·非交互模式，在输入命令行时直接指定所需参数的值。

两种方式的配置效果相同，如果用户对本功能不熟悉，建议使用交互模式。

配置时，需要注意的是：

·如果给成员设备指定新的成员编号，该成员设备会立即自动重启，以使新的成员编号生效。

·多次使用该功能，修改域编号/优先级/IRF物理端口时，域编号和优先级的新配置覆盖旧配置，IRF物理端口的配置会新旧进行叠加。如需删除旧的IRF物理端口配置，需要在IRF端口视图下，执行**undo port group interface**命令。一个IRF端口最多可绑定多少个IRF物理端口与设备的型号有关，请以设备的实际情况为准。

·在交互模式下，为IRF端口指定物理端口时，请注意：

¡接口类型和接口编号间不能有空格。

¡不同物理接口之间用英文逗号分隔。

¡有些接口板出厂时已将接口分组，如果要将该组内的某接口和IRF端口绑定，需要将该组的所有接口都和IRF端口绑定。

【举例】

\# 通过非交互模式配置成员设备2的新成员编号为3，域编号为10，优先级为10，IRF端口1和Ten-GigabitEthernet2/1/0/21、Ten-GigabitEthernet2/1/0/22、Ten-GigabitEthernet2/1/0/23和Ten-GigabitEthernet2/1/0/24绑定。

\<Sysname\> system-view

Sysname easy-irf member 1 renumber 2 domain 10 priority 10 irf-port1 ten-gigabitethernet 2/1/0/21 ten-gigabitethernet 2/1/0/22 ten-gigabitethernet 2/1/0/23 ten-gigabitethernet 2/1/0/24

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

                  Configuration summary for member 2

IRF new member ID: 3

IRF domain ID    : 10

IRF priority     : 10

IRF-port 1       : Ten-GigabitEthernet2/1/0/21, Ten-GigabitEthernet2/1/0/22

                   Ten-GigabitEthernet2/1/0/23, Ten-GigabitEthernet2/1/0/24

IRF-port 2       : Disabled

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Are you sure to use these settings to set up IRF? [Y/N y]

Starting to configure IRF\...

Configuration succeeded.

The device will reboot for the new member ID to take effect. Continue? [Y/N y]

\# 通过交互模式配置成员设备3的新编号为5，域编号为10，优先级为10，IRF端口1和Ten-GigabitEthernet3/1/0/21、Ten-GigabitEthernet3/1/0/22、Ten-GigabitEthernet3/1/0/23和Ten-GigabitEthernet3/1/0/24绑定。

\<Sysname\> system-view

Sysname easy-irf

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Welcome to use easy IRF.

To skip the current step, enter a dot sign (.).

To return to the previous step, enter a minus sign (-).

To use the default value (enclosed in [) for each parameter, press Enter withou]

t entering a value.

To quit the setup procedure, press CTRL+C.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Select a member by its ID \<3\> [3:3]

Specify a new member ID \<1\~10\> [1: 5]

Specify a domain ID \<0\~4294967295\> [0: 10]

Specify a priority \<1\~32\> [1: 10]

Specify IRF-port 1 bindings (a physical interface or a comma-separated physical

interface list)[Disabled: ten-gigabitethernet3/1/0/21,ten-gigabitethernet3/1/0/22,ten-gigabitethernet3/1/0/23,ten-gigabitethernet3/1/0/24]

Specify IRF-port 2 bindings (a physical interface or a comma-separated physical

interface list)[Disabled:]

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

                  Configuration summary for member 3

IRF new member ID: 5

IRF domain ID    : 10

IRF priority     : 10

IRF-port 1       : Ten-GigabitEthernet3/1/0/21, Ten-GigabitEthernet3/1/0/22

                   Ten-GigabitEthernet3/1/0/23, Ten-GigabitEthernet3/1/0/24

IRF-port 2       : Disabled

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Are you sure to use these settings to set up IRF? [Y/N y]

Starting to configure IRF\...

Configuration succeeded.

The device will reboot for the new member ID to take effect. Continue? [Y/N y]

**IRF \-- IRF2配置命令（分布式设备） \-- irf auto-merge enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image003.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[irf auto-merge enable**]命令用来使能IRF合并自动重启功能。

**[undo irf auto-merge enable**]命令用来关闭IRF合并自动重启功能。

【命令】

**[irf auto-merge enable**]

**[undo irf auto-merge enable**]

【缺省情况】

IRF合并自动重启功能处于使能状态。即两台IRF合并时，竞选失败方会自动重启。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

IRF合并时，两台IRF会遵照角色选举的规则进行竞选，竞选失败方IRF的所有成员设备需要重启才能加入获胜方IRF。其中：

·如果没有使能IRF合并自动重启功能，则合并过程中的重启需要用户根据系统提示手工完成。

·如果使能IRF合并自动重启功能，则合并过程中的重启由系统自动完成。

需要注意的是：

·当IRF模式下，IRF端口状态为DOWN或DIS时，配置IRF物理端口和IRF端口绑定，引起IRF端口状态变为UP，从而触发IRF合并，此时，即便使能了IRF合并自动重启功能，该功能也暂时不生效，系统会提示用户必须手工重启竞选失败方才能完成合并。此时，请使用**save**命令将当前配置（尤其是IRF端口的配置）保存到下次启动配置文件后，再重启失败方。否则，失败方重启后，会因为没有IRF配置信息而不能合并。

·其它情况下触发的IRF合并（比如IRF连接故障恢复后引起的合并；两台IRF的启动配置文件中已经绑定了IRF物理端口和IRF端口，然后建立IRF物理连接引起IRF端口状态变为UP，触发的IRF合并等），如果合并时已使能了IRF合并自动重启功能，则竞选失败方会自动重启加入获胜方，合并为一个IRF。

·要使IRF合并自动重启功能正常运行，请在即将合并的两台IRF上都使能IRF合并自动重启功能。

·本命令只在IRF模式下支持。配置**irf auto-merge enable**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

【举例】

\# 使能IRF合并自动重启功能。

\<Sysname\> system-view

Sysname irf auto-merge enable

**IRF \-- IRF2配置命令（分布式设备） \-- irf auto-update enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[irf auto-update enable**]命令用来使能IRF系统启动文件的自动加载功能。

**[undo irf auto-update enable**]命令用来关闭IRF系统启动文件的自动加载功能。

【命令】

**[irf auto-update enable**]

**[undo irf auto-update enable**]

【缺省情况】

IRF系统启动文件的自动加载功能处于使能状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·如果没有使能自动加载功能，当参与IRF的设备软件版本与主设备的软件版本不一致时，则新加入或者优先级低的设备不能正常启动。此时需要用户手工升级设备的软件版本后，再将设备加入IRF。

·使能自动加载功能后，成员设备加入IRF时，会与主设备的软件版本号进行比较，如果不一致，则自动从主设备下载启动文件，然后使用新的系统启动文件重启，重新加入IRF。

需要注意的是：

·当新加入设备的型号和主设备当前运行的软件版本不配套时，自动加载功能可能不能正常工作。因此建议新设备加入IRF前，请确保新加入设备的型号和主设备当前运行的软件版本配套。

·为了能够自动加载成功，请确保从设备存储介质上有足够的空闲空间用于存放新的启动文件。如果从设备存储介质上空闲空间不足，系统会自动删除从设备的当前启动文件来完成加载。如果删除从设备的当前启动文件后空间仍然不足，从设备将无法进行自动加载。此时，需要管理员重启从设备并进入从设备的Boot ROM菜单，删除一些不重要的文件后，再让从设备重新加入IRF。

·本命令只在IRF模式下支持。配置**irf auto-update enable**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

【举例】

\# 使能IRF系统启动文件的自动加载功能。

\<Sysname\> system-view

Sysname irf auto-update enable

**IRF \-- IRF2配置命令（分布式设备） \-- irf domain**

------------------------------------------------------------------------

**[irf domain**]命令用来配置IRF域编号。

**[undo irf domain**]命令用来恢复缺省情况。

【命令】

**[irf domain** *domain-id*]

**[undo irf** **domain**]

【缺省情况】

IRF的域编号为0。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-id*]：IRF的域编号，取值范围为0～4294967295。

【使用指导】

为了适应各种组网应用，同一个网络里可以部署多个IRF。IRF之间使用不同的域编号以示区别。在LACP MAD和ARP MAD检测组网中，如果中间设备本身也是一个IRF系统，则必须配置该命令确保本IRF和中间设备组成的IRF的域编号不同，否则可能造成检测异常，甚至导致业务中断。

IRF域编号是一个全局变量，IRF中的所有成员设备、所有MDC都共用这个IRF域编号。在缺省MDC上通过**irf domain**命令，或者在任意MDC上通过**mad enable**、**mad arp enable**、**mad nd enable**命令均可修改全局IRF域编号。因此，请按照网络规划来修改IRF域编号，不要随意修改。

本命令只在IRF模式下支持。配置**irf domain**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

【举例】

\# 配置IRF的域编号为30。

\<Sysname\> system-view

Sysname irf domain 30

**IRF \-- IRF2配置命令（分布式设备） \-- irf link-delay**

------------------------------------------------------------------------

**[irf link-delay**]命令用来配置IRF链路down延迟上报时间。

**[undo irf link-delay**]命令用来恢复缺省情况。

【命令】

**[irf link-delay ***interval*]

**[undo irf link-delay**]

【缺省情况】

不同型号的设备支持的缺省情况不同，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示延迟上报IRF链路down的时间，取值范围为0～10000，单位为毫秒。取值为0时，表示不延迟。

【使用指导】

本命令只在IRF模式下支持。配置**irf link-delay**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

在IRF环境中使用CFD、BFD功能时，请保证IRF链路down延迟上报时间小于CFD、BFD的超时时间，关于CFD、BFD功能的介绍，请参见"可靠性配置指导"中的"CFD"、"BFD"。

【举例】

\# 配置IRF链路down延迟上报时间为300毫秒。

\<Sysname\> system-view

Sysname irf link-delay 300

**IRF \-- IRF2配置命令（分布式设备） \-- irf isolate member**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[irf isolate member**]命令用来隔离某成员设备，即丢弃指定成员设备发送的所有报文。

**[undo irf isolate member**]命令用来取消隔离。

【命令】

**[irf isolate member** *member-id*]

**[undo irf isolate member** *member-id*]

【缺省情况】

不隔离任何成员设备。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当使用**display interface**命令查看到物理IRF接口的CRC错误报文较多，或者IRF中出现网络风暴时，可多次使用**irf isolate member**命令，将所有空闲的成员编号都隔离，再进行修复。成员设备被隔离后，其它成员设备收到该成员设备发送的报文时，会直接丢弃。如果后续需要扩充IRF，需先执行**undo**命令取消隔离。

【举例】

\# 隔离成员设备3。

\<Sysname\> system-view

Sysname irf isolate member 3

**IRF \-- IRF2配置命令（分布式设备） \-- irf mac-address persistent**

------------------------------------------------------------------------

**[irf mac-address persistent**]命令用来指定IRF桥MAC地址的保留时间。

**[undo irf mac-address persistent**]命令用来设置不保留IRF桥MAC地址，即主设备变更后，立即使用新主设备的桥MAC地址作为IRF桥MAC地址。

【命令】

**[irf mac-address persistent**[ { **always** \| **timer** }]]

**[undo irf mac-address persistent**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[always**]：指定IRF桥MAC地址保留时间为永久保留。

**[timer**]：指定IRF桥MAC地址保留时间为6分钟。

【使用指导】

·如果配置了IRF桥MAC地址保留时间为6分钟，当主设备离开IRF时，IRF桥MAC地址6分钟内不变化；如果主设备在6分钟内重新又加入IRF，则IRF桥MAC不会变化。如果6分钟后主设备没有回到IRF，则会使用新选举的主设备的桥MAC地址作为IRF桥MAC地址。

·如果配置了IRF桥MAC地址永久保留，则不管主设备是否离开IRF，IRF桥MAC地址始终保持不变。

·如果配置了IRF桥MAC地址不保留，立即变化。当主设备离开IRF时，系统立即使用新选举的主设备的桥MAC地址做IRF桥MAC地址。

需要注意的是：

·如果两个IRF的桥MAC地址相同，则它们不能合并为一个IRF。

·当使用ARP MAD和MSTP组网时，需要将IRF配置为桥MAC地址立即改变，即配置**undo irf mac-address persistent**命令。

·如果在IRF中启用了TRILL协议，则强烈建议用户配置IRF桥MAC地址保留时间为永久保留，否则，可能会导致一系列问题。

·本命令只在IRF模式下支持。配置**irf mac-address persistent**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

【举例】

\# 设置IRF桥MAC地址为永久保留。

\<Sysname\> system-view

Sysname irf mac-address persistent always

**IRF \-- IRF2配置命令（分布式设备） \-- irf member**

------------------------------------------------------------------------

**[irf member**]命令用来在独立运行模式下配置设备的成员编号。

**[undo irf member**]命令用来恢复缺省情况。

【命令】

**[irf member** *member-id*]

**[undo irf member**]

【缺省情况】

设备处于独立运行状态时，成员编号为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*]：表示设备在IRF中的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

成员编号有以下作用：

·设备从独立运行模式切换到IRF模式时，需要使用成员编号进行配置文件的自动转换。建议在独立运行模式下规划和修改设备的成员编号，以免成员编号冲突，设备切换到IRF模式后，不能加入已有的IRF。

·IRF系统使用成员编号来唯一标识一台成员设备。如果在独立运行模式下，请使用**irf member**命令来配置，这种方式下配置的成员编号在设备切换到IRF模式后生效；如果在IRF模式下，请使用**irf member ***member-id*** renumber ***new-member-id*命令来配置，这种方式下配置的成员编号需要重启设备才能生效。

【举例】

\# 在独立运行模式下配置设备的成员编号为2。

\<Sysname\> system-view

sysname irf member 2

【相关命令】

·**irf member renumber**

**IRF \-- IRF2配置命令（分布式设备） \-- irf member description**

------------------------------------------------------------------------

**[irf member description**]命令用来配置IRF中指定成员设备的描述信息。

**[undo irf member description**]命令用来恢复缺省情况。

【命令】

**[irf member ***member-id***description ***text*]

**[undo irf member ***member-id***description**]

【缺省情况】

成员设备没有描述信息。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*]：表示设备在IRF中的成员编号。

*[text*]：设备的描述信息，为1～127个字符的字符串。

【使用指导】

本命令只在IRF模式下支持。配置**irf member description**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

【举例】

\# 配置成员设备1的描述信息。

\<Sysname\> system-view

Sysname irf member 1 description F1Num001

**IRF \-- IRF2配置命令（分布式设备） \-- irf member priority**

------------------------------------------------------------------------

**[irf member** **priority**]用来设置IRF中指定成员设备的优先级。

**[undo irf member** **priority**]命令用来恢复缺省情况。

【命令】

**[irf member ***member-id*** priority ***priority*]

**[undo irf member ***member-id ***priority**]

【缺省情况】

设备的优先级为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*]：表示设备在IRF中的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[priority*]：表示优先级，取值范围为1～32。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。

【使用指导】

成员优先级有两种配置方式：

·在独立运行模式下，使用**irf priority**命令来配置。如果在IRF形成过程中，想让某台设备当选为主设备，请使用这种方式配置。

·在IRF模式下，使用**irf member ***member-id*** priority ***priority*命令来配置。这种方式下配置的成员优先级会影响IRF运行过程中的角色选举过程，比如当前主设备离开IRF时，优先级高的成员设备会当选为新的主设备；当发生IRF合并的时候，主设备成员优先级高的IRF会竞选成功。

【举例】

\# 在IRF模式下，将成员编号为2的成员设备的优先级设置为32。

\<Sysname\> system-view

Sysname irf member 2 priority 32

【相关命令】

·**irf priority**

**IRF \-- IRF2配置命令（分布式设备） \-- irf member renumber**

------------------------------------------------------------------------

**[irf member renumber**]命令用来配置IRF中指定成员设备的成员编号。

**[undo irf member renumber**]命令用来取消成员编号的设置。

【命令】

**[irf member ***member-id*** renumber ***new-member-id*]

**[undo irf member ***member-id*** renumber**]

【缺省情况】

设备切换到IRF模式后，使用的是独立运行模式下预配置的成员编号。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*]：表示设备在IRF中的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[new-member-id*]：表示修改后的成员编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

设备处于独立运行状态时，成员编号为1；切换到IRF模式后，使用的是独立运行模式下预配置的成员编号；如果模式切换前没有配置成员编号，则系统会自动使用1作为成员编号。

IRF使用成员编号来唯一标识一台成员设备。如果在独立运行模式下，请使用**irf member**命令来配置，这种方式下配置的成员编号在设备切换到IRF模式后生效；如果在IRF模式下，请使用**irf member ***member-id*** renumber ***new-member-id*命令来配置，这种方式下配置的成员编号需要重启设备才能生效。

需要注意的是：

·需要重启*member-id*对应的设备，*new-member-id*才能生效；

·**undo irf member renumber**命令只能取消本次运行过程中配置的成员编号。设备重启后，设备的成员编号就变为*new-member-id*，不能再取消，只能重新配置。

·在IRF中以设备编号标识设备，接口的标识以及某些命令行都与成员编号有关，修改设备成员编号可能导致设备配置发生变化或者丢失，请慎重。

【举例】

\# 配置IRF中设备（原成员编号为2）的成员编号为4。

\<Sysname\> system-view

Sysname irf member 2 renumber 4

Renumbering the member ID may result in configuration change or loss. Continue?[Y/Ny]

如果要取消以上配置，使设备的成员编号仍然是2，则可以执行以下命令：

Sysname undo irf member 2 renumber

Renumbering the member ID may result in configuration change or loss. Continue?[Y/Ny]

如果配置irf member 2 renumber 4后，重启设备，则设备的成员编号会变为4。此时，不能使用undo irf member 2 renumber恢复到编号2，只能使用irf member 4 renumber 2重新配置。

【相关配置】

·**irf member**

**IRF \-- IRF2配置命令（分布式设备） \-- irf mode enhanced**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[irf mode enhanced**]命令用来配置IRF增强功能。

**[undo irf mode enhanced**]命令用来恢复缺省情况。

【命令】

**[irf mode enhanced**]

**[undo irf mode enhanced**]

【缺省情况】

设备上未配置IRF增强功能。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

未配置IRF增强功能时，IRF中最多可以支持2台成员设备；配置IRF增强功能后，IRF中最多可以支持4台成员设备，大大增强了IRF的吞吐量和可靠性，不过，部分功能模块的规格会低于未配置IRF增强功能时。

配置IRF增强功能，需要注意以下几点：

·IRF合并前，IRF成员设备的IRF增强功能的使能情况应该保持一致，即都配置或都取消IRF增强功能，否则，无法形成一个IRF。

·设备创建了MDC后，不能再配置IRF增强功能，即**irf mode enhanced**和**mdc** *mdc-name* [ **id** *mdc-id* ]命令互斥，不能同时配置。有关MDC的详细描述，请参见"基础配置指导"中的"MDC"。

·设备运行在独立模式时，可以直接配置IRF增强功能。

·设备运行在IRF模式时，若存在三层以太网接口则需要切换为二层以太网接口（设备会有提示信息），才能配置IRF增强功能，关于三层以太网接口的详细介绍请参见"接口管理配置指导"中的"以太网接口"。

·设备从非增强模式切换到增强模式后，某些特性的规格会发生改变，比如设备最多支持的VPLS实例或MAC-in-MAC实例数目等。所以，如果设备运行在IRF模式，且当前配置了VPLS实例或MAC-in-MAC实例，则需要重启设备后（设备会提示重启），才能配置IRF增强功能，否则配置失败。VPLS实例的详细介绍请参见"MPLS配置指导"中的"VPLS"，MAC-in-MAC实例的详细介绍请参见"二层技术-以太网交换"中的"MAC-in-MAC"。

·配置IRF增强功能后必须保存当前配置（执行**save**命令）。

·配置了IRF增强功能后，不能再创建三层以太网接口/子接口，三层聚合接口/子接口。

·当设备运行在IRF模式且配置了IRF增强功能，此时用户如果想取消IRF增强功能（执行**undo irf mode enhanced**命令），必须保证成员设备小于等于两台且每台成员设备上只有一个IRF端口，否则IRF增强功能无法取消。

【举例】

\# 在独立运行模式下，配置IRF增强功能。

\<Sysname\> system-view

Sysname irf mode enhanced

\# 在IRF模式下，配置IRF增强功能。

\<Sysname\> system-view

Sysname irf mode enhanced

**IRF \-- IRF2配置命令（分布式设备） \-- irf priority**

------------------------------------------------------------------------

**[irf priority**]命令用来在独立运行模式下配置设备的成员优先级。

**[undo irf priority**]命令用来恢复缺省情况。

【命令】

**[irf priority** *priority*]

**[undo irf priority**]

【缺省情况】

设备的成员优先级为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：表示优先级，取值范围为1～32。优先级值越大表示优先级越高，优先级高的设备竞选时成为主设备的可能性越大。

【使用指导】

成员优先级有两种配置方式：

·在独立运行模式下，使用**irf priority**命令来配置。如果在IRF形成过程中，想让某台设备当选为主设备，请使用这种方式配置。

·在IRF模式下，使用**irf member ***member-id*** priority ***priority*命令来配置，这种方式下配置的成员优先级会影响IRF运行过程中的角色选举过程。比如当前主设备离开IRF时，优先级高的成员设备会当选为新的主设备；当发生IRF合并的时候，主设备成员优先级高的IRF会竞选成功。

【举例】

\# 在独立运行模式下将本设备的成员优先级设置为32。

\<Sysname\> system-view

sysname irf priority 32

【相关命令】

·**irf member priority**

**IRF \-- IRF2配置命令（分布式设备） \-- irf slot member**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[irf slot member**]命令用来修改主控板的IRF成员编号信息。

【命令】

分布式设备－独立运行模式：

**[irf slot*** slot-number*** member ***member-id*]

分布式设备－IRF模式：

**[irf chassis ***chassis-number*** slot*** slot-number*** member ***member-id*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：表示备用主控板所在的槽位号。

**[chassis ***chassis-number*** slot*** slot-number*]：表示某个成员设备上备用主控板所在的槽位号。

*[member-id*]：表示目标设备的成员编号。

【使用指导】

此命令用来设置指定槽位上主控板的目标设备的成员编号。

需要注意的是，本命令仅在IRF配置快速恢复时使用。其它场合下使用时会发生未知错误，请勿随意配置。

【举例】

\# 设备在IRF模式下，将成员设备2的1号槽位主控板的成员编号设置为1。

\<Sysname\> irf chassis 2 slot 1 member-id 1

**IRF \-- IRF2配置命令（分布式设备） \-- irf-port load-sharing mode**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

·本命令的支持情况以及支持的配置视图与设备的型号有关，请以设备的实际情况为准。

·不同视图下，本命令行支持的参数不同，请以设备的实际情况为准。

**[irf-port load-sharing mode**]命令用来配置IRF链路的负载分担模式。

**[undo irf-port load-sharing** **mode**]命令用来恢复缺省情况。

【命令】

**[irf-port load-sharing mode**\|]{.TableTextChar}** mpls-label2 **[\| **mpls-label3** \| **source-port** \| **source-ip** \| **source-mac** \| **vlan-id** } \* \| **flexible** }]

**[undo irf-port load-sharing mode**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图/IRF端口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination-ip**]：表示按报文的目的IP地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[destination-mac**]：表示按报文的目的MAC地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[destination-port**]：设置按报文的目的端口号实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ingress-port**]：设置按报文的入端口实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip-protocol**]：表示按报文的IP协议类型进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label1**]：表示按MPLS报文第一层（最外层）标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label2**]：表示按MPLS报文第二层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label3**]：表示按MPLS报文第三层标签进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-port**]：设置按报文的源端口号实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-ip**]：表示按报文的源IP地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-mac**]：表示按报文的源MAC地址进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan-id**]：表示按报文所属的VLAN进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flexible**]：设置按报文的不同类型L2、IPv4、IPv6、MPLS等分别按不同模式灵活实现负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以通过全局配置（系统视图下）和端口下（IRF端口视图下）的配置方式设置IRF链路的负载分担模式：

·在系统视图下执行该命令，则该配置对所有IRF链路生效；

·在IRF端口视图下执行该命令，则该配置只对当前IRF端口下的IRF链路生效；

·IRF链路会优先采用端口下的配置。如果端口下没有配置，则采用全局配置。

需要注意的是：

·在同一视图下多次配置该命令，以最新的配置为准。

·对于设备不支持的负载分担模式，系统将提示用户不支持。

·在配置负载分担模式前，请先将IRF端口和IRF物理端口绑定。否则，负载分担模式将配置失败。

【举例】

\# 配置按报文目的MAC地址实现全局的IRF链路负载分担模式。

\<Sysname\> system-view

Sysname irf-port load-sharing mode destination-mac

\# 配置按报文目的MAC地址实现IRF端口1/1下IRF链路的负载分担模式。

\<Sysname\> system-view

Sysname irf-port 1/1

Sysname-irf-port 1/1 irf-port load-sharing mode destination-mac

**IRF \-- IRF2配置命令（分布式设备） \-- irf-port member-id/port-number**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[irf-port ***member-id*/*port-number*]命令用来在IRF模式下创建IRF端口并进入IRF端口视图（如果该IRF端口已经创建，则直接进入该IRF端口视图）。

**[undo** **irf-port** *member-id*/*port-number*]用来删除指定IRF端口。

【命令】

**[irf-port ***member-id*/*port-number*]

**[undo irf-port ***member-id*/*port-number*]

【缺省情况】

设备上没有创建IRF端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[member-id*/*port-number*]：表示IRF端口编号。其中，*member-id*表示设备在IRF中的成员编号；*port-number*表示IRF端口索引，取值为1或2。

【使用指导】

IRF端口创建后，必须在该IRF端口下绑定IRF物理端口，才能用于IRF。

相关配置可参考命令**port group interface**。

【举例】

\# 在IRF模式下为成员编号为1的设备创建IRF端口1。

\<Sysname\> system-view

Sysname irf-port 1/1

**IRF \-- IRF2配置命令（分布式设备） \-- irf-port port-number**

------------------------------------------------------------------------

**[irf-port*** port-number*]命令用来在独立运行模式下创建IRF端口并进入IRF端口视图（如果该IRF端口已经创建，则直接进入该IRF端口视图）。

**[undo** **irf-port** *port-number*]用来删除指定IRF端口。

【命令】

**[irf-port ***port-number*]

**[undo irf-port ***port-number*]

【缺省情况】

设备上没有创建IRF端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：表示IRF端口编号，取值为1或2。

【举例】

\# 在处于独立运行模式下创建IRF端口1。

\<Sysname\> system-view

Sysname irf-port 1

Sysname-irf-port1

【相关命令】

·**port group interface**

**IRF \-- IRF2配置命令（分布式设备） \-- irf-port-configuration active**

------------------------------------------------------------------------

**[irf-port-configuration active**]命令用于来激活设备上所有IRF端口下的配置。

【命令】

**[irf-port-configuration active**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

IRF物理线缆连接好，并将IRF物理端口添加到IRF端口后，必须通过该命令手工激活IRF端口的配置才能形成IRF。

系统启动，通过配置文件将IRF物理端口加入IRF端口，或者IRF形成后再加入新的IRF物理端口时，IRF端口下的配置会自动激活不再需要使用该命令来激活。

【举例】

\# 在IRF端口1/2状态为DIS的情况下，激活该IRF端口。

·IRF端口状态为DIS表示IRF端口还没有与任何IRF物理端口绑定，所以，先配置绑定关系。绑定前需要先将IRF物理端口关闭，绑定后再将IRF物理端口激活。

\<Sysname\> system-view

Sysname interface ten-gigabitEthernet 1/1/0/27

Sysname-Ten-GigabitEthernet1/1/0/27 shutdown

Sysname-Ten-GigabitEthernet1/1/0/27 quit

Sysname irf-port 1/2

Sysname-irf-port1/2 port group interface ten-gigabitethernet 1/1/0/27

 Info : You are recommended to save the configuration now; otherwise, it will be lost after system reboot.

Sysname-irf-port1/2 quit

Sysname interface ten-gigabitethernet 1/1/0/27

Sysname-Ten-GigabitEthernet1/1/0/27 undo shutdown

Sysname-Ten-GigabitEthernet1/1/0/27 quit

·将当前配置保存到下次启动配置文件，以便IRF端口的配置在设备重启后能继续生效。

Sysname save

The current configuration will be written to the device. Are you sure? [Y/N:y]

Please input the file name(\*.cfg)[flash:/startup.cfg]

(To leave the existing filename unchanged, press the enter key):

flash:/aa.cfg exists, overwrite? [Y/N:y]

 Validating file. Please wait\...\...\...\...\...\...\...\...\....

 Saved the current configuration to mainboard device successfully.

Chassis 1 Slot 1:

 Save next configuration file successfully.

 Configuration is saved to device successfully.

·激活IRF端口的配置。

Sysname irf-port-configuration active

**IRF \-- IRF2配置命令（分布式设备） \-- mad arp enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mad arp enable**]命令用来使能ARP MAD检测功能。

**[undo mad arp enable**]用来关闭ARP MAD检测功能。

【命令】

**[mad arp enable**]

**[undo mad arp enable**]

【缺省情况】

ARP MAD检测功能处于关闭状态。

【视图】

三层接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了防止IRF级联组网时，本IRF的MAD检测报文转发到邻居IRF中影响邻居IRF的MAD检测，执行**mad arp enable**命令时，系统会要求用户输入IRF域编号。IRF域编号是一个全局变量，IRF中的所有成员设备、所有MDC都共用这个IRF域编号。缺省MDC上通过**irf domain**命令，或者在任意MDC上通过**mad enable**、**mad arp enable**、**mad nd enable**命令均可修改全局IRF域编号。因此，请按照网络规划来修改IRF域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。

VLAN 1不能用于MAD检测，因此，不能在VLAN接口1下使能ARP MAD检测功能。

BFD MAD、ARP MAD、ND MAD这三种检测方式独立工作，可以同时配置，但不能和LACP MAD方式同时配置。

【举例】

\# 在VLAN接口3上启用ARP MAD检测功能。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-Vlan-interface3 mad arp enable

 You need to assign a domain ID (range: 0-4294967295)

 Current domain is: 0: 1

 The assigned  domain ID is: 1

**IRF \-- IRF2配置命令（分布式设备） \-- mad bfd enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mad** **bfd** **enable**]命令用来使能BFD MAD检测功能。

**[undo** **mad** **bfd** **enable**]用来关闭BFD MAD检测功能。

【命令】

**[mad bfd enable**]

**[undo mad bfd enable**]

【缺省情况】

BFD MAD检测功能处于关闭状态。

【视图】

三层接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

需要注意的是：

·VLAN 1不能用于MAD检测，因此，不能在VLAN接口1下使能BFD MAD检测功能。

·BFD MAD、ARP MAD、ND MAD这三种检测方式独立工作，可以同时配置，但不能和LACP MAD方式同时配置。

·使能BFD MAD检测功能的三层接口只能专用于BFD MAD检测，不允许运行其它业务。如果用户配置了其它业务，可能会影响该业务以及BFD MAD检测功能的运行。

·BFD MAD检测功能与VPN功能互斥，请不要将使能了BFD MAD检测功能的三层接口与VPN实例进行绑定。

·BFD MAD检测功能与生成树功能互斥，在使能了BFD MAD检测功能的三层接口对应VLAN内的端口上，请不要使能生成树协议。

【举例】

\# 在VLAN接口3上启用BFD MAD检测功能。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-Vlan-interface3 mad bfd enable

**IRF \-- IRF2配置命令（分布式设备） \-- mad enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mad** **enable**]命令用来使能LACP MAD方式检测功能。

**[undo** **mad** **enable**]用来关闭LACP MAD方式检测功能。

【命令】

**[mad enable**]

**[undo mad enable**]

【缺省情况】

LACP MAD方式检测功能处于关闭状态。

【视图】

聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令可以在动态或静态聚合口下配置，但由于LACP MAD检测依赖于LACP协议，因此只在动态聚合接口下生效。

为了防止IRF级联组网时，本IRF的MAD检测报文转发到邻居IRF中影响邻居IRF的MAD检测，执行**mad enable**命令时，系统会要求用户输入IRF域编号。IRF域编号是一个全局变量，IRF中的所有成员设备、所有MDC都共用这个IRF域编号。缺省MDC上通过**irf domain**命令，或者在任意MDC上通过**irf domain**、**mad enable**、**mad arp enable**、**mad nd enable**命令均可修改全局IRF域编号。因此，请按照网络规划来修改IRF域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。

需要注意的是，BFD MAD、ARP MAD、ND MAD这三种检测方式独立工作，可以同时配置，但不能和LACP MAD方式同时配置。

【举例】

\# 在二层动态聚合接口1下启用LACP MAD方式检测功能。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 mad enable

 You need to assign a domain ID (range: 0-4294967295)

 Current domain is: 0: 1

 The assigned  domain ID is: 1

MAD LACP only enable on dynamic aggregation interface.

\# 在三层动态聚合接口1下启用LACP MAD方式检测功能。

\<Sysname\> system-view

Sysname interface route-aggregation 1

Sysname-Route-Aggregation1 mad enable

 You need to assign a domain ID (range: 0-4294967295)

 Current domain is: 0: 1

 The assigned  domain ID is: 1

MAD LACP only enable on dynamic aggregation interface.

**IRF \-- IRF2配置命令（分布式设备） \-- mad exclude interface**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mad** **exclude** **interface**]命令用来配置保留接口。

**[undo** **mad** **exclude** **interface**]命令用来恢复缺省情况。

【命令】

**[mad** **exclude** **interface** *interface-type interface-number*]

**[undo mad** **exclude interface** *interface-type interface-number*]

【缺省情况】

设备进入Recovery状态时会自动关闭本设备上所有的业务接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：表示接口类型和接口编号。

【使用指导】

IRF电缆断开后，网络中会存在两台（或者多台）全局配置完全相同的设备，这些设备连接到网络时可能会引起网络故障。为了防止这种情况发生，系统会进行多Active检测，最终只保留一台Active设备，其它设备都进入Recovery状态，并且关闭Recovery状态设备上的所有业务接口。使用该命令可以让指定的端口不被关闭，具体哪些接口需要保留由用户决定。建议除了对Telnet登录接口以及用于多Active检测的接口外，其他接口均关闭。

当分裂的IRF恢复时，处于Recovery状态的设备重启后重新加入IRF，关闭的接口会自动恢复。也可以通过命令行**mad restore**对处于Recovery状态的设备进行恢复，关闭的接口恢复正常。

【举例】

\# 配置GigabitEthernet1/1/0/1为保留接口，即当设备进入Recovery状态时，该接口不会被关闭。

\<Sysname\> system-view

Sysname mad exclude interface gigabitethernet 1/1/0/1

**IRF \-- IRF2配置命令（分布式设备） \-- mad ip address**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mad ip address**]命令用来给指定成员设备配置MAD IP地址。

**[undo** **mad** **ip** **address**]命令用来删除相应的MAD IP地址。

【命令】

**[mad ip address*** ip-address*[ { *mask* \| *mask-length* } **member** *member-id*]]

**[undo mad ip address ***ip-address*[ { *mask* \| *mask-length* } **member** *member-id*]]

【缺省情况】

没有为接口配置MAD IP地址。

【视图】

三层接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：接口的IP地址，为点分十进制格式。

*[mask*]：接口IP地址相应的子网掩码，为点分十进制格式。

*[mask-length*]：子网掩码长度，即掩码中连续"1"的个数，取值范围为0～32。

**[member** *member-id*]：表示设备在IRF中的成员编号。

【使用指导】

BFD MAD检测使用MAD IP地址来进行，MAD IP与普通IP地址不同的地方在于该IP地址与成员编号绑定，IRF中的成员设备的MAD IP地址必须为同一网段，只有主设备的MAD IP地址生效，从设备的MAD IP地址不生效。当IRF链路分裂时，IRF中的原从设备变为主设备，配置的MAD IP地址生效，BFD会话被激活。

需要注意的是，在用于BFD MAD检测的接口下必须使用本命令配置MAD IP地址，而不要配置其它IP地址（包括使用**ip address**命令配置的普通IP地址、VRRP虚拟IP地址等），以免影响MAD检测功能。

【举例】

\# 配置VLAN接口3在成员设备1上的MAD IP地址。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-Vlan-interface3 mad ip address 192.168.0.1 255.255.255.0 member 1

配置VLAN接口3在成员设备2上的MAD IP地址。

Sysname-Vlan-interface3 mad ip address 192.168.0.2 255.255.255.0 member 2

**IRF \-- IRF2配置命令（分布式设备） \-- mad nd enable**

------------------------------------------------------------------------

![说明](IRF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mad nd enable**]命令用来使能ND MAD检测功能。

**[undo mad nd enable**]用来关闭ND MAD检测功能。

【命令】

**[mad nd enable**]

**[undo mad nd enable**]

【缺省情况】

ND MAD检测功能处于关闭状态。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了防止IRF级联组网时，本IRF的MAD检测报文转发到邻居IRF中影响邻居IRF的MAD检测，执行**mad nd enable**命令时，系统会要求用户输入IRF域编号。IRF域编号是一个全局变量，IRF中的所有成员设备、所有MDC都共用这个IRF域编号。缺省MDC上通过**irf domain**命令，或者在任意MDC上通过**mad enable**、**mad arp enable**、**mad nd enable**命令均可修改全局IRF域编号。因此，请按照网络规划来修改IRF域编号，不要随意修改。如果继续使用当前编号，则直接按回车即可。

VLAN 1不能用于MAD检测，因此，不能在VLAN接口1下使能ND MAD检测功能。

BFD MAD、ARP MAD、ND MAD这三种检测方式独立工作，可以同时配置，但不能和LACP MAD方式同时配置。

【举例】

\# 在VLAN接口3上启用ND MAD检测功能。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-Vlan-interface3 mad nd enable

 You need to assign a domain ID (range: 0-4294967295)

 Current domain is: 0: 1

 The assigned  domain ID is: 1

【相关命令】

·**irf domain**

**IRF \-- IRF2配置命令（分布式设备） \-- mad restore**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mad restore**]命令用来将设备从Recovery状态恢复到正常状态。

【命令】

**[mad restore**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当IRF链路故障会导致多Active冲突，原IRF分裂为多个IRF，为了防止网络中配置冲突，IRF系统会通过多Active检测机制，让其中一个IRF继续正常工作，其它IRF的状态修改为Recovery（处于该状态的IRF不能处理业务报文）。如果继续正常工作的IRF也发生故障不能工作，此时可以通过本命令将处于Recovery状态的IRF恢复到正常工作状态接替原IRF工作，以便保证业务尽量少受影响。

【举例】

\# 将IRF从Recovery状态恢复到正常状态。

\<Sysname\> system-view

Sysname mad restore

   This command will restore the device from multi-active conflict state. Continue? [Y/N:Y]

Restoring from multi-active conflict state, please wait\...

**IRF \-- IRF2配置命令（分布式设备） \-- port group interface**

------------------------------------------------------------------------

**[port group interface**]命令用来绑定设备的IRF端口和IRF物理端口。

**[undo** **port group interface**]命令用来取消设备的IRF端口和IRF物理端口的绑定关系。

【命令】

**[port group **[ **mdc** *mdc-name*  **interface** *interface-type* *interface-number* [ **mode** { **enhanced** \| **extended** \| **normal** } ]]]

**[undo port group ** **mdc** *mdc-name* ] **interface** *interface-name*

【缺省情况】

设备上没有创建IRF端口。

【视图】

IRF端口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mdc** *mdc-name*]：表示IRF物理端口所属的MDC的名称，为1～15个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-type* *interface-number*]：表示接口类型和接口编号。

*[interface-name*]：接口的名称，格式为*interface-typeinterface-number，interface-type*与*interface-number*之间没有空格。

**[mode**]：设置IRF物理端口的工作模式。该参数以及各模式的支持情况与设备/接口板的型号有关，请以实际情况为准。

·**enhanced**：将接口的工作模式设置为增强模式。

·**ex****tended**：将接口的工作模式设置为扩展模式。

·**normal**：将接口的工作模式设置为普通模式。

【使用指导】

·当需要绑定的IRF物理端口属于非缺省MDC时，必须指定**mdc**参数，否则，系统将提示该接口不存在；当需要绑定的IRF物理端口属于缺省MDC时，可以不指定**mdc**参数。关于MDC的详细介绍请参见"基础配置指导"中的"MDC"。

·多次执行该命令可以将同一IRF端口与多个IRF物理端口绑定，最多可绑定的物理端口数与设备型号有关，请以设备的实际情况为准。

·配置的工作模式只在接口作为IRF物理端口时生效，作为普通端口使用时不生效。IRF中直接相连的两个IRF物理端口的模式必须相同，否则，报文无法互通。当用于VPLS（Virtual Private LAN Service，虚拟专用局域网服务）组网时，请设置为**enhanced**。

·在IRF模式下，需要先使用**shutdown**命令关闭相应的物理端口，才能执行**port group interface**命令将IRF端口与该物理端口绑定。再使用**undo shutdown**命令开启该物理端口，该物理端口才能用作IRF物理端口建立IRF连接**；**如果在独立运行模式下进行配置，则可以直接执行**port group interface**命令，不需要先使用**shutdown**命令关闭相应的物理端口。

·在IRF模式下，需要先使用**shutdown**命令关闭相应的IRF物理端口，才能执行**undo port group interface**命令取消IRF端口与该IRF物理端口的绑定关系。再使用**undo shutdown**命令开启该IRF物理端口，该物理端口才能用于报文的转发；如果在独立运行模式下进行配置，则可以直接执行**undo port group interface**命令，不需要先使用**shutdown**命令关闭相应的IRF物理端口。

·配置本命令后，即便热插拔接口板导致绑定的IRF物理端口不存在了，但绑定关系仍然存在，使用**undo port group interface**命令可以取消绑定关系。

·有些接口板出厂时已将接口分组，同一组内的接口只能都作为IRF物理端口，或者都不作为IRF物理端口。当将某组中的一个接口和IRF端口绑定时，系统要求先将该组中的所有接口都关闭，否则，绑定失败；当绑定后，将其中一个接口激活时，系统会判断该组中的其它接口是否已经和IRF端口绑定（可以绑定到同一IRF端口，也可以绑定到不同IRF端口），如果没有绑定，则不允许激活。

【举例】

\# 在处于独立运行模式的设备上将IRF端口1和IRF物理端口Ten-GigabitEthernet1/0/1绑定。

\<Sysname\> system-view

Sysname irf-port 1

Sysname-irf-port1 port group interface ten-gigabitethernet 1/0/1

\# 将IRF中的成员设备（编号为1）的IRF物理端口Ten-GigabitEthernet1/1/0/1和IRF端口1绑定。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/1/0/1

Sysname-Ten-GigabitEthernet1/1/0/1 shutdown

Sysname-Ten-GigabitEthernet1/1/0/1 quit

Sysname irf-port 1/1

Sysname-irf-port 1/1 port group interface ten-gigabitethernet 1/1/0/1

Sysname-irf-port 1/1 quit

Sysname interface ten-gigabitethernet 1/1/0/1

Sysname-Ten-GigabitEthernet1/1/0/1 undo shutdown

【相关命令】

·**irf-port**

**IRF \-- IRF3配置命令 \-- associate**

------------------------------------------------------------------------

**[associate**]命令用来给PEX设备分配虚拟框号/虚拟槽位号。

**[undo associate**]命令用来取消指定PEX设备的虚拟框号/虚拟槽位号配置。

【命令】

**[associate **]*[associated-id*]{.TableTextChar}

**[undo associate**]

【缺省情况】

没有给任何PEX设备分配虚拟框号/虚拟槽位号。

【视图】

PEX端口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*associated-id*{.TableTextChar}：表示给PEX设备分配的虚拟框号/虚拟槽位号。该参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

当父设备为分布式设备组成的IRF时，使用该命令配置的为虚拟框号；当父设备为集中式设备组成的IRF时，使用该命令配置的为虚拟槽位号。关于虚拟框号和虚拟槽位号的详细介绍请参见"虚拟化技术配置指导"中的"IRF3"。

在为PEX设备分配虚拟框号/虚拟槽位号时：

·虚拟框号/虚拟槽位号可配置的值还与PEX设备的型号有关，如果配置的值大于PEX设备允许配置的最大值，则会配置失败。

·一个虚拟框号/虚拟槽位号只能分配给一个PEX设备。

·同一PEX端口视图下多次执行该命令，新配置会覆盖旧配置。

·如果PEX设备已经正常启动，修改或删除该PEX设备的虚拟框号/虚拟槽位号会导致该PEX设备自动重启。

·在PEX设备启动过程中，不允许修改虚拟框号/虚拟槽位号。

【举例】

\# 为PEX端口2相连的PEX设备分配虚拟框号100。

\<Sysname\> system-view

Sysname pex-port 2

Sysname-pex-port2 associate 100

\# 为PEX端口2相连的PEX设备分配虚拟槽位号101。

\<Sysname\> system-view

Sysname pex-port 2

Sysname-pex-port2 associate 101

**IRF \-- IRF3配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来为PEX端口配置描述信息。

**[undo description**]用来恢复缺省情况。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

PEX端口的描述信息为"pex-port *pex-number*"，比如pex-port 0002。

【视图】

PEX端口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：表示PEX端口的描述信息，为1～79个字符的字符串，区分大小写。

【举例】

\# 配置编号为2的PEX端口的描述信息为"connettodep2"。

\<Sysname\> system-view

Sysname pex-port 2

Sysname-pex-port2 description connettodep2

**IRF \-- IRF3配置命令 \-- display pex working-mode (Centralized IRF devices)**

------------------------------------------------------------------------

**[display pex working-mode**]命令用来显示设备的工作模式。

【命令】

**[display pex working-mode **[{ **all** \| **slot** *slot-number1* [ **to** *slot-number2* ] }]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有的设备。

**[slot** *slot-number1*]：表示成员设备的编号或者PEX设备的虚拟槽位号。

**[slot** *slot-number1* **to** *slot-number2*]：表示多个成员设备或者PEX设备。*slot-number1*表示起始编号，*slot-number2*表示结束编号，*slot-number2*的值应大于等于*slot-number1*的值。

【举例】

\# 显示设备的工作模式。

\<Sysname\> display pex working-mode all

Parent device mode Configuration:

  Auto mode:

    Slots 1 to 3

  Switch mode:

    None

  PEX mode at startup:

    None

PEX device mode Configuration:

  Switch mode at startup:

    None

  PEX mode at startup:

    Slots 100 to 103

表1-13  display pex working-mode{.FigureDescriptionChar}命令显示{.FigureDescriptionChar}信息描述表

字段

描述

Parent device mode Configuration

给非PEX设备配置的工作模式

Auto mode

表示配置的为auto模式

Switch mode

表示配置的为switch模式

PEX mode at startup

表示配置的为PEX模式。非PEX设备切换到PEX模式需要手工重启后才能生效

PEX device mode Configuration

给PEX设备配置的工作模式

Switch mode at startup

表示配置的为switch模式。PEX切换到switch模式需要手工重启后才能生效

PEX mode at startup

表示配置的为pex模式

**IRF \-- IRF3配置命令 \-- display pex working-mode (Distributed devices--In IRF mode)**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display pex working-mode**]命令用来显示PEX设备的工作模式。

【命令】

**[display pex working-mode **[{ **all** \| **chassis** *chassis-number* **slot** *slot-number1* [ **to** *slot-number2* ] }]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有的PEX设备。

**[chassis ***chassis-number* **slot** *slot-number1* [ **to** *slot-number2* ]]：表示PEX设备所在位置。其中：

·**chassis ***chassis-number*：表示PEX设备对应的虚拟框号。

·**slot** *slot-number1*：表示PEX设备对应的槽位号。

·**to ***slot-number2*：表示多个PEX设备。*slot-number1*表示起始PEX设备对应的槽位号，*slot-number2*表示结束PEX设备对应的槽位号，*slot-number2*的值应大于等于*slot-number1*的值。

【使用指导】

设备工作在IRF模式才支持该命令。

【举例】

\# 显示PEX设备的工作模式。

\<Sysname\> display pex working-mode all

PEX device mode Configuration:

  Switch mode at startup:

    None

  PEX mode at startup:

    Chassis 101 slots 0

表1-14  display pex working-mode{.FigureDescriptionChar}命令显示{.FigureDescriptionChar}信息描述表

字段

描述

PEX device mode Configuration

给PEX设备配置的工作模式

Switch mode at startup

表示配置的为switch模式。PEX切换到switch模式需要手工重启后才能生效

PEX mode at startup

表示配置的为pex模式

**IRF \-- IRF3配置命令 \-- display pex-port**

------------------------------------------------------------------------

**[display pex-port**]命令用来显示已创建的PEX端口的相关信息。

【命令】

**[display pex-port**** *pex-port-id* ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[pex-port-id*]：显示指定编号的PEX端口的相关信息。不指定该参数时，显示所有已创建的PEX端口的相关信息。

**[verbose**]：显示PEX端口的详细信息。不指定该参数时，显示PEX端口的简要信息。

【举例】

\# 显示所有PEX端口的简要信息。（集中式IRF设备）

\<Sysname\> display pex-port

PEX port 2:

  Status: Online

  Associated ID: Slot 100

  Description: pex-port 0002

PEX port 3:

  Status: Offline

  Associated ID: Slot 101

  Description: pex-port 0003

\# 显示所有PEX端口的详细信息。（集中式IRF设备）

\<Sysname\> display pex-port verbose

PEX port 2:

   Status: Online

   Associated ID: Slot 100

   Description: pex-port 0002

   Member port count: 3

   Member port        Status          Peer port

   XGE1/0/2           Down            \--

   XGE1/0/3           Down            \--

   XGE1/0/4           Blocked         \--

\# 显示所有PEX端口的简要信息。（分布式设备－IRF模式）

\<Sysname\> display pex-port

PEX port 2:

  Status: Online

  Associated ID: Chassis 100

  Description: pex-port 0002

PEX port 3:

  Status: Offline

  Associated ID: Chassis 101

  Description: pex-port 0003

\# 显示所有PEX端口的详细信息。（分布式设备－IRF模式）

\<Sysname\> display pex-port verbose

PEX port 2:

   Status: Online

   Associated ID: Chassis 100

   Description: pex-port 0002

   Member port count: 3

   Member port        Status          Peer port

   XGE1/1/0/2          Down            \--

   XGE1/1/0/3          Down            \--

   XGE1/1/0/4          Blocked         \--

表1-15 display pex-port verbose命令显示信息描述表

字段

描述

PEX port 2

编号为2的PEX端口的相关信息

Status

PEX设备的状态信息，取值如下：

·Online：表示PEX设备在线

·Offline：表示PEX设备不在线

·Loading：表示PEX设备正在启动

Associated ID

PEX端口绑定的虚拟槽位号。当显示为Not configured时，表示该PEX端口没有配置虚拟槽位号（集中式IRF设备）

PEX端口对应的虚拟框号。当显示为Not configured时，表示该PEX端口没有配置虚拟框号（分布式设备－IRF模式）

Description

PEX端口的描述信息

Member port

父设备上的PEX物理接口

Status

PEX端口内的成员端口状态，取值如下：

·Forwarding：表示物理链路可转发业务报文

·Down：表示物理链路是断开的

·Blocked：表示物理链路停止转发业务报文

Peer port

PEX设备上的PEX物理端口的名称，当没有获取到该接口的名称时，该字段显示为"\--"

No member ports.

表示该PEX端口没有绑定PEX物理接口

**IRF \-- IRF3配置命令 \-- pex working-mode (Centralized IRF devices)**

------------------------------------------------------------------------

**[pex working-mode**]命令用来配置设备的工作模式。

**[undo pex working-mode**]命令用来恢复缺省情况。

【命令】

**[pex working-mode**[ { **auto** \| **pex** \| **switch** } { **all** \| **slot** *slot-number1* [ **to** *slot-number2* ] }]]

**[undo pex working-mode**[ { **all** \| **slot** *slot-number1* [ **to** *slot-number2* ] }]]

【缺省情况】

非PEX设备的缺省方式是auto模式，即支持自动切换为PEX设备；PEX设备的工作模式是PEX模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示允许设备根据组网环境自动切换到PEX模式。

**[pex**]：表示将设备的工作模式强制设置为PEX模式。

**[switch**]：表示将设备的工作模式强制设置为switch模式。

**[all**]：当和**auto**关键字配合使用时，**all**表示所有非PEX设备；当和**pex**或者**switch**关键字配合使用时，**all**表示所有成员设备以及PEX设备。

**[slot** *slot-number1*]：当和**auto**关键字配合使用时，*slot-number1*表示成员设备的编号；当和**pex**或者**switch**关键字配合使用时，*slot-number1*表示成员设备的编号或者PEX设备的虚拟槽位号。

**[slot** *slot-number1* **to** *slot-number2*]：表示同时修改多个成员设备或者PEX设备的工作模式。*slot-number1*表示起始成员设备的编号或者PEX设备的虚拟槽位号，*slot-number2*表示结束成员设备的编号或者PEX设备的虚拟槽位号，*slot-number2*的值应大于等于*slot-number1*的值。

【使用指导】

该命令只对当前存在的设备生效。如果指定的**slot**上并没有接入设备，命令也可以配置成功，但是不生效。当该**slot**上重新接入时，请重新配置该命令。

关于各模式的详细描述请参见"虚拟化技术配置指导"中的"IRF"。

【举例】

\# 所有设备当前处于switch模式，将所有设备的工作模式设置为auto模式。

\<Sysname\> system-view

Sysname pex working-mode auto all

Are you sure you want to enable auto mode? In auto mode, the device will automatically reboot to enable PEX mode when the connection to the parent device goes up, but PEX device doesn\'t suppport this command. Y/N: y

**IRF \-- IRF3配置命令 \-- pex working-mode (Distributed devices--In IRF mode)**

------------------------------------------------------------------------

![说明](IRF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[pex working-mode**]命令用来配置PEX设备的工作模式。

**[undo pex working-mode**]命令用来恢复缺省情况。

【命令】

**[pex working-mode**[ **switch** { **all** \| **chassis** *chassis-number* **slot** *slot-number1* [ **to** *slot-number2* ] }]]

**[undo pex working-mode **[{ **all** \| **chassis** *chassis-number* **slot** *slot-number1* [ **to** *slot-number2* ] }]]

【缺省情况】

PEX设备的工作模式是PEX模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[switch**]：表示将PEX设备的工作模式强制设置为switch模式。

**[all**]：表示将所有相连的PEX设备的工作模式强制设置为switch模式。

**[chassis ***chassis-number* **slot** *slot-number1* [ **to** *slot-number2* ]]：表示PEX设备所在位置。其中：

·**chassis ***chassis-number*：表示PEX设备对应的虚拟框号。

·**slot** *slot-number1*：表示PEX设备对应的槽位号。

·**to ***slot-number2*：表示多个PEX设备。*slot-number1*表示起始PEX设备对应的槽位号，*slot-number2*表示结束PEX设备对应的槽位号，*slot-number2*的值应大于等于*slot-number1*的值。

【使用指导】

设备工作在IRF模式才支持该命令。

如果某PEX要退出IRF3网络，作为一台交换机独立运行，请使用该命令，将PEX设备的工作模式配置为switch模式。配置switch模式后，需要手动重启该PEX设备，配置才会生效。

当PEX设备切换到switch模式，第一次重启成功后，设备会工作在switch模式。此时，请保存当前配置，否则，设备再一次重启时会遵循启动配置文件中的模式。

该命令只对当前存在的设备生效。如果指定的**slot**上并没有接入设备，命令也可以配置成功，但是不生效。当该**slot**上重新接入时，请重新配置该命令。

【举例】

\# 将PEX设备（所在位置为chassis 100 slot 0）的工作模式设置为switch模式。

\<Sysname\> system-view

Sysname pex working-mode switch chassis 100 slot 0

Are you sure you want to force a change to switch mode? In forced switch mode, the device can\'t change to PEX mode automatically. Y/N: y

If you want to change parent device to PEX mode or change PEX device to switch mode, you must reboot the device.

**IRF \-- IRF3配置命令 \-- port group interface**

------------------------------------------------------------------------

**[port group interface**]用来将PEX端口和父设备上的PEX物理端口绑定。

**[undo port group interface**]用来取消指定绑定。

【命令】

**[port group interface** *interface-type interface-number*]

**[undo port group interface ***interface-name*]

【缺省情况】

PEX端口没有和任何PEX物理端口绑定。

【视图】

PEX端口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：表示PEX物理端口的类型和编号。各设备型号上可用作PEX物理端口的接口请参见产品相关手册。

interface-name：物理端口的名称，格式为*interface-typeinterface-number*。*interface-type*表示接口名称，*interface-number*表示接口编号，*interface-type*和*interface-number*中间不允许有空格。

【使用指导】

·一个PEX端口用来管理一个PEX设备，和同一个PEX端口绑定的多个PEX物理端口只能连接到同一个PEX设备，这些物理端口之间互为备份，自动实现流量的负载分担。

·PEX物理端口和PEX端口绑定后，该物理端口下绑定前的所有配置将恢复到缺省情况。

·多次执行该命令可以将多个PEX物理端口绑定到一个PEX端口中，最多可绑定的物理端口数与设备型号有关，请以设备的实际情况为准。

·一个PEX物理端口只能和一个PEX端口绑定。

·如果PEX设备已经正常启动，关闭（执行**shutdown**命令）PEX端口中最后一个处于Forwarding状态的物理端口，会导致对应的PEX设备重启。

·有些接口板出厂时已将物理端口分组（包括40GE和100GE接口拆分出来的10GE接口）：

¡同一组内的物理端口可以只有一个或者几个作为PEX物理端口，但建议绑定到一个PEX端口或者提前进行PEX端口的规划。否则，绑定的时候，可能会导致该组物理接口已连接的PEX设备重启。

¡如果同一组内的某个物理端口已经和IRF端口绑定，则其它物理端口不能和PEX端口绑定，反之，亦然。

¡当将某组中的一个物理端口和PEX端口绑定时，系统要求先将该组中的所有端口都关闭（执行**shutdown**命令），才能执行**port group interface**命令将PEX端口与该物理端口绑定。再使用**undo shutdown**命令开启该物理端口，该物理端口才能用作PEX物理端口建立连接。

¡取消某组中物理端口和PEX端口的绑定时，需要先使用**shutdown**命令关闭该组的所有物理端口，才能执行**undo port group interface**命令取消PEX端口与该PEX物理端口的绑定关系。再使用**undo shutdown**命令开启该组的物理端口，这些物理端口才能用于报文的转发。

【举例】

\# 将物理端口Ten-GigabitEther1/0/1和PEX 3绑定。

\<Sysname\> system-view

Sysname pex-port 3

Sysname-pex-port3 port group interface ten-gigabitethernet 1/0/1

\# 将物理端口Ten-GigabitEther1/0/6和PEX 4绑定。（Ten-GigabitEther1/0/5～Ten-GigabitEther1/0/８四个接口是一组的）

\<Sysname\> system-view

Sysname interface range name pex interface ten-gigabitethernet 1/0/5 to ten-gigabitethernet 1/0/8

Sysname-if-range-pex shutdown

Sysname-if-range-pex quit

Sysname pex-port 4

Sysname-pex-port4 port group interface ten-gigabitethernet 1/0/6

Sysname-pex-port4 quit

Sysname interface range name pex

Sysname-if-range-pex undo shutdown

Sysname-if-range-pex quit

**IRF \-- IRF3配置命令 \-- pex-port**

------------------------------------------------------------------------

**[pex-port**]命令用来创建PEX端口并进入PEX端口视图。如果PEX端口已经创建，则直接进入PEX端口视图。

**[undo pex-port**]命令用来删除PEX端口。

【命令】

**[pex-port ***pex-port-id*]

**[undo pex-port ***pex-port-id*]

【缺省情况】

没有创建PEX端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pex-port-id*]：表示PEX端口的编号，取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

PEX端口用来配置和管理PEX设备，通过创建PEX端口、绑定成员端口、配置虚拟框号/虚拟槽位号，用户可将与本设备（作为父设备）相连的PEX设备当成一块远程业务板来使用，从而提高了设备的可扩展性。

创建PEX端口时，如果已创建的PEX端口数目已经达到系统最大值，则不允许创建新的PEX端口；删除状态为Online的PEX端口，会导致该端口对应的PEX设备重启。

【举例】

\# 创建编号为2的PEX端口。

\<Sysname\> system-view

Sysname pex-port 2

Sysname-pex-port2
