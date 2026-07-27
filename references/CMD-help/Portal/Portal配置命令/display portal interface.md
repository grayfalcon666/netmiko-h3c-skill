<!-- CMD-INDEX
  display portal interface            | 任意视图             | L47
  display portal packet statistics    | 任意视图             | L447
  display portal rule                 | 任意视图             | L643
  display portal server               | 任意视图             | L1297
  display portal user                 | 任意视图             | L1401
  display portal web-server           | 任意视图             | L2029
  display web-redirect rule           | 任意视图             | L2127
  ip                                  | Portal认证服务器视图    | L2367
  ipv6                                | Portal认证服务器视图    | L2433
  port                                | Portal认证服务器视图    | L2499
  portal { bas-ip \| bas-ipv6 }       | 接口视图             | L2549
  portal apply web-server             | 接口视图             | L2621
  portal authorization strict-checking | 接口视图             | L2693
  portal delete-user                  | 系统视图             | L2757
  portal domain                       | 接口视图             | L2799
  portal enable                       | 接口视图             | L2865
  portal fail-permit server           | 接口视图             | L2943
  portal free-all except destination  | 接口视图             | L3009
  portal free-rule                    | 系统视图             | L3083
  portal free-rule source             | 系统视图             | L3169
  portal { ipv4-max-user \| ipv6-max-user } | 接口视图             | L3225
  portal ipv6 free-all except destination | 接口视图             | L3289
  portal ipv6 layer3 source           | 接口视图             | L3361
  portal ipv6 user-detect             | 接口视图             | L3431
  portal layer3 source                | 接口视图             | L3511
  portal max-user                     | 系统视图             | L3583
  portal nas-id-profile               | 接口视图             | L3637
  portal nas-port-id format           | 系统视图             | L3701
  portal pre-auth domain              | 三层接口视图/三层子接口视图   | L3851
  portal pre-auth ip-pool             | 接口视图             | L3913
  portal roaming enable               | 系统视图             | L3987
  portal server                       | 系统视图             | L4037
  portal user-detect                  | 接口视图             | L4089
  portal web-server                   | 系统视图             | L4169
  reset portal packet statistics      | 用户视图             | L4221
  server-detect (portal server view)  | Portal认证服务器视图    | L4259
  server-detect (portal web-server view) | Portal Web服务器视图  | L4317
  url                                 | Portal Web服务器视图  | L4375
  url-parameter                       | Portal Web服务器视图  | L4425
  user-sync                           | Portal认证服务器视图    | L4491
  vpn-instance                        | Portal Web服务器视图  | L4549
  web-redirect track                  | 接口视图             | L4595
  web-redirect url                    | 接口视图             | L4661
-->

**Portal \-- Portal配置命令 \-- display portal interface**

------------------------------------------------------------------------

**[display portal interface**]命令用来显示指定接口上的Portal配置信息和Portal运行状态信息。

【命令】

