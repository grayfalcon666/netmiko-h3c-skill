<!-- CMD-INDEX
  accelerate                          | 二层ACL视图/IPv4基本ACL视图/IPv4高级ACL视图/IPv6基本ACL视图/IPv6高级ACL视图 | L35
  acl                                 | 系统视图             | L85
  acl copy                            | 系统视图             | L243
  acl hardware-mode                   | 系统视图             | L321
  acl hardware-mode ipv6              | 系统视图             | L373
  acl interval                        | 系统视图             | L423
  description                         | IPv4基本ACL视图/IPv4高级ACL视图/IPv6基本ACL视图/IPv6高级ACL视图/二层ACL视图/用户自定义ACL视图 | L487
  display acl                         | 任意视图             | L533
  display acl accelerate              | 任意视图             | L663
  display acl hardware-mode           | 任意视图             | L763
  display packet-filter               | 任意视图             | L843
  display packet-filter statistics    | 任意视图             | L1085
  display packet-filter statistics sum | 任意视图             | L1361
  display packet-filter verbose       | 任意视图             | L1493
  display qos-acl resource            | 任意视图             | L1769
  packet-filter(Interface view)       | 接口视图             | L1877
  packet-filter(Zone-pair security view) | 安全域间实例视图         | L1959
  packet-filter default deny          | 系统视图             | L2021
  packet-filter default hardware-count | 接口视图             | L2073
  packet-filter global                | 系统视图             | L2139
  packet-filter vlan                  | 系统视图             | L2223
  reset acl counter                   | 用户视图             | L2307
  reset packet-filter statistics      | 用户视图             | L2363
  rule (MAC ACL view)                 | 二层ACL视图          | L2441
  rule (IPv4 advanced ACL view)       | IPv4高级ACL视图      | L2533
  rule (IPv4 basic ACL view)          | IPv4基本ACL视图      | L2959
  rule (IPv6 advanced ACL view)       | IPv6高级ACL视图      | L3053
  rule (IPv6 basic ACL view)          | IPv6基本ACL视图      | L3485
  rule (user-defined ACL view)        | 用户自定义ACL视图       | L3581
  rule comment                        | IPv4基本ACL视图/IPv4高级ACL视图/IPv6基本ACL视图/IPv6高级ACL视图/二层ACL视图/用户自定义ACL视图 | L3667
  step                                | IPv4基本ACL视图/IPv4高级ACL视图/IPv6基本ACL视图/IPv6高级ACL视图/二层ACL视图 | L3725
-->

**ACL \-- ACL配置命令 \-- accelerate**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[accelerate**]命令用来开启ACL加速功能。

**[undo accelerate**]命令用来关闭ACL加速功能。

【命令】

**[accelerate**]

**[undo accelerate **]

【缺省情况】

ACL加速功能处于关闭状态。

【视图】

二层ACL视图/IPv4基本ACL视图/IPv4高级ACL视图/IPv6基本ACL视图/IPv6高级ACL视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

【举例】

\# 开启ACL加速功能。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 accelerate

【相关命令】

·**[display acl accelerate**](?1615842176#_Toc303849088)

**ACL \-- ACL配置命令 \-- acl**

------------------------------------------------------------------------

**[acl**]命令用来创建一个ACL，并进入相应的ACL视图。

**[undo** **acl**]命令用来删除指定或全部ACL。

【命令】

**[acl** [ **ipv6**  { **advanced** \| **basic** } { *acl-number* \| **name** *acl-name* } [ **match-order** { **auto** \| **config** } ]]]

**[acl**[ **mac** { *acl-number* \| **name** *acl-name* } [ **match-order** { **auto** \| **config** } ]]]

**[acl**[ **user-defined** { *acl-number* \| **name** *acl-name* } ]]

**[undo** **acl** [ **ipv6**  { **all** \| { **advanced** \| **basic** } { *acl-number* \| **name** *acl-name* } }]]

**[undo**[ **acl** **mac** { **all** \| *acl-number* \| **name** *acl-name* }]]

**[undo**[ **acl** **user-defined** { **all** \| *acl-number* \| **name** *acl-name* }]]

【缺省情况】

不存在任何ACL。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[basic**]：指定创建基本ACL。

**[advanced**]：指定创建高级ACL。

**[mac**]：指定创建二层ACL。

**[user-defined**]：指定创建用户自定义ACL。

**[number** *acl-number*]：指定ACL的编号。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。为避免混淆，ACL的名称不允许使用英文单词all。

**[match-order**[ { **auto** \| **config** }]]：指定规则的匹配顺序，**auto**表示按照自动排序（即"深度优先"原则）的顺序进行规则匹配，**config**表示按照配置顺序进行规则匹配。缺省情况下，规则的匹配顺序为配置顺序。用户自定义ACL不支持本参数，其规则匹配顺序只能为配置顺序。

**[all**]：指定类型中全部ACL。

【使用指导】

·使用**acl**命令时，如果指定编号或名称的ACL不存在，则创建该ACL并进入其视图，否则直接进入其视图。

·当ACL内不存在任何规则时，用户可以使用本命令对该ACL的规则匹配顺序进行修改，否则不允许进行修改。

·若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 创建一个编号为2000的IPv4基本ACL，并进入其视图。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000

\# 创建一个IPv4基本ACL，指定其名称为flow，并进入其视图。

\<Sysname\> system-view

Sysname acl basic name flow

Sysname-acl-ipv4-basic-flow

\# 创建一个编号为3000的IPv4高级ACL，并进入其视图。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000

\# 创建一个编号为2000的IPv6基本ACL，并进入其视图。

\<Sysname\> system-view

Sysname acl ipv6 basic 2000

Sysname-acl-ipv6-basic-2000

\# 创建一个IPv6基本ACL，其名称为flow，并进入其视图。

\<Sysname\> system-view

Sysname acl ipv6 basic name flow

Sysname-acl-ipv6-basic-flow

\# 创建一个IPv6高级ACL，其名称为abc，并进入其视图。

\<Sysname\> system-view

Sysname acl ipv6 advanced name abc

Sysname-acl-ipv6-adv-abc

\# 创建一个编号为4000的二层ACL，并进入其视图。

\<Sysname\> system-view

Sysname acl mac 4000

Sysname-acl-mac-4000

\# 创建一个二层ACL，其名称为flow，并进入其视图。

\<Sysname\> system-view

Sysname acl mac name flow

Sysname-acl-mac-flow

\# 创建一个编号为5000的用户自定义ACL，并进入其视图。

\<Sysname\> system-view

Sysname acl user-defined 5000

Sysname-acl-user-5000

\# 创建一个用户自定义ACL，其名称为flow，并进入其视图。

\<Sysname\> system-view

Sysname acl user-defined name flow

Sysname-acl-user-flow

【相关命令】

·**display** **acl**

**ACL \-- ACL配置命令 \-- acl copy**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[acl** **copy**]命令用来复制并生成一个新的ACL。

【命令】

**[acl**[ [ **ipv6** \| **mac** \| **user-defined** ] **copy** { *source-acl-number* \| **name** *source-acl-name* } **to** { *dest-acl-number* \| **name** *dest-acl-name* }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[source-acl-number*]：指定源ACL的编号，该ACL必须存在。本参数的取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *source-acl-name*]：指定源ACL的名称，该ACL必须存在。*source-acl-name*为1～63个字符的字符串，不区分大小写。

*[dest-acl-number*]：指定目的ACL的编号，该ACL必须不存在。本参数的取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *dest-acl-name*]：指定目的ACL的名称，该ACL必须不存在。*dest-acl-name*为1～63个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。为避免混淆，ACL的名称不允许使用英文单词all。

【使用指导】

·目的ACL的类型要与源ACL的类型相同。

·除了ACL的编号或名称不同外，新生成的ACL（即目的ACL）的匹配顺序、规则匹配统计功能的使能情况、规则编号的步长、所包含的规则、规则的描述信息以及ACL的描述信息等都与源ACL的相同。

·若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 通过复制已存在的IPv4基本ACL 2001，来生成一个新的编号为2002的同类型ACL。

\<Sysname\> system-view

Sysname acl copy 2001 to 2002

\# 通过复制已存在的IPv4基本ACL test，来生成名为paste的同类型ACL。

\<Sysname\> system-view

Sysname acl copy name test to name paste

**ACL \-- ACL配置命令 \-- acl hardware-mode**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[acl** **hardware-mode** **basic**]命令用来指定ACL的硬件模式。

【命令】

**[acl**[ **hardware-mode** { **advanced** \| **basic** }]]

【缺省情况】

ACL的硬件模式为高级模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[advanced**]：表示高级模式。在高级模式下，单板除了支持IPv4基本ACL、IPv4高级ACL和二层ACL外，还支持IPv6基本ACL、IPv6高级ACL和用户自定义ACL。

**[basic**]：表示基本模式。在基本模式下，单板仅支持IPv4基本ACL、IPv4高级ACL和二层ACL。

【使用指导】

本命令不会立即生效，必须在保存配置后待系统下次启动时才生效。

【举例】

\# 指定ACL的硬件模式为基本模式。

\<Sysname\> system-view

Sysname acl hardware-mode basic

【相关命令】

·**display** **acl****hardware-mode**

**ACL \-- ACL配置命令 \-- acl hardware-mode ipv6**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[acl** **hardware-mode** **ipv6**]命令用来开启或关闭ACL硬件模式下的IPv6功能。

【命令】

**[acl**[ **hardware-mode** **ipv6** { **disable** \| **enable** }]]

【缺省情况】

ACL硬件模式下的IPv6功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disable**]：表示关闭IPv6功能。当IPv6功能关闭时，单板仅支持IPv4基本ACL、IPv4高级ACL和二层ACL。

**[enable**]：表示开启IPv6功能。当IPv6功能开启时，单板除了支持IPv4基本ACL、IPv4高级ACL和二层ACL外，还支持IPv6基本ACL、IPv6高级ACL和用户自定义ACL。

【使用指导】

本命令不会立即生效，必须在保存配置后待系统下次启动时才生效。

【举例】

\# 开启ACL硬件模式下的IPv6功能。

\<Sysname\> system-view

Sysname acl hardware-mode ipv6 enable

【相关命令】

·**display** **acl****hardware-mode**

**ACL \-- ACL配置命令 \-- acl interval**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[acl **[{ **logging** \| **trap** } **interval**]]命令用来配置报文过滤日志信息或告警信息的生成与发送周期，同时使能报文的首包上送功能。

**[undo acl **[{ **logging** \| **trap** } **interval**]]命令用来恢复缺省情况。

【命令】

**[acl **[{ **logging** \| **trap** } **interval** *interval*]]

**[undo acl **[{ **logging** \| **trap** } **interval**]]

【缺省情况】

报文过滤日志信息或告警信息的生成与发送周期为0分钟，即不记录报文过滤的日志。报文首包上送功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[logging**]：指定周期性地生成报文过滤日志信息并发送到信息中心。有关信息中心的详细介绍请参见"网络管理和监控配置指导"中的"信息中心"。

**[trap**]：指定周期性地生成告警信息并发送到SNMP模块。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

**[interval ***interval*]：报文过滤日志信息或告警信息的生成与发送周期，取值范围为0～1440，且必须为5的整数倍，0表示不进行记录，单位为分钟。

【使用指导】

系统只支持对应用IPv4基本ACL、IPv4高级ACL、IPv6基本ACL、IPv6高级ACL或二层ACL进行报文过滤的报文过滤日志信息或告警信息进行记录，且在上述ACL中配置规则时必须指定**logging**参数。

【举例】

\# 配置IPv4报文过滤日志的生成与发送周期为10分钟。

\<Sysname\> system-view

Sysname acl logging interval 10

【相关命令】

·**rule** (IPv4 advanced ACL view)

·**rule** (IPv4 basic ACL view)

