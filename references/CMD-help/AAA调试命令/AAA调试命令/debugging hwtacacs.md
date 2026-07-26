::: {#590448687 .myid}
[]{#_Toc404792147}[]{#struct_0_x1205_x1505_x1391717326}[]{#_Toc259001142}[]{#_Toc205709439}

**AAA调试命令 \-- AAA调试命令 \-- debugging hwtacacs**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x2028529533}

[**[debugging hwtacacs ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **receive-packet** \| **send-packet** }]{lang="EN-US"}]{#struct_0_x1205_x1505_1544958283}

[**[undo debugging hwtacacs ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **receive-packet** \| **send-packet** }]{lang="EN-US"}]{#struct_0_x1205_x1505_1134033828}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1998948792}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1533588151}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x973227702}

[[network-admin]{lang="EN-US"}]{#struct_0_x1205_x1505_56641764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1205_x1505_x1313734866}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1502322664}

[**[all]{lang="EN-US"}**]{#struct_0_x1205_x1505_1981496024}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1205_x1505_x34119642}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1205_x1505_1133968292}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[receive-packet]{lang="EN-US"}**]{#struct_0_x1205_x1505_1287895253}[：表示接收报文调试信息开关。]{style="font-family:宋体"}

[**[send-packet]{lang="EN-US"}**]{#struct_0_x1205_x1505_x483803788}[：表示发送报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1909600037}

[**[debugging hwtacacs]{lang="EN-US"}**]{#struct_0_x1205_x1505_1601167156}[命令用来打开]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging hwtacacs]{lang="EN-US"}**[命令用来表示关闭]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1376485790}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging hwtacacs error]{lang="EN-US"}]{#struct_0_x1205_x1505_x867528101}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_143833371}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x2008908723}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x828370001}

[[PAM_TACACS: Failed to connect to server.]{lang="EN-US"}]{#struct_0_x1205_x1505_1133902756}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_524811567}[：连接服务器失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to encapsulate request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x596126499}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1257180878}[：封装请求报文失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to send request data.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1143921419}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x891441074}[：发送请求数据失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to process reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134885796}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1548694253}[：处理应答数据失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to get available server.]{lang="EN-US"}]{#struct_0_x1205_x1505_1366230264}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x570207216}[：获取可用的服务器失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to encapsulate authentication continue request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x206944028}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1862351823}[：封装认证持续请求报文失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to receive *type* reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134820260}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_423957529}[：接收类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的应答数据失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to process request data.]{lang="EN-US"}]{#struct_0_x1205_x1505_2136389931}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x510838731}[：处理请求数据失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to set scheme name to pam-module-data.]{lang="EN-US"}]{#struct_0_x1205_x1505_1809020923}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1134361509}[：保存方案名到]{style="font-family:宋体"}[PAM]{lang="EN-US"}[数据中失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to set authentic.]{lang="EN-US"}]{#struct_0_x1205_x1505_1171628195}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_2089979892}[：设置]{style="font-family:宋体"}[Authentic]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[PAM_TACACS: Item length too long.]{lang="EN-US"}]{#struct_0_x1205_x1505_x508872350}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1160841388}[：数据项长度超长]{style="font-family:宋体"}

[[PAM_TACACS: Failed to find sequence for *type* packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134295973}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_828165719}[：查找类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的报文序列号失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to decrypt reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x101519725}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_386730676}[：解密应答报文失败]{style="font-family:宋体"}

[[PAM_TACACS: Failed to encrypt packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_696256133}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1134230437}[：加密报文失败]{style="font-family:宋体"}

[[PAM_TACACS: Invalid length of reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_1564677466}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1341621184}[：应答报文长度非法]{style="font-family:宋体"}

[[PAM_TACACS: Failed to instruct aaad to set server in block state.]{lang="EN-US"}]{#struct_0_x1205_x1505_x292964297}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1845950719}[：通知]{style="font-family:宋体"}[aaad]{lang="EN-US"}[进程服务器状态]{style="font-family:宋体"}[block]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[PAM_TACACS: Invalid reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134164901}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x718585200}[：应答报文无效]{style="font-family:宋体"}

[[PAM_TACACS: Failed to send packet, errorCode=*error-number*.]{lang="EN-US"}]{#struct_0_x1205_x1505_753610830}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x436625331}[：发送报文失败，返回错误码]{style="font-family:宋体"}*[error-number]{lang="EN-US"}*[.]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging hwtacacs event]{lang="EN-US"}]{#struct_0_x1205_x1505_1134099365}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_138480315}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_362169694}

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1226096019}

[[PAM_TACACS: Processing authentication reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1648516559}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1564489294}[：处理认证回应报文]{style="font-family:宋体"}

[[PAM_TACACS: Processing authorization reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x473889381}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x856954472}[：处理授权回应报文]{style="font-family:宋体"}

[[PAM_TACACS: Processing accounting reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134033829}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1998883256}[：处理计费回应报文]{style="font-family:宋体"}

[[PAM_TACACS: Encapsulating authentication request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_743242199}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1468561907}[：封装认证请求报文]{style="font-family:宋体"}

[[PAM_TACACS: Encapsulating authorization request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x396063576}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1315322003}[：封装授权请求报文]{style="font-family:宋体"}

[[PAM_TACACS: Encapsulating accounting request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_1133968293}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1287960789}[：封装计费请求报文]{style="font-family:宋体"}

[[PAM_TACACS: Encapsulating authentication continue request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x36145581}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1727436726}[：封装认证持续请求报文]{style="font-family:宋体"}

[[PAM_TACACS: Sending authentication continue request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x428599049}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x940434768}[：发送认证持续请求报文]{style="font-family:宋体"}

[[PAM_TACACS: Session successfully created.]{lang="EN-US"}]{#struct_0_x1205_x1505_1133902757}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_524877103}[：创建会话成功]{style="font-family:宋体"}

[[PAM_TACACS: Getting available server, ]{lang="EN-US"}]{#struct_0_x1205_x1505_x1422809065}[server-ip=]{lang="FR"}*[server-ip]{lang="EN-US"}*[; server-port=*server-port*; ]{lang="FR"}[VPN instance]{lang="EN-US"}[=]{lang="FR"}*[vpn-instance]{lang="EN-US"}*[.]{lang="FR"}

[[PAM_TACACS]{lang="FR"}]{#struct_0_x1205_x1505_x1070982866}[：]{style="font-family:宋体"}[获取可用的服务器]{style="font-family:宋体"}[，]{style="font-family:宋体"}[服务器]{style="font-family:宋体"}[IP]{lang="FR"}[地址为]{style="font-family:宋体"}*[server-ip]{lang="FR"}*[，]{style="font-family:宋体"}[端口号为]{style="font-family:宋体"}*[server-port]{lang="FR"}*[，]{style="font-family:宋体"}[服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[为]{style="font-family:宋体"}*[vpn-instance]{lang="FR"}*

[[PAM_TACACS: Connection succeeded, server-ip=]{lang="EN-US"}]{#struct_0_x1205_x1505_x1182427528}*[server-ip]{lang="FR"}*[, port=]{lang="EN-US"}*[server-port]{lang="FR"}*[, VPN instance=]{lang="EN-US"}*[vpn-instance]{lang="FR"}*

[[PAM_TACACS]{lang="FR"}]{#struct_0_x1205_x1505_1134885797}[：]{style="font-family:宋体"}[连接服务器成功]{style="font-family:宋体"}[，]{style="font-family:宋体"}[服务器]{style="font-family:宋体"}[IP]{lang="FR"}[地址为]{style="font-family:宋体"}*[server-ip]{lang="FR"}*[，]{style="font-family:宋体"}[端口号为]{style="font-family:宋体"}*[server-port]{lang="FR"}*[，]{style="font-family:宋体"}[服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[为]{style="font-family:宋体"}*[vpn-instance]{lang="FR"}*

[[PAM_TACACS: Dispatching request, Primitive: *primitive-name*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1548628717}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_2011620706}[：分发请求，表示请求类型的原语为]{style="font-family:宋体"}*[primitive-name]{lang="EN-US"}*

[[PAM_TACACS: Creating request data, data type: *request-type.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x1182402330}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1134820261}[：创建请求数据，数据类型为]{style="font-family:宋体"}*[request-type]{lang="EN-US"}*

[[PAM_TACACS: Processing reply data, Reply Type: *type.*]{lang="EN-US"}]{#struct_0_x1205_x1505_424023065}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1898458906}[：处理应答输入，应答类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[PAM_TACACS: Processed authentication reply message, resultCode: *code*.]{lang="EN-US"}]{#struct_0_x1205_x1505_129545041}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_949639208}[：处理了认证应答消息，结果码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[PAM_TACACS: Processed authorization reply message, resultCode: *code*.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134361506}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1172480163}[：处理了授权应答消息，结果码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[PAM_TACACS: Processing TACACS authentication.]{lang="EN-US"}]{#struct_0_x1205_x1505_x2004142975}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1015931817}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[PAM_TACACS: Processing TACACS authorization.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134295970}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_828100183}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[授权]{style="font-family:宋体"}

[[PAM_TACACS: Processing TACACS start-accounting.]{lang="EN-US"}]{#struct_0_x1205_x1505_x448526955}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_380786066}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[开始计费]{style="font-family:宋体"}

[[PAM_TACACS: Processing TACACS stop-accounting.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134230434}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1564874074}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[结束计费]{style="font-family:宋体"}

[[PAM_TACACS: Processing TACACS update-accounting.]{lang="EN-US"}]{#struct_0_x1205_x1505_980362550}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_186157143}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[实时计费]{style="font-family:宋体"}

[[PAM_TACACS: TACACS authentication succeeded..]{lang="EN-US"}]{#struct_0_x1205_x1505_1134164898}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1237140105}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[认证成功]{style="font-family:宋体"}

[[PAM_TACACS: TACACS authorization succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_x426830596}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1508310557}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[授权成功]{style="font-family:宋体"}

[[PAM_TACACS: TACACS start-accounting succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134099362}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_362104158}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[开始计费成功]{style="font-family:宋体"}

[[PAM_TACACS: TACACS stop-accounting succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_x840916992}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1134033826}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[结束计费成功]{style="font-family:宋体"}

[[PAM_TACACS: TACACS update-accounting succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_1999604152}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1475685074}[：处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[实时计费成功]{style="font-family:宋体"}

[[PAM_TACACS: Received packet, length=*packet-len*, errorCode=*error-number*.]{lang="EN-US"}]{#struct_0_x1205_x1505_518492815}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1133968290}[：接收报文，获取到的报文长度错误，报文长度为]{style="font-family:宋体"}*[packet-len]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[error-number]{lang="EN-US"}*

[[PAM_TACACS: Received socket close event.]{lang="EN-US"}]{#struct_0_x1205_x1505_1287764181}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x859027083}[：收到关闭]{style="font-family:宋体"}[socket]{lang="EN-US"}[事件，本端也要关闭]{style="font-family:宋体"}[socket]{lang="EN-US"}

[[PAM_TACACS: Response timed out.]{lang="EN-US"}]{#struct_0_x1205_x1505_1133902754}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_524942639}[：响应报文超时]{style="font-family:宋体"}

[[PAM_TACACS: Connection timed out.]{lang="EN-US"}]{#struct_0_x1205_x1505_x215976021}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1134885794}[：连接超时]{style="font-family:宋体"}

[[PAM_TACACS: Connecting to server\...]{lang="EN-US"}]{#struct_0_x1205_x1505_x1548563181}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1859581482}[：连接服务器]{style="font-family:宋体"}

[[PAM_TACACS: Reply SocketFd received *event* event.]{lang="EN-US"}]{#struct_0_x1205_x1505_1134820258}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_423433238}[：回应报文套接字接收到]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件]{style="font-family:宋体"}

[[PAM_TACACS: Reply message successfully sent.]{lang="EN-US"}]{#struct_0_x1205_x1505_x303503049}

[[PAM_TACACS]{lang="EN-US"}]{#struct_0_x1205_x1505_1134361507}[：成功发送回应消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging hwtacacs receive-packet]{lang="EN-US"}]{#struct_0_x1205_x1505_1172545699}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_166755387}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x824143298}

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x589472097}

[[The reply packet body is invalid]{lang="EN-US"}]{#struct_0_x1205_x1505_x1752147012}

[[报文主体不合法]{style="font-family:宋体"}]{#struct_0_x1205_x1505_746719883}

[[version]{lang="EN-US"}]{#struct_0_x1205_x1505_1134295971}

[[协议版本号]{style="font-family:宋体"}]{#struct_0_x1205_x1505_828034647}

[[type]{lang="EN-US"}]{#struct_0_x1205_x1505_x2042594669}

[[报文类型]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x709895103}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHEN_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_x566413076}[：认证请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHEN_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_x1494122725}[：认证回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHEN_CONTINUE]{lang="EN-US"}]{#struct_0_x1205_x1505_1134230435}[：持续认证报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHOR_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_1564808538}[：授权请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUHTOR_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_1395502574}[：授权回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCOUNT_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_1543270095}[：计费请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCOUNT_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_x546749424}[：计费回应报文]{lang="EN-US" style="font-family:宋体"}

[[seq_no]{lang="EN-US"}]{#struct_0_x1205_x1505_x1238291743}

[[报文序列号，每个会话的第一个报文其序列号必为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1205_x1505_1134164899}[，后续的报文递增]{style="font-family:宋体"}

[[flag]{lang="EN-US"}]{#struct_0_x1205_x1505_1237205641}

[[报文主体是否加密的标志]{style="font-family:宋体"}]{#struct_0_x1205_x1505_14208602}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UNENCRYPTED_FLAG]{lang="EN-US"}]{#struct_0_x1205_x1505_x1621089253}[：非加密]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ENCRYPTED_FLAG]{lang="EN-US"}]{#struct_0_x1205_x1505_155593863}[：加密]{lang="EN-US" style="font-family:宋体"}

[[session-id]{lang="EN-US"}]{#struct_0_x1205_x1505_1134099363}

[[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1205_x1505_362038622}[，随机生成，在会话过程中此值不变]{style="font-family:宋体"}

[[length of payload]{lang="EN-US"}]{#struct_0_x1205_x1505_1473397192}

[[报文主体的长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x920486870}

[[status]{lang="EN-US"}]{#struct_0_x1205_x1505_1078007847}

[[当前认证、授权和计费状态]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1134033827}

[[flags]{lang="EN-US"}]{#struct_0_x1205_x1505_1999538616}

[[用户输入的用户名和密码是否回显（认证响应包中）]{style="font-family:宋体"}]{#struct_0_x1205_x1505_756790067}

[[server_msg len]{lang="EN-US"}]{#struct_0_x1205_x1505_x1450493137}

[[显示给用户的信息长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1133968291}

[[data len ]{lang="EN-US"}]{#struct_0_x1205_x1505_1287829717}

[[服务器返回用于说明用户失败原因的信息的长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1950202324}

[[server-msg]{lang="EN-US"}]{#struct_0_x1205_x1505_x1194146014}

[[服务器返回给登录用户的信息，需要输出到用户端]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1133902755}

[[data]{lang="EN-US"}]{#struct_0_x1205_x1505_525008175}

[[服务器返回的信息，用于说明失败原因]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1506566291}

[[arg_cnt]{lang="EN-US"}]{#struct_0_x1205_x1505_x1683813997}

[[授权属性个数]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1134885795}

[[argN_len]{lang="EN-US"}]{#struct_0_x1205_x1505_x1548497645}

[[第]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x1205_x1505_x1636962774}[个授权属性的长度]{style="font-family:宋体"}

[[argN:]{lang="EN-US"}]{#struct_0_x1205_x1505_x509245594}

[[第]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x1205_x1505_1134820259}[个授权属性]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging hwtacacs send-packet]{lang="EN-US"}]{#struct_0_x1205_x1505_423498774}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_163499483}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x322133766}

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_629694112}

[[version]{lang="EN-US"}]{#struct_0_x1205_x1505_x723663054}

[[协议版本号]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x836804753}

[[type]{lang="EN-US"}]{#struct_0_x1205_x1505_1134361504}

[[报文类型]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1172349091}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHEN_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_1170807728}[：认证请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHEN_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_1652390664}[：认证回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHEN_CONTINUE]{lang="EN-US"}]{#struct_0_x1205_x1505_x366402251}[：持续认证报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[AUTHOR_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_603589245}[：授权请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ AUHTOR_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_x590028335}[：授权回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCOUNT_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_1134295968}[：计费请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCOUNT_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_828624472}[：计费回应报文]{lang="EN-US" style="font-family:宋体"}

[[seq_no]{lang="EN-US"}]{#struct_0_x1205_x1505_x121085013}

[[报文序列号，每个会话的第一个报文其序列号必为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1205_x1505_132358818}[，后续的报文递加]{style="font-family:宋体"}

[[flag]{lang="EN-US"}]{#struct_0_x1205_x1505_x2131372003}

[[报文主体是否加密的标志]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1134230432}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UNENCRYPTED_FLAG]{lang="EN-US"}]{#struct_0_x1205_x1505_1564480858}[：非加密]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ENCRYPTED_FLAG]{lang="EN-US"}]{#struct_0_x1205_x1505_1389384516}[：加密]{lang="EN-US" style="font-family:宋体"}

[[session-id]{lang="EN-US"}]{#struct_0_x1205_x1505_x1247917566}

[[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1205_x1505_863016902}[，随机生成，在会话过程中此值不变]{style="font-family:宋体"}

[[length of payload]{lang="EN-US"}]{#struct_0_x1205_x1505_1134164896}

[[报文主体的长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1238057609}

[[version]{lang="EN-US"}]{#struct_0_x1205_x1505_981055306}

[[报文的序列号]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1653916883}

[[type]{lang="EN-US"}]{#struct_0_x1205_x1505_92563535}

[[报文类型]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1134099360}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[AUTHEN_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_361973086}[：认证请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHEN_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_x246547253}[：认证回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHEN_CONTINUE]{lang="EN-US"}]{#struct_0_x1205_x1505_x835270099}[：持续认证报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AUTHOR_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_x2008751640}[：授权请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ AUHTOR_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_1134033824}[：授权回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCOUNT_REQUEST]{lang="EN-US"}]{#struct_0_x1205_x1505_1999735224}[：计费请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCOUNT_REPLY]{lang="EN-US"}]{#struct_0_x1205_x1505_1474541087}[：计费回应报文]{lang="EN-US" style="font-family:宋体"}

[[seq_no]{lang="EN-US"}]{#struct_0_x1205_x1505_1736425425}

[[报文序列号，每个会话的第一个报文其序列号必为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1205_x1505_1133968288}[，后续的报文递加]{style="font-family:宋体"}

[[flag]{lang="EN-US"}]{#struct_0_x1205_x1505_1287239892}

[[报文主体是否加密的标志]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1232124050}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UNENCRYPTED_FLAG]{lang="EN-US"}]{#struct_0_x1205_x1505_x1582580579}[，非加密]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ENCRYPTED_FLAG]{lang="EN-US"}]{#struct_0_x1205_x1505_1133902752}[，加密]{lang="EN-US" style="font-family:宋体"}

[[session-id]{lang="EN-US"}]{#struct_0_x1205_x1505_524549423}

[[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1205_x1505_x1894817557}[，随机生成，在会话过程中此值不变]{style="font-family:宋体"}

[[action ]{lang="EN-US"}]{#struct_0_x1205_x1505_1134885792}

[[需要对用户执行的认证动作]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1548956397}

[[priv_lvl]{lang="EN-US"}]{#struct_0_x1205_x1505_x1886886361}

[[用户级别，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1205_x1505_472606983}[～]{style="font-family:宋体"}[15]{lang="EN-US"}

[[authen_type]{lang="EN-US"}]{#struct_0_x1205_x1505_1134820256}

[[认证类型]{style="font-family:宋体"}]{#struct_0_x1205_x1505_423826454}

[[service]{lang="EN-US"}]{#struct_0_x1205_x1505_975777266}

[[服务类型]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1184867941}

[[user_len]{lang="EN-US"}]{#struct_0_x1205_x1505_1134361505}

[[请求的用户名的长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1172414627}

[[port_len]{lang="EN-US"}]{#struct_0_x1205_x1505_1906771697}

[[用户发起认证的端口名的长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1134295969}

[[rem_len]{lang="EN-US"}]{#struct_0_x1205_x1505_828558936}

[[用户的地址长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x713465737}

[[data_len]{lang="EN-US"}]{#struct_0_x1205_x1505_1134230433}

[[向服务器发送的数据长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1564415322}

[[user]{lang="EN-US"}]{#struct_0_x1205_x1505_1357486672}

[[用户名]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1134164897}

[[port]{lang="EN-US"}]{#struct_0_x1205_x1505_1238123145}

[[用户发起认证的端口名称]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1783002725}

[[rem_addr]{lang="EN-US"}]{#struct_0_x1205_x1505_1134099361}

[[用户的地址]{style="font-family:宋体"}]{#struct_0_x1205_x1505_361907550}

[[data]{lang="EN-US"}]{#struct_0_x1205_x1505_x978888077}

[[向服务器发送的数据，具体数据和报文类型以及各个字段的内容有关]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1134033825}

[[user_msg len]{lang="EN-US"}]{#struct_0_x1205_x1505_1999669688}

[[用户输入的字符串长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1982382336}

[[flags]{lang="EN-US"}]{#struct_0_x1205_x1505_1133968289}

[[对于持续认证报文，表示将要执行的动作：]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1287305428}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ABORT]{lang="EN-US"}]{#struct_0_x1205_x1505_1133902753}[：退出]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[CONTINUE]{lang="EN-US"}]{#struct_0_x1205_x1505_524614959}[：继续认证]{lang="EN-US" style="font-family:宋体"}

[[对于计费报文，表示计费报文的类型：]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1432177711}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[START]{lang="EN-US"}]{#struct_0_x1205_x1505_1134885793}[：计费开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[STOP]{lang="EN-US"}]{#struct_0_x1205_x1505_x1548890861}[：计费结束]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[WATCHDOG]{lang="EN-US"}]{#struct_0_x1205_x1505_725818312}[：计费更新]{lang="EN-US" style="font-family:宋体"}

[[authen_method]{lang="EN-US"}]{#struct_0_x1205_x1505_1134820257}

[[认证采用的方法]{style="font-family:宋体"}]{#struct_0_x1205_x1505_423891990}

[[authen_service]{lang="EN-US"}]{#struct_0_x1205_x1505_x1065734388}

[[用户申请的服务类型]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594521847}

[[arg_cnt]{lang="EN-US"}]{#struct_0_x1205_x1505_x325524247}

[[授权请求属性个数]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594587383}

[[argN_len]{lang="EN-US"}]{#struct_0_x1205_x1505_x1845016072}

[[第]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x1205_x1505_x1644030687}[个授权请求属性长度]{style="font-family:宋体"}

[[argN]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594652919}

[[第]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x1205_x1505_x1737821257}[个授权属性内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1238998116}

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_115587277}[在设备上进行]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的相关配置，打开]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的事件调试信息开关。当用户从]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录设备时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging hwtacacs event]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594718455}

[\*Sep 14 03:00:26:951 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing TACACS authentication.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1143193292}*[处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[认证请求]{style="font-family:宋体"}*

[[\*Sep 14 03:00:26:951 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Dispatching request, Primitive: authentication.]{lang="EN-US"}]{#struct_0_x1205_x1505_x949817694}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_221432530}*[分发请求，请求类型为认证]{style="font-family:宋体"}*

[[\*Sep 14 03:00:26:951 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: START]{lang="EN-US"}]{#struct_0_x1205_x1505_x1589422638}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1728909355}*[创建请求数据，数据类型为]{style="font-family:宋体"}[START]{lang="EN-US"}*

[[\*Sep 14 03:00:26:952 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Session successfully created.]{lang="EN-US"}]{#struct_0_x1205_x1505_681921582}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_275793197}*[创建会话成功]{style="font-family:宋体"}*

[[\*Sep 14 03:00:26:952 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Getting available server, server-ip=192.168.0.111, server-port=49, VPN instance=\--(public).]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594783991}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1213517004}*[获取到可用的服务器，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}[，位于公网]{style="font-family:宋体"}*

[[\*Sep 14 03:00:26:953 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connecting to server\...]{lang="EN-US"}]{#struct_0_x1205_x1505_120630799}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_518029783}*[连接服务器]{style="font-family:宋体"}*

[[\*Sep 14 03:00:26:954 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLOUT event.]{lang="EN-US"}]{#struct_0_x1205_x1505_x156253058}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1176212497}*[应答报文套接字接收到]{style="font-family:宋体"}[EPOLLOUT]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Sep 14 03:00:26:954 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connection succeeded, server-ip=192.168.0.111, port=49, VPN instance=\--(public).]{lang="EN-US"}]{#struct_0_x1205_x1505_x1868423562}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1802474603}*[连接服务器成功，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}[，位于公网]{style="font-family:宋体"}*

[[\*Sep 14 03:00:26:954 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating authentication request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594849527}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_496655786}*[封装认证请求报文]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:125 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.]{lang="EN-US"}]{#struct_0_x1205_x1505_81882927}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1265336502}*[应答报文套接字接收到]{style="font-family:宋体"}[EPOLLIN]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:126 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing authentication reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1475250363}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1123017080}*[处理认证回应报文]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:126 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.]{lang="EN-US"}]{#struct_0_x1205_x1505_1573961533}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_473349957}*[成功发送回应消息]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:127 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed authentication reply message, resultCode: 2.]{lang="EN-US"}]{#struct_0_x1205_x1505_1250308317}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1594915063}*[处理认证回应数据，回应类型为持续认证]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:127 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: CONTINUE]{lang="EN-US"}]{#struct_0_x1205_x1505_x577677318}

[\*Sep 14 03:00:27:127 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating authentication continue request packet.]{lang="EN-US"}

[\*Sep 14 03:00:27:127 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Sending authentication continue request packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x951760440}*[创建持续认证报文并组装发送]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:824 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.]{lang="EN-US"}]{#struct_0_x1205_x1505_494531240}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_97994110}*[回应报文套接字接收到]{style="font-family:宋体"}[EPOLLIN]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:824 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing authentication reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1947544263}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1884241388}*[处理认证回应报文]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:824 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.]{lang="EN-US"}]{#struct_0_x1205_x1505_x872027065}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1594980599}*[回应消息发送成功]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:825 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed authentication reply message, resultCode: 0]{lang="EN-US"}]{#struct_0_x1205_x1505_x736372728}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_977259397}*[处理了认证回应消息，结果码为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Sep 14 03:00:27:825 2012 Sysname TACACS/7/EVENT: PAM_TACACS: TACACS authentication succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1203452125}

*[// ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[处理]{style="font-size:10.5pt;
font-family:宋体"}[TACACS]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[认证成功]{style="font-size:
10.5pt;font-family:宋体"}*

[\*Sep 14 03:00:27:832 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing TACACS authorization.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1467130393}*[处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[授权请求]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:832 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Dispatching request, Primitive: authorization.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1242250208}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1275240372}*[分发请求，请求类型为授权]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:832 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: START]{lang="EN-US"}]{#struct_0_x1205_x1505_x1593997559}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_88522680}*[创建请求数据，数据类型为]{style="font-family:宋体"}[START]{lang="EN-US"}*

[[\*Sep 14 03:00:27:833 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Session successfully created.]{lang="EN-US"}]{#struct_0_x1205_x1505_430226167}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1717535691}*[创建会话成功]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:833 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Getting available server, server-ip=192.168.0.111, server-port=49, VPN instance=\--(public).]{lang="EN-US"}]{#struct_0_x1205_x1505_146825817}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1713614647}*[获取到可用的服务器，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}[，位于公网]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:834 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connecting to server\...]{lang="EN-US"}]{#struct_0_x1205_x1505_x421013686}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1116512707}*[连接服务器]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:834 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLOUT event.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1380947867}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1594063095}*[回应报文套接字接收到]{style="font-family:宋体"}[EPOLLOUT]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:834 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connection succeeded, server-ip=192.168.0.111, port=49, VPN instance=\--(public).]{lang="EN-US"}]{#struct_0_x1205_x1505_x1532872985}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x2013523805}*[连接服务器成功，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}[，位于公网]{style="font-family:宋体"}*

[[\*Sep 14 03:00:27:835 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating authorization request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x477041643}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1640926460}*[封装授权请求报文]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:014 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1492089070}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x521423531}*[回应报文套接字接收到]{style="font-family:宋体"}[EPOLLIN]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:014 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing authorization reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_253714219}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1594521846}*[处理授权回应报文]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:014 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.]{lang="EN-US"}]{#struct_0_x1205_x1505_1240559694}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_674323631}*[成功发送应答消息]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:015 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed authorization reply message, resultCode: 0]{lang="EN-US"}]{#struct_0_x1205_x1505_1674603115}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_791128416}*[处理了授权回应消息，结果码为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示授权成功]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:016 2012 Sysname TACACS/7/EVENT: PAM_TACACS: TACACS authorization succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_1835580879}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_778572915}*[处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[授权成功]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:024 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing TACACS start-accounting.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1578095388}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1014781489}*[处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[开始计费请求]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:024 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Dispatching request, Primitive: accounting-start.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594587382}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x278932131}*[分发请求，请求类型为开始计费]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:024 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: START]{lang="EN-US"}]{#struct_0_x1205_x1505_379055129}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x450438165}*[创建请求数据，数据类型为]{style="font-family:宋体"}[START]{lang="EN-US"}*

[[\*Sep 14 03:00:28:025 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Session successfully created.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1698261145}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x294186229}*[创建会话成功]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:025 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Getting available server, server-ip=192.168.0.111, server-port=49, VPN instance=\--(public).]{lang="EN-US"}]{#struct_0_x1205_x1505_174198486}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x509906872}*[获取到可用的服务器，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}[，位于公网]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:026 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connecting to server\...]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594652918}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_991062098}*[连接服务器]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:026 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLOUT event.]{lang="EN-US"}]{#struct_0_x1205_x1505_1860969091}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1464738417}*[回应报文套接字接收到]{style="font-family:宋体"}[EPOLLOUT]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:026 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connection succeeded, server-ip=192.168.0.111, port=49, VPN instance=\--(public).]{lang="EN-US"}]{#struct_0_x1205_x1505_x740577644}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_622840363}*[连接服务器成功，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}*

[[\*Sep 14 03:00:28:026 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating accounting request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1122536533}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x418621563}*[封装计费请求报文]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:082 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594718454}

[\*Sep 14 03:00:28:083 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing accounting reply packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1585690063}*[处理计费回应报文]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:083 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1483376855}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1928158382}*[成功发送回应消息]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:084 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed accounting-start reply message, resultCode: 0]{lang="EN-US"}]{#struct_0_x1205_x1505_x1127491439}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1419121545}*[处理了认证回应消息，结果码为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示开始计费成功]{style="font-family:宋体"}*

[[\*Sep 14 03:00:28:084 2012 Sysname TACACS/7/EVENT: PAM_TACACS: TACACS start-accounting succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_x2081528476}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x948668596}*[处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[开始计费成功]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_x1791707537}[在设备上进行]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的相关配置，打开]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的事件调试信息开关。当从]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录到设备的用户进行]{style="font-family:宋体"}[logout]{lang="EN-US"}[操作时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging hwtacacs event]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594783990}

[\*Sep 14 03:10:31:210 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing TACACS stop-accounting.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_352566937}*[处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[停止计费请求]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:211 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Dispatching request, Primitive: accounting-stop.]{lang="EN-US"}]{#struct_0_x1205_x1505_1135166745}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x772461622}*[分发请求，请求类型为停止计费]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:211 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Creating request data, data type: START]{lang="EN-US"}]{#struct_0_x1205_x1505_705662437}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1385117686}*[创建请求数据，数据类型为]{style="font-family:宋体"}[START]{lang="EN-US"}*

[[\*Sep 14 03:10:31:211 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Session successfully created.]{lang="EN-US"}]{#struct_0_x1205_x1505_x582167268}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1772790325}*[创建会话成功]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:211 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Getting available server, server-ip=192.168.0.111, server-port=49, VPN instance=\--(public).]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594849526}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_2062739727}*[获取到可用的服务器，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}[，位于公网]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:212 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connecting to server\...]{lang="EN-US"}]{#struct_0_x1205_x1505_x1096804623}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1970738034}*[连接服务器]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:214 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd receive]{lang="EN-US"}]{#struct_0_x1205_x1505_x152399919}

[d EPOLLOUT event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1334697370}*[回应报文套接字接收到]{style="font-family:宋体"}[EPOLLOUT]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:214 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Connection succeeded,]{lang="EN-US"}]{#struct_0_x1205_x1505_1046484098}

[server-ip=192.168.0.111, port=49, VPN instance=\--(public).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1645834477}*[连接服务器成功，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[49]{lang="EN-US"}[，位于公网]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:214 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Encapsulating accounting request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594915062}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x2143761259}*[封装计费请求报文]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:376 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply SocketFd received EPOLLIN event.]{lang="EN-US"}]{#struct_0_x1205_x1505_x2083813752}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_351003582}*[回应报文套接字接收到]{style="font-family:宋体"}[EPOLLIN]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:376 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processing accounting]{lang="EN-US"}]{#struct_0_x1205_x1505_x1670358415}

[reply packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_252991360}*[处理计费回应报文]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:377 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Reply message successfully sent.]{lang="EN-US"}]{#struct_0_x1205_x1505_71468006}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_431436635}*[成功发送回应消息]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:377 2012 Sysname TACACS/7/EVENT: PAM_TACACS: Processed accounting-stop reply message, resultCode: 0]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594980598}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_829711213}*[处理了结束计费回应消息，结果码为，表示结束计费成功]{style="font-family:宋体"}*

[[\*Sep 14 03:10:31:377 2012 Sysname TACACS/7/EVENT: PAM_TACACS: TACACS stop-accounting succeeded]{lang="EN-US"}]{#struct_0_x1205_x1505_1254918432}[[.]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}]{.MsoCommentReference}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1705429185}*[处理]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[结束计费成功]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_878591200}[在设备上进行]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的相关配置，打开]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的发送报文调试信息开关。当用户从]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录设备时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging hwtacacs send-packet]{lang="EN-US"}]{#struct_0_x1205_x1505_1522247915}

[\*Apr 17 11:48:51:342 2010 Sysname TACACS/7/send_packet:Slot=1;]{lang="EN-US"}

[version: 0xc0  type: AUTHEN_REQUEST  seq_no: 1  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0x763657e2]{lang="EN-US"}

[length of payload: 23]{lang="EN-US"}

[action: LOGIN  priv_lvl: 0  authen_type: ASCII  service: LOGIN]{lang="EN-US"}

[user_len: 5    port_len: 0   rem_len: 5   data_len: 0]{lang="EN-US"}

[user: usera]{lang="FR"}

[port: ]{lang="FR"}

[rem_addr: async]{lang="FR"}

[data:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1593997558}*[发送认证请求报文，携带用户名]{style="font-family:宋体"}*

[[\*Apr 17 11:23:46:672 2010 Sysname TACACS/7/send_packet:Slot=1;]{lang="EN-US"}]{#struct_0_x1205_x1505_x1477561261}

[version: 0xc0  type: AUTHEN_CONTINUE  seq_no: 3  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0x7eae3416]{lang="EN-US"}

[length of payload: 11]{lang="EN-US"}

[user_msg len: \*\*\*\*\*\*  data_len: 0  flags: CONTINUE AUTHEN]{lang="EN-US"}

[user_msg: \*\*\*\*\*\*]{lang="EN-US"}

[data: ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1136817528}*[发送认证持续报文，携带用户密码]{style="font-family:宋体"}*

[[\*Apr 17 11:48:53:11 2010 Sysname TACACS/7/send_packet:Slot=1;]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594063094}

[version: 0xc0  type: AUTHOR_REQUEST  seq_no: 1  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0x7fc6570e]{lang="EN-US"}

[length of payload: 42]{lang="EN-US"}

[authen_method: TACACSPLUS  priv_lvl: 0  authen_type: ASCII  authen_service: LOGIN]{lang="EN-US"}

[user_len: 5    port_len: 0    rem_len: 5    arg_cnt: 2]{lang="EN-US"}

[arg0_len: 13    arg1_len: 4  ]{lang="EN-US"}

[user: usera]{lang="EN-US"}

[port: ]{lang="EN-US"}

[rem_addr: async]{lang="EN-US"}

[arg0: service=shell  arg1: cmd\*]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_33210956}*[发送授权请求报文]{style="font-family:宋体"}*

[[\*Apr 17 11:48:53:94 2010 Sysname TACACS/7/send_packet:Slot=1;]{lang="EN-US"}]{#struct_0_x1205_x1505_x436550128}

[version: 0xc0  type: ACCOUNT_REQUEST  seq_no: 1  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0x6e38fb96]{lang="EN-US"}

[length of payload: 59]{lang="EN-US"}

[flags: START]{lang="EN-US"}

[authen_method: TACACSPLUS  authen_service: LOGIN]{lang="EN-US"}

[user_len: 5   port_len: 0   rem_len: 5   arg_cnt: 3]{lang="NO-BOK"}

[arg0_len: 9     arg1_len: 10    arg2_len: 13 ]{lang="NO-BOK"}

[user: usera]{lang="NO-BOK"}

[port: ]{lang="NO-BOK"}

[rem_addr: async]{lang="NO-BOK"}

[arg0: task_id=0  arg1: timezone=0]{lang="NO-BOK"}

[arg2: service=shell]{lang="NO-BOK"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x956177806}*[发送计费开始报文]{style="font-family:宋体"}*

*[ ]{lang="NO-BOK"}*

[[\# ]{lang="NO-BOK"}]{#struct_0_x1205_x1505_2125578697}[在设备上进行]{style="font-family:宋体"}[HWTACACS]{lang="NO-BOK"}[的相关配置]{style="font-family:宋体"}[，]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[HWTACACS]{lang="NO-BOK"}[的发送报文调试信息开关。当从]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录设备的用户进行]{style="font-family:宋体"}[logout]{lang="EN-US"}[操作时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging hwtacacs send-packet]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594521849}

[\*Apr 17 11:49:06:724 2010 Sysname TACACS/7/send_packet:Slot=1;]{lang="EN-US"}

[version: 0xc0  type: ACCOUNT_REQUEST  seq_no: 1  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0x6fe71ef7]{lang="EN-US"}

[length of payload: 179]{lang="EN-US"}

[flags: STOP]{lang="EN-US"}

[authen_method: TACACSPLUS  authen_service: LOGIN]{lang="EN-US"}

[user_len: 5   port_len: 0   rem_len: 5   arg_cnt: 12]{lang="EN-US"}

[arg0_len: 9     arg1_len: 10    arg2_len: 13    arg3_len: 12 ]{lang="EN-US"}

[arg4_len: 16    arg5_len: 10    arg6_len: 11    arg7_len: 9  ]{lang="EN-US"}

[arg8_len: 10    arg9_len: 15    arg10_len: 14    arg11_len: 14 ]{lang="NO-BOK"}

[user: usera]{lang="NO-BOK"}

[port: ]{lang="NO-BOK"}

[rem_addr: async]{lang="NO-BOK"}

[arg0: task_id=0  arg1: timezone=0]{lang="EN-US"}

[arg2: service=shell  arg3: disc_cause=0]{lang="EN-US"}

[arg4: disc_cause_ext=0  arg5: bytes_in=0]{lang="EN-US"}

[arg6: bytes_out=0  arg7: paks_in=0]{lang="EN-US"}

[arg8: paks_out=0  arg9: elapsed_time=13]{lang="EN-US"}

[arg10: nas_rx_speed=0  arg11: nas_tx_speed=0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_124814447}*[发送计费结束报文]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_1341485390}[在设备上进行]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的相关配置，打开]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的接收报文调试信息开关。当用户从]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录设备时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging hwtacacs receive-packet]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594587385}

[\*Apr 17 11:52:20:318 2010 Sysname TACACS/7/recv_packet:Slot=1;]{lang="EN-US"}

[version: 0xc0  type: AUTHEN_REPLY  seq_no: 2  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0x2a1186eb]{lang="EN-US"}

[length of payload: 16]{lang="EN-US"}

[status: STATUS_GETPASS  flags: NOECHO]{lang="EN-US"}

[server_msg len: 10  data len: 0]{lang="NO-BOK"}

[server_msg: Password: ]{lang="NO-BOK"}

[data: ]{lang="NO-BOK"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_1643382170}*[接收认证回应报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[回应类型为获取密码]{style="font-family:宋体"}*

[[\*Apr 17 11:52:22:959 2010 Sysname TACACS/7/recv_packet:Slot=1;]{lang="NO-BOK"}]{#struct_0_x1205_x1505_283400899}

[version: 0xc0  type: AUTHEN_REPLY  seq_no: 4  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0x2a1186eb]{lang="EN-US"}

[length of payload: 6]{lang="EN-US"}

[status: STATUS_PASS  flags: ECHO]{lang="EN-US"}

[server_msg len: 0  data len: 0]{lang="NO-BOK"}

[server_msg: ]{lang="NO-BOK"}

[data: ]{lang="NO-BOK"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x1619088021}*[接收认证回应报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[回应类型为认证通过]{style="font-family:宋体"}*

[[\*Apr 17 11:52:22:982 2010 Sysname TACACS/7/recv_packet:Slot=1;]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1594652921}

[version: 0xc0  type: AUTHOR_REPLY  seq_no: 2  flag: ENCRYPTED_FLAG]{lang="NO-BOK"}

[session-id: 0x7339c2a3]{lang="EN-US"}

[length of payload: 18]{lang="EN-US"}

[Status: STATUS_PASS_ADD  arg_cnt: 1  server_msg len: 0  data len: 0]{lang="EN-US"}

[arg0_len: 11 ]{lang="EN-US"}

[server_msg: ]{lang="EN-US"}

[data: ]{lang="EN-US"}

[arg0: priv-lvl=15  ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x2093986081}*[接收授权回应报文，回应类型为授权成功]{style="font-family:宋体"}*

[[\*Apr 17 11:52:23:68 2010 Sysname TACACS/7/recv_packet:Slot=1;]{lang="EN-US"}]{#struct_0_x1205_x1505_x523474577}

[version: 0xc0  type: ACCOUNT_REPLY  seq_no: 2  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0xeede416]{lang="EN-US"}

[length of payload:  5]{lang="EN-US"}

[server_msg len: 0  data len: 0  status: STATUS_SUCCESS]{lang="EN-US"}

[server_msg: ]{lang="EN-US"}

[data:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_130821874}*[接收计费回应报文，回应类型为计费成功]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594718457}[在设备上进行]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的相关配置，打开]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的接收报文调试信息开关。当从]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录设备的用户进行]{style="font-family:宋体"}[logout]{lang="EN-US"}[操作时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\*Apr 17 11:52:26:670 2010 Sysname TACACS/7/recv_packet:Slot=1;]{lang="EN-US"}]{#struct_0_x1205_x1505_19606122}

[version: 0xc0  type: ACCOUNT_REPLY  seq_no: 2  flag: ENCRYPTED_FLAG]{lang="EN-US"}

[session-id: 0x69522f6]{lang="EN-US"}

[length of payload: 5]{lang="EN-US"}

[server_msg len: 0  data len: 0  status: STATUS_SUCCESS]{lang="EN-US"}

[server_msg: ]{lang="EN-US"}

[data:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1005638333}*[接收计费回应报文，回应类型为计费成功]{style="font-family:宋体"}*

::: {#-311818002 .myid}
[]{#_Toc404792148}[]{#struct_0_x1205_x1505_x1021240567}[]{#_Toc265747194}[]{#_Toc205709442}

**AAA调试命令 \-- AAA调试命令 \-- debugging ldap**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_64881920}

[**[debugging ldap ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1205_x1505_1835826585}

[**[undo debugging ldap]{lang="EN-US"}[ ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1205_x1505_x449697051}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1594783993}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1918650878}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x325057316}

[[1]{lang="EN-US"}]{#struct_0_x1205_x1505_x248542248}[：监控级]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1404688387}

[**[all]{lang="EN-US"}**]{#struct_0_x1205_x1505_x1158284033}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1205_x1505_1767964244}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1205_x1505_1480664340}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1714571672}

[**[debugging ldap]{lang="EN-US"}**]{#struct_0_x1205_x1505_x1594849529}[命令用来打开]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging ldap]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_x1205_x1505_46317092}[的]{style="font-family:宋体"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging ldap error]{lang="EN-US"}]{#struct_0_x1205_x1505_x1145555715}[命令输出信息列表]{style="font-family:黑体"}

[]{#table_struct_0_155021307}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1532248980}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1422899756}

[[PAM_LDAP: Failed to create LDAP session.]{lang="EN-US"}]{#struct_0_x1205_x1505_x117945266}

[[创建]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_x1205_x1505_1341403341}[会话失败]{style="font-family:宋体"}

[[PAM_LDAP: Failed to save LDAP session.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594915065}

[[保存]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_x1205_x1505_585122096}[会话失败]{style="font-family:宋体"}

[[PAM_LDAP: Failed to initialize LDAP.]{lang="EN-US"}]{#struct_0_x1205_x1505_1899107401}

[[初始化]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_x1205_x1505_x632173271}[失败]{style="font-family:宋体"}

[[PAM_LDAP: Failed to set LDAP options.]{lang="EN-US"}]{#struct_0_x1205_x1505_x856992089}

[[设置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_x1205_x1505_353044928}[协议版本选项失败]{style="font-family:宋体"}

[[PAM_LDAP: Anonymous binding not supported.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594980601}

[[不支持匿名绑定]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1093061837}

[[PAM_LDAP: Password not set.]{lang="EN-US"}]{#struct_0_x1205_x1505_947879411}

[[未设置口令]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1378493723}

[[PAM_LDAP: Bind operation failed.]{lang="EN-US"}]{#struct_0_x1205_x1505_564242720}

[[绑定操作失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1593997561}

[[PAM_LDAP: Failed to get bind result.]{lang="EN-US"}]{#struct_0_x1205_x1505_x267511072}

[[获取绑定结果失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1516071485}

[[PAM_LDAP: User DN is invalid.]{lang="EN-US"}]{#struct_0_x1205_x1505_1916998036}

[[用户]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x1205_x1505_x2071484203}[无效]{style="font-family:宋体"}

[[PAM_LDAP: Failed to get DN from the search result.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594063097}

[[从查找结果获取]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x1205_x1505_x370073571}[失败]{style="font-family:宋体"}

[[PAM_LDAP: Failed to allocate user DN resource.]{lang="EN-US"}]{#struct_0_x1205_x1505_x435194317}

[[分配用户]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x1205_x1505_1504448421}[资源失败]{style="font-family:宋体"}

[[PAM_LDAP: Failed to get user\'s filter.]{lang="EN-US"}]{#struct_0_x1205_x1505_624478271}

[[获取用户的过滤器失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594521848}

[[PAM_LDAP: Search operation failed.]{lang="EN-US"}]{#struct_0_x1205_x1505_1690898388}

[[查找操作失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_171881172}

[[PAM_LDAP: Failed to get configuration data.]{lang="EN-US"}]{#struct_0_x1205_x1505_x20607101}

[[获取配置数据失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594587384}

[[PAM_LDAP: Failed to get user information.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1085501185}

[[获取用户信息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_2008373102}

[[PAM_LDAP: Failed to perform binding operation as administrator.]{lang="EN-US"}]{#struct_0_x1205_x1505_450601515}

[[管理员身份的绑定操作失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1439476248}

[[PAM_LDAP: Failed to perform binding operation as user.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594652920}

[[用户身份的绑定操作失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_634897274}

[[PAM_LDAP: Failed to create response timeout timer.]{lang="EN-US"}]{#struct_0_x1205_x1505_x33342010}

[[创建响应超时定时器失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1170677101}

[[PAM_LDAP: Failed to send reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594718456}

[[发送应答消息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1546477819}

[[PAM_LDAP: Password decryption failed.]{lang="EN-US"}]{#struct_0_x1205_x1505_x204807164}

[[解析密码失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1782992821}

[[PAM_LDAP: Failed to search users.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594783992}

[[查询用户失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x810232477}

[[PAM_LDAP: Failed to add session to buffer.]{lang="EN-US"}]{#struct_0_x1205_x1505_x671291202}

[[将]{style="font-family:宋体"}[Session]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594849528}[加入到缓冲表中失败]{style="font-family:宋体"}

[[PAM_LDAP: Failed to create connection resource.]{lang="EN-US"}]{#struct_0_x1205_x1505_1612401033}

[[创建连接资源失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x2130735096}

[[PAM_LDAP: Failed to start state machine.]{lang="EN-US"}]{#struct_0_x1205_x1505_x150954417}

[[启动状态机失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594915064}

[[PAM_LDAP: Failed to create reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_x980961845}

[[创建响应信息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x804996634}

[[PAM_LDAP: Failed to find *primitivesname* sequence.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594980600}

[[查询]{style="font-family:宋体"}*[primitivesname]{lang="EN-US"}*]{#struct_0_x1205_x1505_473022104}[原语序列失败]{style="font-family:宋体"}

[[PAM_LDAP: Failed to find *primitivesname* reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_1396804538}

[[查询]{style="font-family:宋体"}*[primitivesname]{lang="EN-US"}*]{#struct_0_x1205_x1505_602024466}[原语响应数据失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging ldap event]{lang="EN-US"}]{#struct_0_x1205_x1505_x1593997560}[命令输出信息列表]{style="font-family:黑体"}

[]{#table_struct_0_179444635}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1833595013}

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1920616866}

[[PAM_LDAP: Processing LDAP authenticaion.]{lang="EN-US"}]{#struct_0_x1205_x1505_1063144034}

[[LDAP]{lang="EN-US"}]{#struct_0_x1205_x1505_1976051224}[认证操作]{style="font-family:宋体"}

[[PAM_LDAP: Creating LDAP session.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1350778770}

[[创建]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_x1205_x1505_x1958397849}[会话]{style="font-family:宋体"}

[[PAM_LDAP: Sending authentication request.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594063096}

[[发送认证请求]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1196010370}

[[PAM_LDAP: Opening LDAP session, LDAP server IP = *server-ip*, VPN instance = *vpn-instance*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1969006414}

[[打开]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_x1205_x1505_x1589720986}[会话，服务器]{style="font-family:宋体"}[IP]{lang="FR"}[地址为]{style="font-family:宋体"}*[server-ip]{lang="FR"}*[，]{style="font-family:宋体"}[服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[为]{style="font-family:宋体"}*[vpn-instance]{lang="FR"}*

[[PAM_LDAP: Executing bind operation, DN is *dn*.]{lang="EN-US"}]{#struct_0_x1205_x1505_1009348788}

[[执行绑定操作，]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x1205_x1505_x732903203}[是]{style="font-family:宋体"}*[dn]{lang="EN-US"}*

[[PAM_LDAP: Updating user DN.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594521851}

[[更新用户]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x1205_x1505_480979271}

[[PAM_LDAP: Username is *name*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1725749739}

[[用户名是]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x1205_x1505_1193133747}

[[PAM_LDAP: User\'s filter is *filter*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1695221055}

[[用户过滤器是]{style="font-family:宋体"}*[filter]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1594587387}

[[PAM_LDAP: Executing search operation.]{lang="EN-US"}]{#struct_0_x1205_x1505_480582756}

[[执行搜索操作]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x708875446}

[[PAM_LDAP: Getting search result.]{lang="EN-US"}]{#struct_0_x1205_x1505_195442920}

[[获取搜索结果]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1732422454}

[[PAM_LDAP: Executing bind operation, user\'s DN is *dn*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594652923}

[[执行绑定操作，用户]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x1205_x1505_x931186667}[是]{style="font-family:宋体"}*[dn]{lang="EN-US"}*

[[PAM_LDAP: Binding as administrator.]{lang="EN-US"}]{#struct_0_x1205_x1505_18217172}

[[以管理员身份绑定]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1517465479}

[[PAM_LDAP: Getting user information.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594718459}

[[获取用户信息]{style="font-family:宋体"}]{#struct_0_x1205_x1505_469944816}

[[PAM_LDAP: Reopening connection to server.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1914396837}

[[重新打开到服务器的连接]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1556699514}

[[PAM_LDAP: Binding as user.]{lang="EN-US"}]{#struct_0_x1205_x1505_1210799372}

[[以用户身份绑定]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594783995}

[[PAM_LDAP: Closed connection.]{lang="EN-US"}]{#struct_0_x1205_x1505_1112081824}

[[关闭连接]{style="font-family:宋体"}]{#struct_0_x1205_x1505_836210828}

[[PAM_LDAP: Response timeout timer successfully created.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1454192476}

[[成功创建响应超时定时器]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594849531}

[[PAM_LDAP: Administrator\'s b]{lang="EN-US"}]{#struct_0_x1205_x1505_x309847732}[inding operation completed.]{lang="EN-US"}

[[绑定管理员结束]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1828040776}

[[PAM_LDAP: Reply Socket received EPOLLERR/EPOLLHUP event.]{lang="EN-US"}]{#struct_0_x1205_x1505_x265394710}

[[收到]{style="font-family:宋体"}[EPOLL-ERR]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594915067}[或]{style="font-family:宋体"}[EPOLL-UP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[PAM_LDAP: Created new connection.]{lang="EN-US"}]{#struct_0_x1205_x1505_1747921510}

[[创建新连接]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x539510968}

[[PAM_LDAP: Deleted socket.]{lang="EN-US"}]{#struct_0_x1205_x1505_1351213689}

[[删除]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594980603}[连接]{style="font-family:宋体"}

[[PAM_LDAP: Server response timed out, status=*cur-state*]{lang="EN-US"}]{#struct_0_x1205_x1505_2039106045}

[[服务器响应超时，状态为]{style="font-family:宋体"}*[status]{lang="EN-US"}*]{#struct_0_x1205_x1505_1499012863}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1205_x1505_x1593997563}[：管理员绑定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1205_x1505_895288342}[：用户查询]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x1205_x1505_406381007}[：用户绑定]{lang="EN-US" style="font-family:宋体"}

[[PAM_LDAP: Performing binding operation as administrator.]{lang="EN-US"}]{#struct_0_x1205_x1505_x341623460}

[[正在绑定管理员]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594063099}

[[PAM_LDAP: Performing binding operation as user.]{lang="EN-US"}]{#struct_0_x1205_x1505_1148956203}

[[正在绑定用户]{style="font-family:宋体"}]{#struct_0_x1205_x1505_490833677}

[[PAM_LDAP: Processing AAA request data.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1594521850}

[[处理]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_x1205_x1505_2047063212}[请求数据]{style="font-family:宋体"}

[[PAM_LDAP: Number of buffered sessions reached the maximum.]{lang="EN-US"}]{#struct_0_x1205_x1505_1648149179}

[[缓存表项达到最大值]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1594587386}

[[PAM_LDAP: Data of *primitiveName* reply successfully obtained, resultCode: code.]{lang="EN-US"}]{#struct_0_x1205_x1505_2046666697}

[[成功获取原语]{style="font-family:宋体"}*[primitiveName]{lang="EN-US"}*]{#struct_0_x1205_x1505_1633647598}[响应数据，应答码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[PAM_LDAP: Data of *operation* request successfully sent.]{lang="EN-US"}]{#struct_0_x1205_x1505_x62802160}

[[成功发送]{style="font-family:宋体"}*[operation]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1594652922}[请求]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1797696688}

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_x6667864}[一台主机通过]{style="font-family:宋体"}[Console]{lang="EN-US"}[口连接设备，设备使用]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[作为认证方案对登录用户进行身份认证，并打开]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[的事件调试信息开关。用户通过]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录设备的操作时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ldap event]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1046938068}

[\*Mar 19 05:21:25:177 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Processing LDAP authenticaion.]{lang="NO-BOK"}

[*[// LDAP]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_212755058}*[认证操作]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:177 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Creating LDAP session.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1594718458}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x1096139125}*[创建]{style="font-family:宋体"}[LDAP]{lang="NO-BOK"}[会话]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:177 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Sending authentication request.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1174560712}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x1340853147}*[发送认证请求]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:178 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Opening LDAP session, LDAP server = 192.168.0.111, VPN instance = \--(public).]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1573333107}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_855812548}*[打开]{style="font-family:宋体"}[LDAP]{lang="NO-BOK"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}[服务器]{style="font-family:宋体"}[IP]{lang="FR"}[地址为]{style="font-family:宋体"}[192.168.0.111]{lang="NO-BOK"}[，位于公网]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:178 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Binding as administrator.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x422971463}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_1120958034}*[以管理员身份进行绑定]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:178 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Executing bind operation, DN is cn=administrator,cn=users,dc=secalgnbt,dc=com.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x696592496}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_x1594783994}*[执行绑定操作，]{style="font-family:宋体"}[用户]{style="font-family:宋体"}[DN]{lang="NO-BOK"}[是]{style="font-family:宋体"}[cn=administrator,cn=users,dc=secalgnbt,dc=com]{lang="NO-BOK"}*

[[\*Mar 19 05:21:25:293 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Getting user information.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1616801531}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x776317345}*[获取用户信息]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:293 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Username is usera.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x743749312}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x340710686}*[用户名是]{style="font-family:宋体"}[usera]{lang="NO-BOK"}*

[[\*Mar 19 05:21:25:293 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:User\'s filter is (&(objectClass=person)(cn=usera)).]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1678578041}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_539529095}*[用户过滤器是]{style="font-family:宋体"}["]{style="font-family:宋体"}[(&(objectClass=person)(cn=usera))]{lang="NO-BOK"}["]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:293 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Executing search operation.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_389171174}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x852370505}*[执行查询操作]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:336 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Getting search result.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1594849530}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_1256236209}*[获取查找结果]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:336 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Updating user DN.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_2045209009}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_x1000976250}*[更新用户]{style="font-family:宋体"}[DN]{lang="PT-BR"}*

[[\*Mar 19 05:21:25:338 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Reopening connection to server.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1469719454}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x994692574}*[重新打开到服务器的连接]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:338 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Opening LDAP session, LDAP server = 192.168.0.111, VPN instance = \--(public).]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1799109938}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_966278939}*[开启]{style="font-family:宋体"}[LDAP]{lang="NO-BOK"}[会话]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:338 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Binding as user.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1594915066}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_181837569}*[以用户身份进行绑定操作]{style="font-family:宋体"}*

[[\*Mar 19 05:21:25:338 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Executing bind operation, user\'s DN is CN=usera,CN=Users,DC=secalgnbt,DC=com.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1097425682}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_x949373438}*[执行绑定操作，用户]{style="font-family:宋体"}[DN]{lang="PT-BR"}[为]{style="font-family:宋体"}[CN=usera,CN=Users,DC=secalgnbt,DC=com]{lang="NO-BOK"}*

[[\*Mar 19 05:21:25:356 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Closed connection.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x2133287851}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_1586584392}*[关闭连接]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_x1250211519}[一台主机通过二层端口连接设备，设备使用]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[作为认证方案对认证用户进行身份认证，并打开]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[的事件调试信息开关。用户发起认证时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ldap event]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1979004483}

[\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Processing LDAP authenticaion.]{lang="NO-BOK"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_x351467669}*[处理]{style="font-family:宋体"}[LDAP]{lang="PT-BR"}[认证操作]{style="font-family:宋体"}*

[[\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Processing AAA request data.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1594980602}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_x689777310}*[处理]{style="font-family:宋体"}[AAA]{lang="PT-BR"}[请求数据]{style="font-family:宋体"}*

[[\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:LDAP server is: 192.168.0.111.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1417323228}

[*[// LDAP]{lang="PT-BR"}*]{#struct_0_x1205_x1505_2077534073}*[服务器]{style="font-family:宋体"}[IP]{lang="PT-BR"}[为]{style="font-family:宋体"}[192.168.0.111]{lang="PT-BR"}*

[[\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Created new connection.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x476906730}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_x1186480507}*[创建新的连接]{style="font-family:宋体"}*

[[\*Mar 19 05:28:29:755 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Executing bind operation, DN is cn=administrator,cn=users,dc=secalgnbt,dc=com.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1099866180}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_14368995}*[执行绑定操作]{style="font-family:宋体"}*

[[\*Mar 19 05:28:29:776 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Data of authentication request successfully sent.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1593997562}

[\*Mar 19 05:28:29:777 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Performing binding operation as administrator.]{lang="NO-BOK"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_x670795599}*[以管理员身份进行绑定操作进行中]{style="font-family:宋体"}*

[[\*Mar 19 05:28:30:878 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Administrator\'s binding operation completed.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_636313721}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_837183010}*[以管理员身份进行绑定完成]{style="font-family:宋体"}*

[[\*Mar 19 05:28:30:878 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Response timeout timer successfully created.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x2005250152}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_671810534}*[成功创建响应超时定时器]{style="font-family:宋体"}*

[[\*Mar 19 05:28:30:939 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Username is usera.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1223146221}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_1531320419}*[用户名是]{style="font-family:宋体"}[usera]{lang="NO-BOK"}*

[[\*Mar 19 05:28:30:939 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:User\'s filter is (&(objectClass=person)(cn=usera)).]{lang="NO-BOK"}]{#struct_0_x1205_x1505_4134204}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x1205_x1505_x1594063098}*[用户过滤器是]{style="font-family:宋体"}["]{style="font-family:宋体"}[(&(objectClass=person)(cn=usera))]{lang="NO-BOK"}["]{style="font-family:宋体"}*

[[\*Mar 19 05:28:30:986 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Updating user DN.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x1579927152}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_x117828901}*[更新用户]{style="font-family:宋体"}[DN]{lang="PT-BR"}*

[[\*Mar 19 05:28:30:989 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Performing binding operation as user.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1687386105}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_1968136394}*[以用户身份进行绑定操作]{style="font-family:宋体"}*

[[\*Mar 19 05:28:32:877 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Finish bind as user.]{lang="NO-BOK"}]{#struct_0_x1205_x1505_1451036488}

*[// ]{lang="PT-BR" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[以用户身份进行绑定完成]{style="font-size:10.5pt;
font-family:宋体"}*

[\*Mar 19 05:28:32:902 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Processing LDAP]{lang="NO-BOK"}

[ authenticaion.]{lang="NO-BOK"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1205_x1505_728459623}*[LDAP]{lang="NO-BOK"}[认证操作]{style="font-family:宋体"}*

[[\*Mar 19 05:28:32:902 2013 Sysname LDAP/7/EVENT: -MDC=1; PAM_LDAP:Data of authent]{lang="NO-BOK"}]{#struct_0_x1205_x1505_327792454}

[ication reply successfully obtained, resultCode: 0.]{lang="NO-BOK"}

*[// LDAP]{lang="PT-BR" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[认证成功]{style="font-size:
10.5pt;font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_x1205_x1505_579599822}[一台主机通过]{style="font-family:宋体"}[Console]{lang="PT-BR"}[口连接设备]{style="font-family:宋体"}[，]{style="font-family:宋体"}[设备使用]{style="font-family:宋体"}[LDAP]{lang="PT-BR"}[作为认证方案对登录用户进行身份认证]{style="font-family:宋体"}[，]{style="font-family:宋体"}[但是未配置]{style="font-family:宋体"}[login-dn]{lang="PT-BR"}[，]{style="font-family:宋体"}[打开]{style="font-family:宋体"}[LDAP]{lang="PT-BR"}[的错误调试信息开关。用户通过]{style="font-family:宋体"}[Console]{lang="EN-US"}[口登录设备的操作时，设备输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ldap error]{lang="NO-BOK"}]{#struct_0_x1205_x1505_x262561333}

[\*Jan  1 07:57:03:173 2011 ]{lang="EN-US"}[Sysname]{lang="PT-BR"}[ LDAP/7/ERROR:]{lang="EN-US"}

[PAM_LDAP: Anonymous binding not supported.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x117008961}*[不支持匿名绑定]{style="font-family:宋体"}*

[[\*Jan  1 07:57:03:174 2011 ]{lang="EN-US"}]{#struct_0_x1205_x1505_1683060367}[Sysname]{lang="PT-BR"}[ LDAP/7/ERROR:]{lang="EN-US"}

[PAM_LDAP:Failed to get user information.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x75597961}*[获取用户信息失败]{style="font-family:宋体"}*

::: {#223831281 .myid}
[]{#_Toc404792149}[]{#struct_0_x1205_x1505_x368499927}[]{#_Toc265747197}[]{#_Toc205709448}[]{#_Toc189473990}

**AAA调试命令 \-- AAA调试命令 \-- debugging local-server**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1580134665}

[**[debugging local-server]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1205_x1505_327726918}

[**[undo debugging ]{lang="EN-US"}[local-server ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1205_x1505_219878104}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1755043702}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1205_x1505_78563135}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x178342212}

[[1]{lang="EN-US"}]{#struct_0_x1205_x1505_1874848597}[：监控级]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x612331730}

[**[all]{lang="EN-US"}**]{#struct_0_x1205_x1505_x172204611}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1205_x1505_1912853576}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1205_x1505_327661382}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1770692964}

[**[debugging ]{lang="EN-US"}[local-serve]{lang="EN-US"}**[r]{lang="EN-US"}]{#struct_0_x1205_x1505_1256857076}[命令用来打开]{style="font-family:宋体"}[Local-Server]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging  ]{lang="EN-US"}[local-server]{lang="EN-US"}**[ ]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[Local-Server]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Local-Server]{lang="EN-US"}]{#struct_0_x1205_x1505_x1078922287}[的]{style="font-family:宋体"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging local-server error]{lang="EN-US"}]{#struct_0_x1205_x1505_988843811}[命令输出信息列表]{style="font-family:黑体"}

[]{#table_struct_0_168555131}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1594093501}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1751909669}

[[Authentication request processing error: Failed to parse authentication attribute.]{lang="EN-US"}]{#struct_0_x1205_x1505_327595846}

[[认证处理错误：解析认证属性失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1487177356}

[[Authentication processing error: Failed to encapsulate reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_188798249}

[[认证处理错误：封装应答消息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x2110419682}

[[Authentication processing error: Failed to send reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_925281859}

[[认证处理错误：发送应答消息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x2046826384}

[[Authorization processing error: Failed to encapsulate reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_327530310}

[[授权处理错误：封装应答消息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1475453119}

[[Authorization processing error: Failed to get user authorization attribute.]{lang="EN-US"}]{#struct_0_x1205_x1505_1342023965}

[[授权处理错误：获取用户授权属性失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1176031041}

[[Authorization request processing error: Failed to parse request message.]{lang="EN-US"}]{#struct_0_x1205_x1505_2069086320}

[[授权处理错误：解析请求消息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1987181841}

[[Authorization processing error: Failed to send reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_327464774}

[[授权处理错误：发送应答消息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x521899054}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging local-server event]{lang="EN-US"}]{#struct_0_x1205_x1505_x1770710197}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_170725691}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1343353136}

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1180971167}

[[Authentication failed, unexpected caller number *call-num1* (expected = *call-num2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_x668425017}

[[认证失败，]{style="font-family:宋体"}*[call-num1]{lang="EN-US"}*]{#struct_0_x1205_x1505_327399238}[不是期望的主叫号码，期望的主叫号码是]{style="font-family:宋体"}*[call-num2]{lang="EN-US"}*

[[Authentication failed, unexpected MAC address *mac1* (expected = *mac2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_x755886948}

[[认证失败，]{style="font-family:宋体"}*[mac1]{lang="EN-US"}*]{#struct_0_x1205_x1505_2125739878}[不是期望的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，期望的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[mac2]{lang="EN-US"}*

[[Authentication failed, unexpected VLAN ID *vlan-id1* (expected = *vlan-id2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_1835221176}

[[认证失败，]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*]{#struct_0_x1205_x1505_1514709187}[不是期望的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，期望的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*

[[Authentication failed, unexpected IP address *ip-addr1* (expected = *ip-addr2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_764491016}

[[认证失败，]{style="font-family:宋体"}*[ip-addr1]{lang="EN-US"}*]{#struct_0_x1205_x1505_327333702}[不是期望的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，期望的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[ip-addr2]{lang="EN-US"}*

[[Authentication failed, unexpected port *port1* (expected = *port2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_1583444777}

[[认证失败，]{style="font-family:宋体"}*[port1]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1351530152}[不是期望的端口，期望的端口是]{style="font-family:宋体"}*[port2]{lang="EN-US"}*

[[Authentication failed, unexpected slot number *slot-num1* (expected = *slot-num2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_x466194558}

[[认证失败，]{style="font-family:宋体"}*[slot-num1]{lang="EN-US"}*]{#struct_0_x1205_x1505_240579370}[不是期望的槽位号，期望的槽位号是]{style="font-family:宋体"}*[slot-num2]{lang="EN-US"}*

[[Authentication failed, unexpected subslot number *subslot-num1* (expected = *subslot-num2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_328316742}

[[认证失败，]{style="font-family:宋体"}*[subslot-num1]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1023226716}[不是期望的子槽号，期望的子槽号是]{style="font-family:宋体"}*[subslot-num2]{lang="EN-US"}*

[[Authentication succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_1583118201}

[[认证成功]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1820316282}

[[Authentication failed, user *user-name* doesn\'t exist.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1870968123}

[[认证失败，用户]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*]{#struct_0_x1205_x1505_328251206}[不存在]{style="font-family:宋体"}

[[Authentication failed, user\'s state is block.]{lang="EN-US"}]{#struct_0_x1205_x1505_970032669}

[[认证失败，用户的状态是阻塞]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1175114927}

[[Authentication failed, user password is wrong.]{lang="EN-US"}]{#struct_0_x1205_x1505_1737683825}

[[认证失败，用户口令错误]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1405913457}

[[Authentication failed, unexpected user service type *service1* (expected = *service2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_327792455}

[[认证失败，]{style="font-family:宋体"}*[service1]{lang="EN-US"}*]{#struct_0_x1205_x1505_579599823}[不是期望的服务类型，期望的服务类型是]{style="font-family:宋体"}*[service2]{lang="EN-US"}*

[[Authorization succeeded.]{lang="EN-US"}]{#struct_0_x1205_x1505_x262561334}

[[授权成功]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x117074497}

[[Authorization failed, user *user-name* doesn\'t exist. ]{lang="EN-US"}]{#struct_0_x1205_x1505_327726919}

[[授权失败，用户]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*]{#struct_0_x1205_x1505_219878103}[不存在]{style="font-family:宋体"}

[[Authorization failed, the user\'s state is block]{lang="EN-US"}]{#struct_0_x1205_x1505_1755043699}

[[授权失败，用户的状态是阻塞]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1877293256}

[[Authorization failed, unexpected user service type *service1* (expected = *service2*).]{lang="EN-US"}]{#struct_0_x1205_x1505_327661383}

[[授权失败，]{style="font-family:宋体"}*[service1]{lang="EN-US"}*]{#struct_0_x1205_x1505_1770692963}[不是期望的服务类型，期望的服务类型是]{style="font-family:宋体"}*[service2]{lang="EN-US"}*

[[Received authentication request message.]{lang="EN-US"}]{#struct_0_x1205_x1505_1256398324}

[[收到认证请求消息]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x382350834}

[[Received authorization request message.]{lang="EN-US"}]{#struct_0_x1205_x1505_327595847}

[[收到授权请求消息]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1487177357}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_188863785}

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_737727740}[在设备上配置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[类型的本地用户]{style="font-family:宋体"}[test]{lang="EN-US"}[，对其使用本地认证方案进行身份认证，并打开]{style="font-family:宋体"}[Local-Server]{lang="EN-US"}[的事件调试信息开关。当用户]{style="font-family:宋体"}[test]{lang="EN-US"}[使用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[登录设备时，设备上输出如下调试信息：]{style="font-family:宋体"}

[[\<Sysname\> debugging local-server event]{lang="EN-US"}]{#struct_0_x1205_x1505_1140220486}

[\*Jun 11 15:30:20:805 2011 Sysname LOCALSRV/7/EVENT: -MDC=1;]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x2080357360}*[本地服务器接受到认证请求消息]{style="font-family:宋体"}*

[[ Received authentication request message.]{lang="EN-US"}]{#struct_0_x1205_x1505_327530311}

[\*Jun 11 15:30:20:805 2011 Sysname LOCALSRV/7/EVENT: -MDC=1;]{lang="EN-US"}

[ Authentication succeeded.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1475453120}*[认证成功]{style="font-family:宋体"}*

[[\*Jun 11 15:30:20:806 2011 Sysname LOCALSRV/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1205_x1505_1342482720}

[ Received authorization request message.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x418620898}*[本地服务器接收到授权请求消息]{style="font-family:宋体"}*

[[\*Jun 11 15:30:20:806 2011 Sysname LOCALSRV/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1205_x1505_x894971162}

[ Authorization succeeded.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x346115607}*[授权成功]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_884191994}[在设备上配置]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[类型的本地用户]{style="font-family:宋体"}[test]{lang="EN-US"}[，对其使用本地认证方案进行身份认证，并打开]{style="font-family:宋体"}[Local-Server]{lang="EN-US"}[的错误调试信息开关。当用户]{style="font-family:宋体"}[test]{lang="EN-US"}[使用]{style="font-family:宋体"}[SSH]{lang="EN-US"}[登录设备时，设备解析认证属性失败，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging local-server error]{lang="EN-US"}]{#struct_0_x1205_x1505_327464775}

[\*Jun 11 15:33:21:002 2011 Sysname LOCALSRV/7/ERROR: -MDC=1;]{lang="EN-US"}

[  Authentication request processing error: Failed to parse authentication attribute.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x521899055}*[解析认证属性失败]{style="font-family:宋体"}*

::: {#1361744731 .myid}
[]{#_Toc404792150}[]{#struct_0_x1205_x1505_x1770775733}[]{#_Toc205709436}

**AAA调试命令 \-- AAA调试命令 \-- debugging radius**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x259748432}

[**[debugging radius ]{lang="SV"}**]{#struct_0_x1205_x1505_1819580295}[{ **all** \| **event** \| **error** \| **packet** } ]{lang="SV"}[\[ **acl** *acl-number* \| **user** *username* \]]{lang="EN-US"}

[**[undo debugging radius ]{lang="SV"}**]{#struct_0_x1205_x1505_x455736181}[{ **all** \| **event** \| **error** \| **packet** }]{lang="SV"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x310429934}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1161952549}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x912709193}

[[1]{lang="EN-US"}]{#struct_0_x1205_x1505_327399239}[：监控级]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x755886947}

[**[all]{lang="EN-US"}**]{#struct_0_x1205_x1505_2126198630}[：所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1205_x1505_1245367251}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1205_x1505_x314835729}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1205_x1505_x1045942028}[：表示报文调试信息开关。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_x1205_x1505_2040856553}[：指定匹配]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[调试信息的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。该参数可多次设置，但仅最后一次合法的配置生效。指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中仅源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址信息用于匹配用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[，其他信息不做匹配项。]{style="font-family:宋体"}

[**[user ]{lang="EN-US"}***[username]{lang="EN-US"}*]{#struct_0_x1205_x1505_1259961008}[：指定匹配]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[调试信息的部分用户名。其中，]{style="font-family:宋体"}*[username]{lang="EN-US"}*[表示部分用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。该参数用于匹配上线用户的完整用户名中的部分连续字符串。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x563996280}

[**[debugging radius]{lang="EN-US"}**]{#struct_0_x1205_x1505_x2046370478}[命令用来打开]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging radius]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x2042939214}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging radius event]{lang="EN-US"}]{#struct_0_x1205_x1505_327333703}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_194904187}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1583444778}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1352251048}

[[Processing AAA request data.]{lang="EN-US"}]{#struct_0_x1205_x1505_2053098894}

[[处理]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_x1205_x1505_52936033}[请求数据]{style="font-family:宋体"}

[[Got request data successfully, primitive: *primitive_name*.]{lang="EN-US"}]{#struct_0_x1205_x1505_1640032929}

[[成功获取请求数据，原语是]{style="font-family:宋体"}*[primitive_name]{lang="EN-US"}*]{#struct_0_x1205_x1505_328316743}

[[Getting local server info.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1023226715}

[[获取本地服务器信息]{style="font-family:宋体"}]{#struct_0_x1205_x1505_17034260}

[[Getting RADIUS server info.]{lang="EN-US"}]{#struct_0_x1205_x1505_1247214943}

[[获取远端]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1492480432}[服务器信息]{style="font-family:宋体"}

[[Got RADIUS server info successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1788323798}

[[成功获取服务器信息]{style="font-family:宋体"}]{#struct_0_x1205_x1505_328251207}

[[Sent request packet and create request context successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_970032670}

[[成功发送请求报文并创建请求上下文]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1163537226}

[[Added request context to global table successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_987661156}

[[成功将请求上下文加入全局上下文信息表]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1590091212}

[[Created request context successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_327792452}

[[成功创建请求上下文]{style="font-family:宋体"}]{#struct_0_x1205_x1505_579599820}

[[Composed request packet successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x262561335}

[[成功构建请求报文]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x117140033}

[[Created response timeout timer successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_2127352345}

[[成功创建应答超时定时器]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327726916}

[[Sent request packet successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_219878094}

[[成功发送请求报文]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x238007279}

[[Created request packet successfully, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id.*]{lang="EN-US"}]{#struct_0_x1205_x1505_1755218907}

[[成功创建请求报文，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1205_x1505_1652345386}[地址是]{style="font-family:宋体"}*[dst-ip]{lang="EN-US"}*[，目的端口是]{style="font-family:宋体"}*[dst-port]{lang="EN-US"}*[，套接字是]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Added packet socketfd to epoll successfully, socketFd: *fd*.]{lang="EN-US"}]{#struct_0_x1205_x1505_327661380}

[[成功添加报文套接字到]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x1205_x1505_1770692962}[控制变量中，套接字是]{style="font-family:宋体"}*[fd]{lang="EN-US"}*

[[Mapped PAM item to RADIUS attribute successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_1256463860}

[[成功将]{style="font-family:宋体"}[PAM]{lang="EN-US"}]{#struct_0_x1205_x1505_x275921222}[数据项映射为]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Filled RADIUS attributes in packet successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_327595844}

[[成功填充]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1487177354}[报文属性]{style="font-family:宋体"}

[[Got RADIUS username format successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_188929321}

[[成功获取]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1929247976}[用户名格式]{style="font-family:宋体"}

[[Added attribute user-name successfully, user-name: *name*.]{lang="EN-US"}]{#struct_0_x1205_x1505_327530308}

[[成功添加用户名属性，属性值是]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x1205_x1505_x480862009}

[[Response timed out.]{lang="EN-US"}]{#struct_0_x1205_x1505_564223032}

[[应答超时]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1453798161}

[[Found request context, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id*.]{lang="EN-US"}]{#struct_0_x1205_x1505_327464772}

[[成功查找到请求上下文，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1205_x1505_x521899056}[地址是]{style="font-family:宋体"}*[dst-ip]{lang="EN-US"}*[，目的端口是]{style="font-family:宋体"}*[dst-port]{lang="EN-US"}*[，套接字是]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Retransmitting request packet, currentTries: *n*, maxTries: *max*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1770579125}

[[重传请求报文，当前是第]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1205_x1505_1617971540}[次重传，最大重传次数是]{style="font-family:宋体"}*[max]{lang="EN-US"}*

[[Sent reply error message to PAM.]{lang="EN-US"}]{#struct_0_x1205_x1505_327399236}

[[发送应答错误消息给]{style="font-family:宋体"}[PAM]{lang="EN-US"}]{#struct_0_x1205_x1505_x755886950}

[[Reached the maximum retries.]{lang="EN-US"}]{#struct_0_x1205_x1505_2126264167}

[[达到最大重传次数]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327333700}

[[Sent packet to next server successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_1583444779}

[[成功发送报文到下一个服务器]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1352185512}

[[Failed to get next server.]{lang="EN-US"}]{#struct_0_x1205_x1505_1903430918}

[[获取下一个服务器失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_328316740}

[[Got next server successfully, serverIP: *svr-ip*, serverPort: *svr-port*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1023226718}

[[成功获取下一个服务器，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1205_x1505_776549147}[地址为]{style="font-family:宋体"}*[svr-ip]{lang="EN-US"}*[，服务器端口为]{style="font-family:宋体"}*[svr-port]{lang="EN-US"}*

[[Set status of server to block successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_328251204}

[[成功将服务器状态设置为阻塞]{style="font-family:宋体"}]{#struct_0_x1205_x1505_970032667}

[[Set status of server to active successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1175114933}

[[成功将服务器状态设置为激活]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327792453}

[[Reply SocketFd recieved EPOLLIN event.]{lang="EN-US"}]{#struct_0_x1205_x1505_579599821}

[[应答报文套接字接收到]{style="font-family:宋体"}[EPOLLIN]{lang="EN-US"}]{#struct_0_x1205_x1505_x262561336}[事件]{style="font-family:宋体"}

[[Reply SocketFd recieved EPOLLERR/EPOLLHUP event.]{lang="EN-US"}]{#struct_0_x1205_x1505_327726917}

[[应答报文套接字接收到]{style="font-family:宋体"}[EPOLLERR/EPOLLHUP]{lang="EN-US"}]{#struct_0_x1205_x1505_219878093}[事件]{style="font-family:宋体"}

[[Sent reply message successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x238007282}

[[成功发送应答消息]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327661381}

[[Received reply packet succuessfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_1770692961}

[[成功接收应答报文]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1256529396}

[[Found request context, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id*.]{lang="EN-US"}]{#struct_0_x1205_x1505_327595845}

[[成功查找到请求上下文，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1205_x1505_1487177355}[地址是]{style="font-family:宋体"}*[dst-ip]{lang="EN-US"}*[，目的端口是]{style="font-family:宋体"}*[dst-port]{lang="EN-US"}*[，套接字是]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[The reply packet is valid.]{lang="EN-US"}]{#struct_0_x1205_x1505_188994857}

[[应答报文有效]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327530309}

[[Decoded reply packet successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x480862008}

[[应答报文解码成功]{style="font-family:宋体"}]{#struct_0_x1205_x1505_564288568}

[[PAM_RADIUS: Processing RADIUS authentication.]{lang="EN-US"}]{#struct_0_x1205_x1505_327464773}

[[进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x521899057}[认证]{style="font-family:宋体"}

[[PAM_RADIUS: Processing RADIUS authorization.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1770644661}

[[进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_327399237}[授权]{style="font-family:宋体"}

[[PAM_RADIUS: RADIUS authorization successful.]{lang="EN-US"}]{#struct_0_x1205_x1505_x755886949}

[[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_327333701}[授权成功]{style="font-family:宋体"}

[[PAM_RADIUS: RADIUS accounting started.]{lang="EN-US"}]{#struct_0_x1205_x1505_1583444780}

[[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1351726751}[计费开始]{style="font-family:宋体"}

[[PAM_RADIUS: RADIUS accounting stopped.]{lang="EN-US"}]{#struct_0_x1205_x1505_328316741}

[[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1023226717}[计费结束]{style="font-family:宋体"}

[[PAM_RADIUS: RADIUS accounting updated.]{lang="EN-US"}]{#struct_0_x1205_x1505_328251205}

[[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_970032668}[计费更新]{style="font-family:宋体"}

[[PAM_RADIUS: Sent *type* request successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1175114926}

[[成功发送认证]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1205_x1505_327792450}[授权]{style="font-family:宋体"}[/]{lang="EN-US"}[计费请求]{style="font-family:宋体"}

[[PAM_RADIUS: Received authentication reply message, resultCode: *code*.]{lang="EN-US"}]{#struct_0_x1205_x1505_579599818}

[[接收到认证应答消息，结果码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x1205_x1505_327726914}

[[PAM_RADIUS: Received authorization reply message, resultCode: *code*.]{lang="EN-US"}]{#struct_0_x1205_x1505_219878092}

[[接收到授权应答消息，结果码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x1205_x1505_x238007281}

[[PAM_RADIUS: Received accounting-start reply message, resultCode: *code*.]{lang="EN-US"}]{#struct_0_x1205_x1505_327661378}

[[接收到计费开始应答消息，结果码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1804230310}

[[PAM_RADIUS: Received accounting-stop reply message, resultCode: *code*.]{lang="EN-US"}]{#struct_0_x1205_x1505_327595842}

[[接收到计费停止应答消息，结果码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x1205_x1505_1487177352}

[[PAM_RADIUS: Received accounting-update reply message, resultCode: *code*.]{lang="EN-US"}]{#struct_0_x1205_x1505_188536105}

[[接收到计费更新应答消息，结果码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x1205_x1505_327530306}

[[Processed session-control packet successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x480862023}

[[处理]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_327464770}[报文成功]{style="font-family:宋体"}

[[Processed session-control message successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x521899058}

[[处理]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_327399234}[消息成功]{style="font-family:宋体"}

[[Sent session-control reply packet successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x755886952}

[[成功发送]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_327333698}[应答报文]{style="font-family:宋体"}

[[Sent DAE reply packet successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_2041315305}

[[成功发送]{style="font-family:宋体"}[DAE ]{lang="EN-US"}]{#struct_0_x1205_x1505_2041380841}[应答报文]{style="font-family:宋体"}

[[Received DAE request packet successfully.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1872808274}

[[成功接收]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_2040791014}[请求报文]{style="font-family:宋体"}

[[Failed to distinguish DAE request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_2040856550}

[[识别]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_1259764400}[请求报文失败]{style="font-family:宋体"}

[[The length of DAE request packet is invalid.]{lang="EN-US"}]{#struct_0_x1205_x1505_2040659942}

[[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_x1521200882}[请求报文长度无效]{style="font-family:宋体"}

[[The type of DAE request packet is unknown.]{lang="EN-US"}]{#struct_0_x1205_x1505_2040725478}

[[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_2041053158}[请求报文类型未知]{style="font-family:宋体"}

[[The authenticator of DAE request packet is invalid.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1109867841}

[[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_2041118694}[请求报文校验字无效]{style="font-family:宋体"}

[[Created detection request packet successfully, dstIP: *dst-ip*, dstPort: *dst-port*, VPN instance: *vpn-instance*, socketFd: *fd*, pktID: *id*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x354493485}

[[成功创建探测请求报文，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1205_x1505_2040922086}[地址是]{style="font-family:宋体"}*[dst-ip]{lang="EN-US"}*[，目的端口是]{style="font-family:宋体"}*[dst-port]{lang="EN-US"}*[，]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*[，套接字是]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Found detection request context, dstIP: *dst-ip*, dstPort: *dst-port*, pktID: *id*.]{lang="EN-US"}]{#struct_0_x1205_x1505_2040791015}

[[成功查找到探测请求上下文，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1205_x1505_1599253456}[地址是]{style="font-family:宋体"}*[dst-ip]{lang="EN-US"}*[，目的端口是]{style="font-family:宋体"}*[dst-port]{lang="EN-US"}*[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Opened RADIUS server detection successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_2040856551}

[[成功开启]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_2040659943}[服务器探测，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to open RADIUS server detection, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_2040725479}

[[开启]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_2041053159}[服务器探测失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Created detection request context successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x1109802305}

[[成功创建探测请求上下文，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_2041118695}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to create detection request context, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_2040922087}

[[创建探测请求上下文失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_2018069710}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Composed detection request packet successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_2040987623}

[[成功构建探测请求报文，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_2041315303}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Sent detection request packet successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x1880958751}

[[成功发送探测请求报文，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_2041380839}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to send detection request packet, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x688092337}

[[发送探测请求报文失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x537044270}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to save  packet ID of detection request, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x688026801}

[[保存探测请求报文]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1205_x1505_x688223409}[失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Random timer of server detection timed out, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x506802260}

[[服务器探测的随机定时器超时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x688157873}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to clear flag of sending trap, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x180379084}

[[清除发送]{style="font-family:宋体"}[trap]{lang="EN-US"}]{#struct_0_x1205_x1505_x687830193}[标记失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to clear count of block state, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x687764657}

[[清除]{style="font-family:宋体"}[block]{lang="EN-US"}]{#struct_0_x1205_x1505_64558971}[状态计数失败，]{style="font-family:宋体"}[ RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to update count of block state, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x687961265}

[[更新]{style="font-family:宋体"}[block]{lang="EN-US"}]{#struct_0_x1205_x1505_x687895729}[状态计数失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[No detection reply packet received, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_424053878}

[[没有接收到探测应答报文，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x687568049}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Server detection timer timed out, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x687502513}

[[服务器探测定时器超时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1098163309}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Sent trap successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x688092336}

[[发送]{style="font-family:宋体"}[trap]{lang="EN-US"}]{#struct_0_x1205_x1505_x688026800}[成功，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to set flag of sending trap, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_1383476539}

[[设置发送]{style="font-family:宋体"}[trap]{lang="EN-US"}]{#struct_0_x1205_x1505_x688223408}[标记失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Closed RADIUS server detection successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x688157872}

[[成功关闭]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x180444620}[服务器探测，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to close RADIUS server detection, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x687830192}

[[关闭]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x687764656}[服务器探测失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Can't open RADIUS server detection because the specified test profile doesn\'t exist, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_64624507}

[[不能开启]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x687961264}[服务器探测，指定的探测模版不存在，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Opened RADIUS server quiet function successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x687895728}

[[成功开启]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_423988342}[服务器静默，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to open RADIUS server quiet function,  RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x687568048}

[[开启]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x687502512}[服务器静默失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Closed RADIUS server quiet function successfully, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x1098097773}

[[成功关闭]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x688092339}[服务器静默，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to close RADIUS server quiet function, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x688026803}

[[关闭]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1383279931}[服务器静默失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Aaad Sent the notification about the change of server status to application process successfully, server state:*server-state*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x688223411}

[[Aaad]{lang="EN-US"}]{#struct_0_x1205_x1505_x688157875}[发送了服务器状态转换的通知给应用进程，服务器状态是]{style="font-family:宋体"}*[server-state]{lang="EN-US"}*

[[Application process received the notification about the change of server status from aaad process, server state:*server-state*. ]{lang="EN-US"}]{#struct_0_x1205_x1505_x179985868}

[[应用进程接收了来自]{style="font-family:宋体"}[aaad]{lang="EN-US"}]{#struct_0_x1205_x1505_x687830195}[进程的服务器状态转换的通知，服务器状态是]{style="font-family:宋体"}*[server-state]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging radius error]{lang="EN-US"}]{#struct_0_x1205_x1505_444327886}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_214488731}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1513565197}

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_1416896445}

[[Failed to get request data.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1110119081}

[[获取请求数据失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1262768244}

[[Failed to get server info.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1245860201}

[[获取服务器信息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_328316738}

[[Failed to send request packet and create request context.]{lang="EN-US"}]{#struct_0_x1205_x1505_x213922662}

[[发送请求报文和创建请求上下文失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_891283910}

[[Failed to create request context.]{lang="EN-US"}]{#struct_0_x1205_x1505_1283280883}

[[创建请求上下文失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1371240364}

[[Failed to compose request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_328251202}

[[组装请求报文失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_970032673}

[[Failed to create response timeout timer.]{lang="EN-US"}]{#struct_0_x1205_x1505_1163537223}

[[创建应答超时定时器失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_987333476}

[[Failed to send request packet, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id.*]{lang="EN-US"}]{#struct_0_x1205_x1505_1829053852}

[[发送请求报文失败，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1205_x1505_327792451}[地址是]{style="font-family:宋体"}*[dst-ip]{lang="EN-US"}*[，目的端口是]{style="font-family:宋体"}*[dst-port]{lang="EN-US"}*[，套接字是]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Failed to create request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_579599819}

[[创建请求报文失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1311416768}

[[Failed to add packet socketfd to epoll, socketFd: *fd*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x374018603}

[[将报文套接字加入]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x1205_x1505_114121923}[控制变量失败，套接字是]{style="font-family:宋体"}*[fd]{lang="EN-US"}*

[[Failed to map PAM item to attribute.]{lang="EN-US"}]{#struct_0_x1205_x1505_327726915}

[[将]{style="font-family:宋体"}[PAM]{lang="EN-US"}]{#struct_0_x1205_x1505_219878091}[数据项映射到]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[Failed to fill attribute in packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x238007284}

[[填充报文属性失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_1756070870}

[[Failed to get RADIUS username format.]{lang="EN-US"}]{#struct_0_x1205_x1505_327661379}

[[获取]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1804230311}[用户名格式失败]{style="font-family:宋体"}

[[Faild to get domain item.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1986632932}

[[获取]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_x1205_x1505_x1958412744}[域数据项失败]{style="font-family:宋体"}

[[The username length exceeded the upper limt.]{lang="EN-US"}]{#struct_0_x1205_x1505_378771915}

[[用户名长度超过最大值]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327595843}

[[Failed to retransmit request packet *n* times.]{lang="EN-US"}]{#struct_0_x1205_x1505_1487177353}

[[第]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1205_x1505_188601641}[次重发请求报文失败]{style="font-family:宋体"}

[[Failed to set the status of server to active.]{lang="EN-US"}]{#struct_0_x1205_x1505_945381543}

[[设置服务器到激活状态失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327530307}

[[Failed to fill reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_x480862022}

[[填充应答数据失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_564943930}

[[Failed to send reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_1779256520}

[[发送应答消息失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327464771}

[[Failed to recieve reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x521899059}

[[发送应答报文失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1771037877}

[[Failed to find request context, dstIP: *dst-ip*, dstPort: *dst-port*, socketFd: *fd*, pktID: *id*.]{lang="EN-US"}]{#struct_0_x1205_x1505_x316920044}

[[查找请求上下文失败，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1205_x1505_327399235}[地址是]{style="font-family:宋体"}*[dst-ip]{lang="EN-US"}*[，目的端口是]{style="font-family:宋体"}*[dst-port]{lang="EN-US"}*[，套接字是]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[The reply packet is invalid.]{lang="EN-US"}]{#struct_0_x1205_x1505_x755886951}

[[应答报文无效]{style="font-family:宋体"}]{#struct_0_x1205_x1505_2126329703}

[[Failed to decode reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_2046115887}

[[解码应答报文失败]{style="font-family:宋体"}]{#struct_0_x1205_x1505_327333699}

[[Reply packet: Unknown type.]{lang="EN-US"}]{#struct_0_x1205_x1505_444327887}

[[应答报文：未知类型]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x1513565196}

[[Reply packet: Invalid packet length.]{lang="EN-US"}]{#struct_0_x1205_x1505_328316739}

[[应答报文：无效的报文长度]{style="font-family:宋体"}]{#struct_0_x1205_x1505_x213922661}

[[Reply packet: Invalid packet authenticator.]{lang="EN-US"}]{#struct_0_x1205_x1505_891349446}

[[应答报文：无效的报文验证字]{style="font-family:宋体"}]{#struct_0_x1205_x1505_328251203}

[[Failed to map attribute to PAM item.]{lang="EN-US"}]{#struct_0_x1205_x1505_970032674}

[[将]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1163537230}[属性映射成]{style="font-family:宋体"}[PAM]{lang="EN-US"}[数据项失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to set scheme name to pam-module-data.]{lang="EN-US"}]{#struct_0_x1205_x1505_987530085}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1893876395}[：设置方案名称到]{style="font-family:宋体"}[PAM]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[PAM_RADIUS: Local authorization failed.]{lang="EN-US"}]{#struct_0_x1205_x1505_x997900062}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_890644100}[：本地授权失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to get reply data from pam-module-data.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893810859}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x957392984}[：从]{style="font-family:宋体"}[PAM]{lang="EN-US"}[数据获取应答数据失败]{style="font-family:宋体"}

[[PAM_RADIUS: Authorization scheme is RADIUS, but authentication is local.]{lang="EN-US"}]{#struct_0_x1205_x1505_114362618}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1893745323}[：授权方案是]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[，但认证方案是]{style="font-family:宋体"}[local]{lang="EN-US"}

[[PAM_RADIUS: Authorization scheme is different from authentication scheme.]{lang="EN-US"}]{#struct_0_x1205_x1505_1728951839}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x114579628}[：授权方案与认证方案不同]{style="font-family:宋体"}

[[PAM_RADIUS: Authorization failed for setting PAM item.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893679787}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x186302720}[：设置]{style="font-family:宋体"}[PAM]{lang="EN-US"}[数据项失败导致授权失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to find sequence.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893614251}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1780274478}[：查找序列失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to find reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1862847865}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1893548715}[：查找应答数据失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to send *type* request.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1754418381}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x962405556}[：发送认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权]{style="font-family:宋体"}[/]{lang="EN-US"}[计费请求失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to set port item.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893483179}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1353647531}[：设置端口数据项失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to accept connection for receiving *type* reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893417643}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x612184896}[：接收认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权]{style="font-family:宋体"}[/]{lang="EN-US"}[计费应答数据的连接失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to select available socket for receiving *type* reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_1370596476}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1894400683}[：选择可用的套接字失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to receive *type* reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_430921777}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1894335147}[：接收认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权]{style="font-family:宋体"}[/]{lang="EN-US"}[计费应答数据失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to process reply data.]{lang="EN-US"}]{#struct_0_x1205_x1505_1986377373}

[[PAM_RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1120130405}[：处理应答数据失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to open socket when processing *type* request.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893876396}

[[处理认证]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1205_x1505_x998096670}[授权]{style="font-family:宋体"}[/]{lang="EN-US"}[计费请求时，打开套接字失败]{style="font-family:宋体"}

[[PAM_RADIUS: Failed to send *type* request.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893810860}

[[发送认证]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1205_x1505_x957982805}[授权]{style="font-family:宋体"}[/]{lang="EN-US"}[计费请求失败]{style="font-family:宋体"}

[[Failed to process session-control packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1843918408}

[[处理]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_1893745324}[报文失败]{style="font-family:宋体"}

[[Failed to process session-control message.]{lang="EN-US"}]{#struct_0_x1205_x1505_1728886303}

[[处理]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_1893679788}[消息失败]{style="font-family:宋体"}

[[Failed to receive session-control packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x186499328}

[[接收]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_1893614252}[报文失败]{style="font-family:宋体"}

[[Session-control packet is invalid.]{lang="EN-US"}]{#struct_0_x1205_x1505_x1780208942}

[[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_912702361}[报文无效]{style="font-family:宋体"}

[[Checking session-control packet failed.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893548716}

[[检查]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_x1754483917}[报文失败]{style="font-family:宋体"}

[[Failed to decode session-control packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893483180}

[[解码]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_x1353057696}[报文失败]{style="font-family:宋体"}

[[Failed to find attribute hw-command.]{lang="EN-US"}]{#struct_0_x1205_x1505_1893417644}

[[查找]{style="font-family:宋体"}[hw-command]{lang="EN-US"}]{#struct_0_x1205_x1505_x612643648}[属性失败]{style="font-family:宋体"}

[[Failed to send session-control message to aaad.]{lang="EN-US"}]{#struct_0_x1205_x1505_1894400684}

[[向]{style="font-family:宋体"}[aaad]{lang="EN-US"}]{#struct_0_x1205_x1505_431380529}[发送]{style="font-family:宋体"}[session-control]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[[Failed to decode session-control reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_669011076}

[[解码]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_1894335148}[应答消息失败]{style="font-family:宋体"}

[[Failed to send session-control reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_1986705053}

[[发送]{style="font-family:宋体"}[session-control]{lang="EN-US"}]{#struct_0_x1205_x1505_1893876393}[应答报文失败]{style="font-family:宋体"}

[[Failed to send DAE reply packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x688157874}

[[发送]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_x687830194}[应答报文失败]{style="font-family:宋体"}

[[Failed to decode DAE reply message.]{lang="EN-US"}]{#struct_0_x1205_x1505_x687764658}

[[解码]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_63969147}[应答报文失败]{style="font-family:宋体"}

[[Failed to receive DAE request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_x687961266}

[[接收]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_x687895730}[请求报文失败]{style="font-family:宋体"}

[[Failed to decode DAE request packet.]{lang="EN-US"}]{#struct_0_x1205_x1505_424512631}

[[解码]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1205_x1505_x687568050}[请求报文失败]{style="font-family:宋体"}

[[Failed to send server state notify message for multi RADIUS scheme name.]{lang="EN-US"}]{#struct_0_x1205_x1505_x687502514}

[[发送多个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x1098490989}[方案名称的]{style="font-family:宋体"}[server state]{lang="EN-US"}[通知消息失败。]{style="font-family:宋体"}

[[Failed to send server state notify message for single RADIUS scheme name, RADIUS scheme name: scheme-name.]{lang="EN-US"}]{#struct_0_x1205_x1505_x688092341}

[[发送单个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x688026805}[方案名称的]{style="font-family:宋体"}[server state]{lang="EN-US"}[通知消息失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名称]{style="font-family:宋体"}[: scheme-name]{lang="EN-US"}[。]{style="font-family:宋体"}

[[Failed to create detection request packet, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x688157877}

[[创建探测请求报文失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x180116940}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to fill RADIUS attributes in detection request  packet, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_x687830197}

[[向探测请求报文中填充]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x687764661}[报文属性失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[[Failed to get NAS-IP, RADIUS scheme name:*scheme-name*, server IP:*server-ip*, server port:*server-port*, VPN instance: *vpn-instance.*]{lang="EN-US"}]{#struct_0_x1205_x1505_64427898}

[[获取]{style="font-family:宋体"}[NAS-IP]{lang="EN-US"}]{#struct_0_x1205_x1505_x687961269}[失败，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名是]{style="font-family:宋体"}*[scheme-name]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[，服务器端口号是]{style="font-family:宋体"}*[server-port]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="FR"}[实例是]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging radius packet]{lang="EN-US"}]{#struct_0_x1205_x1505_x687568053}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_204855899}[[字段]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x279084679}

[[描述]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x414329852}

[[RADIUS attribute name = *attribute value*]{lang="EN-US"}]{#struct_0_x1205_x1505_1397359230}

[[报文中包含的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_1893810857}[属性及其取值。]{style="font-family:宋体"}

[[其中]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x1205_x1505_x958048344}[属性遵从]{style="font-family:宋体"}[RFC2865/2866/2869/3580]{lang="EN-US"}[描述，不再赘述；另外还支持一些厂商定制属性（]{style="font-family:宋体"}[Vender Specific Attribute]{lang="EN-US"}[），在下面单独描述]{style="font-family:宋体"}

[[3Com-User-Access-Level = *level*]{lang="EN-US"}]{#struct_0_x1205_x1505_x108292487}

[[3Com]{lang="EN-US"}]{#struct_0_x1205_x1505_x1304623230}[用户访问级别为]{style="font-family:宋体"}*[level]{lang="EN-US"}*[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}

[[H3c-Ftp-Directory = *dir*]{lang="EN-US"}]{#struct_0_x1205_x1505_x1179269668}

[[H3c-Ftp]{lang="EN-US"}]{#struct_0_x1205_x1505_1700235078}[用户工作路径为]{style="font-family:宋体"}*[dir]{lang="EN-US"}*

[[H3c-Exec-Privilege = *level*]{lang="EN-US"}]{#struct_0_x1205_x1505_1893745321}

[[H3c-Exec]{lang="EN-US"}]{#struct_0_x1205_x1505_1729082911}[用户访问级别为]{style="font-family:宋体"}*[level]{lang="EN-US"}*[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}

[[Hw-Ftp-Directory = *dir*]{lang="EN-US"}]{#struct_0_x1205_x1505_1090526486}

[[H3c-Ftp]{lang="EN-US"}]{#struct_0_x1205_x1505_x588037816}[用户工作路径为]{style="font-family:宋体"}*[dir]{lang="EN-US"}*

[[Hw-Exec-Privilege = *level*]{lang="EN-US"}]{#struct_0_x1205_x1505_x256400937}

[[Hw-Exec]{lang="EN-US"}]{#struct_0_x1205_x1505_1893679785}[用户访问级别为]{style="font-family:宋体"}*[level]{lang="EN-US"}*[，取值为]{style="font-family:宋体"}[ 0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}

[[H3c-Local-Service-Type = *type*]{lang="EN-US"}]{#struct_0_x1205_x1505_x186171648}

[[Type]{lang="EN-US"}]{#struct_0_x1205_x1505_x2121877250}[取值及其涵义为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1205_x1505_x1455565468}[：]{lang="EN-US" style="font-family:
  宋体"}[DVPN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1205_x1505_x2018204299}[：]{lang="EN-US" style="font-family:
  宋体"}[FTP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x1205_x1505_1893614249}[：网络接入类型（]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x1205_x1505_x1779750189}[：]{lang="EN-US" style="font-family:
  宋体"}[PAD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x1205_x1505_872877333}[：]{lang="EN-US" style="font-family:
  宋体"}[SSH]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x1205_x1505_1470409525}[：]{lang="EN-US" style="font-family:
  宋体"}[Telnet]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x1205_x1505_x1885398254}[：]{lang="EN-US" style="font-family:
  宋体"}[Terminal]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_x1205_x1505_1893548713}[：]{lang="EN-US" style="font-family:
  宋体"}[Portal]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_x1205_x1505_x1754287309}[：]{lang="EN-US" style="font-family:
  宋体"}[PPP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_x1205_x1505_x1063831471}[：]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[11]{lang="EN-US"}]{#struct_0_x1205_x1505_x1095516933}[：命令行]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1205_x1505_x1043638115}

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_1893483177}[在一台设备上配置]{style="font-family:宋体"}[Login]{lang="EN-US"}[用户的认证方案为]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证、授权，并打开]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[事件调试信息开关。当有一个]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户登录本设备时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging radius event]{lang="EN-US"}]{#struct_0_x1205_x1505_x1352992171}

[\*Dec 31 16:04:36:438 2009 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[PAM_RADIUS: Processing RADIUS authentication.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_877816244}*[进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:660 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1056978920}

[PAM_RADIUS: Sent authentication request successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x2147235648}*[成功发送认证请求]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:667 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x1069524234}

[Processing AAA request data.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_494547247}*[处理]{style="font-family:宋体"}[AAA]{lang="EN-US"}[请求数据]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:667 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1893417641}

[Got request data successfully, primitive: authentication.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x612315968}*[成功接收到用户的认证请求，原语是认证]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:668 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1002582054}

[Getting RADIUS server info.]{lang="EN-US"}

[\*Jan  3 02:17:27:669 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Got RADIUS server info successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1457505778}*[成功获取]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器信息]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:669 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_717261796}

[Created request context successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1533043040}*[成功创建请求上下文]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:670 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x524711495}

[Created request packet successfully, dstIP: 192.168.0.244, dstPort: 1812, VPN in]{lang="EN-US"}

[stance: \--(public), socketFd: 23, pktID: 61.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1894400681}*[成功创建认证请求报文，目的地址是]{style="font-family:宋体"}[192.168.0.244]{lang="EN-US"}[，目的端口是]{style="font-family:宋体"}[1812]{lang="EN-US"}[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例是]{style="font-family:宋体"}[public]{lang="EN-US"}[，套接字是]{style="font-family:宋体"}[23]{lang="EN-US"}[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[61]{lang="EN-US"}*

[[\*Jan  3 02:17:27:671 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_431052849}

[Added packet socketfd to epoll successfully, socketFd: 23.]{lang="EN-US"}

[\*Jan  3 02:17:27:672 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Mapped PAM item to RADIUS attribute successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x9923308}*[成功将]{style="font-family:宋体"}[PAM]{lang="EN-US"}[数据项映射为]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[属性]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:673 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1657620327}

[Got RADIUS username format successfully, format: 2.]{lang="EN-US"}

[\*Jan  3 02:17:27:674 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Added attribute user-name successfully, user-name: test.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1364122420}*[成功添加用户名属性，属性值是]{style="font-family:宋体"}[test]{lang="EN-US"}*

[[\*Jan  3 02:17:27:674 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1886272121}

[Filled RADIUS attributes in packet successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1894335145}*[成功填充报文属性，并构建认证请求报文]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:675 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1986508445}

[Composed request packet successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:675 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Created response timeout timer successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x788409869}*[成功创建应答超时定时器]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:679 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x1915153230}

[Sent request packet successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:679 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Sent request packet and create request context successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1923777414}*[成功发送认证请求报文，并创建请求上下文]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:680 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x1454981403}

[Added request context to global table successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_2017179131}*[成功将请求上下文加入全局上下文信息表]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:714 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1893876394}

[Reply SocketFd recieved EPOLLIN event.]{lang="EN-US"}

[\*Jan  3 02:17:27:715 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Received reply packet succuessfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x997965598}*[接收到应答报文]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:716 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1675330660}

[Found request context, dstIP: 192.168.0.244, dstPort: 1812, VPN instance: \--(pub]{lang="EN-US"}

[lic), socketFd: 23, pktID: 61.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1952199979}*[查找到请求上下文]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:717 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x797289166}

[The reply packet is valid.]{lang="EN-US"}

[\*Jan  3 02:17:27:718 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Decoded reply packet successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1144517623}*[应答报文有效，对应答报文解码成功]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:719 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1893810858}

[Sent reply message successfully.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x1205_x1505_x957458520}*[成功发送应答消息]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:719 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x684746909}

[PAM_RADIUS: Fetched authentication reply-data successfully, resultCode: 0]{lang="EN-US"}

[\*Jan  3 02:17:27:720 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[PAM_RADIUS: Received authentication reply message, resultCode: 0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x198693310}*[收到认证应答消息]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:721 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x1749628779}

[PAM_RADIUS: Processing RADIUS authorization.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1170912105}*[开始进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:724 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x1097917162}

[PAM_RADIUS: RADIUS Authorization successfully.]{lang="EN-US"}

[*[// RADIUS]{lang="EN-US"}*]{#struct_0_x1205_x1505_1893745322}*[授权请求成功]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:743 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1729017375}

[PAM_RADIUS: RADIUS accounting started.]{lang="EN-US"}

[*[// RADIUS]{lang="EN-US"}*]{#struct_0_x1205_x1505_323272523}*[计费开始]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:744 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_225232308}

[Processing AAA request data.]{lang="EN-US"}

[\*Jan  3 02:17:27:744 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[PAM_RADIUS: Sent accounting-start request successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:744 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Got request data successfully, primitive: accounting-start.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_723368484}*[成功获取计费请求数据，原语是开始计费]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:745 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1804806143}

[Getting RADIUS server info.]{lang="EN-US"}

[\*Jan  3 02:17:27:745 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Got RADIUS server info successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1893679786}*[成功获取服务器信息]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:746 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x186368256}

[Created request context successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:747 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Created request packet successfully, dstIP: 192.168.0.244, dstPort: 1813, VPN in]{lang="EN-US"}

[stance: \--(public), socketFd: 23, pktID: 184.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1670471754}*[成功创建计费开始请求报文，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[192.168.0.244]{lang="EN-US"}[，目的端口号是]{style="font-family:宋体"}[1813]{lang="EN-US"}[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例是]{style="font-family:宋体"}[public]{lang="EN-US"}[，套接字是]{style="font-family:宋体"}[23]{lang="EN-US"}[，报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[184]{lang="EN-US"}*

[[\*Jan  3 02:17:27:747 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x397157358}

[Added packet socketfd to epoll successfully, socketFd: 23.]{lang="EN-US"}

[\*Jan  3 02:17:27:749 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Mapped PAM item to RADIUS attribute successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:749 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Got RADIUS username format successfully, format: 2.]{lang="EN-US"}

[\*Jan  3 02:17:27:750 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Added attribute user-name successfully, user-name: test.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_262249018}*[成功添加用户名属性，属性值是]{style="font-family:宋体"}[test]{lang="EN-US"}*

[[\*Jan  3 02:17:27:751 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_1893614250}

[Filled RADIUS attributes in packet successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:751 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Composed request packet successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1780340014}*[成功填充报文属性，并构建请求报文]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:752 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x1739358492}

[Created response timeout timer successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_201009452}*[成功创建应答超时定时器]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:754 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_344836882}

[Sent request packet successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:754 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Sent request packet and create request context successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:755 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Added request context to global table successfully.]{lang="EN-US"}

[\*Jan  3 02:17:27:755 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Reply SocketFd recieved EPOLLIN event.]{lang="EN-US"}

[\*Jan  3 02:17:27:756 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Received reply packet succuessfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1893548714}*[成功接收到计费应答报文]{style="font-family:宋体"}*

[[\*Jan  3 02:17:27:757 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_x1754352845}

[Found request context, dstIP: 192.168.0.244, dstPort: 1813, VPN instance: \--(pub]{lang="EN-US"}

[lic), socketFd: 23, pktID: 184.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1958921653}*[成功查找到计费应答报文对应的请求上下文，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[192.168.0.244]{lang="EN-US"}[；目的端口号是]{style="font-family:宋体"}[1646]{lang="EN-US"}[；套接字是]{style="font-family:宋体"}[14]{lang="EN-US"}[；报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Jan  3 02:17:27:758 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}]{#struct_0_x1205_x1505_221446040}

[The reply packet is valid.]{lang="EN-US"}

[\*Jan  3 02:17:27:759 2011 Sysname RADIUS/7/EVENT:]{lang="EN-US"}

[Decoded reply packet successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1908537640}*[计费应答报文有效，对计费应答报文解码成功]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_x402292460}[在一台设备上配置]{style="font-family:宋体"}[Login]{lang="EN-US"}[用户的认证方案为]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证、授权、计费，并打开]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文调试信息开关。当有一个]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户登录本设备时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging radius packet]{lang="EN-US"}]{#struct_0_x1205_x1505_1893483178}

[\*Jan  3 02:33:18:686 2011 Sysname RADIUS/7/PACKET:]{lang="EN-US"}

[    User-Name=\"rbac\"]{lang="EN-US"}

[    User-Password=\*\*\*\*\*\*]{lang="EN-US"}

[    Service-Type=Login-User]{lang="EN-US"}

[    Framed-IP-Address=192.168.0.17]{lang="EN-US"}

[    NAS-IP-Address=192.168.0.16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1353581995}*[认证请求报文中的属性列表]{style="font-family:宋体"}*

[[\*Jan  3 02:33:18:690 2011 Sysname RADIUS/7/PACKET:]{lang="EN-US"}]{#struct_0_x1205_x1505_864780784}

[ 01 ed 00 3e 44 13 50 f2 54 58 6f e8 39 e9 05 ff]{lang="EN-US"}

[ 6c 7e 18 a3 01 06 72 62 61 63 02 12 71 a1 e1 46]{lang="EN-US"}

[ cc a2 77 97 a4 95 57 54 db f6 3b 0b 06 06 00 00]{lang="EN-US"}

[ 00 01 08 06 c0 a8 00 11 04 06 c0 a8 00 10]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_815732579}*[发送的]{style="font-family:宋体"}[access-request]{lang="EN-US"}[报文原始信息]{style="font-family:宋体"}*

[[\*Jan  3 02:33:18:707 2011 Sysname RADIUS/7/PACKET:]{lang="EN-US"}]{#struct_0_x1205_x1505_1622407163}

[    Service-Type=Login-User]{lang="EN-US"}

[    Session-Timeout=86400]{lang="EN-US"}

[    Login-Service=Telnet]{lang="EN-US"}

[*[// access-accept]{lang="EN-US"}*]{#struct_0_x1205_x1505_x1378369858}*[应答报文的属性列表]{style="font-family:宋体"}[    ]{lang="EN-US"}*

[[\*Jan  3 02:33:18:708 2011 Sysname RADIUS/7/PACKET:]{lang="EN-US"}]{#struct_0_x1205_x1505_1893417642}

[ 02 ed 00 26 71 d9 71 09 75 7b af d9 2d fc 10 59]{lang="EN-US"}

[ 4d ee 66 ae 06 06 00 00 00 01 1b 06 00 01 51 80]{lang="EN-US"}

[ 0f 06 00 00 00 00]{lang="EN-US"}

[*[// access-accept]{lang="EN-US"}*]{#struct_0_x1205_x1505_x612250432}*[报文的原始数据]{style="font-family:宋体"}*

[[\*Jan  3 02:33:18:727 2011 Sysname RADIUS/7/PACKET:]{lang="EN-US"}]{#struct_0_x1205_x1505_x160116231}

[    User-Name=\"rbac\"]{lang="EN-US"}

[    Framed-IP-Address=192.168.0.17]{lang="EN-US"}

[    Acct-Session-Id=\"000000032011-01-03:02:33:18-0000000101\"]{lang="EN-US"}

[    Login-Service=Telnet]{lang="EN-US"}

[    Acct-Authentic=RADIUS]{lang="EN-US"}

[    NAS-IP-Address=192.168.0.16]{lang="EN-US"}

[    Acct-Status-Type=Start]{lang="EN-US"}

[    Acct-Delay-Time=0]{lang="EN-US"}

[    Event-Timestamp=\"Jan  3 2011 02:33:18 UTC\"]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_1497422946}*[计费开始请求报文中的属性列表]{style="font-family:宋体"}*

[[\*Jan  3 02:33:18:729 2011 Sysname RADIUS/7/PACKET:]{lang="EN-US"}]{#struct_0_x1205_x1505_1894400682}

[ 04 3c 00 6c 21 aa 18 4e 38 c8 60 f1 12 76 97 26]{lang="EN-US"}

[ e2 04 d8 28 01 06 72 62 61 63 08 06 c0 a8 00 11]{lang="EN-US"}

[ 2c 28 30 30 30 30 30 30 30 33 32 30 31 31 2d 30]{lang="EN-US"}

[ 31 2d 30 33 3a 30 32 3a 33 33 3a 31 38 2d 30 30]{lang="EN-US"}

[ 30 30 30 30 30 31 30 31 0f 06 00 00 00 00 2d 06]{lang="EN-US"}

[ 00 00 00 01 04 06 c0 a8 00 10 28 06 00 00 00 01]{lang="EN-US"}

[ 29 06 00 00 00 00 37 06 4d 21 35 6e]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_430987313}*[计费开始请求报文原始数据]{style="font-family:宋体"}*

[[\*Jan  3 02:33:18:731 2011 Sysname RADIUS/7/PACKET:]{lang="EN-US"}]{#struct_0_x1205_x1505_513906915}

[ 05 3c 00 14 5f 8f 2f e7 21 86 a7 db 52 b3 39 09]{lang="EN-US"}

[ 86 92 80 b0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_2028024911}*[计费应答报文原始数据]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1205_x1505_2111657204}[在一台设备上配置]{style="font-family:宋体"}[Login]{lang="EN-US"}[用户的认证方案为本地认证、]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，并打开]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[错误调试信息开关。当有一个]{style="font-family:宋体"}[Console]{lang="EN-US"}[用户登录本设备时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging radius error]{lang="NO-BOK"}]{#struct_0_x1205_x1505_133721473}

[\*Dec 31 16:04:41:324 2009 Sysname RADIUS/7/ERROR: ]{lang="EN-US"}

[PAM_RADIUS: Failed to get reply-data from pam-module-data..]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1205_x1505_189416174}*[从]{style="font-family:宋体"}[PAM]{lang="EN-US"}[数据获取应答数据失败]{style="font-family:宋体"}*