**[display portal interface ***interface-type interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：表示接口类型和接口编号。

【举例】

·路由应用

\# 显示接口GigabitEthernet1/0/1的Portal配置信息和Portal运行状态信息。

\<Sysname\> display portal interface gigabitEthernet1/0/1

 Portal information of GigabitEthernet1/0/1

     Nas id profile: aaa

     VSRP instance : instance1

     VSRP state    : Master

     Authorization : Strict checking

     ACL           : Enabled

     User profile  : Disabled

 IPv4:

     Portal status: Enabled

     Portal VSRP status: M_Delay

     Authentication type: Layer3

     Portal Web server: wbs

     Authentication domain: my-domain

     Pre-auth domain: abc

     Pre-auth IP pool: ab

BAS-IP: Not configured

User detection: Type: ICMP  Interval: 300s  Attempts: 5  Idle time: 180s

Action for sever detection:

         Server type    Server name                        Action

         Web server     wbs                                fail-permit

         Portal server  pts                                fail-permit

     Layer3 source network:

         IP address               Mask

         1.1.1.1                  255.255.0.0

     Destination authentication subnet:

         IP address               Mask

         2.2.2.2                  255.255.255.0

IPv6:

     Portal status: enabled

     Portal VSRP status: M_Alone

     Authentication type: layer3

     Portal Web server: wbsv6

     Authentication domain: my-domain

     Pre-auth domain: abc

     Pre-auth IP pool: Not configured

     BAS-IPv6: Not configured

User detection: Type: ICMPv6  Interval: 300s   Attempts: 5   Idle time: 180s

Action for sever detection:

         Server type    Server name                        Action

         Web server     wbsv6                              fail-permit

         Portal server  ptsv6                              fail-permit

     Layer3 source network:

         IP address                                        Prefix length

         11::5                                             64

     Destination authentication subnet:

         IP address                                        Prefix length

·交换应用

\# 显示接口Vlan-interface2的Portal配置信息和Portal运行状态信息。

\<Sysname\> display portal interface vlan-interface 2

 Portal information of Vlan-interface2

     Nas id profile: aaa

     VSRP instance : instance1

     VSRP status   : Master

     Authorization : Strict checking

     ACL           : Enabled

     User profile  : Disabled

 IPv4:

     Portal status: Enabled

     Portal VSRP status: M_Delay

     Authentication type: Direct

     Portal Web server  : wbs

     Authentication domain: my-domain

     Pre-auth domain: abc

     Pre-auth IP pool: Not configured

BAS-IP: Not configured

     User detection: Type: ICMP  Interval: 300s  Attempts: 5   Idle time: 180s

     Action for server detection:

         Server type    Server name                        Action

         Web server     wbs                                fail-permit

         Portal server  pts                                fail-permit

     Layer3 source network:

         IP address               Mask

         1.1.1.1                  255.255.0.0

     Destination authentication subnet:

         IP address               Mask

         2.2.2.2                  255.255.255.0

 IPv6:

     portal status: Enabled

     Portal VSRP status: M_Alone

     Authentication type: Direct

     Portal Web server: wbsv6

     Authentication domain: my-domain

     Pre-auth domain: abc

     Pre-auth IP pool: Not configured

     BAS-IPv6:Not configured

     User detection: Type: ICMPv6  Interval: 300s  Attempts: 5   Idle time: 180s

Action for server detection:

         Server type    Server name                        Action

         Web server     wbsv6                              fail-permit

         Portal server  ptsv6                              fail-permit

     Layer3 source network:

         IP address                                        Prefix length

         11::5                                             64

     Destination authentication subnet:

         IP address                                        Prefix length

表1-1 display portal interface命令显示信息描述表

字段

描述

Portal information of interface

接口上的Portal信息

NAS-ID profile

接口上引用的NAS-ID profile

VSRP instance

接口上引用的VSRP实例名称

VSRP state

接口的VSRP状态，包括以下取值：

·Master：表示在该VSRP实例中，本设备为主用设备

·Backup：表示在该VSRP实例中，本设备为备用设备

·Down：表示在该VSRP实例中，本设备不运行（在下面两种情况下设备会处于Down状态：一是当VRRP备份组处于init状态时，互相备份的两台设备在对应VSRP实例中都处于无法运行状态；二是本端VSRP实例不存在或者配置不完整）

·N/A：表示接口上未引用VSRP实例

Authorization

服务器下发给Portal用户的授权信息类型，包括ACL和User profile

Strict checking

Portal授权信息的严格检查模式是否开启

IPv4

IPv4 Portal的相关信息

IPv6

IPv6 Portal的相关信息

Portal status

接口上Portal认证的运行状态，包括以下取值：

·Disabled：Portal认证未使能

·Enabled：Portal认证已使能

·Authorized：Portal认证服务器或者Portal Web服务器不可达，端口自动开放

Portal VSRP status

接口的Portal VSRP状态，包括如下取值：

·M_Initial：主用设备的初始化状态

·M_Delay：主用设备的延迟状态（主用设备延迟一段时间后切换为主状态）

·M_Alone：主用设备的单机状态（备份数据链路断开等原因，导致双机通信失败）

·M_Hello：主用设备处于和备用设备进行握手的状态（协商VSRP状态和接口的Portal使能状态）

·M_Collect：主用设备处于等待备用设备发送Portal用户信息的状态

·M_Sync：主用设备处于向备用设备发送Portal用户信息的状态

·M_Synced：主用设备已经完成向备用设备备份Portal用户信息

·B_Initial：备用设备的初始化状态

·B_Alone：备用设备的单机状态（备份数据链路断开等原因，导致双机通信失败）

·B_Hello：备用设备处于和主用设备进行握手的状态（协商VSRP状态和接口的Portal使能状态）

·B_Report：备用设备处于向主用设备发送Portal用户信息的状态

·B_Sync：备用设备处于接收主用设备发送Portal用户信息的状态

·B_Synced：备用设备已经完成Portal用户信息的备份

·Down：未运行VSRP状态

接口未使能Portal或者未引用VSRP实例时不显示该字段

Authentication type

接口上配置的认证方式，包括以下取值：

·Direct：直接方式

·Redhcp：二次地址方式

·Layer3：可跨三层路由方式

Portal Web server

接口上配置的Portal Web服务器的名称

Authentication domain

接口上的Portal强制认证域

Pre-auth domain

接口上的Portal认证前域，即Portal认证前用户使用的认证域，未指定则显示Not configured

Pre-auth ip-pool

为认证前的Portal用户指定的IP地址池名称

BAS-IP

发送给Portal认证服务器的Portal报文的BAS-IP属性

BAS-IPv6

发送给Portal认证服务器的Portal报文的BAS-IPv6属性

User detection

接口上配置的用户在线状态探测配置，包括探测的方法（ARP、ICMP、ND、ICMPv6），探测周期和探测尝试次数，用户闲置的时间

Action for server detection

服务器可达性探测功能对应的端口控制配置：

·Server type：服务器类型，包括Portal server和Web server，分别表示Portal认证服务器和Portal Web服务器

·Server name：服务器名称

·Action：对应的接口根据服务器探测结果所采取的动作，为不需要认证（fail-permit）

Layer3 source subnet

Portal源认证网段信息

Destination authentication subnet

Portal目的认证网段认证信息

IP address

Portal认证网段的IP地址

Mask

Portal认证网段的子网掩码

Prefix length

Portal IPv6认证网段的地址前缀长度

【相关命令】

·**portal domain**

·**portal enable**

·**portal free-all except destination**

·**portal ipv6 free-all except destination**

·**portal ipv6 layer3 source**

·**portal layer3 source**

·**portal web-server**

**Portal \-- Portal配置命令 \-- display portal packet statistics**

------------------------------------------------------------------------

**[display portal packet statistics**]命令用来显示Portal认证服务器的报文统计信息，包括设备接收到Portal认证服务器发送的报文以及设备发送给该Portal认证服务器的报文的信息。

【命令】

**[display portal packet statistics** [ **server** *server-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[server**]*server-name*：Portal认证服务器的名称，为1～32个字符的字符串，区分大小写。

【使用指导】

若不指定参数**server**，则依次显示所有Portal认证服务器的报文统计信息。

【举例】

\# 显示名字为pts的Portal认证服务器的报文统计信息。

\<Sysname\> display portal packet statistics server pts

 Portal server :  pts

 Invalid packets: 0

 Pkt-Type                            Total    Drops    Errors

 REQ_CHALLENGE                       3        0        0

 ACK_CHALLENGE                       3        0        0

 REQ_AUTH                            3        0        0

 ACK_AUTH                            3        0        0

 REQ_LOGOUT                          1        0        0

 ACK_LOGOUT                          1        0        0

 AFF_ACK_AUTH                        3        0        0

 NTF_LOGOUT                          1        0        0

 REQ_INFO                            6        0        0

 ACK_INFO                            6        0        0

 NTF_USERDISCOVER                    0        0        0

 NTF_USERIPCHANGE                    0        0        0

 AFF_NTF_USERIPCHAN                  0        0        0

 ACK_NTF_LOGOUT                      1        0        0

 NTF_USER_HEARTBEAT                  2        0        0

 ACK_NTF_USER_HEARTBEAT              0        0        0

 NTF_CHALLENGE                       0        0        0

 NTF_USER_NOTIFY                     0        0        0

 AFF_NTF_USER_NOTIFY                 0        0        0

表1-2 display portal server statistics命令显示信息描述表

字段

描述

Portal server

Portal认证服务器名称

Invalid packets

无效报文的数目

Pkt-Type

报文的名称

Total

报文的总数

Drops

丢弃报文数

Errors

错误报文数

REQ_CHALLENGE

Portal认证服务器向接入设备发送的challenge请求报文

ACK_CHALLENGE

接入设备对Portal认证服务器challenge请求的响应报文

REQ_AUTH

Portal认证服务器向接入设备发送的请求认证报文

ACK_AUTH

接入设备对Portal认证服务器认证请求的响应报文

REQ_LOGOUT

Portal认证服务器向接入设备发送的下线请求报文

ACK_LOGOUT

接入设备对Portal认证服务器下线请求的响应报文

AFF_ACK_AUTH

Portal认证服务器收到认证成功响应报文后向接入设备发送的确认报文

NTF_LOGOUT

接入设备发送给Portal认证服务器，用户被强制下线的通知报文

REQ_INFO

信息询问报文

ACK_INFO

信息询问的响应报文

NTF_USERDISCOVER

Portal认证服务器向接入设备发送的发现新用户要求上线的通知报文

NTF_USERIPCHANGE

接入设备向Portal认证服务器发送的通知更改某个用户IP地址的通知报文

AFF_NTF_USERIPCHAN

Portal认证服务器通知接入设备对用户表项的IP切换已成功报文

ACK_NTF_LOGOUT

Portal认证服务器对强制下线通知的响应报文

NTF_USER_HEARTBEAT

接入设备收到的从Portal认证服务器发送的用户同步报文

ACK_NTF_USER_HEARTBEAT

接入设备向Portal认证服务器回应的用户同步响应报文

NTF_HEARTBEAT

Portal认证服务器周期性向接入设备发送的服务器心跳报文

NTF_CHALLENGE

接入设备向Portal认证服务器发送的challenge请求报文

NTF_USER_NOTIFY

接入设备向Portal认证服务器发送的用户消息通知报文

AFF_NTF_USER_NOTIFY

Portal认证服务器向接入设备发送的对NTF_USER_NOTIFY的确认报文

【相关命令】

·**reset portal ****packet statistics**

**Portal \-- Portal配置命令 \-- display portal rule**

------------------------------------------------------------------------

**[display portal rule**]命令用来显示指定接口上用于报文匹配的Portal过滤规则信息。

【命令】

集中式设备：

**[display portal rule**[ { **all** \| **dynamic** \| **static** } **interface** *interface-type interface-number* ]]

分布式设备-独立运行模式/集中式IRF设备：

**[display portal rule **[{ **all** \| **dynamic** \| **static** } **interface** *interface-type interface-number* [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备-IRF设备：

**[display portal rule **[{ **all** \| **dynamic** \| **static** } **interface** *interface-type interface-number* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有Portal规则信息，包括动态Portal规则和静态Portal规则。

**[dynamic**]：显示动态Portal规则信息，即用户通过Portal认证后设备上产生的Portal规则，这类规则定义了允许指定源IP地址的报文通过接口。

**[static**]：显示静态Portal规则信息，即使能Portal后产生的Portal规则，这类规则定义了在Portal功能开启后对接口上收到的报文的过滤动作。

**[interface** *interface-type interface-number*]：显示指定接口的Portal规则信息。*interface-type interface-number*为接口类型和接口编号。

**[slot ***slot-number*]：显示指定单板上的Portal规则信息，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示所有单板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的Portal规则信息，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则表示所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的Portal规则信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示所有成员设备/PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的Portal规则信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的Portal规则信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示所有单板。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的Portal规则信息，*cpu-number*表示CPU编号，只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

·路由应用

\# 显示接口GigabitEthernet1/0/1上所有Portal过滤规则的信息。

\<Sysname\> display portal rule all interface gigabitethernet 1/0/1

IPv4 portal rules on GigabitEthernet1/0/1:

Rule 1

 Type                : Static

 Action              : Permit

 Protocol            : Any

 Status              : Active

 Source:

    IP             : 0.0.0.0

    Mask           : 0.0.0.0

    Port           : Any

    MAC            : 0000-0000-0000

    Interface      : GigabitEthernet1/0/1

VLAN           : Any

 Destination:

    IP             : 192.168.0.111

    Mask           : 255.255.255.255

    Port           : Any

Rule 2

 Type                : Dynamic

 Action              : Permit

 Status              : Active

 Source:

    IP             : 2.2.2.2

    MAC            : 000d-88f8-0eab

    Interface      : GigabitEthernet1/0/1

VLAN           : Any

Author ACL:

    Number         : 3001

Rule 3

 Type                : Static

 Action              : Redirect

 Status              : Active

 Source:

    IP             : 0.0.0.0

    Mask           : 0.0.0.0

Interface      : GigabitEthernet1/0/1

    VLAN           : Any

    Protocol       : TCP

 Destination:

    IP             : 0.0.0.0

Mask           : 0.0.0.0

    Port           : 80

Rule 4:

 Type                : Static

 Action              : Deny

Status              : Active

 Source:

    IP             : 0.0.0.0

    Mask           : 0.0.0.0

    Interface      : GigabitEthernet1/0/1

    VLAN           : Any

 Destination:

    IP             : 0.0.0.0

Mask           : 0.0.0.0

IPv6 portal rules on GigabitEthernet1/0/1:

Rule 1

 Type                : Static

 Action              : Permit

 Protocol            : Any

 Status              : Active

 Source:

    IP             : ::

    Prefix length  : 0

    Port           : Any

    MAC            : 0000-0000-0000

    Interface      : GigabitEthernet1/0/1

    VLAN           : Any

 Destination:

    IP             : 3000::1

    Prefix length  : 64

    Port           : Any

Rule 2

 Type                : Dynamic

 Action              : Permit

 Status              : Active

 Source:

    IP              : 3000::1

    MAC             : 0015-e9a6-7cfe

    Interface       : GigabitEthernet1/0/1

    VLAN            : Any

 Author ACL:

    Number          : 3001

Rule 3

 Type                : Static

 Action              : Redirect

 Status              : Active

 Source:

    IP              : ::

    Prefix length   : 0

    Interface       : GigabitEthernet1/0/1

    VLAN            : Any

    Protocol        : TCP

 Destination:

    IP              : ::

    Prefix length   : 0

    Port            : 80

Rule 4:

 Type                : Static

 Action              : Deny

Status              : Active

 Source:

    IP             : ::

    Prefix length  : 0

    Interface      : GigabitEthernet1/0/1

    VLAN           : Any

 Destination:

    IP             : ::

Prefix length  : 0

Rule 5:

 Type                : Static

 Action              : Match pre-auth ACL

 Status              : Active

 Source:

    Interface      : GigabitEthernet1/0/1

Pre-auth ACL:

    Number          : 3002

·交换应用

\# 显示接口Vlan-interface100上所有Portal过滤规则的信息。

\<Sysname\> display portal rule all interface vlan-interface 100

IPv4 portal rules on Vlan-interface100:

Rule 1

 Type                : Static

 Action              : Permit

 Protocol            : Any

 Status              : Active

 Source:

    IP             : 0.0.0.0

    Mask           : 0.0.0.0

    Port           : Any

    MAC            : 0000-0000-0000

    Interface      : Vlan-interface100

VLAN           : 100

 Destination:

    IP             : 192.168.0.111

    Mask           : 255.255.255.255

    Port           : Any

Rule 2

 Type                : Dynamic

 Action              : Permit

 Status              : Active

 Source:

    IP             : 2.2.2.2

    MAC            : 000d-88f8-0eab

    Interface      : GigabitEthernet1/0/1

VLAN           : 100

Author ACL:

    Number         : 3001

Rule 3

 Type                : Static

 Action              : Redirect

 Status              : Active

 Source:

    IP             : 0.0.0.0

    Mask           : 0.0.0.0

Interface      : Vlan-interface100

    VLAN           : 100

    Protocol       : TCP

 Destination:

    IP             : 0.0.0.0

Mask           : 0.0.0.0

    Port           : 80

Rule 4:

 Type                : Static

 Action              : Deny

Status              : Active

 Source:

    IP             : 0.0.0.0

    Mask           : 0.0.0.0

    Interface      : Vlan-interface100

    VLAN           : Any

 Destination:

    IP             : 0.0.0.0

Mask           : 0.0.0.0

IPv6 portal rules on Vlan-interface100:

Rule 1

 Type                : Static

 Action              : Permit

 Protocol            : Any

 Status              : Active

 Source:

    IP              : ::

    Prefix length   : 0

    Port            : Any

    MAC             : 0000-0000-0000

    Interface       : Vlan-interface100

    VLAN            : 100

 Destination:

    IP               : 3000::1

    Prefix length    : 64

    Port             : Any

Rule 2

 Type                : Dynamic

 Action              : Permit

 Status              : Active

 Source:

    IP              : 3000::1

    MAC             : 0015-e9a6-7cfe

    Interface       : GigabitEthernet1/0/1

    VLAN            : 100

 Author ACL:

    Number          : 3001

Rule 3

 Type                : Static

 Action              : Redirect

 Status              : Active

 Source:

    IP              : ::

    Prefix length   : 0

    Interface       : Vlan-interface100

    VLAN            : 100

    Protocol        : TCP

 Destination:

    IP              : ::

    Prefix length   : 0

    Port            : 80

Rule 4:

 Type                : Static

 Action              : Deny

Status              : Active

 Source:

    IP             : ::

    Prefix length  : 0

    Interface      : Vlan-interface100

    VLAN           : 100

 Destination:

    IP             : ::

Prefix length  : 0

Author ACL:

    Number          : 3001

Rule 5:

 Type                : Static

 Action              : Match pre-auth ACL

 Status              : Active

 Source:

    Interface      : Vlan-interface100

Pre-auth ACL:

    Number          : 3002

表1-3 display portal rule命令显示信息描述表

字段

描述

Rule

Portal过滤规则编号。IPv4过滤规则和IPv6过滤规则分别编号

Type

Portal过滤规则的类型，包括以下取值：

·Static：静态类型

·Dynamic：动态类型

Action

Portal过滤规则的匹配动作，包括以下取值：

·Permit：允许报文通过

·Redirect：重定向报文

·Deny：拒绝报文通过

·Match pre-auth ACL：匹配认证前域中的授权ACL规则

Protocol

Portal过滤规则的传输层协议，包括以下取值：

·Any：不限制传输层协议类型

·TCP：TCP传输类型

·UDP：UDP传输类型

Status

Portal过滤规则下发的状态，包括以下取值：

·Active：表示规则已生效

·Unactuated：表示规则未生效

Source

Portal过滤规则的源信息

IP

源IP地址

Mask

源IPv4地址子网掩码

Prefix length

源IPv6地址前缀

Port

源传输层端口号

MAC

源MAC地址

Interface

Portal过滤规则应用的二层或三层接口

VLAN

源VLAN

Protocol

Portal规则的协议类型

Destination

Portal规则的目的信息

IP

目的IP地址

Port

目的传输层端口号

Mask

目的IPv4地址子网掩码

Prefix length

目的IPv6地址前缀

Author ACL

Portal用户认证后的授权ACL，即AAA授权给用户的ACL，该字段仅在Type为Dynamic时才显示

Pre-auth ACL

Portal用户认证前的授权ACL，该字段仅在Action为Match pre-auth ACL时显示

Number

授权ACL编号，N/A表示AAA未授权ACL

**Portal \-- Portal配置命令 \-- display portal server**

------------------------------------------------------------------------

**[display portal server**]命令用来显示Portal认证服务器信息。

【命令】

**[display portal server** [ *server-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[server-name*]：Portal认证服务器的名称，为1～32个字符的字符串，区分大小写。

【使用指导】

若不指定参数*server-name*，则显示所有Portal认证服务器信息。

【举例】

\# 显示Portal认证服务器pts的信息。

\<Sysname\> display portal server pts

Portal server: pts

  IP                    : 192.168.0.111

  VPN instance          : vpn1

  Port                  : 50100

  Server detection      : Timeout 60s  Action: log, trap

  User synchronization  : Timeout 200s

  Status                : Up

表1-4 display portal server命令显示信息描述表

字段

描述

Portal server

Portal认证服务器名称

IP

Portal认证服务器的IP地址

VPN instance

Portal认证服务器所属的MPLS L3VPN

该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

Port

Portal认证服务器的监听端口

Server detection

Portal认证服务器可达性探测功能的参数，包括超时时间（单位：秒），以及探测到服务器状态变化后触发的动作（log、trap）

User synchronization

Portal用户用户信息同步功能的参数，包括超时时间（单位：秒）

Status

Portal认证服务器当前状态，其取值如下：

·N/A：服务器可达性探测功能未开启，可达状态未知

·Up：服务器可达性探测功能已开启，探测结果为该服务器当前可达

·Down：服务器可达性探测功能已开启，探测结果为该服务器当前不可达

【相关命令】

·**portal enable**

·**portal server**

·**server-detect** (portal server view)

·**user-sync**

**Portal \-- Portal配置命令 \-- display portal user**

------------------------------------------------------------------------

**[display portal user**]命令用来显示Portal用户的信息。

【命令】

**[display portal user**[ { **all** \| **interface** *interface-type interface-number \|* **ip** *ip-address* \| **ipv6** *ipv6-address* \| **pre-auth** [ **interface** { *interface-type interface-number* \| *interface-name* } \| **ip** *ip-address* \| **ipv6** *ipv6-address* ] }  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[pre-auth**]：显示Portal认证前用户信息。若不指定该参数，则显示Portal用户的信息。

**[all**]：显示所有Portal用户的信息。

**[interface**] *interface-type interface-number*：显示指定接口上的Portal用户信息。*interface-type interface-number*为接口类型和接口编号。

**[ip** *ipv4-address*]：显示指定IPv4地址的Portal用户信息。

**[ipv6** *ipv6-address*]：显示指定IPv6地址的Portal用户信息。

**[verbose**]：显示指定Portal用户的详细信息。

【举例】

·路由应用

\# 显示所有Portal用户的信息。

\<Sysname\> display portal user all

Total portal users: 2

Username: abc

  Portal server: pts

  State: Online

  VPN instance: N/A

  MAC                IP                 VLAN   Interface

  000d-88f8-0eab     2.2.2.2            \--     GigabitEthernet1/0/1

  Authorization information:

    DHCP IP pool: N/A

    User profile: abc (active)

    Session group profile: cd (inactive)

    ACL number: N/A

    Inbound CAR: N/A

    Outbound CAR: N/A

Username: def

  Portal server: pts

  State: Online

  VPN instance: vpn1

  MAC                IP                 VLAN   Interface

  000d-88f8-0eac     3.3.3.3            \--     GigabitEthernet1/0/2

  Authorization information:

    DHCP IP pool: N/A

User profile: N/A

    Session group profile: N/A

    ACL number: 3000

\# 显示IP地址为50.50.50.3的Portal用户的详细信息。

\<Sysname\> display portal user ip-address 50.50.50.3 verbose

Basic：

  Current IP address: 50.50.50.3

  Original IP address: 30.30.30.2

  Username: user1@hrss

  User ID: 0x28000002

  Access interface: eth3/2/2

  Service-VLAN/Customer-VLAN: -/-

  MAC address: 0000-0000-0001

  Domain: hrss

  VPN instance: 123

  Status: Online

  Portal server: test

  Portal authentication method: Direct

AAA:

 Realtime accounting interval: 60s, retry times: 3

  Idle-cut:180 sec, 10240 bytes

  Session duration: 500 sec, remaining: 300 sec

  Remaining traffic: 10240000 bytes

  Login time: 2014-01-19  2:42:3 UTC

  ITA policy name: test

  IP pool: abc

ACL&QoS&Multicast:

  Inbound CAR: CIR 64000bps PIR 640000bps

  Outbound CAR: CIR 64000bps PIR 640000bps

  ACL number:3000（inactive）

  User profile: portal (active)

  Session group profile: N/A

  Max multicast addresses: 4

  Multicast address list: 1.2.3.1, 1.34.33.1, 3.123.123.3, 4.5.6.7

2.2.2.2, 3.3.3.3, 4.4.4.4

Flow statistic:

  Uplink   packets/bytes: 7/546

  Downlink packets/bytes: 0/0

ITA:

  level-1 uplink   packets/bytes: 4/32

          downlink packets/bytes: 2/12

  level-2 uplink   packets/bytes: 0/0

          downlink packets/bytes: 0/0

·交换应用

\# 显示所有Portal用户的信息。

\<Sysname\> display portal user all

Total portal users: 2

Username: abc

  Portal server: pts

  State: Online

  VPN instance: N/A

  MAC                IP                 VLAN   Interface

  000d-88f8-0eab     2.2.2.2            100    Vlan-interface100

  Authorization information:

    DHCP IP pool: N/A

    User profile: abc （active）

    Session group profile: bcd (inactive)

    ACL number: N/A

    Inbound CAR: N/A

    Outbound CAR: N/A

Username: def

  Portal server: pts

  State: Online

  VPN instance: vpn1

  MAC                IP                 VLAN   Interface

  000d-88f8-0eac     3.3.3.3            200    Vlan-interface200

  Authorization information:

    DHCP IP pool: N/A

User profile: N/A

    Session group profile: N/A

ACL number: 3001

    Inbound CAR: CIR    3072 bps        PIR     3072 bps

    Outbound CAR: CIR    3072 bps        PIR     3072 bps

\# 显示所有Portal认证前用户的信息。

\<Sysname\> display portal user pre-auth

Total portal pre-auth users: 2

  MAC             IP                    VLAN    Interface

  000a-eb29-75f1  18.18.0.3             200     Route-Aggregation100

  State: Online

  VPN instance: N/A

  Authorization information:

    User profile: quew (active)

    Session group profile: pt1 (active)

    ACL number: 3000 (active)

    Inbound CAR: CIR    3072 bps        PIR     3072 bps

    Outbound CAR: CIR    3072 bps         PIR     3072 bps

  MAC             IP                    VLAN    Interface

  000a-eb29-75f2  18.18.0.4             200     Route-Aggregation100

  State: Online

  VPN instance: N/A

  Authorization information:

    User profile: quew (active)

    Session group profile: pt1 (active)

    ACL number: 3000 (active)

    Inbound CAR: CIR    3072 bps        PIR     3072 bps

    Outbound CAR: CIR    3072 bps         PIR     3072 bp

\# 显示IP地址为50.50.50.3的Portal用户的详细信息。

\<Sysname\>display portal user ip-address 50.50.50.3 verbose

Basic:

  Current IP address: 50.50.50.3

  Original IP address: 30.30.30.2

  Username: user1@hrss

  User ID: 0x28000002

  Access interface: eth3/2/2

  Service-VLAN/Customer-VLAN: -/-

  MAC address: 0000-0000-0001

  Domain: hrss

  VPN instance: 123

  Status: Online

  Portal server: test

  Portal authentication method: Direct

AAA:

  Realtime accounting interval: 60s, retry times: 3

  Idle-cut:180 sec, 10240 bytes

  Session duration: 500 sec, remaining: 300 sec

  Remaining traffic: 10240000 bytes

  Login time: 2014-01-19  2:42:3 UTC

  ITA policy name: test

  IP pool: abc

ACL&QoS&Multicast:

  Inbound CAR: CIR 64000bps PIR 640000bps

  Outbound CAR: CIR 64000bps PIR 640000bps

  ACL number: 3000（inactive）

  User profile: portal (active)

  Session group profile: N/A

  Max multicast addresses: 4

  Multicast address list: 1.2.3.1, 1.34.33.1, 3.123.123.3, 4.5.6.7

                          2.2.2.2, 3.3.3.3, 4.4.4.4

Flow statistic:

  Uplink   packets/bytes: 7/546

  Downlink packets/bytes: 0/0

ITA:

  level-1 uplink   packets/bytes: 4/32

          downlink packets/bytes: 2/12

  level-2 uplink   packets/bytes: 0/0

          downlink packets/bytes: 0/0

表1-5 display portal user命令显示信息描述表

字段

描述

Total portal users

总计的Portal用户数目

Username

用户名

Portal server

用户认证所使用的Portal认证服务器的名称

State

Portal用户的当前状态，包括以下取值：

·Initialized：初始化完成后的待认证状态

·Authenticating：正在认证状态

·Authorizing：正在授权状态

·Online：在线状态

VPN instance

Portal用户所属的MPLS L3VPN。若用户属于公网，则显示为N/A

该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准

MAC

Portal用户的MAC地址

IP

Portal用户的IP地址

VLAN

Portal用户所在的VLAN

Interface

Portal用户接入的接口

Authorization information

Portal用户的授权信息

DHCP IP pool

Portal用户的授权地址池名字。若无授权地址池，则显示为N/A

User profile

Portal用户的授权User Profile名称。若未授权User Profile，则显示为N/A。授权状态包括如下：

·active：AAA授权User profile成功

·inactive：AAA授权User profile失败或者设备上不存在该User profile

Session group profile

Portal用户的授权Session Group Profile名称。若未授权Session Group Profile，则显示为N/A。授权状态包括如下：

·active：AAA授权Session group profile成功

·inactive：AAA授权Session group profile失败或者设备上不存在该User profile

ACL number

Portal用户的授权ACL编号。若未授权ACL，则显示为N/A。授权状态包括如下：

·active：AAA授权ACL成功

·inactive：AAA授权ACL失败或者设备上不存在该ACL

Inbound CAR

授权的入方向CAR（CIR：平均速率，单位为bps；PIR：峰值速率，单位为bps）。若未授权入方向CAR，则显示为N/A

Outbound CAR

授权的出方向CAR（CIR：平均速率，单位为bps；PIR：峰值速率，单位为bps）。若未授权出方向CAR，则显示为N/A

表1-6 display portal user verbose命令显示信息描述表

字段

描述

Current IP address

Portal用户当前的IP地址

Original IP address

Portal用户认证时的IP地址

Username

Portal用户上线时使用的用户名

User ID

Portal用户ID

Access interface

Portal用户接入的接口

Service-VLAN/Customer-VLAN

Portal用户所在的公网VLAN/私网VLAN（"-"表示没有VLAN信息）

MAC address

用户的MAC地址

Domain

用户认证时使用的ISP域名

VPN instance

用户所属的MPLS L3VPN实例，N/A表示用户属于公网

Status

Portal用户的当前状态，包括以下取值：

·Authenticating：正在认证状态

·Authorizing：正在授权状态

·Waiting_SetRule：正在下发Portal规则状态

·Online：在线状态

·Waiting_Traffic：正在等待用户流量状态

·Stop Accounting：正在停止计费状态

·Offline：用户下线完成状态

Portal server

Portal服务器名称

Portal authentication method

接入接口上的Portal认证方式，包括如下取值：

·Direct：直接方式

·Re-Dhcp：二次地址方式

·Layer3：三层方式

AAA

Portal用户的AAA授权信息

Realtime accounting interval

授权的实时计费间隔和重传次数。若未授权，则显示为N/A

Idle-cut

授权的闲置切断时长和流量。若未授权，则显示为N/A

Session duration

授权的会话时长以及剩余的会话时长。若未授权，则显示为N/A

Remaining traffic

授权的剩余流量。若未授权，则显示为N/A

Login time

用户登录时间，即用户授权成功的时间，格式为设备时间，如：2023-1-19  2:42:30 UTC

ITA policy name

授权的ITA（Intelligent Target Accounting，智能靶向计费）策略名称

IP pool

授权的DHCP地址池名称。若未授权DHCP地址池，则显示为N/A

Inbound CAR

授权的入方向CAR（CIR：平均速率，单位为bps；PIR：峰值速率，单位为bps）。若未授权入方向CAR，则显示为N/A

Outbound CAR

授权的出方向CAR（CIR：平均速率，单位为bps；PIR：峰值速率，单位为bps）。若未授权出方向CAR，则显示为N/A

ACL number

授权的ACL编号。若未授权ACL，则显示为N/A。授权状态包括如下：

·active：AAA授权ACL成功

·inactive：AAA授权ACL失败或者设备上不存在该ACL

User profile

授权的User profile名称。若未授权User profile，则显示为N/A。授权状态包括如下：

·active：AAA授权User profile成功

·inactive：AAA授权User profile失败或者设备上不存在该User profile

Session group profile

授权的Session group profile名称。若未授权Session group profile，则显示为N/A。授权状态包括如下：

·active：AAA授权Session group profile成功

·inactive：AAA授权Session group profile失败或者设备上不存在该User profile

Max multicast addresses

授权Portal用户可加入的组播组的最大数目

Multicast address list

授权Portal用户可加入的的组播组列表。若未授权组播组列表，则显示为N/A

Flow statistic

Portal用户流量统计信息

Uplink packets/bytes

上行流量报文数/字节数

Downlink packets/bytes

下行流量报文数/字节数

ITA

Portal用户的ITA业务流量统计信息

level-*n* uplink packets/bytes

计费等级为*n*的上行流量报文数/字节数，*n*的取值范围为1～8

level-n downlink packets/bytes

计费等级为*n*的下行流量报文数/字节数，*n*的取值范围为1～8

【相关命令】

·**portal enable**

**Portal \-- Portal配置命令 \-- display portal web-server**

------------------------------------------------------------------------

**[display portal web-server**]命令用来显示Portal Web服务器信息。

【命令】

**[display portal web-server**  *server-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[server-name*]：Portal Web服务器的名称，为1～32个字符的字符串，区分大小写。

【使用指导】

若不指定参数*server-name*，则显示所有Portal Web服务器信息。

【举例】

\# 显示Portal Web服务器wbs的信息。

\<Sysname\> display portal web-server wbs

Portal Web server: wbs

    URL              : http://www.test.com/portal

    URL parameters   : userurl=http://www.test.com/welcome

                       userip=source-address

    VPN instance     : Not configured

    Server detection : Interval: 120s  Attempts: 5  Action: log, trap

    IPv4 status      : Up

    IPv6 status      : N/A

表1-7 display portal web-server命令显示信息描述表

字段

描述

Portal Web server

Portal Web服务器名称

URL

Portal Web服务器的URL地址以及携带的参数

URL parameters

Portal Web服务器的URL携带的参数信息

VPN instance

Portal Web服务器所属的MPLS L3VPN实例名称

Server detection

Portal Web服务器可达性探测功能的参数，包括探测间隔时间（单位：秒），探测尝试次数以及探测到服务器状态变化后的动作（log、trap）

IPv4/IPv6 status

Portal web服务器当前状态，其取值如下：

·N/A：服务器可达性探测功能未开启，可达状态未知

·Up：服务器可达性探测功能已开启，且探测结果为该服务器当前可达

·Down：服务器可达性探测功能已开启，且探测结果为该服务器当前不可达

【相关命令】

·**portal enable**

·**portal web-server**

·**server-detect** (portal web-server view)

**Portal \-- Portal配置命令 \-- display web-redirect rule**

------------------------------------------------------------------------

**[display web-redirect rule**]命令用来显示指定接口上的Web重定向过滤规则信息。

【命令】

集中式设备：

**[display web-redirect rule interface ***interface-type interface-number*]

分布式设备---独立运行模式/集中式IRF设备：

**[display web-redirect rule** **interface** *interface-type interface-number* [ **slot** *slot-number* ]]

分布式设备---IRF设备：

**[display web-redirect rule** **interface** *interface-type interface-number* [ **chassis** *chassis-number * **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

vd-admin

vd-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的Web重定向过滤规则信息。interface-type interface-number为接口类型和接口编号。

**[slot ***slot-number*]：显示指定单板上指定接口的Web重定向过滤规则信息。*slot-number*表示单板所在槽位号。若不指定该参数，则显示主用主控板上的Web重定向过滤规则信息。（分布式设备-独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上指定接口的Web重定向过滤规则信息。*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则显示主用设备上的Web重定向过滤规则信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上指定接口的Web重定向过滤规则信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则显示主用设备/PEX上的Web重定向过滤规则信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上指定接口的Web重定向过滤规则，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在槽位号。若不指定该参数，则显示全局主用主控板上的Web重定向过滤规则信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上指定接口的Web重定向过滤规则，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板所在槽位号或PEX。若不指定该参数，则显示全局主用主控板上的Web重定向过滤规则信息。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

·路由应用

\# 显示接口GigabitEthernet1/0/1上的所有Web重定向过滤规则。

\<Sysname\> display web-redirect rule interface gigabitethernet 1/0/1

IPv4 web-redirect rules on GigabitEthernet1/0/1:

Rule 1:

 Type                : Dynamic

 Action              : Permit

 Status              : Active

 Source:

    IP             : 192.168.2.114

    VLAN           : Any

Rule 2:

 Type                : Static

 Action              : Redirect

 Status              : Active

 Source:

    VLAN           : Any

    Protocol       : TCP

 Destination:

    Port           : 80

IPv6 web-redirect rules on GigabitEthernet1/0/1:

Rule 1:

 Type                : Static

 Action              : Redirect

 Status              : Active

 Source:

    VLAN           : Any

    Protocol       : TCP

 Destination:

    Port           : 80

·交换应用

\# 显示接口Vlan-interface100上的所有Web重定向过滤规则。

\<Sysname\> display web-redirect rule interface vlan-interface 100

IPv4 web-redirect rules on vlan-interface 100:

Rule 1:

 Type                : Dynamic

 Action              : Permit

 Status              : Active

 Source:

    IP             : 192.168.2.114

    VLAN           : Any

Rule 2:

 Type                : Static

 Action              : Redirect

 Status              : Active

 Source:

    VLAN           : Any

    Protocol       : TCP

 Destination:

    Port           : 80

IPv6 web-redirect rules on vlan-interface 100:

Rule 1:

 Type                : Static

 Action              : Redirect

 Status              : Active

 Source:

    VLAN           : Any

    Protocol       : TCP

 Destination:

    Port           : 80

表1-8 display web-redirect rule命令显示信息描述表

字段

描述

Rule

Web重定向规则编号

Type

Web重定向规则的类型，包括以下取值：

·Static：静态类型。该类型的规则在Web重定向功能生效时生成

·Dynamic：动态类型。该类型的规则在用户访问重定向页面时生成

Action

Web重定向规则的匹配动作，包括以下取值：

·Permit：允许报文通过

·Redirect：重定向报文

Status

Web重定向规则下发的状态，包括以下取值：

·Active：表示规则已生效

·Deactive：表示规则未生效

Source

Web重定向规则的源信息

IP

源IP地址

Mask

源IPv4地址子网掩码

Prefix length

源IPv6地址前缀

VLAN

源VLAN，如果未指定，显示为Any

Protocol

Web重定向规则的传输层协议类型，包括以下取值：

·Any：不限制传输层协议类型

·TCP：TCP传输类型

Destination

Web重定向规则的目的信息

Port

目的传输层端口号，默认为80

**Portal \-- Portal配置命令 \-- ip**

------------------------------------------------------------------------

**[ip**]命令用来指定Portal认证服务器的IPv4地址。

**[undo ip**]命令用来删除指定的Portal认证服务器的IPv4地址。

【命令】

**[ip*** ipv4-address* [ **vpn-instance** *vpn-instance-name*   **key** **cipher**[ \| **simple**]}*key-string* ]

**[undo ip**]

【缺省情况】]

没有指定Portal认证服务器的IPv4地址。

【视图】

Portal认证服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：Portal认证服务器的IPv4地址。

**[vpn-instance**]* vpn-instance-name*：Portal认证服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示Portal认证服务器位于公网中。

**[key**]：与Portal认证服务器通信时使用的共享密钥。设备与Portal认证服务器交互的Portal报文中会携带一个在该共享密钥参与下生成的验证字，该验证字用于接受方校验收到的Portal报文的正确性。

**[cipher**]：表示以密文方式设置共享密钥。

**[simple**]：表示以明文方式设置共享密钥。

*[key-string*]：设置的明文密钥或密文密钥，区分大小写。明文密钥为1～64个字符的字符串；密文密钥为33～117个字符的字符串。

【使用指导】

·一个Portal认证服务器对应一个IP地址，因此一个Portal认证服务器视图下只允许存在一个IP地址，后配置IP地址（无论IPv4或IPv6）会覆盖已配置的。

·不同的Portal认证服务器不允许IP地址和VPN的配置都相同。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 指定Portal认证服务器pts的IPv4地址为192.168.0.111、共享密钥为明文portal。

\<Sysname\> system-view

Sysname portal server pts

Sysname-portal-server-pts ip 192.168.0.111 key simple portal

【相关命令】

·**portal server**

·**display portal server**

**Portal \-- Portal配置命令 \-- ipv6**

------------------------------------------------------------------------

**[ipv6**]命令用来指定Portal认证服务器的IPv6地址。

**[undo ipv6**]命令用来删除指定的Portal认证服务器的IPv6地址。

【命令】

**[ipv6** *ipv6-address* [ **vpn-instance** *vpn-instance-name*  **key** **cipher***[ \| ]***simple****}*key-string* ]

**[undo ipv6**]

【缺省情况】]

没有指定Portal认证服务器的IPv6地址。

【视图】

Portal认证服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：Portal认证服务器的IPv6地址。

**[vpn-instance*** vpn-instance-name*]：Portal认证服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示Portal认证服务器位于公网中。

**[key**]：与Portal认证服务器通信需要的共享密钥。设备与Portal认证服务器交互的Portal报文中会携带一个在该共享密钥参与下生成的验证字，该验证字用于接受方校验收到的Portal报文的正确性。

**[cipher**]：表示以密文方式设置共享密钥。

**[simple**]：表示以明文方式设置共享密钥。

*[key-string*]：设置的明文密钥或密文密钥，区分大小写。明文密钥为1～64个字符的字符串；密文密钥为33～117个字符的字符串。

【使用指导】

·一个Portal认证服务器对应一个IP地址，因此一个Portal认证服务器视图下只允许存在一个IP地址，后配置IP地址（无论IPv4或IPv6）会覆盖已配置的。

·不同的Portal认证服务器不允许IP地址和VPN的配置都相同。

·以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。

【举例】

\# 指定Portal认证服务器pts的IPv6地址为2000::1、共享密钥为明文portal。

\<Sysname\> system-view

Sysname portal server pts

Sysname-portal-server-pts ipv6 2000::1 key simple portal

【相关命令】

·**portal server**

·**display portal server**

**Portal \-- Portal配置命令 \-- port**

------------------------------------------------------------------------

**[port**]命令用来配置接入设备主动向Portal认证服务器发送Portal报文时使用的UDP端口号。

**[undo port**]命令用来恢复缺省情况。

【命令】

**[port** *port-id* ]

**[undo port**]

【缺省情况】

接入设备主动发送Portal报文时使用的UDP端口号为50100。

【视图】

Portal认证服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-id*]：设备向Portal认证服务器主动发送Portal报文时使用的目的UDP端口号，取值范围为1～65534。

【使用指导】

本命令配置的端口号要和Portal认证服务器上配置的监听Portal报文的端口号保持一致。

【举例】

\# 配置设备向Portal认证服务器pts主动发送Portal报文时使用的目的UDP端口号为50000。

\<Sysname\> system-view

Sysname portal server pts

Sysname-portal-server-pts port 50000

【相关命令】

·**portal server**

**Portal \-- Portal配置命令 \-- portal { bas-ip \| bas-ipv6 }**

------------------------------------------------------------------------

**[portal ****bas-ip **[\| ]**bas-ipv6** }命令用来设置发送给Portal认证服务器的Portal报文中的BAS-IP或BAS-IPv6属性。

**[undo portal ****bas-ip **[\| ]**bas-ipv6** }命令用来删除接口下指定的BAS-IP或BAS-IPv6属性。

【命令】]

**[portal****bas-ip ***ipv4-address*[ \| ]**bas-ipv6 ***ipv6-address* }

**[undo portal ****[ bas-ip \| bas-ipv6]** }

【缺省情况】]

对于响应类报文]IPv4 Portal报文中的BAS-IP属性为报文的源IP地址，IPv6 Portal报文中的BAS-IPv6属性为报文源IPv6地址。

对于通知类报文]IPv4 Portal报文中的BAS-IP属性为出接口的IP地址，IPv6 Portal报文中的BAS-IPv6属性为出接口的IPv6地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：接口发送Portal报文的BAS-IP属性值，应该为本机的地址，不能为全0地址、全1地址、D类地址、E类地址和环回地址。

*[ipv6-address*]：接口发送Portal报文的BAS-IPv6属性值，应该为本机的地址，不能为多播地址、全0地址、本地链路地址。

【使用指导】

·设备上运行Portal协议2.0版本时，主动发送给Portal认证服务器的报文（例如强制用户下线报文）中必须携带BAS-IP属性。设备上运行Portal协议3.0版本时，主动发送给Portal认证服务器必须携带BAS-IP或者BAS-IPv6属性。

·配置此命令后，设备主动发送的通知类Portal报文，其源IP地址为配置的BAS-IP，否则为Portal报文出接口IP地址。

·接口上使能了二次地址分配认证方式的Portal认证时，如果Portal认证服务器上指定的设备IP不是Portal报文出接口IP地址，则必须通过本命令配置相应的BAS-IP或BAS-IPv6属性，使其值与Portal认证服务器上指定的设备IP一致，否则Portal用户无法认证成功。

·使用H3C iMC的Portal认证服务器的情况下，如果Portal服务器上指定的设备IP不是设备上Portal报文出接口的IP地址，则使能了Portal认证的接口上必须配置BAS-IP或者BAS-IPv6属性。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1发送Portal报文的BAS-IP属性值为2.2.2.2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 portal bas-ip 2.2.2.2

·交换应用

\# 配置接口Vlan-interface100发送Portal报文的BAS-IP属性值为2.2.2.2。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal bas-ip 2.2.2.2

【相关命令】

·**display portal ****interface**

**Portal \-- Portal配置命令 \-- portal apply web-server**

------------------------------------------------------------------------

**[portal **] **ipv6**  **apply****web-server**命令用来在接口上引用Portal Web服务器，设备会将Portal用户的HTTP请求报文重定向到该Web服务器。

**[undo portal** [ **ipv6**  **apply web-server**]]命令用来取消接口上引用的Portal Web服务器。

【命令】

**[portal** [ **ipv6**  **apply** **web-server** *server-name*  **fail-permit** ]]

**[undo portal ** **ipv6** ] **apply** **web-server**

【缺省情况】

接口上没有引用任何Portal Web服务器。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：表示IPv6 Portal Web服务器。若不指定该参数，则表示IPv4 Portal Web服务器。

*[server-name*]：被引用的Portal Web服务器的名字，为1～32个字符的字符串，区分大小写，且必须已经存在。

**[fail-permit**]：开启Portal Web服务器不可达时的Portal用户逃生功能，即设备探测到Portal Web服务器不可达时取消接口的控制功能，允许用户不经过Portal认证即可自由访问网络。

【使用指导】

一个接口上可以同时使能IPv4 Portal认证和IPv6 Portal认证，因此也可以同时引用一个IPv4 Portal Web服务器和一个IPv6 Portal Web认证服务器。

如果接口上同时开启了Portal认证服务器逃生功能和Portal Web服务器逃生功能，则当任意一个服务器不可达时，即放开接口控制，当两个服务器均恢复可达性后，再重新启动Portal认证功能。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上引用名称为wbs的Portal Web服务器作为用户认证时使用的Web服务器。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 portal apply web-server wbs

·交换应用

\# 在接口Vlan-interface100上引用名称为wbs的Portal Web服务器作为用户认证时使用的Web服务器。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal apply web-server wbs

【相关命令】

·**display portal interface**

·**portal fail-permit server**

·**portal web-server**

**Portal \-- Portal配置命令 \-- portal authorization strict-checking**

------------------------------------------------------------------------

**[portal authorization strict-checking**]命令用来开启Portal授权信息的严格检查模式。

**[undo authorizatio strict-checking**]命令用来恢复缺省情况。

【命令】

**[portal authorization**[ { **acl** \| **user-profile** } **strict-checking**]]

**[undo portal authorization **[{ **acl** \| **user-profile** } **strict-checking**]]

【缺省情况】

缺省为非严格检查授权信息模式，当服务器下发的授权ACL、User Profile在设备上不存在或者设备下发ACL、User Profile失败时，用户保持在线。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl**]：表示开启对授权ACL的严格检查。

**[user-profile**]：表示开启对授权User Profile的严格检查。

【使用指导】

接口上开启Portal授权信息的严格检查模式后**，**当服务器给用户下发的授权ACL、User Profile在设备上不存在或者设备下发ACL、User Profile失败时，设备将强制该用户下线。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启对授权ACL的严格检查模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal authoriztion acl strict-checking

·交换应用

\# 在接口Vlan-interface100上开启对授权ACL的严格检查模式。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 portal authoriztion acl strict-checking

【相关命令】

·**display portal interface**

**Portal \-- Portal配置命令 \-- portal delete-user**

------------------------------------------------------------------------

**[portal delete-user**]命令用来强制Portal用户下线。

【命令】

**[portal delete-user **[{ *ipv4-address* \| **all** \| **interface** *interface-type interface-number* \| **ipv6** *ipv6-address* }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：Portal用户的IPv4地址。

**[all**]：所有接口下的IPv4 Portal用户和IPv6 Portal用户。

**[interface*** interface-type interface-number*]：指定接口下的所有Portal用户，包括IPv4 Portal用户和IPv6 Portal用户。*interface-type interface-number*为接口类型和接口编号。

**[ipv6*** ipv6-address*]：指定IPv6 Portal用户的地址。

【举例】

\# 强制IP地址为1.1.1.1的Portal用户下线。

\<Sysname\> system-view

Sysname portal delete-user 1.1.1.1

【相关命令】

·**display portal user**

**Portal \-- Portal配置命令 \-- portal domain**

------------------------------------------------------------------------

**[portal ** **ipv6** ]**domain**命令用于指定Portal用户使用的认证域，使得所有从该接口上接入的Portal用户强制使用该认证域。

**[undo portal**] **ipv6** **domain**命令用来删除指定的Portal用户使用的认证域。

【命令】

**[portal**] **ipv6** **domain** *domain-name*

**[undo portal**  **ipv6**  **domain**]

【缺省情况】

未指定Portal用户使用的认证域。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定IPv6 Portal用户使用的认证域。若不指定本参数，则表示指定IPv4 Portal用户使用的认证域。

*[domain-name*]：ISP认证域名，为1～255个字符的字符串，不区分大小写。

【使用指导】

·接口上可以同时指定IPv4 Portal用户和IPv6 Portal用户的认证域。

·如果不指定**ipv6**参数，则表示配置或者删除IPv4 Portal用户使用的认证域。

【举例】

·路由应用

\# 指定从接口GigabitEthernet1/0/1上接入的IPv4 Portal用户使用认证域为my-domain。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal domain my-domain

·交换应用

\# 指定从接口Vlan-interface100上接入的IPv4 Portal用户使用认证域为my-domain。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal domain my-domain

【相关命令】

·**display portal ****interface**

**Portal \-- Portal配置命令 \-- portal enable**

------------------------------------------------------------------------

**[portal** [ **ipv6**  **enable**]]命令用来在接口上使能Portal认证，并指定认证方式。

**[undo** **portal** [ **ipv6**  **enable**]]命令用来在指定接口上取消指定的Portal认证。

【命令】

**[portal**[ **enable** **method** { **direct** \| **layer3** \| **redhcp** }]]

**[portal**[ **ipv6 enable** **method** { **direct** \| **layer3** }]]

**[undo** **portal** [ **ipv6**  **enable**]]

【缺省情况】

接口上没有使能Portal认证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：表示IPv6 Portal认证。若不指定该参数，则表示IPv4 Portal认证。

**[method**]：认证方式。

·**direct**：直接认证方式。

·**layer3**：可跨三层认证方式。

·**redhcp**：二次地址分配认证方式。

【使用指导】

·使能IPv6 Portal功能之前，需要保证设备支持IPv6 ACL和IPv6转发功能。

·IPv6 Portal认证不支持二次地址分配方式。

·为保证以太网接口上的Portal功能生效，请不要将使能Portal功能的以太网接口加入聚合组。

·允许在接口上同时使能IPv4 Portal认证和IPv6 Portal认证。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上使能IPv4 Portal认证，且指定为直接认证方式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 portal enable method direct

·交换应用

\# 在接口Vlan-interface100上使能IPv4 Portal认证，且指定为直接认证方式。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal enable method direct

【相关命令】

·**display portal interface**

**Portal \-- Portal配置命令 \-- portal fail-permit server**

------------------------------------------------------------------------

**[portal **] **ipv6**  **fail-permit** **server**命令用来开启Portal认证服务器不可达时的Portal用户逃生功能，即设备探测到Portal认证服务器不可达时取消接口的控制功能，允许用户不经过Portal认证即可自由访问网络。

**[u**]**ndo portal** [ **ipv6** **fail-permit server**]命令用来关闭指定的Portal认证服务器逃生功能。

【命令】

**[portal**  **ipv6**  ]**fail-permit server***server-name*

**[undo portal** [ **ipv6** **fail-permit server**]]

【缺省情况】

设备探测到Portal认证服务器不可达时，不允许Portal用户逃生。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：表示IPv6 Portal认证服务器。若不指定该参数，则表示IPv4 Portal认证服务器。

*[server-name*]：Portal认证服务器名称，为1～32个字符的字符串，区分大小写。

【使用指导】

如果接口上同时开启了Portal认证服务器逃生功能和Portal Web服务器逃生功能，则当任意一个服务器不可达时，立即放开接口控制；当两个服务器均恢复可达后，再重新启动接口的Portal认证功能。重新启动接口的Portal认证功能之后，未通过认证的用户需要通过认证之后才能访问网络资源，已通过认证的用户可继续访问网络资源。

一个接口上，最多同时可以开启一个Portal认证服务器逃生功能和一个Portal Web服务器逃生功能。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上启用Portal认证服务器pts1不可达时的Portal用户逃生功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 portal fail-permit server pts1

·交换应用

\# 在接口Vlan-interface100上启用Portal认证服务器 pts1不可达时的Portal用户逃生功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal fail-permit server pts1

【相关命令】

·**display portal ****interface**

**Portal \-- Portal配置命令 \-- portal free-all except destination**

------------------------------------------------------------------------

**[portal **]**free-all except destination**命令用来配置IPv4 Portal目的认证网段。

**[undo portal **]**free-all except destination**命令用来删除配置的IPv4 Portal目的认证网段。

【命令】

**[portal **]**free-all except destination**[ *ipv4-network-address* { *mask-length* \| *mask* }]

**[undo portal **]**free-all except destination** [ *ipv4-network-address* ]

【缺省情况】

没有配置IPv4 Portal目的网段认证，表示对访问任意目的网段的用户都进行Portal认证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-network-address*]：IPv4 Portal认证网段地址。

*[mask-length*]：子网掩码长度，取值范围为0～32。

*[mask*]：子网掩码，点分十进制格式。

【使用指导】

·接口上仅要求Portal用户访问指定目的认证网段（除免认证规则中指定的目的IP地址或网段）时才需要进行Portal认证，访问其它网段访问时不需要进行Portal认证。

·可以通过多次执行本命令，配置多条目的认证网段。

·如果**undo**命令中不携带IP地址参数，则表示删除所有制定的IPv4 Portal目的认证网段。

·目的网段认证对二次地址分配认证方式的Portal认证不生效。

·如果接口上同时配置了源认证网段和目的认证网段，则源认证网段配置不会生效。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置IPv4 Portal目的认证网段为11.11.11.0/24，仅允许访问11.11.11.0/24网段的用户触发Portal认证，其它目的网段可以直接访问。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal free-all except destination 11.11.11.0 24

·交换应用

\# 在接口Vlan-interface2上配置IPv4 Portal目的认证网段为11.11.11.0/24，仅允许访问11.11.11.0/24网段的用户触发Portal认证，其它目的网段可以直接访问。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname--Vlan-interface2 portal free-all except destination 11.11.11.0 24

【相关命令】

·**display portal ****interface**

**Portal \-- Portal配置命令 \-- portal free-rule**

------------------------------------------------------------------------

**[portal free-rule**]命令用来配置基于IP地址的Portal免认证规则。

**[undo portal free-rule**]命令用来删除指定的或所有Portal免认证规则。

【命令】

**[portal free-rule**[ *rule-number* { **destination** **ip** { *ip-address* { *mask-length* \| *mask* } \| **any** } [ **tcp** *tcp-port-number* \| **udp** *udp-port-number* ] \| **source** **ip** { *ip-address* { *mask-length* \| *mask* } \| **any** } [ **tcp** *tcp-port-number* \| **udp** *udp-port-number* ] } \*  **interface** *interface-type interface-number* ]]

**[portal free-rule**  *rule-number* [\| **any**  } [ **tcp** *tcp-port-numbe*r \| **udp** *udp-port-number* ] \| **source** **ipv6** [\| **any**  } [ **tcp** *tcp-port-number* \| **udp** *udp-port-number* ] } \*  **interface** *interface-type interface-number* ]

**[undo portal free-rule ** { *rule-number* \| **all** }]

【缺省情况】]

不存在基于]IP地址的Portal免认证规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-number*]：免认证规则编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[destination**]：指定目的信息。

**[source**]：指定源信息。

**[ip ***ip-address*]：免认证规则的IPv4地址。

[[{ *mask-length* \| *mask* }]]：免认证规则的IP地址掩码。其中，*mask-length*为子网掩码长度，取值范围为0～32；*mask*为子网掩码，点分十进制格式。

**[ipv6** *ipv6-address*]：免认证规则的IPv6地址。

*[prefix-length*]：免认证规则的IPv6地址前缀长度，取值范围为0～128。

**[ip**]**any**：任意IPv4地址。

**[ipv6 **]**any**：任意IPv6地址。

**[tcp** *tcp-port-number*]：免认证规则的TCP端口号，取值范围为0～65535。

**[udp** *udp-port-number*]：免认证规则的UDP端口号，取值范围为0～65535。

**[all**]：所有免认证规则。

**[interface** *interface-type interface-number*]：免认证规则生效的三层接口。

【使用指导】

·可以同时指定源和目的参数，或者仅指定其中一个参数，后者表示另外一个地址不受限制。

·如果免认证规则中同时配置了源端口号和目的端口号，则要求源和目的端口号所属的传输层协议类型保持一致。

·相同内容的免认证规则不能重复配置，否则提示免认证规则已存在或重复。

·未指定三层接口的情况下，免认证规则对所有使能Portal的接口生效；指定三层接口的情况下，免认证规则只对指定的三层接口生效。

【举例】

\# 配置一条基于IPv4地址的Portal免认证规则：编号为1、源地址为10.10.10.1/24、目的地址为20.20.20.1、目的TCP端口号为23、生效接口为GigabitEthernet1/0/1。该规则表示在GigabitEthernet1/0/1接口上，10.10.10.1/24网段地址的用户不需要经过Portal认证即可以访问地址为20.20.20.1的主机在TCP端口23上提供的服务。

\<Sysname\> system-view

Sysname portal free-rule 1 destination ip 20.20.20.1 32 tcp 23 source ip 10.10.10.1 24 interface gigabitethernet 1/0/1

\# 配置一条基于IPv6地址的Portal免认证规则：编号为2、源地址为2000::1/64、目的地址为2001::1、目的TCP端口号为23、生效接口为GigabitEthernet1/0/1。该规则表示在GigabitEthernet1/0/1接口上，2000::1/64网段地址的用户不需要经过Portal认证即可以访问目的地址为2001::1的主机在TCP端口23上提供的服务。

\<Sysname\> system-view

Sysname portal free-rule 2 destination ipv6 2001::1 128 tcp 23 source ip 2000::1 64 interface gigabitethernet 1/0/1

【相关命令】

·**display portal rule**

**Portal \-- Portal配置命令 \-- portal free-rule source**

------------------------------------------------------------------------

**[portal free-rule source**]命令用来配置基于源的Portal免认证规则，这里的源可以是源MAC地址、源接口或者源VLAN。

**[undo portal free-rule**]命令用来删除免认证规则。

【命令】

**[portal free-rule**[ *rule-number* **source** { **interface** *interface-type interface-number* \| **mac** *mac-address* \| **vlan** *vlan-id* } \*]]

**[undo portal free-rule **[{ *rule-number* \| **all** }]]

【缺省情况】

没有配置基于源的Portal免认证规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-number*]：免认证规则编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[interface** *interface-type interface-number*]：免认证规则的源接口。*interface-type interface-number*为接口类型和接口编号。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac ***mac-address*]：免认证规则的源MAC地址，为H-H-H的形式。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan*** vlan-id*]：免认证规则的源VLAN编号。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：所有免认证规则。

【使用指导】

如果免认证规则中同时指定了源VLAN和二层源接口*，*则要求该接口属于对应的VLAN，否则该规则无效。

【举例】

\# 配置一条Portal免认证规则：编号为3、源MAC地址为1-1-1、源VLAN为VLAN 10。该规则表示MAC地址为1-1-1，属于VLAN 10的用户不需要经过Portal认证即可以访问网络资源。

\<Sysname\> system-view

Sysname portal free-rule 3 source mac 1-1-1 vlan 10

【相关命令】

·**display portal rule**

**Portal \-- Portal配置命令 \-- portal { ipv4-max-user \| ipv6-max-user }**

------------------------------------------------------------------------

**[portal**[ { **ipv4-max-user** \| **ipv6-max-user** }]]命令用来配置每个接口下最大Portal用户数。

**[undo portal**[ { **ipv4-max-user** \| **ipv6-max-user** }]]命令用来恢复缺省情况。

【命令】

**[portal**[ { **ipv4-max-user** \| **ipv6-max-user** } *max-number*]]

**[undo portal**[ { **ipv4-max-user** \| **ipv6-max-user** }]]

【缺省情况】

每个接口下最大Portal用户数不受限制。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-number*]：每个接口下允许的最大IPv4或IPv6 Portal用户数，取值范围为1～4294967296。

