
**登录设备 \-- 登录设备命令 \-- activation-key**

------------------------------------------------------------------------

**[activation-key**]命令用来配置启动终端会话的快捷键。

**[undo activation-key**]命令用来恢复缺省情况。

【命令】

**[activation-key** *key-string*]

**[undo activation-key**]

【缺省情况】

按\<Enter\>键启动终端会话。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[key-string*]：定义启动终端会话的快捷键，可以是区分大小写的单个字符，也可以是单个字符或组合键对应的ACSII码（0～127）。比如设置activation-key 65，此时生效快捷键为A；如果设置activation-key a，生效的快捷键为a。

【使用指导】

如果使用**activation-key**命令设置了别的快捷键，则新的快捷键将代替\<Enter\>键来启动终端会话，新设置的快捷键可以使用**[display current-configuration \| include activation-key]**命令查看。

如果用户线视图下配置**activation-key**为缺省值，并且此时用户线类视图下配置了**activation-key**，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。

VTY用户线视图/VTY用户线类视图不支持该命令。

【举例】

\# 指定启动Console口终端会话的快捷键为\<s\>。

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 activation-key s

验证过程如下：

·退出Console口终端会话。

Sysname-line-console0 return

\<Sysname\> quit

·重新使用Console口登录设备，能看到如下显示信息。

Press ENTER to get started.

·此时，\<Enter\>键失效，需要按\<s\>键才能出现用户视图提示符，启动Console口终端会话。

\<Sysname\>

**登录设备 \-- 登录设备命令 \-- authentication-mode**

------------------------------------------------------------------------

**[authentication-mode**]命令用来设置用户使用当前用户线登录设备时的认证方式。

