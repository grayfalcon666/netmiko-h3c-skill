::: {#2070802095 .myid}
[]{#_Toc404786503}[]{#struct_0_x2084_14375_1089480859}[]{#_Toc242844564}

**流分类 \-- forwarding policy**

------------------------------------------------------------------------

[**[forwarding policy]{lang="EN-US"}**]{#struct_0_x2084_14375_1411741417}[命令用来配置流分类策略。]{style="font-family:宋体"}

[**[undo forwarding policy]{lang="EN-US"}**]{#struct_0_x2084_14375_2117831088}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2084_14375_x595361015}

[**[forwarding policy ]{lang="EN-US"}**[{ **per-flow** \| **per-packet** }]{lang="EN-US"}]{#struct_0_x2084_14375_1420931399}

[**[undo forwarding policy]{lang="EN-US"}**]{#struct_0_x2084_14375_x728783011}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2084_14375_x450273462}

[[采用基于流处理的流分类策略。]{style="font-family:宋体"}]{#struct_0_x2084_14375_x450849776}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2084_14375_x1263852729}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2084_14375_x1317969770}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2084_14375_539731472}

[[network-admin]{lang="EN-US"}]{#struct_0_x2084_14375_x912778694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2084_14375_1285388193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2084_14375_2117765552}

[**[per-flow]{lang="EN-US"}**]{#struct_0_x2084_14375_x1374726567}[：基于流处理，同一条流被分配到同一个]{style="font-family:宋体"}[CPU]{lang="EN-US"}[进行处理，处理过程保证先进先出。]{style="font-family:宋体"}

[**[per-packet]{lang="EN-US"}**]{#struct_0_x2084_14375_1488891667}[：基于报文处理，将报文依次发送到不同的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[进行处理，不保证报文的处理顺序。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2084_14375_392751883}

[[\# ]{lang="EN-US"}]{#struct_0_x2084_14375_x1363160930}[配置流分类策略为基于报文处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2084_14375_x1576330703}

[\[Sysname\] forwarding policy per-packet]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2084_14375_391292440}[配置流分类策略为基于流处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2084_14375_x1414607384}

[\[Sysname\] forwarding policy per-flow]{lang="EN-US"}
:::
