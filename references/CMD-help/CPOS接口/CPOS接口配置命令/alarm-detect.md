<!-- CMD-INDEX
  alarm-detect                        | CPOS接口视图         | L61
  clock                               | CPOS接口视图         | L127
  controller cpos                     | 系统视图             | L181
  default                             | CPOS接口视图         | L215
  description                         | CPOS接口视图         | L251
  display controller cpos             | 任意视图             | L293
  display controller cpos e1          | 任意视图             | L503
  display controller cpos e3          | 任意视图             | L609
  display controller cpos t1          | 任意视图             | L755
  display controller cpos t3          | 任意视图             | L861
  e1 channel-set                      | CPOS接口视图         | L913
  e1 clock                            | CPOS接口视图         | L977
  e1 flag                             | CPOS接口视图         | L1029
  e1 frame-format                     | CPOS接口视图         | L1087
  e1 loopback                         | CPOS接口视图         | L1133
  e1 shutdown                         | CPOS接口视图         | L1195
  e1 unframed                         | CPOS接口视图         | L1241
  e3 clock                            | CPOS接口视图         | L1291
  e3 framed                           | CPOS接口视图         | L1347
  e3 loopback                         | CPOS接口视图         | L1393
  e3 national-bit                     | CPOS接口视图         | L1457
  e3 shutdown                         | CPOS接口视图         | L1507
  fe3                                 | CPOS接口视图         | L1549
  flag                                |                  | L1611
  flag vc-3                           | ]                | L1693
  flag vc-4                           | ]                | L1755
  frame-format                        | CPOS接口视图         | L1817
  ft3                                 | CPOS接口视图         | L1861
  link-delay                          | CPOS接口视图         | L1929
  loopback                            | CPOS接口视图         | L1979
  multiplex mode                      | CPOS接口视图         | L2029
  oc-12                               | 2.5Gbps高速CPOS接口视图 | L2091
  oc-3                                | 622Mbps高速CPOS接口视图/622Mbps通道视图 | L2143
  reset counters controller cpos      | 用户视图             | L2209
  shutdown                            | CPOS接口视图         | L2253
  t1 channel-set                      | CPOS接口视图         | L2295
  t1 clock                            | CPOS接口视图         | L2359
  t1 flag                             | CPOS接口视图         | L2411
  t1 frame-format                     | CPOS接口视图         | L2469
  t1 loopback                         | CPOS接口视图         | L2515
  t1 shutdown                         | CPOS接口视图         | L2571
  t1 unframed                         | CPOS接口视图         | L2617
  t3 alarm                            | CPOS接口视图         | L2667
  t3 bert                             | CPOS接口视图         | L2737
  t3 clock                            | CPOS接口视图         | L2799
  t3 feac                             | CPOS接口视图         | L2855
  t3 framed                           | CPOS接口视图         | L2931
  t3 frame-format                     | CPOS接口视图         | L2977
  t3 loopback                         | CPOS接口视图         | L3023
  t3 mdl                              | CPOS接口视图         | L3079
  t3 shutdown                         | CPOS接口视图         | L3163
  threshold                           | CPOS接口视图         | L3205
  using e3                            | CPOS接口视图/155Mbps通道视图 | L3261
  using oc-12/using oc-12c            | 622Mbps高速CPOS接口视图/622Mbps通道视图 | L3327
  using oc-3/using oc-3c              | 155Mbps高速CPOS接口视图/155Mbps通道视图 | L3397
  using oc-48/using oc-48c            | 2.5Gbps高速CPOS接口视图 | L3467
  using t3                            | CPOS接口视图/155Mbps通道视图 | L3521
-->

**CPOS接口 \-- CPOS接口配置命令 \-- alarm-detect**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[alarm-detect**]命令用来设置当前接口的告警联动动作。

**[undo alarm-detect**]命令用来取消告警联动动作。

【命令】

**[alarm-detect**[ { **rdi** \| **sd** \| **sf** } **action** **link-down**]]

**[undo alarm-detect**[ { **rdi** \| **sd** \| **sf** }]]

【缺省情况】

接口不执行任何告警联动动作。

【视图】

CPOS接口视图

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

\# 配置当CPOS2/4/0接口检测到SD告警时，自动将接口的物理状态设置为down。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 alarm-detect sd action link-down

【相关命令】

·**threshold**

**CPOS接口 \-- CPOS接口配置命令 \-- clock**

------------------------------------------------------------------------

**[clock**]命令用来设置CPOS接口的时钟模式。

**[undo clock**]命令用来恢复缺省情况。

【命令】

**[clock**[ { **master** \| **slave** }]]

**[undo clock**]

【缺省情况】

CPOS接口的时钟模式为从时钟模式（**slave**）。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[master**]：设置CPOS接口的时钟模式为主时钟模式。

**[slave**]：设置CPOS接口的时钟模式为从时钟模式。

【使用指导】

CPOS接口支持两种时钟模式：

·**master**：主时钟模式，使用内部时钟信号；

·**slave**：从时钟模式，使用线路提供的时钟信号。

与SONET/SDH设备相连时，由于SONET/SDH网络的时钟精度高于CPOS本身内部时钟源的精度，应配置CPOS使用从时钟模式。如果CPOS接口之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。

【举例】

\# 设置CPOS接口2/4/0使用主时钟模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 clock master

**CPOS接口 \-- CPOS接口配置命令 \-- controller cpos**

------------------------------------------------------------------------

**[controller cpos**]命令用来进入CPOS接口视图。

【命令】

**[controller cpos** *cpos-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cpos-number*]：CPOS接口的编号。

【举例】

\# 进入CPOS接口2/4/0的接口视图。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0

**CPOS接口 \-- CPOS接口配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将CPOS接口2/4/0恢复为缺省配置。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 default

**CPOS接口 \-- CPOS接口配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：Cpos2/4/0 Interface。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置CPOS接口2/4/0的描述信息为"CPOS-interface"。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 description CPOS-interface

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos**

------------------------------------------------------------------------

**[display controller cpos**]命令用来显示CPOS物理接口状态信息，以及再生段、复用段和高阶通道的告警及错误信息。

【命令】

