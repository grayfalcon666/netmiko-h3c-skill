
**路由策略 \-- 路由策略公共配置命令 \-- apply as-path**

------------------------------------------------------------------------

**[apply as-path**]命令用来配置BGP路由信息AS_PATH属性。

**[undo apply as-path**]命令用来恢复缺省情况。

【命令】

**[apply as-path **]*as-number*&\<1-32\> [ **replace** ]

**[undo apply as-path**]

【缺省情况】

没有配置BGP路由信息的AS_PATH属性。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[as-number*&\<1-32\>]：自治系统号，取值范围为1～4294967295。&\<1-32\>表示前面的参数可以输入1～32次。

**[replace**]：替换原有AS号。如果未指定本参数，则在原AS路径前加入AS号。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果路由信息匹配已存在的编号为1的AS路径访问列表，那么在原AS路径前加入AS号200。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match as-path 1

Sysname-route-policy-policy1-10 apply as-path 200

【相关命令】

·**display ip as-path**

·**if-match as-path**

·**ip as-path**

**路由策略 \-- 路由策略公共配置命令 \-- apply comm-list delete**

------------------------------------------------------------------------

**[apply comm-list delete**]命令用来删除BGP路由信息的团体属性。

**[undo apply comm-list**]命令用来恢复缺省情况。

【命令】

**[apply comm-list**[ { *comm-list-number* \| *comm-list-name* } **delete**]]

**[undo apply comm-list**]

【缺省情况】

没有删除BGP路由信息的团体属性。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[comm-list-number*]：团体属性列表号。

·基本团体属性列表号的取值范围为1～99；

·高级团体属性列表号的取值范围为100～199。

*[comm-list-name*]：团体属性列表名，为1～63个不全为数字的字符串，区分大小写。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。删除已存在的团体属性列表1中指定的BGP路由信息的团体属性。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 apply comm-list 1 delete

【相关命令】

·**ip community-list**

**路由策略 \-- 路由策略公共配置命令 \-- apply community**

------------------------------------------------------------------------

**[apply community**]命令用来配置BGP路由信息的团体属性。

**[undo apply community**]命令用来取消该配置。

【命令】

**[apply community **[{ **none** \| **additive** \| { *community-number*&\<1-32\> \| *aa:nn*&\<1-32\> \| **internet** \| **no-advertise** \| **no-export** \| **no-export-subconfed** } \* [ **additive** ] }]]

**[undo apply community **[[ **none** \| **additive** \| { *community-number*&\<1-32\> \| *aa:nn*&\<1-32\> \| **internet** \| **no-advertise** \| **no-export** \| **no-export-subconfed** } **\*** [ **additive** ] ]]]

【缺省情况】

没有配置BGP路由信息的团体属性。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[none**]：删除路由的团体属性。

*[community-number*&\<1-32\>]：团体序号，取值范围为1～4294967295。&\<1-32\>表示前面的参数可以输入1～32次。

*[aa:nn*&\<1-32\>]：团体号，*aa*和*nn*的取值范围为0～65535。&\<1-32\>表示前面的参数可以输入1～32次。

**[internet**]：预定义的团体属性。缺省情况下，所有的路由都具有**internet**团体属性，可以被通告给所有的BGP对等体。

**[no-advertise**]：具有此属性的路由在收到后，不能被通告给任何其他的BGP对等体。

**[no-export**]：具有此属性的路由在收到后，不能被发布到本地AS之外。如果使用了联盟，则不能被发布到联盟之外，但可以发布给联盟中的其他子AS。

**[no-export-subconfed**]：具有此属性的路由在收到后，不能被发布到本地AS之外，也不能发布到联盟中的其他子AS。

**[additive**]：附加至原有路由的团体属性。

【举例】

\# 创建一个名为setcommunity的路由策略，其节点序列号为16，匹配模式为permit。配置BGP路由的团体属性为no-export。

\<Sysname\> system-view

Sysname route-policy setcommunity permit node 16

Sysname-route-policy-setcommunity-16 apply community no-export

【相关命令】

·**if-match community**

·**ip community-list**

**路由策略 \-- 路由策略公共配置命令 \-- apply cost**

------------------------------------------------------------------------

**[apply cost**]命令用来配置路由信息的路由开销。

**[undo apply cost**]命令用来恢复缺省情况。

【命令】

**[apply cost**[ [ **+** \| **-** ] *value*]]

**[undo apply cost**]

【缺省情况】

没有配置路由信息的路由开销。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[+**]：增加开销值。

**[-**]：减少开销值。

*[value*]：指定路由信息的路由开销，取值范围为0～4294967295。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配OSPF外部路由，那么设置该路由的路由开销为120。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match route-type external-type1or2

Sysname-route-policy-policy1-10 apply cost 120

**路由策略 \-- 路由策略公共配置命令 \-- apply cost-type**

------------------------------------------------------------------------

**[apply cost-type**]命令用来配置路由信息的路由开销类型。

**[undo apply cost-type**]命令用来恢复缺省情况。

【命令】

**[apply cost-type**[{ **external** \| **internal** \| **type-1** \| **type**-**2** }]]

**[undo** **apply cost-type**]

【缺省情况】

没有配置路由开销类型。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[external**]：IS-IS外部路由。

**[internal**]：IS-IS内部路由或者设置BGP路由的MED值为下一跳的IGP度量值。

**[type-1**]：OSPF的外部Type-1路由。

**[type-2**]：OSPF的外部Type-2路由。

【使用指导】

**[apply cost-type internal**]命令的作用：

·应用于IS-IS路由：设置路由类型为IS-IS内部路由。

·应用于BGP路由：路由器从IBGP对等体学到的路由在通告给EBGP对等体时，如果配置**apply cost-type internal**命令，则路由器会将向EBGP对等体通告的路由的MED值设置为该路由的下一跳的IGP度量值。

【举例】

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match tag 8

Sysname-route-policy-policy1-10 apply cost-type internal

**路由策略 \-- 路由策略公共配置命令 \-- apply extcommunity**

------------------------------------------------------------------------

**[apply extcommunity**]命令用来配置BGP路由信息的扩展团体属性。

**[undo apply extcommunity**]命令用来恢复缺省情况。

【命令】

**[apply extcommunity** { **rt** *route-target* }&\<1-32\> [ **additive** ]]

**[undo apply extcommunity**]

【缺省情况】

没有配置BGP路由信息的扩展团体属性。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

{ **rt** *route-target* }&\<1-32\>：指定的RT（Route Target，路由目标）扩展团体属性，为3～21个字符的字符串。&\<1-32\>表示前面的参数可以输入1～32次。

*[route-target*]有三种形式，分别如下：

·16位自治系统号:32位用户自定义数，例如：101:3。其中，自治系统号取值范围为0～65535，用户自定义数取值范围为0～4294967295。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。其中，用户自定义数取值范围为0～65535。

·32位自治系统号:16位用户自定义数，例如：70000:3。其中，自治系统号取值范围为65536～4294967295，用户自定义数取值范围为0～65535。

**[additive**]：允许增加到已有的扩展团体中。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配已存在的编号为1的AS路径访问列表，那么为BGP指定RT扩展团体属性。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match as-path 1

Sysname-route-policy-policy1-10 apply extcommunity rt 100:2 additive

**路由策略 \-- 路由策略公共配置命令 \-- apply ip-precedence**

------------------------------------------------------------------------

**[apply ip-precedence**]命令用来配置路由的IP优先级。

**[undo apply ip-precedence**]命令用来恢复缺省情况。

【命令】

**[apply ip-precedence **[{ *value* \| **clear** }]]

**[undo** **apply ip-precedence**]

【缺省情况】

没有配置路由的IP优先级。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：路由的IP优先级，取值范围是0～7。

**[clear**]：清除路由的IP优先级。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配扩展团体列表号100的BGP路由，那么配置路由的IP优先级为3。

