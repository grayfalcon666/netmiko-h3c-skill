
**时钟监控 \-- 时钟监控配置命令 \-- display network-clock self-test-result**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display network-clock self-test-result**]命令用来查看时钟监控的自检结果。

【命令】

分布式设备－独立运行模式：

**[display network-clock self-test-result**]

分布式设备－IRF模式：

**[display network-clock self-test-result** [ **chassis** *chassis-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。如果不指定该参数，将显示所有成员设备的时钟监控自检结果。（分布式设备－IRF模式）

【举例】

\# 查看时钟监控的自检结果。（分布式设备－独立运行模式）

\<Sysname\> display network-clock self-test-result

Clock module work mode: Normal

  SRAM                : Normal

  CPLD                : Normal

  E1A                 : Normal

  E1B                 : Normal

\# 查看所有成员设备的时钟监控自检结果。（分布式设备－IRF模式）

\<Sysname\> display network-clock self-test-result

Chassis 0：

Clock module state: Normal

  SRAM                : Normal

  CPLD                : Normal

  E1A                 : Normal

  E1B                 : Normal

Chassis 1：

Clock module state: Normal

  SRAM                : Normal

  CPLD                : Normal

  E1A                 : Normal

  E1B                 : Normal

表1-1 display network-clock self-test-result命令显示信息描述表

字段

描述

Clock module work mode

时钟芯片状态，包括：

·Normal：工作正常

·Fault：工作故障（如果以下任意一项故障，则显示工作故障）

SRAM

SRAM（Static Random Access Memory，静态随机存储器）状态，包括：

·Normal：工作正常

·Fault：工作故障

CPLD

CPLD（Complex Programmable Logical Device，复杂可编程逻辑器件）状态，包括：

·Normal：工作正常

·Fault：工作故障

E1A

芯片E1A状态，包括：

·Normal：工作正常

·Fault：工作故障

E1B

芯片E1B状态，包括：

·Normal：工作正常

·Fault：工作故障

**时钟监控 \-- 时钟监控配置命令 \-- display network-clock source**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display network-clock source**]命令用来查看所有参考源的状态。

【命令】

分布式设备－独立运行模式：

**[display network-clock source**]

分布式设备－IRF模式：

**[display network-clock source** [ **chassis** *chassis-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。如果不指定该参数，将显示所有成员设备的时钟监控参考源的状态。（分布式设备－IRF模式）

【使用指导】

本命令用来查看当前MDC的所有参考源的状态。

在任何MDC上都能执行本命令查看到BITS时钟源。线路时钟源只能在它对应的接口所在的MDC中查看，当线路时钟源的所有参数均为默认值时该时钟源不显示。

【举例】

\# 查看所有时钟监控参考源的状态。（分布式设备－独立运行模式）

\<Sysname\> display network-clock source

Traced reference: Pos3/1/1

BITS   State  Priority  SSM level  Force SSM  Sa bit  Direction  Frequency

BITS0  Lost   255       Unknown    ON         4       In         2 Mbps

BITS1  Lost   255       Unknown    ON         4       Out        2 MHz

Port       State  Priority  SSM level  Force SSM  LPU port

Pos3/1/1   Normal 10        Unknown    OFF        Yes

Cpos4/1/9  Normal 15        Unknown    ON         No

\# 查看所有成员设备的时钟监控参考源的状态。（分布式设备－IRF模式）

\<Sysname\> display network-clock source

Chassis 1:

Traced reference: Pos1/3/1/1

BITS   State  Priority  SSM level  Force SSM  Sa bit  Direction  Frequency

BITS0  Lost   255       Unknown    ON         4       In         2 Mbps

BITS1  Lost   255       Unknown    ON         4       Out        2 MHz

Port        State  Priority  SSM level  Force SSM  LPU port

Pos1/3/1/1  Normal 1         PRC        OFF        Yes

Chassis 2:

Traced reference: Pos2/2/1/8

BITS   State  Priority  SSM level  Force SSM  Sa bit  Direction  Frequency

BITS0  Lost   10        Unknown    ON         4       In         2 Mbps

BITS1  Lost   255       Unknown    ON         4       Out        2 MHz

Port        State  Priority  SSM level  Force SSM  LPU port

Pos2/2/1/8  Normal 1         PRC        OFF        Yes

Cpos2/4/2/2 Normal 15        Unknown    ON         No

表1-2 display network-clock source命令显示信息描述表

字段

描述

Traced reference

已选中的参考源，没有跟踪时显示N/A

当参考源被选中时，系统将同步时钟信号到所有接口板

Reference

参考源

State

参考源的状态：

·Normal：正常工作的时钟源

·Lost：未工作或异常的时钟源

Priority

参考源的优先级

SSM level

SSM级别，按照其同步质量由高到低依次为：

·PRC：G.811时钟信号

·SSU-A：G.812转接节点时钟信号

·SSU-B：G.812本地节点时钟信号

·SEC：SDH设备时钟源信号

·DNU：不应用作同步

·Unknown：时钟源的同步质量未知

Force SSM

是否从时钟源提取SSM级别：

·ON：不从时钟源提取SSM级别

·OFF：从时钟源提取SSM级别

Sa bit

传输BITS时钟源承载SSM的时隙比特位：

·sa4：承载SSM的sa时隙为sa4比特

·sa5：承载SSM的sa时隙为sa5比特

·sa6：承载SSM的sa时隙为sa6比特

·sa7：承载SSM的sa时隙为sa7比特

·sa8：承载SSM的sa时隙为sa8比特

·N/A：线路时钟源不支持配置Sa-bit

Direction

BITS时钟源方向：

·In：接收外部时钟信息号

·Out：向外提供时钟信号

Frequency

BITS时钟源频率：

·2 Mbps：频率为2 Mbps

·2 MHz：频率为2 MHz

LPU port

端口是否使能LPU port：

·Yes：使能LPU port

·No：未使能LPU port

·N/A：BITS0、BITS1、PTP等显示为N/A

\

**时钟监控 \-- 时钟监控配置命令 \-- display network-clock status**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display network-clock status**]命令用来查看时钟监控的工作状态。

【命令】

分布式设备－独立运行模式：

**[display network-clock status**]

分布式设备－IRF模式：

**[display network-clock status** [ **chassis** *chassis-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。如果不指定该参数，将显示所有成员设备的时钟监控工作状态。（分布式设备－IRF模式）

【举例】

\# 查看时钟监控的工作状态。（分布式设备－独立运行模式）

\<Sysname\> display network-clock status

Mode              : Auto

Traced reference  : N/A

Lock mode         : Unknown

SSM output level  : SSUB

SSM control enable: On

\# 查看所有成员设备的时钟监控工作状态。（分布式设备－IRF模式）

\<Sysname\> display network-clock status

Chassis 0:

Mode              : Auto

Reference         : N/A

Traced reference  : N/A

Lock mode         : Unknown

SSM output level  : SSUB

SSM control enable: On

Chassis 1:

Mode              : Auto

Reference         : N/A

Traced reference  : N/A

Lock mode         : Unknown

SSM output level  : SSUB

SSM control enable: On

表1-3 display network-clock status命令显示信息描述表

字段

描述

Mode

工作模式，包括：

·Auto：自动模式

·Manual：手动模式

Traced reference

已选中的参考源，没有时钟源选中时显示为N/A

Lock mode

时钟监控的锁相状态，包括：

·Freerun：自由振荡状态

·Locked：锁定（跟踪）状态

·Holdover：保持状态

·Pre-locked：预锁状态

·Lost：信号丢失状态

·Unknown：信号未知

SSM output level

SSM级别，由高到低依次为：

·PRC：G.811时钟信号

·SSU-A：G.812转接节点时钟信号

·SSU-B：G.812本地节点时钟信号

·SEC：SDH设备时钟源信号

·DNU：不应用作同步

·Unknown：时钟源的同步质量未知

SSM control enable

SSM级别是否参与控制时钟源的选举：

·On：SSM级别参与控制

·Off：SSM级别不参与控制

**时钟监控 \-- 时钟监控配置命令 \-- display network-clock version**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display network-clock** **version**]令用来查看时钟监控的版本信息。

【命令】

分布式设备－独立运行模式：

**[display network-clock** **version**]

分布式设备－IRF模式：

**[display network-clock** **version** [ **chassis** *chassis-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。如果不指定该参数，将显示所有成员设备的时钟监控版本信息。（分布式设备－IRF模式）

【举例】

\# 查看时钟监控的版本信息。（分布式设备－独立运行模式）

\<Sysname\> display network-clock version

Clock card

  Type      : SR01CK3A

  Software  : 106

  PCB       : A

  Number of Cpld: 1

  Cpld 0:

    Software  : 001

\# 查看成员设备0的时钟监控版本信息。（分布式设备－IRF模式）

\<Sysname\> display network-clock version chassis 0:

Clock card

  Type      : SR01CK3A

  Software  : 106

  PCB       : A

  Number of Cpld: 1

  Cpld 0:

    Software  : 001

![说明](时钟同步命令.files/image001.png)

本命令的具体显示信息与设备的型号有关，请以设备的实际情况为准。

表1-4 display network-clock version命令显示信息描述表

字段

描述

Type

时钟扣板类型，当前有SR01CK3A和SR07CK3C两种类型

Software

时钟扣板软件版本

PCB

时钟扣板PCB（Printed Circuit Board，印制电路板）版本

Number of Cpld

时钟扣板CPLD个数

Cpld 0

时钟扣板的0号CPLD，即第一个CPLD

Software

时钟扣板0号CPLD的软件版本

**时钟监控 \-- 时钟监控配置命令 \-- network-clock lpuport**

------------------------------------------------------------------------

**[network-clock lpuport**]命令用来配置线路时钟源的输入端口。

**[undo network-clock lpuport**]命令用来恢复缺省情况。

【命令】

**[network-clock lpuport** *port-type port-number*]

**[undo network-clock lpuport** *port-type port-number*]

【缺省情况】

未配置线路时钟源的输入端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-type port-number*]：端口类型及端口编号。

【使用指导】

·只允许将主接口指定为线路时钟源的输入端口。

·设备允许配置多个线路时钟源的输入端口。在自动模式下，设备上最终生效的线路时钟源输入端口为配置的所有输入端口中的最优端口；在手动模式下，设备上最终生效的线路时钟源输入端口为该模式下通过**network-clock work-mode manual mdc**命令指定的MDC的时钟源。

·不建议将主时钟模式的端口配置为线路时钟源的输入端口。

【举例】

\# 配置线路时钟源的输入端口为POS2/2/0接口。

\<Sysname\> system-view

Sysname network-clock lpuport pos 2/2/0

【相关命令】

·**display network-clock source**

·**network-clock work-mode manual mdc**

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source direction**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[network-clock source direction**]命令用来配置传输BITS时钟源方向。

**[undo network-clock source direction**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock source ** { **bits0** \| **bits1** } **direction** { **in** \| **out** }]

**[undo network-clock source ** { **bits0** \| **bits1** } **direction**]

分布式设备－IRF模式：

**[network-clock**]**chassis** *chassis-number***source **[{ **bits0** \| **bits1** } ]**[in**[ \| ]**out** }

**[undo network-clock**]**chassis** *chassis-number* **source **[{ **bits0** \| **bits1** } ]**direction**

【缺省情况】]

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

**[bits0**]：BITS0时钟源。

**[bits1**]：BITS1时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[in**]：时钟源方向为入方向，即此时时钟源接收外部时钟信号。

**[out**]：时钟源方向为出方向，即此时时钟源向外提供时钟信号。

【使用指导】

该命令只支持在管理MDC中配置，但配置对所有MDC生效。

【举例】

\# 配置BITS0时钟源方向为出方向。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname network-clock source bits0 direction out

\# 配置成员设备1上BITS0时钟源的方向为出方向。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname network-clock chassis 1 source bits0 direction out

【相关命令】

·**display network-clock source**

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source forcessm**

------------------------------------------------------------------------

**[network-clock source forcessm**]命令用来配置SSM级别的提取方式。

**[undo network-clock source forcessm**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock source**[ { **bits0** \| **bits1** \| **lpuport** *port-type port-number* \| **ptp** } **forcessm** { **on** \| **off** }]]

**[undo network-clock source**[ { **bits0** \| **bits1** \| **lpuport** *port-type port-number* \| **ptp** } **forcessm**]]

分布式设备－IRF模式：

**[network-clock chassis**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **forcessm** { **on** \| **off** }]]

**[network-clock source lpuport**[ *port-type port-number* **forcessm** { **on** \| **off** }]]

**[undo network-clock chassis**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **forcessm**]]

**[undo network-clock source lpuport** *port-type port-number* **forcessm**]

【缺省情况】

不从时钟源中提取SSM级别，使用用户自行配置的SSM级别。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[on**]：不从时钟源中提取SSM级别，使用用户自行配置的SSM级别。

**[off**]：从时钟源中提取SSM级别，用户配置的SSM级别无效。

**[bits0**]：BITS0时钟源。

**[bits1**]：BITS1时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[lpuport** *port-type port-number*]：指定的线路时钟源，*port-type port-number*表示端口类型及端口编号。

**[ptp**]：PTP协议时钟源。

**[chassis***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

【使用指导】

·BITS时钟源和PTP协议时钟源只支持在缺省MDC中配置，线路时钟源只能在接口对应的MDC中配置。

·时钟源配置为从时钟源中提取SSM级别时，用户自行配置的SSM级别将失效。

【举例】

\# 配置BITS0时钟源从该时钟源接收的信号中提取SSM级别。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname network-clock source bits0 forcessm off

\# 配置成员设备1的BITS0时钟源从该时钟源接收的信号中提取SSM级别。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname network-clock chassis 1 source bits0 forcessm off

【相关命令】

·**display network-clock source**

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source frequency**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[network-clock source frequency**]命令用来配置传输BITS时钟频率。

**[undo network-clock source frequency**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock source ** { **bits0** \| **bits1** } **frequency** { **bps-2m** \| **hz-2m** }]

**[undo network-clock source ** { **bits0** \| **bits1** } **frequency**]

分布式设备－IRF模式：

**[network-clock**]**chassis** *chassis-number*** source **[{ **bits0** \| **bits1** } **frequency** ]**[bps-2m**[ \| ]**hz-2m**}

**[undo network-clock**]**chassis ***chassis-number ***source **[{ **bits0** \| **bits1** } **frequency**]

【缺省情况】]

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chassis **]*chassis-number*：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