**[display controller cpos** [ *cpos-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[cpos-number*]：CPOS接口的编号。如果不指定CPOS接口的编号，则显示所有CPOS接口的所有通道信息。

【使用指导】

显示信息中可能出现的错误类型如 表1-1(?-790475304#_Ref196800432)所示。

表1-1 display controller cpos命令可能出现的错误类型

字段

描述

FRED

Receive Loss of Basic Frame Alignment，接收到基本帧失位。也可以认为是收到有红色告警错误的帧

COFA

Change of Frame Alignment，帧对齐改变

SEF

Severely Errored Frame，严重错帧，连续4个帧同步错误将产生一个SEF

FERR

Framing Bit Error，指有Ft/Fs/FPS/FAS错误的帧

CERR

CRC Error，循环冗余校验错

FEBE

Far End Block Error，远端块错。这种错误只有在E1通道采用CRC4的帧格式时才可能出现。

BERR

PRBS Bit Error（随机码测试位错，只用于测试）

BIP

Bit-Interleaved Parity，比特交叉奇偶校验

REI

Remote Error Indication，远端错误指示

在上表中，前三种错误（FRED、COFA、SEF）统称为Alarm Error，简写为AERR。

相关配置可参考命令**display controller cpos e1**和**display controller cpos t1**。

【举例】

\# 查看CPOS接口2/4/0的所有通道信息。

\<Sysname\> display controller cpos 2/4/0

Cpos2/4/0 current state: DOWN

Description : Cpos2/4/0 Interface

Frame-format SDH,multiplex AU-4,clock master,loopback none

SD threshold: 6, SF threshold: 3

Optical:Absent

Regenerator section:

  Tx: J0:\"\"  (HEX: )

Rx: J0:\"\"  (HEX: )

  Alarm: LOS  LOF  OOF

  Error:  0 RS_BIP

Multiplex section:

  Alarm: MS_AIS  MS_SF  MS_SD

  Error:  0 MS_BIP , 0 MS_REI

Higher order Path (VC-4-1):

  Tx: J1:\"\", C2:0x02, S1S0:0x02

  Rx: J1:\"\", C2:0x6d, S1S0:0x02

  Alarm:   HP_TIU  HP_RDI  HP_ERDI  HP_PLM

  Error:  0 HP_BIP, 0 HP_REI, 0 HP_PJE, 0 HP_NJE

CT1 1 is down

  Frame-format: ESF,  clock: slave,  loopback: none

CT1 2 is down

  Frame-format: ESF,  clock: slave,  loopback: none

CT1 3 is down

  Frame-format: ESF,  clock: slave,  loopback: none

（此处省略部分T1通道的显示信息）

CT1 83 is down

  Frame-format: ESF,  clock: slave,  loopback: none

CT1 84 is down

  Frame-format: ESF,  clock: slave,  loopback: none

表1-2 display controller cpos命令显示信息描述表

字段

描述

Cpos2/4/0 current state

CPOS接口当前的物理状态

Description

接口的描述信息

Frame-format SDH, multiplex AU-4, clock master, loopback none

CPOS接口的物理层信息：帧格式为SDH、采用AU-4的复用路径、主时钟模式（使用内部时钟信号）、没有使能环回

SD threshold: 6 , SF threshold: 3

CPOS接口的SD（信号衰减）和SF（信号失败）的门限值

Optical:

传输介质的模块

Regenerator section

再生段的告警和错误统计

Tx: J0

发送的开销字节

Rx: J0

接收的开销字节

Alarm

对应支路的告警统计

Error

错误统计

Multiplex section

复用段的告警和错误统计

Higher order Path(VC-4-1)

高阶通道的告警和错误统计。VC-4-1表示采用AU-4的复用路径，只有一个高阶通道VC-4

CT1 1 is down

T1通道1当前的物理状态为Down

Frame-format: ESF,  clock: slave,  loopback: none

T1通道的物理层信息：帧格式为ESF、从时钟模式、没有使能环回

【相关命令】

·**display controller cpos**** e1**

·**display controller cpos**** t1**

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos e1**

------------------------------------------------------------------------

**[display controller cpos e1**]命令用来显示指定CPOS接口的E1通道的状态信息。

【命令】

**[display controller cpos ***cpos-number*]**e1***e1-number*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[cpos-number*]：显示指定接口编号的CPOS接口的E1通道的物理层配置信息。

*[e1-number*]：显示指定E1通道号的CPOS接口的E1通道的物理层配置信息，*e1-number*取值范围为1～63。

【使用指导】

与**display controller cpos**命令相比，本命令可以显示对应的低阶通道的错误和告警信息以及E1帧的错误和告警信息。

【举例】

\# 查看CPOS接口2/4/0的1号E1通道的状态信息。

\<Sysname\> display controller cpos 2/4/0 e1 1

Cpos2/4/0 current state: DOWN

Description: Cpos2/4/0 Interface

Lower order path:

  TxFlag: J2: \"\"    LP-C2: 2

  RxFlag: J2: \"\"    LP-C2: 7

  Alarm:  LP-AIS  LP-RDI  LP-RFI  LP-C2-Mismatched  LP-J2-Unstable

  Error:  1164 BIP2,  2047 FEBE

CE1  1 (1-1-1-1) is down

  Frame-format: NO-CRC4,  clock: slave,  loopback: none

  Alarm:  AIS  LFA  Red

  Error:  0 Fer

表1-3 display controller cpos e1命令显示信息描述表

主要字段

描述

Cpos2/4/0 current state

CPOS接口当前的物理状态

Description

接口的描述信息

Lower order path

E1低阶通道的告警和错误统计

TxFlag

发送的开销字节

RxFlag

接收的开销字节

当收到的J2为不可见字符时，显示为：RxFlag: J2: unknow

Alarm

对应支路的告警统计

Error

错误统计

CE1 1 (1-1-1-1) is down

E1通道当前的物理状态为down，1-1-1-1依次表示此E1通道所属的VC-4编号、TUG-3编号、TUG-2编号和TU-12编号

Frame-format: NO-CRC4,  clock: slave,  loopback: none

E1通道的物理层信息：帧格式为no-CRC4，从时钟模式、没有使能环回

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos e3**

------------------------------------------------------------------------

**[display controller cpos e3**]命令用来显示指定CPOS接口的E3通道的状态信息。

【命令】

**[display controller cpos ***cpos-number*]**e3***e3-number*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[cpos-number*]：CPOS接口编号。

*[e3-number*]：CPOS接口的E3通道号，取值范围为1～3。

【使用指导】

与**display controller cpos**命令相比，本命令可以显示对应的低阶通道的错误和告警信息以及E3帧的错误和告警信息。显示信息中可能出现的错误类型如[表]1-4(?1374262063#_Ref194484615)所示。

表1-4 display controller cpos e3/t3命令可能出现的错误类型

字段

描述

OOF

Out Of Frame，接收到基本帧失位，也就是收到E3/T3帧定位比特出错

LOS

Loss Of Signal，信号丢失，检测到输入信号丢失产生的

LOF

Loss Of Frame，帧丢失，连续多次检测到OOF时产生的。

AIS

Alarm Indication Signal，告警指示信号，本端检测到LOS等严重告警时产生，并会传到下游，因此它也可能是上游设备传来的

RAI

Remote Alarm Indication，远端告警指示，是下游设备检测到告警传来的

MS_AIS

Multiplex  Section Alarm Indication Signal，复用段告警指示信号(AIS)

FERR

Framing Bit Error Event，帧定位比特错误计数

LCV

Line code Violation，线路编码不符HDB3（E3）或B3ZS（T3）的计数

PERR

Parity Error Event，奇偶校验错误计数，T3帧P1和P2比特不等产生，只用于T3

FEBE

Far Error Block Event，远端错误块计数，下游传上来的，只用于T3

HCS

Header Check Sequence，HDLC帧CRC校验错误计数

【举例】

\# 查看CPOS接口2/4/0的1号E3通道的状态信息。

\<Sysname\> display controller cpos 2/4/0 e3 1

Cpos2/4/0 current state: UP

Description: Cpos2/4/0 Interface

E3 1: up

  Frame-format: G.751, Clock: slave, Loopback: none

  national-bit: 1

  Alarm: NONE

  Error: 0 FERR, 0 LCV, 0 HCS

表1-5 display controller cpos e3/t3命令显示信息描述表

字段

描述

Cpos2/4/0 current state

CPOS接口当前的物理状态

Description

接口的描述信息

E3 1

E3通道的状态

Frame-format

E3帧格式

Clock

E3通道时钟模式

Loopback

E3通道的环回模式

national-bit

E3国际（内）通信码值

Alarm

E3通道告警

Error

E3通道错误计数

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos t1**

------------------------------------------------------------------------

**[display controller cpos t1**]命令用来显示指定CPOS接口的T1通道的状态信息。

【命令】

**[display controller cpos ***cpos-number* **t1** *t1-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[cpos-number*]：显示指定接口编号的CPOS接口的T1通道的物理层配置信息。

*[t1-number*]：显示指定T1通道号的CPOS接口的T1通道的物理层配置信息，取值范围为1～84。

【使用指导】

与**display controller cpos**命令相比，本命令可以显示对应的低阶通道的错误和告警信息以及T1帧的错误和告警信息。

【举例】

\# 查看CPOS接口2/4/0的1号T1通道的状态信息。

\<Sysname\> display controller cpos 2/4/0 t1 1

Cpos2/4/0 current state: DOWN

Description : Cpos2/4/0 Interface

Lower order path:

  TxFlag: J2: \"\"    LP-C2: 2

  RxFlag: J2: \"\"    LP-C2: 7

  Alarm:  LP-AIS  LP-RDI  LP-RFI  LP-C2-Mismatched  LP-J2-Unstable

  Error:  1080 BIP2,  2047 FEBE

CT1  1 (1-1-1-1) is down

  Frame-format: ESF,  clock: slave,  loopback: none

  Alarm:  AIS  LFA  Red

  Error:  0 Bit Error,  0 Fer,  0 OOF

表1-6 display controller cpos t1命令显示信息描述表

主要字段

描述

Cpos2/4/0 current state

CPOS接口当前的物理状态

Description

接口的描述信息

Lower order path

低阶通道的告警和错误统计

TxFlag:

发送的开销字节

RxFlag:

接收的开销字节

当收到的J2为不可见字符时，显示为：RxFlag: J2: unknow

Alarm

对应支路的告警统计

Error

错误统计

CT1  1 (1-1-1-1) is down

T1通道1当前的物理状态为down，1-1-1-1依次表示此T1通道所属的VC-3编号、TUG-3编号、TUG-2编号和TU-11编号

Frame-format: ESF,  clock: slave,  loopback: nonet

T1通道的物理层信息：帧格式为ESF、从时钟模式、没有使能环回

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos t3**

------------------------------------------------------------------------

**[display controller cpos t3**]命令用来显示指定CPOS接口的T3通道的状态信息。

【命令】

**[display controller** **cpos** *cpos-number* **t3** *t3-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[cpos-number*]：CPOS接口编号。

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

【使用指导】

与**display controller cpos**命令相比，本命令可以显示对应的低阶通道的错误和告警信息以及T3帧的错误和告警信息，具体告警如[表]1-4(?1374262063#_Ref194484615)所示。

【举例】

\# 查看CPOS接口2/4/0的1号T3通道的状态信息，状态信息含义如[表]1-5(?1374262063#_Ref194484623)所示。

\<Sysname\> display controller cpos 2/4/0 t3 1

Cpos2/4/0 current state: UP

Description: Cpos2/4/0 Interface

T3 1: down

  Frame-format: C-bit ,Clock: slave ,Loopback: none

  Alarm: NONE

  Error: 0 FERR, 0 LCV, 0 PERR, 0 FEBE, 0 PARITY_P, 0 HCS

**CPOS接口 \-- CPOS接口配置命令 \-- e1 channel-set**

------------------------------------------------------------------------

**[e1 channel-set**]命令用来对E1通道的时隙进行捆绑。

**[undo e1 channel-set**]命令用来取消指定的捆绑。

【命令】

**[e1** *e1-number* **channel-set** *set-number* **timeslot-list** *range*]

**[undo e1** *e1-number* **channel-set** *set-number*]

【缺省情况】

E1不进行通道化。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e1-number*]：CPOS接口的E1通道号，取值范围为1～63。

*[set-number*]：捆绑集的编号，取值范围为0～30。

**[timeslot-list*** range*]：用于捆绑的时隙列表，时隙编号的取值范围为1～31。在指定捆绑的时隙时，可以用*number*的形式指定单个时隙，也可以用*number1*-*number2*的形式指定一个范围内的时隙，还可以使用*number1*，*number2*-*number3*的形式，同时指定多个时隙。

【使用指导】

当CPOS接口的E1应用在通道化模式（Channelized）时，除时隙0用于同步外，其它31个时隙可任意捆绑为一个或多个串口。

捆绑形成的串口编号形式为"接口编号/通道号:channel-set号"。

【举例】

\# 对E1通道63进行捆绑。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e1 63 channel-set 1 timeslot-list 1-31

\# 进入捆绑后形成的串口的视图。

Sysname-Cpos2/4/0 quit

Sysname interface serial 2/4/0/63:1

Sysname-Serial2/4/0/63:1

【相关命令】

·**e1 unframed**

**CPOS接口 \-- CPOS接口配置命令 \-- e1 clock**

------------------------------------------------------------------------

**[e1 clock**]命令用来设置E1通道的时钟模式。

**[undo e1 clock**]命令用来恢复缺省情况。

【命令】

**[e1**[ *e1-number* **clock** { **master** \| **slave** }]]

**[undo e1** *e1-number* **clock**]

【缺省情况】

E1通道的时钟模式为从时钟模式（**slave**）。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e1-number*]：CPOS接口的E1通道号，取值范围为1～63。

**[master**]：设置E1通道的时钟模式为主时钟模式。

**[slave**]：设置E1通道的时钟模式为从时钟模式。

【使用指导】

可以为不同的E1通道单独配置时钟模式，使用主时钟模式还是从时钟模式应根据连接的设备确定。例如，与SONET/SDH设备连接时，应使用从时钟模式，而如果是设备之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。

需要注意的是，同一CPOS物理接口的不同E1通道的时钟模式是相互独立的。

【举例】

\# 设置E1通道1使用主时钟模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e1 1 clock master

**CPOS接口 \-- CPOS接口配置命令 \-- e1 flag**

------------------------------------------------------------------------

**[e1 flag**]命令用来设置E1通道开销。

**[undo e1 flag**]命令用来恢复缺省情况。

【命令】

**[e1***e1-number* **flag** **c2** *c2-value*]

**[undo e1 **]*e1-number* **flag** **c2**

**[e1**]*****e1-number*[ **flag** **j2** { **sdh** \| **sonet** } *j2-string*]

**[undo e1 **]*e1-number*[ **flag** **j2** { **sdh** \| **sonet** }]

【缺省情况】

**[c2**]取值为02（十六进制），**j2**循环发送空字符""。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e1-number*]：CPOS接口的E1通道号，取值范围为1～63。

**[c2**]：低阶通道信号标签字节。

*[c2-value*]：c2字节的开销的值，取值范围为0～7。协议不支持该值为5。

**[j2**]：低阶通道踪迹字节J2。

**[sdh**]：SDH格式的跟踪字节。

**[sonet**]：SONET格式的跟踪字节。

*[j2-string*]：踪迹字节，对于SDH格式取值范围为1～15个字符，对于SONET格式取值范围为1～62个字符。

【举例】

\# CPOS接口下配置E1通道3的c2开销为0x7。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e1 3 flag c2 7

**CPOS接口 \-- CPOS接口配置命令 \-- e1 frame-format**

------------------------------------------------------------------------

**[e1 frame-format**]命令用来设置E1通道的帧格式。

**[undo e1 frame-format**]命令用来恢复缺省情况。

【命令】

**[e1 **]*e1-number*** frame-format **[{ **crc4** \| **no-crc4** }]

**[undo**] **e1** *e1-number* **frame-format**

【缺省情况】

E1通道的帧格式为**no-crc4**。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e1-number*]：CPOS接口的E1通道号，取值范围为1～63。

**[crc4**]：帧格式为CRC4。

**[no-crc4**]：帧格式为no-CRC4。

【举例】

\# 设置E1通道1使用带CRC4检验的帧格式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e1 1 frame-format crc4

**CPOS接口 \-- CPOS接口配置命令 \-- e1 loopback**

------------------------------------------------------------------------

**[e1 loopback**]命令用来设置E1通道的环回模式。

**[undo e1 loopback**]命令用来取消环回。

【命令】

**[e1**[ *e1-number* **loopback** { **local** \| **payload** \| **remote** }]]

**[undo e1** *e1-number* **loopback**]

【缺省情况】

E1通道不进行任何形式的环回。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e1-number*]：CPOS接口的E1通道号，取值范围为1～63。

**[local**]：使能E1通道对内自环。

**[payload**]：使能E1通道对外载荷环回。

**[remote**]：使能E1通道对外远端环回。

【使用指导】

E1通道提供丰富的环回功能，可用于不同层次的测试。

·在对内自环模式下，发端的数据直接被环回到收端。

·在对外载荷环回模式下，收端接收的数据经过E1成帧器，生成载荷后再进行环回。

·在对外远端环回模式下，收端接收的数据不经过E1成帧器，未生成载荷即进行环回。

【举例】

\# 设置E1通道1进行对外载荷环回。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e1 1 loopback payload

【相关命令】

·**display controller cpos e1**

**CPOS接口 \-- CPOS接口配置命令 \-- e1 shutdown**

------------------------------------------------------------------------

**[e1 shutdown**]命令用来关闭E1通道。

**[undo e1 shutdown**]命令用来打开E1通道。

【命令】

**[e1 ***e1-number ***shutdown**]

**[undo e1 ***e1-number ***shutdown**]

【缺省情况】

E1通道处于打开状态。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e1-number*]：CPOS接口的E1通道号，取值范围为1～63。

【使用指导】

关闭E1通道后，如果有捆绑形成的串口，则串口也被关闭。

【举例】

\# 关闭E1通道1。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e1 1 shutdown

**CPOS接口 \-- CPOS接口配置命令 \-- e1 unframed**

------------------------------------------------------------------------

**[e1 unframed**]命令用来设置CPOS接口的E1工作在非成帧模式。

**[undo e1 unframed**]命令用来恢复缺省情况。

【命令】

**[e1** *e1-number* **unframed**]

**[undo e1** *e1-number* **unframed**]

【缺省情况】

E1工作在成帧模式。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e1-number*]：CPOS接口的E1通道号，取值范围为1～63。

