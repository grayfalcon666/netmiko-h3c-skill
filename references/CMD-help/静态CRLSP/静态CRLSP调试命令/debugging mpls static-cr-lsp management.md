::: {#2073097635 .myid}
[]{#_Toc404790901}[]{#struct_0_x1137_20281_669177221}[]{#_Toc385236920}[]{#_Toc383519225}

**静态CRLSP \-- 静态CRLSP调试命令 \-- debugging mpls static-cr-lsp management**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1137_20281_x1394913045}

[**[debugging mpls static-cr-lsp ]{lang="EN-US"}**[\[ **all \| error \| event \| process** \] ]{lang="EN-US"}]{#struct_0_x1137_20281_152210850}

[**[undo debugging mpls static-cr-lsp]{lang="EN-US"}**[ \[ **all \| error \| event \| process** \]]{lang="EN-US"}]{#struct_0_x1137_20281_871815320}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1137_20281_1528938747}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1137_20281_1623775124}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1137_20281_x2128882261}

[[network-admin]{lang="EN-US"}]{#struct_0_x1137_20281_1884463714}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1137_20281_x1274215854}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1137_20281_x418110701}

[**[all]{lang="EN-US"}**]{#struct_0_x1137_20281_x1230843366}[：表示静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[所有的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1137_20281_1353414064}[：表示]{style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的]{style="font-family:宋体"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1137_20281_x1439084001}[：表示]{style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的]{style="font-family:宋体"}[事件调试信息开关。]{style="font-family:宋体"}

[**[process]{lang="EN-US"}**]{#struct_0_x1137_20281_x1604304447}[：表示]{style="font-family:宋体"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的创建、处理调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1137_20281_701316948}

[**[debugging mpls ]{lang="EN-US"}[static-cr-lsp]{lang="EN-US"}**]{#struct_0_x1137_20281_1884398178}[命令用来打开静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging mpls ]{lang="EN-US"}[static-cr-lsp]{lang="EN-US"}**[命令用来关闭静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}]{#struct_0_x1137_20281_750375612}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mpls static-cr-lsp error]{lang="EN-US"}]{#struct_0_x1137_20281_x1161432362}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2024007778}[[字段]{style="font-family:黑体"}]{#struct_0_x1137_20281_x1261235382}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1137_20281_x1335527717}

[[Failed to reply configuration.]{lang="EN-US"}]{#struct_0_x1137_20281_1884594786}

[[配置处理消息回复失败]{style="font-family:宋体"}]{#struct_0_x1137_20281_x480032445}

[[Not enough resources are available to complete the operation.]{lang="EN-US"}]{#struct_0_x1137_20281_x210740532}

[[申请内存失败]{style="font-family:宋体"}]{#struct_0_x1137_20281_x2113744189}

[[Failed to process a configuration command.]{lang="EN-US"}]{#struct_0_x1137_20281_1884529250}

[[处理配置失败]{style="font-family:宋体"}]{#struct_0_x1137_20281_730809999}

[[Failed to add the static CRLSP (*crlsp-name*) to DBM.]{lang="EN-US"}]{#struct_0_x1137_20281_x1155980322}

[[保存名为]{style="font-family:宋体"}*[crlsp-name]{lang="EN-US"}*]{#struct_0_x1137_20281_1884070499}[的静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的配置失败]{style="font-family:宋体"}

[[Failed to send the GR start message to LSM.]{lang="EN-US"}]{#struct_0_x1137_20281_x495487127}

[[向]{style="font-family:宋体"}[LSM]{lang="EN-US"}]{#struct_0_x1137_20281_418028226}[模块发送]{style="font-family:宋体"}[GR start]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[[Failed to send the GR end message to LSM.]{lang="EN-US"}]{#struct_0_x1137_20281_233404801}

[[向]{style="font-family:宋体"}[LSM]{lang="EN-US"}]{#struct_0_x1137_20281_1884004963}[模块发送]{style="font-family:宋体"}[GR end]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging mpls te static-cr-lsp]{lang="EN-US"}]{#struct_0_x1137_20281_1879525860}[ event]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2046709416}[[字段]{style="font-family:黑体"}]{#struct_0_x1137_20281_x580808145}

[[描述]{style="font-family:黑体"}]{#struct_0_x1137_20281_x799235951}

[[Received an interface next hop changed event from route management.]{lang="EN-US"}]{#struct_0_x1137_20281_1884201571}

[[收到路由管理下一跳变化事件]{style="font-family:宋体"}]{#struct_0_x1137_20281_281996368}

[[Registered to L3VPN.]{lang="EN-US"}]{#struct_0_x1137_20281_x844457598}

[[向]{style="font-family:宋体"}[L3VPN]{lang="EN-US"}]{#struct_0_x1137_20281_x2032022962}[模块注册成功]{style="font-family:宋体"}

[[Failed to register to L3VPN.]{lang="EN-US"}]{#struct_0_x1137_20281_1884136035}

[[向]{style="font-family:宋体"}[L3VPN]{lang="EN-US"}]{#struct_0_x1137_20281_x90021752}[模块注册失败]{style="font-family:宋体"}

[[Failed to send a batch backup message.]{lang="EN-US"}]{#struct_0_x1137_20281_911888015}

[[发送批备消息失败]{style="font-family:宋体"}]{#struct_0_x1137_20281_1884332643}

[[Received an HA upgrade event.]{lang="EN-US"}]{#struct_0_x1137_20281_x2033676709}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x1137_20281_267234477}[升级事件]{style="font-family:宋体"}

[[Received an HA degrade event.]{lang="EN-US"}]{#struct_0_x1137_20281_x256443827}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x1137_20281_1884267107}[降级事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mpls te static-cr-lsp]{lang="EN-US"}]{#struct_0_x1137_20281_669111685}[ process]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2030850834}[[字段]{style="font-family:黑体"}]{#struct_0_x1137_20281_x993975295}

[[描述]{style="font-family:黑体"}]{#struct_0_x1137_20281_x430930844}

[[Status of CRLSP (name *crlsp-name*, role *role*) changed from down to up.]{lang="EN-US"}]{#struct_0_x1137_20281_1884463715}

[[名为]{style="font-family:宋体"}*[crlsp-name]{lang="EN-US"}*]{#struct_0_x1137_20281_x1274281390}*[，]{style="font-family:宋体"}*[角色为]{style="font-family:宋体"}*[role]{lang="EN-US"}*[的静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[状态从]{style="font-family:宋体"}[down]{lang="EN-US"}[变为]{style="font-family:宋体"}[up]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[role]{lang="EN-US"}*[的取值包括]{style="font-family:宋体"}[ingress]{lang="EN-US"}[、]{style="font-family:宋体"}[transit]{lang="EN-US"}[和]{style="font-family:宋体"}[egress]{lang="EN-US"}

[[Status of CRLSP (name *crlsp-name*, role *role*) changed from up to down.]{lang="EN-US"}]{#struct_0_x1137_20281_1452219357}

[[名为]{style="font-family:宋体"}*[crlsp-name]{lang="EN-US"}*]{#struct_0_x1137_20281_522933651}*[，]{style="font-family:宋体"}*[角色为]{style="font-family:宋体"}*[role]{lang="EN-US"}*[的静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[状态从]{style="font-family:宋体"}[up]{lang="EN-US"}[变为]{style="font-family:宋体"}[down]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[role]{lang="EN-US"}*[的取值包括]{style="font-family:宋体"}[ingress]{lang="EN-US"}[、]{style="font-family:宋体"}[transit]{lang="EN-US"}[和]{style="font-family:宋体"}[egress]{lang="EN-US"}

[[Created an LSM entry for the static CRLSP: name *crlsp-name*, role *role*, in label *in-label*, out label *out-label*, out interface index *out-interface-index*.]{lang="EN-US"}]{#struct_0_x1137_20281_1884398179}

[[向]{style="font-family:宋体"}[LSM]{lang="EN-US"}]{#struct_0_x1137_20281_750441148}[创建静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[成功，静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的名称为]{style="font-family:宋体"}*[crlsp-name]{lang="EN-US"}[，]{style="font-family:宋体"}*[角色为]{style="font-family:宋体"}*[role]{lang="EN-US"}*[，入标签为]{style="font-family:宋体"}*[in-label]{lang="EN-US"}*[，出标签为]{style="font-family:宋体"}*[out-label]{lang="EN-US"}*[，出接口索引为]{style="font-family:宋体"}*[out-interface-index]{lang="EN-US"}*[的表项。其中，]{style="font-family:宋体"}*[role]{lang="EN-US"}*[的取值包括]{style="font-family:宋体"}[ingress]{lang="EN-US"}[、]{style="font-family:宋体"}[transit]{lang="EN-US"}[和]{style="font-family:宋体"}[egress]{lang="EN-US"}

[[Failed to create an LSM entry for the static CRLSP: name *crlsp-name*, role *role*, in label *in-label*, out label *out-label*, out interface index *out-interface-index*.]{lang="EN-US"}]{#struct_0_x1137_20281_x1311867374}

[[向]{style="font-family:宋体"}[LSM]{lang="EN-US"}]{#struct_0_x1137_20281_1711985406}[创建静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[失败，静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的名称为]{style="font-family:宋体"}*[crlsp-name]{lang="EN-US"}[，]{style="font-family:宋体"}*[角色为]{style="font-family:宋体"}*[role]{lang="EN-US"}*[，入标签为]{style="font-family:宋体"}*[in-label]{lang="EN-US"}*[，出标签为]{style="font-family:宋体"}*[out-label]{lang="EN-US"}*[，出接口索引为]{style="font-family:宋体"}*[out-interface-index]{lang="EN-US"}*[的表项。其中，]{style="font-family:宋体"}*[role]{lang="EN-US"}*[的取值包括]{style="font-family:宋体"}[ingress]{lang="EN-US"}[、]{style="font-family:宋体"}[transit]{lang="EN-US"}[和]{style="font-family:宋体"}[egress]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1137_20281_1884594787}

[[\# ]{lang="EN-US"}]{#struct_0_x1137_20281_x479966909}[设备上打开静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[错误调试信息开关。配置消息失败时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mpls te management error]{lang="EN-US"}]{#struct_0_x1137_20281_199343750}

[\*Mar 17 09:12:30:026 2014 Sysname SCRLSP/7/ERROR: -MDC=1; Failed to process a configuration command.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1137_20281_1515441348}*[处理配置失败。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1137_20281_1200721921}[设备上打开静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[事件调试信息开关。路由消息变化时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname \>debugging mpls static-cr-lsp event]{lang="EN-US"}]{#struct_0_x1137_20281_x1440704474}

[\*Mar 17 09:07:56:064 2014 Sysname SCRLSP/7/EVENT: -MDC=1; Received an interface next hop changed event from route management.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1137_20281_437947779}*[收到路由管理的路由变化通知消息。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1137_20281_1884529251}[设备上打开静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[处理过程调试信息开关。]{style="font-family:宋体"}[Egress LSP]{lang="EN-US"}[隧道创建时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname \>debugging mpls static-cr-lsp process]{lang="EN-US"}]{#struct_0_x1137_20281_730744463}

[\*Mar 17 09:05:21:898 2014 Sysname SCRLSP/7/PROCESS: -MDC=1; Status of CRLSP (name egress1; role egress) changed from down to up.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1137_20281_1873468393}*[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[名为]{style="font-family:宋体"}[egress1]{lang="EN-US"}[，角色为]{style="font-family:宋体"}[role]{lang="EN-US"}[为]{style="font-family:宋体"}[egress]{lang="EN-US"}[的状态从]{style="font-family:宋体"}[down]{lang="EN-US"}[变化为]{style="font-family:宋体"}[up]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Mar 17 09:05:21:898 2014 Sysname SCRLSP/7/PROCESS: -MDC=1; Created an LSM entry for the static CRLSP: name egress1; role egress; in label 100; out label 4294967295; out interface index 0.]{lang="EN-US"}]{#struct_0_x1137_20281_x1629253710}

[*[// ]{lang="EN-US"}*]{#struct_0_x1137_20281_x1992718756}*[向]{style="font-family:宋体"}[LSM]{lang="EN-US"}[创建静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[成功，静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[名为]{style="font-family:宋体"}[egress1]{lang="EN-US"}[，角色为]{style="font-family:宋体"}[role]{lang="EN-US"}[为]{style="font-family:宋体"}[egress]{lang="EN-US"}[，入标签为]{style="font-family:宋体"}[100]{lang="EN-US"}[，出标签为无效（]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[），出接口索引为无效值（]{style="font-family:宋体"}[0]{lang="EN-US"}[）的表项。]{style="font-family:宋体"}*
