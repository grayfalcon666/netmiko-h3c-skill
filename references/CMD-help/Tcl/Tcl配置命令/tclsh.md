::: {#-423337384 .myid}
[]{#_Toc404782987}[]{#struct_0_x1340_x1334_x351110760}[]{#_Toc328492646}

**Tcl \-- Tcl配置命令 \-- tclsh**

------------------------------------------------------------------------

[**[tclsh]{lang="EN-US"}**]{#struct_0_x1340_x1334_x2102005248}[命令用来从用户视图进入]{style="font-family:宋体"}[Tcl]{lang="EN-US"}[配置视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_525290338}

[**[tclsh]{lang="EN-US"}**]{#struct_0_x1340_x1334_x854936275}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_1651455815}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1340_x1334_x1732256378}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_x1355458190}

[[network-admin]{lang="EN-US"}]{#struct_0_x1340_x1334_x1672992454}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1340_x1334_x1527882975}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_2113406405}

[[在用户视图下执行]{style="font-family:宋体"}**[tclsh]{lang="EN-US"}**]{#struct_0_x1340_x1334_x766647714}[命令，会进入]{style="font-family:宋体"}[Tcl]{lang="EN-US"}[配置视图。为兼容]{style="font-family:宋体"}[Comware]{lang="EN-US"}[配置方式，在]{style="font-family:宋体"}[Tcl]{lang="EN-US"}[配置视图下，用户可以直接输入]{style="font-family:宋体"}[Tcl]{lang="EN-US"}[脚本命令，也可以输入]{style="font-family:宋体"}[Comware]{lang="EN-US"}[系统的命令。命令输入完成后，直接回车即可执行。]{style="font-family:宋体"}

[[Tcl]{lang="EN-US"}]{#struct_0_x1340_x1334_x122465853}[配置视图下，支持]{style="font-family:宋体"}[Tcl8.5]{lang="EN-US"}[版本的所有命令。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[Comware]{lang="EN-US"}]{#struct_0_x1340_x1334_x1899977846}[系统的命令，]{style="font-family:宋体"}[Tcl]{lang="EN-US"}[配置视图相当于用户视图，配置方式同用户视图下的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_556873499}

[[\# ]{lang="EN-US"}]{#struct_0_x1340_x1334_1411388881}[从用户视图进入]{style="font-family:宋体"}[Tcl]{lang="EN-US"}[配置视图。]{style="font-family:宋体"}

[[\<Sysname\> tclsh]{lang="EN-US"}]{#struct_0_x1340_x1334_x1355392654}

[\<Sysname-tcl\>]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_496027659}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tclquit]{lang="EN-US"}**]{#struct_0_x1340_x1334_x342689114}
:::

::: {#877298661 .myid}
[]{#_Toc404782988}[]{#struct_0_x1340_x1334_x83088638}[]{#_Toc328492647}

**Tcl \-- Tcl配置命令 \-- tclquit**

------------------------------------------------------------------------

[**[tclquit]{lang="EN-US"}**]{#struct_0_x1340_x1334_1785592297}[命令用来从]{style="font-family:宋体"}[Tcl]{lang="EN-US"}[配置视图退回到用户视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_1920896415}

[**[tclquit]{lang="EN-US"}**]{#struct_0_x1340_x1334_1844922785}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_1474976129}

[[Tcl]{lang="EN-US"}]{#struct_0_x1340_x1334_1695543168}[配置视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_x2018117066}

[[network-admin]{lang="EN-US"}]{#struct_0_x1340_x1334_x1355327118}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1340_x1334_988124543}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_x1017390016}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在]{style="font-family:宋体"}]{#struct_0_x1340_x1334_2105299367}[Tcl]{lang="EN-US"}[配置视图下使用了]{style="font-family:宋体"}[Comware]{lang="EN-US"}[命令进入了子视图，则只能用]{style="font-family:宋体"}**[quit]{lang="EN-US"}**[命令退回到上一级视图，不能执行]{style="font-family:宋体"}**[tclquit]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行该命令效果等同于在]{style="font-family:宋体"}]{#struct_0_x1340_x1334_1669804180}[Tcl]{lang="EN-US"}[配置视图下执行]{style="font-family:宋体"}**[quit]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_351741239}

[[\# ]{lang="EN-US"}]{#struct_0_x1340_x1334_x2038492183}[从]{style="font-family:宋体"}[Tcl]{lang="EN-US"}[配置视图退回到用户视图。]{style="font-family:宋体"}

[[\<Sysname-tcl\> tclquit]{lang="EN-US"}]{#struct_0_x1340_x1334_x854550258}

[\<Sysname\>]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1340_x1334_840757871}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[t]{lang="EN-US"}[cl]{lang="EN-US"}**]{#struct_0_x1340_x1334_1925308933}**[sh]{lang="EN-US"}**

[ ]{lang="EN-US"}
:::
