<!-- CMD-INDEX
  auto-connect enable                 | POS应用模板视图        | L54
  backup app                          | POS应用模板视图        | L104
  caller-number enable                | POS应用模板视图        | L162
  description                         | POS应用模板视图        | L212
  display fcm statistics              | 任意视图             | L254
  display posa connection terminal    | 任意视图             | L330
  display posa statistics app         | 任意视图             | L466
  display posa statistics terminal    | 任意视图             | L552
  display posa status app             | 任意视图             | L646
  display posa status terminal        | 任意视图             | L764
  hello enable                        | POS应用模板视图        | L858
  ip                                  | POS应用模板视图        | L914
  mode                                | POS应用模板视图        | L972
  negotiation hookoff                 | FCM接口视图          | L1032
  negotiation no-carrier-detect retry | FCM接口视图          | L1074
  negotiation scramble-binary1        | FCM接口视图          | L1116
  negotiation silence                 | FCM接口视图          | L1158
  negotiation unscramble-binary1      | FCM接口视图          | L1208
  posa app                            | 系统视图             | L1250
  posa auto-stop-service enable       | 系统视图             | L1318
  posa bind app                       | 异步接口视图/同异步接口视图   | L1362
  posa bind terminal                  | 异步接口视图/同异步接口视图/物理AM接口视图/物理FCM接口视图 | L1434
  posa bind terminal first-terminal-id | 通道化AM接口视图/通道化FCM接口视图 | L1496
  posa connection-threshold terminal  | 系统视图             | L1564
  posa fcm                            | 系统视图             | L1616
  posa map                            | ]                | L1672
  posa server enable                  | 系统视图             | L1744
  posa statistics caller-id           | 系统视图             | L1788
  posa statistics caller-ip           | 系统视图             | L1836
  posa terminal                       | 系统视图             | L1888
  posa terminal description           | 系统视图             | L1946
  posa tpdu-replace                   | 系统视图             | L1996
  posa trade-limit tcp                | 系统视图             | L2062
  posa trade-timeout                  | 系统视图             | L2112
  reset fcm statistics                | 用户视图             | L2158
  reset posa connection terminal      | 用户视图             | L2192
  reset posa statistics               | 用户视图             | L2236
  snmp-agent trap enable posa         | 系统视图             | L2280
  source ip                           | POS应用模板视图        | L2348
  source port                         | POS应用模板视图        | L2398
  tcp keepalive                       | POS应用模板视图        | L2454
  tcp linking-time                    | POS应用模板视图        | L2504
  threshold answer-tone               | FCM接口视图          | L2554
  threshold rlsdoff                   | FCM接口视图          | L2596
  threshold rlsdon                    | FCM接口视图          | L2638
  threshold txpower                   | FCM接口视图          | L2680
  timer auto-connect                  | POS应用模板视图        | L2722
  timer hello                         | POS应用模板视图        | L2774
  timer quiet                         | POS应用模板视图        | L2824
  tpdu-change                         | POS应用模板视图        | L2876
-->

**POS终端接入 \-- POS终端接入配置命令 \-- auto-connect enable**

------------------------------------------------------------------------

**[auto-connect enable**]命令用来开启自动建立连接功能，即POS接入设备自动为长连接模式的POS应用模板建立与前置机之间的TCP连接。

**[undo auto-connect** **enable**]命令用来恢复缺省情况。

【命令】

**[auto-connect enable**]

**[undo auto-connect enable**]

【缺省情况】

POS应用模板自动建立连接功能处于关闭状态。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有长连接模式的TCP类型的POS应用模板才支持该配置，配置后POS应用模板会立即向前置机发起连接，该连接建立后只能用于非透传模式下的TCP长连接复用。

当POS应用模板的连接模式由短连接修改为长连接时，POS接入设备会立即向前置机发起连接。

【举例】

\# 开启长连接模式的POS应用模板1的自动建立连接功能。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 auto-connect enable

【相关命令】

·**posa server enable**

·**timer auto-connect**

**POS终端接入 \-- POS终端接入配置命令 \-- backup app**

------------------------------------------------------------------------

**[backup app**]命令用来配置备份POS应用模板。

**[undo backup app**]用来取消备份POS应用模板。

【命令】

**[backup app ***app-id*]

**[undo backup app**]

【缺省情况】

未配置备份POS应用模板ID。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[app-id*]：备份应用ID，取值范围为1～1024。

【使用指导】

POS交易时，若某POS应用模板对应的前置机不可达，则向其备份POS应用模板对应的前置机发起连接。仅TCP类型的POS应用模板支持备份POS应用模板。

若指定的APP不存在或者APP类型不是TCP，则允许配置成功，但不生效。

【举例】

\# 创建TCP连接方式的POS应用模板1。

\<Sysname\> system-view

Sysname posa app 1 type tcp

\# 创建TCP连接方式的POS应用模板2，配置其备份应用服务器为1。

\<Sysname\> system-view

Sysname posa app 2 type tcp

Sysname-posa-app2 backup app 1

【相关命令】

·**timer quiet**

**POS终端接入 \-- POS终端接入配置命令 \-- caller-number enable**

------------------------------------------------------------------------

**[caller-number enable**]命令用来使能主叫号码发送功能，即在进行POS交易时向前置机发送POS机的主叫号码。

**[undo caller-number enable**]命令用来关闭主叫号码发送功能。

【命令】

**[caller-number enable**]

**[undo caller-number enable**]

【缺省情况】

主叫号码发送功能处于关闭状态。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该功能对于FCM POS机和AM POS机有效，只有TCP类型的POS应用模板才支持此配置。

当配置此功能后，设备向前置机转发POS机报文时会发送POS机的主叫号码（FCM POS机接入与AM POS机接入两种方式下发送主叫号码的格式不同）。

对于AM POS机接入方式，需要将应用模板配置为短连接模式，此功能才能生效。

对于FCM POS机接入方式，需要将应用模板配置为非透传模式，此功能才能生效。

【举例】

\# 配置TCP类型的POS应用模板1，使能主叫号码发送功能。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 mode temporary

Sysname-posa-app1 caller-number enable

**POS终端接入 \-- POS终端接入配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置POS应用模板的描述信息。

**[undo description**]命令用来删除配置的描述信息。

【命令】

**[description**] *text*

**[undo description**]

【缺省情况】

没有配置POS应用模板的描述信息。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：POS应用模板的描述信息，为1～32字符的字符串，区分大小写，合法字符是不为"？"的可打印字符。

【举例】

\# 创建TCP连接方式的POS应用模板，并配置它的描述信息为"ChinaBank1"。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 description ChinaBank1

**POS终端接入 \-- POS终端接入配置命令 \-- display fcm statistics**

------------------------------------------------------------------------

**[display fcm statistics**]命令用来显示FCM接口的POS接入的统计信息。

【命令】

