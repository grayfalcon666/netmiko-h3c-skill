::: {#68635993 .myid}
[]{#_Toc404782175}[]{#struct_0_x1003_44018_1167068486}[]{#_Toc259001142}[]{#_Toc205709439}

**RBAC \-- RBAC调试命令 \-- debugging role**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1003_44018_x1139691796}

[**[debugging role ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1003_44018_877337845}

[**[undo debugging role ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1003_44018_715500061}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1003_44018_x858811119}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1003_44018_1707441777}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1003_44018_x361064449}

[[network-admin]{lang="EN-US"}]{#struct_0_x1003_44018_603845320}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1003_44018_x80450643}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1003_44018_x1878795656}

[**[all]{lang="EN-US"}**]{#struct_0_x1003_44018_1163819033}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1003_44018_1815945864}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1003_44018_634085841}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1003_44018_x858811120}

[**[debugging role]{lang="EN-US"}**]{#struct_0_x1003_44018_1706851956}[命令用来打开]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging role]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RBAC]{lang="EN-US"}]{#struct_0_x1003_44018_x1150183551}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging role error]{lang="EN-US"}]{#struct_0_x1003_44018_x973216227}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_469225071}[[字段]{style="font-family:黑体"}]{#struct_0_x1003_44018_62438781}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1003_44018_1847384084}

[[Failed to open the role policy file.]{lang="EN-US"}]{#struct_0_x1003_44018_x1335332475}

[[打开用户角色策略文件失败]{style="font-family:宋体"}]{#struct_0_x1003_44018_1893745237}

[[Failed to load role *role-name*.]{lang="EN-US"}]{#struct_0_x1003_44018_x858811121}

[[加载指定的用户角色失败]{style="font-family:宋体"}]{#struct_0_x1003_44018_1706917492}

[[Failed to open the feature policy file.]{lang="EN-US"}]{#struct_0_x1003_44018_x25198438}

[[打开特性策略文件失败]{style="font-family:宋体"}]{#struct_0_x1003_44018_827728010}

[[Failed to load feature *feature-name.*]{lang="EN-US"}]{#struct_0_x1003_44018_x1002942766}

[[加载指定的特性]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*]{#struct_0_x1003_44018_x1507690120}[失败]{style="font-family:宋体"}

[[Failed to get the feature name list.]{lang="EN-US"}]{#struct_0_x1003_44018_x1320906757}

[[获取特性名称列表失败]{style="font-family:宋体"}]{#struct_0_x1003_44018_x858811122}

[[Failed to get the description of feature *feature-name*.]{lang="EN-US"}]{#struct_0_x1003_44018_1706983028}

[[加载指定特性]{style="font-family:宋体"}*[feature-name]{lang="EN-US"}*]{#struct_0_x1003_44018_1202761257}[的描述信息失败]{style="font-family:宋体"}

[[Failed to open the feature group policy file.]{lang="EN-US"}]{#struct_0_x1003_44018_x1608935383}

[[打开特性组策略文件失败]{style="font-family:宋体"}]{#struct_0_x1003_44018_1809618256}

[[Failed to load feature group *featuregp-name*.]{lang="EN-US"}]{#struct_0_x1003_44018_x858811123}

[[加载指定的特性组]{style="font-family:宋体"}*[featuregp-name]{lang="EN-US"}*]{#struct_0_x1003_44018_1707048564}[失败]{style="font-family:宋体"}

[[Failed to set the user role.]{lang="EN-US"}]{#struct_0_x1003_44018_1943390407}

[[下发用户角色失败]{style="font-family:宋体"}]{#struct_0_x1003_44018_1011696633}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging role event]{lang="EN-US"}]{#struct_0_x1003_44018_x1991119338}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_462008967}[[字段]{style="font-family:黑体"}]{#struct_0_x1003_44018_1756058047}

[[描述]{style="font-family:黑体"}]{#struct_0_x1003_44018_x858811124}

[[Checking command permission in role *role-name*.]{lang="EN-US"}]{#struct_0_x1003_44018_1706589812}

[[检查用户角色]{style="font-family:宋体"}*[role-name]{lang="EN-US"}*]{#struct_0_x1003_44018_1193098424}[中的命令行权限]{style="font-family:宋体"}

[[Checking command permission in *rule-list-type* rule list.]{lang="EN-US"}]{#struct_0_x1003_44018_244822999}

[[检查规则列表]{style="font-family:宋体"}*[rule-list-type]{lang="EN-US"}*]{#struct_0_x1003_44018_x1638444913}[中的命令行权限，]{style="font-family:宋体"}*[rule-list-type]{lang="EN-US"}*[包括以下几类：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[priviledged]{lang="EN-US"}]{#struct_0_x1003_44018_1377340763}[：]{style="font-family:宋体"}[特权规则列表]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[包含]{lang="EN-US" style="font-family:宋体"}[通过]{style="font-family:宋体"}**[display role]{lang="EN-US"}**[可]{lang="EN-US" style="font-family:宋体"}[查看到的具有]{style="font-family:宋体"}[sys]{lang="EN-US"}[前缀的规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[user defined]{lang="EN-US"}]{#struct_0_x1003_44018_1964520744}[：]{style="font-family:宋体"}[用户自定义规则列表]{lang="EN-US" style="font-family:宋体"}[，包含]{style="font-family:
  宋体"}[用户自己配置的规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[system predefined]{lang="EN-US"}]{#struct_0_x1003_44018_1479841045}[：]{style="font-family:宋体"}[系统预定义规则列表]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:
  宋体"}[包含普通]{lang="EN-US" style="font-family:宋体"}[用户]{style="font-family:宋体"}[角色无法执行的命令规则]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}[例如，]{lang="EN-US" style="font-family:宋体"}[RBAC]{lang="EN-US"}[命令只能由]{lang="EN-US" style="font-family:宋体"}[nework-admin]{lang="EN-US"}[角色执行]{lang="EN-US" style="font-family:宋体"}

[[Matching rule *rule-num*, its type is *rule-type* and the action is *act-value*.]{lang="EN-US"}]{#struct_0_x1003_44018_x908542104}

[[正在匹配规则]{style="font-family:宋体"}]{#struct_0_x1003_44018_x1984296947}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rule-num]{lang="EN-US"}*]{#struct_0_x1003_44018_998398329}[：规则编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[rule-type]{lang="EN-US"}]{#struct_0_x1003_44018_255467969}[：规则类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[0]{lang="EN-US"}]{#struct_0_x1003_44018_x1748481787}[：基于命令的规则]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[1]{lang="EN-US"}]{#struct_0_x1003_44018_1479841044}[：基于特性的规则]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[2]{lang="EN-US"}]{#struct_0_x1003_44018_x908476568}[：基于特性组的规则]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[3]{lang="EN-US"}]{#struct_0_x1003_44018_x417277282}[：基于]{style="font-family:宋体"}[Web]{lang="EN-US"}[菜单的规则]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[4]{lang="EN-US"}]{#struct_0_x1003_44018_114116238}[：基于]{style="font-family:宋体"}[XML]{lang="EN-US"}[元素]{style="font-family:宋体"} [规则]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[act-value]{lang="EN-US"}*]{#struct_0_x1003_44018_632511097}[：是否允许执行]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[0]{lang="EN-US"}]{#struct_0_x1003_44018_1479841043}[：]{style="font-family:宋体"}[pemit]{lang="EN-US"}[（允许执行）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[1]{lang="EN-US"}]{#struct_0_x1003_44018_x908935320}[：]{style="font-family:宋体"}[deny]{lang="EN-US"}[（禁止执行）]{style="font-family:宋体"}

[[Matching the rule of \"*rule-string*\", the result is *result-code*.]{lang="EN-US"}]{#struct_0_x1003_44018_x431146804}

[[正在匹配指定的规则，匹配结果为]{style="font-family:宋体"}*[result-code]{lang="EN-US"}*]{#struct_0_x1003_44018_x1708525350}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x1003_44018_1918690251}[：匹配失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1003_44018_1479841042}[：匹配成功]{style="font-family:宋体"}

[[Command "*command-string*" is *action*.]{lang="EN-US"}]{#struct_0_x1003_44018_x908869784}

[[命令行]{style="font-family:宋体"}*[command-string]{lang="EN-US"}*]{#struct_0_x1003_44018_1119357793}[是否允许被执行]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1003_44018_x1567852068}

[[\# ]{lang="EN-US"}]{#struct_0_x1003_44018_1047780617}[在设备上进行]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[的相关配置，打开]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[的错误调试信息开关。当用户登录设备，如果系统处理出现错误，设备上输出如下错误调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging role error]{lang="EN-US"}]{#struct_0_x1003_44018_x686996618}

[ ]{lang="EN-US"}

[\*Dec 14 10:53:25:612 2013 Sysname RBAC/7/ERROR: Failed to open the role policy file.]{lang="EN-US"}

[[// ]{lang="EN-US"}]{#struct_0_x1003_44018_380972675}[当用户登录设备，系统为用户加载权限配置信息时，打开用户角色策略文件失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1003_44018_1479841041}[在设备上进行]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[的相关配置，打开]{style="font-family:宋体"}[RBAC]{lang="EN-US"}[的事件调试信息开关。当用户登录设备并输入命令时，设备上输出如下事件调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging role event]{lang="EN-US"}]{#struct_0_x1003_44018_x908804248}

[\<Sysname\> display current-configuration]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 11 10:03:45:739 2013 Sysname RBAC/7/EVENT: -MDC=1; Checking command permis]{lang="EN-US"}

[sion in role network-admin.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1003_44018_x1209547698}*[检查用户角色]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[中的命令权限]{style="font-family:宋体"}*

[[\*Jan 11 10:03:45:739 2013 Sysname RBAC/7/EVENT: -MDC=1; Checking command permission]{lang="EN-US"}]{#struct_0_x1003_44018_468005524}

[in priviledged rule list.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1003_44018_1965402481}*[检查特权规则列表中的命令权限]{style="font-family:宋体"}*

[[\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Checking command permission]{lang="EN-US"}]{#struct_0_x1003_44018_2140355718}

[in user defined rule list.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1003_44018_260561120}*[检查用户自定义规则列表中的命令权限]{style="font-family:宋体"}*

[[\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Checking command permission]{lang="EN-US"}]{#struct_0_x1003_44018_1479841040}

[in system predefined rule list.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1003_44018_x908738712}*[检查系统预定义规则列表中的命令权限]{style="font-family:宋体"}*

[[\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Matching rule 2, its type is]{lang="EN-US"}]{#struct_0_x1003_44018_x1599236514}

[ 4 and the action is 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1003_44018_x1428881057}*[正在匹配规则]{style="font-family:宋体"}[2]{lang="EN-US"}[，规则类型为]{style="font-family:宋体"}[XML]{lang="EN-US"}[元素，规则动作是允许]{style="font-family:宋体"}*

[[\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Matching rule 1, its type is]{lang="EN-US"}]{#struct_0_x1003_44018_x2128609918}

[ 0 and the action is 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1003_44018_1303006353}*[正在匹配规则]{style="font-family:宋体"}[1]{lang="EN-US"}[，规则类型为命令行，规则动作是允许]{style="font-family:宋体"}*

[[\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Matching the rule of \"\*\", th]{lang="EN-US"}]{#struct_0_x1003_44018_x1404170973}

[e result is 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1003_44018_1311774896}*[正在匹配规则]{style="font-family:宋体"}["\*"]{lang="EN-US"}[，匹配结果为成功]{style="font-family:宋体"}*

[[\*Jan 11 10:03:45:740 2013 Sysname RBAC/7/EVENT: -MDC=1; Command \"display current-con]{lang="EN-US"}]{#struct_0_x1003_44018_1479841039}

[figuration\" is permitted.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1003_44018_x909328539}*[允许执行命令行]{style="font-family:宋体"}**[display current-configuration]{lang="EN-US"}**[ ]{lang="EN-US"}*
