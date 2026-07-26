
**802.1X \-- 802.1X配置命令 \-- display dot1x**

------------------------------------------------------------------------

**[display dot1x**]命令用来显示802.1X的相关信息，包括会话连接信息、相关统计信息和配置信息等。

【命令】

**[display dot1x**[ [ **sessions** \| **statistics** ]  **ap** *ap-name* [ **radio** *radio-id*  \| **interface** *interface-type interface-number* ] ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[sessions**]：显示802.1X的会话连接信息。

**[statistics**]：显示802.1X的相关统计信息。

**[ap** *ap-name*]：显示指定AP的所有802.1X的详细信息，*ap-name*表示AP的名称，为1～63个字符的字符串，分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[radio** *radio-id*]：显示指定Radio的所有802.1X的详细信息，*radio-id*表示Radio编号，取值范围与设备型号有关。不指定该参数，则表示显示指定AP的所有Radio的802.1X的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface ***interface-type interface-number*]：显示指定端口的802.1X信息，*interface-type interface-number*为端口类型和端口编号。

【使用指导】

如果不指定参数**sessions**或者**statistics**，则显示802.1X的所有信息，包括会话连接信息、相关统计信息和配置信息等。

如果不指定**ap**和**interface**参数，则显示所有802.1X在线用户的信息，先显示有线的信息再显示无线的信息。

【举例】

\# 显示802.1X的所有信息。

\<Sysname\> display dot1x

 Global 802.1X parameters:

   802.1X authentication  : Enabled

   CHAP authentication    : Enabled

   Max-tx period          : 30 s

   Handshake period       : 15 s

   Quiet timer            : Disabled

       Quiet period       : 60 s

   Supp timeout           : 30 s

   Server timeout         : 100 s

   Reauth period          : 3600 s

   Max auth requests      : 2

   SmartOn switch ID      : 30

   SmartOn supp timeout   : 30 s

   SmartOn retry counts   : 3

   EAD assistant function : Disabled

       URL                : http://www.dwsoft.com

       Free IP            : 6.6.6.0         255.255.255.0

       EAD timeout        : 30 min

   Domain delimiter       : @

 Max 802.1X users         : 1024 per slot

Online 802.1X wired users    : 1

Online 802.1X wireless users : 1

 GigabitEthernet1/0/1  is link-up

   802.1X authentication      : Enabled

   Handshake                  : Enabled

   Handshake security         : Disabled

   Unicast trigger            : Disabled

   Periodic reauth            : Disabled

   Port role                  : Authenticator

   Authorization mode         : Auto

   Port access control        : Port-based

   Multicast trigger          : Enabled

   Mandatory auth domain      : Not configured

   Guest VLAN                 : 3

   Auth-Fail VLAN             : Not configured

   Critical VLAN              : Not configured

   Re-auth server-unreachable : Logoff

   Max online users           : 256

   SmartOn                    : Disabled

   EAPOL packets: Tx 3, Rx 3

   Sent EAP Request/Identity packets : 1

        EAP Request/Challenge packets: 1

        EAP Success packets: 1

        EAP Failure packets: 0

   Received EAPOL Start packets : 1

            EAPOL LogOff packets: 1

            EAP Response/Identity packets : 1

            EAP Response/Challenge packets: 1

            Error packets: 0

   Online 802.1X users: 1

          MAC address         Auth state

          0001-0000-0000      Authenticated

AP name: AP1  Radio ID: 1  SSID: wlan_dot1x_ssid

   BSSID                      : 1111-1111-1111

   802.1X authentication      : Enabled

   Handshake                  : Enabled

   Handshake security         : Disabled

   Periodic reauth            : Disabled

   Mandatory auth domain      : Not configured

   Max online users           : 256

   EAPOL packets: Tx 3, Rx 3

   Sent EAP Request/Identity packets : 1

        EAP Request/Challenge packets: 1

        EAP Success packets: 1

        EAP Failure packets: 0

   Received EAPOL Start packets : 1

        EAPOL LogOff packets: 1

        EAP Response/Identity packets : 1

        EAP Response/Challenge packets: 1

        Error packets: 0

   Online 802.1X users: 1

          MAC address         Auth state

          0001-0000-0002      Authenticated

表1-1 display dot1x命令显示信息描述表

字段

描述

Global 802.1X parameters

全局802.1X参数配置信息

802.1X authentication

全局802.1X的开启状态

CHAP authentication

启用EAP终结方式，并采用CHAP认证方法

EAP authentication

启用EAP中继方式，并支持所有EAP认证方法

PAP authentication

启用EAP终结方式，并采用PAP认证方法

Max-tx period

用户名请求超时定时器的值

Handshake period

握手定时器的值

Quiet timer

静默定时器的开启状态

Quiet period

静默定时器的值

Supp timeout

客户端认证超时定时器的值

Server  timeout

认证服务器超时定时器的值

Reauth period

重认证定时器的值

Max auth requests

设备向接入用户发送认证请求报文的最大次数

SmartOn switch ID

SmartOn的Switch ID

SmartOn supp timeout

SmartOn的客户端认证超时定时器的时长

SmartOn retry counts

SmartOn的通知请求报文的最大发送次数

EAD assistant function

EAD快速部署辅助功能的开启状态

URL

用户HTTP访问的重定向URL

Free IP

用户通过认证之前可访问的网段

EAD timeout

EAD老化定时器超时时间

Domain delimiter

域名分隔符

Max 802.1X users

每个单板最大支持的接入用户数

Online 802.1X wired users

在线802.1X有线用户数

Online 802.1X wireless users

在线802.1X无线用户数

GigabitEthernet1/0/1 is link-up

端口GigabitEthernet1/0/1的链路状态

802.1X authentication

端口上802.1X的开启状态

Handshake

在线用户握手功能的开启状态

Handshake security

安全握手功能的开启状态

Unicast trigger

802.1X单播触发功能的开启状态

Periodic reauth

周期性重认证功能的开启状态

Port role

该端口担当认证端的作用，目前仅支持作为认证端

Authorization mode

端口的授权状态

·Force-Authorized：强制授权状态

·Auto：自动识别状态

·Force-Unauthorized：强制非授权状态

Port access control

端口接入控制方式

·MAC-based：基于MAC地址对接入用户进行认证（该方式的生效情况与设备的型号有关，请以设备的实际情况为准）

·Port-based：基于端口对接入用户进行认证

Multicast trigger

802.1X组播触发功能的开启状态

Mandatory auth domain

端口上的接入用户使用的强制认证域

Guest VLAN

端口配置的Guest VLAN

Auth-fail VLAN

端口配置的Auth-Fail VLAN

Critical VLAN

端口配置的Critical VLAN

Re-auth server-unreachable

重认证时服务器不可达对802.1X在线用户采取的动作

Max online users

本端口最多可容纳的接入用户数

SmartOn

端口上SmartOn的开启状态

EAPOL packets

EAPOL报文数目。Tx表示发送的报文数目；Rx表示接受的报文数目

Sent EAP Request/Identity packets

发送的EAP Request/Identity报文数

EAP Request/Challenge packets

发送的EAP Request/Challenge报文数

EAP Success packets

发送的EAP Success报文数

EAP Fail packets

发送的EAP Failure报文数

Received EAPOL Start packets

接收的EAPOL Start报文数

EAPOL LogOff packets

接收的EAPOL LogOff报文数

EAP Response/Identity packets

接收的EAP Response/Identity报文数

EAP Response/Challenge packets

接收的EAP Response/Challenge报文数

Error packets

接收的错误报文数

Online 802.1X users

端口上的在线802.1X用户数

MAC address

802.1X用户的MAC地址

Auth state

802.1X用户的认证状态

AP name

AP名称

Radio ID

Radio编号

SSID

服务集标识符

BSSID

基本服务集标识符

**802.1X \-- 802.1X配置命令 \-- display dot1x connection**

------------------------------------------------------------------------

**[display dot1x connection**]命令用来显示当前802.1X在线用户的详细信息。

【命令】

集中式设备：

**[display dot1x connection **[ **ap** *ap-name* [ **radio** *radio-id*  \| **interface** *interface-type* *interface-number* \| **user-mac** *mac-addr* \| **user-name** *name-string* ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display dot1x connection **[ **ap** *ap-name* [ **radio** *radio-id*  \| **interface** *interface-type* *interface-number* \| **slot** *slot-number* \| **user-mac** *mac-addr* \| **user-name** *name-string* ]]]

分布式设备－IRF模式[:]

**[display dot1x connection **[ **ap** *ap-name* [ **radio** *radio-id*  \| **chassis** *chassis-number* **slot** *slot-number* \| **interface** *interface-type* *interface-number*  \| **user-mac** *mac-addr* \| **user-name** *name-string* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ap** *ap-name*]：显示接入指定AP的所有802.1X在线用户的信息，*ap-name*表示AP的名称，为1～63个字符的字符串，分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[radio** *radio-id*]：显示接入指定Radio的802.1X在线用户的信息，*radio-id*表示Radio编号，取值范围与设备型号有关。不指定该参数，则表示显示接入AP下所有Radio的802.1X在线用户的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface ***interface-type interface-number*]：显示指定端口的802.1X用户信息。其中*interface-type interface-number*表示端口类型和端口编号。（集中式设备）

**[slot ***slot-number*]：显示指定单板上的802.1X用户信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的802.1X用户信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持[IRF3的设备）]

**[slot** *slot-number*]：显示指定成员设备/PEX上的802.1X用户信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis*** chassis-number ***slot*** slot-number*]：显示指定成员设备上指定单板的802.1X用户信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持[IRF3的设备）]

**[chassis*** chassis-number ***slot*** slot-number*]：显示指定单板的802.1X用户信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[user-mac** *mac-addr*]：显示指定MAC地址的802.1X用户信息。其中*mac-addr*表示用户的MAC地址，格式为H-H-H。

**[user-name ***name-string*]：显示指定用户名的802.1X用户信息。其中*name-string*表示用户名，为1～253个字符的字符串，区分大小写。

【使用指导】

若不指定任何参数，则显示所有端口的802.1X在线用户信息。（集中式设备）

若不指定任何参数，则显示所有单板上的802.1X在线用户信息。（分布式设备－独立运行模式）

若不指定任何参数，则显示所有成员设备上的802.1X在线用户信息。（集中式IRF设备）

若不指定任何参数，则显示所有成员设备上的802.1X在线用户信息。（分布式设备－IRF模式）

【举例】

\# 显示所有802.1X在线用户信息。（集中式设备）

\<Sysname\> display dot1x connection

User MAC address: 0015-e9a6-7cfe

Access interface: GigabitEthernet1/0/1

Username: ias

Authentication domain: h3c

IPv4 address: 192.168.1.1

IPv6 address: 2000:0:0:0:1:2345:6789:abcd

Authentication method: CHAP

Initial VLAN: 1

Authorization untagged VLAN: N/A

Authorization tagged VLAN list: 1 to 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 29 31 33

                                35 37 40 to 100

Authorization ACL ID: 3001

Authorization user profile: N/A

Termination action: Default

Session timeout period: 2 s

Online from: 2013/03/02  13:14:15

Online duration: 0h 2m 15s

User MAC address                : 0015-e9a6-7cfe

AP name                         : ap1

Radio ID                        : 1

SSID                            : wlan_dot1x_ssid

BSSID                           : 0015-e9a6-7cf0

User name                       : ias

Authentication domain           : 1

IPv4 address                    : 192.168.1.1

IPv6 address                    : 2000:0:0:0:1:2345:6789:abcd

Authentication method           : CHAP

Initial VLAN                    : 1

Authorization VLAN              : N/A

Authorization ACL number        : 3001

Authorization user profile      : N/A

Termination action              : Default

Session timeout period          : 2 sec

Online from                     : 2013/03/02 13:14:15

Online duration                 : 0 h 2 m 15 s

Total 1 connections matched.

\# 显示所有802.1X在线用户信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display dot1x connection

Slot ID: 0

User MAC address: 0015-e9a6-7cfe

Access interface: GigabitEthernet1/0/1

Username: ias

Authentication domain: h3c

IPv4 address: 192.168.1.1

IPv6 address: 2000:0:0:0:1:2345:6789:abcd

Authentication method: CHAP

Initial VLAN: 1

Authorization untagged VLAN: N/A

Authorization tagged VLAN list: 1 to 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 29 31 33

                                35 37 40 to 100

Authorization ACL ID: 3001

Authorization user profile: N/A

Termination action: Default

Session timeout period: 2 s

Online from: 2013/03/02  13:14:15

Online duration: 0h 2m 15s

User MAC address                : 0015-e9a6-7cfe

AP name                         : ap1

Radio ID                        : 1

SSID                            : wlan_dot1x_ssid

BSSID                           : 0015-e9a6-7cf0

User name                       : ias

Authentication domain           : 1

IPv4 address                    : 192.168.1.1

IPv6 address                    : 2000:0:0:0:1:2345:6789:abcd

Authentication method           : CHAP

Initial VLAN                    : 1

Authorization VLAN              : N/A

Authorization ACL number        : 3001

Authorization user profile      : N/A

Termination action              : Default

Session timeout period          : 2 sec

Online from                     : 2013/03/02 13:14:15

Online duration                 : 0 h 2 m 15 s

Total 1 connections matched.

\# 显示所有802.1X在线用户信息。（分布式设备－IRF模式）

\<Sysname\> display dot1x connection

Chassis ID: 1

Slot ID: 0

User MAC address: 0015-e9a6-7cfe

Access interface: GigabitEthernet1/0/1

Username: ias

Authentication domain: h3c

IPv4 address: 192.168.1.1

IPv6 address: 2000:0:0:0:1:2345:6789:abcd

Authentication method: CHAP

Initial VLAN: 1

Authorization untagged VLAN: N/A

Authorization tagged VLAN list: 1 to 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 29 31 33

                                35 37 40 to 100

Authorization ACL ID: 3001

Authorization user profile: N/A

Termination action: Default

Session timeout period: 2 s

Online from: 2013/03/02  13:14:15

Online duration: 0h 2m 15s

User MAC address                : 0015-e9a6-7cfe

AP name                         : ap1

Radio ID                        : 1

SSID                            : wlan_dot1x_ssid

BSSID                           : 0015-e9a6-7cf0

User name                       : ias

Authentication domain           : 1

IPv4 address                    : 192.168.1.1

IPv6 address                    : 2000:0:0:0:1:2345:6789:abcd

Authentication method           : CHAP

Initial VLAN                    : 1

Authorization VLAN              : N/A

Authorization ACL number        : 3001

Authorization user profile      : N/A

Termination action              : Default

Session timeout period          : 2 sec

Online from                     : 2013/03/02 13:14:15

Online duration                 : 0 h 2 m 15 s

Total 1 connections matched.

表1-2 display dot1x connection 命令显示信息描述表

字段

描述

Chassis ID

当前设备对应的框号

Slot ID

当前设备对应的板号

User MAC address

用户的MAC地址

Access interface

用户的接入接口名称

AP name

AP的名称

Radio ID

Radio的ID

SSID

服务集标识符

BSSID

用户所属的基本服务集标识符

Username

用户名

Authentication domain

认证时使用的ISP域的名称

IPv4 address

用户IP地址

若未获取到用户的IP地址，则不显示该字段

IPv6 address

用户IPv6地址

若未获取到用户的IP地址，则不显示该字段

Authentication method

802.1X系统的认证方法

·CHAP：启用EAP终结方式，并采用CHAP认证方法

·EAP：启用EAP中继方式，并支持所有EAP认证方法

·PAP：启用EAP终结方式，并采用PAP认证方法

Initial VLAN

初始的VLAN

Authorization untagged VLAN

授权的untagged VLAN

Authorization tagged VLAN list

授权的tagged VLAN列表

Authorization ACL ID

授权的ACL的编号

Authorization user profile

授权用户的User profile名称

Termination action

服务器下发的终止动作类型：

·Default：会话超时时长到达后，强制用户下线

·Radius-Request：会话超时时长到达后，要求802.1X用户进行重认证

用户采用本地认证时，该字段显示为N/A

Session timeout period

服务器下发的会话超时时长，该时间到达之后，用户所在的会话将会被删除，之后，对该用户所采取的动作，由Terminate action字段的取值决定

用户采用本地认证时，该字段显示为N/A

Online from

用户的上线时间

Online duration

用户的在线时长

Total *xxx* connections matched.

在线用户个数

**802.1X \-- 802.1X配置命令 \-- dot1x**

------------------------------------------------------------------------

**[dot1x**]命令用来开启指定端口上或全局的802.1X。

**[undo dot1x**]命令用来关闭指定端口上或全局的802.1X。

【命令】

**[dot1x**]

**[undo dot1x**]

【缺省情况】

所有端口以及全局的802.1X都处于关闭状态。

【视图】

系统视图/以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有同时开启全局和端口的802.1X后，802.1X的配置才能在端口上生效。

【举例】

\# 开启全局的802.1X。

\<Sysname\> system-view

Sysname dot1x

\# 开启端口GigabitEthernet1/0/1上的802.1X。

Sysname interface gabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x

Sysname-GigabitEthernet1/0/1 quit

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x authentication-method**

------------------------------------------------------------------------

**[dot1x authentication-method**]命令用来配置802.1X系统的认证方法。

**[undo dot1x authentication-method**]命令用来恢复缺省情况。

【命令】

**[dot1x authentication-method **[{ **chap** *\|* **eap** *\|* **pap** }]]

**[undo dot1x authentication-method**]

【缺省情况】

设备启用EAP终结方式，并采用CHAP认证方法。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chap**]：启用EAP终结方式，并支持与RADIUS服务器之间采用CHAP类型的认证方法。

**[eap**]：启用EAP中继方式，并支持客户端与RADIUS服务器之间所有类型的EAP认证方法。

**[pap**]：启用EAP终结方式，并支持与RADIUS服务器之间采用PAP类型的认证方法。

【使用指导】

(1)EAP终结：设备将收到的客户端EAP报文中的用户认证信息重新封装在标准的RADIUS报文中，然后采用PAP或CHAP认证方法与RADIUS服务器完成认证交互。该认证方式的优点是，现有的RADIUS服务器基本均可支持PAP和CHAP认证，无需升级服务器，但设备处理较为复杂，且目前仅能支持MD5-Challenge类型的EAP认证以及iNode 802.1X客户端发起的"用户名+密码"方式的EAP认证。

·PAP（Password Authentication Protocol，密码验证协议）通过用户名和口令来对用户进行验证，其特点是在网络上以明文方式传送用户名和口令，仅适用于对网络安全要求相对较低的环境。目前，H3C iNode 802.1X客户端支持此认证方法。

·CHAP（Challenge Handshake Authentication Protocol，质询握手验证协议）采用客户端与服务器端交互挑战信息的方式来验证用户身份，其特点是在网络上以明文方式传送用户名，以密文方式传输口令。与PAP相比，CHAP认证保密性较好，更为安全可靠。

(2)EAP中继：设备将收到的客户端EAP报文直接封装到RADIUS报文的属性字段中，发送给RADIUS服务器完成认证。该认证方式的优点是，设备处理简单，且可支持多种类型的EAP认证方法，例如MD5-Challenge、EAP-TLS、PEAP等，但要求服务器端支持相应的EAP认证方法。

需要注意的是：

·采用远程RADIUS认证时，PAP、CHAP、EAP认证的最终实现，需要RADIUS服务器支持相应的PAP、CHAP、EAP认证方法。

·若采用EAP认证方法，则RADIUS方案下的**user-name-format**配置无效，**user-name-format**的介绍请参见"安全命令参考"中的"AAA"。

【举例】

\# 启用EAP终结方式，并支持与RADIUS服务器之间采用PAP类型的认证方法。

\<Sysname\> system-view

Sysname dot1x authentication-method pap

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x auth-fail vlan**

------------------------------------------------------------------------

**[dot1x auth-fail vlan**]命令用来配置指定端口的802.1X Auth-Fail VLAN，即认证失败的802.1X用户被授权访问的VLAN。

**[undo dot1x auth-fail vlan**]命令用来恢复缺省情况**。**

【命令】

**[dot1x auth-fail vlan ***authfail-vlan-id*]

**[undo dot1x auth-fail vlan**]

【缺省情况】

端口上未配置802.1X Auth-Fail VLAN。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[authfail-vlan-id*]：端口上指定的Auth-Fail VLAN ID，取值范围为1～4094（该取值范围与设备型号有关，请以设备的实际情况为准）。该VLAN必须已经创建。

【使用指导】

如果某个VLAN被指定为Super VLAN，则该VLAN不能被指定为某个端口的802.1X Auth-Fail VLAN；同样，如果某个VLAN被指定为某个端口的802.1X Auth-Fail VLAN，则该VLAN不能被指定为Super VLAN。

禁止删除已被配置为Auth-Fail VLAN的VLAN，若要删除该VLAN，请先使用命令**undo dot1x auth-fail vlan**取消802.1X Auth-Fail VLAN配置。

【举例】

\# 配置端口GigabitEthernet1/0/1的Auth-Fail VLAN为VLAN 100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x auth-fail vlan 100

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x critical vlan**

------------------------------------------------------------------------

**[dot1x critical vlan**]命令用来配置指定端口的802.1X Critical VLAN，即当802.1X用户认证时对应的ISP域下所有认证服务器都不可达的情况下端口加入的VLAN。

**[undo dot1x critical vlan**]命令用来恢复缺省情况**。**

【命令】

**[dot1x critical vlan ***vlan-id*]

**[undo dot1x critical vlan**]

【缺省情况】

端口上未配置Critical VLAN。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：端口上指定的Critical VLAN ID，取值范围为1～4094（该取值范围与设备型号有关，请以设备的实际情况为准）。该VLAN必须已经创建。

【使用指导】

如果某个VLAN被指定为Super VLAN，则该VLAN不能被指定为某个端口的802.1X Critical VLAN；同样，如果某个VLAN被指定为某个端口的802.1X Critical VLAN，则该VLAN不能被指定为Super VLAN。

禁止删除已被配置为Critical VLAN的VLAN，若要删除该VLAN，请先使用命令**undo dot1x critical vlan**取消802.1X Critical VLAN配置。

【举例】

\# 配置端口GigabitEthernet1/0/1的Critical VLAN为VLAN 100 。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x critical vlan 100

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x domain-delimiter**

------------------------------------------------------------------------

**[dot1x domain-delimiter**]命令用来配置域名分隔符。

**[undo dot1x domain-delimiter**]命令用来恢复缺省情况。

【命令】

**[dot1x domain-delimiter** *string*]

**[undo dot1x domain-delimiter**]

【缺省情况】

802.1X支持的域名分隔符为@。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[string*]：多个域名分隔符组成的1～16个字符的字符串，其中每个字符必须是@、/、\和.四之一。若要指定域名分隔符\，则必须在输入时使用转义操作符\，即输入\\\。

【使用指导】

目前，802.1X支持的域名分隔符包括@、\、/和.，对应的用户名格式分别为*username*@*domain-name*， *domain-name*\\*username*、*username*/*domain-name*和*username*.*domain-name*，其中*username*为纯用户名、*domain-name*为域名。如果用户名中包含有多个域名分隔符字符，则设备仅将最后一个出现的域名分隔符识别为实际使用的域名分隔符，例如，用户输入的用户名为121.123/22\\@abc，设备上指定802.1X支持的域名分隔符为/、\，则识别出的纯用户名为\@abc，域名为123/22。

需要注意的是，系统默认支持分隔符@，但如果通过本命令指定的域名分隔符中未包含分隔符@，则802.1X仅会支持命令中指定的分隔符。

【举例】

\# 配置802.1X支持的域名分隔符为@和/。

\<Sysname\> system-view

Sysname dot1x domain-delimiter @/

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x ead-assistant enable**

------------------------------------------------------------------------

**[dot1x ead-assistant enable**]命令用来开启EAD快速部署辅助功能。

**[undo dot1x ead-assistant enable**]命令用来关闭EAD快速部署辅助功能。

【命令】

**[dot1x ead-assistant enable**]

**[undo dot1x ead-assistant enable**]

【缺省情况】

EAD快速部署辅助功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启EAD快速部署辅助功能后，设备允许未通过认证的802.1X用户访问一个特定的IP地址段，并可以将用户发起的HTTP访问请求重定向到该IP地址段中的一个指定的URL，实现用户自动下载并安装EAD客户端的目的。

该命令与MAC地址认证和端口安全的全局使能命令均互斥，即开启EAD快速部署辅助功能时，若全局使能了MAC地址认证或端口安全，则该配置将会执行失败，反之亦然。

【举例】

\# 开启EAD快速部署辅助功能。

\<Sysname\> system-view

Sysname dot1x ead-assistant enable

【相关命令】

·**display dot1x**

·**dot1x ead-assistant free-ip**

·**dot1x ead-assistant url**

**802.1X \-- 802.1X配置命令 \-- dot1x ead-assistant free-ip**

------------------------------------------------------------------------

**[dot1x ead-assistant free-ip**]命令用来配置Free IP，即用户在未通过802.1X认证之前能够访问的网段。

**[undo dot1x ead-assistant free-ip**]命令用来恢复缺省情况。

【命令】

**[dot1x ead-assistant free-ip ***ip-address*****[{ *mask-address* \| *mask-length* }]]

**[undo**[ **dot1x ead-assistant free-ip** { *ip-address* { *mask-address* \| *mask-length* } \| **all** }]]

【缺省情况】

未配置Free IP，用户在通过802.1X认证之前不能够访问任何网段。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定的IP地址。

*[mask-address*]：指定的IP掩码地址。

*[mask-length*]：指定的IP掩码地址长度，取值范围为1～32。

**[all**]：所有配置的IP。

【使用指导】

全局使能EAD快速部署功能且配置Free IP之后，未通过认证的802.1X终端用户可以访问该IP地址段中的网络资源。

【举例】

\# 配置用户在通过802.1X认证之前能够访问的网段为192.168.1.1/16。

\<Sysname\> system-view

Sysname dot1x ead-assistant free-ip 192.168.1.1 255.255.0.0

【相关命令】

·**display dot1x**

·**dot1x ead-assistant enable**

·**dot1x ead-assistant ur****l**

**802.1X \-- 802.1X配置命令 \-- dot1x ead-assistant url**

------------------------------------------------------------------------

**[dot1x ead-assistant url**]命令用来配置802.1X用户HTTP访问的重定向URL。

**[undo dot1x ead-assistant url**]命令用来恢复缺省情况。

【命令】

**[dot1x ead-assistant url ***url-string*]

**[undo dot1x ead-assistant url**]

【缺省情况】

未配置重定向URL。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url-string*]：重定向URL地址字符串，为1～64个字符的字符串，不区分大小写。

【使用指导】

用户在802.1X认证成功之前，如果使用浏览器访问非Free IP网段的其它网络，设备会将用户访问的URL重定向到已配置的HTTP访问的重定向地址。

802.1X用户HTTP访问的重定向URL和Free IP必须在同一个网段内，否则用户无法访问指定的重定向URL。

802.1X用户HTTP访问的重定向URL可多次配置，但仅最后配置的一条有效。

【举例】

\# 配置802.1X用户HTTP访问的重定向URL为http://test.com。

\<Sysname\> system-view

Sysname dot1x ead-assistant url http://test.com

【相关命令】

·**display dot1x**

·**dot1x ead-assistant enable**

·**dot1x ead-assistant free-ip**

**802.1X \-- 802.1X配置命令 \-- dot1x guest-vlan**

------------------------------------------------------------------------

**[dot1x guest-vlan**]命令用来配置指定端口的802.1X Guest VLAN，即802.1X用户在未认证的情况下可以访问的VLAN资源，该VLAN内通常放置一些用于用户下载客户端软件或其他升级程序的服务器。

**[undo dot1x guest-vlan**]命令用来恢复缺省情况**。**

【命令】

**[dot1x guest-vlan ***guest-vlan-id*]

**[undo dot1x guest-vlan**]

【缺省情况】

端口上未配置802.1X Guest VLAN。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[guest-vlan-id*]：端口上指定的Guest VLAN ID，取值范围为1～4094（该取值范围与设备型号有关，请以设备的实际情况为准）。该VLAN必须已经创建。

【使用指导】

如果某个VLAN被指定为Super VLAN，则该VLAN不能被指定为某个端口的802.1X Guest VLAN；同样，如果某个VLAN被指定为某个端口的802.1X Guest VLAN，则该VLAN不能被指定为Super VLAN。

禁止删除已被配置为Guest VLAN的VLAN，若要删除该VLAN，请先使用命令**undo dot1x guest-vlan**取消802.1X Guest VLAN配置。

【举例】

\# 配置端口GigabitEthernet1/0/1的Guest VLAN为VLAN 100 。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x guest-vlan 100

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x handshake**

------------------------------------------------------------------------

**[dot1x handshake**]命令用于开启在线用户握手功能。

**[undo dot1x handshake**]命令用于关闭在线用户握手功能。

【命令】

**[dot1x handshake**]

**[undo dot1x handshake**]

【缺省情况】

在线用户握手功能处于开启状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启设备的在线用户握手功能后，设备会定期（时间间隔通过命令**dot1x timer handshake-period**设置）向通过802.1X认证的在线用户发送握手报文，以定期检测用户的在线情况。如果设备连续多次（通过命令**dot1x retry**设置）没有收到客户端的响应报文，则会将用户置为下线状态。

【举例】

\# 在端口GigabitEthernet1/0/1上开启在线用户握手功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x handshake

【相关命令】

·**display dot1x**

·**dot1x timer handshake-period**

·**dot1x retry**

**802.1X \-- 802.1X配置命令 \-- dot1x handshake secure**

------------------------------------------------------------------------

**[dot1x handshake secure**]命令用来开启在线用户握手安全功能。

**[undo dot1x handshake secure**]命令用来关闭在线用户握手安全功能**。**

【命令】

**[dot1x handshake secure**]

**[undo dot1x handshake secure**]

【缺省情况】

在线用户握手安全功能处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有设备上的在线用户握手功能处于开启状态时，安全握手功能才会生效。

本功能仅能在iNode客户端和iMC服务器配合使用的组网环境中生效。

【举例】

\# 在端口GigabitEthernet1/0/1上开启安全握手功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x handshake secure

【相关命令】

·**display dot1x**

·**dot1x handshake**

**802.1X \-- 802.1X配置命令 \-- dot1x mandatory-domain**

------------------------------------------------------------------------

**[dot1x mandatory-domain**]命令用来指定端口上802.1X用户使用的强制认证域。

**[undo dot1x mandatory-domain**]命令用来删除该端口上为802.1X用户指定的强制认证域。

【命令】

**[dot1x mandatory-domain** *domain-name*]

**[undo dot1x** **mandatory-domain**]

【缺省情况】

未指定802.1X用户使用的强制认证域。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：ISP域名，为1～255个字符的字符串，不区分大小写。

【使用指导】

从指定端口上接入的802.1X用户将按照如下先后顺序选择认证域：端口上指定的强制ISP域\--\>用户名中指定的ISP域\--\>系统缺省的ISP域。

【举例】

\# 指定端口GigabitEthernet1/0/1上802.1X用户使用的强制认证域为my-domain。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x mandatory-domain my-domain

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x max-user**

------------------------------------------------------------------------

**[dot1x** **max-user**]命令用来配置端口上最多允许同时接入的802.1X用户数。当接入此端口的802.1X用户数超过最大值后，新接入的用户将被拒绝。

**[undo dot1x** **max-user**]命令用来恢复缺省情况。

【命令】

**[dot1x** **max-user** *user-number*]

**[undo dot1x** **max-user**]

【缺省情况】

端口上最多允许同时接入的802.1X用户数与设备的型号有关，请以设备的实际情况为准。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[user-number*]：端口允许同时接入的802.1X用户数的最大值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

由于系统资源有限，如果当前端口上接入的用户过多，接入用户之间会发生资源的争用，因此适当地配置该值可以使属于当前端口的用户获得可靠的性能保障。

【举例】

\# 配置端口GigabitEthernet1/0/1上最多允许同时接入32个802.1X用户。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x max-user 32

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x multicast-trigger**

------------------------------------------------------------------------

**[dot1x multicast-trigger**]命令用来开启802.1X的组播触发功能。

**[undo dot1x multicast-trigger**]命令用来关闭802.1X的组播触发功能。

【命令】

**[dot1x multicast-trigger**]

**[undo dot1x multicast-trigger**]

【缺省情况】

802.1X的组播触发功能处于开启状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启了802.1X的组播触发功能的端口会定期（间隔时间通过命令**dot1x timer tx-period**设置）向客户端组播发送EAP-Request/Identity报文来检测客户端并触发认证。该功能用于支持不能主动发送EAPOL-Start报文来发起认证的客户端。

对于无线局域网来说，可以由客户端主动发起认证，或由无线模块发现用户并触发认证，而不必设备端定期发送802.1X的组播报文来触发。同时，组播触发报文会占用无线的通信带宽，因此建议无线局域网中的接入设备关闭该功能。

【举例】

\# 在端口GigabitEthernet1/0/1上开启802.1X的组播触发功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x multicast-trigger

【相关命令】

·**display dot1x**

·**dot1x timer tx-period**

·**dot1x unicast-trigger**

**802.1X \-- 802.1X配置命令 \-- dot1x port-control**

------------------------------------------------------------------------

**[dot1x** **port-control**]命令用来设置端口的授权状态。

**[undo dot1x** **port-control**]命令用来恢复缺省情况。

【命令】

**[dot1x**[ **port-control** { **authorized-force** \| **auto** \| **unauthorized-force** }]]

**[undo dot1x** **port-control**]

【缺省情况】

端口的授权状态为**auto**。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[authorized-force**]：强制授权状态，表示端口始终处于授权状态，允许用户不经认证授权即可访问网络资源。

**[auto**]：自动识别状态，表示端口初始状态为非授权状态，仅允许EAPOL报文收发，不允许用户访问网络资源；如果用户认证通过，则端口切换到授权状态，允许用户访问网络资源。这也是最常用的一种状态。

**[unauthorized-force**]：强制非授权状态，表示端口始终处于非授权状态，不允许用户访问网络资源。

【使用指导】

通过配置端口的授权状态，可以控制端口上接入的用户是否需要通过认证才能访问网络资源。

【举例】

\# 指定端口GigabitEthernet1/0/1处于强制非授权状态。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x port-control unauthorized-force

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x port-method**

------------------------------------------------------------------------

**[dot1x** **port-method**]命令用来配置端口的接入控制方式。

**[undo dot1x** **port-method**]命令用来恢复缺省情况。

【命令】

**[dot1x**[ **port-method** { **macbased** \| **portbased** }]]

**[undo dot1x** **port-method**]

【缺省情况】

端口的接入控制方式为**macbased**。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[macbased**]：表示基于MAC地址对接入用户进行认证，即该端口下的所有接入用户均需要单独认证，当某个用户下线时，也只有该用户无法使用网络。

**[portbased**]：表示基于端口对接入用户进行认证，即只要该端口下的第一个用户认证成功后，其他接入用户无须认证就可使用网络资源，当第一个用户下线后，其它用户也会被拒绝使用网络。

【使用指导】

部分设备上不支持**macbased**方式，因此**macbased**方式的配置生效情况与设备的型号有关，请以设备的实际情况为准。

若端口上同时启动了802.1X和Portal认证功能，则端口接入控制方式必须为**macbased**。关于Portal认证的相关介绍，请参考"安全配置指导"中的"Portal"。

在要求所有接入用户都单独认证的情况下，选择基于MAC的控制方式，可提高网络接入的安全性。否则，可采用基于端口的接入控制方式。

【举例】

\# 在端口GigabitEthernet1/0/1上配置对接入用户进行基于端口的802.1X认证。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x port-method portbased

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x quiet-period**

------------------------------------------------------------------------

**[dot1x** **quiet-period**]命令用来开启静默定时器功能。

**[undo dot1x** **quiet-period**]命令用来关闭静默定时器功能。

【命令】

**[dot1x** **quiet-period**]

**[undo dot1x quiet-period**]

【缺省情况】

静默定时器功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在静默定时器功能处于开启状态的情况下，设备将在一段时间之内不对802.1X认证失败的用户进行802.1X认证处理，该时间由802.1X静默定时器控制，可通过**dot1x timer quiet-period**命令配置。

【举例】

\# 开启静默定时器功能，并配置静默定时器的值为100秒。

\<Sysname\> system-view

Sysname dot1x quiet-period

Sysname dot1x timer quiet-period 100

【相关命令】

·**display dot1x**

·**dot1x timer**

**802.1X \-- 802.1X配置命令 \-- dot1x re-authenticate**

------------------------------------------------------------------------

**[dot1x re-authenticate**]命令用来开启周期性重认证功能。

**[undo dot1x re-authenticate**]命令用来关闭周期性重认证功能。

【命令】

**[dot1x re-authenticate**]

**[undo dot1x re-authenticate**]

【缺省情况】

周期性重认证功能处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

端口启动了802.1X的周期性重认证功能后，设备会根据周期性重认证定时器（**dot1x timer reauth-period**）设定的时间间隔定期启动对该端口在线802.1X用户的认证，以检测用户连接状态的变化，更新服务器下发的授权属性（例如ACL、VLAN、QoS Profile）。

【举例】

\# 在端口GigabitEthernet1/0/1上开启802.1X重认证功能，并配置周期性重认证时间间隔为1800秒。

\<Sysname\> system-view

Sysname dot1x timer reauth-period 1800

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x re-authenticate

【相关命令】

·**display dot1x**

·**dot1x timer**

**802.1X \-- 802.1X配置命令 \-- dot1x re-authenticate server-unreachable keep-online**

------------------------------------------------------------------------

**[dot1x re-authenticate server-unreachable keep-online**]命令用来配置重认证服务器不可达时端口上的用户保持在线状态。

**[undo dot1x re-authenticate server-unreachable**]命令用来恢复缺省情况**。**

【命令】

**[dot1x re-authenticate server-unreachable keep-online**]

**[undo dot1x re-authenticate server-unreachable**]

【缺省情况】

端口上的802.1X在线用户重认证时，若认证服务器不可达，则会被强制下线。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

若端口上启动了802.1X的周期性重认证功能，则设备会定期对端口上的802.1X在线用户进行重认证，重认证过程中，若设备发现认证服务器状态不可达，则可以根据本配置，决定是否保持其在线状态。

【举例】

\# 配置[端口]GigabitEthernet1/0/1上的802.1X在线用户进行重认证时，若服务器不可达，则保持在线状态。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x re-authenticate server-unreachable keep-online

【相关命令】

·**display dot1x**

·**dot1x re-authenticate**

**802.1X \-- 802.1X配置命令 \-- dot1x retry**

------------------------------------------------------------------------

**[dot1x** **retry**]命令用来设置设备向接入用户发送认证请求报文的最大次数。

**[undo dot1x** **retry**]命令用来恢复缺省情况。

【命令】

**[dot1x** **retry** *max-retry-value*]

**[undo dot1x** **retry**]

【缺省情况】

设备向接入用户发送认证请求报文的最大次数为2。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-retry-value*]：向接入用户发送认证请求报文的最大尝试次数，取值范围为1～10。

【使用指导】

如果设备向用户发送认证请求报文后，在规定的时间里没有收到用户的响应，则设备将向用户重发该认证请求报文，若设备累计发送认证请求报文的次数达到配置的最大值后，仍然没有得到用户响应，则停止发送认证请求。对于EAP-Request/Identity报文，该时间由**dot1x timer tx-period**设置；对于EAP-Request/MD5 Challenge报文，该时间由**dot1x timer supp-timeout**设置。

【举例】

\# 配置设备最多向接入用户发送9次认证请求报文。

\<Sysname\> system-view

Sysname dot1x retry 9

【相关命令】

·**display dot1x**

·**dot1x timer**

**802.1X \-- 802.1X配置命令 \-- dot1x smarton**

------------------------------------------------------------------------

**[dot1x smarton**]命令用来开启端口的SmartOn功能。

**[undo dot1x smarton**]命令用来关闭端口的SmartOn功能。

【命令】

**[dot1x smarton**]

**[undo dot1x smarton**]

【缺省情况】

端口的SmartOn功能处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

若开启了SmartOn功能的端口上收到802.1X客户端发送的EAPOL-Start报文，则将向其回复单播的EAP-Request/Notification报文，并开启定时器（**dot1x smarton timer supp-timeout**）等待客户端响应EAP-Response/Notification报文。该Notification报文中包含一个Switch ID和一个MD5摘要，若这两个值与本地配置的SmartOn的Switch ID以及SmartOn密码的MD5摘要值相同，则继续客户端的802.1X认证，否则中止客户端的802.1X认证。

【举例】

\# 使能端口GigabitEthernet1/0/1的SmartOn功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x smarton

【相关命令】

·**display dot1x**

·**dot1x smarton switchid**

·**dot1x smarton password**

**802.1X \-- 802.1X配置命令 \-- dot1x smarton password**

------------------------------------------------------------------------

**[dot1x smarton password**]命令用来配置SmartOn密码。

**[undo dot1x smarton password**]命令用来恢复缺省情况。

【命令】

**[dot1x smarton password **[{ **cipher** *cipher-string* \| **simple** *plain-string* }]]

**[undo** **dot1x smarton password**]

【缺省情况】

未配置SmartOn密码。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置用户密码。

*[cipher-string*]：设置的密文密码，区分大小写，[为]1～53个字符的字符串。

**[simple**]：表示以明文方式设置用户密码。

*[plain-string*]：设置的明文密码，区分大小写，[为]1～16个字符的字符串。

【使用指导】

使能了SmartOn功能的端口上，需要验证802.1X客户端发送的EAP-Response/Notification报文中携带的MD5摘要，只有与本命令配置的SmartOn密码的MD5摘要相同，客户端802.1X的认证才能继续进行。

不论以密文形式还是明文形式配置密码，设备均以密文形式存储，并且后配置的密码会覆盖先前配置的密码。

【举例】

\# 配置SmartOn密码为abc。

\<Sysname\> system-view

Sysname dot1x smarton password simple abc

【相关命令】

·**display dot1x**

·**dot1x smarton**

·**dot1x smarton switchid**

**802.1X \-- 802.1X配置命令 \-- dot1x smarton retry**

------------------------------------------------------------------------

**[dot1x smarton retry**]命令用来配置重发SmartOn通知请求报文的最大次数。

**[undo dot1x smarton retry**]命令用来恢复缺省情况。

【命令】

**[dot1x smarton retry** *retries*]

**[undo dot1x smarton retry**]

【缺省情况】

重发SmartOn通知请求报文的最大次数为3次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retries*]：重发SmartOn通知请求报文的最大次数[，取值范围为]1～10。

【使用指导】

设备向客户端发送EAP-Request/Notification报文后，会开启通知请求超时定时器（**dot1x smarton timer supp-timeout**）等待客户端响应EAP-Response/Notification报文，若定时器超时后客户端仍未回复，则设备会重发EAP-Request/Notification报文，并重新启动定时器。当重发次数达到规定的最大次数后，会停止对该客户端的802.1X认证。

【举例】

\# 配置重发SmartOn通知请求报文的最大次数为5。

\<Sysname\> system-view

Sysname dot1x smarton retry 5

【相关命令】

·**display dot1x**

·**dot1x smarton timer supp-timeout**

**802.1X \-- 802.1X配置命令 \-- dot1x smarton switchid**

------------------------------------------------------------------------

**[dot1x smarton switchid**]命令用来配置SmartOn的Switch ID。

**[undo dot1x smarton switchid**]命令用来恢复缺省情况。

【命令】

**[dot1x smarton switchid ***switch-string*]

**[undo dot1x smarton switchid**]

【缺省情况】

未配置SmartOn的Switch ID。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[switch-string*]：可显示的交换机ID字符串，其长度的取值范围为1～30，区分大小写。

【使用指导】

使能了SmartOn功能的端口上，需要验证802.1X客户端发送的EAP-Response/Notification报文中携带的Switch ID字符串，只有与本命令配置的值相同，客户端802.1X的认证才能继续进行。

【举例】

\# 配置SmartOn的Switch ID为abc。

\<Sysname\> system-view

Sysname dot1x smarton switchid abc

【相关命令】

·**display dot1x**

·**dot1x smarton**

·**dot1x smarton password**

**802.1X \-- 802.1X配置命令 \-- dot1x smarton timer supp-timeout**

------------------------------------------------------------------------

**[dot1x smarton timer supp-timeout**]命令用来配置SmartOn通知请求超时定时器时长。

**[undo dot1x smarton timer supp-timeout**]命令用来恢复缺省情况。

【命令】

**[dot1x smarton timer supp-timeout** *supp-timeout-value*]

**[undo dot1x smarton timer supp-timeout**]

【缺省情况】

SmartOn通知请求超时定时器时长为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[supp-timeout-value*]：SmartOn通知请求超时[定时器的值，取值范围为]10～120，单位为秒。

【使用指导】

设备向客户端发送EAP-Request/Notification报文后，会开启通知请求超时定时器等待客户端响应EAP-Response/Notification报文，若定时器超时后客户端仍未回复，则设备会重发EAP-Request/Notification报文，并重新启动定时器。当重发次数达到规定的最大次数（**dot1x smarton retry**）后，会停止对该客户端的802.1X认证。

【举例】

\# 配置SmartOn定时器时长为20秒。

\<Sysname\> system-view

Sysname dot1x smarton timer supp-timeout 20

【相关命令】

·**display dot1x**

·**dot1x smarton retry**

**802.1X \-- 802.1X配置命令 \-- dot1x timer**

------------------------------------------------------------------------

**[dot1x** **timer**]命令用来配置802.1X的定时器参数。

**[undo dot1x** **timer**]命令用来将指定的定时器恢复为缺省情况。

【命令】

**[dot1x timer **[{ **ead-timeout** *ead-timeout-value* \| **handshake-period** *handshake-period-value* \| **quiet-period** *quiet-period-value* \| **reauth-period** *reauth-period-value* \| **server-timeout** *server-timeout-value* \| **supp-timeout** *supp-timeout-value* \| **tx-period** *tx-period-value* }]]

**[undo dot1x timer **[{ **ead-timeout** \| **handshake-period** \| **quiet-period** \| **reauth-period** \| **server-timeout** \| **supp-timeout** \| **tx-period** }]]

【缺省情况】

握手定时器的值为15秒，EAD超时定时器的值为30分钟，静默定时器的值为60秒，周期性重认证定时器的值为3600秒，认证服务器超时定时器的值为100秒，客户端认证超时定时器的值为30秒，用户名请求超时定时器的值为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ead-timeout-value*]：EAD超时定时器的值，取值范围为1～1440，单位为分钟。

**[handshake-period**]* handshake-period-value*：握手定时器的值，取值范围为5～1024，单位为秒。

**[quiet-period**]* quiet-period-value*：静默定时器的值，取值范围为10～120，单位为秒。

**[reauth-period**]* reauth-period-value*：周期性重认证定时器的值，取值范围为60～7200，单位为秒。

**[server-timeout**]* server-timeout-value*：认证服务器超时定时器的值，取值范围为100～300，单位为秒。

**[supp-timeout**]* supp-timeout-value*：客户端认证超时定时器的值，取值范围为1～120，单位为秒。

**[tx-period **]*tx-period-value*：用户名请求超时定时器的值，取值范围为10～120，单位为秒。

【使用指导】

802.1X认证过程受以下定时器的控制：

·握手定时器（**handshake-period**）：此定时器是在用户认证成功后启动的，设备端以此间隔为周期发送握手请求报文，以定期检测用户的在线情况。如果配置发送次数为N，则当设备端连续N次没有收到客户端的响应报文，就认为用户已经下线。

·静默定时器（**quiet-period**）：对用户认证失败以后，设备端需要静默一段时间（该时间由静默定时器设置），在静默期间，设备端不对802.1X认证失败的用户进行802.1X认证处理。

·周期性重认证定时器（**reauth-period**）：端口下开启了周期性重认证功能（通过命令**dot1x re-authenticate**）后，设备端以此间隔为周期对端口上的在线用户发起重认证。对于已在线的802.1X用户，要等当前重认证周期结束并且认证通过后才会按新配置的周期进行后续的重认证。

·认证服务器超时定时器（**server-timeout**）：当设备端向认证服务器发送了RADIUS Access-Request请求报文后，设备端启动**server-timeout**定时器，若在该定时器设置的时长内，设备端没有收到认证服务器的响应，设备端将重发认证请求报文。

·客户端认证超时定时器（**supp-timeout**）：当设备端向客户端发送了EAP-Request/MD5 Challenge请求报文后，设备端启动此定时器，若在该定时器设置的时长内，设备端没有收到客户端的响应，设备端将重发该报文。

·用户名请求超时定时器（**tx-period**）：当设备端向客户端发送EAP-Request/Identity请求报文后，设备端启动该定时器，若在该定时器设置的时长内，设备端没有收到客户端的响应，则设备端将重发认证请求报文。另外，为了兼容不主动发送EAPOL-Start连接请求报文的客户端，设备会定期组播EAP-Request/Identity请求报文来检测客户端。**tx-period**定义了该组播报文的发送时间间隔。

需要注意的是，一般情况下，用户无需修改定时器的值，除非在一些特殊或恶劣的网络环境下，可以使用该命令调节交互进程。修改后的定时器值，可立即生效。

【举例】

\# 设置认证服务器的超时定时器时长为150秒。

\<Sysname\> system-view

Sysname dot1x timer server-timeout 150

【相关命令】

·**display dot1x**

**802.1X \-- 802.1X配置命令 \-- dot1x unicast-trigger**

------------------------------------------------------------------------

**[dot1x unicast-trigger**]命令用来开启端口上的802.1X的单播触发功能。

**[undo dot1x unicast-trigger**]命令用来关闭802.1X的单播触发功能。

【命令】

**[dot1x unicast-trigger**]

**[undo dot1x unicast-trigger**]

【缺省情况】

802.1X的单播触发功能处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

单播触发功能开启后，当端口收到源MAC未知的报文时，主动向该MAC地址发送单播认证报文来触发认证。若设备端在设置的客户端认证超时时间内（该时间由**dot1x timer supp-timeout**设置）没有收到客户端的响应，则重发该报文（重发次数由**dot1x retry**设置）。

【举例】

\# 在端口GigabitEthernet1/0/1上开启802.1X的单播触发功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1x unicast-trigger

【相关命令】

·**display dot1x**

·**dot1x multicast-trigger**

·**dot1x retry**

·**dot1x timer**

**802.1X \-- 802.1X配置命令 \-- reset dot1x guest-vlan**

------------------------------------------------------------------------

**[reset dot1x guest-vlan**]命令用来清除Guest VLAN内802.1X用户，使其退出Guest VLAN。

【命令】

**[reset dot1x guest-vlan** **interface** *interface-type interface-number* [ **mac-address** *mac-address* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：表示使指定端口上的用户退出Guest VLAN，*interface-type interface-number*为端口类型和端口编号。

**[mac-address** *mac-address*]：表示使指定 MAC地址的用户退出Guest VLAN。

【举例】

\# 在端口GigabitEthernet1/0/1上使得MAC地址为1-1-1的802.1X用户退出Guest VLAN。

\<Sysname\> reset dot1x guest-vlan interface gigabitethernet 1/0/1 mac-address 1-1-1

【相关命令】

·**dot1x guest-vlan**

**802.1X \-- 802.1X配置命令 \-- reset dot1x statistics**

------------------------------------------------------------------------

**[reset dot1x******statistics**]命令用来清除802.1X的统计信息。

【命令】

**[reset dot1x******statistics****[ **ap** *ap-name* [ **radio** *radio-id*  \| **interface** *interface-type interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ap** *ap-name*]：清除指定AP的所有802.1X统计信息，*ap-name*表示AP的名称，为1～64个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[radio** *radio-id*]：清除指定AP的所有的802.1X统计信息，*radio-id*表示Radio编号，取值范围与设备型号有关。如果不指定该参数，则清除指定AP的所有Radio的802.1X统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface** *interface-type interface-number*]：清除指定端口上的802.1X统计信息，*interface-type interface-number*为端口类型和端口编号。

【使用指导】

如果不指定任何参数，则清除所有802.1X统计信息。

【举例】

\# 清除端口GigabitEthernet1/0/1上的802.1X统计信息。

\<Sysname\> reset dot1x statistics interface gigabitethernet 1/0/1

【相关命令】

·**display dot1x**

