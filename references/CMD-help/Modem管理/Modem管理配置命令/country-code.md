<!-- CMD-INDEX
  country-code                        | AM接口视图           | L11
  modem answer-timer                  | 用户线视图            | L59
  modem auto-answer                   | 用户线视图            | L113
  modem callback                      | 系统视图             | L163
  modem caller-number resolve         | 用户线视图            | L203
  modem enable                        | 用户线视图            | L257
  sendat                              | 接口视图             | L309
-->

**Modem管理 \-- Modem管理配置命令 \-- country-code**

------------------------------------------------------------------------

**[country-code**]命令用来配置AM接口的Modem编码格式。

**[undo country-code**]命令用来恢复缺省情况。

【命令】

**[country-code** *area-name*]

**[undo country-code**]

【缺省情况】

地区编码格式为united-states。

【视图】

AM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[area-name*]：地区名称，包括：australia、austria、belgium、brazil、bulgaria、canada、china、czechoslovakia、denmark、finland、france、germany、greece、hongkong、hungary、india、ireland、israel、italy、japan、korea、luxembourg、malaysia、mexico、netherlands、new-zealand、norway、philippines、poland、portugal、russia、singapore、southafrica、spain、sweden、switzerland、taiwan、united-kingdom、united-states。

【使用指导】

在不同的地区，Modem的编码格式有所不同，为了适应不同地区的编码格式，可以配置此命令。

需要注意的是，当Modem处于连接状态时，配置本命令会使Modem连接断开。

【举例】

\# 配置AM接口的编码格式为china。

\<Sysname\> system-view

Sysname interface analogmodem 2/4/0

Sysname-Analogmodem2/4/0 country-code china

**Modem管理 \-- Modem管理配置命令 \-- modem answer-timer**

------------------------------------------------------------------------

**[modem answer-timer**]命令用来配置Modem等待链路建立的有效时间间隔。

**[undo modem answer-timer**]命令用来恢复缺省情况。

【命令】

**[modem answer-timer** *time*]

**[undo modem answer-timer**]

【缺省情况】

Modem等待链路建立的有效时间间隔为60秒。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：Modem等待链路建立的有效时间间隔，取值范围为1～65535，单位为秒。

【使用指导】

当Modem等待链路建立的时间间隔超过配置的有效时间间隔后，Modem将拆除本次呼叫。

Modem作为主叫侧设备或被叫侧设备时，Modem等待链路建立的时间间隔的含义不同：

·Modem作为主叫侧设备时，该间隔是指从拨号到通话的时间间隔。

·Modem作为被叫侧设备时，该间隔是指从摘机到通话的时间间隔。

本命令仅在异步串口、工作在异步方式的同/异步串口、AM接口对应的TTY用户线视图和AUX接口对应的AUX用户线视图下可以配置，在Console、VTY用户线视图下无法配置。

【举例】

\# 将Modem等待链路建立的有效时间配置为50秒。

\<Sysname\> system-view

Sysname line aux 0

Sysname-line-aux0 modem answer-timer 50

**Modem管理 \-- Modem管理配置命令 \-- modem auto-answer**

------------------------------------------------------------------------

**[modem auto-answer**]命令用来配置Modem的应答方式为自动应答方式。

**[undo modem auto-answer**]命令用来配置Modem的应答方式为非自动应答方式，即路由器通过发AT指令给Modem来应答。

【命令】

**[modem auto-answer**]

**[undo modem auto-answer**]

【缺省情况】

Modem为非自动应答方式。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令仅在异步串口、工作在异步方式的同/异步串口、AM接口对应的TTY用户线视图和AUX接口对应的AUX用户线视图下可以配置，在通道化生成的同/异步串口对应的TTY用户线视图和Console、VTY用户线视图下无法配置。

建议根据路由器外接Modem的当前应答状态配置本命令，使得用户接口的状态与Modem的状态一致。当Modem状态为自动应答（Modem的AA灯亮）时，配置**modem auto-answer**（以避免Modem自动应答后，路由器又发出应答指令）；如果外接Modem为非自动应答方式，则可配置**undo modem auto-answer**。

需要注意的是，当本命令的配置与Modem当前的应答状态不一致时，对于某些Modem可能会造成应答不正常，请谨慎配置此命令。

【举例】

\# 在TTY1用户线视图下，配置Modem为自动应答方式。

\<Sysname\> system-view

Sysname line tty 1

Sysname-line-tty1 modem auto-answer

【相关命令】

·**modem caller-number resolve**

**Modem管理 \-- Modem管理配置命令 \-- modem callback**

------------------------------------------------------------------------

**[modem callback**]命令用来开启Modem的回呼功能。

**[undo modem callback**]命令用来恢复缺省情况。

【命令】

**[modem callback**]

**[undo modem callback**]

【缺省情况】

Modem的回呼功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

Modem回呼功能是指Modem作为被叫侧设备和主叫方用户建立连接之后，对于需要回呼的主叫方用户，Modem断开当前连接并主动呼出。

