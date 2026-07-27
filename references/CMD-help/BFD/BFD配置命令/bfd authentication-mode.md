<!-- CMD-INDEX
  bfd authentication-mode             | 接口视图/BFD模板视图     | L24
  bfd demand enable                   | 接口视图             | L108
  bfd detect-interface                | 接口视图             | L166
  bfd detect-multiplier               | 接口视图/BFD模板视图     | L222
  bfd echo enable                     | 接口视图             | L282
  bfd echo-source-ip                  | 系统视图             | L340
  bfd echo-source-ipv6                | 系统视图             | L384
  bfd min-echo-receive-interval       | 接口视图             | L430
  bfd min-receive-interval            | 接口视图/BFD模板视图     | L488
  bfd min-transmit-interval           | 接口视图/BFD模板视图     | L548
  bfd multi-hop authentication-mode   | 系统视图             | L606
  bfd multi-hop destination-port      | 系统视图             | L676
  bfd multi-hop detect-multiplier     | 系统视图             | L716
  bfd multi-hop min-receive-interval  | 系统视图             | L762
  bfd multi-hop min-transmit-interval | 系统视图             | L806
  bfd session init-mode               | 系统视图             | L850
  bfd template                        | 系统视图             | L898
  display bfd session                 | 任意视图             | L944
  reset bfd session statistics        | 用户视图             | L1194
  snmp-agent trap enable bfd          | 系统视图             | L1220
-->

**BFD \-- BFD配置命令 \-- bfd authentication-mode**

------------------------------------------------------------------------

![说明](BFD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bfd authentication-mode**]命令用来配置单跳BFD控制报文进行认证的方式。

**[undo** **bfd authentication-mode**]命令用来恢复缺省情况。

【命令】

**[bfd authentication-mode****[{ **m-md5** \| **m-sha1** \| **md5** \| **sha1** \| **simple** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* }]]

**[undo bfd authentication-mode**]

【缺省情况】

单跳BFD控制报文不进行认证。

【视图】

接口视图/BFD模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[m-md5**]：采用Meticulous MD5算法进行认证。

**[m-sha1**]：采用Meticulous SHA1算法进行认证。

**[md5**]：采用MD5算法进行认证。

**[sha1**]：采用SHA1算法进行认证。

**[simple**]**：**采用简单认证。

*[key-id*]：认证字标识符，取值范围为1～255。

**[cipher**]：表示输入的密码为密文。

*[cipher-string*]：表示设置的密文密码，为33～53个字符的字符串，区分大小写。

**[plain**]：表示输入的密码为明文。

*[plain-string*]：表示设置的明文密码，为1～16个字符的字符串，区分大小写。

【使用指导】

本命令主要为了提高BFD会话的安全性。

以明文或密文方式设置的密码，均以密文的方式保存在配置文件中。

BFD版本0不支持本命令，配置不生效。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1对单跳BFD控制报文进行简单明文认证，认证字标识符为1，密码为123456。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bfd authentication-mode simple 1 plain 123456

·交换应用

\# 配置接口Vlan-interface11对单跳BFD控制报文进行简单明文认证，认证字标识符为1，密码为123456。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 bfd authentication-mode simple 1 plain 123456

**BFD \-- BFD配置命令 \-- bfd demand enable**

------------------------------------------------------------------------

**[bfd demand enable**]命令用来配置BFD会话为查询模式。

**[undo bfd demand enable**]命令用来恢复缺省情况。

【命令】

**[bfd demand enable**]

**[undo** **bfd demand enable**]

【缺省情况】

BFD会话为异步模式。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在查询模式下，设备周期性发送BFD控制报文，但是对端（缺省为异步模式）会停止周期性发送BFD控制报文。如果通信双方都是查询模式，则双方都停止周期性发送BFD控制报文。当需要验证连接性的时候，设备会以协商的周期连续发送几个P比特位置1的BFD控制报文。如果在检测时间内没有收到返回的报文，就认为会话down；如果收到对方的回应F比特位置1的报文，就认为连通，停止发送报文，等待下一次触发查询。