**[bits0**]：BITS0时钟源。

**[bits1**]：BITS1时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bps-2m**]：BITS时钟源的频率为2 Mbps。

**[h**]**z-2m**：BITS时钟源的频率为2 MHz。

【使用指导】

该命令只支持在管理MDC中配置，但配置对所有MDC生效。

【举例】

\# 配置BITS0时钟源频率为2 MHz。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname network-clock source bits0 frequency hz-2m

\# 配置成员设备1上BITS0时钟源频率为2 MHz。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname network-clock chassis 1 source bits0 frequency hz-2m

【相关命令】

·**display network-clock source**

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source priority**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[network-clock source priority**]命令用来配置参考源的优先级。

**[undo network-clock source priority**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock**[ **source** { **bits0** \| **bits1** \| **ptp** \| **lpuport** *port-type port-number* } **priority** *value*]]

**[undo**[ **network-clock** **source** { **bits0** \| **bits1** \| **ptp** \| **lpuport** *port-type port-number* } **priority**]]

分布式设备－IRF模式：

**[network-clock chassis**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **priority** *value*]]

**[network-clock source lpuport** *port-type port-number* **priority** *value*]

**[undo network-clock chassis**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **priority**]]

**[undo network-clock source lpuport ***port-type port-number*** priority**]