\<Sysname\> system-view

Sysname ip extcommunity-list 100 permit rt 100:100

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match extcommunity 100

Sysname-route-policy-policy1-10 apply ip-precedence 3

**路由策略 \-- 路由策略公共配置命令 \-- apply isis**

------------------------------------------------------------------------

**[apply isis**]命令用来配置引入路由到IS-IS某个级别的区域。

**[undo apply isis**]命令用来恢复缺省情况。

【命令】

**[apply isis **[{ **level-1** \| **level-1-2** \| **level-2** }]]

**[undo apply isis**]

【缺省情况】

没有配置引入路由到IS-IS某个级别的区域。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：引入路由到IS-IS的Level-1区域。

**[level-1-2**]：引入路由到IS-IS的Level-1和Level-2区域。

**[level-2**]：引入路由到IS-IS的Level-2区域。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配标记域为8的路由，那么引入路由到IS-IS的Level-2区域。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match tag 8

Sysname-route-policy-policy1-10 apply isis level-2

**路由策略 \-- 路由策略公共配置命令 \-- apply local-preference**

------------------------------------------------------------------------

**[apply local-preference**]命令用来配置BGP路由信息的本地优先级。

**[undo apply local-preference**]命令用来恢复缺省情况。

【命令】

**[apply local-preference** *preference*]

**[undo apply local-preference**]

【缺省情况】

没有配置BGP路由信息的本地优先级。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preference*]：BGP路由信息的本地优先级，取值范围为0～4294967295。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配已存在的编号为1的AS路径访问列表，那么配置该BGP路由的本地优先级为130。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match as-path 1

Sysname-route-policy-policy1-10 apply local-preference 130

**路由策略 \-- 路由策略公共配置命令 \-- apply mpls-label**

------------------------------------------------------------------------

![说明](路由策略命令.files/image001.png)

本命令支持的情况与设备的型号有关，请以设备的实际情况为准。

**[apply mpls-label**]命令用来为路由分配MPLS标签。

**[undo apply mpls-label**]命令用来恢复缺省情况。

【命令】

**[apply mpls-label**]

**[undo apply mpls-label**]

【缺省情况】

没有为路由分配MPLS标签。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果MPLS标签分配失败，路由信息将不会被发布。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。为路由分配MPLS标签。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 apply mpls-label

**路由策略 \-- 路由策略公共配置命令 \-- apply origin**

------------------------------------------------------------------------

**[apply origin**]命令用来配置BGP路由信息的ORIGIN属性。

**[undo apply origin**]命令用来恢复缺省情况。

【命令】

**[apply origin** { **egp** *as-number* \| **igp** \| **incomplete** }]

**[undo apply origin**]

【缺省情况】

没有配置BGP路由信息的ORIGIN属性。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[egp*** as-number*]：设定BGP路由信息的来源为外部路由。*as-number*表示指定外部路由的自治系统号，取值范围为1～4294967295。

**[igp**]：设定BGP路由信息的来源为内部路由。

**[incomplete**]：设定BGP路由信息的来源为未知来源。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配已存在的编号为1的AS路径访问列表，那么设置该BGP路由的路由源为IGP。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match as-path 1

Sysname-route-policy-policy1-10 apply origin igp

**路由策略 \-- 路由策略公共配置命令 \-- apply preference**

------------------------------------------------------------------------

**[apply preference**]命令用来配置路由协议的优先级。

**[undo apply preference**]命令用来恢复缺省情况。

【命令】

**[apply preference** *preference*]

**[undo apply preference**]

【缺省情况】

没有配置路由协议的优先级。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preference*]：路由的优先级，取值范围为1～255。

【使用指导】

如果路由协议已经用命令**preference**配置了优先级，再用**apply preference**命令修改路由协议的优先级，则这些匹配策略的路由采用**apply preference**命令修改的优先级，其它路由的优先级均采用**preference**命令所设的值。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配OSPF外部路由，那么设置该路由协议的优先级为90。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match route-type external-type1or2

Sysname-route-policy-policy1-10 apply preference 90

**路由策略 \-- 路由策略公共配置命令 \-- apply preferred-value**

------------------------------------------------------------------------

**[apply preferred-value**]命令用来配置BGP路由信息的首选值。

**[undo apply preferred-value**]命令恢复缺省情况。

【命令】

**[apply preferred-value** *preferred-value*]

**[undo apply preferred-value**]

【缺省情况】

没有配置BGP路由信息的首选值。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preferred-value*]：首选值，取值范围为0～65535。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配已存在的编号为1的AS路径访问列表，那么设置该BGP路由的首选值为66。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match as-path 1

Sysname-route-policy-policy1-10 apply preferred-value 66

**路由策略 \-- 路由策略公共配置命令 \-- apply prefix-priority**

------------------------------------------------------------------------

**[apply prefix-priority**]命令用来配置路由的收敛优先级。

**[undo apply prefix-priority**]命令用来恢复缺省情况。

【命令】

**[apply prefix-priority**[ { **critical** \| **high** \| **medium** }]]

**[undo apply prefix-priority**]

【缺省情况】

没有配置路由的收敛优先级。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[critical**]：路由的收敛优先级为关键。

**[high**]：路由的收敛优先级为高。

**[medium**]：路由的收敛优先级中。

【使用指导】

未配置时，路由的收敛优先级为低（Low**）**。

路由的收敛优先级由高到低为关键、高、中、低。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配已存在的地址前缀列表abc，那么设置该路由的收敛优先级为关键。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match ip address prefix-list abc

Sysname-route-policy-policy1-10 apply prefix-priority critical

**路由策略 \-- 路由策略公共配置命令 \-- apply qos-local-id**

------------------------------------------------------------------------

**[apply qos-local-id**]命令用来配置路由的 QoS本地ID值。

**[undo** **apply qos-local-id**]命令用来恢复缺省情况。

【命令】

**[apply qos-local-id **[{ *value* \| **clear** }]]

**[undo** **apply qos-local-id**]

【缺省情况】

没有配置路由的QoS本地ID值。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：路由的QoS本地ID值，取值范围是1～4095。

**[clear**]：清除路由的QoS本地ID值。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配扩展团体列表号100的BGP路由，那么配置路由的QoS本地ID值为100。

\<Sysname\> system-view

Sysname ip extcommunity-list 100 permit rt 100:100

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match extcommunity 100

Sysname-route-policy-policy1-10 apply qos-local-id 100

**路由策略 \-- 路由策略公共配置命令 \-- apply tag**

------------------------------------------------------------------------

**[apply tag**]命令用来配置IGP路由信息的标记。

**[undo apply tag**]命令用来恢复缺省情况。

【命令】

**[apply tag** *value*]

**[undo apply tag**]

【缺省情况】

没有配置IGP路由信息的标记。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：指定路由信息的标记值，取值范围为0～4294967295。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。配置IGP路由信息的标记为100。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 apply tag 100

**路由策略 \-- 路由策略公共配置命令 \-- apply traffic-index**

------------------------------------------------------------------------

**[apply traffic-index**]命令用来配置BGP路由信息的流量索引。

**[undo** **apply traffic-index**]命令用来恢复缺省情况。

【命令】

**[apply traffic-index **[{ *value* \| **clear** }]]

**[undo** **apply traffic-index**]

【缺省情况】

没有配置BGP路由信息的流量索引。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：流量索引值，取值范围为1～64。

**[clear**]：清除路由的流量索引值。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配扩展团体列表号100的BGP路由，那么配置路由的流量索引值为6。

\<Sysname\> system-view

Sysname ip extcommunity-list 100 permit rt 100:100

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match extcommunity 100

Sysname-route-policy-policy1-10 apply traffic-index 6

**路由策略 \-- 路由策略公共配置命令 \-- continue**

------------------------------------------------------------------------

**[continue**]命令用来配置下一个执行节点。

**[undo continue**]命令用来恢复缺省情况。

