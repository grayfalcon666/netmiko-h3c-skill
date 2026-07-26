
**HQoS \-- 转发类配置命令 \-- display qos forwarding-class**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display qos forwarding-class**]命令用来显示转发类的信息。

【命令】

**[display qos forwarding-class** [ **name** *fc-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[fc-name*]：转发类的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有转发类的信息。

【举例】

\# 显示指定转发类的信息。

\<Sysname\> display qos forwarding-class name BE

Forwarding class: BE, ID: 0

\# 显示所有转发类的信息。

\<Sysname\> display qos forwarding-class

Forwarding class: BE, ID: 0

Forwarding class: AF, ID: 1

Forwarding class: EF, ID: 2

Forwarding class: NC, ID: 3

表1-1 display qos forwarding-class命令显示信息描述表

字段

描述

Forwarding class

转发类的名称

ID

转发类的ID

**HQoS \-- 转发类配置命令 \-- remark forwarding-class**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[remark forwarding-class**]命令用来重新标记流所属的转发类。

**[undo remark forwarding-class**]命令用来取消重新标记操作。

【命令】

**[remark forwarding-class**[ { **id** *fc-id* \| **name** *fc-name* }]]

**[undo remark forwarding-class**]

【缺省情况】

未配置重标记转发类功能。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[id** *[fc-id*]]：转发类索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。此转发类索引只能是系统预定义转发类的索引。

**[name** *[fc-name*]]：转发类名称，为1～31个字符的字符串，区分大小写。此转发类只能是系统预定义转发类。

【使用指导】

如果同一个流行为中多次配置重标记转发类，那么最后一次的配置生效。

【举例】

\# 重新标记流所属的转发类为BE。

\<Sysname\> system-view

Sysname traffic behavior testtb

Sysname-behavior-testtb remark forwarding-class name BE

**HQoS \-- 转发组配置命令 \-- display qos forwarding-group**

------------------------------------------------------------------------

**[display qos forwarding-group**]命令用来显示转发组的信息。

【命令】

**[display qos forwarding-group** [ **name** *fg-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[fg-name*]：转发组的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有转发组的信息。

【举例】

\# 显示指定转发组的信息，转发组下嵌套转发组。

\<Sysname\> display qos forwarding-group name testfg1

Forwarding group: testfg1, ID: 10

 match service-vlan-id 1 to 10

  Forwarding group: subfg1, ID: 1, profile: fgprofile1

 match service-vlan-id 11 to 20

  Forwarding group: subfg2, ID: 2, profile: fgprofile2

\# 显示指定转发组的信息，转发组下嵌套转发类。

\<Sysname\> display qos forwarding-group name testfg2

Forwarding group: testfg2, ID: 10

 Forwarding class: BE, ID: 0, profile: fcprofile1

 Forwarding class: AF, ID: 1, profile: fcprofile2

 Forwarding class: EF, ID: 2, profile: fcprofile3

 Forwarding class: NC, ID: 3, profile: fcprofile4

表1-2 display qos forwarding-group命令显示信息描述表

字段

描述

Forwarding group

转发组的名称

Forwarding class

转发类的名称

ID

转发组或转发类的ID

match

match方式实例化

profile

转发策略的名称

**HQoS \-- 转发组配置命令 \-- forwarding-class profile**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[forwarding-class** **profile**]命令用来配置转发组嵌套一个转发类，并为该转发类指定转发策略。

**[undo forwarding-class**]命令用来取消转发组嵌套的转发类。

【命令】

**[forwarding-class** *fc-name* **profile** *fp-name*]

**[undo forwarding-class** *fc-name*]

【缺省情况】

自定义转发组不嵌套转发类。

【视图】

转发组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fc-name*]：转发类名称，为1～31个字符的字符串，区分大小写，此转发类只能是系统预定义转发类。

**[profile*** fp-name*]：转发策略名称，为1～31个字符的字符串，区分大小写。

【使用指导】

预定义转发组下默认嵌套的转发类不允许修改与删除。

在转发组内嵌套转发类时需要保证转发类和对应的转发策略都已经存在。

转发组中已经嵌套转发组时不能再嵌套转发类。

【举例】

\# 在转发组testfg中嵌套转发类BE，并指定转发类BE的转发策略为testfp。

\<Sysname\> system-view

Sysname qos forwarding-group testfg

Sysname-hqos-fg-testfg forwarding-class BE profile testfp

**HQoS \-- 转发组配置命令 \-- forwarding-group profile**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[forwarding-group** profile]命令用来在转发组指定匹配规则中嵌套一个转发组，并为该转发组指定转发策略。

**[undo forwarding-group**]命令用来从转发组指定匹配规则下取消嵌套指定的转发组。

【命令】

**[forwarding-group** *sub-fg-name* **profile** *fp-name*]

**[undo forwarding-group** *sub-fg-name*]

【缺省情况】

自定义转发组下不嵌套转发组。

【视图】

转发组匹配规则视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[sub-fg-name*]：子转发组名称，为1～31个字符的字符串，区分大小写。

**[profile*** fp-name*]：转发策略名称，为1～31个字符的字符串，区分大小写。

【使用指导】

在转发组内嵌套转发组时需要保证转发组和对应的转发策略都已经存在。

转发组中已经嵌套转发类时不能再嵌套转发组。

已经嵌套了转发组的转发组不能被其他转发组嵌套。

【举例】

\# 在转发组testfg中指定匹配Service VLAN ID 2的流量嵌套转发组subfg，并指定转发组subfg的转发策略为testfp。

\<Sysname\> system-view

Sysname qos forwarding-group testfg

Sysname-hqos-fg-testfg match service-vlan-id 2

Sysname-hqos-fg-testfg-match forwarding-group subfg profile testfp

**HQoS \-- 转发组配置命令 \-- match**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[match**]命令用来配置转发组的匹配规则，并进入匹配规则视图。

**[undo match**]命令用来取消转发组的匹配规则。

【命令】

**[match** *match-criteria*]

**[undo match** *match-criteria*]

【缺省情况】

自定义转发组下无匹配规则。

【视图】

转发组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-criteria*]：转发组的匹配规则，具体情况如[表]1-3(?461028519#_Ref360725646)所示。

表1-3 转发组的匹配规则取值

取值

描述

service-vlan-id *vlan-id-list*

定义匹配运营商网络VLAN ID的规则

*[vlan-id-list*]：VLAN列表，表示方式为*vlan-id-list *[= { *vlan-id* \| *vlan-id1* **to** *vlan-id2* }&\<1-8\>]，*vlan-id*、*vlan-id1*、*vlan-id2*的取值范围为1～4094，且*vlan-id1*必须小于或等于*vlan-id2*；&\<1-8\>表示前面的参数最多可以重复输入8次

local-precedence *precedence-value-list*

定义匹配本地优先级的规则

*[precedence-value-list*]*：*本地优先级列表，表示方式为*precedence-value-list*[ = { *precedence-value* \| *precedence-value1* **to** *precedence-value2* }&\<1-8\>]，*precedence-value*、*precedence-value1*、*precedence-value2*的取值范围为0～7，且*precedence-value1*必须小于或等于*precedence-value2*；&\<1-8\>表示前面的参数最多可以重复输入8次

dot1p *dot1p-value-list*

定义匹配运营商网络802.1p优先级的规则

*[dot1p-value-list*]：802.1p优先级列表，表示方式为*dot1p-value-list *[= { *dot1p-value* \| *dot1p-value1* **to** *dot1p-value2* }&\<1-8\>]，*dot1p-value*、*dot1p-value1*、*dot1p-value2*的取值范围为0～7，且*dot1p-value1*必须小于或等于*dot1p-value2*；&\<1-8\>表示前面的参数最多可以重复输入8次

qos-local-id *local-id-list*

定义匹配QoS本地ID值的规则

*[local-id-list*]：QoS本地ID值列表，表示方式为*local-id-list *[= { *local-id* \| *local-id1* **to** *local-id2* }&\<1-8\>]，*local-id*、*local-id1*、*local-id2*的取值范围为1～4095，且*local-id1*必须小于或等于*local-id2*；&\<1-8\>表示前面的参数最多可以重复输入8次

【使用指导】

配置匹配规则只是进入视图，并不实际生成配置，仅当在匹配规则下进一步配置嵌套的子转发组后，匹配规则配置才真正生效。

删除匹配规则会同时删除匹配规则下嵌套的子转发组及其关联的转发策略。

【举例】

\# 指定转发组按匹配规则进入配置视图。

\<Sysname\> system-view

Sysname qos forwarding-group testfg

Sysname-hqos-fg-testfg match service-vlan-id 2

Sysname-hqos-fg-testfg-match

【相关命令】

·{.TerminalDisplayshading}**forwarding-group profile** (scheduler-policy match view)

**HQoS \-- 转发组配置命令 \-- qos forwarding-group**

------------------------------------------------------------------------

**[qos forwarding-group**]命令用来创建用户自定义的转发组，并进入该转发组视图。

**[undo qos forwarding-group**]命令用来删除用户自定义的转发组。

【命令】

**[qos** **forwarding-group** *fg-name*]

**[undo qos** **forwarding-group** *fg-name*]

【缺省情况】

不存在自定义转发组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fg-name*]：自定义转发组的名称，为1～31个字符的字符串，区分大小写。自定义的转发组名称不能使用系统预定义的转发组的名称。

【使用指导】

系统有一个预定义的转发组，名称为default，ID为0，不允许修改和删除。

系统最多支持创建的转发组个数为8191。

如果转发组已经被其他转发组或调度策略嵌套，需要先取消嵌套关系才能删除。

【举例】

\# 创建自定义转发组。

\<Sysname\> system-view

Sysname qos forwarding-group testfg

Sysname-fg-testfg

**HQoS \-- 丢弃策略配置命令 \-- display qos drop-profile**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display qos drop-profile**]命令用来显示丢弃策略的信息。

【命令】

**[display qos drop-profile**  **name** *dp-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[dp-name*]：丢弃策略的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有丢弃策略的信息。

【举例】

\# 显示指定丢弃策略testdp的信息。

\<Sysname\> display qos drop-profile name testdp

Drop profile: testdp, ID: 10

 Green thresholds: 50/60/30(min/max/prob)

 Yellow thresholds: 50/60/30(min/max/prob)

 Red thresholds: 50/60/30(min/max/prob)

 Weighting constant: 2

表1-4 display qos drop-profile命令显示信息描述表

字段

描述

Drop profile

丢弃策略的名称

ID

丢弃策略ID

Green thresholds

绿色报文的丢弃参数

Yellow thresholds

黄色报文的丢弃参数

Red thresholds

红色报文的丢弃参数

min/max/prob

开始丢弃的队列门限/完全丢弃的队列门限/丢弃斜率

Weighting constant

计算平均队列长度的指数

**HQoS \-- 丢弃策略配置命令 \-- green**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[green**]命令用来配置绿色报文的丢弃参数。

**[undo green**]命令用来恢复缺省情况。

【命令】

**[green** **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]

**[undo green**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

丢弃策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[low-limit*** low-limit*]：开始丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

**[high-limit*** high-limit*]：完全丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。完全丢弃的队列门限值要大于开始丢弃的队列门限值。

**[discard-probability*** discard-prob*]：丢弃斜率。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【使用指导】

当配置*discard-prob*等于100时，则成为尾丢弃。

【举例】

\# 指定绿色报文的丢弃参数，开始丢弃的队列门限为500，完全丢弃的队列门限为700，丢弃斜率为40。

\<Sysname\> system-view

Sysname qos drop-profile testdp

Sysname-hqos-dp-testdp green low-limit 500 high-limit 700 discard-probability 40

**HQoS \-- 丢弃策略配置命令 \-- qos drop-profile**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[qos drop-profile**]命令用来创建用户自定义的丢弃策略，并进入该丢弃策略视图。

**[undo qos drop-profile**]命令用来删除用户自定义的丢弃策略。

【命令】

**[qos drop-profile** *dp-name*]

**[undo qos drop-profile** *dp-name*]

【缺省情况】

不存在自定义丢弃策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dp-name*]：自定义丢弃策略名称，为1～31个字符的字符串，区分大小写。自定义的丢弃策略名称不能使用系统预定义的丢弃策略名称。

【使用指导】

系统有一个预定义的丢弃策略，名称为default，ID为0，不允许修改和删除。

如果丢弃策略已经被转发策略引用，需要先取消引用才能删除。

【举例】

\# 创建自定义丢弃策略。

\<Sysname\> system-view

Sysname qos drop-profile testdp

Sysname-dp-testdp

**HQoS \-- 丢弃策略配置命令 \-- red**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[red**]命令用来配置红色报文的丢弃参数。

**[undo red**]命令用来恢复缺省情况。

【命令】

**[red** **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]

**[undo red**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

丢弃策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[low-limit*** low-limit*]：开始丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

**[high-limit*** high-limit*]：完全丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。完全丢弃的队列门限值要大于开始丢弃的队列门限值。

**[discard-probability*** discard-prob*]：丢弃斜率。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【使用指导】

当配置*discard-prob*等于100时，则成为尾丢弃。

【举例】

\# 指定红色报文的丢弃参数。

\<Sysname\> system-view

Sysname qos drop-profile testdp

Sysname-hqos-dp-testdp red low-limit 500 high-limit 700 discard-probability 40

**HQoS \-- 丢弃策略配置命令 \-- weighting-constant**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[weighting-constant**]命令用来配置计算平均队列长度的指数。

**[undo weighting-constant**]命令用来恢复缺省情况。

【命令】

**[weighting-constant ***exponent*]

**[undo weighting-constant**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

丢弃策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[exponent*]：表示计算平均队列长度的指数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【使用指导】

平均队列长度的指数越大，计算平均队列长度时对队列的实时变化越不敏感。

【举例】

\# 指定丢弃策略的计算平均队列长度的指数。

\<Sysname\> system-view

Sysname qos drop-profile testdp

Sysname-hqos-dp-testdp weighting-constant 2

**HQoS \-- 丢弃策略配置命令 \-- yellow**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[yellow**]命令用来配置黄色报文的丢弃参数。

**[undo** **yellow**]命令用来恢复缺省情况。

【命令】

**[yellow** **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]

**[undo yellow**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

丢弃策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[low-limit*** low-limit*]：开始丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

**[high-limit*** high-limit*]：完全丢弃的队列门限，即队列中的报文个数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。完全丢弃的队列门限值要大于开始丢弃的队列门限值。

**[discard-probability*** discard-prob*]：丢弃斜率。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【使用指导】

当配置*discard-prob*等于100时，则成为尾丢弃。

【举例】

\# 指定黄色报文的丢弃参数。

\<Sysname\> system-view

Sysname qos drop-profile testdp

Sysname-hqos-dp-testdp yellow low-limit 500 high-limit 700 discard-probability 40

**HQoS \-- 转发策略配置命令 \-- bandwidth**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[bandwidth**]命令用来配置转发策略的最小带宽保证。

**[undo bandwidth**]命令用来取消配置转发策略的最小带宽保证。

【命令】

**[bandwidth ***bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

自定义转发策略不存在最小带宽保证配置。

【视图】

转发策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：最小保证带宽，单位为kbps。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置转发策略testfp的最小带宽保证为2000kbps。

\<Sysname\> system-view

Sysname qos forwarding-profile testfp

Sysname-hqos-fp-testfp bandwidth 2000

**HQoS \-- 转发策略配置命令 \-- display qos forwarding-profile**

------------------------------------------------------------------------

**[display qos forwarding-profile**]命令用来显示转发策略的信息。

【命令】

**[display qos forwarding-profile** [ **name** *fp-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[fp-name*]：转发策略的名称，1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有转发策略的信息。

【举例】

\# 显示指定转发策略testfp的信息。

\<Sysname\> display qos forwarding-profile name testfp

Forwarding profile: testfp, ID: 10

 GTS: CIR 100(kbps), CBS 50(Bytes), EBS 100(Bytes), PIR 150(kbps)

 WRR: priority 2, weight 1

 Bandwidth: 1000(kbps)

 Drop profile: default

表1-5 display qos forwarding-profile命令显示信息描述表

字段

描述

Forwarding profile

转发策略的名称

ID

转发策略的ID

CIR

承诺信息速率

CBS

承诺突发尺寸

EBS

超额突发尺寸

PIR

峰值信息速率

WRR

加权轮循队列调度

priority

调度优先级

weight

调度权重

Bandwidth

最小保证带宽

Drop profile

丢弃策略的名称

**HQoS \-- 转发策略配置命令 \-- drop-profile**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[drop-profile**]命令用来将丢弃策略绑定到转发策略。

**[undo drop-profile**]命令用来将丢弃策略从转发策略中删除。

【命令】

**[drop-profile** *dp-name*]

**[undo drop-profile**]

【缺省情况】

自定义转发策略中不引用丢弃策略，对所有报文进行尾丢弃。

【视图】

转发策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dp-name*]：丢弃策略名称，为1～31个字符的字符串，区分大小写。

【使用指导】

在转发策略下绑定丢弃策略时对应的丢弃策略必须存在。

【举例】

\# 将丢弃策略testdp绑定到转发策略testfp。

\<Sysname\> system-view

Sysname qos forwarding-profile testfp

Sysname-hqos-fp-testfp drop-profile tetsdp

**HQoS \-- 转发策略配置命令 \-- gts cir**

------------------------------------------------------------------------

**[gts**]命令用来配置转发策略的流量整形参数。

**[undo gts**]命令用来取消配置转发策略的整形参数。

【命令】

**[gts cir** *cir-value* [ **cbs** *cbs-value* [ **ebs** *ebs-value*  ]  **pir** *pir-value* ]]

**[undo gts**]

【缺省情况】

转发策略中不存在流量整形配置，不对速率进行限制。

【视图】

转发策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cir-value*]：承诺带宽值，单位为kbps。

**[cbs** *cbs-value*]：承诺突发尺寸。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。如果设备未指定缺省值，该缺省值为500毫秒内以CIR速率通过的流量，单位为bytes。

**[ebs** *ebs-value*]：超额突发尺寸，在双令牌桶算法中超出承诺突发流量的部分，单位为bytes。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。如果设备未指定缺省值，该缺省值为0。

**[pir** *pir-value*]：峰值带宽值，单位为kbps。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。不配置峰值带宽值表示是单令牌桶流量监管。

【举例】

\# 配置转发策略testfp的流量整形参数。

\<Sysname\> system-view

Sysname qos forwarding-profile testfp

Sysname-hqos-fp-testfp gts cir 1000 cbs 1000 pir 2000

**HQoS \-- 转发策略配置命令 \-- qos forwarding-profile**

------------------------------------------------------------------------

**[qos forwarding-profile**]命令用来创建用户自定义的转发策略，并进入该转发策略视图。

**[undo qos forwarding-profile**]命令用来删除用户自定义的转发策略。

【命令】

**[qos forwarding-profile** *fp-name*]

**[undo qos forwarding-profile** *fp-name*]

【缺省情况】

系统中不存在自定义转发策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fp-name*]：自定义转发策略名称，为1～31个字符的字符串，区分大小写。自定义的转发策略名称不能使用系统预定义的转发策略名称。

【使用指导】

系统预定义的转发策略不允许修改和删除。

如果转发策略已经被转发组或调度策略嵌套，需要先取消嵌套关系才能删除。

【举例】

\# 创建自定义转发策略。

\<Sysname\> system-view

Sysname qos forwarding-profile testfp

**HQoS \-- 转发策略配置命令 \-- sp**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[sp**]命令用来配置转发策略的队列调度方式为严格优先级调度。

**[undo sp**]命令用来取消配置转发策略的严格优先级队列调度方式。

【命令】

**[sp**]

**[undo sp**]

【缺省情况】

自定义转发策略不存在sp配置。

【视图】

转发策略视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置转发策略testfp的队列调度方式为严格优先级调度。

\<Sysname\> system-view

Sysname qos forwarding-profile testfp

Sysname-hqos-fp-testfp sp

**HQoS \-- 转发策略配置命令 \-- wfq**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[wfq**]命令用来配置转发策略队列调度方式是加权公平队列调度。同一优先级的队列按照权重调度，权重决定调度该队列时应该占用的带宽比例。

**[undo wfq**]命令用来取消配置转发策略的加权公平队列调度方式。

【命令】

**[wfq ** **priority** *priority-value* ]  **weight** *weight-value*

**[undo wfq**]

【缺省情况】

自定义转发策略不存在wfq配置。

【视图】

转发策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[priority*** priority-value*]：调度优先级，取值范围为1～设备支持的最大值，不同型号的设备支持的最大值不同，请以设备的实际情况为准。缺省值为最低优先级1。

**[weight*** weight-value*]：调度权重，取值范围为1～设备支持的最大值，不同型号的设备支持的最大值不同，请以设备的实际情况为准。缺省值为最小权重1。

【举例】

\# 配置转发策略testfp的队列调度方式为加权公平调度，调度优先级为3，调度权重为2。

\<Sysname\> system-view

Sysname qos forwarding-profile testfp

Sysname-hqos-fp-testfp wfq priority 3 weight 2

**HQoS \-- 转发策略配置命令 \-- wrr**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[wrr**]命令用来配置转发策略的队列调度方式是加权轮循调度。同一优先级的队列按照权重调度，权重决定调度该队列时应该占用的带宽比例。

**[undo wrr**]命令用来取消配置转发策略的加权轮询队列调度方式。

【命令】

**[wrr ** **priority** *priority-value* ]  **weight** *weight-value*

**[undo wrr**]

【缺省情况】

自定义转发策略不存在WRR配置。

【视图】

转发策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[priority*** priority-value*]：调度优先级，取值范围为1～设备支持的最大值，不同型号的设备支持的最大值不同，请以设备的实际情况为准。缺省值为最低优先级1。

**[weight*** weight-value*]：调度权重，取值范围为1～设备支持的最大值，不同型号的设备支持的最大值不同，请以设备的实际情况为准。缺省值为最小权重1。

【举例】

\# 配置转发策略testfp的队列调度方式为加权轮循调度。

\<Sysname\> system-view

Sysname qos forwarding-profile testfp

Sysname-hqos-fp-testfp wrr priority 3 weight 2

**HQoS \-- 调度策略配置命令 \-- display qos scheduler-policy**

------------------------------------------------------------------------

**[display qos scheduler-policy**]命令用来显示调度策略的信息。

【命令】

**[display qos scheduler-policy ** **name** *sp-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[sp-name*]：调度策略的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有调度策略的信息。

【举例】

\# 显示指定调度策略的信息。

\<Sysname\> display qos scheduler-policy name test_sp

SP \-- Scheduler policy      FG \-- Forwarding group     FC \-- Forwarding class

FP \-- Forwarding profile    L  \-- Layer

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SP: test_sp(1)

[ \|  Scheduler unit: weight]

[ \|]

[ \|  Match: group]

 +\--FG(L1): default(0)

[ \|   \|      FP: default(0)]

[ \|   \| ]

[ \|   +\--FC: BE(0)]

[ \|   \|      FP: default(0)]

[ \|   \|]

[ \|   +\--FC: AF(1)]

[ \|   \|      FP: default(0)]

[ \|   \|]

[ \|   +\--FC: EF(2)]

[ \|   \|      FP: default(0)]

[ \|   \|]

[ \|   +\--FC: NC(3)]

[ \|          FP: default(0)]

[ \|  ]

[ \|  Match: group]

 +\--FG(L1): VOIP(1)

[ \|   \|      FP: VOIP(2)]

[ \|   \| ]

[ \|   \|  Match: service-vlan-id 2 to 10]

[ \|   +\--FG(L2): Customer1(2)]

[ \|   \|   \|      FP: Customer1(1)]

[ \|   \|   \| ]

[ \|   \|   +\--FC: BE(0)]

[ \|   \|   \|      FP: BE(3)]

[ \|   \|   \|]

[ \|   \|   +\--FC: AF(1)]

[ \|   \|   \|      FP: default(0)]

[\|   \|   \|]

[ \|   \|   +\--FC: EF(2)]

[ \|   \|   \|      FP: default(0)]

[ \|   \|   \|]

[ \|   \|   +\--FC: NC(3)]

[ \|   \|          FP: default(0)]

[ \|   \|  ]

[ \|   \|  Match: service-vlan-id 11 to 20]

[ \|   +\--FG(L2): Customer2(5)]

[ \|       \|      FP: Customer2(2)]

[ \|       \|]

[ \|       +\--FC: BE(0)]

[ \|       \|      FP: BE(3)]

[ \|       \|]

[ \|       +\--FC: AF(1)]

[ \|       \|      FP: default(0)]

[ \|       \|]

[ \|       +\--FC: EF(2)]

[ \|       \|      FP: default(0)]

[ \|       \|]

[ \|       +\--FC: NC(3)]

[ \|              FP: default(0)]

[ \|   ]

[ \|  Match: group]

 +\--FG(L1): INTERNET(4)

[     \|      FP: INTERNET(4)]

[     \|]

[     \|  Match: service-vlan-id 21 to 30]

     +\--FG(L2): Customer3(6)

[         \|      FP: Customer3(6)]

[         \| ]

         +\--FC: BE(0)

[         \|      FP: BE(3)]

[         \|]

         +\--FC: AF(1)

[         \|      FP: default(0)]

[         \|]

         +\--FC: EF(2)

[         \|      FP: default(0)]

[         \|]

         +\--FC: NC(3)

                FP: default(0)

表1-6 display qos scheduler-policy命令显示描述信息表

字段

描述

Scheduler policy

调度策略的名称

Forwarding group

转发组的名称

Forwarding class

转发类的名称

Forwarding profile

转发策略的名称

Layer

层次的名称

Scheduler unit

调度策略的调度单位

match

match方式实例化

group

group方式实例化

service-vlan-id

实例化匹配规则

括号内的数字

前方对应字段（转发类/转发组/转发策略/调度策略）名称的索引

**HQoS \-- 调度策略配置命令 \-- display qos scheduler-policy diagnosis interface**

------------------------------------------------------------------------

**[display qos scheduler-policy diagnosis interface**]命令用来显示端口的诊断信息。

【命令】

**[display qos scheduler-policy diagnosis interface **[ *interface-type interface-number*  [ **inbound** \| **outbound** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-numb*er]：指定端口类型和端口号。

**[inbound**]：表示显示入方向的诊断信息。

**[outbound**]：表示显示出方向的诊断信息。

【使用指导】

如果未指定端口，将显示所有端口的诊断信息。

如果未指定方向，将显示出入两个方向的诊断信息。

【举例】

\# 显示指定端口入方向的诊断信息。

\<Sysname\> display qos scheduler-policy diagnosis interface gigabitethernet 1/0/1 inbound

SP \-- Scheduler policy      FG \-- Forwarding group     FC \-- Forwarding class

FP \-- Forwarding profile    L  \-- Layer

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Interface: GigabitEthernet1/0/1

Direction: Inbound

SP: test_sp(1)

[ \|]

[ \|  Match: group]

 +\--FG(L1): default(0)

[ \|   \|      FP: default(0)]

[ \|   \|      Status: Success]

[ \|   \| ]

[ \|   +\--FC: BE(0)]

[ \|   \|      FP: default(0)]

[ \|   \|      Status: Success]

[ \|   \| ]

[ \|   +\--FC: AF(1)]

[ \|   \|      FP: default(0)]

[ \|   \|      Status: Success]

[ \|   \| ]

[ \|   +\--FC: EF(2)]

[ \|   \|      FP: default(0)]

[ \|   \|      Status: Success]

[ \|   \|  ]

[ \|   +\--FC: NC(3)]

[ \|          FP: default(0)]

[ \|          Status: Success]

[ \|  ]

[ \|  Match: group]

 +\--FG(L1): VOIP(1)

[ \|   \|      FP: VOIP(2)]

[ \|   \|      Status: Success]

[ \|   \| ]

[ \|   \|  Match: service-vlan-id 2 to 10]

[ \|   +\--FG(L2): Customer1(2)]

[ \|   \|   \|      FP: Customer1(1)]

[ \|   \|   \|      Status: Success]

[ \|   \|   \| ]

[ \|   \|   +\--FC: BE(0)]

[ \|   \|   \|      FP: BE(3)]

[ \|   \|   \|      Status: Queue Failed]

[ \|   \|   \|  ]

[ \|   \|   +\--FC: AF(1)]

[ \|   \|   \|      FP: default(0)]

[ \|   \|   \|      Status: GTS Failed]

[ \|   \|   \|  ]

[ \|   \|   +\--FC: EF(2)]

[ \|   \|   \|      FP: default(0)]

[ \|   \|   \|      Status: Success]

[ \|   \|   \|  ]

[ \|   \|   +\--FC: NC(3)]

[ \|   \|          FP: default(0)]

[ \|   \|          Status: Success]

[ \|   \|  ]

[ \|   \|  Match: service-vlan-id 11 to 20]

[ \|   +\--FG(L2): Customer2(5)]

[ \|       \|      FP: Customer2(2)]

[ \|       \|      Status: Incomplete]

[ \|       \|]

[ \|       +\--FC: BE(0)]

[ \|       \|      FP: BE(3)]

[ \|       \|      Status: Incomplete]

[ \|       \|]

[ \|       +\--FC: AF(1)]

[ \|       \|      FP: default(0)]

[ \|       \|      Status: Incomplete]

[ \|       \|  ]

[ \|       +\--FC: NC(3)]

[ \|              FP: default(0)]

[ \|              Status: Incomplete]

[ \|   ]

[ \|  Match: group]

 +\--FG(L1): INTERNET(4)

[     \|      FP: INTERNET(4)]

[     \|      Status: Insufficent resources]

[     \|]

[     \|  Match: service-vlan-id 21 to 30]

     +\--FG(L2): Customer3(6)

[         \|      FP: Customer3(6)]

[         \|      Status: Insufficent resources]

[         \| ]

         +\--FC: BE(0)

[         \|      FP: BE(3)]

[         \|      Status: Insufficent resources]

[         \|         ]

         +\--FC: AF(1)

[         \|      FP: default(0)]

[         \|      Status: Insufficent resources]

[         \|]

         +\--FC: EF(2)

[         \|      FP: default(0)]

[         \|      Status: Insufficent resources]

[         \|]

         +\--FC: NC(3)

                FP: default(0)

Status: Insufficent resources

表1-7 display qos scheduler-policy diagnosis interface命令显示信息描述表

字段

描述

Interface

端口

Direction

方向

Scheduler policy

调度策略的名称

Forwarding group

转发组的名称

Forwarding class

转发类的名称

Forwarding profile

转发策略的名称

match

match方式实例化

service-vlan-id

实例化匹配规则

status

节点的下发状态

节点匹配规则不完整显示：Incomplete

所有内容下发成功显示：Success

下发未完全成功时显示下发失败的部分，失败的原因包括：

·Insufficientresources：表示硬件资源不足

·Conflicting match rule：match规则类型冲突

·Not support：配置不支持

·GTS Failed：表示转发类/转发组整形参数下发失败

·WRED Failed：表示转发类/转发组随机丢弃参数下发失败

·Queue Failed：表示转发类/转发组的队列调度下发失败

·Bandwidth Failed：表示转发类/转发组最小带宽保证下发失败

如果多个部分失败，则同时显示所有失败的部分。

**HQoS \-- 调度策略配置命令 \-- display qos scheduler-policy interface**

------------------------------------------------------------------------

**[display qos scheduler-policy interface**]命令用来显示端口的统计信息。

【命令】

**[display qos scheduler-policy interface** [ *interface-type interface-number*  [ **inbound** \| **outbound** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：指定端口类型和端口号。

**[inbound**]：表示显示入方向的统计信息。

**[outbound**]：表示显示出方向的统计信息。

【使用指导】

·如果未指定端口，将显示所有端口的统计信息。

·如果未指定方向，将显示出入两个方向的统计信息。

·如果没有使能端口统计功能，输入此命令将只显示端口上应用的调度策略信息，不显示流量统计信息。端口统计功能的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示指定端口入方向的统计信息。

\<Sysname\> display qos scheduler-policy interface gigabitethernet 1/0/1 inbound

SP \-- Scheduler policy      FG \-- Forwarding group     FC \-- Forwarding class

FP \-- Forwarding profile    L  \-- Layer

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Interface: GigabitEthernet1/0/1

Direction: Inbound

SP: test_sp(1)

[ \|]

[ \|  Match: group]

 +\--FG(L1): default(0)

[ \|   \|      FP: default(0)]

[\|   \|      Total queue length: 200 packets ]

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|      Dropped: 0 packets, 0 bytes]

[ \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|      Dropped red: 0 packets, 0 bytes ]

[\|   \|]

[ \|   +\--FC: BE(0)]

[ \|   \|      FP: default(0)]

[\|   \|      Total queue length: 200 packets ]

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|      Dropped: 0 packets, 0 bytes]

[ \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|      Dropped red: 0 packets, 0 bytes ]

[ \|   \|]

[ \|   +\--FC: AF(1)]

[ \|   \|      FP: default(0)]

[\|   \|      Total queue length: 200 packets ]

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|      Dropped: 0 packets, 0 bytes]

[ \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|      Dropped red: 0 packets, 0 bytes ]

[ \|   \| ]

[ \|   +\--FC: EF(2)]

[ \|   \|      FP: default(0)]

[\|   \|      Total queue length: 200 packets ]

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|      Dropped: 0 packets, 0 bytes]

[ \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|      Dropped red: 0 packets, 0 bytes ]

[ \|   \|  ]

[ \|   +\--FC: NC(3)]

[ \|          FP: default(0)]

[\|          Total queue length: 200 packets ]

[ \|          Current queue length: 0 packets, 0% use ratio ]

[ \|          Forwarded: 0 packets, 0 bytes ]

[ \|          Forwarded green: 0 packets, 0 bytes ]

[ \|          Forwarded yellow: 0 packets, 0 bytes ]

[ \|          Forwarded red: 0 packets, 0 bytes ]

[ \|          Tail dropped: 0 packets, 0 bytes ]

[ \|          Dropped: 0 packets, 0 bytes]

[ \|          Dropped green: 0 packets, 0 bytes ]

[ \|          Dropped yellow: 0 packets, 0 bytes ]

[ \|          Dropped red: 0 packets, 0 bytes ]

[ \|]

[ \|  Match: group]

 +\--FG(L1): VOIP(1)

[ \|   \|      FP: VOIP(2)]

[\|   \|      Total queue length: 200 packets ]

[ \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|      Dropped: 0 packets, 0 bytes]

[ \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|      Dropped red: 0 packets, 0 bytes ]

[ \|   \| ]

[ \|   \|  Match: service-vlan-id 2 to 10]

[ \|   +\--FG(L2): Customer1(2)]

[ \|   \|   \|      FP: Customer1(1)]

[\|   \|   \|      Total queue length: 200 packets ]

[ \|   \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped red: 0 packets, 0 bytes]

[\|   \|   \|]

[ \|   \|   +\--FC: BE(0)]

[ \|   \|   \|      FP: BE(3)]

[\|   \|   \|      Total queue length: 200 packets ]

[ \|   \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped red: 0 packets, 0 bytes]

[ \|   \|   \|  ]

[ \|   \|   +\--FC: AF(1)]

[ \|   \|   \|      FP: default(0)]

[\|   \|   \|      Total queue length: 200 packets ]

[ \|   \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped red: 0 packets, 0 bytes]

[ \|   \|   \|  ]

[ \|   \|   +\--FC: EF(2)]

[ \|   \|   \|      FP: default(0)]

[\|   \|   \|      Total queue length: 200 packets ]

[ \|   \|   \|      Current queue length: 0 packets, 0% use ratio ]

[ \|   \|   \|      Forwarded: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded green: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|   \|      Forwarded red: 0 packets, 0 bytes ]

[ \|   \|   \|      Tail dropped: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped green: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|   \|      Dropped red: 0 packets, 0 bytes]

[ \|   \|   \|  ]

[ \|   \|   +\--FC: NC(3)]

[ \|   \|          FP: default(0)]

[\|   \|          Total queue length: 200 packets ]

[ \|   \|          Current queue length: 0 packets, 0% use ratio ]

[ \|   \|          Forwarded: 0 packets, 0 bytes ]

[ \|   \|          Forwarded green: 0 packets, 0 bytes ]

[ \|   \|          Forwarded yellow: 0 packets, 0 bytes ]

[ \|   \|          Forwarded red: 0 packets, 0 bytes ]

[ \|   \|          Tail dropped: 0 packets, 0 bytes ]

[ \|   \|          Dropped: 0 packets, 0 bytes ]

[ \|   \|          Dropped green: 0 packets, 0 bytes ]

[ \|   \|          Dropped yellow: 0 packets, 0 bytes ]

[ \|   \|          Dropped red: 0 packets, 0 bytes]

[ \|   \|  ]

[ \|   \|  Match: service-vlan-id 11 to 20]

[ \|   +\--FG(L2): Customer2(5)]

[ \|       \|      FP: Customer2(2)]

[ \|       \|]

[ \|       +\--FC: BE(0)]

[ \|       \|      FP: BE(3)]

[ \|       \|]

[ \|       +\--FC: AF(1)]

[ \|       \|      FP: default(0)]

[ \|       \|  ]

[ \|       +\--FC: NC(3)]

[ \|              FP: default(0)]

[ \|   ]

[ \|  Match: group]

 +\--FG(L1): INTERNET(4)

[     \|      FP: INTERNET(4)]

[     \|      Total queue length: 200 packets ]

[     \|      Current queue length: 0 packets, 0% use ratio ]

[     \|      Forwarded: 0 packets, 0 bytes ]

[     \|      Forwarded green: 0 packets, 0 bytes ]

[     \|      Forwarded yellow: 0 packets, 0 bytes ]

[     \|      Forwarded red: 0 packets, 0 bytes ]

[     \|      Tail dropped: 0 packets, 0 bytes ]

[     \|      Dropped: 0 packets, 0 bytes ]

[     \|      Dropped green: 0 packets, 0 bytes ]

[     \|      Dropped yellow: 0 packets, 0 bytes ]

[     \|      Dropped red: 0 packets, 0 bytes]

[     \|]

[     \|  Match: service-vlan-id 21 to 30]

     +\--FG(L2): Customer3(6)

[         \|      FP: Customer3(6)]

[         \|      Total queue length: 200 packets ]

[         \|      Current queue length: 0 packets, 0% use ratio ]

[         \|      Forwarded: 0 packets, 0 bytes ]

[         \|      Forwarded green: 0 packets, 0 bytes ]

[         \|      Forwarded yellow: 0 packets, 0 bytes ]

[         \|      Forwarded red: 0 packets, 0 bytes ]

[         \|      Tail dropped: 0 packets, 0 bytes ]

[         \|      Dropped: 0 packets, 0 bytes ]

[         \|      Dropped green: 0 packets, 0 bytes ]

[         \|      Dropped yellow: 0 packets, 0 bytes ]

[         \|      Dropped red: 0 packets, 0 bytes]

[         \| ]

         +\--FC: BE(0)

[         \|      FP: BE(3)]

[\|      Total queue length: 200 packets ]

[\|      Current queue length: 0 packets, 0% use ratio ]

[\|      Forwarded: 0 packets, 0 bytes ]

[\|      Forwarded green: 0 packets, 0 bytes ]

[\|      Forwarded yellow: 0 packets, 0 bytes ]

[\|      Forwarded red: 0 packets, 0 bytes ]

[\|      Tail dropped: 0 packets, 0 bytes ]

[\|      Dropped: 0 packets, 0 bytes ]

[\|      Dropped green: 0 packets, 0 bytes ]

[\|      Dropped yellow: 0 packets, 0 bytes ]

[\|      Dropped red: 0 packets, 0 bytes]

[         \|         ]

         +\--FC: AF(1)

[         \|      FP: default(0)]

[\|      Total queue length: 200 packets ]

[\|      Current queue length: 0 packets, 0% use ratio ]

[\|      Forwarded: 0 packets, 0 bytes ]

[\|      Forwarded green: 0 packets, 0 bytes ]

[\|      Forwarded yellow: 0 packets, 0 bytes ]

[\|      Forwarded red: 0 packets, 0 bytes ]

[\|      Tail dropped: 0 packets, 0 bytes ]

[\|      Dropped: 0 packets, 0 bytes ]

[\|      Dropped green: 0 packets, 0 bytes ]

[\|      Dropped yellow: 0 packets, 0 bytes ]

[\|      Dropped red: 0 packets, 0 bytes]

[         \|]

         +\--FC: EF(2)

[         \|      FP: default(0)]

[         \|      Total queue length: 200 packets ]

[         \|      Current queue length: 0 packets, 0% use ratio ]

[         \|      Forwarded: 0 packets, 0 bytes ]

[         \|      Forwarded green: 0 packets, 0 bytes ]

[         \|      Forwarded yellow: 0 packets, 0 bytes ]

[         \|      Forwarded red: 0 packets, 0 bytes ]

[         \|      Tail dropped: 0 packets, 0 bytes ]

[         \|      Dropped: 0 packets, 0 bytes ]

[         \|      Dropped green: 0 packets, 0 bytes ]

[         \|      Dropped yellow: 0 packets, 0 bytes ]

[         \|      Dropped red: 0 packets, 0 bytes]

[         \|]

         +\--FC: NC(3)

                FP: default(0)

Total queue length: 200 packets

Current queue length: 0 packets, 0% use ratio

Forwarded: 0 packets, 0 bytes

Forwarded green: 0 packets, 0 bytes

Forwarded yellow: 0 packets, 0 bytes

Forwarded red: 0 packets, 0 bytes

Tail dropped: 0 packets, 0 bytes

Dropped: 0 packets, 0 bytes

Dropped green: 0 packets, 0 bytes

Dropped yellow: 0 packets, 0 bytes

Dropped red: 0 packets, 0 bytes

表1-8 display qos scheduler-policy interface命令显示信息描述表

字段

描述

Interface

策略应用的端口

Direction

策略应用的方向

Scheduler policy

调度策略的名称

Forwarding group

转发组的名称

Forwarding class

转发类的名称

Forwarding profile

转发策略的名称

Total queue length

队列总长度

Current queue length

当前队列长度/使用比例

Forwarded

转发报文数/字节数

Forwarded green

转发绿色报文数/字节数

Forwarded yellow

转发黄色报文数/字节数

Forwarded red

转发红色报文数/字节数

Dropped

丢弃的报文总数/字节数

Tail dropped

尾丢弃的报文数/字节数

Dropped green

丢弃的绿色报文数/字节数

Dropped yellow

丢弃的黄色报文数/字节数

Dropped red

丢弃的红色报文数/字节数

**HQoS \-- 调度策略配置命令 \-- forwarding-group profile (scheduler-policy match view)**

------------------------------------------------------------------------

**[forwarding-group profile**]命令用来配置调度策略嵌套转发组，并为该转发组指定转发策略。

**[undo forwarding-group**]命令用来取消配置调度策略嵌套的转发组。

【命令】

**[forwarding-group** *fg-name* **profile** *fp-name*]

**[undo forwarding-group** *fg-name*]

【缺省情况】

调度策略以group方式嵌套预定义转发组。

【视图】

调度策略匹配规则视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fg-name*]：转发组名称，为1～31个字符的字符串，区分大小写。

*[fp-name*]：转发策略名称，为1～31个字符的字符串，区分大小写。

【使用指导】

调度策略中默认嵌套的预定义转发组不能修改与删除。

在调度策略内嵌套转发组时需要保证转发组和对应的转发策略都已经存在。

【举例】

\# 配置调度策略VLAN ID 1～4匹配规则，嵌套转发组testfg，并指定该转发组的转发策略testfp。

\<Sysname\> system-view

Sysname qos scheduler-policy testsp

Sysname-hqos-sp-testsp match service-vlan-id 1 to 4

Sysname-hqos-sp-testsp-match forwarding-group testfg profile testfp

\# 进入VLAN ID 1～4匹配规则视图，取消嵌套转发组testfg，并取消关联转发策略testfp。

\<Sysname\> system-view

Sysname qos scheduler-policy testsp

Sysname-hqos-sp-testsp match service-vlan-id 1 to 4

Sysname-hqos-sp-testsp-match undo forwarding-group testfg

【相关命令】

·**match**

**HQoS \-- 调度策略配置命令 \-- match**

------------------------------------------------------------------------

**[match**]命令用来配置调度策略的匹配规则，并进入该匹配规则视图。

**[undo match**]命令用来取消配置调度策略的匹配规则。

【命令】

**[match**[ { *match-criteria \|* **group }**]]

**[undo match**[ { *match-criteria* \| **group }**]]

【缺省情况】

自定义调度策略无匹配规则。

【视图】

调度策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[match-criteria*]：转发组的匹配规则，具体情况如表 1-9(?-2049749445#_Ref360725206)所示。

**[group**]：该参数表示当前嵌套的转发组的匹配规则为其下嵌套的子转发组匹配规则的并集。

表1-9 转发组的匹配规则取值

取值

描述

service-vlan-id *vlan-id-list*

定义匹配运营商网络VLAN ID的规则

*[vlan-id-list*]：VLAN列表，表示方式为*vlan-id-list *[= { *vlan-id* \| *vlan-id1* **to** *vlan-id2* }&\<1-8\>]，*vlan-id*、*vlan-id1*、*vlan-id2*的取值范围为1～4094，且*vlan-id1*必须小于或等于*vlan-id2*；&\<1-8\>表示前面的参数最多可以重复输入8次

local-precedence *precedence-value-list*

定义匹配本地优先级的规则

*[precedence-value-list*]*：*本地优先级列表，表示方式为*precedence-value-list*[ = { *precedence-value* \| *precedence-value1* **to** *precedence-value2* }&\<1-8\>]，*precedence-value*、*precedence-value1*、*precedence-value2*的取值范围为0～7，且*precedence-value1*必须小于或等于*precedence-value2*；&\<1-8\>表示前面的参数最多可以重复输入8次

dot1p *dot1p-value-list*

定义匹配运营商网络802.1p优先级的规则

*[dot1p-value-list*]：802.1p优先级列表，表示方式为*dot1p-value-list *[= { *dot1p-value* \| *dot1p-value1* **to** *dot1p-value2* }&\<1-8\>]，*dot1p-value*、*dot1p-value1*、*dot1p-value2*的取值范围为0～7，且*dot1p-value1*必须小于或等于*dot1p-value2*；&\<1-8\>表示前面的参数最多可以重复输入8次

qos-local-id *local-id-list*

定义匹配QoS本地ID值的规则

*[local-id-list*]：QoS本地ID值列表，表示方式为*local-id-list *[= { *local-id* \| *local-id1* **to** *local-id2* }&\<1-8\>]，*local-id*、*local-id1*、*local-id2*的取值范围为1～4095，且*local-id1*必须小于或等于*local-id2*；&\<1-8\>表示前面的参数最多可以重复输入8次

【使用指导】

配置匹配规则只是进入视图，并不实际生成配置，仅当在匹配规则下进一步配置嵌套的子转发组后，匹配规则配置才真正生效。

嵌套转发类的转发组不能采用group方式实例化；但是，调度策略可以以group方式嵌套预定义转发组。

取消配置匹配规则会同时删除该匹配规则下嵌套的转发组和转发策略。

【举例】

\# 配置调度策略的VLAN ID 1～4匹配规则。

\<Sysname\> system-view

Sysname qos scheduler-policy testsp

Sysname-hqos-sp-testsp match service-vlan-id 1 to 4

Sysname-hqos-sp-testsp-match

【相关命令】

·**forwarding-group profile** (forwarding-group match view)

**HQoS \-- 调度策略配置命令 \-- qos apply scheduler-policy**

------------------------------------------------------------------------

**[qos apply scheduler-policy**]命令用来在接口上应用调度策略。

**[undo qos apply scheduler-policy**]命令用来取消在接口上应用的调度策略。

【命令】

**[qos apply scheduler-policy**[ *sp-name* { **inbound** \| **outbound** }]]

**[undo qos apply scheduler-policy ***sp-name *[{ **inbound** \| **outbound** }]]

【缺省情况】

接口下没有应用调度策略。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[sp-name*]：调度策略名称，为1～31个字符的字符串，区分大小写。

**[inbound**]：表示在入方向下发调度策略。

**[outbound**]：表示在出方向下发调度策略。

【使用指导】

接口的每个方向上只能应用一个调度策略。

在接口上应用调度策略的配置与端口QoS配置互斥（包括基于队列的GTS、端口WRED、硬件队列调度），且不区分方向。

【举例】

\# 在接口入方向应用调度策略。

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname-GigabitEthernet1/0/1 qos apply scheduler-policy testsp inbound

\# 在接口入方向取消应用调度策略。

\<Sysname\> system-view

Sysname interface gigabitethernet1/0/1

Sysname-GigabitEthernet1/0/1 undo qos apply scheduler-policy testsp inbound

**HQoS \-- 调度策略配置命令 \-- qos scheduler-policy**

------------------------------------------------------------------------

**[qos scheduler-policy**]命令用来创建用户自定义的调度策略，并进入该调度策略视图。

**[undo qos scheduler-policy**]命令用来删除用户自定义的调度策略。

【命令】

**[qos scheduler-policy** *sp-name*]

**[undo qos scheduler-policy** *sp-name*]

【缺省情况】

未创建自定义调度策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[sp-name*]：自定义调度策略的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

系统最多支持创建的调度策略个数为256。

【举例】

\# 创建自定义调度策略。

\<Sysname\> system-view

Sysname qos scheduler-policy testsp

**HQoS \-- 调度策略配置命令 \-- scheduler-unit**

------------------------------------------------------------------------

![说明](HQoS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[scheduler-unit**]命令用来配置调度策略的调度权重单位。

**[undo scheduler-unit**]命令用来恢复调度策略调度权重单位的缺省值。

【命令】

**[scheduler-unit**[ { **byte-count** \| **weight** }]]

**[undo scheduler-unit**]

【缺省情况】

调度策略调度权重单位的缺省值根据实际设备决定。

【视图】

调度策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[byte-count**]：按照每次轮询可发送的字节数进行计算。

**[weight**]：按照权重进行计算。

【举例】

\# 将调度策略指定为按byte-count调度。

\<Sysname\> system-view

Sysname qos scheduler-policy testsp

Sysname-hqos-sp-testsp scheduler-unit byte-count

