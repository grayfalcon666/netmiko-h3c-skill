
**漫游 \-- 漫游配置命令 \-- authentication-mode**

------------------------------------------------------------------------

**[authentication-mode**]命令用来配置漫游组认证模式。

**[undo authentication-mode**]****命令用来恢复缺省情况。

【命令】

**[authentication-mode **]*authentication-mode *[[ **cipher** \| **simple** ] *authentication-key*]

**[undo authentication-mode**]

【缺省情况】

未配置认证模式，即不对IACTP控制消息进行完整性校验。

【视图】

本地漫游组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]**：**以密文方式设置密钥。

**[simple**]**：**以明文方式设置密钥。

*[authentication-key*]**：**设置明文密钥或密文密钥，区分大小写。明文密钥的长度范围是1～16；密文密钥的长度范围是24～53。

【使用指导】

配置认证模式后，所有在IACTP隧道中传输的控制消息都会附带一个摘要（完整性代码），该代码用来与消息内容进行计算。当AC接收到该消息后会重新计算并与消息中携带的摘要进行比较来确认收到的消息的完整性。

以明文或密文方式设置的密钥，均以密文的方式保存在配置文件中。

【举例】

\# 配置IACTP控制消息完整性认证模式为MD5认证模式，以明文方式设置密钥12345。

\<Sysname\> system-view

Sysname wlan mobility group aaa

Sysname-wlan-mg-aaa authentication-mode md5 plain 12345

**漫游 \-- 漫游配置命令 \-- display wlan mobility**

------------------------------------------------------------------------

**[display wlan mobility**]命令用来显示客户端漫入或漫出的信息。

【命令】