**[display fcm statistics**[ [ **interface** **fcm** { *interface-number* \| *interface-number:setnumber*.*subnumber* } ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**[ **fcm** { *interface-number* \| *interface-number:setnumber*.*subnumber* }]]：显示指定接口的POS接入统计信息。interface-number表示物理FCM接口编号，用来显示物理FCM接口的POS接入统计信息；interface-number:setnumber.subnumber表示FCM子接口的编号，用来显示指定通道化FCM接口下子接口的POS接入统计信息。如果不指定该参数，则显示所有物理FCM接口、通道化FCM接口的子接口的POS接入的统计信息。

【使用指导】

设备重启、以及执行**reset fcm statistics**命令行会删除该统计值。

【举例】

\# 显示接口FCM2/1/0的POS接入的统计信息。

\<Sysname\> display fcm statistics interface fcm 2/1/0

Interface TerminalID ConnectFailed TimedOut Transactions (Total/Success)

Fcm2/1/0  5          20            30       100/20

表1-1 display fcm statistics命令显示信息描述表

字段

描述

Interface

接入的接口，只能为FCM接口

TerminalID

POS终端模板ID，若未绑定终端则显示为-

ConnectFailed

因拨号协商不成功的次数

TimedOut

因交易超时而断开的次数，此值与Success的统计不互斥，交易了多个报文但总交易时间超时的交易，既统计为TimeOut又统计为Success

Transactions

该接口下POS交易次数，包括：

·Total：总交易数

·Success：该接口下成功转发了交易报文的POS交易次数。在FCM交易过程中，POS机拨号后只要成功收发了交易报文，就认为本次交易成功，此统计值就加1。此值与TimedOut的统计不互斥，即交易了多个报文但总交易时间超时的交易，既统计为TimeOut又统计为Success

【相关命令】

·**reset fcm**

**POS终端接入 \-- POS终端接入配置命令 \-- display posa connection terminal**

------------------------------------------------------------------------

**[display posa connection terminal**]命令用来显示POS终端模板的连接信息。

【命令】

**[display posa connection terminal** [ *terminal-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[terminal-id*]：POS终端模板ID，取值范围为1～255。如果不指定该参数，则显示所有POS终端的连接信息。

【举例】

\# 显示所有POS终端模板的连接信息。

\<Sysname\> display posa connection terminal

Total TCP connections : 2

Total FCM connections : 1

Total flow connections: 1

Max concurrent trades : 65535

Current non-TCP trades: 2

Current TCP trades    : 60

ID  Type  Interface    SrcIP:SrcPort         DstIP:DstPort         Trades

1   TCP   -            192.168.100.100:1319  192.168.100.236:3000  10

1   TCP   -            192.168.100.100:1320  192.168.100.236:3000  20

5   TCP   -            192.168.100.200:1323  192.168.100.236:4000  30

6   FCM   Fcm10/0:0.0  -                     -                     1

7   Flow  Asy1/0       -                     -                     1

\# 显示POS终端模板1的连接信息。

\<Sysname\> display posa connection terminal 1

ID  Type  Interface    SrcIP:SrcPort         DstIP:DstPort         Trades

1   TCP   -            192.168.100.100:1319  192.168.100.236:3000  10

1   TCP   -            192.168.100.100:1320  192.168.100.236:3000  20

表1-2 display posa status terminal命令显示信息描述表

字段

描述

Total TCP connections

TCP接入方式下的当前连接总数

Total FCM connections

FCM接入方式下的当前连接总数

Total flow connections

Flow接入方式下的当前连接总数

Max coucurrent trades

系统支持的最大并发交易数

Current non-TCP trades

当前并发的所有非TCP交易数

Current TCP trades

当前并发的所有TCP交易数

ID

POS终端模板ID

Type

POS终端模板的连接类型：

·Flow：流接入方式

·FCM：FCM拨号接入方式

·TCP：TCP接入方式

Interface

接入的端口，TCP接入方式下显示为"-"

SrcIP

连接的源地址，非TCP接入方式下显示为"-"

SrcPort

连接的源端口，非TCP接入方式下显示为"-"

DstIP

连接目的地址，非TCP接入方式下显示为"-"

DstPort

连接目的端口，非TCP接入方式下显示为"-"

Trades

链接的当前并发交易数

**POS终端接入 \-- POS终端接入配置命令 \-- display posa statistics app**

------------------------------------------------------------------------

**[display posa statistics app**]命令用来显示POS应用模板的统计信息。

【命令】

**[display posa statistics app** [ *app-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[app-id*]：POS应用模板ID，取值范围为1～1024。如果不指定该参数，则显示所有POS应用模板的统计信息。

【使用指导】

删除应用模板、设备重启、执行**reset posa statistics**命令会删除该统计值。

对某一应用模板进行报文统计指的是该应用模板下所有应用实例接收发送的报文数目。

【举例】

\# 显示所有POS应用模板的统计信息。

\<Sysname\> display posa statistics app

ID  Received     Sent       PktErr      DisErr    InDiscarded    OutDiscarded

1   100          100        0           0         0              3

2   60           70         0           0         0              0

3   100          10         0           0         0              0

表1-3 display posa statistics app命令显示信息描述表

字段

描述

ID

POS应用模板ID

Received

从前置机接收到的报文数目（含PktErr和DisErr错误的报文数目，不含InDiscarded报文数目）

Sent

发送给前置机的报文数目（不包含链路不通丢弃的报文数目）

PktErr

格式错误的报文数目

DisErr

分发处理错误的报文数目，即找不到对应POS终端接入的报文数目

InDiscarded

接收缓冲区满丢弃的报文数目，是指从前置机接收报文时，因接收缓冲区满而丢弃的报文数目

OutDiscarded

链路不通丢弃的报文数目，是指应用发送报文时因链路不通丢弃报文数目

【相关命令】

·**reset posa statistics**

**POS终端接入 \-- POS终端接入配置命令 \-- display posa statistics terminal**

------------------------------------------------------------------------

**[display posa statistics terminal**]命令用来查看POS终端模板的统计信息。

【命令】

**[display posa statistics terminal** [ *terminal-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[terminal-id*]：终端ID，取值范围为1～255。如果不指定该参数，则显示所有POS终端模板的统计信息。

【使用指导】

若指定的终端不存在，则无输出也不提示错误信息。

删除终端模板、设备重启、执行**reset posa statistics**命令会删除该统计值。

对某一终端进行报文统计指的是该终端下所有终端实例接收发送的报文数目。

【举例】

\# 显示所有POS终端模板的统计信息。

\<Sysname\> display posa statistics terminal

ID  Received   Sent      PktErr    MapErr     InDiscarded   OutDiscarded  Notified

1   100        50        2         2          0             5             2

2   60         70        0         10         1             6             0

3   100        100       0         0          1             3             0

4   3          0         0         0          0             3             0

表1-4 display posa statistics terminal命令显示信息描述表

字段

描述

ID

POS终端模板ID

Received

从POS机接收到的报文数目（含PktErr和MapErr错误的报文数目，不含InDiscarded的报文数目）

Sent

发送给POS应用模板的报文数目的报文数目（不包含OutDiscarded和Notified的报文数目）

PktErr

从POS机收到的格式错误的报文数目

MapErr

应用映射失败，即查找不到应用对应关系的报文数目

InDiscarded

从POS机接收报文时，因接收缓冲区满或因获取交易号失败而丢弃的报文数目

OutDiscarded

终端发送报文时，因链路不通而丢弃的报文数目

Notified

设备向POS机发送的通告报文数目，是指当设备处理POS机报文应用映射失败、获取交易号失败或者向前置机转发POS机报文失败时，设备向POS机发送的通告报文数目

【相关命令】

·**reset posa statistics**

**POS终端接入 \-- POS终端接入配置命令 \-- display posa status app**

------------------------------------------------------------------------

**[display posa status app**]命令用来显示POS应用模板的状态信息。

【命令】

**[display posa status app** [ *app-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[app-id*]：POS应用模板ID，取值范围为1～1024。如果不指定该参数，则显示所有POS应用模板的状态信息。

【使用指导】

通过该显示命令查看到的信息项主要包括：应用ID、应用类型、模式、应用接口/应用IP地址和端口号、连接状态。

【举例】

\# 显示所有POS应用模板的状态信息。

\<Sysname\> display posa status app

AppID  Type  Mode       Interface       IPAddr:Port           State

1      TCP   Temporary  -               192.168.7.254:1000    linked

2      TCP   Temporary  -               192.168.7.224:1000    Error

3      Flow  -          Asy2/1/0        -                     Down

9      TCP   Permanent  -               192.168.4.1:20        Unlinked

11     TCP   Permanent  -               192.4.5.5:111         Unlinked

30     TCP   Temporary  -               192.168.7.52:4000     Multilink(10)

31     Flow  -          -                -                    -

表1-5 display posa status app命令显示信息描述表

字段

描述

AppID

POS应用模板ID

Type

应用的连接类型：

·Flow：流连接方式

·TCP：TCP连接方式

Mode

应用模板的模式：

Flow：显示为"-"

TCP：

·Permanent：长连接模式

·Temporary：短连接模式

Interface

应用模板的接口（未配置或者TCP方式下该项为"-"）

IPAddr：Port

应用模板的IP地址和端口号（未配置或者Flow方式下该项为"-"）

State

应用模板的连接状态：

Flow方式：

·Up：连接建立

·Down：连接断开

TCP方式：

·Unlinked：连接未建立

·Linking：连接正在建立

·Linked：连接已建立

·Multilink(N)：标识该应用下建立了N条TCP连接

·Blocked：标识该应用故障，被静默

·Error：应用模板表项不可用，原因为该表项使能失败（TCP绑定源端口失败）

未配置Interface／IPAddr：Port时，该项为"-"

**POS终端接入 \-- POS终端接入配置命令 \-- display posa status terminal**

------------------------------------------------------------------------

**[display posa status terminal**]命令用来显示POS终端模板的状态信息。

【命令】

**[display posa status terminal** [ *terminal-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[terminal-id*]：POS终端模板ID，取值范围为1～255。如果不指定该参数，则显示所有POS终端模板的状态信息。

【举例】

\# 显示所有POS终端模板的状态信息。

\<Sysname\> display posa status terminal

TerminalID  Type  Interface       ListenPort  State

1           TCP   -               2000        Unlinked

2           TCP   -               2000        Error

3           FCM   Fcm2/10/0:0.0   -           Down

254         TCP   -               3000        Multilink(2)

255         Flow  Asy2/1/0        -           Up

表1-6 display posa status terminal命令显示信息描述表

字段

描述

TerminalID

POS终端模板ID

Type

POS终端模板的连接类型：

·Flow：流接入方式

·FCM：FCM拨号接入方式

·TCP：TCP接入方式

Interface

接入的端口（TCP接入方式下该项为"-"）

ListenPort

TCP终端的监听端口（FCM/Flow接入方式下该项为"-"）

State

终端的连接状态：

Flow/FCM接入：

·Up：连接建立

·Down：连接断开

TCP接入：

·Unlinked：连接未建立

·Linked：连接已建立

·Multilink(N)：标识该终端下建立了N条TCP连接

·Error：表项不可用，该表项使能失败

**POS终端接入 \-- POS终端接入配置命令 \-- hello enable**

------------------------------------------------------------------------

**[hello** **enable**]命令用来开启POS应用模板握手功能。

**[undo hello enable**]用来关闭POS应用模板握手功能。

【命令】

**[hello** **enable**]

**[undo hello enable**]

【缺省情况】

POS应用模板握手功能处于关闭状态。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有TCP类型的POS应用模板支持此命令。

缺省情况下，设备只有在存在POS业务的情况下才会和前置机通信，并发现前置机是否故障，这样可能会使当前交易业务处理失败或者导致业务处理的时延较长。为了提前发现故障并做容错处理，尽量降低前置机故障对POS业务的影响，可通过开启POS应用模板周期性握手功能来主动探测前置机的状态。前置机也可以通过此功能来判断设备的可达性。

POS应用模板握手功能的流程为：设备以指定的间隔（可以通过**timer hello**命令设置）向当前POS应用模板对应的前置机发起TCP连接，TCP连接建立后，设备还会向前置机发送DATA字段为空的POS报文（报文内容固定为00056000000000，前置机并不会回应此报文）。

对于短连接应用，设备会新建一个TCP连接发报文，对于长连接应用，设备使用已经存在的长连接发送报文，若长连接不存在则创建，并在握手后继续保持。

握手功能会影响当前应用的静默状态：若处于静默状态的POS应用模板握手成功，则退出静默状态；若处于非静默状态的POS应用模板握手失败，则进入静默状态。

对于短连接应用，握手时发起连接成功不会发送前置机状态变化的告警信息。

【举例】

\# 开启应用1握手功能。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 hello enable

【相关命令】

·**timer hello**

**POS终端接入 \-- POS终端接入配置命令 \-- ip**

------------------------------------------------------------------------

**[ip**]命令用来配置当前POS应用模板对应的前置机的IP地址和端口号。

**[undo ip**]命令用来取消应用模板对应前置机的相关配置。

【命令】

**[ip** *ip-address* **port** *port-number*]

**[undo ip**]

【缺省情况】

未定义当前POS应用模板对应的前置机的IP和端口号。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：TCP类型POS应用模板银行前置机的IP地址，为非环回的单播IPv4地址。

*[port-number*]：TCP类型POS应用模板银行前置机服务的端口号，取值范围为1～65535。

【使用指导】

同一个POS应用模板下只能配置一个IP地址和端口，修改IP地址或者端口号将会删除现有的该POS应用模板的所有TCP连接。

【举例】

\# 配置TCP类型的POS应用模板1，IP地址为1.1.1.1，端口号为3000。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 ip 1.1.1.1 port 3000

\# 修改IP地址和端口。

Sysname-posa-app1 ip 1.1.1.2 port 3001

Connections for the application have been reset.

【相关命令】

·**posa app**

**POS终端接入 \-- POS终端接入配置命令 \-- mode**

------------------------------------------------------------------------

**[mode**]命令用来配置当前POS应用模板的连接模式。

**[undo mode**]命令用来恢复缺省情况。

【命令】

**[mode**[ { **permanent** \| **temporary** }]]

**[undo mode**]

【缺省情况】

POS应用模板的连接模式为长连接模式。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[permanent**]：设置连接模式为长连接模式。

**[temporary**]：设置连接模式为短连接模式。

【使用指导】

该配置只对TCP连接方式的POS应用模板有效。

修改POS应用模板的连接模式会断开该模板的已建立的TCP连接。

短连接模式下，每次POS业务结束时（终端挂机或者断开TCP连接时），设备都会断开与前置机应用的连接。长连接模式下，当第一次POS业务传送完毕后，这个TCP连接会一直保持用来传送后续的POS业务，即这个TCP连接一经建立就不会主动断开。将长连接修改为短连接时，会删除该模板下已经存在的TCP长连接。

在短连接模式下，终端每发起一次新的交易，设备都会向前置机创建一个新的连接，可并发多个与前置机的连接。在长连接模式下，非透传终端每发起一次新的连接，只会使用设备与前置机之间现有的一条长连接不会创建新的连接，所以只创建一条与前置机的连接；有个例外情况：若终端配置透传APP，则无论该APP为长连接或者短连接，设备都会为该终端创建一条与前置机专用的连接，此时设备与前置机之间可并发多个连接。

【举例】

\# 配置TCP方式的POS应用模板1，配置POS应用模板1的连接模式为短连接，现有已经建立的长连接被删除。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 mode temporary

Connections for the application have been reset.

【相关命令】

·**posa app**

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation hookoff**

------------------------------------------------------------------------

**[negotiation hookoff**]命令用来设置FCM接口接收到铃流后FCM卡延时摘机时间。

**[undo negotiation hookoff**]命令用来恢复缺省情况。

【命令】

**[negotiation hookoff **]*delaytime*

**[undo negotiation hookoff**]

【缺省情况】

FCM接口接收到铃流后延时摘机时间为500毫秒。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[d*]*elaytime*：FCM接口收到铃流后FCM卡延时摘机时间，取值范围是100～6000，单位为毫秒。

【举例】

\# 设置FCM2/4/0接口接收到铃流后FCM卡延时摘机时间。

\<Sysname\> system-view

Sysname interface fcm 2/4/0

Sysname-Fcm2/4/0 negotiation hookoff 2000

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation no-carrier-detect retry**

------------------------------------------------------------------------

**[negotiation no-carrier-detect retry**]命令用来配置连续检测到线路为无载波状态的次数。

**[undo negotiation no-carrier-detect retry**]命令用来恢复缺省情况。

【命令】

**[negotiation no-carrier-detect retry ***n-retrytime*]

**[undo negotiation no-carrier-detect retry**]

【缺省情况】

连续检测到线路为无载波状态的次数为1。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[n-retrytime*]：连续检测到线路为无载波状态的次数，取值范围是1～1000。当FCM卡连续检测到线路为无载波状态的次数为*n-retrytime*时，将挂机。

【举例】

\# 设置FCM2/4/0接口连续检测到线路为无载波状态的次数为20次。

\<Sysname\> system-view

Sysname interface fcm 2/4/0

Sysname-Fcm2/4/0 negotiation no-carrier-detect retry 20

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation scramble-binary1**

------------------------------------------------------------------------

**[negotiation scramble-binary1**]命令用来设置Modem协商发送扰码1的持续时间。

**[undo negotiation scramble-binary1**]命令用来恢复缺省情况。

【命令】

**[negotiation scramble-binary1 **]*scramble-binary1time*

**[undo negotiation scramble-binary1**]

【缺省情况】

Modem协商发送扰码1的持续时间为250毫秒。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[scramble-binary1time*]：设置Modem协商发送扰码1的持续时间，取值范围是100～1500，单位为毫秒。

【举例】

\# 设置Modem协商发送扰码1的持续时间为200毫秒。

\<Sysname\> system-view

Sysname interface fcm 2/4/0

Sysname-Fcm2/4/0 negotiation scramble-binary1 200

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation silence**

------------------------------------------------------------------------

**[negotiation silence**]命令用来设置Modem协商的静默时间。

**[undo negotiation silence**]命令用来恢复缺省情况。

【命令】

**[negotiation silence **]*silencetime*

**[undo negotiation silence**]

【缺省情况】

Modem协商的静默时间为0毫秒。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[silencetime*]：设置Modem协商的静默时间，取值范围是0～3000，单位为毫秒。静默时间是指FCM卡从摘机到发送数据之间的时间。

【使用指导】

静默时间主要是应用于FCM卡和POS机握手，静默时间必须大于POS机的摘机响应时间小于POS机的最大等待时间。

·如果静默时间大于POS机的最大等待时间，POS机会以为没有数据而挂机；

·如果静默时间小于POS机的摘机响应时间，因POS机检测到FCM卡摘机需要一段时间，此时POS机还未检测到FCM卡摘机就已将数据发出，从而导致数据丢失。

【举例】

\# 设置Modem协商的静默时间为100毫秒。

\<Sysname\> system-view

Sysname interface fcm 2/4/0

Sysname-Fcm2/4/0 negotiation silence 100

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation unscramble-binary1**

------------------------------------------------------------------------

**[negotiation unscramble-binary1**]命令用来设置Modem协商发送非扰码1的持续时间。

**[undo negotiation unscramble-binary1**]命令用来恢复缺省情况。

【命令】

**[negotiation unscramble-binary1 **]*unscramble-binary1time*

**[undo negotiation  unscramble-binary1**]

【缺省情况】

Modem协商发送非扰码1的持续时间为400毫秒。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[unscramble-binary1time*]：设置Modem协商发送非扰码1持续时间，取值范围是300～1500，单位为毫秒。

【举例】

\# 设置Modem协商发送非扰码1的持续时间为900毫秒。

\<Sysname\> system-view

Sysname interface fcm 2/4/0

Sysname-Fcm2/4/0 negotiation unscramble-binary1 900

**POS终端接入 \-- POS终端接入配置命令 \-- posa app**

------------------------------------------------------------------------

**[posa app**]命令用来创建POS应用模板并进入POS应用模板视图。

**[undo posa app**]用来删除配置的POS应用模板。

【命令】

**[posa app**[ *app-id* **type** { **flow** \| **tcp** }]]

**[undo posa app**] *app-id*

【缺省情况】

不存在POS应用模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[app-id*]：POS应用模板ID，取值范围为1～1024。

**[type**]：设备与银行前置机之间的连接方式。

**[flow**]：表示流连接方式。

**[tcp**]：表示TCP连接方式。

【使用指导】

不能重复配置相同应用ID，并且不能更改已有的设备与前置机之间的连接方式。

创建流方式POS应用模板之后应将其绑定到接口（Async、Serial和Aux接口）上方可生效。

【举例】

\# 创建流连接方式的POS应用模板1，并绑定到Async2/7/0接口上。

\<Sysname\> system-view

Sysname posa app 1 type flow

Sysname-posa-app1 quit

Sysname interface Async 2/7/0

Sysname-Async2/7/0 posa bind app 1

\# 创建TCP连接方式的POS应用模板2。

\<Sysname\> system-view

Sysname posa app 2 type tcp

【相关命令】

·**posa bind app**

**POS终端接入 \-- POS终端接入配置命令 \-- posa auto-stop-service enable**

------------------------------------------------------------------------

**[posa auto-stop-service enable**]命令用来开启当所有的前置机状态为不可达时，主动关闭TCP类型终端模板的监听端口功能。

**[undo posa auto-stop-service enable**]命令用来恢复缺省情况。

【命令】

**[posa auto-stop-service enable**]

**[undo posa auto-stop-service enable**]

【缺省情况】

主动关闭TCP类型终端模板的监听端口功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当所有TCP类型的POS应用模板对应的前置机状态为不可达时，POS终端接入设备将主动关闭所有TCP类型终端模板的监听端口。

当任意一个前置机状态变为可达时，则主动打开所有TCP类型终端模板的监听端口。

前置机状态不可达是指POS终端接入设备与前置机发起连接失败（包含发起连接超时），或在连接过程中keepalive报文保活失败导致连接断开。

【举例】

\# 开启主动关闭TCP类型终端模板的监听端口功能。

\<Sysname\> system-view

Sysname posa auto-stop-service enable

**POS终端接入 \-- POS终端接入配置命令 \-- posa bind app**

------------------------------------------------------------------------

**[posa bind app**]命令用来绑定POS应用模板。

**[undo posa bind app**]命令用来取消该接口下绑定的POS应用模板。

【命令】

**[posa bind app** *app-id*]

**[undo posa bind app**]

【缺省情况】

接口下未绑定任何POS应用模板。

【视图】

异步接口视图/同异步接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[app-id*]：POS应用模板ID，取值范围为1～1024。

【使用指导】

通过异步接口连接前置机的方式下，POS应用模板是通过异步接口来标识的，即一个接口对应一个应用，本命令用来将异步接口与对应的POS应用模板绑定。

需要注意的是：

·在接口下绑定POS应用模板之前，必须先在系统视图下创建该应用，且该应用的类型必须为Flow类型。

·一个接口下只能绑定一个POS应用模板，若要修改绑定的POS应用模板，则必须首先取消与当前POS应用模板的绑定，再绑定新的POS应用模板。

·不同的接口上必须绑定不同的POS应用模板。

·同一接口不能同时配置为接入POS终端模板的接口和绑定POS应用模板的接口。

·同异步接口绑定POS应用模板时，该接口必须工作在异步模式下。若接口不为异步模式则配置可以成功但是该模板的状态为error。

·接口必须工作在流模式下POS终端接入设备才能正常工作。

【举例】

\# 配置Flow类型的应用2。

\<Sysname\> system-view

Sysname posa app 2 type flow

Sysname-posa-app2 quit

\# 配置异步接口Async2/1/0与应用2相连。

\<Sysname\> system-view

Sysname interface async2/1/0

Sysname-Async2/1/0 posa bind app 2

【相关命令】

·**posa app**

**POS终端接入 \-- POS终端接入配置命令 \-- posa bind terminal**

------------------------------------------------------------------------

**[posa bind terminal**]命令用来指定当前接口为某POS终端模板的接入接口。

**[undo posa bind terminal**]命令用来取消该接口为POS终端模板的接入接口。

【命令】

**[posa bind terminal**] *terminal-id* [ **app** *app-id* ]

**[undo posa bind terminal**]

【缺省情况】

当前接口未配置为任何POS终端模板的接入接口。

【视图】

异步接口视图/同异步接口视图/物理AM接口视图/物理FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[terminal-id*]：POS终端模板ID，取值范围为1～255。

**[app**]*app-id*：指定该POS终端模板工作在透传模式下，并指定其对应的POS应用模板。*app-id*为POS应用模板ID，取值范围为1～1024。指定的POS应用模板必须为已经存在的TCP接入类型的POS应用模板。若不指定该参数，则表示该POS终端模板工作在非透传模式下。

【使用指导】

·同异步串口需要工作在异步方式下，才能配置该命令；若接口不为异步模式则配置可以成功但是该模板的状态为error。

·同一个接口只能指定为一个POS终端模板的接入接口；不同的接口必须指定为不同的POS终端模板的接入接口；

·同一接口不能同时配置为接入POS终端模板的接口和绑定POS应用模板的接口；

·接口下配置的POS终端模板不能在非透传模式与非透传模式之间的转换，也不能修改对应的POS应用模板，必须先取消该接口为POS终端模板的接入接口，再重新配置。

·不同POS终端模板可以指定一个相同的透传应用。

·若指定的透传应用不存在或者不是TCP类型允许配置，但不生效，终端交易时会失败。

【举例】

\# 配置Async2/1/0为POS终端模板1的接入接口。

\<Sysname\> system-view

Sysname interface async 2/1/0

Sysname-Async2/1/0 posa bind terminal 1

【相关命令】

·**posa app**

**POS终端接入 \-- POS终端接入配置命令 \-- posa bind terminal first-terminal-id**

------------------------------------------------------------------------

![说明](POS终端接入命令.files/image001.png)

本命令的支持情况与设备支持的接口类型有关，请以设备的实际情况为准。

****

**[posa bind terminal first-terminal-id**]命令用来批量指定当前接口的子接口为POS终端模板接入接口。

**[undo posa bind terminal**]命令用来取消当前接口的子接口为POS终端模板的接入接口。

【命令】

**[posa bind terminal first-terminal-id** *first-terminal-id* [ **app-list** *app-list* [ **reassemble**  ]]]

**[undo posa bind terminal**]

【缺省情况】

当前接口的子接口未配置为任何POS终端模板的接入接口。

【视图】

通道化AM接口视图/通道化FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[first-terminal-id*]：起始终端模板ID，取值范围为1～255。从起始终端模板ID开始到255之间的POS终端模板ID依次用来与FCM子接口或AM子接口进行绑定。

**[app-list*** app-list*]：指定POS终端模板工作在透传模式下，并指定自起始终端模板ID开始到终端模板ID 255连续递增的一组终端对应的POS应用模板。*app-list*为POS应用模板ID列表。*app-list*取值包括数字、逗号"[,"、连字符"-"和冒号":"，不能包含空格。其中，]逗号用来分隔单个数字或一组数字；连字符用来连接两个应用模板ID，表示从起始应用模板ID到结束应用模板ID之间连续的一串应用模板ID，且要求起始应用模板ID要小于结束应用模板ID；冒号用来连接两个数字，表示多次重复指定某一个应用模板ID，前面的数字表示应用模板ID，后面的数字表示重复的次数。应用模板ID的取值范围为1～1024；重复次数的取值范围为1～30。例如"1-14,15,16:13,127-128"表示前14个子接口对应的应用模板ID依次为1～14，第15个子接口对应的应用模板ID为15，第16到第28个子接口对应的应用模板ID均为16，第29和30个子接口对应的应用模板ID分别为127和128。如果不指定本参数，则表示POS终端模板工作在非透传模式下。

**[reassemble**]：指定透传模式下，POS终端接入设备对从POS机接收到的分片报文进行重组后，再发送给前置机。如果不指定本参数，则POS终端接入设备直接将接收到的分片报文发送给前置机。只有通道化AM接口视图下支持本参数。

【使用指导】

一个物理类型为E1POS的CE1/PRI接口会生成多个FCM子接口，一个物理类型为E1DM的CE1/PRI接口会生成多个AM子接口，本命令用来指定与各个子接口绑定的POS终端模板ID和应用模板ID。指定的POS终端模板数目必须大于或等于子接口数目，指定的应用模板数目必须与子接口的数目一致，否则本命令执行失败。例如，指定了起始POS终端模板ID为251，若当前接口下的FCM子接口数目大于5，则由于绑定的POS终端模板只有5个（251～255），POS终端模板数不足导致批量配置失败。FCM子接口和AM子接口生成方式的详细介绍，请参见"接口管理配置指导"中的"WAN接口"。

如果要绑定的POS终端模板中存在非FCM/AM类型终端模板或已经与其它接口绑定的终端模板，则本命令执行失败。

如果指定的应用模板不存在或者不是TCP类型，则允许执行本命令，但配置不会生效，终端交易时会失败。

如果前置机不支持对POS交易报文进行分片重组，那么在透传模式下，需要指定**reassemble**参数，由POS终端接入设备对POS交易报文进行分片重组。

【举例】

\# 接口FCM2/4/0:15下存在30个子接口，批量将这些接口指定为POS终端模板1～30的接入接口，并指定与其绑定的应用模板ID为1～30。

\<sysname\> system-view

sysname interface fcm 2/4/0:15

sysname-Fcm2/4/0:15 posa bind terminal first-terminal-id 1 app-list 1-30

【相关命令】

·**posa app **

·**posa bind terminal**

**POS终端接入 \-- POS终端接入配置命令 \-- posa connection-threshold terminal**

------------------------------------------------------------------------

**[posa connection-threshold terminal**]命令用来设置终端并发连接数阈值。

**[undo posa connection-threshold terminal**]命令用来恢复缺省情况。

【命令】

**[posa connection-threshold**[ **terminal** { **fcm** *fcm-threshold-value* \| **tcp** *tcp-threshold-value* }]]

**[undo posa connection-threshold terminal **[{ **fcm** \| **tcp** }]]

【缺省情况】

TCP接入方式的并发连接数阈值为4096，FCM拨号接入方式的并发连接数阈值为255。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fcm**]* fcm-threshold-value*：设置FCM拨号接入方式的并发连接数阈值，取值范围为1～255。

**[tcp**]* tcp-threshold-value*：设置TCP接入方式的并发连接数阈值，取值范围为1～4096。

【使用指导】

如果开启了相应的POS终端接入告警功能，则当设备上的TCP或FCM拨号接入方式的终端并发连接数超过指定的阈值时，会生成相应的告警信息。

需要注意的是，终端并发连接数达到指定的阈值后，不会影响后续连接的建立。

【举例】

\# 设置TCP接入方式的并发连接数阈值为200。

\<Sysname\> system-view

Sysname posa connection-threshold terminal tcp 200

【相关命令】

·**snmp-agent trap enable posa**

**POS终端接入 \-- POS终端接入配置命令 \-- posa fcm**

------------------------------------------------------------------------

**[posa fcm**]命令用来设置在Modem协商过程中的FCM参数。

**[undo posa fcm**]命令用来恢复参数的缺省值。

【命令】

**[posa fcm**[ { **answer-time** *time1* \| **idle-time** *time2* \| **trade-time** *time3* }]]

**[undo posa fcm**[ { **answer-time** \| **trade-time** \| **idle-time** }]]

【缺省情况】

Modem协商过程中，应答音时间为2000毫秒，空闲时间为180秒，交易时间为12000000毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[answer-time** *time1*]：Modem协商时向POS机发送应答音的时间，取值范围为500～2000，单位为毫秒，缺省值为2000。

**[idle-time** *time2*]：POS机拨号后，链路上空闲最大时间，取值范围为1～12000，单位为秒，缺省值为180。

**[trade-time** *time3*]：单笔POS交易的持续时间，取值范围为30000～12000000，单位为毫秒，缺省值为12000000。

【使用指导】

在POS接入应用中，设备上的Modem通常都是作为应答端，而POS机内嵌的Modem做主叫方。Modem通信的基本过程为POS机发起呼叫，应答端检测到呼叫信号时会摘机并发送应答音给POS机，POS机收到该应答音后双方同步开始Modem协商（V.22）过程。由于电话网络比较复杂，信号质量及延迟也不尽相同，对于网络质量较差的系统，应答音设置太短可能会造成Modem无法协商通过，在设备上将只能看到Modem端口不断的up、down，而没有数据包的收发，这时候可以适当增大**answer-time**参数时间值。

为了提高接入端口的利用效率，需要避免一台POS机拨号接入设备之后长时间占用系统资源，若一台POS机拨入后单笔交易时间超过设置的**trade-time**值，或空闲时间超过设置的**idle-time**值，则设备会主动挂机以释放链路资源。

一般情况下，各FCM参数的缺省值基本上都可以满足应用，但在通信出现异常的情况下需要根据上述说明修改各个参数。

【举例】

\# 配置answer-time为800毫秒，trade-time为20分钟（1200000毫秒），idle-time为6秒。

\<Sysname\> system-view

Sysname posa fcm answer-time 800

Sysname posa fcm trade-time 1200000

Sysname posa idle-time 6

**POS终端接入 \-- POS终端接入配置命令 \-- posa map**

------------------------------------------------------------------------

**[posamap**]命令用来配置多应用的POS接入映射表项。

**[undo **]**posamap**命令用来删除多应用POS接入映射表项。

【命令】

**[posa map ** **[default**[\| **destination** *des-code*  \| ]**source ***src-code*} \*} **app** *app-id*

**[undo posa map** **[default**[\|**destination** *des-code*  \| ]**source ***src-code*} \*}

【缺省情况】]

无]POS接入映射表项。

【视图】]

系统视图]

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[default**]：指定缺省的接入映射表项，即所有未找到匹配项的报文将被发送给指定的POS应用模板处理。

**[destination**]* des-code*：POS报文的TPDU头中的目的地址，是由四个十六进制数字表示的字符（如：FFFF），一般用来区分不同的银行。它一般是由业务中心统一分配的。

**[source**]* src-code*：POS报文的TPDU头中的源地址，是由四个十六进制数字表示的字符（如：0001），一般用来区分不同的POS机。

**[app**]*app-id*：POS应用模板ID，取值范围为1～1024。

【使用指导】

POS接入设备通过将收到的POS报文的TPDU头中的源地址和目的地址与配置的POS接入映射关系表项进行匹配，来决定将该报文发送到哪个POS应用模板上去处理。若POS报文的源地址、目的地址或者源地址和目的地址的组合与某一个映射关系表项对应，则该报文就被发送给该表项所对应的POS应用模板处理；若该报文未找到任何匹配项，则将被发送给缺省的POS应用模板处理。

需要注意的是：

·同一个POS应用模板可对应多个POS接入映射表项。

·匹配时其中指定了源地址和目的地址的组合表项匹配优先级最高，缺省映射的优先级最低。

·包括缺省POS接入映射表项在内，系统最多支持1024个POS接入映射表项。

·在POS交易过程中修改POS接入映射表项的目的前置机，不会删除正在使用中的连接，但可能会影响正在进行的POS交易。

·若应用模板ID不存在，可以配置，但不生效。

【举例】

\# 配置一个POS接入映射表项，将TPDU头中的目的地址为01f1的POS报文都发送给应用2去处理。

\<Sysname\> system-view

Sysname posa map destination 01f1 app 2

\# 配置一个缺省的POS接入映射表项，将未能匹配到任何POS接入映射表项的POS报文都发送给POS应用模板1去处理。

\<Sysname\> system-view

Sysname posa map default app 1

【相关命令】

·**posa app**

**POS终端接入 \-- POS终端接入配置命令 \-- posa server enable**

------------------------------------------------------------------------

**[posa server enable**]命令用来开启POS终端接入服务。

**[undo posa server enable**]命令用来恢复缺省情况。

【命令】

**[posa server enable**]

**[undo posa server enable**]

【缺省情况】

POS终端接入服务处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

要实现POS接入，必须先启动POS终端接入服务。若开启服务时部分功能可以配置但不生效（如TCP端口不可用），管理员通过**display posa status**查看状态为Error，此时将问题修改后重新使能即可。

【举例】

\# 开启POS终端接入服务。

\<Sysname\> system-view

Sysname posa server enable

【相关命令】

·**display posa status**

**POS终端接入 \-- POS终端接入配置命令 \-- posa statistics caller-id**

------------------------------------------------------------------------

**[posa statistics caller-id**]命令用来创建一个主叫号码统计项，设备将根据该统计项中指定的终端主叫号码对POS机与前置机之间交互的终端报文数进行统计。

**[undo posa statistics caller-id**]命令用来取消指定主叫号码统计项。

【命令】

**[posa statistics caller-id** *caller-number*]

**[undo posa statistics caller-id*** caller-number*]

【缺省情况】

无主叫号码统计项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[caller-number*]：终端主叫号码，为1～64个字符的字符串，仅可以为数字和字母，如01012345678。通常意义上的主叫号码都是由数字组成，但是不排除特殊情况使用字母。

【使用指导】

该统计方式仅适用于通过拨号方式接入的POS终端模板。

重复配置相同则主叫号码统计项不提示错误。

最多支持配置64条统计项。

【举例】

\# 创建一个主叫号码统计项，统计主叫号码为01012345678的POS机报文数。

\<Sysname\> system-view

Sysname posa statistics caller-id 01012345678

**POS终端接入 \-- POS终端接入配置命令 \-- posa statistics caller-ip**

------------------------------------------------------------------------

**[posa statistics caller-ip**]命令用来创建一个源IP统计项，该统计项中指定了一个终端源IP地址或者一个源IP网段，设备将根据指定的源IP地址或者源IP网段对POS机与前置机之间交互的终端报文数进行统计。

**[undo posa statistics caller-ip**]命令用来删除指定的源IP统计项。

【命令】

**[posa statistics caller-ip ***group-id* *ip-address ip-mask*]

**[undo posa statistics caller-ip*** group-id*]

【缺省情况】

无源IP统计项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：统计项编号，取值范围为1～64。

*[ip-address*]：终端源IP地址或源IP网段地址，为点分十进制格式。

*[ip-mask*]：终端源IP地址或源IP网段的子网掩码，为点分十进制格式。

【使用指导】

·该统计方式只适用于TCP接入方式的POS终端模板。

·各源IP统计项网段之间可以相互重叠，甚至相同。

·交易时，只要是源IP地址与统计项中指定的源IP地址或者源IP地址段匹配的POS机交易报文，都会被统计到该统计项，所以一个报文可能会被统计到多个表项中。

【举例】

\# 创建源IP统计项1，统计源IP地址为10.0.1.0/24网段内的POS机的交易报文数。

\<Sysname\> system-view

Sysname posa statistics caller-ip 1 10.0.1.0 255.255.255.0

**POS终端接入 \-- POS终端接入配置命令 \-- posa terminal**

------------------------------------------------------------------------

**[posa terminal**]命令用来创建TCP接入方式的POS终端模板。

**[undo posa terminal**]命令用来删除指定的POS接入终端模板。

【命令】

**[posa terminal **]*terminal-id* **type tcp listen-port** *port* \**[idle-time***time* ]

**[undo posa terminal**] *terminal-id*

【缺省情况】

未配置TCP方式的POS终端模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[terminal-id*]：POS终端模板ID，取值范围为1～255。

**[type**] **tcp**：创建TCP接入方式的POS终端模板。

**[listen-port**]* port*：指定监听端口号，取值范围为1～65535。

**[idle-time**] *time*：指定POS终端模板的空闲超时时间，取值范围0～1440，单位为分钟，缺省值为0分钟。0表示对POS终端模板的空闲时间没有限制。

【使用指导】

POS终端模板用于保存POS接入设备与每一个POS终端交互的相关配置信息的的配置信息。对于流接入方式或者拨号接入方式的POS终端模板，在指定POS终端模板的接入接口时，系统会自动创建对应的POS终端模板。对于TCP接入方式，需要手工配置POS终端模板。

TCP接入方式的POS终端模板上指定的监听端口唯一，不能相互冲突。并且不能修改TCP终端的监听端口。

在指定的空闲超时时间内，如果POS机与POS终端模板之间没有报文的交互，则POS终端模板将断开与POS机之间的连接。

【举例】

\# 创建TCP接入方式的POS终端模板1，且指定监听端口号为3000。

\<Sysname\> system-view

Sysname posa terminal 1 type tcp listen-port 3000

【相关命令】

·**posa bind terminal**

**POS终端接入 \-- POS终端接入配置命令 \-- posa terminal description**

------------------------------------------------------------------------

**[posa terminal description**]命令用来配置POS终端模板的描述信息。

**[undo **]**posa terminal description**命令用来删除POS终端模板的描述信息。

【命令】

**[posa terminal **]*terminal-id ***description ***text*

**[undo posa terminal **]*terminal-id*** description**

【缺省情况】

未配置POS终端模板的描述信息。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[terminal-id*]：POS终端模板ID，取值范围为1～255。

*[text*]：POS终端模板的描述信息，为1～32个字符的字符串，区分大小写，合法字符是不为'？'的可打印字符。

【使用指导】

允许先配置POS终端模板的描述信息再创建该POS终端模板。

【举例】

\# 为POS终端模板1配置描述信息为"Shopping1"。

\<Sysname\> system-view

Sysname posa terminal 1 description shopping1

【相关命令】

·**posa terminal**

**POS终端接入 \-- POS终端接入配置命令 \-- posa tpdu-replace**

------------------------------------------------------------------------

**[posa** **tpdu-replace**]命令用来配置TPDU地址替换策略，即将符合匹配条件的POS报文TPDU头中的目的地址替换成指定的目的地址，并按新的目的地址查找映射表。

**[undo posa tpdu-replace**]命令用来恢复缺省情况。

【命令】

**[posa**[ **tpdu-replace match terminal** { *terminal-id* \| **any** } **destination** { *des-code* \| **any** } **to** *des-code*]]

**[undo posa tpdu-replace match terminal**[ { *terminal-id* \| **any** } [ **destination** { *des-code* \| **any** } ]]]

【缺省情况】

不对POS报文TPDU头中的目的地址进行替换。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[terminal-id*]：POS终端模板ID。将该终端发送的POS报文TPDU头中的目的地址替换成指定的目的地址。

**[terminal any**]：任意POS终端模板ID。配置该参数表示，所有终端发送的POS报文，都将进行地址替换。

**[destination ***des-code*]**：**POS报文的TPDU头中的目的地址。如果POS报文TPDU头中的目的地址跟所配置的*des-code*相匹配，则将此地址替换成所需的目的地址。

**[destination any**]**：**任意的TPDU头中的目的地址。配置该参数表示，所有符合**terminal**匹配条件的POS报文TPDU头中的目的地址将替换成指定的目的地址。

**[to*** des-code*]**：**需要替换成的目的地址。

【使用指导】

通过多次执行本命令可以配置多条TPDU地址替换策略。按照优先级由高到低的顺序，TPDU地址替换策略的匹配顺序为：

(1)配置了*terminal-id*和*des-code*的策略；

(2)配置了*terminal-id*和**destination any**的策略；

(3)配置了**terminal any**和*des-code*的策略；

(4)配置了**terminal any**和**destination any**的策略。

当POS终端模板给POS机返回回应消息时，会恢复原始的TPDU头中的目的地址。

【举例】

\# 将终端1发送的目的地址为0002的POS报文中的目的地址替换为0003。

\<Sysname\> system-view

Sysname posa tpdu-replace match terminal 1 destination 0002 to 0003

【相关命令】

·**tpdu-change**

**POS终端接入 \-- POS终端接入配置命令 \-- posa trade-limit tcp**

------------------------------------------------------------------------

**[posa trade-limit tcp**]命令用来设置TCP连接的并发交易数上限。

**[undo posa trade-limit tcp**]命令用来恢复缺省情况。

【命令】

**[posa trade-limit tcp **]*limit-value*

**[undo posa trade-limit tcp**]

【缺省情况】

不对TCP连接的并发交易数做限制。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit-value*]：每条TCP连接的并发交易数上限值，取值范围为0～65535，0表示不对TCP连接的并发交易数做限制。

【使用指导】

配置了TCP连接的并发交易数上限后，当设备收到的某个TCP连接上的并发交易数超过指定的上限时，会将超出限制的交易报文丢弃。同时，如果设备开启了关于TCP连接并发交易数超过上限的告警功能，还会生成相应的告警信息。

需要注意的是，为了避免在大交易流量时频繁生成告警信息，POS终端接入模块只在某个TCP连接上的并发交易数达到上限后第一次收到新交易报文时生成告警信息。此后，在并发交易数低于上限的90%前不再生成告警信息，当并发交易数低于上限的90%后又重新超出上限时才会再次生成告警信息。

【举例】

\# 配置每条TCP连接的并发交易数上限为1024。

\<Sysname\> system-view

Sysname posa trade-limit tcp 1024

【相关命令】

·**snmp-agent trap enable posa**

**POS终端接入 \-- POS终端接入配置命令 \-- posa trade-timeout**

------------------------------------------------------------------------

**[posa trade-timeout**]命令用来设定每笔交易的超时时间。

**[undo posa trade-timeout**]命令用来恢复缺省情况。

【命令】

**[posa**]**trade-timeout ***timeout-value*

**[undo posa trade-timeout**]

【缺省情况】

每笔交易的超时时间为240秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timeout-value*]：每笔交易的超时时间，取值范围为1～240，单位为秒。

【使用指导】

设备从POS终端收到交易报文后，如果在指定的时间内没有收到银行前置机的应答，则认为交易超时。超时之后再收到此交易的应答，设备会将报文丢弃。

需要注意的是，在网络拥塞的情况下，不能将交易超时时间配置的太小，否则可能会出现内部交易号串号的情况，即设备将已超时交易的内部交易号分配给了新交易，之后收到已超时交易的应答会被误认为是对新交易的应答。

【举例】

\# 配置每笔交易的超时时间为120秒。

\<Sysname\> system-view

Sysname posa trade-timeout 120

**POS终端接入 \-- POS终端接入配置命令 \-- reset fcm statistics**

------------------------------------------------------------------------

**[reset fcm statistics**]命令用来清除指定FCM接口的统计信息。

【命令】

**[reset fcm statistics**[ [ **interface** **fcm** { *interface-number* \| *interface-number:setnumber*.*subnumber* } ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface******fcm **[{ *interface-number* \| *interface-number:setnumber*.*subnumber* }]]：清除指定接口的POS接入统计信息。*interface-number*表示物理FCM接口编号，用来清除物理FCM接口的POS接入统计信息；*interface-number:setnumber*.*subnumber*表示FCM子接口的编号，用来清除指定通道化FCM接口下子接口的POS接入统计信息。如果不指定该参数，则清除所有物理FCM接口、通道化FCM接口的子接口的POS接入统计信息。

【举例】

\# 清除所有物理FCM接口、通道化FCM接口的子接口的POS接入统计信息。

\<Sysname\> reset fcm statistics

【相关命令】

·**display fcm statistics**

**POS终端接入 \-- POS终端接入配置命令 \-- reset posa connection terminal**

------------------------------------------------------------------------

**[reset posa connection terminal**]命令用来断开设备与POS机之间的TCP连接。

【命令】

**[reset posa connection terminal**[ { **all** \| **destination-ip** *ip-addr2* \| **destination-port** *port-number* \| **source-ip** *ip-addr1* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：断开设备与所有POS机之间的TCP连接。

**[destination-ip** *ip-addr2*]：目的IP地址。

**[destination-port** *port-number*]：目的端口号，取值范围为1～65535。

**[source-ip** *ip-addr1*]：源IP地址。

【使用指导】

本命令可以根据用户指定的源IP地址、目的IP地址和目的端口号断开指定的单条或多条符合条件的TCP连接。

执行此命令行后会显示已断开的匹配的连接数。

【举例】

\# 断开所有POS机的TCP连接。

\<Sysname\> reset posa connection terminal all

100 connections have been deleted.

**POS终端接入 \-- POS终端接入配置命令 \-- reset posa statistics**

------------------------------------------------------------------------

**[reset posa statistics**]命令用来清空POS终端模板或POS应用模板的相关统计信息。

【命令】

**[reset posa statistics** [ **app** [ *app-id*  \| **terminal**  *terminal-id*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[app-id*]：POS应用模板ID，取值范围为1～1024。

*[terminal-id*]：POS终端模板ID，取值范围为1～255。

【使用指导】

本命令用来将**display posa statistics app**和**display posa statistics terminal**两条命令显示的统计信息清理，从零开始重新对报文进行记数。

复位不存在的应用的统计信息或者复位不存在的终端的统计信息不提示错误。

【举例】

\# 将显示信息记数器清零。

\<Sysname\> reset posa statistics

【相关命令】

·**display posa statistics app**

·**display posa statistics terminal**

**POS终端接入 \-- POS终端接入配置命令 \-- snmp-agent trap enable posa**

------------------------------------------------------------------------

**[snmp-agent trap enable posa**]命令用来在全局下开启POS终端接入的告警功能。

**[undo snmp-agent trap enable posa**]命令用来在全局下关闭POS终端接入的告警功能。

【命令】

**[snmp-agent**[ **trap** **enable posa** [ **app-state-change** \| **fcm-connection-exceed** \| **fcm-link-failure** \| **fcm-physical-failure** \| **server-state-change** \| **tcp-connection-exceed** ]]｜ **tcp-trade-exceed**[ \| **terminal-hangup** ] \*]

**[undo**[ **snmp-agent** **trap** **enable posa** [ **app-state-change** \| **fcm-connection-exceed** \| **fcm-link-failure** \| **fcm-physical-failure** \| **server-state-change** \| **tcp-connection-exceed** ]]｜ **tcp-trade-exceed**[ \| **terminal-hangup** ] \*]

【缺省情况】

POS终端接入告警功能在全局下处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[app-state-change**]：表示POS应用模板状态切换的告警信息。

**[fcm-connection-exceed**]：表示FCM拨号接入方式并发连接数超过阈值的告警信息。

**[fcm-link-failure**]：表示FCM链路层协商失败的告警信息。

**[fcm-physical-failure**]：表示FCM物理层协商失败的告警信息。

**[server-state-change**]：表示POS接入服务状态切换的告警信息。

**[tcp-connection-exceed**]：表示TCP接入方式并发连接数超过阈值的告警信息。

**[tcp-trade-exceed**]：表示TCP连接的并发交易数超过上限的告警信息。

**[terminal-hangup**]：表示终端自动挂机的告警信息。

【使用指导】

开启POS终端接入模块告警功能后，系统触发相应事件后会生成指定类型的告警信息。通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

不指定可选参数时，表示开启/关闭所有类型的告警功能。

【举例】

\# 关闭FCM物理层协商失败的POS终端接入告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable posa fcm-physical-failure

【相关命令】

·**posa connection-threshold**

·**posa trade-limit tcp**

**POS终端接入 \-- POS终端接入配置命令 \-- source ip**

------------------------------------------------------------------------

**[source ip**]命令用来配置绑定TCP连接的源地址。

**[undo source ip**]命令用来取消对TCP连接源地址的绑定。

【命令】

**[source ip** *ip-address*]

**[undo source ip**]

【缺省情况】

未配置绑定TCP连接的源地址。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：与TCP连接绑定的IP地址。该IP地址必须与前置机之间路由可达，且为非环回的单播IPV4地址。

【使用指导】

对于TCP方式连接的POS应用模板，缺省情况下设备以POS应用模板接入的接口的IP地址作为源IP地址向前置机发起TCP连接。这样会暴露设备上POS应用模板接入的接口的真实IP地址，为了满足一定的安全需求，可以通过在POS应用模板上配置源地址绑定功能，指定一个特殊的IP地址作为向前置机发起TCP连接的源IP。

修改绑定TCP连接的源地址会导致该模板下已经建立的TCP连接被删除。

【举例】

\# 配置POS应用模板1的源地址为1.1.1.1，删除现有的长连接。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 source ip 1.1.1.1

Connections for the application have been reset.

**POS终端接入 \-- POS终端接入配置命令 \-- source port**

------------------------------------------------------------------------

**[source port**]命令用来配置绑定TCP连接的源端口号，即与前置机建立TCP连接时，只能使用指定的源端口号。

**[undo source port**]命令用来取消对TCP连接源端口号的绑定。

【命令】

**[source port** *port-number*]

**[undo source port**]

【缺省情况】

未绑定源端口号，与前置机建立TCP连接时将使用系统随机分配的一个未被占用的端口号。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：与TCP连接绑定的源端口号，取值范围为4000～4999。

【使用指导】

有些前置机要求设备必须以一个特定的源端口发起TCP连接，可通过本命令指定一个特殊的端口号作为向前置机发起TCP连接的源端口号。

短连接模式下，也支持配置绑定TCP连接的源端口号，但此时，此APP最多创建一条与前置机的连接，所以使用该APP并发的交易会失败。

修改绑定TCP连接的源端口号会删除该模板下已经建立的TCP连接。

指定的源端口不能和终端的监听端口重复，不能和其它应用绑定的源端口重复。

若指定源端口与系统其它进程端口重复，可配置，但该应用不生效，通过**display posa status**可看到当前系统已经占用的TCP端口。

【举例】

\# 配置TCP类型的POS应用模板1的源端口号为4001，删除已经存在的连接。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 source port 4001

Connections for the application have been reset.

**POS终端接入 \-- POS终端接入配置命令 \-- tcp keepalive**

------------------------------------------------------------------------

**[tcp keepalive**]命令用来设置发送TCP协议栈keepalive报文的相关参数。

**[undo tcp keepalive**]用来恢复缺省情况。

【命令】

**[tcp** **keepalive** **interval** *time* **count** *counts*]

**[undo tcp** **keepalive**]

【缺省情况】

设备通过向前置机发送keepalive报文，来保持该POS应用模板对应连接的连通性。

发送TCP keepalive报文的周期为2秒，当连续发送3次TCP keepalive报文没有得到回应时设备断开与该POS应用模板对应的银行前置机的TCP连接。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval** *time*]：表示keepalive报文发送时间间隔，取值范围为1～7200，单位为秒。

**[count** *counts*]：表示keepalive报文发送次数，取值范围为2～100。

【使用指导】

修改后参数会立刻生效。

【举例】

\# 配置TCP类型的POS应用模板1的keepalive报文发送间隔为100秒，发送次数为4次。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 tcp keepalive interval 100 count 4

**POS终端接入 \-- POS终端接入配置命令 \-- tcp linking-time**

------------------------------------------------------------------------

**[tcp linking-time**]命令用来设置向前置机发起TCP连接请求的超时时间，即该POS应用模板的连接发起时处于Linking状态的最大时间。

**[undo tcp linking-time**]用来恢复缺省情况。

【命令】

**[tcp linking-time** *time*]

**[undo tcp linking-time**]

【缺省情况】

允许向前置机发起TCP连接的超时时间为20秒。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：允许POS应用模板处于Linking状态的最大时间，取值范围为1～20，单位为秒。

【使用指导】

设备向前置机发起TCP连接的时间若超过设置的最大值，则取消此次TCP连接请求，此次交易失败。

修改后的配置仅对新发起的TCP连接生效。

该配置同样用于设备等待银行前置机应答AM POS机的主叫号码协商报文。

【举例】

\# 配置POS应用模板1的TCP连接状态时间为10秒。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 tcp linking-time 10

**POS终端接入 \-- POS终端接入配置命令 \-- threshold answer-tone**

------------------------------------------------------------------------

**[threshold answer-tone**]命令用来设置Modem发送应答音能量增益。

**[undo threshold answer-tone**]命令用来恢复缺省情况。

【命令】

**[threshold answer-tone**]*answertonetime*

**[undo threshold answer-tone**]

【缺省情况】

Modem发送应答音的能量增益缺省值的取值情况与设备型号有关，请以设备的实际情况为准。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[answertometime*]：Modem发送应答音的能量增益，取值范围是1～42，单位为-dBm。

【举例】

\# 设置FCM2/1/0下Modem发送应答音能量增益为-41dBm。

\<Sysname\> system-view

Sysname interface fcm 2/1/0

Sysname--Fcm2/1/0 threshold answer-tone 41

**POS终端接入 \-- POS终端接入配置命令 \-- threshold rlsdoff**

------------------------------------------------------------------------

**[threshold rlsdoff**]命令用来设置Modem协商的接收信号门限值下限。

**[undo threshold rlsdoff**]命令用来恢复缺省情况。

【命令】

**[threshold rlsdoff **]*rlsdofftime*

**[undo threshold rlsdoff**]

【缺省情况】

Modem协商的接收信号门限值下限值为-48dBm。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rlsdofftime*]：Modem接收信号门限值下限，取值范围是0～75，单位为-dBm。

【举例】

\# 设置FCM2/1/0接口下Modem协商的接收信号门限值下限为-74dBm。

\<Sysname\> system-view

Sysname interface fcm 2/1/0

Sysname--Fcm2/1/0 threshold rlsdoff 74

**POS终端接入 \-- POS终端接入配置命令 \-- threshold rlsdon**

------------------------------------------------------------------------

**[threshold rlsdon**]命令用来设置Modem协商的接收信号门限值上限。

**[undo threshold rlsdon**]命令用来恢复缺省情况。

【命令】

**[threshold rlsdon **]*rlsdontime*

**[undo threshold rlsdon**]

【缺省情况】

Modem协商的接收信号门限值上限值为-43dBm。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rlsdontime*]：Modem接收信号门限值上限，取值范围是0～75，单位为-dBm。

【举例】

\# 设置FCM2/1/0协商的接收信号门限值上限为-73dBm。

\<Sysname\> system-view

Sysname interface fcm 2/1/0

Sysname--Fcm2/1/0 threshold rlsdon 73

**POS终端接入 \-- POS终端接入配置命令 \-- threshold txpower**

------------------------------------------------------------------------

**[threshold txpower**]命令用来设置Modem协商的发送能量增益的大小。

**[undo threshold txpower**]命令用来恢复缺省情况。

【命令】

**[threshold txpower **]*txpowertime*

**[undo threshold txpower**]

【缺省情况】

Modem协商的发送能量增益值为-10dBm。

【视图】

FCM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[txpowertime*]：Modem信号发送的能量增益，取值范围是1～42，单位为-dBm。

【举例】

\# 设置FCM2/1/0协商的发送能量增益的大小为-40dBm。

\<Sysname\> system-view

Sysname interface fcm 2/1/0

Sysname--Fcm2/1/0 threshold txpower 40

**POS终端接入 \-- POS终端接入配置命令 \-- timer auto-connect**

------------------------------------------------------------------------

**[timer auto-connect**]命令用来设置POS应用模板自动建立连接的时间间隔。

**[undo timer auto-connect**]命令用来恢复缺省情况。

【命令】

**[timer auto-connect ***interval*]

**[undo timer auto-connect**]

【缺省情况】

POS应用模板自动建立连接的时间间隔为10分钟。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：长连接模式的POS应用模板自动建立连接的时间间隔，取值范围为1～1440，单位为分钟。

【使用指导】

只有长连接模式的TCP类型的POS应用模板才支持该配置。

配置该命令后，当POS应用模板与前置机之间没有建立可复用的长连接前，设备会以*interval*为时间间隔，周期性地向前置机主动发起连接。

【举例】

\# 设置自动建立连接的时间间隔为1分钟。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 timer auto-connect 1

【相关命令】

·**auto-connect enable**

**POS终端接入 \-- POS终端接入配置命令 \-- timer hello**

------------------------------------------------------------------------

**[timer hello**]用来设置POS应用模板发送握手报文的间隔时间。

**[undo timer hello**]命令用来恢复缺省情况。

【命令】

**[timer hello** *interval*]

**[undo timer hello**]

【缺省情况】

POS应用模板发送握手报文间隔为1分钟。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：POS应用模板发送握手报文的时间间隔，取值范围为1～600，单位为分钟。

【使用指导】

当开启POS应用模板握手功能时，设备以*interval*为时间间隔周期性地向前置机发送握手报文。

【举例】

\# 设置POS应用模板发送握手报文的时间间隔为10分钟。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 timer hello 10

【相关命令】

·**hello enable**

**POS终端接入 \-- POS终端接入配置命令 \-- timer quiet**

------------------------------------------------------------------------

**[timer quiet**]用来设置POS应用模板的静默时间。

**[undo timer quiet**]命令用来恢复缺省情况。

【命令】

**[timer quiet** *interval*]

**[undo timer quiet**]

【缺省情况】

POS应用模板的静默时间为600分钟。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：POS应用模板的静默时间，范围为10～600，单位为分钟。

【使用指导】

对于TCP类型的前置机，当POS机发起交易时，若设备尝试连接的前置机无响应，则将此前置机设置为Blocked状态，并开启静默定时器，在此期间，此前置机保持Blocked状态。

修改后的配置会立即生效，对已经处于静默状态的前置机重新计时。

【举例】

\#设置POS应用模板的静默时间为500分钟。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 timer quiet 500

【相关命令】

·**backup app**

**POS终端接入 \-- POS终端接入配置命令 \-- tpdu-change**

------------------------------------------------------------------------

**[tpdu-change**]命令用来配置TPDU地址的更改策略，即设备向该POS应用模板对应的前置机转发终端报文时，对报文TPDU地址的更改策略。

**[undo tpdu-change**]命令用来取消该配置。

【命令】

**[tpdu-change**  { **destination** \| **source** }]

**[undo tpdu-change**]

【缺省情况】

仅允许修改TPDU源地址。

【视图】

POS应用模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination**]：修改转发给前置机的终端报文的TPDU目的地址。

**[source**]：修改转发给前置机的终端报文的TPDU源地址。

【使用指导】

不同的前置机对可更改的TPDU地址字段的要求不同，要么仅允许更改TPDU源地址，要么仅允许更改TPDU目的地，因此需要根据前置机的要求来配置设备对于TPDU地址的更改策略。

对于非透传长连接，修改地址更改策略会删除该POS应用模板下的所有连接。

【举例】

\# 指定向POS应用模板1对应的前置机转发终端报文时，修改其TPDU目的地址，应用模板1为非透传长连接。

\<Sysname\> system-view

Sysname posa app 1 type tcp

Sysname-posa-app1 tpdu-change destination

Connections for the application have been reset.