【缺省情况】

所有参考源的优先级为255。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[priority** *value*]：参考源的优先级，数值越小优先级越高。

**[bits0**]：BITS0时钟源。

**[bits1**]：BITS1时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ptp**]：PTP协议时钟源。

**[lpuport ***port-type port-number*]：指定的线路时钟源，*port-type port-number*表示端口类型及端口编号。

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

【使用指导】

BITS时钟源和PTP协议时钟源只能在缺省MDC中配置，线路时钟源只能在接口对应的MDC中配置。

【举例】

\# 配置BITS0时钟源的优先级为3。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname network-clock source bits0 priority 3

\# 配置成员设备1的BITS0时钟源的优先级为3。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname network-clock chassis 1 source bits0 priority 3

【相关命令】

·**display network-clock source**

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source sa-bit**

------------------------------------------------------------------------

**[network-clock source sa-bit**]命令用来配置传输BITS时钟源承载SSM的时隙比特位。

**[undo network-clock source sa-bit**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock source **[{ **bits0** \| **bits1** } **sa-bit** { **sa4** \| **sa5** \| **sa6** \| **sa7** \| **sa8** }]]

**[undo network-clock source **[{ **bits0** \| **bits1** } **sa-bit**]]

分布式设备－IRF模式：

**[network-clock chassis**[ *chassis-number* **source** { **bits0** \| **bits1** } **sa-bit** { **sa4** \| **sa5** \| **sa6** \| **sa7** \| **sa8** }]]

