
**ADVPN \-- VAM Server配置命令 \-- authentication-algorithm**

------------------------------------------------------------------------

**[authentication-algorithm**]命令用来设置VAM协议报文的验证算法。

**[undo** **authentication-algorithm**]命令用来恢复缺省情况。

【命令】

**[authentication-algorithm**[ { **aes-xcbc-mac** \| **md5** \| **none** \| **sha-1** \| **sha-256** } \*]]

**[undo authentication-algorithm**]

【缺省情况】

VAM协议报文的验证算法为SHA-1。

【视图】

ADVPN域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aes-xcbc-mac**]：表示采用AES-XCBC-MAC验证算法。

**[md5**]：表示采用MD5验证算法。

**[none**]：表示不对VAM协议报文进行验证。

**[sha-1**]：表示采用SHA-1验证算法。

**[sha-256**]：表示采用SHA-256验证算法。

【使用指导】

VAM Server与VAM Client固定使用SHA-1验证算法对连接初始化请求和响应报文进行完整性验证；使用协商出来的验证算法对其他VAM协议报文进行完整性验证。

需要注意的是：

·验证算法在配置中的出现顺序决定其使用优先级。配置中越靠前的验证算法，其优先级越高。VAM Server在与VAM Client协商时，从VAM Client支持的验证算法列表中选择VAM Server上配置最靠前的算法作为协商结果。

·修改本配置对已经注册的VAM Client没有影响，新注册的VAM Client将采用修改后的验证算法进行协商。

【举例】

\# 设置在ADVPN域1中使用的验证算法优先级从高到低依次为MD5、SHA-1和SHA-256。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 authentication-algorithm md5 sha-1 sha-256

**ADVPN \-- VAM Server配置命令 \-- authentication-method**

------------------------------------------------------------------------

**[authentication-method**]命令用来配置VAM Server对VAM Client的身份认证方式。

**[undo authentication-method**]命令用来恢复缺省情况。

【命令】

**[authentication-method**[ { **none** \| { **chap** \| **pap** } [ **domain** *isp-name* ] }]]

**[undo authentication-method**]

【缺省情况】

VAM Server使用CHAP方式对VAM Client进行身份认证，认证使用的ISP域为用户配置的系统默认域。

【视图】

ADVPN域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[none**]：表示不对VAM Client进行认证。

**[chap**]：表示使用CHAP认证方式。

**[pap**]：表示使用PAP认证方式。

**[domain ***isp-name*]：指定认证使用的ISP域。*isp-name*表示ISP域的名称，为1～24个字符的字符串，不区分大小写，不能包括"\"、"[\|]"、"/"、":"、"\*"、"?"、"""、"\<"、"\>"以及"@"字符。如果未指定本参数，则认证使用的ISP域为用户配置的系统默认域。

【使用指导】

·如果指定的ISP域不存在，则VAM Server对VAM Client的身份认证会失败。

·修改本配置对已经注册的VAM Client没有影响，新注册的VAM Client将按照修改后的认证方式进行身份认证。

【举例】

\# 配置ADVPN域1对VAM Client采用CHAP方式进行身份认证，认证使用的ISP域为用户配置的系统默认域。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 authentication-method chap

**ADVPN \-- VAM Server配置命令 \-- display vam server address-map**

------------------------------------------------------------------------

**[display vam server address-map**]命令用来显示注册到VAM Server上的VAM Client的IPv4私网地址和公网地址映射信息。

【命令】

