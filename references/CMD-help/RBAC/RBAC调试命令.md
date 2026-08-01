<!-- CMD-INDEX
  debugging role                      | 用户视图             | L5
-->

**RBAC \-- RBAC调试命令 \-- debugging role**

------------------------------------------------------------------------

【命令】

**[debugging role **[{ **all** \| **error** \| **event** }]]

**[undo debugging role **[{ **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging role**]命令用来打开RBAC调试信息开关。**undo debugging role**命令用来关闭RBAC调试信息开关。

缺省情况下，RBAC调试信息开关处于关闭状态。

表1-1 debugging role error命令输出信息描述表

字段

描述

Failed to open the role policy file.

打开用户角色策略文件失败

Failed to load role *role-name*.

加载指定的用户角色失败

Failed to open the feature policy file.

打开特性策略文件失败

Failed to load feature *feature-name.*

加载指定的特性*feature-name*失败

Failed to get the feature name list.

获取特性名称列表失败

Failed to get the description of feature *feature-name*.

加载指定特性*feature-name*的描述信息失败

Failed to open the feature group policy file.

打开特性组策略文件失败

Failed to load feature group *featuregp-name*.

加载指定的特性组*featuregp-name*失败

Failed to set the user role.

下发用户角色失败

表1-2 debugging role event命令输出信息描述表

字段

描述

Checking command permission in role *role-name*.

检查用户角色*role-name*中的命令行权限

Checking command permission in *rule-list-type* rule list.

检查规则列表*rule-list-type*中的命令行权限，*rule-list-type*包括以下几类：

·priviledged：特权规则列表，包含通过**display role**可查看到的具有sys前缀的规则

·user defined：用户自定义规则列表，包含用户自己配置的规则

·system predefined：系统预定义规则列表，包含普通用户角色无法执行的命令规则。例如，RBAC命令只能由nework-admin角色执行

Matching rule *rule-num*, its type is *rule-type* and the action is *act-value*.

正在匹配规则

·*rule-num*：规则编号

·rule-type：规则类型

¡0：基于命令的规则

¡1：基于特性的规则

¡2：基于特性组的规则

¡3：基于Web菜单的规则

¡4：基于XML元素 规则

·*act-value*：是否允许执行

¡0：pemit（允许执行）

¡1：deny（禁止执行）

Matching the rule of \"*rule-string*\", the result is *result-code*.

正在匹配指定的规则，匹配结果为*result-code*

·0：匹配失败

·1：匹配成功

Command "*command-string*" is *action*.

命令行*command-string*是否允许被执行

【举例】

\# 在设备上进行RBAC的相关配置，打开RBAC的错误调试信息开关。当用户登录设备，如果系统处理出现错误，设备上输出如下错误调试信息。

\<Sysname\> debugging role error

\*Dec 14 10:53:25:612 2013 Sysname RBAC/7/ERROR: Failed to open the role policy file.

// 当用户登录设备，系统为用户加载权限配置信息时，打开用户角色策略文件失败

\# 在设备上进行RBAC的相关配置，打开RBAC的事件调试信息开关。当用户登录设备并输入命令时，设备上输出如下事件调试信息。

\<Sysname\> debugging role event

\<Sysname\> display current-configuration

\*Jan 11 10:03:45:739 2013 Sysname RBAC/7/EVENT: -MDC=1; Checking command permis

sion in role network-admin.

*// 检查用户角色network-admin中的命令权限*

\*Jan 11 10:03:45:739 2013 Sysname RBAC/7/EVENT: -MDC=1; Checking command permission

in priviledged rule list.

*// 检查特权规则列表中的命令权限*

\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Checking command permission

in user defined rule list.

*// 检查用户自定义规则列表中的命令权限*

\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Checking command permission

in system predefined rule list.

*// 检查系统预定义规则列表中的命令权限*

\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Matching rule 2, its type is

 4 and the action is 0.

*// 正在匹配规则2，规则类型为XML元素，规则动作是允许*

\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Matching rule 1, its type is

 0 and the action is 0.

*// 正在匹配规则1，规则类型为命令行，规则动作是允许*

\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Matching the rule of \"\*\", th

e result is 1.

*// 正在匹配规则"\*"，匹配结果为成功*

\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Command \"display current-con

figuration\" is permitted.

*// 允许执行命令行**display current-configuration***
