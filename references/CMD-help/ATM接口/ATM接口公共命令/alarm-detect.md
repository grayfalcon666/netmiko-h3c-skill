
**ATM接口 \-- ATM接口公共命令 \-- alarm-detect**

------------------------------------------------------------------------

![说明](ATM接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[alarm-detect**]命令用来设置当前接口的告警联动动作。

**[undo alarm-detect**]命令用来取消告警联动动作。

【命令】

**[alarm-detect**[ { **rdi** \| **sd** \| **sf** } **action link-down**]]

**[undo alarm-detect**[ { **rdi** \| **sd** \| **sf** }]]

【缺省情况】

接口不执行任何告警联动动作。

【视图】

ATM接口视图（包括13种物理类型：E1、T1、E3、T3、OC-3c/STM-1、OC-12c/STM-4、25M、ADSL、ADSL 2+、G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rdi**]：表示RDI（Remote Defect Indication，远端失效指示）告警。

**[sd**]：表示SD（Signal Degrade，信号衰减）告警。

**[sf**]：表示SF（Signal Fail，信号失败）告警。

**[action**]：设置当接口检测到告警时的联动动作。

**[link-down**]：表示自动将接口的物理状态设置为down。

【使用指导】

当设备收到对端发送的MS-RDI信号时，则认为发生了RDI告警。当设备收到的报文的误码率达到或超过设置的门限时，则生成SD告警或SF告警。SD告警和SF告警的门限可通过**threshold**命令设置。

配置本命令后，当设备检测到告警时，会自动将接口的物理状态设置为down。

【举例】

\# 配置当ATM2/4/0接口检测到SD告警时，自动将接口的物理状态设置为down。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 alarm-detect sd action link-down

【相关命令】

·**threshold**

**ATM接口 \-- ATM接口公共命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

ATM接口视图（包括13种物理类型：E1、T1、E3、T3、OC-3c/STM-1、OC-12c/STM-4、25M、ADSL、ADSL 2+、G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

ATM子接口视图

EFM接口视图（包括4种物理类型：G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

EFM子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置ATM接口2/4/0的期望带宽为50kbit/s。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 bandwidth 50

**ATM接口 \-- ATM接口公共命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

ATM接口视图（包括13种物理类型：E1、T1、E3、T3、OC-3c/STM-1、OC-12c/STM-4、25M、ADSL、ADSL 2+、G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

ATM子接口视图

EFM接口视图（包括4种物理类型：G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

EFM子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将ATM接口2/4/0恢复为缺省配置。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 default

**ATM接口 \-- ATM接口公共命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：ATM2/4/0 Interface。

【视图】

ATM接口视图（包括13种物理类型：E1、T1、E3、T3、OC-3c/STM-1、OC-12c/STM-4、25M、ADSL、ADSL 2+、G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

ATM子接口视图

EFM接口视图（包括4种物理类型：G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

EFM子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置ATM接口2/4/0的描述信息为"atmswitch-interface"。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 description atmswitch-interface

**ATM接口 \-- ATM接口公共命令 \-- display counters**

------------------------------------------------------------------------

![说明](ATM接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display counters**]命令用来显示接口的流量统计信息。

【命令】

