<!-- CMD-INDEX
  client forwarding-mode（仅AC）         | 无线服务模板视图         | L16
  display wlan client                 | 任意视图             | L74
  display wlan service-template       | 任意视图             | L482
  service-template                    |                  | L842
  service-template enable             | 无线服务模板视图         | L928
  ssid                                | 无线服务模板视图         | L970
  vlan                                | 无线服务模板视图         | L1018
  wlan service-template               | 系统视图             | L1068
  client forwarding-location          | 无线服务模板视图         | L1114
  broadcast-probe reply (仅AC)         | AP视图             | L1166
  client idle-timeout                 | AP视图             | L1210
  client keep-alive                   | AP视图             | L1256
-->

**WLAN接入 \-- WLAN接入配置命令 \-- client forwarding-mode（仅AC）**

------------------------------------------------------------------------

!(WLAN接入命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[client forwarding-mode**]命令用配置客户端的数据报文在AP本地转发。

**[undo client forwarding-mode local**]命令用来恢复缺省情况。

【命令】

**[client forwarding-mode local ** **vlan** { *vlan-id1*  **to** *vlan-id2*  } ]

**[undo client forwarding-mode local**]

【缺省情况】

客户端的数据转发模式为集中转发。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id1*** to** *vlan-id2*]：指定VLAN的客户端的数据报文在AP本地转发。*vlan-id*的取值范围为1～4094。如果未指定本参数，则表示所有VLAN的客户端数据报文均在AC进行集中转发。

【使用指导】

·本命令只能在无线服务模板处于关闭状态下配置。

·在AC/FitAP的组网情况下，可以在AC上将客户端的数据报文转发模式配置成集中转发模式或者本地转发模式。

¡若转发模式为集中转发时，客户端的数据流量由AP通过CAPWAP隧道透传到AC，由AC转发数据报文。

¡若转发模式为本地转发时，客户端的数据流量直接由AP进行转发。将转发位置配置在AP上在保持了AC/Fit AP架构在安全、管理等方面的优势的前提下，缓解了AC的数据转发压力。

¡本地转发可以基于VLAN进行配置，即只有处于指定VLAN的客户端，才在AP本地转发其数据流量。

【举例】

\# 配置无线服务模板service1的客户端的转发模式本地转发模式。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client forwarding-mode local

**WLAN接入 \-- WLAN接入配置命令 \-- display wlan client**

------------------------------------------------------------------------

**[display wlan client**]命令用来查看客户端的信息。

【命令】

AC设备：

**[display wlan client**  **ap** *ap-name* [ **radio** *radio-id*  \| **mac-address** *mac-address* \| **service-template** *service-template-name* ]  **verbose** ]

FAT AP设备：

**[display wlan client**  [ **interface wlan-radio** *interface-num*ber \| **mac-address** *mac-address* \| **service-template** *service-template-name* ]  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ap**] *ap-nam*e：显示连接到指定AP的客户端信息。为1～63个字符的字符串，不区分大小写。（仅AC）

**[radio** *radio-id*]：显示连接到指定射频的客户端信息。取值范围为1～4。如果未指定本参数，表示显示连接到指定AP的客户端信息。（仅AC）

**[wlan-radio ***interface-number*]：显示连接到指定射频接口的客户端信息。（仅FAT AP）

**[mac-address **]*mac-address*：显示指定MAC地址的客户端信息。

**[service-template**] *service-template-name*：显示连接到指定无线服务模板的客户端信息，为1～63个字符的字符串，不区分大小写。

**[verbose**]：显示客户端的详细信息。如果未指定本参数，表示显示客户端的简要信息。

【举例】

\# 显示所有客户端的简要信息。

\<Sysname\> display wlan client

Total number of clients: 3

MAC address    Username            APID/RID  IP address                VLAN ID

000f-e265-6400 N/A                    1/1    1.1.1.1                   300

000f-e265-6401 user                1024/1    3.0.0.3                   300

000f-e265-6402 abcde(mailto:mac@h3c.com)                102/1    FE:11:12:03::11:25:13     300

表1-1 display wlan client命令显示信息描述表

字段

描述

MAC address

客户端的MAC地址

Username

客户端的用户名，若客户端采用802.1X认证或MAC地址认证，则显示认证使用的用户名，若客户端不进行802.1X认证或MAC地址认证，则显示为N/A

