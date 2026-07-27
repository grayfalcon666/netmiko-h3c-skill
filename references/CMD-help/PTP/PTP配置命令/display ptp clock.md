<!-- CMD-INDEX
  display ptp clock                   | 任意视图             | L39
  display ptp corrections             | 任意视图             | L223
  display ptp foreign-masters-record  | 任意视图             | L285
  display ptp interface               | 任意视图             | L385
  display ptp parent                  | 任意视图             | L609
  display ptp statistics              | 任意视图             | L727
  display ptp time-property           | 任意视图             | L813
  ptp active force-state              | 系统视图             | L949
  ptp announce-interval               | 二层以太网接口视图/三层以太网接口视图 | L1001
  ptp announce-timeout                | 二层以太网接口视图/三层以太网接口视图 | L1061
  ptp asymmetry-correction            | 二层以太网接口视图/三层以太网接口视图 | L1123
  ptp clock-source                    | 系统视图             | L1183
  ptp clock-step                      | 二层以太网接口视图/三层以太网接口视图 | L1435
  ptp delay-mechanism                 | 二层以太网接口视图/三层以太网接口视图 | L1497
  ptp destination-mac                 | 二层以太网接口视图/三层以太网接口视图 | L1561
  ptp domain                          | 系统视图             | L1623
  ptp dscp                            | 二层以太网接口视图/三层以太网接口视图 | L1677
  ptp enable                          | 二层以太网接口视图/三层以太网接口视图 | L1741
  ptp force-state                     | 二层以太网接口视图/三层以太网接口视图 | L1813
  ptp min-delayreq-interval           | 二层以太网接口视图/三层以太网接口视图 | L1877
  ptp mode                            | 系统视图             | L1937
  ptp pdelay-req-interval             | 二层以太网接口视图/三层以太网接口视图 | L2001
  ptp port-mode                       | 二层以太网接口视图/三层以太网接口视图 | L2057
  ptp priority                        | 系统视图             | L2115
  ptp profile                         | 系统视图             | L2181
  ptp slave-only                      | 系统视图             | L2229
  ptp source                          | 系统视图             | L2285
  ptp syn-interval                    | 二层以太网接口视图/三层以太网接口视图 | L2347
  ptp tod                             | 系统视图             | L2407
  ptp transport-protocol              | 二层以太网接口视图/三层以太网接口视图 | L2473
  ptp unicast-destination             | 三层以太网接口视图        | L2531
  ptp utc                             | 系统视图             | L2595
  ptp utc offset                      | 系统视图             | L2655
  ptp vlan                            | 二层以太网接口视图        | L2709
  reset ptp statistics                | 用户视图             | L2767
-->

**PTP \-- PTP配置命令 \-- display ptp clock**

------------------------------------------------------------------------

**[display ptp clock**]命令用来显示设备的PTP时钟信息。

【命令】