【使用指导】

在目前的实现中，CPOS通道化生成的E1支持净通道（clear channel，又称为非成帧模式，unframed）和通道（channelized，又称为成帧模式）两种工作模式。

·在非成帧模式下，E1通道不分时隙，形成一个速率为2.048Mbps的串口，名称为Serial接口编号/通道号:0。

·在成帧模式下，E1通道除时隙0以外的31个时隙可以任意捆绑为串口使用。

【举例】

\# 将CPOS接口2/4/0的第3个E1通道设置为非成帧模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e1 3 unframed

**CPOS接口 \-- CPOS接口配置命令 \-- e3 clock**

------------------------------------------------------------------------

**[e3 clock**]命令用来配置E3通道的时钟模式。

**[undo e3 clock**]命令用来恢复缺省情况。

【命令】

**[e3**[ *e3-number* **clock** { **master** \| **slave** }]]

**[undo e3** *e3-number* **clock**]

【缺省情况】

E3通道的时钟模式为从时钟模式（**slave**）。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e3-number*]：CPOS接口的E3通道号，取值范围为1～3。

**[master**]：设置E3通道的时钟模式为主时钟模式。

**[slave**]：设置E3通道的时钟模式为从时钟模式。

【使用指导】

可以为不同的E3通道单独配置时钟模式，使用主时钟模式还是从时钟模式应根据连接的设备确定。例如，与SONET/SDH设备连接时，应使用从时钟模式，而如果是设备之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。

![说明](CPOS接口命令.files/image003.png)

·在同一CPOS物理接口的不同E3通道的时钟模式是相互独立。

·建议将全局下**clock**时钟模式和E3通道的时钟模式配置一致。

【举例】

\# 设置E3通道1使用主时钟模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e3 1 clock master

**CPOS接口 \-- CPOS接口配置命令 \-- e3 framed**

------------------------------------------------------------------------

**[e3 framed**]命令用来创建成帧模式下，E3通道对应的串口。

**[undo e3 framed**]命令用来删除该串口。

【命令】

**[e3**] *e3-number* **framed**

**[undo e3**] *e3-number* **framed**

【缺省情况】

未创建串口。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e3-number*]：CPOS接口的E3通道号，取值范围为1～3。

【使用指导】

在将E3通道设置为成帧方式后，系统会自动创建一个串口，名称为Serial接口编号/通道号:0。

【举例】

\# 将CPOS接口2/4/0的第3个E3通道设置为成帧模式，并创建对应的串口。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e3 3 framed

**CPOS接口 \-- CPOS接口配置命令 \-- e3 loopback**

------------------------------------------------------------------------

**[e3 loopback**]命令用来配置E3通道的环回模式。

**[undo e3 loopback**]命令用来取消环回。

【命令】

**[e3**[ *e3-number* **loopback** { **local** \| **payload** \| **remote** }]]

**[undo e3** *e3-number* **loopback**]

【缺省情况】

未进行任何形式的环回。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e3-number*]：CPOS接口的E3通道号，取值范围为1～3。

**[local**]：使能E3通道对内自环。

**[payload**]：使能E3通道对外载荷环回。

**[remote**]：使能E3通道对外远端环回，目前暂不支持该命令。

【使用指导】

E3通道提供丰富的环回功能，可用于不同层次的测试。

·在对内自环模式下，发端的数据直接被环回到收端。

·在对外载荷环回模式下，收端接收的数据经过E3成帧器，生成载荷后再进行环回。

·在对外远端环回模式下，收端接收的数据不经过E3成帧器，未生成载荷即进行环回。

相关配置可参考命令**display controller cpos e3**。

【举例】

\# 设置E3通道1进行对外载荷环回。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e3 1 loopback payload

【相关命令】

·**display controller cpos e3**

**CPOS接口 \-- CPOS接口配置命令 \-- e3 national-bit**

------------------------------------------------------------------------

**[e3 national-bit**]命令用来设置E3通道的national bit通信码。

**[undo e3 national-bit**]命令用来恢复national bit为缺省状态。

【命令】

**[e3**[ *e3-number* **national-bit** { **0** \| **1** }]]

**[undo e3** *e3-number* **national-bit**]

【缺省情况】

E3通道的national bit为1。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e3-number*]：CPOS接口的E3通道号，取值范围为1～3。

**[0**]：设置national-bit为0。

**[1**]：设置national-bit为1。

