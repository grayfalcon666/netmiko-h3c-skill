
**MAC地址认证 \-- MAC地址认证配置命令 \-- display mac-authentication**

------------------------------------------------------------------------

**[display mac-authentication**]命令用来显示MAC地址认证的相关信息，主要包括全局及端口的配置信息、认证报文统计信息以及认证用户信息。

【命令】

**[display mac-authentication****[ **ap** *ap-name* [ **radio** *radio-id*  \| **interface** *interface-type interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ap** *ap-name*]：显示指定AP的所有MAC地址认证的详细信息，*ap-name*表示AP的名称，为1～64个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[radio** *radio-id*]：显示指定Radio的所有的MAC地址认证的详细信息，*radio-id*表示Radio编号，取值范围与设备型号有关。如果不指定该参数，则显示指定AP的所有Radio的MAC地址认证的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface** *interface-type interface-number*]：显示全局及指定端口的MAC地址认证相关信息，*interface-type interface-number*为端口类型和端口编号。若指定的端口上未使能MAC地址认证，则不显示该端口任何信息。

【使用指导】

如果不指定任何参数，则显示所有在线MAC地址认证的详细信息，先显示有线MAC地址认证的信息，再显示无线MAC地址认证的信息。

【举例】

\# 显示MAC地址认证信息。

\<Sysname\> display mac-authentication

Global MAC authentication parameters:

   MAC authentication     : Enabled

   Username format        : MAC address in lowercase(xxxxxxxxxxxx)

           Username       : mac

           Password       : Not configured

   Offline detect period  : 300 s

   Quiet period           : 60 s

   Server timeout         : 100 s

   Authentication domain  : Not configured, use default domain

 Max MAC-auth users       : 1024 per slot

Online MAC-auth wired users    : 1

 Online MAC-auth wireless users : 2

 Silent MAC users:

          MAC address       VLAN ID  From port               Port index

          0001-0000-0001    100      GigabitEthernet1/0/2    21

          0001-0000-0002    2        GigabitEthernet1/0/3    20

          0001-0000-0002    12       GigabitEthernet1/0/4    301

 GigabitEthernet1/0/1  is link-up

   MAC authentication         : Enabled

   Authentication domain      : Not configured

   Auth-delay timer           : Enabled

       Auth-delay period      : 60 s

   Re-auth server-unreachable : Logoff

   Guest VLAN                 : 100

   Critical VLAN              : Not configured

   Host mode                  : Multiple VLAN

   Max online users           : 256

   Authentication attempts    : successful 2, failed 3

   Current online users       : 1

          MAC address       Auth state

          0001-0000-0001    Unauthenticated

AP name: AP1  Radio ID: 1  SSID: wlan_maca_ssid

   BSSID                      : 1111-1111-1111

MAC authentication         : Enabled

   Authentication domain      : Not configured

   Max online users           : 256

   Authentication attempts    : successful 1, failed 0

   Current online users       : 2

          MAC address       Auth state

          0001-0000-0002    Authenticated

          0001-0000-0003    Unauthenticated

表1-1 display mac-authentication命令显示信息描述表

字段

描述

Global MAC authentication parameters

全局MAC地址认证参数

MAC authentication

MAC地址认证的开启状态

该功能的生效情况与设备的型号有关，请以设备的实际情况为准

Username format

MAC地址认证使用的用户名格式，有以下两种情况：

·若采用MAC地址形式，则显示具体的用户名格式以及是否带连字符、字母是否大小写，例如本例中"MAC address in lowercase(xxxxxxxxxxxx)"，它表示用户名格式为不带连字符的MAC地址，其中字母为小写

·若采用固定用户名格式，则显示"Fixed account"

Username:

用户名

·采用MAC地址格式时，该值显示为"mac"，无实际意义，仅表示采用MAC地址作为用户名和密码

·采用固定用户名格式时，该值为配置的用户名（缺省为mac）

Password:

用户名的密码

·采用MAC地址格式时，该值显示为"Not configured"

·采用固定用户名格式时，配置的值将显示为\*\*\*\*\*\*

Offline detect period

下线检测定时器的值

Quiet period

静默定时器的值

Server timeout

服务器连接超时定时器的值

Authentication domain

系统视图下指定的MAC地址认证用户使用的认证域

Max MAC-auth users

每单板能够支持的最大MAC地址认证用户数

Online MAC-auth wired users

在线有线用户数

Online MAC-auth wireless users

在线无线用户数

Silent MAC users

静默用户信息

MAC address

静默用户的MAC地址

VLAN ID

静默用户所在的VLAN

From port

静默用户接入的端口名称

Port index

静默用户接入的端口索引号

GigabitEthernet1/0/1 is link-up

端口GigabitEthernet1/0/1的链路状态

MAC authentication

当前端口的MAC地址认证开启状态

Authentication domain

端口上指定的MAC地址认证用户使用的认证域

Auth-delay timer

MAC地址认证延迟功能的开启状态

Auth-delay period

配置的认证延迟时间

Re-auth server-unreachable

重认证时服务器不可达对MACA地址认证的在线用户采取的动作

Guest VLAN

端口配置的Guest VLAN

Critical VLAN

端口配置的Critical VLAN

Host mode

相同MAC地址用户的工作模式

·Single VLAN：不允许相同MAC地址用户在属于不同VLAN的相同接口再次接入

·Multiple VLAN：允许相同MAC地址用户在属于不同VLAN的相同接口再次接入

Max online users

本端口最多可容纳的接入用户数

Authentication attempts: successful 1, failed 0

端口上MAC地址认证的统计信息，包括认证通过的次数和认证失败的次数

MAC address

接入用户的MAC地址

Auth state

接入用户的状态，包括以下两种：

·Authenticated：认证成功

·Unauthenticated：认证失败

AP name

AP名称

Radio ID

Radio编号

SSID

服务集标识符

BSSID

基本服务集标识符

**MAC地址认证 \-- MAC地址认证配置命令 \-- display mac-authentication connection**

------------------------------------------------------------------------

**[display mac-authentication connection**]命令用来显示当前MAC地址认证在线用户的详细信息。

【命令】

集中式设备：

**[display mac-authentication connection **[ **ap** *ap-name* [ **radio** *radio-id*  \| **interface** *interface-type* *interface-number* \| **user-mac** *mac-addr* \| **user-name** *user-name* ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mac-authentication connection **[ **ap** *ap-name* [ **radio** *radio-id*  \| **interface** *interface-type* *interface-number* \| **slot** *slot-number* \| **user-mac** *mac-addr* \| **user-name** *user-name* ]]]

分布式设备－IRF模式：

**[display mac-authentication connection **[ **ap** *ap-name* [ **radio** *radio-id*  \| **chassis** *chassis-number* **slot** *slot-number* \| **interface** ** ***interface-type* *interface-number* \| **user-mac** *mac-addr* \| **user-name** *user-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ap** *ap-name*]：显示接入指定AP的所有MAC地址认证用户的信息，*ap-name*表示AP的名称，为1～63个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[radio** *radio-id*]：显示接入指定Radio的所有的MAC地址认证用户的信息，*radio-id*表示Radio编号，取值范围与设备型号有关。如果不指定该参数，则显示AP的所有Radio的MAC地址认证用户的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface ***interface-type interface-number*]：显示指定端口的MAC地址认证用户信息。其中*interface-type interface-number*表示绑定的端口类型和端口编号。

**[slot ***slot-number*]：显示指定单板上的MAC地址认证用户信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的MAC地址认证用户信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的MAC地址认证用户信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的MAC地址认证用户信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的MAC地址认证用户信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[user-mac** *mac-addr*]：显示指定MAC地址的MAC地址认证用户信息。其中*mac-addr*表示用户的MAC地址，格式为H-H-H。

**[user-name ***user-name*]：显示指定用户名的MAC地址认证用户信息。其中*user-name*表示用户名（可包含域名），为1～253个字符的字符串，区分大小写。

【使用指导】

若不指定任何参数，则显示所有端口上的MAC地址认证在线用户信息。（集中式设备）

若不指定任何参数，则显示所有单板上的MAC地址认证在线用户信息。（分布式设备－独立运行模式）

若不指定任何参数，则显示所有成员设备上的MAC地址认证在线用户信息。（集中式IRF设备）

若不指定任何参数，则显示所有成员设备的所有单板上的MAC地址认证在线用户信息。（分布式设备－IRF模式）

【举例】

\# 显示所有MAC地址认证在线用户信息。（集中式设备）

\<Sysname\> display mac-authentication connection

User MAC address: 0015-e9a6-7cfe

Access interface: GigabitEthernet1/0/1

Username: ias

Authentication domain: h3c

Initial VLAN: 1

Authorization untagged VLAN: 100

Authorization ACL ID: 3001

Authorization user profile: N/A

Termination action: Radius-request

Session timeout period: 2 s

Online from: 2013/03/02  13:14:15

Online duration: 0h 2m 15s

User MAC address              : 0015-e9a6-7cfe

AP name                           : ap1

Radio ID                         : 1

SSID                             : wlan_dot1x_ssid

BSSID                         : 0015-e9a6-7cf0

User name                     : ias

Authentication domain         : 1

Initial VLAN                  : 1

Authorization untagged VLAN   : 100

Authorization ACL number      : 3001

Authorization user profile    : N/A

Termination action            : Radius-request

Session timeout period        : 2 sec

Online from                   : 2014/06/02 13:14:15

Online duration               : 0h 2m 15s

Total 1 connection(s) matched

\# 显示所有MAC地址认证在线用户信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display mac-authentication connection

Slot ID: 0

User MAC address: 0015-e9a6-7cfe

Access interface: GigabitEthernet1/0/1

Username: ias

Authentication domain: h3c

Initial VLAN: 1

Authorization untagged VLAN: 100

Authorization ACL ID: 3001

Authorization user profile: N/A

Termination action: Radius-request

Session timeout period: 2 s

Online from: 2013/03/02  13:14:15

Online duration: 0h 2m 15s

User MAC address              : 0015-e9a6-7cfe

AP name                           : ap1

Radio ID                         : 1

SSID                             : wlan_dot1x_ssid

BSSID                         : 0015-e9a6-7cf0

User name                     : ias

Authentication domain         : 1

Initial VLAN                  : 1

Authorization untagged VLAN   : 100

Authorization ACL number      : 3001

Authorization user profile    : N/A

Termination action            : Radius-request

Session timeout period        : 2 sec

Online from                   : 2014/06/02 13:14:15

Online duration               : 0h 2m 15s

Total 1 connections matched.

\# 显示所有MAC地址认证在线用户信息。（分布式设备－IRF模式）

\<Sysname\> display mac-authentication connection

Chassis ID: 1

Slot ID: 0

User MAC address: 0015-e9a6-7cfe

Access interface: GigabitEthernet1/0/1

Username: ias

Authentication domain: h3c

Initial VLAN: 1

Authorization untagged VLAN: 100

Authorization ACL ID: 3001

Authorization user profile: N/A

Termination action: Radius-request

Session timeout period: 2 s

Online from: 2013/03/02  13:14:15

Online duration: 0h 2m 15s

User MAC address              : 0015-e9a6-7cfe

AP name                           : ap1

Radio ID                         : 1

SSID                             : wlan_dot1x_ssid

BSSID                         : 0015-e9a6-7cf0

User name                     : ias

Authentication domain         : 1

Initial VLAN                  : 1

Authorization untagged VLAN   : 100

Authorization ACL number      : 3001

Authorization user profile    : N/A

Termination action            : Radius-request

Session timeout period        : 2 sec

Online from                   : 2014/06/02 13:14:15

Online duration               : 0h 2m 15s

Total 1 connections matched.

表1-2 display mac-authentication connection 命令显示信息描述表

字段

描述

Chassis ID

当前设备在IRF中的成员编号（分布式设备－IRF模式）

Slot ID

单板所在的槽位号{.TableTextChar}（分布式设备－独立运行模式{.TableTextChar}/{.TableTextChar}分布式设备－{.TableTextChar}IRF模式{.TableTextChar}）

Slot ID

当前设备在{.TableTextChar}IRF中的成员编号{.TableTextChar}（集中式{.TableTextChar}IRF设备{.TableTextChar}）

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

认证时所用的ISP域的名称

Initial VLAN

初始的VLAN

Authorization untagged VLAN

授权的untagged VLAN

Authorization ACL ID

授权ACL编号

Authorization user profile

授权用户的User profile名称

Terminate action

服务器下发的终止动作类型：

·Default：会话超时时间到达后，强制用户下线

·Radius-Request：会话超时时间到达后，请求MAC地址认证用户进行重认证

用户采用本地认证时，该字段显示为N/A

Session timeout period

服务器下发的会话超时时间，该时间到达之后，用户所在的会话将会被删除，之后，对该用户所采取的动作，由Terminate action字段的取值决定

用户采用本地认证时，该字段显示为N/A

Online from

MAC认证用户的上线时间

Online duration

MAC认证用户的在线时长

Total 1 connection(s) matched

在线MAC地址认证用户个数

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication**

------------------------------------------------------------------------

**[mac-authentication**]命令用来开启指定端口上或全局的MAC地址认证。

**[undo mac-authentication**]命令用来关闭指定端口上或全局的MAC地址认证。

【命令】

**[mac-authentication**]

**[undo mac-authentication**]

【缺省情况】

所有端口及全局的MAC地址认证都处于关闭状态。

【视图】

系统视图/以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有全局和端口的MAC地址认证均开启后，MAC地址认证配置才能在端口上生效。该配置的生效情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 开启全局的MAC地址认证。

\<Sysname\> system-view

Sysname mac-authentication

\# 开启端口GigabitEthernet1/0/1上的MAC地址认证。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-authentication

【相关命令】

·**display mac-authentication**

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication critical vlan**

------------------------------------------------------------------------

**[mac-authentication critical vlan**]命令用来配置指定端口的MAC地址认证的Critical VLAN，即当MAC用户认证时对应的ISP域下所有认证服务器都不可达的情况下被授权访问Critical VLAN内的资源。

**[undo mac-authentication critical vlan**]命令用来恢复缺省情况**。**

【命令】

**[mac-authentication critical vlan*** critical-vlan-id*]

**[undo mac-authentication critical vlan**]

【缺省情况】

端口上未配置MAC地址认证的Critical VLAN。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[critical-vlan-id*]：端口上指定的Critical VLAN ID，取值范围为1～4094（取值范围与设备型号有关，请以设备的实际情况为准）。该VLAN必须已经创建。

【使用指导】

如果某个VLAN被指定为Super VLAN，则该VLAN不能被指定为某个端口的MAC地址认证的Critical VLAN；同样，如果某个VLAN被指定为某个端口的MAC地址认证的Critical VLAN，则该VLAN不能被指定为Super VLAN。

禁止删除已被配置为Critical VLAN的VLAN，若要删除该VLAN，请先使用命令**undo mac-authentication critica vlan**取消MAC地址认证的Critical VLAN配置。

【举例】

\# 配置端口GigabitEthernet1/0/1的Critical VLAN为VLAN 100 。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-authentication critical vlan 100

【相关命令】

·**display mac-authentication**

·**reset mac-authentication critical-vlan**

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication domain**

------------------------------------------------------------------------

**[mac-authentication domain**]命令用来指定MAC地址认证用户使用的认证域。

**[undo mac-authentication domain**]命令用来恢复缺省情况。

【命令】

**[mac-authentication******domain ***domain-name*]

**[undo mac-authentication******domain**]

【缺省情况】

未指定MAC地址认证用户使用的认证域，使用系统缺省的认证域。缺省认证域的介绍请参见"安全命令参考/AAA"中的命令**domain default******enable**。

【视图】

系统视图/以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：ISP域名，为1～255个字符的字符串，不区分大小写。

【使用指导】

不同视图下指定的认证域的生效范围不同：

·系统视图下指定的认证域对所有开启了MAC地址认证的端口生效。

·以太网接口视图下指定的认证域仅对本端口有效。不同的端口可以指定不同的认证域。

端口上接入的MAC地址认证用户将按照如下先后顺序选择认证域：端口上指定的认证域\--\>系统视图下指定的认证域\--\>系统缺省的认证域。

【举例】

\# 在系统视图下指定MAC地址认证用户使用的认证域为domain1。

\<Sysname\> system-view

Sysname mac-authentication domain domain1

\# 指定端口GigabitEthernet1/0/1上接入的MAC地址认证用户使用的认证域为aabbcc。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-authentication domain aabbcc

【相关命令】

·**display mac-authentication**

·**domain default******enable**（安全命令参考/AAA）

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication guest-vlan**

------------------------------------------------------------------------

**[mac-authentication guest-vlan**]命令用来配置指定端口的MAC地址认证的Guest VLAN，即MAC地址认证失败的用户被授权访问的VLAN。

**[undo mac-authentication guest-vlan**]命令用来恢复缺省情况**。**

【命令】

**[mac-authentication guest-vlan ***guest-vlan-id*]

**[undo mac-authentication guest-vlan**]

【缺省情况】

端口上未配置MAC地址认证的Guest VLAN。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[guest-vlan-id*]：端口上指定的Guest VLAN ID，取值范围为1～4094（取值范围与设备型号有关，请以设备的实际情况为准）。该VLAN必须已经创建。

【使用指导】

如果某个VLAN被指定为Super VLAN，则该VLAN不能被指定为某个端口的MAC地址认证的Guest VLAN；同样，如果某个VLAN被指定为某个端口的MAC地址认证的Guest VLAN，则该VLAN不能被指定为Super VLAN。

禁止删除已被配置为Guest VLAN的VLAN，若要删除该VLAN，请先使用命令**undo mac-authentication guest-vlan**取消MAC地址认证的Guest VLAN配置。

【举例】

\# 配置端口GigabitEthernet1/0/1的Guest VLAN为VLAN 100 。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-authentication guest-vlan 100

【相关命令】

·**display mac-authentication**

·**reset mac-authentication guest-vlan**

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication host-mode**

------------------------------------------------------------------------

**[mac-authentication host-mode multi-vlan**]命令用来指定端口工作在MAC地址认证的多VLAN 模式。

**[undo mac-authentication host-mode**]命令用来恢复缺省情况。

【命令】

**[mac-authentication host-mode multi-vlan**]

**[undo mac-authentication host-mode**]

【缺省情况】

端口工作在MAC地址认证的单VLAN 模式。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

端口工作在多VLAN模式下时，如果相同MAC地址的用户在属于不同VLAN的相同端口再次接入，设备将能够允许用户的流量在新的VLAN内通过，且允许该用户的报文无需重新认证而在多个VLAN中转发。

端口工作在单VLAN模式下时，在用户已上线，且没有被下发授权VLAN情况下，如果此用户在属于不同VLAN的相同端口再次接入，则，设备将让原用户下线，使得该用户能够在新的VLAN内重新开始认证。如果已上线用户被下发了授权VLAN，则此用户在属于不同VLAN的相同端口再次接入时不会被强制下线。

对于接入IP电话类用户的端口，指定端口工作在MAC地址认证的多VLAN 模式，可避免IP电话终端的报文所携带的VLAN tag发生变化后，因用户流量需要重新认证带来语音报文传输质量受干扰的问题。

【举例】

\# 配置端口GigabitEthernet1/0/1工作在MAC地址认证的多VLAN模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-authentication host-mode multi-vlan

【相关命令】

·**display mac-authentication**

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication max-user**

------------------------------------------------------------------------

![说明](MAC地址认证命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-authentication** **max-user**]命令用来配置端口上最多允许同时接入的MAC地址认证用户数。当接入此端口的MAC地址认证用户数超过最大值后，新接入的用户将被拒绝。

**[undo mac-authentication** **max-user**]命令用来恢复缺省情况。

【命令】

**[mac-authentication** **max-user** *user-number*]

**[undo mac-authentication max-user**]

【缺省情况】

端口上最多允许同时接入的MAC地址认证用户数与设备的型号有关，请以设备的实际情况为准。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[user-number*]：端口允许同时接入的MAC地址认证用户数的最大值，不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【举例】

\# 配置端口GigabitEthernet1/0/1最多允许同时接入32个MAC地址认证用户。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-authentication max-user 32

【相关命令】

·**display mac-authentication**

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication re-authenticate server-unreachable keep-online**

------------------------------------------------------------------------

**[mac-authentication re-authenticate server-unreachable keep-online**]命令用来配置重认证服务器不可达时端口上的MAC地址认证用户保持在线状态。

**[undo mac-authentication re-authenticate server-unreachable**]命令用来恢复缺省情况**。**

【命令】

**[mac-authentication re-authenticate server-unreachable keep-online**]

**[undo mac-authentication re-authenticate server-unreachable**]

【缺省情况】

端口上的MAC地址认证在线用户重认证时，若认证服务器不可达，则会被强制下线。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置端口GigabitEthernet1/0/1上的MAC地址认证在线用户进行重认证时，若服务器不可达，则保持在线状态。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-authentication re-authenticate server-unreachable keep-online

【相关命令】

·**display mac-authentication**

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication timer**

------------------------------------------------------------------------

**[mac-authentication** **timer**]命令用来配置MAC地址认证的定时器参数。

**[undo mac-authentication** **timer**]命令用来恢复缺省情况。

【命令】

**[mac-authentication**[ **timer** { **offline-detect** *offline-detect-value* \| **quiet** *quiet-value* \| **server-timeout** *server-timeout-value* }]]

**[undo mac-authentication**[ **timer** { **offline-detect** \| **quiet** \| **server-timeout** }]]

【缺省情况】

下线检测定时器的值为300秒，静默定时器的值为60秒，服务器超时定时器的值为100秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[offline-detect*** offline-detect-value*]：表示下线检测定时器。其中，*offline-detect-value*表示下线检测定时器的值，取值范围60～65535，单位为秒。

**[quiet** *quiet-value*]：表示静默定时器。其中*quiet-value*表示静默定时器的值，取值范围1～3600，单位为秒。

**[server-timeout*** server-timeout-value*]：表示服务器超时定时器。其中，*server-timeout-value*表示服务器超时定时器的值，取值范围为100～300，单位为秒。

【使用指导】

MAC地址认证过程受以下定时器的控制：

·下线检测定时器（**offline-detect**）：用来设置在线用户空闲超时的时间间隔。若设备在一个下线检测定时器间隔之内，没有收到某在线用户的报文，将切断该用户的连接，同时通知RADIUS服务器停止对其计费。

·静默定时器（**quiet**）：用来设置用户认证失败以后，设备需要等待的时间间隔。在静默期间，设备不对来自认证失败用户的报文进行认证处理，直接丢弃。静默期后，如果设备再次收到该用户的报文，则依然可以对其进行认证处理。

·服务器超时定时器（**server-timeout**）：用来设置设备同RADIUS服务器的连接超时时间。在用户的认证过程中，如果到服务器超时定时器超时时设备一直没有收到RADIUS服务器的应答，则设备将在相应的端口上禁止此用户访问网络。

【举例】

\# 设置服务器超时定时器时长为150秒。

\<Sysname\> system-view

Sysname mac-authentication timer server-timeout 150

【相关命令】

·**display mac-authentication**

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication timer auth-delay**

------------------------------------------------------------------------

**[mac-authentication timer auth-delay**]命令用来开启MAC地址认证延迟功能，并配置MAC地址认证的延时时间。

**[undo mac-authentication timer auth-delay**]命令用来恢复缺省情况。

【命令】

**[mac-authentication timer auth-delay ***time*]

**[undo mac-authentication timer auth-delay**]

【缺省情况】

MAC地址认证延迟功能处于关闭状态，如果用户报文触发MAC地址认证，认证将会立刻开始。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：延迟MAC地址认证的时间，取值范围为1～180，单位为秒。

【使用指导】

端口同时开启了MAC地址认证和802.1X认证的情况下，某些组网环境中希望设备对用户报文先进行802.1X认证。例如，有些客户端在发送802.1X认证请求报文之前，就已经向设备发送了其它报文，比如DHCP报文，因而触发了并不期望的MAC地址认证。这种情况下，就可以开启端口的MAC地址认证延时功能。

开启端口的MAC地址认证延时功能之后，端口就不会在收到用户报文时立即触发MAC地址认证，而是在等待一定的延迟时间之后，再会对之前收到的用户报文进行MAC地址认证。在此认证延迟期间，端口对用户报文的其它认证过程并不受影响。

开启了MAC地址认证延迟功能的接口上不建议同时配置端口安全的模式为**mac-else-userlogin-secure**或**mac-else-userlogin-secure-ext**，否则MAC地址认证延迟功能不生效。端口安全模式的具体配置请参见"安全命令参考"中的"端口安全"。

【举例】

\# 开启MAC地址延迟认证功能，并指定MAC地址认证的延时时间为10秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-authentication timer auth-delay 10

【相关命令】

·**display mac-authentication**

·**port-security port-mode**（安全命令参考/端口安全）

**MAC地址认证 \-- MAC地址认证配置命令 \-- mac-authentication user-name-format**

------------------------------------------------------------------------

![说明](MAC地址认证命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-authentication user-name-format**]命令用来配置MAC地址认证的用户名格式。

**[undo mac-authentication user-name-format**]命令用来恢复缺省情况。

【命令】

**[mac-authentication user-name-format** { **fixed** [ **account** *name*  [ **password** { **cipher** \| **simple** } *password* ] \| **mac-address** [ { **with-hyphen** \| **without-hyphen** } [ **lowercase** \| **uppercase** ] ] }]]

**[undo mac-authentication user-name-format**]

【缺省情况】

使用用户的MAC地址作为用户名和密码，其中字母为小写，且不带连字符"-"。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fixed**]：表示采用固定用户名格式。

**[account** *name*]：指定发送给RADIUS服务器进行认证或者在本地进行认证的用户名。其中*name*为用户名，为1～55个字符的字符串，区分大小写，不能包括字符@，缺省为mac。

**[password**]：指定固定用户名的密码。

**[cipher**]：表示以密文方式设置密码。

**[simple**]：表示以明文方式设置密码。

*[password*]：设置的明文密码或密文密码，区分大小写。明文密码为1～63个字符的字符串；密文密码为1～117个字符的字符串。

**[mac-address**]：表示使用用户的MAC地址作为用户名和密码。

**[with-hyphen**]：带连字符"-"的MAC地址格式，例如xx-xx-xx-xx-xx-xx。

**[without-hyphen**]：不带连字符"-"的MAC地址格式，例如xxxxxxxxxxxx。

**[lowercase**]：MAC地址中的字母为小写。

**[uppercase**]：MAC地址中的字母为大写。

【使用指导】

若指定用户的MAC地址为用户名，则用户密码也为用户的MAC地址。这种情况下，每一个MAC地址认证用户都使用唯一的用户名进行认证，安全性高，但要求认证服务器端配置多个MAC形式的用户帐户。

若指定一个固定的用户名，则表示不论用户的MAC地址为何值，所有用户均使用设备上指定的一个固定用户名和密码作为身份信息进行认证。由于同一个端口下可以有多个用户进行认证，因此这种情况下端口上的所有MAC地址认证用户均使用同一个固定用户名进行认证，服务器端仅需要配置一个用户帐户即可满足所有认证用户的认证需求，适用于接入客户端比较可信的网络环境。

以明文或密文方式设置的密码，均以密文的方式保存在配置文件中。

【举例】

\# 配置MAC地址认证的用户名为abc，密码是明文xyz。

\<Sysname\> system-view

Sysname mac-authentication user-name-format fixed account abc password simple xyz

\# 配置用户的MAC地址为用户名和密码，使用带连字符"-"的MAC地址格式，其中字母大写。

\<Sysname\> system-view

Sysname mac-authentication user-name-format mac-address with-hyphen uppercase

【相关命令】

·**display mac-authentication**

**MAC地址认证 \-- MAC地址认证配置命令 \-- reset mac-authentication critical-vlan**

------------------------------------------------------------------------

**[reset mac-authentication critical-vlan**]命令用来清除Critical VLAN内的MAC地址认证用户。

【命令】

**[reset mac-authentication critical-vlan** **interface** *interface-type interface-number* [ **mac-address** *mac-address* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：表示使指定端口上的用户退出Critical VLAN，*interface-type interface-number*为端口类型和端口编号。

**[mac-address** *mac-address*]：表示使指定 MAC地址的用户退出Critical VLAN。

【举例】

\# 在端口GigabitEthernet1/0/1上使得MAC地址为1-1-1的MAC地址认证用户退出Critical VLAN。

\<Sysname\> reset mac-authentication critical-vlan interface gigabitethernet 1/0/1 mac-address 1-1-1

【相关命令】

·**display mac-authentication**

·**mac-authentication critical vlan**

**MAC地址认证 \-- MAC地址认证配置命令 \-- reset mac-authentication guest-vlan**

------------------------------------------------------------------------

**[reset mac-authentication guest-vlan**]命令用来清除Guest VLAN内的MAC地址认证用户。

【命令】

**[reset mac-authentication guest-vlan** **interface** *interface-type interface-number* [ **mac-address** *mac-address* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：表示使指定端口上的用户退出Guest VLAN，*interface-type interface-number*为端口类型和端口编号。

**[mac-address** *mac-address*]：表示使指定 MAC地址的用户退出Guest VLAN。

【举例】

\# 在端口GigabitEthernet1/0/1上使得MAC地址为1-1-1的MAC地址认证用户退出Guest VLAN。

\<Sysname\> reset mac-authentication guest-vlan interface gigabitethernet 1/0/1 mac-address 1-1-1

【相关命令】

·**display mac-authentication**

·**mac-authentication guest-vlan**

**MAC地址认证 \-- MAC地址认证配置命令 \-- reset mac-authentication statistics**

------------------------------------------------------------------------

**[reset mac-authentication******statistics**]命令用来清除MAC地址认证的统计信息。

【命令】

**[reset mac-authentication statistics** [ **ap** *ap-name* [ **radio** *radio-id*  \| **interface** *interface-type interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ap** *ap-name*]：清除指定AP的所有MAC地址认证统计信息，*ap-name*表示AP的名称，为1～64个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[radio** *radio-id*]：清除指定AP的所有的MAC地址认证统计信息，*radio-id*表示Radio编号，取值范围与设备型号有关。如果不指定该参数，则清除指定AP的所有射频天线下的MAC地址认证统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface ***interface-type interface-number*]：清除指定端口的MAC地址认证统计信息，*interface-type interface-number*为端口类型和端口编号。

【使用指导】

如果不指定任何参数，则清除所有MAC地址认证统计信息。

【举例】

\# 清除以太网端口GigabitEthernet1/0/1上的MAC认证统计信息。

\<Sysname\> reset mac-authentication statistics interface gigabitethernet 1/0/1

【相关命令】

·**display mac-authentication**
