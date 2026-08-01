<!-- CMD-INDEX
  answer-address                      | POTS语音实体视图/VoIP语音实体视图 | L26
  codec                               | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L132
  codec preference                    | 编解码模板视图          | L272
  description                         | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L362
  display voice call                  | 任意视图             | L408
  display voice call-info             | 任意视图             | L654
  display voice entity                | 任意视图             | L742
  dsp-image                           | 语音视图             | L1172
  entity                              | 语音拨号策略视图         | L1218
  incoming called-number              | POTS语音实体视图/VoIP语音实体视图 | L1276
  ip qos dscp                         | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L1382
  line                                | POTS语音实体视图       | L1568
  match-template                      | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L1614
  outband nte                         | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L1744
  playout-delay                       | POTS语音实体视图/VoIP语音实体视图 | L1794
  playout-delay mode                  | POTS语音实体视图/VoIP语音实体视图 | L1846
  rtp payload-type nte                | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L1898
  shutdown                            | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L1956
  vad-on                              | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L1998
  voice class codec                   | 语音视图             | L2058
  voice-class codec                   | POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图 | L2106
  voice-setup                         | 系统视图             | L2164
-->

**语音实体 \-- 语音实体命令 \-- answer-address**

------------------------------------------------------------------------

**[answer-address**]命令用来在实体下配置一个号码串，若此号码串与呼叫中的主叫号码相匹配，则将该实体作为入实体。该主叫号码是呼叫INVITE报文中的主叫号码。

**[undo answer-address**]命令用来恢复缺省情况。

【命令】

**[answer-address ***calling-number-string*]

**[undo answer-address**]

【缺省情况】

没有配置任何可将该实体作为入实体的主叫号码匹配信息。

【视图】

POTS语音实体视图/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[calling-number-string*]：指定的主叫号码串，为1～31个字符的字符串，格式为[ +  { *regular-expression*  T   \$  \| T }]，其中：

·加号"+"：号码模板如果以"+"号开头，表示整个号码是一个E.164标准号码，如+110022表示110022是符合E.164标准的号码。

![说明](语音实体命令.files/image001.png)

如果配置的号码首位带有"+"号，则在中继环境中需要注意：E&M/R2/LGS信令采用的是DTMF传输，由于"+"号本身没有对应的音频，所以无法将号码成功的传输到被叫侧。而DSS1信令采用ISDN传输，不存在上述问题。在实际应用中，用户应该避免配置传输信令无法识别的字符，否则将会导致呼叫失败。

·美元符号"\$"：只能放在结尾，表示号码结束，号码必须全部匹配\$之前的*regular-expression*部分。如果号码模板后没有\$字符，则表示可以匹配以此号码开头的号码。例如，配置answer-address 20，表示将匹配呼叫中的以20开头的主叫号码的实体作为入实体。

·符号"T"：T表示定时器，表示在用户输入的号码超过最大长度、用户拨号码终止符或是定时器超时前，设备会等待用户拨号。