**[undo network-clock chassis ***chassis-number ***source **[{ **bits0** \| **bits1** } **sa-bit**]]

【缺省情况】

传输BITS时钟源承载SSM的时隙比特位为sa4。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

**[sa4**]：承载SSM的时隙比特位为sa4比特。

**[sa5**]：承载SSM的时隙比特位为sa5比特。

**[sa6**]：承载SSM的时隙比特位为sa6比特。

**[sa7**]：承载SSM的时隙比特位为sa7比特。

**[sa8**]：承载SSM的s时隙比特位为sa8比特。

**[bits0**]：BITS0时钟源。

**[bits1**]：BITS1时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·该命令只支持在缺省MDC中配置，但配置对所有MDC生效。

·建议本配置在网络中各设备上保持一致。

【举例】

\# 配置传输BITS0时钟源承载SSM的时隙比特位为sa5。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname network-clock source bits0 sa-bit sa5

\# 配置成员设备1上传输BITS0承载SSM的时隙比特位为sa5。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname network-clock chassis 1 source bits0 sa-bit sa5

**时钟监控 \-- 时钟监控配置命令 \-- network-clock source ssm**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[network-clock source ssm**]命令用来配置各参考源的SSM级别。

**[undo network-clock source ssm**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock source **[{ **bits0** \| **bits1** \| **ptp** \| **lpuport** *port-type port-number* } **ssm** { **dnu** \| **prc** \| **sec** \| **ssua** \| **ssub** \| **unknown** }]]

