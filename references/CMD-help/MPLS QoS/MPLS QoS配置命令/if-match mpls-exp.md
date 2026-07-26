
**MPLS QoS \-- MPLS QoS配置命令 \-- if-match mpls-exp**

------------------------------------------------------------------------

**[if-match mpls-exp**]命令用来定义匹配第一层MPLS EXP优先级的规则。

**[undo if-match mpls-exp**]命令用来删除匹配第一层MPLS EXP优先级的规则。

【命令】

**[if-match ** **not** ] **mpls-exp** *exp-value*&\<1-8\>

**[undo if-match ** **not** ] **mpls-exp** *exp-value*&\<1-8\>

【缺省情况】

没有定义匹配第一层MPLS EXP优先级的规则。

【视图】

类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[not**]：不匹配该规则。

*[exp-value*&\<1-8\>]：EXP值的列表，EXP优先级的取值范围为0～7，&\<1-8\>表示前面的参数最多可以输入8次。如果指定了多个相同的EXP值，系统默认为一个；多个不同的EXP值是或的关系，即只要有一个值匹配，就算匹配这条规则。

【举例】

\# 定义匹配第一层EXP优先级为3或4的报文的规则。

\<Sysname\> system-view

Sysname traffic classifier database

Sysname-classifier-database if-match mpls-exp 3 4

**MPLS QoS \-- MPLS QoS配置命令 \-- if-match mpls-label**

------------------------------------------------------------------------

**[if-match mpls-label**]命令用来定义匹配第一层MPLS标签的规则。

**[undo if-match mpls-label**]命令用来删除匹配第一层MPLS标签的规则。

【命令】

**[if-match **[ **not**  **mpls-label** { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]]

**[undo if-match **[ **not**  **mpls-label** { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]]

【缺省情况】

没有定义匹配第一层MPLS标签的规则。

【视图】

类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[not**]：不匹配该规则。

*[label-value*&\<1-8\>]：MPLS标签值的列表，MPLS标签值的取值范围为0～1048575，&\<1-8\>表示前面的参数最多可以输入8次。

*[label-value1* **to** *label-value2*]：MPLS标签值的范围，*label-value1*的值必须小于*label-value2*的值，MPLS标签值的取值范围为0～1048575。

【使用指导】

如果指定了多个相同的MPLS标签值，系统默认为一个；多个不同的MPLS标签值是或的关系，即只要有一个值匹配，就算匹配这条规则。

【举例】

\# 定义匹配第一层MPLS标签为1到1000的报文的规则。

\<Sysname\> system-view

Sysname traffic classifier database

Sysname-classifier-database if-match mpls-label 1 to 1000

**MPLS QoS \-- MPLS QoS配置命令 \-- if-match second-mpls-exp**

------------------------------------------------------------------------

**[if-match second-mpls-exp**]命令用来定义匹配第二层MPLS的EXP域的规则。

**[undo if-match second-mpls-exp**]命令用来删除匹配第二层MPLS的EXP域的规则。

【命令】

**[if-match ** **not** ] **second-mpls-exp** *exp-value*&\<1-8\>

**[undo if-match ** **not** ] **second-mpls-exp** *exp-value*&\<1-8\>

【缺省情况】

没有定义匹配第二层MPLS EXP优先级的规则。

【视图】

类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[not**]：不匹配该规则。

*[exp-value*&\<1-8\>]：EXP值的列表，EXP优先级的取值范围为0～7，&\<1-8\>表示前面的参数最多可以输入8次。如果指定了多个相同的EXP值，系统默认为一个；多个不同的EXP值是或的关系，即只要有一个值匹配，就算匹配这条规则。

【举例】

\# 定义匹配第二层EXP为3或4的报文的规则。

\<Sysname\> system-view

Sysname traffic classifier database

Sysname-classifier-database if-match second-mpls-exp 3 4

**MPLS QoS \-- MPLS QoS配置命令 \-- if-match second-mpls-label**

------------------------------------------------------------------------

**[if-match second-mpls-label**]命令用来定义匹配第二层MPLS标签的规则。

**[undo if-match second-mpls-label**]命令用来删除匹配第二层MPLS标签的规则。

【命令】

**[if-match **[ **not**  **second-mpls-label** { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]]

**[undo if-match **[ **not**  **second-mpls-label** { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]]

【缺省情况】

没有定义匹配第二层MPLS标签的规则。

【视图】

类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[not**]：不匹配该规则。

*[label-value*&\<1-8\>]：MPLS标签值的列表，MPLS标签值的取值范围为0～1048575，&\<1-8\>表示前面的参数最多可以输入8次。

*[label-value1* **to** *label-value2*]：MPLS标签值的范围，*label-value1*的值必须小于*label-value2*的值，MPLS标签值的取值范围为0～1048575。

【使用指导】

如果指定了多个相同的MPLS标签值，系统默认为一个；多个不同的MPLS标签值是或的关系，即只要有一个值匹配，就算匹配这条规则。

【举例】

\# 定义匹配第二层MPLS标签为1到1000的报文的规则。

\<Sysname\> system-view

Sysname traffic classifier database

Sysname-classifier-database if-match second-mpls-label 1 to 1000

**MPLS QoS \-- MPLS QoS配置命令 \-- remark mpls-exp**

------------------------------------------------------------------------

**[remark mpls-exp**]命令用来配置标记MPLS报文的EXP值。

**[undo remark mpls-exp**]命令用来取消标记MPLS报文的EXP值。

【命令】

**[remark **[[ **green** \| **red** \| **yellow** ] **mpls-exp** *exp-value*]]

**[undo remark **[[ **green** \| **red** \| **yellow** ] **mpls-exp**]]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[green**]：对绿色报文进行重标记。

**[red**]：对红色报文进行重标记。

**[yellow**]：对黄色报文进行重标记。

*[exp-value*]：MPLS报文的EXP值，取值范围为0～7。

【使用指导】

·如果没有指定颜色，则对所有颜色的报文进行重标记。

·如果是多层标签，则是对最外层标签进行标记。

【举例】

\# 配置标记MPLS报文的EXP值为0。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark mpls-exp 0

**MPLS QoS \-- MPLS QoS配置命令 \-- remark imposition-mpls-exp**

------------------------------------------------------------------------

**[remark imposition-mpls-exp**]命令用来配置标记MPLS新增标签的EXP值。

**[undo remark imposition-mpls-exp**]命令用来取消标记MPLS新增标签的EXP值。

【命令】

**[remark ** [ **green** \| **red** \| **yellow** ] **imposition-mpls-exp** *exp-value*]

**[undo remark ** [ **green** \| **red** \| **yellow** ] **imposition-mpls-exp**]

【缺省情况】

没有配置重新标记报文的动作。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[green**]：对绿色报文进行重标记。

**[red**]：对红色报文进行重标记。

**[yellow**]：对黄色报文进行重标记。

*[exp-value*]：MPLS报文的EXP值，取值范围为0～7。

【使用指导】

如果没有指定颜色，则对所有颜色的报文进行重标记。

【举例】

\# 配置标记MPLS新增标签的EXP值为0。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark imposition-mpls-exp 0

【相关命令】

·**remark mpls-exp**