·*regular-expression*：由"[0-9#\*.!+%[]()-]"中的字符组合形成的字符串。各符号的含义如表 1-1(?-1209837796#_Ref398306821)所示。

表1-1 符号含义描述表

符号

含义

0-9

一位数字表示一位号码，0到9之间的数字

\#和\*

表示一位有效号码

.

通配符，可以与任何一个有效号码匹配。如：555....可以匹配任何以555开头的并有四位附加字符的号码

!

指明符号前的字符串重复零次或一次。如：56!1234可以匹配51234和561234

这些符号不能作为独立号码，之前必须有有效号码或号码串

+

指明符号前的字符串重复一次或多次。如：9876(54)+可以匹配987654、98765454、9876545454、......等号码

%

指明符号前的字符串重复零次或多次。如：9876(54)%可以匹配9876、987654、98765454、9876545454、......等号码

-

连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如： 1-9表示从1到9（包括1和9）

符号"-"只能出现在" "中，且连接两端只能为数字



表示字符选择范围，如： 1-36表示只可匹配单个字符1、2、3、6中的某一个

符号"  "和"( )"如果嵌套使用，则必须以"( [  )]"形式出现，不允许其它形式，如"   "、" ( ) "等

( )

表示一组字符，如：(123)表示字符串123，它一般与符号"!"、"%"、"+"一起使用，如：408(12)+，可以匹配40812或408121212等字符串

【举例】

\# 配置VoIP语音实体1，收到的呼叫中主叫号码以456开头时，可以使用该实体作为入实体。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 answer-address 456

**语音实体 \-- 语音实体命令 \-- codec**

------------------------------------------------------------------------

**[codec**]命令用来配置语音编解码。

**[undo** **codec**]命令用来删除配置的语音编解码。

【命令】

**codec**[ { **g711alaw** \| **g711ulaw** \| **g723r53** \| **g723r63** \| **g726r16** \| **g726r24** \| **g726r32** \| **g726r40** \| **g729a** \| **g729br8** \| **g729r8** } [ **bytes** *payload-size* ]]

**[undo** **codec** ]

【缺省情况】

没有配置语音编解码。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[g711alaw**]：表示G.711的A律编解码方式，带宽为64kbps，通常被欧洲采用。

**[g711ulaw**]：表示G.711的m律编解码方式，带宽为64kbps，通常被北美和日本等国家采用。

**[g723r53**]：表示G.723.1 Annex A编解码方式，带宽为5.3kbps。

**[g723r63**]：表示G.723.1 Annex A编解码方式，带宽为6.3kbps。

**[g726r16**]：表示G.726 Annex A编解码方式，带宽为16kbps。本参数的支持情况与实际使用的板卡有关。

**[g726r24**]：表示G.726 Annex A编解码方式，带宽为24kbps。本参数的支持情况与实际使用的板卡有关。

**[g726r32**]：表示G.726 Annex A编解码，带宽为32kbps。本参数的支持情况与实际使用的板卡有关。

**[g726r40**]：表示G.726 Annex A编解码方式，带宽为40kbps。本参数的支持情况与实际使用的板卡有关。

**[g729a**]：表示G.729 Annex A编解码方式，对G.729编解码进行了一系列简化，带宽为8kbps。

**[g729br8**]：表示G.729 Annex B编解码方式，带宽为8kbps。

**[g729r8**]：表示G.729编解码方式，带宽为8kbps。

**[bytes** *payload-size*]：每秒发送的编码字节数，取值范围和选择的编解码有关，单位为字节：

·**g711alaw**和**g711ulaw**的取值范围为16～80（取值为8的倍数），80～240（取值为80的倍数）；

·**g723r53**的取值范围为20～120（取值为20的倍数）；

·**g723r63**的取值范围为24～144（取值为24的倍数）；

·**g726r16**的取值范围为20～220（取值为20的倍数）；

·**g726r24**的取值范围为30～210（取值为30的倍数）；

·**g726r32**的取值范围为40～200（取值为40的倍数）；

·**g726r40**的取值范围为50～200（取值为50的倍数）；

·**g729a**、**g729br8**和**729r8**的取值范围为10～180（取值为10的倍数）。

缺省情况下，**g711**为160字节，**g723r63**为24字节，**g723r53**为20字节，**g726r16**为60字节，**g726r24**为90字节，**g726r32**为120字节，**g726r40**为150字节，**g729**为30字节。

【使用指导】

![说明](语音实体命令.files/image001.png)

·只有当通讯双方拥有的语音编解码存在交集时，双方才能正常建立呼叫。

·多次执行该命令，新的配置会覆盖已有配置。

**[g711alaw**]和**g711ulaw**编解码可以提供高质量的语音传输，但要占用较高的带宽。

**[g723r53**]和**g723r63**编解码提供了静音压缩技术和舒适噪音，较高速率的输出基于多脉冲多量级技术并提供某种程度上较高质量的音质，较低速率的输出基于码激励线性预测技术并为应用提供了更大的灵活性。

**[g729r8**]和**g729a**编解码提供的话音质量与32kbps的ADPCM（Adaptive Differential Pulse Code Modulation，自适应差分脉冲编码调制）相似，具有长话的质量，同时具有低带宽、较小时间延迟和适中处理复杂度，因此应用广泛。

为了更清晰地了解各种语音编解码算法对语音带宽、话音质量等的影响，表 1-2(?795477320#_Ref404268010)介绍相关算法和带宽的关系。

表1-2 相关算法和带宽的关系

语音编解码

带宽

语音质量

G.711（A律、m律）

64Kbps（没有压缩）

语音质量最好

G.726

16、24、32、40 Kbps

语音质量较好

G.729

8Kbps

语音质量较好

G.723 r63

6.3Kbps

语音质量一般

G.723 r53

5.3Kbps

语音质量一般

【举例】

\# 配置语音编解码为g711alaw。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 codec g711alaw

**语音实体 \-- 语音实体命令 \-- codec preference**

------------------------------------------------------------------------

**[codec preference**]命令用来配置编解码优先级。

**[undo** **codec preference**]命令用来删除已配置的编解码优先级。

【命令】

**[codec preference ***priority*[ { **g711alaw** \| **g711ulaw** \| **g723r53** \| **g723r63** \| **g726r16** \| **g726r24** \| **g726r32** \| **g726r40** \| **g729a** \| **g729br8** \| **g729r8** } [ **bytes** *payload-size* ]]]

**[undo codec preference ***priority*]

【缺省情况】

编解码模板中不存在编解码设置。

【视图】

编解码模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：表示编解码的优先级，取值范围为1～4，数值越小表示优先级越高。

**[g711alaw**]：表示G.711的A律编解码方式，带宽为64kbps，通常被欧洲采用。

**[g711ulaw**]：表示G.711的m律编解码方式，带宽为64kbps，通常被北美和日本等国家采用。

**[g723r53**]：表示G.723.1 Annex A编解码方式，带宽为5.3kbps。

**[g723r63**]：表示G.723.1 Annex A编解码方式，带宽为6.3kbps。

**[g726r16**]：表示G.726 Annex A编解码方式，带宽为16kbps。本参数的支持情况与实际使用的板卡有关。

**[g726r24**]：表示G.726 Annex A编解码方式，带宽为24kbps。本参数的支持情况与实际使用的板卡有关。

**[g726r32**]：表示G.726 Annex A编解码，带宽为32kbps。本参数的支持情况与实际使用的板卡有关。

**[g726r40**]：表示G.726 Annex A编解码方式，带宽为40kbps。本参数的支持情况与实际使用的板卡有关。

**[g729a**]：表示G.729 Annex A编解码方式，对G.729编解码进行了一系列简化，带宽为8kbps。

**[g729br8**]：表示G.729 Annex B编解码方式，带宽为8kbps。

**[g729r8**]：表示G.729编解码方式，带宽为8kbps。

**[bytes** *payload-size*]：每秒发送的编码字节数，取值范围和选择的编解码有关：

·**g711alaw**和**g711ulaw**的取值范围为16～80（取值为8的倍数），80～240（取值为80的倍数）；

·**g723r53**的取值范围为20～120（取值为20的倍数）；

·**g723r63**的取值范围为24～144（取值为24的倍数）；

·**g726r16**的取值范围为20～220（取值为20的倍数）；

·**g726r24**的取值范围为30～210（取值为30的倍数）；

·**g726r32**的取值范围为40～200（取值为40的倍数）；

·**g726r40**的取值范围为50～200（取值为50的倍数）；

·**g729a**、**g729br8**和**729r8**的取值范围为10～180（取值为10的倍数）。

缺省情况下，**g711**为160字节，**g723r63**为24字节，**g723r53**为20字节，**g726r16**为60字节，**g726r24**为90字节，**g726r32**为120字节，**g726r40**为150字节，**g729**为30字节。

【使用指导】

关于各编解码的介绍请参见**codec**命令中的使用指导。

【举例】

\# 配置编解码模版1的第一优先级编解码为g711alaw。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice class codec 1

Sysname-voice-class-codec1 codec preference 1 g711alaw

**语音实体 \-- 语音实体命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置语音实体的描述信息。

**[undo description**]命令用来删除已配置的描述信息。

【命令】

**[description** *string*]

**[undo** **description**]

【缺省情况】

没有配置语音实体的描述信息。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[string*]：语音实体的描述信息，为1～80个字符的字符串，区分大小写。

【举例】

\# 配置语音实体10的描述信息为room10。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 description room10

**语音实体 \-- 语音实体命令 \-- display voice call**

------------------------------------------------------------------------

**[display voice call**]命令用来显示正在呼叫的语音控制信息。

【命令】

**[display voice call**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

一路基本的语音呼叫由两个Leg组成，一个入呼叫Leg和一个出呼叫Leg。Leg的作用是标识一路呼叫段。

【举例】

\# 如[图]1-1(?1417918335#_Ref371944607)所示的组网图，号码2222呼叫号码11111，并建立通话。在Router B上使用**display voice call**命令显示正在呼叫的语音控制信息。

图1-1 呼叫组网图

!(语音实体命令.files/image002.png)

\<RouterB\> display voice call

Voice call information：

Call1

   CallID                   : 6

   Calling number           : 2222

   Called number            : 1111

   Call info-table index    : 0

   Total call-legs          : 2

   Leg 1

      LegID                 : 10

      Leg type              : Call-Leg

      Status                : Connected

      Call reference ID     : 3

      Signal protocol       : LGS

      Voice line            : 2/1/2

   Leg 2

      LegID                 : 11

      Leg type              : Call-Leg

      Status                : Connected

      Call reference ID     : 4

      Signal protocol       : SIP

      Target SIP address    : 192.168.2.1:5060

\# 如[图]1-1(?1417918335#_Ref371944607)所示的组网图，号码1111呼叫号码2222，并建立通话，2222作为呼叫保持发起方进行拍叉操作。在Router B上使用**display voice call**命令显示正在呼叫的语音控制信息。

\<RouterB\> display voice call

Voice call information：

Call1

   CallID                   : 7

   Calling number           : 1111

   Called number            : 2222

   Call info-table index    : 0

   Total call-legs          : 2

   Leg 1

      LegID                 : 17

      Leg type              : Call-Leg

      Status                : Connected

      Call reference ID     : 7

      Signal protocol       : SIP

      Target SIP address    : 192.168.2.1:5060

   Leg 2

      LegID                 : 18

      Leg type              : Call-Leg

      Status                : Connected

      Call reference ID     : 14

      Signal protocol       : LGS

      Voice line            : 2/1/2

      Number of services    : 1

      Service name          : CH

表1-3 display voice call命令显示信息描述表

字段

描述

CallID

标识一路呼叫，取值范围为0～999

Calling number

主叫号码

Called number

被叫号码

Call info-table index

呼叫信息表索引

Total call-legs

呼叫Leg的数量，取值范围0～3

LegID

唯一的标示一路呼叫Leg，取值范围为0～2999

Leg type

Leg的类型：

·Call_Leg：呼叫相关的Leg

·Temp_Leg：临时Leg，在设备作为SIP trunk时，会出现该类型的Leg

·MOH_Leg：音乐保持业务Leg

Status

Leg的状态，Leg的类型不同，状态也不相同

呼叫相关的Leg（Call_Leg）的状态：

·Finding-route：等待路由查询响应

·Incoming_ACK：入呼叫应答状态

·Outgoing_ACK：出呼叫应答状态

·Connected：呼叫已连接状态

音乐保持业务Leg（MOH_Leg）的状态：

·Waiting-music-response：等待音乐服务器响应状态

·MOH_connected：已经和音乐服务器建立连接

Temp_Leg没有状态，该Leg的Status字段显示为-NA-

Call reference ID

Leg对应的呼叫协议控制块ID

Signal protocol

该Leg的信令类型：

·SIP

·LGS

·R2

·E&M

·IVA

Voice line

Leg使用的语音用户线

Number of services

Leg上的语音业务的数量

Service name

Leg上语音业务的名称：

·CH：呼叫保持业务

·CW：呼叫等待业务

·MCH：多方保持业务

·MOH：音乐保持业务

·CT：SIP to SIP的呼叫转接业务

·CF：SIP to SIP的呼叫前转业务

·CB：呼叫备份业务

·CFO：呼叫前转业务发起方

·CTO：呼叫转接业务发起方

·CTR：呼叫转接业务接收方

·CTT：呼叫转接业务目的方

·Conference：三方会议业务

**语音实体 \-- 语音实体命令 \-- display voice call-info**

------------------------------------------------------------------------

**[display voice call-info**]命令用来显示正在呼叫的信息。

【命令】

**[display voice call-info **[{ *tag* **\| all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[tag*]：呼叫的标签号，取值范围为0～511。

**[all**]：显示所有呼叫信息的信息。

【举例】

\# 显示所有正在呼叫的信息。

\<Sysname\> display voice call-info all

Call tag 0

   Caller number : 5000

   Called number : 1000

   Call direction : From packet switch

   Voice interface index : 0x00000000

   Voice entity currently used : 1

   Voice entities offered : 1

表1-4 display voice call-info命令显示信息描述表

字段

描述

Call tag

呼叫信息的标签号

Caller number

主叫号码

Called number

被叫号码

Call direction

该次呼叫的呼叫方向：

·From packet switch：由IP网络发起的呼叫

·From circuit switch：由PSTN网络发起的呼叫

Voice interface index

发起当前呼叫的语音接口索引

Voice entity currently used

当前呼叫使用的语音实体

Voice entities offered

可以提供进行该呼叫的所有语音实体

**语音实体 \-- 语音实体命令 \-- display voice entity**

------------------------------------------------------------------------

**[display voice entity**]命令用来显示语音实体的配置信息。

【命令】

**[display**[ **voice** **entity** { *entity-tag* **\|** **all** \| **ivr** \| **pots** \| **voip** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[entity-tag*]：显示指定语音实体的配置信息，取值范围为1～2147483647。

**[all**]：表示显示所有语音实体的配置信息。

**[ivr**]：表示显示所有IVR语音实体的配置信息。

**[pots**]：表示显示所有POTS语音实体的配置信息。

**[voip**]：表示显示所有VoIP语音实体的配置信息。

【举例】

\# 显示所有语音实体的配置信息。

\<Sysname\> display voice entity all

POTS 9999

   Current state: Up

   Description: entity9999

   Priority level: 0

   Match template: 9999

   Voice line: 2/2/1

   Dial prefix: Not configured

   Send number: All

   Max connections: 50

   Codec: g723r53; bytes: 80; vad: Disabled

   Caller permit: 1

   Caller group: permit group 1

   Substitute called: 9999

   Substitute calling: 9999

   DTMF relay: Outband-NTE

   RTP payload-type for NTE: 113

   Playout mode: adaptive

   Playout initial delay: 30 ms

   Playout minimum delay: 10 ms

   Playout maximum delay: 160 ms

   IP media DSCP: ef

   IP signaling DSCP: ef

   Register number: Enabled

   Call-forwarding no-reply number: 5555

   Call-forwarding on-busy number: 6666

   Call-forwarding unavailable number: 7777

   Call-forwarding unconditional number: 8888

   Authentication info:

     Username: 1000

     Password: \*\*\*\*\*\*

     Realm: abc.com

VoIP 8888

   Current state: Up

   Description: Not configured

   Priority level: 0

   Match template: 8888

   Target SIP address: 1.1.1.1

   Max connections: 10

   Caller permit: 1

   Caller group: permit group 1

   Substitute called: 9999

   Substitute calling: 9999

   DTMF relay: Outband-SIP

   Playout mode: adaptive

   Playout initial delay: 30 ms

   Playout minimum delay: 10 ms

   Playout maximum delay: 160 ms

   IP media DSCP: ef

   Codec transparent: Disabled

   Media flow-around: Enabled

   Voice class SIP early-offer forced: Disabled

   Voice class SIP URI scheme: Global

   Voice class SIP bind media source-interface: GigabitEthernet2/1/1

   Voice class SIP bind control source-interface: GigabitEthernet2/1/1

   Voice class SIP keepalive up-interval: 60 s

   Voice class SIP keepalive down-interval: 30 s

   Voice class SIP keepalive retry: 5

   Fax protocol: standard-t38; ls-redundancy: 0; hs-redundancy: 0

   Fax cng-switch: Disabled

   Fax level: -15

   Fax local-train threshold: 10

   Fax nsf: 0x000000

   Fax rate: Voice

   Fax train-mode: PPP

   Fax ecm: Disabled

表1-5 display voice entity命令显示信息描述表

字段

描述

VoIP *entity-number*

语音实体类型和语音实体号

目前支持的语音实体类型包括：VoIP、POTS、IVR

Current state

语音实体状态：

·Up：语音实体处于开启状态

·Down：语音实体处于关闭状态

Description

语音实体的描述信息。-NA-表示没有配置语音实体的描述信息

Priority level

语音实体的优先级

Match template

语音实体的号码模板

Target SIP address

语音实体的呼叫目的地址

Voice line

绑定到语音实体的语音用户线

Dial prefix

配置的拨号前缀

Send number

号码发送类型：

·All：发送全部被叫号码

·Truncate：按号码截断方式发送被叫号码

·number：号码发送的长度

Max connections

最大连接呼叫数

Codec: *codec* ; bytes: *bytes* ; vad:

语音编解码，

每秒发送的编码字节数，

静音抑制功能的状态：

·Enabled：静音抑制功能处于开启状态

·Disabled：静音抑制功能处于关闭状态

Caller permit

允许呼出/呼入的主叫号码模板

Caller group

绑定到语音实体的用户组

Substitute called

绑定到语音实体的号码变换规则表，对被叫号码应用号码变换

Substitute calling

绑定到语音实体的号码变换规则表，对主叫号码应用号码变换

DTMF relay

·Outband-SIP：将DTMF信号封装为SIP消息

·Outband-NTE：将DTMF信号封装为符合RFC 2833建议的RTP报文

·Inband-voice：将DTMF信号封装为RTP报文

RTP payload-type for NTE

使用NTE方式传输DTMF信号时，RTP报文的payload值

Playout mode

缓存语音包的工作模式

·adaptive：自适应模式

·fixed：静态模式

Playout initial delay

语音包的初始缓冲时间

Playout minimum delay

语音包的最小缓冲时间

Playout maximum delay

语音包的最大缓冲时间

IP media DSCP

承载媒体流的IP报文中DSCP值

Register number

语音实体会是否向SIP服务器发起注册：

·Enabled：语音实体会向SIP服务器发起注册

·Disabled：语音实体不会向SIP服务器发起注册

Codec transparent

编解码透传功能的状态：

·Enabled：编解码透传功能处于开启状态

·Disabled：编解码透传功能处于关闭状态

Media flow-around

媒体旁路功能的状态：

·Enabled：媒体旁路功能处于开启状态

·Disabled：媒体旁路功能处于关闭状态

Voice class SIP early-offer forced

DO-EO转换功能的状态：

·Enabled：DO-EO转换功能处于开启状态

·Disabled：DO-EO转换功能处于关闭状态

Voice class SIP URI scheme

SIP呼叫时使用的URL类型

·Global：全局使用SIP格式的URL类型

·SIP：指定在SIP呼叫时使用SIP格式的URL类型

·SIPS：指定在SIP呼叫时使用SIPS格式的URL类型

Voice class SIP bind media

发送的媒体流的源接口

Voice class SIP bind control

发送的SIP信令流的源接口

Voice class codec

绑定到语音实体的编解码模板

Call-forwarding no-reply number

无应答呼叫前转的目的号码

Call-forwarding on-busy number

遇忙呼叫前转的目的号码

Call-forwarding unavailable number

不可用呼叫前转的目的号码

Call-forwarding unconditional number

无条件呼叫前转的目的号码

Authentication info:

     Username: *name*

     Password: \*\*\*\*\*\*

     Realm: *realm*

注册鉴权信息，包括鉴权用户名、鉴权密码、域名

Voice class SIP keepalive up-interval

在标记语音实体为不可用前，本端发送OPTIONS报文的时间间隔

Voice class SIP keepalive down-interval

在标记语音实体为可用前，本端发送OPTIONS报文的时间间隔

Voice class SIP keepalive retry

在改变语音实体状态前，重复探测的次数

Fax protocol

传真协议

Fax cng-switch

CNG传真切换功能的状态：

·Enabled：CNG传真切换功能处于开启状态

·Disabled：CNG传真切换功能处于关闭状态

Fax level

发送载波能量值

Fax local-train threshold

本地训练阈值百分比

Fax nsf

非标准能力协商的国家码和厂商码

Fax rate

最高传真速率

Fax train-mode

传真的训练方式：

·Local：表示使用本地训练方式

·PPP：表示使用端对端训练方式

Fax ecm

ECM的状态：

·Enabled：ECM处于开启状态

·Disabled：ECM处于关闭状态

**语音实体 \-- 语音实体命令 \-- dsp-image**

------------------------------------------------------------------------

**[dsp-image**]命令用来配置DSP（Digital Signal Processor，数字信号处理器）镜像文件类型。

【命令】

**[dsp-image**[ { **ms** \| **general** }]]

【缺省情况】

缺省情况下，使用通用DSP镜像文件。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ms**]：配置DSP镜像文件为微软认证版本。该类型的DSP镜像文件可以满足微软认证要求的语音通信质量，但不支持G.723编解码。

**[general**]：配置DSP镜像文件为通用版本。

【使用指导】

·修改DSP镜像文件后，必须重启设备，配置的DSP镜像文件才能生效。

·在和微软Lync Server配合时，请使用微软认证版本的DSP镜像文件。其他情况，建议使用通用DSP镜像文件。

【举例】

\# 配置DSP镜像文件为微软认证版本。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dsp-image ms

**语音实体 \-- 语音实体命令 \-- entity**

------------------------------------------------------------------------

**[entity**]命令用来创建语音实体，并进入语音实体视图。

**[undo entity**]命令用来删除已创建的语音实体。

【命令】

**[entity**[ *entity-number* [ **ivr** \| **pots** \| **voip** ]]]

**[undo**[ **entity** { *entity-number* \| **all** \| **ivr** \| **pots** \| **voip** }]]

【缺省情况】

不存在语音实体。

【视图】

语音拨号策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[entity-number*]：语音实体号，取值范围为1～2147483647。

**[all**]：所有语音实体。

**[ivr**]：用于接入可定制交互式语音应答系统的语音实体。

**[pots**]：用于本地电话或是PSTN侧的语音实体。

**[voip**]：用于IP侧的语音实体。

【使用指导】

·创建新语音实体时需指明语音实体类型。

·设备最多支持1000个语音实体。

【举例】

\# 创建并进入POTS语音实体10视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

**语音实体 \-- 语音实体命令 \-- incoming called-number**

------------------------------------------------------------------------

**[incoming called-number**]命令用来在实体下配置一个号码串，若此号码串与呼叫中的被叫号码相匹配，则将该实体作为入实体。该被叫号码是呼叫INVITE报文中的被叫号码。

**[undo incoming called-number**]命令用来恢复缺省情况。

【命令】

**[incoming called-number** *called-number-string*]

**[undo incoming called-number**]

【缺省情况】

没有配置任何可将该实体作为入实体的被叫号码匹配信息。

【视图】

POTS语音实体视图/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[called-number-string*]：指定的被叫号码串，为1～31个字符的字符串，格式为[ +  { *regular-expression*  T   \$  \| T }]，其中：

·加号"+"：号码模板如果以"+"号开头，表示整个号码是一个E.164标准号码，如+110022表示110022是符合E.164标准的号码。

![说明](语音实体命令.files/image001.png)

如果配置的号码首位带有"+"号，则在中继环境中需要注意：E&M/R2/LGS信令采用的是DTMF传输，由于"+"号本身没有对应的音频，所以无法将号码成功的传输到被叫侧。而DSS1信令采用ISDN传输，不存在上述问题。在实际应用中，用户应该避免配置传输信令无法识别的字符，否则将会导致呼叫失败。

·美元符号"\$"：只能放在结尾，表示号码结束，号码必须全部匹配\$之前的*regular-expression*部分。如果号码模板后没有\$字符，则表示可以匹配以此号码开头的号码。例如，配置**incoming called-number **20，表示将匹配呼叫中的以20开头的被叫号码的实体作为入实体。

·符号"T"：T表示定时器，表示在用户输入的号码超过最大长度、用户拨号码终止符或是定时器超时前，设备会等待用户拨号。

·*regular-expression*：由"[0-9#\*.!+%[]()-]"中的字符组合形成的字符串。各符号的含义如表 1-6(?-981241550#_Ref398304882)所示。

表1-6 符号含义描述表

符号

含义

0-9

一位数字表示一位号码，0到9之间的数字

\#和\*

表示一位有效号码

.

通配符，可以与任何一个有效号码匹配。如：555....可以匹配任何以555开头的并有四位附加字符的号码

!

指明符号前的字符串重复零次或一次。如：56!1234可以匹配51234和561234

这些符号不能作为独立号码，之前必须有有效号码或号码串

+

指明符号前的字符串重复一次或多次。如：9876(54)+可以匹配987654、98765454、9876545454、......等号码

%

指明符号前的字符串重复零次或多次。如：9876(54)%可以匹配9876、987654、98765454、9876545454、......等号码

-

连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如： 1-9表示从1到9（包括1和9）

符号"-"只能出现在" "中，且连接两端只能为数字



表示字符选择范围，如： 1-36表示只可匹配单个字符1、2、3、6中的某一个

符号"  "和"( )"如果嵌套使用，则必须以"( [  )]"形式出现，不允许其它形式，如"   "、" ( ) "等

( )

表示一组字符，如：(123)表示字符串123，它一般与符号"!"、"%"、"+"一起使用，如：408(12)+，可以匹配40812或408121212等字符串

【举例】

\# 配置VoIP语音实体1，收到的呼叫中被叫号码以456开头时，可以使用该实体作为入实体。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 incoming called-number 456

**语音实体 \-- 语音实体命令 \-- ip qos dscp**

------------------------------------------------------------------------

**[ip qos dscp**]命令用来配置承载媒体流IP报文中DSCP值。

**[undo ip qos dscp**]命令用来恢复缺省情况。

【命令】

**[ip qos dscp **[{ *dscp-value \| dscp-value-set* } **media** ]]

**[undo ip qos **]**dscp**[{ *dscp-value \| dscp-value-set* }]**media**

【缺省情况】

全局承载媒体流IP报文中DSCP值为**ef**（101110）。语音实体下没有缺省的DSCP值。如果该语音实体下没有DSCP值，那么该语音实体的缺省情况与全局的DSCP值相同。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DSCP值，取值范围为0～63。

*[dscp-value-set*]：DSCP值，取值如下：**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**或**ef**。

**[media**]：承载媒体流的IP报文中DSCP值。

表1-7 DSCP关键字与值的对应表

关键字

DSCP值（二进制）

DSCP值（十进制）

af11

001010

10

af12

001100

12

af13

001110

14

af21

010010

18

af22

010100

20

af23

010110

22

af31

011010

26

af32

011100

28

af33

011110

30

af41

100010

34

af42

100100

36

af43

100110

38

cs1

001000

8

cs2

010000

16

cs3

011000

24

cs4

100000

32

cs5

101000

40

cs6

110000

48

cs7

111000

56

ef

101110

46

【使用指导】

载媒体流的IP报文中DSCP值可以在SIP视图或语音实体视图下配置。SIP视图下的**ip qos dscp**命令为全局命令，当语音实体下配置媒体流的IP报文中DSCP值时，则使用语音实体配置，否则使用全局命令配置的DSCP值，即语音实体配置优先于全局配置。

【举例】

\# 配置承载语音媒体流的IP报文中DSCP值为**af41**。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 ip qos dscp af41 media

【相关命令】

·**ip qos dscp**（语音命令参考/SIP）

**语音实体 \-- 语音实体命令 \-- line**

------------------------------------------------------------------------

**[line**]命令用来将指定的语音用户线绑定到语音实体。

**[undo** **line**]命令用来取消已有的绑定。

【命令】

**[line** *line-number*]

**[undo** **line**]

【缺省情况】

语音实体与语音用户线没有绑定关系。

【视图】

POTS语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[line-number*]：语音用户线号。

【举例】

\# 语音用户线line1/0绑定到指定的语音实体10。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 line 1/0

**语音实体 \-- 语音实体命令 \-- match-template**

------------------------------------------------------------------------

**[match-template**]命令用来配置语音实体的号码模板。

**[undo** **match-template**]命令用来删除已配置的号码模板。

【命令】

**[match-template ***match-string*]

**[undo match-template**]

【缺省情况】

语音实体下不存在号码模板。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-string*]：号码模板，为1～31个字符的字符串，格式为[ **+**  { *string*  **T**   **\$**  \| **T** }]。符号说明如下：

·加号"+"：号码模板如果以"+"号开头，"+"号表示整个号码是一个E.164标准号码，如+110022表示110022是符合E.164标准的号码。

![说明](语音实体命令.files/image001.png)

如果配置的号码首位带有"+"号，则在中继环境中需要注意：E&M/R2/LGS信令采用的是DTMF传输，由于"+"号本身没有对应的音频，所以无法将号码成功的传输到被叫侧。而DSS1信令采用ISDN传输，不存在上述问题。在实际应用中，用户应该避免配置传输信令无法识别的字符，否则将会导致呼叫失败。

·美元符号"\$"：只能放在结尾，表示号码结束，号码必须全部匹配\$之前的*string*部分。如果号码模板后没有\$字符，则表示可以匹配以此号码开头的号码，例如配置**match-template **20，表示可以匹配以20号码开头的号码。

·符号"T"：T表示定时器，表示在用户输入的号码超过最大长度、用户拨号码终止符或是定时器超时前，设备会等待用户拨号。

·*string*：由"0-9#＊[.!+%[]()-]"中的字符组合形成的字符串。各符号的含义如表 1-8(#_0_16135_x6401_668020231)所示。

表1-8 符号含义描述表

符号

含义

0-9

一位数字表示一位号码，0到9之间的数字

\#和＊

表示一位有效号码

.

通配符，可以与任何一位有效号码匹配。如：555. . . . 可以匹配任何以555开头的并有四位附加字符的号码

!

指明符号前的字符串重复零次或一次。如：56!1234可以匹配51234和561234

符号"!%+"前的字符串（一位号码或号码串），作为非精确匹配的号码，处理类似"."通配符；这些符号不能作为独立号码，之前必须有有效号码或号码串

+

指明符号前的字符串重复一次或多次。如：9876(54)+可以匹配987654、98765454、9876545454、......等号码

%

指明符号前的字符串重复零次或多次。如：9876(54)%可以匹配9876、987654、98765454、9876545454、......等号码

-

连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如： 1-9表示从1到9（包括1和9）

符号"-"只能出现在" "中，且连接两端只能为数字，如0-9



表示字符选择范围，如： 1-36表示只可匹配单个字符1、2、3、6中的某一个

符号"  "和"( )"如果嵌套使用，则必须以"( [  )]"形式出现，不允许其它形式，如"   "、" ( ) "等

( )

表示一组字符，如：(123)表示字符串123，它一般与符号"!"、"%"、"+"一起使用，如：408(12)+，可以匹配40812或408121212等字符串，但不能匹配408，即12可连续出现且至少出现一次

![说明](语音实体命令.files/image001.png)

每一个符号占用一个字符，符号 和( )占用两个字符。

【使用指导】

需要注意的是：

·配置本地POTS语音实体时，使用**match-template**指定的是与本地语音用户线绑定的号码模板。配置中继POTS语音实体时，使用**match-template**指定的是被叫方的号码模板。

·配置VoIP语音实体时，使用**match-template**指定的是被叫方的号码模板。

【举例】

\# 配置POTS语音实体1000的号码模板为1000。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1000 pots

Sysname-voice-dial-entity1000 match-template 1000

\# 配置VoIP语音实体2000的号码模板为2000。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 2000 voip

Sysname-voice-dial-entity2000 match-template 2000

**语音实体 \-- 语音实体命令 \-- outband nte**

------------------------------------------------------------------------

**[outband **]**nte**命令用来配置使用NTE（Named Telephone Event，命名的电话事件）带外方式传输DTMF信号。

**[undo** **outband**]命令用来恢复缺省情况。

【命令】

**[outband**] **nte**

**[undo** **outband**]

【缺省情况】

使用带内方式传输DTMF信号。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

建议配置该方式时，在主被叫设备上同时开启**outband** **nte**命令，并设置相同的**rtp** **payload-type**值，否则可能导致DTMF信号传输失败。

【举例】

\# 配置使用NTE带外方式传输DTMF信号。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 outband nte

【相关命令】

·**rtp** **payload-type** **nte**

**语音实体 \-- 语音实体命令 \-- playout-delay**

------------------------------------------------------------------------

**[playout-delay**]命令用来配置缓存语音包的工作参数。

**[undo playout-delay**]命令用来恢复缺省情况。

【命令】

**[playout-delay **[{ **initial** *milliseconds* \| **maximum** *milliseconds* \| **minimum** *milliseconds* }]]

**[undo playout-delay **[{ **initial** \| **maximum** \| **minimum** }]]

【缺省情况】

语音包的初始缓冲时间为30毫秒，最大缓冲时间为160毫秒，最小缓冲时间为10毫秒。

【视图】

POTS语音实体视图/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[initial ***milliseconds*]：在自适应模式下，**initial**是建立通话后语音包初始缓冲时间。在静态模式下，**initial**是语音包固定缓冲时间。取值范围为5～300，单位为毫秒。

**[maximum ***milliseconds*]：设置语音包的最大缓冲时间，取值范围为60～300，单位为毫秒。该参数只在自适应模式下生效。

**[minimum ***milliseconds*]：设置语音包的最小缓冲时间，取值范围为0～40，单位为毫秒。该参数只在自适应模式下生效。

【举例】

\# 配置缓存语音包的工作模式为自适应模式，语音包的最小缓冲时间为30毫秒。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 playout-delay mode adaptive

Sysname-voice-dial-entity10 playout-delay minimum 30

**语音实体 \-- 语音实体命令 \-- playout-delay mode**

------------------------------------------------------------------------

**[playout-delay mode**]命令用来配置缓存语音包的工作模式。

**[undo playout-delay mode**]命令用来恢复缺省情况。

【命令】

**[playout-delay mode **[{ **adaptive \| fixed** }]]

**[undo playout-delay mode**]

【缺省情况】

缓存语音包的工作模式为静态模式。

【视图】

POTS语音实体视图/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[adaptive**]：配置缓存语音包的工作模式为自适应模式。在自适应模式下，语音包缓冲区大小可以根据网络抖动情况自动调整。

**[fixed**]：配置缓存语音包的工作模式为静态模式。在静态模式下，语音包缓冲区大小是固定的。

【使用指导】

在VoIP语音通信质量不理想的情况下，可以使用该命令调整缓存语音包的工作模式。在理想的语音网络环境中，语音包从发送方到接收方所经历的传播时间是恒定的，即网络抖动为零。而在实际的网络环境中，语音包从发送方到接收方所经历的传播时间是不断变化的，即存在网络时延抖动。为了消除网络抖动对话音质量造成的影响，语音数据的接收方需要做防抖动处理。接收方通过将接收到的语音包缓存一段时间后再播放，使得以不同时延到达接收方的语音包能够按照发送方的固定时间间隔均匀地被传递给编解码器，从而有效消除网络抖动对通话质量带来的影响。

【举例】

\# 配置缓存语音包的工作模式为自适应模式。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 playout-delay mode adaptive

**语音实体 \-- 语音实体命令 \-- rtp payload-type nte**

------------------------------------------------------------------------

**[rtp** **payload-type** **nte**]命令用来配置使用NTE方式传输DTMF信号时，RTP报文的payload值。

**[undo** **rtp** **payload-type** **nte**]命令用来恢复缺省情况。

【命令】

**[rtp** **payload-type** **nte** *value*]

**[undo** **rtp** **payload-type** **nte**]

【缺省情况】

使用NTE方式传输DTMF信号时，RTP报文的payload值为101。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：RTP报文的payload值，取值范围为96～127。其中98用于标识非标准T38传真报文，为保留值。

【使用指导】

·建议配置该方式时，在主被叫设备上同时开启**outband** **nte**命令**，**并设置相同的**rtp** **payload-type**值，否则可能导致DTMF信号传输失败。

·与其它厂商的设备互通时，不能配置其它厂商设备禁用payload值，否则可能导致NTE协商失败。

【举例】

\# 配置使用NTE带外方式传输DTMF信号，其中payload值为102。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 outband nte

Sysname-voice-dial-entity10 rtp payload-type nte 102

【相关命令】

·**outband nte**

**语音实体 \-- 语音实体命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭语音实体。

**[undo shutdown**]命令用来开启语音实体。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

语音实体处于开启状态。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭语音实体10。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 shutdown

**语音实体 \-- 语音实体命令 \-- vad-on**

------------------------------------------------------------------------

**[vad-on**]命令用来使能静音抑制功能。

**[undo** **vad-on**]命令用来关闭静音抑制功能。

【命令】

**[vad-on**  [ **g711** \| **g723r53** \| **g723r63** \| **g729a** \| **g729r8** ] \*]

**[undo**  **vad-on** [ **g711** \| **g723r53** \| **g723r63** \| **g729a** \| **g729r8** ] \*]

【缺省情况】

静音抑制功能处于关闭状态。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[g711**]：g711编解码方式的静音抑制功能。

**[g723r53**]：g723r53编解码方式的静音抑制功能。

**[g723r63**]：g723r63编解码方式的静音抑制功能。

**[g729a**]：g729a编解码方式的静音抑制功能。

**[g729r8**]：g729r8编解码方式的静音抑制功能。

【使用指导】

·如果不选择编解码方式，表示打开或关闭所有编解码方式的静音抑制功能。

·G.726编解码方式不支持静音抑制。G.729br8编解码始终支持静音抑制。

【举例】

\# 开启g723r53编解码方式的静音抑制功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 vad-on g723r53

**语音实体 \-- 语音实体命令 \-- voice class codec**

------------------------------------------------------------------------

**[voice class codec**]命令用来创建编解码模板。

**[undo voice class code**]命令用来删除已配置的编解码模板。

【命令】

**[voice class codec ***tag*]

**[undo voice class codec ***tag*]

【缺省情况】

不存在编解码模板。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag*]：编解码模板号，取值范围为1～2147483647。

【使用指导】

设备最多支持配置16个编解码模板。

【举例】

\# 配置编解码模板1。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice class codec 1

sysname-voice-class-codec1

**语音实体 \-- 语音实体命令 \-- voice-class codec**

------------------------------------------------------------------------

**[voice-class codec**]命令用来配置将指定的编解码模板绑定到语音实体。

**[undo voice-class codec**]用来取消已有的绑定。

【命令】

**[voice-class codec** *tag*]

**[undo voice-class codec**]

【缺省情况】

编解码模板和语音实体没有绑定关系。

【视图】

POTS语音实体视图/VoIP语音实体视图/IVR语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag*]：绑定的编解码模板号，取值范围为1～2147483647。

【使用指导】

·用户可以将一个不存在的编解码模板绑定到语音实体，但只有在使用**codec preference**命令完成编解码优先级的设置后，该编解码模板才能生效。

·在语音实体下只能绑定一个编解码模板，如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 将编解码模板1绑定到语音实体。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 voice-class codec 1

【相关命令】

·**codec preference**

·**voice class codec**

**语音实体 \-- 语音实体命令 \-- voice-setup**

------------------------------------------------------------------------

**[voice-setup**]命令用来进入语音视图，并启用语音服务。

**[undo** **voice-setup**]命令用来关闭语音服务，并退出语音视图，删除所有语音配置。

【命令】

**[voice-setup**]

**[undo** **voice-setup**]

【缺省情况】

语音服务处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入语音视图，并启用语音服务。

\<Sysname\> system-view

Sysname voice-setup

