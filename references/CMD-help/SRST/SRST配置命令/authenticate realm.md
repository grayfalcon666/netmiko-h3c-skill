
**SRST \-- SRST配置命令 \-- authenticate realm**

------------------------------------------------------------------------

**[authenticate realm**]命令用来配置语音服务器发送401应答中携带的域名信息。

**[undo**]**authenticate realm**命令用来删除已有配置。

【命令】

**[authenticate realm **]*string*

**[undo **]**authenticate realm**

【缺省情况】

语音服务器发送401应答中不携带域名信息。

【视图】

全局注册视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[string*]：语音服务器发送401应答中携带的域名信息，用于语音服务器和SIP UA之间的握手验证，为1～50个字符的字符串，区分大小写。

【使用指导】

·设备作为语音服务器时，可以通过发送域名信息使SIP UA来选择鉴权信息。

·当设备作为语音服务器工作在本地存活模式时，该命令不生效。

【举例】

\# 配置语音服务器发送401应答中携带的域名信息。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register global

Sysname-voice-register-global authenticate realm server1

【相关命令】

·**authenticate register**

·**mode**

**SRST \-- SRST配置命令 \-- authenticate register**

------------------------------------------------------------------------

**[authenticate register**]命令用来开启全局注册鉴权。

**[undo** **authenticate register**]命令用来关闭全局注册鉴权。

【命令】

**[authenticate register**]

**[undo authenticate register**]

【缺省情况】

全局注册鉴权处于关闭状态。

【视图】

全局注册视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·开启该命令后，设备作为语音服务器在接受SIP UA注册时，如果需要对SIP UA进行鉴权。鉴权信息可以通过注册池视图下的**username**命令配置，域名信息可以通过**authenticate realm**命令配置。

·在接受SIP UA注册时，工作在本地存活模式的语音服务器不会对用户信息进行鉴权，因此在该模式的语音服务器上开启全局的注册鉴权不会生效。

【举例】

\# 开启全局注册鉴权。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register global

Sysname-voice-register-global authenticate register

【相关命令】

·**mode**

**SRST \-- SRST配置命令 \-- caller-group**

------------------------------------------------------------------------

**[caller-group**]命令用来将指定的用户组绑定到注册池。

**[undo** **caller-group**]命令用来取消已有的绑定关系。

【命令】

**[caller-group**[ { **deny** \| **permit** } *group-id*]]

**[undo**[ **caller-group** { { **deny** \| **permit** } *group-id* \| **all** }]]

【缺省情况】

用户组和注册池没有绑定关系。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[deny**]：拒绝用户组中的主叫号码呼出/呼入。

**[permit**]：允许用户组中的主叫号码呼出/呼入。

*[group-id*]：绑定用户组ID，取值范围为1～2147483647。

**[all**]：绑定的所有用户组。

【使用指导】

·可以将一个不存在的用户组绑定到注册池，但只有完成用户组的设置后，该用户组才能生效。

·在注册池下只能绑定一个用户组，如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 将用户组绑定到注册池100，允许用户组1中的主叫号码呼出。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 caller-group permit 1

【相关命令】

·**subscriber-group**（语音命令参考/拨号策略）

**SRST \-- SRST配置命令 \-- codec**

------------------------------------------------------------------------

**[codec**]命令用来配置语音编解码。

**[undo** **codec**]命令用来删除配置的语音编解码。

【命令】

**codec**[ { **g711alaw** \| **g711ulaw** \| **g723r53** \| **g723r63** \| **g726r16** \| **g726r24** \| **g726r32** \| **g726r40** \| **g729a** \| **g729br8** \| **g729r8** } [ **bytes** *payload-size* ]]

**[undo** **codec** ]

【缺省情况】

没有配置语音编解码。

【视图】

注册池视图

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

**[g726r32**]：表示G.726 Annex A编解码方式，带宽为32kbps。本参数的支持情况与实际使用的板卡有关。

**[g726r40**]：表示G.726 Annex A编解码方式，带宽为40kbps。本参数的支持情况与实际使用的板卡有关。

**[g729a**]：表示G.729 Annex A编解码方式，对G.729编解码进行了一系列简化，带宽为8kbps。

**[g729br8**]：表示G.729 Annex B编解码方式，带宽为8kbps。

**[g729r8**]：表示G.729编解码方式，带宽为8kbps。

**[bytes** *payload-size*]：每秒发送的编码字节数，取值范围和选择的编解码方式有关，单位为字节：

·**g711alaw**和**g711ulaw**的取值范围为80～240（取值为80的倍数）；

·**g723r53**的取值范围为20～120（取值为20的倍数）；

·**g723r63**的取值范围为24～144（取值为24的倍数）；

·**g726r16**的取值范围为20～220（取值为20的倍数）；

·**g726r24**的取值范围为30～210（取值为30的倍数）；

·**g726r32**的取值范围为40～200（取值为40的倍数）；

·**g726r40**的取值范围为50～200（取值为50的倍数）；

·**g729a**、**g729br8**和**729r8**的取值范围为10～180（取值为10的倍数）。

缺省情况下，**g711**为160字节，**g723r63**为24字节，**g723r53**为20字节，**g726r16**为60字节，**g726r24**为90字节，**g726r32**为120字节，**g726r40**为150字节，**g729**为30字节。

【使用指导】

**[g711alaw**]和**g711ulaw**编解码可以提供高质量的语音传输，但要占用较高的带宽。

**[g723r53**]和**g723r63**编解码提供了静音压缩技术和舒适噪音，较高速率的输出基于多脉冲多量级技术并提供某种程度上较高质量的音质，较低速率的输出基于码激励线性预测技术并为应用提供了更大的灵活性。

**[g729r8**]和**g729a**编解码提供的话音质量与32kbps的ADPCM（Adaptive Differential Pulse Code Modulation，自适应差分脉冲编码调制）相似，具有长话的质量，同时具有低带宽、较小时间延迟和适中处理复杂度，因此应用广泛。

