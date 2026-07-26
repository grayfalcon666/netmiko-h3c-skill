
**ISDN \-- ISDN配置命令 \-- display isdn active-channel**

------------------------------------------------------------------------

**[display** **isdn active-channel**]命令用来显示ISDN接口上Q.931呼叫成功的呼叫信息。

【命令】

**[display isdn active-channel** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：显示指定ISDN接口上Q.931呼叫成功的呼叫信息。*interface-type interface-number*表示接口类型和编号，可以是BRI接口或者PRI接口。如果不指定接口，则显示全部ISDN接口上Q.931呼叫成功的呼叫信息。

【使用指导】

本命令显示信息可以帮助用户进行ISDN呼叫的故障诊断。

【举例】

\# 显示接口BRI2/4/0上Q.931呼叫成功的呼叫信息。

\<Sysname\> display isdn active-channel interface bri 2/4/0

Bri 2/4/0

  Channel Info: B1

  Call Property: Analog

  Call Type: Out

  Calling Number: 1111

  Calling Subaddress:

  Called Number: 2222

  Called Subaddress:

  Start Time: 13-03-14 15:22:26

  Time Used: 00:01:10

\# 显示PRI接口上Q.931呼叫成功的呼叫信息。

\<Sysname\> display isdn active-channel interface serial 2/3/0:15

Serial2/3/0:15

  Serial2/3/0:15

  Channel Info: B2

  Call Property: Digital

  Call Type: Out

  Calling Number: 8306001

  Calling Subaddress:

  Called Number: 8306002

  Called Subaddress:

  Start Time: 13-02-14 12:22:26

  Time Used: 00:11:20

表1-1 display isdn active-channel命令显示信息描述表

字段

描述

Channel Info

呼叫使用的B通道

Call Property

呼叫性质：

·Digital：数字

·Analog：模拟

Call Type

呼叫类型：

·In：入呼叫

·Out：出呼叫

Calling Number

主叫号码

Calling Subaddress

主叫子地址

Called Number

被叫号码

Called Subaddress

被叫子地址

Start Time

呼叫成功建立时间

Time Used

呼叫建立后已经使用的时间

**ISDN \-- ISDN配置命令 \-- display isdn call-info**

------------------------------------------------------------------------

**[display isdn call-info**]命令用来显示ISDN接口的呼叫信息。

【命令】

**[display isdn call-info** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定ISDN接口的呼叫信息。*interface-type interface-number*表示接口类型和编号，可以是BRI接口或者PRI接口。如果不指定接口，则显示全部ISDN接口的呼叫信息。

【使用指导】

本命令输出的信息中包括接口上ISDN协议各层的信息，包括Q.921、Q.931和CC，用户可以根据此命令进行故障诊断。

【举例】

\# 显示接口BRI2/4/0的呼叫信息。

\<Sysname\> display isdn call-info interface bri 2/4/0

Bri2/4/0(User-side): ACTIVE

  Link Layer 1:  TEI = 65, State = MULTIPLE_FRAME_ESTABLISHED

  Link Layer 2:  TEI = NONE, State = TEI_UNASSIGNED

  Link Layer 3:  TEI = NONE, State = TEI_UNASSIGNED

  Link Layer 4:  TEI = NONE, State = TEI_UNASSIGNED

  Link Layer 5:  TEI = NONE, State = TEI_UNASSIGNED

  Link Layer 6:  TEI = NONE, State = TEI_UNASSIGNED

  Link Layer 7:  TEI = NONE, State = TEI_UNASSIGNED

  Link Layer 8:  TEI = NONE, State = TEI_UNASSIGNED

  Network Layer: 1 connections

    Connection 1:

      CallID: 0x0001, State: ACTIVE, CES: 1, Channel: 0x00000001

      TEI: 65

      Calling_Num[:Sub: 2014:1325]

      Called_Num[:Sub: 50401:24136]

\# 显示PRI接口的呼叫信息。

\<Sysname\> display isdn call-info interface serial 2/3/0:15

Serial2/3/0:15(User-side):

  Link Layer 1: TEI = 0, State = MULTIPLE_FRAME_ESTABLISHED

  Network Layer: 1 connections

    Connection 1:

      CallID: 0x0000ffff, State: ACTIVE, CES: 1, Channel: 0x00200000

      TEI: 0

      Calling_Num[:Sub: 8306001]

      Called_Num[:Sub: 8305001]

表1-2 display isdn call-info命令显示信息描述表

字段

描述

Bri2/4/0(User-side): ACTIVE

ISDN接口物理层的激活状态（BRI接口上有呼叫时才激活物理层；PRI接口只要物理UP就可以使用，不需要激活）：

·ACTIVE：接口处于激活状态

·DEACTIVE：接口处于去激活状态

·User-side表示ISDN接口工作在ISDN协议用户侧模式

Link Layer

ISDN接口二层链路的呼叫连接，协议将为每个终端建立一个呼叫连接，用TEI来区分不同的呼叫连接（PRI接口上只能建立一个呼叫连接，BRI接口上最多可以建立8个呼叫连接）

TEI

一个TEI（Terminal Endpoint Identifier，终端设备标识符）标识一个终端（比如ISDN电话），一个用户侧设备就是一个终端。TEI由网络侧设备分配

State

ISDN接口二层链路的当前状态：

·TEI_UNASSIGNED：TEI未分配

·ASSIGN_AWAITING_TEI：等待分配TEI

·ESTABLISH_AWAITING_TEI：等待分配TEI并等待多帧建链

·TEI_ASSIGNED：TEI已分配

·AWAITING_ESTABLISHMENT：等待多帧建链

·MULTIPLE_FRAME_ESTABLISHED：多帧建链成功（Q.921报文收发序号已同步）

·TIMER_RECOVER：定时器超时尝试恢复链路

·AWAITING_RELEASE：等待多帧连接断开

·TEI_ASSIGNED_EXT1：存在TEI的情况下，BRI接口收到底层去激活指示

·TEI_ASSIGNED_EXT2：存在TEI的情况下，BRI接口有新的呼叫，发起多帧建链

Network Layer: 1 connections

网络层上有一个呼叫连接

CallID

呼叫在CC层的索引

State

BRI接口三层链路的当前状态：

·NULL：初始状态，不存在呼叫

·CALL_INITIATED：发起呼叫

·OVERLAP_SENDING：重叠发送被叫号码

·OUTGOING_CALL_PROCEEDING：正在进行出呼叫

·CALL_DELIVERED：出呼叫时，远端已振铃，但未摘机

·CALL_PRESENT：发出呼叫请求，但未收到应答

·CALL_RECEIVED：入呼叫时，本端已振铃，但未摘机

·CONNECT_REQUEST：入呼叫已摘机，并发送连接请求

·INCOMING_CALL_PROCEEDING：正在进行入呼叫

·ACTIVE：呼叫成功

·DISCONNECT_REQUEST：断开呼叫请求

·DISCONNECT_INDICATION：断开呼叫指示

·SUSPEND_REQUEST：暂停请求

·RESUME_REQUEST：恢复请求

·RELEASE_REQUEST：释放请求

·OVERLAP_RECEIVING：重叠接收

CES

连接端点后缀（Q.931和Q.921协议之间用CES来标识呼叫连接）

Channel

呼叫占用的ISDN B通道的位图（位图中每个2进制位表示一个B通道，如果对应的2进制位值是1，表示B通道被占用）

Calling_Num:Sub

主叫号码 :主叫子地址

Called_Num:Sub

被叫号码 :被叫子地址

**ISDN \-- ISDN配置命令 \-- display isdn call-record**

------------------------------------------------------------------------

**[display isdn call-record**]命令用来显示ISDN的呼叫历史记录。

【命令】

**[display isdn call-record** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定ISDN接口的呼叫历史记录。*interface-type interface-number*表示接口类型和编号，可以是BRI接口或者PRI接口。如果不指定接口，则显示全部ISDN接口的呼叫历史记录。

【使用指导】

本命令显示自设备启动后到目前为止的呼叫成功的历史记录，最多可显示最新的100条记录。

【举例】

\# 显示ISDN的呼叫历史记录。

\<Sysname\> display isdn call-record

Type Caller    Called    Start time        End time          Duration(s)

Out  -         232303    13-03-20 14:10:12 -                 273

In   -         262609    13-03-20 14:04:50 13-03-20 14:08:54 244

Out  -         232303    13-03-20 14:00:47 13-03-20 14:04:07 200

In   232303    262609    13-03-20 13:48:15 13-03-20 13:49:06 51

Out  262609    232303    13-03-20 13:46:39 13-03-20 13:47:31 52

表1-3 display isdn call-record命令显示信息描述表

字段

描述

Type

呼叫类型：

·In：入呼叫

·Out：出呼叫

Caller

主叫号码

Called

被叫号码

Start time

呼叫成功建立时间

End time

呼叫停止时间

Duration

呼叫建立后已经使用的时间，单位为秒

**ISDN \-- ISDN配置命令 \-- display isdn parameters**

------------------------------------------------------------------------

**[display isdn parameters**]命令用来显示ISDN协议二层和三层系统参数。

【命令】

**[display isdn parameters**[ { *protocol* \| **interface** *interface-type interface-number* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[protocol*]：ISDN协议类型，可以取的值包括**5ess**、**ansi**、**at&t**、**dss1**、**etsi**、**ni**、**ni2**、**ntt**、**qsig**。

**[interface** *interface-type interface-number*]：指定接口类型和编号，可以是BRI接口或者PRI接口。

【使用指导】

本命令可以显示ISDN协议二层和三层系统参数，包括各种系统定时器时长以及滑动窗口尺寸信息。

需要注意的是：

·如果指定*protocol*，显示的是该协议的缺省系统参数。

·如果指定接口，显示的是该接口下的系统参数。

【举例】

\# 显示DSS1 ISDN协议的缺省系统参数。

\<Sysname\> display isdn parameters dss1

DSS1 ISDN Layer 2 system parameters:

  T200(sec)   T201(sec)   T202(sec)    T203(sec)   N200   K(BRI)    K(PRI)

  1           1           2            10          3      1         7

DSS1 ISDN Layer 3 system timers(default values):

  Timer                 Value(sec)

  T301                  240

  T302                  15

  T303                  4

  T304                  30

  T305                  30

  T308                  4

  T309                  90

  T310                  40

  T313                  4

  T322                  4

\# 显示PRI接口的系统参数。

\<Sysname\> display isdn parameters interface serial 2/3/0:15

Serial2/3/0:15(Network-side):

QSIG ISDN Layer 2 system parameters:

  T200(sec)   T201(sec)   T202(sec)    T203(sec)   N200   K(PRI)

  1           1           2            10          3      7

QSIG ISDN Layer 3 system timers:

  Timer                 Value(sec)

  T301                  35

  T302                  37

  T303                  8

  T304                  50

  T305                  20

  T308                  3

  T309                  130

  T310                  130

  T313                  6

  T322                  8

表1-4 display isdn parameters命令显示信息描述表

字段

描述

T200(sec)

ISDN二层协议的重传定时器，单位为秒

T201(sec)

ISDN二层协议的TEI检测请求的重发定时器，单位为秒

T202(sec)

ISDN二层协议的TEI请求消息的重发定时器，单位为秒

T203(sec)

ISDN二层协议的链路最大空闲时间，单位为秒

N200

最大重传次数

K(BRI)

ISDN BRI接口上允许的最大未确认帧数（滑动窗口尺寸）

K(PRI)

ISDN PRI接口上允许的最大未确认帧数（滑动窗口尺寸）

Timer

ISDN三层定时器

Value(sec)

ISDN三层定时器时长，单位为秒

**ISDN \-- ISDN配置命令 \-- display isdn spid**

------------------------------------------------------------------------

**[display isdn spid**]命令用来显示采用NI协议的BRI接口上SPID的相关信息。

【命令】

**[display isdn spid** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：指定接口类型和编号。只能是采用NI协议的BRI接口。如果不指定接口，则查看所有采用NI协议的BRI接口的SPID的相关信息。

【使用指导】

在ISDN运行过程中，当需要查看SPID的类型、SPID取值等信息的时候，可以使用本命令。

【举例】

\# 显示支持NI协议的接口BRI2/4/0上的SPID信息（SPID类型为AUTO）。

\<Sysname\> display isdn spid interface bri 2/4/0

Interface Bri2/4/0:

  SPID Type: AUTO

  SPID B1:

SPID Num: 235

    Neg State: SPID_UNASSIGNED

    Init State: INIT_NULL

SPID B2:

    SPID Num: 326

    Neg State: SPID_UNASSIGNED

Init State: INIT_NULL

  SPID timer: 30 seconds

  SPID resend: 1 times

\# 显示支持NI协议的接口BRI2/4/0上的SPID信息（SPID类型为STATIC）。

\<Sysname\> display isdn spid interface bri 2/4/0

Interface Bri2/4/0:

  SPID Type: STATIC

  SPID B1:

    SPID Num: 134

    LDN: 3251

    Init State: INIT_NULL

  SPID B2:

    SPID Num: 257

    LDN: 3657

    Init State: INIT_NULL

  SPID timer: 30 seconds

  SPID resend: 1 times

\# 显示支持NI协议的接口BRI2/4/0上的SPID信息（SPID类型为NIT）。

\<Sysname\> display isdn spid interface bri 2/4/0

Interface Bri2/4/0:

  SPID Type: NIT

表1-5 display isdn spid命令显示信息描述表

字段

描述

SPID Type

SPID类型，包括：

·NIT：非初始化终端模式

·STATIC：静态模式，只包括L3初始化过程

·AUTO：动态模式，包括协商和L3初始化两个过程

SPID B1

BRI接口B1通道的SPID信息

SPID B2

BRI接口B2通道的SPID信息

SPID Num

SPID值，可能是静态配置，也可能是动态协商获取，依赖于SPID Type

LDN

本地拨号号码

Neg State

SPID的协商状态，包括：

·SPID_UNASSIGNED：SPID还未分配或分配失败

·ASSIGN_AWAITING_SPID：终端已经发起Auto-SPID请求，但SPID还未分配

·SPID_ASSIGNED：程控交换机已经完成SPID的分配且终端自动选择了一个SPID

·ASSIGN_AWAITING_CALL_CLEAR：当前存在呼叫时，收到Auto-SPID请求后进入该状态

Init State

SPID的L3初始化状态，包括：

·INIT_NULL：L3还未初始化

·INIT_IND：程控交换机发起L3初始化

·INIT_PROCEEDING：L3初始化正在进行

·INIT_END：L3初始化成功

·INIT_AWAITING_CALL_CLEAR：当前存在呼叫时，收到L3初始化请求后进入该状态

SPID timer

定时器TSPID的时长

SPID resend

SPID消息重传次数

**ISDN \-- ISDN配置命令 \-- isdn bch-local-manage**

------------------------------------------------------------------------

**[isdn bch-local-manage**]命令用来配置本地管理ISDN B通道。

**[undo isdn bch-local-manage**]命令用来恢复缺省情况。

【命令】

**[isdn bch-local-manage** [ **exclusive** ]]

**[undo isdn bch-local-manage**]

【缺省情况】

未配置本地管理ISDN B通道，由程控交换机负责B通道的管理。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[exclusive**]：强制本地管理B通道模式，这种模式下如果程控交换机指示的B通道与本地的要求不一致时，将会导致呼叫失败。

【使用指导】

在呼叫过程中，对呼叫所用B通道进行适当的管理是很重要的，尤其是在PRI方式下，适当的通道管理可以提高呼叫效率，减小呼叫损耗。一般来说，由程控交换机统一对B通道进行管理是比较合适的方式，所以虽然设备提供了B通道本地管理功能，但建议还是以程控交换机为主。

当用户配置了**isdn bch-local-manage**命令后，设备将工作于本地管理B通道的模式，由本地自主选择空闲的B通道。但即使设置了本地管理B通道，程控交换机仍然享有优先权。即：如果程控交换机选定了一条与本地指定的B通道不同的空闲通道，设备还是会按照程控交换机的指示完成通信。

当用户配置了**isdn bch-local-manage exclusive**命令后，设备将工作于强制本地管理B通道的模式。即：在出呼叫Setup消息的Channel ID信息单元中会指示B通道为"必选，不可更改"，由本地来分配一条空闲的B通道，如果程控交换机指示的B通道与之前本地的要求不一致时，将会导致呼叫失败。

【举例】

\# 配置接口BRI2/4/0工作于本地管理B通道的模式。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn bch-local-manage

【相关命令】

·**isdn bch-select-way**

**ISDN \-- ISDN配置命令 \-- isdn bch-select-way**

------------------------------------------------------------------------

**[isdn bch-select-way**]命令用来配置ISDN B通道的选择方式。

**[undo isdn bch-select-way**]命令用来恢复缺省情况。

【命令】

**[isdn bch-select-way**[ { **ascending** \| **descending** }]]

**[undo isdn bch-select-way**]

【缺省情况】

如果用**isdn bch-local-manage**命令配置了本地管理ISDN B通道，则按照升序方式选择ISDN B通道。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ascending**]：按照升序方式选择ISDN B通道，即按照B通道编号从小到大的顺序循环进行选择。

**[descending**]：按照降序方式选择ISDN B通道，即按照B通道编号从大到小的顺序循环进行选择。

【使用指导】

在程控交换机管理ISDN B通道的情况下，本命令不起作用。

如果用户侧不配置**isdn bch-local-manage**命令，则配置**isdn bch-select-way**命令无效。

【举例】

\# 设置接口BRI2/4/0的B通道选择方式为降序方式。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn bch-select-way descending

【相关命令】

·**isdn bch-local-manage**

**ISDN \-- ISDN配置命令 \-- isdn bri-slipwnd-size**

------------------------------------------------------------------------

**[isdn bri-slipwnd-size**]命令用来配置ISDN BRI接口的滑动窗口的大小。

**[undo isdn bri-slipwnd-size**]命令用来恢复缺省情况。

【命令】

**[isdn bri-slipwnd-size** *window-size*]

**[undo isdn bri-slipwnd-size**]

【缺省情况】

ISDN BRI接口的滑动窗口大小为1。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-size*]：滑动窗口大小，取值范围为1～7。

【使用指导】

Q.921缓冲区中的帧是按序号发送的，每个发送出去的帧都要被接收端确认。系统在发送时会连续发送几帧，但在发送时会判断未确认帧的个数，如果V（A） ＋ K ＝ V（S），则不再进行发送。其中，V（A）是已确认帧的序号，V（S）是下次要发送帧的序号，K是滑动窗口大小。

滑动窗机制使得系统在发送帧时不必等待上一帧的确认，提高了发送效率。滑动窗口的大小决定了未确认帧的最大个数。

【举例】

\# 配置接口BRI2/4/0的滑动窗口大小为7。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn bri-slipwnd-size 7

【相关命令】

·**isdn pri-slipwnd-size**

**ISDN \-- ISDN配置命令 \-- isdn caller-number**

------------------------------------------------------------------------

**[isdn caller-number**]命令用来配置允许呼入的主叫号码。

**[undo isdn caller-number**]用来删除配置的允许呼入的主叫号码。

【命令】

**[isdn caller-number** *caller-number*]

**[undo isdn caller-number**]

【缺省情况】

不对呼入的主叫号码进行检查。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[caller-number*]：表示允许呼入的主叫号码，为1～24个字符的字符串，不区分大小写。

【使用指导】

配置本命令后，如果收到的呼叫建立消息中未携带主叫号码或者携带的主叫号码和本命令配置的不一样，都将导致呼叫失败。

【举例】

\# 配置允许呼入的主叫号码为400。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn caller-number 400

【相关命令】

·**isdn calling**

**ISDN \-- ISDN配置命令 \-- isdn calling**

------------------------------------------------------------------------

**[isdn calling**]命令用来配置在出呼叫中携带主叫号码。

**[undo isdn calling**]命令用来恢复缺省情况。

【命令】

**[isdn calling ***calling-number*]

**[undo isdn calling**]

【缺省情况】

语音业务的出呼叫中携带主叫号码，其他业务的出呼叫中不携带主叫号码。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[calling-number*]：主叫号码，为1～24个字符的字符串，不区分大小写。

【使用指导】

主叫方配置该命令把主叫号码发送给被叫方后，被叫方通过查看**display isdn call-info**命令就可以看到主叫方号码。如果被叫方配置了允许呼入的主叫号码，则被叫方会对主叫方发送过来的主叫号码进行检查。

需要注意：

·需要注意的是，配置了**isdn calling**命令后，如果电话网络中的程控交换机可以携带主叫号码，那么主叫号码可以发送给被叫方，如果电话网络中的程控交换机不能携带主叫号码，那么主叫号码也不能发送给被叫方。

·对于语音业务，不建议通过本命令配置出呼叫中携带的主叫号码。

【举例】

\# 配置接口BRI2/4/0在出呼叫中携带主叫号码8060170。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn calling 8060170

【相关命令】

·**display isdn call-info**

·**isdn caller-number**

**ISDN \-- ISDN配置命令 \-- isdn carry calling-name**

------------------------------------------------------------------------

**[isdn carry calling-name**]命令用来配置ISDN协议在出方向报文中携带calling-name字段。

**[undo isdn carry calling-name**]命令用来恢复缺省情况。

【命令】

**[isdn carry calling-name**]

**[undo isdn carry calling-name**]

【缺省情况】

ISDN协议在出方向报文中不携带calling-name字段。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在主叫方配置本命令后，被叫方可以看到主叫方的名字。

当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0在出方向报文中携带calling-name字段。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn carry calling-name

【相关命令】

·**isdn carry connected-name**

**ISDN \-- ISDN配置命令 \-- isdn carry connected-name**

------------------------------------------------------------------------

**[isdn carry connected-name**]命令用来配置ISDN协议在出方向报文中携带connected-name字段。

**[undo isdn carry connected-name**]命令用来恢复缺省情况。

【命令】

**[isdn carry connected-name**]

**[undo isdn carry connected-name**]

【缺省情况】

ISDN协议在出方向报文中不携带connected-name字段。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在被叫方配置本命令后，主叫方可以看到被叫方的名字。

当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0在出方向报文中携带connected-name字段。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn carry connected-name

【相关命令】

·**isdn carry calling-name**

**ISDN \-- ISDN配置命令 \-- isdn check-called-number**

------------------------------------------------------------------------

**[isdn check-called-number**]命令用来设置入呼叫时需要检查的被叫号码或子地址。

**[undo isdn check-called-number**]命令用来取消已有的设置。

【命令】

**[isdn check-called-number ***check-index called-party-number*]

**[undo isdn check-called-numbe**r *check-index*]

【缺省情况】

入呼叫时不对被叫号码或子地址进行检查。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[check-index*]：被叫号码或子地址检查的索引，取值范围为1～3。

*[called-party-number*]：被叫号码和子地址，为1～40个字符的字符串，区分大小写。被叫号码和子地址之间以冒号分隔。

【使用指导】

本命令用于设置入呼叫时的检查项。可以只配置被叫号码，也可以同时配置被叫号码和子地址。

只要设定了被叫号码或者子地址，当对方未发送或发送错被叫号码或者子地址时，设备就会拒绝该呼叫。

同时配置被叫号码和子地址时，被叫号码和子地址之间以冒号分隔。

【举例】

\# 设置接口BRI2/4/0数字入呼叫时检查号码为66668888，子地址为13525。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn check-called-number 1 66668888:13525

**ISDN \-- ISDN配置命令 \-- isdn crlength**

------------------------------------------------------------------------

**[isdn crlength**]命令用来配置ISDN接口发起呼叫时所使用呼叫参考的长度。

**[undo isdn crlength**]命令用来恢复缺省情况。

【命令】

**[isdn crlength***call-reference-length*]

**[undo isdn crlength**]

【缺省情况】

CE1 PRI接口和CT1 PRI接口的呼叫参考的长度为2字节，BRI接口的呼叫参考的长度为1字节。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[call-reference-length*]：ISDN接口发起呼叫时所使用呼叫参考的长度，取值为1或2，单位为字节。

【使用指导】

呼叫参考相当于协议为每个呼叫分配的序列号，长度为1或2字节，循环使用。

通常情况下，当设备收到呼叫时，可以自动识别呼叫参考的长度。但是网络上的某些设备不能自动识别呼叫参考的长度，当本地设备与这种设备对接并向其发出呼叫时，就需要配置本地设备呼叫时所使用的呼叫参考长度与对端一致。

当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置PRI接口Serial2/3/0:15上ISDN消息所带的呼叫参考的长度为1字节。

\<Sysname\> system-view

Sysname interface serial 2/3/0:15

Sysname-Serial2/3/0:15 isdn crlength 1

**ISDN \-- ISDN配置命令 \-- isdn ignore connect-ack**

------------------------------------------------------------------------

**[isdn ignore connect-ack incoming**]命令用来配置ISDN协议在发送了CONNECT消息之后无需等待程控交换机的CONNECT ACK消息，直接切换到ACTIVE状态，并开始数据和语音业务的通信。

**[undo isdn ignore connect-ack incoming**]命令用来恢复ISDN协议在发送CONNECT消息之后的缺省处理方式。

**[isdn ignore connect-ack outgoing**]命令用来配置ISDN协议在收到CONNECT消息之后，不向对端发送CONNECT ACK消息，直接切换到ACTIVE状态。

**[undo isdn ignore connect-ack outgoing**]命令用来恢复ISDN协议在收到CONNECT消息之后的缺省处理方式。

**[isdn ignore connect-ack**]命令的作用相当于同时配置命令**isdn ignore connect-ack incoming**和**isdn ignore connect-ack outgoing**。

**[undo isdn ignore connect-ack**]命令用来恢复ISDN协议在发送和收到CONNECT消息之后的缺省处理方式。

【命令】

**[isdn ignore connect-ack**[ [ **incoming** \| **outgoing** ]]]

**[undo isdn ignore connect-ack**[ [ **incoming** \| **outgoing** ]]]

【缺省情况】

当设备和程控交换机互通时：

·ISDN协议在发送了CONNECT消息之后，需要等待接收到程控交换机的CONNECT ACK消息后才切换到ACTIVE状态，并开始数据和语音业务的通信。

·ISDN协议在收到CONNECT消息之后，需要向对端回应CONNECT ACK消息，并切换到ACTIVE状态。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[incoming**]：ISDN协议在发送CONNECT消息之后，无需等待程控交换机的CONNECT ACK消息，直接切换到ACTIVE状态。

**[outgoing**]：ISDN协议在收到CONNECT消息之后，不向对端发送CONNECT ACK消息，直接切换到ACTIVE状态。

【使用指导】

当设备和程控交换机互通时，应与程控交换机的设置一致。

当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0上呼叫过程无需等待CONNECT ACK消息直接切换到ACTIVE状态。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn ignore connect-ack incoming

\# 配置接口BRI2/4/0上呼叫过程不发送CONNECT ACK消息直接切换到ACTIVE状态。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn ignore connect-ack outgoing

**ISDN \-- ISDN配置命令 \-- isdn ignore hlc**

------------------------------------------------------------------------

**[isdn ignore hlc**]命令用来配置在ISDN发起语音呼叫时Setup消息中不携带高层兼容性信息单元。

**[undo isdn ignore hlc**]命令用来恢复缺省情况。

【命令】

**[isdn ignore hlc**]

**[undo isdn ignore hlc**]

【缺省情况】

当ISDN协议为5ESS、QSIG时都不携带高层兼容性信息单元，在其他ISDN协议下都携带高层兼容性信息单元。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当设备和程控交换机互通时，应与程控交换机的设置一致。

当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0上发起语音呼叫时在Setup消息中不携带高层兼容性单元。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn ignore hlc

**ISDN \-- ISDN配置命令 \-- isdn ignore llc**

------------------------------------------------------------------------

**[isdn ignore llc**]命令用来配置在ISDN发起语音呼叫时Setup消息中不携带低层兼容性信息单元。

**[undo isdn ignore llc**]命令用来恢复缺省情况。

【命令】

**[isdn ignore llc**]

**[undo isdn ignore llc**]

【缺省情况】

当ISDN协议为5ESS、QSIG时都不携带低层兼容性信息单元，在其他ISDN协议下都携带低层兼容性信息单元。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当设备和程控交换机互通时，应与程控交换机的设置一致。

当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0上发起语音呼叫时在Setup消息中不携带低层兼容性单元。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn ignore llc

**ISDN \-- ISDN配置命令 \-- isdn ignore sending-complete**

------------------------------------------------------------------------

**[isdn ignore sending-complete**]命令用来配置ISDN协议在入呼叫和出呼叫方向上对发送完全信息单元（Sending Complete Information Element）的处理。

**[undo isdn ignore sending-complete**]命令用来恢复缺省情况。

【命令】

**[isdn ignore sending-complete**[ [ **incoming** \| **outgoing** ]]]

**[undo isdn ignore sending-complete**[ [ **incoming** \| **outgoing** ]]]

【缺省情况】

当设备和程控交换机互通时，对于入呼叫，检查接收到的Setup消息是否携带发送完全信息单元，对于出呼叫，发送Setup消息时携带发送完全信息单元。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[incoming**]：对于入呼叫，不检查接收到的Setup消息是否携带发送完全信息单元。

**[outgoing**]：对于出呼叫，发送Setup消息时不携带发送完全信息单元。

【使用指导】

发送完全信息单元的作用如下：

·出呼叫发送Setup消息时，如果Setup消息中携带发送完全信息单元，表示号码完全发送，否则，表示号码没有完全发送。

·入呼叫收到Setup消息时，如果Setup消息中携带发送完全信息单元，表示号码完全接收，否则，表示号码没有完全接收。

需要注意的是：

·如果配置命令时不指定**incoming**和**outgoing**参数，表示对于入呼叫和出呼叫都进行处理。

·当设备和程控交换机互通时，应与程控交换机的设置一致。

·本命令只能在接口ISDN协议为DSS1、QSIG或者ETSI时有意义，其他协议不支持该信息单元。

·当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置BRI2/4/0接口对于入呼叫，不检查接收到的Setup消息是否携带发送完全信息单元。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn ignore sending-complete incoming

\# 配置BRI2/4/0接口对于出呼叫，发送Setup消息时不携带发送完全信息单元。

Sysname-Bri2/4/0 isdn ignore sending-complete outgoing

【相关命令】

·**isdn protocol-type**

**ISDN \-- ISDN配置命令 \-- isdn l3-timer**

------------------------------------------------------------------------

**[isdn l3-timer**]命令用来配置ISDN协议三层定时器的时长。

**[undo isdn l3-timer**]命令用来恢复缺省情况。

【命令】

**[isdn l3-timer**] *timer-name time-interval*

**[undo isdn l3-timer**  { *timer-name* \| **all** }]

【缺省情况】

不同类型ISDN协议的三层定时器时长的缺省值不同，用户可以通过**display isdn parameters**命令查看各ISDN协议的三层定时器时长的缺省值。[表]1-6(?1004680360#_Ref350177789)中列出的是DSS1 ISDN协议的三层定时器时长的缺省值。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timer-name*]：ISDN协议三层定时器名字，取值范围见[表]1-6(?1004680360#_Ref350177789)。

*[time-interval*]：定时器时长，取值范围见[表]1-6(?1004680360#_Ref350177789)。

**[all**]：用于恢复所有三层定时器的缺省时长。

表1-6 ISDN协议三层定时器说明

*[timer-name*]

定时器名

取值范围（单位：秒）

缺省值（单位：秒）

t301

T301

30～1200

240

t302

T302

1～60

15

t303

T303

2～10

4

t304

T304

10～60

30

t305

T305

4～30

30

t308

T308

2～10

4

t309

T309

1～240

90

t310

T310

10～240

40

t313

T313

2～10

4

t322

T322

2～10

4

【使用指导】

T302、T304定时器和重叠发送有关，如果当前ISDN网络层协议不支持重叠发送则不支持该定时器配置。AT&T、NTT、NI2、5ESS协议不支持T302、T304定时器配置。

【举例】

\# 配置接口BRI2/4/0上ISDN协议的T301定时器的时长为160秒。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn l3-timer t301 160

【相关命令】

·**display isdn parameters**

·**isdn overlap-sending**

**ISDN \-- ISDN配置命令 \-- isdn link-mode p2p**

------------------------------------------------------------------------

**[isdn **]**[link-mode**]** p2p**命令用来配置BRI接口工作在点到点模式下。

**[undo isdn link-mode**]命令用来恢复缺省情况。

【命令】

**[isdn link-mode p2p**]

**[undo isdn link-mode**]

【缺省情况】

BRI接口工作在点到多点模式下。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

ISDN BRI接口有两种工作模式：点到点、点到多点。工作在点到点模式下的BRI接口只能连接一台终端设备，工作在点到多点的BRI接口可以连接多台终端设备。

某些程控交换机只能工作在点到点模式下，为了互通，需要配置BRI接口工作在点到点模式下。当一个BRI接口通过程控交换机连接多台ISDN电话时，需要配置BRI接口工作在点到多点模式下。

需要注意的是：

·当BRI接口配置了**isdn two-tei**命令时，不能配置BRI接口工作在点到点模式。

·当BRI接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置BRI接口工作在点到点模式下。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn link-mode p2p

【相关命令】

·**isdn two-tei**

**ISDN \-- ISDN配置命令 \-- isdn number-property**

------------------------------------------------------------------------

**[isdn number-property**]命令用来配置ISDN入呼叫或出呼叫时的主叫号码或被叫号码的号码类型和编码方案。

**[undo isdn number-property**]命令用来恢复缺省的ISDN入呼叫或出呼叫时的主叫号码或被叫号码的号码类型和编码方案处理方式。

【命令】

**[isdn number-property**[ *number-property* [ **calling** \| **called**   **in** \| **out** ]]]

**[undo isdn number-property**[ [ **calling** \| **called**   **in** \| **out** ]]]

【缺省情况】

ISDN号码类型和编码方案的缺省处理方式为：根据上层具体业务的不同，系统采用相应的号码类型和编码方案。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number-property*]：ISDN号码的号码类型和编码方案，取值范围为十六进制的0～7F。用8比特的格式表示时，其中1-4位为编码方案，5-7位为号码类型，第8位为保留位。号码类型和编码方案的值见[表]1-7(?1303654043#_Ref350178785)，更加详细的定义请参考相关协议中的描述。

**[calling**]：配置主叫号码所固定使用的号码类型以及编码方案。

**[called**]：配置被叫号码所固定使用的号码类型以及编码方案。

**[in**]：配置入呼叫时的calling、called号码所固定使用的号码类型以及编码方案。

**[out**]：配置出呼叫时的calling、called号码所固定使用的号码类型以及编码方案。

表1-7 ISDN号码的号码类型和编码方案

协议

字段（位）值

定义

号码类型

编码方案

8

7

6

5

4

3

2

1

AT&T

0

0

0

0

主叫号码信息单元

号码类型：

编码方案：Unknown

0

0

0

1

主叫号码信息单元

号码类型：-

编码方案：ISDN/telephony numbering plan( Recommendation E.164)

0

0

1

1

主叫号码信息单元

号码类型：-

编码方案：Data numbering plan( Recommendation X.121)

0

1

0

0

主叫号码信息单元

号码类型：-

编码方案：Telex numbering plan( Recommendation F.69)

1

0

0

0

主叫号码信息单元

号码类型：-

编码方案：National standard numbering plan

1

0

0

1

主叫号码信息单元

号码类型：-

编码方案：Private numbering plan

1

1

1

1

主叫号码信息单元

号码类型：-

编码方案：Reserved for extension

ANSI

ETSI

DSS1

NTT

0

0

0

0

主叫号码信息单元或者被叫号码信息单元

号码类型：-

编码方案：Unknown

0

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：-

编码方案：ISDN/telephony numbering plan( Recommendation E.164)

0

0

1

1

**[步骤1**主叫号码信息单元或者被叫号码信息单元]

**[步骤2**号码类型：-]

编码方案：Data numbering plan( Recommendation X.121)

0

1

0

0

**[步骤3**主叫号码信息单元或者被叫号码信息单元]

**[步骤4**号码类型：-]

编码方案：Telex numbering plan( Recommendation F.69)

1

0

0

0

**[步骤5**主叫号码信息单元或者被叫号码信息单元]

**[步骤6**号码类型：-]

编码方案：National standard numbering plan

1

0

0

1

**[步骤7**主叫号码信息单元或者被叫号码信息单元]

**[步骤8**号码类型：-]

编码方案：Private numbering plan

1

1

1

1

**[步骤9**主叫号码信息单元或者被叫号码信息单元]

**[步骤10**号码类型：-]

编码方案：Reserved for extension

NI

0

0

0

0

0

0

0

**[步骤11**被叫号码信息单元]

**[步骤12**号码类型：Unknown]

编码方案：Unknown

0

0

0

0

0

0

1

**[步骤13**主叫号码信息单元]

**[步骤14**号码类型：Unknown]

编码方案：ISDN/telephony numbering plan( Recommendation E.164)

0

0

0

0

0

1

1

**[步骤15**主叫号码信息单元]

**[步骤16**号码类型：Unknown]

编码方案：Data numbering plan( Recommendation X.121)

0

0

0

0

1

0

0

**[步骤17**主叫号码信息单元]

**[步骤18**号码类型：Unknown]

编码方案：Telex numbering plan (Recommendation F.69)

0

0

0

1

0

0

0

**[步骤19**主叫号码信息单元]

**[步骤20**号码类型：Unknown]

编码方案：National standard numbering plan

0

0

0

1

0

0

1

**[步骤21**主叫号码信息单元]

**[步骤22**号码类型：Unknown]

编码方案：Private numbering plan

0

0

0

1

1

1

1

**[步骤23**主叫号码信息单元]

**[步骤24**号码类型：Unknown]

编码方案：Reserved for extension

0

1

0

0

0

0

1

**[步骤25**被叫号码信息单元]

**[步骤26**号码类型：National number]

编码方案：ISDN/telephony numbering plan( Recommendation E.164)

0

1

1

1

0

0

1

**[步骤27**被叫号码信息单元]

**[步骤28**号码类型：Network specific number]

编码方案：ISDN/telephony numbering plan( Recommendation E.164)

1

0

0

0

0

0

1

**[步骤29**被叫号码信息单元]

**[步骤30**号码类型：Unknown]

编码方案：ISDN/telephony numbering plan( Recommendation E.164)

1

1

0

1

0

0

1

**[步骤31**被叫号码信息单元]

**[步骤32**号码类型：Abbreviated number]

编码方案：Private numbering plan

NI2

0

0

0

0

0

0

0

**[步骤33**主叫号码信息单元]

**[步骤34**号码类型：Unknown]

编码方案：Unknown

0

0

1

0

0

0

1

**[步骤35**主叫号码信息单元]

**[步骤36**号码类型：International number]

编码方案：ISDN/telephony numbering plan (Recommendation E.164)

0

1

0

0

0

0

1

**[步骤37**主叫号码信息单元]

**[步骤38**号码类型：National number]

编码方案：ISDN/telephony numbering plan (Recommendation E.164)

1

0

0

0

0

0

1

**[步骤39**主叫号码信息单元]

**[步骤40**号码类型：Subscriber number]

编码方案：ISDN/telephony numbering plan (Recommendation E.164)

0

0

1

0

0

1

1

**[步骤41**主叫号码信息单元]

**[步骤42**号码类型：International number]

编码方案：Data numbering plan (Recommendation X.121)

1

0

0

1

0

0

1

**[步骤43**主叫号码信息单元]

**[步骤44**号码类型：Subscriber number]

编码方案：Private numbering plan

1

1

0

1

0

0

1

**[步骤45**主叫号码信息单元]

**[步骤46**号码类型：Abbreviated number]

编码方案：Private numbering plan

5ESS

0

0

0

**[步骤47**主叫号码信息单元或者被叫号码信息单元]

**[步骤48**号码类型：Unknown]

编码方案：-

0

0

1

**[步骤49**主叫号码信息单元或者被叫号码信息单元]

**[步骤50**号码类型：International number]

编码方案：-

0

1

0

**[步骤51**主叫号码信息单元或者被叫号码信息单元]

**[步骤52**号码类型：National number]

编码方案：-

0

1

1

**[步骤53**主叫号码信息单元或者被叫号码信息单元]

**[步骤54**号码类型：Network specific number]

编码方案：-

1

0

0

**[步骤55**主叫号码信息单元或者被叫号码信息单元]

**[步骤56**号码类型：Subscriber number]

编码方案：-

0

0

0

0

**[步骤57**主叫号码信息单元或者被叫号码信息单元]

**[步骤58**号码类型：-]

编码方案：Unknown

0

0

0

1

**[步骤59**主叫号码信息单元或者被叫号码信息单元]

**[步骤60**号码类型：-]

编码方案：ISDN/telephony numbering plan (Recommendation E.164)

0

0

1

0

**[步骤61**主叫号码信息单元或者被叫号码信息单元]

**[步骤62**号码类型：-]

编码方案：Data numbering plan (Recommendation X.121)

1

0

0

1

**[步骤63**主叫号码信息单元或者被叫号码信息单元]

**[步骤64**号码类型：-]

编码方案：Private numbering plan

QSIG

0

0

0

0

0

0

0

**[步骤65**主叫号码信息单元或者被叫号码信息单元]

**[步骤66**号码类型：Unknown]

编码方案：Unknown

0

0

0

0

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：Unknown

编码方案：ISDN/telephony numbering plan (Recommendation E.164)

0

0

1

0

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：International number

编码方案：ISDN/telephony numbering plan (Recommendation E.164)

0

1

0

0

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：National number

编码方案：ISDN/telephony numbering plan (Recommendation E.164)

1

0

0

0

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：Network specific number

编码方案：ISDN/telephony numbering plan (Recommendation E.164)

0

0

0

1

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：Unknown

编码方案：Private numbering plan

0

0

1

1

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：International number

编码方案：Level 2 regional number in private numbering plan

0

1

0

1

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：National number

编码方案：Private numbering plan

0

1

1

1

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：Network specific number

编码方案：Private numbering plan

1

0

0

1

0

0

1

主叫号码信息单元或者被叫号码信息单元

号码类型：Subscriber number

编码方案：Private numbering plan

【举例】

\# 设置接口BRI2/4/0上ISDN入呼叫时主叫号码的号码类型为未知(Unknown)，编码方案为未知(Unknown)。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn number-property 0 calling in

\# 设置接口BRI2/4/0上ISDN出呼叫时被叫号码的号码类型为未知，编码方案为未知。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn number-property 0 called out

**ISDN \-- ISDN配置命令 \-- isdn overlap-sending**

------------------------------------------------------------------------

**[isdn overlap-sending**]命令用来配置ISDN接口被叫号码的发送方式为重叠发送。

**[undo isdn overlap-sending**]命令用来恢复缺省情况。

【命令】

**[isdn overlap-sending** [ *digits* ]]

**[undo isdn overlap-sending**]

【缺省情况】

ISDN接口被叫号码的发送方式为整体发送。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[digits*]：重叠发送的时候每次最多能发送的号码位数，取值范围为1～15，缺省每次最多发送10位。

【使用指导】

当ISDN接口采用"重叠发送"方式发送被叫号码时，被叫号码将会分几次发送，每次最多发送此命令设置的位数。当ISDN接口采用"整体发送"方式发送被叫号码时，被叫号码将会一次发送完成。

需要注意的是：

·AT&T、NTT、NI2、5ESS协议不支持重叠发送。

·当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0采用重叠发送方式发送被叫号码，每次最多发送12位被叫号码。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn overlap-sending 12

**ISDN \-- ISDN配置命令 \-- isdn pri-slipwnd-size**

------------------------------------------------------------------------

**[isdn pri-slipwnd-size**]命令用来配置ISDN PRI接口的滑动窗口的大小。

**[undo isdn pri-slipwnd-size**]命令用来恢复缺省情况。

【命令】

**[isdn pri-slipwnd-size** *window-size*]

**[undo isdn pri-slipwnd-size**]

【缺省情况】

ISDN PRI接口的滑动窗口大小为7。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-size*]：滑动窗口大小，取值范围为5～64。

【使用指导】

Q.921缓冲区中的帧是按序号发送的，每个发送出去的帧都要被接收端确认。系统在发送时会连续发送几帧，但在发送时会判断未确认帧的个数，如果V（A） ＋ K ＝ V（S），则不再进行发送。其中，V（A）是已确认帧的序号，V（S）是下次要发送帧的序号，K是滑动窗口大小。

滑动窗机制使得系统在发送帧时不必等待上一帧的确认，提高了发送效率。滑动窗口的大小决定了未确认帧的最大个数。

【举例】

\# 配置接口CE1/PRI2/3/0的滑动窗口大小为10。

\<Sysname\> system-view

Sysname controller e1 2/3/0

Sysname-E1 2/3/0 using ce1

Sysname-E1 2/3/0 pri-set

Sysname-E1 2/3/0 quit

Sysname interface serial 2/3/0:15

Sysname-Serial2/3/0:15 isdn pri-slipwnd-size 10

【相关命令】

·**isdn bri-slipwnd-size**

**ISDN \-- ISDN配置命令 \-- isdn progress-indicator**

------------------------------------------------------------------------

**[isdn progress-indicator**]命令用来配置ISDN信令中的Progress indicator值。

**[undo isdn progress-indicator**]命令用来恢复缺省情况。

【命令】

**[isdn progress-indicator** *indicator*]

**[undo isdn progress-indicator**]

【缺省情况】

ISDN信令使用上层语音业务指示的Progress indicator值。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[indicator*]：Progress indicator值，取值范围如[表]1-8(?1282364247#_Ref350179519)所示。

表1-8 Progress indicator值

取值

描述

1

呼叫不是端到端的ISDN呼叫；进一步的呼叫进展信息可能在带内提供

2

终点设备不是ISDN设备

3

源设备不是ISDN设备

4

呼叫已返回到ISDN网

5

互通发生，导致通信服务改变（比如由ISDN网进入VoIP网）

8

D信道上有除ISDN信令之外的其他业务信息（例如X.25的虚呼叫信令）

【使用指导】

Progress indicator值描述了在呼叫期间发生的事件。为了跟某些程控交换机互通，需要配置该值。

【举例】

\# 配置ISDN信令中的Progress indicator值为8。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn progress-indicator 8

**ISDN \-- ISDN配置命令 \-- isdn progress-to-alerting enable**

------------------------------------------------------------------------

**[isdn progress-to-alerting enable**]命令用来配置ISDN接口上把接收到的Progress消息转义成Alerting消息的功能。

**[undo isdn progress-to-alerting enable**]命令用来恢复缺省情况。

【命令】

**[isdn progress-to-alerting enable**]

**[undo isdn progress-to-alerting enable**]

【缺省情况】

Progress消息转义成Alerting消息的功能处于关闭状态。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在ISDN进行语音业务呼叫流程中，按照标准协议由Alerting消息来表示振铃。但也有一些设备通常采用Progress消息来表示振铃指示，这种使用环境下需要把接收到Progress消息转义成Alerting消息处理。因此为灵活适用各种情况，可以通过命令来控制是否把Progress消息转义成Alerting消息，当跟采用Progress消息来表示振铃的设备对接时需要该转义操作，否则不需要进行该消息的转义操作。

和友商设备互通时可能需要配置本命令。

【举例】

\# PRI接口Serial2/3/0:15上配置Progress消息转义成Alerting消息的功能。

\<Sysname\> system-view

Sysname interface serial 2/3/0:15

Sysname-Serial2/3/0:15 isdn progress-to-alerting enable

**ISDN \-- ISDN配置命令 \-- isdn protocol-mode**

------------------------------------------------------------------------

**[isdn protocol-mode**]命令用来配置ISDN接口所使用的协议模式。

**[undo isdn protocol-mode**]命令用来恢复缺省情况。

【命令】

**[isdn protocol-mode** **[network**[\| **user** }]]

**[undo isdn protocol-mode**]

【缺省情况】]

ISDN接口所使用的协议模式为用户侧模式。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[network**]：网络侧模式。

**[user**]：用户侧模式。

【使用指导】

协议模式分为两种：用户侧模式、网络侧模式。当两台ISDN设备互通时，必须一端工作在用户侧模式，另一端工作在网络侧模式。

当语音BSV板卡上的BRI接口和ISDN电话直接相连时，BRI接口需要配置为网络侧模式，在其它场景下，设备上的ISDN接口通常都需要配置为用户侧模式。

需要注意的是：

·运行数据业务的BRI接口不支持网络侧模式。

·ANSI、AT&T、ETSI、NI、NTT协议不支持网络侧模式。

·当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 配置BRI2/4/0接口的协议模式为网络侧模式。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn protocol-mode network

**ISDN \-- ISDN配置命令 \-- isdn protocol-type**

------------------------------------------------------------------------

**[isdn protocol-type**]命令用来设置ISDN接口所使用的ISDN协议。

**[undo** **isdn protocol-type**]命令用来恢复缺省情况。

【命令】

**[isdn protocol-type ***protocol*]

**[undo isdn protocol-type**]

【缺省情况】

ISDN的BRI和PRI接口都是使用DSS1协议。

【视图】

ISDN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*]：ISDN协议类型，可以取的值包括**5ess**、**ansi**、**at&t**、**dss1**、**etsi**、**ni**、**ni2**、**ntt**、**qsig**。

【使用指导】

·ANSI协议可以在BRI和CT1/PRI接口上配置。

·AT&T协议可以在CT1/PRI接口上配置。

·5ESS协议可以在CT1/PRI接口上配置。

·DSS1协议可以在BRI、CE1/PRI以及CT1/PRI接口上配置。

·ETSI协议可以在BRI、CE1/PRI以及CT1/PRI接口上配置。

·NI（National ISDN）协议可以在BRI接口上配置。

·NI2协议可以在CT1/PRI接口上配置。

·QSIG协议可以在CE1/PRI以及CT1/PRI接口上配置。

·NTT协议可以在BRI和CT1/PRI接口上配置。

·工作在网络侧模式时，不可以配置ANSI、AT&T、ETSI、NI、NTT协议。

·当ISDN接口上存在呼叫时，不能配置本命令。

【举例】

\# 设置接口BRI2/4/0使用ISDN ETSI协议。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn protocol-type etsi

\# 设置接口Serial2/3/0:23使用ISDN 5ESS协议。

\<Sysname\> system-view

Sysname interface serial 2/3/0:23

Sysname-Serial2/3/0:23 isdn protocol-type 5ess

【相关命令】

·**isdn protocol-mode**

**ISDN \-- ISDN配置命令 \-- isdn q921-permanent**

------------------------------------------------------------------------

**[isdn q921-permanent**]命令用来使能BRI接口的Q.921常建链功能。

**[undo isdn q921-permanent**]命令用来恢复缺省情况。

【命令】

**[isdn q921-permanent**]

**[undo isdn q921-permanent**]

【缺省情况】

BRI接口的Q.921常建链功能处于关闭状态。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当在BRI接口下配置了该命令，该BRI接口会自动建立链路层连接并一直维持，不论其是否承载网络层呼叫。若BRI接口配置了**isdn two-tei**命令，Q.921常建链功能会自动建立两条链路层连接并一直维持。

当BRI接口工作在网络侧模式时，不能配置本命令。

【举例】

\# 使能接口BRI2/4/0的Q.921常建链功能。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn q921-permanent

【相关命令】

·**isdn protocol-mode**

·**isdn two-tei**

**ISDN \-- ISDN配置命令 \-- isdn spid auto-trigger**

------------------------------------------------------------------------

**[isdn spid auto-trigger**]命令用来对采用NI协议的BRI接口触发一次SPID的协商请求。

【命令】

**[isdn spid auto-trigger**]

【缺省情况】

没有呼叫触发时，BRI接口不会主动发起SPID的协商请求。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对于采用NI协议的BRI接口，通常需要在协商或者初始化SPID之后才能发起呼叫。SPID信息的获取可以通过静态配置，也可以通过动态协商。当用户采用动态协商而协商失败，或者为了测试需要的时候，可以采用此命令手动重新触发一次SPID的协商请求。

需要注意的是：

·本命令只在采用NI协议的BRI接口上可以使用。

·未配置为动态协商SPID时，不能配置本命令。

·配置的接口存在呼叫时，不能配置本命令。

·配置的接口正在进行SPID协商时，不能配置本命令。

【举例】

\# 设置在接口BRI2/4/0上手动触发一次SPID的协商请求。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn spid auto-trigger

**ISDN \-- ISDN配置命令 \-- isdn spid nit**

------------------------------------------------------------------------

**[isdn spid nit**]命令用来对采用NI协议的BRI接口，将其SPID处理设置为NIT（Not Initial Terminal，非初始化终端）模式。

**[undo isdn spid nit**]命令用来取消BRI接口的NIT模式。

【命令】

**[isdn spid nit**]

**[undo isdn spid nit**]

【缺省情况】

BRI接口不采用NIT模式，使用动态协商SPID方式。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对于采用NI协议的BRI接口，通常需要在协商或者初始化SPID之后才能发起呼叫。如果当设备与采用NI协议但不支持SPID协商的程控交换机互通时，就采用此命令将其SPID处理设置为NIT模式，从而使设备和程控交换机忽略SPID协商和初始化的过程。

需要注意的是：

·本命令只在采用NI协议的BRI接口上可以使用。

·当ISDN接口上存在呼叫时，不能配置本命令。

·当ISDN接口正在进行SPID协商时，不能配置本命令。

【举例】

\# 设置接口BRI2/4/0忽略SPID协商和初始化的过程，即采用NIT模式。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn spid nit

【相关命令】

·**display isdn spid**

**ISDN \-- ISDN配置命令 \-- isdn spid resend**

------------------------------------------------------------------------

**[isdn spid resend**]命令用来对采用NI协议的BRI接口，设置其协商或者初始化的INFORMATION消息的重发次数。

**[undo isdn spid resend**]命令用来恢复缺省情况。

【命令】

**[isdn spid resend** *times*]

**[undo isdn spid resend**]

【缺省情况】

INFORMATION消息重发次数为1次。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[times*]：INFORMATION消息的重发次数，取值范围为1～255。

【使用指导】

对于采用NI协议的BRI接口，通常需要在协商或者初始化SPID之后才能发起呼叫。当设备采用INFORMATION消息发起SPID协商或者初始化请求之后，将启用TSPID定时器，若协商或初始化请求无响应，当TSPID定时器超时后设备将重发INFORMATION消息。可以采用此命令修改INFORMATION的重发次数。

需要注意的是：

·本命令只在采用NI协议的BRI接口上可以使用。

·当ISDN BRI接口正在进行SPID协商时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0的INFORMATION消息的重发次数为5次。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn spid resend 5

【相关命令】

·**isdn spid timer**

**ISDN \-- ISDN配置命令 \-- isdn spid service**

------------------------------------------------------------------------

**[isdn spid service**]命令用来配置SPID协商时设备可接受的业务类型。

**[undo isdn spid service**]命令用来配置设备可接受任意业务类型。

【命令】

**[isdn spid service**[ [ **audio** \| **data** \| **speech** ]]]

**[undo isdn spid service**]

【缺省情况】

设备可接受程控交换机发送的支持语音（speech）和数据（data）业务的SPID。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[audio**]：音频业务。

**[data**]：数据业务。

**[speech**]：语音业务。

三种业务类型可以选择其一，不选择表示所有业务都接受。

【使用指导】

动态协商SPID时，如果程控交换机提供了多个SPID给设备，则设备根据每个SPID提供的业务类型是否满足当前配置的可接受业务类型来决定选择哪一个SPID。缺省情况下，设备优先接受程控交换机发送的同时支持语音（speech）和数据（data）业务的SPID。如果仅配置了**isdn spid service data**，设备优先接受程控交换机发送的支持数据业务的SPID。

多次配置本命令，其结果是取合集，例如先后配置**isdn spid service** **audio**、**isdn spid service** **data**两条命令，其结果是优先接受同时支持音频和数据业务的SPID。

需要注意的是：

·本命令只在采用NI协议的BRI接口上可以使用。

·当ISDN BRI接口正在进行SPID协商时，不能配置本命令。

【举例】

\# 配置设备可接受程控交换机发送的支持音频业务的SPID。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn service audio

**ISDN \-- ISDN配置命令 \-- isdn spid timer**

------------------------------------------------------------------------

**[isdn spid timer**]命令用来配置采用NI协议的BRI接口的TSPID定时器的时长。

**[undo isdn spid timer**]命令用来恢复缺省情况。

【命令】

**[isdn spid timer** *seconds*]

**[undo isdn spid timer**]

【缺省情况】

TSPID定时器的时长为30秒。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：TSPID定时器的时长，取值范围为1～255，单位为秒。

【使用指导】

对于采用NI的BRI接口，通常需要在协商或者初始化SPID之后才能发起呼叫。SPID信息的获取可以通过静态配置，也可以通过动态协商。当设备采用INFORMATION消息发起协商或者初始化请求之后，将启用TSPID定时器，若协商或初始化请求无响应，当TSPID定时器超时后设备将重发INFORMATION消息。用户可以采用此命令修改TSPID定时器的时长。

需要注意的是：

·本命令只在采用NI协议的BRI接口上可以使用。

·当ISDN BRI接口正在进行SPID协商时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0的TSPID定时器的时长为50秒。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn spid timer 50

【相关命令】

·**isdn spid resend**

**ISDN \-- ISDN配置命令 \-- isdn spid1**

------------------------------------------------------------------------

**[isdn spid1**]命令用来配置采用NI协议的BRI接口B1通道的SPID值。

**[undo isdn spid1**]命令用来删除采用NI协议的BRI接口B1通道的SPID值。

【命令】

**[isdn spid1 ***spid * *ldn* ]

**[undo isdn spid1**]

【缺省情况】

BRI接口B1通道的SPID和LDN值均为空。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[spid*]：SPID（Service Profile Identification，业务轮廓标识），为1～20个数字的数字串。

*[ldn*]：LDN（Local Dialing Number，本地拨号号码），为1～30个数字的数字串。

【使用指导】

对于采用NI协议的BRI接口，通常需要在协商或者初始化SPID之后才能发起呼叫。SPID信息的获取可以通过静态配置，也可以通过动态协商。通过哪种方式获取，由程控交换机决定。

缺省情况下，设备采用动态协商方式获取SPID。

静态配置SPID时，用户可以通过**isdn spid1**命令配置B1通道的SPID（LDN）值，通过**isdn spid2**命令配置B2通道的SPID（LDN）值。配置的SPID（LDN）值要与程控交换机上的SPID（LDN）值相同。程控交换机的SPID（LDN）值是由运营商在规划网络时配置的。

需要注意的是：

·配置了LDN后，**isdn calling**命令的配置将失效。

·本命令只在采用NI协议的BRI接口上可以使用。

·当ISDN BRI接口上存在呼叫时，不能配置本命令。

·当ISDN BRI接口正在进行SPID协商时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0的B1通道的SPID为012345，LDN为54321（实际应用中，要根据程控交换机的要求来配置这两个值）。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn spid1 012345 54321

【相关命令】

·**isdn calling**

·**isdn spid2**

**ISDN \-- ISDN配置命令 \-- isdn spid2**

------------------------------------------------------------------------

**[isdn spid2**]命令用来配置采用NI协议的BRI接口B2通道的SPID值。

**[undo isdn spid2**]命令用来删除采用NI协议的BRI接口B2通道的SPID值。

【命令】

**[isdn spid2 ***spid * *ldn* ]

**[undo isdn spid2**]

【缺省情况】

BRI接口B2通道的SPID和LDN值均为空。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[spid*]：SPID（Service Profile Identification，业务轮廓标识），为1～20个数字的数字串。

*[ldn*]：LDN（Local Dialing Number，本地拨号号码），为1～30个数字的数字串。

【使用指导】

对于采用NI协议的BRI接口，通常需要在协商或者初始化SPID之后才能发起呼叫。SPID信息的获取可以通过静态配置，也可以通过动态协商。通过哪种方式获取，由程控交换机决定。

缺省情况下，设备采用动态协商方式获取SPID。

静态配置SPID时，用户可以通过**isdn spid1**命令配置B1通道的SPID（LDN）值，通过**isdn spid2**命令配置B2通道的SPID（LDN）值。配置的SPID（LDN）值要与程控交换机上的SPID（LDN）值相同。程控交换机的SPID（LDN）值是由运营商在规划网络时配置的。

需要注意的是：

·配置了LDN后，**isdn calling**命令的配置将失效。

·本命令只在采用NI协议的BRI接口上可以使用。

·当ISDN BRI接口上存在呼叫时，不能配置本命令。

·当ISDN BRI接口正在进行SPID协商时，不能配置本命令。

【举例】

\# 配置接口BRI2/4/0的B2通道的SPID为012345，LDN为54321（实际应用中，要根据程控交换机的要求来配置这两个值）。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn spid2 012345 54321

【相关命令】

·**isdn calling**

·**isdn spid1**

**ISDN \-- ISDN配置命令 \-- isdn two-tei**

------------------------------------------------------------------------

**[isdn two-tei**]命令用来配置BRI接口的每一个B通道呼叫之前向交换机申请一个新的TEI值。

**[undo isdn two-tei**]命令用来恢复缺省情况。

【命令】

**[isdn two-tei**]

**[undo isdn two-tei**]

【缺省情况】

BRI接口所有B通道的呼叫都使用同一个TEI值。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

一个TEI（Terminal Endpoint Identifier，终端设备标识符）标识一个终端（比如ISDN电话），一个用户侧设备就是一个终端。TEI由网络侧设备分配。

在设备的ISDN BRI接口与部分程控交换机（如北美的采用NI协议的程控交换机DMS100）进行互通的时候，程控交换机要求不同的B通道采用不同的TEI值呼叫，否则MP呼叫无法成功（现象为只能呼起一个B通道），这时就需要使用本命令使每一个B通道呼叫之前向程控交换机申请一个新的TEI值。

需要注意的是：

·当ISDN BRI接口上存在呼叫时，不能配置本命令。

·当ISDN BRI接口工作在点到点模式下时，不能配置本命令。

【举例】

\# 配置每一个ISDN B通道呼叫之前向交换机申请一个新的TEI值。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Router-Bri2/4/0 isdn two-tei

【相关命令】

·**isdn link-mode p2p**

**ISDN \-- ISDN配置命令 \-- permanent-active**

------------------------------------------------------------------------

**[permanent-active**]命令用来使能BRI接口的物理层常激活功能。

**[undo permanent-active**]命令用来恢复缺省情况。

【命令】

**[permanent-active**]

**[undo permanent-active**]

【缺省情况】

BRI接口的物理层常激活功能处于关闭状态。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当工作在网络侧模式下的BRI接口配置了该命令，Q.921协议不会再给物理层发送去激活请求，如果BRI接口已经处于激活状态并且物理连接没有异常，则激活状态会一直维持下去。

使用本命令时注意和**isdn q921-permanent**命令的区别。**isdn q921-permanent**的作用是使Q.921工作在常建链状态（只能在用户侧使用），如果Q.921未建链时配置该命令则Q.921会试图进行链路层建链操作；而**permanent-active**的作用是维持物理层的激活状态（只能在网络侧使用），物理层处于去激活时配置该命令并不会触发底层激活。

物理层常激活功能只能供工作在网络侧模式下的BRI接口使用，目前只有语音BSV板卡上的BRI接口可以工作在网络侧模式。当BRI接口工作在用户侧模式时，不能配置本命令。

【举例】

\# 使能工作在网络侧模式的BRI2/4/0（BSV）接口的物理层常激活功能。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn protocol-mode network

Sysname-Bri2/4/0 permanent-active

【相关命令】

·**isdn protocol-mode**

·**isdn q921-permanent**

**ISDN \-- ISDN配置命令 \-- power-source**

------------------------------------------------------------------------

**[power-source**]命令用来使能BRI接口的远程供电功能。

**[undo power-source**]命令用来恢复缺省情况。

【命令】

**[power-source**]

**[undo power-source**]

【缺省情况】

BRI接口的远程供电功能处于关闭状态。

【视图】

ISDN BRI接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当BRI接口工作在网络侧模式时可以提供远程供电功能，比如工作在网络侧模式下的BSV接口和ISDN数字电话相连时，BSV接口可以为数字电话供电。

需要注意的是：

·远程供电功能只能供工作在网络侧模式下的BRI接口使用，目前只有语音BSV板卡上的BRI接口可以工作在网络侧模式。当BRI接口工作在用户侧模式时，不能配置本命令。

·当BRI接口上存在呼叫时，不能配置本命令。

【举例】

\# 使能工作在网络侧模式的BRI2/4/0（BSV）接口的远程供电功能。

\<Sysname\> system-view

Sysname interface bri 2/4/0

Sysname-Bri2/4/0 isdn protocol-mode network

Sysname-Bri2/4/0 power-source

【相关命令】

·**isdn protocol-mode**

