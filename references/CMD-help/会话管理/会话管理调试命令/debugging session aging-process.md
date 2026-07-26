::: {#-131262177 .myid}
[]{#_Toc404793493}[]{#struct_0_14338_x1629_x1612706819}[]{#_Toc237771564}[]{#_Toc185127721}

**会话管理 \-- 会话管理调试命令 \-- debugging session aging-process**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x992038760}

[**[debugging session aging-process]{lang="EN-US"}**[ **event** \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_14338_x1629_1177649255}

[**[undo debugging session aging-process event]{lang="EN-US"}**]{#struct_0_14338_x1629_2107775821}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1184735661}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14338_x1629_x362593944}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1092976902}

[[network-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1787749593}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14338_x1629_x2075965734}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1656157556}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_14338_x1629_1756755127}[：指定匹配会话的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数可多次设置，但仅最后一次合法的配置生效。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1924980134}

[**[debugging session ]{lang="EN-US"}[aging-process]{lang="EN-US"}**]{#struct_0_14338_x1629_x1945292104}[命令用来打开会话管理的老化队列处理调试信息开关。]{style="font-family:宋体"}**[undo debugging session ]{lang="EN-US"}[aging-process]{lang="EN-US"}**[命令用来关闭会话管理的老化队列处理调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，会话管理的老化队列处理调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14338_x1629_x774445895}

[[表1-1 ]{lang="EN-US"}[debugging session aging-process]{lang="EN-US"}]{#struct_0_14338_x1629_x2131861416}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1633555086}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_x856001985}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x426738430}

[[Tuple5(EVENT):]{lang="EN-US"}]{#struct_0_14338_x1629_1786766553}

[*[srcIP]{lang="FR"}*]{#struct_0_14338_x1629_2125946945}[/*srcPort*\--\>*destIP*/*destPort*(*ProtoType*)]{lang="FR"}

[[会话的五元组：]{style="font-family:宋体"}]{#struct_0_14338_x1629_x462668580}

[[源]{style="font-family:宋体"}[IP/]{lang="EN-US"}]{#struct_0_14338_x1629_x188056394}[源端口]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP/]{lang="EN-US"}[目的端口（传输层协议类型（协议号））]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_14338_x1629_2009279795}[: *PRO_STATE*]{lang="PT-BR"}

[[协议状态，包括如下几种：]{style="font-family:宋体"}]{#struct_0_14338_x1629_1988898979}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[PERSIST]{lang="PT-BR"}]{#struct_0_14338_x1629_1786832089}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_SYN_SENT]{lang="PT-BR"}]{#struct_0_14338_x1629_1001098555}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_SYN_RECV]{lang="PT-BR"}]{#struct_0_14338_x1629_1766901957}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_ESTABLISHED]{lang="PT-BR"}]{#struct_0_14338_x1629_x1983920318}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_FIN_WAIT]{lang="PT-BR"}]{#struct_0_14338_x1629_1269461162}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_CLOSE_WAIT]{lang="PT-BR"}]{#struct_0_14338_x1629_1036044257}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_LAST_ACK]{lang="PT-BR"}]{#struct_0_14338_x1629_1787290838}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_TIME_WAIT]{lang="PT-BR"}]{#struct_0_14338_x1629_202930098}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_CLOSE]{lang="PT-BR"}]{#struct_0_14338_x1629_545203908}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[TCP_SYN_SENT2]{lang="PT-BR"}]{#struct_0_14338_x1629_2093171794}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[UDP_OPEN]{lang="PT-BR"}]{#struct_0_14338_x1629_x335947977}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[UDP_READY]{lang="PT-BR"}]{#struct_0_14338_x1629_x2012904158}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[ICMP_REQUEST]{lang="PT-BR"}]{#struct_0_14338_x1629_1787356374}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[ICMP_REPLY]{lang="PT-BR"}]{#struct_0_14338_x1629_1386766539}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[ICMPV6_REQUEST]{lang="PT-BR"}]{#struct_0_14338_x1629_x1860345782}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[ICMPV6_REPLY]{lang="PT-BR"}]{#struct_0_14338_x1629_1928672325}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[UDPLITE_OPEN]{lang="PT-BR"}]{#struct_0_14338_x1629_x317055790}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[UDPLITE_READY]{lang="PT-BR"}]{#struct_0_14338_x1629_1787421910}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[SCTP_CLOSED]{lang="PT-BR"}]{#struct_0_14338_x1629_578415497}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[SCTP_COOKIE_WAIT]{lang="PT-BR"}]{#struct_0_14338_x1629_732313783}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[SCTP_COOKIE_ECHOED]{lang="PT-BR"}]{#struct_0_14338_x1629_x101407325}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[SCTP_ESTABLISHED]{lang="PT-BR"}]{#struct_0_14338_x1629_1964461877}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[SCTP_SHUTDOWN_SENT]{lang="PT-BR"}]{#struct_0_14338_x1629_1787487446}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[SCTP_SHUTDOWN_RECD]{lang="PT-BR"}]{#struct_0_14338_x1629_1807340730}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[SCTP_SHUTDOWN_ACK_SENT]{lang="PT-BR"}]{#struct_0_14338_x1629_x1954864112}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[DCCP_REQUEST]{lang="PT-BR"}]{#struct_0_14338_x1629_297533500}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[DCCP_RESPOND]{lang="PT-BR"}]{#struct_0_14338_x1629_1787552982}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[DCCP_PARTOPEN]{lang="PT-BR"}]{#struct_0_14338_x1629_972983712}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[DCCP_OPEN]{lang="PT-BR"}]{#struct_0_14338_x1629_x62530090}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[DCCP_CLOSEREQ]{lang="PT-BR"}]{#struct_0_14338_x1629_487391510}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[DCCP_CLOSING]{lang="PT-BR"}]{#struct_0_14338_x1629_x1277854580}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[DCCP_TIMEWAIT]{lang="PT-BR"}]{#struct_0_14338_x1629_1787618518}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[RAWIP_OPEN]{lang="PT-BR"}]{#struct_0_14338_x1629_x507260328}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAWIP_READY]{lang="PT-BR"}]{#struct_0_14338_x1629_2133061821}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FTP]{lang="EN-US"}]{#struct_0_14338_x1629_1350669313}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DNS]{lang="PT-BR"}]{#struct_0_14338_x1629_1787684054}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIP]{lang="PT-BR"}]{#struct_0_14338_x1629_1005799832}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1984283393}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_x94736028}[在启用了]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的设备上打开]{style="font-family:宋体"}[会话管理的老化队列处理调试信息开关，当有相应会话建立并进入老化队列后，将输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging session aging-process]{lang="EN-US"}]{#struct_0_14338_x1629_1787749590}

[\<Sysname\> ping 192.168.1.58]{lang="EN-US"}

[\*May 27 10:30:28:846 2011 Sysname SESSION/7/AGING: -MDC=1;]{lang="EN-US"}

[ Tuple5(EVENT): 3.3.3.2/2048\--\>3.3.3.1/3(icmp(1))]{lang="EN-US"}

[ Aging: ICMP_REQUEST ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_x2076162342}*[发起方为]{style="font-family:宋体"}[3.3.3.2]{lang="EN-US"}[，响应方为]{style="font-family:宋体"}[3.3.3.1]{lang="EN-US"}[的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[会话，处于协议状态为]{style="font-family:宋体"}[ICMP_REQUEST]{lang="EN-US"}[的老化队列]{style="font-family:宋体"}*

::: {#-1640683372 .myid}
[]{#_Toc404793494}[]{#struct_0_14338_x1629_109317273}

**会话管理 \-- 会话管理调试命令 \-- debugging session config**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1231449943}

[**[debugging session config]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_14338_x1629_x836811568}

[**[undo debugging session config]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_14338_x1629_x2138673542}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14338_x1629_2059332914}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14338_x1629_401092278}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14338_x1629_779879835}

[[network-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1393269124}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1786766550}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14338_x1629_2126012481}

[**[all]{lang="EN-US"}**]{#struct_0_14338_x1629_1686835341}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_14338_x1629_1571798388}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_14338_x1629_x2134339627}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1263916386}

[**[debugging session config]{lang="EN-US"}**]{#struct_0_14338_x1629_x857797661}[命令用来打开会话配置处理调试信息开关。]{style="font-family:
宋体"}**[undo debugging session config]{lang="EN-US"}**[命令用来关闭会话配置处理调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，会话配置处理调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14338_x1629_x768949651}

[[表1-2 ]{lang="EN-US"}[debugging session config error]{lang="EN-US"}]{#struct_0_14338_x1629_588050790}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1638434798}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_1786832086}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_1001033019}

[[Failed to send ioctl message to slot *slot-id*, message type: *msg-type*.]{lang="EN-US"}]{#struct_0_14338_x1629_1797828430}

[[向板]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_14338_x1629_x1158106417}[发送]{style="font-family:宋体"}[ioctl]{lang="EN-US"}[消息失败，消息类型为]{style="font-family:宋体"}*[msg-type]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging session config event]{lang="EN-US"}]{#struct_0_14338_x1629_292940812}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1639601710}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_x335950659}

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1703025931}

[[Received config message, message type: *msg-type*.]{lang="EN-US"}]{#struct_0_14338_x1629_1787290839}

[[收到配置消息，消息类型为]{style="font-family:宋体"}*[msg-typ]{lang="EN-US"}*[e]{lang="EN-US"}]{#struct_0_14338_x1629_202864562}[，包括如下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_14338_x1629_x181876274}[：设置应用层老化时间]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_14338_x1629_x177787231}[：设置传输层协议老化时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_14338_x1629_1649035692}[：设置接口下的日志策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_14338_x1629_670492157}[：设置会话日志流量阈值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_14338_x1629_881884073}[：设置会话日志时间阈值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_14338_x1629_1787356375}[：设置最大会话数限制]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_14338_x1629_1386701003}[：设置长连接会话]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_14338_x1629_893709228}[：设置调试信息开关]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_14338_x1629_x1147004958}[：]{style="font-family:宋体"} [获取应用层老化时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_14338_x1629_14699570}[：获取传输层协议老化时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_14338_x1629_x1990429627}[：获取调试信息开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11]{lang="EN-US"}]{#struct_0_14338_x1629_1787421911}[：]{style="font-family:宋体"}[无效消息类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[12]{lang="EN-US"}]{#struct_0_14338_x1629_578481033}[：获取连接数限制调试信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[13]{lang="EN-US"}]{#struct_0_14338_x1629_x437623544}[：设置连接数限制调试信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[14]{lang="EN-US"}]{#struct_0_14338_x1629_1399019380}[：添加连接数限制策略]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[15]{lang="EN-US"}]{#struct_0_14338_x1629_97861426}[：删除连接数限制策略]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_14338_x1629_1787487447}[：添加连接数限制规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[17]{lang="EN-US"}]{#struct_0_14338_x1629_1807406266}[：删除连接数限制规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[18]{lang="EN-US"}]{#struct_0_14338_x1629_x1977021286}[：应用连接数限制策略]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[19]{lang="EN-US"}]{#struct_0_14338_x1629_894476650}[：取消应用连接数限制策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[20]{lang="EN-US"}]{#struct_0_14338_x1629_x675110470}[：获取连接数限制策略]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[21]{lang="EN-US"}]{#struct_0_14338_x1629_1787552983}[：获取下一个连接数限制策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[22]{lang="EN-US"}]{#struct_0_14338_x1629_972918176}[：获取连接数限制策略应用的接口列表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[23]{lang="EN-US"}]{#struct_0_14338_x1629_741721705}[：获取所有策略计数]{lang="EN-US" style="font-family:宋体"}

[[Received slot insert message, slot number: *slot-id*.]{lang="EN-US"}]{#struct_0_14338_x1629_493314043}

[[收到单板插入事件，单板号为]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_14338_x1629_x1722155080}

[[Received interface event message, interface:*interface-type interface-num*, event: *event-type*.]{lang="EN-US"}]{#struct_0_14338_x1629_1787618519}

[[收到接口事件，接口名为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_14338_x1629_x507325864}[，事件类型为]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*

[[Received ACL event message, ACL version: *version*.]{lang="EN-US"}]{#struct_0_14338_x1629_x1454884831}

[[收到]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_14338_x1629_x1778147531}[事件，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[版本为]{style="font-family:宋体"}*[version]{lang="EN-US"}*

[[Received ioctl message, message type: *config-type*]{lang="EN-US"}]{#struct_0_14338_x1629_1466464811}

[[收到]{style="font-family:宋体"}[ioctl]{lang="EN-US"}]{#struct_0_14338_x1629_1466399275}[消息，消息类型为]{style="font-family:宋体"}*[config-type]{lang="EN-US"}*[，包括以下取值]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set AppAging]{lang="EN-US"}]{#struct_0_14338_x1629_1861428145}[：设置应用协议老化时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set L4Aging]{lang="EN-US"}]{#struct_0_14338_x1629_1482993260}[：设置四层协议老化时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set LogPolicy]{lang="EN-US"}]{#struct_0_14338_x1629_1466989098}[：设置会话日志的输出策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set ]{lang="EN-US"}]{#struct_0_14338_x1629_1473978993}[L]{lang="EN-US"}[og]{lang="EN-US"}[F]{lang="EN-US"}[low]{lang="EN-US"}[：设置输出会话日志的流量阈值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set ]{lang="EN-US"}]{#struct_0_14338_x1629_1466923562}[L]{lang="EN-US"}[og]{lang="EN-US"}[T]{lang="EN-US"}[ime]{lang="EN-US"}[：设置输出会话日志的时间阈值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set ]{lang="EN-US"}]{#struct_0_14338_x1629_1821290616}[P]{lang="EN-US"}[ersist]{lang="EN-US"}[S]{lang="EN-US"}[ession]{lang="EN-US"}[：设置长连接会话]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[set ]{lang="EN-US"}]{#struct_0_14338_x1629_92877857}[D]{lang="EN-US"}[ebug]{lang="EN-US"}[：使能]{style="font-family:宋体"}[debug]{lang="EN-US"}[开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[get SpecInfo]{lang="EN-US"}]{#struct_0_14338_x1629_1466858026}[：获取产品定制信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reset ]{lang="EN-US"}]{#struct_0_14338_x1629_x1224299026}[S]{lang="EN-US"}[ession]{lang="EN-US"}[：删除会话表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reset ]{lang="EN-US"}]{#struct_0_14338_x1629_1466792490}[R]{lang="EN-US"}[elation]{lang="EN-US"}[：删除会话关联表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reset ]{lang="EN-US"}]{#struct_0_14338_x1629_1033583770}[S]{lang="EN-US"}[tatistics]{lang="EN-US"}[：删除会话统计计数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[notify A]{lang="EN-US"}]{#struct_0_14338_x1629_1467251242}[CLC]{lang="EN-US"}[hange]{lang="EN-US"}[：通知]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[notify IfActive]{lang="EN-US"}]{#struct_0_14338_x1629_x2032219987}[：通知接口激活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sync GloablCfg]{lang="EN-US"}]{#struct_0_14338_x1629_x1101691492}[：同步全局配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sync IfCfg]{lang="EN-US"}]{#struct_0_14338_x1629_1467185706}[：同步接口配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sync start]{lang="EN-US"}]{#struct_0_14338_x1629_1454283444}[：配置同步开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sync ]{lang="EN-US"}]{#struct_0_14338_x1629_1467120170}[e]{lang="EN-US"}[nd]{lang="EN-US"}[：配置同步结束]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1291342373}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_1787684055}[打开所有会话配置处理调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging session config all]{lang="EN-US"}]{#struct_0_14338_x1629_1005865368}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_x435131921}[配置]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议老化的会话时间时间为]{style="font-family:宋体"}[50000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\[Sysname\] session aging-time application ftp 50000]{lang="EN-US"}]{#struct_0_14338_x1629_x797938317}

[\*Aug 31 14:54:19:617 2011 Sysname SESSION/7/EVENT: -MDC=1; Received config message, message type: 0.]{lang="EN-US"}

[\*Aug 31 14:54:19:617 2011 Sysname SESSION/7/CONFIG: -MDC=1; Received ioctl message, message type: set AppAging.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_1174503856}*[收到一个配置消息，消息类型为]{style="font-family:宋体"}[0]{lang="EN-US"}*

::: {#-1251097754 .myid}
[]{#_Toc404793495}[]{#struct_0_14338_x1629_1436985596}[]{#_Toc237771566}[]{#_Toc185127723}

**会话管理 \-- 会话管理调试命令 \-- debugging session ext-info**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x981086986}

[**[debugging session ext-info ]{lang="EN-US"}**[{ **all** \| **event** \| **error** } \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_14338_x1629_390671668}

[**[undo debugging session ext-info ]{lang="EN-US"}**[{ **all** \| **event** \| **error** }]{lang="EN-US"}]{#struct_0_14338_x1629_x1440611143}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1499105990}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14338_x1629_1787749591}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x2076096806}

[**[all]{lang="EN-US"}**]{#struct_0_14338_x1629_x2142845335}[：表示扩展信息的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_14338_x1629_x231076484}[：表示扩展信息的事件调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_14338_x1629_x816121743}[：表示扩展信息的错误调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_14338_x1629_x1485152901}[：指定匹配会话的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数可多次设置，但仅最后一次合法的配置生效。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x863617197}

[**[debugging session ]{lang="EN-US"}[ext-info]{lang="EN-US"}**]{#struct_0_14338_x1629_x255241782}[命令用来打开会话管理的扩展信息调试开关。]{style="font-family:宋体"}**[undo debugging session ]{lang="EN-US"}[ext-info]{lang="EN-US"}**[命令用来关闭会话管理的扩展信息调试开关。]{style="font-family:宋体"}

[[缺省情况下，会话管理的扩展信息调试开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14338_x1629_1736604996}

[[表1-4 ]{lang="EN-US"}[debugging session ext-info event]{lang="EN-US"}]{#struct_0_14338_x1629_1786766551}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1635782734}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_2126078017}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_110873656}

[[Add]{lang="EN-US"}]{#struct_0_14338_x1629_x912978747}

[[扩展信息操作类型：添加扩展信息]{style="font-family:宋体"}]{#struct_0_14338_x1629_x671123498}

[[Del]{lang="EN-US"}]{#struct_0_14338_x1629_x2058586483}

[[扩展信息操作类型：删除扩展信息]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1660690709}

[[Get]{lang="EN-US"}]{#struct_0_14338_x1629_1786832087}

[[扩展信息操作类型：获取扩展信息]{style="font-family:宋体"}]{#struct_0_14338_x1629_1000967483}

[*[module]{lang="EN-US"}*]{#struct_0_14338_x1629_x1726316388}

[[业务模块，包括以下几种：]{style="font-family:宋体"}]{#struct_0_14338_x1629_666520956}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NAT]{lang="EN-US"}]{#struct_0_14338_x1629_294454733}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASPF]{lang="EN-US"}]{#struct_0_14338_x1629_902426734}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ALG]{lang="EN-US"}]{#struct_0_14338_x1629_x941592513}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STAT]{lang="EN-US"}]{#struct_0_14338_x1629_7809018}[（攻击防范）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCPPROXY]{lang="EN-US"}]{#struct_0_14338_x1629_x2099791809}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ENGINE]{lang="EN-US"}]{#struct_0_14338_x1629_x1424630442}[（会话引擎）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2P]{lang="EN-US"}]{#struct_0_14338_x1629_x1732983810}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LB]{lang="EN-US"}]{#struct_0_14338_x1629_x623799602}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FLOW_REDIRECT]{lang="EN-US"}]{#struct_0_14338_x1629_x941526977}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FLT6]{lang="EN-US"}]{#struct_0_14338_x1629_1197364624}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NATPT]{lang="EN-US"}]{#struct_0_14338_x1629_1569860414}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CONNLMT]{lang="EN-US"}]{#struct_0_14338_x1629_x454208828}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PBR]{lang="EN-US"}]{#struct_0_14338_x1629_x728656195}[（策略路由）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDOS]{lang="EN-US"}]{#struct_0_14338_x1629_x941461441}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SRVASST]{lang="EN-US"}]{#struct_0_14338_x1629_1919518189}[（]{lang="EN-US" style="font-family:宋体"}[Server Assistant]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SESSIONLOG]{lang="EN-US"}]{#struct_0_14338_x1629_1249683810}

[[Tuple5]{lang="FR"}[(EVENT)]{lang="EN-US"}]{#struct_0_14338_x1629_x284242184}[:]{lang="FR"}

[*[srcIP]{lang="FR"}*]{#struct_0_14338_x1629_x941395905}[/*srcPort*\--\>*destIP*/*destPort*(*ProtoType(Proto number)*)]{lang="FR"}

[[会话的五元组：]{style="font-family:宋体"}]{#struct_0_14338_x1629_809349916}

[[源]{style="font-family:宋体"}[IP/]{lang="EN-US"}]{#struct_0_14338_x1629_x1077520295}[源端口]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP/]{lang="EN-US"}[目的端口（传输层协议类型（协议号））]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging session ext-info error]{lang="EN-US"}]{#struct_0_14338_x1629_x433150580}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1642143534}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_x324869624}

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1467671727}

[[Add]{lang="EN-US"}]{#struct_0_14338_x1629_1160630724}

[[扩展信息操作类型：添加扩展信息]{style="font-family:宋体"}]{#struct_0_14338_x1629_x941330369}

[[Del]{lang="EN-US"}]{#struct_0_14338_x1629_x1989930765}

[[扩展信息操作类型：删除扩展信息]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1485814442}

[[Get]{lang="EN-US"}]{#struct_0_14338_x1629_x767884951}

[[扩展信息操作类型：获取扩展信息]{style="font-family:宋体"}]{#struct_0_14338_x1629_1090581552}

[*[module]{lang="EN-US"}*[ unknown]{lang="EN-US"}]{#struct_0_14338_x1629_2140398444}

[[业务模块]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_14338_x1629_x941264833}[未注册]{style="font-family:宋体"}

[[Tuple5]{lang="FR"}[(EVENT)]{lang="EN-US"}]{#struct_0_14338_x1629_395460157}[:]{lang="FR"}

[*[srcIP]{lang="FR"}*]{#struct_0_14338_x1629_1392683067}[/*srcPort*\--\>*destIP*/*destPort*(*ProtoType(Proto number)*)]{lang="FR"}

[[会话的五元组：]{style="font-family:宋体"}]{#struct_0_14338_x1629_x680527212}

[[源]{style="font-family:宋体"}[IP/]{lang="EN-US"}]{#struct_0_14338_x1629_799122074}[源端口]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP/]{lang="EN-US"}[目的端口（传输层协议类型（协议号））]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1668890345}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_1519669959}[在启用了]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的设备上打开扩展信息调试功能。在设备接口配置]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，并向接口发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文时，将输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging session ext-info all]{lang="EN-US"}]{#struct_0_14338_x1629_x941199297}

[\*Mar 24 18:15:47:164 2011 Sysname SESSION/7/EXTINFO: -MDC=1;]{lang="EN-US"}

[ Ext-Info: Add  ASPF]{lang="EN-US"}

[  Tuple5(EVENT): 192.168.0.92/8\--\>192.168.1.58/3840(icmp(1))]{lang="EN-US"}

[*[// ASPF]{lang="EN-US"}*]{#struct_0_14338_x1629_x848287177}*[向会话模块添加扩展信息成功，被添加扩展信息的会话五元组为：]{style="font-family:宋体"}[192.168.0.92/8\--\>192.168.1.58/3840(icmp(1))]{lang="EN-US"}*

::: {#-1952637972 .myid}
[]{#_Toc404793496}[]{#struct_0_14338_x1629_x1911699042}[]{#_Toc237771567}[]{#_Toc185127724}

**会话管理 \-- 会话管理调试命令 \-- debugging session packet-process**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1043357706}

[**[debugging session packet-process event]{lang="EN-US"}**[ \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_14338_x1629_x1279207914}

[**[undo debugging session packet-process event]{lang="EN-US"}**]{#struct_0_14338_x1629_1436218558}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14338_x1629_156088888}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14338_x1629_x941133761}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1189045206}

[[network-admin]{lang="EN-US"}]{#struct_0_14338_x1629_x297815885}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1586726018}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x811507643}

[**[event]{lang="EN-US"}**]{#struct_0_14338_x1629_89343773}[：报文处理相关的事件调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_14338_x1629_x1317427113}[：指定匹配会话的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数可多次设置，但仅最后一次合法的配置生效。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14338_x1629_752570723}

[**[debugging session ]{lang="EN-US"}[packet-process]{lang="EN-US"}**]{#struct_0_14338_x1629_1941808378}[命令用来打开会话管理的报文处理调试信息开关。]{style="font-family:宋体"}**[undo debugging session ]{lang="EN-US"}[packet-process]{lang="EN-US"}**[命令用来关闭会话管理的报文处理调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，会话管理的报文处理调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14338_x1629_x942116801}

[[表1-6 ]{lang="EN-US"}[debugging session packet-process]{lang="EN-US"}]{#struct_0_14338_x1629_x1277471447}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1640421710}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_x637333365}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_1645827814}

[[Tuple3: *srcIP* \--\>*destIP* (*ProtoType(Proto number)*)]{lang="EN-US"}]{#struct_0_14338_x1629_1791425479}

[[报文的三元组：源]{style="font-family:宋体"}[IP\--\>]{lang="EN-US"}]{#struct_0_14338_x1629_x2007910920}[目的]{style="font-family:宋体"}[IP/]{lang="EN-US"}[目的端口（传输层协议类型（协议号））]{style="font-family:宋体"}

[[Received: ]{lang="EN-US"}]{#struct_0_14338_x1629_x1919693446}

[[收到的报文]{style="font-family:宋体"}]{#struct_0_14338_x1629_x412889490}

[[Packet can\'t be resolved]{lang="EN-US"}]{#struct_0_14338_x1629_x942051265}

[[报文无法解析出五元组]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1745255165}

[[Packet checking failed]{lang="EN-US"}]{#struct_0_14338_x1629_x985085220}

[[报文合法性检查不通过（如报文长度、字段等不符合协议或不符合会话处理要求）]{style="font-family:宋体"}]{#struct_0_14338_x1629_478186255}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x2127464501}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_x1307563041}[在启用了]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的设备上打开报文处理调试功能，向该设备发送一个]{style="font-family:宋体"}[flag]{lang="EN-US"}[标记是非法组合的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文，将看到有如下显示信息输出。]{style="font-family:宋体"}

[[\<Sysname\> debugging session packet-process event]{lang="EN-US"}]{#struct_0_14338_x1629_x941592512}

[\<Sysname\> system-view]{lang="EN-US"}

[\*Mar 26 08:50:24:568 2011 Sysname SESSION/7/PACKETS: -MDC=1;]{lang="EN-US"}

[ Tuple3: 192.168.1.58\--\>192.168.1.11(tcp(6))]{lang="EN-US"}

[ Received: Packet checking failed ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_7874554}*[收到一个单包检查不合法的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[192.168.1.58]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[192.168.1.11]{lang="EN-US"}*

::: {#-1436584769 .myid}
[]{#_Toc404793497}[]{#struct_0_14338_x1629_1799091949}[]{#_Toc237771568}[]{#_Toc185127725}

**会话管理 \-- 会话管理调试命令 \-- debugging session relation**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1332339733}

[**[debugging session relation ]{lang="EN-US"}**[{ **all** \| **event** \| **error** }]{lang="EN-US"}]{#struct_0_14338_x1629_x35502722}

[**[undo debugging session relation ]{lang="EN-US"}**[{ **all** \| **event** \| **error** }]{lang="EN-US"}]{#struct_0_14338_x1629_x386547350}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14338_x1629_490971809}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14338_x1629_x2012105701}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14338_x1629_2021992783}

[[network-admin]{lang="EN-US"}]{#struct_0_14338_x1629_x941526976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1197299088}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1582055284}

[**[all]{lang="EN-US"}**]{#struct_0_14338_x1629_x1369260432}[：表示关联表的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_14338_x1629_1566650804}[：表示关联表的事件调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_14338_x1629_1683837833}[：表示关联表的错误调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14338_x1629_702207037}

[**[debugging session ]{lang="EN-US"}[relation]{lang="EN-US"}**]{#struct_0_14338_x1629_2147031643}[命令用来打开会话管理的关联表调试信息开关。]{style="font-family:宋体"}**[undo debugging session ]{lang="EN-US"}[relation]{lang="EN-US"}**[命令用来关闭会话管理的关联表调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，会话管理的关联表调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14338_x1629_1847110644}

[[表1-7 ]{lang="EN-US"}[debugging session relation event]{lang="EN-US"}]{#struct_0_14338_x1629_x941461440}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1613529966}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_1919452653}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_1680022374}

[[Tuple]{lang="FR"}[(EVENT)]{lang="EN-US"}]{#struct_0_14338_x1629_x1916826046}[:]{lang="FR"}

[*[srcIP/ srcPort ]{lang="FR"}*]{#struct_0_14338_x1629_1837509868}[\--\>*destIP*/*destPort*(*ProtoType(ProtoNumber)*)]{lang="FR"}

[[关联表的五元组：]{style="font-family:宋体"}]{#struct_0_14338_x1629_1716208815}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[srcIP]{lang="FR"}*]{#struct_0_14338_x1629_x249451969}[：源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[srcPort]{lang="FR"}*]{#struct_0_14338_x1629_x941395904}[：]{lang="EN-US" style="font-family:宋体"}[源]{style="font-family:宋体"}[Port]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[destIP]{lang="FR"}*]{#struct_0_14338_x1629_809415452}[：]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[destPort]{lang="FR"}*]{#struct_0_14338_x1629_677659843}[：]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[Port]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ProtoType]{lang="FR"}*]{#struct_0_14338_x1629_497316323}[：传输层协议类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ProtoNumber]{lang="FR"}*]{#struct_0_14338_x1629_x700607425}[：]{lang="EN-US" style="font-family:宋体"}[协议号]{style="font-family:宋体"}

[[Relation entry was created for module calling.]{lang="EN-US"}]{#struct_0_14338_x1629_1943359346}

[[业务调用触发创建关联表]{style="font-family:宋体"}]{#struct_0_14338_x1629_x941330368}

[[Relation entry was deleted for module calling]{lang="EN-US"}]{#struct_0_14338_x1629_x1989865229}

[[业务调用触发删除关联表]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1165771710}

[[Relation entry was deleted for timeout.]{lang="EN-US"}]{#struct_0_14338_x1629_1438468712}

[[老化超时触发删除关联表]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1150502546}

[[Relation entry was updated for module calling.]{lang="EN-US"}]{#struct_0_14338_x1629_x746430658}

[[业务调用触发更新关联表]{style="font-family:宋体"}]{#struct_0_14338_x1629_x941264832}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging session relation error]{lang="EN-US"}]{#struct_0_14338_x1629_395394621}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1611498062}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_1950048199}

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1127560736}

[[Error:]{lang="EN-US"}]{#struct_0_14338_x1629_x1156943128}

[[关联表错误]{style="font-family:宋体"}]{#struct_0_14338_x1629_1946720030}

[[Not enough memory for relation entry.]{lang="EN-US"}]{#struct_0_14338_x1629_x16759944}

[[没有足够的内存用于创建关联表]{style="font-family:宋体"}]{#struct_0_14338_x1629_x941199296}

[[Number of relation entries exceeded the max.]{lang="EN-US"}]{#struct_0_14338_x1629_x848221641}

[[关联表个数超过最大值]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1930721981}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1554024846}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_678908584}[在启用了]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的设备上打开关联表调试功能，当有]{style="font-family:宋体"}[FTP]{lang="EN-US"}[报文经过本设备去访问远端服务器时，将看到有如下调试信息输出。]{style="font-family:宋体"}

[[\<Sysname\> debugging session relation all]{lang="EN-US"}]{#struct_0_14338_x1629_1564254455}

[\*Mar 26 09:12:33:800 2011 Sysname SESSION/7/RELATION: -MDC=1;]{lang="EN-US"}

[ Tuple(EVENT): 192.168.1.8/- \--\>2.2.2.2/21 (tcp(6))]{lang="EN-US"}

[ Relation entry was created for module calling.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_x941133760}*[因外部模块通知创建一个关联表，其五元组为]{style="font-family:宋体"}[192.168.1.8/\-\--\>2.2.2.2/21 (TCP)]{lang="EN-US"}*

[[\*Mar 26 09:17:54:112 2011 Sysname SESSION/7/RELATION: -MDC=1;]{lang="EN-US"}]{#struct_0_14338_x1629_x1188979670}

[Tuple(EVENT): 192.168.1.8/- \--\>2.2.2.2/21 (tcp(6))]{lang="EN-US"}

[ Relation entry was deleted for time out.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_182703723}*[五元组为]{style="font-family:宋体"}[192.168.1.8/- \--\>2.2.2.2/21 (TCP(6))]{lang="EN-US"}[的关联表因老化被删除]{style="font-family:宋体"}*

[[\*Mar 24 18:22:13:476 2011 Sysname SESSION/7/RELATION: -MDC=1;]{lang="EN-US"}]{#struct_0_14338_x1629_x1855209658}

[ Error: Not enough memory for relation entry.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_x2128352031}*[没有足够的内存用于创建关联表]{style="font-family:宋体"}*

::: {#2136674472 .myid}
[]{#_Toc404793498}[]{#struct_0_14338_x1629_x553881144}[]{#_Toc237771569}[]{#_Toc185127726}[]{#_Toc302566182}[]{#_Toc302566183}[]{#_Toc302566184}[]{#_Toc302566187}[]{#_Toc302566188}[]{#_Toc302566189}[]{#_Toc302566190}[]{#_Toc302566191}[]{#_Toc302566192}[]{#_Toc302566193}[]{#_Toc302566194}[]{#_Toc302566195}[]{#_Toc302566196}[]{#_Toc302566224}[]{#_Toc302566225}

**会话管理 \-- 会话管理调试命令 \-- debugging session session-table**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x46039443}

[**[debugging session session-table ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** } \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_14338_x1629_x135269550}

[**[undo debugging session session-table ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** }]{lang="EN-US"}]{#struct_0_14338_x1629_x942116800}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1277405911}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14338_x1629_1558746795}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1187747564}

[[network-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1121687974}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1722466044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1914653217}

[**[all]{lang="EN-US"}**]{#struct_0_14338_x1629_1595975441}[：表示会话表项的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_14338_x1629_210023770}[：表示会话表项的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_14338_x1629_x942051264}[：表示会话表项的事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_14338_x1629_x1745189629}[：表示会话表项的状态机调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_14338_x1629_x1136218930}[：指定匹配会话的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数可多次设置，但仅最后一次合法的配置生效。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x178993604}

[]{#OLE_LINK1}[**[debugging session session-table]{lang="EN-US"}**]{#struct_0_14338_x1629_x1633323137}[命令用来打开会话管理的会话表项调试信息开关。]{style="font-family:宋体"}**[undo debugging session session-table]{lang="EN-US"}**[命令用来关闭会话管理的会话表项调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，会话表项的调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1691714438}

[]{#struct_0_14338_x1629_x579513327}[[表1-9 ]{lang="EN-US"}[debugging session session-table error]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1612048910}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1927252228}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1993725788}

[[Error:]{lang="EN-US"}]{#struct_0_14338_x1629_x941592515}

[[会话表错误]{style="font-family:宋体"}]{#struct_0_14338_x1629_7940090}

[[Not enough memory for session entry. ]{lang="EN-US"}]{#struct_0_14338_x1629_x2089405613}

[[会话创建时内存不足]{style="font-family:宋体"}]{#struct_0_14338_x1629_1810174861}

[[Number of session entries exceeded the max.]{lang="EN-US"}]{#struct_0_14338_x1629_2045761396}

[[会话数超过上限]{style="font-family:宋体"}]{#struct_0_14338_x1629_968928200}

[[Updating accelerate table failed.]{lang="EN-US"}]{#struct_0_14338_x1629_x1712215035}

[[更新流加速表失败]{style="font-family:宋体"}]{#struct_0_14338_x1629_x941526979}

[[Creating session entry failed]{lang="EN-US"}]{#struct_0_14338_x1629_1198019984}

[[创建会话表失败]{style="font-family:宋体"}]{#struct_0_14338_x1629_986201906}

[ ]{lang="EN-US"}

[]{#struct_0_14338_x1629_1748779293}[[表1-10 ]{lang="EN-US"}[debugging session session-table event]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1618572942}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1956029202}

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x250055695}

[[Tuple5(EVENT):]{lang="EN-US"}]{#struct_0_14338_x1629_x941461443}*[ srcIP]{lang="FR"}*[/*srcPort*\--\>*destIP*/*destPort*(*ProtoType(ProtoNumber)*)]{lang="FR"}

[[会话的五元组（事件）：]{style="font-family:宋体"}]{#struct_0_14338_x1629_1919649261}

[[源]{style="font-family:宋体"}[IP/]{lang="EN-US"}]{#struct_0_14338_x1629_1232811290}[源端口]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP/]{lang="EN-US"}[目的端口（传输层协议类型（协议号））]{style="font-family:宋体"}

[[Session entry was created.]{lang="EN-US"}]{#struct_0_14338_x1629_x1747345537}

[[会话被创建]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1320886855}

[[Session entry was deleted.]{lang="EN-US"}]{#struct_0_14338_x1629_x919079433}

[[会话被删除]{style="font-family:宋体"}]{#struct_0_14338_x1629_91881975}

[ ]{lang="EN-US"}

[]{#struct_0_14338_x1629_x941395907}[[表1-11 ]{lang="EN-US"}[debugging session session-table fsm]{lang="EN-US"}]{#_Toc130718929}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1615206798}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_809480988}

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x769304125}

[[Tuple5  (FSM):]{lang="EN-US"}]{#struct_0_14338_x1629_141751148}*[ srcIP]{lang="FR"}*[/*srcPort*\--\>*destIP*/*destPort*(*ProtoType(Proto number)*)]{lang="FR"}

[[会话的五元组（状态机）：]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1434152977}

[[源]{style="font-family:宋体"}[IP/]{lang="EN-US"}]{#struct_0_14338_x1629_1290240974}[源端口]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP/]{lang="EN-US"}[目的端口（传输层协议类型（协议号））]{style="font-family:宋体"}

[[FSM:*preState*\--\>*nextState*,]{lang="EN-US"}]{#struct_0_14338_x1629_x324577040}

[[会话状态机发生变迁（原状态为]{style="font-family:宋体"}*[preState]{lang="EN-US"}*]{#struct_0_14338_x1629_x941330371}[，下一个状态为]{style="font-family:宋体"}*[nextState]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[dir ]{lang="EN-US"}]{#struct_0_14338_x1629_x1990455052}

[[报文方向：]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1405326343}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_14338_x1629_x347386344}[：表示发起方发送的报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REPLY]{lang="EN-US"}]{#struct_0_14338_x1629_x1806740145}[：表示响应方发送的报文]{style="font-family:宋体"}

[[PacketType: *PacketType(Packetnum)*]{lang="EN-US"}]{#struct_0_14338_x1629_x120059943}

[[收到的报文的类型（报文编号）：]{style="font-family:宋体"}]{#struct_0_14338_x1629_x941264835}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GENERAL]{lang="EN-US"}]{#struct_0_14338_x1629_395591229}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_14338_x1629_1019621947}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_14338_x1629_x598241212}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN]{lang="EN-US"}]{#struct_0_14338_x1629_1116188904}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_14338_x1629_x941199299}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RST]{lang="EN-US"}]{#struct_0_14338_x1629_x849204681}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUEST]{lang="EN-US"}]{#struct_0_14338_x1629_x1137230280}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RESPONSE]{lang="EN-US"}]{#struct_0_14338_x1629_x968509918}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DATA]{lang="EN-US"}]{#struct_0_14338_x1629_x2054098711}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_14338_x1629_x941133763}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DATAACK]{lang="EN-US"}]{#struct_0_14338_x1629_x1189176278}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSEREQ]{lang="EN-US"}]{#struct_0_14338_x1629_x1730381020}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE]{lang="EN-US"}]{#struct_0_14338_x1629_x870018412}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RESET]{lang="EN-US"}]{#struct_0_14338_x1629_x707437374}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNC]{lang="EN-US"}]{#struct_0_14338_x1629_x942116803}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNCACK]{lang="EN-US"}]{#struct_0_14338_x1629_x1277340375}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INIT]{lang="EN-US"}]{#struct_0_14338_x1629_x865033139}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INITACK]{lang="EN-US"}]{#struct_0_14338_x1629_1978236466}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABORT]{lang="EN-US"}]{#struct_0_14338_x1629_x942051267}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHUTDOWN]{lang="EN-US"}]{#struct_0_14338_x1629_x1745124093}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHUTDOWNACK]{lang="EN-US"}]{#struct_0_14338_x1629_x1245417844}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ERROR]{lang="EN-US"}]{#struct_0_14338_x1629_x285430183}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COOKIEECHO]{lang="EN-US"}]{#struct_0_14338_x1629_849429746}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COOKIEACK]{lang="EN-US"}]{#struct_0_14338_x1629_x941592514}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHUTDOWNCOMPLETE]{lang="EN-US"}]{#struct_0_14338_x1629_8005626}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14338_x1629_298057258}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_x1592688170}[在启用了]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的设备上打开会话表项调试功能，有]{style="font-family:宋体"}[ping]{lang="EN-US"}[报文通过该设备时输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging session session-table all]{lang="EN-US"}]{#struct_0_14338_x1629_x578306577}

[\*Mar 24 18:15:47:164 2011 Sysname SESSION/7/TABLE: -MDC=1;]{lang="EN-US"}

[ Tuple5  (EVENT): 192.168.0.2/8\--\>192.168.1.58/3840(icmp(1))]{lang="EN-US"}

[ Session entry was created]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_1584774616}*[创建一个发起方为]{style="font-family:宋体"}[192.168.0.2]{lang="EN-US"}[，响应方为]{style="font-family:宋体"}[192.168.1.58]{lang="EN-US"}[，协议为]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[的会话]{style="font-family:宋体"}*

[[\*Mar 24 18:15:47:174 2011 Sysname SESSION/7/TABLE: -MDC=1;]{lang="EN-US"}]{#struct_0_14338_x1629_x941526978}

[ Tuple5  (FSM): 192.168.0.2/8\--\>192.168.1.58/3840(icmp(1))]{lang="EN-US"}

[ FSM:NONE  \--\> ICMP_REQUEST,dir:ORIGIN,PacketType:REQUEST(8)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_1197954448}*[由于收到]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文，会话状态发生变迁，变迁前状态为]{style="font-family:宋体"}[NONE]{lang="EN-US"}[，变迁后状态为]{style="font-family:宋体"}[ICMP_REQUEST]{lang="EN-US"}[，方向为发起方－]{style="font-family:宋体"}[\>]{lang="EN-US"}[响应方，报文的类型为]{style="font-family:宋体"}[REQUEST]{lang="EN-US"}*

[[\*Mar 24 18:15:47:175 2011 Sysname SESSION/7/TABLE: -MDC=1;]{lang="EN-US"}]{#struct_0_14338_x1629_1941776886}

[Tuple5  (FSM): 11.1.1.247/1024\--\>11.1.1.241/2048(icmp(1)) ]{lang="EN-US"}

[ FSM:ICMP_REQUEST\--\>ICMP_REPLY, dir:REPLY, PacketType:REPLY(0)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_x763787317}*[由于发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文，会话状态发生变迁，变迁前状态为]{style="font-family:宋体"}[ICMP_REQUEST]{lang="EN-US"}[，变迁后状态为]{style="font-family:宋体"}[ICMP_REPLY]{lang="EN-US"}[，方向为响应方－]{style="font-family:宋体"}[\>]{lang="EN-US"}[发起方，报文的类型为]{style="font-family:宋体"}[REPLY]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_x1760079454}[在启用了安全模块功能的设备上打开会话调试功能，当申请会话表资源的内存不足时，输出调试信息。]{style="font-family:宋体"}

[[\*Mar 24 18:22:13:476 2011 Sysname SESSION/7/TABLE: -MDC=1;]{lang="EN-US"}]{#struct_0_14338_x1629_676320438}

[ Error:  Not enough memory for session entry.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_x1377171336}*[由于]{style="font-family:宋体"}[会话创建时内存不足]{style="font-family:宋体"}*[，*申请会话表资源失败*]{style="font-family:宋体"}

::: {#-1603192721 .myid}
[]{#struct_0_14338_x1629_x1837400622}[]{#_Toc404793499}[]{#_Toc339371888}[]{#_Toc336682672}[]{#_Toc332716122}

**会话管理 \-- 会话管理调试命令 \-- debugging session alg**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x941461442}

[**[debugging session alg ]{lang="EN-US"}**[{ **all** \| **event** \| **error** } \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_14338_x1629_1919583725}

[**[undo debugging session alg ]{lang="EN-US"}**[{ **all** \| **event** \| **error** }]{lang="EN-US"}]{#struct_0_14338_x1629_929539759}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1331227516}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1797081205}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1709099572}

[[network-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1414646121}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14338_x1629_223669783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x7558390}

[**[all]{lang="EN-US"}**]{#struct_0_14338_x1629_x941395906}[：表示]{style="font-family:宋体"}[ALG]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_14338_x1629_809546524}[：表示]{style="font-family:宋体"}[ALG]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_14338_x1629_300273567}[：表示]{style="font-family:宋体"}[ALG]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_14338_x1629_94200469}[：指定匹配会话的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数可多次设置，但仅最后一次合法的配置生效。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1592116267}

[**[debugging session alg]{lang="EN-US"}**]{#struct_0_14338_x1629_1363552706}[命令用来打开]{style="font-family:宋体"}[ALG]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging session alg]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ALG]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ALG]{lang="EN-US"}]{#struct_0_14338_x1629_x1484243873}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-12 ]{lang="EN-US"}[debugging session alg event]{lang="EN-US"}]{#struct_0_14338_x1629_599396534}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1615892206}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_1524737135}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x941330370}

[[Tuple5(EVENT):]{lang="EN-US"}]{#struct_0_14338_x1629_x1990389516}*[ srcIP]{lang="FR"}*[/*srcPort*\--\>*destIP*/*destPort*(*ProtoType*)]{lang="FR"}

[[会话的五元组（事件）：]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1828902541}

[[源]{style="font-family:宋体"}[IP/]{lang="EN-US"}]{#struct_0_14338_x1629_x489510625}[源端口]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP/]{lang="EN-US"}[目的端口（传输层协议类型）]{style="font-family:宋体"}

[[ALG received packet, packet type: ]{lang="EN-US"}]{#struct_0_14338_x1629_x770292535}*[type]{lang="FR"}*

[[收到报文，]{style="font-family:宋体"}[ALG]{lang="EN-US"}]{#struct_0_14338_x1629_2021452561}[类型为]{style="font-family:宋体"}*[t]{lang="EN-US"}[ype]{lang="FR"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FTP_PORT]{lang="EN-US"}]{#struct_0_14338_x1629_x941264834}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FTP_PASV]{lang="EN-US"}]{#struct_0_14338_x1629_395525693}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FTP_EPRT]{lang="EN-US"}]{#struct_0_14338_x1629_x1269997396}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FTP_EPSV]{lang="EN-US"}]{#struct_0_14338_x1629_748992797}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_GRQ]{lang="EN-US"}]{#struct_0_14338_x1629_x1606304603}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_GCF]{lang="EN-US"}]{#struct_0_14338_x1629_x1624543960}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_GRJ]{lang="EN-US"}]{#struct_0_14338_x1629_x941199298}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_RRQ]{lang="EN-US"}]{#struct_0_14338_x1629_x849139145}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_RCF]{lang="EN-US"}]{#struct_0_14338_x1629_x1975375302}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_RRJ]{lang="EN-US"}]{#struct_0_14338_x1629_x944123550}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_URQ]{lang="EN-US"}]{#struct_0_14338_x1629_89889837}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_UCF]{lang="EN-US"}]{#struct_0_14338_x1629_1479865322}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_URJ]{lang="EN-US"}]{#struct_0_14338_x1629_x941133762}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_ARQ]{lang="EN-US"}]{#struct_0_14338_x1629_x1189110742}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_ACF]{lang="EN-US"}]{#struct_0_14338_x1629_x1444892791}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_ARJ]{lang="EN-US"}]{#struct_0_14338_x1629_1793461202}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_BRQ]{lang="EN-US"}]{#struct_0_14338_x1629_595911565}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_BCF]{lang="EN-US"}]{#struct_0_14338_x1629_x942116802}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_BRJ]{lang="EN-US"}]{#struct_0_14338_x1629_x1277274839}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_DRQ]{lang="EN-US"}]{#struct_0_14338_x1629_x672567023}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_DCF]{lang="EN-US"}]{#struct_0_14338_x1629_523389288}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_DRJ]{lang="EN-US"}]{#struct_0_14338_x1629_x942051266}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_LRQ]{lang="EN-US"}]{#struct_0_14338_x1629_x1745058557}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_LCF]{lang="EN-US"}]{#struct_0_14338_x1629_x411180630}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_LRJ]{lang="EN-US"}]{#struct_0_14338_x1629_851104281}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_IRQ]{lang="EN-US"}]{#struct_0_14338_x1629_x1639369354}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RAS_IRR]{lang="EN-US"}]{#struct_0_14338_x1629_x941592517}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_NATIONAL_ESCAPE]{lang="EN-US"}]{#struct_0_14338_x1629_8071162}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_ALERTING ]{lang="EN-US"}]{#struct_0_14338_x1629_219221832}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_CALL_PROCEEDING]{lang="EN-US"}]{#struct_0_14338_x1629_1435215632}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_CONNECT ]{lang="EN-US"}]{#struct_0_14338_x1629_x941526981}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_CONNECTACK ]{lang="EN-US"}]{#struct_0_14338_x1629_1197495701}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_PROGRESS ]{lang="EN-US"}]{#struct_0_14338_x1629_777631226}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_SETUP ]{lang="EN-US"}]{#struct_0_14338_x1629_1616708699}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_SETUP_ACK ]{lang="EN-US"}]{#struct_0_14338_x1629_x941461445}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_RESUME ]{lang="EN-US"}]{#struct_0_14338_x1629_1919780333}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_RESUME_ACK ]{lang="EN-US"}]{#struct_0_14338_x1629_1290536135}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_RESUME_REJECT ]{lang="EN-US"}]{#struct_0_14338_x1629_x1916387009}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_SUSPEND ]{lang="EN-US"}]{#struct_0_14338_x1629_x941395909}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_SUSPEND_ACK ]{lang="EN-US"}]{#struct_0_14338_x1629_808563484}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_SUSPEND_REJECT ]{lang="EN-US"}]{#struct_0_14338_x1629_x175676631}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_USER_INFORMATION]{lang="EN-US"}]{#struct_0_14338_x1629_1351007840}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_DISCONNECT ]{lang="EN-US"}]{#struct_0_14338_x1629_x941330373}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_RELEASE ]{lang="EN-US"}]{#struct_0_14338_x1629_x1990586124}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_RELEASE_COMPLETE]{lang="EN-US"}]{#struct_0_14338_x1629_526127789}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_RESTART ]{lang="EN-US"}]{#struct_0_14338_x1629_x363498674}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_RESTART_ACK ]{lang="EN-US"}]{#struct_0_14338_x1629_x941264837}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_SEGMENT ]{lang="EN-US"}]{#struct_0_14338_x1629_395722301}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_CONGESTION_CTRL]{lang="EN-US"}]{#struct_0_14338_x1629_x1817330053}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_INFORMATION ]{lang="EN-US"}]{#struct_0_14338_x1629_x941199301}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_NOTIFY ]{lang="EN-US"}]{#struct_0_14338_x1629_1107634750}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_STATUS ]{lang="EN-US"}]{#struct_0_14338_x1629_x329976305}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_STATUS_ENQUIRY ]{lang="EN-US"}]{#struct_0_14338_x1629_x2115823481}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Q931_FACILITY]{lang="EN-US"}]{#struct_0_14338_x1629_x941133765}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MULTIMEDIA_SYS_CTRL_REQUEST]{lang="EN-US"}]{#struct_0_14338_x1629_x1188783062}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MULTIMEDIA_SYS_CTRL_RESPONSE]{lang="EN-US"}]{#struct_0_14338_x1629_828046932}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MULTIMEDIA_SYS_CTRL_COMMAND]{lang="EN-US"}]{#struct_0_14338_x1629_x942116805}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MULTIMEDIA_SYS_CTRL_INDICATION]{lang="EN-US"}]{#struct_0_14338_x1629_x1277209303}

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging session alg error]{lang="EN-US"}]{#struct_0_14338_x1629_1127776219}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1623036398}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1005565366}

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_529789639}

[[Tuple5:]{lang="EN-US"}]{#struct_0_14338_x1629_x942051269}*[ srcIP]{lang="FR"}*[/*srcPort*\--\>*destIP*/*destPort*(*ProtoType*)]{lang="FR"}

[[会话的五元组：]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1745517309}

[[源]{style="font-family:宋体"}[IP/]{lang="EN-US"}]{#struct_0_14338_x1629_1797511298}[源端口]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP/]{lang="EN-US"}[目的端口（传输层协议类型）]{style="font-family:宋体"}

[[Error: No enough memory for ALG process.]{lang="EN-US"}]{#struct_0_14338_x1629_1145037685}

[[没有足够的内存用于]{style="font-family:宋体"}[ALG]{lang="EN-US"}]{#struct_0_14338_x1629_385350855}[处理]{style="font-family:宋体"}

[[Error: Encoding failed.]{lang="EN-US"}]{#struct_0_14338_x1629_526500297}

[[编码失败]{style="font-family:宋体"}]{#struct_0_14338_x1629_1371024379}

[[Error: Decoding failed.]{lang="EN-US"}]{#struct_0_14338_x1629_x941592516}

[[解码失败]{style="font-family:宋体"}]{#struct_0_14338_x1629_8136698}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14338_x1629_640199421}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_x1652237961}[在启用了安全模块功能（如]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[）的设备上打开]{style="font-family:宋体"}[ALG]{lang="EN-US"}[调试功能，有]{style="font-family:宋体"}[RAS RRQ]{lang="EN-US"}[报文通过该设备时输出调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging session alg event]{lang="EN-US"}]{#struct_0_14338_x1629_x204207941}

[\*Mar 24 18:15:47:164 2011 Sysname SESSION/7/ALG: -MDC=1;]{lang="EN-US"}

[ Tuple5(EVENT): 192.168.0.2/1018\--\>192.168.1.58/1719(UDP(17))]{lang="EN-US"}

[ ALG received packet, packet type: RAS_RRQ]{lang="EN-US"}

*[// ]{lang="EN-US"}[收到一个需要进行]{style="font-family:
宋体"}[ALG]{lang="EN-US"}[的报文，类型为]{style="font-family:
宋体"}[RAS_RRQ]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_253316749}[在启用了安全模块功能（如]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[）的设备上打开]{style="font-family:宋体"}[ALG]{lang="EN-US"}[调试功能，有]{style="font-family:宋体"}[RAS]{lang="EN-US"}[报文通过该设备，解码失败时输出调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging session alg error]{lang="EN-US"}]{#struct_0_14338_x1629_x941526980}

[\*Mar 24 18:15:47:164 2011 Sysname SESSION/7/ALG: -MDC=1;]{lang="EN-US"}

[Tuple5: 192.168.0.2/1018\--\>192.168.1.58/1719(UDP(17))]{lang="EN-US"}

[Error: Decoding failed]{lang="EN-US"}

*[// ]{lang="EN-US"}[报文解码失败]{style="font-family:
宋体"}*

::: {#662298597 .myid}
[]{#_Toc404793500}[]{#struct_0_14338_x1629_x990018561}

**会话管理 \-- 会话管理调试命令 \-- debugging session tcp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14338_x1629_523141223}

[**[debugging session tcp]{lang="EN-US"}**[ { **all** \| **packet** \| **error** } \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_14338_x1629_x1633358382}

[**[undo debugging session tcp]{lang="EN-US"}**[ { **all** \| **packet** \| **error** }]{lang="EN-US"}]{#struct_0_14338_x1629_738356948}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1551576340}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14338_x1629_1738864794}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14338_x1629_86131119}

[[network-admin]{lang="EN-US"}]{#struct_0_14338_x1629_x906985067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14338_x1629_1320564936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14338_x1629_1602838736}

[**[all]{lang="EN-US"}**]{#struct_0_14338_x1629_1609353148}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_14338_x1629_445296501}[：表示报文调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_14338_x1629_x582170691}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_14338_x1629_x633722665}[：指定匹配会话的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数可多次设置，但仅最后一次合法的配置生效。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1646081043}

[**[debugging session tcp]{lang="EN-US"}**]{#struct_0_14338_x1629_x668783282}[命令用来打开会话模块的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[检查]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging session tcp]{lang="EN-US"}**[命令用来关闭会话模块的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[检查]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1228308673}[会话模块的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[检查调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表]{style="font-family:宋体"}]{#struct_0_14338_x1629_611471354}[1-1 debugging session tcp packet]{lang="EN-US"}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1626361787}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_290621636}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_2095160690}

[[TCP seq check: Processed the first *type* packet.]{lang="EN-US"}]{#struct_0_14338_x1629_1471368146}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_2014875726}[序列号检查：对]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型的首包进行了序列号检查，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_14338_x1629_x1796522079}[：]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_14338_x1629_x1568230581}[：]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other]{lang="EN-US"}]{#struct_0_14338_x1629_x868106978}[：其他]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}

[[TCP seq check: Packet from *Dir*, seq *seq*, next seq *nextSeq*, ack *ack.*]{lang="EN-US"}]{#struct_0_14338_x1629_932361276}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_x927319434}[序列号检查：报文的方]{style="font-family:宋体"}[向为]{style="font-family:宋体"}*[Dir]{lang="EN-US"}*[，序列号为]{style="font-family:宋体"}*[seq]{lang="EN-US"}*[，下一个报文的序列号为]{style="font-family:宋体"}*[nextSeq]{lang="EN-US"}*[，确认序列号为]{style="font-family:宋体"}*[ack]{lang="EN-US"}*

[*[Dir]{lang="EN-US"}*]{#struct_0_14338_x1629_x926999955}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initiator]{lang="EN-US"}]{#struct_0_14338_x1629_1691876163}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Responder]{lang="EN-US"}]{#struct_0_14338_x1629_x1791147808}

[[TCP state check: Invalid SYN packet.]{lang="EN-US"}]{#struct_0_14338_x1629_1086083497}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_125792222}[状态机检查：非法的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[TCP state check: Current state is *state.* Invalid *type* packet.]{lang="EN-US"}]{#struct_0_14338_x1629_94517938}

[[状态机检查：当前状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*]{#struct_0_14338_x1629_x559761302}[，无效的报文类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[State]{lang="EN-US"}]{#struct_0_14338_x1629_1506901520}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONE]{lang="EN-US"}]{#struct_0_14338_x1629_529076749}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_SENT]{lang="EN-US"}]{#struct_0_14338_x1629_831765732}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_RECV]{lang="EN-US"}]{#struct_0_14338_x1629_x1037007192}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_14338_x1629_996706285}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN_WAIT]{lang="EN-US"}]{#struct_0_14338_x1629_x1123394931}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE_WAIT]{lang="EN-US"}]{#struct_0_14338_x1629_x989953025}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAST_ACK]{lang="EN-US"}]{#struct_0_14338_x1629_1746129074}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TIME_WAIT]{lang="EN-US"}]{#struct_0_14338_x1629_2136300846}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSE]{lang="EN-US"}]{#struct_0_14338_x1629_1738930330}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN_SENT2]{lang="EN-US"}]{#struct_0_14338_x1629_x1109715980}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAX]{lang="EN-US"}]{#struct_0_14338_x1629_x1212365215}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IGNORE]{lang="EN-US"}]{#struct_0_14338_x1629_x767416105}

[[类型取值包括：]{style="font-family:宋体"}]{#struct_0_14338_x1629_700505317}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYN]{lang="EN-US"}]{#struct_0_14338_x1629_x8088118}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SYNACK]{lang="EN-US"}]{#struct_0_14338_x1629_1961467250}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIN]{lang="EN-US"}]{#struct_0_14338_x1629_1977582464}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_14338_x1629_x2094719596}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RST]{lang="EN-US"}]{#struct_0_14338_x1629_x1930215519}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONE]{lang="EN-US"}]{#struct_0_14338_x1629_817945791}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAX]{lang="EN-US"}]{#struct_0_14338_x1629_1823446324}

[[TCP state check: Invalid RST packet.]{lang="EN-US"}]{#struct_0_14338_x1629_798667836}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_1164228588}[状态机检查：非法的]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[TCP seq check: Invalid sequence number during slow forwarding.]{lang="EN-US"}]{#struct_0_14338_x1629_1558182723}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_1105214397}[序列号检查：慢转处理中，检查到报文的序列号非法]{style="font-family:宋体"}

[[TCP seq check: Invalid sequence number during fast forwarding.]{lang="EN-US"}]{#struct_0_14338_x1629_927594127}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_x7901218}[序列号检查：]{style="font-family:宋体"}[快转]{style="font-family:宋体"}[处理中，检查到报文的序列号非法]{style="font-family:宋体"}

[[TCP seq check: First fragment from *Dir*, seq *seq*, sack *sack*.]{lang="EN-US"}]{#struct_0_14338_x1629_x1367420214}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_182324486}[序列号检查：分片报文的首片报文的方向为]{style="font-family:宋体"}*[Dir]{lang="EN-US"}*[，序列号为]{style="font-family:宋体"}*[seq]{lang="EN-US"}*[，]{style="font-family:宋体"}[SACK]{lang="EN-US"}[为]{style="font-family:宋体"}*[sack]{lang="EN-US"}*

[[TCP seq check: Last fragment from *Dir*, next seq *nextSeq*, total length *length*.]{lang="EN-US"}]{#struct_0_14338_x1629_395383309}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_1939914061}[序列号检查：分片报文的最后一片报文的方]{style="font-family:宋体"}[向为]{style="font-family:
  宋体"}*[Dir]{lang="EN-US"}*[，下一个报文的序列号为]{style="font-family:宋体"}*[nextSeq]{lang="EN-US"}*[，总长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[TCP seq check: Received a fragment from *Dir,* updated data of sender: ack *ack*, next seq *SendernextSeq*, maxEnd *SendermaxEnd*; and receiver: next seq *RecvnextSeq*, maxEnd *RecvmaxEnd*.]{lang="EN-US"}]{#struct_0_14338_x1629_623657354}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_x1170700632}[序列号检查：收到分片报文，方向为]{style="font-family:宋体"}*[Dir]{lang="EN-US"}*[，更新发送方数据：确认序列号为]{style="font-family:宋体"}*[ack]{lang="EN-US"}*[，下一个报文序列号为]{style="font-family:宋体"}*[SendernextSeq]{lang="EN-US"}*[、最大序列号为]{style="font-family:宋体"}*[SendermaxEnd]{lang="EN-US"}*[；更新响应方数据：下一个报文序列号为]{style="font-family:宋体"}*[RecvnextSeq]{lang="EN-US"}*[、最大序列号为]{style="font-family:宋体"}*[RecvmaxEnd]{lang="EN-US"}*

[[TCP seq check: Received a fragment from *Dir* during fast forwarding*,* updated data of sender: ack *ack*, next seq *SendernextSeq*, maxEnd *SendermaxEnd*; and receiver: next seq *RecvnextSeq*, maxEnd *RecvmaxEnd*.]{lang="EN-US"}]{#struct_0_14338_x1629_2098147757}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_x1123646465}[序列号检查：在快转流程中收到分片报文，方向为]{style="font-family:宋体"}*[Dir]{lang="EN-US"}*[，更新发送方数据：确认序列号为]{style="font-family:宋体"}*[ack]{lang="EN-US"}*[，下一个报文序列号为]{style="font-family:宋体"}*[SendernextSeq]{lang="EN-US"}*[，最大序列号为]{style="font-family:宋体"}*[SendermaxEnd]{lang="EN-US"}*[；更新响应方数据：下一个报文序列号为]{style="font-family:宋体"}*[RecvnextSeq]{lang="EN-US"}*[，最大序列号为]{style="font-family:宋体"}*[RecvmaxEnd]{lang="EN-US"}*

[[TCP seq check: Received a packet from *Dir*, updated data of sender: ack *ack*, next seq *SendernextSeq*, maxEnd *SendermaxEnd*; and receiver: next seq *RecvnextSeq*, maxEnd *RecvmaxEnd*.]{lang="EN-US"}]{#struct_0_14338_x1629_405605828}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_1726133486}[序列号检查：收到报文，方向为]{style="font-family:宋体"}*[Dir]{lang="EN-US"}*[，更新发送方数据：确认序列号为]{style="font-family:宋体"}*[ack]{lang="EN-US"}*[，下一个报文序列号为]{style="font-family:宋体"}*[SendernextSeq]{lang="EN-US"}*[，最大序列号为]{style="font-family:宋体"}*[SendermaxEnd]{lang="EN-US"}*[；更新响应方数据：下一个报文序列号为]{style="font-family:宋体"}*[RecvnextSeq]{lang="EN-US"}*[，最大序列号为]{style="font-family:宋体"}*[RecvmaxEnd]{lang="EN-US"}*

[[TCP seq check: Received a packet from *Dir* during fast forwarding*,* updated data of sender: ack *ack*, next seq *SendernextSeq*, maxEnd *SendermaxEnd*; and receiver next seq *RecvnextSeq*, maxEnd *RecvmaxEnd*.]{lang="EN-US"}]{#struct_0_14338_x1629_1605236890}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_x18346662}[序列号检查：在快转流程中收到报文，方向为]{style="font-family:宋体"}*[Dir]{lang="EN-US"}*[，更新发送方数据：确认序列号为]{style="font-family:宋体"}*[ack]{lang="EN-US"}*[，下一个报文序列号为]{style="font-family:宋体"}*[SendernextSeq]{lang="EN-US"}*[，最大序列号为]{style="font-family:宋体"}*[SendermaxEnd]{lang="EN-US"}*[；更新响应方数据：下一个报文序列号为]{style="font-family:宋体"}*[RecvnextSeq]{lang="EN-US"}*[，最大序列号为]{style="font-family:宋体"}*[RecvmaxEnd]{lang="EN-US"}*

[[TCP seq check: Invalid fragmented packet.]{lang="EN-US"}]{#struct_0_14338_x1629_93466146}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_x767350569}[序列号检查：分片报文]{style="font-family:宋体"}[TCP]{lang="EN-US"}[序列号检查报文非法]{style="font-family:宋体"}

[[TCP state check: Invalid packet.]{lang="EN-US"}]{#struct_0_14338_x1629_735060220}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_x1706942161}[状态机检查：]{style="font-family:宋体"} [TCP]{lang="EN-US"}[状态错误的非法报文]{style="font-family:宋体"}

[[TCP seq check: Successfully got the last ack *ack*.]{lang="EN-US"}]{#struct_0_14338_x1629_1961532786}

[[TCP]{lang="EN-US"}]{#struct_0_14338_x1629_x1874445209}[序列号检查：成功获取到最后一个确认序列号为]{style="font-family:宋体"}*[ack]{lang="EN-US"}*[。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表]{style="font-family:宋体"}]{#struct_0_14338_x1629_x978110505}[1-2 debugging session tcp error]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1630517739}[[字段]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1930149983}

[[描述]{style="font-family:黑体"}]{#struct_0_14338_x1629_x806273830}

[[Not enough memory.]{lang="EN-US"}]{#struct_0_14338_x1629_785546274}

[[没有足够的内存]{style="font-family:宋体"}]{#struct_0_14338_x1629_x355393171}

[[Failed to get the next sequence number of the packet with a Layer 2 header.]{lang="EN-US"}]{#struct_0_14338_x1629_x796093346}

[[获取带有二层帧头的报文的下一个报文序列号失败]{style="font-family:宋体"}]{#struct_0_14338_x1629_798733372}

[[Failed to get the next sequence number.]{lang="EN-US"}]{#struct_0_14338_x1629_1967515886}

[[获取下一个报文序列号失败]{style="font-family:宋体"}]{#struct_0_14338_x1629_x1523082696}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14338_x1629_x1761630355}

[[\# ]{lang="EN-US"}]{#struct_0_14338_x1629_x197978031}[在启用了安全模块功能（如]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[）的设备上打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[检查调试功能，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文通过该设备时输出调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging session tcp packet ]{lang="EN-US"}]{#struct_0_14338_x1629_1558248259}

[\*May 15 01:56:15:610 2014 Sysname SESSION/7/TCP-PACKET: -MDC=1; ]{lang="EN-US"}

[ TCP seq check: Processed the first SYN packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_1082116655}*[对]{style="font-family:宋体"}[SYN]{lang="EN-US"}[类型的首包进行了序列号检查]{style="font-family:宋体"}*

[[\*May 15 09:39:57:111 2014 Sysname SESSION/7/TCP-EVENT: -MDC=1; ]{lang="EN-US"}]{#struct_0_14338_x1629_x1240178546}

[ TCP seq check: Packet from Responder, seq 70c8e503, next seq 70c8e504, ack 445b75ff]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_x46526589}*[收到一个响应报文，该报文的序列号是]{style="font-family:宋体"}*[70c8e503]{lang="EN-US"}*[，下一个序列号是]{style="font-family:宋体"}*[70c8e504]{lang="EN-US"}*[，确认序列号是]{style="font-family:宋体"}*[445b75ff]{lang="EN-US"}

[[\*May 15 01:56:15:621 2014 Sysname SESSION/7/TCP-EVENT: -MDC=1; ]{lang="EN-US"}]{#struct_0_14338_x1629_x1126996064}

[TCP seq check: Invalid sequence number during fast forwarding.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_14338_x1629_x272485471}*[在快转处理流程中，报文的序列号检查不通过]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