需要注意的是，如果客户端采用Portal认证方式，Username字段不会显示客户端的Portal用户名

APID/RID

客户端的关联AP的ID及Radio的ID

IP address

客户端的IP地址

VLAN ID

客户端的所属VLAN

\# 显示所有客户端的详细信息。

\<Sysname\> display wlan client verbose

Total number of clients: 3

MAC address                        : 000f-e265-6400

Username                           : N/A

AP ID                              : 1

AP name                            : ap1

Radio ID                           : 1

SSID                               : office

BSSID                              : 0026-3e08-1150

VLAN ID                            : 3

Power save mode                    : Active

Wireless mode                      : 11gn

Channel bandwidth                  : 20MHz

SM power save                      : Disabled

Short GI for 20MHz                 : Not supported

Short GI for 40MHz                 : Supported

Support MCS set                    : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Block Ack (TID 0)                  : In

QoS mode                           : WMM

Listen interval                    : 10

RSSI                               : 62

Rx/Tx rate                         : 130/11

Authentication method              : Open system

Security mode                      : PRE-RSNA

AKM mode                           : None

Cipher suite                       : N/A

User authentication mode           : Bypass

Authorization ACL ID               : 3001(Not effective)

Authorization user profile         : N/A

Roam status                        : Normal

Key derivation                     : SHA1

PMF status                         : Enabled

Online time                        : 0hr 1min 13sec

表1-2 display wlan client verbose命令显示信息描述表

字段

描述

MAC address

客户端的MAC地址

Username

客户端的用户名，若客户端采用802.1X认证或MAC地址认证，则显示认证使用的用户名，若客户端不进行802.1X认证或MAC地址认证，则显示为N/A

需要注意的是，如果客户端采用Portal认证方式，Username字段不会显示客户端的Portal用户名

AP ID

客户端的关联的AP的ID

AP name

接入点名称

Radio ID

客户端关联的Radio的ID

SSID

客户端关联的SSID

BSSID

基本服务集识别码

VLAN ID

客户端的VLAN

Power save mode

客户端节电模式的状态：

·Active：表示客户端处于正常工作状态

·Sleep：表示客户端处于睡眠状态

Wireless mode

无线模式：

·802.11a：表示客户端工作模式为 802.11a

·802.11b：表示客户端工作模式为 802.11b

·802.11g：表示客户端工作模式为 802.11g

·802.11gn：表示客户端工作模式为 802.11gn

·802.11an：表示客户端工作模式为 802.11an

Channel bandwidth

客户端工作的带宽模式：

·20MHz：工作带宽为20MHz

·40MHz：工作带宽为40MHz

SM Power Save

省电模式可以使客户端上只有一个天线处于工作状态，其余天线均处于休眠状态，从而达到节省电源的目的：

·Enabled：省电模式处于开启状态

·Disabled：省电模式处于关闭状态

Short GI for 20MHz

客户端工作带宽为20MHz时，对于Short GI的支持情况：

·Supported：客户端支持Short GI

·Not supported：客户端不支持Short GI

Short GI for 40MHz

客户端工作带宽为40MHz时，对于Short GI的支持情况：

·Supported：客户端支持Short GI

·Not supported：客户端不支持Short GI

Support MCS set

客户端支持MCS

Block Ack (TID 0)

QoS TID的Block Ack协商结果：

·In：表示上行数据报文支持Block Ack

·Out：表示下行数据报文支持Block Ack

·Both：表示上行和上行数据报文都支持Block Ack

QoS mode

QoS模式：

·N/A：不支持WMM协议

·WMM：支持WMM协议

对于WMM的支持情况，AP和客户端会进行协商。对于只有AP和客户端同时支持WMM时，才能协商成功

Listen interval

处于Sleep模式的客户端定期醒来，接收缓存在AP中的数据帧的时间间隔，间隔时间单位为信标发送时间间隔

RSSI

客户端信号强度指示，该值表明了AP检测到客户端的信号强度

Rx/Tx rate

客户端发送/接收报文的速率（包括数据、管理和控制报文）

Authentication method

链路层认证方法：

·Open system：开放系统认证

·Shared key：共享密钥认证

Security mode

安全模式：

·RSN：信标和探查响应帧携带RSN IE

·WPA：信标和探查响应帧携带WPA IE