【使用指导】

如果接口上配置的Portal最大用户数小于当前接口上已经在线的Portal用户数，则该配置可以执行成功，且在线Portal用户不受影响，但系统将不允许新的Portal用户从该接口接入。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置最大IPv4 Portal用户数为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 portal ipv4-max-user 100

·交换应用

\# 在接口Vlan-interface100上配置最大IPv4 Portal用户数为100。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal ipv4-max-user 100

【相关命令】

·**display portal interface**

·**portal max-user**

**Portal \-- Portal配置命令 \-- portal ipv6 free-all except destination**

------------------------------------------------------------------------

**[portal** **ipv6** ]**free-all except destination**命令用来配置IPv6 Portal目的网段认证。

**[undo portal** **ipv6** ]**free-all except destination**命令用来删除配置的IPv6 Portal目的认证网段。

【命令】

**[portal ipv6 **]**free-all except destination** *ipv6-network-address* *prefix-length*

**[undo portal ipv6 **]**free-all except destination** [ *ipv6-network-address* ]

【缺省情况】

没有配置IPv6 Portal目的网段认证，表示对访问任意IPv6目的网段的用户都进行Portal认证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-network-address*]：IPv6 Portal认证网段地址。

*[prefix-length*]：IPv6地址前缀长度，取值范围为0～128。