【命令】

**[continue** \*[node-number* ]]

**[undo continue**]

【缺省情况】

没有配置下一个执行节点。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[node-number*]：标识本命令会跳转到同一路由策略中的节点索引，取值范围为0～65535。

【使用指导】

下一个执行节点序列号必须大于当前节点序列号。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义continue子句，配置下一个执行节点序列号为20。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 continue 20

**路由策略 \-- 路由策略公共配置命令 \-- display ip as-path**

------------------------------------------------------------------------

**[display ip as-path**]命令用来显示BGP AS路径过滤列表信息。

【命令】

**[display ip as-path** [ *as-path-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[as-path-number*]：AS路径过滤列表号，取值范围为1～256。如果未指定本参数，将显示所有已配置的BGP AS路径过滤列表信息。

【举例】

\# 显示列表号为1的BGP AS路径列表信息。

\<Sysname\> display ip as-path 1

ListID    Mode      Expression

1         permit    2

表1-1 display ip as-path命令显示信息描述表

字段

描述

ListID

AS路径列表号

Mode

匹配模式，有两种取值：

·permit：表示允许

·deny：表示拒绝

Expression

匹配的AS路径正则表达式

**路由策略 \-- 路由策略公共配置命令 \-- display ip community-list**

------------------------------------------------------------------------

**[display ip community-list**]命令用来显示BGP团体属性列表信息。

【命令】

**[display ip community-list**[ [ *basic-community-list-number* \| *adv-community-list-number* \| **name** *comm-list-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[basic-community-list-number*]：为基本团体属性列表号，取值范围为1～99。

*[adv-community-list-number*]：为高级团体属性列表号，取值范围为100～199。

**[name** *comm-list-name*]：团体属性列表名，为1～63个不全为数字的字符串，区分大小写。

【使用指导】

如果未指定团体属性列表号或团体属性列表名，将显示所有已配置的BGP团体属性列表信息。

【举例】

\# 显示所有的BGP团体属性列表信息。

\<Sysname\> display ip community-list

Community List Basic aaa

        permit

Community List Advanced bbb

        permit  3333

表1-1 display ip community-list命令显示信息描述表

字段

描述

Community List Basic

基本团体属性列表

Community List Advanced

高级团体属性列表

permit

匹配模式，有两种取值：

·permit：表示允许

·deny：表示拒绝

**路由策略 \-- 路由策略公共配置命令 \-- display ip extcommunity-list**

------------------------------------------------------------------------

**[display ip extcommunity-list**]命令用来显示BGP扩展团体属性列表信息。

【命令】

**[display ip extcommunity-list** [ *ext-comm-list-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ext-comm-list-number*]：扩展团体属性列表号，取值范围为1～199。如果未指定本参数，将显示所有已配置的BGP扩展团体属性列表信息。

【举例】

\# 显示列表号为1的BGP扩展团体属性列表信息。

\<Sysname\> display ip extcommunity-list 1

Extended Community List Number 1

         permit rt : 9:6

         Permit soo: 9:6

表1-2 display ip extcommunity-list命令显示信息描述表

字段

描述

Extended Community List Number

扩展团体属性列表

permit

匹配模式，有两种取值：

·permit：表示允许

·deny：表示拒绝

rt

RT（Route Target，路由目标）扩展团体属性

soo

SoO（Site of Origin，源站点）扩展团体属性

**路由策略 \-- 路由策略公共配置命令 \-- display mac-list**

------------------------------------------------------------------------

**[display mac-list**]命令用来显示MAC地址列表的统计信息。

【命令】

**[display mac-list **\**[name** *mac-list-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name** *mac-list-name*]*：*指定显示的MAC地址列表名，为1～63个字符的字符串，区分大小写。如果未指定本参数，将显示所有已配置的MAC地址列表的统计信息。

【举例】

\# 显示名为abc的地址前缀列表的统计信息。

\<Sysname\> display mac-list name abc

MAC address list: abc

 Permitted 0

 Denied 0

  Index: 1  Permit: 001b-2188-946c/32

表1-3 display mac-list命令显示信息描述表

字段

描述

MAC address list

MAC地址列表名

Permitted

允许通过的报文个数

Denied 0

拒绝通过的报文个数

Index

标识MAC地址前缀列表中的一条表项

Permit

允许通过的MAC地址

**路由策略 \-- 路由策略公共配置命令 \-- display route-policy**

------------------------------------------------------------------------

**[display route-policy**]命令用来显示配置的路由策略信息。

【命令】

**[display route-policy** [ **name** *route-policy-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name** *route-policy-name*]：指定显示的路由策略名，为1～63个字符的字符串，区分大小写。如果未指定本参数，将显示所有已配置的路由策略信息。

【举例】

\# 显示名为policy1的路由策略信息。

\<Sysname\> display route-policy name policy1

Route-policy: policy1

  permit : 1

          if-match cost 10

          continue: next node 11

          apply comm-list a delete

表1-4 display route-policy命令显示信息描述表

字段

描述

Route-policy

路由策略名称

permit

匹配模式，有两种取值：

·permit表示允许

·deny表示拒绝

if-match

if-match子句，配置的匹配条件

continue

continue字句，配置下一个执行节点

apply

apply子句，如满足匹配条件，则要执行的动作

**路由策略 \-- 路由策略公共配置命令 \-- if-match as-path**

------------------------------------------------------------------------

**[if-match as-path**]命令用来配置BGP路由信息的AS路径域的匹配条件。

**[undo if-match as-path**]命令用来取消该配置。

【命令】

**[if-match as-path** *as-path-number*&\<1-32\>]

**[undo if-match as-path** [ *as-path-number*&\<1-32\> ]]

【缺省情况】

没有配置BGP路由信息的AS路径域的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[as-path-number*&\<1-32\>]：为AS路径过滤列表号，取值范围为1～256。&\<1-32\>表示前面的参数可以输入1～32次。

【使用指导】

路由策略的if-match子句之一，用于过滤BGP路由信息，根据路由信息的自治系统路径属性指定匹配条件。

【举例】

\# 首先定义一个编号为2的as-path，允许自治系统号包含200和300的路由信息通过。然后定义名为test的路由策略，该路由策略编号为10的节点定义了一条if-match子句，它引用的是先前定义的as-path。

\<Sysname\> system-view

Sysname ip as-path 2 permit \_\*200.\*300

Sysname route-policy test permit node 10

Sysname-route-policy-policy1-10 if-match as-path 2

【相关命令】

·**apply as-path**

·**ip as-path**

**路由策略 \-- 路由策略公共配置命令 \-- if-match community**

------------------------------------------------------------------------

**[if-match community**]命令用来配置BGP路由信息的团体属性的匹配条件。

**[undo if-match community**]命令用来取消该配置。

【命令】

**[if-match community**[ { { *basic-community-list-number* \| **name** *comm-list-name* } [ **whole-match** ] \| *adv-community-list-number* }&\<1-32\>]]

**[undo if-match community **[[ { *basic-community-list-number* \| **name** *comm-list-name* } [ **whole-match** ] \| *adv-community-list-number* ]&\<1-32\>]]

【缺省情况】

没有配置BGP路由信息的团体属性的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[basic-community-list-number*]：为基本团体属性列表号，取值范围为1～99。

*[adv-community-list-number*]：为高级团体属性列表号，取值范围为100～199。

*[comm-list-name*]：团体属性列表名，为1～63个不全为数字的字符串，区分大小写。

**[whole-match**]：为确切匹配，即所有团体而且仅有这些团体必须出现。

&\<1-32\>：表示前面的参数可以输入1～32次。

【使用指导】

路由策略的if-match子句之一，用于过滤BGP路由信息，根据路由信息的团体属性指定匹配条件。

【举例】

\# 首先定义一个编号为1的community-list，允许包含团体号100和200的路由信息。然后定义名为test的路由策略，该路由策略编号为10的节点定义了一条if-match子句，它引用的是先前定义的community-list。

\<Sysname\> system-view

Sysname ip community-list 1 permit 100 200

Sysname route-policy test permit node 10

Sysname-route-policy-test-10 if-match community 1

【相关命令】

·**apply community**

·**ip community-list**

**路由策略 \-- 路由策略公共配置命令 \-- if-match cost**

------------------------------------------------------------------------

**[if-match cost**]命令用来配置路由信息的路由开销的匹配条件。

**[undo if-match cost**]命令用来恢复缺省情况。

【命令】

**[if-match cost** *value*]

**[undo if-match cost**]

【缺省情况】

没有配置路由信息的路由开销的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：路由开销，取值范围为0～4294967295。

【使用指导】

路由策略的if-match子句之一，指定满足条件的路由信息的路由开销。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，允许路由开销为8的路由信息通过。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match cost 8

**路由策略 \-- 路由策略公共配置命令 \-- if-match extcommunity**

------------------------------------------------------------------------

**[if-match** **extcommunity**]命令用来配置BGP路由信息的扩展团体属性的匹配条件。

**[undo if-match extcommunity**]命令用来取消该配置。

【命令】

**[if-match extcommunity** *ext-comm-list-number*&\<1-32\>]

**[undo if-match extcommunity** [ *ext-comm-list-number*&\<1-32\> ]]

【缺省情况】

没有配置BGP路由信息的扩展团体属性的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ext-comm-list-number*&\<1-32\>]：扩展团体属性列表号，取值范围为1～199。&\<1-32\>表示前面的参数可以输入1～32次。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，匹配已存在的扩展团体列表号100和150定义的扩展团体属性的路由。

\<Sysname\> system-view

Sysname ip extcommunity-list 100 permit rt 100:100

Sysname ip extcommunity-list 150 permit rt 150:150

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match extcommunity 100 150

【相关命令】

·**apply extcommunity**

·**ip extcommunity-list**

**路由策略 \-- 路由策略公共配置命令 \-- if-match interface**

------------------------------------------------------------------------

**[if-match interface**]命令用来配置路由信息的出接口的匹配条件。

**[undo if-match interface**]命令用来取消该配置。

【命令】

**[if-match interface **{ *interface-type interface-number* }&\<1-16\>]

**[undo if-match interface ** *interface-type interface-number* ]&\<1-16\>

【缺省情况】

没有配置路由信息的出接口的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定接口类型和编号。

&\<1-16\>：表示前面的参数可以输入1～16次。

【使用指导】

将路由策略应用到BGP时，BGP协议不支持配置路由信息的出接口的匹配条件。

【举例】

·路由应用

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，匹配出接口为GigabitEthernet1/0/1的路由信息。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match interface gigabitethernet 1/0/1

·交换应用

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，匹配出接口为Vlan-interface1的路由信息。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match interface vlan-interface 1

**路由策略 \-- 路由策略公共配置命令 \-- if-match local-preference**

------------------------------------------------------------------------

**[if-match **]**local-preference**命令用来配置BGP路由信息的本地优先级的匹配条件。

**[undo if-match **]**local-preference**命令用来恢复缺省情况。

【命令】

**[if-match**]**local-preference ***preference*

**[undo if-match**]**local-preference**

【缺省情况】

没有配置BGP路由信息的本地优先级的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preference*]：BGP路由信息的本地优先级，取值范围为0～4294967295。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，允许BGP路由信息的本地优先级为2的路由信息通过。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match preference 2

**路由策略 \-- 路由策略公共配置命令 \-- if-match mac-list**

------------------------------------------------------------------------

**[if-match mac-list**]命令用来配置MAC地址的匹配条件。

**[undo if-match mac-list**]命令用来取消该配置。

【命令】

**[if-match mac-list ***mac-list-name*]

**[undo if-match mac-list** *mac-list-name*]

【缺省情况】

没有配置MAC地址的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-list-name*]：指定用于过滤MAC地址列表的名称，为1～63 个字符的字符串，区分大小写。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一个if-match子句，允许MAC地址匹配已存在的MAC地址列表p1的路由信息通过。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10if-match mac-list p1

【相关命令】

·**mac-list**

**路由策略 \-- 路由策略公共配置命令 \-- if-match mpls-label**

------------------------------------------------------------------------

![说明](路由策略命令.files/image001.png)

本命令支持的情况与设备的型号有关，请以设备的实际情况为准。

**[if-match mpls-label**]命令用来配置路由信息的MPLS标签的匹配条件。

**[undo if-match mpls-label**]命令用来恢复缺省情况。

【命令】

**[if-match mpls-label**]

**[undo if-match mpls-label**]

【缺省情况】

没有配置路由信息的MPLS标签的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，匹配路由信息的MPLS标签。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match mpls-label

**路由策略 \-- 路由策略公共配置命令 \-- if-match route-type**

------------------------------------------------------------------------

**[if-match route-type**]命令用来配置路由信息类型的匹配条件。

**[undo if-match route-type**]命令用来取消该配置。

【命令】

**[if-match route-type**[ { **external**-**type1** \| **external-type1or2** \| **external-type2** \| **internal** \| **is-is-level-1** \| **is-is-level-2** \| **nssa-external-type1** \| **nssa-external-type1or2** \| **nssa-external-type2** } \*]]

**[undo if-match route-type**[ [ **external**-**type1** \| **external-type1or2** \| **external-type2** \| **internal** \| **is-is-level-1** \| **is-is-level-2** \| **nssa-external-type1** \| **nssa-external-type1or2** \| **nssa-external-type2** ] \*]]

【缺省情况】

没有配置路由信息的类型的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[external-type1**]：OSPF Type1的外部路由。

**[external-type1or2**]：OSPF外部路由。

**[external-type2**]：OSPF Type2的外部路由。

**[internal**]：内部路由（包括OSPF区域间和区域内路由）。

**[is-is-level-1**]：IS-IS的Level-1路由。

**[is-is-level-2**]：IS-IS的Level-2路由。

**[nssa-external-type1**]：OSPF NSSA Type1的外部路由。

**[nssa-external-type1or2**]：OSPF NSSA的外部路由。

**[nssa-external-type2**]：OSPF NSSA Type2的外部路由。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，匹配internal类型的路由。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match route-type internal

**路由策略 \-- 路由策略公共配置命令 \-- if-match tag**

------------------------------------------------------------------------

**[if-match tag**]命令用来配置IGP路由信息标记的匹配条件。

**[undo if-match tag**]命令用来恢复缺省情况。

【命令】

**[if-match tag** *value*]

**[undo if-match tag**]

【缺省情况】

没有配置IGP路由信息标记的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：指定要求的标记值，取值范围为0～4294967295。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，匹配标记为8的IGP路由信息。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match tag 8

**路由策略 \-- 路由策略公共配置命令 \-- if-match vlan**

------------------------------------------------------------------------

**[if-match vlan**]命令用来配置VLAN的匹配条件。

**[undo if-match vlan**]命令用来取消该配置。

【命令】

**[if-match vlan ***vlan-list*]

**[undo if-match vlan ** *vlan-list* ]

【缺省情况】

没有配置VLAN的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-list*]：VLAN列表，表示多个VLAN的ID号。表示方式为*vlan-list* = { *vlan-id* [ to *vlan-id*  }&\<1-16\>]。其中，*vlan-id*为指定VLAN的ID号，取值范围为1～4094。&\<1-16\>表示前面的参数最多可以输入16次。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一个if-match子句，允许VLAN 10和VLAN 100到200的路由信息通过。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match vlan 10 100 to 200

**路由策略 \-- 路由策略公共配置命令 \-- ip as-path**

------------------------------------------------------------------------

**[ip as-path**]命令用来配置一个AS路径过滤列表。

**[undo ip as-path**]命令用来删除指定的AS路径过滤列表。

【命令】

**[ip as-path**[ *as-path-number* { **deny** \| **permit** } *regular-expression*]]

**[undo ip as-path**[ *as-path-number* [ *regular-expression* \| **deny** \| **permit** ]]]

【缺省情况】

没有配置AS路径过滤列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[as-path-number*]：指定的AS路径过滤列表号，取值范围为1～256。

**[deny**]：指定AS路径过滤列表的匹配模式为拒绝模式。

**[permit**]：指定AS路径过滤列表的匹配模式为允许模式。

*[regular-expression*]：AS路径正则表达式，为1～63个字符的字符串。

【使用指导】

BGP协议的路由信息中，包含一个AS路径域，在BGP协议交换路由信息的过程中，该路由所经过的所有AS都会记录在这个域中。试图识别AS路径列表就是要把其与一个正则表达式进行比较。一个正则表达式就是用一个公式代表的字符组合。例如\^200. \*100\$，表示匹配所有AS 200开始、以AS 100结束的AS路径域。AS路径正则表达式所用到的特殊字符及其含义，请参见"基础配置指导"中的"CLI"。

【举例】

\# 配置序号为1的AS路径过滤列表，允许AS_PATH以10开头的路由信息通过。

\<Sysname\> system-view

Sysname ip as-path 1 permit \^10

【相关命令】

·**apply as-path**

·**display ip as-path**

·**if-match as-path**

**路由策略 \-- 路由策略公共配置命令 \-- ip community-list**

------------------------------------------------------------------------

**[ip community-list**]命令用来配置一个团体属性列表表项。

**[undo ip community-list**]命令用来删除指定的团体属性列表或其某个表项。

【命令】

**[ip community-list**[ { *basic-comm-list-num* \| **basic** *basic-comm-list-name* } { **deny** \| **permit** } [ *community-number*&\<1-32\> \| *aa:nn*&\<1-32\>   **internet** \| **no-advertise** \| **no-export** \| **no-export-subconfed** ] \*]]

**[undo ip community-list **[{ *basic-comm-list-num* \| **basic** *basic-comm-list-name* } [ **deny** \| **permit**   *community-number*&\<1-32\> \| *aa:nn*&\<1-32\>   **internet** \| **no-advertise** \| **no-export** \| **no-export-subconfed** ] \*]]

**[ip community-list**[ { *adv-comm-list-num* \| **advanced** *adv-comm-list-name* } { **deny** \| **permit** } *regular-expression*]]

**[undo ip community-list **[{ *adv-comm-list-num* \| **advanced** *adv-comm-list-name* } [ **deny** \| **permit** ]  *regular-expression* ]]

【缺省情况】

没有配置团体属性列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[basic-comm-list-num*]：基本团体属性列表号，取值范围为1～99。

**[basic**]：标识基本团体属性名字。

**[advanced**]：标识高级团体属性名字。

*[basic-comm-list-name*]：基本团体属性列表名，为1～63个不全为数字的字符串，区分大小写。

*[adv-comm-list-name*]：高级团体属性列表名，为1～63个不全为数字的字符串，区分大小写。

*[adv-comm-list-num*]：高级团体属性列表号，取值范围为100～199。

*[regular-expression*]：指定高级团体属性的正则表达式，为1～63个字符的字符串。有关正则表达式的详细介绍，请参见"基础配置指导"中的"CLI"。

**[deny**]：指定团体属性列表的匹配模式为拒绝模式。

**[permit**]：指定团体属性列表的匹配模式为允许模式。

*[community-number*&\<1-32\>]：团体序号，取值范围为1～4294967295。&\<1-32\>表示前面的参数可以输入1～32次。

*[aa:nn*&\<1-32\>]：团体号，*aa*和*nn*的取值范围为0～65535。&\<1-32\>表示前面的参数可以输入1～32次。

**[internet**]：预定义的团体属性。缺省情况下，所有的路由都具有**internet**团体属性，可以被通告给所有的BGP对等体。

**[no-advertise**]：具有此属性的路由在收到后，不能被通告给任何其他的BGP对等体。

**[no-export**]：具有此属性的路由在收到后，不能被发布到本地AS之外。如果使用了联盟，则不能被发布到联盟之外，但可以发布给联盟中的其他子AS。

**[no-export-subconfed**]：具有此属性的路由在收到后，不能被发布到本地AS之外，也不能发布到联盟中的其他子AS。

【举例】

\# 配置序号为1的基本团体属性列表，允许**internet**团体属性的路由信息通过。

\<Sysname\> system-view

Sysname ip community-list 1 permit internet

\# 创建序号为100的高级团体属性列表，允许团体属性内容以"10"开头的路由信息通过。

\<Sysname\> system-view

Sysname ip community-list 100 permit \^10

【相关命令】

·**apply comm-list delete**

·**apply community**

·**display ip community-list**

·**if-match community**

**路由策略 \-- 路由策略公共配置命令 \-- ip extcommunity-list**

------------------------------------------------------------------------

**[ip extcommunity-list**]命令用来配置一个扩展团体属性列表表项。

**[undo ip extcommunity-list**]命令用来删除指定的扩展团体属性列表。

【命令】

**[ip extcommunity-list**[ *ext-comm-list-number* { **deny** \| **permit** } { **rt** *route-target* \| **soo** *site-of-origin* }&\<1-32\>]]

**[undo ip extcommunity-list**[ *ext-comm-list-number* [ { **deny** \| **permit** } [ **rt** *route-target* \| **soo** *site-of-origin* ]&\<1-32\> ]]]

【缺省情况】

没有配置扩展团体属性列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ext-comm-list-number*]：扩展团体属性列表号，取值范围为1～199。

**[deny**]：指定扩展团体属性列表的匹配模式为拒绝模式。

**[permit**]：指定扩展团体属性列表的匹配模式为允许模式。

**[rt***route-target*]：指定的RT（Route Target，路由目标）扩展团体属性，为3～21个字符的字符串。&\<1-32\>表示前面的参数可以输入1～32次。

**[soo** *site-of-origin*]：指定的SoO（Site of Origin，源站点）扩展团体属性，为3～21个字符的字符串。&\<1-32\>表示前面的参数可以输入1～32次。

*[route-target*]和*site-of-origin*有三种形式，分别如下：

·16位自治系统号:32位用户自定义数，例如：101:3。其中，自治系统号取值范围为0～65535，用户自定义数取值范围为0～4294967295。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。其中，用户自定义数取值范围为0～65535。

·32位自治系统号:16位用户自定义数，例如：70000:3。其中，自治系统号取值范围为65536～4294967295，用户自定义数取值范围为0～65535。

【举例】

\# 配置序号为1的扩展团体属性列表，允许RT为200:200的路由信息通过。

\<Sysname\> system-view

Sysname ip extcommunity-list 1 permit rt 200:200

\# 配置序号为2的扩展团体属性列表，允许SoO为100:100的路由信息通过。

\<Sysname\> system-view

Sysname ip extcommunity-list 2 permit soo 100:100

【相关命令】

·**apply extcommunity**

·**display ip extcommunity-list**

·**if-match** **extcommunity**

**路由策略 \-- 路由策略公共配置命令 \-- mac-list**

------------------------------------------------------------------------

**[mac-list**]命令用来配置一个MAC地址列表。

**[undo mac-list**]命令用来删除一个MAC地址列表或其某个表项。

【命令】

**[mac-list** *mac-list-name* [ **index** *index-number*  { **deny** \| **permit** } *mac-address*  *mask-length* ]]

**[undo mac-list ***mac-list-name* [ **index** *index-number* ]]

【缺省情况】

没有配置MAC地址列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-list-name*]：指定MAC地址前缀列表名，唯一标识一个MAC地址前缀列表，为1～63个字符的字符串，区分大小写。

*[index-number*]：标识MAC地址前缀列表中的一条表项，*index-number*小的表项先被测试，取值范围为1～65535。

**[deny**]：指定所定义的MAC地址前缀列表表项的匹配模式为拒绝模式。当指定为拒绝模式并且待过滤的MAC地址在该表项指定的前缀范围内时，则该MAC地址不能通过该表项的过滤，并且不会进行下一个表项的测试，否则进入下一表项的测试。

**[permit**]：指定所定义的MAC地址前缀列表表项的匹配模式为允许模式。当指定为允许模式并且待过滤的MAC地址在该表项指定的前缀范围内时，通过该表项的过滤不进入下一个结点的测试；如待过滤的MAC地址不在该表项指定的前缀范围内，则进行下一表项测试。

*[mac-address mask-length*]：指定MAC地址前缀和前缀长度，*mask-length*的取值范围为0～48。

【举例】

\# 定义一条名为wxy的MAC地址前缀列表，只允许MAC地址范围是001b-2188-0000～001b-2188-ffff的通过。

\<Sysname\> system-view

Sysname mac-list wxy permit 001b-2188-946c 32

【相关命令】

·**if-match mac-list**

**路由策略 \-- 路由策略公共配置命令 \-- reset mac-list**

------------------------------------------------------------------------

**[reset mac-list**]命令用来清除MAC地址列表统计信息。

【命令】

**[reset mac-list** [ *mac-list-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-list-name*]：MAC地址前缀列表的名称，为1～63个字符的字符串，区分大小写。如果未指定本参数，将清除所有MAC地址列表的统计信息。

【举例】

\# 清除MAC地址列表abc的统计信息。

\<Sysname\> reset mac-list abc

**路由策略 \-- 路由策略公共配置命令 \-- route-policy**

------------------------------------------------------------------------

**[route-policy**]命令用来创建路由策略，并进入该路由策略视图。

**[undo route-policy**]命令用来删除指定的路由策略。

【命令】

**[route-policy**[ *route-policy-name* { **deny** \| **permit** } **node** *node-number*]]

**[undo route-policy**[ *route-policy-name* [ **deny** \| **permit** ]  **node** *node-number* ]]

【缺省情况】

没有配置路由策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[route-policy-name*]：指定路由策略名，为1～63个字符的字符串，区分大小写。

**[deny**]：指定所定义的路由策略节点的匹配模式为拒绝模式，当路由项满足该节点的所有if-match子句时被拒绝通过该节点的过滤，并且不会进行下一个节点的匹配；如果路由项不满足该节点的if-match子句，将进入下一个节点继续匹配。

**[permit**]：指定所定义的路由策略节点的匹配模式为允许模式。当路由项满足该节点的所有if-match子句时被允许通过该节点的过滤并执行该节点的apply子句，如路由项不满足该节点的if-match子句，将继续匹配该路由策略的下一个节点。

**[node*** node-number*]：标识路由策略中的一个节点索引，当该路由策略用于路由信息过滤时，*node-number*小的节点先被匹配，取值范围为0～65535。

【使用指导】

路由策略用于路由信息过滤。一个路由策略由若干节点组成，每一节点由一些if-match子句和apply子句组成。if-match子句定义该节点的匹配规则，apply子句定义通过该节点过滤后进行的动作。节点的if-match子句之间的过滤关系是"与"的关系，即必须满足该节点的所有if-match子句。路由策略节点之间的过滤关系是"或"的关系，即通过一个节点的过滤就意味着通过该路由策略的过滤。若没有通过任一节点的过滤，则表示没有通过该路由策略的过滤。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit，并进入路由策略视图。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10

【相关命令】

·**display route-policy**

**路由策略 \-- IPv4路由策略配置命令 \-- apply fast-reroute**

------------------------------------------------------------------------

![说明](路由策略命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply** **fast-reroute**]命令用来配置快速重路由备份。

**[undo apply** **fast-reroute**]命令用来取消快速重路由配置。

【命令】

**[apply** **fast-reroute** { **backup-interface** *interface-type interface-number* [ **backup-nexthop** *ip-address*  \| **backup-nexthop** *ip-address* }]]

**[undo apply fast-reroute**]

【缺省情况】

没有配置快速重路由。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[backup-interface*** interface-type interface-number*]：备份出接口。对于备份出接口为非P2P类型的接口时（包括NBMA类型接口或广播类型接口，如以太网接口、VLAN接口等），必须同时指定其对应的备份下一跳地址。*interface-type interface-number*为指定的接口类型和编号。

**[backup-nexthop*** ip-address*]：备份下一跳地址。

【使用指导】

当网络中的链路或某台路由器发生故障时，需要通过故障链路或故障路由器传输才能到达目的地的报文将会丢失或产生路由环路，数据流量将会被中断，直到路由协议根据新的拓扑网络路由收敛完毕后，被中断的流量才能恢复正常的传输。

网络管理员可以为路由协议配置快速重路由功能，路由协议将通过路由策略为路由指定备份下一跳，当路由器探测到网络故障时，路由协议会使用事先指定好的备份下一跳替换失效下一跳，通过备份下一跳来指导报文的转发，从而大大缩短了流量中断时间。

网络管理员可以在路由策略中配置快速重路由功能的指定备份下一跳，为符合过滤条件的路由指定备份下一跳。

【举例】

·路由应用

\# 创建一个名为policy1的路由策略，为到达目的地100.1.1.0/24的路由配置备份出接口为GigabitEthernet1/0/1，备份下一跳地址为193.1.1.8。

\<Sysname\> system-view

Sysname ip prefix-list abc index 10 permit 100.1.1.0 24

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match ip address prefix-list abc

Sysname-route-policy-policy1-10 apply fast-reroute backup-interface gigabitethernet 1/0/1 backup-nexthop 193.1.1.8

·交换应用

\# 创建一个名为policy1的路由策略，为到达目的地100.1.1.0/24的路由配置备份出接口为Vlan-interface1，备份下一跳地址为193.1.1.8。

\<Sysname\> system-view

Sysname ip prefix-list abc index 10 permit 100.1.1.0 24

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match ip address prefix-list abc

Sysname-route-policy-policy1-10 apply fast-reroute backup-interface vlan-interface 1 backup-nexthop 193.1.1.8

**路由策略 \-- IPv4路由策略配置命令 \-- apply ip-address next-hop**

------------------------------------------------------------------------

**[apply ip-address next-hop**]命令用来配置IPv4路由信息的下一跳地址。

**[undo apply ip-address next-hop**]命令用来恢复缺省情况。

【命令】

**[apply ip-address next-hop**[ *ip-address* [ **public** \| **vpn-instance** *vpn-instance-name* ]]]

**[undo apply ip-address** **next-hop**]

【缺省情况】

没有配置IPv4路由信息的下一跳地址。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：下一跳IP地址。

**[public**]：指定公网。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·当引入路由时，使用本命令设置下一跳地址无效。

·如果未指定参数**public**或**vpn-instance ***vpn-instance-name*，则表示下一跳地址为公网地址。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配已存在的编号为1的AS路径访问列表，那么设置路由信息的下一跳地址为193.1.1.8。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match as-path 1

Sysname-route-policy-policy1-10 apply ip-address next-hop 193.1.1.8

**路由策略 \-- IPv4路由策略配置命令 \-- display ip prefix-list**

------------------------------------------------------------------------

**[display ip prefix-list**]命令用来显示IPv4地址前缀列表的统计信息。

【命令】

**[display ip prefix-list** [ **name** *prefix-list-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name** *prefix-list-name*]：指定显示的地址前缀列表名，为1～63个字符的字符串，区分大小写。如果未指定本参数，将显示所有已配置的地址前缀列表的统计信息。

【举例】

\# 显示名为abc的地址前缀列表的统计信息。

\<Sysname\> display ip prefix-list name abc

Prefix-list: abc

 Permitted 0

 Denied 0

         index: 10        deny   6.6.6.0/24              ge  26  le  28

表1-5 display ip prefix-list命令显示信息描述表

字段

描述

Prefix-list

地址前缀列表的名称

Permitted

符合匹配条件的路由个数

Denied

不符合匹配条件的路由个数

index

地址前缀列表的内部序列号

deny

匹配模式，有两种取值：

·permit：表示允许

·deny：表示拒绝

6.6.6.0/24

匹配的IP地址和掩码长度

ge

即greater-equal，匹配的IP地址掩码长度的下限值

le

即less-equal，匹配的IP地址掩码长度的上限值

【相关命令】

·**ip prefix-list**

·**reset ip prefix-list**

**路由策略 \-- IPv4路由策略配置命令 \-- if-match ip**

------------------------------------------------------------------------

**[if-match ip**]命令用来配置IPv4的路由信息的匹配条件。

**[undo if-match ip**]命令用来取消该配置。

【命令】

**[if-match ip**[ { **address** \| **next-hop** \| **route-source** } { **acl** *acl-number* \| **prefix-list** *prefix-list-name* }]]

**[undo if-match ip ****[address**[ \| **next-hop** \| **route-source** } [ **acl** \| **prefix-list** ]]]

【缺省情况】]

没有配置IPv4的路由信息的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[address**]：匹配IPv4路由信息的目的地址。

**[next-hop**]：匹配下一跳地址。

**[route-source**]：匹配路由发布的源地址。

**[acl ***acl-number*]：指定用于过滤的ACL号。对于**address**，*acl-number*的取值范围为2000～3999；对于**next-hop**和**route-source**，*acl-number*的取值范围为2000～2999。

**[prefix-list** *prefix-list-name*]：指定用于过滤的地址前缀列表名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一个if-match子句，允许下一跳地址匹配已存在的地址前缀列表p1的路由信息通过。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match ip next-hop prefix-list p1

**路由策略 \-- IPv4路由策略配置命令 \-- ip prefix-list**

------------------------------------------------------------------------

**[ip prefix-list**]命令用来配置一个IPv4地址前缀列表表项。

**[undo ip prefix-list**]命令用来删除一个IPv4地址前缀列表或其某个表项。

【命令】

**[ip prefix-list** *prefix-list-name* [ **index** *index-number*  { **deny** \| **permit** } *ip-address mask-length*  **greater-equal** *min-mask-length*   **less-equal** *max-mask-length* ]]

**[undo ip prefix-list** *prefix-list-name* [ **index** *index-number* ]]

【缺省情况】

没有配置IPv4地址前缀列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prefix-list-name*]：指定IPv4地址前缀列表名，为1～63个字符的字符串，区分大小写。

*[index-number*]：标识IPv4地址前缀列表中的一条表项，*index-number*小的表项先被匹配，取值范围为1～65535。

**[deny**]：指定所定义的IPv4地址前缀列表表项的匹配模式为拒绝模式。当指定为拒绝模式并且待过滤的IPv4地址在该表项指定的前缀范围内时，则该IPv4地址不能通过该表项的过滤，并且不会进行下一个表项的匹配，否则进入下一表项的匹配。

**[permit**]：指定所定义的IPv4地址前缀列表表项的匹配模式为允许模式。当指定为允许模式并且待过滤的IPv4地址在该表项指定的前缀范围内时，通过该表项的过滤不进入下一个节点的匹配；如待过滤的IPv4地址不在该表项指定的前缀范围内，则进行下一表项匹配。

*[ip-address mask-length*]：指定IPv4地址前缀和前缀长度，*mask-length*的取值范围为0～32。

*[min-mask-length*]、*max-mask-length*：如果IPv4地址和前缀长度都已匹配，则使用该参数来指定地址前缀长度范围。**greater-equal**的含义为"大于等于"，**less-equal**的含义为"小于等于"，其取值范围为*mask-length* \<= *min-mask-length* \<= *max-mask-length* \<= 32。如果只指定*min-mask-length*时，则前缀长度范围为 *min-mask-length*，32 ；如果只指定*max-mask-length*时，则前缀长度范围为 *mask-length*，*max-mask-length *；如果二者都指定，则前缀长度范围为 *min-mask-length*，*max-mask-length *。

【使用指导】

IPv4地址前缀列表用于IPv4地址的过滤。一个IPv4地址前缀列表可以有若干条表项，每一表项指定一个地址前缀范围。表项之间的过滤关系是"或"的关系，即通过一条表项的过滤就意味着通过该IPv4地址前缀列表的过滤。若没有通过任一表项的过滤，则不能通过该IPv4地址前缀列表的过滤。

需要注意的是：

·如果将*ip-address mask-length*指定为0.0.0.0 0，则只匹配缺省路由。

·如果需要匹配所有路由，则应配置为0.0.0.0 0 **less-equal** 32。

【举例】

\# 定义一条名为p1的IPv4地址前缀列表，只允许10.0.0.0/8网段的，掩码长度为17或18的路由通过。

\<Sysname\> system-view

Sysname ip prefix-list p1 permit 10.0.0.0 8 greater-equal 17 less-equal 18

【相关命令】

·**display ip prefix-list**

·**reset ip prefix-list**

**路由策略 \-- IPv4路由策略配置命令 \-- reset ip prefix-list**

------------------------------------------------------------------------

**[reset ip prefix-list**]命令用来清除指定的IPv4地址前缀列表的统计信息。

【命令】

**[reset ip prefix-list**]**** *prefix-list-name*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prefix-list-name*]：指定地址前缀列表的名称，为1～63个字符的字符串，区分大小写。如果未指定本参数，将清除所有的IPv4地址前缀列表的统计信息。

【举例】

\# 清除IPv4地址前缀列表abc的统计信息。

\<Sysname\> reset ip prefix-list abc

【相关命令】

·**display ip prefix-list**

·**ip prefix-list**

**路由策略 \-- IPv6路由策略配置命令 \-- apply ipv6 fast-reroute**

------------------------------------------------------------------------

![说明](路由策略命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply** **ipv6** **fast-reroute**]命令用来配置快速重路由备份。

**[undo apply****ipv6 fast-reroute**]命令用来取消快速重路由配置。

【命令】

**[apply** **ipv6** **fast-reroute backup-nexthop** *ipv6-address*]

**[undo apply ipv6** **fast-reroute**]

【缺省情况】

没有配置快速重路由。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[backup-nexthop*** ipv6-address*]：备份下一跳IPv6地址。

【使用指导】

当网络中的链路或某台路由器发生故障时，需要通过故障链路或故障路由器传输才能到达目的地的报文将会丢失或产生路由环路，数据流量将会被中断，直到路由协议根据新的拓扑网络路由收敛完毕后，被中断的流量才能恢复正常的传输。

网络管理员可以为路由协议配置快速重路由功能，路由协议将通过路由策略为路由指定备份下一跳，当路由器探测到网络故障时，路由协议会使用事先指定好的备份下一跳替换失效下一跳，通过备份下一跳来指导报文的转发，从而大大缩短了流量中断时间。

网络管理员可以在路由策略中配置快速重路由功能的指定备份下一跳，为符合过滤条件的路由指定备份下一跳。

【举例】

\# 创建一个名为policy1的路由策略，为到达目的地100::1/64的路由配置备份下一跳地址为1::1/64。

\<Sysname\> system-view

Sysname ipv6 prefix-list abc index 10 permit 100::1 64

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match ipv6 address prefix-list abc

Sysname-route-policy-policy1-10 apply ipv6 fast-reroute backup-nexthop 1::1

**路由策略 \-- IPv6路由策略配置命令 \-- apply ipv6 next-hop**

------------------------------------------------------------------------

**[apply ipv6 next-hop**]命令用来配置IPv6路由信息的下一跳地址。

**[undo apply ipv6 next-hop**]命令用来恢复缺省情况。

【命令】

**[apply ipv6 next-hop**] *ipv6-address*

**[undo apply ipv6 next-hop**]

【缺省情况】

没有配置IPv6路由信息的下一跳地址。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：指定下一跳IPv6地址。

【使用指导】

引入路由时，使用**apply ipv6 next-hop**命令设置下一跳地址无效。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。如果匹配已存在的编号为1的as-path，那么配置路由的下一跳地址为3ffe:506::1。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match as-path 1

Sysname-route-policy-policy1-10 apply ipv6 next-hop 3ffe:506::1

**路由策略 \-- IPv6路由策略配置命令 \-- display ipv6 prefix-list**

------------------------------------------------------------------------

**[display ipv6 prefix-list**]命令用来显示IPv6地址前缀列表的统计信息。

【命令】

**[display ipv6 prefix-list** [ **name** *prefix-list-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name** *prefix-list-name*]：指定IPv6地址前缀列表的名称，为1～63个字符的字符串，区分大小写。如果未指定本参数，将显示所有配置的IPv6地址前缀列表的统计信息。

【举例】

\# 显示所有IPv6地址前缀列表的统计信息。

\<Sysname\> display ipv6 prefix-list

Prefix-list6: 666

 Permitted 0

 Denied 0

         index: 10        permit 6::/64                  ge  66  le  88

表1-6 display ipv6 prefix-list命令显示信息描述表

字段

描述

Prefix-list6

IPv6地址前缀列表的名字

Permitted

符合匹配条件的路由个数

Denied

不符合匹配条件的路由个数

index

地址前缀列表的内部序列号

permit

匹配模式，有两种取值：

·permit：表示允许

·deny：表示拒绝

6::/64

匹配的IPv6 地址和前缀长度

ge

即greater-equal，匹配的IPv6前缀长度的下限值

le

即less-equal，匹配的IPv6前缀长度的上限值

【相关命令】

·**ip****v6 prefix-list**

·**reset ip****v6 prefix-list**

**路由策略 \-- IPv6路由策略配置命令 \-- if-match ipv6**

------------------------------------------------------------------------

**[if-match** **ipv6**]命令用来配置IPv6的路由信息的匹配条件。

**[undo if-match ipv6**]命令用来恢复取消该配置。

【命令】

**[if-match ipv6**[ { **address** \| **next-hop** \| **route-source** } { **acl** *acl6-number* \| **prefix-list** *prefix-list-name* }]]

**[undo if-match ipv6**[ { **address** \| **next-hop** \| **route-source** } [ **acl** \| **prefix-list** ]]]

【缺省情况】

没有配置IPv6的路由信息的匹配条件。

【视图】

路由策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[address**]：匹配IPv6路由信息的目的地址。

**[next-hop**]：匹配IPv6路由信息的下一跳。

**[route-source**]：匹配IPv6路由信息的源地址。

**[acl ***acl6-number*]：指定用于过滤的IPv6 ACL号。对于**address**，*acl6-number*的取值范围为2000～3999；对于**next-hop**和**route-source**，*acl6-number*的取值范围为2000～2999。

**[prefix-list** *prefix-list-name*]：指定用于过滤的IPv6地址前缀列表的名称，为1～63个字符的字符串，区分大小写。

【举例】

\# 创建一个名为policy1的路由策略，其节点序列号为10，匹配模式为permit。定义一条if-match子句，允许下一跳地址匹配已存在的IPv6地址前缀列表p1的路由信息通过。

\<Sysname\> system-view

Sysname route-policy policy1 permit node 10

Sysname-route-policy-policy1-10 if-match ipv6 next-hop prefix-list p1

**路由策略 \-- IPv6路由策略配置命令 \-- ipv6 prefix-list**

------------------------------------------------------------------------

**[ipv6 prefix-list**]命令用来配置IPv6地址前缀列表表项。

**[undo ipv6 prefix-list**]命令用来删除IPv6地址前缀列表或其中某个表项。

【命令】

**[ipv6 prefix-list ***prefix-list-name *[ **index** *index-number*  { **deny** \| **permit** } *ipv6-address prefix-length*  **greater-equal** *min-prefix-length*   **less-equal** *max-prefix-length* ]]

**[undo ipv6 prefix-list***prefix-list-name* [ **index** *index-number* ]]

【缺省情况】

没有配置IPv6地址前缀列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prefix-list-name*]：指定IPv6地址前缀列表名，为1～63个字符的字符串，区分大小写。

*[index-number*]：标识IPv6地址前缀列表中的一条表项，*index-number*小的表项先被匹配，取值范围为1～65535。

**[deny**]：指定所定义的IPv6地址前缀列表表项的匹配模式为拒绝模式。当指定为拒绝模式并且待过滤的IPv6地址在该表项指定的前缀范围内时，则该IPv6地址不能通过该表项的过滤，并且不会进行下一个表项的匹配，否则进入下一表项的匹配。

**[permit**]：指定所定义的IPv6地址前缀列表表项的匹配模式为允许模式。当指定为允许模式并且待过滤的IPv6地址在该表项指定的前缀范围内时，通过该表项的过滤不进入下一个节点的匹配；如待过滤的IPv6地址不在该表项指定的前缀范围内，则进行下一表项匹配。

*[ipv6-address prefix-length*]：指定IPv6地址前缀和前缀长度，当指定为:: 0时匹配缺省路由，*prefix-length*的取值范围为0～128。

**[greater-equal ***min-prefix-length*]：大于等于最小前缀长度。

**[less-equal** *max-prefix-length*]：小于等于最大前缀长度。

前缀长度范围可以表达为*prefix-length* \<= *min-prefix-length* \<= *max-prefix-length* \<= 128。如果只指定了*min-prefix-length*，则前缀范围为 *min-prefix-length*，128 ；如果只指定了*max-prefix-length*，则前缀范围为 *prefix-length*，*max-prefix-length *；如果二者都指定，则前缀范围为 *min-prefix-length*，*max-prefix-length* 。

【使用指导】

IPv6地址前缀列表用于IPv6地址过滤。一个IPv6地址前缀列表可包含多个表项，一个表项指定一个地址前缀范围。表项之间的过滤关系是"或"，即通过一个表项就可通过该IPv6地址前缀列表的过滤。没有通过任何一个表项的过滤就意味着没有通过该IPv6地址前缀列表的过滤。

需要注意的是：

·如果将*ipv6-address prefix-length*指定为:: 0，则只匹配缺省路由。

·如果需要匹配所有路由，则应配置为:: 0 **less-equal** 128。

【举例】

\# 配置一条IPv6地址前缀列表，允许前缀长度在32位到64位之间的IPv6地址通过。

\<Sysname\> system-view

Sysname ipv6 prefix-list abc permit :: 0 greater-equal 32 less-equal 64

\# 配置一条IPv6地址前缀列表，拒绝地址前缀为3FFE:D00::/32，前缀长度大于等于32位的IPv6地址通过。

\<Sysname\> system-view

Sysname ipv6 prefix-list abc deny 3FFE:D00:: 32 less-equal 128

【相关命令】

·**display ip****v6 prefix-list**

·**reset ip****v6 prefix-list**

**路由策略 \-- IPv6路由策略配置命令 \-- reset ipv6 prefix-list**

------------------------------------------------------------------------

**[reset ipv6 prefix-list**]命令用来清除指定的IPv6地址前缀列表的统计信息。

【命令】

**[reset ipv6 prefix-list**]**** *prefix-list-name*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prefix-list-name*]：指定地址前缀列表的名称。该名称必须唯一，为1～63个字符的字符串，区分大小写。如果未指定本参数，将清除所有的IPv6地址前缀列表的统计信息。

【举例】

\# 清除指定IPv6地址前缀列表的统计信息。

\<Sysname\> reset ipv6 prefix-list abc

【相关命令】

·**display ip****v6 prefix-list**

·**ip****v6 prefix-list**

****
