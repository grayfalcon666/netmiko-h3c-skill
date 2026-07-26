
**SIP \-- SIP配置命令 \-- address sip**

------------------------------------------------------------------------

**[address sip**]命令用来配置SIP呼叫路由。

**[undo** **address sip**]命令用来删除已配置的SIP呼叫路由。

【命令】

**[address**[ **sip** { **dns** *domain-name* **port** *port-number* \| **ip** *ip-address* [ **port** *port-number* ] \| **proxy** }]]

**[undo**[ **address** **sip** { **dns** \| **ip** \| **proxy** }]]

【缺省情况】

没有配置SIP呼叫路由。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dns** *domain-name*]：呼叫目的的域名，由"."分隔的字符串组成（如aabbcc.com），每个字符串的长度不超过63个字符，包括"."在内的总长度不超过253个字符。不区分大小写，字符串中可以包含字母、数字、"-"及"\_"。

**[port** *port-number*]：目的端口号，取值范围为1～65535。如果选择配置IP参数，在使用UDP和TCP传输协议发起呼叫的情况下，缺省值为5060。在使用TLS传输协议发起呼叫的情况下，缺省值为5061。如果选择配置DNS参数，则必须配置端口号。

**[ip** *ip-address*]：呼叫目的IP地址。

**[proxy**]：使用SIP代理服务器查找呼叫目的地址。

【举例】

\# 配置VoIP语音实体10，呼叫目的IP地址为3.3.3.3。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 address sip ip 3.3.3.3

**SIP \-- SIP配置命令 \-- asserted-id**

------------------------------------------------------------------------

**[asserted-id**]命令用来配置发送的SIP消息中携带P-Asserted-Identity头域或者P-Preferred-Identity头域。

**[undo asserted-id**]命令用来配置发送的SIP消息中不携带P-Asserted-Identity 头域或者P-Preferred-Identity头域。

【命令】

**[asserted-id **[{ **pai \| ppi** }]]

**[undo asserted-id**]

【缺省情况】

发送的SIP消息中不携带P-Asserted-Identit头域或者P-Preferred-Identity头域。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pai**]：发送的SIP消息中携带P-Asserted-Identit头域。

**[ppi**]：发送的SIP消息中携带P-Preferred-Identity头域。

【举例】

\# 配置发送的SIP消息中携带P-Asserted-Identity头域。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip asserted-id pai

**SIP \-- SIP配置命令 \-- bind**

------------------------------------------------------------------------

**[bind**]命令用来配置全局源接口绑定功能，即发送的SIP信令或媒体流的源地址。

**[undo** **bind**]命令用来删除已有的绑定配置。

【命令】

**[bind**[ { **control \|** **media** } **source-interface** *interface-type* *interface-number* ]]

**[undo**[ **bind** { **control \|** **media** }]]

【缺省情况】

没有配置全局源接口绑定功能。使用路由出接口的IP地址作为设备发送SIP信令或媒体流的源地址。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[control**]：SIP信令。

**[media**]：媒体流。

**[source-interface*** interface-type interface-number*]：设备发送SIP信令或媒体流所使用的源接口，包括接口类型和编号类型，目前只支持三层以太网接口、LoopBack接口和Dialer接口。此接口下的IP地址即为发送媒体流或是SIP信令的源地址。

【使用指导】

表1-1 配置源接口绑定命令的生效情况

状态

源接口绑定功能的生效情况

在通话过程中

·对于媒体流，媒体流的源地址不会随配置立即更新。在下一次创建新的SIP会话后，该绑定才会在相应的媒体流上生效

·对于SIP信令，配置将立即生效

绑定的接口被**shutdown**

源地址绑定功能失效，SIP信令流或媒体流的源地址恢复为缺省情况

绑定接口的IP地址被删除或绑定的接口被删除

被绑定的接口对应的物理层或链路层状态为down

绑定的接口从DHCP服务器动态获得了新的IP地址

使用最新的IP地址作为媒体流或信令流的源地址

正在进行SIP注册

重新发起注册时间超时后，配置才会生效

SIP视图下的**bind**命令为全局命令，当VoIP语音实体下配置源接口绑定时，会使用VoIP语音实体配置，否则使用全局命令配置的源接口绑定，即VoIP语音实体配置优先于全局配置。

如果通过**bind**命令指定的地址不存在或者无效，那么命令行的配置不会生效，设备会使用缺省情况，即使用路由出接口的IP地址作为设备发送SIP信令或媒体流的源地址。

【举例】

\# 配置设备发送SIP信令所使用的源接口为Dialer 0。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip bind control source-interface dialer 0

【相关命令】

·**voice-class sip bind**

**SIP \-- SIP配置命令 \-- crypto**

------------------------------------------------------------------------

**[crypto**]命令用来配置SIP会话使用TLS传输协议时选择的策略名称。

**[undo** **crypto**]命令用来取消相应策略名称的配置。

【命令】

**[crypto**[ { **ssl-client-policy** *client-policy-name* \| **ssl-server-policy** *server-policy-name* }]]

**[undo**[ **crypto** { **server-policy** \| **client-policy** }]]

【缺省情况】

没有配置SIP会话使用的TLS策略名称。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ssl-client-policy***client-policy-name*]：SSL客户端策略名称，为1～31个字符的字符串，不区分大小写。

**[ssl-server-policy***server-policy-name*]：SSL服务器端策略名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

·请先配置TLS传输协议使用的客户端和服务器端的TLS策略，然后通过**transport**命令开启TLS传输协议接收呼叫，否则设备无法接收TLS请求。

·如果要修改绑定的TLS服务器端的策略或是TLS服务器策略的配置信息，需要先使用**transport**命令关闭TLS传输协议的侦听端口。

·如果修改了TLS客户端策略的配置信息或是策略名称，仅对后续新的TLS连接生效，当前已经建立的TLS连接仍然使用原有的策略。

【举例】

\# 配置SIP会话使用TLS传输协议，使用服务器端的策略名称为Server1，使用客户端的策略名称为Server2。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip crypto ssl-server-policy Server1

Sysname-voice-sip crypto ssl-client-policy Server2

【相关命令】

·**transport**

**SIP \-- SIP配置命令 \-- display voice ip address trusted list**

------------------------------------------------------------------------

**[display voice ip address trusted list**]命令用来显示可信节点信息。

【命令】