【使用指导】

·接口上仅要求Portal用户访问指定目的认证网段（除免认证规则中指定的目的IP地址或网段）时才需要进行Portal认证，访问其它网段访问时不需要进行Portal认证。

·可以通过多次执行本命令，配置多条目的认证网段。

·如果**undo**命令中不携带IP地址参数，则表示删除所有制定的IPv6 Portal目的认证网段。

·目的网段认证对二次地址分配认证方式的Portal认证不生效。

·如果接口上同时配置了源认证网段和目的认证网段，则源认证网段配置不会生效。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置IPv6 Portal目的认证网段为1::2/16，仅要求访问1::2/16网段的用户必须进行Portal认证。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal ipv6 free-all except destination 1::2 16

·交换应用

\# 在接口Vlan-interface2上配置IPv6 Portal目的认证网段为1::2/16，仅要求访问1::2/16网段的用户必须进行Portal认证。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname--Vlan-interface2 portal ipv6 free-all except destination 1::2 16

【相关命令】

·**display portal ****interface**

**Portal \-- Portal配置命令 \-- portal ipv6 layer3 source**

------------------------------------------------------------------------

**[portal** **ipv6** ]**layer3** **source**命令用来配置IPv6 Portal源认证网段，即接口上只允许在源认证网段范围内的IPv6用户报文才能触发Portal认证，否则丢弃。

