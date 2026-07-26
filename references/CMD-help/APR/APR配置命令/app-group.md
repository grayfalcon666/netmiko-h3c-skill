
**APR \-- APR配置命令 \-- app-group**

------------------------------------------------------------------------

**[app-group**]命令用来创建应用组，并进入应用组视图。

**[undo app-group**]命令用来删除指定的应用组。

【命令】

**[app-group ***group-name*]

**[undo app-group ***group-name*]

【缺省情况】

系统中存在若干预定义应用组，可通过**display app-group pre-defined**命令查看。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：应用组的名字，为1～63个字符的字符串，不区分大小写，可以为数字、字母、连字符、下划线，不允许为"invalid"、"other"或系统预定义应用组的名称。

【使用指导】

系统中最多可以定义65536个应用组。

【举例】

\# 创建名字为aaa的应用组，并进入应用组视图。

\<Sysname\> system-view

Sysname app-group aaa

Sysname-app-group-aaa

【相关命令】

·**copy app-group**

·**description**

·**include application**

**APR \-- APR配置命令 \-- application statistics enable**

------------------------------------------------------------------------

**[application statistics enable**]命令用来开启接口的应用统计功能。

**[undo application statistics enable**]命令用来关闭接口的应用统计功能。

【命令】

**[application statistics enable**[ [ **inbound \| outbound** ]]]

**[undo application statistics enable**[ [ **inbound** \| **outbound** ]]]

【缺省情况】

接口的应用统计功能处于关闭状态。

【视图】

三层接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：在接口的入方向上开启应用统计功能。

**[outbound**]：在接口的出方向上开启应用统计功能。

【使用指导】

如果不指定任何参数，则表示同时开启接口出方向和入方向上的应用统计功能。

在接口上开启应用统计功能之后，设备能够对接口上收到或者发送的报文的数目、速率按照应用协议分别进行统计，生成的统计信息可以通过**display application statistics**命令查看。

需要注意的是，接口的应用统计功能会消耗大量系统内存。当系统出现内存告警时，请关闭接口的应用统计功能。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启入方向应用统计功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 application statistics enable inbound

\# 在接口GigabitEthernet1/0/2上开启出方向应用统计功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 application statistics enable outbound

\# 在接口GigabitEthernet1/0/3上开启所有方向应用统计功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 application statistics enable

·交换应用

\# 在接口Vlan-interface1入方向上开启入方向应用统计功能。

\<Sysname\> system-view

Sysname interface vlan-interface 1

Sysname-vlan-interface1 application statistics enable inbound

\# 在接口Vlan-interface2上开启出方向应用统计功能。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-vlan-interface2 application statistics enable outbound

\# 在接口Vlan-interface3上开启所有方向应用统计功能。

\<Sysname\> system-view

Sysname interface vlan-interface 3

Sysname-vlan-interface3 application statistics enable

【相关命令】

·**display application statistics**

**APR \-- APR配置命令 \-- copy app-group**

------------------------------------------------------------------------

**[copy app-group**]命令用来在应用组中拷贝另一个应用组中的所有应用。

【命令】

**[copy app-group*** group-name*]

【视图】

应用组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：要拷贝的应用组的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

可以通过多次执行本命令拷贝多个应用组里的应用。

【举例】

\# 在组abc中拷贝组bcd中的所有应用。

\<Sysname\> system-view

Sysname app-group abc

Sysname-app-group-abc copy app-group bcd

【相关命令】

·**app-group**

·**include application**

**APR \-- APR配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来为自定义的应用组设置描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description ***group-description*]

**[undo description **]

【缺省情况】

自定义应用组的描述信息为User-defined application group。

【视图】

应用组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-description*]：应用组的描述信息，为1～127个字符的字符串，可以包含空格，区分大小写。

【举例】

\# 配置名字为aaa的应用组描述信息为User defined aaa group。

\<Sysname\> system-view

Sysname app-group aaa

Sysname-app-group-aaa description User defined aaa group

【相关命令】

·**app-group**

**APR \-- APR配置命令 \-- display app-group**

------------------------------------------------------------------------

**[display app-group**]命令用来显示应用组信息。

【命令】

