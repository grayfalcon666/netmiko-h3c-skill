
**语音业务 \-- 语音业务配置命令 \-- call-forwarding**

------------------------------------------------------------------------

**[call-forwarding**]命令用来配置呼叫前转功能。

**[undo** **call-forwarding**]命令用来关闭呼叫前转功能。

【命令】

**[call-forwarding**[ { **on-busy** \| **no-reply** \| **unavailable** \| **unconditional** } **number** *number*]]

**[undo**[ **call-forwarding** { **on-busy** \| **no-reply** \| **unavailable** \| **unconditional** }]]

【缺省情况】

呼叫前转功能处于关闭状态。

【视图】

POTS语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[on-busy**]：遇忙呼叫前转。

**[no-reply**]：无应答呼叫前转。

**[unavailable**]：线路不可用呼叫前转。

**[unconditional**]：无条件呼叫前转。

**[number*** number*]：呼叫前转的目的号码，为1～31字符的字符串，取值范围为数字0～9。

【使用指导】

·四种前转类型可以同时配置，按优先级从高到底分别是**unconditional**、**unavailable**、**on-busy**、**no-reply**。

·配置该功能时，需要保证前转发起方必须有到前转目的方的呼叫路由。

·本命令配置在POTS语音实体下，且只有该POTS语音实体上绑定的语音用户线为FXS语音用户线时，配置才能生效。

·实际应用时，为了保证该功能能够正常使用，请用户合理、有效地规划前转目的号码，避免出现错号、循环呼叫。

·目前，一个呼叫最多可以前转5次。

【举例】

\# 配置无应答呼叫前转功能，使呼叫前转到目的号码12345678上。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 call-forwarding no-reply number 12345678

\# 配置遇忙呼叫前转业务，使呼叫前转到目的号码12345678上。

\<Sysname\> system-view   

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 call-forwarding on-busy number 12345678

\# 配置不可用呼叫前转功能，使呼叫前转到目的号码12345678上。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 call-forwarding unavailable number 12345678

\# 配置无条件呼叫前转功能，使呼叫前转到目的号码12345678上。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 call-forwarding unconditional number 12345678

**语音业务 \-- 语音业务配置命令 \-- call-hold-format**

------------------------------------------------------------------------

**[call-hold-format**]命令用来配置呼叫保持模式。

**[undo call-hold-format**]命令用来恢复缺省情况。

【命令】

**[call-hold-format**[ { **inactive** \| **sendonly** [ **moh-number** *string* ] }]]

**[undo** **call-hold-format**]

【缺省情况】

呼叫保持采用**inactive**模式。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inactive**]：表示呼叫保持的模式为静音模式，用来指示被保持方关闭其发送和接收媒体通道。

**[sendonly**]：表示呼叫保持的模式为单向放音模式，用来表示呼叫保持发起方开启发送媒体通道，关闭接收媒体通道。

**[moh-number** *string*]：播放保持音乐的接入服务号码，为1～31个字符的字符串，取值范围为数字0～9。

【举例】

\# 配置呼叫保持功能采用**sendonly**模式。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice call-hold-format sendonly

**语音业务 \-- 语音业务配置命令 \-- display voice mwi**

------------------------------------------------------------------------

**[display** **voice** **mwi**]命令用来显示消息等待指示功能的配置信息和从语音信箱服务器接收到的订阅信息。

【命令】