**[undo portal** **ipv6** ]**layer3** **source**命令用来删除配置的IPv6 Portal源认证网段。

【命令】

**[portal ipv6 **]**layer3 source ***ipv6-network-address prefix-length*

**[undo portal ipv6 **]**layer3** **source** [ *ipv6-network-address* ]

【缺省情况】

没有配置IPv6 Portal源认证网段，表示对来自任意网段的IPv6用户都进行Portal认证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-network-address*]：IPv6 Portal源认证网段地址。

*[prefix-length*]：IPv6地址前缀长度，取值范围为0～128。

【使用指导】

·如果**undo**命令中不携带IP地址参数，则表示删除指定所有的IPv6 Portal源认证网段。

·源认证网段仅对Portal的可跨三层认证方式（**layer3**）生效。

·如果接口上同时配置了源认证网段和目的网段认证，则源认证网段配置不会生效。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置一条IPv6 Portal源认证网段为1::1/16，仅允许来自1::1/16网段的用户触发Portal认证。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal ipv6 layer3 source 1::1 16

·交换应用

\# 在接口Vlan-interface2上配置一条IPv6 Portal源认证网段为1::1/16，仅允许来自1::1/16网段的用户触发Portal认证。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname--Vlan-interface2 portal ipv6 layer3 source 1::1 16

