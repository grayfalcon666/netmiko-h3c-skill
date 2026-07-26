
**设备管理 \-- 设备管理配置命令 \-- bootrom-access enable**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bootrom-access enable**]命令用来设置在系统启动过程中允许访问Boot ROM菜单。

**[undo bootrom-access enable**]命令用来设置在系统启动过程中禁止访问Boot ROM菜单。

【命令】

**[bootrom-access enable**]

**[undo bootrom-access enable**]

【缺省情况】

在系统启动过程中允许访问Boot ROM菜单。

【视图】

用户视图

【缺省用户角色】

network-admin

【使用指导】

缺省情况下，在系统启动过程中，用户在指定时间内按组合键\<Ctrl+B\>可以进入Boot ROM菜单，以便完成系统软件的加载和对存储介质的管理等操作。为防止非法用户访问Boot ROM菜单，用户可以配置禁止访问Boot ROM菜单。配置禁止访问Boot ROM菜单后，在系统启动过程中即使按组合键\<Ctrl+B\>都不会进入Boot ROM菜单，而直接进入命令行配置界面。

【举例】

\# 设置在系统启动过程中禁止访问Boot ROM菜单。

\<Sysname\> undo bootrom-access enable

【相关命令】

·**display bootrom-access**

**设备管理 \-- 设备管理配置命令 \-- brand**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[brand**]命令用来设置主控板的品牌标识。

【命令】

分布式设备－独立运行模式：

**[brand**[ { **hp** \| **h3c** } [ **slot** *slot-number* ]]]

分布式设备－IRF模式：

**[brand **[{ **hp \| h3c** } [ **chassis** *chassis-number* **slot** *slot-number* ]]]

【缺省情况】

主控板品牌标识的缺省情况与主控板的型号有关，请以设备的实际情况为准。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hp**]：表示配置主控板的品牌标识为hp。

**[h3c**]：表示配置主控板的品牌标识为h3c。

**[slot ***slot-number*]：表示主控板所在的槽位号。不指定该参数时，表示对所有主控板进行操作。（分布式设备－独立运行模式）

**[chassis ***chassis-number ***slot*** slot-number*]：表示指定成员设备上的指定主控板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。不指定该参数时，则表示IRF中的所有主控板。（分布式设备－IRF模式）

【使用指导】

修改主控板的品牌标识后，需要重启该主控板，新品牌标识才能生效。

【举例】

\# 修改设备主控板的品牌标识为HP。

\<Sysname\> brand hp

 Configuration will take effect after next reboot, do you want to continue? [Y/N: Y]

 Configuration is successful.

【相关命令】

·**display brand**

**设备管理 \-- 设备管理配置命令 \-- card-mode**

------------------------------------------------------------------------

![说明](设备管理命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[card-mode**]命令用来设置接口卡的工作模式。

【命令】

集中式设备：

**[card-mode slot ***slot-number mode-name*]

分布式设备---独立运行模式/集中式IRF设备：

**[card-mode slot ***slot-number*** subslot ***subslot-number******mode-name*]

分布式设备---IRF模式：

**[card-mode chassis ***chassis-number*** slot** *slot-number* **subslot** *subslot-number* *mode-name*]

【缺省情况】

与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：子卡所在槽位号。（集中式设备）

**[slot** *slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis ***chassis-number* **slot** *slot-number*]：指定成员设备上指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[subslot** *subslot-number*]：子卡所在的子槽位号。

*[mode-name*]：指定接口卡的工作模式。工作模式如下所示，但支持情况与接口卡的型号有关，请以接口卡的实际情况为准。

**[e**]：配置接口卡的工作模式为E模式（包括E1模式和E3模式）。配置后，该接口卡上的所有接口可作为CPOS E3E1融合接口使用。关于CPOS E3E1融合接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[t**]：配置接口卡的工作模式为T模式（包括T1模式和T3模式）。配置后，该接口卡上的所有接口可作为CPOS T3T1融合接口使用。关于CPOS T3 T1融合接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[e1**]：配置接口卡的工作模式为E1模式。配置后，该接口卡上的所有接口可作为CPOS E1接口使用。关于CPOS E1接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[t1**]：配置接口卡的工作模式为T1模式。配置后，该接口卡上的所有接口可作为CPOS T1接口使用。关于CPOS T1接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[e3**]：配置接口卡的工作模式为E3模式。配置后，该接口卡上的所有接口可作为CPOS E3接口使用。关于CPOS E3接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[t3**]：配置接口卡的工作模式为T3模式。配置后，该接口卡上的所有接口可作为CPOS T3接口使用。关于CPOS T3接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[pos**]：配置接口卡的工作模式为POS模式。配置后，该接口卡上的所有接口可作为POS接口使用。关于POS接口的详细介绍请参见"接口管理配置指导"中"POS接口"。

**[e-cpos**]：配置接口卡的工作模式为E-CPOS模式。配置后，该接口卡上的所有接口可作为2.5Gbps高速CPOS接口使用。关于2.5Gbps高速CPOS接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[oc-3**]：配置接口卡的工作模式为OC-3c/STM-1c（155Mbps)模式。配置后，该接口卡上的所有接口可作为155Mbps高速CPOS接口使用。关于155Mbps高速CPOS接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[oc-12**]：配置接口卡的工作模式为OC-12c/STM-4c（622Mbps）模式。配置后，该接口卡上的所有接口可作为622Mbps高速CPOS接口使用。关于CPOS T3接口的详细介绍请参见"接口管理配置指导"中"CPOS接口"。

**[ipsec**]：配置加密接口卡的加密模式为IPsec模式。

**[ssl**]：配置加密接口卡的加密模式为SSL模式。

**[atm**]：配置接口卡的工作模式ATM模式。配置后，该接口卡上的所有接口可作为ATM接口使用。关于ATM接口的详细介绍请参见"接口管理配置指导"中"ATM接口"。

**[auto**]：表示接口卡自动选择工作在ATM模式或者EFM模式。

**[efm**]：配置接口卡的工作模式EFM（Ethernet First Mile）模式。配置后，该接口卡上的所有接口可作为EFM接口使用。关于EFM接口的详细介绍请参见"接口管理配置指导"中"ATM接口"。

【使用指导】

模式切换后是必须重启设备或热插拔接口卡（如果接口卡支持热插拔），新配置的模式才会生效，还是配置后新模式立即生效，与设备的型号有关，请以设备的实际情况为准。

缺省MDC支持该命令，非缺省MDC不支持。

【举例】

\# 将位于2号槽位的接口卡的工作模式设置为E3模式。（集中式设备）

\<Sysname\> system-view

Sysname card-mode slot 2 e3

Please reboot or hot-swap the board or card (if supported) to make the configuration take effect.

\# 将位于2号槽位的接口卡1的工作模式设置为E3模式。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname card-mode slot 2 subslot 1 e3

Please reboot or hot-swap the board or card (if supported) to make the configuration take effect.

\# 将位于成员设备1的2号槽位的接口卡1的工作模式设置为E3模式。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname card-mode chassis 1 slot 2 subslot 1 e3

Please reboot or hot-swap the board or card (if supported) to make the configuration take effect.

\# 将位于0号槽位的ATM接口卡的工作模式设置为EFM模式。

\<Sysname\> system-view

Sysname card-mode slot 0 efm

Please reboot or hot-swap the board or card (if supported) to make the configuration take effect.

**设备管理 \-- 设备管理配置命令 \-- clock datetime**

------------------------------------------------------------------------

**[clock datetime**]命令用来设置设备的UTC（Coordinated Universal Time，国际协调时间）时间。

【命令】

**[clock datetime** *time date*]

【缺省情况】

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：设置的时间，格式为HH:MM:SS（小时:分钟:秒），HH取值范围为0～23，MM和SS取值范围为0～59。如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。比如将*time*参数设置为0表示零点。

*[date*]：设置的日期，格式为MM/DD/YYYY（月/日/年）或者YYYY/MM/DD（年/月/日），MM的取值范围为1～12，DD的取值范围与月份有关，YYYY的取值范围为2000～2035。

【使用指导】

命令行配置的系统时间由配置的UTC时间、本地时区和夏令时运算之后联合决定，通过**display clock**命令可以查看。

为了保证与其它设备协调工作，为了更好的监控和维护设备，请将系统时间配置准确。用户可使用该命令来配置系统时间，或者通过NTP、PTP协议获取系统时间。

【举例】

\# 设置设备的UTC时间为2012年1月1日8时8分8秒。

\<Sysname\> clock datetime 8:8:8 1/1/2012

\# 设置设备的UTC时间为2012年1月1日8时10分。

\<Sysname\> clock datetime 8:10 2012/1/1

【相关命令】

·**clock protocol**

·**clock summer-time**

·**clock timezone**

·**display clock**

**设备管理 \-- 设备管理配置命令 \-- clock protocol**

------------------------------------------------------------------------

**[clock protocol**]命令用来配置获取系统时间的方式。

**[undo clock protocol**]命令用来恢复缺省情况。

【命令】

**[clock protocol **[{ **none** \| { **ntp** \| **ptp** } **mdc** *mdc-id* }]]

**[undo clock protocol**]

【缺省情况】

由缺省MDC通过的NTP协议获取系统时间。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[none**]：表示通过本地时钟源获取系统时间。配置该参数后，用户可通过**clock datetime**、**clock timezone**、**clock summer-time**命令修改系统时间。

**[ptp**]：表示通过PTP（Precision Time Protocol，精确时间协议）协议获取系统时间。配置该参数后，用户不能通过命令行修改系统时间，需要配置PTP的相关参数才能获取到时钟。关于PTP的详细介绍和配置，请参见"网络管理和监控配置指导"中的"PTP"。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ntp**]：表示通过NTP（Network Time Protocol，网络时间协议）协议获取系统时间。配置该参数后，用户不能通过命令行修改系统时间，需要配置NTP的相关参数才能获取到时钟。关于NTP的详细介绍和配置，请参见"网络管理和监控配置指导"中的"NTP"。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mdc **]*mdc-id*：表示时钟的来源MDC编号。本参数的支持情况以及取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

所有MDC共用一个时钟源，系统时间相同。这个共用时钟源可以是：

·本地时钟源，设备上的晶体振荡器产生的时钟信号。

·网络时钟源，通过协议从其它网络设备上获取的时钟信号。设备根据用户的配置，从指定的MDC，使用指定的协议获取时间后，同步给其它MDC作为系统时间。

多次使用该命令配置不同的系统时间获取方式时，新配置将覆盖旧配置。

【举例】

\# 配置通过本地时钟源获取系统时间。

\<Sysname\> system-view

Sysname clock protocol none

**设备管理 \-- 设备管理配置命令 \-- clock summer-time**

------------------------------------------------------------------------

**[clock summer-time**]命令用来设置夏令时。

**[undo clock summer-time**]命令用来恢复缺省情况。

【命令】

**[clock summer-time** *name* *start-time* *start-date end-time* *end-date* *add*-*time*]

**[undo clock summer-time**]

【缺省情况】

没有配置夏令时。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[name*]：夏令时的名称，为1～32个字符的字符串，区分大小写。

*[start-time*]：开始时间，格式为HH:MM:SS，HH取值范围为0～23，MM和SS取值范围为0～59。如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。

*[start-date*]：开始日期，有两种输入方式：

·直接一次性输入月和日，参数格式为MM/DD，MM取值范围为1～12，DD的取值范围与月份有关。

·分次输入月、日，各参数之间以\<空格\>键隔开。首先输入开始的月份，取值如下：**January**、**February**、**March**、**April**、**May**、**June**、**July**、**August**、**September**、**October**、**November**或**December**；然后输入开始的星期，用当月的第几个星期表示，取值如下：**first**、**second**、**third**、**fourth**、**fifth**或**last**；最后输入起始日，取值为**Sunday**、**Monday**、**Tuesday**、**Wednesday**、**Thursday**、**Friday**或**Saturday**。

*[end-time*]：结束时间，格式为HH:MM:SS，HH取值范围为0～23，MM和SS取值范围为0～59。如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。

*[end-date*]：结束日期，有两种输入方式：

·直接一次性输入月日，参数格式为MM/DD，MM取值范围为1～12，DD的取值范围与月份有关。

·分次输入月、日，各参数之间以\<空格\>键隔开。首先输入开始的月份，取值如下：**January**、**February**、**March**、**April**、**May**、**June**、**July**、**August**、**September**、**October**、**November**或**December**；然后输入开始的星期，用当月的第几个星期表示，取值如下：**first**、**second**、**third**、**fourth**、**fifth**或**last**；最后输入起始日，取值为**Sunday**、**Monday**、**Tuesday**、**Wednesday**、**Thursday**、**Friday**或**Saturday**。

*[add-time*]：偏移时间，格式为HH:MM:SS，HH取值范围为0～23，MM和SS取值范围为0～59。如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。

【使用指导】

命令行配置的系统时间由配置的UTC时间、本地时区和夏令时运算之后联合决定，通过**display clock**命令可以查看。为了保证与其它设备协调工作，为了更好的监控和维护设备，请将所有网络设备的夏令时配置保持一致。

【举例】

\# 设置夏令时PDT，从每年的8月1日的06:00:00开始，到9月1日的06:00:00结束，比当前设备标准时间增加1小时。

\<Sysname\> system-view

Sysname clock summer-time PDT 6 08/01 6 09/01 1

【相关命令】

·**clock datetime**

·**clock timezone**

·**display clock**

**设备管理 \-- 设备管理配置命令 \-- clock timezone**

------------------------------------------------------------------------

**[clock timezone**]命令用来对本地时区进行设置。

**[undo clock timezone**]命令用来恢复缺省情况。

【命令】

**[clock timezone**[ *zone-name* { **add** \| **minus** } *zone-offset*]]

**[undo clock timezone**]

【缺省情况】

本地时区采用UTC时区。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[zone-name*]：时区名称，为1～32个字符的字符串，区分大小写。

**[add**]：在UTC时间的基础上增加指定时间。

**[minus**]：在UTC时间的基础上减少指定时间。

*[zone-offset*]：与UTC的时间差，格式为HH:MM:SS，HH取值范围为0～23，MM和SS取值范围为0～59，如果要设置成整分，则可以不输入秒；如果要设置成整点，则可以不输入分和秒。

【使用指导】

命令行配置的系统时间由配置的UTC时间、本地时区和夏令时运算之后联合决定，通过**display clock**命令可以查看。为了保证与其它设备协调工作，为了更好的监控和维护设备，请将所有网络设备的时区和当地地理时区保持一致。

【举例】

\# 设置本地时区名称为Z5，比UTC标准时间增加5小时。

\<Sysname\> system-view

Sysname clock timezone Z5 add 5

【相关命令】

·**clock datetime**

·**clock summer-time**

·**display clock**

**设备管理 \-- 设备管理配置命令 \-- command**

------------------------------------------------------------------------

**[command**]命令用来为Job分配命令。

**[undo command**]命令用来取消为Job分配的命令。

【命令】

**[command ***id command*]

**[undo command ***id*]

【缺省情况】

没有为Job分配命令。

【视图】

Job视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[id*]：命令编号，取值范围为0～4294967295。该编号表示命令在Job中的执行顺序，编号小的命令优先执行。

*[command*]：为Job分配的命令。

【使用指导】

多次输入**command**命令可以为当前Job分配多条命令，不同命令用编号来唯一区别。如果新分配命令的编号和已分配的某命令的编号相同，则新分配的命令会覆盖已分配的命令。

通过**command**分配的命令行必须是设备上可成功执行的命令行，不包括**telnet**、**ftp**、**ssh2**和**monitor process**。由用户保证配置的正确性，否则，命令行不能自动被执行。

如果需要分配的命令（假设为A）是用户视图下的命令，则直接使用**command**命令分配即可，比如：command 1 display interface；如果需要分配的命令（假设为A）是非用户视图下的命令，则必须先分配进入A所在视图的命令（指定较小的*id*值），再分配A。比如：要使用Job定时执行**shutdown**命令，则需执行三次**command**命令，分别分配**system-view**、**interface**、**shutdown**命令，且各**command**命令的*id*值逐渐增大。

【举例】

\# 为Job（假设名称为backupconfig）分配命令，以便将配置文件startup.cfg备份到TFTP服务器192.168.100.11。

\<Sysname\> system-view

Sysname scheduler job backupconfig

Sysname-job-backupconfig command 2 tftp 192.168.100.11 put flash:/startup.cfg backup.cfg

\# 为Job（假设名称为shutdownGE）分配命令，以便将接口GigabitEthernet1/0/1关闭。

\<Sysname\> system-view

Sysname scheduler job shutdownGE

Sysname-job-shutdownGE command 1 system-view

Sysname-job-shutdownGE command 2 interface gigabitethernet 1/0/1

Sysname-job-shutdownGE command 3 shutdown

【相关命令】

·**scheduler job**

**设备管理 \-- 设备管理配置命令 \-- copyright-info enable**

------------------------------------------------------------------------

**[copyright-info enable**]命令用来使能显示版权信息。

**[undo copyright-info enable**]命令用来禁止显示版权信息。

【命令】

**[copyright-info enable**]

**[undo copyright-info enable**]

【缺省情况】

显示版权信息处于使能状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能显示版权信息。

\<Sysname\> system-view

Sysname copyright-info enable

·使用Telnet方式登录设备，会显示如下信息：

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.\*

\* Without the owner\'s prior written consent,                               \*

\* no decompiling or reverse-engineering shall be allowed.                  \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\<Sysname\>

·如果当前已经使用Console口登录设备了，再退出用户视图重新登录，会显示如下信息：

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.\*

\* Without the owner\'s prior written consent,                               \*

\* no decompiling or reverse-engineering shall be allowed.                  \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

User interface con0 is available.

Press ENTER to get started.

\# 禁止显示版权信息。

\<Sysname\> system-view

Sysname undo copyright-info enable

·使用Telnet方式登录设备，会显示如下信息：

\<Sysname\>

·如果当前已经使用Console口登录设备了，再退出用户视图重新登录，会显示如下信息：

User interface con0 is available.

Press ENTER to get started.

**设备管理 \-- 设备管理配置命令 \-- display alarm**

------------------------------------------------------------------------

![说明](设备管理命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display alarm**]命令用来显示设备的告警信息。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[display alarm ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display alarm ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省级别】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot ***slot-number*]：取值为0，暂无意义。（集中式设备）

**[slot*** slot-number*]：显示指定单板的告警信息。*slot-number*表示单板所在的槽位号。不指定该参数时，则表示所有单板。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的告警信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，则表示所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备或者PEX的告警信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，则表示所有成员设备/PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot*** slot-number*]：显示指定单板的告警信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定单板/PEX的告警信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示IRF中的所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的告警信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示设备的告警信息。（集中式设备）

\<Sysname\> display alarm

Slot CPU Level   Info

0    0   ERROR   faulty

表1-1 display alarm命令显示信息描述表（集中式设备）

字段

描述

Slot

取值为0，暂无意义（如果显示为"-"，则表示产生告警的元件位于机框上）

CPU

告警CPU的编号

Level

告警的级别，级别由高到低依次为ERROR、WARNING、NOTICE、INFO

Info

告警的详细信息。取值为：

·faulty：表示单板处于faulty状态（该单板可能正在启动，或者当前处于故障状态）

·Fan *n* is absent：风扇*n*当前不在位

\# 显示设备的告警信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display alarm

Slot CPU Level   Info

2    0   ERROR   faulty

5    0   ERROR   faulty

8    1   ERROR   faulty

表1-2 display alarm命令显示信息描述表

字段

描述

Slot

产生告警的单板所在的槽位号（如果显示为"-"，则表示产生告警的元件位于机框上）（分布式设备－独立运行模式）

产生告警的成员设备的编号（如果显示为"-"，则表示产生告警的元件位于机框上）（集中式IRF设备）

CPU

告警单板的CPU编号

Level

告警的级别，级别由高到低依次为ERROR、WARNING、NOTICE、INFO

Info

告警的详细信息。取值为：

·faulty：表示单板处于faulty状态（该单板可能正在启动，或者当前处于故障状态）

·Fan *n* is absent：风扇*n*当前不在位

·Power *n* is absent：电源*n*当前不在位

·The temperature of sensor *n* exceeds the lower limit：传感器*n*的温度低于低温门限

·The temperature of sensor *n* exceeds the upper limit：传感器*n*的温度高于高温门限

\# 显示设备当前告警信息。（分布式设备－IRF模式）

\<Sysname\> display alarm

Chassis  Slot  CPU  Level    Info

1        6     0    ERROR    Fan 2 is absent.

1        6     0    ERROR    Power 2 is absent.

1        6     1    ERROR    The board in slot 10 is faulty.

2        3     1    WARNING  The temperature of sensor 3 exceeds the lower limit.

