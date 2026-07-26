
**域名解析 \-- 域名解析配置命令 \-- display dns domain**

------------------------------------------------------------------------

**[display** **dns** **domain**]命令用来显示域名后缀信息。

【命令】

**[display** **dns** **domain** [ **dynamic**   **vpn-instance** *vpn-instance-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dynamic**]：显示通过DHCP等协议动态获得的域名后缀信息。如果不指定本参数，则显示静态配置和动态获得的域名后缀信息。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN内的域名后缀信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网的域名后缀信息。

【举例】

\# 显示公网静态配置和动态获得的域名后缀信息。

\<Sysname\> display dns domain

Type:

  D: Dynamic    S: Static

No.    Type   Domain suffix

1      S      com

2      D      net

表1-1 display dns domain命令显示信息描述表

字段

描述

No.

序号

Type

域名后缀类型：

·S：表示静态配置的域名后缀

·D：表示通过DHCP等协议动态获得的域名后缀

Domain suffix

域名后缀

【相关命令】

·**dns** **domain**

**域名解析 \-- 域名解析配置命令 \-- display dns host**

------------------------------------------------------------------------

**[display** **dns** **host**]命令用来显示域名解析信息。

【命令】

**[display**[ **dns** **host** [ **ip** \| **ipv6** ]  **vpn-instance** *vpn-instance-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ip**]：显示A类查询的信息。A类查询用来解析域名对应的IPv4地址。

**[ipv6**]：显示AAAA类查询的信息。AAAA类查询用来解析域名对应的IPv6地址。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN的域名解析信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网的域名解析信息。

【使用指导】

如果不指定**ip**和**ipv6**参数，则显示所有查询类型的域名解析信息。

【举例】

\# 显示所有查询类型的域名解析信息。

\<Sysname\> display dns host

Type:

  D: Dynamic    S: Static

Total number: 3

No.  Host name         Type  TTL        Query type   IP addresses

1    sample.com        D     3132       A            192.168.10.1

                                                     192.168.10.2

                                                     192.168.10.3

2    zig.sample.com    S     -          A            192.168.1.1

3    sample.net        S     -          AAAA         FE80::4904:4448

表1-2 display dns host命令显示信息描述表

字段

描述

No.

序号

Host name

查询名称

Type

域名解析信息的类型：

·S：表示静态配置的域名解析信息，即通过**ip host**或**ipv6 host**命令配置的主机名及其对应的主机IPv4/IPv6地址

·D：表示通过动态域名解析获得的域名解析信息

TTL

域名解析信息的剩余有效时间，单位为秒

静态信息的TTL值显示为"-"

Query type

查询类型，取值包括A和AAAA

IP addresses

主机名对应的IP地址

·对于A类查询类型，为IPv4地址

·对于AAAA类查询类型，为IPv6地址

【相关命令】

·**reset** **dns** **host**

·**ip** **host**

·**ipv6** **host**

**域名解析 \-- 域名解析配置命令 \-- display dns server**

------------------------------------------------------------------------

**[display** **dns** **server**]命令用来显示域名服务器的IPv4地址信息。

【命令】

**[display** **dns** **server** [ **dynamic**   **vpn-instance** *vpn-instance-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dynamic**]：显示通过DHCP等协议动态获得的域名服务器IPv4地址信息。如果不指定本参数，则显示静态配置和动态获得的域名服务器IPv4地址信息。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN内的域名服务器IPv4地址信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网的域名服务器IPv4地址信息。

【举例】

\# 显示公网的域名服务器IPv4地址信息。

\<Sysname\> display dns server

Type:

  D: Dynamic    S: Static

No. Type  IP address

1   S     202.114.0.124

2   S     169.254.65.125

表1-3 display dns server命令显示信息描述表

字段

描述

No.

域名服务器的序号，系统自动给所配置的服务器编号，从1开始

Type

域名服务器类型

·S表示静态指定的域名服务器信息

·D表示通过DHCP等协议动态获得的域名服务器信息

IP address

域名服务器的IPv4地址

【相关命令】

·**dns** **server**

**域名解析 \-- 域名解析配置命令 \-- display ipv6 dns server**

------------------------------------------------------------------------

**[display** **ipv6** **dns** **server**]命令用来显示域名服务器的IPv6地址信息。

【命令】

**[display** **ipv6** **dns** **server** [ **dynamic**   **vpn-instance** *vpn-instance-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dynamic**]：显示通过DHCP等协议动态获得的域名服务器IPv6地址信息。如果不指定本参数，则显示静态配置和动态获得的域名服务器IPv6地址信息。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN内的域名服务器IPv6地址信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网的域名服务器IPv6地址信息。

【举例】

\# 显示公网域名服务器的IPv6地址信息。

\<Sysname\> display ipv6 dns server

Type:

  D: Dynamic    S: Static

No. Type  IPv6 address                             Outgoing Interface

1   S     2::2

表1-4 display ipv6 dns server命令显示信息描述表

字段

描述

No.

域名服务器的序号

Type

域名服务器类型

·S表示静态指定的域名服务器信息

·D表示通过DHCP等协议动态获得的域名服务器信息

IPv6 address

域名服务器的IPv6地址

Outgoing Interface

出接口名

【相关命令】

·**ipv6** **dns** **server**

**域名解析 \-- 域名解析配置命令 \-- dns domain**

------------------------------------------------------------------------

**[dns** **domain**]命令用来添加域名后缀。

**[undo** **dns** **domain**]命令用来删除指定的域名后缀。

【命令】

**[dns** **domain** *domain-name* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **dns** **domain** *domain-name* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

没有配置域名后缀，即只根据用户输入的域名信息进行解析。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：域名后缀，由"."分隔的字符串组成（如aabbcc.com），每个字符串的长度不超过63个字符，包括"."在内的总长度不超过253个字符。不区分大小写，字符串中可以包含字母、数字、"-"、"\_"或"."。

**[vpn-instance*** vpn-instance-name*]：为指定VPN添加或删除域名后缀。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示为公网添加或删除域名后缀。

【使用指导】

域名解析时，用户只需要输入域名的部分字段，系统会按照域名后缀配置的先后顺序，依次将输入的域名加上不同的域名后缀进行解析。

需要注意的是：

·本命令配置的域名后缀同时用于IPv4域名解析和IPv6域名解析。

·公网或每个VPN内最多可以配置16个域名后缀。可以为公网和最多1024个VPN配置域名后缀。

【举例】

\# 为公网添加一个域名后缀com。

\<Sysname\> system-view

Sysname dns domain com

【相关命令】

·**display** **dns** **domain**

**域名解析 \-- 域名解析配置命令 \-- dns dscp**

------------------------------------------------------------------------

**[dns dscp**]命令用来配置发送DNS报文的DSCP优先级。

**[undo dns dscp**]命令用来恢复缺省值。

【命令】

**[dns dscp ***dscp-value*]

**[undo dns dscp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DNS报文的DSCP优先级，取值范围为0～63，缺省值为0。

【使用指导】

DSCP优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的DSCP优先级的取值越大，报文的优先级越高。

通过本命令可以指定DNS客户端或DNS proxy发送的DNS报文中携带的DSCP优先级的取值。

【举例】

\# 配置发送的DNS报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname dns dscp 30

**域名解析 \-- 域名解析配置命令 \-- dns proxy enable**

------------------------------------------------------------------------

**[dns** **proxy** **enable**]命令用来开启DNS proxy功能。

**[undo** **dns** **proxy** **enable**]命令用来恢复缺省情况。

【命令】

**[dns** **proxy** **enable**]

**[undo** **dns** **proxy** **enable**]

【缺省情况】

DNS proxy功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令的配置同时用于IPv4域名解析和IPv6域名解析。

【举例】

\# 开启DNS proxy功能。

\<Sysname\> system-view

Sysname dns proxy enable

**域名解析 \-- 域名解析配置命令 \-- dns server**

------------------------------------------------------------------------

**[dns** **server**]命令用来配置域名服务器的IPv4地址。

**[undo** **dns** **server**]命令用来删除域名服务器的IPv4地址。

【命令】

**[dns** **server** *ip-address* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **dns** **server** [ *ip-address*   **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

没有配置域名服务器的IPv4地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：域名服务器的IPv4地址。

**[vpn-instance*** vpn-instance-name*]：为指定VPN配置或删除域名服务器的IPv4地址。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置或删除域名服务器的IPv4地址。

【使用指导】

在进行动态域名解析时，系统按照域名服务器IPv4地址配置的先后顺序，依次向各个域名服务器发送查询请求。

需要注意的是：

·公网或单个VPN内最多可以配置6个域名服务器的IPv4地址。可以为公网和最多1024个VPN配置域名服务器的IPv4地址。

·执行**undo** **dns** **server**命令时如果不指定*ip-address*参数，则删除公网或指定VPN中的所有域名服务器IPv4地址。

【举例】

\# 配置域名服务器的IPv4地址为172.16.1.1。

\<Sysname\> system-view

Sysname dns server 172.16.1.1

【相关命令】

·**display** **dns** **server**

**域名解析 \-- 域名解析配置命令 \-- dns source-interface**

------------------------------------------------------------------------

**[dns** **source-interface**]命令用来指定DNS报文的源接口。

**[undo** **dns** **source-interface**]命令用来恢复缺省情况。

【命令】

**[dns** **source-interface** *interface-type* *interface-number* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **dns** **source-interface** *interface-type* *interface-number* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

设备根据DNS server的地址，通过路由表查找报文的出接口，并将该出接口的主IP地址作为发送到该服务器的DNS查询报文的源地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type* *interface-number*]：源接口的接口类型和接口编号。

**[vpn-instance*** vpn-instance-name*]：为指定VPN配置DNS报文的源接口。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置DNS报文的源接口。

【使用指导】

通过本命令指定DNS报文的源接口后，系统将选择指定接口的主IPv4地址或根据RFC 3484中定义的规则选择指定接口的某个IPv6地址，作为DNS查询报文的源地址。

需要注意的是：

·本命令的配置同时用于IPv4域名解析和IPv6域名解析。

·公网或每个VPN内只能配置1个源接口。重复配置时，新的配置会覆盖原有配置。可以为公网和最多1024个VPN配置源接口。

·无论配置的源接口是否属于指定的VPN，该配置都会生效。不建议将不属于VPN的接口配置为该VPN的源接口。

【举例】

·路由应用

\# 指定公网DNS报文的源接口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname dns source-interface gigabitethernet 1/0/1

·交换应用

\# 指定公网DNS报文的源接口为VLAN接口2。

\<Sysname\> system-view

Sysname dns source-interface vlan-interface 2

**域名解析 \-- 域名解析配置命令 \-- dns spoofing**

------------------------------------------------------------------------

**[dns** **spoofing**]命令用来开启欺骗性应答域名解析请求（DNS spoofing）功能，并指定应答的IPv4地址。

**[undo** **dns** **spoofing**]命令关闭DNS spoofing功能。

【命令】

**[dns** **spoofing** *ip-address* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **dns** **spoofing** *ip-address* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

DNS spoofing功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：用来欺骗性应答域名解析请求的IPv4地址。

**[vpn-instance*** vpn-instance-name*]：为指定VPN配置DNS spoofing功能。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置DNS spoofing功能。

【使用指导】

配置DNS spoofing前，需要先开启DNS proxy功能。

公网或每个VPN内只能配置1个DNS spoofing应答的IPv4地址。重复配置时，新的配置会覆盖原有配置。可以为公网和最多1024个VPN配置DNS spoofing功能。

【举例】

\# 开启公网的DNS spoofing功能，并指定应答的IPv4地址为1.1.1.1。

\<Sysname\> system-view

Sysname dns proxy enable

Sysname dns spoofing 1.1.1.1

【相关命令】

·**dns** **proxy** **enable**

**域名解析 \-- 域名解析配置命令 \-- dns spoofing track**

------------------------------------------------------------------------

![说明](域名解析命令.files/image001.png)

本命令的支持情况和设备型号有关，请以设备的实际情况为准。

**[dns spoofing track**]命令用来配置监视指定出接口的网络制式。

**[undo dns spoofing track**]命令用来取消对指定出接口的监视。

【命令】

**[dns spoofing track controller ***interface-type* *interface-number*]

**[undo dns spoofing track**]

【缺省情况】

未指定被监视的出接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[controller ***interface-type interface-number*]：指定被监视的出接口。*interface-type interface-number*表示接口类型和接口编号。

【使用指导】

·配置监视指定出接口的网络制式时，需要先开启DNS spoofing或IPv6 DNS spoofing功能。

·多次配置该命令，新的配置会覆盖已有配置。

【举例】

\# 配置监视指定出接口Cellular0/1的网络制式。如果该接口网络制式为2G，则以IP地址192.168.1.10进行欺骗应答；如果该接口网络制式为3G/4G，则不进行欺骗应答。

\<Sysname\> system-view

Sysname dns proxy enable

Sysname dns spoofing 192.168.1.10

Sysname dns spoofing track controller cellular 0/1

【相关命令】

·**dns spoofing**

·**ipv6 dns spoofing**

**域名解析 \-- 域名解析配置命令 \-- dns trust-interface**

------------------------------------------------------------------------

**[dns** **trust-interface**]命令用来指定DNS信任接口。

**[undo** **dns** **trust-interface**]命令用来删除指定的DNS信任接口。

【命令】

**[dns** **trust-interface** *interface-type* *interface-number*]

**[undo** **dns** **trust-interface** [ *interface-type* *interface-number* ]]

【缺省情况】

没有指定任何接口为信任接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type* *interface-number*]：DNS信任接口的接口类型和接口编号。

【使用指导】

缺省情况下，任意接口通过DHCP等协议动态获得的域名后缀和域名服务器信息都将作为有效信息，用于域名解析。如果网络攻击者通过DHCP服务器为设备分配错误的域名后缀和域名服务器地址，则会导致设备域名解析失败，或解析到错误的结果。通过本配置指定信任接口后，域名解析时只采用信任接口动态获得的域名后缀和域名服务器信息，非信任接口获得的信息不能用于域名解析，从而在一定程度上避免这类攻击。

需要注意的是：

·本命令同时用于IPv4域名解析和IPv6域名解析。

·设备最多可以配置128个信任接口。

·执行**undo** **dns** **trust-interface**命令时，如果不指定任何接口，则删除所有的DNS信任接口，恢复到缺省状态。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1为DNS信任接口。

\<Sysname\> system-view

Sysname dns trust-interface gigabitethernet 1/0/1

·交换应用

\# 指定VLAN接口2为DNS信任接口。

\<Sysname\> system-view

Sysname dns trust-interface vlan-interface 2

**域名解析 \-- 域名解析配置命令 \-- ip host**

------------------------------------------------------------------------

**[ip** **host**]命令用来配置主机名及其对应的主机IPv4地址。

**[undo** **ip** **host**]命令用来删除主机名及其对应的主机IPv4地址。

【命令】

**[ip** **host** *host-name* *ip-address* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **ip** **host** *host-name* *ip-address* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

静态域名解析表中不存在主机名及IPv4地址的对应关系。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[host-name*]：主机名，为1～253个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"-"、"\_"和"."。

*[ip-address*]：与主机名对应的IPv4地址。

**[vpn-instance*** vpn-instance-name*]：为指定VPN配置主机名和IPv4地址的对应关系。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置主机名和IPv4地址的对应关系。

【使用指导】

·公网或单个VPN内最多可以配置1024个主机名和IPv4地址的对应关系。可以同时在公网和最多1024个VPN内配置主机名和IPv4地址的对应关系。

·在公网或单个VPN内，一个主机名只能对应一个IPv4地址。重复配置时，新的配置会覆盖原有配置。

·**ip**、**-a**、**-c**、**-f**、**-h**、**-i**、**-m**、**-n**、**-p**、**-q**、**-r**、**-s**、**-t**、**-tos**、**-v**和**-vpn-instance**已被系统用作**ping**命令的参数关键字，在配置主机名时，请避免使用相同的字符串作为主机名。**ping**命令支持的参数形式，请参考"网络管理和监控"中的"**ping**"命令。

【举例】

\# 配置公网内主机名aaa对应的IPv4地址为10.110.0.1。

\<Sysname\> system-view

Sysname ip host aaa 10.110.0.1

【相关命令】

·**display dns host**

**域名解析 \-- 域名解析配置命令 \-- ipv6 dns dscp**

------------------------------------------------------------------------

**[ipv6 dns dscp**]命令用来配置发送IPv6 DNS报文的DSCP优先级。

**[undo ipv6 dns dscp**]命令用来恢复缺省值。

【命令】

**[ipv6 dns dscp ***dscp-value*]

**[undo ipv6 dns dscp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：IPv6 DNS报文的DSCP优先级，取值范围为0～63，缺省值为0。

【使用指导】

DSCP优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的DSCP优先级的取值越大，报文的优先级越高。

通过本命令可以指定IPv6 DNS客户端或DNS proxy发送的IPv6 DNS报文中携带的DSCP优先级的取值。

【举例】

\# 配置发送的IPv6 DNS报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname ipv6 dns dscp 30

**域名解析 \-- 域名解析配置命令 \-- ipv6 dns server**

------------------------------------------------------------------------

**[ipv6** **dns** **server**]命令用来配置域名服务器的IPv6地址。

**[undo** **ipv6** **dns** **server**]命令用来删除域名服务器的IPv6地址。

【命令】

**[ipv6** **dns** **server** *ipv6-address* [ *interface-type* *interface-number*   **vpn-instance** *vpn-instance-name* ]]

**[undo** **ipv6** **dns** **server** [ *ipv6-address* [ *interface-type* *interface-number*  ]  **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

没有配置域名服务器的IPv6地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：域名服务器的IPv6地址。

*[interface-type* *interface-number*]：指定报文的出接口的接口类型和接口编号。如果不指定本参数，则根据路由表查找报文的出接口。域名服务器的IPv6地址为链路本地地址时，必须指定本参数。域名服务器的IPv6地址为全球单播地址时，无法指定本参数。

**[vpn-instance*** vpn-instance-name*]：为指定VPN配置或删除域名服务器的IPv6地址。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置或删除域名服务器的IPv6地址。

【使用指导】

在进行动态域名解析时，系统按照域名服务器IPv6地址配置的先后顺序，依次向各个域名服务器发送查询请求。

需要注意的是：

·公网或单个VPN内最多可以配置6个域名服务器的IPv6地址。可以为公网和最多1024个VPN配置域名服务器的IPv6地址。

·执行**undo** **ipv6** **dns** **server**命令时如果不指定*ipv6-address*参数，则删除公网或指定VPN中的所有域名服务器IPv6地址。

【举例】

\# 配置公网内域名服务器的IPv6地址为2002::1。

\<Sysname\> system-view

Sysname ipv6 dns server 2002::1

【相关命令】

·**display ipv6 dns server**

**域名解析 \-- 域名解析配置命令 \-- ipv6 dns spoofing**

------------------------------------------------------------------------

**[ipv6** **dns** **spoofing**]命令用来开启DNS spoofing功能，并指定应答的IPv6地址。

**[undo** **ipv6** **dns** **spoofing**]命令用来关闭DNS spoofing功能。

【命令】

**[ipv6** **dns** **spoofing** *ipv6-address* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **ipv6** **dns** **spoofing** *ipv6-address* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

DNS spoofing功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：用来欺骗性应答域名解析请求的IPv6地址。

**[vpn-instance*** vpn-instance-name*]：为指定VPN配置DNS spoofing功能。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置DNS spoofing功能。

【使用指导】

需要注意的是：

·公网或每个VPN内只能配置1个DNS spoofing应答的IPv6地址。重复配置时，新的配置会覆盖原有配置。可以为公网和最多1024个VPN配置DNS spoofing功能。

·本命令必须和**dns proxy enable**命令一起使用。

【举例】

\# 为公网开启DNS spoofing功能，并指定应答的IPv6地址为2001::1。

\<Sysname\> system-view

Sysname dns proxy enable

Sysname ipv6 dns spoofing 2001::1

【相关命令】

·**dns** **proxy** **enable**

**域名解析 \-- 域名解析配置命令 \-- ipv6 host**

------------------------------------------------------------------------

**[ipv6** **host**]命令用来配置主机名及其对应的主机IPv6地址。

**[undo** **ipv6** **host**]命令用来删除主机名及其对应的主机IPv6地址。

【命令】

**[ipv6** **host** *host-name* *ipv6-address* [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **ipv6** **host** *host-name* *ipv6-address* [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

静态域名解析表中不存在主机名及IPv6地址的对应关系。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[host-name*]：主机名，为1～253个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"-"、"\_"和"."。

*[ipv6-address*]：与主机名对应的IPv6地址。

**[vpn-instance*** vpn-instance-name*]：为指定VPN配置主机名和IPv6地址的对应关系。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置主机名和IPv6地址的对应关系。

【使用指导】

·公网或每个VPN内最多可以配置1024个主机名和IPv6地址的对应关系。可以为公网和最多1024个VPN配置主机名和IPv6地址的对应关系。

·在公网或同一个VPN内，一个主机名只能对应一个IPv6地址。重复配置时，新的配置会覆盖原有配置。

·**-a**、**-c**、**-i**、**-m**、**-q**、**-s**、**-t**、**-tc**、**-v**和**-vpn-instance**已被系统用作**ping ipv6**命令的参数关键字，在配置主机名时，请避免使用相同的字符串作为主机名。**ping ipv6**命令支持的参数形式，请参考"网络管理和监控"中的"**ping ipv6**"命令。

【举例】

\# 配置公网内主机名aaa对应的IPv6地址为2001::1。

\<Sysname\> system-view

Sysname ipv6 host aaa 2001::1

【相关命令】

·**ip** **host**

**域名解析 \-- 域名解析配置命令 \-- reset dns host**

------------------------------------------------------------------------

**[reset** **dns** **host**]命令用来清除动态域名解析缓存信息。

【命令】

**[reset**[ **dns** **host** [ **ip** \| **ipv6** ]  **vpn-instance** *vpn-instance-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip**]：清除A类查询的动态缓存信息。A类查询用来解析域名对应的IPv4地址。

**[ipv6**]：清除AAAA类查询的动态缓存信息。AAAA类查询用来解析域名对应的IPv6地址。

**[vpn-instance*** vpn-instance-name*]：清除指定VPN的动态域名解析缓存信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则清除公网的动态域名解析缓存信息。

【使用指导】

如果不指定**ip**和**ipv6**参数，则清除所有查询类型的动态域名解析缓存信息。

【举例】

\# 清除公网所有查询类型的动态域名解析缓存信息。

\<Sysname\> reset dns host

【相关命令】

·**display** **dns** **host**

****

**\
**

**DDNS \-- DDNS配置命令 \-- ddns apply policy**

------------------------------------------------------------------------

**[ddns** **apply** **policy**]命令用来在接口上应用指定的DDNS策略来更新指定的FQDN与IP地址的对应关系，并启动DDNS更新。

**[undo** **ddns** **apply** **policy**]命令用来在接口上取消应用DDNS策略，停止DDNS更新。

【命令】

**[ddns** **apply** **policy** *policy-name* [ **fqdn** *domain-name* ]]

**[undo** **ddns** **apply** **policy** *policy-name*]

【缺省情况】

没有为接口指定任何DDNS策略和需要更新的FQDN，且未启动DDNS更新。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：DDNS策略名称，为1～32个字符的字符串，不区分大小写。

**[fqdn** *domain-name*]：指定需要更新该FQDN与IP地址的对应关系，用于替换DDNS更新请求URL中的\<h\>。*domain-name*为主机名，主机名，为1～253个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"-"、"\_"和"."。

【使用指导】

·一个接口上最多可以应用4个DDNS策略。

·重复应用名称相同的DDNS策略，并指定不同的FQDN时，新的配置会覆盖原有配置，同时发起一次DDNS更新。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1下指定应用DDNS策略steven_policy来更新合格域名www.whatever.com与IP地址的对应关系，并启动DDNS更新功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ddns apply policy steven_policy fqdn www.whatever.com

·交换应用

\# 在VLAN接口2下指定应用DDNS策略steven_policy来更新合格域名www.whatever.com与IP地址的对应关系，并启动DDNS更新功能。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 ddns apply policy steven_policy fqdn www.whatever.com

【相关命令】

·{.MsoCommentReference}**ddns** **policy**

·**display** **ddns** **policy**

**DDNS \-- DDNS配置命令 \-- ddns dscp**

------------------------------------------------------------------------

**[ddns dscp**]命令用来配置发送DDNS报文的DSCP优先级。

**[undo ddns dscp**]命令用来恢复缺省值。

【命令】

**[ddns dscp ***dscp-value*]

**[undo ddns dscp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DDNS报文的DSCP优先级，取值范围为0～63，缺省值为0。

【使用指导】

DSCP优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的DSCP优先级的取值越大，报文的优先级越高。通过本命令可以指定发送的DDNS报文中携带的DSCP优先级的取值。

【举例】

\# 配置发送的DDNS报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname ddns dscp 30

**DDNS \-- DDNS配置命令 \-- ddns policy**

------------------------------------------------------------------------

**[ddns** **policy**]命令用来创建DDNS策略，并进入DDNS策略视图。

**[undo** **ddns** **policy**]命令用来删除DDNS策略。

【命令】

**[ddns** **policy** *policy-name*]

**[undo** **ddns** **policy** *policy-name*]

【缺省情况】

设备上不存在任何DDNS策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：DDNS策略名称，为1～32个字符的字符串，不区分大小写。

【使用指导】

设备上最多可以创建16个DDNS策略。

【举例】

\# 创建名称为steven_policy的DDNS策略，并进入DDNS策略视图。

\<Sysname\> system-view

Sysname ddns policy steven_policy

【相关命令】

·**display** **ddns** **policy**

·**ddns** **apply** **policy**

**DDNS \-- DDNS配置命令 \-- display ddns policy**

------------------------------------------------------------------------

**[display ddns policy**]命令用来显示DDNS策略的信息。

【命令】

**[display** **ddns** **policy** [ *policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[policy-name*]：DDNS策略名称，为1～32个字符的字符串，不区分大小写。如果不指定本参数，则显示所有DDNS策略的信息。

【举例】

\# 显示名称为steven_policy的DDNS策略的信息。

\<Sysname\> display ddns policy steven_policy

DDNS policy: steven_policy

  URL              : http://members.3322.org/dyndns/update?

                     system=dyndns&hostname=\<h\>&myip=\<a\>

  Username         : steven

  Password         : \*\*\*\*\*\*

  Method           : GET

  SSL client policy:

  Interval         : 1 days 0 hours 1 minutes

\# 显示所有DDNS策略的信息。

\<Sysname\> display ddns policy

DDNS policy: steven_policy

  URL              : http://members.3322.org/dyndns/update?system=

                     dyndns&hostname=\<h\>&myip=\<a\>

  Username         : steven

  Password         : \*\*\*\*\*\*

  Method           : GET

  SSL client policy:

  Interval         : 0 days 0 hours 30 minutes 

DDNS policy: tom-policy

  URL              : http://members.3322.org/dyndns/update?system=

                     dyndns&hostname=\<h\>&myip=\<a\>

  Username         :

  Password         :

  Method           : GET

  SSL client policy:

  Interval         : 0 days 0 hours 15 minutes

DDNS policy: u-policy

  URL              : oray://phservice2.oray.net

  Username         : username

  Password         :

  Method           : -

  SSL client policy:

  Interval         : 0 days 0 hours 15 minutes

表2-1 display ddns policy命令显示信息描述表

字段

描述

DDNS policy

DDNS策略名称

URL

DDNS更新请求的URL地址。未配置时显示为空

Username

DDNS更新请求URL地址中的用户名。未配置时显示为空

Password

DDNS更新请求URL地址中的密码。未配置时显示为空，有配置时显示为"\*\*\*\*\*\*"

Method

采用HTTP或HTTPS报文发送DDNS更新请求时，使用的参数传输方式

取值包括：

·GET：表示使用HTTP或HTTPS报文发送DDNS更新请求，且参数传输方式为GET方式

·POST：表示使用HTTP或HTTPS报文发送DDNS更新请求，且参数传输方式为POST方式

SSL client policy

关联的SSL客户端策略名称。未配置时显示为空

Interval

定时发起DDNS更新请求的时间间隔

【相关命令】

·**ddns** **policy**

**DDNS \-- DDNS配置命令 \-- interval**

------------------------------------------------------------------------

**[interval**]命令用来指定DDNS更新启动后，定时发起更新请求的时间间隔。

**[undo** **interval**]命令用来恢复缺省情况。

【命令】

**[interval** *days* [ *hours* [ *minutes*  ]]]

**[undo** **interval**]

【缺省情况】

定时发起DDNS更新请求的时间间隔是1小时。

【视图】

DDNS策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[days*]：天，取值范围为0～365。

*[hours*]：小时，取值范围为0～23。

*[minutes*]：分钟，取值范围为0～59。

【使用指导】

·不论是否到达定时发起更新请求的时间，只要对应接口的主IP地址发生改变或接口的链路状态由down变为up，都会立即发起更新请求。

·如果配置时间间隔为0，则不会定时发起更新，除非对应接口的IP地址发生改变或接口的链路状态由down变为up。

·重复执行本命令，配置不同的时间间隔时，只有最后一次配置的时间间隔生效。如果DDNS策略已经应用到接口上，则立即触发一次DDNS更新，并以最后一次配置的时间间隔为更新周期。

【举例】

\# 为DDNS策略steven_policy指定定时发起更新请求的时间间隔为1天零1分。

\<Sysname\> system-view

Sysname ddns policy steven_policy

Sysname-ddns-policy-steven_policy interval 1 0 1

【相关命令】

·**display** **ddns** **policy**

·**ddns** **policy**

**DDNS \-- DDNS配置命令 \-- method**

------------------------------------------------------------------------

**[method**]命令用来配置采用HTTP或HTTPS报文发送DDNS更新请求时，使用的参数传输方式。

**[undo** **method**]命令用来恢复缺省情况。

【命令】

**[method**[ { **http-get** *\|* **http-post** }]]

**[undo** **method**]

【缺省情况】

采用HTTP或HTTPS报文发送DDNS更新请求时，参数的传输方式为http-get。

【视图】

DDNS策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[http-get**]：参数的传输方式为http-get。

**[http-post**]：参数的传输方式为http-post。

【使用指导】

采用HTTP或HTTPS报文发送DDNS更新请求时，不同的DDNS服务器要求使用的参数传输方式可能不同。例如DHS服务器，需要使用http-post参数传输方式。通过本配置可以修改参数传输方式，以满足DDNS服务器的要求。

需要注意的是：

·本命令仅在基于HTTP或HTTPS与DDNS服务器通信时生效。基于其他协议与DDNS服务器通信时，本命令不生效。

·通过本命令修改DDNS策略的参数传输方式时，如果该DDNS策略已经应用到接口上，则立即触发一次DDNS更新。

【举例】

\# 配置DDNS策略steven_policy采用HTTP或HTTPS报文发送DDNS更新请求时，使用的参数传输方式为post方式。

\<Sysname\> system-view

Sysname ddns policy steven_policy

Sysname-ddns-policy-steven_policy method http-post

【相关命令】

·**display** **ddns** **policy**

·**ddns** **policy**

**DDNS \-- DDNS配置命令 \-- password**

------------------------------------------------------------------------

**[password**]命令用来指定DDNS更新请求的URL地址中的密码。

**[undo** **password**]命令用来删除DDNS更新请求的URL地址中的密码。

【命令】

**[password**[ { **cipher** \| **simple** } *password*]]

**[undo password**]

【缺省情况】

未指定DDNS更新请求的URL地址中的密码。

【视图】

DDNS策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置用户密码。

**[simple**]：表示以明文方式设置用户密码。

*[password*]：设置的明文密码或密文密码，区分大小写。明文密码为1～32个字符的字符串；密文密码为1～73个字符的字符串。

【使用指导】

以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。

【举例】

\# 为DDNS策略steven_policy指定DDNS更新请求的URL地址中登录密码为nevets。

\<Sysname\> system-view

Sysname ddns policy steven_policy

Sysname-ddns-policy-steven_policy password simple nevets

【相关命令】

·**display ddns policy**

·**ddns policy**

·**url**

·**username**

**DDNS \-- DDNS配置命令 \-- ssl-client-policy**

------------------------------------------------------------------------

!(域名解析命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ssl-client-policy**]命令用来指定与DDNS策略关联的SSL客户端策略。

**[undo** **ssl-client-policy**]命令用来取消与DDNS策略关联的SSL客户端策略。

【命令】

**[ssl-client-policy** *policy-name*]

**[undo** **ssl-client-policy**]

【缺省情况】

未指定与DDNS策略关联的SSL客户端策略。

【视图】

DDNS策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：SSL客户端策略名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

·SSL客户端策略只对URL为HTTPS地址的DDNS更新请求有效。

·重复执行本命令，为同一个DDNS策略关联不同的SSL客户端策略时，DDNS策略将只与最后配置的SSL客户端策略关联。

【举例】

\# 将SSL客户端策略ssl_policy与DDNS策略steven_policy关联。

\<Sysname\> system-view

Sysname ddns policy steven_policy

Sysname-ddns-policy-steven_policy ssl-client-policy ssl_policy

【相关命令】

·**ddns** **policy**

·**display** **ddns** **policy**

·**ssl-client-policy**（安全命令参考/SSL）

**DDNS \-- DDNS配置命令 \-- url**

------------------------------------------------------------------------

**[url**]命令用来指定DDNS更新请求的URL地址。

**[undo** **url**]命令用来删除DDNS更新请求的URL地址。

【命令】

**[url** *request-url*]

**[undo** **url**]

【缺省情况】

未指定DDNS更新请求的URL地址。

【视图】

DDNS策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[request-url*]：DDNS更新请求的URL地址，为1～240个字符的字符串，区分大小写。

【使用指导】

不同DDNS服务器的请求更新URL地址有所不同。常见的DDNS服务器URL地址格式如表 2-2(?-1384273943#_Ref309136168)所示。

表2-2 常见的DDNS更新请求URL地址格式列表

DDNS服务器

DDNS更新请求的URL地址格式

www.3322.org

http://members.3322.org/dyndns/update?system=dyndns&hostname=\<h\>&myip=\<a\>

DYNDNS

http://members.dyndns.org/nic/update?system=dyndns&hostname=\<h\>&myip=\<a\>

DYNS

http://www.dyns.cx/postscript.php?host=\<h\>&ip=\<a\>

ZONEEDIT

http://dynamic.zoneedit.com/auth/dynamic.html?host=\<h\>&dnsto=\<a\>

TZO

http://cgi.tzo.com/webclient/signedon.html?TZOName=\<h\>IPAddress=\<a\>

EASYDNS

http://members.easydns.com/dyn/ez-ipupdate.php?action=edit&myip=\<a\>&host_id=\<h\>

HEIPV6TB

http://dyn.dns.he.net/nic/update?hostname=\<h\>&myip=\<a\>

CHANGE-IP

http://nic.changeip.com/nic/update?hostname=\<h\>&offline=1

NO-IP

http://dynupdate.no-ip.com/nic/update?hostname=\<h\>&myip=\<a\>

DHS

http://members.dhs.org/nic/hosts?domain=dyn.dhs.org&hostname=\<h\>&hostscmd=edit&hostscmdstage=2&type=1&ip=\<a\>

HP

https://*server-name*/nic/update?group=*group-name*&myip=\<a\>

ODS

ods://update.ods.org

GNUDIP

gnudip://*server-name*

花生壳

oray://phservice2.oray.net

其中：

·URL地址中不支持携带用户名和密码，配置用户名和密码请配合**username**和**password**命令使用，请根据实际情况修改。

·HP和GNUDIP是通用的DDNS更新协议，*server-name*是使用对应DDNS更新协议的服务提供商的服务器域名或地址。

·DDNS更新请求的URL地址可以以"http://"开头，表示基于HTTP与DDNS服务器通信；以"https://"开头，表示基于HTTPS与DDNS服务器通信；以"ods://"开头，表示基于TCP与ODS服务器通信；以"gnudip://"开头，表示基于TCP与GNUDIP服务器通信；以"oray://"开头，表示基于TCP与花生壳DDNS服务器通信。

·members.3322.org和phservice2.oray.net是服务提供商提供DDNS服务的域名。花生壳提供DDNS服务的域名可能是phservice2.oray.net、phddns60.oray.net、client.oray.net和ph031.oray.net等，请根据实际情况修改域名。

·URL地址中的端口号是可选项，如果不包含端口号则使用缺省端口号：HTTP是80，HTTPS是443，花生壳DDNS服务器是6060。

·\<h\>由系统根据接口上应用DDNS策略时指定的FQDN自动填写，\<a\>由系统根据应用DDNS策略的接口的主IP地址自动填写，用户可以不更改URL中的\<h\>和\<a\>。用户也可以手工输入需要更新的FQDN和IP地址，代替URL中的\<h\>和\<a\>，此时，应用DDNS策略时指定的FQDN将不会生效。为了避免配置错误，建议用户不要修改URL中的\<h\>和\<a\>。

·花生壳DDNS服务器的URL地址中不能指定用于更新的FQDN和IP地址。用户可在接口上应用DDNS策略时指定FQDN；用于更新的IP地址是应用DDNS策略的接口的主IP地址。

需要注意的是：

·为避免歧义，请尽量不要在DDNS服务器上申请含有":"、"@"或"?"字符的用户名和密码。

·重复执行本命令，配置不同的URL地址时，新的配置会覆盖已有配置。

【举例】

\# 为DDNS策略steven_policy指定DDNS更新请求的URL地址。DDNS服务提供商为www.3322.org。

\<Sysname\> system-view

Sysname ddns policy steven_policy

Sysname-ddns-policy-steven_policy url http:// members.3322.org/dyndns/update?system=dyndns&hostname=\<h\>&myip=\<a\>

【相关命令】

·**display** **ddns** **policy**

·**ddns** **policy**

·**password**

·**username**

**DDNS \-- DDNS配置命令 \-- username**

------------------------------------------------------------------------

**[username**]命令用来指定DDNS更新请求的URL地址中的用户名。

**[undo** **username**]命令用来删除DDNS更新请求的URL地址中的用户名。

【命令】

**[username**]*username*

**[undo** **username**]

【缺省情况】

未指定DDNS更新请求的URL地址中的用户名。

【视图】

DDNS策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[username*]：DDNS更新请求的URL地址中的用户名，为1～32个字符的字符串，区分大小写。

【举例】

\# 为DDNS策略steven_policy指定DDNS更新请求的URL地址中的登录用户名为steven。

\<Sysname\> system-view

Sysname ddns policy steven_policy

Sysname-ddns-policy-steven_policy username steven

【相关命令】

·**display ddns policy**

·**ddns policy**

·**password**

·**url**
