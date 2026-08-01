<!-- CMD-INDEX
  display port-security               | 任意视图             | L22
  display port-security mac-address block | 任意视图             | L242
  display port-security mac-address security | 任意视图             | L488
  port-security authorization ignore  | 以太网接口视图          | L618
  port-security authorization-fail offline | 系统视图             | L666
  port-security enable                | 系统视图             | L712
  port-security intrusion-mode        | 二层以太网接口视图        | L772
  port-security mac-address aging-type inactivity | 二层以太网接口视图        | L830
  port-security mac-address dynamic   | 二层以太网接口视图        | L878
  port-security mac-address security  | 二层以太网接口视图/系统视图   | L928
  port-security mac-move permit       | 系统视图             | L1014
  port-security max-mac-count         | 以太网接口视图          | L1062
  port-security nas-id-profile        | 系统视图/接口视图        | L1122
  port-security ntk-mode              | 以太网接口视图          | L1182
  port-security oui                   | 系统视图             | L1242
  port-security port-mode             | 接口视图             | L1296
  port-security timer autolearn aging | 系统视图             | L1470
  port-security timer disableport     | 系统视图             | L1522
-->

**端口安全 \-- 端口安全配置命令 \-- display port-security**

------------------------------------------------------------------------

**[display port-security**]命令用来显示端口安全的配置信息、运行情况和统计信息。

【命令】