表1-3 display alarm命令显示信息描述表（分布式设备－IRF模式）

字段

描述

Chassis

告警设备的成员编号

Slot

告警单板所在的槽位号

CPU

告警单板的CPU编号

Level

告警的级别，级别由高到低依次为ERROR、WARNING、NOTICE、INFO

Info

告警的详细信息。取值为：

·Fan *n* is absent：风扇*n*当前不在位

·Power *n* is absent：电源*n*当前不在位

·The board in slot *n* is faulty：*n*号槽位上的单板处于faulty状态（该单板可能正在启动，或者当前处于故障状态）

·The temperature of sensor *n* exceeds the lower limit：传感器*n*的温度低于低温门限

·The temperature of sensor *n* exceeds the upper limit：传感器*n*的温度高于高温门限

**设备管理 \-- 设备管理配置命令 \-- display bootrom-access**

------------------------------------------------------------------------

**[display bootrom-access**]命令用来显示设备启动过程中用户是否可以进入Boot ROM菜单。

【命令】

**[display bootrom-access**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【举例】

\# 显示设备启动过程中用户是否可以进入Boot ROM菜单。

\<Sysname\> display bootrom-access

Bootrom access: Enabled.

【相关命令】

·**bootrom-access enable**

**设备管理 \-- 设备管理配置命令 \-- display brand**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display brand**]命令用来显示主控板的品牌标识。

【命令】