【使用指导】

national-bit是一种E3通道内使用的通信码。当用于国内通信时设置为0，用于国际通信时设置为1。

【举例】

\# 设置E3通道的national-bit为1。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e3 1 national-bit 1

**CPOS接口 \-- CPOS接口配置命令 \-- e3 shutdown**

------------------------------------------------------------------------

**[e3 shutdown**]命令用来关闭E3通道。

**[undo e3 shutdown**]命令用来打开E3通道。

【命令】

**[e3** *e3-number* **shutdown**]

**[undo e3** *e3-number* **shutdown**]

【缺省情况】

E3通道处于打开状态。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e3-number*]：CPOS接口的E3通道号，取值范围为1～3。

【举例】

\# 关闭E3通道。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 e3 1 shutdown

**CPOS接口 \-- CPOS接口配置命令 \-- fe3**

------------------------------------------------------------------------

**[fe3**]命令用来配置指定的E3通道工作在FE3模式，并配置DSU模式或子速率。

**[undo fe3**]命令用来恢复缺省情况。

【命令】

**[fe3**[ *e3-number* { **dsu-mode** { **0** \| **1** } \| **subrate** *sub-number* }]]

**[undo fe3**[ *e3-number* { **dsu-mode** \| **subrate** }]]

【缺省情况】

DSU模式为1，即Kentrox模式；子速率为34010kbps。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e3-number*]：CPOS接口的E3通道号，取值范围为1～3。

**[dsu-mode**]：设置FE3的DSU（Data Service Units）模式，目前支持的FE3 DSU模式，如下：

·**0**：Digital Link，子速率范围为358kbps～34010kbps，共95个速率等级，级差358kbps。

·**1**：Kentrox，子速率范围为500kbps～24500kbps，34010kbps，共50个速率等级，级差500kbps。

**[subrate*** sub-number*]：设置FE3的子速率，取值范围为1～34010，单位为kbps。

【使用指导】

FE3（Fractional E3，或称Subrate E3）是E3的一种非标准应用模式。目前各厂商支持的速率等级均不一样，使用**fe3**命令可以使我们的设备和其他厂家设备的FE3 DSU模式兼容，实现互通。

需要注意的是：

·通过**fe3 subrate**设置的速率值是一个大概值。由于通过**fe3 dsu-mode**命令配置的各DSU的子速率值是离散的，因此，当再通过**fe3 subrate**命令指定子速率后，E3接口会根据当前配置的DSU模式计算出与这个指定子速率最匹配的精确速率（精确到bps），并设置硬件电路支持该速率。

·通过**display interface serial ***interface-number*:**0**命令可以查看E3接口的DSU模式、子速率设置值、接口实际速率和接口的波特率。接口实际速率为不含开销在内的纯数据带宽，接口波特率（34368kbps）为E3线路的实际速率（含开销位在内）。

【举例】

\# 设置E3通道1工作在DSU模式1，速率500kbps。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 fe3 1 dsu-mode 1

Sysname-Cpos2/4/0 fe3 1 subrate 500

**CPOS接口 \-- CPOS接口配置命令 \-- flag**

------------------------------------------------------------------------

**[flag**]命令用来设置SONET/SDH帧的开销字节。

**[undo flag**]命令用来恢复缺省情况。

【命令】

**[flag **[{ **c2** *path-number c2-value* \| **s1** *s1-value \|* **s1s0** *path-number s1s0-value* }]]

**[undo**[ **flag** { **c2** *path-number* \| **s1 \| s1s0** *path-number* }]]

**[flag**[ { **j0** \| **j1** *path-number* } { **sdh** \| **sonet** } *flag-value*]]

**[undo flag **[{ **j0** \| **j1** *path-number* } { **sdh** \| **sonet** }]]

【缺省情况】

**[c2**]取值为0x02。

**[s1**]取值为0x0f。

**[s1s0**]的SONET取值为0x00，**s1s0**的SDH取值为0x02。

**[j0**]的SONET取值为0x01，**j0**的SDH取值为16字节空字符""。

**[j1**]的SONET取值为64字节空字符""，**j1**的SDH取值为16字节空字符""。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[c2*** path-number c2-value*]：*path-number*通道编号、*c2-value*信号标记字节，取值范围为0x00～0xFF。

**[s1** *s1-value*]：同步状态字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[s1s0*** path-number s1s0-value*]：*path-number*通道编号、*s1s0-value*指示AU，TU类型。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[j0*** flag-value*]：再生段踪迹字节，属于段开销字节（Section Overhead），用于检测两个端口之间的连接在段层次上的连续性。SDH帧格式下*flag-value*的取值范围为1～15个字符的字符串；SONET帧格式下*flag-value*的取值范围为0x00～0xFF。

**[j1*** path-number*]：通道踪迹字节，属于高阶通道开销字节，用于检测两个端口之间的连接在通道层次上的连续性。SDH帧格式下*flag-value*的取值范围为1～15个字符的字符串；SONET帧格式下*flag-value*的取值范围为1～62个字符的字符串。

**[sdh**]：帧格式为SDH（Synchronous Digital Hierarchy，同步数字系列）。

**[sonet**]：帧格式为SONET（Synchronous Optical Network，同步光网络）。

【使用指导】

SONET/SDH帧具有丰富的开销字节，可完成对传输网的分层管理等运行维护功能（OAM，Operation and Maintenance）。

·**j0**、**j1**和**c2**主要用于在不同国家、不同地区、或不同厂商的设备之间提供互通支持。

·**j0**属于段开销字节，用于检测两个接口之间的连接在段层次上的连续性。**j1**和**c2**属于高阶通道开销字节，**j1**用于检测两个接口之间的连接在通道层次上的连续性，**c2**用来指示VC帧的复接结构和信息净负荷的性质。

·**S1**是同步状态字节，不同的值表示ITU-T的不同时钟质量级别，使设备能据此判定接收的时钟信号的质量以此决定是否切换时钟源即切换到较高质量的时钟源上。值越小，时钟精度越高。

·**S1S0**是H1字节中的两个比特，在ITU标准里用于指示AU-n/TU-n的类型。当处理AU-4，AU-3，TU-3时要求必须设置为2。

【举例】

\# 设置CPOS接口2/4/0的再生段跟踪字节**j0**为字符串aa。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 flag j0 sdh aa

【相关命令】

·**display controller cpos**

**CPOS接口 \-- CPOS接口配置命令 \-- flag vc-3**

------------------------------------------------------------------------

**[flag vc-3**]命令用来设置vc-3帧的开销字节。

**[undo flag vc-3**]命令用来恢复缺省情况。

【命令】

**[flag** **vc-3** *path-number******[c2-value *[\| **j1** *[sdh-string ]*[\| **sonet** ]*sonet-string*****[} \| **s1s0** ]*s1s0-value *}]

**[undo flag vc-3 ***path-number*****[{ **c2** \| **j1** { **sdh** \| **sonet** } \| **s1s0** }]]

【缺省情况】]

**[c2**]取值为0x02。

**[j1**]的SONET取值为64字节空字符""，**j1**的SDH取值为16字节空字符""。

**[s1s0**]的SONET取值为0x00，**s1s0**的SDH取值为0x02。

【视图】]

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[path-number*]：vc3通道编号。

**[c2 ***c2-value*]：信号标记字节，取值范围为0x00～0xFF。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[j1** **sdh** *sdh-string*]：高阶通道追踪字节，*sdh-string*为1～15个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[j1** **sonet** *sonet-string*]：高阶通道追踪字节，*sonet-string*为1～62个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[s1s0 ***s1s0-value*]：AU/TU类型指示值。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

SONET/SDH帧具有丰富的开销字节，可完成对传输网的分层管理等运行维护功能。

·**j1**和**c2**主要用于在不同国家、不同地区、或不同厂商的设备之间提供互通支持。

·**j1**和**c2**属于高阶通道开销字节，**j1**用于检测两个接口之间的连接在通道层次上的连续性，**c2**用来指示VC帧的复接结构和信息净负荷的性质。

【举例】

\# 设置CPOS接口2/4/0的vc-3的2号通道的c2的开销值为2。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 flag vc-3 2 c2 2

**CPOS接口 \-- CPOS接口配置命令 \-- flag vc-4**

------------------------------------------------------------------------

**[flag vc-4**]命令用来设置vc-4帧的开销字节。

**[undo flag vc-4**]命令用来恢复缺省情况。

【命令】

**[flag** **vc-4** *path-number******[c2-value *[\| **j1** *[sdh-string ]*[\| **sonet** ]*sonet-string*****[} \| **s1s0** ]*s1s0-value *}]

**[undo flag vc-4 ***path-number*[ { **c2** \| **j1** { **sdh** \| **sonet** } \| **s1s0** }]]

【缺省情况】]

**[c2**]取值为0x02。

**[j1**]的SONET取值为64字节空字符""，**j1**的SDH取值为16字节空字符""。

**[s1s0**]的SONET取值为0x00，**s1s0**的SDH取值为0x02。

【视图】]

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[path-number*]：vc4通道编号。

**[c2 ***c2-value*]：信号标记字节，取值范围为0x00～0xFF。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[j1** **sdh** *sdh-string*]：高阶通道追踪字节，为1～15个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[j1** **sonet** *sonet-string*]：高阶通道追踪字节，为1～62个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[s1s0 ***s1s0-value*]：AU/TU类型指示值。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

SONET/SDH帧具有丰富的开销字节，可完成对传输网的分层管理等运行维护功能。

·**j1**和**c2**主要用于在不同国家、不同地区、或不同厂商的设备之间提供互通支持。

·**j1**和**c2**属于高阶通道开销字节，**j1**用于检测两个接口之间的连接在通道层次上的连续性，**c2**用来指示VC帧的复接结构和信息净负荷的性质。