**[display voice ip address trusted list**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

执行本命令后，将显示可信节点列表中配置的IP地址或地址段，同时，由于实体下SIP呼叫路由中配置的目的地址会被认为是可信的，所以该地址也会显示在可信节点列表中。

【举例】

\# 显示可信节点信息。

\<Sysname\> display voice ip address trusted list

IP address trusted authentication: Enabled

VoIP entity IP addresses:

Entity tag      State    SIP IP address

\-\-\-\-\-\-\-\-\--      \-\-\-\--    \-\-\-\-\-\-\-\-\-\-\-\-\--

20              Up       192.168.4.110

53232           Down     192.168.4.210

55555           Up       192.168.4.210

9613            Up       192.168.4.125

IP address trusted list:

 192.168.4.0 255.255.255.0

 192.168.5.120 255.255.255.255

表1-2 display voice ip address trust list命令显示信息描述表

字段

描述

IP address trusted authentication

可信节点功能状态，包括以下取值：

lEnabled：使能

lDisabled：关闭

VoIP entity IP addresses

VoIP语音实体下的可信地址

Entity tag

实体索引

State

实体状态，取值包括：Up和Down

SIP IP address

实体下SIP呼叫路由中配置的目的地址

IP address trusted list

可信节点列表

【相关命令】

·**address sip**

·**ip**

·**ip address trusted authenticate**

**SIP \-- SIP配置命令 \-- display voice sip call**

------------------------------------------------------------------------

**[display** **voice** **sip** **call**]命令用来显示SIP当前的呼叫信息。

【命令】

**[display** **voice** **sip** **call**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示SIP当前的呼叫信息。

\<Sysname\> display voice sip call

SIP UAC Call Information

Call 1

   Call ID: 2856599de8c8824524de623ac7b1755e@200.1.1.36

   Call status: Connected

   Calling number: 77201

   Called number: 30

   Control block ID: 8

   Local IP address: 200.1.1.36: 5060

   Remote IP address: 200.1.1.30: 5060

Media stream

   Media status: Send and receive

   Negotiated codec: g729r8

   Codec payload type: 18

   Codec payload size: 30

   Codec transparent: Disabled

   Media mode: Flow-through

   Negotiated DTMF-relay: Inband-voice

   Local IP address: 200.1.1.36: 16316

   Remote IP address: 200.1.1.30: 16642

Number of SIP UAC calls: 1

表1-3 display voice sip call命令显示信息描述表

字段

描述

Call *number*

呼叫的编号

Call ID

呼叫ID

State of the call

呼叫状态：

·Originating：正在发起SIP呼叫

·Answering：等待接受SIP呼叫

·Connected：SIP呼叫已经建立

·Releasing：正在结束SIP呼叫

Calling number

主叫号码

Called  number

被叫号码

Control block ID

控制块标识

Local IP address

SIP信令源IP地址和发送数据的端口号

Remote IP address

SIP信令目的IP地址和目的方监听数据的端口号

Media stream

媒体流信息

State of the media

媒体状态：

·Send and receive：双向发送和接收媒体流

·Send only：单向发送媒体流

·Receive only：单向接收媒体流

·Inactive：没有媒体流

·None：没有媒体流方向的记录

Negotiated codec

协商的编解码类型：

g711alaw、g711ulaw 、g723r53、g723r63、g726r16、g726r24、g726r32、g726r40、g729a、g729br8、g729r8

N/A表示编解码协商失败或者不使用编解码

Codec payload type

编解码载荷类型

设备支持标准编号为0～127的编码方式

Codec payload size

编解码打包时长

Codec transparent

SIP Trunk设备的编解码透传功能：

·Enabled：SIP Trunk设备的编解码透传功能处于开启状态

·Disabled：SIP Trunk设备的编解码透传功能处于关闭状态

Media mode

SIP Trunk设备的媒体旁路功能：

·Flow-around：SIP Trunk设备的媒体旁路功能处于开启状态

·Flow-through：SIP Trunk设备的媒体旁路功能处于关闭状态

Negotiated Dtmf-relay

协商的DTMF信号传输方式：

·Inband-voice：带内语音传输

·Outband-SIP：带外SIP传输

·Outband-NTE：带外NTE传输

Source IP address

媒体流源IP地址

Destination IP address

媒体流目的IP地址

Number of SIP UAC calls

设备作为SIP UAC发起的呼叫数量

Number of SIP UAS calls

设备作为SIP UAS接收的呼叫数量

**SIP \-- SIP配置命令 \-- display voice sip connection**

------------------------------------------------------------------------

**[display** **voice** **sip** **connection**]命令用来显示SIP使用的传输层上的连接信息，包括已经建立和正在建立的连接信息。

【命令】

**[display**[ **voice** **sip** **connection** { **tcp** \| **tls** }]]

【视图】

任意视图

【缺省用户级别】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[tcp**]：显示所有的TCP连接的信息。

**[tls**]：显示所有的TLS连接信息。

【举例】

\# 显示所有的TCP连接信息。

\<Sysname\> display voice sip connection tcp

Conn-Id  Local-IP         Local-Port  Remote-IP        Remote-Port      Conn-State

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 569      100.1.1.84       1593       100.1.1.100       5060            Established

 570      100.1.1.84       1594       100.1.1.101       5060            Established

 571      100.1.1.84       1595       100.1.1.81        5060            Established

 572      192.168.0.82     1596       192.168.0.81      5060            Established

\# 显示所有的TLS连接信息。

\<Sysname\> display voice sip connection tls

Conn-Id  Local-IP         Local-Port  Remote-IP        Remote-Port      Conn-State

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 73       192.168.0.202    1086       192.168.0.132     5061            Established

表1-4 display voice sip connection命令显示信息描述表

字段

描述

Conn-Id

连接ID

Local-IP

本地IP地址

Local-Port

本地端口号

Remote-IP

远端IP地址

Reomte-Port

远端端口号

Conn-State

连接状态：

·Connecting表示处于正在连接状态

·Established表示连接已经建立

【相关命令】

·**reset voice sip connection**

**SIP \-- SIP配置命令 \-- display voice sip map**

------------------------------------------------------------------------

**[display** **voice** **sip** **map**]命令用来显示PSTN原因值和SIP状态码的映射关系。

【命令】

**[display voice sip map **[{ **pstn-sip** \| **sip-pstn** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pstn-sip**]：显示PSTN原因值到SIP状态码的映射关系。

**[sip-pstn**]：显示SIP状态码到PSTN原因值的映射关系。

【举例】

\# 显示与PSTN原因值对应的SIP状态码的映射表。

\<Sysname\> display voice sip map pstn-sip

 The PSTN Cause to SIP Status code mapping table:

 Index       PSTN-Cause     SIP-Status     Default

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  1              1            400\*           404

  2              2            400\*           404

  3              3            404            404

  4             16            \-\--            \-\--

  5             17            486            486

  6             18            408            408

  7             19            480            480

  8             20            480            480

  9             21            403            403

 10             22            410            410

 11             23            410            410

 12             25            500            500

 13             26            404            404

 14             27            502            502

 15             28            484            484

 16             29            501            501

 17             31            480            480

 18             34            503            503

 19             38            503            503

 20             41            503            503

 21             42            503            503

 22             47            503            503

 23             55            403            403

 24             57            403            403

 25             58            503            503

 26             63            500            500

 27             65            488            488

 28             70            488            488

 29             79            501            501

 30             87            403            403

 31             88            503            503

 32            102            504            504

 33            111            500            500

 34            127            500            500

表1-5 display voice sip map pstn-sip命令显示信息描述表

字段

描述

The PSTN Cause to SIP Status code mapping table

与PSTN原因值对应的SIP状态码的映射表

Index

索引号

PSTN-Cause

PSTN原因值

SIP-Status

与PSTN原因值对应的SIP状态码（如果取值和缺省值不一样，将加星号显示）

Default

缺省情况下，与PSTN原因值对应的SIP状态码

\# 显示与SIP状态码对应的PSTN原因值的映射表。

\<Sysname\> display voice sip map sip-pstn

 The SIP Status code to PSTN Cause mapping table:

 Index       SIP-Status     PSTN-Cause     Default

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  1            400             41             41

  2            401             21             21

  3            402             21             21

  4            403             21             21

  5            404              1              1

  6            405             63             63

  7            406             79             79

  8            407             21             21

  9            408            102            102

 10            410             22             22

 11            413            127            127

 12            414            127            127

 13            415             79             79

 14            416            127            127

 15            420            127            127

 16            421            127            127

 17            423            127            127

 18            480             18             18

 19            481             41             41

 20            482             25             25

 21            483             25             25

 22            484             28             28

 23            485              1              1

 24            486             17             17

 25            487            127            127

 26            488            127            127

 27            500             41             41

 28            501             79             79

 29            502             38             38

 30            503             41             41

 31            504            102            102

 32            505            127            127

 33            513            127            127

 34            600             17             17

 35            603             21             21

 36            604              1              1

 37            606             58             58

表1-6 display voice sip map sip-pstn命令显示信息描述表

字段

描述

The SIP Status code to PSTN Cause mapping table

与SIP状态码对应的PSTN原因值的映射表

Index

索引号

SIP-Status

SIP状态码

PSTN-Cause

与SIP状态码对应的PSTN原因值（如果取值和缺省值不一样，将加星号显示）

Default

缺省情况下，与SIP状态码对应的PSTN原因值

**SIP \-- SIP配置命令 \-- display voice sip register-status**

------------------------------------------------------------------------

**[display** **voice** **sip** **register-status**]命令用来显示SIP UA和SIP Trunk账户的注册状态信息。

【命令】

**[display** **voice** **sip** **register-status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示注册状态信息。

\<Sysname\> display voice sip register-status

Number                          Entity     Registrar Server      Expires Status

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

98                              98         192.168.4.240:5060    N/A     Offline

1000                            0          192.168.4.240:5060    2877    Online

表1-7 display voice sip register-status命令显示信息描述表

字段

描述

Number

电话号码

Entity

语音实体号，显示语音实体号为0时，表示是使用**credentials**命令进行注册的SIP Trunk账户

Registrar Server

注册服务器地址

Expires

电话号码的注册老化时长，单位为秒

N/A表示电话号码正在注册或是注册失败

Status

表示该号码所处的状态：

·Offline：表示注册失败状态

·Online：表示注册成功状态

·Login：表示正在注册状态

·Logout：表示正在注销状态

·DNS-in：表示注册前进行DNS查询状态

·DNS-out：表示注销前进行DNS查询状态

**SIP \-- SIP配置命令 \-- ip**

------------------------------------------------------------------------

**[ip**]命令用来添加可信节点。

**[undo ip**]命令用来删除可信节点**。**

【命令】

**[ip ***ipv4−address * *mask* ]

**[undo ip*** ipv4−address * *mask* ]

【缺省情况】

没有配置可信节点。

【视图】

可信节点列表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4−address*]：可信节点的IPv4地址。

*[mask*]：子网掩码。不配置此参数，表示32位掩码。

【举例】

\# 配置可信节点为1.1.1.0/24网段的IP地址。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip ip address trusted list

Sysname-voice-sip-iptrust-list ip 1.1.1.0 255.255.255.0

**SIP \-- SIP配置命令 \-- ip address trusted authenticate**

------------------------------------------------------------------------

**[ip address trusted authenticate**]命令用来开启可信节点功能。

**[undo ip address trusted authenticate**]命令用来关闭可信节点功能。

【命令】

**[ip address trusted authenticate**]

**[undo ip address trusted authenticate**]

【缺省情况】

可信节点功能处于关闭状态。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

未开启可信节点功能，所有节点默认为可信，设备接受所有呼叫请求。开启可信节点功能后，只有来自可信节点的呼叫请求才被设备所接受。

如果开启了可信节点功能，建议将代理服务器、注册服务器、DNS服务器、MWI服务器配置为可信节点。

【举例】

\# 开启可信节点功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip ip address trusted authenticate

**SIP \-- SIP配置命令 \-- ip address trusted list**

------------------------------------------------------------------------

**[ip address trusted list**]命令用来进入可信节点视图。

**[undo ip address trusted list**]命令删除可信节点视图。

【命令】

**[ip address trusted list **]

**[undo ip address trusted list**]

【缺省情况】

没有配置可信节点列表。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入可信节点视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip ip address trusted list

Sysname-voice-sip-iptrust-list

**SIP \-- SIP配置命令 \-- ip qos dscp**

------------------------------------------------------------------------

**[ip qos dscp**]命令用来配置承载媒体流或语音信令的IP报文中DSCP值。

**[undo ip qos dscp**]命令用来恢复缺省情况。

【命令】

**[ip qos dscp **[{ *dscp-value \| dscp-value-set* } { **media** \| **signaling** }]]

**[undo ip qos **]**dscp**[{ *dscp-value \| dscp-value-set* }] **[signaling**}

【缺省情况】]

承载媒体流或语音信令的IP报文中DSCP值为**ef**（101110）。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DSCP值，取值范围为0～63。

*[dscp-value-set*]：DSCP值，取值如下：**af11**、**af12**、**af13**、**af21**、**af22**、**af23**、**af31**、**af32**、**af33**、**af41**、**af42**、**af43**、**cs1**、**cs2**、**cs3**、**cs4**、**cs5**、**cs6**、**cs7**或**ef**。

**[media**]：承载媒体流的IP报文中DSCP值。

**[signaling**]：承载语音信令的IP报文中DSCP值。

表1-8 DSCP关键字与值的对应表

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

\# 配置承载语音信令的IP报文中DSCP值为**af41**。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip ip qos dscp af41 signaling

【相关命令】

·**ip qos dscp**（语音命令参考/语音实体）

**SIP \-- SIP配置命令 \-- min-se**

------------------------------------------------------------------------

**[min-se**]命令用来配置SIP会话更新参数。

**[undo min-se**]命令用来恢复缺省情况。

【命令】

**[min-se **]*time* [ **session-expires** *interval* ]

**[undo min-se**]

【缺省情况】

SIP会话的最短持续时间和SIP会话的最长持续时间均为1800秒。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：SIP会话的最短持续时间，取值范围为90～65535，单位为秒。该值不能大于SIP会话的最长持续时间。

*[interval*]：SIP会话的最长持续时间，取值范围为90～65535，单位为秒。不配置该值，表示SIP会话的最长持续时间=SIP会话的最短持续时间。

【使用指导】

·在UAC上配置该命令，表示会话请求消息中携带的Session-Expires头域和Min-se头域的值。

·由于UAS回复的Session-Expires头域值是从接收到的最终会话请求中Session-Expires头域拷贝的，因此在UAS上配置该命令，只有**min-se**参数生效。

【举例】

\# 配置SIP会话的最短持续时间为1000秒，SIP会话的最长持续时间为2000秒。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip min-se 1000 session-expires 2000

【命令参考】

·**session refresh**

**SIP \-- SIP配置命令 \-- options-ping**

------------------------------------------------------------------------

**[options-ping**]命令用来全局开启呼叫内OPTIONS保活探测功能。

**[undo options-ping**]命令用来全局关闭呼叫内OPTIONS保活探测功能。

【命令】

**[options-ping ***seconds*]

**[undo options-ping**]

【缺省情况】

全局呼叫内OPTIONS保活探测功能处于关闭状态。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：全局下发送OPTIONS保活探测报文的时间间隔，取值范围为60～1200，单位为秒。

【使用指导】

呼叫内OPTIONS保活探测功能全局开启后，设备通过VoIP语音实体与对端建立起呼叫。如果会话更新协商失败，设备会按照配置的时间间隔给远端发送OPTIONS探测报文以维持呼叫连接。

关闭呼叫内OPTIONS保活探测功能的情况下，呼叫建立后，设备不会发送OPTIONS探测报文。

【举例】

\# 在SIP视图下开启呼叫内OPTIONS保活探测功能，保活探测报文的时间间隔设置为60秒。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip options-ping 60

【相关命令】

·**voice-class sip options-ping**

**SIP \-- SIP配置命令 \-- outband sip**

------------------------------------------------------------------------

**[outband sip**]命令用来配置使用SIP带外方式传输DTMF信号。

**[undo** **outband**]命令用来恢复缺省情况。

【命令】

**[outband sip**]

**[undo** **outband**]

【缺省情况】

使用带内方式传输DTMF信号。

【视图】

POTS/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

建议配置该方式时，在主被叫设备上同时开启**outband** **sip**命令。

【举例】

\# 配置使用SIP带外方式传输DTMF信号。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 outband sip

**SIP \-- SIP配置命令 \-- privacy**

------------------------------------------------------------------------

**[privacy**]命令用来配置发送的SIP消息中携带Privacy头域。

**[undo privacy**]命令用来配置发送的SIP消息中不携带Privacy头域。

【命令】

**[privacy**]

**[undo privacy**]

【缺省情况】

发送的SIP消息中不携带Privacy头域。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置发送的INVITE消息中携带Privacy头域。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip privacy

**SIP \-- SIP配置命令 \-- proxy**

------------------------------------------------------------------------

**[proxy**]命令用来配置SIP UA使用的代理服务器信息。

**[undo**] **proxy**命令用来删除SIP UA使用的代理服务器信息。

【命令】

**[proxy**[ { **dns** *domain-name* **port** *port-number* \| **ip** *ip-address* [ **port** *port-number* ] }]]

**[undo**[ **proxy** { **dns** \| **ip** }]]

【缺省情况】

没有配置SIP UA使用的代理服务器信息。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dns** *domain-name*]：代理服务器的域名，由"."分隔的字符串组成（如aabbcc.com），每个字符串的长度不超过63个字符，包括"."在内的总长度不超过253个字符。不区分大小写，字符串中可以包含字母、数字、"-"及"\_"。

**[ip*** ip-address*]：代理服务器的IPv4地址。

**[port** *port-number*]：代理服务器的端口号，取值范围为1～65535。如果选择配置IP参数，缺省值为5060。如果选择配置DNS参数，则必须配置端口号。

【举例】

\# 配置SIP UA使用的代理服务器地址为169.54.5.10，端口号为1120。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip proxy ip 169.54.5.10 port 1120

\# 配置SIP UA使用的代理服务器地址为abc.com，端口号为1100。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip proxy dns abc.com port 1100

**SIP \-- SIP配置命令 \-- register-number**

------------------------------------------------------------------------

**[register-number**]命令用来配置语音实体向注册服务器发起注册。

**[undo** **register-number**]命令用来配置语音实体向注册服务器发起注销。

【命令】

**[register-number**]

**[undo** **register-number**]

【缺省情况】

完成SIP注册的相关配置后，POTS语音实体会向注册服务器发起注册。

【视图】

POTS语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

由于在注册服务器上不能存在相同的号码，因此如果在设备上有多个语音实体下配置相同的号码，那么只有一个号码能注册到注册服务器上。

【举例】

\# 配置POTS语音实体10向注册服务器发起注销。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 pots

Sysname-voice-dial-entity10 match-template 1000

Sysname-voice-dial-entity10 line 2/1/1

Sysname-voice-dial-entity10 undo register-number

【相关命令】

·**match-template**

**SIP \-- SIP配置命令 \-- registrar**

------------------------------------------------------------------------

**[registrar**]命令用来配置SIP UA使用的注册服务器信息。

**[undo** **registrar**]命令用来删除指定注册服务器信息，并通知注册服务器注销SIP UA的号码信息。

【命令】

**[registrar**[ *registrar-index* { **dns** *domain-name* **port** *port-number* \| **ip** *ip-address* [ **port** *port-number* ] }  **expires** *seconds*   **refresh-ratio** *ratio-percentage*  [ **scheme** { **sip** \| **sips** } ]  **tcp** [ **tls**  ]]]

**[undo registrar ***registrar-index*]

【缺省情况】

没有配置SIP UA使用的注册服务器信息。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[registrar-index*]：注册服务器索引，取值范围为1～6。

**[dns** *domain-name*]：设置注册服务器的域名，由"."分隔的字符串组成（如aabbcc.com），每个字符串的长度不超过63个字符，包括"."在内的总长度不超过253个字符。不区分大小写，字符串中可以包含字母、数字、"-"及"\_"。

**[ip** *ip-address*]：注册服务器的IP地址。

**[port*** port-number*]：注册服务器的端口号，取值范围为1～65535。如果选择配置IP参数，在注册使用UDP和TCP传输协议的情况下，缺省值为5060，在注册使用TLS传输协议的情况下，缺省值为5061。如果选择配置DNS参数，则必须配置端口号。

**[expires*** seconds*]：注册老化时长，取值范围为60～65535，单位为秒。缺省情况下，注册老化时长为3600秒。

**[refresh-ratio** *ratio-percentage*]：注册老化时长的百分比，取值范围为50～100。缺省情况下，注册老化时长的百分比为80。

**[tcp**]：注册时使用TCP传输协议，缺省情况下，使用UDP传输协议。如果不选择**tls**参数，表示注册时使用TCP传输协议。

**[tls**]：注册时使用TLS传输协议。

**[scheme**]：注册时使用的URL类型。

**[sip**]：注册时使用SIP格式的URL类型，缺省情况下，使用SIP格式的URL类型。

**[sips**]：注册时使用SIPS格式的URL类型。

【使用指导】

·完成SIP UA上的号码或是SIP Trunk账户配置后，还需要使用**registrar**命令指定注册服务器信息。

·如果注册时使用TLS传输协议，那么该命令的目的端口号应该和注册服务器上配置的端口号保持一致。

【举例】

\# 配置注册服务器信息。设置索引号为1的注册服务器的IP地址为169.54.5.10，端口号为1120，注册老化时长为120秒。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip registrar 1 ip 169.54.5.10 port 1120 expires 120

\# 配置注册服务器信息。设置索引号为2的注册服务器的域名为cc.news.com，端口号为1100，注册老化时长为520秒。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip registrar 2 dns cc.news.com port 1100 expires 520

【相关命令】

·**credentials**

·**display** **voice** **sip** **register-status**

·**transport**

**SIP \-- SIP配置命令 \-- rel1xx**

------------------------------------------------------------------------

**[rel1xx**]命令用来配置SIP可靠临时响应。

**[undo rel1xx**]命令用来恢复缺省情况。

【命令】

**[rel1xx **[{ **disable** \| **require** *value* \| **supported** *value* }]]

**[undo** **rel1xx**]

【缺省情况】

发送的SIP消息中携带Supported: *value*头域，即命令行**rel1xx supported 100rel**生效。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disable**]：不支持可靠临时响应。

**[require ***value*]：发送的SIP消息中携带Require: *value*头域，取值范围为1～49，区分大小写。

**[supported ***value*]：发送的SIP消息中携带Supported: *value*头域，取值范围为1～49，区分大小写。

【使用指导】

如果需要使用SIP可靠临时响应，建议在UAC和UAS上配置该功能处于非关闭状态，且头域中的*value*值保持一致。

【举例】

\# 配置发送的SIP消息中携带Require: 100rel头域。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip rel1xx require 100rel

**SIP \-- SIP配置命令 \-- remote-party-id**

------------------------------------------------------------------------

**[remote-party-id**]命令用来配置发送的INVITE消息中携带Remote-Party-Id头域。

**[undo remote-party-id**]命令用来配置发送的INVITE消息中不携带Remote-Party-Id头域。

【命令】

**[remote-party-id**]

**[undo remote-party-id**]

【缺省情况】

发送的INVITE消息中携带Remote-Party-ID头域。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置发送的INVITE中携带Remote-Party-ID头域。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip remote-party-id

**SIP \-- SIP配置命令 \-- reset voice sip connection**

------------------------------------------------------------------------

**[reset** **voice** **sip** **connection**]命令用来删除SIP使用的传输层上的连接，包括已经建立和正在建立的连接信息。

【命令】

**[reset**[ **voice** **sip** **connection** { **tcp** \| **tls** } **id** *conn-id*]]

【视图】

用户视图

【缺省用户级别】

network-admin

mdc-admin

【参数】

**[tcp**]：删除TCP连接。

**[tls**]：删除TLS连接。

*[conn-id*]：连接ID值，可以通过**display** **voice** **sip** **connection**来确定*conn-id*字段值，取值范围为0～1499。

【举例】

\# 删除连接ID为1的TCP连接。

\<Sysname\> reset voice sip connection tcp id 1

【命令参考】

·**display voice sip connection**

**SIP \-- SIP配置命令 \-- session refresh**

------------------------------------------------------------------------

**[session refresh**]命令用来全局开启会话更新功能。

**[undo session refresh**]命令用来全局关闭会话更新功能。

【命令】

**[session refresh**]

**[undo session refresh**]

【缺省情况】

设备作为UAC，不主动启用初始会话更新。设备作为UAS，支持会话更新功能。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在UAC上配置该命令。

【举例】

\# 全局开启会话更新功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip session refresh

【命令参考】

·**min-se**

**SIP \-- SIP配置命令 \-- session transport**

------------------------------------------------------------------------

**[session transport**]命令用来配置发起SIP呼叫时使用的传输协议类型。

**[undo session transport**]命令用来恢复缺省情况。

【命令】

**[session transport **]{ **tcp** [ **tls**  \| **udp** }]

**[undo session transport**]

【缺省情况】

全局传输协议类型为UDP协议。VoIP语音实体下没有缺省传输协议类型。如果该语音实体下没有配置传输协议，那么该VoIP语音实体的缺省情况与全局传输协议相同。

【视图】

SIP视图/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[udp**]：发起呼叫时，使用UDP传输协议。

**[tcp**]：发起呼叫时，使用TCP传输协议。

**[tls**]：发起呼叫时，使用TLS传输协议。

【使用指导】

SIP视图下的**session transport**命令表示的是全局使用的传输协议类型，如果用户需要针对某一个呼叫采用其它的传输协议时，可以在对应的VoIP语音实体视图下配置相应的传输协议类型。当VoIP语音实体视图下配置的传输协议类型与SIP视图下的**session transport**命令配置的传输协议类型不一致时，则使用该VoIP语音实体下的配置，即VoIP语音实体配置优先于全局配置。

需要注意的是：

·发送方和接收方必须配置相同的传输协议类型，如在发送方配置**session transport** **tcp**，那么在接收方需要配置**transport** **tcp**。

·如果使用TLS传输协议发起SIP呼叫，需要通过**crypto**命令完成客户端或服务器的SSL策略的配置，否则设备无法发起会话请求。

【举例】

\# 配置SIP呼叫采用TLS传输协议。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip session transport tcp tls

【相关命令】

·**crypto**

·**transport**

**SIP \-- SIP配置命令 \-- set pstn-cause**

------------------------------------------------------------------------

**[set pstn-cause**]命令用来配置与PSTN原因值对应的SIP状态码**。**

**[undo** **set pstn-cause**]命令用来恢复缺省情况。

【命令】

**[set** **pstn-cause** *pstn-cause* **sip-status** *sip-status*]

**[undo** **set** **pstn-cause** *pstn-cause*]

【缺省情况】

PSTN原因值和SIP状态码的对应关系请参见表 1-9(#_0_17903_12401_1141177252)。

表1-9 PSTN原因值和SIP状态码的缺省对应关系

PSTN原因值

PSTN原因值描述

SIP状态码

SIP状态码描述

1

Unallocated (unassigned) number!

404

Not Found

2

No route to specified transit network!

404

Not Found

3

No route to destination!

404

Not Found

16

Normal clearing!

\-\--

BYE or CANCEL

17

User busy!

486

Busy here

18

No user responding!

408

Request Timeout

19

No answer from user!

480

Temporarily unavailable

20

Subscriber absent!

480

Temporarily unavailable

21

Call rejected!

403

Forbidden

22

Number changed!

410

Gone

23

Redirection to new destination!

410

Gone

25

Exchange routing error!

500

Server internal error

26

Non-selected user clearing!

404

Not Found

27

Destination out of order!

502

Bad Gateway

28

Invalid number format (address incomplete)!

484

Address incomplete

29

Facility rejected!

501

Not implemented

31

Normal, unspecified!

480

Temporarily unavailable

34

No circuit/channel available!

503

Service unavailable

38

Network out of order!

503

Service unavailable

41

Temporary failure!

503

Service unavailable

42

Switching equipment congestion!

503

Service unavailable

47

Resource unavailable, unspecified!

503

Service unavailable

55

Incoming class barred within Closed User Group (CUG)!

403

Forbidden

57

Bearer capability not authorized!

403

Forbidden

58

Bearer capability not presently available!

503

Service unavailable

63

Service or option not available, unspecified!

500

Server internal error

65

Bearer capability not implemented!

488

Not Acceptable Here

70

Only restricted digital information bearer capability is available!

488

Not Acceptable Here

79

Service or option not implemented, unspecified!

501

Not implemented

87

User not member of Closed User Group (CUG)!

403

Forbidden

88

Incompatible destination!

503

Service unavailable

102

Recovery on timer expiry!

504

Gateway timeout

111

Protocol error, unspecified!

500

Server internal error

127

Interworking, unspecified!

500

Server internal error

****

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pstn-code*]：PSTN原因值。取值范围为表 1-9(#_0_17903_12401_1141177252)中的PSTN原因值，其中的PSTN原因值16为无效取值。

*[sip-code*]：SIP状态码。取值范围为表 1-9(#_0_17903_12401_1141177252)中的SIP状态码。

【举例】

\# 配置与PSTN原因值17对应的SIP状态码为408。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip set pstn-cause 17 sip-status 408

**SIP \-- SIP配置命令 \-- set sip-status**

------------------------------------------------------------------------

**[set** **sip-status**]命令用来配置与SIP状态码对应的PSTN原因值**。**

**[undo** **set** **sip-status**]命令用来恢复缺省情况。

【命令】

**[set** **sip-status** *sip-status* **pstn-cause** *pstn-cause*]

**[undo** **set** **sip-status** *sip-status*]

【缺省情况】

SIP状态码和PSTN原因值的对应关系参见表 1-10(?-378992963#_Ref165367589)。

表1-10 SIP状态码和PSTN原因值的缺省对应关系

SIP状态码

SIP状态码描述

PSTN原因值

PSTN原因值描述

400

Bad Request

41

Temporary failure!

401

Unauthorized

21

Call rejected!

402

Payment required

21

Call rejected!

403

Forbidden

21

Call rejected!

404

Not found

1

Unallocated (unassigned) number!

405

Method not allowed

63

Service or option not available, unspecified!

406

Not acceptable

79

Service or option not implemented, unspecified!

407

Proxy authentication required

21

Call rejected!

408

Request timeout

102

Recovery on timer expiry!

410

Gone

22

Number changed!

413

Request Entity too long

127

Interworking, unspecified!

414

Request-URI too long

127

Interworking, unspecified!

415

Unsupported media type

79

Service or option not implemented, unspecified!

416

Unsupported URI Scheme

127

Interworking, unspecified!

420

Bad extension

127

Interworking, unspecified!

421

Extension Required

127

Interworking, unspecified!

423

Interval Too Brief

127

Interworking, unspecified!

480

Temporarily unavailable

18

No user responding!

481

Call/Transaction Does not Exist

41

Temporary failure!

482

Loop Detected

25

Exchange routing error!

483

Too many hops

25

Exchange routing error!

484

Address incomplete

28

Invalid number format (address incomplete)!

485

Ambiguous

1

Unallocated (unassigned) number!

486

Busy here

17

User busy!

487

Request Terminated

127

Interworking, unspecified!

488

Not Acceptable here

127

Interworking, unspecified!

500

Server internal error

41

Temporary failure!

501

Not implemented

79

Service or option not implemented, unspecified!

502

Bad gateway

38

Network out of order!

503

Service unavailable

41

Temporary failure!

504

Server time-out

102

Recovery on timer expiry!

505

Version Not Supported

127

Interworking, unspecified!

513

Message Too Large

127

Interworking, unspecified!

600

Busy everywhere

17

User busy!

603

Decline

21

Call rejected!

604

Does not exist anywhere

1

Unallocated (unassigned) number!

606

Not acceptable

58

Bearer capability not presently available!

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[sip-code*]：SIP状态码。取值范围为表 1-10(?-378992963#_Ref165367589)中的SIP状态码。

*[pstn-code*]：PSTN原因值。取值范围为表 1-10(?-378992963#_Ref165367589)中的PSTN原因值。

【举例】

\# 配置与SIP状态码486对应的PSTN原因值为18。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip set sip-status 486 pstn-cause 18

**SIP \-- SIP配置命令 \-- signaling forward rawmsg**

------------------------------------------------------------------------

**[signaling forward rawmsg**]命令用来开启SIP消息中携带QSIG信令功能。

**[undo signaling forward**]命令用来恢复缺省情况。

【命令】

**[signaling forward rawmsg**]

**[undo signaling forward**]

【缺省情况】

SIP消息中不携带QSIG信令。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rawmsg**]：发送的SIP消息中可以携带QSIG信令。在SIP报文中携带的Content-type类型为application/qsig，消息体为从ISDN侧收到的QSIG信令。

【使用指导】

当ISDN网络使用重叠发号时，设备不支持该功能。

【举例】

\# 开启SIP消息中携带QSIG信令功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 signaling forward rawmsg

**SIP \-- SIP配置命令 \-- sip**

------------------------------------------------------------------------

**[sip**]命令用来进入SIP视图。

**[undo sip**]命令用来删除SIP视图下的配置。

【命令】

**[sip**]

**[undo sip**]

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入SIP视图。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip

**SIP \-- SIP配置命令 \-- srtp**

------------------------------------------------------------------------

**[srtp**]命令用来配置SIP呼叫使用SRTP协议。

**[undo srtp**]命令用来恢复缺省情况。

【命令】

**[srtp **] **fallback**

**[undo srtp**]

【缺省情况】

全局SIP呼叫使用的媒体流协议为RTP协议。VoIP语音实体下没有缺省的媒体流协议。如果该语音实体下没有配置媒体流协议，那么该VoIP语音实体的缺省情况与全局媒体流协议相同。

【视图】

SIP视图/VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fallback**]：SIP呼叫使用SRTP协议，当对端不支持SRTP协议的情况下，支持回退使用RTP协议。

【使用指导】

设备作为呼叫发起方：

·配置**srtp**命令，表示设备在发起呼叫时，INVITE消息中携带crypto和RTP/SAVP参数，如果收到对方的488应答，则会释放呼叫。

·配置**srtp fallback**命令，表示设备在发起呼叫时，INVITE消息中携带crypto和RTP/SAVP参数，如果收到对方的488应答，会重新发送携带RTP/AVP参数的INVITE消息。

设备作为呼叫接收方，会收到的INVITE消息中不支持的m字段参数置为0：

·配置**srtp**命令，表示设备只能接收使用SRTP协议的呼叫。

·配置**srtp fallback**命令，表示设备会优先使用SRTP协议进行媒体流协商，若协商失败，则使用RTP协议。

SIP视图下的**srtp**命令为全局命令，当VoIP语音实体下配置了媒体流协议时，则使用VoIP语音实体配置，否则使用SIP视图下的**srtp**命令的配置，即VoIP语音实体配置优先于全局配置。

【举例】

\# 配置SIP呼叫使用SRTP协议。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip srtp

**SIP \-- SIP配置命令 \-- timers connection aging**

------------------------------------------------------------------------

**[timers** **connection** **aging**]命令用来配置TCP和TLS连接的老化时间。

**[undo** **timers** **connection** **aging**]命令用来缺省情况。

【命令】

**[timers**[ **connection** **aging** { **tcp** *tcp-age-time* \| **tls** *tls-age-time* }]]

**[undo**[ **timers** **connection** **aging** { **tcp** \| **tls** }]]

【缺省情况】

TCP连接的老化时间为5分钟，TLS连接的老化时间为30分钟。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tcp***tcp-age-time*]：TCP连接的老化时间，TCP连接的老化时间是指建立的TCP连接处于空闲状态的时间，老化时间过后，会删除已建立的TCP连接。取值范围为5～30，单位为分钟。

**[tls***tls-age-time*]：TLS连接的老化时间，TLS连接的老化时间是指建立的TLS连接处于空闲状态的时间，老化时间过后，会删除已建立的TLS连接。取值范围为30～180，单位为分钟。

【举例】

\# 配置TCP连接老化时间为6分钟，TLS连接的老化时间为60分钟。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip timers connection aging tcp 6

Sysname-voice-sip timers connection aging tls 60

**SIP \-- SIP配置命令 \-- timers options**

------------------------------------------------------------------------

**[timers options**]命令用来配置在开启呼叫外OPTIONS保活探测功能后，在重复探测期间，发送OPTIONS报文的时间间隔。

**[undo timers options**]命令用来恢复缺省情况。

【命令】

**[timers options ***value*]

**[undo** **timers options**]

【缺省情况】

发送OPTIONS报文的时间间隔为500毫秒。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：发送OPTIONS报文的时间间隔，取值范围为100～1000，单位为毫秒。

【使用指导】

只有使用**voice-class sip options-keepalive**命令开启呼叫外OPTIONS保活探测功能后，该配置才能生效。关于该命令作用范围的详细说明请参见"1.1.37  (?314585580#_Ref404342067)voice-class sip options-keepalive(?314585580#_Ref404342083)"中的使用指导。

【举例】

\# 配置在开启呼叫外OPTIONS保活探测功能后，在重复探测期间，发送OPTIONS报文的时间间隔。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip timers options 600

【相关命令】

·**voice-class sip options-keepalive**

**SIP \-- SIP配置命令 \-- transport**

------------------------------------------------------------------------

**[transport**]命令用来开启传输协议的侦听端口。

**[undo** **transport**]命令用来关闭传输协议的侦听端口。

【命令】

**[transport**] { **tcp** [ **tls**  \| **udp** }]

**[undo transport**] { **tcp** [ **tls**  \| **udp** }]

【缺省情况】

UDP和TCP传输协议侦听端口处于开启状态，TLS协议侦听端口处于关闭状态。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[udp**]：表示开启UDP侦听端口，侦听的端口号为5060。

**[tcp**]：表示开启TCP侦听端口，侦听的端口号为5060。

**[tls**]：表示开启TLS侦听端口，侦听的端口号为5061。

【使用指导】

可以通过多次执行该命令来开启多个传输协议的侦听端。三种传输协议互不影响。

在下列情况下需要配置该命令：

·设备作为呼叫接收方，在接收使用某种传输协议的呼叫时，需要开启相应传输协议的侦听端口。

·使用**registrar**命令配置选用TCP/TLS协议向注册服务器发起注册时，必须通过**transport**命令开启相应传输协议侦听端口，否则设备无法发起注册请求。

·使用**mwi**命令配置选用TCP/TLS协议向语音信箱服务器发起订阅时，必须通过**transport**命令开启相应传输协议侦听端口，否则设备无法发起订阅请求。

需要注意的是：

·开启TLS侦听端口之前，必须已经使用**crypto**命令配置了TLS的客户端或服务器端的SSL策略，否则无法成功配置开启TLS侦听端口的命令。

·执行**undo** **transport**命令会删除当前已经建立的连接。

【举例】

\# 配置接收SIP呼叫时使用的传输协议为TLS。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip transport tcp tls

【相关命令】

·**crypto**

·**mwi**（语音命令参考/语音业务）

·**registrar**

**SIP \-- SIP配置命令 \-- url**

------------------------------------------------------------------------

**[url**]命令配置SIP呼叫时使用的URL类型。

**[undo url**]命令用来恢复缺省情况。

【命令】

**[url**  { **sip** \| **sips** }]

**[undo url**]

【缺省情况】

使用SIP格式的URL类型。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sip**]：指定在SIP呼叫时使用SIP格式的URL类型。

**[sips**]：指定在SIP呼叫时使用SIPS格式的URL类型。

【使用指导】

SIP视图下的**url**命令为全局命令，当VoIP语音实体下通过**voice-class sip url**命令配置了URL类型时，会使用VoIP语音实体配置，否则使用全局命令配置的URL类型，即VoIP语音实体配置优先于全局配置。

【举例】

\# 配置SIP呼叫使用SIPS格式的URL类型。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip url sips

【相关命令】

·**voice-class sip url**

**SIP \-- SIP配置命令 \-- user**

------------------------------------------------------------------------

**[user**]命令用来配置鉴权信息。

**[undo**] **user**命令用来恢复缺省情况。

【命令】

**[user**[ *username* **password** { **cipher** \| **simple** } *password* [ **realm** *realm* ] ]]

**[undo**[ **user** [ *username* **password** { **cipher** \| **simple** } *password* [ **realm** *realm* ] ]]]

【缺省情况】

没有SIP鉴权信息。

【视图】

SIP视图/POTS语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：鉴权时使用的用户名，为1～63个字符的字符串，区分大小写。

**[cipher**]：以密文方式设置用户的密码。

**[simple**]：以明文方式设置用户的密码。

*[password*]：鉴权使用的明文密码或密文密码，区分大小写。明文密码的长度范围是1～16；密文密码的长度范围是1～53。

**[realm*** realm*]：域名，用于注册服务器和SIP UA之间的握手验证，为1～50个字符的字符串，区分大小写。不配置此参数，表示该鉴权信息可以用于回复任何注册服务器的鉴权请求。

【使用指导】

SIP UA上的号码最多可以向6个注册服务器发起注册，为了区分发送给不同注册服务器的带鉴权信息的注册请求，SIP UA需要根据注册服务器回复的401/407响应消息中的域名参数来匹配配置的鉴权信息。

在设备上，对于设置鉴权信息的**user**命令，无论是语音实体或是SIP视图下，只能配置一个*username*，该*username*可以组合12个不同的域名（命令行中的参数为*realm*），如果没有配置域名，表示该鉴权信息可以用于回复任何注册服务器的鉴权请求，如：

Sysname-voice-dial-entity100 user 1000 password simple 1000 realm server1

Sysname-voice-dial-entity100 user 1000 password simple 1000 realm server2

Sysname-voice-dial-entity100 user 1000 password simple 2000 realm server3

Sysname-voice-dial-entity100 user 1000 password simple 3000

假设SIP UA收到注册服务器回复的401/407响应消息中携带的域名是server2，那么SIP UA使用鉴权信息为用户名1000，密码1000。如果SIP UA收到注册服务器回复的401/407响应消息中携带的域名是server4，SIP UA上没有能和其精确匹配的鉴权信息，在这种情况下，就使用不带域名的鉴权信息，即用户名1000，密码3000。

【举例】

\# 配置全局SIP鉴权信息，用户名为abcd，以明文方式设置密码为1234。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip user abcd password simple 1234

\# 在POTS语音实体下配置SIP鉴权信息，用户名为abcd，以明文方式设置密码为1234，域名为abc。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 100 pots

Sysname-voice-dial-entity100 user abcd password simple 1234 realm abc

【命令参考】

·**registrar**

**SIP \-- SIP配置命令 \-- voice-class sip bind**

------------------------------------------------------------------------

**[voice-class sip bind**]命令用来配置源地址绑定功能，即发送的SIP信令或媒体流的源地址。

**[undo voice-class sip bind**]命令用来删除已有的绑定配置。

【命令】

**[voice-class sip bind **[{ **control** \| **media** } **source-interface** *interface-type interface-number*]]

**[undo voice-class sip bind**[ { **control** \| **media** }]]

【缺省情况】

VoIP语音实体下没有配置源地址绑定功能。如果该语音实体下没有配置源地址绑定，那么该VoIP语音实体的缺省情况与全局源地址绑定的配置情况相同。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[control**]：SIP信令。

**[media**]：媒体流。

**[source-interface*** interface-type interface-number*]：设备发送SIP信令或媒体流所使用的源接口，包括接口类型和编号类型，目前只支持三层以太网接口和Dialer接口。此接口下的IP地址即为发送媒体流或是SIP信令的源地址。

【使用指导】

关于源地址绑定命令的生效情况请参见"1.1.3  (?835817746#_Ref365364515)bind(?835817746#_Ref365364528)"中的使用指导。

SIP视图下的**bind**命令为全局命令，当VoIP语音实体下配置源地址绑定时，会使用VoIP语音实体配置，否则使用全局命令配置的源地址绑定，即VoIP语音实体配置优先于全局配置。

【举例】

\# 配置设备发送SIP信令所使用的源接口为Dialer 0。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 voice-class sip bind control source-interface dialer 0

【相关命令】

·**bind**

**SIP \-- SIP配置命令 \-- voice-class sip options-keepalive**

------------------------------------------------------------------------

**[voice-class sip options-keepalive**]命令用来开启呼叫外OPTIONS保活探测功能，并配置保活报文的时间间隔。

**[undo voice-class sip options-keepalive**]命令用来关闭呼叫外OPTIONS保活探测功能。

【命令】

**[voice-class sip options-keepalive** [ **up-interval** *seconds*   **down-interval** *seconds*   **retry** *retries* ]]

**[undo voice-class sip options-keepalive**]

【缺省情况】

呼叫外OPTIONS保活探测功能处于关闭状态。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[up-interval ***seconds*]：在标记语音实体为不可用前，本端发送OPTIONS报文的时间间隔。取值范围为5～1200。单位为秒，缺省值为60。该参数在语音实体状态为可用时生效。

**[down-interval ***seconds*]：在标记语音实体为可用前，本端发送OPTIONS报文的时间间隔。取值范围为5～1200。单位为秒，缺省值为30。该参数在语音实体状态为不可用时生效。

**[retry ***retries*]：在改变语音实体状态前，重复探测的次数。取值范围为1～10，缺省值为5。

【使用指导】

开启保活探测功能后，本端会按配置的**up-interval**参数定时发送OPTIONS报文，如果本端设备在**up-interval**时间内收到对端应答报文，则表示该VoIP语音实体可用，本端继续使用**up-interval**参数定时发送OPTIONS报文；如果本端在**up-interval**时间内没有收到应答报文或是收到的应答报文为408、499以及5XX（500、501、502、503、504、513除外），会开始重复探测，每次探测的时间间隔由**timers options**命令控制，在完成重复探测后，若还未收到表示语音实体可用的应答报文，则表示该VoIP语音实体不可用。

如果语音实体被判定为不可用，则本端会按配置的**down-interval**参数定时发送OPTIONS报文，如果收到表示语音实体可用的应答报文，会开始重复探测，每次探测的时间间隔由**timers options**命令控制，在重复探测期间，本端每次都能收到对端应答报文，则将该VoIP语音实体的状态恢复为可用。如果一直没有收到表示语音实体可用的应答报文，则本端继续按配置的**down-interval**参数定时发送OPTIONS报文。

需要注意的是，对已经被**shutdown**的VoIP语音实体，保活探测功能不生效。

【举例】

\# 开启呼叫外OPTIONS保活探测功能，配置**up-interval**为50秒，**down-interval**为20秒，**retry**为2次。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 10 voip

Sysname-voice-dial-entity10 voice-class sip options-keepalive up-interval 50 down-interval 20 retry 2

【相关命令】

·**timers options**

**SIP \-- SIP配置命令 \-- voice-class sip options-ping**

------------------------------------------------------------------------

**[voice-class sip options-ping**]命令用来在VoIP语音实体下开启呼叫内OPTIONS保活探测功能。

**[undo voice-class sip options-ping**]命令用来在VoIP语音实体下关闭呼叫内OPTIONS保活探测功能。

【命令】

**[voice-class sip options-ping **[{ **global** \| *seconds* }]]

**[undo voice-class sip options-ping**]

【缺省情况】

VoIP语音实体下呼叫内OPTIONS保活探测使用全局配置。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[global**]：该VoIP语音实体下呼叫内OPTIONS保活探测使用全局配置。

*[seconds*]：VoIP语音实体下发送OPTIONS保活探测报文的时间间隔，取值范围为60～1200，单位为秒。

【使用指导】

如果配置了VoIP语音实体下发送OPTIONS保活探测报文的时间间隔，则无论全局是否开启，通过该VoIP语音实体的出呼叫建立完成后，设备都会根据配置的时间间隔给此VoIP语音实体对应的远端设备发OPTIONS保活报文。

如果关闭了VoIP语音实体下呼叫内OPTIONS保活探测功能，则无论全局是否开启，通过该VoIP语音实体的出呼叫都不会发送OPTIONS报文进行保活探测。

VoIP语音实体下呼叫内OPTIONS保活探测功能使用全局配置的情况下，如果全局开启了呼叫内OPTIONS保活探测功能，则通过该VoIP语音实体的出呼叫建立完成后，设备会根据全局配置的时间间隔发OPTIONS保活报文给该VoIP语音实体对应的远端设备，如果全局未开启，则VoIP语音实体下不会发送OPTIONS保活探测报文。

【举例】

\# 配置VoIP语音实体1，开启呼叫内OPTIONS保活探测功能，发送的保活报文的时间间隔设置为60秒。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 voice-class sip options-ping 60

\# 配置VoIP语音实体1，使呼叫内OPTIONS保活探测功能使用全局配置。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 voice-class sip options-ping global

【相关命令】

·**options-ping**

**SIP \-- SIP配置命令 \-- voice-class sip session refresh**

------------------------------------------------------------------------

**[voice-class sip session refresh**]命令用来在VoIP语音实体下开启会话更新功能。

**[undo voice-class sip session refresh**]命令用来在VoIP语音实体下关闭会话更新功能。

【命令】

**[voice-class sip session refresh ** **global** ]

**[undo voice-class sip session refresh**]

【缺省情况】

VoIP语音实体下会话更新功能开启状态与全局开启状态保持一致。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[global**]：VoIP语音实体下会话更新使用全局配置。

【使用指导】

手工开启VoIP语音实体下会话更新功能（即不指定**global**关键字），无论全局是否开启，通过该VoIP语音实体的出呼叫建立完成后，设备都会定时给该VoIP语音实体对应的远端设备发UPDATE或INVITE探测报文。

VoIP语音实体下会话更新功能使用全局配置的情况下（即指定**global**关键字），如果全局开启了会话更新，则通过该VoIP语音实体的出呼叫建立后具有会话更新功能，如果全局未开启，则不具有会话更新功能。

关闭VoIP语音实体下会话更新功能后，无论全局是否开启会话更新功能，通过该VoIP语音实体的出呼叫建立后不具有会话更新功能，不发UPDATE或INVITE报文进行会话更新。

【举例】

\# 配置VoIP语音实体1，开启会话更新功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 voice-class sip session refresh

\# 配置VoIP语音实体1，会话更新功能使用全局配置。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 voice-class sip session refresh global

【相关命令】

·**min-se**

·**session refresh**

**SIP \-- SIP配置命令 \-- voice-class sip url**

------------------------------------------------------------------------

**[voice-class sip url**]命令配置SIP呼叫时使用的URL类型。

**[undo voice-class sip** **url**]命令用来恢复缺省情况。

【命令】

**[voice-class sip url**  { **sip** \| **sips** }]

**[undo voice-class sip url**]

【缺省情况】

全局使用SIP格式的URL类型。VoIP语音实体下没有缺省的URL类型。如果该语音实体下没有配置URL类型，那么该VoIP语音实体的缺省情况与全局的URL类型相同。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sip**]：指定在SIP呼叫时使用SIP格式的URL类型。

**[sips**]：指定在SIP呼叫时使用SIPS格式的URL类型。

【使用指导】

SIP视图下的**url**命令为全局命令，当VoIP语音实体下配置了URL类型时，则使用VoIP语音实体配置，否则使用全局命令配置的URL类型，即VoIP语音实体配置优先于全局配置。

【举例】

\# 配置SIP呼叫使用SIPS格式的URL类型。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1000 voip

Sysname-voice-dial-entity1000 voice-class sip url sips

【相关命令】

·**url**

**SIP \-- SIP Trunk配置命令 \-- allow-connections**

------------------------------------------------------------------------

**[allow-connections sip**]****tosip**命令用来配置允许SIP到SIP的VoIP呼叫连接。

**[undo allow-connections sip**]****tosip**命令用来关闭SIP到SIP的VoIP呼叫连接，即取消SIP Trunk功能。

【命令】

**[allow-connections sip to sip**]

**[undo allow-connections sip to sip**]

【缺省情况】

不允许SIP到SIP的VoIP呼叫连接。

【视图】

语音视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启**allow-connections sip******tosip**功能后，设备作为SIP Trunk设备。在设备作为SIP Trunk设备使用时，不推荐再将设备作为SIP UA使用。

【举例】

\# 配置允许SIP到SIP的VoIP呼叫连接。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice allow-connections sip to sip

**SIP \-- SIP Trunk配置命令 \-- codec transparent**

------------------------------------------------------------------------

**[codec transparent**]命令用来开启SIP Trunk设备的编解码透传功能。

**[undo** **codec transparent**]命令用来关闭SIP Trunk设备的编解码透传功能。

【命令】

**[codec** **transparent**]

**[undo** **codec** **transparent**]

【缺省情况】

SIP Trunk设备的编解码透传功能处于关闭状态，SIP Trunk设备参与呼叫双方的媒体协商。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

SIP Trunk设备上配置的VoIP语音实体的编解码如果不能和呼叫双方的编解码存在交集，可以使用该命令开启SIP Trunk设备的编解码透传功能。开启SIP Trunk设备的编解码透传功能后，SIP Trunk设备不会干预呼叫两端的编解码协商，而是将编解码能力集透传给对方，由呼叫双方完成编解码协商。

【举例】

\# 在SIP Trunk设备上开启编解码透传功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 codec transparent

**SIP \-- SIP Trunk配置命令 \-- credential**

------------------------------------------------------------------------

**[credentials**]命令用来配置SIP Trunk账户信息。

**[undo** **acredentials**]命令用来删除已配置的SIP Trunk账户信息。

【命令】

**[credentials**]**number** *number*****username***username ***password**[ [{ **cipher** \| **simple** } *password*]]****realm***realm*

**[undo credentials**]******[number ***number*[\|]**number ***number***username***username ***password **[{ **cipher** \| **simple** } *password*]****realm***realm *}

【缺省情况】]