**[display port-security** [ **interface** *interface-type interface-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定端口的端口安全相关信息，*interface-type interface-number*表示端口类型和端口编号

【使用指导】

如果不指定**interface**参数，则显示所有端口的端口安全信息。

【举例】

\# 显示所有端口的端口安全相关状态。

\<Sysname\> display port-security

Port security parameters:

   Port security           : Enabled

   AutoLearn aging time   : 30 min

   Disableport timeout    : 30 s

   MAC move                 : Denied

   Authorization fail     : Offline

   NAS-ID profile          : globalnasidprofile

   OUI value list          :

       Index :  1       Value : 123401

 GigabitEthernet1/0/1 is link-up

   Port mode                      : userLoginWithOUI

   NeedToKnow mode               : Disabled

   Intrusion protection mode   : NoAction

   Security MAC address attribute

        Learning mode             ： Dynamic

        Aging type                 : Periodical

   Max secure MAC addresses      : 64

   Current secure MAC addresses   : 1

   Authorization                   ： Permitted

NAS-ID profile                : portnasidprofile

表1-1 display port-security命令显示信息描述表

字段

描述

Port security

端口安全的开启状态

AutoLearn aging time

Sticky MAC地址的老化时间，单位为分钟

Disableport timeout

收到非法报文的端口暂时被关闭的时间，单位为秒

MAC move

MAC迁移功能的开启状态

·如果MAC迁移功能处于开启状态，则显示Permitted

·如果MAC迁移功能处于关闭状态，则显示Denied

Authorization fail

授权失败后用户的状态，包括下线（Offline）和保持在线（Online）两种类型

NAS-ID profile

全局引用的 NAS-ID Profile

OUI value list

允许通过认证的用户的24位OUI值

Index

OUI的索引

Value

OUI值

Port mode

端口安全模式，包括以下几种：

·noRestriction

·autoLearn

·macAddressWithRadius

·macAddressElseUserLoginSecure

·macAddressElseUserLoginSecureExt

·secure

·userLogin

·userLoginSecure

·userLoginSecureExt

·macAddressOrUserLoginSecure

·macAddressOrUserLoginSecureExt

·userLoginWithOUI

以上各模式的支持情况以及生效情况与设备的型号有关，请以设备的实际情况为准。关于各模式的具体涵义，请参考端口安全配置手册

NeedToKnow mode

Need To Know模式，包括以下四种：

·NeedToKnowOnly：表示仅允许目的MAC地址为已通过认证的MAC地址的单播报文通过

·NeedToKnowWithBroadcast：允许目的MAC地址为已通过认证的MAC地址的单播报文或广播地址的报文通过

·NeedToKnowWithMulticast：允许目的MAC地址为已通过认证的MAC地址的单播报文，广播地址或组播地址的报文通过

·Disabled：表示不进行NTK处理

该模式的生效情况与设备的型号有关，请以设备的实际情况为准

Intrusion protection mode

入侵检测特性模式，包括以下四种：

·BlockMacAddress：表示将非法报文的源MAC地址加入阻塞MAC地址列表中

·DisablePort：表示将收到非法报文的端口永久关闭

·DisablePortTemporarily：表示将收到非法报文的端口暂时关闭一段时间

·NoAction：表示不进行入侵检测处理

Security MAC address attribute

安全MAC地址的相关属性

Security MAC address learning mode

安全MAC地址的学习方式：

·Dynamic：动态类型

·Sticky：Sticky类型

Security MAC address aging type

安全MAC地址的老化方式：

·Periodical：按照配置的老化时间间隔进行老化

·Inactivity：无流量命中时老化

Max secure MAC addresses

端口安全允许的最大安全MAC地址数目或上线用户数

Current secure MAC addresses

端口下保存的安全MAC地址数目

Authorization

服务器的授权信息是否被忽略

·Permitted：表示当前端口应用RADIUS服务器或本地设备下发的授权信息

·Ignored：表示当前端口不应用RADIUS服务器或本地设备下发的授权信息

NAS-ID profile

端口下引用的 NAS-ID Profile

**端口安全 \-- 端口安全配置命令 \-- display port-security mac-address block**

------------------------------------------------------------------------

**[display port-security mac-address block**]命令用来显示阻塞MAC地址信息。

【命令】

**[display port-security mac-address block** [ **interface** *interface-type interface-number*   **vlan** *vlan-id*   **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定端口的阻塞MAC地址信息，*interface-type interface-number*表示端口类型和端口编号。

**[vlan*** vlan-id*]：显示指定VLAN的阻塞MAC地址信息。其中，*vlan-id*表示VLAN编号，取值范围为1～4094。

**[count**]：显示阻塞MAC地址的个数。

【使用指导】

如果不指定任何参数，则显示所有阻塞MAC地址的信息。

【举例】

\# 显示所有阻塞MAC地址。（集中式设备）

\<Sysname\> display port-security mac-address block

 MAC ADDR             Port                         VLAN ID

 0002-0002-0002      GE1/0/1                     1

 000d-88f8-0577      GE1/0/1                     1

 \-\--  2 mac address(es) found  \-\--

\# 显示所有阻塞MAC地址。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display port-security mac-address block

 MAC ADDR             Port                         VLAN ID

 \-\-- On slot 0, no MAC address found \-\--

 MAC ADDR              Port                        VLAN ID

 000f-3d80-0d2d       GE1/0/1                    30

 \-\-- On slot 1, 1 MAC address(es) found \-\--

 \-\-- 1 mac address(es) found \-\--

\# 显示所有阻塞MAC地址。（分布式设备－IRF模式）

\<Sysname\> display port-security mac-address block

 MAC ADDR             Port                         VLAN ID

 \-\-- On slot 0 in chassis 1, no MAC address found \-\--

 MAC ADDR              Port                        VLAN ID

 000f-3d80-0d2d       GE1/0/1                    30

 \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--

 \-\--  1 mac address(es) found  \-\--

\# 显示所有阻塞MAC地址计数。（集中式设备）

\<Sysname\> display port-security mac-address block count

\-\-- 2 mac address(es) found \-\--

\# 显示所有阻塞MAC地址计数。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display port-security mac-address block count

\-\-- On slot 0, no MAC address found \-\--

\-\-- On slot 1, 1 MAC address(es) found \-\--

\-\-- 1 mac address(es) found \-\--

\# 显示所有阻塞MAC地址计数。（分布式设备－IRF模式）

\<Sysname\> display port-security mac-address block count

 \-\-- On slot 0 in chassis 1, no MAC address found \-\--

 \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--

 \-\--  1 mac address(es) found  \-\--

\# 显示指定VLAN中的阻塞MAC地址。（集中式设备）

\<Sysname\> display port-security mac-address block vlan 1

 MAC ADDR             Port                         VLAN ID

 0002-0002-0002      GE1/0/1                     1

 000d-88f8-0577      GE1/0/1                     1

 \-\--  2 mac address(es) found  \-\--

\# 显示指定VLAN中的阻塞MAC地址。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display port-security mac-address block vlan 30

 MAC ADDR               Port                        VLAN ID

 \-\-- On slot 0, no MAC address found \-\--

 MAC ADDR               Port                        VLAN ID

 000f-3d80-0d2d        GE1/0/1                    30

 \-\-- On slot 1, 1 MAC address(es) found \-\--

 \-\-- 1 mac address(es) found \-\--

\# 显示指定VLAN中的阻塞MAC地址。（分布式设备－IRF模式）

\<Sysname\> display port-security mac-address block vlan 30

 MAC ADDR               Port                        VLAN ID

 \-\-- On slot 0 in chassis 1, no MAC address found \-\--

 MAC ADDR               Port                       VLAN ID

 000f-3d80-0d2d        GE1/0/1                   30

 \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--

 \-\-- 1 mac address(es) found \-\--

\# 显示指定端口下的阻塞MAC地址。（集中式设备）

\<Sysname\> display port-security mac-address block interface GigabitEthernet1/0/1

 MAC ADDR             Port                        VLAN ID

 000d-88f8-0577      GE1/0/1                    1

 \-\--  1 mac address(es) found  \-\--

\# 显示指定端口下的阻塞MAC地址。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display port-security mac-address block interface GigabitEthernet1/0/1

 MAC ADDR             Port                        VLAN ID

 000f-3d80-0d2d      GE1/0/1                    30

 \-\-- On slot 1, 1 MAC address(es) found \-\--

 \-\-- 1 mac address(es) found \-\--

\# 显示指定端口下的阻塞MAC地址。（分布式设备－IRF模式）

\<Sysname\> display port-security mac-address block interface GigabitEthernet1/0/1

 MAC ADDR             Port                        VLAN ID

 000f-3d80-0d2d      GE1/0/1                    30

 \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--

 \-\-- 1 mac address(es) found \-\--

\# 显示指定端口下的在指定VLAN中的阻塞MAC地址。（集中式设备）

\<Sysname\> display port-security mac-address block interface ethernet 1/1 vlan 1

 MAC ADDR             Port                        VLAN ID

 000d-88f8-0577      GE1/0/1                    1

 \-\--  1 mac address(es) found  \-\--

\# 显示指定端口下的在指定VLAN中的阻塞MAC地址。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display port-security mac-address block interface ethernet 1/1 vlan 30

 MAC ADDR             Port                        VLAN ID

 000f-3d80-0d2d      GE1/0/1                    30

 \-\-- On slot 1, 1 MAC address(es) found \-\--

 \-\-- 1 mac address(es) found \-\--

\# 显示指定端口下的在指定VLAN中的阻塞MAC地址。（分布式设备－IRF模式）

\<Sysname\> display port-security mac-address block interface ethernet 1/1 vlan 30

 MAC ADDR             Port                        VLAN ID

 000f-3d80-0d2d      GE1/0/1                    30

 \-\-- On slot 1 in chassis 1, 1 MAC address(es) found \-\--

 \-\-- 1 mac address(es) found \-\--

表1-2 display port-security mac-address block命令显示信息描述表

字段

描述

MAC ADDR

阻塞MAC地址

Port

阻塞MAC地址所在端口

VLAN ID

端口所属VLAN

*[number* mac address(es) found]

当前阻塞MAC地址数目为*number*个

【相关命令】

·**port-security intrusion-mode**

**端口安全 \-- 端口安全配置命令 \-- display port-security mac-address security**

------------------------------------------------------------------------

**[display port-security mac-address security**]命令用来显示安全MAC地址信息。

【命令】

**[display port-security mac-address security** [ **interface** *interface-type interface-number*   **vlan** *vlan-id*   **count**  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定端口的安全MAC地址信息。其中，*interface-type interface-number*表示端口类型和端口编号。

**[vlan*** vlan-id*]：显示指定VLAN的安全MAC地址信息。其中，*vlan-id*表示VLAN编号，取值范围为1～4094。

**[count**]：统计符合条件的安全MAC地址个数。

【使用指导】

当端口工作于autoLearn模式时，端口上通过自动学习或者静态配置的安全MAC地址可通过该命令查看。

如果不指定任何参数，则显示所有安全MAC地址的信息。

【举例】

\# 显示所有安全MAC地址。

\<Sysname\> display port-security mac-address security

 MAC ADDR         VLAN ID  STATE          PORT INDEX                      AGING TIME

 0002-0002-0002  1         Security       GE1/0/1                         NOAGED

 000d-88f8-0577  1         Security       GE1/0/1                         28

 \-\--  2 mac address(es) found  \-\--

\# 显示所有安全MAC地址计数。

\<Sysname\> display port-security mac-address security count

 \-\--  2 mac address(es) found  \-\--

\# 显示指定VLAN中的安全MAC地址。

\<Sysname\> display port-security mac-address security vlan 1

 MAC ADDR         VLAN ID  STATE          PORT INDEX                      AGING TIME

 0002-0002-0002  1         Security       GE1/0/1                         NOAGED

 000d-88f8-0577  1         Security       GE1/0/1                         28

 \-\--  2 mac address(es) found  \-\--

\# 显示指定端口下的安全MAC地址。

\<Sysname\> display port-security mac-address security interface gigabitethernet 1/0/1

 MAC ADDR         VLAN ID  STATE          PORT INDEX                      AGING TIME

 000d-88f8-0577  1         Security       GE/0/1                          NOAGED

  \-\--  1 mac address(es) found  \-\--

\# 显示指定端口下的在指定VLAN中的安全MAC地址。

\<Sysname\> display port-security mac-address security interface gigabitethernet 1/0/1 vlan 1

 MAC ADDR         VLAN ID  STATE          PORT INDEX                      AGING TIME

 000d-88f8-0577  1         Security       GE1/0/1                         NOAGED

 \-\--  1 mac address(es) found  \-\--

表1-3 display port-security mac-address security命令显示信息描述表

字段

描述

MAC ADDR

安全MAC地址

VLAN ID

端口所属VLAN

STATE

添加的MAC地址类型

·Security：表示该项是安全MAC地址

PORT INDEX

安全MAC地址所在端口

AGING TIME

安全MAC地址的剩余存活时间

·对于静态MAC地址，显示为NOAGED

·对于Sticky MAC地址，显示为具体的剩余存活时间，单位为分钟。缺省情况下为不进行老化，显示为NOAGED

*[number* mac address(es) found]

当前保存的安全MAC地址数目为*number*个

【相关命令】

·**port-security mac-address security**

**端口安全 \-- 端口安全配置命令 \-- port-security authorization ignore**

------------------------------------------------------------------------

**[port-security authorization ignore**]命令用来配置端口不应用RADIUS服务器或设备本地下发的授权信息。

**[undo port-security authorization ignore**]命令用来恢复缺省情况。

【命令】

**[port-security authorization ignore**]

**[undo port-security authorization ignore**]

【缺省情况】

端口应用RADIUS服务器或设备本地下发的授权信息。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当用户通过RADIUS认证或本地认证后，RADIUS服务器或设备会根据用户帐号配置的相关属性进行授权，比如动态下发VLAN等。若不希望接受这类动态下发的属性，则可通过配置本命令来忽略。

需要注意的是，该命令在三层以太网接口视图下的支持情况与产品型号有关，请以设备的实际情况为准。

【举例】

\# 配置端口GigabitEthernet1/0/1不应用RADIUS服务器或设备本地下发的授权信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security authorization ignore

【相关命令】

·**display port-security**

**端口安全 \-- 端口安全配置命令 \-- port-security authorization-fail offline**

------------------------------------------------------------------------

**[port-security authorization-fail offline**]命令用来开启授权失败用户下线功能。

**[undo port-security authorization-fail offline**]命令用来恢复缺省情况。

【命令】

**[port-security authorization-fail offline**]

**[undo port-security authorization-fail offline**]

【缺省情况】

授权失败用户下线功能处于关闭状态，即授权失败后用户保持在线。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果配置为授权失败用户下线，当下发的授权ACL、User Profile不存在或者ACL、User Profile下发失败时，将强制用户下线；

如果配置为授权失败用户保持在线，当下发的授权ACL、User Profile不存在或者ACL、User Profile下发失败时，用户保持在线，授权ACL、User Porfile不生效，设备打印LOG信息。

【举例】

\# 开启授权失败用户下线功能。

\<Sysname\> system-view

Sysname port-security authorization-fail offline

【相关命令】

·**display port-security**

**端口安全 \-- 端口安全配置命令 \-- port-security enable**

------------------------------------------------------------------------

**[port-security enable**]命令用来使能端口安全。

**[undo port-security enable**]命令用来关闭端口安全。

【命令】

**[port-security enable**]

**[undo port-security enable**]

【缺省情况】

端口安全的使能情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果已全局开启了802.1X或MAC地址认证，则无法使能端口安全。

执行使能或关闭端口安全的命令后，端口上的相关配置将会恢复为如下情况：

·802.1X端口接入控制方式恢复为**macbased**；

·802.1X端口的授权状态恢复为**auto**。

端口上有用户在线的情况下，若关闭端口安全，则在线用户将会下线。

【举例】

\# 使能端口安全。

\<Sysname\> system-view

Sysname port-security enable

【相关命令】

·**display port-security**

·**dot1x**（安全命令参考/802.1X）

·**dot1x port-control**（安全命令参考/802.1X）

·**dot1x port-method**（安全命令参考/802.1X）

·**mac-authentication**（安全命令参考/MAC地址认证）

**端口安全 \-- 端口安全配置命令 \-- port-security intrusion-mode**

------------------------------------------------------------------------

**[port-security intrusion-mode**]命令用来配置入侵检测特性，对接收到非法报文的端口采取相应的安全策略。

**[undo port-security intrusion-mode**]命令用来缺省情况。

【命令】

**[port-security intrusion-mode **[{ **blockmac** \| **disableport** \| **disableport-temporarily** }]]

**[undo port-security intrusion-mode**]

【缺省情况】

对接收到非法报文的端口不进行入侵检测处理。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[blockmac**]：表示将非法报文的源MAC地址加入阻塞MAC地址列表中，源MAC地址为阻塞MAC地址的报文将被丢弃，实现在端口上过滤非法流量的作用。此MAC地址在被阻塞3分钟（系统默认，不可配）后恢复正常。阻塞MAC地址列表可以通过**display port-security mac-address block**命令查看。

**[disableport**]：表示将收到非法报文的端口永久关闭。

**[disableport-temporarily**]：表示将收到非法报文的端口暂时关闭一段时间。关闭时长可通过**port-security timer disableport**命令配置。

【使用指导】

可以通过执行**undo shutdown**命令重新开启被入侵检测特性临时或永久断开的端口。

【举例】

\# 配置端口GigabitEthernet1/0/1的入侵检测特性检测到非法报文后，将非法报文的源MAC地址置为阻塞MAC。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security intrusion-mode blockmac

【相关命令】

·**display port-security**

·**display port-security mac-address block**

·**port-security timer disableport**

**端口安全 \-- 端口安全配置命令 \-- port-security mac-address aging-type inactivity**

------------------------------------------------------------------------

**[port-security mac-address aging-type inactivity**]命令用来配置安全MAC地址的老化方式为无流量老化。

**[undo port-security mac-address aging-type inactivity**]命令用来恢复缺省情况。

【命令】

**[port-security mac-address aging-type inactivity**]

**[undo port-security mac-address aging-type inactivity**]

【缺省情况】

安全MAC地址按照配置的老化时间进行老化，即在安全MAC地址的老化时间到达后立即老化，不论该安全MAC地址是否还有流量产生。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

无流量老化方式下，设备会定期检测（检测周期不可配）端口上的安全MAC地址是否有流量产生，若某安全MAC地址在配置的老化时间内没有任何流量产生，则才会被老化，否则该安全MAC地址不会被老化，并在下一个老化周期内重复该检测过程。下一个周期内若还有流量产生则继续保持该安全MAC地址的学习状态，该方式可有效避免非法用户通过仿冒合法用户MAC地址乘机在合法用户的安全MAC地址老化时间到达之后占用端口资源。

此命令仅对于Sticky MAC地址以及动态类型的安全MAC地址有效。

【举例】

\# 配置端口GigabitEthernet1/0/1的安全MAC地址的老化方式为无流量老化。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security mac-address aging-type inactivity

【相关命令】

·**display port-security**

**端口安全 \-- 端口安全配置命令 \-- port-security mac-address dynamic**

------------------------------------------------------------------------

**[port-security mac-address dynamic**]命令用来将Sticky MAC地址设置为动态类型的安全MAC地址。

**[undo port-security mac-address dynamic**]命令用来恢复缺省情况。

【命令】

**[port-security mac-address dynamic**]

**[undo port-security mac-address dynamic**]

【缺省情况】

端口学习到的是Sticky类型的安全MAC，它能够被保存在配置文件中，设备重启后也不会丢失。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

动态类型的安全MAC地址不会被保存在配置文件中，可通过执行**display port-security mac-address security**命令查看到，设备重启之后会丢失。在不希望设备上保存重启之前端口上已有的Sticky MAC地址的情况下，可将其设置为动态类型的安全MAC地址。

本命令成功执行后，指定端口上的Sticky MAC地址会立即被转换为动态类型的安全MAC地址，且将不能手工添加Sticky MAC地址。之后，若成功执行对应的**undo**命令，该端口上的动态类型的安全MAC地址会立即转换为Sticky MAC地址，且用户可以手工添加Sticky MAC地址。

【举例】

\# 将端口GigabitEthernet1/0/1上的Sticky MAC地址设置为动态类型的安全MAC地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security mac-address dynamic

【相关命令】

·**display port-security**

·**display port-security mac-address security**

**端口安全 \-- 端口安全配置命令 \-- port-security mac-address security**

------------------------------------------------------------------------

**[port-security mac-address security**]命令用来添加安全MAC地址。

**[undo port-security mac-address security**]命令用来删除指定的安全MAC地址。

【命令】

在二层以太网接口视图下：

**[port-security mac-address security ** **sticky** ] *mac-address* **vlan** *vlan-id*

**[undo port-security mac-address security ** **sticky** ] *mac-address* **vlan** *vlan-id*

在系统视图下：

**[port-security** **mac-address** **security** [ **sticky**  *mac-address* **interface** *interface-type interface-number* **vlan** *vlan-id*]]

**[undo port-security mac-address security **  *mac-address* [ **interface** *interface-type interface-number*  ] **vlan** *vlan-id* ]

【缺省情况】

未配置安全MAC地址。

【视图】

二层以太网接口视图/系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sticky**]：表示要添加一个可老化的安全MAC地址（Sticky MAC地址）。Sticky MAC地址的老化时间可通过**port-security timer autolearn aging**命令配置。当Sticky MAC地址的老化时间到达时，Sticky MAC地址即被删除。若不指定本参数，则表示添加的是一个不老化的安全MAC地址。

*[mac-address*]：安全MAC地址，格式为H-H-H。

**[interface*** interface-type interface-number*]：指定添加安全MAC地址的接口。其中，*interface-type interface-number*表示接口类型和接口编号。

**[vlan ***vlan-id*]：指定安全MAC地址所属的VLAN。其中，*vlan-id*表示VLAN编号，取值范围为1～4094。

【使用指导】

手工配置添加的安全MAC地址在保存配置并设备重启后，不会被删除。因此，可以将网络中一些已知的、固定要接入某端口的主机或设备的MAC地址添加为安全MAC地址，这样在端口处于autoLearn安全模式时，此类源MAC地址为安全MAC地址的主机或设备的报文将被允许通过指定端口，而且还可避免与其它通过自动方式学习到端口上的MAC地址的报文争夺资源而被拒绝接收。

需要注意的是：

·成功添加安全MAC地址的前提为：端口安全处于开启状态；端口的端口安全模式为autoLearn；当前的接口允许指定的VLAN通过或已加入该VLAN，且该VLAN已存在。

·已添加的安全MAC地址，除非首先将其删除，否则不能重复添加或者修改其地址类型，例如已经在某端口上添加了一条安全MAC地址**port-security mac-address security** 1-1-1 **vlan** 10，则不能再添加一条安全MAC地址**port-security mac-address security sticky** 1-1-1 **vlan** 10。

【举例】

\# 使能端口安全，配置端口GigabitEthernet1/0/1的安全模式为autoLearn，并指定端口安全允许的最大MAC地址数为100。

\<Sysname\> system-view

Sysname port-security enable

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security max-mac-count 100

Sysname-GigabitEthernet1/0/1 port-security port-mode autolearn

\# 为该端口添加一条Sticky MAC地址0001-0002-0003，该安全MAC地址属于VLAN 4。

Sysname-GigabitEthernet1/0/1 port-security mac-address security sticky 0001-0002-0003 vlan 4

Sysname-GigabitEthernet1/0/1 quit

\# 在系统视图下为端口GigabitEthernet1/0/1添加一条安全MAC地址0001-0001-0002，该安全MAC地址属于VLAN 10。

Sysname port-security mac-address security 0001-0001-0002 interface gigabitethernet 1/0/1 vlan 10

【相关命令】

·**display port-security**

·**port-security timer autolearn aging**

**端口安全 \-- 端口安全配置命令 \-- port-security mac-move permit**

------------------------------------------------------------------------

**[port-security mac-move permit**]命令用来开启允许MAC迁移功能。

**[undo port-security mac-move permit**]命令用来恢复缺省情况。

【命令】

**[port-security mac-move permit**]

**[undo port-security mac-move permit**]

【缺省情况】

允许MAC迁移功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该功能对系统中的所有802.1X认证用户和MAC地址认证用户生效。

MAC迁移功能处于关闭状态时，如果用户从某一端口上线成功，则该用户在未从当前端口下线的情况下无法在设备的其它端口上（无论该端口是否与当前端口属于同一VLAN）发起认证，也无法上线。

MAC迁移功能处于开启状态时，如果用户从某一端口上线成功，则允许该在线用户在设备的其它端口上（无论该端口是否与当前端口属于同一VLAN）发起认证。如果该用户在后接入的端口上认证成功，则当前端口会将该用户立即进行下线处理，保证该用户仅在一个端口上处于上线状态。

【举例】

\# 开启允许MAC迁移功能。

\<Sysname\> system-view

Sysname port-security mac-move permit

【相关命令】

·**display port-security**

**端口安全 \-- 端口安全配置命令 \-- port-security max-mac-count**

------------------------------------------------------------------------

**[port-security max-mac-count**]命令用来设置端口安全允许的最大安全MAC地址数。

**[undo port-security max-mac-count**]命令用来恢复缺省情况。

【命令】

**[port-security max-mac-count ***count-value*]

**[undo port-security max-mac-count**]

【缺省情况】

端口安全不限制本端口可保存的最大安全MAC地址数。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count-value*]：端口允许的最大安全MAC地址数，取值范围为1～1024。

【使用指导】

对于autoLearn安全模式，端口允许的最大安全MAC地址数由本命令配置，包括端口上学习到的以及手工配置的安全MAC地址数；对于采用802.1X、MAC地址认证或者两者组合形式的认证类安全模式，端口允许的最大用户数取本命令配置的值与相应模式下允许认证用户数的最小值。例如，userLoginSecureExt模式下，端口下所允许的最大安全MAC地址数为配置的端口安全允许的最大安全MAC地址数与802.1X认证所允许的最大用户数的最小值。

需要注意的是：

·当端口工作于autoLearn模式时，无法更改端口安全允许的最大安全MAC地址数。

·无线端口上有用户在线时，无法更改端口安全允许的最大安全MAC地址数。

·端口安全允许的最大安全MAC地址数不能小于当前端口下已保存的MAC地址数。

·该命令在三层以太网接口视图下的支持情况与产品型号有关，请以设备的实际情况为准。

【举例】

\# 在端口GigabitEthernet1/0/1上配置端口安全允许的最大安全MAC地址数为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security max-mac-count 100

【相关命令】

·**display port-security**

**端口安全 \-- 端口安全配置命令 \-- port-security nas-id-profile**

------------------------------------------------------------------------

**[port-security nas-id-profile**]命令用来指定全局/端口引用的NAS-ID Profile。

**[undo port-security nas-id-profile**]命令用来删除全局/端口引用的NAS-ID Profile。

【命令】

**[port-security nas-id-profile ***profile-name*]

**[undo port-security nas-id-profile**]

【缺省情况】

未指定引用的NAS-ID Profile。

【视图】

系统视图/接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：标识指定VLAN和NAS-ID绑定关系的Profile名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

本命令引用的NAS-ID Profile由命令**aaa nas-id profile**配置，具体情况请参考"安全命令参考"中的"AAA"。

NAS-ID Profile可以在系统视图下或者接口视图下进行配置引用，接口上的配置优先，若接口上没有配置，则使用系统视图下的全局配置。

需要注意的是，如果指定了NAS-ID Profile，则此Profile中定义的绑定关系优先使用；如果未指定NAS-ID Profile或指定的Profile中没有找到匹配的绑定关系，则使用设备名作为NAS-ID。

【举例】

\# 在接口GigabitEthernet1/0/1上指定名为aaa的NAS-ID Profile。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-secutiry nas-id-profile aaa

\# 在系统视图下指定名为aaa的NAS-ID Profile。

\<Sysname\> system-view

Sysname port-secutiry nas-id-profile aaa

【相关命令】

·**aaa nas-id profile**（安全命令参考/AAA）

**端口安全 \-- 端口安全配置命令 \-- port-security ntk-mode**

------------------------------------------------------------------------

**[port-security ntk-mode**]命令用来配置端口Need To Know特性。

**[undo port-security ntk-mode**]命令用来恢复缺省情况。

【命令】

**[port-security ntk-mode **[{ **ntk-withbroadcasts** \| **ntk-withmulticasts** \| **ntkonly** }]]

**[undo port-security ntk-mode**]

【缺省情况】

端口没有配置Need To Know特性，即所有报文都可成功发送。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ntk-withbroadcasts**]：允许目的MAC地址为已通过认证的MAC地址的单播报文或广播地址的报文通过。

**[ntk-withmulticasts**]：允许目的MAC地址为已通过认证的MAC地址的单播报文，广播地址或组播地址的报文通过。

**[ntkonly**]：仅允许目的MAC地址为已通过认证的MAC地址的单播报文通过。

【使用指导】

Need To Know特性通过检测从端口发出的数据帧的目的MAC地址，保证数据帧只能被发送到已经通过认证的设备上，从而防止非法设备窃听网络数据。

需要注意的是：

·无线端口上有用户在线的情况下，无法更改Need To Know特性的配置。

·Need To Know特性的配置生效情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置端口GigabitEthernet1/0/1的Need To Know特性为**ntkonly**，即仅发送目的地址为已认证的MAC地址的报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security ntk-mode ntkonly

【相关命令】

·**display port-security**

**端口安全 \-- 端口安全配置命令 \-- port-security oui**

------------------------------------------------------------------------

**[port-security oui**]命令用来配置允许通过认证的用户的OUI值。

**[undo port-security oui**]命令用来删除指定索引的OUI值。

【命令】

**[port-security oui index ***index-value ***mac-address ***oui-value*]

**[undo port-security oui index ***index-value*]

【缺省情况】

不存在允许通过认证的用户OUI值。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[index-value*]：标识此OUI的索引值，取值范围为1～16。

*[oui-value*]：OUI值，输入格式为H-H-H的48位MAC地址。系统会自动取输入的前24位做为OUI值，忽略后24位。

【使用指导】

OUI是MAC地址的前24位（二进制），是IEEE为不同设备供应商分配的一个全球唯一的标识符。当需要允许某些特殊设备的（有线接入）报文总是可以通过认证，或仅允许这些设备的（无线接入）报文可以进行认证的情况下，就可以通过本命令来指定这些设备的OUI值，例如，某公司仅允许A厂商的IP电话在本企业网内使用，则可以通过本命令将A厂商设备的OUI值设置为认证的OUI值。

可通过多次执行本命令，配置多个OUI值。

配置的OUI值只在端口安全模式为userLoginWithOUI时生效。在userLoginWithOUI模式下，端口上除了允许一个802.1X认证用户接入之外，还额外允许一个特殊用户接入，该用户报文的源MAC地址的OUI与设备上配置的某个OUI值相符。

【举例】

\# 配置一个允许通过认证的用户OUI值为000d2a，索引为4。

\<Sysname\> system-view

Sysname port-security oui index 4 mac-address 000d-2a10-0033

【相关命令】

·**display port-security**

**端口安全 \-- 端口安全配置命令 \-- port-security port-mode**

------------------------------------------------------------------------

**[port-security port-mode**]命令用来配置端口安全模式。

**[undo port-security port-mode**]命令用来恢复缺省情况。

【命令】

**[port-security port-mode **[{ **autolearn** \| **mac-authentication** \| **mac-else-userlogin-secure** \| **mac-else-userlogin-secure-ext** \| **secure** \| **userlogin** \| **userlogin-secure** \| **userlogin-secure-ext** \| **userlogin-secure-or-mac** \| **userlogin-secure-or-mac-ext** \| **userlogin-withoui** }]]

**[undo port-security port-mode**]

【缺省情况】

端口处于noRestrictions模式，此时该端口的安全功能关闭，端口处于不受端口安全限制的状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

表1-4 安全模式的参数解释表

参数

安全模式

说明

**[autolearn**]

autoLearn

端口可通过手工配置或自动学习MAC地址。手工配置或自动学习到的MAC地址被称为安全MAC，并被添加到安全MAC地址表中

当端口下的安全MAC地址数超过端口安全允许的最大安全MAC地址数后，端口模式会自动转变为secure模式。之后，该端口停止添加新的安全MAC，只有源MAC地址为安全MAC地址、通过命令**mac-address dynamic**或**mac-address static**手工配置的MAC地址的报文，才能通过该端口

**[mac-authentication**]

macAddressWithRadius

对接入用户采用MAC地址认证

此模式下，端口允许多个用户接入

**[mac-else-userlogin-secure**]

macAddressElseUserLoginSecure

端口同时处于macAddressWithRadius模式和userLoginSecure模式，但MAC地址认证优先级大于802.1X认证。允许端口下一个802.1X认证用户及多个MAC地址认证用户接入

非802.1X报文直接进行MAC地址认证。802.1X报文先进行MAC地址认证，如果MAC地址认证失败再进行802.1X认证

**[mac-else-userlogin-secure-ext**]

macAddressElseUserLoginSecureExt

与macAddressElseUserLoginSecure类似，但允许端口下有多个802.1X和MAC地址认证用户

**[secure**]

secure

禁止端口学习MAC地址，只有源MAC地址为端口上的安全MAC地址、手工配置的MAC地址的报文，才能通过该端口

**[userlogin**]

userLogin

对接入用户采用基于端口的802.1X认证

此模式下，端口下的第一个802.1X用户认证成功后，其它用户无须认证就可接入

**[userlogin-secure**]

userLoginSecure

对接入用户采用基于MAC地址的802.1X认证

此模式下，端口最多只允许一个802.1X认证用户接入

**[userlogin-secure-ext**]

userLoginSecureExt

对接入用户采用基于MAC的802.1X认证，且允许端口下有多个802.1X用户

**[userlogin-secure-or-mac**]

macAddressOrUserLoginSecure

端口同时处于userLoginSecure模式和macAddressWithRadius模式，且允许一个802.1X认证用户及多个MAC地址认证用户接入

此模式下，802.1X认证优先级大于MAC地址认证：报文首先进行802.1X认证，如果802.1X认证失败再进行MAC地址认证

**[userlogin-secure-or-mac-ext**]

macAddressOrUserLoginSecureExt

与macAddressOrUserLoginSecure类似，但允许端口下有多个802.1X和MAC地址认证用户

**[userlogin-withoui**]

userLoginWithOUI

与userLoginSecure模式类似，但端口上除了允许一个802.1X认证用户接入之外，还额外允许一个特殊用户接入，该用户报文的源MAC的OUI与设备上配置的OUI值相符

此模式下，报文首先进行OUI匹配，OUI匹配失败的报文再进行802.1X认证，OUI匹配成功和802.1X认证成功的报文都允许通过端口

【使用指导】

·各端口安全模式的支持情况与设备的型号有关，请以设备的实际情况为准。

·端口安全模式与端口下的802.1X认证使能、端口接入控制方式、端口授权状态以及端口下的MAC地址认证使能配置互斥。

·当端口安全已经使能且当前端口安全模式不是noRestrictions时，若要改变端口安全模式，必须首先执行**undo port-security port-mode**命令恢复端口安全模式为noRestrictions模式。

·配置端口安全autoLearn模式时，首先需要通过命令**port-security max-mac-count**设置端口安全允许的最大安全MAC地址数。

·端口上有用户在线的情况下，端口安全模式无法改变。

·开启了MAC地址认证延迟功能的接口上不建议同时配置端口安全的模式为**mac-else-userlogin-secure**或**mac-else-userlogin-secure-ext**，否则MAC地址认证延迟功能不生效。MAC地址认证延迟功能的具体配置请参见"安全命令参考"中的"MAC地址认证"。

·部分端口安全模式的配置生效情况与设备的型号有关，请以设备的实际情况为准。即，部分设备上不支持autoLearn模式、基于MAC地址的802.1X认证的端口安全模式（userLoginSecure userLoginWithOUI userLoginSecureExt）以及基于MAC地址认证的端口安全模式（macAddressWithRadius、macAddressOrUserLoginSecure、macAddressElseUserLoginSecure、macAddressOrUserLoginSecureExt、macAddressElseUserLoginSecureExt），因此相关配置不生效。

表1-5 接口支持的端口安全模式列表

接口类型

支持的端口安全模式

二层以太网接口

**[autolearn**]、**mac-authentication**、**mac-else-userlogin-secure**、**mac-else-userlogin-secure-ext**、**secure**、**userlogin**、**userlogin-secure**、**userlogin-secure-ext**、**userlogin-secure-or-mac**、**userlogin-secure-or-mac-ext**、**userlogin-withoui**

三层以太网接口

**[mac-authentication**]、**mac-else-userlogin-secure**、**mac-else-userlogin-secure-ext**、**userlogin-secure**、**userlogin-secure-ext**、**userlogin-secure-or-mac**、**userlogin-secure-or-mac-ext**

备注：三层以太网接口下配置安全模式的支持情况与产品型号有关

【举例】

\# 使能端口安全，并配置端口GigabitEthernet1/0/1的端口安全模式为secure。

\<Sysname\> system-view

Sysname port-security enable

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security port-mode secure

\# 将端口GigabitEthernet1/1的端口安全模式改变为userLogin。

Sysname-GigabitEthernet1/0/1 undo port-security port-mode

Sysname-GigabitEthernet1/0/1 port-security port-mode userlogin

【相关命令】

·**display port-security**

·**port-security max-mac-count**

**端口安全 \-- 端口安全配置命令 \-- port-security timer autolearn aging**

------------------------------------------------------------------------

**[port-security timer autolearn aging**]命令用来配置安全MAC地址的老化时间。

**[undo port-security timer autolearn aging**]命令用来恢复缺省情况。

【命令】

**[port-security timer autolearn aging ***time-value*]

**[undo port-security timer autolearn aging**]

【缺省情况】

安全MAC地址不会老化。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-value*]：安全MAC地址的老化时间，取值范围为0～129600，单位为分钟，取值为0表示不会老化。

【使用指导】

安全MAC地址的老化时间对所有端口学习到的安全MAC地址以及手工添加的Sticky MAC地址均有效。

较短的老化时间可提高端口接入的安全性和端口资源的利用率，但也会影响在线用户的在线稳定性，因此需要结合当前的网络环境和设备的性能合理设置老化时间。

【举例】

\# 配置安全MAC地址的老化时间为30分钟。

\<Sysname\> system-view

Sysname port-security timer autolearn aging 30

【相关命令】

·**display port-security**

·**port-security mac-address security**

**端口安全 \-- 端口安全配置命令 \-- port-security timer disableport**

------------------------------------------------------------------------

**[port-security timer disableport**]命令用来配置系统暂时关闭端口的时间。

**[undo port-security timer disableport**]命令用来恢复缺省情况。

【命令】

**[port-security timer disableport ***time-value*]

**[undo port-security timer disableport**]

【缺省情况】

系统暂时关闭端口的时间为20秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-value*]：端口关闭的时间，取值范围为20～300，单位为秒。

【使用指导】

当**port-security intrusion-mode**设置为**disableport-temporarily**模式时，系统暂时关闭端口的时间由该命令配置。

【举例】

\# 配置端口GigabitEthernet1/0/1的入侵检测特性检测到非法报文后，将收到非法报文的端口暂时关闭30秒。

\<Sysname\> system-view

Sysname port-security timer disableport 30

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port-security intrusion-mode disableport-temporarily

【相关命令】

·**display port-security**

·**port-security intrusion-mode**