**[display** **vam** **server** **address-map** [ **advpn-domain** *domain-name* [ **private-address** *private-ip-address*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[advpn-domain ***domain-name*]：显示指定ADVPN域中注册的VAM Client的IPv4私网地址和公网地址映射信息。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。如果未指定本参数，则显示VAM Server上所有注册的VAM Client的IPv4私网地址和公网地址映射信息。

**[private-address ***private-ip-address*]：显示指定IPv4私网地址的映射信息。*private-ip-address*为VAM Client的IPv4私网地址。

**[verbose**]：显示地址映射的详细信息。如果未指定本参数，则显示地址映射的摘要信息。

【举例】

\# 显示所有ADVPN域中的IPv4私网地址和公网地址映射信息。

\<Sysname\> display vam server address-map

ADVPN domain name: 1

Total private address mappings: 2

Group      Private address  Public address              Type   NAT  Holding time

1          10.0.0.1         2001::1                     Hub    No   0H 13M 34S

1          10.0.0.3         74.125.128.102              Spoke  Yes  0H 4M 21S

ADVPN domain name: 2

Total private address mappings: 0

ADVPN domain name: 3

Total private address mappings: 1

Group      Private address  Public address              Type   NAT  Holding time

1          30.0.0.1         113.124.136.1               Hub    No   0H 0M 2S

ADVPN domain name: 4

Total private address mappings: 1

Group      Private address  Public address              Type   NAT  Holding time

1          40.0.0.1         4001::1                     Hub    No   1H 8M 22S

ADVPN domain name: 5

Total private address mappings: 1

Group      Private address  Public address              Type   NAT  Holding time

1          50.0.0.1         115.194.156.1               Hub    No   132H 41M 29S

\# 显示ADVPN域1中的IPv4私网地址和公网地址映射信息。

\<Sysname\> display vam server address-map advpn-domain 1

ADVPN domain name: 1

Total private address mappings: 2

Group      Private address  Public address              Type   NAT  Holding time

1          10.0.0.1         2001::1                     Hub    No   0H 13M 34S

1          10.0.0.3         74.125.128.102              Spoke  Yes  0H 4M 21S

\# 显示ADVPN域1中私网地址10.0.0.1的地址映射信息。

\<Sysname\> display vam server address-map advpn-domain 1 private-address 10.0.0.1

Group      Private address  Public address              Type   NAT  Holding time

1          10.0.0.1         2001::1                     Hub    No   0H 13M 34S

表1-1 display vam server address-map命令显示信息描述表

字段

描述

ADVPN domain name

ADVPN域的名称

Total private address mappings

IPv4私网地址和公网地址映射总数

Group

VAM Client所属的Hub组

Private address

VAM Client向VAM Server注册的私网地址

Public address

VAM Client向VAM Server注册的公网地址

Type

VAM Client类型，有Hub和Spoke两种类型

NAT

VAM Client是否穿越NAT

Holding time

VAM Client的存活时间，为x小时y分钟z秒（xH yM zS）

\# 显示所有ADVPN域中的IPv4私网地址和公网地址映射的详细信息。

\<Sysname\> display vam server address-map verbose

ADVPN domain name : 1

Private address   : 10.0.0.1

Type              : Hub

Hub group         : 1

Holding time      : 0H 13M 34S

Link protocol     : UDP

Public address    : 2001::1

Public port       : 10018

Registered address: 2001::1

Registered port   : 10018

Behind NAT        : No

ADVPN domain name : 1

Private address   : 10.0.0.3

Type              : Spoke

Hub group         : 1

Holding time      : 0H 4M 21S

Link protocol     : UDP

Public address    : 74.125.128.102

Public port       : 11297

Registered address: 192.168.23.6

Registered port   : 2158

Behind NAT        : Yes

ADVPN domain name : 3

Private address   : 30.0.0.1

Type              : Hub

Hub group         : 1

Holding time      : 0H 0M 2S

Link protocol     : GRE

Public address    : 113.124.136.1

Registered address: 113.124.136.1

Behind NAT        : No

ADVPN domain name : 4

Private address   : 40.0.0.1

Hub group         : 1

Holding time      : 1H 8M 22S

Link protocol     : IPsec-UDP

Public address    : 4001::1

Registered address: 4001::1

Registered port   : 4072

Behind NAT        : No

ADVPN domain name : 5

Private address   : 50.0.0.1

Type              : Hub

Hub group         : 1

Holding time      : 132H 41M 29S

Link protocol     : IPsec-GRE

Public address    : 115.194.156.1

Registered address: 115.194.156.1

Behind NAT        : No

\# 显示ADVPN域1中的IPv4私网地址和公网地址映射的详细信息。

\<Sysname\> display vam server address-map advpn-domain 1 verbose

ADVPN domain name : 1

Private address   : 10.0.0.1

Type              : Hub

Hub group         : 1

Holding time      : 0H 13M 34S

Link protocol     : UDP

Public address    : 2001::1

Public port       : 10018

Registered address: 2001::1

Registered port   : 10018

Behind NAT        : No

ADVPN domain name : 1

Private address   : 10.0.0.3

Type              : Spoke

Hub group         : 1

Holding time      : 0H 4M 21S

Link protocol     : UDP

Public address    : 74.125.128.102

Public port       : 11297

Registered address: 192.168.23.6

Registered port   : 2158

Behind NAT        : Yes

\# 显示ADVPN域1中私网地址10.0.0.1的地址映射详细信息。

\<Sysname\> display vam server address-map advpn-domain 1 private-address 10.0.0.1 verbose

ADVPN domain name : 1

Private address   : 10.0.0.1

Type              : Hub

Hub group         : 1

Holding time      : 0H 13M 34S

Link protocol     : UDP

Public address    : 2001::1

Public port       : 10018

Registered address: 2001::1

Registered port   : 10018

Behind NAT        : No

表1-2 display vam server address-map verbose命令显示信息描述表

字段

描述

ADVPN domain name

ADVPN域的名称

Private address

VAM Client向VAM Server注册的私网地址

Type

VAM Client类型，有Hub和Spoke两种类型

Hub group

VAM Client所属的Hub组

Holding time

VAM Client的存活时间，为x小时y分钟z秒（xH yM zS）

Link protocol

VAM Client建立ADVPN隧道使用的链路层协议，包括：

·UDP

·GRE

·IPsec-UDP

·IPsec-GRE

Public address

NAT转换后的VAM Client的公网地址

Public port

NAT转换后的VAM Client的ADVPN端口号

本字段仅在Link protocol为UDP或IPsec-UDP时显示

Registered address

VAM Client向VAM Server注册的公网地址

Registered port

VAM Client向VAM Server注册的ADVPN端口号

本字段仅在Link protocol为UDP或IPsec-UDP时显示

IPsec address

建立IPsec隧道时，本VAM Client使用的IP地址

本字段仅在Link protocol为IPsec-UDP或IPsec-GRE时显示

IPsec port

建立IPsec隧道时，本VAM Client使用的UDP端口号

本字段仅在Link protocol为IPsec-UDP或IPsec-GRE时显示

Behind NAT

VAM Client是否穿越NAT

【相关命令】

·**reset** **vam** **server** **address-map**

**ADVPN \-- VAM Server配置命令 \-- display vam server ipv6 address-map**

------------------------------------------------------------------------

**[display** **vam server ipv6** **address-map**]命令用来显示注册到VAM Server上的VAM Client的IPv6私网地址和公网地址映射信息。

【命令】

**[display** **vam** **server** **ipv6** **address-map** [ **advpn-domain** *domain-name* [ **private-address** *private-ipv6-address*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[advpn-domain*** domain-name*]：显示指定ADVPN域中注册的VAM Client的IPv6私网地址和公网地址映射信息。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。如果未指定本参数，则显示VAM Server上所有注册的VAM Client的IPv6私网地址和公网地址映射信息。

**[private-address ***private-ipv6-address*]：显示指定IPv6私网地址的映射信息。*private-ipv6-address*为VAM Client的IPv6私网地址。

**[verbose**]：显示地址映射的详细信息。如果未指定本参数，则显示地址映射的摘要信息。

【举例】

\# 显示所有ADVPN域中的IPv6私网地址和公网地址映射信息。

\<Sysname\> display vam server ipv6 address-map

ADVPN domain name: 1

Total private address mappings: 2

Group      Private address       Public address         Type   NAT  Holding time

1          1000::1:0:0:1         2001::1                Hub    No   0H 13M 34S

2          1000::2:0:0:1         220.181.111.85         Spoke  Yes  0H 4M 21S

ADVPN domain name: 2

Total private address mappings: 0

ADVPN domain name: 3

Total private address mappings: 1

Group      Private address       Public address         Type   NAT  Holding time

1          1003::1:0:0:1         3001::1                Hub    No   0H 0M 2S

ADVPN domain name: 4

Total private address mappings: 1

Group      Private address       Public address         Type   NAT  Holding time

1          1004::1:0:0:1         202.108.231.125        Hub    No   1H 8M 22S

ADVPN domain name: 5

Total private address mappings: 1

Group      Private address       Public address         Type   NAT  Holding time

1          1005::1:0:0:1         5001::1                Hub    No   132H 41M 29S

\# 显示ADVPN域1中的IPv6私网地址和公网地址映射信息。

\<Sysname\> display vam server ipv6 address-map advpn-domain 1

ADVPN domain name: 1

Total private address mappings: 2

Group      Private address       Public address         Type   NAT  Holding time

1          1000::1:0:0:1         2001::1                Hub    No   0H 13M 34S

2          1000::2:0:0:1         220.181.111.85         Spoke  Yes  0H 4M 21S

\# 显示ADVPN域1中私网地址1000::1:0:0:1的地址映射信息。

\<Sysname\> display vam server ipv6 address-map advpn-domain 1 private-address 1000::1:0:0:1

Group      Private address       Public address         Type   NAT  Holding time

1          1000::1:0:0:1         2001::1                Hub    No   0H 13M 34S

表1-3 display vam server ipv6 address-map命令显示信息描述表

字段

描述

ADVPN domain name

ADVPN域的名称

Total private address mappings

IPv6私网地址和公网地址映射总数

Group

VAM Client所属的Hub组

Private address

VAM Client向VAM Server注册的私网地址

Public address

VAM Client向VAM Server注册的公网地址

Type

VAM Client类型，有Hub和Spoke两种类型

NAT

VAM Client是否穿越NAT

Holding time

VAM Client的存活时间，为x小时y分钟z秒（xH yM zS）

\# 显示所有ADVPN域中IPv6私网地址和公网地址映射的详细信息。

\<Sysname\> display vam server ipv6 address-map verbose

ADVPN domain name : 1

Private address   : 1000::1:0:0:1

Link local address: FE80::50:4

Type              : Hub

Hub group         : 1

Holding time      : 0H 13M 34S

Link protocol     : UDP

Public address    : 2001::1

Public port       : 2098

Registered address: 2001::1

Registered port   : 2098

Behind NAT        : No

ADVPN domain name : 1

Private address   : 1000::2:0:0:1

Link local address: FE80::60:4

Type              : Spoke

Hub group         : 2

Holding time      : 0H 4M 21S

Link protocol     : UDP

Public address    : 220.181.111.85

Public port       : 10018

Registered address: 10.158.26.14

Registered port   : 2694

Behind NAT        : Yes

ADVPN domain name : 3

Private address   : 1003::1:0:0:1

Link local address: FE80::70:4

Type              : Hub

Hub group         : 1

Holding time      : 0H 0M 2S

Link protocol     : GRE

Public address    : 3001::1

Registered address: 3001::1

Behind NAT        : No

ADVPN domain name : 4

Private address   : 1004::1:0:0:1

Link local address: FE80::80:4

Hub group         : 1

Holding time      : 1H 8M 22S

Link protocol     : IPsec-UDP

Public address    : 202.108.231.125

Registered address: 202.108.231.125

Registered port   : 4072

Behind NAT        : No

ADVPN domain name : 5

Private address   : 1005::1:0:0:1

Link local address: FE80::90:4

Type              : Hub

Hub group         : 1

Holding time      : 132H 41M 29S

Link protocol     : IPsec-GRE

Public address    : 5001::1

Registered address: 5001::1

Behind NAT        : No

\# 显示ADVPN域1中的IPv6私网地址和公网地址映射的详细信息。

\<Sysname\> display vam server ipv6 address-map advpn-domain 1 verbose

ADVPN domain name : 1

Private address   : 1000::1:0:0:1

Link local address: FE80::50:4

Type              : Hub

Hub group         : 1

Holding time      : 0H 13M 34S

Link protocol     : UDP

Public address    : 2001::1

Public port       : 2098

Registered address: 2001::1

Registered port   : 2098

Behind NAT        : No

ADVPN domain name : 1

Private address   : 1000::2:0:0:1

Link local address: FE80::60:4

Type              : Spoke

Hub group         : 2

Holding time      : 0H 4M 21S

Link protocol     : UDP

Public address    : 220.181.111.85

Public port       : 10018

Registered address: 10.158.26.14

Registered port   : 2694

Behind NAT        : Yes

\# 显示ADVPN域1中私网地址1000::1:0:0:1的地址映射详细信息。

\<Sysname\> display vam server ipv6 address-map advpn-domain 1 ipv6 private-address 1000::1:0:0:1 verbose

ADVPN domain name : 1

Private address   : 1000::1:0:0:1

Link local address: FE80::50:4

Type              : Hub

Hub group         : 1

Holding time      : 0H 13M 34S

Link protocol     : UDP

Public address    : 2001::1

Public port       : 2098

Registered address: 2001::1

Registered port   : 2098

Behind NAT        : No

表1-4 display vam server ipv6 address-map verbose命令显示信息描述表

字段

描述

ADVPN domain name

ADVPN域的名称

Private address

VAM Client向VAM Server注册的私网地址

Link local address

VAM Client向VAM Server注册的私网链路本地地址

Type

VAM Client类型，有Hub和Spoke两种类型

Hub group

VAM Client所属的Hub组

Holding time

VAM Client的存活时间，为x小时y分钟z秒（xH yM zS）

Link protocol

VAM Client建立ADVPN隧道使用的链路层协议，包括：

·UDP

·GRE

·IPsec-UDP

·IPsec-GRE

Public address

VAM Client的真实公网地址

Public port

VAM Client的真实ADVPN端口号

本字段仅在Link protocol为UDP或IPsec-UDP时显示

Registered address

VAM Client向VAM Server注册的公网地址

Registered port

VAM Client向VAM Server注册的ADVPN端口号

本字段仅在Link protocol为UDP或IPsec-UDP时显示

IPsec address

IPsec链路使用的IP地址

本字段仅在Link protocol为IPsec-UDP或IPsec-GRE时显示

IPsec port

IPsec链路使用的UDP端口号

本字段仅在Link protocol为IPsec-UDP或IPsec-GRE时显示

Behind NAT

VAM Client是否穿越NAT

【相关命令】

·**reset** **vam** **server** **ipv6** **address-map**

**ADVPN \-- VAM Server配置命令 \-- display vam server ipv6 private-network**

------------------------------------------------------------------------

**[display** **vam server ipv6** **private-network**]命令用来显示注册到VAM Server上的VAM Client的IPv6私网信息。

【命令】

**[display** **vam** **server** **ipv6** **private-network** [ **advpn-domain** *domain-name* [ **private-address** *private-ipv6-address*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[advpn-domain*** domain-name*]：显示指定ADVPN域中VAM Client的IPv6私网信息。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。如果未指定本参数，则显示VAM Server上所有注册的VAM Client的IPv6私网信息。

**[private-address ***private-ipv6-address*]：显示指定IPv6私网地址的私网信息。*private-ipv6-address*为VAM Client的IPv6私网地址。

【举例】

\# 显示所有ADVPN域中VAM Client的IPv6私网信息。

\<Sysname\> display vam server ipv6 private-network

ADVPN domain name: 1

Total private networks: 5

Network/Prefix                     Private address                    Preference

1000::1:0:0:0/96                   1000::1:0:0:2                      80

1000::1:0:0:0/100                  1000::1:0:0:1                      80

1000::1:1:0:0/96                   1000::1:0:0:1                      80

1000::2:0:0:0/96                   1000::1:0:0:2                      80

1000::2:0:0:0/96                   1000::2:0:0:2                      80

ADVPN domain name: 2

Total private networks: 0

ADVPN domain name: 3

Total private networks: 1

Network/Prefix                     Private address                    Preference

1001::1:0:0:0/100                  1001::1:0:0:1                      80

\# 显示ADVPN域1中的IPv6私网信息。

\<Sysname\> display vam server ipv6 private-network advpn-domain 1

ADVPN domain name: 1

Total private networks: 5

Network/Prefix                     Private address                    Preference

1000::1:0:0:0/96                   1000::1:0:0:2                      80

1000::1:0:0:0/100                  1000::1:0:0:1                      80

1000::1:1:0:0/96                   1000::1:0:0:1                      80

1000::2:0:0:0/96                   1000::1:0:0:2                      80

1000::2:0:0:0/96                   1000::2:0:0:2                      80

\# 显示ADVPN域1中私网地址1000::1:0:0:1的私网信息。

\<Sysname\> display vam server ipv6 private-network advpn-domain 1 private-address 1000::1:0:0:1

Total private networks: 2

Network/Prefix                     Private address                    Preference

1000::1:0:0:0/100                  1000::1:0:0:1                      80

1000::1:1:0:0/96                   1000::1:0:0:1                      80

表1-5 display vam server ipv6 address-map命令显示信息描述表

字段

描述

ADVPN domain name

ADVPN域的名称

Total private networks

IPv6私网总数

Network/Prefix

Tunnel接口下配置的ADVPN隧道的私网网络地址/前缀长度

Private address

VAM Client向VAM Server注册的私网地址

Preference

VAM Client向VAM Server注册的私网路由优先级

**ADVPN \-- VAM Server配置命令 \-- display vam server private-network**

------------------------------------------------------------------------

**[display** **vam** **server** **private-network**]命令用来显示注册到VAM Server上的VAM Client的IPv4私网信息。

【命令】

**[display** **vam** **server** **private-network** [ **advpn-domain** *domain-name* [ **private-address** *private-ip-address*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[advpn-domain ***domain-name*]：显示指定ADVPN域中VAM Client的IPv4私网信息。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。如果未指定本参数，则显示VAM Server上所有注册VAM Client的的IPv4私网信息。

**[private-address ***private-ip-address*]：显示指定IPv4私网地址的私网信息。*private-ip-address*为VAM Client的IPv4私网地址。

【举例】

\# 显示所有ADVPN域中VAM Client的IPv4私网信息。

\<Sysname\> display vam server private-network

ADVPN domain name: 1

Total private networks: 5

Network/Mask              Private address        Preference

192.168.0.0/24            10.0.0.2               80

192.168.0.0/28            10.0.0.1               80

192.168.1.0/24            10.0.0.1               80

192.168.100.0/24          10.0.0.2               80

192.168.100.0/24          10.0.0.3               80

ADVPN domain name: 2

Total private networks: 0

ADVPN domain name: 3

Total private networks: 1

Network/Mask              Private address        Preference

192.168.200.0/24          20.0.0.1               80

\# 显示ADVPN域1中的IPv4私网信息。

\<Sysname\> display vam server private-network advpn-domain 1

ADVPN domain name: 1

Total private networks: 5

Network/Mask              Private address        Preference

192.168.0.0/24            10.0.0.2               80

192.168.0.0/28            10.0.0.1               80

192.168.1.0/24            10.0.0.1               80

192.168.100.0/24          10.0.0.2               80

192.168.100.0/24          10.0.0.3               80

\# 显示ADVPN域1中私网地址10.0.0.1的私网信息。

\<Sysname\> display vam server private-network advpn-domain 1 private-address 10.0.0.1

Total private networks: 5

Network/Mask              Private address        Preference

192.168.0.0/28            10.0.0.1               80

192.168.1.0/24            10.0.0.1               80

表1-6 display vam server address-map命令显示信息描述表

字段

描述

ADVPN domain name

ADVPN域的名称

Total private network number

IPv4私网总数

Network/Mask

Tunnel接口下配置的ADVPN隧道的私网网络地址/子网掩码长度

Private address

VAM Client向VAM Server注册的私网地址

Preference

VAM Client向VAM Server注册的私网路由优先级

**ADVPN \-- VAM Server配置命令 \-- display vam server statistics**

------------------------------------------------------------------------

**[display vam server statistic**]命令用来显示VAM Server上ADVPN域的统计信息。

【命令】

**[display** **vam** **server** **statistics** [ **advpn-domain** *domain-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[advpn-domain*** domain-name*]：显示指定ADVPN域的统计信息。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。如果未指定本参数，则显示VAM Server上所有ADVPN域的统计信息。

【举例】

\# 显示VAM Server上所有ADVPN域的统计信息。

\<Sysname\> display vam server statistics

Total ADVPN number: 3

Total spoke number: 121

Total hub number  : 3

ADVPN domain name      : 1

Server status          : Enabled

Holding time           : 0H 1M 47S

Registered spoke number: 98

Registered hub number  : 2

Packets received:

  Initialization request        : 100

  Initialization complete       : 100

  Register request              : 100

  Authentication information    : 100

  Address resolution request    : 203

  Network registration request  : 59

  Update request                : 196

  Logout request                : 0

  Hub information response      : 2

  Data flow information response: 0

  Keepalive                     : 642

  Error notification            : 0

  Unkonwn                       : 0

Packets sent:

  Initialization response      : 100

  Initialization complete      : 100

  Authentication request       : 100

  Register response            : 100

  Address resolution response  : 203

  Network registration response: 59

  Update response              : 196

  Hub information request      : 2

  Data flow information request: 0

  Logout response              : 0

  Keepalive                    : 642

  Error notification           : 0

ADVPN domain name      : 2

Server status          : Disabled

ADVPN domain name      : 3

Server status          : Enabled

Holding time           : 0H 33M 53S

Registered spoke number: 23

Registered hub number  : 1

Packets received:

  Initialization request        : 24

  Initialization complete       : 24

  Register request              : 24

  Authentication information    : 24

  Address resolution request    : 23

  Network registration request  : 0

  Update request                : 5

  Logout request                : 0

  Hub information response      : 2

  Data flow information response: 0

  Keepalive                     : 362

  Error notification            : 0

  Unkonwn                       : 0

Packets sent:

  Initialization response      : 24

  Initialization complete      : 24

  Authentication request       : 24

  Register response            : 24

  Address resolution response  : 23

  Network registration response: 0

  Update response              : 0

  Hub information request      : 2

  Data flow information request: 0

  Logout response              : 0

  Keepalive                    : 362

  Error notification           : 0

\# 显示VAM Server上ADVPN域1的统计信息。

\<Sysname\> display vam server statistics advpn-domain 1

ADVPN domain name      : 1

Server status          : Enabled

Holding time           : 0H 1M 47S

Registered spoke number: 98

Registered hub number  : 2

Packets received:

  Initialization request        : 100

  Initialization complete       : 100

  Register request              : 100

  Authentication information    : 100

  Address resolution request    : 203

  Network registration request  : 59

  Update request                : 196

  Logout request                : 0

  Hub information response      : 2

  Data flow information response: 0

  Keepalive                     : 642

  Error notification            : 0

  Unkonwn                       : 0

Packets sent:

  Initialization response      : 100

  Initialization complete      : 100

  Authentication request       : 100

  Register response            : 100

  Address resolution response  : 203

  Network registration response: 59

  Update response              : 196

  Hub information request      : 2

  Data flow information request: 0

  Logout response              : 0

  Keepalive                    : 642

  Error notification           : 0

表1-7 display vam server statistics命令显示信息描述表

字段

描述

Total ADVPN number

VAM Server上ADVPN域的数目

Total spoke number

VAM Server上所有ADVPN域中Spoke类型客户端数目

Total hub number

VAM Server上所有ADVPN域中Hub类型客户端数目

ADVPN domain name

ADVPN域的名称

Server status

ADVPN域中VAM Server功能的启用情况：

·Enabled：表示启用VAM Server功能

·Disabled：表示关闭VAM Server功能

Holding time

ADVPN域的存活时间，为x小时y分钟z秒（xH yM zS）

Registered spoke number

ADVPN域中注册的Spoke数目

Registered hub number

ADVPN域中注册的Hub数目

Packets received

ADVPN域中接收的报文数目

Initialization request

ADVPN域中接收的初始化请求报文数目

Initialization complete

ADVPN域中接收的初始化完成报文数目

Register request

ADVPN域中接收的注册请求报文数目

Authentication information

ADVPN域中接收的认证信息报文数目

Address resolution request

ADVPN域中接收的地址解析请求报文数目

Network registration request

ADVPN域中接收的私网注册请求报文数目

Update request

ADVPN域中接收的节点更新请求报文数目

Logout request

ADVPN域中接收的清除请求报文数目

Hub information response

ADVPN域中接收的Hub信息响应报文数目

Data flow information response

ADVPN域中接收的数据流信息响应报文数目

Keepalive

ADVPN域中接收的Keepalive报文数目

Error notification

ADVPN域中接收的错误通知报文数目

Unkonwn

ADVPN域中接收的未知报文或错误报文数目

Packets sent

ADVPN域中发送的报文数目

Initialization response

ADVPN域中发送的初始化响应报文数目

Initialization complete

ADVPN域中发送的初始化完成报文数目

Authentication request

ADVPN域中发送的认证请求报文数目

Register response

ADVPN域中发送的注册响应报文数目

Address resolution response

ADVPN域中发送的地址解析响应报文数目

Network registration response

ADVPN域中发送的子网注册响应报文数目

Update response

ADVPN域中发送的节点更新响应报文数目

Hub information request

ADVPN域中发送的Hub信息请求报文数目

Data flow information request

ADVPN域中发送的数据流信息请求报文数目

Logout response

ADVPN域中发送的清除响应报文数目

Keepalive

ADVPN域中发送的Keepalive报文数目

Error notification

ADVPN域中发送的错误通知报文数目

【相关命令】

·**reset vam server statistic**

**ADVPN \-- VAM Server配置命令 \-- encryption-algorithm**

------------------------------------------------------------------------

**[encryption-algorithm**]命令用来配置VAM协议报文的加密算法。

**[undo encryption-algorithm**]命令用来恢复缺省情况。

【命令】

**[encryption-algorithm**[ { **3des-cbc** \| **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** \| **aes-ctr-128** \| **aes-ctr-192** \| **aes-ctr-256** \| **des-cbc** \| **none** } \*]]

**[undo encryption-algorithm**]

【缺省情况】

按照优先级由高到低依次使用AES-CBC-256、AES-CBC-192、AES-CBC-128、AES-CTR-256、AES-CTR-192、AES-CTR-128、3DES-CBC、DES-CBC算法。

【视图】

ADVPN域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[3des-cbc**]：表示采用3DES-CBC加密算法。

**[aes-cbc-128**]：表示采用AES-CBC加密算法，密钥长度128位。

**[aes-cbc-192**]：表示采用AES-CBC加密算法，密钥长度192位。

**[aes-cbc-256**]：表示采用AES-CBC加密算法，密钥长度256位。

**[aes-ctr-128**]：表示采用AES-CTR加密算法，密钥长度128位。

**[aes-ctr-192**]：表示采用AES-CTR加密算法，密钥长度192位。

**[aes-ctr-256**]：表示采用AES-CTR加密算法，密钥长度256位。

**[des-cbc**]：表示采用DES-CBC加密算法。

**[none**]：表示不对VAM协议报文进行加密。

【使用指导】

VAM Server与VAM Client固定使用AES-CBC-128加密算法对连接初始化请求和响应报文进行加密；使用协商出来的加密算法对其他VAM协议报文进行加密。

需要注意的是：

·加密算法在配置中的出现顺序决定其使用优先级。配置中越靠前的加密算法，其优先级越高。VAM Server在与VAM Client协商时，从VAM Client支持的加密算法列表中选择配置最靠前的算法作为协商结果。

·修改本配置对已经注册的VAM Client没有影响，新注册的VAM Client将采用修改后的加密算法进行协商。

【举例】

\# 配置在ADVPN域1中按照优先级由高到低的顺序使用AES-CBC-128和3DES-CBC加密算法。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 encryption-algorithm aes-cbc-128 3des-cbc

**ADVPN \-- VAM Server配置命令 \-- hub-group**

------------------------------------------------------------------------

**[hub-group**]命令用来创建Hub组，并进入Hub组视图。如果Hub组已经存在，则直接进入该Hub组视图。

**[undo hub-group**]命令用来删除指定Hub组。

【命令】

**[hub-group** *group-name*]

**[undo hub-group** *group-name*]

【缺省情况】

不存在Hub组。

【视图】

ADVPN域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：Hub组的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。

【使用指导】

在大规模组网情况下，将ADVPN域划分为多个Hub组可以方便管理。创建Hub组后，可以按照Spoke的私网地址网段或地址范围，将Spoke划分到不同的Hub组中，并为每个Hub组指定一个或多个Hub。

当VAM Client向VAM Server注册时，VAM Server根据VAM Client的私网地址将VAM Client划分到对应的ADVPN域Hub组中：

(1)根据Hub组名称字典序依次匹配各Hub组内配置的Hub私网地址。

(2)如果匹配上，则VAM Client为Hub，并被划分到该Hub组；如果VAM Client不是Hub，再根据Hub组名称字典序依次匹配各Hub组内配置的Spoke私网地址范围。

(3)如果匹配上，则VAM Client为Spoke，并被划分到该Hub组；否则，VAM Client既不是Hub也不是Spoke，注册失败。

VAM Server只向VAM Client下发其所属的Hub组内的Hub信息。VAM Client只与本Hub组内的Hub建立永久ADVPN隧道。

【举例】

\# 在ADVPN域1内创建Hub组1，并进入Hub组视图。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 hub-group 1

Sysname-vam-server-domain-1-hub-group-1

**ADVPN \-- VAM Server配置命令 \-- hub ipv6 private-address**

------------------------------------------------------------------------

**[hub ipv6 private-address**]命令用来添加Hub组内的Hub IPv6私网地址。

**[undo hub ipv6 private-address**]命令用来删除Hub组内的Hub IPv6私网地址。

【命令】

**[hub** **ipv6 private-address**[ *private-ipv6-address* [ **public-address** { *public-ip-address* \| *public-ipv6-address* } [ **advpn-port** *port-number* ] ]]]

**[undo** **hub** **ipv6** **private-address** *private-ipv6-address*]

【缺省情况】

Hub组内没有配置Hub IPv6私网地址。

【视图】

Hub组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[private-ipv6-addres*s]：Hub的IPv6私网地址，该地址必须是全球单播地址。

**[public-address**]：指定Hub的公网地址。如果未指定本参数，VAM Server使用该Hub注册的公网地址。

*[public-ip-address*]：Hub的IPv4公网地址，该地址必须是单播地址。

*[public-ipv6-address*]：Hub的IPv6公网地址，该地址必须是全球单播地址。

**[advpn-port*** port-number*]：Hub的ADVPN端口号，取值范围为1025～65535。如果未指定本参数，VAM Server使用该Hub注册的ADVPN端口号。

【使用指导】

一般情况下，不需要指定Hub的公网地址和ADVPN端口号。只有当Hub要穿越NAT时，由于Hub注册的公网地址和ADVPN端口号是经过NAT转换前的，需要在NAT网关上为Hub配置一个固定的地址和端口号的转换关系。此时，需要指定Hub的公网地址和ADVPN端口号为NAT网关上配置的转换后的地址和端口号。

需要注意的是：

·每个Hub组内可以配置多个IPv6私网地址不同的Hub。

·如果指定IPv6私网地址的Hub已经存在，新配置将覆盖原有配置。

【举例】

\# 向ADVPN域1的Hub组1中添加Hub，其IPv6私网地址为1000::1:0:0:1，公网地址为2001::1，ADVPN端口号为8000。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 hub-group 1

Sysname-vam-server-domain-1-hub-group-1 hub ipv6 private-address 1000::1:0:0:1 public-address 2001::1 advpn-port 8000

**ADVPN \-- VAM Server配置命令 \-- hub private-address**

------------------------------------------------------------------------

**[hub private-address**]命令用来添加Hub组内的Hub IPv4私网地址。

**[undo hub private-address**]命令用来删除Hub组内的Hub IPv4私网地址。

【命令】

**[hub** **private-address**[ *private-ip-address* [ **public-address** { *public-ip-address* \| *public-ipv6-address* } [ **advpn-port** *port-number* ] ]]]

**[undo** **hub** **private-address** *private-ip-address*]

【缺省情况】

Hub组内没有配置Hub IPv4私网地址。

【视图】

Hub组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[private-ip-addres*s]：Hub的IPv4私网地址，该地址必须是单播地址。

**[public-address**]：指定Hub的公网地址。如果未指定本参数，VAM Server使用该Hub注册的公网地址。

*[public-ip-address*]：Hub的IPv4公网地址，该地址必须是单播地址。

*[public-ipv6-address*]：Hub的IPv6公网地址，该地址必须是全球单播地址。

**[advpn-port*** port-number*]：Hub的ADVPN端口号，取值范围为1025～65535。如果未指定本参数，VAM Server使用该Hub注册的ADVPN端口号。

【使用指导】

·一般情况下，不需要指定Hub的公网地址和ADVPN端口号。只有当Hub要穿越NAT时，由于Hub注册的公网地址和ADVPN端口号是经过NAT转换前的，需要在NAT网关上为Hub配置一个固定的地址和端口号的转换关系。此时，需要指定Hub的公网地址和ADVPN端口号为NAT网关上配置的转换后的地址和端口号。

·每个Hub组内可以配置多个IPv4私网地址不同的Hub。

·如果指定IPv4私网地址的Hub已经存在，新配置将覆盖原有配置。

【举例】

\# 向ADVPN域1的Hub组1中添加Hub，其IPv4私网地址为10.1.1.1，公网地址为123.0.0.1，ADVPN端口号为8000。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 hub-group 1

Sysname-vam-server-domain-1-hub-group-1 hub private-address 10.1.1.1 public-address 123.0.0.1 advpn-port 8000

**ADVPN \-- VAM Server配置命令 \-- keepalive**

------------------------------------------------------------------------

**[keepalive**]命令用来配置VAM Client发送Keepalive报文的时间间隔和重发次数。

**[undo keepalive**]命令用来恢复缺省情况。

【命令】

**[keepalive interval*** time-interval*** retry ***retry-times*]

**[undo keepalive**]

【缺省情况】

VAM Client发送Keepalive报文的时间间隔为180秒，重发次数为3次。

【视图】

ADVPN域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval** *time-interval*]：VAM Client发送Keepalive报文的时间间隔，取值范围为5～65535，单位为秒。

**[retry ***retry-times*]：VAM Client发送Keepalive报文的重发次数，取值范围为1～6。

【使用指导】

配置的时间间隔和重发次数值由VAM Server在注册响应报文中下发给VAM Client，同一个ADVPN域中所有VAM Client的Keepalive报文参数都是相同的。但是，如果VAM Server改变Keepalive报文参数，则修改后的参数只对新注册的VAM Client生效，已经注册的VAM Client不受影响。

VAM Client和VAM Server之间通过Keepalive报文保持联系。VAM Client按照VAM Server指定的时间间隔向VAM Server发送Keepalive报文，VAM Server收到Keepalive报文后回复响应报文。当Keepalive报文的重发次数达到指定的值仍没有收到VAM Server的响应时，VAM Client认为与VAM Server的连接中断，不再发送Keepalive报文。当VAM Server在时间间隔×重发次数的时间内没有收到VAM Client的Keepalive报文，则认为与VAM Client的连接中断，会删除该VAM Client的信息并将其下线。

需要注意的是，如果VAM Server与VAM Client间存在配置了动态NAT的设备，则Keepalive报文的发送时间间隔应小于NAT表项的老化时间，从而保证NAT表项不会老化。

【举例】

\# 配置ADVPN域1中VAM Client发送Keepalive报文的时间间隔为30秒，重发次数为5次。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 keepalive interval 30 retry 5

**ADVPN \-- VAM Server配置命令 \-- pre-shared-key (ADVPN domain view)**

------------------------------------------------------------------------

**[pre-shared-key**]命令用来配置VAM Server的预共享密钥。

**[undo pre-shared-key**]命令用来删除配置的预共享密钥。

【命令】

**[pre-shared-key **[{ **cipher** *cipher-string* \| **simple** *simple-string* }]]

**[undo** **pre-shared-key**]

【缺省情况】

未配置VAM Server的预共享密钥。

【视图】

ADVPN域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher*** cipher-string*]：以密文方式设置预共享密钥。*cipher-string*为密文预共享密钥，为1～73个字符的密文字符串，区分大小写。

**[simple*** simple-string*]：以明文方式设置预共享密钥。*simple-string*为明文预共享密钥，为1～31个字符的明文字符串，区分大小写。

【使用指导】

预共享密钥是VAM Server用来和VAM Client建立安全通道的公共密钥材料。在连接初始化阶段预共享密钥用来生成验证和加密连接请求、连接响应报文的初始密钥；如果选择对后续的报文进行加密和验证，则预共享密钥还用来生成验证和加密后续报文的连接密钥。

需要注意的是：

·以明文或密文形式设置的预共享密钥，均以密文的方式保存在配置文件中。

·同一个ADVPN域内的VAM Client和VAM Server上配置的预共享密钥必须一致。

【举例】

\# 以明文方式配置ADVPN域1中VAM Server的预共享密钥为123。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 pre-shared-key simple 123

【相关命令】

·**pre-shared-key** (VAM client view)

**ADVPN \-- VAM Server配置命令 \-- retry interval**

------------------------------------------------------------------------

**[retry interval**]命令用来设置VAM Server重发请求报文的时间间隔。

**[undo retry interval**]命令用来恢复缺省情况。

【命令】

**[retry interval** *time-interval*]

**[undo retry interval**]

【缺省情况】

VAM Server重发请求报文的时间间隔为5秒。

【视图】

ADVPN域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-interval*]：VAM Server重发请求报文的时间间隔，取值范围为3～30，单位为秒。

【使用指导】

VAM Server向VAM Client发送请求报文后，如果在指定的时间间隔内没有收到响应报文，VAM Server将重新发送请求报文，直到收到响应报文或者VAM Client Keepalive超时（即VAM Server在Keepalive报文发送时间间隔×重发次数的时间内没有收到VAM Client的Keepalive报文）为止。

【举例】

\# 设置ADVPN域1中VAM Server向VAM Client重发请求报文的时间间隔为20秒。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 retry interval 20

**ADVPN \-- VAM Server配置命令 \-- reset vam server address-map**

------------------------------------------------------------------------

**[reset** **vam** **server** **address-map**]命令用来清除注册到VAM Server上的IPv4私网地址和公网地址映射信息。

【命令】

**[reset** **vam** **server** **address-map** [ **advpn-domain** *domain-name* [ **private-address** *private-ip-address*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advpn-domain ***domain-name*]：清除指定ADVPN域中注册的IPv4私网地址和公网地址映射信息。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。如果未指定本参数，则清除VAM Server上注册的所有IPv4私网地址和公网地址映射信息。

**[private-address ***private-ip-address*]：清除指定IPv4私网地址的映射信息。*private-ip-address*为VAM Client的IPv4私网地址。如果未指定本参数，则清除指定ADVPN域或所有ADVPN域中的IPv4私网地址和公网地址映射信息。

【使用指导】

执行本命令除了会清除VAM Server上注册的IPv4私网地址和公网地址映射信息外，还会清除该IPv4私网地址相关的私网信息，并向注册该IPv4私网地址的VAM Client发送错误通知报文，要求VAM Client下线。

【举例】

\# 清除VAM Server上注册的所有IPv4私网地址和公网地址映射信息。

\<Sysname\> reset vam server address-map

\# 清除ADVPN域1中注册的所有IPv4私网地址和公网地址映射信息。

\<Sysname\> reset vam server address-map advpn-domain 1

\# 清除ADVPN域1中私网地址10.0.0.1的地址映射信息。

\<Sysname\> reset vam server address-map advpn-domain 1 private-address 10.0.0.1

【相关命令】

·**display** **vam** **server** **address-map**

**ADVPN \-- VAM Server配置命令 \-- reset vam server ipv6 address-map**

------------------------------------------------------------------------

**[reset** **vam** **server** **ipv6** **address-map**]命令用来清除注册到VAM Server上的IPv6私网地址和公网地址映射信息。

【命令】

**[reset** **vam** **server** **ipv6** **address-map** [ **advpn-domain** *domain-name* [ **private-address** *private-ipv6-address*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advpn-domain ***domain-name*]：清除指定ADVPN域中注册的IPv6私网地址和公网地址映射信息。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。如果未指定本参数，则清除VAM Server上注册的所有IPv6私网地址和公网地址映射信息。

**[private-address ***private-ipv6-address*]：清除指定IPv6私网地址的映射信息。*private-ipv6-address*为VAM Client的IPv6私网地址。如果未指定本参数，则清除指定ADVPN域或所有ADVPN域中的IPv6私网地址和公网地址映射信息。

【使用指导】

执行本命令除了会清除VAM Server上注册的IPv6私网地址和公网地址映射信息外，还会清除该IPv6私网地址相关的私网信息，并向注册该IPv6私网地址的VAM Client发送错误通知报文，要求VAM Client下线。

【举例】

\# 清除VAM Server上注册的所有IPv6私网地址和公网地址映射信息。

\<Sysname\> reset vam server ipv6 address-map

\# 清除ADVPN域1中注册的所有IPv6私网地址和公网地址映射信息。

\<Sysname\> reset vam server ipv6 address-map advpn-domain 1

\# 清除ADVPN域1中私网地址1000::1:0:0:1的地址映射信息。

\<Sysname\> reset vam server ipv6 address-map advpn-domain 1 private-address 1000::1:0:0:1

【相关命令】

·**display vam server ****ipv6 address-map**

**ADVPN \-- VAM Server配置命令 \-- reset vam server statistics**

------------------------------------------------------------------------

**[reset vam server statistics**]命令用来清除VAM Server上ADVPN域的统计信息。

【命令】

**[reset** **vam** **server** **statistics** [ **advpn-domain** *domain-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advpn-domain*** domain-name*]：清除VAM Server上指定ADVPN域的统计信息。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符为A～Z、a～z、0～9和"."。如果未指定本参数，则清除VAM Server上所有ADVPN域的统计信息。

【举例】

\# 清除名为abc的ADVPN域的统计信息。

\<Sysname\> reset vam server statistics advpn-domain abc

\# 清除所有ADVPN域的统计信息。

\<Sysname\> reset vam server statistics

【相关命令】

·**display vam server statistics**

**ADVPN \-- VAM Server配置命令 \-- server enable**

------------------------------------------------------------------------

**[server enable**]命令用来启动指定ADVPN域的VAM Server功能。

**[undo server enable**]命令用来关闭指定ADVPN域的VAM Server功能。

【命令】

**[server enable**]

**[undo server enable**]

【缺省情况】

ADVPN域的VAM Server功能处于关闭状态。

【视图】

ADVPN域视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

除了执行本命令外，还可以在系统视图下通过**vam** **server** **enable**命令来启动所有或指定ADVPN域的VAM Server功能。

【举例】

\# 启动ADVPN域1的VAM Server功能。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 server enable

【相关命令】

·**vam server enable**

**ADVPN \-- VAM Server配置命令 \-- shortcut interest**

------------------------------------------------------------------------

**[shortcut interest**]命令用来配置跨Hub组建立IPv4 Spoke-Spoke直连隧道的规则。

**[undo** **shortcut interest**]命令用来恢复缺省情况。

【命令】

**[shortcut interest**[ [ { *acl-number* \| **name** *acl-name* } \| **all** }]]

**[undo****shortcut interest**]

【缺省情况】]

没有配置跨Hub组建立IPv4 Spoke-Spoke直连隧道的规则，不允许跨Hub组建立IPv4 Spoke-Spoke直连隧道。

【视图】

Hub组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl**]：表示只允许匹配指定IPv4 ACL的Spoke之间建立跨Hub组的IPv4 Spoke-Spoke直连隧道。

*[acl-number*]：IPv4 ACL的编号，取值范围及其代表的ACL类型如下：

·2000～2999：表示IPv4基本ACL。

·3000～3999：表示IPv4高级ACL。

**[name** *acl-name*]：指定IPv4 ACL的名称。*acl-name*为ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。为避免混淆，ACL的名称不允许使用英文单词all。

**[all**]：表示所有跨Hub组的Spoke之间均可建立IPv4 Spoke-Spoke直连隧道。

【使用指导】

如果配置了跨Hub组建立IPv4 Spoke-Spoke直连隧道的规则，则在Hub上线后，VAM Server将指定的规则下发到Hub。

·如果规则指定为**all**，则Hub在转发任意跨Hub组的IPv4 Spoke-Spoke私网数据报文的同时，会向相应Spoke发送重定向报文。

·如果规则指定为匹配ACL，则Hub在转发跨Hub组的IPv4 Spoke-Spoke私网数据报文的同时，会将报文与指定的ACL进行匹配。如果匹配成功，Hub会向相应的Spoke发送重定向报文；否则，不会发送重定向报文。

Spoke收到重定向报文后，将被重定向的数据报文的目的地址发送给VAM Server，向VAM Server查询连接该目的地址所在私网网段的Spoke节点的信息，并与该Spoke建立直连隧道。

跨Hub组Spoke-Spoke直连隧道建立前，数据报文仍由Hub进行转发。直连隧道建立后，数据报文将直接发送到直连路由下一跳所对应的Spoke，而不再经过Hub中转。

需要注意的是：

·如果指定的ACL不存在，则配置不生效。任何私网数据报文都不会触发Hub向Spoke发送重定向报文。

·对于IPv4基本ACL，本命令仅支持匹配源地址信息的规则；对于IPv4高级ACL，仅支持匹配协议类型、源地址、目的地址、源端口和目的端口信息的规则，并且不支持排除某个源/目的端口号的规则。

·如果本命令指定的ACL中包含不支持的规则，则该条ACL规则将不生效。

【举例】

\# 配置如果Spoke之间的报文匹配ACL 3000，则允许建立跨Hub组的IPv4 Spoke-Spoke直连隧道。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 hub-group 1

Sysname-vam-server-domain-1-hub-group-1 shortcut interest acl 3000

**ADVPN \-- VAM Server配置命令 \-- shortcut ipv6 interest**

------------------------------------------------------------------------

**[shortcut ipv6 interest**]命令用来配置跨Hub组建立IPv6 Spoke-Spoke直连隧道的规则。

**[undo** **shortcut ipv6 interest**]命令用来恢复缺省情况。

【命令】

**[shortcut** **ipv6**[ **interest** { **acl** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \| **all** }]]

**[undo** **shortcut** **ipv6** **interest**]

【缺省情况】

没有配置跨Hub组建立IPv6 Spoke-Spoke直连隧道的规则，不允许跨Hub组建立IPv6 Spoke-Spoke直连隧道。

【视图】

Hub组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl**]：表示只允许匹配指定IPv6 ACL的Spoke之间建立跨Hub组的IPv6 Spoke-Spoke直连隧道。

*[ipv6-acl-number*]：IPv6 ACL的编号，取值范围及其代表的ACL类型如下：

·2000～2999：表示IPv6基本ACL。

·3000～3999：表示IPv6高级ACL。

**[name** *ipv6-acl-name*]：指定IPv6 ACL的名称。*ipv6-acl-name*为ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。为避免混淆，ACL的名称不允许使用英文单词all。

**[all**]：表示所有跨Hub组的Spoke之间均可建立IPv6 Spoke-Spoke直连隧道。

【使用指导】

配置了跨Hub组建立IPv6 Spoke-Spoke直连隧道的规则，在Hub上线后，VAM Server通过数据流信息报文将指定的规则下发到Hub。

·如果规则指定为**all**，则Hub在转发任意跨Hub组的IPv6 Spoke-Spoke私网数据报文的同时，会向相应Spoke发送重定向报文。

·如果规则指定为匹配ACL，则Hub在转发跨Hub组的IPv6 Spoke-Spoke私网数据报文的同时，会将报文与指定的ACL进行匹配。如果匹配成功，Hub会向相应的Spoke发送重定向报文；否则，不会发送重定向报文。

Spoke收到重定向报文后，将被重定向的数据报文的目的地址发送给VAM Server，向VAM Server查询连接该目的地址所在私网网段的Spoke节点的信息，并与该Spoke建立直连隧道。

跨Hub组Spoke-Spoke直连隧道建立前，数据报文仍由Hub进行转发。直连隧道建立后，数据报文将直接发送到直连路由下一跳所对应的Spoke，而不再经过Hub中转。

需要注意的是：

·如果指定的ACL不存在，则配置不生效。任何私网数据报文都不会触发Hub向Spoke发送重定向报文。

·对于IPv6基本ACL，本命令仅支持匹配源地址信息的规则；对于IPv6高级ACL，仅支持匹配协议类型、源地址、目的地址、源端口和目的端口信息的规则，并且不支持排除某个源/目的端口号的规则。

·如果本命令指定的ACL中包含不支持的规则，则该条ACL规则将不生效。

【举例】

\# 配置如果Spoke之间的报文匹配IPv6 ACL 3000，则允许建立跨Hub组的IPv6 Spoke-Spoke直连隧道。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 hub-group 1

Sysname-vam-server-domain-1-hub-group-1 shortcut ipv6 interest acl 3000

**ADVPN \-- VAM Server配置命令 \-- spoke ipv6 private-address**

------------------------------------------------------------------------

**[spoke ipv6 private-address**]命令用来配置Hub组内Spoke的IPv6私网地址范围。

**[undo spoke ipv6 private-address**]命令用来删除Hub组内Spoke的IPv6私网地址范围。

【命令】

**[spoke** **ipv6 private-address** [{ **network** *prefix prefix-length* \| **range** *start-ipv6-address end-ipv6-address* }]]

**[undo** **spoke** **ipv6** **private-address** [{ **network** *prefix prefix-length* \| **range** *start-ipv6-address end-ipv6-address* }]]

【缺省情况】

Hub组内没有配置Spoke的IPv6私网地址范围。

【视图】

Hub组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[network*** prefix prefix-length*]：指定子网网段形式的IPv6私网地址范围。*prefix*为IPv6地址前缀，*prefix-length*为IPv6地址前缀长度，取值范围为0～128。

**[range*** start-ipv6-address end-ipv6-address*]：指定地址段形式的IPv6私网地址范围。*start-ipv6-address*为地址段的起始IPv6地址，*end-ipv6-address*为地址段的结束IPv6地址。

【使用指导】

·Hub组内Spoke的IPv6私网地址范围可以指定为地址段形式或子网网段形式。以子网网段形式指定的IPv6私网地址范围，系统会自动将其转换为地址段形式。

·每个Hub组可以配置多个Spoke的IPv6私网地址范围，将按照地址从低到高的顺序排列。

·删除的私网地址范围必须和配置时的一致。

【举例】

\# 指定Hub组1内Spoke的IPv6私网地址范围为1000::/64。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 hub-group 1

Sysname-vam-server-domain-1-hub-group-1 spoke ipv6 private-address network 1000:: 64

**ADVPN \-- VAM Server配置命令 \-- spoke private-address**

------------------------------------------------------------------------

**[spoke private-address**]命令用来配置Hub组内Spoke的IPv4私网地址范围。

**[undo spoke private-address**]命令用来删除Hub组内Spoke的IPv4私网地址范围。

【命令】

**[spoke private-address **[{ **network** *ip-address* { *mask-length* \| *mask* } \| **range** *start-address end-address* }]]

**[undo spoke private-address **[{ **network** *ip-address* { *mask-length* \| *mask* } \| **range** *start-address end-address* }]]

【缺省情况】

Hub组内没有配置Spoke的IPv4私网地址范围。

【视图】

Hub组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[network*** ip-address*[ { *mask-length* \| *mask* }]]：指定子网网段形式的IPv4私网地址范围。*ip-address*为子网网段IPv4地址；*mask-length*为子网掩码长度，取值范围为0～32；*mask*为子网掩码。

**[range*** start-address end-address*]：指定地址段形式的IPv4私网地址范围。*start-address*为地址段的起始IPv4地址，*end-address*为地址段的结束IPv4地址。

【使用指导】

·Hub组内Spoke的IPv4私网地址范围可以指定为地址段形式或子网网段形式。以子网网段形式指定的IPv4私网地址范围，系统会自动将其转换为地址段形式。

·每个Hub组可以配置多个Spoke的IPv4私网地址范围，将按照地址从低到高的顺序排列。

·删除的私网地址范围必须和配置时的一致。

【举例】

\# 指定Hub组1内Spoke的IPv4私网地址范围为1.1.1.0/24。

\<Sysname\> system-view

Sysname vam server advpn-domain 1

Sysname-vam-server-domain-1 hub-group 1

Sysname-vam-server-domain-1-hub-group-1 spoke private-address network 1.1.1.0 255.255.255.0

**ADVPN \-- VAM Server配置命令 \-- vam server advpn-domain**

------------------------------------------------------------------------

**[vam server advpn-domain**]命令用来创建ADVPN域，并进入ADVPN域视图。如果ADVPN域已经存在，则直接进入该ADVPN域视图。

**[undo vam server advpn-domain**]命令用来删除指定ADVPN域。

【命令】

**[vam server advpn-domain ***domain-name* [ **id** *domain-id* ]]

**[undo vam server advpn-domain**] *domain-name*

【缺省情况】

设备上不存在任何ADVPN域。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。

**[id** *domain-id*]：指定ADVPN域的ID。*domain-id*为ADVPN域的ID，取值范围为1～65535。

【使用指导】

·创建ADVPN域时必须指定ADVPN域的ID。若要进入已存在的ADVPN域的视图，可以不指定其域ID。

·不同的ADVPN域必须使用不同的域ID。

【举例】

\# 创建ADVPN域1，ID为1，并进入其视图。

\<Sysname\> system-view

Sysname vam server advpn-domain 1 id 1

Sysname-vam-server-domain-1

**ADVPN \-- VAM Server配置命令 \-- vam server enable**

------------------------------------------------------------------------

**[vam server enable**]命令用来启动所有或指定ADVPN域的VAM Server功能。

**[undo vam server enable**]命令用来关闭所有或指定ADVPN域的VAM Server功能。

【命令】

**[vam** **server** **enable** [ **advpn-domain** *domain-name* ]]

**[undo** **vam** **server** **enable** [ **advpn-domain** *domain-name* ]]

【缺省情况】

ADVPN域的VAM Server功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advpn-domain ***domain-name*]：启动指定ADVPN域的VAM Server功能。*domain-name*为ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A～Z、a～z、0～9和"."。如果未指定本参数，则启动所有ADVPN域的VAM Server功能。

【使用指导】

除了执行本命令外，还可以在ADVPN域视图下通过**server** **enable**命令来启动相应ADVPN域的VAM Server功能。

【举例】

\# 启动所有ADVPN域的VAM Server功能。

\<Sysname\> system-view

Sysname vam server enable

\# 启动ADVPN域1的VAM Server功能。

\<Sysname\> system-view

Sysname vam server enable advpn-domain 1

【相关命令】

·**server ****enable**

**ADVPN \-- VAM Server配置命令 \-- vam server listen-port**

------------------------------------------------------------------------

**[vam server listen-port**]命令用来配置VAM Server的监听端口号。

**[undo vam server listen-port**]命令用来恢复缺省情况。

【命令】

**[vam server listen-port** *port-number* ]

**[undo vam server listen-port**]

【缺省情况】

VAM Server的监听端口号为18000。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：VAM Server监听的端口号，取值范围为1025～65535。

【使用指导】

VAM Server的监听端口号与VAM Client上指定的VAM Server的端口号必须一致。

【举例】

\# 配置VAM Server的监听端口号为10000。

\<Sysname\> system-view

Sysname vam server listen-port 10000

【相关命令】

·**server primary**

·**server secondary**

**ADVPN \-- VAM Client配置命令 \-- advpn-domain**

------------------------------------------------------------------------

**[advpn-domain**]命令用来配置VAM Client所属的ADVPN域。

**[undo advpn-domain**]命令用来删除VAM Client所属的ADVPN域。

【命令】

**[advpn-domain** *domain-name*]

**[undo advpn-domain**]

【缺省情况】

VAM Client不属于任何ADVPN域。

【视图】

VAM Client视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：ADVPN域的名称，为1～31个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。

【使用指导】

多个VAM Client可以属于同一个ADVPN域。

【举例】

\# 配置VAM Client abc属于ADVPN域100。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc advpn-domain 100

**ADVPN \-- VAM Client配置命令 \-- client enable**

------------------------------------------------------------------------

**[client enable**]命令用来启动指定VAM Client的VAM Client功能。

**[undo client enable**]命令用来关闭指定VAM Client的VAM Client功能。

【命令】

**[client enable**]

**[undo client enable**]

【缺省情况】

VAM Client的VAM Client功能处于关闭状态。

【视图】

VAM Client视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

还可以在系统视图下通过**vam client enable**命令来启动所有或指定VAM Client的VAM Client功能。

【举例】

\# 启动VAM Client abc的VAM Client功能。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc client enable

【相关命令】

·**vam client enable**

**ADVPN \-- VAM Client配置命令 \-- display vam client fsm**

------------------------------------------------------------------------

**[display vam client fsm**]命令用来显示VAM Client的状态机信息。

【命令】

**[display** **vam** **client** **fsm** [ **name** *client-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***client-name*]：显示指定VAM Client的状态机信息。*client-name*为VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。如果未指定本参数，则显示所有VAM Client的状态机信息。

【使用指导】

需要注意的是，一些没有配置的命令参数，或者未能动态获取的信息将不会出现在本命令的显示信息中。

【举例】

\# 显示所有VAM Client的状态机信息。

\<Sysname\> display vam client fsm

Client name      : abc

Status           : Enabled

ADVPN domain name: 1

  Primary server: abc.com (28.1.1.23)

    Private address: 10.0.0.12

    Interface      : Tunnel1

      Current state           : Online (active)

      Client type             : Hub

      Holding time            : 9H 20M 30S

      Encryption algorithm    : AES-CBC-128

      Authentication algorithm: SHA1

      Keepalive               : 30 seconds, 3 times

      Number of hubs          : 1

    Private address: 1000::22

    Interface      : Tunnel2

      Current state           : Online (active)

      Client type             : Spoke

      Holding time            : 9H 20M 30S

      Encryption algorithm    : AES-CBC-128

      Authentication algorithm: SHA1

      Keepalive               : 30 seconds, 3 times

      Number of hubs          : 1

  Secondary server: 2811::24

    Private address: 10.0.0.12

    Interface      : Tunnel1

      Current state           : Offline

      Client type             : Unknown

      Holding time            : 0H 0M 0S

      Encryption algorithm    : AES-CBC-128

      Authentication algorithm: SHA1

      Keepalive               : 0 seconds, 0 times

      Number of hubs          : 0

    Private address: 1000::22

    Interface      : Tunnel2

      Current state           : Offline

      Client type             : Unknown

      Holding time            : 0H 0M 0S

      Encryption algorithm    : AES-CBC-128

      Authentication algorithm: SHA1

      Keepalive               : 0 seconds, 0 times

      Number of hubs          : 0

Client name      : hub

Status           : Enabled

ADVPN domain name: 2

  Primary server: 202.159.36.24

    Private address: 10.0.0.12

    Interface      : Tunnel20

      Current state           : Online (active)

      Client type             : Hub

      Holding time            : 0H 0M 47S

      Encryption algorithm    : AES-CBC-128

      Authentication algorithm: SHA1

      Keepalive               : 30 seconds, 3 times

      Number of hubs          : 1

Client name      : spoke

Status           : Disabled

ADVPN domain name:

表1-8 display vam client fsm命令显示信息描述表

字段

描述

Client name

VAM Client的名称

Status

VAM Client的状态，包括：

·Enabled

·Disabled

ADVPN domain name

该VAM Client所在的ADVPN域名

Primary server

主VAM Server的公网地址

Private address

VAM Client注册的私网地址

Interface

与该VAM Client绑定的ADVPN隧道接口

Current state

VAM Client当前状态，包括：

·Offline：离线状态

·Init：连接初始化阶段

·Reg：注册阶段

·Online：在线状态

·Dumb：静默状态

Client type

VAM Client类型，包括：

·Hub

·Spoke

·Unknown

Holding time

VAM Client维持当前状态的时间，为x小时y分z秒（xH yM zS）

Encryption algorithm

协商使用的加密算法

Authentication algorithm

协商使用的认证算法

Keepalive

VAM Server下发的Keepalive时间间隔（单位为秒）和重发次数

Number of hubs

VAM Server下发的Hub数量

Secondary server

备VAM Server的公网地址

【相关命令】

·**reset vam client fsm**

**ADVPN \-- VAM Client配置命令 \-- display vam client shortcut interest**

------------------------------------------------------------------------

**[display** **vam** **client** **shortcut** **interest**]命令用来显示VAM Client收到的VAM Server下发的跨Hub组建立IPv4 Spoke-Spoke直连隧道的规则。

【命令】

**[display** **vam** **client** **shortcut** **interest** [ **name** *client-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***client-name*]：显示指定VAM Client收到的规则。*client-name*为VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。如果未指定本参数，则显示所有VAM Client收到的规则。

【使用指导】

VAM Server仅给Hub下发跨Hub组建立IPv4 Spoke-Spoke直连隧道的规则。如果指定的VAM Client为Spoke，则下发的规则数为0。

【举例】

\# 显示所有VAM Client收到的跨Hub组建立IPv4 Spoke-Spoke直连隧道的规则。

\<Sysname\> display vam client shortcut interest

Client name      : abc

ADVPN domain name: 1

Client type      : Spoke

ACL rules        : 0

Client name      : hub

ADVPN domain name: 2

Client type      : Hub

ACL rules        : 2

  Rule 1: Permit

    Protocol   : 6 (TCP)

    Source     : Address 0.0.0.0-255.255.255.255, port 0-65535

    Destination: Address 192.168.114.100-192.168.114.200, port 10000-20000

  Rule 2: Deny

    Protocol   : 0 (IP)

    Source     : Address 0.0.0.0-255.255.255.255, port 0-65535

    Destination: Address 0.0.0.0-255.255.255.255, port 0-65535

Client name      : spoke

ADVPN domain name: 3

Client type      : Unknown

ACL rules        : 0

\# 显示VAM Client abc收到的跨Hub组建立IPv4 Spoke-Spoke直连隧道的规则。

\<Sysname\> display vam client shortcut interest name abc

Client name      : abc

ADVPN domain name: 1

Client type      : Spoke

ACL rules        : 0

表1-9 display vam client shortcut interest命令显示信息描述表

字段

描述

Client name

VAM Client的名称

ADVPN domain name

该VAM Client所在的ADVPN域名

Client type

VAM Client类型，包括：

·Hub

·Spoke

·Unknown

ACL rules

VAM Client收到的匹配规则计数

Rule *n*: Operation

ACL规则的编号（*n*）和动作（*Operation*）。*Operation*包括：

·Permit：允许建立跨Hub组IPv4 Spoke-Spoke直连隧道

·Deny：不允许建立跨Hub组IPv4 Spoke-Spoke直连隧道

·Discard：丢弃该报文

Protocol

匹配指定的协议类型

Source

匹配指定范围的源IP地址和源端口号

Destination

匹配指定范围的目的IP地址和目的端口号

**ADVPN \-- VAM Client配置命令 \-- display vam client shortcut ipv6 interest**

------------------------------------------------------------------------

**[display** **vam** **client** **shortcut** **ipv6** **interest**]命令用来显示VAM Client收到VAM Server下发的跨Hub组建立IPv6 Spoke-Spoke直连隧道的规则。

【命令】

**[display** **vam** **client** **shortcut** **ipv6** **interest** [ **name** *client-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***client-name*]：显示指定VAM Client收到的规则。*client-name*为VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。如果未指定本参数，则显示所有VAM Client收到的规则。

【使用指导】

VAM Server仅给Hub下发跨Hub组建立IPv6 Spoke-Spoke直连隧道的规则。如果指定的VAM Client为Spoke，则下发的规则数为0。

【举例】

\# 显示所有VAM Client收到的跨Hub组建立IPv6 Spoke-Spoke直连隧道的规则。

\<Sysname\> display vam client shortcut ipv6 interest

Client name      : abc

ADVPN domain name: 1

Client type      : Spoke

ACL rules         : 0

Client name      : hub

ADVPN domain name: 2

Client type      : Hub

ACL rules        : 2

  Rule 1: Permit

    Protocol                 : TCP

    Start source address     : 0::0

    End source address       : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF

    Start source port        : 0

    End source port          : 65535

    Start destination address: 2000::0

    End destination address  : 2000:1::0

    Start destination port   : 0

    End destination port     : 65535

  Rule 2: Deny

    Protocol                 : All

    Start source address     : 0::0

    End source address       : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF

    Start source port        : 0

    End source port          : 65535

    Start destination address: 0::0

    End destination address  : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF

    Start destination port   : 0

    End destination port     : 65535

Client name      : spoke

ADVPN domain name:

Client type      : Unknown

ACL rules        : 0

\# 显示VAM Client abc收到的跨Hub组建立IPv6 Spoke-Spoke直连隧道的规则。

\<Sysname\> display vam client shortcut ipv6 interest name abc

Client name      : spoke

ADVPN domain name:

Client type      : Unknown

ACL rules        : 0

表1-10 display vam client shortcut ipv6 interest命令显示信息描述表

字段

描述

Client name

VAM Client的名称

ADVPN domain name

该VAM Client所在的ADVPN域名

Client type

VAM Client类型，包括：

·Hub

·Spoke

·Unknown

ACL rules

VAM Client收到的匹配规则计数

Rule *n*: operation

ACL规则的编号（*n*）和动作（*Operation*）。*Operation*包括：

·Permit：允许建立跨Hub组IPv6 Spoke-Spoke直连隧道

·Deny：不允许建立跨Hub组IPv6 Spoke-Spoke直连隧道

·Discard：丢弃该报文

Protocol

匹配指定的协议类型

Start source address

匹配的源IPv6地址范围的起始地址

End source address

匹配的源IPv6地址范围的结束地址

Start source port

匹配的源端口范围的起始端口号

End source port

匹配的源端口范围的结束端口号

Start destination address

匹配的目的IPv6地址范围的起始地址

End destination address

匹配的目的IPv6地址范围的结束地址

Start destination port

匹配的目的端口范围的起始端口号

End destination port

匹配的目的端口范围的结束端口号

**ADVPN \-- VAM Client配置命令 \-- display vam client statistics**

------------------------------------------------------------------------

**[display vam client statistics**]命令用来显示VAM Client的统计信息。

【命令】

**[display** **vam** **client** **statistics** [ **name** *client-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***client-name*]：显示指定VAM Client的统计信息。*client-name*为VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。如果未指定本参数，则显示所有VAM Client的统计信息。

【举例】

\# 显示所有VAM Client的统计信息。

\<Sysname\> display vam client statistics

Client name: abc

 Status     : Enabled

  Primary server: abc.com

    Packets sent:

      Initialization request        : 1

      Initialization complete       : 1

      Register request              : 1

      Authentication information    : 1

      Address resolution request    : 9

      Network registration request  : 0

      Update request                : 0

      Logout request                : 0

      Hub information response      : 0

      Data flow information response: 0

      Keepalive                     : 35

      Error notification            : 0

    Packets received:

      Initialization response      : 1

      Initialization complete      : 1

      Authentication request       : 1

      Register response            : 1

      Address resolution response  : 9

      Network registration response: 0

      Update response              : 0

      Hub information request      : 0

      Data flow information request: 0

      Logout response              : 0

      Keepalive                    : 35

      Error notification           : 0

      Unkonwn                      : 0

  Secondary server: 28.1.1.24

    Packets sent:

      Initialization request        : 15

      Initialization complete       : 0

      Register request              : 0

      Authentication information    : 0

      Address resolution request    : 0

      Network registration request  : 0

      Update request                : 0

      Logout request                : 0

      Hub information response      : 0

      Data flow information response: 0

      Keepalive                     : 0

      Error notification            : 0

    Packets received:

      Initialization response      : 0

      Initialization complete      : 0

      Register response            : 0

      Authentication request       : 0

      Address resolution response  : 0

      Network registration response: 0

      Update response              : 0

      Hub information request      : 0

      Data flow information request: 0

      Logout response              : 0

      Keepalive                    : 0

      Error notification           : 0

      Unkonwn                      : 0

Client name: hub

Status     : Disabled

Client name: spoke

Status     : Enabled

  Primary server: test.com

    Packets sent:

      Initialization request        : 3

      Initialization complete       : 3

      Register request              : 3

      Authentication information    : 3

      Address resolution request    : 0

      Network registration request  : 0

      Update request                : 0

      Logout request                : 0

      Hub information response      : 0

      Data flow information response: 0

      Keepalive                     : 124

      Error notification            : 0

    Packets received:

      Initialization response      : 3

      Initialization complete      : 3

      Authentication request       : 3

      Register response            : 3

      Address resolution response  : 0

      Network registration response: 0

      Update response              : 0

      Hub information request      : 0

      Data flow information request: 0

      Logout response              : 0

      Keepalive                    : 114

      Error notification           : 0

      Unkonwn                      : 0

\# 显示VAM Client abc的统计信息。

\<Sysname\> display vam client statistics name abc

Client name: abc

Status     : Enabled

  Primary server: abc.com

    Packets sent:

      Initialization request        : 1

      Initialization complete       : 1

      Register request              : 1

      Authentication information    : 1

      Address resolution request    : 9

      Network registration request  : 0

      Update request                : 0

      Logout request                : 0

      Hub information response      : 0

      Data flow information response: 0

      Keepalive                     : 35

      Error notification            : 0

    Packets received:

      Initialization response      : 1

      Initialization complete      : 1

      Authentication request       : 1

      Register response            : 1

      Address resolution response  : 9

      Network registration response: 0

      Update response              : 0

      Hub information request      : 0

      Data flow information request: 0

      Logout response              : 0

      Keepalive                    : 35

      Error notification           : 0

      Unkonwn                      : 0

  Secondary server: 28.1.1.24

    Packets sent:

      Initialization request        : 15

      Initialization complete       : 0

      Register request              : 0

      Authentication information    : 0

      Address resolution request    : 0

      Network registration request  : 0

      Update request                : 0

      Logout request                : 0

      Hub information response      : 0

      Data flow information response: 0

      Keepalive                     : 0

      Error notification            : 0

    Packets received:

      Initialization response      : 0

      Initialization complete      : 0

      Register response            : 0

      Authentication request       : 0

      Address resolution response  : 0

      Network registration response: 0

      Update response              : 0

      Hub information request      : 0

      Data flow information request: 0

      Logout response              : 0

      Keepalive                    : 0

      Error notification           : 0

      Unkonwn                      : 0

表1-11 display vam client statistic命令显示信息描述表

字段

描述

Client name

VAM Client的名称

Status

VAM Client的状态，包括：

·Enabled

·Disabled

Primary server

主VAM Server的公网地址或域名

Secondary server

备VAM Server的公网地址或域名

Packets sent

向VAM Server发送的报文数目

Initialization request

向VAM Server发送的初始化请求报文数目

Initialization complete

向VAM Server发送的初始化完成报文数目

Register request

向VAM Server发送的注册请求报文数目

Authentication information

向VAM Server发送的认证信息报文数目

Address resolution request

向VAM Server发送的地址解析请求报文数目

Network registration request

向VAM Server发送的私网注册请求报文数目

Update request

向VAM Server发送的节点更新请求报文数目

Logout request

向VAM Server发送的清除请求报文数目

Hub information response

向VAM Server发送的Hub信息响应报文数目

Data flow information response

向VAM Server发送的数据流信息响应报文数目

Keepalive

向VAM Server发送的Keepalive报文数目

Error notification

向VAM Server发送的错误通知报文数目

Unkonwn

向VAM Server发送的未知报文或错误报文数目

Packets received

从VAM Server接收的报文数目

Initialization response

从VAM Server接收的初始化响应报文数目

Initialization complete

从VAM Server接收的初始化完成报文数目

Authentication request

从VAM Server接收的认证请求报文数目

Register response

从VAM Server接收的注册响应报文数目

Address resolution response

从VAM Server接收的地址解析响应报文数目

Network registration response

从VAM Server接收的私网注册响应报文数目

Update response

从VAM Server接收的节点更新响应报文数目

Hub information request

从VAM Server接收的Hub信息请求报文数目

Data flow information request

从VAM Server接收的数据流信息请求报文数目

Logout response

从VAM Server接收的清除响应报文数目

Keepalive

从VAM Server接收的Keepalive报文数目

Error notification

从VAM Server接收的错误通知报文数目

【相关命令】

·**reset vam client ****statistics**

**ADVPN \-- VAM Client配置命令 \-- dumb-time**

------------------------------------------------------------------------

**[dumb-time**]命令用来配置VAM Client连接超时的静默时间。

**[undo dumb-time**]命令用来恢复缺省情况。

【命令】

**[dumb-time** *time-interval*]

**[undo dumb-time**]

【缺省情况】

VAM Client连接超时的静默时间为120秒。

【视图】

VAM Client视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-interval*]：VAM Client连接超时的静默时间，取值范围为10～600，单位为秒。

【使用指导】

VAM Client在与VAM Server连接超时后，会进入静默状态，此时VAM Client不处理任何报文。当静默时间到达后，VAM Client将重新上线。

【举例】

\# 配置VAM Client的静默时间为100秒。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc dumb-time 100

**ADVPN \-- VAM Client配置命令 \-- pre-shared-key (VAM Client view)**

------------------------------------------------------------------------

**[pre-shared-key**]命令用来配置VAM Client的预共享密钥。

**[undo pre-shared-key**]命令用来删除VAM Client的预共享密钥。

【命令】

**[pre-shared-key**[ { **cipher** *cipher-string* \| **simple** *simple-string* }]]

**[undo pre-shared-key**]

【缺省情况】

未配置VAM Client的预共享密钥。

【视图】

VAM Client视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher*** cipher-string*]：以密文方式设置预共享密钥。*cipher-string*为密文预共享密钥，为1～73个字符的密文字符串，区分大小写。

**[simple*** simple-string*]：以明文方式设置预共享密钥。*simple-string*为明文预共享密钥，为1～31个字符的明文字符串，区分大小写。

【使用指导】

预共享密钥是VAM Server用来和VAM Client建立安全通道的公共密钥材料。在连接初始化阶段预共享密钥用来生成验证和加密连接请求、连接响应报文的初始密钥；如果选择对后续的报文进行加密和验证，则预共享密钥还用来生成验证和加密后续报文的连接密钥。

需要注意的是：

·同一个ADVPN域内的VAM Client和VAM Server上配置的预共享密钥必须一致。

·以明文或密文形式设置的预共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 以明文方式配置VAM Client的预共享密钥为123。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc pre-shared-key simple 123

【相关命令】

·**vam client name**

·**pre-shared-key** (ADVPN domain view)

**ADVPN \-- VAM Client配置命令 \-- reset vam client fsm**

------------------------------------------------------------------------

**[reset vam client fsm**]命令用来重置VAM Client的状态机。

【命令】

**[reset** **vam** **client** **fsm** [ **name** *client-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[name ***client-name*]：重置指定VAM Client的状态机。*client-name*为VAM Client的名称，为1～63个字符的字符串，不区分大小写。只能包含字符A-Z、a-z、0-9和"."。如果未指定本参数，则重置所有VAM Client的状态机。

【使用指导】

VAM Client的状态机重置后，会立刻尝试重新上线。

【举例】

\# 重置VAM Client abc的状态机。

\<Sysname\> reset vam client fsm name abc

\# 重置所有VAM Client的状态机。

\<Sysname\> reset vam client fsm

【相关命令】

·**display vam client fsm**

**ADVPN \-- VAM Client配置命令 \-- reset vam client ipv6 fsm**

------------------------------------------------------------------------

**[reset vam client ipv6 fsm**]命令用来重置IPv6 VAM Client的状态机。

【命令】

**[reset** **vam** **client** **ipv6** **fsm** [ **name** *client-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

【参数】

**[name ***client-name*]：重置指定IPv6 VAM Client的状态机。*client-name*为VAM Client的名称，为1～63个字符的字符串，不区分大小写。只能包含字符A-Z、a-z、0-9和"."。如果未指定本参数，则重置所有IPv6 VAM Client的状态机。

【使用指导】

VAM Client的状态机重置后，会立刻尝试重新上线。

【举例】

\# 重置IPv6 VAM Client abc的状态机。

\<Sysname\> reset vam client ipv6 fsm name abc

\# 重置所有IPv6 VAM Client的状态机。

\<Sysname\> reset vam client ipv6 fsm

【相关命令】

·**display vam client fsm**

**ADVPN \-- VAM Client配置命令 \-- reset vam client statistics**

------------------------------------------------------------------------

**[reset vam client statistic**]命令用来清除VAM Client的统计信息。

【命令】

**[reset** **vam** **client** **statistics** [ **name** *client-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name ***client-name*]：清除指定VAM Client的统计信息。*client-name*为VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。如果未指定本参数，则清除所有VAM Client的统计信息。

【举例】

\# 清除VAM Client abc的统计信息。

\<Sysname\> reset vam client statistics name abc

\# 清除所有VAM Client的统计信息。

\<Sysname\> reset vam client statistics

【相关命令】

·**display vam client ****statistics**

**ADVPN \-- VAM Client配置命令 \-- retry**

------------------------------------------------------------------------

**[retry**]命令用来设置VAM Client重发请求报文的时间间隔和重发次数。

**[undo retry**]命令用来恢复缺省情况。

【命令】

**[retry interval** *time-interval* **count** *retry-times*]

**[undo retry**]

【缺省情况】

请求报文的重发时间间隔为5秒，重发次数为3次。

【视图】

VAM Client视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval** *time-interval*]：请求报文的重发时间间隔，取值范围为3～30，单位为秒。

**[count** *retry-times*]：请求报文的重发次数，取值范围为1～6。

【使用指导】

VAM Client向VAM Server发送请求报文后，如果在指定的时间间隔内没有收到响应报文，VAM Client将重新发送请求报文。如果重新发送请求报文的次数超过指定的重发次数，则VAM Client认为VAM Server不可达。

需要注意的是：

·私网注册请求报文和节点信息更新请求报文不受重发次数的限制，将会按照指定的时间间隔一直发送，直至VAM Client下线。

·VAM Client发送Keepalive报文的时间间隔和重发次数由VAM Server的配置决定。

【举例】

\# 设置VAM Client重发请求报文的时间间隔为20秒，重发次数为4次。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc retry interval 20 count 4

**ADVPN \-- VAM Client配置命令 \-- server primary**

------------------------------------------------------------------------

**[server primary**]命令用来配置主VAM Server的地址。

**[undo server primary**]命令用来恢复缺省情况。

【命令】

**[server primary**[ [ *ip-address* \| **ipv6-address** *ipv6-address* \| **name** *host-name* } [ **port** *port-number* ]]]

**[undo server primary**]

【缺省情况】]

没有配置主VAM Server的地址。

【视图】

VAM Client视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-address** *ip-address*]：主VAM Server的公网IP地址，该地址必须是单播地址。

**[ipv6-address** *ipv6-address*]：主VAM Server的公网IPv6地址，该地址必须是全球单播地址。

**[name** *host-name*]：主VAM Server的域名，由以"."分隔的字符串组成，每个字符串的长度不超过63个字符，包括"."在内的总长度不超过253个字符，不区分大小写，字符串中可以包含字母、数字、"-"及"\_"。

**[port** *port-number*]：主VAM Server的端口号，取值范围为1025～65535，缺省值为18000。

【使用指导】

·重复执行本命令，新的配置将覆盖原有配置。

·VAM Client上指定的VAM Server的端口号，则必须和VAM Server上通过**vam server listen-port**命令配置的监听端口号一致。

·如果主VAM Server和备VAM Server的地址相同（配置了相同的地址或通过域名解析到相同的地址），则只有主VAM Server有效。

【举例】

\# 指定主VAM Server的域名为abc.com，端口号为2000。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc server primary name abc.com port 2000

\# 指定主VAM Server的公网IP地址为1.1.1.1，端口号为2000。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc server primary ip-address 1.1.1.1 port 2000

\# 指定主VAM Server的公网IPv6地址为1001::1，端口号为2000。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc server primary ipv6-address 1001::1 port 2000

【相关命令】

·**server secondary**

**ADVPN \-- VAM Client配置命令 \-- server secondary**

------------------------------------------------------------------------

**[server secondary**]命令用来配置备VAM Server的地址。

**[undo server secondary**]命令用来恢复缺省情况。

【命令】

**[server secondary**[ [ *ip-address* \| **ipv6-address** *ipv6-address* \| **name** *host-name* } [ **port** *port-number* ]]]

**[undo server secondary**]

【缺省情况】]

没有配置备VAM Server的地址。

【视图】

VAM Client视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip-address*** ip-address*]：备VAM Server的公网IP地址，该地址必须是单播地址。

**[ipv6-address*** ipv6-address*]：备VAM Server的公网IPv6地址，该地址必须是全球单播地址。

**[name** *host-name*]：备VAM Server的域名，由以"."分隔的字符串组成，每个字符串的长度不超过63个字符，包括"."在内的总长度不超过253个字符，不区分大小写，字符串中可以包含字母、数字、"-"及"\_"。

**[port** *port-number*]：备VAM Server的端口号，取值范围为1025～65535，缺省值为18000。

【使用指导】

·重复执行本命令，新的配置将覆盖原有配置。

·VAM Client上指定的VAM Server的端口号，则必须和VAM Server上通过**vam server listen-port**命令配置的监听端口号一致。

·如果主VAM Server和备VAM Server的地址相同（配置了相同的地址或通过域名解析到相同的地址），则只有主VAM Server有效。

【举例】

\# 指定备VAM Server的域名为abc.com，端口号为2000。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc server secondary name abc.com port 2000

\# 指定备VAM Server的公网IP地址为1.1.1.2，端口号为3000。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc server secondary ip-address 1.1.1.2 port 3000

\# 指定备VAM Server的公网IPv6地址为1001::2，端口号为3000。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc server secondary ipv6-address 1001::2 port 3000

【相关命令】

·**server primary**

**ADVPN \-- VAM Client配置命令 \-- user**

------------------------------------------------------------------------

**[user**]命令用来配置认证用户名和密码。

**[undo user**]命令用来取消配置的认证用户名和密码。

【命令】

**[user**[ *username* **password** { **cipher** *cipher-string* \| **simple** *simple-string* }]]

**[undo user**]

【缺省情况】

没有配置认证用户名和密码。

【视图】

VAM Client视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：认证用户名，为1～253个字符的字符串，区分大小写，不能包括"/"、"\"、":"、"\*"、"?"、"\<"、"\>"、"""、"[\|]"以及"@"字符。

**[password**]：设置用户密码。

**[cipher*** cipher-string*]：以密文方式设置用户密码。*cipher-string*为密文用户密码，为1～117个字符的密文字符串，区分大小写。

**[simple*** simple-string*]：以明文方式设置用户密码。*simple-string*为明文用户密码，为1～63个字符的明文字符串，区分大小写。

【使用指导】

VAM Client的用户名和密码，用于向VAM Server进行身份认证。

需要注意的是：

·一个VAM Client下只允许配置一个认证用户。

·以明文或密文形式设置的用户密码，均以密文的方式保存在配置文件中。

【举例】

\# 设置VAM Client abc的认证用户名为user，以明文方式设置用户密码为user。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc user user password simple user

**ADVPN \-- VAM Client配置命令 \-- vam client enable**

------------------------------------------------------------------------

**[vam client enable**]命令用来启动所有或指定VAM Client的VAM Client功能。

**[undo vam client enable**]命令用来关闭所有或指定VAM Client的VAM Client功能。

【命令】

**[vam client enable** [ **name** *client-name* ]]

**[undo vam client enable** [ **name** *client-name* ]]

【缺省情况】

VAM Client的VAM Client功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name ***client-name*]：启动指定VAM Client的VAM Client功能。*client-name*为VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。如果未指定本参数，启动所有VAM Client的VAM Client功能。

【使用指导】

还可以在VAM Client视图下通过**client** **enable**命令来启动相应VAM Client的VAM Client功能。

【举例】

\# 启动所有VAM Client的VAM Client功能。

\<Sysname\> system-view

Sysname vam client enable

\# 启动VAM Client abc的VAM Client功能。

\<Sysname\> system-view

Sysname vam client enable name abc

【相关命令】

·**client enable**

**ADVPN \-- VAM Client配置命令 \-- vam client name**

------------------------------------------------------------------------

**[vam client name**]命令用来创建VAM Client，并进入VAM Client视图。如果VAM Client已经存在，则直接进入该VAM Client视图。

**[undo vam client name**]命令用来删除指定的VAM Client。

【命令】

**[vam client name ***client-name*]

**[undo vam client name** *client-name*]

【缺省情况】

没有配置VAM Client。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[client-name*]：VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。

【举例】

\# 创建一个名为abc的VAM Client，并进入VAM Client视图。

\<Sysname\> system-view

Sysname vam client name abc

Sysname-vam-client-abc

**ADVPN \-- ADVPN隧道配置命令 \-- advpn ipv6 network**

------------------------------------------------------------------------

**[advpn ipv6 network**]命令用来添加ADVPN隧道的IPv6私网信息。

**[undo advpn ipv6 network**]命令用来删除ADVPN隧道的IPv6私网信息。

【命令】

**[advpn ipv6 network** *prefix prefix-length* [ **preference** *preference-value* ]]

**[undo advpn ipv6 network** *prefix prefix-length*]

【缺省情况】

没有配置ADVPN隧道的IPv6私网信息。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prefix prefix-length*]：ADVPN隧道的私网IPv6地址前缀及前缀长度。*prefix-length*取值范围为0～128。

**[preference** *preference-value*]：ADVPN隧道私网路由优先级，取值范围为1～255，缺省值为8。

【使用指导】

VAM Client向VAM Server注册ADVPN隧道的私网信息。其他VAM Client向VAM Server解析私网报文目的地址时，如果解析的地址属于注册私网，则VAM Server将注册VAM Client的节点信息返回给查询方。

需要注意的是：

·本命令只有在IPv6 ADVPN类型的Tunnel接口下才能配置。

·只有在Tunnel接口上配置了IPv6地址，并通过**vam** **ipv6** **client**命令指定了接口引用的VAM Client后，本命令才会生效。

·每个Tunnel接口下可以配置多个IPv6私网信息。

·私网路由的优先级建议高于其他动态路由协议，且低于静态路由。优先级数值越大，优先级越低。

【举例】

\# 给接口Tunnel1增加IPv6私网信息1001::/64，私网路由优先级为20。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn udp ipv6

Sysname-Tunnel1 advpn ipv6 network 1001:: 64 preference 20

【相关命令】

·**vam ipv6 client**

**ADVPN \-- ADVPN隧道配置命令 \-- advpn network**

------------------------------------------------------------------------

**[advpn network**]命令用来添加ADVPN隧道的IPv4私网信息。

**[undo advpn network**]命令用来删除ADVPN隧道的IPv4私网信息。

【命令】

**[advpn network**[ *ip-address* { *mask-length* \| *mask* } [ **preference** *preference-value* ]]]

**[undo advpn network**[ *ip-address* { *mask-length* \| *mask* }]]

【缺省情况】

没有配置ADVPN隧道的IPv4私网信息。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：ADVPN隧道的IPv4私网网段地址。

*[mask-length*]：ADVPN隧道的私网网段掩码长度，取值范围为0～32。

*[mask*]：ADVPN隧道的私网网段掩码。

**[preference** *preference-value*]：ADVPN隧道的私网路由优先级，取值范围为1～255，缺省值为8。

【使用指导】

VAM Client向VAM Server注册ADVPN隧道的私网信息。其他VAM Client向VAM Server解析私网报文目的地址时，如果解析的地址属于注册私网，则VAM Server将注册VAM Client的节点信息返回给查询方。

需要注意的是：

·本命令只有在IPv4 ADVPN类型的Tunnel接口下才能配置。

·只有在Tunnel接口上配置了IPv4地址，并通过**vam** **client**命令指定了接口引用的VAM Client后，本命令才会生效。

·每个Tunnel接口下可以配置多个IPv4私网信息。

·私网路由的优先级建议高于其他动态路由协议，且低于静态路由。优先级数值越大，优先级越低。

【举例】

\# 给接口Tunnel1增加IPv4私网信息10.0.5.0 255.255.255.0，私网路由优先级为20。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn udp ipv4

Sysname-Tunnel1 advpn network 10.0.5.0 255.255.255.0 preference 20

【相关命令】

·**vam client**

**ADVPN \-- ADVPN隧道配置命令 \-- advpn session dumb-time**

------------------------------------------------------------------------

**[advpn session dumb-time**]命令用来配置ADVPN隧道建立失败的静默时间。

**[undo advpn session dumb-time**]命令用来恢复缺省情况。

【命令】

**[advpn session dumb-time** *time-interval*]

**[undo advpn session dumb-time**]

【缺省情况】

ADVPN隧道建立失败的的静默时间为120秒。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-interval*]：ADVPN隧道建立失败的的静默时间，取值范围为10～600，单位为秒。

【使用指导】

·本命令只有在ADVPN类型的Tunnel接口下才能配置。

·修改此参数对已经建立的ADPVN隧道没有影响，之后建立的ADPVN隧道会使用修改后的参数值。

【举例】

\# 配置ADVPN隧道建立失败的的静默时间为100秒。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn udp ipv4

Sysname-Tunnel1 advpn session dumb-time 100

**ADVPN \-- ADVPN隧道配置命令 \-- advpn session idle-time**

------------------------------------------------------------------------

**[advpn session idle-time**]命令用来配置Spoke-Spoke类型ADVPN隧道的空闲超时时间。

**[undo advpn session idle-time**]命令用来恢复缺省情况。

【命令】

**[advpn session idle-time** *time-interval*]

**[undo advpn session idle-time**]

【缺省情况】

Spoke-Spoke类型ADVPN隧道的空闲超时时间为600秒。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-interval*]：Spoke-Spoke类型ADVPN隧道的空闲超时时间，取值范围为60～65535，单位为秒。

【使用指导】

·本命令只有在ADVPN类型的Tunnel接口下才能配置。

·如果修改此参数，已经建立的Spoke-Spoke类型ADVPN隧道会使用修改后的参数值重新开始计时。

·如果在空闲超时时间内，Spoke-Spoke类型ADVPN隧道上没有数据传输，则断开该隧道。

【举例】

\# 配置Spoke-Spoke类型ADVPN隧道的空闲超时时间为800秒。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn udp ipv4

Sysname-tunnel1 advpn session idle-time 800

**ADVPN \-- ADVPN隧道配置命令 \-- advpn source-port**

------------------------------------------------------------------------

**[advpn source-port**]命令用来配置ADVPN报文的源UDP端口号。

**[undo advpn source-port**]命令用来恢复缺省情况。

【命令】

**[advpn source-port ***port-number*]

**[undo advpn sourc-port**]

【缺省情况】

ADVPN报文的源UDP端口号为18001。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：端口号，取值范围为1025～65535。

【使用指导】

·本命令只有在UDP封装模式的ADVPN类型的Tunnel接口下才能配置。

·如果Tunnel接口下通过**vam client**命令配置了**compatible**参数，则该Tunnel接口配置的源端口号不能和其他Tunnel接口的源端口号相同。

【举例】

\# 配置ADVPN报文的源UDP端口号为6000。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn udp ipv4

Sysname-Tunnel1 advpn source-port 6000

【相关命令】

·**vam client**

**ADVPN \-- ADVPN隧道配置命令 \-- display advpn ipv6 session**

------------------------------------------------------------------------

**[display advpn ipv6 session**]命令用来显示IPv6 ADVPN隧道的信息。

【命令】

**[display** **advpn** **ipv6** **session** [ **interface** **tunnel** *number* [ **private-address** *private-ipv6-address*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface******tunnel***number*]：显示指定IPv6 ADVPN类型Tunnel接口上的IPv6 ADVPN隧道信息。*number*为Tunnel接口的编号。如果未指定本参数，则显示所有IPv6 ADVPN隧道的信息。

**[private-address*** private-ipv6-address*]：显示指定对端IPv6私网地址的IPv6 ADVPN隧道信息。*private-ipv6-address*为隧道对端的IPv6私网地址。

**[verbose**]：显示IPv6 ADVPN隧道的详细信息。如果未指定本参数，则显示IPv6 ADVPN隧道的摘要信息。

【举例】

\# 显示所有IPv6 ADVPN隧道的摘要信息。

\<Sysname\> display advpn ipv6 session

Interface         : Tunnel1

Number of sessions: 2

Private address       Public address        Port  Type  State      Holding time

1001::3               2000::180:136         1139  H-S   Success    5H 38M 8S

1001::4               2000::180:137         3546  H-S   Dumb       0H 0M 27S

Interface         : Tunnel2

Number of sessions: 1

Private address       Public address        Port  Type  State      Holding time

1002::4               202.0.180.137         \--    S-H   Establish  0H 0M 2S

Interface         : Tunnel3

Number of sessions: 1

Private address       Public address        Port  Type  State      Holding time

1003::4               2003::180:137         2057  S-S   Success    1H 12M 26S

Interface         : Tunnel4

Number of sessions: 1

Private address       Public address        Port  Type  State      Holding time

1004::4               204.1.181:157         \--    H-H   Success    10H 48M 19S

Interface         : Tunnel5

Number of sessions: 0

\# 显示接口Tunnel1上IPv6 ADVPN隧道的摘要信息。

\<Sysname\> display advpn ipv6 session interface tunnel 1

Interface         : Tunnel1

Number of sessions: 2

Private address       Public address        Port  Type  State      Holding time

1001::3               2000::180:136         1139  H-S   Success    5H 38M 8S

1001::4               2000::180:137         3546  H-S   Dumb       0H 0M 27S

\# 显示接口Tunnel1上对端私网地址为1001::3的IPv6 ADVPN隧道的摘要信息。

\<Sysname\> display advpn ipv6 session interface tunnel 1 private-address 1001::3

Private address       Public address        Port  Type  State      Holding time

1001::3               2000::180:136         1139  H-S   Success    5H 38M 8S

表1-12 display advpn ipv6 session命令显示信息描述表

字段

描述

Interface

ADVPN隧道接口

Number of seesions

隧道接口下建立的ADVPN隧道总数

Private address

ADVPN隧道对端的私网地址

Public address

ADVPN隧道对端的公网地址

Port

ADVPN隧道对端的端口号

Type

ADVPN隧道的类型，包括：

·H-H：本端是Hub，对端也是Hub

·H-S：本端是Hub，对端是Spoke

·S-H：本端是Spoke，对端是Hub

·S-S：本端是Spoke，对端也是Spoke

State

ADVPN隧道的状态，包括：

·Success：表示隧道建立成功

·Establishing：表示隧道正在建立中

·Dumb：表示隧道建立失败后处于静默状态

Holding time

当前ADVPN隧道状态的持续时间，为x小时y分z秒（xH yM zS）

\# 显示所有IPv6 ADVPN隧道的详细信息。

\<Sysname\> display advpn ipv6 session verbose

Interface         : Tunnel1

Client name       : vpn1

ADVPN domain name : 1

Link protocol     : UDP

Number of sessions: 2

  Private address: 1001::3

  Public address : 2000::180:136

  ADVPN port     : 1139

  Session type   : Hub-Spoke

  State          : Success

  Holding time   : 5H 38M 8S

  Input : 2201 packets, 2198 data packets, 3 control packets

          2191 multicasts, 0 errors

  Output: 2169 packets, 216 data packets, 1 control packets

          2163 multicasts, 0 errors

  Private address: 1001::4

  Public address : 2000::180:137

  ADVPN port     : 3546

  Session type   : Hub-Spoke

  State          : Dumb

  Holding time   : 0H 0M 27S

  Input : 1 packets, 0 data packets, 1 control packets

          0 multicasts, 0 errors

  Output: 16 packets, 0 data packets, 16 control packets

          0 multicasts, 0 errors

Interface         : Tunnel2

Client name       : vpn2

ADVPN domain name : 2

Link protocol     : GRE

Number of sessions: 1

  Private address: 1002::4

  Public address : 202.0.180.137

  Session type   : Spoke-Hub

  State          : Establish

  Holding time   : 0H 0M 2S

  Input:  0 packets, 0 data packets, 0 control packets

          0 multicasts, 0 errors

  Output: 1 packets, 0 data packets, 1 control packets

          0 multicasts, 0 errors

Interface         : Tunnel3

Client name       : vpn3

ADVPN domain name : 3

Link protocol     : IPsec-UDP

Number of sessions: 1

  Private address: 1003::4

  Public address : 2003::180:137

  ADVPN port     : 2057

  SA\'s SPI       :

    Inbound : 187199087 (0xb286e6f) [ESP]

    Outbound: 3562274487 (0xd453feb7) [ESP]

  Session type   : Spoke-Spoke

  State          : Establish

  Holding time   : 0H 0M 2S

  Input:  0 packets, 0 data packets, 0 control packets

          0 multicasts, 0 errors

  Output: 1 packets, 0 data packets, 1 control packets

          0 multicasts, 0 errors

Interface         : Tunnel4

Client name       : vpn4

ADVPN domain name : 4

Link protocol     : IPsec-GRE

Number of sessions: 1

  Private address: 1004::4

  Public address : 204.1.181:157

  SA\'s SPI       :

    Inbound:  187199087 (0xb286e6f) [ESP ]

    Outbound: 3562274487 (0xd453feb7) [ESP]

  Session type   : Hub-Hub

  State          : Success

  Holding time   : 10H 48M 19S

  Input : 2201 packets, 2198 data packets, 3 control packets

          2191 multicasts, 0 errors

  Output: 2169 packets, 2168 data packets, 1 control packets

          2163 multicasts, 0 errors

Interface         : Tunnel5

Client name       : vpn5

ADVPN domain name : 5

Link protocol     : UDP

Number of sessions: 0

\# 显示接口Tunnel1上IPv6 ADVPN隧道的详细信息。

\<Sysname\> display advpn ipv6 session interface tunnel 1 verbose

Interface         : Tunnel1

Client name       : vpn1

ADVPN domain name : 1

Link protocol     : UDP

Number of sessions: 2

  Private address: 1001::3

  Public address : 2000::180:136

  ADVPN port     : 1139

  Session type   : Hub-Spoke

  State          : Success

  Holding time   : 5H 38M 8S

  Input : 2201 packets, 2198 data packets, 3 control packets

          2191 multicasts, 0 errors

  Output: 2169 packets, 216 data packets, 1 control packets

          2163 multicasts, 0 errors

  Private address: 1001::4

  Public address : 2000::180:137

  ADVPN port     : 3546

  Session type   : Hub-Spoke

  State          : Dumb

  Holding time   : 0H 0M 27S

  Input : 1 packets, 0 data packets, 1 control packets

          0 multicasts, 0 errors

  Output: 16 packets, 0 data packets, 16 control packets

          0 multicasts, 0 errors

\# 显示接口Tunnel1上对端私网地址为1001::3的IPv6 ADVPN隧道的详细信息。

\<Sysname\> display advpn ipv6 session interface tunnel 1 private-address 1001::3 verbose

  Private address: 1001::3

  Public address : 2000::180:136

  ADVPN port     : 1139

  Session type   : Hub-Spoke

  State          : Success

  Holding time   : 5H 38M 8S

  Input : 2201 packets, 2198 data packets, 3 control packets

          2191 multicasts, 0 errors

  Output: 2169 packets, 216 data packets, 1 control packets

          2163 multicasts, 0 errors

表1-13 display advpn ipv6 session verbose命令显示信息描述表

字段

描述

Interface

ADVPN隧道接口

Client name

隧道接口绑定的VAM Client名称

ADVPN domain name

ADVPN域的名称

Link protocol

ADVPN隧道使用的承载链路层协议：

·UDP

·GRE

·IPsec-UDP

·IPsec-GRE

Number of sessions

隧道接口下建立的ADVPN隧道总数

Private address

ADVPN隧道对端的私网地址

Public address

ADVPN隧道对端的公网地址

ADVPN port

ADVPN隧道使用的承载链路层协议为UDP或IPsec-UDP时，隧道的UDP端口号

SA\'s SPI

ADVPN隧道使用的承载链路层协议为IPsec-UDP或IPsec-GRE时，出方向和入方向的安全策略索引

Session type

ADVPN隧道的类型，包括：

·Hub-Hub：本端是Hub，对端也是Hub

·Hub-Spoke：本端是Hub，对端是Spoke

·Spoke-Hub：本端是Spoke，对端是Hub

·Spoke-Spoke：本端是Spoke，对端也是Spoke

State

ADVPN隧道的状态，包括：

·Success：表示隧道建立成功

·Establishing：表示隧道正在建立中

·Dumb：表示隧道建立失败后处于静默状态

Holding time

当前隧道状态的持续时间，为x小时y分z秒（xH yM zS）

Input

接收的报文统计信息，包括：

·packets：报文总个数

·data packets：数据报文个数

·control packets：控制报文个数

·multicasts：组播报文个数

·errors：错误报文个数

Output

发送的报文统计信息，包括：

·packets：报文总个数

·data packets：数据报文个数

·control packets：控制报文个数

·multicasts：组播报文个数

·errors：错误报文个数

【相关命令】

·**reset advpn ipv6 session**

**ADVPN \-- ADVPN隧道配置命令 \-- display advpn session**

------------------------------------------------------------------------

**[display advpn session**]命令用来显示IPv4 ADVPN隧道的信息。

【命令】

**[display** **advpn** **session** [ **interface** **tunnel** *number* [ **private-address** *private-ip-address*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface******tunnel** *number*]：显示指定IPv4 ADVPN类型Tunnel接口上的IPv4 ADVPN隧道信息。*number*为Tunnel接口的编号。如果未指定本参数，则显示所有IPv4 ADVPN隧道的信息。

**[private-address***private-ip-address*]：显示指定对端IPv4私网地址的IPv4 ADVPN隧道信息。*private-ip-address*为对到对端的IPv4私网地址。

**[verbose**]：显示IPv4 ADVPN隧道的详细信息。如果未指定本参数，则显示IPv4 ADVPN隧道的摘要信息。

【举例】

\# 显示所有IPv4 ADVPN隧道的摘要信息。

\<Sysname\> display advpn session

Interface         : Tunnel1

Number of sessions: 2

Private address  Public address              Port  Type  State      Holding time

10.0.0.3         192.168.180.136             1139  H-S   Success    5H 38M 8S

10.0.1.4         192.168.180.137             3546  H-S   Dumb       0H 0M 27S

Interface         : Tunnel2

Number of sessions: 1

Private address  Public address              Port  Type  State      Holding time

20.0.0.3         200::3                      \--     S-H   Establish  0H 0M 2S

Interface         : Tunnel3

Number of sessions: 1

Private address  Public address              Port  Type  State      Holding time

30.0.0.3         192.168.200.22              2057  S-S   Success    1H 12M 26S

Interface         : Tunnel4

Number of sessions: 1

Private address  Public address              Port  Type  State      Holding time

40.0.0.3         4::4                        \--    H-H   Success    10H 48M 19S

Interface         : Tunnel5

Number of sessions: 0

\# 显示接口Tunnel1上IPv4 ADVPN隧道的摘要信息。

\<Sysname\> display advpn session interface tunnel 1

Interface         : Tunnel1

Number of sessions: 2

Private address  Public address              Port  Type  State      Holding time

10.0.0.3         192.168.180.136             1139  H-S   Success    5H 38M 8S

10.0.1.4         192.168.180.137             3546  H-S   Dumb       0H 0M 27S

\# 显示接口Tunnel1上对端私网地址为10.0.1.3的IPv4 ADVPN隧道的摘要信息。

\<Sysname\> display advpn session interface tunnel 1 private-address 10.0.1.3

Private address  Public address              Port  Type  State      Holding time

10.0.0.3         192.168.180.136             1139  H-S   Success    5H 38M 8S

表1-14 display advpn session命令显示信息描述表

字段

描述

Interface

ADVPN隧道接口

ADVPN domain name

ADVPN域的名称

Number of sessions

隧道接口下建立的ADVPN隧道总数

Private address

ADVPN隧道对端的私网地址

Public address

ADVPN隧道对端的公网地址

Port

ADVPN隧道对端的端口号

Type

ADVPN隧道的类型，包括：

·H-H：本端是Hub，对端也是Hub

·H-S：本端是Hub，对端是Spoke

·S-H：本端是Spoke，对端是Hub

·S-S：本端是Spoke，对端也是Spoke

State

ADVPN隧道的状态，包括：

·Success：表示隧道建立成功

·Establishing：表示隧道正在建立中

·Dumb：表示隧道建立失败后处于静默状态

Holding time

当前隧道状态的持续时间，为x小时y分z秒（xH yM zS)

\# 显示所有IPv4 ADVPN隧道的详细信息。

\<Sysname\> display advpn session verbose

Interface         : Tunnel1

Client name       : vpn1

ADVPN domain name : 1

Link Protocol     : UDP

Number of sessions: 2

  Private address: 10.0.1.3

  Public address : 192.168.180.136

  ADVPN Port     : 1139

  Behind NAT     : No

  Session type   : Hub-Spoke

  State          : Success

  Holding time   : 5H 38M 8S

  Input : 2201 packets, 218 data packets, 3 control packets

          2191 multicasts, 0 errors

  Output: 2169 packets, 2168 data packets, 1 control packets

          2163 multicasts, 0 errors

  Private address: 10.0.1.4

  Public address : 192.168.180.137

  ADVPN port     : 3546

  Behind NAT     : No

  Session type   : Hub-Spoke

  State          : Dumb

  Holding time   : 0H 0M 27S

  Input : 1 packets, 0 data packets, 1 control packets

          0 multicasts, 0 errors

  Output: 16 packets, 0 data packets, 16 control packets

          0 multicasts, 0 errors

Interface         : Tunnel2

Client name       : vpn2

ADVPN domain name : 2

Link protocol     : GRE

Number of sessions: 1

  Private address: 20.0.0.3

  Public address : 200::3

  Behind NAT     : No

  Session type   : Spoke-Hub

  State          : Establish

  Holding time   : 0H  0M 2S

  Input:  0 packets, 0 data packets, 0 control packets

          0 multicasts, 0 errors

  Output: 1 packets, 0 data packets, 1 control packets

          0 multicasts, 0 errors

Interface         : Tunnel3

Client name       : vpn3

ADVPN domain name : 3

Link Protocol     : IPsec-UDP

Number of sessions: 1

  Private address: 30.0.0.3

  Public address : 192.168.200.32

  ADVPN port     : 2057

  SA\'s SPI       :

    Inbound:  187199087 (0xb286e6f) [ESP]

    Outbound: 3562274487 (0xd453feb7) [ESP]

  Behind NAT     : No

  Session type   : Spoke-Spoke

  State          : Establish

  Holding time   : 0H  0M 2S

  Input:  0 packets, 0 data packets, 0 control packets

          0 multicasts, 0 errors

  Output: 1 packets, 0 data packets, 1 control packets

          0 multicasts, 0 errors

Interface         : Tunnel4

Client name       : vpn4

ADVPN domain name : 4

Link protocol     : IPsec-GRE

Number of sessions: 1

  Private address: 40.0.0.3

  Public address : 4::4

  SA\'s SPI       :

    Inbound:  187199087 (0xb286e6f) [ESP]

    Outbound: 3562274487 (0xd453feb7) [ESP]

  Behind NAT     : No

  Session type   : Hub-Hub

  State          : Success

  Holding time   : 10H 48M 19S

  Input : 2201 packets, 2198 data packets, 3 control packets

          2191 multicasts, 0 errors

  Output: 2169 packets, 2168 data packets, 1 control packets

          2163 multicasts, 0 errors

Interface         : Tunnel5

Client name       : vpn5

ADVPN domain name : 5

Link protocol     : UDP

Number of sessions: 0

\# 显示接口Tunnel1上IPv4 ADVPN隧道的详细信息。

\<Sysname\> display advpn session interface tunnel 1 verbose

Interface         : Tunnel1

Client name       : vpn1

ADVPN domain name : 1

Link Protocol     : UDP

Number of sessions: 2

  Private address: 10.0.1.3

  Public address : 192.168.180.136

  ADVPN Port     : 1139

  Behind NAT     : No

  Session type   : Hub-Spoke

  State          : Success

  Holding time   : 5H 38M 8S

  Input : 2201 packets, 218 data packets, 3 control packets

          2191 multicasts, 0 errors

  Output: 2169 packets, 2168 data packets, 1 control packets

          2163 multicasts, 0 errors

  Private address: 10.0.1.4

  Public address : 192.168.180.137

  ADVPN port     : 3546

  Behind NAT     : No

  Session type   : Hub-Spoke

  State          : Dumb

  Holding time   : 0H 0M 27S

  Input : 1 packets, 0 data packets, 1 control packets

          0 multicasts, 0 errors

  Output: 16 packets, 0 data packets, 16 control packets

          0 multicasts, 0 errors

\# 显示接口Tunnel1上对端私网地址为10.0.1.3的IPv4 ADVPN隧道的详细信息。

\<Sysname\> display advpn session verbose interface tunnel 1 private-address 10.0.1.3

  Private address: 10.0.1.3

  Public address : 192.168.180.136

  ADVPN Port     : 1139

  Behind NAT     : No

  Session type   : Hub-Spoke

  State          : Success

  Holding time   : 5H 38M 8S

  Input : 2201 packets, 218 data packets, 3 control packets

          2191 multicasts, 0 errors

  Output: 2169 packets, 2168 data packets, 1 control packets

          2163 multicasts, 0 errors

表1-15 display advpn session verbose命令显示信息描述表

字段

描述

Interface

ADVPN隧道接口

Client name

隧道接口绑定的VAM Client名称

ADVPN domain name

ADVPN域的名称

Link protocol

ADVPN隧道使用的承载链路层协议：

·UDP

·GRE

·IPsec-UDP

·IPsec-GRE

Number of sessions

隧道接口下建立的ADVPN隧道总数

Private address

ADVPN隧道对端的私网地址

Public address

ADVPN隧道对端的公网地址

ADVPN port

ADVPN隧道使用的承载链路层协议为UDP或IPsec-UDP时，隧道的UDP端口号

SA\'s SPI

ADVPN隧道使用的承载链路层协议为IPsec-UDP或IPsec-GRE时，出方向和入方向的安全策略索引

Behind NAT

ADVPN隧道对端是否穿越NAT

Session type

ADVPN隧道的类型，包括：

·Hub-Hub：本端是Hub，对端也是Hub

·Hub-Spoke：本端是Hub，对端是Spoke

·Spoke-Hub：本端是Spoke，对端是Hub

·Spoke-Spoke：本端是Spoke，对端也是Spoke

State

ADVPN隧道的状态，包括：

·Success：表示隧道建立成功

·Establishing：表示隧道正在建立中

·Dumb：表示隧道建立失败后处于静默状态

Holding time

当前隧道状态的持续时间，为x小时y分z秒（xH yM zS）

Input

接收的报文统计信息，包括：

·packets：报文总个数

·data packets：数据报文个数

·control packets：控制报文个数

·multicasts：组播报文个数

·errors：错误报文个数

Output

发送的报文统计信息，包括：

·packets：报文总个数

·data packets；数据报文个数

·control packets：控制报文个数

·multicasts：组播报文个数

·errors：错误报文个数

【相关命令】

·**reset advpn session**

**ADVPN \-- ADVPN隧道配置命令 \-- keepalive**

------------------------------------------------------------------------

**[keepalive**]命令用来配置ADVPN隧道的Keepalive报文发送周期及最大发送次数。

**[undo keepalive**]命令用来恢复缺省情况。

【命令】

**[keepalive interval*** time-interval*** retry ***retry-times*]

**[undo keepalive**]

【缺省情况】

ADVPN隧道的Keepalive报文发送周期为180秒，最大发送次数为3次。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** time-interval*]：Keepalive报文的发送周期，取值范围为1～32767，单位为秒。

**[retry ***retry-times*]：Keepalive报文的最大发送次数，取值范围为1～255。

【使用指导】

·本命令只有在ADVPN隧道类型的Tunnel接口下才能配置。

·如果在Keepalive报文发送周期×最大发送次数时间内没有收到Keepalive报文，则断开该隧道。

·在同一个ADVPN域中，所有Tunnel接口的Keepalive报文发送周期及最大发送次数必须一致。

·本命令配置之后，ADVPN隧道的Keepalive定时器并不立即启动，直到ADVPN隧道建立成功之后才启动。

【举例】

\# 配置ADVPN隧道的Keepalive报文发送周期为20秒，最大发送次数为5次。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn udp ipv4

Sysname-Tunnel1 keepalive interval 20 retry 5

**ADVPN \-- ADVPN隧道配置命令 \-- reset advpn ipv6 session**

------------------------------------------------------------------------

**[reset advpn ipv6 session**]命令用来拆除IPv6 ADVPN隧道。

【命令】

**[reset** **advpn** **ipv6** **session** [ **interface** **tunnel** *number* [ **private-address** *private-ipv6-address*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface******tunnel***number*]：拆除指定IPv6 ADVPN类型Tunnel接口上的IPv6 ADVPN隧道。*number*为Tunnel接口的编号。如果未指定本参数，则拆除所有IPv6 ADVPN隧道。

**[private-address*** private-ipv6-address*]：拆除指定对端IPv6私网地址的IPv6 ADVPN隧道。*private-ipv6-address*为隧道对端的IPv6私网地址。如未指定本参数，则拆除指定或所有Tunnel接口上的所有ADVPN隧道。

【使用指导】

如果隧道对端是Hub，且与本端在同一个Hub组内，隧道拆除后将重新建立隧道。

【举例】

\# 拆除所有IPv6 ADVPN隧道。

\<Sysname\> reset advpn ipv6 session

\# 拆除接口Tunnel1上的所有IPv6 ADVPN隧道。

\<Sysname\> reset advpn ipv6 session interface tunnel 1

\# 拆除接口Tunnel1上对端私网地址为1000::1的IPv6 ADVPN隧道。

\<Sysname\> reset advpn ipv6 session interface tunnel 1 private-address 1000::1

【相关命令】

·**display advpn ****ipv6 session**

**ADVPN \-- ADVPN隧道配置命令 \-- reset advpn ipv6 session statistics**

------------------------------------------------------------------------

**[reset advpn ipv6 session statistic**]命令用来清除IPv6 ADVPN隧道的统计信息。

【命令】

**[reset** **advpn** **ipv6** **session** **statistics** [ **interface** **tunnel** *number* [ **private-address** *private-ipv6-address*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface******tunnel***number*]：清除指定IPv6 ADVPN类型Tunnel接口上IPv6 ADVPN隧道的统计信息。*number*为Tunnel接口的编号。如果未指定本参数，则清除所有IPv6 ADVPN隧道的统计信息。

**[private-address*** private-ipv6-address*]：清除指定对端IPv6私网地址的IPv6 ADVPN隧道的统计信息。*private-ipv6-address*为隧道对端的IPv6私网地址。如果未指定本参数，则清除指定或所有Tunnel接口上所有IPv6 ADVPN隧道的统计信息。

【举例】

\# 清除所有IPv6 ADVPN隧道的统计信息。

\<Sysname\> reset advpn ipv6 session statistics

\# 清除接口Tunnel1上所有IPv6 ADVPN隧道的统计信息。

\<Sysname\> reset advpn ipv6 session statistics interface tunnel 1

\# 清除接口Tunnel1上对端私网地址为1::1的IPv6 ADVPN隧道的统计信息。

\<Sysname\> reset advpn ipv6 session statistics interface tunnel 1 private-address 1::1

**ADVPN \-- ADVPN隧道配置命令 \-- reset advpn session**

------------------------------------------------------------------------

**[reset advpn session**]命令用来删除IPv4 ADVPN隧道。

【命令】

**[reset** **advpn** **session** [ **interface** **tunnel** *number* [ **private-address** *private-ip-address*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface******tunnel** *number*]：删除指定IPv4 ADVPN类型Tunnel接口上的IPv4 ADVPN隧道。*number*为Tunnel接口的编号。如果未指定本参数，则删除所有IPv4 ADVPN隧道。

**[private-address*** private-ip-address*]：删除指定对端IPv4私网地址的IPv4 ADVPN隧道。*private-ip-address*为隧道对端的IPv4私网地址。如果未指定本参数，则删除指定或所有Tunnel接口上的所有IPv4 ADVPN隧道。

【使用指导】

如果隧道对端是Hub，且与本端在同一个Hub组内，隧道删除后将重新建立。

【举例】

\# 删除所有IPv4 ADVPN隧道。

\<Sysname\> reset advpn session

\# 删除接口Tunnel1上所有IPv4 ADVPN隧道。

\<Sysname\> reset advpn session interface tunnel 1

\# 删除接口Tunnel1上对端私网地址为169.254.0.1的IPv4 ADVPN隧道。

\<Sysname\> reset advpn session interface tunnel 1 private-address 169.254.0.1

【相关命令】

·**display advpn session**

**ADVPN \-- ADVPN隧道配置命令 \-- reset advpn session statistics**

------------------------------------------------------------------------

**[reset advpn session statistic**]命令用来清除IPv4 ADVPN隧道的统计信息。

【命令】

**[reset** **advpn** **session** **statistics** [ **interface** **tunnel** *number* [ **private-address** *private-ip-address*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface******tunnel***number*]：清除指定IPv4 ADVPN类型Tunnel接口上IPv4 ADVPN隧道的统计信息。*number*为Tunnel接口的编号。如果未指定本参数，则清除所有IPv4 ADVPN隧道的统计信息。

**[private-address*** private-ip-address*]：清除指定对端IPv4私网地址的IPv4 ADVPN隧道的统计信息。*private-ip-address*为隧道对端的IPv4私网地址。如果未指定本参数，则清除指定或所有Tunnel接口上所有IPv4 ADVPN隧道的统计信息。

【举例】

\# 清除所有IPv4 ADVPN隧道的统计信息。

\<Sysname\> reset advpn session statistics

\# 清除接口Tunnel1上所有IPv4 ADVPN隧道的统计信息。

\<Sysname\> reset advpn session statistics interface tunnel 1

\# 清除接口Tunnel1上对端私网地址为169.254.0.1的IPv4 ADVPN隧道的统计信息。

\<Sysname\> reset advpn session statistics interface tunnel 1 private-address 169.254.0.1

**ADVPN \-- ADVPN隧道配置命令 \-- vam client**

------------------------------------------------------------------------

**[vam client**]命令用来配置IPv4 ADVPN隧道接口绑定的VAM Client。

**[undo vam client**]命令用来取消IPv4 ADVPN隧道接口绑定的VAM Client。

【命令】

**[vam client ***client-name* \**[compatible** **advpn0** ]]

**[undo vam client**]

【缺省情况】

IPv4 ADVPN隧道接口没有绑定任何VAM Client。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[client-name*]：绑定的VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。

**[compatible** **advpn0**]：兼容ADVPN V0版本报文格式。如果未指定本参数，则不兼容ADVPN V0版本报文格式。

【使用指导】

对于IPv4 ADVPN隧道，需要配置此命令将隧道接口与VAM Client绑定。绑定后，VAM Client会向VAM Server注册相应隧道接口的IPv4私网信息。

需要注意的是：

·本命令只有在IPv4 ADVPN类型的Tunnel接口下才能配置。

·一个VAM Client只能与一个IPv4 ADVPN类型的Tunnel接口绑定。

·如果Tunnel接口绑定的VAM Client所在的Hub组内中有仅支持ADVPN V0版本报文格式的设备，则必须配置**compatible**参数。配置了**compatible**参数后，Tunnel接口上配置的ADVPN报文源UDP端口号必须和其他Tunnel接口不同。

【举例】

\# 配置IPv4 ADVPN隧道接口Tunnel1与VAM Client abc绑定。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn udp ipv4

Sysname-Tunnel1 vam client abc

【相关命令】

·**vam ipv6 client**

·**advpn source-port**

**ADVPN \-- ADVPN隧道配置命令 \-- vam ipv6 client**

------------------------------------------------------------------------

**[vam ipv6 client**]命令用来配置IPv6 ADVPN隧道接口绑定的VAM Client。

**[undo vam ipv6 client**]命令用来取消IPv6 ADVPN隧道接口绑定的VAM Client。

【命令】

**[vam ipv6 client ***client-name*]

**[undo vam ipv6 client**]

【缺省情况】

IPv6 ADVPN隧道接口没有绑定任何VAM Client。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[client-name*]：绑定的VAM Client的名称，为1～63个字符的字符串，不区分大小写，只能包含字符A-Z、a-z、0-9和"."。

【使用指导】

对于IPv6 ADVPN隧道，需要配置此命令将隧道接口与VAM Client绑定。绑定之后， VAM Client会向VAM Server注册相应隧道接口的IPv6私网信息。

需要注意的是：

·本命令只有在IPv6 ADVPN类型的Tunnel接口下才能配置。

·一个VAM Client只能与一个IPv6 ADVPN类型的Tunnel接口绑定。

【举例】

\# 配置IPv6 ADVPN隧道接口Tunnel1与VAM Client abc绑定。

\<Sysname\> system-view

Sysname interface tunnel 1 mode advpn udp ipv6

Sysname-Tunnel1 vam ipv6 client abc

【相关命令】

·**vam client**