·PRE-RSN：信标和探查响应帧不携带RSN IE或WPA IE

AKM mode

身份认证与密钥管理模式：

·802.1X：表示身份认证与密钥管理模式是802.1X方式

·PSK：表示身份认证与密钥管理模式是PSK方式

Cipher suite

加密套件：

·N/A：明文方式，不加密

·WEP40：使用WEP40加密套件

·WEP104：使用WEP104加密套件

·WEP128：使用WEP128加密套件

·CCMP：使用AES-CCMP加密套件

·TKIP：使用TKIP加密套件

User authentication mode

用户认证模式：

·Bypass：不做用户认证

·MAC：MAC认证

·802.1X：802.1X认证

·OUI ：OUI认证

Authorization ACL ID

授权ACL对应的ACL编号：

·授权ACL生效，则显示ACL编号

·授权ACL未生效，则显示ACL编号 + Not effective

·不配置授权ACL，显示N/A

Authorization user profile

授权User profile名称：

·如果下发授权User Profile生效，显示Authorization User Profile名称

·如果下发授权User Profile未生效，显示Authorization User Profile名称+Not effective

·不配置授权User profile，显示N/A

Roam status

漫游状态：

·Roaming in progress：漫游切换中

·Inter-AC slow roam：AC间慢速漫游

·Inter-AC fast roam：AC间快速漫游

·Intra-AC slow roam：AC内慢速漫游

·Intra-AC fast roam：AC内快速漫游

·Inter-MA slow roam：MA间慢速漫游

·Inter-MA fast roam：MA间快速漫游

·Intra-MA slow roam：MA内慢速漫游

·Intra-MA fast roam：MA内快速漫游

·N/A：客户端正常上线

Key derivation

密钥衍生类型，包括以下几种：

·SHA1：SHA1 Key Derivation

·SHA256：SHA256 Key Derivation

·N/A：不涉及密钥衍生算法

PMF status

保护管理帧状态，包括以下几种：

·Enabled：保护管理帧功能开启

·Disabled：保护管理帧功能关闭

·N/A：不涉及保护管理帧功能

Online time

客户端在线的时间

**WLAN接入 \-- WLAN接入配置命令 \-- display wlan service-template**

------------------------------------------------------------------------

**[display wlan service-template**]命令用来查看无线服务模板信息。

【命令】