**[display wlan mobility **[{ **roam-in** \| **roam-out** } [ **member** { **ip** *ipv4-address* \| **ipv6** *ipv6-address* } ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[roam-in**]：显示漫入客户端的信息，即从其它AC漫游到本AC的客户端信息。

**[roam-out**]：显示漫出客户端的信息，即从本AC漫游到其它AC的客户端信息。

**[member ip ***ipv4-address*]：漫游组成员AC的IPv4地址。

**[member ipv6 ***ipv6-address*]：漫游组成员AC的IPv6地址。

【使用指导】

如果不指定**member**参数，则显示所有客户端漫入或漫出的信息。

【举例】

\# 显示所有漫入客户端的信息。

\<Sysname\> display wlan mobility roam-in

Total entries: 1

MAC address     BSSID           VLAN ID  HA IP address

5250-0012-0411  cbab-abab-abab  1        192.168.0.101

\# 显示从指定成员AC漫入的客户端信息。

\<Sysname\> display wlan mobility roam-in member ip 192.168.0.101

Total entries: 1

MAC address     BSSID           VLAN ID

5250-0012-0411  cbab-abab-abab  1

\# 显示所有漫出客户端的信息。

\<Sysname\> display wlan mobility roam-out

Total entries: 1

MAC address     BSSID           VLAN ID  Online time       FA IP address

5250-0012-0411  cbab-abab-abab  1        00hr 01min 39sec  192.168.0.102

\# 显示从指定成员AC漫出的客户端信息。

Sysname display wlan mobility roam-out member ip 192.168.0.102

Total entries: 1

MAC address     BSSID           VLAN ID  Online time

5250-0012-0411  cbab-abab-abab  1        00hr 03min 02sec

表1-1 display wlan mobility命令显示信息描述表

字段

描述

Total entries

客户端总数目

MAC address

客户端的MAC地址

BSSID

客户端关联的AP的BSSID

VLAN ID

客户端所在的VLAN ID

HA IP address

HA的IP地址

FA IP address

FA的IP地址

Online time

客户端的累积在线时长

**漫游 \-- 漫游配置命令 \-- display wlan mobility roam-track mac-address**

------------------------------------------------------------------------

**[display wlan mobility roam-track mac-address**]命令用来在HA上显示客户端的漫游跟踪信息。

【命令】

**[display wlan mobility roam-track mac-address ***mac-address*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[mac-address*]：客户端的MAC地址，格式为[H-H-H。]

【使用指导】

在显示信息中，漫游跟踪信息以漫游到达AP的先后依次排序，最近的轨迹排在第一行。

【举例】

\# 显示MAC地址为5250-0012-0411的客户端的漫游跟踪信息。

\<Sysname\> display wlan mobility roam-track mac-address 5250-0012-0411

Total entries: 2

BSSID           Online time       AC IP address

3ce5-a68d-2280  00hr 48min 46sec  192.168.0.2

0026-3e08-1150  00hr 40min 46sec  127.0.0.1

表1-2 display wlan mobility roam-track mac-address命令显示信息描述表

字段

描述

BSSID

客户端关联的AP的BSSID

Online time

客户端的累积在线时长

AC IP address

客户端上线所在AC的IP地址。当客户端在HA上时，显示的IP地址为127.0.0.1

**漫游 \-- 漫游配置命令 \-- display wlan mobility group**

------------------------------------------------------------------------

**[display wlan mobility group**]命令用来显示本地漫游组的信息。

【命令】

**[display wlan mobility group ***group-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-name*]：本地漫游组名，为1～15个字符的字符串，区分大小写。

【使用指导】

如果不指定本地漫游组名，则显示所有本地漫游组的信息。

【举例】

\# 显示指定本地漫游组的信息。

\<Sysname\> display wlan mobility group aaa

Mobility group name: aaa

 Tunnel type: IPv4

 Source IPv4: 172.16.220.101

 Source IPv6: Not configured

Authentication mode  : Not configured

 Mobility group status: Enabled

 Member entries: 2

 IP address                              State          Online time

 172.16.220.102                          Down           00hr 00min 00sec

 172.16.220.105                          Up             00hr 36min 27sec

表1-3 display wlan mobility group命令显示信息描述表

字段

描述

Mobility group name

本地漫游组的名称

Tunnel type

本地漫游组的隧道类型，有未配置，IPv4和IPv6三种隧道类型

Source IPv4

源IPv4地址

Source IPv6

源IPv6地址

Authentication method

本地漫游组的认证方式

Mobility group status

本地漫游组的状态：

·Enabled：本地漫游组处于开启状态

·Disabled：本地漫游组处于关闭状态

Member entries

成员AC的数量

IP address

成员AC的IP地址

State

隧道状态

Up：已建立IACTP隧道

Down：未建立IACTP隧道

Online time

成员的累计在线时长

**漫游 \-- 漫游配置命令 \-- group enable**

------------------------------------------------------------------------

**[group enable**]命令用来开启漫游组功能。

**[undo group enable**]命令用来恢复缺省情况。

【命令】

**[group enable**]

**[undo group enable**]

【缺省情况】

漫游组功能处于关闭状态。

【视图】

本地漫游组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·只有配置了与隧道类型相同的源IP地址和成员AC的IP地址后，才可以开启漫游组功能。

·开启漫游组功能后，AC会使用源IP地址与组内其他成员AC建立IACTP隧道，并同步漫游表项信息。

·关闭漫游组功能后，AC会断开同组内其他成员AC的IACTP隧道连接，并删除漫游表项信息。

【举例】

\# 开启漫游组功能。

\<Sysname\> system-view

Sysname wlan mobility group floor1

Sysname-wlan-mg-floor1 tunnel-type ipv4

Sysname-wlan-mg-floor1 source ip 192.168.0.1

Sysname-wlan-mg-floor1 member ip 192.168.0.2

Sysname-wlan-mg-floor1 group enable

【相关命令】

·**wlan mobility group**

·**member**

·**source**

·**tunnel-type**

**漫游 \-- 漫游配置命令 \-- member**

------------------------------------------------------------------------

**[member**]命令用来添加漫游组内的AC成员。

**[undo member**]命令用来删除漫游组内的AC成员。

【命令】

**[member ** { **ip** *ip-address \|* **ipv6** *ipv6-address* }]

**[undo member ** [ **ip** *ip-address \|* **ipv6** *ipv6-address* ]]

【缺省情况】

漫游组内不存在AC成员。

【视图】

本地漫游组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip **]*ip-address*：漫游组内AC成员的IPv4地址。

**[ipv6**]* ipv6-address*：漫游组内AC成员的IPv6地址。

【使用指导】

·漫游组内的AC成员通过IP地址标识，该IP地址为AC成员建立IACTP隧道的源IP地址，一个成员只能属于一个漫游组。

·删除漫游组成员时，如果不指定IP地址，则删除漫游组内所有成员。

·可以使用该命令添加IPv4和IPv6类型的成员地址，但是只有与隧道类型相同的成员地址才能生效。

·**member**命令和**undo member**命令只能在漫游组处于关闭的情况下使用。

【举例】

\# 为漫游组添加一个AC成员。

\<Sysname\> system-view

Sysname wlan mobility group abc

Sysname-wlan-mg-abc member ip 192.168.1.55

**漫游 \-- 漫游配置命令 \-- source**

------------------------------------------------------------------------

**[source**]命令用来[配置]AC加入本地漫游组时建立IACTP隧道的源IP地址。

**[undo source**]命令用来删除建立IACTP隧道的源IP地址。

【命令】

**[source ** { **ip** *ip-address \|* **ipv6** *ipv6-address* }]

**[undo source ** [**ip** *\|* **ipv6**]]

【缺省情况】

未配置建立IACTP隧道的源IP地址。

【视图】

本地漫游组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip **]*ip-address*：AC加入漫游组时建立IACTP隧道的源IPv4地址。

**[ipv6**]* ipv6-address*：AC加入漫游组时建立IACTP隧道的源IPv6地址。

【使用指导】

·AC在加入漫游组后需要使用IACTP隧道源IP地址和同一漫游组内AC成员建立IACTP隧道。

·只有与漫游组隧道IP地址类型相同的源地址才能生效。

·删除建立IACTP隧道的源IP地址时，如果指定地址类型，则删除指定类型的源IP地址。如果没有指定地址类型，则删除所有源IP地址。

·**source**命令和**undo source**命令只能在漫游组处于关闭的情况下使用。

【举例】

\# 配置AC加入漫游组时建立IACTP隧道的源IP地址。

\<Sysname\> system-view

Sysname wlan mobility group abc

Sysname-wlan-mg-abc source ip 192.168.1.55

【相关命令】

·**group enable**

·**member**

**漫游 \-- 漫游配置命令 \-- tunnel-type**

------------------------------------------------------------------------

**[tunnel-type**]命令用来[配置漫游组]IACTP隧道IP地址类型。

**[undo tunnel-type**]命令用来删除配置的漫游组隧道IP地址类型。

【命令】

**[tunnel-type ** { **ipv4 \| ipv6** }]

**[undo tunnel-type ** { **ipv4 \| ipv6** }]

【缺省情况】

未配置漫游组IACTP隧道IP地址类型。

【视图】

本地漫游组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]:指定漫游组使用IPv4类型的隧道IP地址。

**[ipv6**]:指定漫游组使用IPv6类型的隧道IP地址。

【使用指导】

**[tunnel-type**]命令和**undo tunnel-type**命令只能在漫游组未使能的情况下使用并且不能同时配置两种隧道IP地址类型。

【举例】

\# 配置漫游组IACTP隧道IP地址类型IPv6。

\<Sysname\> system-view

Sysname wlan mobility group aaa

Sysname-wlan-mg-aaa tunnel-type ipv6

**漫游 \-- 漫游配置命令 \-- wlan mobility group**

------------------------------------------------------------------------

**[wlan mobility group**]命令用来创建本地漫游组。

**[undo wlan mobility group**]命令用来删除本地漫游组。

【命令】

**[wlan mobility group **]*group-name*

**[undo wlan mobility group **]*group-name*

【缺省情况】

不存在本地漫游组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：本地漫游组名，为1～15个字符的字符串，区分大小写。

【使用指导】

·同一本地漫游组内的成员的本地漫游组名应该保持一致。

·每个设备只允许创建一个本地漫游组。

·本地漫游组只在水平组网中的AC上生效。

【举例】

\# 创建本地漫游组。

\<Sysname\> sysname-view

Sysname wlan mobility group aaa

Sysname-wlan-mg-aaa