不存在SIP Trunk账户信息。

【视图】

SIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：账户号码，为4～32个字符的字符串。

*[username*]：鉴权时使用的用户名，为1～63个字符的字符串，区分大小写。

**[cipher**]：以密文方式设置用户的密码。

**[simple**]：以明文方式设置用户的密码。

*[password*]：鉴权使用的明文密码或密文密码，区分大小写。明文密码的长度范围是1～16；密文密码的长度范围是1～53。

**[realm*** realm*]：域名，用于注册服务器和SIP UA之间的握手验证，为1～50个字符的字符串，区分大小写。

【使用指导】

在SIP Trunk设备上，运营商给用户分配的信息是通过配置SIP Trunk账户来完成的。SIP Trunk账户号码最多可以向6个注册服务器发起注册，为了区分发送给不同注册服务器的带鉴权信息的注册请求，SIP Trunk设备需要根据注册服务器回复的401/407响应消息中的realm值来匹配配置的鉴权信息。因此一个账户号码需要支持多域名参数，完成账户号码和realm值的配置后，SIP Trunk设备就能选择相应的用户名和密码发送给指定的注册服务器。目前，一个账户号码可以配置携带12个不同的域名，并且设备最多支持128个账户号码。完成SIP Trunk账户配置后，还需要配置**registrar**命令使SIP Trunk账户向指定的注册服务器发起注册。