在异步模式下，设备周期性地发送BFD控制报文，如果在检测时间内对端没有收到BFD控制报文，则认为会话down。

BFD版本0不支持本命令，配置不生效。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置BFD会话为查询模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bfd demand enable

·交换应用

\# 在接口Vlan-interface11上配置BFD会话为查询模式。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 bfd demand enable

**BFD \-- BFD配置命令 \-- bfd detect-interface**

------------------------------------------------------------------------

![说明](BFD命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bfd detect-interface source-ip**]命令用来创建一个检测本接口状态的BFD会话。

**[undo bfd** **detect-interface**]命令用来删除创建的检测本接口状态的BFD会话。

【命令】

**[bfd detect-interface source-ip** *ip-address*]

**[undo bfd** **detect-interface**]

【缺省情况】

没有创建检测本接口状态的BFD会话。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：BFD控制报文的源IP地址。

【使用指导】

三层聚合接口的成员端口上没有IP地址，没有可以支持的快速检测机制。通过本功能可以快速检测成员链路的故障，帮助快速找出故障成员接口；本功能同时支持普通三层以太网接口故障快速检测，实现接口状态与BFD会话状态的快速联动，帮助上层路由协议实现快速收敛。

BFD会话采用控制报文方式，两端都必须配置；报文目的地址固定为224.0.0.184，不支持配置。

源IP地址建议配置为接口IP地址，如果接口没有IP地址，建议配置一个单播地址（0.0.0.0除外）。

在同一接口下，同时配置**bfd detect-interface**和**bfd echo enable**命令，只有**bfd detect-interface**命令生效。

【举例】

\# 配置检测GigabitEthernet1/0/1接口状态的BFD会话，其源地址为接口地址20.1.1.1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bfd detect-interface source-ip 20.1.1.1

**BFD \-- BFD配置命令 \-- bfd detect-multiplier**

------------------------------------------------------------------------

**[bfd detect-multiplier**]命令用来配置[单跳]BFD检测时间倍数。

**[undo** **bfd detect-multiplier**]命令用来恢复缺省情况。

【命令】

**[bfd detect-multiplier ***value*]

**[undo** **bfd detect-multiplier**]

【缺省情况】

单跳BFD检测时间倍数为5。

【视图】

接口视图/BFD模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：单跳BFD检测时间倍数，取值范围为3～50。

【使用指导】

检测时间倍数，即允许发送方发送BFD报文（包括echo报文和控制报文）的最大连续丢包数。

对于echo报文方式，实际检测时间为发送方的检测时间倍数和发送方的实际发送时间的乘积；对于控制报文方式的异步模式，实际检测时间为接收方的检测时间倍数和接收方的实际发送时间的乘积；对于控制报文方式的查询模式，实际检测时间为发送方的检测时间倍数和发送方的实际发送时间的乘积。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1的单跳BFD检测时间倍数为6。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bfd detect-multiplier 6

·交换应用

\# 配置接口Vlan-interface11的单跳BFD检测时间倍数为6。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 bfd detect-multiplier 6

**BFD \-- BFD配置命令 \-- bfd echo enable**

------------------------------------------------------------------------

**[bfd echo enable**]命令用来使能echo功能。

**[undo** **bfd echo enable**]命令用来恢复缺省情况。

【命令】

**[bfd echo enable**]

**[undo bfd echo enable**]

【缺省情况】

echo功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本功能在发送控制报文的BFD会话时使用。使能echo功能并且会话up后，设备周期性发送echo报文检测链路连通性，同时降低控制报文的接收速率。

在同一接口下，同时配置**bfd detect-interface**和**bfd echo enable**命令，只有**bfd detect-interface**命令生效。

BFD版本0不支持本命令，配置不生效。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1使能echo功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bfd echo enable

·交换应用

\# 配置接口Vlan-interface11使能echo功能。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 bfd echo enable

**BFD \-- BFD配置命令 \-- bfd echo-source-ip**

------------------------------------------------------------------------

**[bfd echo-source-ip**]命令用来配置echo报文的源IP地址。

**[undo** **bfd echo-source-ip**]命令用来删除echo报文的源IP地址。