**[display counters**[ { **inbound** \| **outbound** } **interface** [ **atm** [ *interface-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[inbound**]：显示输入报文的流量统计信息。

**[oubound**]：显示输出报文的流量统计信息。

**[atm**]：显示ATM接口的流量统计信息。

*[interface-number*]：ATM接口的编号。

【使用指导】

·如果不指定**atm**，则显示所有可统计的接口的流量统计信息。

·如果指定**atm**而不指定*interface-number*，则显示所有ATM接口的流量统计信息。

·如果同时指定**atm**和*interface-number*，则显示指定ATM接口的流量统计信息。

【举例】

\# 显示ATM2/4/0接口的输入报文流量统计信息。

\<Sysname\> display counters inbound interface atm 2/4/0

Interface         Total (pkts)   Broadcast (pkts)   Multicast (pkts)  Err (pkts)

ATM2/4/0                   100                  0                100           0

 Overflow: More than 14 digits (7 digits for column \"Err\").

       \--: Not supported.

表1-1 display counters命令显示信息描述表

字段

描述

Interface

接口名称缩写

Total (pkts)

接口接收或发送报文的总数（单位为包）

Broadcast (pkts)

接口接收或发送广播报文的总数（单位为包）

Multicast (pkts)

接口接收或发送组播报文的总数（单位为包）

Err (pkts)

接口接收或发送错误报文的总数（单位为包）

Overflow：More than 14 digits（7 digits for colum "Err"）

当某个统计信息的值为Overflow时，表示该项数据的长度超过了显示范围

·对于Err项，Overflow表示数据的长度超过了7位十进制数

·对于其它项，Overflow表示数据的长度超过了14位十进制数

\--: Not supported.

当某个统计信息的值为"\--"时，表示设备不支持该项数据的统计

【相关命令】

·**reset counters interface**

**ATM接口 \-- ATM接口公共命令 \-- display counters rate**

------------------------------------------------------------------------

**[display counters rate**]命令用来显示最近一个统计周期内处于up状态的接口的报文速率统计信息。

【命令】

**[display counters rate**[ { **inbound** \| **outbound** } **interface** [ **atm** [ *interface-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[inbound**]**：**显示报文接收速率统计信息。

**[outbound**]**：**显示报文发送速率统计信息。

**[atm**]：显示ATM接口的报文速率统计信息。

*[interface-number*]：ATM接口的编号。

【使用指导】

·如果不指定**atm**，则显示所有可统计的接口类型中最近一个统计周期内处于up状态的接口的报文速率统计信息。

·如果指定**atm**而不指定*interface-number*，则显示最近一个统计周期内所有处于up状态的ATM接口的报文速率统计信息。

·如果同时指定**atm**和*interface-number*，则显示指定ATM接口在最近一个统计周期内的报文速率统计信息。

![说明](ATM接口命令.files/image003.png)

统计周期与设备的型号有关，请以设备的实际情况为准：

·不支持**flow-interval**命令的设备，统计周期固定为5分钟。

·支持flow-interval命令的设备，统计周期可以通过flow-interval命令来配置。

【举例】

\# 显示ATM2/4/0接口的报文接收速率统计信息。

\<Sysname\> display counters rate inbound interface atm 2/4/0

Interface               Total (pps)       Broadcast (pps)       Multicast (pps)

ATM2/4/0                        100                     0                   100

 Overflow: More than 14 digits.

       \--: Not supported.

表1-2 display counters rate命令显示信息描述表

字段

描述

Interface

接口名称缩写

Total (pps)

在最近一个统计周期内，接口接收或发送所有类型报文的平均速率（单位为包/秒）

Broadcast (pps)

在最近一个统计周期内，接口接收或发送广播报文的平均速率（单位为包/秒）

Multicast (pps)

在最近一个统计周期内，接口接收或发送组播报文的平均速率（单位为包/秒）

Overflow: More than 14 digits.

当某个统计信息的值为Overflow时，表示该项数据的长度超过了14位十进制数

\--: Not supported.

当某个统计信息的值为"\--"时，则表示设备不支持该项数据的统计

【相关命令】

·**reset counters interface**

**ATM接口 \-- ATM接口公共命令 \-- display interface atm**

------------------------------------------------------------------------

**[display interface atm**]命令用来显示ATM接口的相关信息。

【命令】

**[display interface** [ **atm** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定ATM接口的信息，interface-number表示ATM接口的编号。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**atm**参数，将显示设备支持的所有接口的相关信息。

·如果指定**atm**参数，不指定*interface-number*参数，将显示所有ATM接口的相关信息。

【举例】

\# 显示接口ATM2/4/0的详细信息。

\<Sysname\> display interface atm 2/4/0

ATM2/4/0

Current state: DOWN

Line protocol state: DOWN

Description: ATM2/4/0 Interface

Bandwidth: 20000kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

AAL enabled: AAL5

Current VCs: 0 (0 on main interface)

ATM over E1, Scramble: enabled, Frame-format: crc4-adm

Code: hdb3, Clock: slave, Cable length: long

Loopback: cell

Cable type: 75 ohm non-balanced

Line Alarm: LOS LOF

Line Error: 0 FERR, 0 LCV, 0 CERR, 0 FEBE

Last link flapping: 6 hours 39 minutes 25 seconds

Last clearing of counters: Never

Last 300 seconds input rate: 0.00 bytes/sec, 0.00 packets/sec

Last 300 seconds output rate: 0.00 bytes/sec, 0.00 packets/sec

Input:

  0 packets, 0 bytes, 0 buffers

  0 errors, 0 crcs, 0 lens, 0 giants

  0 pads, 0 aborts, 0 timeouts

  0 overflows, 0 overruns, 0 no buffer

Output:

  0 packets, 0 bytes, 0 buffers

  0 errors, 0 overflows, 0 underruns

\# 显示接口ATM2/4/0的概要信息。

\<Sysname\> display interface atm 2/4/0 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

ATM2/4/0             UP   UP(s)    \--

\# 显示当前物理状态为down的ATM接口的信息以及down的原因。

\<Sysname\> display interface atm brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

ATM2/4/0             DOWN Not connected

表1-3 display interface atm命令显示信息描述表

字段

描述

ATM2/4/0

Current state

接口当前的物理状态和管理状态，可能的取值及含义如下：

·DOWN（Administratively）：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态，可能的状态及含义如下：

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

Description

接口的描述信息

Bandwidth

接口的期望带宽

Maximum Transmit Unit

接口的最大传输单元

Internet protocol processing

对IP报文的处理能力，disabled表示尚未配置IP地址，不能处理IP报文。当接口下配置了IP地址之后，该字段将变为"Internet Address is"

AAL enabled

该ATM接口使能的ATM适配层类型，ATM支持的适配层类型固定为AAL 5（ATM Adaptation Layer 5，ATM适配层5）

Current VCs: 0 (0 on main interface)

该ATM接口下已经配置的虚电路数，括号中的内容表示主接口上已经配置的虚电路数

ATM over E1

该ATM接口的类型

Scramble

该ATM接口下加扰功能的使能情况

Frame-format

该ATM接口的帧格式：

·sdh：帧格式为SDH STM-1

·sonet：帧格式为SONET OC-3

·crc4-adm：帧格式为CRC4 ADM格式

·no-crc4-adm：帧格式为No-CRC4 ADM

·esf-adm：帧格式为ESF ADM

·sf-adm：帧格式为SF ADM

·g751-adm：帧格式为G.751直接成帧

·g751-plcp：帧格式为G.751 PLCP

·g832-adm：帧格式为G.823直接成帧

·cbit-adm：帧格式为C-bit直接成帧

·cbit-plcp：帧格式为C-bit PLCP

·m23-adm：帧格式为M23直接成帧

·m23-plcp：帧格式为M23 PLCP

Code

该ATM接口的线路编码格式：

·ami：线路编码为AMI

·hdb3：线路编码为HDB3

·b8zs：线路编码为B8ZS

Clock

该ATM接口的时钟模式：

·master：主时钟模式

·slave：从时钟模式

Cable length

该ATM接口的电缆模式：

·long：长距模式，151～500米

·short：短距模式，0～150米

Loopback

该ATM接口的环回模式：

·cell：对内进行信元自环

·local：对内自环

·payload：对外载荷环回

·remote：对外线路环回

Cable type

该ATM接口电缆类型

Line Alarm

该ATM接口线路报警

Line Error

该ATM接口线路出错情况：

·FERR：Framing Bit Error（帧比特错误）

·LCV：Line Code Violation（线路编码错误）

·CERR：CRC Errors（循环冗余校验错误）

·FEBE：Far-End Block Error（远端模块错误）

Last link flapping

接口最近一次物理状态改变到现在的时长。Never表示接口从设备启动后一直处于down状态（没有改变过）

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

Last 300 seconds input rate: 0.00 bytes/sec, 0.00 packets/sec

最近300秒钟的平均输入速率：bytes/sec表示平均每秒输入的字节数，packets/sec表示平均每秒输入的报文数

Last 300 seconds output rate: 0.00 bytes/sec, 0.00 packets/sec

最近300秒钟的平均输出速率：bytes/sec表示平均每秒输出的字节数， packets/sec表示平均每秒输出的报文数

Input:

  0 packets, 0 bytes, 0 buffers

  0 errors, 0 crcs, 0 lens, 0 giants

  0 pads, 0 aborts, 0 timeouts

  0 overflows, 0 overruns, 0 no buffer

·packets：接口收到的总报文数

·bytes：接口收到的总字节数

·buffers： 接口接收报文所使用缓冲区个数

·errors：在物理层检测时发现的错误报文数目

·crcs：CRC错误数

·lens： 接口接收到长度错误的报文个数

·giants：接口接收到长度大于规定长度的报文数目

·pads： 接口接收报文进行填充时发生的相关错误个数

·aborts：接收报文的异常错误

·timeouts：接口接收报文超时的个数

·overflows：接口接收报文时芯片FIFO溢出错误个数

·overruns：接收的报文速度大于转发处理能力导致无法处理的报文

·no buffer： 接口接收报文时因系统资源不足产生的相关错误

Output:

  0 packets, 0 bytes, 0 buffers

  0 errors, 0 overflows, 0 underruns

·packets：接口发送的总报文数

·bytes：接口发送的总字节数

·buffers：接口发送报文所使用的缓冲区个数

·errors：在物理层检测时发现的错误报文数目

·overflows：接口发送报文时芯片FIFO溢出错误个数

·underruns：因为接口读取内存的速度小于转发的速度而无法发送报文数目

Brief information on interface(s) under route mode

三层模式下（route）的接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Protocol

接口数据链路层协议状态，取值可能为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口主IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

**ATM接口 \-- ATM接口公共命令 \-- interface atm**

------------------------------------------------------------------------

**[interface atm**]命令用来进入ATM接口或子接口视图。在进入子接口视图之前，如果指定的子接口不存在，则先创建子接口，再进入该子接口的视图。

**[undo interface atm**]命令用来删除ATM子接口。

【命令】

**[interface atm**[ { *interface-number* \| *interface-number.subnumber* [ **p2mp** \| **p2p** ] }]]

**[undo interface atm** *interface-number.subnumber*]

【缺省情况】

不存在ATM子接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*interface-number*：ATM接口编号。

*[interface-number.subnumber*]：ATM子接口编号，其中interface-number为主接口编号；subnumber为子接口编号，取值范围为0～1023。

**[p2mp**]：点到多点子接口。子接口缺省为**p2mp**类型。

**[p2p**]：点到点子接口。

【举例】

\# 进入ATM接口2/4/0接口视图。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0

\# 创建ATM子接口ATM2/4/0.1并进入子接口视图。

\<Sysname\> system-view

Sysname interface atm2/4/0.1

Sysname-ATM2/4/0.1

**ATM接口 \-- ATM接口公共命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

接口的MTU值为1500字节。

【视图】

ATM接口视图（包括13种物理类型：E1、T1、E3、T3、OC-3c/STM-1、OC-12c/STM-4、25M、ADSL、ADSL 2+、G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

ATM子接口视图

EFM接口视图（包括4种物理类型：G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

EFM子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

接口的MTU值影响IP协议报文在该接口上传输时的分片与重组。

【举例】

\# 配置接口ATM2/4/0的MTU值为200字节。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 mtu 200

**ATM接口 \-- ATM接口公共命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除指定接口的统计信息。

【命令】

**[reset counters interface** [ **atm** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[atm**]：清除ATM接口的统计信息。

*[interface-number*]：ATM接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**atm**参数，则清除所有接口的统计信息；

·如果指定**atm**参数而不指定*interface-number*，则清除所有ATM接口的统计信息；

·如果同时指定**atm**和*interface-number*，则清除指定ATM接口的统计信息。

【举例】

\# 清除ATM接口2/4/0的统计信息。

\<Sysname\> reset counters interface atm 2/4/0

**ATM接口 \-- ATM接口公共命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭接口。

**[undo shutdown**]命令用来打开接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

ATM接口处于打开状态。

【视图】

ATM接口视图（包括13种物理类型：E1、T1、E3、T3、OC-3c/STM-1、OC-12c/STM-4、25M、ADSL、ADSL 2+、G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

ATM子接口视图

EFM接口视图（包括4种物理类型：G.SHDSL、SHDSL_4WIRE、SHDSL_4WIRE_BIS、SHDSL_8WIRE_BIS）

EFM子接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭ATM物理接口2/4/0。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0shutdown

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- clock**

------------------------------------------------------------------------

**[clock**]命令用来配置ATM接口的时钟模式。

**[undo clock**]命令用来恢复缺省情况。

【命令】

**[clock**[ { **master** \| **slave** }]]

**[undo clock**]

【缺省情况】

时钟模式为从时钟模式（**slave**）。

【视图】

ATM 25M接口视图

ATM OC-3c/STM-1接口视图

ATM OC-12c/STM-4接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[master**]：配置ATM接口的时钟模式为主时钟模式，使用内部时钟信号。

**[slave**]：配置ATM接口的时钟模式为从时钟模式，使用线路提供的时钟信号。

【使用指导】

当作为DCE设备使用时，应配置ATM接口使用主时钟模式；作为DTE设备使用时，应配置ATM接口使用从时钟模式。

当两台路由器的ATM接口通过光纤直连时，应该将一端的时钟配置为主时钟模式，另一端为从时钟模式。

【举例】

\# 配置ATM接口2/4/0上的时钟为主时钟模式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 clock master

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- flag**

------------------------------------------------------------------------

**[flag**]命令用来配置SONET/SDH帧的开销字节。

**[undo flag**]命令用来恢复SONET/SDH帧开销字节的缺省情况。

【命令】

**[flag**]**c2***flag-value*

**[undo flag c2**]

**[flag****j0**[\| ]**j1**} **[sdh**[\| ]**sonet**} *flag-value*

**[undo flag**]**[j0**[\| ]**j1**} **[sdh**[\| ]**sonet**}

【缺省情况】]

·]**c2**的缺省值为0x13；

·]系统使用SDH帧格式的缺省值，SDH帧格式下**j0**和**j1**的缺省值都为空。

【视图】]

ATM OC-3c/STM-1接口视图

ATM OC-12c/STM-4接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[c2 ***flag-value*]：信号标记字节，属于高阶通道开销（Higher-Order Path Overhead）字节，用于指示虚拟容器VC（Virtual Container）帧的复接结构和信息净负荷的性质。取值范围为0x00～0xFF。

**[j0**]* flag-value*：再生段踪迹字节，属于段开销字节（Section Overhead），用于检测两个端口之间的连接在段层次上的连续性。SDH帧格式下*flag-value*的取值范围为1～15个字符的字符串；SONET帧格式下*flag-value*的取值范围为0x00～0xFF。

**[j1**]* flag-value*：通道踪迹字节，属于高阶通道开销字节，用于检测两个端口之间的连接在通道层次上的连续性。SDH帧格式下*flag-value*的取值范围为1～15个字符的字符串；SONET帧格式下*flag-value*的取值范围为1～62个字符的字符串。

**[sdh**]：帧格式为SDH（Synchronous Digital Hierarchy，同步数字系列）。

**[sonet**]：帧格式为SONET（Synchronous Optical Network，同步光网络）。

【使用指导】

·C2字节和J1字节的设置一定要使收/发两端相匹配，否则会产生告警。

·在同一个运营者的网络内J0字节可为任意字符，而在两个不同运营者的网络边界处要使设备收、发两端的J0字节相匹配。

【举例】

\# 配置ATM接口2/4/0的SDH开销字节J0为ff。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 flag j0 sdh ff

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- frame-format**

------------------------------------------------------------------------

**[frame-format**]命令用来设定ATM接口的帧格式。

**[undo frame-format**]命令用来恢复缺省情况。

【命令】

**[frame-format**[ { **sdh** \| **sonet** }]]

**[undo frame-format**]

【缺省情况】

ATM接口的帧格式为SDH。

【视图】

ATM OC-3c/STM-1接口视图

ATM OC-12c/STM-4接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sdh**]：帧格式为SDH。

**[sonet**]：帧格式为SONET。

【使用指导】

通过**flag**命令设置开销字节时，需要与帧格式匹配。

【举例】

\# 设置ATM接口2/4/0的帧格式为SDH。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 frame-format sdh

【相关命令】

·**flag**

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- link-delay**

------------------------------------------------------------------------

**[link-delay**]命令用来配置ATM接口物理连接状态抑制功能。

**[undo link-delay**]命令用来恢复缺省情况。

【命令】

**[link-delay** *seconds*]

**[undo link-delay**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

ATM 25M接口视图

ATM OC-3c/STM-1接口视图

ATM OC-12c/STM-4接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：物理连接状态的抑制时间，单位为秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

通常情况下，当接口的物理连接状态（up和down）改变时，系统会立即通知上层协议模块并生成Trap和Log信息。为了避免接口物理连接状态在短时间内的频繁改变带来额外的系统开销，可通过本命令配置接口的物理连接状态抑制时间，接口在此时间内产生的物理连接状态变化将被系统忽略。

【举例】

\# 配置ATM接口2/4/0的物理连接状态抑制时间为20秒。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 link-delay 20

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- loopback**

------------------------------------------------------------------------

**[loopback**]命令用来开启ATM接口的环回检测功能并设置检测方式。

**[undo loopback**]命令用来恢复缺省情况。

【命令】

**[loopback**[ { **cell** \| **local** \| **remote** }]]

**[undo loopback**]

【缺省情况】

ATM接口的环回检测功能处于关闭状态。

【视图】

ATM 25M接口视图

ATM OC-3c/STM-1接口视图

ATM OC-12c/STM-4接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cell**]：设置接口对内信元环回。此方式可以用来检测本端物理芯片是否正常。

**[local**]：设置接口对内自环。此方式可以用来检测本端业务芯片是否正常。

**[remote**]：设置接口对外线路环回。此方式可以用来检测对端是否正常。

【使用指导】

只有在进行某些特殊功能测试的时候，才将接口设置为对内自环或对外环回。正常工作时，不要启用环回检测功能。

【举例】

\# 开启ATM接口2/4/0对内自环。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 loopback local

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- scramble**

------------------------------------------------------------------------

**[scramble**]命令用来开启ATM接口对载荷的加扰功能。

**[undo scramble**]命令用来关闭加扰功能。

【命令】

**[scramble**]

**[undo scramble**]

【缺省情况】

ATM接口对载荷的加扰功能处于开启状态。

【视图】

ATM OC-3c/STM-1接口视图

ATM OC-12c/STM-4接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的1或0，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端ATM接口都打开或关闭对载荷的加扰功能，才能对接成功。

**[scramble**]命令只对载荷进行加扰和解扰，不影响信元头。

【举例】

\# 开启ATM接口2/4/0对载荷的加扰功能。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 scramble

**ATM接口 \-- ATM 25M、ATM OC-3c/STM-1、ATM OC-12c/STM-4接口配置命令 \-- threshold**

------------------------------------------------------------------------

![说明](ATM接口命令.files/image004.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[threshold**]命令用来设置ATM接口的SD告警门限和（或）SF告警门限。

**[undo threshold**]命令用来恢复缺省情况。

【命令】

**[threshold** { **sd** *sdvalue* \| **sf** *sfvalue* } \*]

**[undo threshold** [ **sd** \| **sf** ]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

ATM OC-3c/STM-1接口视图

ATM OC-12c/STM-4接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sd**]：表示配置SD（Signal Degrade，信号衰减）告警门限。

*[sdvalue*]：以10e-sd*value*的形式表示的SD告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。*sdvalue*值越大表示SD告警门限越小。

**[sf**]：表示配置SF（Signal Fail，信号失败）告警门限。

*[sfvalue*]：以10e-sf*value*的形式表示的SF告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。*sfvalue*值越大表示SF告警门限越小。

【使用指导】

SD告警和SF告警都是用于指示当前线路性能的，相比较而言，SF告警比SD告警更为严重，SF的误码率门限一般会比SD的误码率门限高，也就是说，当出现少量误码时，设备产生SD告警，当误码率增大到一定程度时，说明线路质量严重下降，此时设备才产生SF告警。因此，应使SD的告警门限小于SF的告警门限，*sdvalue*的值应大于*sfvalue*。

【举例】

\#设置ATM接口2/4/0的SD告警门限为10e-4。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 threshold sd 4

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- cable**

------------------------------------------------------------------------

**[cable**]命令用来配置ATM接口的电缆模式。

**[undo cable**]命令用来恢复缺省情况。

【命令】

**[cable**[ { **long** \| **short** }]]

**[undo cable**]

【缺省情况】

接口链路使用长距模式，在该模式下系统可自动对长距/短距模式进行调整，即缺省模式下先是使用长距模式，如果电缆属于短距离的，那么系统会自动切换成短距模式而无需手工输入命令。

【视图】

ATM E1接口视图/ATM T1接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[long**]：长距模式，电缆长度为151～500米。在该模式下，如果电缆属于短距离的（电缆长度为0～150米），那么系统会自动切换成短距模式。

**[short**]：短距模式，电缆长度为0～150米。

【举例】

\# 设置ATM E1接口2/4/0使用短距模式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 cable short

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- clock**

------------------------------------------------------------------------

**[clock**]命令用来配置ATM接口的时钟模式。

**[undo clock**]命令用来恢复缺省情况。

【命令】

**[clock**[ { **master** \| **slave** }]]

**[undo clock**]

【缺省情况】

时钟模式为从时钟模式（**slave**）。

【视图】

ATM E1接口视图/ATM T1接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[master**]：配置ATM接口的时钟模式为主时钟模式，使用内部时钟信号。

**[slave**]：配置ATM接口的时钟模式为从时钟模式，使用线路提供的时钟信号。

【使用指导】

当作为DCE设备使用时，应配置ATM接口使用主时钟模式；作为DTE设备使用时，应配置ATM接口使用从时钟模式。

当两台路由器的ATM接口通过光纤直连时，应该将一端的时钟配置为主时钟模式，另一端为从时钟模式。

【举例】

\# 配置ATM接口2/4/0上的时钟为主时钟模式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 clock master

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- clock-change auto**

------------------------------------------------------------------------

**[clock-change auto**]命令用来开启接口的时钟自动切换功能。

**[undo clock-change auto**]命令用来关闭时钟自动切换功能，接口恢复成当前用户配置的时钟模式。

【命令】

**[clock-change auto**]

**[undo clock-change auto**]

【缺省情况】

时钟自动切换功能处于关闭状态。

【视图】

ATM E1接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

时钟自动切换功能指的是ATM E1接口在**slave**模式下收到AIS/LOS告警后，接口自动切换成**master**模式。当告警消除后，接口自动切换成用户配置的时钟模式。

【举例】

\# 开启ATM E1接口时钟自动切换功能。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 clock-change auto

【相关命令】

·**clock**

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- code**

------------------------------------------------------------------------

**[code**]命令用来配置ATM接口的线路编码格式。

**[undo code**]用来恢复缺省情况。

【命令】

在ATM E1接口视图下：

**[code**[ { **ami** \| **hdb3** }]]

**[undo code**]

在ATM T1接口视图下：

**[code**[ { **ami** \| **b8zs** }]]

**[undo code**]

【缺省情况】

ATM E1接口的线路编码为HDB3格式；ATM T1接口的线路编码为B8ZS格式。

【视图】

ATM E1接口视图/ATM T1接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ami**]：配置ATM E1/T1线路编码为AMI（Alternate Mark Inversion，信号交替反转码）格式。

**[hdb3**]：配置ATM E1线路编码为HDB3（High Density Bipolar 3，3阶高密度双极性码）格式。

**[b8zs**]：配置ATM T1线路编码为B8ZS（Bipolar 8-zero substitution，双极性8zero替换码）格式。

【使用指导】

线路编码采用AMI格式时，请确保该接口工作在加扰模式（即使用**scramble**命令开启加扰功能）。

两端ATM接口配置的线路编码格式要保持一致。

【举例】

\# 配置ATM接口2/4/0的线路编码为AMI格式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 code ami

【相关命令】

·**scramble**

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- frame-format**

------------------------------------------------------------------------

**[frame-format**]命令用来配置ATM接口的帧格式。

**[undo frame-format**]命令用来恢复缺省情况。

【命令】

在ATM E1接口视图下：

**[frame-format**]**[crc4-adm**[\| ]**no-crc4-adm**}

**[undo frame-format**]

在]ATM T1接口视图下：

**[frame-format**]**[esf-adm**[\| ]**sf-adm**}

**[undo frame-format**]

【缺省情况】]

ATM E1的帧格式为CRC4 ADM，ATM T1的帧格式为ESF ADM。

【视图】

ATM E1接口视图/ATM T1接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[crc4-adm**]：配置ATM E1帧格式为CRC4 ADM。

**[no-crc4-adm**]：配置ATM E1帧格式为No-CRC4 ADM。

**[esf-adm**]：配置ATM T1帧格式为ESF ADM。

**[sf-adm**]：配置ATM T1帧格式为SF ADM。

【使用指导】

ADM（ATM Direct Mapping，ATM直接映射）是指当在E1/T1线路上传输ATM信元时，ATM信元可以直接映射到E1/T1帧中，ITU−T建议G.804和ATM论坛分别定义了ATM直接映射的过程和帧格式，系统根据用户配置的ATM接口的帧格式自动选择对应的ATM直接映射方式。

两端ATM接口配置的帧格式要保持一致。

【举例】

\# 配置ATM E1接口2/4/0使用No-CRC4 ADM帧格式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 frame-format no-crc4-adm

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- loopback**

------------------------------------------------------------------------

**[loopback**]命令用来开启ATM接口的环回检测功能并设置检测方式。

**[undo loopback**]命令用来恢复缺省情况。

【命令】

**[loopback**[ { **cell** \| **local** \| **payload** \| **remote** }]]

**[undo loopback**]

【缺省情况】

ATM接口的环回检测功能处于关闭状态。

【视图】

ATM E1接口视图/ATM T1接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cell**]：设置接口对内信元环回。此方式可以用来检测本端物理芯片是否正常。

**[local**]：设置接口对内自环。此方式可以用来检测本端业务芯片是否正常。

**[payload**]：设置接口对外载荷环回。此方式可以用来检测数据负荷成帧是否正常。

**[remote**]：设置接口对外线路环回。此方式可以用来检测对端是否正常。

【使用指导】

只有在进行某些特殊功能测试的时候，才将接口配置为对内自环或对外环回。正常工作时，不要启用环回检测功能。

【举例】

\# 开启ATM E1接口2/4/0对外载荷环回。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 loopback payload

**ATM接口 \-- ATM E1、ATM T1接口配置命令 \-- scramble**

------------------------------------------------------------------------

**[scramble**]命令用来开启ATM接口对载荷的加扰功能。

**[undo scramble**]命令用来关闭加扰功能。

【命令】

**[scramble**]

**[undo scramble**]

【缺省情况】

ATM接口对载荷的加扰功能处于开启状态。

【视图】

ATM E1接口视图/ATM T1接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的1或0，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端ATM接口都打开或关闭对载荷的加扰功能，才能对接成功。

**[scramble**]命令只对载荷进行加扰和解扰，不影响信元头。

【举例】

\# 开启ATM E1接口对载荷的加扰功能。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 scramble

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- cable**

------------------------------------------------------------------------

**[cable**]命令用来配置ATM T3接口的电缆模式。

**[undo cable**]命令用来恢复缺省情况。

【命令】

**[cable**[ { **long** \| **short** }]]

**[undo cable**]

【缺省情况】

电缆模式为短距模式。

【视图】

ATM T3接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[long**]：长距模式，电缆长度为151～500米。

**[short**]：短距模式，电缆长度为0～150米。

【举例】

\# 配置ATM T3接口2/4/0使用长距模式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 cable long

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- clock**

------------------------------------------------------------------------

**[clock**]命令用来配置ATM接口的时钟模式。

**[undo clock**]命令用来恢复缺省情况。

【命令】

**[clock**[ { **master** \| **slave** }]]

**[undo clock**]

【缺省情况】

时钟模式为从时钟模式（**slave**）。

【视图】

ATM E3接口视图/ATM T3接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[master**]：设置ATM接口的时钟模式为主时钟模式，使用内部时钟信号。

**[slave**]：设置ATM接口的时钟模式为从时钟模式，使用线路提供的时钟信号。

【使用指导】

当作为DCE设备使用时，应配置ATM接口使用主时钟模式；作为DTE设备使用时，应配置ATM接口使用从时钟模式。

当两台路由器的ATM接口通过光纤直连时，应该将一端的时钟配置为主时钟模式，另一端为从时钟模式。

【举例】

\# 设置ATM接口2/4/0上的时钟为主时钟模式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 clock master

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- frame-format**

------------------------------------------------------------------------

**[frame-format**]命令用来配置ATM接口的帧格式。

**[undo frame-format**]命令用来恢复缺省情况。

【命令】

在ATM E3接口视图下：

**[frame-format**[ { **g751-adm** \| **g751-plcp** \| **g832-adm** }]]

**[undo frame-format**]

在ATM T3接口视图下：

**[frame-format**[ { **cbit-adm** \| **cbit-plcp** \| **m23-adm** \| **m23-plcp** }]]

**[undo frame-format**]

【缺省情况】

ATM E3接口的帧格式为G.751 PLCP，ATM T3接口的帧格式为C-bit PLCP。

【视图】

ATM E3接口视图/ATM T3接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[g751-adm**]：配置ATM E3的帧格式为G.751直接成帧。

**[g751-plcp**]：配置ATM E3的帧格式为G.751 PLCP。

**[g832-adm**]：配置ATM E3的帧格式为G.823直接成帧。

**[cbit-adm**]：配置ATM T3的帧格式为C-bit直接成帧。

**[cbit-plcp**]：配置ATM T3的帧格式为C-bit PLCP。

**[m23-adm**]：配置ATM T3的帧格式为M23直接成帧。

**[m23-plcp**]：配置ATM T3的帧格式为M23 PLCP。

【举例】

\# 配置ATM E3接口2/4/0使用的帧格式为G.832直接成帧。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 frame-format g832-adm

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- loopback**

------------------------------------------------------------------------

**[loopback**]命令用来开启接口的环回检测功能并设置检测方式。

**[undo loopback**]命令用来恢复缺省情况。

【命令】

**[loopback**[ { **cell** \| **local** \| **payload** \| **remote** }]]

**[undo loopback**]

【缺省情况】

环回检测功能处于关闭状态。

【视图】

ATM E3接口视图/ATM T3接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cell**]：设置接口对内信元环回。此方式可以用来检测本端物理芯片是否正常。

**[local**]：设置接口对内自环。此方式可以用来检测本端业务芯片是否正常。

**[payload**]：设置接口对外载荷环回。此方式可以用来检测数据负荷成帧是否正常。

**[remote**]：设置接口对外线路环回。此方式可以用来检测对端是否正常。

【使用指导】

只有在进行某些特殊功能测试的时候，才将接口配置为对内自环或对外环回。正常工作时，不要启用环回检测功能。

【举例】

\# 开启ATM T3接口2/4/0对外载荷环回。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 loopback payload

**ATM接口 \-- ATM E3、ATM T3接口配置命令 \-- scramble**

------------------------------------------------------------------------

**[scramble**]命令用来开启ATM接口对载荷的加扰功能。

**[undo scramble**]命令用来关闭加扰功能。

【命令】

**[scramble**]

**[undo scramble**]

【缺省情况】

ATM接口对载荷的加扰功能处于开启状态。

【视图】

ATM E3接口视图/ATM T3接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的1或0，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端ATM接口都打开或关闭对载荷的加扰功能，才能对接成功。

**[scramble**]命令只对载荷进行加扰和解扰，不影响信元头。

【举例】

\# 开启ATM T3接口2/4/0对载荷的加扰功能。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 scramble

**ATM接口 \-- ADSL接口配置命令 \-- activate**

------------------------------------------------------------------------

**[activate**]命令用来激活ADSL接口。

**[undo activate**]命令用来去激活ADSL接口。

【命令】

**[activate**]

**[undo activate**]

【缺省情况】

ADSL接口处于激活状态。

【视图】

ATM ADSL接口视图/ATM ADSL 2+接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

CPE（Customer Premises Equipment，用户侧设备）设备上的ADSL接口在进行业务传输前必须先激活。

激活是指局端设备CO（Central Office，中心局）与用户CPE之间进行的一系列的握手训练和交换信息的操作。激活过程将根据CO设备的线路配置模板中制定的ADSL标准、通道方式、上下行线路速率、规定的噪声容限等设定，检测线路距离和线路状况，在CO设备与CPE设备之间进行协商，确认能否在上述条件下正常工作。如果激活成功，则在CO设备与CPE设备建立起了通信连接，此时，就可以传输业务了。

线路激活协商连接参数时，CO设备处于主导地位，CPE设备处于从属地位，也就是说，大多数连接参数都是由CO设备提供并拥有最终的决定权。典型的激活时间是30秒（激活时间是指从线路开始协商到线路up的时间）。

激活的相反操作是去激活。去激活后，CO设备与CPE设备建立通信的连接不再存在。

ADSL不同于DDR，ADSL是永远在线的。所以，路由器开机后ADSL接口会自己启动激活任务，进入激活状态。只要线路良好，就应该始终处于激活状态。路由器会定时检测线路的状态，如果线路质量恶化，路由器会自动将线路去激活，重新训练，重新激活。

本命令用于手工的激活/去激活ADSL接口，主要在测试和故障诊断时使用。

【举例】

\# 激活ADSL接口ATM2/4/0。

\<Sysname\> system-view

Sysname interface atm2/4/0

Sysname-ATM2/4/0 activate

**ATM接口 \-- ADSL接口配置命令 \-- adsl standard**

------------------------------------------------------------------------

**[adsl standard**]命令用来配置ADSL接口使用的工作标准。

**[undo adsl standard**]命令用来恢复缺省情况。

【命令】

在ATM ADSL接口视图下：

**[adsl standard**[ { **auto** \| **gdmt** \| **glite** \| **t1413** }]]

**[undo adsl standard**]

在ATM ADSL 2+接口视图下：

**[adsl standard**[ { **auto** \| **g9923** \| **g9925** \| **gdmt** \| **glite** \| **t1413** }]]

**[undo adsl standard**]

【缺省情况】

ADSL接口使用的工作标准是自适应方式。

【视图】

ATM ADSL接口视图/ATM ADSL 2+接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：自适应方式。由ADSL接口芯片自动与对端协商使用的工作标准。

**[g9923**]：使用ADSL2(G992.3)标准。

**[g9925**]：使用ADSL2+(G992.5)标准。

**[gdmt**]：使用G.DMT（G992.1）标准。

**[glite**]：使用G.Lite（G992.2）标准。

**[t1413**]：使用T1.413标准。

【使用指导】

ADSL-I模块不支持G.Lite（G992.2）和T1.413标准。

两端ADSL接口需要使用相同的工作标准。

该项配置不会立即生效，只有下一次激活或开启接口后才能够起作用。如果用户要立即生效，可以执行**shutdown**/**undo shutdown**或者**undo activate**/**activate**操作。

【举例】

\# 配置ATM2/4/0接口使用的工作标准为T1.413。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 adsl standard t1413

**ATM接口 \-- ADSL接口配置命令 \-- adsl tx-attenuation**

------------------------------------------------------------------------

**[adsl tx-attenuation**]命令用来配置ADSL接口的发送功率衰减值。

**[undo adsl tx-attenuation**]命令用来恢复缺省情况。

【命令】

**[adsl tx-attenuation** *attenuation*]

**[undo adsl tx-attenuation**]

【缺省情况】

ADSL接口的发送功率衰减值为0，表示不衰减。

【视图】

ATM ADSL接口视图/ATM ADSL 2+接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[attenuation*]：发送功率的衰减值，取值范围为0～12，单位为dB。

【使用指导】

本命令的配置会影响ADSL接口发送信号功率的大小。配置的衰减值越大，表示发送功率越小；配置的衰减值越小，表示发送功率越大。如果发送功率太大，可能会影响其它ADSL接口发送的信号。

【举例】

\# 配置ADSL接口的发送功率衰减值为10。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 adsl tx-attenuation 10

**ATM接口 \-- ADSL接口配置命令 \-- display dsl configuration**

------------------------------------------------------------------------

**[display dsl configuration**]命令用来显示ADSL接口的配置信息。

【命令】

**[display dsl configuration interface atm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface atm** *interface-number*]：显示指定ADSL接口的配置信息。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 显示ADSL接口ATM2/4/0的配置信息。

\<Sysname\> display dsl configuration interface atm 2/4/0

Line Params Set by User:

  Standard:               T1.413

  Annex:                  A

  Coding Gain(dB):        Auto

  Tx Pow Attn(dB):        0

  Bit-Swap:               disable

 Actual Config           Near End        Far End

Standard:               T1.413          T1.413

Trellis Coding:         Enable          Enable

 Vendor ID:              0x0039          0x0004

                         AS0 (DS)        LS0(US)

 Rate(Bytes):            238             26

 Rate(kbps):             7616            832

 Latency:                Intlv           Intlv

表1-4 display dsl configuration命令显示信息描述表

字段

描述

以下信息为配置信息：

Standard

接口链路配置的标准：（此参数可以通过**adsl standard**命令进行配置）

·Auto：自适应方式（缺省情况标准值）

·G992.3：使用ADSL2（G992.3）标准

·G992.5：使用ADSL2+（G992.5）标准

·G992.1：使用G.DMT（G992.1）标准

·G992.2：使用G.Lite（G992.2）标准

·T1.413：使用T1.413标准

Annex

接口链路所采用的附加标准：（此参数为预设值，用户不能修改）

·A：Annex A标准（表示ADSL接口类型为ADSL over POTS）

·B：Annex B标准（表示ADSL接口类型为ADSL over ISDN）

Coding Gain(dB)

接口线路所采用的编码增益，单位为dB（此参数为预设值，用户不能修改）

Auto表示自动协商编码增益

Tx Pow Attn(dB)

接口链路的发送功率衰减，单位为dB（此参数为预设值，用户不能修改）

Bit-Swap

比特交换功能使能情况（此参数为预设值，用户不能修改）

·enable：使能

·disable：未使能

以下信息只有在线路激活以后才会显示：

Standard

接口实际生效的标准：

·Auto：自适应方式（缺省情况标准值）

·G992.3：使用ADSL2（G992.3）标准

·G992.5：使用ADSL2+（G992.5）标准

·G992.1：使用G.DMT（G992.1）标准

·G992.2：使用G.Lite（G992.2）标准

·T1.413：使用T1.413标准

Trellis Coding

网格编码功能使能情况：

·Enable：使能

·Disable：未使能

Vendor ID

厂商ID，表示生产芯片的厂商编号

Rate(Bytes)

表示协商速率，AS0 (DS)下行，LS0 (US)上行，单位是Bytes

Rate(kbps)

表示协商速率，AS0 (DS)下行，LS0 (US)上行，单位是kbps

Latency

表示使用的数据编码模式：

·{.TableTextChar}Fast：快速模式（该模式的特点：线路时延较小，线路质量较差）

·Interleave：交织模式（该模式的特点：纠错能力强，线路时延较大）

**ATM接口 \-- ADSL接口配置命令 \-- display dsl status**

------------------------------------------------------------------------

**[display dsl status**]命令用来显示ADSL接口的状态信息。

【命令】

**[display dsl status interface atm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface atm** *interface-number*]：显示指定ADSL接口的状态信息。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 显示ADSL接口ATM2/4/0的状态信息。

\<Sysname\> display dsl status interface atm 2/4/0

Line Status:            Loss Of Signal

Training Status:        Idle

Active Params           Near End        Far End

Standard:               G.dmt           G.dmt

SNR (dB):               0.0             0.0

Attn(dB):               0.0             0.0

Pwr(dBm):               0.0             0.0

Current Rate(kbps):     0               0

Latency:                Intl            Intl

表1-5 display dsl status命令显示信息描述表

字段

描述

Line Status

ADSL链路当前所处的状态：

·No Defect：正常状态{.TableTextChar}

·Loss Of Frame：帧错误{.TableTextChar}

·Loss Of Signal：信号错误{.TableTextChar}

·Loss Of Power：电源错误{.TableTextChar}

·Loss Of Signal Quality：信号质量错误{.TableTextChar}

·Unknown：未知{.TableTextChar}

Training Status

ADSL链路同DSLAM（Digital Subscriber Line Access Multiplexer，数字用户线路接入复用器）设备训练过程中所处的状态：

·Idle：空闲{.TableTextChar}

·G.994 Training：{.TableTextChar}G.994训练{.TableTextChar}

·G.992 Started：{.TableTextChar}G.992开始{.TableTextChar}

·G.922 Channel Analysis：{.TableTextChar}G.922通道分析{.TableTextChar}

·G.992 Message Exchange：{.TableTextChar}G.992消息交换{.TableTextChar}

·Showtime：正常数据交换{.TableTextChar}

·Unknown：未知{.TableTextChar}

以下信息只有在线路激活以后才会显示：

Active Params

·Standard：ADSL链路同DSLAM设备当前的连接标准

·SNR：当前ADSL链路的信噪比，信噪比越大，表示信号质量越好

·Attn：当前ADSL链路的衰减，衰减越大，说明线路状况越差

·Pwr：当前ADSL模块的发射能量，单位为dbm

·Current Rate：ADSL链路的速率，单位为kbps

·Latency：ADSL链路的数据编码模式，分为Intl（交织）和Fast（快速）两种

Near End表示下行方向（接口接收报文的方向），Far End表示上行方向（接口发送报文的方向）

**ATM接口 \-- ADSL接口配置命令 \-- display dsl version**

------------------------------------------------------------------------

**[display dsl version**]命令用来显示ADSL接口的版本信息和支持的能力。

【命令】

**[display dsl version interface atm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface atm**]*interface-number*：显示指定ADSL接口的版本信息和支持的能力。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 显示ADSL接口ATM2/4/0的版本信息和支持的能力。

\<Sysname\> display dsl version interface atm 2/4/0

ADSL board chipset and version info:

  DSL Line Type:          ADSL Over Pots

  Chipset Vendor:         BDCM

  FW Release:             A2pB017l.d15h

  DSP Version:            17.1200

  AFE Version:            1.0

  Bootrom Version:        1.1

  Hardware Version:       4.0

  Driver Version:         1.3

  CPLD Version:           1.0

ADSL Capability:

  ANNEX Supported:

    ANNEX A

  Standard Supported:

    ANSI T1.413 Issue 2

    ITU G992.1(G.dmt)

    ITU G992.2(G.lite)

    ITU G992.3(Adsl2)

    ITU G992.3(ReAdsl2)

    ITU G992.5(Adsl2p)

表1-6 display adsl version命令显示信息描述表

字段

描述

ADSL board chipset and version info

接口板的版本信息和厂商信息

DSL Line Type

用户接入线的类型，取值为

·ADSL over ISDN：ADSL承载在ISDN线路上，ADSL信号的频段分布在比较高的频段，ISDN信号的频段分布在比较低的频段

·ADSL Over Pots：ADSL承载在电话线路上

Chipset Vendor

ADSL Chipsets的厂商标识

FW Release

FirmWare的标识和版本信息

DSP Version

DSP版本

AFE Version

AFE版本

Bootrom Version

Bootrom的版本号

Hardware Version

接口板硬件的版本号

Driver Version

驱动软件的版本号

CPLD Version

逻辑器件的版本号

ADSL Capability

该接口支持的标准及其附加标准

**ATM接口 \-- G.SHDSL接口配置命令 \-- activate**

------------------------------------------------------------------------

**[activate**]命令用来激活ATM接口。

**[undo activate**]命令用来去激活ATM接口。

【命令】

**[activate**]

**[undo activate**]

【缺省情况】

接口处于激活状态。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

CPE设备上的SHDSL类型的ATM接口在进行业务传输前必须先激活。

激活是指局端设备CO（Central Office，中心局）与用户CPE之间进行的一系列的握手训练和交换信息的操作。激活过程将根据CO设备的线路配置模板中制定的SHDSL标准、通道方式、上下行线路速率、规定的噪声容限等设定，检测线路距离和线路状况，在CO设备与CPE设备之间进行协商，确认能否在上述条件下正常工作。如果激活成功，则在CO设备与CPE设备建立起了通信连接，此时，就可以传输业务了。

线路激活协商连接参数时，CO设备处于主导地位，CPE设备处于从属地位，也就是说，大多数连接参数都是由CO设备提供并拥有最终的决定权。典型的激活时间是30秒（激活时间是指从线路开始协商到线路up的时间）。

激活的相反操作是去激活。去激活后，CO设备与CPE设备建立通信的连接不再存在。

SHDSL类型的ATM接口是永远在线的。所以，路由器开机后SHDSL类型的ATM接口会自己启动激活任务，进入激活状态。只要线路良好，就应该始终处于激活状态。路由器会定时检测线路的状态，如果线路质量恶化，路由器会自动将线路去激活，重新训练，重新激活。

本命令用于手工的激活/去激活SHDSL类型的ATM接口，主要在测试和故障诊断时使用。

【举例】

\# 激活ATM2/4/0接口。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 activate

**ATM接口 \-- G.SHDSL接口配置命令 \-- display dsl configuration**

------------------------------------------------------------------------

**[display dsl configuration**]命令用来显示ATM接口的配置信息。

【命令】

**[display dsl configuration interface atm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface atm** *interface-number*]：显示指定ATM接口的配置信息。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 显示G.SHDSL接口ATM2/4/0的配置信息。

\<Sysname\> display dsl configuration interface atm 2/4/0

Line parameter and mode configuration:

  Mode:           CPE

  Standard:       G.991.2

  Annex:          B

Wire type:      2

Line rate:      Auto Adaptive

Current margin: 2

SNEXT margin:   0

PSD mode:       Sym PSD

Actual handshake status:

00: 0002 0000 0000 0000 0000 0000 0000 0000 0000 0000

10: 0000 0008 0000 0000 0000 0000 0000 0000 0008 0000

20: 0000 0000 0002 0002 0004 0010

Local handshake status:

00: 0002 0001 0000 0000 0000 0000 0034 003f 003f 003f

10: 003f 003f 0003 0034 003f 003f 003f 003f 003f 0003

20: 0000 0000 0003 0003 000f 0010

Remote handshake status:

00: 0002 0000 0000 0000 0000 0000 0030 003f 003f 003f

10: 003f 000f 0000 0030 003f 003f 003f 003f 000f 0000

20: 0000 0000 0003 0003 0003 0004 0010

表1-7 display dsl configuration命令显示信息描述表

字段

描述

Mode

工作模式：CPE为用户端，CO为中心局端

Standard

所支持的标准规范：（此参数为预设值，用户不能修改）

·Auto：自适应方式（缺省情况标准值）

·G992.3：使用ADSL2（G992.3）标准

·G992.5：使用ADSL2+（G992.5）标准

·G992.1：使用G.DMT（G992.1）标准

·G992.2：使用G.Lite（G992.2）标准

·T1.413：使用T1.413标准

·G.SHDSL.bis：协商采用物理层标准是G.BIS标准

Annex

接口链路所采用的附加标准：

·A：Annex A标准

·B：Annex B标准

Wire type

连线类型，分为2线制和4线制

Current margin

当前信噪比容限量

SNEXT margin

最差的信噪比容限量

Line rate

线路速率

PSD mode

功率频谱密度方式，分为对称（Sym）和非对称方式（Asym）

Actual handshake status

实际的握手状态

Local handshake status

本端的握手状态

Remote handshake status

远端的握手状态

**ATM接口 \-- G.SHDSL接口配置命令 \-- display dsl status**

------------------------------------------------------------------------

**[display dsl status**]命令用来显示ATM接口的状态信息。

【命令】

**[display dsl status interface atm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface atm** *interface-number*]：显示指定ATM接口的状态信息。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 当接口状态为up时显示两线G.SHDSL接口的状态信息。

\<Sysname\> display dsl status interface atm 2/4/0

Operating Mode:CPE

DSL Mode:SHDSL Annex B

Configured Wire Type:2

Line A Statistics since last activation:

CRC:            0

LOSW Defect:    0

ES:             0

SES:            0

UAS:            0

TX EOC:         0

RX EOC:         0

Line A status:

Xcvr Op State:          Data Mode

Last Fail Op State:     0x00

Line Rate(Kbps):        2312

Wire Type:              2

SNR Margin(dB):         16.30

Loop Attenuation(dB):   0.00

RecvGain(dB):           6.07

TxPower(dBm):           9.50

Power Backoff:          enable

Power Backoff Level:    5

Tip/Ring Reversal:      Reversed

FrmOH Stat:             0x00

Rmt Encoder A:          0x0000016e

Rmt Encoder B:          0x00000331

Rmt NSF Cusdata:        0x0000

Rmt NSF CusID:          0x0000

Rmt Country Code:       0x00b5

Rmt Provider Code:      GSPN

Rmt Vendor Data:        0x12 0x34 0x56 0x78

                        0x12 0x34 0x56 0x78

\# 当接口状态为up时显示四线G.SHDSL接口的状态信息。

\<Sysname\> display dsl status interface atm 2/4/0

Operating Mode:         CPE

DSL Mode:               SHDSLAnnex B

Configured Wire Type:   4

Line A Statistics since last activation:

CRC:             0

LOSW Defect:     0

ES:              0

SES:             0

UAS:             0

TX EOC:          0

RX EOC:          0

Line A status:

Xcvr Op State:          Data Mode

Last Fail Op State:     0x00

Line Rate(Kbps):        2312

Wire Type:              4

SNR Margin(dB):         13.30

Loop Attenuation(dB):   0.00

RecvGain(dB):           5.86

TxPower(dBm):           9.50

Power Backoff:          enable

Power Backoff Level:    5

Tip/Ring Reversal:      Reversed

FrmOH Stat:             0x00

Rmt Encoder A:          0x0000016e

Rmt Encoder B:          0x00000331

Rmt NSF Cusdata:        0x0000

Rmt NSF CusID:          0x0000

Rmt Country Code:       0x00b5

Rmt Provider Code:      GSPN

Rmt Vendor Data:        0x12 0x34 0x56 0x78

                        0x12 0x34 0x56 0x78

Line B Statistics since last activation:

CRC:            1

LOSW Defect:    1

ES:             1

SES:            1

UAS:            0

TX EOC:         0

RX EOC:         0

Line B status:

Xcvr Op State:          Data Mode

Last Fail Op State:     0x00

Line Rate(Kbps):        2312

Wire Type:              4

SNR Margin(dB):         12.30

Loop Attenuation(dB):   0.00

RecvGain(dB):           5.28

TxPower(dBm):           9.50

Power Backoff:          enable

Power Backoff Level:    5

Tip/Ring Reversal:      Reversed

FrmOH Stat:             0x00

Rmt Encoder A:          0x0000016e

Rmt Encoder B:          0x00000331

Rmt NSF Cusdata:        0x0000

Rmt NSF CusID:          0x0000

Rmt Country Code:       0x00b5

Rmt Provider Code:      GSPN

Rmt Vendor Data:        0x12 0x34 0x56 0x78

                        0x12 0x34 0x56 0x78

表1-8 display dsl status命令显示信息描述表

字段

描述

Operating Mode

工作模式：CPE为用户端，CO为中心局端

DSL Mode

接口链路所采用的附加标准：

·SHDSL Annex A：Annex A标准

·SHDSL Annex B：Annex B标准

Configured Wire Type

配置连线类型，分为2线制和4线制

Line A Statistics since last activation

从激活时开始到现在A线对的统计信息

CRC

CRC错误数

LOSW Defect

同步丢失错误数

ES

每秒错误数

SES

每秒严重错误数

UAS

每秒不可用状态计数

TX EOC

发送EOC信源计数

RX EOC

接收EOC信源计数

Line A status

A线对状态

Xcvr Op State

收发器工作状态：

·Idle：空闲状态

·Data Mode：激活状态

·HandShaking：激活握手阶段

·Training：激活训练阶段

Last Fail Op State

上次协商失败收发器工作状态，可能的取值同上

Line Rate(Kbps)

协商线对速率

Wire Type

线数类型，可能的取值有2（2线制）、4（4线制）

SNR Margin(dB)

信噪比容限量

Loop Attenuation(dB)

环路衰减

RecvGain(dB)

接收增益

TxPower(dBm)

发送功率

Power Backoff

功率补偿状态

Power Backoff Level

功率补偿级别

Tip/Ring Reversal

Tip/Ring翻转状态

FrmOH Stat

帧溢出状态

Rmt Encoder A

远端译码器系数A

Rmt Encoder B

远端译码器系数B

Rmt NSF Cusdata

远端非标准格式用户数据

Rmt NSF CusID

远端非标准格式用户ID

Rmt Country Code

远端国家代码

Rmt Provider Code

远端芯片供应商代码

Rmt Vendor Data

远端制造商代码

**ATM接口 \-- G.SHDSL接口配置命令 \-- display dsl version**

------------------------------------------------------------------------

**[display dsl version**]命令用来显示ATM接口的版本信息和支持的能力。

【命令】

**[display dsl version interface atm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface atm** *interface-number*]：显示指定ATM接口的版本信息和支持的能力。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 显示G.SHDSL接口2/4/0上的版本信息和支持的能力。

\<Sysname\> display dsl version interface atm 2/4/0

DSL Line Type:          G.SHDSL

ATM SAR Device:         0x823614f1

ATM SAR Revision:       0x02

Chipset Vendor:         GSPN

Firmware Rel-Rev:       R2.3.1-0

DSP Version:            1

PCB Version:            0.0

CPLD Version:           0.0

Driver Version:         2.0

Hardware Version:       1.0

ITU G991.2 ANNEX A:     Supported

ITU G991.2 ANNEX B:     Supported

表1-9 display dsl version命令显示信息描述表

字段

描述

DSL Line Type

用户接入线的类型

ATM SAR Device

SAR芯片的标识

ATM SAR Revision

SAR芯片的修改标识

Chipset Vendor

DSL Chipsets的厂商标识

Firmware Rel-Rev

FirmWare的标识和版本信息

DSP Version

DSP版本

PCB Version

单板PCB的版本号

CPLD Version

逻辑器件的版本号

Driver Version

驱动软件的版本号

Hardware Version

硬件版本

ITU G991.2 ANNEX A，ITU G991.2 ANNEX B

支持的标准及其附加标准

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl annex**

------------------------------------------------------------------------

**[shdsl annex**]命令用来配置ATM接口所支持的Annex标准。

**[undo shdsl annex**]命令用来恢复缺省情况。

【命令】

**[shdsl annex**[ { **a** \| **b** }]]

**[undo shdsl annex**]

【缺省情况】

支持的Annex标准为Annex b。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[a**]：支持的Annex标准为Annex a。

**[b**]：支持的Annex标准为Annex b。

【使用指导】

如果CO设备和CPE设备选用的Annex标准不一样，线路会难以激活，两设备之间将无法建立连接。

Annex a/b均是G.991.2的标准，Annex a主要在北美应用，Annex b主要在欧洲应用，其它地区网络要根据当地网络的不同，选择不同的标准，例如中国地区网络执行的标准类型为Annex b。

【举例】

\# 配置G.SHDSL接口ATM2/4/0所支持的标准为Annex a。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl annex a

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl capability**

------------------------------------------------------------------------

**[shdsl capability**]命令用来配置接口的协商能力。

**[undo shdsl capability**]命令用来恢复缺省情况。

【命令】

**[shdsl capability**[ { **auto** \| **g-shdsl** \| **g-shdsl-bis** }]]

**[undo shdsl capability**]

【缺省情况】

在CPE模式下，采用**auto**方式。

在CO模式下，采用**g-shdsl-bis**方式。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：自动选择与对端接口相同的协商能力（只在CPE模式下支持，在CO模式下不支持）。

**[g-shdsl**]：使用G.SHDSL。

**[g-shdsl-bis**]：使用G.SHDSL.bis。

【使用指导】

在CPE模式下支持g-shdsl和g-shdsl-bis以及auto。

在CO模式下支持g-shdsl和g-shdsl-bis，不支持auto。

在配置**shdsl mode**时，会自动恢复为各自模式下的缺省配置。

两端接口需要使用相同的协商能力，才能协商成功。

【举例】

\# 配置接口的协商能力为G.SHDSL。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl capability g-shdsl

【相关命令】

·**shdsl mode**

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl line-probing**

------------------------------------------------------------------------

**[shdsl line-probing enable**]命令用来开启SHDSL线路的探询功能。

**[undo shdsl line-probing enable**]命令用来关闭SHDSL线路的探询功能。

【命令】

**[shdsl line-probing enable**]

**[undo shdsl line-probing enable**]

【缺省情况】

SHDSL线路的探询功能处于开启状态。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启探询功能后，在线路激活的过程中，系统将执行线路探询功能去协商最佳的线路速率；若关闭探询功能，系统会选择CPE和CO都支持的速率交集中的最大速率。这种方式因为跳过了线路速率的适配过程，减短了激活SHDSL线路的时间。

【举例】

\# 关闭SHDSL线路的探询功能。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 undo shdsl line-probing enable

【相关命令】

·**activate**

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl mode**

------------------------------------------------------------------------

**[shdsl mode**]命令用来配置ATM接口的工作模式。

**[undo shdsl mode**]命令用来恢复缺省情况。

【命令】

**[shdsl mode **[{ **co** \| **cpe** }]]

**[undo shdsl mode**]

【缺省情况】

工作模式为CPE模式。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[co**]：设置为CO（Central Office，中心局）模式。

**[cpe**]：设置为CPE（Customer Premises Equipment，用户侧设备）模式。

【使用指导】

两台设备直连时，必须把一端配置为CO模式，另一端配置成CPE模式。

【举例】

\# 配置ATM2/4/0工作在CO模式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl mode co

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl pam**

------------------------------------------------------------------------

**[shdsl pam**]用来配置PAM（Pulse Amplitude Modulation，脉冲调制） Constellation。

**[undo shdsl pam**]用来恢复缺省情况。

【命令】

**[shdsl pam****16**[\| ]**32**[\| ]**auto**}

**[undo shdsl pam**]

【缺省情况】]

自动选择PAM。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[16**]：使用16 PAM Constellation。在16 PAM下，速率范围为192～3840，单位为kbps。

**[32**]：使用32 PAM Constellation。在32 PAM下，速率范围为768～5696，单位为kbps。

**[auto**]：根据线路两端的参数自动选择两端都支持的最好的PAM（32 PAM比16 PAM好）。

【使用指导】

PAM是数字线路的一种编码模式，叫脉冲调制模式，Constellation用来形容PAM编码模式像星座。本命令用于配置PHY芯片的数字信号调制模式。

当接口的协商能力为G.SHDSL时，不支持32 PAM Constellation。

【举例】

\# 配置ATM2/4/0使用16 PAM Constellation。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl pam 16

【相关命令】

·**shdsl capability**

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl pbo**

------------------------------------------------------------------------

**[shdsl pbo**]命令用来调整发送功率。

**[undo shdsl pbo**]命令用来恢复缺省情况。

【命令】

**[shdsl pbo** }

**[undo shdsl pbo**]

【缺省情况】]

自动调整发送功率。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：自动调整发送功率。

*[value*]：发送功率调整值，取值范围为0～31，单位为dB。

【使用指导】

正常情况下，接口会根据线路噪声情况，自动调整发送功率，以保证可以获得合适的信噪比。当线路的噪声已知的情况下，或者自动调整不准确的时候，可以通过此命令行手动调整发射功率。

【举例】

\# 设置ATM2/4/0接口的发送功率调整值为20db。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl pbo 20

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl psd**

------------------------------------------------------------------------

**[shdsl psd**]命令用来配置ATM接口的功率频谱密度模式。

**[undo shdsl psd**]命令用来恢复缺省情况。

【命令】

**[shdsl psd**[ { **asymmetry** \| **symmetry** }]]

**[undo shdsl psd**]

【缺省情况】

功率频谱密度模式为对称模式。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[asymmetry**]：功率频谱密度模式为非对称模式。

**[symmetry**]：功率频谱密度模式为对称模式。

【使用指导】

PSD（Power Spectral Density，功率频谱密度）指发射功率在最高准位时，一脉冲或一序列脉冲，其单位带宽的总输出能量除以总脉冲持续时间。

【举例】

\# 配置ATM2/4/0的功率频谱密度模式为非对称模式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl psd asymmetry

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl rate**

------------------------------------------------------------------------

**[shdsl rate**]命令用来配置ATM接口单线对的速率。

**[undo shdsl rate**]命令用来恢复缺省情况。

【命令】

**[shdsl rate**[ { *rate* \| **auto** }]]

**[undo shdsl rate**]

【缺省情况】

ATM G.SHDSL、ATM SHDSL_4WIRE_BIS、ATM SHDSL 8WIRE_BIS接口的单线对速率为自动协商方式。

ATM SHDSL_4WIRE接口，在两线模式下单线对速率为自动协商方式，在非两线模式下的单线对速率为2312kbit/s（即四线接口速率为4624kbit/s）。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rate*]：ATM接口的单线对速率最大值。对于ATM G.SHDSL接口和ATM SHDSL_4WIRE接口，取值范围为192～2312，单位为kbit/s；对于ATM SDHSL_4WIRE_BIS接口和ATM SHDSL_8WIRE_BIS接口，取值范围为192～5696，单位为kbit/s。

**[auto**]：为自动协商方式。

【使用指导】

在实际使用中，最大下行速率还会受局端设备的限制和线路条件的限制，有可能达不到设置的值。如果将速率设置成自动协商方式，在激活过程中两端会根据当前的线路状况协商出一个合适的速率；如果CPE端和CO端设置成固定速率，CPE端和CO端将进行速率协商，若无法满足二者之中较低的速率要求的时候，线路无法被激活。

需要注意的是：

·四线（即双线对）的ATM接口的速率为单线对速率的两倍。例如设置单线对速率为2312kbit/s，则四线接口的速率为4624kbit/s。

·四线的ATM接口的单线对速率无法配置成auto方式，因为四线的接口无法进行速率的协商。

【举例】

\# 配置ATM2/4/0的单线对速率为自动协商方式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl rate auto

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl snr-margin**

------------------------------------------------------------------------

**[shdsl snr-margin**]命令用来配置接口链路的信噪比容限量。

**[undo shdsl snr-margin**]命令用来恢复缺省情况。

【命令】

**[shdsl snr-margin** [ **current** *current-margin-value*   **snext** *snext-margin-value* ]]

**[undo shdsl snr-margin**]

【缺省情况】

线路协商时current-margin-value为2，snext-margin-value为0。

【视图】

ATM G.SHDSL接口视图/ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[current*** current-margin-value*]：当前信噪比容限量。*current-margin-value*的取值范围为0～10，缺省值为2。SHDSL线路在训练的时候以线路信噪比门限加上*current-margin-value*进行训练。配置比较大的*current-margin-value*可以使得协商成功的链路更加稳定，抗噪能力更强。

**[snext ***snext-margin-value*]：最差的信噪比容限量。*snext-margin-value*的取值范围为0～10，缺省值为0。SHDSL线路在训练的时候以最差信噪比门限加上*snext-margin-value*进行训练。设置比较大的*snext-margin-value*可以使得协商成功的链路更加稳定，抗噪能力更强。

【使用指导】

配置信噪比容限量会影响线路支持的最大速率。因此在线路比较好的情况下，可以配置较小的信噪比容限量，以获得更高的速率。但是，在线路存在较多的噪声的情况下，配置过小的当前信噪比容限量会造成线路容易掉线。

【举例】

\# 配置接口ATM2/4/0的当前信噪比容限量为5。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl snr-margin current 5

**ATM接口 \-- G.SHDSL接口配置命令 \-- shdsl wire**

------------------------------------------------------------------------

**[shdsl wire**]命令用来配置四线和八线SHDSL接口的连线模式。

**[undo shdsl wire**]命令用来恢复缺省情况。

【命令】

在ATM SHDSL_4WIRE、ATM SHDSL_4WIRE_BIS接口视图下：

**[shdsl wire**[ { **2** \| **4-auto-enhanced** \| **4-enhanced** \| **4-standard** }]]

**[undo shdsl wire**]

在ATM SHDSL_8WIRE_BIS接口视图下：

**[shdsl wire**[ { **2** \| **4-enhanced** \| **4-standard** \| **6** \| **8** \| **auto** }]]

**[undo shdsl wire**]

【缺省情况】

ATM SHDSL_4WIRE接口的连线模式为**4-enhanced**（四线增强模式）。

ATM SHDSL 4WIRE_BIS接口的连线模式为**4-standard**（四线标准模式）。

ATM SHDSL_8WIRE_BIS接口的连线模式为**8**（八线模式）。

【视图】

ATM SHDSL_4WIRE接口视图/ATM SHDSL_4WIRE_BIS接口视图/ATM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[2**]：两线模式。

**[4-auto-enhanced**]：四线自动模式，系统首先以**4-enhanced**模式进行协商，如果检测到对端是**4-standard**模式，则本端自动切换成**4-standard**模式进行协商。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[4-enhanced**]：四线增强模式，四线中的一个线对先与对端协商，协商成功后，另一个线对再与对端进行协商。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[4-standard**]：四线标准模式，四线的两个线对必须同时开始进行协商，要求对端也为四线标准模式。

**[6**]：六线模式。

**[8**]：八线模式。

**[auto**]：自动模式，本端根据对端接口连线模式进行协商，最终协商的连线模式与对端配置一致。

【使用指导】

配置**shdsl wire**命令时，需要根据对端接口的设置选择正确连线模式。在无法确定对端接口连线模式的情况下，本端接口可以配置为**auto**自动模式与对端进行协商。

【举例】

\# 设置SHDSL_4WIRE ATM接口2/4/0工作在四线自动模式。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 shdsl wire 4-auto-enhanced

**ATM接口 \-- EFM接口配置命令 \-- display dsl configuration**

------------------------------------------------------------------------

**[display dsl configuration**]命令用来显示EFM接口的配置信息。

【命令】

**[display dsl configuration interface efm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface efm**]*interface-number*：显示指定EFM接口的配置信息。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 显示EFM接口2/4/0的配置信息。

\<Sysname\> display dsl configuration interface efm 2/4/0

Line parameter and mode configuration:

  Mode:           CPE

  Standard:       G.991.2

  Annex:          B

Wire type:      2

Line rate:      Auto Adaptive

Current margin: 2

SNEXT margin:   0

Psd mode:       Sym PSD

Actual handshake status:

  00: 0002 0000 0000 0000 0000 0000 0000 0000 0000 0000

  10: 0000 0008 0000 0000 0000 0000 0000 0000 0008 0000

  20: 0000 0000 0002 0002 0004 0010

Local handshake status:

  00: 0002 0001 0000 0000 0000 0000 0034 003f 003f 003f

  10: 003f 003f 0003 0034 003f 003f 003f 003f 003f 0003

  20: 0000 0000 0003 0003 000f 0010

Remote handshake status:

  00: 0002 0000 0000 0000 0000 0000 0030 003f 003f 003f

  10: 003f 000f 0000 0030 003f 003f 003f 003f 000f 0000

  20: 0000 0000 0003 0003 0004 0010

表1-10 display dsl configuration命令显示信息描述表

字段

描述

Mode

工作模式：CPE为用户端，CO为中心局端

Standard

所支持的标准规范：（此参数为预设值，用户不能修改）

·Auto：自适应方式（缺省情况标准值）

·G992.3：使用ADSL2（G992.3）标准

·G992.5：使用ADSL2+（G992.5）标准

·G992.1：使用G.DMT（G992.1）标准

·G992.2：使用G.Lite（G992.2）标准

·T1.413：使用T1.413标准

·G.SHDSL.bis：协商采用物理层标准是G.BIS标准

Annex

接口链路所采用的附加标准：

·A：Annex A标准

·B：Annex B标准

Wire type

连线类型，分为2线制和4线制

Current margin

当前容限量

SNEXT margin

最差情况的容限量

Line rate

线路速率

PSD mode

功率频谱密度方式，分为对称（Sym）和非对称方式（Asym）

Actual handshake status

实际的握手状态

Local handshake status

本端的握手状态

Remote handshake status

远端的握手状态

**ATM接口 \-- EFM接口配置命令 \-- display dsl status**

------------------------------------------------------------------------

**[display dsl status**]命令用来显示EFM接口的状态信息。

【命令】

**[display dsl status interface efm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface efm**]*interface-number*：显示指定EFM接口的状态信息。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 当接口状态为up时显示两线EFM接口的状态信息。

\<Sysname\> display dsl status interface efm 2/4/0

Operating Mode:CPE

DSL Mode:SHDSL Annex B

Configured Wire Type:2

Line A Statistics since last activation:

CRC:            0

LOSW Defect:    0

ES:             0

SES:            0

UAS:            0

TX EOC:         0

RX EOC:         0

Line A status:

Xcvr Op State:          Data Mode

Last Fail Op State:     0x00

Line Rate(Kbps):        2312

Wire Type:              2

SNR Margin(dB):         16.30

Loop Attenuation(dB):   0.00

RecvGain(dB):           6.07

TxPower(dBm):           9.50

Power Backoff:          enable

Power Backoff Level:    5

Tip/Ring Reversal:      Reversed

FrmOH Stat:             0x00

Rmt Encoder A:          0x0000016e

Rmt Encoder B:          0x00000331

Rmt NSF Cusdata:        0x0000

Rmt NSF CusID:          0x0000

Rmt Country Code:       0x00b5

Rmt Provider Code:      GSPN

Rmt Vendor Data:        0x12 0x34 0x56 0x78

                        0x12 0x34 0x56 0x78

\# 当接口状态为up时显示四线EFM接口的状态信息。

\<Sysname\> display dsl status interface efm 2/4/0

Operating Mode:CPE

DSL Mode:SHDSLAnnex B

Configured Wire Type:   4

Line A Statistics since last activation:

CRC:             0

LOS WDefect:     0

ES:              0

SES:             0

UAS:             0

TX EOC:          0

RX EOC:          0

Line A status:

Xcvr Op State:          Data Mode

Last Fail Op State:     0x00

Line Rate(Kbps):        2312

Wire Type:              4

SNR Margin(dB):         13.30

Loop Attenuation(dB):   0.00

RecvGain(dB):           5.86

TxPower(dBm):           9.50

Power Backoff:          enable

Power Backoff Level:    5

Tip/Ring Reversal:      Reversed

FrmOH Stat:             0x00

Rmt Encoder A:          0x0000016e

Rmt Encoder B:          0x00000331

Rmt NSF Cusdata:        0x0000

Rmt NSF CusID:          0x0000

Rmt Country Code:       0x00b5

Rmt Provider Code:      GSPN

Rmt Vendor Data:        0x12 0x34 0x56 0x78

                        0x12 0x34 0x56 0x78

Line B Statistics since last activation:

CRC:            1

LOSW Defect:    1

ES:             1

SES:            1

UAS:            0

TX EOC:         0

RX EOC:         0

Line B status:

Xcvr Op State:          Data Mode

Last Fail Op State:     0x00

Line Rate(Kbps):        2312

Wire Type:              4

SNR Margin(dB):         12.30

Loop Attenuation(dB):   0.00

RecvGain(dB):           5.28

TxPower(dBm):           9.50

Power Backoff:          enable

Power Backoff Level:    5

Tip/Ring Reversal:      Reversed

FrmOH Stat:             0x00

Rmt Encoder A:          0x0000016e

Rmt Encoder B:          0x00000331

Rmt NSF Cusdata:        0x0000

Rmt NSF CusID:          0x0000

Rmt Country Code:       0x00b5

Rmt Provider Code:      GSPN

Rmt Vendor Data:        0x12 0x34 0x56 0x78

                        0x12 0x34 0x56 0x78

表1-11 display dsl status命令显示信息描述表

字段

描述

Operating Mode

工作模式：CPE为用户端，CO为中心局端

DSL Mode

接口链路所采用的附加标准：

·A：Annex A标准

·B：Annex B标准

Configured Wire Type

配置连线类型，分为2线制和4线制

Line A Statistics since last activation

从激活时开始到现在A线对的统计信息

CRC

CRC错误数

LOSW Defect

LOSW（同步丢失）错误数

ES

每秒错误数

SES

每秒严重错误数

UAS

每秒不可用状态计数

TX EOC

发送ECO信源计数

RX EOC

接收ECO信源计数

Line A status

A线对状态

Xcvr Op State

收发器工作状态：

·Idle：空闲状态

·Data Mode：激活状态

·HandShaking：激活握手阶段

·Training：激活训练阶段

Last Fail Op State

上次协商失败收发器工作状态，可能的取值同上

Line Rate(Kbps)

协商线对速率

Wire Type

线数类型，可能的取值有2（2线制）、4（4线制）

SNR Margin(dB)

信噪比容限量

Loop Attenuation(dB)

环路衰减

RecvGain(dB)

接收增益

TxPower(dBm)

发送功率

Power Backoff

功率补偿状态

Power Backoff Level

功率补偿级别

Tip/Ring Reversal

Tip/Ring翻转状态

FrmOH Stat

帧溢出状态

Rmt Encoder A

远端译码器系数A

Rmt Encoder B

远端译码器系数B

Rmt NSF Cusdata

远端非标准格式用户数据

Rmt NSF CusID

远端非标准格式用户ID

Rmt Country Code

远端国家代码

Rmt Provider Code

远端芯片供应商代码

Rmt Vendor Data

远端制造商代码

**ATM接口 \-- EFM接口配置命令 \-- display dsl version**

------------------------------------------------------------------------

**[display dsl version**]命令用来显示EFM接口的版本信息和支持的能力。

【命令】

**[display dsl version interface efm** *interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface efm**]* interface-number*：显示指定EFM接口的版本信息和支持的能力。

【举例】

![说明](ATM接口命令.files/image003.png)

本命令的显示信息与具体芯片相关，请以设备的实际情况为准。

\# 显示EFM接口2/4/0上的版本信息和支持的能力。

\<Sysname\> display dsl version interface efm 2/4/0

DSL Line Type:          G.SHDSL

ATM SAR Device:         0x823614f1

ATM SAR Revision:       0x02

Chipset Vendor:         GSPN

Firmware Rel-Rev:       R2.3.1-0

DSP Version:            1

PCB Version:            0.0

CPLD Version:           0.0

Driver Version:         2.0

Hardware Version:       1.0

ITU G991.2 ANNEX A:     Supported

ITU G991.2 ANNEX B:     Supported

表1-12 display dsl version命令显示信息描述表

字段

描述

DSL Line Type

用户接入线的类型

ATM SAR Device

SAR芯片的标识

ATM SAR Revision

SAR芯片的修改标识

Chipset Vendor

DSL Chipsets的厂商标识

Firmware Rel-Rev

FirmWare的标识和版本信息

DSP Version

DSP版本

PCB Version

单板PCB的版本号

CPLD Version

逻辑器件的版本号

Driver Version

驱动软件的版本号

Hardware Version

硬件版本

ITU G991.2 ANNEX A，ITU G991.2 ANNEX B

接口支持的标准及其附加标准

**ATM接口 \-- EFM接口配置命令 \-- display interface efm**

------------------------------------------------------------------------

**[display interface efm**]命令用来显示EFM接口的相关信息。

【命令】

**[display interface** [ **efm** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定EFM接口的信息，interface-number表示EFM接口的编号。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**efm**参数，将显示设备支持的所有接口的相关信息。

·如果指定**efm**参数，不指定*interface-number*参数，将显示所有EFM接口的相关信息。

【举例】

\# 显示接口EFM2/4/0的详细信息。

\<Sysname\> display interface efm 2/4/0

EFM2/4/0

Current state: DOWN

Line protocol state: DOWN

Description: EFM2/4/0 Interface

Bandwidth: 20000kbps

Maximum Transmit Unit: 1500

Hold timer: 10 seconds

Internet protocol processing: disabled

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: b8af-67fa-10f0

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: b8af-67fa-10f0

2Wire-Shdsl Line, Operation State: DOWN_NOT_READY, Operating Mode: CO

Last link flapping: 6 hours 39 minutes 25 seconds

Last clearing of counters: Never

Last 300 seconds input rate: 0.00 bytes/sec, 0.00 packets/sec

Last 300 seconds output rate: 0.00 bytes/sec, 0.00 packets/sec

Input:

  0 packets, 0 bytes, 0 buffers

  0 errors, 0 crcs, 0 lens, 0 giants

  0 pads, 0 aborts, 0 timeouts

  0 overflows, 0 overruns, 0 no buffer

Output:

  0 packets, 0 bytes, 0 buffers

  0 errors, 0 overflows, 0 underruns

\# 显示接口EFM2/4/0的概要信息。

\<Sysname\> display interface efm 2/4/0 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

EFM2/4/0             UP   UP(s)    \--

\# 显示当前物理状态为down的EFM接口的信息以及down的原因。

\<Sysname\> display interface efm brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

EFM2/4/0             DOWN Not connected

表1-13 display interface efm命令显示信息描述表

字段

描述

EFM2/4/0

Current state

接口当前的物理状态和管理状态，可能的取值及含义如下：

·DOWN（Administratively）：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态，可能的状态及含义如下：

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

Description

接口的描述信息

Bandwidth

接口的期望带宽

Maximum Transmit Unit

接口的最大传输单元

Hold timer

轮询时间间隔

Internet protocol processing

网络层协议处理状况：（enabled/disabled）

IP Packet Frame Type

IP报文帧类型

IPv6 Packet Frame Type

IPv6报文帧类型

Hardware Address

接口的硬件地址

2Wire-Shdsl Line

线对采用的连线模式：

·2Wire-Shdsl：2线模式

·4Wire-Shdsl：4线模式

·6Wire-Shdsl：6线模式

·8Wire-Shdsl：8线模式

Operation State

线对的状态：

·DOWN_NOT_READY：线路处于DOWN，未就绪状态

·DOWN\_ READY：线路处于DOWN，就绪状态

·INITIALIZING：线路处于正在协商的状态

·UP_DATA_MODE：线路协商成功，处于数据模式

Operating Mode

线对的工作模式：

·CO：表示模式为局端模式

·CPE：表示模式为用户端模式

Last link flapping

接口最近一次物理状态改变到现在的时长。Never表示接口从设备启动后一直处于down状态（没有改变过）

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

Last 300 seconds input rate: 0.00 bytes/sec, 0.00 packets/sec

最近300秒钟的平均输入速率：bytes/sec表示平均每秒输入的字节数，packets/sec表示平均每秒输入的报文数

Last 300 seconds output rate: 0.00 bytes/sec, 0.00 packets/sec

最近300秒钟的平均输出速率：bytes/sec表示平均每秒输出的字节数， packets/sec表示平均每秒输出的报文数

Input:

  0 packets, 0 bytes, 0 buffers

  0 errors, 0 crcs, 0 lens, 0 giants

  0 pads, 0 aborts, 0 timeouts

  0 overflows, 0 overruns, 0 no buffer

·packets：接口收到的总报文数

·bytes：接口收到的总字节数

·buffers： 接口接收报文所使用缓冲区个数

·errors：在物理层检测时发现的错误报文数目

·crcs：CRC错误数

·lens： 接口接收到长度错误的报文个数

·giants：接口接收到长度大于规定长度的报文数目

·pads： 接口接收报文进行填充时发生的相关错误个数

·aborts：接收报文的异常错误

·timeouts：接口接收报文超时的个数

·overflows：接口接收报文时芯片FIFO溢出错误个数

·overruns：接收的报文速度大于转发处理能力导致无法处理的报文

·no buffer： 接口接收报文时因系统资源不足产生的相关错误

Output:

  0 packets, 0 bytes, 0 buffers

  0 errors, 0 overflows, 0 underruns

·packets：接口发送的总报文数

·bytes：接口发送的总字节数

·buffers：接口发送报文所使用的缓冲区个数

·errors：在物理层检测时发现的错误报文数目

·overflows：接口发送报文时芯片FIFO溢出错误个数

·underruns：因为接口读取内存的速度小于转发的速度而无法发送报文数目

Brief information on interface(s) under route mode

三层模式下（route）的接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

Protocol

接口数据链路层协议状态，取值可能为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口主IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

**ATM接口 \-- EFM接口配置命令 \-- interface efm**

------------------------------------------------------------------------

**[interface efm**]命令用来进入EFM接口或子接口视图。在进入子接口视图之前，如果指定的子接口不存在，则先创建子接口，再进入该子接口的视图。

**[undo interface efm**]命令用来删除EFM子接口。

【命令】

**[interface efm**[ { *interface-number* \| *interface-number.subnumber* }]]

**[undo interface efm** *interface-number.subnumber*]

【缺省情况】

不存在EFM子接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：EFM接口编号。

*[interface-number.subnumber*]：EFM子接口编号，其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为1～4094，但单个EFM主接口上最大只能创建1024个EFM子接口。

【举例】

\# 进入EFM接口2/4/0接口视图。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0

\# 创建EFM子接口EFM2/4/0.1并进入子接口视图。

\<Sysname\> system-view

Sysname interface efm 2/4/0.1

Sysname-EFM2/4/0.1

**ATM接口 \-- EFM接口配置命令 \-- shdsl annex**

------------------------------------------------------------------------

**[shdsl annex**]命令是用来配置EFM接口所支持的Annex标准。当两端标准不同，线路会难以激活。

**[undo shdsl annex**]命令用来恢复缺省情况。

【命令】

**[shdsl annex**[ { **a** \| **b** }]]

**[undo shdsl annex**]

【缺省情况】

支持的Annex标准为Annex b。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[a**]：支持的Annex标准为Annex a。

**[b**]：支持的Annex标准为Annex b。

【使用指导】

Annex a/b均是G.991.2的标准，Annex a主要在北美应用，Annex b主要在欧洲应用，其它地区网络要根据当地网络的不同，选择不同的标准，例如中国地区网络执行的标准类型为Annex b。

【举例】

\# 配置EFM接口2/4/0所支持的标准为Annex a。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0shdsl annex a

**ATM接口 \-- EFM接口配置命令 \-- shdsl capability**

------------------------------------------------------------------------

**[shdsl capability**]命令用来配置接口的协商能力。

**[undo shdsl capability**]命令用来恢复缺省情况。

【命令】

**[shdsl capability**[ { **auto** \| **g-shdsl** \| **g-shdsl-bis** }]]

**[undo shdsl capability**]

【缺省情况】

在CPE模式下，采用**auto**方式。

在CO模式下，采用**g-shdsl-bis**方式。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：自动选择与对端接口相同的协商能力（只在CPE模式下支持，在CO模式下不支持）。

**[g-shdsl**]：使用G.SHDSL。

**[g-shdsl-bis**]：使用G.SHDSL.bis。

【使用指导】

在CPE模式下支持g-shdsl和g-shdsl-bis以及auto。

在CO模式下支持g-shdsl和g-shdsl-bis，不支持auto。

在配置**shdsl mode**时，会自动恢复为各自模式下的缺省配置。

两端接口需要使用相同的协商能力，才能协商成功。

【举例】

\# 配置接口的协商能力为G.SHDSL。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0 shdsl capability g-shdsl

【相关命令】

·shdsl mode

**ATM接口 \-- EFM接口配置命令 \-- shdsl line-probing**

------------------------------------------------------------------------

**[shdsl line-probing enable**]命令用来开启SHDSL线路的探询功能。

**[undo shdsl line-probing enable**]命令用来关闭SHDSL线路的探询功能。

【命令】

**[shdsl line-probing enable**]

**[undo shdsl line-probing enable**]

【缺省情况】

线路的探询功能处于开启状态。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启探询功能后，在线路激活的过程中，系统将执行线路探询功能去协商最佳的线路速率；若关闭探询功能，系统会选择CPE和CO都支持的速率交集中的最大速率。这种方式因为跳过了线路速率的适配过程，减短了激活SHDSL线路的时间。

【举例】

\# 关闭SHDSL线路的探询功能。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0 undo shdsl line-probing enable

**ATM接口 \-- EFM接口配置命令 \-- shdsl mode**

------------------------------------------------------------------------

**[shdsl mode**]命令用来配置EFM接口的工作模式。

**[undo shdsl mode**]命令用来恢复缺省情况。

【命令】

**[shdsl mode**[ { **co** \| **cpe** }]]

**[undo shdsl mode**]

【缺省情况】

工作模式为CPE模式。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[co**]：配置为CO模式。

**[cpe**]：配置为CPE模式。

【使用指导】

两台设备直连时，必须把一端配置为CO模式，另一端配置成CPE模式。

【举例】

\# 配置EFM2/4/0工作在CO模式。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0 shdsl mode co

**ATM接口 \-- EFM接口配置命令 \-- shdsl pam**

------------------------------------------------------------------------

**[shdsl pam**]用来配置PAM Constellation。

**[undo shdsl pam**]用来恢复缺省情况。

【命令】

**[shdsl pam****16**[\| ]**32**[\| ]**auto**}

**[undo shdsl pam**]

【缺省情况】]

自动选择PAM。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[16**]：使用16 PAM Constellation。在16 PAM下，速率范围为192～3840，单位为kbps。

**[32**]：使用32 PAM Constellation。在32 PAM下，速率范围为768～5696，单位为kbps。

**[auto**]：根据线路两端的参数自动选择两端都支持的最好的PAM（32 PAM比16 PAM好）。

【使用指导】

PAM是数字线路的一种编码模式，叫脉冲调制模式，Constellation用来形容PAM编码方式像星座。本命令用于配置PHY芯片的数字信号调制模式。

当接口的协商能力为G.SHDSL时，不支持32 PAM Constellation。

【举例】

\# 配置EFM2/4/0使用16 PAM Constellation。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0 shdsl pam 16

【相关命令】

·**shdsl capability**

**ATM接口 \-- EFM接口配置命令 \-- shdsl pbo**

------------------------------------------------------------------------

**[shdsl pbo**]命令用来调整发送功率。

**[undo shdsl pbo**]命令用来恢复缺省情况。

【命令】

**[shdsl pbo** }

**[undo shdsl pbo**]

【缺省情况】]

自动调整发送功率。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：自动调整发送功率。

*[value*]：发送功率调整值，取值范围为0～31，单位为dB。

【使用指导】

正常情况下，接口会根据线路噪声情况，自动调整发送功率，以保证可以获得合适的信噪比。当线路的噪声已知的情况下，或者自动调整不准确的时候，可以通过此命令行手动调整发射功率。

【举例】

\# 配置EFM2/4/0接口的发送功率调整值为20db。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0 shdsl pbo 20

**ATM接口 \-- EFM接口配置命令 \-- shdsl psd**

------------------------------------------------------------------------

**[shdsl psd**]命令用来配置EFM接口的功率频谱密度模式。

**[undo shdsl psd**]命令用来恢复缺省情况。

【命令】

**[shdsl psd **[{ **asymmetry** \| **symmetry** }]]

**[undo shdsl psd**]

【缺省情况】

功率频谱密度模式为对称模式。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[asymmetry**]：功率频谱密度模式为非对称模式。

**[symmetry**]：功率频谱密度模式为对称模式。

【使用指导】

PSD（Power Spectral Density，功率频谱密度）指发射功率在最高准位时，一脉冲或一序列脉冲，其单位带宽的总输出能量除以总脉冲持续时间。

【举例】

\# 配置EFM2/4/0的功率频谱密度模式为非对称模式。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0 shdsl psd asymmetry

**ATM接口 \-- EFM接口配置命令 \-- shdsl rate**

------------------------------------------------------------------------

**[shdsl rate**]命令用来配置EFM接口单线对的速率。

**[undo shdsl rate**]命令用来恢复缺省情况。

【命令】

**[shdsl rate**[ { *rate* \| **auto** }]]

**[undo shdsl rate**]

【缺省情况】

EFM G.SHDSL、EFM SHDSL_4WIRE_BIS、EFM SHDSL 8WIRE_BIS接口的单线对速率为自动协商方式。

EFM SHDSL_4WIRE接口，在两线模式下单线对速率为自动协商方式，在非两线模式下的单线对速率为2312kbit/s（即四线接口速率为4624kbit/s）。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rate*]：EFM接口的单线对速率最大值。对于EFM G.SHDSL接口和EFM SHDSL_4WIRE接口，取值范围为192～2312，单位为kbit/s；对于EFM SDHSL_4WIRE_BIS接口和EFM SHDSL_8WIRE_BIS接口，取值范围为192～5696，单位为kbit/s。