为了更清晰地了解各种语音编解码算法对语音带宽、话音质量等的影响， 表1-1(?795477320#_Ref148446106)介绍相关算法和带宽的关系。

表1-1 编解码方式和带宽的关系

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

需要注意的是：

·当通讯双方拥有的语音编解码存在交集时，双方才能正常建立呼叫。

·多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置语音编解码为g711alaw。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 codec g711alaw

**SRST \-- SRST配置命令 \-- display voice register entity**

------------------------------------------------------------------------

**[display** **voice register entity**]命令用来显示注册池产生的动态VoIP语音实体信息。

【命令】

**[display**[ **voice** **register entity** { **all** \| **pool** *tag* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pool*** tag*]：注册池索引，取值范围为0～200。

**[all**]：表示所有注册池产生的动态VoIP语音实体。

【举例】

\# 显示注册池2产生的动态VoIP语音实体信息。

\<Sysname\> display voice register entity pool 2

Entities created dynamically on register pool 2:

entity 40003 voip

 match-template 2000\$

 address sip ip 192.168.4.101 port 10003

 session transport udp

 priority 1

entity 40004 voip

 match-template 2000\$

 address sip ip 10.1.1.2 port 5060 : VoIP entity available

 session transport global

表1-2 display voice register entity显示信息描述表

字段

描述

entity 40003 voip

动态创建的VoIP语音实体。在独立模式或本地存活模式语音服务器上生成的动态VoIP语音实体从40001开始编号，如果存在从40001开始的手工配置的POTS或VoIP语音实体，独立模式和本地存活模式语音服务器会跳过该编号后，继续编号

match-template

匹配语音实体号码模板

address sip

SIP呼叫路由

ip

呼叫目的IP地址

port

目的端口号

session transport

发起SIP呼叫时使用的传输协议类型，取值包括：

·tcp：发起呼叫时，使用TCP传输协议

·tls：发起呼叫时，使用TLS传输协议

·udp：发起呼叫时，使用UDP传输协议

priority

指向SIP UA的动态VoIP语音实体的优先级

VoIP entity

独立模式语音服务器可用状态，取值包括：

·available

·unavailable

**SRST \-- SRST配置命令 \-- display voice register pool all brief**

------------------------------------------------------------------------

**[display** **voice** **register pool all brief**]命令用来显示注册池中SIP UA的注册状态信息。

【命令】

**[display voice sip register pool all brief**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示注册池信息中SIP UA的注册状态信息。

\<Sysname\> display voice register pool all brief

Pool ID              IP Address       Ln DN  Number        State

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1    192.168.4.100   192.168.4.100    1  1   1000\$         Registered

                                      2      2000          Unregistered

2    192.168.4.101   192.168.4.101    1      2000\$         Registered

表1-3 display voice register pool all brief命令显示信息描述表

字段

描述

Pool

注册池索引

ID

注册池下使用**id**命令配置允许注册的SIP UA的条件

IP Address

成功注册的SIP UA的IP地址

Ln

[使用**number ***tag*****[{ *number \|* **dn** *dn-tag* }]]命令配置的*tag*

DN

[使用**number ***tag*****[{ *number \|* **dn** *dn-tag* }]]命令配置的*dn-tag*

Number

注册池中的号码

当号码处于Unregistered状态时，显示的是配置的注册号码模板，当号码处于Registered状态时，显示的是成功注册到语音服务器上的号码

State

号码的注册状态：

·Unregistered：表示号码处于未注册状态

·Registered：表示号码处于成功注册状态

**SRST \-- SRST配置命令 \-- id**

------------------------------------------------------------------------

**[id**]命令用来配置注册池中允许注册的SIP UA的条件。

**[undo **]**id**命令用来删除已有配置。

【命令】

**[id ** { **ip** *ip-address* \| **network** *network* [ **mask** { *mask-length* \| *mask* } ] \| **mac** *mac-address* }]

**[undo** **id**]

【缺省情况】

没有限定允许注册的条件。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip **]*ip-address*：[允许注册的]SIP [UA]的IP地址。

**[network **]*network*：[允许注册的]SIP [UA]的IP网段。

**[mask**[ { *mask-length* \| *mask* }]]：子网掩码。其中，*mask-length*为子网掩码长度，*mask*为点分十进制格式的子网掩码，取值范围为0～32。不指定**mask**关键字，设备默认子网掩码为0.0.0.0，即拒绝所有SIP UA的注册请求。

**[mac **]*mac-address*：[允许注册的]SIP [UA]的MAC地址，格式为H-H-H。

【使用指导】

·在注册池中可以通过**id**命令配置允许注册的SIP UA的条件，也可以通过**number**命令配置允许注册的号码。至少要选择其中一种方式来指定能够注册的SIP UA的注册信息。如果同时配置，那么只有同时满足两者条件的SIP UA才能注册成功。

·如果当前的注册池下已经配置了**number**命令，并生成动态VoIP语音实体，那么增加配置**id**后，此注册池下生成的所有已存在的动态VoIP语音实体都会被删除。

【举例】

\# 配置注册池100中[允许注册的]SIP [UA]的MAC地址为1cbd-b9e3-b2e4。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 id mac 1cbd-b9e3-b2e4

【相关命令】

·**number**(Pool view)

**SRST \-- SRST配置命令 \-- max-dn**

------------------------------------------------------------------------

**[max-dn**]命令用来配置DN（Directory Number，号码目录）的最大数量。

**[undo max-dn**]命令用来恢复缺省情况。

【命令】

**[max-dn** *max-dn*]

**[undo** **max-dn**]

【缺省情况】

DN的最大数量为0，即不允许配置DN。

【视图】

全局注册视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-dn*]：DN的最大数量，取值范围为1～200。

【使用指导】

在DN下的号码完成注册并产生动态VoIP语音实体后，如果要修改**max-dn**命令的参数，可以直接将该参数增大。但是如果要将该参数减小，需要使用**undo voice register dn**命令先手工删除比将要配置的*max-dn*参数值大的*dn-tag*。

【举例】

\# 配置DN的最大数量为100。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register global

Sysname-voice-register-global max-dn 100

【相关命令】

·**voice register dn**

**SRST \-- SRST配置命令 \-- max-pool**

------------------------------------------------------------------------

**[max-pool**]命令用来配置注册池的最大数量。

**[undo max- pool**]命令用来恢复缺省情况。

【命令】

**[max-pool** *max-pool*]

**[undo max-pool**]

【缺省情况】

注册池的最大数量为0，即不允许配置注册池。

【视图】

全局注册视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-pool*]：注册池的最大数量，取值范围为1～200。

【使用指导】

在注册池下的号码完成注册并产生动态VoIP语音实体后，如果要修改**max-pool**命令的参数，可以直接将该参数增大。但是如果要将该参数减小，需要使用**undo voice register pool**命令先手工删除比将要配置的*max-pool*参数值大的*pool-tag*。

【举例】

\# 配置注册池的最大数量为100。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register global

Sysname-voice-register-global max-pool 100

【相关命令】

·**voice register pool**

**SRST \-- SRST配置命令 \-- mode**

------------------------------------------------------------------------

**[mode**]命令用来配置设备作为语音服务器时的工作模式。

**[undo **]**mode**命令用来恢复缺省情况。

【命令】

**[mode ** { **alive** \| **alone** }]

**[undo **]**mode**

【缺省情况】

设备工作在非语音服务器模式。

【视图】

全局注册视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[alone**]：设备作为语音服务器工作在独立模式。

**[alive**]：设备作为语音服务器工作在本地存活模式。

【使用指导】

改变语音服务器的工作模式时，语音服务器上已有的SIP UA注册信息都将被自动删除。

【举例】

\# 配置设备作为语音服务器工作在独立模式。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register global

Sysname-voice-register-global mode alone

**SRST \-- SRST配置命令 \-- number(DN view)**

------------------------------------------------------------------------

**[number**]命令用来配置[允许注册的号码模板。]

**[undo** **number**]命令用来删除已有配置。

【命令】

**[number ***number*]

**[undo number**]

【缺省情况】

不存在允许注册的号码模板。

【视图】

DN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：允许注册的号码模板，为1～31个字符的字符串，取值范围为数字0～9和\$。\$只能配置在号码的最后一位，表示号码结束，号码必须全部匹配\$之前的字符串。

【使用指导】

一个DN目录只能配置一个号码模板，例如配置**number** 1000，号码1000是一个号码模板，表示可以匹配以1000号码开头的号码。如果有语音组网中有话机10001，10002，10003，那么这些号码都可以注册到语音服务器上。

【举例】

\# 配置[允许注册的号码模板。]

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 100

Sysname-voice-register-dn100 number 1000

**SRST \-- SRST配置命令 \-- number(Register pool view)**

------------------------------------------------------------------------

**[number**]命令用来配置注册池中[允许注册的号码模板。]

**[undo** **number**]命令用来删除已有配置。

【命令】

**[number ***tag*****[{ *number \|* **dn** *dn-tag* }]]

**[undo number ***tag*]

【缺省情况】

不存在允许注册的号码模板。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag*]：号码索引，取值范围为1～10。

