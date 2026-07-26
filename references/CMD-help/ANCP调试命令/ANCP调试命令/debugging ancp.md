::: {#1552812949 .myid}
[]{#_Toc404785468}[]{#struct_0_x6514_x1315_1844445919}[]{#_Toc205700592}[]{#_Toc205697805}

**ANCP调试命令 \-- ANCP调试命令 \-- debugging ancp**

------------------------------------------------------------------------

[**[debugging ]{lang="FR"}[ancp]{lang="EN-US"}**]{#struct_0_x6514_x1315_1126360448}[命令用来打开]{style="font-family:宋体"}[ANCP]{lang="FR"}[的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging ]{lang="FR"}[ancp]{lang="EN-US"}**]{#struct_0_x6514_x1315_1056363924}[命令用来关闭]{style="font-family:
宋体"}[ANCP]{lang="FR"}[的调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6514_x1315_x2098411675}

[**[debugging ancp]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x6514_x1315_2027778047}

[**[undo debugging ancp]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x6514_x1315_1100467228}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6514_x1315_x1545699015}

[[ANCP]{lang="EN-US"}]{#struct_0_x6514_x1315_x293409399}[的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6514_x1315_x1584919367}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x228971929}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6514_x1315_x1568967082}

[[network-admin]{lang="EN-US"}]{#struct_0_x6514_x1315_x1529744627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6514_x1315_x1176805882}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6514_x1315_x1533267235}

[**[all]{lang="EN-US"}**]{#struct_0_x6514_x1315_x283363704}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x6514_x1315_x1771974674}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6514_x1315_353424661}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x6514_x1315_x258464991}[：表示报文调试信息开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6514_x1315_x509720017}

[[表1-1 ]{lang="EN-US"}[debugging ancp error]{lang="EN-US"}]{#struct_0_x6514_x1315_1149497731}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1297000081}[[字段]{style="font-family:黑体"}]{#struct_0_x6514_x1315_1656290380}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6514_x1315_x1022220982}

[[Failed to send a(an) *type* message to neighbor *neighbor-name*.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1010850628}

[[向邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_1491814268}[发送]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文失败。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_x6514_x1315_x2073286121}[：]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_x6514_x1315_1369950017}[：]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_x6514_x1315_442847910}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTACK]{lang="EN-US"}]{#struct_0_x6514_x1315_1420310740}[：]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OAM Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_76362751}[：线路检测管理]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Line Config Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_1412528748}[：线路配置管理报文]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic Response]{lang="EN-US"}]{#struct_0_x6514_x1315_x1245402794}[：一般应答报文]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to send a SYN message.]{lang="EN-US"}]{#struct_0_x6514_x1315_1614928577}

[[发送]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x6514_x1315_34318554}[报文失败]{style="font-family:宋体"}

[[Capability not supported(*CapType*). ]{lang="EN-US"}]{#struct_0_x6514_x1315_x674775539}

[[不支持的能力集，其中]{style="font-family:宋体"}*[CapType]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1565564817}[为当前能力集字段的取值]{style="font-family:宋体"}

[[Interface *interfaceName* with socket *sock* discarded the received data: Invalid encapsulating header.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1879528597}

[[接口名为]{style="font-family:宋体"}*[interfaceName]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1971712601}[，]{style="font-family:宋体"}[Socket]{lang="EN-US"}[为]{style="font-family:宋体"}*[sock]{lang="EN-US"}*[的通信接口丢弃包含有不合法的封装头的接收数据]{style="font-family:宋体"}

[[Discarded a message: Invalid version.]{lang="EN-US"}]{#struct_0_x6514_x1315_x153555193}

[[收到报文中]{style="font-family:宋体"}*[version]{lang="EN-US"}*]{#struct_0_x6514_x1315_x2077250708}[（版本号）不合法，丢弃]{style="font-family:宋体"}

[[Discarded a message: Unknown message type.]{lang="EN-US"}]{#struct_0_x6514_x1315_754957599}

[[收到未知类型的报文，丢弃]{style="font-family:宋体"}]{#struct_0_x6514_x1315_181718002}

[[Discarded a message: Insufficient length.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1433205500}

[[报文长度不够，丢弃]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x1882670173}

[[Discarded a message from neighbor *neighbor-name*: Invalid version.]{lang="EN-US"}]{#struct_0_x6514_x1315_475584570}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1087518818}[的一个报文，因为其中的]{style="font-family:宋体"}[version]{lang="EN-US"}[（版本号）不合法]{style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Result field.]{lang="EN-US"}]{#struct_0_x6514_x1315_600011345}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1719639134}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[Result]{lang="EN-US"}[（结果域）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_x793890811}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_x2086918487}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_x452426099}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adjacency Update]{lang="EN-US"}]{#struct_0_x6514_x1315_978859758}[：]{style="font-family:宋体"}[邻接更新报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic Response]{lang="EN-US"}]{#struct_0_x6514_x1315_x340069697}[：]{style="font-family:宋体"}[一般应答报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a *type* message from neighbor *neighbor-name*: Invalid ResultCode field.]{lang="EN-US"}]{#struct_0_x6514_x1315_479996372}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_1009244221}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[ResultCode]{lang="EN-US"}[（结果代码域）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_44234390}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_x1397015305}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic Response]{lang="EN-US"}]{#struct_0_x6514_x1315_978947528}[：]{style="font-family:宋体"}[一般应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_384818068}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Partition ID field.]{lang="EN-US"}]{#struct_0_x6514_x1315_x339789011}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x80801036}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[Partition ID]{lang="EN-US"}[（分区]{style="font-family:宋体"}[ID]{lang="EN-US"}[）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_x556839720}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_1612915531}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic Response]{lang="EN-US"}]{#struct_0_x6514_x1315_1766810063}[：]{style="font-family:宋体"}[一般应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_x1233628471}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adjacency Update]{lang="EN-US"}]{#struct_0_x6514_x1315_1592477767}[：]{style="font-family:宋体"}[邻接更新报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid I Flag and SubMessage Number field.]{lang="EN-US"}]{#struct_0_x6514_x1315_x812790591}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x2122923661}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[I Flag]{lang="EN-US"}[和]{style="font-family:宋体"}[SubMessage Number]{lang="EN-US"}[（分片标记和分片序列号）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_x1690694869}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_x296889825}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic Response]{lang="EN-US"}]{#struct_0_x6514_x1315_x658240200}[：]{style="font-family:宋体"}[一般应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Managemen]{lang="EN-US"}]{#struct_0_x6514_x1315_793375206}[t]{lang="EN-US"}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adjacency Update]{lang="EN-US"}]{#struct_0_x6514_x1315_x1326193664}[：]{style="font-family:宋体"}[邻接更新报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid length value in the message header.]{lang="EN-US"}]{#struct_0_x6514_x1315_605959694}

[]{#OLE_LINK4}[]{#OLE_LINK3}[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1936700639}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为报文头中的]{style="font-family:宋体"}[length]{lang="EN-US"}[（长度）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_780858845}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_963423902}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic Response]{lang="EN-US"}]{#struct_0_x6514_x1315_x1785765089}[：]{style="font-family:宋体"}[一般应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_x960124247}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adjacency Update]{lang="EN-US"}]{#struct_0_x6514_x1315_840758057}[：]{style="font-family:宋体"}[邻接更新报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Transaction ID field.]{lang="EN-US"}]{#struct_0_x6514_x1315_1927626027}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x113292698}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[Transaction ID]{lang="EN-US"}[（业务]{style="font-family:宋体"}[ID]{lang="EN-US"}[）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_796911804}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_1056298388}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_x239351261}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adjacency Update]{lang="EN-US"}]{#struct_0_x6514_x1315_161705373}[：]{style="font-family:宋体"}[邻接更新报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a *type* message from neighbor *neighbor-name*: Invalid Message Type field.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1157060778}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1908308215}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[Message Type]{lang="EN-US"}[（消息类型）不合法，与报文头中的不一致。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_x509785553}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_x1222756210}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_x1625572492}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Tech Type field.]{lang="EN-US"}]{#struct_0_x6514_x1315_972074145}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_486655548}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[Tech Type]{lang="EN-US"}[（线路类型）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_1412463212}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_1530898127}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_x6514_x1315_x1640908564}[：]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_x6514_x1315_1305713720}[：]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_x6514_x1315_789688048}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTACk]{lang="EN-US"}]{#struct_0_x6514_x1315_x153620729}[：]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Discarded a *type* message from neighbor *neighbor-name*: Invalid \# of TLVs field.]{lang="EN-US"}]{#struct_0_x6514_x1315_x916589879}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x2037644610}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[\# of TlVs]{lang="EN-US"}[（扩展数据域中的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[个数）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_x1069302112}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_x1719704670}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_x1853434961}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a *type* message from neighbor *neighbor-name*: Invalid Extension Block length field.]{lang="EN-US"}]{#struct_0_x6514_x1315_x373494232}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_1009178685}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[Extension Block length]{lang="EN-US"}[（扩展数据域长度）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_1598671003}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_1496441807}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_x556905256}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a Port Management message from neighbor *neighbor-name*: Invalid Function field.]{lang="EN-US"}]{#struct_0_x6514_x1315_124365793}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x543228790}[的线路管理报文，因为其中的]{style="font-family:宋体"}[Function]{lang="EN-US"}[（线路检测与线路配置标示）不合法]{style="font-family:宋体"}

[[Discarded a Port Management message from neighbor *neighbor-name*: Invalid X-Function field.]{lang="EN-US"}]{#struct_0_x6514_x1315_x2122989197}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_605894158}[的线路管理报文，因为其中的]{style="font-family:宋体"}[X-Function]{lang="EN-US"}[（对]{style="font-family:宋体"}[Function]{lang="EN-US"}[的补充说明）不合法]{style="font-family:宋体"}

[[Discarded a *type* message from neighbor *neighbor-name*: Insufficient length.]{lang="EN-US"}]{#struct_0_x6514_x1315_x960189783}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1820200836}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为报文长度不够。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_1372271385}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_x182927194}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_1056232852}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a Port Management message from neighbor *neighbor-name*: The neighbor does not support Line Config Capability.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1701430240}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_219480454}[的线路管理报文，因为该邻居不支持线路配置能力]{style="font-family:宋体"}

[]{#struct_0_x6514_x1315_x509851089}[]{#OLE_LINK10}[[Discarded a]{lang="EN-US"}]{#OLE_LINK9}[ Port Management message from neighbor *neighbor-name*: The neighbor does not support OAM Capability.]{lang="EN-US"}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x419666296}[的线路管理报文，因为该邻居不支持]{style="font-family:宋体"}[OAM]{lang="EN-US"}[（线路检测）能力]{style="font-family:宋体"}

[[Discarded a *type* message from neighbor *neighbor-name*: The neighbor does not support Topology Discovery Capacity.]{lang="EN-US"}]{#struct_0_x6514_x1315_x86655972}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_1466364134}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为该邻居不支持线路拓扑发现能力。其中，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以是*：*]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_1546680940}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_x16301169}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[Discarded a(an) Unknown message from neighbor *neighbor-name*: Invalid Code field.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1739483918}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x252430146}[的未知类型的报文，因为其中的]{style="font-family:宋体"}[Code]{lang="EN-US"}[（邻接报文类型）不合法]{style="font-family:宋体"}

[[Discarded a SYN message from neighbor *neighbor-name*: Invalid M flag.]{lang="EN-US"}]{#struct_0_x6514_x1315_x19403001}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x657447616}[的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文，因为其中的]{style="font-family:宋体"}[M flag]{lang="EN-US"}[（]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文发起标示）不合法]{style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Capability Fields. ]{lang="EN-US"}]{#struct_0_x6514_x1315_x1707294132}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_1017301291}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[Capability Fields]{lang="EN-US"}[（能力域）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_x6514_x1315_x1585486942}[：]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_x6514_x1315_25875782}[：]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x1854553473}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTACK]{lang="EN-US"}]{#struct_0_x6514_x1315_1143396413}[：]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid PFlag.]{lang="EN-US"}]{#struct_0_x6514_x1315_1279559768}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_432937707}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[P Flag]{lang="EN-US"}[（邻接建立类型）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_x6514_x1315_x1724732900}[：]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x422687528}[：]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x2024502019}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTACK]{lang="EN-US"}]{#struct_0_x6514_x1315_1576783568}[：]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid PType field.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1988771469}

[[丢弃来自邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x559026658}[的]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文，因为其中的]{style="font-family:宋体"}[P Type]{lang="EN-US"}[（分区使用标志及协商方式）不合法。其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_x6514_x1315_x1982908929}[：]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_x6514_x1315_740111886}[：]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x1221021925}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x1680598394}[：]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Not enough memory resources.]{lang="EN-US"}]{#struct_0_x6514_x1315_x825972055}

[[内存资源不足]{style="font-family:宋体"}]{#struct_0_x6514_x1315_2145315568}

[[Failed to add a circuit entry: Not enough memory resources.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1177888545}

[[由于内存资源不足，添加线路结点失败]{style="font-family:宋体"}]{#struct_0_x6514_x1315_1190450580}

[[Not enough TCP socket resources.]{lang="EN-US"}]{#struct_0_x6514_x1315_366958641}

[[TCP socket]{lang="EN-US"}]{#struct_0_x6514_x1315_x1226897585}[资源不足]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ancp event]{lang="EN-US"}]{#struct_0_x6514_x1315_170119112}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1308187227}[[字段]{style="font-family:黑体"}]{#struct_0_x6514_x1315_2791527}

[[描述]{style="font-family:黑体"}]{#struct_0_x6514_x1315_872463661}

[[Established the adjacency with neighbor *neighbor-name*.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1720294385}

[[与邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_2022903595}[建立邻接关系]{style="font-family:宋体"}

[[The FSM state for neighbor *neighbor-name* with peer ID *H-H-H* changed from *state1* to *state2.*]{lang="EN-US"}]{#struct_0_x6514_x1315_x375633361}

[[名为]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_1640396638}[，]{style="font-family:宋体"}[Peer ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[H-H-H]{lang="EN-US"}*[的邻居状态机状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[。其中，]{style="font-family:宋体"}*[state1]{lang="EN-US"}[、]{style="font-family:宋体"}[state2]{lang="EN-US"}*[的取值可以是：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNSENT]{lang="EN-US"}]{#struct_0_x6514_x1315_x1896511405}[：]{style="font-family:宋体"}[SYNSENT]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNRCVD]{lang="EN-US"}]{#struct_0_x6514_x1315_x1080385301}[：]{style="font-family:宋体"}[SYNRECV]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTAB]{lang="EN-US"}]{#struct_0_x6514_x1315_x542283539}[：]{style="font-family:宋体"}[ESTAB]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Halted the adjacency relationship with neighbor *neighbor-name*, because the set of Capabilities is empty.]{lang="EN-US"}]{#struct_0_x6514_x1315_1778424847}

[[由于协商的能力集为空，断开与邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_230819562}[的邻接关系]{style="font-family:宋体"}

[[Interface *interfaceName* with socket *sock* stopped adjacency establishment, because it failed to receive a response from the peer after completing retransmission in *SYNSENT* state.]{lang="EN-US"}]{#struct_0_x6514_x1315_93347341}

[[通信接口（源接口名为]{style="font-family:宋体"}*[interfaceName]{lang="EN-US"}*]{#struct_0_x6514_x1315_611464153}[，]{style="font-family:宋体"}[socket]{lang="EN-US"}[为]{style="font-family:宋体"}*[sock]{lang="EN-US"}*[）在]{style="font-family:宋体"}[SYNSENT]{lang="EN-US"}[状态下完成超时重传后，还未收到对端回应，中断邻接建立过程]{style="font-family:宋体"}

[[Halted the adjacency relationship with neighbor *neighbor-name*, due to failure to receive a response from the peer after completing retransmission in *states* state. ]{lang="EN-US"}]{#struct_0_x6514_x1315_1446932958}

[[在]{style="font-family:宋体"}*[states]{lang="EN-US"}*]{#struct_0_x6514_x1315_1546615404}[状态下完成超时重传后，还未收到来自对端的回应，断开与邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*[的邻接关系。其中]{style="font-family:宋体"}*[states]{lang="EN-US"}*[的取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNSENT]{lang="EN-US"}]{#struct_0_x6514_x1315_359327170}[：]{style="font-family:宋体"}[SYNSENT]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNRCVD]{lang="EN-US"}]{#struct_0_x6514_x1315_x808264883}[：]{style="font-family:宋体"}[SYNRECV]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Halted the adjacency relationship with neighbor *neighbor-name*, due to failure to receive ACK messages from the peer within three periods of the adjacency timer.]{lang="EN-US"}]{#struct_0_x6514_x1315_900580132}

[[由于三个邻接定时器周期内未收到邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_1543550743}[对端回应]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，断开邻接关系]{style="font-family:宋体"}

[[Halted the adjacency relationship with neighbor *neighbor-name*, because the peer disconnected the TCP connection.]{lang="EN-US"}]{#struct_0_x6514_x1315_1787446062}

[[由于邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x182558687}[对端关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，断开邻接关系]{style="font-family:宋体"}

[[Interface *interfaceName* with socket *sock* halted the adjacency relationship, because the peer disconnected the TCP connection.]{lang="EN-US"}]{#struct_0_x6514_x1315_1312989179}

[[通信接口（接口名为]{style="font-family:宋体"}*[interfaceName]{lang="EN-US"}*]{#struct_0_x6514_x1315_623064126}[，]{style="font-family:宋体"}[socket]{lang="EN-US"}[为]{style="font-family:宋体"}*[sock]{lang="EN-US"}*[）的对端关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，断开邻接关系]{style="font-family:宋体"}

[[Interface *interfaceName* with socket *sock* halted the adjacency relationship after receiving an EPOLLHUP/EPOLLERR signal.]{lang="EN-US"}]{#struct_0_x6514_x1315_1505395151}

[[通信接口（源接口名为]{style="font-family:宋体"}*[interfaceName]{lang="EN-US"}*]{#struct_0_x6514_x1315_x19468537}[，]{style="font-family:宋体"}[socket]{lang="EN-US"}[为]{style="font-family:宋体"}*[sock]{lang="EN-US"}*[）由于收到]{style="font-family:宋体"}[EPOLLHUP/EPOLLERR]{lang="EN-US"}[（]{style="font-family:宋体"}[EPOLL]{lang="EN-US"}[挂起]{style="font-family:宋体"}[/EPOLL]{lang="EN-US"}[错误）信号，断开邻接关系]{style="font-family:宋体"}

[[Halted the adjacency relationship with neighbor *neighbor-name* after receiving an EPOLLHUP/EPOLLERR signal.]{lang="EN-US"}]{#struct_0_x6514_x1315_876119097}

[[由于收到]{style="font-family:宋体"}[EPOLLHUP/EPOLLERR]{lang="EN-US"}]{#struct_0_x6514_x1315_x807441030}[（]{style="font-family:宋体"}[EPOLL]{lang="EN-US"}[挂起]{style="font-family:宋体"}[/EPOLL]{lang="EN-US"}[错误）信号，断开与邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*[的邻接关系]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ancp packet]{lang="EN-US"}]{#struct_0_x6514_x1315_x35297794}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1305592389}[[字段]{style="font-family:黑体"}]{#struct_0_x6514_x1315_x1004879187}

[[描述]{style="font-family:黑体"}]{#struct_0_x6514_x1315_593169792}

[[Received a(an) *type* message from neighbor *neighbor-name*.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1900566774}

[[收到邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_x523668495}[的一个]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文]{style="font-family:宋体"}

[[其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x6514_x1315_862430842}[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_x6514_x1315_397341343}[：]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_x6514_x1315_448569761}[：]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x526663417}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x1585552478}[：]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_1413244976}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Up]{lang="EN-US"}]{#struct_0_x6514_x1315_x8792108}[：]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Down]{lang="EN-US"}]{#struct_0_x6514_x1315_x1055841344}[：]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Adjacency Update]{lang="EN-US"}]{#struct_0_x6514_x1315_526779750}[：]{style="font-family:宋体"}[邻接更新报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic Response]{lang="EN-US"}]{#struct_0_x6514_x1315_x1147112532}[：]{style="font-family:宋体"}[一般应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Provisioning]{lang="EN-US"}]{#struct_0_x6514_x1315_314027849}[：]{style="font-family:宋体"}[信息提供报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x6514_x1315_x1737957391}[：未知报文]{style="font-family:宋体"}

[[Sent a(an) *type* message to neighbor *neighbor-name*.]{lang="EN-US"}]{#struct_0_x6514_x1315_1704304012}

[[向邻居]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*]{#struct_0_x6514_x1315_1677850231}[发送一个]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的报文。]{style="font-family:宋体"}

[[其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x6514_x1315_1143330877}[的类型可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_x6514_x1315_x1799404552}[：]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x1686061848}[：]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_x6514_x1315_91314649}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTACK]{lang="EN-US"}]{#struct_0_x6514_x1315_x1047383082}[：]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_277465028}[：]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic Response]{lang="EN-US"}]{#struct_0_x6514_x1315_x587192129}[：]{style="font-family:宋体"}[一般应答报文]{lang="EN-US" style="font-family:宋体"}

[[Identifier: *identifier*]{lang="EN-US"}]{#struct_0_x6514_x1315_x422749390}

[[标识符，用于标示]{style="font-family:宋体"}[GSMP]{lang="EN-US"}]{#struct_0_x6514_x1315_674306807}[协议或]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[协议，必须为：]{style="font-family:宋体"}[0x880c]{lang="EN-US"}

[[Length: *length*]{lang="EN-US"}]{#struct_0_x6514_x1315_x422753064}

[[ANCP]{lang="EN-US"}]{#struct_0_x6514_x1315_x1242407094}[消息的长度，不包括]{style="font-family:宋体"}[4]{lang="EN-US"}[字节的封装头长度]{style="font-family:宋体"}

[[Version: *version*]{lang="EN-US"}]{#struct_0_x6514_x1315_945478203}

[[ANCP]{lang="EN-US"}]{#struct_0_x6514_x1315_x739288699}[协议版本域]{style="font-family:宋体"}

[[Message Type: *message-type*]{lang="EN-US"}]{#struct_0_x6514_x1315_2014348993}

[[ANCP]{lang="EN-US"}]{#struct_0_x6514_x1315_x1844208416}[协议消息类型，总共有]{style="font-family:宋体"}[7]{lang="EN-US"}[种，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0xa]{lang="EN-US"}]{#struct_0_x6514_x1315_x1604897783}[：]{style="font-family:宋体"}[Adjacency Protocol]{lang="EN-US"}[，]{style="font-family:宋体"}[邻接报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x32]{lang="EN-US"}]{#struct_0_x6514_x1315_1526011758}[：]{style="font-family:宋体"}[Port Management]{lang="EN-US"}[，]{style="font-family:宋体"}[线路管理报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x80]{lang="EN-US"}]{#struct_0_x6514_x1315_x1988837005}[：]{style="font-family:宋体"}[Port Up]{lang="EN-US"}[，]{style="font-family:宋体"}[线路]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x81]{lang="EN-US"}]{#struct_0_x6514_x1315_x810400390}[：]{style="font-family:宋体"}[Port Down]{lang="EN-US"}[，]{style="font-family:宋体"}[线路下线报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x85]{lang="EN-US"}]{#struct_0_x6514_x1315_x1084697948}[：]{style="font-family:宋体"}[Adjacency Update]{lang="EN-US"}[，]{style="font-family:宋体"}[邻接更新报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x91]{lang="EN-US"}]{#struct_0_x6514_x1315_509831253}[：]{style="font-family:宋体"}[Generic Response]{lang="EN-US"}[，]{style="font-family:宋体"}[一般应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x93]{lang="EN-US"}]{#struct_0_x6514_x1315_829382297}[：]{style="font-family:宋体"}[Provisioning]{lang="EN-US"}[，]{style="font-family:宋体"}[信息提供报文]{lang="EN-US" style="font-family:宋体"}

[[M flag and Code: *m-code*]{lang="EN-US"}]{#struct_0_x6514_x1315_x807826933}

[[邻接报文中]{style="font-family:宋体"}[M Flag]{lang="EN-US"}]{#struct_0_x6514_x1315_1886575389}[和]{style="font-family:宋体"}[Code]{lang="EN-US"}[，共]{style="font-family:宋体"}[8]{lang="EN-US"}[位，其中，]{style="font-family:宋体"}[M Flag]{lang="EN-US"}[为第一位，用于标识]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文发起者身份，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:宋体"}[AN]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[；其余]{style="font-family:宋体"}[7]{lang="EN-US"}[位为]{style="font-family:宋体"}[Code]{lang="EN-US"}[，表示邻接消息类型，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[4]{lang="EN-US"}[，依次代表]{style="font-family:宋体"}[SYN]{lang="EN-US"}[、]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[、]{style="font-family:宋体"}[ACK]{lang="EN-US"}[、]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文。正常情况下取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x81]{lang="EN-US"}]{#struct_0_x6514_x1315_740046350}[：]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[端发出的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x01]{lang="EN-US"}]{#struct_0_x6514_x1315_x1984654107}[：]{style="font-family:宋体"}[AN]{lang="EN-US"}[端发出的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x02]{lang="EN-US"}]{#struct_0_x6514_x1315_x2040411475}[：]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x03]{lang="EN-US"}]{#struct_0_x6514_x1315_x1146065259}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x04]{lang="EN-US"}]{#struct_0_x6514_x1315_1614907175}[：]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Sender Name: *sender-name*]{lang="EN-US"}]{#struct_0_x6514_x1315_1638103197}

[[发送端的标示]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x2073196147}

[[Receiver Name: *receiver-name*]{lang="EN-US"}]{#struct_0_x6514_x1315_x826037591}

[[接收端的标示]{style="font-family:宋体"}]{#struct_0_x6514_x1315_847547344}

[[Sender Port: *sender-port*]{lang="EN-US"}]{#struct_0_x6514_x1315_147571395}

[[发送端端口号]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x194467514}

[[Receiver Port: *receiver-port*]{lang="EN-US"}]{#struct_0_x6514_x1315_876714687}

[[接收端端口号]{style="font-family:宋体"}]{#struct_0_x6514_x1315_1190385044}

[[PType: *ptype*]{lang="EN-US"}]{#struct_0_x6514_x1315_x1612335459}

[[邻接报文中]{style="font-family:宋体"}[PType]{lang="EN-US"}]{#struct_0_x6514_x1315_x1287268221}[字段，用于确定是否使用分区及分区]{style="font-family:宋体"}[ID]{lang="EN-US"}[的协商方式，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x0]{lang="EN-US"}]{#struct_0_x6514_x1315_x1323751203}[：不支持分区]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_x6514_x1315_x1260497267}[：]{style="font-family:宋体"}[固定的分]{lang="EN-US" style="font-family:宋体"}[区]{style="font-family:宋体"}[请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_x6514_x1315_x375698897}[：]{style="font-family:宋体"}[固定的分区分配]{lang="EN-US" style="font-family:宋体"}

[[P Flag: *p-flag*]{lang="EN-US"}]{#struct_0_x6514_x1315_x1029022224}

[[邻接建立类型，取值为：]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x2089131668}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_x6514_x1315_1899782799}[：新建邻接]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_x6514_x1315_1546549868}[：恢复邻接]{style="font-family:宋体"}

[[Sender Instance: *sender-instance*]{lang="EN-US"}]{#struct_0_x6514_x1315_761879715}

[[发送端实例号]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x1808965777}

[[Partition ID: *partition-id*]{lang="EN-US"}]{#struct_0_x6514_x1315_457440629}

[[分区]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x1240212448}[ID]{lang="EN-US"}

[[Receiver Instance: *receiver-instance*]{lang="EN-US"}]{#struct_0_x6514_x1315_x19534073}

[[接收]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_x6514_x1315_x1075894841}[端]{style="font-family:宋体"}[实例号]{lang="EN-US" style="font-family:宋体"}

[[\# of Caps: *of-caps*]{lang="EN-US"}]{#struct_0_x6514_x1315_x1735193329}

[[能力域个数]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_x6514_x1315_12051034}

[[Total Length: *total-length*]{lang="EN-US"}]{#struct_0_x6514_x1315_x1596874861}

[[邻接报文中能力域总字节长度]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x1585618014}

[[Result: *result*]{lang="EN-US"}]{#struct_0_x6514_x1315_1490007468}

[[业务报文中的结果域，具体取值和报文类型有关]{style="font-family:宋体"}]{#struct_0_x6514_x1315_697027918}

[[Result Code: *code*]{lang="EN-US"}]{#struct_0_x6514_x1315_x552600107}

[[业务报文中的结果代码域，具体取值和]{style="font-family:宋体"}]{#struct_0_x6514_x1315_x1990266166}[Result]{lang="EN-US"}[（结果域）有关]{style="font-family:宋体"}

[[Length: *length*]{lang="EN-US"}]{#struct_0_x6514_x1315_1143265341}

[[业务报文中的长度字段]{style="font-family:宋体"}]{#struct_0_x6514_x1315_1704912459}

[[Transaction ID: *transaction-id*]{lang="EN-US"}]{#struct_0_x6514_x1315_x1051903601}

[[业务]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x6514_x1315_1220314944}[，发起一次请求时选择的随机数，用来标识一次业务请求过程]{style="font-family:宋体"}

[[Function: *function*]{lang="EN-US"}]{#struct_0_x6514_x1315_1806393747}

[[Port Management]{lang="EN-US"}]{#struct_0_x6514_x1315_x422818600}[报文中的]{style="font-family:宋体"}[Function]{lang="EN-US"}[字段取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x8]{lang="EN-US"}]{#struct_0_x6514_x1315_x873617740}[：]{style="font-family:宋体"}[Line Configuration]{lang="EN-US"}[（线路配置）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x9]{lang="EN-US"}]{#struct_0_x6514_x1315_268323276}[：]{style="font-family:宋体"}[OAM]{lang="EN-US"}[（线路检测）]{style="font-family:宋体"}

[[Extension Block length: *extension-block-length*]{lang="EN-US"}]{#struct_0_x6514_x1315_x483425930}

[[扩展数据域]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_x6514_x1315_x1988902541}[长度]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6514_x1315_45390576}

[[\# ]{lang="EN-US"}]{#struct_0_x6514_x1315_x2029672726}[在]{style="font-family:宋体"}[BARS]{lang="EN-US"}[设备上配置全局源接口、创建邻居名为]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[的邻居并设置]{style="font-family:宋体"}[peer-id]{lang="EN-US"}[为]{style="font-family:宋体"}[2-2-2]{lang="EN-US"}[，最后使能]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[功能。打开]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[的所有调试开关。]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[与]{style="font-family:宋体"}[BARS]{lang="EN-US"}[设备建立邻接过程后，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[端开始上报线路信息。]{style="font-family:宋体"}

[[\<Syaname\> terminal monitor]{lang="EN-US"}]{#struct_0_x6514_x1315_1280416070}

[The current terminal is enabled to display logs.]{lang="EN-US"}

[\<Syaname\> terminal debugging]{lang="EN-US"}

[The current terminal is enabled to display debugging logs.]{lang="EN-US"}

[\<Syaname\> debugging ancp all]{lang="EN-US"}

[\<Syaname\>\*Jul 16 11:35:07:540 2013 Syaname ANCP/7/PACKET: -MDC=1; Sent a(an) SYN message.]{lang="EN-US"}

[    Identifier: 0x880c    Length: 0x30]{lang="EN-US"}

[    Version: 0x32     Message Type: 0xa]{lang="EN-US"}

[    Timer: 0xfa     M flag and Code: 0x81]{lang="EN-US"}

[    Sender Name: 00-11-22-00-00-01    Receiver Name: 00-00-00-00-00-00]{lang="EN-US"}

[    Sender Port: 0x0     Receiver Port: 0x0]{lang="EN-US"}

[    PType: 0x0  P Flag: 0x1     Sender Instance: 0x5]{lang="EN-US"}

[    Partition ID: 0x0     Receiver Instance: 0x0]{lang="EN-US"}

[    \# of Caps: 0x3     Total Length: 0xc]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1268162527}*[连接建立，发送一个]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jul 16 11:35:07:540 2013 Syaname ANCP/7/PACKET: -MDC=1; Received a(an) SYN message. ]{lang="EN-US"}]{#struct_0_x6514_x1315_1610337126}

[    Identifier: 0x880c     Length: 0x30]{lang="EN-US"}

[    Version: 0x32     Message Type: 0xa]{lang="EN-US"}

[    Timer: 0xfa     M flag and Code: 0x01]{lang="EN-US"}

[    Sender Name: 00-02-00-02-00-02     Receiver Name: 00-00-00-00-00-00]{lang="EN-US"}

[    Sender Port: 0x0     Receiver Port: 0x0]{lang="EN-US"}

[    PType: 0x0, P Flag: 0x1     Sender Instance: 0x1]{lang="EN-US"}

[    Partition ID: 0x0     Receiver Instance: 0x0]{lang="EN-US"}

[    \# of Caps: 0x3     Total Length: 0xc]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6514_x1315_1105557984}*[收到一个]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jul 16 11:35:07:540 2013 Syaname ANCP/7/PACKET: -MDC=1; Sent a(an) SYNACK message to neighbor dslam1.]{lang="EN-US"}]{#struct_0_x6514_x1315_739980814}

[    Identifier: 0x880c     Length: 0x30]{lang="EN-US"}

[    Version: 0x32     Message Type: 0xa]{lang="EN-US"}

[    Timer: 0xfa     M flag and Code: 0x02]{lang="EN-US"}

[    Sender Name: 00-11-22-00-00-01     Receiver Name: 00-02-00-02-00-02]{lang="EN-US"}

[    Sender Port: 0x0     Receiver Port: 0x0]{lang="EN-US"}

[    PType: 0x0  P Flag: 0x1     Sender Instance: 0x5]{lang="EN-US"}

[    Partition ID: 0x0     Receiver Instance: 0x1]{lang="EN-US"}

[    \# of Caps: 0x3     Total Length: 0xc]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1847354533}*[向邻居]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[发送一个]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jul 16 11:35:07:540 2013 Syaname ANCP/7/EVENT: -MDC=1; The FSM state for neighbor dslam1 with peer ID 0002-0002-0002 changed from SYNSENT to SYNRCVD.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1174923641}

[*[// ]{lang="EN-US"}*]{#struct_0_x6514_x1315_1203541822}*[邻居名为]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[，]{style="font-family:宋体"}[peer-id]{lang="EN-US"}[为]{style="font-family:宋体"}[2-2-2]{lang="EN-US"}[的邻居，状态机由]{style="font-family:宋体"}[SYNSENT]{lang="EN-US"}[状态迁移到]{style="font-family:宋体"}[SYNRCVD]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jul 16 11:35:07:541 2013 Syaname ANCP/7/PACKET: -MDC=1; Received a(an) SYNACK message from neighbor dslam1.]{lang="EN-US"}]{#struct_0_x6514_x1315_1554618336}

[    Identifier: 0x880c     Length: 0x30]{lang="EN-US"}

[    Version: 0x32     Message Type: 0xa]{lang="EN-US"}

[    Timer: 0xfa     M flag and Code: 0x02]{lang="EN-US"}

[    Sender Name: 00-02-00-02-00-02     Receiver Name: 00-11-22-00-00-01]{lang="EN-US"}

[    Sender Port: 0x0     Receiver Port: 0x0]{lang="EN-US"}

[    PType: 0x0, P Flag: 0x1     Sender Instance: 0x1]{lang="EN-US"}

[    Partition ID: 0x0     Receiver Instance: 0x5]{lang="EN-US"}

[    \# of Caps: 0x3     Total Length: 0xc]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1754740315}*[收到邻居]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[发送的一个]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jul 16 11:35:07:541 2013 Syaname ANCP/7/PACKET: -MDC=1; Sent a(an) ACK message to neighbor dslam1.]{lang="EN-US"}]{#struct_0_x6514_x1315_x154239031}

[    Version: 0x32     Message Type: 0xa]{lang="EN-US"}

[    Timer: 0xfa     M flag and Code: 0x03]{lang="EN-US"}

[    Sender Name: 00-11-22-00-00-01     Receiver Name: 00-02-00-02-00-02]{lang="EN-US"}

[    Sender Port: 0x0     Receiver Port: 0x0]{lang="EN-US"}

[    PType: 0x0  P Flag: 0x1     Sender Instance: 0x5]{lang="EN-US"}

[    Partition ID: 0x0     Receiver Instance: 0x1]{lang="EN-US"}

[    \# of Caps: 0x3     Total Length: 0xc]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1855118815}*[向邻居]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[发送一个]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jul 16 11:35:07:541 2013 Syaname ANCP/7/EVENT: -MDC=1; The FSM state for neighbor dslam1 with peer ID 0002-0002-0002 changed from SYNRCVD to ESTAB.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1372115981}

[*[// ]{lang="EN-US"}*]{#struct_0_x6514_x1315_337558836}*[邻居名为]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[，]{style="font-family:宋体"}[peer-id]{lang="EN-US"}[为]{style="font-family:宋体"}[2-2-2]{lang="EN-US"}[的邻居，状态机由]{style="font-family:宋体"}[SYNRCVD]{lang="EN-US"}[状态迁移到]{style="font-family:宋体"}[ESTAB]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jul 16 11:35:07:541 2013 Syaname ANCP/7/EVENT: -MDC=1; Established the adjacency with neighbor dslam1.]{lang="EN-US"}]{#struct_0_x6514_x1315_x1454405616}

[*[// ]{lang="EN-US"}*]{#struct_0_x6514_x1315_x2052056618}*[与邻居]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[，建立邻接关系]{style="font-family:宋体"}*

[[\*Jul 16 11:35:07:542 2013 Syaname ANCP/7/PACKET: -MDC=1; Received a(an) ACK message from neighbor dslam1.]{lang="EN-US"}]{#struct_0_x6514_x1315_x826103127}

[   []{#OLE_LINK2}[ Identifier: 0x880c    Length: 0x30]{#OLE_LINK1}]{lang="EN-US"}

[    Version: 0x32    Message Type: 0xa]{lang="EN-US"}

[    Timer: 0xfa     M flag and Code: 0x03]{lang="EN-US"}

[    Sender Name: 00-02-00-02-00-02     Receiver Name: 00-11-22-00-00-01]{lang="EN-US"}

[    Sender Port: 0x0    Receiver Port: 0x0]{lang="EN-US"}

[    PType: 0x0 P Flag: 0x1     Sender Instance: 0x1]{lang="EN-US"}

[    Partition ID: 0x0     Receiver Instance: 0x5]{lang="EN-US"}

[    \# of Caps: 0x3     Total Length: 0xc]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1888526684}*[收到邻居]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[发送的一个]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jul 16 11:35:09:043 2013 Syaname ANCP/7/PACKET: -MDC=1; Received a(an) Port Up message from neighbor dslam1.]{lang="EN-US"}]{#struct_0_x6514_x1315_387833907}

[    Identifier: 0x880c     Length: 0xc0]{lang="EN-US"}

[    Version: 0x32     Message Type: 0x50]{lang="EN-US"}

[    Result: 0x0     Code: 0x0]{lang="EN-US"}

[    Partition ID: 0x0     Transaction ID: 0x0]{lang="EN-US"}

[    Length: 0xc0    \# of TLVs: 0x2     Extension Block length: 0x98]{lang="EN-US"}

[*[// DSLAM]{lang="EN-US"}*]{#struct_0_x6514_x1315_x1275718996}*[端开始上报线路信息。]{style="font-family:宋体"}[BARS]{lang="EN-US"}[端邻居名为]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[的邻居，收到一个]{style="font-family:宋体"}[Port Up]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