**[auto**]：为自动协商方式。

【使用指导】

在实际使用中，最大下行速率还会受局端设备的限制和线路条件的限制，有可能达不到设置的值。如果将速率设置成自动协商方式，在激活过程中两端会根据当前的线路状况协商出一个合适的速率；如果CPE端和CO端设置成固定速率，CPE端和CO端将进行速率协商，若无法满足二者之中较低的速率要求的时候，线路无法被激活。

需要注意的是：

·四线（即双线对）的EFM接口的速率为单线对速率的两倍。例如设置单线对速率为2312kbit/s，则四线接口的速率为4624kbit/s。

·四线的EFM接口的单线对速率无法配置成auto方式，因为四线的接口无法进行速率的协商。

【举例】

\# 配置EFM2/4/0的单线对速率为自动协商方式。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0 shdsl rate auto

**ATM接口 \-- EFM接口配置命令 \-- shdsl snr-margin**

------------------------------------------------------------------------

**[shdsl snr-margin**]命令用来配置SNR的目标容限量。

**[undo shdsl snr-margin**]命令用来恢复缺省情况。

【命令】

**[shdsl snr-margin ** **current** *current-margin-value* ]  **snext** *snext-margin-value*

**[undo shdsl snr-margin**]

【缺省情况】

线路协商时current-margin-value为2，snext-margin-value为0。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[current*** current-margin-value*]：当前信噪比容限量。*current-margin-value*的取值范围为0～10，缺省值为2。SHDSL线路在训练的时候以线路信噪比门限加上*current-margin-value*进行训练。配置比较大的*current-margin-value*可以使得协商成功的链路更加稳定，抗噪能力更强。