*[number*]：允许注册的号码模板，为1～31个字符的字符串，取值范围为数字0～9和\$，且"\$"只能配置在号码的最后一位。

**[dn*** dn-tag*]：应用到注册池的号码目录索引，取值范围为1～200。

【使用指导】

·在注册池中可以通过**id**命令配置允许注册的SIP UA的条件，也可以通过**number**命令配置允许注册的号码。至少要选择其中一种方式来指定能够注册的SIP UA的注册信息。如果同时配置，那么只有同时满足两者条件的SIP UA才能注册成功。

·在使用**number**命令配置[允许注册的号码时，可以直接配置号码，也可以通过引用]DN（Directory Number，号码目录）的配置。如果使用引用目录号码方式，引用的目录号码必须已经存在。

·如果当前的注册池下已经配置了**id**命令，并生成动态VoIP语音实体，那么使用**number**命令新增配置[允许注册的号码模板后，会删除不符合新增配置的已有动态]VoIP语音实体。

·一个注册池可以配置十个号码索引，并且配置的*number*参数是一个号码模板。例如配置**number** 1000，号码1000是一个号码模板，表示可以匹配以1000号码开头的号码。如果有语音组网中有话机10001，10002，10003，那么这些号码都可以注册到语音服务器上。

【举例】

\# 配置[允许注册的号码模板。]

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 number 1000

【相关命令】

·**voice register dn**

**SRST \-- SRST配置命令 \-- outband**

------------------------------------------------------------------------

**[outband**]命令用来配置使用带外方式传输DTMF（Dual Tone Multi-Frequency，双音多频）信号。

**[undo** **outband**]命令用来恢复缺省情况。

【命令】

**[outband** { **nte** \| **sip** }]

**[undo** **outband**]

【缺省情况】

使用带内方式传输DTMF信号。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[nte**]：使用NTE（Named Telephone Event，命名的电话事件）带外方式传输DTMF信号。

**[sip**]：使用SIP带外方式传输DTMF信号。

【举例】

\# 配置使用NTE带外方式传输DTMF信号。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 10

Sysname-voice-register-pool10 outband nte

**SRST \-- SRST配置命令 \-- priority**

------------------------------------------------------------------------

**[priority**]命令用来配置指向SIP UA的动态VoIP语音实体的优先级。

**[undo** **priority**]命令用来恢复缺省情况。

【命令】

**[priority** *order*]

**[undo** **priority**]

【缺省情况】

优先级为0。

【视图】

DN视图/注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[order*]：为号码生成动态VoIP语音实体的优先级，取值范围为0～10，数值越小表示优先级越高。

【举例】

\# 配置为DN视图下号码模版1000生成动态VoIP语音实体的优先级为5。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 100

Sysname-voice-register-dn100 number 1000

Sysname-voice-register-dn100 priority 5

\# 配置为注册池下号码模版2000生成动态VoIP语音实体的优先级为6。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 10

Sysname-voice-register-pool10 priority 6

Sysname-voice-register-pool10 number 2000

【相关命令】

·**number******(DN view)

·**number******(Pool view)

**SRST \-- SRST配置命令 \-- proxy**

------------------------------------------------------------------------

**[proxy**]命令用来配置远端语音服务器地址信息及开启保活探测功能。

**[undo proxy**]命令用来删除已配置信息。

【命令】

**[proxy ip ***ip1 * **port** *main-port-number* ]  **monitor probe sip** [ *ip2* [ **port** *backup-port-number*  ] ]  **priority** *order*

**[undo** **proxy**]

【缺省情况】

没有配置语音远端服务器信息。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip1*]：远端语音主服务器的IPv4地址。

**[port** *main-port-number*]：远端语音主服务器的端口号，取值范围为1～65535，缺省值为5060。

**[monitor probe sip**]：开启保活探测功能。

*[ip2*]：远端备份语音服务器的IPv4地址。

**[port** *backup-port-number*]：远端备份语音服务器的端口号，取值范围为1～65535，缺省值为5060。

*[priority*]：产生的指向远端语音主服务器的动态VoIP语音实体的优先级，取值范围为0～10，缺省值为0。

【使用指导】

·该命令只能在本地存活模式的语音服务器上生效。

·此命令可以完成两个功能，一是配置远端主、备语音服务器信息，二是开启保活探测功能（可选），保活探测的具体参数由注册池下的**voice-class sip options-keepalive**命令确定。如果配置**monitor probe sip**参数开启保活探测功能，生成的指向远端语音服务器的动态VoIP语音实体会返回保活探测结果。如果保活探测结果为VoIP entity available，则表示远端语音服务器可达。

【举例】