**[undo authentication-mode**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[authentication-mode**[ { **none** \| **password** \| **scheme** }]]

**[undo authentication-mode**]

FIPS模式下：

**[authentication-mode** **scheme**]

**[undo authentication-mode**]

【缺省情况】

非FIPS模式下：使用VTY、AUX用户线登录的用户的认证方式为password，使用Console、TTY用户线登录的用户不需要认证。如果设备上只有一个AUX口，而没有Console口（Console口与AUX口共用），则使用AUX用户线登录的用户不需要认证。

FIPS模式下：使用当前用户线登录设备时的认证方式为scheme。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[none**]：指定不进行认证。

**[password**]：指定进行密码认证方式。

**[scheme**]：指定进行AAA认证方式。AAA的相关内容请参见"安全配置指导"中的"AAA"。

【使用指导】

当认证方式设置为none时，用户不需要输入用户名和密码，就可以使用该用户线登录设备，存在安全隐患，请谨慎配置。

用户线视图下，对**authentication-mode**和**protocol inbound**进行关联绑定。

当这两条命令均配置为缺省值，此时该用户线视图下的这两条命令配置值均取该类用户线类视图下的相应的配置；若该类用户线类视图下没有进行相应的配置，则均取缺省值。

当两条命令中的任意一条配置了非缺省值，那么另外一条取缺省值。当两条命令都配置成非缺省值，则均取用户线下的配置值。

需要注意的是，在用户线视图/用户线类视图下，该命令的配置结果将在下次登录设备时生效。

【举例】

\# 设置用户使用VTY 0用户线登录设备时，不需要认证。

\<Sysname\> system-view

Sysname line vty 0

Sysname-line-vty0 authentication-mode none

\# 设置用户使用VTY 0用户线登录设备时，需要密码认证，认证密码为321。

\<Sysname\> system-view

Sysname line vty 0

Sysname-line-vty0 authentication-mode password

Sysname-line-vty0 set authentication password simple 321

\# 设置用户使用VTY 0用户线，采用Telnet方式登录设备时采用本地AAA认证，用户名为123，认证密码为321，用户角色为network-admin。

\<Sysname\> system-view

Sysname line vty 0

Sysname-line-vty0 authentication-mode scheme

Sysname-line-vty0 quit

Sysname local-user 123

Sysname-luser-manage-123 password simple 321

Sysname-luser-manage-123 service-type telnet

Sysname-luser-manage-123 authorization-attribute user-role network-admin

【相关命令】

·**set authentication password**

**登录设备 \-- 登录设备命令 \-- auto-execute command**

------------------------------------------------------------------------

**[auto-execute command**]命令用来设置自动执行命令。

**[undo auto-execute command**]命令用来取消自动执行命令。

【命令】

**[auto-execute command ***command*]

**[undo auto-execute command**]

【缺省情况】

未设定自动执行命令。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[command*]：需要自动执行的某条命令。

【使用指导】

用户在登录时设备会自动执行**auto-execute command**配置好的命令，执行完命令后，自动断开用户连接。

该命令通常的用法是：配置**auto-execute command telnet X.X.X.X**，使用户通过该用户线登录设备时能自动连接到指定的主机。用户断开与指定主机的连接后，用户与该设备的连接才会自动断开。

需要注意的是：

·Console用户线视图/Console用户线类视图不支持该命令。

·如果设备上只有一个AUX口，没有Console口（Console口和AUX口共用），则AUX用户线视图/AUX用户线类视图不支持该命令。

·在配置**auto-execute command**命令之前，请确保可以通过其它用户线（比如Console用户线）登录系统，以便出现问题后，能删除该配置。

·执行**auto-execute command**命令后，可能导致用户不能通过该终端线对本系统进行配置，需谨慎使用。

·如果用户线视图下配置** auto-execute command**为缺省值，并且此时用户线类视图下配置了**auto-execute command**，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。

需要注意的是，在用户线视图/用户线类视图下，使用该命令设置的自动执行命令将在下次登录设备时生效。

【举例】

\# 配置用户从VTY0登录本设备（IP地址为192.168.1.40）后，自动Telnet到IP地址为192.168.1.41的设备。

\<Sysname\> system-view

Sysname line vty 0

Sysname-line-vty0 auto-execute command telnet 192.168.1.41

This action will lead to configuration failure through line-vty0. Are you sure?

Y/N:y

Sysname-line-vty0

结果验证：

重新Telnet登录到本设备，设备会自动执行telnet 192.168.1.41命令，在Telnet客户端会看到以下显示信息。

C:\\\> telnet 192.168.1.40

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2010 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*

\* Without the owner\'s prior written consent,                                 \*

\* no decompiling or reverse-engineering shall be allowed.                    \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\<Sysname\>

Trying 192.168.1.41 \...

Press CTRL+K to abort

Connected to 192.168.1.41 \...

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2014 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*

\* Without the owner\'s prior written consent,                                 \*

\* no decompiling or reverse-engineering shall be allowed.                    \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\<Sysname.41\>

此时相当于用户直接登录了192.168.1.41设备。如果用户断开与192.168.1.41的Telnet连接，用户与192.168.1.40设备的Telnet连接也会同时自动断开。

**登录设备 \-- 登录设备命令 \-- command accounting**

------------------------------------------------------------------------

**[command accounting**]命令用来使能命令行计费功能。

**[undo command accounting**]命令用来恢复缺省情况。

【命令】

**[command accounting**]

**[undo command accounting**]

【缺省情况】

没有使能命令行计费功能，即计费服务器不会记录用户执行的命令行。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能命令行计费功能后，如果没有配置命令行授权功能，则当前用户执行的每一条合法命令都会发送到HWTACACS服务器上做记录；如果配置了命令行授权功能，则当前用户执行的并且授权成功的命令都会发送到HWTACACS服务器上做记录。

如果在用户线类视图下使用**command accounting**命令使能了命令行计费功能，则该类型用户线视图都使能命令行计费功能，且用户线视图下无法使用**undo command accounting**恢复缺省情况。

需要注意的是，在用户线视图/用户线类视图下，该命令的配置结果将在下次登录设备时生效。

【举例】

\# 设置用户使用VTY 0用户线登录设备时，执行的命令需要在HWTACACS服务器上做记录。

\<Sysname\> system-view

Sysname line vty 0

Sysname-line-vty0 command accounting{.TerminalDisplayChar}

【相关命令】

·**command authorization**

·**accounting command**（安全命令参考/AAA）

**登录设备 \-- 登录设备命令 \-- command authorization**

------------------------------------------------------------------------

**[command authorization**]命令用来使能命令行授权功能。

**[undo command authorization**]命令用来恢复缺省情况。

【命令】

**[command authorization**]

**[undo command authorization**]

【缺省情况】

没有使能命令行授权功能，即用户登录后执行命令行不需要服务器授权。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能命令行授权功能后，使用该用户线登录的用户只能执行服务器授权的命令，服务器没有授权的命令不能执行。

如果在用户线类视图下使用**command authorization**命令使能了命令行授权功能，则该类型用户线视图都使能命令行授权功能，且用户线视图下无法使用**undo command authorization**恢复缺省情况。

需要注意的是，在用户线视图/用户线类视图下该命令的配置结果将在下次登录设备时生效。

【举例】

\# 设置用户使用VTY 0用户线登录设备时，需要服务器授权才能执行命令。

\<Sysname\> system-view

Sysname line vty 0

Sysname-line-vty0 command authorization{.TerminalDisplayChar}

【相关命令】

·**command accounting**

·**authorization command**（安全命令参考/AAA）

**登录设备 \-- 登录设备命令 \-- databits**

------------------------------------------------------------------------

**[databits**]命令用来设置数据位的个数。

**[undo databits**]命令用来恢复缺省的数据位。

【命令】

**[databits **[{ **5** \| **6** \| **7** \| **8** }]]

**[undo databits**]

【缺省情况】

用户线的数据位为8位。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[5**]：数据位为5位，即使用5比特来表示一个字符。

**[6**]：数据位为6位，即使用6比特来表示一个字符。

**[7**]：数据位为7位，即使用7比特来表示一个字符。

**[8**]：数据位为8位，即使用8比特来表示一个字符。

【使用指导】

访问终端和设备相应用户线下数据位的设置必须一致，双方才能正常通信。

VTY用户线类视图不支持该命令。

【举例】

\# 设置数据位为5位。

\<Sysname\> system-view

Sysname line aux 0

Sysname-line-aux0 databits 5

**登录设备 \-- 登录设备命令 \-- display ip http**

------------------------------------------------------------------------

**[display ip http**]命令用来显示HTTP的状态信息。

【命令】

**[display ip http**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示HTTP的状态信息。

\<Sysname\> display ip http

HTTP port: 80

Basic ACL: 2222

HTTP status: Enabled

表1-1 display ip http命令显示信息描述表

字段

描述

HTTP port

HTTP服务使用的端口号

Basic ACL

与HTTP服务关联的基本访问控制列表号，Not configured表示没有配置

HTTP status

HTTP服务是否开启：

Enabled：表示HTTP服务处于开启状态

Disabled：表示HTTP服务处于关闭状态

【相关命令】

·**ip http ****port**

·**ip http acl**

·**ip http enable**

**登录设备 \-- 登录设备命令 \-- display ip https**

------------------------------------------------------------------------

**[display ip https**]命令用来显示HTTPS的状态信息。

【命令】

**[display ip https**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示HTTPS的状态信息。

\<Sysname\> display ip https

HTTPS port: 443

SSL server policy: test

Certificate access control policy: Not configured

Basic ACL: 2222

HTTPS status: Enabled

表1-2 display ip https命令显示信息描述表

字段

描述

HTTPS port

HTTPS服务使用的端口号

SSL server policy

与HTTPS服务关联的SSL服务器端策略，Not configured表示没有配置

Certificate access-control-policy

与HTTPS服务关联的证书属性访问控制策略,Not configured表示没有配置

Basic ACL

与HTTPS服务关联的基本访问控制列表号，Not configured表示没有配置

HTTPS status

HTTPS服务是否开启：

Enabled：表示{.TableTextChar}HTTPS服务处于开启状态{.TableTextChar}

Disabled：表示HTTPS{.TableTextChar}服务处于关闭状态{.TableTextChar}

【相关命令】

·**ip http****sport**

·**ip https acl**

·**ip https enable**

·**ip https ssl-server-policy**

·**ip https certificate access-control-policy**

**登录设备 \-- 登录设备命令 \-- display line**

------------------------------------------------------------------------

**[display line**]命令用来显示用户线的相关信息。

【命令】

**[display line**[ [ *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* ]  **summary** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[number1*]：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始。

**[aux**]：AUX用户线。

**[console**]：Console用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线。

*[number2*]：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[summary**]：显示用户线的摘要信息。不使用该参数时，将显示用户线类型、绝对/相对编号、传输速率、Modem属性、认证方式及接入接口；使用该参数时，将显示正在使用和未使用的用户线数目和类型。

【举例】

\# 显示用户线0的相关信息。

\<Sysname\> display line 0

  Idx  Type     Tx/Rx      Modem Auth  Int         Location

  0    CON 0    9600       -     N     -           0/0

  +    : Line is active.

  F    : Line is active and in async mode.

  Idx  : Absolute index of line.

  Type : Type and relative index of line.

  Auth : Login authentication mode.

  Int  : Physical port of the line.

  A    : Authentication use AAA.

  N    : No authentication is required.

  P    : Password authentication.

表1-3 display line命令显示信息描述表

字段

描述

+

表示当前正在使用的用户线

F

表示当前正在使用的用户线，且工作在异步方式

Idx

用户线的绝对编号

Type

用户线的类型及相对编号

Tx/Rx

用户线的速率

Modem

Modem的呼入/呼出开关，取值有in（允许呼入）、out（允许呼出）、inout（允许呼入呼出），缺省显示"-"（表示没有配置）

Auth

使用该用户线登录的用户的认证方式，取值有A、L、N和P四种方式

Int

用户线对应的物理接口的简称表示（没有对应接口的用户线均显示"-"，但console口除外，即使console口有对应的物理接口，此处仍显示为"-"）

Location

用户线的物理位置：

·集中式设备：显示为"槽位号/CPU编号"

·分布式设备---独立运行模式：显示为"槽位号/CPU编号"

·分布式设备---IRF模式：显示为"设备成员编号/槽位号/CPU编号"

A

表示使用AAA认证方式，对应的**authentication-mode**为**scheme**

N

表示无需认证，对应的**authentication-mode**为**none**

P

表示使用当前用户线的密码进行认证，对应的**authentication-mode**为**password**

\# 显示所有用户线的摘要信息。

\<Sysname\> display line summary

  Line type : [CON]

           0:U

  Line type : [AUX]

           1:X

  Line type : [VTY]

           2:UXXX X

   2 lines used.      (U)

   5 lines not used.  (X)

表1-4 display line summary命令显示信息描述表

字段

描述

Line type

用户线类型（CON/TTY/AUX/VTY）

0:X

0表示用户线的绝对编号，X表示当前没有用户使用该用户线（U表示当前有用户使用该用户线）。比如"2:UXXX X"表示该行第一个用户线的绝对编号是2，有用户使用；第3、4、5、6号用户线，没有用户使用

lines used.      (U)

当前正在使用的用户线的数目（即U字符的个数）

lines not used.  (X)

当前未使用的用户线的数目（即X字符的个数）

**登录设备 \-- 登录设备命令 \-- display telnet client**

------------------------------------------------------------------------

**[display telnet client**]命令用来显示设备作为Telnet客户端的相关配置信息。

【命令】

**[display telnet client**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

目前该命令显示的是Telnet客户端源IPv4地址或源接口的配置信息。用户可以使用**telnet client source**命令指定Telnet客户端源IPv4地址或源接口。

【举例】

\# 显示设备作为Telnet客户端的相关配置信息。

\<Sysname\> display telnet client

 The source IP address is 1.1.1.1.

以上显示信息表示设备作为Telnet客户端时，发送Telnet报文的源IPv4地址为1.1.1.1。

【相关命令】

·**telnet client source**

**登录设备 \-- 登录设备命令 \-- display user-interface**

------------------------------------------------------------------------

**[display user-interface**]命令用来显示用户线的相关信息。

【命令】

**[display user-interface**[ [ *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* ]  **summary** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[number1*]：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始。

**[aux**]：AUX用户线。

**[console**]：Console用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线。

*[number2*]：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[summary**]：显示用户线的摘要信息。不使用该参数时，将显示用户线类型、绝对/相对编号、传输速率、Modem属性、认证方式及接入接口；使用该参数时，将显示正在使用和未使用的用户线数目和类型。

【使用指导】

该命令实现与**display line**一致，仅为与旧版本兼容保留，请使用**display line**。

【举例】

\# 显示用户线0的相关信息。

\<Sysname\> display user-interface 0

  Idx  Type     Tx/Rx      Modem Auth  Int        Location

  0    CON 0    9600       -     N     -         0/0

  +    : Line is active.

  F    : Line is active and in async mode.

  Idx  : Absolute index of line.

  Type : Type and relative index of line.

  Auth : Login authentication mode.

  Int  : Physical port of the line.

  A    : Authentication use AAA.

  N    : No authentication is required.

  P    : Password authentication.

表1-5 display user-interface命令显示信息描述表

字段

描述

+

表示当前正在使用的用户线

F

表示当前正在使用的用户线，且工作在异步方式

Idx

用户线的绝对编号

Type

用户线的类型及相对编号

Tx/Rx

用户线的速率

Modem

Modem的呼入/呼出开关，取值有in（允许呼入）、out（允许呼出）、inout（允许呼入呼出），缺省显示"-"（表示没有配置）

Auth

使用该用户线登录的用户的认证方式，取值有A、L、N和P四种方式

Int

用户线对应的物理接口的简称表示（没有对应接口的用户线均显示"-"）

Location

用户线的物理位置：

·集中式设备：显示为"槽位号/CPU编号"

·分布式设备---独立运行模式：显示为"槽位号/CPU编号"

·分布式设备---IRF模式：显示为"设备成员编号/槽位号/CPU编号"

A

表示使用AAA认证方式，对应的**authentication-mode**为**scheme**

N

表示无需认证，对应的**authentication-mode**为**none**

P

表示使用当前用户线的密码进行认证，对应的**authentication-mode**为**password**

\# 显示所有用户线的摘要信息。

\<Sysname\> display user-interface summary

  Line type : [CON]

           0:U

  Line type : [AUX]

           1:X

  Line type : [VTY]

           2:UXXX X

   2 lines used.      (U)

   5 lines not used.  (X)

表1-6 display user-interface summary命令显示信息描述表

字段

描述

Line type

用户线类型（CON/TTY/AUX/VTY）

0:X

0表示用户线的绝对编号，X表示当前没有用户使用该用户线（U表示当前有用户使用该用户线）。比如"2:UXXX X"表示该行第一个用户线的绝对编号是2，有用户使用；第3、4、5、6号用户线，没有用户使用

lines used.      (U)

当前正在使用的用户线的数目（即U字符的个数）

lines not used.  (X)

当前未使用的用户线的数目（即X字符的个数）

**登录设备 \-- 登录设备命令 \-- display users**

------------------------------------------------------------------------

**[display users**]命令用来显示当前正在使用的用户线以及用户的相关信息。

**[display users all**]命令用来显示设备支持所有用户线以及用户的相关信息。

【命令】

**[display users** [ **all** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示设备支持的所有用户线以及用户的相关信息。

【举例】

\# 显示当前正在使用的用户线以及用户的相关信息。

\<Sysname\> display users

  Idx  Line     Idle       Time              Pid     Type

  10   VTY 0    00:10:49   Jun 11 11:27:32   320     TEL

+ 11   VTY 1    00:00:00   Jun 11 11:39:40   334     TEL

Following are more details.

VTY 0   :

        Location: 192.168.1.12

VTY 1   :

        Location: 192.168.1.26

 +    : Current operation user.

 F    : Current operation user works in async mode.

以上显示信息表明，当前有两个用户已经登录设备，用户自己使用的是VTY 1用户线，用户的IP地址为192.168.1.26；另一个用户使用的是VTY 0用户线。

表1-7 display users命令显示信息描述表

字段

描述

Idx

用户线的绝对编号

Line

用户线的相对编号，第一列（比如VTY）表示用户线的类型，第二列（比如0）表示用户线的相对编号

Idle

空闲时间，表明用户和设备没有报文交互的时间长度，格式为hh:mm:ss。当空闲时间大于等于24小时时，显示为old

Time

用户本次登录的时间

Pid

用户对应的进程ID（CLI用户登录时，系统会自动运行一个用户登录进程来监控用户的操作）

Type

显示用户的登录类型，如Telnet、SSH、PAD

+

当前操作用户

Location

使用该用户线登录的用户的位置信息（即用户的IP地址）

F

当前操作用户工作在异步模式

**登录设备 \-- 登录设备命令 \-- display web menu**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display web menu**]命令用来显示Web的页面菜单树。

【命令】

**[display web menu**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

当用户需要配置角色对应的web菜单项时，可使用这个命令来查看系统支持的全部菜单树。

【举例】

\# 显示全部web菜单信息。

\<Sysname\> display web menu

  .

    \`\--Device: ID = m_device

[         \|\--Summary: ID = m_panel]

[         \|    \|\--System Information: ID = i_main]

[         \|    \`\--Device Information: ID = i_panel]

[         \|\--Basic Settings: ID = m_device_basic]

[         \|    \|\--Device Name: ID = i_device_sysname]

[         \|    \`\--Web Idle Timeout: ID = i_device_webidle]

[         \|\--Device Maintenance: ID = m_maintains]

[         \|    \`\--Reboot: ID = i_reboot]

[         \|\--System Time: ID = m_datetime]

[         \|    \|\--UTC Time: ID = i_systime]

[         \|    \`\--Time Zone: ID = i_timezone]

[         \|\--System Log: ID = m_log]

[         \|    \|\--Log List: ID = i_syslog]

[         \|    \|\--Log Host: ID = i_loghost]

[         \|    \`\--Log Setup: ID = i_logsetup]

[         \|\--Port Management: ID = m_port]

[         \|    \|\--Summary: ID = i_portsummary]

[         \|    \`\--Setup: ID = i_portsetup]

[         \|\--Interface Statistics: ID = m_int_statistic]

[         \|    \`\--Interface Statistics: ID = i_statistic_summary]

         \`\--Configuration: ID = m_config

[              \|\--Save: ID = i_save]

[              \|\--Backup: ID = i_backup]

[              \|\--Restore: ID = i_restore]

[              \|\--Import: ID = i_import]

              \`\--Export: ID = i_export

**登录设备 \-- 登录设备命令 \-- display web users**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display web users**]命令用来显示当前Web用户的相关信息。

【命令】

**[display web users**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示当前Web用户的相关信息。

\<Sysname\> display web users

UserID          Name            Type   Language JobCount LoginTime LastOperation

AB2039483271293 Administrator   HTTP   Chinese     3     12:00:23  14:10:05

F09382BA2014AC8 user            HTTPS  English     1     13:05:00  14:11:00

表1-8 display web users命令显示信息描述表

字段

描述

UserID

Web用户的ID号，用来唯一标识一个登录用户

Name

Web用户的登录用户名

Type

Web用户登录使用的协议类型：

·HTTP表示Hypertext Transfer Protocol

·HTTPS表示基于安全套接字的Hypertext Transfer Protocol

Language

Web用户登录时使用的语言：

·Chinese表示中文

·English表示英文

JobCount

Web用户建立的连接数量

LoginTime

Web用户的登录时间

LastOperation

Web用户的最后操作时间

**登录设备 \-- 登录设备命令 \-- escape-key**

------------------------------------------------------------------------

**[escape-key**]命令用来配置终止当前运行任务（比如**ping**命令等）的快捷键。

**[undo escape-key**]命令用来取消快捷键的配置，包括缺省快捷键。

【命令】

**[escape-key**[ { *key-string* \| **default** }]]

**[undo escape-key**]

【缺省情况】

按\<Ctrl+C\>组合键终止当前运行的任务。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[key-string*]：定义终止当前运行任务的快捷键，可以是区分大小写的单个字符，也可以是单个字符或组合键对应的ACSII码（0～127）。比如设置**escape-key** 65，此时生效快捷键为A；如果设置**escape-key **a，生效的快捷键为a。

**[default**]：恢复为缺省的快捷键\<Ctrl+C\>。

【使用指导】

有些命令行执行时间比较长，比如ping时指定发送1000个包、tracert时目的地址不可达，系统执行这些命令时，在当前用户线下用户无法输入其他命令。此时，用户可以按\<Ctrl+C\>组合键来终止ping或者tracert任务，以便输入新的命令。如果配置了**escape-key**，则用户可以用新配置的快捷键来代替\<Ctrl+C\>。命令行是否支持\<Ctrl+C\>终止与功能模块的软件实现有关，请参见相关命令行的描述。

如果设置的快捷键为单个字符，且当前有任务可终止，则输入快捷键会终止命令的执行；如果当前没有任务可终止，则输入的快捷键会作为普通的编辑字符。如果在某用户线下设置了*key-string*，当使用该用户线登录到设备，又通过该设备telnet到别的设备，这时的*key-string*将被视为控制字符，只能用来中止当前的任务，不能作为编辑字符输入。比如，在Device A的VTY 0用户线下指定*key-string*为e，此时，PC（超级终端）使用VTY 0用户线登录设备，在PC上e可以作为编辑字符输入，也可以用e来中止Device A上正在运行的任务。如果通过Device A再telnet到Device B，则此时，PC上只能使用e来中止Device B上正在运行的任务，不能作为编辑字符输入。所以，建议用户尽量将*key-string*配置为组合键。

多次执行该命令配置不同的快捷键时，最新的配置生效。新设置的快捷键可以使用**display current-configuration**命令来查看。

如果用户线视图下配置**escape-key**为缺省值，并且此时用户线类视图下配置了**escape-key**，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。

需要注意的是，用户线视图下使用本命令配置的快捷键立即生效；用户线类视图下配置的快捷键将在下次登录时生效。

【举例】

\# 配置终止当前运行任务的快捷键为a。

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 escape-key a

验证过程如下：

·使用**ping**命令检查IP地址为192.168.1.49的设备是否可达，并用**-c**参数指定发送ICMP回显请求报文的数目为20。

\<Sysname\> ping -c 20 192.168.1.49

  PING 192.168.1.49: 56  data bytes, press a to break

    Reply from 192.168.1.49: bytes=56 Sequence=1 ttl=255 time=3 ms

    Reply from 192.168.1.49: bytes=56 Sequence=2 ttl=255 time=3 ms

·键入a，任务立即终止，并返回到当前视图。

  \-\-- 192.168.1.49 ping statistics \-\--

    2 packet(s) transmitted

    2 packet(s) received

    0.00% packet loss

    round-trip min/avg/max = 3/3/3 ms

\<Sysname\>

**登录设备 \-- 登录设备命令 \-- flow-control**

------------------------------------------------------------------------

**[flow-control**]命令用来配置流量控制方式。

**[undo flow-control**]命令用来恢复缺省情况。

【命令】

(1)不支持*direction1*、*direction2*参数的设备：

**[flow-control **[{ **hardware** \| **none** \| **software** }]]

**[undo flow-control**]

(2)支持*direction1*、*direction2*参数的设备：

**[flow-control **[{ **hardware** \| **none** \| **software** }]]

**[flow-control hardware** *direction1* [ **software** *direction2* ]]

**[flow-control software** *direction1* [ **hardware** *direction2* ]]

**[undo flow-control**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hardware**]：进行硬件方式的流量控制。

**[none**]：不进行流量控制。

**[software**]：进行软件方式的流量控制。

*[direction1*]、*direction2*：表示流量控制的方向，取值为**in**或**out**，**in**表示入方向，即本设备接受远端设备流量控制；**out**表示出方向，即本设备流量控制远端设备。*direction1*和*direction2*参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

(1)不支持*direction1*、*direction2*参数的设备：

流量控制分为入方向和出方向，入方向表示本设备能够接受远端设备的流量控制，出方向表示本设备能够对远端设备进行流量控制。配置该命令后，指定的流量控制方式对入方向和出方向都生效。

要使流量控制生效，双方才能正常通信，对端设备也要配置相同的流量控制方式。

(2)支持*direction1*、*direction2*参数的设备：

流量控制分为**in**和**out**两个方向，**in**表示本设备能够接受远端设备流量控制，**out**表示本设备能够流量控制远端设备。流量控制方式又分为**hardware**、**software**和**none**三种，同一个方向，只能配置一种流量控制方式。

·如果要给**in**和**out**方向配置相同的流量控制方式，请使用命令**flow-control**[ { **hardware** \| **software** \| **none** }]。

·如果要给**in**和**out**方向配置不同的流量控制方式，请使用命令**flow-control hardware** *direction1* [ **software** *direction2* ]或**flow-control software** *direction1* [ **hardware** *direction2* ]。当不指定可选参数时，表示另一个方向的流量控制方式为**none**（比如配置**flow-control hardware in**，则系统会自动将**out**方向配置为无流量控制）。

要使流量控制生效，本设备上**in**（**out**）方向配置的流量控制方式和对端设备上**out**（**in**）方向配置

的流量控制方式必须相同。

VTY用户线视图不支持该命令。

【举例】

\# 配置Console 0用户线视图下，入方向和出方向都采用软件流量控制方式。

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 flow-control software

\# 配置Console 0用户线视图下，入方向采用硬件流量控制方式，出方向不进行流量控制。（支持*direction1*、*direction2*参数的设备才支持该举例）

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 flow-control hardware in

\# 配置Console 0用户线视图下，入方向采用硬件流量控制方式，出方向采用软件流量控制方式。（支持*direction1*、*direction2*参数的设备才支持该举例）

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 flow-control hardware in software out

**登录设备 \-- 登录设备命令 \-- free line**

------------------------------------------------------------------------

**[free line**]命令用来释放指定用户线上建立的连接。

【命令】

**[free line****[{ *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number1*]：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始。

**[aux**]：AUX用户线。

**[console**]：Console用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线。

*[number2*]：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

用户不能使用该命令释放自己的连接。

【举例】

\# 释放用户线上VTY 1建立的连接。

·查看当前有哪些用户正在操作设备。

\<Sysname\> display users

  Idx  Line     Idle       Time              Pid     Type

  10   VTY 0    00:10:49   Jun 11 11:27:32   320     TEL

+ 11   VTY 1    00:00:00   Jun 11 11:39:40   334     TEL

Following are more details.

VTY 0   :

        Location: 192.168.1.12

VTY 1   :

        Location: 192.168.1.26

 +    : Current operation user.

 F    : Current operation user works in async mode.

·假设VTY 1用户的操作影响到网络管理员当前的操作，将他强制下线。

\<Sysname\> free line vty 1

Are you sure to free line vty1? [Y/N:y]

 OK

**登录设备 \-- 登录设备命令 \-- free user-interface**

------------------------------------------------------------------------

**[free user-interface**]命令用来释放指定用户线上建立的连接。

【命令】

**[free user-interface****[{ *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number1*]：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始。

**[aux**]：AUX用户线。

**[console**]：Console用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线。

*[number2*]：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

用户不能使用该命令释放自己的连接。

该命令实现与**free line**一致，仅为与旧版本兼容保留，请使用**free line**。

【举例】

\# 释放用户线上VTY 1建立的连接。

·查看当前有哪些用户正在操作设备。

\<Sysname\> display users

  Idx  LINE     Idle       Time              Pid     Type

  10   VTY 0    00:10:49   Jun 11 11:27:32   320     TEL

+ 11   VTY 1    00:00:00   Jun 11 11:39:40   334     TEL

Following are more details.

VTY 0   :

        Location: 192.168.1.12

VTY 1   :

        Location: 192.168.1.26

 +    : Current operation user.

 F    : Current operation user works in async mode.

·假设VTY 1用户的操作影响到网络管理员当前的操作，将他强制下线。

\<Sysname\> free user-interface vty 1

Are you sure to free line vty1? [Y/N:y]

 OK

**登录设备 \-- 登录设备命令 \-- free web users**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[free web users**]命令用来强制在线Web用户下线。

【命令】

**[free web users**[ { **all** \| **user-id** *user-id* \| **user-name** *user-name* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有Web用户。

*[user-id*]：Web用户的ID号，为15位十六进制数。系统会自动为每位成功登录的Web用户分配一个用户ID，用户ID用于唯一标识Web用户。

**[user-name** *user-name*]：Web用户的用户名，为1～255个字符的字符串，区分大小写。

【使用指导】

管理员在管理需要时，可以使用该命令强制下线部分或全部的Web用户。

【举例】

\# 强制所有在线Web用户下线。

\<Sysname\> free web users all

【相关命令】

·**display web users**

**登录设备 \-- 登录设备命令 \-- history-command max-size**

------------------------------------------------------------------------

**[history-command max-size**]命令用来设置可以存储的当前用户线下历史命令的条数。

**[undo history-command max-size**]命令用来恢复缺省情况。

【命令】

**[history-command max-size ***size-value*]

**[undo history-command max-size**]

【缺省情况】

历史命令缓冲区可存储10条历史命令。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size-value*]：可存储的历史命令的条数，取值范围为0～256。

【使用指导】

每个用户线对应一个历史命令缓冲区，缓冲区里保存了当前用户最近执行成功的命令，缓冲区的容量决定了可以保存的历史命令的数目。用户使用**display history-command**命令、上光标键↑或下光标键↓可以随时了解近期成功执行了哪些操作（**display history-command**命令的详细介绍请参见"基础配置命令参考"中的"CLI"）。同时登录设备的不同用户拥有不同的历史命令缓冲区，互不影响。

用户退出当前会话时，系统会自动清除相应历史命令缓冲区内保存的历史命令。

如果用户线视图下配置**history-command max-size**为缺省值，并且此时用户线类视图下配置了**history-command max-size**，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。

需要注意的是，在用户线视图下使用本命令配置的当前用户线下可存储的历史命令条数立即生效；用户线类视图下配置的可存储的历史命令条数将在下次登录时生效。

【举例】

\# 设置Console用户线下历史命令缓冲区最多可以存储20条历史命令。

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 history-command max-size 20

**登录设备 \-- 登录设备命令 \-- idle-timeout**

------------------------------------------------------------------------

**[idle-timeout**]命令用来设置用户连接的超时时间。

**[undo idle-timeout**]命令用来恢复缺省情况。

【命令】

**[idle-timeout ***minutes * *seconds* ]

**[undo idle-timeout**]

【缺省情况】

超时时间为10分钟。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：指定超时时间，取值范围为0～35791，单位为分钟。

*[seconds*]：指定超时时间，取值范围为0～59，单位为秒，缺省值为0秒。

【使用指导】

·用户登录后，如果在超时时间内设备和用户间没有消息交互，则超时时间到达时设备会自动断开用户连接。

·当超时时间设置为0时，表示设备不会因为超时自动断开用户连接。

·如果用户线视图下配置**idle-timeout**为缺省值，并且此时用户线类视图下配置了**idle-timeout**，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。

·用户线视图下使用本命令配置的连接超时时间立即生效；用户线类视图下配置的连接超时时间将在下次登录时生效。

【举例】

\# 设置Console用户线下用户连接超时时间为1分钟30秒。

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 idle-timeout 1 30

**登录设备 \-- 登录设备命令 \-- ip alias**

------------------------------------------------------------------------

**[ip alias**]命令用来建立Telnet重定向监听端口与IP地址的对应关系。

**[undo ip alias**]命令用来恢复缺省情况。

【命令】

**[ip alias **]*ip-address port-number*

**[undo ip alias **]*ip-address*

【缺省情况】

Telnet重定向监听端口与IP地址没有对应关系。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：与Telnet重定向监听端口对应的IP地址。该地址不能为设备上接口的地址，但可以和接口地址同一网段。

*[port-number*]：Telnet重定向的监听端口，取值范围为2000～50000。

【使用指导】

用户和设备A相连，能够Telnet登录到设备A，设备A通过AUX口/异步串口和设备B相连。在设备A上配置**redirect enable**和**redirect listen-port ***port-number*后，用户就可以使用"telnet 设备A的IP地址 *port-number*"来登录设备B，相当于用户直接Telnet登录设备B。如果再使用**ip alias ***ip-address port-number*建立Telnet重定向监听端口与IP地址的对应关系后，用户就可以直接执行"**telnet***ip-address*"来登录设备B。

【举例】

\# 配置Telnet重定向监听端口2000对应的IP地址为1.1.1.1。

\<Sysname\> system-view

Sysname ip alias 1.1.1.1 2000

【相关命令】

·**redirect enable**

·**redirect listen-port**

·**display tcp**（请参考三层技术-IP业务）

**登录设备 \-- 登录设备命令 \-- ip http acl**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip http acl**]命令用来配置HTTP服务与ACL关联。

**[undo ip http acl**]命令用来恢复缺省情况。

【命令】

**[ip http acl **[{ *acl-number* \| **name** *acl-name* }]]

**[undo ip http acl**]

【缺省情况】

HTTP服务没有与任何ACL关联。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：ACL的编号，取值范围为2000～2999（基本IPv4 ACL）。

**[name*** acl*-name]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a\~z或A\~Z开头。为避免混淆，ACL的名称不允许使用英文单词all。仅当指定名称的ACL存在且为基本IPv4 ACL时生效。

【使用指导】

FIPS模式下，不支持本命令。

配置HTTP服务与ACL关联后，只有ACL允许通过的HTTP客户端能够通过Web方式登录设备。不匹配ACL或ACL拒绝通过的HTTP客户端将不能通过Web方式登录设备。

多次执行该命令最新配置生效。

【举例】

\# 配置HTTP服务与ACL 2001关联，只允许10.10.0.0/16网段的客户端通过Web访问设备。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit source 10.10.0.0 0.0.255.255

Sysname-acl-ipv4-basic-2001 quit

Sysname ip http acl 2001

【相关命令】

·**acl**（ACL和QoS命令参考/ACL）

**登录设备 \-- 登录设备命令 \-- ip http enable**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip http enable**]命令用来使能HTTP服务。

**[undo ip http enable**]命令用来关闭HTTP服务。

【命令】

**[ip http enable**]

**[undo ip http enable**]

【缺省情况】

HTTP服务处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

FIPS模式下，不支持本命令。

使能HTTP服务后，用户才能通过Web使用HTTP方式登录设备。

使用Web方式登录设备，用户输入的用户名和密码属于敏感信息，Web登录请求采用HTTPS方式发送到Web服务器。所以，即使用户希望使用HTTP方式访问Web，也必须先开启设备的HTTPS服务才能成功的登录。

【举例】

\# 使能HTTP服务。

\<Sysname\> system-view

Sysname ip http enable

【相关命令】

·**ip https enable**

**登录设备 \-- 登录设备命令 \-- ip http port**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip http port**]命令用来配置HTTP服务的端口号。

**[undo ip http port**]命令用来恢复缺省情况。

【命令】

**[ip http **]**port ***port-number*

**[undo ip http **]**port**

【缺省情况】

HTTP服务的端口号为80。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：HTTP服务的端口号，取值范围为1～65535。

【使用指导】

FIPS模式下，不支持本命令。

如果修改端口号前HTTP服务是开启的，则修改端口号后系统会自动重启HTTP服务，正在访问的用户将被断开，用户需要在浏览器的地址栏中重新输入新的地址后才可以继续访问。

【举例】

\# 配置HTTP服务的端口号为80。

\<Sysname\> system-view

Sysname ip http port 80

**登录设备 \-- 登录设备命令 \-- ip https acl**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip https acl**]命令用来配置HTTPS服务与ACL关联。

**[undo ip https acl**]命令用来恢复缺省情况。

【命令】

**[ip https acl ***[acl-number *[\| **name** *acl-name* }]]

**[undo ip https acl**]

【缺省情况】]

HTTPS服务没有与任何ACL关联。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：ACL的编号，取值范围为2000～2999（基本IPv4 ACL）。

**[name ***acl*-name]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a\~z或A\~Z开头。为避免混淆，ACL的名称不允许使用英文单词all。仅当指定名称的ACL存在且为基本IPv4 ACL时生效。

【使用指导】

配置HTTPS服务与ACL关联后，只有ACL允许通过的HTTPS客户端能够通过Web方式登录设备。不匹配ACL或ACL拒绝通过的HTTPS客户端将不能通过Web方式登录设备。

需要注意的是，Web登录时用户输入的用户名和密码属于敏感信息，Web登录请求采用HTTPS方式发送到Web服务器。所以，如果本命令中的ACL规则拒绝客户端通过HTTPS服务访问Web页面，那么该客户端也无法通过HTTP服务访问Web页面。

多次执行该命令最新配置生效。

【举例】

\# 配置HTTPS服务与ACL 2001关联，只允许10.10.0.0/16网段的客户端通过Web访问设备。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit source 10.10.0.0 0.0.255.255

Sysname-acl-ipv4-basic-2001 quit

Sysname ip https acl 2001

【相关命令】

·**acl**（ACL和QoS命令参考/ACL）

**登录设备 \-- 登录设备命令 \-- ip https certificate access-control-policy**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip https certificate access-control-policy**]命令用来配置HTTPS服务与证书属性访问控制策略关联。

**[undo ip https certificate access-control-policy**]命令用来恢复缺省情况。

【命令】

**[ip https certificate access-control-policy ***policy-name*]

**[undo ip https certificate access-control-policy**]

【缺省情况】

HTTPS服务没有与任何证书属性访问控制策略关联。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：证书属性访问控制策略名，为1～31个字符的字符串，区分大小写。

【使用指导】

通过将HTTPS服务与已配置的客户端证书属性访问控制策略关联，可以实现对客户端的访问权限进行控制。证书属性访问控制策略的相关介绍请参见"安全配置指导"中"PKI"。

【举例】

\# 设置HTTPS服务使用的证书属性访问控制策略为myacl。

\<Sysname\> system-view

Sysname ip https certificate access-control-policy myacl

【相关命令】

·**pki certificate access-control-policy**（PKI命令参考/PKI）

**登录设备 \-- 登录设备命令 \-- ip https enable**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip https enable**]命令用来使能HTTPS服务。

**[undo ip https enable**]命令用来关闭HTTPS服务。

【命令】

**[ip https enable**]

**[undo ip https enable**]

【缺省情况】

HTTPS服务处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有使能该功能后，用户才能通过Web方式使用HTTPS登录设备。

需要注意的是，使能HTTPS服务，会触发SSL的握手协商过程。在SSL握手协商过程中，如果设备的本地证书已经存在，则SSL协商可以成功，HTTPS服务可以正常启动；如果设备的本地证书不存在，则SSL协商过程会触发证书申请流程。由于证书申请需要较长的时间，会导致SSL协商不成功，从而无法正常启动HTTPS服务。因此，在这种情况下，需要多次执行**ip https enable**命令，这样HTTPS服务才能正常启动。

【举例】

\# 使能HTTPS服务。

\<Sysname\> system-view

Sysname ip https enable

【相关命令】

·**ip https ssl-server-policy**

·**ip https certificate access-control-policy**

**登录设备 \-- 登录设备命令 \-- ip https port**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip https port**]命令用来配置HTTPS服务的端口号。

**[undo ip https port**]命令用来恢复缺省情况。

【命令】

**[ip https **]**port** *port-number*

**[undo ip https **]**port**

【缺省情况】

HTTPS服务的端口号为443。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：HTTPS服务的端口号，取值范围为1～65535。

【使用指导】

如果修改端口号前HTTPS服务是开启的，则修改端口号后系统会自动重启HTTPS服务，正在访问的用户将被断开，用户需要在浏览器的地址栏中重新输入新的地址后才可以继续访问。

【举例】

\# 配置HTTPS服务的端口号为8080。

\<Sysname\> system-view

Sysname ip https port 8080

**登录设备 \-- 登录设备命令 \-- ip https ssl-server-policy**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip https ssl-server-policy**]命令用来配置HTTPS服务与SSL服务器端策略关联。

**[undo ip https ssl-server-policy**]命令用来恢复缺省情况。

【命令】

**[ip https ssl-server-policy ***policy-name*]

**[undo ip https ssl-server-policy**]

【缺省情况】

HTTPS服务没有与任何SSL服务器端策略关联，HTTPS使用自签名证书。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL服务器端策略名，为1～31个字符的字符串。

【使用指导】

·关闭HTTPS服务后，系统将自动取消HTTPS服务与SSL服务器端策略的关联。再次使能HTTPS服务之前，需要重新配置HTTPS服务与SSL服务器端策略关联。

·HTTPS服务处于使能状态时，对与其关联的SSL服务器端策略进行的修改不会生效。

【举例】

\# 设置HTTPS服务使用的SSL服务器端策略为myssl。

\<Sysname\> system-view

Sysname ip https ssl-server-policy myssl

【相关命令】

·**ssl server-policy**（安全命令参考/SSL）

**登录设备 \-- 登录设备命令 \-- line**

------------------------------------------------------------------------

**[line**]命令用来进入一个或多个用户线视图。

【命令】

**[line** { *first-number1* [ *last-number1*  \| { **aux** \| **console** \| **tty** \| **vty** } *first-number2*  *last-number2*  }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[first-number1*]：第一个用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始。

*[last-number1*]：最后一个用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始，但不能小于*first-number1*。

**[aux**]：AUX用户线。

**[console**]：Console用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线。

*[first-number2*]：第一个用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[last-number2*]：最后一个用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但不能小于*first-number2*。

【使用指导】

·进入一个用户线视图进行配置后，该配置只对该用户视图有效。

·进入多个用户线视图进行配置后，该配置对这些用户视图均有效。

【举例】

\# 进入Console 0用户线视图。

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0

\# 进入VTY 0～4用户线视图。

\<Sysname\> system-view

Sysname line vty 0 4

Sysname-line-vty0-4

【相关命令】

·**line class**

**登录设备 \-- 登录设备命令 \-- line class**

------------------------------------------------------------------------

**[line class**]命令用来进入指定用户线类视图。

【命令】

**[line class **[{ **aux** \| **console** \| **tty** \| **vty** }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aux**]：AUX用户线类。

**[console**]：Console用户线类。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线类。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线类。

【使用指导】

**[line class**]命令用来进入指定用户线类视图，**line**命令用来进入一个或多个用户线视图。对于同时支持这两种视图的命令：

·用户线视图下的配置优先于用户线类视图下的配置。

·用户线视图下的配置只对该用户线生效。

·用户线类视图下的配置修改不会立即生效，当用户下次登录后所修改的配置值才会生效。

·用户线视图下的属性配置为缺省值时，将采用用户线类视图下配置的值。如果用户线类视图下的属性配置也为缺省值时，则直接采用该属性的缺省值。

用户线类视图下支持的命令有：

·**activation-key**

·**auto-execute command**

·**authentication-mode**

·**command accounting**

·**command authorization**

·**escape-key**

·**history-command max-size**

·**idle-timeout**

·**protocol inbound**

·**screen-length**

·**set authentication password**

·**shell**

·**terminal type**

·**user-role**

【举例】

\# 将VTY用户线参数------用户连接的超时时间的缺省值设置为15分钟。

\<Sysname\> system-view

Sysname line class vty

Sysname-line-class-vty idle-timeout 15

\# 在console用户线类视图下，将启动Console口终端会话的快捷键设置为\<s\>。

\<Sysname\> system-view

Sysname line class console

Sysname-line-class-console activation-key s

Sysname-line-class-console quit

·在console用户线视图下，将启动Console口终端会话的快捷键设置为缺省值（可以使用undo activation-key或者直接使用activation-key 13进行配置）。

Sysname line console 0

Sysname-line-console0 undo activation-key

·此时生效的快捷键为用户线类视图下的配置，验证过程如下：

·退出Console口终端会话。

Sysname-line-console0 return

\<Sysname\> quit

·重新使用Console口登录设备，能看到如下显示信息。

Press ENTER to get started.

·此时，\<Enter\>键失效，需要按\<s\>键才能出现用户视图提示符，启动Console口终端会话。

\<Sysname\>

【相关命令】

·**line**

**登录设备 \-- 登录设备命令 \-- lock**

------------------------------------------------------------------------

**[lock**]命令用来锁住当前用户线，防止未授权的用户操作该用户线。

【命令】

**[lock**]

【缺省情况】

系统不会自动锁住当前用户线。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

FIPS模式下，不支持本命令。

用户输入**lock**命令后，系统提示输入密码（密码最大长度为16个字符），并提示再次输入密码，只有两次输入的密码相同，Lock操作才能成功。之后，如果用户要再进入系统，需要按回车键，并输入刚才配置的密码后，才能结束锁定，进入系统。

【举例】

\# 锁住当前用户线然后解锁。

\<Sysname\> lock

Please input password\<1 to 16\> to lock current line:

Password:

Again:

                   locked !

此时，命令行用户线被锁定。键入回车，并输入正确的密码后，可以解锁。

Password:

\<Sysname\>

**登录设备 \-- 登录设备命令 \-- parity**

------------------------------------------------------------------------

**[parity**]命令用来设置校验位的解析和生成方式。

**[undo parity**]命令用来恢复缺省情况。

【命令】

**[parity**[ { **even** \| **mark** \| **none** \| **odd** \| **space** }]]

**[undo parity**]

【缺省情况】

设备校验位的校验方式为**none**，即不进行校验。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[even**]：进行偶校验。

**[mark**]：进行标记校验。

**[none**]：无校验。

**[odd**]：进行奇校验。

**[space**]：进行空格校验。

【使用指导】

访问终端和设备相应用户线下校验位的设置必须一致，双方才能正常通信。

VTY用户线视图不支持该命令。

【举例】

\# 将AUX口传输校验位设为奇校验。

\<Sysname\> system-view

Sysname line aux 0

Sysname-line-aux0 parity odd

**登录设备 \-- 登录设备命令 \-- protocol inbound**

------------------------------------------------------------------------

**[protocol inbound**]命令用来指定所在用户线支持的协议。

**[undo** **protocol inbound**]命令用来恢复缺省情况。

【命令】

非FIPS模式下：

**[protocol inbound**[ { **all** \| **pad** \| **ssh** \| **telnet** }]]

**[undo** **protocol inbound**]

FIPS模式下：

**[protocol inbound** **ssh**]

**[undo** **protocol inbound**]

【缺省情况】

非FIPS模式下：系统支持所有协议。

FIPS模式下：系统支持SSH协议。

【视图】

VTY用户线视图/VTY用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：支持所有的协议，包括Telnet、SSH和PAD。

**[pad**]：支持PAD协议。该参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[ssh**]：支持SSH协议。

**[telnet**]：支持Telnet协议。

【使用指导】

如果要配置用户线支持SSH协议，必须先将该用户的认证方式配置为**scheme**，否则**protocol inbound ssh**命令会执行失败。相关配置可参考命令**authentication-mode**。

用户线视图下，该命令的配置结果将在下次登录时生效。

用户线视图下，对**authentication-mode**和**protocol inbound**进行关联绑定。

当这两条命令均配置为缺省值，此时该用户线视图下的这两条命令配置值均取该类用户线类视图下的相应的配置；若该类用户线类视图下没有进行相应的配置，则均取缺省值。

当两条命令中的任意一条配置了非缺省值，那么另外一条取缺省值。当两条命令都配置成非缺省值，则均取用户线下的配置值。

【举例】

\# 设置用户线VTY 0到VTY 4只支持SSH协议。

\<Sysname\> system-view

Sysname line vty 0 4

Sysname-line-vty0-4 authentication-mode scheme

Sysname-line-vty0-4 protocol inbound ssh

\# 设置VTY用户线类支持SSH协议，认证方式为scheme。同时设置用户线VTY 0到VTY 4不进行登陆认证，支持所有的协议。

\<Sysname\> system-view

Sysname line class vty

Sysname-line-class-vty authentication-mode scheme

Sysname-line-class-vty protocol inbound ssh

Sysname-line-class-vty line vty 0 4

Sysname-line-vty0-4 authentication-mode none

验证过程如下：

·使用Telnet方式登陆，无需认证即可成功登陆。

\<Client\> telnet 192.168.1.241

Trying 192.168.1.241 \...

Press CTRL+K to abort

Connected to 192.168.1.241 \...

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \*

\* Without the owner\'s prior written consent,                                 \*

\* no decompiling or reverse-engineering shall be allowed.                    \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\<Server\>

·查看当前正在使用的用户线以及用户的相关信息，用户线为line 0，则证明该配置下用户线下配置生效。

\<Server\> display users

  Idx  Line     Idle       Time              Pid     Type

+ 50   VTY 0    00:00:00   Jan 17 15:29:27   189     TEL

Following are more details.

VTY 0   :

        Location: 192.168.1.186

 +    : Current operation user.

 F    : Current operation user works in async mode.

**登录设备 \-- 登录设备命令 \-- redirect disconnect**

------------------------------------------------------------------------

**[redirect disconnect**]命令用来强制断开已经建立的Telnet重定向连接。

【命令】

**[redirect disconnect**]

【视图】

AUX/TTY用户线视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 强制断开已经建立的Telnet重定向连接。

\<Sysname\> system-view

Sysname line tty 1

Sysname-line-tty1 redirect disconnect

【相关命令】

·**redirect enable**

·**display tcp**

**登录设备 \-- 登录设备命令 \-- redirect enable**

------------------------------------------------------------------------

**[redirect enable**]命令用来使能当前用户线的Telnet重定向功能。

**[undo redirect enable**]命令用来用来恢复缺省情况。

【命令】

**[redirect enable**]

**[undo redirect enable**]

【缺省情况】

当前用户线的重定向功能处于关闭状态。

【视图】

AUX/TTY用户线视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

用户和设备A相连，能够Telnet登录到设备A；设备A通过AUX口/异步串口和设备B相连，如果设备B要给用户提供Telnet服务，但又不方便告知用户IP地址时，可以在设备A上配置Telnet重定向功能，则用户执行"telnet 设备A的IP地址 特定端口号"（该端口号由**redirect listen-port**命令决定）能够登录设备B，相当于用户直接Telnet登录设备B。

重定向服务器与目的设备相连端口对应的用户线的传输速率和停止位的设置必须相同，否则重定向将失败。

·传输速率可以通过**speed**命令进行设置。

·传输速率的设置，请先使用**stopbit-error intolerance**命令检测重定向设备与目的设备的停止位设置是否相同。如不相同，可以通过**stopbits**命令进行设置。

【举例】

\# 使能TTY 7用户线的Telnet重定向功能。

\<Sysname\> system-view

Sysname line tty 7

Sysname-line-tty7 redirect enable

【相关命令】

·**telnet**

·**display tcp**（请参考三层技术-IP业务）

**登录设备 \-- 登录设备命令 \-- redirect listen-port**

------------------------------------------------------------------------

**[redirect listen-port**]命令用来设置Telnet重定向的监听端口。

**[undo redirect listen-port**]命令用来恢复缺省的监听端口。

【命令】

**[redirect listen-port ***port-number*]

**[undo redirect listen-port**]

【缺省情况】

Telnet重定向的监听端口号为用户线的绝对编号加2000。

【视图】

AUX/TTY用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：监听端口号，取值范围为2000～50000。

【使用指导】

设备只对从该监听端口收到的数据进行重定向。

【举例】

\# 设置Telnet重定向的监听端口号为3000。

\<Sysname\> system-view

Sysname line tty 1

Sysname-line-tty1 redirect listen-port 3000

【相关命令】

·**redirect enable**

·**display tcp**（请参考三层技术-IP业务）

**登录设备 \-- 登录设备命令 \-- redirect passthrough**

------------------------------------------------------------------------

**[redirect** **passthrough**]命令用来设置在Telnet重定向时对数据不进行任何处理直接转发。

**[undo redirect** **passthrough**]命令用来恢复缺省情况。

【命令】

**[redirect** **passthrough**]

**[undo** **redirect** **passthrough**]

【缺省情况】

在建立Telnet重定向连接后，将对数据按照Telnet协议规定处理。

【视图】

AUX/TTY用户线视图

【缺省用户角色】

network-admin

【使用指导】

配置该命令后，对经过Telnet重定向设备的数据不进行任何处理直接转发。某些情况下，Telnet重定向服务器连接的用户和目的设备之间的报文传输是不遵循Telnet标准协议的，因此只需要用户与目的设备能够解析双方交互的数据报文即可完成登录过程。在此情况下，Telnet重定向服务器需要配置**redirect passthrough**命令保证对这些交互报文仅仅是转发而不进行任何处理，否则将导致用户和目的设备之间的数据解析错误。

【举例】

\# 设置在建立Telnet重定向时对数据不进行任何处理直接转发。

\<Sysname\> system-view

Sysname line tty 1

Sysname-line-tty1 redirect passthrough

【相关命令】

·**redirect** **enable**

**登录设备 \-- 登录设备命令 \-- redirect refuse-negotiation**

------------------------------------------------------------------------

**[redirect refuse-negotiation**]命令用来强制设置在建立Telnet重定向连接时不进行Telnet选项协商。

**[undo redirect refuse-negotiation**]命令用来设置在建立Telnet重定向连接时进行Telnet选项协商。

【命令】

**[redirect refuse-negotiation**]

**[undo redirect refuse-negotiation**]

【缺省情况】

在建立Telnet重定向连接时，将进行Telnet选项协商。

【视图】

AUX/TTY用户线视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 设置在建立Telnet重定向连接时不进行Telnet选项协商。

\<Sysname\> system-view

Sysname line tty 1

Sysname-line-tty1 redirect refuse-negotiation

【相关命令】

·**redirect enable**

**登录设备 \-- 登录设备命令 \-- redirect timeout**

------------------------------------------------------------------------

**[redirect timeout**]命令用来设置Telnet重定向的空闲超时时间。

**[undo** **redirect timeout**]命令用来恢复缺省情况。

【命令】

**[redirect timeout ***time*]

**[undo redirect timeout**]

【缺省情况】

设备Telnet重定向的空闲超时时间为360秒。

【视图】

AUX/TTY用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：超时时间，取值范围为0～86400，单位为秒。0表示永不超时。

【使用指导】

如果在指定的时间内没有从Telnet客户端接收到数据，则断开Telnet重定向连接。

【举例】

\# 设置Telnet重定向的空闲超时时间为200秒。

\<Sysname\> system-view

Sysname line tty 1

Sysname-line-tty1 redirect timeout 200

【相关命令】

·**redirect enable**

**登录设备 \-- 登录设备命令 \-- screen-length**

------------------------------------------------------------------------

**[screen-length**]命令用来设置分屏显示时，每屏所显示的行数。

**[undo screen-length**]命令用来恢复缺省情况。

【命令】

**[screen-length** *screen-length*]

**[undo screen-length**]

【缺省情况】

每屏显示24行数据。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[screen-length*]：指定每屏所显示的行数，取值范围为0～512。0表示一次性显示全部信息，即不进行分屏显示。

【使用指导】

设备支持分屏显示信息，在暂停显示时按空格键，能继续显示下一屏信息。该命令设置的是每一屏所显示的行数，但显示终端实际显示的行数由终端的规格决定。比如，设置*screen-length*的值为40，但显示终端的规格为24行，当暂停显示按空格键时，设备发送给显示终端的信息为40行，但当前屏幕显示的是第18～第40行的信息，前面的17行信息，需要通过\<Page Up\>/\<Page Down\>键来翻看。

缺省情况下，分屏显示功能处于开启状态。配置**screen-length 0**或**screen-length disable**可关闭分屏显示功能。

如果用户线视图下配置**screen-length**为缺省值，并且此时用户线类视图下配置了**screen-length**，那么用户线视图下的生效配置值为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。

需要注意的是，用户线视图下使用本命令配置的分屏显示信息行数立即生效；在用户线类视图下配置的分屏显示信息行数将在下次登录时生效。

【举例】

\# 设置Console用户线分屏显示时，每屏显示30行数据。

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 screen-length 30

【相关命令】

·**screen-length disable**（基础配置指导/CLI）

**登录设备 \-- 登录设备命令 \-- send**

------------------------------------------------------------------------

**[send**]命令用来向指定的用户线发送消息。

【命令】

**[send**[ { **all** \| *number1* \| { **aux** \| **console** \| **tty** \| **vty** } *number2* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有的用户线。

*[number1*]：用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始。

**[aux**]：AUX用户线。

**[console**]：Console用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线。

*[number2*]：用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

输入本命令后回车，系统会提示您可以输入消息内容了。在输入消息内容时，按\<Enter\>键结束输入，按\<Ctrl+C\>组合键取消此次操作。

【举例】

\# 使用VTY 0用户线上线的用户想重启设备，于是发信息"Note please, I will reboot the system in 3 minutes."来提醒VTY 1。

\<Sysname\> send vty 1

Input message, end with Enter; abort with CTRL+C:

Note please, I will reboot the system in 3 minutes.

Send message? [Y/N:y]

使用VTY 1用户线登录的用户将收到如下消息：

Sysname

\*\*\*

\*\*\*

\*\*\*Message from vty0 to vty1

\*\*\*

Note please, I will reboot the system in 3 minutes.

**登录设备 \-- 登录设备命令 \-- set authentication password**

------------------------------------------------------------------------

**[set authentication password**]命令用来设置认证密码。

**[undo set authentication password**]命令用来取消认证密码。

【命令】

**[set authentication password**[ { **hash** \| **simple** } *password*]]

**[undo set authentication password**]

【缺省情况】

没有设置认证密码。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hash**]：表示以哈希方式设置认证密码。

**[simple**]：表示以明文方式设置认证密码。

*[password*]：设置的明文密码或哈希密码，区分大小写。明文密码的长度范围是1～16；哈希密码的长度范围是1～110。

【使用指导】

FIPS模式下，不支持本命令。

以明文或哈希方式设置的密码，均以哈希计算后的密文形式保存在配置文件中。

如果用户线视图下配置**set authentication password**为缺省值，并且此时用户线类视图下配置了**set authentication password**，那么用户线视图下的生效的认证密码为用户线类视图下的配置；如果用户线类视图下未配置，则生效的为缺省值。

需要注意的是，在用户线视图/用户线类视图下，使用该命令设置的认证密码将在下次登录设备时生效。

【举例】

\# 设置用户线Console 0的认证密码为hello。

\<Sysname\> system-view

Sysname line console 0

Sysname-line-console0 authentication-mode password

Sysname-line-console0 set authentication password simple hello

设置完后如果退出系统，则只有在密码提示信息后输入hello字符串才能再进入系统。

【相关配置】

·**authentication-mode**

**登录设备 \-- 登录设备命令 \-- shell**

------------------------------------------------------------------------

**[shell**]命令用来在当前用户线上启动终端服务。

**[undo shell**]命令用来在当前用户线上禁止终端服务。

【命令】

**[shell**]

**[undo shell**]

【缺省情况】

系统在所有的用户线上启动终端服务。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

**[undo shell**]命令有以下几点限制：

·Console用户线视图/Console用户线类视图不支持该命令。

·如果设备上只有一个AUX口，没有Console口（Console口和AUX口共用），则AUX用户线视图/AUX用户线类视图也不支持该命令。

·用户不能在自己登录的用户线上使用该命令。

·当设备作为Telnet/SSH服务器的时候，不能配置**undo shell**命令。

·如果在用户线类视图下使用**undo shell**命令禁止了终端服务，那么用户线视图下无法使用**shell**启动终端服务。

·当设备作为重定向服务器时，如果使用本命令在用户线上禁止了终端服务，则该用户线只能用于重定向服务功能，其它设备无法通过该用户线登录到本设备；如果未禁止终端服务，则该用户线既能用于重定向服务，也能用于终端服务使其它设备通过该用户线登录到本设备，但需要注意的是两者不能同时占用该用户线。

【举例】

\# 在VTY0到VTY4上终止终端服务（用户将不能通过VTY0-4登录设备）。

\<Sysname\> system-view

Sysname line vty 0 4

Sysname-line-vty0-4 undo shell

Disable line-vty0-4 , are you sure? Y/N:y

Sysname-line-vty0-4

**登录设备 \-- 登录设备命令 \-- speed**

------------------------------------------------------------------------

**[speed**]命令用来设置用户线的传输速率。

**[undo speed**]命令用来恢复缺省情况。

【命令】

**[speed ***speed-value*]

**[undo speed**]

【缺省情况】

用户线的传输速率为9600bps。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[speed-value*]：传输速率，单位为bps。异步串口的传输速率有：300bps、600bps、1200bps、2400bps、4800bps、9600bps、19200bps、38400bps、57600bps和115200bps。设备对以上速率的支持由产品和配置时的网络环境决定。

【使用指导】

访问终端和设备相应用户线下传输速率的设置必须一致，双方才能正常通信。

VTY用户线视图不支持该命令。

【举例】

\# 将用户线AUX 0的传输速率设置为19200bps。

\<Sysname\> system-view

Sysname line aux 0

Sysname-line-aux0 speed 19200

**登录设备 \-- 登录设备命令 \-- stopbit-error intolerance**

------------------------------------------------------------------------

![说明](登录设备命令.files/image002.png)

本命令的支持情况与设备型号相关，请以设备的实际情况为准。

****

**[stopbit-error** **intolerance**]命令用来检测停止位。

**[undo** **stopbit-error** **intolerance**]命令用来恢复缺省情况。

【命令】

**[stopbit-error intolerance**]

**[undo stopbit-error intolerance**]

【缺省情况】

不检测停止位。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

VTY用户线视图不支持该命令。

【举例】

\# 设置对用户线AUX 0检测停止位。

\<Sysname\> system-view

Sysname line aux 0

Sysname-line-aux0 stopbit-error intolerance

**登录设备 \-- 登录设备命令 \-- stopbits**

------------------------------------------------------------------------

**[stopbits**]命令用来设置停止位的个数。

**[undo stopbits**]命令用来恢复缺省情况。

【命令】

**[stopbits **[{ **1** \| **1.5** \| **2** }]]

**[undo stopbits**]

【缺省情况】

停止位为1比特。

【视图】

用户线视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[1**]：停止位为1比特。

**[1.5**]：停止位为1.5比特。目前，设备不支持该参数，配置后实际生效的是命令行**stopbits 2**。

**[2**]：停止位为2比特。

【使用指导】

访问终端和设备相应用户线下停止位的设置必须一致，双方才能正常通信。

VTY用户线视图不支持该命令。

【举例】

\# 设置AUX用户线的停止位为1比特。

\<Sysname\> system-view

Sysname line aux 0

Sysname-line-aux0 stopbits 1

**登录设备 \-- 登录设备命令 \-- telnet**

------------------------------------------------------------------------

**[telnet**]命令用于Telnet登录到远端设备，以便进行远程管理。

【命令】

**[telnet** *remote-host* [ *service-port*   **vpn-instance** *vpn-instance-name*  [ **source** { **interface**  *interface-type interface-number* \| **ip** *ip-address* } ]  **dscp** *dscp-value* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-host*]：远端设备的IPv4地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

*[service-port*]：远端设备提供Telnet服务的TCP端口号，取值范围为0～65535，缺省值为23。

**[vpn-instance** *vpn-instance-name*]：指定远端设备所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示远端设备位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source**]：指定Telnet报文的源接口或源IPv4地址。如果未指定本参数，则使用路由出接口的主IP地址作为设备发送的Telnet报文的源IPv4地址。

**[interface** *interface-type interface-number*]：指定源接口，发送的Telnet报文的源IPv4地址为该接口的地址。*interface-type interface-number*为接口类型和接口编号。

**[ip** *ip-address*]：指定Telnet报文的源IPv4地址。

*[dscp-value*]：Telnet客户端向服务器端发送Telnet报文的DSCP优先级，取值范围为0～63，缺省值为48。DSCP携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

【使用指导】

FIPS模式下，不支持本命令。

用户可以使用\<Ctrl+K\>组合键或**quit**命令来中断本次Telnet登录。

需要注意的是，本命令指定的源IPv4地址或源接口只对当前Telnet连接有效。

【举例】

\# Telnet登录到远程主机（IP地址为1.1.1.2），并指定发送Telnet报文的源IP地址为1.1.1.1。

\<Sysname\> telnet 1.1.1.2 source ip 1.1.1.1

【相关命令】

·**telnet client source**

**登录设备 \-- 登录设备命令 \-- telnet client source**

------------------------------------------------------------------------

**[telnet client source**]命令用来指定设备作为Telnet客户端时，发送Telnet报文的源IPv4地址或源接口。

**[undo telnet client source**]命令用来恢复缺省情况。

【命令】

**[telnet client source **[{ **interface** *interface-type interface-number* \| **ip** *ip-address* }]]

**[undo telnet client source**]

【缺省情况】

没有指定发送Telnet报文的源IPv4地址和源接口，使用报文路由出接口的主IPv4地址作为Telnet报文的源地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：指定源接口，发送的Telnet报文的源IPv4地址为该接口的地址。*interface-type interface-number*为接口类型和接口编号。

**[ip** *ip-address*]：指定发送Telnet报文的源IPv4地址。

【使用指导】

·FIPS模式下，不支持本命令。

·本命令指定的源IPv4地址或源接口对所有Telnet连接有效。

·若同时使用本命令和**telnet**命令指定源IPv4地址或源接口，则以**telnet**命令指定的源IP地址或源接口为准。

【举例】

\# 设备作为Telnet客户端时，指定发送的Telnet报文的源IP地址为1.1.1.1。

\<Sysname\> system-view

Sysname telnet client source ip 1.1.1.1

【相关命令】

·**display telnet client configuration**

**登录设备 \-- 登录设备命令 \-- telnet ipv6**

------------------------------------------------------------------------

**[telnet ipv6**]命令用于IPv6组网环境下，Telnet登录到远程主机，以便进行远程管理。

【命令】

**[telnet** **ipv6** *remote-host* [ **-i** *interface-type* *interface-number*   *port-number*   **vpn-instance** *vpn-instance-name*  [ **source** { **interface** *interface-type* *interface-number* \| **ipv6** *ipv6-address* } ]  **dscp** *dscp-value* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-host*]：远端设备的IPv6地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

**[-i** *interface-type interface-number*]：指定Telnet报文的出接口。*interface-type interface-number*为接口类型和接口编号。当Telnet指定的服务端IPv6地址是全球单播地址时，则不能指定该参数；当指定的服务端IPv6地址为链路本地地址时，必须指定该参数。

*[port-number*]：远端设备提供Telnet服务的TCP端口号，取值范围为0～65535，缺省值为23。

**[vpn-instance** *vpn-instance-name*]：指定远端设备所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示远端设备位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source**]：指定Telnet报文的源接口或源IPv6地址。如果未指定本参数，则使用路由出接口的主IPv6地址作为Telnet报文的源IPv6地址。

**[interface**{.apple-converted-space}*interface-type interface-number*]：指定源接口，发送的Telnet报文的源IPv6地址为该接口的主地址。*interface-type interface-number*为接口类型和接口编号。

**[ipv6** *ipv6-address*]：指定Telnet报文的源IPv6地址。

*[dscp-value*]：IPv6 Telnet客户端向服务器端发送Telnet报文的DSCP优先级，取值范围为0～63，缺省值为48。DSCP携带在IPv6报文中的Traffic class字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

【使用指导】

FIPS模式下，不支持本命令。

用户可以使用\<Ctrl+K\>组合键或**quit**命令来中断本次Telnet登录。

【举例】

\# Telnet登录到远程主机，IPv6地址为5000::1。

\<Sysname\> telnet ipv6 5000::1

\# Telnet登录到远程主机，IPv6地址为2000::1，并指定Telnet报文的源IPv6地址为1000::1。

\<Sysname\> telnet ipv6 2000::1 source ipv6 1000::1

**登录设备 \-- 登录设备命令 \-- telnet server acl**

------------------------------------------------------------------------

**[telnet server acl**]命令用来使用ACL（Access Controle List，访问控制列表）限制哪些Telnet客户端可以访问设备。

**[undo telnet server acl**]命令用来恢复缺省情况。

【命令】

**[telnet server acl ***acl-number*]

**[undo telnet server acl**]

【缺省情况】

没有使用ACL限制Telnet客户端。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示IPv4基本ACL。

·3000～3999：表示IPv4高级ACL。

·4000～4999：表示二层ACL。

【使用指导】

·当未引用ACL、或者引用的ACL不存在、或者引用的ACL为空时，允许所有登录用户访问设备；

·当引用的ACL非空时，则只有ACL中permit的用户才能访问设备，其它用户不允许访问设备，以免非法用户使用Telnet访问设备。

关于ACL的详细描述和介绍请参见"ACL和QoS配置指导"中的"ACL"。

该配置只过滤新建立的Telnet连接，不会对已建立的Telnet连接和操作造成影响。

如果多次使用该命令配置Telnet服务与ACL关联，最新配置生效。

FIPS模式下，不支持本命令。

【举例】

\# 仅允许地址为1.1.1.1的用户通过Telnet访问本设备。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit source 1.1.1.1 0

Sysname-acl-ipv4-basic-2001 quit

Sysname telnet server acl 2001

**登录设备 \-- 登录设备命令 \-- telnet server dscp**

------------------------------------------------------------------------

**[telnet server dscp**]命令用来配置Telnet服务器发送Telnet报文的DSCP优先级。

**[undo telnet server dscp**]命令用来恢复缺省情况。

【命令】

**[telnet server dscp ***dscp-value*]

**[undo telnet server dscp**]

【缺省情况】

Telnet服务器发送Telnet报文的DSCP优先级为48。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：Telnet报文的DSCP优先级，取值范围为0～63。DSCP携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

【使用指导】

FIPS模式下不支持该命令。

【举例】

\# 配置Telnet服务器发送报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname telnet server dscp 30

**登录设备 \-- 登录设备命令 \-- telnet server enable**

------------------------------------------------------------------------

**[telnet server enable**]命令用来使能Telnet服务。

**[undo telnet server enable**]命令用来关闭Telnet服务。

【命令】

**[telnet server enable**]

**[undo telnet server enable**]

【缺省情况】

Telnet服务处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

FIPS模式下，不支持本命令。

只有使能Telnet服务后，才允许网络管理员通过Telnet协议登录设备。

【举例】

\# 使能Telnet服务。

\<Sysname\> system-view

Sysname telnet server enable

**登录设备 \-- 登录设备命令 \-- telnet server ipv6 acl**

------------------------------------------------------------------------

**[telnet server ipv6 acl**]命令用来使用ACL限制哪些IPv6 Telnet客户端可以访问设备。

**[undo telnet server ipv6 acl**]命令用来恢复缺省情况。

【命令】

**[telnet server ipv6 acl ** **ipv6** ] *acl-number*

**[undo telnet server ipv6 acl**]

【缺省情况】

没有使用ACL限制Telnet客户端。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：需指定**ipv6**关键字，表示IPv6基本ACL。

·3000～3999：需指定**ipv6**关键字，表示IPv6高级ACL。

·4000～4999：表示二层ACL。

【使用指导】

·当未引用ACL、或者引用的ACL不存在、或者引用的ACL为空时，允许所有登录用户访问设备；

·当引用的ACL非空时，则只有ACL中permit的用户才能访问设备，其它用户不允许访问设备，以免非法用户使用Telnet访问设备。

关于ACL的详细描述和介绍请参见"ACL和QoS配置指导"中的"ACL"。

该配置只过滤新建立的Telnet连接，不会对已建立的Telnet连接和操作造成影响。

如果多次使用该命令配置Telnet服务与ACL关联，最新配置生效。

FIPS模式下，不支持本命令。

【举例】

\# 仅允许地址为2000::1的用户通过Telnet访问本设备。

\<Sysname\> system-view

Sysname acl ipv6 basic 2001

Sysname-acl6-ipv6-basic-2001 rule permit source 2000::1 128

Sysname-acl6-ipv6-basic-2001 quit

Sysname telnet server ipv6 acl ipv6 2001

**登录设备 \-- 登录设备命令 \-- telnet server ipv6 dscp**

------------------------------------------------------------------------

**[telnet server ipv6 dscp**]命令用来配置IPv6 Telnet服务器发送报文的DSCP优先级。

**[undo** **telnet server ipv6 dscp**]命令用来恢复缺省情况。

【命令】

**[telnet server ipv6 dscp ***dscp-value*]

**[undo telnet server ipv6 dscp**]

【缺省情况】

IPv6 Telnet服务器发送IPv6 Telnet报文的DSCP优先级为48。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：IPv6 Telnet报文的DSCP优先级，取值范围为0～63。DSCP携带在IPv6报文中的Traffic class字段，用来体现报文自身的优先等级，决定报文传输的优先程度。

【使用指导】

FIPS模式下不支持该命令。

【举例】

\# 配置IPv6 Telnet服务器发送的报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname telnet server ipv6 dscp 30

**登录设备 \-- 登录设备命令 \-- terminal type**

------------------------------------------------------------------------

**[terminal type**]命令用来设置当前用户线下的终端显示类型。

**[undo terminal type**]命令用来恢复缺省情况。

【命令】

**[terminal type**[ { **ansi** \| **vt100** }]]

**[undo terminal type**]

【缺省情况】

终端显示类型为ANSI。

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ansi**]：终端显示类型为ANSI类型。

**[vt100**]：终端显示类型为VT100类型。

【使用指导】

设备支持ANSI和VT100两种终端显示类型。当设备的终端类型与客户端（如超级终端或者Telnet客户端等）的终端类型不一致，或者均设置为ANSI时，并且当前编辑行的总字符数超过80个字符时，客户端会出现光标错位、终端屏幕不能正常显示的现象。建议两端都设置为VT100类型。

需要注意的是，用户线视图/用户线类视图下配置的终端显示类型都在下次登录时生效。

【举例】

\# 设置终端显示类型为VT100类型。

\<Sysname\> system-view

Sysname line vty 0

Sysname-line-vty0 terminal type vt100

**登录设备 \-- 登录设备命令 \-- user-interface**

------------------------------------------------------------------------

**[user-interface**]命令用来进入一个或多个用户线视图。

【命令】

**[user-interface** { *first-number1* [ *last-number1*  \| { **aux** \| **console** \| **tty** \| **vty** } *first-number2*  *last-number2*  }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[first-number1*]：第一个用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始。

*[last-number1*]：最后一个用户线的编号（绝对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，一般从0开始，但不能小于*first-number1*。

**[aux**]：AUX用户线。

**[console**]：Console用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线。

*[first-number2*]：第一个用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[last-number2*]：最后一个用户线的编号（相对编号方式），不同型号的设备支持的取值范围不同，请以设备的实际情况为准，但不能小于*first-number2*。

【使用指导】

·进入一个用户线视图进行配置后，该配置只对该用户视图有效。

·进入多个用户线视图进行配置后，该配置对这些用户视图均有效。

·该命令实现与**line**一致，仅为与旧版本兼容保留，请使用**line**。

【举例】

\# 进入Console 0用户线视图。

\<Sysname\> system-view

Sysname user-interface console 0

Sysname-line-console0

\# 进入VTY 0～4用户线视图。

\<Sysname\> system-view

Sysname user-interface vty 0 4

Sysname-line-vty0-4

【相关命令】

·**user-interface class**

**登录设备 \-- 登录设备命令 \-- user-interface class**

------------------------------------------------------------------------

**[user-interface class**]命令用来进入指定用户线类视图。

【命令】

**[user-interface class **[{ **aux** \| **console** \| **tty** \| **vty** }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aux**]：AUX用户线类。

**[console**]：Console用户线类。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tty**]：TTY用户线类。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vty**]：VTY用户线类。

【使用指导】

**[user-interface class**]命令用来进入指定用户线类视图，**user-interface**命令用来进入一个或多个用户线视图。对于同时支持这两种视图的命令：

·用户线视图下的配置优先于用户线类视图下的配置。

·用户线视图下的配置只对该用户线生效。

·用户线类视图下的配置修改不会立即生效，当用户下次登录后所修改的配置值才会生效。

·用户线视图下的属性配置为缺省值时，将采用用户线类视图下配置的值。如果用户线类视图下的属性配置也为缺省值时，则直接采用该属性的缺省值。

·该命令实现与**line class**一致，仅为与旧版本兼容保留，请使用**line class**。

用户线类视图下支持的命令有：

·**activation-key**

·**auto-execute command**

·**authentication-mode**

·**command accounting**

·**command authorization**

·**escape-key**

·**history-command max-size**

·**idle-timeout**

·**protocol inbound**

·**screen-length**

·**set authentication password**

·**shell**

·**terminal type**

·**user-role**

【举例】

\# 将VTY用户线参数------用户连接的超时时间的缺省值设置为15分钟。

\<Sysname\> system-view

Sysname user-interface class vty

Sysname-line-class-vty idle-timeout 15

\#在console用户线类视图下，将启动Console口终端会话的快捷键设置为\<s\>。

\<Sysname\> system-view

Sysname user-interface class console

Sysname-line-class-console activation-key s

Sysname-line-class-console quit

·在console用户线视图下，将启动Console口终端会话的快捷键设置为缺省值（可以使用undo activation-key或者直接使用activation-key 13进行配置）。

Sysname line console 0

Sysname-line-console0 undo activation-key

·此时生效的快捷键为用户线类视图下的配置，验证过程如下：

·退出Console口终端会话。

Sysname-line-console0 return

\<Sysname\> quit

·重新使用Console口登录设备，能看到如下显示信息。

Press ENTER to get started.

·此时，\<Enter\>键失效，需要按\<s\>键才能出现用户视图提示符，启动Console口终端会话。

\<Sysname\>

【相关命令】

·**user-interface**

**登录设备 \-- 登录设备命令 \-- user-role**

------------------------------------------------------------------------

**[user-role**]命令用来配置从当前用户线登录系统的用户角色。

**[undo user-role**]命令用来删除指定的用户角色配置或者恢复缺省情况。

【命令】

**[user-role** *role-name*]

**[undo** **user-role** [ *role-name* ]]

【缺省情况】

通过Console口登录系统的用户角色为network-admin，通过其它接口登录系统的用户角色为network-operator。（不支持MDC的设备）

对于缺省MDC，通过Console口登录系统的用户角色为network-admin，通过其它接口登录系统的用户角色为network-operator。对于非缺省MDC，通过**switchto mdc**命令登录用户的缺省角色为mdc-admin，其它登录用户的缺省角色均为mdc-operator（支持MDC的设备）

【视图】

用户线视图/用户线类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[role-name*]：用户角色名称，为1～63个字符的字符串，区分大小写。可以是系统预定义的角色名称，包括network-admin、network-operator、mdc-admin、mdc-operator、level-0～level-15，也可以是自定义的用户角色名称。不指定该参数时，表示恢复到缺省情况。由于系统预定义角色security-audit只能在local-user视图下进行配置，所以该参数不能指定为security-audit角色，否则会弹出错误提示信息。

【使用指导】

FIPS模式下，不支持本命令。

可通过多次执行本命令，配置多个用户角色，最多可配置64个。用户登录后具有的权限是这些角色权限的集合。

在用户线视图/用户线类视图下使用该命令设置的用户角色将在下次登录设备时生效。

关于用户角色的详细介绍请参见"基础配置指导"中的"RBAC"。

【举例】

\# 设置从AUX用户线登录系统的用户角色为network-admin。

\<Sysname\> system-view

Sysname line aux 0

Sysname-line-aux0 user-role network-admin

**登录设备 \-- 登录设备命令 \-- web captcha**

------------------------------------------------------------------------

![说明](登录设备命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[web captcha**]命令用来配置用户访问Web的固定校验码。

**[undo web captcha**]命令用来恢复缺省情况。

【命令】

**[web captcha** *verification-code*]

**[undo web captcha**]

【缺省情况】

用户只能使用Web页面显示的校验码访问Web。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[verification-code*]：访问Web的固定校验码，为4个字符的字符串，区分大小写。

【描述】

配置该命令后，不管Web登录页面显示的校验码是什么，用户只要输入该固定的校验码，即可访问设备。本命令主要用于测试环境，当需要对设备的Web功能进行测试时，可以配置一个固定的校验码，使用脚本即可登录设备，以免每次测试都要手工输入变化的校验码，影响测试效率。

设备在网络中正常使用的时候，建议不要配置该命令，以免降低Web访问的安全性。

多次配置该命令，最新配置生效。

该命令不能保存到配置文件，设备重启后失效。

【举例】

\# 设置访问Web的固定校验码为test。

\<Sysname\> web captcha test

**登录设备 \-- 登录设备命令 \-- web https-authorization mode**

------------------------------------------------------------------------

**[web https-authorization mode**]命令用来设置使用HTTPS登录设备的认证模式。

**[undo web https-authorization mode**]命令用来恢复缺省情况。

【命令】

**[web**[ **https-authorization mode** { **auto** \| **manual** }]]

**[undo** **web** **https-authorization** **mode**]

【缺省情况】

使用HTTPS登录设备的认证模式为manual。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]**：**表示用户通过HTTPS登录设备时，使用客户端的PKI证书自动认证登录。

**[manual**]**：**表示用户通过HTTPS登录设备时，设备给出登录页面，用户必须输入合法的用户名和密码后才能登录。

【使用指导】

当选用**auto**认证模式时，设备客户端的PKI证书自动认证登录：

·当用户侧的证书正确且未超期，则读取证书中的CN字段作为用户名，进行AAA认证。如果认证成功，则自动进入设备的Web界面；

·当用户侧的证书有效且未超期，但AAA认证失败，则回到登录界面（如果此时用户输入合法的用户名和密码仍然能够登录）；

·当用户侧的证书错误或超期，则断开HTTPS连接。

【举例】

\# 设置Web的HTTPS认证模式为auto。

\<Sysname\> system-view

Sysname web https-authorization mode auto

**登录设备 \-- 登录设备命令 \-- web idle-timeout**

------------------------------------------------------------------------

![说明](登录设备命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[web idle-timeout**]命令用来设置Web闲置超时时间。

**[undo web idle-timeout**]命令用来恢复缺省情况。

【命令】

**[web** **idle-timeout** *idle-time*]

**[undo** **web** **idle-timeout**]

【缺省情况】

Web闲置超时时间为10分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[idle-time*]：Web闲置超时时间，取值范围为1～999，单位为分钟。

【使用指导】

当某Web用户在指定时间（*idle-time*）内一直没有操作Web页面，包括点击鼠标或键盘操作（只是移动鼠标，不会延长用户的下线时间），则系统会强制断开该用户的Web链接，使该用户下线。从而尽量避免在用户离开登录终端期间，非法用户对设备进行配置。

需要注意的是，修改Web线的闲置超时时间，会影响正在访问的用户。

【举例】

\# 设置Web闲置超时时间为100分钟。

\<Sysname\> system-view

Sysname web idle-timeout 100

**登录设备 \-- 登录设备命令 \-- webui log**

------------------------------------------------------------------------

**[webui log enable**]命令用来开启Web操作日志输出功能。

**[undo webui log enable**]命令用来恢复缺省情况。

【命令】

**[webui log enable**]

**[undo webui log enable**]

【缺省情况】

Web操作日志输出功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启Web操作日志输出功能，比较关键的Web操作（比如修改系统时间）会产生对应的Web操作日志，输出到信息中心。通过设置信息中心的参数，最终决定Web操作日志的输出规则（即是否允许输出以及输出方向）

能够触发Web操作日志的Web操作动作和设备相关，请以实际设备情况为准。

Web操作日志，采用固定的模块名"WEB"；日志助记符有统一的前缀"WEBOPT\_"；同时Web操作日志还包含Web用户信息：Web客户端IP地址和Web用户名。

【举例】

\# 开启Web操作日志输出功能，Web用户执行修改系统时间的操作。

\<Sysname\> system-view

Sysname webui log enable

当Web用户执行修改系统时间的操作时，设备上将输出如下日志：

%Mar 25 14:32:38:802 2013 H3C WEB/6/WEBOPT_SET_TIME: -HostIP=192.168.100.235-User=Admin; Set the system date and time to 2013-05-27T10:00:00.