**[display brand**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【举例】

**[\# **]显示设备的品牌标识。

\<Sysname\> display brand

Current BRANDs:

 Slot 0: H3C.

 Slot 1: HP.

New BRANDs:

 Slot 0: HP.

 Slot 1: HP.

以上显示信息中，Current BRANDs表示设备上当前生效的品牌标识；New BRANDs表示通过**brand**命令修改后的品牌标识，该标识在主控板重启后生效。

【相关命令】

·**brand**

**设备管理 \-- 设备管理配置命令 \-- display clock**

------------------------------------------------------------------------

**[display clock**]命令用来显示系统当前的时间、日期、本地时区以及夏令时配置。

【命令】

**[display clock**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 没有配置本地时区时，显示系统当前日期和时间。

\<Sysname\> display clock

10:09:00 UTC Fri 03/16/2012

\# 配置了本地时区Z5后，显示系统当前日期和时间。

\<Sysname\> display clock

15:10:00 Z5 Fri 03/16/2012

Time Zone : Z5 add 05:00:00

\# 配置了本地时区Z5和夏令时PDT后，显示系统当前日期和时间。

\<Sysname\> display clock

15:11:00 Z5 Fri 03/16/2012

Time Zone : Z5 add 05:00:00

Summer Time : PDT 06:00:00 08/01 06:00:00 09/01 01:00:00

【相关命令】

·**clock datetime**

·**clock timezone**

·**clock summer-time**

**设备管理 \-- 设备管理配置命令 \-- display copyright**

------------------------------------------------------------------------

display copyright命令用来显示系统软件和硬件的详细版权信息。

【命令】

**[display copyright**]

【视图】

任意视图

【缺省级别】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

通过查看版权信息，可以获知系统当前使用软件和硬件版本的版权信息、版权的参照标准、版权证书等相关信息。

【举例】

\# 显示详细的软件版权信息。（本显示信息与设备的型号有关，请以设备的实际情况为准，此处略）

\<Sysname\> display copyright

**设备管理 \-- 设备管理配置命令 \-- display cpu-usage**

------------------------------------------------------------------------

**[display cpu-usage**]命令用来显示CPU利用率的统计信息。

【命令】

集中式设备：

**[display cpu-usage**]

分布式设备－独立运行模式/集中式IRF设备：

**[display cpu-usage ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display cpu-usage ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot ***slot-number*]：显示指定单板的CPU利用率的统计信息。*slot-number*表示单板所在的槽位号。不指定该参数时，显示的是所有单板的相应信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的CPU利用率的统计信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示的是所有成员设备的相应信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备或者PEX的CPU利用率的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，显示的是所有成员设备/PEX的相应信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定成员设备指定单板的CPU利用率的统计信息。*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定单板的CPU利用率的统计信息。*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的利用率统计信息。*cpu-number*表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

该命令用于显示最近5秒钟、最近1分钟、最近5分钟CPU利用率的平均值。

【举例】

\# 显示当前CPU利用率统计信息。（集中式设备）

\<Sysname\> display cpu-usage

Unit CPU usage:

       1% in last 5 seconds

       1% in last 1 minute

       1% in last 5 minutes

\# 显示当前CPU利用率统计信息。（分布式设备－独立运行模式）

\<Sysname\> display cpu-usage

Slot 0 CPU 0 CPU usage:

       1% in last 5 seconds

       0% in last 1 minute

       0% in last 5 minutes

Slot 1 CPU 0 CPU usage:

       1% in last 5 seconds

       1% in last 1 minute

       1% in last 5 minutes

\# 显示所有成员设备当前CPU利用率统计信息。（集中式IRF设备）

\<Sysname\> display cpu-usage

Slot 1 CPU 0 CPU usage:

       6% in last 5 seconds

      10% in last 1 minute

       5% in last 5 minutes

Slot 2 CPU 0 CPU usage:

       5% in last 5 seconds

       8% in last 1 minute

       5% in last 5 minutes

\# 显示所有单板CPU利用率统计信息。（分布式设备－IRF模式）

\<Sysname\> display cpu-usage

Chassis 1 Slot 0 CPU 0 CPU usage:

       9% in last 5 seconds

       8% in last 1 minute

       8% in last 5 minutes

Chassis 1 Slot 1 CPU 0 CPU usage:

       5% in last 5 seconds

       4% in last 1 minute

       4% in last 5 minutes

Chassis 2 Slot 0 CPU 0 CPU usage:

       6% in last 5 seconds

       6% in last 1 minute

       6% in last 5 minutes

Chassis 2 Slot 1 CPU 0 CPU usage:

       6% in last 5 seconds

       6% in last 1 minute

       6% in last 5 minutes

表1-4 display cpu-usage命令显示信息描述表

字段

描述

Unit CPU usage

CPU利用率信息（集中式设备）

1% in last 5 seconds

设备启动后，会以5秒为周期计算并记录一次该5秒内的CPU的平均利用率。该字段显示的是最近一个5秒统计周期内CPU的平均利用率

1% in last 1 minute

设备启动后，会以1分钟为周期计算并记录一次该1分钟内的CPU的平均利用率。该字段显示的是最近一个1分钟统计周期内CPU的平均利用率

1% in last 5 minutes

设备启动后，会以5分钟为周期计算并记录一次该5分钟内的CPU的平均利用率。该字段显示的是最近一个5分钟统计周期内CPU的平均利用率

Slot *x* CPU *y* CPU usage

*[x*]号单板上*y*号CPU的CPU利用率信息（分布式设备－独立运行模式）

Slot *x* CPU *y* CPU usage

*[x*]号成员设备上*y*号CPU的CPU利用率信息（集中式IRF设备）

Chassis *x* Slot *y* CPU *z* CPU usage

*[x*]号成员设备*y*号单板上*z*号CPU的CPU利用率信息（分布式设备－IRF模式）

**设备管理 \-- 设备管理配置命令 \-- display cpu-usage configuration**

------------------------------------------------------------------------

**[display cpu-usage configuration**]命令用来显示CPU利用率历史信息记录功能相关配置。

【命令】

集中式设备：

**[display cpu-usage configuration**]

分布式设备－独立运行模式/集中式IRF设备：

**[display cpu-usage configuration** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display cpu-usage configuration** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，显示的是主用主控板上的相应信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，显示的是主设备上的相应信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，显示的是主设备上的相应信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定单板。不指定该参数时，显示的是全局主用主控板上的相应信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：表示指定单板/PEX。*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定该参数时，显示的是全局主用主控板上的相应信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示CPU利用率历史信息记录功能相关配置。

\<Sysname\> display cpu-usage configuration

CPU usage monitor is enabled.

Current monitor interval is 60 seconds.

Current monitor threshold is 90%.

【相关命令】

·**monitor cpu-usage enable**

·**monitor cpu-usage interval**

·**monitor cpu-usage**** threshold**

**设备管理 \-- 设备管理配置命令 \-- display cpu-usage history**

------------------------------------------------------------------------

**[display cpu-usage history**]命令用来以图表方式显示CPU利用率的历史信息。

【命令】

集中式设备：

**[display cpu-usage history** [ **job** *job-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display cpu-usage history ** **job** *job-id* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display cpu-usage history ** **job** *job-id* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[job** *job-id*]：显示指定进程的CPU利用率的历史信息，*job-id*表示进程的编号。不指定该参数时，显示的是整个系统的相应信息（整个系统的CPU利用率等于所有进程CPU利用率之和）。可以使用**display process**命令可以查看当前运行的进程的编号和名称，**display process**命令的详细介绍请参见"网络管理与监控"中的"系统维护与调试"。

**[slot** *slot-number*]：显示指定单板的CPU利用率的历史信息。*slot-number*表示单板所在的槽位号。当不指定**job**和该参数时，显示的是所有单板上所有进程的相应信息；当指定**job**参数，但不指定该参数时，显示的是主用主控板上指定进程的相应信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的CPU利用率的历史信息。*slot-number*表示设备在IRF中的成员编号。当不指定**job**和该参数时，显示的是所有成员设备上所有进程的相应信息；当指定**job**参数，但不指定该参数时，显示的是主设备上指定进程的相应信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备或者PEX的CPU利用率的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，显示的是所有成员设备/PEX的相应信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的CPU利用率的历史信息。*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。当不指定**job**和该参数时，显示的是所有单板上所有进程的相应信息；当指定**job**参数，但不指定该参数时，显示的是全局主用主控板上指定进程的相应信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定单板的CPU利用率的统计信息。*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的利用率的历史信息。*cpu-number*表示CPU的编号。当不指定**job**和该参数时，表示所有CPU。当指定**job**参数，但不指定该参数时，表示默认CPU。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

开启CPU利用率历史记录功能后，系统每隔一定时间（可通过**monitor cpu-usage interval**命令配置）会对CPU的利用率进行采样，并把采样结果保存到历史记录区。通过**display cpu-usage history**命令可以查看到最近60个采样点的值。结果以坐标的形式进行显示，显示信息中：

·纵坐标表示利用率，采用就近显示的原则。比如，利用率的间隔为5％，则实际统计值53％将被显示成55％，实际统计值52％将被显示成50％。

·横坐标表示时间，时间越靠左表示距离当前时间越近。

·用连续的\#号表示该时刻的利用率，某个时间点上最高处的\#号对应的纵坐标值即为该时刻CPU的利用率。

【举例】

\# 以图表方式显示整个系统的CPU利用率的历史记录。

\<Sysname\> display cpu-usage history

[100%\|]

[ 95%\|]

[ 90%\|]

[ 85%\|]

[ 80%\|]

[ 75%\|]

[ 70%\|]

[ 65%\|]

[ 60%\|]

[ 55%\|]

[ 50%\|]

[ 45%\|]

[ 40%\|]

[ 35%\|]

[ 30%\|]

[ 25%\|]

[ 20%\|]

[ 15%\|             \#]

[ 10%\|            ###  \#]

[  5%\|           \########]

     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

              10        20        30        40        50        60  (minutes)

                      cpu-usage (Chassis 1 slot 0 CPU 0) last 60 minutes (SYSTEM)

以上显示信息表明系统（用"SYSTEM"表示，运行在Chassis 1 slot 0 CPU 0上）在最近60分钟内CPU的利用率情况：12分钟前大约为5％，13分钟前大约为10％，14分钟前大约为15％，15分钟前大约为10％，16、17分钟前大约为5％，18分钟前大约为10％，19分钟前大约为5％，其它时间均小于或等于2％。

\# 以图表方式显示编号为1的进程的CPU利用率的历史记录。

\<Sysname\> display cpu-usage history job 1

[100%\|]

[ 95%\|]

[ 90%\|]

[ 85%\|]

[ 80%\|]

[ 75%\|]

[ 70%\|]

[ 65%\|]

[ 60%\|]

[ 55%\|]

[ 50%\|]

[ 45%\|]

[ 40%\|]

[ 35%\|]

[ 30%\|]

[ 25%\|]

[ 20%\|]

[ 15%\|]

[ 10%\|]

[  5%\|                   \#]

     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

              10        20        30        40        50        60  (minutes)

                      cpu-usage (Chassis 1 slot 0 CPU 0) last 60 minutes (scmd)

以上显示信息表明Chassis 1 slot 0 CPU 0上编号为1的进程（进程名为scmd，如果进程名带有""标识则表示它是内核线程）在最近60分钟内CPU的利用率情况：20分钟前大约为5％，其它时间均小于或等于2％。

【相关命令】

·**monitor cpu-usage enable**

·{.TerminalDisplayChar}**monitor cpu-usage interval**

**设备管理 \-- 设备管理配置命令 \-- display device**

------------------------------------------------------------------------

**[display device**]命令用来显示设备信息。

【命令】

集中式设备：

**[display device **[[ **cf-card** \| **flash** \| **harddisk** \| **usb** ]  **cpu** *cpu-number*  [ **subslot** *subslot-number* \| **verbose** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display device **[[ **cf-card** \| **flash** \| **harddisk** \| **usb**]  **slot** *slot-number* [ **cpu** *cpu-number*   **subslot** m*subslot-number*  \| **verbose** ]]]

分布式设备－IRF模式：

**[display device **[[ **cf-card** \| **flash** \| **harddisk** \| **usb** ]  **chassis** *chassis-number* [ **slot** *slot-number* [ **cpu** *cpu-number*   **subslot** *subslot-number*  ] \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[cf-card**]：显示CF卡的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flash**]：显示Flash的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[harddisk**]：显示硬盘的信息。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[usb**]：显示USB接口的信息。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[chassis ***chassis-number*]：显示指定成员设备的详细信息。*chassis-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。该参数仅在分布式设备－IRF模式上有效，其它设备上暂无实际意义。

**[slot** *slot-number*]：显示指定单板的信息。*slot-number*表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的单板的信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备或者PEX的单板的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示所有成员设备/PEX。（集中式IRF设备）（支持IRF3的设备）

**[slot** *slot-number*]：显示指定单板的信息。*slot-number*表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定单板/PEX的信息。*slot-number*表示单板或者PEX所在的槽位号。不指定该参数时，表示所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[subslot** *subslot-number*]：显示指定子卡的信息。*subslot-number*表示子卡所在的子槽位号。不指定该参数时，不会显示子卡的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示设备的详细信息。不指定该参数时，显示设备的简要信息，且此时不会显示防火墙插卡的信息。

**[cpu** *cpu-number*]：显示单板指定CPU的信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

不带**cf-card**、**flash**、**harddisk**和**usb**参数时，显示的是设备上所有单板的信息。

【举例】

\# 显示设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备）

\<Sysname\> display device

Slot brief information:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Slot No.   Brd Type        Brd Status   Software Version

 0         Simware         Master       Simware-V700R001

SubCard information on slot 0:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SSlot No.   Type        Status   Software Version

 1          Simware     Normal   Simware-V700R001

 2          Simware     Normal   Simware-V700R001

 3          NONE        Fault    NONE

 4          NONE        Absent   NONE

 5          NONE        Absent   NONE

 6          NONE        Fault    NONE

 7          Simware     Normal   Simware-V700R001

 8          NONE        Absent   NONE

表1-5 display device命令显示信息描述表（集中式设备）

字段

描述

Slot brief information

单板的概要信息

Slot No.

单板的槽位号

Brd Type

单板的硬件类型

Brd Status

单板的状态：

·Fault表示该槽位单板出错，不能正常启动

·Normal表示该槽位单板处于正常工作状态

Software Version

当前单板上运行的软件版本

SubCard information on slot

单板上子卡的信息

SSlot No.

子卡所在的子槽位号

Type

当前子卡的类型

Status

子卡的状态：

·Fault表示子卡出错，不能正常启动

·Normal表示子卡处于正常工作状态

·Absent表示子卡不存在

Max Ports

单板支持的最大物理端口数

Hardware

当前单板的硬件版本

Driver

当前单板的驱动版本

CPLD

当前单板的CPLD版本

\# 缺省Context下，显示设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）

\<Sysname\> display device

Slot No.   Brd Type     Brd Status     Subslot Num    Sft Ver          Patch Ver

 0         LSQ1MPUA     Standby        0              AAAAAA-0000      None

 1         LSQ1MPUA     Master         0              AAAAAA-0000      None

 2         LSQ1GP12EA   Normal         0              AAAAAA-0000      None

 3         NONE         Absent         0              NONE             None

以上显示信息表明，该分布式设备－独立运行模式上有两块主控板，一块接口板。其中插在0号槽位的是备用主控板，插在1号槽位的是主用主控板，插在2号槽位的是接口板。

\# 非缺省Context下，显示设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）

\<Sysname\> display device

Slot No. CPU No.  Brd Type      Brd Status   Subslot  Sft Ver      Patch Ver   

  6        1      NSQ1FWCEA0    Master        0       M9000-9101   None        

  9        1      NSQ1FWCEA0    Normal        0       M9000-9101   None

以上显示信息表明，该Context中有两个安全引擎，其中插在6号槽位的是主安全引擎，插在9号槽位的是备安全引擎。

表1-6 display device命令显示信息描述表（分布式设备－独立运行模式）

字段

描述

Slot No.

单板的槽位号

CPU No.

安全引擎的CPU编号（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）

Brd Type

单板的硬件类型

Brd Status

单板状态：

·Standby表示该板是备用主控板

·Master表示该板是主用主控板

·Absent表示该槽位没有插入单板

·Fault表示该槽位单板出错，不能正常启动

·Normal表示该槽位单板是接口板并处于正常工作状态

Subslot Num

单板支持子卡的最大个数

Sft Ver

当前单板上运行的软件版本

Patch Ver

当前单板上运行的热补丁版本

\# 显示IRF中各成员设备的设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式IRF设备）

\<Sysname\> display device

Slot 1

SubSNo PortNum PCBVer FPGAVer CPLDVer BootRomVer AddrLM Type       State

0      28      REV.C  NULL    002     505        IVL    MAIN       Normal

1      0       REV.A  NULL    NULL    NULL       IVL    2\*10GE     Normal

Slot 2

SubSNo PortNum PCBVer FPGAVer CPLDVer BootRomVer AddrLM Type       State

0      28      REV.C  NULL    002     503        IVL    MAIN       Normal

1      0       REV.B  NULL    NULL    NULL       IVL    2\*10GE     Normal

以上显示信息表明，该IRF中包含两台成员设备，每台成员设备都拥有28个以太网接口，配置了2个10GE的IRF物理口。

表1-7 display device命令显示信息描述表（集中式IRF设备）

字段

描述

Slot 1

成员编号为1的成员设备的信息

SubSNo

子卡所在的槽位号

PortNum

子卡支持的最大端口数

PCBVer

子卡的PCB版本

FPGAVer

子卡的FPGA版本

CPLDVer

子卡的CPLD版本

BootRomVer

子卡的BootRom版本

AddrLM

地址学习模式

Type

子卡的类型

State

子卡的状态

\# 缺省Context下，显示IRF中各成员设备的设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display device

Chassis   Slot Type         State        Subslot      Soft Ver     Patch Ver

1         0    LSQ1SRP1CB   Master       0            S7500E-0000  None

1         1    NONE         Absent       0            NONE         None

1         2    LSQ1P24XGSC  Normal       0            S7500E-0000  None

1         3    NONE         Absent       0            NONE         None

1         4    LSQ1FV48SA   Normal       0            S7500E-0000  None

2         0    LSQ1SRP2XB   Standby      0            S7500E-0000  None

2         1    LSQ1SRP2XB   Standby      0            S7500E-0000  None

2         2    LSQ1FV48SA   Normal       0            S7500E-0000  None

2         3    LSQ1FV48SA   Normal       0            S7500E-0000  None

2         4    LSQ1P24XGSC  Normal       0            S7500E-0000  None

2         5    SRP2XBSLAVE  Normal       0            S7500E-0000  None

2         6    SRP2XBSLAVE  Normal       0            S7500E-0000  None

以上显示信息表明，该IRF中包含两台成员设备，成员编号分别为1和2。同时还显示了每个框上的单板信息。从单板状态可以看出，成员设备1的0号单板为整个IRF的主用主控板，成员设备2的两个主控板（0号和1号槽位）均为整个IRF的备用主控板。

\# 非缺省Context下，显示IRF中各成员设备的设备信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display device                                                                  

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Blade controller device info \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--      

Chassis  Slot CPU   Type         State    Subslot  Soft Ver     Patch Ver

1        6    1     NSQ1FWCEA0   Master   0        M9000-9101   None        

2        1    1     NSQ1FWCEA0   Normal   0        M9000-9101   None

以上显示信息表明，该Context中包含两个安全引擎，其中成员设备1的6号单板的CPU 1是主安全引擎，成员设备2的1号单板的CPU 1是备安全引擎。

表1-8 display device命令显示信息描述表（分布式设备－IRF模式）

字段

描述

Chassis

设备在IRF中的成员编号

Slot

成员设备上单板所在的槽位号

CPU

安全引擎的CPU编号（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）

Type

单板型号

State

单板的当前状态：

·Absent：单板不在位

·Master：单板为全局主用主控板（即整个IRF的主用主控板）

·Standby：单板为全局备用主控板（即整个IRF的备用主控板）

·Normal：单板为接口板，并且状态正常

·Fault：单板状态异常

Subslot

单板支持子卡的最大个数

Soft Ver

当前单板上运行的软件版本

Patch Ver

当前单板上运行的热补丁版本，None表示没有补丁

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo**

------------------------------------------------------------------------

**[display device manuinfo**]命令用来显示设备的电子标签信息。

【命令】

集中式设备：

**[display device manuinfo** [ **cpu** *cpu-number*   **subslot** *subslot-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display device manuinfo** [ **slot** *slot-number* [ **cpu** *cpu-number*   **subslot** *subslot-number*  ]]]

分布式设备－IRF模式：

**[display device manuinfo ** **chassis** *chassis-number*  **slot** *slot-number* [ **cpu** *cpu-number*   **subslot** *subslot-number*  ] ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：显示指定成员设备的电子标签信息。*chassis-number*表示设备在IRF中的成员编号。不输入该参数时，显示所有成员设备的相应信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*]：显示指定成员设备/虚拟框的电子标签信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号。不输入该参数时，显示所有成员设备/虚拟框的相应信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot** *slot-number*]：显示指定单板的电子标签信息。*slot-number*表示单板所在的槽位号。不输入该参数时，显示所有单板的相应信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定单板的电子标签信息。*slot-number*表示单板所在的槽位号。不输入该参数时，显示所有单板的相应信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定单板/PEX的电子标签信息。*slot-number*表示单板/PEX所在的槽位号。不输入该参数时，显示所有单板/PEX的相应信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备的电子标签信息。*slot-number*表示设备在IRF中的成员编号。不输入该参数时，显示所有成员设备的相应信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的电子标签信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不输入该参数时，显示所有成员设备/PEX的相应信息。（集中式IRF设备）（支持IRF3的设备）

**[subslot** *subslot-number*]：显示指定子卡的电子标签信息。*subslot-number*表示子卡所在的子槽位号。不指定该参数时，不会显示子卡的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cpu** *cpu-number*]：显示指定CPU的电子标签信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

电子标签信息也可以称为永久配置数据或档案信息等，在单板或者设备的调测（调试、测试）过程中被写入到设备的存储器件中，包括单板的名称、生产序列号、MAC地址、制造商等信息。本命令显示的是设备的部分电子标签信息。

【举例】

\# 显示设备的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备）

\<Sysname\> display device manuinfo

Slot 0:

DEVICE_NAME          : aaaa

DEVICE_SERIAL_NUMBER : xxxx

MAC_ADDRESS          : 000F-E26A-58EA

MANUFACTURING_DATE   : 2012-11-10

VENDOR_NAME          : H3C

Slot 1:

The card does not support manufacture information.

\# 显示设备的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）

\<Sysname\> display device manuinfo

Slot 0 CPU 0:

DEVICE_NAME          : LSQ1MPUA0

DEVICE_SERIAL_NUMBER : 210231A73SA07B000108

MAC_ADDRESS          : 000F-E26A-58ED

MANUFACTURING_DATE   : 2012-11-9

VENDOR_NAME          : H3C

Slot 1 CPU 0:

DEVICE_NAME          : LSQ1MPUA0

DEVICE_SERIAL_NUMBER : 210231A73SA07B000075

MAC_ADDRESS          : 000F-E26A-581B

MANUFACTURING_DATE   : 2012-11-10

VENDOR_NAME          : H3C

Slot 2 CPU 0:

DEVICE_NAME          : LSQ1T24XGSC0

DEVICE_SERIAL_NUMBER : 210231A76VX081000020

MAC_ADDRESS          : No

MANUFACTURING_DATE   : 2012-12-2

VENDOR_NAME          : H3C

\# 显示设备的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式IRF设备）

\<Sysname\> display device manuinfo

Slot 1 CPU 0:

DEVICE_NAME          : 3CRS48G-24-91

DEVICE_SERIAL_NUMBER : 9S4F9PLBC3111

MAC_ADDRESS          : 001C-C5BC-3111

MANUFACTURING_DATE   : 2012-05-08

VENDOR_NAME          : H3C

Slot 2 CPU 0:

DEVICE_NAME          : S5500-28C-EI

DEVICE_SERIAL_NUMBER : 210235A252A079000140

MAC_ADDRESS          : 000F-E269-46D1

MANUFACTURING_DATE   : 2012-09-26

VENDOR_NAME          : H3C

表1-9 display device manuinfo命令信息显示描述表

字段

描述

Slot 1 CPU 0

单板所在的槽位号和CPU编号（分布式设备－独立运行模式）

设备的成员编号和CPU编号（集中式IRF设备）

DEVICE_NAME

设备名称

DEVICE_SERIAL_NUMBER

设备序列号

MAC_ADDRESS

设备出厂MAC地址

MANUFACTURING_DATE

设备调测日期

VENDOR_NAME

制造商名称

\# 显示设备的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display device manuinfo

Chassis 1 slot 0 CPU 0:

DEVICE_NAME          : LSQ1MPUA0

DEVICE_SERIAL_NUMBER : 210231A73SA07B000108

MAC_ADDRESS          : 000F-E26A-58ED

MANUFACTURING_DATE   : 2012-11-9

VENDOR_NAME          : H3C

Chassis 1 slot 1 CPU 0:

DEVICE_NAME          : LSQ1MPUA0

DEVICE_SERIAL_NUMBER : 210231A73SA07B000075

MAC_ADDRESS          : 000F-E26A-581B

MANUFACTURING_DATE   : 2012-11-10

VENDOR_NAME          : H3C

Chassis 1 slot 2 CPU 0:

DEVICE_NAME          : LSQ1T24XGSC0

DEVICE_SERIAL_NUMBER : 210231A76VX081000020

MAC_ADDRESS          : No

MANUFACTURING_DATE   : 2012-12-2

VENDOR_NAME          : H3C

表1-10 display device manuinfo命令信息显示描述表

字段

描述

Chassis 1 slot 0 CPU 0

成员设备1上0号单板的0号CPU的相关信息

DEVICE_NAME

设备名称

DEVICE_SERIAL_NUMBER

设备序列号

MAC_ADDRESS

设备出厂MAC地址

MANUFACTURING_DATE

设备调测日期

VENDOR_NAME

制造商名称

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo chassis-only**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display device manuinfo chassis-only**]命令用来显示指定机框背板的电子标签信息。

【命令】

分布式设备－独立运行模式：

**[display device manuinfo chassis-only**]

分布式设备－IRF模式：

**[display device manuinfo chassis** *chassis-number* **chassis-only**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis** *chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number*]：表示设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示机框背板的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）

\<Sysname\> display device manuinfo chassis-only

Chassis self:

DEVICE_NAME          : backplane

DEVICE_SERIAL_NUMBER : 210235A36L1234567890

MAC_ADDRESS          : NONE

MANUFACTURING_DATE   : 2010-01-20

VENDOR_NAME          : H3C

\# 显示成员设备1上机框背板的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display device manuinfo chassis 1 chassis-only

Chassis 1:

Chassis self:

DEVICE_NAME            : backplane

DEVICE_SERIAL_NUMBER   : 210235A36L1234567891

MAC_ADDRESS            : NONE

MANUFACTURING_DATE     : 2010-01-20

VENDOR_NAME            : H3C

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo fan**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display device manuinfo fan**]命令用来显示指定风扇的电子标签信息。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display device manuinfo fan*** fan-id*]

集中式IRF设备：

**[display device manuinfo slot ***slot-number*** fan*** fan-id*]

分布式设备－IRF模式：（不支持IRF3的设备）

**[display device manuinfo chassis** *chassis-number* **fan** *fan-id*]

分布式设备－IRF模式：（支持IRF3的设备）

**[display device manuinfo chassis**[ { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } **fan** *fan-id*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot ***slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]]：*chassis-number*表示设备在IRF中的成员编号；*virtual-chassis-number*表示PEX对应的虚拟框号，*slot-number*表示PEX在虚拟框中的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

*[fan-id*]：表示设备上风扇的ID编号。该参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示风扇2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备/分布式设备－独立运行模式）

\<Sysname\> display device manuinfo fan 2

Fan 2:

DEVICE_NAME          : fan

DEVICE_SERIAL_NUMBER : 210235A36L1234567890

MAC_ADDRESS          : NONE

MANUFACTURING_DATE   : 2010-01-20

VENDOR_NAME          : H3C

\# 显示成员设备1上风扇2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式IRF设备）

\<Sysname\> display device manuinfo fan 2

Slot 1:

Fan 2:

DEVICE_NAME          : fan

DEVICE_SERIAL_NUMBER : 210235A36L1234567890

MAC_ADDRESS          : NONE

MANUFACTURING_DATE   : 2010-01-20

VENDOR_NAME          : H3C

\# 显示成员设备1上风扇2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display device manuinfo chassis 1 fan 2

Chassis 1:

Fan 2:

DEVICE_NAME            : fan2

DEVICE_SERIAL_NUMBER   : 210235A36L1234567891

MAC_ADDRESS            : NONE

MANUFACTURING_DATE     : 2010-01-20

VENDOR_NAME            : H3C

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo power**

------------------------------------------------------------------------

![说明](设备管理命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display device manuinfo power**]命令用来显示指定电源的电子标签信息。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display device manuinfo power** *power-id*]

集中式IRF设备：

**[display device manuinfo slot ***slot-number ***power** *power-id*]

分布式设备－IRF模式：（不支持IRF3的设备）

**[display device manuinfo chassis** *chassis-number* **power** *power-id*]

分布式设备－IRF模式：（支持IRF3的设备）

**[display device manuinfo chassis**[ { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } **power** *power-id*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot ***slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]]：*chassis-number*表示设备在IRF中的成员编号；*virtual-chassis-number*表示PEX对应的虚拟框号，*slot-number*表示PEX在虚拟框中的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

*[power-id*]：表示设备上电源的ID编号，该参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示电源2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备/分布式设备－独立运行模式）

\<Sysname\> display device manuinfo power 2

Power 2:

DEVICE_NAME          : power

DEVICE_SERIAL_NUMBER : 210235A36L1234567890

MAC_ADDRESS          : NONE

MANUFACTURING_DATE   : 2010-01-20

VENDOR_NAME          : H3C

\# 显示成员设备1上电源2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式IRF设备）

\<Sysname\> display device manuinfo slot 1 power 2

Slot 1:

Power 2:

DEVICE_NAME          : power

DEVICE_SERIAL_NUMBER : 210235A36L1234567890

MAC_ADDRESS          : NONE

MANUFACTURING_DATE   : 2010-01-20

VENDOR_NAME          : H3C

\# 显示成员设备1上电源监控模块2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display device manuinfo chassis 1 power 2

Chassis 1:

Power 2:

DEVICE_NAME            : power2

DEVICE_SERIAL_NUMBER   : 210235A36L1234567891

MAC_ADDRESS            : NONE

MANUFACTURING_DATE     : 2010-01-20

VENDOR_NAME            : H3C

**设备管理 \-- 设备管理配置命令 \-- display device manuinfo power-monitor**

------------------------------------------------------------------------

![说明](设备管理命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display device manuinfo power-monitor**]命令用来显示指定电源监控模块的电子标签信息。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display device manuinfo power-monitor** *pm-id*]

集中式IRF设备：

**[display device manuinfo slot ***slot-number ***power-monitor** *pm-id*]

分布式设备－IRF模式：（不支持IRF3的设备）

**[display device manuinfo chassis** *chassis-number* **power-monitor** *pm-id*]

分布式设备－IRF模式：（支持IRF3的设备）

**[display device manuinfo chassis**[ { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } **power-monitor** *pm-id*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot ***slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]]：*chassis-number*表示设备在IRF中的成员编号；*virtual-chassis-number*表示PEX对应的虚拟框号，*slot-number*表示PEX在虚拟框中的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

*[pm-id*]：表示设备上电源监控模块的ID编号，该参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示电源监控模块2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备/分布式设备－独立运行模式）

\<Sysname\> display device manuinfo power-monitor 2

PowerMonitor 2:

DEVICE_NAME          : PowerMonitor

DEVICE_SERIAL_NUMBER : 210235A36L1234567890

MAC_ADDRESS          : NONE

MANUFACTURING_DATE   : 2013-01-20

VENDOR_NAME          : H3C

\# 显示成员设备1上电源监控模块2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式IRF设备）

\<Sysname\> display device manuinfo slot 1 power-monitor 2

Slot 1:

PowerMonitor 2:

DEVICE_NAME          : PowerMonitor

DEVICE_SERIAL_NUMBER : 210235A36L1234567890

MAC_ADDRESS          : NONE

MANUFACTURING_DATE   : 2013-01-20

VENDOR_NAME          : H3C

\# 显示成员设备1上电源监控模块2的电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display device manuinfo chassis 1 power-monitor 2

Chassis 1:

PowerMonitor 2:

DEVICE_NAME            : PowerMonitor

DEVICE_SERIAL_NUMBER   : 210235A36L1234567891

MAC_ADDRESS            : NONE

MANUFACTURING_DATE     : 2013-01-20

VENDOR_NAME            : H3C

**设备管理 \-- 设备管理配置命令 \-- display diagnostic-information**

------------------------------------------------------------------------

**[display diagnostic-information**]命令用来显示系统当前多个功能模块运行的统计信息。

【命令】

**[display diagnostic-information **[[ **hardware** \| **infrastructure** \| **l2** \| **l3** \| **service** ]  *filename* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[hardware**]：收集硬件相关诊断信息。

**[infrastructure**]：收集基础模块的诊断信息。

**[l2**]：收集二层特性相关诊断信息。

**[l3**]：收集三层特性相关诊断信息。

**[service**]：收集上层业务模块相关诊断信息。

*[filename*]：表示将收集到的诊断信息保存到指定文件。*filename*表示文件的名称，后缀必须为".tar.gz"。

【使用指导】

在日常维护或系统出现故障时，为了便于问题定位，用户需要查看各个功能模块的运行信息。因为各个功能模块都有其对应的运行信息，所以一般情况下，用户需要逐条运行相应的**display**命令。为便于一次性收集更多信息，用户可以在任意视图下执行**display** **diagnostic-information**命令，显示系统当前多个功能模块运行的统计信息。

使用该命令，用户可以直接显示指定的诊断信息或者将诊断信息直接保存到指定文件，因为诊断信息较多，系统会自动将该文件压缩后保存，文件名后缀为".tar.gz"。如果要在设备上查看该文件的内容，请使用**tar extract**命令解包后再使用**more**命令查看。

[该命令不支持"**[\|]**]"、"**\>**"和"**\>\>**"参数。

【举例】

\# 显示系统当前各个功能模块运行的统计信息（因为显示信息多，而且跟设备型号有关，请以设备的实际情况为准，此处略）。

\<Sysname\> display diagnostic-information

Save or display diagnostic information (Y=save, N=display)? [Y/N:n]

===============================================

  ===============display clock===============

14:03:55 UTC Thu 01/05/2012

=================================================

  ===============display version=============== 

......略......

\# 将收集到的诊断信息保存到文件test.tar.gz。

·方法一：在交互信息时选择将诊断信息保存到指定文件，并输入文件名test.tar.gz。

\<Sysname\> display diagnostic-information

Save or display diagnostic information (Y=save, N=display)? [Y/N:y]

Please input the file name(\*.tar.gz)[flash:/diag.tar.gz: test.tar.gz]

Diagnostic information is outputting to flash:/test.tar.gz.

Please wait\...

·方法二：在命令行中直接通过参数指定将诊断信息保存到文件test.tar.gz。

\<Sysname\> display diagnostic-information test.tar.gz

Diagnostic information is outputting to flash:/test.tar.gz.

Please wait\...

【相关命令】

·**more**（基础配置命令参考/文件系统管理）

·**tar extract**（基础配置命令参考/文件系统管理）

**设备管理 \-- 设备管理配置命令 \-- display environment**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display environment**]命令用来显示设备上温度传感器的温度信息，包括当前温度和设定的温度告警门限。

【命令】

集中式设备：

**[display environment**]

分布式设备－独立运行模式：

**[display environment**[ [ **slot** *slot-number* \| **vent** ]]]

集中式IRF设备：

**[display environment** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display**[ **environment** [ **chassis** *chassis-number* [ **slot** *slot-number* \| **vent** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis***chassis-number*]：显示IRF中指定成员设备上温度传感器的温度信息。*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis***chassis-number*]：显示IRF中指定成员设备或者PEX上温度传感器的温度信息。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot ***slot-number*]：显示设备中指定单板上的温度传感器的温度信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示设备中指定单板上的温度传感器的温度信息。*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot ***slot-number*]：显示设备中指定单板/PEX上的温度传感器的温度信息。*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot ***slot-number*]：显示IRF中指定成员设备上的温度传感器的温度信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示的是IRF中所有温度传感器的温度信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示IRF中指定成员设备或者PEX上的温度传感器的温度信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，显示的是IRF中所有温度传感器的温度信息。（集中式IRF设备）（支持IRF3的设备）

**[vent**]：显示设备中机框、风扇框上温度传感器的温度信息。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·不指定**slot**和**vent**参数时，显示的是设备上所有温度传感器的温度信息。（分布式设备－独立运行模式）

·不指定**chassis**参数时，显示的是IRF中所有温度传感器的温度信息；指定**chassis**但不指定**slot**和**vent**参数时，显示的是指定成员设备上所有温度传感器的温度信息。（分布式设备－IRF模式）

【举例】

\# 显示设备上所有温度传感器的温度信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（集中式设备）

\<Sysname\> display environment

System temperature information (degree centigrade):

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Slot  Sensor       Temperature  LowerLimit  WarningLimit  AlarmLimit ShutdownLimit

Vent  outflow 1    38           10          40            50          70

0     inflow 1     27           -10         50            70          100

0     hotspot 1    53           10          50            80          100

\# 显示设备上所有温度传感器的温度信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）

\<Sysname\> display environment

System temperature information (degree centigrade):

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Slot  Sensor       Temperature  LowerLimit  WarningLimit  AlarmrLimit ShutdownLimit

Vent  outflow 1    38           10          40            50          100

0     hotspot 1    53           10          50            80          100

0     hotspot 2    52           10          50            80          100

0     outflow 1    39           10          50            80          100

1     hotspot 1    42           10          50            80          100

4     hotspot 1    42           10          50            80          100

\# 显示IRF中所有温度传感器的温度信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> display environment

System temperature information (degree centigrade):

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Slot   Sensor        Temperature LowerLimit WarningLimit AlarmrLimit ShutdownLimit

1/Vent outflow 1     38          10         40           50          70

1/0    inflow  1     27          -10        50           70          100

1/0    hotspot 1     53          10         50           80          100

1/0    hotspot 2     52          10         50           80          100

1/0    outflow 1     39          10         50           80          100

1/1    hotspot 1     42          10         50           80          100

1/4    hotspot 1     42          10         50           80          100

表1-11 display environment命令显示信息描述表

字段

描述

System Temperature information (degree centigrade)

系统温度信息（单位为摄氏度）

sensor

温度传感器

·hotspot：表示热点温度传感器

·inflow：表示入风口温度传感器

·outflow：表示出风口温度传感器

Slot

当显示数字时表示设备上温度传感器的温度信息；当显示Vent时表示位于机框、风扇框上的温度传感器的温度信息（集中式设备）

Slot

当显示数字时表示指定槽位单板上温度传感器的温度信息；当显示Vent时表示位于机框、风扇框上的温度传感器的温度信息（分布式设备－独立运行模式）

Slot

当显示数字时表示指定成员设备上温度传感器的温度信息；当显示Vent时表示位于机框、风扇框上的温度传感器的温度信息（集中式IRF设备）

Slot

当显示*chassis-number*/*slot-number*时表示指定成员设备指定单板上温度传感器的温度信息；当显示*chassis-number*/Vent时表示指定成员设备上位于机框、风扇框上的温度传感器的温度信息（分布式设备－IRF模式）

Temperature

当前温度

LowerLimit

低温告警门限

WarningLimit

一般级（Warning）高温告警门限

AlarmLimit

严重级（Alarm）高温告警门限

ShutdownLimit

关断级（Shutdown）高温告警门限，当温度传感器的温度大于该门限时，设备会自动关闭

**设备管理 \-- 设备管理配置命令 \-- display fabric utilization**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display fabric utilization**]命令用来显示设备接口板上交换芯片的通道利用率信息。

【命令】

分布式设备－独立运行模式:

**[display fabric utilization** [ **slot** *slot-number* ]]

分布式设备－IRF模式:

**[display fabric utilization** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot ***slot-number*]：显示指定单板上交换芯片的通道利用率信息。*slot-number*表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）。

**[chassis ***chassis-number *]**slot ***slot-number*：显示指定成员设备上指定单板的通道利用率信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示所有IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number *]**slot ***slot-number*：显示指定单板或者PEX的通道利用率信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示所有IRF中的所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示5号接口板上交换芯片的通道信息。（分布式设备－独立运行模式）

\<System\> display fabric utilization slot 5

                    Input                         Output

Chs Slot Chan Speed Usage Peak                    Usage Peak

0    5    0    10G    0%   0% 08:13:14 2012/10/30   0%   0% 08:13:14 2012/10/30

0    5    1    10G    0%   0% 08:13:14 2012/10/30   0%   0% 08:13:14 2012/10/30

0    5    2    10G    0%   0% 08:13:14 2012/10/30   0%   0% 08:13:14 2012/10/30

0    5    3    10G    0%   0% 08:13:14 2012/10/30   0%   0% 08:13:14 2012/10/30

\# 显示2号成员设备6号接口板上交换芯片的通道信息。（分布式设备－IRF模式）

\<System\> display fabric utilization chassis 2 slot 6

                    Input                         Output

Chs Slot Chan Speed Usage Peak                    Usage Peak

2    6    0    10G    0%   0% 21:50:27 2012/02/24   0%   0% 21:50:27 2012/02/24

2    6    1    10G    0%   0% 21:50:27 2012/02/24   0%   0% 21:50:27 2012/02/24

2    6    2    10G    0%   0% 21:50:27 2012/02/24   0%   0% 21:50:27 2012/02/24

2    6    3    10G    0%   0% 21:50:27 2012/02/24   0%   0% 21:50:27 2012/02/24

表1-12 display fabric utilization命令显示信息描述表

字段

描述

Chs

取值为0，无实际意义（分布式设备－独立运行模式）

Chassis的缩写，为设备在IRF中的成员编号（分布式设备－IRF模式）

Slot

接口板所在的槽位号

Chan

Channel的缩写，通道号

Speed

通道的速率

Input

入方向的统计数据

Output

出方向的统计数据

Usage

通道利用率

Peak

通道利用率峰值以及峰值发生的时间

**设备管理 \-- 设备管理配置命令 \-- display fan**

------------------------------------------------------------------------

**[display fan**]命令用来显示设备风扇的工作状态。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display fan**[ [ *fan-id \|* **verbose** ]]]

集中式IRF设备：

**[display fan** [ **slot** *slot-number* [ *fan-id*  *\|* **verbose** ]]]

分布式设备－IRF模式：（不支持IRF3的设备）

**[display fan** [ **chassis** *chassis-number* [ *fan-id*  ]  **verbose** ]]

分布式设备－IRF模式：（支持IRF3的设备）

**[display fan**[ [ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } [ *fan-id* ] ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示所有风扇。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示所有风扇。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。不指定**chassis**参数时，表示所有风扇。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]]：显示指定成员设备或者PEX上风扇的状态信息。*chassis-number*表示设备在IRF中的成员编号；*virtual-chassis-number*表示PEX对应的虚拟框号，*slot-number*表示PEX在虚拟框中的槽位号。不指定**chassis**参数时，表示所有风扇。（分布式设备－IRF模式）（支持IRF3的设备）

*[fan-id*]：表示设备内置风扇的编号，是否支持本参数以及本参数的取值范围与设备的型号有关，请以设备的实际情况为准。不指定该参数时，表示指定位置的所有风扇。

**[verbose**]：显示设备内置风扇的详细信息。不指定该参数时，显示设备内置风扇的简要信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示设备上所有风扇的工作状态。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准，此处略）

\<Sysname\> display fan

**设备管理 \-- 设备管理配置命令 \-- display lpu-type**

------------------------------------------------------------------------

![说明](设备管理命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display lpu-type**]命令用来显示设备支持的接口板类型。

【命令】

**[display lpu-type**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示设备支持的接口板类型。

\<Sysname\> display lpu-type

Current LPU type is E series.

LPU type for the next startup is F series.

【相关命令】

·**lpu-type**

**设备管理 \-- 设备管理配置命令 \-- display memory**

------------------------------------------------------------------------

**[display memory**]命令用来显示内存使用情况。

【命令】

集中式设备：

**[display memory**]

分布式设备－独立运行模式/集中式IRF设备：

**[display memory**** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display memory ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号，不指定时显示当前所有单板的内存使用情况。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号，不指定时显示当前所有成员设备的内存使用情况。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定单板，不指定时显示当前所有单板的内存使用情况。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示设备的内存使用情况。

\<Sysname\> display memory

The statistics about memory is measured in KB:

Slot 0:

             Total      Used      Free    Shared   Buffers    Cached   FreeRatio

Mem:        507980    154896    353084         0       488     54488       69.5%

-/+ Buffers/Cache:     99920    408060

Swap:           0         0         0

表1-13 display memory命令显示信息描述表

字段

描述

The statistics about memory is measured in KB:

系统内存使用情况，以下统计信息均以KB为单位

Slot

为固定值0，暂无实际意义（集中式设备）

单板所在的槽位号（分布式设备－独立运行模式）

设备在IRF中的成员编号（集中式IRF设备）

Chassis x Slot x

单板所在的槽位号（分布式设备－IRF模式）

Mem

内存使用信息

Total

系统可分配的物理内存的大小

设备总物理内存分为不可分配物理内存和可分配物理内存。其中，不可分配物理内存用于内核代码段存储、内核管理开销以及ISSU功能运行等；可分配物理内存用于支撑业务模块的运行、文件存储等操作。不可分配内存的大小由设备根据系统运行需要自动计算划分，可分配物理内存的大小等于设备总物理内存减去不可分配内存的大小

Used

整个系统已用的物理内存大小

Free

整个系统可用的物理内存大小

Shared

多个进程共享的物理内存总额

Buffers

已使用的文件缓冲区的大小

Cached

高速缓冲寄存器已使用的内存大小

FreeRatio

整个系统物理内存的空闲率

-/+ buffers/cache

-/+ Buffers/Cache:used = Mem:Used -- Mem:Buffers -- Mem:Cached，表示应用程序已用的物理内存大小

-/+ Buffers/Cache:free = Mem:Free + Mem:Buffers + Mem:Cached，表示应用程序可用的物理内存大小

Swap

交换分区的使用信息

**设备管理 \-- 设备管理配置命令 \-- display memory-threshold**

------------------------------------------------------------------------

**[display memory-threshold**]命令用来显示内存告警门限相关信息。

【命令】

集中式设备：

**[display memory-threshold**]

分布式设备－独立运行模式/集中式IRF设备：

**[display memory-threshold ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display memory-threshold ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定单板。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

当设备已经使用的物理内存大小超过内存某个告警门限阈值时，系统会认为发生了一次该类型内存异常，并记录第一次、最近一次发生异常的时间，以及这段时间内发生的该类异常的次数。如果想了解该类异常的详细情况，请查看日志信息，可按日志摘要关键字"MEM_EXCEED_THRESHOLD"或"MEM_BELOW_THRESHOLD"进行搜索。

【举例】

\# 显示内存告警门限相关信息。

\<Sysname\> display memory-threshold

Memory usage threshold: 100%

Free memory threshold:

     Minor: 64M

     Severe: 48M

     Critical: 32M

     Normal: 96M

Current memory state: Normal

Event statistics:

 Back to normal state

    First notification: 2012-5-15 09:21:35.546

    Latest notification: 2012-5-15 09:21:35.546

    Total number of notifications sent: 1

 Enter minor low-memory state

    First notification at: 2012-5-15 09:07:05.941

    Latest  notification at: 2012-5-15 09:07:05.941

    Total number of notifications sent: 1

 Back to minor low-memory state

    First notification at: 0.0

    Latest  notification at: 0.0

    Total number of notifications sent: 0

 Enter severe low-memory state

    First notification at: 0.0

    Latest  notification at: 0.0

    Total number of notifications sent: 0

 Back to severe low-memory state

    First notification at: 0.0

    Latest  notification at: 0.0

    Total number of notifications sent: 0

 Enter critical low-memory state

    First notification at: 0.0

    Latest  notification at: 0.0

    Total number of notifications sent: 0

表1-14 display memory-threshold命令显示信息描述表

字段

描述

Memory usage threshold

内存利用率阈值

Free memory threshold

         Minor:

         Severe:

         Critical:

         Normal:

剩余内存门限阈值：

·Minor：一级告警门限，单位为MB

·Severe：二级告警门限，单位为MB

·Critical：三级告警门限，单位为MB

·Normal：恢复到正常状态的阈值，单位为MB

Current memory state

系统当前内存使用状态：

·Normal：正常状态

·Minor：一级告警门限状态

·Severe：二级告警门限状态

·Critical：三级告警门限状态

Event statistics:

门限事件统计信息，事件分为：

·Back to normal state：内存恢复到正常状态

·Enter minor low-memory state：进入一级告警门限状态

·Back to minor low-memory state：恢复到一级告警门限状态

·Enter severe low-memory state：进入二级告警门限状态

·Back to severe low-memory state：恢复到二级告警门限状态

·Enter critical low-memory state：进入三级告警门限状态

First notification at

事件第一次发生的时间，格式yyyy-mm-dd hh:mm:ss.msec

Latest  notification at

事件最近一次发生的时间，格式yyyy-mm-dd hh:mm:ss.msec

Total number of notification send

事件发生的总次数

**设备管理 \-- 设备管理配置命令 \-- display power**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display power**]命令用来显示设备电源的信息。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display power** [ *power*-*id* ]]

集中式IRF设备：

**[display power** [ **slot** *slot-number* [ *power-id*  ]]]

分布式设备－IRF模式：（不支持IRF3的设备）

**[display power** [ **chassis** *chassis-number* [ *power-id*  ]]]

分布式设备－IRF模式：（支持IRF3的设备）

**[display power**[ [ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } [ *power-id* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示所有电源。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示所有电源。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示所有电源。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]]：显示指定成员设备或者PEX上电源的信息。*chassis-number*表示设备在IRF中的成员编号；*virtual-chassis-number*表示PEX对应的虚拟框号，*slot-number*表示PEX在虚拟框中的槽位号。不指定**chassis**参数时，表示所有电源。（分布式设备－IRF模式）（支持IRF3的设备）

*[power*-*id*]：表示电源的编号，不同型号的设备的取值范围不同，请以设备的实际情况为准。不指定该参数时，表示指定位置的所有电源。

【举例】

\# 显示设备电源的状况。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准，此处略）

\<Sysname\> display power

**设备管理 \-- 设备管理配置命令 \-- display power-supply**

------------------------------------------------------------------------

![说明](设备管理命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display power-supply**]命令用来显示设备电源的信息。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display power-supply ** **verbose** ]

集中式IRF设备：

**[display power-supply ** **slot** *slot-number* ]  **verbose**

分布式设备－IRF模式：

**[display power-supply** [ **chassis** *chassis-number*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[slot** *slot-number*]：显示指定成员设备上电源的信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上电源的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示所有成员设备/PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*]：显示指定成员设备上电源的信息。*chassis-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（分布式IRF设备）（不支持IRF3的设备）

**[chassis ***chassis-number*]：显示指定成员设备/PEX上电源的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号。不指定该参数时，表示所有成员设备/PEX。（分布式IRF设备）（支持IRF3的设备）

**[verbose**]：显示电源的详细信息。不指定该参数时，显示电源的简要信息。

【举例】

\# 显示电源详细信息（该显示信息与设备的型号有关，请以设备的实际情况为准）。

\<Sysname\> display power-supply verbose

**设备管理 \-- 设备管理配置命令 \-- display rps**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display rps**]命令用来显示设备RPS（Redundant Power System，冗余电源系统）的状态。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display rps** [ *rps*-*id* ]]

集中式IRF设备：

**[display rps** [ **slot** *slot-number* [ *rps-id*  ]]]

分布式设备－IRF模式：（不支持IRF3的设备）

**[display rps** [ **chassis** *chassis-number* [ *rps-id*  ]]]

分布式设备－IRF模式：（支持IRF3的设备）

**[display rps**[ [ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } [ *rps-id* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：表示单板所在的槽位号。不指定该参数时，表示所有RPS。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示所有RPS。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示所有RPS。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]]：显示指定成员设备或者PEX上风扇的状态信息。*chassis-number*表示设备在IRF中的成员编号；*virtual-chassis-number*表示PEX对应的虚拟框号，*slot-number*表示PEX在虚拟框中的槽位号。不指定**chassis**参数时，表示所有风扇。（分布式设备－IRF模式）（支持IRF3的设备）

*[rps*-*id*]：表示设备RPS的编号，不同型号的设备的取值范围不同，请以设备的实际情况为准。不指定该参数时，表示指定位置的所有RPS。

【举例】

\# 显示设备RPS的状态信息。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准，此处略）

\<Sysname\> display rps

**设备管理 \-- 设备管理配置命令 \-- display save-power**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **save-power**]命令用来显示节能功能相关信息。

【命令】

**[display save-power**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示节能功能是否使能以及所处的节能状态。

\<Sysname\> display save-power

Save-power state: enable(wake)

Save-power delay-time: 30(s)

Save-power delay-time remained: 5(s)

表1-15 display save-power命令输出信息描述表

字段

描述

Save-power state

节能功能的状态，取值可能为：

·disabled：表示没有使能

·enabled(wake)：表示已经使能，且处于节能唤醒状态

·enabled(sleep)：表示已经使能，且处于节能休眠状态

Save-power delay-time

配置的设备从节能唤醒状态切换到节能休眠状态的时间间隔（只有节能功能使能时，才会显示该信息）

Save-power delay-time remained

设备从节能唤醒状态切换到节能休眠状态的剩余时间间隔（只有节能功能的状态为"enabled(wake)"时才显示该信息）

**设备管理 \-- 设备管理配置命令 \-- display scheduler job**

------------------------------------------------------------------------

**[display scheduler job**]命令用来查看Job的配置信息，包括Job的名称和分配的命令。

【命令】

**[display scheduler job ** *job-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[job-name*]：Job的名称，为1～47个字符的字符串，区分大小写。不指定该参数时，则显示所有Job的配置信息。

【举例】

\# 查看所有Job的配置信息。

\<Sysname\> display scheduler job

Job name: saveconfig

 copy startup.cfg backup.cfg

Job name: backupconfig

Job name: creat-VLAN100

 system-view

 vlan 100

以上显示信息表明，设备当前配置了3个Job，分别显示了Job的名称，以及为Job分配的命令（如果没有为Job分配命令，则只显示Job的名称），不同Job间用空行分隔。

**设备管理 \-- 设备管理配置命令 \-- display scheduler logfile**

------------------------------------------------------------------------

**[display scheduler logfile**]命令用来显示已执行的Job的日志信息，包括Job的名称、对应的Schedule的名称、执行时间以及执行结果。

【命令】

**[display scheduler logfile**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示Schedule日志文件的相关信息。

\<Sysname\> display scheduler logfile

Logfile Size: 1902 Bytes.

Job name        : shutdown{.TerminalDisplayChar}

Schedule name   : shutdown{.TerminalDisplayChar}

Execution time  : Tue Dec 27 10:44:42 2011{.TerminalDisplayChar}

Completion time : Tue Dec 27 10:44:47 2011{.TerminalDisplayChar}

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- Job output \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--{.TerminalDisplayChar}

\<{.TerminalDisplayChar}Sysname[\>system-view{.TerminalDisplayChar}]

System View: return to User View with Ctrl+Z.{.TerminalDisplayChar}

{.TerminalDisplayChar}Sysname[interface rang gigabitethernet 1/0/1 to gigabitethernet 1/0/3]{.TerminalDisplayChar}

{.TerminalDisplayChar}Sysname[-if-rangeshutdown]{.TerminalDisplayChar}

表1-16 display scheduler logfile命令显示信息描述表

字段

描述

Logfile Size

Schedule日志文件的大小，单位为字节

Job name

Job的名称

Schedule name

Schedule的名称

Execution time

开始执行Job的时间

Completion time

Job执行结束的时间（没有调度的或者没有分配命令的Job，均不会显示该信息）

Job output

Job中的命令执行时的输出信息

【相关命令】

·**reset scheduler logfile**

**设备管理 \-- 设备管理配置命令 \-- display scheduler reboot**

------------------------------------------------------------------------

**[display scheduler reboot**]命令用来查看定时重启功能的相关配置。

【命令】

**[display scheduler reboot**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看定时重启功能的相关配置。

\<Sysname\> display scheduler reboot

System will reboot at 16:32:00 05/23/2011 (in 1 hours and 39 minutes).

【相关命令】

·**scheduler reboot at**

·**scheduler reboot delay**

**设备管理 \-- 设备管理配置命令 \-- display scheduler schedule**

------------------------------------------------------------------------

**[display scheduler schedule**]命令用来查看Schedule的相关信息。

【命令】

**[display scheduler schedule ** *schedule-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[schedule-name*]：Schedule的名称，为1～47个字符的字符串，区分大小写。如果不指定该参数，则显示所有Schedule的信息。

【举例】

\# 查看所有Schedule的信息。

\<Sysname\> display scheduler schedule

Schedule name        : shutdown

Schedule type        : Run once after 0 hours 2 minutes

Start time           : Tue Dec 27 10:44:42 2011

Last execution time  : Tue Dec 27 10:44:42 2011

Last completion time : Tue Dec 27 10:44:47 2011

Execution counts     : 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Job name                                          Last execution status

shutdown                                          Successful

表1-17 display scheduler schedule命令显示信息描述表

字段

描述

Schedule name

Schedule的名称

Schedule type

Schedule的执行时间配置。如果没有为Schedule配置执行时间，则不会显示该信息

Start time

Schedule第一次开始执行的时间。如果没有为Schedule配置执行时间，则不会显示该信息

Last execution time

Schedule上一开始执行的时间

·如果没有为Schedule配置执行时间，则不会显示该信息

·如果还没有执行，则显示Yet to be executed

Last completion time

Schedule上一次执行完成的时间。如果没有为Schedule配置执行时间，则不会显示该信息

Execution counts

Schedule已经执行的次数。如果Schedule还没有执行，则不会显示该信息

Job name

Schedule下关联的Job的名称

Last execution status

Job上一次被执行的状态（Job下分配的命令是否执行以及执行结果，请通过**display scheduler logfile**命令查看）

·Successful：表示执行成功

·Failed：表示执行失败

·Waiting：表示正在等待被执行

·In process：表示正在执行

·-NA-：表示还没有到执行时间

**设备管理 \-- 设备管理配置命令 \-- display system-working-mode**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system-working-mode**]命令用来显示设备当前的工作模式。

【命令】

**[display system-working-mode**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示设备当前的工作模式。

\<Sysname\> display system-working-mode

The current system working mode is standard.

The system working mode for next startup is standard.

**设备管理 \-- 设备管理配置命令 \-- display transceiver alarm**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·是否支持可插拔接口模块以及模块类型的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display transceiver alarm**]命令用来显示可插拔接口模块的当前故障告警信息。

【命令】

**[display transceiver alarm interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** [ *interface-type interface-number* ]]：显示接口上插入的可插拔接口模块的当前故障告警信息。*interface-type interface-number*表示接口类型和接口编号，如果不指定该参数，表示所有接口。

【使用指导】

目前，使用的可插拔接口模块可能出现的故障告警信息见 表1-18(?975698249#_Ref170038014)。如果没有故障，则显示为None。

表1-18 display transceiver alarm命令输出信息描述表

字段

描述

SFP/SFP+/GBIC/SFF

RX loss of signal

接收信号丢失

RX power high

接收光功率高

RX power low

接收光功率低

TX fault

发送错误

TX bias high

偏置电流高

TX bias low

偏置电流低

TX power high

发送光功率高

TX power low

发送光功率低

Temp high

温度高

Temp low

温度低

Voltage high

电压高

Voltage low

电压低

Transceiver info I/O error

模块信息读写错误

Transceiver info checksum error

模块信息校验和错误

Transceiver type and port configuration mismatch

模块类型和端口配置不匹配

Transceiver type not supported by port hardware

端口不支持该模块类型

QSFP+

Temp high

温度高

Temp low

温度低

Voltage high

电压高

Voltage low

电压低

RX signal loss in channel *x*

通道*x*接收到的信号丢失

TX fault in channel *x*

通道*x*发送报文时出错

TX signal loss in channel *x*

通道*x*发送的信号丢失

RX power high in channel *x*

通道*x*接收到的光的功率太高

RX power low in channel *x*

通道*x*接收到的光的功率太低

TX bias high in channel *x*

通道*x*的偏置电流高

TX bias low in channel *x*

通道*x*的偏置电流低

Transceiver info I/O error

模块读写错误

Transceiver info checksum error

模块信息校验和错误

Transceiver type and port configuration mismatched

模块类型和端口配置不匹配

Transceiver type not supported

端口不支持该类型的模块

CFP

TX jitter PLL unlocked

发送Jitter PLL失锁

TX CMU unlocked

发送CMU失锁

Overloaded

负载过大

Loss of REFCLK input

缺乏参考时钟

Channel signals out of alignment

主机通道信号不对齐

PLD or flash initialization error

初始化错误

Power supply fault

电源错误

CFP checksum error

校验和错误

TX bias high

偏置电流高

TX bias low

偏置电流低

Temp high

温度高

Temp low

温度低

Voltage high

电压高

Voltage low

电压低

RX signal loss in channel *x*

通道*x*接收到的信号丢失

RX IC unlocked in channel *x*

通道*x*接收到的IC时钟失锁

RX FIFO error in channel *x*

通道*x*接收到FIFO错误

TX signal loss in channel *x*

通道*x*发送的信号丢失

TX IC unlocked in channel *x*

通道*x*发送的IC时钟失锁

TX FIFO error in channel *x*

主机通道*x*的发送FIFO出错

TX IC unlocked in channel *x*

主机通道*x*发送的IC时钟失锁

APD supply fault in channel *x*

通道*x*出现APD错误

TEC fault in channel x

通道*x*出现TEC错误

Wavelength unlocked in channel *x*

通道*x*的光信号波长失锁

RX power high in lane *x*

通道*x*接收到的光的功率太高

RX power low in lane *x*

通道*x*接收到的光的功率太低

TX power high in lane *x*

通道*x*发送的光的功率太高

TX power low in lane *x*

通道*x*发送的光的功率太低

TX bias high in lane *x*

通道*x*的偏置电流高

TX bias low in lane *x*

通道*x*的偏置电流低

Temp high in lane *x*

通道*x*的温度高

Temp low in lane *x*

通道*x*的温度低

Transceiver info I/O error

模块读写错误

Transceiver info checksum error

模块信息校验和错误

Transceiver type and port configuration mismatched

模块类型和端口配置不匹配

Transceiver type not supported

端口不支持该类型的模块

XFP

RX loss of signal

接收信号丢失

RX not ready

接收状态未就绪

RX CDR loss of lock

RX CDR时钟失锁

RX power high

接收光功率高

RX power low

接收光功率低

TX not ready

发送状态未就绪

TX fault

发送错误

TX CDR loss of lock

TX CDR时钟失锁

TX bias high

偏置电流高

TX bias low

偏置电流低

TX power high

发送光功率高

TX power low

发送光功率低

Module not ready

模块状态未就绪

APD supply fault

APD（Avalanche Photo Diode，雪崩光电二极管）错误

TEC fault

TEC（Thermoelectric Cooler，热点冷却器）错误

Wavelength unlocked

光信号波长失锁

Temp high

温度高

Temp low

温度低

Voltage high

电压高

Voltage low

电压低

Transceiver info I/O error

模块信息读写错误

Transceiver info checksum error

模块信息校验错误

Transceiver type and port configuration mismatch

模块类型和端口配置不匹配

Transceiver type not supported by port hardware

端口不支持该模块类型

XENPAK

WIS local fault

WIS（WAN Interface Sublayer）本地错误

Receive optical power fault

接收光功率错误

PMA/PMD receiver local fault

PMA/PMD（Physical Medium Attachment/Physical Medium Dependent）接收器本地错误

PCS receive local fault

PCS（Physical Coding Sublayer）接收本地错误

PHY XS receive local fault

PHY XS（PHY Extended Sublayer）接收本地错误

RX power high

接收光功率高

RX power low

接收光功率低

Laser bias current fault

激光器偏置电流错误

Laser temperature fault

激光器温度错误

Laser output power fault

激光器输出光功率错误

TX fault

发送器错误

PMA/PMD receiver local fault

PMA/PMD接收器本地错误

PCS receive local fault

PCS接收本地错误

PHY XS receive local fault

PHY XS接收本地错误

TX bias high

偏置电流高

TX bias low

偏置电流低

TX power high

发送光功率高

TX power low

发送光功率低

Temp high

温度高

Temp low

温度低

Transceiver info I/O error

模块信息I/O错误

Transceiver info checksum error

模块信息校验错误

Transceiver type and port configuration mismatch

模块类型和端口配置不匹配

Transceiver type not supported by port hardware

端口不支持该模块类型

【举例】

\# 显示接口GigabitEthernet1/0/1上插入的可插拔接口模块的当前故障告警信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。

\<Sysname\> display transceiver alarm interface gigabitethernet 1/0/1

GigabitEthernet1/0/1 transceiver current alarm information:

  RX loss of signal

  RX power low

表1-19 display transceiver alarm显示信息描述表

字段

描述

transceiver current alarm information

接口光模块当前故障告警信息

RX loss of signal

接收信号丢失

RX power low

接收光功率低告警

**设备管理 \-- 设备管理配置命令 \-- display transceiver diagnosis**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·数字诊断参数的显示与可插拔接口模块的类型有关，请以设备的实际情况为准。

**[display transceiver diagnosis**]命令用来显示可插拔光模块的数字诊断参数的当前测量值。

【命令】

**[display transceiver diagnosis interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** [ *interface-type interface-number* ]]：显示接口上插入的可插拔光模块的数字诊断参数的当前测量值。*interface-type interface-number*表示接口类型和接口编号，如果不指定该参数，表示所有接口。

【举例】

\# 显示接口GigabitEthernet1/0/1上插入的可插拔光模块的数字诊断参数的当前测量值（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。

\<Sysname\> display transceiver diagnosis interface gigabitethernet 1/0/1

GigabitEthernet1/0/1 transceiver diagnostic information:

  Current diagnostic parameters:

    Temp(°C)  Voltage(V)  Bias(mA)  RX power(dBm)  TX power(dBm)

    36        3.31        6.13      -35.64          -5.19

  Alarm thresholds:

           Temp(℃)   Voltage(V)  Bias(mA)  RX power(dBM)  TX power(dBM)

    High   50         3.55        1.44      -10.00         5.00

    Low    30         3.01        1.01      -30.00         0.00

表1-20 display transceiver diagnosis显示信息描述表

字段

描述

transceiver diagnostic information

接口插入的光模块的数字诊断信息

Current diagnostic parameters

当前的诊断参数

Temp.(°C)

数字诊断参数------温度，单位为°C，精确到1°C

Voltage(V)

数字诊断参数------电压，单位为V，精确到0.01V

Bias(mA)

数字诊断参数------偏置电流，单位为mA，精确到0.01mA

RX power(dBm)

数字诊断参数------接收光功率，单位为dBm，精确到0.01dBm

TX power(dBm)

数字诊断参数------发送光功率，单位为dBm，精确到0.01dBm

Alarm thresholds

告警门限

High

高告警门限

Low

低告警门限

**设备管理 \-- 设备管理配置命令 \-- display transceiver interface**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display transceiver interface**]命令用来显示可插拔接口模块的主要特征参数。

【命令】

**[display transceiver interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：显示接口上插入的可插拔接口模块的主要特征参数。*interface-type interface-number*表示接口类型和接口编号，如果不指定该参数，表示所有接口。

【举例】

\# 显示接口GigabitEthernet1/0/1上插入的可插拔接口模块的主要特征参数（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。

\<Sysname\> display transceiver interface gigabitethernet 1/0/1

GigabitEthernet1/0/1 transceiver information:

  Transceiver Type              : 1000_BASE_SX_SFP

  Connector Type                : LC

  Wavelength(nm)                : 850

  Transfer Distance(m)          : 550(50um),270(62.5um)

  Digital Diagnostic Monitoring : YES

  Vendor Name                   : H3C

  Ordering Name                 : SFP-GE-SX-MM850

表1-21 display transceiver interface命令显示信息描述表

字段

描述

transceiver information

可插拔接口模块信息

Transceiver Type

可插拔接口模块的物理型号

Connector Type

可插拔接口模块的连接器类型，其中：

·光纤连接器包括SC（SC Connector，NTT公司推出的拔插锁紧式光纤连接器）、LC（LC Connector，Lucent公司推出的1.25mm/RJ45锁紧式光纤连接器）两种类型

·其他连接器包括RJ-45、CX4等类型

Wavelength(nm)

·光模块：显示发送激光中心波长，单位nm；对于支持多条不同波长光路的模块（例如10GBASE-LX4模块），各个波长值之间用逗号分隔

·电模块：显示为"N/A"

Transfer Distance(xx)

传输距离，xx为传输距离的单位，对于单模模块xx为km，对于其他模块xx为m。当模块支持多种传输介质时，各个传输距离值之间用逗号分隔。距离值后面括号里包含对应的"传输介质"。下面是各个介质的名称：

·9um：表示9/125um单模光纤

·50um：表示50/125um多模光纤

·62.5um：表示62.5/125um多模光纤

·TP：表示双绞线

·CX4：表示CX4电缆

Digital Diagnostic Monitoring

对数字诊断功能的支持情况，其中：

·YES：表示支持数字诊断

·NO：表示不支持数字诊断

Vendor Name

模块生产或定制厂商名称

Ordering Name

可插拔接口模块的对外型号

**设备管理 \-- 设备管理配置命令 \-- display transceiver manuinfo**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display transceiver manuinfo**]命令用于显示可插拔接口模块的部分电子标签信息。

【命令】

**[display transceiver manuinfo interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** [ *interface-type interface-number* ]]：显示接口上插入的可插拔接口模块的部分电子标签信息。*interface-type interface-number*表示接口类型和接口编号，如果不指定该参数，表示所有接口。

【举例】

\# 显示接口GigabitEthernet1/0/1上插入的可插拔接口模块的部分电子标签信息（本命令的显示信息与设备型号有关，请以设备的实际情况为准）。

\<Sysname\> display transceiver manuinfo interface gigabitethernet 1/0/1

GigabitEthernet1/0/1 transceiver manufacture information:

  Manu. Serial Number  : 213410A0000054000251

  Manufacturing Date   : 2012-09-01

  Vendor Name          : H3C

表1-22 display transceiver manuinfo命令显示信息描述表

字段

描述

Manu. Serial Number

在生产过程中生成的序列号

Manufacturing Date

写入电子标签的日期

Vendor Name

厂商名称

**设备管理 \-- 设备管理配置命令 \-- display version**

------------------------------------------------------------------------

**[display version**]命令用来显示系统版本信息。

【命令】

**[display** **version**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看系统版本信息（不同设备的版本信息不同，请以设备的实际情况为准，此处略）。

\<Sysname\> display version

**设备管理 \-- 设备管理配置命令 \-- display version-update-record**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display version-update-record**]命令用来显示设备启动软件包版本更新操作的记录。（集中式设备）

**[display version-update-record**]命令用来显示主用主控板启动软件包版本更新操作的记录。（分布式设备－独立运行模式）

**[display version-update-record**]命令用来显示主设备启动软件包版本更新操作的记录。（集中式IRF设备）

**[display version-update-record**]命令用来显示全局主用主控板启动软件包版本更新操作的记录。（分布式设备－IRF模式）

【命令】

**[display version-update-record**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【描述】

设备启动时会记录当前使用的启动软件包版本信息，如果在运行过程中进行启动软件包版本更新操作，系统会记录该次更新的简要信息，包括升级时间和版本，以便管理员了解相关信息。设备重启这些记录也不会被删除。

目前最多可以保存的更新记录的数目与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示设备启动软件包版本更新操作的记录。

\<Sysname\> display version-update-record

Record 1  (updated on Apr 18 2014 at 06:23:54):

 \*Name        : simware-cmw710-boot-a5301.bin

  Version     : 7.1.053 Alpha 7153

  Compile time: Mar 25 2014 15:52:43

 \*Name        : simware-cmw710-system-a5301.bin

  Version     : 7.1.053 Alpha 7153

  Compile time: Mar 25 2014 15:52:43

表1-23 display version-update-record命令显示信息描述表

字段

描述

Record *n* (updated on Apr 18 2014 at 06:23:54)

最近的第*n*次更新的时间，Record 1为最新的一次更新

\*Name

软件包的名称。带\*符号，表示软件包的版本和升级前的版本有变化；不带\*符号，表示版本没有变化

Version

软件包的版本号

Compile time

版本编译时间

【相关命令】

·**reset version-update-record**

**设备管理 \-- 设备管理配置命令 \-- display xbar**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display xbar**]命令用来显示设备上主用主控板和备用主控板的负载模式，包括配置的负载模式和当前运行的负载模式。

【命令】

分布式设备－独立运行模式：

**[display xbar**]

分布式设备－IRF模式：

**[display xbar ** **chassis** *chassis-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：用来显示指定成员设备上主用主控板和备用主控板的负载模式。*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式）

【使用指导】

配置的负载模式和当前运行的负载模式不一定相同。只有主用主控板和备用主控板同时在位时，配置的负载分担模式才会生效；否则，即便配置了负载分担模式，主用主控板也会自动切换到独立负载模式。

【举例】

\# 显示设备主用主控板和备用主控板的负载模式。（分布式设备－独立运行模式）

\<Sysname\> display xbar

The configured system HA xbar load mode is BALANCE

The activated system HA xbar load mode is SINGLE

以上显示信息表明：当前系统配置的负载模式为负载分担模式，但实际生效的是独立负载模式。

\# 显示IRF系统中所有成员设备上主用主控板和备用主控板的负载模式。（分布式设备－IRF模式）

\<Sysname\> display xbar

Chassis 1:

The configured system HA xbar load mode is BALANCE

The activated system HA xbar load mode is SINGLE

Chassis 2:

The configured system HA xbar load mode is SINGLE

The activated system HA xbar load mode is SINGLE

以上显示信息表明：IRF系统中有两个成员设备，成员设备1上配置的主用主控板和备用主控板的负载模式为负载分担模式，但实际生效的是独立负载模式；成员设备2上配置的主用主控板和备用主控板的负载模式为独立负载模式，实际生效的也是独立负载模式。

【相关命令】

·**xbar**

**设备管理 \-- 设备管理配置命令 \-- fabric load-sharing mode**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[fabric load-sharing mode**]命令用来配置业务板的负载分担类型。

**[undo fabric load-sharing mode**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[fabric load-sharing mode**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-ip** \| **source-mac** \| **source-port** \| **vlan-id** } \* \| **flexible** \| **per-packet** } **slot** *slot-number*]]

**[undo fabric load-sharing mode slot ***slot-number*]

分布式设备－IRF模式：

**[fabric load-sharing mode**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-ip** \| **source-mac** \| **source-port** \| **vlan-id** } \* \| **flexible** \| **per-packet** } **chassis** *chassis-number* **slot** *slot-number*]]

**[undo fabric load-sharing mode chassis** *chassis-number* **slot** *slot-number*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination-ip**]：表示按报文的目的IP地址进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[destination-mac**]：表示按报文的目的MAC地址进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[destination-port**]：表示按报文的目的服务端口进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[ingress-port**]：表示按报文的入端口进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[ip-protocol**]：表示按报文的IP协议类型进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[mpls-label1**]：表示按MPLS报文第一层标签进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[mpls-label2**]：表示按MPLS报文第二层标签进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[mpls-label3**]：表示按MPLS报文第三层标签进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[source-ip**]：表示按报文的源IP地址进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[source-mac**]：表示按报文的源MAC地址进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[source-port**]：表示按报文的源服务端口进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[vlan-id**]：表示按报文所属的VLAN进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[flexible**]：表示按报文类型（如二层、IPv4、IPv6、MPLS等）自动选择负载分担的类型。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[per-packet**]：表示对每个报文逐包进行负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[slot **]*slot-number*：单板所在的槽位号。（分布式设备－独立运行模式）

**[slot **]*slot-number*：设备所在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot **]*slot-number*：设备所在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number ***slot ***slot-number*：*chassis-number*表示设备在IRF中的成员编号，*slot-number*为单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number ***slot ***slot-number*：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*为单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

·如果多次执行本命令，新的配置将覆盖旧的配置。

·对于业务板不支持的负载分担类型，系统将提示用户不支持。

【举例】

\# 配置单板2按照报文目的MAC地址进行负载分担。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname fabric load-sharing mode destination-mac slot 2

**设备管理 \-- 设备管理配置命令 \-- fan auto-control-mode**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

****

**[fan auto-control-mode**]命令用来配置风扇的工作模式。

**[undo fan auto-control-mode**]命令用来回复缺省情况。

【命令】

分布式设备－独立运行模式：

**[fan auto-control-mode**[ { **low-temperature** \| **silence** }]]

**[undo fan auto-control-mode**]

分布式设备－IRF模式：

**[fan auto-control-mode chassis**[ *chassis-number* { **low-temperature** \| **silence** }]]

**[undo fan auto-control-mode chassis ***chassis-number*]

【缺省情况】

风扇工作在低温模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chassis** *chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

**[low-temperature**]：配置风扇工作在低温模式。该模式下风扇转速较高，以便优先保证单板在较低的温度下工作。

**[silence**]：配置设备工作在静音模式。该模式下风扇转速较低、噪音较小，但是单板温度比低温模式略高。在对噪音比较敏感的场合推荐使用此模式。

【举例】

\# 配置风扇工作在静音模式。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname fan auto-control-mode silence

\# 配置IRF中成员设备2的风扇工作在静音模式。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname fan auto-control-mode chassis 2 silence

**设备管理 \-- 设备管理配置命令 \-- fan prefer-direction**

------------------------------------------------------------------------

![说明](设备管理命令.files/image003.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

****

**[fan prefer-direction**]命令用来配置用户期望的风扇模块的风道方向。

**[undo fan prefer-direction**]命令用来恢复缺省情况。

【命令】

集中式设备/分布式设备－独立运行模式：

**[fan prefer-direction **[{ **power-to-port** \| **port-to-power** }]]

**[undo fan prefer-direction**]

集中式IRF设备：

**[fan prefer-direction slot*** slot-number *[{ **power-to-port** \| **port-to-power** }]]

**[undo fan prefer-direction slot*** slot-number*]

分布式设备－IRF模式：

**[fan prefer-direction chassis*** chassis-number *[{ **power-to-port** \| **port-to-power** }]]

**[undo fan prefer-direction chassis*** chassis-number*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：表示设备的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：表示设备的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number*]：表示设备的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number*]：表示设备的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[power-to-port**]：表示用户期望的风道方向是电源侧进风、端口侧出风。

**[port-to-power**]**：**表示用户期望的风道方向是端口侧进风、电源侧出风。

【举例】

\# 配置用户期望的风扇模块的风道方向为port-to-power。（集中式设备/分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname fan prefer-direction port-to-power

\# 配置成员设备1的用户期望的风扇模块的风道方向为port-to-power。（集中式IRF设备）

\<Sysname\> system-view

Sysname fan prefer-direction slot 1 port-to-power

\# 配置成员设备1的用户期望的风扇模块的风道方向为port-to-power。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname fan prefer-direction chassis 1 port-to-power

【相关命令】

·**display fan**

**设备管理 \-- 设备管理配置命令 \-- forward-path-detection enable**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

****

**[forward-path-detection enable**]命令用来开启转发通道自动检测功能。

**[undo forward-path-detection enable**]命令用来关闭转发通道自动检测功能。

【命令】

**[forward-path-detection enable**]

**[undo forward-path-detection enable**]

【缺省情况】

转发通道自动检测功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

转发通道自动检测功能可以检测设备中的数据转发通道是否正常。如果不正常，会打印日志信息提醒用户。

【举例】

\# 开启转发通道自动检测功能。

\<Sysname\> system-view

Sysname forward-path-detection enable

**设备管理 \-- 设备管理配置命令 \-- hardware-failure-detection**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[hardware-failure-detection**]命令用来配置当系统检测到硬件故障时自动采取的修复操作。

**[undo hardware-failure-detection**]命令用来恢复缺省情况。

【命令】

**[hardware-failure-detection**[ { **board** \| **chip** \| **forwarding** } { **off** \| **isolate** \| **reset** \| **warning** }]]

**[undo hardware-failure-detection **[{ **board** \| **chip** \| **forwarding** }]]

【缺省情况】

当系统检测到器件（chip）、单板（board）和转发（forwarding）的硬件故障时，修复操作均为warning。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[board**]：对单板故障进行在线检测，包括控制通道检测和单板状态快速检测。

**[chip**]：对器件故障进行在线检测，包括单板上各种器件（比如芯片、电容、电阻等）的检测。

**[forwarding**]：对转发层面的故障进行在线检测，包括业务自动检测和其他转发相关的检测。

**[off**]：检测到故障时，设备不进行任何操作。

**[isolate**]：检测到故障时，设备会自动关闭端口、隔离单板、禁止单板加载或给单板下电，从而尽量减小故障的影响。

**[reset**]：检测到故障时，设备会自动重启器件/单板以尝试修复故障。

**[warning**]：检测到故障时，设备发送Trap信息，不会修复故障。

【使用指导】

设备启动后，系统会持续自动检测器件、单板和转发的硬件故障。

【举例】

\# 配置系统检测到器件故障时自动告警。

\<Sysname\> system-view

Sysname hardware-failure-detection chip warning

\# 配置系统检测到单板故障时自动重启。

\<Sysname\> system-view

Sysname hardware-failure-detection board reset

**设备管理 \-- 设备管理配置命令 \-- hardware-failure-protection aggregation**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[hardware-failure-protection aggregation**]命令用来开启针对聚合组的硬件故障保护功能。

**[undo hardware-failure-protection aggregation**]命令用来关闭针对聚合组的硬件故障保护功能。

【命令】

**[hardware-failure-protection aggregation**]

**[undo hardware-failure-protection aggregation**]

【缺省情况】

针对聚合组的硬件故障保护功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有配置**hardware-failure-detection forwarding isolate**命令后，该命令才生效。

配置该命令后，当系统检测到硬件故障时，会按顺序遵循如下原则处理：

(1)如果聚合组成员端口配置**undo hardware-failure-protection auto-down**命令，而且该端口不是聚合组中最后一个UP状态的端口，则该端口会被自动关闭；

(2)如果聚合组成员端口配置**undo hardware-failure-protection auto-down**命令，而该端口是聚合组中最后一个UP状态的端口，则该端口不会被关闭；

(3)如果聚合组成员端口配置了**hardware-failure-protection** **auto-down**命令，则不管该端口是不是聚合组中最后一个UP状态的端口，该端口都会被关闭。

出现以下任意一种情况时，**hardware-failure-protection aggregation**命令会对聚合组中的该成员端口失效：

·端口下配置了以太网接口环回测试功能，即**loopback**[ { **external** \| **internal** }]命令；

·端口下配置了以太网接口的强制开启功能，即**port up-mode**命令；

·该端口配置为IRF物理端口。

【举例】

\# 开启针对聚合组的硬件故障保护功能。

\<Sysname\> system-view

Sysname hardware-failure-protection aggregation

【相关命令】

·**hardware-failure-detection**

·**hardware-failure-protection auto-down**

**设备管理 \-- 设备管理配置命令 \-- hardware-failure-protection auto-down**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

**[hardware-failure-protection auto-down**]命令用来开启针对端口的硬件故障保护功能。

**[undo hardware-failure-protection auto-down**]命令用来关闭针对端口的硬件故障保护功能。

【命令】

**[hardware-failure-protection auto-down**]

**[undo hardware-failure-protection auto-down**]

【缺省情况】

端口的硬件故障保护功能处于开启状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置了**hardware-failure-detection** **forwarding** **isolate**后，本命令才会生效。

在端口上配置该命令前，请确保该端口存在备份的链路，以免造成业务中断。

在端口上配置**hardware-failure-protection auto-down**命令后，当系统检测到硬件故障时，会自动关闭该端口。此时使用**display interface**命令可看到该端口状态为Protect DOWN。端口硬件故障解除后，请在接口下执行**undo shutdown**命令来恢复端口状态。

出现以下任意一种情况时，**hardware-failure-protection aggregation**命令会对该端口失效：

·端口下配置了以太网接口环回测试功能，即**loopback**[ { **external** \| **internal** }]命令；

·端口下配置了以太网接口的强制开启功能，即**port up-mode**命令；

·该端口配置为IRF物理端口。

【举例】

\# 对端口配置硬件故障保护。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 hardware-failure-protection auto-down

**设备管理 \-- 设备管理配置命令 \-- header**

------------------------------------------------------------------------

**[header**]命令用来设置欢迎信息。

**[undo header**]命令用来关闭欢迎信息。

【命令】

**[header**[ { **incoming** \| **legal** \| **login** \| **motd** \| **shell** } *text*]]

**[undo header **[{ **incoming \| legal** \| **login** \| **motd** \| **shell** }]]

【缺省情况】

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[incoming**]：设置Modem登录用户登录进入用户视图时的欢迎信息。如果要求认证，则欢迎信息在通过认证后输出。

**[legal**]：设置登录终端界面前的授权信息，在输入认证用户名和密码前输出。

**[login**]：设置登录验证时的欢迎信息。

**[motd**]：设置登录终端界面前的欢迎信息。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[shell**]：设置非Modem登录用户登录进入用户视图时的欢迎信息。

*[text*]：输入欢迎信息的内容。内容的输入支持单行和多行两种方式，具体输入规则请参见"基础配置指导"中的"设备管理"。

【举例】

\# 先后配置**incoming**、**legal**、**login**、**motd**和**shell**欢迎信息，并验证配置效果。

\<Sysname\> system-view

Sysname header incoming

Please input banner content, and quit with the character \'%\'.

Welcome to incoming(header incoming)%

Sysname header legal

Please input banner content, and quit with the character \'%\'.

Welcome to legal (header legal)%

Sysname header login

Please input banner content, and quit with the character \'%\'.

Welcome to login(header login)%

Sysname header motd

Please input banner content, and quit with the character \'%\'.

Welcome to motd(header motd)%

Sysname header shell

Please input banner content, and quit with the character \'%\'.

Welcome to shell(header shell)%

本例中，"%"为*text*的起始/结束字符，在显示文本后输入"%"表示文本结束，退出header命令。作为起始与结束字符，"%"不会成为所设置欢迎信息的一部分。

采用Telnet方式远程登录设备，测试以上设置（只有设置了登录认证之后，才会显示login欢迎信息）。

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*

\* Without the owner\'s prior written consent,                                 \*

\* no decompiling or reverse-engineering shall be allowed.                    \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Welcome to legal (header legal)

 Press Y or ENTER to continue, N to exit.

Welcome to motd(header motd)

Welcome to login(header login)

Login authentication

Password:

Welcome to shell(header shell)

**设备管理 \-- 设备管理配置命令 \-- job**

------------------------------------------------------------------------

**[job**]命令用来为Schedule分配Job。

**[undo job**]命令用来将Job从Schedule中删除。

【命令】

**[job ***job-name*]

**[undo job*** job-name*]

【缺省情况】

没有为Schedule分配Job。

【视图】

Schedule视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[job-name*]：Job的名称，为1～47个字符的字符串，区分大小写。

【使用指导】

多次执行该命令，可以为Schedule分配多个Job。多个Job在Schedule指定的时间同时执行，没有先后顺序。

分配的Job必须是设备上已经创建的Job，否则不能分配。Job可以通过**scheduler job**命令来创建。

【举例】

\# 为Schedule分配一个名称为save-job的Job。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig job save-job

【相关命令】

·**scheduler job**

·**scheduler schedule**

**设备管理 \-- 设备管理配置命令 \-- locator blink**

------------------------------------------------------------------------

![说明](设备管理命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[locator blink ***blink-time*]命令用来定位设备的位置。

**[locator blink stop**]命令用来停止定位。

【命令】

集中式设备/分布式设备－独立运行模式：

**[locator blink ***blink-time*]

**[locator blink stop**]

集中式IRF设备：

**[locator ** **slot** *slot-number* ] **blink** *blink-time*

**[locator** [ **slot** *slot-number*  **blink** **stop**]]

分布式设备－IRF模式：（不支持IRF3的设备）

**[locator ** **chassis** *chassis-number* ] **blink** *blink-time*

**[locator ** **chassis** *chassis-number* ] **blink stop**

分布式设备－IRF模式：（支持IRF3的设备）

**[locator **[[ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } ] **blink** *blink-time*]]

**[locator **[[ **chassis** { *chassis-number \| virtual-chassis-number* **slot** *slot-number* } ] **blink stop**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示对所有设备进行操作。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示对所有设备/PEX进行操作。（集中式IRF设备）（支持IRF3的设备）

**[chassis **[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]]：显示指定成员设备上风扇的状态信息。*chassis-number*表示设备在IRF中的成员编号。不指定该参数时，表示对所有设备进行操作。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **[{ *chassis-number \| virtual-chassis-number* **slot** *slot-number* }]]：显示指定成员设备或者PEX上风扇的状态信息。*chassis-number*表示设备在IRF中的成员编号；*virtual-chassis-number*表示PEX对应的虚拟框号，*slot-number*表示PEX在虚拟框中的槽位号。不指定**chassis**参数时，表示对所有设备/PEX进行操作。（分布式设备－IRF模式）（支持IRF3的设备）

**[time ***blink-time*]：闪烁的持续时间，取值范围为5～120，单位为秒。

**[stop**]：停止闪烁。

【使用指导】

配置**locator blink ***blink-time*命令后，指定设备上用于定位的LED灯会以间隔快闪的方式闪烁，并持续指定的时间。用户可根据LED灯的指示来定位设备所在的位置。

不同型号的设备用于定位的LED灯不同，请以设备的实际情况为准。如果设备支持Locator灯，则Locator灯闪烁；如果只有SYS灯，则SYS灯闪烁；如果只有RUN灯，则RUN灯闪烁。

*[blink-time*]时间到或者执行**locator blink stop**命令，则定位闪烁的LED灯会恢复正常点亮状态。

【举例】

\# 开始定位。

\<Sysname\> locator blink 30

\# 结束定位。

\<Sysname\> locator blink stop

**设备管理 \-- 设备管理配置命令 \-- lpu-type**

------------------------------------------------------------------------

![说明](设备管理命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[lpu-type**]命令用来配置设备支持的接口板类型。

【命令】

**[lpu-type**[ { **e-series** \| **f-series** }]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[e-series**]：配置设备只支持E系列的接口板。

**[f-series**]：配置设备只支持F系列的接口板。

【使用指导】

设备支持E系列的接口板和F系列的接口板。这两种类型的接口板不能互通，支持的特性有明显差异。请不要在同一台设备上同时插入这两种类型的接口板，即使插入，设备也只能识别指定类型的接口板。

修改设备支持的接口板类型后，须重启设备才能生效。

【举例】

\# 将设备支持的接口板类型配置为E系列。

\<Sysname\> system-view

Sysname lpu-type e-series

Changing the LPU type to support. Continue? [Y/N:y]

LPU type changed. The change will take effect after a reboot.

【相关命令】

·**display lpu-type**

**设备管理 \-- 设备管理配置命令 \-- memory-threshold**

------------------------------------------------------------------------

**[memory-threshold**]命令用来配置空闲内存告警的门限值。

**[undo memory-threshold**]命令用来恢复空闲内存告警的门限值。

【命令】

集中式设备：

**[memory-threshold minor ***minor-value*** severe ***severe-value*** critical ***critical-value ***normal ***normal-value*]

**[undo memory-threshold**]

分布式设备－独立运行模式/集中式IRF设备：

**[memory-threshold**** **slot** *slot-number*  **cpu** *cpu-number*  ] **minor** *minor-value* **severe** *severe-value* **critical** *critical-value* **normal** *normal-value*

**[undo memory-threshold ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[memory-threshold** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] **minor** *minor-value* **severe** *severe-value* **critical** *critical-value* **normal** *normal-value*]]

**[undo memory-threshold ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[minor ***minor-value*]：一级告警门限，单位为兆字节（MB），不同型号的设备取值范围不同，请以设备的实际情况为准；*minor-value*应小于等于*normal-value*；为0则表示关闭该级门限告警功能。

**[severe ***severe-value*]：二级告警门限，单位为兆字节（MB），不同型号的设备取值范围不同，请以设备的实际情况为准；*severe-value*必须小于等于*minor-value*；为0则表示关闭该级门限告警功能。

**[critical ***critical-value*]：三级告警门限，单位为兆字节（MB），不同型号的设备取值范围不同，请以设备的实际情况为准；*critical-value*必须小于等于*severe-value*；为0则表示关闭该级门限告警功能。

**[normal ***normal-value*]：系统内存恢复正常状态时的内存大小，单位为兆字节（MB），不同型号的设备取值范围不同，请以设备的实际情况为准；*normal-value*必须小于等于实际内存大小。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定单板/PEX。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

系统实时监控系统剩余空闲内存大小，当条件达到时，就产生相应的告警/告警解除通知，以便通知关联的业务模块/进程采取相应的措施，以便最大限度的利用内存，又能保证设备的正常运行。

设备支持一级、二级、三级告警门限，关于这些告警门限的详细介绍请参见"基础配置指导"中的"设备管理"。

【举例】

\#一级、二级、三级告警门限分别为64MB、48MB、32MB，当系统剩余空闲内存大于96MB时，恢复到正常状态。

\<Sysname\> system-view

Sysname memory-threshold minor 64 severe 48 critical 32 normal 96

【相关命令】

·**display ****memory-threshold**

**设备管理 \-- 设备管理配置命令 \-- memory-threshold usage**

------------------------------------------------------------------------

**[memory-threshold usage**]命令用来配置内存利用率阈值。

**[undo memory-threshold usage**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[memory-threshold usage **]*memory-threshold*

**[undo memory-threshold usage**]

分布式设备－独立运行模式/集中式IRF设备：

**[memory-threshold ****slot***slot-number* [ **cpu** *cpu-number*  ]]** usage ***memory-threshold*

**[undo memory-threshold ****slot***slot-number* [ **cpu** *cpu-number*  ]]** usage**

分布式设备－IRF模式：

**[memory-threshold** **chassis*** chassis-number***slot***slot-number* [ **cpu** *cpu-number*  ]]** usage ***memory-threshold*

**[undo memory-threshold ****chassis*** chassis-number***slot***slot-number* [ **cpu** *cpu-number*  ] ]**usage**

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[memory-threshold*]：内存利用率阈值百分比，取值范围为0～100。

**[slot**]*slot-number*：表示单板所在的槽位号，不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot**]*slot-number*：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定单板/PEX。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：设置单板的指定CPU的内存门限。*cpu-number*表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

系统每隔1分钟会对内存利用率进行采样，并将采样值和用户配置的内存利用率阈值比较。当采样值大时，则认为内存利用率过高，设备会发送Trap报文。

【举例】

\# 配置内存利用率阈值为80%。

\<Sysname\> system-view

Sysname memory-threshold chassis 1 slot 2 cpu 1 usage 80

【相关命令】

·**display memory-threshold**

**设备管理 \-- 设备管理配置命令 \-- monitor cpu-usage enable**

------------------------------------------------------------------------

**[monitor cpu-usage enable**]命令用来开启CPU利用率历史记录功能。

**[undo monitor cpu-usage enable**]命令用来关闭CPU利用率历史记录功能。

【命令】

集中式设备：

**[monitor cpu-usage enable**]

**[undo monitor cpu-usage enable**]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor cpu-usage enable ** **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor cpu-usage enable ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[monitor cpu-usage enable ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor cpu-usage enable ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【缺省情况】

CPU利用率历史记录功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号，不指定表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号，不指定表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定单板/PEX。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 打开CPU利用率历史记录功能。

\<Sysname\> system-view

Sysname monitor cpu-usage enable

【相关命令】

·**display cpu-usage configuration**

·**display cpu-usage history**

·**monitor cpu-usage interval**

**设备管理 \-- 设备管理配置命令 \-- monitor cpu-usage interval**

------------------------------------------------------------------------

**[monitor cpu-usage interval**]命令用来配置CPU利用率历史记录的采样周期。

【命令】

集中式设备：

**[monitor cpu-usage interval ***interval-value*]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor cpu-usage interval ***interval-value * **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[monitor cpu-usage interval ***interval-value * **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【缺省情况】

CPU利用率历史记录采样周期为1分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：CPU利用率历史记录采用周期，取值为5Sec、1Min或者5Min。输入该参数时，请完整输入，否则，系统会提示参数错误。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定单板/PEX。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 配置CPU利用率历史记录的采样周期为5秒。

\<Sysname\> system-view

Sysname monitor cpu-usage interval 5Sec

【相关命令】

·**display cpu-usage configuration**

·**display cpu-usage history**

·**monitor cpu-usage enable**

**设备管理 \-- 设备管理配置命令 \-- monitor cpu-usage threshold**

------------------------------------------------------------------------

**[monitor cpu-usage threshold**]命令用来配置CPU利用率阈值。

**[undo monitor cpu-usage threshold**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[monitor cpu-usage threshold ***cpu-threshold*]

**[undo monitor cpu-usage threshold**]

分布式设备－独立运行模式/集中式IRF设备：

**[monitor cpu-usage threshold ***cpu-threshold * **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor cpu-usage threshold ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[monitor cpu-usage threshold ***cpu-threshold * **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo monitor cpu-usage threshold ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【缺省情况】

与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cpu-threshold*]：CPU利用率阈值百分比，取值范围为0～100。

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示主用主控板。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示主设备。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis*** chassis-number ***slot** *slot-number*]：表示指定单板/PEX。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示全局主用主控板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

系统每隔1分钟会对CPU的利用率进行采样，并将采样值和用户配置的CPU利用率阈值比较。当采样值大时，则认为CPU利用率过高，设备会发送Trap报文。

【举例】

\# 配置CPU利用率阈值为80%。

\<Sysname\> system-view{.TerminalDisplayChar}

Sysname monitor cpu-usage threshold 80{.TerminalDisplayChar}

【相关命令】

·**display cpu-usage configuration**

**设备管理 \-- 设备管理配置命令 \-- password-recovery enable**

------------------------------------------------------------------------

**[password-recovery enable**]命令用来使能密码恢复功能。

**[undo password-recovery enable**]命令用来关闭密码恢复功能。

【命令】

**[password-recovery enable**]

**[undo password-recovery enable**]

【缺省情况】

密码恢复功能处于使能状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置密码恢复功能后，当用户忘记Console口认证密码或者登录认证失败，导致无法使用命令行操作设备时，可通过Boot ROM菜单清除该认证密码，再继续使用设备；关闭密码恢复功能后，设备将处于一个安全性更高的状态，即当出现上述情况时，若想继续使用Console口对设备进行命令行操作，只能通过Boot ROM菜单选择将设备恢复为出厂配置之后方可继续操作，这样可以有效地防止非法用户获取启动配置文件。

Boot ROM菜单中支持配置的选项与密码恢复功能的配置有关，详见产品的相关手册。

【举例】

\# 关闭密码恢复功能。

\<Sysname\> system-view

Sysname undo password-recovery enable

**设备管理 \-- 设备管理配置命令 \-- power-supply off**

------------------------------------------------------------------------

![说明](设备管理命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[power-supply off**]命令用来强制给指定单板或子卡断电。

【命令】

分布式设备－独立运行模式：

**[power-supply off slot ***slot-number * **subslot** *subslot-number* ]

分布式设备－IRF模式：

**[power-supply off chassis** *chassis-number* **slot** *slot-number* [ **subslot** *subslot-number* ]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

用户视图

【缺省级别】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[subslot ***subslot-number*]：表示子卡所在的子槽位号。不指定该参数时，表示所有子卡。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如果设备电量不足，且某些接口板处于空闲状态或者连接的为非关键网络节点时，可以手工停止给这些接口板供电，以便节约电能保证给重要接口板供电。

在IRF中，当成员设备上处于up状态的IRF物理端口都位于同一接口板上时，则不允许强制给该接口板断电，以免导致IRF分裂。（分布式设备---IRF模式）

【举例】

\# 强制给9号槽位的单板断电。（分布式设备－独立运行模式）

\<Sysname\> power-supply off slot 9

\# 强制给成员设备1的3号单板的单板断电。（分布式设备－IRF模式）

\<Sysname\> power-supply off chassis 1 slot 3

**设备管理 \-- 设备管理配置命令 \-- power-supply on**

------------------------------------------------------------------------

![说明](设备管理命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[power-supply on**]命令用来手工给指定单板或子卡供电。

【命令】

分布式设备－独立运行模式：

**[power-supply on slot ***slot-number* [ **subslot ** *subslot-number* ]]

分布式设备－IRF模式中：

**[power-supply on chassis** *chassis-number* **slot** *slot-number* [ **subslot** *subslot-number* ]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

用户视图

【缺省级别】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[subslot ***subslot-number*]：表示子卡所在的子槽位号。不指定该参数时，表示所有子卡。

【举例】

\# 手工给9号槽位的单板供电。（分布式设备－独立运行模式）

\<Sysname\> power-supply on slot 9

\# 手工给成员设备1的3号单板的单板供电。（分布式设备－IRF模式）

\<Sysname\> power-supply on chassis 1 slot 3

**设备管理 \-- 设备管理配置命令 \-- power-supply policy enable**

------------------------------------------------------------------------

![说明](设备管理命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[power-supply policy enable**]命令用来启用电源管理功能。

**[undo power-supply policy enable**]命令用来关闭电源管理功能。

【命令】

分布式设备－独立运行模式：

**[power-supply policy enable**]

**[undo power-supply policy enable**]

分布式设备－IRF模式：

**[power-supply policy chassis ***chassis-number ***enable**]

**[undo power-supply policy chassis ***chassis-number*** enable**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省级别】

network-admin

mdc-admin

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

【举例】

\# 启用电源管理功能。（集中式设备/分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname power-supply policy enable

\# 启用成员设备1的电源管理功能。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname power-supply policy chassis 1 enable

**设备管理 \-- 设备管理配置命令 \-- power-supply policy priority**

------------------------------------------------------------------------

**[power-supply policy priority**]命令用来设置指定槽位单板的电源管理优先级。

**[undo power-supply policy priority**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[power-supply policy slot ***slot-number*** priority** *priority*]

**[undo power-supply policy slot** *slot-number* **priority**]

分布式设备－IRF模式：

**[power-supply policy chassis ***chassis-number ***slot ***slot-number*** priority** *priority*]

**[undo power-supply policy chassis ***chassis-number*** slot** *slot-number* **priority**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省级别】

network-admin

mdc-admin

【参数】

*[priority*]：单板的电源管理优先级，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。本参数值越小表示单板的电源管理优先级越高。

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

请根据实际组网应用，将正在处理或将要处理重要业务的单板的优先级设置得高一些，以便在系统供电不足或者电力恢复时，优先保证对该单板的供电。

【举例】

\# 设置1号槽位的单板的电源管理优先级为10。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname power-supply policy slot 1 priority 10

\# 设置成员设备1上1号单板的电源管理优先级为10。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname power-supply policy chassis 1 slot 1 priority 10

**设备管理 \-- 设备管理配置命令 \-- power-supply policy redundant**

------------------------------------------------------------------------

![说明](设备管理命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[power-supply policy redundant**]命令用来配置冗余电源模块数。

**[undo** **power-supply policy redundant**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[power-supply policy redundant ***module-count*]

**[undo power-supply policy redundant**]

分布式设备－IRF模式：

**[power-supply policy chassis ***chassis-number ***redundant ***module-count*]

**[undo power-supply policy chassis ***chassis-number*** redundant**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省级别】

network-admin

mdc-admin

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

*[module-count*]：表示冗余电源模块数目，不同型号的设备支持的取值范围不同，用户可以通过帮助信息来获取设备支持的取值范围，但是该范围的上限是系统支持的最大冗余模块数，根据设备安插的接口板的数量和耗电量不同，用户实际能够设置的值会小于等于系统支持的最大冗余模块数。

【使用指导】

只有在使能电源管理功能后，冗余电源配置才会生效。

【举例】

\# 配置电源冗余模块数为3。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname power-supply policy redundant 3

\# 配置成员设备1的电源冗余模块数为3。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname power-supply policy chassis 1 redundant 3

**设备管理 \-- 设备管理配置命令 \-- reboot**

------------------------------------------------------------------------

**[reboot**]命令用来重启设备或者指定子卡。（集中式设备）

**[reboot**]命令用来重启指定单板、指定子卡或整个设备。（分布式设备－独立运行模式）

**[reboot**]命令用来重启指定成员设备、指定子卡或所有成员设备。（集中式IRF设备）

**[reboot**]命令用来重启指定成员设备、指定子卡或所有成员设备。（分布式设备－IRF模式）

【命令】

集中式设备：

**[reboot ** **subslot** *subslot-number* ]  **force**

分布式设备－独立运行模式/集中式IRF设备：

**[reboot ** **slot** *slot-number*  **subslot** *subslot-number*  ]  **force**

分布式设备－IRF模式：

**[reboot ** **chassis** *chassis-number*  **slot** *slot-number* [ **subslot** *subslot-number*  ] ]  **force**

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号或者PEX对应的虚拟框号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot** *slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[slot** *slot-number*]：表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[slot*** slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[subslot** *subslot-number*]：子卡所在的子槽位号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[force**]：强制重启：

·不指定该参数时，重启设备，系统会做一些保护性检查（如启动文件是否存在，是否正在写磁盘等），若检查不通过则退出处理，不会重启设备；

·指定该参数时，系统将不进行任何检查，直接执行重启操作。

【使用指导】

(1)分布式设备－独立运行模式：

·不指定**slot**参数，会导致整个设备重启。

·指定**slot**参数，不指定**subslot**参数，会重启指定单板。

需要注意的是：

·重新启动可能会导致业务中断，请谨慎使用该命令。

·如果主用启动文件损坏或者不存在，则不能通过**reboot**命令重启设备。此时，可以通过指定新的主用启动文件再重启。

·如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。

·使用**force**参数时，系统在重启时不会做任何保护性措施。重启后，可能导致文件系统损坏，请谨慎使用该参数。建议在系统故障或无法正常重启时，才使用该参数。

(2)集中式IRF设备：

·不指定**slot**参数，会导致所有成员设备重启。

·指定**slot**参数，不指定**subslot**参数，会重启指定成员设备。

需要注意的是：

·重新启动可能会导致业务中断，请谨慎使用该命令。

·如果主用启动文件损坏或者不存在，则不能通过**reboot**命令重启设备。此时，可以通过指定新的主用启动文件再重启。

·如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。

·使用**force**参数时，系统在重启时不会做任何保护性措施。重启后，可能导致文件系统损坏，请谨慎使用该参数。建议在系统故障或无法正常重启时，才使用该参数。

(3)分布式设备－IRF模式：

·不指定**chassis**和**slot**参数，则会重启所有成员设备。

·只指定**chassis**不指定**slot**参数，则会重启IRF中指定的成员设备。

·同时指定**chassis**和**slot**参数，则会重启IRF中指定的单板。

需要注意的是：

·重新启动可能会导致业务中断，请谨慎使用该命令。

·如果主用启动文件损坏或者不存在，则不能通过**reboot**命令重启设备。此时，可以通过指定新的主用启动文件再重启。

·如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。

·使用**force**参数时，系统在重启时不会做任何保护性措施。重启后，可能导致文件系统损坏，请谨慎使用该参数。建议在系统故障或无法正常重启时，才使用该参数。

【举例】

\# 当配置没有变化时，重启设备（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。

\<Sysname\> reboot

Start to check configuration with next startup configuration file, please wait\...\...\...DONE!

This command will reboot the device. Continue? [Y/N:y]

Now rebooting, please wait\...

\# 当配置有变化时，重启设备，并选择保存配置文件（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。

\<Sysname\> reboot

Start to check configuration with next startup configuration file, please wait\...\...\...DONE!

Current configuration will be lost after the reboot, save current configuration? [Y/N:y]

Please input the file name(\*.cfg)[flash:/startup.cfg]

(To leave the existing filename unchanged, press the enter key):

flash:/startup.cfg exists, overwrite? [Y/N:y]

Validating file. Please wait\...

Configuration is saved to flash successfully.

This command will reboot the device. Continue? [Y/N:y]

Now rebooting, please wait\...

\# 当配置有变化时，重启设备，但不保存配置文件（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。

\<Sysname\> reboot

Start to check configuration with next startup configuration file, please wait\...\...\...DONE!

Current configuration will be lost after the reboot, save current configuration? [Y/N:n]

This command will reboot the device. Continue? [Y/N:y]

Now rebooting, please wait\...

\# 强制重启设备。

\<Sysname\> reboot force

A forced reboot might cause the storage medium to be corrupted. Continue? [Y/N:y]

Now rebooting, please wait\...

\# 重启接口板（接口板所在的槽位号为2）（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。（分布式设备－独立运行模式）

\<Sysname\> reboot slot 2

Start to check configuration with next startup configuration file, please wait..

\...\....DONE!

This command will reboot the specified slot, Continue? [Y/N:y]

Now rebooting, please wait\...

\# 强制重启接口板（接口板所在的槽位号为2）。

\<Sysname\> reboot slot 2 force

A forced reboot might cause the storage medium to be corrupted. Continue? [Y/N:y]

Now rebooting, please wait\...

\# 重启成员设备2（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> reboot chassis 2

Start to check configuration with next startup configuration file, please wait..

\...\....DONE!

This command will reboot the specified chassis, Continue? [Y/N:y]

Now rebooting, please wait\...

\# 强制重启成员设备2。

\<Sysname\> reboot chassis 2 force

A forced reboot might cause the storage medium to be corrupted. Continue? [Y/N:y]

Now rebooting, please wait\...

\# 重启成员设备2上的2号接口板（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）。（分布式设备－IRF模式）

\<Sysname\> reboot chassis 2 slot 2

Start to check configuration with next startup configuration file, please wait..

\...\....DONE!

This command will reboot the specified slot, Continue? [Y/N:y]

Now rebooting, please wait\...

\# 强制重启成员设备2上的2号接口板。

\<Sysname\> reboot chassis 2 slot 2 force

A forced reboot might cause the storage medium to be corrupted. Continue? [Y/N:y]

Now rebooting, please wait\...

**设备管理 \-- 设备管理配置命令 \-- restore factory-default**

------------------------------------------------------------------------

**[restore factory-default**]命令用来将设备恢复到出厂状态。

【命令】

**[restore factory-default**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当设备使用场景更改，或者设备出现故障时，可以使用本命令来将设备恢复到出厂状态。执行该命令后，设备将只保留".bin"软件包、MAC地址、电子标签等维持设备正常工作必需的信息，其它文件和参数均恢复到出厂状态，例如，设备存储介质根目录下的所有配置文件（即后缀为".cfg"的文件）将被清除，设备在使用过程中生成的日志信息（即/logfile下的".log"文件以及logbuffer中的信息）、Trap信息、Debug信息将被清除，Boot ROM菜单中各选项的值将恢复到缺省值等。因此，请谨慎使用该命令。

【举例】

\# 将设备恢复到出厂状态。

\<Sysname\> restore factory-default

This command will restore the system to the factory default configuration and clear the operation data. Continue [Y/N:y]

Restoring the factory default configuration. This process might take a few minutes. Please wait\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\....Done.

Please reboot the system to place the factory default configuration into effect.

【相关命令】

·**reboot**

**设备管理 \-- 设备管理配置命令 \-- reset scheduler logfile**

------------------------------------------------------------------------

**[reset scheduler logfile**]命令用来清除Schedule日志文件的相关信息。

【命令】

**[reset scheduler logfile**]

【缺省情况】

无

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除Schedule日志文件的相关信息。

\<Sysname\> reset scheduler logfile

【相关命令】

·**display scheduler logfile**

**设备管理 \-- 设备管理配置命令 \-- reset version-update-record**

------------------------------------------------------------------------

![说明](设备管理命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset version-update-record**]命令用来清除设备启动软件包版本更新操作的记录。（集中式设备）

**[reset version-update-record**]命令用来清除主用主控板启动软件包版本更新操作的记录。（分布式设备－独立运行模式）

**[reset version-update-record**]命令用来清除主设备启动软件包版本更新操作的记录。（集中式IRF设备）

**[reset version-update-record**]命令用来清除全局主用主控板启动软件包版本更新操作的记录。（分布式设备－IRF模式）

【命令】

**[reset version-update-record**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除设备启动软件包版本更新操作的记录。

\<Sysname\> system-view

Sysname reset version-update-record

This command will delete all records of version update. Continue? [Y/N:y]

【相关命令】

·**display version-update-record**

**设备管理 \-- 设备管理配置命令 \-- save-power delay-timer**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[save-power delay-timer**]命令用来设置设备从节能唤醒状态切换到节能休眠状态的时间间隔。

**[undo save-power delay-timer**]命令用来恢复缺省情况。

【命令】

**[save-power delay-timer ***time*]

**[undo save-power delay-timer**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：设备从节能唤醒状态切换到节能休眠状态的时间间隔，单位为秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

使能节能功能后，设备可能处于节能休眠状态（**sleep**）或节能唤醒状态（**wake**）。当设备处于节能休眠状态时，只要用户按设备上的\<Mode\>按钮或者通过Console连接和设备之间有报文交互，设备会立即切换到节能唤醒状态；反之，当设备处于节能唤醒状态，且在*time*时间内用户没有按\<Mode\>按钮并且没有通过Console连接和设备之间有报文交互，设备会切换到节能休眠状态以便达到更节能的效果。

【举例】

\# 设置设备从节能唤醒状态切换到节能休眠状态的时间间隔为30秒。

\<Sysname\> system-view

Sysname save-power delay-timer 30

【相关命令】

·**save-power enable**

·**save-power mode**

**设备管理 \-- 设备管理配置命令 \-- save-power enable**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[save-power enable**]命令用来使能设备的节能功能。

**[undo save-power enable**]命令用来恢复缺省情况。

【命令】

**[save-power enable**]

**[undo save-power enable**]

【缺省情况】

节能功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能设备的节能功能。

\<Sysname\> system-view

Sysname save-power enable

【相关命令】

·**save-power delay-timer**

·**save-power mode**

**设备管理 \-- 设备管理配置命令 \-- save-power mode**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[save-power mode**]命令用于手工强制切换设备的节能状态。

【命令】

**[save-power mode**[ { **sleep** \| **wake** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sleep**]：将设备切换到节能休眠状态。处于该状态的设备会强制关闭除SYS指示灯以外的面板上的所有指示灯，并自动使能所有以太网接口的节能功能。

**[wake**]：将设备切换到节能唤醒状态。处于该状态的设备上的所有指示灯仍然正常亮、灭、闪烁，只是自动使能所有以太网接口的节能功能。

【使用指导】

使能节能功能后，设备可能处于节能休眠状态（**sleep**）或节能唤醒状态（**wake**），节能休眠状态比节能唤醒状态更节能。两种状态的切换由按键、报文或者定时器触发，使用**save-power mode**命令可以不需要按键也不需要等到定时器超时来实现节能状态之间的快速切换。

【举例】

\# 将设备切换到节能休眠状态。

\<Sysname\> save-power mode sleep

【相关命令】

·**save-power enable**

·**save-power delay-time**

**设备管理 \-- 设备管理配置命令 \-- scheduler job**

------------------------------------------------------------------------

**[scheduler job**]命令用来创建Job并进入Job视图。如果Job已创建，则直接进入Job视图。

**[undo scheduler job**]命令用来删除已创建的Job。

【命令】

**[scheduler job ***job-name*]

**[undo scheduler job ***job-name*]

【缺省情况】

没有创建Job。

【视图】

系统视图

【缺省级别】

network-admin

mdc-admin

【参数】

*[job-name*]：Job的名称，为1～47个字符的字符串，区分大小写。

【使用指导】

一个Job可以被多个Schedule引用。Job视图下用户可以通过**command**命令为Job分配命令。

【举例】

\# 创建名称为backupconfig的Job并进入Job视图。

\<Sysname\> system-view

Sysname scheduler job backupconfig

Sysname-job-backupconfig

【相关命令】

·**command**

·**scheduler schedule**

**设备管理 \-- 设备管理配置命令 \-- scheduler logfile size**

------------------------------------------------------------------------

**[scheduler logfile size**]命令用来设置Schedule日志文件的大小。

【命令】

**[scheduler logfile size ***value*]

【缺省情况】

Schedule日志文件的大小为16KB。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：Schedule日志文件的大小，取值范围为16～1024，单位是KB。

【使用指导】

Schedule日志文件用来记录Job下命令行的执行结果。如果该文件的大小超过了用户设置值，则系统会把老的记录删除，用来记录新的记录。如果要记录的日志信息超长，超过了日志文件的大小，则该日志超出的部分不会记录。

【举例】

\# 设置Schedule日志文件的大小为32KB。

\<Sysname\> system-view

Sysname scheduler logfile size 32

【相关命令】

·**display scheduler logfile**

**设备管理 \-- 设备管理配置命令 \-- scheduler reboot at**

------------------------------------------------------------------------

**[scheduler reboot at**]命令用来指定设备重启的具体时间和日期。

**[undo scheduler reboot**]命令用来取消重启时间的设置。

【命令】

**[scheduler reboot at** *time* [ *date* ]]

**[undo scheduler** **reboot**]

【缺省情况】

没有指定设备重启的具体时间和日期。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：设备重启的时间，格式为*HH:MM*。*HH*代表小时，取值范围为0～23，*MM*代表分钟，取值范围为0～59。

*[date*]：设备重启的日期，格式为*MM/DD/YYYY*（月/日/年）或者*YYYY/MM/DD*（年/月/日）。

·*YYYY*的取值范围为2000～2035；

·*MM*的取值范围为1～12；

·*DD*的取值范围与具体月份有关。

【使用指导】

如果没有指定*date*参数，并且：

·设置的时间点在当前时间之后，则设备将在当天的该时间点重启；

·设置的时间点在当前时间之前，则设备将在第二天的该时间点重启。

多次配置**scheduler reboot at**、**scheduler reboot delay**命令，最新配置生效。

如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。

需要注意的是，该命令会使设备在将来的某个时间点重新启动，从而导致业务中断，请谨慎使用。

【举例】

\# 假设系统的当前时间为2011年6月6日11:43，设置设备在当天中午12:00重启。

\<Sysname\> scheduler reboot at 12:00

Reboot system at 12:00:00 06/06/2011 (in 0 hours and 16 minutes). Confirm? [Y/N:]

【相关命令】

·**scheduler reboot delay**

**设备管理 \-- 设备管理配置命令 \-- scheduler reboot delay**

------------------------------------------------------------------------

**[scheduler reboot delay**]命令用来配置重启设备的延迟时间。

**[undo** **scheduler reboot**]命令用来取消延时重启配置。

【命令】

**[scheduler** **reboot** **delay** *time*]

**[undo scheduler** **reboot**]

【缺省情况】

没有配置重启设备的延迟时间。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：设备重启的等待时延，格式为*HH:MM*（小时:分钟）或*MM*（分钟）。

·使用*HH:MM*格式时，*MM*的取值范围为0～59，*HH:MM*的最大长度为6个字符。

·使用*MM*格式时，最大长度为6个字符。

【使用指导】

如果设备在准备重启时，用户正在进行文件操作，为了安全起见，系统将不会执行此次重启操作。

需要注意的是，该命令会使设备在将来的某个时间点重新启动，从而导致业务中断，请谨慎使用。

【举例】

\# 假设系统的当前时间为2011年6月6日11:48，配置设备在88分钟后重启。

\<Sysname\> scheduler reboot delay 88

Reboot system at 13:16 06/06/2011(in 1 hours and 28 minutes). Confirm? [Y/N:]

**设备管理 \-- 设备管理配置命令 \-- scheduler schedule**

------------------------------------------------------------------------

**[scheduler schedule**]命令用来创建Schedule并进入相应的Schedule视图。如果Schedule已创建，则直接进入Schedule视图。

**[undo scheduler schedule**]命令用来删除指定Schedule。

【命令】

**[scheduler schedule ***schedule-name*]

**[undo scheduler schedule ***schedule-name*]

【缺省情况】

没有创建Schedule。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[schedule-name*]：Schedule的名字，为1～47个字符的字符串，区分大小写。

【使用指导】

使用**scheduler schedule**命令可以配置定时执行任务，让设备在指定时间执行指定命令。

配置步骤如下：

(1)使用**scheduler job**命令创建Job。

(2)在Job视图下，使用**command**命令配置需要执行的命令。

(3)使用**scheduler schedule**命令创建Schedule*。*

(4)在Schedule视图下，使用**job**命令为Schedule分配Job。一个Schedule下可以分配多个Job，但必须是已创建的Job，否则分配失败。

(5)在Schedule视图下，使用**user-role**命令为Schedule配置用户角色。一个Schedule下最多可以分配64个角色。

(6)在Schedule视图下，使用**time at**、**time once**或者**time repeating**命令来配置任务执行的时间。一个Schedule下只能设置一个执行时间。

【举例】

\# 创建名为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

【相关命令】

·**job**

·**time at**

·**time ****once**

**设备管理 \-- 设备管理配置命令 \-- shutdown-interval**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[shutdown-interval**]命令用来设定定时检测的时间间隔。

**[undo shutdown-interval**]命令用来恢复缺省情况。

【命令】

**[shutdown-interval*** time*]

**[undo shutdown-interval**]

【缺省情况】

定时检测的时间间隔为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：定时检测的时间间隔，取值范围为1～300，单位为秒。

【使用指导】

某些协议模块在特定情况下会自动关闭某个端口，比如当使能了BPDU保护功能的端口收到配置消息时，MSTP协议模块将自动关闭该端口。同时，系统会启动一个检测定时器，如果直到定时器超时（即经过*time*秒之后），该端口仍处于关闭状态，协议模块则自动激活该端口，令其恢复到真实的物理状态。

需要注意的是，如果用户在端口定时检测过程中将检测时间间隔修改为T1，修改时刻距协议关闭端口时间间隔为T。若T\<T1，则被关闭的端口会再经过T1-T时间后被恢复；若T\>=T1，则被关闭的端口会立即恢复。例如当前*time*设置为30，当端口被协议模块关闭2秒（T=2）后，修改*time*为10（T1=10），则该接口会再经过8秒后被恢复；如果当前*time*为30，端口被协议模块关闭10秒后，修改*time*为2，则该端口会立即恢复。

【举例】

\# 设定定时检测时间间隔为100秒。

\<Sysname\> system-view

Sysname shutdown-interval 100

**设备管理 \-- 设备管理配置命令 \-- sysname**

------------------------------------------------------------------------

**[sysname**]命令用来设置设备的名称。

**[undo sysname**]用来恢复缺省情况。

【命令】

**[sysname** *sysname*]

**[undo sysname**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[sysname*]：设备名称，为1～64个字符的字符串。

【使用指导】

设备的名称对应于命令行接口的提示符，如设备的名称为Sysname，则用户视图的提示符为\<Sysname\>。

【举例】

\# 设置设备的名称为R2000。

\<Sysname\> system-view

Sysname sysname R2000

R2000

**设备管理 \-- 设备管理配置命令 \-- system-working-mode**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[system-working-mode**]命令用来配置设备的工作模式。

**[undo system-working-mode**]命令用来恢复缺省情况。

【命令】

**[system-working-mode**[ { **advance** \| **bridgee** \| **expert** \| **routee** \| **standard** }]]

**[undo system-working-mode**]

【缺省情况】

设备工作在标准模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advance**]：将设备的工作模式设置为高级模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bridgee**]：将设备的工作模式设置为二层增强模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[expert**]：将设备的工作模式设置为专家模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[routee**]：将设备的工作模式设置为三层增强模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[standard**]：将设备的工作模式设置为标准模式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

不同模式下设备支持的特性不同，或者相同的特性支持的规格不同，请根据实际需要配置。

要使修改的工作模式生效，必须重启设备。

【举例】

\# 将设备工作模式配置为高级模式。

\<Sysname\> system-view

Sysname system-working-mode advance

The system working mode is changed, it will take effect after system restart.

**设备管理 \-- 设备管理配置命令 \-- temperature-limit**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[temperature-limit**]命令用于设置设备的温度告警门限。

**[undo** **temperature-limit**]命令用来恢复缺省情况。

【命令】

集中式设备：

**[temperature-limit**[ { **hotspot** \| **inflow** \| **outflow** } *sensor-number* *lowlimit warninglimit* [ *alarmlimit* ]]]

**[undo temperature-limit**[ { **hotspot** \| **inflow** \| **outflow** } *sensor-number*]]

分布式设备－独立运行模式：

**[temperature-limit**[{ **slot** *slot-number* \| **vent** } { **hotspot** \| **inflow** \| **outflow** } *sensor-number* *lowlimit warninglimit* [ *alarmlimit* ]]]

**[undo temperature-limit **[{ **slot** *slot-number* \| **vent** } [\| **inflow** \| **outflow** } *sensor-number*]]

集中式]IRF设备：

**[temperature-limit** **slot** *slot-number*[ { **hotspot** \| **inflow** \| **outflow** } *sensor-number* *lowlimit warninglimit* [ *alarmlimit* ]]]

**[undo temperature-limit slot ***slot-number*[ [\| **inflow** \| **outflow** } *sensor-number*]]

分布式设备－]IRF模式：

**[temperature-limit** **chassis**[ *chassis-number* { **slot** *slot-number* \| **vent** } { **hotspot** \| **inflow** \| **outflow** } *sensor-number* *lowlimit warninglimit* [ *alarmlimit* ]]]

**[undo temperature-limit chassis**[ *chassis-number* { **slot** *slot-number* \| **vent** } { **hotspot** \| **inflow** \| **outflow** } *sensor-number*]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

**[slot ***slot-number*]：配置指定单板上温度传感器的温度门限。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[slot ***slot-number*]：配置指定成员设备上温度传感器的温度门限。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[vent**]：配置位于机框、风扇框上面的温度传感器的温度门限。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[hotspot**]：配置热点传感器的温度门限。热点传感器一般置于发热量较大的芯片附近，监测芯片温度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[inflow**]：配置入风传感器的温度门限。入风传感器一般置于入风口附近，监测环境温度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outflow**]：配置出风传感器的温度门限。出风传感器一般置于出风口附近，监测设备温度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[sensor-number*]：温度传感器的编号，取值为从1开始的正整数，每一个数字对应设备（单板）上的一个温度传感器。

*[lowlimit*]：低温告警门限，单位为摄氏度，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[warninglimit*]：一般级（Warning）高温告警门限，单位为摄氏度，不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但必须大于低温告警门限。

*[alarmlimit*]：严重级（Alarm）高温告警门限，单位为摄氏度，不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但必须大于一般级高温告警门限。

【使用指导】

如果温度低于低温告警门限，系统会生成日志信息和告警信息提示用户；如果温度高于Warning高温门限，系统会生成日志信息和告警信息提示用户；如果温度高于Alarm高温门限，系统一方面通过反复打印日志信息和告警信息提示用户，另一方面还会通过设备面板上的指示指示灯来告警。

配置时，需要注意的是：

·高温告警门限必须大于低温告警门限；

·Alarm高温告警门限必须大于Warning高温告警门限。

【举例】

\# 配置入风方向1号温度传感器，低温门限为-10摄氏度，Warning级高温门限为70摄氏度，Alarm级高温门限为100摄氏度。（集中式设备）

\<Sysname\> system-view

sysname temperature-limit inflow 1 -10 70 100

\# 配置0号单板上入风方向1号温度传感器，低温门限为-10摄氏度，Warning级高温门限为70摄氏度，Alarm级高温门限为100摄氏度。（分布式设备－独立运行模式）

\<Sysname\> system-view

sysname temperature-limit slot 0 inflow 1 -10 70 100

\# 配置成员设备1上入风方向1号温度传感器，低温门限为-10摄氏度，Warning级高温门限为70摄氏度，Alarm级高温门限为100摄氏度。（集中式IRF设备）

\<Sysname\> system-view

sysname temperature-limit slot 1 inflow 1 -10 70 100

\# 配置1号成员设备0号单板上入风方向1号温度传感器，低温门限为-10摄氏度，Warning级高温门限为70摄氏度，Alarm级高温门限为100摄氏度。（分布式设备－IRF模式）

\<Sysname\> system-view

sysname temperature-limit chassis 1 slot 0 inflow 1 -10 70 100

**设备管理 \-- 设备管理配置命令 \-- time at**

------------------------------------------------------------------------

**[time at**]命令用来配置在指定时刻执行Schedule。

**[undo time**]命令用来为Schedule取消执行时间配置。

【命令】

**[time at ***time date*]

**[undo time**]

【缺省情况】

没有为Schedule配置执行时间。

【视图】

Schedule视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：Schedule的执行时间，格式为*HH:MM*（小时:分钟）。*HH*取值范围为0～23，*MM*取值范围为0～59。

*[date*]：Schedule执行的日期，格式为*MM/DD/YYYY*（月/日/年）或者*YYYY/MM/DD*（年/月/日）。

·*YYYY*的取值范围为2000～2035；

·*MM*的取值范围为1～12；

·*DD*的取值范围与具体月份有关。

【使用指导】

配置的时间点必须晚于系统当前时间点，否则配置失败。

一个Schedule只能配置一个执行时间。因此，同一Schedule视图下，多次执行**time at**、**time once**或**time repeating**命令时，最新配置生效。

【举例】

\# 配置2011年5月11日1点1分执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time at 1:1 2011/05/11

【相关命令】

·**scheduler schedule**

**设备管理 \-- 设备管理配置命令 \-- time once**

------------------------------------------------------------------------

**[time once**]命令用来为Schedule配置执行时间。

**[undo time**]命令用来为Schedule取消执行时间配置。

【命令】

**[time**[ **once** **at** *time* [ **month-date** *month-day* \| **week-day** *week-day*&\<1-7\> ]]]

**[time once delay** *time*]

**[undo time**]

【缺省情况】

没有为Schedule配置执行时间。

【视图】

Schedule视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[at ***time*]：Schedule的执行时间，格式为*HH:MM*（小时:分钟）。*HH*取值范围为0～23，*MM*取值范围为0～59。

**[month-date ***month-day*]：Schedule在一个月中的哪天被执行。*month-day*表示日期，取值范围为1～31。如果指定了一个本月不存在的日期，则实际生效的时间为下一个月的该日期，比如，二月没有30号，则实际生效的时间为三月的30号。

**[week-day** *week-day*&\<1-7\>]：Schedule在一周中的哪（些）天被执行。*week-day*&\<1-7\>表示一周中任一天或几天的组合，*week-day*取值为：**Mon**、**Tue**、**Wed**、**Thu**、**Fri**、**Sat**、**Sun**，&\<1-7\>表示前面的参数最多可以输入7次。设置多天时，字符串之间用空格分开。

**[delay ***time*]：指定Schedule延迟执行的时间。格式为*HH:MM*（小时:分钟）或*MM*（分钟）。

·使用*HH:MM*格式时，*MM*的取值范围为0～59，*HH:MM*最大长度为6个字符。

·使用*MM*格式时，最大长度为6个字符。

【使用指导】

配置该命令后，Schedule在该设定时间点到达时执行，若当天/本月/本周该时间点已过去，则顺延到第二天/下月/下周。执行后下次再到达该时间点时Schedule不再执行。

一个Schedule只能配置一个执行时间。因此，同一Schedule视图下，多次执行**time at**、**time once**或**time repeating**命令时，最新配置生效。

【举例】

\# 当天的15点执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time once at 15:00

\# 最近到达的15号的15点执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time once at 15:00 month-date 15

\# 最近一个周一和周五的12点整执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time once at 12:00 week-day mon fri

\# 延迟10分钟执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time once delay 10

【相关命令】

·**scheduler schedule**

**设备管理 \-- 设备管理配置命令 \-- time repeating**

------------------------------------------------------------------------

**[time repeating**]命令用来配置重复执行Schedule的时间。

**[undo time**]命令用来为Schedule取消执行时间配置。

【命令】

**[time repeating ** **at** *time*  *date*  ] **interval** *interval-time*

**[time**[ **repeating at** *time* [ **month-date** [ *month-day* *\|* **last** ] \| **week-day** *week-day*&\<1-7\> ]]]

**[undo time**]

【缺省情况】

没有配置重复执行Schedule的时间。

【视图】

Schedule视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[at*** time*]：表示重复执行的时间，格式为*HH:MM*（小时:分钟）。*HH*取值范围为0～23，*MM*取值范围为0～59。不指定该参数时，表示从现在开始。

*[date*]：指定Schedule重复执行的开始日期，格式为*MM/DD/YYYY*（月/日/年）或者*YYYY/MM/DD*（年/月/日）。不指定该参数时，表示将来第一次到达time的时间点的日期。

·*YYYY*的取值范围为2000～2035；

·*MM*的取值范围为1～12；

·*DD*的取值范围与具体月份有关。

**[interval ***interval-time*]：指定重复执行的时间间隔。格式为*HH:MM*（小时:分钟）或*MM*（分钟）。

·使用*HH:MM*格式时，*MM*的取值范围为0～59，最大长度为6个字符。

·使用*MM*格式时，取值的最小值为1，最大长度为6个字符。

**[month-date **[[ *month-day* *\|* **last** ]]]：表示每月中的某一天。其中，*month-day*表示日期，取值范围为1～31。如果指定了一个本月不存在的日期，则实际生效的时间为下一个月的该日期，比如，二月没有30号，则实际生效的时间为三月的30号。**last**表示每月的最后一天。

**[week-day** *week-day*&\<1-7\>]：表示每周中的某（些）天。*week-day*&\<1-7\>表示一周中任一天或几天的组合，*week-day*取值为：**Mon**、**Tue**、**Wed**、**Thu**、**Fri**、**Sat**、**Sun**，&\<1-7\>表示前面的参数最多可以输入7次。设置多天时，字符串之间用空格分开。

【使用指导】

**[time repeating ** **at** *time*  *date*  ] **interval** *interval-time*表示从指定时间开始，周期性执行Schedule。

**[time**[ **repeating at** *time* [ **month-date** [ *month-day* *\|* **last** ] \| **week-day** *week-day*&\<1-7\> ]]]表示每月/每周的某（些）天重复执行Schedule。

一个Schedule只能配置一个执行时间。因此，同一Schedule视图下，多次执行**time at**、**time once**或**time repeating**命令时，最新配置生效。

【举例】

\# 配置从早上八点开始，每隔1小时执行一次名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time repeating at 8:00 interval 60

\# 配置从现在开始每天的12:00执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time repeating at 12:00

\# 配置从现在开始每个月5号的上午8点执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time repeating at 8:00 month-date 5

\# 配置从现在开始每个月的最后一天8点执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time repeating at 8:00 month-date last

\# 配置从现在开始每个周五和周六的上午8点执行名称为saveconfig的Schedule。

\<Sysname\> system-view

Sysname scheduler schedule saveconfig

Sysname-schedule-saveconfig time repeating at 8:00 week-day fri sat

【相关命令】

·**scheduler schedule**

**设备管理 \-- 设备管理配置命令 \-- usb disable**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[usb disable**]命令用来关闭设备上所有的USB接口。

**[undo usb disable**]命令用来打开设备上所有的USB接口。

【命令】

**[usb disable**]

**[undo usb disable**]

【缺省情况】

设备上所有的USB接口处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在执行**usb disable**命令前，请先使用**umount**命令卸载所有USB分区，否则命令执行失败。有关**umount**命令的详细介绍，请参见"基础配置命令参考"中的"文件系统管理"。

用户可通过USB口进行文件的上传和下载或者接USB 3G Modem模块。缺省状态下USB口处于开启状态，用户可根据需要关闭USB口。

缺省MDC支持该命令，非缺省MDC不支持。

【举例】

\# 关闭USB接口，请先umount所有USB分区。

\<Sysname\> umount usba0:

\<Sysname\> umount slot1\#[usba0:]

\<Sysname\> system-view

Sysname usb disable

\# 打开USB接口。

\<Sysname\> system-view

Sysname undo usb disable

**设备管理 \-- 设备管理配置命令 \-- user-role**

------------------------------------------------------------------------

**[user-role**]命令用来配置执行Schedule的定时任务时使用的用户角色。

**[undo user-role**]命令用来将已经配置的用户角色从Schedule中删除。

【命令】

**[user-role** *role-name*]

**[undo user-role ***role-name*]

【缺省情况】

Schedule执行定时任务时使用的用户角色，为创建该Schedule的用户的用户角色。

【视图】

Schedule视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[role-name*]：执行定时任务时使用的用户角色，为1～63个字符，区分大小写。可以是系统预定义的角色名称，包括network-admin、network-operator、mdc-admin、mdc-operator、level-0～level-15，也可以是自定义的用户角色名称。

【使用指导】

用户角色中定义了允许用户操作哪些系统功能、资源对象以及可执行哪些命令。设备支持的每条命令执行时都需要相应的用户角色，如果本命令中配置的用户角色不能执行**command**命令中指定的命令行，则会导致Schedule中的部分命令不能执行。管理员使用本命令可以限制低级别用户使用Schedule执行高级别命令行。

多次执行本命令可给Schedule配置多个用户角色，系统会使用这些用户角色权限的并集去执行Schedule。同一个Schedule最多可以配置64个用户角色。关于用户角色的详细描述请参见"基础配置指导"中的"RBAC"。

【举例】

\# 配置执行定时任务test时使用的用户角色为rolename。

\<sysname\> system-view

Sysname scheduler schedule test

Sysname-schedule-test user-role rolename

【相关命令】

·**command**

·**scheduler schedule**

**设备管理 \-- 设备管理配置命令 \-- warm-reboot**

------------------------------------------------------------------------

**[warm-reboot**]命令用来热重启设备，并可同时升级启动软件包。

【命令】

**[warm-reboot ** **file ipe** *ipe-filename* ]

**[warm-reboot **[[ **file** { **boot** *boot-package* \| **system** *system-package* \| **feature** *feature-package*&\<1-30\> } ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[file**]：用于在热重启设备时，升级启动软件包（该启动软件包会被设置为主用下次启动软件包）。

**[ipe*** ipe-filename*]：表示IPE（Image Package Envelope，复合软件包套件）文件的名称，以.ipe作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[boot ***boot-package*]：Boot包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[system** *system-package*]：System包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。

**[feature** *feature-package*]：Feature包的名称，以.bin作为后缀名，从flash、cf、usb开始最多可输入63个字符，不区分大小写。*feature-package*&\<1-30\>表示前面的参数最多可以输入30次。

【使用指导】

当配置该命令时，命令中指定的软件包必须放在存储介质根目录下，文件名中必须且只能包含存储介质的名称。

在热重启并同时升级时，要求如下（否则，热重启命令执行失败）：

·设备必须支持ISSU功能。

·设备工作在非IRF模式，且没有配置IRF3功能。

·新启动软件包/IPE文件的升级方式必须为增量升级或者软重启方式，为其它方式时，不能使用该方式升级。用户可以使用**display version comp-matrix**命令来显示软件版本兼容信息。关于ISSU和升级方式的详细介绍请参见"基础配置指导"中的"ISSU"。

【举例】

\# 热重启设备，并同时升级Feature包flash:/devkit.bin。

\<Sysname\> warm-reboot file feature flash:/devkit.bin

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? [Y/N:y]

Verifying the file flash:/devkit.bin on slot 1\...Done.

Upgrade summary according to following table:

flash:/devkit.bin

  Running Version             New Version

  None                        Demo 2601006

  Slot                        Upgrade Way

  1                           Warm Reboot

Upgrading software images to compatible versions. Continue? [Y/N:y]

This operation maybe take several minutes, please wait\...\.....

表1-24 warm-reboot命令显示信息描述表

字段

描述

This operation will delete the rollback point information for the previous upgrade and maybe get unsaved configuration lost. Continue? Y/N

当前操作会删除上一次的日志信息和回滚点，并且未保存的配置可能会丢失，询问用户是否继续执行升级操作

Verifying the file flash:/devkit.bin on slot 1\...Done.

检验软件包的合法性

Decompressing file *A* to *B*\...\...\...\...\...\...\...\...\...Done.

将文件从位置*A*解压缩到位置*B*。只有使用IPE文件升级时，才显示该信息

Upgrade summary according to following table

升级信息摘要

Running Version

设备当前运行的相同类型软件包的产品版本号

New Version

将要升级的软件包的产品版本号

Slot

设备成员编号只能为1

Upgrade Way

升级策略，取值为Warm Reboot，表示通过热重启方式升级

Upgrading software images to compatible versions. Continue? Y/N

询问用户是否执行兼容升级操作

This operation maybe take several minutes, please wait\...\.....

热重启过程需要一定时间，请稍候

**设备管理 \-- 设备管理配置命令 \-- xbar**

------------------------------------------------------------------------

![说明](设备管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[xbar**]命令用来配置主用主控板和备用主控板的负载模式。

【命令】

分布式设备－独立运行模式：

**[xbar **[{ **load-balance** \| **load-single** }]]

分布式设备－IRF模式：

**[xbar chassis ***chassis-number*[ { **load-balance** \| **load-single** }]]

【缺省情况】

主控板的负载模式为**load-single**。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chassis ***chassis-number*]：用来设置指定成员设备上主用主控板和备用主控板的负载模式。*chassis-number*表示设备在IRF中的成员编号。（分布式设备－IRF模式）

**[load-balance**]：设备的主用主控板和备用主控板共同参与报文的处理和转发。

**[load-single**]：只有主用主控板能处理和转发报文，备用主控板仅备份主用主控板的数据、监控主用主控板的状态。

【使用指导】

只有主用主控板和备用主控板同时在位时，配置的**load-balance**模式才会生效；否则，即便配置了**load-balance**模式，主用主控板也会自动切换到**load-single**模式。

【举例】

\# 配置主用主控板和备用主控板的负载模式为**load-balance**。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname xbar load-balance

\# 配置成员设备2上主用主控板和备用主控板的负载模式为**load-balance**。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname xbar chassis 2 load-balance

【相关命令】

·**display xbar**
