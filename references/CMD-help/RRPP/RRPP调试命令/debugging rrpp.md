::: {#-1416934083 .myid}
[]{#_Toc215298276}[]{#_Toc404795675}[]{#struct_0_17107_11229_x1604327354}[]{#_Toc341775661}

**RRPP \-- RRPP调试命令 \-- debugging rrpp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17107_11229_x206698432}

[**[debugging]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17107_11229_1216583289}**[rrpp]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[domain]{lang="EN-US"}**[ ]{lang="EN-US"}*[domain-id ]{lang="EN-US"}*[\[ **ring** *ring-id* \] \] { **all** \| **error** \| **event** \| **fast-detect-fsm** \| **fast-detect-packet** \| **fsm** \| **packet** }]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17107_11229_x2107070791}**[debugging]{lang="EN-US"}**[ **rrpp** \[ ]{lang="EN-US"}**[domain]{lang="EN-US"}**[ ]{lang="EN-US"}*[domain-id ]{lang="EN-US"}*[\[ **ring** *ring-id* \] \] { **all** \| **error** \| **event** \| **fast-detect-fsm** \| **fast-detect-packet** \| **fsm** \| **packet** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17107_11229_x253664912}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17107_11229_x800186274}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17107_11229_748018192}

[[network-admin]{lang="EN-US"}]{#struct_0_17107_11229_2105672777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17107_11229_x1801245064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17107_11229_x1269335120}

[**[domain]{lang="EN-US"}**[ ]{lang="EN-US"}*[domain-id]{lang="EN-US"}*]{#struct_0_17107_11229_x178691845}[：指定]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域。]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域。]{style="font-family:宋体"}

[**[ring]{lang="EN-US"}**[ *ring-id*]{lang="EN-US"}]{#struct_0_17107_11229_x119828950}[：指定]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环。]{style="font-family:宋体"}*[ring-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_17107_11229_x2009565196}[：表示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17107_11229_601879373}[：表示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17107_11229_x558397239}[：表示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[fast-detect-fsm]{lang="EN-US"}**]{#struct_0_17107_11229_x1226784249}[：表示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[快速检测状态机调试信息开关。]{style="font-family:宋体"}

[**[fast-detect-packet]{lang="EN-US"}**]{#struct_0_17107_11229_x255798290}[：表示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[快速检测报文调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_17107_11229_2089916301}[：表示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_17107_11229_x896249122}[：表示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17107_11229_x623210578}

[**[debugging]{lang="EN-US"}**[ **rrpp**]{lang="EN-US"}]{#struct_0_17107_11229_x1779695440}[命令用来打开]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **rrpp**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_17107_11229_1582180153}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging rrpp error]{lang="EN-US"}]{#struct_0_17107_11229_x198674603}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1112190354}[[字段]{style="font-family:黑体"}]{#struct_0_17107_11229_1377106131}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17107_11229_x1998786423}

[[Failed to allocate memory.]{lang="EN-US"}]{#struct_0_17107_11229_126906851}

[[表示申请动态内存失败]{style="font-family:宋体"}]{#struct_0_17107_11229_1478209267}

[[Failed to allocate memory for realtime backup.]{lang="EN-US"}]{#struct_0_17107_11229_1854544856}

[[表示]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17107_11229_1657950719}[实时备份分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for batch backup.]{lang="EN-US"}]{#struct_0_17107_11229_942873363}

[[表示]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17107_11229_x1267421349}[批量备份分配内存失败]{style="font-family:宋体"}

[[Failed to send batch backup message.]{lang="EN-US"}]{#struct_0_17107_11229_14090691}

[[表示]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17107_11229_1975463328}[发送批量备份消息失败]{style="font-family:宋体"}

[[Failed to send realtime backup message.]{lang="EN-US"}]{#struct_0_17107_11229_x2009421536}

[[表示]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17107_11229_988706869}[发送实时备份消息失败]{style="font-family:宋体"}

[[Domain *domain* ring *ring* port *port* : Master node received Health packet from primary port.]{lang="EN-US"}]{#struct_0_17107_11229_x1716457431}

[[RRPP]{lang="FR"}]{#struct_0_17107_11229_x1073549272}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[上的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[收发报文错误，错误原因]{style="font-family:宋体"}[为主节点主端口收到本节点的]{style="font-family:宋体"}[Health]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received packet on port *port* error. Reason: *string*.]{lang="EN-US"}]{#struct_0_17107_11229_510871941}

[[端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_17107_11229_x1333646079}[收到错误报文，错误原因]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal RRPP packet ]{lang="EN-US"}]{#struct_0_17107_11229_x1594314998}[l]{lang="EN-US"}[ength]{lang="EN-US"}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[长度字段非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal RRPP version]{lang="EN-US"}]{#struct_0_17107_11229_518930062}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[版本号非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal RRPP PDU ]{lang="EN-US"}]{#struct_0_17107_11229_x696031597}[l]{lang="EN-US"}[ength]{lang="EN-US"}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[长度]{style="font-family:宋体"}[字段非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal domain ID]{lang="EN-US"}]{#struct_0_17107_11229_x229920610}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[nexistent domain]{lang="EN-US"}]{#struct_0_17107_11229_492534669}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文携带的域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[在]{style="font-family:宋体"}[本设备上]{lang="EN-US" style="font-family:宋体"}[并未]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ring is inactive]{lang="EN-US"}]{#struct_0_17107_11229_756168079}[：收]{lang="EN-US" style="font-family:
  宋体"}[到]{style="font-family:宋体"}[报文携带的域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[在本设备上]{lang="EN-US" style="font-family:宋体"}[已]{style="font-family:宋体"}[配置但]{lang="EN-US" style="font-family:宋体"}[未]{style="font-family:宋体"}[被激活，即该域下]{lang="EN-US" style="font-family:宋体"}[的环未被激活]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal level]{lang="EN-US"}]{#struct_0_17107_11229_449853720}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的级别]{style="font-family:宋体"}[非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal RRPP packet]{lang="EN-US"}]{#struct_0_17107_11229_x1820018584}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[报文类型非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}[acket receive]{lang="EN-US"}]{#struct_0_17107_11229_x1715459295}[d]{lang="EN-US"}[ from non-ctrlvlan]{lang="EN-US"}[：报文不是从指定域的控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[，即控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[不匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal ring ID]{lang="EN-US"}]{#struct_0_17107_11229_485935833}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[环]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}[ello time out of range]{lang="EN-US"}]{#struct_0_17107_11229_1271313604}[：报文中携带的]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器超出范围]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}[ail time out of range]{lang="EN-US"}]{#struct_0_17107_11229_x1429845168}[：报文中携带的]{lang="EN-US" style="font-family:宋体"}[Fail]{lang="EN-US"}[定时器超出范围]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fail time must be greater than or equal to three times of Hello time]{lang="EN-US"}]{#struct_0_17107_11229_x282377903}[：]{lang="EN-US" style="font-family:宋体"}[Fail]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}[必须大于等于]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}[的三倍]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Level mismatch]{lang="EN-US"}]{#struct_0_17107_11229_x1761303974}[：报文中携带的环的级别与设备该环的级别不匹配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}[ conflicting master node of current ring was detected]{lang="EN-US"}]{#struct_0_17107_11229_x1740213003}[：环上存在两个主节点（本条消息由主节点打印）]{lang="EN-US" style="font-family:宋体"}

[[Received fast-detect packet packet error. Reason: *string*.]{lang="EN-US"}]{#struct_0_17107_11229_1545835360}

[[收到快速检测错误报文，错误原因]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_17107_11229_x1840847614}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal domain ID]{lang="EN-US"}]{#struct_0_17107_11229_136238773}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[nexistent]{lang="EN-US"}]{#struct_0_17107_11229_x1913945041}[ ]{lang="EN-US"}[domain]{lang="EN-US"}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文携带的域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[不属于本设备上配置的域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal ring ID]{lang="EN-US"}]{#struct_0_17107_11229_x442358116}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[环]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inexistent ring]{lang="EN-US"}]{#struct_0_17107_11229_1573565894}[：收]{lang="EN-US" style="font-family:
  宋体"}[到]{style="font-family:宋体"}[报文携带的]{lang="EN-US" style="font-family:宋体"}[环]{style="font-family:宋体"}[ID]{lang="EN-US"}[不属于本设备上配置的对应域的环]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal level]{lang="EN-US"}]{#struct_0_17107_11229_x1451847109}[：]{lang="EN-US" style="font-family:宋体"}[收到]{style="font-family:宋体"}[报]{lang="EN-US" style="font-family:宋体"}[文的级别]{style="font-family:宋体"}[非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[llegal]{lang="EN-US"}]{#struct_0_17107_11229_1702322714}[ PDU type]{lang="EN-US"}[：收]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[报文类型非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}[acket receive]{lang="EN-US"}]{#struct_0_17107_11229_x126207275}[s ]{lang="EN-US"}[from non-ctrlvlan]{lang="EN-US"}[：报文不是从指定域的控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[收到]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[，即控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[不匹配]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging rrpp event]{lang="EN-US"}]{#struct_0_17107_11229_1714523156}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1114311422}[[字段]{style="font-family:黑体"}]{#struct_0_17107_11229_x901142869}

[[描述]{style="font-family:黑体"}]{#struct_0_17107_11229_2120026019}

[[Domain *domain* ring *ring* is activated/inactivated.]{lang="EN-US"}]{#struct_0_17107_11229_2098478634}

[[RRPP]{lang="FR"}]{#struct_0_17107_11229_x1099323429}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[被激活]{style="font-family:宋体"}[/]{lang="EN-US"}[解除激活]{style="font-family:宋体"}

[[Domain *domain* ring *ring* turns to fault for link down.]{lang="EN-US"}]{#struct_0_17107_11229_792313659}

[[由于链路]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_17107_11229_x1026560641}[，]{style="font-family:宋体"}[RRPP]{lang="FR"}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[出现故障]{style="font-family:宋体"}

[[Domain *domain* ring *ring* turns to fault for Link-Down packet.]{lang="EN-US"}]{#struct_0_17107_11229_1134311986}

[[由于收到]{style="font-family:宋体"}[Link-Down]{lang="EN-US"}]{#struct_0_17107_11229_x1123573605}[报文，]{style="font-family:宋体"}[RRPP]{lang="FR"}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[出现故障]{style="font-family:宋体"}

[[Domain *domain* ring *ring* turns to fault for fail-timer timeout.]{lang="EN-US"}]{#struct_0_17107_11229_1479380615}

[[由于主节点在]{style="font-family:宋体"}[Fail]{lang="EN-US"}]{#struct_0_17107_11229_1405236523}[定时器超时前未收到自身的]{style="font-family:宋体"}[Health]{lang="EN-US"}[报文，]{style="font-family:宋体"}[RRPP]{lang="FR"}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[出现故障]{style="font-family:宋体"}

[[Domain *domain* ring *ring* recovered for Health packet.]{lang="EN-US"}]{#struct_0_17107_11229_71044448}

[[主节点重新收到自身的]{style="font-family:宋体"}[Health]{lang="EN-US"}]{#struct_0_17107_11229_377284047}[报文，]{style="font-family:宋体"}[RRPP]{lang="FR"}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[恢复健康]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging rrpp fast-detect-fsm]{lang="EN-US"}]{#struct_0_17107_11229_x1235145961}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1107425192}[[字段]{style="font-family:黑体"}]{#struct_0_17107_11229_539523300}

[[描述]{style="font-family:黑体"}]{#struct_0_17107_11229_378464794}

[[Domain *domain* ring *ring* *string* ]{lang="EN-US"}]{#struct_0_17107_11229_x1994404602}[FSM]{lang="NO-BOK"}[.]{lang="EN-US"}

[[RRPP]{lang="FR"}]{#struct_0_17107_11229_833633446}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[的]{style="font-family:宋体"}*[string]{lang="EN-US"}*[状态机信息，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[RX]{lang="NO-BOK"}]{#struct_0_17107_11229_x643539813}[：表示接收状态机]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[TX]{lang="NO-BOK"}]{#struct_0_17107_11229_1071721120}[：表示发送状态机]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[RXTX]{lang="NO-BOK"}]{#struct_0_17107_11229_x81346547}[：表示同时为接收状态机和发送状态机]{style="font-family:宋体"}

[[Previous/Current state is *state*.]{lang="EN-US"}]{#struct_0_17107_11229_x1637666701}

[[状态机之前]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17107_11229_x1785315266}[当前的状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，包括]{style="font-family:宋体"}[Active]{lang="EN-US"}[、]{style="font-family:宋体"}[Completed]{lang="EN-US"}[、]{style="font-family:宋体"}[Failed]{lang="EN-US"}[和]{style="font-family:宋体"}[Idle]{lang="EN-US"}

[[Transition event: event.]{lang="EN-US"}]{#struct_0_17107_11229_2105607241}

[[迁移条件为]{style="font-family:宋体"}[event]{lang="EN-US"}]{#struct_0_17107_11229_543454592}[，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[Receiv]{lang="NO-BOK"}]{#struct_0_17107_11229_781565299}[ed]{lang="NO-BOK"}[ Fast-Detect packet]{lang="NO-BOK"}[：从主端口]{lang="EN-US" style="font-family:宋体"}[或副端口]{style="font-family:宋体"}[收到快速检测报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[FastFail]{lang="NO-BOK"}]{#struct_0_17107_11229_1834352954}[-]{lang="NO-BOK"}[Timer-Expired]{lang="NO-BOK"}[：]{lang="EN-US" style="font-family:宋体"}[Fast-Fail]{lang="NO-BOK"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[Detect-Enabled]{lang="NO-BOK"}]{#struct_0_17107_11229_x817693071}[：]{lang="EN-US" style="font-family:
  宋体"}[使能]{style="font-family:宋体"}[快速检测]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detect-Disabled]{lang="NO-BOK"}]{#struct_0_17107_11229_x1026657009}[：]{lang="EN-US" style="font-family:
  宋体"}[关闭]{style="font-family:宋体"}[快速检测]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging rrpp fast-detect-packet]{lang="EN-US"}]{#struct_0_17107_11229_217103679}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1110517534}[[字段]{style="font-family:黑体"}]{#struct_0_17107_11229_1252189217}

[[描述]{style="font-family:黑体"}]{#struct_0_17107_11229_x623276114}

[[Domain *domain* ring *ring* received fast-detect packet. (Length: *length*, count: *count*) *string*]{lang="EN-US"}]{#struct_0_17107_11229_599988096}

[[RRPP]{lang="FR"}]{#struct_0_17107_11229_700007999}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[收到了快速检测报文报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，报文计数为]{style="font-family:宋体"}*[count]{lang="EN-US"}*[，报文内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[[Domain *domain* ring *ring* sent fast-detect packet. (Length: *length*, count: *count*) *string*]{lang="EN-US"}]{#struct_0_17107_11229_x959962146}

[[RRPP]{lang="FR"}]{#struct_0_17107_11229_x840431180}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[发送了快速检测报文报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，报文计数为]{style="font-family:宋体"}*[count]{lang="EN-US"}*[，报文内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging rrpp fsm]{lang="EN-US"}]{#struct_0_17107_11229_159942129}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1109457210}[[字段]{style="font-family:黑体"}]{#struct_0_17107_11229_x1637424234}

[[描述]{style="font-family:黑体"}]{#struct_0_17107_11229_x1069348764}

[[Domain *domain* ring *ring* *string*]{lang="EN-US"}]{#struct_0_17107_11229_1623524838}[ FSM]{lang="NO-BOK"}[.]{lang="EN-US"}

[[RRPP]{lang="FR"}]{#struct_0_17107_11229_942807827}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[的]{style="font-family:宋体"}*[string]{lang="EN-US"}*[状态机信息，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="NO-BOK"}[aster Node]{lang="EN-US"}]{#struct_0_17107_11229_265418309}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[主节点状态机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit Node]{lang="EN-US"}]{#struct_0_17107_11229_684046950}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[传输节点状态机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Edge Node]{lang="EN-US"}]{#struct_0_17107_11229_x260358336}[：表示边缘节点状态机]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[Assistant-Edge ]{lang="NO-BOK"}[Node]{lang="EN-US"}]{#struct_0_17107_11229_53836814}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[辅助边缘节点状态机]{lang="EN-US" style="font-family:宋体"}

[[Previous/Current state is *state*.]{lang="EN-US"}]{#struct_0_17107_11229_1845484498}

[[状态机之前]{style="font-family:宋体"}]{#struct_0_17107_11229_x839225107}[/]{lang="NO-BOK"}[当前的状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，]{style="font-family:宋体"}[包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}[Completed]{lang="EN-US"}[、]{style="font-family:宋体"}[Failed]{lang="EN-US"}[、]{style="font-family:宋体"}[Init]{lang="EN-US"}[、]{style="font-family:宋体"}[Link-Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Link-Down]{lang="EN-US"}[、]{style="font-family:宋体"}[Preforwarding]{lang="EN-US"}[、]{style="font-family:宋体"}[Link-Up-Notify]{lang="EN-US"}[、]{style="font-family:宋体"}[Link-Down-Notify]{lang="EN-US"}[、]{style="font-family:宋体"}[Preforward-Notify]{lang="EN-US"}

[[Transition event: *event*.]{lang="EN-US"}]{#struct_0_17107_11229_54893290}

[[迁移条件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_17107_11229_x1073614808}[，包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ring-Enabled]{lang="EN-US"}]{#struct_0_17107_11229_x1803032984}[：]{lang="EN-US" style="font-family:宋体"}[环]{style="font-family:宋体"}[使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ring-Disabled]{lang="EN-US"}]{#struct_0_17107_11229_1811684284}[：]{lang="EN-US" style="font-family:宋体"}[环]{style="font-family:宋体"}[去使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fail-Timer-Expired]{lang="EN-US"}]{#struct_0_17107_11229_468506455}[：]{lang="EN-US" style="font-family:
  宋体"}[Fail]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Edge]{lang="EN-US"}]{#struct_0_17107_11229_x633391915}[F]{lang="EN-US"}[ail-Timer-Expired]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Edge-]{lang="EN-US"}[F]{lang="EN-US"}[ail]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiv]{lang="EN-US"}]{#struct_0_17107_11229_x1219596875}[ed]{lang="EN-US"}[ own Health packet]{lang="EN-US"}[：收到自己的]{lang="EN-US" style="font-family:宋体"}[Health]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiv]{lang="EN-US"}]{#struct_0_17107_11229_161206256}[ed]{lang="EN-US"}[ Link-Down packet]{lang="EN-US"}[：收到]{lang="EN-US" style="font-family:宋体"}[Link-Down]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiv]{lang="EN-US"}]{#struct_0_17107_11229_492469133}[ed]{lang="EN-US"}[ Common-Flush-FDB packet]{lang="EN-US"}[：收到]{lang="EN-US" style="font-family:宋体"}[Common-Flush-FDB]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiv]{lang="EN-US"}]{#struct_0_17107_11229_401970241}[ed]{lang="EN-US"}[ Complete-Flush-FDB packet]{lang="EN-US"}[：收到]{lang="EN-US" style="font-family:宋体"}[Complete-Flush-FDB]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiv]{lang="EN-US"}]{#struct_0_17107_11229_1013319504}[ed]{lang="EN-US"}[ Sub-Ring-FDB packet]{lang="EN-US"}[：收到]{lang="EN-US" style="font-family:宋体"}[Sub-Ring-FDB]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiv]{lang="EN-US"}]{#struct_0_17107_11229_x2138622587}[ed]{lang="EN-US"}[ Edge-Hello packet]{lang="EN-US"}[：收到]{lang="EN-US" style="font-family:宋体"}[Edge-Hello]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiv]{lang="EN-US"}]{#struct_0_17107_11229_x2066210020}[ed]{lang="EN-US"}[ Major-Fault packet]{lang="EN-US"}[：收到]{lang="EN-US" style="font-family:宋体"}[Major-Fault]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}[wn link down]{lang="EN-US"}]{#struct_0_17107_11229_1573274155}[：自身链路故障]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}[wn link restoring]{lang="EN-US"}]{#struct_0_17107_11229_461834169}[：自身链路恢复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}[ort join]{lang="EN-US"}]{#struct_0_17107_11229_x1429910704}[ed]{lang="EN-US"}[ lagg]{lang="EN-US"}[：端口加入聚合]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}[ort leave]{lang="EN-US"}]{#struct_0_17107_11229_x872104570}[d]{lang="EN-US"}[ lagg]{lang="EN-US"}[：端口离开聚合]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging rrpp packet]{lang="EN-US"}]{#struct_0_17107_11229_279368803}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1137714864}[[字段]{style="font-family:黑体"}]{#struct_0_17107_11229_x910514282}

[[描述]{style="font-family:黑体"}]{#struct_0_17107_11229_x1305369358}

[[Port *port* received packet from domain *domain* ring *ring*. (Length: *length*, type: *type*) *string*]{lang="EN-US"}]{#struct_0_17107_11229_547244710}

[[端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_17107_11229_x1297454194}[从]{style="font-family:宋体"}[RRPP]{lang="FR"}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[收到报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，报文类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[（取值为]{style="font-family:宋体"}[Health]{lang="FR"}[、]{style="font-family:宋体"}[Link-Down]{lang="FR"}[、]{style="font-family:宋体"}[Complete-Flush-FDB]{lang="FR"}[、]{style="font-family:宋体"}[Common-Flush-FDB]{lang="FR"}[、]{style="font-family:宋体"}[Edge-Hello]{lang="FR"}[或]{style="font-family:宋体"}[Major-Fault]{lang="FR"}[），报文内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[[Port *port* sent packet to domain *domain* ring *ring*. (Length: *length*, type: *type*) *string*]{lang="EN-US"}]{#struct_0_17107_11229_x527832624}

[[端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_17107_11229_136173237}[向]{style="font-family:宋体"}[RRPP]{lang="FR"}[域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[下的环]{style="font-family:宋体"}*[ring]{lang="FR"}*[发送报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，报文类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[（取值为]{style="font-family:宋体"}[Health]{lang="FR"}[、]{style="font-family:宋体"}[Link-Down]{lang="FR"}[、]{style="font-family:宋体"}[Complete-Flush-FDB]{lang="FR"}[、]{style="font-family:宋体"}[Common-Flush-FDB]{lang="FR"}[、]{style="font-family:宋体"}[Edge-Hello]{lang="FR"}[或]{style="font-family:宋体"}[Major-Fault]{lang="FR"}[），报文内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17107_11229_x1764082520}

[[\# ]{lang="EN-US"}]{#struct_0_17107_11229_1850411030}[在一个]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环上配置两个主节点，其它设备都配置成传输节点，所有设备的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议都使能，所有的环都使能。在其中一个主节点上打开]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[异常信息调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging rrpp error]{lang="EN-US"}]{#struct_0_17107_11229_x2033209357}

[\*Jan 2 05:08:27:501 2012 Sysname RRPP/7/Error: -MDC=1; Received packet on port GigabitEthernet1/0/1 error. Reason: A conflicting master node of current ring was detected.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17107_11229_1648115812}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到错误报文，错误原因为环上存在两个主节点]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17107_11229_1793582564}[两台设备组网，设备]{style="font-family:宋体"}[A]{lang="EN-US"}[配置为主环传输节点，使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环不使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议；设备]{style="font-family:宋体"}[B]{lang="EN-US"}[首先打开]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[事件调试信息开关，然后配置为主环主节点，使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环和]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> debugging rrpp event]{lang="EN-US"}]{#struct_0_17107_11229_1006792401}

[\*May  2 23:48:18:579 2012 Sysname RRPP/7/Event: -MDC=1; Domain 1 ring 1 is activated.]{lang="EN-US"}

[*[// RRPP]{lang="EN-US"}*]{#struct_0_17107_11229_x159499693}*[域]{style="font-family:宋体"}[1]{lang="EN-US"}[下的环]{style="font-family:宋体"}[1]{lang="EN-US"}[被激活]{style="font-family:宋体"}*

[[%May  2 23:52:47:650 2012 Sysname RRPP/7/Event: -MDC=1; Domain 1 ring 1 turns to fault for fail-timer timeout.]{lang="EN-US"}]{#struct_0_17107_11229_x609082675}

[*[// ]{lang="EN-US"}*]{#struct_0_17107_11229_x357300410}*[由于主节点在]{style="font-family:宋体"}[Fail]{lang="EN-US"}[定时器超时前未收到自身的]{style="font-family:宋体"}[Health]{lang="EN-US"}[报文，]{style="font-family:宋体"}[RRPP]{lang="FR"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[下的环]{style="font-family:宋体"}[1]{lang="FR"}[出现故障]{style="font-family:宋体"}*

[[\*Jan  2 05:29:35:393 2012 Sysname RRPP/7/Event: -MDC=1; Domain 1 ring 1 recovered for Health packet.]{lang="EN-US"}]{#struct_0_17107_11229_664007209}

[*[// ]{lang="EN-US"}*]{#struct_0_17107_11229_1605844257}*[使能设备]{style="font-family:宋体"}[A]{lang="EN-US"}[的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议，这时设备]{style="font-family:宋体"}[B]{lang="EN-US"}[就会打印环恢复事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17107_11229_1702257178}[配置主环主节点，定时器使用缺省值，主端口是]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，副端口是]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。打开]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging rrpp fsm]{lang="EN-US"}]{#struct_0_17107_11229_1006273023}

[\*Jan  2 05:29:35:293 2012 Sysname RRPP/7/Fsm: -MDC=1; Domain 1 ring 1 Master Node FSM. Previous state is Failed. Current state is Completed. Transition event: Received Link-Down packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17107_11229_1808904079}*[RRPP]{lang="FR"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[环]{style="font-family:宋体"}[1]{lang="EN-US"}[的主节点状态机信息。之前的状态为]{style="font-family:宋体"}[Failed]{lang="EN-US"}[，当前的状态为]{style="font-family:宋体"}[Completed]{lang="EN-US"}[，迁移条件为收到]{style="font-family:宋体"}[Link-Down]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17107_11229_x617482958}[配置主环主节点，定时器使用缺省值，主端口是]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，副端口是]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。打开]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging rrpp packet]{lang="EN-US"}]{#struct_0_17107_11229_x78583445}

[\*May  3 00:48:09:423 2012 Sysname RRPP/7/Pkt: -MDC=1; Port GigabitEthernet1/0/1 sent packet to domain 1 ring 1. (Length: 64, type: Health)]{lang="EN-US"}

[99 0b 00 40 01 05 00 01 00 01 00 00 00 00 00 00]{lang="EN-US"}

[01 11 00 01 00 03 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17107_11229_1476007894}*[主端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Health]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*May  3 00:48:09:423 2012 Sysname RRPP/7/Pkt: -MDC=1; Port GigabitEthernet1/0/2 received packet from domain 1 ring 1. (Length: 64, type: Health)]{lang="EN-US"}]{#struct_0_17107_11229_x1026626177}

[99 0b 00 40 01 05 00 01 00 01 00 00 00 00 00 00]{lang="EN-US"}

[01 11 00 01 00 03 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17107_11229_x1154022535}*[副端口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[收到本节点发出的]{style="font-family:宋体"}[Health]{lang="EN-US"}[报文]{style="font-family:宋体"}*
