<!-- CMD-INDEX
  display sma-anti-spoof ipv6 address-prefix | 任意视图             | L9
  display sma-anti-spoof ipv6 packet-tag | 任意视图             | L75
  sma-anti-spoof ipv6 enable          | 系统视图             | L153
  sma-anti-spoof ipv6 port-type       | 接口视图             | L197
  sma-anti-spoof ipv6 server          | 系统视图             | L253
-->

**SMA \-- SMA配置命令 \-- display sma-anti-spoof ipv6 address-prefix**

------------------------------------------------------------------------

**[display sma-anti-spoof ipv6 address-prefix**]命令用来显示所有AS的IPv6地址前缀信息。

【命令】

**[display sma-anti-spoof ipv6 address-prefix**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有AS的IPv6地址前缀信息。

\<Sysname\> display sma-anti-spoof ipv6 address-prefix

Alliance number: 1                                AS number: 10

IPv6 prefix                                       Effecting time

AA:AA::/64                                        May 1 14:12:49 2009

AA:AA::AA:AB/128                                  May 1 14:12:49 2009

Alliance number: 1                                AS number: 11

IPv6 prefix                                       Effecting time

BB:BB::/64                                        May 1 14:02:49 2009(i)

表1-1 display sma-anti-spoof ipv6 address-prefix命令显示信息描述表

字段

描述

Alliance number

信任联盟号

AS number

自治系统号

IPv6 prefix

当前自治系统下的IPv6前缀

Effecting time

IPv6前缀生效的起始时间，表示格式如：May 1 14:12:49 2009或May 1 14:02:49 2009(i)，其中（i）表示立即生效

**SMA \-- SMA配置命令 \-- display sma-anti-spoof ipv6 packet-tag**

------------------------------------------------------------------------

**[display sma-anti-spoof ipv6 packet-tag**]命令用来显示所有AS对的标签信息。

【命令】

**[display sma-anti-spoof ipv6 packet-tag**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有AS对的标签信息。

\<Sysname\> display sma-anti-spoof ipv6 packet-tag

Alliance number: 1

Source AS number: 10                         Destination AS number: 11

State machine ID: 100                        Tag: 0xABCD

Effecting time: May 1 14:12:49 2009(i)       Transition interval: 10s

Source AS number: 11                         Destination AS number: 10

State machine ID: 101                        Tag: 0xCDEF

Effecting time: May 1 14:02:49 2009          Transition interval: 12s

表1-2 display sma-anti-spoof ipv6 packet-tag命令显示信息描述表

字段

描述

Alliance number

信任联盟号

Source AS number

源自治系统号

Destination  AS number

目的自治系统号

State machine ID

状态机ID

Tag

标签，0～128位的二进制数，以十六进制数的形式显示，如：0xABCD

Effecting time

标签生效的起始时间，表示格式如：May 1 14:12:49 2009或May 1 14:02:49 2009(i)，其中（i）表示立即生效

Transition interval

标签有效时间，单位为秒，超时后标签失效

**SMA \-- SMA配置命令 \-- sma-anti-spoof ipv6 enable**

------------------------------------------------------------------------

**[sma-anti-spoof ipv6 enable**]命令用来开启SMA功能。

**[undo sma-anti-spoof ipv6 enable**]命令用来关闭SMA功能。

【命令】

**[sma-anti-spoof ipv6 enable**]

**[undo sma-anti-spoof ipv6 enable**]

【缺省情况】

SMA功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有使能SMA功能后，SMA的相关配置才会生效。

【举例】

\# 开启SMA功能。

\<Sysname\> system-view

Sysname sma-anti-spoof ipv6 enable

【相关命令】

·**sma-anti-spoof ipv6 server**

**SMA \-- SMA配置命令 \-- sma-anti-spoof ipv6 port-type**

------------------------------------------------------------------------

**[sma-anti-spoof ipv6 port-type**]命令用来配置SMA的接口类型。

**[undo sma-anti-spoof ipv6 port-type**]命令用来恢复缺省情况。

【命令】

**[sma-anti-spoof ipv6 port-type **[**ingress** \| **egress**}]]

**[undo sma-anti-spoof ipv6 port-type**]

【缺省情况】

未配置SMA接口类型，不对报文进行SMA处理。

【视图】

接口视图

【缺省用户角色】

network-admin

network-operator

【参数】

**[ingress**]：设置SMA的接口类型为Ingress类型。

**[egress**]：设置SMA的接口类型为Egress类型。

【使用指导】

在SMA组网环境中，为了正确地对报文进行分类，并完成标签的添加、检查以及报文转发，需要手动指定AER上的接口类型。

·Ingress接口：连接到本AS内部未使能SMA特性的路由器的接口。

·Egress接口：连接到其它AS内部AER的接口。

【举例】

\# 配置接口GigabitEthernet1/0/1的SMA接口类型为Ingress类型。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 sma-anti-spoof ipv6 port-type ingress

【相关命令】

·**sma-anti-spoof ipv6 enable**

**SMA \-- SMA配置命令 \-- sma-anti-spoof ipv6 server**

------------------------------------------------------------------------

**[sma-anti-spoof ipv6 server**]命令用来配置AER与ACS之间建立SSL连接。

**[undo sma-anti-spoof ipv6 server**]命令用来恢复缺省情况。

【命令】

**[sma-anti-spoof ipv6 server ***ipv6-address*** ssl-client-policy ***policy-name*]

**[undo sma-anti-spoof ipv6 server**]

【缺省情况】

AER与ACS之间未建立SSL连接。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：指定ACS服务器的IPv6地址。

**[ssl-client-policy*** policy-name*]：指定SSL客户端策略名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

配置此命令前需要先通过**sma-anti-spoof ipv6 enable**命令开启SMA功能。如果指定的SSL客户端策略不存在，则AER与ACS无法建立连接。

【举例】

\# 指定ACS的IPv6地址为1::1，并指定与ACS建立SSL连接时使用的SSL客户端策略为ssl，使AER与ACS之间建立SSL连接。

Sysname\> system-view

Sysname sma-anti-spoof ipv6 server 1::1 ssl-client-policy ssl

【相关命令】

·**sma-anti-spoof ipv6 enable**