**[undo**[ **network-clock source** { **bits0** \| **bits1** \| **ptp** \| **lpuport** *port-type port-number* } **ssm**]]

分布式设备－IRF模式：

**[network-clock chassis**[ *chassis-number* **source** { **bits0** \| **bits1** \| **ptp** } **ssm** { **dnu** \| **prc** \| **sec** \| **ssua** \| **ssub** \| **unknown** }]]

**[network-clock source lpuport*** port-type port-number*** ssm**[ { **dnu** \| **prc** \| **sec** \| **ssua** \| **ssub** \| **unknown** }]]

**[undo network-clock chassis**[ *chassis-numb*er **source** { **bits0** \| **bits1** \| **ptp** } **ssm**]]

**[undo network-clock source lpuport** *port-type port-number* **ssm**]

【缺省情况】

所有参考源的SSM级别为**unknown**。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dnu**]：SSM级别为DNU（不应用作同步）。

**[ssub**]：SSM级别为SSU-B（G.812本地节点时钟信号）。

**[prc**]：SSM级别为PRC（G.811时钟信号）。

**[sec**]：SSM级别为SEC（SDH设备时钟源信号）。

**[ssua**]：SSM级别为SSU-A（G.812转接节点时钟信号）。

**[unknown**]：SSM级别为Unknown（时钟源的同步质量未知）。