**[display wlan service-template ** *service-template-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[service-template-name*]：无线服务模板名字，为1～63个字符的字符串。不区分大小写。如果未指定本参数，则显示所有无线服务模板的信息。

【举例】

\# 显示无线服务模板信息。

\<Sysname\> display wlan service-template

Service template name        : service1

SSID                         : wuxianfuwu

SSID-hide                    : Disabled

Service template status      : Disabled

Maximum clients per BSS      : 64

VLAN ID                      : 1

AKM mode                     : PSK

Security IE                  : RSN

Cipher suite                 : WEP40

WEP key ID                   : 1

TKIP countermeasure time     : 100 sec

PTK lifetime                 : 43200 sec

GTK rekey                    : Enabled

GTK rekey method             : Time-based

GTK rekey time               : 86400 sec

GTK rekey client-offline     : Enabled

User authentication mode     : Central

Authentication mode          : 802.1X

Intrusion protection         : Disabled

Intrusion protection mode    : Temporary-block

Temporary block time         : 180 sec

Temporary service stop time  : 20 sec

Fail VLAN ID                 : 1

Critical VLAN ID             : Not configured

802.1X handshake             : Enabled

802.1X handshake secure      : Disabled

802.1X domain                : my-domain

MAC-auth domain              : Not configured

Max 802.1X users             : 4096

Max MAC-auth users           : 4096

802.1X re-authenticate       : Enabled

Authorization fail mode      : Online

Accounting fail mode         : Online

Authorization                : Permitted

Key derivation               : SHA1

PMF status                   : Optional

表1-3 display wlan service-template命令显示信息描述表

字段

描述

Service template name

当前无线服务模板名称

SSID

客户端关联的SSID

SSID-hide

SSID隐藏

·Disabled：启用SSID通告

·Enabled：禁用SSID通告

Service template status

无线服务模板状态：

·Disabled：无线服务模板处于关闭状态

·Enabled：无线服务模板处于开启状态

Maximum clients per BSS

一个BSS中能够连接的最大客户端数

VLAN ID

无线服务模板配置的VLAN ID

AKM mode

身份认证与密钥管理模式：

·802.1X：以802.1X作为身份认证与密钥管理模式

·PSK：以PSK作为身份认证与密钥管理模式

Security IE

安全IE类型：

·RSN：RSN类型的IE

·WPA：WPA类型的IE

Cipher suite

加密套件：

·WEP40：使用WEP40作为加密套件

·WEP104：使用WEP104作为加密套件

·WEP128：使用WEP128作为加密套件

·TKIP：使用TKIP作为加密套件

·CCMP：使用CCMP作为加密套件

WEP key ID

WEP密钥ID

TKIP countermeasure time

TKIP反制策略的时间，0表示不启动反制策略

PTK life time

PTK的生存时间

GTK rekey

GTK更新功能状态：

·Enabled：开启状态

·Disabled：关闭状态

GTK rekey method

GTK更新方法：

·Time-based：基于时间更新

·Packet-based：基于报文数更新

GTK rekey time

GTK更新的时间间隔

GTK rekey packets

触发GTK更新的最大报文数量

GTK rekey client-offline

客户端离线更新功能状态：

·Enabled：开启状态

·Disabled：关闭状态

User authentication mode

用户认证点模式：

·Central：集中式

·Split：分离式

Authentication mode

认证模式，包括以下几种：

·Bypass：不认证模式

·MAC：只进行MAC地址认证

·MAC-or-802.1X：先进行MAC地址认证，如果失败在进行802.1X认证

·802.1X：只进行802.1X认证

·802.1X-or-MAC：先进行802.1X认证，如果失败，再进行MAC地址认证

·OUI-or-802.1X：先进行OUI认证，如果失败，再进行802.1X认证

Intrusion protection

入侵检测功能使能状态：

·Enabled：入侵检测功能处于开启状态

·Disabled：入侵检测功能处于关闭状态

Intrusion protection mode

入侵检测特性模式，包括以下三种：

·Temporary-block：表示临时将用户MAC加入阻止MAC列表中

·Service-stop：表示直接关闭对应BSS上的所有服务，直到重启该BSS

·Temporary-service-stop：表示临时关闭收到非法报文的BSS所提供的接入服务

Temporary block time

临时阻塞非法入侵用户的时长，单位为秒

Temporary service stop time

临时关闭BSS服务时长，单位为秒

Fail VLAN ID

认证失败的VLAN ID。未配置，则显示"Not configured"

Critical VLAN ID

认证服务器不可达VLAN。未配置，则显示"Not configured"

802.1X handshake

802.1X握手功能开启状态

·Enabled：开启状态

·Disabled：关闭状态

802.1X handshake secure

802.1X安全握手功能开启状态

·Enabled：开启状态

·Disabled：关闭状态

802.1X domain

802.1X认证域的域名。未配置，则显示"Not configured"

MAC-auth domain

MAC地址认证域的域名。未配置，则显示"Not configured"

Max 802.1X users

802.1X认证的最大用户数

Max MAC-auth users

MAC地址认证的最大用户数

802.1X re-authenticate

802.1X重认证功能

·Enabled：开启状态

·Disabled：关闭状态

Authorization fail mode

授权失败处理模式包括以下两种模式：

·Offline：强制下线模式

·Online：非强制下线模式

Accounting fail mode

计费请求失败处理模式包括以下两种模式：

·Offline：下线模式

·Online：非下线模式

Authorization

服务器的授权信息：

·Permitted：应用RADIUS服务器或本地设备下发的授权信息

·Ignored：忽略RADIUS服务器或本地设备下发的授权信息

Key derivation

密钥衍生类型，包括以下几种：

·SHA1：表示使用SHA1算法衍生密钥

·SHA256：表示使用SHA256算法衍生密钥

·SHA1-AND-SHA256：表示使用SHA1 and SHA256算法衍生密钥

PMF status

保护管理帧状态，包括以下几种：

·Disabled：保护管理帧功能关闭

·Optional：保护管理帧功能可选

·Mandatory：保护管理帧功能强制

**WLAN接入 \-- WLAN接入配置命令 \-- service-template**

------------------------------------------------------------------------

AC设备：

**[service-template**]命令用来将无线服务模板绑定到当前Radio上。

**[undo service-template**]命令用来解除当前Radio与无线服务模板的绑定关系。

FAT AP设备：

**[service-template**]命令用来将无线服务模板绑定到当前WLAN射频接口上。

**[undo service-template**]命令用来解除当前WLAN射频接口上与无线服务模板的绑定关系。

【命令】

AC设备：

**[service-template ***service-template-name *[[ **vlan** *vlan-id \|* **vlan-group** *vlan-group-name* ]]]

**[undo service-template ***service-template-name *]

FAT AP设备：

**[service-template ***service-template-name*]

**[undo service-template ***service-template-name*]

【缺省情况】

未绑定无线服务模版

【视图】

AC设备：Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[service-template-name*]：无线服务模板名字，为1～63个字符的字符串，不区分大小写。

**[vlan*** vlan-id*]：无线服务模板绑定Radio时绑定的VLAN ID，取值范围为1～4094。

**[vlan-group*** vlan-group-name*]：指定无线服务模板绑定Radio时绑定的VLAN组，为1～16个字符的字符串。

【使用指导】

·当只指定无线服务模板名字时，该无线服务模板须先被创建才可完成绑定。

·当指定VLAN ID时，该VLAN须已经创建才可完成绑定，否则绑定失败。

·VLAN组由**vlan-group**命令创建，有关该命令的详细介绍，请参见"二层技术-以太网交换配置指导"中的"VLAN"。

【举例】

AC设备：

\# 将无线服务模板service1绑定到Radio1上，并绑定VLAN组vg1。

\<Sysname\> system-view

Sysname wlan ap ap1

Sysname-ap-ap1 radio 1

Sysname-ap-ap1-radio-1 service-template service1 vlan-group vg1

FAT AP设备：

\# 将无线服务模板service1绑定到WLAN射频接口1上。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-wlan-radio-1 service-template service1

**WLAN接入 \-- WLAN接入配置命令 \-- service-template enable**

------------------------------------------------------------------------

**[service-template enable**]命令用来打开无线服务模板。

**[undo service-template enable**]命令用来关闭无线服务模板。

【命令】

**[service-template enable**]

**[undo service-template enable**]

【缺省情况】

无线服务模板处于关闭状态。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

若AC上所能创建的BSS（基本服务集）已达上限，则不能打开其它处于关闭状态的无线服务模板。

【举例】

\# 打开无线服务模板开关。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 service-template enable

**WLAN接入 \-- WLAN接入配置命令 \-- ssid**

------------------------------------------------------------------------

**[ssid**]命令用来在无线服务模板视图下配置SSID。

**[undo ssid**]命令用来删除当前无线服务模板的SSID。

【命令】

**[ssid ***ssid-name*]

**[undo ssid**]

【缺省情况】

未配置SSID。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ssid-name*]：指定无线服务模板的SSID，为1～32个字符的字符串，区分大小写。