【举例】

\# 设置CPOS2/4/0的vc-4 1号通道j1的sdh开销字节为abcd。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 flag vc-4 1 j1 sdh abcd

**CPOS接口 \-- CPOS接口配置命令 \-- frame-format**

------------------------------------------------------------------------

**[frame-format**]命令用来设置CPOS接口的帧格式。

**[undo frame-format**]用来恢复缺省情况。

【命令】

**[frame-format**[ { **sdh** \| **sonet** }]]

**[undo** **frame-format**]

【缺省情况】

CPOS接口的帧格式为SDH。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sdh**]：帧格式为SDH。

**[sonet**]：帧格式为SONET。

【举例】

\# 设置CPOS接口2/4/0接口的帧格式为SONET。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 frame-format sonet

**CPOS接口 \-- CPOS接口配置命令 \-- ft3**

------------------------------------------------------------------------

**[ft3**]命令用于配置E3通道工作在FT3模式，并配置DSU模式或子速率。

**[undo ft3**]命令用来恢复缺省情况。

【命令】

**[ft3**[ *t3-number* { **dsu-mode** { **0** \| **1** \| **2** \| **3** \| **4** } \| **subrate** *sub-number* }]]

**[undo ft3**[ *t3-number* { **dsu-mode** \| **subrate** }]]

【缺省情况】

DSU模式为0，即Digital Link模式；子速率为44210kbps。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

**[dsu-mode**]：设置FT3的DSU模式，支持常用的几家厂商的FT3 DSU模式，如下：

·**0**：Digital Link，支持子速率范围为300～44210kbps，共147个速率等级，级差300746bps。

·**1**：Kentrox，支持子速率范围为1500～35000kbps及44210kbps，共69个速率等级，级差500000bps。

·**2**：Larscom，支持子速率范围为3100～44210kbps，共14个速率等级，级差3157835bps。

·**3**：Adtran，支持子速率范围为75～44210kbps，共588个速率等级，级差75187bps。

·**4**：Verilink，支持子速率范围为1500～44210kbps，共20个速率等级，级差1578918bps。

**[subrate ***sub-number*]：设置FT3的子速率，取值范围为1～44210。

【使用指导】

FT3（Fractional T3，或称Subrate T3）是T3的一种非标准应用模式。目前各厂商支持的速率等级均不一样，使用**ft3**命令可以使我们的设备和其他厂家设备的FT3 DSU模式兼容，实现互通。

需要注意的是：

·通过**ft3 subrate**设置的速率值是一个大概值。由于通过**ft3 dsu-mode**命令配置的各DSU的子速率值是离散的，因此，当再通过**ft3 subrate**命令指定子速率后，T3接口会根据当前配置的DSU模式计算出与这个指定子速率最匹配的精确速率（精确到bps），并设置硬件电路支持该速率。

·通过**display interface serial ***interface-number***:0**命令可以查看T3接口的DSU模式、子速率设置值、接口实际速率和接口的波特率。接口实际速率为不含开销在内的纯数据带宽，接口波特率（44736kbps）为T3线路的实际速率（含开销位在内）。

【举例】

\# 设置T3通道1工作在DSU模式3，速率3000kbps。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 ft3 1 dsu-mode 3

Sysname-Cpos2/4/0 ft3 1 subrate 3000

**CPOS接口 \-- CPOS接口配置命令 \-- link-delay**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-delay**]命令用来配置当前接口的物理连接状态抑制时间。

**[undo link-delay**]命令用来恢复缺省情况。

【命令】

**[link-delay** *seconds*]

**[undo link-delay**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：表示物理连接状态的抑制时间，单位为秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

通常情况下，当接口的物理连接状态（up和down）改变时，系统会立即通知上层协议模块并生成Trap和Log信息。为了避免接口物理连接状态在短时间内的频繁改变带来额外的系统开销，可通过本命令配置接口的物理连接状态抑制时间，接口在此时间内产生的物理连接状态变化将被系统忽略。

【举例】

\# 设置CPOS接口2/4/0的物理连接状态抑制时间为8秒。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 link-delay 8

**CPOS接口 \-- CPOS接口配置命令 \-- loopback**

------------------------------------------------------------------------

**[loopback**]命令用来开启CPOS接口的环回功能。

**[undo loopback**]命令用来取消环回设置。

【命令】

**[loopback**[ { **local** \| **remote** }]]

**[undo loopback**]

【缺省情况】

环回功能处于关闭状态。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：设置CPOS接口进行对内自环。

**[remote**]：设置CPOS接口进行对外远端环回。

【使用指导】

环回主要用于一些特殊功能的测试。对内自环也称为本地环回，用于对物理接口本身进行检测。对外环回则可用于对接口连接的线缆进行检测。

正常情况下，不要设置环回功能。

【举例】

\# 设置CPOS接口2/4/0进行远端线路环回。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 loopback remote

**CPOS接口 \-- CPOS接口配置命令 \-- multiplex mode**

------------------------------------------------------------------------

**[multiplex mode**]命令用来设置AUG的复用路径。

**[undo multiplex mode**]命令用来恢复缺省情况。

【命令】

**[multiplex mode **[{ **au-3** \| **au-4** }]]

**[undo** **multiplex mode**]

【缺省情况】

AUG的复用路径为**au-4**。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[au-3**]：配置AUG通过AU-3得到。

**[au-4**]：配置AUG通过AU-4得到。

【使用指导】

当CPOS应用在SDH模式下时，可使用**multiplex mode**命令选择设置AUG复用到AU-4还是AU-3，如果CPOS应用在SONET模式下，则只能复用到AU-3，不能使用**multiplex mode**命令。

在SDH中，载荷有两种映射/复用的方案：ANSI和ETSI：

·ANSI的复用方案为AU-3复用（**au-3**），低阶载荷被聚合进VC-3高阶通道，VC-3加上一个AU指针后成为管理单元AU-3，再由三个这样的AU-3同步复用成一个管理单元组AUG。

·ETSI的复用方案为AU-4复用（**au-4**），低阶载荷被聚合进VC-4高阶通道，VC-4加上一个AU指针后成为管理单元AU-4，再由一个这样的AU-4同步复用成一个管理单元组AUG。

实际应用中，不同的国家和地区可能采用不同的复用路径，为保证互通，请用户根据实际情况选择合适的复用路径（我国光同步传输网技术体制选用的是AU-4的复用路径）。

【举例】

\# 在SDH模式下，设置AUG复用到AU-3。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 frame-format sdh

Sysname-Cpos2/4/0 multiplex mode au-3

【相关命令】

·**frame-format**

**CPOS接口 \-- CPOS接口配置命令 \-- oc-12**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[oc-12**]命令用来在2.5Gbps高速CPOS接口视图下创建指定通道号的622Mbps通道，并且进入指定622Mbps通道视图；如果已经创建了此622Mbps通道，直接进入指定622Mbps通道视图。

**[undo oc-12**]命令用来删除指定通道号的622Mbps通道及其派生的低阶通道（包括155Mbps通道和155Mbps通道下的E3/T3通道）及POS通道接口。

【命令】

**[oc-12 **]*oc-12-number*

**[undo oc-12 **]*oc-12-number*

【缺省情况】

2.5Gbps高速CPOS接口下无622Mbps通道。

【视图】

2.5Gbps高速CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[oc-12-number*]：622Mbps通道号，取值范围为1～4。

【使用指导】

2.5Gbps高速CPOS接口工作在通道模式时，最多支持创建4个622Mbps通道。

【举例】

\# 在2.5Gbps高速CPOS2/4/0接口下创建622Mbps通道。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 oc-12 2

Sysname-Cpos2/4/0-oc-12-2

**CPOS接口 \-- CPOS接口配置命令 \-- oc-3**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[oc-3**]命令用来在622Mbps高速CPOS接口视图下或622Mbps通道视图下创建指定通道号的155Mbps通道，并且进入指定155Mbps通道视图；如果已经创建了此155Mbps通道，直接进入指定155Mbps通道视图。

**[undo oc-3**]命令用来删除指定通道号的155Mbps通道及其派生的低阶通道（包括E3/T3通道）及POS通道接口。

【命令】

**[oc-3 **]*oc-3-number*

**[undo oc-3 **]*oc-3-number*

【缺省情况】

622Mbps高速CPOS接口或622Mbps通道下无155Mbps通道。

【视图】

622Mbps高速CPOS接口视图/622Mbps通道视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[oc-3-number*]：155Mbps通道号，取值范围为1～4。

【使用指导】

622Mbps高速CPOS接口或622Mbps通道工作在通道模式时，最多支持创建4个155Mbps通道。

622Mbps高速CPOS接口或622Mbps通道创建155Mbps通道时，如果155Mbps通道不支持通道模式，则自动配置为级联模式。

【举例】

\# 在622Mbps高速CPOS2/4/0接口下创建155Mbps通道。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 oc-3 2

Sysname-Cpos2/4/0-oc-3-2

\# 在2.5Gbps高速CPOS2/4/0接口的622Mbps通道下创建155Mbps通道。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 oc-12 1

Sysname-Cpos2/4/0-oc-12-1 oc-3 1

Sysname-Cpos2/4/0-oc-12-1-oc-3-1

**CPOS接口 \-- CPOS接口配置命令 \-- reset counters controller cpos**

------------------------------------------------------------------------

**[reset counters controller cpos**]命令用来清除CPOS接口的统计信息。

【命令】

**[reset counters controller cpos** [ *interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：CPOS接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定*interface-number*，则清除所有CPOS接口的统计信息；

·如果指定*interface-number*，则清除指定CPOS接口的统计信息。

统计信息可以用**display controller cpos**命令来查看。

【举例】

\# 清除CPOS接口2/4/0的统计信息。

\<Sysname\> reset counters controller cpos 2/4/0

【相关命令】

·**display controller cpos**

**CPOS接口 \-- CPOS接口配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭接口。

**[undo** **shutdown**]命令用来打开接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

CPOS接口处于打开状态。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对CPOS物理接口执行**shutdown**操作后，该CPOS的所有E1/T1通道及捆绑形成的串口将全部被禁用，停止收发数据。如果执行**undo shutdown**操作，则所有E1/T1通道和捆绑形成的串口将恢复为up。

【举例】

\# 关闭CPOS接口2/4/0。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 shutdown

**CPOS接口 \-- CPOS接口配置命令 \-- t1 channel-set**

------------------------------------------------------------------------

**[t1 channel-set**]命令用来对T1通道的时隙进行捆绑。

**[undo t1 channel-set**]命令用来取消指定的捆绑。

【命令】

**[t1**[ *t1-number* **channel-set** *set-number* **timeslot-list** *range* [ **speed** { **56k** \| **64k** } ]]]

**[undo t1** *t1-number* **channel-set** *set-number*]

【缺省情况】

T1不进行通道化。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t1-number*]：CPOS接口的T1通道号，取值范围为1～84。

*[set-number*]：捆绑集的编号，取值范围为0～23。

**[timeslot-list*** range*]：用于捆绑的时隙列表。*range*的取值范围为1～24，在指定捆绑的时隙时，可以用*number*的形式指定单个时隙，也可以用*number1*～*number2*的形式指定一个范围内的时隙，还可以使用*number1*、*number2*～*number3*的形式，同时指定多个时隙。

**[speed**[ { **56k** \| **64k** }]]：配置时隙捆绑的方式。选用参数**56k**时，捆绑方式为N×56kbps；选用参数**64k**时，捆绑方式为N×64kbps。如果不指定速率，缺省采用64kbps。

【使用指导】

捆绑形成的串口编号形式为：接口编号/通道号:channel-set号。

【举例】

\# 对T1通道1进行捆绑。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t1 1 channel-set 1 timeslot-list 1-23

\# 进入捆绑后形成的串口的视图。

Sysname-Cpos2/4/0 quit

Sysname interface serial 2/4/0/1:1

Sysname-Serial2/4/0/1:1

【相关命令】

·**t1 unframed**

**CPOS接口 \-- CPOS接口配置命令 \-- t1 clock**

------------------------------------------------------------------------

**[t1 clock**]命令用来设置T1通道的时钟模式。

**[undo t1 clock**]命令用来恢复缺省情况。

【命令】

**[t1**[ *t1-number* **clock** { **master** \| **slave** }]]

**[undo t1** *t1-number* **clock**]

【缺省情况】

T1通道的时钟模式为从时钟模式（**slave**）。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t1-number*]：CPOS接口的T1通道号，取值范围为1～84。

**[master**]：设置T1通道的时钟模式为主时钟模式。

**[slave**]：设置T1通道的时钟模式为从时钟模式。

【使用指导】

可以为不同的T1通道单独配置时钟模式，使用主时钟模式还是从时钟模式应根据连接的设备确定。例如，与SONET/SDH设备连接时，应使用从时钟模式，而如果是设备之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。

同一CPOS物理接口的不同T1通道的时钟模式是相互独立的。

【举例】

\# 设置T1通道1使用主时钟模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t1 1 clock master

**CPOS接口 \-- CPOS接口配置命令 \-- t1 flag**

------------------------------------------------------------------------

**[t1 flag**]命令用来设置T1通道开销。

**[undo t1 flag**]命令用来恢复缺省情况。

【命令】

**[t1***t1-number* **flag** **c2** *c2-value*]

**[undo t1 **]*t1-number* **flag** **c2**

**[t1**]*****t1-number***flag j2 **[{ **sdh** \| **sonet** } ]*j2-string*

**[undo t1 **]*t1-number***flag j2**[ { **sdh** \| **sonet** }]

【缺省情况】

**[c2**]取值为02（十六进制），**j2**循环发送空字符""。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t1-number*]：CPOS接口的T1通道号，取值范围为1～84。