【相关命令】

·**display portal ****interface**

·**portal ipv6 ****free-all except destination**

**Portal \-- Portal配置命令 \-- portal ipv6 user-detect**

------------------------------------------------------------------------

**[portal ipv6 **]**user-detect**命令用来开启IPv6 Portal用户在线探测功能。

**[undo portal user-detect**]命令用来恢复缺省情况。

【命令】

**[portal ipv6 user-detect type**[ { **icmpv6** \| **nd** } [ **retry** *retries* ]  **interval** *interval*   **idle** *time* ]]

**[undo portal ipv6 user-detect**]

【缺省情况】

接口上的IPv6 Portal用户在线探测功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[type**]：指定探测类型。

·**icmpv6**：表示探测类型为ICMPv6。

·**nd**：表示探测类型为ND。

**[retry** *retries*]：探测次数，取值范围为1～10，缺省3次。

**[interval** *interval*]：探测间隔，取值范围为1～1200，单位为秒，缺省3秒。

**[idle **]*time*：用户在线探测闲置时长，即闲置多长时间后发起探测，取值范围为60～3600，单位为秒，缺省180秒。

【使用指导】

·根据探测类型的不同，设备有以下两种探测机制：

¡当探测类型为ICMPv6时，若设备发现一定时间（**idle*** time*）内接口上未收到某Portal用户的报文，则会向该用户定期（**interval** *interval*）发送探测报文。如果在指定探测次数（**retry** *retries*）之内，设备收到了该用户的响应报文，则认为用户在线，且停止发送探测报文，重复这个过程，否则，强制其下线。

¡当探测类型为ND时，若设备发现一定时间（**idle** *time*）内接口上未收到某Portal用户的报文，则会向该用户发送ND请求报文。设备定期（**interval** *interval*）检测用户ND表项是否被刷新过，如果在指定探测次数（**retry** *retries*）内用户ND表项被刷新过，则认为用户在线，且停止检测用户ND表项，重复这个过程，否则，强制其下线。

·请根据配置的认证方式选择合适的探测方法，如果配置了直接方式或者二次地址分配方式，则可以使用ND或ICMPv6探测方式，如果配置了可跨三层认证方式，则可以使用ICMPv6探测方式，若配置了ND探测方式，则探测功能不生效。

·如果用户接入设备上配置了阻止ICMPv6报文的防火墙策略，则接口上的ICMPv6探测方式可能会失败，从而导致接口上的Portal用户非正常下线。因此，若接口上需要使用ICMPv6探测方式，请保证用户接入设备不会过滤掉ICMPv6报文。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启IPv6 Portal用户在线探测功能：探测类型为ICMPv6，发送探测报文的次数为5次，发送间隔为10秒，闲置时间为300秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal ipv6 user-detect type icmpv6 retry 5 interval 10 idle 300

·交换应用

\# 在接口Vlan-interface100上开启IPv6 Portal用户在线探测功能：探测类型为ND，检测用户ND表项的探测次数为5次，探测间隔为10秒，闲置时间为300秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal ipv6 user-detect type nd retry 5 interval 10 idle 300

【相关命令】

·**display portal ****interface**

**Portal \-- Portal配置命令 \-- portal layer3 source**

------------------------------------------------------------------------

**[portal**]**layer3** **source**命令用来配置IPv4 Portal源认证网段，即接口上只允许在源认证网段范围内的IPv4用户报文才能触发Portal认证，否则丢弃。

**[undo portal**]**layer3** **source**命令用来删除配置的IPv4 Portal源认证网段。

【命令】

**[portal **]**layer3 source ***ipv4-network-address*[ { *mask-length* \| *mask* }]

**[undo portal **]**layer3 source** [ *ipv4-network-address* ]

【缺省情况】

没有配置IPv4 Portal源认证网段，表示对来自任意网段的IPv4用户都进行Portal认证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-network-address*]：IPv4 Portal认证网段地址。

*[mask-length*]：子网掩码长度，取值范围为0～32。

*[mask*]：子网掩码，点分十进制格式。

【使用指导】

·如果**undo**命令中不携带IP地址参数，则表示删除指定所有的IPv4 Portal源认证网段。

·源认证网段仅对Portal的可跨三层认证方式（**layer3**）生效。

·如果接口上同时配置了源认证网段和目的网段认证，则源认证网段配置不会生效。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置一条IPv4 Portal源认证网段为10.10.10.0/24，仅允许来自10.10.10.0/24网段的用户触发Portal认证。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal layer3 source 10.10.10.0 24

·交换应用

\# 在接口Vlan-interface2上配置一条IPv4 Portal源认证网段为10.10.10.0/24，仅允许来自10.10.10.0/24网段的用户触发Portal认证。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname--Vlan-interface2 portal layer3 source 10.10.10.0 24

【相关命令】

·**display portal ****interface**

·**portal ****free-all except destination**

**Portal \-- Portal配置命令 \-- portal max-user**

------------------------------------------------------------------------

**[portal max-user**]命令用来配置全局Portal最大用户数。

**[undo portal max-user**]命令用来恢复缺省情况。

【命令】

**[portal max-user** *max-number*]

**[undo portal max-user**]

【缺省情况】

全局Portal最大用户数不受限制。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-number*]：系统中允许同时在线的最大Portal用户数。该参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果配置的全局Portal最大用户数小于当前已经在线的Portal用户数，则该命令可以执行成功，且在线Portal用户不受影响，但系统将不允许新的Portal用户接入。

·该命令指定的最大用户数是指IPv4 Portal和IPv6 Portal用户的总数。

·建议所有使能Portal的接口上的最大IPv4 Portal用户数和最大IPv6 Portal用户数之和不超过全局最大Portal用户数配置为，否则会有部分Portal用户因为全局最大用户数已达到而无法上线。

【举例】

\# 配置全局Portal最大用户数为100。

\<Sysname\> system-view

Sysname portal max-user 100

【相关命令】

·**display portal ****user**

[·**portal**[ { **ipv4-max-user** \| **ipv6-max-user** }]]

**Portal \-- Portal配置命令 \-- portal nas-id-profile**

------------------------------------------------------------------------

**[portal nas-id-profile**]命令用来指定接口引用的NAS-ID Profile。

**[undo portal nas-id-profile**]命令用来删除接口引用的NAS-ID Profile。

【命令】

**[portal nas-id-profile **]*profile-name*

**[undo portal nas-id-profile**]

【缺省情况】

未指定引用的NAS-ID Profile。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：标识指定VLAN和NAS-ID绑定关系的Profile名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

本命令引用的NAS-ID Profile由命令**aaa nas-id profile**配置，具体情况请参考"安全命令参考"中的"AAA"。

需要注意的是，如果接口上指定了NAS-ID Profile，则此Profile中定义的绑定关系优先使用；如果接口上未指定NAS-ID Profile或指定的Profile中没有找到匹配的绑定关系，则使用设备名作为NAS-ID。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上指定名为aaa的NAS-ID Profile。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal nas-id-profile aaa

·交换应用

\# 在接口Vlan-interface 2上指定名为aaa的NAS-ID Profile。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 portal nas-id-profile aaa

【相关命令】

·**aaa nas-id profile**（安全命令参考/AAA）

**Portal \-- Portal配置命令 \-- portal nas-port-id format**

------------------------------------------------------------------------

**[portal nas-port-id format**]命令用来配置NAS-Port-ID属性的格式。

**[undo portal nas-port-id format**]命令用来恢复缺省情况。

【命令】

**[portal nas-port-id format**[ { **1** \| **2** \| **3** \| **4** }]]

**[undo portal nas-port-id format**]

【缺省情况】

NAS-Port-ID的消息格式为格式2。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[1**]：表示格式1，具体为[{atm\|eth\|trunk}NAS_slot/NAS_subslot/NAS_port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port[:ANI_XPI.ANI_XCI]]。

**[2**]：表示格式2，具体为SlotID/00/IfNO/VlanID。

**[3**]：表示格式3，具体为在格式2的内容后面添加Option82或者Option18。

**[4**]：表示格式4，具体为"slot=\*\*;subslot=\*\*;port=\*\*;vlanid=\*\*;vlanid2=\*\*;"。

【使用指导】

可通过本命令修改设备为Portal用户发送的RADIUS报文中填充的NAS-Port-ID属性的格式。

不同厂商的RADIUS服务器要求不同的格式，通常中国电信的RADIUS服务器要求采用格式1。

#### 1. 格式1

{atm\|eth\|trunk}NAS_slot/NAS_subslot/NAS_port:XPI.XCI AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port:ANI_XPI.ANI_XCI

各项含义如下：

· {atm\|eth\|trunk}：BRAS端口类型，包括ATM接口、以太接口或trunk类型的以太网接口。

·NAS_slot：BRAS槽号，取值为0～31。

·NAS_subslot：BRAS子槽号，取值为0～31。

·NAS_Port：BRAS端口号，取值为0～63。

·XPI：如果接口类型为atm，则XPI对应VPI，取值为0～255；如果接口类型为eth或trunk，则XPI对应PVLAN，XPI取值为0～4095。

·XCI：如果接口类型为atm，则XCI对应VCI，取值为0～65535；如果接口类型为eth或trunk，XCI对应于CVLAN，XCI取值为0～4095。

·AccessNodeIdentifier：接入节点标识（例如DSLAM设备），为不超过50个字符的字符串，字符串中不能包括空格。

·ANI_rack：接入节点机架号（如支持紧耦合的DSLAM设备），取值为0～15。

·ANI_frame：接入节点机框号，取值为0～31。

·ANI_slot：接入节点槽号，取值为0～127。

·ANI_subslot：接入节点子槽号，取值为0～31。

·ANI_port：接入节点端口号，取值为0～255。

·ANI_XPI.ANI_XCI：可选项，主要用于携带CPE侧的业务信息，可用于标识未来的业务类型需求，如在多PVC应用场合下可标识具体的业务。其中，如果接口类型为atm，则ANI_XPI对应VPI，取值为0～255，ANI_XCII对应VCI，取值为0～65535；如果接口类型为eth或trunk，则ANI_XPI对应PVLAN，取值为0～4095，则ANI_XCI对应CVLAN，取值为0～4095。

需要注意的是：

·字符串之间用一个空格隔开，要求字符串中间不能有空格。花括号中的内容是必选的，[\|]表示并列的关系，多选一。表示可选项。对于某些设备没有机架、框、子槽的概念，相应位置应统一填0，对于无效的VLAN ID值都填4096。

·如接口类型为ATM，则AccessNodeIdentifier、ANI_rack、ANI_frame、ANI_slot、ANI_subslot、ANI_port域可统一填0。

