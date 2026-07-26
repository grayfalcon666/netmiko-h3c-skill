::: {#118604133 .myid}
[]{#_Toc404795794}[]{#struct_0_x6711_x2124_2086638777}

**Monitor Link \-- Monitor Link调试命令 \-- debugging monitor-link**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6711_x2124_1640416862}

[**[debugging monitor-link]{lang="EN-US"}**[ \[ **group** *group-id* \] { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x6711_x2124_2031716269}

[**[undo debugging monitor-link]{lang="EN-US"}**[ \[ **group** *group-id* \] { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x6711_x2124_477241163}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6711_x2124_719760365}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6711_x2124_x351543253}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6711_x2124_1772348634}

[[network-admin]{lang="EN-US"}]{#struct_0_x6711_x2124_x1205628850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6711_x2124_x322978520}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6711_x2124_1015654035}

[**[group]{lang="EN-US"}***[ group-id]{lang="EN-US"}*]{#struct_0_x6711_x2124_98359116}[：表示指定]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的调试信息开关。如果未指定本参数，则表示所有]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的调试信息开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x6711_x2124_x173305420}[：表示]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x6711_x2124_1114922993}[：表示]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6711_x2124_735320785}[：表示]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6711_x2124_1733286671}

[**[debugging monitor-link]{lang="EN-US"}**]{#struct_0_x6711_x2124_126889001}[命令用来打开]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组调试信息开关。]{style="font-family:宋体"}**[undo debugging monitor-link]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}]{#struct_0_x6711_x2124_x152022333}[组调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging monitor-link error]{lang="EN-US"}]{#struct_0_x6711_x2124_1772807386}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2123250499}[[字段]{style="font-family:黑体"}]{#struct_0_x6711_x2124_x1273267443}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6711_x2124_958700790}

[[Failed to allocate memory for batch backup]{lang="EN-US"}]{#struct_0_x6711_x2124_1885139658}

[[为批量备份分配内存失败]{style="font-family:宋体"}]{#struct_0_x6711_x2124_x1243920613}

[[Failed to allocate memory for realtime backup]{lang="EN-US"}]{#struct_0_x6711_x2124_1808675199}

[[为实时备份分配内存失败]{style="font-family:宋体"}]{#struct_0_x6711_x2124_149646006}

[[Failed to send batch backup message]{lang="EN-US"}]{#struct_0_x6711_x2124_x463185881}

[[发送批量备份消息失败]{style="font-family:宋体"}]{#struct_0_x6711_x2124_x1419614272}

[[Failed to send realtime backup message]{lang="EN-US"}]{#struct_0_x6711_x2124_1772741850}

[[发送实时备份消息失败]{style="font-family:宋体"}]{#struct_0_x6711_x2124_x430587899}

[[Failed to allocate memory for the monitor link group]{lang="EN-US"}]{#struct_0_x6711_x2124_x959544148}

[[为]{style="font-family:宋体"}]{#struct_0_x6711_x2124_x2006376446}[Monitor Link]{lang="SV"}[组]{style="font-family:宋体"}[分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for the monitor link port]{lang="EN-US"}]{#struct_0_x6711_x2124_2111215916}

[[为]{style="font-family:宋体"}]{#struct_0_x6711_x2124_1350456884}[Monitor Link]{lang="SV"}[组的成员端口]{style="font-family:宋体"}[分配内存失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging monitor-link event]{lang="EN-US"}]{#struct_0_x6711_x2124_x878876429}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2129606869}[[字段]{style="font-family:黑体"}]{#struct_0_x6711_x2124_1772283099}

[[描述]{style="font-family:黑体"}]{#struct_0_x6711_x2124_x2007914020}

[[Monitor link group *group-id* is up]{lang="EN-US"}]{#struct_0_x6711_x2124_x1384133263}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x6711_x2124_x753903300}[组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Monitor link group *group-id* is down]{lang="EN-US"}]{#struct_0_x6711_x2124_x1710058212}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x6711_x2124_x43112471}[组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6711_x2124_215617445}

[[\# ]{lang="EN-US"}]{#struct_0_x6711_x2124_x783137346}[打开]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:
宋体"}

[[\<Sysname\> debugging monitor-link group 1 event]{lang="EN-US"}]{#struct_0_x6711_x2124_1772217563}

[\*Dec 28 19:37:47:543 2011 ]{lang="EN-US"}[Sysname]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[MTLK/7/Event:]{lang="EN-US"}

[ Monitor link group 1 is down]{lang="EN-US"}

[*[// ]{lang="EN-US"}[Monitor Link]{lang="EN-US"}*]{#struct_0_x6711_x2124_1868266577}*[组]{style="font-family:宋体"}[1]{lang="EN-US"}[处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}*