\# 配置远端服务器地址信息，并开启保活探测功能。SIP UA号码成功注册到语音服务上后，在语音服务上生成指向指定远端服务器（IP地址为1.1.1.1）的动态VoIP语音实体。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 proxy ip 1.1.1.1 monitor probe sip

【相关命令】

·**voice-class sip options-keepalive**

**SRST \-- SRST配置命令 \-- registrar server**

------------------------------------------------------------------------

**[registrar server**]命令用来开启接受注册服务，并配置全局注册时间。

**[undo** **registrar** **server**]命令用来关闭注册服务。

【命令】

**[registrar**[ **server** [ **expires** { **max** *max * \| **min** *min* } **\*** ]]]

**[undo registrar server**]

【缺省情况】

接受注册服务处于关闭状态。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[expires**]：指定服务器接受的注册有效时间。缺省情况下，接受的注册有效时间范围为60～3600秒。

**[max**]：全局注册有效时间的最大值，取值范围为120～86400，单位为秒。缺省情况下，注册有效时间的最大值为3600秒。

**[min**]：全局注册有效时间的最小值，取值范围为60～3600，单位为秒。缺省情况下，注册有效时间的最小值为60秒。

【使用指导】

·开启该命令后，设备作为语音服务器才能接收SIP UA的注册。接收到SIP UA的注册报文中，如果注册时间不在指定的范围内，语音服务器会通知SIP UA其可接受的注册有效时间。

·使用**undo** **registrar** **server**命令关闭注册服务后，设备会拒绝新SIP UA的注册请求，对已有注册SIP UA号码没有影响，已注册SIP UA在老化时间超时后，注销其信息。

·在注册池下如果没有配置注册有效时间，缺省采用**registrar server**命令配置的全局注册有效时间。如果都进行了配置，则优先采用注册池视图下注册有效时间的配置。

【举例】

\# 配置开启注册服务，全局配置中注册有效时间的最大值为3000秒，最小值为100秒。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip registrar server expires max 3000 min 100

【相关命令】

·**mode**

·**voice register global**

**SRST \-- SRST配置命令 \-- registration-timer**

------------------------------------------------------------------------

**[registration-timer**]命令用来配置注册池下的注册有效时间。

**[undo** **registration-timer**]命令用来删除已有配置。

【命令】

**[registration-timer max ***max*** min ***min*]

**[undo registration-timer**]

【缺省情况】

注册池下没有缺省的注册有效时间。如果该注册池下没有注册有效时间，那么该注册池使用全局命令**registrar server**设置的全局注册有效时间。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[max**]：注册有效时间的最大值，取值范围为120～86400，单位为秒。

**[min**]：注册有效时间的最小值，取值范围为60～3600，单位为秒。

【使用指导】

在注册池下如果没有配置注册有效时间，缺省采用**registrar server**命令配置的全局注册有效时间。如果都进行了配置，则优先采用注册池视图下注册有效时间的配置。

【举例】

\# 配置注册有效时间最大值为2000，最小值为300。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 registration-timer max 2000 min 300

【相关命令】

·**registrar** **server**

**SRST \-- SRST配置命令 \-- substitute**

------------------------------------------------------------------------

**[substitute**]命令用来将指定号码变换规则表绑定到注册池。

**[undo** **substitute**]命令用来取消已有的绑定关系。

【命令】

**[substitute**[ { **called** \| **calling** } *list-number*]]

**[undo**[ **substitute** { **called** \| **calling** }]]

【缺省情况】

没有绑定号码变换规则表，即不进行号码变换。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[called**]：对被叫号码应用号码变换。

**[calling**]：对主叫号码应用号码变换。

*[list-number*]：绑定的号码变换规则表的序号，取值范围为1～2147483647。

【使用指导】

·可以将一个不存在的号码变换规则表绑定到注册池，但只有完成号码变换规则表的配置后，该号码变换规则表才能生效。

·在注册池下只能绑定一种号码变换规则表，如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 配置将号码变换规则表6绑定到注册池100，表示对被叫号码应用号码变换。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 substitute called 6

【相关命令】

·**number-substitute**（语音命令参考/拨号策略）

·**rule**（语音命令参考/拨号策略）

**SRST \-- SRST配置命令 \-- username**

------------------------------------------------------------------------

**[username**]命令用来配置注册池中的鉴权信息。

**[undo**] **username**命令用来删除已有配置。

【命令】

**[username**[ *username* **password** { **cipher** \| **simple** } *password* ]]

**[undo** **username**]

【缺省情况】

不存在鉴权信息，即语音服务器不对SIP UA进行鉴权。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：用户名，为1～63个字符的字符串，区分大小写。

**[cipher**]：以密文方式设置用户的密码。

**[simple**]：以明文方式设置用户的密码。

*[password*]：明文密码或密文密码，区分大小写。明文密码的长度范围是1～16；密文密码的长度范围是1～53。

【使用指导】

·使用**authentication register**命令开启注册鉴权后，语音服务器会使用本命令配置的鉴权信息对SIP UA进行鉴权。

·工作在本地存活模式的语音服务器不会对用户信息进行鉴权，因此在该模式的语音服务器上配置的鉴权信息不会生效。

·需要注意的是，在注册池下配置的**username**命令不会同步到动态VoIP语音实体上。

【举例】

\# 配置注册池中的鉴权信息，用户名为abcd，以明文方式设置密码为1234。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 username abcd password simple 1234

【相关命令】

·**authenticate register**

**SRST \-- SRST配置命令 \-- voice register dn**

------------------------------------------------------------------------

**[voice register dn**]命令用来创建并进入指定的DN视图。

**[undo **]**voice register dn**命令用来删除指定的DN。

【命令】

**[voice register dn **]*dn*-*tag*

**[undo**]**voice register dn ***dn-tag*

【缺省情况】

不存在DN。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dn-tag*]：号码目录索引，取值范围为1～200。

【使用指导】

如果需要为某个号码做特殊的配置，例如配置指向其的动态VoIP语音实体或是为该号码开启特定的语音业务，这时可以配置DN，然后将DN引用到注册池中，实现将DN下号码注册到语音服务器上。需要注意的是，DN下的配置优先级高于Pool注册池下的配置。例如在注册池下配置**id**命令，使10.1.1.0网段上的IP话机使用该注册池的设置，在这个网段中对于号码为1000的IP话机需要做特殊配置，例如修改指向号码1000的动态VoIP语音实体的优先级为1，这时可以为号码1000配置DN，在DN视图配置**priority** 1，该配置优先于号码1000所在注册池的**priority**命令优先级。

【举例】

\# 创建号码目录100，并进入指定的视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 100

Sysname-voice-register-dn100

【相关命令】

·**max-dn**