**[bits0**]：BITS0时钟源。

**[bits1**]：BITS1时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ptp**]：PTP协议时钟源。

**[lpuport ***port-type port-number*]：指定的线路时钟源，*port-type port-number*表示端口类型及端口编号。

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

【使用指导】

·对于线路时钟源，配置的SSM级别为该时钟源的SSM级别。

·BITS时钟源和PTP协议时钟源只能在缺省MDC中配置，线路时钟源只能在接口对应的MDC中配置。

·时钟源已配置从时钟源中提取SSM级别时，用户自行配置的SSM级别不生效。

·配置参考源的SSM级别后设备响应需要一定时间，可通过**display network-clock source**命令和日志信息查看配置是否生效。

【举例】

\# 配置BITS0时钟源的SSM级别为DNU。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname network-clock source bits0 ssm dnu

\# 配置成员设备1的BITS0时钟源的SSM级别为DNU。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname network-clock chassis 1 source bits0 ssm dnu

**时钟监控 \-- 时钟监控配置命令 \-- network-clock ssmcontrol**

------------------------------------------------------------------------

**[network-clock ssmcontrol**]命令用来配置SSM级别是否参与控制。

**[undo network-clock ssmcontrol**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock ssmcontrol**[ { **on** \| **off** }]]

**[undo network-clock ssmcontrol**]

分布式设备－IRF模式：

**[network-clock chassis**[ *chassis-number* **ssmcontrol** { **on** \| **off** }]]

**[undo network-clock chassis** *chassis-number* **ssmcontrol**]

【缺省情况】

SSM级别不参与控制。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

**[on**]：配置SSM级别参与控制。

**[off**]：配置SSM级别不参与控制。

【使用指导】

·SSM级别参与控制：时钟源在自动工作模式时，将首先按照参考源的SSM级别确定。

·SSM级别不参与控制：用户可以配置和查看SSM级别，但是在自动切换时钟源时，参考源的SSM级别被忽略，直接按照参考源的优先级来确定。

·该命令只支持在缺省MDC中配置，但配置对所有MDC生效。

【举例】

\# 配置时钟监控SSM级别参与控制。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname network-clock ssmcontrol on

\# 配置成员设备1的时钟监控SSM级别参与控制。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname network-clock chassis 1 ssmcontrol on

【相关命令】

·**display network-clock source**

·**network-clock ssm**

**时钟监控 \-- 时钟监控配置命令 \-- network-clock work-mode**

------------------------------------------------------------------------

**[network-clock work-mode**]命令用来配置时钟监控的工作模式，即时钟源的选择模式。

**[undo network-clock work-mode**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock work-mode **[{ **auto** \| **manual source** { **bits0** \| **bits1** \| **lpuport** *port-type port-number* } }]]

**[undo network-clock work-mode**]

分布式设备－IRF模式：

**[network-clock chassis**[ *chassis-number* **work-mode** { **auto** \| **manual source** { **bits0** \| **bits1** } }]]