【使用指导】

·本命令只能在无线服务模板处于关闭状态下配置。

·SSID的名称应该尽量具有唯一性。

【举例】

\# 设置SSID为lynn。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 ssid lynn

**WLAN接入 \-- WLAN接入配置命令 \-- vlan**

------------------------------------------------------------------------

**[vlan**]命令用来在无线服务模板下配置VLAN。

**[undo vlan**]命令用来恢复缺省情况。

【命令】

**[vlan** *vlan-id*]

**[undo vlan**]

【缺省情况】

无线服务模板的VLAN为1。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：指定无线服务模板的VLAN ID，取值范围为1～4094。

【使用指导】

·本命令只能在无线服务模板处于关闭状态下配置。

·无线服务模板配置VLAN后，客户端在该服务模板上线后会被加入此VLAN。

·无线服务模板配置VLAN时，若指定的VLAN没有创建则配置失败。

【举例】

\# 配置基于服务模板的VLAN。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 vlan 2

**WLAN接入 \-- WLAN接入配置命令 \-- wlan service-template**

------------------------------------------------------------------------

**[wlan service-template**]命令用来创建无线服务模板。

**[undo wlan service-template**]命令用来删除无线服务模板。

【命令】

**[wlan service-template **]*service-template-name*

**[undo wlan service-template **]*service-template-name*

【缺省情况】

未创建无线服务模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[service-template-name*]：无线服务模板名字，为1～63个字符的字符串。不区分大小写。

【使用指导】

·创建无线服务模板时，如果输入的无线服务模板已经存在，则直接进入该视图。

