<!-- CMD-INDEX
  apply poe-profile                   | PoE接口视图          | L33
  apply poe-profile interface         | 系统视图             | L83
  display poe device                  | 任意视图             | L139
  display poe interface               | 任意视图             | L283
  display poe interface power         | 任意视图             | L563
  display poe power-usage             | 任意视图             | L663
  display poe pse                     | 任意视图             | L905
  display poe pse interface           | 任意视图             | L1173
  display poe pse interface power     | 任意视图             | L1317
  display poe-power                   | 任意视图             | L1411
  display poe-profile                 | 任意视图             | L1799
  display poe-profile interface       | 任意视图             | L1913
  poe disconnect                      | 系统视图             | L1955
  poe enable                          | PoE接口视图/PoE profile视图 | L2007
  poe enable pse                      | 系统视图             | L2065
  poe legacy enable                   | 系统视图             | L2113
  poe max-power                       | PoE接口视图/PoE profile视图 | L2171
  poe max-power (System view)         | 系统视图             | L2227
  poe mode                            | PoE接口视图/PoE profile视图 | L2293
  poe pd-description                  | PoE接口视图          | L2349
  poe pd-policy priority              | 系统视图             | L2391
  poe power max-value                 |                  | L2437
  poe priority                        | PoE接口视图/PoE profile视图 | L2509
  poe priority (system view)          | 系统视图             | L2583
  poe pse-policy priority             | 系统视图             | L2645
  poe temperature-protection          | 系统视图             | L2695
  poe update                          | 系统视图             | L2743
  poe-profile                         | 系统视图             | L2803
  poe utilization-threshold           | 系统视图             | L2873
-->

**PoE \-- PoE配置命令 \-- apply poe-profile**

------------------------------------------------------------------------

**[apply poe-profile**]命令用来将PoE profile应用到当前PoE接口。

**[undo apply poe-profile**]命令用来取消PoE profile在当前PoE接口的应用。

【命令】

**[apply poe-profile**[ { **index** *index* \| **name** *profile-name* }]]

**[undo apply poe-profile**[ { **index** *index* \| **name** *profile-name* }]]

【缺省情况】

没有将PoE profile应用到当前PoE接口。

【视图】

PoE接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[index*** index*]：PoE profile的索引，取值范围为1～100。

**[name*** profile-name*]：PoE profile的名称，为1～15个字符的字符串，区分大小写。

【举例】

\# 将名为forIPphone的PoE profile应用到PoE接口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 apply poe-profile name forIPphone

【相关命令】

·**apply poe-profile interface**

·**display poe-profile**

**PoE \-- PoE配置命令 \-- apply poe-profile interface**

------------------------------------------------------------------------

**[apply poe-profile interface**]命令用来将PoE profile应用到一个或多个PoE接口。

**[undo apply poe-profile interface**]命令用来取消PoE profile在PoE接口的应用。

【命令】

**[apply poe-profile **[{ **index** *index* *\|* **name** *profile-name* } **interface** *interface-range*]]

**[undo apply poe-profile **[{ **index** *index* *\|* **name** *profile-name* } **interface** *interface-range*]]

【缺省情况】

PoE profile没有应用到任何接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[index*** index*]：PoE profile的索引，取值范围为1～100。

**[name*** profile-name*]：PoE profile的名称，为1～15个字符，区分大小写。

*[interface-range*]：以太网接口范围，表示多个以太网接口。表示方式为*interface-range*＝ *interface-type interface-number* [ **to** *interface-type interface-number* ]。其中，*interface-type* *interface-number*为接口类型和接口编号。起始接口号要小于结束接口号，结束接口要和起始接口是同种类型。接口范围可以任意，如果指定范围内存在不支持PoE的接口，PoE配置文件应用时将忽略这类接口。

【举例】

\# 将名称为forIPphone的PoE profile应用到PoE接口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname apply poe-profile name forIPphone interface gigabitethernet 1/0/1

\# 将索引为1的PoE profile应用到PoE接口GigabitEthernet1/0/2至GigabitEthernet1/0/8。

\<Sysname\> system-view

Sysname apply poe-profile index 1 interface gigabitethernet 1/0/2 to gigabitethernet 1/0/8

【相关命令】

·**apply poe-profile**

·**display poe-profile interface**

**PoE \-- PoE配置命令 \-- display poe device**

------------------------------------------------------------------------

**[display poe device**]命令用来显示PSE（Power Sourcing Equipment，供电设备）的相关信息。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display poe device**]

分布式设备－IRF模式：

**[display poe device ** **chassis** *chassis-number* ]

集中式设备－IRF模式：