**[network-clock work-mode manual source lpuport ***port-type port-number*]

**[undo network-clock chassis** *chassis-number* **work-mode**]

【缺省情况】

时钟监控的工作模式为自动模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：配置时钟监控的工作模式为自动模式。

**[manual source**]：配置时钟监控手动模式的时钟源。

**[bits0**]：配置手动模式下参考时钟为BITS0时钟源。

**[bits1**]：配置手动模式下参考时钟为BITS1时钟源。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[lpuport** *port-type port-number*]：配置手动模式下主用时钟源为线路时钟源，*port-type port-number*表示端口类型及端口编号。

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

【使用指导】

·手动模式指定线路时钟源时，只能在接口对应的MDC中配置。

·若配置手动模式下主用时钟源为线路时钟源，该线路时钟源的输入端口必须同时为**network-clock lpuport**命令指定的线路时钟源输入端口，配置才能生效。

·配置时钟监控的工作模式后设备响应需要一定时间，可通过**display network-clock status**命令和日志信息查看配置是否生效。

【举例】

\# 配置时钟监控的工作模式为手动模式，主用时钟源为BITS0时钟源。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname network-clock work-mode manual source bits0

\# 配置成员设备1的时钟监控的工作模式为自动模式。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname network-clock chassis 1 work-mode auto

【相关命令】

·**display network-clock source**

·**display network-clock status**

**时钟监控 \-- 时钟监控配置命令 \-- network-clock work-mode manual mdc**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[network-clock work-mode manual mdc**]命令用来配置手动模式下指定MDC的时钟源有效。

**[undo network-clock work-mode manual mdc**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式：

**[network-clock work-mode manual mdc ***mdc-id*]

**[undo network-clock work-mode manual mdc**]

分布式设备－IRF模式：

**[network-clock chassis ***chassis-number*** work-mode manual mdc ***mdc-id*]

**[undo network-clock chassis ***chassis-number*** work-mode manual mdc**]

【缺省情况】

缺省MDC下配置的手动配置生效。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mdc*** mdc-id*]：表示手动模式下指定的非缺省MDC ID号，取值范围与设备的型号有关，请以设备的实际情况为准。

**[chassis ***chassis-number*]：表示设备在IRF中的成员编号。（分布式设备－IRF模式）

【使用指导】

·该命令只支持在缺省MDC中配置，但配置对所有MDC生效。

·在手工指定非缺省MDC时钟源时，请使用**display network-clock source**命令查看时钟源的状态，只有该MDC内的所有框上有可以正常工作的参考源，该MDC才能配置为主用时钟源。

·配置主控板时钟监控的工作模式后设备响应需要一定时间。

【举例】

\# 配置手动模式下MDC 2的时钟源有效。

\<Sysname\> system-view

Sysname network-clock work-mode manual mdc 2

【相关命令】

·**display network-clock status**

·**network-clock work-mode**

\

**同步以太网 \-- 同步以太网配置命令 \-- display esmc**

------------------------------------------------------------------------

**[display esmc**]命令用来显示接口上的ESMC信息。

【命令】

**[display esmc ** **interface** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type* *interface-number*]：显示指定接口上的ESMC信息，*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，将显示所有接口的ESMC信息。

【使用指导】

如果接口工作在非同步模式，则该接口的ESMC信息显示为空。

【举例】

\# 显示所有接口的ESMC信息。

\<Sysname\> display esmc

Interface   : GigabitEthernet1/0/1

Mode        : Synchronous

ESMC status : Enable

Port status : Up

Duplex mode : Full

QL received : QL-SEC

QL sent     : QL-PRC

ESMC information packets received : 2195

ESMC information packets sent     : 6034

ESMC event packets received       : 1

ESMC event packets sent           : 16

ESMC information rate             : 1 packets/sec

ESMC expiration                   : 5 seconds

表2-1 display esmc命令显示信息描述表

字段

描述

Mode