【命令】

**[bfd echo-source-ip*** ip-address*]

**[undo** **bfd** **echo-source-ip**]

【缺省情况】

没有配置echo报文的源IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：echo报文的源IP地址。

【使用指导】

echo报文的源IP地址用户可以任意指定。为了避免对端发送大量的ICMP重定向报文造成网络拥塞，建议配置echo报文的源IP地址不属于该设备任何一个接口所在网段。

【举例】

\# 配置echo报文的源IP地址为8.8.8.8。

\<Sysname\> system-view

Sysname bfd echo-source-ip 8.8.8.8

**BFD \-- BFD配置命令 \-- bfd echo-source-ipv6**

------------------------------------------------------------------------

**[bfd echo-source-ipv6**]命令用来配置echo报文的源IPv6地址。

**[undo** **bfd echo-source-ipv6**]命令用来删除echo报文的源IPv6地址。

【命令】

**[bfd echo-source-ipv6*** ipv6-address*]

**[undo** **bfd** **echo-source-ipv6**]

【缺省情况】

没有配置echo报文的源IPv6地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：echo报文的源IPv6地址。

【使用指导】

echo报文源IPv6地址仅支持全球单播地址。

为了避免对端发送大量的ICMPv6重定向报文造成网络拥塞，建议不要将echo报文的源IPv6地址配置为属于该设备任何一个接口所在网段。

【举例】

\# 配置echo报文的源IPv6地址为80::2。

\<Sysname\> system-view

Sysname bfd echo-source-ipv6 80::2

**BFD \-- BFD配置命令 \-- bfd min-echo-receive-interval**

------------------------------------------------------------------------

**[bfd min-echo-receive-interval**]命令用来配置接收echo报文的最小时间间隔。

**[undo** **bfd min-echo-receive-interval**]命令用来恢复缺省情况。

【命令】

**[bfd min-echo-receive-interval ***value*]