**SRST \-- SRST配置命令 \-- voice register global**

------------------------------------------------------------------------

**[voice register global**]命令用来创建并进入全局注册视图。

**[undo** **voice register global**]命令用来删除全局注册视图。

【命令】

**[voice register global**]

**[undo voice register global**]

【缺省情况】

不存在全局注册视图。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置**undo** **voice register global**命令后，设备会自动删除已存在的DN、注册池和所有动态VoIP语音实体，并强制注销已注册的SIP UA。

【举例】

\# 创建并进入全局注册视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register global

Sysname-voice-register-global

**SRST \-- SRST配置命令 \-- voice register pool**

------------------------------------------------------------------------

**[voice register pool**]命令用来创建并进入指定的注册池视图。

**[undo **]**voice register pool**命令用来删除指定的注册池。

【命令】

**[voice register pool **]*pool*-*tag*

**[undo**]**voice register pool ***pool*-*tag*

【缺省情况】

不存在注册池。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pool-tag*]：注册池索引，取值范围为1～200。

【使用指导】

·注册池是SIP UA注册信息的集合，如果SIP UA的注册信息匹配上注册池中配置的条件，那么这些SIP UA可以注册到语音服务器上。

·执行**undo** **voice register pool**命令时，由该注册池生成的所有动态VoIP语音实体会被删除。

【举例】

\# 创建注册池索引100，并进入指定的视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100

【相关命令】

·**max-pool**

**SRST \-- SRST配置命令 \-- voice-class codec**

------------------------------------------------------------------------

**[voice-class codec**]命令用来将指定的编解码模板绑定到注册池。

**[undo voice-class codec**]用来取消已有的绑定。

【命令】

**[voice-class codec** *tag*]

**[undo voice-class codec**]

【缺省情况】

编解码模板和注册池没有绑定关系。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag*]：绑定的编解码模板号，取值范围为1～2147483647。

【使用指导】

·可以将一个不存在的编解码模板绑定到注册池，但只有在使用**codec preference**命令完成编解码优先级的设置后，该编解码模板才能生效。

·在注册池下只能绑定一个编解码模板，如果多次执行该命令，新的配置会覆盖已有配置。

【举例】

\# 将编解码模板1绑定到注册池100。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 voice-class codec 1

【相关命令】

·**codec preference**（语音命令参考/语音实体）

·**voice class codec**（语音命令参考/语音实体）

**SRST \-- SRST配置命令 \-- voice-class sip options-keepalive**

------------------------------------------------------------------------

**[voice-class sip options-keepalive**]命令用来配置保活报文的参数。

**[undo voice-class sip options-keepalive**]命令用来恢复缺省情况。

【命令】

**[voice-class sip options-keepalive** [ **up-interval** *seconds*   **down-interval** *seconds*   **retry** *retries* ]]

**[undo voice-class sip options-keepalive**]

【缺省情况】

**[up-interval**]为60秒，**down-interval**为30秒，**retry**为5次。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[up-interval ***seconds*]：在标记远端语音服务器为不可用前，本地语音服务器发送OPTIONS报文的时间间隔。取值范围为5～1200。单位为秒。该参数在远端语音服务器为可达时生效。

**[down-interval ***seconds*]：在标记远端语音服务器为可用前，本地语音服务器发送OPTIONS报文的时间间隔。取值范围为5～1200。单位为秒。该参数在远端语音服务器为可达时生效。

**[retry ***retries*]：在改变远端语音服务器状态前，重复探测的次数。取值范围为1～10。

【使用指导】

使用**proxy**命令开启保活功能后，本地语音服务器会按配置的**up-interval**参数定时发送OPTIONS报文，如果本地语音服务器在**up-interval**时间内收到远端语音服务器应答报文，则表示远端服务器处于可达状态，本地语音服务器继续使用**up-interval**参数定时发送OPTIONS报文；如果本地语音服务器在**up-interval**时间内没有收到应答报文或是收到的应答报文为408、499以及5XX（500、501、502、503、504、513除外），会开始重复探测，每次探测的时间间隔由**timers options**命令控制，在完成重复探测后，若还未收到表示远端语音服务器可用的应答报文，则表示本地语音服务器处于不可达状态。

如果远端语音服务器被判定为处于不可达状态，则本地语音服务器会按配置的**down-interval**参数定时发送OPTIONS报文，如果收到表示远端语音服务器可达的应答报文，会开始重复探测，每次探测的时间间隔由**timers options**命令控制，在重复探测期间，本地语音服务器每次都能收到远端 语音服务器的应答报文，则将远端语音服务器的状态恢复为可达。如果一直没有收到表示远端语音服务器可达的应答报文，则本地语音服务器继续按配置的**down-interval**参数定时发送OPTIONS报文。

需要注意的是，在注册池下配置的**voice-class sip options-keepalive**命令不会同步到动态VoIP语音实体上。

【举例】

\# 配置保活报文的参数，**up-interval**为50秒，**down-interval**为20秒，**retry**为2次。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 100

Sysname-voice-register-pool100 voice-class sip options-keepalive up-interval 50 down-interval 20 retry 2

【相关命令】

·**proxy**

·**timers options**（语音命令参考/SIP）

**SRST \-- SRST业务配置命令 \-- after-hours block pattern**

------------------------------------------------------------------------

**[after-hours block pattern**]命令用来开启呼叫阻塞功能。

**[undo after-hours block pattern**]命令用来关闭呼叫阻塞功能。

【命令】

**[after-hours block pattern ***pattern-tag pattern***** **7-24** ]

**[undo after-hours block pattern ***pattern-tag*]

【缺省情况】

呼叫阻塞功能处于关闭状态。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pattern-tag*]：呼叫阻塞索引，取值范围为[1]～100。