**[snext ***snext-margin-value*]：最差的信噪比容限量。*snext-margin-value*的取值范围为0～10，缺省值为0。SHDSL线路在训练的时候以最差信噪比门限加上*snext-margin-value*进行训练。设置比较大的*snext-margin-value*可以使得协商成功的链路更加稳定，抗噪能力更强。

【使用指导】

配置信噪比容限量会影响线路支持的最大速率。因此在线路比较好的情况下，可以配置较小的信噪比容限量，以获得更高的速率。但是，在线路存在较多的噪声的情况下，配置过小的当前信噪比容限量会造成线路容易掉线。

【举例】

\# 配置接口EFM2/4/0的当前信噪比容限量为5。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0shdsl snr-margin current 5

**ATM接口 \-- EFM接口配置命令 \-- shdsl wire**

------------------------------------------------------------------------

**[shdsl wire**]命令用来配置EFM接口的连线模式。

**[undo shdsl wire**]命令用来恢复缺省情况。

【命令】

在EFM SHDSL_4WIRE、EFM SHDSL_4WIRE_BIS接口视图下：

**[shdsl wire**[ { **2** \| **4-auto-enhanced** \| **4-enhanced** \| **4-standard** }]]

**[undo shdsl wire**]

在EFM SHDSL_8WIRE_BIS接口视图下：