**[display** **poe** **device** [ **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：显示指定成员设备上所有PSE的相关信息。*chassis-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－IRF模式）

**[slot** *slot-number*]：显示指定成员设备上所有PSE的相关信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式设备－IRF模式）

【举例】

\# 显示PSE的相关信息。（显示信息与设备的型号相关，请以设备的实际情况为准）（单PSE设备）

\<Sysname\> display poe device

 PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model

 1        0          0          48        0              Off     LSP1POEA

\# 显示PSE的相关信息。（显示信息与设备的型号相关，请以设备的实际情况为准）（多PSE设备）

\<Sysname\> display poe device

 PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model

 7        2         0           24        370            Off     LSP2LTSUC

 10       3         0           24        370            Off     LSP2LTSUC

\# 显示所有PSE的相关信息。（显示信息与设备的型号相关）（分布式设备－IRF模式）

\<Sysname\> display poe device

Chassis 1：

 PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model

 4        1         0           1         200            Off    LSBMPOEGV48TP

 7        1         4           8         200            Off    LSBMPOEGV48TP

Chassis 2：

 PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model

 43       10        4           8         200            Off    LSBMPOEGV48TP

\# 显示所有PSE的相关信息。（显示信息与设备的型号相关）（集中式设备－IRF模式）

\<Sysname\> display poe device

Slot 1：

 PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model

 4        1         0           1         200            Off    LSBMPOEGV48TP

 7        1         4           8         200            Off    LSBMPOEGV48TP

Slot 2：

 PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model

 43       10        4           8         200            Off    LSBMPOEGV48TP

表1-1 display poe device命令显示信息描述表

字段

描述

Chassis 1

成员设备1上PSE的相关信息（分布式设备－IRF模式）

Slot 1

成员设备1上PSE的相关信息（集中式设备－IRF模式）

PSE ID

PSE编号

Slot No.

PSE所在槽位号

SSlot No.

PSE所在子槽位号

PortNum

PSE上PoE接口的数量

MaxPower(W)

PSE最大供电功率（单位为：瓦）

State

PSE状态：

·On：PSE正在供电

·Off：PSE停止供电

·Faulty：PSE故障

Model

PSE型号

**PoE \-- PoE配置命令 \-- display poe interface**

------------------------------------------------------------------------

**[display poe interface**]命令用来显示设备指定PoE接口的供电状态。

【命令】

**[display poe interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型及接口编号，显示指定PoE接口的供电状态。如果未指定本参数，则显示所有PoE接口的供电状态。

【举例】

\# 显示PoE接口GigabitEthernet1/0/1的供电状态。

\<Sysname\> display poe interface gigabitethernet 1/0/1

 PoE Status                         : Enabled

 Power Priority                    : Critical

 Oper                                : On

 IEEE Class                         : 1

 Detection Status                  : Delivering power

 Power Mode                         : Signal

 Current Power                      : 11592    mW

 Average Power                      : 11610    mW

 Peak Power                          : 11684    mW

 Max Power                           : 15400    mW

 Electric Current                   : 244      mA

 Voltage                              : 51.7     V

 PD Description                      : IP Phone For Room 101

表1-2 display poe interface命令显示信息描述表

字段

描述

PoE status

PoE接口远程供电功能是否开启：

·Enabled：开启

·Disabled：关闭

Power Priority

PoE接口供电优先级：

·Critical：最高

·High：高

·Low：低

Oper

PoE接口工作状态：

·Off：供电功能处于关闭状态

·On：正在正常供电

·Power-lack：PSE剩余保证功率不够，导致无法对优先级为Critical的PoE接口供电

·Power-deny：拒绝供电，PD要求功率大于配置功率

·Power-itself：外接设备正在自己供电

·Power-limit：正在受限供电，PD要求功率大于配置功率，PSE仍按配置功率供电

不同型号的设备支持的PoE接口工作状态不同，请以设备的实际情况为准

IEEE Class

由IEEE规定的PD功率等级，取值为：0、1、2、3、4、-

其中，"-"表示不支持，该值的支持情况与设备的型号有关，请以设备的实际情况为准

Detection Status

PoE接口检测状态：

·Disabled：PoE接口供电功能处于关闭状态

·Searching：正在搜索PD

·Delivering power：正在向PD供电

·Fault：错误

·Test：测试状态

·Other fault：其他错误状态

·PD disconnected：PD未连接

不同型号的设备支持的PoE接口检测状态不同，请以设备的实际情况为准

Power Mode

PoE接口供电方式：

·Signal：信号线供电方式

·Spare：空闲线供电方式

不同型号的设备支持的PoE接口供电方式不同，请以设备的实际情况为准

Current Power

PoE接口当前功率

包括PD消耗功率和传输损耗。一般损耗不超过1W，损耗的具体情况与设备的型号有关，请以设备的实际情况为准

Average Power

PoE接口平均功率

Peak Power

PoE接口峰值功率

Max Power

PoE接口最大功率

Electric Current

PoE接口当前电流

Voltage

PoE接口当前电压

PD Description

PoE接口所连接PD的描述信息，用于辅助用户识别PD的类型和位置等

\# 显示设备所有PoE接口的供电状态。

\<Sysname\> display poe interface

 Interface    PoE       Priority  CurPower  Oper      IEEE  Detection

                                      (W)                   Class Status

 GE1/0/1      Enabled   Low        4.4       On         1      Delivering Power

 GE1/0/2      Enabled   Critical  0.0       On         -      Disabled

 GE1/0/3      Enabled   Low        0.0       On         -      Disabled

 GE1/0/4      Enabled   Critical  0.0       On         -      Searching

 GE1/0/5      Enabled   Low        4.0       On         2      Delivering Power

 GE1/0/6      Enabled   Low        0.0       On         -      Disabled

 GE1/0/7      Disabled  Low        0.0       Off        -      Fault

   \-\--  On State Ports: 2; Used: 8.4(W); Remaining: 171.6(W)  \-\--

表1-3 display poe interface命令显示信息描述表

字段

描述

Interface

PoE接口名称简称

PoE

PoE接口远程供电功能是否开启：

·Enabled：开启

·Disabled：关闭

Priority

PoE接口供电优先级：

·Critical：最高

·High：高

·Low：低

CurPower

PoE接口当前功率

Oper

PoE接口工作状态：

·Off：供电功能处于关闭状态

·On：正在正常供电

·Power-lack：剩余保证功率不够，导致无法给Critical接口供电

·Power-deny：拒绝供电，PD要求功率大于配置功率

·Power-itself：外接设备正在自己供电

·Power-limit：正在受限供电，PD要求功率大于配置功率，PSE仍按配置功率供电

不同型号的设备支持的PoE接口工作状态不同，请以设备的实际情况为准

IEEE Class

由IEEE规定的PD功率等级，取值为：0、1、2、3、4、-

其中，"-"表示不支持，该值的支持情况与设备的型号有关，请以设备的实际情况为准

Detection Status

PoE接口检测状态：

·Disabled：PoE接口供电处于关闭状态

·Searching：正在搜索PD

·Delivering Power：正在向PD供电

·Fault：错误

·Test：测试状态

·Other Fault：其他错误状态

·PD Disconnected：PD未连接

不同型号的设备支持的PoE接口检测状态不同，请以设备的实际情况为准

On State Ports

正在供电的PoE接口数量

Used

当前供电PoE接口消耗的功率

Remaining

系统总剩余功率

**PoE \-- PoE配置命令 \-- display poe interface power**

------------------------------------------------------------------------

**[display poe interface power**]命令用来显示PoE接口的功率信息。

【命令】

**[display poe interface power ** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定接口类型及接口编号，显示指定PoE接口的功率信息。如果未指定本参数，则显示所有PoE接口的功率信息。

【举例】

\# 显示PoE接口GigabitEthernet1/0/1的功率信息。

\<Sysname\> display poe interface power gigabitethernet 1/0/1

Interface    Current   Peak      Max       PD Description

               (W)       (W)       (W)

 GE1/1        15.0      15.3      15.4      Access Point on Room 509 for Peter

\# 显示所有PoE接口的功率信息。

\<Sysname\> display poe interface power

Interface    Current   Peak      Max       PD Description

               (W)       (W)       (W)

 GE1/0/25    4.4        4.5       4.6         IP Phone in Room 309 for Peter Smith

 GE1/0/26    4.4        4.5       15.4        IP Phone in Room 409 for Peter Pan

 GE1/0/27    15.0      15.3       15.4        Access Point in Room 509 for Peter

 GE1/0/28    0.0        0.0        0.0        IP Phone in Room 609 for Peter John

 GE1/0/29    0.0        0.0        0.0        IP Phone in Room 709 for Jack

 GE1/0/30    0.0        0.0        0.0        IP Phone in Room 809 for Alien

\-\-- On State Ports: 3; Used: 23.8(W);  Remaining: 776.2(W) \-\--

表1-4 display poe interface power命令显示信息描述表

字段

描述

Interface

PoE接口简称

CurPower

PoE接口当前功率

PeakPower

PoE接口峰值功率

MaxPower

PoE接口最大功率

PD Description

PoE接口连接PD描述信息，用于辅助用户识别PD的类型和位置等

Ports On

正在供电的PoE接口数量

Used

所有PoE接口当前消耗功率

Remaining

系统总剩余功率

**PoE \-- PoE配置命令 \-- display poe power-usage**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display poe power-usage**]命令用来显示PoE电源的功率和各PSE的功率信息。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display poe power-usage**]

分布式设备－IRF模式：

**[display poe power-usage ** **chassis** *chassis-number* ]

集中式设备－IRF模式：

**[display** **poe** **power-usage** [ **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：显示指定成员设备上PoE电源的功率和各PSE的功率信息。*chassis-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－IRF模式）

**[slot** *slot-number*]：显示指定成员设备上PoE电源的功率和各PSE的功率信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式设备－IRF模式）

【举例】

\# 显示PoE电源的功率和各PSE的功率信息。

\<Sysname\> dis poe power-usage

 PoE Current Power                    : 12    W

 PoE Max Power                         : 2000  W

 PoE Max Guaranteed Power            : 2000  W

 PoE Remaining Allocable Power      : 1800  W

 PoE Remaining Guaranteed Power     : 2000  W

 Powered PoE Ports                     : 1

 Statistics by PSE:

 PSE ID  Max     Current  Peak     Average  Remaining      Powered

         (W)     (W)       (W)      (W)        Guaranteed(W) Ports

 5       200     12        12        6          200             1

\# 显示PoE电源的功率和各PSE的功率信息。（分布式设备－IRF模式）

\<Sysname\> display poe power-usage

Chassis 1 :

 PoE Current Power                   : 600   W

 PoE Max Power                        : 2000  W

 PoE Max Guaranteed Power           : 1000  W

 PoE Remaining Allocable Power      : 800   W

 PoE Remaining Guaranteed Power    : 600   W

 Powered PoE Ports                    : 60

 Statistics by PSE:

 PSE ID   Max    Current    Peak    Average    Remaining          Powered

          (W)     (W)         (W)     (W)         Guaranteed(W)     Ports

 4        300     200         230     205         100                 20

 7        400     300         345     290         200                 30

 10       500     100         120     110         300                 10

Chassis 2 :

 PoE Current Power                   : 600   W

 PoE Max Power                        : 2000  W

 PoE Max Guaranteed Power           : 1000  W

 PoE Remaining Allocable Power    : 800   W

 PoE Remaining Guaranteed Power    : 600   W

 Powered PoE Ports                   : 60

 Statistics by PSE:

 PSE ID   Max    Current    Peak    Average    Remaining          Powered

          (W)     (W)         (W)     (W)         Guaranteed(W)     Ports

 35       300     200         230     205         100                 20

\# 显示PoE电源的功率和各PSE的功率信息。（集中式设备－IRF模式）

\<Sysname\> display poe power-usage

Slot 1 :

 PoE Current Power                    : 600   W

 PoE Max Power                         : 2000  W

 PoE Max Guaranteed Power            : 1000  W

 PoE Remaining Allocable Power      : 800   W

 PoE Remaining Guaranteed Power     : 600   W

 Powered PoE Ports                     : 60

 Statistics by PSE:

 PSE ID   Max    Current    Peak    Average    Remaining          Powered

          (W)     (W)         (W)     (W)         Guaranteed(W)     Ports

 4        300     200         230     205         100                 20

 7        400     300         345     290         200                 30

 10       500     100         120     110         300                 10

Slot 2 :

 PoE Current Power                     : 600   W

 PoE Max Power                          : 2000  W

 PoE Max Guaranteed Power             : 1000  W

 PoE Remaining Allocable Power       : 800   W

 PoE Remaining Guaranteed Power      : 600   W

 Powered PoE Ports                     : 60

 Statistics by PSE:

 PSE ID   Max    Current    Peak    Average    Remaining          Powered

          (W)     (W)         (W)     (W)         Guaranteed(W)     Ports

 35       300     200         230     205         100                 20

表1-5 display poe power-usage命令显示信息描述表

字段

描述

Chassis 1

成员设备1上PoE电源的功率和各PSE的功率信息（分布式设备－IRF模式）

Slot 1

成员设备1上PoE电源的功率和各PSE的功率信息（集中式设备－IRF模式）

PoE Current Power

PSE当前消耗功率总和

PoE Max Power

PoE最大功率

PoE Max Guaranteed Power

PoE最大保证功率，即电源提供给优先级为Critical的PSE的最大功率

PoE Remaining Allocable Power

PoE剩余可分配功率=PoE最大功率--已经开启的PSE的最大功率之和

PoE Remaining Guaranteed Power

PoE剩余保证功率=PoE最大保证功率－设备中优先级为Critical的PSE最大功率之和（通常PoE最大保证功率＝PoE最大功率）

Powered PoE Ports

当前设备正在供电的PoE接口总数

PSE ID

PSE编号

Max

PSE最大功率

Current

PSE当前功率

Peak

PSE峰值功率

Average

PSE平均功率

Remaining Guaranteed

PSE剩余保证功率=PSE最大保证功率－该PSE中优先级为Critical的PoE接口最大功率之和（通常PSE最大保证功率＝PSE最大功率）

Powered Ports

PSE正在供电的PoE接口数量

**PoE \-- PoE配置命令 \-- display poe pse**

------------------------------------------------------------------------

**[display poe pse**]命令用来显示PSE的信息。

【命令】

单PSE设备：

**[display poe pse**]

多PSE设备：

**[display poe pse ** *pse-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[pse-id*]：PSE编号。如果不指定该参数，则显示设备上所有在位的PSE的信息。

【举例】

\# 显示设备的PSE的信息。（单PSE设备）

\<Sysname\> display poe pse

 PSE ID                                    : 1

 Slot NO.                                  : 0

 PSE Model                                 : LSBMPOEGV48TP

 PSE Status                                : Enabled

 PSE Preempted                             : No

 Power Priority                            : Low

 Current Power                             : 130      W

 Average Power                             : 20       W

 Peak Power                                : 240      W

 Max Power                                 : 200      W

 Remaining Guaranteed Power             : 120      W

 PSE CPLD Version                         : 100

PSE Software Version                    : 200

 PSE Hardware Version                    : 100

Legacy PD Detection                     : Disabled

 Power Utilization Threshold            : 80

PSE Power Policy                         : Disabled

 PD Power Policy                          : Disabled

 PD Disconnect-Detection Mode           : DC

\# 显示PSE 7的信息。（多PSE设备）

\<Sysname\> display poe pse 7

 PSE ID                                      : 7

 Slot No.                                    : 2

 PSE Model                                   : LSBMPOEGV48TP

 PSE Status                                  : Enabled

 PSE Preempted                               : No

 Power Priority                              : Low

 Current Power                               : 130      W

 Average Power                               : 20       W

 Peak Power                                   : 240      W

 Max Power                                     : 200      W

 Remaining Guaranteed Power                : 120      W

PSE CPLD Version                            : 100

 PSE Software Version                       : 200

PSE Hardware Version                       : 100

 Legacy  PD Detection                       : Disabled

 Power Utilization Threshold              : 80

PSE Power Policy: Disabled

PD Power Policy                           : Disabled

 PD Disconnect-Detection Mode             : DC

\# 显示PSE 7的信息。（分布式设备－IRF模式）

\<Sysname\> display poe pse 7

 PSE ID                                       : 7

 Chassis                                      : 1

 Slot No.                                     : 2

 SSlot No.                                    : 0

 PSE Model                                    : LSBMPOEGV48TP

 PSE Status                                   : Disabled

 PSE Preempted                               : No

 Power Priority                              : Low

 Current Power                               : 0        W

 Average Power                               : 0        W

 Peak Power                                     : 0        W

 Max Power                                    : 200      W

 Remaining Guaranteed Power                : 200      W

PSE CPLD Version                            : 100

 PSE Software Version                       : 200

PSE Hardware Version                       : 100

 Legacy PD Detection                        : Disabled

 Power Utilization Threshold               : 80

 PSE Power Policy                            : Disabled

 PD Power Policy                             : Disabled

 PD Disconnect Detection Mode              : DC

表1-6 display poe pse命令显示信息描述表

字段

描述

PSE ID

PSE编号

Slot No.

PSE所在槽号

SSlot No.

PSE所在的子槽位号

Chassis

PSE所在设备的成员编号（分布式设备－IRF模式）

PSE Model

PSE模块型号

PSE Status

PSE供电状态：

·Enabled：已使能

·Disabled：未使能

Preempted

PSE供电抢占状态（该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准）

·No：表示该PSE没有被抢占

·Yes：表示该PSE虽然被开启了，但是被其他PSE抢占了，无法供电

Power Priority

PSE供电优先级

Current Power

PSE当前功率

Average Power

PSE平均功率

Peak Power

PSE峰值功率

Max Power

PSE最大功率

Remaining Guaranteed Power

PSE剩余保证功率=PSE最大保证功率-该PSE中优先级为Critical的接口最大功率之和

PSE CPLD Version

PSE CPLD（Complex Programmable Logical Device，复杂可编程逻辑器件）版本

PSE Software Version

PSE软件版本

PSE Hardware Version

PSE硬件版本

Legacy PD Detection

PSE非标准PD检测：

·Enabled：开启

·Disabled：关闭

Power Utilization Threshold

PSE功率告警阈值

PSE Power Policy

PSE功率管理策略模式

PD Power Policy

PD功率管理策略模式

PD Disconnect Detection Mode

PD断开检测方式

**PoE \-- PoE配置命令 \-- display poe pse interface**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display poe pse interface**]命令用来显示指定PSE上PoE接口的供电状态。

【命令】

**[display poe pse*** pse-id*** interface**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pse*** pse-id*]：PSE编号，可以用**display poe device**命令查看PSE编号和槽号的对应关系。

【举例】

\# 显示PSE 7上连接的所有PoE接口的供电状态。

\<Sysname\> display poe pse 7 interface

 Interface   PoE        Priority  CurPower  Oper                IEEE     Detection

                                      (W)                             Class    Status

 GE1/0/1     Enabled   Low        4.4        On                   1         Delivering Power

 GE1/0/2     Enabled   Critical  0.0        Power-lack          -        Disabled

 GE1/0/3     Enabled   Low        0.0        Power-deny          -        Disabled

 GE1/0/4     Enabled   Critical  0.0        On                   -         Searching

 GE1/0/5     Enabled   Low        4.0        Power-limit        2         Delivering Power

 GE1/0/6     Enabled   Low        0.0        Power-itself       -         Disabled

 GE1/0/7     Disabled  Low        0.0        Off                  -         Fault

   \-\--  On State Ports: 2; Used: 8.4(W); Remaining: 171.6 (W)  \-\--

表1-7 display poe pse interface命令显示信息描述表

字段

描述

Interface

PoE接口简称

PoE

PoE接口远程供电功能是否开启：

·Enabled：开启

·Disabled：关闭

Priority

PoE接口供电优先级：

·Critical：最高

·High：高

·Low：低

CurPower

PoE接口当前功率

Oper

PoE接口工作状态：

·Off：供电功能处于关闭状态

·On：正在正常供电

·Power-lack：剩余保证功率不够，导致无法给Critical接口供电

·Power-deny：拒绝供电，PD要求功率大于配置功率

·Power-itself：外接设备正在自己供电

·Power-limit：正在受限供电，PD要求功率大于配置功率，PSE仍按配置功率供电

不同型号的设备支持的PoE接口工作状态不同，请以设备的实际情况为准

IEEE Class

PD功率等级

Detection Status

PoE接口检测状态：

·Disabled：PoE接口供电处于关闭状态

·Searching：正在搜索PD

·Delivering Power：正在向PD供电

·Fault：错误

·Test：测试状态

·Other Fault：其他错误状态

·PD Disconnected：PD未连接

不同型号的设备支持的PoE接口检测状态不同，请以设备的实际情况为准

On State Ports

正在供电的PoE接口数量

Used

该PSE上供电PoE接口消耗的功率

Remaining

此PSE上剩余功率

**PoE \-- PoE配置命令 \-- display poe pse interface power**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display poe pse interface power**]命令用来显示指定PSE上PoE接口的功率信息。

【命令】

**[display poe pse ***pse-id* **interface power**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pse*** pse-id*]：PSE编号，可以用**display poe device**命令查看PSE编号和槽号的对应关系。

【举例】

\# 显示PSE 7连接的PoE接口的功率信息。

\<Sysname\> display poe pse 7 interface power

Interface  Current   Peak       Max        PD Description

            (W)        (W)        (W)

 GE1/0/25  4.4        4.5        4.6         IP Phone on Room 309 for Peter Smith

 GE1/0/26  4.4        4.5        15.4        IP Phone on Room 409 for Peter Pan

 GE1/0/27  15.0       15.3       15.4        Access Point on Room 509 for Peter

 GE1/0/28  0.0        0.0        5.0         IP Phone on Room 609 for Peter John

 GE1/0/29  0.0        0.0        4.0         IP Phone on Room 709 for Jack

 GE1/0/30  0.0        0.0        5.0         IP Phone on Room 809 for Alien

   \-\--  On State Ports: 3; Used: 23.8(W);  Remaining: 776.2(W) \-\--

表1-8 display poe pse interface power命令显示信息描述表

字段

描述

Interface

PoE接口简称

Current

PoE接口当前功率

Peak

PoE接口峰值功率

Max

PoE接口最大功率

PD Description

PoE接口连接PD描述信息，用于辅助用户识别PD的类型和位置等

Ports On

正在供电的PoE接口数量

Used

所有PoE接口当前消耗功率

Remaining

此PSE上的剩余功率

**PoE \-- PoE配置命令 \-- display poe-power**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display poe-power**]命令用来显示PoE电源的信息。

【命令】

集中式设备/分布式设备－独立运行模式：

**[display poe-power**]

分布式设备－IRF模式：

**[display poe-power ** **chassis** *chassis-number* ]

集中式设备－IRF模式：

**[display** **poe-power** [ **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：显示指定成员设备的PoE电源的信息。*chassis-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－IRF模式）

**[slot** *slot-number*]：显示指定成员设备的PoE电源的信息。*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式设备－IRF模式）

【举例】

\# 显示PoE电源的信息。

\<Sysname\> display poe-power

 PoE Current Power                    : 1870     W

 PoE Average Power                    : 2100     W

 PoE Peak Power                        : 2350     W

 PoE Max Power                          : 2000     W

 PoE Nominal Power                     : 2500     W

 PoE Current Electric Current        : 3.00     A

 PoE Current Voltage                   : 55.00    V

 PoE Lower Input Threshold            : 111.22   V

 PoE Upper Input Threshold            : 131.00   V

 PoE Lower Output Threshold           : 45.00    V

 PoE Upper Output Threshold           : 57.00    V

 PoE Hardware Version                  : 0002

 PoE Software Version                  : 0001

 PoE Power Supplies                     : 2

 PoE Power Supply 1:

 Manufacturer                          : Tyco Electronics Com

 Type                                    : PSE2500-A

 Status                                  : Normal

 PoE Power Supply 2:

 Manufacturer                           : Tyco Electronics Com

 Type                                    : PSE2500-B

 Status                                  : Normal

\# 显示PoE电源的信息。（分布式设备－IRF模式）

\<Sysname\> display poe-power

Chassis 1 ：

 PoE Current Power                     : 1870     W

 PoE Average Power                     : 2100     W

 PoE Peak Power                         : 2350     W

 PoE Max Power                          : 2000     W

 PoE Nominal Power                     : 2500     W

 PoE Current Electric Current        : 3.00     A

 PoE Current Voltage                   : 55.00    V

 PoE Lower Input Threshold            : 111.22   V

 PoE Upper Input Threshold            : 131.00   V

 PoE Lower Output Threshold           : 45.00    V

 PoE Upper Output Threshold           : 57.00    V

 PoE Hardware Version                  : 0002

 PoE Software Version                  : 0001

 PoE Power Supplies                    : 2

 PoE Power Supply 1:

     Manufacturer                       : Tyco Electronics Com

     Type                                 : PSE2500-A

     Status                              : Normal

 PoE Power Supply 2:

     Manufacturer                       : Tyco Electronics Com

     Type                                : PSE2500-B

     Status                              : Normal

Chassis 2 ：

PoE Current Power                      : 1870     W

 PoE Average Power                     : 2100     W

 PoE Peak Power                         : 2350     W

 PoE Max Power                           : 2000     W

 PoE Nominal Power                      : 2500     W

 PoE Current Electric Current         : 3.00     A

 PoE Current Voltage                    : 55.00    V

 PoE Lower Input Threshold             : 111.22   V

 PoE Upper Input Threshold             : 131.00   V

 PoE Lower Output Threshold            : 45.00    V

 PoE Upper Output Threshold           : 57.00    V

 PoE Hardware Version                   : 0002

 PoE Software Version                   : 0001

 PoE Power Supplies                      : 2

 PoE Power Supply 1:

 Manufacturer                             : Tyco Electronics Com

 Type                                       : PSE2500-A

 Status                                     : Normal

 PoE Power Supply 2:

 Manufacturer                              : Tyco Electronics Com

 Type                                        : PSE2500-B

 Status                                      ：Normal

\# 显示PoE电源的信息。（集中式设备－IRF模式）

\<Sysname\> display poe-power

Slot 1 ：

 PoE Current Power                     : 1870     W

 PoE Average Power                     : 2100     W

 PoE Peak Power                        : 2350     W

 PoE Max Power                          : 2000     W

 PoE Nominal Power                     : 2500     W

 PoE Current Electric Current        : 3.00     A

 PoE Current Voltage                   : 55.00    V

 PoE Lower Input Threshold            : 111.22   V

 PoE Upper Input Threshold            : 131.00   V

 PoE Lower Output Threshold           : 45.00    V

 PoE Upper Output Threshold           : 57.00    V

 PoE Hardware Version                  : 0002

 PoE Software Version                  : 0001

 PoE Power Supplies                    : 2

 PoE Power Supply 1:

     Manufacturer                       : Tyco Electronics Com

     Type                                : PSE2500-A

     Status                              : Normal

 PoE Power Supply 2:

     Manufacturer                       : Tyco Electronics Com

     Type                                 : PSE2500-B

     Status                              : Normal

Slot 2 ：

PoE Current Power                      : 1870     W

 PoE Average Power                     : 2100     W

 PoE Peak Power                        : 2350     W

 PoE Max Power                          : 2000     W

 PoE Nominal Power                     : 2500     W

 PoE Current Electric Current        : 3.00     A

 PoE Current Voltage                   : 55.00    V

 PoE Lower Input Threshold            : 111.22   V

 PoE Upper Input Threshold            : 131.00   V

 PoE Lower Output Threshold           : 45.00    V

 PoE Upper Output Threshold           : 57.00    V

 PoE Hardware Version                  : 0002

 PoE Software Version                  : 0001

 PoE Power Supplies                    : 2

 PoE Power Supply 1:

 Manufacturer                           : Tyco Electronics Com

 Type                                    : PSE2500-A

 Status                                  : Normal

 PoE Power Supply 2:

 Manufacturer                           : Tyco Electronics Com

 Type                                    : PSE2500-B

 Status                                  ：Normal

表1-9 display poe-power命令显示信息描述表

字段

描述

Chassis 1

成员设备1的相关信息（分布式设备－IRF模式）

Slot 1

成员设备1的相关信息（集中式设备－IRF模式）

PoE Current Power

PoE当前功率

PoE Average Power

PoE平均功率

PoE Peak Power

PoE峰值功率

PoE Max Power

PoE最大供电功率

PoE Nominal Power

PoE额定功率

PoE Current Electric Current

PoE当前电流

PoE Current Voltage

PoE当前电压

PoE Lower Input Threshold

输入交流电欠压阈值

PoE Upper Input Threshold

输入交流电过压阈值

PoE Lower Output Threshold

输出直流电欠压阈值

PoE Upper Output Threshold

输出直流电过压阈值

PoE Hardware Version

PoE硬件版本号

PoE Software Version

PoE软件版本号

PoE Power Supplies

PoE电源数目

Manufacturer

PoE电源制造商，当设备不支持获取该参数时，该信息将显示为NONE

Type

PoE电源类型，当设备不支持获取该参数时，该信息将显示为NONE

Status

PoE电源状态：

·Normal：正常

·Absent：不在位

·Off：关机

·Active：主用正常

·Standby ：备用正常

·Balanced：负载分担

·Redundant：冗余备份

·Alarm：告警

·Faulty：故障

不同型号的设备支持的PoE电源状态不同，请以设备的实际情况为准

**PoE \-- PoE配置命令 \-- display poe-profile**

------------------------------------------------------------------------

**[display poe-profile**]命令用来显示PoE配置文件的相关信息。

【命令】

**[display poe-profile **[[ **index** *index* \| **name** *profile-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[index*** index*]：PoE配置文件的索引，取值范围为1～100。

**[name*** profile-name*]：PoE配置文件的名称，为1～15个字符的字符串，区分大小写。

【使用指导】

如果不指定参数，将显示当前已存在的所有的PoE配置文件的配置和应用信息。

【举例】

\# 显示当前的所有PoE配置文件的相关信息。

\<Sysname\> display poe-profile

 PoE Profile     Index   ApplyNum  Interfaces     Configuration

 forIPphone      1        6          GE1/0/5         poe enable

                                        GE1/0/6        poe priority critical

                                        GE1/0/7

                                        GE1/0/8

                                        GE1/0/9

                                        GE1/0/10

 forAP            2        2          GE1/0/11       poe enable

                                        GE1/0/12       poe max-power 14000

   \-\--  Total PoE profiles: 3, total ports: 0  \-\--

\# 显示索引为1的PoE配置文件的相关信息。

\<Sysname\> display poe-profile index 1

 PoE Profile     Index   ApplyNum  Interfaces   Configuration

 forIPphone      1        6          GE1/0/5       poe enable

                                       GE1/0/6       poe priority critical

                                       GE1/0/7

                                       GE1/0/8

                                       GE1/0/9

                                       GE1/0/1

   \-\--  Total ports: 0  \-\--

表1-10 display poe-profile命令显示信息描述表

字段

描述

PoE Profile

PoE配置文件的名称

Index

PoE配置文件的索引

ApplyNum

应用到的PoE接口数量

Interfaces

应用了PoE配置文件的PoE接口名称简称

Configuration

PoE配置文件的配置项

Total PoE profiles

创建的PoE配置文件数目

total ports

应用PoE配置文件的PoE接口数目

**PoE \-- PoE配置命令 \-- display poe-profile interface**

------------------------------------------------------------------------

**[display poe-profile interface**]命令用来显示指定PoE接口当前生效的PoE配置文件配置项和应用的所有信息。

【命令】

**[display poe-profile interface ***interface-type interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interfece-number*]：指定接口类型及接口编号。

【举例】

\# 显示PoE接口GigabitEthernet1/0/1的当前PoE配置文件配置和应用的所有信息。

\<Sysname\> display poe-profile interface gigabitethernet 1/0/1

 PoEProfile     Index   ApplyNum  Interface   Effective configuration

 forIPphone      1        6          GE1/0/1    poe enable

                                                    poe priority critical

因为PoE配置文件的配置项（Configuration）可能只有部分应用成功，所以显示的是该接口当前生效的配置项（Effective configuration），其它字段的描述请参见[表]1-10(?-1319701084#_Ref216168243)。

**PoE \-- PoE配置命令 \-- poe disconnect**

------------------------------------------------------------------------

**[poe disconnect**]命令用来配置PD断开检测的方式。

**[undo poe disconnect**]命令用来恢复缺省情况。

【命令】

**[poe disconnect**[ { **ac** \| **dc** }]]

**[undo poe disconnect**]

【缺省情况】

PD断开检测的方式与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ac**]：PD断开检测方式为交流检测方式。

**[dc**]：PD断开检测方式为直流检测方式。

【使用指导】

改变PD断开的检测方式，可能会导致连接的PD断电，请谨慎使用。

由于不同型号的设备采用的的PoE芯片不同，用户在配置时采用哪种检测方式以设备的实际情况为准。

【举例】

\# 配置PD断开检测的方式为直流检测方式。

\<Sysname\> system-view

Sysname poe disconnect dc

【相关命令】

·**display poe pse**

**PoE \-- PoE配置命令 \-- poe enable**

------------------------------------------------------------------------

**[poe enable**]命令用来开启PoE接口远程供电功能。

**[undo poe enable**]命令用来关闭PoE接口远程供电功能。

【命令】

**[poe enable**]

**[undo poe enable**]

【缺省情况】

PoE接口远程供电功能处于关闭状态。

【视图】

PoE接口视图/PoE profile视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在PoE profile视图下配置时，如果该PoE profile已经应用到PoE接口，需先取消该PoE profile在PoE接口的应用。

·在接口视图下配置时，若已用PoE配置文件对该PoE接口进行过配置，应先取消PoE配置文件在该PoE接口的应用。

【举例】

\# 开启PoE接口远程供电功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 poe enable

\#在PoE profile abc中，开启PoE接口远程供电功能。

\<Sysname\> system-view

Sysname poe-profile abc

Sysname-poe-profile-abc-1 poe enable

【相关命令】

·**poe-profile**

·**display poe interface**

**PoE \-- PoE配置命令 \-- poe enable pse**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[poe enable pse**]命令用来开启PSE的远程供电功能。

**[undo poe enable pse**]命令用来恢复缺省情况。

【命令】

**[poe enable pse ***pse-id*]

**[undo** **poe enable pse** *pse-id*]

【缺省情况】

PSE远程供电功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pse-id*]：PSE编号。

【举例】

\# 开启PSE 7的远程供电功能。

\<Sysname\> system-view

Sysname poe enable pse 7

【相关命令】

·**display poe pse**

**PoE \-- PoE配置命令 \-- poe legacy enable**

------------------------------------------------------------------------

**[poe legacy enable**]命令用来开启PSE的检测非标准PD功能。

**[undo poe legacy enable**]命令用来恢复缺省情况。

【命令】

单PSE设备：

**[poe legacy enable**]

**[undo** **poe legacy enable**]

多PSE设备：

**[poe legacy enable** **pse** *pse-id*]

**[undo** **poe legacy enable** **pse** *pse-id*]

【缺省情况】

PSE检测非标准PD功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pse*** pse-id*]：PSE编号。

【举例】

\# 开启PSE的检测非标准PD功能。（单PSE设备）

\<Sysname\> system-view

Sysname poe legacy enable

\# 开启PSE 7的检测非标准PD功能。（多PSE设备）

\<Sysname\> system-view

Sysname poe legacy enable pse 7

【相关命令】

·**display poe pse**

**PoE \-- PoE配置命令 \-- poe max-power**

------------------------------------------------------------------------

**[poe max-power**]命令用来配置PoE接口的最大功率。

**[undo poe max-power**]命令用来恢复缺省情况。

【命令】

**[poe max-power** *max-power*]

**[undo poe max-power**]

【缺省情况】

PoE接口的最大功率为15400毫瓦。

【视图】

PoE接口视图/PoE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-power*]：为PoE接口分配的最大供电功率，单位为毫瓦，按照一定的步长取值。不同型号的设备支持的步长和取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置PoE接口的最大功率为12000毫瓦。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 poe max-power 12000

\# 通过PoE profile配置PoE接口的最大供电功率为12000毫瓦。

\<Sysname\> system-view

Sysname poe-profile abc

Sysname-poe-profile-abc-1 poe max-power 12000

【相关命令】

·**poe max-power(System view)**

·**poe power max-value**

**PoE \-- PoE配置命令 \-- poe max-power (System view)**

------------------------------------------------------------------------

**[poe max-power**]命令用来配置PSE的最大供电功率。

**[undo poe max-power**]命令用来恢复缺省情况。

【命令】

单PSE设备：

**[poe max-power ***max-power*]

**[undo** **poe max-power**]

多PSE设备：

**[poe pse ***pse-id*** max-power ***max-power*]

**[undo poe pse ***pse-id*** max-power**]

【缺省情况】

不同型号的设备支持的缺省值不同，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-power*]：PSE的最大功率，单位为瓦，按照一定的步长取值。不同型号的设备支持的步长和取值范围不同，请以设备的实际情况为准。

**[pse*** pse-id*]：PSE编号。

【使用指导】

·为保证对优先级为Critical的PoE接口的供电，PSE最大功率必须大于或等于该PSE所有Critical的PoE接口的最大功率之和。当PSE上所有PD消耗的功率大于PSE最大功率时，将会有PD断电。

·各PSE的最大供电功率之和不能超过PoE电源的最大供电功率。

【举例】

\# 配置PSE的最大供电功率为150瓦。（单PSE设备）

\<Sysname\> system-view

Sysname poe max-power 150

\# 配置PSE 7的最大供电功率为150瓦。（多PSE设备）

\<Sysname\> system-view

Sysname poe pse 7 max-power 150

【相关命令】

·**poe priority pse**

**PoE \-- PoE配置命令 \-- poe mode**

------------------------------------------------------------------------

**[poe mode**]命令用来配置PoE接口远程供电模式。

**[undo poe mode**]命令用来恢复缺省情况。

【命令】

**[poe mode**[ { **signal** \| **spare** }]]

**[undo poe mode**]

【缺省情况】

PoE接口远程供电模式为采用信号线供电。

【视图】

PoE接口视图/PoE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[signal**]：PoE接口远程供电方式为采用信号线供电，即使用3/5类双绞线中传输数据所用的线对（1、2、3、6）同时传输直流电。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[spare**]：PoE接口远程供电方式为采用空闲线供电，即使用3/5类双绞线中没有被使用的线对（4、5、7、8）来传输直流电。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置PoE接口远程供电的方式为采用信号线供电。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 poe mode signal

\# 通过PoE配置文件配置PoE接口远程供电的方式为采用信号线供电。

\<Sysname\> system-view

Sysname poe-profile abc

Sysname-poe-profile-abc-1 poe mode signal

【相关命令】

·**poe-profile**

**PoE \-- PoE配置命令 \-- poe pd-description**

------------------------------------------------------------------------

**[poe pd-description**]命令用来配置PoE接口连接PD的描述信息。

**[undo poe pd-description**]命令用来恢复缺省情况。

【命令】

**[poe pd-description** *text*]

**[undo poe pd-description**]

【缺省情况】

PoE接口连接PD的描述信息为空，即没有描述信息。

【视图】

PoE接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：PoE接口连接PD的描述信息，为1～80个字符的字符串，区分大小写。

【举例】

\# 配置PoE接口连接PD的描述信息为连接101室的IP电话。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 poe pd-description IP Phone For Room 101

**PoE \-- PoE配置命令 \-- poe pd-policy priority**

------------------------------------------------------------------------

**[poe pd-policy priority**]命令用来配置PoE接口功率管理策略为优先级策略。

**[undo poe pd-policy priority**]命令用来恢复缺省情况。

【命令】

**[poe pd-policy priority**]

**[undo poe pd-policy priority**]

【缺省情况】

没有配置PoE接口功率管理策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在没有开启PoE接口功率管理的情况下，如果PSE功率过载，则不对新接入的PD供电。

·在开启PoE接口功率管理优先级策略的情况下，如果PSE功率过载，接入新的PD，将对优先级低的PD断电，保证优先级高的PD供电。

【举例】

\# 配置PD功率管理策略为优先级策略。

\<Sysname\> system-view

Sysname poe pd-policy priority

【相关命令】

·**poe priority**

**PoE \-- PoE配置命令 \-- poe power max-value**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[poe power max-value**]命令用来配置PoE电源的最大供电功率。

**[undo poe power max-value**]命令用来恢复缺省情况。

【命令】

集中式设备/分布式设备－独立运行模式：

**[poe power max-value ***max-power*]

**[undo poe power max-value**]

分布式设备－IRF模式：

**[poe power chassis*** chassis-number ***max-value ***max-power*]

**[undo poe power chassis*** chassis-number*** max-value**]

集中式设备－IRF模式：

**[poe** **power** **slot** *slot-number* **max-value** *max-power*]

**[undo** **poe** **power** **slot** *slot-number* **max-value**]

【缺省情况】

不同型号的设备支持的缺省值不同，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-power*]：PoE电源的最大供电功率，即PoE电源能提供给各PSE的最大功率，单位为瓦，以一定的步长取值。不同型号的设备支持的步长和取值范围不同，请以设备的实际情况为准。考虑到瞬时峰值功率的影响，实际可用的最大功率比配置的要多5%左右的额度。

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。（集中式设备－IRF模式）

【使用指导】

需要注意的是，配置的PoE电源最大供电功率不可大于PoE电源的额定功率。

【举例】

\# 配置设备的PoE最大功率为2000瓦。

\<Sysname\> system-view

Sysname poe power max-value 2000

【相关命令】

·**poe max-power**

·**poe max-power(System view)**

**PoE \-- PoE配置命令 \-- poe priority**

------------------------------------------------------------------------

**[poe priority**]命令用来配置PoE接口供电优先级。

**[undo** **poe priority**]命令用来恢复缺省情况。

【命令】

**[poe priority**[ { **critical** \| **high** \| **low** }]]

**[undo poe priority**]

【缺省情况】

PoE接口供电优先级为**low**。

【视图】

PoE接口视图/PoE profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[critical**]：配置PoE接口供电优先级为最高，即将该PoE接口置为供电保证模式，插入该接口的PD可以以最高优先级得到供电。

**[high**]：配置PoE接口供电优先级为高。

**[low**]**：**配置PoE接口供电优先级为低。

【使用指导】

·当PSE功率过载的情况下，优先对供电优先级高的PoE接口进行供电。

·在PoE配置文件视图下配置时，如果该PoE配置文件已经应用到PoE接口，需先取消该PoE配置文件在PoE接口的应用。

·在PoE接口视图下配置时，若已用PoE配置文件对该PoE接口进行过配置，应先取消PoE配置文件在该PoE接口的应用。

·如果配置了相同的优先级，接口编号小的PoE接口的优先级高，支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置PoE接口供电优先级为Critical。

\<Sysname\> system-view

Sysname interface gigabitEthernet 1/0/1

Sysname-GigabitEthernet1/0/1 poe priority critical

\# 通过PoE profile配置PoE接口供电优先级为Critical。

\<Sysname\> system-view

Sysname poe-profile abc

Sysname-poe-profile-abc-1 poe priority critical

Sysname-poe-profile-abc-1 quit

Sysname interface gigabitEthernet 1/0/1

Sysname-GigabitEthernet1/0/1 apply poe-profile name abc

【相关命令】

·**poe pd-policy priority**

**PoE \-- PoE配置命令 \-- poe priority (system view)**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[poe priority**]命令用来配置PSE供电优先级。

**[undo poe priority**]命令用来恢复缺省情况。

【命令】

**[poe priority **[{ **critical** \| **high** \| **low** } **pse** *pse-id*]]

**[undo** **poe priority pse** *pse-id*]

【缺省情况】

PSE供电优先级为**low**。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[critical**]：配置PSE供电优先级为最高，即将该PSE置为供电保证模式，可以以最高优先级得到供电。

**[high**]：配置PSE供电优先级为高。

**[low**]**：**配置PSE供电优先级为低。

**[pse*** pse-id*]：PSE编号。

【使用指导】

当PoE功率过载时，

·如果配置了PSE功率管理优先级策略，将优先对供电优先级高的PSE进行供电（如果优先级相同，PSE ID小的优先供电）。比如有新的PSE开启PoE功能，该PSE优先级配置高，系统将对供电优先级低的PSE断电，以保证对优先级高的PSE的供电；如果PSE优先级配置低，该PSE将不能获得供电。

·如果没有配置PSE功率管理优先级策略，如果有新的PSE开启PoE功能，该PSE将不能获得供电。

【举例】

\# 配置PSE 7的供电优先级为critical。

\<Sysname\> system-view

Sysname poe priority critical pse 7

【相关命令】

·**poe pse-policy priority**

**PoE \-- PoE配置命令 \-- poe pse-policy priority**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[poe pse-policy priority**]命令用来配置PSE功率管理策略为优先级策略。

**[undo poe pse-policy priority**]命令用来恢复缺省情况。

【命令】

**[poe pse-policy priority**]

**[undo poe pse-policy priority**]

【缺省情况】

没有配置PSE功率管理策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在没有开启PSE功率管理的情况下，如果PoE功率过载，则不对新接入的PSE供电。

·在开启PSE功率管理优先级策略的情况下，如果PoE功率过载，分为两种情况：如果新接入的PSE优先级是最低的（为Low），则不对新接入的PSE供电；如果接入新的PSE优先级高（为High或者Critical），将对优先级低的PSE断电，保证给优先级高的PSE供电。

【举例】

\# 配置PSE功率管理策略为优先级策略。

\<Sysname\> system-view

Sysname poe pse-policy priority

【相关命令】

·**poe priority(System view)**

**PoE \-- PoE配置命令 \-- poe temperature-protection**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[poe temperature-protection enable**]命令用来开启设备PoE过温保护功能。

**[undo poe temperature-protection enable**]命令用来关闭设备PoE过温保护功能。

【命令】

**[poe temperature-protection enable**]

**[undo poe temperature-protection enable**]

【缺省情况】

设备的PoE过温保护功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

设备开启PoE过温保护功能后，系统会实时监控设备内部温度：

·当设备内部温度超过上限阈值时，设备进行自我保护，自动关闭所有端口的PoE供电功能；

·当设备内部温度低于下限阈值时，设备自动恢复所有端口的PoE供电功能。

【举例】

\# 关闭设备PoE过温保护功能。

\<Sysname\> system-view

Sysname undo poe temperature-protection enable

**PoE \-- PoE配置命令 \-- poe update**

------------------------------------------------------------------------

![说明](PoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[poe update**]命令用来在线升级PSE固件。

【命令】

单PSE设备：

**[poe update **[{ **full** \| **refresh** } *filename*]]

多PSE设备：

**[poe update **[{ **full** \| **refresh** } *filename* [ **pse** *pse-id* ]]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[full**]：用full模式升级PSE固件，一般用于PSE固件不可用时。

**[refresh**]：用refresh模式升级PSE固件。

*[filename*]：升级文件的名称，取值范围为1～64个字符。该文件必须在设备文件系统的根目录下。升级文件的扩展名与设备的型号有关，请以设备的实际情况为准。

**[pse*** pse-id*]：PSE编号，不指定该参数，表示升级所有PSE的固件。

【使用指导】

·full模式的升级方式是在用refresh模式升级出现异常的情况下使用的，其它情况下，请勿用full模式进行升级。

·PSE固件固件损坏的情况下（表现为所有的PoE命令执行不成功）可以用full模式进行升级，使固件恢复。

【举例】

\# 在线升级PSE固件。（单PSE设备）

\<Sysname\> system-view

Sysname poe update refresh 0400_001.S19

\# 在线升级PSE 7固件。（多PSE设备）

\<Sysname\> system-view

Sysname poe update refresh 0400_001.S19 pse 7

**PoE \-- PoE配置命令 \-- poe-profile**

------------------------------------------------------------------------

**[poe-profile**]命令用来创建PoE profile，并进入PoE profile视图。

**[undo poe-profile**]命令用来删除指定的PoE profile 。

【命令】

**[poe-profile** *profile-name* [ *index* ]]

**[undo poe-profile **[{ **index** *index* \| **name** *profile-name* }]]

【缺省情况】

没有创建PoE profile。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：PoE profile 的名称，为1～15个字符的字符串，区分大小写。以英文字母a-z,A-Z开始，并且不能为保留关键字**undo**、**all**、**name**、**interface**、**user**、**poe**、**disable**、**max-power**、**mode**、**priority**和**enable**等。

*[index*]：PoE profile 的索引，取值范围为1～100。

【使用指导】

批量配置PoE接口时，一般采用PoE Profile配置。如果不指定索引值，系统会为此PoE profile 自动分配索引，从1开始。

如果PoE profile已经应用，不允许删除该PoE profile。必须先执行**undo apply poe-profile**，取消PoE profile 在指定PoE接口的应用后，才能删除该PoE profile 。

【举例】

\# 创建名称为abc的PoE profile，指定索引为3。

\<Sysname\> system-view

Sysname poe-profile abc 3

Sysname-poe-profile-abc-3

\#创建名称为def的PoE profile，不指定索引。

\<Sysname\> system-view

Sysname poe-profile def

Sysname-poe-profile-def-1

【相关命令】

·**apply poe-profile**

·**poe enable**

·**poe priority**

·**poe max-power**

·**poe mode**

**PoE \-- PoE配置命令 \-- poe utilization-threshold**

------------------------------------------------------------------------

**[poe utilization-threshold**]命令用来配置PSE的功率告警阈值。

**[undo poe utilization-threshold**]命令用来恢复缺省情况。

【命令】

单PSE设备：

**[poe utilization-threshold ***value*]

**[undo poe utilization-threshold**]

多PSE设备：

**[poe utilization-threshold ***value* **pse** *pse-id*]

**[undo poe utilization-threshold** **pse** *pse-id*]

【缺省情况】

PSE的功率告警阈值为80%。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：功率告警阈值,取值范围为1～99，单位为百分比。

**[pse**]* pse-id*：PSE编号。

【使用指导】

当PSE的功率使用百分比首次超过或者低于设置的告警阈值时，系统将生成告警信息，发送给设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 配置PSE的功率告警阈值为90%。（单PSE设备）

\<Sysname\> system-view

Sysname poe utilization-threshold 90

\# 配置PSE 7的功率告警阈值为90%。（多PSE设备）

\<Sysname\> system-view

Sysname poe utilization-threshold 90 pse 7