*[pattern*]：匹配阻塞的被叫号码模板，为1～31个字符的字符串，由"0-9#\*[.!+%[]()-]"中的字符组合形成的字符串，第一个字符必须为数字。各符号的含义如[表]1-4(?1526392022#_Ref148492379)所示。

·加号"+"：号码模板如果以"+"号开头，"+"号表示整个号码是一个E.164标准号码，如+110022表示110022是符合E.164标准的号码。

·美元符号"\$"：只能放在结尾，表示号码结束，号码必须全部匹配\$之前的*string*部分。如果号码模板后没有\$字符，则表示可以匹配以此号码开头的号码，例如配置**match-template **20，表示可以匹配以20号码开头的号码。

·符号"T"：T表示定时器，表示在用户输入的号码超过最大长度、用户拨号码终止符或是定时器超时前，设备会等待用户拨号。

·*string*：由"0-9#\*[.!+%[]()-]"中的字符组合形成的字符串。各符号的含义如[表]1-4(?1526392022#_Ref148492379)所示。

表1-4 符号含义描述表

符号

含义

0-9

一位数字表示一位号码，0到9之间的数字

\#和\*

表示一位有效号码

.

通配符，可以与任何一位有效号码匹配。如：555. . . . 可以匹配任何以555开头的并有四位附加字符的号码

!

指明符号前的字符串重复零次或一次。如：56!1234可以匹配51234和561234

符号"!%+"前的字符串（一位号码或号码串），作为非精确匹配的号码，处理类似"**.**"通配符；这些符号不能作为独立号码，之前必须有有效号码或号码串

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

**[7-24**]：表示1周7天，每天24小时呼叫都被阻塞。不指定该关键字将不开启全天候呼叫阻塞功能，用户可配合**after-hours day**和**after-hours date**命令按需配置特定时间的呼叫阻塞功能。

【使用指导】

·如果被叫号码可以匹配多个*pattern*（匹配阻塞的被叫号码模板），以*pattern-tag*最小的被叫号码模板为准。

·如果在注册池下同时配置呼叫前转，呼叫阻塞的优先级高于呼叫前转功能。

【举例】

\# 对被叫号码模板1000开启呼叫阻塞功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice after-hours block pattern 1 1000 7-24

【相关命令】

·**after-hours date**

·**after-hours day**

·**after-hours exempt**

**SRST \-- SRST业务配置命令 \-- after-hours date**

------------------------------------------------------------------------

**[after-hours date**]命令用来配置对每月的特定时间开启呼叫阻塞。

**[undo after-hours date**]命令用来取消已有配置。

【命令】

**[after-hours date ***month date start-time stop-time*]

**[undo after-hours date ***month date*]

【缺省情况】

没有对呼叫阻塞时间进行限定。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[month*]：指定的月份，取值为：January、February、March、April、May、June、July、August、September、October、November、December。最少输入月份拼写的前三个字符，例如Jan，不区分大小写。

*[date*]：日期，取值范围为1～31。

*[start-time*]：呼叫阻塞的起始时间，格式是HH:MM，且使用24小时制。24:00是无效值。

*[stop-time*]：呼叫阻塞的结束时间，格式与*start-time*相同。24:00是无效值。如果将00:00作为*stop-time*，则会自动被修改成23:59。

【使用指导】

·如果*start-time*和*stop-time*都是00:00，那么在指定的这一天，呼叫将会被阻塞24小时。如果结束时间小于起始时间，代表呼叫阻塞从当天的起始时间开始一直持续到后一天的结束时间。

·如果还配置了**after-hours day**命令，那么实际阻塞时间为这两条命令的合集。

【举例】

\# 配置从4月1日上午8点到晚上8点开启呼叫阻塞。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice after-hours date apr 1 08:00 20:00

【相关命令】

·**after-hours block**

·**after-hours day**

·**after-hours exempt**

**SRST \-- SRST业务配置命令 \-- after-hours day**

------------------------------------------------------------------------

**[after-hours day**]命令用来配置对每周的特定时间开启呼叫阻塞。

**[undo after-hours day**]命令用来取消已有配置。

【命令】

**[after-hours day ***day start-time stop-time*]

**[undo after-hours day ***day*]

【缺省情况】

没有对呼叫阻塞时间进行限定。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[day*]：指定的一周中的一天，取值为：Sunday、Monday、Tuesday、Wednesday、Thursday、Friday、Saturday。最少输入英文拼写的前三个字符，例如Sat，不区分大小写。

*[start-time*]：呼叫阻塞的起始时间，格式是HH:MM，使用的是24小时制。24:00是无效值。

*[stop-time*]：呼叫阻塞的结束时间，格式与*start-time*相同。24:00是无效值。如果将00:00作为*stop-time*，则会自动被修改成23:59。

【使用指导】

·如果*start-time*和*stop-time*都是00:00，那么在指定的这一天，呼叫将会被阻塞24小时。如果结束时间小于起始时间，代表呼叫阻塞从当天的起始时间开始一直持续到后一天的结束时间。

·如果还配置了**after-hours date**命令，那么实际阻塞时间为这两条命令的合集。

【举例】

\# 配置对每周一的上午8点到晚上8点开启呼叫阻塞。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice after-hours day mon 08:00 20:00

【相关命令】

·**after-hours block**

·**after-hours date**

·**after-hours exempt**

**SRST \-- SRST业务配置命令 \-- after-hours exempt**

------------------------------------------------------------------------

**[after-hours** **exempt**]命令用来免除呼叫阻塞。

**[undo after-hours**]命令用来取消免除呼叫阻塞。

【命令】

**[after-hours exempt**]

**[undo after-hours**]

【缺省情况】

没有配置免除呼叫阻塞。

【视图】

DN视图/注册池视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置**after-hours exempt**命令后，DN或注册池下的号码可以免除呼叫阻塞的作用。

【举例】

\# 对号码1000免除呼叫阻塞。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 1

Sysname-voice-register-dn1 after-hours exempt

Sysname-voice-register-dn1 number 1000\$

【相关命令】

·**after-hours block**

·**after-hours day**

·**after-hours date**

**SRST \-- SRST业务配置命令 \-- call-forward b2bua**

------------------------------------------------------------------------

**[call-forward b2bua**]命令用来开启呼叫前转功能。

**[undo call-forward b2bua**]命令用来关闭呼叫前转功能。

【命令】

注册池视图下：

**[call-forward b2bua ***[number*****[\| **busy** ]*number*****[\| **noan** ]*number***** **timeout** ]*seconds*  }]

**[undo call-forward b2bua **[{ **all** \| **busy** \| **noan** }]]

DN视图下：

**[call-forward b2bua ***[number*****[\| **busy** ]*number*****[\| **noan** ]*number*****[ **timeout** *seconds*  \| **unregistered** ]*number*****}]

**[undo call-forward b2bua **[{ **all** \| **busy** \| **noan** \| **unregistered** }]]

【缺省情况】]

呼叫前转功能处于关闭状态。

【视图】

DN视图/注册池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：配置无条件呼叫前转。

**[busy**]：配置遇忙呼叫前转。

**[noan**]：配置无应答呼叫前转。

**[unregistered**]：配置未注册呼叫前转。

**[timeout**]：指定无应答呼叫前转超时时间。

*[number*]：呼叫前转的目的号码，为1～31个字符的字符串，取值范围为数字0～9。

*[seconds*]：无应答超时时间，取值范围为2～120，单位为秒。该时间超时后，触发无应答呼叫前转。缺省值为20秒。