**[c2**]：低阶通道信号标签字节。

*[c2-value*]：一个字节的开销的值，取值范围为0～7。协议不支持该值为5。

**[j2**]：低阶通道踪迹字节J2。

**[sdh**]：SDH格式的跟踪字节。

**[sonet**]：SONET格式的跟踪字节。

*[j2-string*]：踪迹字节，对于SDH格式取值范围为1～15个字符，对于SONET格式取值范围为1～62个字符。

【举例】

\# CPOS接口下配置T1通道3的c2开销为0x7。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t1 3 flag c2 7

**CPOS接口 \-- CPOS接口配置命令 \-- t1 frame-format**

------------------------------------------------------------------------

**[t1 frame-format**]命令用来设置T1通道的帧格式。

**[undo t1 frame-format**]命令用来恢复缺省情况。

【命令】

**[t1*** t1-number*** frame-format **[{ **esf** \| **sf** }]]

**[undo** **t1** *t1-number* **frame-format**]

【缺省情况】

T1通道的帧格式为ESF。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t1-number*]：CPOS接口的T1通道号，取值范围为1～84。

**[esf**]：设置T1通道使用ESF（Extended Super Frame，扩展超帧）格式。

**[sf**]：设置T1通道使用SF（Super Frame，超帧）格式。

【举例】

\# 设置T1通道1的帧格式为SF。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t1 1 frame-format sf

**CPOS接口 \-- CPOS接口配置命令 \-- t1 loopback**

------------------------------------------------------------------------

**[t1 loopback**]命令用来设置T1通道的环回模式。

**[undo t1 loopback**]命令用来取消环回。

【命令】

**[t1**[ *t1-number* **loopback** { **local** \| **payload** \| **remote** }]]

**[undo t1** *t1-number* **loopback**]

【缺省情况】

未进行任何形式的环回。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t1-number*]：CPOS接口的T1通道号，取值范围为1～84。

**[local**]：使能T1通道对内自环。

**[payload**]：使能T1通道对外载荷环回。

**[remote**]：使能T1通道对外远端环回。

【使用指导】

环回功能通常用于进行某些特殊测试，正常工作时不要启动环回。

【举例】

\# 设置T1通道1进行对外载荷环回。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t1 1 loopback payload

【相关命令】

·**display controller cpos t1**

**CPOS接口 \-- CPOS接口配置命令 \-- t1 shutdown**

------------------------------------------------------------------------

**[t1 shutdown**]命令用来关闭T1通道。

**[undo t1 shutdown**]命令用来打开T1通道。

【命令】

**[t1 ***t1-number ***shutdown**]

**[undo t1 ***t1-number ***shutdown**]

【缺省情况】

T1通道处于打开状态。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t1-number*]：CPOS接口的T1通道号，取值范围为1～84。

【使用指导】

关闭T1通道后，如果有捆绑形成的串口，则串口也被关闭。

【举例】

\# 关闭T1通道1。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t1 1 shutdown

**CPOS接口 \-- CPOS接口配置命令 \-- t1 unframed**

------------------------------------------------------------------------

**[t1 unframed**]命令用来设置CPOS的T1通道工作在非成帧模式。

**[undo t1 unframed**]命令用来恢复缺省情况。

【命令】

**[t1** *t1-number* **unframed**]

**[undo t1** *t1-number* **unframed**]

【缺省情况】

T1工作在成帧模式。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t1-number*]：CPOS的T1通道号，取值范围为1～84。

【使用指导】

CPOS通道化生成的T1支持非成帧和成帧两种工作模式。

·在非成帧模式下，T1通道不分时隙，形成一个速率为1.544Mbps的串口，名称为Serial接口编号/通道号:0。

·在成帧模式下，T1通道的24个时隙可以任意捆绑为串口使用。

【举例】

\# 将CPOS接口2/4/0的第3个T1通道设置为非成帧模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t1 3 unframed

**CPOS接口 \-- CPOS接口配置命令 \-- t3 alarm**

------------------------------------------------------------------------

**[t3** **alarm**]命令用来配置T3通道的告警信号检测与发送功能。用户可打开或关闭告警信号的检测开关，也可发送某种告警信号以测试线路状态等。

**[undo t3** **alarm**]命令用来恢复缺省情况。

【命令】

**[t3**[ *t3-number* **alarm** { **detect** \| **generate** { **ais** \| **febe** \| **idle** \| **rai** } }]]

**[undo t3**[ *t3-number* **alarm** { **detect** \| **generate** { **ais** \| **febe** \| **idle** \| **rai** } }]]

【缺省情况】

T3通道的告警信号检测功能处于打开状态，发送功能处于关闭状态。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

**[detect**]：T3通道的定时检测各种告警的功能。

**[generate**]：发送某种告警信号，如AIS、RAI、IDLE和FEBE。可用于线路状态测试。

·**ais**：Alarm Indication Signal，即告警指示信号。

·**febe**：Far End Block Error，即远端块错误。

·**idle**：空闲信号。

·**rai**：Remote Alarm Indication，即远端告警指示信号。

【使用指导】

上电后，T3通道的告警信号检测功能是打开的，并能通过通道显示实时报告通道告警状态，如LOS、LOF、AIS、RAI等。当检测到LOS、LOF或AIS告警信号后，会向对方发送RAI告警信号。

主要的告警信号包括：LOS（Loss Of Signal，信号丢失）、LOF（Loss Of Frame，帧同步丢失）、AIS（Alarm Indication Signal，告警指示信号）、RAI（Remote Alarm Indication，远端告警指示信号）、FEBE（Far End Block Error，远端块错误）、IDLE为空闲信号。各信号具体格式遵循T3规范ANSI T1.107-1995。