【举例】

\# 配置SIP Trunk账户信息，号码为1000。对于域名为server1的服务器上，使用的用户名和密码为1000，对于域名为server2的服务器上，使用的用户名和密码为2000，对于域名为server3的服务器上，使用的用户名和密码为3000。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice sip

Sysname-voice-sip credentials number 1000 username 1000 password simple 1000 realm server1

Sysname-voice-sip credentials number 1000 username 2000 password simple 2000 realm server2

Sysname-voice-sip credentials number 1000 username 3000 password simple 3000 realm server3

【命令参考】

·**registrar**

**SIP \-- SIP Trunk配置命令 \-- media flow-around**

------------------------------------------------------------------------

**[media** **flow-around**]命令用来开启SIP Trunk设备的媒体旁路功能，使媒体流在呼叫的两个SIP端点间直接传输。

**[undo** **media** **flow-around**]命令用来恢复缺省情况。

【命令】

**[media** **flow-around**]

**[undo** **media** **flow-around**]

【缺省情况】

媒体流经过SIP Trunk设备进行中继转发。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启SIP Trunk设备的媒体旁路功能，可以使媒体流在呼叫的两个SIP端点间直接传输，SIP Trunk设备不参与媒体流协商。缺省情况下，媒体流经过SIP Trunk设备进行中继转发，SIP Trunk设备会隐藏SIP端点携带的媒体地址，将媒体地址替换为SIP Trunk设备的地址。当不需要隐藏媒体地址时，配置媒体旁路功能可以提升SIP Trunk设备性能。

