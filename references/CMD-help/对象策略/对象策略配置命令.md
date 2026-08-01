<!-- CMD-INDEX
  accelerate                          | 对象策略视图           | L20
  description                         | 对象策略视图           | L70
  display object-policy accelerate    | 任意视图             | L122
  display object-policy ip            | 任意视图             | L212
  display object-policy ipv6          | 任意视图             | L286
  display object-policy statistics zone-pair security | 任意视图             | L362
  display object-policy zone-pair security | 任意视图             | L446
  move rule                           | 对象策略视图           | L506
  object-policy apply ip              | 安全域间实例视图         | L550
  object-policy apply ipv6            | 安全域间实例视图         | L610
  object-policy ip                    | 系统视图             | L670
  object-policy ipv6                  | 系统视图             | L726
  reset object-policy statistics      | 用户视图             | L782
  rule comment                        | 对象策略视图           | L824
  rule(ipv4 object-policy view)       | IPv4对象策略视图       | L882
  rule(ipv6 object-policy view)       | IPv6对象策略视图       | L966
-->

**对象策略 \-- 对象策略配置命令 \-- accelerate**

------------------------------------------------------------------------

![说明](对象策略命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[accelerate**]命令用来开启对象策略加速功能。

**[undo accelerate**]命令用来关闭对象策略加速功能。

【命令】

**[accelerate**]

**[undo accelerate **]

【缺省情况】

对象策略的加速功能处于关闭状态。

【视图】

对象策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

【举例】

\# 关闭对象策略加速功能。

\<Sysname\> system-view

Sysname object-policy ip a

Sysname-object-policy-ip-a undo accelerate

【相关命令】

·**[display object-policy accelerate**](#_display_object-policy_accelerate)

**对象策略 \-- 对象策略配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置对象策略的描述信息。

**[undo** **description**]命令用来删除对象策略的描述信息。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

对象策略没有任何描述信息。

【视图】

对象策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：表示对象策略的描述信息，为1～127个字符的字符串，区分大小写。

【使用指导】

使用**description**命令时，如果当前对象策略没有描述信息，则为其添加描述信息，否则修改其描述信息。

【举例】

\# 为IPv4对象策略配置描述信息。

\<Sysname\> system-view

Sysname object-policy ip permit

Sysname-object-policy-ip-permit description zone-pair security office to library

【相关命令】

·**display** **object-policy ip**

·**display** **object-policy ipv6**

**对象策略 \-- 对象策略配置命令 \-- display object-policy accelerate**

------------------------------------------------------------------------

![说明](对象策略命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display object-policy** **accelerate**]命令用来显示对象策略的加速状态。

【命令】

集中式设备：

**[display object-policy accelerate**[ { **summary** { **ip** \| **ipv6** } \| **verbose** { **ip** *object-policy-name* \| **ipv6** *object-policy-ipv6name* } }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display object-policy**[ **accelerate** { **summary** { **ip \| ipv6** } \| **verbose** { **ip** *object-policy-name* \| **ipv6** *object-policy-name* } **slot** *slot-number* ]{.apple-converted-space}**cpu**{.apple-converted-space}*cpu-number * }]

分布式设备－IRF模式：

**[display object-policy**[ **accelerate** { **summary** { **ip** \| **ipv6** } \| **verbose** { **ip** *object-policy-name* \| **ipv6** *object-policy-name* } **chassis** *chassis-number* **slot** *slot-number* [ **cpu**]]{.apple-converted-space}*cpu-number * }]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[summary**]：显示对象策略加速的概要信息。

**[verbose**]：显示对象策略加速的详细信息。

**[ip**]：显示IPv4对象策略的加速状态。

**[ipv6**]：显示IPv6对象策略的加速状态。

*[object-policy-name*]：指定对象策略的名称，为1～63个字符的字符串，不区分大小写。

**[slot*** slot-number*]：显示指定单板的对象策略加速信息，该单板必须为加速芯片所在单板，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的对象策略加速信息，该设备必须为加速芯片所在成员设备，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的对象策略加速信息，该单板必须为加速芯片所在单板，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU上对象策略加速信息，*cpu-number*表示CPU的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示加速状态的概要信息。

\<Sysname\> display object-policy accelerate summary ip

Object-policy ip a

Object-policy ip c

\# 显示加速状态的详细信息。

\<Sysname\> display object-policy accelerate verbose ip a

Object-policy ip a

 rule 1 drop

 rule 0 pass (failed)

表1-1 display object-policy accelerate verbose命令显示信息描述表

字段

描述

failed

表示此规则加速失败，匹配不生效

**对象策略 \-- 对象策略配置命令 \-- display object-policy ip**

------------------------------------------------------------------------

**[display** **object-policy ip**]命令用来显示指定名称的IPv4对象策略的配置信息。

【命令】

**[display object-policy ip** [ *object-policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[object-policy-name*]表示对象策略的名称，为1～63个字符的字符串，不区分大小写。若未指定本参数，将显示所有IPv4对象策略配置信息。

【使用指导】

本命令将按照实际匹配顺序即规则配置的先后顺序来排列对象策略内的IPv4规则。

【举例】

\# 显示所有的IPv4对象策略配置信息。

\<Sysname\> display object-policy ip

Object-policy ip pass

This is an IPv4 object policy for zone-pair security source office destination library

Object-policy accelerated

 rule 5 pass source-ip sourceip

 rule 5 comment This rule is used for source-ip sourceip

表1-2 display object-policy ip命令显示信息描述表

字段

描述

Object-policy ip pass

对象策略的名称

This is an IPv4 object policy for zone-pair security source office destination library

该对象策略的描述信息

Object-policy accelerated

该对象策略使能了加速功能

rule 5 pass source-ip sourceip

规则5的具体内容，sourceip为源IP地址对象组的名称

rule 5 comment This rule is used for source-ip sourceip

规则5的描述信息

**对象策略 \-- 对象策略配置命令 \-- display object-policy ipv6**

------------------------------------------------------------------------

**[display** **object-policy ipv6**]命令用来显示指定名称的IPv6对象策略的配置信息。

【命令】

**[display object-policy ipv6** [ *object-policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[object-policy-name*]表示对象策略的名称，为1～63个字符的字符串，不区分大小写。若未指定本参数，将显示所有IPv6对象策略配置信息。

【使用指导】

本命令将按照实际匹配顺序即规则配置的先后顺序来排列对象策略内的IPv6规则。

【举例】

\# 显示所有的IPv6对象策略配置信息。

\<Sysname\> display object-policy ipv6

Object-policy ipv6 pass

This is an IPv6 object policy for zone-pair security source office destination library

Object-policy accelerated

 rule 5 pass source-ip sourceipv6

 rule 5 comment This rule is used for source-ip sourceipv6

表1-3 display object-policy ipv6命令显示信息描述表

字段

描述

Object-policy ipv6 pass

对象策略的名称

This is an IPv6 object policy for zone-pair security source office destination library

该对象策略的描述信息

Object-policy accelerated

该对象策略使能了加速功能

rule 5 pass source-ip sourceipv6

规则5的具体内容，sourceipv6为源IPv6地址对象组的名称

rule 5 comment This rule is used for source-ip sourceipv6

规则5的描述信息

·

**对象策略 \-- 对象策略配置命令 \-- display object-policy statistics zone-pair security**

------------------------------------------------------------------------

**[display** **object-policy statistics zone-pair security**]命令用来显示指定安全域间实例的统计信息。

【命令】

**[display object-policy statistics zone-pair security**[ **source** *source-zone-name* **destination** *destination-zone-name* [ **ip** \| **ipv6** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[source-zone-name*]：表示安全域间实例源安全域的名称，为1～31个字符的字符串，不区分大小写。*destination-zone-name*：表示安全域间实例目的安全域的名称，为1～31个字符的字符串，不区分大小写。

**[ip**]：表示显示IP对象策略的统计信息。

**[Ipv6**]：表示显示IPv6对象策略的统计信息。

【使用指导】

如果不指定指定**ip**或者**ipv6**，则显示指定安全域间实例应用的所有对象策略的统计信息。

【举例】

\# 显示所有的安全域间实例应用对象策略的统计信息。

\<Sysname\> display object-policy statistics zone-pair security source office destination library

Object-policy apply ip OfficeToLibrary

 rule 0 pass source-ip sourceip1 (5 times matched)

 rule 1 drop source-ip sourceip2 (6 times matched)

Object-policy apply ipv6 OfficeToLibraryIPv6

 rule 0 pass source-ip sourceip3

 rule 1 drop source-ip sourceip4 (6 times matched)

表1-4 display object-policy statistics zone-pair security命令显示信息描述表

字段

描述

Object-policy apply ip OfficeToLibrary

安全域间实例应用IPv4对象策略名称

rule 0 pass source-ip sourceip1

安全域间实例应用IPv4对象策略规则，sourceip1为源IP地址对象组的名称

Object-policy apply ipv6 OfficeToLibraryIPv6

安全域间实例应用IPv6对象策略名称

rule 0 pass source-ip sourceip3

安全域间实例应用IPv6对象策略规则，sourceip3为源IPv6地址对象组的名称

5 times matched

该规则匹配的次数为5（当匹配次数为0时不显示本字段）

【相关命令】

·**reset object-policy statistics**

**对象策略 \-- 对象策略配置命令 \-- display object-policy zone-pair security**

------------------------------------------------------------------------

**[display** **object-policy zone-pair security**]命令用来显示指定安全域间实例应用对象策略的配置信息。

【命令】

**[display object-policy zone-pair security** [ **source** *source-zone-name* **destination** *destination-zone-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[source-zone-name*]：表示安全域间实例源安全域的名称，为1～31个字符的字符串，不区分大小写。*destination-zone-name*：表示安全域间实例目的安全域的名称，为1～31个字符的字符串，不区分大小写。

若未指定安全域间实例，将显示所有安全域间实例应用对象策略的配置信息。

【举例】

\# 显示所有的安全域间实例应用对象策略的配置信息。

\<Sysname\> display object-policy zone-pair security

Zone-pair source office destination library

object-policy apply ip permit

object-policy apply ipv6 drop

表1-5 display object-policy zone-pair security命令显示信息描述表

字段

描述

Zone-pair source office destination library

安全域间实例

object-policy apply ip permit

安全域间实例应用IPv4对象策略配置信息

object-policy apply ipv6 drop

安全域间实例应用IPv6对象策略配置信息

**对象策略 \-- 对象策略配置命令 \-- move rule**

------------------------------------------------------------------------

**[move rule**]命令用来移动对象策略规则。

【命令】

**[move** **rule** *rule-id* **before** *insert-rule-id*]

【视图】

对象策略视图

【参数】

*[rule-id*]：指定待移动的对象策略规则编号，取值范围为0～65534。

*[insert-rule-id*]：表示移动到指定编号的规则之前，取值范围为0～65535，其中指定编号为65535时表示移动到所有规则之后。

【使用指导】

如果*insert-rule-id*与*rule-id*相同或其指定的规则不存在，则不执行任何移动操作。

【举例】

\# 在IPv4对象策略permit上，将对象策略规则5移动到规则2之前。

\<Sysname\> system-view

Sysname object-policy ip permit

Sysname-object-policy-ip-permit move rule 5 before 2

【相关命令】

·**object-policy ip**

·**object-policy apply ipv6**

·**rule(ipv4 object-policy view)**

·**rule(ipv6 object-policy view)**

**对象策略 \-- 对象策略配置命令 \-- object-policy apply ip**

------------------------------------------------------------------------

**[object-policy apply ip**]命令用来在安全域间实例内应用IPv4对象策略。

**[undo** **object-policy apply ip**]命令用来在安全域间实例内取消应用IPv4对象策略。

【命令】

**[object-policy apply ip ***object-policy-name*]

**[undo object-policy apply ip ***object-policy-name*]

【缺省情况】

安全域间实例内不应用任何IPv4对象策略。

【视图】

安全域间实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-policy-name*]：指定对象策略的名称。为1～63个字符的字符串，不区分大小写。

【使用指导】

·使用**object-policy apply ip**时，对应的IPv4对象策略必须已经创建，否则将配置失败。

·每个安全域间实例只能应用一个IPv4对象策略。如果使用**object-policy apply ip**时对应安全域间实例已经应用其他IPv4策略，则会配置失败。若要应用新的IPv4对象策略，需要先将已经应用的IPv4对象策略删掉。

【举例】

\# 创建IPv4对象策略，并将该对象策略应用于一个安全域间实例中。

\<Sysname\> system-view

Sysname object-policy ip permit

Sysname-object-policy-ip-permitquit

Sysname zone-pair security source office destination library

Sysname-zone-pair-security-office-library object-policy apply ip permit

【相关命令】

·**object-policy ip**

·**object-policy apply ipv6**

·**display object-policy zone-pair security**

**对象策略 \-- 对象策略配置命令 \-- object-policy apply ipv6**

------------------------------------------------------------------------

**[object-policy apply ipv6**]命令用来在安全域间实例内应用IPv6对象策略。

**[undo** **object-policy apply ipv6**]命令用来在安全域间实例内取消应用IPv6对象策略。

【命令】

**[object-policy apply ipv6 ***object-policy-name*]

**[undo object-policy apply ipv6 ***object-policy-name*]

【缺省情况】

安全域间实例内不应用任何IPv6对象策略。

【视图】

安全域间实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-policy-name*]：指定对象策略的名称。为1～63个字符的字符串，不区分大小写。

【使用指导】

·使用**object-policy apply ipv6**时，对应的IPv6对象策略必须已经创建，否则将配置失败。

·每个安全域间实例只能应用一个IPv6对象策略。如果使用**object-policy apply ipv6**时对应安全域间实例已经应用其他IPv6策略，则会配置失败。若要应用新的IPv6对象策略，需要先将已经应用的IPv6对象策略删掉。

【举例】

\# 创建IPv6对象策略，并将该对象策略应用于一个安全域间实例中。

\<Sysname\> system-view

Sysname object-policy ipv6 permit

Sysname-object-policy-ipv6-permitquit

Sysname zone-pair security source office destination library

Sysname-zone-pair-security-office-library object-policy apply ipv6 permit

【相关命令】

·**object-policy ipv6**

·**object-policy apply ip**

·**display object-policy zone-pair security**

**对象策略 \-- 对象策略配置命令 \-- object-policy ip**

------------------------------------------------------------------------

**[object-policy ip**]命令用来创建一个IPv4对象策略，并进入相应的对象策略视图。

**[undo** **object-policy ip**]命令用来删除指定IPv4对象策略。

【命令】

**[object-policy ip ***object-policy-name*]

**[undo object-policy ip ***object-policy-name*]

【缺省情况】

不存在任何IPv4对象策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-policy-name*]：指定对象策略的名称。为1～63个字符的字符串，不区分大小写。

【使用指导】

·使用**object-policy ip**时，如果指定名称的IPv4对象策略不存在，则创建该对象策略，并进入其视图，否则直接进入其视图。

·IPv4对象策略的名称只能在创建时设置。对象策略一旦创建，便不允许再修改其原有名称。

·使用**undo object-policy ip**时，必须保证无安全域间实例应用指定IPv4对象策略，否则，将删除失败。

【举例】

\#创建一个IPv4对象策略并进入其视图。

\<Sysname\> system-view

Sysname object-policy ip permit

Sysname-object-policy-ip-permit rule pass

【相关命令】

·**object-policy ipv6**

·**display object-policy**** ip**

**对象策略 \-- 对象策略配置命令 \-- object-policy ipv6**

------------------------------------------------------------------------

**[object-policy ipv6**]命令用来创建一个IPv6对象策略，并进入相应的对象策略视图。

**[undo** **object-policy ipv6**]命令用来删除指定IPv6对象策略。

【命令】

**[object-policy ipv6 ***object-policy-name*]

**[undo object-policy ipv6 ***object-policy-name*]

【缺省情况】

不存在任何IPv6对象策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[object-policy-name*]：指定对象策略的名称。为1～63个字符的字符串，不区分大小写。

【使用指导】

·使用**object-policy ipv6**时，如果指定名称的IPv6对象策略不存在，则创建该对象策略，并进入其视图，否则直接进入其视图。

·IPv6对象策略的名称只能在创建时设置。对象策略一旦创建，便不允许再修改其原有名称。

·使用**undo object-policy ipv6**时，必须保证无安全域间实例应用指定IPv6对象策略，否则，将删除失败。

【举例】

\# 创建一个IPv6对象策略并进入其视图。

\<Sysname\> system-view

Sysname object-policy ipv6 permit

Sysname-object-policy-ipv6-permit rule pass

【相关命令】

·**object-policy ip**

·**display object-policy**** ipv6**

**对象策略 \-- 对象策略配置命令 \-- reset object-policy statistics**

------------------------------------------------------------------------

**[reset object-policy statistics**]命令用来清除对象策略在安全域间实例中的统计信息。

【命令】

**[reset** **object-policy** **statistics** [ **zone-pair security** **source** *source-zone-name* **destination** *destination-zone-name*  [ **ip** \| **ipv6** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[source-zone-name*]：表示安全域间实例源安全域的名称，为1～31个字符的字符串，不区分大小写。*destination-zone-name*：表示安全域间实例目的安全域的名称，为1～31个字符的字符串，不区分大小写。

**[ip**]：表示清除IP对象策略的统计信息。

**[Ipv6**]：表示清除IPv6对象策略的统计信息。

【使用指导】

若未指定安全域间实例，则清除所有安全域间实例指定类型对象策略的统计信息。若未指定**ip**或**ipv6，**则清除所有类型对象策略的统计信息。

【举例】

\# 清除指定安全域间实例的IPv4对象策略的统计信息。

\<Sysname\> reset object-policy statistics zone-pair security source office destination library ip

【相关命令】

·**display**** object-policy** **statistics****zone-pair security**

**对象策略 \-- 对象策略配置命令 \-- rule comment**

------------------------------------------------------------------------

**[rule** **comment**]命令用来为指定规则配置描述信息。

**[undo** **rule** **comment**]命令用来删除指定规则的描述信息。

【命令】

**[rule** *rule-id* **comment** *text*]

**[undo** **rule** *rule-id* **comment**]

【缺省情况】

规则没有任何描述信息。

【视图】

对象策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定规则的编号，该规则必须存在。取值范围为0～65534。

*[text*]：表示规则的描述信息，为1～127个字符的字符串，区分大小写。

【使用指导】

·使用**rule** **comment**命令时，指定的规则必须已经创建，如果没有创建，则会配置失败。

·使用**rule** **comment**命令时，如果指定的规则没有描述信息，则为其添加描述信息，否则修改其描述信息。

【举例】

\# 为IPv4对象策略配置规则0，并为该规则配置描述信息。

\<Sysname\> system-view

Sysname object-policy ip permit

Sysname-object-policy-ip-permit rule 0 pass source-ip ip1

Sysname-object-policy-ip-permit rule 0 comment This rule is used for source-ip ip1

【相关命令】

·**display** **object-policy ip**

·**display** **object-policy ipv6**

**对象策略 \-- 对象策略配置命令 \-- rule(ipv4 object-policy view)**

------------------------------------------------------------------------

**[rule**]命令用来创建一条IPv4对象策略规则。

**[undo** **rule**]命令用来删除一条IPv4对象策略规则或删除规则中的部分内容。

【命令】

**[rule** [ *rule-id*  { **drop** \| **pass** } [ [ **source-ip** { *object-group-name* \| **any ** }   **destination-ip** { *object-group-name \|* **any** }   **service** { *object-group-name* \| **any** } ]  **vrf** *vrf-name*   **counting**   **disable**   **logging**   **time-range** *time-range-name*  ] ]]*\**

**[undo**[ **rule** *rule-id* [ **source-ip** *\|* **destination-ip** *\|* **service** *\|* **vrf** \| **counting** \|**disable** \| **logging** \| **time-range** ] ]]*\**

【缺省情况】

IPv4对象策略内不存在任何规则。

【视图】

IPv4对象策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定IPv4对象策略规则的编号，取值范围为0～65534。若未指定本参数，系统将从0开始，自动分配一个大于现有最大编号的最小编号，步长为1。若新编号超出了编号上限（65534），则选择当前未使用的最小编号作为新的编号。

**[drop**]：表示丢弃符合条件的报文。

**[pass**]：表示允许符合条件的报文。

**[source-ip*** object-group-name*]：指定IPv4源IP地址对象组的名称。*object-group-name*表示源IP地址对象组的名称，为1～31个字符的字符串，不区分大小写。**any**表示任意源IP地址对象组。

**[destination-ip*** object-group-name*]：指定IPv4目的IP地址对象组的名称。*object-group-name*表示IPv4目的IP地址对象组的名称，为1～31个字符的字符串，不区分大小写。**any**表示任意目的IP地址对象组。

**[service*** object-group-name*]：指定服务对象组的名称。*object-group-name*表示服务对象组的名称，为1～31个字符的字符串，不区分大小写。**any**表示任意服务对象组。

**[vrf** *vrf-name*]：表示对指定VRF中的报文有效。*vrf-name*表示VRF的名称，为1～31个字符的字符串，区分大小写。若未指定本参数，表示该规则仅对公网报文有效。

**[counting**]：表示使能当前IPv4对象策略规则匹配统计功能，缺省为关闭。

**[disable**]：表示关闭当前IPv4对象策略规则。

**[logging**]：表示对符合条件的报文记录日志信息。

**[time-range** *time-range-name*]：指定本规则生效的时间段。*time-range-name*表示时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"ACL和QoS配置指导"中的"时间段"。

【使用指导】

·使用**rule**命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。

·创建规则时可以不指定任何对象，则规则对任意报文生效。

·创建规则时，若指定的对象组不存在，该规则仍会成功创建，但不会匹配任何报文。

·使用**undo** **rule**命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。

·使用**undo** **rule**命令时必须指定一个已存在规则的编号，可以使用**display** **object-policy**命令来查看当前对象策略所有已存在的规则。

【举例】

\# 为IPv4对象策略创建规则如下：允许源IP地址对象组sourceip1对应的报文在时间段time1通过。

\<Sysname\> system-view

Sysname object-policy ip permit

Sysname-object-policy-ip-permit rule pass source-ip sourceip1 logging time-range time1

【相关命令】

·**object-policy ip**

·**display** **object-policy**** ip**

·**move rule**

·**time-range**

**对象策略 \-- 对象策略配置命令 \-- rule(ipv6 object-policy view)**

------------------------------------------------------------------------

**[rule**]命令用来创建一条IPv6对象策略规则。

**[undo** **rule**]命令用来删除一条IPv6对象策略规则或删除规则中的部分内容。

【命令】

**[rule** [ *rule-id*  { **drop** \| **pass** } [ [ **source-ip** { *object-group-name* \| **any** }   **destination-ip** { *object-group-name* \| **any** }   **service** { *object-group-name* \| **any** } ] **vrf** *vrf-name*   **counting**   **disable**   **logging**   **time-range** *time-range-name*  ] ]]*\**

**[undo**[ **rule** *rule-id* [ **source-ip** *\|* **destination-ip** *\|* **service** *\|* **vrf** *\|* **counting** \| **disable** \| **logging** \| **time-range** ] ]]*\**

【缺省情况】

IPv6对象策略内不存在任何规则。

【视图】

IPv6对象策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rule-id*]：指定IPv6对象策略规则的编号，取值范围为0～65534。若未指定本参数，系统将从0开始，自动分配一个大于现有最大编号的最小编号，步长为1。若新编号超出了编号上限（65534），则选择当前未使用的最小编号作为新的编号。

**[drop**]：表示丢弃符合条件的报文。

**[pass**]：表示允许符合条件的报文。

**[source-ip*** object-group-name*]：指定源IPv6地址对象组的名称。*object-group-name*表示源IPv6地址对象组的名称，为1～31个字符的字符串，不区分大小写。**any**表示任意源IPv6地址对象组。

**[destination-ip*** object-group-name*]：指定目的IPv6地址对象组的名称。*object-group-name*表示目的IPv6地址对象组的名称，为1～31个字符的字符串，不区分大小写。**any**表示任意目的IPv6地址对象组。

**[service*** object-group-name*]：指定服务对象组的名称。*object-group-name*表示服务对象组的名称，为1～31个字符的字符串，不区分大小写。**any**表示任意服务对象组。

**[vrf** *vrf-name*]：表示对指定VRF中的报文有效。*vrf-name*表示VRF的名称，为1～31个字符的字符串，区分大小写。若未指定本参数，表示该规则仅对公网报文有效。

**[counting**]：表示使能当前IPv6对象策略规则匹配统计功能，缺省为关闭。

**[disable**]：表示关闭当前IPv6对象策略规则。

**[logging**]：表示对符合条件的报文记录日志信息。

**[time-range** *time-range-name*]：指定本规则生效的时间段。*time-range-name*表示时间段的名称，为1～32个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"ACL和QoS配置指导"中的"时间段"。

【使用指导】

·使用**rule**命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。

·创建规则时可以不指定任何对象，则规则对任意报文生效。

·创建规则时，若指定的对象组不存在，该规则仍会成功创建，但不会匹配任何报文。

·使用**undo** **rule**命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。

·使用**undo** **rule**命令时必须指定一个已存在规则的编号，可以使用**display** **object-policy**** ipv6**命令来查看当前对象策略所有已存在的规则。

【举例】

\# 为IPv6对象策略创建规则如下：允许源IPv6地址对象组sourceip1对应的报文在时间段time1通过。

\<Sysname\> system-view

Sysname object-policy ipv6 permit

Sysname-object-policy-ipv6-permit rule pass source-ip sourceip1 logging time-range time1

【相关命令】

·**object-policy ipv6**

·**display** **object-policy**** ipv6**

·**move rule**

·**time-range**
