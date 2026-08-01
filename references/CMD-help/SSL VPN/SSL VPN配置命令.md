<!-- CMD-INDEX
  aaa domain                          | SSL VPN访问实例视图    | L55
  bandwidth                           | SSL VPN AC接口视图   | L101
  certificate-authentication enable   | SSL VPN访问实例视图    | L155
  default                             | SSL VPN AC接口视图   | L201
  default-policy-group                | SSL VPN访问实例视图    | L239
  description                         | SSL VPN AC接口视图   | L297
  display interface sslvpn-ac         | 任意视图             | L345
  display sslvpn context              | 任意视图             | L599
  display sslvpn gateway              | 任意视图             | L793
  display sslvpn policy-group         | 任意视图             | L939
  display sslvpn port-forward connection | 任意视图             | L1003
  display sslvpn session              | 任意视图             | L1095
  dynamic-password enable             | SSL VPN访问实例视图    | L1223
  emo-server                          | SSL VPN访问实例视图    | L1265
  filter ip-tunnel                    | SSL VPN策略组视图     | L1317
  filter tcp-access                   | SSL VPN策略组视图     | L1369
  filter web-access                   | SSL VPN策略组视图     | L1421
  gateway                             | SSL VPN访问实例视图    | L1473
  http-redirect                       | SSL VPN网关视图      | L1539
  include                             | 路由列表视图           | L1585
  interface sslvpn-ac                 | 系统视图             | L1639
  ip address (SSL VPN gateway view)   | SSL VPN网关视图      | L1681
  ip-route-list                       | SSL VPN访问实例视图    | L1735
  ip-tunnel access-route              | SSL VPN策略组视图     | L1789
  ip-tunnel address-pool              | SSL VPN策略组视图     | L1859
  ip-tunnel dns-server                | SSL VPN策略组视图     | L1919
  ip-tunnel interface                 | SSL VPN访问实例视图    | L1967
  ip-tunnel keepalive                 | SSL VPN策略组视图     | L2019
  ip-tunnel wins-server               | SSL VPN策略组视图     | L2071
  local-port                          | 端口转发列表视图         | L2119
  log enable user-log                 | SSL VPN访问实例视图    | L2191
  login-message                       | SSL VPN访问实例视图    | L2233
  logo                                | SSL VPN访问实例视图    | L2279
  max-users                           | SSL VPN访问实例视图    | L2329
  mtu                                 | SSL VPN AC接口视图   | L2379
  policy-group                        | SSL VPN访问实例视图    | L2421
  port-forward                        | SSL VPN访问实例视图    | L2475
  reset counters interface sslvpn-ac  | 用户视图             | L2533
  resources port-forward              | SSL VPN策略组视图     | L2577
  service enable (SSL VPN context view) | SSL VPN访问实例视图    | L2633
  service enable (SSL VPN gateway view) | SSL VPN网关视图      | L2675
  shutdown                            | SSL VPN AC接口视图   | L2717
  ssl server-policy                   | SSL VPN网关视图      | L2755
  sslvpn context                      | 系统视图             | L2807
  sslvpn gateway                      | 系统视图             | L2857
  sslvpn ip address-pool              | 系统视图             | L2917
  timeout idle                        | SSL VPN策略组视图     | L2967
  title                               | SSL VPN访问实例视图    | L3019
  verify-code                         | SSL VPN访问实例视图    | L3065
  vpn-instance (SSL VPN context View) | SSL VPN访问实例视图    | L3107
  vpn-instance (SSL VPN gateway view) | SSL VPN网关视图      | L3157
-->

**SSL VPN \-- SSL VPN配置命令 \-- aaa domain**

------------------------------------------------------------------------

**[aaa domain**]命令用来配置SSL VPN访问实例使用指定的ISP域进行AAA认证。

**[undo aaa domain**]命令用来恢复缺省情况。

【命令】

**[aaa domain*** domain-name*]

**[undo aaa domain**]

【缺省情况】

SSL VPN访问实例使用缺省的ISP域进行认证。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：ISP域名称，为1～255个字符的字符串，不区分大小写，不能包括"/"、"\"、"[\|]"、"""、":"、"\*"、"?"、"\<"、"\>"以及"@"字符，且不能为字符串"d"、"de"、"def"、"defa"、"defau"、"defaul"、"default"、"i"、"if"、"if-"、"if-u"、"if-un"、"if-unk"、"if-unkn"、"if-unkno"、"if-unknow"和"if-unknown"。

【使用指导】

SSL VPN用户的用户名中不能携带所属ISP域信息。配置本命令后，SSL VPN用户将采用指定ISP域内的认证、授权、计费方案对SSL VPN用户进行认证、授权和计费。

【举例】

\# 配置SSL VPN访问实例使用ISP域myserver进行AAA认证。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 aaa domain myserver

**SSL VPN \-- SSL VPN配置命令 \-- bandwidth**

------------------------------------------------------------------------

![说明](SSL%20VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽为64kbps。

【视图】

SSL VPN AC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：接口的期望带宽，取值范围为1～400000000，单位为kbps。

【使用指导】

接口的期望带宽会对下列内容有影响：

·CBQ队列带宽。具体介绍请参见"ACL和QoS配置指导"中的"[拥塞管理"。]

·链路开销值。具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置接口SSL VPN AC 1000的期望带宽为10000kbps。

\<Sysname\> system-view

Sysname interface sslvpn-ac 1000

Sysname-SSLVPN-AC1000 bandwidth 10000

**SSL VPN \-- SSL VPN配置命令 \-- certificate-authentication enable**

------------------------------------------------------------------------

**[certificate-authentication enable**]命令用来开启证书认证功能。

**[undo certificate-authentication enable**]命令用来关闭证书认证功能。

【命令】

**[certificate-authentication** **enable**]

**[undo certificate-authentication enable**]

【缺省情况】

证书认证功能处于关闭状态。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启证书认证功能后，需要同时在SSL服务器端策略视图下执行**client-verify enable**命令。SSL VPN网关会对SSL客户端（SSL VPN用户）进行基于数字证书的身份验证，并检查SSL VPN用户的用户名是否与SSL VPN用户的数字证书中的用户名信息一致。若不一致，则认证不通过，不允许SSL VPN用户登录。

【举例】

\# 开启SSL VPN访问实例的证书认证功能。

\<Sysname\> system-view

Sysname sslvpn context ctx

Sysname-sslvpn-context-ctx certificate-authencation enable

【相关命令】

·**client-verify enable**（安全命令参考/SSL）

**SSL VPN \-- SSL VPN配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

SSL VPN AC接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将接口SSL VPN AC 1000恢复为缺省配置。

\<Sysname\> system-view

Sysname interface sslvpn-ac 1000

Sysname-SSLVPN-AC1000 default

This command will restore the default settings. Continue? [Y/N:y]

**SSL VPN \-- SSL VPN配置命令 \-- default-policy-group**

------------------------------------------------------------------------

**[default-policy-group**]命令用来指定某个策略组为缺省策略组。

**[undo default-policy-group**]命令用来取消缺省策略组。

【命令】

**[default-policy-group ***group-name*]

**[undo default-policy-group**]

【缺省情况】

没有指定缺省策略组。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：策略组名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。

【使用指导】

一个SSL VPN访问实例下可以配置多个策略组。远端接入用户访问SSL VPN访问实例时，AAA服务器将授权给该用户的策略组信息下发给SSL VPN网关。该用户可以访问的资源由授权的策略组决定。如果AAA服务器没有为该用户进行授权，则用户可以访问的资源由缺省策略组决定。

本命令中指定的策略组必须为已经通过**policy-group**命令创建的策略组。

【举例】

\# 指定名为pg1的策略组为缺省策略组。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 policy group pg1

Sysname-sslvpn-context-ctx1-policy-group-pg1 quit

Sysname-sslvpn-context-ctx1 default-policy-group pg1

【相关命令】

·**display sslvpn context**

·**policy-group**

**SSL VPN \-- SSL VPN配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，例如：SSLVPN-AC1000 Interface。

【视图】

SSL VPN AC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口的描述字符串，为1～255个字符的字符串，区分大小写。

【使用指导】

当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。

本命令仅用于标识某接口，并无特别的功能。使用**display interface**等命令可以看到设置的描述信息。

【举例】

\# 配置接口SSL VPN AC 1000的描述信息为"SSL VPN A"。

\<Sysname\> system-view

Sysname interface sslvpn-ac 1000

Sysname-SSLVPN-AC1000 description SSL VPN A

**SSL VPN \-- SSL VPN配置命令 \-- display interface sslvpn-ac**