【举例】

\# 在SIP Trunk设备上开启媒体旁路功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 media flow-around

**SIP \-- SIP Trunk配置命令 \-- voice-class sip early-offer forced**

------------------------------------------------------------------------

**[voice-class sip early-offer** **forced**]命令用来开启SIP Trunk设备的DO-EO转换功能（Delayed offer到Early offer的INVITE消息的转换功能）。

undo {.commandkeywords}**voice-class sip early-offer** **forced**命令用来恢复缺省情况。

【命令】

**[voice-class sip early-offer** **forced**]

**[undo** **voice-class sip** **early-offer** **forced**]

【缺省情况】

SIP Trunk设备的DO-EO转换功能处于关闭状态。

【视图】

VoIP语音实体视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

携带SDP Offer的INVITE消息请求称为Early Offer，不携带SDP Offer的INVITE消息称为Delayed Offer。由于目前很多运营商均不接受不携带SDP Offer的INVITE消息，所以作为中间设备的SIP Trunk设备需要提供这种报文转换功能。在SIP Trunk设备上配置DO-EO转换功能后，设备可以将不携带SDP Offer的INVITE消息转换为携带SDP Offer的INVITE消息，以满足服务器业务呼叫的需求。

需要注意的是，在开启编解码透传功能或媒体旁路功能的情况下，该命令配置不会生效。

【举例】

\# 在SIP Trunk设备上开启DO-EO转换功能。

\<Sysname\> system-view

Sysname voice-setup

Sysname-voice dial-program

Sysname-voice-dial entity 1 voip

Sysname-voice-dial-entity1 **voice-class sip** early-offer forced

【相关命令】

·**codec** **transparent**

·**media** **flow-around**