**[undo** **bfd min-echo-receive-interval**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接收echo报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

使用本命令，设备能够控制接收两个echo报文之间的时间间隔，即echo报文实际发送时间间隔。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1接收echo报文的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bfd min-echo-receive-interval 500

·交换应用

\# 配置接口Vlan-interface11接收echo报文的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 bfd min-echo-receive-interval 500

**BFD \-- BFD配置命令 \-- bfd min-receive-interval**

------------------------------------------------------------------------

**[bfd min-receive-interval**]命令用来配置接收单跳BFD控制报文的最小时间间隔。

**[undo** **bfd min-receive-interval**]命令用来恢复缺省情况。

【命令】

**[bfd min-receive-interval ***value*]

**[undo** **bfd min-receive-interval**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图/BFD模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接收单跳BFD控制报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

本命令主要为了防止对端发送控制报文的速度超过本地接收控制报文的速度。

对端的控制报文实际发送时间为对端发送控制报文的最小时间间隔和本地接收控制报文的最小时间间隔之间的较大值。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1接收单跳BFD控制报文的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bfd min-receive-interval 500

·交换应用

\# 配置接口Vlan-interface11接收单跳BFD控制报文的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 bfd min-receive-interval 500

**BFD \-- BFD配置命令 \-- bfd min-transmit-interval**

------------------------------------------------------------------------

**[bfd min-transmit-interval**]命令用来配置发送单跳BFD控制报文的最小时间间隔。

**[undo** **bfd min-transmit-interval**]命令用来恢复缺省情况。

【命令】

**[bfd min-transmit-interval ***value*]

**[undo** **bfd min-transmit-interval**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

接口视图/BFD模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：发送单跳BFD控制报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

本命令主要是为了保证发送BFD控制报文的速度不能超过设备发送报文的能力。本地实际发送BFD控制报文的时间间隔，为本地配置的发送BFD控制报文的最小时间间隔和对端接收BFD控制报文的最小时间间隔的最大值。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1发送单跳BFD控制报文的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bfd min-transmit-interval 500

·交换应用

\# 配置接口Vlan-interface11发送单跳BFD控制报文的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 bfd min-transmit-interval 500

**BFD \-- BFD配置命令 \-- bfd multi-hop authentication-mode**

------------------------------------------------------------------------

![说明](BFD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bfd **]**multi-hop authentication-mode**命令用来配置多跳BFD控制报文进行认证的方式。

**[undo bfd **]**multi-hopauthentication-mode**命令用来恢复缺省情况。

【命令】

**[bfd **]**multi-hop authentication-mode **[{ **m-md5** \| **m-sha1** \| **md5** \| **sha1** \| **simple** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* }]

**[undo** **bfd** ]**multi-hop authentication-mode**

【缺省情况】

多跳BFD控制报文不进行认证。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[m-md5**]：采用Meticulous MD5算法进行认证。

**[m-sha1**]：采用Meticulous SHA1算法进行认证。

**[md5**]：采用MD5算法进行认证。

**[sha1**]：采用SHA1算法进行认证。

**[simple**]**：**采用简单认证。

*[key-id*]：认证字标识符，取值范围为1～255。

**[cipher**]：表示输入的密码为密文。

*[cipher-string*]：表示设置的密文密码，为33～53个字符的字符串，区分大小写。

**[plain**]：表示输入的密码为明文。

*[plain-string*]：表示设置的明文密码，为1～16个字符的字符串，区分大小写。

【使用指导】

本命令主要为了提高BFD会话的安全性。

以明文或密文方式设置的密码，均以密文的方式保存在配置文件中。

BFD版本0不支持本命令，配置不生效。

【举例】

\# 配置多跳BFD控制报文进行简单明文认证，认证字标识符为1，密码为123456。

\<Sysname\> system-view

Sysname bfd multi-hop authentication-mode simple 1 plain 123456

**BFD \-- BFD配置命令 \-- bfd multi-hop destination-port**

------------------------------------------------------------------------

**[bfd multi-hop destination-port**]命令用来配置多跳BFD控制报文的目的端口号。

**[undo** **bfd multi-hop destination-port**]命令用来恢复缺省情况。

【命令】

**[bfd multi-hop destination-port**]*port-number*

**[undo** **bfd multi-hop destination-port**]

【缺省情况】

多跳BFD控制报文的目的端口号为4784。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：多跳BFD控制报文的目的端口号，取值可以为3784或者4784。

【举例】

\# 配置多跳BFD控制报文的目的端口号为3784。

\<Sysname\> system-view

Sysname bfd multi-hop destination-port 3784

**BFD \-- BFD配置命令 \-- bfd multi-hop detect-multiplier**

------------------------------------------------------------------------

**[bfd **]**multi-hop detect-multiplier**命令用来配置多跳BFD检测时间倍数。

**[undo bfd **]**multi-hop detect-multiplier**命令用来恢复缺省情况。

【命令】

**[bfd multi-hop detect-multiplier ***value*]

**[undo** **bfd multi-hop detect-multiplier**]

【缺省情况】

多跳BFD检测时间倍数为5。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：多跳BFD检测时间倍数，取值范围为3～50。

【使用指导】

检测时间倍数，即接收方允许发送方发送BFD控制报文的最大连续丢包数。

对于控制报文方式的异步模式，实际检测时间为接收方的检测时间倍数和接收方的实际发送时间的乘积；对于控制报文方式的查询模式，实际检测时间为发送方的检测时间倍数和发送方的实际发送时间的乘积。

【举例】

\# 配置多跳BFD检测时间倍数为6。

\<Sysname\> system-view

Sysname bfd multi-hop detect-multiplier 6

**BFD \-- BFD配置命令 \-- bfd multi-hop min-receive-interval**

------------------------------------------------------------------------

**[bfd multi-hop **]**min-receive-interval**命令用来配置接收多跳BFD控制报文的最小时间间隔。

**[undo** **bfd multi-hop**]** min-receive-interval**命令用来恢复缺省情况。

【命令】

**[bfd multi-hop min-receive-interval ***value*]

**[undo** **bfd multi-hop min-receive-interval**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

value：接收BFD控制报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

本命令主要为了防止对端设备发送报文的速度超出本地接收报文的能力（接收BFD控制报文的最小时间间隔），若超出，则对端设备将发送BFD控制报文的时间间隔动态调整为本地接收BFD控制报文的最小时间间隔。

【举例】

\# 配置接收多跳BFD控制报文的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname bfd multi-hop min-receive-interval 500

**BFD \-- BFD配置命令 \-- bfd multi-hop min-transmit-interval**

------------------------------------------------------------------------

**[bfd multi-hop **]**min-transmit-interval**命令用来配置发送多跳BFD控制报文的最小时间间隔。

**[undo** **bfd multi-hop**]**min-transmit-interval**命令用来恢复缺省情况。

【命令】

**[bfd multi-hop min-transmit-interval ***value*]

**[undo** **bfd multi-hop min-transmit-interval**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：发送BFD控制报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

本命令主要是为了保证发送BFD控制报文的速度不能超过设备发送报文的能力。本地实际发送BFD控制报文的时间间隔，为本地配置的发送BFD控制报文的最小时间间隔和对端接收BFD控制报文的最小时间间隔的最大值。

【举例】

\# 配置发送多跳BFD控制报文的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname bfd multi-hop min-transmit-interval 500

**BFD \-- BFD配置命令 \-- bfd session init-mode**

------------------------------------------------------------------------

**[bfd session init-mode**]命令用来配置BFD会话建立前的运行模式。

**[undo** **bfd session init-mode**]命令用来恢复缺省情况。

【命令】

**[bfd session init-mode ** [\| ]**passive****}

**[undo** **bfd session init-mode**]

【缺省情况】]

BFD会话建立前的运行模式为主动模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[active**]：主动模式。在建立会话前不管是否收到对端发来的BFD控制报文，都会主动向会话的对端发送BFD控制报文。

**[passive**]：被动模式。在建立会话前不会主动向会话的对端发送BFD控制报文，只有等收到BFD控制报文后才会向对端发送BFD控制报文。

【使用指导】

通信双方至少要有一方运行在主动模式才能成功建立起BFD会话。

BFD版本0不支持本命令，配置不生效。

【举例】

\# 配置BFD会话建立前的运行模式为被动模式。

\<Sysname\> system-view

Sysname bfd session init-mode passive

**BFD \-- BFD配置命令 \-- bfd template**

------------------------------------------------------------------------

![说明](BFD命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bfd template**]命令用来创建BFD模板，并进入BFD模板视图。

**[undo bfd template**]命令用来删除BFD模板。

【命令】

**[bfd template** *template-name*]

**[undo bfd template** *template-name*]

【缺省情况】

没有创建BFD模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[template-name*]：BFD模板名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 创建BFD模板bfd1，并进入BFD模板视图。

\<Sysname\> system-view

Sysname bfd template bfd1

Sysname-bfd-template-bfd1

**BFD \-- BFD配置命令 \-- display bfd session**

------------------------------------------------------------------------

**[display bfd session**]命令用来显示BFD会话信息。

【命令】

**[display bfd session **[[ **discriminator** *value* \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[discriminator ***value*]：显示指定本地标识符的BFD会话信息。*value*为本地标识符的值，取值范围为1～4294967295。如果未指定本参数，将显示所有BFD会话概要信息。

**[verbose**]：显示会话的详细信息。如果未指定本参数，将显示BFD会话概要信息。

【举例】

\# 显示所有BFD会话的信息（IPv4）。

\<Sysname\> display bfd session

 Total Session Num: 1     Up Session Num: 1     Init Mode: Active

 IPv4 Session Working Under Ctrl Mode:

 LD/RD          SourceAddr      DestAddr        State    Holdtime    Interface

 513/513        1.1.1.1         1.1.1.2         Up       2297ms      GE1/0/1

\# 显示所有BFD会话的信息（IPv6）。

\<Sysname\> display bfd session

 Total Session Num: 1     Up Session Num: 1     Init Mode: Active

 IPv6 Session Working Under Ctrl Mode:

       Local Discr: 513                  Remote Discr: 513

         Source IP: FE80::20C:29FF:FED4:7171

    Destination IP: FE80::20C:29FF:FE72:AC4D

     Session State: Up                      Interface: GE1/0/2

         Hold Time: 2142ms

\# 显示BFD会话的详细信息（IPv4）。

\<Sysname\> display bfd session verbose

 Total Session Num: 1     Up Session Num: 1     Init Mode: Active

 IPv4 Session Working Under Ctrl Mode:

       Local Discr: 513                  Remote Discr: 513

         Source IP: 1.1.1.1            Destination IP: 1.1.1.2

     Session State: Up                      Interface: GigabitEthernet1/0/1

      Min Tx Inter: 500ms                Act Tx Inter: 500ms

      Min Rx Inter: 500ms                Detect Inter: 2500ms

          Rx Count: 42                       Tx Count: 43

      Connect Type: Direct             Running Up for: 00:00:20

         Hold Time: 2078ms                  Auth mode: None

       Detect Mode: Async                        Slot: 0

          Protocol: OSPF

          Version:1

         Diag Info: No Diagnostic

\# 显示BFD会话的详细信息（IPv6）。

\<Sysname\> display bfd session verbose

 Total Session Num: 1     Up Session Num: 1     Init Mode: Active

 IPv6 Session Working Under Ctrl Mode:

       Local Discr: 513                  Remote Discr: 513

         Source IP: FE80::20C:29FF:FED4:7171

    Destination IP: FE80::20C:29FF:FE72:AC4D

     Session State: Up                      Interface: GigabitEthernet1/0/2

      Min Tx Inter: 500ms                Act Tx Inter: 500ms

      Min Rx Inter: 500ms                Detect Inter: 2500ms

          Rx Count: 38                       Tx Count: 38

      Connect Type: Direct             Running Up for: 00:00:15

         Hold Time: 2211ms                  Auth mode: None

       Detect Mode: Async                        Slot: 0

          Protocol: OSPFv3

          Version:1

         Diag Info: No Diagnostic

表1-1 display bfd session命令显示信息描述表

字段

描述

Total Session Num

所有BFD会话的数目

Up Session Num

up的BFD会话的数目

Init Mode

BFD运行模式：

·Active：主动模式

·Passive：被动模式

Session Working Under Ctrl Mode

BFD会话（有IPv4和IPv6两种）的工作方式：

·Ctrl：控制报文方式

·Echo：echo报文方式

Local Discr/LD

会话的本地标识符

Remote Discr/RD

会话的远端标识符

Source IP/SourceAddr

会话的源IP地址

Destination IP/DestAddr

会话的目的IP地址

Session State/State

会话状态：Up和Down

Interface

会话所在的接口名

Min Tx Inter

最小发送时间间隔

Min Rx Inter

最小接收时间间隔

Act Tx Inter

实际发送间隔

Detect Inter

实际检测间隔

Rx Count

接收的报文数

Tx Count

发送的报文数

Hold Time/Holdtime

离会话检测时间超时的剩余时间

Auth mode

会话的认证模式，目前只支持Simple

Connect Type

接口的连接类型：

·Direct：直连

·Indirect：非直连

Running up for

会话持续up的时间

Detect Mode

检测模式：

·Async：异步模式

·Demand：查询模式

Slot

槽号

Protocol

协议名

Version

版本号

Diag Info

会话的诊断信息

**BFD \-- BFD配置命令 \-- reset bfd session statistics**

------------------------------------------------------------------------

**[reset bfd session statistics**]命令用来清除所有BFD会话的统计信息。

【命令】

**[reset bfd session statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除所有BFD会话的统计信息。

\<Sysname\> reset bfd session statistics

**BFD \-- BFD配置命令 \-- snmp-agent trap enable bfd**

------------------------------------------------------------------------

**[snmp-agent trap enable bfd**]命令用来开启BFD的告警功能。

**[undo snmp-agent trap enable bfd**]命令用来关闭BFD的告警功能。

【命令】

**[snmp-agent trap enable bfd**]

**[undo snmp-agent trap enable bfd**]

【缺省情况】

BFD的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启BFD模块的告警功能后，该模块会生成告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。（有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。）

【举例】

\# 关闭BFD的告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable bfd