**[display**[ **voice** **mwi** { **all** \| **number** *number* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有号码的订阅状态信息。

**[number** *number*]：显示指定号码的订阅状态信息，为1～31个字符的字符串，取值范围为数字0～9和+。

【举例】

\# 显示消息等待指示功能的配置信息和从语音信箱服务器接收到的订阅信息。

\<Sysname\> display voice mwi all

Message Waiting Indication Information:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

MWI type: Solicited

MWI server: 192.168.4.8 port: 5060

MWI expires: 200

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Number: 1515

Messages-Waiting: Yes

Voicemail: 1/3(1/2)

Total: 4(3)

表1-1 display voice mwi命令显示信息描述表

字段

描述

MWI type

消息等待指示的类型：

·Unsolicited：非请求模式

·Solicited：请求模式

MWI server

语音信箱服务器地址，采用IP地址加端口号或域名的方式表示

MWI expires

订阅的老化时长

Number

发起订阅的号码

Messages-Waiting

消息等待标志：

·Yes：语音信箱服务器上有新消息

·No：语音信箱服务器上没有新消息

如上面例子中的Messages-Waiting: Yes，说明当前语音信箱服务器上有号码1515的新消息

Voicemail

消息类型：新消息数/旧消息数（新的紧急消息数/旧的紧急消息数）

如上面例子中的Voicemail: 1/3(1/2)，说明号码1515当前有1个新消息，3个旧消息，1个新的紧急消息，2个旧的紧急消息

Total

普通消息数（紧急消息数）

例如上面例子中的Total: 4(3)，说明号码1515当前共有普通消息4个，紧急消息3个

**语音业务 \-- 语音业务配置命令 \-- display voice sip subscribe-state**

------------------------------------------------------------------------

**[display voice sip subscribe-state**]命令用来显示号码的订阅状态。

【命令】

**[display voice sip subscribe-state**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

只有在使用请求模式的情况下，才能使用该命令查看号码的订阅状态。

【举例】

\# 显示号码的订阅状态。

\<Sysname\> display voice sip subscribe-state

Number                          Server Address             Expires Status

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

2233                            192.168.4.8:5060           146     online

表1-2 display voice sip subscribe-state命令显示信息描述表

字段

描述

Number

使用订阅功能的号码

Server Address

语音信箱服务器地址，采用IP地址加端口号或域名的方式表示

Expires

订阅的老化时长

Status

号码所处的订阅状态：

·Offline：表示订阅失败

·Online：表示订阅成功

·Logging in：表示正在订阅

·Logging out：表示正在取消订阅

**语音业务 \-- 语音业务配置命令 \-- mwi**

------------------------------------------------------------------------

**[mwi**]命令用来开启消息等待指示功能。

**[undo mwi**]命令用来关闭消息等待指示功能。

【命令】

**[mwi**]

**[undo mwi**]

【缺省情况】

消息等待指示功能处于关闭状态。

【视图】

FXS语音用户线视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在语音用户线下配置**mwi**命令后，与该语音用户线绑定的语音实体才有能力去发起订阅。

【举例】

\# 开启消息等待指示功能。

\<Sysname\> system-view

Sysname subscriber-line 2/1/1

Sysname-subscriber-line2/1/1 mwi

**语音业务 \-- 语音业务配置命令 \-- mwi-server**

------------------------------------------------------------------------

**[mwi-server**]命令用来配置语音信箱服务器的信息。

**[undo** **mwi-server**]命令用来取消已配置的语音信箱服务器信息。

【命令】

**[mwi-server**[ { **dns** *domain-name* \| **ip** *ip-address* } [ **port** *port-number* ]  **expires** *seconds*   **transport** { **tcp** [ **tls**  \| **udp** }   **scheme** { **sip** \| **sips** } ]  **unsolicited** ]]

**[undo mwi-server**]

【缺省情况】

没有配置语音信箱服务器的信息。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dns** *domain-name*]：语音信箱服务器的域名，由"."分隔的字符串组成（如aabbcc.com），每个字符串的长度不超过63个字符，包括"."在内的总长度不超过253个字符。不区分大小写，字符串中可以包含字母、数字、"-"及"\_"。

**[ip** *ip-address*]：语音信箱服务器的IP地址。

**[port** *port-number*]：语音信箱服务器的端口号，取值范围为1～65535，如果选择配置IP参数，在MWI功能使用UDP和TCP传输协议的情况下，缺省值为5060，在MWI功能使用TLS传输协议的情况下，缺省值为5061。如果选择配置DNS参数，则必须配置端口号。

**[expires** *seconds*]：订阅的老化时长，取值范围为10～72000，单位为秒，缺省值为3600秒。

**[transport**]：订阅时使用的传输协议。缺省情况下，订阅时使用的UDP传输协议。

**[tcp**]：订阅时使用TCP传输协议，缺省情况下，使用UDP传输协议。如果不选择**tls**参数，表示订阅时使用TCP传输协议。

**[tls**]：订阅时使用TLS传输协议。

**[udp**]：订阅时使用UDP传输协议。

**[scheme**]：订阅时使用的URL方案类型。缺省情况下，使用SIP格式的URL方案。

**[sip**]：订阅时使用SIP格式的URL方案。

**[sips**]：订阅时使用SIPS格式的URL方案。

**[unsolicited**]：非请求模式，表示SIP UA已经通过注册过程与语音信箱服务器建立订阅关系，SIP UA不需要向语音信箱服务器发送SUBSCRIBE消息即可接收到语音信箱服务器发送的NOTIFY消息。缺省情况下为请求模式，表示SIP UA需要通过发起SUBSCRIBE消息来与语音信箱服务器建立订阅关系后，才能够接收到语音信箱服务器发送的NOTIFY消息。

【使用指导】

如果订阅时使用TLS传输协议，那么该命令的目的端口号应该和语音信箱服务器上配置的端口号保持一致。

【举例】

\# 配置语音信箱服务器地址为100.1.1.101，端口号为5060，订阅的老化时长是7200秒。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip mwi-server ip 100.1.1.101 port 5060 expires 7200

