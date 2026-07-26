
**QCN \-- QCN配置命令 \-- display qcn cp interface**

------------------------------------------------------------------------

**[display qcn cp interface**]命令用来显示CP端的统计信息，包括接口对应CND绑定的proflie ID、通过的报文数、丢弃的报文数和发送的CNM报文数。

【命令】

**[display qcn cp interface** [ *interface-type interface-number*   **priority** *priority-value* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有二层以太网接口下的统计信息。

**[priority*** priority-value*]：CNPV优先级，取值范围为0～7。如果未指定本参数，将显示设备加入的所有CND的统计信息。

【举例】

\# 显示所有二层以太网接口下的统计信息。

\<Sysname\> display qcn cp interface

Interface: GE1/0/1

 CNPV 1: CP profile 1

  Passed   : 100000 (Packets)

  Discarded: 10 (Packets)

  CNM count: 3000 (Packets)

CNPV 2: CP profile default

  Passed   : 200000 (Packets)

  Discarded: 20 (Packets)

  CNM count: 3000 (Packets)

Interface: GE1/0/2

 CNPV 1: CP profile 1

  Passed   : 100000 (Packets)

  Discarded: 10 (Packets)

  CNM count: 3000 (Packets)

 CNPV 2: CP profile default

  Passed   : 200000 (Packets)

  Discarded: 20 (Packets)

  CNM count: 3000 (Packets)

表1-1 display qcn cp interface命令显示信息描述表

字段

描述

Interface

接口

CNPV

CNPV对应CDN绑定的profile

Passed

通过报文数

Discarded

丢弃报文数

CNM count

发送的CNM报文数

【相关命令】

·**reset qcn cp interface**

**QCN \-- QCN配置命令 \-- display qcn global**

------------------------------------------------------------------------

**[display qcn global**]命令用来显示QCN的全局运行信息。

【命令】

集中式设备：

**[display qcn global**]

分布式设备－独立运行模式/集中式IRF设备：

**[display qcn global** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display qcn global** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板上QCN的全局运行信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上QCN的全局运行信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上QCN的全局运行信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主用设备上QCN的全局运行信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上QCN的全局运行信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备上QCN的全局运行信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上QCN的全局运行信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上QCN的全局运行信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上QCN的全局运行信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上QCN的全局运行信息。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示QCN的全局运行信息。

\<Sysname\> display qcn global chassis 1 slot 1

Chassis 1 Slot 1:

QCN global status: Enabled

 CNPV  Mode   Defense-mode    Alternate  CP-profile

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 1     admin  interior-ready  4          default

 2     auto   -               0          1

 3     auto   -               0          1

表1-2 display qcn global命令显示信息描述表

字段

描述

QCN global status

QCN全局使能状态：

·Enabled：使能

·Disabled：未使能

CNPV

拥塞通知优先级

Mode

模式选择方式：

·auto：LLDP协商方式

·admin：配置方式

Defense-mode

端口保护模式：

·disabled：配置后，接口的优先级映射按优先级映射表起作用，不受任何QCN配置影响

·edge：CNPV优先级的报文需要被改写成隔离优先级

·interior：优先级保持不变，不按优先级映射表映射。同interiorReady模式的差异是，出方向需要删除CN tag

·interior-ready：优先级保持不变，不按优先级映射表映射。出方向时保留CN tag

·全局下配置成auto时，显示为"-"，表示每个接口独立协商，无全局统一的保护模式

Alternate

隔离优先级

CP-profile

CP profile ID

**QCN \-- QCN配置命令 \-- display qcn interface**

------------------------------------------------------------------------

**[display qcn interface**]命令用来显示QCN的接口运行信息。

【命令】

**[display qcn interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将显示所有二层以太网接口的运行信息。

【举例】

\# 显示QCN的接口运行信息。

\<Sysname\> display qcn interface

Interface: GE1/0/1

 CNPV  Mode   Defense-mode     Alternate

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 1     comp   interior-ready   4

 2     admin  edge             0

 3     auto   edge             0

Interface: GE1/0/2

 CNPV  Mode   Defense-mode     Alternate

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 1     comp   interior-ready   4

 2     admin  edge             0

 3     auto   edge             0

表1-3 display qcn interface命令显示信息描述表

字段

描述

Interface

接口

CNPV

拥塞通知优先级

Mode

接口保护模式的选择方式，取值包括：

·auto：LLDP协商方式

·admin：配置方式

·comp：使用全局的保护模式。接口下配置的选择方式会覆盖全局的选择方式

Defense-mode

端口保护模式

Alternate

隔离优先级

**QCN \-- QCN配置命令 \-- display qcn profile**

------------------------------------------------------------------------

![说明](QCN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display qcn profile**]命令用来显示QCN的profile运行信息。

【命令】

集中式设备：

**[display qcn profile **[[ *profile-id* \| **default** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display qcn profile**[ [ *profile-id* \| **default** ]  **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display qcn profile**[ [ *profile-id* \| **default** ]  **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[profile-id*]：显示指定profile的运行信息。*profile-id*的取值范围与设备的型号有关，请以设备的实际情况为准。

**[default**]：显示缺省profile（即ID为0的profile）的运行信息。

**[slot*** slot-number*]：显示指定单板上QCN的profile运行信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上QCN的profile运行信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上QCN的profile运行信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主用设备上QCN的profile运行信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上QCN的profile运行信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备上QCN的profile运行信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上QCN的profile运行信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的QCN的profile运行信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上QCN的profile运行信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上QCN的profile运行信息。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

如果未指定*profile-id*和**default**参数，将显示所有profile的运行信息。

【举例】

\# 显示QCN的profile运行信息。

\<Sysname\> display qcn profile chassis 2 slot 1

Chassis 2 Slot 1:

 Profile  Set-point   Weight

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 default  26000       1

 1        30000       2

表1-4 display qcn profile命令显示信息描述表

字段

描述

Profile

CP profile参数

Set-point

期望队列，单位为byte

Weight

权重

**QCN \-- QCN配置命令 \-- qcn enable**

------------------------------------------------------------------------

**[qcn enable**]命令用来开启QCN功能。

**[undo qcn enable**]命令用来关闭QCN功能。

【命令】

**[qcn enable**]

**[undo qcn enable**]

【缺省情况】

QCN功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启QCN功能后，其它QCN配置才能生效。

【举例】

\# 开启QCN功能。

\<Sysname\> system-view

Sysname qcn enable

**QCN \-- QCN配置命令 \-- qcn port priority**

------------------------------------------------------------------------

**[qcn port priority**]命令用来配置指定接口指定优先级的保护模式选择方式。

**[undo qcn port priority**]命令用来恢复缺省情况。

【命令】

**[qcn port priority**[ *priority-value* { **admin** [ **defense-mode** { **disabled** \| **edge** \| **interior** \| **interior-ready** } **alternate** *alternate-value* ] \| **auto** }]]

**[undo** **qcn** **port** **priority** *priority-value*]

【缺省情况】

以全局配置为准。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-value*]：CNPV优先级，取值范围为0～7。

**[admin**]：配置方式。

**[defense-mode**]：接口保护模式，缺省为disabled模式。

**[disabled**]：接口的优先级映射按优先级映射表起作用，不受QCN配置影响。

**[edge**]：CNPV优先级的报文需要被改写成隔离优先级。

**[interior**]：优先级保持不变，不按优先级映射表映射。出方向时删掉CN tag。

**[interior-ready**]：优先级保持不变，不按优先级映射表映射。出方向时保留CN tag。

**[alternate ***alternate-value*]：隔离优先级，取值范围为0～7，缺省为0。此隔离优先级不能和已有CNPV域冲突。

**[auto**]：LLDP协商方式。

【使用指导】

如果设备还没有加入对应CND，不能在接口下配置保护模式选择方式。

对于接口而言，接口下的配置优于全局配置生效。

【举例】

\# 配置在CNPV为1的CND中接口GigabitEthernet1/0/1的保护模式为disabled，隔离优先级为0。

\<Sysname\> system-view

Sysname qcn priority 1 auto

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qcn port priority 1 admin defense-mode disabled alternate 0

\# 配置接口GigabitEthernet1/0/2的模式选择方式为LLDP协商方式。

\<Sysname\> system-view

Sysname qcn priority 2 admin

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 qcn port priority 2 auto

【相关命令】

·**qcn priority**

**QCN \-- QCN配置命令 \-- qcn priority**

------------------------------------------------------------------------

**[qcn priority**]命令用来配置CNPV，加入CND。

**[undo qcn priority**]命令用来退出CND，同时删除此CND下的所有配置。

【命令】

**[qcn priority ***priority-value*[ { **admin** [ **defense-mode** { **disabled** \| **edge** \| **interior** \| **interior-ready** } **alternate** *alternate-value* ] \| **auto** }]]

**[undo qcn priority ***priority-value*]

【缺省情况】

设备未加入任何CND。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-value*]：CNPV优先级，取值范围为0～7。此CNPV优先级不能和全局或者接口下的admin模式下的隔离优先级冲突。

**[admin**]：配置方式。

**[defense-mode**]：接口保护模式，缺省为interior模式。

**[disabled**]：接口的优先级映射按优先级映射表起作用，不受QCN配置影响。

**[edge**]：CNPV优先级的报文需要被改写成隔离优先级。

**[interior**]：优先级保持不变，不按优先级映射表映射。出方向时删掉CN tag。

**[interior-ready**]：优先级保持不变，不按优先级映射表映射。出方向时保留CN tag。

**[alternate*** alternate-value*]：隔离优先级，取值范围为0～7，缺省为0。此隔离优先级不能和已有CNPV域冲突。

**[auto**]：LLDP协商方式。

【使用指导】

配置**auto**方式后，接口保护模式由LLDP协商得到，隔离优先级为小于CNPV且最接近CNPV的优先级值，如果小于CNPV的优先级值都被域占用，隔离优先级为大于CNPV且最接近CNPV的未被占用的优先级值。

【举例】

\# 配置设备加入CND，CNPV为2，模式选择方式为LLDP协商方式。

\<Sysname\> system-view

Sysname qcn priority 2 auto

\# 配置设备加入CND，CNPV为1，模式选择方式为配置方式，保护模式为disabled，隔离优先级为0。

\<Sysname\> system-view

Sysname qcn priority 1 admin defense-mode disabled alternate 0

【相关命令】

·**qcn ****port priority**

**QCN \-- QCN配置命令 \-- qcn priority profile**

------------------------------------------------------------------------

![说明](QCN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[qcn priority******profile**]命令用来为指定CND绑定profile。

**[undo qcn priority proflie**]命令用来恢复缺省情况。

【命令】

**[qcn priority ***priority-value ***profile ***profile-id*]

**[undo qcn priority ***priority-value ***proflie**]

【缺省情况】

CND绑定缺省profile。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-value*]：CNPV优先级，取值范围为0～7。

*[profile-id*]：指定的profile ID。此处不包括缺省profile ID。

【使用指导】

如果设备还没有加入对应CND或指定的profile不存在，则不能绑定profile。

【举例】

\# 为CNPV值为2的CND绑定profile 2。

\<Sysname\> system-view

Sysname qcn priority 2 profile 2

**QCN \-- QCN配置命令 \-- qcn proflie**

------------------------------------------------------------------------

![说明](QCN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[qcn profile**]命令用来创建profile。

**[undo qcn profile**]命令用来删除profile。

【命令】

**[qcn profile*** profile-id ***set-point*** length-value*** weight ***weight-value*]

**[undo qcn profile ***profile-id*]

【缺省情况】

没有创建profile。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-id*]：指定的profile ID。系统自动创建缺省profile，ID为0，参数不能修改。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[set-point** *length-value*]：期望队列长度，单位为byte。取值范围与设备的型号有关，请以设备的实际情况为准。

**[weight ***weight-value*]：权重参数。取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 创建profile，ID为1，期望队列长度为28000bytes，权重为1。

\<Sysname\> system-view

Sysname qcn profile 1 set-point 28000 weight 1

**QCN \-- QCN配置命令 \-- reset qcn cp interface**

------------------------------------------------------------------------

**[reset qcn cp interface**]命令用来清除CP端的统计信息。

【命令】

**[reset qcn cp interface** [ *interface-type interface-number*   **priority** *priority-value* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。如果未指定本参数，将清除所有二层[以太网接口下的统计信息。]

**[priority** *[priority-value*]]：CNPV优先级，取值范围为0～7。如果未指定本参数，将清除对应接口加入的所有CNPV域统计信息。

【举例】

\# 清除所有域所有二层[以太网接口]CP端的统计信息。

\<Sysname\> reset qcn cp interface

【相关命令】

·**display qcn cp interface**
