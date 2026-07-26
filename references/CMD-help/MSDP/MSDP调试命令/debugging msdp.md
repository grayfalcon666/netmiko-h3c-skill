::: {#1298895960 .myid}
[]{#_Toc404789739}[]{#struct_0_x5826_19109_427982391}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**MSDP \-- MSDP调试命令 \-- debugging msdp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5826_19109_x419982536}

[**[debugging]{lang="EN-US"}**[ **msdp** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **connect** \| **event** \| **packet** \| **source-active** }]{lang="EN-US"}]{#struct_0_x5826_19109_x1631655477}

[**[undo]{lang="EN-US"}**[ **debugging** **msdp** \[ **vpn-instance** *vpn-instance-name* \] { **all** \| **connect** \| **event** \| **packet** \| **source-active** }]{lang="EN-US"}]{#struct_0_x5826_19109_23770546}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5826_19109_336544428}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5826_19109_x2006901198}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5826_19109_x110345300}

[[network-admin]{lang="EN-US"}]{#struct_0_x5826_19109_2093101069}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5826_19109_1635047210}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5826_19109_x2133149878}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x5826_19109_398664169}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x5826_19109_x1621761084}[：表示]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[connect]{lang="EN-US"}**]{#struct_0_x5826_19109_x1000175968}[：表示]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体连接调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x5826_19109_2084845439}[：表示]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x5826_19109_336478892}[：表示]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[source-active]{lang="EN-US"}**]{#struct_0_x5826_19109_x776755565}[：表示]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[活跃组播源调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x5826_19109_x1531289484}

[**[debugging msdp]{lang="EN-US"}**]{#struct_0_x5826_19109_980652151}[命令用来打开]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging msdp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_x5826_19109_x2005551605}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging msdp connect]{lang="EN-US"}]{#struct_0_x5826_19109_x1849936860}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1906533631}[[字段]{style="font-family:黑体"}]{#struct_0_x5826_19109_x222368019}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5826_19109_x350378544}

[[Failed to modify epoll for peer *peer* connect, close the socket.]{lang="EN-US"}]{#struct_0_x5826_19109_336413356}

[[更改对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1481025794}[连接的]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败，关闭]{style="font-family:宋体"}[socket]{lang="EN-US"}

[[Connected to peer *peer* successfully.]{lang="EN-US"}]{#struct_0_x5826_19109_541245040}

[[连接对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x16190299}[成功]{style="font-family:宋体"}

[[Accepted connection request from peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_768412392}

[[接受对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_197716271}[的连接成功]{style="font-family:宋体"}

[[Failed to accept connection request from peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_x539484641}

[[接受对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_336347820}[的连接失败]{style="font-family:宋体"}

[[Stopped listening for connection request from peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_x1432705290}

[[停止侦听对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1897219237}[的连接请求]{style="font-family:宋体"}

[[Failed to listen for connection request from peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_1000191892}

[[侦听对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_634886239}[的连接请求失败]{style="font-family:宋体"}

[[Stopped connection with peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_336806572}

[[关闭与对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1608815183}[的连接]{style="font-family:宋体"}

[[Failed to connect to peer *peer* (errcode: *errcode*).]{lang="EN-US"}]{#struct_0_x5826_19109_x771134992}

[[连接对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1495411618}[失败（错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Started a session with peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_x252099131}

[[开始与对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_265626083}[的会话]{style="font-family:宋体"}

[[Reset connection with peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_336741036}

[[重置与对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1411075024}[的连接]{style="font-family:宋体"}

[[Peer *peer* state changed from *state1* to *state2*.]{lang="EN-US"}]{#struct_0_x5826_19109_856318712}

[[对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1272668750}[的状态由]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[切换到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[，状态包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISABLED]{lang="EN-US"}]{#struct_0_x5826_19109_1671172421}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CONNECTING]{lang="EN-US"}]{#struct_0_x5826_19109_336675500}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_x5826_19109_x178744716}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_x5826_19109_316396815}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging msdp event]{lang="EN-US"}]{#struct_0_x5826_19109_1042195792}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1903828518}[[字段]{style="font-family:黑体"}]{#struct_0_x5826_19109_1498080735}

[[描述]{style="font-family:黑体"}]{#struct_0_x5826_19109_336609964}

[[Created *timer* timer for peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_x1739515127}

[[为对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1122670826}[创建]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[定时器，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}[onnectRetry]{lang="EN-US"}]{#struct_0_x5826_19109_x837019235}[：重连]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[session reconnection]{lang="EN-US"}]{#struct_0_x5826_19109_x189853203}[：会话重连]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA-]{lang="EN-US"}]{#struct_0_x5826_19109_1622921427}[R]{lang="EN-US"}[eponse]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[回应]{lang="EN-US" style="font-family:宋体"}

[[Created *timer* timer.]{lang="EN-US"}]{#struct_0_x5826_19109_979871573}

[[创建]{style="font-family:宋体"}*[timer]{lang="EN-US"}*]{#struct_0_x5826_19109_337068716}[定时器，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[memory ]{lang="EN-US"}]{#struct_0_x5826_19109_x1658227756}[threshold]{lang="EN-US"}[ recover]{lang="EN-US"}[：内存门限恢复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth end]{lang="EN-US"}]{#struct_0_x5826_19109_622498853}[：平滑结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth]{lang="EN-US"}]{#struct_0_x5826_19109_x1290814505}[：平滑]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[resend]{lang="EN-US"}]{#struct_0_x5826_19109_1983390242}[：重发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reconnect to MRIB]{lang="EN-US"}]{#struct_0_x5826_19109_x1311606895}[：重连]{style="font-family:宋体"}[MRIB]{lang="EN-US"}

[[Failed to create *timer* timer for peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_337003180}

[[为对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x413878294}[创建]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[定时器失败，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ConnectRetry]{lang="EN-US"}]{#struct_0_x5826_19109_1501263872}[：重连]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[session reconnection]{lang="EN-US"}]{#struct_0_x5826_19109_x206852205}[：会话重连]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA-]{lang="EN-US"}]{#struct_0_x5826_19109_x676198224}[R]{lang="EN-US"}[eponse]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[回应]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA batch advertise]{lang="EN-US"}]{#struct_0_x5826_19109_336544425}[ment]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[批量通告]{lang="EN-US" style="font-family:宋体"}

[[Failed to create *timer* timer.]{lang="EN-US"}]{#struct_0_x5826_19109_x2006901187}

[[创建]{style="font-family:宋体"}*[timer]{lang="EN-US"}*]{#struct_0_x5826_19109_x63356669}[定时器失败，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA advertisement]{lang="EN-US"}]{#struct_0_x5826_19109_329120068}[：]{lang="EN-US" style="font-family:
  宋体"}[SA]{lang="EN-US"}[通告]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface reconnect]{lang="EN-US"}]{#struct_0_x5826_19109_x726446095}[ion]{lang="EN-US"}[：接口重连]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA batch advertisement]{lang="EN-US"}]{#struct_0_x5826_19109_336478889}[：]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[批量通告]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[memory ]{lang="EN-US"}]{#struct_0_x5826_19109_1179559566}[threshold]{lang="EN-US"}[ recover]{lang="EN-US"}[：内存门限恢复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth end]{lang="EN-US"}]{#struct_0_x5826_19109_x21423381}[：平滑结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth]{lang="EN-US"}]{#struct_0_x5826_19109_28603433}[：平滑]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[resend]{lang="EN-US"}]{#struct_0_x5826_19109_336413353}[：重发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reconnect to MRIB]{lang="EN-US"}]{#struct_0_x5826_19109_1481025791}[：]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[重连]{lang="EN-US" style="font-family:宋体"}

[[Deleted *timer* timer for peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_541441648}

[[为对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1359880749}[删除]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[定时器，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ConnectRetry]{lang="EN-US"}]{#struct_0_x5826_19109_336347817}[：重连]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Keepalive]{lang="EN-US"}]{#struct_0_x5826_19109_905946871}[：保活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hold]{lang="EN-US"}]{#struct_0_x5826_19109_x1579252}[：保持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[session reconnection]{lang="EN-US"}]{#struct_0_x5826_19109_230673610}[：会话重连]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA-Reponse]{lang="EN-US"}]{#struct_0_x5826_19109_x897777536}[：]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[回应]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA batch advertisement]{lang="EN-US"}]{#struct_0_x5826_19109_336806569}[：]{style="font-family:宋体"}[SA]{lang="EN-US"}[批量通告]{style="font-family:宋体"}

[[Deleted *timer* timer.]{lang="EN-US"}]{#struct_0_x5826_19109_x729836968}

[[删除]{style="font-family:宋体"}*[timer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1262610269}[定时器，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth end]{lang="EN-US"}]{#struct_0_x5826_19109_1981167240}[：平滑结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth]{lang="EN-US"}]{#struct_0_x5826_19109_336741033}[：平滑]{lang="EN-US" style="font-family:宋体"}

[[Peer *peer*'s *timer* timer expired.]{lang="EN-US"}]{#struct_0_x5826_19109_1411075019}

[[对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_855597813}[的]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[定时器超时，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ConnectRetry]{lang="EN-US"}]{#struct_0_x5826_19109_x956570469}[：重连]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Keepalive]{lang="EN-US"}]{#struct_0_x5826_19109_336675497}[：保活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hold]{lang="EN-US"}]{#struct_0_x5826_19109_x2098324004}[：保持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[session reconnection]{lang="EN-US"}]{#struct_0_x5826_19109_1936548237}[：会话重连]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA-Response]{lang="EN-US"}]{#struct_0_x5826_19109_336609961}[：]{style="font-family:宋体"}[SA]{lang="EN-US"}[回应]{style="font-family:宋体"}

[*[Timer]{lang="EN-US"}*[ timer expired.]{lang="EN-US"}]{#struct_0_x5826_19109_x1739515124}

[*[Timer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1525955353}[定时器超时，]{style="font-family:宋体"}*[Timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="EN-US"}[emory ]{lang="EN-US"}]{#struct_0_x5826_19109_861091822}[threshold]{lang="EN-US"}[ recover]{lang="EN-US"}[：内存门限恢复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[mooth end]{lang="EN-US"}]{#struct_0_x5826_19109_337068713}[：平滑结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[mooth]{lang="EN-US"}]{#struct_0_x5826_19109_x1658227761}[：平滑]{lang="EN-US" style="font-family:宋体"}

[[Failed to set/reset password for peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_x1750088606}

[[为对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_337003177}[设置]{style="font-family:宋体"}[/]{lang="EN-US"}[清除密码失败]{style="font-family:宋体"}

[[Failed to recover original-rp/peer configuration for interface *name* from DBM.]{lang="EN-US"}]{#struct_0_x5826_19109_x1987856413}

[[为接口]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x5826_19109_183826529}[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}[恢复]{style="font-family:宋体"}[original-rp/peer]{lang="EN-US"}[的配置失败]{style="font-family:宋体"}

[[Failed to cache (*source*, *group*).]{lang="EN-US"}]{#struct_0_x5826_19109_1221381709}

[[缓存（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_x5826_19109_336544426}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）失败]{style="font-family:宋体"}

[[Failed to save original-rp/peer/global/static-rpf-peer configuration to DBM.]{lang="EN-US"}]{#struct_0_x5826_19109_x2006901188}

[[将]{style="font-family:宋体"}[original-rp/peer/global/static-rpf-peer]{lang="EN-US"}]{#struct_0_x5826_19109_x110410836}[的配置保存到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to process HA upgrade event.]{lang="EN-US"}]{#struct_0_x5826_19109_336478890}

[[处理]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x5826_19109_x776755563}[的升级事件失败]{style="font-family:宋体"}

[[Failed to recover cofiguration from DBM.]{lang="EN-US"}]{#struct_0_x5826_19109_x1531158412}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x5826_19109_336413354}[恢复配置失败]{style="font-family:宋体"}

[[Failed to enable redirecting TCP packets to CPU.]{lang="EN-US"}]{#struct_0_x5826_19109_1481025792}

[[使能]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x5826_19109_541638256}[报文上报]{style="font-family:宋体"}[CPU]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to notify main thread to processing multicast enable/disable message.]{lang="EN-US"}]{#struct_0_x5826_19109_336347818}

[[通知主线程处理组播使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5826_19109_905946862}[关闭消息失败]{style="font-family:宋体"}

[[Failed to notify main thread to processing message.]{lang="EN-US"}]{#struct_0_x5826_19109_x1957894385}

[[通知主线程处理报文失败]{style="font-family:宋体"}]{#struct_0_x5826_19109_336806570}

[[Failed to connect to MRIB.]{lang="EN-US"}]{#struct_0_x5826_19109_1608815185}

[[连接]{style="font-family:宋体"}[MRIB]{lang="EN-US"}]{#struct_0_x5826_19109_x771266064}[失败]{style="font-family:宋体"}

[[Failed to resend message to MRIB.]{lang="EN-US"}]{#struct_0_x5826_19109_336741034}

[[向]{style="font-family:宋体"}[MRIB]{lang="EN-US"}]{#struct_0_x5826_19109_1411075026}[重发消息失败]{style="font-family:宋体"}

[[Failed to read message from socket (errcode: *errcode*).]{lang="EN-US"}]{#struct_0_x5826_19109_856187640}

[[从]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x5826_19109_336675498}[读取数据失败（错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Failed to set fd limit(errno: *errcode*).]{lang="EN-US"}]{#struct_0_x5826_19109_x2098324015}

[[设置进程]{style="font-family:宋体"}[FD]{lang="EN-US"}]{#struct_0_x5826_19109_x792269582}[上限失败（错误码为]{style="font-family:宋体"}[errcode]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Failed to notify work thread to originate SA adv message.]{lang="EN-US"}]{#struct_0_x5826_19109_336609962}

[[通知工作线程生成]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x5826_19109_x1739515125}[通告消息失败]{style="font-family:宋体"}

[[Failed to notify work thread to processing exit message.]{lang="EN-US"}]{#struct_0_x5826_19109_40128588}

[[通知工作线程处理退出的消息失败]{style="font-family:宋体"}]{#struct_0_x5826_19109_337068714}

[[Refreshed *timer* timer of peer *peer* to *n* seconds.]{lang="EN-US"}]{#struct_0_x5826_19109_x1658227758}

[[刷新对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_337003178}[的]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[定时器为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Keepalive]{lang="EN-US"}]{#struct_0_x5826_19109_x1987856398}[：保活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hold]{lang="EN-US"}]{#struct_0_x5826_19109_2106665125}[：]{lang="EN-US" style="font-family:宋体"}[保持]{style="font-family:宋体"}

[[Refreshed SA cache timer of (*source*, *group*) to *n* seconds.]{lang="EN-US"}]{#struct_0_x5826_19109_336544423}

[[刷新]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x5826_19109_x2006901193}[缓冲（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的缓冲定时器为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Received HA *event* event.]{lang="EN-US"}]{#struct_0_x5826_19109_336478887}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x5826_19109_1179559576}[的]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stop]{lang="EN-US"}]{#struct_0_x5826_19109_x21423380}[：停止]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[upgrade]{lang="EN-US"}]{#struct_0_x5826_19109_336413351}[：升级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[degrade]{lang="EN-US"}]{#struct_0_x5826_19109_1481025789}[：降级]{lang="EN-US" style="font-family:宋体"}

[[Received socket *n* *event* event.]{lang="EN-US"}]{#struct_0_x5826_19109_336347815}

[[收到]{style="font-family:宋体"}[socket *n*]{lang="EN-US"}]{#struct_0_x5826_19109_905946873}[的]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x5826_19109_336806567}[RROR]{lang="EN-US"}[/HU]{lang="EN-US"}[P]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IN]{lang="EN-US"}]{#struct_0_x5826_19109_x729836982}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OUT]{lang="EN-US"}]{#struct_0_x5826_19109_x1263003475}

[[Received *event* from MRIB.]{lang="EN-US"}]{#struct_0_x5826_19109_336741031}

[[从]{style="font-family:宋体"}[MRIB]{lang="EN-US"}]{#struct_0_x5826_19109_1411075021}[收到]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth start]{lang="EN-US"}]{#struct_0_x5826_19109_336675495}[：平滑开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[connection up]{lang="EN-US"}]{#struct_0_x5826_19109_x2098324002}[：连接]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[connection down]{lang="EN-US"}]{#struct_0_x5826_19109_336609959}[：连接]{lang="EN-US" style="font-family:
  宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enable-]{lang="EN-US"}[multicast notif]{lang="EN-US"}]{#struct_0_x5826_19109_216800020}[ication]{lang="EN-US"}[：]{style="font-family:宋体"}[组播使能通知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disable-]{lang="EN-US"}[multicast notif]{lang="EN-US"}]{#struct_0_x5826_19109_x586266805}[ication]{lang="EN-US"}[：]{style="font-family:宋体"}[组播关闭通知]{lang="EN-US" style="font-family:宋体"}

[[Received address event *event* on interface *name*.]{lang="EN-US"}]{#struct_0_x5826_19109_337068711}

[[收到接口]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x5826_19109_x1658227763}[的地址事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_x5826_19109_337003175}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d]{lang="EN-US"}[elete]{lang="EN-US"}]{#struct_0_x5826_19109_x1987856411}

[[Received *event* event on interface *name*.]{lang="EN-US"}]{#struct_0_x5826_19109_336544424}

[[收到接口]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x5826_19109_x2006901186}[的]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_x5826_19109_336478888}[：]{style="font-family:宋体"}[添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_x5826_19109_1179559565}[：]{style="font-family:宋体"}[删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unbind]{lang="EN-US"}]{#struct_0_x5826_19109_336413352}[：去绑定]{style="font-family:宋体"}[VPN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[insert]{lang="EN-US"}]{#struct_0_x5826_19109_1481025790}[：]{style="font-family:宋体"}[插入]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[extract]{lang="EN-US"}]{#struct_0_x5826_19109_336347816}[：]{style="font-family:宋体"}[拔出]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP to DOWN]{lang="EN-US"}]{#struct_0_x5826_19109_905946872}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN to UP]{lang="EN-US"}]{#struct_0_x5826_19109_336806568}

[[Received local source (*source*, *group*) add event with *n* bytes data.]{lang="EN-US"}]{#struct_0_x5826_19109_x729836967}

[[收到本地源（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[, *group*]{lang="EN-US"}]{#struct_0_x5826_19109_336741032}[）添加事件，同时带有]{style="font-family:宋体"}*[n]{lang="EN-US"}[字节的组播数据]{style="font-family:宋体"}*

[[Droped local source (*source*, *group*) data for exceed max data length *n.*]{lang="EN-US"}]{#struct_0_x5826_19109_1411075020}

[[由于携带数据的长度超过了最大数据长度]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x5826_19109_336675496}[，将本地源（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[, *group*]{lang="EN-US"}[）的数据丢弃]{style="font-family:宋体"}

[[Droped local source (*source*, *group*) for exceed work thread queue limit.]{lang="EN-US"}]{#struct_0_x5826_19109_x2098324005}

[[由于超过了工作线程队列长度的限制，将本地源（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[, *group*]{lang="EN-US"}]{#struct_0_x5826_19109_336609960}[）丢弃]{style="font-family:宋体"}

[[Left *n* bytes message to resend.]{lang="EN-US"}]{#struct_0_x5826_19109_x1739515123}

[[剩余]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x5826_19109_337068712}[字节的消息需要重发]{style="font-family:宋体"}

[[Left *n* bytes message to drop from socket.]{lang="EN-US"}]{#struct_0_x5826_19109_x1658227760}

[[需要从]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x5826_19109_337003176}[丢弃]{style="font-family:宋体"}*[n]{lang="EN-US"}*[字节的消息]{style="font-family:宋体"}

[[Processed HA stop event successfully.]{lang="EN-US"}]{#struct_0_x5826_19109_x1987856412}

[[处理]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x5826_19109_1902628368}[的停止事件成功]{style="font-family:宋体"}

[[Tried to enable/disable peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_x1204893574}

[[尝试使能]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5826_19109_1902562832}[关闭对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*

[[Shutdown peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_1606629904}

[[手工]{style="font-family:宋体"}[shutdown]{lang="EN-US"}]{#struct_0_x5826_19109_1902497296}[对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*

[[Read *n* bytes message from socket.]{lang="EN-US"}]{#struct_0_x5826_19109_1902431760}

[[从]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x5826_19109_404592639}[读取]{style="font-family:宋体"}*[n]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[[Connection has been closed, restart peer connection.]{lang="EN-US"}]{#struct_0_x5826_19109_1902890512}

[[连接已经关闭，重新启动对等体的连接]{style="font-family:宋体"}]{#struct_0_x5826_19109_1601446625}

[[Can\'t forward (*source*, *group*) entry because the same entry had been forwarded within 30 seconds.]{lang="EN-US"}]{#struct_0_x5826_19109_1902824976}

[[不能转发（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[, *group*]{lang="EN-US"}]{#struct_0_x5826_19109_1902759440}[）表项，因为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒内转发过相同的表项]{style="font-family:宋体"}

[[Failed to connect to MBGP, creating reconnection timer]{lang="EN-US"}]{#struct_0_x5826_19109_x1297223997}

[[连接]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_x1655896974}[失败，创建重连定时器]{style="font-family:宋体"}

[[Failed to create reconnection timer for MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_x1297289533}

[[创建重连]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_633180016}[定时器失败]{style="font-family:宋体"}

[[Startup reconnect to MBGP timer]{lang="EN-US"}]{#struct_0_x5826_19109_x1296699710}

[[启动重连]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_1504872639}[定时器]{style="font-family:宋体"}

[[Failed to startup reconnection to MBGP timer]{lang="EN-US"}]{#struct_0_x5826_19109_x1296765246}

[[启动重连]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_2069935197}[定时器失败]{style="font-family:宋体"}

[[Stop reconnect to MBGP timer]{lang="EN-US"}]{#struct_0_x5826_19109_x1296830782}

[[停止重连]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_x756284665}[定时器]{style="font-family:宋体"}

[[Reconnect to MBGP timer expired]{lang="EN-US"}]{#struct_0_x5826_19109_x1296896318}

[[重连]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_x1241829997}[定时器超时]{style="font-family:宋体"}

[[Startup age MBGP timer]{lang="EN-US"}]{#struct_0_x5826_19109_x1296437566}

[[启动老化]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_1978717557}[数据定时器]{style="font-family:宋体"}

[[Stop age MBGP timer]{lang="EN-US"}]{#struct_0_x5826_19109_x1296503102}

[[停止老化]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_980206676}[数据定时器]{style="font-family:宋体"}

[[Age MBGP timer expired]{lang="EN-US"}]{#struct_0_x5826_19109_x1296568638}

[[老化]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_1844396655}[数据定时器超时]{style="font-family:宋体"}

[[Receive connection close from MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_x1296634174}

[[收到]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_x1014382937}[通知的连接关闭消息]{style="font-family:宋体"}

[[Register to MBGP error: *errcode*]{lang="EN-US"}]{#struct_0_x5826_19109_x1297223998}

[[向]{style="font-family:宋体"}[MBGP]{lang="EN-US"}]{#struct_0_x5826_19109_1523325075}[注册失败（错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging msdp packet]{lang="EN-US"}]{#struct_0_x5826_19109_x1971045120}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1921066940}[[字段]{style="font-family:黑体"}]{#struct_0_x5826_19109_321332859}

[[描述]{style="font-family:黑体"}]{#struct_0_x5826_19109_450994467}

[[Received SA/SA-Response message from peer *peer* can\'t pass import.]{lang="EN-US"}]{#struct_0_x5826_19109_x1201479672}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1648681551}[收到的]{style="font-family:宋体"}[SA/SA-Response]{lang="EN-US"}[不能通过入策略]{style="font-family:宋体"}

[[Received (*source*, *group*) from peer *peer* can\'t pass import ACL.]{lang="EN-US"}]{#struct_0_x5826_19109_x152651733}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x535658963}[收到的]{style="font-family:宋体"}[SA/SA-Response]{lang="EN-US"}[报文中的（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）不能通过入方向的]{style="font-family:宋体"}[ACL]{lang="EN-US"}

[[Received group *group* from peer *peer* is in SSM range.]{lang="EN-US"}]{#struct_0_x5826_19109_1902693904}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1891979507}[收到的]{style="font-family:宋体"}[SA/SA-Response]{lang="EN-US"}[中包含的组地址]{style="font-family:宋体"}*[group]{lang="EN-US"}*[在]{style="font-family:宋体"}[SSM]{lang="EN-US"}[范围]{style="font-family:宋体"}

[[Received SA/SA-Response message from peer *peer* with illegal RP(0.0.0.0).]{lang="EN-US"}]{#struct_0_x5826_19109_1946593987}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1921003872}[收到的]{style="font-family:宋体"}[SA/SA-Response]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[RP]{lang="EN-US"}[是非法的]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Received SA/SA-Response message from peer *peer* with local RP.]{lang="EN-US"}]{#struct_0_x5826_19109_1047346197}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1063942064}[收到的]{style="font-family:宋体"}[SA/SA-Response]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[RP]{lang="EN-US"}[是本地的]{style="font-family:宋体"}[RP]{lang="EN-US"}

[[Received SA-Request packet from peer *peer* can\'t pass request policy.]{lang="EN-US"}]{#struct_0_x5826_19109_1903152656}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_6896282}[收到的]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文不能通过请求策略]{style="font-family:宋体"}

[[Received SA/SA-Response message from peer *peer* with illegal RP/source/group address (*address*).]{lang="EN-US"}]{#struct_0_x5826_19109_1980391123}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1208554446}[收到的]{style="font-family:宋体"}[SA/SA-Response]{lang="EN-US"}[报文的]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[组地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*[非法]{style="font-family:宋体"}

[[Received SA/SA-Response message from peer *peer* with illegal mask length (*length*).]{lang="EN-US"}]{#struct_0_x5826_19109_1523045218}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1903087120}[收到的]{style="font-family:宋体"}[SA/SA-Response]{lang="EN-US"}[报文的地址掩码长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[非法]{style="font-family:宋体"}

[[Received *message* message from peer *peer* with illegal length (*length*).]{lang="EN-US"}]{#struct_0_x5826_19109_x1932623427}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_664969375}[收到的]{style="font-family:宋体"}*[message]{lang="EN-US"}*[报文的长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[非法，]{style="font-family:宋体"}*[message]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA]{lang="EN-US"}]{#struct_0_x5826_19109_x526077814}[：]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA-Request]{lang="EN-US"}]{#struct_0_x5826_19109_x476083239}[：]{style="font-family:宋体"}[SA-]{lang="EN-US"}[Request]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SA-Response]{lang="EN-US"}]{#struct_0_x5826_19109_1902628369}[：]{style="font-family:宋体"}[SA-Response]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Keepalive]{lang="EN-US"}]{#struct_0_x5826_19109_x1204828038}[：保活报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Notification]{lang="EN-US"}]{#struct_0_x5826_19109_x692578201}[：通告报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}[raceroute in progress]{lang="EN-US"}]{#struct_0_x5826_19109_x1105559251}[：路由回溯请求]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}[raceroute reply]{lang="EN-US"}]{#struct_0_x5826_19109_319451427}[：路由回溯回应]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nknown]{lang="EN-US"}]{#struct_0_x5826_19109_1902562833}[：未知类型]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}

[[Received SA/SA-Response message from peer *peer* with illegal entry count (*count*).]{lang="EN-US"}]{#struct_0_x5826_19109_1606695440}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1336634026}[收到的]{style="font-family:宋体"}[SA/SA-Response]{lang="EN-US"}[报文的表项数量]{style="font-family:宋体"}*[count]{lang="EN-US"}*[非法]{style="font-family:宋体"}

[[Received SA message from peer *peer* with illegal data.]{lang="EN-US"}]{#struct_0_x5826_19109_x1409400213}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_885731581}[收到的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的数据非法]{style="font-family:宋体"}

[[Received SA-Request message packet from peer *peer* for group *group*.]{lang="EN-US"}]{#struct_0_x5826_19109_1902497297}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_6717758}[收到组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Received SA-Request message from peer *peer* for group *group* can\'t pass request policy.]{lang="EN-US"}]{#struct_0_x5826_19109_1043700052}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x58440838}[收到组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文不能通过请求策略]{style="font-family:宋体"}

[[Received *message* message from peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_1902431761}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_404527103}[收到]{style="font-family:宋体"}*[message]{lang="EN-US"}*[报文，]{style="font-family:宋体"}*[message]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Notification]{lang="EN-US"}]{#struct_0_x5826_19109_x1370577997}[ ]{lang="EN-US"}[(]{lang="EN-US"}[openbit: *openbit*]{lang="EN-US"}[, ]{lang="EN-US"}[e]{lang="EN-US"}[rr]{lang="EN-US"}[c]{lang="EN-US"}[ode: ]{lang="EN-US"}*[e]{lang="EN-US"}[rr]{lang="EN-US"}[c]{lang="EN-US"}[ode]{lang="EN-US"}*[, ]{lang="EN-US"}[s]{lang="EN-US"}[ub]{lang="EN-US"}[e]{lang="EN-US"}[rr]{lang="EN-US"}[c]{lang="EN-US"}[ode: ]{lang="EN-US"}*[s]{lang="EN-US"}[ub]{lang="EN-US"}[e]{lang="EN-US"}[rr]{lang="EN-US"}[c]{lang="EN-US"}[ode]{lang="EN-US"}*[)]{lang="EN-US"}[：通告报文（]{lang="EN-US" style="font-family:宋体"}[openbit]{lang="EN-US"}[为]{style="font-family:宋体"}*[openbit]{lang="EN-US"}*[/]{lang="EN-US"}[错误码]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:宋体"}*[e]{lang="EN-US"}[rr]{lang="EN-US"}[c]{lang="EN-US"}[ode]{lang="EN-US"}*[/]{lang="EN-US"}[子错误码]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:宋体"}*[s]{lang="EN-US"}[ub]{lang="EN-US"}[e]{lang="EN-US"}[rr]{lang="EN-US"}[c]{lang="EN-US"}[ode]{lang="EN-US"}*[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unknown]{lang="EN-US"}]{#struct_0_x5826_19109_1686565210}[ ]{lang="EN-US"}[(]{lang="EN-US"}*[code]{lang="EN-US"}*[)]{lang="EN-US"}[：未知类型]{lang="EN-US" style="font-family:宋体"}[（类型码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[traceroute in progress]{lang="EN-US"}]{#struct_0_x5826_19109_1902890513}[：路由回溯请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[traceroute reply]{lang="EN-US"}]{#struct_0_x5826_19109_1601381089}[：路由回溯回应]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Keepalive]{lang="EN-US"}]{#struct_0_x5826_19109_x1779918689}[：保活]{lang="EN-US" style="font-family:宋体"}

[[Sent SA message to peer *peer*, can\'t pass export policy.]{lang="EN-US"}]{#struct_0_x5826_19109_1902824977}

[[发送的]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x5826_19109_x1147800237}[报文不能通过出策略]{style="font-family:宋体"}

[[Sent SA message to peer *peer*, (*source*, *group*) can\'t pass export policy.]{lang="EN-US"}]{#struct_0_x5826_19109_x583180212}

[[发送的]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x5826_19109_x2135735195}[报文中的（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）不能通过出策略]{style="font-family:宋体"}

[[Sent SA-Request message to peer *peer* for group *group*.]{lang="EN-US"}]{#struct_0_x5826_19109_1902759441}

[[向对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1971110656}[发送组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Sent Keepalive message to peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_x266686581}

[[向对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1902693905}[发送保活报文]{style="font-family:宋体"}

[[Sent Notification(openbit: *openbit*, errcode: *errcode*, suberrcode: *suberrcode*) message to peer *peer.*]{lang="EN-US"}]{#struct_0_x5826_19109_x1892045043}

[[向对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1497489984}[发送通告报文（]{style="font-family:宋体"}[openbit]{lang="EN-US"}[为]{style="font-family:宋体"}*[openbit]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[，子错误码为]{style="font-family:宋体"}*[suberrcode]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Sent *n* bytes SA message to peer *peer*.]{lang="EN-US"}]{#struct_0_x5826_19109_1795852431}

[[向对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1903152657}[发送]{style="font-family:宋体"}*[n]{lang="EN-US"}*[字节的报文]{style="font-family:宋体"}

[[Discarded SA message send to peer *peer* due to TTL *n* less than min-TTL *m*.]{lang="EN-US"}]{#struct_0_x5826_19109_6830746}

[[向对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x1660282052}[发送的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文由于]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}*[n]{lang="EN-US"}*[小于]{style="font-family:宋体"}[TTL]{lang="EN-US"}[下限值]{style="font-family:宋体"}*[m]{lang="EN-US"}*[而被丢弃]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging msdp source-active]{lang="EN-US"}]{#struct_0_x5826_19109_x1358567478}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1920565169}[[字段]{style="font-family:黑体"}]{#struct_0_x5826_19109_1903087121}

[[描述]{style="font-family:黑体"}]{#struct_0_x5826_19109_x1932557891}

[[RPF check on received SA message from peer *peer* failed.]{lang="EN-US"}]{#struct_0_x5826_19109_x566555038}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x323065812}[收到的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文]{style="font-family:宋体"}[RPF]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

[[Received SA message from peer *peer* with *n* bytes data (RP: *rp*, len: *length*, count: *count*).]{lang="EN-US"}]{#struct_0_x5826_19109_x1250385246}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_x142354788}[收到携带]{style="font-family:宋体"}*[n]{lang="EN-US"}*[字节数据的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文（]{style="font-family:宋体"}[RP]{lang="EN-US"}[的地址为]{style="font-family:宋体"}*[rp]{lang="EN-US"}*[，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，数量为]{style="font-family:宋体"}*[count]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received SA-Response message from peer *peer* (RP: *rp*, len: *length*, count: *count*).]{lang="EN-US"}]{#struct_0_x5826_19109_x1435877751}

[[从对等体]{style="font-family:宋体"}*[peer]{lang="EN-US"}*]{#struct_0_x5826_19109_1902628366}[收到]{style="font-family:宋体"}[SA-Response]{lang="EN-US"}[报文（]{style="font-family:宋体"}[RP]{lang="EN-US"}[的地址为]{style="font-family:宋体"}*[rp]{lang="EN-US"}*[，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，数量为]{style="font-family:宋体"}*[count]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[RPF check passed for *rp* (*reason*)]{lang="EN-US"}]{#struct_0_x5826_19109_269646380}

[[RP]{lang="EN-US"}]{#struct_0_x5826_19109_x1723339042}[地址为]{style="font-family:宋体"}*[rp]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[检查通过，原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[，]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer is the only established peer]{lang="EN-US"}]{#struct_0_x5826_19109_x1721505056}[：收到报文的对等体是唯一处于]{style="font-family:宋体"}[Established]{lang="EN-US"}[状态的对等体]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer is in the mesh-group]{lang="EN-US"}]{#struct_0_x5826_19109_1285024151}[：收到报文的对等体属于全连接组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer is the RP]{lang="EN-US"}]{#struct_0_x5826_19109_269580844}[：收到报文的对等体就是]{style="font-family:宋体"}[RP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer is MBGP nexthop]{lang="EN-US"}]{#struct_0_x5826_19109_314418663}[：收到报文的对等体是]{style="font-family:宋体"}[MBGP]{lang="EN-US"}[路由的下一跳]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer is BGP nexthop]{lang="EN-US"}]{#struct_0_x5826_19109_384139158}[：收到报文的对等体是]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的下一跳]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer is IGP nexthop]{lang="EN-US"}]{#struct_0_x5826_19109_x182472810}[：收到报文的对等体是]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由的下一跳]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer with the highest IP address in AS]{lang="EN-US"}]{#struct_0_x5826_19109_269515308}[：收到报文的对等体是]{style="font-family:宋体"}[AS]{lang="EN-US"}[中]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址最大的对等体]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Peer is a static RPF-peer]{lang="EN-US"}]{#struct_0_x5826_19109_320073217}[：收到报文的对等体是静态]{lang="EN-US" style="font-family:宋体"}[RPF]{lang="EN-US"}[对等体]{lang="EN-US" style="font-family:宋体"}

[[RPF check failed for *rp* (*reason*: *rpf-peer*)]{lang="EN-US"}]{#struct_0_x5826_19109_491008600}

[[RP]{lang="EN-US"}]{#struct_0_x5826_19109_x2067539624}[地址为]{style="font-family:宋体"}*[rp]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[检查不通过，原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[（所包含内容同上），]{style="font-family:宋体"}[RPF]{lang="EN-US"}[对等体的地址为]{style="font-family:宋体"}*[rpf-peer]{lang="EN-US"}*

[[RPF check failed for *rp*]{lang="EN-US"}]{#struct_0_x5826_19109_269449772}

[[RP]{lang="EN-US"}]{#struct_0_x5826_19109_261734728}[地址为]{style="font-family:宋体"}*[rp]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[检查不通过，且不存在任何]{style="font-family:宋体"}[RPF]{lang="EN-US"}[对等体]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5826_19109_x1205548934}

[[\# ]{lang="EN-US"}]{#struct_0_x5826_19109_x1456316493}[使能]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体连接调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging msdp connect]{lang="EN-US"}]{#struct_0_x5826_19109_x498597430}

[\*Dec  5 05:49:28:081 2012 Sysname MSDP/7/CONNECT: -MDC=1; Peer 10.1.1.1 state changed from DISABLED to LISTEN]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_2078579360}*[对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的状态由]{style="font-family:宋体"}[DISABLED]{lang="EN-US"}[迁移到]{style="font-family:宋体"}[LISTEN]{lang="EN-US"}*

[[\*Dec  5 05:50:16:343 2012 Sysname MSDP/7/CONNECT: -MDC=1; Accepted connection request from peer 10.1.1.1]{lang="EN-US"}]{#struct_0_x5826_19109_169152312}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_1734343226}*[接受对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的连接成功]{style="font-family:宋体"}*

[[\*Dec  5 05:50:16:343 2012 Sysname MSDP/7/CONNECT: -MDC=1; Stopped listening for connection request from peer 10.1.1.1]{lang="EN-US"}]{#struct_0_x5826_19109_x1582921258}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_1902562830}*[停止侦听]{style="font-family:宋体"}[对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的连接请求]{style="font-family:宋体"}*

[[\*Dec  5 05:50:16:343 2012 Sysname MSDP/7/CONNECT: -MDC=1; Peer 10.1.1.1 state changed from LISTEN to ESTABLISHED]{lang="EN-US"}]{#struct_0_x5826_19109_1606498832}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_x1360803776}*[对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的状态由]{style="font-family:宋体"}[LISTEN]{lang="EN-US"}[迁移到]{style="font-family:宋体"}[ESTABLISHED]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x5826_19109_1217258810}[使能]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging msdp event]{lang="EN-US"}]{#struct_0_x5826_19109_x216946114}

[\*Dec 5 05:55:15:888 2012 Sysname MSDP/7/EVENT: -MDC=1; Received socket 72 IN event]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_616676409}*[收到]{style="font-family:宋体"}[socket 72]{lang="EN-US"}[的]{style="font-family:宋体"}[IN]{lang="EN-US"}[报文事件]{style="font-family:宋体"}*

[[\*Dec 5 05:55:15:888 2012 Sysname MSDP/7/EVENT: -MDC=1; Read 3 bytes message from socket]{lang="EN-US"}]{#struct_0_x5826_19109_1519257507}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_2076867073}*[从]{style="font-family:宋体"}[socket]{lang="EN-US"}[读取]{style="font-family:宋体"}[3]{lang="EN-US"}[节的数据]{style="font-family:宋体"}*

[[\*Dec 5 05:55:15:890 2012 Sysname MSDP/7/EVENT: -MDC=1; Refreshed Hold timer of peer 10.1.1.1 to 75 seconds]{lang="EN-US"}]{#struct_0_x5826_19109_1902497294}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_6652222}*[刷新对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[Hold]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[75]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x5826_19109_x1702614217}[使能]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging msdp packet]{lang="EN-US"}]{#struct_0_x5826_19109_x524065268}

[\*Dec 5 05:58:15:645 2012 Sysname MSDP/7/PACKET: -MDC=1; Received Keepalive message from peer 10.1.1.1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_x754081120}*[从对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[收到]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Dec 5 05:58:16:295 2012 Sysname MSDP/7/PACKET: -MDC=1; Sent Keepalive message to peer 10.1.1.1]{lang="EN-US"}]{#struct_0_x5826_19109_x281510645}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_x2028976945}*[向对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x5826_19109_x927521578}[在设备上使能]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[，并打开公网实例]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[活跃组播源调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ]{lang="EN-US"}]{#struct_0_x5826_19109_675640791}[msdp source-active]{lang="EN-US"}

[\*Dec 5 06:05:13:680 2012 Sysname MSDP/7/SOURCE-ACTIVE: -MDC=1; Received SA message from peer 10.1.1.1 with 52 bytes data(RP: 1.1.1.1, len: 72, count: 1)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_1902431758}*[从对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[收到一个包含]{style="font-family:宋体"}[52]{lang="EN-US"}[字节数据的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文，]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，长度为]{style="font-family:宋体"}[72]{lang="EN-US"}[，报文中包含一个（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）的组播源信息]{style="font-family:宋体"}*

[[\*Dec 5 06:05:14:684 2012 Sysname MSDP/7/SOURCE-ACTIVE: -MDC=1; RPF check passed for 1.1.1.1 (Peer is the only established peer)]{lang="EN-US"}]{#struct_0_x5826_19109_268794412}

[*[// ]{lang="EN-US"}*]{#struct_0_x5826_19109_x1134609391}*[从对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[收到的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文通过]{style="font-family:宋体"}[RPF]{lang="EN-US"}[检查，该对等体是唯一处于]{style="font-family:宋体"}[Established]{lang="EN-US"}[状态的对等体]{style="font-family:宋体"}*