**[display ptp clock**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

如果PTP profile和PTP mode没有指定，则显示信息为空。

【举例】

\# 显示设备的PTP时钟信息。

\<Sysname\> display ptp clock

PTP profile         : IEEE 1588 Version 2

PTP mode            : BC

Slave only          : No

Clock ID            : 000FE2-FFFE-FF0000

Clock type          : ToD1

 ToD direction  : In

 ToD delay time : 0 (ns)

Clock domain        : 0

Number of PTP ports : 2

Priority1     : 128

Priority2     : 128

Clock quality :

 Class                 : 248

 Accuracy              : 254

 Offset (log variance) : 65535

Offset from master : 0 (ns)

Mean path delay    : 0 (ns)

Steps removed      : 1

Local clock time   : Sun Jan 15 20:57:29 2011

表1-1 display ptp clock命令显示信息描述表

字段

描述

PTP profile

PTP协议遵循的标准：

·IEEE 1588 Version 2：PTP协议遵循IEEE1588 version 2标准

·IEEE 802.1AS：PTP协议遵循IEEE 802.1AS标准

PTP mode

时钟节点类型：

·BC：表示BC类型

·E2ETC：表示E2ETC类型

·E2ETC-OC：表示E2ETC+OC类型

·OC：表示OC类型

·P2PTC：表示P2PTC类型

·P2PTC-OC：表示P2PTC+OC类型

Slave only

OC的工作模式是否为Slave only：

·Yes：表示是

·No：表示不是

Clock ID

本设备的时钟编号

Clock type

本设备的时钟类型：

·Local：本地时钟

·ToD0：第一路ToD时钟

·ToD1：第二路ToD时钟

ToD direction

ToD时钟方向，取值为In。本设备的时钟类型为Local时，不显示该字段

 

ToD delay time

ToD时钟时延校正时间，单位为纳秒。本设备的时钟类型为Local时，不显示该字段

 

Clock domain

本设备所在的PTP域

Number of PTP ports

PTP接口的数量

Priority1

本设备上时钟优先级一的值

Priority2

本设备上时钟优先级二的值

Clock quality

时钟品质特性

Class

本设备上时钟的时间等级值

Accuracy

本设备上时钟的时间精度值

Offset (log variance)

最优时钟的偏差度量

Offset from master

与父节点的时钟偏差，单位为纳秒，N/A表示无意义

Mean path delay

平均路径延时，单位为纳秒，N/A表示无意义

Steps removed

最优时钟到本时钟节点的跳数，N/A表示无意义

Local clock time

当前的本地系统时间

**PTP \-- PTP配置命令 \-- display ptp corrections**

------------------------------------------------------------------------

**[display ptp corrections**]命令用来显示Slave端口时间校正的历史信息。

【命令】

**[display ptp corrections**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

当设备每通过Slave端口进行过一次时间/频率同步，就会记录一条对应信息，从而显示信息不为空，具体为：如果指定PTP profile和PTP mode，且设备存在Slave端口时，通过该Slave端口进行了时间同步，则显示信息不为空。若Slave端口更换，记录会被清空。

【举例】

\# 显示Slave端口时间校正的历史信息。

\<Sysname\> display ptp corrections

Slave port   Correction time          Corrections(s,ns)     Rate ratio

GE1/0/1      Mar 11 03:14:54 2012     0,74                  0.999999973

GE1/0/1      Mar 11 03:14:55 2012    -1,17                  0.999999980

表1-2 display ptp corrections命令显示信息描述表

字段

描述

Slave port

Slave端口名称

Correction time

时间偏差的校正时间

Corrections(s,ns)

时间偏差（秒，纳秒），N/A表示本次没有校正

Rate ratio

本端口与Master端口的频率比，N/A表示本次没有校正

**PTP \-- PTP配置命令 \-- display ptp foreign-masters-record**

------------------------------------------------------------------------

**[display ptp foreign-masters-record**]命令用来显示外部主节点的信息。

【命令】

**[display ptp foreign-masters-record ** **interface** *interface-type* *interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type* *interface-number*]：显示指定接口上的外部主节点信息，*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，将显示所有接口的外部主节点信息。

【使用指导】

在指定PTP profile为IEEE 1588 version 2，同时指定PTP mode，且设备存在Slave或Uncalibrated端口时，显示信息才不为空。

【举例】

\# 显示所有接口的外部主节点信息。

\<Sysname\> display ptp foreign-masters-record

P1=Priority1, P2=Priority2, C=Class, A=Accuracy,

OSLV=Offset-scaled-log-variance, SR=Steps-removed

GM=Grandmaster

\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-\-- \-\-\-\-\-\-\-\--

Interface    Clock ID             P1   P2   C    A    OSLV   SR   GM

\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-- \-\-\-\-- \-\-\-\-\-\-\-\--

GE1/0/1      000FE2-FFFE-FF0000   0    128  248  254  65535  0    Yes

GE1/0/2      000FE2-FFFE-FF0001   0    128  248  254  65535  1    No

表1-3 display ptp foreign-masters-record命令显示信息描述表

字段

描述

Interface

PTP接口的名称

Clock ID

外部主时钟节点的编号

P1

时钟优先级一的值

P2

时钟优先级二的值

C

时钟的时间等级值

A

时钟的时间精度值

OSLV

最优时钟的偏差度量

SR

最优时钟到该时钟节点的跳数

GM

最优时钟节点：

·Yes：表示该节点是最优时钟节点

·No：表示该节点不是最优时钟节点

**PTP \-- PTP配置命令 \-- display ptp interface**

------------------------------------------------------------------------

**[display ptp interface**]命令用来显示接口的PTP运行信息。

【命令】

**[display**[ **ptp** **interface** [ *interface-type* *interface-number* \| **brief** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type* *interface-number*]：详细显示指定接口的PTP运行信息，*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，将显示所有接口的PTP运行信息。

**[brief**]：简要显示所有接口的PTP运行信息。如果未指定本参数，将详细显示指定接口或所有接口的PTP运行信息。

【使用指导】

如果接口使能了PTP功能，则详细显示信息不为空。只有接口PTP功能实际工作时，简要显示信息才不为空。

【举例】

\# 简要显示所有接口的PTP运行信息。

\<Sysname\> display ptp interface brief

Name         State        Delay mechanism  Clock step  Asymmetry correction

GE1/0/1      Slave        E2E              Two         0

GE1/0/2      Passive      E2E              Two         0

\# 详细显示接口GigabitEthernet1/0/1的PTP运行信息。

\<Sysname\> display ptp interface gigabitethernet 1/0/1

Clock ID                    : 000FE2-FFFE-FF0000

Port number                 : 15

PTP version                 : 2

PTP enable                  : Enabled

Transport of PTP            : User Datagram Protocol (IPv4)

Unicast destination address : 10.10.10.2

DSCP priority               : 56

Port state                  : Slave

Force state                 : No

Clock step                  : Two

Asymmetry correction        : 0

Delay mechanism             : End to End

Announce interval (log mean)           : 1

Announce receipt time out              : 3

Sync interval (log mean)               : 2

Delay request interval (log mean)      : 2

Peer delay request interval (log mean) : 0

Mean path delay                        : 0 (ns)

表1-4 display ptp interface命令显示信息描述表

字段

描述

Name

PTP接口的名称

State

PTP接口的状态：

·Slave：接口状态为Slave，跟踪外部时间信息

·Uncalibrated：接口状态为Uncalibrated，Slave状态前的临时状态

·Passive：接口状态为Passive（端口收到对端的Announce报文后，计算出的状态），不跟踪外部时间信息，也不对外发布时间信息

·Master：接口状态为Master，对外发布时间信息

·Premaster：接口状态为Premaster，Master状态前的临时状态

·Listening：接口状态为Listening（端口初始化后，即进入Listening状态），不跟踪外部时间信息，也不对外发布时间信息

·Faulty：接口状态为Faulty，该状态为PTP协议的错误状态（即检测到错误），接口不处理PTP协议报文

·Disabled：接口状态为Disabled，接口上PTP协议未运行，接口不处理协议报文

·Initializing：接口状态为Initializing，接口位于初始化状态，接口不处理协议报文

·N/A：表示无意义

Delay mechanism

接口的延时测量机制：

·End to End：请求应答机制

·Peer to Peer：端延时机制

Clock step

时间戳的携带模式：

·One：表示单步模式

·Two：表示双步模式

Asymmetry correction

非对称延迟校正时间，单位为纳秒

Clock ID

接口所在设备的时钟编号

Port number

接口号

PTP version

PTP版本号：取值只能为2，表示PTP版本号为2

PTP enable

接口的PTP状态：

·Enabled：表示接口的PTP处于激活状态

·Disabled：表示接口的PTP处于未激活状态

Transport of PTP

PTP报文封装格式：

·User Datagram Protocol (IPv4)：PTP报文采用UDP（IPv4）封装格式

·IEEE 802.3/Ethernet：PTP报文采用IEEE 802.3/Ethernet封装格式

Unicast destination address

采用UDP（IPv4）封装格式的单播PTP报文的目的IP地址。未配置**ptp** **unicast-destination**命令，不显示该字段

 

DSCP priority

PTP报文封装格式为UDP（IPv4）时的DSCP优先级。未配置**ptp dscp**命令时，不显示该字段

 

VLAN

PTP报文的VLAN。未配置**ptp vlan**命令时，不显示该字段

 

Dot1p priority

PTP报文的802.1p优先级。未配置**ptp vlan**命令时，不显示该字段

 

Force state

是否配置强制状态生效：

·Yes：表示已配置

·No：表示未配置

Announce interval (log mean)

Announce报文的发送周期＝2*^value^*（单位为秒），本字段就是*value*的值

Announce receipt time out

Announce报文的接收超时倍数，在倍数的发送周期内，若未收到主节点的Announce报文，则认为主节点失效

Sync interval (log mean)

Sync报文的发送周期＝2*^value^*（单位为秒），本字段就是*value*的值

Delay request interval (log mean)

Delay_Req报文的最小发送间隔＝2*^value^*（单位为秒），本字段就是*value*的值

Peer delay request interval (log mean)

Pdelay_Req报文的发送周期＝2*^value^*（单位为秒），本字段就是*value*的值

Mean path delay

接口与对端的平均路径延时，单位为纳秒

**PTP \-- PTP配置命令 \-- display ptp parent**

------------------------------------------------------------------------

**[display ptp parent**]命令用来显示当前PTP设备父节点信息。

【命令】

**[display ptp parent**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

如果PTP profile和PTP mode没有指定、PTP mode指定为TC或配置了强制状态生效，则显示信息为空。

【举例】

\# 显示当前PTP设备父节点信息。

\<Sysname\> display ptp parent

Parent clock:

 Parent clock ID                         : 000FE2-FFFE-FF0005

 Parent port number                      : 15

 Observed parent offset (log variance)   : N/A

 Observed parent clock phase change rate : N/A

Grandmaster clock:

 Grandmaster clock ID: 000FE2-FFFE-FF0000

 Grandmaster clock quality:

  Class                 : 248

  Accuracy              : 254

  Offset (log variance) : 65535

  Priority1             : 128

  Priority2             : 128

表1-5 display ptp parent命令显示信息描述表

字段

描述

Parent clock

父时钟信息

Parent clock ID

父时钟的编号

Parent port number

父时钟节点的输出接口号

Observed parent offset (log variance)

父时钟节点的偏差度量，N/A表示无意义

Observed parent clock phase change rate

父时钟节点的相位变化比率，N/A表示无意义

Grandmaster clock

最优时钟节点信息

Grandmaster clock ID

最优时钟节点编号

Grandmaster clock quality

最优时钟节点品质特性

Class

最优时钟的时间等级值

Accuracy

最优时钟的时间精度值

Offset (log variance)

最优时钟的偏差度量

Priority1

最优时钟优先级一的值

Priority2

最优时钟优先级二的值

**PTP \-- PTP配置命令 \-- display ptp statistics**

------------------------------------------------------------------------

**[display ptp statistics**]命令用来显示PTP统计信息。

【命令】

**[display ptp statistics ** **interface** *interface-type* *interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type* *interface-number*]：显示指定接口上的PTP统计信息。*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，将显示所有接口的PTP统计信息。

【使用指导】

如果PTP profile和PTP mode没有指定，则显示信息为空。

【举例】

\# 显示接口GigabitEthernet1/0/1上的PTP统计信息。

\<Sysname\> display ptp statistics interface gigabitethernet 1/0/1

                     Received packets

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Announce :0          Sync      :0          Signaling          :0

DelayReq :0          DelayResp :0          FollowUp           :0

PdelayReq:0          PdelayResp:0          PdelayRespFollowUp :0

                     Sent packets

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Announce :476        Sync      :2543       Signaling          :0

DelayReq :0          DelayResp :0          FollowUp           :2542

PdelayReq:238        PdelayResp:0          PdelayRespFollowUp :0

                     Discarded packets

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Announce :0          Sync      :0          Signaling          :0

DelayReq :0          DelayResp :0          FollowUp           :0

PdelayReq:0          PdelayResp:0          PdelayRespFollowUp :0

表1-6 display ptp statistics命令显示信息描述表

字段

描述

Received packets

收到的PTP协议报文数量的统计信息

Sent packets

发出的PTP协议报文数量的统计信息

Discarded packets

丢弃的PTP协议报文数量的统计信息

**PTP \-- PTP配置命令 \-- display ptp time-property**

------------------------------------------------------------------------

**[display ptp time-property**]命令用来显示PTP时钟节点时间特性。

【命令】

**[display ptp time-property**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

如果PTP profile和PTP mode没有指定、PTP mode指定为TC或配置了强制状态生效，则显示信息为空。

【举例】

\# 显示PTP节点时间特性。

\<Sysname\> display ptp time-property

PTP clock time property:

 Current UTC offset valid : True

 Current UTC offset       : 33

 Leap59 : Yes

 Leap61 : No

 Time traceable      : True

 Frequency traceable : True

 PTP timescale       : True

 Time source         : 0xA0 (Internal oscillator)

表1-7 display ptp time-property命令显示信息描述表

字段

描述

PTP clock time property

PTP时钟节点时间特性

Current UTC offset valid

当前偏移量是否有效：

·True：有效

·False：无效

Current UTC offset

最优时钟的UTC时间相对于TAI时间的累计偏移量（单位为秒）

Leap59

是否对累计偏移量减一：

·Yes：表示是

·No：表示不是

Leap61

是否对累计偏移量加一：

·Yes：表示是

·No：表示不是

Time traceable

时间可跟踪性：

·Ture：PTP时间可跟踪

·False：PTP时间不可跟踪

Frequency traceable

频率可跟踪性：

·Ture：频率可跟踪

·False：频率不可跟踪

PTP timescale

PTP时间标识：

·True：PTP时间标识

·False：非PTP时间标识

Time source

最优时钟的属性值，代表的时钟类别包括：

·Atomic clock：原子时钟

·GPS：Global Positioning System，全球定位系统

·Handset：手持设备

·Internal oscillator：内部振荡器

·NTP：Network Time Protocol，网络时间协议

·Other：其他

·PTP：Precision Time Protocol，精确时间协议

·Terrestrial radio：陆基无线电

·Unknown：未知

**PTP \-- PTP配置命令 \-- ptp active force-state**

------------------------------------------------------------------------

**[ptp active force-state**]命令用来配置强制状态生效。

**[undo ptp active force-state**]命令用来恢复缺省情况。

【命令】

**[ptp** **active** **force-state**]

**[undo** **ptp** **active** **force-state**]

【缺省情况】

未配置强制状态生效功能。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 配置强制状态生效。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname ptp active force-state

【相关命令】

·**ptp** **profile**

·**ptp** **mode**

·**ptp force-state**

**PTP \-- PTP配置命令 \-- ptp announce-interval**

------------------------------------------------------------------------

**[ptp** **announce-interval**]命令用来配置Announce报文的发送周期。

**[undo** **ptp** **announce-interval**]命令用来恢复缺省情况。

【命令】

**[ptp** **announce-interval** *value*]

**[undo** **ptp** **announce-interval**]

【缺省情况】

不同PTP profile的缺省情况不同：

·当PTP profile为IEEE 1588 version 2时，Announce报文的发送周期为2（即2^1^）秒。

·当PTP profile为IEEE 802.1AS时，Announce报文的发送周期为1（即2^0^）秒。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：Announce报文的发送周期＝2*^value^*，单位为秒。当PTP profile为IEEE 1588 version 2时，*value*的取值范围为0～4；当PTP profile为IEEE 802.1AS时，*value*的取值范围为0～6。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 在接口GigabitEthernet1/0/1上配置Announce报文的发送周期为4（即2^2^）秒。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp announce-interval 2

【相关命令】

·**ptp profile**

·**ptp mode**

**PTP \-- PTP配置命令 \-- ptp announce-timeout**

------------------------------------------------------------------------

**[ptp** **announce-timeout**]命令用来配置Announce报文的接收超时倍数。

**[undo** **ptp** **announce-timeout**]命令用来恢复缺省情况。

【命令】

**[ptp** **announce-timeout** *multiple-value*]

**[undo** **ptp** **announce-timeout**]

【缺省情况】

Announce报文的接收超时倍数为3。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[multiple-value*]：表示Announce报文的接收超时倍数，取值范围为2～10。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·主节点会周期性地发送Announce报文给从节点，当PTP profile为IEEE 1588 version 2时，如果从节点在本端配置的Announce报文发送周期的*multiple-value*倍时间之内未收到主节点发来的Announce报文，便认为该主节点失效；当PTP profile为IEEE 802.1AS时，如果从节点在对端配置的Announce报文发送周期的*multiple-value*倍时间之内未收到主节点发来的Announce报文，便认为该主节点失效。

·为了保证PTP网络的稳定，请根据网络环境配置合理的值。一般情况下，建议将Announce报文的接收超时倍数配置为5～7。

【举例】

\# 在接口GigabitEthernet1/0/1上配置Announce报文的接收超时倍数为5。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp announce-timeout 5

【相关命令】

·**ptp announce-interval**

·**ptp mode**

·**ptp profile**

**PTP \-- PTP配置命令 \-- ptp asymmetry-correction**

------------------------------------------------------------------------

**[ptp** **asymmetry-correction**]命令用来配置非对称延迟校正时间。

**[undo** **ptp** **asymmetry-correction**]命令用来恢复缺省情况。

【命令】

**[ptp**[ **asymmetry-correction** { **minus** \| **plus** } *value*]]

**[undo** **ptp** **asymmetry-correction**]

【缺省情况】

接口的非对称延迟校正时间为0纳秒，即不进行校正。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[minus**]：表示进行负的非对称延迟校正。

**[plus**]：表示进行正的非对称延迟校正。

*[value*]：表示非对称延迟的校正时间值，取值范围为0～2000000，单位为纳秒。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 在接口GigabitEthernet1/0/1上配置非对称延迟的校正时间100纳秒。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp asymmetry-correction plus 100

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp clock-source**

------------------------------------------------------------------------

**[ptp clock-source**]命令用来配置外接ToD时钟源的相关参数。

**[undo ptp clock-source**]命令用来恢复缺省情况。

【命令】

**[ptp clock-source **[{ **tod0** \| **tod1** }  { **accuracy** *acc-value* \| **class** *class-value* \| **time-source** *ts-value* }]]

**[undo ptp clock-source **[{ **tod0** \| **tod1** }  { **accuracy** \| **class** \| **time-source** }]]

【缺省情况】

外接ToD时钟源的时间精度值为32，时间等级值为6，属性值为32。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tod0**]：表示配置第一路外接ToD时钟源的参数。

**[tod1**]：表示配置第二路外接ToD时钟源的参数。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[accuracy** *acc-value*]：表示时钟的时间精度。*acc-value*为时间精度值，取值范围为0～255，数值越小精度越高，具体取值及其含义如[表]1-8(?1715489589#_Ref268612052)所示。

表1-8 时间精度值及其含义

时间精度值（十六进制）

含义

00～1F

Reserved（保留）

20

时间精确到25纳秒（1纳秒＝10^-9^秒）以内

21

时间精确到100纳秒以内

22

时间精确到250纳秒以内

23

时间精确到1微秒（1微秒＝10^-6^秒）以内

24

时间精确到2.5微秒以内

25

时间精确到10微秒以内

26

时间精确到25微秒以内

27

时间精确到100微秒以内

28

时间精确到250微秒以内

29

时间精确到1毫秒（1毫秒＝10^-3^秒）以内

2A

时间精确到2.5毫秒以内

2B

时间精确到10毫秒以内

2C

时间精确到25毫秒以内

2D

时间精确到100毫秒以内

2E

时间精确到250毫秒以内

2F

时间精确到1秒以内

30

时间精确到10秒以内

31

时间精确到大于10秒

32～7F

Reserved（保留）

80～FD

For use by alternate PTP profiles（为PTP profile预留）

FE

Unknown（未知）

FF

Reserved（保留）

**[class** *class-value*]：表示时钟的时间等级。*class-value*为时间等级值，取值范围为0～255，数值越小等级越高，具体取值及其含义如[表]1-9(?1715489589#_Ref268612094)所示（未列出的取值均被协议所保留）。

表1-9 时间等级值及其含义

时间等级值（十进制）

含义

6

表示与主参考时间源保持同步的时钟节点，由PTP来分配时间表。时间等级值为6的时钟节点不可成为该域中其他时钟的从时钟

7

表示先前时间等级值为6、但已无法与特定用途时间源保持同步的时钟节点，已进入续任模式且满足续任条件的时钟节点，由PTP来分配时间表。时间等级值为7的时钟节点不可成为该域中其他时钟的从时钟

13

表示与特定用途的时间源保持同步的时钟节点，由ARB来分配时间表。时间等级值为13的时钟节点不可成为该域中其他时钟的从时钟

14

表示先前时间等级值为13、但已无法与特定用途时间源保持同步的时钟节点，已进入续任模式且满足续任条件的时钟节点，由ARB来分配时间表。时间等级值为14的时钟节点不可成为该域中其他时钟的从时钟

52

表示时间等级值为7的时钟节点由于不满足续任条件而降级为备选时钟A。时间等级值为52的时钟节点不可成为该域中其他时钟的从时钟

58

表示时间等级值为14的时钟节点由于不满足续任条件而降级为备选时钟A。时间等级值为58的时钟节点不可成为该域中其他时钟的从时钟

187

表示时间等级值为7的时钟节点由于不满足续任条件而降级为备选时钟B。时间等级值为187的时钟节点可成为该域中其他时钟的从时钟

193

表示时间等级值为14的时钟节点由于不满足续任条件而降级为备选时钟B。时间等级值为193的时钟节点可成为该域中其他时钟的从时钟

248

时间等级值的缺省取值

255

表示工作模式为Slave-only的时钟节点

**[time-source** *ts-value*]：表示时钟的属性。*ts-value*为属性值，取值范围为0～255，具体取值及其含义如[表]1-10(?1715489589#_Ref268612150)所示（未列出的取值均被协议所保留）。

表1-10 属性值及其含义

属性值（十六进制）

含义

10

Atomic clock（原子时钟）

20

GPS（Global Positioning System，全球定位系统）

30

Terrestrial radio（陆基无线电）

40

PTP（Precision Time Protocol，精确时间协议）

50

NTP（Network Time Protocol，网络时间协议）

60

Handset（手持设备）

90

Other（其他）

A0

Internal oscillator（内部振荡器）

F0～FE

For use by alternate PTP profiles（为PTP profile预留）

FF

Reserved（保留）

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 配置第一路外接ToD时钟源的时间精度值为44。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname ptp clock-source tod0 accuracy 44

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp clock-step**

------------------------------------------------------------------------

**[ptp** **clock-step**]命令用来[配置时间戳的携带模式。]

**[undo** **ptp** **clock-step**]命令用来恢复缺省情况。

【命令】

**[ptp**[ **clock-step** { **one-step** \| **two-step** }]]

**[undo** **ptp** **clock-step**]

【缺省情况】

时间戳的携带模式为双步模式。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[one-step**]：表示时间戳的携带模式为单步模式。

**[two-step**]：表示时间戳的携带模式为双步模式。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·当profile为IEEE 802.1AS时，只支持双步模式。

·当mode为E2ETC、P2PTC、E2ETC+OC或P2PTC+OC时，只支持双步模式。

【举例】

\# 在接口GigabitEthernet1/0/1上配置时间戳的携带模式为双步模式。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp clock-step two-step

【相关命令】

·**ptp mode**

·**ptp profile**

**PTP \-- PTP配置命令 \-- ptp delay-mechanism**

------------------------------------------------------------------------

**[ptp** **delay-mechanism**]命令用来配置BC或OC的延时测量机制。

**[undo** **ptp** **delay-mechanism**]命令用来恢复缺省情况。

【命令】

**[ptp**[ **delay-mechanism** { **e2e** \| **p2p** }]]

**[undo** **ptp** **delay-mechanism**]

【缺省情况】

不同PTP profile的缺省情况不同：

·当profile为IEEE 1588 version 2时，缺省延时测量机制为请求应答机制。

·当profile为IEEE 802.1AS时，缺省延时测量机制为端延时机制。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[e2e**]：表示E2ETC所使用的请求应答机制。

**[p2p**]：表示P2PTC所使用的端延时机制。

【使用指导】

·只有当设备的时钟节点类型为BC或OC时，才允许配置该命令。

·当profile为IEEE 802.1AS时，只支持端延时机制，不允许配置该命令。

【举例】

\# 配置设备的时钟节点类型为OC，并在接口GigabitEthernet1/0/1上配置延时测量机制为请求应答机制。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp delay-mechanism e2e

【相关命令】

·**ptp profile**

·**ptp mode**

**PTP \-- PTP配置命令 \-- ptp destination-mac**

------------------------------------------------------------------------

**[ptp** **destination-mac**]命令用来配置非Pdelay报文的目的MAC地址。

**[undo** **ptp** **destination-mac**]命令用来恢复缺省情况。

【命令】

**[ptp** **destination-mac** *mac-address*]

**[undo** **ptp** **destination-mac**]

【缺省情况】

非Pdelay报文的目的MAC地址为011B-1900-0000。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：表示非Pdelay报文的目的MAC地址，取值为0180-C200-000E或011B-1900-0000。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·Pdelay报文（包括Pdelay_Req、Pdelay_Resp、Pdelay_Resp_Follow_Up等）默认的目的MAC地址为0180-C200-000E，不可修改。

·当profile为IEEE 802.1AS时，不允许配置该命令。

·该命令在PTP报文采用IEEE 802.3/Ethernet封装格式时才生效。

【举例】

\# 在接口GigabitEthernet1/0/1上配置非Pdelay报文的目的MAC地址为0180-C200-000E。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp destination-mac 0180-c200-000e

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp domain**

------------------------------------------------------------------------

**[ptp** **domain**]命令用来配置设备所属的PTP域。

**[undo ptp** **domain**]命令用来恢复缺省情况。

【命令】

**[ptp** **domain** *domain-number*]

**[undo** **ptp** **domain**]

【缺省情况】

PTP设备缺省属于域0。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-number*]：表示设备加入的PTP域，*domain-number*的取值范围为0～255。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 配置设备所属的PTP域为2。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname ptp domain 2

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp dscp**

------------------------------------------------------------------------

**[ptp dscp**]命令用来配置PTP报文封装格式为UDP（IPv4）时的DSCP优先级。

**[undo ptp dscp**]命令用来恢复缺省情况。

【命令】

**[ptp dscp***dscp*]

**[undo ptp dscp**]

【缺省情况】

PTP报文封装格式为UDP（IPv4）时的DSCP优先级为56。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp*]：DSCP优先级，取值范围为0～63。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·当profile为IEEE 802.1AS时，不允许配置该命令。

·只有当PTP报文封装格式为UDP（IPv4）时，该命令才生效。

【举例】

\# 在接口GigabitEthernet1/0/1上配置PTP报文封装格式为UDP（IPv4）时的DSCP优先级为63。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp transport-protocol udp

Sysname-GigabitEthernet1/0/1 ptp dscp 63

【相关命令】

·**ptp** **profile**

·**ptp mode**

·**ptp transport-protocol**

**PTP \-- PTP配置命令 \-- ptp enable**

------------------------------------------------------------------------

**[ptp** **enable**]命令用来使能接口的PTP功能。

**[undo** **ptp** **enable**]命令用来关闭接口的PTP功能。

【命令】

**[ptp** **enable**]

**[undo** **ptp** **enable**]

【缺省情况】

接口的PTP功能处于关闭状态。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·当设备时钟节点类型为OC时，只允许在一个接口上使能PTP功能。

·建议在完成PTP相关参数配置后，再在接口上使能PTP功能。

【举例】

\# 配置设备的时钟节点类型为OC，并在接口GigabitEthernet1/0/1上使能PTP功能。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp enable

\# 配置设备的时钟节点类型为E2ETC，并在接口GigabitEthernet1/0/1和GigabitEthernet1/0/2上使能PTP功能。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode e2etc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp enable

Sysname-GigabitEthernet1/0/1 interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 ptp enable

【相关命令】

·**ptp** **mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp force-state**

------------------------------------------------------------------------

**[ptp force-state**]命令用来[配置]PTP接口的强制角色。

**[undo** **ptp** **force-state**]命令用来恢复缺省情况。

【命令】

**[ptp force-state**[ { **master** \| **passive** \| **slave** }]]

**[undo** **ptp** **force-state**]

【缺省情况】

PTP接口的角色由BMC算法自动生成。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[master**]：表示PTP接口的角色为Master端口。

**[passive**]：表示PTP接口的角色为Passive端口。

**[slave**]：表示PTP接口的角色为Slave端口。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·一台设备上最多只允许配置一个Slave端口。

【举例】

\# 配置设备的时钟节点类型为OC，并配置PTP接口GigabitEthernet1/0/1的强制角色为Slave端口。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp force-state slave

【相关命令】

·**ptp mode**

·**ptp profile**

·**ptp slave-only**

**PTP \-- PTP配置命令 \-- ptp min-delayreq-interval**

------------------------------------------------------------------------

**[ptp** **min-delayreq-interval**]命令用来配置Delay_Req报文的最小发送间隔。

**[undo** **ptp** **min-delayreq-interval**]命令用来恢复缺省情况。

【命令】

**[ptp** **min-delayreq-interval** *value*]

**[undo** **ptp** **min-delayreq-interval**]

【缺省情况】

不同PTP profile的缺省情况不同：

·当profile为IEEE 1588 version 2时，Delay_Req报文的最小发送间隔为1（即2^0^）秒。

·当profile为IEEE 802.1AS时，不允许配置该命令。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：Delay_Req报文的最小发送间隔＝2*^value^*，单位为秒，*value*的取值范围为-4～6。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 在接口GigabitEthernet1/0/1上配置Delay_Req报文的最小发送间隔为4（即2^2^）秒。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp min-delayreq-interval 2

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp mode**

------------------------------------------------------------------------

**[ptp** **mode**]命令用来配置设备的时钟节点类型。

**[undo** **ptp** **mode**]命令用来恢复缺省情况。

【命令】

**[ptp**[ **mode** { **bc** \| **e2etc** \| **e2etc-oc** \| **oc** \| **p2ptc** \| **p2ptc-oc** }]]

**[undo** **ptp** **mode**]

【缺省情况】

设备上没有配置任何时钟节点类型。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bc**]：表示时钟节点类型为BC（Boundary Clock，边界时钟）。

**[e2etc**]：表示时钟节点类型为E2ETC（End-to-End Transparent Clock，端到端透明时钟）。

**[e2etc-oc**]：表示时钟节点类型为E2ETC+OC（端到端透明时钟与普通时钟混合）。

**[oc**]：表示时钟节点类型为OC（Ordinary Clock，普通时钟）。

**[p2ptc**]：表示时钟节点类型为P2PTC（Peer-to-Peer Transparent Clock，点到点透明时钟）。

**[p2ptc-oc**]：表示时钟节点类型为P2PTC+OC（点到点透明时钟与普通时钟混合）。

【使用指导】

·必须先配置PTP profile后，才允许配置该命令。

·当profile为IEEE 802.1AS时，不允许配置为E2ETC或E2ETC+OC类型。

·改变设备的时钟节点类型，会清空除profile类型外的所有配置。

【举例】

\# 配置设备的时钟节点类型为OC。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

【相关命令】

·**ptp profile**

**PTP \-- PTP配置命令 \-- ptp pdelay-req-interval**

------------------------------------------------------------------------

**[ptp pdelay-req-interval**]命令用来配置Pdelay_Req报文的发送周期。

**[undo** **ptp** **pdelay-req-interval**]命令用来恢复缺省情况。

【命令】

**[ptp** **pdelay-req-interval** *value*]

**[undo** **ptp** **pdelay-req-interval**]

【缺省情况】

Pdelay_Req报文的发送周期为1（即2^0^）秒。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：Pdelay_Req报文的发送周期＝2*^value^*，单位为秒，*value*的取值范围为-4～6。当profile为IEEE 1588 version 2时，*value*的取值范围为0～5。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 在接口GigabitEthernet1/0/1上配置Pdelay_Req报文的发送周期为4（即2^2^）秒。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp pdelay-req-interval 2

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp port-mode**

------------------------------------------------------------------------

**[ptp** **port-mode**]命令用来配置TC+OC（包括E2ETC+OC和P2PTC+OC）的接口类型为OC。

**[undo ptp** **port-mode**]命令用来恢复缺省情况。

【命令】

**[ptp** **port-mode** **oc**]

**[undo** **ptp** **port-mode**]

【缺省情况】

E2ETC+OC和P2PTC+OC上各接口的类型都为TC。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[oc**]：表示TC+OC的接口类型为OC。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·只有当设备的时钟节点类型为E2ETC+OC或P2PTC+OC时才允许配置该命令。

【举例】

\# 配置设备的时钟节点类型为P2PTC+OC，并配置接口GigabitEthernet1/0/1的类型为OC。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode p2ptc-oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp port-mode oc

【相关命令】

·**ptp** **mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp priority**

------------------------------------------------------------------------

**[ptp** **priority** **clock-source**]命令用来配置时钟参与BMC算法的优先级参数。

**[undo ptp** **priority** **clock-source**]命令用来恢复缺省情况。

【命令】

**[ptp**[ **priority** **clock-source** { **local** \| **tod0** \| **tod1** } { **priority1** *pri1-value* \| **priority2** *pri2-value* }]]

**[undo**[ **ptp** **priority** **clock-source** { **local** \| **tod0** \| **tod1** } { **priority1** \| **priority2** }]]

【缺省情况】

不同PTP profile的缺省情况不同：

·当profile为IEEE 1588 version 2时，时钟优先级一、二的缺省值均为128。

·当profile为IEEE 802.1AS时，时钟优先级一的缺省值均为246，时钟优先级二的缺省值均为248。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：表示配置本地时钟的优先级参数。

**[tod0**]：表示配置第一路ToD时钟的优先级参数。

**[tod1**]：表示配置第二路ToD时钟的优先级参数。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[priority1** *pri1-value*]：表示时钟的优先级一。*pri1-value*为优先级一的值，取值范围为0～255，数值越小优先级越高。

**[priority2** *pri2-value*]：表示时钟的优先级二。*pri2-value*为优先级二的值，取值范围为0～255，数值越小优先级越高。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 配置本地时钟的优先级一值为10。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname ptp priority clock-source local priority1 10

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp profile**

------------------------------------------------------------------------

**[ptp profile**]命令用来配置设备采用的PTP协议标准。

**[undo ptp profile**]命令用来恢复缺省情况。

【命令】

**[ptp**[ **profile** { **1588v2** \| **8021as** }]]

**[undo** **ptp** **profile**]

【缺省情况】

未配置设备采用的PTP协议标准，PTP协议不运行。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[1588v2**]：表示采用的PTP协议标准为IEEE 1588 version 2。

**[8021as**]：表示采用的PTP协议标准为IEEE 802.1AS。

【使用指导】

·必须首先配置设备支持的PTP协议标准，否则不允许执行其他PTP配置命令。

·当改变或取消设备采用的PTP协议标准时，PTP功能不工作，将会清空用户在之前PTP协议标准下的所有PTP配置。

【举例】

\# 配置设备采用的PTP协议标准为IEEE 1588 version 2。

\<Sysname\> system-view

Sysname ptp profile 1588v2

**PTP \-- PTP配置命令 \-- ptp slave-only**

------------------------------------------------------------------------

**[ptp** **slave-only**]命令用来配置OC的工作模式为Slave-only，即OC只能作为从时钟。

**[undo** **ptp** **slave-only**]命令用来恢复缺省情况。

【命令】

**[ptp** **slave-only**]

**[undo** **ptp** **slave-only**]

【缺省情况】

OC的工作模式不是Slave-only，即OC既可作为主时钟也可作为从时钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·只有当设备的时钟节点类型为OC时，才允许配置该命令。

·当OC的工作模式为Slave-only时，也允许将其PTP接口强制配置为Master端口或Passive端口，通过**ptp force-state**命令进行生效配置。

【举例】

\# 配置设备的时钟节点类型为OC，并配置其工作模式为Slave-only。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname ptp slave-only

【相关命令】

·**ptp force-state**

·**ptp** **mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp source**

------------------------------------------------------------------------

**[ptp** **source**]命令用来配置采用UDP（IPv4）封装格式的组播PTP报文的源IP地址。

**[undo ptp** **source**]命令用来恢复缺省情况。

【命令】

**[ptp** **source** *ip-address* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **ptp** **source** *ip-address* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

未配置采用UDP（IPv4）封装格式的组播PTP报文的源IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：表示采用UDP（IPv4）封装格式的组播PTP报文的源IP地址。

**[vpn-instance ***vpn-instance-name*]：指定本端设备和对端设备通信时使用的VPN，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示对端设备位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·当profile为IEEE 802.1AS时，不允许配置该命令。

·该命令在PTP报文采用UDP（IPv4）封装格式时才生效。

【举例】

\# 配置采用UDP（IPv4）封装格式的组播PTP报文的源IP地址为3.5.1.5。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname ptp source 3.5.1.5

【相关命令】

·**ptp mode**

·**ptp profile**

·**ptp transport-protocol**

**PTP \-- PTP配置命令 \-- ptp syn-interval**

------------------------------------------------------------------------

**[ptp** **syn-interval**]命令用来配置Sync报文的发送周期。

**[undo ptp** **syn-interval**]命令用来恢复缺省情况。

【命令】

**[ptp** **syn-interval** *value*]

**[undo** **ptp** **syn-interval**]

【缺省情况】

不同PTP profile的缺省情况不同：

·当profile为IEEE 1588 version 2时，Sync报文的发送周期为1（即2^0^）秒。

·当profile为IEEE 802.1AS时，Sync报文的发送周期为1/8（即2^-3^）秒。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：Sync报文的发送周期＝2*^value^*，单位为秒，当profile为IEEE 802.1AS时，*value*的取值范围为-4～6；当profile为IEEE 1588 version 2时，*value*的取值范围为-1～1。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 在接口GigabitEthernet1/0/1上配置Sync报文的发送周期为2（即2^1^）秒。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp syn-interval 1

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp tod**

------------------------------------------------------------------------

**[ptp tod**]命令用来配置ToD时钟信号的方向和收发时延校正时间。

**[undo **]**ptp tod**命令用来恢复缺省情况。

【命令】

**[ptp ** { **tod0** \| **tod1** } { **input** [ **delay** *input-delay-time* ] \| **output**  **delay** *output-delay-time*  }]

**[undo ptp ** { **tod0** \| **tod1** } { **input** \| **output** }]

【缺省情况】

ToD时钟信号方向为入方向，收发时延校正时间为[0]纳秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tod0**]：第一路ToD时钟。

**[tod1**]：第二路ToD时钟。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。

**[input**]：时钟信号方向为入方向，即此时设备接收外部时间信号。

*[input-delay-time*]：ToD时钟信号的接收延迟校正时间，单位为纳秒，取值范围与设备的型号有关，请以设备的实际情况为准。

**[output**]：时钟信号方向为出方向，即此时设备向外提供时间信号。

*[output-delay-time*]：ToD时钟信号的发送延迟校正时间，单位为纳秒，取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 配置PTP第一路ToD时钟信号为入方向、接收时延校正时间为1000纳秒，第二路ToD时钟信号为出方向、发送时延校正时间为100纳秒。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname ptp tod0 input delay 1000

Sysname ptp tod1 output delay 100

【相关命令】

·**ptp** **profile**

·**ptp mode**

**PTP \-- PTP配置命令 \-- ptp transport-protocol**

------------------------------------------------------------------------

**[ptp** **transport-protocol**]命令用来配置当前接口的PTP报文封装格式为UDP（IPv4）格式。

**[undo ptp** **transport-protocol**]命令用来恢复缺省情况。

【命令】

**[ptp** **transport-protocol udp**]

**[undo** **ptp** **transport-protocol**]

【缺省情况】

PTP报文的封装格式为IEEE 802.3/Ethernet格式。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[udp**]：表示配置接口下PTP报文的封装格式为UDP（IPv4）。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·当profile为IEEE 802.1AS时，不允许配置该命令。

【举例】

\# 配置接口GigabitEthernet1/0/1的PTP报文封装格式为UDP（IPv4）格式。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp transport-protocol udp

【相关命令】

·**ptp mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp unicast-destination**

------------------------------------------------------------------------

**[ptp** **unicast-destination**]命令用来配置采用UDP（IPv4）封装格式的单播PTP报文的目的IP地址。

**[undo** **ptp** **unicast-destination**]命令用来恢复缺省情况。

【命令】

**[ptp** **unicast-destination** *ip-address*]

**[undo** **ptp** **unicast-destination** *ip-address*]

【缺省情况】

未配置采用UDP（IPv4）封装格式的单播PTP报文的目的IP地址。

【视图】

三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：表示采用UDP（IPv4）封装格式的单播PTP报文的目的IP地址。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·当profile为IEEE 802.1AS时，不允许配置该命令。

·该命令在PTP报文采用UDP（IPv4）封装格式时才生效。

【举例】

\# 在接口GigabitEthernet1/0/1上配置采用UDP（IPv4）封装格式的单播PTP报文的目的IP地址为10.10.10.2。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp transport-protocol udp

Sysname-GigabitEthernet1/0/1 ptp unicast-destination 10.10.10.2

【相关命令】

·**ptp** **profile**

·**ptp mode**

·**ptp transport-protocol**

**PTP \-- PTP配置命令 \-- ptp utc**

------------------------------------------------------------------------

**[ptp** **utc**]命令用来配置UTC的校正日期。

**[undo** **ptp** **utc**]命令用来恢复缺省情况。

【命令】

**[ptp**[ **utc** { **leap59-date** \| **leap61-date** } *date*]]

**[undo**[ **ptp** **utc** { **leap59-date** \| **leap61-date** }]]

【缺省情况】

没有配置UTC的校正日期。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[leap59-date**]：表示在指定日期的最后一分钟（23点59分）对当前设备的UTC进行校正，使其比TAI慢一秒。

**[leap61-date**]：表示在指定日期的最后一分钟（23点59分）对当前设备的UTC进行校正，使其比TAI快一秒。

*[date*]：表示指定日期，格式为YYYY/MM/DD。YYYY表示年，取值范围为2000～2035；MM表示月，取值范围为1～12；DD表示日，取值范围取决于所输入的月份。指定日期请不要早于系统的当前日期，否则配置将不会生效。

【使用指导】

·必须先配置PTP profile和PTP mode后，才允许配置该命令。

·leap59和leap61的配置不能够同时存在，后配置的会覆盖前面的配置。

【举例】

\# 假设系统的当前日期为2010年8月8日，配置设备的时钟节点类型为BC，并指定在2010年12月31日的最后一分钟对当前设备的UTC进行校正，使其比TAI慢一秒。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode bc

Sysname ptp utc leap59-date 2010/12/31

【相关命令】

·**ptp** **mode**

·**ptp** **profile**

**PTP \-- PTP配置命令 \-- ptp utc offset**

------------------------------------------------------------------------

**[ptp** **utc** **offset**]命令用来配置UTC相对于TAI的累计偏移量。

**[undo ptp** **utc** **offset**]命令用来恢复缺省情况。

【命令】

**[ptp** **utc** **offset** *utc-offset*]

**[undo** **ptp** **utc** **offset**]

【缺省情况】

UTC相对于TAI的累计偏移量为0秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[utc-offset*]：表示当前设备的UTC相对于TAI的累计偏移量，单位为秒，取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 配置UTC相对于TAI的累计偏移量为33秒。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname ptp utc offset 33

【相关命令】

·**ptp mode**

·**ptp profile**

**PTP \-- PTP配置命令 \-- ptp vlan**

------------------------------------------------------------------------

**[ptp vlan**]命令用来配置PTP报文的VLAN Tag。

**[undo **]**ptp vlan**命令用来恢复缺省情况。

【命令】

**[ptp vlan **]*vlan-id***** **dot1p** *dot1p-value*

**[undo ptp vlan **] **dot1p**

【缺省情况】

PTP报文不带VLAN Tag。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan**]* vlan-id*：VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[dot1p **]*dot1p-value*：802.1p优先级，取值范围为0～7。如果未指定本参数，表示802.1p优先级为7，即最高优先级。

【使用指导】

必须先配置PTP profile和PTP mode后，才允许配置该命令。

【举例】

\# 在接口GigabitEthernet1/0/1上配置PTP报文的VLAN ID为2、802.1p优先级为6。

\<Sysname\> system-view

Sysname ptp profile 1588v2

Sysname ptp mode oc

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp vlan 2 dot1p 6

【相关命令】

·**ptp** **profile**

·**ptp mode**

**PTP \-- PTP配置命令 \-- reset ptp statistics**

------------------------------------------------------------------------

**[reset** **ptp statistics**]命令用来清除PTP的统计信息。

【命令】

**[reset** **ptp** **statistics** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：清除指定接口上的统计信息。*interface-type* *interface-number*表示接口类型和接口编号。若未指定接口类型和接口编号，将清除所有接口上的统计信息。

【举例】

\# 清除接口GigabitEthernet1/0/1上PTP的统计信息。

\<Sysname\>reset ptp statistics interface gigabitethernet 1/0/1

【相关命令】

·**display ptp statistics**