**[display app-group **[[ **name** *group-name* \| **pre-defined** \| **user-defined** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** group-name*]：显示指定名称的应用组信息。*group-name*表示应用组的名字，不区分大小写，为1～63个字符的字符串。

**[pre-defined**]：显示预定义的应用组信息。

**[user-defined**]：显示用户自定义的应用组信息。

【使用指导】

如果不指定任何参数，则表示显示所有的应用组信息。

【举例】

\# 显示用户自定义的所有应用组信息。

\<Sysname\> display app-group user-defined

 Group name                         Type           Group ID

 g1                                 User-defined   0x80000001

 g1234                              User-defined   0x80000003

 g2                                 User-defined   0x80000002

 g234                               User-defined   0x80000004

\# 显示系统预定义的所有应用组信息。

\<Sysname\> display app-group pre-defined

 Group name                         Type           Group ID

 authentication                     Pre-defined    0x00000010

 database                           Pre-defined    0x00000003

 email                              Pre-defined    0x00000002

 file-share                         Pre-defined    0x00000009

 games                              Pre-defined    0x00000004

 im                                 Pre-defined    0x0000000a

 internet                           Pre-defined    0x00000005

 multimedia                         Pre-defined    0x00000008

 network-management                 Pre-defined    0x0000000e

 network-service                    Pre-defined    0x0000000f

 news                               Pre-defined    0x0000000d

 p2p                                Pre-defined    0x00000006

 productivity-tools                 Pre-defined    0x00000012

 routing                            Pre-defined    0x00000011

 shopping-and-bank                  Pre-defined    0x0000000c

 stock                              Pre-defined    0x0000000b

 voip                               Pre-defined    0x00000007

\# 显示所有应用组的信息。

\<Sysname\> display app-group

 Group name                         Type           Group ID

 authentication                     Pre-defined    0x00000010

 database                           Pre-defined    0x00000003

 email                              Pre-defined    0x00000002

 file-share                         Pre-defined    0x00000009

 g1                                 User-defined   0x80000001

 g1234                              User-defined   0x80000003

 g2                                 User-defined   0x80000002

 g234                               User-defined   0x80000004

 games                              Pre-defined    0x00000004

 im                                 Pre-defined    0x0000000a

 internet                           Pre-defined    0x00000005

 multimedia                         Pre-defined    0x00000008

 network-management                 Pre-defined    0x0000000e

 network-service                    Pre-defined    0x0000000f

 news                               Pre-defined    0x0000000d

 p2p                                Pre-defined    0x00000006

 productivity-tools                 Pre-defined    0x00000012

 routing                            Pre-defined    0x00000011

 shopping-and-bank                  Pre-defined    0x0000000c

 stock                              Pre-defined    0x0000000b

 voip                               Pre-defined    0x00000007

\# 显示名为group_A的应用组的信息。

\<Sysname\> display app-group name group_A

 Group name:         group_A

 Group ID:           0x80000005

 Type:               User-defined

 Application count:  5

 Include application list:

 Application name                   Type           App ID

 3com-amp3                          Pre-defined    0x00000003

 app1                               User-defined   0x80000001

 bapp3                              User-defined   0x80000006

 pop3                               Pre-defined    0x00000e75

 smtp                               Pre-defined    0x00001135

表1-1 display app-group命令显示信息描述表

字段

描述

Group name

应用组的组名

Group ID

应用组的组号

Type

应用组或应用的类型，取值包括：

·Pre-defined：系统预定义

·User-defined：用户自定义

Application count

应用组中包含的应用个数

Include application list

包含的应用列表

Application name

应用名

App ID

应用协议编号

【相关命令】

·**app-group **

·**include**

**APR \-- APR配置命令 \-- display application**

------------------------------------------------------------------------

**[display application**]命令用来显示应用信息。

【命令】

**[display application**[ [ **name** *application-name* \| **pre-defined** \| **user-defined** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name**]* application-name*：显示指定名称的应用信息。*app-name*表示应用的名称，为1～63个字符的字符串，不区分大小写。

**[pre-defined**]：显示系统预定义的应用列表。

**[user-defined**]：显示用户自定义的应用列表。

【使用指导】

若不指定任何参数，则表示显示所有的应用信息。

【举例】

\# 显示系统预定义的应用列表。

\<Sysname\> display application pre-defined

 Pre-defined count:   15

 Application name                   Type          App ID       Tunnel   Encrypted

 ambit-lm                           Pre-defined   0x000000b9   No       No

 amdsched                           Pre-defined   0x000000ba   No       No

 amidxtape                          Pre-defined   0x000000bb   No       No

 amiganetfs                         Pre-defined   0x000000bc   No       No

 aminet                             Pre-defined   0x000000bd   No       No

 amp                                Pre-defined   0x000000be   No       No

 amt-soap-https                     Pre-defined   0x000000cc   No       Yes

 appserv-http                       Pre-defined   0x00000122   No       No

 appserv-https                      Pre-defined   0x00000123   No       Yes

 ktelnet                            Pre-defined   0x000009ae   No       No

 l2c-connect                        Pre-defined   0x000009b6   No       No

 l2c-info                           Pre-defined   0x000009b7   No       No

 l2tp                               Pre-defined   0x000009b8   Yes      No

 l3-exprt                           Pre-defined   0x000009b9   No       No

 l3-hawk                            Pre-defined   0x000009ba   No       No

\# 显示用户自定义的应用列表。

\<Sysname\> display application user-defined

 User-defined count:  2

 Application name                   Type          App ID       Tunnel   Encrypted

 amp_User                           User-defined  0x80000003   No       No

 amp_User2                          User-defined  0x80000004   No       No

\# 显示所有应用列表。

\<Sysname\> display application

 Total count:         17

 Pre-defined count:   15

 User-defined count:  2

 Application name                   Type          App ID       Tunnel   Encrypted

 ambit-lm                           Pre-defined   0x000000b9   No       No

 amdsched                           Pre-defined   0x000000ba   No       No

 amidxtape                          Pre-defined   0x000000bb   No       No

 amiganetfs                         Pre-defined   0x000000bc   No       No

 aminet                             Pre-defined   0x000000bd   No       No

 amp                                Pre-defined   0x000000be   No       No

 amp_User                           User-defined  0x80000003   No       No

 amp_User2                          User-defined  0x80000004   No       No

 amt-soap-https                     Pre-defined   0x000000cc   No       Yes

 appserv-http                       Pre-defined   0x00000122   No       No

 appserv-https                      Pre-defined   0x00000123   No       Yes

 ktelnet                            Pre-defined   0x000009ae   No       No

 l2c-connect                        Pre-defined   0x000009b6   No       No

 l2c-info                           Pre-defined   0x000009b7   No       No

 l2tp                               Pre-defined   0x000009b8   Yes      No

 l3-exprt                           Pre-defined   0x000009b9   No       No

 l3-hawk                            Pre-defined   0x000009ba   No       No

\# 显示名为telnet的应用信息。

\<Sysname\> display application name telnet

 Application name: telnet

 Application ID:   0x000012b7

 Tunnel:           No

 Encrypted:        No

表1-2 display application命令显示信息描述表

字段

描述

Total count

应用总数

Pre-defined count

预定义应用总数

User-defined count

自定义应用总数

Application Name

应用名

Type

应用的类型，取值包括：

·Pre-defined：系统预定义

·User-defined：用户自定义

App ID/Application ID

应用协议编号

Tunnel

应用是否为隧道类型，例如L2TP为一个隧道类型的应用

Encrypted

应用是否为加密类型，例如HTTPS为一个加密类型的应用

【相关命令】

·**app-group **

·**include**

**APR \-- APR配置命令 \-- display application statistics**

------------------------------------------------------------------------

**[display application statistics**]命令用来显示接口上的应用统计信息。

【命令】

集中式设备：

**[display application statistics **[[ **direction** { **inbound** \| **outbound** } \| **interface** *interface-type interface-number* \| **name** *application-name* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display application statistics **[[ **direction** { **inbound** \| **outbound** } \| **interface** *interface-type interface-number* [ **slot** *slot-number* [ **cpu** *cpu-number* ] ] \| **name** *application-name* ] \*]]

分布式设备－IRF模式：

**[display application statistics **[[ **direction** { **inbound** \| **outbound** } \| **interface** *interface-type interface-number* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ] \| **name** *application-name* ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[direction**]：显示指定方向的应用统计信息。

**[inbound**]：显示接口入方向的应用统计信息。

**[outbound**]：显示接口出方向的应用统计信息。

**[interface** *interface-type interface-number*]：显示指定接口的应用统计信息，*interface-type interface-number*表示要显示统计信息的接口类型和接口编号。

**[slot*** slot-number*]：显示指定单板上全局接口的应用统计信息。*slot-number*表示单板所在的槽位号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上全局接口的应用统计信息。*slot-number*表示设备在IRF中的成员编号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上全局接口的应用统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上全局接口的应用统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上全局接口的应用统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上全局接口的应用统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[name ***application-name*]：显示指定名称的应用统计信息。*app-name*表示应用的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

如果不指定任何参数，则表示显示所有接口的应用统计信息。

只有在接口应用统计功能开启的情况下，接口才能产生相应的应用统计信息。因此，使用本命令查看接口统计信息之前，请确保接口的应用统计功能处于开启状态。

可以按应用名称、接口出方向、接口入方向、接口名称分别显示相应的应用统计信息，也可以通过指定多个参数，显示同时符合多个参数的应用统计信息。

【举例】

\# 显示接口上的所有应用统计信息。

\<Sysname\> display application statistics

Interface : GigabitEthernet1/0/1

Application   In/Out Packets            Bytes              PPS        BPS

appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222

                OUT  170034             270011351          3211       451134

app2            IN   2195               18560000           300        654222

                OUT  21986666666        655555555123123101 55551      5454125111

aPP3            IN   2195               17560000           300        45161

                OUT  21986666666        5555555551231231   55551       5454125111

Interface : GigabitEthernet1/0/2

Application   In/Out Packets          Bytes               PPS         BPS

app4            IN   1900231111111    252334402111        2342222222  3411222222

                OUT  170034           270011351           3211        451134

app2            IN   2195             18560000            300         654222

                OUT  21986666666      65555555512         55551       45412

App123456981200 IN   2195             17560000            300         45161

123456789012300 OUT  21986666666      5555555551231231    55551       54541251

11111111111100

01234567890100

0123456

\# 显示接口Vlan-interface1上所有应用的统计信息。

\<Sysname\> display application statistics interface vlan-interface 1

Interface : Vlan-interface1

Application   In/Out Packets            Bytes              PPS        BPS

appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222

                OUT  170034             270011351          3211       451134

app2            IN   2195               18560000           300        654222

                OUT  21986666666        655555555123123101 55551      5454125111

APP3            IN   2195               17560000           300        45161

                OUT  21986666666        5555555551231231   55551      5454125111

\# 显示接口GigabitEthernet1/0/1上所有的入方向应用统计信息。

\<Sysname\> display application statistics interface gigabitethernet 1/0/1 direction inbound

Interface : GigabitEthernet1/0/1

Application   In/Out Packets            Bytes              PPS        BPS

appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222

app2            IN   2195               18560000           300        654222

APP3            IN   2195               17560000           300        45161

\# 显示接口GigabitEthernet1/0/1上所有的出方向应用统计信息。

\<Sysname\> display application statistics interface gigabitethernet 1/0/1 direction outbound

Interface : GigabitEthernet1/0/1

Application   In/Out Packets            Bytes              PPS        BPS

appaaaaasg      OUT  190023111111111111 252334402111111111 2342222222 3411222222

app2            OUT  2195               18560000           300        654222

APP3            OUT  2195               17560000           300        45161

\# 显示应用名为app1的统计信息。

\<Sysname\> display application statistics name app1

Interface : GigabitEthernet1/0/1

Application   In/Out Packets            Bytes              PPS        BPS

app1            IN   190023111111111111 252334402111111111 2342222222 3411222222

                OUT  170034             270011351          3211       451134

Interface : GigabitEthernet1/0/2

Application   In/Out Packets            Bytes              PPS        BPS

app1            IN   190023111111111111 252334402111111111 2342222222 3411222222

                OUT  170034             270011351          3211       451134

Interface : GigabitEthernet1/0/3

Application   In/Out Packets            Bytes              PPS        BPS

app1            IN   190023111111111111 252334402111111111 2342222222 3411222222

表1-3 display application statistics命令显示信息描述表

字段

描述

Interface

接口的名称

Application

应用的名称

In/Out

入方向/出方向

Packets

接口上接收或发送的报文个数

Bytes

接口上接收或发送的字节数

PPS

每秒报文数

BPS

每秒比特数

【相关命令】

·**app-group**

·**application statistics enable**

**APR \-- APR配置命令 \-- display application statistics top**

------------------------------------------------------------------------

**[display application statistics top**]命令用来按指定类型的统计排名显示接口应用统计信息。

【命令】

集中式设备：

**[display application statistics top ***number*[ { **bps** \| **bytes** \| **packets** \| **pps** } **interface** *interface-type interface-number*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display application statistics top ***number*[ { **bps** \| **bytes** \| **packets** \| **pps** } **interface** *interface-type interface-number* [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[display application statistics top ***number*[ { **bps** \| **bytes** \| **packets** \| **pps** } **interface** *interface-type interface-number* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[number*]：显示排名前*number*的应用统计信息。

**[bytes**]：显示接口字节数为前*number*的应用统计信息。

**[bps**]：显示接口比特速率统计为前*number*的应用统计信息。

**[packets**]：显示接口包数为前*number*的应用统计信息。

**[pps**]：显示接口包速率统计为前*number*的应用统计信息。

**[interface** *interface-type interface-number*]：显示指定接口的应用统计信息，*interface-type interface-number*指定要显示统计信息的接口类型和接口编号。

**[slot*** slot-number*]：显示指定单板上全局接口的应用统计信息。*slot-number*表示单板所在的槽位号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上全局接口的应用统计信息。*slot-number*表示设备在IRF中的成员编号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上全局接口的应用统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上全局接口应用的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上全局接口应用的统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。该参数仅在指定显示全局接口（例如VLAN接口、Tunnel接口）时可见。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上全局接口的应用统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

只有在接口应用统计功能开启的情况下，接口才能产生相应的应用统计信息。因此，使用本命令查看接口统计信息之前，请确保接口的应用统计功能处于开启状态。

系统以接口上某一个应用的出方向和入方向的统计值之和为依据对应用进行排名。统计值相同的应用，再按照应用名称的字母顺序排列。

【举例】

\# 显示接口GigabitEthernet1/0/1上包数为前3的应用统计信息。

\<Sysname\> display application statistics top 3 packets interface gigabitethernet 1/0/1

Interface : GigabitEthernet1/0/1

Application   In/Out Packets            Bytes              PPS        BPS

appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222

                OUT  170034             270011351          3211       451134

app2            IN   2196               18560000           300        654222

                OUT  21986666666        655555555123123101 55551      5454125111

aPP3            IN   2195               17560000           300        45161

                OUT  21986666666        5555555551231231   55551      5454125111

\# 显示接口GigabitEthernet1/0/1字节数为前3的应用统计信息。

\<Sysname\> display application statistics top 3 bytes interface gigabitethernet 1/0/1

Interface : GigabitEthernet1/0/1

Application   In/Out Packets            Bytes              PPS        BPS

appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222

                OUT  170034             270011351          3211       451134

app2            IN   2196               18560000           300        654222

                OUT  21986666666        155555555123123101 55551      5454125111

aPP3            IN   2195               17560000           300        45161

                OUT  21986666666        5555555551231231   55551      5454125111

\# 显示接口GigabitEthernet1/0/1包速率为前3的应用统计信息。

\<Sysname\> display application statistics top 3 pps interface gigabitethernet 1/0/1

Interface : GigabitEthernet1/0/1

Application   In/Out Packets            Bytes              PPS        BPS

appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 3411222222

                OUT  170034             270011351          3211       451134

app2            IN   2196               18560000           305        654222

                OUT  21986666666        655555555123123101 55551      5454125111

aPP3            IN   2195               17560000           300        45161

                OUT  21986666666        5555555551231231   55551      5454125111

\# 显示接口GigabitEthernet1/0/1比特速率为前3的应用统计信息。

\<Sysname\> display application statistics top 3 bps interface gigabitethernet 1/0/1

Interface : GigabitEthernet1/0/1

Application   In/Out Packets            Bytes              PPS        BPS

appaaaaasg      IN   190023111111111111 252334402111111111 2342222222 9411222222

                OUT  170034             270011351          3211       451134

app2            IN   2196               18560000           300        654222

                OUT  21986666666        155555555123123101 55551      5454125111

aPP3            IN   2195               17560000           300        45161

                OUT  21986666666        5555555551231231   55551      5454125111

表1-4 display application statistics top命令显示信息描述表

字段

描述

Interface

接口的名称

Application

应用的名称

In/Out

入方向/出方向

Packets

接口上接收或发送的报文个数

Bytes

接口上接收或发送的字节数

PPS

每秒报文数

BPS

每秒比特数

【相关命令】

·**app-group**

·**application statistics ****enable**

**APR \-- APR配置命令 \-- display port-mapping pre-defined**

------------------------------------------------------------------------

**[display port-mapping pre-defined**]命令用来显示预定义的端口映射信息。

【命令】

**[display port-mapping** **pre-defined**]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示预定义的端口映射信息。

\<Sysname\> display port-mapping pre-defined

 Application                      Protocol Port

 tacacs-ds                        TCP      65

                                  UDP      65

 net-bios-dgm                     TCP      137, 138, 139

                                  UDP      137, 138, 139

 ftp                              TCP      21

 tftp                             UDP      69

表1-5 display port-mapping pre-defined命令显示信息描述表

字段

描述

Application

进行端口映射的应用层协议

Protocol

传输层协议类型

Port

应用层协议的端口号

【相关命令】

·**display port-mapping**

·**port-mapping**

**APR \-- APR配置命令 \-- display port-mapping user-defined**

------------------------------------------------------------------------

**[display port-mapping user-defined**]命令用来显示自定义的端口映射信息。

【命令】

**[display port-mapping user-defined ** **application** ]*application[-name \| ]***port** *port-number*

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[application** *application-name*]：显示指定端口映射的应用协议。*application-name*表示应用协议名称，必须标准且能够被设备识别，不区分大小写。

**[port**]* port-number*：显示指定应用层协议的端口。*port-number*表示端口号，取值范围为0～65535。

【使用指导】

若不指定任何参数，则表示显示所有的用户自定义端口映射信息。

【举例】

\# 显示所有自定义的端口映射信息。

\<Sysname\> display port-mapping user-defined

 Application       Port  Protocol    Match Type  Match Condition

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 FTP                21     TCP          \-\--          \-\--

 FTP                21     UDP          IPv4 host   10.10.10.1(vpn1)

[ FTP                2121   UDP          IPv4 host   [11.10.10.1, 11.10.10.10](vpn2)]

 FTP                21     UDP          IPv4 subnet 10.10.10.1/24

 FTP                21     SCTP         IPv6 host   2000:fdb8::1:00ab:853c:39ab

 HTTP               899    TCP          IPV4 ACL    3002

 HTTP               999    SCTP         IPv6 ACL    3002

表1-6 display port-mapping user-defined命令显示信息描述表

字段

描述

Application

进行端口映射的应用层协议

Port

应用层协议映射的端口号

Protocol

传输层协议类型

Match Type

匹配方式，包括以下类型：

·\-\--：表示通配，即未指定匹配类型和匹配条件，所有报文都可以进行匹配

·IPv4 host：表示基于报文的目的IPv4地址进行匹配

·IPv6 host：表示基于报文的目的IPv6地址进行匹配

·IPv4 subnet：表示基于报文的目的IPv4网段进行匹配

·IPv6 subnet：表示基于报文的目的IPv6网段进行匹配

·IPv4 ACL：表示基于IPv4 ACL进行匹配

·IPv6 ACL：表示基于IPv6 ACL进行匹配

Match Condition

匹配条件，包括以下几种情况：

·对于IPv4 host/IPv6 host匹配方式，显示为主机报文的目的IP地址

·对于IPv4 subnet/IPv6 subnet匹配方式，显示为主机报文的目的网段地址

·对于IPv4 ACL/IPv6 ACL匹配方式，显示为ACL编号

对于host和subnet类型的端口映射配置，如果指定了主机所属的VPN，则还会显示其所属的MPLS L3VPN的VPN实例名称

**APR \-- APR配置命令 \-- include application**

------------------------------------------------------------------------

**[include application**]命令用来在应用组中添加应用。

**[undo include application**]命令用来在应用组中删除应用。

【命令】

**[include application*** application-name*]

**[undo include application ***application-name*]

【缺省情况】

应用组中不包含任何应用。

【视图】

应用组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[application*]*-name*：向应用组中添加的应用的名称，为1～63个字符的字符串，不区分大小写，可以为数字、字母、连字符、下划线，不允许为系统保留的invalid或other。

【使用指导】

可以通过多次执行本命令为一个应用组中添加多个预定义应用和自定义应用，每个组里最多可以包含65536个自定义应用。

向应用组中添加应用时，如果对应的应用不存在就会创建这个应用，但该应用的报文是否能被识别，取决于系统中是否定义了相应的识别规则，比如端口映射配置。

【举例】

\# 在应用组abc中增加应用HTTP和FTP。

\<Sysname\> system-view

Sysname app-group abc

Sysname-app-group-abc include application http

Sysname-app-group-abc include application ftp

【相关命令】

·**app-group**

·**copy app-group**

**APR \-- APR配置命令 \-- port-mapping**

------------------------------------------------------------------------

**[port-mapping**]命令用来配置通用端口映射。

**[undo port-mapping**]命令用来删除指定的通用端口映射。

【命令】

**[port-mapping** **application** *application-name*]**port** *port-number*  **protocol** *protocol-name*

**[undo port-mapping** **application** *application-name*]**port** *port-number*  **protocol** *protocol-name*

【缺省情况】

各应用层协议与其对应的知名端口号映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[application*** application-name*]：指定端口映射的应用层协议。*app-name*表示应用协议名称。该应用层协议名称必须标准且能够被设备识别，不区分大小写。

**[port**]* port-number*：指定与应用层协议映射的端口。*port-number*表示端口号，取值范围为0～65535。

**[protocol ***protocol-name*]：指定应用层协议使用的传输层协议名称，其取值及含义如下：

·**dccp**：表示DCCP（Datagram Congestion Control Protocol，数据报拥塞控制协议）协议。

·**sctp**：表示SCTP（Stream Control Transmission Protocol，流控制传输协议）协议。

·**tcp**：表示TCP协议。

·**udp**：表示UDP协议。

·**udp-lite**：表示UDP-Lite协议。

【使用指导】

若不指定**protocol**参数，则表示所有传输层协议的指定报文均可被识别为指定应用层协议的报文。

如果报文的目的端口号与某个通用端口映射匹配，则该报文将被识别为相应的应用层协议报文。

对于端口号、传输层协议参数均相同但是应用层协议名称不相同的两个配置，新的配置会覆盖原有的配置。

指定传输层协议名称的映射优先级高于不指定传输层协议名称的映射。

【举例】

\# 建立端口3456到FTP协议的通用端口映射。

\<Sysname\> system-view

Sysname port-mapping application ftp port 3456

【相关命令】

·**display port-mapping user-defined**

**APR \-- APR配置命令 \-- port-mapping acl**

------------------------------------------------------------------------

**[port-mapping acl**]命令用来配置基于ACL的主机端口映射。

**[undo port-mapping acl**]命令用来删除指定的主机端口映射。

【命令】

**[port-mapping** **application** *application-name*]**port** *port-number*  **protocol** *protocol-name*  **acl** [ **ipv6**  *acl-number*]

**[undo port-mapping** **application** *application-name*]**port** *port-number*  **protocol** *protocol-name*  **acl** [ **ipv6**  *acl-number*]

【缺省情况】

各应用层协议与其对应的知名端口号映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[application*** application-name*]：指定端口映射的应用层协议。*application-name*表示应用层协议名称。该应用协议名称必须标准且能够被设备识别，不区分大小写。

**[port**]* port-number*：指定与应用层协议映射的端口。*port-number*表示端口号，取值范围为0～65535。

**[protocol ***protocol-name*]：指定应用层协议使用的传输层协议名称，其取值及含义如下：

·**dccp**：表示DCCP（Datagram Congestion Control Protocol，数据报拥塞控制协议）协议。

·**sctp**：表示SCTP（Stream Control Transmission Protocol，流控制传输协议）协议。

·**tcp**：表示TCP协议。

·**udp**：表示UDP协议。

·**udp-lite**：表示UDP-Lite协议。

**[acl**  **ipv6**  *acl-number*]：ACL编号，取值范围为2000～2999。如果指定**ipv6**，则表示IPv6 ACL，否则表示IPv4 ACL。

【使用指导】

若不指定**protocol**参数，则表示所有传输层协议的指定报文均可被识别为指定应用层协议的报文。

对于匹配指定ACL的报文（其目的IP地址与ACL中某规则指定的源IP地址参数相匹配），如果报文的目的端口号与某个映射关系匹配，则该报文将被识别为对应的应用层协议报文。

对于端口号、传输层协议、ACL参数均相同但是应用层协议名称不相同的两个配置，新的配置会覆盖原有的配置。

指定传输层协议名称的映射优先级高于不指定传输层协议名称的映射。

【举例】

\# 为匹配ACL 2000的报文，建立端口3456到FTP协议的映射。

\<Sysname\> system-view

Sysname port-mapping application ftp port 3456 acl 2000

【相关命令】

·**display port-mapping user-defined**

**APR \-- APR配置命令 \-- port-mapping host**

------------------------------------------------------------------------

**[port-mapping host**]命令用来设置基于IP地址的主机端口映射。

**[undo port-mapping host**]命令用来删除指定IP地址的主机端口映射。

【命令】

**[port-mapping** **application** *application-name*]**port** *port-number*  **protocol** *protocol-name*  **host **[{ **ip** *\|* **ipv6** } *start-ip-address* [ *end-ip-address* ]  **vpn-instance** *vpn-instance-name* ]

**[undo port-mapping** **application** *application-name*]**port** *port-number*  **protocol** *protocol-name*  **host **[{ **ip** *\|* **ipv6** } *start-ip-address* [ *end-ip-address* ]  **vpn-instance** *vpn-instance-name* ]

【缺省情况】

各应用层协议与其对应的知名端口号映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[application*** application-name*]：指定端口映射的应用层协议。*application-name*表示应用层协议名称，该应用协议名称必须标准且能够被设备识别，不区分大小写。

**[port**]* port-number*：指定与应用层协议映射的端口。*port-number*表示端口号，取值范围为0～65535。

**[protocol ***protocol-name*]：指定应用层协议使用的传输层协议名称，其取值及含义如下：

·**dccp**：表示DCCP（Datagram Congestion Control Protocol，数据报拥塞控制协议）协议。

·**sctp**：表示SCTP（Stream Control Transmission Protocol，流控制传输协议）协议。

·**tcp**：表示TCP协议。

·**udp**：表示UDP协议。

·**udp-lite**：表示UDP-Lite协议。

**[ip**]：指定基于IPv4地址的主机端口映射。

**[ipv6**]：指定基于IPv6地址的主机端口映射。

*[start-ip-address *] *end-ip-address* ：表示IPv4地址范围或IPv6地址范围。*start-ip-address*表示起始IP地址，*end-ip-address*表示终止IP地址。如果仅配置*start-ip-address*，则表示单个主机；如果同时配置*start-ip-address*和*end-ip-address*，则表示位于*start-ip-address*和*end-ip-address*范围内的所有主机，其中的*end-ip-address*必须大于等于*start-ip-address*。

**[vpn-instance **]*vpn-instance-name*：表示报文所属的VPN。*vpn-instance-name*为MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则表示报文属于公网。

【使用指导】

若不指定**protocol**参数，则表示所有传输层协议的指定报文均可被识别为指定应用层协议的报文。

对于目的地址为指定地址或指定范围的地址的报文，如果报文的目的端口号与某个映射关系匹配，则该报文将被识别为对应的应用层协议报文。

对于应用协议、端口号、传输层协议参数均相同的配置，要求各配置中指定的IP地址或者IP地址范围不能重叠。

对于端口号、传输层协议、IP地址或地址范围参数均相同但是应用层协议名称不相同的两个配置，新的配置会覆盖原有的配置。

指定传输层协议名称的映射优先级高于不指定传输层协议名称的映射。

【举例】

\# 为目的IP地址范围为1.1.1.1～1.1.1.10的IPv4报文，建立端口3456到FTP协议的映射。

\<Sysname\> system-view

Sysname port-mapping application ftp port 3456 host ip 1.1.1.1 1.1.1.10

\# 为目的IP地址为1::1的IPv6报文，建立端口3456到FTP协议的映射。

\<Sysname\> system-view

Sysname port-mapping application ftp port 3456 host ipv6 1::1

【相关命令】

·**display port-mapping user-defined**

**APR \-- APR配置命令 \-- port-mapping subnet**

------------------------------------------------------------------------

**[port-mapping subnet**]命令用来配置基于网段的主机端口映射。

**[undo port-mapping subnet**]命令用来删除指定网段的主机端口映射。

【命令】

**[port-mapping** **application** *application-name*]**port** *port-number*  **protocol** *protocol-name*  **subnet **[{ **ip** *ipv4-address* { *mask-length* \| *mask* } \| **ipv6** *ipv6-address* *prefix-length* } [ **vpn-instance** *vpn-instance-name* ] ]

**[undo port-mapping** **application** *application-name*]**port** *port-number*  **protocol** *protocol-name*  **subnet **[{ **ip** *ipv4-address* { *mask-length* \| *mask* } \| **ipv6** *ipv6-address* *prefix-length* } [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

各应用层协议与其对应的知名端口号映射。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[application*** application-name*]：指定端口映射的应用层协议。*application-name*表示应用层协议名称。该应用协议名称必须标准且能够被设备识别，不区分大小写。

**[port**]* port-number*：指定与应用层协议映射的端口。*port-number*表示端口号，取值范围为0～65535。

**[protocol ***protocol-name*]：指定应用层协议使用的传输层协议名称，其取值及含义如下：

·**dccp**：表示DCCP（Datagram Congestion Control Protocol，数据报拥塞控制协议）。

·**sctp**：表示SCTP（Stream Control Transmission Protocol，流控制传输协议）。

·**tcp**：表示TCP协议。

·**udp**：表示UDP协议。

·**udp-lite**：表示UDP-Lite协议。

**[ip**]：指定基于IPv4网段的主机端口映射。

*[ipv4-address*  { *mask-length* \| *mask* }]：指定IPv4网段。其中，*ipv4-address*表示IPv4地址；*mask-length*表示子网掩码长度，取值范围为1～32；*mask*表示子网掩码，为点分十进制格式。

**[ipv6**]：指定基于IPv6网段的主机端口映射。

*[ipv6-address prefix-length*]：指定IPv6网段。其中，*ipv6-address*表示IPv6地址；*prefix-length*表示IPv6前缀长度，取值范围为1～128。

**[vpn-instance **]*vpn-instance-name*：表示主机所属的VPN。*vpn-instance-name*为MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则表示主机属于公网。

【使用指导】

若不指定**protocol**参数，则表示所有传输层协议的指定端口的报文均被识别为指定应用层协议的报文。

对于目的地址为指定网段的报文，如果报文的目的端口号与某个映射关系匹配，则该报文将被识别为对应的应用层协议报文。

PBAR以最精确的网络范围对报文进行匹配，即如果配置了多条网段映射关系，且各映射关系中指定的网段范围互相包含，则使用网络范围最小的映射配置进行匹配。

对于端口号、传输层协议、IP网段参数均相同但是应用层协议名称不相同的两个配置，新的配置会覆盖原有的配置。

指定传输层协议名称的映射优先级高于不指定传输层协议名称的映射。

【举例】

\# 为目的网段地址为1.1.1.0/24的IPv4主机报文，建立端口3456到FTP协议的映射。

\<Sysname\> system-view

Sysname port-mapping application ftp port 3456 subnet ip 1.1.1.0 24

\# 为目的网段地址为1:: /120的IPv6主机报文，建立端口3456到FTP协议的映射。

\<Sysname\> system-view

Sysname port-mapping application ftp port 3456 subnet ipv6 1:: 120

【相关命令】

·**display port-mapping user-defined**

**APR \-- APR配置命令 \-- reset application statistics**

------------------------------------------------------------------------

**[reset application statistics**]命令用来清除指定接口或所有接口的应用统计信息。

【命令】

**[reset application statistics ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：清除指定接口上的应用统计信息，*interface-type* *interface-number*表示接口类型和接口编号。

【举例】

\# 清除接口GigabitEthernet1/0/1上的应和统计信息。

\<Sysname\> reset application statistics interface gigabitethernet 1/0/1

\# 清除所有统计信息。

\<Sysname\> reset application statistics

【相关命令】

·**application statistics enable**

·**display application statistics**