以太网接口工作模式：

·Synchronous：同步模式

·Non-Synchronous：非同步模式（不显示接口ESMC信息）

ESMC status

ESMC报文收发处理是否使能：

·Enable：表示已使能

·Disable：表示未使能

Port status

接口状态：

·Up：表示接口up

·Down：表示接口down

Duplex mode

以太网接口的双工模式：

·Full：接口处于全双工状态

·Half：接口处于半双工状态

QL received

接收到的QL值：

·PRC：G.811时钟信号

·SSU-A：G.812转接节点时钟信号

·SSU-B：G.812本地节点时钟信号

·SEC：SDH设备时钟源信号

·DNU：不应用作同步

·UNK：同步质量未知

QL sent

发送的QL值：

·PRC：G.811时钟信号

·SSU-A：G.812转接节点时钟信号

·SSU-B：G.812本地节点时钟信号

·SEC：SDH设备时钟源信号

·DNU：不应用作同步

·UNK：同步质量未知

ESMC information packets received

接收的ESMC信息报文数目

ESMC information packets sent

发送的ESMC信息报文数目

ESMC event packets received

接收的ESMC事件报文数目

ESMC event packets sent

发送的ESMC事件报文数目

ESMC information rate

ESMC信息报文发包频率，固定为1 packets/sec

ESMC expiration

接收ESMC报文的超时时间，固定为5秒

【相关命令】

·**esmc enable**

·**synchronous mode**

**同步以太网 \-- 同步以太网配置命令 \-- esmc enable**

------------------------------------------------------------------------

**[esmc enable**]命令用来使能当前接口的ESMC功能。

**[undo esmc enable**]命令用来恢复缺省情况。

【命令】

**[esmc enable**]

**[undo esmc enable**]

【缺省情况】

接口上ESMC功能处于关闭状态。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

必须先配置以太网接口的工作模式为同步模式后，才能使能ESMC功能。

【举例】

\# 使能接口GigabitEthernet1/01的ESMC功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 esmc enable

【相关命令】

·**display esmc**

·**synchronous mode**

**同步以太网 \-- 同步以太网配置命令 \-- synce state**

------------------------------------------------------------------------

![说明](时钟同步命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[synce state**]命令用来配置GE电口的端口模式为Master或者Slave。

**[undo synce state**]命令用来恢复缺省情况。

【命令】

**[synce state **[{ **master** \| **slave** }]]

**[undo synce state**]

【缺省情况】

GE电口将采用自动协商的方式决定其端口模式。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[master**]：GE电口的端口模式为Master。

**[slave**]：GE电口的端口模式为Slave。

【使用指导】

在同步以太网中，GE电口的端口模式与其同步时钟的方向关联。如果GE电口需要向下游同步时钟，则其端口模式需要配置成Master；如果GE电口需要从上游同步时钟，则其端口模式需要配置成Slave。如果未配置端口模式，GE电口将采用自动协商的方式决定其端口模式（Master端口使用本设备的时钟，Slave端口从线路上提取时钟），此时协商出的主从关系和网络管理员规划的主从关系可能会相互冲突，造成设备间时钟同步错误。

【举例】

\# 配置GE电口GigabitEthernet1/0/1的端口模式为Master。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 synce state master

**同步以太网 \-- 同步以太网配置命令 \-- synchronous mode**

------------------------------------------------------------------------

**[synchronous mode**]命令用来配置当前接口的工作模式为同步模式。

**[undo synchronous mode**]命令用来恢复缺省情况。

【命令】

**[synchronous mode**]

**[undo synchronous mode**]

【缺省情况】

接口的工作模式为非同步模式。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有当接口的工作模式为同步模式时，该接口才能有可能作为本设备的线路时钟源参与时钟源选择。

【举例】

\# 配置接口GigabitEthernet1/01的工作模式为同步模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 synchronous mode

【相关命令】

·**display esmc**

·**esmc enable**