·如运营商未使用SVLAN技术，则XPI=4096，XCI=VLAN，取值为0～4095。

·如运营商未使用VLAN技术区分用户（用户PC直连BAS端口），则XPI=4096，XCI=4096。

·对于接入节点设备（如DSLAM），按如上格式上报本接入节点的接入线路信息，对于与BRAS设备相关的接入线路信息可统一填0，如：

"0 0/0/0:4096.1234 guangzhou001/0/31/63/31/127"

其含义是DSLAM节点标识为guangzhou001、DSLAM的机架号为0（没有机架）、DSLAM的框号为31、DSLAM的槽号为63、DSLAM的子槽号为31、DSLAM的端口号为127、VLAN ID号为1234，BRAS接入线路信息为未知。

·对于BRAS设备，在获取接入节点设备（如DSLAM）的接入线路信息后，根据BRAS的配置可透传接入线路信息，也可修改添加接入线路信息中与BRAS设备相关的线路信息，形成完整的接入线路信息，如：

"eth  31/31/7:4096.1234 guangzhou001/0/31/63/31/127"。

示例：

·例1：NAS_PORT_ID ="atm 31/31/7:255.65535 0/0/0/0/0/0"

含义：BRAS设备的用户接口类型为ATM接口，BRAS槽号为31，BRAS子槽号为31，BRAS端口号为7，VPI为255，VCI为65535。

·例2：NAS_PORT_ID ="eth 31/31/7:1234.2345 0/0/0/0/0/0"

含义：BRAS设备的用户接口类型为以太接口，BRAS槽号为31，BRAS子槽号为31，BRAS端口号为7，PVLAN ID为1234，CVLAN ID为2345。

·例3：NAS_PORT_ID ="eth 31/31/7:4096.2345 0/0/0/0/0/0"

含义：BRAS设备的用户接口类型为以太接口，BRAS槽号为31，BRAS子槽号为31，BRAS端口号为7，VLAN ID为2345。

·例4：NAS_PORT_ID ="eth  31/31/7:4096.2345 guangzhou001/1/31/63/31/127"

含义：BRAS设备的用户接口类型为以太接口，BRAS槽号为31，BRAS子槽号为31, BRAS端口号为7，VLAN ID为2345,接入节点DSLAM的标识为guangzhou001，DSLAM的机架号为1，DSLAM的框号为31，DSLAM的槽号为63，DSLAM的子槽号为31，DSLAM的端口号为127。

#### 2. 格式2

SlotID/00/IfNO/VlanID

各项含义如下：

·SlotID：用户接入的槽位号，为两个字符的字符串。

·IFNO：用户接入的接口编号，为3个字符的字符串。

·VlanID：用户接入的VLAN ID，为9个字符的字符串。

#### 3. 格式3

其格式为在格式2的NAS-Port-ID内容后面添加用户DHCP报文中指定Option的内容：

·对于IPv4用户，此处添加的是DHCP Option82的内容。

·对于IPv6用户，此处添加的是DHCP Option18的内容。

#### 4. 格式4

其格式为"slot=\*\*;subslot=\*\*;port=\*\*;vlanid=\*\*;vlanid2=\*\*;"，具体情况如下：

·对于非VLAN接口，其格式为"slot=\*\*;subslot=\*\*;port=\*\*;vlanid=0;"。

·对于只终结了一层VLAN Tag的接口，其格式为"slot=\*\*;subslot=\*\*;port=\*\*;vlanid=\*\*;"。

【举例】

\# 配置NAS-Port-ID属性的格式为format 1。

\<Sysname\> system-view

Sysname portal nas-port-id format 1

**Portal \-- Portal配置命令 \-- portal pre-auth domain**

------------------------------------------------------------------------

**[portal** [ **ipv6**  **pre-auth domain**]]命令用来在接口上配置Portal认证前用户使用的认证域。

**[undo portal** [ **ipv6**  **pre-auth domain**]]命令用来删除接口上Portal认证前用户使用的认证域。

【命令】

**[portal** [ **ipv6**  **pre-auth domain domain-name**]]

**[undo portal** [ **ipv6**  **pre-auth domain**]]

【缺省情况】

接口上未配置Portal认证前用户使用的认证域。

【视图】

三层接口视图/三层子接口视图

【缺省用户角色】

network-admin

mdc-admin

context-admin

【参数】

**[ipv6**]：指定IPv6用户使用的认证域。若不指定该参数，则表示指定IPv4用户使用的认证域。

domain-name：ISP认证域名，为1～255个字符的字符串，不区分大小写，不能包括"/"、"\"、"[\|]"、"""、":"、"\*"、"?"、"\<"、"\>"以及"@"字符。

【使用指导】

使能Portal的接口上配置了认证前使用的认证域（简称为认证前域）时，在此接口上获取到IP地址的用户将被Portal授予指定认证前域内配置的相关授权属性（目前包括ACL、User Profile、Session Group Profile和CAR），并根据授权信息获得相应的网络访问权限。若此用户后续触发了Portal认证，则认证成功之后会被AAA下发新的授权信息。用户下线之后，将被重新授予该认证前域中的授权属性。

认证前域的配置只对采用DHCP或DHCPv6分配IP地址的用户生效。

如果认证前域的域名发生变化，新的域名对所有认证前用户生效。

如果当前认证前域中的ACL、User Profile、Session Group Profile和CAR授权配置发生变化，则新配置仅对新生成的认证前用户生效，已经存在的用户继续使用旧配置。

需要注意的是，若认证前域中指定的授权ACL不存在，或者ACL中无任何规则，则表示不对用户的访问进行限制；若认证前域中指定的ACL中存在匹配源IP地址、匹配源MAC地址、匹配所有IP地址或匹配所有IPv6地址的规则，则该授权ACL下发后将会导致用户不能正常上线和下线。

【举例】

\# 在接口GigabitEthernet1/0/1上配置Portal认证前用户使用的认证域为abc。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 portal pre-auth domain abc

【相关命令】

·**display portal interface**

**Portal \-- Portal配置命令 \-- portal pre-auth ip-pool**

------------------------------------------------------------------------

**[portal ** **ipv6** ] **pre-auth ip-pool**命令用来配置Portal认证前用户使用的地址池。

**[undo** **portal** [ **ipv6**  **pre-auth ip-pool**]]命令用来恢复缺省情况。

【命令】

**[portal** [ **ipv6**  **pre-auth ip-pool** *pool-name*]]

**[undo** **portal** [ **ipv6**  **pre-auth ip-pool**]]

【缺省情况】

接口上未配置Portal认证前用户使用的地址池。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：表示IPv6 Portal用户。若不指定该参数，则表示IPv4 Portal用户。

*[pool-name*]：表示IP地址池的名字，为1～63个字符的字符串，不区分大小写。

【使用指导】

在Portal用户通过设备的子接口接入网络的组网环境中，当子接口上未配置IP地址，且用户需要通过DHCP获取地址时，就必须通过本命令指定一个地址池，并在用户进行Portal认证之前为其分配一个IP地址使其可以进行Portal认证。

需要注意的是：

·仅当接口使用直接认证方式的情况下，接口上为认证前的Portal用户指定的IP地址池才能生效。

·当使用接口上指定的IP地址池为认证前的Portal用户分配IP地址时，该指定的IP地址池必须存在且配置完整，否则无法为Portal用户分配IP地址，并导致用户无法进行Portal认证。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上为认证前的Portal用户指定IPv4地址池为abc。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 portal pre-auth ip-pool abc

·交换应用

\# 在接口Vlan-interface100上为认证前的Portal用户指定IPv4地址池为abc。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal pre-auth ip-pool abc

【相关命令】

·**dhcp server ip-pool**（三层技术-IP业务/DHCP）

·**ipv6 dhcp pool**（三层技术-IP业务/DHCP）

·**display portal interface**

**Portal \-- Portal配置命令 \-- portal roaming enable**

------------------------------------------------------------------------

![说明](Portal命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[portal roaming enable**]命令用来使能Portal用户漫游功能。

**[undo portal roaming enable**]命令用来关闭Portal用户漫游功能。

【命令】

**[portal roaming enable**]

**[undo portal roaming enable**]

【缺省情况】

Portal用户漫游功能处于关闭状态，即Portal用户上线后不能在所在的VLAN内漫游。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·该命令只对通过VLAN接口上线的Portal用户有效。

·如果使能了Portal用户漫游功能，则Portal用户上线后可以在使能Portal的VLAN内漫游，即用户通过VLAN内的任何二层端口都可以访问网络资源；否则用户只能通过认证成功的二层端口访问网络资源。

·有用户在线的情况下，不能配置此命令。

【举例】

\# 使能Portal用户漫游功能。

\<Sysname\> system-view

Sysname portal roaming enable

**Portal \-- Portal配置命令 \-- portal server**

------------------------------------------------------------------------

**[portal server**]命令用来创建Portal认证服务器，并进入Portal认证服务器视图。

**[undo portal server**]命令用来删除指定的Portal认证服务器。

【命令】

**[portal server ***server-name*]

**[undo portal server ***server-name*]

【缺省情况】

没有配置任何Portal认证服务器。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-name*]：Portal认证服务器名称，为1～32个字符的字符串，区分大小写。

【使用指导】

Portal认证服务器视图用于配置Portal认证服务器的相关参数，包括服务器的IP地址、端口号，服务器所在的VPN实例，设备和服务器间通信的预共享密钥，服务器探测功能等。

可以配置多个Portal认证服务器。

【举例】

\# 创建名称为pts的Portal认证服务器，并进入Portal认证服务器视图。

\<Sysname\> system-view

Sysname portal server pts

Sysname-portal-server-pts

【相关命令】

·**display portal server**

**Portal \-- Portal配置命令 \-- portal user-detect**

------------------------------------------------------------------------

**[portal user-detect**]命令用来开启IPv4 Portal用户在线探测功能。

**[undo portal user-detect**]命令用来恢复缺省情况。

【命令】

**[portal user-detect type**[ { **arp** \| **icmp** } [ **retry** *retries*]  **interval** *interval*   **idle** *time* ]]

**[undo portal user-detect**]

【缺省情况】

接口上的IPv4 Portal用户在线探测功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[type**]：指定探测类型。

·**arp**：表示探测类型为ARP。

·**icmp**：表示探测类型为ICMP。

**[retry** *retries*]：探测次数，取值范围为1～10，缺省3次。

**[interval** *interval*]：探测间隔，取值范围为1～1200，单位为秒，缺省3秒。

**[idle **]*time*：用户在线探测闲置时长，即闲置多长时间后发起探测，取值范围为60～3600，单位为秒，缺省180秒。

【使用指导】

·根据探测类型的不同，设备有以下两种探测机制：

¡当探测类型为ICMP时，若设备发现一定时间（**idle*** time*）内接口上未收到某Portal用户的报文，则会向该用户定期（**interval** *interval*）发送探测报文。如果在指定探测次数（**retry** *retries*）之内，设备收到了该用户的响应报文，则认为用户在线，且停止发送探测报文，重复这个过程，否则，强制其下线。

¡当探测类型为ARP时，若设备发现一定时间（**idle** *time*）内接口上未收到某Portal用户的报文，则会向该用户发送ARP请求报文。设备定期（**interval** *interval*）检测用户ARP表项是否被刷新过，如果在指定探测次数（**retry** *retries*）内用户ARP表项被刷新过，则认为用户在线，且停止检测用户ARP表项，重复这个过程，否则，强制其下线。

·请根据配置的认证方式选择合适的探测方法，如果配置了直接方式或者二次地址分配方式，则可以使用ARP或ICMP探测方式，如果配置了可跨三层认证方式，则仅可以使用ICMP探测方式，若配置了ARP探测方式，则探测功能不生效。

·如果用户接入设备上配置了阻止ICMP报文的防火墙策略，则接口上的ICMP探测方式可能会失败，从而导致接口上的Portal用户非正常下线。因此，若接口上需要使用ICMP探测方式，请保证用户接入设备不会过滤掉ICMP报文。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启Portal用户在线探测功能：探测类型为ICMP，发送探测报文的次数为5次，发送间隔为10秒，闲置时间为300秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 portal user-detect type icmp retry 5 interval 10 idle 300

·交换应用

\# 在接口Vlan-interface100上开启Portal用户在线探测功能：探测类型为ARP，检测用户ARP表项的探测次数为5次，探测间隔为10秒，闲置时间为300秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 portal user-detect type arp retry 5 interval 10 idle 300

【相关命令】

·**display portal ****interface**

**Portal \-- Portal配置命令 \-- portal web-server**

------------------------------------------------------------------------

**[portal web-server**]命令用来创建Portal Web服务器，并进入Portal Web服务器视图。

**[undo portal web-server**]命令用来删除Portal Web服务器。

【命令】

**[portal web-server** *server-name*]

**[undo portal web-server** *server-name*]

【缺省情况】

没有配置任何Portal Web服务器。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-name*]：Portal Web服务器的名称，为1～32个字符的字符串，区分大小写。

【使用指导】

Portal Web服务器是指Portal认证过程中向用户推送认证页面的Web服务器，也是设备强制重定向用户HTTP请求报文时所指的Web服务器。Portal Web服务器视图用于配置该Web服务器的URL地址及配置设备重定向该URL地址给用户时URL地址所携带的参数，同时该视图还用于配置Portal Web服务器探测等功能。

【举例】

\# 创建名称为wbs的Portal Web服务器，并进入Portal Web服务器视图。

\<Sysname\> system-view

Sysname portal web-server wbs

Sysname-portal-websvr-wbs

【相关命令】

