::: {#-1344348365 .myid}
[]{#_Toc404790691}[]{#struct_0_x1939_19096_1487405107}[]{#_Toc385236956}[]{#_Toc383519317}

**MPLS TE \-- MPLS TE调试命令 \-- debugging mpls te management**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1939_19096_1731050997}

[**[debugging mpls te management ]{lang="EN-US"}**[\[ **all \| error \| event \| process** \]]{lang="EN-US"}]{#struct_0_x1939_19096_1035801875}

[**[undo debugging mpls te management]{lang="EN-US"}**[ \[ **all \| error \| event \| process** \]]{lang="EN-US"}]{#struct_0_x1939_19096_1832689533}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1939_19096_457852179}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1939_19096_1487470643}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x2129103126}

[[network-admin]{lang="EN-US"}]{#struct_0_x1939_19096_416672754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1939_19096_x67014801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1939_19096_1487274035}

[**[all]{lang="EN-US"}**]{#struct_0_x1939_19096_1343900189}[：表示]{style="font-family:宋体"}[TE management]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1939_19096_1545028279}[：表示]{style="font-family:宋体"}[TE management]{lang="EN-US"}[的]{style="font-family:宋体"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1939_19096_456648884}[：表示]{style="font-family:宋体"}[TE management]{lang="EN-US"}[的]{style="font-family:宋体"}[事件调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_x1939_19096_1304599160}[：表示]{style="font-family:宋体"}[TE management]{lang="EN-US"}[的]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[创建、处理调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1939_19096_1487339571}

[**[debugging mpls te manatement]{lang="EN-US"}**]{#struct_0_x1939_19096_x1721284777}[命令用来打开]{style="font-family:
宋体"}[MPLS TE management]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls te manatement]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MPLS TE management]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MPLS TE management]{lang="EN-US"}]{#struct_0_x1939_19096_1001725525}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mpls te ]{lang="EN-US"}]{#struct_0_x1939_19096_x2109379950}[management error]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1153134643}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1487142963}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1346997791}

[[Failed to reply configurations.]{lang="EN-US"}]{#struct_0_x1939_19096_1487208499}

[[配置处理消息回复失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x2104765741}

[[Failed to update tunnel configurations (tunnel ID: *tunnel-id*) to DBM.]{lang="EN-US"}]{#struct_0_x1939_19096_1487011891}

[[更新]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}]{#struct_0_x1939_19096_x1023022076}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[的隧道配置到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to register protocol with interface management.]{lang="EN-US"}]{#struct_0_x1939_19096_1487077427}

[[向接口管理模块注册失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_2145178949}

[[Failed to send bypass tunnel message.]{lang="EN-US"}]{#struct_0_x1939_19096_1487929395}

[[发送备隧道消息失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1337309673}

[[Failed to send the ingress CRLSP creation message to RSVP: ingress LSR ID *ingress-lsr-id*, egress LSR ID *egress-lsr-id*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction-value*.]{lang="EN-US"}]{#struct_0_x1939_19096_1487994931}

[[向]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x1939_19096_1487405108}[发送]{style="font-family:宋体"}[Ingress CRLSP]{lang="EN-US"}[创建消息失败。]{style="font-family:宋体"}[Ingress CRLSP]{lang="EN-US"}[头节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[ingress-lsr-id]{lang="EN-US"}*[，尾节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[egress-lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[direction]{lang="EN-US"}[为]{style="font-family:宋体"}*[direction-value]{lang="EN-US"}*[ ]{lang="EN-US"}

[[Not enough resources are available to complete the operation.]{lang="EN-US"}]{#struct_0_x1939_19096_1732034037}

[[申请内存失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_1487470644}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging mpls te ]{lang="EN-US"}]{#struct_0_x1939_19096_x2128775446}[management event]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1115653519}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1487274036}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1343703581}

[[Disconnected from tunnel management unexpectedly.]{lang="EN-US"}]{#struct_0_x1939_19096_x418656558}

[[与]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x1939_19096_1487339572}[管理的链接由于异常断开]{style="font-family:宋体"}

[[Registered protocol with interface management.]{lang="EN-US"}]{#struct_0_x1939_19096_1487142964}

[[向接口管理注册成功]{style="font-family:宋体"}]{#struct_0_x1939_19096_1347456543}

[[Sent the ingress CRLSP creation message to RSVP: ingress LSR ID *ingress-lsr-id*, egress LSR ID *egress-lsr-id*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction-value*.]{lang="EN-US"}]{#struct_0_x1939_19096_1487208500}

[[向]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x1939_19096_x148909348}[发送]{style="font-family:宋体"}[Ingress CRLSP]{lang="EN-US"}[创建消息成功。]{style="font-family:宋体"}[Ingress CRLSP]{lang="EN-US"}[头节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[ingress-lsr-id]{lang="EN-US"}*[，尾节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[egress-lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[direction]{lang="EN-US"}[为]{style="font-family:宋体"}*[direction-value]{lang="EN-US"}*[ ]{lang="EN-US"}

[[Received an ingress CRLSP up notification: ingress LSR ID *ingress-lsr-id*, egress LSR ID *egress-lsr-id*, tunnel ID *tunnel-id*, LSP ID *lsp-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_827468578}

[[收到]{style="font-family:宋体"}[Ingress CRLSP UP]{lang="EN-US"}]{#struct_0_x1939_19096_1487011892}[消息。]{style="font-family:宋体"}[Ingress CRLSP]{lang="EN-US"}[头节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[ingress-lsr-id]{lang="EN-US"}*[，尾节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[egress-lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*

[[Protocol registered events (*event-value*).]{lang="EN-US"}]{#struct_0_x1939_19096_x1022956540}

[[协议注册事件类型为]{style="font-family:宋体"}*[event-value]{lang="EN-US"}*]{#struct_0_x1939_19096_1487077428}[的事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mpls te ]{lang="EN-US"}]{#struct_0_x1939_19096_2144458053}[management process]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1090816913}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x443032402}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1487929396}

[[Status of CRLSP (tunnel ID *tunnel-id*, LSP ID *lsp-id*) changed from *old-state* to *new-state*]{lang="EN-US"}]{#struct_0_x1939_19096_1487994932}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_x1939_19096_512772278}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[从状态]{style="font-family:宋体"}*[old-state]{lang="EN-US"}*[切换到新状态]{style="font-family:宋体"}*[new-state]{lang="EN-US"}*

[[Status of TE tunnel (tunnel ID *tunnel-id*) changed from *old-state* to *new-state*.]{lang="EN-US"}]{#struct_0_x1939_19096_1487405109}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_x1939_19096_1731968501}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道口从状态]{style="font-family:宋体"}*[old-state]{lang="EN-US"}*[切换到新状态]{style="font-family:宋体"}*[new-state]{lang="EN-US"}*

[[Sent the batch backup message.]{lang="EN-US"}]{#struct_0_x1939_19096_x2144094005}

[[发送批备消息成功]{style="font-family:宋体"}]{#struct_0_x1939_19096_1487470645}

[[Created a local NHLFE entry: tunnel interface *tunnel-interface-name*, destination IP address *destination-ip*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, source IP address *source-ip*, direction *direction-value*.]{lang="EN-US"}]{#struct_0_x1939_19096_x2128709910}

[[创建]{style="font-family:宋体"}[local NHLFE]{lang="EN-US"}]{#struct_0_x1939_19096_1487274037}[表项成功。]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口名为]{style="font-family:宋体"}*[tunnel-interface-name]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination-ip]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}[，]{style="font-family:宋体"}*[源地址为]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[，]{style="font-family:宋体"}[direction]{lang="EN-US"}[为]{style="font-family:宋体"}*[direction-value]{lang="EN-US"}*[ ]{lang="EN-US"}

[[Setting up timer of CRLSP (tunnel ID *tunnel-id*, LSP ID *lsp-id*) expired.]{lang="EN-US"}]{#struct_0_x1939_19096_1343769117}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_x1939_19096_1487339573}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[ LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[ ]{lang="EN-US"}[的]{style="font-family:
  宋体"}[CRLSP setting up]{lang="EN-US"}[定时器超时]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1721415849}

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x1934829545}[设备上打开]{style="font-family:宋体"}[MPLS TE management]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}[TE]{lang="EN-US"}[模块向]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[发送消息，失败时打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te management error]{lang="EN-US"}]{#struct_0_x1939_19096_292665362}

[\*Mar 12 05:31:02:030 2014 Sysname TE/7/ERROR: -MDC=1; Failed to send the ingress CRLSP creation message to RSVP: ingress LSR ID 1.1.1.1; egress LSR ID 2.2.2.2; tunnel ID 1; LSP ID 34265; direction 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_997295472}*[向]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[发送头节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，尾节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[34265]{lang="EN-US"}[，]{style="font-family:宋体"}[direction]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[Ingress CRLSP]{lang="EN-US"}[创建消息失败。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_444278370}[设备上打开]{style="font-family:宋体"}[MPLS TE management]{lang="EN-US"}[事件调试信息开关。向]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[模块发送或从]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[模块接收消息时，打印如下调试信息。]{style="font-family:宋体"}

[[\*Mar 17 06:16:53:910 2014 Sysname TE/7/EVENT: -MDC=1; Sent the ingress CRLSP creation message to RSVP: ingress LSR ID 1.1.1.1; egress LSR ID 2.2.2.2; tunnel ID 1; LSP ID 20432; direction 0.]{lang="EN-US"}]{#struct_0_x1939_19096_1487142965}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_1347391007}*[向]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[发送头节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，尾节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[20432]{lang="EN-US"}[，]{style="font-family:宋体"}[direction]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[Ingress CRLSP]{lang="EN-US"}[创建消息成功。]{style="font-family:宋体"}*

[[\*Mar 17 06:16:53:913 2014 Sysname TE/7/EVENT: -MDC=1; Received an ingress CRLSP up notification: ingress LSR ID 1.1.1.1; egress LSR ID 2.2.2.2; tunnel ID 1; LSP ID 20432.]{lang="EN-US"}]{#struct_0_x1939_19096_x1463371628}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_1115608048}*[收到头节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，尾节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[20432 ]{lang="EN-US"}[的]{style="font-family:宋体"}[ingress CRLSP UP]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x2070959689}[设备上打开]{style="font-family:宋体"}[MPLS TE management]{lang="EN-US"}[处理过程调试信息开关。]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道创建时，打印如下调试信息。]{style="font-family:宋体"}

[[\*Mar 17 06:16:53:912 2014 Sysname TE/7/PROCESS: -MDC=1; Status of CRLSP (tunnel ID 1; LSP ID 20432) changed from SETUP to READY. ]{lang="EN-US"}]{#struct_0_x1939_19096_1487208501}

[*[// Tunnel ID]{lang="EN-US"}*]{#struct_0_x1939_19096_x148974884}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[20432]{lang="EN-US"}[的]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[从状态]{style="font-family:宋体"}[SETUP]{lang="EN-US"}[切换到新状态]{style="font-family:宋体"}[READY]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Mar 17 06:16:53:912 2014 Sysname TE/7/PROCESS: -MDC=1; Status of TE tunnel (tunnel ID 1) changed from HBK MAINSETUP to HBK BKSETUP. ]{lang="EN-US"}]{#struct_0_x1939_19096_x725663921}

[*[// Tunnel ID]{lang="EN-US"}*]{#struct_0_x1939_19096_x141729944}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道口从状态]{style="font-family:宋体"}[HBK MAINSETUP]{lang="EN-US"}[切换到新状态]{style="font-family:宋体"}[HBK BKSETUP]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-1210959901 .myid}
[]{#_Toc404790692}[]{#struct_0_x1939_19096_x1314706720}[]{#_Toc385236957}[]{#_Toc383519318}

**MPLS TE \-- MPLS TE调试命令 \-- debugging mpls te cspf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x667306519}

[**[debugging mpls te cspf ]{lang="EN-US"}**[\[ **all \| computation \| error \| event \| tedb** \] ]{lang="EN-US"}]{#struct_0_x1939_19096_1487011893}

[**[undo debugging mpls te cspf]{lang="EN-US"}**[ \[ **all \| computation \| error \| event \| tedb** \]]{lang="EN-US"}]{#struct_0_x1939_19096_x1022891004}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1031587304}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1939_19096_659426171}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x939997623}

[[network-admin]{lang="EN-US"}]{#struct_0_x1939_19096_1487077429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1939_19096_2144523589}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x406011179}

[**[all]{lang="EN-US"}**]{#struct_0_x1939_19096_742483222}[：表示]{style="font-family:宋体"}[TE CSPF]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[**[computation]{lang="EN-US"}**]{#struct_0_x1939_19096_197461142}[：表示]{style="font-family:宋体"}[TE CSPF]{lang="EN-US"}[的路径计算调试信息开关]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1939_19096_x1230454744}[：表示]{style="font-family:宋体"}[TE CSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1939_19096_1487929397}[：表示]{style="font-family:宋体"}[TE CSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[事件调试信息开关。]{style="font-family:宋体"}

[**[tedb]{lang="EN-US"}**]{#struct_0_x1939_19096_x1337178601}[：表示]{style="font-family:宋体"}[TE CSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[数据库维护调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1939_19096_931745849}

[**[debugging mpls te cspf]{lang="EN-US"}**]{#struct_0_x1939_19096_1588250392}[命令用来打开]{style="font-family:宋体"}[MPLS TE CSPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls te cspf]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MPLS TE CSPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MPLS TE CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_578713516}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging mpls te ]{lang="EN-US"}]{#struct_0_x1939_19096_1369353555}[cspf computation]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1081056943}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1487994933}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_512837814}

[[Received a computation request message: tunnel ID *tunnel-id*, LSP ID *lsp-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1245853733}

[[收到]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}]{#struct_0_x1939_19096_1487405110}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[的路径计算请求消息]{style="font-family:宋体"}

[[Can\'t decode the computation request message.]{lang="EN-US"}]{#struct_0_x1939_19096_1731509748}

[[无法解析该计算请求消息]{style="font-family:宋体"}]{#struct_0_x1939_19096_x175946576}

[[Added a path node to the shortest path list: LSR ID *lsr-id*, area ID *area-value*, pre-LSR ID *prelsr-id*, in interface IP *in-interface-ip*, metric m*etric-value*, min bandwidth *min-bandwidth*, bandwidth *bandwidth,*hop count number *ho-count*.]{lang="EN-US"}]{#struct_0_x1939_19096_1487470646}

[[向最短路径表中添加一个]{style="font-family:宋体"}[path]{lang="EN-US"}]{#struct_0_x1939_19096_x2128906518}[节点：]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[area ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[area-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[pre-LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[prelsr-id]{lang="EN-US"}*[，入接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[in-interface-ip]{lang="EN-US"}*[，]{style="font-family:宋体"}[metric]{lang="EN-US"}[为]{style="font-family:宋体"}[m*etric-value*]{lang="EN-US"}[，最小带宽为]{style="font-family:宋体"}*[min-bandwidth]{lang="EN-US"}*[，实际带宽为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}[，]{style="font-family:宋体"}*[下一跳个数为]{style="font-family:宋体"}*[ho-count]{lang="EN-US"}*

[[Computed a path in IGP *igp-type*.]{lang="EN-US"}]{#struct_0_x1939_19096_1487274038}

[[在类型为]{style="font-family:宋体"}*[igp-type]{lang="EN-US"}*]{#struct_0_x1939_19096_1487339574}[的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[域成功计算一条路径]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging mpls te ]{lang="EN-US"}]{#struct_0_x1939_19096_x1721612457}[cspf error]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1087049965}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1080334807}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1487142966}

[[Failed to reply configurations.]{lang="EN-US"}]{#struct_0_x1939_19096_1347325471}

[[配置处理消息回复失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x240916953}

[[Failed to upgrade the thread.]{lang="EN-US"}]{#struct_0_x1939_19096_1487208502}

[[PCE]{lang="EN-US"}]{#struct_0_x1939_19096_x149040420}[进程升级失败]{style="font-family:宋体"}

[[Failed to activate the service.]{lang="EN-US"}]{#struct_0_x1939_19096_92213356}

[[PCE]{lang="EN-US"}]{#struct_0_x1939_19096_1487011894}[激活服务端口失败]{style="font-family:宋体"}

[[The loose hop address was invalid.]{lang="EN-US"}]{#struct_0_x1939_19096_x1022825468}

[[松散地址是无效值]{style="font-family:宋体"}]{#struct_0_x1939_19096_888877775}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging mpls te ]{lang="EN-US"}]{#struct_0_x1939_19096_1487077430}[cspf event]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1340232979}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_2144982340}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x8106798}

[[Can\'t process a node with an invalid link type]{lang="EN-US"}]{#struct_0_x1939_19096_763896863}

[[无法处理无效链路类型节点]{style="font-family:宋体"}]{#struct_0_x1939_19096_1487929398}

[[Entered the critical memory alert threshold.]{lang="EN-US"}]{#struct_0_x1939_19096_x1336457705}

[[进入]{style="font-family:宋体"}[critical]{lang="EN-US"}]{#struct_0_x1939_19096_x1962601775}[内存门限]{style="font-family:宋体"}

[[Quitted the severe memory alert threshold.]{lang="EN-US"}]{#struct_0_x1939_19096_1487994934}

[[退出]{style="font-family:宋体"}[severe]{lang="EN-US"}]{#struct_0_x1939_19096_512903350}[内存门限]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging mpls te ]{lang="EN-US"}]{#struct_0_x1939_19096_1935245485}[cspf tedb]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1313708333}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_2079837774}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1487405103}

[[Updated a link node.]{lang="EN-US"}]{#struct_0_x1939_19096_1731313141}

[[成功更新链路信息节点]{style="font-family:宋体"}]{#struct_0_x1939_19096_1006012892}

[[Created an IGP mapping node: IGP type *igp-type*, LSR ID *lsr-id*, VRF index *vrf-index*, process ID *process-id*, area ID *area-value*.]{lang="EN-US"}]{#struct_0_x1939_19096_1487470639}

[[创建一个]{style="font-family:宋体"}[IGP]{lang="EN-US"}]{#struct_0_x1939_19096_x2129496337}[映射节点：]{style="font-family:宋体"}[IGP type]{lang="EN-US"}[为]{style="font-family:宋体"}*[igp-type]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[VRF]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vrf-index]{lang="EN-US"}*[，进程号为]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[area ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[area-value]{lang="EN-US"}*

[[Created a network node.]{lang="EN-US"}]{#struct_0_x1939_19096_1487274031}

[[成功创建一个网络信息节点]{style="font-family:宋体"}]{#struct_0_x1939_19096_1343638045}

[[Deleted an IGP mapping node: IGP type *igp-type*, LSR ID *lsr-id*, VRF index *vrf-index*, process ID *process-id*, area ID *area-value*.]{lang="EN-US"}]{#struct_0_x1939_19096_x65607576}

[[成功删除一个]{style="font-family:宋体"}[IGP]{lang="EN-US"}]{#struct_0_x1939_19096_1487339567}[映射节点：]{style="font-family:宋体"}[IGP type]{lang="EN-US"}[为]{style="font-family:宋体"}*[igp-type]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[VRF]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vrf-index]{lang="EN-US"}*[，进程号为]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[area ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[area-value]{lang="EN-US"}*[的]{style="font-family:宋体"}

[[Failed to update the mapping node.]{lang="EN-US"}]{#struct_0_x1939_19096_x1721677994}

[[更新映射节点失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_940335225}

[[Received an invalid IGP message.]{lang="EN-US"}]{#struct_0_x1939_19096_1487142959}

[[收到一个无效]{style="font-family:宋体"}[IGP]{lang="EN-US"}]{#struct_0_x1939_19096_1346604578}[消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1939_19096_117928225}

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x883089790}[设备上打开]{style="font-family:宋体"}[MPLS TE CSPF]{lang="EN-US"}[计算调试信息开关。]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道创建时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te cspf computation]{lang="EN-US"}]{#struct_0_x1939_19096_1487208495}

[\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Received a computation request message]{lang="EN-US"}[：]{style="font-family:
宋体"}[tunnel ID 1, LSP ID 20432.]{lang="EN-US"}

[\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Added a path node to the shortest path list: LSR ID 1.1.1.1; area ID 0; pre-LSR ID 0.0.0.0; in interface IP 0.0.0.0; metric 0; min bandwidth 4294967295; bandwidth 0; hop count number 0.]{lang="EN-US"}

[\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Added a path node to the heap: LSR ID 2.2.2.2; area ID 0; pre-LSR ID 1.1.1.1, in interface IP 12.1.22.2; metric 1; min bandwidth 0; bandwidth 0; hop count number 1.]{lang="EN-US"}

[\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Added a path node to the shortest path list: LSR ID 2.2.2.2; area ID 0; pre-LSR ID 1.1.1.1; in interface IP 12.1.22.2; metric 1; min bandwidth 0; bandwidth 0; hop count number 1.]{lang="EN-US"}

[\*Mar 17 06:16:53:910 2014 Sysname PCE/7/COMPUTATION: -MDC=1; Computed a path in IGP OSPF.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x2105552173}*[成功计算一条]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道路径。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_884169308}[设备上打开]{style="font-family:宋体"}[MPLS TE CSPF]{lang="EN-US"}[错误调试信息开关。配置响应发送失败时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te cspf error]{lang="EN-US"}]{#struct_0_x1939_19096_1758062730}

[\*Mar 17 06:30:21:538 2014 Sysname PCE/7/ERROR: -MDC=1; Failed to reply configurations.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_966867933}*[配置消息回应失败。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x373210893}[设备上打开]{style="font-family:宋体"}[MPLS TE CSPF TE]{lang="EN-US"}[事件调试信息开关。当内存进入三级门限时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te cspf event]{lang="EN-US"}]{#struct_0_x1939_19096_1487011887}

[\*Mar 17 06:30:21:537 2014 Sysname PCE/7/EVENT: -MDC=1; Entered the critical memory alert threshold.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1022628859}*[进入内存门限告警。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x1157382608}[设备上打开]{style="font-family:宋体"}[MPLS TE CSPF TE]{lang="EN-US"}[数据库调试信息开关。新增加]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[数据信息时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te cspf tedb]{lang="EN-US"}]{#struct_0_x1939_19096_1269675754}

[\*Mar 17 06:30:21:534 2014 Sysname PCE/7/TEDB: -MDC=1; Created an IGP mapping node: IGP type OSPF; LSR ID 1.1.1.1; VRF index 0; process ID 1; area ID 0. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1317299572}*[创建一个]{style="font-family:宋体"}[IGP]{lang="EN-US"}[类型为]{style="font-family:宋体"}[OSPF, LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[VRF]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Area ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[映射节点。]{style="font-family:宋体"}*

::: {#-2139758735 .myid}
[]{#_Toc365359826}[]{#_Toc404790693}[]{#struct_0_x1939_19096_x81418393}[]{#_Toc395684561}[]{#_Toc384279421}[]{#_Toc382581524}[]{#_Toc366499935}[]{#_Toc365359827}

**MPLS TE \-- MPLS TE调试命令 \-- debugging mpls te pce**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1272417208}

[**[debugging mpls te pce ]{lang="EN-US"}**[{ **all** \| **brpc** { **all** \| **pcreq** \| **pcrep** \[ **peer** *ip-address* \] \| **process** } \| **cspf** { **all** \| **computation** \| **process** } \| **epc** { **all** \| **pcreq** \| **pcrep** \[ **peer** *ip-address* \] \| **process** } \| **error** \| **event** \| **pcep** { **all** \| **packet** { **received** \| **sent** } \| **pcerr** \| **pcntf** \| **session** \| **fsm** \| **socket** \[ **peer** *ip-address* \] } \| **process** \|]{lang="EN-US"}]{#struct_0_x1939_19096_1450027811}[]{#_GoBack}[ **tedb** \| **timer** }]{lang="EN-US"}

[**[undo debugging mpls te pce ]{lang="EN-US"}**[{ **all** \| **brpc** { **all** \| **pcreq** \| **pcrep** \[ **peer** *ip-address* \] \| **process** } \| **cspf** { **all** \| **computation** \| **process** } \| **epc** { **all** \| **pcreq** \| **pcrep** \[ **peer** *ip-address* \] \| **process** } \| **error** \| **event** \| **pcep** { **all** \| **packet** { **received** \| **sent** } \| **pcerr** \| **pcntf** \| **session** \| **fsm** \| **socket** \[ **peer** *ip-address* \] } \| **process** \| **tedb** \| **timer** }]{lang="EN-US"}]{#struct_0_x1939_19096_747304147}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1280858393}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1939_19096_x81418392}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1272417209}

[[network-admin]{lang="EN-US"}]{#struct_0_x1939_19096_x1899812972}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1939_19096_1244730798}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x333729031}

[**[all]{lang="EN-US"}**]{#struct_0_x1939_19096_x2050288814}[：表示]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[brpc]{lang="EN-US"}**]{#struct_0_x1939_19096_x1201466634}**[：]{style="font-family:宋体"}**[表示跨域计算的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[all]{lang="EN-US"}**]{#struct_0_x1939_19096_1938541150}**[：]{style="font-family:
宋体"}**[表示跨域计算的所有调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pcreq]{lang="EN-US"}**]{#struct_0_x1939_19096_1766498266}**[：]{style="font-family:宋体"}**[表示跨域计算请求消息的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pcrep]{lang="EN-US"}**]{#struct_0_x1939_19096_x1189892499}**[：]{style="font-family:宋体"}**[表示跨域计算回复消息的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer ]{lang="EN-US"}**]{#struct_0_x1939_19096_2024991929}*[ip-address]{lang="EN-US"}***[：]{style="font-family:宋体"}**[表示指定对等体的调试信息开关。如果不指定本参数，则打开所有对等体的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[process]{lang="EN-US"}**]{#struct_0_x1939_19096_x1067738449}**[：]{style="font-family:宋体"}**[表示跨域计算的处理过程调试信息开关。]{style="font-family:宋体"}

[**[cspf]{lang="EN-US"}**]{#struct_0_x1939_19096_471884367}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[CSPF]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[all]{lang="EN-US"}**]{#struct_0_x1939_19096_766415077}**[：]{style="font-family:
宋体"}**[表示]{style="font-family:宋体"}[CSPF]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[computation]{lang="EN-US"}**]{#struct_0_x1939_19096_1232354910}**[：]{lang="EN-US" style="font-family:宋体"}**[表示]{lang="EN-US" style="font-family:宋体"}[CSPF]{lang="EN-US"}[计算的调试信息开关。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[process]{lang="EN-US"}**]{#struct_0_x1939_19096_x925744429}**[：]{lang="EN-US" style="font-family:宋体"}**[表示]{lang="EN-US" style="font-family:宋体"}[CSPF]{lang="EN-US"}[处理过程调试信息开关。]{lang="EN-US" style="font-family:宋体"}

[**[epc]{lang="EN-US"}**]{#struct_0_x1939_19096_x790483183}**[：]{style="font-family:宋体"}**[表示域内计算的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[all]{lang="EN-US"}**]{#struct_0_x1939_19096_1139198043}**[：]{style="font-family:
宋体"}**[表示域内计算的所有调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pcreq]{lang="EN-US"}**]{#struct_0_x1939_19096_x1510491688}**[：]{style="font-family:宋体"}**[表示域内计算请求消息的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pcrep]{lang="EN-US"}**]{#struct_0_x1939_19096_x732286007}**[：]{style="font-family:宋体"}**[表示域内计算回复消息的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer ]{lang="EN-US"}**]{#struct_0_x1939_19096_x1039599430}*[ip-address]{lang="EN-US"}***[：]{style="font-family:宋体"}**[表示指定对等体的调试信息开关。如果不指定本参数，则打开所有对等体的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[process]{lang="EN-US"}**]{#struct_0_x1939_19096_x1557262969}**[：]{style="font-family:宋体"}**[表示域内计算处理过程调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1939_19096_1473095616}[：表示]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1939_19096_637965015}[：表示]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[pcep]{lang="EN-US"}**]{#struct_0_x1939_19096_x1496528445}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[的调试信息开关]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[all]{lang="EN-US"}**]{#struct_0_x1939_19096_x1494553064}**[：]{style="font-family:
宋体"}**[表示]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[packet]{lang="EN-US"}**]{#struct_0_x1939_19096_1473095615}[：表示所有]{style="font-family:
宋体"}[PCEP]{lang="EN-US"}[消息调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[received]{lang="EN-US"}**]{#struct_0_x1939_19096_637899479}[：表示]{lang="EN-US" style="font-family:宋体"}[PCEP]{lang="EN-US"}[接收消息调试信息开关。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sent]{lang="EN-US"}**]{#struct_0_x1939_19096_160098956}[：表示]{style="font-family:
宋体"}[PCEP]{lang="EN-US"}[发送消息调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pcerr]{lang="EN-US"}**]{#struct_0_x1939_19096_x629982149}[：表示]{lang="EN-US" style="font-family:宋体"}[PCEP PCErr]{lang="EN-US"}[消息调试信息开关。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pcntf]{lang="EN-US"}**]{#struct_0_x1939_19096_x270603538}[：表示]{style="font-family:
宋体"}[PCEP PCNtf]{lang="EN-US"}[消息调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[session]{lang="EN-US"}**]{#struct_0_x1939_19096_x223840423}[：表示]{lang="EN-US" style="font-family:宋体"}[PCEP]{lang="EN-US"}[会话调试信息开关。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fsm]{lang="EN-US"}**]{#struct_0_x1939_19096_1473095614}**[：]{style="font-family:
宋体"}**[表示]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[socket]{lang="EN-US"}**]{#struct_0_x1939_19096_637833943}[：表示]{style="font-family:
宋体"}[PCEP]{lang="EN-US"}[套接字调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer ]{lang="EN-US"}**]{#struct_0_x1939_19096_1395981677}*[ip-address]{lang="EN-US"}*[：表示指定对等体的]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[调试信息开关。如果不指定本参数，则打开所有对等体的]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_x1939_19096_782016216}[：表示]{style="font-family:宋体"}[PCE]{lang="EN-US"}[处理过程调试信息开关。]{style="font-family:宋体"}

[**[tedb]{lang="EN-US"}**]{#struct_0_x1939_19096_x1135672465}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1939_19096_x2032628025}[：表示]{style="font-family:宋体"}[PCE]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[]{#struct_0_x1939_19096_981003212}[]{#_Toc359321187}[【描述】]{style="font-family:黑体"}

[**[debugging mpls te pce]{lang="EN-US"}**]{#struct_0_x1939_19096_136410456}[命令用来打开]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls te pce]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PCE]{lang="EN-US"}]{#struct_0_x1939_19096_x78567909}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging mpls te pce error]{lang="EN-US"}]{#struct_0_x1939_19096_749737207}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1600329833}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1473095618}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_638096087}

[[Failed to encode message: message type=*msg-type*.]{lang="EN-US"}]{#struct_0_x1939_19096_1473095617}

[[消息编码失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_638030551}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msg]{lang="EN-US"}*]{#struct_0_x1939_19096_1473095624}*[-]{lang="EN-US"}[type]{lang="EN-US"}*[：]{style="font-family:宋体"}[消息类型]{lang="EN-US" style="font-family:宋体"}

[[Failed to decode message: message type=*msg-type*, length=*msg-len*.]{lang="EN-US"}]{#struct_0_x1939_19096_637833946}

[[消息解码失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_1473095623}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msg]{lang="EN-US"}*]{#struct_0_x1939_19096_637768410}*[-]{lang="EN-US"}[type]{lang="EN-US"}*[：]{style="font-family:宋体"}[消息类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msg]{lang="EN-US"}*]{#struct_0_x1939_19096_x865556544}*[-]{lang="EN-US"}[len]{lang="EN-US"}*[：消息长度]{style="font-family:宋体"}

[[Not enough resources are available to complete the operation.]{lang="EN-US"}]{#struct_0_x1939_19096_x1959863093}

[[socket buffer]{lang="EN-US"}]{#struct_0_x1939_19096_x865556547}[分配内存失败]{style="font-family:宋体"}

[[Failed to delete PCE configurations from DBM: PCE address=*pce-address*, instance ID= *instance-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1959797557}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x1939_19096_x865556540}[中删除本地]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的配置失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pce]{lang="EN-US"}[-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1960256309}[：]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x865556541}[：]{style="font-family:宋体"}[实例号]{lang="EN-US" style="font-family:宋体"}

[[Failed to delete PCE peer configurations from DBM: PCE address= *pce-address*, instance ID= *instance-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1960190773}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x1939_19096_x865556542}[中删除]{style="font-family:宋体"}[PCE peer]{lang="EN-US"}[的配置失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pce-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1960125237}[：]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1549020104}[：]{style="font-family:宋体"}[实例号]{lang="EN-US" style="font-family:宋体"}

[[Failed to send configuration response message.]{lang="EN-US"}]{#struct_0_x1939_19096_x865556543}

[[发送配置回应消息失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1960059701}

[[Failed to send display respond message.]{lang="EN-US"}]{#struct_0_x1939_19096_x865556536}

[[发送显示回应消息失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1959863098}

[[Failed to write message to queue: message type=*msg-type,* sub message type=*sub-msg-type*.]{lang="EN-US"}]{#struct_0_x1939_19096_x865556537}

[[往队列里写消息失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1959797562}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msg]{lang="EN-US"}*]{#struct_0_x1939_19096_1090758592}*[-]{lang="EN-US"}[type]{lang="EN-US"}*[：]{style="font-family:宋体"}[消息类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sub]{lang="EN-US"}*]{#struct_0_x1939_19096_224965485}*[-]{lang="EN-US"}[msg]{lang="EN-US"}[-]{lang="EN-US"}[type]{lang="EN-US"}*[：]{style="font-family:
  宋体"}[子消息类型]{lang="EN-US" style="font-family:宋体"}

[[Failed to write an event.]{lang="EN-US"}]{#struct_0_x1939_19096_1090758591}

[[写事件失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_224899949}

[[Failed to set parameter: type name=*type-name,* option type=*option-type*.]{lang="EN-US"}]{#struct_0_x1939_19096_1090758590}

[[设置参数失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_224834413}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1090758589}[：]{style="font-family:宋体"}[参数名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[option-type]{lang="EN-US"}*]{#struct_0_x1939_19096_224375660}[：]{style="font-family:宋体"}[选择类型]{lang="EN-US" style="font-family:宋体"}

[[Failed to get parameter *type-name*.]{lang="EN-US"}]{#struct_0_x1939_19096_1090758596}

[[获取参数失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_1090758595}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type-name]{lang="EN-US"}*]{#struct_0_x1939_19096_225162093}[：]{style="font-family:宋体"}[参数名称]{lang="EN-US" style="font-family:宋体"}

[[Failed to create a TCP socket.]{lang="EN-US"}]{#struct_0_x1939_19096_1090758594}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1939_19096_225096557}[失败]{style="font-family:宋体"}

[[Failed to bind a socket: error=*error-info*.]{lang="EN-US"}]{#struct_0_x1939_19096_1090758593}

[[绑定]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1939_19096_225031021}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error]{lang="EN-US"}*]{#struct_0_x1939_19096_1090758600}*[-]{lang="EN-US"}[info]{lang="EN-US"}*[：]{style="font-family:宋体"}[错误]{lang="EN-US" style="font-family:宋体"}[信]{style="font-family:宋体"}[息]{lang="EN-US" style="font-family:宋体"}

[[Failed to listen to a TCP socket: error=*error-info*.]{lang="EN-US"}]{#struct_0_x1939_19096_1798812532}

[[监听]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1939_19096_1090758599}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error]{lang="EN-US"}*]{#struct_0_x1939_19096_224375661}*[-]{lang="EN-US"}[info]{lang="EN-US"}*[：]{style="font-family:宋体"}[错误]{lang="EN-US" style="font-family:宋体"}[信]{style="font-family:宋体"}[息]{lang="EN-US" style="font-family:宋体"}

[[Failed to receive TCP data from socket *socket-id*: error=*error-info*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1247893568}

[[从]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1939_19096_13249908}[接收]{style="font-family:宋体"}[TCP]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[socket-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1247893569}[：]{style="font-family:宋体"}[套接字]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error]{lang="EN-US"}*]{#struct_0_x1939_19096_x1247893570}*[-]{lang="EN-US"}[info]{lang="EN-US"}*[：]{style="font-family:宋体"}[错误]{lang="EN-US" style="font-family:宋体"}[信]{style="font-family:宋体"}[息]{lang="EN-US" style="font-family:宋体"}

[[Failed to create TCP accept socket: error=*error-info*.]{lang="EN-US"}]{#struct_0_x1939_19096_x342914916}

[[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1939_19096_x1247893571}[接收]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error]{lang="EN-US"}*]{#struct_0_x1939_19096_x1908998857}*[-]{lang="EN-US"}[info]{lang="EN-US"}*[：]{style="font-family:宋体"}[错误]{lang="EN-US" style="font-family:宋体"}[信]{style="font-family:宋体"}[息]{lang="EN-US" style="font-family:宋体"}

[[Failed to establish a connection to RIB.]{lang="EN-US"}]{#struct_0_x1939_19096_x1247893564}

[[连接]{style="font-family:宋体"}[RIB]{lang="EN-US"}]{#struct_0_x1939_19096_1982618376}[失败]{style="font-family:宋体"}

[[Failed to create the timer.]{lang="EN-US"}]{#struct_0_x1939_19096_x1247893565}

[[定时器创建失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_416534435}

[[Failed to set the timer: sec=*sec,* nsec=*nsec*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1247893566}

[[设置定时器时间失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1149549506}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sec]{lang="EN-US"}*]{#struct_0_x1939_19096_x1247893567}[：]{style="font-family:宋体"}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nsec]{lang="EN-US"}*]{#struct_0_x1939_19096_1579333849}[：]{style="font-family:宋体"}[微秒]{lang="EN-US" style="font-family:宋体"}

[[Failed to reset the timer.]{lang="EN-US"}]{#struct_0_x1939_19096_x1247893560}

[[重置定时器失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1247893561}

[[Failed to get the configuration: instance=*instance-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1909064393}

[[获取配置失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x2057197632}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1538942804}[：]{style="font-family:宋体"}[实例号]{lang="EN-US" style="font-family:宋体"}

[[Failed to save request-id-number to DBM.]{lang="EN-US"}]{#struct_0_x1939_19096_829135919}

[[保存]{style="font-family:宋体"}[request-id-number]{lang="EN-US"}]{#struct_0_x1939_19096_x1479386837}[到数据库失败]{style="font-family:宋体"}

[[Received an invalid message: type=*msg-type*, length=*msg-len*.]{lang="EN-US"}]{#struct_0_x1939_19096_x2057197633}

[[接收到不合法消息]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1899747436}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[msg]{lang="EN-US"}]{#struct_0_x1939_19096_x1016896054}[-]{lang="EN-US"}[type]{lang="EN-US"}[：]{style="font-family:宋体"}[消息类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[msg]{lang="EN-US"}]{#struct_0_x1939_19096_x773965060}[-]{lang="EN-US"}[len]{lang="EN-US"}[：消息长度]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging mpls te pce event]{lang="EN-US"}]{#struct_0_x1939_19096_1593225078}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_553479069}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x825182526}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x2057197635}

[[Sent an event to IGP: event type=*event-type*, result=*result.*]{lang="EN-US"}]{#struct_0_x1939_19096_x1135658277}

[[发送]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x2057197628}[事件到]{style="font-family:宋体"}[IGP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x732439286}[：]{style="font-family:宋体"}[事件类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_x1939_19096_x2057197629}[：]{style="font-family:宋体"}[发送结果]{lang="EN-US" style="font-family:宋体"}

[[Failed to keep current connection (found same protocol).]{lang="EN-US"}]{#struct_0_x1939_19096_x2057197631}

[[当前连接断开]{style="font-family:宋体"}]{#struct_0_x1939_19096_1189940551} [（发现相同协议的连接）]{style="font-family:宋体"}

[[Received an event from IGP: event type=*event-type*.]{lang="EN-US"}]{#struct_0_x1939_19096_x333663495}

[[接收来自]{style="font-family:宋体"}[IGP]{lang="EN-US"}]{#struct_0_x1939_19096_378689399}[的]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_266533093}[：]{style="font-family:宋体"}[事件类型]{lang="EN-US" style="font-family:宋体"}

[[Received a message with unknown TLV type=*tlv-type*.]{lang="EN-US"}]{#struct_0_x1939_19096_x2057197624}

[[收到含有未知消息类型的]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1939_19096_1593159542}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tlv]{lang="EN-US"}[-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x787398882}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[Received a PCUpd message.]{lang="EN-US"}]{#struct_0_x1939_19096_x100882498}

[[接收到一个]{style="font-family:宋体"}[PCUpd]{lang="EN-US"}]{#struct_0_x1939_19096_1595476151}[消息]{style="font-family:宋体"}

[[Received a PCRpt message.]{lang="EN-US"}]{#struct_0_x1939_19096_x1327218341}

[[接收到一个]{style="font-family:宋体"}[PCRpt]{lang="EN-US"}]{#struct_0_x1939_19096_x100882499}[消息]{style="font-family:宋体"}

[[Received a PCRpt message from a stateless session.]{lang="EN-US"}]{#struct_0_x1939_19096_1595541687}

[[从无状态会话收到一个]{style="font-family:宋体"}[PCRpt]{lang="EN-US"}]{#struct_0_x1939_19096_x100882492}[消息]{style="font-family:宋体"}

[[Received a PCUpd message from a stateless session.]{lang="EN-US"}]{#struct_0_x1939_19096_x1496462909}

[[从无状态会话收到一个]{style="font-family:宋体"}[PCUpd]{lang="EN-US"}]{#struct_0_x1939_19096_x236995421}[消息]{style="font-family:宋体"}

[[Sent an event to IGP: event type=*event-type*, result=*result.*]{lang="EN-US"}]{#struct_0_x1939_19096_1122671599}

[[发送]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x772102080}[事件到]{style="font-family:宋体"}[IGP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_704113449}[：]{style="font-family:宋体"}[事件类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_x1939_19096_873289678}[：]{style="font-family:宋体"}[发送结果]{lang="EN-US" style="font-family:宋体"}

[[Sent an event to IGP: event type=*event-type*, instance=*instance-id*, process ID=*process-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_782081752}

[[成功发送]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x1481922875}[事件到]{style="font-family:宋体"}[IGP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_1229939831}[：]{style="font-family:宋体"}[事件类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1536773163}[：]{style="font-family:宋体"}[实例号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1563265358}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging mpls te pce process]{lang="EN-US"}]{#struct_0_x1939_19096_1594886327}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_561193872}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x2141699876}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x100882494}

[[Added a new PCE *pce-address* to synchronization group.]{lang="EN-US"}]{#struct_0_x1939_19096_1595214007}

[[添加新的]{style="font-family:宋体"}[PCE]{lang="EN-US"}]{#struct_0_x1939_19096_x100882495}[到同步组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[p]{lang="EN-US"}*]{#struct_0_x1939_19096_1595279543}*[ce]{lang="EN-US"}[-address]{lang="EN-US"}*[：]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[Can\'t find matched request: reply ID=*reply-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x100882488}

[[没有找到匹配的请求]{style="font-family:宋体"}]{#struct_0_x1939_19096_1595476152}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reply-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1327283877}[：回复消息]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Received an invalid CSPF result: reply ID=*reply-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1946801603}

[[接收到一个不合法的]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x243402240}[结果]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reply-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1746196452}[：回复]{style="font-family:宋体"}[消息]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}*[ ]{lang="EN-US"}*

[[Received a reply from CSPF: reply ID=*reply-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_696895821}

[[从]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x451571179}[接收到一个回复消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reply-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1322681701}[：回复]{style="font-family:宋体"}[消息]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Received a request from CSPF: source address=*source-address*, dest address=*dest-address*, tunnel ID=*tunnel-id*, local LSP ID=*local-lsp-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x539514823}

[[从]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_1363808265}[接收到一个请求消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1431392782}[：源]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-address]{lang="EN-US"}*]{#struct_0_x1939_19096_2066525556}[：目的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tunnel-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1406201654}[：隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[local-lsp-id]{lang="EN-US"}*]{#struct_0_x1939_19096_361270959}[：本地]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}

[[Received a request cancellation from CSPF: source address=*source-address*, dest address=*dest-address*, tunnel ID=*tunnel-id*, local LSP ID=*local-lsp-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x203739911}

[[从]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x416937223}[接收到一个请求取消消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-address]{lang="EN-US"}*]{#struct_0_x1939_19096_86198171}[：源]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-address]{lang="EN-US"}*]{#struct_0_x1939_19096_159882287}[：目的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tunnel-id]{lang="EN-US"}*]{#struct_0_x1939_19096_291663477}[：隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[local-lsp-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x925840555}[：本地]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}

[[Received a cancellation of all requests from CSPF.]{lang="EN-US"}]{#struct_0_x1939_19096_x803274281}

[[从]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x1354382556}[接收到一个取消所有请求的消息]{style="font-family:宋体"}

[[Received a synchronization start message from CSPF.]{lang="EN-US"}]{#struct_0_x1939_19096_1725966228}

[[从]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x946452092}[接收到一个开始同步的消息]{style="font-family:宋体"}

[[Received a synchronization end message from CSPF.]{lang="EN-US"}]{#struct_0_x1939_19096_x1188288481}

[[从]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x765371359}[接收到一个同步结束的消息]{style="font-family:宋体"}

[[Sent an event to PCECP: event type=*event-type*, sub event type=*sub-event-type*.]{lang="EN-US"}]{#struct_0_x1939_19096_x100882489}

[[发送一个事件给]{style="font-family:宋体"}[PCECP]{lang="EN-US"}]{#struct_0_x1939_19096_1595541688}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_1475258304}[：事件类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sub-event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x1360555919}[：]{lang="EN-US" style="font-family:
  宋体"}[子事件类型]{style="font-family:宋体"}

[[Sent an event to CSPF: event type=*event-type*.]{lang="EN-US"}]{#struct_0_x1939_19096_1475258303}

[[发送一个事件给]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x1360097167}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_1475258302}[：事件类型]{style="font-family:宋体"}

[[Sent a result to CSPF: source address=*source-address*, dest address=*dest-address*, tunnel ID=*tunnel-id*, local LSP ID=*local-lsp-id.*]{lang="EN-US"}]{#struct_0_x1939_19096_x1360162703}

[[发送计算结果给]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_1475258301}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1360228239}[：源]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-address]{lang="EN-US"}*]{#struct_0_x1939_19096_150806560}[：目的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tunnel-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1475258308}[：隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[local-lsp-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1360818063}[：本地]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}

[[Sent a request to CSPF: source address=*source-address*, dest address=*dest-address*, reply ID=*reply-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_1475258307}

[[发送请求消息到]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x1360359311}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1475258306}[：源]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1360424847}[：目的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reply-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1475258305}[：回复消息]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Sent a request cancellation to CSPF: reply ID=*reply-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1360490383}

[[发送请求取消消息到]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_1475258312}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reply-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1360162704}[：回复消息]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Sent an update message to CSPF.]{lang="EN-US"}]{#struct_0_x1939_19096_1475258311}

[[发送]{style="font-family:宋体"}[update]{lang="EN-US"}]{#struct_0_x1939_19096_x1360228240}[消息到]{style="font-family:宋体"}[CSPF]{lang="EN-US"}

[[Sent a report message to CSPF.]{lang="EN-US"}]{#struct_0_x1939_19096_x863393856}

[[发送]{style="font-family:宋体"}[report]{lang="EN-US"}]{#struct_0_x1939_19096_x1754300743}[消息到]{style="font-family:宋体"}[CSPF]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging mpls te pce timer]{lang="EN-US"}]{#struct_0_x1939_19096_1092921277}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_591347596}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1229972206}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1540875281}

[[Created the *timer-name* timer (*sec-count* sec) for a session: peer=*peer-address:instance-id*, session role=*session-role*.]{lang="EN-US"}]{#struct_0_x1939_19096_1092921284}

[[会话创建]{style="font-family:宋体"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1229906675}[定时器成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1092921283}[：]{style="font-family:宋体"}[定时器的名字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sec-count]{lang="EN-US"}*]{#struct_0_x1939_19096_1229710067}[：定时器设置时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1092921282}[：]{style="font-family:宋体"}[对端的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1229775603}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-role]{lang="EN-US"}*]{#struct_0_x1939_19096_1092921281}[：]{style="font-family:宋体"}[本地会话的角色]{lang="EN-US" style="font-family:宋体"}

[[Created the request timer: PCE address=*pce-address,* request ID=*request-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_2129250755}

[[创建请求定时器成功]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1588451558}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pce-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1017931978}[：]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_112828120}[：请求消息]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Created the *timer-name* timer: instance=*instance-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1604998979}

[[创建]{style="font-family:宋体"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1114559250}[定时器成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_x1685703492}[：]{style="font-family:宋体"}[定时器的名字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x303242908}[：]{style="font-family:宋体"}[实例号]{lang="EN-US" style="font-family:宋体"}

[[Deleted the *timer-name* timer for a session: peer=*peer-address:instance-id*, session role=*session-role*.]{lang="EN-US"}]{#struct_0_x1939_19096_1229578995}

[[会话删除]{style="font-family:宋体"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1092921288}[定时器成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1229120243}[：]{style="font-family:宋体"}[定时器的名字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1601385413}[：]{style="font-family:宋体"}[对端的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1092921287}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-role]{lang="EN-US"}*]{#struct_0_x1939_19096_1229972211}[：]{style="font-family:宋体"}[本地会话的角色]{lang="EN-US" style="font-family:宋体"}

[[Deleted the request timer: PCE address=*pce-address,* request ID=*request-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_1678912061}

[[删除请求定时器成功]{style="font-family:宋体"}]{#struct_0_x1939_19096_2045582619}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pce-address]{lang="EN-US"}*]{#struct_0_x1939_19096_176836161}[：]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x243336704}[：请求消息]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Request timer expired: PCE address=*pce-address,* request ID=*request-id.*]{lang="EN-US"}]{#struct_0_x1939_19096_x1348774581}

[[请求定时器超时]{style="font-family:宋体"}]{#struct_0_x1939_19096_x534359913}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pce-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1044508019}[：]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1203974448}[：请求]{style="font-family:宋体"}[消息]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[The *timer-name* timer expired for a session: peer=*peer-address:instance-id*, session role=*session-role*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1245730880}

[[会话]{style="font-family:宋体"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1802038243}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_x1245730881}[：]{style="font-family:宋体"}[定时器的名字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_235954302}[：]{style="font-family:宋体"}[对端的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i]{lang="EN-US"}[nstance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1245730882}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-role]{lang="EN-US"}*]{#struct_0_x1939_19096_639238829}[：]{style="font-family:宋体"}[本地会话的角色]{lang="EN-US" style="font-family:宋体"}

[[The *timer-name* timer expired: instance=*instance-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1245730877}

[*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1397770676}[定时器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[timer-name]{lang="EN-US"}*]{#struct_0_x1939_19096_x1245730878}[：]{style="font-family:宋体"}[定时器的名字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1444824843}[：]{style="font-family:宋体"}[实例号]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging mpls te pce pcep packet]{lang="EN-US"}]{#struct_0_x1939_19096_x1128743140}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_636848299}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x2055034947}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1575015436}

[[Received *msg-type* message from a peer: peer=*peer-address:instance-id*, message content: .]{lang="EN-US"}]{#struct_0_x1939_19096_1322747237}

[[接收来自对等体的]{style="font-family:宋体"}*[msg-type]{lang="EN-US"}*]{#struct_0_x1939_19096_1044496103}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msg]{lang="EN-US"}*]{#struct_0_x1939_19096_x1743419472}*[-]{lang="EN-US"}[type]{lang="EN-US"}*[：]{style="font-family:宋体"}[消息]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1406136118}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1597126189}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[[Sent *msg-type* message to a peer: peer=*peer-address:instance-id*, message content: .]{lang="EN-US"}]{#struct_0_x1939_19096_x1062125125}

[[发送]{style="font-family:宋体"}*[msg-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x1196710716}[消息给对等体]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[msg]{lang="EN-US"}*]{#struct_0_x1939_19096_622255360}*[-]{lang="EN-US"}[type]{lang="EN-US"}*[：]{style="font-family:宋体"}[消息]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1497992345}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x2107056545}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging mpls te pce pcep pcerr]{lang="EN-US"}]{#struct_0_x1939_19096_8734887}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_625897786}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_407611486}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x2055034937}

[[Received a PCEP error from peer: error info=*error-info,* peer=*peer-address:instance-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_159947823}

[[接收来自对等体的]{style="font-family:宋体"}[PCErr]{lang="EN-US"}]{#struct_0_x1939_19096_741716819}[消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error]{lang="EN-US"}*]{#struct_0_x1939_19096_79138913}*[-]{lang="EN-US"}[info]{lang="EN-US"}*[：错误信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_262242319}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_948340138}[：对端]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[Sent a PCEP error to peer: error info=*error-info,* peer=*peer-address:instance-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_1726031764}

[[发送]{style="font-family:宋体"}[PCErr]{lang="EN-US"}]{#struct_0_x1939_19096_1246734464}[消息给对等体]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error]{lang="EN-US"}*]{#struct_0_x1939_19096_x2008387313}*[-]{lang="EN-US"}[info]{lang="EN-US"}*[：错误信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1957450635}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_915022990}[：对端地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[debugging mpls te pce pcep fsm]{lang="EN-US"}]{#struct_0_x1939_19096_1205182352}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_650698604}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1790065306}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x98719804}

[[Session received an event: peer=*peer-address:instance-id,* session role*=session-role,* event type=*event-type,* state=*session-state*.]{lang="EN-US"}]{#struct_0_x1939_19096_x751132789}

[[会话接收]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x98719805}[类型事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x751132788}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x98719806}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-role]{lang="EN-US"}*]{#struct_0_x1939_19096_x751132791}[：]{style="font-family:宋体"}[会话角色]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x98719807}[：]{style="font-family:宋体"}[事件类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-state]{lang="EN-US"}*]{#struct_0_x1939_19096_x751132790}[：]{style="font-family:宋体"}[会话状态]{lang="EN-US" style="font-family:宋体"}

[[Status of the session changed from *presession-state* to *cursession-state*: peer=*peer-address:instance-id,* session role*=session-role*.]{lang="EN-US"}]{#struct_0_x1939_19096_740362438}

[[会话状态改变]{style="font-family:宋体"}]{#struct_0_x1939_19096_x98719800}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x751132785}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x98719801}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-role]{lang="EN-US"}*]{#struct_0_x1939_19096_x751132784}[：]{style="font-family:宋体"}[会话角色]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[presession-state]{lang="EN-US"}*]{#struct_0_x1939_19096_1468770240}[：]{style="font-family:宋体"}[改变之前会话状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cursession-state]{lang="EN-US"}*]{#struct_0_x1939_19096_x656518289}[：当前]{style="font-family:宋体"}[的会话状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[debugging mpls te pce pcep session]{lang="EN-US"}]{#struct_0_x1939_19096_1306105673}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_641849889}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1468770239}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x656977042}

[[Created a new session: peer=*peer-address:instance-id,* session role*=session-role*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1342258516}

[[创建新的会话]{style="font-family:宋体"}]{#struct_0_x1939_19096_1468770238}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x657042578}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1468770237}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-role]{lang="EN-US"}*]{#struct_0_x1939_19096_x656321682}[：]{style="font-family:宋体"}[会话角色]{lang="EN-US" style="font-family:宋体"}

[[Destroyed the session: peer=*peer-address:instance-id,* session role*=session-role*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1008697948}

[[释放会话资源成功]{style="font-family:宋体"}]{#struct_0_x1939_19096_1468770244}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x656256145}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1468770243}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-role]{lang="EN-US"}*]{#struct_0_x1939_19096_x656583825}[：]{style="font-family:宋体"}[会话角色]{lang="EN-US" style="font-family:宋体"}

[[Failed to get the local address for session: peer=*peer-address:instance-id,* session role*=session-role*.]{lang="EN-US"}]{#struct_0_x1939_19096_1468770242}

[[会话获取本地地址失败]{style="font-family:宋体"}]{#struct_0_x1939_19096_x656649361}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_925901577}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1468770241}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[session-role]{lang="EN-US"}*]{#struct_0_x1939_19096_x656452753}[：]{style="font-family:宋体"}[会话角色]{lang="EN-US" style="font-family:宋体"}

[[Opened a TCP connection: socket=*socket-id*, peer=*peer-address:instance-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_1468770248}

[[打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1939_19096_x657042577}[连接]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1468770247}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x656321681}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[socket-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x869881920}[：]{style="font-family:宋体"}[套接字]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[D]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[debugging mpls te pce pcep socket]{lang="EN-US"}]{#struct_0_x1939_19096_x1069640091}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_670007725}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_952805402}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x869881921}

[[Accepted a new socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_2129316291}

[[接收新的]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1939_19096_360988045}[连接]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[socket-id]{lang="EN-US"}*]{#struct_0_x1939_19096_426646012}[：]{style="font-family:宋体"}[套接字]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[D]{lang="EN-US"}

[[Closed the TCP server: socket=*socket-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1069771163}

[[关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1939_19096_x869881923}[服务端成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[socket-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1069836699}[：]{style="font-family:宋体"}[套接字]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[D]{lang="EN-US"}

[[Failed to create a TCP connection to transport address *transport-address*: error=*error-info*.]{lang="EN-US"}]{#struct_0_x1939_19096_112893656}

[[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1939_19096_774064517}[连接传输地址失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[transport-address]{lang="EN-US"}*]{#struct_0_x1939_19096_982043479}[：传输]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error]{lang="EN-US"}*]{#struct_0_x1939_19096_x1465287025}*[-]{lang="EN-US"}[info]{lang="EN-US"}*[：]{style="font-family:宋体"}[错误信息]{lang="EN-US" style="font-family:宋体"}

[[Failed to send TCP data: peer *peer-address:instance-id*.  Error=*error-info*]{lang="EN-US"}]{#struct_0_x1939_19096_311980410}

[[给对端发送]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1939_19096_x1577005657}[数据失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1678977597}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1065846035}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error]{lang="EN-US"}*]{#struct_0_x1939_19096_x1832486398}*[-]{lang="EN-US"}[info]{lang="EN-US"}*[：]{style="font-family:宋体"}[错误信息]{lang="EN-US" style="font-family:宋体"}

[[Opened the TCP server: socket=*socket-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x452296298}

[[打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1939_19096_1346254396}[服务端成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[socket-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x261459549}[：]{style="font-family:宋体"}[套接字]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[D]{lang="EN-US"}

[[TCP is down abnormally: socket=*socket-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1408343409}

[[TCP ]{lang="EN-US"}]{#struct_0_x1939_19096_x869881916}[异常关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[socket-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1069509022}[：]{style="font-family:宋体"}[套接字]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[D]{lang="EN-US"}

[[The message might be too large for peer *peer-address* to process.]{lang="EN-US"}]{#struct_0_x1939_19096_1086433216}

[[消息太大对端可能不能处理]{style="font-family:宋体"}]{#struct_0_x1939_19096_459342418}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1086433215}[：]{style="font-family:宋体"}[对端地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[debugging mpls te pce brpc pcreq]{lang="EN-US"}]{#struct_0_x1939_19096_459539026}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_954389614}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_201802628}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1086433214}

[[Received a PCReq from peer (*peer-address*, *instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* END-POINTS: source=*source-address*, destination=*dest-address*]{lang="EN-US"}]{#struct_0_x1939_19096_x243271168}

[[从对端接收到一个请求消息]{style="font-family:宋体"}]{#struct_0_x1939_19096_182289729}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1906490948}[：对端地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1322812773}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x2094916589}[：请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VSPT-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_538568388}[：]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[计算标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[O-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1302859119}[：松散、严格路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[B-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1406070582}[：双向、单向路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1411603373}[：重优化路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority-value]{lang="EN-US"}*]{#struct_0_x1939_19096_858992662}[：计算优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-address]{lang="EN-US"}*]{#struct_0_x1939_19096_185629529}[：源地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-address]{lang="EN-US"}*]{#struct_0_x1939_19096_160013359}[：]{style="font-family:宋体"}[目的地址]{lang="EN-US" style="font-family:宋体"}

[[Sent a PCReq to peer (*peer-address*, *instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* END-POINTS: source=*source-address*, destination=*dest-address*]{lang="EN-US"}]{#struct_0_x1939_19096_x2125222106}

[[发送一个请求消息到对端]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1129992732}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1614942367}[：对端地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x941966747}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1726097300}[：请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VSPT-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x659374268}[：]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[计算标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[O-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_18227157}[：松散、严格路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[B-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1412417105}[：双向、单向路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1002786055}[：重优化路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority-value]{lang="EN-US"}*]{#struct_0_x1939_19096_x1477470526}[：计算优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x173717923}[：源地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1933724075}[：]{style="font-family:宋体"}[目的地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[debugging mpls te pce brpc pcrep]{lang="EN-US"}]{#struct_0_x1939_19096_899484566}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_940802558}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x187444975}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1252218947}

[[PCE list: *pce-list* Sent a PCRep to peer (*peer-address, instance-id*): Request-ID-number: *request-id* Flags: SPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* Path: *interfere-address-list*]{lang="EN-US"}]{#struct_0_x1939_19096_x1829398789}

[[发送一个回复消息到对端]{style="font-family:宋体"}]{#struct_0_x1939_19096_527554673}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pce-list]{lang="EN-US"}*]{#struct_0_x1939_19096_x1252218940}[：]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址列表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1706053620}[：传输]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1252218941}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1022829735}[：请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VSPT-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_664726469}[：]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[计算标志]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[O-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1252218942}[：松散、严格路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[B-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1426114262}[：双向、单向路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1252218943}[：重优化路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority-value]{lang="EN-US"}*]{#struct_0_x1939_19096_139969679}[：计算优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i]{lang="EN-US"}*]{#struct_0_x1939_19096_x730119768}*[nterfere-address]{lang="EN-US"}[-list]{lang="EN-US"}*[：接口地址列表]{style="font-family:宋体"}

[[PCE list: *pce-list* Received a PCRep from peer: (*peer-address, instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* Path: *interfere-address-list*]{lang="EN-US"}]{#struct_0_x1939_19096_x1252218936}

[[从对端接收一个回复消息]{style="font-family:宋体"}]{#struct_0_x1939_19096_899943318}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pce-list]{lang="EN-US"}*]{#struct_0_x1939_19096_x1252218937}[：]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址列表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1828940037}[：传输]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x2061523008}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x913397875}[：请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VSPT-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x979941666}[：]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[计算标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[O-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x2061523009}[：松散、严格路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[B-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1815485480}[：双向、单向路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x2061523010}[：重优化路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority-value]{lang="EN-US"}*]{#struct_0_x1939_19096_x1269562699}[：计算优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[i]{lang="EN-US"}*]{#struct_0_x1939_19096_x2061523011}*[nterfere-address]{lang="EN-US"}[-list]{lang="EN-US"}*[：]{style="font-family:宋体"}[接口地址列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[debugging mpls te pce brpc process]{lang="EN-US"}]{#struct_0_x1939_19096_1459320656}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_966093393}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1707025713}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1968335601}

[[Failed to get the external PCE for inter-domain request.]{lang="EN-US"}]{#struct_0_x1939_19096_x2061523004}

[[域间路径计算请求获取]{style="font-family:宋体"}[PCE]{lang="EN-US"}]{#struct_0_x1939_19096_699740233}[失败]{style="font-family:宋体"}

[[Number of requests reached the limit.]{lang="EN-US"}]{#struct_0_x1939_19096_x2061523005}

[[请求数目达到最大数目]{style="font-family:宋体"}]{#struct_0_x1939_19096_x866343708}

[ ]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[debugging mpls te pce epc pcreq]{lang="EN-US"}]{#struct_0_x1939_19096_x1313309004}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_962693189}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x2061523006}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1862539647}

[[Received a PCReq from peer (*peer-address*, *instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* END-POINTS: source=*source-address*, destination=*dest-address*]{lang="EN-US"}]{#struct_0_x1939_19096_112959192}

[[从对端接收一个请求消息]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1250121770}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1679043133}[：对端地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_2067704228}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_2137659802}[：请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VSPT-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_995571993}[：]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[计算标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[O-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x145591560}[：松散、严格路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[B-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1130923468}[：双向、单向路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x243205632}[：重优化路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority-value]{lang="EN-US"}*]{#struct_0_x1939_19096_584692440}[：优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1373413537}[：源地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x738625243}[：]{style="font-family:宋体"}[目的地址]{lang="EN-US" style="font-family:宋体"}

[[Sent a PCReq to peer (*peer-address*, *instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* END-POINTS: source=*source-address*, destination=*dest-address*]{lang="EN-US"}]{#struct_0_x1939_19096_93363153}

[[发送一个请求消息到对端]{style="font-family:宋体"}]{#struct_0_x1939_19096_1322878309}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x2132879440}[：对端地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x281946813}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x2020069754}[：请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VSPT-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1737630922}[：]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[计算标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[O-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1406005046}[：松散、严格路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[B-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_2055763939}[：双向、单向路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_x1963803999}[：重优化路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority-value]{lang="EN-US"}*]{#struct_0_x1939_19096_x1964343130}[：计算优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[source-address]{lang="EN-US"}*]{#struct_0_x1939_19096_160078895}[：源地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-address]{lang="EN-US"}*]{#struct_0_x1939_19096_171427931}[：]{style="font-family:宋体"}[目的地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[debugging mpls te pce epc pcrep]{lang="EN-US"}]{#struct_0_x1939_19096_x1368240502}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_986450070}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x120589240}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1647909552}

[[Received a PCRep from peer (*peer-address, instance-id*): ]{lang="EN-US"}]{#struct_0_x1939_19096_x105207864}

[[Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* Path: *interfere-address-list*]{lang="EN-US"}]{#struct_0_x1939_19096_x1368043893}

[[从对端接收一个回复消息]{style="font-family:宋体"}]{#struct_0_x1939_19096_x105207865}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1367978357}[：传输]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1709109869}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1470932928}[：请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VSPT-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1592335636}[：]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[计算标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[O-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1470932927}[：松散、严格路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[B-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1591483668}[：]{style="font-family:宋体"} [双向、单向路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1470932926}[：重优化路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority-value]{lang="EN-US"}*]{#struct_0_x1939_19096_1591418132}[：优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Interfere-address]{lang="EN-US"}*]{#struct_0_x1939_19096_900379475}*[-list]{lang="EN-US"}*[：接口地址列表]{style="font-family:宋体"}

[[Sent a PCRep to peer (*peer-address, instance-id*): Request-ID-number: *request-id* Flags: VSPT=*VSPT-flag*, O=*O-flag*, B=*B-flag*, R=*R-flag*, pri=*priority-value* Path: *interfere-address-list*]{lang="EN-US"}]{#struct_0_x1939_19096_1470932925}

[[发送一个回复消息到对端]{style="font-family:宋体"}]{#struct_0_x1939_19096_1591614740}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[peer-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1470932932}[：传输]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1591680277}[：实例号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[request-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x335062939}[：请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VSPT-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1470932931}[：]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[计算标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[O-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1591876885}[：松散、严格路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[B-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1470932930}[：双向、单向路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[R-flag]{lang="EN-US"}*]{#struct_0_x1939_19096_1591811349}[：重优化路径标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority-value]{lang="EN-US"}*]{#struct_0_x1939_19096_1470932929}[：优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Interfere-address]{lang="EN-US"}*]{#struct_0_x1939_19096_1592401172}*[-list]{lang="EN-US"}*[：接口地址列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[debugging mpls te pce epc process]{lang="EN-US"}]{#struct_0_x1939_19096_x1600068724}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_978832490}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x31947204}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_1470932936}

[[Failed to get an external PCE for intra-domain request.]{lang="EN-US"}]{#struct_0_x1939_19096_1591418133}

[[域内路径计算请求获取]{style="font-family:宋体"}[PCE]{lang="EN-US"}]{#struct_0_x1939_19096_1470932935}[失败]{style="font-family:宋体"}

[[Number of requests reached the limit.]{lang="EN-US"}]{#struct_0_x1939_19096_1591614741}

[[请求消息达到最大个数]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1095292206}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x867719232}

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x1607798483}[打开]{style="font-family:宋体"}[PCE]{lang="EN-US"}[事件调试信息开关，配置本地]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[10.10.10.1]{lang="EN-US"}[后，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pce event]{lang="EN-US"}]{#struct_0_x1939_19096_1934301064}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls te]{lang="EN-US"}

[\[Sysname-te\] pce address 10.10.10.1]{lang="EN-US"}

[\*Dec 20 12:24:00:581 2013 Sysname PCECP/7/EVENT: -MDC=1; Sent an event (advertise local PCE) to IGP successfully. Instance: 0, process ID: 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1431199583}*[向]{style="font-family:宋体"}[IGP]{lang="EN-US"}[通告本地]{style="font-family:宋体"}[PCE]{lang="EN-US"}[，实例号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_1433346577}[打开]{style="font-family:宋体"}[PCE]{lang="EN-US"}[定时器调试信息开关，配置本地]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[后，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pce timer]{lang="EN-US"}]{#struct_0_x1939_19096_x1485558777}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls te]{lang="EN-US"}

[\[Sysname-te\] pce address 1.1.1.1]{lang="EN-US"}

[\*Dec 20 13:10:30:215 2013 PE1 PCECP/7/TIMER: -MDC=1; Created the OpenWait timer (60 sec) successfully for session (3.3.3.1:0, passive).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x867719233}*[会话创建]{style="font-family:宋体"}[OpenWait]{lang="EN-US"}[定时器成功，对端地址为]{style="font-family:宋体"}[3.3.3.1]{lang="EN-US"}[，实例号为：]{style="font-family:宋体"}[0]{lang="EN-US"}[，会话角色为：]{style="font-family:宋体"}[passive]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Dec 20 13:10:30:215 2013 PE1 PCECP/7/TIMER: -MDC=1; Deleted the OpenWait timer successfully for session (3.3.3.1:0, passive).]{lang="EN-US"}]{#struct_0_x1939_19096_x1607732947}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x637681013}*[会话删除]{style="font-family:宋体"}[OpenWait]{lang="EN-US"}[定时器成功，对端地址为]{style="font-family:宋体"}[3.3.3.1]{lang="EN-US"}[，实例号为：]{style="font-family:宋体"}[0]{lang="EN-US"}[，会话角色为：]{style="font-family:宋体"}[passive]{lang="EN-US"}[。]{style="font-family:宋体"}*[]{#_Toc359321188}

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x1117098438}[打开]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[的发送消息调试信息开关，设备上会话处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态时，如果]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[定时器超时，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pcep packet sent]{lang="EN-US"}]{#struct_0_x1939_19096_x1915920110}

[\*Dec 20 13:53:00:668 2013 PE1 PCECP/7/PACKET SENT: -MDC=1; Sent a Keepalive message to peer (3.3.3.1:0). Message content: 20 02 00 04.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1569122878}*[给对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息，对端的地址为]{style="font-family:宋体"}[3.3.3.1]{lang="EN-US"}[，实例号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，消息内容为]{style="font-family:宋体"}[20 02 00 04]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_1368098004}[打开]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[的接收消息调试信息开关，收到对等体的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息时，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pcep packet received]{lang="EN-US"}]{#struct_0_x1939_19096_x867719234}

[\*Dec 20 13:11:29:438 2013 P2 PCECP/7/PACKET RECEIVED: -MDC=1; Received a Keepalive message from peer (1.1.1.1:0). Message content: 20 02 00 04.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1608191699}*[接收来自对端的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息，对端的地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，实例号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，消息内容为]{style="font-family:宋体"}[20 02 00 04]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x74067059}[打开]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[的状态机调试信息开关，配置]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[后，设备上打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pcep fsm]{lang="EN-US"}]{#struct_0_x1939_19096_x192409192}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls te]{lang="EN-US"}

[\[Sysname-te\] pce address 1.1.1.1]{lang="EN-US"}

[\*Dec 21 08:17:39:968 2013 P1 PCECP/7/FSM: -MDC=1; Session (4.4.4.1:0, active) received event (TCP connect), state: Idle.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1670837063}*[会话接收到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接事件，当前会话状态为]{style="font-family:宋体"}[Idle]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Dec 21 06:24:37:073 2013 PE1 PCECP/7/FSM: -MDC=1; Changed the session (3.3.3.1:0, passive) state from Idle to TCPPending.]{lang="EN-US"}]{#struct_0_x1939_19096_465117004}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_561647528}*[会话状态由]{style="font-family:宋体"}[Idle]{lang="EN-US"}[变为]{style="font-family:宋体"}[TCPPending]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x867719235}[打开]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[套接字调试信息开关，执行撤销本地]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址命令后，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pcep socket]{lang="EN-US"}]{#struct_0_x1939_19096_x1608126163}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls te]{lang="EN-US"}

[\[Sysname-te\] undo pce address]{lang="EN-US"}

[\*Dec 20 14:27:52:634 2013 PE1 PCECP/7/SOCKET: -MDC=1; Closed the TCP server (socket: 35) successfully.]{lang="EN-US"}

[*[//]{lang="EN-US"}[ ]{lang="EN-US"}*]{#struct_0_x1939_19096_682577865}*[成功关闭了]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[服务端，]{style="font-family:
宋体"}[socket]{lang="EN-US"}[资源为]{style="font-family:
宋体"}[35]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x1812153817}[打开]{style="font-family:宋体"}[PCEP]{lang="EN-US"}[会话调试信息开关，配置]{style="font-family:宋体"}[PCE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[后，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pcep session]{lang="EN-US"}]{#struct_0_x1939_19096_1156966441}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mpls te]{lang="EN-US"}

[\[Sysname-te\] pce address 1.1.1.1]{lang="EN-US"}

[\*Dec 21 06:24:37:073 2013 PE1 PCECP/7/SESSION: -MDC=1; Created a new session (3.3.3.1:0, passive).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1940559796}*[创建新的会话，对端地址]{style="font-family:宋体"}[3.3.3.1]{lang="EN-US"}[，实例号]{style="font-family:宋体"}[0]{lang="EN-US"}[，会话角色]{style="font-family:宋体"}[passive]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x867719228}[打开]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[请求消息调试信息开关，在]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下执行]{style="font-family:宋体"}**[mpls te path]{lang="EN-US"}**[命令后，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pce brpc pcreq]{lang="EN-US"}]{#struct_0_x1939_19096_x1607405268}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface tunnel 0 mode mpls-te]{lang="EN-US"}

[\[Sysname-Tunnel0\] destination 3.3.3.3]{lang="EN-US"}

[\[Sysname-Tunnel0\] mpls te path preference 1 dynamic pce 2.2.2.2 3.3.3.3]{lang="EN-US"}

[\*Jun 27 03:20:31:406 2014 H3C PCE/7/PCREQ: -MDC=1; PCE list: 2.2.2.2         3.3.3.3 Sent a request to peer (2.2.2.2:0): Request-ID-number: 0x2 Flags: VSPT=1, O=1, B=0, R=0, Pri=6 END-POINTS: source=1.1.1.1, destination=3.3.3.3.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_1770006018}*[给对端]{style="font-family:宋体"}[peer]{lang="EN-US"}[发送请求消息，]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[，对端]{style="font-family:宋体"}[peer]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，实例号为]{style="font-family:宋体"}[ 0]{lang="EN-US"}[，请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0x2]{lang="EN-US"}[，]{style="font-family:宋体"}[VSPT]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[O]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[B]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[R]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[6]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x1532497751}[打开]{style="font-family:宋体"}[BRPC]{lang="EN-US"}[回复消息调试信息开关，在]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下执行]{style="font-family:宋体"}**[mpls te path]{lang="EN-US"}**[命令后，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pce brpc pcrep]{lang="EN-US"}]{#struct_0_x1939_19096_455875219}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface tunnel 0 mode mpls-te]{lang="EN-US"}

[\[Sysname-Tunnel0\] destination 3.3.3.3]{lang="EN-US"}

[\[Sysname-Tunnel0\] mpls te path preference 1 dynamic pce 2.2.2.2 3.3.3.3]{lang="EN-US"}

[\*Jun 27 03:20:31:408 2014 PCE2 PCE/7/PCREP: -MDC=1; Received a reply from peer (3.3.3.3:0): Request-ID-number: 0x2 Flags: VSPT=1, O=1, B=0, R=0, Pri=6 Path: 20.1.1.1 \--\> 20.1.1.2 \--\> 2.2.2.2 \--\> 30.1.1.1 \--\> 30.1.1.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x867719229}*[给对端]{style="font-family:宋体"}[peer]{lang="EN-US"}[发送回复消息，对端]{style="font-family:宋体"}[peer]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，实例号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0x2]{lang="EN-US"}[，]{style="font-family:宋体"}[VSPT]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[O]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[B]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[R]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[6]{lang="EN-US"}[，接口地址列表为]{style="font-family:宋体"}[20.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[20.1.1.2]{lang="EN-US"}[，]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，]{style="font-family:宋体"}[30.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[30.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x1607339732}[打开]{style="font-family:宋体"}[EPC]{lang="EN-US"}[请求消息调试信息开关，在]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下执行]{style="font-family:宋体"}**[mpls te path]{lang="EN-US"}**[命令后，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pce epc pcreq]{lang="EN-US"}]{#struct_0_x1939_19096_x362799022}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface tunnel 0 mode mpls-te]{lang="EN-US"}

[\[Sysname-Tunnel0\] destination 3.3.3.3]{lang="EN-US"}

[\[Sysname-Tunnel0\] mpls te path preference 1 dynamic pce 3.3.3.3]{lang="EN-US"}

[\*Jun 27 03:13:40:741 2014 H3C PCE/7/PCREQ: -MDC=1; Sent a request to peer (3.3.3.3:0): Request-ID-number: 0x1 Flags: VSPT=0, O=1, B=0, R=1, Pri=7 END-POINTS: source=2.2.2.2, destination=3.3.3.3.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_873787692}*[给对端]{style="font-family:宋体"}[peer]{lang="EN-US"}[发送请求消息，]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[，对端]{style="font-family:宋体"}[peer]{lang="EN-US"}[地址]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[，实例号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[，]{style="font-family:宋体"}[VSPT]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[O]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[B]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[R]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[7]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_x564836745}[打开]{style="font-family:宋体"}[EPC]{lang="EN-US"}[回复消息调试信息开关，在]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下执行]{style="font-family:宋体"}**[mpls te path]{lang="EN-US"}**[命令后，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te pce epc pcrep]{lang="EN-US"}]{#struct_0_x1939_19096_x867719230}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface tunnel 0 mode mpls-te]{lang="EN-US"}

[\[Sysname-Tunnel0\] destination 3.3.3.3]{lang="EN-US"}

[\[Sysname-Tunnel0\] mpls te path preference 1 dynamic pce 3.3.3.3]{lang="EN-US"}

[\*Jun 27 03:13:40:743 2014 H3C PCE/7/PCREP: -MDC=1; Received a reply  from peer (3.3.3.3:0): Request-ID-number: 0x1 Flags: VSPT=0, O=1, B=0, R=1, Pri=7 Path: 20.1.1.1 \--\> 20.1.1.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1607929555}*[给对端]{style="font-family:宋体"}[peer]{lang="EN-US"}[发送回复消息，对端]{style="font-family:宋体"}[peer]{lang="EN-US"}[地址]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[，实例号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0x1]{lang="EN-US"}[，]{style="font-family:宋体"}[VSPT]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[O]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[B]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[R]{lang="EN-US"}[标志位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[7]{lang="EN-US"}[，接口地址列表为]{style="font-family:宋体"}[20.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[20.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-1966930903 .myid}
[]{#_Toc404790694}[]{#struct_0_x1939_19096_x1395274492}[]{#_Toc352336495}[]{#_Toc350865778}[]{#_Toc345666324}

**MPLS TE \-- MPLS TE调试命令 \-- debugging isis mpls te**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1241403954}

[**[debugging isis mpls te ]{lang="EN-US"}**[\[ **advertisement** \| **event** \| **map** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1939_19096_1480251987}

[**[undo debugging isis mpls te ]{lang="EN-US"}**[\[ **advertisement** \| **event \| map** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1939_19096_x1395340028}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1003275599}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1939_19096_528592043}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x343513754}

[[network-admin]{lang="EN-US"}]{#struct_0_x1939_19096_x1395667708}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1939_19096_x886093142}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1353855129}

[**[advertisement]{lang="EN-US"}**]{#struct_0_x1939_19096_x70040981}[：表示链路或节点]{style="font-family:宋体"}[TE]{lang="EN-US"}[信息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1939_19096_x1395733244}[：表示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[ TE]{lang="EN-US"}[的]{style="font-family:
宋体"}[事件调试信息开关。]{style="font-family:宋体"}

[**[map]{lang="EN-US"}**]{#struct_0_x1939_19096_x1327515926}[：表示隧道目的地址与隧道目的端设备]{style="font-family:宋体"}[System ID]{lang="EN-US"}[映射关系的调试信息开关。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x890496717}[：表示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的调试信息开关。]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定本参数，则表示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1939_19096_1891241818}

[**[debugging isis mpls te]{lang="EN-US"}**]{#struct_0_x1939_19096_x1395536636}[命令用来打开]{style="font-family:宋体"}[IS-IS TE]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging isis mpls te]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS TE]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IS-IS TE]{lang="EN-US"}]{#struct_0_x1939_19096_232955940}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定任何参数，则表示所有]{style="font-family:宋体"}[IS-IS TE]{lang="EN-US"}]{#struct_0_x1939_19096_x966049547}[调试信息开关。]{style="font-family:宋体"}

[[表1-23 ]{lang="EN-US"}[debugging isis mpls te advertisement]{lang="EN-US"}]{#struct_0_x1939_19096_870707231}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1850439922}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1395602172}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1030840580}

[[ISIS-*process-id*-TE]{lang="EN-US"}]{#struct_0_x1939_19096_x1394881276}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_533687168}[进程]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[TE]{lang="EN-US"}[调试信息]{style="font-family:宋体"}

[[Updated level-*Level* LSR ID *lsr-id* in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x1394946812}

[[更新]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}]{#struct_0_x1939_19096_49512246}[到]{style="font-family:宋体"}[TEDB]{lang="EN-US"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x2123546041}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[lsr-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395405565}[：]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[，点分十进制格式]{style="font-family:宋体"}

[[Deleted level-*Level* LSR ID *lsr-id* from TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x502072111}

[[删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1395471101}[中的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[信息]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x1252306950}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[lsr-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395274493}[：]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[，点分十进制格式]{style="font-family:宋体"}

[[Updated TE node overload state (*state*)]{lang="EN-US"}]{#struct_0_x1939_19096_324679987}[[.]{lang="EN-US" style="font-size:10.5pt"}]{.MsoCommentReference}[ level-*Level*, system ID: *system-id.*]{lang="EN-US"}

[[更新]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1395340029}[中节点的]{style="font-family:宋体"}[Overload]{lang="EN-US"}[状态]{style="font-family:宋体"}

[*[state]{lang="EN-US"}*]{#struct_0_x1939_19096_1725607756}[：节点的]{style="font-family:宋体"}[Overload]{lang="EN-US"}[状态，取值为]{style="font-family:宋体"}[TRUE]{lang="EN-US"}[或者]{style="font-family:宋体"}[FALSE]{lang="EN-US"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_228114175}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[system-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395667709}[：节点的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[Updated TE link. level-*Level*, type: *type*, neighbor ID: *nbr-id*, local address count: *count_l*, remote address count: *count_r*.]{lang="EN-US"}]{#struct_0_x1939_19096_1842790213}

[[更新]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1395733245}[中的]{style="font-family:宋体"}[TE Link]{lang="EN-US"}[信息]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_238568015}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[nbr-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395536637}[：扩展]{style="font-family:宋体"}[IS]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ID ]{lang="EN-US"}

[*[type]{lang="EN-US"}*]{#struct_0_x1939_19096_1799039881}[：链路类型]{style="font-family:宋体"}

[*[count_l]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395602173}[：本地接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[址个数]{style="font-family:宋体"}

[*[count_r]{lang="EN-US"}*]{#struct_0_x1939_19096_1698042775}[：邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[址个数]{style="font-family:宋体"}

[[Deleted TE link. level-*Level*, type: *type*, neighbor ID: *nbr-id*, local address count: *count_l*, remote address count: *count_r*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1394881277}

[[从]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1032396773}[中删除]{style="font-family:宋体"}[TE Link]{lang="EN-US"}[信息]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x1394946813}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[nbr-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1516571695}[：扩展]{style="font-family:宋体"}[IS]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[count_l]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395405566}[：本地接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[址个数]{style="font-family:宋体"}

[*[count_r]{lang="EN-US"}*]{#struct_0_x1939_19096_x2068156052}[：邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[址个数]{style="font-family:宋体"}

[[Updated TE network. level-*Level*, source ID: *source-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1395471102}

[[更新]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1655591477}[中的网络信息]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_828559431}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[source-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395274494}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成路由器的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[Deleted TE network. level-*Level*, source ID: *source-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x434834900}

[[从]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1395340030}[中删除网络信息]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x1359571495}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[source-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395667710}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成路由器的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[Deleted all information in Level-*Level* TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x1242257966}

[[删除指定]{style="font-family:宋体"}[Level]{lang="EN-US"}]{#struct_0_x1939_19096_x1395733246}[的]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[中的信息]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x164716512}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-24 ]{lang="EN-US"}[debugging isis mpls te event]{lang="EN-US"}]{#struct_0_x1939_19096_x1395536638}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1845472338}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_683294634}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1502867701}

[[ISIS-*process-id*-TE]{lang="EN-US"}]{#struct_0_x1939_19096_x1395602174}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_131958834}[进程]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[TE]{lang="EN-US"}[调试信息]{style="font-family:宋体"}

[[Received a TE enable state change event.]{lang="EN-US"}]{#struct_0_x1939_19096_x1394881278}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_1696486582}[接收到]{style="font-family:宋体"}[TE]{lang="EN-US"}[使能状态变化事件]{style="font-family:宋体"}

[[Received an interface TE information change event.]{lang="EN-US"}]{#struct_0_x1939_19096_x659406490}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_x1394946814}[接收到接口]{style="font-family:宋体"}[TE]{lang="EN-US"}[信息变化事件]{style="font-family:宋体"}

[[Received a TE tunnel interface information update event.]{lang="EN-US"}]{#struct_0_x1939_19096_856081300}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_x1395405567}[接收到]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道接口信息更新事件]{style="font-family:宋体"}

[[Received a TE tunnel interface information delete event.]{lang="EN-US"}]{#struct_0_x1939_19096_660727303}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_x2103209592}[接收到]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道接口信息删除事件]{style="font-family:宋体"}

[[Received an MPLS LSR ID change event.]{lang="EN-US"}]{#struct_0_x1939_19096_x1395471103}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_x89507536}[接收到]{style="font-family:宋体"}[TE]{lang="EN-US"}[上报的]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[变化事件]{style="font-family:宋体"}

[[Received a level-*Level* tunnel destination address update event.]{lang="EN-US"}]{#struct_0_x1939_19096_x1395274495}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_1131249041}[接收到]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道目的地址更新事件]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x1330821730}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-25 ]{lang="EN-US"}[debugging isis mpls te map]{lang="EN-US"}]{#struct_0_x1939_19096_x1395340031}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1827371666}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1369311860}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_397396104}

[[ISIS-*process-id*-TE]{lang="EN-US"}]{#struct_0_x1939_19096_x1395667711}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_1486625389}[进程]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[TE]{lang="EN-US"}[调试信息]{style="font-family:宋体"}

[[Notified TEDB to add a mapping for the destination *ip-address* of tunnel *tunnel-name* in level-*Level*.]{lang="EN-US"}]{#struct_0_x1939_19096_1708310079}

[[通知]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1395733247}[为某个]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[的目的地址生成映射]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_1401367429}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[tunnel-name]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395536639}[：隧道接口名]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x2045588721}[：隧道接口的目的地址]{style="font-family:宋体"}

[[Notified TEDB to delete the mapping for the destination *ip-address* of tunnel *tunnel-name* in level-*Level*.]{lang="EN-US"}]{#struct_0_x1939_19096_1676765620}

[[通知]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1395602175}[删除某个]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[的目的地址的映射]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x1434125107}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[tunnel-name]{lang="EN-US"}*]{#struct_0_x1939_19096_x1394881279}[：隧道接口名]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1939_19096_130402641}[：隧道接口的目的地址]{style="font-family:宋体"}

[[(MT*topoId*) (L*Level*) Added a mapping in IS-IS. TE tunnel: *tunnel-name*, destination address: *ip-address*, SPF node: *system-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_1557597471}

[[在]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_x1394946815}[模块添加一条映射信息，这条映射信息是将隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*[的目的地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[映射到]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点]{style="font-family:宋体"}*[system-id]{lang="EN-US"}[。]{style="font-family:宋体"}*

[*[topoId]{lang="EN-US"}*]{#struct_0_x1939_19096_x710002641}[：拓扑号]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395405568}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[tunnel-name]{lang="EN-US"}*]{#struct_0_x1939_19096_x1617817358}[：隧道接口名]{style="font-family:宋体"}

[*[ip-address: ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395471104}[隧道接口目的地址]{style="font-family:宋体"}

[*[system-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x849022423}[：]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[(MT*topoId*) (L*Level*) Updated the mapping in IS-IS. TE tunnel: *tunnel-name*, destination address: *ip-address*, SPF node: *system-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1395274496}

[[在]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_727964514}[模块更新一条映射信息，这条映射信息是将隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*[的目的地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[映射到]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[topoId]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395340032}[：拓扑号]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_x196772081}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[tunnel-name]{lang="EN-US"}*]{#struct_0_x1939_19096_x1562231526}[：隧道接口名]{style="font-family:宋体"}

[*[ip-address: ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395667712}[隧道接口目的地址]{style="font-family:宋体"}

[*[system-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1889909916}[：]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[(MT*topoId*) (L*Level*) Deleted the mapping in IS-IS. TE tunnel: *tunnel-name*, destination address: *ip-address*, SPF node: *system-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1395733248}

[[在]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1939_19096_285622182}[模块删除一条映射信息，这条映射信息是将隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*[的目的地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[映射到]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[topoId]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395536640}[：拓扑号]{style="font-family:宋体"}

[*[Level]{lang="EN-US"}*]{#struct_0_x1939_19096_1039197314}[：系统级别，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[2]{lang="EN-US"}

[*[tunnel-name]{lang="EN-US"}*]{#struct_0_x1939_19096_1088993068}[：隧道接口名]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1395602176}[：隧道接口目的地址]{style="font-family:宋体"}

[*[system-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1294758248}[：]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1394881280}

[[\# ]{lang="EN-US"}]{#struct_0_x1939_19096_1340583902}[设备上打开所有]{style="font-family:宋体"}[IS-IS TE]{lang="EN-US"}[调试信息开关。在设备上全局、接口使能]{style="font-family:宋体"}[IS-IS TE]{lang="EN-US"}[和关闭]{style="font-family:宋体"}[IS-IS TE]{lang="EN-US"}[功能时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging isis mpls te 1]{lang="EN-US"}]{#struct_0_x1939_19096_x1394946816}

[%May 7 11:01:22:257 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Received an MPLS LSR ID change event.]{lang="EN-US"}

[%May 7 11:01:22:260 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Updated level-1 LSR ID 7.0.0.2 in TEDB.]{lang="EN-US"}

[%May 7 11:01:22:269 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Updated level-2 LSR ID 7.0.0.1 in TEDB.]{lang="EN-US"}

*[// ]{lang="EN-US"}[全局使能]{style="font-family:
宋体"}[IS-IS TE]{lang="EN-US"}[，更新]{style="font-family:
宋体"}[TEDB]{lang="EN-US"}[信息]{style="font-family:宋体"}*[。]{style="font-family:宋体"}

[%May 7 11:01:22:278 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Received an interface TE information change event.]{lang="EN-US"}

[%May 7 11:01:22:286 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Updated TE link. level-1, type: Broadcast, neighbor ID: 0000.0000.0001.01, local address count: 1, remote address count: 0.]{lang="EN-US"}

[%May 7 11:01:22:299 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Updated TE link. level-2, type: Broadcast, neighbor ID: 0000.0000.0001.01, local address count: 1, remote address count: 0.]{lang="EN-US"}

*[//]{lang="EN-US"}[ ]{lang="EN-US"}[接口使能]{style="font-family:宋体"}[IS-IS ]{lang="EN-US"}[TE]{lang="EN-US"}[，增加]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[信息]{style="font-family:宋体"}*[。]{style="font-family:宋体"}

[%May 7 11:01:22:310 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Received an interface TE information change event.]{lang="EN-US"}

[%May 7 11:01:22:326 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Deleted TE link. level-1, type: Broadcast, neighbor ID: 0000.0000.0001.01, local address count: 1, remote address count: 0.]{lang="EN-US"}

[%May 7 11:01:22:345 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Deleted TE link. level-2, type: Broadcast, neighbor ID: 0000.0000.0001.01, local address count: 1, remote address count: 0.]{lang="EN-US"}

*[//]{lang="EN-US"}[ ]{lang="EN-US"}[接口关闭]{style="font-family:宋体"}[IS-IS ]{lang="EN-US"}[TE]{lang="EN-US"}[功能]{style="font-family:宋体"}[，删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[信息]{style="font-family:宋体"}*[。]{style="font-family:宋体"}

[%May 7 11:01:22:390 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Received a TE enable state change event.]{lang="EN-US"}

[%May 7 11:01:22:410 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Deleted all information in Level-1 TEDB.]{lang="EN-US"}

[%May 7 11:01:22:540 2013 Sysname SCMD/6/JOBINFO: -MDC=1; ISIS-1-TE: Deleted all information in Level-2 TEDB.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_2018880714}*[全局关闭]{style="font-family:宋体"}[IS-IS TE]{lang="EN-US"}[功能，删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

::: {#621926332 .myid}
[]{#_Toc404790695}[]{#struct_0_x1939_19096_x927670383}

**MPLS TE \-- MPLS TE调试命令 \-- debugging ospf mpls te**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1676148318}

[**[debugging]{lang="EN-US"}**[ **ospf** \[ *process-id* \] **mpls te** \[ **advertisement** \| **event** \| **pce** \]]{lang="EN-US"}]{#struct_0_x1939_19096_x295780749}

[**[undo debugging ospf ]{lang="EN-US"}**[\[ *process-id* \] **mpls te** \[ **advertisement** \| **event** \| **pce** \]]{lang="EN-US"}]{#struct_0_x1939_19096_x1013897660}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1939_19096_1685327051}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1793862296}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1939_19096_930522665}

[[network-admin]{lang="EN-US"}]{#struct_0_x1939_19096_x1571018003}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1939_19096_x2033691542}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1939_19096_581182356}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x663251738}[：表示指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的调试信息开关。]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定本参数，则表示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的调试信息开关。]{style="font-family:宋体"}

[**[advertisement]{lang="EN-US"}**]{#struct_0_x1939_19096_9803067}[：表示]{style="font-family:宋体"}[OSPF TE]{lang="EN-US"}[通告调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1939_19096_x1520864538}[：表示]{style="font-family:宋体"}[OSPF TE]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[pce]{lang="EN-US"}**]{#struct_0_x1939_19096_x1140373700}[：表示]{style="font-family:宋体"}[OSPF PCE]{lang="EN-US"}[通告调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1939_19096_214710439}

[**[debugging ospf mpls te]{lang="EN-US"}**]{#struct_0_x1939_19096_x487299953}[命令用来打开]{style="font-family:宋体"}[OSPF TE]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf mpls te]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[OSPF TE]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPF TE]{lang="EN-US"}]{#struct_0_x1939_19096_559879174}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-26 ]{lang="EN-US"}[debugging ospf mpls te advertisement]{lang="EN-US"}]{#struct_0_x1939_19096_x1635920968}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1912416416}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_1421030845}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1865141276}

[[Notify CSPF to update one link of node *node-id*. Result: *result*, link type: *link-type*, link ID: *link-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_x2033757078}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_1683310593}[更新节点]{style="font-family:宋体"}*[node-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[Link]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1056274315}[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[中为]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[；]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[中为]{style="font-family:宋体"}[systemID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_x1939_19096_1377391334}[：更新结果，取值为]{style="font-family:宋体"}[success]{lang="EN-US"}[或者]{style="font-family:宋体"}[fail]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[link-type]{lang="EN-US"}*]{#struct_0_x1939_19096_x30359406}[：链路类型，]{style="font-family:宋体"}[1]{lang="EN-US"}[为]{style="font-family:宋体"}[P2P]{lang="EN-US"}[，]{style="font-family:宋体"}[2]{lang="EN-US"}[为广播网，]{style="font-family:宋体"}[3]{lang="EN-US"}[为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[，]{style="font-family:宋体"}[4]{lang="EN-US"}[为]{style="font-family:宋体"}[P2MP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[link-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1838169167}[：链路]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Notify CSPF to delete one link of node *node-id*. Result: *result*, link type: *link-type*, link ID: *link-id*.]{lang="EN-US"}]{#struct_0_x1939_19096_1627389303}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_671960437}[删除节点]{style="font-family:宋体"}*[node-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[Link]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Notify CSPF to delete the LSR ID of node *node-id*. Result: *result*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1622886174}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x2033560470}[删除节点]{style="font-family:宋体"}*[node-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}

[[Notify CSPF to update the LSR ID of node *node-id*. Result: *result*, new LSR ID: ]{lang="EN-US"}]{#struct_0_x1939_19096_x258036180}*[lsr-id]{lang="EN-US"}*[.]{lang="EN-US"}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_305083899}[更新节点]{style="font-family:宋体"}*[node-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}

[[Notify CSPF to update the network information of node *node-id*. Result: *result*, attatched router number: *number*.]{lang="EN-US"}]{#struct_0_x1939_19096_1354088438}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_1481034218}[更新节点]{style="font-family:宋体"}*[node-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[network]{lang="EN-US"}[信息，其中，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[表示相连路由器的个数]{style="font-family:宋体"}

[[Notify CSPF to delete the network information of node *node-id*. Result: *result*, attatched router number: *number*.]{lang="EN-US"}]{#struct_0_x1939_19096_914442717}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_796006896}[删除节点]{style="font-family:宋体"}*[node-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[network]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Notify CSPF of the smooth event *event*. Result: *result*.]{lang="EN-US"}]{#struct_0_x1939_19096_x2033626006}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_1208317810}[平滑事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_x1939_19096_1837269471}[：表示平滑开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_x1939_19096_x589281893}[：表示平滑结束]{style="font-family:宋体"}

[[Notify CSPF of the process GR event *event*. Result: *result*, process: ]{lang="EN-US"}]{#struct_0_x1939_19096_x656426789}*[process-id]{lang="EN-US"}*[.]{lang="EN-US"}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x2033429398}[进程]{style="font-family:宋体"}[GR]{lang="EN-US"}[事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x1939_19096_1870672663}[：表示]{style="font-family:宋体"}[GR]{lang="EN-US"}[开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x1939_19096_418192885}[：表示]{style="font-family:宋体"}[GR]{lang="EN-US"}[结束]{style="font-family:宋体"}

[[Notify CSPF of the area delete event. Result: *result*, process: ]{lang="EN-US"}]{#struct_0_x1939_19096_698596425}*[process-id]{lang="EN-US"}*[, area: *area-id*.]{lang="EN-US"}

[[通知]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x1939_19096_2025794819}[进程]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[的区域]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[删除]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-27 ]{lang="EN-US"}[debugging ospf mpls te event]{lang="EN-US"}]{#struct_0_x1939_19096_913069267}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1904584558}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_259595184}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x117844413}

[[OSPF *process-id* area *area-id*]{lang="EN-US"}]{#struct_0_x1939_19096_x2033494934}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}*[process-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1255064990}[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area-id]{lang="EN-US"}*]{#struct_0_x1939_19096_1963463128}[：区域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[MPLS TE is enabled. ]{lang="EN-US"}]{#struct_0_x1939_19096_1494266139}

[[OSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x1521925598}[区域使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[MPLS TE is disabled.]{lang="EN-US"}]{#struct_0_x1939_19096_x1202122938}

[[OSPF]{lang="EN-US"}]{#struct_0_x1939_19096_x1484843076}[区域去使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[Updated the router TLV in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_981316317}

[[更新]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x2033298326}[中的]{style="font-family:宋体"}[Router TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Deleted the router TLV in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x798404314}

[[删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x232130415}[中的]{style="font-family:宋体"}[Router TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Updated the link TLV in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x161357295}

[[更新]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_1471107369}[中的]{style="font-family:宋体"}[Link TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Deleted the link TLV in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x786269199}

[[删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1724247037}[中的]{style="font-family:宋体"}[Link TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Deleted all information in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x2033363862}

[[删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1005992710}[中的所有信息]{style="font-family:宋体"}

[[Link TLV invalid.]{lang="EN-US"}]{#struct_0_x1939_19096_1442450698}

[[因]{style="font-family:宋体"}[Link TLV]{lang="EN-US"}]{#struct_0_x1939_19096_x1504033959}[信息错误没有更新]{style="font-family:宋体"}[TEDB]{lang="EN-US"}

[[Advertising router]{lang="EN-US"}]{#struct_0_x1939_19096_x718601299}

[[发布者的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x1939_19096_x1588699572}

[[Opaque ID]{lang="EN-US"}]{#struct_0_x1939_19096_x2033167254}

[[Opaque ID]{lang="EN-US"}]{#struct_0_x1939_19096_1586748350}

[[LSR ID]{lang="EN-US"}]{#struct_0_x1939_19096_395301427}

[[发布信息的路由器的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}]{#struct_0_x1939_19096_x1175631332}

[[Link type]{lang="EN-US"}]{#struct_0_x1939_19096_x752217170}

[[链路类型，取值包括：]{style="font-family:宋体"}]{#struct_0_x1939_19096_233619876}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1939_19096_x2033232790}[：表示]{style="font-family:宋体"}[P2P]{lang="EN-US"}[链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1939_19096_x997147394}[：表示广播链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x1939_19096_891853366}[：表示]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x1939_19096_1707196566}[：表示]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[链路]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x1939_19096_x1525543674}

[[链路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1939_19096_x2033691543}

[[Local interface address number]{lang="EN-US"}]{#struct_0_x1939_19096_x984901585}

[[本地接口地址个数]{style="font-family:宋体"}]{#struct_0_x1939_19096_72595954}

[[Remote interface address number]{lang="EN-US"}]{#struct_0_x1939_19096_447860100}

[[远端接口地址个数]{style="font-family:宋体"}]{#struct_0_x1939_19096_x2033757079}

[[Updated the network information in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_117226652}

[[更新]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_729477353}[的]{style="font-family:宋体"}[Network]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Deleted the network information in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x1383079792}

[[删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}]{#struct_0_x1939_19096_1206234511}[的]{style="font-family:宋体"}[Network]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[DR address]{lang="EN-US"}]{#struct_0_x1939_19096_x2033560471}

[[广播网]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x1939_19096_1308047761}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Updated the TE information of the interface.]{lang="EN-US"}]{#struct_0_x1939_19096_1300529601}

[[更新接口的]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_x1939_19096_1035877562}[信息]{style="font-family:宋体"}

[[Deleted the TE information of the interface.]{lang="EN-US"}]{#struct_0_x1939_19096_x2033626007}

[[删除接口的]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_x1939_19096_x1520565545}[信息]{style="font-family:宋体"}

[[Updated the tunnel interface information.]{lang="EN-US"}]{#struct_0_x1939_19096_129971710}

[[更新]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x1939_19096_1449708775}[接口信息]{style="font-family:宋体"}

[[Deleted the tunnel interface information.]{lang="EN-US"}]{#struct_0_x1939_19096_x2033429399}

[[删除]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x1939_19096_x858210692}[接口信息]{style="font-family:宋体"}

[[Interface index: *index*.]{lang="EN-US"}]{#struct_0_x1939_19096_950202846}

[[接口索引]{style="font-family:宋体"}]{#struct_0_x1939_19096_x2033494935}

[[TE metric]{lang="EN-US"}]{#struct_0_x1939_19096_1473818365}

[[接口的]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_x1939_19096_1893895981}[度量值]{style="font-family:宋体"}

[[Administrative Group]{lang="EN-US"}]{#struct_0_x1939_19096_612414846}

[[接口的管理组属性]{style="font-family:宋体"}]{#struct_0_x1939_19096_x2033298327}

[[Bandwidth constrain model]{lang="EN-US"}]{#struct_0_x1939_19096_1930479041}

[[接口使用的带宽约束模型]{style="font-family:宋体"}]{#struct_0_x1939_19096_x1611053872}

[[Maximum bandwidth]{lang="EN-US"}]{#struct_0_x1939_19096_x710709593}

[[链路的最大带宽]{style="font-family:宋体"}]{#struct_0_x1939_19096_x2033363863}

[[maximum reservable bandwidth]{lang="EN-US"}]{#struct_0_x1939_19096_560091231}

[[链路的最大可预留带宽]{style="font-family:宋体"}]{#struct_0_x1939_19096_x181131097}

[[Destination]{lang="EN-US"}]{#struct_0_x1939_19096_x2033167255}

[[Tunnel]{lang="EN-US"}]{#struct_0_x1939_19096_x1142135005}[接口的目的地址]{style="font-family:宋体"}

[[Tunnel metric]{lang="EN-US"}]{#struct_0_x1939_19096_x1907027156}

[[Tunnel]{lang="EN-US"}]{#struct_0_x1939_19096_x2033232791}[接口的]{style="font-family:宋体"}[metric]{lang="EN-US"}

[[Route flag]{lang="EN-US"}]{#struct_0_x1939_19096_1731735961}

[[路由标记]{style="font-family:宋体"}]{#struct_0_x1939_19096_278908332}

[ ]{lang="EN-US"}

[[表1-28 ]{lang="EN-US"}[debugging ospf mpls te pce]{lang="EN-US"}]{#struct_0_x1939_19096_x1140242633}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x7151985}[[字段]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1140177097}

[[描述]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1140373705}

[[OSPF instance *vrfIndex*, process *process-id*:]{lang="EN-US"}]{#struct_0_x1939_19096_x1140308169}

[*[vrfIndex]{lang="EN-US"}*]{#struct_0_x1939_19096_53067708}[：]{style="font-family:宋体"}[ VRF]{lang="EN-US"}[实例索引]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1140504777}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{style="font-family:宋体"}

[[Updated PCED TLV information in area(*area-id*) PCEDB. LSA type=*type*, router ID=*router-id*, PCE address=*pce-address*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1139587273}

[[更新]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x1939_19096_x1139521737}[中的]{style="font-family:宋体"}[PCED TLV]{lang="EN-US"}[信息到]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}

[*[area-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1140111562}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[type]{lang="EN-US"}*]{#struct_0_x1939_19096_x87314880}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[所属]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Opq-AS]{lang="EN-US"}]{#struct_0_x1939_19096_x1140046026}[：表示]{lang="EN-US" style="font-family:宋体"}[Opaque-AS]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Opq-Area]{lang="EN-US"}]{#struct_0_x1939_19096_x1140242634}[：表示]{lang="EN-US" style="font-family:宋体"}[Opaque-Area]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}

[*[router-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1140177098}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[所属]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的生成路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[pce-address]{lang="EN-US"}*]{#struct_0_x1939_19096_x1140373706}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中携带的]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址值]{style="font-family:宋体"}

[[Deleted PCED TLV information in area(*area-id*) PCEDB. LSA type=*type*, router ID=*router-id*, PCE address=*pce-address*.]{lang="EN-US"}]{#struct_0_x1939_19096_x1140504778}

[[删除]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}]{#struct_0_x1939_19096_x1140439242}[中的]{style="font-family:宋体"}[PCED TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[*[area-id]{lang="EN-US"}*]{#struct_0_x1939_19096_x1062417435}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[type]{lang="EN-US"}*]{#struct_0_x1939_19096_x1139587274}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[所属]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Opq-AS]{lang="EN-US"}]{#struct_0_x1939_19096_x1139521738}[：表示]{lang="EN-US" style="font-family:宋体"}[Opaque-AS]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Opq-Area]{lang="EN-US"}]{#struct_0_x1939_19096_425972384}[：表示]{lang="EN-US" style="font-family:宋体"}[Opaque-Area]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}

[*[router-id]{lang="EN-US"}*]{#struct_0_x1939_19096_426037920}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[所属]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的生成路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[*[pce-address]{lang="EN-US"}*]{#struct_0_x1939_19096_425841312}[：]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中携带的]{style="font-family:宋体"}[PCE]{lang="EN-US"}[地址值]{style="font-family:宋体"}

[[Parsed all the PCE information when global PCEP was enabled.]{lang="EN-US"}]{#struct_0_x1939_19096_425906848}

[[全局]{style="font-family:宋体"}[PCEP]{lang="EN-US"}]{#struct_0_x1939_19096_1820636398}[使能时解析所有]{style="font-family:宋体"}[PCE]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Deleted all the PCE information when global PCEP was disabled.]{lang="EN-US"}]{#struct_0_x1939_19096_425710240}

[[全局]{style="font-family:宋体"}[PCEP]{lang="EN-US"}]{#struct_0_x1939_19096_425775776}[去使能时删除所有]{style="font-family:宋体"}[PCE]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Created the PCEDB in process.]{lang="EN-US"}]{#struct_0_x1939_19096_425579168}

[[创建进程下的]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}]{#struct_0_x1939_19096_425644704}

[[Deleted the PCEDB in process.]{lang="EN-US"}]{#struct_0_x1939_19096_426496672}

[[删除进程下的]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}]{#struct_0_x1939_19096_426562208}

[[Cleared the PCEDB in process.]{lang="EN-US"}]{#struct_0_x1939_19096_948381885}

[[清空进程下]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}]{#struct_0_x1939_19096_425972383}[中的数据]{style="font-family:宋体"}

[[Created the PCEDB in area(*area-id*).]{lang="EN-US"}]{#struct_0_x1939_19096_426037919}

[[创建区域下的]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}]{#struct_0_x1939_19096_425841311}

[*[area-id]{lang="EN-US"}*]{#struct_0_x1939_19096_425906847}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Deleted the PCEDB in area(*area-id*).]{lang="EN-US"}]{#struct_0_x1939_19096_425710239}

[[删除区域下的]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}]{#struct_0_x1939_19096_425775775}

[*[area-id]{lang="EN-US"}*]{#struct_0_x1939_19096_515825721}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Cleared the PCEDB in area(*area-id*).]{lang="EN-US"}]{#struct_0_x1939_19096_425579167}

[[清空区域下]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}]{#struct_0_x1939_19096_425644703}[中的数据]{style="font-family:宋体"}

[*[area-id]{lang="EN-US"}*]{#struct_0_x1939_19096_426496671}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Updated the PCE information when the TE area was enabled.]{lang="EN-US"}]{#struct_0_x1939_19096_426562207}

[[区域使能]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_x1939_19096_425972386}[时更新]{style="font-family:宋体"}[PCE]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Updated the PCE information when the TE area was disabled.]{lang="EN-US"}]{#struct_0_x1939_19096_426037922}

[[区域去使能]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_x1939_19096_449842795}[时更新]{style="font-family:宋体"}[PCE]{lang="EN-US"}[信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1939_19096_x1114835373}

[[\# Router A]{lang="EN-US"}]{#struct_0_x1939_19096_x163489747}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[197.168.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[197.168.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，]{style="font-family:宋体"}[Router A]{lang="EN-US"}[为]{style="font-family:宋体"}[DR]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上配置]{style="font-family:宋体"}[OSPF TE]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[OSPF TE]{lang="EN-US"}[的调试信息开关后，打印如下信息。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf 1 mpls te]{lang="EN-US"}]{#struct_0_x1939_19096_x111377237}

[OSPF process 1 area 0.0.0.1 : MPLS TE is enabled.]{lang="EN-US"}

[OSPF process 1 area 0.0.0.1 : Updated the router TLV in TEDB.]{lang="EN-US"}

[Advertising router: 7.7.7.12. Opaque ID: 0.]{lang="EN-US"}

[LSR ID: 12.1.1.2.]{lang="EN-US"}

[Notify CSPF to update the LSR ID of node 7.7.7.12. Result: success, new LSR ID: 12.1.1.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_137840346}*[区域使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，更新]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

[[OSPF process 1 : Updated the TE information of the interface.]{lang="EN-US"}]{#struct_0_x1939_19096_x1373460196}

[Interface index: 7.]{lang="EN-US"}

[TE metric: 0. Administrative group: 0. Bandwidth constrain model: 0.]{lang="EN-US"}

[Maximum bandwidth: 10000000. Maximum reservable bandwidth: 0.]{lang="EN-US"}

[OSPF process 1 area 0.0.0.0 : Updated the link TLV in TEDB.]{lang="EN-US"}

[Advertising router: 7.7.7.12. Opaque ID: 1.]{lang="EN-US"}

[Link type: 1. Link ID: 2.2.2.2.]{lang="EN-US"}

[Local interface address number = 3. Remote interface address number = 1.]{lang="EN-US"}

[Notify CSPF to update one link of node 7.7.7.12. Result: success, link type: 1, link ID:7.7.7.12.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x669098361}*[接口使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，增加]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

[[OSPF process 1 : Deleted the TE information of the interface.]{lang="EN-US"}]{#struct_0_x1939_19096_x1964934267}

[Interface index: 7.]{lang="EN-US"}

[OSPF process 1 area 0.0.0.0 : Delete the link TLV in TEDB.]{lang="EN-US"}

[Advertising router: 7.7.7.12. Opaque ID: 1.]{lang="EN-US"}

[Link type: 1. Link ID: 2.2.2.2.]{lang="EN-US"}

[Local interface address number = 3. Remote interface address number = 1.]{lang="EN-US"}

[Notify CSPF to delete one link of node 7.7.7.12. Result: success, link type: 1,]{lang="EN-US"}

[link ID:7.7.7.12.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_120055591}*[接口和全局去使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[信息]{style="font-family:宋体"}*

[[OSPF process 1 area 0.0.0.1 : Deleted all information in TEDB.]{lang="EN-US"}]{#struct_0_x1939_19096_x111442773}

[OSPF process 1 area 0.0.0.1 : MPLS TE is disabled.]{lang="EN-US"}

[Notify CSPF of the area delete event. Result: success, process: 1, area: 0.0.0.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_1735190892}*[区域去使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，删除]{style="font-family:宋体"}[TEDB]{lang="EN-US"}[信息]{style="font-family:宋体"}*

[[OSPF instance 0, process 1: Created the PCEDB in process.]{lang="EN-US"}]{#struct_0_x1939_19096_425906850}

[OSPF instance 0, process 1: Created the PCEDB in area(0.0.0.0).]{lang="EN-US"}

[OSPF instance 0, process 1: Parsed all the PCE information when global PCEP was enabled.]{lang="EN-US"}

[OSPF instance 0, process 1: Updated PCED TLV information in area(0.0.0.0) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_425710242}*[进程下第一个区域使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，解析所有]{style="font-family:宋体"}[PCE]{lang="EN-US"}[信息并更新]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}*

[[OSPF instance 0, process 1: Updated the PCE information when the TE area was enabled.]{lang="EN-US"}]{#struct_0_x1939_19096_x292149639}

[OSPF instance 0, process 1: Created the PCEDB in area(0.0.0.1).]{lang="EN-US"}

[OSPF instance 0, process 1: Updated PCED TLV information in area(0.0.0.0) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.]{lang="EN-US"}

[OSPF instance 0, process 1: Updated PCED TLV information in area(0.0.0.1) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_425775778}*[区域使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，更新]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

[[OSPF instance 0, process 1: Updated the PCE information when the TE area was disabled.]{lang="EN-US"}]{#struct_0_x1939_19096_515825710}

[OSPF instance 0, process 1: Deleted PCED TLV information in area(0.0.0.1) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.]{lang="EN-US"}

[OSPF instance 0, process 1: Cleared the PCEDB in area(0.0.0.1).]{lang="EN-US"}

[OSPF instance 0, process 1: Deleted the PCEDB in area(0.0.0.1).]{lang="EN-US"}

[OSPF instance 0, process 1: Updated PCED TLV information in area(0.0.0.0) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_425579170}*[区域去使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，删除区域下]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}[信息，并更新其他区域]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

[[OSPF instance 0, process 1: Deleted PCED TLV information in area(0.0.0.0) PCEDB. LSA type=Opq-Area, router ID=7.7.7.12, PCE address=1.2.3.4.]{lang="EN-US"}]{#struct_0_x1939_19096_1726847960}

[*[// MPLS]{lang="EN-US"}*]{#struct_0_x1939_19096_425644706}*[撤销发布]{style="font-family:宋体"}[PCE]{lang="EN-US"}[信息，删除]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}[信息]{style="font-family:宋体"}*

[[OSPF instance 0, process 1: Cleared the PCEDB in area(0.0.0.0).]{lang="EN-US"}]{#struct_0_x1939_19096_x1079648169}

[OSPF instance 0, process 1: Cleared the PCEDB in process.]{lang="EN-US"}

[OSPF instance 0, process 1: Deleted all the PCE information when global PCEP was disabled.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_426496674}*[全局去使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，清空所有]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}[信息]{style="font-family:宋体"}[OSPF instance 0, process 1: Cleared the PCEDB in area(0.0.0.0).]{lang="EN-US"}*

[[OSPF instance 0, process 1: Deleted the PCEDB in area(0.0.0.0).]{lang="EN-US"}]{#struct_0_x1939_19096_426562210}

[OSPF instance 0, process 1: Cleared the PCEDB in process.]{lang="EN-US"}

[OSPF instance 0, process 1: Deleted the PCEDB in process.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1939_19096_x1390270267}*[进程下最后一个区域去使能]{style="font-family:宋体"}[TE]{lang="EN-US"}[，删除所有]{style="font-family:宋体"}[PCEDB]{lang="EN-US"}[信息]{style="font-family:宋体"}*