【举例】

\# 开启Modem的回呼功能。

\<Sysname\> system-view

Sysname modem callback

**Modem管理 \-- Modem管理配置命令 \-- modem caller-number resolve**

------------------------------------------------------------------------

**[modem caller-number resolve**]命令用来开启Modem模块获取终端主叫号码功能，即在Modem模块接受终端呼叫时，获取其主叫号码。

**[undo modem caller-number resolve**]命令用来恢复缺省情况。

【命令】

**[modem caller-number resolve** [ **ata-waiting-time** *time* ]]

**[undo modem caller-number resolve**]

【缺省情况】

Modem模块接受终端呼叫时，不获取其主叫号码。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ata-waiting-time **]*time*：Modem模块等待接收主叫方号码的时间，取值范围为10～10000，单位为毫秒，缺省值为1000毫秒。超过该时间之后，Modem模块将不再接收[主叫方号码。该参数取值与主叫方和主叫方接入设备之间的连接速率有关，若主叫方与主叫方接入设备之间的连接速率较低，则该参数配置的大一些，会增加]Modem模块获取终端主叫号码的成功几率。

【使用指导】

本命令仅在AM接口对应的TTY用户线视图下可以配置，在其它用户线视图下无法配置。

通过AM接口接入的POS（Point of Sale，销售点）终端，若前置机需要获取POS终端的主叫号码，则POS接入设备在向前置机转发终端的数据前，首先等待获取POS终端的主叫号码，然后将获取到的终端的主叫号码发送给前置机，并等待前置机响应之后，再转发该终端的数据。本功能用于配合POS接入终端实现主叫号码发送功能，关于POS接入终端主叫号码功能的相关介绍请参考"终端接入配置指导"中的"POS终端接入"。

需要注意的是，当Modem处于连接状态时，配置本命令会使Modem连接断开。

【举例】

\# 在TTY用户线视图下，开启Modem模块获取终端主叫号码功能，并设置获取终端主叫号码的最长等待时间为10秒。

\<Sysname\> system-view

Sysname line tty 81

Sysname-line-tty81 modem caller-number resolve ata-waiting-time 10000

【相关命令】

·**modem auto-answer**

**Modem管理 \-- Modem管理配置命令 \-- modem enable**

------------------------------------------------------------------------

**[modem enable**]命令用来开启Modem的呼入/呼出权限。

**[undo modem enable**]命令用来恢复缺省情况。

【命令】

**[modem enable**[ { **both** \| **call-in** \| **call-out** }]]

**[undo modem enable**]

【缺省情况】

禁止Modem呼入和呼出。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[both**]：同时允许Modem呼入和呼出。

**[call-in**]：仅允许Modem呼入。

**[call-out**]：仅允许Modem呼出。

【使用指导】

本命令仅在异步串口、工作在异步方式的同/异步串口、AM接口对应的TTY用户线视图和AUX接口对应的AUX用户线视图下可以配置，在Console、VTY用户线视图下无法配置。

需要注意的是，当Modem处于连接状态时，配置本命令会使Modem连接断开。

【举例】

\# 在TTY1用户线上，配置仅允许Modem呼入。

\<Sysname\> system-view

Sysname line tty 1

Sysname-line-tty1 modem enable call-in

**Modem管理 \-- Modem管理配置命令 \-- sendat**

------------------------------------------------------------------------

**[sendat**]命令用来手工向Modem发送AT指令。

【命令】