通道一次只能发送一种告警信号（包括在使用**detect**功能时检测到LOS、LOF或AIS后而产生的RAI告警信号），发送另一种告警信号前必须使用**undo t3 alarm generate**命令取消前一种告警信号。**detect**功能产生的告警信号（RAI）必须通过**undo t3 alarm detect**命令取消。

【举例】

\# 打开CPOS接口2/4/0通道2的告警检测功能。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 2 alarm detect

\# 在CPOS接口2/4/0通道2上发送AIS告警信号。

\<Sysname\> system-view

Sysname controller CPOS 2/4/0

Sysname-Cpos2/4/0 t3 2 alarm generate ais

**CPOS接口 \-- CPOS接口配置命令 \-- t3 bert**

------------------------------------------------------------------------

**[t3******bert**]命令用来进行线路位（Bit）错误率的测试。

**[undo** **t3** **bert**]命令用来恢复缺省情况。

【命令】

**[t3**[ *t3-number* **bert** **pattern** { **2\^7** \| **2\^11** \| **2\^15** \| **qrss** } **time** *time-number*]]

**[undo t3**] *t3-number* **bert**

【缺省情况】

不进行线路位错误率的测试。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

**[pattern**]：设置BERT测试模式，包括**2\^7**，**2\^11**，**2\^15**和**qrss**。

·**2\^7**：发送的码流长度为2的7次方个bit。

·**2\^11**：发送的码流长度为2的11次方个bit。

·**2\^15**：发送的码流长度为2的15次方个bit。

·**qrss**：发送码流长度为2的20次方个bit，且码流中不允许连续14个以上的0。

*[time-number*]：设置BERT测试的持续时间，取值范围为1～1440，单位为分钟。

【使用指导】

ITU O.151、ITU O.153及ANSI T1.403-1999定义了各种BERT测试模式，目前T3通道支持**2\^7**，**2\^11**，**2\^15**和**qrss**这几种测试模式。

BERT测试方式为，本端发出测试数据流，经过线路某处环回回来，本端检测收到的测试数据流与发出的测试数据流是否一致，位错误率达到多少，从而为用户判断线路状态提供依据。因此，要求线路中某处能环回发出的数据流，如将对端设置为远端环回等。

利用**t3******bert**命令配置好测试模式，指定测试持续时间，开始测试后，可以查看接口状态中的BERT测试状态和测试结果。BERT测试状态和测试结果的说明详见T3通道显示部分。

【举例】

\# 在CPOS接口2/4/0的2号通道上执行QRSS格式的BERT测试10分钟。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 2 bert pattern qrss time 10

**CPOS接口 \-- CPOS接口配置命令 \-- t3 clock**

------------------------------------------------------------------------

**[t3 clock**]命令用来设置T3通道的时钟模式。

**[undo t3 clock**]命令用来恢复缺省情况。

【命令】

**[t3**[ *t3-number* **clock** { **master** \| **slave** }]]

**[undo t3** *t3-number* **clock**]

【缺省情况】

T3通道的时钟模式为从时钟模式（**slave**）。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

**[master**]：设置T3通道的时钟模式为主时钟模式。

**[slave**]：设置T3通道的时钟模式为从时钟模式。

【使用指导】

可以为不同的T3通道单独配置时钟模式，使用主时钟模式还是从时钟模式应根据连接的设备确定。例如，与SONET/SDH设备连接时，应使用从时钟模式，而如果是设备之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。

同一CPOS物理接口的不同T3通道的时钟模式是相互独立的。

![说明](CPOS接口命令.files/image004.png)

建议将全局下**clock**时钟模式和T3通道的时钟模式配置一致。

【举例】

\# 设置T3通道3使用主时钟模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 clock master

**CPOS接口 \-- CPOS接口配置命令 \-- t3 feac**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image004.png)

本命令的支持情况与设备的型号相关，请以设备的实际情况为准。

**[t3** **feac**]命令用来配置T3接口的FEAC链路信号的检测和传输功能。

**[undo t3** **feac**]命令用来取消已有的FEAC配置。

【命令】

**[t3**[ *t3-number* **feac** { **detect** \| **generate** { **ds3-los** \| **ds3-ais** \| **ds3-oof** \| **ds3-idle** \| **ds3-eqptfail** \| **loopback** { **ds3-line** \| **ds3-payload** } } }]]

**[undo t3**[ *t3-number* **feac** { **detect** \| **generate** { **ds3-los** \| **ds3-ais** \| **ds3-oof** \| **ds3-idle** \| **ds3-eqptfail** \| **loopback** { **ds3-line** \| **ds3-payload** } } }]]

【缺省情况】

T3接口的FEAC链路信号检测功能处于打开状态，传输功能处于关闭状态。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

**[detect**]：T3接口上的定时检测FEAC链路信号功能。

**[generate**]：发送FEAC信号，包括**ds3-los**、**ds3-ais**、**ds3-oof**、**ds3-idle**、**ds3-eqptfail**。

**[loopback**]：发送环回码，用于激活对端的线路环回（**ds3-line**）或者净荷环回（**ds3-payload**）。

【使用指导】

FEAC（Far End Alarm and Control signal，远端告警与控制信号）是利用C-bit帧格式中第一个子帧中的第三个C比特组成的一条数据链路，可用于传输各种告警状态信号，也可用于传输环回控制码，用来激活或者取消对端的环回，进行环回测试。ANSI T1.107a中规定，FEAC可用于传输多种告警信号，并规定这条链路的数据帧为基于位的BOP（Bit Oriented Protocol）协议格式。

上电后，T3接口的FEAC定时检测功能是打开的，但不发送任何FEAC信号。

当利用该命令配置远端环回前，最好禁止本端的FEAC检测，以免发出的环回码在对方配好环回后被返回来，造成本端也配置为环回，引起线路上的环路死锁。

【举例】

\# 打开T3通道1的FEAC链路数据检测功能。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 feac detect

\# 在T3通道1上发送ds3-los信号。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 feac generate ds3-los

\# 在T3通道1上发送环回码给对端，设置对端为线路环回。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 feac generate loopback ds3-line

**CPOS接口 \-- CPOS接口配置命令 \-- t3 framed**

------------------------------------------------------------------------

**[t3 framed**]命令用来创建成帧模式下，T3通道对应的串口。

**[undo t3 framed**]命令用来删除该串口。

【命令】

**[t3**] *t3-number* **framed**

**[undo t3**] *t3-number* **framed**

【缺省情况】

未创建串口。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

【使用指导】

在将T3通道设置为成帧方式后，系统会自动创建一个串口，名称为Serial接口编号/通道号:0。

【举例】

\# 将CPOS接口2/4/0的第3个T3通道设置为成帧模式，并创建对应的串口。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 3 framed

**CPOS接口 \-- CPOS接口配置命令 \-- t3 frame-format**

------------------------------------------------------------------------

**[t3 **]**frame-format**命令用来配置T3接口所使用的帧格式。

**[undo t3 frame-format**]命令用来恢复缺省情况。

【命令】

**[t3*** t3-number*****]**frame-format **[{ **c-bit** \| **m23** }]

**[undo** **t3** *t3-number* **frame-format**]

【缺省情况】

T3接口的帧格式为C-bit Parity。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

**[c-bit**]：设置帧格式为C-bit Parity（G.704）携带可维护信息（如FEAC）。

**[m23**]：设置帧格式为M23（G.752）。

【举例】

\# 设置T3通道1的帧格式为m23。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 frame-format m23

**CPOS接口 \-- CPOS接口配置命令 \-- t3 loopback**

------------------------------------------------------------------------

**[t3 loopback**]命令用来设置T3通道的环回模式。

**[undo t3 loopback**]命令用来恢复缺省情况。

【命令】

**[t3**[ *t3-number* **loopback** { **local** \| **payload** \| **remote** }]]

**[undo t3** *t3-number* **loopback**]

【缺省情况】

不进行任何形式的环回。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

**[local**]：使能T3通道对内自环。

**[payload**]：使能T3通道对外载荷环回。

**[remote**]：使能T3通道对外远端环回。

【使用指导】

环回功能通常用于进行某些特殊测试，正常工作时不要启动环回。

【举例】

\# 设置T3通道1进行对外载荷环回。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 loopback payload

【相关命令】

·**display controller cpos t****3**

**CPOS接口 \-- CPOS接口配置命令 \-- t3 mdl**

------------------------------------------------------------------------

**[t3 mdl**]命令用来配置T3通道的MDL链路消息检测与传输功能。

**[undo t3 mdl**]命令用来恢复缺省情况。

【命令】

**[t3**[ *t3-number* **mdl** { **data** { **eic** *string* \| **fic** *string* \| **gen-no** *string* \| **lic** *string* \| **pfi** *string* \| **port-no** *string* \| **unit** *string* } \| **detect** \| **generate** { **idle-signal** \| **path** \| **test-signal** } }]]

**[undo t3**[ *t3-number* **mdl** [ **data** [ **eic** \| **fic** \| **gen-no** \| **lic** \| **pfi** \| **port-no** \| **unit** ] \| **detect** \| **generate** [ **idle-signal** \| **path** \| **test-signal** ] ]]]

【缺省情况】

上电后，T3通道的MDL定时检测功能处于关闭状态，不发送任何消息。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

**[data**]：设置MDL消息参数，其中eic、lic、fic和unit为三类MDL消息的公有参数，pfi、port-no和gen-no分别为消息path、idle signal和test signal的私有参数。

**[eic ***string*]：Equipment ID，为1～10个字符的字符串，缺省值为line。

**[fic ***string*]：Frame ID，为1～10个字符的字符串，缺省值为line。

**[gen-no ***string*]：Generator number in test signal message，test signal消息的私有参数，为1～38个字符的字符串，缺省值为line。