------------------------------------------------------------------------

**[display interface **]**sslvpn-ac**命令用来显示SSL VPN AC接口的相关信息。

【命令】

**[display interface** **sslvpn-ac** [ *interface-number*    **brief** [ **description** \| **down** ] ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：SSL VPN AC接口的编号，取值范围为0～4095。

**[brief**]：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定接口类型**sslvpn-ac**，将显示设备支持的所有接口的相关信息。

·如果指定接口类型，不指定接口编号*interface-number*，则显示所有SSL VPN AC接口的信息。

·如果同时指定接口类型和接口编号，则显示指定SSL VPN AC接口的信息。

【举例】

\# 显示接口SSL VPN AC 1000的相关信息。

\<Sysname\> display interface sslvpn-ac 1000

SSLVPN-AC1000

Current state: UP

Line protocol state: DOWN

Description: SSLVPN-AC1000 Interface

Bandwidth: 64kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

Link layer protocol is SSLVPN

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

表1-1 display interface命令显示信息描述表

字段

描述

SSLVPN-AC1000

接口SSL VPN AC 1000的相关信息

Current state

接口的物理状态和管理状态，取值包括：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态，取值包括：

·UP：表示该接口的链路层协议状态为开启

·UP (spoofing)：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常NULL、LoopBack等接口会具有该属性

·DOWN：表示该接口的链路层协议状态为关闭

Description

接口的描述信息

Bandwidth

接口的期望带宽，单位为kbps

Maximum Transmit Unit

接口的最大传输单元

Internet protocol processing

接口的IP地址。如果没有为接口配置IP地址，则该字段显示为Internet protocol processing: disabled，表示不能处理IP报文

Primary表示该IP地址为接口的主IP地址

Link layer protocol

链路层协议类型

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间（如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never）

Last 300 seconds input rate

最近300秒钟的平均输入速率：bytes/sec表示平均每秒输入的字节数，bits/sec表示平均每秒输入的比特数，packets/sec表示平均每秒输入的包数

Last 300 seconds output rate

最近300秒钟的平均输出速率：bytes/sec表示平均每秒输出的字节数，bits/sec表示平均每秒输出的比特数，packets/sec表示平均每秒输出的包数

Input: 0 packets, 0 bytes, 0 drops

总计输入的报文数，总计输入的字节，总计丢弃的输入报文数

Output: 0 packets, 0 bytes, 0 drops

总计输出的报文数，总计输出的字节，总计丢弃的输出报文数

\# 显示所有SSL VPN AC类型接口的概要信息。

\<Sysname\> display interface sslvpn-ac brief

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

SSLVPN-AC1000        DOWN DOWN     \--

\# 显示接口SSL VPN AC 1000的概要信息，包括用户配置的全部描述信息。

\<Sysname\> display interface sslvpn-ac 1000 brief description

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

SSLVPN-AC1000        UP    UP      1.1.1.1         SSLVPN-AC1000 Interface

\# 显示当前状态为down的接口的信息以及DOWN的原因。

\<Sysname\> display interface brief down

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

SSLVPN-AC1000        DOWN Administratively

SSLVPN-AC1001        DOWN Administratively

表1-2 display interface brief命令显示信息描述表

字段

描述

Brief information of interface(s) under route mode:

三层模式下（route）的接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"字符串，则表示该接口的网络层协议状态显示是UP的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立

Interface

接口名称缩写

Link

接口物理连接状态，取值包括：

·UP：表示本链路物理上是连通的

·DOWN：表示本链路物理上是不通的

·ADM：表示本链路被手工关闭了，需要执行**undo shutdown**命令才能恢复真实的物理状态

·Stby：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准

Protocol

接口的链路层协议状态，取值包括：

·UP：表示该接口的链路层协议状态为开启

·UP (s)：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常NULL、LoopBack等接口会具有该属性

·DOWN：表示该接口的链路层协议状态为关闭

Main IP

接口主IP地址

Description

接口的描述信息

Cause

接口物理连接状态为down的原因，取值为：

·Administratively：表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

·Not connected：表示物理层不通

【相关命令】

·**reset counters interface**

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn context**

------------------------------------------------------------------------

**[display sslvpn context**]命令用来显示SSL VPN访问实例的信息。

【命令】

**[display sslvpn context **[[ **brief** \| **name** *context-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[brief**]：显示所有SSL VPN访问实例的简要信息。如果不指定本参数，则显示SSL VPN访问实例的详细信息。

**[name** *context-name*]：显示指定SSL VPN访问实例的详细信息。*context-name*表示SSL VPN访问实例名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有SSL VPN访问实例的信息。

【举例】

\# 显示所有SSL VPN访问实例的详细信息。

\<Sysname\> display sslvpn context

Context name: ctx1

  Operation status: Down

  Down reason: Administratively down

  AAA domain: domain1

  Certificate authentication: Enabled

  Dynamic password: Enabled

  Verify code validation: Enabled

  Default policy group not configured

  Domain name and virtual host not configured

  Maximum users allowed: 200

  VPN-instance：vpn1

Context name: ctx2

  Operation status: Up

  AAA domain not specified

  Certificate authentication: Disabled

  Dynamic password: Disabled

  Verify code validation: Disabled

  Default group policy: gp

  Associated SSL VPN gateway: gw2

  Virtual host: abc.com

  Maximum users allowed: 200

  VPN-instance not configured

表1-3 display sslvpn context命令显示信息描述表

字段

描述

Context name

SSL VPN访问实例的名称

Operation status

SSL VPN访问实例的操作状态，取值包括：

·Up：SSL VPN访问实例处于运行状态

·Down：SSL VPN访问实例未处于运行状态

Down reason

SSL VPN访问实例处于down状态的原因，取值包括：

·Administratively down：管理down，即未通过**service enable**命令开启SSL VPN访问实例

·No gateway associated：SSL VPN访问实例未引用SSL VPN网关

AAA domain

SSL VPN访问实例使用的ISP域

Certificate authentication

SSL VPN访问实例是否开启证书认证功能

Dynamic password

SSL VPN访问实例是否开启动态口令验证功能

Verify code validation

SSL VPN访问实例是否开启验证码验证功能

Default policy group

SSL VPN访问实例使用的缺省策略组

Associated SSL VPN gateway

SSL VPN访问实例引用的SSL VPN网关

Domain name

SSL VPN访问实例的域名

Virtual host

SSL VPN访问实例的虚拟主机名称

Maximum users allowed

SSL VPN访问实例的最大用户会话数

VPN-instance

SSL VPN访问实例关联的VPN实例

\# 显示所有SSL VPN访问实例的简要信息。

\<Sysname\> display sslvpn context brief

Context name      Gateway       Domain/VHost      VRF       Admin  Operation

ctx1              -             -                 -         Down   Down

ctx2              gw2           abc.com           -         Up     Up

表1-4 display sslvpn context brief命令显示信息描述表

字段

描述

Context name

SSL VPN访问实例的名称

Gateway

SSL VPN访问实例引用的SSL VPN网关

Domain/VHost

SSL VPN访问实例的域名或虚拟主机名称

VRF

SSL VPN访问实例关联的VPN实例

Admin

SSL VPN访问实例的管理状态，取值包括：

·up：已通过**service enable**命令开启SSL VPN访问实例

·down：未通过**service enable**命令开启SSL VPN 访问实例

Operation

SSL VPN访问实例的操作状态，取值包括：

·up：SSL VPN访问实例处于运行状态

·down：SSL VPN访问实例未处于运行状态

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn gateway**

------------------------------------------------------------------------

**[display sslvpn gateway**]命令用来显示SSL VPN网关的信息。

【命令】

**[display sslvpn gateway **[[ **brief** \| **name** *gateway-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[brief**]：显示所有SSL VPN网关的简要信息。如果不指定本参数，则显示SSL VPN网关的详细信息。

**[name** *gateway-name*]：显示指定SSL VPN网关的详细信息。*gateway-name*表示SSL VPN网关名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有SSL VPN网关的信息。

【举例】

\# 显示所有SSL VPN网关的详细信息。

\<Sysname\> display sslvpn gateway

Gateway name: gw1

  Operation status: Up

  IP: 192.168.10.75, port: 443

  HTTP redirect port: 80

  SSL server-policy: ssl

  Front VPN-instance: vpn1

Gateway name: gw2

  Operation status: Down

  Down reason: Administratively down

  Gateway IP address not configured

  SSL server-policy: ssl1

  Front VPN-instance not configured

表1-5 display sslvpn gateway命令显示信息描述表

字段

描述

Gateway name

SSL VPN网关的名称

Operation status

SSL VPN网关的操作状态，取值包括：

·Up：SSL VPN网关处于运行状态

·Down：SSL VPN网关未处于运行状态

Down reason

SSL VPN网关处于down状态的原因，取值包括：

·Administratively down：管理down，即没有通过**service enable**命令开启SSL VPN网关

·No gateway IP：未配置SSL VPN网关的IP地址

·VPN instance not exist：SSL VPN网关所属的VPN实例不存在

·Applying SSL server-policy failed：为SSL VPN网关应用SSL服务器端策略失败

IP

SSL VPN网关的IP地址

port

SSL VPN网关的端口号

HTTP redirect port

HTTP重定向端口号

SSL server-policy

SSL VPN网关引用的SSL服务器端策略名称

Front VPN-instance

前端VPN实例名称，即SSL VPN网关所属的VPN实例名称

\# 显示所有SSL VPN网关的简要信息。

\<Sysname\> display sslvpn gateway brief

Gateway name                    Admin  Operation

gw1                             Up     Up

gw2                             Down   Down (Administratively down)

表1-6 display sslvpn gateway brief命令显示信息描述表

字段

描述

Gateway name

SSL VPN网关的名称

Admin

SSL VPN网关的管理状态，取值包括：

·Up：已通过**service enable**命令开启SSL VPN网关

·Down：未通过**service enable**命令开启SSL VPN网关

Operation

SSL VPN网关的操作状态，取值包括：

·Up：SSL VPN网关处于运行状态

·Down：SSL VPN网关未处于运行状态

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn policy-group**

------------------------------------------------------------------------

**[display sslvpn policy-group**]命令用来显示指定策略组的信息。

【命令】

**[display sslvpn policy-group ***group-name * **context** *context-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-name*]：策略组名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。

**[context ***context-name*]：显示指定SSL VPN访问实例下的指定策略组的信息。*context-name*表示SSL VPN访问实例的名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有SSL VPN访问实例下的指定名称的策略组信息。

【举例】

\# 显示所有SSL VPN访问实例下名称为pg1的策略组的信息。

\<Sysname\> display sslvpn policy-group pg1

Group policy: pg1

  Context: context1

   Idle timeout: 2100 sec

  Context: context2

   Idle timeout: 4000 sec

表1-7 display sslvpn policy-group命令显示信息描述表

字段

描述

Group policy

策略组名称

Context

SSL VPN访问实例名称

Idle timeout

SSL VPN会话可以保持空闲状态的最长时间，单位为秒

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn port-forward connection**

------------------------------------------------------------------------

**[display sslvpn port-forward connection**]命令用来显示TCP端口转发的连接信息。

【命令】

**[display sslvpn port-forward connection** [ **context** *context-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[context ***context-name*]：显示指定SSL VPN访问实例下的TCP端口转发连接信息。*context-name*表示SSL VPN访问实例名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有SSL VPN访问实例下的TCP端口转发连接信息。

【举例】

\# 显示名为ctx1的SSL VPN访问实例下TCP端口转发的连接信息。

\<Sysname\> display sslvpn port-forward connection context ctx1

SSL VPN context: ctx1

Client IP   Client port      Server IP       Server port  Status

192.0.2.1   1025             192.168.0.39    80           Connected

192.0.2.2   1026             192.168.0.35    23           Connecting

\# 显示所有SSL VPN访问实例下TCP端口转发的连接信息。

\<Sysname\> display sslvpn port-forward connection

SSL VPN context: ctx1

Client IP   Client port      Server IP       Server port  Status

192.0.2.1   1025             192.168.0.39    80           Connected

192.0.2.2   1026             192.168.0.35    23           Connecting

SSL VPN context: ctx2

Client IP   Client port      Server IP       Server port  Status

192.0.2.3   1025             192.168.0.39    80           Connected

192.0.2.4   1026             192.168.0.35    23           Connected

表1-8 display sslvpn port-forward connection命令显示信息描述表

字段

描述

Client IP

SSL VPN客户端的IP地址

Client port

SSL VPN客户端的本地端口号

Server IP

企业网内服务器的IP地址

Server port

企业网内服务器的端口号

Status

连接状态，取值包括：

·Connected：连接成功

·Connecting：正在连接

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn session**

------------------------------------------------------------------------

**[display sslvpn session**]命令用来显示SSL VPN会话信息。

【命令】

**[display sslvpn session** [ **context** *context-name*   **user** *user-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[context ***context-name*]：显示指定SSL VPN访问实例下的SSL VPN会话信息。*context-name*表示SSL VPN访问实例名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有SSL VPN访问实例下的SSL VPN会话信息。

**[user ***user-name*]：显示指定SSL VPN用户对应的SSL VPN会话的详细信息。*user-name*表示SSL VPN用户名称，为1～31个字符的字符串，不区分大小写。如果不指定本参数，则显示指定或所有SSL VPN访问实例下SSL VPN会话的简要信息。

【举例】

\# 显示名为ctx1的SSL VPN访问实例下SSL VPN会话的简要信息。

\<Sysname\> display sslvpn session context ctx1

SSL VPN context: ctx1

Login name  User IP address Connections Created  Idle time

user1       192.0.2.1       2           04:47:16 00:01:26

user2       192.0.2.2       2           04:48:36 00:01:56

表1-9 display sslvpn session命令简要显示信息描述表

字段

描述

SSL VPN context

SSL VPN访问实例名称

Login name

SSL VPN会话的登录用户名称

User IP address

SSL VPN会话使用的IP地址

Connections

SSL VPN会话对应的连接数目

Created

SSL VPN会话的创建时间

Idle time

SSL VPN会话的空闲时间

\# 显示SSL VPN用户user1对应的SSL VPN会话的详细信息。

\<Sysname\> display sslvpn session user user1

User        : user1

Context     : context1

Policy group: Default

Connections : 1                 User IP address: 192.168.56.1

Idle time   : 00:00:02          Created        : 13:49:27 UTC Wed 05/14/2014

Idle timeout: 2100 sec

表1-10 display sslvpn session命令详细显示信息描述表

字段

描述

User

SSL VPN用户的名称

Context

SSL VPN用户所属的SSL VPN访问实例

Policy group

SSL VPN用户使用的策略组

Connections

SSL VPN会话对应的连接数目

User IP Address

SSL VPN会话使用的IP地址

Idle time

SSL VPN会话的空闲时间

Created

SSL VPN会话的创建时间

Idle timeout

SSL VPN会话保持空闲状态的最长时间，单位为秒

**SSL VPN \-- SSL VPN配置命令 \-- dynamic-password enable**

------------------------------------------------------------------------

**[dynamic-password enable**]命令用来开启动态口令验证功能。

**[undo dynamic-password enable**]命令用来关闭动态口令验证功能。

【命令】

**[dynamic-password** **enable**]

**[undo dynamic-password enable**]

【缺省情况】

动态口令验证功能处于关闭状态。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启动态口令验证功能后，用户登录SSL VPN页面时，需要输入动态口令进行验证。

【举例】

\# 开启动态口令验证功能。

\<Sysname\> system-view

Sysname sslvpn context ctx

Sysname-sslvpn-context-ctx dynamic-password enable

**SSL VPN \-- SSL VPN配置命令 \-- emo-server**

------------------------------------------------------------------------

**[emo-server**]命令用来配置为客户端指定的EMO（Endpoint Mobile Office，终端移动办公）服务器。

**[undo emo-server**]命令用来恢复缺省情况。

【命令】

**[emo-server **[{ **host-name** *host-name* \| **ip** *ip-address* } **port** *port-number* ]]

**[undo emo-server**]

【缺省情况】

没有配置为客户端指定的EMO服务器。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[host-name*** host-name*]：指定EMO服务器的主机名。*host-name*为1～127个字符的字符串，可以包含字母、数字、下划线、"-"和"."，不区分大小写。

**[ip ***ip-address*]：指定EMO服务器的IPv4地址。*ip-address*为点分十进制格式，不能是组播、广播、环回地址。

**[port ***port-number*]：指定EMO服务器使用的端口号。*port-number*取值范围为1025～65535。

【使用指导】

EMO服务器用来为移动客户端提供服务。执行本命令后，SSL VPN网关会将配置的EMO服务器信息下发给客户端，以便客户端访问EMO服务器。

在同一个SSL VPN访问实例视图下，重复执行本命令，则新的配置会覆盖已有的配置。

【举例】

\# 在名为ctx1的SSL VPN访问实例下配置EMO服务器地址为10.10.1.1、端口号为8000。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 emo-server ip 10.10.1.1 port 8000

**SSL VPN \-- SSL VPN配置命令 \-- filter ip-tunnel**

------------------------------------------------------------------------

**[filter ip-tunnel**]命令用来配置对IP接入进行过滤。

**[undo filter ip-tunnel**]命令用来恢复缺省情况。

【命令】

**[filter ip-tunnel** *advanced-acl-number*]

**[undo filter ip-tunnel**]

【缺省情况】

不会对IP接入进行过滤，允许所有IP接入报文通过。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[advance-acl-number*]：用来过滤IP接入报文的高级ACL的编号，取值范围为3000～3999。

【使用指导】

执行本命令后，如果SSL VPN客户端使用IP接入方式访问SSL VPN网关，则只有通过ACL检查的报文才可以访问IP资源。

如果引用的ACL不存在，则SSL VPN网关拒绝所有IP接入方式的访问。

在SSL VPN策略组视图下重复执行本命令，则新的配置会覆盖已有配置。

【举例】

\# 配置策略组pg1通过ACL 3000过滤IP接入方式访问。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 policy group pg1

Sysname-sslvpn-context-ctx1-policy-group-pg1 filter ip-tunnel 3000

**SSL VPN \-- SSL VPN配置命令 \-- filter tcp-access**

------------------------------------------------------------------------

**[filter tcp-access**]命令用来配置对TCP接入进行过滤。

**[undo filter tcp-access**]命令用来恢复缺省情况。

【命令】

**[filter tcp-access** *advanced-acl-number*]

**[undo filter tcp-access**]

【缺省情况】

不会对TCP接入进行过滤，允许所有客户端访问TCP接入服务。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[advanced-acl-number*]：用来过滤TCP接入的高级ACL的编号，取值范围为3000～3999。

【使用指导】

执行本命令后，如果SSL VPN客户端访问TCP接入服务，则只有SSL VPN客户端发送的报文通过了ACL检查，才允许其访问TCP接入服务。

如果引用的ACL不存在，则SSL VPN网关拒绝所有SSL VPN客户端访问TCP应用。

在SSL VPN策略组视图下重复执行本命令，则新的配置会覆盖已有配置。

【举例】

\# 配置策略组pg1通过ACL 3000过滤TCP接入。

\<Sysname\> system-view

Sysnamesslvpn context ctx1

Sysname-sslvpn-context-ctx1 policy-group pg1

Sysname-sslvpn-context-ctx1 filter tcp-access 3000

**SSL VPN \-- SSL VPN配置命令 \-- filter web-access**

------------------------------------------------------------------------

**[filter web-access**]命令用来配置对Web接入进行过滤。

**[undo filter web-access**]命令用来恢复缺省情况。

【命令】

**[filter web-access** *advanced-acl-number*]

**[undo filter web-access**]

【缺省情况】

不会对Web接入进行过滤，允许所有客户端访问Web接入资源。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[advanced-acl-number*]：用来过滤Web接入的高级ACL的编号，取值范围为3000～3999。

【使用指导】

执行本命令后，如果SSL VPN客户端访问Web资源，则只有SSL VPN客户端发送的报文通过了ACL检查，才允许其访问Web资源。

如果引用的ACL不存在，则SSL VPN网关拒绝所有SSL VPN客户端访问Web资源。

在SSL VPN策略组视图下重复执行本命令，则新的配置会覆盖已有配置。

【举例】

\# 配置策略组pg1通过ACL 3000过滤Web接入。

\<Sysname\> system-view

Sysnamesslvpn context ctx1

Sysname-sslvpn-context-ctx1 policy-group pg1

Sysname-sslvpn-context-ctx1 filter web-access 3000

**SSL VPN \-- SSL VPN配置命令 \-- gateway**

------------------------------------------------------------------------

**[gateway**]命令用来配置SSL VPN访问实例引用SSL VPN网关。

**[undo gateway**]命令用来取消SSL VPN访问实例引用SSL VPN网关。

【命令】

**[gateway ***gateway-name *[[ **domain** *domain-name* \| **virtual-host** *virtual-host-name* ]]]

**[undo gateway**]

【缺省情况】

SSL VPN访问实例没有引用SSL VPN网关。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[gateway-name*]：SSL VPN网关名称。为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。

**[domain ***domain-name*]：域名，为1～127个字符的字符串，只能包含字母、数字、下划线、"-"，不区分大小写。

**[virtual-host ***virtual-host-name*]：虚拟主机名称，为1～127个字符的字符串，只能包含字母、数字、下划线、"-"和"."，不区分大小写。

【使用指导】

多个SSL VPN访问实例引用同一个SSL VPN网关时，可以通过以下方法判断远端接入用户所属的SSL VPN访问实例：

·为不同的SSL VPN访问实例指定不同的域名。远端用户登录SSL VPN网关时，指定自己所在的域，SSL VPN网关根据用户指定的域判断该用户所属的SSL VPN访问实例。

·为不同的SSL VPN访问实例指定不同的虚拟主机名称。远端用户访问SSL VPN网关时，输入虚拟主机名称，SSL VPN网关根据虚拟主机名称判断该用户所属的SSL VPN访问实例。

需要注意的是：

·如果SSL VPN访问实例引用SSL VPN网关时没有指定域名和虚拟主机名称，那么其他的SSL VPN访问实例就不能再引用该SSL VPN网关。

·在同一个SSL VPN访问实例视图下，重复配置本命令，则新的配置会覆盖已有配置。

【举例】

\# 配置名为ctx1的SSL VPN访问实例引用SSL VPN网关gw1，域名为domain1、虚拟主机名称为abc.com。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 gateway gw1 domain domain1

Sysname-sslvpn-context-ctx1 gateway gw1 virtual-host abc.com

【相关命令】

·**display sslvpn context**

**SSL VPN \-- SSL VPN配置命令 \-- http-redirect**

------------------------------------------------------------------------

**[http-redirect**]命令用来开启HTTP流量的重定向功能。

**[undo http-redirect**]命令用来恢复缺省情况。

【命令】

**[http-redirect ** **port** *port-number* ]

**[undo http-redirect**]

【缺省情况】

未开启HTTP流量的重定向功能，SSL VPN网关不会处理HTTP流量。

【视图】

SSL VPN网关视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：需要重定向的HTTP流量的端口号，取值范围为80、1025～65535，缺省值为80。

【使用指导】

配置该命令后，SSL VPN网关将监听指定的端口号，并把指定端口号的HTTP流量重定向到HTTPS的443端口，向客户端发送重定向报文，让客户端重新以HTTPS方式登录。

【举例】

\# 为端口号为1025的HTTP流量开启重定向功能。

\<Sysname\> system-view

Sysname sslvpn gateway gateway1

Sysname-sslvpn-gateway-gateway1 http-redirect port 1025

**SSL VPN \-- SSL VPN配置命令 \-- include**

------------------------------------------------------------------------

**[include**]命令用来在路由列表中添加路由。

**[undo include**]命令用来删除路由列表中的路由。

【命令】

**[include**[ *ip-address* { *mask-length \| mask* }]]

**[undo include**[ *ip-address* { *mask-length \| mask* }]]

【缺省情况】

路由列表中不存在任何路由。

【视图】

路由列表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：路由的目的地址，不能是组播、广播、环回地址。

*[mask-length*]：路由的掩码长度，取值范围为0～32。

*[mask*]：路由的掩码。

【使用指导】

本命令指定的目的网段需要是企业内部服务器所在的网络。策略组引用路由列表后，SSL VPN网关将路由列表中的路由表项下发给客户端。客户端在本地添加这些路由表项，以便客户端将访问企业网络内部服务器的报文通过虚拟网卡发送给SSL VPN网关，防止这些报文进入Internet。

在路由列表视图下，通过重复执行本命令，可以在该路由列表中添加多条路由。

【举例】

\# 在路由列表rtlist下添加路由10.0.0.0/8。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 ip-route-list rtlist

Sysname-sslvpn-context-ctx1-route-list-rtlist include 10.0.0.0 8

**SSL VPN \-- SSL VPN配置命令 \-- interface sslvpn-ac**

------------------------------------------------------------------------

**[interface sslvpn-ac**]命令用来创建SSL VPN AC接口，并进入SSL VPN AC接口视图。

**[undo interface sslvpn-ac**]命令用来删除指定的SSL VPN AC接口。

【命令】

**[interface sslvpn-ac ***interface-number*]

**[undo interface sslvpn-ac ***interface--number*]

【缺省情况】

设备上不存在任何SSL VPN AC接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：SSL VPN AC接口的编号，取值范围为0～4095。

【举例】

\# 创建SSL VPN AC接口1000，并进入SSL VPN AC接口视图。

\<Sysname\>system-view

Sysnameinterface SSLVPN-AC 1000

Sysname-SSLVPN-AC1000

**SSL VPN \-- SSL VPN配置命令 \-- ip address (SSL VPN gateway view)**

------------------------------------------------------------------------

**[ip address**]命令用来配置SSL VPN网关的IP地址和端口号。

**[undo ip address**]命令用来删除SSL VPN网关的IP地址和端口号。

【命令】

**[ip address ***ip-address* **port** *port-number* ]

**[undo ip address**]

【缺省情况】

没有指定SSL VPN网关的IP地址和端口号。

【视图】

SSL VPN网关视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：SSL VPN网关的IPv4地址，为点分十进制格式。

**[port ***port-number*]：指定SSL VPN网关的端口号。*port-number*取值范围为443、1025～65535，缺省值为443。

【使用指导】

远端接入用户可以通过本命令配置的IP地址和端口号访问SSL VPN网关。本命令指定的IP地址应为SSL VPN网关上接口的IP地址，并需要保证该IP地址路由可达。

在同一个SSL VPN网关视图下，重复执行**ip address**命令，则新的配置会覆盖已有配置。

【举例】

\# 配置SSL VPN网关的IP地址为10.10.1.1、端口号为8000。

\<Sysname\> system-view

Sysname sslvpn gateway gw1

Sysname-sslvpn-gateway-gw1 ip address 10.10.1.1 port 8000

【相关命令】

·**display sslvpn gateway**

**SSL VPN \-- SSL VPN配置命令 \-- ip-route-list**

------------------------------------------------------------------------

**[ip-route-list**]命令用来创建路由列表，并进入路由列表视图。

**[undo ip-route-list**]命令用来删除指定的路由列表。

【命令】

**[ip-route-list** *list-name*]

**[undo ip-route-list ***list-name*]

【缺省情况】

设备上不存在任何路由列表。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[list-name*]：路由列表名称，为1～31个字符的字符串，由字母、数字、下划线组成，不区分大小写。

【使用指导】

在路由列表视图下，通过**include**命令可以添加路由表项，路由表项的目的网段为企业内部服务器所在的网段。策略组引用路由列表后，SSL VPN网关将路由列表中的路由表项下发给客户端，客户端在本地添加这些路由表项，路由表项的出接口为客户端的虚拟网卡，以便客户端通过这些路由表项访问企业网络内部的服务器。

需要注意的是，若路由列表被策略组引用，则不允许删除该路由列表。

【举例】

\# 在名为ctx1的SSL VPN访问实例下，创建路由列表rtlist，并进入路由列表视图。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 ip-route-list rtlist

Sysname-sslvpn-context-ctx1-route-list-rtlist

【相关命令】

·**ip-tunnel access-route**

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel access-route**

------------------------------------------------------------------------

**[ip-tunnel access-route**]命令用来配置下发给客户端的路由表项。

**[undo ip-tunnel access-route**]命令用来取消下发给客户端的路由表项。

【命令】

**[ip-tunnel access-route **[{ *ip-address* { *mask-length \| mask* } \| **force-all** \| **ip-route-list** *list-name* }]]

**[undo ip-tunnel access-route**]

【缺省情况】

未指定下发给客户端的路由表项。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*****[{ *mask-length \| mask* }]]：将指定路由下发给客户端。*ip-address*为路由的目的地址，不能是组播、广播、环回地址；*mask-length*为路由的掩码长度，取值范围为0～32；*mask*为路由的掩码。

**[force-all**]：强制将客户端的流量转发给SSL VPN网关。

**[ip-route-list*** list-name*]：将指定路由列表中的路由表项下发给客户端。*list-name*表示路由列表名称，为1～31个字符的字符串，由字母、数字、下划线组成，不区分大小写。

【使用指导】

客户端通过IP接入方式访问网关时，网关将指定的路由下发给客户端。客户端若访问该网段内的服务器，报文就会通过虚拟网卡发送给SSL VPN网关，防止报文进入Internet。

本命令中指定的路由列表必须先通过**ip-route-list**命令创建。通过指定路由列表，可以同时将路由列表中的多条路由下发给客户端。若只需要为客户端下发一条路由，则可以直接配置*ip-address*****[{ *mask-length \| mask* }]参数，无需指定路由列表。

执行本命令时如果指定了**force-all**参数，则SSL VPN网关将在客户端上添加优先级最高的缺省路由，路由的出接口为虚拟网卡，从而使得所有没有匹配到路由表项的流量都通过虚拟网卡发送给SSL VPN网关。SSL VPN网关还会实时监控SSL VPN客户端，不允许SSL VPN客户端删除此缺省路由，且不允许SSL VPN客户端添加优先级高于此路由的缺省路由。

若重复执行本命令，则新的配置会覆盖已有的配置。

【举例】

\# 在策略组pg1下，配置将路由列表rtlist中的路由下发给客户端。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 ip-route-list rtlist

Sysname-sslvpn-context-ctx1-route-list-rtlist include 10.0.0.0 8

Sysname-sslvpn-context-ctx1-route-list-rtlist include 20.0.0.0 8

Sysname-sslvpn-context-ctx1-route-list-rtlist quit

Sysname-sslvpn-context-ctx1 policy group pg1

Sysname-sslvpn-context-ctx1-policy-group-pg1 ip-tunnel access-route ip-route-list rtlist

【相关命令】

·**ip-route-list**

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel address-pool**

------------------------------------------------------------------------

**[ip-tunnel address-pool**]命令用来配置IP接入引用地址池。

**[undo ip-tunnel address-pool**]命令用来取消IP接入引用地址池。

【命令】

**[ip-tunnel address-pool ***pool-name*[ **mask** { *mask-length \| mask* }]]

**[undo ip-tunnel address-pool**]

【缺省情况】

IP接入未引用地址池。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pool-name*]：引用的地址池名称，为1～31个字符的字符串，由字母、数字、下划线组成，不区分大小写。

**[mask **[{ *mask-length \| mask* }]]：指定地址池的掩码或掩码长度。*mask-length*表示地址池的掩码长度，取值范围为1～30；*mask*表示地址池的掩码。

【使用指导】

客户端使用IP接入方式访问SSL VPN网关时，网关需要为客户端分配IP地址。本命令指定了分配的地址所属的地址池，即从地址池中选取地址分配给客户端。本命令还可以指定分配的地址的掩码或掩码长度。

需要注意的是：

·本命令可以引用不存在的地址池。但此时SSL VPN网关无法为客户端分配IP地址。只有创建地址池后，SSL VPN网关才可以为客户端分配IP地址。

·每个SSL VPN策略组视图下只能引用一个地址池。若重复执行本命令，则新的配置会覆盖已有配置。

【举例】

\# 配置IP接入引用地址池pool1。

\<Sysname\> system-view

Sysname sslvpn context ctx

Sysname-sslvpn-context-ctx policy-group pgroup

Sysname-sslvpn-context-ctx-policy-group-pgroup ip-tunnel address-pool pool mask 24

【相关命令】

·**sslvpn ip address-pool**

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel dns-server**

------------------------------------------------------------------------

**[ip-tunnel dns-server**]命令用来配置为客户端指定的内网DNS服务器地址。

**[undo ip-tunnel dns-server**]命令用来恢复缺省情况。

【命令】

**[ip-tunnel dns-server **[{ **primary** \| **secondary** } *ip-address*]]

**[undo ip-tunnel dns-server **[{ **primary** \| **secondary** }]]

【缺省情况】

没有配置为客户端指定的DNS服务器地址。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[primary**]：指定主DNS服务器。

**[secondary**]：指定备DNS服务器。

*[ip-address*]：DNS服务器的IPv4地址，不能是组播、广播、环回地址。

【举例】

\# 配置为客户端指定的主DNS服务器地址为1.1.1.1。

\<Sysname\> system-view

Sysname sslvpn context ctx

Sysname-sslvpn-context-ctx policy-group pgroup

Sysname-sslvpn-context-ctx-policy-group-pgroup ip-tunnel dns-server primary 1.1.1.1

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel interface**

------------------------------------------------------------------------

**[ip-tunnel interface**]命令用来配置IP接入引用的SSL VPN AC接口。

**[undo ip-tunnel interface**]命令用来取消IP接入引用SSL VPN AC接口。

【命令】

**[ip-tunnel interface sslvpn-ac** *interface-number*]

**[undo ip-tunnel interface**]

【缺省情况】

IP接入未引用SSL VPN AC接口。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sslvpn-ac** *interface-number*]：引用的SSL VPN AC接口。*interface-number*为SSL VPN AC接口编号，取值范围为设备上已创建的SSL VPN AC接口的编号。

【使用指导】

当SSL VPN用户使用IP接入方式访问SSL VPN网关时，网关使用指定的SSL VPN AC接口与客户端通信。网关从SSL VPN AC接口接收到客户端发送的报文后，将报文转发到远端服务器；服务器做出响应后，网关会把应答报文通过SSL VPN AC接口发给客户端。

指定的SSL VPN AC接口必须已经通过**interface sslvpn-ac**命令创建。

【举例】

\# 指定IP接入引用的接口为SSL VPN AC 100。

\<Sysname\> system-view

Sysname sslvpn context ctx

Sysname-sslvpn-context-ctx ip-tunnel interface sslvpn-ac 100

【相关命令】

·**interface sslvpn-ac**

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel keepalive**

------------------------------------------------------------------------

**[ip-tunnel keepalive**]命令用来配置保活报文的发送时间间隔。

**[undo ip-tunnel keepalive**]命令用来恢复缺省情况。

【命令】

**[ip-tunnel keepalive ***seconds*]

**[undo ip-tunnel keepalive**]

【缺省情况】

保活报文的发送时间间隔为30秒。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：保活报文的发送间隔时间，取值范围为0～600，单位为秒。

【使用指导】

保活报文由客户端发送给网关，用于维持客户端和网关之间的会话。如果保活报文发送时间间隔配置为0，则客户端不会发送保活报文。

如果SSL VPN会话的空闲时间超过**timeout idle**命令指定的时间，即在该命令指定的时间内，既没有收到客户端发送的数据报文，也没有收到保活报文，则会断开客户端与网关之间的会话。

通常情况下，配置的保活报文发送时间间隔应该小于**timeout idle**命令配置的最大空闲时间。

【举例】

\# 在策略组pgroup下配置保活报文的发送时间间隔为50秒。

\<Sysname\> system-view

Sysname sslvpn context ctx

Sysname-sslvpn-context-ctx policy-group pgroup

Sysname-sslvpn-context-ctx-policy-group-pgroup ip-tunnel keepalive 50

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel wins-server**

------------------------------------------------------------------------

**[ip-tunnel wins-server**]命令用来配置为客户端指定的内网WINS服务器地址。

**[undo ip-tunnel wins-server**]命令用来恢复缺省情况。

【命令】

**[ip-tunnel wins-server **[{ **primary** \| **secondary** } *ip-address*]]

**[undo ip-tunnel wins-server **[{ **primary** \| **secondary** }]]

【缺省情况】

没有配置为客户端指定的WINS服务器地址。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[primary**]：配置主WINS服务器。

**[secondary**]：配置备WINS服务器。

*[ip-address*]：WINS服务器的IPv4地址，不能是组播、广播、环回地址。

【举例】

\# 配置为客户端指定的内网主WINS服务器地址为1.1.1.1。

\<Sysname\> system-view

Sysname sslvpn context ctx

Sysname-sslvpn-context-ctx policy-group pgroup

Sysname-sslvpn-context-ctx-policy-group-pgroup ip-tunnel wins-server primary 1.1.1.1

**SSL VPN \-- SSL VPN配置命令 \-- local-port**

------------------------------------------------------------------------

**[local-port**]命令用来添加一个端口转发实例。

**[undo local-port**]命令用来删除指定的端口转发实例。

【命令】

**[local-port** *local-port-number* **local-name** *local-name* **remote-server** *remote-server* **remote-port** *remote-port-number* [ **description** *description-string* ]]

**[undo local-port ***local-port-number ***local-name ***local-name*]

【缺省情况】

设备上不存在任何端口转发实例。

【视图】

端口转发列表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[local-port-number*]：企业网内的TCP服务映射的本地端口号，取值范围为1～65535。

**[local-name ***local-name*]：指定企业网内的TCP服务映射的本地地址或本地主机名称。*local-name*为1～253个字符的字符串，可以包含字母、数字、下划线、"-"和"."，不区分大小写。

**[remote-server ***remote-server*]：指定企业网内TCP服务的IP地址或完整域名。*remote-server*为为1～253个字符的字符串，可以包含字母、数字、下划线、"-"和"."，不区分大小写。

**[remote-port ***remote-port-number*]：指定企业网内TCP服务的端口号。*remote-port-number*取值范围为1～65535。

**[description ***description-string*]：指定端口转发实例的描述信息。*description-string*为1～63个字符的字符串，区分大小写。

【使用指导】

本命令用来将企业网内的基于TCP的服务（如Telnet、SSH、POP3）映射为SSL VPN客户端上的本地地址和本地端口，以便SSL VPN客户端通过本地地址和本地端口访问企业网内的服务器。例如，执行如下命令，表示在SSL VPN客户端上通过127.0.0.1、端口80可以访问企业网内的HTTP服务器192.168.0.213。

local-port 80 local-name 127.0.0.1 remote-server 192.168.0.213 remote-port 80

需要注意的是：

·配置的*local-port-number*不能与本地已有服务的端口号相同。

·如果将企业网内的TCP服务映射为本地地址，则建议将本地地址配置为127.0.0.0/8网段的地址；如果映射为本地主机名，SSL VPN的TCP接入客户端软件会在主机文件hosts（C:\\Windows\\System32\\drivers\\etc\\hosts）中添加主机名对应的IP地址，并在用户退出时恢复原来的主机文件hosts。

【举例】

\# 配置端口转发实例：将企业网内的HTTP服务器192.168.0.213映射为本地地址127.0.0.1、本地端口80；将企业网内的Telnet服务器100.100.100.101映射为本地地址127.0.0.1、本地端口2323。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 port-forward pflist1

Sysname-sslvpn-context-ctx1-port-forward-pflist1 local-port 80 local-name 127.0.0.1 remote-server 192.168.0.213 remote-port 80 description http

Sysname-sslvpn-context-ctx1-port-forward-pflist1 local-port 2323 local-name 127.0.0.1 remote-server 100.100.100.101 remote-port 23 description telnet

【相关命令】

·**port-forward**

·**resources port-forward**

**SSL VPN \-- SSL VPN配置命令 \-- log enable user-log**

------------------------------------------------------------------------

**[log enable user-log**]命令用来开启用户上下线信息的日志开关。

**[undo log enable user-log**]命令用来恢复缺省情况。

【命令】

**[log enable user-log**]

**[undo log enable user-log**]

【缺省情况】

用户上下线信息的日志开关处于关闭状态。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启本功能后，用户上线和下线时，SSL VPN网关会记录日志信息。生成的日志信息将被发送到设备的信息中心，通过设置信息中心的参数，决定日志信息的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）

【举例】

\# 开启用户上下线信息的日志开关。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 log enable user-log

**SSL VPN \-- SSL VPN配置命令 \-- login-message**

------------------------------------------------------------------------

**[login-message**]命令用来配置SSL VPN登录页面的欢迎信息。

**[undo login-message**]命令用来恢复缺省情况。

【命令】

**[login-message**[ { **chinese** *chinese-message* \| **english** *english-message* }]]

**[undo login-message **[{ **chinese** \| **english** }]]

【缺省情况】

英文登录页面的欢迎信息为"Welcome to SSL VPN"，中文登录页面的欢迎信息为"欢迎进入SSL VPN"。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chinese** *chinese-message*]：指定中文页面的欢迎信息。*chinese-message*为1～255个字符的字符串，区分大小写。

**[english** *english-message*]：指定英文页面的欢迎信息。*english-message*为1～255个字符的字符串，区分大小写。

【举例】

\# 配置SSL VPN英文页面的欢迎信息为"hello"，中文页面的欢迎信息为"你好"。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 login-message english hello

Sysname-sslvpn-context-ctx1 login-message chinese 你好

**SSL VPN \-- SSL VPN配置命令 \-- logo**

------------------------------------------------------------------------

**[logo**]命令用来配置SSL VPN页面上显示的logo。

**[undo logo**]命令用来恢复缺省情况。

【命令】

**[logo**[ { **file** *file-name* \| **none** }]]

**[undo logo**]

【缺省情况】

SSL VPN页面上显示"H3C"logo图标。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[file** *file-name*]：指定logo图标文件。*file-name*为1～255字符的字符串，不区分大小写。*filename*指定的logo图标文件必须为gif、jpg或png格式，且不能超过100KB。

**[none**]：不显示logo图标。

【使用指导】

指定的logo图标文件必须是本地已经存在的文件。

如果指定logo图标文件后，删除该文件，则仍然会显示该文件对应的logo图标。

【举例】

\# 配置SSL VPN页面上显示的logo为flash:/mylogo.gif文件对应的logo图标。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 logo flash:/mylogo.gif

**SSL VPN \-- SSL VPN配置命令 \-- max-users**

------------------------------------------------------------------------

**[max-users**]命令用来配置SSL VPN访问实例的最大会话数。

**[undo max-users**]命令用来恢复缺省情况。

【命令】

**[max-users ***number*]

**[undo max-users**]

【缺省情况】

SSL VPN访问实例的最大会话数为1048575。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：SSL VPN访问实例的最大会话数，取值范围为1～1048575。

【使用指导】

SSL VPN访问实例下的会话数目达到本命令配置的值后，新的用户将无法登录。

【举例】

\# 配置SSL VPN访问实例的最大会话数为500。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 max-users 500

【相关命令】

·**display sslvpn context**

**SSL VPN \-- SSL VPN配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置接口的MTU值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

SSL VPN AC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，取值范围为100～64000，单位为字节。

【举例】

\# 配置接口SSL VPN AC 1000的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface sslvpn-ac 1000

Sysname-SSLVPN-AC1000 mtu 1430

**SSL VPN \-- SSL VPN配置命令 \-- policy-group**

------------------------------------------------------------------------

**[policy-group**]命令用来创建策略组，并进入SSL VPN策略组视图。

**[undo policy-group**]命令用来删除指定的策略组。

【命令】

**[policy-group** *group-name*]

**[undo policy-group** *group-name*]

【缺省情况】

设备上不存在任何策略组。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：策略组名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。

【使用指导】

策略组包含一系列规则，这些规则为用户定义了资源的访问权限。

一个SSL VPN访问实例下可以配置多个策略组。远端接入用户访问SSL VPN访问实例时，AAA服务器将授权给该用户的策略组信息下发给SSL VPN网关。该用户可以访问的资源由授权的策略组决定。如果AAA服务器没有为该用户进行授权，则用户可以访问的资源由缺省策略组决定。

【举例】

\# 创建名为pg1的策略组，并进入SSL VPN策略组视图。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 policy-group pg1

Sysname-sslvpn-context-ctx1-policy-group-pg1

【相关命令】

·**default-policy-group**

**SSL VPN \-- SSL VPN配置命令 \-- port-forward**

------------------------------------------------------------------------

**[port-forward**]命令用来创建端口转发列表，并进入端口转发列表视图。

**[undo port-forward**]命令用来删除指定的端口转发列表。

【命令】

**[port-forward** *port-forward-name*]

**[undo port-forward ***port-forward-name*]

【缺省情况】

设备上不存在任何端口转发列表。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-forward-name*]：端口转发列表名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。

【使用指导】

端口转发列表用来为SSL VPN用户提供TCP接入服务。

在转发列表视图下，通过**local-port**命令可以创建端口转发实例。端口转发实例将企业网内的基于TCP的服务（如Telnet、SSH、POP3）映射为SSL VPN客户端上的本地地址和本地端口，以便SSL VPN客户端通过本地地址和本地端口访问企业网内的服务器。

在SSL VPN策略组视图下，通过**resources port-forward**命令可以配置策略组引用的端口转发列表。SSL VPN用户被授权访问某个策略组后，该策略组引用的端口转发列表指定的TCP接入服务将同时授权给SSL VPN用户，SSL VPN用户可以访问这些TCP接入服务。

【举例】

\# 创建端口转发列表pflist1，并进入端口转发列表视图。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-gateway-ctx1 port-forward pflist1

Sysname-sslvpn-context-ctx1-port-forward-pflist1

【相关命令】

·**local-port**

·**resources port-forward**

**SSL VPN \-- SSL VPN配置命令 \-- reset counters interface sslvpn-ac**

------------------------------------------------------------------------

**[reset counters interface sslvpn-ac**]命令用来清除SSL VPN AC接口的统计信息。

【命令】

**[reset counters interface** **sslvpn-ac** [ *interface-number*  ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：SSL VPN AC接口的编号，取值范围为0～4095。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定接口类型**sslvpn-ac**，则清除所有接口的统计信息；

·如果指定接口类型，不指定接口编号*interface-number*，则清除所有SSL VPN AC接口的统计信息；

·如果同时指定接口类型和接口编号，则清除指定SSL VPN AC接口的统计信息。

【举例】

\# 清除接口SSL VPN AC 1000的统计信息。

\<Sysname\> reset counters interface sslvpn-ac 1000

【相关命令】

·**display interface****sslvpn-ac**

**SSL VPN \-- SSL VPN配置命令 \-- resources port-forward**

------------------------------------------------------------------------

**[resources port-forward**]命令用来配置策略组引用端口转发列表。

**[undo resources port-forward**]命令用来取消策略组引用端口转发列表。

【命令】

**[resources port-forward** *port-forward-name*]

**[undo resources port-forward**]

【缺省情况】

策略组没有引用任何端口转发列表。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-forward-name*]：端口转发列表名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。

【使用指导】

SSL VPN用户被授权访问某个策略组后，该策略组引用的端口转发列表指定的TCP接入服务将同时授权给SSL VPN用户，SSL VPN用户可以访问这些TCP接入服务。

需要注意的是，本命令引用的端口转发列表必须先通过**port-forward**命令创建。

【举例】

\# 配置策略组pg1引用端口转发列表pflist1。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 policy-group pg1

Sysname-sslvpn-context-ctx1-policy-group-pg1 resources port-forward pflist1

【相关命令】

·**local-port**

·**port-forward**

**SSL VPN \-- SSL VPN配置命令 \-- service enable (SSL VPN context view)**

------------------------------------------------------------------------

**[service enable**]命令用来开启当前的SSL VPN访问实例。

**[undo service enable**]命令用来关闭当前的SSL VPN访问实例。

【命令】

**[service enable**]

**[undo service enable**]

【缺省情况】

SSL VPN访问实例处于关闭状态。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启名为ctx1的SSL VPN访问实例。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 service enable

【相关命令】

·**display sslvpn context**

**SSL VPN \-- SSL VPN配置命令 \-- service enable (SSL VPN gateway view)**

------------------------------------------------------------------------

**[service enable**]命令用来开启当前的SSL VPN网关。

**[undo service enable**]命令用来关闭当前的SSL VPN网关。

【命令】

**[service enable**]

**[undo service enable**]

【缺省情况】

当前的SSL VPN网关处于关闭状态。

【视图】

SSL VPN网关视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启当前的SSL VPN网关。

\<Sysname\> system-view

Sysname sslvpn gateway gw1

Sysname-sslvpn-gateway-gw1 service enable

【相关命令】

·**display sslvpn gateway**

**SSL VPN \-- SSL VPN配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo** **shutdown**]命令用来开启当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

SSL VPN AC接口均处于开启状态。

【视图】

SSL VPN AC接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭接口SSL VPN AC 1000。

\<Sysname\> system-view

Sysname interface sslvpn-ac 1000

Sysname-SSLVPN-AC1000 shutdown

**SSL VPN \-- SSL VPN配置命令 \-- ssl server-policy**

------------------------------------------------------------------------

**[ssl server-policy**]命令用来配置SSL VPN网关引用SSL服务器端策略。

**[undo ssl server-policy**]命令用来取消SSL VPN网关引用SSL服务器端策略。

【命令】

**[ssl server-policy** *policy-name*]

**[undo ssl server-policy**]

【缺省情况】

SSL VPN网关没有引用SSL服务器端策略。

【视图】

SSL VPN网关视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL VPN网关引用的SSL服务器端策略名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

通过本命令指定SSL VPN网关引用的SSL服务器端策略后，SSL VPN网关将采用该策略下的参数与远端接入用户建立SSL连接。

SSL VPN网关只能引用一个SSL服务器端策略。在同一个SSL VPN网关视图下，重复执行本命令，新的配置会覆盖已有配置，但新的配置不会立即生效。只有执行**undo service enable**命令关闭SSL VPN网关，并执行**service enable**命令开启SSL VPN网关后，新的配置才会生效。

【举例】

\# 配置SSL VPN网关gw1引用SSL服务器端策略CA_CERT。

\<Sysname\> system-view

Sysname sslvpn gateway gw1

Sysname-sslvpn-gateway-gw1 ssl server-policy CA_CERT

【相关命令】

·**display sslvpn gateway**

**SSL VPN \-- SSL VPN配置命令 \-- sslvpn context**

------------------------------------------------------------------------

**[sslvpn context**]命令用来创建SSL VPN访问实例，并进入SSL VPN访问实例视图。

**[undo sslvpn context**]命令用来删除指定的SSL VPN访问实例。

【命令】

**[sslvpn context** *context-name*]

**[undo sslvpn context** *context-name*]

【缺省情况】

设备上不存在任何SSL VPN访问实例。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：SSL VPN访问实例名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。

【使用指导】

SSL VPN访问实例用来管理用户会话、用户可以访问的资源、用户认证方式等。一个SSL VPN网关可以被多个SSL VPN访问实例引用，不同SSL VPN访问实例对应不同的资源。远端接入用户登录SSL VPN网关后可以访问的资源，由该用户所属的SSL VPN访问实例决定。

【举例】

\# 创建名为ctx1的SSL VPN访问实例，并进入SSL VPN访问实例视图。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1

【相关命令】

·**display sslvpn context**

**SSL VPN \-- SSL VPN配置命令 \-- sslvpn gateway**

------------------------------------------------------------------------

**[sslvpn gateway**]命令用来创建SSL VPN网关，并进入SSL VPN网关视图。

**[undo sslvpn gateway**]命令用来删除指定的SSL VPN网关。

【命令】

**[sslvpn gateway** *gateway-name*]

**[undo sslvpn gateway** *gateway-name*]

【缺省情况】

设备上不存在任何SSL VPN网关。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[gateway-name*]：SSL VPN网关名称，为1～31个字符的字符串，只能包含字母、数字、下划线，不区分大小写。

【使用指导】

SSL VPN网关位于远端接入用户和企业内部网络之间，负责在二者之间转发报文。SSL VPN网关与远端接入用户建立SSL连接，并对接入用户进行身份认证。远端接入用户的访问请求只有通过SSL VPN网关的安全检查和认证后，才会被SSL VPN网关转发到企业网络内部，从而实现对企业内部资源的保护。

在SSL VPN网关视图下，需要进行以下配置：

·通过**ip address**命令指定SSL VPN网关的IP地址和端口号，以便远端接入用户通过该IP地址和端口号访问SSL VPN网关。

·通过**ssl server-policy**命令指定SSL VPN网关引用的SSL服务器端策略，以便SSL VPN网关采用该策略下的参数与远端接入用户建立SSL连接。

·通过**service enable**命令开启SSL VPN网关。

需要注意的是，如果SSL VPN网关被SSL VPN访问实例引用，则该SSL VPN网关不能被删除。

【举例】

\# 创建SSL VPN网关gw1，并进入SSL VPN网关视图。

\<Sysname\> system-view

Sysname sslvpn gateway gw1

Sysname-sslvpn-gateway-gw1

【相关命令】

·**display sslvpn gateway**

**SSL VPN \-- SSL VPN配置命令 \-- sslvpn ip address-pool**

------------------------------------------------------------------------

**[sslvpn ip address-pool**]命令用来创建地址池。

**[undo sslvpn ip address-pool**]命令用来删除指定的地址池。

【命令】

**[sslvpn ip address-pool ***pool-name start-ip-address end-ip-address*]

**[undo sslvpn ip address-pool*** pool-name*]

【缺省情况】

设备上不存在任何地址池。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pool-name*]：地址池名称，为1～31个字符的字符串，由字母、数字、下划线组成，不区分大小写。

*[start-ip-address*]：地址池的起始地址。

*[end-ip-address*]：地址池的结束地址。结束地址必须大于起始地址。

【使用指导】

在策略组中引用本命令创建的地址池后，SSL VPN网关将从引用的地址池中选择地址、分配给IP接入方式的客户端。

需要注意的是，本命令中指定的起始地址和结束地址不能是组播、广播、环回地址。

【举例】

\# 创建地址池pool1，指定地址范围为10.1.1.1～10.1.1.254。

\<Sysname\> system-view

Sysname sslvpn ip address-pool pool1 10.1.1.1 10.1.1.254

**SSL VPN \-- SSL VPN配置命令 \-- timeout idle**

------------------------------------------------------------------------

**[timeout idle**]命令用来配置SSL VPN会话保持空闲状态的最长时间。

**[undo timeout idle**]命令用来恢复缺省情况。

【命令】

**[timeout** **idle** *seconds*]

**[undo timeout idle**]

【缺省情况】

SSL VPN会话保持空闲状态的最长时间为2100秒。

【视图】

SSL VPN策略组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：SSL VPN会话保持空闲状态的最长时间，取值范围为60～86400，单位为秒。

【使用指导】

如果SSL VPN会话保持空闲状态的时间超过本命令配置的值，则将断开该会话。

【举例】

\# 配置SSL VPN会话保持空闲状态的最长时间为1800秒。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 policy group pg1

Sysname-sslvpn-context-ctx1-policy-group-pg1 timeout idle 1800

【相关命令】

·**display sslvpn policy-group**

**SSL VPN \-- SSL VPN配置命令 \-- title**

------------------------------------------------------------------------

**[title**]命令用来配置SSL VPN页面的标题信息。

**[undo title**]命令用来恢复缺省情况。

【命令】

**[title**[ { **chinese** *chinese-title* \| **english** *english-title* }]]

**[undo title **[{ **chinese** \| **english** }]]

【缺省情况】

SSL VPN页面的标题为"SSL VPN"。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[chinese** *chinese-title*]：指定中文页面的标题信息。*chinese-title*为1～255个字符的字符串，区分大小写。

**[english** *english-title*]：指定英文页面的标题信息。*english-title*为1～255个字符的字符串，区分大小写。

【举例】

\# 配置SSL VPN英文页面的标题信息为"SSL VPN service for company A"，中文页面的标题信息为"公司A的SSL VPN服务"。

\<Sysname\> system-view

Sysname sslvpn context ctx1

Sysname-sslvpn-context-ctx1 title english SSL VPN service for company A

Sysname-sslvpn-context-ctx1 title chinese公司A的SSL VPN服务

**SSL VPN \-- SSL VPN配置命令 \-- verify-code**

------------------------------------------------------------------------

**[verify-code enable**]命令用来开启验证码验证功能。

**[undo verify-code enable**]命令用来关闭验证码验证功能。

【命令】

**[verify-code enable**]

**[undo verify-code enable**]

【缺省情况】

验证码验证功能处于开启状态。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启验证码验证后，用户登录时需要输入验证码。只有验证码验证成功后，才允许用户登录SSL VPN页面。

【举例】

\# 开启验证码验证功能。

\<Sysname\> system-view

Sysname sslvpn context ctx

Sysname-sslvpn-context-ctx verify-code enable

**SSL VPN \-- SSL VPN配置命令 \-- vpn-instance (SSL VPN context View)**

------------------------------------------------------------------------

**[vpn-instance**]命令用来配置SSL VPN访问实例关联的VPN实例。

**[undo vpn-instance**]命令用来取消SSL VPN访问实例关联VPN实例。

【命令】

**[vpn-instance ***vpn-instance-name*]

**[undo vpn-instance**]

【缺省情况】

SSL VPN访问实例关联公网。

【视图】

SSL VPN访问实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：SSL VPN访问实例关联的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

执行本命令后，SSL VPN访问实例包含的资源将属于关联的VPN实例。

每个SSL VPN访问实例只能关联一个VPN实例。

SSL VPN访问实例可以关联不存在的VPN实例，但该SSL VPN访问实例会处于未生效的状态。待VPN实例创建后，SSL VPN访问实例进入生效状态。

【举例】

\# 配置名为contex1的SSL VPN访问实例关联VPN实例vpn1。

\<Sysname\> System-view

Sysname sslvpn context context1

Sysname-sslvpn-context-context1 vpn-instance vpn1

**SSL VPN \-- SSL VPN配置命令 \-- vpn-instance (SSL VPN gateway view)**

------------------------------------------------------------------------

**[vpn-instance**]命令用来配置SSL VPN网关所属的VPN实例。

**[undo vpn-instance**]命令用来恢复缺省情况。

【命令】

**[vpn-instance ***vpn-instance-name*]

**[undo vpn-instance**]

【缺省情况】

SSL VPN网关属于公网。

【视图】

SSL VPN网关视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：SSL VPN网关所属的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

每个SSL VPN网关只能属于一个VPN实例。SSL VPN所属的VPN实例又称为front VPN instance。

本命令指定的VPN实例可以不存在，但此时SSL VPN网关处于不生效的状态。待VPN实例创建后，SSL VPN网关进入生效状态。

【举例】

\# 配置SSL VPN网关gateway1属于VPN实例vpn1。

\<Sysname\> system-view

Sysname sslvpn gateway gateway1

Sysname-sslvpn-gateway-gateway1 vpn-instance vpn1