·删除无线服务模板时，如果指定的无线服务模板映射到射频，则在解除映射之前不能删除此无线服务模板。

【举例】

\# 创建无线服务模板service1。

\<Sysname\> system-view

Sysname wlan service-template service1

**WLAN接入 \-- WLAN接入配置命令 \-- client forwarding-location**

------------------------------------------------------------------------

**[client forwarding-location**]命令用来配置客户端数据报文的转发位置。

**[undo client forwarding-location**]命令用来恢复缺省情况。

【命令】

**[client forwarding-location **[{ **ac** \| **ap** [ **vlan** { *vlan-start* [ **to** *vlan-end* ] } ] \| **mac** }]]

**[undo client forwarding-location**]

【缺省情况】

客户端数据报文转发位置在AC上。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ac**]：配置客户端数据报文的转发位置在AC上。

**[ap**]：配置客户端数据报文的转发位置在AP上。

**[vlan ***vlan-start ***to ***vlan-end*]：配置指定VLAN的客户端在AP上转发数据报文。若未配置本参数，表示所有VLAN的客户端数据报文的转发位置都在AP上。

**[mac**]：配置客户端数据报文的转发位置在MAC上。

【使用指导】

本命令只能在无线服务模板处于关闭状态时配置。

【举例】

\# 配置无线客户端的数据报文转发位置在AP上。

\<Sysname\> system-view

Sysname wlan service-template s1

Sysname-wlan-st-s1 user-forward location ap

**WLAN接入 \-- WLAN接入配置命令 \-- broadcast-probe reply (仅AC)**

------------------------------------------------------------------------

**[broadcast-probe reply**]命令用来使能AP回复广播Probe request报文功能**。**

**[undo broadcast-probe reply**]命令用来禁止AP回复广播Probe request报文。

【命令】

**[broadcast-probe reply**]

**[undo broadcast-probe reply**]

【缺省情况】

AP回应广播Probe request报文。

【视图】

AP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

广播Probe request报文即报文中不携带服务的SSID，AP收到广播报文后，将AP提供的所有服务的信息封装在Probe response报文中，回应给客户端。

配置不回应客户端的广播Probe request报文，可以减少AP回应的Probe response报文。

【举例】

\# 在ap1下配置AP不回应广播Probe request报文。

\<Sysname\> system-view

Sysname wlan ap ap1 model wa2620i-AGN

Sysname-wlan-ap-ap1 undo broadcast-probe reply

**WLAN接入 \-- WLAN接入配置命令 \-- client idle-timeout**

------------------------------------------------------------------------

**[client idle-timeout**]命令用来配置AP和客户端之间连接允许的最大空闲时间。

**[undo client idle-timeout**]命令用来恢复缺省情况。

【命令】

**[client idle-timeout*** interval*]

**[undo client idle-timeout**]

【缺省情况】

AP和客户端之间连接允许的最大空闲时间为3600秒。

【视图】

AP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：AP和客户端之间连接允许的最大空闲时间，取值范围为60～86400，单位为秒。

【使用指导】

当客户端处于空闲状态，即客户端与AP无任何报文交互，当达到最大空闲时间时，AP会自动与客户端断开连接。

【举例】

\# 设置AP和客户端之间连接允许的最大空闲时间为2000秒。

\<sysname\> system-view

sysname wlan ap ap1 model WA2620-AGN

sysname-wlan-ap-ap1 client idle-timeout 2000

**WLAN接入 \-- WLAN接入配置命令 \-- client keep-alive**

------------------------------------------------------------------------

**[client keep-alive**]命令用来配置客户端保活时间。

**[undo client keep-alive**]命令用来恢复缺省情况。

【命令】

**[client keep-alive*** interval*]

**[undo client keep-alive**]

【缺省情况】

客户端保活功能处于关闭状态。

【视图】

AP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：客户端保活时间，取值范围为3～1800，单位为秒。

【使用指导】

·AP会定期给客户端发送空数据报文，以确认其是否在线。如果在保活时间内未收到客户端回应的ACK报文，则断开客户端与AP的连接。

·保活机制通常用来检测客户端是否在线。导致客户端异常离线原因有电源故障、系统崩溃等。

【举例】

\# 设置客户端保活时间为20秒。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA2100

Sysname-wlan-ap-ap1 client keep-alive 20