·**rule** (IPv6 advanced ACL view)

·**rule** (IPv6 basic ACL view)

·**rule** (MAC ACL view)

**ACL \-- ACL配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置ACL的描述信息。

**[undo** **description**]命令用来删除ACL的描述信息。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

ACL没有任何描述信息。

【视图】

IPv4基本ACL视图/IPv4高级ACL视图/IPv6基本ACL视图/IPv6高级ACL视图/二层ACL视图/用户自定义ACL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：表示ACL的描述信息，为1～127个字符的字符串，区分大小写。

【举例】

\# 为IPv4基本ACL 2000配置描述信息。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 description This is an IPv4 basic ACL.

【相关命令】

·**display** **acl**

**ACL \-- ACL配置命令 \-- display acl**

------------------------------------------------------------------------

**[display** **acl**]命令用来显示ACL的配置和运行情况。

【命令】

**[display**[ **acl** [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **all** \| **name** *acl-name* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：显示指定编号的ACL的配置和运行情况。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[all**]：显示指定类型中全部ACL的配置和运行情况。

**[name** *acl-name*]：显示指定名称的ACL的配置和运行情况。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

本命令将按照实际匹配顺序来排列ACL内的规则，即：当ACL的规则匹配顺序为配置顺序时，各规则将按照编号由小到大排列；当ACL的规则匹配顺序为自动排序时，各规则将按照"深度优先"原则由深到浅排列。

若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 显示IPv4基本ACL 2001的配置和运行情况。

\<Sysname\> display acl 2001

Basic IPv4 ACL 2001, 2 rules, match-order is auto,

This is an IPv4 basic ACL.

ACL\'s step is 5

ACL accelerated

 rule 5 permit source 1.1.1.1 0 (5 times matched)

 rule 5 comment This rule is used on GigabitEthernet 1/0/1.

 rule 10 permit source object-group permit (5 times matched)

表1-1 display acl命令显示信息描述表

字段

描述

Basic IPv4 ACL 2001

该ACL的类型和编号，ACL的类型包括：

·Basic IPv4 ACL：表示IPv4基本ACL

·Advanced IPv4 ACL：表示IPv4高级ACL

·Basic IPv6 ACL：表示IPv6基本ACL

·Advanced IPv6 ACL：表示IPv6高级ACL

·MAC ACL：表示二层ACL

·User defined ACL：表示用户自定义ACL

2 rules

该ACL内包含的规则数量

match-order is auto

该ACL的规则匹配顺序为自动排序（匹配顺序为配置顺序时不显示本字段）

This is an IPv4 basic ACL.

该ACL的描述信息

ACL\'s step is 5

该ACL的规则编号的步长值为5

ACL accelerated

该ACL使能了加速功能

rule 5 permit source 1.1.1.1 0

规则5的具体内容，源地址为具体地址

rule 10 permit source object-group permit

规则10的具体内容，源地址为对象组

5 times matched

该规则匹配的次数为5（仅统计软件ACL的匹配次数，当匹配次数为0时不显示本字段）

rule 5 comment This rule is used on GigabitEthernet 1/0/1.

规则5的描述信息

**ACL \-- ACL配置命令 \-- display acl accelerate**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display acl** **accelerate**]命令用来显示ACL的加速状态。

【命令】

集中式设备：

**[display acl**[ **accelerate** { **summary** [ **ipv6** \| **mac** ] \| **verbose** [ **ipv6** \| **mac** ] { *acl-number* \| **name** *acl-name* } }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display acl**[ **accelerate** { **summary** [ **ipv6** \| **mac** ] \| **verbose** [ **ipv6** \| **mac** ] { *acl-number* \| **name** *acl-name* } **slot** *slot-number* ]{.apple-converted-space}**cpu**{.apple-converted-space}*cpu-number * }]

分布式设备－IRF模式：

**[display acl**[ **accelerate** { **summary** [ **ipv6** \| **mac** ] \| **verbose** [ **ipv6** \| **mac** ] { *acl-number* \| **name** *acl-name* } **chassis** *chassis-number* **slot** *slot-number* ]{.apple-converted-space}**cpu**{.apple-converted-space}*cpu-number * }]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[summary**]：显示ACL加速的概要信息。

**[verbose**]：显示ACL加速的详细信息。

**[ipv6**]：显示IPv6 ACL的加速状态。

**[mac**]：显示二层ACL的加速状态。

*[acl-number*]：显示指定编号的ACL的加速状态。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

**[name** *acl-name*]：显示指定名称的ACL的加速状态。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

**[slot*** slot-number*]：显示指定单板的ACL加速[信息，该单板必须为加速芯片所在单板，]*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的ACL加速[信息，该设备必须为加速芯片所在成员设备，]*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ACL加速[信息，该单板必须为加速芯片所在单板，]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU上ACL加速[信息，]*cpu-number*表示CPU的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

若未指定**ipv6**或**mac**参数，则表示IPv4 ACL。

【举例】

\# 显示加速概要信息。

\<Sysname\>display acl accelerate summary

Basic IPv4 ACL 2000

ACL named acl.

\# 显示加速详细信息。

\<Sysname\>display acl accelerate verbose 2000

Basic IPv4 ACL 2000.

 rule 0 permit

 rule 1 deny (failed)

表1-2 display acl accelerate verbose命令显示信息描述表

字段

描述

failed

表示此规则加速失败，匹配不生效

**ACL \-- ACL配置命令 \-- display acl hardware-mode**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **acl** **hardware-mode**]命令用来显示ACL的硬件模式及其IPv6状态。

【命令】

**[display** **acl** **hardware-mode**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示ACL的硬件模式及其IPv6状态。

\<Sysname\> display acl hardware-mode

Current ACL hardware mode:

 Mode: Advanced

 IPv6 status: Disabled

Next startup ACL hardware mode:

 Mode: Basic

 IPv6 status: Enabled

![说明](ACL命令.files/image001.jpg)

本命令的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-3 display acl hardware-mode命令显示信息描述表

字段

描述

Current ACL hardware mode

当前的ACL硬件模式及其IPv6状态

Next startup ACL hardware mode

下次启动后的ACL硬件模式及其IPv6状态

Mode

ACL的硬件模式，包括：

·Basic：表示基本模式

·Advanced：表示高级模式

IPv6 status

ACL硬件模式下的IPv6状态，包括：

·Enabled：表示IPv6功能已开启

·Disabled：表示IPv6功能已关闭

**ACL \-- ACL配置命令 \-- display packet-filter**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **packet-filter**]命令用来显示ACL在报文过滤中的应用情况。

【命令】

集中式设备：

**[display**[ **packet-filter** { { **global** \| **interface** [ *interface-type* *interface-number* ] \| **vlan**  *vlan-id*  } [ **inbound** \| **outbound** ] \| **zone-pair security**  **source** *source-zone-name* **destination** *destination-zone-name*  }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **packet-filter** { **interface** [ *interface-type* *interface-number*  [ **inbound** \| **outbound** ] \| { { **global** \| **interface** **vlan-interface** *vlan-interface-number* \| **vlan**  *vlan-id*  } [ **inbound** \| **outbound** ] \| **zone-pair security**  **source** *source-zone-name* **destination** *destination-zone-name*  }  **slot** *slot-number* [ **cpu** *cpu-number*  ] }]]

分布式设备－IRF模式：

**[display** **packet-filter** { **interface** [ *interface-type* *interface-number*  [ **inbound** \| **outbound** ] \| { { **global** \| **interface** **vlan-interface** *vlan-interface-number* \| **vlan**  *vlan-id*  } [ **inbound** \| **outbound** ] \| **zone-pair security**  **source** *source-zone-name* **destination** *destination-zone-name*  }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示ACL在报文过滤中的全局（即所有物理接口）应用情况。

**[interface** [ *interface-type* *interface-number* ]]：显示指定接口上ACL在报文过滤中的应用情况。*interface-type* *interface-number*表示接口类型和接口编号。若未指定接口类型和接口编号，将显示所有接口上ACL在报文过滤中的应用情况。（集中式设备）

**[interface** [ *interface-type* *interface-number* ]]：显示指定接口上ACL在报文过滤中的应用情况。*interface-type* *interface-number*表示接口类型和接口编号，这里的接口类型不包括VLAN接口。若未指定接口类型和接口编号，将显示除VLAN接口以外的所有接口上ACL在报文过滤中的应用情况。（分布式设备－独立运行模式、集中式IRF设备和分布式设备－IRF模式）

**[interface** **vlan-interface** *vlan-interface-number*]：显示指定VLAN接口上ACL在报文过滤中的应用情况。*vlan-interface-number*表示VLAN接口的编号。

**[vlan** [ *vlan-id* ]]：显示指定VLAN中ACL在报文过滤中的应用情况。*vlan-id*表示VLAN的编号。若未指定VLAN编号，将显示所有VLAN中ACL在报文过滤中的应用情况。

**[zone-pair security ** **source** *source-zone-name* **destination** *destination-zone-name* ]：显示指定安全域间实例上ACL在报文过滤中的应用情况。*source-zone-name*：表示安全域间实例源安全域的名称，为1～31个字符的字符串，不区分大小写。*destination-zone-name*：表示安全域间实例目的安全域的名称，为1～31个字符的字符串，不区分大小写。

**[inbound**]：显示入方向上ACL在报文过滤中的应用情况。

**[outbound**]：显示出方向上ACL在报文过滤中的应用情况。

**[slot** *slot-number*]：显示指定单板上ACL在报文过滤中的应用情况，*slot-number*表示单板所在的槽位号。若未指定本参数，将显示主用主控板上ACL在报文过滤中的应用情况。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上ACL在报文过滤中的应用情况，*slot-number*表示设备在IRF中的成员编号。若未指定本参数，将显示主用设备上ACL在报文过滤中的应用情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上ACL在报文过滤中的应用情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若未指定本参数，将显示主用设备上ACL在报文过滤中的应用情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上ACL在报文过滤中的应用情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若未指定本参数，将显示全局主用主控板上ACL在报文过滤中的应用情况。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上ACL在报文过滤中的应用情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若未指定本参数，将显示全局主用主控板上ACL在报文过滤中的应用情况。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上ACL在报文过滤中的应用情况，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

显示安全域间实例上的应用情况时不区分方向，其他情况，若未指定**inbound**和**outbound**参数，将同时显示出、入方向上ACL在报文过滤中的应用情况。

【举例】

\# 显示VLAN 2中出、入方向上ACL在报文过滤中的应用情况。

\<Sysname\> display packet-filter vlan 2

VLAN: 2

In-bound policy:

  IPv4 ACL 2001

  IPv6 ACL 2001

  MAC ACL 4001

  IPv4 default action: Deny

  IPv6 default action: Deny

  MAC default action: Deny

Out-bound policy:

  IPv6 ACL 2001 (Failed)

  IPv6 default action: Deny (Failed)

\# 显示接口GigabitEthernet1/0/1入方向上ACL在报文过滤中的应用情况。

\<Sysname\> display packet-filter interface gigabitethernet 1/0/1 inbound

Interface: GigabitEthernet1/0/1

 In-bound policy:

  IPv4 ACL 2001

  IPv6 ACL 2002 (Failed)

  MAC ACL 4003 (Failed), Hardware-count (Failed)

  IPv4 ACL 2004, Hardware-count (Failed)

  IPv4 default action: Deny, Hardware-count

\# 显示出、入方向上ACL在报文过滤中的全局应用情况。

\<Sysname\> display packet-filter global

Global:

 In-bound policy:

  IPv4 ACL 2001

  IPv6 ACL 2001

  MAC ACL 4001

  IPv4 default action: Deny (Failed)

  IPv6 default action: Deny (Failed)

  MAC default action: Deny

 Out-bound policy:

  MAC ACL 4001, Hardware-count

  MAC default action: Deny

\# 显示安全域间实例源域office到目的域library上ACL在报文过滤中的应用情况。

\<Sysname\> display packet-filter zone-pair security source office destination library

Zone-pair: source office destination library

  IPv4 ACL 2001

  IPv4 ACL 2002

表1-4 display packet-filter命令显示信息描述表

字段

描述

Interface

ACL在指定接口上的应用情况

VLAN

ACL在指定VLAN中的应用情况

Zone-pair

ACL在指定安全域间实例上的应用情况

Global

ACL的全局（即所有物理接口）应用情况

In-bound policy

ACL在入方向上的应用情况

Out-bound policy

ACL在出方向上的应用情况

IPv4 ACL 2001

IPv4基本ACL 2001应用成功

IPv6 ACL 2002 (Failed)

IPv6基本ACL 2002应用失败

Hardware-count

规则匹配统计功能应用成功

Hardware-count (Failed)

规则匹配统计功能应用失败

IPv4 default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

IPv6 default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

MAC default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

**ACL \-- ACL配置命令 \-- display packet-filter statistics**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **packet-filter** **statistics**]命令用来显示ACL在报文过滤中应用的统计信息以及报文过滤缺省动作的统计信息。

【命令】

**[display**[ **packet-filter** **statistics** { { **global** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* } { **inbound** \| **outbound** } [ **default** \| [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } ] \| **zone-pair security** **source** *source-zone-name* **destination** *destination-zone-name*  [ **ipv6**  { *acl-number* \| **name** *acl-name* } ] }  **brief** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示全局（即所有物理接口）统计信息。

**[interface** *interface-type* *interface-number*]：显示指定接口上的统计信息。*interface-type* *interface-number*表示接口类型和接口编号。

**[vlan** *vlan-id*]：显示指定VLAN中的统计信息。*vlan-id*表示VLAN的编号。

**[zone-pair security source ***source-zone-name ***destination ***destination-zone-name*]：显示指定安全域间实例上的统计信息。*source-zone-name*：表示安全域间实例源安全域的名称，为1～31个字符的字符串，不区分大小写。*destination-zone-name*：表示安全域间实例目的安全域的名称，为1～31个字符的字符串，不区分大小写。

**[inbound**]：显示入方向上的统计信息。

**[outbound**]：显示出方向上的统计信息。

**[default**]：显示报文过滤缺省动作的统计信息。

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：显示指定编号ACL在报文过滤中应用的统计信息。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：显示指定名称ACL在报文过滤中应用的统计信息。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

**[brief**]：显示简要统计信息。

【使用指导】

·若未指定**default**、*acl-number*、**name** *acl-name*和ACL类型（**ipv6**、**mac**、**user-defined**）参数，将显示全部ACL在报文过滤中应用的统计信息以及报文过滤缺省动作的统计信息。

·显示安全域间实例统计信息时不区分方向。

·若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 显示接口GigabitEthernet1/0/1入方向上全部ACL在报文过滤中应用的统计信息以及报文过滤缺省动作的统计信息。

\<Sysname\> display packet-filter statistics interface gigabitethernet 1/0/1 inbound

Interface: GigabitEthernet1/0/1

 In-bound policy:

  IPv4 ACL 2001, Hardware-count

   From 2011-06-04 10:25:21 to 2011-06-04 10:35:57

   rule 0 permit source 2.2.2.2 0 (2 packets)

   rule 5 permit source 1.1.1.1 0 (Failed)

   rule 10 permit vpn-instance test (No resource)

   Totally 2 packets permitted, 0 packets denied

   Totally 100% permitted, 0% denied

  IPv4 ACL 2002 (Failed)

  MAC ACL 4000

   From 2011-06-04 10:25:34 to 2011-06-04 10:35:57

   rule 0 permit

  IPv6 ACL 2000

  IPv4 default action: Deny, Hardware-count

   From 2011-06-04 10:25:21 to 2011-06-04 10:35:57

   Totally 7 packets

  IPv6 default action: Deny, Hardware-count

   From 2011-06-04 10:25:41 to 2011-06-04 10:35:57

   Totally 0 packets

  MAC default action: Deny, Hardware-count

   From 2011-06-04 10:25:34 to 2011-06-04 10:35:57

   Totally 0 packets

\# 显示VLAN 2中入方向上IPv4高级ACL 3000在报文过滤中应用的统计信息。

\<Sysname\> display packet-filter statistics vlan 2 inbound 3000

VLAN: 2

 In-bound policy:

  IPv4 ACL 3000, Hardware-count (Failed)

   From 2011-06-04 10:25:34 to 2011-06-04 10:35:57

   rule 0 permit source 2.2.2.2 0

   rule 5 permit source 1.1.1.1 0 counting (2 packets)

   rule 10 permit vpn-instance test (Failed)

\# 显示安全域间实例源域office到目的域library上IPv4高级ACL 3000在报文过滤中应用的统计信息。

\<Sysname\> display packet-filter statistics zone-pair security source office destination library 3001

Zone-pair: source office destination library

IPv4 ACL 3001

   rule 0 permit source 2.2.2.2 0

   rule 5 permit source 1.1.1.1 0 counting (2 packets)

   rule 10 permit vpn-instance test (Failed)

   Totally 2 packets permitted, 0 packets denied

   Totally 100% permitted, 0% denied

表1-5 display packet-filter statistics命令显示信息描述表

字段

描述

Interface

在指定接口上应用的统计信息

VLAN

在指定VLAN中应用的统计信息

Zone-pair

在指定安全域间实例上应用的统计信息

In-bound policy

在入方向上应用的统计信息

Out-bound policy

在出方向上应用的统计信息

IPv4 ACL 2001

IPv4基本ACL 2001应用成功

IPv4 ACL 2002 (Failed)

IPv4基本ACL 2002应用失败

Hardware-count

规则匹配统计功能应用成功

Hardware-count (Failed)

规则匹配统计功能应用失败

From 2011-06-04 10:25:21 to 2011-06-04 10:35:57

该统计的起始和终止时间

2 packets

该规则匹配了2个包（当匹配的包个数为0时不显示本字段）

No resource

该规则对应的统计资源不足。在显示统计信息时，若该规则的统计资源不足，便会显示本字段（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）

rule 5 permit source 1.1.1.1 0 (Failed)

规则5应用失败

Totally 2 packets permitted, 0 packets denied

该ACL允许和拒绝符合条件报文的个数

Totally 100% permitted, 0% denied

该ACL允许符合条件报文的通过率和拒绝符合条件报文的丢弃率

IPv4 default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

IPv6 default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

MAC default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

Totally 7 packets

报文过滤缺省动作的执行次数

【相关命令】

·**reset** **packet-filter** **statistics**

**ACL \-- ACL配置命令 \-- display packet-filter statistics sum**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **packet-filter** **statistics sum**]命令用来显示ACL在报文过滤中应用的累加统计信息。

【命令】

**[display**[ **packet-filter** **statistics** **sum** { **inbound** \| **outbound** } [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* }  **brief** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[inbound**]：显示入方向上ACL在报文过滤中应用的累加统计信息。

**[outbound**]：显示出方向上ACL在报文过滤中应用的累加统计信息。

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：显示指定编号ACL在报文过滤中应用的累加统计信息。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：显示指定名称ACL在报文过滤中应用的累加统计信息。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

**[brief**]：显示ACL在报文过滤中应用的简要累加统计信息。

【使用指导】

若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 显示入方向上IPv4基本ACL 2001在报文过滤中应用的累加统计信息。

\<Sysname\> display packet-filter statistics sum inbound 2001

Sum:

 In-bound policy:

  IPv4 ACL 2001

   rule 0 permit source 2.2.2.2 0 (2 packets)

   rule 5 permit source 1.1.1.1 0

   rule 10 permit vpn-instance test

   Totally 2 packets permitted, 0 packets denied

   Totally 100% permitted, 0% denied

\# 显示入方向上IPv4基本ACL 2000在报文过滤中应用的简要累加统计信息。

\<Sysname\> display packet-filter statistics sum inbound 2000 brief

Sum:

 Inbound policy:

  IPv4 ACL 2000

   Totally 2 packets permitted, 0 packets denied

   Totally 100% permitted, 0% denied

表1-6 display packet-filter statistics sum命令显示信息描述表

字段

描述

Sum

ACL在报文过滤中应用的累加统计信息

In-bound policy

ACL在入方向上应用的累加统计信息

Out-bound policy

ACL在出方向上应用的累加统计信息

IPv4 ACL 2001

IPv4基本ACL 2001应用的累加统计信息

2 packets

该规则匹配了2个包（当匹配的包个数为0时不显示本字段）

Totally 2 packets permitted, 0 packets denied

该ACL允许和拒绝符合条件报文的个数

Totally 100% permitted, 0% denied

该ACL允许符合条件报文的通过率和拒绝符合条件报文的丢弃率

【相关命令】

·**reset** **packet-filter** **statistics**

**ACL \-- ACL配置命令 \-- display packet-filter verbose**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **packet-filter** **verbose**]命令用来显示ACL在报文过滤中的详细应用情况。

【命令】

集中式设备：

**[display**[ **packet-filter** **verbose** { { **global** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* } { **inbound** \| **outbound** } [ [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } ] \| **zone-pair security source** *source-zone-name* **destination** *destination-zone-name* }  [ **ipv6**  { *acl-number* \| **name** *acl-name* } ] }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **packet-filter** **verbose** { { **global** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* } { **inbound** \| **outbound** } [ [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } ]  \| **zone-pair security source** *source-zone-name* **destination** *destination-zone-name* }  [ **ipv6**  { *acl-number* \| **name** *acl-name* } ] }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display**[ **packet-filter** **verbose** { { **global** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* } { **inbound** \| **outbound** } [ [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } ] \| **zone-pair security source** *source-zone-name* **destination** *destination-zone-name* }  [ **ipv6**  { *acl-number* \| **name** *acl-name* } ] }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示ACL在报文过滤中的全局（即所有物理接口）详细应用情况。

**[interface** *interface-type* *interface-number*]：显示指定接口上ACL在报文过滤中的详细应用情况。*interface-type* *interface-number*表示接口类型和接口编号。

**[vlan** *vlan-id*]：显示指定VLAN中ACL在报文过滤中的详细应用情况。*vlan-id*表示VLAN的编号。

**[zone-pair security source ***source-zone-name ***destination ***destination-zone-name*]：显示指定安全域间实例上ACL在报文过滤中的详细应用情况。*source-zone-name*：表示安全域间实例源安全域的名称，为1～31个字符的字符串，不区分大小写。*destination-zone-name*：表示安全域间实例目的安全域的名称，为1～31个字符的字符串，不区分大小写。

**[inbound**]：显示入方向上ACL在报文过滤中的详细应用情况。

**[outbound**]：显示出方向上ACL在报文过滤中的详细应用情况。

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：显示指定编号ACL在报文过滤中的详细应用情况。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：显示指定名称ACL在报文过滤中的详细应用情况。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

**[slot** *slot-number*]：显示指定单板上ACL在报文过滤中的详细应用情况，*slot-number*表示单板所在的槽位号。若未指定本参数，将显示主用主控板上ACL在报文过滤中的详细应用情况。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上ACL在报文过滤中的详细应用情况，*slot-number*表示设备在IRF中的成员编号。若未指定本参数，将显示主用设备上ACL在报文过滤中的详细应用情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上ACL在报文过滤中的详细应用情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若未指定本参数，将显示主用设备上ACL在报文过滤中的详细应用情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上ACL在报文过滤中的详细应用情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若未指定本参数，将显示全局主用主控板上ACL在报文过滤中的详细应用情况。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上ACL在报文过滤中的详细应用情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若未指定本参数，将显示全局主用主控板上ACL在报文过滤中的详细应用情况。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上ACL在报文过滤中的详细应用情况，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

·若未指定**default**、*acl-number*、**name** *acl-name*和ACL类型（**ipv6**、**mac**、**user-defined**）参数，将显示全部ACL在报文过滤中应用的统计信息以及报文过滤缺省动作的统计信息。

·显示安全域间实例详细应用情况时不区分方向。

·若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 显示VLAN 2中入方向上全部ACL在报文过滤中的详细应用情况。

\<Sysname\> display packet-filter verbose vlan 2 inbound

VLAN: 2

 In-bound policy:

  IPv4 ACL 2001, Hardware-count

   rule 0 permit

   rule 5 permit source 1.1.1.1 0 (Failed)

   rule 10 permit vpn-instance test (Failed)

  IPv4 ACL 2002 (Failed)

\# 显示接口GigabitEthernet1/0/1入方向上全部ACL在报文过滤中的详细应用情况。

\<Sysname\> display packet-filter verbose interface gigabitethernet 1/0/1 inbound

Interface: GigabitEthernet1/0/1

 In-bound policy:

  IPv4 ACL 2001, Hardware-count (Failed)

   rule 0 permit

   rule 5 permit source 1.1.1.1 0 (Failed)

   rule 10 permit vpn-instance test (Failed)

  IPv4 ACL 2002 (Failed), Hardware-count (Failed)

  IPv6 ACL 2000, Hardware-count

   rule 0 permit

  MAC ACL 4000, Hardware-count

  IPv4 default action: Deny, Hardware-count (Failed)

  IPv6 default action: Deny, Hardware-count (Failed)

  MAC default action: Deny, Hardware-count

\# 显示入方向上全部ACL在报文过滤中的全局详细应用情况。

\<Sysname\> display packet-filter verbose global inbound

Global:

 In-bound policy:

  IPv4 ACL 2001

   rule 0 permit

   rule 5 permit source 1.1.1.1 0 (Failed)

   rule 10 permit vpn-instance test (Failed)

  IPv4 ACL 2002 (Failed)

  IPv6 ACL 2000, Hardware-count

  MAC ACL 4000, Hardware-count

   rule 0 permit

  IPv4 default action: Deny

  IPv6 default action: Deny

  MAC default action: Deny

\#显示安全域间实例源域office到目的域library上全部ACL在报文过滤中的详细应用情况。

\<Sysname\> display packet-filter verbose zone-pair security source office destination library

Zone-pair: source office destination library

  IPv4 ACL 2001

   rule 0 permit

   rule 5 permit source 1.1.1.1 0

   rule 10 permit vpn-instance test

表1-7 display packet-filter verbose命令显示信息描述表

字段

描述

Interface

ACL在指定接口上的详细应用情况

VLAN

ACL在指定VLAN中的详细应用情况

Zone-pair

ACL在指定安全域间实例上的详细应用情况

Global

ACL的全局（即所有物理接口）详细应用情况

In-bound policy

ACL在入方向上的详细应用情况

Out-bound policy

ACL在出方向上的详细应用情况

IPv4 ACL 2001

IPv4基本ACL 2001应用成功

IPv4 ACL 2002 (Failed)

IPv4基本ACL 2002应用失败

Hardware-count

规则匹配统计功能应用成功

Hardware-count (Failed)

规则匹配统计功能应用失败

rule 5 permit source 1.1.1.1 0 (Failed)

规则5应用失败

IPv4 default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

IPv6 default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

MAC default action

报文过滤的缺省动作，包括：

·Deny：报文过滤缺省动作为Deny应用成功

·Deny (Failed)：报文过滤缺省动作为Deny应用失败，实际动作仍为Permit

·Permit：报文过滤缺省动作为Permit

·Hardware-count：报文过滤缺省动作统计功能应用成功

·Hardware-count (Failed)：报文过滤缺省动作统计功能应用失败

**ACL \-- ACL配置命令 \-- display qos-acl resource**

------------------------------------------------------------------------

**[display** **qos-acl** **resource**]命令用来显示QoS和ACL资源的使用情况。

【命令】

集中式设备：

**[display** **qos-acl** **resource**]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **qos-acl** **resource** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **qos-acl** **resource** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板上QoS和ACL资源的使用情况，*slot-number*表示单板所在的槽位号。若未指定本参数，将显示所有单板上QoS和ACL资源的使用情况。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上QoS和ACL资源的使用情况，*slot-number*表示设备在IRF中的成员编号。若未指定本参数，将显示IRF中所有成员设备上QoS和ACL资源的使用情况。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上QoS和ACL资源的使用情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若未指定本参数，将显示所有成员设备/PEX上QoS和ACL资源的使用情况。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上QoS和ACL资源的使用情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若未指定本参数，将显示IRF中所有成员设备的所有单板上QoS和ACL资源的使用情况。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上QoS和ACL资源的使用情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若未指定本参数，将显示所有单板上QoS和ACL资源的使用情况。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上QoS和ACL资源的使用情况，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

如果指定的单板/成员设备不支持统计QoS和ACL资源，将不会显示该单板/成员设备上QoS和ACL资源的使用情况。

【举例】

\# 显示QoS和ACL资源的使用情况。

\<Sysname\> display qos-acl resource

Interfaces: GE1/0/1 to GE1/0/2

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Type             Total      Reserved   Configured Remaining  Usage

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPv4 ACL         2048       512        0          1536       25%

 IPv6 ACL         8192       1536       6656       0          100%

![说明](ACL命令.files/image001.jpg)

本命令的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-8 display qos-acl resource命令显示信息描述表

字段

描述

Interfaces

资源对应的接口范围

Type

资源类型

Total

资源总数

Reserved

预留的资源数

Configured

已经配置的资源数

Remaining

剩余可用的资源数

Usage

预留的资源数与已配置的资源数之和占资源总数的百分比，分子按实际计算结果的整数部分显示，例如实际计算结果为50.8%，此处显示为50%。

**ACL \-- ACL配置命令 \-- packet-filter(Interface view)**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[packet-filter**]命令用来在接口上应用ACL进行报文过滤。

**[undo** **packet-filter**]命令用来取消在接口上应用ACL进行报文过滤。

【命令】

**[packet-filter**[ [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } { **inbound**  **extension**  \| **outbound** }  **hardware-count** ]]

**[undo**[ **packet-filter** [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } { **inbound** \| **outbound** }]]

【缺省情况】

接口不对报文进行过滤。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：指定ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

**[inbound**]：对收到的报文进行过滤。

**[extension**]：对报文过滤进行扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outbound**]：对发出的报文进行过滤。

**[hardware-count**]：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能指定ACL内所有规则的匹配统计功能，而**rule**命令中的**counting**参数则用于使能当前规则的匹配统计功能。

【使用指导】

若未指定**ipv6**、**mac**或**user-defined**关键字，则表示IPv4 ACL。

【举例】

\# 应用IPv4基本ACL 2001对接口GigabitEthernet1/0/1收到的报文进行过滤，并对过滤的报文进行统计。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 packet-filter 2001 inbound hardware-count

【相关命令】

·**display** **packet-filter**

·**display** **packet-filter** **statistics**

·**display** **packet-filter** **verbose**

**ACL \-- ACL配置命令 \-- packet-filter(Zone-pair security view)**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[packet-filter**]命令用来在安全域间实例上应用ACL进行报文过滤。

**[undo** **packet-filter**]命令用来取消在安全域间实例上应用ACL进行报文过滤。

【命令】

**[packet-filter** [ **ipv6**  { *acl-number* \| **name** *acl-name* } ]]

**[undo** **packet-filter** [ **ipv6**  { *acl-number* \| **name** *acl-name* } ]]

【缺省情况】

安全域间实例不对报文进行过滤。

【视图】

安全域间实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。若未指定本参数，则表示IPv4 ACL。

*[acl-number*]：指定ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

**[name** *acl-name*]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

【举例】

\# 应用IPv4基本ACL 2002对安全域间实例source office destination library收到的报文进行过滤。

\<Sysname\> system-view

Sysname zone-pair security source office destination library

Sysname-zone-pair-security-office-library packet-filter 2002

【相关命令】

·**display** **packet-filter**

·**display** **packet-filter** **statistics**

·**display packet-filter verbose**

**ACL \-- ACL配置命令 \-- packet-filter default deny**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[packet-filter** **default** **deny**]命令用来配置报文过滤的缺省动作为Deny，即禁止未匹配上ACL规则的报文通过。

**[undo** **packet-filter** **default** **deny**]命令用来恢复缺省情况。

【命令】

**[packet-filter** **default** **deny**]

**[undo** **packet-filter** **default** **deny**]

【缺省情况】

报文过滤的缺省动作为Permit，即允许未匹配上ACL规则的报文通过。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置报文过滤的缺省动作会在所有的应用对象下添加一个缺省动作应用，该应用也会像其它应用的ACL一样显示。

【举例】

\# 配置报文过滤的缺省动作为Deny。

\<Sysname\> system-view

Sysname packet-filter default deny

【相关命令】

·**display** **packet-filter**

·**display** **packet-filter** **statistics**

·**display** **packet-filter** **verbose**

**ACL \-- ACL配置命令 \-- packet-filter default hardware-count**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[packet-filter** **default** **hardware-count**]命令用来在接口上使能报文过滤缺省动作统计功能。

**[undo** **packet-filter** **default** **hardware-count**]命令用来在接口上关闭报文过滤缺省动作统计功能。

【命令】

**[packet-filter**[ **default** { **inbound** \| **outbound** } **hardware-count**]]

**[undo**[ **packet-filter** **default** { **inbound** \| **outbound** } **hardware-count**]]

【缺省情况】

报文过滤缺省动作统计功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inbound**]：表示收到的报文。

**[outbound**]：表示发出的报文。

【使用指导】

在接口上只有应用了ACL进行报文过滤，才允许使能报文过滤缺省动作统计功能。

【举例】

\# 配置报文过滤的缺省动作为Deny，在接口GigabitEthernet1/0/1上对收到的报文应用IPv4基本ACL 2001进行过滤，并使能报文过滤缺省动作统计功能。

\<Sysname\> system-view

Sysname packet-filter default deny

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 packet-filter 2001 inbound

Sysname-GigabitEthernet1/0/1 packet-filter default inbound hardware-count

【相关命令】

·**packet-filter**

·**packet-filter** **default** **deny**

·**display** **packet-filter**

·**display** **packet-filter** **statistics**

**ACL \-- ACL配置命令 \-- packet-filter global**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[packet-filter** **global**]命令用来全局应用ACL进行报文过滤。

**[undo** **packet-filter** **global**]命令用来取消全局应用ACL进行报文过滤。

【命令】

**[packet-filter**[ [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } **global** { **inbound**  **extension**  \| **outbound** }  **hardware-count** ]]

**[undo**[ **packet-filter** [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } **global** { **inbound** \| **outbound** }]]

【缺省情况】

全局不对报文进行过滤。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：指定ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

**[global**]：表示全局（即所有物理接口）配置。

**[inbound**]：对收到的报文进行过滤。

**[extension**]：对报文过滤进行扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outbound**]：对发出的报文进行过滤。

**[hardware-count**]：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能指定ACL内所有规则的匹配统计功能，而**rule**命令中的**counting**参数则用于使能当前规则的匹配统计功能。

【使用指导】

若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 全局应用IPv4基本ACL 2001对收到的报文进行过滤，并对过滤的报文进行统计。

\<Sysname\> system-view

Sysname packet-filter 2001 global inbound hardware-count

【相关命令】

·**display** **packet-filter**

·**display** **packet-filter** **statistics**

·**display** **packet-filter** **verbose**

**ACL \-- ACL配置命令 \-- packet-filter vlan**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[packet-filter** **vlan**]命令用来在VLAN中应用ACL进行报文过滤。

**[undo** **packet-filter** **vlan**]命令用来取消在VLAN中应用ACL进行报文过滤。

【命令】

**[packet-filter**[ [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } **vlan** *vlan-list* { **inbound**  **extension**  \| **outbound** }  **hardware-count** ]]

**[undo**[ **packet-filter** [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } **vlan** *vlan-list* { **inbound** \| **outbound** }]]

【缺省情况】

在VLAN中不对报文进行过滤。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：指定ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

**[vlan**] *vlan-list*：指定VLAN。*vlan-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

**[inbound**]：对收到的报文进行过滤。

**[extension**]：对报文过滤进行扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[outbound**]：对发出的报文进行过滤。

**[hardware-count**]：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能指定ACL内所有规则的匹配统计功能，而**rule**命令中的**counting**参数则用于使能当前规则的匹配统计功能。

【使用指导】

若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 在VLAN 2中应用IPv4基本ACL 2001对收到的报文进行过滤，并对过滤的报文进行统计。

\<Sysname\> system-view

Sysname packet-filter 2001 vlan 2 inbound hardware-count

【相关命令】

·**display** **packet-filter**

·**display** **packet-filter** **statistics**

·**display** **packet-filter** **verbose**

**ACL \-- ACL配置命令 \-- reset acl counter**

------------------------------------------------------------------------

**[reset** **acl** **counter**]命令用来清除ACL的统计信息。

【命令】

**[reset**[ **acl** [ **ipv6** \| **mac** \| **user-defined** ] **counter** { *acl-number* \| **all** \| **name** *acl-name* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：清除指定编号ACL的统计信息。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[all**]：清除指定类型中全部ACL的统计信息。

**[name** *acl-name*]：清除指定名称ACL的统计信息。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 清除IPv4基本ACL 2001的统计信息。

\<Sysname\> reset acl counter 2001

【相关命令】

·**display** **acl**

**ACL \-- ACL配置命令 \-- reset packet-filter statistics**

------------------------------------------------------------------------

![说明](ACL命令.files/image001.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset** **packet-filter** **statistics**]命令用来清除ACL在报文过滤中应用的统计信息（包括累加统计信息）以及报文过滤缺省动作的统计信息。

【命令】

**[reset**[ **packet-filter** **statistics** { { **global** \| **interface** [ *interface-type* *interface-number* ] \| **vlan**  *vlan-id*  } { **inbound** \| **outbound** } [ **default** \| [ **ipv6** \| **mac** \| **user-defined** ] { *acl-number* \| **name** *acl-name* } ] \| **zone-pair security**  **source** *source-zone-name* **destination** *destination-zone-name*   **ipv6**  { *acl-number* \| **name** *acl-name* } ] }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[global**]：清除全局（即所有物理接口）统计信息。

**[interface** [ *interface-type* *interface-number* ]]：清除指定接口上的统计信息。*interface-type* *interface-number*表示接口类型和接口编号。若未指定接口类型和接口编号，将清除所有接口上的统计信息。

**[zone-pair security ** **source** *source-zone-name* **destination** *destination-zone-name* ]：清除指定接口上的统计信息。*source-zone-name*：表示安全域间实例源安全域的名称，为1～31个字符的字符串，不区分大小写。*destination-zone-name*：表示安全域间实例目的安全域的名称，为1～31个字符的字符串，不区分大小写。

**[vlan** [ *vlan-id* ]]：清除指定VLAN中的统计信息。*vlan-id*表示VLAN的编号。若未指定VLAN编号，将清除所有VLAN中的统计信息。

**[inbound**]：清除入方向上的统计信息。

**[outbound**]：清除出方向上的统计信息。

**[default**]：清除缺省动作在报文过滤中应用的统计信息。

**[ipv6**]：指定ACL类型为IPv6 ACL。

**[mac**]：指定ACL类型为二层ACL。

**[user-defined**]：指定ACL类型为用户自定义ACL。

*[acl-number*]：清除指定编号ACL在报文过滤中应用的统计信息。*acl-number*表示ACL的编号，取值范围及其代表的ACL类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：

·2000～2999：表示基本ACL。

·3000～3999：表示高级ACL。

·4000～4999：表示二层ACL。

·5000～5999：表示用户自定义ACL。

**[name** *acl-name*]：清除指定名称ACL在报文过滤中应用的统计信息。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

·若未指定**default**、*acl-number*和**name** *acl-name*参数，将清除全部ACL（若指定**ipv6**关键字，表示全部IPv6基本ACL、IPv6高级ACL；若指定**mac**关键字，表示全部二层 ACL；若指定**user-defined**关键字，则表示全部用户自定义ACL；否则，表示全部IPv4基本ACL和IPv4高级ACL）和缺省动作在报文过滤中应用的统计信息。

·清除安全域间实例统计信息时不区分方向且不支持**default**。

·若未指定**ipv6**、**mac**或**user-defined**参数，则表示IPv4 ACL。

【举例】

\# 清除VLAN 2中入方向上IPv4基本ACL 2001在报文过滤中应用的统计信息。

\<Sysname\> reset packet-filter statistics vlan 2 inbound 2001

【相关命令】

·**display** **packet-filter** **statistics**

·**display** **packet-filter** **statistics sum**

**ACL \-- ACL配置命令 \-- rule (MAC ACL view)**

------------------------------------------------------------------------

![说明](ACL命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rule**]命令用来为二层ACL创建一条规则。

**[undo** **rule**]命令用来为二层ACL删除一条规则或删除规则中的部分内容。

【命令】

**[rule**[ *rule-id*  { **deny** \| **permit** } [ **cos** *vlan-pri* \| **counting** \| **dest-mac** *dest-address* *dest-mask* \| { **lsap** *lsap-type* *lsap-type-mask* \| **type** *protocol-type* *protocol-type-mask* } \| **source-mac** *source-address* *source-mask* \| **time-range** *time-range-name* ] \*]]

**[undo**[ **rule** *rule-id* [ **counting** \| **time-range** ] \*]]

【缺省情况】

二层ACL内不存在任何规则。

【视图】

二层ACL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定二层ACL规则的编号，取值范围为0～65534。若未指定本参数，系统将按照步长从0开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为28，步长为5，那么自动分配的新编号将是30。

**[deny**]：表示拒绝符合条件的报文。

**[permit**]：表示允许符合条件的报文。

**[cos** *vlan-pri*]：指定802.1p优先级。*vlan-pri*表示802.1p优先级，可输入的形式如下：

·数字：取值范围为0～7；

·名称：**best-effort**、**background**、**spare**、**excellent-effort**、**controlled-load**、**video**、**voice**和**network-management**，依次对应于数字0～7。

**[counting**]：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能本规则的匹配统计功能，而**packet-filter**命令中的**hardware-count**参数则用于使能指定ACL内所有规则的匹配统计功能。

**[dest-mac** *dest-address* *dest-mask*]：指定目的MAC地址范围。*dest-address*表示目的MAC地址，格式为H-H-H。*dest-mask*表示目的MAC地址的掩码，格式为H-H-H。

**[lsap***lsap-type* *lsap-type-mask*]：指定LLC封装中的DSAP字段和SSAP字段。*lsap-type*表示数据帧的封装格式，为16比特的十六进制数。*lsap-type-mask*表示LSAP的类型掩码，为16比特的十六进制数，用于指定屏蔽位。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[type** *protocol-type* *protocol-type-mask*]：指定链路层协议类型。*protocol-type*表示16比特的十六进制数表征的数据帧类型，对应Ethernet_II类型和Ethernet_SNAP类型帧中的type域。*protocol-type-mask*表示类型掩码，为16比特的十六进制数，用于指定屏蔽位。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-mac** *source-address* *source-mask*]：指定源MAC地址范围。*source-address*表示源MAC地址，格式为H-H-H。*source-mask*表示源MAC地址的掩码，格式为H-H-H。

**[time-range** *time-range-name*]：指定本规则生效的时间段。*time-range-name*表示时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"ACL和QoS配置指导"中的"时间段"。

【使用指导】

·使用**rule**命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。

·新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。

·当ACL的规则匹配顺序为配置顺序时，允许修改该ACL内的任意一条已有规则；当ACL的规则匹配顺序为自动排序时，不允许修改该ACL内的已有规则，否则将提示出错。

·使用**undo** **rule**命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。

·使用**undo** **rule**命令时必须指定一个已存在规则的编号，可以使用**display** **acl** **all**命令来查看所有已存在的规则。

【举例】

\# 为二层ACL 4000创建规则如下：允许ARP报文通过，但拒绝RARP报文通过。

\<Sysname\> system-view

Sysname acl mac 4000

Sysname-acl-mac-4000 rule permit type 0806 ffff

Sysname-acl-mac-4000 rule deny type 8035 ffff

【相关命令】

·**acl**

·**display** **acl**

·**step**

·**time-range**（ACL和QoS命令参考/时间段）

**ACL \-- ACL配置命令 \-- rule (IPv4 advanced ACL view)**

------------------------------------------------------------------------

![说明](ACL命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rule**]命令用来为IPv4高级ACL创建一条规则。

**[undo** **rule**]命令用来为IPv4高级ACL删除一条规则或删除规则中的部分内容。

【命令】

**[rule** [ *rule-id*  { **deny** \| **permit** } *protocol* [ { { **ack** *ack-value* \| **fin** *fin-value* \| **psh** *psh-value* \| **rst** *rst-value* \| **syn** *syn-value* \| **urg** *urg-value* } \* \| **established** } \| **counting** \| **destination** { **object-group** *addr-group-name* \| *dest-address* *dest-wildcard* \| **any** } \| **destination-port** { **object-group** *port-group-name* \| *operator* *port1* [ *port2* ] } \| { **dscp** *dscp* \| { **precedence** *precedence* \| **tos** *tos* } \* } \| **fragment** \| **icmp-type** { *icmp-type*  *icmp-code*  \| *icmp-message* } \| **logging** \| **source** { **object-group** *addr-group-name* \| *source-address* *source-wildcard* \| **any** } \| **source-port** { **object-group** *port-group-name* \| *operator* *port1*  *port2*  } \| **time-range** *time-range-name* \| **vpn-instance** *vpn-instance-name* ] \*]]

**[undo**[ **rule** *rule-id* [ { { **ack** \| **fin** \| **psh** \| **rst** \| **syn** \| **urg** } \* \| **established** } \| **counting** \| **destination** \| **destination-port** \| { **dscp** \| { **precedence** \| **tos** } \* } \| **fragment** \| **icmp-type** \| **logging** \| **source** \| **source-port** \| **time-range** \| **vpn-instance** ] \*]]

【缺省情况】

IPv4高级ACL内不存在任何规则。

【视图】

IPv4高级ACL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定IPv4高级ACL规则的编号，取值范围为0～65534。若未指定本参数，系统将按照步长从0开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为28，步长为5，那么自动分配的新编号将是30。

**[deny**]：表示拒绝符合条件的报文。

**[permit**]：表示允许符合条件的报文。

*[protocol*]：表示IPv4承载的协议类型，可输入的形式如下：

·数字：取值范围为0～255；

·名称（括号内为对应的数字）：可选取**gre**（47）、**icmp**（1）、**igmp**（2）、**ip**、**ipinip**（4）、**ospf**（89）、**tcp**（6）或**udp**（17）。

*[protocol*]之后可配置如[表]1-9(?-233529961#_Ref295383134)所示的规则信息参数。

表1-9 规则信息参数

参数

类别

作用

说明

**[source**[ { **object-group** *addr-group-name* \| *source-address* *source-wildcard* \| **any** }]]

源地址信息

指定ACL规则的源地址信息

*[addr-group-name*]：源地址对象组的名称

*[source-address*]：源IP地址

*[source-wildcard*]：源IP地址的通配符掩码（为0表示主机地址）

**[any**]：任意源IP地址

**[destination**[ { **object-group** *addr-group-name* \| *dest-address* *dest-wildcard* \| **any** }]]

目的地址信息

指定ACL规则的目的地址信息

*[addr-group-name*]：目的地址对象组的名称

*[dest-address*]：目的IP地址

*[dest-wildcard*]：目的IP地址的通配符掩码（为0表示主机地址）

**[any**]：任意目的IP地址

**[counting**]

统计

使能规则匹配统计功能，缺省为关闭

本参数用于使能本规则的匹配统计功能，而**packet-filter**命令中的**hardware-count**参数则用于使能指定ACL内所有规则的匹配统计功能

**[precedence** *precedence*]

报文优先级

IP优先级

*[precedence*]用数字表示时，取值范围为0～7；用文字表示时，分别对应**routine**、**priority**、**immediate**、**flash**、**flash-override**、**critical**、**internet**、**network**

**[tos** *tos*]

报文优先级

ToS优先级

*[tos*]用数字表示时，取值范围为0～15；用文字表示时，可以选取**max-reliability**（2）、**max-throughput**（4）、**min-delay**（8）、**min-monetary-cost**（1）、**normal**（0）

**[dscp** *dscp*]

报文优先级

DSCP优先级

*[dscp*]用数字表示时，取值范围为0～63；用文字表示时，可以选取**af11**（10）、**af12**（12）、**af13**（14）、**af21**（18）、**af22**（20）、**af23**（22）、**af31**（26）、**af32**（28）、**af33**（30）、**af41**（34）、**af42**（36）、**af43**（38）、**cs1**（8）、**cs2**（16）、**cs3**（24）、**cs4**（32）、**cs5**（40）、**cs6**（48）、**cs7**（56）、**default**（0）、**ef**（46）

**[fragment**]

分片信息

仅对分片报文的非首个分片有效，而对非分片报文和分片报文的首个分片无效

若未指定该参数，则表示该规则对所有报文（包括非分片报文和分片报文的每个分片）均有效

**[logging**]

日志操作

对符合条件的报文可记录日志信息

该功能需要使用该ACL的模块支持日志记录功能，例如报文过滤

**[time-range** *time-range-name*]

时间段

指定本规则生效的时间段

*[time-range-name*]：时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"ACL和QoS配置指导"中的"时间段"

**[vpn-instance** *vpn-instance-name*]

VPN实例

对指定VPN实例中的报文有效

*[vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写

若未指定本参数，表示该规则仅对非VPN报文有效

当*protocol*为**tcp**（6）或**udp**（17）时，用户还可配置如[表]1-10(?-233529961#_Ref259115846)所示的规则信息参数。

表1-10 TCP/UDP特有的规则信息参数

参数

类别

作用

说明

**[source-port**]*[operator* *port1* [ *port2*  }]

源端口]

定义TCP/UDP报文的源端口信息

*[port-group-name*]：端口对象组的名称

*[operator*]为操作符，取值可以为**lt**（小于）、**gt**（大于）、**eq**（等于）、**neq**（不等于）或者**range**（在范围内，包括边界值）。只有操作符**range**需要两个端口号做操作数，其它的只需要一个端口号做操作数

*[port1*]、*port2*：TCP或UDP的端口号，用数字表示时，取值范围为0～65535；用文字表示时，TCP端口号可以选取**chargen**（19）、**bgp**（179）、**cmd**（514）、**daytime**（13）、**discard**（9）、**dns**（53）、**domain**（53）、**echo**（7）、**exec**（512）、**finger**（79）、**ftp**（21）、**ftp-data**（20）、**gopher**（70）、**hostname**（101）、**irc**（194）、**klogin**（543）、**kshell**（544）、**login**（513）、**lpd**（515）、**nntp**（119）、**pop2**（109）、**pop3**（110）、**smtp**（25）、**sunrpc**（111）、**tacacs**（49）、**talk**（517）、**telnet**（23）、**time**（37）、**uucp**（540）、**whois**（43）、**www**（80）；UDP端口号可以选取**biff**（512）、**bootpc**（68）、**bootps**（67）、**discard**（9）、**dns**（53）、**dnsix**（90）、**echo**（7）、**mobilip-ag**（434）、**mobilip-mn**（435）、**nameserver**（42）、**netbios-dgm**（138）、**netbios-ns**（137）、**netbios-ssn**（139）、**ntp**（123）、**rip**（520）、**snmp**（161）、**snmptrap**（162）、**sunrpc**（111）、**syslog**（514）、**tacacs-ds**（65）、**talk**（517）、**tftp**（69）、**time**（37）、**who**（513）、**xdmcp**（177）

**[destination-port**]*[operator* *port1* [ *port2*  }]

目的端口]

定义TCP/UDP报文的目的端口信息

[[{ **ack** *ack-value* \| **fin** *fin-value* \| **psh** *psh-value* \| **rst** *rst-value* \| **syn** *syn-value* \| **urg** *urg-value* } \*]]

TCP报文标识

定义对携带不同标志位（包括ACK、FIN、PSH、RST、SYN和URG六种）的TCP报文的处理规则

TCP协议特有的参数。表示匹配携带不同标志位的TCP报文，各*value*的取值可为0或1（0表示不携带此标志位，1表示携带此标志位）

对于一条规则中各标志位的配置组合，不同产品的处理方式（"与"或"或"）不同，请以设备的实际情况为准。譬如：当配置为**ack** 0 **psh** 1时，有些产品将匹配不携带ACK标志位且携带PSH标志位的TCP报文，而有些产品则匹配不携带ACK或携带PSH标志位的TCP报文

**[established**]

TCP连接建立标识

定义对TCP连接报文的处理规则

TCP协议特有的参数。对于路由器，表示匹配携带ACK或RST标志位的TCP连接报文；对于交换机，请以各产品实际情况为准

当*protocol*为**icmp**（1）时，用户还可配置如[表]1-11(?-233529961#_Ref295383166)所示的规则信息参数。

表1-11 ICMP特有的规则信息参数

参数

类别

作用

说明

**[icmp-type**[ { *icmp-type* *icmp-code* \| *icmp-message* }]]

ICMP报文的消息类型和消息码信息

指定本规则中ICMP报文的消息类型和消息码信息

*[icmp-type*]：ICMP消息类型，取值范围为0～255

*[icmp-code*]：ICMP消息码，取值范围为0～255

*[icmp-message*]：ICMP消息名称。可以输入的ICMP消息名称，及其与消息类型和消息码的对应关系如[表]1-12(?-233529961#_Ref144979012)所示

表1-12 ICMP消息名称与消息类型和消息码的对应关系

ICMP消息名称

ICMP消息类型

ICMP消息码

echo

8

0

echo-reply

0

0

fragmentneed-DFset

3

4

host-redirect

5

1

host-tos-redirect

5

3

host-unreachable

3

1

information-reply

16

0

information-request

15

0

net-redirect

5

0

net-tos-redirect

5

2

net-unreachable

3

0

parameter-problem

12

0

port-unreachable

3

3

protocol-unreachable

3

2

reassembly-timeout

11

1

source-quench

4

0

source-route-failed

3

5

timestamp-reply

14

0

timestamp-request

13

0

ttl-exceeded

11

0

【使用指导】

·使用**rule**命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。

·新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。

·新创建或修改的规则若指定对象组，则该对象组必须存在，否则将提示出错，并导致该操作失败。

·当ACL的规则匹配顺序为配置顺序时，允许修改该ACL内的任意一条已有规则；当ACL的规则匹配顺序为自动排序时，不允许修改该ACL内的已有规则，否则将提示出错。

·使用**undo** **rule**命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。

·使用**undo** **rule**命令时必须指定一个已存在规则的编号，可以使用**display** **acl** **all**命令来查看所有已存在的规则。

【举例】

\# 为IPv4高级ACL 3000创建规则如下：允许129.9.0.0/16网段内的主机与202.38.160.0/24网段内主机的WWW端口（端口号为80）建立连接。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule permit tcp source 129.9.0.0 0.0.255.255 destination 202.38.160.0 0.0.0.255 destination-port eq 80

\# 为IPv4高级ACL 3001创建规则如下：允许IP报文通过，但拒绝发往192.168.1.0/24网段的ICMP报文通过。

\<Sysname\> system-view

Sysname acl advanced 3001

Sysname-acl-ipv4-adv-3001 rule deny icmp destination 192.168.1.0 0.0.0.255

Sysname-acl-ipv4-adv-3001 rule permit ip

\# 为IPv4高级ACL 3002创建规则如下：在出、入双方向上都允许建立FTP连接并传输FTP数据。

\<Sysname\> system-view

Sysname acl advanced 3002

Sysname-acl-ipv4-adv-3002 rule permit tcp source-port eq ftp

Sysname-acl-ipv4-adv-3002 rule permit tcp source-port eq ftp-data

Sysname-acl-ipv4-adv-3002 rule permit tcp destination-port eq ftp

Sysname-acl-ipv4-adv-3002 rule permit tcp destination-port eq ftp-data

\# 为IPv4高级ACL 3003创建规则如下：在出、入双方向上都允许SNMP报文和SNMP Trap报文通过。

\<Sysname\> system-view

Sysname acl advanced 3003

Sysname-acl-ipv4-adv-3003 rule permit udp source-port eq snmp

Sysname-acl-ipv4-adv-3003 rule permit udp source-port eq snmptrap

Sysname-acl-ipv4-adv-3003 rule permit udp destination-port eq snmp

Sysname-acl-ipv4-adv-3003 rule permit udp destination-port eq snmptrap

【相关命令】

·**acl**

·**acl** **logging** **interval**

·**display** **acl**

·**step**

·**time-range**（ACL和QoS命令参考/时间段）

**ACL \-- ACL配置命令 \-- rule (IPv4 basic ACL view)**

------------------------------------------------------------------------

![说明](ACL命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rule**]命令用来为IPv4基本ACL创建一条规则。

**[undo** **rule**]命令用来为IPv4基本ACL删除一条规则或删除规则中的部分内容。

【命令】

**[rule** [ *rule-id*  { **deny** \| **permit** } [ **counting** \| **fragment** \| **logging** \| **source** { **object-group** *addr-group-name* \| *source-address* *source-wildcard* \| **any** } \| **time-range** *time-range-name* \| **vpn-instance** *vpn-instance-name* ] \*]]

**[undo**[ **rule** *rule-id* [ **counting** \| **fragment** \| **logging** \| **source** \| **time-range** \| **vpn-instance** ] \*]]

【缺省情况】

IPv4基本ACL内不存在任何规则。

【视图】

IPv4基本ACL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定IPv4基本ACL规则的编号，取值范围为0～65534。若未指定本参数，系统将按照步长从0开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为28，步长为5，那么自动分配的新编号将是30。

**[deny**]：表示拒绝符合条件的报文。

**[permit**]：表示允许符合条件的报文。

**[counting**]：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能本规则的匹配统计功能，而**packet-filter**命令中的**hardware-count**参数则用于使能指定ACL内所有规则的匹配统计功能。

**[fragment**]：表示仅对非首片分片报文有效，而对非分片报文和首片分片报文无效。若未指定本参数，表示该规则对非分片报文和分片报文均有效。

**[logging**]：表示对符合条件的报文可记录日志信息。该功能需要使用该ACL的模块支持日志记录功能，例如报文过滤。

**[source**[ { **object-group** *addr-group-name* \| *source-address* *source-wildcard* \| **any** }]]：指定规则的源IP地址信息。*addr-group-name*表示源IP地址对象组的名称，*source-address*表示报文的源IP地址，*source-wildcard*表示源IP地址的通配符掩码（为0表示主机地址），**any**表示任意源IP地址。

**[time-range** *time-range-name*]：指定本规则生效的时间段。*time-range-name*表示时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"ACL和QoS配置指导"中的"时间段"。

**[vpn-instance** *vpn-instance-name*]：表示对指定VPN实例中的报文有效。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若未指定本参数，表示该规则仅对非VPN报文有效。

【使用指导】

·使用**rule**命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。

·新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。

·新创建或修改的规则若指定对象组，则该对象组必须存在，否则将提示出错，并导致该操作失败。

·当ACL的规则匹配顺序为配置顺序时，允许修改该ACL内的任意一条已有规则；当ACL的规则匹配顺序为自动排序时，不允许修改该ACL内的已有规则，否则将提示出错。

·使用**undo** **rule**命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。

·使用**undo** **rule**命令时必须指定一个已存在规则的编号，可以使用**display** **acl** **all**命令来查看所有已存在的规则。

【举例】

\# 为IPv4基本ACL 2000创建规则如下：仅允许来自10.0.0.0/8、172.17.0.0/16和192.168.1.0/24网段的报文通过，而拒绝来自所有其它网段的报文通过。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 10.0.0.0 0.255.255.255

Sysname-acl-ipv4-basic-2000 rule permit source 172.17.0.0 0.0.255.255

Sysname-acl-ipv4-basic-2000 rule permit source 192.168.1.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 rule deny source any

【相关命令】

·**acl**

·**acl** **logging** **interval**

·**display** **acl**

·**step**

·**time-range**（ACL和QoS命令参考/时间段）

**ACL \-- ACL配置命令 \-- rule (IPv6 advanced ACL view)**

------------------------------------------------------------------------

![说明](ACL命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rule**]命令用来为IPv6高级ACL创建一条规则。

**[undo** **rule**]命令用来为IPv6高级ACL删除一条规则或删除规则中的部分内容。

【命令】

**[rule** [ *rule-id*  { **deny** \| **permit** } *protocol* [ { { **ack** *ack-value* \| **fin** *fin-value* \| **psh** *psh-value* \| **rst** *rst-value* \| **syn** *syn-value* \| **urg** *urg-value* } \* \| **established** } \| **counting** \| **destination** { **object-group** *addr-group-name* \|*dest-address* *dest-prefix* \| *dest-address/dest-prefix* \| **any** } \| **destination-port** { **object-group** *port-group-name* \| *operator* *port1* [ *port2* ] } \| **dscp** *dscp* \| **flow-label** *flow-label-value* \| **fragment** \| **icmp6-type** { *icmp6-type* *icmp6-code* \| *icmp6-message* } \| **logging** \| **routing**  **type** *routing-type*  \| **hop-by-hop**  **type** *hop-type*  \| **source** { **object-group** *addr-group-name* \| *source-address* *source-prefix* \| *source-address/source-prefix* \| **any** } \| **source-port** { **object-group** *port-group-name* \| *operator* *port1*  *port2*  } \| **time-range** *time-range-name* \| **vpn-instance** *vpn-instance-name* ] \*]]

**[undo**[ **rule** *rule-id* [ { { **ack** \| **fin** \| **psh** \| **rst** \| **syn** \| **urg** } \* \| **established** } \| **counting** \| **destination** \| **destination-port** \| **dscp** \| **flow-label** \| **fragment** \| **icmp6-type** \| **logging** \| **routing** \| **hop-by-hop** \| **source** \| **source-port** \| **time-range** \| **vpn-instance** ] \*]]

【缺省情况】

IPv6高级ACL内不存在任何规则。

【视图】

IPv6高级ACL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定IPv6高级ACL规则的编号，取值范围为0～65534。若未指定本参数，系统将按照步长从0开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为28，步长为5，那么自动分配的新编号将是30。

**[deny**]：表示拒绝符合条件的报文。

**[permit**]：表示允许符合条件的报文。

*[protocol*]：表示IPv6承载的协议类型，可输入的形式如下：

·数字：取值范围为0～255；

·名称（括号内为对应的数字）：可选取**gre**（47）、**icmpv6**（58）、**ipv6**、**ipv6-ah**（51）、**ipv6-esp**（50）、**ospf**（89）、**tcp**（6）或**udp**（17）。

*[protocol*]之后可配置如表 1-13(?872051014#_Ref259116285)所示的规则信息参数。

表1-13 规则信息参数

参数

类别

作用

说明

**[source**[ { **object-group** *addr-group-name* \| *source-address* *source-prefix* \| *source-address/source-prefix* \| **any** }]]

源IPv6地址

指定ACL规则的源IPv6地址信息

*[addr-group-name*]：源地址对象组的名称

*[source-address*]：源IPv6地址

*[source-prefix*]：源IPv6地址的前缀长度，取值范围1～128

**[any**]：任意源IPv6地址

**[destination**[ { **object-group** addr-group-name \| *dest-address* *dest-prefix* \| *dest-address/dest-prefix* \| **any** }]]

目的IPv6地址

指定ACL规则的目的IPv6地址信息

*[addr-group-name*]：目的地址对象组的名称

*[dest-address*]：目的IPv6地址

*[dest*-*prefix*]：目的IPv6地址的前缀长度，取值范围1～128

**[any**]：任意目的IPv6地址

**[counting**]

统计

使能规则匹配统计功能，缺省为关闭

本参数用于使能本规则的匹配统计功能，而**packet-filter ipv6**命令中的**hardware-count**参数则用于使能指定ACL内所有规则的匹配统计功能

**[dscp** *dscp*]

报文优先级

DSCP优先级

*[dscp*]：用数字表示时，取值范围为0～63；用名称表示时，可选取**af11**（10）、**af12**（12）、**af13**（14）、**af21**（18）、**af22**（20）、**af23**（22）、**af31**（26）、**af32**（28）、**af33**（30）、**af41**（34）、**af42**（36）、**af43**（38）、**cs1**（8）、**cs2**（16）、**cs3**（24）、**cs4**（32）、**cs5**（40）、**cs6**（48）、**cs7**（56）、**default**（0）或**ef**（46）

**[flow-label** *flow-label-value*]

流标签字段

指定IPv6基本报文头中流标签字段的值

*[flow-label-value*]：流标签字段的值，取值范围为0～1048575

**[fragment**]

报文分片

仅对分片报文的非首个分片有效，而对非分片报文和分片报文的首个分片无效

若未指定本参数，表示该规则对所有报文（包括非分片报文和分片报文的每个分片）均有效

**[logging**]

日志操作

对符合条件的报文可记录日志信息

该功能需要使用该ACL的模块支持日志记录功能，例如报文过滤

**[routing** [ **type** *routing-type* ]]

路由头

指定路由头的类型

*[routing-type*]：路由头类型的值，取值范围为0～255

若指定了**type** *routing-type*参数，表示仅对指定类型的路由头有效；否则，表示对IPv6所有类型的路由头都有效

**[hop-by-hop** [ **type** *hop-type* ]]

逐跳头

指定逐跳头的类型

*[hop-type*]：逐跳头类型的值，取值范围为0～255

若指定了**type** *hop-type*参数，表示仅对指定类型的逐跳头有效；否则，表示对IPv6所有类型的逐跳头都有效

**[time-range** *time-range-name*]

时间段

指定本规则生效的时间段

*[time-range-name*]：时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"ACL和QoS配置指导"中的"时间段"

**[vpn-instance** *vpn-instance-name*]

VPN实例

对指定VPN实例中的报文有效

*[vpn-instance-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写

若未指定本参数，表示该规则仅对非VPN报文有效

当*protocol*为**tcp**（6）或**udp**（17）时，用户还可配置如表 1-14(?872051014#_Ref259116335)所示的规则信息参数。

表1-14 TCP/UDP特有的规则信息参数

参数

类别

作用

说明

**[source-port**]*[operator* *port1* [ *port2*  }]

源端口]

定义TCP/UDP报文的源端口信息

*[port-group-name*]：端口对象组的名称

*[operator*]：操作符，取值可以为**lt**（小于）、**gt**（大于）、**eq**（等于）、**neq**（不等于）或者**range**（在范围内，包括边界值）。只有**range**操作符需要两个端口号做操作数，其它操作符只需要一个端口号做操作数

*[port1*/*port2*]：TCP或UDP的端口号，用数字表示时，取值范围为0～65535；用名称表示时，TCP端口号可选取**chargen**（19）、**bgp**（179）、**cmd**（514）、**daytime**（13）、**discard**（9）、**dns**（53）、**domain**（53）、**echo**（7）、**exec**（512）、**finger**（79）、**ftp**（21）、**ftp-data**（20）、**gopher**（70）、**hostname**（101）、**irc**（194）、**klogin**（543）、**kshell**（544）、**login**（513）、**lpd**（515）、**nntp**（119）、**pop2**（109）、**pop3**（110）、**smtp**（25）、**sunrpc**（111）、**tacacs**（49）、**talk**（517）、**telnet**（23）、**time**（37）、**uucp**（540）、**whois**（43）或**www**（80）；UDP端口号可选取**biff**（512）、**bootpc**（68）、**bootps**（67）、**discard**（9）、**dns**（53）、**dnsix**（90）、**echo**（7）、**mobilip-ag**（434）、**mobilip-mn**（435）、**nameserver**（42）、**netbios-dgm**（138）、**netbios-ns**（137）、**netbios-ssn**（139）、**ntp**（123）、**rip**（520）、**snmp**（161）、**snmptrap**（162）、**sunrpc**（111）、**syslog**（514）、**tacacs-ds**（65）、**talk**（517）、**tftp**（69）、**time**（37）、**who**（513）或**xdmcp**（177）

**[destination-port**]*[operator* *port1* [ *port2*  }]

目的端口]

定义TCP/UDP报文的目的端口信息

[[{ **ack** *ack-value* \| **fin** *fin-value* \| **psh** *psh-value* \| **rst** *rst-value* \| **syn** *syn-value* \| **urg** *urg-value* } \*]]

TCP报文标识

定义对携带不同标志位（包括ACK、FIN、PSH、RST、SYN和URG六种）的TCP报文的处理规则

TCP协议特有的参数。表示匹配携带不同标志位的TCP报文，各*value*的取值可为0或1（0表示不携带此标志位，1表示携带此标志位）

对于一条规则中各标志位的配置组合，不同产品的处理方式（"与"或"或"）不同，请以设备的实际情况为准。譬如：当配置为**ack** 0 **psh** 1时，有些产品将匹配不携带ACK标志位且携带PSH标志位的TCP报文，而有些产品则匹配不携带ACK或携带PSH标志位的TCP报文

**[established**]

TCP连接建立标识

定义对TCP连接报文的处理规则

TCP协议特有的参数。对于路由器，表示匹配携带ACK或RST标志位的TCP连接报文；对于交换机，请以各产品实际情况为准

当*protocol*为**icmpv6**（58）时，用户还可配置如表 1-15(?872051014#_Ref259116368)所示的规则信息参数。

表1-15 ICMPv6特有的规则信息参数

参数

类别

作用

说明

**[icmp6-type**[ { *icmp6-type* *icmp6-code* \| *icmp6-message* }]]

ICMPv6报文的消息类型和消息码

指定本规则中ICMPv6报文的消息类型和消息码信息

*[icmp6-type*]：ICMPv6消息类型，取值范围为0～255

*[icmp6-code*]：ICMPv6消息码，取值范围为0～255

*[icmp6-message*]：ICMPv6消息名称。可以输入的ICMPv6消息名称，及其与消息类型和消息码的对应关系如表 1-16(?872051014#_Ref139034904)所示

表1-16 ICMPv6消息名称与消息类型和消息码的对应关系

ICMPv6消息名称

ICMPv6消息类型

ICMPv6消息码

echo-reply

129

0

echo-request

128

0

err-Header-field

4

0

frag-time-exceeded

3

1

hop-limit-exceeded

3

0

host-admin-prohib

1

1

host-unreachable

1

3

neighbor-advertisement

136

0

neighbor-solicitation

135

0

network-unreachable

1

0

packet-too-big

2

0

port-unreachable

1

4

redirect

137

0

router-advertisement

134

0

router-solicitation

133

0

unknown-ipv6-opt

4

2

unknown-next-hdr

4

1

****

【使用指导】

·使用**rule**命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。

·新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。

·当ACL的规则匹配顺序为配置顺序时，允许修改该ACL内的任意一条已有规则；当ACL的规则匹配顺序为自动排序时，不允许修改该ACL内的已有规则，否则将提示出错。

·新创建或修改的规则若指定对象组，则该对象组必须存在，否则将提示出错，并导致该操作失败。

·使用**undo** **rule**命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。

·使用**undo** **rule**命令时必须指定一个已存在规则的编号，可以使用**display** **acl** **ipv6** **all**命令来查看所有已存在的规则。

【举例】

\# 为IPv6高级ACL 3000创建规则如下：允许2030:5060::/64网段内的主机与FE80:5060::/96网段内主机的WWW端口（端口号为80）建立连接。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3000

Sysname-acl-ipv6-adv-3000 rule permit tcp source 2030:5060::/64 destination fe80:5060::/96 destination-port eq 80

\# 为IPv6高级ACL 3001创建规则如下：允许IPv6报文通过，但拒绝发往FE80:5060:1001::/48网段的ICMPv6报文通过。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3001

Sysname-acl-ipv6-adv-3001 rule deny icmpv6 destination fe80:5060:1001:: 48

Sysname-acl-ipv6-adv-3001 rule permit ipv6

\# 为IPv6高级ACL 3002创建规则如下：在出、入双方向上都允许建立FTP连接并传输FTP数据。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3002

Sysname-acl-ipv6-adv-3002 rule permit tcp source-port eq ftp

Sysname-acl-ipv6-adv-3002 rule permit tcp source-port eq ftp-data

Sysname-acl-ipv6-adv-3002 rule permit tcp destination-port eq ftp

Sysname-acl-ipv6-adv-3002 rule permit tcp destination-port eq ftp-data

\# 为IPv6高级ACL 3003创建规则如下：在出、入双方向上都允许SNMP报文和SNMP Trap报文通过。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3003

Sysname-acl-ipv6-adv-3003 rule permit udp source-port eq snmp

Sysname-acl-ipv6-adv-3003 rule permit udp source-port eq snmptrap

Sysname-acl-ipv6-adv-3003 rule permit udp destination-port eq snmp

Sysname-acl-ipv6-adv-3003 rule permit udp destination-port eq snmptrap

\# 为IPv6高级ACL 3004创建规则如下：在含有逐跳头的报文中，只允许转发含有MLD选项（Type＝5）的报文，丢弃其他报文。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3004

Sysname-acl-ipv6-adv-3004 rule permit ipv6 hop-by-hop type 5

Sysname-acl-ipv6-adv-3004 rule deny ipv6 hop-by-hop

【相关命令】

·**acl**

·**acl** **logging** **interval**

·**display** **acl**

·**step**

·**time-range**（ACL和QoS命令参考/时间段）

**ACL \-- ACL配置命令 \-- rule (IPv6 basic ACL view)**

------------------------------------------------------------------------

![说明](ACL命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rule**]命令用来为IPv6基本ACL创建一条规则。

**[undo** **rule**]命令用来为IPv6基本ACL删除一条规则或删除规则中的部分内容。

【命令】

**[rule** [ *rule-id*  { **deny** \| **permit** } [ **counting** \| **fragment** \| **logging** \| **routing** [ **type** *routing-type* ] \| **source** { **object-group** *addr-group-name* \| *source-address* *source-prefix* \| *source-address*/*source-prefix* \| **any** } \| **time-range** *time-range-name* \| **vpn-instance** *vpn-instance-name* ] \*]]

**[undo**[ **rule** *rule-id* [ **counting** \| **fragment** \| **logging** \| **routing** \| **source** \| **time-range** \| **vpn-instance** ] \*]]

【缺省情况】

IPv6基本ACL内不存在任何规则。

【视图】

IPv6基本ACL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定IPv6基本ACL规则的编号，取值范围为0～65534。若未指定本参数，系统将按照步长从0开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为28，步长为5，那么自动分配的新编号将是30。

**[deny**]：表示拒绝符合条件的报文。

**[permit**]：表示允许符合条件的报文。

**[counting**]：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能本规则的匹配统计功能，而**packet-filter ipv6**命令中的**hardware-count**参数则用于使能指定ACL内所有规则的匹配统计功能。

**[fragment**]：表示仅对非首片分片报文有效，而对非分片报文和首片分片报文无效。若未指定本参数，表示该规则对非分片报文和分片报文均有效。

**[logging**]：表示对符合条件的报文可记录日志信息。该功能需要使用该ACL的模块支持日志记录功能，例如报文过滤。

**[routing** [ **type** *routing-type* ]]：表示对所有或指定类型的路由头有效，*routing-type*表示路由头类型的值，取值范围为0～255。若指定了**type** *routing-type*参数，表示仅对指定类型的路由头有效；否则，表示对所有类型的路由头都有效。

**[source**[ { **object-group** *addr-group-name* \| *source-address* *source-prefix* \| *source-address*/*source-prefix* \| **any** }]]：指定规则的源IPv6地址信息。*addr-group-name*表示源IP地址对象组的名称，*source-address*表示报文的源IPv6地址，*source-prefix*表示源IPv6地址的前缀长度，取值范围为1～128，**any**表示任意源IPv6地址。

**[time-range** *time-range-name*]：指定本规则生效的时间段。*time-range-name*表示时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"ACL和QoS配置指导"中的"时间段"。

**[vpn-instance** *vpn-instance-name*]：表示对指定VPN实例中的报文有效。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。若未指定本参数，表示该规则仅对非VPN报文有效。

【使用指导】

·使用**rule**命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。

·新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。

·新创建或修改的规则若指定对象组，则该对象组必须存在，否则将提示出错，并导致该操作失败。

·当ACL的规则匹配顺序为配置顺序时，允许修改该ACL内的任意一条已有规则；当ACL的规则匹配顺序为自动排序时，不允许修改该ACL内的已有规则，否则将提示出错。

·使用**undo** **rule**命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。

·使用**undo** **rule**命令时必须指定一个已存在规则的编号，可以使用**display** **acl** **ipv6** **all**命令来查看所有已存在的规则。

【举例】

\# 为IPv6基本ACL 2000创建规则如下：仅允许来自1001::/16、3124:1123::/32和FE80:5060:1001::/48网段的报文通过，而拒绝来自所有其它网段的报文通过。

\<Sysname\> system-view

Sysname acl ipv6 basic 2000

Sysname-acl-ipv6-basic-2000 rule permit source 1001:: 16

Sysname-acl-ipv6-basic-2000 rule permit source 3124:1123:: 32

Sysname-acl-ipv6-basic-2000 rule permit source fe80:5060:1001:: 48

Sysname-acl-ipv6-basic-2000 rule deny source any

【相关命令】

·**acl**

·**acl** **logging** **interval**

·**display** **acl**

·**step**

·**time-range**（ACL和QoS命令参考/时间段）

**ACL \-- ACL配置命令 \-- rule (user-defined ACL view)**

------------------------------------------------------------------------

![说明](ACL命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rule**]命令用来为用户自定义ACL创建一条规则。

**[undo** **rule**]命令用来为用户自定义ACL删除一条规则。

【命令】

**[rule** [ *rule-id*  { **deny** \| **permit** } [ { { **ipv4** \| **ipv6** \| **l2** \| **l4** } *rule-string* *rule-mask* *offset* }&\<1-8\>   **counting** \| **time-range** *time-range-name* ] \*]]

**[undo** **rule** *rule-id*]

【缺省情况】

用户自定义ACL内不存在任何规则。

【视图】

用户自定义ACL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定用户自定义ACL规则的编号，取值范围为0～65534。若未指定本参数，系统将按照步长从0开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为28，步长为5，那么自动分配的新编号将是30。

**[deny**]：表示拒绝符合条件的报文。

**[permit**]：表示允许符合条件的报文。

**[ipv4**]：表示从IPv4报文头开始偏移（具体的偏移开始位与设备的型号有关，请以设备的实际情况为准）。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6**]：表示从IPv6报文头开始偏移（具体的偏移开始位与设备的型号有关，请以设备的实际情况为准）。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[l2**]：表示从L2帧头开始偏移（具体的偏移开始位与设备的型号有关，请以设备的实际情况为准）。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[l4**]：表示从L4报文头开始偏移（具体的偏移开始位与设备的型号有关，请以设备的实际情况为准）。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[rule-string*]：指定用户自定义的规则字符串，必须是16进制数组成，字符长度必须是偶数。

*[rule-mask*]：指定规则字符串的掩码，用于和报文作"与"操作，必须是16进制数组成，字符长度必须是偶数，且必须与*rule-string*的长度相同。

*[offset*]：指定偏移量，它以用户指定的报文头部为基准，指定从第几个字节开始进行比较。

&\<1-8\>：表示前面的参数最多可以输入8次。

**[counting**]：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能本规则的匹配统计功能，而**packet-filter**命令中的**hardware-count**参数则用于使能指定ACL内所有规则的匹配统计功能。

**[time-range** *time-range-name*]：指定本规则生效的时间段。*time-range-name*表示时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"ACL和QoS配置指导"中的"时间段"。

【使用指导】

·使用**rule**命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。

·新创建的规则不能与已有规则的内容完全相同，否则将提示出错，并导致创建失败。

·使用**undo** **rule**命令时必须指定一个已存在规则的编号，可以使用**display** **acl** **all**命令来查看所有已存在的规则。

【举例】

\# 为用户自定义ACL 5005创建规则如下：允许从L2帧头开始算起第13、14两字节的内容为0x0806的报文（即ARP报文）通过。

\<Sysname\> system-view

Sysname acl user-defined 5005

Sysname-acl-user-5005 rule permit l2 0806 ffff 12

【相关命令】

·**acl**

·**display** **acl**

·**time-range**（ACL和QoS命令参考/时间段）

**ACL \-- ACL配置命令 \-- rule comment**

------------------------------------------------------------------------

**[rule** **comment**]命令用来为指定规则配置描述信息。

**[undo** **rule** **comment**]命令用来删除指定规则的描述信息。

【命令】

**[rule** *rule-id* **comment** *text*]

**[undo** **rule** *rule-id* **comment**]

【缺省情况】

规则没有任何描述信息。

【视图】

IPv4基本ACL视图/IPv4高级ACL视图/IPv6基本ACL视图/IPv6高级ACL视图/二层ACL视图/用户自定义ACL视图

![说明](ACL命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定规则的编号，该规则必须存在。取值范围为0～65534。

*[text*]：表示规则的描述信息，为1～127个字符的字符串，区分大小写。

【使用指导】

使用**rule** **comment**命令时，如果指定的规则没有描述信息，则为其添加描述信息，否则修改其描述信息。

【举例】

\# 为IPv4基本ACL 2000配置规则0，并为该规则配置描述信息。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule 0 deny source 1.1.1.1 0

Sysname-acl-ipv4-basic-2000 rule 0 comment This rule is used on GigabitEthernet 1/0/1.

【相关命令】

·**display** **acl**

**ACL \-- ACL配置命令 \-- step**

------------------------------------------------------------------------

**[step**]命令用来配置规则编号的步长。

**[undo** **step**]命令用来恢复缺省情况。

【命令】

**[step** *step-value*]

**[undo** **step**]

【缺省情况】

规则编号的步长为5。

【视图】

IPv4基本ACL视图/IPv4高级ACL视图/IPv6基本ACL视图/IPv6高级ACL视图/二层ACL视图

![说明](ACL命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[step-value*]：表示规则编号的步长值，取值范围为1～20。

【举例】

\# 将IPv4基本ACL 2000的规则编号的步长配置为2。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 step 2

【相关命令】

·**display** **acl**