**[shdsl wire**[ { **2** \| **4-enhanced** \| **4-standard** \| **6** \| **8** \| **auto** }]]

**[undo shdsl wire**]

【缺省情况】

EFM SHDSL_4WIRE接口的连线模式为**4-enhanced**（四线增强模式）。

EFM SHDSL 4WIRE_BIS接口的连线模式为**4-standard**（四线标准模式）。

EFM SHDSL_8WIRE_BIS接口的连线模式为**8**（八线模式）。

【视图】

EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[2**]：两线模式。

**[4-auto-enhanced**]：四线自动模式，系统首先以**4-enhanced**模式进行协商，如果检测到对端是**4-standard**模式，则本端自动切换成**4-standard**模式进行协商。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[4-enhanced**]：四线增强模式，四线中的一个线对先与对端协商，协商成功后，另一个线对再与对端进行协商。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[4-standard**]：四线标准模式，四线的两个线对必须同时开始进行协商，要求对端也为四线标准模式。

**[6**]：六线模式。

**[8**]：八线模式。

**[auto**]：自动模式，本端根据对端接口连线模式进行协商，最终协商的连线模式与对端配置一致。

【使用指导】

配置**shdsl wire**命令时，需要根据对端接口的配置选择正确连线模式。在无法确定对端接口连线模式的情况下，本端接口可以配置为**auto**自动模式与对端进行协商。

【举例】

\# 配置四线EFM2/4/0工作在四线自动模式。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0shdsl wire 4-auto-enhanced

**ATM接口 \-- EFM接口配置命令 \-- sub-interface rate-statistic**

------------------------------------------------------------------------

![说明](ATM接口命令.files/image004.jpg)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·开启本功能后可能需要耗费大量系统资源，请谨慎使用。

**[sub-interface rate-statistic**]命令用来开启EFM子接口的速率统计功能。

**[undo sub-interface rate-statistic**]命令用来关闭EFM子接口的速率统计功能。

【命令】

**[sub-interface rate-statistic**]

**[undo sub-interface rate-statistic**]

【缺省情况】

EFM子接口的速率统计功能处于关闭状态。

【视图】

EFM G.SHDSL接口视图/EFM SHDSL_4WIRE接口视图/EFM SHDSL_4WIRE_BIS接口视图/EFM SHDSL_8WIRE_BIS接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启接口EFM2/4/0的子接口速率统计功能。

\<Sysname\> system-view

Sysname interface efm 2/4/0

Sysname-EFM2/4/0sub-interface rate-statistic

