<!-- CMD-INDEX
  display dldp                        | 任意视图             | L14
  display dldp statistics             | 任意视图             | L196
  dldp authentication-mode            | 系统视图             | L296
  dldp authentication-password        | 系统视图             | L364
  dldp delaydown-timer                | 系统视图             | L432
  dldp enable                         | 二层以太网接口视图/三层以太网接口视图 | L480
  dldp global enable                  | 系统视图             | L530
  dldp interval                       | 系统视图             | L576
  dldp unidirectional-shutdown        | 系统视图             | L626
  reset dldp statistics               | 用户视图             | L672
-->

**DLDP \-- DLDP配置命令 \-- display dldp**

------------------------------------------------------------------------

**[display dldp**]命令用来显示DLDP的全局配置信息和接口的DLDP信息。

【命令】

**[display dldp ** **interface** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的DLDP信息，*interface-type interface-number*为接口类型和接口编号。如果未指定本参数，将显示DLDP的全局配置信息和所有接口的DLDP信息。

【举例】

\# 显示DLDP的全局配置信息和所有接口的DLDP信息。

\<Sysname\> display dldp

 DLDP global status: Enabled

 DLDP advertisement interval: 5s

 DLDP authentication-mode: Simple

 DLDP authentication-password: \*\*\*\*\*\*

 DLDP unidirectional-shutdown mode: Auto

 DLDP delaydown-timer value: 1s

 Number of enabled ports: 2

Interface GigabitEthernet1/0/1

 DLDP port state: Bidirectional

 Number of the port's neighbors: 1

  Neighbor MAC address: 0023-8956-3600

  Neighbor port index: 79

  Neighbor state: Confirmed

  Neighbor aged time: 13s

Interface GigabitEthernet1/0/2

 DLDP port state: Inactive

 Number of the port's neighbors: 0 (Maximum number ever detected: 1)

\# 显示接口GigabitEthernet1/0/1的DLDP信息。

\<Sysname\> display dldp interface gigabitethernet 1/0/1

Interface GigabitEthernet1/0/1

 DLDP port state: Bidirectional

 Number of the port's neighbors: 1

  Neighbor MAC address: 0023-8956-3600

  Neighbor port index: 79

  Neighbor state: Confirmed

  Neighbor aged time: 13s

表1-1 display dldp命令显示信息描述表

字段

描述

DLDP global status

DLDP的全局状态：

·Enabled：表示已使能

·Disabled：表示已关闭

DLDP advertisement interval

Advertisement报文的发送间隔，单位为秒

DLDP authentication-mode

当前设备与邻居设备间的DLDP认证模式：

·MD5：表示MD5认证

·None：表示不认证

·Simple：表示明文认证

DLDP authentication-password

当前设备与邻居设备间的DLDP认证密码：

·\*\*\*\*\*\*：表示已配置密码

·Not configured：表示已配置认证模式但尚未配置密码

DLDP unidirectional-shutdown mode

DLDP发现单向链路后接口的关闭模式：

·Auto：表示自动模式

·Manual：表示手动模式

DLDP delaydown-timer value

DelayDown定时器的超时时间，单位为秒

Number of enabled ports

使能DLDP的接口数

Interface

使能DLDP的接口名称

DLDP port state

DLDP接口的状态：

·Bidirectional：表示双通状态

·Inactive：表示非活动状态

·Initial：表示初始状态

·Unidirectional：表示单通状态

Number of the port's neighbors

接口的邻居数

Maximum number ever detected

接口曾收到的最大邻居数（只有在接口的当前邻居数与其曾收到的最大邻居数不一致时，才会显示本字段）

Neighbor MAC address

邻居的MAC地址

Neighbor port index

邻居的接口索引

Neighbor state

DLDP邻居的状态：

·Confirmed：表示确定状态

·Unconfirmed：表示未确定状态

Neighbor aged time

邻居的老化时间，单位为秒

**DLDP \-- DLDP配置命令 \-- display dldp statistics**

------------------------------------------------------------------------

**[display dldp statistics**]命令用来显示接口的DLDP报文统计信息。

【命令】

**[display dldp statistics ** **interface** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的DLDP报文统计信息，*interface-type interface-number*为接口类型和接口编号。如果未指定本参数，将显示所有接口的DLDP报文统计信息。

【举例】

\# 显示所有接口的DLDP报文统计信息。

\<Sysname\> display dldp statistics

Interface GigabitEthernet1/0/1

 Packets sent: 6

 Packets received: 5

 Invalid packets received: 2

 Loopback packets received: 0

 Authentication-failed packets received: 0

 Valid packets received: 3

Interface GigabitEthernet1/0/2

 Packets sent: 7

 Packets received: 7

 Invalid packets received: 3

 Loopback packets received: 0

 Authentication-failed packets received: 0

 Valid packets received: 4

表1-2 display dldp statistics命令显示信息描述表

字段

描述

Interface

使能DLDP的接口名称

Packets sent

发送的报文总数

Packets received

收到的报文总数

Invalid packets received

收到的错误报文数

Loopback packets received

收到的自环报文数

Authentication-failed packets received

收到的认证失败报文数

Valid packets received

收到的合法报文数

【相关命令】

·**reset dldp statistics**

**DLDP \-- DLDP配置命令 \-- dldp authentication-mode**

------------------------------------------------------------------------

**[dldp authentication-mode**]命令用来配置当前设备与邻居设备间的DLDP认证模式。

**[undo dldp authentication-mode**]命令用来恢复缺省情况。

【命令】

**[dldp authentication-mode**[ { **md5** \| **none** \| **simple** }]]

**[undo dldp authentication-mode**]

【缺省情况】

当前设备与邻居设备间的DLDP认证模式为不认证。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[md5**]：表示认证模式为MD5认证。

**[none**]：表示认证模式为不认证。

**[simple**]：表示认证模式为明文认证。

【使用指导】

·请确保两台设备间通过光纤/网线连接的接口上配置的DLDP认证模式和认证密码都相同，否则DLDP将无法正常工作。

·在配置认证模式为明文认证或MD5认证后若未配置认证密码，则认证模式将仍为不认证。

【举例】

\# 配置Device A和Device B通过光纤/网线连接的接口间的DLDP认证模式均为明文认证，认证密码均为abc。

·Device A上的配置：

\<DeviceA\> system-view

DeviceA dldp authentication-mode simple

DeviceA dldp authentication-password simple abc

·Device B上的配置：

\<DeviceB\> system-view

DeviceB dldp authentication-mode simple

DeviceB dldp authentication-password simple abc

【相关命令】

·**display dldp**

·**dldp authentication-password**

**DLDP \-- DLDP配置命令 \-- dldp authentication-password**

------------------------------------------------------------------------

**[dldp authentication-password**]命令用来配置当前设备与邻居设备间的DLDP认证密码。

**[undo dldp authentication-password**]命令用来恢复缺省情况。

【命令】

**[dldp authentication-password**[ { **cipher** *cipher* \| **simple** *simple* }]]

**[undo dldp authentication-password**]

【缺省情况】

没有配置当前设备与邻居设备间的DLDP认证密码。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher** *cipher*]：表示以密文方式输入的DLDP认证密码。*cipher*为1～53个字符的字符串，区分大小写。

**[simple** *simple*]：表示以明文方式输入的DLDP认证密码。*simple*为1～16个字符的字符串，区分大小写。

【使用指导】

·以明文或密文方式设置的DLDP认证密码，均以密文的方式保存在配置文件中。

·请确保两台设备间通过光纤/网线连接的接口上配置的DLDP认证模式和认证密码都相同，否则DLDP将无法正常工作。

·在配置认证模式为明文认证或MD5认证后若未配置认证密码，则认证模式将仍为不认证。

【举例】

\# 配置Device A和Device B通过光纤/网线连接的接口间的DLDP认证模式均为明文认证，认证密码均为abc。

·Device A上的配置：

\<DeviceA\> system-view

DeviceA dldp authentication-mode simple

DeviceA dldp authentication-password simple abc

·Device B上的配置：

\<DeviceB\> system-view

DeviceB dldp authentication-mode simple

DeviceB dldp authentication-password simpleabc

【相关命令】

·**display dldp**

·**dldp authentication-mode**

**DLDP \-- DLDP配置命令 \-- dldp delaydown-timer**

------------------------------------------------------------------------

**[dldp delaydown-timer**]命令用来配置DelayDown定时器的超时时间。

**[undo dldp delaydown-timer**]命令用来恢复缺省情况。

【命令】

**[dldp delaydown-timer** *time*]

**[undo dldp delaydown-timer**]

【缺省情况】

DelayDown定时器的超时时间为1秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：表示DelayDown定时器的超时时间，取值范围为1～5，单位为秒。

【使用指导】

本配置将应用于所有使能了DLDP功能的接口上。

【举例】

\# 配置DelayDown定时器的超时时间为2秒。

\<Sysname\> system-view

Sysname dldp delaydown-timer 2

【相关命令】

·**display dldp**

**DLDP \-- DLDP配置命令 \-- dldp enable**

------------------------------------------------------------------------

**[dldp enable**]命令用来在接口上使能DLDP功能。

**[undo dldp enable**]命令用来在接口上关闭DLDP功能。

【命令】

**[dldp enable**]

**[undo dldp enable**]

【缺省情况】

接口上的DLDP功能处于关闭状态。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

要启用DLDP功能，必须在全局和接口上都使能DLDP功能。

【举例】

\# 全局使能DLDP功能，并在接口GigabitEthernet1/0/1上使能DLDP功能。

\<Sysname\> system-view

Sysname dldp global enable

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dldp enable

【相关命令】

·**display dldp**

·**dldp global enable**

**DLDP \-- DLDP配置命令 \-- dldp global enable**

------------------------------------------------------------------------

**[dldp global enable**]命令用来全局使能DLDP功能。

**[undo dldp global enable**]命令用来全局关闭DLDP功能。

【命令】

**[dldp global enable**]

**[undo dldp global enable**]

【缺省情况】

DLDP功能处于全局关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

要启用DLDP功能，必须在全局和接口上都使能DLDP功能。

【举例】

\# 全局使能DLDP功能。

\<Sysname\> system-view

Sysname dldp global enable

【相关命令】

·**display dldp**

·**dldp enable**

**DLDP \-- DLDP配置命令 \-- dldp interval**

------------------------------------------------------------------------

**[dldp interval**]命令用来配置Advertisement报文的发送间隔。

**[undo dldp interval**]命令用来恢复缺省情况。

【命令】

**[dldp interval ***time*]

**[undo dldp interval**]

【缺省情况】

Advertisement报文的发送间隔为5秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：表示Advertisement报文的发送间隔，取值范围为1～100，单位为秒。

【使用指导】

·本配置将应用于所有使能了DLDP功能的接口上。

·请确保通过光纤/网线连接的两台设备上Advertisement报文的发送间隔相同，否则DLDP将无法正常工作。

【举例】

\# 配置Advertisement报文的发送间隔为20秒。

\<Sysname\> system-view

Sysname dldp interval 20

【相关命令】

·**display dldp**

**DLDP \-- DLDP配置命令 \-- dldp unidirectional-shutdown**

------------------------------------------------------------------------

**[dldp unidirectional-shutdown**]命令用来配置DLDP发现单向链路后接口的关闭模式。

**[undo dldp unidirectional-shutdown**]命令用来恢复缺省情况。

【命令】

**[dldp unidirectional-shutdown**[ { **auto** \| **manual** }]]

**[undo** **dldp unidirectional-shutdown**]

【缺省情况】

DLDP发现单向链路后接口的关闭模式为自动模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示自动模式。在此模式下，当DLDP检测到单向链路时会自动关闭单通接口。

**[manual**]：表示手动模式。在此模式下，当DLDP检测到单向链路时不会直接关闭单通接口，而是需要用户手工将其关闭；当单向链路恢复为双向链路后，还需要用户手工将其打开。

【举例】

\# 配置DLDP发现单向链路后接口的关闭模式为手动模式。

\<Sysname\> system-view

Sysname dldp unidirectional-shutdown manual

【相关命令】

·**display dldp**

**DLDP \-- DLDP配置命令 \-- reset dldp statistics**

------------------------------------------------------------------------

**[reset dldp statistics**]命令用来清除接口的DLDP报文统计信息。

【命令】

**[reset dldp statistics ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：清除指定接口的DLDP报文统计信息，*interface-type interface-number*为接口类型和接口编号。如果未指定本参数，将清除所有接口的DLDP报文统计信息。

【举例】

\# 清除所有接口的DLDP报文统计信息。

\<Sysname\> reset dldp statistics

【相关命令】

·**display dldp statistics**