【使用指导】

·**all**、**busy**、**noan**参数可以在注册池、DN视图下配置，**unregistered**参数只能在DN视图下配置。

·语音服务器支持无条件、遇忙、无应答和未注册四种呼叫前转，按优先级从高到低依次是：无条件前转、遇忙前转、无应答前转。未注册前转不会和其他三种前转出现在同一动态VoIP语音实体中，其优先级与其他三种没有可比性。

·实际应用时，为了保证该功能能够正常使用，请用户合理、有效地规划前转目的号码，避免出现错号、循环呼叫。

·为避免循环前转，目前一个呼叫最多可以前转5次。

·如果在注册池下同时配置DND，DND的优先级高于呼叫前转功能。

·如果在注册池下同时配置呼叫阻塞，呼叫阻塞的优先级高于呼叫前转功能。

【举例】

\# 配置遇忙呼叫前转功能，当有电话呼叫号码5000时，如果号码5000处于通话状态，该路呼叫会被前转到目的号码8000上。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 3

Sysname-voice-register-dn3 number 5000

Sysname-voice-register-dn3 call-forward b2bua busy 8000

\# 配置未注册呼叫前转功能，当有电话呼叫号码3000时，如果号码3000没有应用到注册池，即生成号码3000的未注册动态VoIP语音实体，该路呼叫会被前转到目的号码2000上。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 3

Sysname-voice-register-dn3 number 3000

Sysname-voice-register-dn3 call-forward unregistered 2000

**SRST \-- SRST业务配置命令 \-- display voice fac**

------------------------------------------------------------------------

**[display** **voice** **fac**]命令用来显示配置的FACs。

【命令】

**[display voice fac**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

设备作为语音服务器或网关模式下都可以使用该命令查看配置的FACs。

【举例】

\# 显示网关模式下标准的FACs。

\<Sysname\> display voice fac

Standard FACs enabled in gateway mode

  callfwd all \*57\*

  callfwd all cancel #57#

  callfwd busy \*40\*

  callfwd busy cancel #40#

  callfwd noan \*41\*

  callfwd noan cancel #41#

\# 显示语音服务器模式下标准的FACs。

\<Sysname\> display voice fac

Standard FACs enabled in server mode

  pickup direct \*80\*

  pickup local \*81\*

  pickup group \*82\*

  callfwd all \*57\*

  callfwd all cancel #57#

  callfwd busy \*40\*

  callfwd busy cancel #40#

  callfwd noan \*41\*

  callfwd noan cancel #41#

  callfwd unregistered \*44\*

  callfwd unregistered cancel #44#

  dnd \*70\*

  dnd cancel #70#

![说明](SRST命令.files/image001.png)

设备作为语音服务器时，**display voice fac**命令显示信息中会存在拨号结束符的配置信息，但该配置并不生效。

表1-5 display voice fac显示信息描述表

字段

描述

Custom

自定义的FACs

Standard

标准的FACs

gateway mode

FACs工作在网关模式

server mode

FACs工作在语音服务器模式

fac terminator

FACs结尾符

callfwd

呼叫前转，取值包括：

·all：无条件呼叫前转FACs

·all-cancel：取消无条件前转FACs

·busy：遇忙前转FACs

·busy-cancel：取消遇忙前转FACs

·noan：无应答前转FACs

·noan-cancel：取消无应答前转FACs

·unregistered：未注册前转FACs

·unregistered-cancel：取消未注册前转FACs

dnd

免打扰功能

pickup

呼叫代答FACs，取值包括：

·direct：直接呼叫代答FACs

·group：组间呼叫代答FACs

·local：组内呼叫代答FACs

**SRST \-- SRST业务配置命令 \-- dnd**

------------------------------------------------------------------------

**[dnd**]命令用来开启DND（Do-not Disturb，免打扰）功能。

**[undo dnd**]命令用来关闭DND功能。

【命令】

**[dnd**]

**[undo dnd**]

【缺省情况】

DND功能处于关闭状态。

【视图】

注册池视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·开启DND功能，对注册池下的号码实现禁止入呼叫，即这些号码作为被叫接受呼叫时，会回复用户忙。但是这些号码向外发起呼叫是不受限的。

·如果在注册池下同时配置呼叫前转，DND的优先级高于呼叫前转功能。

【举例】

\# 为注册池1开启DND功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register pool 1

Sysname-voice-register-pool1 dnd

**SRST \-- SRST业务配置命令 \-- fac custom**

------------------------------------------------------------------------

**[fac** **custom**]命令用来配置自定义FACs（Feature Access Codes，业务特征码）功能。

**[undo fac** **custom**]命令用来关闭FACs功能。

【命令】

**[fac**[ **custom** { **alias ** *id* *custom-string* **to** *existing-string* \| **callfwd** { **all** \| **all-cancel** \| **busy** \| **busy-cancel** \| **noan** \| **noan-cancel** \| **unregistered** \| **unregistered-cancel** } *string* \| **dnd** [ **cancel** ] *string* \| **pickup** { **direct** \| **group** \| **local** } *string* }]]

**[undo**[ **fac** **custom** { **alias ** *id* \| **callfwd** { **all** \| **all-cancel** \| **busy** \| **busy-cancel** \| **noan** \| **noan-cancel** \| **unregistered** \| **unregistered-cancel** } \| **dnd** \| **pickup** { **direct** \| **group** \| **local** } }]]

【缺省情况】

FACs功能处于关闭状态。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[alias ***id*]：自定义FACs的标记，取值范围为0～9。

*[custom-string*]：自定义新FACs，为1～10个字符的字符串，取值范围为数字0～9、\*和\#。

*[existing-string*]：已有的FACs，为1～10个字符的字符串，取值范围为数字0～9、\*和\#。

**[pickup**]：自定义呼叫代答FACs。

**[direct**]：自定义直接呼叫代答FACs。

**[group**]：自定义组间呼叫代答FACs。

**[local**]：自定义组内呼叫代答FACs。

**[dnd**]：自定义DND的FACs。

**[cancel**]：取消自定义DND的FACs。

**[callfwd**]：自定义呼叫前转FACs。

**[all**]：自定义无条件呼叫前转FACs。

**[all-cancel**]：取消自定义无条件前转FACs。

**[busy**]：自定义遇忙前转FACs。

**[busy-cancel**]：取消自定义遇忙前转FACs。

**[noan**]：自定义无应答前转FACs。

**[noan-cancel**]：取消自定义无应答前转FACs。

**[unregistered**]：自定义未注册前转FACs。

**[unregistered-cancel**]：取消自定义未注册前转FACs。

*[string*]：自定义特征码，为1～10个字符的字符串，取值范围为数字0～9、\*和\#。

【使用指导】

·该命令不能和**fac standard**命令同时配置。

·设备作为网关或语音服务器时，均可以使用自定义FACs。需要注意的是，设备作为网关时，只支持呼叫前转（不包括未注册和不可用呼叫前转）FACs。

·配置自定义FACs时，建议不要将不同业务配置共用一个FACs。

【举例】

\# 配置自定义无条件呼叫前转FACs为1234。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice fac custom callfwd all 1234

【相关命令】

·**fac standard**

**SRST \-- SRST业务配置命令 \-- fac standard**

------------------------------------------------------------------------

**[fac** **standard**]命令用来配置标准FACs功能。

**[undo fac** **standard**]命令用来关闭标准FACs功能。

【命令】

**[fac** **standard**]

**[undo** **fac** **standard**]

【缺省情况】

FACs功能处于关闭状态。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·该命令不能和**fac custom**命令同时配置。

·设备作为网关或语音服务器时，均可以使用标准FACs。需要注意的是，设备作为网关时，只支持呼叫前转（不包括未注册和不可用呼叫前转）FACs。

【举例】

\# 配置标准FACs功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice fac standard

【相关命令】

·**fac custom**

**SRST \-- SRST业务配置命令 \-- fac terminator**

------------------------------------------------------------------------

**[fac** **terminator**]命令用来配置匹配FACs的结尾符。

**[undo fac** **terminator**]命令用来恢复缺省情况。

【命令】

**[fac** **terminator** *character*]

**[undo** **fac** **terminator**]

【缺省情况】

匹配FACs的结尾符为\#。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[character*]：结尾符，取值范围为数字0～9、"\#"、"\*"。

【使用指导】

该命令仅在设备作为网关模式，并且配置使用自定义FACs时才能生效。

【举例】

\# 配置匹配FACs的结尾符为\*。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice fac terminator \*

【相关命令】

·**fac custom**

**SRST \-- SRST业务配置命令 \-- moh file**

------------------------------------------------------------------------

**[moh file**]命令用来配置音乐保持媒体资源文件。

**[undo moh file**]命令用来取消已有配置。

【命令】

**[moh file ***filename*]

**[undo moh file**]

【缺省情况】

不存在音乐保持媒体资源文件。

【视图】

全局注册视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[filename*]：媒体资源文件名。

【使用指导】

呼叫被保持方可使用组播或单播方式接收音乐保持媒体流。

·配置使用单播方式接收音乐保持媒体流时，需要使用**call-hold-format sendonly**命令将呼叫保持的模式配置为放音模式。

·配置使用组播方式接收音乐保持媒体流时，需要使用**multicast** **moh** **ip**命令配置提供音乐保持媒体流的组播地址。

目前只支持G.711u和G.711a编解码的wav文件作为音乐保持媒体资源文件。

【举例】

\# 配置音乐保持媒体资源文件为cfa0:/g711u/moh.wav。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register global

Sysname-voice-register-global moh file cfa0:/g711u/moh.wav

【相关命令】

·**call-hold-format**（语音命令参考/语音业务）

·**multicast** **moh** **ip**

**SRST \-- SRST业务配置命令 \-- multicast moh**

------------------------------------------------------------------------

**[multicast** **moh**]命令用来配置提供音乐保持媒体流的组播地址。

**[undo multicast moh ip**]命令用来删除已有配置。

【命令】

**[multicast** **moh** **ip** *multicast-address* **port** *port-number* **route** *address-list*&\<1-5\>]

**[undo multicast** **moh** **ip**]

【缺省情况】

不存在提供音乐保持媒体流的组播地址。

【视图】

全局注册视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip** *multicast-address*]：提供音乐保持媒体流的组播地址，取值范围为224.0.1.0～239.255.255.255。