·**display portal web-server**

·**portal ****apply web-server**

**Portal \-- Portal配置命令 \-- reset portal packet statistics**

------------------------------------------------------------------------

**[reset portal packet statistics**]命令用来清除Portal报文的统计信息。

【命令】

**[reset portal packet statistics**]**** **server** *server-name*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-name*]：Portal认证服务器的名称，为1～32个字符的字符串，区分大小写。

【使用指导】

若不指定参数**server**，则清除所有Portal认证服务器的报文统计信息。

【举例】

\# 清除名字为st上的Portal认证服务器的统计信息。

\<Sysname\> reset portal packet statistics server pts

【相关命令】

·**display portal ****packet statistics**

**Portal \-- Portal配置命令 \-- server-detect (portal server view)**

------------------------------------------------------------------------

**[server-detect**]命令用来开启Portal认证服务器的可达性探测功能。开启Portal认证服务器的可达性探测功能后，设备会定期检测Portal认证服务器发送的Portal报文来判断服务器的可达状态。

**[undo **]**server-detect**命令用来恢复缺省情况。

【命令】

**[server-detect**  **timeout** *timeout*  { **log \| trap** } \*]

**[undo server-detect**]

【缺省情况】

Portal认证服务器的可达性探测功能处于关闭状态。

【视图】

Portal认证服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[timeout ***timeout*]：探测超时时间，取值范围10～3600，单位为秒，缺省值为60。

[[{ **log \| trap** } **\***]]：设备探测到Portal认证服务器可达状态变化时，触发执行的操作。包括以下两种，且可同时选择多种。

·**log**：Portal认证服务器可达或者不可达的状态改变时，发送日志信息。日志信息中记录了Portal认证服务器名以及该服务器状态改变前后的状态。

·**trap**：Portal认证服务器可达或者不可达的状态改变时，向网管服务器发送Trap信息。Trap信息中记录了Portal认证服务器名以及该服务器的当前状态。

【使用指导】

只有在支持Portal服务器心跳功能（目前仅iMC的Portal认证服务器支持）的Portal认证服务器的配合下，本功能才有效。

若设备在指定的探测超时时间（**timeout** *timeout*）内收到Portal报文，且验证其正确，则认为此次探测成功且服务器可达，否则认为此次服务器不可达。

【举例】

\# 开启对Portal认证服务器pts的探测功能，探测超时时间为600秒，若服务器状态改变，则发送日志信息和Trap信息。

\<Sysname\> system-view

Sysname portal server pts

Sysname-portal-server-pts server-detect timeout 600 log trap

【相关命令】

·**portal server**

**Portal \-- Portal配置命令 \-- server-detect (portal web-server view)**

------------------------------------------------------------------------

**[server-detect**]命令用来开启Portal Web服务器的可达性探测功能。

**[undo **]**server-detect**命令用来恢复缺省情况。

【命令】

**[server-detect** [ **interval** *interval*   **retry** ]*retries* { **log** \| **trap** } \*]

**[undo server-detect**]

【缺省情况】

当前Portal Web服务器的可达性探测功能处于关闭状态。

【视图】

Portal Web服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval**]* interval*：进行探测尝试的时间间隔，取值范围为10～1200，单位为秒，缺省值为20。

**[retry**]* retries*：连续探测失败的最大次数，取值范围为1～10，缺省值为3。若连续探测失败数目达到此值，则认为服务器不可达。

}** \***：Portal Web服务器可达状态的变化时，可触发执行的操作。包括以下两种，且可同时选择多种。

·**log**：Portal Web服务器可达或者不可达的状态改变时，发送日志信息。日志信息中记录了Portal Web服务器名以及该服务器状态改变前后的状态。

·**trap**：Portal Web服务器可达或者不可达的状态改变时，向网管服务器发送Trap信息。Trap信息中记录了Portal Web服务器名以及该服务器的当前状态。

【使用指导】

该探测方法可由设备独立完成，不需要Portal Web服务器端的任何配置来配合。

【举例】

\# 配置对Portal Web服务器wbs的探测功能，每次探测间隔时间为600秒，若连续二次探测均失败，则发送服务器不可达的日志信息和Trap信息。

\<Sysname\> system-view

Sysname portal web-server wbs

Sysname-portal-websvr-wbs server-detect interval 600 retry 2 log trap

【相关命令】

·**portal web-server**

**Portal \-- Portal配置命令 \-- url**

------------------------------------------------------------------------

**[url**]命令用来指定Portal Web服务器的URL。

**[undo url**]命令用来删除指定的Portal Web服务器的URL。

【命令】

**[url** *url-string*]

**[undo url**]

【缺省情况】

没有指定Portal Web服务器的URL。

【视图】

Portal Web服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[url-string*]：Portal Web服务器的URL，为1～256个字符的字符串，区分大小写。

【使用指导】

本命令指定的URL是可用标准HTTP或者HTTPS协议访问的URL，它以http://或者https://开头。如果该URL未以http://或者https://开头，则缺省认为是以http://开头。

【举例】

\# 配置Portal Web服务器wbs的URL为http://www.test.com/portal。

\<Sysname\> system-view

Sysname portal web-server wbs

Sysname-portal-websvr-wbs url http://www.test.com/portal

【相关命令】

·**display portal web-server**

**Portal \-- Portal配置命令 \-- url-parameter**

------------------------------------------------------------------------

**[url-parameter**]命令用来配置设备重定向给用户的Portal Web服务器的URL中携带的参数信息。

**[undo url-parameter**]命令用来删除配置的Portal Web服务器URL携带的参数信息。

【命令】

**[url-parameter ***param-name *[{ **original-url** \| **source-address** \| **source-mac** \| **value** *expression* }]]

**[undo url-parameter ***param-name*]

【缺省情况】

未配置设备重定向给用户的Portal Web服务器的URL中携带的参数信息。

【视图】

Portal Web服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[param-name*]：URL参数名，为1～32个字符的字符串，区分大小写。URL参数名对应的参数内容由*param-name*后的参数指定。

**[original-url**]：用户初始访问的Web页面的URL。

**[source-address**]：用户的IP地址。

**[source-mac**]：用户的MAC地址。

**[value ***expression*]：自定义字符串，为1～256个字符的字符串，区分大小写。

【使用指导】

可以通过多次执行本命令配置多条参数信息。

对于同一个参数名*param-name*后的参数设置，最后配置的生效。

该命令用于配置用户访问Portal Web服务器时，要求携带的一些参数，比较常用的是要求携带用户的IP地址、MAC地址、用户原始访问的URL信息。用户也可以手工指定，携带一些特定的字符信息。配置完成后，在设备给用户强制重定向URL时会携带这些参数，例如配置Portal Web服务器的URL为：http://www.test.com/portal，若同时配置如下两个参数信息：**url-parameter** **userip** **source-address**和**url-parameter** **userurl** **value** **http://www.test.com/welcome**，则设备给源IP为1.1.1.1的用户重定向时回应的URL格式即为：http://www.test.com/portal?userip=1.1.1.1&userurl= http://www.test.com/welcome。

【举例】

\# 为设备重定向给用户的Portal Web服务器wbs的URL中配置两个参数userip和userurl，其值分别为用户IP地址和自定义字符串http://www.test.com/welcome。

\<Sysname\> system-view

Sysname portal web-server wbs

Sysname-portal-websvr-wbs url-parameter userip source-address

Sysname-portal-websvr-wbs url-parameter userurl value http://www.test.com/welcome

【相关命令】

·**display portal web-server**

·**url**

**Portal \-- Portal配置命令 \-- user-sync**

------------------------------------------------------------------------

**[user-sync**]命令用来配置开启Portal用户信息同步功能。配置此功能后，设备会响应并周期性地检测指定的Portal认证服务器发来的用户同步报文，以保持设备与该服务器上在线用户信息的一致性。

**[undo user-sync**]命令用来恢复缺省情况。

【命令】

**[user-sync timeout** *timeout*]

**[undo user-sync**]

【缺省情况】

当前Portal认证服务器的Portal用户信息同步功能处于关闭状态。

【视图】

Portal认证服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[timeout ***timeout*]：检测用户同步报文的时间间隔，取值范围为60～18000，单位为秒，缺省值为1200。

【使用指导】

·只有在支持Portal用户心跳功能（目前仅iMC的Portal认证服务器支持）的Portal认证服务器的配合下，本功能才有效。为了实现该功能，还需要在Portal认证服务器上选择支持用户心跳功能，且服务器上配置的用户心跳间隔要小于等于设备上配置的检测超时时间。

·在设备上删除Portal认证服务器时将会同时删除该服务器的用户信息同步功能配置。

·对同一服务器多次执行用户信息同步功能的配置时，新的配置将覆盖原有的配置。

·对于设备上多余的用户信息，即在检测用户同步报文的时间间隔*timeout*到达后被判定为Portal认证服务器上已不存在的用户信息，设备会在*timeout*后的某时刻将其删除掉。

·如果服务器同步过来的用户信息在设备上不存在，则设备会将这些用户的IP地址封装在用户心跳回应报文中发送给服务器，由服务器删除多余的用户。

【举例】

\# 配置对Portal认证服务器pts的Portal用户信息同步功能，检测用户同步报文的时间间隔为600秒，如果设备中的某用户信息在600秒内未在该Portal认证服务器发送的同步报文中出现，设备将强制该用户下线。

\<Sysname\> system-view

Sysname portal server pts

Sysname-portal-server-pts user-sync timeout 600

【相关命令】

·**portal server**

**Portal \-- Portal配置命令 \-- vpn-instance**

------------------------------------------------------------------------

**[vpn-instance**]命令用来配置Portal Web服务器所属的VPN。

**[undo vpn-instance**]命令用来取消配置的Portal Web服务器所属的VPN。

【命令】

**[vpn-instance*** vpn-instance-name*]

**[undo vpn-instance**]

【缺省情况】

Portal Web服务器位于公网中。

【视图】

Portal Web服务器视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

v*pn-instance-name*：Portal Web服务器所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

一个Portal Web服务器只能属于一个VPN。

【举例】

\# 配置Portal Web服务器wbs所属的VPN为abc。

\<Sysname\> system-view

Sysname portal web-server wbs

Sysname-portal-websvr-wbs vpn-instance abc

**Portal \-- Portal配置命令 \-- web-redirect track**

------------------------------------------------------------------------

[![说明](Portal命令.files/image002.png)]

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[web-redirect track**]命令用来开启Web重定向Track功能。

**[undo web-redirect track**]命令用来关闭Web重定向Track功能。

【命令】

**[web-redirect track interface** *interface-type interface-number*]

**[undo web-redirect track**]

【缺省情况】

Web重定向Track功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：表示监视指定接口的状态或网络信号信息。*interface-type interface-number*为接口类型和接口编号。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

本命令用来开启Web重定向Track功能，监视指定接口的状态或网络信号信息。

如果监视的指定接口状态为Down或以太网通道接口（Eth-channel）的网络信号为2G信号、无信号，当用户访问互联网时，为其推出不可达页面。之后，用户不能访问外网资源。

需要注意的是：

·目前只支持对以太网通道接口（Eth-channel）网络信号信息的监视，不支持监视其他类型的接口。

·Web重定向Track功能，目前只支持IPv4用户。

·使能Web重定向Track功能时，Web重定向功能指定的URL页面必须配置在本机上的。

【举例】

\# 在接口Vlan-interface2下开启Web重定向Track功能，监视上行接口Eth-channel2/0:0的网络信号信息。

\<Sysname\> system-view

Sysname interface vlan 2

Sysname-Vlan-interface2 web-redirect track interface eth-channel 2/0:0

【相关命令】

·**display web-redirect rule**

·**web-redirect url**

**Portal \-- Portal配置命令 \-- web-redirect url**

------------------------------------------------------------------------

**[web-redirect url**]命令用来配置Web重定向功能。

**[undo web-redirect**]命令用来关闭Web重定向功能。

【命令】

**[web-redirect** [ **ipv6**  **url** *url-string*  **interval** *interval* ]]

**[undo web-redirect** [ **ipv6** ]]

【缺省情况】

Web重定功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：表示IPv6 Web重定向功能。若不指定该参数，则表示IPv4 Web重定向功能。

**[url**]*url-string*：Web重定向的地址，即用户的Web访问请求被重定向的URL地址，为1～256个字符的字符串，必须是以http://或者https://开头的完整URL路径。

**[interval**]*interval*：对用户访问的Web页面进行重定向的周期，取值范围为60～86400，单位为秒，缺省为86400秒。

【使用指导】

接口上配置了Web重定向功能后，当该接口上接入的用户初次通过Web页面访问外网时，设备会将用户的初始访问页面重定向到指定的URL页面，之后用户才可以正常访问外网，经过一定时长（*interval*）后，设备又可以对用户要访问的网页或者正在访问的网页重定向到指定的URL页面。

如果设备支持以太网通道接口（Eth-channel），则接口下可以同时开启Web重定向功能和Portal功能，否则当接口下同时开启Web重定向功能和Portal功能时，Web重定向功能失效。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置IPv4 Web重定向功能：Web重定向地址为http://192.0.0.1，Web重定向周期为3600秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 web-redirect url http://192.0.0.1 interval 3600

·{.ItemStepChar}交换应用{.ItemStepChar}

\# 在接口Vlan-interface100上配置IPv4 Web重定向功能：Web重定向地址为http://192.0.0.1，Web重定向周期为3600秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname--Vlan-interface100 web-redirect url http://192.0.0.1 interval 3600

【相关命令】

·**display web-redirect rule**