**[sendat** *at-string*]

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[at-string*]：AT指令字符串，为1～300个字符的字符串，对于Modem而言，AT指令指的是"+++"和"A/"以及任意以AT开头的字符串。AT指令的详细解释请参见[表]1-1(?-361739400#_Ref329712072)。

【使用指导】

**[sendat**]命令不检查AT指令的合法性，直接将用户输入的字符串作为AT指令送至Modem（遇到小写字母自动转化为大写字母）。若打开该接口的Modem调试信息开关，则可以看到Modem返回的结果码，若Modem通过E*n*指令设置了命令回显，还可以看到回显的AT指令。

需要注意的是：

·本命令可以在异步串口、工作在异步方式的同/异步串口、AUX接口、AM接口下执行。

·Modem处于AT指令模式下才能接受AT指令，若处于数据传输状态，使用该命令发送的AT指令无效。

·通过**sendat**命令一次只能发送一条AT指令。

·通过AT指令配置Modem后，Modem的工作状态会被改变，有可能导致Modem的状态混乱从而影响到拨号等基本功能。请在专业人员的指导下慎重使用本功能。

![说明](Modem管理命令.files/image001.png)

·**AT**是命令行的字首，告诉Modem要输入命令。它执行除**A/**（重复）和**+++**（换码）之外的所有命令。单独输入**AT**，如果Modem准备接收命令，则Modem返回OK或0信息。

· 表1-1(?-361739400#_Ref329712072)提供了常用AT指令的说明，表格中所有的命令均以AT字符开头，用户可以参考。

表1-1 常用AT指令描述表

指令

说明

**[A**]

应答命令。**A**命令使Modem无需等待响铃即可应答呼叫。此命令在手动应答呼叫时有用。同一命令行中**A**之后的所有命令将被忽略

**[B***n*]

通信标准选项，在ITU与Bell标准之间作出选择

参数*n*：

·*n* = 0，ITU V.22使用1200bps的传输速率

·*n* = 1，Bell 212使用1200bps的传输速率（缺省值）

·*n* = 2或3，撤消ITU V.23反向通道

·*n* = 15，ITU V.21使用300bps的传输速率

·*n* = 16，103J使用300bps的传输速率（Compaq Presario 192-VS型和Compaq Presario 288-VS型调制解调器的缺省值）

**[E***n*]

命令回应。**E***n*命令确定当Modem在命令方式时，用户在键盘上输入的字符是否回显到屏幕上（本地回显）

参数*n*：

·*n* = 0，关闭本地回显功能

·*n* = 1，启用本地回显功能（缺省值）

**[D***n*]

拨号命令。**D**命令使Modem拨命令行中D后面的号码。在脉冲拨号方式下，非数字字符不起作用

**[H***n*]

挂断控制。**H***n*命令配置Modem挂断是以断开呼叫还是以摘机占用电话线方式

参数*n*：

·*n* = 0，Modem挂断（缺省值）

·*n* = 1，Modem摘机

**[I***n*]

要求Modem的识别号（ID）。**I***n*命令询问Modem的产品识别号、ROM校验和或ROM 校验和的状态

参数*n*：

·*n* = 0或3，返回Modem默认的速率和控制器的硬件版本

·*n* = 1，计算ROM校验和并显示校验和

·*n* = 2，检查ROM、计算并验证校验和及显示OK或ERROR（错误）信息

·*n* = 4，返回数据泵的硬件版本

·*n* = 5，返回Modem板的ID、软件版本、硬件版本和国家代码

·*n* = 9，返回国家代码

**[L***n*]

配置扬声器音量。**L***n*命令在传真和数据通信时配置扬声器的音量为低、中或高

参数*n*：

·*n* = 0或1，低音量

·*n* = 2，中音量（缺省配置）

·*n* = 3，高音量

**[M***n*]

扬声器音量控制选项。**M***n*命令控制传真和数据通信时扬声器是打开还是关闭

参数*n*：

·*n* = 0，扬声器一直关闭

·*n* = 1，Modem在检测到载波信号之前，扬声器始终打开（缺省值）

·*n* = 2，在Modem摘机时，扬声器始终打开

·*n* = 3，在拨号后扬声器始终打开，直到Modem检测到载波信号为止，拨号时除外

**[N***n*]

调制握手。**N***n*命令控制本地Modem在与速率不同的远程Modem连接时是否执行协商的握手

参数*n*：

·*n* = 0，在始发呼叫或应答呼叫时，仅以S37寄存器和**ATB**命令指定的通信标准下进行数字交换

·*n* = 1，在始发呼叫或应答呼叫时，仅以S37寄存器和**ATB**命令指定的速率开始握手，在握手期间，速率可能会回落（缺省值）

**[O***n*]

在线数据方式。**O***n*命令强迫Modem进入在线数据方式

参数*n*：

·*n* = 0，进入在线数据方式

·*n* = 1，在返回在线数据方式前初始化均衡，重新排定序列

·*n* = 3，在返回在线数据方式前，进行速率的重新协商

注意：在使用 **+++**换码命令换至在线命令方式后执行该命令将返回在线数据方式

**[Q***n*]

抑制结果码。**Q***n*命令启用Modem发送结果码

参数*n*：

·*n* = 0，启用结果码（缺省值）

·*n* = 1，禁用返回结果码

**[S***r*=*n*]

写入S寄存器。**S***r*=*n*将*r*寄存器的值配置为*n*。用此命令可修改某些寄存器中的内容

参数*r*表示寄存器号，取值范围：0～27, 29, 31～33, 35, 37, 89

参数*n*表示赋值，取值范围：0～255

**[T**]

音频拨号。**T**命令将拨号方式设为音频拨号。缺省情况下，Modem配置为音频拨号。此命令也可用作拨号修正符

**[P**]

脉冲拨号。**P**命令配置脉冲拨号方式。所有的呼叫将停留在脉冲方式，直到使用**T**命令选择音频拨号为止。此命令也可用作拨号修正符

**[V***n*]

结果码的形式。**V***n*命令确定Modem返回的结果码的类型

参数*n*：

·*n* = 0，以数字形式发送结果码

·*n* = 1，以文本的形式发送结果码（缺省值）

【举例】

\# 在异步串口下发送拨号命令，呼叫号码169。

\<Sysname\> system-view

Sysname interface async 2/4/0

Sysname-Async2/4/0 sendat ATD169

\# 在工作在异步方式的同/异步串口下发送拨号命令，呼叫号码169。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 physical-mode async

Sysname-Serial2/1/0 sendat ATD169