**[port** *port-number*]：提供音乐保持媒体流的端口号，取值范围为2000～65535。

**[route ***address-list*&\<1-5\>]：组播路由出口地址，可以从这些出接口将音乐保持媒体流发送到配置的组播地址。*address-list*&\<1-5\>表示以空格为分隔，最多可以配置5个组播路由出接口地址。

【举例】

\# 配置提供音乐保持媒体流的组播地址。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register global

Sysname-voice-register-global multicast moh ip 239.1.1.1 port 2009 route 192.168.4.16

【相关命令】

·**moh** **file**

**SRST \-- SRST业务配置命令 \-- mwi**

------------------------------------------------------------------------

**[mwi**]命令用来开启消息等待指示功能。

**[undo mwi**]命令用来关闭消息等待指示功能。

【命令】

**[mwi**]

**[undo mwi**]

【缺省情况】

消息等待指示功能处于关闭状态。

【视图】

DN视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 为号码1000开启消息等待指示功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 100

Sysname-voice-register-dn100 number 1000

Sysname-voice-register-dn100 mwi

【相关命令】

·**mode**

**SRST \-- SRST业务配置命令 \-- pickup-call any-group**

------------------------------------------------------------------------

**[pickup-call any-group**]命令用来配置代答方以"GPickUp软键\*"按键实现组间代答。

**[undo pickup-call any-group**]命令用来删除已有配置。

【命令】

**[pickup-call any-group**]

**[undo pickup-call any-group**]

【缺省情况】

没有配置此命令。

【视图】

DN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

假设被代答方IP Phone A存在某个代答组中，而代答方IP Phone B不在该代答组中或是不在任何代答组中，在这种情况下，为IP Phone B号码配置**pickup-call any-group**，IP Phone B可以用按 "GPickUp软键"，然后拨打"\*"的方式为IP Phone A代答。

【举例】

\# 配置用DN1注册成功的话机以"GPickUp软键\*"按键实现组间代答。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 1

Sysname-voice-register-dn1 number 1000

Sysname-voice-register-dn1 pickup-call any-group

**SRST \-- SRST业务配置命令 \-- pickup-group**

------------------------------------------------------------------------

**[pickup-group**]命令用来为号码指定呼叫代答组。

**[undo pickup-group**]命令用来删除已配置的呼叫代答组。

【命令】

**[pickup-group ***group-number*]

**[undo pickup-group**]

【缺省情况】

没有配置呼叫代答组。

【视图】

DN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：呼叫代答组，为1～31个字符的字符串，取值范围为数字、字母、\#、\*，字母区分大小写。

【举例】

\# 配置用DN100注册成功的话机属于呼叫代答组25。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice voice register dn 100

Sysname-voice-register-dn100 number 1000

Sysname-voice-register-dn100 pickup-group 25

