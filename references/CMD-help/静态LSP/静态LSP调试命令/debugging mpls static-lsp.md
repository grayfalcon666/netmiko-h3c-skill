::: {#-1682207415 .myid}
[]{#_Toc404790477}[]{#struct_0_89099_53084_x1582298117}

**静态LSP \-- 静态LSP调试命令 \-- debugging mpls static-lsp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_89099_53084_1673319995}

[**[debugging mpls static-lsp ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **process** }]{lang="EN-US"}]{#struct_0_89099_53084_x2125259859}

[**[undo debugging mpls static-lsp]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **process** }]{lang="EN-US"}]{#struct_0_89099_53084_296930389}

[[【视图】]{style="font-family:黑体"}]{#struct_0_89099_53084_x2087082880}

[[用户视图]{style="font-family:宋体"}]{#struct_0_89099_53084_2121260694}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_89099_53084_x639949018}

[[1]{lang="EN-US"}]{#struct_0_89099_53084_x422708318}[：监控级]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_89099_53084_x2062703020}

[**[all]{lang="EN-US"}**]{#struct_0_89099_53084_x1547496820}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_89099_53084_x1099657214}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_89099_53084_x704200695}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_89099_53084_x265752392}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[创建和删除过程调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_89099_53084_x1019934042}

[**[debugging mpls static-lsp]{lang="EN-US"}**]{#struct_0_89099_53084_92448499}[命令用来打开静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls static-lsp]{lang="EN-US"}**[命令用来关闭静态]{style="font-family:
宋体"}[LSP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_89099_53084_x1382134148}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mpls static-lsp error]{lang="EN-US"}]{#struct_0_89099_53084_857489188}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_526266752}[[字段]{style="font-family:黑体"}]{#struct_0_89099_53084_x422773854}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_89099_53084_1519411017}

[[Failed to process a configuration command.]{lang="EN-US"}]{#struct_0_89099_53084_x286748666}

[[处理配置命令失败]{style="font-family:宋体"}]{#struct_0_89099_53084_x843603917}

[[Failed to activate a static LSP on the ingress.]{lang="EN-US"}]{#struct_0_89099_53084_x1864721164}

[[在]{style="font-family:宋体"}[Ingress]{lang="EN-US"}]{#struct_0_89099_53084_x730157197}[上激活静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging mpls static-lsp event]{lang="EN-US"}]{#struct_0_89099_53084_x1728216011}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_527649849}[[字段]{style="font-family:黑体"}]{#struct_0_89099_53084_x422839390}

[[描述]{style="font-family:黑体"}]{#struct_0_89099_53084_659299158}

[*[Module-A]{lang="EN-US"}*[ created a connection to *Module-B*.]{lang="EN-US"}]{#struct_0_89099_53084_1907738411}

[*[Module-A]{lang="EN-US"}*]{#struct_0_89099_53084_925419618}[模块与]{style="font-family:宋体"}*[Module-B]{lang="EN-US"}*[建立一个连接]{style="font-family:宋体"}

[[Received a message from LSM: The MPLS enable state changed on an interface.]{lang="EN-US"}]{#struct_0_89099_53084_x581335200}

[[从]{style="font-family:宋体"}[LSM]{lang="EN-US"}]{#struct_0_89099_53084_x857633873}[接收到接口上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[使能状态变化事件]{style="font-family:宋体"}

[[Received an HA upgrade event.]{lang="EN-US"}]{#struct_0_89099_53084_x83716869}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_89099_53084_x422904926}[升级事件]{style="font-family:宋体"}

[[Received an HA degrade event.]{lang="EN-US"}]{#struct_0_89099_53084_1932799823}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_89099_53084_1442006265}[降级事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mpls static-lsp process]{lang="EN-US"}]{#struct_0_89099_53084_60786746}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_527270420}[[字段]{style="font-family:黑体"}]{#struct_0_89099_53084_2088761035}

[[描述]{style="font-family:黑体"}]{#struct_0_89099_53084_1830805358}

[[Activated the static LSP (*lsp-destination*/*destination-mask*).]{lang="EN-US"}]{#struct_0_89099_53084_x2126000881}

[[激活一条静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_89099_53084_x422446174}[，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[lsp-destination]{lang="EN-US"}*[，目的地址掩码为]{style="font-family:宋体"}*[destination-mask]{lang="EN-US"}*

[[Deactivated the static LSP (*lsp-destination*/*destination-mask*).]{lang="EN-US"}]{#struct_0_89099_53084_339286055}

[[去激活一条静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_89099_53084_508186302}[，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[lsp-destination]{lang="EN-US"}*[，目的地址掩码为]{style="font-family:宋体"}*[destination-mask]{lang="EN-US"}*

[[Added the label of the static LSP (*lsp-destination*/*destination-mask*, next hop count: *count-num*) to the corresponding routes.]{lang="EN-US"}]{#struct_0_89099_53084_47771757}

[[将静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_89099_53084_1482654327}[（]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[lsp-destination]{lang="EN-US"}*[，目的地址掩码为]{style="font-family:宋体"}*[destination-mask]{lang="EN-US"}*[）的标签添加到对应的路由表项中，静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的下一跳数目为]{style="font-family:宋体"}*[count-num]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_89099_53084_x1545713254}

[[\# ]{lang="EN-US"}]{#struct_0_89099_53084_x115362390}[打开静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的错误调试信息开关。在设备上配置一条本节点作为]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[使用的标签已经被其他的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[使用。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls static-lsp error]{lang="EN-US"}]{#struct_0_89099_53084_x422511710}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] static-lsp egress test2 in-label 100]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[\*May 21 16:12:57:279 2011 Sysname SLSP/7/ERROR: -MDC=1; Failed to process a configuration command.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_89099_53084_x457280043}*[处理命令失败。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_89099_53084_1471934947}[打开静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[事件调试信息开关。在设备上配置一条本节点作为]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，设备上存在该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[下一跳地址对应的激活路由。在该静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[对应的出接口上关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力，设备上会打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls static-lsp event]{lang="EN-US"}]{#struct_0_89099_53084_x1139014064}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] static-lsp ingress test1 destination 100.100.100.2 32 nexthop 172.168.1.2 out-label 30]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo mpls enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]]{lang="EN-US"}

[\*Jun 22 17:09:18:012 2011 Sysname SLSP/7/EVENT: -MDC=1; Received a message from LSM:]{lang="EN-US"}

[The MPLS enable state changed on an interface. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_89099_53084_179303404}*[从]{style="font-family:宋体"}[LSM]{lang="EN-US"}[接收到接口上]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[使能状态变化事件。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_89099_53084_1747528476}[打开静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[创建和删除过程调试信息开关。在设备上删除一条本节点作为]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[时，打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls static-lsp process]{lang="EN-US"}]{#struct_0_89099_53084_x422970461}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] undo static-lsp ingress test1]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[\*Jun 22 17:21:07:821 2011 Sysname SLSP/7/PROCESS: -MDC=1; Deactivated the static LSP (100.100.100.2/32).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_89099_53084_x1607794249}*[去激活一条静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jun 22 17:21:07:822 2011 Sysname SLSP/7/PROCESS: -MDC=1; Added the label of the static LSP (100.100.100.2/32, next hop count: 0) to the corresponding routes.]{lang="EN-US"}]{#struct_0_89099_53084_591385392}

[*[// ]{lang="EN-US"}*]{#struct_0_89099_53084_x1376414486}*[将静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}[100.100.100.2/32]{lang="EN-US"}[）的标签添加到对应的路由表项中，静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的下一跳数目为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*