**[lic ***string*]：Location ID，为1～11个字符的字符串，缺省值为line。

**[pfi ***string*]：Facility ID in path message，path消息的私有参数，为1～38个字符的字符串，缺省值为line。

**[port-no ***string*]：Port number in idle signal message，idle signal消息的私有参数，为1～38个字符的字符串，缺省值为line。

**[unit ***string*]：Unit，为1～6个字符的字符串，缺省值为line。

**[detect**]：T3通道上的定时检测MDL消息功能。

**[generate**]：按照data中配置的参数定时发送MDL消息，包括path、idle sig和test signal，可以同时发送。

【使用指导】

MDL（Maintenance Data Link，维护数据链路）是利用C-bit帧格式中第五个子帧中的3个C比特组成的一条数据链路，可用于传输一些维护性的消息。ANSI T1.107a中规定，MDL可用于传输三种消息：path、idle signal和test signal，并规定这条链路的数据帧为LAPD协议格式。

MDL链路的收发状态详见T3通道显示部分。

【举例】

\# 打开T3通道1的MDL检测功能。

\<Sysname\> system-view

Sysname controller Cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 mdl detect

\# 配置T3通道1的MDL的lic参数为字符串"hello"。

\<Sysname\> system-view

Sysname controller Cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 mdl data lic hello

\# 设置T3通道1发送path消息。

\<Sysname\> system-view

Sysname controller Cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 mdl generate path

**CPOS接口 \-- CPOS接口配置命令 \-- t3 shutdown**

------------------------------------------------------------------------

**[t3 shutdown**]命令用来关闭T3通道。

**[undo t3 shutdown**]命令用来打开T3通道。

【命令】

**[t3** *t3-number* **shutdown**]

**[undo t3** *t3-number* **shutdown**]

【缺省情况】

T3通道处于打开状态。

【视图】

CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：CPOS接口的T3通道号，取值范围为1～3。

【举例】

\# 关闭T3通道1。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 t3 1 shutdown

**CPOS接口 \-- CPOS接口配置命令 \-- threshold**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image005.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[threshold**]命令用来设置CPOS接口的SD告警门限和（或）SF告警门限。

**[undo threshold**]命令用来恢复缺省情况。

【命令】

**[threshold** { **sd** *sdvalue* \| **sf** *sfvalue* } \*]

**[undo threshold** [ **sd** \| **sf** ]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

CPOS接口视图

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

\#设置CPOS接口2/4/0的SD告警门限为10e-4。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 threshold sd 4

**CPOS接口 \-- CPOS接口配置命令 \-- using e3**

------------------------------------------------------------------------

**[using e3**]命令用来创建非成帧模式的E3通道对应的串口。

**[undo using e3**]命令用来删除该串口。

【命令】

**[using e3 ***e3-number*]

**[undo using e3 ***e3-number*]

【缺省情况】

未创建串口。

【视图】

CPOS接口视图/155Mbps通道视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[e3-number*]：E3通道号，取值范围为1～3。

【使用指导】

·CPOS接口视图下，创建非成帧模式的E3通道对应的串口名称为Serial接口编号/E3通道号:0。

·155Mbps通道视图下，创建非成帧模式的E3通道对应的串口名称为Serial接口编号/155Mbps通道号/E3通道号:0。

【举例】

\# 在CPOS接口2/4/0下创建非成帧模式的E3通道1对应的串口。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 using e3 1

Sysname-Cpos2/4/0 interface serial 2/4/0/1:0

Sysname-Serial2/4/0/1:0

\# 在622Mbps高速CPOS接口2/4/0的155Mbps通道下创建非成帧模式的E3通道1对应的串口。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 oc-3 2

Sysname-Cpos2/4/0-oc-3-2 using e3 1

Sysname-Cpos2/4/0-oc-3-2 interface serial 2/4/0/2/1:0

Sysname-Serial2/4/0/2/1:0

**CPOS接口 \-- CPOS接口配置命令 \-- using oc-12/using oc-12c**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[using oc-12**]命令用来配置622Mbps高速CPOS接口或622Mbps通道的工作模式为通道模式。

**[using oc-12c**]命令用来配置622Mbps高速CPOS接口或622Mbps通道的工作模式为级联模式。

**[undo using**]命令用来恢复缺省情况。

【命令】

**[using**  { **oc-12** \| **oc-12c** }]

**[undo using**]

【缺省情况】

接口或通道工作在通道模式。

【视图】

622Mbps高速CPOS接口视图/622Mbps通道视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在622Mbps高速CPOS接口视图或者622Mbps通道视图下通过**using oc-12c**命令设置接口或通道为级联模式后，系统会自动创建一个622Mbps的POS通道接口。POS通道接口的名称为：Pos接口编号/622Mbps通道号:0

配置**using oc-12**或者**undo using**命令会设置接口为通道模式，并删除级联模式下创建的POS通道接口。

【举例】

\# 配置622Mbps高速CPOS2/4/0接口的工作模式为级联模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 using oc-12c

\# 配置622Mbps高速CPOS2/4/0接口的工作模式为通道模式。

Sysname-Cpos2/4/0 using oc-12

\# 配置2.5Gbps高速CPOS2/4/0接口的622Mbps通道的工作模式为级联模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 oc-12 1

Sysname-Cpos2/4/0-oc-12-1 using oc-12c

\# 配置2.5Gbps高速CPOS2/4/0接口的622Mbps通道的工作模式为通道模式。

Sysname-Cpos2/4/0-oc-12-1 undo using

**CPOS接口 \-- CPOS接口配置命令 \-- using oc-3/using oc-3c**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[using oc-3**]命令用来配置155Mbps高速CPOS接口或155Mbps通道的工作模式为通道模式。

**[using oc-3c**]命令用来配置155Mbps高速CPOS接口或155Mbps通道的工作模式为级联模式。

**[undo using**]命令用来恢复缺省情况。

【命令】

**[using**  { **oc-3** \| **oc-3c** }]

**[undo using**]

【缺省情况】

接口或通道工作在通道模式。

【视图】

155Mbps高速CPOS接口视图/155Mbps通道视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在155Mbps高速CPOS接口视图或者155Mbps通道视图下通过**using oc-3c**命令设置接口为级联模式后，系统会自动创建一个155Mbps的POS通道接口。POS通道接口的名称为：Pos接口编号 /622Mbps通道号/155Mbps通道号:0

配置**using oc-3**或者**undo using**命令会设置接口为通道模式，并删除级联模式下创建的POS通道接口。

【举例】

\# 配置155Mbps高速CPOS2/4/0接口的工作模式为级联模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 using oc-3c

\# 配置155Mbps高速CPOS2/4/0接口的工作模式为通道模式。

Sysname-Cpos2/4/0 using oc-3

\# 配置2.5Gbps高速CPOS2/4/0接口的155Mbps通道的工作模式为级联模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 oc-12 1

Sysname-Cpos2/4/0-oc-12-1 oc-3 1

Sysname-Cpos2/4/0-oc-12-1-oc-3-1 using oc-3c

\# 配置2.5Gbps高速CPOS2/4/0接口的155Mbps通道的工作模式为通道模式。

Sysname-Cpos2/4/0-oc-12-1-oc-3-1 undo using

**CPOS接口 \-- CPOS接口配置命令 \-- using oc-48/using oc-48c**

------------------------------------------------------------------------

![说明](CPOS接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[using oc-48**]命令用来配置2.5Gbps高速CPOS接口的工作模式为通道模式。

**[using oc-48c**]命令用来配置2.5Gbps高速CPOS接口的工作模式为级联模式。

**[undo using**]命令用来恢复缺省情况。

【命令】

**[using**  { **oc-48** \| **oc-48c** }]

**[undo using**]

【缺省情况】

接口工作在通道模式。

【视图】

2.5Gbps高速CPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过**using oc-48c**命令设置接口为级联模式后，系统会自动创建一个2.5Gbps的POS通道接口。POS通道接口的名称为：Pos接口编号:0。

配置**using oc-48**或者**undo using**命令会设置接口为通道模式，并删除级联模式下创建的POS通道接口。

【举例】

\# 配置2.5Gbps高速CPOS2/4/0接口的工作模式为级联模式。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 using oc-48c

\# 配置2.5Gbps高速CPOS2/4/0接口的工作模式为通道模式。

Sysname-Cpos2/4/0 using oc-48

**CPOS接口 \-- CPOS接口配置命令 \-- using t3**

------------------------------------------------------------------------

**[using t3**]命令用来创建非成帧模式的T3通道对应的串口。

**[undo using t3**]命令用来删除该串口。

【命令】

**[using t3 ***t3-number*]

**[undo using ***t3-number*]

【缺省情况】

未创建串口。

【视图】

CPOS接口视图/155Mbps通道视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t3-number*]：T3通道号，取值范围为1～3。

【使用指导】

·CPOS接口视图下，创建非成帧模式的T3通道对应的串口名称为Serial接口编号/T3通道号:0。

·155Mbps通道视图下，创建非成帧模式的T3通道对应的串口名称为Serial接口编号/155Mbps通道号/T3通道号:0。

【举例】

\# 在CPOS接口2/4/0下创建非成帧模式的T3通道1对应的串口。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 using t3 1

Sysname-Cpos2/4/0 interface serial 2/4/0/1:0

Sysname-Serial2/4/0/1:0

\# 在622Mbps高速CPOS接口2/4/0的155Mbps通道下创建非成帧模式的T3通道1对应的串口。

\<Sysname\> system-view

Sysname controller cpos 2/4/0

Sysname-Cpos2/4/0 oc-3 2

Sysname-Cpos2/4/0-oc-3-2 using t3 1

Sysname-Cpos2/4/0-oc-3-2 interface serial 2/4/0/2/1:0

Sysname-Serial2/4/0/2/1:0
